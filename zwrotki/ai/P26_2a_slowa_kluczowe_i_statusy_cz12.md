# Paczka AI P26 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 12/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P26_2a_slowa_kluczowe_i_statusy_cz12.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P26_2a_slowa_kluczowe_i_statusy_cz12.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs
- plik gry: `Bufs.json`

1. [Status [VioletResistDown] — nazwa] 질투 내성 약화
   źródło: Bufs.json :: dataList[id=VioletResistDown].name
   kontekst: identyfikator statusu w tekstach: `[VioletResistDown]`
   limit: do 40 znaków
   EN: Envy Resist Down
   PL: Osłabienie Odporności na Zazdrość
2. [Status [VioletResistDown] — opis] 대상의 질투 내성을 {0:F1} 증가
   źródło: Bufs.json :: dataList[id=VioletResistDown].desc
   limit: do 120 znaków
   EN: Increase Envy Resistance by {0:F1}
   PL: Zwiększa Odporność celu na Zazdrość o {0:F1}
3. [Status [CrimsonResistUp] — nazwa] 분노 내성 강화
   źródło: Bufs.json :: dataList[id=CrimsonResistUp].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonResistUp]`
   limit: do 40 znaków
   EN: Wrath Resist Up
   PL: Wzmocnienie Odporności na Gniew
4. [Status [ScarletResistUp] — nazwa] 색욕 내성 강화
   źródło: Bufs.json :: dataList[id=ScarletResistUp].name
   kontekst: identyfikator statusu w tekstach: `[ScarletResistUp]`
   limit: do 40 znaków
   EN: Lust Resist Up
   PL: Wzmocnienie Odporności na Żądzę
5. [Status [AmberResistUp] — nazwa] 나태 내성 강화
   źródło: Bufs.json :: dataList[id=AmberResistUp].name
   kontekst: identyfikator statusu w tekstach: `[AmberResistUp]`
   limit: do 40 znaków
   EN: Sloth Resist Up
   PL: Wzmocnienie Odporności na Lenistwo
6. [Status [ShamrockResistUp] — nazwa] 탐식 내성 강화
   źródło: Bufs.json :: dataList[id=ShamrockResistUp].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockResistUp]`
   limit: do 40 znaków
   EN: Gluttony Resist Up
   PL: Wzmocnienie Odporności na Obżarstwo
7. [Status [AzureResistUp] — nazwa] 우울 내성 강화
   źródło: Bufs.json :: dataList[id=AzureResistUp].name
   kontekst: identyfikator statusu w tekstach: `[AzureResistUp]`
   limit: do 40 znaków
   EN: Gloom Resist Up
   PL: Wzmocnienie Odporności na Posępność
8. [Status [IndigoResistUp] — nazwa] 오만 내성 강화
   źródło: Bufs.json :: dataList[id=IndigoResistUp].name
   kontekst: identyfikator statusu w tekstach: `[IndigoResistUp]`
   limit: do 40 znaków
   EN: Pride Resist Up
   PL: Wzmocnienie Odporności na Pychę
9. [Status [VioletResistUp] — nazwa] 질투 내성 강화
   źródło: Bufs.json :: dataList[id=VioletResistUp].name
   kontekst: identyfikator statusu w tekstach: `[VioletResistUp]`
   limit: do 40 znaków
   EN: Envy Resist Up
   PL: Wzmocnienie Odporności na Zazdrość
10. [Status [CrimsonDamageDown] — nazwa] 분노 피해량 감소
   źródło: Bufs.json :: dataList[id=CrimsonDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonDamageDown]`
   limit: do 40 znaków
   EN: Wrath DMG Down
   PL: Spadek Obrażeń Gniewu
11. [Status [CrimsonDamageDown] — opis] 이번 턴 동안 분노 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=CrimsonDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Wrath skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Gniewu w tej turze (maks. 100%)
12. [Status [CrimsonDamageDown] — podsumowanie] 분노 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=CrimsonDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath damage -{0}0%
   PL: Obrażenia Umiejętności Gniewu -{0}0%
13. [Status [ScarletDamageDown] — nazwa] 색욕 피해량 감소
   źródło: Bufs.json :: dataList[id=ScarletDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[ScarletDamageDown]`
   limit: do 40 znaków
   EN: Lust DMG Down
   PL: Spadek Obrażeń Żądzy
14. [Status [ScarletDamageDown] — opis] 이번 턴 동안 색욕 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ScarletDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Lust skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Żądzy w tej turze (maks. 100%)
15. [Status [ScarletDamageDown] — podsumowanie] 색욕 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=ScarletDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust damage -{0}0%
   PL: Obrażenia Umiejętności Żądzy -{0}0%
16. [Status [AmberDamageDown] — nazwa] 나태 피해량 감소
   źródło: Bufs.json :: dataList[id=AmberDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[AmberDamageDown]`
   limit: do 40 znaków
   EN: Sloth DMG Down
   PL: Spadek Obrażeń Lenistwa
17. [Status [AmberDamageDown] — opis] 이번 턴 동안 나태 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AmberDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Sloth skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Lenistwa w tej turze (maks. 100%)
18. [Status [AmberDamageDown] — podsumowanie] 나태 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=AmberDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth damage -{0}0%
   PL: Obrażenia Umiejętności Lenistwa -{0}0%
19. [Status [ShamrockDamageDown] — nazwa] 탐식 피해량 감소
   źródło: Bufs.json :: dataList[id=ShamrockDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockDamageDown]`
   limit: do 40 znaków
   EN: Gluttony DMG Down
   PL: Spadek Obrażeń Obżarstwa
20. [Status [ShamrockDamageDown] — opis] 이번 턴 동안 탐식 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ShamrockDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Gluttony skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Obżarstwa w tej turze (maks. 100%)
21. [Status [ShamrockDamageDown] — podsumowanie] 탐식 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=ShamrockDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony damage -{0}0%
   PL: Obrażenia Umiejętności Obżarstwa -{0}0%
22. [Status [AzureDamageDown] — nazwa] 우울 피해량 감소
   źródło: Bufs.json :: dataList[id=AzureDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[AzureDamageDown]`
   limit: do 40 znaków
   EN: Gloom DMG Down
   PL: Spadek Obrażeń Posępności
23. [Status [AzureDamageDown] — opis] 이번 턴 동안 우울 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AzureDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Gloom skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Posępności w tej turze (maks. 100%)
24. [Status [AzureDamageDown] — podsumowanie] 우울 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=AzureDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom damage -{0}0%
   PL: Obrażenia Umiejętności Posępności -{0}0%
25. [Status [IndigoDamageDown] — nazwa] 오만 피해량 감소
   źródło: Bufs.json :: dataList[id=IndigoDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[IndigoDamageDown]`
   limit: do 40 znaków
   EN: Pride DMG Down
   PL: Spadek Obrażeń Pychy
26. [Status [IndigoDamageDown] — opis] 이번 턴 동안 오만 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=IndigoDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Pride skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Pychy w tej turze (maks. 100%)
27. [Status [IndigoDamageDown] — podsumowanie] 오만 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=IndigoDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride damage -{0}0%
   PL: Obrażenia Umiejętności Pychy -{0}0%
28. [Status [VioletDamageDown] — nazwa] 질투 피해량 감소
   źródło: Bufs.json :: dataList[id=VioletDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[VioletDamageDown]`
   limit: do 40 znaków
   EN: Envy DMG Down
   PL: Spadek Obrażeń Zazdrości
29. [Status [VioletDamageDown] — opis] 이번 턴 동안 질투 속성 스킬로 가하는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=VioletDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal -{0}0% damage with Envy skills this turn. (Max 100%)
   PL: Zadaje -{0}0% obrażeń Umiejętnościami Zazdrości w tej turze (maks. 100%)
30. [Status [VioletDamageDown] — podsumowanie] 질투 속성 스킬로 가하는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=VioletDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy damage -{0}0%
   PL: Obrażenia Umiejętności Zazdrości -{0}0%
31. [Status [CrimsonDamageUp] — nazwa] 분노 피해량 증가
   źródło: Bufs.json :: dataList[id=CrimsonDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonDamageUp]`
   limit: do 40 znaków
   EN: Wrath DMG Up
   PL: Wzrost Obrażeń Gniewu
32. [Status [CrimsonDamageUp] — opis] 이번 턴 동안 분노 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=CrimsonDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Wrath skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Gniewu w tej turze (maks. 100%)
33. [Status [CrimsonDamageUp] — podsumowanie] 분노 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=CrimsonDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath damage +{0}0%
   PL: Obrażenia Umiejętności Gniewu +{0}0%
34. [Status [ScarletDamageUp] — nazwa] 색욕 피해량 증가
   źródło: Bufs.json :: dataList[id=ScarletDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[ScarletDamageUp]`
   limit: do 40 znaków
   EN: Lust DMG Up
   PL: Wzrost Obrażeń Żądzy
35. [Status [ScarletDamageUp] — opis] 이번 턴 동안 색욕 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ScarletDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Lust skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Żądzy w tej turze (maks. 100%)
36. [Status [ScarletDamageUp] — podsumowanie] 색욕 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=ScarletDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust damage +{0}0%
   PL: Obrażenia Umiejętności Żądzy +{0}0%
37. [Status [AmberDamageUp] — nazwa] 나태 피해량 증가
   źródło: Bufs.json :: dataList[id=AmberDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[AmberDamageUp]`
   limit: do 40 znaków
   EN: Sloth DMG Up
   PL: Wzrost Obrażeń Lenistwa
38. [Status [AmberDamageUp] — opis] 이번 턴 동안 나태 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AmberDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Sloth skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Lenistwa w tej turze (maks. 100%)
39. [Status [AmberDamageUp] — podsumowanie] 나태 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=AmberDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth damage +{0}0%
   PL: Obrażenia Umiejętności Lenistwa +{0}0%
40. [Status [ShamrockDamageUp] — nazwa] 탐식 피해량 증가
   źródło: Bufs.json :: dataList[id=ShamrockDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockDamageUp]`
   limit: do 40 znaków
   EN: Gluttony DMG Up
   PL: Wzrost Obrażeń Obżarstwa
41. [Status [ShamrockDamageUp] — opis] 이번 턴 동안 탐식 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ShamrockDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Gluttony skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Obżarstwa w tej turze (maks. 100%)
42. [Status [ShamrockDamageUp] — podsumowanie] 탐식 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=ShamrockDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony damage +{0}0%
   PL: Obrażenia Umiejętności Obżarstwa +{0}0%
43. [Status [AzureDamageUp] — nazwa] 우울 피해량 증가
   źródło: Bufs.json :: dataList[id=AzureDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[AzureDamageUp]`
   limit: do 40 znaków
   EN: Gloom DMG Up
   PL: Wzrost Obrażeń Posępności
44. [Status [AzureDamageUp] — opis] 이번 턴 동안 우울 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AzureDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Gloom skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Posępności w tej turze (maks. 100%)
45. [Status [AzureDamageUp] — podsumowanie] 우울 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=AzureDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom damage +{0}0%
   PL: Obrażenia Umiejętności Posępności +{0}0%
46. [Status [IndigoDamageUp] — nazwa] 오만 피해량 증가
   źródło: Bufs.json :: dataList[id=IndigoDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[IndigoDamageUp]`
   limit: do 40 znaków
   EN: Pride DMG Up
   PL: Wzrost Obrażeń Pychy
47. [Status [IndigoDamageUp] — opis] 이번 턴 동안 오만 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=IndigoDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Pride skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Pychy w tej turze (maks. 100%)
48. [Status [IndigoDamageUp] — podsumowanie] 오만 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=IndigoDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride damage +{0}0%
   PL: Obrażenia Umiejętności Pychy +{0}0%
49. [Status [VioletDamageUp] — nazwa] 질투 피해량 증가
   źródło: Bufs.json :: dataList[id=VioletDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[VioletDamageUp]`
   limit: do 40 znaków
   EN: Envy DMG Up
   PL: Wzrost Obrażeń Zazdrości
50. [Status [VioletDamageUp] — opis] 이번 턴 동안 질투 속성 스킬로 가하는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=VioletDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}0% damage with Envy skills this turn. (Max 100%)
   PL: Zadaje +{0}0% obrażeń Umiejętnościami Zazdrości w tej turze (maks. 100%)
51. [Status [VioletDamageUp] — podsumowanie] 질투 속성 스킬로 가하는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=VioletDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy damage +{0}0%
   PL: Obrażenia Umiejętności Zazdrości +{0}0%
52. [Status [Curse] — nazwa] 저주
   źródło: Bufs.json :: dataList[id=Curse].name
   kontekst: identyfikator statusu w tekstach: `[Curse]`
   limit: do 40 znaków
   EN: Curse
   PL: Klątwa
53. [Status [Curse] — opis] 턴 종료 시 다음 턴에 공격 위력 감소 1, 수비 위력 감소 1, 공격 레벨 감소 2, 방어 레벨 감소 2 중 무작위 1개의 효과를 얻고, 수치 1 감소
   źródło: Bufs.json :: dataList[id=Curse].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Next turn, randomly gain one of the following, then reduce this effect’s Count by 1.\n1 Attack Power Down/1 Defense Power Down/2 Offense Level Down/2 Defense Level Down.
   PL: Na koniec tury zyskuje na następną turę 1 losowy efekt spośród: 1 Spadek Mocy Ataku, 1 Spadek Mocy Obrony, 2 Spadki Poziomu Ataku, 2 Spadki Poziomu Obrony, po czym Licznik maleje o 1
54. [Status [Curse] — podsumowanie] 무작위 효과 얻음. 수치 1 감소
   źródło: Bufs.json :: dataList[id=Curse].summary
   limit: do 120 znaków
   EN: Gain a negative status effect, then reduce Count by 1
   PL: Zyskuje negatywny status, po czym wartość maleje o 1
55. [Status [AttackDmgUp_Weak] — nazwa] 약점 공격 시 피해 증가
   źródło: Bufs.json :: dataList[id=AttackDmgUp_Weak].name
   kontekst: identyfikator statusu w tekstach: `[AttackDmgUp_Weak]`
   limit: do 40 znaków
   EN: Weak-resist DMG Boost
   PL: Wzrost Obrażeń w Słabość
56. [Status [AttackDmgUp_Weak] — opis] 약점 공격 시 피해 {0}% 증가
   źródło: Bufs.json :: dataList[id=AttackDmgUp_Weak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Boost the damage of attacks against Weak resistances by {0}%
   PL: Zwiększa o {0}% obrażenia ataków trafiających słabość
57. [Status [AttackDmgUp_Weak] — podsumowanie] 약점 피해량 +{0}%
   źródło: Bufs.json :: dataList[id=AttackDmgUp_Weak].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}% damage to Weak resistances
   PL: Obrażenia w słabość +{0}%
58. [Status [Bullet] — nazwa] 탄환
   źródło: Bufs.json :: dataList[id=Bullet].name
   kontekst: identyfikator statusu w tekstach: `[Bullet]`
   limit: do 40 znaków
   EN: Ammo
   PL: Amunicja
59. [Status [Bullet] — opis] 특정 스킬에서 소모. 탄환이 없는 경우 스킬이 취소됨.
   źródło: Bufs.json :: dataList[id=Bullet].desc
   limit: do 120 znaków
   EN: Spent by certain skills. Some attacks cancel if lacking Ammo.
   PL: Zużywana przez określone Umiejętności. Przy braku amunicji Umiejętność zostaje anulowana.
60. [Status [Bullet] — podsumowanie] 탄환 소모
   źródło: Bufs.json :: dataList[id=Bullet].summary
   limit: do 120 znaków
   EN: Resource for certain skills
   PL: Zużycie amunicji
61. [Status [Meursault_Last_Remodeling] — nazwa] 마지막 개조
   źródło: Bufs.json :: dataList[id=Meursault_Last_Remodeling].name
   kontekst: identyfikator statusu w tekstach: `[Meursault_Last_Remodeling]`
   limit: do 40 znaków
   EN: Final Augment
   PL: Ostateczna Przeróbka
62. [Status [Meursault_Last_Remodeling] — opis] 매 턴마다 공격 위력 증가, 수비 위력 증가, 신속 3을 얻고, {0} 턴 뒤 사망함
   źródło: Bufs.json :: dataList[id=Meursault_Last_Remodeling].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn Start: Gain 3 Attack Power Up, Defense Power Up, and Haste; die in {0} turn(s).
   PL: Co turę zyskuje 3 Wzrosty Mocy Ataku, Wzrostu Mocy Obrony i Pośpiechu; umiera po {0} turach
63. [Status [Choice_90103301] — nazwa] 바둥거림
   źródło: Bufs.json :: dataList[id=Choice_90103301].name
   kontekst: identyfikator statusu w tekstach: `[Choice_90103301]`
   limit: do 40 znaków
   EN: Struggle
   PL: Wiercenie się
64. [Status [Choice_90103301] — opis] 이번 전투 동안 속도 +1
   źródło: Bufs.json :: dataList[id=Choice_90103301].desc
   limit: do 120 znaków
   EN: Speed +1 for this battle.
   PL: W tej walce Szybkość +1
65. [Status [Choice_90103301] — podsumowanie] 속도 +1
   źródło: Bufs.json :: dataList[id=Choice_90103301].summary
   limit: do 120 znaków
   EN: SPD +1
   PL: Szybkość +1
66. [Status [Choice_90103402] — nazwa] 후련함
   źródło: Bufs.json :: dataList[id=Choice_90103402].name
   kontekst: identyfikator statusu w tekstach: `[Choice_90103402]`
   limit: do 40 znaków
   EN: Relief
   PL: Ukojenie
67. [Status [Choice_90103402] — opis] 이번 전투 동안 속도 +2
   źródło: Bufs.json :: dataList[id=Choice_90103402].desc
   limit: do 120 znaków
   EN: Speed +2 for this battle.
   PL: W tej walce Szybkość +2
68. [Status [Choice_90103402] — podsumowanie] 속도 +2
   źródło: Bufs.json :: dataList[id=Choice_90103402].summary
   limit: do 120 znaków
   EN: SPD +2
   PL: Szybkość +2
69. [Status [Choice_901001] — nazwa] 불번짐
   źródło: Bufs.json :: dataList[id=Choice_901001].name
   kontekst: identyfikator statusu w tekstach: `[Choice_901001]`
   limit: do 40 znaków
   EN: Spreading Flame
   PL: Niegasnący Płomień
70. [Status [Choice_901001] — opis] 다음 전투에서 분노 속성 죄를 보유하지 않은 인격이 스테이지 시작 시, 분노 피해 5를 입음
   źródło: Bufs.json :: dataList[id=Choice_901001].desc
   limit: do 120 znaków
   EN: At the start of the next Encounter, allies without Wrath Affinity take 5 Wrath damage
   PL: W następnej walce Tożsamości bez Gniewu otrzymują na początku etapu 5 obrażeń Gniewu
71. [Status [Choice_901007] — nazwa] 나긋한 배웅
   źródło: Bufs.json :: dataList[id=Choice_901007].name
   kontekst: identyfikator statusu w tekstach: `[Choice_901007]`
   limit: do 40 znaków
   EN: Gentle Sendoff
   PL: Łagodne Pożegnanie
72. [Status [Choice_901007] — opis] 턴 시작 시 10만큼 체력과 정신력 회복 (최대 3턴)
   źródło: Bufs.json :: dataList[id=Choice_901007].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 10 HP and SP. (Up to 3 turns)
   PL: Na początku tury leczy 10 HP i 10 Poczytalności (do 3 tur)
73. [Status [Choice_901007] — podsumowanie] 체력, 정신력 +10
   źródło: Bufs.json :: dataList[id=Choice_901007].summary
   limit: do 120 znaków
   EN: HP & SP +10
   PL: HP i Poczytalność +10
74. [Status [Choice_901009] — nazwa] 명순응
   źródło: Bufs.json :: dataList[id=Choice_901009].name
   kontekst: identyfikator statusu w tekstach: `[Choice_901009]`
   limit: do 40 znaków
   EN: Photopia
   PL: Fotopia
75. [Status [Choice_901009] — opis] 다음 전투에서 모든 인격이 스킬 최종 위력 1 감소
   źródło: Bufs.json :: dataList[id=Choice_901009].desc
   limit: do 120 znaków
   EN: All Ally Units lose 1 Skill Final Power for the next Encounter
   PL: W następnej walce wszystkie Tożsamości mają Moc Końcową Umiejętności obniżoną o 1
76. [Status [Choice_901009] — podsumowanie] 스킬 최종 위력 -1
   źródło: Bufs.json :: dataList[id=Choice_901009].summary
   limit: do 120 znaków
   EN: Skill Final Power -1
   PL: Moc Końcowa Umiejętności -1
77. [Status [Choice_901010] — nazwa] 비워짐
   źródło: Bufs.json :: dataList[id=Choice_901010].name
   kontekst: identyfikator statusu w tekstach: `[Choice_901010]`
   limit: do 40 znaków
   EN: Emptied
   PL: Opróżnienie
78. [Status [Choice_901010] — opis] 전투 시작 시 색욕 공격 스킬을 보유하지 않은 인격이 흐트러짐 상태로 시작함
   źródło: Bufs.json :: dataList[id=Choice_901010].desc
   limit: do 120 znaków
   EN: Combat Start: Allies without Lust Affinity Attack Skill are Staggered.
   PL: Na początku walki Tożsamości bez Umiejętności ataku atrybutu Żądzy rozpoczynają w stanie Oszołomienia
79. [Status [Choice_901019] — nazwa] 오물
   źródło: Bufs.json :: dataList[id=Choice_901019].name
   kontekst: identyfikator statusu w tekstach: `[Choice_901019]`
   limit: do 40 znaków
   EN: Contamination
   PL: Zanieczyszczenie
80. [Status [Choice_901019] — opis] 전투 시작 시 속도 -2
   źródło: Bufs.json :: dataList[id=Choice_901019].desc
   limit: do 120 znaków
   EN: Combat Start: Speed -2.
   PL: Na początku walki Szybkość -2
81. [Status [Choice_901019] — podsumowanie] 속도 -2
   źródło: Bufs.json :: dataList[id=Choice_901019].summary
   limit: do 120 znaków
   EN: SPD -2
   PL: Szybkość -2
82. [Status [Choice_1030301] — nazwa] 선택지 효과
   źródło: Bufs.json :: dataList[id=Choice_1030301].name
   kontekst: identyfikator statusu w tekstach: `[Choice_1030301]`
   limit: do 40 znaków
   EN: Event Effect
   PL: Efekt wydarzenia
83. [Status [Choice_1030301] — opis] 전투 시작 시 공격 위력 증가 3 얻음
   źródło: Bufs.json :: dataList[id=Choice_1030301].desc
   limit: do 120 znaków
   EN: Combat Start: Gain 3 Attack Power Up.
   PL: Na początku walki zyskuje 3 Wzrosty Mocy Ataku
84. [Status [Choice_1030301] — podsumowanie] 공격 위력 증가 3 얻음
   źródło: Bufs.json :: dataList[id=Choice_1030301].summary
   limit: do 120 znaków
   EN: Gain 3 Attack Power Up
   PL: Zyskuje 3 Wzrosty Mocy Ataku
85. [Status [Choice_1030501] — nazwa] 선택지 효과
   źródło: Bufs.json :: dataList[id=Choice_1030501].name
   kontekst: identyfikator statusu w tekstach: `[Choice_1030501]`
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Status [Choice_1030501] — opis] 매 턴 공격 위력 감소 5 얻음
   źródło: Bufs.json :: dataList[id=Choice_1030501].desc
   limit: do 120 znaków
   EN: Gain 5 Attack Power Down each turn.
   PL: Co turę zyskuje 5 Spadków Mocy Ataku.
87. [Status [Choice_1030501] — podsumowanie] 공격 위력 감소 5 얻음
   źródło: Bufs.json :: dataList[id=Choice_1030501].summary
   limit: do 120 znaków
   EN: Gain 5 Attack Power Down
   PL: Zyskuje 5 Spadków Mocy Ataku
88. [Status [Choice_1031001] — nazwa] 선택지 효과
   źródło: Bufs.json :: dataList[id=Choice_1031001].name
   kontekst: identyfikator statusu w tekstach: `[Choice_1031001]`
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Status [Choice_1031001] — opis] 매 턴 피해량 감소 3 얻음
   źródło: Bufs.json :: dataList[id=Choice_1031001].desc
   limit: do 120 znaków
   EN: Gain 3 Damage Down each turn.
   PL: Co turę zyskuje 3 Spadki Obrażeń.
90. [Status [Choice_1031001] — podsumowanie] 피해량 감소 3 얻음
   źródło: Bufs.json :: dataList[id=Choice_1031001].summary
   limit: do 120 znaków
   EN: Gain 3 Damage Down
   PL: Zyskuje 3 Spadki Obrażeń
91. [Status [Assemble] — nazwa] 광신
   źródło: Bufs.json :: dataList[id=Assemble].name
   kontekst: identyfikator statusu w tekstach: `[Assemble]`
   limit: do 40 znaków
   EN: Fanatic
   PL: Fanatyzm
92. [Status [Assemble] — opis] 이번 턴 동안 못이 부여된 대상 공격 시 최종 위력 +{0} (합 진행 시에도 적용됨)
   źródło: Bufs.json :: dataList[id=Assemble].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power +{0} against units that have Nails for this turn. (Applies to clashes as well)
   PL: W tej turze Moc Końcowa przy atakowaniu celów z Gwoździem rośnie o {0} (działa także podczas Stareć)
93. [Status [Assemble] — podsumowanie] 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=Assemble].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Final Power +{0}
   PL: Moc Końcowa +{0}
94. [Status [ReinforcedAssemble] — nazwa] 크로머의 휘파람
   źródło: Bufs.json :: dataList[id=ReinforcedAssemble].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedAssemble]`
   limit: do 40 znaków
   EN: Kromer’s Whistles
   PL: Gwizdki Kromer
95. [Status [ReinforcedAssemble] — opis] 쥐는 자께서 함께하시니 두려움 없도다.
   źródło: Bufs.json :: dataList[id=ReinforcedAssemble].desc
   limit: do 120 znaków
   EN: We shall fear not, for the One Who Grips is with us.
   PL: Nie będziemy się bać, albowiem Ta, Która Ściska, jest z nami.
96. [Status [Greedy] — nazwa] 탐욕
   źródło: Bufs.json :: dataList[id=Greedy].name
   kontekst: identyfikator statusu w tekstach: `[Greedy]`
   limit: do 40 znaków
   EN: Desirous
   PL: Chciwość
97. [Status [Greedy] — opis] 이번 턴 동안 취약 2,  속박  10를 얻음. 스킬 슬롯이 1 증가하며, 스킬 패턴이 변경됨.
   źródło: Bufs.json :: dataList[id=Greedy].desc
   limit: do 120 znaków
   EN: Gain 2 Fragile and 10 Bind this turn. Also, gain a skill slot and change behavior.
   PL: W tej turze zyskuje 2 Wrażliwości i 10 Spętań. Zyskuje 1 slot Umiejętności, a wzorzec Umiejętności ulega zmianie.
98. [Status [Greedy] — podsumowanie] 취약 2, 속박 10 얻음
   źródło: Bufs.json :: dataList[id=Greedy].summary
   limit: do 120 znaków
   EN: Gain 2 Fragile and 10 Bind
   PL: Zyskuje 2 Wrażliwości i 10 Spętań
99. [Status [Desire] — nazwa] 욕망
   źródło: Bufs.json :: dataList[id=Desire].name
   kontekst: identyfikator statusu w tekstach: `[Desire]`
   limit: do 40 znaków
   EN: Urge
   PL: Pożądanie
100. [Status [Desire] — opis] 턴 종료 시 스택이 5 이상이면 정신력 피해를 30 받고, 다음 턴에 취약 2, 속박 10을 얻은 뒤 버프 소멸.
   źródło: Bufs.json :: dataList[id=Desire].desc
   limit: do 130 znaków
   EN: Turn End: At 5+ Stack, take 30 SP damage, gain 2 Fragile and 10 Bind, and remove this effect.
   PL: Na koniec tury przy 5+ stosach: 30 obrażeń Poczytalności, 2 Wrażliwości i 10 Spętań w następnej turze, po czym znika.
101. [Status [Desire] — podsumowanie] 정신력 피해 -30, 취약 2, 속박 10 얻음
   źródło: Bufs.json :: dataList[id=Desire].summary
   limit: do 120 znaków
   EN: Take 30 SP damage & gain 2 Fragile and 10 Bind
   PL: Obrażenia Poczytalności -30, zyskuje 2 Wrażliwości i 10 Spętań
102. [Status [GreedyReady] — nazwa] 조여드는 욕망
   źródło: Bufs.json :: dataList[id=GreedyReady].name
   kontekst: identyfikator statusu w tekstach: `[GreedyReady]`
   limit: do 40 znaków
   EN: Constricting Desires
   PL: Ściskające Żądze
103. [Status [GreedyReady] — opis] {0}턴 후에 탐욕 상태가 되는 스킬을 사용함
   źródło: Bufs.json :: dataList[id=GreedyReady].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Use a skill that applies ‘Desirous’ in {0} turn(s).
   PL: Po {0} turach użyje Umiejętności, która wprowadza w stan Chciwości
104. [Status [Decay] — nazwa] 썩어가는 피부
   źródło: Bufs.json :: dataList[id=Decay].name
   kontekst: identyfikator statusu w tekstach: `[Decay]`
   limit: do 40 znaków
   EN: Rotting Skin
   PL: Gnijąca Skóra
105. [Status [Decay] — opis] 피격 시 공격자에게 독 3 부여
   źródło: Bufs.json :: dataList[id=Decay].desc
   limit: do 120 znaków
   EN: When attacked, inflict 3 Poison on the attacker.
   PL: Przy trafieniu nadaje atakującemu Truciznę 3
106. [Status [Decay] — podsumowanie] 피격 시 독 3 부여
   źródło: Bufs.json :: dataList[id=Decay].summary
   limit: do 120 znaków
   EN: Inflict 3 Poison on attacker
   PL: Nadaje atakującemu Truciznę 3
107. [Status [Poison] — nazwa] 독
   źródło: Bufs.json :: dataList[id=Poison].name
   kontekst: identyfikator statusu w tekstach: `[Poison]`
   limit: do 40 znaków
   EN: Poison
   PL: Trucizna
108. [Status [Poison] — opis] 턴 종료 시 피해를 {0} 주고, 수치가 반으로 감소
   źródło: Bufs.json :: dataList[id=Poison].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Take {0} fixed damage, then halve the Count.
   PL: Na koniec tury otrzymuje {0} obrażeń, a wartość maleje o połowę
109. [Status [Poison] — podsumowanie] 체력 피해 -{0}
   źródło: Bufs.json :: dataList[id=Poison].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} HP damage
   PL: Obrażenia HP -{0}
110. [Status [Cromer_Target] — nazwa] 쥐는 자의 주시
   źródło: Bufs.json :: dataList[id=Cromer_Target].name
   kontekst: identyfikator statusu w tekstach: `[Cromer_Target]`
   limit: do 40 znaków
   EN: Gaze of the One Who Grips
   PL: Spojrzenie Tej, Która Ściska
111. [Status [Cromer_Target] — opis] 이번 턴 동안 흐트러짐 상태가 되고, 크로머에게 받는 피해량 +100%
   źródło: Bufs.json :: dataList[id=Cromer_Target].desc
   limit: do 120 znaków
   EN: Staggered for this turn. Take +100% damage from Kromer.
   PL: W tej turze popada w stan Oszołomienia i otrzymuje +100% obrażeń od Kromer
112. [Status [Cromer_Boredom] — nazwa] 고통을 받아들여!
   źródło: Bufs.json :: dataList[id=Cromer_Boredom].name
   kontekst: identyfikator statusu w tekstach: `[Cromer_Boredom]`
   limit: do 40 znaków
   EN: Accept the Pain!
   PL: Zaakceptuj ból!
113. [Status [Cromer_Boredom] — opis] 받는 피해량, 가하는 피해량 +100%. 수비 스킬 최종 위력 -5.
   źródło: Bufs.json :: dataList[id=Cromer_Boredom].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal and take 100% more damage.\nDefense Skill Final Power -5.
   PL: Zadaje i otrzymuje +100% obrażeń. Moc Końcowa Umiejętności obrony -5.
114. [Status [Cromer_Ecstasy] — nazwa] 희열
   źródło: Bufs.json :: dataList[id=Cromer_Ecstasy].name
   kontekst: identyfikator statusu w tekstach: `[Cromer_Ecstasy]`
   limit: do 40 znaków
   EN: Ecstatic
   PL: Uniesienie
115. [Status [Cromer_Ecstasy] — opis] 입 부위의 모든 물리 내성이 취약으로 변경됨.
   źródło: Bufs.json :: dataList[id=Cromer_Ecstasy].desc
   limit: do 120 znaków
   EN: All the Maw’s physical resistances change to ‘Fatal’.
   PL: Wszystkie Odporności fizyczne Paszczy zmieniają się na „Wrażliwość”
116. [Status [Cromer_Ecstasy] — podsumowanie] 부위 물리 내성 취약
   źródło: Bufs.json :: dataList[id=Cromer_Ecstasy].summary
   limit: do 120 znaków
   EN: Weaken part’s phys. resist
   PL: Słabość fizycznej odporności części
117. [Status [Cromer_Madness] — nazwa] 순수
   źródło: Bufs.json :: dataList[id=Cromer_Madness].name
   kontekst: identyfikator statusu w tekstach: `[Cromer_Madness]`
   limit: do 40 znaków
   EN: Purity
   PL: Czystość
118. [Status [Cromer_Madness] — opis] 모든 부위가 속박 3, 피해량 증가 3을 얻고, 모든 물리 내성이 취약으로 변경됨.
   źródło: Bufs.json :: dataList[id=Cromer_Madness].desc
   limit: do 120 znaków
   EN: All parts gain 3 Bind and 3 Damage Up, and their phys. resistances change to ‘Fatal’.
   PL: Wszystkie części zyskują 3 Spętań i 3 Wzrosty Obrażeń, a ich Odporności fizyczne zmieniają się na „Wrażliwość”
119. [Status [Hardening] — nazwa] 경화
   źródło: Bufs.json :: dataList[id=Hardening].name
   kontekst: identyfikator statusu w tekstach: `[Hardening]`
   limit: do 40 znaków
   EN: Hardening
   PL: Stwardnienie
120. [Status [Hardening] — opis] 턴 시작 시 수치가 3 이상이면, 팔이 완전한 상태로 변경됨.
   źródło: Bufs.json :: dataList[id=Hardening].desc
   limit: do 120 znaków
   EN: Turn Start: At 3+ Count, the Arms change into a “perfect” state.
   PL: Na początek tury przy wartości 3 lub więcej Ramiona zmieniają się w stan „Doskonały”.
121. [Status [Perfected] — nazwa] 완전한 껍데기
   źródło: Bufs.json :: dataList[id=Perfected].name
   kontekst: identyfikator statusu w tekstach: `[Perfected]`
   limit: do 40 znaków
   EN: Perfect Shell
   PL: Doskonała Powłoka
122. [Status [Perfected] — opis] 매 턴마다 팔이 공격 위력 증가 2를 얻음. 팔의 체력이 50% 미만이 되면 해제됨.
   źródło: Bufs.json :: dataList[id=Perfected].desc
   limit: do 120 znaków
   EN: Turn Start: The Arms gain 2 Attack Power Up. Removed when the Arms’ HP falls below 50%
   PL: Co turę Ramiona zyskują 2 Wzrosty Mocy Ataku. Znika, gdy HP Ramion spadnie poniżej 50%
123. [Status [Perfected] — podsumowanie] 공격 위력 증가 2 얻음
   źródło: Bufs.json :: dataList[id=Perfected].summary
   limit: do 120 znaków
   EN: Gain 2 Attack Power Up
   PL: Zyskuje 2 Wzrosty Mocy Ataku
124. [Status [Enrage] — nazwa] 광란
   źródło: Bufs.json :: dataList[id=Enrage].name
   kontekst: identyfikator statusu w tekstach: `[Enrage]`
   limit: do 40 znaków
   EN: Frenzy
   PL: Furia
125. [Status [Enrage] — opis] 이번 턴동안 공격 위력 증가 3, 취약 3을 얻고, 스킬 패턴이 변경됨. 피격 시 본능을 얻지 않음.
   źródło: Bufs.json :: dataList[id=Enrage].desc
   limit: do 140 znaków
   EN: Gain 3 Attack Power Up and 3 Fragile this turn, and change behavior. Does not gain Instincts when attacked.
   PL: W tej turze zyskuje 3 Wzrosty Mocy Ataku i 3 Wrażliwości, a wzorce Umiejętności się zmieniają. Nie zyskuje Instynktu przy trafieniu.
126. [Status [Enrage] — podsumowanie] 공격 위력 증가 3, 취약 3 얻음
   źródło: Bufs.json :: dataList[id=Enrage].summary
   limit: do 120 znaków
   EN: Gain 3 Attack Power Up & 3 Fragile
   PL: Zyskuje 3 Wzrosty Mocy Ataku i 3 Wrażliwości
127. [Status [Aggressive] — nazwa] 본능
   źródło: Bufs.json :: dataList[id=Aggressive].name
   kontekst: identyfikator statusu w tekstach: `[Aggressive]`
   limit: do 40 znaków
   EN: Instincts
   PL: Instynkt
128. [Status [Aggressive] — opis] 턴 종료 시 수치가 4 이상이면 상태가 공격적으로 변경됨.
   źródło: Bufs.json :: dataList[id=Aggressive].desc
   limit: do 120 znaków
   EN: Turn End: At 4+ Stack, change to an “aggressive” state.
   PL: Na koniec tury, przy 4 lub więcej stosach, przechodzi w stan agresywny.
129. [Status [Whistle_Courage] — nazwa] 공포를 이기는 용기
   źródło: Bufs.json :: dataList[id=Whistle_Courage].name
   kontekst: identyfikator statusu w tekstach: `[Whistle_Courage]`
   limit: do 40 znaków
   EN: Courage to Triumph Fear
   PL: Odwaga Pokonująca Strach
130. [Status [Whistle_Courage] — opis] 매 턴마다 공격 위력 증가 1, 보호 2를 얻음
   źródło: Bufs.json :: dataList[id=Whistle_Courage].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Attack Power Up and 2 Protection.
   PL: Co turę zyskuje 1 Wzrost Mocy Ataku i 2 Ochrony
131. [Status [Whistle_Courage] — podsumowanie] 공격 위력 증가 1, 보호 2 얻음
   źródło: Bufs.json :: dataList[id=Whistle_Courage].summary
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up & 2 Protection
   PL: Zyskuje 1 Wzrost Mocy Ataku i 2 Ochrony
132. [Status [Whistle_Fear] — nazwa] 휘파람의 공포
   źródło: Bufs.json :: dataList[id=Whistle_Fear].name
   kontekst: identyfikator statusu w tekstach: `[Whistle_Fear]`
   limit: do 40 znaków
   EN: Fearsome Whistles
   PL: Przerażające Gwizdki
133. [Status [Whistle_Fear] — opis] 매 턴마다 속박 1, 마비 1을 얻음
   źródło: Bufs.json :: dataList[id=Whistle_Fear].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Bind and 1 Paralyze.
   PL: Co turę zyskuje 1 Spętania i 1 Paraliżu
134. [Status [Whistle_Fear] — podsumowanie] 속박 1, 마비 1 얻음
   źródło: Bufs.json :: dataList[id=Whistle_Fear].summary
   limit: do 120 znaków
   EN: Gain 1 Bind & 1 Paralyze
   PL: Zyskuje 1 Spętania i 1 Paraliżu
135. [Status [SlashTakeDamageDown] — nazwa] 참격 보호
   źródło: Bufs.json :: dataList[id=SlashTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[SlashTakeDamageDown]`
   limit: do 40 znaków
   EN: Slash Protection
   PL: Ochrona przed Cięciem
136. [Status [SlashTakeDamageDown] — opis] 이번 턴 동안 참격 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=SlashTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Slash skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Cięcia (maks. 100%)
137. [Status [SlashTakeDamageDown] — podsumowanie] 참격 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=SlashTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash damage taken -{0}0%
   PL: Obrażenia od Umiejętności Cięcia -{0}0%
138. [Status [PenetrateTakeDamageDown] — nazwa] 관통 보호
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateTakeDamageDown]`
   limit: do 40 znaków
   EN: Pierce Protection
   PL: Ochrona przed Przebiciem
139. [Status [PenetrateTakeDamageDown] — opis] 이번 턴 동안 관통 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Pierce skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Przebicia (maks. 100%)
140. [Status [PenetrateTakeDamageDown] — podsumowanie] 관통 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce damage taken -{0}0%
   PL: Obrażenia od Umiejętności Przebicia -{0}0%
141. [Status [HitTakeDamageDown] — nazwa] 타격 보호
   źródło: Bufs.json :: dataList[id=HitTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[HitTakeDamageDown]`
   limit: do 40 znaków
   EN: Blunt Protection
   PL: Ochrona przed Uderzeniem
142. [Status [HitTakeDamageDown] — opis] 이번 턴 동안 타격 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=HitTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Blunt skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Uderzenia (maks. 100%)
143. [Status [HitTakeDamageDown] — podsumowanie] 타격 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=HitTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt damage taken -{0}0%
   PL: Obrażenia od Umiejętności Uderzenia -{0}0%
144. [Status [CrimsonTakeDamageDown] — nazwa] 분노 보호
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonTakeDamageDown]`
   limit: do 40 znaków
   EN: Wrath Protection
   PL: Ochrona przed Gniewem
145. [Status [CrimsonTakeDamageDown] — opis] 이번 턴 동안 분노 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Wrath skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Gniewu (maks. 100%)
146. [Status [CrimsonTakeDamageDown] — podsumowanie] 분노 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath damage taken -{0}0%
   PL: Obrażenia od Umiejętności Gniewu -{0}0%
147. [Status [ScarletTakeDamageDown] — nazwa] 색욕 보호
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[ScarletTakeDamageDown]`
   limit: do 40 znaków
   EN: Lust Protection
   PL: Ochrona przed Żądzą
148. [Status [ScarletTakeDamageDown] — opis] 이번 턴 동안 색욕 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Lust skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Żądzy (maks. 100%)
149. [Status [ScarletTakeDamageDown] — podsumowanie] 색욕 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust damage taken -{0}0%
   PL: Obrażenia od Umiejętności Żądzy -{0}0%
150. [Status [AmberTakeDamageDown] — nazwa] 나태 보호
   źródło: Bufs.json :: dataList[id=AmberTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[AmberTakeDamageDown]`
   limit: do 40 znaków
   EN: Sloth Protection
   PL: Ochrona przed Lenistwem
151. [Status [AmberTakeDamageDown] — opis] 이번 턴 동안 나태 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AmberTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Sloth skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Lenistwa (maks. 100%)
152. [Status [AmberTakeDamageDown] — podsumowanie] 나태 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=AmberTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth damage taken -{0}0%
   PL: Obrażenia od Umiejętności Lenistwa -{0}0%
153. [Status [ShamrockTakeDamageDown] — nazwa] 탐식 보호
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockTakeDamageDown]`
   limit: do 40 znaków
   EN: Gluttony Protection
   PL: Ochrona przed Obżarstwem
154. [Status [ShamrockTakeDamageDown] — opis] 이번 턴 동안 탐식 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Gluttony skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Obżarstwa (maks. 100%)
155. [Status [ShamrockTakeDamageDown] — podsumowanie] 탐식 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony damage taken -{0}0%
   PL: Obrażenia od Umiejętności Obżarstwa -{0}0%
156. [Status [AzureTakeDamageDown] — nazwa] 우울 보호
   źródło: Bufs.json :: dataList[id=AzureTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[AzureTakeDamageDown]`
   limit: do 40 znaków
   EN: Gloom Protection
   PL: Ochrona przed Posępnością
157. [Status [AzureTakeDamageDown] — opis] 이번 턴 동안 우울 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AzureTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Gloom skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Posępności (maks. 100%)
158. [Status [AzureTakeDamageDown] — podsumowanie] 우울 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=AzureTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom damage taken -{0}0%
   PL: Obrażenia od Umiejętności Posępności -{0}0%
159. [Status [IndigoTakeDamageDown] — nazwa] 오만 보호
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[IndigoTakeDamageDown]`
   limit: do 40 znaków
   EN: Pride Protection
   PL: Ochrona przed Pychą
160. [Status [IndigoTakeDamageDown] — opis] 이번 턴 동안 오만 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Pride skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Pychy (maks. 100%)
161. [Status [IndigoTakeDamageDown] — podsumowanie] 오만 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride damage taken -{0}0%
   PL: Obrażenia od Umiejętności Pychy -{0}0%
162. [Status [VioletTakeDamageDown] — nazwa] 질투 보호
   źródło: Bufs.json :: dataList[id=VioletTakeDamageDown].name
   kontekst: identyfikator statusu w tekstach: `[VioletTakeDamageDown]`
   limit: do 40 znaków
   EN: Envy Protection
   PL: Ochrona przed Zazdrością
163. [Status [VioletTakeDamageDown] — opis] 이번 턴 동안 질투 속성 스킬로 받는 피해량 -{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=VioletTakeDamageDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0}0% damage from Envy skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze -{0}0% obrażeń od Umiejętności Zazdrości (maks. 100%)
164. [Status [VioletTakeDamageDown] — podsumowanie] 질투 속성 스킬로 받는 피해량 -{0}0%
   źródło: Bufs.json :: dataList[id=VioletTakeDamageDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy damage taken -{0}0%
   PL: Obrażenia od Umiejętności Zazdrości -{0}0%
165. [Status [SlashTakeDamageUp] — nazwa] 참격 취약
   źródło: Bufs.json :: dataList[id=SlashTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[SlashTakeDamageUp]`
   limit: do 40 znaków
   EN: Slash Fragility
   PL: Wrażliwość na Cięcie
166. [Status [SlashTakeDamageUp] — opis] 이번 턴 동안 참격 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=SlashTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Slash skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Cięcia (maks. 100%)
167. [Status [SlashTakeDamageUp] — podsumowanie] 참격 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=SlashTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash damage taken +{0}0%
   PL: Obrażenia od Umiejętności Cięcia +{0}0%
168. [Status [PenetrateTakeDamageUp] — nazwa] 관통 취약
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateTakeDamageUp]`
   limit: do 40 znaków
   EN: Pierce Fragility
   PL: Wrażliwość na Przebicie
169. [Status [PenetrateTakeDamageUp] — opis] 이번 턴 동안 관통 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Pierce skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Przebicia (maks. 100%)
170. [Status [PenetrateTakeDamageUp] — podsumowanie] 관통 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=PenetrateTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce damage taken +{0}0%
   PL: Obrażenia od Umiejętności Przebicia +{0}0%
171. [Status [HitTakeDamageUp] — nazwa] 타격 취약
   źródło: Bufs.json :: dataList[id=HitTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[HitTakeDamageUp]`
   limit: do 40 znaków
   EN: Blunt Fragility
   PL: Wrażliwość na Uderzenie
172. [Status [HitTakeDamageUp] — opis] 이번 턴 동안 타격 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=HitTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Blunt skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Uderzenia (maks. 100%)
173. [Status [HitTakeDamageUp] — podsumowanie] 타격 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=HitTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt damage taken +{0}0%
   PL: Obrażenia od Umiejętności Uderzenia +{0}0%
174. [Status [CrimsonTakeDamageUp] — nazwa] 분노 취약
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonTakeDamageUp]`
   limit: do 40 znaków
   EN: Wrath Fragility
   PL: Wrażliwość na Gniew
175. [Status [CrimsonTakeDamageUp] — opis] 이번 턴 동안 분노 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Wrath skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Gniewu (maks. 100%)
176. [Status [CrimsonTakeDamageUp] — podsumowanie] 분노 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=CrimsonTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath damage taken +{0}0%
   PL: Obrażenia od Umiejętności Gniewu +{0}0%
177. [Status [ScarletTakeDamageUp] — nazwa] 색욕 취약
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[ScarletTakeDamageUp]`
   limit: do 40 znaków
   EN: Lust Fragility
   PL: Wrażliwość na Żądzę
178. [Status [ScarletTakeDamageUp] — opis] 이번 턴 동안 색욕 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Lust skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Żądzy (maks. 100%)
179. [Status [ScarletTakeDamageUp] — podsumowanie] 색욕 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=ScarletTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust damage taken +{0}0%
   PL: Obrażenia od Umiejętności Żądzy +{0}0%
180. [Status [AmberTakeDamageUp] — nazwa] 나태 취약
   źródło: Bufs.json :: dataList[id=AmberTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[AmberTakeDamageUp]`
   limit: do 40 znaków
   EN: Sloth Fragility
   PL: Wrażliwość na Lenistwo
181. [Status [AmberTakeDamageUp] — opis] 이번 턴 동안 나태 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AmberTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Sloth skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Lenistwa (maks. 100%)
182. [Status [AmberTakeDamageUp] — podsumowanie] 나태 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=AmberTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth damage taken +{0}0%
   PL: Obrażenia od Umiejętności Lenistwa +{0}0%
183. [Status [ShamrockTakeDamageUp] — nazwa] 탐식 취약
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockTakeDamageUp]`
   limit: do 40 znaków
   EN: Gluttony Fragility
   PL: Wrażliwość na Obżarstwo
184. [Status [ShamrockTakeDamageUp] — opis] 이번 턴 동안 탐식 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Gluttony skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Obżarstwa (maks. 100%)
185. [Status [ShamrockTakeDamageUp] — podsumowanie] 탐식 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=ShamrockTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony damage taken +{0}0%
   PL: Obrażenia od Umiejętności Obżarstwa +{0}0%
186. [Status [AzureTakeDamageUp] — nazwa] 우울 취약
   źródło: Bufs.json :: dataList[id=AzureTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[AzureTakeDamageUp]`
   limit: do 40 znaków
   EN: Gloom Fragility
   PL: Wrażliwość na Posępność
187. [Status [AzureTakeDamageUp] — opis] 이번 턴 동안 우울 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=AzureTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Gloom skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Posępności (maks. 100%)
188. [Status [AzureTakeDamageUp] — podsumowanie] 우울 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=AzureTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom damage taken +{0}0%
   PL: Obrażenia od Umiejętności Posępności +{0}0%
189. [Status [IndigoTakeDamageUp] — nazwa] 오만 취약
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[IndigoTakeDamageUp]`
   limit: do 40 znaków
   EN: Pride Fragility
   PL: Wrażliwość na Pychę
190. [Status [IndigoTakeDamageUp] — opis] 이번 턴 동안 오만 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Pride skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Pychy (maks. 100%)
191. [Status [IndigoTakeDamageUp] — podsumowanie] 오만 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=IndigoTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride damage taken +{0}0%
   PL: Obrażenia od Umiejętności Pychy +{0}0%
192. [Status [VioletTakeDamageUp] — nazwa] 질투 취약
   źródło: Bufs.json :: dataList[id=VioletTakeDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[VioletTakeDamageUp]`
   limit: do 40 znaków
   EN: Envy Fragility
   PL: Wrażliwość na Zazdrość
193. [Status [VioletTakeDamageUp] — opis] 이번 턴 동안 질투 속성 스킬로 받는 피해량 +{0}0% (최대 10)
   źródło: Bufs.json :: dataList[id=VioletTakeDamageUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}0% damage from Envy skills this turn. (Max 100%)
   PL: Otrzymuje w tej turze +{0}0% obrażeń od Umiejętności Zazdrości (maks. 100%)
194. [Status [VioletTakeDamageUp] — podsumowanie] 질투 속성 스킬로 받는 피해량 +{0}0%
   źródło: Bufs.json :: dataList[id=VioletTakeDamageUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy damage taken +{0}0%
   PL: Obrażenia od Umiejętności Zazdrości +{0}0%
195. [Status [LittleCourage] — nazwa] 어느 표지
   źródło: Bufs.json :: dataList[id=LittleCourage].name
   kontekst: identyfikator statusu w tekstach: `[LittleCourage]`
   limit: do 40 znaków
   EN: A Sign
   PL: Pewien Znak
196. [Status [LittleCourage] — opis] 크로머에 맞서고자 하는 싱클레어의 마음. 획이 3번 그어지면...
   źródło: Bufs.json :: dataList[id=LittleCourage].desc
   limit: do 120 znaków
   EN: Sinclair’s determination to stand up to Kromer. Once three strokes have been drawn…
   PL: Zdeterminowanie Sinclaira, by stawić czoła Kromer. Gdy trzy kreski zostaną naniesione...
197. [Status [LittleCourage] — podsumowanie] 싱클레어의 마음
   źródło: Bufs.json :: dataList[id=LittleCourage].summary
   limit: do 120 znaków
   EN: Sinclair’s Will
   PL: Wola Sinclaira
198. [Status [NailPersonality] — nazwa] 못
   źródło: Bufs.json :: dataList[id=NailPersonality].name
   kontekst: identyfikator statusu w tekstach: `[NailPersonality]`
   limit: do 40 znaków
   EN: Nails
   PL: Gwóźdź
199. [Status [NailPersonality] — opis] 특수 출혈\n턴 시작 시 출혈 1을 얻고, 출혈 횟수가 {0} 증가. 턴 종료 시 수치가 절반으로 감소 (소수점 버림)
   źródło: Bufs.json :: dataList[id=NailPersonality].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Unique Bleed\nTurn Start: Gain 1 Bleed and increase the Bleed Count by {0}.\nTurn End: Halve this effect’s Count. (Rounded down)
   PL: Specjalne Krwawienie\nNa początek tury zyskuje Krwawienie 1, a Licznik Krwawienia rośnie o {0}. Na koniec tury wartość maleje o połowę (zaokrąglona w dół)
200. [Status [NailPersonality] — podsumowanie] 출혈 1 얻음. 출혈 횟수 {0} 증가
   źródło: Bufs.json :: dataList[id=NailPersonality].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain 1 Bleed and add +{0} Bleed Count
   PL: Zyskuje Krwawienie 1. Licznik Krwawienia rośnie o {0}
201. [Status [AssemblePersonality] — nazwa] 광신
   źródło: Bufs.json :: dataList[id=AssemblePersonality].name
   kontekst: identyfikator statusu w tekstach: `[AssemblePersonality]`
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Status [AssemblePersonality] — opis] 이번 턴 동안 못이 있는 대상 공격 시 최종 위력 +{0} (합 진행 시에도 적용됨)
   źródło: Bufs.json :: dataList[id=AssemblePersonality].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power +{0} against units that have Nails for this turn. (Applies to clashes as well)
   PL: W tej turze Moc Końcowa przy atakowaniu celów z Gwoździem rośnie o {0} (działa także podczas Stareć)
203. [Status [AssemblePersonality] — podsumowanie] 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=AssemblePersonality].summary
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Status [MarkOfHeresy] — nazwa] 주시
   źródło: Bufs.json :: dataList[id=MarkOfHeresy].name
   kontekst: identyfikator statusu w tekstach: `[MarkOfHeresy]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
205. [Status [MarkOfHeresy] — opis] 이번 턴동안 관통, 타격 속성 스킬로 받는 피해 +20%. 표적이 찍힌 적 처치 시 처치한 아군의 정신력 10 회복되며, 해당 아군이 N사 광신도면 다음 턴에 광신 1을 얻음
   źródło: Bufs.json :: dataList[id=MarkOfHeresy].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +20% damage from Pierce and Blunt skills this turn.\nThe ally that defeats the marked unit heals 10 SP; if the ally is an 'N Corp. Fanatic', also apply 1 Fanatic next turn.
   PL: W tej turze otrzymuje +20% obrażeń od Umiejętności Przebicia i Uderzenia. Sojusznik, który zabije oznaczonego wroga, odzyskuje 10 Poczytalności; jeśli tym sojusznikiem jest Fanatyk Korp. N, zyskuje w następnej turze 1 Fanatyzmu
206. [Status [MarkOfHeresy] — podsumowanie] 관통, 타격 속성 스킬로 받는 피해 +20%
   źródło: Bufs.json :: dataList[id=MarkOfHeresy].summary
   limit: do 120 znaków
   EN: Pierce & Blunt damage taken +20%
   PL: Otrzymuje +20% obrażeń od Umiejętności Przebicia i Uderzenia
207. [Status [HitResultUp] — nazwa] 타격 위력 증가
   źródło: Bufs.json :: dataList[id=HitResultUp].name
   kontekst: identyfikator statusu w tekstach: `[HitResultUp]`
   limit: do 40 znaków
   EN: Blunt Power Up
   PL: Wzrost Mocy Uderzenia
208. [Status [HitResultUp] — opis] 이번 턴 동안 타격 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=HitResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Uderzenia +{0}
209. [Status [HitResultUp] — podsumowanie] 타격 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=HitResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Uderzenia +{0}
210. [Status [WeaknessAnalysis] — nazwa] 약점 분석
   źródło: Bufs.json :: dataList[id=WeaknessAnalysis].name
   kontekst: identyfikator statusu w tekstach: `[WeaknessAnalysis]`
   limit: do 40 znaków
   EN: Weakness Analyzed
   PL: Przeanalizowana Słabość
211. [Status [WeaknessAnalysis] — opis] 이번 턴 동안 공격 유형 내성에서 '견딤', '보통' 내성 중 무작위 하나를 선택하여 약화[+0.2]시킴
   źródło: Bufs.json :: dataList[id=WeaknessAnalysis].desc
   limit: do 140 znaków
   EN: A random “Endure” or “Normal” attack type resistance is weakened [+0.2 to damage multiplier] for this turn.
   PL: W tej turze jedna z Odporności na typy ataków o wartości „Znośna” lub „Zwykła” zostaje losowo osłabiona [+0,2 do mnożnika obrażeń]
212. [Status [WeaknessAnalysis] — podsumowanie] '견딤', '보통' 내성 중 1개 약화[+0.2]
   źródło: Bufs.json :: dataList[id=WeaknessAnalysis].summary
   limit: do 120 znaków
   EN: Weaken [+0.2 dmg multi] an “Endured” or “Normal” resistance
   PL: Osłabienie [+0,2 do mnożnika obrażeń] jednej z Odporności „Znośna” lub „Zwykła”
213. [Status [Cycle] — nazwa] 업보
   źródło: Bufs.json :: dataList[id=Cycle].name
   kontekst: identyfikator statusu w tekstach: `[Cycle]`
   limit: do 40 znaków
   EN: Karma
   PL: Karma
214. [Status [Cycle] — opis] 받는 피해량 +{0}%. 턴 종료 시 수치가 108이 되면 사망한다.
   źródło: Bufs.json :: dataList[id=Cycle].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0}% damage. Turn End: Die at 108+ Count.
   PL: Otrzymuje +{0}% obrażeń. Umiera, gdy wartość osiągnie 108.
215. [Status [Cycle] — podsumowanie] 나는 비워내느니 전용 패시브
   źródło: Bufs.json :: dataList[id=Cycle].summary
   limit: do 120 znaków
   EN: My Form Empties’ Passive
   PL: Pasyw wyłącznie dla „Formy, Którą Wypełnia Pustka”
216. [Status [Duress] — nazwa] 구속
   źródło: Bufs.json :: dataList[id=Duress].name
   kontekst: identyfikator statusu w tekstach: `[Duress]`
   limit: do 40 znaków
   EN: Captivity
   PL: Niewola
217. [Status [Duress] — opis] 3턴간 흐트러짐 상태가 되고 퇴각 관련 기능이 작동하지 않음\nkqe-1j-23이 흐트러짐 상태인 경우 해제됨
   źródło: Bufs.json :: dataList[id=Duress].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Become Staggered for 3 turns; disable any Retreat-related abilities\nRemove this effect when kqe-1j-23 becomes Staggered
   PL: Pozostaje oszołomiona przez 3 tury; zdolności odwrotu są wyłączone\nEfekt znika, gdy kqe-1j-23 zostanie oszołomione
218. [Status [Duress] — podsumowanie] kqe 전용 패시브
   źródło: Bufs.json :: dataList[id=Duress].summary
   limit: do 120 znaków
   EN: Kqe’s Passive
   PL: Pasyw wyłącznie dla kqe
219. [Status [VioletResultUp] — nazwa] 질투 위력 증가
   źródło: Bufs.json :: dataList[id=VioletResultUp].name
   kontekst: identyfikator statusu w tekstach: `[VioletResultUp]`
   limit: do 40 znaków
   EN: Envy Power Up
   PL: Wzrost Mocy Zazdrości
220. [Status [VioletResultUp] — opis] 이번 턴 동안 질투 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=VioletResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Zazdrości +{0}
221. [Status [VioletResultUp] — podsumowanie] 질투 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=VioletResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Zazdrości +{0}
222. [Status [CyclingKarma] — nazwa] 순환하는 업보
   źródło: Bufs.json :: dataList[id=CyclingKarma].name
   kontekst: identyfikator statusu w tekstach: `[CyclingKarma]`
   limit: do 40 znaków
   EN: Cyclical Karma
   PL: Krążąca Karma
223. [Status [CyclingKarma] — opis] 모든 캐릭터가 공격 적중 시마다 업보를 공격 대상에게 옮긴다. 아군이 살아있는동안에는 나는 비워내느니에게는 업보가 옮겨지지 않는다.
   źródło: Bufs.json :: dataList[id=CyclingKarma].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All units transfer their Karma to their targets after a successful attack.\nKarma is not transferred to My Form Empties as long as its allies are alive.
   PL: Wszystkie postacie przy każdym trafieniu atakiem przenoszą Karmę na cel ataku. Dopóki żyją sojusznicy, Karma nie jest przenoszona na „Formę, Którą Wypełnia Pustka”
224. [Status [CyclingKarma] — podsumowanie] 공격 적중 시 업보 이동
   źródło: Bufs.json :: dataList[id=CyclingKarma].summary
   limit: do 120 znaków
   EN: Karma transfers on hit
   PL: Przy trafieniu Karma zostaje przeniesiona
225. [Status [TakeHpHealReduce] — nazwa] 체력 회복 감소
   źródło: Bufs.json :: dataList[id=TakeHpHealReduce].name
   kontekst: identyfikator statusu w tekstach: `[TakeHpHealReduce]`
   limit: do 40 znaków
   EN: HP Healing Down
   PL: Spadek Leczenia HP
226. [Status [TakeHpHealReduce] — opis] 이번 턴 동안 패시브, 스킬, 코인의 효과로 회복하는 체력 -{0}0% (최대 5)
   źródło: Bufs.json :: dataList[id=TakeHpHealReduce].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Heal -{0}0% HP from Passives, Skills, and Coin effects this turn. (Max 5)
   PL: W tej turze odzyskuje o {0}0% mniej HP dzięki Pasywom, Umiejętnościom i efektom Monet (maks. 5)
227. [Status [TakeHpHealReduce] — podsumowanie] 체력 회복량 -{0}0%
   źródło: Bufs.json :: dataList[id=TakeHpHealReduce].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: HP Healing -{0}0%
   PL: Odzyskiwane HP -{0}0%
228. [Status [AttackLevelAdder] — nazwa] 공격 레벨+
   źródło: Bufs.json :: dataList[id=AttackLevelAdder].name
   kontekst: identyfikator statusu w tekstach: `[AttackLevelAdder]`
   limit: do 40 znaków
   EN: Offense Level+
   PL: Poziom Ataku+
229. [Status [AttackLevelAdder] — opis] 이번 턴 동안 공격 레벨 +{0}
   źródło: Bufs.json :: dataList[id=AttackLevelAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level +{0} for this turn.
   PL: W tej turze Poziom Ataku +{0}
230. [Status [AttackLevelAdder] — podsumowanie] 공격 레벨 +{0}
   źródło: Bufs.json :: dataList[id=AttackLevelAdder].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level +{0}
   PL: Poziom Ataku +{0}
231. [Status [Thirst] — nazwa] 갈증
   źródło: Bufs.json :: dataList[id=Thirst].name
   kontekst: identyfikator statusu w tekstach: `[Thirst]`
   limit: do 40 znaków
   EN: Appetite
   PL: Pragnienie
232. [Status [Thirst] — opis] 즉흥 조리 패시브의 회복량 +{0}0%. 패시브 발동 시 전부 소모.
   źródło: Bufs.json :: dataList[id=Thirst].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: +{0}0% healing from [Rustle Up].\nSpent when the Passive activates.
   PL: Zwiększa leczenie z pasywu „Improwizowane Gotowanie” o {0}0%. Zużywane w całości przy aktywacji pasywu.
233. [Status [Thirst] — podsumowanie] 즉흥 조리의 회복량 +{0}0%
   źródło: Bufs.json :: dataList[id=Thirst].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Rustle Up] healing +{0}0% HP
   PL: Leczenie „Improwizowanego Gotowania” +{0}0%
234. [Status [GainSinStockAdder] — nazwa] E.G.O 자원 획득량 +
   źródło: Bufs.json :: dataList[id=GainSinStockAdder].name
   kontekst: identyfikator statusu w tekstach: `[GainSinStockAdder]`
   limit: do 40 znaków
   EN: E.G.O Resource Amp
   PL: Zysk Zasobów E.G.O +
235. [Status [GainSinStockAdder] — opis] 이번 턴 동안 스킬 사용 시 획득하는 E.G.O 자원 수 +{0}
   źródło: Bufs.json :: dataList[id=GainSinStockAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain +{0} E.G.O resources from using skills this turn.
   PL: W tej turze zyskuje +{0} zasobów E.G.O przy użyciu Umiejętności
236. [Status [GainSinStockAdder] — podsumowanie] 획득 E.G.O 자원 수 +{0}
   źródło: Bufs.json :: dataList[id=GainSinStockAdder].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0} E.G.O resource gain
   PL: Zysk zasobów E.G.O +{0}
237. [Status [Weak_Chicken] — nazwa] 닭들의 종말 요리
   źródło: Bufs.json :: dataList[id=Weak_Chicken].name
   kontekst: identyfikator statusu w tekstach: `[Weak_Chicken]`
   limit: do 40 znaków
   EN: Poultry Apocalypse
   PL: Apokalipsa Drobiu
238. [Status [Weak_Chicken] — opis] 수감자들의 요리가 만들어낸 반응. 체력이 최대 체력의 40%만큼 감소
   źródło: Bufs.json :: dataList[id=Weak_Chicken].desc
   limit: do 120 znaków
   EN: The reaction wrought by the Sinners’ cooking. Loses HP by 40% of Max HP.
   PL: Reakcja wywołana przez gotowanie Grzeszników. Traci HP w wysokości 40% Maks. HP
239. [Status [Weak_Chicken] — podsumowanie] 체력 -40%
   źródło: Bufs.json :: dataList[id=Weak_Chicken].summary
   limit: do 120 znaków
   EN: HP -40%
   PL: HP -40%
240. [Status [Strong_Chicken] — nazwa] 표현되지 않은 분노
   źródło: Bufs.json :: dataList[id=Strong_Chicken].name
   kontekst: identyfikator statusu w tekstach: `[Strong_Chicken]`
   limit: do 40 znaków
   EN: Unvented Anger
   PL: Niewyrażony Gniew
241. [Status [Strong_Chicken] — opis] 매 턴마다 공격 위력 증가 1 얻음.
   źródło: Bufs.json :: dataList[id=Strong_Chicken].desc
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up every turn.
   PL: Co turę zyskuje 1 Wzrost Mocy Ataku.
242. [Status [Strong_Chicken] — podsumowanie] 공격 위력 증가 1 얻음.
   źródło: Bufs.json :: dataList[id=Strong_Chicken].summary
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up
   PL: Zyskuje 1 Wzrost Mocy Ataku
243. [Status [DimensionRift] — nazwa] 차원 균열
   źródło: Bufs.json :: dataList[id=DimensionRift].name
   kontekst: identyfikator statusu w tekstach: `[DimensionRift]`
   limit: do 40 znaków
   EN: Dimensional Rift
   PL: Szczelina Wymiarowa
244. [Status [DimensionRift] — opis] 이번 턴 종료 시 파열 횟수가 {0} 증가
   źródło: Bufs.json :: dataList[id=DimensionRift].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Gain +{0} Rupture Count
   PL: Na koniec tej tury Licznik Rozdarcia rośnie o {0}
245. [Status [DimensionRift] — podsumowanie] 파열 횟수 증가
   źródło: Bufs.json :: dataList[id=DimensionRift].summary
   limit: do 120 znaków
   EN: Increase Rupture Count
   PL: Licznik Rozdarcia rośnie
246. [Status [Scared] — nazwa] 두려움
   źródło: Bufs.json :: dataList[id=Scared].name
   kontekst: identyfikator statusu w tekstach: `[Scared]`
   limit: do 40 znaków
   EN: Fear
   PL: Lęk
247. [Status [Scared] — opis] 정신력이 -20이하일 때, 턴 종료 시 다음 턴에 보호 1 얻음.
   źródło: Bufs.json :: dataList[id=Scared].desc
   limit: do 120 znaków
   EN: Turn End: At -20 SP or lower, gain 1 Protection next turn.
   PL: Przy Poczytalności -20 lub niższej, na koniec tury zyskuje 1 Ochrony w następnej turze
248. [Status [Scared] — podsumowanie] 정신력이 -20이하일 때, 턴 종료 시 다음 턴에 보호 1 얻음.
   źródło: Bufs.json :: dataList[id=Scared].summary
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Status [Stressed] — nazwa] 스트레스
   źródło: Bufs.json :: dataList[id=Stressed].name
   kontekst: identyfikator statusu w tekstach: `[Stressed]`
   limit: do 40 znaków
   EN: Stressed
   PL: Stres
250. [Status [Stressed] — opis] 정신력이 -25이하일 때, 턴 종료 시 다음 턴에 수비 위력 증가 1 얻음.
   źródło: Bufs.json :: dataList[id=Stressed].desc
   limit: do 120 znaków
   EN: Turn End: At -25 SP or lower, gain 1 Defense Power Up next turn
   PL: Przy Poczytalności -25 lub niższej, na koniec tury zyskuje 1 Wzrost Mocy Obrony w następnej turze
251. [Status [Stressed] — podsumowanie] 정신력이 -25이하일 때, 턴 종료 시 다음 턴에 수비 위력 증가 1 얻음.
   źródło: Bufs.json :: dataList[id=Stressed].summary
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Status [Nervous] — nazwa] 초조함
   źródło: Bufs.json :: dataList[id=Nervous].name
   kontekst: identyfikator statusu w tekstach: `[Nervous]`
   limit: do 40 znaków
   EN: Nervous
   PL: Nerwowość
253. [Status [Nervous] — opis] 정신력이 -15이하일 때, 턴 종료 시 다음 턴에 방어 레벨 증가 5 얻음.
   źródło: Bufs.json :: dataList[id=Nervous].desc
   limit: do 120 znaków
   EN: Turn End: At -15 SP or lower, gain 5 Defense Level Up next turn
   PL: Przy Poczytalności -15 lub niższej, na koniec tury zyskuje 5 Wzrostów Poziomu Obrony w następnej turze
254. [Status [Nervous] — podsumowanie] 정신력이 -15이하일 때, 턴 종료 시 다음 턴에 방어 레벨 증가 5 얻음.
   źródło: Bufs.json :: dataList[id=Nervous].summary
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Status [ShardOfUmbrella] — nazwa] 우산 파편
   źródło: Bufs.json :: dataList[id=ShardOfUmbrella].name
   kontekst: identyfikator statusu w tekstach: `[ShardOfUmbrella]`
   limit: do 40 znaków
   EN: Umbrella Splinters
   PL: Odłamki Parasola
256. [Status [ShardOfUmbrella] — opis] 턴 종료 시 {0}X5만큼 파열 얻음
   źródło: Bufs.json :: dataList[id=ShardOfUmbrella].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Gain {0} x 5 Rupture
   PL: Na koniec tury zyskuje {0} x 5 Rozdarcia
257. [Status [ShardOfUmbrella] — podsumowanie] 턴 종료 시 {0}X5만큼 파열 얻음
   źródło: Bufs.json :: dataList[id=ShardOfUmbrella].summary
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Status [WrappedCurseTag] — nazwa] 얽혀온 저주 부적
   źródło: Bufs.json :: dataList[id=WrappedCurseTag].name
   kontekst: identyfikator statusu w tekstach: `[WrappedCurseTag]`
   limit: do 40 znaków
   EN: Entangled Curse Talisman
   PL: Przepleciony Talizman Klątwy
259. [Status [WrappedCurseTag] — opis] 가하는 피해량 +{0}%\n9이상이라면, 턴 시작 시 공격 위력 감소 2 얻음
   źródło: Bufs.json :: dataList[id=WrappedCurseTag].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Deal +{0}% damage\nAt 9+ Stack, gain 2 Attack Power Down at turn start
   PL: Zadaje +{0}% obrażeń\nPrzy 9 lub więcej stosach zyskuje na początek tury 2 Spadki Mocy Ataku
260. [Status [WrappedCurseTag] — podsumowanie] 가하는 피해량 +{0}%, 9이상이라면, 턴 시작 시 공격 위력 감소 2 얻음
   źródło: Bufs.json :: dataList[id=WrappedCurseTag].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}% damage; at 9+ Stack, gain 2 Attack Power Down at turn start
   PL: Zadaje +{0}% obrażeń; przy 9 lub więcej stosach zyskuje 2 Spadki Mocy Ataku na początek tury
261. [Status [ReattachedCurseTag] — nazwa] 다시 붙여진 저주 부적
   źródło: Bufs.json :: dataList[id=ReattachedCurseTag].name
   kontekst: identyfikator statusu w tekstach: `[ReattachedCurseTag]`
   limit: do 40 znaków
   EN: Reattached Curse Talisman
   PL: Ponownie Naklejony Talizman Klątwy
262. [Status [ReattachedCurseTag] — opis] 9이상이라면, 턴 시작 시 속박 5 얻음.\n12이상이라면, 턴 시작 시 공격 위력 감소 5 얻음.
   źródło: Bufs.json :: dataList[id=ReattachedCurseTag].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 9+, gain 5 Bind at the start of the turn.\nAt 12+, gain 5 Attack Power Down at the start of the turn.
   PL: Przy 9 lub więcej stosach zyskuje na początku tury 5 Spętań.\nPrzy 12 lub więcej stosach zyskuje na początku tury 5 Spadków Mocy Ataku.
263. [Status [ReattachedCurseTag] — podsumowanie] 9이상이라면, 턴 시작 시 속박 5 얻음.\n12이상이라면, 턴 시작 시 공격 위력 감소 5 얻음.
   źródło: Bufs.json :: dataList[id=ReattachedCurseTag].summary
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Status [ElectricStorage] — nazwa] 축전
   źródło: Bufs.json :: dataList[id=ElectricStorage].name
   kontekst: identyfikator statusu w tekstach: `[ElectricStorage]`
   limit: do 40 znaków
   EN: Capacitor
   PL: Kondensator
265. [Status [ElectricStorage] — opis] 몸에 전류가 쌓인 것 같다.
   źródło: Bufs.json :: dataList[id=ElectricStorage].desc
   limit: do 120 znaków
   EN: It seems to be storing electricity in its body.
   PL: Wygląda na to, że w ciele gromadzi się prąd.
266. [Status [SelfCharge] — nazwa] 자가 충전
   źródło: Bufs.json :: dataList[id=SelfCharge].name
   kontekst: identyfikator statusu w tekstach: `[SelfCharge]`
   limit: do 40 znaków
   EN: Self-charge
   PL: Samoładowanie
267. [Status [SelfCharge] — opis] 몸 주변으로 전류가 흐르는 것 같다.\n죽음을 맞이한 후 자가 충전이 남아있다면 전부 소모하기 전까지 체력 1로 고정. (최대 20)
   źródło: Bufs.json :: dataList[id=SelfCharge].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Electric currents seem to flow around its body.\nAfter the unit faces death, as long as it has Self-charge, its HP is fixed at 1 until it is fully consumed. (Max 20)
   PL: Wokół ciała zdają się płynąć prądy.\nPo doświadczeniu śmierci, dopóki pozostaje Samoładowanie, HP zostaje ustalone na 1, aż do pełnego zużycia. (maks. 20)
268. [Status [Exalted] — nazwa] 고양
   źródło: Bufs.json :: dataList[id=Exalted].name
   kontekst: identyfikator statusu w tekstach: `[Exalted]`
   limit: do 40 znaków
   EN: Morale Boost
   PL: Podniesienie Moralu
269. [Status [Exalted] — opis] 매 턴마다 피해량 증가 {0} 얻음 (최대 5)\n취기가 있을 때, 얻을 수 없음.
   źródło: Bufs.json :: dataList[id=Exalted].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Gain {0} Damage Up every turn (Max 5)\nCannot gain the status while Tipsy
   PL: Co turę zyskuje {0} Wzrostów Obrażeń (maks. 5)\nNie można zyskać tego efektu w stanie Pijaństwa
270. [Status [Exalted] — podsumowanie] 매 턴마다 피해량 증가 수치만큼 얻음. 취기가 있을 때, 얻을 수 없음.
   źródło: Bufs.json :: dataList[id=Exalted].summary
   limit: do 120 znaków
   EN: Gain Damage Up by the effect's Count every turn; Cannot gain the status while Tipsy
   PL: Co turę zyskuje tyle Wzrostów Obrażeń, ile wynosi wartość; nie można zyskać w stanie Pijaństwa
271. [Status [Tipsiness] — nazwa] 취기
   źródło: Bufs.json :: dataList[id=Tipsiness].name
   kontekst: identyfikator statusu w tekstach: `[Tipsiness]`
   limit: do 40 znaków
   EN: Tipsy
   PL: Upojenie
272. [Status [Tipsiness] — opis] 합 위력 -{0} (최대 5)
   źródło: Bufs.json :: dataList[id=Tipsiness].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clash Power -{0} (Max 5)
   PL: Moc Starcia -{0} (maks. 5)
273. [Status [Tipsiness] — podsumowanie] 합 위력이 수치만큼 감소
   źródło: Bufs.json :: dataList[id=Tipsiness].summary
   limit: do 120 znaków
   EN: Lose Clash Power equal to Stack
   PL: Moc Starcia maleje o wartość
274. [Status [Predation] — nazwa] 포식
   źródło: Bufs.json :: dataList[id=Predation].name
   kontekst: identyfikator statusu w tekstach: `[Predation]`
   limit: do 40 znaków
   EN: Predation
   PL: Drapieżność
275. [Status [Predation] — opis] 강력한 기술을 사용하는 것 같다.
   źródło: Bufs.json :: dataList[id=Predation].desc
   limit: do 120 znaków
   EN: It seems to be preparing a powerful move.
   PL: Wydaje się, że przygotowuje potężny atak.
276. [Status [ATL_Agility] — nazwa] 더 빠르게!
   źródło: Bufs.json :: dataList[id=ATL_Agility].name
   kontekst: identyfikator statusu w tekstach: `[ATL_Agility]`
   limit: do 40 znaków
   EN: Faster!
   PL: Szybciej!
277. [Status [ATL_Agility] — opis] 신속 2 얻음
   źródło: Bufs.json :: dataList[id=ATL_Agility].desc
   limit: do 120 znaków
   EN: Gain 2 Haste
   PL: Zyskuje 2 Pośpiechu
278. [Status [ATL_Breath] — nazwa] 더 정확하게!
   źródło: Bufs.json :: dataList[id=ATL_Breath].name
   kontekst: identyfikator statusu w tekstach: `[ATL_Breath]`
   limit: do 40 znaków
   EN: Aim True!
   PL: Celniej!
279. [Status [ATL_Breath] — opis] 호흡 3 얻음
   źródło: Bufs.json :: dataList[id=ATL_Breath].desc
   limit: do 120 znaków
   EN: Gain 3 Poise
   PL: Zyskuje 3 Oddechu
280. [Status [ATL_Target] — nazwa] 저 놈 잡아!
   źródło: Bufs.json :: dataList[id=ATL_Target].name
   kontekst: identyfikator statusu w tekstach: `[ATL_Target]`
   limit: do 40 znaków
   EN: Get 'Em!
   PL: Złapcie Go!
281. [Status [ATL_Target] — opis] 한 명의 적을 동시 공격합니다.
   źródło: Bufs.json :: dataList[id=ATL_Target].desc
   limit: do 120 znaków
   EN: Simultaneously attacks one unit
   PL: Atakuje jednocześnie jedną jednostkę.
282. [Status [ATL_EndureCombustion] — nazwa] 화상 저항
   źródło: Bufs.json :: dataList[id=ATL_EndureCombustion].name
   kontekst: identyfikator statusu w tekstach: `[ATL_EndureCombustion]`
   limit: do 40 znaków
   EN: Burn Resistance
   PL: Odporność na Podpalenie
283. [Status [ATL_EndureCombustion] — opis] 화상에 피해를 입을 때, {0}0%만큼 피해량 감소 (최대 10)
   źródło: Bufs.json :: dataList[id=ATL_EndureCombustion].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When taking damage from Burn, reduce the damage by {0}0% (Max 10)
   PL: Otrzymując obrażenia od Podpalenia, zmniejsza je o {0}0% (maks. 10)
284. [Status [ATL_EndureCombustion] — podsumowanie] 화상에 피해를 입을 때, {0}0%만큼 감소한 피해를 입는다.
   źródło: Bufs.json :: dataList[id=ATL_EndureCombustion].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When taking damage from Burn, take {0}0% less damage
   PL: Otrzymując obrażenia od Podpalenia, otrzymuje {0}0% mniej obrażeń
285. [Status [Resonate] — nazwa] 공진
   źródło: Bufs.json :: dataList[id=Resonate].name
   kontekst: identyfikator statusu w tekstach: `[Resonate]`
   limit: do 40 znaków
   EN: Resonant
   PL: Rezonans
286. [Status [Resonate] — opis] 대상에게 진동 폭발 또는 흐트러짐 손상을 줄 때, 추가로 고정 피해량 ({0}X3)과 흐트러짐 손상 ({0}X3)% 입힘
   źródło: Bufs.json :: dataList[id=Resonate].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When triggering Tremor Burst or raising Stagger Threshold, deal ({0} * 3) fixed damage and raise Stagger Threshold by ({0} * 3)%
   PL: Wywołując Wyładowanie Wstrząsu lub podnosząc Próg Oszołomienia celu, zadaje dodatkowo ({0} x 3) obrażeń stałych i podnosi Próg Oszołomienia o ({0} x 3)%
287. [Status [Resonate] — podsumowanie] 진동 폭발 혹은 흐트러짐 손상을 줄 때, 피해량과 흐트러짐 손상을 추가로 줌.
   źródło: Bufs.json :: dataList[id=Resonate].summary
   limit: do 140 znaków
   EN: When triggering Tremor Burst or raising Stagger Thresholds, deal damage and raise Stagger Threshold further
   PL: Wywołując Wybuch Wstrząsu lub podnosząc Próg Oszołomienia, zadaje dodatkowe obrażenia i podnosi Próg Oszołomienia
288. [Status [VibrationAssimilation] — nazwa] 진동 동화
   źródło: Bufs.json :: dataList[id=VibrationAssimilation].name
   kontekst: identyfikator statusu w tekstach: `[VibrationAssimilation]`
   limit: do 40 znaków
   EN: Tremor Sync
   PL: Synchronizacja Wstrząsu
289. [Status [VibrationAssimilation] — opis] 대상이 가지고 있는 진동 5마다, 대상의 합 위력 -1
   źródło: Bufs.json :: dataList[id=VibrationAssimilation].desc
   limit: do 120 znaków
   EN: In a clash, the opponent has -1 Clash Power for every 5 Tremor they have
   PL: Podczas Starcia przeciwnik ma -1 Mocy Starcia za każde 5 Wstrząsu, które posiada
290. [Status [VibrationAssimilation] — podsumowanie] 대상이 가지고 있는 진동 5마다, 대상의 합 위력 -1
   źródło: Bufs.json :: dataList[id=VibrationAssimilation].summary
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Status [CollapseAmpoule] — nazwa] 붕괴 앰플
   źródło: Bufs.json :: dataList[id=CollapseAmpoule].name
   kontekst: identyfikator statusu w tekstach: `[CollapseAmpoule]`
   limit: do 40 znaków
   EN: Decay Ampule
   PL: Ampułka Rozpadu
292. [Status [CollapseAmpoule] — opis] 최대 체력의 {0}X2%만큼 피해 입힘.
   źródło: Bufs.json :: dataList[id=CollapseAmpoule].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take damage by {0} * 2% of Max HP
   PL: Zadaje obrażenia równe {0} x 2% Maks. HP.
293. [Status [CollapseAmpoule] — podsumowanie] 최대 체력의 {0}X2%만큼 피해 입힘.
   źródło: Bufs.json :: dataList[id=CollapseAmpoule].summary
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Status [InterlockingTime] — nazwa] 맞물리는 시간
   źródło: Bufs.json :: dataList[id=InterlockingTime].name
   kontekst: identyfikator statusu w tekstach: `[InterlockingTime]`
   limit: do 40 znaków
   EN: Interlocking Time
   PL: Przeplatający się Czas
295. [Status [InterlockingTime] — opis] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 1.5배만큼 고정 피해를 입음.
   źródło: Bufs.json :: dataList[id=InterlockingTime].desc
   limit: do 150 znaków
   EN: Reduce final damage by 30% and store it. At 3 Stacks, take fixed damage equal to 1.5 times the accumulated damage
   PL: Redukuje 30% obrażeń końcowych i gromadzi je. Przy 3 stosach otrzymuje obrażenia stałe równe 1,5 gromadzonych obrażeń
296. [Status [InterlockingTime] — podsumowanie] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 1.5배만큼 고정 피해를 입음.
   źródło: Bufs.json :: dataList[id=InterlockingTime].summary
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Status [TimeRental] — nazwa] 심상 속 시간 대여
   źródło: Bufs.json :: dataList[id=TimeRental].name
   kontekst: identyfikator statusu w tekstach: `[TimeRental]`
   limit: do 40 znaków
   EN: Borrowed Time of the Fathoms
   PL: Pożyczony Czas Wyobraźni
298. [Status [TimeRental] — opis] 턴 종료 시 신속 3, 피해량 증가 2 얻음. 턴 종료 시 수치가 1 남았다면, 다음 턴에 속박 4, 공격 위력 감소 1 얻음
   źródło: Bufs.json :: dataList[id=TimeRental].desc
   limit: do 130 znaków
   EN: Turn End: Gain 3 Haste and 2 Damage Up; If only 1 Stack remains, gain 4 Bind and 1 Attack Power Down
   PL: Na koniec tury: 3 Pośpiechu i 2 Wzrosty Obrażeń. Przy 1 wartości zyskuje w następnej turze 4 Spętań i 1 Spadek Mocy Ataku
299. [Status [TimeRental] — podsumowanie] 턴 종료 시 신속 3, 피해량 증가 2 얻음. 턴 종료 시 수치가 1 남았다면, 다음 턴에 속박 4, 공격 위력 감소 1 얻음
   źródło: Bufs.json :: dataList[id=TimeRental].summary
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Status [Bull_FadedHeat] — nazwa] 잠시 사그라든 열기
   źródło: Bufs.json :: dataList[id=Bull_FadedHeat].name
   kontekst: identyfikator statusu w tekstach: `[Bull_FadedHeat]`
   limit: do 40 znaków
   EN: Momentary Cool
   PL: Chwilowe Ostudzenie
301. [Status [Bull_FadedHeat] — opis] 본체와 몸통 부위의 최대 체력 -50%
   źródło: Bufs.json :: dataList[id=Bull_FadedHeat].desc
   limit: do 120 znaków
   EN: Core and body lose 50% Max HP
   PL: Korpus i część Tułowia tracą 50% Maks. HP
302. [Status [Bull_Fever] — nazwa] 흥분
   źródło: Bufs.json :: dataList[id=Bull_Fever].name
   kontekst: identyfikator statusu w tekstach: `[Bull_Fever]`
   limit: do 40 znaków
   EN: Fever
   PL: Podniecenie
303. [Status [Bull_Fever] — opis] 가하는 피해량 +{0}0%\n턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=Bull_Fever].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Deal +{0}0% damage\nTurn End: Reduce Count by 1
   PL: Zadaje +{0}0% obrażeń\nNa koniec tury wartość maleje o 1
304. [Status [Bull_Sadness] — nazwa] 해소되지 않은 슬픔
   źródło: Bufs.json :: dataList[id=Bull_Sadness].name
   kontekst: identyfikator statusu w tekstach: `[Bull_Sadness]`
   limit: do 40 znaków
   EN: Unresolved Sorrow
   PL: Nierozwiązany Smutek
305. [Status [Bull_Sadness] — opis] 다음 턴에 수치만큼 공격 위력 감소를 얻음.\n턴 종료 시 수치가 3 이상이면, 팽창하는 슬픔 으로 교체됨.
   źródło: Bufs.json :: dataList[id=Bull_Sadness].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Attack Power Down by the Count next turn.\nTurn End: At 3+ Count, changes to Expanding Sorrow.
   PL: W następnej turze zyskuje Spadki Mocy Ataku równe wartości.\nNa koniec tury przy 3+ wartości zamienia się w „Pęczniejący Smutek”
306. [Status [Bull_ReinforcedSadness] — nazwa] 팽창하는 슬픔
   źródło: Bufs.json :: dataList[id=Bull_ReinforcedSadness].name
   kontekst: identyfikator statusu w tekstach: `[Bull_ReinforcedSadness]`
   limit: do 40 znaków
   EN: Expanding Sorrow
   PL: Rozszerzający Smutek
307. [Status [Bull_ReinforcedSadness] — opis] 스킬 패턴이 변경됨.
   źródło: Bufs.json :: dataList[id=Bull_ReinforcedSadness].desc
   limit: do 120 znaków
   EN: Changes behavior.
   PL: Zmienia wzorzec Umiejętności.
308. [Status [Bull_ReinforcedSadness] — podsumowanie] 스킬 패턴이 변경됨.
   źródło: Bufs.json :: dataList[id=Bull_ReinforcedSadness].summary
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Status [Bull_BuzzingEmotion] — nazwa] 울렁이는 감정
   źródło: Bufs.json :: dataList[id=Bull_BuzzingEmotion].name
   kontekst: identyfikator statusu w tekstach: `[Bull_BuzzingEmotion]`
   limit: do 40 znaków
   EN: Wavering Emotions
   PL: Wahające się Emocje
310. [Status [Bull_BuzzingEmotion] — opis] 턴 시작 시 공격 위력 감소, 마비, 속박 중 무작위로 수치만큼 얻고 소멸
   źródło: Bufs.json :: dataList[id=Bull_BuzzingEmotion].desc
   limit: do 150 znaków
   EN: Turn Start: Randomly gain Attack Power Down, Paralyze, or Bind by this effect's Count, then remove this effect
   PL: Na początku tury zyskuje losowo tyle Spadków Mocy Ataku, Paraliżu albo Spętań, ile wynosi wartość, po czym efekt znika
311. [Status [Bull_BuzzingEmotion] — podsumowanie] 턴 시작 시 공격 위력 감소, 마비, 속박 중 무작위로 수치만큼 얻고 소멸
   źródło: Bufs.json :: dataList[id=Bull_BuzzingEmotion].summary
   (powtórzenie elementu 310 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Status [Crazy_LowMorale] — nazwa] 광인
   źródło: Bufs.json :: dataList[id=Crazy_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Crazy_LowMorale]`
   limit: do 40 znaków
   EN: Maddened
   PL: Szaleniec
313. [Status [Crazy_LowMorale] — opis] - 사기 저하\n- 첫 사기저하일 때, 피아식별 불가상태
   źródło: Bufs.json :: dataList[id=Crazy_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When at low morale for the first time, targets units indiscriminately
   PL: - Spadek Moralu\n- Przy pierwszym Spadku Moralu atakuje sojuszników i wrogów bez rozeznania
314. [Status [Crazy_Panic] — nazwa] 광인
   źródło: Bufs.json :: dataList[id=Crazy_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Crazy_Panic]`
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Status [Crazy_Panic] — opis] - 패닉\n- 피아식별 불가상태, 합 위력 +1, 피해량 증가 2 얻음
   źródło: Bufs.json :: dataList[id=Crazy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Targets indiscriminately; Clash Power +1, and gain 2 Damage Up
   PL: - Panika\n- Atakuje bez rozeznania; Moc Starcia +1, zyskuje 2 Wzrosty Obrażeń
316. [Status [Suicide_LowMorale] — nazwa] 자살
   źródło: Bufs.json :: dataList[id=Suicide_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Suicide_LowMorale]`
   limit: do 40 znaków
   EN: Suicidal
   PL: Samobójstwo
317. [Status [Suicide_LowMorale] — opis] - 사기 저하\n- 첫 사기저하 상태였을 때, 행동 불가 상태.
   źródło: Bufs.json :: dataList[id=Suicide_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When at low morale for the first time, become unable to act
   PL: - Spadek Moralu\n- Przy pierwszym Spadku Moralu nie może podejmować działań
318. [Status [Suicide_Panic] — nazwa] 자살
   źródło: Bufs.json :: dataList[id=Suicide_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Suicide_Panic]`
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Status [Suicide_Panic] — opis] - 패닉\n- 3턴 간 행동불가 상태. 턴 시작 시 죽음. 모든 아군 고정 정신력 -10
   źródło: Bufs.json :: dataList[id=Suicide_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Cannot act for 3 turns. Unit dies at turn start; all its allies lose 10 SP
   PL: - Panika\n- Nie może działać przez 3 tury. Umiera na początku tury; wszyscy sojusznicy tracą 10 Poczytalności
320. [Status [Prowl_LowMorale] — nazwa] 배회
   źródło: Bufs.json :: dataList[id=Prowl_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Prowl_LowMorale]`
   limit: do 40 znaków
   EN: Wandering
   PL: Błąkanie
321. [Status [Prowl_LowMorale] — opis] - 사기 저하\n- 턴 종료 시 아군에게 정신력 2 피해
   źródło: Bufs.json :: dataList[id=Prowl_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn End: Deal 2 SP damage to allies
   PL: - Spadek Moralu\n- Na koniec tury zadaje sojusznikom 2 obrażeń Poczytalności
322. [Status [Prowl_Panic] — nazwa] 배회
   źródło: Bufs.json :: dataList[id=Prowl_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Prowl_Panic]`
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Status [Prowl_Panic] — opis] - 패닉\n- 3턴 간 턴 종료 시 아군에게 정신력 5 피해. 3턴 종료 시 도주
   źródło: Bufs.json :: dataList[id=Prowl_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn End: Deal 5 SP damage to allies. Flees from battle after 3 turns have passed
   PL: - Panika\n- Przez 3 tury na koniec tury zadaje sojusznikom 5 obrażeń Poczytalności. Po 3 turach ucieka z walki
324. [Status [Thorn] — nazwa] 가시
   źródło: Bufs.json :: dataList[id=Thorn].name
   kontekst: identyfikator statusu w tekstach: `[Thorn]`
   limit: do 40 znaków
   EN: Thorns
   PL: Ciernie
325. [Status [Thorn] — opis] 피격 시 자신이 받은 피해량의 50%를 공격자에게 돌려줌
   źródło: Bufs.json :: dataList[id=Thorn].desc
   limit: do 120 znaków
   EN: When hit, return 50% of the damage taken to the attacker
   PL: Przy trafieniu oddaje atakującemu 50% otrzymanych obrażeń
326. [Status [Thorn] — podsumowanie] 받은 피해의 50%를 공격자에게 입힘
   źródło: Bufs.json :: dataList[id=Thorn].summary
   limit: do 120 znaków
   EN: Deal 50% of damage taken to attacker
   PL: Zadaje atakującemu 50% otrzymanych obrażeń
327. [Status [Fragile_Mind_LowMorale] — nazwa] 위태로운 마음
   źródło: Bufs.json :: dataList[id=Fragile_Mind_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Fragile_Mind_LowMorale]`
   limit: do 40 znaków
   EN: Perilous Heart
   PL: Chwiejne Serce
328. [Status [Fragile_Mind_LowMorale] — opis] 턴 시작 시 공격 위력 증가 2 , 속박 3 얻음
   źródło: Bufs.json :: dataList[id=Fragile_Mind_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Attack Power Up and 3 Bind
   PL: Na początku tury zyskuje 2 Wzrosty Mocy Ataku i 3 Spętań
329. [Status [Fragile_Mind_LowMorale] — podsumowanie] 턴 시작 시 공격 위력 증가 2 , 속박 3 얻음
   źródło: Bufs.json :: dataList[id=Fragile_Mind_LowMorale].summary
   (powtórzenie elementu 328 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Status [Fragile_Mind_Panic] — nazwa] 흐트러진 마음
   źródło: Bufs.json :: dataList[id=Fragile_Mind_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Fragile_Mind_Panic]`
   limit: do 40 znaków
   EN: Faltering Heart
   PL: Roztrzęsione Serce
331. [Status [Fragile_Mind_Panic] — opis] 패닉 상태면 흐트러짐 상태가 됨
   źródło: Bufs.json :: dataList[id=Fragile_Mind_Panic].desc
   limit: do 120 znaków
   EN: In panic, become staggered.
   PL: W stanie Paniki zostaje oszołomiony
332. [Status [Fragile_Mind_Panic] — podsumowanie] 패닉 상태면 흐트러짐 상태가 됨
   źródło: Bufs.json :: dataList[id=Fragile_Mind_Panic].summary
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Status [ErodingMind] — nazwa] 침식되는 마음
   źródło: Bufs.json :: dataList[id=ErodingMind].name
   kontekst: identyfikator statusu w tekstach: `[ErodingMind]`
   limit: do 40 znaków
   EN: Corroding Heart
   PL: Korodujące Serce
334. [Status [ErodingMind] — opis] 턴 시작 시 공격 위력 감소 2, 취약 2, 속박 5를 얻음
   źródło: Bufs.json :: dataList[id=ErodingMind].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Attack Power Down, 2 Fragile, and 5 Bind
   PL: Na początku tury zyskuje 2 Spadki Mocy Ataku, 2 Wrażliwości i 5 Spętań
335. [Status [ErodingMind] — podsumowanie] 턴 시작 시 공격 위력 감소 2, 취약 2, 속박 5를 얻음
   źródło: Bufs.json :: dataList[id=ErodingMind].summary
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Status [Blue_LowMorale] — nazwa] 슬픔
   źródło: Bufs.json :: dataList[id=Blue_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Blue_LowMorale]`
   limit: do 40 znaków
   EN: Dejection
   PL: Smutek
337. [Status [Blue_LowMorale] — opis] - 사기 저하\n- 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 대상의 합 위력 -1
   źródło: Bufs.json :: dataList[id=Blue_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- In a clash, if any Coin lands tails, Clash Power -1 for the clash
   PL: - Spadek Moralu\n- Jeśli w Starciu któraś moneta wypadła rewersem, Moc Starcia celu maleje w tym Starciu o 1
338. [Status [Blue_Panic] — nazwa] 슬픔
   źródło: Bufs.json :: dataList[id=Blue_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Blue_Panic]`
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Status [Blue_Panic] — opis] - 패닉\n- 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 대상의 합 위력 -3
   źródło: Bufs.json :: dataList[id=Blue_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- In a clash, if any Coin lands tails, Clash Power -3 for the clash
   PL: - Panika\n- Jeśli w Starciu któraś moneta wypadła rewersem, Moc Starcia celu maleje w tym Starciu o 3
340. [Status [ATL_EndureLaceration] — nazwa] 출혈 저항
   źródło: Bufs.json :: dataList[id=ATL_EndureLaceration].name
   kontekst: identyfikator statusu w tekstach: `[ATL_EndureLaceration]`
   limit: do 40 znaków
   EN: Bleed Resistance
   PL: Odporność na Krwawienie
341. [Status [ATL_EndureLaceration] — opis] 출혈에 피해를 입을 때, {0}0%만큼 피해량 감소 (최대 10)
   źródło: Bufs.json :: dataList[id=ATL_EndureLaceration].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When taking damage from Bleed, reduce the damage by {0}0% (Max 10)
   PL: Otrzymując obrażenia od Krwawienia, zmniejsza je o {0}0% (maks. 10)
342. [Status [ATL_EndureLaceration] — podsumowanie] 출혈에 피해를 입을 때, {0}0%만큼 감소한 피해를 입는다.
   źródło: Bufs.json :: dataList[id=ATL_EndureLaceration].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When taking damage from Bleed, take {0}0% less damage
   PL: Otrzymując obrażenia od Krwawienia, otrzymuje {0}0% mniej obrażeń
343. [Status [DongbaekGrow] — nazwa] 성장
   źródło: Bufs.json :: dataList[id=DongbaekGrow].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekGrow]`
   limit: do 40 znaków
   EN: Growing
   PL: Wzrost
344. [Status [DongbaekGrow] — opis] 턴 종료 시 수치가 1 증가하고, 수치에 비례하여 최대 체력이 증가한다. (최대 3)
   źródło: Bufs.json :: dataList[id=DongbaekGrow].desc
   limit: do 120 znaków
   EN: Turn End: Add +1 Count, and gain Max HP proportionally to the Count (Max 3)
   PL: Na koniec tury wartość rośnie o 1, a Maks. HP rośnie proporcjonalnie do wartości. (maks. 3)
345. [Status [DongbaekGrow] — podsumowanie] 턴 종료 시 수치가 1 증가하고, 수치에 비례하여 최대 체력이 증가한다. (최대 3)
   źródło: Bufs.json :: dataList[id=DongbaekGrow].summary
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Status [DongbaekFlorescence] — nazwa] 개화
   źródło: Bufs.json :: dataList[id=DongbaekFlorescence].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekFlorescence]`
   limit: do 40 znaków
   EN: Blooming
   PL: Zakwitanie
347. [Status [DongbaekFlorescence] — opis] 턴 종료 시 수치가 5 이상이면, 최대 체력의 (수치)%만큼 나태 속성 피해를 받고 만개 상태가 됨\n수치가 5 미만이면, (수치x5)만큼 정신력 피해를 받고, 수치가 1 감소함
   źródło: Bufs.json :: dataList[id=DongbaekFlorescence].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: At 5+ Count, take Sloth damage by (Count)% of Max HP, and become Fully Bloomed\nAt less than 5 Count, lose (Count * 5) SP, then reduce Count by 1
   PL: Na koniec tury, przy wartości 5+, otrzymuje obrażenia Lenistwem równe (wartość)% Maks. HP i przechodzi w stan Pełnego Rozkwitu\nPoniżej 5 traci (wartość x 5) Poczytalności, a wartość maleje o 1
348. [Status [DongbaekFullBloom] — nazwa] 만개
   źródło: Bufs.json :: dataList[id=DongbaekFullBloom].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekFullBloom]`
   limit: do 40 znaków
   EN: Fully Bloomed
   PL: Pełen Rozkwit
349. [Status [DongbaekFullBloom] — opis] 행동 불가\n턴 종료 시 정신력 -20. 정신력이 -45가 된 경우 정신력을 최대로 회복하고, 다음 턴에 아찔한 정신 상태가 됨\n2턴 동안 해제되지 않으면, 턴 종료 시 상태 해제
   źródło: Bufs.json :: dataList[id=DongbaekFullBloom].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot act\nAt the end of the turn, lose 20 SP; if SP reaches -45, fully heal SP, then gain 'Dazzled Mind' next turn.\nIf this effect isn't removed for 2 turns, remove it at the end of the turn.
   PL: Nie może działać\nNa koniec tury traci 20 Poczytalności; przy Poczytalności -45 regeneruje ją w pełni, a w następnej turze wpada w stan Oszalałego Umysłu\nJeśli efekt nie zostanie zdjęty przez 2 tury, znika na koniec tury
350. [Status [DongbaekFascination] — nazwa] 아찔한 정신
   źródło: Bufs.json :: dataList[id=DongbaekFascination].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekFascination]`
   limit: do 40 znaków
   EN: Dazzled Mind
   PL: Oszalały Umysł
351. [Status [DongbaekFascination] — opis] 이번 턴 동안 아군을 공격함\n흐트러짐 상태가 되면 다음 턴 시작 시 상태 해제\n2턴 동안 해제되지 않으면, 턴 종료 시 정신력이 30 감소하고, 상태 해제
   źródło: Bufs.json :: dataList[id=DongbaekFascination].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Targets allies for attacks\nWhen staggered, remove this effect next turn\nIf this effect isn't removed for 2 turns, lose 30 SP and remove it at the end of the turn
   PL: W tej turze atakuje sojuszników\nPo oszołomieniu efekt znika na początku następnej tury\nJeśli nie zostanie zdjęty przez 2 tury, na koniec tury traci 30 Poczytalności i znika
352. [Status [DongbaekShowdown] — nazwa] 대결
   źródło: Bufs.json :: dataList[id=DongbaekShowdown].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekShowdown]`
   limit: do 40 znaków
   EN: Dueling
   PL: Konfrontacja
353. [Status [DongbaekShowdown] — opis] 턴 시작 시 이 효과를 보유하지 않은 대상이 만개 상태가 됨.\n보유한 캐릭터가 이상이면, 동백이 공격 위력 증가 1을 얻음
   źródło: Bufs.json :: dataList[id=DongbaekShowdown].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Units without this status go into a 'Fully Bloomed' status\nIf Yi Sang has this effect, Dongbaek gains 1 Attack Power Up
   PL: Na początku tury cele bez tego efektu przechodzą w stan Pełnego Rozkwitu.\nJeśli ma go Yi Sang, Dongbaek zyskuje 1 Wzrost Mocy Ataku
354. [Status [DongbaekScatterPetal] — nazwa] 흩어지는 꽃잎
   źródło: Bufs.json :: dataList[id=DongbaekScatterPetal].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekScatterPetal]`
   limit: do 40 znaków
   EN: Scattering Petals
   PL: Rozsypujące się Płatki
355. [Status [DongbaekScatterPetal] — opis] 턴 종료 시 수치가 6 이상이면 흐트러짐 상태가 됨
   źródło: Bufs.json :: dataList[id=DongbaekScatterPetal].desc
   limit: do 120 znaków
   EN: Turn End: At 6+ Count, become staggered
   PL: Na koniec tury, przy wartości 6 lub wyższej, zostaje oszołomiony
356. [Status [CrimsonResultUp] — nazwa] 분노 위력 증가
   źródło: Bufs.json :: dataList[id=CrimsonResultUp].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonResultUp]`
   limit: do 40 znaków
   EN: Wrath Power Up
   PL: Wzrost Mocy Gniewu
357. [Status [CrimsonResultUp] — opis] 이번 턴 동안 분노 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=CrimsonResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath Skill Final Power +{0} for this turn
   PL: W tej turze Moc Końcowa Umiejętności Gniewu +{0}
358. [Status [CrimsonResultUp] — podsumowanie] 분노 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=CrimsonResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Gniewu +{0}
359. [Status [EmittedCurrent] — nazwa] 방출 전류
   źródło: Bufs.json :: dataList[id=EmittedCurrent].name
   kontekst: identyfikator statusu w tekstach: `[EmittedCurrent]`
   limit: do 40 znaków
   EN: Spark Discharge
   PL: Wyładowanie Prądu
360. [Status [EmittedCurrent] — opis] 피격 시 공격자의 충전 횟수 1 증가. 우울 속성으로 피격 시 자신의 파열 횟수 1 증가. 이후 수치 1 감소
   źródło: Bufs.json :: dataList[id=EmittedCurrent].desc
   limit: do 160 znaków
   EN: When hit, the attacker gains +1 Charge Count; when hit with a Gloom attack, gain +1 Rupture Count, then reduce Count by 1
   PL: Przy trafieniu atakujący zyskuje +1 Licznika Ładowania; przy trafieniu atakiem Posępności zyskuje +1 Licznika Rozdarcia, po czym wartość maleje o 1
361. [Status [DistortedDongrangRadiantVanity] — nazwa] 빛나는 허영
   źródło: Bufs.json :: dataList[id=DistortedDongrangRadiantVanity].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangRadiantVanity]`
   limit: do 40 znaków
   EN: Radiant Vanity
   PL: Jaśniejąca Próżność
362. [Status [DistortedDongrangRadiantVanity] — opis] 턴 시작 시 동랑에게 보호 1, 공격 위력 증가 1 부여
   źródło: Bufs.json :: dataList[id=DistortedDongrangRadiantVanity].desc
   limit: do 120 znaków
   EN: Turn Start: Dongrang gains 1 Protection and 1 Attack Power Up
   PL: Na początku tury Dongrang zyskuje 1 Ochrony i 1 Wzrost Mocy Ataku
363. [Status [DistortedDongrangEmptyMark] — nazwa] 텅 빈 징표
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptyMark].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangEmptyMark]`
   limit: do 40 znaków
   EN: Empty Mark
   PL: Pusty Ślad
364. [Status [DistortedDongrangEmptyMark] — opis] 동랑의 타겟이 됨. 매 턴 시작 시 속박 2를 얻고, 동랑에게 받는 피해량 +50%
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptyMark].desc
   limit: do 120 znaków
   EN: Targeted by Dongrang. Gain 2 Bind every turn, and take +50% damage from Dongrang.
   PL: Staje się celem Dongranga. Na początku każdej tury zyskuje 2 Spętań i otrzymuje +50% obrażeń od Dongranga
365. [Status [DistortedDongrangEarnestAchievement] — nazwa] 간절한 성과
   źródło: Bufs.json :: dataList[id=DistortedDongrangEarnestAchievement].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangEarnestAchievement]`
   limit: do 40 znaków
   EN: Earnest Accomplishment
   PL: Gorliwy Dorobek
366. [Status [DistortedDongrangEarnestAchievement] — opis] 이 유닛의 체력을 1로 만들거나, 처치하면 공격자가 강화 효과를 얻음
   źródło: Bufs.json :: dataList[id=DistortedDongrangEarnestAchievement].desc
   limit: do 120 znaków
   EN: If this unit is defeated or its HP is brought to 1, the attacker gains buffs
   PL: Gdy ta jednostka zostaje pokonana lub jej HP spada do 1, atakujący zyskuje wzmocnienie
367. [Status [DistortedDongrangEmptyHonor] — nazwa] 공허한 영예
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptyHonor].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangEmptyHonor]`
   limit: do 40 znaków
   EN: Empty Honor
   PL: Pusta Chwała
368. [Status [DistortedDongrangEmptyHonor] — opis] 동랑이 이 유닛을 처치하면, 체력을 잃은 뒤 공허함 1을 얻고 다음 턴에 약화됨
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptyHonor].desc
   limit: do 120 znaków
   EN: If Dongrang defeats this unit, he loses HP, gains 1 Emptiness, and is weakened next turn
   PL: Gdy Dongrang pokona tę jednostkę, traci HP, zyskuje 1 Pustki i w następnej turze zostaje osłabiony
369. [Status [DistortedDongrangMomentaryGlory] — nazwa] 찰나의 영광
   źródło: Bufs.json :: dataList[id=DistortedDongrangMomentaryGlory].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangMomentaryGlory]`
   limit: do 40 znaków
   EN: Momentary Glory
   PL: Chwalebna Chwila
370. [Status [DistortedDongrangMomentaryGlory] — opis] 수치가 3 이상이면 동랑이 강화 상태가 됨
   źródło: Bufs.json :: dataList[id=DistortedDongrangMomentaryGlory].desc
   limit: do 120 znaków
   EN: At 3+ Count, Dongrang becomes more powerful
   PL: Przy wartości 3 lub wyższej Dongrang zostaje wzmocniony
371. [Status [DistortedDongrangEmptiness] — nazwa] 공허함
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptiness].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangEmptiness]`
   limit: do 40 znaków
   EN: Emptiness
   PL: Pustka
372. [Status [DistortedDongrangEmptiness] — opis] 수치가 4 이상이면 동랑이 흐트러짐 상태가 됨
   źródło: Bufs.json :: dataList[id=DistortedDongrangEmptiness].desc
   limit: do 120 znaków
   EN: At 4+ Count, Dongrang becomes staggered.
   PL: Przy wartości 4 lub wyższej Dongrang zostaje oszołomiony
373. [Status [DistortedDongrangFruition] — nazwa] 맺힌 결실
   źródło: Bufs.json :: dataList[id=DistortedDongrangFruition].name
   kontekst: identyfikator statusu w tekstach: `[DistortedDongrangFruition]`
   limit: do 40 znaków
   EN: Borne Fruition
   PL: Dojrzały Owoc
374. [Status [DistortedDongrangFruition] — opis] 이 유닛을 처치한 대상은 체력을 회복하고, 다음 턴에 신속 1, 공격 위력 증가 1을 얻음
   źródło: Bufs.json :: dataList[id=DistortedDongrangFruition].desc
   limit: do 120 znaków
   EN: The unit that defeated this unit heals HP, and gains 1 Haste and 1 Attack Power Up next turn
   PL: Jednostka, która pokonała tę jednostkę, leczy HP, a w następnej turze zyskuje 1 Pośpiechu i 1 Wzrost Mocy Ataku
375. [Status [EgoAwakenDongrangRadiantDesire] — nazwa] 빛나는 욕망
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangRadiantDesire].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangRadiantDesire]`
   limit: do 40 znaków
   EN: Radiant Desire
   PL: Jaśniejące Pożądanie
376. [Status [EgoAwakenDongrangRadiantDesire] — opis] 동랑이 턴 시작 시 피해량 증가, 보호 1을 얻음
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangRadiantDesire].desc
   limit: do 120 znaków
   EN: Turn Start: Dongrang gains 1 Damage Up and 1 Protection
   PL: Na początku tury Dongrang zyskuje 1 Wzrost Obrażeń i 1 Ochrony
377. [Status [EgoAwakenDongrangSeed] — nazwa] 씨앗
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangSeed].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangSeed]`
   limit: do 40 znaków
   EN: Seeds
   PL: Nasiona
378. [Status [EgoAwakenDongrangSeed] — opis] 턴 종료 시 수치가 5 이상이면, 2턴 동안 양분 흡수 상태가 됨. 수치가 5 미만이면 수치 1 감소
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangSeed].desc
   limit: do 130 znaków
   EN: Turn End: At 5+ Count, gain Nutrient Drain for 2 turns; at less than 5 Count, reduce Count by 1
   PL: Na koniec tury, przy wartości 5+, przechodzi w stan Poboru Substancji na 2 tury; poniżej 5 wartość maleje o 1
379. [Status [EgoAwakenDongrangTree] — nazwa] 양분 흡수
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangTree].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangTree]`
   limit: do 40 znaków
   EN: Nutrient Drain
   PL: Pobór Substancji
380. [Status [EgoAwakenDongrangTree] — opis] 턴 종료 시 동랑의 체력 10 회복
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangTree].desc
   limit: do 120 znaków
   EN: Turn End: Dongrang heals 10 HP
   PL: Na koniec tury Dongrang odzyskuje 10 HP
381. [Status [EgoAwakenDongrangOverHeal] — nazwa] 과잉 회복
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangOverHeal].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangOverHeal]`
   limit: do 40 znaków
   EN: Overheal
   PL: Nadmierna Regeneracja
382. [Status [EgoAwakenDongrangOverHeal] — opis] 동랑이 회복시킨 체력만큼 수치 증가. 수치가 50 이상이 되면 수치만큼 탐식 피해를 주고, 다음 턴에 취약 5 부여 후 효과가 소멸됨.
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangOverHeal].desc
   limit: do 200 znaków
   EN: Count rises by the amount of HP Dongrang caused to heal; at 50+ Count, take Gluttony damage by the effect's Count, gain 5 Fragile, and remove the effect.
   PL: Wartość rośnie o HP wyleczone przez Dongranga; przy wartości 50+ otrzymuje tyle obrażeń Obżarstwem, ile wynosi wartość, a w następnej turze 5 Wrażliwości, po czym efekt znika.
383. [Status [SinkingSurge] — nazwa] 침잠쇄도
   źródło: Bufs.json :: dataList[id=SinkingSurge].name
   kontekst: identyfikator statusu w tekstach: `[SinkingSurge]`
   limit: do 40 znaków
   EN: Sinking Deluge
   PL: Powódź Zatonięcia
384. [Status [SinkingSurge] — opis] (침잠 횟수 x 침잠 위력)만큼 정신 피해를 주고, 침잠 제거\n대상의 정신력이 -45 이하면 초과된 정신 피해를 우울 속성 피해로 가함.\n(정신력이 없는 대상에게는 전부 우울 속성 피해로 적용됨)
   źródło: Bufs.json :: dataList[id=SinkingSurge].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal SP damage by (Sinking Count * Sinking Potency), then remove Sinking\nIf target's SP is -45 or lower, the excess SP damage is dealt as Gloom-affinity HP damage\n(Non-SP Units take all of it as Gloom HP damage)
   PL: Zadaje (Licznik Zatonięcia x Moc Zatonięcia) obrażeń Poczytalności i usuwa Zatonięcie\nJeśli Poczytalność celu wynosi -45 lub mniej, nadwyżka obrażeń Poczytalności trafia jako obrażenia Posępnością\n(Jednostki bez Poczytalności otrzymują całość jako obrażenia Posępnością)
385. [Status [Blue] — nazwa] 눈물
   źródło: Bufs.json :: dataList[id=Blue].name
   kontekst: identyfikator statusu w tekstach: `[Blue]`
   limit: do 40 znaków
   EN: Tears
   PL: Łzy
386. [Status [Blue] — opis] 턴 종료 시, 자신의 정신력 5 감소.\n뒷면 적중 시 침잠 2 부여
   źródło: Bufs.json :: dataList[id=Blue].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 5 SP\nTails Coins inflict 2 Sinking
   PL: Na koniec tury traci 5 Poczytalności.\nMonety rewersu nadają 2 Zatonięcia
387. [Status [AmberResultUp] — nazwa] 나태 위력 증가
   źródło: Bufs.json :: dataList[id=AmberResultUp].name
   kontekst: identyfikator statusu w tekstach: `[AmberResultUp]`
   limit: do 40 znaków
   EN: Sloth Power Up
   PL: Wzrost Mocy Lenistwa
388. [Status [AmberResultUp] — opis] 이번 턴 동안 나태 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=AmberResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth Skill Final Power +{0} for this turn
   PL: W tej turze Moc Końcowa Umiejętności Lenistwa +{0}
389. [Status [AmberResultUp] — podsumowanie] 나태 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=AmberResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Lenistwa +{0}
390. [Status [EgoAwakenDongrangTreeDisplay] — nazwa] 양분 흡수
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangTreeDisplay].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangTreeDisplay]`
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Status [EgoAwakenDongrangTreeDisplay] — opis] 턴 종료 시 동랑의 체력 10 회복
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangTreeDisplay].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Status [DongbaekFullBloomDisplay] — nazwa] 만개
   źródło: Bufs.json :: dataList[id=DongbaekFullBloomDisplay].name
   kontekst: identyfikator statusu w tekstach: `[DongbaekFullBloomDisplay]`
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Status [DongbaekFullBloomDisplay] — opis] 행동 불가\n턴 종료 시 정신력 -20. 정신력이 -45가 된 경우 정신력을 최대로 회복하고, 다음 턴에 아찔한 정신 상태가 됨\n2턴 동안 해제되지 않으면, 턴 종료 시 상태 해제
   źródło: Bufs.json :: dataList[id=DongbaekFullBloomDisplay].desc
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Status [EgoAwakenDongrangShardOfBrokenConnection] — nazwa] 부서진 인연의 조각
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangShardOfBrokenConnection].name
   kontekst: identyfikator statusu w tekstach: `[EgoAwakenDongrangShardOfBrokenConnection]`
   limit: do 40 znaków
   EN: Piece of a Broken Bond
   PL: Odłamek Zerwanej Więzi
395. [Status [EgoAwakenDongrangShardOfBrokenConnection] — opis] 이상의 모든 스킬의 최종 위력 +2\n아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 신속, 공격 위력 증가 1을 얻음 (턴 당 1회)\n이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 이상이 사망하지 않음
   źródło: Bufs.json :: dataList[id=EgoAwakenDongrangShardOfBrokenConnection].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yi Sang's skills gain +2 Final Power\nWhen an ally dies, remaining allies gain 1 Haste and 1 Attack Power Up next turn (Once per turn)\nAs long as at least one other ally is alive in this battle, Yi Sang does not die
   PL: Moc Końcowa wszystkich Umiejętności Yi Sanga +2\nPo śmierci sojusznika pozostali sojusznicy zyskują na koniec tury w następnej turze Pośpiech i 1 Wzrost Mocy Ataku (raz na turę)\nDopóki w tej walce żyje co najmniej 1 inny sojusznik, Yi Sang nie ginie
396. [Status [Choice_1040301] — nazwa] 알 수 없는 상처
   źródło: Bufs.json :: dataList[id=Choice_1040301].name
   kontekst: identyfikator statusu w tekstach: `[Choice_1040301]`
   limit: do 40 znaków
   EN: Unknown Wound
   PL: Nieznana Rana
397. [Status [Choice_1040301] — opis] 이번 턴동안 파열 10을 얻음.
   źródło: Bufs.json :: dataList[id=Choice_1040301].desc
   limit: do 120 znaków
   EN: Gain 10 Rupture for this turn.
   PL: W tej turze zyskuje Rozdarcie 10.
398. [Status [Choice_1040301] — podsumowanie] 턴동안 파열 10을 얻음
   źródło: Bufs.json :: dataList[id=Choice_1040301].summary
   limit: do 120 znaków
   EN: Gain 10 Rupture for the turn
   PL: W tej turze zyskuje Rozdarcie 10
399. [Status [TakeHpHealIncrease] — nazwa] 체력 회복 증가
   źródło: Bufs.json :: dataList[id=TakeHpHealIncrease].name
   kontekst: identyfikator statusu w tekstach: `[TakeHpHealIncrease]`
   limit: do 40 znaków
   EN: HP Healing Boost
   PL: Wzrost Leczenia HP
400. [Status [TakeHpHealIncrease] — opis] 이번 턴 동안 패시브, 스킬, 코인의 효과로 회복하는 체력 +{0}0% (최대 5)
   źródło: Bufs.json :: dataList[id=TakeHpHealIncrease].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Heal +{0}0% HP from Passives, Skills, and Coin effects this turn. (Max 5)
   PL: W tej turze odzyskuje o {0}0% więcej HP dzięki Pasywom, Umiejętnościom i efektom Monet (maks. 5)
401. [Status [TakeHpHealIncrease] — podsumowanie] 체력 회복량 +{0}0%
   źródło: Bufs.json :: dataList[id=TakeHpHealIncrease].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: HP Healing +{0}0%
   PL: Odzyskiwane HP +{0}0%
402. [Status [Choice_90104001] — nazwa] 이해
   źródło: Bufs.json :: dataList[id=Choice_90104001].name
   kontekst: identyfikator statusu w tekstach: `[Choice_90104001]`
   limit: do 40 znaków
   EN: Understanding
   PL: Zrozumienie
403. [Status [Choice_90104001] — opis] 이번 전투 시작 시 모든 속성의 E.G.O 자원+2
   źródło: Bufs.json :: dataList[id=Choice_90104001].desc
   limit: do 120 znaków
   EN: At the start of the battle, gain 2 E.G.O resources for every Affinity
   PL: Na początku tej walki +2 zasobów E.G.O każdego atrybutu
404. [Status [Choice_90104001] — podsumowanie] 모든 속성 E.G.O 자원 +2
   źródło: Bufs.json :: dataList[id=Choice_90104001].summary
   limit: do 120 znaków
   EN: Gain +2 E.G.O resource for all Affinities
   PL: Zasoby E.G.O wszystkich atrybutów +2
405. [Status [Choice_9010400101] — nazwa] 각오
   źródło: Bufs.json :: dataList[id=Choice_9010400101].name
   kontekst: identyfikator statusu w tekstach: `[Choice_9010400101]`
   limit: do 40 znaków
   EN: Determined
   PL: Postanowienie
406. [Status [Choice_9010400101] — opis] 이번 전투 동안 모든 인격이 최종 스킬 위력 +2
   źródło: Bufs.json :: dataList[id=Choice_9010400101].desc
   limit: do 120 znaków
   EN: All Ally Units gain +2 Skill Final Power for this battle
   PL: W tej walce wszystkie osobowości zyskują Moc Końcową Umiejętności +2
407. [Status [Choice_9010400101] — podsumowanie] 최종 스킬 위력 +2
   źródło: Bufs.json :: dataList[id=Choice_9010400101].summary
   limit: do 120 znaków
   EN: Skill Final Power +2
   PL: Moc Końcowa Umiejętności +2
408. [Status [Choice_90104002] — nazwa] 회모
   źródło: Bufs.json :: dataList[id=Choice_90104002].name
   kontekst: identyfikator statusu w tekstach: `[Choice_90104002]`
   limit: do 40 znaków
   EN: Longing
   PL: Tęsknota
409. [Status [Choice_90104002] — opis] 이번 전투 동안 모든 인격이 스킬 위력 +1
   źródło: Bufs.json :: dataList[id=Choice_90104002].desc
   limit: do 120 znaków
   EN: All Ally Units gain +1 Skill Power for this battle
   PL: W tej walce wszystkie osobowości zyskują Moc Umiejętności +1
410. [Status [Choice_90104002] — podsumowanie] 스킬 위력 +1
   źródło: Bufs.json :: dataList[id=Choice_90104002].summary
   limit: do 120 znaków
   EN: Skill Power +1
   PL: Moc Umiejętności +1
411. [Status [S2Mirror2ndFloor] — nazwa] 거울의 거울 - 2층
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror2ndFloor]`
   limit: do 40 znaków
   EN: Mirror of Mirrors - F2
   PL: Lustro Luster - Piętro 2
412. [Status [S2Mirror2ndFloor] — opis] 스킬 최종 위력 1 증가
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor].desc
   limit: do 120 znaków
   EN: Skill Final Power +1
   PL: Moc Końcowa Umiejętności +1
413. [Status [S2Mirror2ndFloor] — podsumowanie] 스킬 최종 위력 1 증가
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor].summary
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Status [S2Mirror3rdFloor] — nazwa] 거울의 거울 - 3층
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror3rdFloor]`
   limit: do 40 znaków
   EN: Mirror of Mirrors - F3
   PL: Lustro Luster - Piętro 3
415. [Status [S2Mirror3rdFloor] — opis] 스킬 최종 위력 1 증가\n공격 레벨 3 증가
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +1\nSkill Offense Level +3
   PL: Moc Końcowa Umiejętności +1\nPoziom Ataku +3
416. [Status [S2Mirror3rdFloor] — podsumowanie] 스킬 최종 위력 1 증가. 공격 레벨 3 증가.
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor].summary
   limit: do 120 znaków
   EN: Skill Final Power +1; Skill Offense Level +3
   PL: Moc Końcowa Umiejętności +1. Poziom Ataku +3.
417. [Status [S2Mirror4thFloor] — nazwa] 거울의 거울 - 4층
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror4thFloor]`
   limit: do 40 znaków
   EN: Mirror of Mirrors - F4
   PL: Lustro Luster - Piętro 4
418. [Status [S2Mirror4thFloor] — opis] 스킬 최종 위력 1 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +1\nSkill Offense Level +3\nSkill Base Power +1
   PL: Moc Końcowa Umiejętności +1\nPoziom Ataku +3\nMoc Bazowa Umiejętności +1
419. [Status [S2Mirror4thFloor] — podsumowanie] 스킬 최종 위력 1 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가.
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor].summary
   limit: do 120 znaków
   EN: Skill Final Power +1; Skill Offense Level +3; Skill Base Power +1
   PL: Moc Końcowa Umiejętności +1. Poziom Ataku +3. Moc Bazowa Umiejętności +1.
420. [Status [S2Mirror5thFloor] — nazwa] 거울의 거울 - 5층
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror5thFloor]`
   limit: do 40 znaków
   EN: Mirror of Mirrors - F5
   PL: Lustro Luster - Piętro 5
421. [Status [S2Mirror5thFloor] — opis] 스킬 최종 위력 1 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +1\nSkill Offense Level +3\nSkill Base Power +1\nSkill Plus Coin Power +2\nSkill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +1\nPoziom Ataku +3\nMoc Bazowa Umiejętności +1\nMoc Monet Plus Umiejętności +2\nMoc Monet Minus Umiejętności -2
422. [Status [S2Mirror5thFloor] — podsumowanie] 스킬 최종 위력 1 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor].summary
   limit: do 160 znaków
   EN: Skill Final Power +1; Skill Offense Level +3; Skill Base Power +1; Skill Plus Coin Power +2; Skill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +1. Poziom Ataku +3. Moc Bazowa Umiejętności +1. Moc Monet Plus Umiejętności +2. Moc Monet Minus Umiejętności -2.
423. [Status [SkillPowerUp] — nazwa] 기본 위력 증가
   źródło: Bufs.json :: dataList[id=SkillPowerUp].name
   kontekst: identyfikator statusu w tekstach: `[SkillPowerUp]`
   limit: do 40 znaków
   EN: Base Power Up
   PL: Wzrost Mocy Bazowej
424. [Status [SkillPowerUp] — opis] 스킬 기본 위력 {0}만큼 증가
   źródło: Bufs.json :: dataList[id=SkillPowerUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Base Power +{0} for this turn.
   PL: Moc Bazowa Umiejętności rośnie o {0}
425. [Status [SkillPowerUp] — podsumowanie] 스킬 기본 위력 {0}만큼 증가
   źródło: Bufs.json :: dataList[id=SkillPowerUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Base Power +{0}
   PL: Moc Bazowa Umiejętności +{0}
426. [Status [MaxHpMultiplier] — nazwa] 최대 체력 증가
   źródło: Bufs.json :: dataList[id=MaxHpMultiplier].name
   kontekst: identyfikator statusu w tekstach: `[MaxHpMultiplier]`
   limit: do 40 znaków
   EN: Max HP Up
   PL: Wzrost Maks. HP
427. [Status [MaxHpMultiplier] — opis] 최대 체력 {0}0만큼 증가
   źródło: Bufs.json :: dataList[id=MaxHpMultiplier].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase Max HP by {0}0
   PL: Maks. HP +{0}0
428. [Status [MaxHpMultiplier] — podsumowanie] 최대 체력 {0}0만큼 증가
   źródło: Bufs.json :: dataList[id=MaxHpMultiplier].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Max HP +{0}0
   PL: Maks. HP +{0}0
429. [Status [StickCoinHeadAndTailToMaxPer] — nazwa] 맞물린 가능성
   źródło: Bufs.json :: dataList[id=StickCoinHeadAndTailToMaxPer].name
   kontekst: identyfikator statusu w tekstach: `[StickCoinHeadAndTailToMaxPer]`
   limit: do 40 znaków
   EN: Meshed Possibilities
   PL: Sprzężone Możliwości
430. [Status [StickCoinHeadAndTailToMaxPer] — opis] 세 번째 턴마다 사용하는 아군 인격 스킬의 코인 결과가 종류에 따라 전부 앞면 혹은 뒷면으로 결정됨
   źródło: Bufs.json :: dataList[id=StickCoinHeadAndTailToMaxPer].desc
   limit: do 140 znaków
   EN: Every three turns, all Coins on each skill used by allies land on the same side depending on the Coin's type
   PL: Co trzy tury wszystkie Monety w Umiejętnościach używanych przez sojuszników wypadają na tę samą stronę zależnie od rodzaju Monety
431. [Status [StickCoinHeadAndTailToMaxPer] — podsumowanie] 세 번째 턴마다 전부 코인 종류에 따라 앞면 혹은 뒷면이 됨
   źródło: Bufs.json :: dataList[id=StickCoinHeadAndTailToMaxPer].summary
   limit: do 120 znaków
   EN: Every 3 turns, all Coins land on the same side based on the type
   PL: Co trzy tury wszystkie Monety wypadają na tę samą stronę zależnie od rodzaju
432. [Status [RemoveBreakSection] — nazwa] 굳센 정신
   źródło: Bufs.json :: dataList[id=RemoveBreakSection].name
   kontekst: identyfikator statusu w tekstach: `[RemoveBreakSection]`
   limit: do 40 znaków
   EN: Stalwart Spirit
   PL: Niezłomny Duch
433. [Status [RemoveBreakSection] — opis] 아군 인격의 첫 번째 흐트러짐 구간을 무효로 함
   źródło: Bufs.json :: dataList[id=RemoveBreakSection].desc
   limit: do 120 znaków
   EN: The 1st stagger thresholds of allies are nullified
   PL: Unieważnia pierwszy Próg Oszołomienia sojuszników
434. [Status [RemoveBreakSection] — podsumowanie] 첫 흐트러짐 구간을 무효로 함
   źródło: Bufs.json :: dataList[id=RemoveBreakSection].summary
   limit: do 120 znaków
   EN: Nullify 1st stagger threshold
   PL: Unieważnia pierwszy Próg Oszołomienia
435. [Status [KCorpSerum] — nazwa] K사 앰플
   źródło: Bufs.json :: dataList[id=KCorpSerum].name
   kontekst: identyfikator statusu w tekstach: `[KCorpSerum]`
   limit: do 40 znaków
   EN: K Corp Ampule
   PL: Ampułka Korporacji K
436. [Status [KCorpSerum] — opis] 턴 시작 시 4 미만이면, 최대 체력의 ({0} X 5) %만큼 체력 회복.\n수치가 4 이상이면, 사망
   źródło: Bufs.json :: dataList[id=KCorpSerum].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Turn Start: At less than 4 Count, heal by ({0} * 5)% of Max HP\nAt 4+ Count, the unit dies
   PL: Na początek tury przy wartości poniżej 4 odzyskuje HP równe ({0} x 5)% Maks. HP.\nPrzy wartości 4 lub więcej umiera
437. [Status [Talisman] — nazwa] 부적
   źródło: Bufs.json :: dataList[id=Talisman].name
   kontekst: identyfikator statusu w tekstach: `[Talisman]`
   limit: do 40 znaków
   EN: Talisman
   PL: Talizman
438. [Status [Talisman] — opis] 최댓값 : 6\n- 공격 적중 시 대상의 파열 횟수를 1 소모하여 (수치/2)만큼 파열 부여 (파열 횟수를 소모한 경우 최소 1 부여. 소수점 버림)\n- 피격 시 (수치/2)만큼 파열을 얻고 수치 1 감소 (최소 1 얻음, 소수점 버림)\n- 턴 종료 시 수치가 6 이상이면, 부적을 전부 소모하고 수치만큼 고정 피해를 받음
   źródło: Bufs.json :: dataList[id=Talisman].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 6\nOn Hit, consume 1 Rupture Count on target to inflict (Stack / 2) Rupture (inflicts at least 1 Rupture if Rupture Count was consumed; rounded down)\nWhen hit, gain (Stack / 2) Rupture and lose 1 Stack (gain at least 1 Rupture; rounded down)\nTurn End: at 6+ Stack, remove all Talisman on self and take fixed damage by Stack
   PL: Maks.: 6\n- Przy trafieniu atakiem zużywa 1 Licznika Rozdarcia celu, by nadać (wartość/2) Rozdarcia (przy zużytym Liczniku nadaje co najmniej 1; zaokrąglone w dół)\n- Przy trafieniu zyskuje (wartość/2) Rozdarcia, a wartość maleje o 1 (co najmniej 1; zaokrąglone w dół)\n- Na koniec tury, przy wartości 6 lub wyższej, zużywa wszystkie Talizmany i otrzymuje obrażenia stałe równe wartości
439. [Status [Talisman] — podsumowanie] 공격 적중 시 파열 횟수를 소모하여 파열 부여, 피격 시 파열 얻고 수치 1 감소
   źródło: Bufs.json :: dataList[id=Talisman].summary
   limit: do 130 znaków
   EN: On Hit, consume Rupture Count on target to inflict Rupture; when hit, gain Rupture and lose 1 Stack
   PL: Przy trafieniu zużywa Licznik Rozdarcia celu, by nadać Rozdarcie; przy trafieniu zyskuje Rozdarcie, a wartość maleje o 1
440. [Status [S2Mirror2ndFloor_Hard] — nazwa] 거울의 거울 어려움 - 2층
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor_Hard].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror2ndFloor_Hard]`
   limit: do 40 znaków
   EN: Mirror of Mirrors Hard - F2
   PL: Lustro Luster — Trudny - Piętro 2
441. [Status [S2Mirror2ndFloor_Hard] — opis] 스킬 최종 위력 1 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor_Hard].desc
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Status [S2Mirror2ndFloor_Hard] — podsumowanie] 스킬 최종 위력 1 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror2ndFloor_Hard].summary
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Status [S2Mirror3rdFloor_Hard] — nazwa] 거울의 거울 어려움 - 3층
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor_Hard].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror3rdFloor_Hard]`
   limit: do 40 znaków
   EN: Mirror of Mirrors Hard - F3
   PL: Lustro Luster — Trudny - Piętro 3
444. [Status [S2Mirror3rdFloor_Hard] — opis] 스킬 최종 위력 2 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor_Hard].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +2\nSkill Offense Level +3\nSkill Base Power +1\nSkill Plus Coin Power +2\nSkill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +2\nPoziom Ataku +3\nMoc Bazowa Umiejętności +1\nMoc Monet Plus Umiejętności +2\nMoc Monet Minus Umiejętności -2
445. [Status [S2Mirror3rdFloor_Hard] — podsumowanie] 스킬 최종 위력 2 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror3rdFloor_Hard].summary
   limit: do 160 znaków
   EN: Skill Final Power +2; Skill Offense Level +3; Skill Base Power +1; Skill Plus Coin Power +2; Skill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +2. Poziom Ataku +3. Moc Bazowa Umiejętności +1. Moc Monet Plus Umiejętności +2. Moc Monet Minus Umiejętności -2.
446. [Status [S2Mirror4thFloor_Hard] — nazwa] 거울의 거울 어려움 - 4층
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor_Hard].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror4thFloor_Hard]`
   limit: do 40 znaków
   EN: Mirror of Mirrors Hard - F4
   PL: Lustro Luster — Trudny - Piętro 4
447. [Status [S2Mirror4thFloor_Hard] — opis] 스킬 최종 위력 3 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor_Hard].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +3\nSkill Offense Level +3\nSkill Base Power +1\nSkill Plus Coin Power +2\nSkill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +3\nPoziom Ataku +3\nMoc Bazowa Umiejętności +1\nMoc Monet Plus Umiejętności +2\nMoc Monet Minus Umiejętności -2
448. [Status [S2Mirror4thFloor_Hard] — podsumowanie] 스킬 최종 위력 3 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror4thFloor_Hard].summary
   limit: do 160 znaków
   EN: Skill Final Power +3; Skill Offense Level +3; Skill Base Power +1; Skill Plus Coin Power +2; Skill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +3. Poziom Ataku +3. Moc Bazowa Umiejętności +1. Moc Monet Plus Umiejętności +2. Moc Monet Minus Umiejętności -2.
449. [Status [S2Mirror5thFloor_Hard] — nazwa] 거울의 거울 어려움 - 5층
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor_Hard].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror5thFloor_Hard]`
   limit: do 40 znaków
   EN: Mirror of Mirrors Hard - F5
   PL: Lustro Luster — Trudny - Piętro 5
450. [Status [S2Mirror5thFloor_Hard] — opis] 스킬 최종 위력 5 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor_Hard].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Final Power +5\nSkill Offense Level +3\nSkill Base Power +1\nSkill Plus Coin Power +2\nSkill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +5\nPoziom Ataku +3\nMoc Bazowa Umiejętności +1\nMoc Monet Plus Umiejętności +2\nMoc Monet Minus Umiejętności -2
451. [Status [S2Mirror5thFloor_Hard] — podsumowanie] 스킬 최종 위력 5 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror5thFloor_Hard].summary
   limit: do 160 znaków
   EN: Skill Final Power +5; Skill Offense Level +3; Skill Base Power +1; Skill Plus Coin Power +2; Skill Minus Coin Power -2
   PL: Moc Końcowa Umiejętności +5. Poziom Ataku +3. Moc Bazowa Umiejętności +1. Moc Monet Plus Umiejętności +2. Moc Monet Minus Umiejętności -2.
452. [Status [S2Mirror1stFloor_Hard] — nazwa] 거울의 거울 어려움 - 1층
   źródło: Bufs.json :: dataList[id=S2Mirror1stFloor_Hard].name
   kontekst: identyfikator statusu w tekstach: `[S2Mirror1stFloor_Hard]`
   limit: do 40 znaków
   EN: Mirror of Mirrors Hard - F1
   PL: Lustro Luster — Trudny - Piętro 1
453. [Status [S2Mirror1stFloor_Hard] — opis] 스킬 최종 위력 1 증가\n공격 레벨 3 증가\n스킬 기본 위력 1 증가\n스킬 더하기 코인 위력 2 증가\n스킬 빼기 코인 위력 2 감소
   źródło: Bufs.json :: dataList[id=S2Mirror1stFloor_Hard].desc
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Status [S2Mirror1stFloor_Hard] — podsumowanie] 스킬 최종 위력 1 증가. 공격 레벨 3 증가. 스킬 기본 위력 1 증가. 스킬 더하기 코인 위력 2 증가. 스킬 빼기 코인 위력 2 감소.
   źródło: Bufs.json :: dataList[id=S2Mirror1stFloor_Hard].summary
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Status [MentalSystemResultIncrease_Typo] — nazwa] 정신력 회복 효율
   źródło: Bufs.json :: dataList[id=MentalSystemResultIncrease_Typo].name
   kontekst: identyfikator statusu w tekstach: `[MentalSystemResultIncrease_Typo]`
   limit: do 40 znaków
   EN: SP Heal Efficiency
   PL: Wydajność Leczenia Poczytalności
456. [Status [MentalSystemResultIncrease_Typo] — opis] 인격의 기본 정신력 증가 조건에 의한 정신력 회복량
   źródło: Bufs.json :: dataList[id=MentalSystemResultIncrease_Typo].desc
   limit: do 120 znaków
   EN: Amount of SP healed due to the Identity's 'Base factors increasing Sanity(SP)'
   PL: Ilość regenerowanej Poczytalności z warunków bazowych zwiększających Poczytalność osobowości
457. [Status [MentalSystemResultDecrease_Typo] — nazwa] 정신력 감소 효율
   źródło: Bufs.json :: dataList[id=MentalSystemResultDecrease_Typo].name
   kontekst: identyfikator statusu w tekstach: `[MentalSystemResultDecrease_Typo]`
   limit: do 40 znaków
   EN: SP Loss Efficiency
   PL: Wydajność Spadku Poczytalności
458. [Status [MentalSystemResultDecrease_Typo] — opis] 인격의 기본 정신력 감소 조건에 의한 정신력 감소량
   źródło: Bufs.json :: dataList[id=MentalSystemResultDecrease_Typo].desc
   limit: do 120 znaków
   EN: Amount of SP lost due to the Identity's 'Base factors decreasing Sanity(SP)'
   PL: Ilość traconej Poczytalności z warunków bazowych zmniejszających Poczytalność osobowości
459. [Status [DuelDeclaration] — nazwa] 결투 선포
   źródło: Bufs.json :: dataList[id=DuelDeclaration].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclaration]`
   limit: do 40 znaków
   EN: Declared Duel
   PL: Wyzwanie na Pojedynek
460. [Status [DuelDeclaration] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs.json :: dataList[id=DuelDeclaration].desc
   limit: do 410 znaków
   EN: In a clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power, and gains 1 Haste next turn after a successful attack. (4 times per turn) Effect lifted when the unit that declared duel declares it on a different target. Replaced when another unit declares a duel.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
461. [Status [Aggro] — nazwa] 도발치
   źródło: Bufs.json :: dataList[id=Aggro].name
   kontekst: identyfikator statusu w tekstach: `[Aggro]`
   limit: do 40 znaków
   EN: Aggro
   PL: Wartość Prowokacji
462. [Status [Aggro] — opis] 집중 전투에서 도발치가 높은 슬롯일수록 적에게 공격 받을 확률이 증가함
   źródło: Bufs.json :: dataList[id=Aggro].desc
   limit: do 130 znaków
   EN: In focused encounters, slots with higher Aggro values are more likely to be targeted by enemies.
   PL: W walkach skupionych sloty o wyższej Wartości Prowokacji są częściej atakowane przez wrogów.
463. [Status [BurstVulnerable] — nazwa] 파열 취약
   źródło: Bufs.json :: dataList[id=BurstVulnerable].name
   kontekst: identyfikator statusu w tekstach: `[BurstVulnerable]`
   limit: do 40 znaków
   EN: Rupture Fragility
   PL: Wrażliwość na Rozdarcie
464. [Status [BurstVulnerable] — opis] 이번 턴 동안 파열 효과로 받는 피해 {0} 증가
   źródło: Bufs.json :: dataList[id=BurstVulnerable].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0} damage from Rupture effects this turn.
   PL: W tej turze otrzymuje {0} więcej obrażeń od efektów Rozdarcia
465. [Status [EmergencyFeed] — nazwa] 긴급 영양 보급
   źródło: Bufs.json :: dataList[id=EmergencyFeed].name
   kontekst: identyfikator statusu w tekstach: `[EmergencyFeed]`
   limit: do 40 znaków
   EN: Emergency Nutrient Supply
   PL: Awaryjna Dostawa Substancji
466. [Status [EmergencyFeed] — opis] 턴 종료 시 총 회복한 양이 자신의 체력 15% 이상이면, 다음 턴에 몸통 부위 회복.
   źródło: Bufs.json :: dataList[id=EmergencyFeed].desc
   limit: do 140 znaków
   EN: At the end of the turn, if this unit has healed 15% of Max HP or more, the body is restored next turn.
   PL: Na koniec tury, jeśli ogół wyleczonych ilości wynosi 15% HP lub więcej, część Tułowia zostaje odtworzona w następnej turze.
467. [Status [Bullet_Crab] — nazwa] 오래된 게딱지 탄
   źródło: Bufs.json :: dataList[id=Bullet_Crab].name
   kontekst: identyfikator statusu w tekstach: `[Bullet_Crab]`
   limit: do 40 znaków
   EN: Molted Shell Shot
   PL: Pocisk ze Starego Pancerza Kraba
468. [Status [Bullet_Crab] — opis] 특정 스킬 사용 시 오래된 게딱지 탄이 소모됨
   źródło: Bufs.json :: dataList[id=Bullet_Crab].desc
   limit: do 120 znaków
   EN: Resource used by certain skills for additional effects.
   PL: Zużywany przez określone Umiejętności
469. [Status [SinkingVulnerable] — nazwa] 침잠 취약
   źródło: Bufs.json :: dataList[id=SinkingVulnerable].name
   kontekst: identyfikator statusu w tekstach: `[SinkingVulnerable]`
   limit: do 40 znaków
   EN: Sinking Fragility
   PL: Wrażliwość na Zatonięcie
470. [Status [SinkingVulnerable] — opis] 이번 턴 동안 침잠 효과로 받는 피해 +{0}
   źródło: Bufs.json :: dataList[id=SinkingVulnerable].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take +{0} damage from Sinking effects this turn.
   PL: W tej turze otrzymuje +{0} obrażeń od efektów Zatonięcia
471. [Status [BurstProtection] — nazwa] 파열 보호
   źródło: Bufs.json :: dataList[id=BurstProtection].name
   kontekst: identyfikator statusu w tekstach: `[BurstProtection]`
   limit: do 40 znaków
   EN: Rupture Protection
   PL: Ochrona przed Rozdarciem
472. [Status [BurstProtection] — opis] 이번 턴 동안 파열 효과로 받는 피해 -{0}
   źródło: Bufs.json :: dataList[id=BurstProtection].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Take -{0} damage from Rupture effects this turn.
   PL: W tej turze otrzymuje -{0} obrażeń od efektów Rozdarcia
473. [Status [PseudoLastBoss_KingCrap] — nazwa] 분.게
   źródło: Bufs.json :: dataList[id=PseudoLastBoss_KingCrap].name
   kontekst: identyfikator statusu w tekstach: `[PseudoLastBoss_KingCrap]`
   limit: do 40 znaków
   EN: Crab Rage
   PL: Wściek. Krab
474. [Status [PseudoLastBoss_KingCrap] — opis] 매 턴 시작 시 자신을 제외한 모든 아군 게에게 공격 위력 증가 1 부여하고, 소라가 파괴되지 않았으면, 보호 2를 얻음.\n스킬 사용시 대상의 정신력 5 감소.\n체력이 50% 미만이 되면 모든 부위가 공격 위력 증가 2, 취약 2를 얻음
   źródło: Bufs.json :: dataList[id=PseudoLastBoss_KingCrap].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, apply Attack Power Up to all other allied crabs, and gain 2 Protection if its Shell isn't broken.\n-5 SP to target when using a skill.\nAt 50%- HP, every part gains 2 Attack Power Up and 2 Fragile.
   PL: Na początku każdej tury nadaje 1 Wzrost Mocy Ataku wszystkim sojuszniczym krabom poza sobą, a jeśli Pancerz nie jest rozbity, zyskuje 2 Ochrony.\nPrzy użyciu Umiejętności traci 5 Poczytalności celu.\nPoniżej 50% HP wszystkie części zyskują 2 Wzrosty Mocy Ataku i 2 Wrażliwości
475. [Status [ChargeForceField] — nazwa] 충전 역장
   źródło: Bufs.json :: dataList[id=ChargeForceField].name
   kontekst: identyfikator statusu w tekstach: `[ChargeForceField]`
   limit: do 40 znaków
   EN: Charge Barrier
   PL: Bariera Ładunku
476. [Status [ChargeForceField] — opis] - ({0} x 3)만큼 보호막을 얻음.\n- ({0} x 3)만큼 보호막을 잃으면, 충전 역장 1 감소.\n- (효과가 부여된 대상이 W사 직원이면, 보호막 계수가 3 대신 5로 적용됨)\n- 턴 종료 시 충전 횟수를 충전 역장 수치만큼 얻고, 충전 역장과 충전 역장 효과로 얻는 보호막 소멸.
   źródło: Bufs.json :: dataList[id=ChargeForceField].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Gain ({0} x 3) Shield.\n- Lose 1 Charge Barrier # after losing ({0} x 3) Shield.\n- (If the unit is a W Corp. employee, ALL Charge Barrier effects activate at ({0} x 5) instead of at ({0} x 3))\n- Turn End: Gain a Charge Count for each Charge Barrier #, and Charge Barrier and Shield Gained from Charge Barrier expire completely next turn
   PL: - Zyskuje Tarczę równą ({0} x 3).\n- Traci 1 Bariery Ładunku po utracie ({0} x 3) Tarczy.\n- (Jeżeli celem efektu jest pracownik W Corp., mnożnik Tarczy wynosi 5 zamiast 3)\n- Na koniec tury zyskuje Licznik Ładowania równy wartości Bariery Ładunku, po czym Bariera Ładunku i Tarcza zyskana dzięki niej znikają.
477. [Status [SlashResultUp] — nazwa] 참격 위력 증가
   źródło: Bufs.json :: dataList[id=SlashResultUp].name
   kontekst: identyfikator statusu w tekstach: `[SlashResultUp]`
   limit: do 40 znaków
   EN: Slash Power Up
   PL: Wzrost Mocy Cięcia
478. [Status [SlashResultUp] — opis] 이번 턴 동안 참격 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=SlashResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Cięcia +{0}
479. [Status [SlashResultUp] — podsumowanie] 참격 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=SlashResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Cięcia +{0}
480. [Status [RailBuffForLine2_A_ENEMY] — nazwa] 순환
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_A_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_A_ENEMY]`
   limit: do 40 znaków
   EN: Cycle
   PL: Cykl
481. [Status [RailBuffForLine2_B_ENEMY] — nazwa] 기회주의
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_B_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_B_ENEMY]`
   limit: do 40 znaków
   EN: Opportunistic
   PL: Oportunizm
482. [Status [RailBuffForLine2_C_ENEMY] — nazwa] 경화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_C_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_C_ENEMY]`
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Status [RailBuffForLine2_D_ENEMY] — nazwa] 가속
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_D_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_D_ENEMY]`
   limit: do 40 znaków
   EN: Accelerating
   PL: Przyspieszenie
484. [Status [RailBuffForLine2_E_ENEMY] — nazwa] 흡입
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_E_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_E_ENEMY]`
   limit: do 40 znaków
   EN: Inhaling
   PL: Wdychanie
485. [Status [RailBuffForLine2_F_ENEMY] — nazwa] 갈증
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_F_ENEMY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_F_ENEMY]`
   limit: do 40 znaków
   EN: Thirsting
   PL: Pragnienie
486. [Status [RailBuffForLine2_A_ALLY] — nazwa] 참격 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_A_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_A_ALLY]`
   limit: do 40 znaków
   EN: Slash Boost
   PL: Wzmocnienie Cięcia
487. [Status [RailBuffForLine2_B_ALLY] — nazwa] 관통 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_B_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_B_ALLY]`
   limit: do 40 znaków
   EN: Pierce Boost
   PL: Wzmocnienie Przebicia
488. [Status [RailBuffForLine2_C_ALLY] — nazwa] 타격 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_C_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_C_ALLY]`
   limit: do 40 znaków
   EN: Blunt Boost
   PL: Wzmocnienie Uderzenia
489. [Status [RailBuffForLine2_D_ALLY] — nazwa] 분노 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_D_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_D_ALLY]`
   limit: do 40 znaków
   EN: Wrath Boost
   PL: Wzmocnienie Gniewu
490. [Status [RailBuffForLine2_E_ALLY] — nazwa] 색욕 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_E_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_E_ALLY]`
   limit: do 40 znaków
   EN: Lust Boost
   PL: Wzmocnienie Żądzy
491. [Status [RailBuffForLine2_F_ALLY] — nazwa] 나태 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_F_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_F_ALLY]`
   limit: do 40 znaków
   EN: Sloth Boost
   PL: Wzmocnienie Lenistwa
492. [Status [RailBuffForLine2_G_ALLY] — nazwa] 탐식 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_G_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_G_ALLY]`
   limit: do 40 znaków
   EN: Gluttony Boost
   PL: Wzmocnienie Obżarstwa
493. [Status [RailBuffForLine2_H_ALLY] — nazwa] 우울 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_H_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_H_ALLY]`
   limit: do 40 znaków
   EN: Gloom Boost
   PL: Wzmocnienie Posępności
494. [Status [RailBuffForLine2_I_ALLY] — nazwa] 오만 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_I_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_I_ALLY]`
   limit: do 40 znaków
   EN: Pride Boost
   PL: Wzmocnienie Pychy
495. [Status [RailBuffForLine2_J_ALLY] — nazwa] 질투 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_J_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_J_ALLY]`
   limit: do 40 znaków
   EN: Envy Boost
   PL: Wzmocnienie Zazdrości
496. [Status [RailBuffForLine2_K_ALLY] — nazwa] 전체 회복
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_K_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_K_ALLY]`
   limit: do 40 znaków
   EN: Heal All
   PL: Leczenie Wszystkich
497. [Status [RailBuffForLine2_L_ALLY] — nazwa] 선택 회복
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_L_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_L_ALLY]`
   limit: do 40 znaków
   EN: Heal Selected
   PL: Leczenie Wybranych
498. [Status [RailBuffForLine2_T_ALLY] — nazwa] 부활
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_T_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_T_ALLY]`
   limit: do 40 znaków
   EN: Resurrect
   PL: Odrodzenie
499. [Status [Discard] — nazwa] 버림
   źródło: Bufs.json :: dataList[id=Discard].name
   kontekst: identyfikator statusu w tekstach: `[Discard]`
   limit: do 40 znaków
   EN: Discard
   PL: Odrzut
500. [Status [Discard] — opis] - 명령 페이즈 때 선택 가능한 스킬 중 조건에 맞는 스킬을 패널에서 제거함. (수비, E.G.O 스킬 제외. 버린 스킬은 다음 스킬 목록에서 사라지지 않음)\n- 버려지는 스킬은 버림 관련 효과 외의 스킬, 코인 효과가 발동하지 않으며, 해당 스킬의 E.G.O 자원을 얻지 않음.
   źródło: Bufs.json :: dataList[id=Discard].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Delete Skills that fit the condition and are selectable during the Chaining Phase from the Dashboard. (Defensive & E.G.O Skills do not count. Does not delete the Skill from the upcoming Skills list)\n- Discarded Skills will not activate Skill effects or Coin effects other than effects from Discard, and will not give E.G.O resources.
   PL: - Usuwa z panelu poleceń Umiejętności spełniające warunek, które da się wybrać w fazie łączenia (poza Umiejętnościami obronnymi i E.G.O; odrzucona Umiejętność nie znika z nadchodzącej listy Umiejętności)\n- Odrzucone Umiejętności nie aktywują efektów Umiejętności ani monet poza efektami Odrzutu i nie dają zasobów E.G.O
501. [Status [RailBuffForLine2_M_ALLY] — nazwa] 화상 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_M_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_M_ALLY]`
   limit: do 40 znaków
   EN: Burn Boost
   PL: Wzmocnienie Podpalenia
502. [Status [RailBuffForLine2_N_ALLY] — nazwa] 출혈 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_N_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_N_ALLY]`
   limit: do 40 znaków
   EN: Bleed Boost
   PL: Wzmocnienie Krwawienia
503. [Status [RailBuffForLine2_O_ALLY] — nazwa] 진동 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_O_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_O_ALLY]`
   limit: do 40 znaków
   EN: Tremor Boost
   PL: Wzmocnienie Wstrząsu
504. [Status [RailBuffForLine2_P_ALLY] — nazwa] 파열 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_P_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_P_ALLY]`
   limit: do 40 znaków
   EN: Rupture Boost
   PL: Wzmocnienie Rozdarcia
505. [Status [RailBuffForLine2_Q_ALLY] — nazwa] 침잠 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_Q_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_Q_ALLY]`
   limit: do 40 znaków
   EN: Sinking Boost
   PL: Wzmocnienie Zatonięcia
506. [Status [RailBuffForLine2_R_ALLY] — nazwa] 호흡 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_R_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_R_ALLY]`
   limit: do 40 znaków
   EN: Poise Boost
   PL: Wzmocnienie Oddechu
507. [Status [RailBuffForLine2_S_ALLY] — nazwa] 충전 강화
   źródło: Bufs.json :: dataList[id=RailBuffForLine2_S_ALLY].name
   kontekst: identyfikator statusu w tekstach: `[RailBuffForLine2_S_ALLY]`
   limit: do 40 znaków
   EN: Charge Boost
   PL: Wzmocnienie Ładowania
508. [Status [KnowledgeExplored] — nazwa] 탐구한 지식
   źródło: Bufs.json :: dataList[id=KnowledgeExplored].name
   kontekst: identyfikator statusu w tekstach: `[KnowledgeExplored]`
   limit: do 40 znaków
   EN: Insight
   PL: Zgłębiona Wiedza
509. [Status [KnowledgeExplored] — opis] 마지막으로 버린 스킬의 등급 : {0} (기본값: 1)
   źródło: Bufs.json :: dataList[id=KnowledgeExplored].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Last Discarded Skill Rank: {0} (Base Value: 1)
   PL: Ranga ostatnio odrzuconej Umiejętności: {0} (wartość bazowa: 1)
510. [Status [Unjust_Enrichment] — nazwa] 부당 수익
   źródło: Bufs.json :: dataList[id=Unjust_Enrichment].name
   kontekst: identyfikator statusu w tekstach: `[Unjust_Enrichment]`
   limit: do 40 znaków
   EN: Unjust Enrichment
   PL: Nieprawne Wzbogacenie
511. [Status [Unjust_Enrichment] — opis] - 출혈이 부여된 대상에게 앞면 적중시 획득 (최대 4)\n- 총알은 비싸다고 패시브의 효과 발동 시 이 버프를 전부 소모하여 추가 피해를 줌
   źródło: Bufs.json :: dataList[id=Unjust_Enrichment].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gained on Heads Hit against targets that have Bleed (Max 4)\n- When 'Bullets are Pricey' Passive activates, consume all Unjust Enrichment Stack to deal bonus damage
   PL: - Zyskiwane przy trafieniu atakiem w cel z nadanym Krwawieniem (maks. 4)\n- Po aktywacji pasywu „Amunicja Jest Droga” zużywa wszystkie stosy tego wzmocnienia, by zadać dodatkowe obrażenia
512. [Status [RetaliationBook] — nazwa] 앙갚음 대상
   źródło: Bufs.json :: dataList[id=RetaliationBook].name
   kontekst: identyfikator statusu w tekstach: `[RetaliationBook]`
   limit: do 40 znaków
   EN: Vengeance Mark
   PL: Cel Odwetu
513. [Status [RetaliationBook] — opis] 이전 턴에 아군에게 스킬로 가장 많이 피해를 준 대상에게 부여됨. (최대 1회 부여 가능)
   źródło: Bufs.json :: dataList[id=RetaliationBook].desc
   limit: do 120 znaków
   EN: Applied to the unit that dealt the most damage to an ally (Max 1)
   PL: Nadawany jednostce, która zadała sojusznikowi najwięcej obrażeń w poprzedniej turze (do nadania raz na turę)
514. [Status [PenetrateResultUp] — nazwa] 관통 위력 증가
   źródło: Bufs.json :: dataList[id=PenetrateResultUp].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateResultUp]`
   limit: do 40 znaków
   EN: Pierce Power Up
   PL: Wzrost Mocy Przebicia
515. [Status [PenetrateResultUp] — opis] 이번 턴 동안 관통 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=PenetrateResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Przebicia +{0}
516. [Status [PenetrateResultUp] — podsumowanie] 관통 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=PenetrateResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Przebicia +{0}
517. [Status [DuelDeclaration_DonQuixote] — nazwa] 결투 선포 - 돈키호테
   źródło: Bufs.json :: dataList[id=DuelDeclaration_DonQuixote].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclaration_DonQuixote]`
   limit: do 40 znaków
   EN: Declared Duel - Don Quixote
   PL: Wyzwanie na Pojedynek - Don Kichot
518. [Status [DuelDeclaration_DonQuixote] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs.json :: dataList[id=DuelDeclaration_DonQuixote].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. Replaced when another unit inflicts Declared Duel on the same target.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
519. [Status [DuelDeclaration_Outis] — nazwa] 결투 선포 - 오티스
   źródło: Bufs.json :: dataList[id=DuelDeclaration_Outis].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclaration_Outis]`
   limit: do 40 znaków
   EN: Declared Duel - Outis
   PL: Wyzwanie na Pojedynek - Outis
520. [Status [DuelDeclaration_Outis] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs.json :: dataList[id=DuelDeclaration_Outis].desc
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Status [DuelDeclaration_Sinclair] — nazwa] 결투 선포 - 싱클레어
   źródło: Bufs.json :: dataList[id=DuelDeclaration_Sinclair].name
   kontekst: identyfikator statusu w tekstach: `[DuelDeclaration_Sinclair]`
   limit: do 40 znaków
   EN: Declared Duel - Sinclair
   PL: Wyzwanie na Pojedynek - Sinclair
522. [Status [DuelDeclaration_Sinclair] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: Bufs.json :: dataList[id=DuelDeclaration_Sinclair].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit that has the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. Replaced when another unit inflicts Declared Duel on the same target.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
523. [Status [VibrationExplosion] — nazwa] 진동 폭발
   źródło: Bufs.json :: dataList[id=VibrationExplosion].name
   kontekst: identyfikator statusu w tekstach: `[VibrationExplosion]`
   limit: do 40 znaków
   EN: Tremor Burst
   PL: Wybuch Wstrząsu
524. [Status [VibrationExplosion] — opis] 대상의 진동 위력만큼 흐트러짐 손상을 입힘
   źródło: Bufs.json :: dataList[id=VibrationExplosion].desc
   limit: do 120 znaków
   EN: Raise target's Stagger Threshold by Tremor Potency on target
   PL: Podnosi Próg Oszołomienia celu o Moc Wstrząsu celu
525. [Status [OneOnOneDuel] — nazwa] 1대1 대결
   źródło: Bufs.json :: dataList[id=OneOnOneDuel].name
   kontekst: identyfikator statusu w tekstach: `[OneOnOneDuel]`
   limit: do 40 znaków
   EN: Single Combat
   PL: Pojedynek Jeden na Jednego
526. [Status [OneOnOneDuel] — opis] 피격을 당하는 슬롯이 한 유닛에게만 타겟됨. 동시에 피격을 당하는 슬롯의 스킬과 합을 하는 공격 스킬과만 1대1 대결이 성립됨. (단, 스킬 재사용의 경우에는 적용되지 않음)
   źródło: Bufs.json :: dataList[id=OneOnOneDuel].desc
   limit: do 280 znaków
   EN: Established when the attacked Slot is targeted by a single unit, and only by that single unit. This condition is established only between the attacking unit and the attacked Slot. (Does not apply to reused Skills)
   PL: Tworzy się, gdy atakowany slot jest celowany wyłącznie przez jedną jednostkę, i tylko przez tę jednostkę. Stan tworzy się wyłącznie między atakującą jednostką a atakowanym slocie. (Nie dotyczy ponownie używanych Umiejętności)
527. [Status [FreischutzShotCount] — nazwa] 마탄
   źródło: Bufs.json :: dataList[id=FreischutzShotCount].name
   kontekst: identyfikator statusu w tekstach: `[FreischutzShotCount]`
   limit: do 40 znaków
   EN: Magic Bullet
   PL: Magiczna Amunicja
528. [Status [FreischutzShotCount] — opis] - 최댓값: 7\n- 특정 스킬 효과에 따라 수치가 변경됨.\n- [로보토미 E.G.O::마탄 오티스 인격 전용 효과]\n· 스킬 3 기본 위력 +{0}\n- 스킬 3 코인 위력 +{1}
   źródło: Bufs.json :: dataList[id=FreischutzShotCount].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: - Max Value: 7\n- Value changes depending on certain Skill effects.\n- [Lobotomy E.G.O::Magic Bullet Outis Only]\n· Skill 3 Base Power +{0}\n· Skill 3 Coin Power +{1}
   PL: - Maks. wartości: 7\n- Wartość zmienia się zależnie od efektów określonych Umiejętności.\n- [Efekt dla Lobotomy E.G.O::Magiczny Pocisk Otis]\n· Moc Bazowa Umiejętności 3 +{0}\n- Moc Monet Umiejętności 3 +{1}
529. [Status [DarkFlame] — nazwa] 흑염
   źródło: Bufs.json :: dataList[id=DarkFlame].name
   kontekst: identyfikator statusu w tekstach: `[DarkFlame]`
   limit: do 40 znaków
   EN: Dark Flame
   PL: Czarny Płomień
530. [Status [DarkFlame] — opis] - 특수 화상\n- 최댓값: 7\n- 대상의 방어 레벨 -{0}\n- 턴 종료 시 ({0} x 대상의 화상)만큼 오만 속성 피해를 주고, 효과 소멸
   źródło: Bufs.json :: dataList[id=DarkFlame].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Unique Burn\n- Max Value: 7\n- Target Defense Level -{0}\n- Turn End: Deal ({0} x Burn on target) Pride Affinity damage, then expires
   PL: - Specjalne Podpalenie\n- Maks. wartości: 7\n- Poziom Obrony celu -{0}\n- Na koniec tury zadaje ({0} x Podpalenie celu) obrażeń atrybutu Pychy, po czym efekt znika
531. [Status [CtrlTeamCaptain] — nazwa] 지휘팀 팀장
   źródło: Bufs.json :: dataList[id=CtrlTeamCaptain].name
   kontekst: identyfikator statusu w tekstach: `[CtrlTeamCaptain]`
   limit: do 40 znaków
   EN: Control Team Captain
   PL: Kapitan Zespołu Dowodzenia
532. [Status [CtrlTeamCaptain] — opis] - 스킬 슬롯 수 +1\n- 스킬 3 수량 +1, 대신 스킬 1 수량 -1\n- 스킬로 적 처치 시 자신을 포함하여 정신력이 가장 낮은 아군 2명 정신력 25 회복, 적을 처치한 스킬 속성의 EGO 자원 +2, 나머지 속성의 EGO 자원 +1
   źródło: Bufs.json :: dataList[id=CtrlTeamCaptain].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- When this unit defeats an enemy with a Skill, 2 allies(including this unit) with the least SP heal 25 SP. Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: - Liczba slotów Umiejętności +1\n- Modyfikuje pulę Umiejętności: +1 użycie Umiejętności 3, w zamian -1 użycie Umiejętności 1\n- Gdy ta jednostka pokona wroga Umiejętnością, 2 sojusznicy (łącznie z nią) z najniższą Poczytalnością odzyskują 25 Poczytalności; +2 zasobów E.G.O atrybutu Umiejętności, która pokonała wroga, +1 zasobów pozostałych atrybutów
533. [Status [HeatedGasHarpoon] — nazwa] 가열된 가스 작살
   źródło: Bufs.json :: dataList[id=HeatedGasHarpoon].name
   kontekst: identyfikator statusu w tekstach: `[HeatedGasHarpoon]`
   limit: do 40 znaków
   EN: Heated Gas Harpoon
   PL: Nagrzany Harpun Gazowy
534. [Status [HeatedGasHarpoon] — opis] 이번 턴 동안 공격 앞면 적중 시 화상 1 부여
   źródło: Bufs.json :: dataList[id=HeatedGasHarpoon].desc
   limit: do 120 znaków
   EN: This Turn: Inflict 1 Burn with Heads Hit
   PL: W tej turze nadaje Podpalenie 1 przy trafieniu Awersami
535. [Status [OverHeatedGasHarpoon] — nazwa] 과열된 가스 작살
   źródło: Bufs.json :: dataList[id=OverHeatedGasHarpoon].name
   kontekst: identyfikator statusu w tekstach: `[OverHeatedGasHarpoon]`
   limit: do 40 znaków
   EN: Overheated Gas Harpoon
   PL: Przegrzany Harpun Gazowy
536. [Status [OverHeatedGasHarpoon] — opis] 이번 턴 동안 공격 적중 시 화상 1 부여
   źródło: Bufs.json :: dataList[id=OverHeatedGasHarpoon].desc
   limit: do 120 znaków
   EN: This Turn: inflict 1 Burn On Hit
   PL: W tej turze nadaje Podpalenie 1 przy trafieniu
537. [Status [CoverAttack] — nazwa] 원호 공격
   źródło: Bufs.json :: dataList[id=CoverAttack].name
   kontekst: identyfikator statusu w tekstach: `[CoverAttack]`
   limit: do 40 znaków
   EN: Assist Attack
   PL: Atak Wsparcia
538. [Status [CoverAttack] — opis] - 이 효과를 부여한 대상의 공격 스킬 종료 시, 부여 대상이 공격한 적을 스킬 1로 일방 공격 함.\n- 원호 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: Bufs.json :: dataList[id=CoverAttack].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 1 against the same enemy Unit A attacked with its Skill. Activates at Unit A's Attack End.\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 1 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A.\n- Umiejętność użyta jako Atak Wsparcia nie wpływa na nadchodzącą listę Umiejętności B.
539. [Status [ReCompulsion] — nazwa] 반전 강박
   źródło: Bufs.json :: dataList[id=ReCompulsion].name
   kontekst: identyfikator statusu w tekstach: `[ReCompulsion]`
   limit: do 40 znaków
   EN: Reverse Compulsion
   PL: Odwrócona Kompulsja
540. [Status [ReCompulsion] — opis] 매 턴 시작 시 정신력 15 회복
   źródło: Bufs.json :: dataList[id=ReCompulsion].desc
   limit: do 120 znaków
   EN: Heal 15 SP at every Turn Start
   PL: Regeneruje 15 Poczytalności na początku każdej tury
541. [Status [IndigoResultUp] — nazwa] 오만 위력 증가
   źródło: Bufs.json :: dataList[id=IndigoResultUp].name
   kontekst: identyfikator statusu w tekstach: `[IndigoResultUp]`
   limit: do 40 znaków
   EN: Pride Power Up
   PL: Wzrost Mocy Pychy
542. [Status [IndigoResultUp] — opis] 이번 턴 동안 오만 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=IndigoResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Pychy +{0}
543. [Status [IndigoResultUp] — podsumowanie] 오만 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=IndigoResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Pychy +{0}
544. [Status [BladeResultUpTier1] — nazwa] 본국검 - 세법 전수
   źródło: Bufs.json :: dataList[id=BladeResultUpTier1].name
   kontekst: identyfikator statusu w tekstach: `[BladeResultUpTier1]`
   limit: do 50 znaków
   EN: Sword of the Homeland - Rending
   PL: Szermierka Ojczyzny - Cięcie
545. [Status [BladeResultUpTier1] — opis] 이번 턴 동안 스킬 1의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=BladeResultUpTier1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill 1 Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności 1 +{0}
546. [Status [BladeResultUpTier1] — podsumowanie] 스킬 1의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=BladeResultUpTier1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill 1 Final Power +{0}
   PL: Moc Końcowa Umiejętności 1 +{0}
547. [Status [BladeResultUpTier2] — nazwa] 본국검 - 자법 전수
   źródło: Bufs.json :: dataList[id=BladeResultUpTier2].name
   kontekst: identyfikator statusu w tekstach: `[BladeResultUpTier2]`
   limit: do 50 znaków
   EN: Sword of the Homeland - Penetrating
   PL: Szermierka Ojczyzny - Przebicie
548. [Status [BladeResultUpTier2] — opis] 이번 턴 동안 스킬 2의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=BladeResultUpTier2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill 2 Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności 2 +{0}
549. [Status [BladeResultUpTier2] — podsumowanie] 스킬 2의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=BladeResultUpTier2].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill 2 Final Power +{0}
   PL: Moc Końcowa Umiejętności 2 +{0}
550. [Status [SwordPlayOfTheHomeland] — nazwa] 본국검술
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheHomeland].name
   kontekst: identyfikator statusu w tekstach: `[SwordPlayOfTheHomeland]`
   limit: do 40 znaków
   EN: Swordplay of the Homeland
   PL: Szermierka Ojczyzny
551. [Status [SwordPlayOfTheHomeland] — opis] - 스킬 사용 시 호흡이 5 이상이면, 스킬 1, 2의 코인 위력 +(3/코인 수, 최소 1), 크리티컬 피해량 +(30/코인수)%\n- 스킬 사용 시 호흡이 7 이상이면, 스킬 3의 피해량 +(30/코인 수)%, 크리티컬 피해량 +(50/코인수)%
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheHomeland].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When at 5+ Poise, upon Skill use, Skill 1 and Skill 2 gain Coin Power +(3/# of Coins, minimum 1) and deal +(30/# of Coins)% damage on Critical Hit\n- When at 7+ Poise, upon Skill use, Skill 3 deals +(30/# of Coins)% damage and deals +(50/# of Coins)% damage on Critical Hit
   PL: - Przy użyciu Umiejętności, przy 5 lub więcej Oddechu, Umiejętności 1 i 2 zyskują moc monet +(3/liczba monet, min. 1) i zadają +(30/liczba monet)% obrażeń przy trafieniu krytycznym\n- Przy użyciu Umiejętności, przy 7 lub więcej Oddechu, Umiejętność 3 zadaje +(30/liczba monet)% obrażeń i +(50/liczba monet)% obrażeń przy trafieniu krytycznym
552. [Status [SwordPlayOfTheHomeland] — podsumowanie] 호흡이 일정 수치 이상이면 스킬 강화
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheHomeland].summary
   limit: do 120 znaków
   EN: Enhance Skill when over a certain Poise threshold
   PL: Wzmacnia Umiejętność przy Oddechu powyżej określonej wartości
553. [Status [SwordPlayOfTheMemorial] — nazwa] 추모
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheMemorial].name
   kontekst: identyfikator statusu w tekstach: `[SwordPlayOfTheMemorial]`
   limit: do 40 znaków
   EN: Remembrance
   PL: Pamięć
554. [Status [SwordPlayOfTheMemorial] — opis] 스킬 사용 시 호흡이 5 이상이면, 스킬 1, 2의 코인 위력 +(3/코인 수, 최소 1), 크리티컬 피해량 +(30/코인수)%\n스킬 사용 시 호흡이 7 이상이면, 스킬 3의 피해량 +(30/코인 수)%, 크리티컬 피해량 +(50/코인수)%
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheMemorial].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When at 5+ Poise, upon Skill use, Skill 1 and Skill 2 gain Coin Power +(3/# of Coins, minimum 1) and deal +(30/# of Coins)% damage on Critical Hit\nWhen at 7+ Poise, upon Skill use, Skill 3 deals +(30/# of Coins)% damage and deals +(50/# of Coins)% damage on Critical Hit
   PL: Przy użyciu Umiejętności, przy Oddechu 5 lub więcej, Moc Monet Umiejętności 1 i 2 +(3/liczba monet, min. 1), obrażenia krytyczne +(30/liczba monet)%\nPrzy użyciu Umiejętności, przy Oddechu 7 lub więcej, Umiejętność 3 zadaje +(30/liczba monet)% obrażeń, a obrażenia krytyczne rosną o +(50/liczba monet)%
555. [Status [SwordPlayOfTheMemorial] — podsumowanie] 호흡이 일정 수치 이상이면 스킬 강화
   źródło: Bufs.json :: dataList[id=SwordPlayOfTheMemorial].summary
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Status [RedApricotBlossom] — nazwa] 홍매화
   źródło: Bufs.json :: dataList[id=RedApricotBlossom].name
   kontekst: identyfikator statusu w tekstach: `[RedApricotBlossom]`
   limit: do 40 znaków
   EN: Red Plum Blossom
   PL: Czerwony Kwiat Śliwy
557. [Status [RedApricotBlossom] — opis] - 특수 출혈\n- 최댓값: 10\n- 메인 타겟이면 피격 시 크리티컬 발동 확률 +10%\n- 크리티컬로 피격 시 수치의 절반만큼 출혈을 얻고, 받는 크리티컬 피해량 + {0} x 3%\n- 피격 시 1 감소
   źródło: Bufs.json :: dataList[id=RedApricotBlossom].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Unique Bleed\n- Max value: 10\n- +10% chance for this unit to be Critically Hit if this unit is the main target\n- When struck by a Critical Hit, gain Bleed equal to the half of the value and take +({0} x 3)% damage on Critical Hit\n- Reduce value by 1 when hit
   PL: - Specjalne Krwawienie\n- Maks. wartości: 10\n- Jako główny cel: +10% szansy na otrzymanie trafienia krytycznego\n- Przy trafieniu krytycznym zyskuje Krwawienie równe połowie wartości, a otrzymywane obrażenia krytyczne rosną o {0} x 3%\n- Przy trafieniu maleje o 1
558. [Status [RedApricotBlossom] — podsumowanie] 피격 시 크리티컬 발동 확률, 받는 크리티컬 피해량 증가
   źródło: Bufs.json :: dataList[id=RedApricotBlossom].summary
   limit: do 120 znaków
   EN: Higher chance to be Critically Hit; take more damage upon Critical Hit
   PL: Wyższa szansa na trafienie krytyczne; otrzymuje więcej obrażeń krytycznych
559. [Status [ShamrockResultUp] — nazwa] 탐식 위력 증가
   źródło: Bufs.json :: dataList[id=ShamrockResultUp].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockResultUp]`
   limit: do 40 znaków
   EN: Gluttony Power Up
   PL: Wzrost Mocy Obżarstwa
560. [Status [ShamrockResultUp] — opis] 이번 턴 동안 탐식 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ShamrockResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Obżarstwa +{0}
561. [Status [ShamrockResultUp] — podsumowanie] 탐식 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ShamrockResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Obżarstwa +{0}
562. [Status [ScarletResultUp] — nazwa] 색욕 위력 증가
   źródło: Bufs.json :: dataList[id=ScarletResultUp].name
   kontekst: identyfikator statusu w tekstach: `[ScarletResultUp]`
   limit: do 40 znaków
   EN: Lust Power Up
   PL: Wzrost Mocy Żądzy
563. [Status [ScarletResultUp] — opis] 이번 턴 동안 색욕 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ScarletResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Żądzy +{0}
564. [Status [ScarletResultUp] — podsumowanie] 색욕 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=ScarletResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Żądzy +{0}
565. [Status [AzureResultUp] — nazwa] 우울 위력 증가
   źródło: Bufs.json :: dataList[id=AzureResultUp].name
   kontekst: identyfikator statusu w tekstach: `[AzureResultUp]`
   limit: do 40 znaków
   EN: Gloom Power Up
   PL: Wzrost Mocy Posępności
566. [Status [AzureResultUp] — opis] 이번 턴 동안 우울 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=AzureResultUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom Skill Final Power +{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Posępności +{0}
567. [Status [AzureResultUp] — podsumowanie] 우울 속성 스킬의 최종 위력 +{0}
   źródło: Bufs.json :: dataList[id=AzureResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Posępności +{0}
568. [Status [HitResultDown] — nazwa] 타격 위력 감소
   źródło: Bufs.json :: dataList[id=HitResultDown].name
   kontekst: identyfikator statusu w tekstach: `[HitResultDown]`
   limit: do 40 znaków
   EN: Blunt Power Down
   PL: Spadek Mocy Uderzenia
569. [Status [HitResultDown] — opis] 이번 턴 동안 타격 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=HitResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Uderzenia -{0}
570. [Status [HitResultDown] — podsumowanie] 타격 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=HitResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Blunt Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Uderzenia -{0}
571. [Status [PenetrateResultDown] — nazwa] 관통 위력 감소
   źródło: Bufs.json :: dataList[id=PenetrateResultDown].name
   kontekst: identyfikator statusu w tekstach: `[PenetrateResultDown]`
   limit: do 40 znaków
   EN: Pierce Power Down
   PL: Spadek Mocy Przebicia
572. [Status [PenetrateResultDown] — opis] 이번 턴 동안 관통 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=PenetrateResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Przebicia -{0}
573. [Status [PenetrateResultDown] — podsumowanie] 관통 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=PenetrateResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pierce Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Przebicia -{0}
574. [Status [SlashResultDown] — nazwa] 참격 위력 감소
   źródło: Bufs.json :: dataList[id=SlashResultDown].name
   kontekst: identyfikator statusu w tekstach: `[SlashResultDown]`
   limit: do 40 znaków
   EN: Slash Power Down
   PL: Spadek Mocy Cięcia
575. [Status [SlashResultDown] — opis] 이번 턴 동안 참격 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=SlashResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Cięcia -{0}
576. [Status [SlashResultDown] — podsumowanie] 참격 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=SlashResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slash Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Cięcia -{0}
577. [Status [CrimsonResultDown] — nazwa] 분노 위력 감소
   źródło: Bufs.json :: dataList[id=CrimsonResultDown].name
   kontekst: identyfikator statusu w tekstach: `[CrimsonResultDown]`
   limit: do 40 znaków
   EN: Wrath Power Down
   PL: Spadek Mocy Gniewu
578. [Status [CrimsonResultDown] — opis] 이번 턴 동안 분노 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=CrimsonResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath Skill Final Power -{0} for this turn
   PL: W tej turze Moc Końcowa Umiejętności Gniewu -{0}
579. [Status [CrimsonResultDown] — podsumowanie] 분노 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=CrimsonResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wrath Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Gniewu -{0}
580. [Status [ScarletResultDown] — nazwa] 색욕 위력 감소
   źródło: Bufs.json :: dataList[id=ScarletResultDown].name
   kontekst: identyfikator statusu w tekstach: `[ScarletResultDown]`
   limit: do 40 znaków
   EN: Lust Power Down
   PL: Spadek Mocy Żądzy
581. [Status [ScarletResultDown] — opis] 이번 턴 동안 색욕 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ScarletResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Żądzy -{0}
582. [Status [ScarletResultDown] — podsumowanie] 색욕 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ScarletResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lust Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Żądzy -{0}
583. [Status [ShamrockResultDown] — nazwa] 탐식 위력 감소
   źródło: Bufs.json :: dataList[id=ShamrockResultDown].name
   kontekst: identyfikator statusu w tekstach: `[ShamrockResultDown]`
   limit: do 40 znaków
   EN: Gluttony Power Down
   PL: Spadek Mocy Obżarstwa
584. [Status [ShamrockResultDown] — opis] 이번 턴 동안 탐식 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ShamrockResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Obżarstwa -{0}
585. [Status [ShamrockResultDown] — podsumowanie] 탐식 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=ShamrockResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gluttony Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Obżarstwa -{0}
586. [Status [AmberResultDown] — nazwa] 나태 위력 감소
   źródło: Bufs.json :: dataList[id=AmberResultDown].name
   kontekst: identyfikator statusu w tekstach: `[AmberResultDown]`
   limit: do 40 znaków
   EN: Sloth Power Down
   PL: Spadek Mocy Lenistwa
587. [Status [AmberResultDown] — opis] 이번 턴 동안 나태 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=AmberResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth Skill Final Power -{0} for this turn
   PL: W tej turze Moc Końcowa Umiejętności Lenistwa -{0}
588. [Status [AmberResultDown] — podsumowanie] 나태 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=AmberResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Lenistwa -{0}
589. [Status [AzureResultDown] — nazwa] 우울 위력 감소
   źródło: Bufs.json :: dataList[id=AzureResultDown].name
   kontekst: identyfikator statusu w tekstach: `[AzureResultDown]`
   limit: do 40 znaków
   EN: Gloom Power Down
   PL: Spadek Mocy Posępności
590. [Status [AzureResultDown] — opis] 이번 턴 동안 우울 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=AzureResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Posępności -{0}
591. [Status [AzureResultDown] — podsumowanie] 우울 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=AzureResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gloom Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Posępności -{0}
592. [Status [IndigoResultDown] — nazwa] 오만 위력 감소
   źródło: Bufs.json :: dataList[id=IndigoResultDown].name
   kontekst: identyfikator statusu w tekstach: `[IndigoResultDown]`
   limit: do 40 znaków
   EN: Pride Power Down
   PL: Spadek Mocy Pychy
593. [Status [IndigoResultDown] — opis] 이번 턴 동안 오만 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=IndigoResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Pychy -{0}
594. [Status [IndigoResultDown] — podsumowanie] 오만 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=IndigoResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pride Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Pychy -{0}
595. [Status [VioletResultDown] — nazwa] 질투 위력 감소
   źródło: Bufs.json :: dataList[id=VioletResultDown].name
   kontekst: identyfikator statusu w tekstach: `[VioletResultDown]`
   limit: do 40 znaków
   EN: Envy Power Down
   PL: Spadek Mocy Zazdrości
