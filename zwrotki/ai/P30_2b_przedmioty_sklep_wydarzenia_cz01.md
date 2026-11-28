# Paczka AI P30 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 1/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P30_2b_przedmioty_sklep_wydarzenia_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P30_2b_przedmioty_sklep_wydarzenia_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Pojęcia bazowe i cechy jednostek: KeywordDictionary
- plik gry: `KeywordDictionary.json`

1. [Pojęcia bazowe i cechy jednostek [Gcorp] — nazwa] G사
   źródło: KeywordDictionary.json :: dataList[id=Gcorp].name
   limit: do 40 znaków
   EN: G Corp.
   PL: Korp. G
2. [Pojęcia bazowe i cechy jednostek [Gcorp] — opis] G사이다.
   źródło: KeywordDictionary.json :: dataList[id=Gcorp].desc
   limit: do 120 znaków
   EN: It’s G Corp.
   PL: To Korp. G.
3. [Pojęcia bazowe i cechy jednostek [body] — nazwa] 시체
   źródło: KeywordDictionary.json :: dataList[id=body].name
   limit: do 40 znaków
   EN: Corpse
   PL: Trup
4. [Pojęcia bazowe i cechy jednostek [body] — opis] 사람 혹은 동물이 사망한 후의 육신을 칭하는 말
   źródło: KeywordDictionary.json :: dataList[id=body].desc
   limit: do 120 znaków
   EN: Corpse (NOUN): The body of a person or animal after death.
   PL: Określenie ciała człowieka lub zwierzęcia po śmierci

## Pojęcia bazowe i cechy jednostek: SynergyKeyword
- plik gry: `SynergyKeyword.json`

5. [Pojęcia bazowe i cechy jednostek [MAGICAL_GIRL] — nazwa] 마법 소녀
   źródło: SynergyKeyword.json :: dataList[id=MAGICAL_GIRL].name
   limit: do 40 znaków
   EN: Magical Girl
   PL: Czarodziejka
6. [Pojęcia bazowe i cechy jednostek [FOURTH_MATCH_FLAME] — nazwa] 4번째 성냥불
   źródło: SynergyKeyword.json :: dataList[id=FOURTH_MATCH_FLAME].name
   limit: do 40 znaków
   EN: 4th Match Flame
   PL: 4. Płomyk Zapałki

## Statusy i efekty bojowe — BuffAbilities
- plik gry: `BuffAbilities.json`

7. [Status [AtkDamageMultiplier] — opis] 가하는 피해량 {0}%
   źródło: BuffAbilities.json :: dataList[id=AtkDamageMultiplier].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}% to damage dealt
   PL: Zadawane obrażenia {0}%
8. [Status [AtkDamageMultiplier] — wariant opisu 1] {0} 속성 스킬로 가하는 피해량 {1}%
   źródło: BuffAbilities.json :: dataList[id=AtkDamageMultiplier].variation
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1}% to damage dealt with {0} Affinity
   PL: {1}% obrażeń Umiejętnościami atrybutu {0}
9. [Status [AtkAndTakeAtkDamageMultiplier] — opis] 가하는 / 받는 피해량 {0}%
   źródło: BuffAbilities.json :: dataList[id=AtkAndTakeAtkDamageMultiplier].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}% to damage dealt & taken
   PL: Zadawane / otrzymywane obrażenia {0}%
10. [Status [AtkAndTakeAtkDamageMultiplier] — wariant opisu 1] {0} 속성 스킬로 가하는 / 받는 피해량 {1}%
   źródło: BuffAbilities.json :: dataList[id=AtkAndTakeAtkDamageMultiplier].variation
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1}% to damage dealt & taken with {0} Affinity
   PL: {1}% obrażeń zadawanych / otrzymywanych Umiejętnościami atrybutu {0}
11. [Status [GiveBuffOnSucceedAttack] — opis] 적중 시 {0} {1} 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnSucceedAttack].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Apply {1} {0} On Hit
   PL: Przy trafieniu nadaje {0} {1}
12. [Status [MaxHpMultiplierRail] — opis] 최대 체력 {0}%
   źródło: BuffAbilities.json :: dataList[id=MaxHpMultiplierRail].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Max HP {0}%
   PL: Maks. HP {0}%
13. [Status [SlotWeightAdder] — opis] 슬롯 가중치 {0}
   źródło: BuffAbilities.json :: dataList[id=SlotWeightAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slot Weight {0}
   PL: Waga Slotów {0}
14. [Status [AtkAdder] — opis] 공격 레벨 {0}
   źródło: BuffAbilities.json :: dataList[id=AtkAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level {0}
   PL: Poziom Ataku {0}
15. [Status [DefAdder] — opis] 방어 레벨 {0}
   źródło: BuffAbilities.json :: dataList[id=DefAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level {0}
   PL: Poziom Obrony {0}
16. [Status [AtkAdderIfNotDamagedPrevTurn] — opis] 한 턴 동안 체력 피해를 받지 않았다면 다음 턴에 공격 레벨 {0}\n(보호막 피해는 해당되지 않음)
   źródło: BuffAbilities.json :: dataList[id=AtkAdderIfNotDamagedPrevTurn].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Offense Level {0} if user took no HP damage for a turn\n(Shield damage ≠ HP damage)
   PL: Poziom Ataku {0} w następnej turze, jeśli przez turę nie otrzymał obrażeń HP\n(obrażenia Tarczy się nie liczą)
17. [Status [MaxSpeedAdderAsStack] — opis] 속도 최댓값 {0}
   źródło: BuffAbilities.json :: dataList[id=MaxSpeedAdderAsStack].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Max Speed {0}
   PL: Maksymalna Szybkość {0}
18. [Status [MaxSpeedAdder] — opis] 속도 최댓값 {0}
   źródło: BuffAbilities.json :: dataList[id=MaxSpeedAdder].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
19. [Status [MinSpeedAdder] — opis] 속도 최솟값 {0}
   źródło: BuffAbilities.json :: dataList[id=MinSpeedAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Min Speed {0}
   PL: Minimalna Szybkość {0}
20. [Status [TakeHpHealMultiplier] — opis] 스킬, 코인 효과를 통한 체력 회복량 {0}%
   źródło: BuffAbilities.json :: dataList[id=TakeHpHealMultiplier].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: HP Healed from Skill and Coin Effects {0}%
   PL: Leczenie HP z efektów Umiejętności i Monet {0}%
21. [Status [RecoverSelfHpOnSucceedAttackByDmg] — opis] 가한 피해량의 {0}%만큼 체력 회복
   źródło: BuffAbilities.json :: dataList[id=RecoverSelfHpOnSucceedAttackByDmg].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Heal {0}% of Damage dealt
   PL: Leczy HP o {0}% zadanych obrażeń
22. [Status [RecoverSelfHpOnSucceedAttackByDmgRR2] — opis] 가한 피해량의 {0}%만큼 체력 회복
   źródło: BuffAbilities.json :: dataList[id=RecoverSelfHpOnSucceedAttackByDmgRR2].desc
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Status [RailEnemyBuffF] — opis] 수감자가 E.G.O 스킬을 사용할 때 소모하는 E.G.O 자원 수량 {0}
   źródło: BuffAbilities.json :: dataList[id=RailEnemyBuffF].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} to amount of E.G.O resources consumed by Sinners when using E.G.O Skills
   PL: Ilość zasobów E.G.O zużywanych przez Skazanych przy użyciu Umiejętności E.G.O {0}
24. [Status [MaxHpMultiplier] — opis] 최대 체력 {0}%
   źródło: BuffAbilities.json :: dataList[id=MaxHpMultiplier].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Status [AtkAndDefAdder] — opis] 공격 레벨 {0}, 방어 레벨 {0}
   źródło: BuffAbilities.json :: dataList[id=AtkAndDefAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level {0}, Defense Level {0}
   PL: Poziom Ataku {0}, Poziom Obrony {0}
26. [Status [GiveBuffOnRoundStartToAllAlly] — opis] 턴 시작 시 아군 전체에게 {0} {1}, {0} 횟수 {2} 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnRoundStartToAllAlly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Turn Start: Apply {1} {0} and +{2} {0} Count to all allies
   PL: Na początek tury nadaje wszystkim sojusznikom {1} Mocy {0} i {2} Licznika {0}
27. [Status [GiveBuffOnRoundStartToAllAlly] — wariant opisu 1] 턴 시작 시 아군 전체에게 {0} {1} 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnRoundStartToAllAlly].variation
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Turn Start: Apply {1} {0} to all allies
   PL: Na początek tury nadaje wszystkim sojusznikom {1} Mocy {0}
28. [Status [GiveBuffOnRoundStartToAllAlly] — wariant opisu 2] 턴 시작 시 아군 전체에게 {0} 횟수 {1} 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnRoundStartToAllAlly].variation2
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Turn Start: Apply +{1} {0} Count to all allies
   PL: Na początek tury nadaje wszystkim sojusznikom {1} Licznika {0}
29. [Status [GiveBuffOnRoundStartToAllAllyExtra] — opis] 턴 시작 시 아군 전체에게 {0} {1} 부여, {0} 상태인 아군에게는 {0} 횟수 {2} 추가로 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnRoundStartToAllAllyExtra].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Turn Start: Apply {1} {0} to all allies and apply +{2} more {0} Count to allies with {0}
   PL: Na początek tury nadaje wszystkim sojusznikom {1} Mocy {0}, a sojusznikom z {0} dodatkowo {2} Licznika {0}
30. [Status [GiveBuffOnRoundStartToAllEnemyExtra] — opis] 턴 시작 시 적 전체에게 {0} {1} 부여, {0} 상태인 적에게는 {0} 횟수 {2} 추가로 부여
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnRoundStartToAllEnemyExtra].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Turn Start: Apply {1} {0} to all enemies and apply +{2} more {0} Count to all enemies with {0}
   PL: Na początek tury nadaje wszystkim wrogom {1} Mocy {0}, a wrogom z {0} dodatkowo {2} Licznika {0}
31. [Status [LoseTurnOnRoundEnd] — opis] 턴 종료 시 횟수 {0} 감소
   źródło: BuffAbilities.json :: dataList[id=LoseTurnOnRoundEnd].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Lose {0} Count
   PL: Na koniec tury Licznik maleje o {0}
32. [Status [Vibration] — opis] {1}턴 동안 진동 폭발 스킬로 피격 시 {0}만큼 흐트러짐 손상
   źródło: BuffAbilities.json :: dataList[id=Vibration].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: When hit by attacks that trigger Tremor Burst, raise the Stagger Threshold by {0}. Lasts {1} turn(s)
   PL: Przez {1} tur przy trafieniu atakami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}
33. [Status [DefAdderByStackCeilToInt] — opis] 진동 위력 4 당 방어 레벨 1 감소
   źródło: BuffAbilities.json :: dataList[id=DefAdderByStackCeilToInt].desc
   limit: do 120 znaków
   EN: Lose 1 Defense Level for every 4 Tremor Potency
   PL: Poziom Obrony maleje o 1 za każde 4 Mocy Wstrząsu
34. [Status [Crack] — opis] 흐트러짐 상태가 되었을 때, 자신의 진동 위력과 횟수의 합이 20 이상이면, 흐트러짐 단계 1 증가\n해당 효과로 최대 흐트러짐 단계를 초과할 수 없음
   źródło: BuffAbilities.json :: dataList[id=Crack].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When Staggered, and when the sum of Tremor Potency and Count adds up to 20 or higher, raise Stagger Level by 1\nCannot exceed maximum Stagger Level with this effect
   PL: W stanie Oszołomienia, przy sumie Mocy i Licznika Wstrząsu wynoszącej 20 lub więcej, Poziom Oszołomienia rośnie o 1\nTen efekt nie może przekroczyć maksymalnego Poziomu Oszołomienia
35. [Status [VibrationEcho] — opis] {1} 턴 동안 진동 폭발 시 {0}만큼 나태 피해를 입음.
   źródło: BuffAbilities.json :: dataList[id=VibrationEcho].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: When hit by attacks that trigger Tremor Burst, take {0} Sloth damage
   PL: Przez {1} tur przy trafieniu atakami wywołującymi Wyładowanie Wstrząsu otrzymuje {0} obrażeń Lenistwa
36. [Status [VibrationDistribution] — opis] 턴 종료 시 (아군 전체의 진동 - 분배 횟수의 합 / (인원 수(진동 - 분배가 있는 아군 수))만큼 다음 턴에 공격 레벨 증가를 얻음 (최대 5)
   źródło: BuffAbilities.json :: dataList[id=VibrationDistribution].desc
   limit: do 190 znaków
   EN: Turn End: Gain ((sum of all allies' Tremor - Distribution Count) / (# of allies with Tremor - Distribution)) Offense Level Up next turn (max 5)
   PL: Na koniec tury zyskuje Wzrost Poziomu Ataku w następnej turze równy (suma Liczników Wstrząsu - Rozdzielania sojuszników / liczba sojuszników z Wstrząsem - Rozdzielaniem) (maks. 5)
37. [Status [VibrationChain] — opis] 대상의 진동 위력 10 당 합 위력 1 감소 (최대 3)
   źródło: BuffAbilities.json :: dataList[id=VibrationChain].desc
   limit: do 120 znaków
   EN: Lose 1 Clash Power for every 10 Tremor Potency on target (max 3)
   PL: Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu celu (maks. 3)
38. [Status [VibrationContinue] — opis] 스킬, 코인 효과로 진동 폭발 시 자신의 {0}% 확률로 진동 폭발 1회 추가 발동. (최대 50%)\n- 스킬, 코인 효과로 진동 폭발 시 자신의 {1}% 확률로 진동 폭발 1회 추가 발동. (최대 50%)
   źródło: BuffAbilities.json :: dataList[id=VibrationContinue].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: - When triggering Tremor Burst with Skill or Coin effects, {0}% chance to trigger an additional Tremor Burst. (max 50%)\n- When triggering Tremor Burst with Skill or Coin effects, {1}% chance to trigger an additional Tremor Burst. (max 50%)
   PL: - Przy wywołaniu Wybuchu Wstrząsu efektem Umiejętności lub Monety, {0}% szans na wywołanie dodatkowego Wybuchu Wstrząsu (maks. 50%)\n- Przy wywołaniu Wybuchu Wstrząsu efektem Umiejętności lub Monety, {1}% szans na wywołanie dodatkowego Wybuchu Wstrząsu (maks. 50%)
39. [Status [TimeSuspend] — opis] 효과 발동 시 {3}만큼 나태 피해를 입히고 진동 폭발 {0}회 발동
   źródło: BuffAbilities.json :: dataList[id=TimeSuspend].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {3}, {0}
   EN: Upon activation, deal {3} Sloth damage and trigger {0} Tremor Burst(s)
   PL: Przy aktywacji efektu zadaje {3} obrażeń Lenistwem i wywołuje Wybuch Wstrząsu {0} razy
40. [Status [TimeRentalTwoPersonality] — nazwa] 시간 대여
   źródło: BuffAbilities.json :: dataList[id=TimeRentalTwoPersonality].name
   kontekst: identyfikator statusu w tekstach: `[TimeRentalTwoPersonality]`
   limit: do 40 znaków
   EN: Borrowed Time
   PL: Pożyczony Czas
41. [Status [TimeRentalTwoPersonality] — opis] 턴 종료시 다음 턴에 신속, 합 위력 증가, 취약 {1} 만큼 얻음\n횟수가 1이면, 턴 종료시 효과를 대신하여 다음 턴에 속박 {0} 얻음
   źródło: BuffAbilities.json :: dataList[id=TimeRentalTwoPersonality].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Turn End: gain {1} Haste, Clash Power Up, and Fragile next turn\nAt 1 Count, gain {0} Bind next turn instead
   PL: Na koniec tury zyskuje w następnej turze {1} Pośpiechu, Wzrostu Mocy Starcia i Wrażliwości\nPrzy Liczniku 1 zamiast tego zyskuje {0} Spętań
42. [Status [VibrationChainPersonality] — nazwa] 진동 - 사슬
   źródło: BuffAbilities.json :: dataList[id=VibrationChainPersonality].name
   kontekst: identyfikator statusu w tekstach: `[VibrationChainPersonality]`
   limit: do 40 znaków
   EN: Tremor - Chain
   PL: Wstrząs - Łańcuch
43. [Status [VibrationChainPersonality] — opis] 진동 위력 10 당 합 위력 1 감소 (최대 3)
   źródło: BuffAbilities.json :: dataList[id=VibrationChainPersonality].desc
   limit: do 120 znaków
   EN: Lose 1 Clash Power for every 10 Tremor Potency (max 3)
   PL: Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu (maks. 3)
44. [Status [DefSkillPowerResultAdder] — opis] 수비 스킬 최종 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=DefSkillPowerResultAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Skill Final Power {0}
   PL: Moc Końcowa Umiejętności obrony {0}
45. [Status [TakeAtkDamageMultiplier] — opis] 받는 피해량 {0}%
   źródło: BuffAbilities.json :: dataList[id=TakeAtkDamageMultiplier].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Damage Taken {0}%
   PL: Otrzymywane obrażenia {0}%
46. [Status [ParryingResultAdder] — opis] 합 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=ParryingResultAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clash Power {0}
   PL: Moc Starcia {0}
47. [Status [SkillPowerResultAdder] — opis] 최종 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=SkillPowerResultAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Final Power {0}
   PL: Moc Końcowa {0}
48. [Status [SkillPowerAdder] — opis] 기본 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=SkillPowerAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Base Power {0}
   PL: Moc bazowa {0}
49. [Status [PlusCoinScaleAdder] — opis] 더하기 코인 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=PlusCoinScaleAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Plus Coin Power {0}
   PL: Moc Monet Plus {0}
50. [Status [MinusCoinScaleAdder] — opis] 빼기 코인 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=MinusCoinScaleAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Minus Coin Power {0}
   PL: Moc Monet Minus {0}
51. [Status [DefaultMaxHpMultiplier] — opis] 최대 체력 {0}%
   źródło: BuffAbilities.json :: dataList[id=DefaultMaxHpMultiplier].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Status [ResistAdderForLastBoss] — opis] 3구간 마지막 보스의 {0} 내성 {1}
   źródło: BuffAbilities.json :: dataList[id=ResistAdderForLastBoss].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Final Boss of Section 3 {0} Resistance {1}
   PL: Odporność {0} ostatniego bossa 3. sekcji: {1}
53. [Status [MRR519P] — opis] 아군이 사망할 때마다 적 전체에게 사망한 아군의 최대 체력의 20%만큼 고정 피해를 입힘
   źródło: BuffAbilities.json :: dataList[id=MRR519P].desc
   limit: do 140 znaków
   EN: Whenever an ally dies, inflict fixed damage equal to 20% of the dead ally's max HP against all enemies
   PL: Za każdą śmierć sojusznika wszyscy wrogowie otrzymują stałe obrażenia równe 20% Maks. HP zmarłego sojusznika
54. [Status [HealSelfOnSucceedAttackByDmgRatio] — opis] 공격 적중시 적의 체력이 감소했으면, 가한 피해량의 {0}% 만큼 체력 회복
   źródło: BuffAbilities.json :: dataList[id=HealSelfOnSucceedAttackByDmgRatio].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: On Hit, if the hit reduced the target's HP, heal by {0}% of the damage dealt
   PL: Przy trafieniu, jeśli HP celu zostało zredukowane, leczy HP o {0}% zadanych obrażeń
55. [Status [MRR524P] — opis] 자신의 {0} 10 당 모든 스킬 피해량 +1% (최대 30%)
   źródło: BuffAbilities.json :: dataList[id=MRR524P].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All Skills deal +1% damage for every 10 {0} on self (max 30%)
   PL: Wszystkie Umiejętności zadają +1% obrażeń za każde 10 {0} tej jednostki (maks. 30%)
56. [Status [MRR525] — opis] 턴 종료시 {0} 횟수 {1} 감소
   źródło: BuffAbilities.json :: dataList[id=MRR525].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Turn End: Lose {1} {0} Count
   PL: Na koniec tury Licznik {0} maleje o {1}
57. [Status [CoinScaleAdderByAtkType] — opis] {0} 스킬의 더하기 코인 위력 +{1}, 빼기 코인 위력 -{1}
   źródło: BuffAbilities.json :: dataList[id=CoinScaleAdderByAtkType].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Skills gain Plus Coin Power +{1}, Minus Coin Power -{1}
   PL: Umiejętności atrybutu {0} zyskują Moc Monet Plus +{1} i Moc Monet Minus -{1}
58. [Status [GiveBuffOnReleaseStandBy] — opis] 대기 해제 시 {0} {1} 얻음
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnReleaseStandBy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Gain {1} {0} when Substituting in
   PL: Gdy wchodzi z rezerwy, zyskuje {1} Mocy {0}
59. [Status [MRR532] — opis] 각성 E.G.O 스킬 공격 종료시 보유한 E.G.O 자원 중 1개 이상인 무작위 속성 자원을 1개씩, 총 2개 소모
   źródło: BuffAbilities.json :: dataList[id=MRR532].desc
   limit: do 160 znaków
   EN: After using an Awakening E.G.O, also consume 1 E.G.O Resource from 3 random Sin Affinities with more than 1 E.G.O resource
   PL: Po zakończeniu ataku Umiejętnością Przebudzenia E.G.O zużywa po 1 zasobie E.G.O z 2 losowych atrybutów posiadających co najmniej 1 zasób (łącznie 2)
60. [Status [LacerationStackAndTurnAdder] — opis] 스킬, 코인 효과로 부여하는 {1} 위력, 횟수 {0}
   źródło: BuffAbilities.json :: dataList[id=LacerationStackAndTurnAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: +{0} to {1} Potency and Count inflicted with Skill & Coin effects
   PL: Umiejętności i monety nakładają +{0} Mocy i Licznika {1}
61. [Status [MRR536] — opis] 스킬로 피격 시 마다 다음 턴에 {0} 1, {1} 1 중 무작위 1개를 얻음 (최대 4회)
   źródło: BuffAbilities.json :: dataList[id=MRR536].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: When hit by a Skill, randomly gain 1 of the following next turn: {0}, {1} (max 4 times)
   PL: Za każde otrzymanie trafienia Umiejętnością zyskuje w następnej turze losowo 1 Mocy {0} albo 1 Mocy {1} (maks. 4 razy)
62. [Status [MRR540] — opis] {0}을 소모하는 스킬의 최종 위력 +1, 가하는 피해량 10% 증가
   źródło: BuffAbilities.json :: dataList[id=MRR540].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skills that consume {0} gain the following: Final Power +1, deal +10% damage
   PL: Umiejętności zużywające {0} zyskują Moc Końcową +1 i zadają +10% obrażeń
63. [Status [MRR541] — opis] {1}이 가장 낮은 대상이 메인 타겟이면, 스킬 최종 위력 +{0}
   źródło: BuffAbilities.json :: dataList[id=MRR541].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: When mainly targeting the unit that has the lowest {1}, Skill Final Power +{0}
   PL: Jeśli głównym celem jest jednostka z najniższą wartością {1}, Moc Końcowa Umiejętności +{0}
64. [Status [MRR518P] — opis] 전투 시작 시 현재 편성 순서가 가장 빠른 아군 3명이 호흡 위력 10 얻음
   źródło: BuffAbilities.json :: dataList[id=MRR518P].desc
   limit: do 120 znaków
   EN: Combat Start: 3 currently earliest Deployed allies gain 10 Poise Potency
   PL: Na początku walki 3 sojuszników rozmieszczonych najwcześniej zyskuje 10 Mocy Oddechu
65. [Status [MRR520P] — opis] 사망할 때, 적 전체에게 사망자 최대 체력의 {0}% 만큼 고정 피해를 입힘 (집중 전투인 경우 부위에 적용 됨)
   źródło: BuffAbilities.json :: dataList[id=MRR520P].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: On death, inflict fixed damage equal to {0}% of the dead unit's max HP against all enemies (for Focused Encounters, all Parts)
   PL: Po śmierci zadaje wszystkim wrogom stałe obrażenia równe {0}% Maks. HP zmarłego (w walkach skupionych dotyczy części)
66. [Status [MRR517] — opis] 스킬로 피격 시마다 다음 턴에 공격 레벨 증가 2 얻음. (최대 6)
   źródło: BuffAbilities.json :: dataList[id=MRR517].desc
   limit: do 120 znaków
   EN: When hit by a Skill, gain 2 Offense Level Up next turn (max 6)
   PL: Za każde otrzymanie trafienia Umiejętnością zyskuje 2 Wzrosty Poziomu Ataku w następnej turze (maks. 6)
67. [Status [MRR5051] — opis] {0} 횟수를 8 이상 소모한 스킬 적중 시 이번 전투동안 대상의 {1} 내성 +0.1\n- 적 1명 당 1개의 스킬로 1회만 적용 가능\n- 이 효과로 적 1명의 내성은 최대 0.3 까지 증가시킬 수 있음
   źródło: BuffAbilities.json :: dataList[id=MRR5051].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: On Hit with Skills that consumed 8+ {0} Count: +0.1 to {1} Resistance on the target for this Encounter\n- Once per Skill per Enemy\n- Max Resistance adjustment with this effect: 0.3
   PL: Przy trafieniu Umiejętnością zużywającą 8 lub więcej Licznika {0}: odporność {1} celu +0.1 na czas tej walki\n- Działa raz na Umiejętność na wroga\n- Ten efekt może zwiększyć odporność jednego wroga maksymalnie o 0.3
68. [Status [MRR5052] — opis] {0} 횟수를 획득하거나 소모하는 스킬의 피해량 +(10 + 소모한 값 x 2)% (최대 50%)
   źródło: BuffAbilities.json :: dataList[id=MRR5052].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skills that gain or consume {0} Count deal +(10 + (Charge Count consumed x 2))% damage (max 50%)
   PL: Umiejętności zyskujące lub zużywające {0} Licznika zadają +(10 + zużyta wartość x 2)% obrażeń (maks. 50%)
69. [Status [MRR506] — opis] 턴 종료 시 각 키워드의 횟수가 2 이상이면, 모든 부위에 {0} 위력만큼 {1} 피해를 주고, {0} 횟수 1 감소, {2}을 1회 발동시키고, {3} 횟수 1 감소
   źródło: BuffAbilities.json :: dataList[id=MRR506].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Turn End: For each Keyword, against all enemy Parts with 2+ Count, inflict {1} damage equal to {0} Potency on each Part; then, reduce their {0} Count by 1, trigger {2} once, and reduce their {3} Count by 1
   PL: Na koniec tury: dla każdego słowa kluczowego z Licznikiem 2 lub więcej zadaje wszystkim częściom obrażenia {1} równe Mocy {0}, zmniejsza Licznik {0} o 1, wywołuje {2} raz i zmniejsza Licznik {3} o 1
70. [Status [MRR507] — opis] {0} 위력이나 횟수를 부여하는 스킬의 최종 위력 +2
   źródło: BuffAbilities.json :: dataList[id=MRR507].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skills that inflict {0} Potency or Count: Final Power +2
   PL: Umiejętności nadające {0} Mocy lub Licznika zyskują Moc Końcową +2
71. [Status [MRR508] — opis] 정신력이 없거나 0 미만인 적에게 입히는 피해량 + (대상의 {0} 위력)% (최대 45%)
   źródło: BuffAbilities.json :: dataList[id=MRR508].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +({0} Potency on the target)% damage against targets at less than 0 SP or targets that are non-SP units (max 45%)
   PL: Zadaje +(Moc {0} celu)% obrażeń celom bez Poczytalności lub z Poczytalnością poniżej 0 (maks. 45%)
72. [Status [MRR509P] — opis] 파괴되었거나, 흐트러짐 상태인 부위에 가하는 피해량 {0}%
   źródło: BuffAbilities.json :: dataList[id=MRR509P].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}% damage against Destroyed or Staggered Parts
   PL: Zadaje +{0}% obrażeń zniszczonym lub oszołomionym częściom
73. [Status [GiveBuffOnFirstRoundStartPerWave] — opis] 웨이브 첫 턴 시작시 {0} 위력 {1} 얻고 {0} 횟수 {2} 증가
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnFirstRoundStartPerWave].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: First Turn Start of a wave: Gain {1} {0} Potency and +{2} {0} Count
   PL: Na pierwszy początek tury fali zyskuje {1} Mocy {0} i {2} Licznika {0}
74. [Status [GiveBuffOnBattleStartAR] — opis] {0} 공명을 발동하였다면 전투 시작 시, 모든 아군이 {1} 위력 {2} 얻고 {1} 횟수 {3} 증가
   źródło: BuffAbilities.json :: dataList[id=GiveBuffOnBattleStartAR].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Combat Start: If {0} Reson. was activated, all allies gain {2} {1} Potency and +{3} {1} Count
   PL: Na początku walki, przy aktywnym rezonansie {0}, wszyscy sojusznicy zyskują {2} Mocy {1} i {3} Licznika {1}
75. [Status [MRR511PMaxSpeedAdder] — opis] 편성 순서 1번인 아군의 속도 최댓값 +1
   źródło: BuffAbilities.json :: dataList[id=MRR511PMaxSpeedAdder].desc
   limit: do 120 znaków
   EN: #1 Deployed ally: Max Speed +1
   PL: Sojusznik rozmieszczony jako #1: Maksymalna Szybkość +1
76. [Status [MRR511PMinSpeedAdder] — opis] 편성 순서 1번인 아군의 속도 최솟값 +1
   źródło: BuffAbilities.json :: dataList[id=MRR511PMinSpeedAdder].desc
   limit: do 120 znaków
   EN: #1 Deployed ally: Min Speed +1
   PL: Sojusznik rozmieszczony jako #1: Minimalna Szybkość +1
77. [Status [MRR511PMinSpeedChangeSkill] — opis] 편성 순서 1번인 아군의 1스킬 1개 감소. 3스킬 1개 증가
   źródło: BuffAbilities.json :: dataList[id=MRR511PMinSpeedChangeSkill].desc
   limit: do 120 znaków
   EN: #1 Deployed Ally: Lose a Skill 1, but gain a Skill 3
   PL: Sojusznik rozmieszczony jako #1: traci 1 Umiejętność 1, zyskuje 1 Umiejętność 3
78. [Status [MRR512] — opis] 7번째 편성 순서부터 대기 해제된 턴 시작시 정신력 {0} 회복, 이번 전투동안 {1} {2}를 얻고, 자신의 스킬 1, 2, 3 속성의 E.G.O 자원을 {3}개씩 얻음
   źródło: BuffAbilities.json :: dataList[id=MRR512].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Starting from #7 Deployed Sinner, at the start of the same turn it Substitutes in, heal {0} SP, gain {2} {1} for the Encounter, and gain {3} E.G.O resource for each one of their Skills 1, 2, and 3
   PL: Od rozmieszczenia #7, przy wejściu z rezerwy na początku tej samej tury: leczy {0} Poczytalności, zyskuje {2} Mocy {1} na czas tej walki i {3} zasobów E.G.O atrybutu każdej z Umiejętności 1, 2 i 3
79. [Status [AddSinStockOnKillTargetByUsedSkillAttribute] — opis] 공격, 반격 스킬 종료 시 적이 사망한 경우, 사용한 스킬 속성의 E.G.O 자원 +{0} (스킬당 1회, E.G.O 스킬 포함)
   źródło: BuffAbilities.json :: dataList[id=AddSinStockOnKillTargetByUsedSkillAttribute].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: After using an Attack or a Counter Skill, if the enemy is defeated, gain {0} E.G.O resource of the Skill Affinity that was used (once per Skill, including E.G.O Skills)
   PL: Po zakończeniu Umiejętności ataku lub kontrataku, jeśli wróg ginie, zyskuje {0} zasobu E.G.O atrybutu użytej Umiejętności (raz na Umiejętność, w tym Umiejętności E.G.O)
80. [Status [MRR514] — opis] 새로운 적이 증원되면, 전투 시작 시 해당 적에게 출혈 5, 출혈 횟수 3 부여. 아군에 <혈귀>가 있다면, 위 조건 만족 시 모든 적의 출혈을 1회 발동시키고, 모든 적의 출혈 횟수 1 감소
   źródło: BuffAbilities.json :: dataList[id=MRR514].desc
   limit: do 310 znaków
   EN: When Backup enemies enter the battle, inflict 5 Bleed and +3 Bleed against them at Combat Start. If there is a <Bloodfiend> among allies: when above conditions are met: activate Bleed on all enemies once and reduce their Bleed Count by 1
   PL: Gdy wzmocnienia wprowadzą nowych wrogów, na początku ich walki nakłada na nich 5 Krwawienia i 3 Licznika Krwawienia. Jeśli wśród sojuszników jest <Krwiożerca>, po spełnieniu powyższego warunku wywołuje Krwawienie wszystkich wrogów i maleje Licznik Krwawienia wszystkich wrogów o 1
81. [Status [EnemyLevelTextOnly] — opis] 적 레벨 {0}
   źródło: BuffAbilities.json :: dataList[id=EnemyLevelTextOnly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy Level {0}
   PL: Poziom wroga {0}
82. [Status [MRR501] — opis] 적에게 스킬, 코인 효과로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 {0}
   źródło: BuffAbilities.json :: dataList[id=MRR501].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0} to Burn, Bleed, Tremor, Rupture, and Sinking Potency inflicted against enemies with Skills & Coin effects
   PL: Umiejętności i monety nakładają na wrogów +{0} Mocy Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
83. [Status [TakeBuffTurnAdder] — opis] 아군이 스킬, 코인 효과로 얻는 {0} 횟수 {1}
   źródło: BuffAbilities.json :: dataList[id=TakeBuffTurnAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} to {0} Count gained by allies with Skills & Coin effects
   PL: Sojusznicy zyskują {1} Licznika {0} z efektów Umiejętności i Monet
84. [Status [MRR503] — opis] 턴 종료 시 정신력이 가장 낮은 아군 {0}명 정신력 {1} 회복 (패닉, 침식 상태인 아군 제외)
   źródło: BuffAbilities.json :: dataList[id=MRR503].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} allies that have the lowest SP heal {1} SP at Turn End (excluding allies that are Panicked or Corroded)
   PL: Na koniec tury {0} sojuszników z najniższą Poczytalnością odzyskuje {1} Poczytalności (z wyłączeniem sojuszników w Panice lub Korozji)
85. [Status [CriticalDamageBoostWithBuffUse] — opis] 크리티컬 발동 시 보유한 {0} 위력이 {1}을 초과했으면, 초과한 {0} 위력을 최대 {1} 소모하여 크리티컬 피해량 + (소모한 값 x {2})% (최대 {3}%)
   źródło: BuffAbilities.json :: dataList[id=CriticalDamageBoostWithBuffUse].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: On Crit, at more than {1} {0} Potency, consume up to {1} of the excess {0} Potency to deal +(Poise Potency consumed x {2})% damage on Critical Hit (max {3}%)
   PL: Przy trafieniu krytycznym, jeśli posiadana Moc {0} przekracza {1}, zużywa nadwyżkę Mocy {0} (maks. {1}), zadając przy trafieniu krytycznym +(zużyta wartość x {2})% obrażeń (maks. {3}%)
86. [Status [GainSinStockOnDieByDefaultSkill] — opis] 사망 시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음
   źródło: BuffAbilities.json :: dataList[id=GainSinStockOnDieByDefaultSkill].desc
   limit: do 130 znaków
   EN: When defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has
   PL: Po śmierci zyskuje zasoby E.G.O odpowiadające atrybutom i rangom posiadanych Umiejętności ataku
87. [Status [MRR547] — opis] 턴 시작 시 적의 스킬 최종 위력 +1 ~ 3
   źródło: BuffAbilities.json :: dataList[id=MRR547].desc
   limit: do 120 znaków
   EN: Turn Start: All enemy Skills gain Final Power +1~3
   PL: Na początek tury Moc Końcowa Umiejętności wrogów +1~3
88. [Status [MRR544] — opis] 턴 시작 시 모든 아군의 스킬 최종 위력 +1 ~ 3
   źródło: BuffAbilities.json :: dataList[id=MRR544].desc
   limit: do 120 znaków
   EN: Turn Start: All ally Skills gain Final Power +1~3
   PL: Na początek tury wszystkie Umiejętności sojuszników zyskują Moc Końcową +1~3
89. [Status [MRR551] — opis] 턴 시작 시 체력이 최대라면 {0} 위력 {1} 얻음, 횟수 {2} 증가 (적 1명당 부위별 전투당 1회 발동)
   źródło: BuffAbilities.json :: dataList[id=MRR551].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Turn Start: At max HP, gain {1} {0} Potency and +{2} Count (once per enemy per Part per Encounter)
   PL: Na początek tury, przy pełnym HP, zyskuje {1} Mocy {0} i {2} Licznika {0} (raz na walkę na wroga na część)
90. [Status [MRR552] — opis] 사망 시, 다음 턴에 현재 체력이 가장 낮은 아군 1명이 {0} {1} 얻음
   źródło: BuffAbilities.json :: dataList[id=MRR552].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: On death, 1 ally with the lowest current HP gains {1} {0} next turn
   PL: Po śmierci 1 sojusznik z najniższym obecnym HP zyskuje {1} Mocy {0} w następnej turze
91. [Status [MRR553] — opis] E.G.O 스킬의 피해량 {0}%
   źródło: BuffAbilities.json :: dataList[id=MRR553].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Skills deal +{0}% damage
   PL: Umiejętności E.G.O zadają +{0}% obrażeń
92. [Status [MRR521] — opis] 첫 번째 흐트러짐 선 제거
   źródło: BuffAbilities.json :: dataList[id=MRR521].desc
   limit: do 120 znaków
   EN: Remove the first Stagger threshold
   PL: Usuwa pierwszy Próg Oszołomienia
93. [Status [MRR557] — opis] 크리티컬 피해량 + (10 + 보유한 {0} 위력과 횟수의 합)% (최대 50%)
   źródło: BuffAbilities.json :: dataList[id=MRR557].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +(10 + {0} Potency + {0} Count)% damage on Critical Hit (max 50%)
   PL: Zadaje +(10 + suma Mocy i Licznika {0})% obrażeń przy trafieniu krytycznym (maks. 50%)
94. [Status [LacerationStackAndTurnAdderIfNotZero] — opis] 스킬, 코인 효과로 부여하는 {1} 위력, 횟수 {0}
   źródło: BuffAbilities.json :: dataList[id=LacerationStackAndTurnAdderIfNotZero].desc
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Status [AttackDmgMultiplierSpecificType] — opis] {0} 속성 스킬의 피해량 +30%
   źródło: BuffAbilities.json :: dataList[id=AttackDmgMultiplierSpecificType].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Skills deal +30% damage
   PL: Umiejętności atrybutu {0} zadają +30% obrażeń
96. [Status [MRR565MaxSpeedAdder] — opis] 속도 최댓값 {0}
   źródło: BuffAbilities.json :: dataList[id=MRR565MaxSpeedAdder].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Status [MRR565MinSpeedAdder] — opis] 속도 최솟값 {0}
   źródło: BuffAbilities.json :: dataList[id=MRR565MinSpeedAdder].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Status [DefaultLevelAdder] — opis] 기본 공격 레벨 {0}, 기본 방어 레벨 {0}, 기본 유닛 방어 레벨 {0}
   źródło: BuffAbilities.json :: dataList[id=DefaultLevelAdder].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Base Offense Level {0}, Base Defense Level {0}, Base Unit Defense Level {0}
   PL: Bazowy Poziom Ataku {0}, bazowy Poziom Obrony {0}, bazowy Poziom Obrony jednostki {0}
99. [Status [VibrationIgnition] — opis] {1} 턴 동안 진동 폭발 시 ({0}+화상 위력)/2 만큼 분노 피해를 입고 화상 횟수 1 감소
   źródło: BuffAbilities.json :: dataList[id=VibrationIgnition].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: For {1} turns, upon Tremor Burst, take ({0} + Burn Potency) / 2 Wrath Damage; then, reduce Tremor Count by 1
   PL: Przez {1} tur, przy Wybuchu Wstrząsu, otrzymuje ({0} + Moc Podpalenia) / 2 obrażeń Gniewu, a Licznik Wstrząsu maleje o 1
100. [Status [Heishou10212] — opis] 흑수 - 묘 필두 파우스트 : 받는 스킬 피해 -5%
   źródło: BuffAbilities.json :: dataList[id=Heishou10212].desc
   limit: do 120 znaków
   EN: Heishou Pack - Mao Branch Adept Faust: Take -5% damage from Skills
   PL: Wataha Heishou - Gałąź Mao, Adept Faust: otrzymuje -5% obrażeń od Umiejętności
101. [Status [Heishou10411] — opis] 흑수 - 묘 료슈 : 자신의 속도가 대상보다 빠르면, 피해량 +5%
   źródło: BuffAbilities.json :: dataList[id=Heishou10411].desc
   limit: do 130 znaków
   EN: Heishou Pack - Mao Branch Ryōshū: If this unit's Speed is faster than the target's, deal +5% damage
   PL: Wataha Heishou - Gałąź Mao, Ryōshū: jeśli jego Szybkość jest większa niż Szybkość celu, zadaje +5% obrażeń
102. [Status [Heishou11112] — opis] 흑수 - 묘 오티스 : 일방 공격 적중 시, 파열 횟수 1 증가 (턴 당 1회)
   źródło: BuffAbilities.json :: dataList[id=Heishou11112].desc
   limit: do 140 znaków
   EN: Heishou Pack - Mao Branch Outis: Inflict +1 Rupture Count On Hit with an Unopposed Attack (once per turn)
   PL: Wataha Heishou - Gałąź Mao, Outis: przy trafieniu atakiem jednostronnym zwiększa Licznik Rozdarcia o 1 (raz na turę)
103. [Status [Heishou10912] — opis] 흑수 - 사 로쟈 : 크리티컬 적중 시, 파열 1 부여 (턴 당 3회)
   źródło: BuffAbilities.json :: dataList[id=Heishou10912].desc
   limit: do 120 znaków
   EN: Heishou Pack - Si Branch Rodion: Inflict 1 Rupture On Critical Hit (3 times per turn)
   PL: Wataha Heishou - Gałąź Si, Rodion: przy trafieniu krytycznym nadaje 1 Rozdarcia (3 razy na turę)
104. [Status [Heishou11212] — opis] 흑수 - 사 그레고르 : 파열 피해를 가하면, 호흡 횟수 1 얻음 (턴 당 1회)
   źródło: BuffAbilities.json :: dataList[id=Heishou11212].desc
   limit: do 130 znaków
   EN: Heishou Pack - Si Branch Gregor: When dealing Rupture damage, gain +1 Poise Count (once per turn)
   PL: Wataha Heishou - Gałąź Si, Gregor: zadając obrażenia Rozdarcia, zyskuje 1 Licznika Oddechu (raz na turę)
105. [Status [Heishou11014] — opis] 흑수 - 유 싱클레어 : 스킬로 파열 부여 시, 화상 1 부여 (턴 당 3회)
   źródło: BuffAbilities.json :: dataList[id=Heishou11014].desc
   limit: do 140 znaków
   EN: Heishou Pack - You Branch Sinclair: When inflicting Rupture with Skills, inflict 1 Burn (3 times per turn)
   PL: Wataha Heishou - Gałąź You, Sinclair: nakładając Rozdarcie Umiejętnością, nadaje 1 Podpalenia (3 razy na turę)
106. [Status [Heishou10114] — opis] 흑수 - 오 필두 이상 : 기본 스킬의 마지막 코인 적중 시, 진동 폭발 1회 (턴 당 1회)
   źródło: BuffAbilities.json :: dataList[id=Heishou10114].desc
   limit: do 160 znaków
   EN: Heishou Pack - Wu Branch Adept Yi Sang: On Hit with a Base Skill's Final Coin, trigger Tremor Burst once (once per turn)
   PL: Wataha Heishou - Gałąź Wu, Adept Yi Sang: przy trafieniu ostatnią monetą Umiejętności bazowej wywołuje Wybuch Wstrząsu (raz na turę)
107. [Status [GiveMpDmgAsValueOnRESelf] — opis] 턴 종료 시, 아군 매 턴 정신력 {0} 감소
   źródło: BuffAbilities.json :: dataList[id=GiveMpDmgAsValueOnRESelf].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Every Turn End: Allies lose {0} SP
   PL: Na koniec tury sojusznicy tracą {0} Poczytalności
108. [Status [GiveHpDmgAsValueAndIncreaseOnRESelf] — opis] 턴 종료 시 아군이 체력 고정 {0} 피해를 받음. 턴 마다 피해량 {1} 증가(최대 {2})
   źródło: BuffAbilities.json :: dataList[id=GiveHpDmgAsValueAndIncreaseOnRESelf].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Turn End: Allies take {0} fixed HP damage. Fixed damage increases by {1} every turn. (max {2})
   PL: Na koniec tury sojusznicy otrzymują {0} stałych obrażeń HP. Obrażenia rosną o {1} co turę (maks. {2})
109. [Status [CantRecoverMpOverValue] — opis] 정신력 {0}을 초과하여 회복 불가
   źródło: BuffAbilities.json :: dataList[id=CantRecoverMpOverValue].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cannot heal SP past {0}
   PL: Poczytalność nie może przekroczyć {0}
110. [Status [MD6LimitTest105] — opis] E.G.O 소모 자원 증가 {0}배로 변경됨
   źródło: BuffAbilities.json :: dataList[id=MD6LimitTest105].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Multiply E.G.O Resource consumption by {0}
   PL: Zmienia zużycie zasobów E.G.O x{0}
111. [Status [RemoveFirstBreakSection] — opis] 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제
   źródło: BuffAbilities.json :: dataList[id=RemoveFirstBreakSection].desc
   limit: do 120 znaków
   EN: Remove the first Stagger Threshold
   PL: Usuwa pierwszy Próg Oszołomienia
112. [Status [MinSpeedAdderIncludeFirstTurn] — opis] 속도 최솟값 {0}
   źródło: BuffAbilities.json :: dataList[id=MinSpeedAdderIncludeFirstTurn].desc
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Status [MaxSpeedAdderIncludeFirstTurn] — opis] 속도 최댓값 {0}
   źródło: BuffAbilities.json :: dataList[id=MaxSpeedAdderIncludeFirstTurn].desc
   (powtórzenie elementu 17 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Status [DefaultMaxHpMultiplierBossRoomOnly] — opis] 보스 전투 최대 체력 {0}%
   źródło: BuffAbilities.json :: dataList[id=DefaultMaxHpMultiplierBossRoomOnly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Boss Max HP {0}%
   PL: Maks. HP bossa {0}%
115. [Status [MaxHpReducerMirrorDungeonPersonality] — opis] 최대 체력 {0}%
   źródło: BuffAbilities.json :: dataList[id=MaxHpReducerMirrorDungeonPersonality].desc
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Status [VibrationBleeding] — opis] {1} 턴 동안 진동 폭발 시 ({0}+출혈 위력)/2 만큼 색욕 속성 피해를 입고 출혈 횟수 1 감소
   źródło: BuffAbilities.json :: dataList[id=VibrationBleeding].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: For {1} turns, upon Tremor Burst, take ({0} + Bleed Potency) / 2 Lust Damage; then, reduce Bleed Count by 1
   PL: Przez {1} tur, przy Wybuchu Wstrząsu, otrzymuje ({0} + Moc Krwawienia) / 2 obrażeń atrybutu Żądzy, a Licznik Krwawienia maleje o 1
117. [Status [Heishou10714] — opis] 흑수 - 유 필두 히스클리프 : 기본 스킬로 적에게 가한 탐식 피해의 5%만큼 분노 피해
   źródło: BuffAbilities.json :: dataList[id=Heishou10714].desc
   limit: do 140 znaków
   EN: Heishou Pack - You Branch Adept Heathcliff: Deal 5% of Gluttony damage dealt by Base Skills as Wrath damage
   PL: Wataha Heishou - Gałąź You, Adept Heathcliff: zadaje obrażenia Gniewu równe 5% obrażeń Obżarstwa zadanych Umiejętnościami bazowymi
118. [Status [Heishou10313] — opis] 흑수 - 미 돈키호테 : 스킬로 파열 부여 시, 침잠 1 부여 (턴 당 3회)
   źródło: BuffAbilities.json :: dataList[id=Heishou10313].desc
   limit: do 150 znaków
   EN: Heishou Pack - Wei Branch Don Quixote: When inflicting Rupture with Skills, inflict 1 Sinking (3 times per turn)
   PL: Wataha Heishou - Gałąź Wei, Don Quixote: nakładając Rozdarcie Umiejętnością, nadaje 1 Zatonięcia (3 razy na turę)
119. [Status [MD7LimitGiveBuffAllyDie] — opis] 아군 사망 시 다음 턴에 {0} {1}, {0} 횟수 {2} 획득 (턴 당 {3}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDie].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: On Ally Death: Gain {1} {0} and +{2} {0} Count next turn ({3} times per turn)
   PL: Po śmierci sojusznika zyskuje w następnej turze {1} Mocy {0} i {2} Licznika {0} ({3} razy na turę)
120. [Status [MD7LimitGiveBuffAllyDie] — wariant opisu 1] 아군 사망 시 다음 턴에 {0} {1} 획득 (턴 당 {2}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDie].variation
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: On Ally Death: Gain {1} {0} next turn ({2} times per turn)
   PL: Po śmierci sojusznika zyskuje w następnej turze {1} Mocy {0} ({2} razy na turę)
121. [Status [MD7LimitGiveBuffAllyDie] — wariant opisu 2] 아군 사망 시 다음 턴에 {0} 횟수 {1} 획득 (턴 당 {2}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDie].variation2
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: On Ally Death: Gain +{1} {0} Count next turn ({2} times per turn)
   PL: Po śmierci sojusznika zyskuje w następnej turze {1} Licznika {0} ({2} razy na turę)
122. [Status [MD7LimitGiveBuffAllyDieAlt] — opis] 아군 사망 시 다음 턴에 {0} {1}, {0} 횟수 {2} 획득 (턴 당 {3}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDieAlt].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Status [MD7LimitGiveBuffAllyDieAlt] — wariant opisu 1] 아군 사망 시 다음 턴에 {0} {1} 획득 (턴 당 {2}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDieAlt].variation
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Status [MD7LimitGiveBuffAllyDieAlt] — wariant opisu 2] 아군 사망 시 다음 턴에 {0} 횟수 {1} 획득 (턴 당 {2}회)
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveBuffAllyDieAlt].variation2
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Status [RecoverSelfMpOnRoundStart] — opis] 턴 시작 시 정신력 {0} 회복
   źródło: BuffAbilities.json :: dataList[id=RecoverSelfMpOnRoundStart].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn Start: Heal {0} SP
   PL: Na początek tury odzyskuje {0} Poczytalności
126. [Status [MD7LimitGiveShield] — opis] 보호막 {0} 획득
   źródło: BuffAbilities.json :: dataList[id=MD7LimitGiveShield].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain {0} Shield
   PL: Zyskuje {0} Tarczy
127. [Status [MD7LimitSinBuffGiveBooster] — opis] 스킬, 코인의 화상, 출혈, 진동, 파열, 침잠 부여량 {0} 배로 증가
   źródło: BuffAbilities.json :: dataList[id=MD7LimitSinBuffGiveBooster].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skills and Coins inflict x{0} more Burn, Bleed, Tremor, Rupture, and Sinking
   PL: Umiejętności i monety nakładają x{0} więcej Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
128. [Status [GiveRandomNegativeSinbuffOnRoundStart] — opis] 턴 시작 시 화상, 출혈, 진동, 파열, 침잠 중 무작위로 {0} 획득
   źródło: BuffAbilities.json :: dataList[id=GiveRandomNegativeSinbuffOnRoundStart].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn Start: Gain {0} Potency randomly among Burn, Bleed, Tremor, Rupture, and Sinking
   PL: Na początek tury zyskuje losowo {0} z: Podpalenia, Krwawienia, Wstrząsu, Rozdarcia, Zatonięcia
129. [Status [MD7LimitMpAdjuster] — opis] 턴 시작 시 정신력 {0} 회복\n- 모든 스킬이 빼기 코인이면 대신 정신력 {1} 감소
   źródło: BuffAbilities.json :: dataList[id=MD7LimitMpAdjuster].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: Turn Start: Heal {0} SP\n- If all Skills are Minus Coin Skills, lose {1} SP instead
   PL: Na początek tury odzyskuje {0} Poczytalności\n- Przy samych monetach Minus zamiast tego traci {1} Poczytalności
130. [Status [SpiderHouse10115] — opis] 거미집 검지 아비 이상 : 기본 공격 스킬 사용시 마지막 코인이 파괴 불가 코인으로 변경됨. 기본 공격 스킬의 파괴 불가 코인의 피해량 +10%
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10115].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders: The Index Nursefather Yi Sang\n- On Base Attack Skill Use, convert the final Coin into Unbreakable Coin. Unbreakable Coins of Base Attack Skills deal +10% damage
   PL: Dom Pajęczyn: Ojciec Wskazującego Yi Sang\n- Przy użyciu Umiejętności ataku bazowej zamienia ostatnią monetę w Niezniszczalną Monetę. Niezniszczalne Monety Umiejętności ataku bazowej zadają +10% obrażeń
131. [Status [SpiderHouse10314] — opis] 검지 대행자 - 개화 E.G.O:: 대행 돈키호테 : 기본 공격 스킬 사용시 호흡 2 얻음. 기본 공격 스킬 크리티컬 적중시 침잠 1 부여
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10314].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Index Proxy - Effloresced E.G.O::Procuration Don Quixote\n- On Base Attack Skill Use, gain 2 Poise. On Crit using Base Attack Skills, inflict 1 Sinking
   PL: Pełnomocnik Wskazującego - Rozkwitłe E.G.O::Pełnomocnictwo Don Quixote\n- Przy użyciu Umiejętności ataku bazowej zyskuje 2 Oddechu; przy trafieniu krytycznym nadaje 1 Zatonięcia
132. [Status [SpiderHouse10814] — opis] 거미집 중지 제자 이스마엘 : 방어 레벨 +2, 기본 스킬로 부여하는 화상 위력 +1
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10814].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders: The Middle Apprentice Ishmael\n- Defense Level +2 and inflict 1 additional Burn Potency using Base Skills
   PL: Dom Pajęczyn: Uczeń Środkowego Ishmael\n- Poziom Obrony +2; Umiejętności bazowe nadają +1 Mocy Podpalenia
133. [Status [SpiderHouse10614] — opis] 거미집 약지 아비 홍루 : 신체가 울리는 선율 얻음
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10614].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders: The Ring Nursefather Hong Lu\n- Gain Somatic Frisson-inspiring Melody
   PL: Dom Pajęczyn: Ojciec Serdecznego Hong Lu\n- Zyskuje Melodię Drgającego Ciała
134. [Status [SpiderHouse10215] — opis] 거미집 약지 제자 파우스트 : 매 턴 시작시 최대 체력의 10%만큼 보호막 얻음
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10215].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders: The Ring Apprentice Faust\n- Turn Start: Gain Shield equal to 10% HP
   PL: Dom Pajęczyn: Uczeń Serdecznego Faust\n- Na początek tury zyskuje Tarczę równą 10% HP
135. [Status [SpiderHouse11015] — opis] 거미집 소지 제자 싱클레어 : 매 턴 시작시 호흡 횟수 1, 크리티컬 피해량 증가 1 얻음
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse11015].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The House of Spiders: The Pinky Apprentice Sinclair\n- Turn Start: Gain +1 Poise Count and 1 Crit DMG Up
   PL: Dom Pajęczyn: Uczeń Małego Palca Sinclair\n- Na początek tury zyskuje 1 Licznika Oddechu i 1 Wzrostu Obrażeń Krytycznych
136. [Status [SojiRyoshuEntangle] — opis] - 최댓값 : 4\n- 사망한 아군 거미집 아비 인격 1명당 수치 1 증가\n- 사망한 아군 거미집 인격에 따라 고유 효과 얻음\n- 수치당 받는 피해 -7.5%
   źródło: BuffAbilities.json :: dataList[id=SojiRyoshuEntangle].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Gain 1 Stack for every defeated The House of Spiders Nursefather Identity\n- Gain a different unique effect based on which of The House of Spiders ally was defeated\n- Take -7.5% damage for every Stack
   PL: - Maks.: 4\n- Zyskuje 1 wartości za każdą pokonaną osobowość sojuszniczego Ojca Domu Pajęczyn\n- Zyskuje unikalny efekt zależnie od tego, która sojusznicza osobowość Domu Pajęczyn poległa\n- Otrzymuje -7,5% obrażeń za każdą wartość
137. [Status [Railway6PowderBuff] — opis] - {0} 내성 +{2}, {1} 내성 +{2}
   źródło: BuffAbilities.json :: dataList[id=Railway6PowderBuff].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {2}, {1}
   EN: - +{2} {0} Resist.; +{2} {1} Resist.
   PL: - Odporność {0} +{2}; odporność {1} +{2}
138. [Status [Railway6PowderBuff] — wariant opisu 1] - {0} 내성 +{1}
   źródło: BuffAbilities.json :: dataList[id=Railway6PowderBuff].variation
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: - +{1} {0} Resist.
   PL: - Odporność {0} +{1}
139. [Status [Railway6PowderBuff] — wariant opisu 2] - 적용 효과 없음
   źródło: BuffAbilities.json :: dataList[id=Railway6PowderBuff].variation2
   limit: do 120 znaków
   EN: - No effect
   PL: - Brak efektów
140. [Status [SpiderHouse11115] — opis] 거미집 중지 아비 오티스 : 받는 피해 -20%. 피격 시 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse11115].desc
   limit: do 160 znaków
   EN: The House of Spiders: The Middle Nursefather Outis: Take -20% damage; when hit, gain 1 Offense Level Up (2 times per turn)
   PL: Dom Pajęczyn: Ojciec Środkowego Outis: otrzymuje -20% obrażeń; przy trafieniu zyskuje 1 Wzrost Poziomu Ataku (2 razy na turę)
141. [Status [SpiderHouse10916] — opis] 거미집 엄지 아비 로쟈 : 수비 스킬 코인 위력 +1, 보호막을 보유한 대상에게 가하는 기본 공격 스킬 피해량 +10%
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10916].desc
   limit: do 200 znaków
   EN: The House of Spiders: The Thumb Nursefather Rodion: Defense Skill Coin Power +1, Base Attack Skills deal +10% damage against targets that have Shield
   PL: Dom Pajęczyn: Ojciec Kciuka Rodion: Moc Monet Umiejętności obrony +1; Umiejętności ataku bazowe zadają +10% obrażeń celom z Tarczą
142. [Status [SpiderHouse10716] — opis] 거미집 엄지 제자 히스클리프 : 기본 스킬로 합 승리시 진동 2를 부여하고 진동 폭발. 대상의 진동 횟수 1 감소 (턴당 2회)
   źródło: BuffAbilities.json :: dataList[id=SpiderHouse10716].desc
   limit: do 250 znaków
   EN: The House of Spiders: The Thumb Apprentice Heathcliff: On Clash Win using a Base Skill, inflict 2 Tremor and trigger Tremor Burst; then, reduce target's Tremor Count by 1 (2 times per turn)
   PL: Dom Pajęczyn: Uczeń Kciuka Heathcliff: wygrywając Starcie Umiejętnością bazową, nadaje 2 Wstrząsu i wywołuje Wybuch Wstrząsu; Licznik Wstrząsu celu maleje o 1 (2 razy na turę)
143. [Status [VibrationFocusing] — opis] {1} 턴 동안 진동 폭발 시 {0} x (60 + 공격자의 충전 위력 또는 특수 충전 x 8)%만큼 나태 피해를 입고 진동 횟수 1 감소\n· 르누아르 소속 캐릭터의 스킬, 패시브 효과로 진동 폭발 시 이 효과로 횟수가 감소하지 않음
   źródło: BuffAbilities.json :: dataList[id=VibrationFocusing].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: For {1} turns, upon Tremor Burst, take Sloth Damage equal to (60 + Sum of Charge Potency or Unique Charge on the attacker x 8)% of {0} and reduce the Count by 1\n  · When "Le Noir" units' Skills and Passives trigger Tremor Burst, the above effect does not reduce the Count
   PL: Przez {1} tur, przy Wybuchu Wstrząsu, otrzymuje obrażenia Lenistwa równe {0} x (60 + suma Mocy Ładowania lub Szczególnego Ładowania atakującego x 8)%, a Licznik maleje o 1\n· Przy Wybuchu Wstrząsu wywołanym Umiejętnościami i Pasywami postaci frakcji Le Noir Licznik nie maleje
144. [Status [RougeFamilySinclair] — opis] 자신을 제외한 르루주 소속 아군이 조건 만족 시 다음 효과 발동\n- 해당 캐릭터가 사망한 상태여도 효과 유지
   źródło: BuffAbilities.json :: dataList[id=RougeFamilySinclair].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When conditions are met by other "Le Rouge" allies, activate corresponding effects for Haute Couture::The Crimson God of Le Rouge Sinclair\n- Effects remain active even if the corresponding ally is defeated
   PL: - Gdy sojusznicy frakcji Le Rouge (poza tą jednostką) spełnią warunki, wywoływane są następujące efekty\n- Efekty pozostają aktywne nawet, gdy odpowiednia postać zginie
145. [Status [RougeFamily10816] — opis] 오트쿠튀르::르루주 부티크 이스마엘\n- 해당 캐릭터가 새단장 상태이면, 자신의 최대 체력 10% 증가. 기본 공격 적중 시 자신의 최대 체력의 5%만큼 체력 회복 (소수점 올림, 턴당 5회)
   źródło: BuffAbilities.json :: dataList[id=RougeFamily10816].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::Boutique du Rouge Ishmael\n- If Ishmael is in "Full Makeover" state, Sinclair's max HP +10%; Sinclair heals 5% max HP On Base Attack Hit (rounded up, 5 times per turn)
   PL: Haute Couture::Boutique du Rouge Ishmael\n- Jeśli Ishmael jest w stanie „Nowych Szat”, Maks. HP tej jednostki +10%; przy trafieniu Umiejętnością ataku bazowej leczy HP równe 5% własnego Maks. HP (zaokrąglone w górę, 5 razy na turę)
146. [Status [RougeFamily10717] — opis] 오트쿠튀르::르루주 바느질의 왕 히스클리프\n- '라 드망드(la demande)'스킬 코인 적중 시 맥동 횟수를 1 얻고, 자신의 최대 체력의 5%만큼 회복
   źródło: BuffAbilities.json :: dataList[id=RougeFamily10717].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::Le Rouge King of Needleworks Heathcliff\n- On Hit using the "La Demande" Skill's Coins, gain +1 Pulsation Count and heal 5% HP
   PL: Haute Couture::Le Rouge King of Needleworks Heathcliff\n- Przy trafieniu monetą Umiejętności „La Demande” zyskuje 1 Licznika Pulsacji i leczy HP równe 5% Maks. HP
147. [Status [RougeFamily11217] — opis] 오트쿠튀르::르루주 B2F 타래둥지 그레고르\n- 맥동 횟수 최대치 +5\n‘라 보라시테’, ‘라 카스트라시옹’ 스킬 사용 전 맥동 횟수 5 얻음
   źródło: BuffAbilities.json :: dataList[id=RougeFamily11217].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Haute Couture::Le Rouge B2F Skein Nest Gregor\n- Pulsation Count max cap +5\nGain +5 Pulsation Count before using the "La Voracité" and "La Castration" Skills
   PL: Haute Couture::Le Rouge B2F Skein Nest Gregor\n- Maks. Licznika Pulsacji +5\nPrzy użyciu Umiejętności „La Voracité” lub „La Castration” zyskuje 5 Licznika Pulsacji

## System komentatorów: AnnouncerTicketUIPopup
- plik gry: `AnnouncerTicketUIPopup.json`

148. [System komentatorów [select_announcer_popup_title] — tekst] 아나운서 선택
   źródło: AnnouncerTicketUIPopup.json :: dataList[id=select_announcer_popup_title].content
   limit: do 120 znaków
   EN: Select Announcer
   PL: Wybór Komentatora
149. [System komentatorów [select_announcer_popup_confirm_desc] — tekst] <color=#f8c200>{0}</color> 아나운서를 선택하시겠습니까?
   źródło: AnnouncerTicketUIPopup.json :: dataList[id=select_announcer_popup_confirm_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: Select <color=#f8c200>{0}</color> Announcer?
   PL: Czy wybrać Komentatora <color=#f8c200>{0}</color>?
150. [System komentatorów [select_announcer_popup_exchange_confirm_desc] — tekst] 보유 중인 아나운서 선택 시 {0}로 교환됩니다.
   źródło: AnnouncerTicketUIPopup.json :: dataList[id=select_announcer_popup_exchange_confirm_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Selecting an Announcer you already own will yield {0}.
   PL: Wybranie posiadanego już Komentatora da {0}.

## System komentatorów: AnnouncerVoiceType
- plik gry: `AnnouncerVoiceType.json`

151. [System komentatorów [Danger] — tekst] 긴박한 상황
   źródło: AnnouncerVoiceType.json :: dataList[id=Danger].content
   limit: do 120 znaków
   EN: Danger
   PL: Zagrożenie
152. [System komentatorów [SpecialSkill] — tekst] 강력한 스킬 경고
   źródło: AnnouncerVoiceType.json :: dataList[id=SpecialSkill].content
   limit: do 120 znaków
   EN: Powerful Enemy Skill Warning
   PL: Ostrzeżenie o potężnej Umiejętności wroga
153. [System komentatorów [SpecialGimmick] — tekst] 특수 기믹 알림
   źródło: AnnouncerVoiceType.json :: dataList[id=SpecialGimmick].content
   limit: do 120 znaków
   EN: Enemy Gimmick Warning
   PL: Powiadomienie o specjalnym mechanizmie wroga
154. [System komentatorów [AllyDebuff] — tekst] 아군에게 특수한 디버프
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyDebuff].content
   limit: do 120 znaków
   EN: Debuffed Allies
   PL: Sojusznicy z Specjalnym Osłabieniem
155. [System komentatorów [AllyBuff] — tekst] 아군에게 특수한 버프
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyBuff].content
   limit: do 120 znaków
   EN: Buffed Allies
   PL: Sojusznicy z Specjalnym Wzmocnieniem
156. [System komentatorów [SpecialCheer] — tekst] 상황별 응원
   źródło: AnnouncerVoiceType.json :: dataList[id=SpecialCheer].content
   limit: do 120 znaków
   EN: Situational Rally
   PL: Wsparcie zależne od sytuacji
157. [System komentatorów [EnemyAdv] — tekst] 적 우세
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyAdv].content
   limit: do 120 znaków
   EN: Enemy Advantage
   PL: Przewaga wroga
158. [System komentatorów [AllyDead] — tekst] 아군 사망 시
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyDead].content
   limit: do 120 znaków
   EN: Ally Death
   PL: Śmierć sojusznika
159. [System komentatorów [AllyBigDamage_Round] — tekst] 큰 피해 입은 후 다음 턴 시작
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyBigDamage_Round].content
   limit: do 120 znaków
   EN: Starting Turn after taking Devastating Damage
   PL: Początek tury po otrzymaniu poważnych obrażeń
160. [System komentatorów [AllyAdvEx] — tekst] 아군 역전
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyAdvEx].content
   limit: do 120 znaków
   EN: Ally Turnabout
   PL: Sojusznik odwraca losy
161. [System komentatorów [AllyAdv] — tekst] 아군 우세
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyAdv].content
   limit: do 120 znaków
   EN: Ally Advantage
   PL: Przewaga sojuszników
162. [System komentatorów [AllyBreak] — tekst] 아군 흐트러짐
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyBreak].content
   limit: do 120 znaków
   EN: Ally Staggered
   PL: Oszołomienie sojusznika
163. [System komentatorów [KillEnemy] — tekst] 적 처치 시
   źródło: AnnouncerVoiceType.json :: dataList[id=KillEnemy].content
   limit: do 120 znaków
   EN: Enemy Kill
   PL: Zabójstwo wroga
164. [System komentatorów [EnemyDestroy_RoundStart] — tekst] 적 부위 파괴 후 다음 턴 시작
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyDestroy_RoundStart].content
   limit: do 120 znaków
   EN: Starting Turn after Breaking Enemy Part
   PL: Początek tury po zniszczeniu części wroga
165. [System komentatorów [EnemyBigDamage_Round] — tekst] 큰 피해 입힌 후 다음 턴 시작
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyBigDamage_Round].content
   limit: do 120 znaków
   EN: Starting Turn after dealing Devastating Damage
   PL: Początek tury po zadaniu poważnych obrażeń
166. [System komentatorów [EnemyBreak] — tekst] 적 흐트러짐
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyBreak].content
   limit: do 120 znaków
   EN: Enemy Staggered
   PL: Oszołomienie wroga
167. [System komentatorów [Cheer] — tekst] 응원
   źródło: AnnouncerVoiceType.json :: dataList[id=Cheer].content
   limit: do 120 znaków
   EN: Rally
   PL: Wsparcie
168. [System komentatorów [AllyBigDamage] — tekst] 큰 피해 입을 시
   źródło: AnnouncerVoiceType.json :: dataList[id=AllyBigDamage].content
   limit: do 120 znaków
   EN: Taking Devastating Damage
   PL: Otrzymywanie poważnych obrażeń
169. [System komentatorów [EnemyBigDamage] — tekst] 큰 피해 입힐 시
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyBigDamage].content
   limit: do 120 znaków
   EN: Dealing Devastating Damage
   PL: Zadawanie poważnych obrażeń
170. [System komentatorów [EnemyDestroy_Battle] — tekst] 적 부위 파괴
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyDestroy_Battle].content
   limit: do 120 znaków
   EN: Breaking Enemy Part
   PL: Niszczenie części wroga
171. [System komentatorów [MultiKillEnemy] — tekst] 아군이 적 다수 처치 시
   źródło: AnnouncerVoiceType.json :: dataList[id=MultiKillEnemy].content
   limit: do 120 znaków
   EN: Ally Multikill
   PL: Sojusznik uzyskuje wielokrotne zabójstwo
172. [System komentatorów [Equip] — tekst] 배틀 아나운서 장착
   źródło: AnnouncerVoiceType.json :: dataList[id=Equip].content
   limit: do 120 znaków
   EN: Equipping Announcer
   PL: Wyposażanie Komentatora
173. [System komentatorów [PhysicalAdv] — tekst] 적합한 물리 피해
   źródło: AnnouncerVoiceType.json :: dataList[id=PhysicalAdv].content
   limit: do 120 znaków
   EN: Advantageous Attack Type
   PL: Korzystny Typ Ataku
174. [System komentatorów [AttrAdv] — tekst] 적합한 속성 피해
   źródło: AnnouncerVoiceType.json :: dataList[id=AttrAdv].content
   limit: do 120 znaków
   EN: Advantageous Affinity Type
   PL: Korzystny Typ Atrybutu
175. [System komentatorów [PhysicalDisadv] — tekst] 부적합한 물리 피해
   źródło: AnnouncerVoiceType.json :: dataList[id=PhysicalDisadv].content
   limit: do 120 znaków
   EN: Disadvantageous Attack Type
   PL: Niekorzystny Typ Ataku
176. [System komentatorów [AttrDisadv] — tekst] 부적합한 속성 피해
   źródło: AnnouncerVoiceType.json :: dataList[id=AttrDisadv].content
   limit: do 120 znaków
   EN: Disadvantageous Affinity Type
   PL: Niekorzystny Typ Atrybutu
177. [System komentatorów [EnemyBuff] — tekst] 적에게 특수한 버프
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyBuff].content
   limit: do 120 znaków
   EN: Buffed Enemies
   PL: Wrogowie z Specjalnym Wzmocnieniem
178. [System komentatorów [EnemyDebuff] — tekst] 적에게 특수한 디버프
   źródło: AnnouncerVoiceType.json :: dataList[id=EnemyDebuff].content
   limit: do 120 znaków
   EN: Debuffed Enemies
   PL: Wrogowie z Specjalnym Osłabieniem
179. [System komentatorów [Neglect] — tekst] 아무 조작 없을 시
   źródło: AnnouncerVoiceType.json :: dataList[id=Neglect].content
   limit: do 120 znaków
   EN: No Input for an Extended Period of Time
   PL: Brak aktywności przez dłuższy czas
180. [System komentatorów [MultiKillAlly] — tekst] 아군 다수가 사망시
   źródło: AnnouncerVoiceType.json :: dataList[id=MultiKillAlly].content
   limit: do 120 znaków
   EN: Multiple Ally Deaths
   PL: Śmierć wielu sojuszników
181. [System komentatorów [Win] — tekst] 전투 승리
   źródło: AnnouncerVoiceType.json :: dataList[id=Win].content
   limit: do 120 znaków
   EN: Victory Cry
   PL: Zwycięstwo w walce
182. [System komentatorów [Defeat] — tekst] 전투 패배
   źródło: AnnouncerVoiceType.json :: dataList[id=Defeat].content
   limit: do 120 znaków
   EN: Defeat Wail
   PL: Porażka w walce

## Komentator bitwy [1]: Dante (단테)
- ID komentatora: `1` · pliki kwestii: BattleAnnouncerDlg/Announcer_Dante_1.json

183. [Komentator [1] — nazwa] 단테
   źródło: Announcer.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Dante
   PL: Dante

## Komentator bitwy [2]: Gregor (그레고르)
- ID komentatora: `2` · pliki kwestii: BattleAnnouncerDlg/Announcer_Gregor_2.json

184. [Komentator [2] — nazwa] 그레고르
   źródło: Announcer.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor

## Komentator bitwy [3]: Charon (카론)
- ID komentatora: `3` · pliki kwestii: BattleAnnouncerDlg/Announcer_Charon_3.json

185. [Komentator [3] — nazwa] 카론
   źródło: Announcer.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Charon
   PL: Charon

## Komentator bitwy [4]: Sinclair (싱클레어)
- ID komentatora: `4` · pliki kwestii: BattleAnnouncerDlg/Announcer_Sinclair_4.json

186. [Komentator [4] — nazwa] 싱클레어
   źródło: Announcer.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair

## Komentator bitwy [5]: Rodion (로쟈)
- ID komentatora: `5` · pliki kwestii: BattleAnnouncerDlg/Announcer_Rodion_5.json

187. [Komentator [5] — nazwa] 로쟈
   źródło: Announcer.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion

## Komentator bitwy [6]: Yi Sang (이상)
- ID komentatora: `6` · pliki kwestii: BattleAnnouncerDlg/Announcer_Yisang_6.json

188. [Komentator [6] — nazwa] 이상
   źródło: Announcer.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang

## Komentator bitwy [7]: Effie/Saude (에피/소드)
- ID komentatora: `7` · pliki kwestii: BattleAnnouncerDlg/Announcer_EpiSode_7.json

189. [Komentator [7] — nazwa] 에피/소드
   źródło: Announcer.json :: dataList[id=7].name
   limit: do 40 znaków
   EN: Effie/Saude
   PL: Effie/Saude

## Komentator bitwy [8]: Ishmael (이스마엘)
- ID komentatora: `8` · pliki kwestii: BattleAnnouncerDlg/Announcer_Ishmael_8.json

190. [Komentator [8] — nazwa] 이스마엘
   źródło: Announcer.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael

## Komentator bitwy [9]: Yuri (유리)
- ID komentatora: `9` · pliki kwestii: BattleAnnouncerDlg/Announcer_Yuri_9.json

191. [Komentator [9] — nazwa] 유리
   źródło: Announcer.json :: dataList[id=9].name
   limit: do 40 znaków
   EN: Yuri
   PL: Yuri

## Komentator bitwy [10]: Malkuth (말쿠트)
- ID komentatora: `10` · pliki kwestii: BattleAnnouncerDlg/Announcer_Malkuth_10.json

192. [Komentator [10] — nazwa] 말쿠트
   źródło: Announcer.json :: dataList[id=10].name
   limit: do 40 znaków
   EN: Malkuth
   PL: Malkuth

## Komentator bitwy [11]: Pierre/Jack (피에르/잭)
- ID komentatora: `11` · pliki kwestii: BattleAnnouncerDlg/Announcer_JackPierre_11.json

193. [Komentator [11] — nazwa] 피에르/잭
   źródło: Announcer.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: Pierre/Jack
   PL: Pierre/Jack

## Komentator bitwy [12]: Angela <size=90%>(Lobotomy Corporation AI)</size> (앤젤라 <size=90%>(로보토미 코퍼레이션 AI)</size>)
- ID komentatora: `12` · pliki kwestii: BattleAnnouncerDlg/Announcer_Angela_12.json

194. [Komentator [12] — nazwa] 앤젤라\n<size=90%>(로보토미 코퍼레이션 AI)</size>
   źródło: Announcer.json :: dataList[id=12].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: <size=90%>, </size>, \n
   EN: Angela\n<size=90%>(Lobotomy Corporation AI)</size>
   PL: Angela\n<size=90%>(AI Lobotomy Corporation)</size>

## Komentator bitwy [13]: Nelly (넬리)
- ID komentatora: `13` · pliki kwestii: BattleAnnouncerDlg/Announcer_Nellie_13.json

195. [Komentator [13] — nazwa] 넬리
   źródło: Announcer.json :: dataList[id=13].name
   limit: do 40 znaków
   EN: Nelly
   PL: Nelly

## Komentator bitwy [14]: Heathcliff (히스클리프)
- ID komentatora: `14` · pliki kwestii: BattleAnnouncerDlg/Announcer_Heathcliff_14.json

196. [Komentator [14] — nazwa] 히스클리프
   źródło: Announcer.json :: dataList[id=14].name
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff

## Komentator bitwy [15]: Samjo (삼조)
- ID komentatora: `15` · pliki kwestii: BattleAnnouncerDlg/Announcer_Samjo_15.json

197. [Komentator [15] — nazwa] 삼조
   źródło: Announcer.json :: dataList[id=15].name
   limit: do 40 znaków
   EN: Samjo
   PL: Samjo

## Komentator bitwy [16]: Yesod (예소드)
- ID komentatora: `16` · pliki kwestii: BattleAnnouncerDlg/Announcer_Yesod_16.json

198. [Komentator [16] — nazwa] 예소드
   źródło: Announcer.json :: dataList[id=16].name
   limit: do 40 znaków
   EN: Yesod
   PL: Yesod

## Komentator bitwy [17]: Molar Office (어금니 사무소)
- ID komentatora: `17` · pliki kwestii: BattleAnnouncerDlg/Announcer_Molar_17.json

199. [Komentator [17] — nazwa] 어금니 사무소
   źródło: Announcer.json :: dataList[id=17].name
   limit: do 40 znaków
   EN: Molar Office
   PL: Biuro Trzonowca

## Komentator bitwy [18]: Hod (호드)
- ID komentatora: `18` · pliki kwestii: BattleAnnouncerDlg/Announcer_Hod_18.json

200. [Komentator [18] — nazwa] 호드
   źródło: Announcer.json :: dataList[id=18].name
   limit: do 40 znaków
   EN: Hod
   PL: Hod

## Komentator bitwy [19]: Dawn Office (새벽 사무소)
- ID komentatora: `19` · pliki kwestii: BattleAnnouncerDlg/Announcer_Dawn_19.json

201. [Komentator [19] — nazwa] 새벽 사무소
   źródło: Announcer.json :: dataList[id=19].name
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu

## Komentator bitwy [20]: Sancho (산초)
- ID komentatora: `20` · pliki kwestii: BattleAnnouncerDlg/Announcer_Sancho_20.json

202. [Komentator [20] — nazwa] 산초
   źródło: Announcer.json :: dataList[id=20].name
   limit: do 40 znaków
   EN: Sancho
   PL: Sancho

## Komentator bitwy [21]: Don Quixote (돈키호테)
- ID komentatora: `21` · pliki kwestii: BattleAnnouncerDlg/Announcer_DonQuixote_21.json

203. [Komentator [21] — nazwa] 돈키호테
   źródło: Announcer.json :: dataList[id=21].name
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote

## Komentator bitwy [22]: Bloodfiends of La Mancha (라만차의 혈귀)
- ID komentatora: `22` · pliki kwestii: BattleAnnouncerDlg/Announcer_LaMancha_22.json

204. [Komentator [22] — nazwa] 라만차의 혈귀
   źródło: Announcer.json :: dataList[id=22].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Bloodfiends\nof La Mancha
   PL: Krwiożercy z La Manchy

## Komentator bitwy [23]: Gnome Tri-ome! (노움 삼총사라움!)
- ID komentatora: `23` · pliki kwestii: BattleAnnouncerDlg/Announcer_Gnome_23.json

205. [Komentator [23] — nazwa] 노움 삼총사라움!
   źródło: Announcer.json :: dataList[id=23].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gnome\nTri-ome!
   PL: Gnome Tri-ome!

## Komentator bitwy [24]: Netzach (네짜흐)
- ID komentatora: `24` · pliki kwestii: BattleAnnouncerDlg/Announcer_Netzach_24.json

206. [Komentator [24] — nazwa] 네짜흐
   źródło: Announcer.json :: dataList[id=24].name
   limit: do 40 znaków
   EN: Netzach
   PL: Netzach

## Komentator bitwy [25]: Full-Stop Office (마침표 사무소)
- ID komentatora: `25` · pliki kwestii: BattleAnnouncerDlg/Announcer_FullStop_25.json

207. [Komentator [25] — nazwa] 마침표 사무소
   źródło: Announcer.json :: dataList[id=25].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full-Stop\nOffice
   PL: Biuro Kropki

## Komentator bitwy [26]: Aeng-du (앵두)
- ID komentatora: `26` · pliki kwestii: BattleAnnouncerDlg/Announcer_Aengdu_26.json

208. [Komentator [26] — nazwa] 앵두
   źródło: Announcer.json :: dataList[id=26].name
   limit: do 40 znaków
   EN: Aeng-du
   PL: Aeng-du

## Komentator bitwy [27]: Jun (쥰)
- ID komentatora: `27` · pliki kwestii: BattleAnnouncerDlg/Announcer_Jun_27.json

209. [Komentator [27] — nazwa] 쥰
   źródło: Announcer.json :: dataList[id=27].name
   limit: do 40 znaków
   EN: Jun
   PL: Jun

## Komentator bitwy [28]: Vergilius (베르길리우스)
- ID komentatora: `28` · pliki kwestii: BattleAnnouncerDlg/Announcer_Vergilius_28.json

210. [Komentator [28] — nazwa] 베르길리우스
   źródło: Announcer.json :: dataList[id=28].name
   limit: do 40 znaków
   EN: Vergilius
   PL: Wergiliusz

## Komentator bitwy [29]: Ricardo (리카르도)
- ID komentatora: `29` · pliki kwestii: BattleAnnouncerDlg/Announcer_Ricardo_29.json

211. [Komentator [29] — nazwa] 리카르도
   źródło: Announcer.json :: dataList[id=29].name
   limit: do 40 znaków
   EN: Ricardo
   PL: Ricardo

## Komentator bitwy [30]: Zilu/Zigong (자로/자공)
- ID komentatora: `30` · pliki kwestii: BattleAnnouncerDlg/Announcer_ZigongZilu_30.json

212. [Komentator [30] — nazwa] 자로/자공
   źródło: Announcer.json :: dataList[id=30].name
   limit: do 40 znaków
   EN: Zilu/Zigong
   PL: Zilu/Zigong

## Komentator bitwy [31]: Hong Lu (홍루)
- ID komentatora: `31` · pliki kwestii: BattleAnnouncerDlg/Announcer_Honglu_31.json

213. [Komentator [31] — nazwa] 홍루
   źródło: Announcer.json :: dataList[id=31].name
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu

## Komentator bitwy [32]: Magical Girl (The Queen of Hatred) (마법소녀 (증오의 여왕))
- ID komentatora: `32` · pliki kwestii: BattleAnnouncerDlg/Announcer_Magical_32.json

214. [Komentator [32] — nazwa] 마법소녀 (증오의 여왕)
   źródło: Announcer.json :: dataList[id=32].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Magical Girl\n(The Queen of Hatred)
   PL: Czarodziejka (Królowa Nienawiści)

## Komentator bitwy [33]: Tiphereth (티페리트)
- ID komentatora: `33` · pliki kwestii: BattleAnnouncerDlg/Announcer_Tiphereth_33.json

215. [Komentator [33] — nazwa] 티페리트
   źródło: Announcer.json :: dataList[id=33].name
   limit: do 40 znaków
   EN: Tiphereth
   PL: Tiphereth

## Komentator bitwy [34]: Herbert (허버트)
- ID komentatora: `34` · pliki kwestii: BattleAnnouncerDlg/Announcer_Hubert_34.json

216. [Komentator [34] — nazwa] 허버트
   źródło: Announcer.json :: dataList[id=34].name
   limit: do 40 znaków
   EN: Herbert
   PL: Herbert

## Komentator bitwy [35]: T Corp. Temp Special Investigators (임시 T사 특별수사관들)
- ID komentatora: `35` · pliki kwestii: BattleAnnouncerDlg/Announcer_DetectiveTrio_35.json

217. [Komentator [35] — nazwa] 임시 T사 특별수사관들
   źródło: Announcer.json :: dataList[id=35].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: T Corp. Temp\nSpecial Investigators
   PL: Tymczasowi Specjalni Śledczy T Corp.

## Komentator bitwy [36]: Jia Xichun/Wei (가시춘/웨이)
- ID komentatora: `36` · pliki kwestii: BattleAnnouncerDlg/Announcer_XichunWei_36.json

218. [Komentator [36] — nazwa] 가시춘/웨이
   źródło: Announcer.json :: dataList[id=36].name
   limit: do 40 znaków
   EN: Jia Xichun/Wei
   PL: Jia Xichun/Wei

## Komentator bitwy [37]: Amiya (아미야)
- ID komentatora: `37` · pliki kwestii: BattleAnnouncerDlg/Announcer_Amiya_37.json

219. [Komentator [37] — nazwa] 아미야
   źródło: Announcer.json :: dataList[id=37].name
   limit: do 40 znaków
   EN: Amiya
   PL: Amiya

## Komentator bitwy [38]: W Corp. WARP Train PA System (W사 워프 열차 방송)
- ID komentatora: `38` · pliki kwestii: BattleAnnouncerDlg/Announcer_WarpAnnouncer_38.json

220. [Komentator [38] — nazwa] W사 워프 열차 방송
   źródło: Announcer.json :: dataList[id=38].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: W Corp. WARP\nTrain PA System
   PL: System Nagłośnienia Pociągu WARP W Corp.

## Komentator bitwy [39]: Gebura (게부라)
- ID komentatora: `39` · pliki kwestii: BattleAnnouncerDlg/Announcer_Gebura_39.json

221. [Komentator [39] — nazwa] 게부라
   źródło: Announcer.json :: dataList[id=39].name
   limit: do 40 znaków
   EN: Gebura
   PL: Gebura

## Komentator bitwy [40]: Lei Heng (뇌횡)
- ID komentatora: `40` · pliki kwestii: BattleAnnouncerDlg/Announcer_Leiheng_40.json

222. [Komentator [40] — nazwa] 뇌횡
   źródło: Announcer.json :: dataList[id=40].name
   limit: do 40 znaków
   EN: Lei Heng
   PL: Lei Heng

## Komentator bitwy [41]: Araya (아라야)
- ID komentatora: `41` · pliki kwestii: BattleAnnouncerDlg/Announcer_PinkyChibi_41.json

223. [Komentator [41] — nazwa] ??
   źródło: Announcer-a1c9p1.json :: dataList[id=41].name
   limit: do 40 znaków
   EN: ??
   PL: ??
224. [Komentator [41] — nazwa] 아라야
   źródło: Announcer-a1c9p3.json :: dataList[id=41].name
   limit: do 40 znaków
   EN: Araya
   PL: Araya

## Komentator bitwy [42]: Ryōshū (료슈)
- ID komentatora: `42` · pliki kwestii: BattleAnnouncerDlg/Announcer_Ryoshu_42.json

225. [Komentator [42] — nazwa] ??
   źródło: Announcer-a1c9p1.json :: dataList[id=42].name
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Komentator [42] — nazwa] 료슈
   źródło: Announcer-a1c9p3.json :: dataList[id=42].name
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū

## Komentator bitwy [43]: Angela <size=90%>(Library Director - Early Days)</size> (앤젤라 <size=90%>(도서관 관장 - 초기)</size>)
- ID komentatora: `43` · pliki kwestii: BattleAnnouncerDlg/Announcer_AngelaLoR_43.json

227. [Komentator [43] — nazwa] 앤젤라\n<size=90%>(도서관 관장 - 초기)</size>
   źródło: Announcer.json :: dataList[id=43].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: <size=90%>, </size>, \n
   EN: Angela\n<size=90%>(Library Director - Early Days)</size>
   PL: Angela\n<size=90%>(Dyrektorka Biblioteki — Pierwsze Dni)</size>

## Komentator bitwy [44]: Chesed (헤세드)
- ID komentatora: `44` · pliki kwestii: BattleAnnouncerDlg/Announcer_Chesed_44.json

228. [Komentator [44] — nazwa] 헤세드
   źródło: Announcer.json :: dataList[id=44].name
   limit: do 40 znaków
   EN: Chesed
   PL: Chesed

## Komentator bitwy [45]: LCE Research Team (LCE 연구팀)
- ID komentatora: `45` · pliki kwestii: BattleAnnouncerDlg/Announcer_LCE_45.json

229. [Komentator [45] — nazwa] LCE 연구팀
   źródło: Announcer.json :: dataList[id=45].name
   limit: do 40 znaków
   EN: LCE Research Team
   PL: Zespół Badawczy LCE

## Komentator bitwy [46]: Kira (키라)
- ID komentatora: `46` · pliki kwestii: BattleAnnouncerDlg/Announcer_Kira_46.json

230. [Komentator [46] — nazwa] 키라
   źródło: Announcer.json :: dataList[id=46].name
   limit: do 40 znaków
   EN: Kira
   PL: Kira

## Komentator bitwy [47]: <District 8 Sweepers> (8구 청소부들)
- ID komentatora: `47` · pliki kwestii: BattleAnnouncerDlg/Announcer_Sweepers_47.json

231. [Komentator [47] — nazwa] 8구 청소부들
   źródło: Announcer.json :: dataList[id=47].name
   limit: do 40 znaków
   EN: <District 8 Sweepers>
   PL: Sprzątacze Dystryktu 8

## Komentator bitwy [48]: <District 8 Sweepers [Interpreted]> (8구 청소부들[통역])
- ID komentatora: `48` · pliki kwestii: BattleAnnouncerDlg/Announcer_Sweepers_48.json

232. [Komentator [48] — nazwa] 8구 청소부들[통역]
   źródło: Announcer.json :: dataList[id=48].name
   limit: do 50 znaków
   EN: <District 8 Sweepers [Interpreted]>
   PL: Sprzątacze Dystryktu 8 [Zinterpretowani]

## Komentator bitwy [49]: Bamboo-hatted Kim & Aeng-Du (김삿갓/앵두)
- ID komentatora: `49` · pliki kwestii: BattleAnnouncerDlg/Announcer_SatgatAengdu_49.json

233. [Komentator [49] — nazwa] 김삿갓/앵두
   źródło: Announcer.json :: dataList[id=49].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Bamboo-hatted Kim\n& Aeng-Du
   PL: Kim w Słomkowym Kapeluszu i Aeng-du

## Komentator bitwy [50]: Binah (비나)
- ID komentatora: `50` · pliki kwestii: BattleAnnouncerDlg/Announcer_Binah_50.json

234. [Komentator [50] — nazwa] 비나
   źródło: Announcer.json :: dataList[id=50].name
   limit: do 40 znaków
   EN: Binah
   PL: Binah

## Komentator bitwy [51]: Matthias/Kira (마티아스/키라)
- ID komentatora: `51` · pliki kwestii: BattleAnnouncerDlg/Announcer_MatthiasKira_51.json

235. [Komentator [51] — nazwa] 마티아스/키라
   źródło: Announcer.json :: dataList[id=51].name
   limit: do 40 znaków
   EN: Matthias/Kira
   PL: Matthias/Kira

## Komentator bitwy [52]: Valencina/Lucio (발렌치나/루치오)
- ID komentatora: `52` · pliki kwestii: BattleAnnouncerDlg/Announcer_ValencinaLucio_52.json

236. [Komentator [52] — nazwa] 발렌치나/루치오
   źródło: Announcer.json :: dataList[id=52].name
   limit: do 40 znaków
   EN: Valencina/Lucio
   PL: Valencina/Lucio

## Komentator bitwy [53]: Callisto/Albina (칼리스토/알비나)
- ID komentatora: `53` · pliki kwestii: BattleAnnouncerDlg/Announcer_CallistoAlbina_53.json

237. [Komentator [53] — nazwa] 칼리스토/알비나
   źródło: Announcer.json :: dataList[id=53].name
   limit: do 40 znaków
   EN: Callisto/Albina
   PL: Callisto/Albina

## Komentator bitwy [54]: Rien/Sora (뤼엔/소라)
- ID komentatora: `54` · pliki kwestii: BattleAnnouncerDlg/Announcer_RienSora_54.json

238. [Komentator [54] — nazwa] 뤼엔/소라
   źródło: Announcer.json :: dataList[id=54].name
   limit: do 40 znaków
   EN: Rien/Sora
   PL: Rien/Sora

## Komentator bitwy [55]: G.M. Sisyphe Customer Announcement (시지프 백화점 안내방송)
- ID komentatora: `55` · pliki kwestii: BattleAnnouncerDlg/Announcer_Emporium_55.json

239. [Komentator [55] — nazwa] 시지프 백화점 안내방송
   źródło: Announcer-a1c10p1.json :: dataList[id=55].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: G.M. Sisyphe\nCustomer Announcement
   PL: Komunikat dla Klientów Domu Towarowego Sisyphe
240. [Komentator [55] — nazwa] 시지프 백화점 안내방송
   źródło: Announcer-a1c10p3.json :: dataList[id=55].name
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Komentator [55] — nazwa] 시지프 백화점 안내방송
   źródło: Announcer.json :: dataList[id=55].name
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Komentator bitwy [56]: Jeanne (잔느)
- ID komentatora: `56` · pliki kwestii: BattleAnnouncerDlg/Announcer_Jeanne_56.json

242. [Komentator [56] — nazwa] ??
   źródło: Announcer-a1c10p1.json :: dataList[id=56].name
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Komentator [56] — nazwa] 잔느
   źródło: Announcer-a1c10p3.json :: dataList[id=56].name
   limit: do 40 znaków
   EN: Jeanne
   PL: Jeanne
244. [Komentator [56] — nazwa] 잔느
   źródło: Announcer.json :: dataList[id=56].name
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Komentator bitwy [57]: Meursault (뫼르소)
- ID komentatora: `57` · pliki kwestii: BattleAnnouncerDlg/Announcer_Meursault_57.json

245. [Komentator [57] — nazwa] ??
   źródło: Announcer-a1c10p1.json :: dataList[id=57].name
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Komentator [57] — nazwa] 뫼르소
   źródło: Announcer-a1c10p3.json :: dataList[id=57].name
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
247. [Komentator [57] — nazwa] 뫼르소
   źródło: Announcer.json :: dataList[id=57].name
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Komentator bitwy [58]: Pwie (뿌이)
- ID komentatora: `58` · pliki kwestii: BattleAnnouncerDlg/Announcer_Pwei_58.json

248. [Komentator [58] — nazwa] 뿌이
   źródło: Announcer.json :: dataList[id=58].name
   limit: do 40 znaków
   EN: Pwie
   PL: Pwie

## Komentator bitwy [59]: Hokma (호크마)
- ID komentatora: `59` · pliki kwestii: BattleAnnouncerDlg/Announcer_Hokma_59.json

249. [Komentator [59] — nazwa] 호크마
   źródło: Announcer.json :: dataList[id=59].name
   limit: do 40 znaków
   EN: Hokma
   PL: Hokma

## Komentator bitwy [60]: The Overseer (통제자)
- ID komentatora: `60` · pliki kwestii: BattleAnnouncerDlg/Announcer_Overseer_60.json

250. [Komentator [60] — nazwa] 통제자
   źródło: Announcer.json :: dataList[id=60].name
   limit: do 40 znaków
   EN: The Overseer
   PL: Nadzorca

## Komentator bitwy [90001]: Hohenheim (호엔하임)
- ID komentatora: `90001` · pliki kwestii: BattleAnnouncerDlg/Announcer_Hohenheim_90001.json

251. [Komentator [90001] — nazwa] 호엔하임
   źródło: Announcer.json :: dataList[id=90001].name
   limit: do 40 znaków
   EN: Hohenheim
   PL: Hohenheim

## Komentator bitwy [90002]: Charon (카론)
- ID komentatora: `90002` · pliki kwestii: BattleAnnouncerDlg/Announcer_Charon_90002.json

252. [Komentator [90002] — nazwa] 카론
   źródło: Announcer-m4d1.json :: dataList[id=90002].name
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Komentator bitwy [90003]: LCCB Manager Saude (LCCB 과장 소드)
- ID komentatora: `90003` · pliki kwestii: BattleAnnouncerDlg/Announcer_Sode_90003.json

253. [Komentator [90003] — nazwa] LCCB 과장 소드
   źródło: Announcer-a1c9p3.json :: dataList[id=90003].name
   limit: do 40 znaków
   EN: LCCB Manager Saude
   PL: Kierownik LCCB Saude

## Komentator bitwy [90004]: LCD Team Aeng-du (LCD 팀 앵두)
- ID komentatora: `90004` · pliki kwestii: BattleAnnouncerDlg/Announcer_LCDAengdu_90004.json

254. [Komentator [90004] — nazwa] LCD 팀 앵두
   źródło: Announcer-a1c9p3.json :: dataList[id=90004].name
   limit: do 40 znaków
   EN: LCD Team Aeng-du
   PL: Zespół LCD — Aeng-du

## Komentator bitwy [90005]: Outis (오티스)
- ID komentatora: `90005` · pliki kwestii: BattleAnnouncerDlg/Announcer_X1P1C1_90005.json

255. [Komentator [90005] — nazwa] 오티스
   źródło: Announcer-x1p1c1.json :: dataList[id=90005].name
   limit: do 40 znaków
   EN: Outis
   PL: Outis

## Komentator bitwy [90006]: Yi Sang (이상)
- ID komentatora: `90006` · pliki kwestii: BattleAnnouncerDlg/Announcer_X1P1C1_90006.json

256. [Komentator [90006] — nazwa] 이상
   źródło: Announcer-x1p1c1.json :: dataList[id=90006].name
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Komentator bitwy [90007]: Faust (파우스트)
- ID komentatora: `90007` · pliki kwestii: BattleAnnouncerDlg/Announcer_X1P1C1_90007.json

257. [Komentator [90007] — nazwa] 파우스트
   źródło: Announcer-x1p1c1.json :: dataList[id=90007].name
   limit: do 40 znaków
   EN: Faust
   PL: Faust

## Komentator bitwy [90008]: Patron Librarian Malkuth [Floor of History] (지정사서 말쿠트[역사의 층])
- ID komentatora: `90008` · pliki kwestii: BattleAnnouncerDlg/Announcer_Walpu10_90008.json

258. [Komentator [90008] — nazwa] 지정사서 말쿠트[역사의 층]
   źródło: Announcer-walpu10.json :: dataList[id=90008].name
   limit: do 60 znaków
   EN: Patron Librarian Malkuth [Floor of History]
   PL: Wyznaczony Bibliotekarz Malkuth [Piętro Historii]

## Muzyka i tekst utworu: LobbyBGM-29
- plik gry: `LobbyBGM-29.json`

259. [Muzyka i tekst utworu [200303 · wykonawca: Mili] — nazwa] Rendezvous
   źródło: LobbyBGM-29.json :: dataList[id=200303].name
   limit: do 40 znaków
   EN: Rendezvous
   PL: Rendezvous
260. [Muzyka i tekst utworu [200304 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.뫼르소
   źródło: LobbyBGM-29.json :: dataList[id=200304].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Meursault
   PL: Sarajinae (Pass On) - ver. Meursault
261. [Muzyka i tekst utworu [200305 · wykonawca: ProjectMoon] — nazwa] Punctum
   źródło: LobbyBGM-29.json :: dataList[id=200305].name
   limit: do 40 znaków
   EN: Punctum
   PL: Punctum
262. [Muzyka i tekst utworu [200306 · wykonawca: ProjectMoon] — nazwa] Affliction
   źródło: LobbyBGM-29.json :: dataList[id=200306].name
   limit: do 40 znaków
   EN: Affliction
   PL: Affliction
263. [Muzyka i tekst utworu [200307 · wykonawca: ProjectMoon] — nazwa] Floor Nobody
   źródło: LobbyBGM-29.json :: dataList[id=200307].name
   limit: do 40 znaków
   EN: Floor Nobody
   PL: Floor Nobody
264. [Muzyka i tekst utworu [200308 · wykonawca: ProjectMoon] — nazwa] Precious Than Your Brain
   źródło: LobbyBGM-29.json :: dataList[id=200308].name
   limit: do 40 znaków
   EN: Precious Than Your Brain
   PL: Precious Than Your Brain
265. [Muzyka i tekst utworu [200309 · wykonawca: ProjectMoon] — nazwa] And There
   źródło: LobbyBGM-29.json :: dataList[id=200309].name
   limit: do 40 znaków
   EN: And There
   PL: And There
266. [Muzyka i tekst utworu [200310 · wykonawca: ProjectMoon] — nazwa] Passion Red
   źródło: LobbyBGM-29.json :: dataList[id=200310].name
   limit: do 40 znaków
   EN: Passion Red
   PL: Passion Red
267. [Muzyka i tekst utworu [200311 · wykonawca: ProjectMoon] — nazwa] Run, Not Walk
   źródło: LobbyBGM-29.json :: dataList[id=200311].name
   limit: do 40 znaków
   EN: Run, Not Walk
   PL: Run, Not Walk
268. [Muzyka i tekst utworu [200312 · wykonawca: ProjectMoon] — nazwa] Timewalker
   źródło: LobbyBGM-29.json :: dataList[id=200312].name
   limit: do 40 znaków
   EN: Timewalker
   PL: Timewalker
269. [Muzyka i tekst utworu [200313 · wykonawca: ProjectMoon] — nazwa] Reason Black
   źródło: LobbyBGM-29.json :: dataList[id=200313].name
   limit: do 40 znaków
   EN: Reason Black
   PL: Reason Black
270. [Muzyka i tekst utworu [200314 · wykonawca: ProjectMoon] — nazwa] Never Look Back
   źródło: LobbyBGM-29.json :: dataList[id=200314].name
   limit: do 40 znaków
   EN: Never Look Back
   PL: Never Look Back
271. [Muzyka i tekst utworu [200315 · wykonawca: ProjectMoon] — nazwa] Good Sinew To Cut
   źródło: LobbyBGM-29.json :: dataList[id=200315].name
   limit: do 40 znaków
   EN: Good Sinew To Cut
   PL: Good Sinew To Cut
272. [Muzyka i tekst utworu [200316 · wykonawca: ProjectMoon] — nazwa] I Said Run
   źródło: LobbyBGM-29.json :: dataList[id=200316].name
   limit: do 40 znaków
   EN: I Said Run
   PL: I Said Run
273. [Muzyka i tekst utworu [200317 · wykonawca: ProjectMoon] — nazwa] Enough Height To Fall
   źródło: LobbyBGM-29.json :: dataList[id=200317].name
   limit: do 40 znaków
   EN: Enough Height To Fall
   PL: Enough Height To Fall
274. [Muzyka i tekst utworu [200318 · wykonawca: ProjectMoon] — nazwa] Sisyphe Emporium
   źródło: LobbyBGM-29.json :: dataList[id=200318].name
   limit: do 40 znaków
   EN: Sisyphe Emporium
   PL: Sisyphe Emporium
275. [Muzyka i tekst utworu [200319 · wykonawca: ProjectMoon] — nazwa] Rust Free Chair
   źródło: LobbyBGM-29.json :: dataList[id=200319].name
   limit: do 40 znaków
   EN: Rust Free Chair
   PL: Rust Free Chair
276. [Muzyka i tekst utworu [200320 · wykonawca: ProjectMoon] — nazwa] Please Follow Nobody
   źródło: LobbyBGM-29.json :: dataList[id=200320].name
   limit: do 40 znaków
   EN: Please Follow Nobody
   PL: Please Follow Nobody
277. [Muzyka i tekst utworu [200321 · wykonawca: ProjectMoon] — nazwa] Fresh Meal
   źródło: LobbyBGM-29.json :: dataList[id=200321].name
   limit: do 40 znaków
   EN: Fresh Meal
   PL: Fresh Meal
278. [Muzyka i tekst utworu [200322 · wykonawca: ProjectMoon] — nazwa] Soleil
   źródło: LobbyBGM-29.json :: dataList[id=200322].name
   limit: do 40 znaków
   EN: Soleil
   PL: Soleil
279. [Muzyka i tekst utworu [200323 · wykonawca: ProjectMoon] — nazwa] Faint Aroma
   źródło: LobbyBGM-29.json :: dataList[id=200323].name
   limit: do 40 znaków
   EN: Faint Aroma
   PL: Faint Aroma
280. [Muzyka i tekst utworu [200324 · wykonawca: ProjectMoon] — nazwa] Intruder
   źródło: LobbyBGM-29.json :: dataList[id=200324].name
   limit: do 40 znaków
   EN: Intruder
   PL: Intruder
281. [Muzyka i tekst utworu [200325 · wykonawca: ProjectMoon] — nazwa] Endless Pain
   źródło: LobbyBGM-29.json :: dataList[id=200325].name
   limit: do 40 znaków
   EN: Endless Pain
   PL: Endless Pain
282. [Muzyka i tekst utworu [200326 · wykonawca: ProjectMoon] — nazwa] Calvary
   źródło: LobbyBGM-29.json :: dataList[id=200326].name
   limit: do 40 znaków
   EN: Calvary
   PL: Calvary
283. [Muzyka i tekst utworu [200327 · wykonawca: ProjectMoon] — nazwa] Endless Death
   źródło: LobbyBGM-29.json :: dataList[id=200327].name
   limit: do 40 znaków
   EN: Endless Death
   PL: Endless Death
284. [Muzyka i tekst utworu [200328 · wykonawca: ProjectMoon] — nazwa] You Can Be Good Leather
   źródło: LobbyBGM-29.json :: dataList[id=200328].name
   limit: do 40 znaków
   EN: You Can Be Good Leather
   PL: You Can Be Good Leather
285. [Muzyka i tekst utworu [200329 · wykonawca: ProjectMoon] — nazwa] Studium
   źródło: LobbyBGM-29.json :: dataList[id=200329].name
   limit: do 40 znaków
   EN: Studium
   PL: Studium
286. [Muzyka i tekst utworu [200330 · wykonawca: ProjectMoon] — nazwa] Le Rouge et Le Noir
   źródło: LobbyBGM-29.json :: dataList[id=200330].name
   limit: do 40 znaków
   EN: Le Rouge et Le Noir
   PL: Le Rouge et Le Noir
287. [Muzyka i tekst utworu [200331 · wykonawca: Studio EIM] — nazwa] Canto X Battle 01
   źródło: LobbyBGM-29.json :: dataList[id=200331].name
   limit: do 40 znaków
   EN: Canto X Battle 01
   PL: Canto X Battle 01
288. [Muzyka i tekst utworu [200332 · wykonawca: Studio EIM] — nazwa] Canto X Battle 02
   źródło: LobbyBGM-29.json :: dataList[id=200332].name
   limit: do 40 znaków
   EN: Canto X Battle 02
   PL: Canto X Battle 02
289. [Muzyka i tekst utworu [200333 · wykonawca: Studio EIM] — nazwa] Canto X Battle 03
   źródło: LobbyBGM-29.json :: dataList[id=200333].name
   limit: do 40 znaków
   EN: Canto X Battle 03
   PL: Canto X Battle 03
290. [Muzyka i tekst utworu [200334 · wykonawca: Studio EIM] — nazwa] Canto X Battle 04
   źródło: LobbyBGM-29.json :: dataList[id=200334].name
   limit: do 40 znaków
   EN: Canto X Battle 04
   PL: Canto X Battle 04
291. [Muzyka i tekst utworu [200335 · wykonawca: Studio EIM] — nazwa] The Symbolic Battle [Le Rouge]
   źródło: LobbyBGM-29.json :: dataList[id=200335].name
   limit: do 50 znaków
   EN: The Symbolic Battle [Le Rouge]
   PL: The Symbolic Battle [Le Rouge]
292. [Muzyka i tekst utworu [200336 · wykonawca: Studio EIM] — nazwa] The Crimson God [Inchoate Life]
   źródło: LobbyBGM-29.json :: dataList[id=200336].name
   limit: do 50 znaków
   EN: The Crimson God [Inchoate Life]
   PL: The Crimson God [Inchoate Life]
293. [Muzyka i tekst utworu [200337 · wykonawca: Studio EIM] — nazwa] The Symbolic Battle [Le Noir]
   źródło: LobbyBGM-29.json :: dataList[id=200337].name
   limit: do 50 znaków
   EN: The Symbolic Battle [Le Noir]
   PL: The Symbolic Battle [Le Noir]
294. [Muzyka i tekst utworu [200338 · wykonawca: Studio EIM] — nazwa] Le Noir's Brand Manager
   źródło: LobbyBGM-29.json :: dataList[id=200338].name
   limit: do 40 znaków
   EN: Le Noir's Brand Manager
   PL: Le Noir's Brand Manager
295. [Muzyka i tekst utworu [200339 · wykonawca: Studio EIM] — nazwa] The Symbolic Battle [The Warden]
   źródło: LobbyBGM-29.json :: dataList[id=200339].name
   limit: do 50 znaków
   EN: The Symbolic Battle [The Warden]
   PL: The Symbolic Battle [The Warden]
296. [Muzyka i tekst utworu [200340 · wykonawca: Studio EIM] — nazwa] Battle The Warden Phase1
   źródło: LobbyBGM-29.json :: dataList[id=200340].name
   limit: do 40 znaków
   EN: Battle The Warden Phase1
   PL: Battle The Warden Phase1
297. [Muzyka i tekst utworu [200341 · wykonawca: Studio EIM] — nazwa] Battle The Warden Phase2
   źródło: LobbyBGM-29.json :: dataList[id=200341].name
   limit: do 40 znaków
   EN: Battle The Warden Phase2
   PL: Battle The Warden Phase2
298. [Muzyka i tekst utworu [200342 · wykonawca: Studio EIM] — nazwa] Battle The Warden Phase3
   źródło: LobbyBGM-29.json :: dataList[id=200342].name
   limit: do 40 znaków
   EN: Battle The Warden Phase3
   PL: Battle The Warden Phase3
299. [Muzyka i tekst utworu [200343 · wykonawca: Studio EIM] — nazwa] The Symbolic Battle [Buffet]
   źródło: LobbyBGM-29.json :: dataList[id=200343].name
   limit: do 40 znaków
   EN: The Symbolic Battle [Buffet]
   PL: The Symbolic Battle [Buffet]
300. [Muzyka i tekst utworu [200344 · wykonawca: Studio EIM] — nazwa] Battle Buffet Phase1
   źródło: LobbyBGM-29.json :: dataList[id=200344].name
   limit: do 40 znaków
   EN: Battle Buffet Phase1
   PL: Battle Buffet Phase1
301. [Muzyka i tekst utworu [200345 · wykonawca: Studio EIM] — nazwa] Battle Buffet Phase2
   źródło: LobbyBGM-29.json :: dataList[id=200345].name
   limit: do 40 znaków
   EN: Battle Buffet Phase2
   PL: Battle Buffet Phase2

## Muzyka i tekst utworu: LobbyBGM
- plik gry: `LobbyBGM.json`

302. [Muzyka i tekst utworu [100001 · wykonawca: Mili] — nazwa] In Hell We Live, Lament (inst)
   źródło: LobbyBGM.json :: dataList[id=100001].name
   limit: do 50 znaków
   EN: In Hell We Live, Lament (inst)
   PL: In Hell We Live, Lament (inst)
303. [Muzyka i tekst utworu [100002 · wykonawca: Studio EIM] — nazwa] Window
   źródło: LobbyBGM.json :: dataList[id=100002].name
   limit: do 40 znaków
   EN: Window
   PL: Window
304. [Muzyka i tekst utworu [100003 · wykonawca: Studio EIM] — nazwa] Extract
   źródło: LobbyBGM.json :: dataList[id=100003].name
   limit: do 40 znaków
   EN: Extract
   PL: Extract
305. [Muzyka i tekst utworu [100004 · wykonawca: Studio EIM] — nazwa] Battle Victory
   źródło: LobbyBGM.json :: dataList[id=100004].name
   limit: do 40 znaków
   EN: Battle Victory
   PL: Battle Victory
306. [Muzyka i tekst utworu [100005 · wykonawca: Mili] — nazwa] In Hell We Live, Lament
   źródło: LobbyBGM.json :: dataList[id=100005].name
   limit: do 40 znaków
   EN: In Hell We Live, Lament
   PL: In Hell We Live, Lament
307. [Muzyka i tekst utworu [100006 · wykonawca: Mili] — nazwa] In Hell We Live, Lament (Long Ver)
   źródło: LobbyBGM.json :: dataList[id=100006].name
   limit: do 50 znaków
   EN: In Hell We Live, Lament (Long Ver.)
   PL: In Hell We Live, Lament (Long Ver)
308. [Muzyka i tekst utworu [200001 · wykonawca: Studio EIM] — nazwa] Backstreet
   źródło: LobbyBGM.json :: dataList[id=200001].name
   limit: do 40 znaków
   EN: Backstreet
   PL: Backstreet
309. [Muzyka i tekst utworu [200002 · wykonawca: Studio EIM] — nazwa] Bus Inside
   źródło: LobbyBGM.json :: dataList[id=200002].name
   limit: do 40 znaków
   EN: Bus Inside
   PL: Bus Inside
310. [Muzyka i tekst utworu [200003 · wykonawca: Studio EIM] — nazwa] Happy
   źródło: LobbyBGM.json :: dataList[id=200003].name
   limit: do 40 znaków
   EN: Happy
   PL: Happy
311. [Muzyka i tekst utworu [200004 · wykonawca: Studio EIM] — nazwa] Daily
   źródło: LobbyBGM.json :: dataList[id=200004].name
   limit: do 40 znaków
   EN: Daily
   PL: Daily
312. [Muzyka i tekst utworu [200005 · wykonawca: Studio EIM] — nazwa] Depressed
   źródło: LobbyBGM.json :: dataList[id=200005].name
   limit: do 40 znaków
   EN: Depressed
   PL: Depressed
313. [Muzyka i tekst utworu [200006 · wykonawca: Studio EIM] — nazwa] Nervous
   źródło: LobbyBGM.json :: dataList[id=200006].name
   limit: do 40 znaków
   EN: Nervous
   PL: Nervous
314. [Muzyka i tekst utworu [200007 · wykonawca: Studio EIM] — nazwa] Serious
   źródło: LobbyBGM.json :: dataList[id=200007].name
   limit: do 40 znaków
   EN: Serious
   PL: Serious
315. [Muzyka i tekst utworu [200008 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.그레고르
   źródło: LobbyBGM.json :: dataList[id=200008].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Gregor
   PL: Sarajinae (Pass On) - ver. Gregor
316. [Muzyka i tekst utworu [200009 · wykonawca: Studio EIM] — nazwa] Anxiety
   źródło: LobbyBGM.json :: dataList[id=200009].name
   limit: do 40 znaków
   EN: Anxiety
   PL: Anxiety
317. [Muzyka i tekst utworu [200010 · wykonawca: Studio EIM] — nazwa] War
   źródło: LobbyBGM.json :: dataList[id=200010].name
   limit: do 40 znaków
   EN: War
   PL: War
318. [Muzyka i tekst utworu [200011 · wykonawca: Studio EIM] — nazwa] Canto I Battle 01
   źródło: LobbyBGM.json :: dataList[id=200011].name
   limit: do 40 znaków
   EN: Canto I Battle 01
   PL: Canto I Battle 01
319. [Muzyka i tekst utworu [200012 · wykonawca: Studio EIM] — nazwa] Canto I Battle 02
   źródło: LobbyBGM.json :: dataList[id=200012].name
   limit: do 40 znaków
   EN: Canto I Battle 02
   PL: Canto I Battle 02
320. [Muzyka i tekst utworu [200013 · wykonawca: Studio EIM] — nazwa] Canto I Battle 03
   źródło: LobbyBGM.json :: dataList[id=200013].name
   limit: do 40 znaków
   EN: Canto I Battle 03
   PL: Canto I Battle 03
321. [Muzyka i tekst utworu [200014 · wykonawca: Studio EIM] — nazwa] Canto I Battle 04
   źródło: LobbyBGM.json :: dataList[id=200014].name
   limit: do 40 znaków
   EN: Canto I Battle 04
   PL: Canto I Battle 04
322. [Muzyka i tekst utworu [200015 · wykonawca: Studio EIM] — nazwa] Canto I Battle 05
   źródło: LobbyBGM.json :: dataList[id=200015].name
   limit: do 40 znaków
   EN: Canto I Battle 05
   PL: Canto I Battle 05
323. [Muzyka i tekst utworu [200016 · wykonawca: Studio EIM] — nazwa] Canto I Battle 06
   źródło: LobbyBGM.json :: dataList[id=200016].name
   limit: do 40 znaków
   EN: Canto I Battle 06
   PL: Canto I Battle 06
324. [Muzyka i tekst utworu [200017 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.로쟈
   źródło: LobbyBGM.json :: dataList[id=200017].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Rodion
   PL: Sarajinae (Pass On) - ver. Rodion
325. [Muzyka i tekst utworu [200018 · wykonawca: Studio EIM] — nazwa] Casino 01
   źródło: LobbyBGM.json :: dataList[id=200018].name
   limit: do 40 znaków
   EN: Casino 01
   PL: Casino 01
326. [Muzyka i tekst utworu [200019 · wykonawca: Studio EIM] — nazwa] Casino 02
   źródło: LobbyBGM.json :: dataList[id=200019].name
   limit: do 40 znaków
   EN: Casino 02
   PL: Casino 02
327. [Muzyka i tekst utworu [200020 · wykonawca: Studio EIM] — nazwa] Sin
   źródło: LobbyBGM.json :: dataList[id=200020].name
   limit: do 40 znaków
   EN: Sin
   PL: Sin
328. [Muzyka i tekst utworu [200021 · wykonawca: Studio EIM] — nazwa] Canto II Battle 01
   źródło: LobbyBGM.json :: dataList[id=200021].name
   limit: do 40 znaków
   EN: Canto II Battle 01
   PL: Canto II Battle 01
329. [Muzyka i tekst utworu [200022 · wykonawca: Studio EIM] — nazwa] Canto II Battle 02
   źródło: LobbyBGM.json :: dataList[id=200022].name
   limit: do 40 znaków
   EN: Canto II Battle 02
   PL: Canto II Battle 02
330. [Muzyka i tekst utworu [200023 · wykonawca: Studio EIM] — nazwa] Canto II Battle 03
   źródło: LobbyBGM.json :: dataList[id=200023].name
   limit: do 40 znaków
   EN: Canto II Battle 03
   PL: Canto II Battle 03
331. [Muzyka i tekst utworu [200024 · wykonawca: Studio EIM] — nazwa] Canto II Battle 04
   źródło: LobbyBGM.json :: dataList[id=200024].name
   limit: do 40 znaków
   EN: Canto II Battle 04
   PL: Canto II Battle 04
332. [Muzyka i tekst utworu [200025 · wykonawca: Studio EIM] — nazwa] Canto II Battle 05
   źródło: LobbyBGM.json :: dataList[id=200025].name
   limit: do 40 znaków
   EN: Canto II Battle 05
   PL: Canto II Battle 05
333. [Muzyka i tekst utworu [200026 · wykonawca: Studio EIM] — nazwa] Canto II Battle 06
   źródło: LobbyBGM.json :: dataList[id=200026].name
   limit: do 40 znaków
   EN: Canto II Battle 06
   PL: Canto II Battle 06
334. [Muzyka i tekst utworu [200027 · wykonawca: Studio EIM] — nazwa] Canto II Battle 07
   źródło: LobbyBGM.json :: dataList[id=200027].name
   limit: do 40 znaków
   EN: Canto II Battle 07
   PL: Canto II Battle 07
335. [Muzyka i tekst utworu [200028 · wykonawca: Mili] — nazwa] Between Two Worlds
   źródło: LobbyBGM.json :: dataList[id=200028].name
   limit: do 40 znaków
   EN: Between Two Worlds
   PL: Between Two Worlds
336. [Muzyka i tekst utworu [200029 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.싱클레어
   źródło: LobbyBGM.json :: dataList[id=200029].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Sinclair
   PL: Sarajinae (Pass On) - ver. Sinclair
337. [Muzyka i tekst utworu [200030 · wykonawca: Studio EIM] — nazwa] Examiner
   źródło: LobbyBGM.json :: dataList[id=200030].name
   limit: do 40 znaków
   EN: Examiner
   PL: Examiner
338. [Muzyka i tekst utworu [200031 · wykonawca: Studio EIM] — nazwa] Sinclair's Recollection 01
   źródło: LobbyBGM.json :: dataList[id=200031].name
   limit: do 40 znaków
   EN: Sinclair's Recollection 01
   PL: Sinclair's Recollection 01
339. [Muzyka i tekst utworu [200032 · wykonawca: Studio EIM] — nazwa] Sinclair's Recollection 02
   źródło: LobbyBGM.json :: dataList[id=200032].name
   limit: do 40 znaków
   EN: Sinclair's Recollection 02
   PL: Sinclair's Recollection 02
340. [Muzyka i tekst utworu [200033 · wykonawca: Studio EIM] — nazwa] Sinclair's hometown
   źródło: LobbyBGM.json :: dataList[id=200033].name
   limit: do 40 znaków
   EN: Sinclair's Hometown
   PL: Sinclair's hometown
341. [Muzyka i tekst utworu [200034 · wykonawca: Studio EIM] — nazwa] Canto III Battle 01
   źródło: LobbyBGM.json :: dataList[id=200034].name
   limit: do 40 znaków
   EN: Canto III Battle 01
   PL: Canto III Battle 01
342. [Muzyka i tekst utworu [200035 · wykonawca: Studio EIM] — nazwa] Canto III Battle 02
   źródło: LobbyBGM.json :: dataList[id=200035].name
   limit: do 40 znaków
   EN: Canto III Battle 02
   PL: Canto III Battle 02
343. [Muzyka i tekst utworu [200036 · wykonawca: Studio EIM] — nazwa] Canto III Battle 03
   źródło: LobbyBGM.json :: dataList[id=200036].name
   limit: do 40 znaków
   EN: Canto III Battle 03
   PL: Canto III Battle 03
344. [Muzyka i tekst utworu [200037 · wykonawca: Studio EIM] — nazwa] Canto III Battle 04
   źródło: LobbyBGM.json :: dataList[id=200037].name
   limit: do 40 znaków
   EN: Canto III Battle 04
   PL: Canto III Battle 04
345. [Muzyka i tekst utworu [200038 · wykonawca: Studio EIM] — nazwa] Canto III Battle 05
   źródło: LobbyBGM.json :: dataList[id=200038].name
   limit: do 40 znaków
   EN: Canto III Battle 05
   PL: Canto III Battle 05
346. [Muzyka i tekst utworu [200039 · wykonawca: Studio EIM] — nazwa] Canto III Battle 06
   źródło: LobbyBGM.json :: dataList[id=200039].name
   limit: do 40 znaków
   EN: Canto III Battle 06
   PL: Canto III Battle 06
347. [Muzyka i tekst utworu [200040 · wykonawca: Studio EIM] — nazwa] Canto III Battle 07
   źródło: LobbyBGM.json :: dataList[id=200040].name
   limit: do 40 znaków
   EN: Canto III Battle 07
   PL: Canto III Battle 07
348. [Muzyka i tekst utworu [200042 · wykonawca: Studio EIM] — nazwa] Eunbong’s Bar & Fryers
   źródło: LobbyBGM.json :: dataList[id=200042].name
   limit: do 40 znaków
   EN: Eunbong’s Bar & Fryers
   PL: Eunbong’s Bar & Fryers
349. [Muzyka i tekst utworu [200043 · wykonawca: Studio EIM] — nazwa] Hell's Chicken
   źródło: LobbyBGM.json :: dataList[id=200043].name
   limit: do 40 znaków
   EN: Hell's Chicken
   PL: Hell's Chicken
350. [Muzyka i tekst utworu [200044 · wykonawca: Studio EIM] — nazwa] Hell's Chicken Battle 01
   źródło: LobbyBGM.json :: dataList[id=200044].name
   limit: do 40 znaków
   EN: Hell's Chicken Battle 01
   PL: Hell's Chicken Battle 01
351. [Muzyka i tekst utworu [200045 · wykonawca: Studio EIM] — nazwa] Hell's Chicken Battle 02
   źródło: LobbyBGM.json :: dataList[id=200045].name
   limit: do 40 znaków
   EN: Hell's Chicken Battle 02
   PL: Hell's Chicken Battle 02
352. [Muzyka i tekst utworu [200046 · wykonawca: ProjectMoon] — nazwa] Budda
   źródło: LobbyBGM.json :: dataList[id=200046].name
   limit: do 40 znaków
   EN: Budda
   PL: Budda
353. [Muzyka i tekst utworu [200047 · wykonawca: Mili] — nazwa] Fly, My Wings
   źródło: LobbyBGM.json :: dataList[id=200047].name
   limit: do 40 znaków
   EN: Fly, My Wings
   PL: Fly, My Wings
354. [Muzyka i tekst utworu [200048 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.이상
   źródło: LobbyBGM.json :: dataList[id=200048].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Yi Sang
   PL: Sarajinae (Pass On) - ver. Yi Sang
355. [Muzyka i tekst utworu [200049 · wykonawca: Studio EIM] — nazwa] K Corp's Lab
   źródło: LobbyBGM.json :: dataList[id=200049].name
   limit: do 40 znaków
   EN: K Corp's Lab
   PL: K Corp's Lab
356. [Muzyka i tekst utworu [200050 · wykonawca: Studio EIM] — nazwa] Abnormal Science
   źródło: LobbyBGM.json :: dataList[id=200050].name
   limit: do 40 znaków
   EN: Abnormal Science
   PL: Abnormal Science
357. [Muzyka i tekst utworu [200051 · wykonawca: ProjectMoon] — nazwa] Dongbaek
   źródło: LobbyBGM.json :: dataList[id=200051].name
   limit: do 40 znaków
   EN: Dongbaek
   PL: Dongbaek
358. [Muzyka i tekst utworu [200052 · wykonawca: Studio EIM] — nazwa] Destroyed Lab
   źródło: LobbyBGM.json :: dataList[id=200052].name
   limit: do 40 znaków
   EN: Destroyed Lab
   PL: Destroyed Lab
359. [Muzyka i tekst utworu [200053 · wykonawca: Studio EIM] — nazwa] League of Nine Littérateurs - Spring
   źródło: LobbyBGM.json :: dataList[id=200053].name
   limit: do 50 znaków
   EN: League of Nine Littérateurs - Spring
   PL: League of Nine Littérateurs - Spring
360. [Muzyka i tekst utworu [200054 · wykonawca: Studio EIM] — nazwa] League of Nine Littérateurs - Summer
   źródło: LobbyBGM.json :: dataList[id=200054].name
   limit: do 50 znaków
   EN: League of Nine Littérateurs - Summer
   PL: League of Nine Littérateurs - Summer
361. [Muzyka i tekst utworu [200055 · wykonawca: Studio EIM] — nazwa] League of Nine Littérateurs - Autumn
   źródło: LobbyBGM.json :: dataList[id=200055].name
   limit: do 50 znaków
   EN: League of Nine Littérateurs - Autumn
   PL: League of Nine Littérateurs - Autumn
362. [Muzyka i tekst utworu [200056 · wykonawca: Studio EIM] — nazwa] Tearful Thing
   źródło: LobbyBGM.json :: dataList[id=200056].name
   limit: do 40 znaków
   EN: Tearful Thing
   PL: Tearful Thing
363. [Muzyka i tekst utworu [200057 · wykonawca: Studio EIM] — nazwa] Reminiscence
   źródło: LobbyBGM.json :: dataList[id=200057].name
   limit: do 40 znaków
   EN: Reminiscence
   PL: Reminiscence
364. [Muzyka i tekst utworu [200058 · wykonawca: ProjectMoon] — nazwa] Cry For My Dream
   źródło: LobbyBGM.json :: dataList[id=200058].name
   limit: do 40 znaków
   EN: Cry For My Dream
   PL: Cry For My Dream
365. [Muzyka i tekst utworu [200059 · wykonawca: ProjectMoon] — nazwa] We'd Lost Our Winter
   źródło: LobbyBGM.json :: dataList[id=200059].name
   limit: do 40 znaków
   EN: We'd Lost Our Winter
   PL: We'd Lost Our Winter
366. [Muzyka i tekst utworu [200060 · wykonawca: ProjectMoon] — nazwa] What Are You Thinking
   źródło: LobbyBGM.json :: dataList[id=200060].name
   limit: do 40 znaków
   EN: What Are You Thinking
   PL: What Are You Thinking
367. [Muzyka i tekst utworu [200061 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 01
   źródło: LobbyBGM.json :: dataList[id=200061].name
   limit: do 40 znaków
   EN: Canto IV Battle 01
   PL: Canto IV Battle 01
368. [Muzyka i tekst utworu [200062 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 02
   źródło: LobbyBGM.json :: dataList[id=200062].name
   limit: do 40 znaków
   EN: Canto IV Battle 02
   PL: Canto IV Battle 02
369. [Muzyka i tekst utworu [200063 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 03
   źródło: LobbyBGM.json :: dataList[id=200063].name
   limit: do 40 znaków
   EN: Canto IV Battle 03
   PL: Canto IV Battle 03
370. [Muzyka i tekst utworu [200064 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 04
   źródło: LobbyBGM.json :: dataList[id=200064].name
   limit: do 40 znaków
   EN: Canto IV Battle 04
   PL: Canto IV Battle 04
371. [Muzyka i tekst utworu [200065 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 05
   źródło: LobbyBGM.json :: dataList[id=200065].name
   limit: do 40 znaków
   EN: Canto IV Battle 05
   PL: Canto IV Battle 05
372. [Muzyka i tekst utworu [200066 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 06
   źródło: LobbyBGM.json :: dataList[id=200066].name
   limit: do 40 znaków
   EN: Canto IV Battle 06
   PL: Canto IV Battle 06
373. [Muzyka i tekst utworu [200067 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 07
   źródło: LobbyBGM.json :: dataList[id=200067].name
   limit: do 40 znaków
   EN: Canto IV Battle 07
   PL: Canto IV Battle 07
374. [Muzyka i tekst utworu [200068 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 08
   źródło: LobbyBGM.json :: dataList[id=200068].name
   limit: do 40 znaków
   EN: Canto IV Battle 08
   PL: Canto IV Battle 08
375. [Muzyka i tekst utworu [200069 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 09
   źródło: LobbyBGM.json :: dataList[id=200069].name
   limit: do 40 znaków
   EN: Canto IV Battle 09
   PL: Canto IV Battle 09
376. [Muzyka i tekst utworu [200070 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 10
   źródło: LobbyBGM.json :: dataList[id=200070].name
   limit: do 40 znaków
   EN: Canto IV Battle 10
   PL: Canto IV Battle 10
377. [Muzyka i tekst utworu [200071 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 11
   źródło: LobbyBGM.json :: dataList[id=200071].name
   limit: do 40 znaków
   EN: Canto IV Battle 11
   PL: Canto IV Battle 11
378. [Muzyka i tekst utworu [200072 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 12
   źródło: LobbyBGM.json :: dataList[id=200072].name
   limit: do 40 znaków
   EN: Canto IV Battle 12
   PL: Canto IV Battle 12
379. [Muzyka i tekst utworu [200073 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 13
   źródło: LobbyBGM.json :: dataList[id=200073].name
   limit: do 40 znaków
   EN: Canto IV Battle 13
   PL: Canto IV Battle 13
380. [Muzyka i tekst utworu [200074 · wykonawca: Studio EIM] — nazwa] Canto IV Battle 14
   źródło: LobbyBGM.json :: dataList[id=200074].name
   limit: do 40 znaków
   EN: Canto IV Battle 14
   PL: Canto IV Battle 14
381. [Muzyka i tekst utworu [200075 · wykonawca: ProjectMoon] — nazwa] Oh Crab, So Crab
   źródło: LobbyBGM.json :: dataList[id=200075].name
   limit: do 40 znaków
   EN: Oh Crab, So Crab
   PL: Oh Crab, So Crab
382. [Muzyka i tekst utworu [200076 · wykonawca: ProjectMoon] — nazwa] Summer Splash
   źródło: LobbyBGM.json :: dataList[id=200076].name
   limit: do 40 znaków
   EN: Summer Splash
   PL: Summer Splash
383. [Muzyka i tekst utworu [200077 · wykonawca: Studio EIM] — nazwa] S.E.A.
   źródło: LobbyBGM.json :: dataList[id=200077].name
   limit: do 40 znaków
   EN: S.E.A.
   PL: S.E.A.
384. [Muzyka i tekst utworu [200078 · wykonawca: Studio EIM] — nazwa] S.E.A. Battle 01
   źródło: LobbyBGM.json :: dataList[id=200078].name
   limit: do 40 znaków
   EN: S.E.A. Battle 01
   PL: S.E.A. Battle 01
385. [Muzyka i tekst utworu [200079 · wykonawca: Studio EIM] — nazwa] S.E.A. Battle 02
   źródło: LobbyBGM.json :: dataList[id=200079].name
   limit: do 40 znaków
   EN: S.E.A. Battle 02
   PL: S.E.A. Battle 02
386. [Muzyka i tekst utworu [200080 · wykonawca: ProjectMoon] — nazwa] Flore sicut rosa
   źródło: LobbyBGM.json :: dataList[id=200080].name
   limit: do 40 znaków
   EN: Flore sicut rosa
   PL: Flore sicut rosa
387. [Muzyka i tekst utworu [200081 · wykonawca: Mili] — nazwa] Compass
   źródło: LobbyBGM.json :: dataList[id=200081].name
   limit: do 40 znaków
   EN: Compass
   PL: Compass
388. [Muzyka i tekst utworu [200082 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.이스마엘
   źródło: LobbyBGM.json :: dataList[id=200082].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Ishmael
   PL: Sarajinae (Pass On) - ver. Ishmael
389. [Muzyka i tekst utworu [200083 · wykonawca: ProjectMoon] — nazwa] Nobody Came Back
   źródło: LobbyBGM.json :: dataList[id=200083].name
   limit: do 40 znaków
   EN: Nobody Came Back
   PL: Nobody Came Back
390. [Muzyka i tekst utworu [200084 · wykonawca: ProjectMoon] — nazwa] Electronic Devil Maker
   źródło: LobbyBGM.json :: dataList[id=200084].name
   limit: do 40 znaków
   EN: Electronic Devil Maker
   PL: Electronic Devil Maker
391. [Muzyka i tekst utworu [200085 · wykonawca: ProjectMoon] — nazwa] Suspicious
   źródło: LobbyBGM.json :: dataList[id=200085].name
   limit: do 40 znaków
   EN: Suspicious
   PL: Suspicious
392. [Muzyka i tekst utworu [200086 · wykonawca: ProjectMoon] — nazwa] Middle Finger Toujou
   źródło: LobbyBGM.json :: dataList[id=200086].name
   limit: do 40 znaków
   EN: Middle Finger Toujou
   PL: Middle Finger Toujou
393. [Muzyka i tekst utworu [200087 · wykonawca: ProjectMoon] — nazwa] Bad Time
   źródło: LobbyBGM.json :: dataList[id=200087].name
   limit: do 40 znaków
   EN: Bad Time
   PL: Bad Time
394. [Muzyka i tekst utworu [200088 · wykonawca: ProjectMoon] — nazwa] Ship of Ghost
   źródło: LobbyBGM.json :: dataList[id=200088].name
   limit: do 40 znaków
   EN: Ship of Ghost
   PL: Ship of Ghost
395. [Muzyka i tekst utworu [200089 · wykonawca: ProjectMoon] — nazwa] Heart
   źródło: LobbyBGM.json :: dataList[id=200089].name
   limit: do 40 znaków
   EN: Heart
   PL: Heart
396. [Muzyka i tekst utworu [200090 · wykonawca: ProjectMoon] — nazwa] Negative Sail
   źródło: LobbyBGM.json :: dataList[id=200090].name
   limit: do 40 znaków
   EN: Negative Sail
   PL: Negative Sail
397. [Muzyka i tekst utworu [200091 · wykonawca: ProjectMoon] — nazwa] Positive Sail
   źródło: LobbyBGM.json :: dataList[id=200091].name
   limit: do 40 znaków
   EN: Positive Sail
   PL: Positive Sail
398. [Muzyka i tekst utworu [200092 · wykonawca: ProjectMoon] — nazwa] Port In Shadow
   źródło: LobbyBGM.json :: dataList[id=200092].name
   limit: do 40 znaków
   EN: Port In Shadow
   PL: Port In Shadow
399. [Muzyka i tekst utworu [200093 · wykonawca: ProjectMoon] — nazwa] Overwhelming
   źródło: LobbyBGM.json :: dataList[id=200093].name
   limit: do 40 znaków
   EN: Overwhelming
   PL: Overwhelming
400. [Muzyka i tekst utworu [200094 · wykonawca: ProjectMoon] — nazwa] Pequod
   źródło: LobbyBGM.json :: dataList[id=200094].name
   limit: do 40 znaków
   EN: Pequod
   PL: Pequod
401. [Muzyka i tekst utworu [200095 · wykonawca: ProjectMoon] — nazwa] Deep Cold Sea
   źródło: LobbyBGM.json :: dataList[id=200095].name
   limit: do 40 znaków
   EN: Deep Cold Sea
   PL: Deep Cold Sea
402. [Muzyka i tekst utworu [200096 · wykonawca: ProjectMoon] — nazwa] Unacceptable
   źródło: LobbyBGM.json :: dataList[id=200096].name
   limit: do 40 znaków
   EN: Unacceptable
   PL: Unacceptable
403. [Muzyka i tekst utworu [200097 · wykonawca: Studio EIM] — nazwa] Canto V Battle 01
   źródło: LobbyBGM.json :: dataList[id=200097].name
   limit: do 40 znaków
   EN: Canto V Battle 01
   PL: Canto V Battle 01
404. [Muzyka i tekst utworu [200098 · wykonawca: Studio EIM] — nazwa] Canto V Battle 02
   źródło: LobbyBGM.json :: dataList[id=200098].name
   limit: do 40 znaków
   EN: Canto V Battle 02
   PL: Canto V Battle 02
405. [Muzyka i tekst utworu [200099 · wykonawca: Studio EIM] — nazwa] Canto V Battle 03
   źródło: LobbyBGM.json :: dataList[id=200099].name
   limit: do 40 znaków
   EN: Canto V Battle 03
   PL: Canto V Battle 03
406. [Muzyka i tekst utworu [200100 · wykonawca: Studio EIM] — nazwa] Canto V Battle 04
   źródło: LobbyBGM.json :: dataList[id=200100].name
   limit: do 40 znaków
   EN: Canto V Battle 04
   PL: Canto V Battle 04
407. [Muzyka i tekst utworu [200101 · wykonawca: Studio EIM] — nazwa] Canto V Battle 05
   źródło: LobbyBGM.json :: dataList[id=200101].name
   limit: do 40 znaków
   EN: Canto V Battle 05
   PL: Canto V Battle 05
408. [Muzyka i tekst utworu [200102 · wykonawca: Studio EIM] — nazwa] Canto V Battle 06
   źródło: LobbyBGM.json :: dataList[id=200102].name
   limit: do 40 znaków
   EN: Canto V Battle 06
   PL: Canto V Battle 06
409. [Muzyka i tekst utworu [200103 · wykonawca: Studio EIM] — nazwa] Canto V Battle 07
   źródło: LobbyBGM.json :: dataList[id=200103].name
   limit: do 40 znaków
   EN: Canto V Battle 07
   PL: Canto V Battle 07
410. [Muzyka i tekst utworu [200104 · wykonawca: Studio EIM] — nazwa] Canto V Battle 08
   źródło: LobbyBGM.json :: dataList[id=200104].name
   limit: do 40 znaków
   EN: Canto V Battle 08
   PL: Canto V Battle 08
411. [Muzyka i tekst utworu [200105 · wykonawca: ProjectMoon] — nazwa] Canto V Battle 09
   źródło: LobbyBGM.json :: dataList[id=200105].name
   limit: do 40 znaków
   EN: Canto V Battle 09
   PL: Canto V Battle 09
412. [Muzyka i tekst utworu [200106 · wykonawca: Studio EIM] — nazwa] Canto V Battle 10
   źródło: LobbyBGM.json :: dataList[id=200106].name
   limit: do 40 znaków
   EN: Canto V Battle 10
   PL: Canto V Battle 10
413. [Muzyka i tekst utworu [200107 · wykonawca: Studio EIM] — nazwa] Canto V Battle 11
   źródło: LobbyBGM.json :: dataList[id=200107].name
   limit: do 40 znaków
   EN: Canto V Battle 11
   PL: Canto V Battle 11
414. [Muzyka i tekst utworu [200108 · wykonawca: Studio EIM] — nazwa] Canto V Battle 12
   źródło: LobbyBGM.json :: dataList[id=200108].name
   limit: do 40 znaków
   EN: Canto V Battle 12
   PL: Canto V Battle 12
415. [Muzyka i tekst utworu [200109 · wykonawca: ProjectMoon] — nazwa] Jingle Jingle
   źródło: LobbyBGM.json :: dataList[id=200109].name
   limit: do 40 znaków
   EN: Jingle Jingle
   PL: Jingle Jingle
416. [Muzyka i tekst utworu [200110 · wykonawca: ProjectMoon] — nazwa] We Wish You
   źródło: LobbyBGM.json :: dataList[id=200110].name
   limit: do 40 znaków
   EN: We Wish You
   PL: We Wish You
417. [Muzyka i tekst utworu [200111 · wykonawca: ProjectMoon] — nazwa] Or Maybe Not
   źródło: LobbyBGM.json :: dataList[id=200111].name
   limit: do 40 znaków
   EN: Or Maybe Not
   PL: Or Maybe Not
418. [Muzyka i tekst utworu [200112 · wykonawca: ProjectMoon] — nazwa] Clear Wind
   źródło: LobbyBGM.json :: dataList[id=200112].name
   limit: do 40 znaków
   EN: Clear Wind
   PL: Clear Wind
419. [Muzyka i tekst utworu [200113 · wykonawca: ProjectMoon] — nazwa] Bright Moon
   źródło: LobbyBGM.json :: dataList[id=200113].name
   limit: do 40 znaków
   EN: Bright Moon
   PL: Bright Moon
420. [Muzyka i tekst utworu [200114 · wykonawca: ProjectMoon] — nazwa] Thundercloud
   źródło: LobbyBGM.json :: dataList[id=200114].name
   limit: do 40 znaków
   EN: Thundercloud
   PL: Thundercloud
421. [Muzyka i tekst utworu [200115 · wykonawca: ProjectMoon] — nazwa] Flesh And Bone
   źródło: LobbyBGM.json :: dataList[id=200115].name
   limit: do 40 znaków
   EN: Flesh And Bone
   PL: Flesh And Bone
422. [Muzyka i tekst utworu [200116 · wykonawca: Studio EIM] — nazwa] Ready for Sword
   źródło: LobbyBGM.json :: dataList[id=200116].name
   limit: do 40 znaków
   EN: Ready for Sword
   PL: Ready for Sword
423. [Muzyka i tekst utworu [200117 · wykonawca: ProjectMoon] — nazwa] Miracle in District 20 Battle 01
   źródło: LobbyBGM.json :: dataList[id=200117].name
   limit: do 50 znaków
   EN: Miracle in District 20 Battle 01
   PL: Miracle in District 20 Battle 01
424. [Muzyka i tekst utworu [200118 · wykonawca: ProjectMoon] — nazwa] Miracle in District 20 Battle 02
   źródło: LobbyBGM.json :: dataList[id=200118].name
   limit: do 50 znaków
   EN: Miracle in District 20 Battle 02
   PL: Miracle in District 20 Battle 02
425. [Muzyka i tekst utworu [200119 · wykonawca: Studio EIM] — nazwa] Yield My Flesh to Claim Their Bones Battle 01
   źródło: LobbyBGM.json :: dataList[id=200119].name
   limit: do 70 znaków
   EN: Yield My Flesh to Claim Their Bones Battle 01
   PL: Yield My Flesh to Claim Their Bones Battle 01
426. [Muzyka i tekst utworu [200120 · wykonawca: Studio EIM] — nazwa] Yield My Flesh to Claim Their Bones Battle 02
   źródło: LobbyBGM.json :: dataList[id=200120].name
   limit: do 70 znaków
   EN: Yield My Flesh to Claim Their Bones Battle 02
   PL: Yield My Flesh to Claim Their Bones Battle 02
427. [Muzyka i tekst utworu [200121 · wykonawca: ProjectMoon] — nazwa] Cur dolorem sentis
   źródło: LobbyBGM.json :: dataList[id=200121].name
   limit: do 40 znaków
   EN: Cur dolorem sentis
   PL: Cur dolorem sentis
428. [Muzyka i tekst utworu [200122 · wykonawca: Mili] — nazwa] Through Patches of Violet
   źródło: LobbyBGM.json :: dataList[id=200122].name
   limit: do 40 znaków
   EN: Through Patches of Violet
   PL: Through Patches of Violet
429. [Muzyka i tekst utworu [200123 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.히스클리프
   źródło: LobbyBGM.json :: dataList[id=200123].name
   limit: do 60 znaków
   EN: Sarajinae (Pass On) - ver. Heathcliff
   PL: Sarajinae (Pass On) - ver. Heathcliff
430. [Muzyka i tekst utworu [200124 · wykonawca: ProjectMoon] — nazwa] Wuthering Opus 01
   źródło: LobbyBGM.json :: dataList[id=200124].name
   limit: do 40 znaków
   EN: Wuthering Opus 01
   PL: Wuthering Opus 01
431. [Muzyka i tekst utworu [200125 · wykonawca: ProjectMoon] — nazwa] Wuthering Opus 02
   źródło: LobbyBGM.json :: dataList[id=200125].name
   limit: do 40 znaków
   EN: Wuthering Opus 02
   PL: Wuthering Opus 02
432. [Muzyka i tekst utworu [200126 · wykonawca: ProjectMoon] — nazwa] Wuthering Opus 03
   źródło: LobbyBGM.json :: dataList[id=200126].name
   limit: do 40 znaków
   EN: Wuthering Opus 03
   PL: Wuthering Opus 03
433. [Muzyka i tekst utworu [200127 · wykonawca: ProjectMoon] — nazwa] Spanner And Drill
   źródło: LobbyBGM.json :: dataList[id=200127].name
   limit: do 40 znaków
   EN: Spanner And Drill
   PL: Spanner And Drill
434. [Muzyka i tekst utworu [200128 · wykonawca: ProjectMoon] — nazwa] Falling Down
   źródło: LobbyBGM.json :: dataList[id=200128].name
   limit: do 40 znaków
   EN: Falling Down
   PL: Falling Down
435. [Muzyka i tekst utworu [200129 · wykonawca: ProjectMoon] — nazwa] Take Off Your Veil
   źródło: LobbyBGM.json :: dataList[id=200129].name
   limit: do 40 znaków
   EN: Take Off Your Veil
   PL: Take Off Your Veil
436. [Muzyka i tekst utworu [200130 · wykonawca: ProjectMoon] — nazwa] Lone Wolf
   źródło: LobbyBGM.json :: dataList[id=200130].name
   limit: do 40 znaków
   EN: Lone Wolf
   PL: Lone Wolf
437. [Muzyka i tekst utworu [200131 · wykonawca: ProjectMoon] — nazwa] Distorted Dream
   źródło: LobbyBGM.json :: dataList[id=200131].name
   limit: do 40 znaków
   EN: Distorted Dream
   PL: Distorted Dream
438. [Muzyka i tekst utworu [200132 · wykonawca: ProjectMoon] — nazwa] Rise of Evil
   źródło: LobbyBGM.json :: dataList[id=200132].name
   limit: do 40 znaków
   EN: Rise of Evil
   PL: Rise of Evil
439. [Muzyka i tekst utworu [200133 · wykonawca: ProjectMoon] — nazwa] Erlkönig
   źródło: LobbyBGM.json :: dataList[id=200133].name
   limit: do 40 znaków
   EN: Erlkönig
   PL: Erlkönig
440. [Muzyka i tekst utworu [200134 · wykonawca: ProjectMoon] — nazwa] Endless Sorrow
   źródło: LobbyBGM.json :: dataList[id=200134].name
   limit: do 40 znaków
   EN: Endless Sorrow
   PL: Endless Sorrow
441. [Muzyka i tekst utworu [200135 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 01
   źródło: LobbyBGM.json :: dataList[id=200135].name
   limit: do 40 znaków
   EN: Canto VI Battle 01
   PL: Canto VI Battle 01
442. [Muzyka i tekst utworu [200136 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 02
   źródło: LobbyBGM.json :: dataList[id=200136].name
   limit: do 40 znaków
   EN: Canto VI Battle 02
   PL: Canto VI Battle 02
443. [Muzyka i tekst utworu [200137 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 03
   źródło: LobbyBGM.json :: dataList[id=200137].name
   limit: do 40 znaków
   EN: Canto VI Battle 03
   PL: Canto VI Battle 03
444. [Muzyka i tekst utworu [200138 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 04
   źródło: LobbyBGM.json :: dataList[id=200138].name
   limit: do 40 znaków
   EN: Canto VI Battle 04
   PL: Canto VI Battle 04
445. [Muzyka i tekst utworu [200139 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 05
   źródło: LobbyBGM.json :: dataList[id=200139].name
   limit: do 40 znaków
   EN: Canto VI Battle 05
   PL: Canto VI Battle 05
446. [Muzyka i tekst utworu [200140 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 06
   źródło: LobbyBGM.json :: dataList[id=200140].name
   limit: do 40 znaków
   EN: Canto VI Battle 06
   PL: Canto VI Battle 06
447. [Muzyka i tekst utworu [200141 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 07
   źródło: LobbyBGM.json :: dataList[id=200141].name
   limit: do 40 znaków
   EN: Canto VI Battle 07
   PL: Canto VI Battle 07
448. [Muzyka i tekst utworu [200142 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 08
   źródło: LobbyBGM.json :: dataList[id=200142].name
   limit: do 40 znaków
   EN: Canto VI Battle 08
   PL: Canto VI Battle 08
449. [Muzyka i tekst utworu [200143 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 09
   źródło: LobbyBGM.json :: dataList[id=200143].name
   limit: do 40 znaków
   EN: Canto VI Battle 09
   PL: Canto VI Battle 09
450. [Muzyka i tekst utworu [200144 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 10
   źródło: LobbyBGM.json :: dataList[id=200144].name
   limit: do 40 znaków
   EN: Canto VI Battle 10
   PL: Canto VI Battle 10
451. [Muzyka i tekst utworu [200145 · wykonawca: Studio EIM] — nazwa] Canto VI Battle 11
   źródło: LobbyBGM.json :: dataList[id=200145].name
   limit: do 40 znaków
   EN: Canto VI Battle 11
   PL: Canto VI Battle 11
452. [Muzyka i tekst utworu [200146 · wykonawca: Studio EIM] — nazwa] Heathcliff? Battle
   źródło: LobbyBGM.json :: dataList[id=200146].name
   limit: do 40 znaków
   EN: Heathcliff? Battle
   PL: Heathcliff? Battle
453. [Muzyka i tekst utworu [200147 · wykonawca: Studio EIM] — nazwa] Heathcliff, The Heartbroken Battle
   źródło: LobbyBGM.json :: dataList[id=200147].name
   limit: do 50 znaków
   EN: Heathcliff, The Heartbroken Battle
   PL: Heathcliff, The Heartbroken Battle
454. [Muzyka i tekst utworu [200149 · wykonawca: ProjectMoon] — nazwa] Observe, Not See
   źródło: LobbyBGM.json :: dataList[id=200149].name
   limit: do 40 znaków
   EN: Observe, Not See
   PL: Observe, Not See
455. [Muzyka i tekst utworu [200150 · wykonawca: Studio EIM] — nazwa] Good Day Detective
   źródło: LobbyBGM.json :: dataList[id=200150].name
   limit: do 40 znaków
   EN: Good Day Detective
   PL: Good Day Detective
456. [Muzyka i tekst utworu [200151 · wykonawca: ProjectMoon] — nazwa] Time Killing Time
   źródło: LobbyBGM.json :: dataList[id=200151].name
   limit: do 40 znaków
   EN: Time Killing Time
   PL: Time Killing Time
457. [Muzyka i tekst utworu [200152 · wykonawca: ProjectMoon] — nazwa] Warp Station
   źródło: LobbyBGM.json :: dataList[id=200152].name
   limit: do 40 znaków
   EN: Warp Station
   PL: Warp Station
458. [Muzyka i tekst utworu [200153 · wykonawca: ProjectMoon] — nazwa] Warp Malfunction
   źródło: LobbyBGM.json :: dataList[id=200153].name
   limit: do 40 znaków
   EN: Warp Malfunction
   PL: Warp Malfunction
459. [Muzyka i tekst utworu [200154 · wykonawca: ProjectMoon] — nazwa] Train of Bloodshed
   źródło: LobbyBGM.json :: dataList[id=200154].name
   limit: do 40 znaków
   EN: Train of Bloodshed
   PL: Train of Bloodshed
460. [Muzyka i tekst utworu [200155 · wykonawca: ProjectMoon] — nazwa] Yet Tense
   źródło: LobbyBGM.json :: dataList[id=200155].name
   limit: do 40 znaków
   EN: Yet Tense
   PL: Yet Tense
461. [Muzyka i tekst utworu [200156 · wykonawca: Studio EIM] — nazwa] Timekilling Time Battle 01
   źródło: LobbyBGM.json :: dataList[id=200156].name
   limit: do 40 znaków
   EN: Timekilling Time Battle 01
   PL: Timekilling Time Battle 01
462. [Muzyka i tekst utworu [200157 · wykonawca: Studio EIM] — nazwa] Timekilling Time Battle 02
   źródło: LobbyBGM.json :: dataList[id=200157].name
   limit: do 40 znaków
   EN: Timekilling Time Battle 02
   PL: Timekilling Time Battle 02
463. [Muzyka i tekst utworu [200158 · wykonawca: Studio EIM] — nazwa] Murder on the WARP Express Battle 01
   źródło: LobbyBGM.json :: dataList[id=200158].name
   limit: do 50 znaków
   EN: Murder on the WARP Express Battle 01
   PL: Murder on the WARP Express Battle 01
464. [Muzyka i tekst utworu [200159 · wykonawca: Studio EIM] — nazwa] Murder on the WARP Express Battle 02
   źródło: LobbyBGM.json :: dataList[id=200159].name
   limit: do 50 znaków
   EN: Murder on the WARP Express Battle 02
   PL: Murder on the WARP Express Battle 02
465. [Muzyka i tekst utworu [200160 · wykonawca: ProjectMoon] — nazwa] Audite, pauper
   źródło: LobbyBGM.json :: dataList[id=200160].name
   limit: do 40 znaków
   EN: Audite, pauper
   PL: Audite, pauper
466. [Muzyka i tekst utworu [200161 · wykonawca: ProjectMoon] — nazwa] Vovete miserias
   źródło: LobbyBGM.json :: dataList[id=200161].name
   limit: do 40 znaków
   EN: Vovete miserias
   PL: Vovete miserias
467. [Muzyka i tekst utworu [200162 · wykonawca: Mili] — nazwa] Hero
   źródło: LobbyBGM.json :: dataList[id=200162].name
   limit: do 40 znaków
   EN: Hero
   PL: Hero
468. [Muzyka i tekst utworu [200163 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.돈키호테
   źródło: LobbyBGM.json :: dataList[id=200163].name
   limit: do 60 znaków
   EN: Sarajinae (Pass On) - ver. Don Quixote
   PL: Sarajinae (Pass On) - ver. Don Quixote
469. [Muzyka i tekst utworu [200164 · wykonawca: ProjectMoon] — nazwa] Absolutely Nothing
   źródło: LobbyBGM.json :: dataList[id=200164].name
   limit: do 40 znaków
   EN: Absolutely Nothing
   PL: Absolutely Nothing
470. [Muzyka i tekst utworu [200165 · wykonawca: ProjectMoon] — nazwa] Cautious Operation
   źródło: LobbyBGM.json :: dataList[id=200165].name
   limit: do 40 znaków
   EN: Cautious Operation
   PL: Cautious Operation
471. [Muzyka i tekst utworu [200166 · wykonawca: ProjectMoon] — nazwa] Welcome Back
   źródło: LobbyBGM.json :: dataList[id=200166].name
   limit: do 40 znaków
   EN: Welcome Back
   PL: Welcome Back
472. [Muzyka i tekst utworu [200167 · wykonawca: ProjectMoon] — nazwa] Inconvenient Welcome
   źródło: LobbyBGM.json :: dataList[id=200167].name
   limit: do 40 znaków
   EN: Inconvenient Welcome
   PL: Inconvenient Welcome
473. [Muzyka i tekst utworu [200168 · wykonawca: ProjectMoon] — nazwa] Shooting Range
   źródło: LobbyBGM.json :: dataList[id=200168].name
   limit: do 40 znaków
   EN: Shooting Range
   PL: Shooting Range
474. [Muzyka i tekst utworu [200169 · wykonawca: ProjectMoon] — nazwa] En un lugar de La Mancha
   źródło: LobbyBGM.json :: dataList[id=200169].name
   limit: do 40 znaków
   EN: En un lugar de La Mancha
   PL: En un lugar de La Mancha
475. [Muzyka i tekst utworu [200170 · wykonawca: ProjectMoon] — nazwa] Haunted Mansion
   źródło: LobbyBGM.json :: dataList[id=200170].name
   limit: do 40 znaków
   EN: Haunted Mansion
   PL: Haunted Mansion
476. [Muzyka i tekst utworu [200171 · wykonawca: ProjectMoon] — nazwa] Confession
   źródło: LobbyBGM.json :: dataList[id=200171].name
   limit: do 40 znaków
   EN: Confession
   PL: Confession
477. [Muzyka i tekst utworu [200172 · wykonawca: ProjectMoon] — nazwa] Noble Ideal
   źródło: LobbyBGM.json :: dataList[id=200172].name
   limit: do 40 znaków
   EN: Noble Ideal
   PL: Noble Ideal
478. [Muzyka i tekst utworu [200173 · wykonawca: ProjectMoon] — nazwa] La Mancha Carnival (inst)
   źródło: LobbyBGM.json :: dataList[id=200173].name
   limit: do 40 znaków
   EN: La Mancha Carnival (inst)
   PL: La Mancha Carnival (inst)
479. [Muzyka i tekst utworu [200174 · wykonawca: ProjectMoon] — nazwa] La Mancha Carnival
   źródło: LobbyBGM.json :: dataList[id=200174].name
   limit: do 40 znaków
   EN: La Mancha Carnival
   PL: La Mancha Carnival
480. [Muzyka i tekst utworu [200175 · wykonawca: ProjectMoon] — nazwa] Abandoned
   źródło: LobbyBGM.json :: dataList[id=200175].name
   limit: do 40 znaków
   EN: Abandoned
   PL: Abandoned
481. [Muzyka i tekst utworu [200176 · wykonawca: ProjectMoon] — nazwa] Soy Quixote
   źródło: LobbyBGM.json :: dataList[id=200176].name
   limit: do 40 znaków
   EN: Soy Quixote
   PL: Soy Quixote
482. [Muzyka i tekst utworu [200177 · wykonawca: ProjectMoon] — nazwa] Una Estrella Alcanzar
   źródło: LobbyBGM.json :: dataList[id=200177].name
   limit: do 40 znaków
   EN: Una Estrella Alcanzar
   PL: Una Estrella Alcanzar
483. [Muzyka i tekst utworu [200178 · wykonawca: ProjectMoon] — nazwa] Sueño Imposible
   źródło: LobbyBGM.json :: dataList[id=200178].name
   limit: do 40 znaków
   EN: Sueño Imposible
   PL: Sueño Imposible
484. [Muzyka i tekst utworu [200179 · wykonawca: ProjectMoon] — nazwa] Opening Show
   źródło: LobbyBGM.json :: dataList[id=200179].name
   limit: do 40 znaków
   EN: Opening Show
   PL: Opening Show
485. [Muzyka i tekst utworu [200180 · wykonawca: ProjectMoon] — nazwa] Oblivion
   źródło: LobbyBGM.json :: dataList[id=200180].name
   limit: do 40 znaków
   EN: Oblivion
   PL: Oblivion
486. [Muzyka i tekst utworu [200181 · wykonawca: ProjectMoon] — nazwa] Where Your Dream Ends
   źródło: LobbyBGM.json :: dataList[id=200181].name
   limit: do 40 znaków
   EN: Where Your Dream Ends
   PL: Where Your Dream Ends
487. [Muzyka i tekst utworu [200182 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 01
   źródło: LobbyBGM.json :: dataList[id=200182].name
   limit: do 40 znaków
   EN: Canto VII Battle 01
   PL: Canto VII Battle 01
488. [Muzyka i tekst utworu [200183 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 02
   źródło: LobbyBGM.json :: dataList[id=200183].name
   limit: do 40 znaków
   EN: Canto VII Battle 02
   PL: Canto VII Battle 02
489. [Muzyka i tekst utworu [200184 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 03
   źródło: LobbyBGM.json :: dataList[id=200184].name
   limit: do 40 znaków
   EN: Canto VII Battle 03
   PL: Canto VII Battle 03
490. [Muzyka i tekst utworu [200185 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 04
   źródło: LobbyBGM.json :: dataList[id=200185].name
   limit: do 40 znaków
   EN: Canto VII Battle 04
   PL: Canto VII Battle 04
491. [Muzyka i tekst utworu [200186 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 05
   źródło: LobbyBGM.json :: dataList[id=200186].name
   limit: do 40 znaków
   EN: Canto VII Battle 05
   PL: Canto VII Battle 05
492. [Muzyka i tekst utworu [200187 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 06
   źródło: LobbyBGM.json :: dataList[id=200187].name
   limit: do 40 znaków
   EN: Canto VII Battle 06
   PL: Canto VII Battle 06
493. [Muzyka i tekst utworu [200188 · wykonawca: ProjectMoon] — nazwa] Canto VII Battle 07
   źródło: LobbyBGM.json :: dataList[id=200188].name
   limit: do 40 znaków
   EN: Canto VII Battle 07
   PL: Canto VII Battle 07
494. [Muzyka i tekst utworu [200189 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 08
   źródło: LobbyBGM.json :: dataList[id=200189].name
   limit: do 40 znaków
   EN: Canto VII Battle 08
   PL: Canto VII Battle 08
495. [Muzyka i tekst utworu [200190 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 09
   źródło: LobbyBGM.json :: dataList[id=200190].name
   limit: do 40 znaków
   EN: Canto VII Battle 09
   PL: Canto VII Battle 09
496. [Muzyka i tekst utworu [200191 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 10
   źródło: LobbyBGM.json :: dataList[id=200191].name
   limit: do 40 znaków
   EN: Canto VII Battle 10
   PL: Canto VII Battle 10
497. [Muzyka i tekst utworu [200192 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 11
   źródło: LobbyBGM.json :: dataList[id=200192].name
   limit: do 40 znaków
   EN: Canto VII Battle 11
   PL: Canto VII Battle 11
498. [Muzyka i tekst utworu [200193 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 12
   źródło: LobbyBGM.json :: dataList[id=200193].name
   limit: do 40 znaków
   EN: Canto VII Battle 12
   PL: Canto VII Battle 12
499. [Muzyka i tekst utworu [200194 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 13
   źródło: LobbyBGM.json :: dataList[id=200194].name
   limit: do 40 znaków
   EN: Canto VII Battle 13
   PL: Canto VII Battle 13
500. [Muzyka i tekst utworu [200195 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 14
   źródło: LobbyBGM.json :: dataList[id=200195].name
   limit: do 40 znaków
   EN: Canto VII Battle 14
   PL: Canto VII Battle 14
501. [Muzyka i tekst utworu [200196 · wykonawca: Studio EIM] — nazwa] Canto VII Battle 15
   źródło: LobbyBGM.json :: dataList[id=200196].name
   limit: do 40 znaków
   EN: Canto VII Battle 15
   PL: Canto VII Battle 15
502. [Muzyka i tekst utworu [200197 · wykonawca: ProjectMoon] — nazwa] Team Energy
   źródło: LobbyBGM.json :: dataList[id=200197].name
   limit: do 40 znaków
   EN: Team Energy
   PL: Team Energy
503. [Muzyka i tekst utworu [200198 · wykonawca: ProjectMoon] — nazwa] Who Will Remember
   źródło: LobbyBGM.json :: dataList[id=200198].name
   limit: do 40 znaków
   EN: Who Will Remember
   PL: Who Will Remember
504. [Muzyka i tekst utworu [200199 · wykonawca: ProjectMoon] — nazwa] Time To Clean
   źródło: LobbyBGM.json :: dataList[id=200199].name
   limit: do 40 znaków
   EN: Time To Clean
   PL: Time To Clean
505. [Muzyka i tekst utworu [200200 · wykonawca: ProjectMoon] — nazwa] Into Darkness
   źródło: LobbyBGM.json :: dataList[id=200200].name
   limit: do 40 znaków
   EN: Into Darkness
   PL: Into Darkness
506. [Muzyka i tekst utworu [200201 · wykonawca: ProjectMoon] — nazwa] Shadow Incoming
   źródło: LobbyBGM.json :: dataList[id=200201].name
   limit: do 40 znaków
   EN: Shadow Incoming
   PL: Shadow Incoming
507. [Muzyka i tekst utworu [200202 · wykonawca: ProjectMoon] — nazwa] LCB Regular Check-up Battle 01
   źródło: LobbyBGM.json :: dataList[id=200202].name
   limit: do 50 znaków
   EN: LCB Regular Check-up Battle 01
   PL: LCB Regular Check-up Battle 01
508. [Muzyka i tekst utworu [200203 · wykonawca: ProjectMoon] — nazwa] LCB Regular Check-up Battle 02
   źródło: LobbyBGM.json :: dataList[id=200203].name
   limit: do 50 znaków
   EN: LCB Regular Check-up Battle 02
   PL: LCB Regular Check-up Battle 02
509. [Muzyka i tekst utworu [200204 · wykonawca: ProjectMoon] — nazwa] LCB Regular Check-up Battle 03
   źródło: LobbyBGM.json :: dataList[id=200204].name
   limit: do 50 znaków
   EN: LCB Regular Check-up Battle 03
   PL: LCB Regular Check-up Battle 03
510. [Muzyka i tekst utworu [200205 · wykonawca: Studio EIM] — nazwa] Nocturnal Sweeping Battle 01
   źródło: LobbyBGM.json :: dataList[id=200205].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping Battle 01
   PL: Nocturnal Sweeping Battle 01
511. [Muzyka i tekst utworu [200206 · wykonawca: Studio EIM] — nazwa] Nocturnal Sweeping Battle 02
   źródło: LobbyBGM.json :: dataList[id=200206].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping Battle 02
   PL: Nocturnal Sweeping Battle 02
512. [Muzyka i tekst utworu [200207 · wykonawca: Studio EIM] — nazwa] Nocturnal Sweeping Battle 03
   źródło: LobbyBGM.json :: dataList[id=200207].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping Battle 03
   PL: Nocturnal Sweeping Battle 03
513. [Muzyka i tekst utworu [200208 · wykonawca: ProjectMoon] — nazwa] Me relinque
   źródło: LobbyBGM.json :: dataList[id=200208].name
   limit: do 40 znaków
   EN: Me relinque
   PL: Me relinque
514. [Muzyka i tekst utworu [200209 · wykonawca: ProjectMoon] — nazwa] Ne me relinque
   źródło: LobbyBGM.json :: dataList[id=200209].name
   limit: do 40 znaków
   EN: Ne me relinque
   PL: Ne me relinque
515. [Muzyka i tekst utworu [200210 · wykonawca: Mili] — nazwa] TIAN TIAN
   źródło: LobbyBGM.json :: dataList[id=200210].name
   limit: do 40 znaków
   EN: TIAN TIAN
   PL: TIAN TIAN
516. [Muzyka i tekst utworu [200211 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.홍루
   źródło: LobbyBGM.json :: dataList[id=200211].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Hong Lu
   PL: Sarajinae (Pass On) - ver. Hong Lu
517. [Muzyka i tekst utworu [200212 · wykonawca: ProjectMoon] — nazwa] City of Boluses
   źródło: LobbyBGM.json :: dataList[id=200212].name
   limit: do 40 znaków
   EN: City of Boluses
   PL: City of Boluses
518. [Muzyka i tekst utworu [200213 · wykonawca: ProjectMoon] — nazwa] First Step
   źródło: LobbyBGM.json :: dataList[id=200213].name
   limit: do 40 znaków
   EN: First Step
   PL: First Step
519. [Muzyka i tekst utworu [200214 · wykonawca: ProjectMoon] — nazwa] Relaxation
   źródło: LobbyBGM.json :: dataList[id=200214].name
   limit: do 40 znaków
   EN: Relaxation
   PL: Relaxation
520. [Muzyka i tekst utworu [200215 · wykonawca: ProjectMoon] — nazwa] Show Your Boldness
   źródło: LobbyBGM.json :: dataList[id=200215].name
   limit: do 40 znaków
   EN: Show Your Boldness
   PL: Show Your Boldness
521. [Muzyka i tekst utworu [200216 · wykonawca: ProjectMoon] — nazwa] Prove Your Brutality
   źródło: LobbyBGM.json :: dataList[id=200216].name
   limit: do 40 znaków
   EN: Prove Your Brutality
   PL: Prove Your Brutality
522. [Muzyka i tekst utworu [200217 · wykonawca: ProjectMoon] — nazwa] Brutality
   źródło: LobbyBGM.json :: dataList[id=200217].name
   limit: do 40 znaków
   EN: Brutality
   PL: Brutality
523. [Muzyka i tekst utworu [200218 · wykonawca: ProjectMoon] — nazwa] Best Day for You
   źródło: LobbyBGM.json :: dataList[id=200218].name
   limit: do 40 znaków
   EN: Best Day for You
   PL: Best Day for You
524. [Muzyka i tekst utworu [200219 · wykonawca: ProjectMoon] — nazwa] Peony
   źródło: LobbyBGM.json :: dataList[id=200219].name
   limit: do 40 znaków
   EN: Peony
   PL: Peony
525. [Muzyka i tekst utworu [200220 · wykonawca: ProjectMoon] — nazwa] Regret Not 01
   źródło: LobbyBGM.json :: dataList[id=200220].name
   limit: do 40 znaków
   EN: Regret Not 01
   PL: Regret Not 01
526. [Muzyka i tekst utworu [200221 · wykonawca: ProjectMoon] — nazwa] Regret Not 02
   źródło: LobbyBGM.json :: dataList[id=200221].name
   limit: do 40 znaków
   EN: Regret Not 02
   PL: Regret Not 02
527. [Muzyka i tekst utworu [200222 · wykonawca: ProjectMoon] — nazwa] Grand Party
   źródło: LobbyBGM.json :: dataList[id=200222].name
   limit: do 40 znaków
   EN: Grand Party
   PL: Grand Party
528. [Muzyka i tekst utworu [200223 · wykonawca: ProjectMoon] — nazwa] Golden Flower
   źródło: LobbyBGM.json :: dataList[id=200223].name
   limit: do 40 znaków
   EN: Golden Flower
   PL: Golden Flower
529. [Muzyka i tekst utworu [200224 · wykonawca: ProjectMoon] — nazwa] Zàng Huā Yín
   źródło: LobbyBGM.json :: dataList[id=200224].name
   limit: do 40 znaków
   EN: Zàng Huā Yín
   PL: Zàng Huā Yín
530. [Muzyka i tekst utworu [200225 · wykonawca: ProjectMoon] — nazwa] Remembrance 01
   źródło: LobbyBGM.json :: dataList[id=200225].name
   limit: do 40 znaków
   EN: Remembrance 01
   PL: Remembrance 01
531. [Muzyka i tekst utworu [200226 · wykonawca: ProjectMoon] — nazwa] Remembrance 02
   źródło: LobbyBGM.json :: dataList[id=200226].name
   limit: do 40 znaków
   EN: Remembrance 02
   PL: Remembrance 02
532. [Muzyka i tekst utworu [200227 · wykonawca: ProjectMoon] — nazwa] Prove It
   źródło: LobbyBGM.json :: dataList[id=200227].name
   limit: do 40 znaków
   EN: Prove It
   PL: Prove It
533. [Muzyka i tekst utworu [200228 · wykonawca: ProjectMoon] — nazwa] Remembrance 03
   źródło: LobbyBGM.json :: dataList[id=200228].name
   limit: do 40 znaków
   EN: Remembrance 03
   PL: Remembrance 03
534. [Muzyka i tekst utworu [200229 · wykonawca: ProjectMoon] — nazwa] Sè Jí Shì Kōng
   źródło: LobbyBGM.json :: dataList[id=200229].name
   limit: do 40 znaków
   EN: Sè Jí Shì Kōng
   PL: Sè Jí Shì Kōng
535. [Muzyka i tekst utworu [200230 · wykonawca: Studio EIM] — nazwa] Canto VIII Dungeon
   źródło: LobbyBGM.json :: dataList[id=200230].name
   limit: do 40 znaków
   EN: Canto VIII Dungeon
   PL: Canto VIII Dungeon
536. [Muzyka i tekst utworu [200231 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 01
   źródło: LobbyBGM.json :: dataList[id=200231].name
   limit: do 40 znaków
   EN: Canto VIII Battle 01
   PL: Canto VIII Battle 01
537. [Muzyka i tekst utworu [200232 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 02
   źródło: LobbyBGM.json :: dataList[id=200232].name
   limit: do 40 znaków
   EN: Canto VIII Battle 02
   PL: Canto VIII Battle 02
538. [Muzyka i tekst utworu [200233 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 03
   źródło: LobbyBGM.json :: dataList[id=200233].name
   limit: do 40 znaków
   EN: Canto VIII Battle 03
   PL: Canto VIII Battle 03
539. [Muzyka i tekst utworu [200234 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 04
   źródło: LobbyBGM.json :: dataList[id=200234].name
   limit: do 40 znaków
   EN: Canto VIII Battle 04
   PL: Canto VIII Battle 04
540. [Muzyka i tekst utworu [200235 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 05
   źródło: LobbyBGM.json :: dataList[id=200235].name
   limit: do 40 znaków
   EN: Canto VIII Battle 05
   PL: Canto VIII Battle 05
541. [Muzyka i tekst utworu [200236 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 06
   źródło: LobbyBGM.json :: dataList[id=200236].name
   limit: do 40 znaków
   EN: Canto VIII Battle 06
   PL: Canto VIII Battle 06
542. [Muzyka i tekst utworu [200237 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 07
   źródło: LobbyBGM.json :: dataList[id=200237].name
   limit: do 40 znaków
   EN: Canto VIII Battle 07
   PL: Canto VIII Battle 07
543. [Muzyka i tekst utworu [200238 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 08
   źródło: LobbyBGM.json :: dataList[id=200238].name
   limit: do 40 znaków
   EN: Canto VIII Battle 08
   PL: Canto VIII Battle 08
544. [Muzyka i tekst utworu [200239 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 09
   źródło: LobbyBGM.json :: dataList[id=200239].name
   limit: do 40 znaków
   EN: Canto VIII Battle 09
   PL: Canto VIII Battle 09
545. [Muzyka i tekst utworu [200240 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 10
   źródło: LobbyBGM.json :: dataList[id=200240].name
   limit: do 40 znaków
   EN: Canto VIII Battle 10
   PL: Canto VIII Battle 10
546. [Muzyka i tekst utworu [200241 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 11
   źródło: LobbyBGM.json :: dataList[id=200241].name
   limit: do 40 znaków
   EN: Canto VIII Battle 11
   PL: Canto VIII Battle 11
547. [Muzyka i tekst utworu [200242 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 12
   źródło: LobbyBGM.json :: dataList[id=200242].name
   limit: do 40 znaków
   EN: Canto VIII Battle 12
   PL: Canto VIII Battle 12
548. [Muzyka i tekst utworu [200243 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 13
   źródło: LobbyBGM.json :: dataList[id=200243].name
   limit: do 40 znaków
   EN: Canto VIII Battle 13
   PL: Canto VIII Battle 13
549. [Muzyka i tekst utworu [200244 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 14
   źródło: LobbyBGM.json :: dataList[id=200244].name
   limit: do 40 znaków
   EN: Canto VIII Battle 14
   PL: Canto VIII Battle 14
550. [Muzyka i tekst utworu [200245 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 15
   źródło: LobbyBGM.json :: dataList[id=200245].name
   limit: do 40 znaków
   EN: Canto VIII Battle 15
   PL: Canto VIII Battle 15
551. [Muzyka i tekst utworu [200246 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 16
   źródło: LobbyBGM.json :: dataList[id=200246].name
   limit: do 40 znaków
   EN: Canto VIII Battle 16
   PL: Canto VIII Battle 16
552. [Muzyka i tekst utworu [200247 · wykonawca: Studio EIM] — nazwa] Canto VIII Battle 17
   źródło: LobbyBGM.json :: dataList[id=200247].name
   limit: do 40 znaków
   EN: Canto VIII Battle 17
   PL: Canto VIII Battle 17
553. [Muzyka i tekst utworu [200248 · wykonawca: ProjectMoon] — nazwa] Long Live the Hierarch
   źródło: LobbyBGM.json :: dataList[id=200248].name
   limit: do 40 znaków
   EN: Long Live the Hierarch
   PL: Long Live the Hierarch
554. [Muzyka i tekst utworu [200249 · wykonawca: ProjectMoon] — nazwa] You Must Study
   źródło: LobbyBGM.json :: dataList[id=200249].name
   limit: do 40 znaków
   EN: You Must Study
   PL: You Must Study
555. [Muzyka i tekst utworu [200250 · wykonawca: ProjectMoon] — nazwa] You Must Train
   źródło: LobbyBGM.json :: dataList[id=200250].name
   limit: do 40 znaków
   EN: You Must Train
   PL: You Must Train
556. [Muzyka i tekst utworu [200251 · wykonawca: ProjectMoon] — nazwa] You Must Rest
   źródło: LobbyBGM.json :: dataList[id=200251].name
   limit: do 40 znaków
   EN: You Must Rest
   PL: You Must Rest
557. [Muzyka i tekst utworu [200252 · wykonawca: ProjectMoon] — nazwa] Spring Cultivation Battle 01
   źródło: LobbyBGM.json :: dataList[id=200252].name
   limit: do 40 znaków
   EN: Spring Cultivation Battle 01
   PL: Spring Cultivation Battle 01
558. [Muzyka i tekst utworu [200253 · wykonawca: Studio EIM] — nazwa] Spring Cultivation Battle 02
   źródło: LobbyBGM.json :: dataList[id=200253].name
   limit: do 40 znaków
   EN: Spring Cultivation Battle 02
   PL: Spring Cultivation Battle 02
559. [Muzyka i tekst utworu [200254 · wykonawca: Studio EIM] — nazwa] Spring Cultivation Battle 03
   źródło: LobbyBGM.json :: dataList[id=200254].name
   limit: do 40 znaków
   EN: Spring Cultivation Battle 03
   PL: Spring Cultivation Battle 03
560. [Muzyka i tekst utworu [200255 · wykonawca: Mili] — nazwa] SAIKAI
   źródło: LobbyBGM.json :: dataList[id=200255].name
   limit: do 40 znaków
   EN: SAIKAI
   PL: SAIKAI
561. [Muzyka i tekst utworu [200256 · wykonawca: Studio EIM] — nazwa] 사라지네 - ver.료슈
   źródło: LobbyBGM.json :: dataList[id=200256].name
   limit: do 50 znaków
   EN: Sarajinae (Pass On) - ver. Ryōshū
   PL: Sarajinae (Pass On) - ver. Ryōshū
562. [Muzyka i tekst utworu [200257 · wykonawca: ProjectMoon] — nazwa] They Were Here
   źródło: LobbyBGM.json :: dataList[id=200257].name
   limit: do 40 znaków
   EN: They Were Here
   PL: They Were Here
563. [Muzyka i tekst utworu [200258 · wykonawca: ProjectMoon] — nazwa] They Must Be Here
   źródło: LobbyBGM.json :: dataList[id=200258].name
   limit: do 40 znaków
   EN: They Must Be Here
   PL: They Must Be Here
564. [Muzyka i tekst utworu [200259 · wykonawca: ProjectMoon] — nazwa] Thumbs Down
   źródło: LobbyBGM.json :: dataList[id=200259].name
   limit: do 40 znaków
   EN: Thumbs Down
   PL: Thumbs Down
565. [Muzyka i tekst utworu [200260 · wykonawca: ProjectMoon] — nazwa] Call New Index
   źródło: LobbyBGM.json :: dataList[id=200260].name
   limit: do 40 znaków
   EN: Call New Index
   PL: Call New Index
566. [Muzyka i tekst utworu [200261 · wykonawca: ProjectMoon] — nazwa] Middle Finger Sanjou
   źródło: LobbyBGM.json :: dataList[id=200261].name
   limit: do 40 znaków
   EN: Middle Finger Sanjou
   PL: Middle Finger Sanjou
567. [Muzyka i tekst utworu [200262 · wykonawca: ProjectMoon] — nazwa] Cut Your Rings
   źródło: LobbyBGM.json :: dataList[id=200262].name
   limit: do 40 znaków
   EN: Cut Your Rings
   PL: Cut Your Rings
568. [Muzyka i tekst utworu [200263 · wykonawca: ProjectMoon] — nazwa] Sanzunokawa
   źródło: LobbyBGM.json :: dataList[id=200263].name
   limit: do 40 znaków
   EN: Sanzunokawa
   PL: Sanzunokawa
569. [Muzyka i tekst utworu [200264 · wykonawca: ProjectMoon] — nazwa] Good Old Day
   źródło: LobbyBGM.json :: dataList[id=200264].name
   limit: do 40 znaków
   EN: Good Old Day
   PL: Good Old Day
570. [Muzyka i tekst utworu [200265 · wykonawca: ProjectMoon] — nazwa] And Day Passes
   źródło: LobbyBGM.json :: dataList[id=200265].name
   limit: do 40 znaków
   EN: And Day Passes
   PL: And Day Passes
571. [Muzyka i tekst utworu [200266 · wykonawca: ProjectMoon] — nazwa] City Hero
   źródło: LobbyBGM.json :: dataList[id=200266].name
   limit: do 40 znaków
   EN: City Hero
   PL: City Hero
572. [Muzyka i tekst utworu [200267 · wykonawca: ProjectMoon] — nazwa] Yumenomaichiru
   źródło: LobbyBGM.json :: dataList[id=200267].name
   limit: do 40 znaków
   EN: Yumenomaichiru
   PL: Yumenomaichiru
573. [Muzyka i tekst utworu [200268 · wykonawca: ProjectMoon] — nazwa] Alert - Alpha
   źródło: LobbyBGM.json :: dataList[id=200268].name
   limit: do 40 znaków
   EN: Alert - Alpha
   PL: Alert - Alpha
574. [Muzyka i tekst utworu [200269 · wykonawca: ProjectMoon] — nazwa] Alert - Beta
   źródło: LobbyBGM.json :: dataList[id=200269].name
   limit: do 40 znaków
   EN: Alert - Beta
   PL: Alert - Beta
575. [Muzyka i tekst utworu [200270 · wykonawca: ProjectMoon] — nazwa] Kumo no Ito
   źródło: LobbyBGM.json :: dataList[id=200270].name
   limit: do 40 znaków
   EN: Kumo no Ito
   PL: Kumo no Ito
576. [Muzyka i tekst utworu [200271 · wykonawca: ProjectMoon] — nazwa] Aka no Ito
   źródło: LobbyBGM.json :: dataList[id=200271].name
   limit: do 40 znaków
   EN: Aka no Ito
   PL: Aka no Ito
577. [Muzyka i tekst utworu [200272 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 01
   źródło: LobbyBGM.json :: dataList[id=200272].name
   limit: do 40 znaków
   EN: Canto IX Battle 01
   PL: Canto IX Battle 01
578. [Muzyka i tekst utworu [200273 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 02
   źródło: LobbyBGM.json :: dataList[id=200273].name
   limit: do 40 znaków
   EN: Canto IX Battle 02
   PL: Canto IX Battle 02
579. [Muzyka i tekst utworu [200274 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 03
   źródło: LobbyBGM.json :: dataList[id=200274].name
   limit: do 40 znaków
   EN: Canto IX Battle 03
   PL: Canto IX Battle 03
580. [Muzyka i tekst utworu [200275 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 04
   źródło: LobbyBGM.json :: dataList[id=200275].name
   limit: do 40 znaków
   EN: Canto IX Battle 04
   PL: Canto IX Battle 04
581. [Muzyka i tekst utworu [200276 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 05
   źródło: LobbyBGM.json :: dataList[id=200276].name
   limit: do 40 znaków
   EN: Canto IX Battle 05
   PL: Canto IX Battle 05
582. [Muzyka i tekst utworu [200277 · wykonawca: Studio EIM] — nazwa] Canto IX Battle 06
   źródło: LobbyBGM.json :: dataList[id=200277].name
   limit: do 40 znaków
   EN: Canto IX Battle 06
   PL: Canto IX Battle 06
