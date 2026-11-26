# Paczka AI P29 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 15/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P29_2a_slowa_kluczowe_i_statusy_cz15.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P29_2a_slowa_kluczowe_i_statusy_cz15.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs_Mirror5
- plik gry: `Bufs_Mirror5.json`

1. [Status [MD573] — opis] 공격 레벨 +5, 방어 레벨 +2, 최대 체력 +15%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD573].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +2, Max HP +15%, Damage Dealt +7.5%
   PL: Poziom Ataku +5, Poziom Obrony +2, Maks. HP +15%, Zadawane Obrażenia +7.5%
2. [Status [MD574] — nazwa] 성장 VII
   źródło: Bufs_Mirror5.json :: dataList[id=MD574].name
   kontekst: identyfikator statusu w tekstach: `[MD574]`
   limit: do 40 znaków
   EN: Growth VII
   PL: Rozwój VII
3. [Status [MD574] — opis] 공격 레벨 +2, 최대 체력 +35%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD574].desc
   limit: do 120 znaków
   EN: Offense Level +2, Max HP +35%, Damage Dealt +7.5%
   PL: Poziom Ataku +2, Maks. HP +35%, Zadawane Obrażenia +7.5%
4. [Status [MD575] — nazwa] 합 위력 증강 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD575].name
   kontekst: identyfikator statusu w tekstach: `[MD575]`
   limit: do 40 znaków
   EN: Clash Power Up IV
   PL: Wzmocnienie Mocy Starcia IV
5. [Status [MD575] — opis] 합 위력 +1, 공격 레벨 +2, 최대 체력 +20%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD575].desc
   limit: do 120 znaków
   EN: Clash Power +1, Offense Level +2, Max HP +20%, Damage Dealt +7.5%
   PL: Moc Starcia +1, Poziom Ataku +2, Maks. HP +20%, Zadawane Obrażenia +7.5%
6. [Status [MD576] — nazwa] 최종 위력 증강 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD576].name
   kontekst: identyfikator statusu w tekstach: `[MD576]`
   limit: do 40 znaków
   EN: Final Power Up IV
   PL: Wzmocnienie Mocy Końcowej IV
7. [Status [MD576] — opis] 최종 위력 +1, 공격 레벨 +2, 최대 체력 +17.5%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD576].desc
   limit: do 120 znaków
   EN: Final Power +1, Offense Level +2, Max HP +17.5%, Damage Dealt +7.5%
   PL: Moc Końcowa +1, Poziom Ataku +2, Maks. HP +17.5%, Zadawane Obrażenia +7.5%
8. [Status [MD577] — nazwa] 기본 위력 증강 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD577].name
   kontekst: identyfikator statusu w tekstach: `[MD577]`
   limit: do 40 znaków
   EN: Base Power Up IV
   PL: Wzmocnienie Mocy Bazowej IV
9. [Status [MD577] — opis] 기본 위력 +1, 공격 레벨 +2, 최대 체력 +15%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD577].desc
   limit: do 120 znaków
   EN: Base Power +1, Offense Level +2, Max HP +15%, Damage Dealt +7.5%
   PL: Moc Bazowa +1, Poziom Ataku +2, Maks. HP +15%, Zadawane Obrażenia +7.5%
10. [Status [MD578] — nazwa] 파괴력 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD578].name
   kontekst: identyfikator statusu w tekstach: `[MD578]`
   limit: do 40 znaków
   EN: Brutality IV
   PL: Siła Niszczenia IV
11. [Status [MD578] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD578].desc
   limit: do 120 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Damage Dealt +7.5%
   PL: Moc Końcowa +2, Poziom Ataku +1, Maks. HP +20%, Zadawane Obrażenia +7.5%
12. [Status [MD581] — nazwa] 예리 VIII
   źródło: Bufs_Mirror5.json :: dataList[id=MD581].name
   kontekst: identyfikator statusu w tekstach: `[MD581]`
   limit: do 40 znaków
   EN: Keen VIII
   PL: Ostrość VIII
13. [Status [MD581] — opis] 공격 레벨 +6, 최대 체력 +30%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD581].desc
   limit: do 120 znaków
   EN: Offense Level +6, Max HP +30%, Damage Dealt +7.5%
   PL: Poziom Ataku +6, Maks. HP +30%, Zadawane Obrażenia +7.5%
14. [Status [MD582] — nazwa] 강인함 VIII
   źródło: Bufs_Mirror5.json :: dataList[id=MD582].name
   kontekst: identyfikator statusu w tekstach: `[MD582]`
   limit: do 40 znaków
   EN: Resilient VIII
   PL: Twardość VIII
15. [Status [MD582] — opis] 공격 레벨 +3, 방어 레벨 +6, 최대 체력 +30%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD582].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +6, Max HP +30%, Damage Dealt +7.5%
   PL: Poziom Ataku +3, Poziom Obrony +6, Maks. HP +30%, Zadawane Obrażenia +7.5%
16. [Status [MD583] — nazwa] 육체 강화 VIII
   źródło: Bufs_Mirror5.json :: dataList[id=MD583].name
   kontekst: identyfikator statusu w tekstach: `[MD583]`
   limit: do 40 znaków
   EN: Body Up VIII
   PL: Umocnienie Ciała VIII
17. [Status [MD583] — opis] 공격 레벨 +5, 방어 레벨 +4, 최대 체력 +22.5%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD583].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +4, Max HP +22.5%, Damage Dealt +7.5%
   PL: Poziom Ataku +5, Poziom Obrony +4, Maks. HP +22.5%, Zadawane Obrażenia +7.5%
18. [Status [MD584] — nazwa] 성장 VIII
   źródło: Bufs_Mirror5.json :: dataList[id=MD584].name
   kontekst: identyfikator statusu w tekstach: `[MD584]`
   limit: do 40 znaków
   EN: Growth VIII
   PL: Rozwój VIII
19. [Status [MD584] — opis] 공격 레벨 +3, 최대 체력 +45%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD584].desc
   limit: do 120 znaków
   EN: Offense Level +3, Max HP +45%, Damage Dealt +7.5%
   PL: Poziom Ataku +3, Maks. HP +45%, Zadawane Obrażenia +7.5%
20. [Status [MD585] — nazwa] 합 위력 증강 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD585].name
   kontekst: identyfikator statusu w tekstach: `[MD585]`
   limit: do 40 znaków
   EN: Clash Power Up V
   PL: Wzmocnienie Mocy Starcia V
21. [Status [MD585] — opis] 합 위력 +2, 공격 레벨 +1, 최대 체력 +25%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD585].desc
   limit: do 120 znaków
   EN: Clash Power +2, Offense Level +1, Max HP +25%, Damage Dealt +7.5%
   PL: Moc Starcia +2, Poziom Ataku +1, Maks. HP +25%, Zadawane Obrażenia +7.5%
22. [Status [MD586] — nazwa] 최종 위력 증강 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD586].name
   kontekst: identyfikator statusu w tekstach: `[MD586]`
   limit: do 40 znaków
   EN: Final Power Up V
   PL: Wzmocnienie Mocy Końcowej V
23. [Status [MD586] — opis] 최종 위력 +2, 공격 레벨 +1, 최대 체력 +20%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD586].desc
   limit: do 120 znaków
   EN: Final Power +2, Offense Level +1, Max HP +20%, Damage Dealt +7.5%
   PL: Moc Końcowa +2, Poziom Ataku +1, Maks. HP +20%, Zadawane Obrażenia +7.5%
24. [Status [MD587] — nazwa] 기본 위력 증강 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD587].name
   kontekst: identyfikator statusu w tekstach: `[MD587]`
   limit: do 40 znaków
   EN: Base Power Up V
   PL: Wzmocnienie Mocy Bazowej V
25. [Status [MD587] — opis] 기본 위력 +2, 공격 레벨 +1, 최대 체력 +15%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD587].desc
   limit: do 120 znaków
   EN: Base Power +2, Offense Level +1, Max HP +15%, Damage Dealt +7.5%
   PL: Moc Bazowa +2, Poziom Ataku +1, Maks. HP +15%, Zadawane Obrażenia +7.5%
26. [Status [MD588] — nazwa] 파괴력 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD588].name
   kontekst: identyfikator statusu w tekstach: `[MD588]`
   limit: do 40 znaków
   EN: Brutality V
   PL: Siła Niszczenia V
27. [Status [MD588] — opis] 더하기 코인 위력 +2, 빼기 코인 위력 -2, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD588].desc
   limit: do 120 znaków
   EN: Plus Coin Power +2, Minus Coin Power -2, Damage Dealt +7.5%
   PL: Moc Monet Plus +2, Moc Monet Minus -2, Zadawane Obrażenia +7.5%
28. [Status [MD591] — nazwa] 예리 IX
   źródło: Bufs_Mirror5.json :: dataList[id=MD591].name
   kontekst: identyfikator statusu w tekstach: `[MD591]`
   limit: do 40 znaków
   EN: Keen IX
   PL: Ostrość IX
29. [Status [MD591] — opis] 공격 레벨 +8, 최대 체력 +40%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD591].desc
   limit: do 120 znaków
   EN: Offense Level +8, Max HP +40%, Damage Dealt +10%
   PL: Poziom Ataku +8, Maks. HP +40%, Zadawane Obrażenia +10%
30. [Status [MD592] — nazwa] 강인함 IX
   źródło: Bufs_Mirror5.json :: dataList[id=MD592].name
   kontekst: identyfikator statusu w tekstach: `[MD592]`
   limit: do 40 znaków
   EN: Resilient IX
   PL: Twardość IX
31. [Status [MD592] — opis] 공격 레벨 +3, 방어 레벨 +9, 최대 체력 +40%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD592].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +9, Max HP +40%, Damage Dealt +10%
   PL: Poziom Ataku +3, Poziom Obrony +9, Maks. HP +40%, Zadawane Obrażenia +10%
32. [Status [MD593] — nazwa] 육체 강화 IX
   źródło: Bufs_Mirror5.json :: dataList[id=MD593].name
   kontekst: identyfikator statusu w tekstach: `[MD593]`
   limit: do 40 znaków
   EN: Body Up IX
   PL: Umocnienie Ciała IX
33. [Status [MD593] — opis] 공격 레벨 +6, 방어 레벨 +5, 최대 체력 +32.5%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD593].desc
   limit: do 120 znaków
   EN: Offense Level +6, Defense Level +5, Max HP +32.5%, Damage Dealt +10%
   PL: Poziom Ataku +6, Poziom Obrony +5, Maks. HP +32.5%, Zadawane Obrażenia +10%
34. [Status [MD594] — nazwa] 성장 IX
   źródło: Bufs_Mirror5.json :: dataList[id=MD594].name
   kontekst: identyfikator statusu w tekstach: `[MD594]`
   limit: do 40 znaków
   EN: Growth IX
   PL: Rozwój IX
35. [Status [MD594] — opis] 공격 레벨 +3, 최대 체력 +72.5%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD594].desc
   limit: do 120 znaków
   EN: Offense Level +3, Max HP +72.5%, Damage Dealt +10%
   PL: Poziom Ataku +3, Maks. HP +72.5%, Zadawane Obrażenia +10%
36. [Status [MD595] — nazwa] 합 위력 증강 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD595].name
   kontekst: identyfikator statusu w tekstach: `[MD595]`
   limit: do 40 znaków
   EN: Clash Power Up VI
   PL: Wzmocnienie Mocy Starcia VI
37. [Status [MD595] — opis] 합 위력 +2, 공격 레벨 +2, 최대 체력 +40%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD595].desc
   limit: do 120 znaków
   EN: Clash Power +2, Offense Level +2, Max HP +40%, Damage Dealt +10%
   PL: Moc Starcia +2, Poziom Ataku +2, Maks. HP +40%, Zadawane Obrażenia +10%
38. [Status [MD596] — nazwa] 최종 위력 증강 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD596].name
   kontekst: identyfikator statusu w tekstach: `[MD596]`
   limit: do 40 znaków
   EN: Final Power Up VI
   PL: Wzmocnienie Mocy Końcowej VI
39. [Status [MD596] — opis] 최종 위력 +2, 공격 레벨 +2, 최대 체력 +35%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD596].desc
   limit: do 120 znaków
   EN: Final Power +2, Offense Level +2, Max HP +35%, Damage Dealt +10%
   PL: Moc Końcowa +2, Poziom Ataku +2, Maks. HP +35%, Zadawane Obrażenia +10%
40. [Status [MD597] — nazwa] 기본 위력 증강 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD597].name
   kontekst: identyfikator statusu w tekstach: `[MD597]`
   limit: do 40 znaków
   EN: Base Power Up VI
   PL: Wzmocnienie Mocy Bazowej VI
41. [Status [MD597] — opis] 기본 위력 +2, 공격 레벨 +2, 최대 체력 +30%, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD597].desc
   limit: do 120 znaków
   EN: Base Power +2, Offense Level +2, Max HP +30%, Damage Dealt +10%
   PL: Moc Bazowa +2, Poziom Ataku +2, Maks. HP +30%, Zadawane Obrażenia +10%
42. [Status [MD598] — nazwa] 파괴력 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD598].name
   kontekst: identyfikator statusu w tekstach: `[MD598]`
   limit: do 40 znaków
   EN: Brutality VI
   PL: Siła Niszczenia VI
43. [Status [MD598] — opis] 더하기 코인 위력 +2, 빼기 코인 위력 -2, 가하는 피해량 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD598].desc
   limit: do 120 znaków
   EN: Plus Coin Power +2, Minus Coin Power -2, Damage Dealt +10%
   PL: Moc Monet Plus +2, Moc Monet Minus -2, Zadawane Obrażenia +10%

## Statusy i efekty bojowe — Bufs_Mirror6
- plik gry: `Bufs_Mirror6.json`

44. [Status [MD6LimitBaseN] — nazwa] 추가되는 제약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6LimitBaseN].name
   kontekst: identyfikator statusu w tekstach: `[MD6LimitBaseN]`
   limit: do 40 znaków
   EN: Mounting Adversities
   PL: Narastające Ograniczenia
45. [Status [MD6101] — nazwa] 예리 XII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6101].name
   kontekst: identyfikator statusu w tekstach: `[MD6101]`
   limit: do 40 znaków
   EN: Keen XII
   PL: Ostrość XII
46. [Status [MD6101] — opis] 합 위력 +1, 공격 레벨 +8, 방어레벨 +3, 최대 체력 +40%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6101].desc
   limit: do 130 znaków
   EN: Clash Power +1, Offense Level +8, Defense Level +3, Max HP +40%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Poziom Ataku +8, Poziom Obrony +3, Maks. HP +40%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
47. [Status [MD6102] — nazwa] 강인함 XII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6102].name
   kontekst: identyfikator statusu w tekstach: `[MD6102]`
   limit: do 40 znaków
   EN: Resilient XII
   PL: Twardość XII
48. [Status [MD6102] — opis] 합 위력 +1, 공격 레벨 +4, 방어 레벨 +11, 최대 체력 +40%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6102].desc
   limit: do 140 znaków
   EN: Clash Power +1, Offense Level +4, Defense Level +11, Max HP +40%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Poziom Ataku +4, Poziom Obrony +11, Maks. HP +40%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
49. [Status [MD6103] — nazwa] 육체 강화 XII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6103].name
   kontekst: identyfikator statusu w tekstach: `[MD6103]`
   limit: do 40 znaków
   EN: Body Up XII
   PL: Umocnienie Ciała XII
50. [Status [MD6103] — opis] 합 위력 +1, 공격 레벨 +6, 방어 레벨 +7, 최대 체력 +35%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6103].desc
   limit: do 130 znaków
   EN: Clash Power +1, Offense Level +6, Defense Level +7, Max HP +35%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Poziom Ataku +6, Poziom Obrony +7, Maks. HP +35%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
51. [Status [MD6104] — nazwa] 성장 XII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6104].name
   kontekst: identyfikator statusu w tekstach: `[MD6104]`
   limit: do 40 znaków
   EN: Growth XII
   PL: Rozwój XII
52. [Status [MD6104] — opis] 합 위력 +1, 공격 레벨 +3, 방어레벨 +3, 최대 체력 +72.5%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6104].desc
   limit: do 140 znaków
   EN: Clash Power +1, Offense Level +3, Defense Level +3, Max HP +72.5%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +72.5%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
53. [Status [MD6105] — nazwa] 합 위력 증강 VII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6105].name
   kontekst: identyfikator statusu w tekstach: `[MD6105]`
   limit: do 40 znaków
   EN: Clash Power Up VII
   PL: Wzmocnienie Mocy Starcia VII
54. [Status [MD6105] — opis] 합 위력 +3, 공격 레벨 +2, 방어레벨 +2,최대 체력 +42.5%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6105].desc
   limit: do 140 znaków
   EN: Clash Power +3, Offense Level +2, Defense Level +2, Max HP +42.5%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +3, Poziom Ataku +2, Poziom Obrony +2, Maks. HP +42.5%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
55. [Status [MD6106] — nazwa] 최종 위력 증강 VII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6106].name
   kontekst: identyfikator statusu w tekstach: `[MD6106]`
   limit: do 40 znaków
   EN: Final Power Up VII
   PL: Wzmocnienie Mocy Końcowej VII
56. [Status [MD6106] — opis] 합 위력 +1, 최종 위력 +2, 공격 레벨 +2,  방어레벨 +2, 최대 체력 +37.5%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6106].desc
   limit: do 160 znaków
   EN: Clash Power +1, Final Power +2, Offense Level +2, Defense Level +2, Max HP +37.5%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Moc Końcowa +2, Poziom Ataku +2, Poziom Obrony +2, Maks. HP +37.5%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
57. [Status [MD6107] — nazwa] 기본 위력 증강 VII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6107].name
   kontekst: identyfikator statusu w tekstach: `[MD6107]`
   limit: do 40 znaków
   EN: Base Power Up VII
   PL: Wzmocnienie Mocy Bazowej VII
58. [Status [MD6107] — opis] 합 위력 +1, 기본 위력 +2, 공격 레벨 +2, 방어레벨 +2, 최대 체력 +32.5%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6107].desc
   limit: do 150 znaków
   EN: Clash Power +1, Base Power +2 Offense Level +2, Defense Level +2, Max HP +32.5%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Starcia +1, Moc Bazowa +2, Poziom Ataku +2, Poziom Obrony +2, Maks. HP +32.5%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
59. [Status [MD6111] — nazwa] 예리 XIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6111].name
   kontekst: identyfikator statusu w tekstach: `[MD6111]`
   limit: do 40 znaków
   EN: Keen XIII
   PL: Ostrość XIII
60. [Status [MD6111] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 공격 레벨 +8, 방어레벨 +5, 최대 체력 +40%, 피해량 증가 12.5%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6111].desc
   limit: do 170 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Offense Level +8, Defense Level +5, Max HP +40%, Damage Dealt +12.5%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Poziom Ataku +8, Poziom Obrony +5, Maks. HP +40%, Zadawane Obrażenia +12.5%, w walkach z bossami Maks. HP +30%
61. [Status [MD6112] — nazwa] 강인함 XIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6112].name
   kontekst: identyfikator statusu w tekstach: `[MD6112]`
   limit: do 40 znaków
   EN: Resilient XIII
   PL: Twardość XIII
62. [Status [MD6112] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 공격 레벨 +5, 방어 레벨 +12, 최대 체력 +42.5%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6112].desc
   limit: do 170 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Offense Level +5, Defense Level +12, Max HP +42.5%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Poziom Ataku +5, Poziom Obrony +12, Maks. HP +42.5%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
63. [Status [MD6113] — nazwa] 육체 강화 XIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6113].name
   kontekst: identyfikator statusu w tekstach: `[MD6113]`
   limit: do 40 znaków
   EN: Body Up XIII
   PL: Umocnienie Ciała XIII
64. [Status [MD6113] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 공격 레벨 +7, 방어 레벨 +7, 최대 체력 +40%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6113].desc
   limit: do 170 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Offense Level +7, Defense Level +7, Max HP +40%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Poziom Ataku +7, Poziom Obrony +7, Maks. HP +40%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
65. [Status [MD6114] — nazwa] 성장 XIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6114].name
   kontekst: identyfikator statusu w tekstach: `[MD6114]`
   limit: do 40 znaków
   EN: Growth XIII
   PL: Rozwój XIII
66. [Status [MD6114] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 공격 레벨 +3, 방어레벨 +3, 최대 체력 +80%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6114].desc
   limit: do 170 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Offense Level +3, Defense Level +3, Max HP +80%, Damage Dealt +10%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +80%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
67. [Status [MD6115] — nazwa] 합 위력 증강 VIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6115].name
   kontekst: identyfikator statusu w tekstach: `[MD6115]`
   limit: do 40 znaków
   EN: Clash Power Up VIII
   PL: Wzmocnienie Mocy Starcia VIII
68. [Status [MD6115] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 합 위력 +2, 공격 레벨 +3, 방어레벨 +3,최대 체력 +45%, 피해량 증가 12.5%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6115].desc
   limit: do 190 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Clash Power +2, Offense Level +3, Defense Level +3, Max HP +45%, Damage Dealt +12.5%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Moc Starcia +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +45%, Zadawane Obrażenia +12.5%, w walkach z bossami Maks. HP +30%
69. [Status [MD6116] — nazwa] 최종 위력 증강 VIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6116].name
   kontekst: identyfikator statusu w tekstach: `[MD6116]`
   limit: do 40 znaków
   EN: Final Power Up VIII
   PL: Wzmocnienie Mocy Końcowej VIII
70. [Status [MD6116] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 최종 위력 +2, 공격 레벨 +2,  방어레벨 +2, 최대 체력 +40%, 피해량 증가 12.5%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6116].desc
   limit: do 190 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Final Power +2, Offense Level +2, Defense Level +2 Max HP +40%, Damage Dealt +12.5%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Moc Końcowa +2, Poziom Ataku +2, Poziom Obrony +2, Maks. HP +40%, Zadawane Obrażenia +12.5%, w walkach z bossami Maks. HP +30%
71. [Status [MD6117] — nazwa] 기본 위력 증강 VIII
   źródło: Bufs_Mirror6.json :: dataList[id=MD6117].name
   kontekst: identyfikator statusu w tekstach: `[MD6117]`
   limit: do 40 znaków
   EN: Base Power Up VIII
   PL: Wzmocnienie Mocy Bazowej VIII
72. [Status [MD6117] — opis] 더하기 코인 위력 +1 , 빼기 코인 위력 -1, 기본 위력 +2, 공격 레벨 +2, 방어레벨 +2, 최대 체력 +35%, 피해량 증가 12.5%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6117].desc
   limit: do 190 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Base Power +2, Offense Level +2, Defense Level +2, Max HP +35%, Damage Dealt +12.5%, Boss Max HP +30%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Moc Bazowa +2, Poziom Ataku +2, Poziom Obrony +2, Maks. HP +35%, Zadawane Obrażenia +12.5%, w walkach z bossami Maks. HP +30%
73. [Status [MD6121] — nazwa] 예리 XIV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6121].name
   kontekst: identyfikator statusu w tekstach: `[MD6121]`
   limit: do 40 znaków
   EN: Keen XIV
   PL: Ostrość XIV
74. [Status [MD6121] — opis] 공격 레벨 +10, 방어레벨 +5, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6121].desc
   limit: do 120 znaków
   EN: Offense Level +10, Defense Level +5, Max HP +40%, Damage Dealt +15%, Boss Max HP +30%
   PL: Poziom Ataku +10, Poziom Obrony +5, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +30%
75. [Status [MD6122] — nazwa] 강인함 XIV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6122].name
   kontekst: identyfikator statusu w tekstach: `[MD6122]`
   limit: do 40 znaków
   EN: Resilient XIV
   PL: Twardość XIV
76. [Status [MD6122] — opis] 공격 레벨 +5, 방어 레벨 +15, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6122].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +15, Max HP +45%, Damage Dealt +10%, Boss Max HP +30%
   PL: Poziom Ataku +5, Poziom Obrony +15, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
77. [Status [MD6123] — nazwa] 육체 강화 XIV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6123].name
   kontekst: identyfikator statusu w tekstach: `[MD6123]`
   limit: do 40 znaków
   EN: Body Up XIV
   PL: Umocnienie Ciała XIV
78. [Status [MD6123] — opis] 공격 레벨 +8, 방어 레벨 +8, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6123].desc
   limit: do 120 znaków
   EN: Offense Level +8, Defense Level +8, Max HP +45%, Damage Dealt +10%, Boss Max HP +30%
   PL: Poziom Ataku +8, Poziom Obrony +8, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
79. [Status [MD6124] — nazwa] 성장 XIV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6124].name
   kontekst: identyfikator statusu w tekstach: `[MD6124]`
   limit: do 40 znaków
   EN: Growth XIV
   PL: Rozwój XIV
80. [Status [MD6124] — opis] 공격 레벨 +3, 방어레벨 +3, 최대 체력 +90%, 피해량 증가 10%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6124].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +3, Max HP +90%, Damage Dealt +10%, Boss Max HP +30%
   PL: Poziom Ataku +3, Poziom Obrony +3, Maks. HP +90%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +30%
81. [Status [MD6125] — nazwa] 합 위력 증강 IX
   źródło: Bufs_Mirror6.json :: dataList[id=MD6125].name
   kontekst: identyfikator statusu w tekstach: `[MD6125]`
   limit: do 40 znaków
   EN: Clash Power Up IX
   PL: Wzmocnienie Mocy Starcia IX
82. [Status [MD6125] — opis] 합 위력 +2, 공격 레벨 +4, 방어레벨 +4,최대 체력 +45%, 피해량 증가 15%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6125].desc
   limit: do 130 znaków
   EN: Clash Power +2, Offense Level +4, Defense Level +4, Max HP +45%, Damage Dealt +15%, Boss Max HP +30%
   PL: Moc Starcia +2, Poziom Ataku +4, Poziom Obrony +4, Maks. HP +45%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +30%
83. [Status [MD6126] — nazwa] 최종 위력 증강 IX
   źródło: Bufs_Mirror6.json :: dataList[id=MD6126].name
   kontekst: identyfikator statusu w tekstach: `[MD6126]`
   limit: do 40 znaków
   EN: Final Power Up IX
   PL: Wzmocnienie Mocy Końcowej IX
84. [Status [MD6126] — opis] 최종 위력 +2, 공격 레벨 +3,  방어레벨 +3, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6126].desc
   limit: do 130 znaków
   EN: Final Power +2, Offense Level +3, Defense Level +3, Max HP +40%, Damage Dealt +15%, Boss Max HP +30%
   PL: Moc Końcowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +30%
85. [Status [MD6127] — nazwa] 기본 위력 증강 IX
   źródło: Bufs_Mirror6.json :: dataList[id=MD6127].name
   kontekst: identyfikator statusu w tekstach: `[MD6127]`
   limit: do 40 znaków
   EN: Base Power Up IX
   PL: Wzmocnienie Mocy Bazowej IX
86. [Status [MD6127] — opis] 기본 위력 +2, 공격 레벨 +3, 방어레벨 +3, 최대 체력 +35%, 피해량 증가 15%, 보스 전투 최대 체력 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6127].desc
   limit: do 130 znaków
   EN: Base Power +2, Offense Level +3, Defense Level +3, Max HP +35%, Damage Dealt +15%, Boss Max HP +30%
   PL: Moc Bazowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +35%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +30%
87. [Status [MD6131] — nazwa] 예리 XV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6131].name
   kontekst: identyfikator statusu w tekstach: `[MD6131]`
   limit: do 40 znaków
   EN: Keen XV
   PL: Ostrość XV
88. [Status [MD6131] — opis] 공격 레벨 +10, 방어레벨 +5, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6131].desc
   limit: do 120 znaków
   EN: Offense Level +10, Defense Level +5, Max HP +40%, Damage Dealt +15%, Boss Max HP +40%
   PL: Poziom Ataku +10, Poziom Obrony +5, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +40%
89. [Status [MD6132] — nazwa] 강인함 XV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6132].name
   kontekst: identyfikator statusu w tekstach: `[MD6132]`
   limit: do 40 znaków
   EN: Resilient XV
   PL: Twardość XV
90. [Status [MD6132] — opis] 공격 레벨 +5, 방어 레벨 +15, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6132].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +15, Max HP +45%, Damage Dealt +10%, Boss Max HP +40%
   PL: Poziom Ataku +5, Poziom Obrony +15, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +40%
91. [Status [MD6133] — nazwa] 육체 강화 XV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6133].name
   kontekst: identyfikator statusu w tekstach: `[MD6133]`
   limit: do 40 znaków
   EN: Body Up XV
   PL: Umocnienie Ciała XV
92. [Status [MD6133] — opis] 공격 레벨 +8, 방어 레벨 +8, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6133].desc
   limit: do 120 znaków
   EN: Offense Level +8, Defense Level +8, Max HP +45%, Damage Dealt +10%, Boss Max HP +40%
   PL: Poziom Ataku +8, Poziom Obrony +8, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +40%
93. [Status [MD6134] — nazwa] 성장 XV
   źródło: Bufs_Mirror6.json :: dataList[id=MD6134].name
   kontekst: identyfikator statusu w tekstach: `[MD6134]`
   limit: do 40 znaków
   EN: Growth XV
   PL: Rozwój XV
94. [Status [MD6134] — opis] 공격 레벨 +3, 방어레벨 +3, 최대 체력 +90%, 피해량 증가 10%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6134].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +3, Max HP +90%, Damage Dealt +10%, Boss Max HP +40%
   PL: Poziom Ataku +3, Poziom Obrony +3, Maks. HP +90%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +40%
95. [Status [MD6135] — nazwa] 합 위력 증강 X
   źródło: Bufs_Mirror6.json :: dataList[id=MD6135].name
   kontekst: identyfikator statusu w tekstach: `[MD6135]`
   limit: do 40 znaków
   EN: Clash Power Up X
   PL: Wzmocnienie Mocy Starcia X
96. [Status [MD6135] — opis] 합 위력 +2, 공격 레벨 +4, 방어레벨 +4,최대 체력 +45%, 피해량 증가 15%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6135].desc
   limit: do 130 znaków
   EN: Clash Power +2, Offense Level +4, Defense Level +4, Max HP +45%, Damage Dealt +15%, Boss Max HP +40%
   PL: Moc Starcia +2, Poziom Ataku +4, Poziom Obrony +4, Maks. HP +45%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +40%
97. [Status [MD6136] — nazwa] 최종 위력 증강 X
   źródło: Bufs_Mirror6.json :: dataList[id=MD6136].name
   kontekst: identyfikator statusu w tekstach: `[MD6136]`
   limit: do 40 znaków
   EN: Final Power Up X
   PL: Wzmocnienie Mocy Końcowej X
98. [Status [MD6136] — opis] 최종 위력 +2, 공격 레벨 +3,  방어레벨 +3, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6136].desc
   limit: do 130 znaków
   EN: Final Power +2, Offense Level +3, Defense Level +3, Max HP +40%, Damage Dealt +15%, Boss Max HP +40%
   PL: Moc Końcowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +40%
99. [Status [MD6137] — nazwa] 기본 위력 증강 X
   źródło: Bufs_Mirror6.json :: dataList[id=MD6137].name
   kontekst: identyfikator statusu w tekstach: `[MD6137]`
   limit: do 40 znaków
   EN: Base Power Up X
   PL: Wzmocnienie Mocy Bazowej X
100. [Status [MD6137] — opis] 기본 위력 +2, 공격 레벨 +3, 방어레벨 +3, 최대 체력 +35%, 피해량 증가 15%, 보스 전투 최대 체력 +40%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6137].desc
   limit: do 130 znaków
   EN: Base Power +2, Offense Level +3, Defense Level +3, Max HP +35%, Damage Dealt +15%, Boss Max HP +40%
   PL: Moc Bazowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +35%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +40%
101. [Status [MD6141] — nazwa] 예리 XVI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6141].name
   kontekst: identyfikator statusu w tekstach: `[MD6141]`
   limit: do 40 znaków
   EN: Keen XVI
   PL: Ostrość XVI
102. [Status [MD6141] — opis] 공격 레벨 +10, 방어레벨 +5, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6141].desc
   limit: do 120 znaków
   EN: Offense Level +10, Defense Level +5, Max HP +40%, Damage Dealt +15%, Boss Max HP +50%
   PL: Poziom Ataku +10, Poziom Obrony +5, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +50%
103. [Status [MD6142] — nazwa] 강인함 XVI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6142].name
   kontekst: identyfikator statusu w tekstach: `[MD6142]`
   limit: do 40 znaków
   EN: Resilient XVI
   PL: Twardość XVI
104. [Status [MD6142] — opis] 공격 레벨 +5, 방어 레벨 +15, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6142].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +15, Max HP +45%, Damage Dealt +10%, Boss Max HP +50%
   PL: Poziom Ataku +5, Poziom Obrony +15, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +50%
105. [Status [MD6143] — nazwa] 육체 강화 XVI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6143].name
   kontekst: identyfikator statusu w tekstach: `[MD6143]`
   limit: do 40 znaków
   EN: Body Up XVI
   PL: Umocnienie Ciała XVI
106. [Status [MD6143] — opis] 공격 레벨 +8, 방어 레벨 +8, 최대 체력 +45%, 피해량 증가 10%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6143].desc
   limit: do 120 znaków
   EN: Offense Level +8, Defense Level +8, Max HP +45%, Damage Dealt +10%, Boss Max HP +50%
   PL: Poziom Ataku +8, Poziom Obrony +8, Maks. HP +45%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +50%
107. [Status [MD6144] — nazwa] 성장 XVI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6144].name
   kontekst: identyfikator statusu w tekstach: `[MD6144]`
   limit: do 40 znaków
   EN: Growth XVI
   PL: Rozwój XVI
108. [Status [MD6144] — opis] 공격 레벨 +3, 방어레벨 +3, 최대 체력 +90%, 피해량 증가 10%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6144].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +3, Max HP +90%, Damage Dealt +10%, Boss Max HP +50%
   PL: Poziom Ataku +3, Poziom Obrony +3, Maks. HP +90%, Zadawane Obrażenia +10%, w walkach z bossami Maks. HP +50%
109. [Status [MD6145] — nazwa] 합 위력 증강 XI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6145].name
   kontekst: identyfikator statusu w tekstach: `[MD6145]`
   limit: do 40 znaków
   EN: Clash Power Up XI
   PL: Wzmocnienie Mocy Starcia XI
110. [Status [MD6145] — opis] 합 위력 +2, 공격 레벨 +4, 방어레벨 +4,최대 체력 +45%, 피해량 증가 15%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6145].desc
   limit: do 130 znaków
   EN: Clash Power +2, Offense Level +4, Defense Level +4, Max HP +45%, Damage Dealt +15%, Boss Max HP +50%
   PL: Moc Starcia +2, Poziom Ataku +4, Poziom Obrony +4, Maks. HP +45%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +50%
111. [Status [MD6146] — nazwa] 최종 위력 증강 XI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6146].name
   kontekst: identyfikator statusu w tekstach: `[MD6146]`
   limit: do 40 znaków
   EN: Final Power Up XI
   PL: Wzmocnienie Mocy Końcowej XI
112. [Status [MD6146] — opis] 최종 위력 +2, 공격 레벨 +3,  방어레벨 +3, 최대 체력 +40%, 피해량 증가 15%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6146].desc
   limit: do 130 znaków
   EN: Final Power +2, Offense Level +3, Defense Level +3, Max HP +40%, Damage Dealt +15%, Boss Max HP +50%
   PL: Moc Końcowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +40%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +50%
113. [Status [MD6147] — nazwa] 기본 위력 증강 XI
   źródło: Bufs_Mirror6.json :: dataList[id=MD6147].name
   kontekst: identyfikator statusu w tekstach: `[MD6147]`
   limit: do 40 znaków
   EN: Base Power Up XI
   PL: Wzmocnienie Mocy Bazowej XI
114. [Status [MD6147] — opis] 기본 위력 +2, 공격 레벨 +3, 방어레벨 +3, 최대 체력 +35%, 피해량 증가 15%, 보스 전투 최대 체력 +50%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6147].desc
   limit: do 130 znaków
   EN: Base Power +2, Offense Level +3, Defense Level +3, Max HP +35%, Damage Dealt +15%, Boss Max HP +50%
   PL: Moc Bazowa +2, Poziom Ataku +3, Poziom Obrony +3, Maks. HP +35%, Zadawane Obrażenia +15%, w walkach z bossami Maks. HP +50%
115. [Status [MD6Limit101] — nazwa] 레벨 강화
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit101].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit101]`
   limit: do 40 znaków
   EN: Level Boost
   PL: Wzmocnienie Poziomu
116. [Status [MD6Limit101] — opis] 모든 적 레벨 3 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit101].desc
   limit: do 120 znaków
   EN: All Enemy Levels +3
   PL: Poziom wszystkich przeciwników +3
117. [Status [MD6Limit102] — nazwa] 쇠약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit102].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit102]`
   limit: do 40 znaków
   EN: Frailness
   PL: Wyniszczenie
118. [Status [MD6Limit102] — opis] 모든 아군의 최대 체력 -10%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit102].desc
   limit: do 120 znaków
   EN: -10% Max HP for all allies
   PL: Maks. HP wszystkich sojuszników -10%
119. [Status [MD6Limit103] — nazwa] 불꽃 낙인 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit103].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit103]`
   limit: do 40 znaków
   EN: Mark of Fire I
   PL: Znamię Ognia I
120. [Status [MD6Limit103] — opis] 턴 종료 시 모든 아군이 체력 5 고정 피해를 받음. 턴 마다 체력 고정 피해가 3 증가 (최대 20)
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit103].desc
   limit: do 130 znaków
   EN: Turn End: all allies take 5 fixed HP damage. Fixed damage increases by 3 every turn. (max 20)
   PL: Na koniec tury wszyscy sojusznicy otrzymują 5 stałych obrażeń HP. Co turę stałe obrażenia HP rosną o 3 (maks. 20)
121. [Status [MD6Limit104] — nazwa] 인플레이션 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit104].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit104]`
   limit: do 40 znaków
   EN: Inflation I
   PL: Inflacja I
122. [Status [MD6Limit104] — opis] 상점 내 판매를 제외한 모든 기능의 가격 2배 상승
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit104].desc
   limit: do 120 znaków
   EN: Doubles the cost of every Shop function, except for selling E.G.O Gifts
   PL: Podwaja ceny wszystkich funkcji Sklepu, z wyjątkiem sprzedaży Darów E.G.O
123. [Status [MD6Limit105] — nazwa] 자아 간섭 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit105].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit105]`
   limit: do 40 znaków
   EN: Ego Interference I
   PL: Interferencja Ego I
124. [Status [MD6Limit105] — opis] E.G.O 사용 시 소모되는 자원이 2배로 증가\n(기프트 효과에 영향을 주지 않음)
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit105].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Doubles the amount of E.G.O Resources consumed when using E.G.O Skills\n(Does not interact with E.G.O Gift effects)
   PL: Podwaja ilość zasobów E.G.O zużywanych przy użyciu Umiejętności E.G.O\n(Nie wpływa na efekty Darów E.G.O)
125. [Status [MD6Limit111] — nazwa] 레벨 강화
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit111].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit111]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Status [MD6Limit111] — opis] 모든 적 레벨 3 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit111].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Status [MD6Limit112] — nazwa] 쇠약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit112].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit112]`
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Status [MD6Limit112] — opis] 모든 아군의 최대 체력 -10%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit112].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Status [MD6Limit113] — nazwa] 정신 착란 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit113].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit113]`
   limit: do 40 znaków
   EN: Mental Psychosis I
   PL: Psychoza I
130. [Status [MD6Limit113] — opis] 턴 종료 시 모든 아군의 정신력 3 감소
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit113].desc
   limit: do 120 znaków
   EN: Turn End: all allies lose 3 SP
   PL: Na koniec tury wszyscy sojusznicy tracą 3 Poczytalności
131. [Status [MD6Limit114] — nazwa] 신경 촉진 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit114].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit114]`
   limit: do 40 znaków
   EN: Nerve Acceleration I
   PL: Przyspieszenie Nerwów I
132. [Status [MD6Limit114] — opis] 모든 적의 속도 최솟값, 속도 최댓값 +1 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit114].desc
   limit: do 120 znaków
   EN: Raise Min & Max Speed values by 1 for all enemies
   PL: Minimalna i maksymalna Szybkość wszystkich przeciwników +1
133. [Status [MD6Limit115] — nazwa] 정신력 고갈 I
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit115].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit115]`
   limit: do 40 znaków
   EN: SP Fatigue I
   PL: Wyczerpanie Poczytalności I
134. [Status [MD6Limit115] — opis] 전투 내 모든 아군의 정신력이 35초과로 회복 불가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit115].desc
   limit: do 120 znaków
   EN: In battles, allies cannot heal higher than 35 SP
   PL: W walkach Poczytalność wszystkich sojuszników nie może przekroczyć 35
135. [Status [MD6Limit121] — nazwa] 레벨 강화
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit121].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit121]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Status [MD6Limit121] — opis] 모든 적 레벨 3 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit121].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Status [MD6Limit122] — nazwa] 쇠약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit122].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit122]`
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Status [MD6Limit122] — opis] 모든 아군의 최대 체력 -10%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit122].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Status [MD6Limit123] — nazwa] 진동 차단
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit123].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit123]`
   limit: do 40 znaków
   EN: Tremor Barrier
   PL: Bariera Wstrząsu
140. [Status [MD6Limit123] — opis] 모든 적의 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit123].desc
   limit: do 120 znaków
   EN: Remove the first Stagger Threshold for all enemies
   PL: Usuwa pierwszy Próg Oszołomienia u wszystkich przeciwników
141. [Status [MD6Limit124] — nazwa] 인플레이션 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit124].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit124]`
   limit: do 40 znaków
   EN: Inflation II
   PL: Inflacja II
142. [Status [MD6Limit124] — opis] 상점 내 판매를 제외한 모든 기능의 가격 3배 상승
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit124].desc
   limit: do 120 znaków
   EN: Triples the cost of every Shop function, except for selling E.G.O Gifts
   PL: Potroja ceny wszystkich funkcji Sklepu, z wyjątkiem sprzedaży Darów E.G.O
143. [Status [MD6Limit125] — nazwa] 자아 간섭 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit125].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit125]`
   limit: do 40 znaków
   EN: Ego Interference II
   PL: Interferencja Ego II
144. [Status [MD6Limit125] — opis] E.G.O 사용 시 소모되는 자원이 3배로 증가\n(기프트 효과에 영향을 주지 않음)
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit125].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Triples the amount of E.G.O Resources consumed when using E.G.O Skills\n(Does not interact with E.G.O Gift effects)
   PL: Potroja ilość zasobów E.G.O zużywanych przy użyciu Umiejętności E.G.O\n(Nie wpływa na efekty Darów E.G.O)
145. [Status [MD6Limit131] — nazwa] 레벨 강화
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit131].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit131]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Status [MD6Limit131] — opis] 모든 적 레벨 3 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit131].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Status [MD6Limit132] — nazwa] 쇠약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit132].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit132]`
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Status [MD6Limit132] — opis] 모든 아군의 최대 체력 -10%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit132].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Status [MD6Limit133] — nazwa] 생명력 증폭
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit133].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit133]`
   limit: do 40 znaków
   EN: Vitality Boost
   PL: Wzmocnienie Witalności
150. [Status [MD6Limit133] — opis] 모든 적의 최대 체력 증가 +30%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit133].desc
   limit: do 120 znaków
   EN: +30% to max HP for all enemies
   PL: Maks. HP wszystkich przeciwników +30%
151. [Status [MD6Limit134] — nazwa] 파괴력
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit134].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit134]`
   limit: do 40 znaków
   EN: Brutality
   PL: Siła Niszczenia
152. [Status [MD6Limit134] — opis] 모든 적의 더하기 코인 위력 +2, 빼기 코인 위력 -2
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit134].desc
   limit: do 120 znaków
   EN: Plus Coin Power +2, Minus Coin Power -2 for all enemies
   PL: Moc Monet Plus wszystkich przeciwników +2, Moc Monet Minus -2
153. [Status [MD6Limit135] — nazwa] 불꽃 낙인 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit135].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit135]`
   limit: do 40 znaków
   EN: Mark of Fire II
   PL: Znamię Ognia II
154. [Status [MD6Limit135] — opis] 턴 종료 시 모든 아군이 체력 10 고정 피해를 받음. 턴 마다 체력 고정 피해가 5 증가 (최대 30)
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit135].desc
   limit: do 130 znaków
   EN: Turn End: all allies take 10 fixed HP damage. Fixed damage increases by 5 every turn. (max 30)
   PL: Na koniec tury wszyscy sojusznicy otrzymują 10 stałych obrażeń HP. Stałe obrażenia HP rosną o 5 co turę (maks. 30)
155. [Status [MD6Limit141] — nazwa] 레벨 강화
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit141].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit141]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Status [MD6Limit141] — opis] 모든 적 레벨 3 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit141].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Status [MD6Limit142] — nazwa] 쇠약
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit142].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit142]`
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Status [MD6Limit142] — opis] 모든 아군의 최대 체력 -10%
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit142].desc
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Status [MD6Limit143] — nazwa] 정신 착란 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit143].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit143]`
   limit: do 40 znaków
   EN: Mental Psychosis II
   PL: Psychoza II
160. [Status [MD6Limit143] — opis] 턴 종료 시 모든 아군의 정신력 5 감소
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit143].desc
   limit: do 120 znaków
   EN: Turn End: all allies lose 5 SP
   PL: Na koniec tury wszyscy sojusznicy tracą 5 Poczytalności
161. [Status [MD6Limit144] — nazwa] 신경 촉진 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit144].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit144]`
   limit: do 40 znaków
   EN: Nerve Acceleration II
   PL: Przyspieszenie Nerwów II
162. [Status [MD6Limit144] — opis] 모든 적의 속도 최솟값, 속도 최댓값 +2 증가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit144].desc
   limit: do 120 znaków
   EN: Raise Min & Max Speed values by 2 for all enemies
   PL: Minimalna i maksymalna Szybkość wszystkich przeciwników +2
163. [Status [MD6Limit145] — nazwa] 정신력 고갈 II
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit145].name
   kontekst: identyfikator statusu w tekstach: `[MD6Limit145]`
   limit: do 40 znaków
   EN: SP Fatigue II
   PL: Wyczerpanie Poczytalności II
164. [Status [MD6Limit145] — opis] 전투 내 모든 아군의 정신력이 30초과로 회복 불가
   źródło: Bufs_Mirror6.json :: dataList[id=MD6Limit145].desc
   limit: do 120 znaków
   EN: In battles, allies cannot heal higher than 30 SP
   PL: W trakcie walki Poczytalność wszystkich sojuszników nie może przekroczyć 30
165. [Status [DerivativeHugeIrritation] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: Bufs_Mirror6.json :: dataList[id=DerivativeHugeIrritation].name
   kontekst: identyfikator statusu w tekstach: `[DerivativeHugeIrritation]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
166. [Status [DerivativeHugeIrritation] — opis] - 턴 시작 시, 잃은 체력 15%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 5)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +3, 진동 횟수 증가량 +1\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 40%)\n- '이연참-폭', '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: Bufs_Mirror6.json :: dataList[id=DerivativeHugeIrritation].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Damage Up and 1 Power Up for every 15% missing HP on self (max 5 each)\n- Inflict +3 more Tremor Potency and +1 more Tremor Count with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 40%)\n- Convert the final Coins of 'Double Slash - Blast' and 'Triple Slash - Burst' to Unbreakable Coins
   PL: - Na początek tury: zyskuje 1 Wzrostu Obrażeń i 1 Wzrostu Mocy za każde 15% brakującego HP (każde maks. 5)\n- Wartość Siły Wstrząsu nadawanej Umiejętnościami wrogom +3, wartość nadawanego Licznika Wstrząsu +1\n- Jeśli Szybkość tej jednostki przewyższa Szybkość celu o 3 lub więcej, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 40%)\n- Ostatnie monety umiejętności 'Podwójne Cięcie - Wybuch' i 'Potrójne Cięcie - Seria' zmieniają się w Niezniszczalne Monety
167. [Status [GiveMeCandy] — nazwa] 사탕
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy].name
   kontekst: identyfikator statusu w tekstach: `[GiveMeCandy]`
   limit: do 40 znaków
   EN: Candy
   PL: Cukierek
168. [Status [GiveMeCandy] — opis] 최댓값: 99\n사탕을 가지고 주지 않고 있을까?
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 99\n- Are you hoarding candy all for yourself?
   PL: Maks.: 99\nCzy nie chomikujesz cukierków tylko dla siebie?
169. [Status [HungryCharon] — nazwa] 배고픔-분노
   źródło: Bufs_Mirror6.json :: dataList[id=HungryCharon].name
   kontekst: identyfikator statusu w tekstach: `[HungryCharon]`
   limit: do 40 znaków
   EN: Hunger-Rage
   PL: Głód-Wściekłość
170. [Status [HungryCharon] — opis] 최댓값: 3\n배고파. 빨리 사탕줘
   źródło: Bufs_Mirror6.json :: dataList[id=HungryCharon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nI'm starving. I want candy now
   PL: Maks.: 3\nUmieram z głodu. Chcę cukierka natychmiast
171. [Status [FullCharon] — nazwa] 포만감
   źródło: Bufs_Mirror6.json :: dataList[id=FullCharon].name
   kontekst: identyfikator statusu w tekstach: `[FullCharon]`
   limit: do 40 znaków
   EN: Indulged
   PL: Nasycenie
172. [Status [FullCharon] — opis] 턴 시작 시 수치 2당 합 위력 감소 1 얻음 (최대 5)
   źródło: Bufs_Mirror6.json :: dataList[id=FullCharon].desc
   limit: do 120 znaków
   EN: Turn Start: for every 2 Stack, gain 1 Clash Power Down (max 5)
   PL: Na początek tury za każde 2 wartości zyskuje 1 Spadku Mocy Starcia (maks. 5)
173. [Status [GiveMeCandy_LowMorale] — nazwa] 사탕
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[GiveMeCandy_LowMorale]`
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Status [GiveMeCandy_LowMorale] — opis] - 사기 저하\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +3, 그 외의 인격과 합 진행시, 합 위력 -1
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When Clashing against Identities with Candy, Clash Power +3; when clashing against other Identities, Clash Power -1
   PL: - Obniżone Morale\n- W Starciu z tożsamością posiadającą Cukierek Moc Starcia +3; w Starciu z pozostałymi tożsamościami Moc Starcia -1
175. [Status [GiveMeCandy_LowMorale] — podsumowanie] 조건에 따라 합위력 증감
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_LowMorale].summary
   limit: do 120 znaków
   EN: Conditional Clash Power fluctuation
   PL: Warunkowe Wahanie Mocy Starcia
176. [Status [GiveMeCandy_Panic] — nazwa] 사탕
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_Panic].name
   kontekst: identyfikator statusu w tekstach: `[GiveMeCandy_Panic]`
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Status [GiveMeCandy_Panic] — opis] - 패닉\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +5, 그 외의 인격과 합 진행시, 합 위력 -2
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- When Clashing against Identities with Candy, Clash Power +5; when clashing against other Identities, Clash Power -2
   PL: - Panika\n- W Starciu z tożsamością posiadającą Cukierek Moc Starcia +5; w Starciu z pozostałymi tożsamościami Moc Starcia -2
178. [Status [GiveMeCandy_Panic] — podsumowanie] 조건에 따라 합위력 증감
   źródło: Bufs_Mirror6.json :: dataList[id=GiveMeCandy_Panic].summary
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Status [UnfinishedDreamMirror] — nazwa] 물보다 진한 피에서 벗어나,
   źródło: Bufs_Mirror6.json :: dataList[id=UnfinishedDreamMirror].name
   kontekst: identyfikator statusu w tekstach: `[UnfinishedDreamMirror]`
   limit: do 90 znaków
   EN: IN WHICH IS RECOUNTED THE LIBERATION FROM BLOOD THICKER THAN WATER
   PL: Oswobodzenie z krwi gęstszej niż woda,
180. [Status [UnfinishedDreamMirror] — opis] - 매 턴 종료 시, 다음 턴에 신속 1, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs_Mirror6.json :: dataList[id=UnfinishedDreamMirror].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At every Turn End: gain 1 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Na koniec tury w następnej turze zyskuje 1 Pośpiechu i 3 Wzrosty Poziomu Ataku\n- Za każde 3 skumulowane tury zyskuje dodatkowe 2 Wzrosty Poziomu Ataku (maks. 6)\n- Wygrana w Starciu: odzyskuje 3 Poczytalności\n- Za zabicie wroga zyskuje 1 Wzrost Mocy Starcia w następnej turze (raz na turę)
181. [Status [UnfinishedDreamSanchoMirror] — nazwa] 물보다 진한 피에서 벗어나지 못하여,
   źródło: Bufs_Mirror6.json :: dataList[id=UnfinishedDreamSanchoMirror].name
   kontekst: identyfikator statusu w tekstach: `[UnfinishedDreamSanchoMirror]`
   limit: do 90 znaków
   EN: In which is recounted the thralldom to blood thicker than water.
   PL: Niezdolny do oswobodzenia z krwi gęstszej niż woda,
182. [Status [UnfinishedDreamSanchoMirror] — opis] - 경혈을 얻을 때마다, 경혈을 2 추가로 얻음. (턴 당 최대 5회)\n- 매 턴 종료 시, 다음 턴에 신속 2, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: Bufs_Mirror6.json :: dataList[id=UnfinishedDreamSanchoMirror].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 2 additional Hardblood every time this unit gains Hardblood. (5 times per turn)\n- At every Turn End: gain 2 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Za każdym razem, gdy zyskuje Twardą Krew, zyskuje dodatkowo 2 Twardą Krew (maks. 5 razy na turę)\n- Na koniec tury w następnej turze zyskuje 2 Pośpiechu i 3 Wzrosty Poziomu Ataku\n- Za każde 3 skumulowane tury zyskuje dodatkowe 2 Wzrosty Poziomu Ataku (maks. 6)\n- Wygrana w Starciu: odzyskuje 3 Poczytalności\n- Za zabicie wroga zyskuje 1 Wzrost Mocy Starcia w następnej turze (raz na turę)
183. [Status [FragmentOfHopeFamilyMirror] — nazwa] 내 아이의 동료들아
   źródło: Bufs_Mirror6.json :: dataList[id=FragmentOfHopeFamilyMirror].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHopeFamilyMirror]`
   limit: do 50 znaków
   EN: O compatriots of my dear child
   PL: O towarzysze mego drogiego dziecka
184. [Status [FragmentOfHopeFamilyMirror] — opis] 수치당 합 위력 +1 (최대 4)\n가하는 피해량 +5%
   źródło: Bufs_Mirror6.json :: dataList[id=FragmentOfHopeFamilyMirror].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +1 per Stack (max 4)\nDeal +5% damage
   PL: Moc Starcia +1 za każdą wartość (maks. 4)\nZadawane Obrażenia +5%
185. [Status [FragmentOfHopeTwoFamilyMirror] — nazwa] 나를 대신해 그 아이의 꿈을 함께 해주려무나
   źródło: Bufs_Mirror6.json :: dataList[id=FragmentOfHopeTwoFamilyMirror].name
   kontekst: identyfikator statusu w tekstach: `[FragmentOfHopeTwoFamilyMirror]`
   limit: do 50 znaków
   EN: Dream her dream together in my stead
   PL: Śnijcie wspólnie jej sen zamiast mnie
186. [Status [FragmentOfHopeTwoFamilyMirror] — opis] 수치당 합 위력 +2 (최대 8)\n전투 시작 시 자신과 아군에게 보호막 부여\n적중시마다 고정 피해 1 입힘
   źródło: Bufs_Mirror6.json :: dataList[id=FragmentOfHopeTwoFamilyMirror].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +2 for every value (max 8)\n- Apply Shield to self and all allies at Combat Start\n- On Hit, deal 1 fixed damage
   PL: Moc Starcia +2 za każdą wartość (maks. 8)\nNa początku walki nakłada na siebie i sojuszników Tarczę\nPrzy każdym trafieniu zadaje 1 stałych obrażeń
187. [Status [VerEmergencyCandy] — nazwa] 비상용 사탕
   źródło: Bufs_Mirror6.json :: dataList[id=VerEmergencyCandy].name
   kontekst: identyfikator statusu w tekstach: `[VerEmergencyCandy]`
   limit: do 40 znaków
   EN: Backup Candy
   PL: Zapasowy Cukierek
188. [Status [VerEmergencyCandy] — opis] 턴 종료 시 최대 체력의 60% 미만이라면\n최대 체력의 30%만큼 회복, 정신력을 15 회복하고 비상용 사탕 1, 배고픔 1 감소\n수치가 0이 되면, 빛나는 포만감을 1 부여하고 소멸
   źródło: Bufs_Mirror6.json :: dataList[id=VerEmergencyCandy].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: at less than 60% HP...\nHeal 30% HP, heal 15 SP, lose 1 Backup Candy, and 1 Hunger\nAt 0 Stack, apply 1 Incandescent Indulgence, then expires
   PL: Na koniec tury, jeśli HP poniżej 60% Maks. HP:\nodzyskuje 30% Maks. HP i 15 Poczytalności, traci 1 Zapasowy Cukierek i 1 Głód\nGdy wartość osiągnie 0, nakłada 1 Rozżarzone Nasycenie i znika
189. [Status [VerHunger] — nazwa] 배고픔
   źródło: Bufs_Mirror6.json :: dataList[id=VerHunger].name
   kontekst: identyfikator statusu w tekstach: `[VerHunger]`
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
190. [Status [VerHunger] — opis] 최댓값: 3\n턴 종료 시 다음 턴에 스택만큼 공격 레벨 증가 2 얻음, 피해량 증가 1 얻음\n최댓값(3)인 경우 턴 종료 시 최대 체력의 5% 만큼 체력 감소
   źródło: Bufs_Mirror6.json :: dataList[id=VerHunger].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nTurn End: gain 2 Offense Level Up and 1 Damage Up next turn for every Stack\nAt max Stack(3), lose 5% HP at Turn End
   PL: Maks.: 3\nNa koniec tury zyskuje 2 Wzrosty Poziomu Ataku i 1 Wzrost Obrażeń w następnej turze za każdy stos\nPrzy wartości maksymalnej (3) traci 5% Maks. HP na koniec tury
191. [Status [VerShiningFullness] — nazwa] 빛나는 포만감
   źródło: Bufs_Mirror6.json :: dataList[id=VerShiningFullness].name
   kontekst: identyfikator statusu w tekstach: `[VerShiningFullness]`
   limit: do 40 znaków
   EN: Incandescent Indulgence
   PL: Rozżarzone Nasycenie
192. [Status [VerShiningFullness] — opis] 이번 스테이지 동안 기본 최대 체력이 30% 상승\n턴 시작 시 모든 체력과 정신력을 회복 (전투 당 1번)
   źródło: Bufs_Mirror6.json :: dataList[id=VerShiningFullness].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 30% base HP for this Encounter\nTurn Start: fully heal HP and SP (once per Encounter)
   PL: Przez ten etap walki bazowe Maks. HP rośnie o 30%\nNa początek tury w pełni odzyskuje HP i Poczytalność (raz na walkę)

## Statusy i efekty bojowe — Bufs_Mirror7
- plik gry: `Bufs_Mirror7.json`

193. [Status [ObjectOfExploration] — nazwa] 탐구 대상
   źródło: Bufs_Mirror7.json :: dataList[id=ObjectOfExploration].name
   kontekst: identyfikator statusu w tekstach: `[ObjectOfExploration]`
   limit: do 40 znaków
   EN: Curio
   PL: Kuriozum
194. [Status [ObjectOfExploration] — opis] 특정 조건 만족 시, ‘그림 재료’로 교체됨
   źródło: Bufs_Mirror7.json :: dataList[id=ObjectOfExploration].desc
   limit: do 120 znaków
   EN: When certain conditions are fulfilled, replace this effect with 'Art Medium'
   PL: Po spełnieniu określonych warunków zamienia się w 'Materiał Malarski'
195. [Status [Inspire] — nazwa] 영감
   źródło: Bufs_Mirror7.json :: dataList[id=Inspire].name
   kontekst: identyfikator statusu w tekstach: `[Inspire]`
   limit: do 40 znaków
   EN: Spark of Inspiration
   PL: Natchnienie
196. [Status [Inspire] — opis] 그림 재료를 보유한 대상 공격 시 피해량 +10%
   źródło: Bufs_Mirror7.json :: dataList[id=Inspire].desc
   limit: do 120 znaków
   EN: Deal +10% damage against targets with Art Medium
   PL: Atakując cel posiadający Materiał Malarski, zadaje +10% obrażeń
197. [Status [PaintingMaterial] — nazwa] 그림 재료
   źródło: Bufs_Mirror7.json :: dataList[id=PaintingMaterial].name
   kontekst: identyfikator statusu w tekstach: `[PaintingMaterial]`
   limit: do 40 znaków
   EN: Art Medium
   PL: Materiał Malarski
198. [Status [PaintingMaterial] — opis] 출혈을 보유(집중 전투일 경우 부위마다 별도로 판정)하고 있으면, 색욕 속성 받는 피해량 +10%
   źródło: Bufs_Mirror7.json :: dataList[id=PaintingMaterial].desc
   limit: do 160 znaków
   EN: If this unit has Bleed (in Focused Encounters, count Bleed on each Part separately), take +10% damage from Lust Skills
   PL: Jeśli jednostka posiada Krwawienie (w walkach skupionych rozpatrywane osobno dla każdej części), otrzymuje +10% obrażeń atrybutu Żądzy
199. [Status [GreatAesthetics] — nazwa] 훌륭한 미감
   źródło: Bufs_Mirror7.json :: dataList[id=GreatAesthetics].name
   kontekst: identyfikator statusu w tekstach: `[GreatAesthetics]`
   limit: do 40 znaków
   EN: Exquisite Aesthetics
   PL: Wyrafinowana Estetyka
200. [Status [GreatAesthetics] — opis] - 더하기 코인 스킬의 코인 위력 +1, 빼기 코인 스킬의 기본 위력 +(4/코인 수)\n- 스킬 피해량 +30%
   źródło: Bufs_Mirror7.json :: dataList[id=GreatAesthetics].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Plus Coin Skills gain Coin Power +1; Minus Coin Skills gain Base Power +(4 / # of Coins)\n- Deal +30% damage with Skills
   PL: - Umiejętności z monetami Plus zyskują Moc Monet +1; Umiejętności z monetami Minus zyskują Moc bazową +(4/liczba monet)\n- Zadaje +30% obrażeń Umiejętnościami
201. [Status [GiftCannon] — nazwa] 화력
   źródło: Bufs_Mirror7.json :: dataList[id=GiftCannon].name
   kontekst: identyfikator statusu w tekstach: `[GiftCannon]`
   limit: do 40 znaków
   EN: Firepower
   PL: Siła Ognia
202. [Status [GiftCannon] — opis] - 최댓값: 10\n- 수치 1당 가하는 피해량 +10%
   źródło: Bufs_Mirror7.json :: dataList[id=GiftCannon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Deal +10% damage for every Stack
   PL: - Maks.: 10\n- Za każdą wartość zadaje +10% obrażeń
203. [Status [GiftGlass] — nazwa] 연약
   źródło: Bufs_Mirror7.json :: dataList[id=GiftGlass].name
   kontekst: identyfikator statusu w tekstach: `[GiftGlass]`
   limit: do 40 znaków
   EN: Delicateness
   PL: Delikatność
204. [Status [GiftGlass] — opis] - 최댓값: 10\n- 수치 1당 받는 피해량 +10%
   źródło: Bufs_Mirror7.json :: dataList[id=GiftGlass].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Take +10% damage for every Stack
   PL: - Maks.: 10\n- Za każdą wartość otrzymuje +10% obrażeń
205. [Status [BlandishmentShinEnemyDelete] — nazwa] 신(心) - ???
   źródło: Bufs_Mirror7.json :: dataList[id=BlandishmentShinEnemyDelete].name
   kontekst: identyfikator statusu w tekstach: `[BlandishmentShinEnemyDelete]`
   limit: do 40 znaków
   EN: Shin (心) - ???
   PL: Shin (心) - ???
206. [Status [BlandishmentShinEnemyDelete] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +2, 방어 레벨 +2\n- 스킬로 획득하는 호흡 위력과 횟수 +1\n- 가하는 피해량 +(25+잃은 체력 비율)% (최대 100%)
   źródło: Bufs_Mirror7.json :: dataList[id=BlandishmentShinEnemyDelete].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +2, Defense Level +2\n- Gain +1 more Poise Potency and Poise Count from Skills\n- Deal +(missing HP percentage + 25)% damage (max 100%)
   PL: - Minimalna i maksymalna Szybkość +1\n- Poziom Ataku +2, Poziom Obrony +2\n- Zyskiwana z Umiejętności Moc Oddechu i Licznik Oddechu +1\n- Zadawane Obrażenia +(25+procent utraconego HP)% (maks. 100%)
207. [Status [EnhanceRoseSign] — nazwa] 굴레
   źródło: Bufs_Mirror7.json :: dataList[id=EnhanceRoseSign].name
   kontekst: identyfikator statusu w tekstach: `[EnhanceRoseSign]`
   limit: do 40 znaków
   EN: Bridle
   PL: Uzda
208. [Status [EnhanceRoseSign] — opis] - ((현재 층 - 4) x 10)%만큼 모든 아군의 최대 체력이 증가 (최대 60%)\n- 모든 아군의 공격 레벨 + (현재 층 - 4) (최대 5)
   źródło: Bufs_Mirror7.json :: dataList[id=EnhanceRoseSign].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All allies gain ((current Floor - 4) x 10)% max HP (max 60%)\n- All allies gain Offense Level +(current Floor - 4) (max 5)
   PL: - Wszyscy sojusznicy zyskują Maks. HP o ((obecne Piętro - 4) x 10)% (maks. 60%)\n- Wszyscy sojusznicy zyskują Poziom Ataku +(obecne Piętro - 4) (maks. 5)
209. [Status [LookingFutureMirror] — nazwa] 순간의 예지
   źródło: Bufs_Mirror7.json :: dataList[id=LookingFutureMirror].name
   kontekst: identyfikator statusu w tekstach: `[LookingFutureMirror]`
   limit: do 40 znaków
   EN: Glimpse of Precognition
   PL: Pobłysk Przeczuć
210. [Status [LookingFutureMirror] — opis] - 최댓값 : 5\n\n- 수치 1당, 합 위력 +2\n- 수치 2당, 더하기 코인 스킬인 경우 코인 위력 +1, 빼기 코인 스킬인 경우 최종 위력 +2\n스킬 종료 시 소멸
   źródło: Bufs_Mirror7.json :: dataList[id=LookingFutureMirror].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n\n- Clash Power +2 for every Stack\n- For every 2 Stack:\n  - Plus Coin Skills gain Coin Power +1\n  - Minus Coin Skills gain Final Power +2\n- Expires at Skill End
   PL: - Maks.: 5\n\n- Za każdą wartość Moc Starcia +2\n- Za każde 2 wartości: umiejętność z monetą Plus zyskuje Moc Monet +1, umiejętność z monetą Minus zyskuje Moc Końcową +2\nZnika po zakończeniu umiejętności
211. [Status [MiddleFatherGutsMirror] — nazwa] 초근성
   źródło: Bufs_Mirror7.json :: dataList[id=MiddleFatherGutsMirror].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherGutsMirror]`
   limit: do 40 znaków
   EN: Ridiculous Grit
   PL: Zwariowana Wytrwałość
212. [Status [MiddleFatherGutsMirror] — opis] - 스킬로 받는 피해를 (50 + 잃은 체력 비율)% 만큼 감소함 (소수점 버림)\n\n- 합 승리시 (합 횟수 x 5)만큼 정신력 추가로 오름 (최대 15)\n\n- 턴 종료시 자신의 스킬 효과로 이번 턴 정신력이 감소했으면, 다음 턴에 피해량 증가 3 얻음
   źródło: Bufs_Mirror7.json :: dataList[id=MiddleFatherGutsMirror].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take -(50 + missing HP percentage)% damage from Skills (rounded down)\n\n- On Clash Win, heal (Clash Count x 5) more SP (max 15)\n\n- Turn End: If this unit lost SP this turn due to its Skill effects, gain 3 Damage Up next turn
   PL: - Obrażenia od Umiejętności maleją o (50 + % utraconego HP)% (bez części dziesiętnych)\n\n- Wygrana w Starciu: dodatkowo odzyskuje Poczytalność (liczba Starć x 5) (maks. 15)\n\n- Na koniec tury, jeśli jej Umiejętności obniżyły dziś Poczytalność, w następnej turze zyskuje 3 Wzrost Obrażeń
213. [Status [MiddleFatherGutsMirror] — tekst klimatyczny] “신(心)이니 뭐니 다 필요 없어. 이 악물고 지금까지 새겨 온 모든 문신의 힘을 끌어 올리면, 신(心) 같은 기술 없이도 난 충분히 강하다.”
   źródło: Bufs_Mirror7.json :: dataList[id=MiddleFatherGutsMirror].flavor
   limit: do 250 znaków
   EN: "I don't need some stupid crutch like that "Shin (心)" crap. I just gotta pull as much power as I can from these tattoos and grit my teeth, and I'll overpower your fancy little tricks no problem."
   PL: „Shin (心) czy co tam jeszcze — nic z tego nie potrzebuję. Zaciśnę zęby i wyciągnę całą moc ze wszystkich wytatuowanych do dziś znaków. Bez technik pokroju Shin (心) i tak jestem wystarczająco silny.”
214. [Status [FutureEyeOnMirror] — nazwa] 예지안
   źródło: Bufs_Mirror7.json :: dataList[id=FutureEyeOnMirror].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOnMirror]`
   limit: do 40 znaków
   EN: Eye of Precognition
   PL: Oko Prekognicji
215. [Status [FutureEyeOnMirror] — opis] - 최댓값: 30\n- 합 위력 +2\n- 턴 시작 시 5 증가
   źródło: Bufs_Mirror7.json :: dataList[id=FutureEyeOnMirror].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Clash Power +2\n- Turn Start: Gain 5 Stack
   PL: - Maks.: 30\n- Moc Starcia +2\n- Na początek tury rośnie o 5
216. [Status [FutureEyeOnMirror] — tekst klimatyczny] ‘마법처럼 미래를 보여 주는 건 아니다. 이 눈은 시야에 들어온 모든 것을 분석해 앞으로 다가올 찰나의 순간을 예측해 주는 계산기에 가깝다.’
   źródło: Bufs_Mirror7.json :: dataList[id=FutureEyeOnMirror].flavor
   limit: do 290 znaków
   EN: "The eye does not possess some supernatural power that shows its user the destined future. It is more akin to a computing device that analyzes everything it sees and provides the most likely scenario in the upcoming instant."
   PL: „Nie jest to magia ukazująca przyszłość. To oko przypomina raczej kalkulator, który analizuje wszystko, co wpada w pole widzenia, i przewiduje ulotną chwilę, jaka ma nadejść.”
217. [Status [FutureEyeOffMirror] — nazwa] 예지안 과열
   źródło: Bufs_Mirror7.json :: dataList[id=FutureEyeOffMirror].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOffMirror]`
   limit: do 50 znaków
   EN: Eye of Precognition - Overheat
   PL: Oko Prekognicji - Przegrzanie
218. [Status [FutureEyeOffMirror] — opis] - 최댓값: 30\n- 공격 스킬로 가하는 피해량 -20%\n- 가속탄을 소모하는 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 턴 시작 시 10 증가\n- 수치가 30이면, ‘예지안’으로 변환
   źródło: Bufs_Mirror7.json :: dataList[id=FutureEyeOffMirror].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Attack Skills deal -20% damage\n- Convert all Coins on Skills that spend Acceleration Round to Unbreakable Coins\n- Turn Start: Gain 10 Stack\n- At 30 Stack, convert into "Eye of Precognition"
   PL: - Maks.: 30\n- Umiejętności ataku zadają -20% obrażeń\n- Wszystkie monety Umiejętności zużywających Pocisk Przyspieszenia stają się Niezniszczalnymi Monetami\n- Na początek tury rośnie o 10\n- Przy wartości 30 zamienia się w 'Oko Prekognicji'
219. [Status [TeachersPreyMirror] — nazwa] 사냥 표적
   źródło: Bufs_Mirror7.json :: dataList[id=TeachersPreyMirror].name
   kontekst: identyfikator statusu w tekstach: `[TeachersPreyMirror]`
   limit: do 40 znaków
   EN: Game Target
   PL: Cel Polowania
220. [Status [TeachersPreyMirror] — opis] 속도가 1로 고정되며, ‘엄지 아비 - 발렌치나’의 공격 스킬 '처분'의 메인 타겟으로 지정됨
   źródło: Bufs_Mirror7.json :: dataList[id=TeachersPreyMirror].desc
   limit: do 170 znaków
   EN: Fix this unit's Speed to 1; become the main target of the Attack Skill "Disposal" used by "The Thumb Nursefather - Valencina"
   PL: Szybkość zostaje zablokowana na wartości 1; jednostka zostaje głównym celem Umiejętności ataku 'Likwidacja' używanej przez 'Ojca Kciuka - Valencinę'
221. [Status [TeachersPreyMirror] — tekst klimatyczny] 보냐텔리 가의 표적이 되었다면 사냥은 피할 수 없다.
   źródło: Bufs_Mirror7.json :: dataList[id=TeachersPreyMirror].flavor
   limit: do 120 znaków
   EN: Prey marked by Famiglia Bognatelli will be hunted down without fail.
   PL: Kto raz stanie się celem rodu Bognatellich, nie uniknie polowania.
222. [Status [ObservationTheRingsHidden] — nazwa] 조망
   źródło: Bufs_Mirror7.json :: dataList[id=ObservationTheRingsHidden].name
   kontekst: identyfikator statusu w tekstach: `[ObservationTheRingsHidden]`
   limit: do 40 znaków
   EN: Viewing the Tableau
   PL: Podziwianie Tableau
223. [Status [ObservationTheRingsHidden] — opis] - 기본 공격 레벨 20 감소\n- 기본 방어 레벨 20 감소\n- 약지 제자가 전투 가능 상태면, 받는 최종 피해량 -70% (소수점 버림, 최솟값 없음)
   źródło: Bufs_Mirror7.json :: dataList[id=ObservationTheRingsHidden].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -20\n- Base Defense Level -20\n- Turn Start: Take -70% final damage if The Ring Apprentice has not retreated from this Encounter (rounded down; no min. value)
   PL: - Bazowy Poziom Ataku -20\n- Bazowy Poziom Obrony -20\n- Jeśli Uczeń Pierścienia może walczyć, otrzymuje -70% obrażeń końcowych (bez części dziesiętnych, bez minimum)
224. [Status [ObservationTheRingsHidden] — tekst klimatyczny] “갤러리에서 작품을 감상할 때는 느긋하고 여유롭게. 서두르지 않는 것이 중요하답니다.”
   źródło: Bufs_Mirror7.json :: dataList[id=ObservationTheRingsHidden].flavor
   limit: do 180 znaków
   EN: "The appreciation of artwork in a gallery calls for unhurried contemplation. Please remember—impatience dulls the appreciation of art."
   PL: „Podziwianie dzieł sztuki w galerii wymaga niespiesznej kontemplacji. Proszę pamiętać — niecierpliwość tępi wrażliwość na sztukę.”
225. [Status [MD7Limit101] — nazwa] 전력 재분배
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit101].name
   kontekst: identyfikator statusu w tekstach: `[MD7Limit101]`
   limit: do 40 znaków
   EN: Force Redistribution
   PL: Redystrybucja Sił
226. [Status [MD7Limit101] — opis] 사망하면 다음 턴 시작 시 모든 아군에게 공격 레벨 증가 3 부여 (턴당 최대 3회, 웨이브 포함)
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit101].desc
   limit: do 190 znaków
   EN: When killed, apply 3 Offense Level Up to all allies at the next Turn Start (3 times per turn; start of a new wave counts as Turn Start as well)
   PL: Po śmierci nadaje wszystkim sojusznikom 3 Wzrosty Poziomu Ataku na początek następnej tury (maks. 3 razy na turę; początek fali również liczy się jako początek tury)
227. [Status [MD7Limit111] — nazwa] 정신적 고양
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit111].name
   kontekst: identyfikator statusu w tekstach: `[MD7Limit111]`
   limit: do 40 znaków
   EN: Psychological Elation
   PL: Psychiczne Uniesienie
228. [Status [MD7Limit111] — opis] 턴 시작 시 모든 아군의 정신력 20 회복\n- 모든 스킬이 빼기 코인이면 대신 정신력 15 감소
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit111].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Heal 20 SP for all allies\n- If all Skills are Minus Coin Skills, lose 15 SP instead
   PL: Na początek tury wszyscy sojusznicy odzyskują 20 Poczytalności\n- Przy samych monetach Minus zamiast tego traci 15 Poczytalności
229. [Status [MD7Limit121] — nazwa] 보호막 생성
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit121].name
   kontekst: identyfikator statusu w tekstach: `[MD7Limit121]`
   limit: do 40 znaków
   EN: Shield Generation
   PL: Generowanie Tarczy
230. [Status [MD7Limit121] — opis] 보호막 3000 얻음\n(집중 전투인 경우 본체에만 적용, 이 효과로 획득한 보호막은 턴 종료시에도 사라지지 않음)
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit121].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 3000 Shield\n(In Focused Encounters, applies to Core only; Shield gained by this effect does not expire at Turn End)
   PL: Zyskuje 3000 Tarczy\n(W walkach skupionych dotyczy wyłącznie Rdzenia; Tarcza zdobyta dzięki temu efektowi nie znika na koniec tury)
231. [Status [MD7Limit131] — nazwa] 균열 증식
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit131].name
   kontekst: identyfikator statusu w tekstach: `[MD7Limit131]`
   limit: do 40 znaków
   EN: Fracture Proliferation
   PL: Rozprzestrzenianie Pęknięć
232. [Status [MD7Limit131] — opis] 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠의 부여량 2배로 증가
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit131].desc
   limit: do 120 znaków
   EN: Skills inflict x2 Burn, Bleed, Tremor, Rupture, and Sinking
   PL: Umiejętności nakładają 2x Podpalenie, Krwawienie, Wstrząs, Rozdarcie i Zatonięcie
233. [Status [MD7Limit141] — nazwa] 상태이상 부여
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit141].name
   kontekst: identyfikator statusu w tekstach: `[MD7Limit141]`
   limit: do 40 znaków
   EN: Inflict Status Effect
   PL: Nakładanie Stanów
234. [Status [MD7Limit141] — opis] 턴 시작 시 모든 아군(인격)에게 화상, 출혈, 진동, 파열, 침잠 중 무작위 1개 효과의 위력 5 부여
   źródło: Bufs_Mirror7.json :: dataList[id=MD7Limit141].desc
   limit: do 170 znaków
   EN: Turn Start: Inflict 5 Potency of a random status, chosen from Burn, Bleed, Tremor, Rupture, and Sinking, on all allies(Identities)
   PL: Na początek tury nakłada na wszystkich sojuszników (tożsamości) 5 Mocy losowego efektu z puli: Podpalenie, Krwawienie, Wstrząs, Rozdarcie i Zatonięcie
235. [Status [RingFingerPhysical] — nazwa] 육체미
   źródło: Bufs_Mirror7.json :: dataList[id=RingFingerPhysical].name
   kontekst: identyfikator statusu w tekstach: `[RingFingerPhysical]`
   limit: do 40 znaków
   EN: Beauty of the Physique
   PL: Piękno Ciała
236. [Status [RingFingerPhysical] — opis] - 출혈을 20 이상 보유하고 있는 적에게 사용하는 기본 스킬의 코인 위력 +1, 가하는 피해량 +20% (가중치가 2 이상인 스킬일 경우, 모든 타겟의 출혈의 합으로 계산)\n- 특수 충전을 소모하는 기본 스킬의 코인 위력 +1 (E.G.O 스킬 제외)\n- 턴 종료시 소멸
   źródło: Bufs_Mirror7.json :: dataList[id=RingFingerPhysical].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Against enemies that have 20+ Bleed, Base Skills gain Coin Power +1 and deal +20% damage (calculated as the sum of Bleed on all targets for Skills that have 2+ Atk Weight)\n- Base Skills that consume 'Unique Charge' gain Coin Power +1 (excluding E.G.O Skills)\n- Turn End: This effect expires
   PL: - Umiejętności podstawowe używane przeciwko wrogom posiadającym 20+ Krwawienia zyskują Moc Monet +1 i zadają +20% obrażeń (dla Umiejętności o Wadze 2+ obliczane jako suma Krwawień wszystkich celów)\n- Umiejętności podstawowe zużywające Szczególne Ładowanie zyskują Moc Monet +1 (z wyłączeniem Umiejętności E.G.O)\n- Znika na koniec tury
237. [Status [RingFingerFauvism] — nazwa] 야성미
   źródło: Bufs_Mirror7.json :: dataList[id=RingFingerFauvism].name
   kontekst: identyfikator statusu w tekstach: `[RingFingerFauvism]`
   limit: do 40 znaków
   EN: Charm of the Beastly
   PL: Urok Dzikości
238. [Status [RingFingerFauvism] — opis] - 출혈을 20 이상 보유하고 있는 적에게 사용하는 기본 스킬의 코인 위력 +1, 가하는 피해량 +20% (가중치가 2 이상인 스킬일 경우, 모든 타겟의 출혈의 합으로 계산)\n- 공격 시작 시, 대상의 정신력이 15 이하이거나, 침잠 위력이 20 이상이면, 다음 턴에 타격 위력 증가 1 얻음 (턴당 1회)\n- 턴 종료시 소멸
   źródło: Bufs_Mirror7.json :: dataList[id=RingFingerFauvism].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Against enemies that have 20+ Bleed, Base Skills gain Coin Power +1 and deal +20% damage (calculated as the sum of Bleed on all targets for Skills that have 2+ Atk Weight)\n- On Attack Start, if target has 15- SP or 20+ Sinking Potency, gain 1 Blunt Power Up next turn (once per turn)\n- Turn End: This effect expires
   PL: - Umiejętności podstawowe używane przeciwko wrogom posiadającym 20+ Krwawienia zyskują Moc Monet +1 i zadają +20% obrażeń (dla Umiejętności o Wadze 2+ obliczane jako suma Krwawień wszystkich celów)\n- Na początku ataku, jeśli Poczytalność celu wynosi 15 lub mniej albo Moc Zatonięcia celu wynosi 20 lub więcej, w następnej turze zyskuje 1 Wzrost Mocy Trafienia (raz na turę)\n- Znika na koniec tury
239. [Status [KAmpouleMirror] — nazwa] 비상용 K사 앰플
   źródło: Bufs_Mirror7.json :: dataList[id=KAmpouleMirror].name
   kontekst: identyfikator statusu w tekstach: `[KAmpouleMirror]`
   limit: do 40 znaków
   EN: K Corp. Emergency Ampule
   PL: Awaryjna Ampułka K Corp.
240. [Status [KAmpouleMirror] — opis] 자신의 체력이 0이 되는 피해를 받으면, 아래 효과 발동\n- 흐트러짐 상태면, 흐트러짐 상태 해제\n- 체력 전부 회복\n- 이 효과는 인격/EGO 패시브로 체력이 1 미만으로 감소하지 않는 효과보다 우선적으로 발동함\n-  효과 발동시 소멸
   źródło: Bufs_Mirror7.json :: dataList[id=KAmpouleMirror].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Activate the following effects upon taking damage that would reduce this unit's HP to 0:\n- If Staggered, recover from Stagger\n- Fully heal HP\n- This effect activates before the "X does not reduce HP below 1" effects from Identities & E.G.O Passives\n- Expires after activation
   PL: Po otrzymaniu obrażeń, które obniżyłyby HP do 0, uruchamia następujące efekty:\n- Jeśli znajduje się w stanie Oszołomienia, znosi Oszołomienie\n- W pełni odzyskuje HP\n- Ten efekt uruchamia się przed efektami pasywów Tożsamości/E.G.O, które zapobiegają spadnięciu HP poniżej 1\n- Znika po uruchomieniu efektu
241. [Status [PlayingWithWaterTogetherMirror] — nazwa] 찰박찰박
   źródło: Bufs_Mirror7.json :: dataList[id=PlayingWithWaterTogetherMirror].name
   kontekst: identyfikator statusu w tekstach: `[PlayingWithWaterTogetherMirror]`
   limit: do 40 znaków
   EN: Splish Splash
   PL: Chlup-Chlap
242. [Status [PlayingWithWaterTogetherMirror] — opis] - 최댓값: 10\n- 단수어와 합 진행 시 아래 효과 적용 (스킬당 1회)\n  · 침잠을 수치만큼 얻고 줌\n  · 정신력 수치만큼 오름\n- 최댓값이면, 단수어를 타겟으로 하는 스킬의 피해량 +50%
   źródło: Bufs_Mirror7.json :: dataList[id=PlayingWithWaterTogetherMirror].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- In a Clash against Headless Ichthys, gain the following effects (once per Skill):\n  · Gain and inflict Sinking equal to Stack\n  · Heal SP equal to Stack\n- At max Stack, Skills targeting Headless Ichthys deal +50% damage
   PL: - Maks.: 10\n- W Starciu z Bezgłowym Ichtisem stosuje poniższe efekty (raz na Umiejętność)\n  · Zyskuje Zatonięcie równe wartości i przekazuje je\n  · Odzyskuje Poczytalność równą wartości\n- Przy maksymalnej wartości Umiejętności wymierzone w Bezgłowego Ichtisa zadają +50% obrażeń
243. [Status [RedButterfly] — nazwa] 찢겨나온나비
   źródło: Bufs_Mirror7.json :: dataList[id=RedButterfly].name
   kontekst: identyfikator statusu w tekstach: `[RedButterfly]`
   limit: do 40 znaków
   EN: Torn-out Butterfly
   PL: Wyrwany Motyl
244. [Status [RedButterfly] — opis] - 모든 스킬의 최종 위력 +2\n- 피해로 인해 흐트러짐 상태가 되면, 즉시 흐트러짐 상태를 해제하고 최대 체력의 100% 만큼 보호막을 얻음 (턴당 1회, 강제 흐트러짐 제외)
   źródło: Bufs_Mirror7.json :: dataList[id=RedButterfly].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +2 for all Skills\n- When Staggered due to damage, immediately recover from Stagger and gain Shield equal to 100% HP (once per turn, excluding forced Staggers)
   PL: - Moc Końcowa wszystkich Umiejętności +2\n- Gdy wskutek obrażeń popada w stan Oszołomienia, natychmiast znosi Oszołomienie i zyskuje Tarczę równą 100% Maks. HP (raz na turę, z wyłączeniem wymuszonego Oszołomienia)

## Statusy i efekty bojowe — Bufs_Mirror8
- plik gry: `Bufs_Mirror8.json`

245. [Status [SoundOfStorm] — nazwa] 우레
   źródło: Bufs_Mirror8.json :: dataList[id=SoundOfStorm].name
   kontekst: identyfikator statusu w tekstach: `[SoundOfStorm]`
   limit: do 40 znaków
   EN: Thundercrack
   PL: Grzmot
246. [Status [SoundOfStorm] — opis] 최댓값: 3\n- 수치 1당 코인 위력 +1, 적에게 가하는 기본 스킬 피해량 +15%\n- 와일드헌트 히스클리프가 퇴각 및 사망했으면, 소멸
   źródło: Bufs_Mirror8.json :: dataList[id=SoundOfStorm].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- For every Stack:\n  · Coin Power +1\n  · Base Skills deal +15% damage against enemies\n- If Wild Hunt Heathcliff has been defeated or Retreated, expires
   PL: Maks.: 3\n- Za każdą wartość Moc Monet +1, Umiejętności podstawowe zadają wrogom +15% obrażeń\n- Znika, gdy Heathcliff Dzikiego Gonu wycofa się lub zginie

## Statusy i efekty bojowe — Bufs_Refraction2
- plik gry: `Bufs_Refraction2.json`

247. [Status [TipsinessRail] — nazwa] 취기
   źródło: Bufs_Refraction2.json :: dataList[id=TipsinessRail].name
   kontekst: identyfikator statusu w tekstach: `[TipsinessRail]`
   limit: do 40 znaków
   EN: Tipsy
   PL: Upojenie
248. [Status [TipsinessRail] — opis] 합 위력 -{0} (최대 5)
   źródło: Bufs_Refraction2.json :: dataList[id=TipsinessRail].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clash Power -{0} (max 5)
   PL: Moc Starcia -{0} (maks. 5)
249. [Status [TipsinessRail] — podsumowanie] 합 위력이 수치만큼 감소
   źródło: Bufs_Refraction2.json :: dataList[id=TipsinessRail].summary
   limit: do 120 znaków
   EN: Lose Clash Power equal to Stack
   PL: Moc Starcia maleje o wartość
250. [Status [PassedPortal_Red] — nazwa] 피가 흐르는 차원
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Red].name
   kontekst: identyfikator statusu w tekstach: `[PassedPortal_Red]`
   limit: do 40 znaków
   EN: Hemorrhaging Dimension
   PL: Krwawiący Wymiar
251. [Status [PassedPortal_Red] — opis] 차원을 통과해 피해량 증가 +{0}0%
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Red].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pass through the Dimensional Rift to deal +{0}0% damage
   PL: Przejście przez Szczelinę Wymiarową: +{0}0% obrażeń
252. [Status [PassedPortal_Green] — nazwa] 독이 들끓는 차원
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Green].name
   kontekst: identyfikator statusu w tekstach: `[PassedPortal_Green]`
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL: Wymiar Wrzącej Trucizny
253. [Status [PassedPortal_Green] — opis] 차원을 통과해 수치당 최대 체력 증가 20%
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Green].desc
   limit: do 120 znaków
   EN: Pass through the Dimensional Rift to gain +20% max HP
   PL: Przejście przez Szczelinę Wymiarową: Maks. HP +20% za każdą wartość
254. [Status [PassedPortal_Yellow] — nazwa] 끊임없이 진동하는 차원
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Yellow].name
   kontekst: identyfikator statusu w tekstach: `[PassedPortal_Yellow]`
   limit: do 40 znaków
   EN: Tremoring Dimension
   PL: Nieustannie Wstrząsany Wymiar
255. [Status [PassedPortal_Yellow] — opis] 차원을 통과해 속도 {0} 증가
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Yellow].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pass through the Dimensional Rift to gain {0} Speed
   PL: Przejście przez Szczelinę Wymiarową: +{0} Szybkości
256. [Status [PassedPortal_Blue] — nazwa] 전류를 뿜어내는 차원
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Blue].name
   kontekst: identyfikator statusu w tekstach: `[PassedPortal_Blue]`
   limit: do 40 znaków
   EN: Electrifying Dimension
   PL: Wymiar Emitujący Prąd
257. [Status [PassedPortal_Blue] — opis] 차원을 통과해 코인 위력 +{0}
   źródło: Bufs_Refraction2.json :: dataList[id=PassedPortal_Blue].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pass through the Dimensional Rift to gain Coin Power +{0}
   PL: Przejście przez Szczelinę Wymiarową: +{0} Mocy Monet
258. [Status [FairyCharm] — nazwa] 매혹
   źródło: Bufs_Refraction2.json :: dataList[id=FairyCharm].name
   kontekst: identyfikator statusu w tekstach: `[FairyCharm]`
   limit: do 40 znaków
   EN: Charmed
   PL: Oczarowanie
259. [Status [FairyCharm] — opis] - 요정에 가하는 피해가 0이 됨.\n- 요정이 죽으면 해제됨.
   źródło: Bufs_Refraction2.json :: dataList[id=FairyCharm].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All damage dealt to Fairy reduced to 0\n- Expires when Fairy dies
   PL: - Obrażenia zadawane Wróżce wynoszą 0\n- Efekt znika, gdy Wróżka zginie
260. [Status [FairyCharm] — podsumowanie] 피해가 0이 됨
   źródło: Bufs_Refraction2.json :: dataList[id=FairyCharm].summary
   limit: do 120 znaków
   EN: Damage fixed to 0
   PL: Obrażenia wynoszą 0
261. [Status [DecoyRegenerated] — nazwa] 재생
   źródło: Bufs_Refraction2.json :: dataList[id=DecoyRegenerated].name
   kontekst: identyfikator statusu w tekstach: `[DecoyRegenerated]`
   limit: do 40 znaków
   EN: Regenerate
   PL: Regeneracja
262. [Status [DecoyRegenerated] — opis] 부위가 재생될 때마다 매혹 인원 수 +1
   źródło: Bufs_Refraction2.json :: dataList[id=DecoyRegenerated].desc
   limit: do 120 znaków
   EN: Number of Charmed Units +1 every time a Part is restored
   PL: Liczba jednostek pod Zauroczeniem +1 za każde przywrócenie części
263. [Status [WaveFoxUmbrella] — nazwa] 보호 우산
   źródło: Bufs_Refraction2.json :: dataList[id=WaveFoxUmbrella].name
   kontekst: identyfikator statusu w tekstach: `[WaveFoxUmbrella]`
   limit: do 40 znaków
   EN: Protection Umbrella
   PL: Ochronny Parasol
264. [Status [WaveFoxUmbrella] — opis] 모든 부위에 {0}만큼 보호 얻음\n기다림 스킬을 사용할 때, 낡은 우산을 {0} 소환\n우산 파괴 시 1씩 소모됨.
   źródło: Bufs_Refraction2.json :: dataList[id=WaveFoxUmbrella].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: All Parts gain Protection equal to {0}\nWhen using the "Waiting" Skill, spawn {0} Old Umbrella\n1 Spent every time an Umbrella is broken
   PL: Wszystkie części zyskują Ochronę równą {0}\nPrzy użyciu Umiejętności 'Oczekiwanie' przywołuje Stary Parasol w liczbie {0}\nPrzy zniszczeniu parasola zużywa 1
265. [Status [InterlockingTime_Re] — nazwa] 맞물리는 시간
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTime_Re].name
   kontekst: identyfikator statusu w tekstach: `[InterlockingTime_Re]`
   limit: do 40 znaków
   EN: Interlocking Time
   PL: Przeplatający się Czas
266. [Status [InterlockingTime_Re] — opis] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 2배만큼 고정 피해를 입음. 다음 턴에 수치만큼 속박 얻음.
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTime_Re].desc
   limit: do 190 znaków
   EN: Reduce final damage by 30% and store it. At 3 Stacks, take fixed damage equal to 2 times the accumulated damage. Gain Bind next turn equal to Stack
   PL: Zmalekuje o 30% obrażeń końcowych i zapisuje je. Gdy wartość osiągnie 3, otrzymuje stałe obrażenia równe dwukrotności zapisanych obrażeń. W następnej turze zyskuje Spętanie równe wartości.
267. [Status [InterlockingTime_Re] — podsumowanie] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 2배만큼 고정 피해를 입음. 다음 턴에 수치만큼 속박 얻음.
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTime_Re].summary
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Status [TimeRental_Re] — nazwa] 시간 대여
   źródło: Bufs_Refraction2.json :: dataList[id=TimeRental_Re].name
   kontekst: identyfikator statusu w tekstach: `[TimeRental_Re]`
   limit: do 40 znaków
   EN: Borrowed Time
   PL: Pożyczony Czas
269. [Status [TimeRental_Re] — opis] 턴 종료 시 신속 3, 피해량 증가 2, 공격 레벨 증가 2 얻음.\n턴 종료 시 수치가 1 남았다면, 다음 턴에 속박 3, 공격 위력 감소 1, 취약 2 얻음\n턴 종료 시 1 감소
   źródło: Bufs_Refraction2.json :: dataList[id=TimeRental_Re].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End:\n- Gain 3 Haste, 2 Damage Up, and 2 Offense Level Up\n- If only 1 Stack remains, gain 3 Bind, 1 Attack Power Down, and 2 Fragile next turn\n- Lose 1 Stack
   PL: Na koniec tury: 3 Pośpiechu, 2 Wzrosty Obrażeń i 2 Wzrosty Poziomu Ataku\nJeśli na koniec tury zostaje 1 wartość, w następnej turze zyskuje 3 Spętań, 1 Spadek Mocy Ataku i 2 Wrażliwości\nNa koniec tury maleje o 1
270. [Status [TimeRental_Re] — podsumowanie] -
   źródło: Bufs_Refraction2.json :: dataList[id=TimeRental_Re].summary
   limit: do 120 znaków
   EN: -
   PL: -
271. [Status [ReattachedCurseTag_Re] — nazwa] 다시 붙여진 저주 부적
   źródło: Bufs_Refraction2.json :: dataList[id=ReattachedCurseTag_Re].name
   kontekst: identyfikator statusu w tekstach: `[ReattachedCurseTag_Re]`
   limit: do 40 znaków
   EN: Reattached Curse Talisman
   PL: Ponownie Naklejony Talizman Klątwy
272. [Status [ReattachedCurseTag_Re] — opis] - 최댓값: 12\n- 8 이하이면, 가하는 피해량 +30%\n- 9 이상이면, 턴 시작 시 속박 5 얻음\n- 12면, 턴 시작 시 공격 위력 감소 5 얻음
   źródło: Bufs_Refraction2.json :: dataList[id=ReattachedCurseTag_Re].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 12\n- At 8- Stacks, deal +30% damage\n- At 9+ Stacks, gain 5 Bind at Turn Start\n- At 12 Stacks, gain 5 Attack Power Down at Turn Start
   PL: - Maks.: 12\n- Przy 8 lub mniej zadaje +30% obrażeń\n- Przy 9 lub więcej na początek tury zyskuje 5 Spętań\n- Przy 12 na początek tury zyskuje 5 Spadku Mocy Ataku
273. [Status [ReattachedCurseTag_Re] — podsumowanie] 수치가 9이상이라면, 턴 시작 시 속박 5 얻음.\n12이상이라면, 턴 시작 시 공격 위력 감소 5 얻음.
   źródło: Bufs_Refraction2.json :: dataList[id=ReattachedCurseTag_Re].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 9+, gain 5 Bind at Turn Start\nAt 12+, gain 5 Attack Power Down at Turn Start
   PL: Przy 9 lub więcej na początek tury zyskuje 5 Spętań.\nPrzy 12 lub więcej na początek tury zyskuje 5 Spadku Mocy Ataku.
274. [Status [WrappedCurseTagRe] — nazwa] 얽혀온 저주 부적
   źródło: Bufs_Refraction2.json :: dataList[id=WrappedCurseTagRe].name
   kontekst: identyfikator statusu w tekstach: `[WrappedCurseTagRe]`
   limit: do 40 znaków
   EN: Entangled Curse Talisman
   PL: Przepleciony Talizman Klątwy
275. [Status [WrappedCurseTagRe] — opis] - 최댓값: 9\n- 가하는 피해량 수치당 1% 증가\n- 수치가 9면, 턴 시작 시 공격 위력 감소 2 얻음\n해당 웨이브 종료 시, 제거
   źródło: Bufs_Refraction2.json :: dataList[id=WrappedCurseTagRe].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- Deal +1% damage for every Stack\n- At 9 Stacks, gain 2 Attack Power Down at Turn Start\nRemove this effect at the end of the wave
   PL: - Maks.: 9\n- Zadawane Obrażenia +1% za każdą wartość\n- Przy wartości 9 na początek tury zyskuje 2 Spadki Mocy Ataku\nZnika po zakończeniu tej fali
276. [Status [WrappedCurseTagRe] — podsumowanie] 가하는 피해량 수치당 1%, 9면, 턴 시작 시 공격 위력 감소 2 얻음
   źródło: Bufs_Refraction2.json :: dataList[id=WrappedCurseTagRe].summary
   limit: do 120 znaków
   EN: Deal +1% damage per Stack; at 9 Stacks, gain 2 Attack Power Down at Turn Start
   PL: Zadawane Obrażenia +1% za każdą wartość; przy wartości 9 na początek tury zyskuje 2 Spadki Mocy Ataku
277. [Status [AccumulatedPast] — nazwa] 축적된 과거
   źródło: Bufs_Refraction2.json :: dataList[id=AccumulatedPast].name
   kontekst: identyfikator statusu w tekstach: `[AccumulatedPast]`
   limit: do 40 znaków
   EN: Accumulated Past
   PL: Zakumulowana Przeszłość
278. [Status [AccumulatedPast] — opis] 거울굴절철도 누적 턴 수가 표시되어있다.\n턴 종료 시, 1씩 증가함.\n몸통 부위 파괴 시, 전부 소모됨.
   źródło: Bufs_Refraction2.json :: dataList[id=AccumulatedPast].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This displays the Total Turns taken in the Refraction Railway\nThe number goes up by 1 at the end of the turn\nSpent completely when Body is broken
   PL: Wyświetla łączną liczbę tur na Lustrzanej Kolei Załamania.\nNa koniec tury rośnie o 1.\nPrzy zniszczeniu części Tułowia zużywana jest całkowicie.
279. [Status [PrepareSinRose] — nazwa] 면류관
   źródło: Bufs_Refraction2.json :: dataList[id=PrepareSinRose].name
   kontekst: identyfikator statusu w tekstach: `[PrepareSinRose]`
   limit: do 40 znaków
   EN: Crown of Thorns
   PL: Korona z Róż
280. [Status [PrepareSinRose] — opis] 이 효과가 부여된 대상이 가장 많이 보유한 스킬의 속성을 가진 장미 유닛이 생성됨\n- 해당 효과로 장미가 7개 초과되면, 초과된 수치만큼 사망한 수감자와 연결된 장미 제거 (사망으로 처리되지 않음)
   źródło: Bufs_Refraction2.json :: dataList[id=PrepareSinRose].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Generates a Rose unit whose Affinity corresponds to the most-owned Skill Affinity of the target inflicted with this effect\n- If this effect causes the number of Rose units on the field to exceed 7, remove Rose units that are bound with defeated Sinners equal to the excess amount (does not count as death)
   PL: Tworzy jednostkę-Różę o atrybucie Umiejętności, którego cel objęty tym efektem posiada najwięcej\n- Jeśli dzięki temu efektowi liczba Róż przekroczy 7, usuwa Róże połączone ze zmarłymi Sinnersami w liczbie przekroczenia (nie liczy się jako śmierć)
281. [Status [BloomingRose] — nazwa] 피어나는 죄
   źródło: Bufs_Refraction2.json :: dataList[id=BloomingRose].name
   kontekst: identyfikator statusu w tekstach: `[BloomingRose]`
   limit: do 40 znaków
   EN: Blooming Sin
   PL: Rozkwitający Grzech
282. [Status [BloomingRose] — opis] 턴 종료 시\n-수치 1 증가.\n-{2} 체력이 최대 체력의 25%만큼 감소.\n-{1} E.G.O 자원이 10% 감소 (소수점 버림).\n- 장미 표지판의 본체 최대 체력의 5%만큼 본체 체력 회복.\n\n수치가 4가 되면,\n- {2} 사망.\n- {1} E.G.O 자원 수량이 0이 됨.
   źródło: Bufs_Refraction2.json :: dataList[id=BloomingRose].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: {2}, {1}, \n
   EN: Turn End:\n- Gain 1 Stack\n- {2} loses HP equal to 25% of max HP\n- Lose 10% of {1} E.G.O Resource (rounded down)\n- The Sign of Roses's Core heals HP equal to 5% of the Core's max HP\n\nAt 4 Stacks,\n- {2} dies\n- Lose all of {1} E.G.O Resource
   PL: Na koniec tury:\n- zyskuje 1 stos\n- {2} traci HP równe 25% Maks. HP\n- zasoby E.G.O {1} maleją o 10% (zaokrąglone w dół)\n- Rdzeń Znaku Róż odzyskuje HP równe 5% Maks. HP Rdzenia\n\nPrzy 4 stosach:\n- {2} ginie\n- zasoby E.G.O {1} spadają do 0
283. [Status [EatingSin] — nazwa] 머금은 죄
   źródło: Bufs_Refraction2.json :: dataList[id=EatingSin].name
   kontekst: identyfikator statusu w tekstach: `[EatingSin]`
   limit: do 40 znaków
   EN: Drenched Sin
   PL: Nasiąknięty Grzech
284. [Status [EatingSin] — opis] 최대 체력이 {0}%(감소시킨 E.G.O 자원 수)만큼 증가.\n\n사망 시\n- {1} E.G.O 자원 {0}개가 복구됨.\n- {2} 체력을 (인격 최대 체력의 25% x 사망 시 피어나는 죄 스택)만큼 회복.
   źródło: Bufs_Refraction2.json :: dataList[id=EatingSin].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: Gain Max HP by {0}%(E.G.O resource drained).\n\nOn Death\n- Regain {0} of {1} E.G.O resource.\n- {2} heals HP by (25% of Identity's Max HP x Blooming Sin Stack at death).
   PL: Zyskuje Maks. HP równe {0}% (osuszone zasoby E.G.O)\n\nPo śmierci:\n- przywraca {0} zasobów E.G.O {1}\n- {2} odzyskuje HP równe (25% Maks. HP Tożsamości x stosów Kwitnącego Grzechu w momencie śmierci)
285. [Status [EnhanceRose] — nazwa] 강화 상태
   źródło: Bufs_Refraction2.json :: dataList[id=EnhanceRose].name
   kontekst: identyfikator statusu w tekstach: `[EnhanceRose]`
   limit: do 40 znaków
   EN: Power-up State
   PL: Stan Wzmocnienia
286. [Status [EnhanceRose] — opis] 강화 상태 패시브가 발동됨
   źródło: Bufs_Refraction2.json :: dataList[id=EnhanceRose].desc
   limit: do 120 znaków
   EN: Power-up State passive activated
   PL: Aktywuje się pasyw Stanu Wzmocnienia
287. [Status [RailLine2Buff] — nazwa] 거울 굴절
   źródło: Bufs_Refraction2.json :: dataList[id=RailLine2Buff].name
   kontekst: identyfikator statusu w tekstach: `[RailLine2Buff]`
   limit: do 40 znaków
   EN: Mirror Refraction
   PL: Załamanie Lustra
288. [Status [FullBloomRose] — nazwa] 피워낸 장미
   źródło: Bufs_Refraction2.json :: dataList[id=FullBloomRose].name
   kontekst: identyfikator statusu w tekstach: `[FullBloomRose]`
   limit: do 40 znaków
   EN: Bloomed Rose
   PL: Rozkwitnięta Róża
289. [Status [KalpaVine] — nazwa] 억겁의 덩굴
   źródło: Bufs_Refraction2.json :: dataList[id=KalpaVine].name
   kontekst: identyfikator statusu w tekstach: `[KalpaVine]`
   limit: do 40 znaków
   EN: Brambles of Eternity
   PL: Ciernie Wieczności
290. [Status [KalpaVine] — opis] 모든 캐릭터 가하는 피해량 -{0}0%\n모든 캐릭터 받는 피해량 -{0}0%
   źródło: Bufs_Refraction2.json :: dataList[id=KalpaVine].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: All characters deal -{0}0% damage\nAll characters receive -{0}0% damage
   PL: Wszystkie postacie zadają -{0}0% obrażeń\nWszystkie postacie otrzymują -{0}0% obrażeń
291. [Status [InterlockingTimeBokGak] — nazwa] 맞물리는 시간
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTimeBokGak].name
   kontekst: identyfikator statusu w tekstach: `[InterlockingTimeBokGak]`
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Status [InterlockingTimeBokGak] — opis] - 최종 피해의 30%만큼 감소 및 저장\n- 수치가 3이 되면, 쌓인 피해량의 2배만큼 고정 피해를 입고 효과 소멸\n- 턴 종료 시 수치만큼 다음 턴에 속박 얻음\n- 굴절된 T사 징수직 3등급 직원이 등장하지 않는 웨이브일 경우, 제거
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTimeBokGak].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Reduce final damage by 30% and store it\n- At 3 Stacks, take fixed damage equal to 2 times the accumulated damage and remove this effect\n- Turn End: Gain Bind next turn equal to Stack\n- Remove this effect in waves that do not feature Refracted T Corp. Class 3 Collector
   PL: - Zmalekuje o 30% obrażeń końcowych i zapisuje je\n- Gdy wartość osiągnie 3, otrzymuje stałe obrażenia równe dwukrotności zakumulowanych obrażeń, a efekt znika\n- Na koniec tury zyskuje w następnej turze Spętanie równe wartości\n- Znika, jeśli w fali nie pojawia się załamany pracownik poboru T Corp. 3. klasy
293. [Status [InterlockingTimeBokGak] — podsumowanie] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 2배만큼 고정 피해를 입음. 다음 턴에 속박 수치만큼 얻음.
   źródło: Bufs_Refraction2.json :: dataList[id=InterlockingTimeBokGak].summary
   limit: do 190 znaków
   EN: Reduce final damage by 30% and store it. At 3 Stacks, take fixed damage equal to 2 times the accumulated damage. Gain Bind next turn equal to Stack
   PL: Zmalekuje o 30% obrażeń końcowych i zapisuje je. Gdy wartość osiągnie 3, otrzymuje stałe obrażenia równe dwukrotności zapisanych obrażeń. W następnej turze zyskuje Spętanie równe wartości.

## Statusy i efekty bojowe — Bufs_Refraction3
- plik gry: `Bufs_Refraction3.json`

294. [Status [MRcAfBa] — nazwa] 목화
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBa].name
   kontekst: identyfikator statusu w tekstach: `[MRcAfBa]`
   limit: do 40 znaków
   EN: Gossypium
   PL: Bawełna
295. [Status [MRcAfBa] — opis] 머금은 목화가 붉게 물든 목화 상태일 때, 턴 종료 시 목화 수치의 절반만큼 출혈 얻음, 출혈 횟수 증가
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBa].desc
   limit: do 160 znaków
   EN: When the Drenched Gossypium is in a Red-stained Gossypium state, gain (Gossypium value/2) Bleed and Bleed Count at Turn End
   PL: Gdy Nasiąknięta Bawełna znajduje się w stanie Czerwono Ubarwionej Bawełny, na koniec tury zyskuje Krwawienie równe połowie wartości Bawełny i Licznik Krwawienia
296. [Status [MRcAfBa] — podsumowanie] 턴 종료 시 목화 수치의 절반만큼 출혈 얻음, 출혈 횟수 증가
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBa].summary
   limit: do 120 znaków
   EN: Turn End: Gain (Gossypium value/2) Bleed and Bleed Count
   PL: Na koniec tury zyskuje Krwawienie równe połowie wartości Bawełny i Licznik Krwawienia
297. [Status [MRcAfBb] — nazwa] 붉게 물든 목화
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBb].name
   kontekst: identyfikator statusu w tekstach: `[MRcAfBb]`
   limit: do 40 znaków
   EN: Red-stained Gossypium
   PL: Czerwono Ubarwiona Bawełna
298. [Status [MRcAfBb] — opis] 턴 시작 시 공격 스킬로 부여하는 출혈, 출혈 횟수가 2배가 됨.\n대상에게 목화가 있을 때, 목화 수 절반만큼 합 위력 증가
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBb].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Double the Bleed and Bleed Count applied by Attack Skills.\nIf the target has Gossypium, gain Clash Power +(Gossypium value/2)
   PL: Na początek tury Krwawienie i Licznik Krwawienia nadawane przez Umiejętności ataku podwajają się.\nGdy cel posiada Bawełnę, Moc Starcia rośnie o połowę wartości Bawełny
299. [Status [MRcAfBb] — podsumowanie] 목화 수 절반만큼 합 위력 증가
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAfBb].summary
   limit: do 120 znaków
   EN: Gain Clash Power +(Gossypium value/2)
   PL: Moc Starcia rośnie o połowę wartości Bawełny
300. [Status [MRcAiBa] — nazwa] 불씨
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBa].name
   kontekst: identyfikator statusu w tekstach: `[MRcAiBa]`
   limit: do 40 znaków
   EN: Ember
   PL: Ognik
301. [Status [MRcAiBa] — opis] 최대 5\n불씨를 얻게되면, 분노 속성이 아닌 스킬이 {0}만큼 분노 속성이 됨.\n날개 부위 파괴 시, 마지막 공격자에게 자신의 불씨만큼 아른거리는 불씨 부여. 자신의 불씨 소멸
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBa].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Max 5\nUpon gaining Ember, convert {0} non-Wrath Affinity Skills into Wrath Affinity Skills.\nWhen the Wings Part is broken, inflict Shimmering Ember equal to the value of Ember upon the last attacker; then, all Ember on self expires.
   PL: Maks. 5\nPo uzyskaniu Ognika Umiejętności nieposiadające atrybutu Gniewu, w liczbie równej {0}, zyskują atrybut Gniewu.\nPrzy zniszczeniu części Skrzydła ostatni atakujący zyskuje Drgający Ognik równy posiadanej wartości Ognika. Posiadany Ognik znika.
302. [Status [MRcAiBb] — nazwa] 아른거리는 불씨
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBb].name
   kontekst: identyfikator statusu w tekstach: `[MRcAiBb]`
   limit: do 40 znaków
   EN: Shimmering Ember
   PL: Drgający Ognik
303. [Status [MRcAiBb] — opis] 최대 5\n특정 스킬에 피격 시 점화를 얻음. 아른거리는 불씨는 소멸됨.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBb].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max 5\nGain Spark when hit by a certain Skill. All Shimmering Ember expires.
   PL: Maks. 5\nPo otrzymaniu trafienia określoną Umiejętnością zyskuje Iskrę. Drgający Ognik znika.
304. [Status [MRcAiBc] — nazwa] 점화
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBc].name
   kontekst: identyfikator statusu w tekstach: `[MRcAiBc]`
   limit: do 40 znaków
   EN: Spark
   PL: Iskra
305. [Status [MRcAiBc] — opis] 전투 시작 시 속도 기준으로 양 옆의 인격에게 자신의 화상만큼 화상 부여.\n점화가 있을 때는 불씨를 얻을 수 없음.\n턴 종료 시 1 감소
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAiBc].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Combat Start: inflict Burn equal to Burn on self against 2 adjacent(based on Speed) units.\nCannot gain Ember when this unit has Spark.\nTurn End: reduce the value by 1
   PL: Na początku walki nakłada na sąsiednie Tożsamości (po obu stronach, według Szybkości) Podpalenie równe posiadanemu Podpaleniu.\nPrzy posiadaniu Iskry nie może zyskać Ognika.\nNa koniec tury maleje o 1
306. [Status [MRcAmBa] — nazwa] 경멸
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBa].name
   kontekst: identyfikator statusu w tekstach: `[MRcAmBa]`
   limit: do 40 znaków
   EN: Contempt
   PL: Pogarda
307. [Status [MRcAmBa] — opis] 턴 종료 시 선택한 스킬 속성의 E.G.O 자원 3 감소.\n턴 종료 시 다음 턴에 피해량 감소 3 얻음.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBa].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 3 E.G.O Resource of the Affinity corresponding to the selected Skill Affinity.\nTurn End: Gain 3 Damage Down next turn.
   PL: Na koniec tury traci 3 zasobów E.G.O o atrybucie wybranej Umiejętności.\nNa koniec tury zyskuje w następnej turze 3 Spadki Obrażeń.
308. [Status [MRcAmBb] — nazwa] 손아귀
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBb].name
   kontekst: identyfikator statusu w tekstach: `[MRcAmBb]`
   limit: do 40 znaków
   EN: Grasp
   PL: Uchwyt
309. [Status [MRcAmBb] — opis] 최대 3\n행동 불가 상태가 됨\n턴 종료 시 2이하라면, 대상의 최대 체력 절반만큼 피해를 줌. 경멸의 나선 모든 부위를 피해만큼 회복시킴.\n턴 종료 시 1 감소.\n이 피해로 체력이 0이 되면, 체력 회복이 불가능함.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBb].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max 3\nCannot act\nTurn End: at 2- value, deal damage equal to half of the target's Max HP. Then, all Parts of Spiral of Contempt heals the same amount of HP as the damage dealt by this effect.\nTurn End: reduce the value by 1.\nIf this effect brings the target's HP down to 0, the target can no longer be healed.
   PL: Maks. 3\nJednostka nie może działać\nNa koniec tury, przy wartości 2 lub mniej, zadaje obrażenia równe połowie Maks. HP celu; wszystkie części Spirali Pogardy odzyskują HP w wysokości tych obrażeń.\nNa koniec tury maleje o 1.\nJeśli wskutek tych obrażeń HP spadnie do 0, odzyskanie HP nie jest możliwe.
310. [Status [MRcAmBc] — nazwa] 시선
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBc].name
   kontekst: identyfikator statusu w tekstach: `[MRcAmBc]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
311. [Status [MRcAmBc] — opis] 시선 1당 가하는 피해량 +10%\n턴 종료 시 시선 7이 되면, 출혈을 15 얻음. 경멸로 변환됨.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBc].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +10% damage for every Gaze value\nTurn End: at 7 Gaze, gain 15 Bleed and replace this effect with Contempt.
   PL: Zadaje +10% obrażeń za każdą wartość Spojrzenia\nNa koniec tury, przy wartości Spojrzenia 7, zyskuje 15 Krwawienia. Zamienia się w Pogardę.
312. [Status [MRcAmBd] — nazwa] 전부를 보는 시선
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBd].name
   kontekst: identyfikator statusu w tekstach: `[MRcAmBd]`
   limit: do 40 znaków
   EN: All-beholding Gaze
   PL: Wszystkowidzące Spojrzenie
313. [Status [MRcAmBd] — opis] 매 턴 종료시 1 얻음.\n시선이 있는 인격에게 턴 종료 시 체력 (4 * {0}) 고정 피해와 정신력 (4 * {0}) 고정 피해를 줌.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBd].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Gain 1 at every Turn End.\nTurn End: all units with Gaze take (4 x {0}) fixed HP damage and (4 x {0}) fixed SP damage.
   PL: Zyskuje 1 na koniec każdej tury.\nNa koniec tury jednostki ze Spojrzeniem otrzymują (4 x {0}) stałych obrażeń HP i (4 x {0}) stałych obrażeń Poczytalności
314. [Status [MRcAmBbDisplay] — nazwa] 손아귀
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBbDisplay].name
   kontekst: identyfikator statusu w tekstach: `[MRcAmBbDisplay]`
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Status [MRcAmBbDisplay] — opis] 최대 3\n행동 불가 상태가 됨\n턴 종료 시 2이하라면, 대상의 최대 체력 절반만큼 피해를 줌. 경멸의 나선 모든 부위를 피해만큼 회복시킴.\n턴 종료 시 1 감소.\n이 피해로 체력이 0이 되면, 체력 회복이 불가능함.
   źródło: Bufs_Refraction3.json :: dataList[id=MRcAmBbDisplay].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs_Refraction4
- plik gry: `Bufs_Refraction4.json`

316. [Status [UninvitedGuest] — nazwa] 불청객
   źródło: Bufs_Refraction4.json :: dataList[id=UninvitedGuest].name
   kontekst: identyfikator statusu w tekstach: `[UninvitedGuest]`
   limit: do 40 znaków
   EN: Interloper
   PL: Nieproszony Gość
317. [Status [UninvitedGuest] — opis] 불청객을 가진 인격이 죽을 때, 없는 인격에게 옮겨감.
   źródło: Bufs_Refraction4.json :: dataList[id=UninvitedGuest].desc
   limit: do 130 znaków
   EN: When an Identity with Interloper is defeated, move to a different Identity without Interloper.
   PL: Gdy ginie Tożsamość posiadająca Nieproszonego Gościa, efekt przenosi się na Tożsamość, która go nie posiada.
318. [Status [ConnectedPlug] — nazwa] 연결된 플러그
   źródło: Bufs_Refraction4.json :: dataList[id=ConnectedPlug].name
   kontekst: identyfikator statusu w tekstach: `[ConnectedPlug]`
   limit: do 40 znaków
   EN: Plugged In
   PL: Podłączony
319. [Status [ConnectedPlug] — opis] 턴 종료시\n- 최대 3\n- 3이 되면, 다음 턴동안 흐트러짐 상태가 됨.\n- 3이 되면, 자신의 모든 충전 횟수를 소모함.
   źródło: Bufs_Refraction4.json :: dataList[id=ConnectedPlug].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End:\n- Max 3\n- At 3, become Staggered next turn.\n- At 3, consume all Charge Count on self.
   PL: Na koniec tury:\n- maks. 3\n- przy 3, w następnej turze staje się Oszołomiony\n- przy 3, zużywa wszystkie własne Liczniki Ładowania
320. [Status [AntiSheepGround] — nazwa] 대양전 접지 플러그
   źródło: Bufs_Refraction4.json :: dataList[id=AntiSheepGround].name
   kontekst: identyfikator statusu w tekstach: `[AntiSheepGround]`
   limit: do 40 znaków
   EN: Anti-Ovine Grounding Plug
   PL: Wtyczka Uziemiająca Stacji Wielkiej Owcy
321. [Status [AntiSheepGround] — opis] - 최대 1\n- 해당 버프를 소유한 채, 접지 거부 스킬에 합 승리시 대상에게 연결된 플러그 1 부여\n- 대상의 충전 횟수 절반 감소\n-다음 턴에 소멸됨
   źródło: Bufs_Refraction4.json :: dataList[id=AntiSheepGround].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max 1\n- When a unit under this effect wins a Clash against the 'Grounding Refusal' Skill, inflict 1 Plugged In against the target\n- Halve the Charge Count on the target\n- Expires next turn
   PL: - Maks. 1\n- Posiadając ten efekt, przy wygranej w Starciu z Umiejętnością 'Odmowa Uziemienia' nakłada na cel 1 Podłączenia\n- Zmalekuje Licznik Ładowania celu o połowę\n- Znika w następnej turze
322. [Status [ThundercloudFormation] — nazwa] 전운집
   źródło: Bufs_Refraction4.json :: dataList[id=ThundercloudFormation].name
   kontekst: identyfikator statusu w tekstach: `[ThundercloudFormation]`
   limit: do 40 znaków
   EN: Gathering Lightning Cloud
   PL: Gromadząca się Chmura Gromu
323. [Status [ThundercloudFormation] — opis] - 최대 5\n- 수치가 1일 때, 강한 스킬을 사용함.\n- 턴 종료 시 1 감소함. 흐트러짐 상태가 되면, 1 증가
   źródło: Bufs_Refraction4.json :: dataList[id=ThundercloudFormation].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max 5\n- At 1 value, use a powerful Skill.\n- Reduced by 1 at Turn End. Gain 1 value when Staggered
   PL: - Maks. 5\n- Przy wartości 1 używa potężnej Umiejętności\n- Na koniec tury maleje o 1. Po popadnięciu w stan Oszołomienia rośnie o 1
324. [Status [Refraction4A] — nazwa] 1번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4A].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4A]`
   limit: do 40 znaków
   EN: #1 Deployment Effect
   PL: Efekt Rozmieszczenia nr 1
325. [Status [Refraction4A] — opis] 인격 레벨 +2\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4A].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Identity Level +2\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Poziom Tożsamości +2\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
326. [Status [Refraction4B] — nazwa] 2번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4B].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4B]`
   limit: do 40 znaków
   EN: #2 Deployment Effect
   PL: Efekt Rozmieszczenia nr 2
327. [Status [Refraction4B] — opis] 정신력 회복 효율 +3\n시작 정신력 +10 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 수량만큼 E.G.O 자원을 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4B].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SP Heal Efficiency +3\nEntry SP +10 (-10 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on each Attack Skill's Affinity & number.
   PL: Skuteczność leczenia Poczytalności +3\nPoczytalność początkowa +10 (Tożsamości z monetami Minus: -10)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i liczbie posiadanych Umiejętności ataku
328. [Status [Refraction4C] — nazwa] 3번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4C].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4C]`
   limit: do 40 znaków
   EN: #3 Deployment Effect
   PL: Efekt Rozmieszczenia nr 3
329. [Status [Refraction4C] — opis] 공격 레벨 +2\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4C].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Offense Level +2\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Poziom Ataku +2\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
330. [Status [Refraction4D] — nazwa] 4번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4D].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4D]`
   limit: do 40 znaków
   EN: #4 Deployment Effect
   PL: Efekt Rozmieszczenia nr 4
331. [Status [Refraction4D] — opis] 방어 레벨 +2\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4D].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Defense Level +2\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Poziom Obrony +2\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
332. [Status [Refraction4E] — nazwa] 5번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4E].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4E]`
   limit: do 40 znaków
   EN: #5 Deployment Effect
   PL: Efekt Rozmieszczenia nr 5
333. [Status [Refraction4E] — opis] 2턴부터 최대 속도 +2\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4E].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting 2nd turn: Max Speed +2\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Od 2. tury Maksymalna Szybkość +2\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
334. [Status [Refraction4F] — nazwa] 6번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4F].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4F]`
   limit: do 40 znaków
   EN: #6 Deployment Effect
   PL: Efekt Rozmieszczenia nr 6
335. [Status [Refraction4F] — opis] 최대 체력 +5%\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4F].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max HP +5%\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Maks. HP +5%\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
336. [Status [Refraction4G] — nazwa] 7번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4G].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4G]`
   limit: do 40 znaków
   EN: #7 Deployment Effect
   PL: Efekt Rozmieszczenia nr 7
337. [Status [Refraction4G] — opis] 합 위력 +1\n시작 정신력 +15 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4G].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +1\nEntry SP +15 (-15 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Moc Starcia +1\nPoczytalność początkowa +15 (Tożsamości z monetami Minus: -15)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
338. [Status [Refraction4H] — nazwa] 8번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4H].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4H]`
   limit: do 40 znaków
   EN: #8 Deployment Effect
   PL: Efekt Rozmieszczenia nr 8
339. [Status [Refraction4H] — opis] 받는 피해량 -10%\n시작 정신력 +15 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4H].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Damage Taken -10%\nEntry SP +15 (-15 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Otrzymywane obrażenia -10%\nPoczytalność początkowa +15 (Tożsamości z monetami Minus: -15)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
340. [Status [Refraction4I] — nazwa] 9번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4I].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4I]`
   limit: do 40 znaków
   EN: #9 Deployment Effect
   PL: Efekt Rozmieszczenia nr 9
341. [Status [Refraction4I] — opis] 도발치 +5\n시작 정신력 +20 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4I].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Aggro +5\nEntry SP +20 (-20 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Wartość Prowokacji +5\nPoczytalność początkowa +20 (Tożsamości z monetami Minus: -20)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
342. [Status [Refraction4J] — nazwa] 10번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4J].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4J]`
   limit: do 40 znaków
   EN: #10 Deployment Effect
   PL: Efekt Rozmieszczenia nr 10
343. [Status [Refraction4J] — opis] 가하는 피해량 +10%\n시작 정신력 +20 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4J].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Damage Dealt +10%\nEntry SP +20 (-10 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Zadawane obrażenia +10%\nPoczytalność początkowa +20 (Tożsamości z monetami Minus: -20)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
344. [Status [Refraction4K] — nazwa] 11번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4K].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4K]`
   limit: do 40 znaków
   EN: #11 Deployment Effect
   PL: Efekt Rozmieszczenia nr 11
345. [Status [Refraction4K] — opis] 최종 위력 +1\n시작 정신력 +30 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4K].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Final Power +1\nEntry SP +30 (-30 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Moc Końcowa +1\nPoczytalność początkowa +30 (Tożsamości z monetami Minus: -30)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
346. [Status [Refraction4L] — nazwa] 12번 편성 효과
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4L].name
   kontekst: identyfikator statusu w tekstach: `[Refraction4L]`
   limit: do 40 znaków
   EN: #12 Deployment Effect
   PL: Efekt Rozmieszczenia nr 12
347. [Status [Refraction4L] — opis] 인격 레벨 +3\n시작 정신력 +30 (빼기 코인 인격은 -로 적용)\n사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=Refraction4L].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Identity Level +3\nEntry SP +30 (-30 for Minus Coin Identities)\nWhen defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Poziom Tożsamości +3\nPoczytalność początkowa +30 (Tożsamości z monetami Minus: -30)\nPo śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
348. [Status [BandageOfTheBoundKing] — nazwa] 묶인 왕의 붕대
   źródło: Bufs_Refraction4.json :: dataList[id=BandageOfTheBoundKing].name
   kontekst: identyfikator statusu w tekstach: `[BandageOfTheBoundKing]`
   limit: do 50 znaków
   EN: Bandages of the King in Binds
   PL: Bandaże Króla w Spętaniu
349. [Status [BandageOfTheBoundKing] — opis] 사망 시 모든 적에게 침잠 위력 2, 횟수 1 부여\n자신을 처치한 대상에게 묶인 왕의 붕대 부여. 대상에게 이미 해당 효과가 있거나 자신을 처치한 대상이 없으면, 해당 효과가 없는 무작위 적에게 부여
   źródło: Bufs_Refraction4.json :: dataList[id=BandageOfTheBoundKing].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When defeated, inflict 2 Sinking Potency and 1 Count against all enemies.\nApply Bandages of the King in Binds against the target that defeated this unit. If the said target already has that effect, or if the said target does not exist, apply it to a random enemy without that effect
   PL: Po śmierci nakłada na wszystkich wrogów Moc Zatonięcia 2 i Licznik 1\nNakłada Bandaże Króla w Spętaniu na jednostkę, która go pokonała. Jeśli cel już posiada ten efekt albo pokonująca jednostka nie istnieje, nakłada go na losowego wroga bez tego efektu
350. [Status [ComeForwardToTheKing] — nazwa] 알현의 시간
   źródło: Bufs_Refraction4.json :: dataList[id=ComeForwardToTheKing].name
   kontekst: identyfikator statusu w tekstach: `[ComeForwardToTheKing]`
   limit: do 40 znaków
   EN: Moment of Audience
   PL: Czas Audiencji
351. [Status [ComeForwardToTheKing] — opis] 자신의 모든 공격 스킬의 공격 가중치 +{0}\n합 패배 시 다음 턴에 취약 1을 얻음
   źródło: Bufs_Refraction4.json :: dataList[id=ComeForwardToTheKing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Gain +{0} Atk Weight to all of this unit's Attack Skills\nClash Lose: Gain 1 Fragile next turn
   PL: Wszystkie Umiejętności ataku tej jednostki zyskują +{0} Wagi Ataku\nPo przegranej w Starciu zyskuje 1 Wrażliwości w następnej turze
352. [Status [RefractedWill] — nazwa] 굴절된 의지
   źródło: Bufs_Refraction4.json :: dataList[id=RefractedWill].name
   kontekst: identyfikator statusu w tekstach: `[RefractedWill]`
   limit: do 40 znaków
   EN: Refracted Determination
   PL: Załamana Determinacja
353. [Status [RefractedWill] — opis] 아군 사망 시 기본 정신력 감소 조건으로 인한 정신력 감소가 절반으로 적용. (소수점 버림)
   źródło: Bufs_Refraction4.json :: dataList[id=RefractedWill].desc
   limit: do 170 znaków
   EN: Halve the amount of SP lost when an ally is defeated as per the Identity's 'Base factors decreasing Sanity(SP)'. (rounded down)
   PL: Spadek Poczytalności po śmierci sojusznika, wynikający z bazowych czynników obniżających Poczytalność, stosuje się w połowie (bez części dziesiętnych)
354. [Status [VioletPeccatulumTwo] — nazwa] 질투 죄종 2형
   źródło: Bufs_Refraction4.json :: dataList[id=VioletPeccatulumTwo].name
   kontekst: identyfikator statusu w tekstach: `[VioletPeccatulumTwo]`
   limit: do 40 znaków
   EN: Peccatulum Invidiae Class 2
   PL: Peccatulum Zazdrości 2. stadium
355. [Status [VioletPeccatulumTwo] — opis] - 가하는 피해량 +15%\n- 받는 피해량 -15%
   źródło: Bufs_Refraction4.json :: dataList[id=VioletPeccatulumTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Damage Dealt +15%\n- Damage Taken -15%
   PL: - Zadawane obrażenia +15%\n- Otrzymywane obrażenia -15%
356. [Status [BigWelcome] — nazwa] 성대한 환대
   źródło: Bufs_Refraction4.json :: dataList[id=BigWelcome].name
   kontekst: identyfikator statusu w tekstach: `[BigWelcome]`
   limit: do 40 znaków
   EN: Grand Welcome
   PL: Wspaniałe Powitanie
357. [Status [BigWelcome] — opis] 공격 종료 시 대상이 흐트러짐 상태가 되었거나 사망하였으면, 오만 속성 E.G.O 자원 +1, 나머지 속성의 E.G.O 자원 중 무작위 1종 +1 (턴 당 최대 3회 발동)
   źródło: Bufs_Refraction4.json :: dataList[id=BigWelcome].desc
   limit: do 200 znaków
   EN: Attack End: If the target is Staggered or defeated, gain +1 Pride E.G.O resource and +1 E.G.O resource for 1 other random Affinity (3 times per turn)
   PL: Po zakończeniu ataku, jeśli cel popadł w stan Oszołomienia lub zginął, zyskuje +1 zasobu E.G.O atrybutu Pychy i +1 zasobu losowego pozostałego atrybutu (maks. 3 razy na turę)
358. [Status [BreathSupport] — nazwa] 결전의 호흡
   źródło: Bufs_Refraction4.json :: dataList[id=BreathSupport].name
   kontekst: identyfikator statusu w tekstach: `[BreathSupport]`
   limit: do 40 znaków
   EN: Poised Showdown
   PL: Pojedynek na Oddechu
359. [Status [BreathSupport] — opis] 웨이브 시작 시 호흡 위력 4, 횟수 4 얻음.
   źródło: Bufs_Refraction4.json :: dataList[id=BreathSupport].desc
   limit: do 120 znaków
   EN: Wave Start: Gain 4 Poise Potency and Count.
   PL: Na początku fali zyskuje 4 Mocy Oddechu i 4 Licznika Oddechu.
360. [Status [FirmWill] — nazwa] 굳은 의지
   źródło: Bufs_Refraction4.json :: dataList[id=FirmWill].name
   kontekst: identyfikator statusu w tekstach: `[FirmWill]`
   limit: do 40 znaków
   EN: Resilient Determination
   PL: Niezłomna Wola
361. [Status [FirmWill] — opis] 아군 사망 시 정신력이 감소하지 않음.
   źródło: Bufs_Refraction4.json :: dataList[id=FirmWill].desc
   limit: do 120 znaków
   EN: Does not lose SP upon ally defeat.
   PL: Po śmierci sojusznika nie traci Poczytalności.

## Statusy i efekty bojowe — Bufs_Refraction5
- plik gry: `Bufs_Refraction5.json`

362. [Status [FellBulletMark] — nazwa] 징표
   źródło: Bufs_Refraction5.json :: dataList[id=FellBulletMark].name
   kontekst: identyfikator statusu w tekstach: `[FellBulletMark]`
   limit: do 40 znaków
   EN: Stigmatized
   PL: Napiętnowany
363. [Status [FellBulletMark] — opis] - 흉탄의 사수 표적이 됨\n- 턴 종료시 제거됨
   źródło: Bufs_Refraction5.json :: dataList[id=FellBulletMark].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Targeted by Der Fluchschütze\n- Expires at Turn End
   PL: - Staje się celem Der Fluchschütze\n- Znika na koniec tury
364. [Status [MRR501] — nazwa] 부여량 굴절
   źródło: Bufs_Refraction5.json :: dataList[id=MRR501].name
   kontekst: identyfikator statusu w tekstach: `[MRR501]`
   limit: do 40 znaków
   EN: Infliction Refraction
   PL: Załamanie Nadawania
365. [Status [MRR502] — nazwa] 획득량 굴절
   źródło: Bufs_Refraction5.json :: dataList[id=MRR502].name
   kontekst: identyfikator statusu w tekstach: `[MRR502]`
   limit: do 40 znaków
   EN: Gain Refraction
   PL: Załamanie Zyskiwania
366. [Status [MRR503] — nazwa] 굴절된 정신
   źródło: Bufs_Refraction5.json :: dataList[id=MRR503].name
   kontekst: identyfikator statusu w tekstach: `[MRR503]`
   limit: do 40 znaków
   EN: Refracted Mind
   PL: Załamany Umysł
367. [Status [MRR504] — nazwa] 굴절된 호흡
   źródło: Bufs_Refraction5.json :: dataList[id=MRR504].name
   kontekst: identyfikator statusu w tekstach: `[MRR504]`
   limit: do 40 znaków
   EN: Refracted Poise
   PL: Załamany Oddech
368. [Status [MRR505] — nazwa] 굴절된 충전
   źródło: Bufs_Refraction5.json :: dataList[id=MRR505].name
   kontekst: identyfikator statusu w tekstach: `[MRR505]`
   limit: do 40 znaków
   EN: Refracted Charge
   PL: Załamane Ładowanie
369. [Status [MRR506] — nazwa] 굴절된 폭발
   źródło: Bufs_Refraction5.json :: dataList[id=MRR506].name
   kontekst: identyfikator statusu w tekstach: `[MRR506]`
   limit: do 40 znaków
   EN: Refracted Burst
   PL: Załamany Wybuch
370. [Status [MRR507] — nazwa] 굴절된 파열
   źródło: Bufs_Refraction5.json :: dataList[id=MRR507].name
   kontekst: identyfikator statusu w tekstach: `[MRR507]`
   limit: do 40 znaków
   EN: Refracted Rupture
   PL: Załamane Rozdarcie
371. [Status [MRR508] — nazwa] 굴절된 침잠
   źródło: Bufs_Refraction5.json :: dataList[id=MRR508].name
   kontekst: identyfikator statusu w tekstach: `[MRR508]`
   limit: do 40 znaków
   EN: Refracted Sinking
   PL: Załamane Zatonięcie
372. [Status [MRR509] — nazwa] 약점 파괴
   źródło: Bufs_Refraction5.json :: dataList[id=MRR509].name
   kontekst: identyfikator statusu w tekstach: `[MRR509]`
   limit: do 40 znaków
   EN: Weakness Destroyed
   PL: Zniszczony Słaby Punkt
373. [Status [MRR510] — nazwa] 네뷸라이저
   źródło: Bufs_Refraction5.json :: dataList[id=MRR510].name
   kontekst: identyfikator statusu w tekstach: `[MRR510]`
   limit: do 40 znaków
   EN: Nebulizer
   PL: Nebulizator
374. [Status [MRR511] — nazwa] 고독한 사수
   źródło: Bufs_Refraction5.json :: dataList[id=MRR511].name
   kontekst: identyfikator statusu w tekstach: `[MRR511]`
   limit: do 40 znaków
   EN: The Lone Gunman
   PL: Samotny Strzelec
375. [Status [MRR512] — nazwa] 이어지는 투지
   źródło: Bufs_Refraction5.json :: dataList[id=MRR512].name
   kontekst: identyfikator statusu w tekstach: `[MRR512]`
   limit: do 40 znaków
   EN: Lasting Battle Spirit
   PL: Trwały Duch Walki
376. [Status [MRR513] — nazwa] 자원 수확
   źródło: Bufs_Refraction5.json :: dataList[id=MRR513].name
   kontekst: identyfikator statusu w tekstach: `[MRR513]`
   limit: do 40 znaków
   EN: Resource Reaping
   PL: Żniwa Zasobów
377. [Status [MRR515] — nazwa] 완강한 방어
   źródło: Bufs_Refraction5.json :: dataList[id=MRR515].name
   kontekst: identyfikator statusu w tekstach: `[MRR515]`
   limit: do 40 znaków
   EN: Dogged Defense
   PL: Zacięta Obrona
378. [Status [MRR516] — nazwa] 사생결단
   źródło: Bufs_Refraction5.json :: dataList[id=MRR516].name
   kontekst: identyfikator statusu w tekstach: `[MRR516]`
   limit: do 40 znaków
   EN: Life or Death
   PL: Życie albo Śmierć
379. [Status [MRR517] — nazwa] 격노한 반격
   źródło: Bufs_Refraction5.json :: dataList[id=MRR517].name
   kontekst: identyfikator statusu w tekstach: `[MRR517]`
   limit: do 40 znaków
   EN: Wrathful Counter
   PL: Wściekły Kontratak
380. [Status [MRR518] — nazwa] 추억의 펜던트
   źródło: Bufs_Refraction5.json :: dataList[id=MRR518].name
   kontekst: identyfikator statusu w tekstach: `[MRR518]`
   limit: do 40 znaków
   EN: Pendant of Nostalgia
   PL: Wisiorek Nostalgii
381. [Status [MRR520] — nazwa] 흉탄 쇄도
   źródło: Bufs_Refraction5.json :: dataList[id=MRR520].name
   kontekst: identyfikator statusu w tekstach: `[MRR520]`
   limit: do 40 znaków
   EN: Fell Bullet Deluge
   PL: Powódź Mrocznych Pocisków
382. [Status [MRR521] — nazwa] 체력 왜곡
   źródło: Bufs_Refraction5.json :: dataList[id=MRR521].name
   kontekst: identyfikator statusu w tekstach: `[MRR521]`
   limit: do 40 znaków
   EN: HP Manipulation
   PL: Manipulacja HP
383. [Status [MRR522] — nazwa] 위태로운 승부
   źródło: Bufs_Refraction5.json :: dataList[id=MRR522].name
   kontekst: identyfikator statusu w tekstach: `[MRR522]`
   limit: do 40 znaków
   EN: Perilous Contest
   PL: Ryzykowny Pojedynek
384. [Status [MRR523] — nazwa] 핏빛 연회
   źródło: Bufs_Refraction5.json :: dataList[id=MRR523].name
   kontekst: identyfikator statusu w tekstach: `[MRR523]`
   limit: do 40 znaków
   EN: Bloody Banquet
   PL: Krwawa Biesiada
385. [Status [MRR524] — nazwa] 피의 축제
   źródło: Bufs_Refraction5.json :: dataList[id=MRR524].name
   kontekst: identyfikator statusu w tekstach: `[MRR524]`
   limit: do 40 znaków
   EN: Festival of Blood
   PL: Święto Krwi
386. [Status [MRR526] — nazwa] 굴절된 참격
   źródło: Bufs_Refraction5.json :: dataList[id=MRR526].name
   kontekst: identyfikator statusu w tekstach: `[MRR526]`
   limit: do 40 znaków
   EN: Refracted Slash
   PL: Załamane Cięcie
387. [Status [MRR527] — nazwa] 굴절된 관통
   źródło: Bufs_Refraction5.json :: dataList[id=MRR527].name
   kontekst: identyfikator statusu w tekstach: `[MRR527]`
   limit: do 40 znaków
   EN: Refracted Pierce
   PL: Załamane Przebicie
388. [Status [MRR528] — nazwa] 굴절된 타격
   źródło: Bufs_Refraction5.json :: dataList[id=MRR528].name
   kontekst: identyfikator statusu w tekstach: `[MRR528]`
   limit: do 40 znaków
   EN: Refracted Blunt
   PL: Załamane Uderzenie
389. [Status [MRR529] — nazwa] 성장 굴절 I
   źródło: Bufs_Refraction5.json :: dataList[id=MRR529].name
   kontekst: identyfikator statusu w tekstach: `[MRR529]`
   limit: do 40 znaków
   EN: Growth Refraction I
   PL: Załamanie Rozwoju I
390. [Status [MRR530] — nazwa] 성장 굴절 II
   źródło: Bufs_Refraction5.json :: dataList[id=MRR530].name
   kontekst: identyfikator statusu w tekstach: `[MRR530]`
   limit: do 40 znaków
   EN: Growth Refraction II
   PL: Załamanie Rozwoju II
391. [Status [MRR532] — nazwa] 자원 휘발
   źródło: Bufs_Refraction5.json :: dataList[id=MRR532].name
   kontekst: identyfikator statusu w tekstach: `[MRR532]`
   limit: do 40 znaków
   EN: Resource Vaporization
   PL: Wyparowanie Zasobów
392. [Status [MRR533] — nazwa] 만발한 피
   źródło: Bufs_Refraction5.json :: dataList[id=MRR533].name
   kontekst: identyfikator statusu w tekstach: `[MRR533]`
   limit: do 40 znaków
   EN: Blossomed Blood
   PL: Rozkwitła Krew
393. [Status [MRR534] — nazwa] 완강한 방어
   źródło: Bufs_Refraction5.json :: dataList[id=MRR534].name
   kontekst: identyfikator statusu w tekstach: `[MRR534]`
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Status [MRR535] — nazwa] 사생결단
   źródło: Bufs_Refraction5.json :: dataList[id=MRR535].name
   kontekst: identyfikator statusu w tekstach: `[MRR535]`
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Status [MRR536] — nazwa] 굴절된 격노
   źródło: Bufs_Refraction5.json :: dataList[id=MRR536].name
   kontekst: identyfikator statusu w tekstach: `[MRR536]`
   limit: do 40 znaków
   EN: Refracted Rage
   PL: Załamana Wściekłość
396. [Status [MRR537] — nazwa] 체력 굴절 II
   źródło: Bufs_Refraction5.json :: dataList[id=MRR537].name
   kontekst: identyfikator statusu w tekstach: `[MRR537]`
   limit: do 40 znaków
   EN: HP Refraction II
   PL: Załamanie HP II
397. [Status [MRR539] — nazwa] 핏빛 연회
   źródło: Bufs_Refraction5.json :: dataList[id=MRR539].name
   kontekst: identyfikator statusu w tekstach: `[MRR539]`
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Status [MRR542] — nazwa] 체력 굴절 I
   źródło: Bufs_Refraction5.json :: dataList[id=MRR542].name
   kontekst: identyfikator statusu w tekstach: `[MRR542]`
   limit: do 40 znaków
   EN: HP Refraction I
   PL: Załamanie HP I
399. [Status [MRR543] — nazwa] 이어지는 의지
   źródło: Bufs_Refraction5.json :: dataList[id=MRR543].name
   kontekst: identyfikator statusu w tekstach: `[MRR543]`
   limit: do 40 znaków
   EN: Lasting Determination
   PL: Trwała Wola
400. [Status [FellBulletGroggy] — nazwa] 타겟 설정
   źródło: Bufs_Refraction5.json :: dataList[id=FellBulletGroggy].name
   kontekst: identyfikator statusu w tekstach: `[FellBulletGroggy]`
   limit: do 40 znaków
   EN: Targeting Settings
   PL: Ustawienia Celowania
401. [Status [FellBulletGroggy] — opis] - 해제 불가능\n- 턴 종료 시 0이 되면, 다음 턴에 흐트러짐 상태가 됨\n- 대상 지정 사격 스킬 사용시 타겟에게 징표가 없으면 1 감소\n- 대상 조정 사격 스킬이 합에서 패배하면 1 감소\n- 대상 조정 사격 스킬 사용 전 타겟으로 삼은 아군이 사망한 경우 1 감소
   źródło: Bufs_Refraction5.json :: dataList[id=FellBulletGroggy].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot be removed\n- If at 0 at Turn End, become Staggered next turn\n- When using 'Designated Target Fire' Skill, if the target isn't Stigmatized, lose 1 Stack\n- If the 'Designated Target Fire' Skill loses the Clash, lose 1 Stack\n- If the ally this unit targeted before using the 'Designated Target Fire' Skill is killed, lose 1 Stack
   PL: - Nie można go usunąć\n- Jeśli na koniec tury osiąga 0, w następnej turze popada w stan Oszołomienia\n- Przy użyciu Umiejętności 'Wystrzał Wskazanego Celu', jeśli cel nie posiada Napiętnowania, maleje o 1\n- Jeśli Umiejętność 'Wystrzał Wskazanego Celu' przegra Starcie, maleje o 1\n- Jeśli sojusznik wskazany jako cel przed użyciem Umiejętności 'Wystrzał Wskazanego Celu' zginie, maleje o 1
402. [Status [MRR544] — nazwa] 위력 룰렛
   źródło: Bufs_Refraction5.json :: dataList[id=MRR544].name
   kontekst: identyfikator statusu w tekstach: `[MRR544]`
   limit: do 40 znaków
   EN: Power Roulette
   PL: Ruletka Mocy
403. [Status [MRR545] — nazwa] 유리 대포
   źródło: Bufs_Refraction5.json :: dataList[id=MRR545].name
   kontekst: identyfikator statusu w tekstach: `[MRR545]`
   limit: do 40 znaków
   EN: Glass Cannon
   PL: Szklane Działo
404. [Status [MRR546] — nazwa] 하이리스크
   źródło: Bufs_Refraction5.json :: dataList[id=MRR546].name
   kontekst: identyfikator statusu w tekstach: `[MRR546]`
   limit: do 40 znaków
   EN: High-risk
   PL: Wysokie Ryzyko
405. [Status [MRR547] — nazwa] 위력 룰렛
   źródło: Bufs_Refraction5.json :: dataList[id=MRR547].name
   kontekst: identyfikator statusu w tekstach: `[MRR547]`
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Status [MRR548] — nazwa] 위태로운 승부
   źródło: Bufs_Refraction5.json :: dataList[id=MRR548].name
   kontekst: identyfikator statusu w tekstach: `[MRR548]`
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Status [MRR549] — nazwa] 사생결단
   źródło: Bufs_Refraction5.json :: dataList[id=MRR549].name
   kontekst: identyfikator statusu w tekstach: `[MRR549]`
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Status [MRR550] — nazwa] 하이리스크
   źródło: Bufs_Refraction5.json :: dataList[id=MRR550].name
   kontekst: identyfikator statusu w tekstach: `[MRR550]`
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Status [MRR551] — nazwa] 굴절된 출혈
   źródło: Bufs_Refraction5.json :: dataList[id=MRR551].name
   kontekst: identyfikator statusu w tekstach: `[MRR551]`
   limit: do 40 znaków
   EN: Refracted Bleed
   PL: Załamane Krwawienie
410. [Status [MRR552] — nazwa] 굴절된 투지
   źródło: Bufs_Refraction5.json :: dataList[id=MRR552].name
   kontekst: identyfikator statusu w tekstach: `[MRR552]`
   limit: do 40 znaków
   EN: Refracted Determination
   PL: Załamany Zapał
411. [Status [MRR553] — nazwa] 한 번의 숨
   źródło: Bufs_Refraction5.json :: dataList[id=MRR553].name
   kontekst: identyfikator statusu w tekstach: `[MRR553]`
   limit: do 40 znaków
   EN: A Single Breath
   PL: Jeden Oddech
412. [Status [MRR554] — nazwa] 사생결단
   źródło: Bufs_Refraction5.json :: dataList[id=MRR554].name
   kontekst: identyfikator statusu w tekstach: `[MRR554]`
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Status [MRR555] — nazwa] 합 위력 굴절
   źródło: Bufs_Refraction5.json :: dataList[id=MRR555].name
   kontekst: identyfikator statusu w tekstach: `[MRR555]`
   limit: do 40 znaków
   EN: Clash Power Refraction
   PL: Załamanie Mocy Starcia
414. [Status [MRR556] — nazwa] 유리 대포
   źródło: Bufs_Refraction5.json :: dataList[id=MRR556].name
   kontekst: identyfikator statusu w tekstach: `[MRR556]`
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Status [MRR5BaseP] — nazwa] 적용 중인 버프
   źródło: Bufs_Refraction5.json :: dataList[id=MRR5BaseP].name
   kontekst: identyfikator statusu w tekstach: `[MRR5BaseP]`
   limit: do 40 znaków
   EN: Active Buffs
   PL: Aktywne Wzmocnienia
416. [Status [MRR5BaseN] — nazwa] 적용 중인 고난
   źródło: Bufs_Refraction5.json :: dataList[id=MRR5BaseN].name
   kontekst: identyfikator statusu w tekstach: `[MRR5BaseN]`
   limit: do 40 znaków
   EN: Active Trials
   PL: Aktywne Utrapienia

## Statusy i efekty bojowe — Bufs_Refraction6
- plik gry: `Bufs_Refraction6.json`

417. [Status [NoeulNageuneBuffA3] — nazwa] 노을 나그네의 수액
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA3].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffA3]`
   limit: do 40 znaków
   EN: Sunset Wayfarer's Sap
   PL: Sok Wędrowca Zachodu Słońca
418. [Status [NoeulNageuneBuffA3] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 자신의 첫번째 흐트러짐 구간 삭제
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- Remove this unit's first Stagger Threshold
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Usuwa pierwszy Próg Oszołomienia
419. [Status [NoeulNageuneBuffA4] — nazwa] 노을 나그네의 수액
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA4].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffA4]`
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Status [NoeulNageuneBuffA4] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 파괴 불가 코인으로 피격 시 받는 피해량 -20%
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- When hit by Unbreakable Coins, take -20% damage
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Przy trafieniu Niezniszczalnymi Monetami otrzymuje -20% obrażeń
421. [Status [NoeulNageuneBuffA5] — nazwa] 노을 나그네의 수액
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA5].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffA5]`
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Status [NoeulNageuneBuffA5] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 자신의 첫번째 흐트러짐 구간 삭제\n- 턴 종료 시 정신력이 가장 낮은 아군 4명의 정신력 4 회복 (패닉, 침식 상태인 아군 제외)
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffA5].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- Remove this unit's first Stagger Threshold\n- Turn End: 4 allies that have the lowest SP heal 4 SP (excluding Panicked or Corroded allies)
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Usuwa pierwszy Próg Oszołomienia\n- Na koniec tury 4 sojuszników z najniższą Poczytalnością odzyskuje 4 Poczytalności (z wyłączeniem sojuszników w stanie Paniki lub Korozji)
423. [Status [NoeulNageuneBuffB3] — nazwa] 노을 나그네의 나방
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB3].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffB3]`
   limit: do 40 znaków
   EN: Sunset Wayfarer's Moth
   PL: Ćma Wędrowca Zachodu Słońca
424. [Status [NoeulNageuneBuffB3] — opis] - 턴 시작 시 전장에 자신과 같은 소속인 아군(자신 포함) 1명당, 공격 레벨 증가 1 얻음 (최대 4)
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB3].desc
   limit: do 150 znaków
   EN: - Turn Start: Gain 1 Offense Level Up for every allied unit (including self) in the same faction as self (max 4)
   PL: - Na początek tury za każdego sojusznika tej samej frakcji na polu walki (wliczając siebie) zyskuje 1 Wzrost Poziomu Ataku (maks. 4)
425. [Status [NoeulNageuneBuffB4] — nazwa] 노을 나그네의 나방
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB4].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffB4]`
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Status [NoeulNageuneBuffB4] — opis] - 매 턴마다 참격 피해량 증가 1, 관통 피해량 증가 1, 타격 피해량 증가 1 중 무작위 1개 얻음. 해당 속성의 E.G.O 스킬 사용 시 가하는 피해량 +50%\n- 파괴 불가 코인으로 적중 시 가하는 피해량 +20%
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB4].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack of a random status every turn, chosen from Slash DMG Up, Pierce DMG Up, and Blunt DMG Up. When using an E.G.O Skill of the corresponding Attack Type, deal +50% damage\n- On Hit with Unbreakable Coins, deal +20% damage
   PL: - Co turę zyskuje 1 losowy z efektów: Wzrost Obrażeń Cięcia, Wzrost Obrażeń Przebicia i Wzrost Obrażeń Uderzenia. Umiejętności E.G.O atrybutu zyskanego efektu zadają +50% obrażeń\n- Przy trafieniu Niezniszczalnymi Monetami zadaje +20% obrażeń
427. [Status [NoeulNageuneBuffB5] — nazwa] 노을 나그네의 나방
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB5].name
   kontekst: identyfikator statusu w tekstach: `[NoeulNageuneBuffB5]`
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Status [NoeulNageuneBuffB5] — opis] - 턴 시작 시 이미 사망한 아군 1명당, 공격 레벨 증가 1 얻음 (최대 6)\n- 전투 시작 시 완전 공명했으면, 완전 공명한 스킬이 가하는 피해량 +20%
   źródło: Bufs_Refraction6.json :: dataList[id=NoeulNageuneBuffB5].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Offense Level Up for every ally defeated in this Encounter (max 6)\n- Combat Start: On A-Reson., Skills that are a part of the A-Reson. chain deal +20% damage
   PL: - Na początek tury za każdego sojusznika, który już zginął, zyskuje 1 Wzrost Poziomu Ataku (maks. 6)\n- Jeśli na początku walki wywołano Rezonans Absolutny, Umiejętności z Rezonansem Absolutnym zadają +20% obrażeń
429. [Status [HeatedWingScalesExplain] — nazwa] 달궈진 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=HeatedWingScalesExplain].name
   kontekst: identyfikator statusu w tekstach: `[HeatedWingScalesExplain]`
   limit: do 40 znaków
   EN: Incandescent Scale Dust
   PL: Rozżarzony Pył Łusek
430. [Status [HeatedWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 회귀’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=HeatedWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Regression" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Regres' Motyla Splątanych Żywotów::Poczwarki
431. [Status [TransparentWingScalesExplain] — nazwa] 예리한 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=TransparentWingScalesExplain].name
   kontekst: identyfikator statusu w tekstach: `[TransparentWingScalesExplain]`
   limit: do 40 znaków
   EN: Acuate Scale Dust
   PL: Ostry Pył Łusek
432. [Status [TransparentWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 현현’과 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=TransparentWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Manifestation" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Manifestacja' Motyla Splątanych Żywotów::Poczwarki
433. [Status [RustedWingScalesExplain] — nazwa] 녹슨 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=RustedWingScalesExplain].name
   kontekst: identyfikator statusu w tekstach: `[RustedWingScalesExplain]`
   limit: do 40 znaków
   EN: Rusted Scale Dust
   PL: Zardzewiały Pył Łusek
434. [Status [RustedWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 도래’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=RustedWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Advent" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Nadejście' Motyla Splątanych Żywotów::Poczwarki
435. [Status [HeatedWingScales] — nazwa] 달궈진 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=HeatedWingScales].name
   kontekst: identyfikator statusu w tekstach: `[HeatedWingScales]`
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Status [HeatedWingScales] — opis] - 나생접::고치의 ‘나생 - 회귀’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=HeatedWingScales].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Regression" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z 'Splątany Żywot - Regres' Motyla Splątanych Żywotów::Poczwarki
437. [Status [TransparentWingScales] — nazwa] 예리한 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=TransparentWingScales].name
   kontekst: identyfikator statusu w tekstach: `[TransparentWingScales]`
   (powtórzenie elementu 431 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Status [TransparentWingScales] — opis] - 나생접::고치의 ‘나생 - 현현’과 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=TransparentWingScales].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Manifestation" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z 'Splątany Żywot - Manifestacja' Motyla Splątanych Żywotów::Poczwarki
439. [Status [RustedWingScales] — nazwa] 녹슨 비늘 가루
   źródło: Bufs_Refraction6.json :: dataList[id=RustedWingScales].name
   kontekst: identyfikator statusu w tekstach: `[RustedWingScales]`
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Status [RustedWingScales] — opis] - 나생접::고치의 스킬 ‘나생 - 도래’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: Bufs_Refraction6.json :: dataList[id=RustedWingScales].desc
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Status [StackPast] — nazwa] 과거 상태 (비활성화)
   źródło: Bufs_Refraction6.json :: dataList[id=StackPast].name
   kontekst: identyfikator statusu w tekstach: `[StackPast]`
   limit: do 40 znaków
   EN: In the Past (Deactivated)
   PL: Stan Przeszłości (Nieaktywny)
442. [Status [StackPast] — opis] - 패시브 ‘과거 [過去]’ 비활성화\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackPast].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Past [過去]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Przeszłość [過去]' nieaktywny\n- Maks. 30
443. [Status [StackPresent] — nazwa] 현재 상태 (비활성화)
   źródło: Bufs_Refraction6.json :: dataList[id=StackPresent].name
   kontekst: identyfikator statusu w tekstach: `[StackPresent]`
   limit: do 40 znaków
   EN: In the Present (Deactivated)
   PL: Stan Teraźniejszości (Nieaktywny)
444. [Status [StackPresent] — opis] - 패시브 ‘현재 [現在]’ 비활성화\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackPresent].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Present [現在]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Teraźniejszość [現在]' nieaktywny\n- Maks. 30
445. [Status [StackFuture] — nazwa] 미래 상태 (비활성화)
   źródło: Bufs_Refraction6.json :: dataList[id=StackFuture].name
   kontekst: identyfikator statusu w tekstach: `[StackFuture]`
   limit: do 40 znaków
   EN: In the Future (Deactivated)
   PL: Stan Przyszłości (Nieaktywny)
446. [Status [StackFuture] — opis] - 패시브 ‘미래 [未來]’ 비활성화\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackFuture].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Future [未來]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Przyszłość [未來]' nieaktywny\n- Maks. 30
447. [Status [StackPastActivate] — nazwa] 과거 상태
   źródło: Bufs_Refraction6.json :: dataList[id=StackPastActivate].name
   kontekst: identyfikator statusu w tekstach: `[StackPastActivate]`
   limit: do 40 znaków
   EN: In the Past
   PL: Stan Przeszłości
448. [Status [StackPastActivate] — opis] - 패시브 ‘과거 [過去]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 부여하는 화상 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 부여하는 화상 위력 +2, 화상 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 부여하는 화상 위력 +3, 화상 횟수 +2\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackPastActivate].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Past [過去]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills inflict +1 more Burn Potency and Count\n· 11~20: Clash Power +1; Skills inflict +2 more Burn Potency and +1 more Burn Count\n· 21~30: Final Power +2; Skills inflict +3 more Burn Potency and +2 more Burn Count\n- Max Stack: 30
   PL: - Pasyw 'Przeszłość [過去]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności nadają Moc Podpalenia i Licznik Podpalenia +1\n· 11~20: Moc Starcia +1, Umiejętności nadają Moc Podpalenia +2 i Licznik Podpalenia +1\n· 21~30: Moc Końcowa +2, Umiejętności nadają Moc Podpalenia +3 i Licznik Podpalenia +2\n- Maks. 30
449. [Status [StackPresentActivate] — nazwa] 현재 상태
   źródło: Bufs_Refraction6.json :: dataList[id=StackPresentActivate].name
   kontekst: identyfikator statusu w tekstach: `[StackPresentActivate]`
   limit: do 40 znaków
   EN: In the Present
   PL: Stan Teraźniejszości
450. [Status [StackPresentActivate] — opis] - 패시브 ‘현재 [現在]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 획득하는 호흡 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 획득하는 호흡 위력 +2, 호흡 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 획득하는 호흡 위력 +3, 호흡 횟수 +2\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackPresentActivate].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Present [現在]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills gain +1 more Poise Potency and Count\n· 11~20: Clash Power +1; Skills gain +2 more Poise Potency and +1 more Poise Count\n· 21~30: Final Power +2; Skills gain +3 more Poise Potency and +2 more Poise Count\n- Max Stack: 30
   PL: - Pasyw 'Teraźniejszość [現在]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności zyskują Moc Oddechu i Licznik Oddechu +1\n· 11~20: Moc Starcia +1, Umiejętności zyskują Moc Oddechu +2 i Licznik Oddechu +1\n· 21~30: Moc Końcowa +2, Umiejętności zyskują Moc Oddechu +3 i Licznik Oddechu +2\n- Maks. 30
451. [Status [StackFutureActivate] — nazwa] 미래 상태
   źródło: Bufs_Refraction6.json :: dataList[id=StackFutureActivate].name
   kontekst: identyfikator statusu w tekstach: `[StackFutureActivate]`
   limit: do 40 znaków
   EN: In the Future
   PL: Stan Przyszłości
452. [Status [StackFutureActivate] — opis] - 패시브 ‘미래 [未來]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 부여하는 출혈 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 부여하는 출혈 위력 +2, 출혈 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 부여하는 출혈 위력 +3, 출혈 횟수 +2\n- 최대 30
   źródło: Bufs_Refraction6.json :: dataList[id=StackFutureActivate].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Future [未來]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills inflict +1 more Bleed Potency and Count\n· 11~20: Clash Power +1; Skills inflict +2 more Bleed Potency and +1 more Bleed Count\n· 21~30: Final Power +2; Skills inflict +3 more Bleed Potency and +2 more Bleed Count\n- Max Stack: 30
   PL: - Pasyw 'Przyszłość [未來]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności nadają Moc Krwawienia i Licznik Krwawienia +1\n· 11~20: Moc Starcia +1, Umiejętności nadają Moc Krwawienia +2 i Licznik Krwawienia +1\n· 21~30: Moc Końcowa +2, Umiejętności nadają Moc Krwawienia +3 i Licznik Krwawienia +2\n- Maks. 30
453. [Status [TimeGap] — nazwa] 시간 괴리
   źródło: Bufs_Refraction6.json :: dataList[id=TimeGap].name
   kontekst: identyfikator statusu w tekstach: `[TimeGap]`
   limit: do 40 znaków
   EN: Temporal Disjunction
   PL: Rozdźwięk Czasu
454. [Status [TimeGap] — opis] - 과거 상태/현재 상태/미래 상태에서 다른 상태로 전환될 때마다 수치 1 증가\n- 받는 피해량 +(수치 x 15)% (최대 150%)\n- 턴 시작 시 수치가 10이면, 취약 5 얻음\n- 최대 10
   źródło: Bufs_Refraction6.json :: dataList[id=TimeGap].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack every time this unit switches between In the Past / In the Present / In the Future\n- Take +(Stack x 15)% damage (max 150%)\n- Turn Start: At 10 Stack, gain 5 Fragile\n- Max Stack: 10
   PL: - Za każdą zmianę między Stanem Przeszłości / Stanem Teraźniejszości / Stanem Przyszłości a innym stanem rośnie o 1\n- Otrzymuje +(wartość x 15)% obrażeń (maks. 150%)\n- Na początek tury przy wartości 10 zyskuje 5 Wrażliwości\n- Maks. 10
455. [Status [YesdragonSelfRefraction] — nazwa] 매화침[埋花針]
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonSelfRefraction].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonSelfRefraction]`
   limit: do 40 znaków
   EN: Flower-burying Pin [埋花針]
   PL: Igła Pogrzebania Kwiatów [埋花針]
456. [Status [YesdragonSelfRefraction] — opis] - 최댓값: 10\n- 수치 2당, 공격 레벨 1 증가, 방어 레벨 1 증가\n- 수치가 5 이상이면, 최종 위력 +1\n- 수치가 최댓값이면, 코인 위력 +1\n- 매화침이 소모되면 소모된 수치 1당, 적에게 가장 부족한 E.G.O 자원 1개씩 지급
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonSelfRefraction].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Gain 1 Offense Level and 1 Defense Level for every 2 Stack\n- At 5+ Stack, Final Power +1\n- At max Stack, Coin Power +1\n- When consuming Flower-burying Pin, give 1 E.G.O resource of the least-owned Affinity for every Stack consumed
   PL: - Maks.: 10\n- Za każde 2 wartości Poziom Ataku +1 i Poziom Obrony +1\n- Przy wartości 5 lub więcej Moc Końcowa +1\n- Przy maksymalnej wartości Moc Monet +1\n- Po zużyciu Igły Pogrzebania Kwiatów za każdą zużytą wartość przyznaje wrogowi po 1 najbardziej mu brakującego zasobu E.G.O
457. [Status [CondensedBloodRefraction] — nazwa] 용혈[龍血]
   źródło: Bufs_Refraction6.json :: dataList[id=CondensedBloodRefraction].name
   kontekst: identyfikator statusu w tekstach: `[CondensedBloodRefraction]`
   limit: do 40 znaków
   EN: Dragon's Blood [龍血]
   PL: Krew Smoka [龍血]
458. [Status [CondensedBloodRefraction] — opis] - 위력 최댓값: 50\n- 턴 종료 시 수치당 최대 체력의 1%만큼 체력 피해를 받음 (최소 1, 해당 피해로 인해 흐트러지지 않음)\n- 수비 스킬 사용 시 횟수 1 감소 (턴당 1회)\n- 턴 종료 시 위력이 2배로 증가하고, 횟수 1 감소\n- 해당 효과는 횟수가 0이 되어야만 해제됨
   źródło: Bufs_Refraction6.json :: dataList[id=CondensedBloodRefraction].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 50\n- Turn End: Take 1% HP damage per Potency (min 1; cannot be Staggered by this effect)\n- Lose 1 Count when using a Defense Skill (once per turn)\n- Turn End: Double Potency and lose 1 Count\n- This effect can be removed only by reducing Count to 0
   PL: - Maks. Mocy: 50\n- Na koniec tury otrzymuje obrażenia HP równe 1% Maks. HP za każdą wartość (min. 1; nie popada w Oszołomienie z tych obrażeń)\n- Przy użyciu Umiejętności obrony Licznik maleje o 1 (raz na turę)\n- Na koniec tury Moc rośnie dwukrotnie, a Licznik maleje o 1\n- Ten efekt znika dopiero przy Liczniku 0
459. [Status [DragonLanceRefraction] — nazwa] 매화첨[埋花櫼]
   źródło: Bufs_Refraction6.json :: dataList[id=DragonLanceRefraction].name
   kontekst: identyfikator statusu w tekstach: `[DragonLanceRefraction]`
   limit: do 40 znaków
   EN: Flower-burying Wedge [埋花櫼]
   PL: Klin Pogrzebania Kwiatów [埋花櫼]
460. [Status [DragonLanceRefraction] — opis] - 매화첨 부위 체력: {0}\n- 최댓값: 3\n- 응룡의 특정 스킬 강화
   źródło: Bufs_Refraction6.json :: dataList[id=DragonLanceRefraction].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Flower-burying Wedge Part HP: {0}\n- Max Stack: 3\n- Enhances Yinglong's certain Skills
   PL: - HP części Klin Pogrzebania Kwiatów: {0}\n- Maks.: 3\n- Wzmacnia określone Umiejętności Yinglonga
461. [Status [YesdragonPower] — nazwa] 용의 기운[龍氣]
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonPower].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonPower]`
   limit: do 40 znaków
   EN: Dragon's Spirit [龍氣]
   PL: Energia Smoka [龍氣]
462. [Status [YesdragonPower] — opis] - 받는 피해량 -100%\n- 피격 후 해당 스킬 종료 시 소멸
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take -100% damage\n- When hit, expires at Skill End of the Skill that hit
   PL: - Otrzymuje -100% obrażeń\n- Znika po zakończeniu Umiejętności, która trafiła
463. [Status [YesdragonWind] — nazwa] 변덕스러운 자비
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonWind].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonWind]`
   limit: do 40 znaków
   EN: Capricious Mercy
   PL: Kapryśne Miłosierdzie
464. [Status [YesdragonWind] — opis] - 속도 최솟값, 최댓값 +3\n- 합 위력+2\n- 피격 후 해당 스킬 종료 시 소멸
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonWind].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Clash Power +2\n- When hit, expires at Skill End of the Skill that hit
   PL: - Minimalna i maksymalna Szybkość +3\n- Moc Starcia +2\n- Znika po zakończeniu Umiejętności, która trafiła
465. [Status [YesdragonScale] — nazwa] 뒤덮은 비늘
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonScale].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonScale]`
   limit: do 40 znaków
   EN: Scaleclad
   PL: Pokrywające Łuski
466. [Status [YesdragonScale] — opis] - 최댓값: 20\n- 해당 효과는 수치가 0이 되더라도 소멸하지 않음\n- 매화침으로 인한 피해를 받을 시 수치가 1 감소\n- 수치가 1 감소할 때 마다, 받는 피해량 +10%
   źródło: Bufs_Refraction6.json :: dataList[id=YesdragonScale].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Does not expire at 0 Stack\n- Lose 1 Stack when taking damage due to Flower-burying Pin\n- Take +10% damage for every Stack lost
   PL: - Maks.: 20\n- Ten efekt nie znika nawet przy wartości 0\n- Przy otrzymaniu obrażeń od Igły Pogrzebania Kwiatów maleje o 1\n- Za każdy spadek o 1 otrzymuje +10% obrażeń
467. [Status [TagGameBuff] — nazwa] 술래
   źródło: Bufs_Refraction6.json :: dataList[id=TagGameBuff].name
   kontekst: identyfikator statusu w tekstach: `[TagGameBuff]`
   limit: do 40 znaków
   EN: "It"
   PL: Berek
468. [Status [TagGameBuff] — opis] - 일방 공격으로 가하는 피해량 -100%\n- 일방 공격으로 받는 피해량 +80%\n- 자신을 포함한 모든 질투 죄종은 스킬 슬롯에 수비 스킬만 장착함\n- 턴 종료 시 수치 1 감소
   źródło: Bufs_Refraction6.json :: dataList[id=TagGameBuff].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal -100% damage using Unopposed Attacks\n- Take +80% damage from Unopposed Attacks\n- All Peccatulum Invidiae units, including this unit, equip only Defense Skills in their Skill Slots\n- Turn End: Lose 1 Stack
   PL: - Zadaje -100% obrażeń Atakami Niekwestionowanymi\n- Otrzymuje +80% obrażeń od Ataków Niekwestionowanych\n- Wszystkie Peccatulum Zazdrości, wliczając tę jednostkę, wyposażają w slotach Umiejętności wyłącznie Umiejętności obrony\n- Na koniec tury maleje o 1
469. [Status [ObservationTheRingsRail] — nazwa] 조망
   źródło: Bufs_Refraction6.json :: dataList[id=ObservationTheRingsRail].name
   kontekst: identyfikator statusu w tekstach: `[ObservationTheRingsRail]`
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Status [ObservationTheRingsRail] — opis] - 기본 공격 레벨 20 감소\n- 기본 방어 레벨 20 감소\n- 약지 제자가 전투 가능 상태면, 턴 시작 시 보호 7 얻음
   źródło: Bufs_Refraction6.json :: dataList[id=ObservationTheRingsRail].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -20\n- Base Defense Level -20\n- Turn Start: Gain 7 Protection if The Ring Apprentice has not retreated from this Encounter
   PL: - Bazowy Poziom Ataku -20\n- Bazowy Poziom Obrony -20\n- Jeśli Uczeń Pierścienia może walczyć, na początek tury zyskuje 7 Ochrony
471. [Status [ObservationTheRingsRail] — tekst klimatyczny] “갤러리에서 작품을 감상할 때는 느긋하고 여유롭게. 서두르지 않는 것이 중요하답니다.”
   źródło: Bufs_Refraction6.json :: dataList[id=ObservationTheRingsRail].flavor
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Status [MiddleFingerLeashBuff] — nazwa] 억제된 힘
   źródło: Bufs_Refraction6.json :: dataList[id=MiddleFingerLeashBuff].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerLeashBuff]`
   limit: do 40 znaków
   EN: Suppressed Might
   PL: Stłumiona Siła
473. [Status [MiddleFingerLeashBuff] — opis] - 일방 공격으로 가하는 피해량 -100%\n- 이번 전투에 아군이 3명 이상 사망했으면, 턴 종료 시 이 효과 소멸
   źródło: Bufs_Refraction6.json :: dataList[id=MiddleFingerLeashBuff].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unopposed Attacks deal -100% damage\n- Turn End: If 3+ allies are defeated in this Encounter, this effect expires
   PL: - Zadaje -100% obrażeń Atakami Niekwestionowanymi\n- Jeśli w tej walce zginęło 3 lub więcej sojuszników, ten efekt znika na koniec tury
474. [Status [ScarBygoneDaysRefraction_LowMorale] — nazwa] 애증
   źródło: Bufs_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ScarBygoneDaysRefraction_LowMorale]`
   limit: do 40 znaków
   EN: Affection and Resentment
   PL: Miłość i Uraza
475. [Status [ScarBygoneDaysRefraction_LowMorale] — opis] 가하는 피해량과 받는 피해량 +10%
   źródło: Bufs_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_LowMorale].desc
   limit: do 120 znaków
   EN: Deal and take +10% damage
   PL: Zadaje i otrzymuje +10% obrażeń
476. [Status [ScarBygoneDaysRefraction_Panic] — nazwa] 애증
   źródło: Bufs_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ScarBygoneDaysRefraction_Panic]`
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Status [ScarBygoneDaysRefraction_Panic] — opis] 가하는 피해량과 받는 피해량 +20%
   źródło: Bufs_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_Panic].desc
   limit: do 120 znaków
   EN: Deal and take +20% damage
   PL: Zadaje i otrzymuje +20% obrażeń
478. [Status [PainfulScarRailway_Panic] — nazwa] 모조된 아비
   źródło: Bufs_Refraction6.json :: dataList[id=PainfulScarRailway_Panic].name
   kontekst: identyfikator statusu w tekstach: `[PainfulScarRailway_Panic]`
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
479. [Status [PainfulScarRailway_Panic] — opis] - 패닉\n- 턴 시작 시, 화상 5, 화상 횟수 3, 출혈 5, 출혈 횟수 3 얻음
   źródło: Bufs_Refraction6.json :: dataList[id=PainfulScarRailway_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 5 Burn, +3 Burn Count, 5 Bleed, and +3 Bleed Count
   PL: - Panika\n- Na początek tury zyskuje Moc Podpalenia 5, Licznik Podpalenia 3, Moc Krwawienia 5 i Licznik Krwawienia 3
480. [Status [PainfulScarRailway_LowMorale] — nazwa] 모조된 아비
   źródło: Bufs_Refraction6.json :: dataList[id=PainfulScarRailway_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[PainfulScarRailway_LowMorale]`
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Status [PainfulScarRailway_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 화상 5, 출혈 5 얻음
   źródło: Bufs_Refraction6.json :: dataList[id=PainfulScarRailway_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 5 Burn and 5 Bleed
   PL: - Niskie Morale\n- Na początek tury zyskuje Moc Podpalenia 5 i Moc Krwawienia 5

## Statusy i efekty bojowe — Bufs_Synergy
- plik gry: `Bufs_Synergy.json`

482. [Status [SynergyActivationConditions_ForthMatchFlame] — nazwa] 시너지 발동 조건
   źródło: Bufs_Synergy.json :: dataList[id=SynergyActivationConditions_ForthMatchFlame].name
   kontekst: identyfikator statusu w tekstach: `[SynergyActivationConditions_ForthMatchFlame]`
   limit: do 40 znaków
   EN: Synergy Activation Condition
   PL: Warunki Aktywacji Synergii
483. [Status [SynergyActivationConditions_ForthMatchFlame] — opis] - [4번째 성냥불] 이상 : 환상 해석 5단계\n- [4번째 성냥불] 료슈 : 환상 해석 5단계\n- [4번째 성냥불] 로쟈 : 환상 해석 5단계
   źródło: Bufs_Synergy.json :: dataList[id=SynergyActivationConditions_ForthMatchFlame].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - [4th Match Flame] Yi Sang: Threadspin Tier 5\n- [4th Match Flame] Ryōshū: Threadspin Tier 5\n- [4th Match Flame] Rodion: Threadspin Tier 5
   PL: - [4. Płomyk Zapałki] Yi Sang: Splot Nici na 5. stopniu\n- [4. Płomyk Zapałki] Ryōshū: Splot Nici na 5. stopniu\n- [4. Płomyk Zapałki] Rodion: Splot Nici na 5. stopniu
