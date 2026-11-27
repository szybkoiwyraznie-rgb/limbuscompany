# Paczka AI P73 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 9/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P73_3c_przeciwnicy_i_anomalie_cz09.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P73_3c_przeciwnicy_i_anomalie_cz09.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c8p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c8p3
- grupa rozdziału/trybu: `a1c8p3` · plik: `Skills_Abnormality-a1c8p3.json`

1. [Umiejętność wroga [114501] (ulepszenie 1) — nazwa] 이연참
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114501].levelList[level=1].name
   limit: do 40 znaków
   EN: Double Slash
   PL:
2. [Umiejętność wroga [114501] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 2)
   PL:
3. [Umiejętność wroga [114501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL:
4. [Umiejętność wroga [114501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
5. [Umiejętność wroga [114502] (ulepszenie 1) — nazwa] 삼연격
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114502].levelList[level=1].name
   limit: do 40 znaków
   EN: Triple Slash
   PL:
6. [Umiejętność wroga [114502] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114502].levelList[level=1].desc
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Umiejętność wroga [114502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
8. [Umiejętność wroga [114502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration] and +2 [Vibration] Count
   PL:
9. [Umiejętność wroga [114502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
10. [Umiejętność wroga [114503] (ulepszenie 1) — nazwa] 이연참-폭[爆]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].name
   limit: do 40 znaków
   EN: Double Slash - Blast [爆]
   PL:
11. [Umiejętność wroga [114503] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 4)\n[DefeatDuel] [BulletPropellant] 1 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [DefeatDuel], [BulletPropellant]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Final Power +1 for every 4 ([Combustion] + [Vibration]) on target (max 4)\n[DefeatDuel] Lose 1 [BulletPropellant]
   PL:
12. [Umiejętność wroga [114503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Umiejętność wroga [114503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend 1 [BulletPropellant]
   PL:
14. [Umiejętność wroga [114503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +2 [Combustion] Count
   PL:
15. [Umiejętność wroga [114503] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114503].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +2 [Vibration] Count
   PL:
16. [Umiejętność wroga [114504] (ulepszenie 1) — nazwa] 삼연격-폭[爆]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].name
   limit: do 40 znaków
   EN: Triple Slash - Blast [爆]
   PL:
17. [Umiejętność wroga [114504] (ulepszenie 1) — opis] 대상의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 4)\n[DefeatDuel] [BulletPropellant] 1 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].desc
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
18. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL:
22. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
24. [Umiejętność wroga [114504] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114504].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] twice; then, reduce target's [Vibration] Count by 2
   PL:
25. [Umiejętność wroga [114505] (ulepszenie 1) — nazwa] 폭쇄참 [爆碎斬]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].name
   limit: do 40 znaków
   EN: Blasting Shatterslash [爆碎斬]
   PL:
26. [Umiejętność wroga [114505] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n대상의 [Combustion]과 [Vibration]의 합 6당 코인 위력 +1 (최대 3)\n[DefeatDuel] 자신의 정신력 10 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [Combustion], [Vibration], [DefeatDuel]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [Prey]\nCan clash with this Skill regardless of Speed\nCoin Power +1 for every 6 ([Combustion] + [Vibration]) on target (max 3)\n[DefeatDuel] Lose 10 SP
   PL:
27. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:
28. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion]
   PL:
30. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 4 부여, [Vibration] 횟수 4 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Vibration] and +4 [Vibration] Count
   PL:
32. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
35. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
36. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 2, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#1].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationIgnition], [Switch_Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [Switch_Vibration] into [VibrationIgnition]
   PL:
37. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 3, efekt 3 — opis] 이 코인 효과로 [BulletPropellant]을 소모하였다면, 피해량 +50%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: If this unit spent [BulletPropellant] due to this Coin's effect, deal +50% damage
   PL:
40. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [Combustion] 3 부여, [Combustion] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 3 [Combustion] and +3 [Combustion] Count
   PL:
41. [Umiejętność wroga [114505] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114505].levelList[level=1].coinlist[#2].coindescs[#4].desc
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Umiejętność wroga [114506] (ulepszenie 1) — nazwa] 쾌도난마 [快刀亂麻]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].name
   limit: do 40 znaków
   EN: Tanglecleaver [快刀亂麻]
   PL:
43. [Umiejętność wroga [114506] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 2)\n- 25일 경우, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 5)\n[DefeatDuel] [ResultReduction] 4 얻음\n[DefeatDuel] [Paralysis] 1 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, [Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소 (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].desc
   limit: do 1040 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [ResultReduction], [Paralysis], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze …
   EN: Prioritizes targets with [Prey]\nCan Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stack , gain Atk Weight +1 for every 10 Stack consumed (max 2)\n- ... 25 Stack, Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 5)\n[DefeatDuel] Gain 4 [ResultReduction]\n[DefeatDuel] Gain 1 [Paralysis]\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[EndSkill] Ends this turn
   PL:
44. [Umiejętność wroga [114506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Umiejętność wroga [114506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 전부 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Spend all [BulletPropellant]
   PL:
46. [Umiejętność wroga [114506] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 소모한 [BulletPropellant]만큼 [Combustion] 부여, [Combustion] 횟수 증가, [Vibration] 부여, [Vibration] 횟수 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BulletPropellant], [Combustion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BulletPropellant] = 호표탄 / Tigermark Round; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict [Combustion], [Combustion] Count, [Vibration], and [Vibration] Count by [BulletPropellant] spent
   PL:
47. [Umiejętność wroga [114506] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Umiejętność wroga [114506] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114506].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 3 times; then, reduce target's [Vibration] Count by 3
   PL:
49. [Umiejętność wroga [114507] (ulepszenie 1) — nazwa] 초절맹호살격난참 [超絕猛虎殺擊亂斬]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].name
   limit: do 80 znaków
   EN: Savage Tigerslayer's Perfected Flurry of Blades [超絕猛虎殺擊亂斬]
   PL:
50. [Umiejętność wroga [114507] (ulepszenie 1) — opis] [Prey]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [BattleSense]을 전부 소모. 소모한 수치가\n- 10 이상이면, 10당 공격 가중치 +1 (최대 4)\n- 25 이상이면, 메인 타겟의 [Combustion]과 [Vibration]의 합 4당 최종 위력 +1 (최대 6)\n- 50일 경우, 코인 위력 +1, 피해량 +50%\n[DefeatDuel] [ResultReduction] 2 얻음\n[DefeatDuel] [Paralysis] 6 얻음\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않으며, [Combustion] 위력과 횟수, [Vibration] 위력과 횟수 부여량이 절반으로 감소 (다른 효과로 증가되는 수치 제외)\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].desc
   limit: do 1100 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [WhenUse], [BattleSense], [Combustion], [Vibration], [DefeatDuel], [ResultReduction], [Paralysis], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [WhenUse] = [사용시] / [On Use]; [BattleSense] = 저력 [底力] / Inner Strength [底力]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze …
   EN: Prioritizes targets with [Prey]\nCan Clash with this Skill regardless of Speed; this unit does not become Staggered before it uses this Skill\n[WhenUse] Consume all [BattleSense] Stack on self. If this unit consumed...\n- ... 10+ Stack , gain Atk Weight +1 for every 10 Stack consumed (max 4)\n- ... 25 Stack, Final Power +1 for every 4 ([Combustion] + [Vibration]) on the main target (max 6)\n- ... 50 Stack, Coin Power +1 and deal +50% damage\n[DefeatDuel] Gain 2 [ResultReduction]\n[DefeatDuel] Gain 6 [Paralysis]\n[DefeatDuel] Deal -80% damage; this Skill's damage cannot Stagger the target; inflict only half the Potency and Count for both [Combustion] and [Vibration] inflicted by this Skill (unless raised by other effects)\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)\n[EndSkill] Ends this turn
   PL:
51. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Combustion] 6 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 6 [Combustion]
   PL:
54. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Combustion] 횟수 6 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +6 [Combustion] Count
   PL:
57. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 3, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL:
60. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 4, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 6 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +6 [Vibration] Count
   PL:
63. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 5, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 5, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#4].coindescs[#2].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 6, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#5].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 6, efekt 2 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#5].coindescs[#1].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Umiejętność wroga [114507] (ulepszenie 1) — moneta 6, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 5회. 대상의 [Vibration] 횟수 5 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114507].levelList[level=1].coinlist[#5].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 5 times; then, reduce target's [Vibration] Count by 5
   PL:
69. [Umiejętność wroga [114508] (ulepszenie 1) — nazwa] 천퇴성도 장전
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].name
   limit: do 50 znaków
   EN: Reloading Tiantui Star's Blade
   PL:
70. [Umiejętność wroga [114508] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] [BulletPropellant] 1 감소\n[EndSkill] [FullReload] (턴당 1회)\n- [BulletPropellantSpecial]을 보유하였다면, 대신 [ReloadKeepAmmo] (턴당 1회)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [BulletPropellant], [EndSkill], [FullReload], [BulletPropellantSpecial], [ReloadKeepAmmo]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [BulletPropellant] = 호표탄 / Tigermark Round; [EndSkill] = [공격 종료시] / [Attack End]; [FullReload] = 재장전 / Reload; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [ReloadKeepAmmo] = 재장전 - 잔탄 유지 / Reload - Tactical
   EN: [DuelCounter]\n[DefeatDuel] Lose 1 [BulletPropellant]\n[EndSkill] [FullReload] (once per turn)\n- If this unit has [BulletPropellantSpecial], [ReloadKeepAmmo] instead (once per turn)
   PL:
71. [Umiejętność wroga [114508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Umiejętność wroga [114508] (ulepszenie 1) — moneta 2, efekt 1 — opis] [BulletPropellant] 1 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Umiejętność wroga [114508] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Umiejętność wroga [114508] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114508].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [Umiejętność wroga [117101] (ulepszenie 1) — nazwa] 맹호표탄 지원
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=117101].levelList[level=1].name
   limit: do 40 znaków
   EN: Savage Tigermark Support
   PL:
76. [Umiejętność wroga [117101] (ulepszenie 1) — opis] [EndBattle] 자신이 생존한 상태일 경우, 뇌횡에게 [BulletPropellantSpecial] 6 부여\n[EndBattle] [DisengageCombat]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=117101].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [BulletPropellantSpecial], [DisengageCombat]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [DisengageCombat] = 전투 이탈 / Escape Battle
   EN: [EndBattle] If this unit survives, give 6 [BulletPropellantSpecial] to Lei Heng\n[EndBattle] [DisengageCombat]
   PL:
77. [Umiejętność wroga [113501] (ulepszenie 1) — nazwa] 경멸
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113501].levelList[level=1].name
   limit: do 40 znaków
   EN: Contempt
   PL:
78. [Umiejętność wroga [113501] (ulepszenie 1) — opis] 대상의 [GazeReplica]이 3 이상이면 이 스킬에서 부여하는 부정적인 효과가 2배가 됨\n[WhenUse] 대상의 [Laceration]이 6 이상이면 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113501].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [GazeReplica], [WhenUse], [Laceration]
   znaczenie tagów: [GazeReplica] = 시선 / Gaze; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: If target has 3+ [GazeReplica], double the amount of negative effects inflicted with this Skill\n[WhenUse] If target has 6+ [Laceration], Coin Power +1
   PL:
79. [Umiejętność wroga [113501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration], [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed; [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
80. [Umiejętność wroga [113501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 4 [Laceration]
   PL:
81. [Umiejętność wroga [113502] (ulepszenie 1) — nazwa] 경외
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].name
   limit: do 40 znaków
   EN: Awe
   PL:
82. [Umiejętność wroga [113502] (ulepszenie 1) — opis] 대상의 [GazeReplica]이 3 이상이면 이 스킬에서 부여하는 부정적인 효과가 2배가 됨\n[WhenUse] 대상의 [Laceration]이 6 이상이면 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
85. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttackHead] 다음 턴에 [DefenseDown] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [DefenseDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttackHead] Inflict 3 [DefenseDown] next turn
   PL:
86. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
88. [Umiejętność wroga [113502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [AttackDmgDown] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AttackDmgDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: [OnSucceedAttack] Inflict 1 [AttackDmgDown] next turn
   PL:
89. [Umiejętność wroga [113503] (ulepszenie 1) — nazwa] 경멸, 경외 【잠재 해방】
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].name
   limit: do 40 znaków
   EN: Contempt, Awe 【Unleashed】
   PL:
90. [Umiejętność wroga [113503] (ulepszenie 1) — opis] [CantChangeTarget]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantChangeTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantChangeTarget]
   PL:
91. [Umiejętność wroga [113503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable]
   PL:
92. [Umiejętność wroga [113503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 정신력 10 피해
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage
   PL:
93. [Umiejętność wroga [113503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Umiejętność wroga [113503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] (대상의 [GazeReplica] x 5)만큼 흐트러짐 손상
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeReplica]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeReplica] = 시선 / Gaze
   EN: [OnSucceedAttack] Raise Stagger Threshold equal to ([GazeReplica] on target x 5)
   PL:
95. [Umiejętność wroga [113503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [EndSkill] 대상의 [GazeReplica] 제거
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndSkill], [GazeReplica]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [GazeReplica] = 시선 / Gaze
   EN: [EndSkill] Remove [GazeReplica] on the target
   PL:
96. [Umiejętność wroga [113504] (ulepszenie 1) — nazwa] 경멸스러운 것
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113504].levelList[level=1].name
   limit: do 40 znaków
   EN: Contemptuous Thing
   PL:
97. [Umiejętność wroga [113504] (ulepszenie 1) — opis] 홍루를 우선으로 지정\n[WhenUse] 대상에게 [GraspReplica] 4 부여\n[WhenUse] 다음 턴에 [AttackDmgUp] 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113504].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [GraspReplica], [AttackDmgUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [GraspReplica] = 손아귀 / Grasp; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Prioritizes Hong Lu\n[WhenUse] Inflict 4 [GraspReplica]\n[WhenUse] Gain 2 [AttackDmgUp] next turn
   PL:
98. [Umiejętność wroga [113504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Umiejętność wroga [113505] (ulepszenie 1) — nazwa] 경외하도록
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113505].levelList[level=1].name
   limit: do 40 znaków
   EN: Be Awed
   PL:
100. [Umiejętność wroga [113505] (ulepszenie 1) — opis] [GraspReplica]가 부여된 대상 우선으로 사용
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GraspReplica]
   znaczenie tagów: [GraspReplica] = 손아귀 / Grasp
   EN: Prioritizes targets with [GraspReplica]
   PL:
101. [Umiejętność wroga [113505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
102. [Umiejętność wroga [113505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 6 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 6 [Laceration]
   PL:
103. [Umiejętność wroga [113506] (ulepszenie 1) — nazwa] 받아내야만 할거다
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113506].levelList[level=1].name
   limit: do 40 znaków
   EN: You Must Confront This
   PL:
104. [Umiejętność wroga [113506] (ulepszenie 1) — opis] [DuelCounter]\n[DefeatDuel] 대상의 [GazeReplica] 2 감소\n[DefeatDuel] 대상의 [GraspReplica] 1 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113506].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [DefeatDuel], [GazeReplica], [GraspReplica]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [DefeatDuel] = [합 패배] / [Clash Lose]; [GazeReplica] = 시선 / Gaze; [GraspReplica] = 손아귀 / Grasp
   EN: [DuelCounter]\n[DefeatDuel] Reduce target's [GazeReplica] by 2\n[DefeatDuel] Reduce target's [GraspReplica] by 1
   PL:
105. [Umiejętność wroga [113506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Umiejętność wroga [113507] (ulepszenie 1) — nazwa] 경외, 경멸 【잠재 해방】
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113507].levelList[level=1].name
   limit: do 40 znaków
   EN: Awe, Contempt【Unleashed】
   PL:
107. [Umiejętność wroga [113507] (ulepszenie 1) — opis] [BeforeAttack] [GazeReplica]이 4 이상인 수감자의 수만큼 공격 가중치 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113507].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeAttack], [GazeReplica]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [GazeReplica] = 시선 / Gaze
   EN: [BeforeAttack] Gain Atk Weight by the number of Sinners with 4+ [GazeReplica]
   PL:
108. [Umiejętność wroga [113507] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113507].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Umiejętność wroga [113507] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113507].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
110. [Umiejętność wroga [113507] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상의 [GazeReplica]이 4 이상이면, [GazeReplica] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113507].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GazeReplica]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GazeReplica] = 시선 / Gaze
   EN: [OnSucceedAttack] If target has 4+ [GazeReplica], inflict 1 [GazeReplica]
   PL:
111. [Umiejętność wroga [113508] (ulepszenie 1) — nazwa] 나선형 왜곡장
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113508].levelList[level=1].name
   limit: do 40 znaków
   EN: Spiral Warp Field
   PL:
112. [Umiejętność wroga [113508] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 가환과 구보가 보호막 30 얻음\n[WinDuel] 가환과 구보가 보호막 30 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113508].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[StartBattle] Jia Huan and Gubo gain 30 Shield\n[WinDuel] Jia Huan and Gubo gain 30 Shield
   PL:
113. [Umiejętność wroga [113508] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113508].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Umiejętność wroga [113601] (ulepszenie 1) — nazwa] 전방 사격
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113601].levelList[level=1].name
   limit: do 40 znaków
   EN: Front Line Fire
   PL:
115. [Umiejętność wroga [113601] (ulepszenie 1) — opis] 가장 앞에 있는 대상 공격\n[WhenUse] [BoseProjektilReplica] 1 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 횟수 1 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113601].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BoseProjektilReplica], [Laceration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektilReplica] = 찢어진 추억 / Torn Memory; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise
   EN: Targets the frontmost target\n[WhenUse] Gain 1 [BoseProjektilReplica]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Gain +1 [Breath] Count
   PL:
116. [Umiejętność wroga [113601] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL:
117. [Umiejętność wroga [113601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Umiejętność wroga [113602] (ulepszenie 1) — nazwa] 후방 사격
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113602].levelList[level=1].name
   limit: do 40 znaków
   EN: Rear Line Fire
   PL:
119. [Umiejętność wroga [113602] (ulepszenie 1) — opis] 가장 뒤에 있는 대상 공격\n[WhenUse] [BoseProjektilReplica] 1 얻음\n[WhenUse] 대상의 [Laceration]이 6 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113602].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [BoseProjektilReplica], [Laceration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [BoseProjektilReplica] = 찢어진 추억 / Torn Memory; [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise
   EN: Targets the rearmost target\n[WhenUse] Gain 1 [BoseProjektilReplica]\n[WhenUse] If target has 6+ [Laceration], Coin Power +1\n[WhenUse] Gain +2 [Breath] Count
   PL:
120. [Umiejętność wroga [113602] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +70%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: +70% Damage on Critical Hit
   PL:
121. [Umiejętność wroga [113602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Umiejętność wroga [113603] (ulepszenie 1) — nazwa] 마법진으로 쪼개어 나뉘어지는 탄환
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].name
   limit: do 40 znaków
   EN: Sigilshattered Bullet
   PL:
123. [Umiejętność wroga [113603] (ulepszenie 1) — opis] 가장 앞에 있는 대상 공격\n[WhenUse] [Breath] 3, [Breath] 횟수 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: Targets the frontmost target\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count
   PL:
124. [Umiejętność wroga [113603] (ulepszenie 1) — moneta 1, efekt 1 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the main target
   PL:
125. [Umiejętność wroga [113603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EnemyKill] 마지막 코인의 피해량 +100%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] The final Coin deals +100% damage
   PL:
126. [Umiejętność wroga [113603] (ulepszenie 1) — moneta 2, efekt 1 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: This Coin deals damage only against the sub-targets
   PL:
127. [Umiejętność wroga [113603] (ulepszenie 1) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL:
128. [Umiejętność wroga [113603] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113603].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and +2 [Laceration] Count
   PL:
129. [Umiejętność wroga [113604] (ulepszenie 1) — nazwa] 전우의 피를 뒤집어 쓴 탄환
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].name
   limit: do 60 znaków
   EN: Bullet Drenched with the Blood of a Comrade
   PL:
130. [Umiejętność wroga [113604] (ulepszenie 1) — opis] [CantChangeTarget]\nN사 직원을 우선으로 지정\n- 지정한 대상을 공격하지 못했으면, 스킬이 취소됨\n[WhenUse] [Breath] 5 얻음\n[EndBattle] 정신력 20 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [Breath], [EndBattle]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantChangeTarget]\nPrioritizes N Corp. Employees\n- If this unit failed to attack the targeted unit, cancel this Skill\n[WhenUse] Gain 5 [Breath]\n[EndBattle] Heal 20 SP
   PL:
131. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 1, efekt 1 — opis] 이 코인에는 메인 타겟만 피해를 입음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (대상의 적중시 현재 체력)만큼 마지막 코인에 오만 추가 피해
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict (target's HP at the "On Hit' timing) Pride bonus damage with the final Coin
   PL:
133. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상 처치
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Kills the target
   PL:
134. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 2, efekt 1 — opis] 이 코인에는 서브 타겟만 피해를 입음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 4 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Umiejętność wroga [113604] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [Sinking] 4 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113604].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking] and +2 [Sinking] Count
   PL:
138. [Umiejętność wroga [113605] (ulepszenie 1) — nazwa] 추억을 깨는 탄환
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].name
   limit: do 50 znaków
   EN: Reminiscence Shattering Bullet
   PL:
139. [Umiejętność wroga [113605] (ulepszenie 1) — opis] [WideAreaRampage]\n자신의 [BoseProjektilReplica] 당 피해량 +10%\n[WhenUse] 정신력 10 감소\n[EndSkill] [BoseProjektilReplica]을 전부 소모
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WideAreaRampage], [BoseProjektilReplica], [WhenUse], [EndSkill]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [BoseProjektilReplica] = 찢어진 추억 / Torn Memory; [WhenUse] = [사용시] / [On Use]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [WideAreaRampage]\nDeal +10% damage for every [BoseProjektilReplica] on self\n[WhenUse] Lose 10 SP\n[EndSkill] Spend all [BoseProjektilReplica] on self
   PL:
140. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
142. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL:
143. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 정신력 5 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lose 5 SP
   PL:
144. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 정신력 5 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] 정신력 5 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Umiejętność wroga [113605] (ulepszenie 1) — moneta 4, efekt 4 — opis] [OnSucceedAttack] 정신력 5 감소
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113605].levelList[level=1].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Umiejętność wroga [113606] (ulepszenie 1) — nazwa] 근접 전투
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113606].levelList[level=1].name
   limit: do 40 znaków
   EN: Melee Combat
   PL:
157. [Umiejętność wroga [113606] (ulepszenie 1) — opis] [DuelCounter]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DuelCounter]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]
   EN: [DuelCounter]
   PL:
158. [Umiejętność wroga [113606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
159. [Umiejętność wroga [113606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=113606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath]
   PL:
160. [Umiejętność wroga [114601] (ulepszenie 1) — nazwa] 전흑선환- 미[未]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114601].levelList[level=1].name
   limit: do 50 znaków
   EN: Completed Heixian Bolus - Wei [未]
   PL:
161. [Umiejętność wroga [114601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합이 5 이상이면, 합 위력 +1\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합이 7 이상이면 [Breath] 5 얻고, [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114601].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Burst], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 5+ ([Laceration] + [Burst]), Clash Power +1\n[WhenUse] If target has 7+ ([Laceration] + [Burst]), gain 5 [Breath] and +2 [Breath] Count
   PL:
162. [Umiejętność wroga [114601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
163. [Umiejętność wroga [114601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [114602] (ulepszenie 1) — nazwa] 전흑선환 - 인[寅]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114602].levelList[level=1].name
   limit: do 50 znaków
   EN: Completed Heixian Bolus - Yin [寅]
   PL:
165. [Umiejętność wroga [114602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 5 ([Laceration] + [Burst]) on target (max 3)
   PL:
166. [Umiejętność wroga [114602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 2 [DefenseDown] next turn
   PL:
167. [Umiejętność wroga [114602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 5 [Breath]
   PL:
168. [Umiejętność wroga [114602] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114602].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 5 [Laceration]
   PL:
169. [Umiejętność wroga [114603] (ulepszenie 1) — nazwa] 전흑선환 - 사[巳]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114603].levelList[level=1].name
   limit: do 50 znaków
   EN: Completed Heixian Bolus - Si [巳]
   PL:
170. [Umiejętność wroga [114603] (ulepszenie 1) — opis] [WhenUse] 메인 공격 대상의 [Laceration]과 [Burst]의 합이 10 이상이면, 공격 가중치 +1
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] If the main target has 10+ ([Laceration] + [Burst]), Atk Weight +1
   PL:
171. [Umiejętność wroga [114603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Poison] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Poison]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Poison] = 독 / Poison
   EN: [OnSucceedAttack] Inflict 3 [Poison]
   PL:
172. [Umiejętność wroga [114603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Umiejętność wroga [114603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Poison] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Poison]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Poison] = 독 / Poison
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Poison]
   PL:
174. [Umiejętność wroga [114604] (ulepszenie 1) — nazwa] 전흑선환 - 유[酉]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].name
   limit: do 50 znaków
   EN: Completed Heixian Bolus - You [酉]
   PL:
175. [Umiejętność wroga [114604] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합이 10 이상이면, 코인 위력 +1\n크리티컬 적중 시마다 [Laceration], [DefenseDown] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Burst], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] If target has 10+ ([Laceration] + [Burst]), Coin Power +1\nInflict 1 [Laceration] and [DefenseDown] with every Critical Hit
   PL:
176. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst] Count
   PL:
178. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 SP
   PL:
179. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Burst]
   PL:
181. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [114604] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 정신력 2 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114604].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [114605] (ulepszenie 1) — nazwa] 전흑선환 - 혼[混]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].name
   limit: do 50 znaków
   EN: Completed Heixian Bolus - Hun [混]
   PL:
186. [Umiejętność wroga [114605] (ulepszenie 1) — opis] [WhenUse] 메인 공격 대상에게 부여된 부정적인 효과 수 1개당 코인 위력 +1 (최대 2)\n[DefeatDuel] 피해량이 50%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 다음 턴에 [Binding] 2, [DefenseDown] 6 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [EndSkill], [Binding], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [Binding] = 속박 / Bind; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] Coin Power +1 for every type of negative effect on the main target (max 2)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Gain 2 [Binding] and 6 [DefenseDown] next turn
   PL:
187. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 5 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Laceration]
   PL:
190. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Poison] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 173 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [114605] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114605].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Burst] Count
   PL:
194. [Umiejętność wroga [114606] (ulepszenie 1) — nazwa] 전흑선환 - 유[酉] - 수비
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114606].levelList[level=1].name
   limit: do 60 znaków
   EN: Completed Heixian Bolus - You [酉] - Defense
   PL:
195. [Umiejętność wroga [114606] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합이 5 이상이면, 코인 위력 +2\n[WhenUse] 정신력 8 회복\n[WhenUse] [Breath] 3 얻고, [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114606].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Laceration], [Burst], [Breath]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: [CanDuelGuard]\n[WhenUse] If target has 5+ ([Laceration] + [Burst]), Coin Power +2\n[WhenUse] Heal 8 SP\n[WhenUse] Gain 3 [Breath] and +2 [Breath] Count
   PL:
196. [Umiejętność wroga [114606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=114606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [115201] (ulepszenie 1) — nazwa] 보옥요람[寶玉搖籃]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115201].levelList[level=1].name
   limit: do 50 znaków
   EN: Precious Jade's Cradle [寶玉搖籃]
   PL:
198. [Umiejętność wroga [115201] (ulepszenie 1) — opis] [CantChangeTarget]\n홍루 우선 공격\n대상이 홍루면 피해량이 0으로 고정됨\n[EndSkill] 대상이 홍루면, 흐트러짐 상태로 만들고 다음 턴에 [ExpensiveJade]으로 만듦. 이후 턴 종료
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115201].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [EndSkill], [ExpensiveJade]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EndSkill] = [공격 종료시] / [Attack End]; [ExpensiveJade] = 보옥요람 / Precious Jade's Cradle
   EN: [CantChangeTarget]\nPrioritizes Hong Lu\nWhen this Skill targets Hong Lu, deal 0 damage\n[EndSkill] When this Skill targets Hong Lu, Stagger him, then turn him into [ExpensiveJade] next turn; then, end the turn
   PL:
199. [Umiejętność wroga [115201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [115202] (ulepszenie 1) — nazwa] 괴력난신 - 인사유[寅巳酉]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115202].levelList[level=1].name
   limit: do 90 znaków
   EN: Supernatural, Strength, Chaos, and Spirits - Yin Si You [寅巳酉]
   PL:
201. [Umiejętność wroga [115202] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [WhenUse] Coin Power +1 for every 5 ([Laceration] + [Burst]) on target (max 2)
   PL:
202. [Umiejętność wroga [115202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2, [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and 2 [Burst]
   PL:
203. [Umiejętność wroga [115202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2, [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [115203] (ulepszenie 1) — nazwa] 너희는 그 눈의 힘과 특별함을 아직도 한참을 모르고 있구나
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115203].levelList[level=1].name
   limit: do 90 znaków
   EN: You do not know the fathoms of the eye's powers, its special nature
   PL:
205. [Umiejętność wroga [115203] (ulepszenie 1) — opis] 홍루 우선 공격\n[WhenUse] 보옥이 있으면, 이 스킬의 모든 코인이 [SuperCoin]이 됨\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115203].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SuperCoin], [Laceration], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: Prioritizes Hong Lu\n[WhenUse] When there is Baoyu, the Precious Jade, convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] Coin Power +1 for every 5 (sum of [Laceration] and [Burst] on target) (max 2)
   PL:
206. [Umiejętność wroga [115203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3, [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count and +3 [Burst] Count
   PL:
207. [Umiejętność wroga [115203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1, [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Laceration] and 1 [Burst]
   PL:
208. [Umiejętność wroga [115203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Laceration] 1, [Burst] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [115204] (ulepszenie 1) — nazwa] 선인님들 지켜봐주세요...!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115204].levelList[level=1].name
   limit: do 50 znaków
   EN: Please Watch me, O Xianren...!
   PL:
210. [Umiejętność wroga [115204] (ulepszenie 1) — opis] 홍루 우선 공격\n[WinDuel] [Breath] 5 얻음, [Breath] 횟수 2 증가\n[DefeatDuel] 다음 턴에 [AttackUp] 2, [DefenseDown] 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115204].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Breath], [DefeatDuel], [AttackUp], [DefenseDown]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Prioritizes Hong Lu\n[WinDuel] Gain 5 [Breath] and +2 [Breath] Count\n[DefeatDuel] Gain 2 [AttackUp] and 2 [DefenseDown] next turn
   PL:
211. [Umiejętność wroga [115204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2, [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Binding] and 2 [Vulnerable] next turn
   PL:
212. [Umiejętność wroga [115204] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2, [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count and +2 [Burst] Count
   PL:
213. [Umiejętność wroga [115205] (ulepszenie 1) — nazwa] 어르신들의 보살핌이 없는 가주가 어떻게 될지 알고 있느냐!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].name
   limit: do 90 znaków
   EN: You do not know the fate of a Hierarch without the Xianren's care!
   PL:
214. [Umiejętność wroga [115205] (ulepszenie 1) — opis] [WhenUse] 정신력 25 회복\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Heal 25 SP\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
215. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] (대상의 [Burst]과 [Laceration]의 합)당 피해량 2.5% 증가 (최대 50%)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Burst], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Deal +2.5% damage for every ([Burst] + [Laceration]) on target (max 50%)
   PL:
217. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Poison] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] (대상의 [Burst]과 [Laceration]의 합)당 피해량 2.5% 증가 (최대 50%)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Laceration] 3 부여. [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration] and +2 [Laceration] Count
   PL:
221. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] (대상의 [Burst]과 [Laceration]의 합)당 피해량 2.5% 증가 (최대 50%)
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Umiejętność wroga [115205] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여. [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115205].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst] and +2 [Burst] Count
   PL:
224. [Umiejętność wroga [115206] (ulepszenie 1) — nazwa] 부질 없는 짓을...!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115206].levelList[level=1].name
   limit: do 60 znaków
   EN: Nothing But a Meaningless Struggle...!
   PL:
225. [Umiejętność wroga [115206] (ulepszenie 1) — opis] [CanDuelGuard]\n[WinDuel] 가모의 정신력 15 회복. 가모의 정신력이 0 미만이면, 대신 30 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115206].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[WinDuel] Jia Mu heals 15 SP. At 0 SP, heal 30 SP instead.
   PL:
226. [Umiejętność wroga [115206] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115206].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [115207] (ulepszenie 1) — nazwa] 너는 여전히 아무것도 할 수 없단다
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].name
   limit: do 40 znaków
   EN: Still, you can do nothing
   PL:
228. [Umiejętność wroga [115207] (ulepszenie 1) — opis] [WhenUse] [OutpouringAnger] 얻음\n[WhenUse] 정신력 8 회복\n[WhenUse] 메인 타겟의 체력이 50% 미만이거나, 메인 타겟의 [Burst]과 [Laceration]의 합이 10 이상이면 [SuperCoin]이 됨\n[DefeatDuel] [Vulnerable] 1 얻음\n- 홍루에게 합 패배 시 대신 2 얻음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [OutpouringAnger], [Burst], [Laceration], [SuperCoin], [DefeatDuel], [Vulnerable]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [OutpouringAnger] = 발악 / Rampage; [Burst] = 파열 / Rupture; [Laceration] = 출혈 / Bleed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile
   EN: [WhenUse] Gain [OutpouringAnger]\n[WhenUse] Heal 8 SP\n[WhenUse] If the main target has less than 50% HP, or if the main target has 10+ ([Burst] + [Laceration]), convert this Skill's Coins to [SuperCoin]s\n[DefeatDuel] Gain 1 [Vulnerable]\n- When losing a clash against Hong Lu, gain 2 [Vulnerable] instead
   PL:
229. [Umiejętność wroga [115207] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4, [Burst] 4 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 4 [Laceration] and 4 [Burst]
   PL:
230. [Umiejętność wroga [115207] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
231. [Umiejętność wroga [115207] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 정신력 피해 10, 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 10 SP damage and raise target's Stagger Threshold by 50% of damage dealt
   PL:
232. [Umiejętność wroga [115207] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
233. [Umiejętność wroga [115207] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] 정신력 8 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115207].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 8 SP
   PL:
234. [Umiejętność wroga [115208] (ulepszenie 1) — nazwa] 선인들의 그 어떤 비호도 못받는 이름뿐인 가주는 벌레만도 못하게 죽어버릴게다!!!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].name
   limit: do 140 znaków
   EN: A Hierarch without the Xianren's blessing is a Hierarch in name only; she will die an insect's death!!!
   PL:
235. [Umiejętność wroga [115208] (ulepszenie 1) — opis] [WhenUse] 본체의 체력이 30% 이하면, 코인 위력 +3, 피해량 +30%\n[WhenUse] 본체의 체력이 50% 미만이면 이 스킬의 코인이 [SuperCoin]이 됨\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [SuperCoin], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] At 30% or less Core HP: Coin Power +3, deal +30% damage\n[WhenUse] At less than 50% Core HP: convert this Skill's Coins to [SuperCoin]s\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
236. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] 쌓이는 순종 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 Heaping Obedience
   PL:
237. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
238. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL:
239. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 정신력 5 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 5 SP
   PL:
240. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [PileObedient] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [PileObedient]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [PileObedient] = 쌓이는 순종 / Heaping Obedience
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [PileObedient]
   PL:
241. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Umiejętność wroga [115208] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 정신력 5 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115208].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Umiejętność wroga [115209] (ulepszenie 1) — nazwa] 감히 배알하거라
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115209].levelList[level=1].name
   limit: do 70 znaków
   EN: Be honored to be in audience of such a great man
   PL:
245. [Umiejętność wroga [115209] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] 다음 턴에 몸통 부위에 [Enhancement] 2, [Endurance] 2, [AttackDmgUp] 2 부여\n[WhenUse] 자신의 정신력을 30까지 회복\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115209].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Enhancement], [Endurance], [AttackDmgUp], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n[WhenUse] Gain 2 [Enhancement], 2 [Endurance], and 2 [AttackDmgUp] to the Body Part next turn\n[WhenUse] Heal this unit's SP up to 30 SP\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL:
246. [Umiejętność wroga [115209] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115209].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [115209] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 10 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115209].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Sinking]
   PL:
248. [Umiejętność wroga [115210] (ulepszenie 1) — nazwa] 선황충님 소녀와 함께 해주셔요
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115210].levelList[level=1].name
   limit: do 50 znaków
   EN: Be with this little girl, O Xianren
   PL:
249. [Umiejętność wroga [115210] (ulepszenie 1) — opis] [StartBattle] 몸통 부위와 본체에 각 최대 체력의 10%만큼 보호막 부여\n[WhenUse] 다음 턴에 몸통 부위에 [Enhancement] 1, [Endurance] 1, [AttackDmgUp] 2 부여\n[WhenUse] 정신력 15 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115210].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Enhancement], [Endurance], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] Body and Core Parts gain Shield equal to 10% of their max HP, respectively\n[WhenUse] Body Part gains 1 [Enhancement], 1 [Endurance], and 2 [AttackDmgUp] next turn\n[WhenUse] Heal 15 SP
   PL:
250. [Umiejętność wroga [115210] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115210].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [115210] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115210].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +2 [Sinking] Count
   PL:
252. [Umiejętność wroga [115211] (ulepszenie 1) — nazwa] 선인이시여...!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115211].levelList[level=1].name
   limit: do 40 znaków
   EN: O Xianren...!
   PL:
253. [Umiejętność wroga [115211] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[StartBattle] 다음 턴에 어르신 나무 5개 생성\n[DefeatDuel] 피해량이 50%만큼 감소하고, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 턴 종료
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115211].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel], [EndSkill]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n[StartBattle] Generate 5 Elder Trees next turn\n[DefeatDuel] Deal -50% damage and this damage dealt by this Skill cannot Stagger the target\n[EndSkill] Ends turn
   PL:
254. [Umiejętność wroga [115211] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115211].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [115212] (ulepszenie 1) — nazwa] 사미윤의 힘이 되어주셔요!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].name
   limit: do 60 znaków
   EN: Please give me, Shi Miyin, your strength!
   PL:
256. [Umiejętność wroga [115212] (ulepszenie 1) — opis] 대상의 체력이 50% 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].desc
   limit: do 120 znaków
   EN: If target has 50%+ HP, Coin Power +1
   PL:
257. [Umiejętność wroga [115212] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [ImperfectEternalLife]가 없는 아군 중 체력이 가장 낮은 아군의 체력을 회복 대상 최대 체력의 15%만큼 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ImperfectEternalLife]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ImperfectEternalLife] = 불완전한 불사 / Imperfect Immortality
   EN: [OnSucceedAttack] Among targets without [ImperfectEternalLife], choose and heal 15% HP for the ally with the least HP
   PL:
258. [Umiejętność wroga [115212] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [115212] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ImperfectEternalLife]가 없는 아군 중 체력이 가장 낮은 아군의 체력을 회복 대상 최대 체력의 15%만큼 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [115212] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115212].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [115213] (ulepszenie 1) — nazwa] 극선착적공양[極仙榨滴供養]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115213].levelList[level=1].name
   limit: do 80 znaków
   EN: An Offering of Extreme Extracted Immortality [極仙榨滴供養]
   PL:
262. [Umiejętność wroga [115213] (ulepszenie 1) — opis] [CantIdentify]\n이 스킬은 아군에게 피해를 주지 않음\n속도에 상관없이 이 스킬과 합을 할 수 있으며, 이 스킬을 사용하기 전까지 흐트러짐 상태가 되지 않음\n[WhenUse] [SupremeEternalLife]를 보유한 아군 1명당 코인 위력 +2, 피해량 +20%\n[WhenUse] [SupremeEternalLife]를 가진 아군이 없는 경우 대신 모든 대상에게 보호막 200 부여\n[EndSkill] 턴 종료
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115213].levelList[level=1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [WhenUse], [SupremeEternalLife], [EndSkill]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [WhenUse] = [사용시] / [On Use]; [SupremeEternalLife] = 지고한 불사 / Sublime Immortality; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantIdentify]\nThis Skill cannot deal damage to allies\nCan Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n[WhenUse] Coin Power +2 and deal +20% damage for every 1 ally with [SupremeEternalLife]\n[WhenUse] If there aren't any allies with [SupremeEternalLife], apply 200 Shield to all targets\n[EndSkill] Ends turn
   PL:
263. [Umiejętność wroga [115213] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115213].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [115213] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면 남은 체력을 흡수하고, 대상의 [ImperfectEternalLife]를 흡수하여 다음 턴에 모든 부위가 흡수한 수치만큼 해당 효과를 얻음. 이후 흡수한 대상을 제거함
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115213].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ImperfectEternalLife]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ImperfectEternalLife] = 불완전한 불사 / Imperfect Immortality
   EN: [OnSucceedAttack] If the target is an ally, siphon their remaining HP and their [ImperfectEternalLife]. Then, apply the same amount of [ImperfectEternalLife] Stack to all of this unit's Parts next turn. Eliminate the Siphoned unit afterward.
   PL:
265. [Umiejętność wroga [115213] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 8, [Burst] 8 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115213].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration], [Burst]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 8 [Laceration] and 8 [Burst]
   PL:
266. [Umiejętność wroga [115301] (ulepszenie 1) — nazwa] 문안 인사 드립니다
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115301].levelList[level=1].name
   limit: do 40 znaków
   EN: I greet you now
   PL:
267. [Umiejętność wroga [115301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [115301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상에게 정신력 피해 5
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Deal 5 SP damage
   PL:
269. [Umiejętność wroga [115301] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115301].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vulnerable]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vulnerable] = 취약 / Fragile
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL:
270. [Umiejętność wroga [115302] (ulepszenie 1) — nazwa] 얌전히 있을게요
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115302].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll be docile
   PL:
271. [Umiejętność wroga [115302] (ulepszenie 1) — opis] [CanDuelGuard]\n[WinDuel] 가모의 정신력 15 회복. 가모의 정신력이 0 미만이면, 대신 30 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115302].levelList[level=1].desc
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [115302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [115303] (ulepszenie 1) — nazwa] 즐거움을 드릴게요
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115303].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll be your amusement
   PL:
274. [Umiejętność wroga [115303] (ulepszenie 1) — opis] [CantDuel]\n[EndSkill] 이 캐릭터가 사망하고, 가모의 정신력을 45까지 회복. 다음 턴에 가모에게 [Enhancement] 2, [AttackDmgUp] 5 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115303].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [EndSkill], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [CantDuel]\n[EndSkill] Kills this unit and heals Jia Mu's SP up to 45 SP. Apply 2 [Enhancement] and 5 [AttackDmgUp] to Jia Mu next turn
   PL:
275. [Umiejętność wroga [115303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Umiejętność wroga [115303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 정신력 피해 15
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 SP damage
   PL:
277. [Umiejętność wroga [115303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 50%만큼 흐트러짐 손상
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 50% of damage dealt
   PL:
278. [Umiejętność wroga [115401] (ulepszenie 1) — nazwa] 생기를 다오
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].name
   limit: do 40 znaków
   EN: Give me your vitality
   PL:
279. [Umiejętność wroga [115401] (ulepszenie 1) — opis] 대상의 체력이 50% 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].desc
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [115401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 20%만큼 체력 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 20% of Max HP
   PL:
281. [Umiejętność wroga [115401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
282. [Umiejętność wroga [115401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 20%만큼 체력 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [115401] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115401].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [115402] (ulepszenie 1) — nazwa] 즐거움을 주려무나
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115402].levelList[level=1].name
   limit: do 40 znaków
   EN: Please me
   PL:
285. [Umiejętność wroga [115402] (ulepszenie 1) — opis] 대상의 체력이 50% 이상이면, 합 위력 +2\n[WhenUse] 가모의 정신력 10 회복
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If target has 50%+ HP, Clash Power +2\n[WhenUse] Heal 10 SP for Jia Mu
   PL:
286. [Umiejętność wroga [115402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [115403] (ulepszenie 1) — nazwa] 선인의 지혜로운 조언
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115403].levelList[level=1].name
   limit: do 40 znaków
   EN: The Xianren's Wise Counsel
   PL:
288. [Umiejętność wroga [115403] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 가모에게 [Enhancement] 1, [AttackDmgUp] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [WhenUse] Apply 1 [Enhancement] and 1 [AttackDmgUp] to Jia Mu next turn
   PL:
289. [Umiejętność wroga [115403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność wroga [115403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [115404] (ulepszenie 1) — nazwa] 선인의 참된 조언
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115404].levelList[level=1].name
   limit: do 40 znaków
   EN: The Xianren's True Counsel
   PL:
292. [Umiejętność wroga [115404] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 가모에게 [Endurance] 1, [Protection] 1 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Endurance], [Protection]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Endurance] = 수비 위력 증가 / Defense Power Up; [Protection] = 보호 / Protection
   EN: [WhenUse] Apply 1 [Endurance] and 1 [Protection] to Jia Mu next turn
   PL:
293. [Umiejętność wroga [115404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [115405] (ulepszenie 1) — nazwa] 생기가 필요해...
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115405].levelList[level=1].name
   limit: do 40 znaków
   EN: I need more vitality...
   PL:
295. [Umiejętność wroga [115214] (ulepszenie 1) — nazwa] 부질 없는 짓을...!
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115214].levelList[level=1].name
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Umiejętność wroga [115214] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 대상의 [Laceration]과 [Burst]의 합 5당, 코인 위력 +1 (최대 3)\n[WinDuel] [Burst] 횟수 1 증가, [DefenseDown] 2 부여
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115214].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Laceration], [Burst], [WinDuel], [DefenseDown]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [CanDuelGuard]\n[WhenUse] Coin Power +1 for every 5 ([Laceration] + [Burst]) on target (max 3)\n[WinDuel] Inflict +1 [Burst] Count, inflict 2 [DefenseDown]
   PL:
297. [Umiejętność wroga [115214] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c8p3.json :: dataList[id=115214].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c8p3] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c8p3
- grupa rozdziału/trybu: `a1c8p3` · plik: `Skills_Enemy-a1c8p3.json`

298. [Umiejętność wroga [9021301] (ulepszenie 1) — nazwa] 상처 터뜨리기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021301].levelList[level=1].name
   limit: do 40 znaków
   EN: Burst Wounds
   PL:
299. [Umiejętność wroga [9021301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [9021301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Umiejętność wroga [9021302] (ulepszenie 1) — nazwa] 상처 옭아매기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021302].levelList[level=1].name
   limit: do 40 znaków
   EN: Snag Wounds
   PL:
302. [Umiejętność wroga [9021302] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021302].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 2+ [Laceration], Coin Power +1
   PL:
303. [Umiejętność wroga [9021302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL:
304. [Umiejętność wroga [9021302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [9021303] (ulepszenie 1) — nazwa] 살점 녹이기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021303].levelList[level=1].name
   limit: do 40 znaków
   EN: Flesh Melting
   PL:
306. [Umiejętność wroga [9021303] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021303].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If target has 3+ [Laceration], Clash Power +1
   PL:
307. [Umiejętność wroga [9021303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [9021303] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021303].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 1 [Agility] next turn
   PL:
309. [Umiejętność wroga [9021304] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021304].levelList[level=1].name
   limit: do 40 znaków
   EN: Casting Shade
   PL:
310. [Umiejętność wroga [9021304] (ulepszenie 1) — opis] [WhenUse] [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze
   EN: [WhenUse] Inflict 1 [Paralysis]
   PL:
311. [Umiejętność wroga [9021401] (ulepszenie 1) — nazwa] 상처 헤집기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021401].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Up Wound
   PL:
312. [Umiejętność wroga [9021401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność wroga [9021401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność wroga [9021402] (ulepszenie 1) — nazwa] 상처 훑기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021402].levelList[level=1].name
   limit: do 40 znaków
   EN: Skim Wounds
   PL:
315. [Umiejętność wroga [9021402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021402].levelList[level=1].desc
   (powtórzenie elementu 302 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [9021402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [9021402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [9021403] (ulepszenie 1) — nazwa] 살점 뜯기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021403].levelList[level=1].name
   limit: do 40 znaków
   EN: Flesh Tearing
   PL:
319. [Umiejętność wroga [9021403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration]이 3 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021403].levelList[level=1].desc
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [9021403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność wroga [9021403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Umiejętność wroga [9021404] (ulepszenie 1) — nazwa] 드리우는 그늘
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021404].levelList[level=1].name
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność wroga [9021404] (ulepszenie 1) — opis] [WhenUse] [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021404].levelList[level=1].desc
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [9021701] (ulepszenie 1) — nazwa] 진탕 찌르기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021701].levelList[level=1].name
   limit: do 40 znaków
   EN: Concussive Stab
   PL:
325. [Umiejętność wroga [9021701] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Combustion], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: [WhenUse] Coin Power +1 for every 7 ([Combustion] + [Vibration]) on target (max 2)
   PL:
326. [Umiejętność wroga [9021701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [9021701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Umiejętność wroga [9021702] (ulepszenie 1) — nazwa] 작열 찌르기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021702].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Stab
   PL:
329. [Umiejętność wroga [9021702] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021702].levelList[level=1].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [9021702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 3 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Umiejętność wroga [9021702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +2 [Combustion] Count
   PL:
332. [Umiejętność wroga [9021703] (ulepszenie 1) — nazwa] 추진 베기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].name
   limit: do 40 znaków
   EN: Propulsion Slice
   PL:
333. [Umiejętność wroga [9021703] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)\n[DefeatDuel] 피해량이 75%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [Vibration], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 7 ([Combustion] + [Vibration]) on target (max 2)\n[DefeatDuel] Deal -75% damage and damage dealt by this Skill cannot Stagger the target
   PL:
334. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BudgetBulletPropellant] 1 소모
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BudgetBulletPropellant]
   znaczenie tagów: [BudgetBulletPropellant] = 추진탄 / Propellant Ammo
   EN: Spend 1 [BudgetBulletPropellant]
   PL:
336. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL:
337. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
338. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BudgetBulletPropellant] 1 소모.
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BudgetBulletPropellant]
   znaczenie tagów: [BudgetBulletPropellant] = 추진탄 / Propellant Ammo
   EN: Spend 1 [BudgetBulletPropellant]
   PL:
341. [Umiejętność wroga [9021703] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
342. [Umiejętność wroga [9021704] (ulepszenie 1) — nazwa] 추진탄 재장전
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021704].levelList[level=1].name
   limit: do 40 znaków
   EN: Propellant Ammo Reload
   PL:
343. [Umiejętność wroga [9021704] (ulepszenie 1) — opis] [StartBattle] [FullReload] (턴 당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +3\n[WhenUse] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021704].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [FullReload], [WhenUse], [Combustion], [Vibration], [AttackDmgUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [FullReload] = 재장전 / Reload; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [StartBattle] [FullReload] (once per turn)\n[WhenUse] If target has 6+ ([Combustion] + [Vibration]), Coin Power +3\n[WhenUse] Gain 1 [AttackDmgUp] next turn
   PL:
344. [Umiejętność wroga [9021801] (ulepszenie 1) — nazwa] 진탕 꿰뚫기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021801].levelList[level=1].name
   limit: do 40 znaków
   EN: Concussive Penetration
   PL:
345. [Umiejętność wroga [9021801] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021801].levelList[level=1].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [9021801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Umiejętność wroga [9021801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Umiejętność wroga [9021802] (ulepszenie 1) — nazwa] 작열 꿰뚫기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021802].levelList[level=1].name
   limit: do 40 znaków
   EN: Burning Penetration
   PL:
349. [Umiejętność wroga [9021802] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021802].levelList[level=1].desc
   (powtórzenie elementu 325 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [9021802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 2 부여
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion]
   PL:
351. [Umiejętność wroga [9021802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [9021803] (ulepszenie 1) — nazwa] 추진 가르기
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].name
   limit: do 40 znaków
   EN: Propulsion Cleave
   PL:
353. [Umiejętność wroga [9021803] (ulepszenie 1) — opis] [WhenUse] 대상의 [Combustion]과 [Vibration]의 합 7 당, 코인 위력 +1 (최대 2)\n[DefeatDuel] 피해량이 75%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].desc
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 1, efekt 2 — opis] [BudgetBulletPropellant] 1 소모
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가,
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count,
   PL:
357. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [Combustion] 2 부여, [Combustion] 횟수 2 증가
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 2 [Combustion] and +2 [Combustion] Count
   PL:
358. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 1, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationIgnition]로 [Switch_Vibration]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 2, efekt 2 — opis] [BudgetBulletPropellant] 1 소모.
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Umiejętność wroga [9021803] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021803].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [9021804] (ulepszenie 1) — nazwa] 추진탄 재장전
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021804].levelList[level=1].name
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [9021804] (ulepszenie 1) — opis] [StartBattle] [FullReload] (턴 당 1회)\n[WhenUse] 대상의 [Combustion]과 [Vibration]의 합이 6 이상이면, 코인 위력 +3\n[WhenUse] 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Skills_Enemy-a1c8p3.json :: dataList[id=9021804].levelList[level=1].desc
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c8p3] Pasywka wroga: Passives_Abnormality-a1c8p3
- plik gry: `Passives_Abnormality-a1c8p3.json`

364. [[a1c8p3] Pasywka wroga [114501] — nazwa] 엄지 간부 카포 IIII
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114501].name
   limit: do 50 znaków
   EN: The Thumb's Officer, Capo IIII
   PL:
365. [[a1c8p3] Pasywka wroga [114501] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -30%\n\n[BulletPropellant]을 소모하는 코인을 굴릴 때, [BulletPropellant]이 없는 경우에도 공격을 취소하지 않는 대신 해당 코인의 적중 시 [Combustion] 부여, [Combustion] 횟수 증가 효과가 발동하지 않음\n\n합 진행 시, (1 + 합을 진행한 횟수/3)만큼 대상의 [Vibration] 횟수 증가\n(최대 3, 하나의 대상에게 턴당 최대 3회 적용)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114501].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [BulletPropellant]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Take -30% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\n\nWhen flipping a Coin that consumes [BulletPropellant]: while not having [BulletPropellant] does not cancel this unit's attacks, the Coin's "inflict [Combustion]" and "inflict [Combustion] Count" effects do not activate\n\nIn a Clash, inflict +(1 + (# of Clashes / 3)) [Vibration] Count\n(max 3; 3 times per turn against the same target)
   PL:
366. [[a1c8p3] Pasywka wroga [114502] — nazwa] 동부십검
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114502].name
   limit: do 40 znaków
   EN: Ten Blades of the East
   PL:
367. [[a1c8p3] Pasywka wroga [114502] — opis] 스테이지 시작 시와 패턴이 변경되는 턴 시작 시,\n- [Bothersome] 1 얻음\n- 자신의 잃은 체력 10%당 정신력 5 회복 (최대 40)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114502].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Bothersome]
   znaczenie tagów: [Bothersome] = 절참 [切斬] / Severing Slash [切斬]
   EN: At Encounter Start, and at the Turn Start of gaining a new pattern:\n- Gain 1 [Bothersome]\n- Heal 5 SP for every 10% missing HP on self (max 40)
   PL:
368. [[a1c8p3] Pasywka wroga [114503] — nazwa] 사냥감 선정
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114503].name
   limit: do 40 znaków
   EN: Chosen Prey
   PL:
369. [[a1c8p3] Pasywka wroga [114503] — opis] 턴 시작 시, 이전 턴에 자신에게 가장 많은 피해를 입힌 대상에게 [Prey] 1 부여\n\n뇌횡이 [Prey]을 보유한 대상을 공격하여 공격 종료 시 대상이\n- 흐트러진 경우, 모든 적의 정신력이 10 감소하고 이번 턴과 다음 턴에 [ParryingResultDown] 1 부여 (턴당 1회)\n- 사망한 경우, 위의 효과가 1회 추가로 발동
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114503].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Prey], [ParryingResultDown]
   znaczenie tagów: [Prey] = 사냥감 / Prey; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: Turn Start: inflict 1 [Prey] against the target that dealt the most damage to this unit last turn\n\nAfter Lei Heng attacks the target with [Prey], if the target is:\n- Staggered, all enemies lose 10 SP and gain 1 [ParryingResultDown] for this turn and next turn (once per turn)\n- Defeated, activate the above effect once more
   PL:
370. [[a1c8p3] Pasywka wroga [114504] — nazwa] 천퇴성도 [天退星刀]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114504].name
   limit: do 40 znaków
   EN: Tiantui Star's Blade [天退星刀]
   PL:
371. [[a1c8p3] Pasywka wroga [114504] — opis] 일방 공격 적중 시 피해량이 30%만큼 증가하고, 다음 턴에 [Vulnerable] 1 부여\n\n[BulletPropellant]을 소모하여 적중한 스킬 코인의 피해량이 20%만큼 증가하고, 다음 턴에 [DefenseDown] 2 부여\n\n대상이 수비 스킬을 장착한 경우에는 위의 효과가 적용되지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114504].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [BulletPropellant], [DefenseDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [BulletPropellant] = 호표탄 / Tigermark Round; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Unopposed Attacks deal +30% damage On Hit and inflict 1 [Vulnerable] next turn\n\nSkill Coins that spent [BulletPropellant] deal +20% damage On Hit and inflict 2 [DefenseDown] next turn\n\nThe above effects do not activate if the target equipped a Defense Skill
   PL:
372. [[a1c8p3] Pasywka wroga [114505] — nazwa] 호표탄 장전
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114505].name
   limit: do 40 znaków
   EN: Tigermark Round Reload
   PL:
373. [[a1c8p3] Pasywka wroga [114505] — opis] 턴 종료 시점에 체력이 90% 이하가 되었거나 2번째 턴 종료 시, [BulletPropellant]을 장전하고 다음 턴에 패턴이 변경됨\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114505].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [BulletPropellant]
   znaczenie tagów: [BulletPropellant] = 호표탄 / Tigermark Round
   EN: Turn End: at 90% or less HP, or at the end of the 2nd turn, reload [BulletPropellant] and gain a new pattern next turn\n- If this unit is Staggered, recover from Stagger
   PL:
374. [[a1c8p3] Pasywka wroga [114506] — nazwa] 뇌횡 [雷橫]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114506].name
   limit: do 40 znaków
   EN: Lei Heng [雷橫]
   PL:
375. [[a1c8p3] Pasywka wroga [114506] — opis] 턴 종료 시점에 체력이 80% 이하가 되었거나 4번째 턴 종료 시, 다음 턴에 패턴이 변경됨\n- 강력한 공격('쾌도난마')을 사용하며, 3번째 턴마다 반복함. 이 스킬을 사용하는 턴의 속도 최솟값, 최댓값 +10\n- 해당 턴 시작 시, [BattleSense] 25 얻음\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114506].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [BattleSense]
   znaczenie tagów: [BattleSense] = 저력 [底力] / Inner Strength [底力]
   EN: Turn End: at 80% or less HP, or at the end of the 4th turn, gain a new pattern next turn\n- Use a powerful attack ('Tanglecleaver'), repeat every 3rd turn. +10 to Min & Max Speed for turns in which this unit uses this Skill\n- At the start of that turn, gain 25 [BattleSense]\n- If this unit is Staggered, recover from Stagger
   PL:
376. [[a1c8p3] Pasywka wroga [114507] — nazwa] 천퇴성 [天退星]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114507].name
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL:
377. [[a1c8p3] Pasywka wroga [114507] — opis] 턴 종료 시점에 체력이 60% 이하가 되었거나 다음 턴에 강력한 공격('쾌도난마')을 이번 전투에서 두 번째로 사용할 예정이면, 다음 턴에 패턴이 변경됨\n- 해당 턴 시작 시, [Irritation] 1 얻음\n- 해당 턴 시작 시, [BulletPropellantSpecial] 18 얻고 즉시 장전\n· [BulletPropellantSpecial]을 전부 소모할 경우, 해당 효과가 [BulletPropellant]으로 변경되고 다음 턴에 엄격한 엄지 솔다토 2명을 소환하여 [BulletPropellantSpecial]을 보급받음\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114507].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [Irritation], [BulletPropellantSpecial], [BulletPropellant]
   znaczenie tagów: [Irritation] = 천퇴성[天退星] / Tiantui Star [天退星]; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [BulletPropellant] = 호표탄 / Tigermark Round
   EN: If this unit's HP dropped to 60% or below at Turn End, or if this unit is set to use a powerful attack ('Tanglecleaver') next turn for the second time this Encounter, gain a new pattern next turn\n- When that turn starts, gain 1 [Irritation]\n- When that turn starts, gain 18 [BulletPropellantSpecial] and reload immediately\n· If this unit spends all [BulletPropellantSpecial], convert the effect to [BulletPropellant] and summon 2 of "Stern Soldato of the Thumb" units next turn and have them supply this unit with [BulletPropellantSpecial]\n- When Staggered, recover from Stagger
   PL:
378. [[a1c8p3] Pasywka wroga [114508] — nazwa] 소지 천퇴성 뇌횡
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114508].name
   limit: do 50 znaków
   EN: Lei Heng, The Pinky's Tiantui Star
   PL:
379. [[a1c8p3] Pasywka wroga [114508] — opis] 턴 종료 시점에 체력이 40% 이하가 되었거나 다음 턴에 강력한 공격('쾌도난마')을 이번 전투에서 세 번째로 사용할 예정이면, 다음 턴에 패턴이 변경됨\n- 강력한 공격 '쾌도난마'가 '초절맹호살격난참'으로 변경됨. 이 스킬을 사용하는 턴의 속도 최솟값, 최댓값 +15\n- [BattleSense]이 [RestoredBattleSense]으로 변경\n- [Irritation]가 [HugeIrritation]으로 변경\n- 흐트러짐 상태면, 흐트러짐 해제
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114508].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n, [BattleSense], [RestoredBattleSense], [Irritation], [HugeIrritation]
   znaczenie tagów: [BattleSense] = 저력 [底力] / Inner Strength [底力]; [RestoredBattleSense] = 극력 [極力] / Extreme Strength [極力]; [Irritation] = 천퇴성[天退星] / Tiantui Star [天退星]; [HugeIrritation] = 신(心) - 천퇴성[天退星] / Shin (心) - Tiantui Star [天退星]
   EN: Turn End: at 40% or less HP, or if this unit is set to use a powerful attack ('Tanglecleaver') next turn for the third time this Encounter, gain a new pattern next turn\n- Replace the powerful attack 'Tanglecleaver' with 'Savage Tigerslayer's Perfected Flurry of Blades'. +15 to Min & Max Speed for turns in which this unit uses this Skill\n- Convert [BattleSense] to [RestoredBattleSense]\n- Convert [Irritation] to [HugeIrritation]\n- If this unit is Staggered, recover from Stagger
   PL:
380. [[a1c8p3] Pasywka wroga [114510] — nazwa] 삽시호 [揷翅虎]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114510].name
   limit: do 40 znaków
   EN: Chachihu [揷翅虎]
   PL:
381. [[a1c8p3] Pasywka wroga [114510] — opis] 전투 시작 시 자신의 속도에 비례하여,\n- 수치만큼 정신력을 회복. 정신력이 0 미만이면 회복 수치가 2배로 적용됨\n- (수치/3)만큼 [SlashDamageUp] 얻음 (최대 5)\n\n전투 시작 시 자신이 [Binding]을 3 이상 보유하였다면 위의 효과가 발동하지 않고, 보유한 [Binding] 수치만큼 [DefenseDown] 얻음 (최대 9)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114510].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp], [Binding], [DefenseDown]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [Binding] = 속박 / Bind; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Combat Start: based on this unit's Speed value,\n- Heal SP equal to Speed value. At less than 0 SP, double the heal amount\n- Gain (Speed Value / 3) [SlashDamageUp] (max 5)\n\nCombat Start: if this unit has 3+ [Binding], the above effect does not activate; gain [DefenseDown] equal to [Binding] on self (max 9)
   PL:
382. [[a1c8p3] Pasywka wroga [114512] — nazwa] 천퇴성도 오버히트
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114512].name
   limit: do 50 znaków
   EN: Tiantui Star's Blade - Overheat
   PL:
383. [[a1c8p3] Pasywka wroga [114512] — opis] 강력한 공격('쾌도난마', '초절맹호살격난참')을 사용하였다면, 이번 전투 동안 강력한 공격을 사용한 횟수만큼 다음 턴에 [Complacency] 얻음 (최대 5)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114512].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Complacency]
   znaczenie tagów: [Complacency] = 오버히트 / Overheat
   EN: If this unit used a powerful attack ('Tanglecleaver' or 'Savage Tigerslayer's Perfected Flurry of Blades'), gain [Complacency] next turn equal to the number of times those skills were used (max 5)
   PL:
384. [[a1c8p3] Pasywka wroga [117101] — nazwa] 맹호표탄 지원
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=117101].name
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [[a1c8p3] Pasywka wroga [117101] — opis] 턴 시작 시, [Vulnerable] 5 얻음\n턴 종료 시, 뇌횡에게 [BulletPropellantSpecial]을 지원함.\n\n사망 시 뇌횡에게 [BulletPropellantSpecial]을 지원하지 못하고, 다음 턴에 뇌횡이 [Vulnerable] 1, [ParryingResultDown] 1 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=117101].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [BulletPropellantSpecial], [ParryingResultDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [BulletPropellantSpecial] = 맹호표탄 / Savage Tigermark Round; [ParryingResultDown] = 합 위력 감소 / Clash Power Down
   EN: Turn Start: gain 5 [Vulnerable]\nTurn End: supply [BulletPropellantSpecial] to Lei Heng\n\nIf this unit is killed, this unit cannot supply [BulletPropellantSpecial] for Lei Heng; Lei Heng gains 1 [Vulnerable] and 1 [ParryingResultDown] next turn
   PL:
386. [[a1c8p3] Pasywka wroga [113501] — nazwa] 놓쳤던 동생의 손
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113501].name
   limit: do 50 znaków
   EN: My Little Brother's Hand I Let Slip
   PL:
387. [[a1c8p3] Pasywka wroga [113501] — opis] 적에게 자신의 공격 적중 시, [GazeReplica] 1 부여 (인격 당 턴 당 1회)\n적에게 자신이 공격당하면, 공격자에게 [GazeReplica] 1 부여 (인격 당 턴 당 1회)\n턴 시작시 홍루가 전투에 등장해 있으면, 홍루에게 [GazeReplica] 1 부여
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113501].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [GazeReplica]
   znaczenie tagów: [GazeReplica] = 시선 / Gaze
   EN: On Hit against an enemy, inflict 1 [GazeReplica] (once per Identity per turn)\nWhen attacked by an enemy, inflict 1 [GazeReplica] against the attacker (once per Identity per turn)\nTurn Start: if Hong Lu is on the field, inflict 1 [GazeReplica] against Hong Lu
   PL:
388. [[a1c8p3] Pasywka wroga [113502] — nazwa] 손아귀
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113502].name
   limit: do 40 znaków
   EN: Grasp
   PL:
389. [[a1c8p3] Pasywka wroga [113502] — opis] [GraspReplica]가 부여된 대상 우선 공격\n[GraspReplica]가 부여된 대상이 있으면 패턴이 변경되고, 모든 내성 +0.1
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113502].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [GraspReplica]
   znaczenie tagów: [GraspReplica] = 손아귀 / Grasp
   EN: Prioritizes targets with [GraspReplica]\nGains a new pattern when there are targets with [GraspReplica]; +0.1 to all Resistances
   PL:
390. [[a1c8p3] Pasywka wroga [113503] — nazwa] E.G.O 침식 - N사
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113503].name
   limit: do 40 znaków
   EN: E.G.O Corrosion - N Corp.
   PL:
391. [[a1c8p3] Pasywka wroga [113503] — opis] 이 캐릭터가 등장한지 1턴 경과할 때마다 턴 종료시 [EgoErodeReplica] 1 얻음\n- 턴 종료시 자신의 체력이 최대 체력의 50% 미만이거나 정신력이 -20 이하면, [EgoErodeReplica] 1 추가로 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113503].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [EgoErodeReplica]
   znaczenie tagów: [EgoErodeReplica] = E.G.O 침식 - N사 / E.G.O Corrosion - N Corp.
   EN: After entering this Encounter, gain 1 [EgoErodeReplica] at every passing Turn End\n- Turn End: at less than 50% HP, or at -20 SP or less, gain 1 additional [EgoErodeReplica]
   PL:
392. [[a1c8p3] Pasywka wroga [113504] — nazwa] E.G.O 순간 감응도 최대화
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113504].name
   limit: do 50 znaków
   EN: E.G.O Temporary Max Attunement
   PL:
393. [[a1c8p3] Pasywka wroga [113504] — opis] [GazeReplica]이 4 이상인 수감자들이 4명 이상이면, '경외[TabExplain], 경멸[TabExplain] 【잠재 해방】' 스킬 사용
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113504].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [GazeReplica], [TabExplain]
   znaczenie tagów: [GazeReplica] = 시선 / Gaze
   EN: If there are 4+ Sinners with 4+ [GazeReplica] Stacks, use the Skill 'Awe[TabExplain], Contempt[TabExplain] 【Unleashed】' Skill
   PL:
394. [[a1c8p3] Pasywka wroga [113505] — nazwa] 나만 노려봐서는 안 될 텐데
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113505].name
   limit: do 40 znaków
   EN: Better avert your gazes
   PL:
395. [[a1c8p3] Pasywka wroga [113505] — opis] 아군이 있을 때 적 5명 이상이 자신을 메인 타겟으로 지정하면, 해당 적의 체력, 정신력 10 감소
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113505].desc
   limit: do 170 znaków
   EN: Where there are other surviving allies, if this unit becomes the main target from 5+ enemies, those enemies lose 10 HP and SP
   PL:
396. [[a1c8p3] Pasywka wroga [113601] — nazwa] 흉탄 비용
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113601].name
   limit: do 40 znaków
   EN: The Cost of Fell Bullets
   PL:
397. [[a1c8p3] Pasywka wroga [113601] — opis] 공격 적중 시, 정신력 5 회복\n합 패배 시, 정신력 5 감소
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Hit, heal 5 SP; on Clash Lose, lose 5 SP
   PL:
398. [[a1c8p3] Pasywka wroga [113602] — nazwa] 약진
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113602].name
   limit: do 40 znaków
   EN: Charge Forth
   PL:
399. [[a1c8p3] Pasywka wroga [113602] — opis] 적 처치 시, [Breath] 횟수 3 증가
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: On enemy Kill, gain +3 [Breath] Count
   PL:
400. [[a1c8p3] Pasywka wroga [113603] — nazwa] 벗이여, 새로운 시대가 오고 있다네.
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113603].name
   limit: do 60 znaków
   EN: A new era is upon us, my dear fellow.
   PL:
401. [[a1c8p3] Pasywka wroga [113603] — opis] 정신력이 -20 미만이면, 특수 패턴 사용
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113603].desc
   limit: do 120 znaków
   EN: At less than -20 SP, use a special pattern
   PL:
402. [[a1c8p3] Pasywka wroga [113604] — nazwa] 부디 새로운 이상을 위해 헌신해주게.
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113604].name
   limit: do 60 znaków
   EN: Please, dedicate yourself for the new ideal.
   PL:
403. [[a1c8p3] Pasywka wroga [113604] — opis] 가환을 제외한 N사 직원의 체력이 50% 미만이면, 특수 패턴 사용
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=113604].desc
   limit: do 120 znaków
   EN: If an N Corp. Employee(except Jia Huan)'s HP is less than 50%, use a special pattern
   PL:
404. [[a1c8p3] Pasywka wroga [114601] — nazwa] -
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114601].name
   limit: do 40 znaków
   EN: -
   PL:
405. [[a1c8p3] Pasywka wroga [114601] — opis] 체력이 최대 체력의 50% 미만으로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114601].desc
   limit: do 120 znaków
   EN: HP does not drop below 50%
   PL:
406. [[a1c8p3] Pasywka wroga [114602] — nazwa] 보옥아 여기서 가주의 대가 끊기면 안된다…
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114602].name
   limit: do 90 znaków
   EN: Little Baoyu, the lineage of Family Hierarchs cannot end here...
   PL:
407. [[a1c8p3] Pasywka wroga [114602] — opis] 홍루 사망 시 전투 패배. 모든 스킬이 홍루를 우선 타겟팅함
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114602].desc
   limit: do 120 znaków
   EN: Lose Encounter when Hong Lu dies. All Skills prioritize Hong Lu
   PL:
408. [[a1c8p3] Pasywka wroga [114603] — nazwa] 누가 어르신들의 수발을 들고 선황충님의 뜻을 홍원에 펼쳐주겠느냐!!!
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114603].name
   limit: do 130 znaków
   EN: Who shall serve the elders, who shall convey the revered Xianhuang Worm's will to Hongyuan then?!!!
   PL:
409. [[a1c8p3] Pasywka wroga [114603] — opis] 홍루에게 합 승리 후 적중 시 [PileObedient] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114603].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PileObedient]
   znaczenie tagów: [PileObedient] = 쌓이는 순종 / Heaping Obedience
   EN: On Hit after Clash Win against Hong Lu: inflict 1 [PileObedient] (once per Skill)
   PL:
410. [[a1c8p3] Pasywka wroga [114604] — nazwa] 황금가지의 동화 - 부감응
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114604].name
   limit: do 60 znaków
   EN: Golden Bough Assimilation - Malattunement
   PL:
411. [[a1c8p3] Pasywka wroga [114604] — opis] 전투 시작 시 [GoldenBoughSync] 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114604].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GoldenBoughSync]
   znaczenie tagów: [GoldenBoughSync] = 부감응 / Malattunement
   EN: Encounter Start: gain [GoldenBoughSync]
   PL:
412. [[a1c8p3] Pasywka wroga [114605] — nazwa] 홍원금단 - 전흑선환[全黑仙丸]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114605].name
   limit: do 80 znaków
   EN: Forbidden Pill of Hongyuan - Completed Heixian Bolus [全黑仙丸]
   PL:
413. [[a1c8p3] Pasywka wroga [114605] — opis] 서로 다른 종류의 스킬을 사용할 때마다 [AttackUp] 1, [DefenseDown] 1 얻음 (턴당 3회)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114605].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Gain 1 [AttackUp] and 1 [DefenseDown] every time this unit uses a different type of Skill (3 times per turn)
   PL:
414. [[a1c8p3] Pasywka wroga [114606] — nazwa] 예로부터 홍원은 선인들의 뜻에 따라 다뤄져왔다
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114606].name
   limit: do 90 znaków
   EN: Hongyuan has always been a putty in the hands of the revered Xianren
   PL:
415. [[a1c8p3] Pasywka wroga [114606] — opis] 턴 종료 시 패닉 상태면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨\n\n패닉 상태가 해제될 때, 다음 턴에 [Enhancement] 2, [Endurance] 2를 얻고, 홍루에게 [Obedient]이 있으면 정신력 15 회복
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114606].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Endurance], [Obedient]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [Obedient] = 공허한 순종 / Hollow Obedience
   EN: Turn End: if Panicked, recover from Panic at the next Turn Start and reset SP to 0\n\nWhen recovering from Panic, gain 2 [Enhancement] and 2 [Endurance] next turn; if Hong Lu has [Obedient], heal 15 SP
   PL:
416. [[a1c8p3] Pasywka wroga [115201] — nazwa] 소녀를 지켜봐주세요…!
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115201].name
   limit: do 40 znaków
   EN: Watch this little girl...!
   PL:
417. [[a1c8p3] Pasywka wroga [115201] — opis] 홍루 사망 시 전투 패배. 턴 시작 시 자신이 소환한 유닛이 있으면 정신력 10 회복
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115201].desc
   limit: do 130 znaków
   EN: Lose Encounter when Hong Lu dies. If there are this unit's summoned units at Turn Start, heal 10 SP
   PL:
418. [[a1c8p3] Pasywka wroga [115202] — nazwa] 황금가지의 동화- 뒤틀림
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115202].name
   limit: do 60 znaków
   EN: Golden Bough Assimilation - Distortion
   PL:
419. [[a1c8p3] Pasywka wroga [115202] — opis] 2페이즈 시작 시 [GoldenBoughSyncDistorted] 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GoldenBoughSyncDistorted]
   znaczenie tagów: [GoldenBoughSyncDistorted] = 괴력난신 / Supernatural, Strength, Chaos, and Spirits
   EN: Start of the 2nd Phase: gain [GoldenBoughSyncDistorted]
   PL:
420. [[a1c8p3] Pasywka wroga [115203] — nazwa] 모든 가주는 선황충님에게 몸을 내어드리고 그 뜻을 이어받아왔거늘
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115203].name
   limit: do 140 znaków
   EN: Every Family Hierarch has the duty to surrender their bodies to the Xianhuang Worm and his honored will
   PL:
421. [[a1c8p3] Pasywka wroga [115203] — opis] 턴 종료 시 패닉 상태면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨\n\n패닉 상태가 해제될 때,\n- 다음 턴에 [Enhancement] 2, [Endurance] 2, [Agility] 1을 얻음\n- 자신이 소환한 유닛이 있으면 정신력 15 회복\n- 홍루에게 [Obedient]이 있으면 정신력 15 회복
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115203].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Endurance], [Agility], [Obedient]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up; [Agility] = 신속 / Haste; [Obedient] = 공허한 순종 / Hollow Obedience
   EN: Turn End: if Panicked, recover from Panic at the next Turn Start and reset SP to 0\n\nWhen recovering from Panic,\n- gain 2 [Enhancement], 2 [Endurance], and 1 [Agility] next turn\n- If there are units summoned by this unit, heal 15 SP\n- If Hong Lu has [Obedient], heal 15 SP
   PL:
422. [[a1c8p3] Pasywka wroga [115204] — nazwa] -
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115204].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [[a1c8p3] Pasywka wroga [115204] — opis] 체력이 최대 체력의 85% 미만으로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115204].desc
   limit: do 120 znaków
   EN: HP does not drop below 85%
   PL:
424. [[a1c8p3] Pasywka wroga [115205] — nazwa] -
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115205].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [[a1c8p3] Pasywka wroga [115205] — opis] 체력이 최대 체력의 65% 미만으로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115205].desc
   limit: do 120 znaków
   EN: HP does not drop below 65%
   PL:
426. [[a1c8p3] Pasywka wroga [115206] — nazwa] -
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115206].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [[a1c8p3] Pasywka wroga [115206] — opis] 체력이 최대 체력의 50% 미만으로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115206].desc
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [[a1c8p3] Pasywka wroga [115207] — nazwa] 금옥기외 패서기중[金玉其外 敗絮其中]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115207].name
   limit: do 80 znaków
   EN: Rot and Decay in the Husk of Gold and Jade [金玉其外 敗絮其中]
   PL:
429. [[a1c8p3] Pasywka wroga [115207] — opis] [Burst]이 10 이상 부여되어 있을 때 받는 피해량 +10%\n부여된 부정적인 효과 수가 5개 이상이면 받는 피해량 +10%
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115207].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If this unit has 10+ [Burst], take +10% damage\nIf this unit has 5+ types of negative effects, take +10% damage
   PL:
430. [[a1c8p3] Pasywka wroga [115208] — nazwa] 선황충이 임하지 않은 가주는 홍원을 위해 움직이지도 않을 터
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115208].name
   limit: do 110 znaków
   EN: A Family Hierarch without the revered Xianhuang Worm will never serve Hongyuan
   PL:
431. [[a1c8p3] Pasywka wroga [115208] — opis] 체력이 0이 되면, 몸통 부위가 다음 턴에 흐트러짐 상태가 됨\n이후 적출된 상태가 되고, 몸통 부위가 [Vulnerable] 2를 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115208].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: At 0 HP, the Body Part becomes Staggered next turn\nThen, this Part becomes Severed, and the Body Part gains 2 [Vulnerable]
   PL:
432. [[a1c8p3] Pasywka wroga [115209] — nazwa] -
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115209].name
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [[a1c8p3] Pasywka wroga [115209] — opis] 체력이 최대 체력의 20% 미만으로 감소하지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115209].desc
   limit: do 120 znaków
   EN: HP does not drop below 20%
   PL:
434. [[a1c8p3] Pasywka wroga [115301] — nazwa] 선인이시여 봐주십시오!
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115301].name
   limit: do 50 znaków
   EN: Witness Me, O Revered Xianren!
   PL:
435. [[a1c8p3] Pasywka wroga [115301] — opis] 이 유닛이 살아있는 동안 가모가 턴 시작 시 본체와 모든 부위가 보호막 200 얻음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115301].desc
   limit: do 120 znaków
   EN: When this unit is present, Jia Mu gains 200 Shield for her Core and every Part
   PL:
436. [[a1c8p3] Pasywka wroga [115302] — nazwa] 보옥의 소임
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115302].name
   limit: do 40 znaków
   EN: Duties of the Precious Jade
   PL:
437. [[a1c8p3] Pasywka wroga [115302] — opis] 이 유닛이 살아있는 동안 갇혀 있는 캐릭터에게 아래의 효과가 적용됨\n- 행동 불가능 상태가 됨\n- 버프, 체력, 정신력이 갱신되지 않음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115302].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As long as this unit is present, apply the following effects to the caged unit:\n- Become 'immobilized'\n- This unit's buffs, HP, and SP cannot be changed
   PL:
438. [[a1c8p3] Pasywka wroga [115303] — nazwa] 출가
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115303].name
   limit: do 40 znaków
   EN: Departure
   PL:
439. [[a1c8p3] Pasywka wroga [115303] — opis] 이 유닛이 처치되면 다음 턴에 갇혀 있던 캐릭터가 전투에 복귀함.
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115303].desc
   limit: do 120 znaków
   EN: When this unit is defeated, return the caged character to the battle next turn
   PL:
440. [[a1c8p3] Pasywka wroga [115304] — nazwa] 파사현정[破邪顯正]
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115304].name
   limit: do 60 znaków
   EN: Refute the Evil; Restore Justice [破邪顯正]
   PL:
441. [[a1c8p3] Pasywka wroga [115304] — opis] 이 유닛이 수감자들에게 처치되면 아래의 효과가 발동됨\n- 모든 아군 정신력 10 회복, 다음 턴에 [AttackDmgUp] 2 부여\n- 가모에게 다음 2턴 동안 [Binding] 5, [AttackDown] 3, [Vulnerable] 5 부여\n- 이 유닛에 갇혀있던 캐릭터의 정신력이 45까지 회복. 복귀 시 [Enhancement] 2 얻음\n- 모든 E.G.O 자원 3개씩 획득
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115304].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [AttackDmgUp], [Binding], [AttackDown], [Vulnerable], [Enhancement]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Binding] = 속박 / Bind; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: If this unit is defeated by the Sinners, activate the following effects:\n- All allies heal 10 SP; all allies gain 2 [AttackDmgUp] next turn\n- Inflict 5 [Binding], 3 [AttackDown], and 5 [Vulnerable] against Jia Mu for the next 2 turns\n- The unit that was caged in this unit heals up to 45 SP. Gain 2 [Enhancement] upon its return\n- Gain 3 E.G.O Resources to all Affinities
   PL:
442. [[a1c8p3] Pasywka wroga [115401] — nazwa] 지고한 불사의 선인이시여
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115401].name
   limit: do 50 znaków
   EN: O The Supreme Xianren of Immortality
   PL:
443. [[a1c8p3] Pasywka wroga [115401] — opis] [SupremeEternalLife] 효과를 보유하고 있음
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SupremeEternalLife]
   znaczenie tagów: [SupremeEternalLife] = 지고한 불사 / Sublime Immortality
   EN: Has the [SupremeEternalLife] effect
   PL:
444. [[a1c8p3] Pasywka wroga [115402] — nazwa] 불로불사는 영원토록 이어지리
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115402].name
   limit: do 70 znaków
   EN: Let us be eternally free from aging and death
   PL:
445. [[a1c8p3] Pasywka wroga [115402] — opis] 체력이 1 미만으로 감소하지 않음\n체력이 1이 될 때, [SupremeEternalLife] 효과가 [ImperfectEternalLife]로 변경됨
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115402].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [SupremeEternalLife], [ImperfectEternalLife]
   znaczenie tagów: [SupremeEternalLife] = 지고한 불사 / Sublime Immortality; [ImperfectEternalLife] = 불완전한 불사 / Imperfect Immortality
   EN: HP does not drop below 1\n\nAt 1 HP, replace [SupremeEternalLife] with [ImperfectEternalLife]
   PL:
446. [[a1c8p3] Pasywka wroga [115403] — nazwa] 불로불사의 지식
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115403].name
   limit: do 40 znaków
   EN: Knowledge of Immortality
   PL:
447. [[a1c8p3] Pasywka wroga [115403] — opis] 피격 시 체력이 1이 되면, 자신을 공격한 수감자의 정신력을 10 회복시키고, 수량이 부족한 E.G.O 자원 중 무작위 속성 자원 3개 획득 (이 유닛이 생존해있는동안 1회 발동)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=115403].desc
   limit: do 260 znaków
   EN: If this unit's HP drops to 1 upon getting hit, heal 10 SP to the Sinner who attacked this unit; then, gain 3 random E.G.O Resources for the least-owned Sin Affinities (activates once for this unit)
   PL:
448. [[a1c8p3] Pasywka wroga [114513] — nazwa] 패닉 회복
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114513].name
   limit: do 40 znaków
   EN: Panic Recovery
   PL:
449. [[a1c8p3] Pasywka wroga [114513] — opis] 턴 종료 시 패닉 상태라면, 정신력이 0이 됨\n\n패닉 상태가 해제되면 다음 턴 시작 시, 자신의 잃은 체력 비율 수치만큼 정신력 회복 (최대 30)
   źródło: Passives_Abnormality-a1c8p3.json :: dataList[id=114513].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: if this unit is Panicked, reset SP to 0\n\nWhen recovering from Panic: at the next Turn Start, heal SP by this unit's missing HP (max 30)
   PL:

## [a1c8p3] Pasywka wroga: Passives_Enemy-a1c8p3
- plik gry: `Passives_Enemy-a1c8p3.json`

450. [[a1c8p3] Pasywka wroga [9021701] — nazwa] 규율 집행 - 준비 단계
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021701].name
   limit: do 60 znaków
   EN: Esecuzione della Regola - Preparation Stage
   PL:
451. [[a1c8p3] Pasywka wroga [9021701] — opis] 전 턴에 [VibrationExplosion]을 시켰다면, 다음 턴에 [Enhancement] 1, [AttackDmgUp] 1 얻음
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021701].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [VibrationExplosion], [Enhancement], [AttackDmgUp]
   znaczenie tagów: [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: If this unit triggered [VibrationExplosion] last turn, gain 1 [Enhancement] and 1 [AttackDmgUp] next turn
   PL:
452. [[a1c8p3] Pasywka wroga [9021702] — nazwa] 규율 집행 - 아랫턱 부수기
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021702].name
   limit: do 70 znaków
   EN: Esecuzione della Regola - Crush the Lower Jaw
   PL:
453. [[a1c8p3] Pasywka wroga [9021702] — opis] 흐트러진 적에게 피해량 +10%\n전 턴에 적을 흐트러뜨렸다면, 다음 턴에 합 승리 후 스킬 적중시 [Vibration] 2 부여 (턴 당 2회)
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021702].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal +10% damage against Staggered enemies\nIf an enemy was Staggered in the last turn: for the next turn, inflict 2 [Vibration] On Hit with a Skill after Clash Win (2 times per turn)
   PL:
454. [[a1c8p3] Pasywka wroga [9021703] — nazwa] 어긋난 규율
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021703].name
   limit: do 40 znaków
   EN: Regola Infranta
   PL:
455. [[a1c8p3] Pasywka wroga [9021703] — opis] 죽은 아군이 1명 이상이라면, 다음 턴부터 [ParryingResultUp] 1 얻음
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: If 1 or more ally has been defeated, gain 1 [ParryingResultUp] starting next turn
   PL:
456. [[a1c8p3] Pasywka wroga [9021301] — nazwa] 네잎클로버
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021301].name
   limit: do 40 znaków
   EN: Four-leaf Clover
   PL:
457. [[a1c8p3] Pasywka wroga [9021301] — opis] 턴 시작 시, [Breath] 5 획득, [Breath] 횟수 2 증가\n전투 시작 단계에서 [Breath] 상태인 아군이 스킬을 사용하여 적에게 치명타 피해를 입힐 경우, 다음 턴 시작 시 랜덤 아군에게 [Breath] 위력 5 부여, [Breath] 횟수 2 증가. (턴 당 1회 발동)
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021301].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn Start: gain 5 [Breath] and +2 [Breath] Count\nCombat Start: if an ally with [Breath] Critically Hits an enemy with a Skill, apply 5 [Breath] Potency and +2 [Breath] Potency to a random ally at the next Turn Start (once per turn)
   PL:
458. [[a1c8p3] Pasywka wroga [9021302] — nazwa] 맛있는 살점
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021302].name
   limit: do 40 znaków
   EN: Tasty Flesh
   PL:
459. [[a1c8p3] Pasywka wroga [9021302] — opis] 체력 50% 이하일 시, [Laceration]이 있는 적에게 공격 적중 시, 상대의 [Laceration] 당 자신의 전체 체력의 1% 만큼 회복 (최대 10 %, 전투 당 1회 발동)
   źródło: Passives_Enemy-a1c8p3.json :: dataList[id=9021302].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: At 50%- HP: On Hit against enemies with [Laceration], heal 1% HP for every [Laceration] on target (max 10%; once per Encounter)
   PL:

## [a1c9115] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9115
- grupa rozdziału/trybu: `a1c9115` · plik: `Skills_Abnormality-a1c9115.json`

460. [Umiejętność wroga [112204] (ulepszenie 1) — nazwa] 살주
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].name
   limit: do 40 znaków
   EN: Overthrow
   PL:
461. [Umiejętność wroga [112204] (ulepszenie 1) — opis] [WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +3 [Breath] Count
   PL:
462. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴된 코인이면, 최종 위력 10 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If this Coin is Cracked, lose 10 Final Power
   PL:
464. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Breath] 3 얻음, [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] and +1 [Breath] Count
   PL:
465. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Laceration] Count
   PL:
466. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴된 코인이면, 최종 위력 10 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [SlashDamageUp] 2 얻음
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashDamageUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up
   EN: [OnSucceedAttack] Gain 2 [SlashDamageUp] next turn
   PL:
469. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [SlashResistDown] 2 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [SlashResistDown]
   PL:
470. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 3, efekt 2 — opis] 파괴된 코인이면, 최종 위력 10 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 5 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Laceration]
   PL:
473. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL:
474. [Umiejętność wroga [112204] (ulepszenie 1) — moneta 3, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112204].levelList[level=1].coinlist[#2].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
475. [Umiejętność wroga [112205] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].name
   limit: do 40 znaków
   EN: To Claim Their Bones
   PL:
476. [Umiejętność wroga [112205] (ulepszenie 1) — opis] [StartBattle] 보호막 100 얻음\n[WhenUse] 보호막이 전부 소모되지 않았다면, 합 위력 +5
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]
   EN: [StartBattle] Gain 100 Shield\n[WhenUse] If the Shield isn't fully depleted, Clash Power +5
   PL:
477. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴된 코인이면, 최종 위력 20 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If this Coin is Cracked, lose 20 Final Power
   PL:
479. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [SlashResistDown] 3 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [SlashResistDown]
   PL:
480. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴된 코인이면, 최종 위력 20 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] +100% Damage on Critical Hit
   PL:
483. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Laceration] and +2 [Laceration] Count
   PL:
484. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 3, efekt 2 — opis] 파괴된 코인이면, 최종 위력 20 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Umiejętność wroga [112205] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 보호막이 전부 소모되지 않았다면, 공격 가중치만큼 [Grudge] 수치를 나눠 고정 피해로 부여함.
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112205].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Grudge]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [UnBrokenCoinOnSucceedAttack] If the Shield isn't fully depleted, divide [Grudge] value by Atk Weight and inflict it as fixed damage.
   PL:
487. [Umiejętność wroga [112305] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].name
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Umiejętność wroga [112305] (ulepszenie 1) — opis] [StartBattle] 보호막 250 얻음\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] 보호막이 전부 소모되지 않았다면, 합 위력 +10
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Gain 250 Shield\n[WhenUse] Gain +3 [Breath] Count\n[WhenUse] If the Shield isn't fully depleted, Clash Power +10
   PL:
489. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴된 코인이면, 최종 위력 23 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If this Coin is Cracked, lose 23 Final Power
   PL:
491. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [SlashResistDown] 3 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [SlashResistDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SlashResistDown] = 참격 내성 약화 / Slash Resist Down
   EN: [OnSucceedAttack] Inflict 3 [SlashResistDown]
   PL:
492. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴된 코인이면, 최종 위력 23 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 크리티컬 피해량 +100%
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [Paralysis] 5 부여
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Paralysis]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Paralysis] = 마비 / Paralyze
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Paralysis] next turn
   PL:
496. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 2, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 10 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#1].coindescs[#4].desc
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 3, efekt 2 — opis] 파괴된 코인이면, 최종 위력 23 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Umiejętność wroga [112305] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 보호막이 전부 소모되지 않았다면, 공격 가중치만큼 [Grudge] 수치를 나눠 고정 피해로 부여함.
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112305].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [112309] (ulepszenie 1) — nazwa] 골단
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].name
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Umiejętność wroga [112309] (ulepszenie 1) — opis] [CantChangeTarget]\n체력이 가장 없는 대상 우선 공격\n[EnemyKill] [Grudge]가 2배가 됨.\n[EnemyKill] [Grudge]만큼 체력 회복
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [EnemyKill], [Grudge]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [EnemyKill] = [적 처치 시] / [On Kill]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [CantChangeTarget]\nPrioritizes the unit with the least HP\n[EnemyKill] Double the [Grudge] value.\n[EnemyKill] Heal HP equal to [Grudge] value
   PL:
502. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 1, efekt 2 — opis] 파괴된 코인이면, 최종 위력 25 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   EN: If this Coin is Cracked, lose 25 Final Power
   PL:
504. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 2, efekt 2 — opis] 파괴된 코인이면, 최종 위력 25 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 3, efekt 2 — opis] 파괴된 코인이면, 최종 위력 25 감소
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność wroga [112309] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Grudge] 수치만큼 고정 피해.
   źródło: Skills_Abnormality-a1c9115.json :: dataList[id=112309].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Grudge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Grudge] = 맺혀가는 응어리 / Growing Resentment
   EN: [OnSucceedAttack] Deal fixed damage equal to [Grudge] value.
   PL:

## [a1c9115] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c9115
- grupa rozdziału/trybu: `a1c9115` · plik: `Skills_Enemy-a1c9115.json`

509. [Umiejętność wroga [9101905] (ulepszenie 1) — nazwa] 쾌청 베기
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].name
   limit: do 40 znaków
   EN: Sky-clearing Cut
   PL:
510. [Umiejętność wroga [9101905] (ulepszenie 1) — opis] [StartBattle] 메인 타겟의 [Laceration]이 5이상이면, 공격 가중치 +1\n[StartBattle] 이번 턴에 사용하는 공격 스킬이 4개 이상이면, 최종 위력 +5\n[WinDuel] 모든 아군 정신력 15 회복\n대상의 [Laceration]이 7 이상이면, 피해량 +30%
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Laceration], [WinDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [StartBattle] If the main target has 5+ [Laceration], Atk Weight +1\n[StartBattle] If this unit will use 4+ Attack Skills this turn, Final Power +5\n[WinDuel] All allies heal 15 SP\nIf target has 7+ [Laceration], deal +30% damage
   PL:
511. [Umiejętność wroga [9101905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 2 [Laceration]
   PL:
512. [Umiejętność wroga [9101905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict 3 [Laceration]
   PL:
513. [Umiejętność wroga [9101905] (ulepszenie 1) — moneta 3, efekt 1 — opis] 대상의 [Laceration]이 7 이상이면, 피해량 +50%
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 7+ [Laceration], deal +50% damage
   PL:
514. [Umiejętność wroga [9101905] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 10 부여
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101905].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +10 [Laceration] Count
   PL:
515. [Umiejętność wroga [9101906] (ulepszenie 1) — nazwa] 뒷골목의 규칙
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101906].levelList[level=1].name
   limit: do 40 znaków
   EN: Rules of the Backstreets
   PL:
516. [Umiejętność wroga [9101906] (ulepszenie 1) — opis] [WhenUse] 자신 제외 살아있는 아군 수만큼 1코인 추가 (최대 3)
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101906].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Add 1 more coin per every surviving other ally (max 3)
   PL:
517. [Umiejętność wroga [9101906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2, [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration] and +2 [Laceration] Count
   PL:
518. [Umiejętność wroga [9101906] (ulepszenie 1) — moneta 1, efekt 2 — opis] [EnemyKill] 모든 아군 정신력 20 회복
   źródło: Skills_Enemy-a1c9115.json :: dataList[id=9101906].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] All allies heal 20 SP
   PL:

## [a1c9116] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c9116
- grupa rozdziału/trybu: `a1c9116` · plik: `Skills_Abnormality-a1c9116.json`

519. [Umiejętność wroga [112701] (ulepszenie 1) — nazwa] 시험은 끝났다
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112701].levelList[level=1].name
   limit: do 40 znaków
   EN: No More Tests
   PL:
520. [Umiejętność wroga [112701] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [HitDamageUp] 3 얻음\n[WhenUse] 메인 타겟의 [MiddleFingerBook] 수치가 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112701].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [HitDamageUp], [MiddleFingerBook], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Gain 3 [HitDamageUp] next turn\n[WhenUse] If the main target has 3+ [MiddleFingerBook], convert all Coins on this Skill to [SuperCoin]s
   PL:
521. [Umiejętność wroga [112701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [112702] (ulepszenie 1) — nazwa] 고통 새기기
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].name
   limit: do 40 znaków
   EN: Promised Suffering
   PL:
523. [Umiejętność wroga [112702] (ulepszenie 1) — opis] [MiddleFingerBook] 수치가 가장 높은 대상을 우선 지정\n[WhenUse] 대상의 [MiddleFingerBook] 수치가 3 이상이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [WhenUse], [SuperCoin]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Prioritizes targets with the highest [MiddleFingerBook] Stack\n[WhenUse] If target has 3+ [MiddleFingerBook], convert all Coins on this Skill to [SuperCoin]s
   PL:
524. [Umiejętność wroga [112702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] this turn and next turn
   PL:
525. [Umiejętność wroga [112702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [112702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (대상의 [MiddleFingerBook] 수치 x 3)만큼 타격 추가 피해
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Inflict ([MiddleFingerBook] on the target x 3) Blunt bonus damage
   PL:
527. [Umiejętność wroga [112702] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 모든 [MiddleFingerBook] 제거
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112702].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Remove all [MiddleFingerBook] on the target
   PL:
528. [Umiejętność wroga [112703] (ulepszenie 1) — nazwa] 장난이 길었군
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112703].levelList[level=1].name
   limit: do 40 znaków
   EN: Enough Games
   PL:
529. [Umiejętność wroga [112703] (ulepszenie 1) — opis] [StartBattle] 모든 아군의 정신력 10 회복\n[EndBattle] 패닉 상태인 아군이 있으면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력을 0으로 초기화함\n[EndBattle] 다음 턴에 자신을 포함한 모든 아군에게 [HitResultUp] 1 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112703].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [EndBattle], [HitResultUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [HitResultUp] = 타격 위력 증가 / Blunt Power Up
   EN: [StartBattle] Heal all allies' SP by 10\n[EndBattle] If there are Panicked allies, recover them from Panic at the next Turn Start and reset their SP to 0\n[EndBattle] Apply 1 [HitResultUp] to all allies, including this unit
   PL:
530. [Umiejętność wroga [112704] (ulepszenie 1) — nazwa] 전원, 처형이다!!!
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112704].levelList[level=1].name
   limit: do 50 znaków
   EN: COMPLETE AND TOTAL EXTERMINATION!!!
   PL:
531. [Umiejętność wroga [112704] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n메인 타겟의 [MiddleFingerBook] 수치가 5 이상이면, 최종 위력 +5\n[DefeatDuel] 최종 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill] 공격 당한 모든 대상의 [MiddleFingerBook] 제거
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112704].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [DefeatDuel], [EndSkill]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed\nIf the main target has 5+ [MiddleFingerBook], Final Power +5\n[DefeatDuel] Deal -80% final damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] Remove [MiddleFingerBook] from all targets that were hit
   PL:
532. [Umiejętność wroga [112704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Umiejętność wroga [112704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] (대상의 [MiddleFingerBook] 수치 x 10)만큼 타격 추가 피해
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark
   EN: [OnSucceedAttack] Inflict ([MiddleFingerBook] on the target x 10) Blunt bonus damage
   PL:
534. [Umiejętność wroga [112601] (ulepszenie 1) — nazwa] 초격
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112601].levelList[level=1].name
   limit: do 40 znaków
   EN: Startling Strike
   PL:
535. [Umiejętność wroga [112601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Burst], Clash Power +1
   PL:
536. [Umiejętność wroga [112601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [112602] (ulepszenie 1) — nazwa] 척살
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112602].levelList[level=1].name
   limit: do 40 znaków
   EN: Perforating Kill
   PL:
538. [Umiejętność wroga [112602] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 합 위력 +1\n[WhenUse] [LegStrength] 3 얻음
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112602].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [LegStrength]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [WhenUse] If target has 5+ [Burst], Clash Power +1\n[WhenUse] Gain 3 [LegStrength]
   PL:
539. [Umiejętność wroga [112602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [112602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BurstAgility]이 있으면, 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] If target has [BurstAgility], gain 1 [Agility] next turn
   PL:
541. [Umiejętność wroga [112603] (ulepszenie 1) — nazwa] 표각
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112603].levelList[level=1].name
   limit: do 40 znaków
   EN: Etching Strike
   PL:
542. [Umiejętność wroga [112603] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 5 이상이면, 코인 위력 +1
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112603].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 5+ [Burst], Coin Power +1
   PL:
543. [Umiejętność wroga [112603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Umiejętność wroga [112603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Umiejętność wroga [112603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BurstAgility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: [OnSucceedAttack] Inflict [BurstAgility]
   PL:
546. [Umiejętność wroga [112604] (ulepszenie 1) — nazwa] 각주살검 - 순보
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].name
   limit: do 50 znaków
   EN: Cursewrit Butcherblade - Blinkstep
   PL:
547. [Umiejętność wroga [112604] (ulepszenie 1) — opis] [BurstAgility]이 있는 대상을 우선 공격함\n자신과 대상의 속도 차이 2 당 피해량 +15% (최대 60%)\n[WhenUse] 대상의 [Burst]이 5 당, 코인 위력 +1 (최대 2)\n[WhenUse] 대상의 [Burst] 횟수 2 당, 기본 위력 +1 (최대 3)\n[EndSkill] 자신의 속도가 10 이상이고 대상이 사망했다면, 이 스킬을 무작위 대상 한 명에게 다시 사용함 (턴 당 1회)
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n, [BurstAgility], [WhenUse], [Burst], [EndSkill]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Prioritizes targets with [BurstAgility]\nDeal +15% damage for every 2 Speed difference between this unit and the target (max 60%)\n[WhenUse] Coin Power +1 for every 5 [Burst] on the target (max 2)\n[WhenUse] Base Power +1 for every 2 [Burst] Count on the target (max 3)\n[EndSkill] At 10+ Speed, and if the target is defeated, Reuse this Skill against a random enemy (once per turn)
   PL:
548. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 5 [Burst]
   PL:
552. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BurstAgility]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】
   EN: If target has [BurstAgility], deal +50% damage
   PL:
554. [Umiejętność wroga [112604] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112604].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Umiejętność wroga [112605] (ulepszenie 1) — nazwa] 각주
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112605].levelList[level=1].name
   limit: do 40 znaków
   EN: Cursewrit
   PL:
556. [Umiejętność wroga [112605] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상에게 [BurstAgility]이 있으면, 이 스킬에서 부여하는 [Burst] 횟수 1 추가 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112605].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WhenUse], [BurstAgility], [Burst]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Burst] = 파열 / Rupture
   EN: [DuelCounter]\n[WhenUse] If target has [BurstAgility], inflict +1 more [Burst] Count with this Skill
   PL:
557. [Umiejętność wroga [112605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność wroga [112605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +1 [Burst] Count
   PL:
559. [Umiejętność wroga [112605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Abnormality-a1c9116.json :: dataList[id=112605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9116] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c9116
- grupa rozdziału/trybu: `a1c9116` · plik: `Skills_Enemy-a1c9116.json`

560. [Umiejętność wroga [9018301] (ulepszenie 1) — nazwa] 예의없는 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018301].levelList[level=1].name
   limit: do 40 znaków
   EN: Unmannerly Attack
   PL:
561. [Umiejętność wroga [9018301] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: [WhenUse] Gain 1 [Agility] next turn
   PL:
562. [Umiejętność wroga [9018301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność wroga [9018302] (ulepszenie 1) — nazwa] 힘줄 베기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018302].levelList[level=1].name
   limit: do 40 znaków
   EN: Tendon Slice
   PL:
564. [Umiejętność wroga [9018302] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 대상보다 빠르면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 3 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018302].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] If this unit's Speed is faster than the target's, Coin Power +1\n[WhenUse] If target has 3+ [Laceration], Base Power +1
   PL:
565. [Umiejętność wroga [9018302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Umiejętność wroga [9018302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Umiejętność wroga [9018302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Umiejętność wroga [9018303] (ulepszenie 1) — nazwa] 무질서한 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018303].levelList[level=1].name
   limit: do 40 znaków
   EN: Messy Attack
   PL:
569. [Umiejętność wroga [9018303] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 7 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 4 이상이면, 코인 위력 +1\n[WinDuel] 합 횟수에 비례하여 피해량이 증가 (합 횟수 1당 +5% 최대 50%)\n[WinDuel] [Laceration] 횟수 3 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018303].levelList[level=1].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 7+ Speed, Coin Power +1\n[WhenUse] If target has 4+ [Laceration], Coin Power +1\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, max 50%)\n[WinDuel] Inflict +3 [Laceration] Count
   PL:
570. [Umiejętność wroga [9018303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność wroga [9018303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność wroga [9018304] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018304].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL:
573. [Umiejętność wroga [9018304] (ulepszenie 1) — opis] [WhenUse] 자신이 보유한 부정적인 효과당 3의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018304].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Gain 3 Shield for every type of negative effect on self (max 10)
   PL:
574. [Umiejętność wroga [9018401] (ulepszenie 1) — nazwa] 베어내기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018401].levelList[level=1].name
   limit: do 40 znaków
   EN: Cleave
   PL:
575. [Umiejętność wroga [9018401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność wroga [9018402] (ulepszenie 1) — nazwa] 다리 상처내기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018402].levelList[level=1].name
   limit: do 40 znaków
   EN: Leg Wound
   PL:
577. [Umiejętność wroga [9018402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 3 [Laceration] on target (max 2)
   PL:
578. [Umiejętność wroga [9018402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność wroga [9018402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność wroga [9018402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 1 [Paralysis] next turn
   PL:
581. [Umiejętność wroga [9018403] (ulepszenie 1) — nazwa] 무차별 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018403].levelList[level=1].name
   limit: do 40 znaków
   EN: Wild Swipe
   PL:
582. [Umiejętność wroga [9018403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018403].levelList[level=1].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność wroga [9018403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność wroga [9018403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność wroga [9018404] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018404].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL:
586. [Umiejętność wroga [9018404] (ulepszenie 1) — opis] [BeforeHit] 자신이 보유한 부정적인 효과당 2의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BeforeHit]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]
   EN: [BeforeHit] Gain 2 Shield for every type of negative effect on self (max 10)
   PL:
587. [Umiejętność wroga [9018404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 보호막이 있다면, 대상에게 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] If this unit has Shield, inflict 1 [Paralysis] on target next turn
   PL:
588. [Umiejętność wroga [9018701] (ulepszenie 1) — nazwa] 연료 뽑기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018701].levelList[level=1].name
   limit: do 40 znaków
   EN: Extract Fuel
   PL:
589. [Umiejętność wroga [9018701] (ulepszenie 1) — opis] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018701].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 2+ [Laceration], Coin Power +1
   PL:
590. [Umiejętność wroga [9018701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność wroga [9018701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność wroga [9018701] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 체력 2 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018701].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 2 HP
   PL:
593. [Umiejętność wroga [9018702] (ulepszenie 1) — nazwa] 뒷골목 청소
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018702].levelList[level=1].name
   limit: do 40 znaków
   EN: Sweep the Backstreets
   PL:
594. [Umiejętność wroga [9018702] (ulepszenie 1) — opis] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018702].levelList[level=1].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Umiejętność wroga [9018702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL:
596. [Umiejętność wroga [9018702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność wroga [9018703] (ulepszenie 1) — nazwa] 쓰레기 처리
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].name
   limit: do 40 znaków
   EN: Trash Disposal
   PL:
598. [Umiejętność wroga [9018703] (ulepszenie 1) — opis] 대상의 [Laceration]이 4 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If target has 4+ [Laceration], Coin Power +1
   PL:
599. [Umiejętność wroga [9018703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL:
600. [Umiejętność wroga [9018703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność wroga [9018703] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 1 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Umiejętność wroga [9018703] (ulepszenie 1) — moneta 2, efekt 3 — opis] 이 코인에서 적중 시, 입힌 체력 피해량의 30%만큼 체력 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   EN: On Hit using this Coin, heal 30% of the HP damage dealt
   PL:
603. [Umiejętność wroga [9018703] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttackHead] 이 코인 재사용 (스킬 당 최대 3회)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018703].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Reuse this Coin (3 times per Skill)
   PL:
604. [Umiejętność wroga [9018704] (ulepszenie 1) — nazwa] 333..1973
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].name
   limit: do 40 znaków
   EN: 333..1973
   PL:
605. [Umiejętność wroga [9018704] (ulepszenie 1) — opis] [StartBattle] [Persistent] 4 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Persistent]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Persistent] = 끈질김 / Persistence
   EN: [StartBattle] Gain 4 [Persistent]
   PL:
606. [Umiejętność wroga [9018704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność wroga [9018704] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 흐트러짐 5 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 5
   PL:
608. [Umiejętność wroga [9018704] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność wroga [9018704] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 출혈 횟수 3 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018704].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count
   PL:
610. [Umiejętność wroga [9018705] (ulepszenie 1) — nazwa] 가족을 위하여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018705].levelList[level=1].name
   limit: do 40 znaków
   EN: For the Family
   PL:
611. [Umiejętność wroga [9018705] (ulepszenie 1) — opis] [StartBattle] 무작위 아군 2명에게 [Protection] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018705].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [Protection]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection
   EN: [StartBattle] Apply 1 [Protection] to 2 random allies
   PL:
612. [Umiejętność wroga [9018706] (ulepszenie 1) — nazwa] 뒷골목의 밤
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].name
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL:
613. [Umiejętność wroga [9018706] (ulepszenie 1) — opis] 대상의 [Laceration]이 2 이상이면, 코인 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].desc
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 체력 8 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 8 HP
   PL:
615. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 체력 8 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 흐트러짐 8 회복
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Lower user's Stagger Threshold by 8
   PL:
619. [Umiejętność wroga [9018706] (ulepszenie 1) — moneta 2, efekt 4 — opis] [OnSucceedAttack] 대상의 [Laceration] 1 회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018706].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on the target once (reduce [Laceration] Count by 1)
   PL:
620. [Umiejętność wroga [9019301] (ulepszenie 1) — nazwa] 갑작스런 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019301].levelList[level=1].name
   limit: do 40 znaków
   EN: Sudden Strike
   PL:
621. [Umiejętność wroga [9019301] (ulepszenie 1) — opis] [WhenUse] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019301].levelList[level=1].desc
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność wroga [9019301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Umiejętność wroga [9019302] (ulepszenie 1) — nazwa] 근육 베기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019302].levelList[level=1].name
   limit: do 40 znaków
   EN: Muscle Slice
   PL:
624. [Umiejętność wroga [9019302] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 대상보다 빠르면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 3 이상이면, 기본 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019302].levelList[level=1].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Umiejętność wroga [9019302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Umiejętność wroga [9019302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Umiejętność wroga [9019302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność wroga [9019303] (ulepszenie 1) — nazwa] 무분별한 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019303].levelList[level=1].name
   limit: do 40 znaków
   EN: Indiscriminate Attack
   PL:
629. [Umiejętność wroga [9019303] (ulepszenie 1) — opis] [WhenUse] 자신의 속도가 7 이상이면, 코인 위력 +1\n[WhenUse] 대상의 [Laceration]이 4 이상이면, 코인 위력 +1\n[WinDuel] 합 횟수에 비례하여 피해량이 증가 (합 횟수 1당 +5% 최대 50%)\n[WinDuel] [Laceration] 5 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019303].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] At 7+ Speed, Coin Power +1\n[WhenUse] If target has 4+ [Laceration], Coin Power +1\n[WinDuel] Deal more damage based on Clash count (+5% per Clash count, max 50%)\n[WinDuel] Inflict 5 [Laceration]
   PL:
630. [Umiejętność wroga [9019303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność wroga [9019303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność wroga [9019304] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019304].levelList[level=1].name
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność wroga [9019304] (ulepszenie 1) — opis] [WhenUse] 자신이 보유한 부정적인 효과당 3의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019304].levelList[level=1].desc
   (powtórzenie elementu 573 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność wroga [9019401] (ulepszenie 1) — nazwa] 가르기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019401].levelList[level=1].name
   limit: do 40 znaków
   EN: Slice
   PL:
635. [Umiejętność wroga [9019401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność wroga [9019402] (ulepszenie 1) — nazwa] 근육 상처내기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019402].levelList[level=1].name
   limit: do 40 znaków
   EN: Muscle Wound
   PL:
637. [Umiejętność wroga [9019402] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019402].levelList[level=1].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Umiejętność wroga [9019402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Umiejętność wroga [9019402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Umiejętność wroga [9019402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność wroga [9019403] (ulepszenie 1) — nazwa] 신속한 공격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019403].levelList[level=1].name
   limit: do 40 znaków
   EN: Swift Attack
   PL:
642. [Umiejętność wroga [9019403] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 3당, 코인 위력 +1 (최대 2)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019403].levelList[level=1].desc
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Umiejętność wroga [9019403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Umiejętność wroga [9019403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Umiejętność wroga [9019404] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019404].levelList[level=1].name
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Umiejętność wroga [9019404] (ulepszenie 1) — opis] [BeforeHit] 자신이 보유한 부정적인 효과당 2의 보호막을 얻음 (최대 10)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019404].levelList[level=1].desc
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność wroga [9019404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 보호막이 있다면, 대상에게 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9019404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Umiejętność wroga [9018501] (ulepszenie 1) — nazwa] 초격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018501].levelList[level=1].name
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Umiejętność wroga [9018501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ [Burst], Clash Power +1
   PL:
650. [Umiejętność wroga [9018501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność wroga [9018502] (ulepszenie 1) — nazwa] 억제
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018502].levelList[level=1].name
   limit: do 40 znaków
   EN: Restraint
   PL:
652. [Umiejętność wroga [9018502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Umiejętność wroga [9018502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Umiejętność wroga [9018502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Umiejętność wroga [9018502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack]  자신의 (속도 / 4)만큼 이 코인을 재사용함 (최대 2번)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin (this unit's Speed / 4) times (max 2)
   PL:
656. [Umiejętność wroga [9018503] (ulepszenie 1) — nazwa] 쾌격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].name
   limit: do 40 znaków
   EN: Feather Strike
   PL:
657. [Umiejętność wroga [9018503] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Burst], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture; [WinDuel] = [합 승리시] / [Clash Win]
   EN: If this unit's Speed is faster than the target's gain Coin Power based on Speed difference (Coin Power +1 for every 2 Speed difference; max 3)\n[WhenUse] If target has 4+ [Burst], Coin Power +1\n[WinDuel] Inflict +3 [Burst] Count
   PL:
658. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 1 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność wroga [9018503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [LegStrength] 3 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [LegStrength]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [LegStrength] = 각력【묘】 / Strider【Mao】
   EN: [OnSucceedAttack] Gain 3 [LegStrength]
   PL:
664. [Umiejętność wroga [9018504] (ulepszenie 1) — nazwa] 준비 동작
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018504].levelList[level=1].name
   limit: do 40 znaków
   EN: The Windup
   PL:
665. [Umiejętność wroga [9018504] (ulepszenie 1) — opis] [DuelCounter]\n[WinDuel] 다음 턴에 [Agility]을 3 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018504].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [DuelCounter], [WinDuel], [Agility]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WinDuel] = [합 승리시] / [Clash Win]; [Agility] = 신속 / Haste
   EN: [DuelCounter] \n[WinDuel] Gain 3 [Agility] next turn
   PL:
666. [Umiejętność wroga [9018601] (ulepszenie 1) — nazwa] 추격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018601].levelList[level=1].name
   limit: do 40 znaków
   EN: Pursuit
   PL:
667. [Umiejętność wroga [9018601] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst]이 3 이상이면, 합 위력 +1
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018601].levelList[level=1].desc
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność wroga [9018601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Umiejętność wroga [9018602] (ulepszenie 1) — nazwa] 압도
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018602].levelList[level=1].name
   limit: do 40 znaków
   EN: Overwhelm
   PL:
670. [Umiejętność wroga [9018602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność wroga [9018602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Umiejętność wroga [9018602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Umiejętność wroga [9018602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 (속도 / 4)만큼 이 코인을 재사용함 (최대 2번)
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]
   EN: [UnBrokenCoinOnSucceedAttack] Reuse this Coin (this unit's Speed / 4) times (max 2)
   PL:
674. [Umiejętność wroga [9018603] (ulepszenie 1) — nazwa] 암격
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].name
   limit: do 40 znaków
   EN: Umbra Strike
   PL:
675. [Umiejętność wroga [9018603] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높을수록 코인 위력 +1 (속도 차이 2 당 코인 위력 +1. 최대 3)\n[WhenUse] 대상의 [Burst]이 4 이상이면, 코인 위력 +1\n[WinDuel] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].desc
   (powtórzenie elementu 657 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 1 [Burst]
   PL:
678. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BurstAgility] 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 3, efekt 2 — opis] 대상에게 [BurstAgility]이 있으면, 피해량 +50%
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Umiejętność wroga [9018603] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [LegStrength] 3 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018603].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 663 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność wroga [9018604] (ulepszenie 1) — nazwa] 준비 동작
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018604].levelList[level=1].name
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Umiejętność wroga [9018604] (ulepszenie 1) — opis] [DuelCounter]\n[WinDuel] 다음 턴에 [Agility]을 3 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9018604].levelList[level=1].desc
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Umiejętność wroga [9102001] (ulepszenie 1) — nazwa] 명치 노리기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102001].levelList[level=1].name
   limit: do 40 znaków
   EN: Aim for the Solar Plexus
   PL:
685. [Umiejętność wroga [9102001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Umiejętność wroga [9102002] (ulepszenie 1) — nazwa] 머리 후리기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102002].levelList[level=1].name
   limit: do 40 znaków
   EN: Right in the Dome
   PL:
687. [Umiejętność wroga [9102002] (ulepszenie 1) — opis] [WhenUse] 대상이 [MiddleFingerBook]이면, 이 스킬에서 부여하는 [DefenseDown] 2 추가 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102002].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MiddleFingerBook], [DefenseDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [WhenUse] If target has [MiddleFingerBook], inflict 2 additional [DefenseDown] with this Skill
   PL:
688. [Umiejętność wroga [9102002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Umiejętność wroga [9102002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność wroga [9102003] (ulepszenie 1) — nazwa] 복부 으깨기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].name
   limit: do 40 znaków
   EN: Gut Crush
   PL:
691. [Umiejętność wroga [9102003] (ulepszenie 1) — opis] [WhenUse] 대상이 [MiddleFingerBook]이면, 이 스킬에서 부여하는 [AttackDown] 1 추가 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [MiddleFingerBook], [AttackDown]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [WhenUse] If target has [MiddleFingerBook], inflict 1 additional [AttackDown] with this Skill
   PL:
692. [Umiejętność wroga [9102003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackDown]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: [OnSucceedAttackHead] Inflict 1 [AttackDown] next turn
   PL:
693. [Umiejętność wroga [9102003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [MiddleFingerBook]이면, 다음 턴에 [PlusCoinValueUp] 1 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MiddleFingerBook], [PlusCoinValueUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: [OnSucceedAttack] If target has [MiddleFingerBook], gain 1 [PlusCoinValueUp] next turn
   PL:
694. [Umiejętność wroga [9102003] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 [AttackDown] 1 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Umiejętność wroga [9102003] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 [MiddleFingerBook]이면, 다음 턴에 [PlusCoinValueUp] 1 얻음
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102003].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 693 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Umiejętność wroga [9102004] (ulepszenie 1) — nazwa] 너희 모두 복수 상대다!
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102004].levelList[level=1].name
   limit: do 40 znaków
   EN: Vengeance awaits you all!
   PL:
697. [Umiejętność wroga [9102004] (ulepszenie 1) — opis] 대상의 [MiddleFingerBook] 수치 2 당, 피해량 +10% (최대 50%)\n[BeforeAttack] 자신의 체력이 40% 이하일 때, 가중치 +1\n[WhenUse] 메인 타겟이 [MiddleFingerBook]이면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] [MiddleFingerBook]인 모든 적 3명 당, 코인 위력 +1 (최대 2)\n[WhenUse] 메인 타겟의 [MiddleFingerBook] 2 당, 합 위력 +1 (최대 5)\n[EndSkill] [MiddleFingerBook]을 사망시켰다면, 다음 턴에 [PlusCoinValueUp] 1 얻음 (턴 당 최대 2)\n[EndSkill] 공격 당한 모든 대상의 [MiddleFingerBook] 제거
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102004].levelList[level=1].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [BeforeAttack], [WhenUse], [SuperCoin], [EndSkill], [PlusCoinValueUp]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [EndSkill] = [공격 종료시] / [Attack End]; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: Deal +10% damage for every 2 [MiddleFingerBook] on the target (max 50%)\n[BeforeAttack] At 40% or less HP, gain Atk Weight +1\n[WhenUse] If the main target has [MiddleFingerBook], convert all Coins on this Skill to [SuperCoin]s\n[WhenUse] Coin Power +1 for every 3 enemy with [MiddleFingerBook] (max 2)\n[WhenUse] Clash Power +1 for every 2 [MiddleFingerBook] on the main target (max 5)\n[EndSkill] If this unit killed a target with [MiddleFingerBook], gain 1 [PlusCoinValueUp] next turn (2 times per turn)\n[EndSkill] Remove [MiddleFingerBook] on all targets that were hit
   PL:
698. [Umiejętność wroga [9102004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
699. [Umiejętność wroga [9102004] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102004].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
700. [Umiejętność wroga [9102004] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 2 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102004].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Reduction] next turn
   PL:
701. [Umiejętność wroga [9102005] (ulepszenie 1) — nazwa] 기회 잡기
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].name
   limit: do 40 znaków
   EN: Seize ya Chance
   PL:
702. [Umiejętność wroga [9102005] (ulepszenie 1) — opis] [BeforeHit] 대상의 [MiddleFingerBook] 수치당, 보호막 5 얻음 (턴 당 1회, 최대 50)\n[WhenUse] 대상의 [MiddleFingerBook] 수치가 5 이상이면, 기본 위력 +3, [DefenseDown] 4 부여
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [BeforeHit], [MiddleFingerBook], [WhenUse], [DefenseDown]
   znaczenie tagów: [BeforeHit] = [피격 직전] / [Before Getting Hit]; [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [WhenUse] = [사용시] / [On Use]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [BeforeHit] Gain 5 Shield for every [MiddleFingerBook] on the target (once per turn; max 50)\n[WhenUse] If target has 5+ [MiddleFingerBook], Base Power +3; inflict 4 [DefenseDown]
   PL:
703. [Umiejętność wroga [9102005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 20만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 20
   PL:
704. [Umiejętność wroga [9102005] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 15만큼 고정 체력 피해
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 15 fixed HP damage
   PL:
705. [Umiejętność wroga [9102005] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 20만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Umiejętność wroga [9102005] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 15만큼 고정 체력 피해
   źródło: Skills_Enemy-a1c9116.json :: dataList[id=9102005].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 704 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c9116] Pasywka wroga: Passives_Abnormality-a1c9116
- plik gry: `Passives_Abnormality-a1c9116.json`

707. [[a1c9116] Pasywka wroga [112601] — nazwa] 부여받은 명령
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112601].name
   limit: do 40 znaków
   EN: Bestowed Mission
   PL:
708. [[a1c9116] Pasywka wroga [112601] — opis] 스테이지 시작 시, [WeighedMurderousIntend]를 얻음
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WeighedMurderousIntend]
   znaczenie tagów: [WeighedMurderousIntend] = 짓눌린 살기 / Crushed Bloodthirst
   EN: Encounter Start: gain [WeighedMurderousIntend]
   PL:
709. [[a1c9116] Pasywka wroga [112603] — nazwa] 각력[묘]
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112603].name
   limit: do 40 znaków
   EN: Strider [Mao]
   PL:
710. [[a1c9116] Pasywka wroga [112603] — opis] 자신보다 속도가 낮은 대상 공격 시, 부여하는 [Burst] 혹은 [Burst] 횟수 +2, 피해량 +10%
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112603].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When attacking targets with slower Speed than this unit's, inflict +1 more [Burst] or [Burst] Count and deal +10% damage
   PL:
711. [[a1c9116] Pasywka wroga [112602] — nazwa] 기세[묘]
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112602].name
   limit: do 40 znaków
   EN: Vigor [Mao]
   PL:
712. [[a1c9116] Pasywka wroga [112602] — opis] [BurstAgility]을 가지고 있는 적 적중시, 대상의 [Burst] 횟수 2 증가 (턴 당 최대 6)
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112602].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [BurstAgility], [Burst]
   znaczenie tagów: [BurstAgility] = 주살【신속】 / Deathrite【Haste】; [Burst] = 파열 / Rupture
   EN: On Hit against enemy with [BurstAgility]: inflict +2 [Burst] Count on the target (6 times per turn)
   PL:
713. [[a1c9116] Pasywka wroga [112604] — nazwa] 압도[묘]
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112604].name
   limit: do 40 znaków
   EN: Dominator [Mao]
   PL:
714. [[a1c9116] Pasywka wroga [112604] — opis] 스킬 사용 시 자신의 속도가 대상보다 2 이상 높으면 코인 위력 +1
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112604].desc
   limit: do 120 znaków
   EN: On Skill Use, if this unit's Speed is faster than the target's by 2 or more, Coin Power +1
   PL:
715. [[a1c9116] Pasywka wroga [112701] — nazwa] 작은 형님
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112701].name
   limit: do 40 znaków
   EN: The Big Brother
   PL:
716. [[a1c9116] Pasywka wroga [112701] — opis] 턴 시작 시 자신을 포함한 모든 아군의 정신력 10 회복\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -20%
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112701].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Turn Start: all allies, including this unit, heal 10 SP\nTake -20% damage from [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   PL:
717. [[a1c9116] Pasywka wroga [112702] — nazwa] 원한 문신
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112702].name
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL:
718. [[a1c9116] Pasywka wroga [112702] — opis] 이번 전투에서 중지 소속 아군이 사망할 때마다 [AttackUp] 1을 얻음 (최대 5)
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112702].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Every time a Middle ally is killed in this encounter, gain 1 [AttackUp] (max 5)
   PL:
719. [[a1c9116] Pasywka wroga [112703] — nazwa] 조금 더 퍼석해져버린 머리
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112703].name
   limit: do 50 znaków
   EN: Deeper in the World of Bristly
   PL:
720. [[a1c9116] Pasywka wroga [112703] — opis] 합에서 2회 패배하면, 다음 턴에 [DefenseDown] 6을 얻음
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112703].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseDown]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: If this unit loses 2 Clashes, gain 6 [DefenseDown] next turn
   PL:
721. [[a1c9116] Pasywka wroga [112704] — nazwa] 앙갚음 장부
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112704].name
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL:
722. [[a1c9116] Pasywka wroga [112704] — opis] 자신 또는 아군 중지 조직원이 피격 시, 공격자에게 [MiddleFingerBook]을 1 부여하고, 다음 턴에 [AttackUp] 1 얻음 (턴 당 최대 5)\n- 아군 중지 조직원이 스킬로 사망 시, 공격자에게 [MiddleFingerBook] 2 추가 부여
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112704].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerBook], [AttackUp]
   znaczenie tagów: [MiddleFingerBook] = 중지의 복수 대상 / The Middle's Vendetta Mark; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When this unit or its ally is hit, inflict 1 [MiddleFingerBook] against the attacker, then gain 1 [AttackUp] next turn (max 5 per turn)\n- When an allied unit from The Middle is killed by a Skill, inflict 2 additional [MiddleFingerBook] against the attacker
   PL:
723. [[a1c9116] Pasywka wroga [112705] — nazwa] 전투 부상
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112705].name
   limit: do 40 znaków
   EN: Wounded in Battle
   PL:
724. [[a1c9116] Pasywka wroga [112705] — opis] 최대 체력의 40% 만큼 체력이 감소한 상태로 전투 시작 (부위 포함)
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112705].desc
   limit: do 120 znaków
   EN: Begins Encounter with 40% less HP (including Parts)
   PL:
725. [[a1c9116] Pasywka wroga [112707] — nazwa] 머리 털기
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112707].name
   limit: do 40 znaków
   EN: Brush it Off
   PL:
726. [[a1c9116] Pasywka wroga [112707] — opis] 패닉 상태가 되면, 다음 턴 시작 시 패닉 상태를 해제하고, 정신력이 0으로 초기화 됨.
   źródło: Passives_Abnormality-a1c9116.json :: dataList[id=112707].desc
   limit: do 120 znaków
   EN: When in panic, recover from panic at the start of the next turn and reset SP to 0.
   PL:

## [a1c951] Wróg / część: Enemies-a1c951
- plik gry: `Enemies-a1c951.json`

727. [[a1c951] Wróg / część [90101] — nazwa] 초록 노움
   źródło: Enemies-a1c951.json :: dataList[id=90101].name
   limit: do 40 znaków
   EN: Leafy Gnome
   PL:
728. [[a1c951] Wróg / część [90101] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=90101].desc
   limit: do 120 znaków
   EN: Enemy Unit
   PL:
729. [[a1c951] Wróg / część [90102] — nazwa] 빨간 노움
   źródło: Enemies-a1c951.json :: dataList[id=90102].name
   limit: do 40 znaków
   EN: Cherry Gnome
   PL:
730. [[a1c951] Wróg / część [90102] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=90102].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [[a1c951] Wróg / część [90103] — nazwa] 검은 노움
   źródło: Enemies-a1c951.json :: dataList[id=90103].name
   limit: do 40 znaków
   EN: Shadowy Gnome
   PL:
732. [[a1c951] Wróg / część [90103] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=90103].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [[a1c951] Wróg / część [90104] — nazwa] 실장 노움
   źródło: Enemies-a1c951.json :: dataList[id=90104].name
   limit: do 40 znaków
   EN: Manager Gnome
   PL:
734. [[a1c951] Wróg / część [90104] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=90104].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [[a1c951] Wróg / część [811401] — nazwa] 몸통
   źródło: Enemies-a1c951.json :: dataList[id=811401].name
   limit: do 40 znaków
   EN: Body
   PL:
736. [[a1c951] Wróg / część [811401] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=811401].desc
   limit: do 120 znaków
   EN: Part
   PL:
737. [[a1c951] Wróg / część [811501] — nazwa] 몸통
   źródło: Enemies-a1c951.json :: dataList[id=811501].name
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [[a1c951] Wróg / część [811501] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=811501].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [[a1c951] Wróg / część [811601] — nazwa] 몸통
   źródło: Enemies-a1c951.json :: dataList[id=811601].name
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [[a1c951] Wróg / część [811601] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=811601].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [[a1c951] Wróg / część [813501] — nazwa] 몸통
   źródło: Enemies-a1c951.json :: dataList[id=813501].name
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [[a1c951] Wróg / część [813501] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=813501].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [[a1c951] Wróg / część [8113] — nazwa] 산타타
   źródło: Enemies-a1c951.json :: dataList[id=8113].name
   limit: do 40 znaków
   EN: Santata
   PL:
744. [[a1c951] Wróg / część [8113] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=8113].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [[a1c951] Wróg / część [811301] — nazwa] 몸통
   źródło: Enemies-a1c951.json :: dataList[id=811301].name
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [[a1c951] Wróg / część [811301] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=811301].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [[a1c951] Wróg / część [811302] — nazwa] 선물 주머니
   źródło: Enemies-a1c951.json :: dataList[id=811302].name
   limit: do 40 znaków
   EN: Gift Sack
   PL:
748. [[a1c951] Wróg / część [811302] — opis] 부위
   źródło: Enemies-a1c951.json :: dataList[id=811302].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [[a1c951] Wróg / część [90105] — nazwa] 도도루
   źródło: Enemies-a1c951.json :: dataList[id=90105].name
   limit: do 40 znaków
   EN: Dodoru
   PL:
750. [[a1c951] Wróg / część [90105] — opis] 적 잡몹
   źródło: Enemies-a1c951.json :: dataList[id=90105].desc
   (powtórzenie elementu 728 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c951] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c951
- grupa rozdziału/trybu: `a1c951` · plik: `Skills_Abnormality-a1c951.json`

751. [Umiejętność wroga [811301] (ulepszenie 1) — nazwa] 기쁨이 되시지요
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811301].levelList[level=1].name
   limit: do 40 znaków
   EN: Be The Joy
   PL:
752. [Umiejętność wroga [811301] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811301].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Charge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge
   EN: [WhenUse] Gain +2 [Charge] Count
   PL:
753. [Umiejętność wroga [811301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] on target next turn
   PL:
754. [Umiejętność wroga [811301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Umiejętność wroga [811302] (ulepszenie 1) — nazwa] 위안이 되시지요
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].name
   limit: do 40 znaków
   EN: Be The Comfort
   PL:
756. [Umiejętność wroga [811302] (ulepszenie 1) — opis] [WhenUse] 자신의 [Charge] 횟수 2 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].desc
   (powtórzenie elementu 752 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Umiejętność wroga [811302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +3 [Breath] Count
   PL:
758. [Umiejętność wroga [811302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Breath] 3 얻음
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath], [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise; [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
759. [Umiejętność wroga [811302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 가지고 있는 [Breath]만큼 [Breath]얻음
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain [Breath] equal to [Breath] on self
   PL:
760. [Umiejętność wroga [811302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 757 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Umiejętność wroga [811303] (ulepszenie 1) — nazwa] 선물이랍니다
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811303].levelList[level=1].name
   limit: do 40 znaków
   EN: Here's a Gift
   PL:
762. [Umiejętność wroga [811303] (ulepszenie 1) — opis] 대상에게 [Binding]이 있다면, 자신이 더 빠를 경우 자신과의 속도 차이만큼 합 위력이 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811303].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: If target has [Binding], and if this unit has a faster Speed, gain Clash Power equal to the Speed difference
   PL:
763. [Umiejętność wroga [811303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 정신력 5 감소
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność wroga [811303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 2 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] and +3 [Breath] Count
   PL:
765. [Umiejętność wroga [811303] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811303].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Paralysis]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Paralysis] = 마비 / Paralyze
   EN: [CriticalOnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
766. [Umiejętność wroga [811304] (ulepszenie 1) — nazwa] 포장하겠어요
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Get Packing
   PL:
767. [Umiejętność wroga [811304] (ulepszenie 1) — opis] 자신에게 [AaCeSeBa]가 있다면, 코인 효과에 다음 턴에 [Paralysis] 1 부여 추가\n가장 느린 대상 우선 공격\n[EndBattle] 모든 [Charge] 횟수 소모
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [AaCeSeBa], [Paralysis], [EndBattle], [Charge]
   znaczenie tagów: [AaCeSeBa] = 호!호!호! / HO! HO! HO!; [Paralysis] = 마비 / Paralyze; [EndBattle] = [턴 종료 시] / [Turn End]; [Charge] = 충전 / Charge
   EN: If this unit has [AaCeSeBa], add 'Inflict 1 [Paralysis] next turn' to Coin effects\nTargets the unit with the slowest Speed\n[EndBattle] Spend all [Charge] Count
   PL:
768. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음.
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath].
   PL:
769. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath]만큼 추가 피해
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Deal bonus damage equal to [Breath] on self
   PL:
770. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Breath] 1 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 1 [Breath] and +3 [Breath] Count
   PL:
771. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack]  [Protection], [Enhancement], [Vulnerable], [Paralysis] 중 무작위 1개 효과를 3 부여
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Protection], [Enhancement], [Vulnerable], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Protection] = 보호 / Protection; [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Randomly select 1 of 4 effects ([Protection], [Enhancement], [Vulnerable], [Paralysis]). Inflict or apply 3 of the selected effect.
   PL:
772. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수만큼 대상의 정신력을 감소
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Target loses SP equal to [Charge] Count on this unit
   PL:
773. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [EnemyKill] 모든 적의 정신력 10 감소.
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]
   EN: [EnemyKill] All enemies lose 10 Sp.
   PL:
774. [Umiejętność wroga [811304] (ulepszenie 1) — moneta 3, efekt 4 — opis] [EnemyKillFail] 다음 턴에 [Paralysis] 2 얻음.
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811304].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKillFail], [Paralysis]
   znaczenie tagów: [EnemyKillFail] = [적 처치 실패 시] / [Failed Kill]; [Paralysis] = 마비 / Paralyze
   EN: [EnemyKillFail] Gain 2 [Paralysis] next turn.
   PL:
775. [Umiejętność wroga [811305] (ulepszenie 1) — nazwa] 선물 준비 시간이에요
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811305].levelList[level=1].name
   limit: do 40 znaków
   EN: Time to Get Boxed
   PL:
776. [Umiejętność wroga [811305] (ulepszenie 1) — opis] 보호막 체력이 전부 소모되었다면, 다음 턴에 흐트러짐.\n보호막 체력이 남아있다면, 다음 턴에 [Enhancement] 2 얻음
   źródło: Skills_Abnormality-a1c951.json :: dataList[id=811305].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: If Shield HP is completely depleted, get Staggered next turn.\nIf there is remaining Shield HP, gain 2 [Enhancement] next turn
   PL:

## [a1c951] Umiejętności wrogów / Anomalii — Skills_Enemy-a1c951
- grupa rozdziału/trybu: `a1c951` · plik: `Skills_Enemy-a1c951.json`

777. [Umiejętność wroga [9010101] (ulepszenie 1) — nazwa] 인간있움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010101].levelList[level=1].name
   limit: do 40 znaków
   EN: Human-omes!
   PL:
778. [Umiejętność wroga [9010101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 4 [Breath]
   PL:
779. [Umiejętność wroga [9010101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath]
   PL:
780. [Umiejętność wroga [9010101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Breath]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttackHead] Gain +1 [Breath] Count
   PL:
781. [Umiejętność wroga [9010101] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010101].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Paralysis]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Paralysis] = 마비 / Paralyze
   EN: [CriticalOnSucceedAttack] Inflict 2 [Paralysis]
   PL:
782. [Umiejętność wroga [9010102] (ulepszenie 1) — nazwa] 포획하움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010102].levelList[level=1].name
   limit: do 40 znaków
   EN: Capture them-ome
   PL:
783. [Umiejętność wroga [9010102] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WinDuel] Heal 5 SP
   PL:
784. [Umiejętność wroga [9010102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 4 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 778 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [9010102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [9010102] (ulepszenie 1) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +40%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010102].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: +40% Damage on Critical Hit
   PL:
787. [Umiejętność wroga [9010103] (ulepszenie 1) — nazwa] 움움!!
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010103].levelList[level=1].name
   limit: do 40 znaków
   EN: Ome, Ome!!
   PL:
788. [Umiejętność wroga [9010103] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
789. [Umiejętność wroga [9010103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [9010103] (ulepszenie 1) — moneta 2, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 788 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Umiejętność wroga [9010103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +2 [Breath] Count
   PL:
792. [Umiejętność wroga [9010201] (ulepszenie 1) — nazwa] 싱싱하움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010201].levelList[level=1].name
   limit: do 40 znaków
   EN: Fresh Meat-omes
   PL:
793. [Umiejętność wroga [9010201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] and +2 [Breath] Count
   PL:
794. [Umiejętność wroga [9010201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Umiejętność wroga [9010201] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010201].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Umiejętność wroga [9010201] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010201].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Binding]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Binding] = 속박 / Bind
   EN: [CriticalOnSucceedAttack] Inflict 3 [Binding] next turn
   PL:
797. [Umiejętność wroga [9010202] (ulepszenie 1) — nazwa] 팔팔하움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010202].levelList[level=1].name
   limit: do 40 znaków
   EN: Lookin' Lively-ome!
   PL:
798. [Umiejętność wroga [9010202] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010202].levelList[level=1].desc
   (powtórzenie elementu 783 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [9010202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 793 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Umiejętność wroga [9010202] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +40%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Umiejętność wroga [9010203] (ulepszenie 1) — nazwa] 막았움!
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010203].levelList[level=1].name
   limit: do 40 znaków
   EN: No Use-ome!
   PL:
802. [Umiejętność wroga [9010203] (ulepszenie 1) — opis] [EndBattle] 보호막 체력이 남아있다면, 다음 턴에 [Enhancement] 1 얻음.
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010203].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle], [Enhancement]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndBattle] If this unit has Shield, gain 1 [Enhancement] next turn.
   PL:
803. [Umiejętność wroga [9010301] (ulepszenie 1) — nazwa] 가구로 만들겠움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010301].levelList[level=1].name
   limit: do 40 znaków
   EN: Turn Ya Into Furniture-omes!
   PL:
804. [Umiejętność wroga [9010301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 757 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [9010301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [9010301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 780 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [9010301] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010301].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [9010302] (ulepszenie 1) — nazwa] 얼른 옮기겠움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010302].levelList[level=1].name
   limit: do 40 znaków
   EN: Let's Get It Moving-ome
   PL:
809. [Umiejętność wroga [9010302] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010302].levelList[level=1].desc
   (powtórzenie elementu 783 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Umiejętność wroga [9010302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Umiejętność wroga [9010302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 758 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Umiejętność wroga [9010302] (ulepszenie 1) — moneta 1, efekt 3 — opis] 크리티컬 피해량 +40%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010302].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 786 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Umiejętność wroga [9010303] (ulepszenie 1) — nazwa] 헤움헤움~
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010303].levelList[level=1].name
   limit: do 40 znaków
   EN: Hoom Hoom~
   PL:
814. [Umiejętność wroga [9010303] (ulepszenie 1) — opis] [OnSucceedEvade] 다음 턴에 [Breath] 5얻음. 자신의 [Breath] 횟수 2 증가.\n[OnDefeatEvade] 10만큼 흐트러짐 손상
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010303].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedEvade], [Breath], [OnDefeatEvade]
   znaczenie tagów: [OnSucceedEvade] = [회피 성공시] / [On Evade]; [Breath] = 호흡 / Poise; [OnDefeatEvade] = [회피 실패시] / [Failed Evade]
   EN: [OnSucceedEvade] Gain 5 [Breath] and +2 [Breath] Count.\n[OnDefeatEvade] Raise Stagger Threshold by 10
   PL:
815. [Umiejętność wroga [9010401] (ulepszenie 1) — nazwa] 놓치지 않겠움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010401].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll Get You-ome
   PL:
816. [Umiejętność wroga [9010401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Umiejętność wroga [9010401] (ulepszenie 1) — moneta 1, efekt 2 — opis] [CriticalOnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010401].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Binding]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Binding] = 속박 / Bind
   EN: [CriticalOnSucceedAttack] Inflict 2 [Binding] next turn
   PL:
818. [Umiejętność wroga [9010402] (ulepszenie 1) — nazwa] 노다지움
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].name
   limit: do 40 znaków
   EN: We Struck Gold-ome!
   PL:
819. [Umiejętność wroga [9010402] (ulepszenie 1) — opis] [WinDuel] 정신력 5 회복
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].desc
   (powtórzenie elementu 783 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Umiejętność wroga [9010402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Breath] 2 얻음. 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 2 [Breath] and +3 [Breath] Count
   PL:
821. [Umiejętność wroga [9010402] (ulepszenie 1) — moneta 1, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [9010402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 3 얻음. 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain 3 [Breath] and +1 [Breath] Count
   PL:
823. [Umiejętność wroga [9010402] (ulepszenie 1) — moneta 2, efekt 2 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [9010403] (ulepszenie 1) — nazwa] 산지 직송이움!
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].name
   limit: do 40 znaków
   EN: Local Raw Material-omes!
   PL:
825. [Umiejętność wroga [9010403] (ulepszenie 1) — opis] [WinDuel] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Breath]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Breath] = 호흡 / Poise
   EN: [WinDuel] Gain 3 [Breath]
   PL:
826. [Umiejętność wroga [9010403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [CriticalOnSucceedAttack] 마지막 코인 피해량 +20%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Damage +20% for the last Coin
   PL:
827. [Umiejętność wroga [9010403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Breath] 3 얻음
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 779 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Umiejętność wroga [9010403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [CriticalOnSucceedAttack] 마지막 코인 피해량 +20%
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Umiejętność wroga [9010403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Umiejętność wroga [9010403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] 자신의 [Breath] 횟수를 소모하지 않음. [Breath]만큼 추가 타격 피해 입힘
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Does not consume [Breath] Count. Deal bonus Blunt damage equal to [Breath]
   PL:
831. [Umiejętność wroga [9010404] (ulepszenie 1) — nazwa] 막았움!
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010404].levelList[level=1].name
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Umiejętność wroga [9010404] (ulepszenie 1) — opis] [EndBattle] 보호막 체력이 남아있다면, 다음 턴에 [Enhancement] 2 얻음.
   źródło: Skills_Enemy-a1c951.json :: dataList[id=9010404].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndBattle], [Enhancement]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [EndBattle] If this unit has Shield, gain 2 [Enhancement] next turn.
   PL:

## [a1c951] Pasywka wroga: Passives_Abnormality-a1c951
- plik gry: `Passives_Abnormality-a1c951.json`

833. [[a1c951] Pasywka wroga [811301] — nazwa] 산타타의 웃음
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811301].name
   limit: do 40 znaków
   EN: Santata's Guffaw
   PL:
834. [[a1c951] Pasywka wroga [811301] — opis] [Charge] 횟수가 10이상이면, 다음 턴에 [AaCeSeBa]를 얻음.\n본체 체력이 30%이하가 되면, 매 턴마다 [AaCeSeBa]를 얻음.
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811301].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AaCeSeBa]
   znaczenie tagów: [Charge] = 충전 / Charge; [AaCeSeBa] = 호!호!호! / HO! HO! HO!
   EN: At 10+ [Charge] Count, gain [AaCeSeBa] next turn.\nAt 30%- Core HP, gain [AaCeSeBa] every turn.
   PL:
835. [[a1c951] Pasywka wroga [811302] — nazwa] 전구 방전
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811302].name
   limit: do 40 znaków
   EN: Lights Out
   PL:
836. [[a1c951] Pasywka wroga [811302] — opis] 흐트러짐 상태가 되면, 모든 [Charge] 횟수 잃음.
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Lose all [Charge] Count when this unit is Staggered.
   PL:
837. [[a1c951] Pasywka wroga [811303] — nazwa] 흩어지는 호흡
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811303].name
   limit: do 40 znaków
   EN: Scattering Breath
   PL:
838. [[a1c951] Pasywka wroga [811303] — opis] 공격 스킬에 피격시 [Breath] 횟수 1 감소
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811303].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Lose 1 [Breath] when hit by an Attack Skill
   PL:
839. [[a1c951] Pasywka wroga [811304] — nazwa] 선물을 담을 수 없어요!!
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811304].name
   limit: do 40 znaków
   EN: I CAN'T BAG THE GIFTS!!
   PL:
840. [[a1c951] Pasywka wroga [811304] — opis] 선물 주머니 부위가 파괴되었다면, 포장하겠어요 기본 위력 -2
   źródło: Passives_Abnormality-a1c951.json :: dataList[id=811304].desc
   limit: do 120 znaków
   EN: Base Power -2 to 'Let's Get Packing' if the Gift Sack Part is broken.
   PL:

## [a1c951] Pasywka wroga: Passives_Enemy-a1c951
- plik gry: `Passives_Enemy-a1c951.json`

841. [[a1c951] Pasywka wroga [9010101] — nazwa] 싱싱한 인간이움
   źródło: Passives_Enemy-a1c951.json :: dataList[id=9010101].name
   limit: do 40 znaków
   EN: Fresh Human-omes!
   PL:
842. [[a1c951] Pasywka wroga [9010101] — opis] 살아있는 적 수당 앞면 확률 2% 증가. (최대 95%)
   źródło: Passives_Enemy-a1c951.json :: dataList[id=9010101].desc
   limit: do 120 znaków
   EN: Every surviving enemy gives this unit +2% chance to flip Heads. (Max 95%)
   PL:
843. [[a1c951] Pasywka wroga [9010102] — nazwa] 내 몫이움
   źródło: Passives_Enemy-a1c951.json :: dataList[id=9010102].name
   limit: do 40 znaków
   EN: Mine-omes
   PL:
844. [[a1c951] Pasywka wroga [9010102] — opis] 턴 종료 시 살아있는 적보다 살아있는 아군이 적을 때, 다음 턴에 [Agility] 1, [Enhancement] 1을 얻음.
   źródło: Passives_Enemy-a1c951.json :: dataList[id=9010102].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Agility], [Enhancement]
   znaczenie tagów: [Agility] = 신속 / Haste; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn End: when there are more surviving enemies than surviving allies, gain 1 [Agility] and 1 [Enhancement] next turn.
   PL:

## [a1c971] Wróg / część: Enemies-a1c971
- plik gry: `Enemies-a1c971.json`

845. [[a1c971] Wróg / część [1079] — nazwa] 산초
   źródło: Enemies-a1c971.json :: dataList[id=1079].name
   limit: do 40 znaków
   EN: Sancho
   PL:
846. [[a1c971] Wróg / część [1079] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1079].desc
   limit: do 120 znaków
   EN: Core
   PL:
847. [[a1c971] Wróg / część [1080] — nazwa] 나태 죄종??
   źródło: Enemies-a1c971.json :: dataList[id=1080].name
   limit: do 40 znaków
   EN: Peccatulum Pigritiae??
   PL:
848. [[a1c971] Wróg / część [1080] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1080].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [[a1c971] Wróg / część [1081] — nazwa] 우울 죄종??
   źródło: Enemies-a1c971.json :: dataList[id=1081].name
   limit: do 40 znaków
   EN: Peccatulum Morositatis??
   PL:
850. [[a1c971] Wróg / część [1081] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1081].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [[a1c971] Wróg / część [1082] — nazwa] 뒤틀린 호엔하임
   źródło: Enemies-a1c971.json :: dataList[id=1082].name
   limit: do 40 znaków
   EN: Distorted Hohenheim
   PL:
852. [[a1c971] Wróg / część [1082] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1082].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [[a1c971] Wróg / część [108201] — nazwa] 몸통
   źródło: Enemies-a1c971.json :: dataList[id=108201].name
   (powtórzenie elementu 735 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [[a1c971] Wróg / część [108201] — opis] 부위
   źródło: Enemies-a1c971.json :: dataList[id=108201].desc
   (powtórzenie elementu 736 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [[a1c971] Wróg / część [90181] — nazwa] 검열된 로보토미 3등급 직원
   źródło: Enemies-a1c971.json :: dataList[id=90181].name
   limit: do 50 znaków
   EN: Censored Lobotomy Corp. L3 Agent
   PL:
856. [[a1c971] Wróg / część [90181] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=90181].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [[a1c971] Wróg / część [90182] — nazwa] 검열된 로보토미 2등급 직원
   źródło: Enemies-a1c971.json :: dataList[id=90182].name
   limit: do 50 znaków
   EN: Censored Lobotomy Corp. L3 Agent
   PL:
858. [[a1c971] Wróg / część [90182] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=90182].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [[a1c971] Wróg / część [1098] — nazwa] 질투 죄종?
   źródło: Enemies-a1c971.json :: dataList[id=1098].name
   limit: do 40 znaków
   EN: Peccatulum Invidiae?
   PL:
860. [[a1c971] Wróg / część [1098] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1098].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [[a1c971] Wróg / część [1100] — nazwa] 질투 죄종
   źródło: Enemies-a1c971.json :: dataList[id=1100].name
   limit: do 40 znaków
   EN: Peccatulum Invidiae
   PL:
862. [[a1c971] Wróg / część [1100] — opis] 본체
   źródło: Enemies-a1c971.json :: dataList[id=1100].desc
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c971] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c971
- grupa rozdziału/trybu: `a1c971` · plik: `Skills_Abnormality-a1c971.json`

863. [Umiejętność wroga [108001] (ulepszenie 1) — nazwa] 바위 세례
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108001].levelList[level=1].name
   limit: do 40 znaków
   EN: Stoneshower
   PL:
864. [Umiejętność wroga [108001] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration]이 5 이상이면, 기본 위력 +1
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: [WhenUse] If target has 5+ [Vibration], Base Power +1
   PL:
865. [Umiejętność wroga [108001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 8 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 8 [Vibration]
   PL:
866. [Umiejętność wroga [108001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Umiejętność wroga [108002] (ulepszenie 1) — nazwa] 돌 모으기
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108002].levelList[level=1].name
   limit: do 40 znaków
   EN: Gather Stones
   PL:
868. [Umiejętność wroga [108002] (ulepszenie 1) — opis] [WinDuel] 대상에게 [Vibration]이 있으면, 기본 위력 +2
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WinDuel], [Vibration]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor
   EN: [WinDuel] If target has [Vibration], Base Power +2
   PL:
869. [Umiejętność wroga [108002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 8 부여
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 865 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Umiejętność wroga [108002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
871. [Umiejętność wroga [108003] (ulepszenie 1) — nazwa] 솟아나는 나태
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108003].levelList[level=1].name
   limit: do 40 znaków
   EN: Rising Sloth
   PL:
872. [Umiejętność wroga [108003] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration] 3 당, 코인 위력 +1 (최대 3)\n[WinDuel] 대상의 [Vibration] 5 당, 이 스킬의 공격 가중치 +1 (최대 2)
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108003].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [WinDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [WhenUse] Coin Power +1 for every 3 [Vibration] on target (max 3)\n[WinDuel] This Skill gains Atk Weight +1 for every 5 [Vibration] on the target (max 2)
   PL:
873. [Umiejętność wroga [108003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationEcho]으로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationEcho], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationEcho]
   PL:
874. [Umiejętność wroga [108003] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 2 당, [VibrationExplosion] 1회 (최대 2회). [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108003].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] once for every [Vibration] Count on the target (max 2); then, reduce target's [Vibration] Count by 2
   PL:
875. [Umiejętność wroga [108003] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 4 증가
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108003].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +4 [Vibration] Count
   PL:
876. [Umiejętność wroga [108004] (ulepszenie 1) — nazwa] 가드
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108004].levelList[level=1].name
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Umiejętność wroga [108004] (ulepszenie 1) — opis] 보호막 체력이 있는 동안 피격 시, 공격자에게 [Vibration] 2 부여\n[WhenUse] 보호 3 얻음.
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108004].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [WhenUse]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [WhenUse] = [사용시] / [On Use]
   EN: Inflict 2 [Vibration] against the Attacker when hit as long as there is remaining Shield HP\n[WhenUse] Gain 3 Protection
   PL:
878. [Umiejętność wroga [108101] (ulepszenie 1) — nazwa] 잠식 충돌
   źródło: Skills_Abnormality-a1c971.json :: dataList[id=108101].levelList[level=1].name
   limit: do 40 znaków
   EN: Decay Collission
   PL:
