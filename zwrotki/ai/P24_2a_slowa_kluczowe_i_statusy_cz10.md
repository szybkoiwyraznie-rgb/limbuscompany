# Paczka AI P24 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 10/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P24_2a_slowa_kluczowe_i_statusy_cz10.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P24_2a_slowa_kluczowe_i_statusy_cz10.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs-a1c9p1
- plik gry: `Bufs-a1c9p1.json`

1. [Status [SeveredTendon] — opis] - 최댓값 3\n- 수치 1당 기본 공격 스킬의 기본 위력 -1\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c9p1.json :: dataList[id=SeveredTendon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Base Attack Skill Base Power -1 for every Stack\n- Turn End: Lose 1 Stack
   PL: - Maks. 3 stosów\n- Podstawowa Siła podstawowej Umiejętności ataku -1 za każdy stos\n- Na koniec tury traci 1 stos
2. [Status [HowDareYouApple] — nazwa] 감히…!
   źródło: Bufs-a1c9p1.json :: dataList[id=HowDareYouApple].name
   kontekst: identyfikator statusu w tekstach: `[HowDareYouApple]`
   limit: do 40 znaków
   EN: The Audacity...!
   PL: Zuchwałość...!
3. [Status [HowDareYouApple] — opis] - 최댓값: 4\n- 수치당 피해량 +20%\n- 특정 스킬 사용시 소모됨
   źródło: Bufs-a1c9p1.json :: dataList[id=HowDareYouApple].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Deal +20% damage for every Stack\n- Consumed when using certain Skills
   PL: - Maks. stosów: 4\n- Zadaje +20% obrażeń za każdy stos\n- Zużywane przy użyciu określonych Umiejętności
4. [Status [RapidGrowthApple] — nazwa] 급한 성장
   źródło: Bufs-a1c9p1.json :: dataList[id=RapidGrowthApple].name
   kontekst: identyfikator statusu w tekstach: `[RapidGrowthApple]`
   limit: do 40 znaków
   EN: Rapid Growth
   PL: Przyspieszony Wzrost
5. [Status [RapidGrowthApple] — opis] - 최댓값: 3\n- 수치당 부위의 방어 레벨 1 감소 (최소 방어 레벨 1)\n- 팔 부위 전부 파괴 시 소멸
   źródło: Bufs-a1c9p1.json :: dataList[id=RapidGrowthApple].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Lose 1 Defense Level for every Stack; minimum Defense Level due to this effect: 1\n- Lose this effect when all Arms are broken
   PL: - Maks. stosów: 3\n- Poziom Obrony części maleje o 1 za każdy stos (min. Poziom Obrony 1)\n- Znika po zniszczeniu wszystkich części Ramion
6. [Status [HumanFleshTheRings] — nazwa] 생체 재료
   źródło: Bufs-a1c9p1.json :: dataList[id=HumanFleshTheRings].name
   kontekst: identyfikator statusu w tekstach: `[HumanFleshTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient
   PL: Materiał Biologiczny
7. [Status [HumanFleshTheRings] — opis] - 최댓값: 2\n- 특수 충전 (위력 고정)
   źródło: Bufs-a1c9p1.json :: dataList[id=HumanFleshTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 2\n- Specjalny Ładunek (Siła zablokowana)
8. [Status [BoneBladeTheRings] — nazwa] 작품명: 파시아
   źródło: Bufs-a1c9p1.json :: dataList[id=BoneBladeTheRings].name
   kontekst: identyfikator statusu w tekstach: `[BoneBladeTheRings]`
   limit: do 40 znaków
   EN: Artwork: Fascia
   PL: Dzieło: Fascia
9. [Status [BoneBladeTheRings] — opis] - 턴 시작 시, 기본 위력 증가 4 얻음\n- 공격 스킬로 출혈 부여 시, 출혈 위력 2 추가 부여
   źródło: Bufs-a1c9p1.json :: dataList[id=BoneBladeTheRings].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Base Power Up\n- When inflicting Bleed with Attack Skills, inflict additional 2 Bleed Potency
   PL: - Na początku tury zyskuje 4 Wzrostu Mocy Bazowej\n- Nakładając Krwawienie Umiejętnościami ataku, nakłada dodatkowo 2 Siły Krwawienia
10. [Status [UnsteadyTheRings] — nazwa] 심하게 울리는 갑주
   źródło: Bufs-a1c9p1.json :: dataList[id=UnsteadyTheRings].name
   kontekst: identyfikator statusu w tekstach: `[UnsteadyTheRings]`
   limit: do 40 znaków
   EN: Impact-rattled Armor
   PL: Rozkołysana Zbroja
11. [Status [UnsteadyTheRings] — opis] - 최댓값: 3\n- ‘억압당한 육체’ 사용 시 수치 1당, 최종 위력 10 감소\n- ‘억압당한 육체’ 공격 종료 후 수치가 3이면, 효과 소멸하고 다음 턴까지 흐트러짐 상태가 됨
   źródło: Bufs-a1c9p1.json :: dataList[id=UnsteadyTheRings].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When using 'Repressed Flesh', lose 10 Final Power for every Stack\n- At 3 Stacks after using 'Repressed Flesh', lose this effect and become Staggered until next turn
   PL: - Maks. stosów: 3\n- Przy użyciu „Uciskanego Ciała” traci 10 Mocy Końcowej za każdy stos\n- Jeżeli po zakończeniu ataku „Uciskanego Ciała” wartość wynosi 3, efekt znika, a jednostka pozostaje w stanie Oszołomienia do następnej tury
12. [Status [IronMaiden_LowMorale] — nazwa] 아이언 메이든
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[IronMaiden_LowMorale]`
   limit: do 40 znaków
   EN: Iron Maiden
   PL: Iron Maiden
13. [Status [IronMaiden_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 감소 1, 방어 레벨 증가 1 얻음
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down and 1 Defense Level Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Spadek Poziomu Ataku i 1 Wzrost Poziomu Obrony
14. [Status [IronMaiden_LowMorale] — podsumowanie] 턴 시작 시, 공격 레벨 감소 1, 방어 레벨 증가 1 얻음
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].summary
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Offense Level Down and 1 Defense Level Up
   PL: Na początku tury zyskuje 1 Spadek Poziomu Ataku i 1 Wzrost Poziomu Obrony
15. [Status [IronMaiden_Panic] — nazwa] 아이언 메이든
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_Panic].name
   kontekst: identyfikator statusu w tekstach: `[IronMaiden_Panic]`
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
16. [Status [IronMaiden_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 감소 2, 방어 레벨 증가 2 얻음
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Offense Level Down and 2 Defense Level Up
   PL: - Panika\n- Na początku tury zyskuje 2 Spadku Poziomu Ataku i 2 Wzrost Poziomu Obrony
17. [Status [IronMaiden_Panic] — podsumowanie] 턴 시작 시, 공격 레벨 감소 2, 방어 레벨 증가 2 얻음
   źródło: Bufs-a1c9p1.json :: dataList[id=IronMaiden_Panic].summary
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Offense Level Down and 2 Defense Level Up
   PL: Na początku tury zyskuje 2 Spadku Poziomu Ataku i 2 Wzrost Poziomu Obrony
18. [Status [DicipleLittleFinger] — nazwa] 월하청도
   źródło: Bufs-a1c9p1.json :: dataList[id=DicipleLittleFinger].name
   kontekst: identyfikator statusu w tekstach: `[DicipleLittleFinger]`
   limit: do 40 znaków
   EN: Moonlit Azure Blade
   PL: Błękitne Ostrze w Blasku Księżyca
19. [Status [DicipleLittleFinger] — opis] - 최댓값 : 50\n- 턴 시작시 수치 1당 보호막 5 얻음\n- 수치 1당 자신의 크리티컬 피해량 +1%\n- 피격 시 수치 1 감소
   źródło: Bufs-a1c9p1.json :: dataList[id=DicipleLittleFinger].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Turn Start: Gain 5 Shield for every Stack\n- +1% Damage on Critical Hit for every Stack\n- Lose 1 Stack when hit
   PL: - Maks. stosów: 50\n- Na początku tury zyskuje 5 Tarczy za każdy stos\n- +1% obrażeń Krytycznych za każdy stos\n- Przy trafieniu traci 1 stos
20. [Status [RyoshuSlotPlusA1C9] — nazwa] 과거의 악취
   źródło: Bufs-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuSlotPlusA1C9]`
   limit: do 40 znaków
   EN: Stench of Times Past
   PL: Smród Przeszłości
21. [Status [RyoshuSlotPlusA1C9] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)\n- 퇴각 불가능
   źródło: Bufs-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)\n- Wycofanie niemożliwe
22. [Status [RyoshuSlotPlusA1C9] — podsumowanie] 거미집 소속 적에게 가하는 피해량 증가
   źródło: Bufs-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].summary
   limit: do 120 znaków
   EN: Deal more damage to The House of Spiders enemies
   PL: Zadaje więcej obrażeń wrogom z Domu Pajęczyn
23. [Status [ObservationMoses] — nazwa] 관찰력
   źródło: Bufs-a1c9p1.json :: dataList[id=ObservationMoses].name
   kontekst: identyfikator statusu w tekstach: `[ObservationMoses]`
   limit: do 40 znaków
   EN: Keen Observation
   PL: Spostrzegawczość
24. [Status [ObservationMoses] — opis] - 매혹 대상이 되지 않음\n- 요정 부위에 가하는 피해량 +25%
   źródło: Bufs-a1c9p1.json :: dataList[id=ObservationMoses].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot be targeted for Charmed\n- Deal +25% damage to Fairy
   PL: - Nie może być celem Zauroczenia\n- Zadaje +25% obrażeń Wróżce
25. [Status [CalmAnalysisMoses] — nazwa] 차분한 분석
   źródło: Bufs-a1c9p1.json :: dataList[id=CalmAnalysisMoses].name
   kontekst: identyfikator statusu w tekstach: `[CalmAnalysisMoses]`
   limit: do 40 znaków
   EN: Untroubled Analysis
   PL: Spokojna Analiza
26. [Status [CalmAnalysisMoses] — opis] - 요정 초롱에게 가하는 피해량 +25%
   źródło: Bufs-a1c9p1.json :: dataList[id=CalmAnalysisMoses].desc
   limit: do 120 znaków
   EN: - Deal +25% damage to Faelantern
   PL: - Zadaje +25% obrażeń Faelantern
27. [Status [TeachersCommand] — nazwa] 엄지 아비의 명령
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersCommand].name
   kontekst: identyfikator statusu w tekstach: `[TeachersCommand]`
   limit: do 50 znaków
   EN: The Thumb Nursefather's Command
   PL: Rozkaz Ojca Kciuka
28. [Status [TeachersCommand] — opis] - 공격 레벨 5 감소
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersCommand].desc
   limit: do 120 znaków
   EN: - Lose 5 Offense Levels
   PL: - Traci 5 Poziomów Ataku
29. [Status [TeachersPet_LowMorale] — nazwa] 교본
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersPet_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[TeachersPet_LowMorale]`
   limit: do 40 znaków
   EN: Textbook
   PL: Podręcznik
30. [Status [TeachersPet_LowMorale] — opis] - 결투 고조를 보유한 적과 합 진행 시 합 위력 +1\n- 합 패배 시 다음 턴 취약 1 얻음 (턴당 1회)
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersPet_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power +1 when Clashing against targets with The Duel Escalates\n- Clash Lose: Gain 1 Fragile next turn (once per turn)
   PL: - Moc Starcia +1 w Starciu z celami posiadającymi Eskalację Pojedynku\n- Przegrana w Starciu: 1 Wrażliwości w następnej turze (raz na turę)
31. [Status [TeachersPet_Panic] — nazwa] 교본
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersPet_Panic].name
   kontekst: identyfikator statusu w tekstach: `[TeachersPet_Panic]`
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Status [TeachersPet_Panic] — opis] - 결투 고조를 보유한 적과 합 진행 시 합 위력 +2\n- 합 패배 시 다음 턴 취약 1 얻음 (턴당 1회)
   źródło: Bufs-a1c9p1.json :: dataList[id=TeachersPet_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power +2 when Clashing against targets with The Duel Escalates\n- Clash Lose: Gain 1 Fragile next turn (once per turn)
   PL: - Moc Starcia +2 w Starciu z celami posiadającymi Eskalację Pojedynku\n- Przegrana w Starciu: 1 Wrażliwości w następnej turze (raz na turę)
33. [Status [RyoshuStartA1C9] — nazwa] 되살아나는 희열
   źródło: Bufs-a1c9p1.json :: dataList[id=RyoshuStartA1C9].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuStartA1C9]`
   limit: do 40 znaków
   EN: Rekindled Exhilaration
   PL: Odrodzona Euforia
34. [Status [RyoshuStartA1C9] — opis] - 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)
   źródło: Bufs-a1c9p1.json :: dataList[id=RyoshuStartA1C9].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)
   PL: - Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)
35. [Status [BreathLoss_LowMorale] — nazwa] 흐트러진 숨
   źródło: Bufs-a1c9p1.json :: dataList[id=BreathLoss_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BreathLoss_LowMorale]`
   limit: do 40 znaków
   EN: Ragged Breath
   PL: Urywany Oddech
36. [Status [BreathLoss_LowMorale] — opis] 턴 시작시 자신의 호흡 위력 3 감소
   źródło: Bufs-a1c9p1.json :: dataList[id=BreathLoss_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 3 Poise Potency
   PL: Na początku tury traci 3 Siły Oddechu
37. [Status [BreathLoss_Panic] — nazwa] 흐트러진 숨
   źródło: Bufs-a1c9p1.json :: dataList[id=BreathLoss_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BreathLoss_Panic]`
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Status [BreathLoss_Panic] — opis] 턴 시작시 자신의 호흡 위력 5 감소
   źródło: Bufs-a1c9p1.json :: dataList[id=BreathLoss_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 5 Poise Potency
   PL: Na początku tury traci 5 Siły Oddechu
39. [Status [IndexPrescriptTargetMarkToEnemy] — nazwa] 지령 표식
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptTargetMarkToEnemy].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptTargetMarkToEnemy]`
   limit: do 40 znaków
   EN: Mark of the Prescript
   PL: Znak Nakazu
40. [Status [IndexPrescriptTargetMarkToEnemy] — opis] - 조작 슬롯에 배치된 기본 공격 스킬 중 하나에 지령 표식이 새겨짐
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptTargetMarkToEnemy].desc
   limit: do 120 znaków
   EN: - Apply Mark of the Prescript to a Base Attack Skill on this unit's Dashboard
   PL: - Nakłada Znak Nakazu na jedną podstawową Umiejętność ataku na Panelu dowodzenia tej jednostki
41. [Status [IndexPrescriptTargetToEnemy] — nazwa] 지령 대상
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptTargetToEnemy].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptTargetToEnemy]`
   limit: do 40 znaków
   EN: The Prescript's Target
   PL: Cel Nakazu
42. [Status [IndexPrescriptTargetToEnemy] — opis] - 검지 소속에게 받는 피해 +10%\n- 검지 소속 인격 수와 상관없이 매 턴마다 하나의 대상에게만 적용됨
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptTargetToEnemy].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from The Index units\n- This effect is applied to a single target every turn regardless of the number of The Index units deployed
   PL: - Otrzymuje +10% obrażeń od jednostek Wskazującego\n- Niezależnie od liczby Tożsamości Wskazującego efekt nakładany jest co turę tylko na jeden cel
43. [Status [BlessingOfIndexPrescriptAlly] — nazwa] 지령의 가호
   źródło: Bufs-a1c9p1.json :: dataList[id=BlessingOfIndexPrescriptAlly].name
   kontekst: identyfikator statusu w tekstach: `[BlessingOfIndexPrescriptAlly]`
   limit: do 40 znaków
   EN: Grace of the Prescript
   PL: Łaska Nakazu
44. [Status [BlessingOfIndexPrescriptAlly] — opis] - 수치 3당 공격 레벨 +1\n- 최대 9
   źródło: Bufs-a1c9p1.json :: dataList[id=BlessingOfIndexPrescriptAlly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1 for every 3 Stacks\n- Max Stack: 9
   PL: - Poziom Ataku +1 za każde 3 stosy\n- Maks. 9
45. [Status [IndexPrescript_Base] — nazwa] 지령
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescript_Base].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescript_Base]`
   limit: do 40 znaków
   EN: Prescript
   PL: Nakaz
46. [Status [IndexPrescript_Base] — opis] - 특정 조건에 따라 지령[쪽지]가 주어짐
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescript_Base].desc
   limit: do 120 znaków
   EN: - Receive 'Prescript: [Paper Slip]' under specific conditions
   PL: - Zgodnie z określonymi warunkami otrzymuje Nakaz [Kartka]
47. [Status [IndexPrescript_Base] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescript_Base].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy przekazywane są na rozmaite sposoby. Forma, w jakiej dotrą do adresata, zostaje wybrana jednokierunkowo, niczym wyrocznia — bez jego wpływu.
48. [Status [IndexPrescriptFaust_0] — nazwa] 지령[쪽지] I
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptFaust_0]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] I
   PL: Nakaz [Kartka] I
49. [Status [IndexPrescriptFaust_0] — opis] 지령 표식이 새겨진 스킬을 사용하거나 적중한다.\n\n- 턴 시작 시 지령의 가호가 0~2일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a Skill marked with Mark of the Prescript or hit a target with a marked Skill.\n\n- Turn Start: At 0~2 Grace of the Prescript, gain this effect \n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Używa Umiejętności oznaczonej Znakiem Nakazu lub trafia nią cel.\n\n- Na początku tury zdobywany przy Łasce Nakazu 0–2\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
50. [Status [IndexPrescriptFaust_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Status [IndexPrescriptFaust_1] — nazwa] 지령[쪽지] II
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptFaust_1]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] II
   PL: Nakaz [Kartka] II
52. [Status [IndexPrescriptFaust_1] — opis] 지령 표식이 새겨진 스킬이 적중한다.\n\n- 턴 시작 시 지령의 가호가 3~5일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with a Skill marked with Mark of the Prescript.\n\n- Turn Start: At 3~5 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Umiejętność oznaczona Znakiem Nakazu trafia cel.\n\n- Na początku tury zdobywany przy Łasce Nakazu 3–5\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
53. [Status [IndexPrescriptFaust_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [Status [IndexPrescriptFaust_2] — nazwa] 지령[쪽지] III
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptFaust_2]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] III
   PL: Nakaz [Kartka] III
55. [Status [IndexPrescriptFaust_2] — opis] E.G.O 각성 스킬 또는 지령 표식이 새겨진 ‘스킬 3’이 적중한다.\n\n- 턴 시작 시 지령의 가호가 6~8일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with E.G.O Awakening Skill or 'Skill 3' marked with Mark of the Prescript.\n\n- Turn Start: At 6~8 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Trafia cel Umiejętność Przebudzenia E.G.O lub „Umiejętność 3” oznaczona Znakiem Nakazu.\n\n- Na początku tury zdobywany przy Łasce Nakazu 6–8\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
56. [Status [IndexPrescriptFaust_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Status [IndexPrescriptFaust_3] — nazwa] 지령[쪽지] IV
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptFaust_3]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] IV
   PL: Nakaz [Kartka] IV
58. [Status [IndexPrescriptFaust_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 지령의 가호가 9일 때 얻음
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: At 9 Grace of the Prescript, gain this effect
   PL: Zabija wszystkich wrogów, zanim nadejdzie kolejny Nakaz.\n\n- Na początku tury, przy 9 Łaskach Nakazu
59. [Status [IndexPrescriptFaust_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Status [KarmaOfIndexAlly] — nazwa] 카르마
   źródło: Bufs-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].name
   kontekst: identyfikator statusu w tekstach: `[KarmaOfIndexAlly]`
   limit: do 40 znaków
   EN: Karmic Consequence
   PL: Karma
61. [Status [KarmaOfIndexAlly] — opis] - 턴 시작 시,\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: Bufs-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury,\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Maks. 100 stosów
62. [Status [KarmaOfIndexAlly] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: Bufs-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].flavor
   limit: do 200 znaków
   EN: Receive the Prescript and undertake it. Its execution is etched as karma, drawn into a ceaseless cycle that circles back to the hand of its executor.
   PL: Przyjmuje Nakaz i wypełnia go. Wypełnienie staje się karmą, która — krążąc bez końca — nawarstwia się znowu.

## Statusy i efekty bojowe — Bufs-a1c9p2
- plik gry: `Bufs-a1c9p2.json`

63. [Status [IndexPrescriptTargetToPersonality] — nazwa] 검지의 지령 대상
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptTargetToPersonality].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptTargetToPersonality]`
   limit: do 50 znaków
   EN: The Prescript's Target - The Index
   PL: Cel Nakazu - Wskazujący
64. [Status [IndexPrescriptTargetToPersonality] — opis] 검지 소속 적에게 사용하는 스킬 위력 -2, 받는 피해량 +20%
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptTargetToPersonality].desc
   limit: do 120 znaków
   EN: Skill Power -2 against and take +20% damage from The Index enemies
   PL: Siła Umiejętności -2 i otrzymuje +20% obrażeń od wrogów Wskazującego
65. [Status [BlessingOfIndexPrescriptEnemy] — nazwa] 지령의 가호
   źródło: Bufs-a1c9p2.json :: dataList[id=BlessingOfIndexPrescriptEnemy].name
   kontekst: identyfikator statusu w tekstach: `[BlessingOfIndexPrescriptEnemy]`
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Status [BlessingOfIndexPrescriptEnemy] — opis] - 수치 3당 공격 레벨 +1\n- 최대 9
   źródło: Bufs-a1c9p2.json :: dataList[id=BlessingOfIndexPrescriptEnemy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1 for every 3 Stack\n- Max Stack: 9
   PL: - Poziom Ataku +1 za każde 3 stosy\n- Maks. 9
67. [Status [IndexPrescript_Base_2nd] — nazwa] 지령
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescript_Base_2nd]`
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Status [IndexPrescript_Base_2nd] — opis] 특정 조건에 따라 지령[단말기]가 주어짐
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].desc
   limit: do 120 znaków
   EN: Receive Prescript: [Device] under specific conditions
   PL: Zgodnie z określonymi warunkami otrzymuje Nakaz [Urządzenie]
69. [Status [IndexPrescript_Base_2nd] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Status [IndexPrescriptStudent_0] — nazwa] 지령[단말기] I
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptStudent_0]`
   limit: do 40 znaków
   EN: Prescript: [Device] I
   PL: Nakaz [Urządzenie] I
71. [Status [IndexPrescriptStudent_0] — opis] 지령 대상을 공격하여 적중한다.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Cel Nakazu i trafia.\n\n- Na początku tury zdobywany przy braku Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
72. [Status [IndexPrescriptStudent_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [Status [IndexPrescriptStudent_1] — nazwa] 지령[단말기] II
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptStudent_1]`
   limit: do 40 znaków
   EN: Prescript: [Device] II
   PL: Nakaz [Urządzenie] II
74. [Status [IndexPrescriptStudent_1] — opis] 지령 대상에게 첫 번째 슬롯에 장착된 스킬이 적중한다. 또는 무작위 상대를 처치한다.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a Prescript's Target with the Skill equipped in the first Slot, or eliminate a random target.\n\n- Turn Start: Gain this effect if this unit has Unlock - I\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Cel Nakazu trafiają Umiejętność z pierwszego slotu lub losowy cel zostaje zabity.\n\n- Na początku tury zdobywany przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
75. [Status [IndexPrescriptStudent_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Status [IndexPrescriptStudent_2] — nazwa] 지령[단말기] III
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptStudent_2]`
   limit: do 40 znaków
   EN: Prescript: [Device] III
   PL: Nakaz [Urządzenie] III
77. [Status [IndexPrescriptStudent_2] — opis] 무작위 상대를 흐트러뜨리거나 처치한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stagger or eliminate a random target.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Oszłamia lub zabija losowy cel.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
78. [Status [IndexPrescriptStudent_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Status [IndexPrescriptStudent_3] — nazwa] 지령[단말기] IV
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptStudent_3]`
   limit: do 40 znaków
   EN: Prescript: [Device] IV
   PL: Nakaz [Urządzenie] IV
80. [Status [IndexPrescriptStudent_3] — opis] 모든 방해물을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all obstacles before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Wyeliminuj wszystkie przeszkody, zanim przyjdzie kolejny Nakaz.\n\n- Na początku tury zdobywany przy Odblokowaniu - III
81. [Status [IndexPrescriptStudent_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Status [UnlockBuff_1] — nazwa] 해금 - I
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_1].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_1]`
   limit: do 40 znaków
   EN: Unlock - I
   PL: Odblokowanie - I
83. [Status [UnlockBuff_1] — opis] - 공격 레벨 +1, 방어 레벨 +1\n- 전투 종료 시, 정신력 15 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1, Defense Level +1\n- Combat End: Heal 15 SP
   PL: - Poziom Ataku +1, Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 15 Poczytalności
84. [Status [UnlockBuff_2] — nazwa] 해금 - II
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_2].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_2]`
   limit: do 40 znaków
   EN: Unlock - II
   PL: Odblokowanie - II
85. [Status [UnlockBuff_2] — opis] - 공격 레벨 +2, 방어 레벨 +2\n- 전투 종료 시, 정신력 30 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2, Defense Level +2\n- Combat End: Heal 30 SP
   PL: - Poziom Ataku +2, Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 30 Poczytalności
86. [Status [UnlockBuff_3] — nazwa] 해금 - III
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_3].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_3]`
   limit: do 40 znaków
   EN: Unlock - III
   PL: Odblokowanie - III
87. [Status [UnlockBuff_3] — opis] - 공격 레벨 +3, 방어 레벨 +3\n- 전투 종료 시, 정신력 45 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3, Defense Level +3\n- Combat End: Heal 45 SP
   PL: - Poziom Ataku +3, Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 45 Poczytalności
88. [Status [KarmaOfIndexStudent] — nazwa] 카르마
   źródło: Bufs-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].name
   kontekst: identyfikator statusu w tekstach: `[KarmaOfIndexStudent]`
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Status [KarmaOfIndexStudent] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: Bufs-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury:\n· 1 Spadek Poziomu Obrony za każde 10 stosów\n· 1 Wrażliwość za każde 20 stosów\n- Maks. stosów: 100
90. [Status [KarmaOfIndexStudent] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: Bufs-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].flavor
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Status [Blandishment_Enemy] — nazwa] 당연한 믿음
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Enemy].name
   kontekst: identyfikator statusu w tekstach: `[Blandishment_Enemy]`
   limit: do 40 znaków
   EN: Faith Beyond Question
   PL: Wiara Ponad Wątpliwość
92. [Status [Blandishment_Enemy] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +3, 방어 레벨 +3\n- 스킬로 획득하는 호흡 위력 +1
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Enemy].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +3, Defense Level +3\n- Gain +1 more Poise Potency from Skills
   PL: - Min. i Maks. Szybkość +1\n- Poziom Ataku +3, Poziom Obrony +3\n- Umiejętności zyskują +1 więcej Siły Oddechu
93. [Status [Blandishment_Enemy] — tekst klimatyczny] “다, 당연한 것 아닌가요? 삐삐가 전해주는 말들은 당연히… 다, 당연한 거잖아요?”
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Enemy].flavor
   limit: do 140 znaków
   EN: "Isn't... Isn't it self-evident? Each word that the beeper grants is unquestionably... b-beyond question."
   PL: „Cz-czy to nie oczywiste? Każde słowo, które przynosi beeper, jest bezdyskusyjnie... b-bez dyskusji.”
94. [Status [Blandishment_Shin_Enemy] — nazwa] 신(心) - 소라
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Shin_Enemy].name
   kontekst: identyfikator statusu w tekstach: `[Blandishment_Shin_Enemy]`
   limit: do 40 znaków
   EN: Shin (心) - Sora
   PL: Shin (心) - Sora
95. [Status [Blandishment_Shin_Enemy] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +2, 방어 레벨 +2\n- 스킬로 획득하는 호흡 위력과 횟수 +1\n- 가하는 피해량 +(25+잃은 체력 비율)% (최대 100%)
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Shin_Enemy].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +2, Defense Level +2\n- Gain +1 more Poise Potency and Poise Count from Skills\n- Deal +(missing HP percentage + 25)% damage (max 100%)
   PL: - Minimalna i maksymalna Szybkość +1\n- Poziom Ataku +2, Poziom Obrony +2\n- Zyskiwana z Umiejętności Moc Oddechu i Licznik Oddechu +1\n- Zadawane Obrażenia +(25+procent utraconego HP)% (maks. 100%)
96. [Status [PressureOfPrescript] — nazwa] 압박감
   źródło: Bufs-a1c9p2.json :: dataList[id=PressureOfPrescript].name
   kontekst: identyfikator statusu w tekstach: `[PressureOfPrescript]`
   limit: do 40 znaków
   EN: Onus
   PL: Nacisk
97. [Status [PressureOfPrescript] — opis] - 수치 1당 가하는 피해량 +25% (최대 50%)\n- 개화 E.G.O::대행 상태면,\n· 수치가 1일 때, 최종 위력 +1\n· 수치가 2일 때, 대신 최종 위력 +3\n- 최대 2
   źródło: Bufs-a1c9p2.json :: dataList[id=PressureOfPrescript].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +25% damage for every Stack (max 50%)\n- Under Effloresced E.G.O::Procuration state:\n· At 1 Stack, Final Power +1\n· At 2 Stack, Final Power +3 instead\n- Max Stack: 2
   PL: - Zadaje +25% obrażeń za każdy stos (maks. 50%)\n- W stanie Rozkwitu E.G.O::Procuration,\n· Przy 1 stosie Moc Końcowa +1\n· Przy 2 stosach zamiast tego Moc Końcowa +3\n- Maks. 2
98. [Status [PressureOfPrescript] — tekst klimatyczny] ‘어,어떡하지. 당연한 건 당연히 수행되어야만 하는데….’
   źródło: Bufs-a1c9p2.json :: dataList[id=PressureOfPrescript].flavor
   limit: do 120 znaków
   EN: 'W-what should I do? What is unquestionable must be carried out unquestionably...'
   PL: „C-co robić? To, co oczywiste, musi być wykonane bezdyskusyjnie…”
99. [Status [PressureOfPrescript_2nd] — nazwa] 극심한 압박감
   źródło: Bufs-a1c9p2.json :: dataList[id=PressureOfPrescript_2nd].name
   kontekst: identyfikator statusu w tekstach: `[PressureOfPrescript_2nd]`
   limit: do 40 znaków
   EN: Extreme Onus
   PL: Ekstremalny Nacisk
100. [Status [PressureOfPrescript_2nd] — opis] - 수치 1당 가하는 피해량 +50% (최대 100%)\n- 개화 E.G.O::대행 상태면,\n· 수치가 1일 때, 최종 위력 +2\n· 수치가 2일 때, 대신 더하기 코인 위력 +1, 최종 위력 +3\n- 최대 2\n- 특정 스킬 사용 시, 압박감과 동일하게 취급되어 소모됨
   źródło: Bufs-a1c9p2.json :: dataList[id=PressureOfPrescript_2nd].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +50% damage for every Stack (max 100%)\n- Under Effloresced E.G.O::Procuration state:\n· At 1 Stack, Final Power +2\n· At 2 Stack, Plus Coin Power +1 and Final Power +3 instead\n- Max Stack: 2\n- When using certain Skills, counts as Onus and is consumed
   PL: - Zadaje +50% obrażeń za każdy stos (maks. 100%)\n- W stanie Rozkwitu E.G.O::Procuration,\n· Przy 1 stosie Moc Końcowa +2\n· Przy 2 stosach zamiast tego Moc Monety Plus +1 i Moc Końcowa +3\n- Maks. 2\n- Przy użyciu określonych Umiejętności traktowana jak Nacisk i zużywana
101. [Status [BlindFaith_LowMorale] — nazwa] 지령 붕괴 위기
   źródło: Bufs-a1c9p2.json :: dataList[id=BlindFaith_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BlindFaith_LowMorale]`
   limit: do 40 znaków
   EN: Prescript Incompliance Risk
   PL: Ryzyko Odrzucenia Nakazu
102. [Status [BlindFaith_LowMorale] — opis] - 사기저하\n- 지령 대상에게 가하는 피해량 +20%\n지령 대상이 아닌 대상에게 받는 피해량 +10%
   źródło: Bufs-a1c9p2.json :: dataList[id=BlindFaith_LowMorale].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +20% damage to targets that have The Prescript's Target\n- Take +10% damage from targets that do not have The Prescript's Target
   PL: - Niskie Morale\n- Zadaje +20% obrażeń celom z Celem Nakazu\nOtrzymuje +10% obrażeń od celów bez Celu Nakazu
103. [Status [BlindFaith_Panic] — nazwa] 지령 붕괴 위기
   źródło: Bufs-a1c9p2.json :: dataList[id=BlindFaith_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BlindFaith_Panic]`
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Status [BlindFaith_Panic] — opis] - 패닉\n- 지령 대상에게 가하는 피해량 +30%\n지령 대상이 아닌 대상에게 받는 피해량 +20%
   źródło: Bufs-a1c9p2.json :: dataList[id=BlindFaith_Panic].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +30% damage to targets that have The Prescript's Target\n- Take +20% damage from targets that do not have The Prescript's Target
   PL: - Panika\n- Zadaje +30% obrażeń celom z Celem Nakazu\nOtrzymuje +20% obrażeń od celów bez Celu Nakazu
105. [Status [YellowHarpoon] — nazwa] 노란작살
   źródło: Bufs-a1c9p2.json :: dataList[id=YellowHarpoon].name
   kontekst: identyfikator statusu w tekstach: `[YellowHarpoon]`
   limit: do 40 znaków
   EN: The Yellow Harpoon
   PL: Żółty Harpun
106. [Status [YellowHarpoon] — opis] - 턴 시작시, 신속 4, 호흡 8 얻음\n- 턴 종료시 박힌 작살을 보유한 적이 있으면, 호흡 횟수 3 증가
   źródło: Bufs-a1c9p2.json :: dataList[id=YellowHarpoon].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Haste and 8 Poise\n- Turn End: Gain +3 Poise Count if an enemy has Nested Harpoon
   PL: - Na początku tury zyskuje 4 Pośpiechu i 8 Oddechu\n- Na koniec tury, jeżeli jakiś wroga ma Wbity Harpun, zyskuje +3 Licznika Oddechu
107. [Status [YellowHarpoonSin] — nazwa] 신(心) - 노란작살
   źródło: Bufs-a1c9p2.json :: dataList[id=YellowHarpoonSin].name
   kontekst: identyfikator statusu w tekstach: `[YellowHarpoonSin]`
   limit: do 40 znaków
   EN: Shin(心) - The Yellow Harpoon
   PL: Shin (心) - Żółty Harpun
108. [Status [YellowHarpoonSin] — opis] - 기본 공격 레벨 +3, 기본 방어 레벨 +3\n- 전 턴에 자신을 공격한 대상 공격 시 정신력 3 회복\n- 자신의 정신력이 0 이상이면, (정신력 / 10)만큼 최종 위력 증가 (소수점 버림)
   źródło: Bufs-a1c9p2.json :: dataList[id=YellowHarpoonSin].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +3, Base Defense Level +3\n- Heal 3 SP when attacking target that attacked this unit last turn\n- At 0+ SP, gain Final Power by (SP / 10) (rounded down)
   PL: - Podstawowy Poziom Ataku +3, Podstawowy Poziom Obrony +3\n- Atakując cel, który w poprzedniej turze ją zaatakował, odzyskuje 3 Poczytalności\n- Przy Poczytalności 0+: Moc Końcowa +(Poczytalność / 10) (zaokr. w dół)
109. [Status [BeeSting] — nazwa] 박힌 작살 [벌침]
   źródło: Bufs-a1c9p2.json :: dataList[id=BeeSting].name
   kontekst: identyfikator statusu w tekstach: `[BeeSting]`
   limit: do 40 znaków
   EN: Nested Harpoon [Beesting]
   PL: Wbity Harpun [Żądło]
110. [Status [BeeSting] — opis] - 참격 내성 +0.2, 나태 내성 +0.2\n- 턴 종료 시 다음 턴에 속박 2 얻음\n- 공격 적중시 출혈 위력 1 얻음\n- 베스파에게 피격 시 궁니르 공명 2 얻음\n- 효과 제거 시 자신의 출혈 1회 발동
   źródło: Bufs-a1c9p2.json :: dataList[id=BeeSting].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Slash Resist. +0.2, Sloth Resist. +0.2\n- Turn End: Gain 2 Bind next turn\n- On Hit: Gain 1 Bleed Potency\n- When attacked by Vespa, gain 2 Gungnir's Droning\n- Activate Bleed on this unit once when this effect is removed
   PL: - Odporność na Cięcie +0,2, Odporność na Żądzę +0,2\n- Na koniec tury zyskuje 2 Spętań w następnej turze\n- Przy trafieniu zyskuje 1 Siły Krwawienia\n- Przy trafieniu przez Vespę zyskuje 2 Dudnienia Gungnira\n- Po usunięciu efektu wywołuje Krwawienie na tej jednostce 1 raz
111. [Status [ArtifactBeeSting] — nazwa] 박힌 작살 [말벌침]
   źródło: Bufs-a1c9p2.json :: dataList[id=ArtifactBeeSting].name
   kontekst: identyfikator statusu w tekstach: `[ArtifactBeeSting]`
   limit: do 40 znaków
   EN: Nested Harpoon [Waspsting]
   PL: Wbity Harpun [Żądło Osy]
112. [Status [ArtifactBeeSting] — opis] - 참격 내성 +1, 나태 내성 +1\n- 턴 종료 시 다음 턴에 속박 4 얻음\n- 공격 적중시 출혈 위력 3 얻음\n- 베스파에게 피격 시 궁니르 공명 3 얻음\n- 효과 제거 시 자신의 출혈 2회 발동
   źródło: Bufs-a1c9p2.json :: dataList[id=ArtifactBeeSting].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Slash Resist. +1, Sloth Resist. +1\n- Turn End: Gain 4 Bind next turn\n- On Hit: Gain 3 Bleed Potency\n- When attacked by Vespa, gain 3 Gungnir's Droning\n- Activate Bleed on this unit 2 times when this effect is removed
   PL: - Odporność na Cięcie +1, Odporność na Żądzę +1\n- Na koniec tury zyskuje 4 Spętań w następnej turze\n- Przy trafieniu zyskuje 3 Siły Krwawienia\n- Przy trafieniu przez Vespę zyskuje 3 Dudnienia Gungnira\n- Po usunięciu efektu wywołuje Krwawienie na tej jednostce 2 razy
113. [Status [HornetPoison] — nazwa] 궁니르 공명
   źródło: Bufs-a1c9p2.json :: dataList[id=HornetPoison].name
   kontekst: identyfikator statusu w tekstach: `[HornetPoison]`
   limit: do 40 znaków
   EN: Gungnir's Droning
   PL: Dudnienie Gungnira
114. [Status [HornetPoison] — opis] - 베스파에게 피격 시 효과 위력만큼 고정 피해를 입음\n- 턴 종료 후 횟수 1 감소 (진동 횟수를 증가시키는 효과를 동일하게 적용받음)
   źródło: Bufs-a1c9p2.json :: dataList[id=HornetPoison].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When attacked by Vespa, take fixed damage equal to this effect's Potency\n- Reduce Count by 1 after Turn End (Interacts the same way as normal Tremor does to effects that raise Tremor Count)
   PL: - Przy trafieniu przez Vespę otrzymuje obrażenia stałe równe Siłe tego efektu\n- Po zakończeniu tury traci 1 Licznika (Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających Licznik Wstrząsu)
115. [Status [HornetPoison] — tekst klimatyczny] <color=#fde55d>이 작살에 박힌 상대는 공격받을수록 강해지는 떨림으로 인해 붕괴된다.</color>
   źródło: Bufs-a1c9p2.json :: dataList[id=HornetPoison].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>
   EN: <color=#fde55d>Those impaled by the harpoon are pulverized as successive strikes amplify its vibrating force.</color>
   PL: <color=#fde55d>Wbięty przez ten harpun rozpada się, gdy kolejne uderzenia wzmacniają jego siłę drgań.</color>
116. [Status [CriticalDmgUpVespa] — nazwa] 섬봉광검술 - 환도
   źródło: Bufs-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].name
   kontekst: identyfikator statusu w tekstach: `[CriticalDmgUpVespa]`
   limit: do 50 znaków
   EN: Apic Flashburst Blade Art - Hwando
   PL: Sztuka Ostrza Apic Flashburst - Hwando
117. [Status [CriticalDmgUpVespa] — opis] 이번 턴 동안 치명타로 가하는 피해량이 수치당 추가로 10%씩 증가함
   źródło: Bufs-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].desc
   limit: do 120 znaków
   EN: Deal +10% more damage on Critical Hit for every Stack this turn
   PL: W tej turze obrażenia krytyczne rosną o 10% za każdą wartość
118. [Status [CriticalDmgUpVespa] — tekst klimatyczny] <color=#fde55d>공간이동에 가까운 순간적이고 폭발적인 도약법을 다루는 자에게 알맞은 검술.\n동부에서 전해져 내려온다.\n소년은 생과 사를 오가는 시술을 필사의 마음으로 받아들였고, 끝내 이겨내어 자격을 증명했다.</color>
   źródło: Bufs-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>, \n
   EN: <color=#fde55d>A swordfighting style originating from the East, suited to those who employ instantaneous bursts of leaping movement that verge on teleportation.\n\nThe boy braved the life-threatening augmentation with a desperate resolve, and his survival proved his worth.</color>
   PL: <color=#fde55d>Szermierka ze Wschodu, odpowiednia dla tych, którzy poruszają się skokami na granicy teleportacji.\nChłopak przyjął tę śmiertelnie niebezpieczną modyfikację z rozpaczliwą determinacją i ostatecznie ją przetrwał, dowodząc swojej wartości.</color>
119. [Status [Vespa_LowMorale] — nazwa] 언짢음
   źródło: Bufs-a1c9p2.json :: dataList[id=Vespa_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Vespa_LowMorale]`
   limit: do 40 znaków
   EN: Vexation
   PL: Zirytowanie
120. [Status [Vespa_LowMorale] — opis] - 사기 저하\n- 관통 위력 증가 1, 정신력 회복 효율 감소 1 얻음
   źródło: Bufs-a1c9p2.json :: dataList[id=Vespa_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Pierce Power Up and 1 SP Heal Efficiency Down
   PL: - Niskie Morale\n- Zyskuje 1 Wzrost Mocy Kłucia i 1 Spadek Wydajności Leczenia Poczytalności
121. [Status [Vespa_Panic] — nazwa] 언짢음
   źródło: Bufs-a1c9p2.json :: dataList[id=Vespa_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Vespa_Panic]`
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Status [Vespa_Panic] — opis] - 패닉\n- 관통 위력 증가 2, 관통 피해량 증가 1, 정신력 회복 효율 감소 2 얻음
   źródło: Bufs-a1c9p2.json :: dataList[id=Vespa_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Pierce Power Up, 1 Pierce DMG Up, and 2 SP Heal Efficiency Down
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Kłucia, 1 Wzrost Obrażeń Kłucia i 2 Spadek Wydajności Leczenia Poczytalności
123. [Status [ScarBygoneDays_LowMorale] — nazwa] 애증
   źródło: Bufs-a1c9p2.json :: dataList[id=ScarBygoneDays_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ScarBygoneDays_LowMorale]`
   limit: do 40 znaków
   EN: Affection and Resentment
   PL: Miłość i Uraza
124. [Status [ScarBygoneDays_LowMorale] — opis] 료슈에게 가하는 피해량과 받는 피해량 +10%
   źródło: Bufs-a1c9p2.json :: dataList[id=ScarBygoneDays_LowMorale].desc
   limit: do 120 znaków
   EN: Deal +10% damage to and take +10% damage from Ryōshū
   PL: Zadaje i otrzymuje +10% obrażeń od i wobec Ryōshū
125. [Status [ScarBygoneDays_Panic] — nazwa] 애증
   źródło: Bufs-a1c9p2.json :: dataList[id=ScarBygoneDays_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ScarBygoneDays_Panic]`
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Status [ScarBygoneDays_Panic] — opis] 료슈에게 가하는 피해량과 받는 피해량 +20%
   źródło: Bufs-a1c9p2.json :: dataList[id=ScarBygoneDays_Panic].desc
   limit: do 120 znaków
   EN: Deal +20% damage to and take +20% damage from Ryōshū
   PL: Zadaje i otrzymuje +20% obrażeń od i wobec Ryōshū
127. [Status [PhantomIncision] — nazwa] 검흔[잔상]
   źródło: Bufs-a1c9p2.json :: dataList[id=PhantomIncision].name
   kontekst: identyfikator statusu w tekstach: `[PhantomIncision]`
   limit: do 40 znaków
   EN: Bladetrail [Afterimage]
   PL: Ślad Ostrza [Powidło]
128. [Status [PhantomIncision] — opis] - 최댓값 : 99\n- 턴 시작시 수치 10당 취약 1 얻음 (최대 5)
   źródło: Bufs-a1c9p2.json :: dataList[id=PhantomIncision].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 99\n- Turn Start: Gain 1 Fragile for every 10 Stack (max 5)
   PL: - Maks. stosów: 99\n- Na początku tury zyskuje 1 Wrażliwości za każde 10 stosów (maks. 5)
129. [Status [PhantomIncisionTotal] — nazwa] 지혜성도
   źródło: Bufs-a1c9p2.json :: dataList[id=PhantomIncisionTotal].name
   kontekst: identyfikator statusu w tekstach: `[PhantomIncisionTotal]`
   limit: do 40 znaków
   EN: Dihui Star's Blade
   PL: Ostrze Gwiazdy Dihui
130. [Status [PhantomIncisionTotal] — opis] - 현재 스테이지의 검흔[잔상] 수치 총합
   źródło: Bufs-a1c9p2.json :: dataList[id=PhantomIncisionTotal].desc
   limit: do 120 znaków
   EN: - Total sum of Bladetrail [Afterimage] Stack in this Encounter
   PL: - Łączna suma stosów Śladu Ostrza [Powidło] w tej walce
131. [Status [LvDownLittleFingerBoss] — nazwa] 관망
   źródło: Bufs-a1c9p2.json :: dataList[id=LvDownLittleFingerBoss].name
   kontekst: identyfikator statusu w tekstach: `[LvDownLittleFingerBoss]`
   limit: do 40 znaków
   EN: Silent Regard
   PL: Wyczekiwanie
132. [Status [LvDownLittleFingerBoss] — opis] 미사용 버프
   źródło: Bufs-a1c9p2.json :: dataList[id=LvDownLittleFingerBoss].desc
   limit: do 120 znaków
   EN: UNUSED BUFF
   PL: NIEWYKORZYSTANY BUFF
133. [Status [TimeGapAb] — nazwa] 괴리
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeGapAb].name
   kontekst: identyfikator statusu w tekstach: `[TimeGapAb]`
   limit: do 40 znaków
   EN: Disjunction
   PL: Dysocjacja
134. [Status [TimeGapAb] — opis] - 턴 시작 시 수치만큼 부위가 보호막 얻음\n- 보호막이 감소하면 수치도 감소함
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeGapAb].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: The Part gains Shield equal to Stack\n- Reduction in the Shield reduces the Stack as well
   PL: - Na początku tury część zyskuje Tarczę równą wartości\n- Zmniejszenie Tarczy zmniejsza również wartość
135. [Status [TimeEntangleFour] — nazwa] 4중 잔상 얽힘
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleFour].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleFour]`
   limit: do 50 znaków
   EN: Fourfold Afterimage Entanglement
   PL: Splot Powideł IV
136. [Status [TimeEntangleFour] — opis] 잔상 얽힘 4단계\n- 자신의 속도 최댓값, 최솟값 -2\n- 자신의 공격 적중시 아래 효과 적용\n  · 독 1 부여\n  · 출혈 2 부여\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleFour].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 4 Afterimage Entanglement\n- Min & Max Speed -2 for this unit\n- On Hit, activate the following effects:\n  · Inflict 1 Poison\n  · Inflict 2 Bleed\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 4. stopnia\n- Min. i Maks. Szybkość tej jednostki -2\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 1 Zatrucia\n  · Nakłada 2 Krwawienia\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
137. [Status [TimeEntangleFour] — podsumowanie] 잔상 얽힘 4단계
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleFour].summary
   limit: do 120 znaków
   EN: Stage 4 Afterimage Entanglement
   PL: Splot Powideł 4. stopnia
138. [Status [TimeEntangleThree] — nazwa] 3중 잔상 얽힘
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleThree].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleThree]`
   limit: do 50 znaków
   EN: Threefold Afterimage Entanglement
   PL: Splot Powideł III
139. [Status [TimeEntangleThree] — opis] 잔상 얽힘 3단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 출혈 2 부여\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleThree].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 3 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 2 Bleed\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 3. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 2 Krwawienia\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
140. [Status [TimeEntangleThree] — podsumowanie] 잔상 얽힘 3단계
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleThree].summary
   limit: do 120 znaków
   EN: Stage 3 Afterimage Entanglement
   PL: Splot Powideł 3. stopnia
141. [Status [TimeEntangleTwo] — nazwa] 2중 잔상 얽힘
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleTwo].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleTwo]`
   limit: do 50 znaków
   EN: Twofold Afterimage Entanglement
   PL: Splot Powideł II
142. [Status [TimeEntangleTwo] — opis] 잔상 얽힘 2단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleTwo].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 2 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 2. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
143. [Status [TimeEntangleTwo] — podsumowanie] 잔상 얽힘 2단계
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleTwo].summary
   limit: do 120 znaków
   EN: Stage 2 Afterimage Entanglement
   PL: Splot Powideł 2. stopnia
144. [Status [TimeEntangleOne] — nazwa] 1중 잔상 얽힘
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleOne].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleOne]`
   limit: do 50 znaków
   EN: Onefold Afterimage Entanglement
   PL: Splot Powideł I
145. [Status [TimeEntangleOne] — opis] 잔상 얽힘 1단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 화상 2 부여
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleOne].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 1 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 2 Burn
   PL: Splot Powideł 1. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 2 Podpalenia
146. [Status [TimeEntangleOne] — podsumowanie] 잔상 얽힘 1단계
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleOne].summary
   limit: do 120 znaków
   EN: Stage 1 Afterimage Entanglement
   PL: Splot Powideł 1. stopnia
147. [Status [LittleFingerBoss_Shin] — nazwa] 신(心) - 지혜성
   źródło: Bufs-a1c9p2.json :: dataList[id=LittleFingerBoss_Shin].name
   kontekst: identyfikator statusu w tekstach: `[LittleFingerBoss_Shin]`
   limit: do 40 znaków
   EN: Shin (心) - Dihui Star
   PL: Shin (心) - Gwiazda Dihui
148. [Status [LittleFingerBoss_Shin] — opis] - 최댓값 : 3\n- 턴 시작 시 아래 효과 적용\n· 수치 1당 호흡 위력 5, 호흡 횟수 1 얻음\n· 자신의 잃은 체력 15% 당 참격 피해량 증가 1 얻음 (최대 5)
   źródło: Bufs-a1c9p2.json :: dataList[id=LittleFingerBoss_Shin].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Apply the following effects\n· Gain 5 Poise Potency and +1 Poise Count for every Stack\n· Gain 1 Slash DMG Up for every 15% missing HP on self (max 5)
   PL: - Maks. stosów: 3\n- Na początku tury działają następujące efekty\n· Zyskuje 5 Siły Oddechu i +1 Licznika Oddechu za każdy stos\n· Zyskuje 1 Wzrost Obrażeń Cięcia za każde 15% brakującego HP (maks. 5)
149. [Status [RyoshuParrySoji] — nazwa] 뒤엉키고 틀어진 기억과 추억
   źródło: Bufs-a1c9p2.json :: dataList[id=RyoshuParrySoji].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParrySoji]`
   limit: do 70 znaków
   EN: Twisted and Disjointed Memory and Recollection
   PL: Skręcone i Rozdarte Wspomnienia
150. [Status [RyoshuParrySoji] — opis] - 스킬 슬롯 수 +1\n- 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (턴당 1회)\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: Bufs-a1c9p2.json :: dataList[id=RyoshuParrySoji].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn (once per turn)\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (1 raz na turę)\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
151. [Status [RyoshuParrySoji] — podsumowanie] 생존한 아군이 있으면, 체력이 1 미만으로 감소하지 않음
   źródło: Bufs-a1c9p2.json :: dataList[id=RyoshuParrySoji].summary
   limit: do 120 znaków
   EN: If there is a surviving ally, HP does not drop below 1
   PL: Jeżeli żyją sojusznicy, HP nie spada poniżej 1
152. [Status [RyoshuStartA1C9P2] — nazwa] 난도질당한 기억
   źródło: Bufs-a1c9p2.json :: dataList[id=RyoshuStartA1C9P2].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuStartA1C9P2]`
   limit: do 40 znaków
   EN: Mutilated Memory
   PL: Pocięta Pamięć
153. [Status [RyoshuStartA1C9P2] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작 시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)
   źródło: Bufs-a1c9p2.json :: dataList[id=RyoshuStartA1C9P2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)
154. [Status [Ryoshu_IndexFightBuff] — nazwa] 난도질당한 기억과 추억
   źródło: Bufs-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].name
   kontekst: identyfikator statusu w tekstach: `[Ryoshu_IndexFightBuff]`
   limit: do 50 znaków
   EN: Mutilated Memory and Recollection
   PL: Pocięta Pamięć i Wspomnienia
155. [Status [Ryoshu_IndexFightBuff] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (턴당 1회)\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: Bufs-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (once per turn)\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (1 raz na turę)\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
156. [Status [Ryoshu_IndexFightBuff] — podsumowanie] 료슈 특수 효과
   źródło: Bufs-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].summary
   limit: do 120 znaków
   EN: Ryōshū Exclusive Effect
   PL: Efekt specjalny Ryōshū
157. [Status [Malkuth_Imperfect] — nazwa] 말쿠트의 통치 - 불완전 현현
   źródło: Bufs-a1c9p2.json :: dataList[id=Malkuth_Imperfect].name
   kontekst: identyfikator statusu w tekstach: `[Malkuth_Imperfect]`
   limit: do 60 znaków
   EN: Malkuth's Reign - Imperfect Manifestation
   PL: Panowanie Malkuth - Niedoskonała Manifestacja
158. [Status [Malkuth_Imperfect] — opis] <i><color=#d3a562>완전하지는 않지만 왕국을 다스릴 힘의 편린</color></i>
   źródło: Bufs-a1c9p2.json :: dataList[id=Malkuth_Imperfect].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#d3a562>, </color>, </i>
   EN: <i><color=#d3a562>An imperfect glimpse of the power that shall reign over the Kingdom</color></i>
   PL: <i><color=#d3a562>Niedoskonały fragment mocy, która zapanuje nad Królestwem</color></i>
159. [Status [TimeEntangleDesc] — nazwa] 잔상 얽힘
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleDesc].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleDesc]`
   limit: do 40 znaków
   EN: Afterimage Entanglement
   PL: Splot Powideł
160. [Status [TimeEntangleDesc] — opis] 잔상이 얽혀있는 상태\n패턴이 진행됨에 따라 단계가 변화함
   źródło: Bufs-a1c9p2.json :: dataList[id=TimeEntangleDesc].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Afterimages are Entangled\nEffect Stage changes with the progress of combat pattern
   PL: Stan splecionych powideł\nStopień efektu zmienia się wraz z postępem wzorca walki
161. [Status [IndexPrescriptDon_0] — nazwa] 지령[단말기] I
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptDon_0]`
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Status [IndexPrescriptDon_0] — opis] 지령 표식이 새겨진 스킬을 사용하거나 적중한다.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a Skill marked with Mark of the Prescript or hit a target with a marked Skill.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Używa Umiejętności oznaczonej Znakiem Nakazu lub trafia nią cel.\n\n- Na początku tury zyskuje efekt, gdy nie ma Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
163. [Status [IndexPrescriptDon_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Status [IndexPrescriptDon_1] — nazwa] 지령[단말기] II
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptDon_1]`
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Status [IndexPrescriptDon_1] — opis] 지령 표식이 새겨진 스킬이 적중한다.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with a Skill marked with Mark of the Prescript.\n\n- Turn Start: Gain this effect if this unit has Unlock - I\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Trafia cel Umiejętnością oznaczoną Znakiem Nakazu.\n\n- Na początku tury zyskuje efekt przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
166. [Status [IndexPrescriptDon_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Status [IndexPrescriptDon_2] — nazwa] 지령[단말기] III
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptDon_2]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Status [IndexPrescriptDon_2] — opis] E.G.O 각성 스킬 또는 개화 E.G.O::대행 상태에서 지령 표식이 새겨진 ‘스킬 3’이 적중한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with E.G.O Awakening Skill, or, in Effloresced E.G.O::Procuration state, 'Skill 3' marked with Mark of the Prescript.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Trafia cel Umiejętność Przebudzenia E.G.O, lub w stanie Rozkwitu E.G.O::Procuration, „Umiejętność 3” oznaczona Znakiem Nakazu.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
169. [Status [IndexPrescriptDon_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Status [IndexPrescriptDon_3] — nazwa] 지령[단말기] IV
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptDon_3]`
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Status [IndexPrescriptDon_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Zabija wszystkich wrogów przed nadejściem kolejnego Nakazu.\n\n- Na początku tury zyskuje efekt przy Odblokowaniu - III
172. [Status [IndexPrescriptDon_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].flavor
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Status [UnlockBuff_Base] — nazwa] 해금
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_Base].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_Base]`
   limit: do 40 znaków
   EN: Unlock
   PL: Odblokowanie
174. [Status [UnlockBuff_Base] — opis] - 지령의 가호가 일정 수치 이상이면 획득\n- 지령의 가호 수치에 따라 단계 증가\n- 최대 3단계까지 달성 가능
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuff_Base].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain this effect when over certain Grace of the Prescript Stack\n- Effect stage increases based on Grace of the Prescript Stack\n- Max: Stage 3
   PL: - Zdobywane przy Łasce Nakazu powyżej określonej wartości\n- Stopień rośnie zależnie od liczby stosów Łaski Nakazu\n- Maksymalnie 3. stopień
175. [Status [UnlockBuffAlly_1] — nazwa] 해금 - I
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_1].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuffAlly_1]`
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Status [UnlockBuffAlly_1] — opis] - 방어 레벨 +1\n- 전투 종료 시, 정신력 5 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +1\n- Combat End: Heal 5 SP
   PL: - Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 5 Poczytalności
177. [Status [UnlockBuffAlly_2] — nazwa] 해금 - II
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_2].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuffAlly_2]`
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Status [UnlockBuffAlly_2] — opis] - 방어 레벨 +2\n- 전투 종료 시, 정신력 10 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +2\n- Combat End: Heal 10 SP
   PL: - Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 10 Poczytalności
179. [Status [UnlockBuffAlly_3] — nazwa] 해금 - III
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_3].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuffAlly_3]`
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Status [UnlockBuffAlly_3] — opis] - 방어 레벨 +3\n- 전투 종료 시, 정신력 15 회복
   źródło: Bufs-a1c9p2.json :: dataList[id=UnlockBuffAlly_3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3\n- Combat End: Heal 15 SP
   PL: - Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 15 Poczytalności
181. [Status [Blandishment] — nazwa] 당연한 믿음
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment].name
   kontekst: identyfikator statusu w tekstach: `[Blandishment]`
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Status [Blandishment] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +2, 방어 레벨 +2\n- 기본 스킬로 획득하는 호흡 위력 +1\n- 기본 공격 스킬의 정신력 감소 효과로 정신력이 -15 미만으로 내려가지 않음\n- 최댓값 : 1
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +2, Defense Level +2\n- Gain 1 more Poise Potency from Base Skills\n- This unit's SP does not drop below -15 from SP loss effects on this unit's Base Attack Skills\n- Max Stack: 1
   PL: - Min. i Maks. Szybkość +1\n- Poziom Ataku +2, Poziom Obrony +2\n- Podstawowe Umiejętności zyskują +1 więcej Siły Oddechu\n- Poczytalność tej jednostki nie spada poniżej -15 z powodu efektów utraty Poczytalności jej podstawowych Umiejętności ataku\n- Maks. stosów: 1
183. [Status [Blandishment_Shin] — nazwa] 신(心) - 대행
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Shin].name
   kontekst: identyfikator statusu w tekstach: `[Blandishment_Shin]`
   limit: do 40 znaków
   EN: Shin (心) - Procuration
   PL: Shin (心) - Procuration
184. [Status [Blandishment_Shin] — opis] - 속도 최솟값, 최댓값 2 증가\n- 공격 레벨 +1, 방어 레벨 +1\n- 기본 스킬로 획득하는 호흡 위력과 횟수 +1\n- 기본 스킬의 피해량 +(잃은 체력 비율/2)% (최대 40%)\n- 최댓값 : 1
   źródło: Bufs-a1c9p2.json :: dataList[id=Blandishment_Shin].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- Offense Level +1, Defense Level +1\n- Gain 1 more Poise Potency and Poise Count from Base Skills\n- Deal +(missing HP percentage / 2)% damage with Base Skills (max 40%)\n- Max Stack: 1
   PL: - Min. i Maks. Szybkość +2\n- Poziom Ataku +1, Poziom Obrony +1\n- Podstawowe Umiejętności zyskują +1 więcej Siły Oddechu i Licznika Oddechu\n- Podstawowe Umiejętności zadają +(procent brakującego HP / 2)% obrażeń (maks. 40%)\n- Maks. stosów: 1

## Statusy i efekty bojowe — Bufs-a1c9p3
- plik gry: `Bufs-a1c9p3.json`

185. [Status [MosesWhiteBreathMental] — nazwa] 하얀 숨 - 정신 보호
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesWhiteBreathMental].name
   kontekst: identyfikator statusu w tekstach: `[MosesWhiteBreathMental]`
   limit: do 50 znaków
   EN: White Breath - Safeguard the Mind
   PL: Biały Oddech - Osłona Umysłu
186. [Status [MosesWhiteBreathMental] — opis] - 캐릭터의 기본 정신력 증가 조건에 의한 정신력 회복량 5 증가\n- 캐릭터의 기본 정신력 감소 조건에 의한 정신력 감소량 5 감소\n- 턴 종료시 1 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesWhiteBreathMental].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Amount of SP healed due to the unit's 'Base factors increasing Sanity(SP)' increases by 5\n- Amount of SP lost due to the unit's 'Base factors decreasing Sanity(SP)' decreases by 5\n- Turn End: Lose 1 Stack
   PL: - Odzyskiwana Poczytalność z podstawowych warunków wzrostu Poczytalności rośnie o 5\n- Tracona Poczytalność z podstawowych warunków spadku Poczytalności maleje o 5\n- Na koniec tury traci 1 stos
187. [Status [MosesRedBreathBody] — nazwa] 붉은 숨 - 육체 강화
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathBody].name
   kontekst: identyfikator statusu w tekstach: `[MosesRedBreathBody]`
   limit: do 50 znaków
   EN: Red Breath - Strengthen the Body
   PL: Czerwony Oddech - Wzmocnienie Ciała
188. [Status [MosesRedBreathBody] — opis] - (자신의 정신력 / 10)만큼 공격 레벨, 방어 레벨이 증가함 (소수점 버림)\n- 턴 종료시 1 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathBody].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +(SP/10) Offense Level and Defense Level (rounded down)\n- Turn End: Lose 1 Stack
   PL: - Poziom Ataku i Poziom Obrony rosną o (Poczytalność / 10) (zaokrąglone w dół)\n- Na koniec tury traci 1 stos
189. [Status [MosesRedBreathShield] — nazwa] 붉은 숨 - 보호
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathShield].name
   kontekst: identyfikator statusu w tekstach: `[MosesRedBreathShield]`
   limit: do 40 znaków
   EN: Red Breath - Protect
   PL: Czerwony Oddech - Ochrona
190. [Status [MosesRedBreathShield] — opis] - 턴 시작시 이번 턴 동안 보호막 30 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathShield].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 30 Shield for this turn
   PL: - Na początku tury zyskuje 30 Tarczy na tę turę
191. [Status [MosesPurpleBreathBind] — nazwa] 보라색 숨 - 히스테릭
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesPurpleBreathBind].name
   kontekst: identyfikator statusu w tekstach: `[MosesPurpleBreathBind]`
   limit: do 40 znaków
   EN: Purple Breath - Hysteria
   PL: Fioletowy Oddech - Histeria
192. [Status [MosesPurpleBreathBind] — opis] - 최댓값: 4\n- 턴 종료시 체력, 정신력 수치만큼 감소\n- 턴 종료시 모제스의 체력, 정신력 수치만큼 감소\n- 다음 턴에 취약 2, 속박 3, 더하기 코인 약화 3 얻음\n- 효과 발동시 1 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesPurpleBreathBind].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: Lose HP and SP equal to Stack\n- Turn End: Moses loses HP and SP equal to Stack\n- Gain 2 Fragile, 3 Bind, and 3 Plus Coin Drop next turn\n- Lose 1 Stack when this effect is triggered
   PL: - Maks. stosów: 4\n- Na koniec tury traci HP i Poczytalność równą wartości\n- Na koniec tury Moses traci HP i Poczytalność równą wartości\n- W następnej turze zyskuje 2 Wrażliwości, 3 Spętań i 3 Osłabienia Monet Plus\n- Przy wywołaniu efektu traci 1 stos
193. [Status [MosesRedBreathCharge] — nazwa] 깊은 숨 - 붉은색
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathCharge].name
   kontekst: identyfikator statusu w tekstach: `[MosesRedBreathCharge]`
   limit: do 40 znaków
   EN: Deep Breath - Red
   PL: Głęboki Oddech - Czerwień
194. [Status [MosesRedBreathCharge] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>턴 종료시 최댓값이면, 강력한 스킬을 사용함</color></mark></b></u>\n- 특정 스킬 사용시 소모됨\n- 해당 버프가 있으면 패닉 상태가 되지 않음\n- 받는 피해 +(수치 x 20)%, 방어 레벨 수치만큼 감소\n- 턴 종료시 체력 피해 10, 정신력 피해 20 받음
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathCharge].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Turn End: At Max Stack, use a powerful Skill</color></mark></b></u>\n- Consumed when using a certain Skill\n- Becomes immune to Panic under this effect\n- Take +(Stack x 20)% damage and lose Defense Level equal to Stack\n- Turn End: Take 10 HP damage and 20 SP damage
   PL: - Maks. stosów: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Na koniec tury przy Maks. stosach używa potężnej Umiejętności</u></b></mark></color>\n- Zużywana przy użyciu określonych Umiejętności\n- Ten efekt chroni przed Paniką\n- Otrzymuje +(stosy x 20)% obrażeń i traci Poziom Obrony równy liczbie stosów\n- Na koniec tury otrzymuje 10 obrażeń HP i 20 obrażeń Poczytalności
195. [Status [MosesRedBreathCharge] — tekst klimatyczny] 깊게 가라앉아, 호흡 하나마다 붉은색의 표상을 떠올리며 숨을 삼킨다.
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathCharge].flavor
   limit: do 120 znaków
   EN: Sink deeper and let the crimson images surface with every breath.
   PL: Pogrąża się głębiej, a z każdym oddechem połyka szkarłatne obrazy.
196. [Status [MosesRedBreathAttack] — nazwa] 붉은 숨 - 내달리는 몸
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathAttack].name
   kontekst: identyfikator statusu w tekstach: `[MosesRedBreathAttack]`
   limit: do 50 znaków
   EN: Red Breath - Push the Body's Limit
   PL: Czerwony Oddech - Granica Ciała
197. [Status [MosesRedBreathAttack] — opis] - 공격 레벨 5 증가\n- 기본 스킬의 합 위력 +5
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesRedBreathAttack].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 5 Offense Level\n- Base Skill Clash Power +5
   PL: - Zyskuje 5 Poziomu Ataku\n- Moc Starcia podstawowych Umiejętności +5
198. [Status [MosesSin] — nazwa] 신(心) - 모제스
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesSin].name
   kontekst: identyfikator statusu w tekstach: `[MosesSin]`
   limit: do 40 znaków
   EN: Shin (心) - Moses
   PL: Shin (心) - Moses
199. [Status [MosesSin] — opis] - 방어 레벨 +3, 수비 위력 +2\n- 스킬 효과로 자신의 정신력을 감소했으면, 다음 턴에 보호를 (정신력 감소량 / 5)만큼 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesSin].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3, Defense Power +2\n- If this unit lost SP due to its Skill's SP loss effects, gain Protection equal to (SP lost / 5) next turn
   PL: - Poziom Obrony +3, Moc Obrony +2\n- Jeżeli straciła Poczytalność przez efekty utraty Poczytalności swoich Umiejętności, w następnej turze zyskuje Ochronę równą (utracona Poczytalność / 5)
200. [Status [MosesWarPTSD] — nazwa] 그 날의 기억
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesWarPTSD].name
   kontekst: identyfikator statusu w tekstach: `[MosesWarPTSD]`
   limit: do 40 znaków
   EN: Memories of that Day
   PL: Wspomnienia Tamtego Dnia
201. [Status [MosesWarPTSD] — opis] - 기본 공격 레벨 -??\n- 기본 방어 레벨 -??\n- 턴 시작시 신속 5 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesWarPTSD].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Attack Level -??\n- Base Defense Level -??\n- Turn Start: Gain 5 Haste
   PL: - Podstawowy Poziom Ataku -??\n- Podstawowy Poziom Obrony -??\n- Na początku tury zyskuje 5 Pośpiechu
202. [Status [MosesMiddle_LowMorale] — nazwa] 돌이킬 수 없이 망가진 몸
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesMiddle_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[MosesMiddle_LowMorale]`
   limit: do 40 znaków
   EN: Body Broken Beyond Repair
   PL: Ciało Nieodwracalnie Złamane
203. [Status [MosesMiddle_LowMorale] — opis] - 사기 저하\n- 턴 시작시 에즈라, 베스파에게 수비 위력 증가 +2 부여, 취약 1 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesMiddle_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile and apply +2 Defense Power Up to Ezra and Vespa
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości i nakłada +2 Wzrostu Mocy Obrony na Ezrę i Vespę
204. [Status [MosesMiddle_Panic] — nazwa] 돌이킬 수 없이 망가진 몸
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesMiddle_Panic].name
   kontekst: identyfikator statusu w tekstach: `[MosesMiddle_Panic]`
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Status [MosesMiddle_Panic] — opis] - 패닉\n- 취약을 1 얻고, ‘숨 고르기’를 사용함
   źródło: Bufs-a1c9p3.json :: dataList[id=MosesMiddle_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Fragile and use 'Steady the Breath'
   PL: - Panika\n- Zyskuje 1 Wrażliwości i używa „Wyrównania Oddechu”
206. [Status [EzraMiddle_LowMorale] — nazwa] 자기 방어 - 가면
   źródło: Bufs-a1c9p3.json :: dataList[id=EzraMiddle_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[EzraMiddle_LowMorale]`
   limit: do 40 znaków
   EN: Insecurity: Mask
   PL: Niepewność: Maska
207. [Status [EzraMiddle_LowMorale] — opis] - 사기 저하\n- 공격 위력 감소 1 얻음\n- 방어 레벨 증가 2 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=EzraMiddle_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Attack Power Down\n- Gain 2 Defense Level Up
   PL: - Niskie Morale\n- Zyskuje 1 Spadek Mocy Ataku\n- Zyskuje 2 Wzrostu Poziomu Obrony
208. [Status [EzraMiddle_Panic] — nazwa] 자기 방어 - 가면
   źródło: Bufs-a1c9p3.json :: dataList[id=EzraMiddle_Panic].name
   kontekst: identyfikator statusu w tekstach: `[EzraMiddle_Panic]`
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Status [EzraMiddle_Panic] — opis] - 패닉\n- 공격 위력 감소 1 얻음\n- 방어 레벨 증가 3 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=EzraMiddle_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Attack Power Down\n- Gain 3 Defense Level Up
   PL: - Panika\n- Zyskuje 1 Spadek Mocy Ataku\n- Zyskuje 3 Wzrostu Poziomu Obrony
210. [Status [DimensionalBagEzraA] — nazwa] 차원가방 - 알라스 공방
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraA].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraA]`
   limit: do 50 znaków
   EN: Dimensional Bag - Allas Workshop
   PL: Worek Wymiarowy - Warsztat Allas
211. [Status [DimensionalBagEzraA] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 알라스 공방 장갑\n- 다음 공방 무기: 네스터 공방 망치
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraA].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Allas Workshop Gloves\n- Next Workshop weapon: Nester Workshop Hammer
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Rękawice Warsztatu Allas\n- Następna broń warsztatowa: Młot Warsztatu Nester
212. [Status [DimensionalBagEzraA] — tekst klimatyczny] “여기 제품들은 하나같이 가속력이 빵! 하고 터져 나와서 시원시원해!”
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraA].flavor
   limit: do 140 znaków
   EN: "Everything from this Workshop kicks off the acceleration with a bang! It's super punchy and satisfying!"
   PL: „Każdy produkt stąd rozpędza się jak wybuch — bwam! I czujesz każde uderzenie!”
213. [Status [DimensionalBagEzraB] — nazwa] 차원가방 - 네스터 공방
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraB].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraB]`
   limit: do 50 znaków
   EN: Dimensional Bag - Nester Workshop
   PL: Worek Wymiarowy - Warsztat Nester
214. [Status [DimensionalBagEzraB] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 네스터 공방 망치\n- 다음 공방 무기: 스크류 아틀리에제 드릴 망치
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraB].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Nester Workshop Hammer\n- Next Workshop weapon: Screw Atelier Drill Hammer
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Młot Warsztatu Nester\n- Następna broń warsztatowa: Młot Wiertniczy Screw Atelier
215. [Status [DimensionalBagEzraB] — tekst klimatyczny] “이게 참… 타격이 들어가는 절묘한 타이밍에 버튼을 눌러주면 진동과 함께 무기의 충격 면적이 극대화되는데, 적응만 잘하면 재밌어!”
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraB].flavor
   limit: do 220 znaków
   EN: "Alright, so... Hit the button <i>right</i> as the strike lands, and bam! The vibration goes nuts and maximizes the area of the impact. It's a riot once you get the hang of it!"
   PL: „Słuchaj... Wciśniesz przycisk dokładnie w momencie uderzenia i bum! Wibracja szaleje, maksymalizując powierzchnię uderzenia. Gdy się przyzwyczaisz, to czysta frajda!”
216. [Status [DimensionalBagEzraC] — nazwa] 차원가방 - 스크류 아틀리에
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraC].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraC]`
   limit: do 50 znaków
   EN: Dimensional Bag - Screw Atelier
   PL: Worek Wymiarowy - Screw Atelier
217. [Status [DimensionalBagEzraC] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 스크류 아틀리에제 드릴 망치\n- 다음 공방 무기: 나미르 공방 건틀릿
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraC].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Screw Atelier Drill Hammer\n- Next Workshop weapon: Namir Workshop Gauntlets
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Młot Wiertniczy Screw Atelier\n- Następna broń warsztatowa: Gauntlety Warsztatu Namir
218. [Status [DimensionalBagEzraC] — tekst klimatyczny] “여기 걸 다룰 땐 조심해야 해. 잘못했다간, 휘두른 사람이 감전될 수도 있어!”
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraC].flavor
   limit: do 150 znaków
   EN: "Seriously, gotta be careful with this Workshop's babies. One bad slip and you'll end up zapping yourself instead!"
   PL: „Z tymi dziećmi Screw Atelier trzeba uważać. Jedna pomyłka i porażenie cię we własnym uzbrojeniu!”
219. [Status [DimensionalBagEzraD] — nazwa] 차원가방 - 나미르 공방
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraD].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraD]`
   limit: do 50 znaków
   EN: Dimensional Bag - Namir Workshop
   PL: Worek Wymiarowy - Warsztat Namir
220. [Status [DimensionalBagEzraD] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 나미르 공방 건틀릿\n- 다음 공방 무기: 알라스 공방 장갑
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraD].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Namir Workshop Gauntlets\n- Next Workshop weapon: Allas Workshop Gloves
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Gauntlety Warsztatu Namir\n- Następna broń warsztatowa: Rękawice Warsztatu Allas
221. [Status [DimensionalBagEzraD] — tekst klimatyczny] “G사 특이점인 구가 들어간 제품인데, 잘 쓰려면 공중에서 스위치를 눌러 발동시킨 다음, 무게로 찍어 눌러야 해. 제대로 꽂히면 진짜 아파!”
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraD].flavor
   limit: do 280 znaków
   EN: "Now this one's got G Corp.'s Singularity baked in—the Sphere! Here's how it works: You float up, pop the switch midair, and crush down with the weight of the gravity. Land a solid hit, and it's gonna be... brutal."
   PL: „Ten ma w sobie osobliwość Korporacji G — Kulę! Działa tak: wzlatujesz, wciskasz przełącznik w powietrzu i dociskasz ciężarem grawitacji. Jak trafi porządnie, to boli... brutalnie.”
222. [Status [DimensionalBagEzraE] — nazwa] 차원가방 - 유리아 공방
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraE].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraE]`
   limit: do 50 znaków
   EN: Dimensional Bag - YuRia Atelier
   PL: Worek Wymiarowy - YuRia Atelier
223. [Status [DimensionalBagEzraE] — opis] - 현재 공방 무기: 유리아 공방 특제 수제작 골든 리트리버 전용 도끼
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraE].desc
   limit: do 120 znaków
   EN: - Current Workshop Weapon: YuRia Atelier Special Handmade Golden Retriever-Exclusive Axe
   PL: - Obecna broń warsztatowa: Ręcznie robiona siekiera YuRia tylko dla Golden Retrievera
224. [Status [DimensionalBagEzraE] — tekst klimatyczny] “유리아? 지금은 독립해서 공방을 운영하고 있어. 예전보다 더 잘나간다더라.”\n“인형에서 사람 몸으로 되돌렸던 그 사건이 진짜 대박이었는데.”
   źródło: Bufs-a1c9p3.json :: dataList[id=DimensionalBagEzraE].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Oh, YuRia? Yeah, she's gone full solo now, and her Workshop—man, it's totally blowin' up."\n\n"Speaking of, I still remember her turning back from plush doll to human... Haha, that case sure was one hell of a bombshell."
   PL: „YuRia? Dziś działa solo i jej warsztat szaleje — mówią, że świetnie idzie.”\n„Ta sprawa, gdy wróciła z pluszowej lalki w człowieka? Prawdziwa bomba.”
225. [Status [MiddleFingerEzraSin] — nazwa] 신(心) - 에즈라
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerEzraSin].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerEzraSin]`
   limit: do 40 znaków
   EN: Shin (心) - Ezra
   PL: Shin (心) - Ezra
226. [Status [MiddleFingerEzraSin] — opis] - 기본 방어 레벨 +2\n- 기본 공격 위력 +1, 수비 위력 +2\n- 모제스의 깊은 숨 - 붉은색 1당 에즈라, 베스파가 사용하는 원호 방어로 에즈라가 받는 정신력 회복량 +4 (최대 12)
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerEzraSin].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Defense Level +2\n- Base Attack Power +1, Defense Power +2\n- For every 'Deep Breath - Red' Stack on Moses, Ezra and Vespa's Assist Defense heals 4 more SP for Ezra (max 12)
   PL: - Podstawowy Poziom Obrony +2\n- Podstawowa Moc Ataku +1, Moc Obrony +2\n- Za każdy stos Głębokiego Oddechu - Czerwieni Moses: Wsparcie Obrony używane przez Ezrę i Vespę odzyskuje dla Ezry +4 Poczytalności (maks. 12)
227. [Status [VengeanceBookSpider] — nazwa] 앙갚음 장부
   źródło: Bufs-a1c9p3.json :: dataList[id=VengeanceBookSpider].name
   kontekst: identyfikator statusu w tekstach: `[VengeanceBookSpider]`
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: Księga Zemsty
228. [Status [VengeanceBookSpider] — opis] 중지 아비 - 마티아스나 중지 제자 - 키라가 이 효과를 보유한 대상에게 스킬 적중시 정신력 회복 7 (스킬당 1회)
   źródło: Bufs-a1c9p3.json :: dataList[id=VengeanceBookSpider].desc
   limit: do 200 znaków
   EN: When The Middle Nursefather - Matthias or The Middle Apprentice - Kira uses a Skill to hit a target who has this effect, they heal 7 SP (once per Skill)
   PL: Gdy Ojciec Środkowego - Matthias albo Uczeń Środkowego - Kira trafi Umiejętnością cel z tym efektem, odzyskuje 7 Poczytalności (1 raz na Umiejętność)
229. [Status [VengeanceBookSpider] — tekst klimatyczny] “네놈들… 즉결 처형이다.”
   źródło: Bufs-a1c9p3.json :: dataList[id=VengeanceBookSpider].flavor
   limit: do 120 znaków
   EN: "Bastards... Prepare to face complete and total extermination."
   PL: „Wy... natychmiastowa egzekucja.”
230. [Status [ResentmentSpider] — nazwa] 중지 - 원한
   źródło: Bufs-a1c9p3.json :: dataList[id=ResentmentSpider].name
   kontekst: identyfikator statusu w tekstach: `[ResentmentSpider]`
   limit: do 40 znaków
   EN: The Middle - Grudge
   PL: Środkowy - Uraza
231. [Status [ResentmentSpider] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: Bufs-a1c9p3.json :: dataList[id=ResentmentSpider].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced when using certain Skills\n- For every Stack, Offense Level +1, Defense Level -2, and Counter Skills deal +5% damage\n- At max Stack, take +20% damage
   PL: - Maks. stosów: 10\n- Zmniejszana przy użyciu określonych Umiejętności\n- Za każdy stos: Poziom Ataku +1, Poziom Obrony -2, Obrażenia Umiejętności Kontratakujących +5%\n- Przy maks. stosach otrzymuje +20% obrażeń
232. [Status [ResentmentSpider] — tekst klimatyczny] 중지는 잊지 않아.
   źródło: Bufs-a1c9p3.json :: dataList[id=ResentmentSpider].flavor
   limit: do 120 znaków
   EN: The Middle never forgets.
   PL: Środkowy nie zapomina.
233. [Status [ResentmentSpiderDaughter] — nazwa] 중지 - 원한
   źródło: Bufs-a1c9p3.json :: dataList[id=ResentmentSpiderDaughter].name
   kontekst: identyfikator statusu w tekstach: `[ResentmentSpiderDaughter]`
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Status [ResentmentSpiderDaughter] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: Bufs-a1c9p3.json :: dataList[id=ResentmentSpiderDaughter].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Status [GotACompliment] — nazwa] 칭찬 받았다!
   źródło: Bufs-a1c9p3.json :: dataList[id=GotACompliment].name
   kontekst: identyfikator statusu w tekstach: `[GotACompliment]`
   limit: do 40 znaków
   EN: I Got Praised!
   PL: Dostałam Pochwałę!
236. [Status [GotACompliment] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치 2당 기본 위력 +1\n- 수치당 참격, 타격 스킬의 피해량 +8%
   źródło: Bufs-a1c9p3.json :: dataList[id=GotACompliment].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced by 1 when this unit is hit by 2 Skills\n- Base Power +1 for every 2 Stack\n- Slash and Blunt Skills deal +8% damage for every Stack
   PL: - Maks. stosów: 10\n- Maleje o 1 przy trafieniu 2 Umiejętnościami\n- Moc Bazowa +1 za każde 2 stosy\n- Umiejętności Cięcia i Obuchu zadają +8% obrażeń za każdy stos
237. [Status [DaughterEducationSpider] — nazwa] 잘 봐둬라 딸!
   źródło: Bufs-a1c9p3.json :: dataList[id=DaughterEducationSpider].name
   kontekst: identyfikator statusu w tekstach: `[DaughterEducationSpider]`
   limit: do 40 znaków
   EN: Check This Out, Kiddo!
   PL: Dobrze się Przyjrzyj, Córeczko!
238. [Status [DaughterEducationSpider] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치 2당 기본 위력 +1\n- 수치당 참격, 타격 스킬의 피해량 +5%
   źródło: Bufs-a1c9p3.json :: dataList[id=DaughterEducationSpider].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced by 1 when this unit is hit by 2 Skills\n- Base Power +1 for every 2 Stack\n- Slash and Blunt Skills deal +5% damage for every Stack
   PL: - Maks. stosów: 10\n- Maleje o 1 przy trafieniu 2 Umiejętnościami\n- Moc Bazowa +1 za każde 2 stosy\n- Umiejętności Cięcia i Obuchu zadają +5% obrażeń za każdy stos
239. [Status [ReinforcedTattooSpider] — nazwa] 중지 - 원한 문신 [<s>큰 형님</s>]
   źródło: Bufs-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedTattooSpider]`
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: The Middle - Vengeance Tattoo [<s>Great Brother</s>]
   PL: Środkowy - Tatuaż Zemsty [<s>Wielki Brat</s>]
240. [Status [ReinforcedTattooSpider] — opis] - 최댓값: 2\n- 턴 종료시 소멸\n- 타격, 질투 속성의 피해량 +10%
   źródło: Bufs-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Expires at Turn End\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 2\n- Znika na koniec tury\n- Zadaje +10% obrażeń Obuchu i Zawiści
241. [Status [ReinforcedTattooSpider] — tekst klimatyczny] 누구보다 의리를 잘 지켜 큰 형님이 되었지만, 검 하나 때문에 의리를 저버린 놈.
   źródło: Bufs-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].flavor
   limit: do 150 znaków
   EN: A Great Brother whose prestige was secured by his loyalty; a fool who has abandoned that very thing over a sword.
   PL: Z lojalności zrobił się Wielki Brat; tchórz z niego, gdy dla jednego miecza zdradził tę lojalność.
242. [Status [ReinforcedTattooSpiderDaughter] — nazwa] 중지식 강화 문신
   źródło: Bufs-a1c9p3.json :: dataList[id=ReinforcedTattooSpiderDaughter].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedTattooSpiderDaughter]`
   limit: do 60 znaków
   EN: The Middle Styled Augmentation Tattoos
   PL: Wzmocnione Tatuaże Stylu Środkowego
243. [Status [ReinforcedTattooSpiderDaughter] — opis] - 최댓값: 3\n- 턴 종료시 소멸\n- 타격, 질투 속성의 피해량 +10%
   źródło: Bufs-a1c9p3.json :: dataList[id=ReinforcedTattooSpiderDaughter].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Expires at Turn End\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 3\n- Znika na koniec tury\n- Zadaje +10% obrażeń Obuchu i Zawiści
244. [Status [HeatingWireOnSpider] — nazwa] 열선 ON
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOnSpider].name
   kontekst: identyfikator statusu w tekstach: `[HeatingWireOnSpider]`
   limit: do 40 znaków
   EN: Thermal Blades ON
   PL: Ostrza Termiczne - ON
245. [Status [HeatingWireOnSpider] — opis] 열선 스킬의 코인 적중시 출혈 위력 및 횟수 부여량 만큼 화상 위력 및 횟수 추가 부여
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOnSpider].desc
   limit: do 170 znaków
   EN: On Hit with Thermal Blade Skill Coins: additionally inflict Burn Potency and Count equal to Bleed Potency and Count inflicted
   PL: Przy trafieniu monetą Umiejętności Ostrzy Termicznych dodatkowo nadaje Podpalenie (Moc i Licznik) w wysokości nadawanego Krwawienia (Moc i Licznik)
246. [Status [HeatingWireOnSpider] — tekst klimatyczny] 아빠 거만큼은 아니지만, 내 검으로도 녹이면서 벨 수 있어! 하지만 아빠 거처럼 계속 켜둘 순 없어…
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOnSpider].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's not as good as papa's, but I can also slice and sizzle at the same time!\nBut unlike papa's, I gotta let it cool from time to time...
   PL: To nie to co u taty, ale moje ostrze też potrafi ciąć i rozgrzewać! Tylko w przeciwieństwie do taty muszę czasem dać mu ostygnąć…
247. [Status [HeatingWireOffSpider] — nazwa] 열선 OFF
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOffSpider].name
   kontekst: identyfikator statusu w tekstach: `[HeatingWireOffSpider]`
   limit: do 40 znaków
   EN: Thermal Blades OFF
   PL: Ostrza Termiczne - OFF
248. [Status [HeatingWireOffSpider] — opis] 열선 스킬의 추가 효과가 발동되지 않음
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOffSpider].desc
   limit: do 120 znaków
   EN: Additional effects of Thermal Blade Skills do not activate
   PL: Dodatkowe efekty Umiejętności Rozgrzanych Ostrz nie działają
249. [Status [HeatingWireOffSpider] — tekst klimatyczny] 검의 열선이 꺼져있다
   źródło: Bufs-a1c9p3.json :: dataList[id=HeatingWireOffSpider].flavor
   limit: do 120 znaków
   EN: The sword's thermal wires are deactivated.
   PL: Ostrza miecza są wyłączone
250. [Status [MiddleFatherGuts] — nazwa] 초근성
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherGuts].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherGuts]`
   limit: do 40 znaków
   EN: Ridiculous Grit
   PL: Zwariowana Wytrwałość
251. [Status [MiddleFatherGuts] — opis] - 받는 피해를 1로 고정함 (키워드 피해 포함)\n- 합 승리시 (합 횟수 x 5)만큼 정신력 추가로 오름 (최대 15)\n- 턴 종료시 자신의 스킬 효과로 이번 턴 정신력이 감소했으면, 다음 턴에 피해량 증가 3 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherGuts].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Reduce all incoming damage to 1 (including Keyword damages)\n- On Clash Win, heal (Clash count x 5) more SP (max 15)\n- Turn End: If this unit lost SP this turn due to its Skill effects, gain 3 Damage Up next turn
   PL: - Otrzymywane obrażenia są blokowane na 1 (z obrażeniami słów kluczowych)\n- Po wygranym Starciu odzyskuje dodatkowo (liczba starć x 5) Poczytalności (maks. 15)\n- Na koniec tury, jeśli w tej turze stracił Poczytalność od Umiejętności, zyskuje w następnej turze 3 Wzrost Obrażeń
252. [Status [MiddleFatherGuts] — tekst klimatyczny] “신(心)이니 뭐니 다 필요 없어. 이 악물고 지금까지 새겨 온 모든 문신의 힘을 끌어 올리면, 신(心) 같은 기술 없이도 난 충분히 강하다.”
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherGuts].flavor
   limit: do 250 znaków
   EN: "I don't need some stupid crutch like that "Shin (心)" crap. I just gotta pull as much power as I can from these tattoos and grit my teeth, and I'll overpower your fancy little tricks no problem."
   PL: „Shin (心) czy co tam jeszcze — nic z tego nie potrzebuję. Zaciśnę zęby i wyciągnę całą moc ze wszystkich wytatuowanych do dziś znaków. Bez technik pokroju Shin (心) i tak jestem wystarczająco silny.”
253. [Status [MiddleFingerDaddy_LowMorale] — nazwa] 광분
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaddy_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerDaddy_LowMorale]`
   limit: do 40 znaków
   EN: Mad Rampage
   PL: Szał
254. [Status [MiddleFingerDaddy_LowMorale] — opis] - 사기 저하\n턴 시작 시 공격 위력 증가 2, 방어 레벨 감소 4를 얻고,\n이전 턴에 받은 체력 피해량 30당 피해량 증가 1을 얻음 (최대 5)
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaddy_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 2 Attack Power Up and 4 Defense Level Down; gain 1 Damage Up for every 30 HP damage taken last turn (max 5)
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Wzrostu Mocy Ataku i 4 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 30 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
255. [Status [MiddleFingerDaddy_Panic] — nazwa] 광분
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaddy_Panic].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerDaddy_Panic]`
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Status [MiddleFingerDaddy_Panic] — opis] - 패닉\n턴 시작 시 공격 위력 증가 3, 방어 레벨 감소 5를 얻고,\n이전 턴에 받은 체력 피해량 25당 피해량 증가 1을 얻음 (최대 5)
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaddy_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 3 Attack Power Up and 5 Defense Level Down; gain 1 Damage Up for every 25 HP damage taken last turn (max 5)
   PL: - Panika\nNa początku tury zyskuje 3 Wzrostu Mocy Ataku i 5 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 25 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
257. [Status [MiddleFingerDaughter_LowMorale] — nazwa] 흥분
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaughter_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerDaughter_LowMorale]`
   limit: do 40 znaków
   EN: Fervor
   PL: Podniecenie
258. [Status [MiddleFingerDaughter_LowMorale] — opis] - 사기 저하\n턴 시작 시 방어 레벨 감소 2을 얻고,\n이전 턴에 받은 체력 피해량 30당 피해량 증가 1을 얻음 (최대 5)
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaughter_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 2 Defense Level Down; gain 1 Damage Up for every 30 HP damage taken last turn (max 5)
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Spadek Poziomu Obrony,\ni 1 Wzrost Obrażeń za każde 30 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
259. [Status [MiddleFingerDaughter_Panic] — nazwa] 흥분
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaughter_Panic].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerDaughter_Panic]`
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Status [MiddleFingerDaughter_Panic] — opis] - 패닉\n턴 시작 시 공격 위력 증가 1,방어 레벨 감소 3를 얻고,\n이전 턴에 받은 체력 피해량 25당 피해량 증가 1을 얻음 (최대 5)
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFingerDaughter_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 1 Attack Power Up and 3 Defense Level Down; gain 1 Damage Up for every 25 HP damage taken last turn (max 5)
   PL: - Panika\nNa początku tury zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 25 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
261. [Status [HumanBoneTheRings] — nazwa] 생체 재료(뼈)
   źródło: Bufs-a1c9p3.json :: dataList[id=HumanBoneTheRings].name
   kontekst: identyfikator statusu w tekstach: `[HumanBoneTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient (Bones)
   PL: Materiał Biologiczny (Kość)
262. [Status [HumanBoneTheRings] — opis] - 최댓값: 206\n- 특수 충전 (위력 고정)
   źródło: Bufs-a1c9p3.json :: dataList[id=HumanBoneTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 206\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 206\n- Specjalny Ładunek (Siła zablokowana)
263. [Status [HumanBloodTheRings] — nazwa] 생체 재료(피)
   źródło: Bufs-a1c9p3.json :: dataList[id=HumanBloodTheRings].name
   kontekst: identyfikator statusu w tekstach: `[HumanBloodTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient (Blood)
   PL: Materiał Biologiczny (Krew)
264. [Status [HumanBloodTheRings] — opis] - 최댓값: 5\n- 특수 충전 (위력 고정)
   źródło: Bufs-a1c9p3.json :: dataList[id=HumanBloodTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 5\n- Specjalny Ładunek (Siła zblokowana)
265. [Status [LivingSpecimenTheRings] — nazwa] 신체관극
   źródło: Bufs-a1c9p3.json :: dataList[id=LivingSpecimenTheRings].name
   kontekst: identyfikator statusu w tekstach: `[LivingSpecimenTheRings]`
   limit: do 40 znaków
   EN: Corpus Theater
   PL: Teatr Ciała
266. [Status [LivingSpecimenTheRings] — opis] - 버프, 체력, 정신력이 갱신되지 않는 행동 불가능 상태가 되고, 이 캐릭터와 연결된 신체관극이 생성됨
   źródło: Bufs-a1c9p3.json :: dataList[id=LivingSpecimenTheRings].desc
   limit: do 170 znaków
   EN: - Enter an 'immobilized' state where this unit's buffs, HP, and SP cannot be changed. Forms a Corpus Theater connected to this unit
   PL: - Przechodzi w stan „Unieruchomienia”, w którym buffy, HP i Poczytalność nie mogą się zmieniać. Tworzy Teatr Ciała połączony z tą postacią
267. [Status [MineTheRings] — nazwa] 작품명: 티비아
   źródło: Bufs-a1c9p3.json :: dataList[id=MineTheRings].name
   kontekst: identyfikator statusu w tekstach: `[MineTheRings]`
   limit: do 40 znaków
   EN: Artwork: Tibia
   PL: Dzieło: Tibia
268. [Status [MineTheRings] — opis] - 턴 시작 시, 위력 증가 4, 참격 위력 증가 2 얻음\n- 공격 스킬로 출혈 부여 시, 출혈 위력 2 추가 부여
   źródło: Bufs-a1c9p3.json :: dataList[id=MineTheRings].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Power Up and 2 Slash Power Up\n- When inflicting Bleed with Attack Skills, inflict 2 more Bleed Potency
   PL: - Na początku tury zyskuje 4 Wzrost Mocy i 2 Wzrost Mocy Cięcia\n- Nakładając Krwawienie Umiejętnościami ataku, nakłada dodatkowo 2 Siły Krwawienia
269. [Status [ObservationTheRings] — nazwa] 조망
   źródło: Bufs-a1c9p3.json :: dataList[id=ObservationTheRings].name
   kontekst: identyfikator statusu w tekstach: `[ObservationTheRings]`
   limit: do 40 znaków
   EN: Viewing the Tableau
   PL: Podziwianie Tableau
270. [Status [ObservationTheRings] — opis] - 기본 공격 레벨 20 감소\n- 기본 방어 레벨 20 감소\n- 수감자 및 조력자의 퇴각 관련 기능이 작동하지 않음\n- 약지 제자가 전투 가능 상태면, 턴 시작 시 보호 7 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=ObservationTheRings].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -20\n- Base Defense Level -20\n- The Sinners & Assist Units' Retreat-related abilities do not activate\n- Turn Start: Gain 7 Protection if The Ring Apprentice has not retreated from this Encounter
   PL: - Podstawowy Poziom Ataku -20\n- Podstawowy Poziom Obrony -20\n- Funkcje wycofania Grzeszników i jednostek wsparcia nie działają\n- Jeżeli Uczeń Serdecznego jest gotów do walki, na początku tury zyskuje 7 Ochrony
271. [Status [ObservationTheRings] — tekst klimatyczny] “갤러리에서 작품을 감상할 때는 느긋하고 여유롭게. 서두르지 않는 것이 중요하답니다.”
   źródło: Bufs-a1c9p3.json :: dataList[id=ObservationTheRings].flavor
   limit: do 180 znaków
   EN: "The appreciation of artwork in a gallery calls for unhurried contemplation. Please remember—impatience dulls the appreciation of art."
   PL: „Podziwianie dzieł sztuki w galerii wymaga niespiesznej kontemplacji. Proszę pamiętać — niecierpliwość tępi wrażliwość na sztukę.”
272. [Status [RedemptionTheRings] — nazwa] 재료가 떨어지는 상처
   źródło: Bufs-a1c9p3.json :: dataList[id=RedemptionTheRings].name
   kontekst: identyfikator statusu w tekstach: `[RedemptionTheRings]`
   limit: do 40 znaków
   EN: Ingredient-shedding Wound
   PL: Rana Tracąca Materiał
273. [Status [RedemptionTheRings] — opis] 스킬 사용 시, 공격 레벨 감소 2 얻음 (턴당 최대 3회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RedemptionTheRings].desc
   limit: do 120 znaków
   EN: Gain 2 Offense Level Down when using a Skill (max 3 times per turn)
   PL: Przy użyciu Umiejętności zyskuje 2 Spadek Poziomu Ataku (maks. 3 razy na turę)
274. [Status [SpecimenTheRings] — nazwa] 전시회의 완성
   źródło: Bufs-a1c9p3.json :: dataList[id=SpecimenTheRings].name
   kontekst: identyfikator statusu w tekstach: `[SpecimenTheRings]`
   limit: do 40 znaków
   EN: The Exhibition is Complete!
   PL: Wystawa Gotowa!
275. [Status [SpecimenTheRings] — opis] 모든 수감자 및 조력자가 신체관극이 되면 전투에서 패배함
   źródło: Bufs-a1c9p3.json :: dataList[id=SpecimenTheRings].desc
   limit: do 120 znaków
   EN: Lose the Encounter when all Sinners and Assist Units fall under the effect of Corpus Theater
   PL: Walka kończy się porażką, gdy wszyscy Grzesznicy i jednostki wsparcia przechodzą w Teatr Ciała
276. [Status [SpecimenTheRings] — tekst klimatyczny] 모든 살과 근육이 있어야 할 그곳 그 제자리에.
   źródło: Bufs-a1c9p3.json :: dataList[id=SpecimenTheRings].flavor
   limit: do 130 znaków
   EN: That precise, delicate spot where all elements of flesh and muscles are arranged to perfection.
   PL: To precyzyjne, delikatne miejsce, gdzie każdy element mięśni i ciała zajmuje idealnie swoje miejsce.
277. [Status [KAmpouleA1C94TH] — nazwa] 비상용 K사 앰플
   źródło: Bufs-a1c9p3.json :: dataList[id=KAmpouleA1C94TH].name
   kontekst: identyfikator statusu w tekstach: `[KAmpouleA1C94TH]`
   limit: do 40 znaków
   EN: K Corp. Emergency Ampule
   PL: Awaryjna Ampułka K Corp.
278. [Status [KAmpouleA1C94TH] — opis] 자신을 제외한 아군이 생존했을 때, 자신의 체력이 0이 되는 피해를 받으면, 아래 효과 발동\n- 흐트러짐 상태면, 흐트러짐 상태 해제\n- 체력 전부 회복\n- 아군이 보유한 모든 비상용 K사 앰플 수치 1 감소\n- 이 효과는 인격/EGO 패시브로 체력이 1 미만으로 감소하지 않는 효과보다 우선적으로 발동함
   źródło: Bufs-a1c9p3.json :: dataList[id=KAmpouleA1C94TH].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If at least one ally other than this unit is alive, activate the following effects upon taking damage that would reduce this unit's HP to 0:\n- If Staggered, recover from Stagger\n- Fully heal HP\n- All allies lose 1 K Corp. Emergency Ampule\n- This effect activates before the "X does not reduce HP below 1" effects from Identities & E.G.O Passives
   PL: Gdy co najmniej 1 sojusznik poza tą jednostką żyje, a otrzymane obrażenia obniżyłyby jej HP do 0, działają następujące efekty\n- Jeżeli jest oszołomiona, wychodzi z Oszołomienia\n- Pełne leczenie HP\n- Wszyscy sojusznicy tracą 1 Ampułki Awaryjnej Korporacji K\n- Ten efekt działa przed efektami „X nie obniża HP poniżej 1” z Tożsamości i pasywnych E.G.O
279. [Status [LanternHohenheimBigBird] — nazwa] 램프
   źródło: Bufs-a1c9p3.json :: dataList[id=LanternHohenheimBigBird].name
   kontekst: identyfikator statusu w tekstach: `[LanternHohenheimBigBird]`
   limit: do 40 znaków
   EN: Lamp
   PL: Lampa
280. [Status [LanternHohenheimBigBird] — opis] - 최댓값: 20\n- 다음 턴에 수치 2당 속박 1 얻음 (최대 10)\n- 턴 종료 시 다음 턴에 (수치 / 자신의 슬롯 수)만큼 자신의 각 슬롯의 도발치 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=LanternHohenheimBigBird].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Gain 1 Bind for every 2 Stack next turn (max 10)\n- Turn End: Gain +(Stack / # of this unit's Slot) Aggro to each of this unit's Skill Slot next turn
   PL: - Maks. stosów: 20\n- W następnej turze zyskuje 1 Spętanie za każde 2 stosy (maks. 10)\n- Na koniec tury prowokacja każdego slotu rośnie o (stosy / liczba slotów tej jednostki) w następnej turze
281. [Status [DelusionHohenheimBigBird] — nazwa] 현혹
   źródło: Bufs-a1c9p3.json :: dataList[id=DelusionHohenheimBigBird].name
   kontekst: identyfikator statusu w tekstach: `[DelusionHohenheimBigBird]`
   limit: do 40 znaków
   EN: Dazzle
   PL: Omam
282. [Status [DelusionHohenheimBigBird] — opis] - 턴 시작 시 흐트러짐 상태가 아니면, 마지막 스킬 슬롯에 장착한 공격 스킬은 대상 변경 불가 스킬이 되고, 호엔하임을 우선 공격함\n- 효과가 발동된 턴 종료 시 효과 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=DelusionHohenheimBigBird].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: If this unit is not Staggered, the Attack Skill equipped in this unit's last Skill Slot prioritizes Hohenheim and cannot be redirected\n- This effect expires at the end of the turn it is activated
   PL: - Na początku tury, jeżeli nie jest oszołomiona, Umiejętność ataku w ostatnim slocie celuje priorytetowo w Hohenheima i nie może zmienić celu\n- Efekt znika na koniec tury, w której zadziałał
283. [Status [LvUpHohenheimBigBird] — nazwa] E.G.O 감응도 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird].name
   kontekst: identyfikator statusu w tekstach: `[LvUpHohenheimBigBird]`
   limit: do 40 znaków
   EN: E.G.O Attunement Boost
   PL: Wzrost Dostrojenia E.G.O
284. [Status [LvUpHohenheimBigBird] — opis] - 기본 공격 레벨 15 증가\n- 기본 방어 레벨 15 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +15\n- Base Defense Level +15
   PL: - Podstawowy Poziom Ataku +15\n- Podstawowy Poziom Obrony +15
285. [Status [LvUpHohenheimBigBird_Over] — nazwa] E.G.O 감응도 과잉
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].name
   kontekst: identyfikator statusu w tekstach: `[LvUpHohenheimBigBird_Over]`
   limit: do 40 znaków
   EN: E.G.O Attunement Overload
   PL: Przeciążenie Dostrojenia E.G.O
286. [Status [LvUpHohenheimBigBird_Over] — opis] - 기본 공격 레벨 15 증가\n- 기본 방어 레벨 15 증가\n- 턴 종료 시 램프를 20이 되도록 얻고, 얻은 수치 1당 체력 2, 정신력 1 소모 (이 효과로 체력이 1 미만이 되지 않음)
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +15\n- Base Defense Level +15\n- Turn End: Increase Lamp Stack to 20; lose 2 HP and 1 SP for every Stack gained (this effect does not reduce this unit's HP below 1)
   PL: - Podstawowy Poziom Ataku +15\n- Podstawowy Poziom Obrony +15\n- Na koniec tury podnosi Lampę do 20 stosów; traci 2 HP i 1 Poczytalności za każdy zdobyty stos (ten efekt nie obniża HP poniżej 1)
287. [Status [LvUpHohenheimBigBird_Over] — tekst klimatyczny] 추출된 E.G.O의 힘을 무리하게 끌어내고 있다.
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].flavor
   limit: do 120 znaków
   EN: Overdrawing the power of the Extracted E.G.O.
   PL: Bezwstydnie drenuje moc wyekstrahowanego E.G.O.
288. [Status [HohenheimBigBird_LowMorale] — nazwa] 쏟아지는 잠
   źródło: Bufs-a1c9p3.json :: dataList[id=HohenheimBigBird_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[HohenheimBigBird_LowMorale]`
   limit: do 40 znaków
   EN: Wave of Somnolence
   PL: Zalew Senności
289. [Status [HohenheimBigBird_LowMorale] — opis] - 사기 저하\n- 스킬로 얻는 램프 획득량 1 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=HohenheimBigBird_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 fewer Lamp from Skills
   PL: - Niskie Morale\n- Umiejętności zyskują o 1 mniej Lampy
290. [Status [HohenheimBigBird_Panic] — nazwa] 쏟아지는 잠
   źródło: Bufs-a1c9p3.json :: dataList[id=HohenheimBigBird_Panic].name
   kontekst: identyfikator statusu w tekstach: `[HohenheimBigBird_Panic]`
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Status [HohenheimBigBird_Panic] — opis] - 패닉\n- 한 턴 동안 행동하지 않음
   źródło: Bufs-a1c9p3.json :: dataList[id=HohenheimBigBird_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Does not act for this turn
   PL: - Panika\n- Nie działa przez tę turę
292. [Status [LvUpFireFly] — nazwa] E.G.O 감응도 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpFireFly].name
   kontekst: identyfikator statusu w tekstach: `[LvUpFireFly]`
   (powtórzenie elementu 283 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Status [LvUpFireFly] — opis] - 기본 공격 레벨 10 증가\n- 기본 방어 레벨 10 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpFireFly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +10\n- Base Defense Level +10
   PL: - Podstawowy Poziom Ataku +10\n- Podstawowy Poziom Obrony +10
294. [Status [LvUpFireFly_Over] — nazwa] E.G.O 감응도 과잉
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpFireFly_Over].name
   kontekst: identyfikator statusu w tekstach: `[LvUpFireFly_Over]`
   (powtórzenie elementu 285 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Status [LvUpFireFly_Over] — opis] - 기본 공격 레벨 10 증가\n- 기본 방어 레벨 10 증가\n- 턴 종료 시, 화상 4 얻음. 정신력 5 소모
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpFireFly_Over].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +10\n- Base Defense Level +10\n- Turn End: Gain 4 Burn and lose 5 SP
   PL: - Podstawowy Poziom Ataku +10\n- Podstawowy Poziom Obrony +10\n- Koniec tury: zyskuje 4 Podpalenia i traci 5 Poczytalności
296. [Status [LvUpFireFly_Over] — tekst klimatyczny] 추출된 E.G.O의 힘을 무리하게 끌어내고 있다.
   źródło: Bufs-a1c9p3.json :: dataList[id=LvUpFireFly_Over].flavor
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Status [LCEFireFly_LowMorale] — nazwa] 열화침식
   źródło: Bufs-a1c9p3.json :: dataList[id=LCEFireFly_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LCEFireFly_LowMorale]`
   limit: do 40 znaków
   EN: Degraded Corrosion
   PL: Zdegradowana Korozja
298. [Status [LCEFireFly_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 취약 1 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=LCEFireFly_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości
299. [Status [LCEFireFly_Panic] — nazwa] 열화침식
   źródło: Bufs-a1c9p3.json :: dataList[id=LCEFireFly_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LCEFireFly_Panic]`
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Status [LCEFireFly_Panic] — opis] - 패닉\n- 턴 시작 시 취약 1, 화상 5 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=LCEFireFly_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 1 Fragile and 5 Burn
   PL: - Panika\n- Na początku tury zyskuje 1 Wrażliwości i 5 Podpalenia
301. [Status [Cubism_LowMorale] — nazwa] 한물간 예술
   źródło: Bufs-a1c9p3.json :: dataList[id=Cubism_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Cubism_LowMorale]`
   limit: do 40 znaków
   EN: Outmoded Art
   PL: Przestarzała Sztuka
302. [Status [Cubism_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 1 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=Cubism_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku
303. [Status [Cubism_Panic] — nazwa] 한물간 예술
   źródło: Bufs-a1c9p3.json :: dataList[id=Cubism_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Cubism_Panic]`
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Status [Cubism_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 증가 2 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=Cubism_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Offense Level Up
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku
305. [Status [FutureEyeOn] — nazwa] 예지안
   źródło: Bufs-a1c9p3.json :: dataList[id=FutureEyeOn].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOn]`
   limit: do 40 znaków
   EN: Eye of Precognition
   PL: Oko Prekognicji
306. [Status [FutureEyeOn] — opis] - 최댓값: 30\n- 합 위력 +2\n- 턴 시작 시 10 증가\n- 턴 시작 시 (수치/4)만큼 정신력 회복
   źródło: Bufs-a1c9p3.json :: dataList[id=FutureEyeOn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Clash Power +2\n- Turn Start: Gain 10 Stack\n- Turn Start: Heal (Stack / 4) SP
   PL: - Maks. stosów: 30\n- Moc Starcia +2\n- Na początku tury rośnie o 10\n- Na początku tury odzyskuje (stosy / 4) Poczytalności
307. [Status [FutureEyeOn] — tekst klimatyczny] ‘마법처럼 미래를 보여 주는 건 아니다. 이 눈은 시야에 들어온 모든 것을 분석해 앞으로 다가올 찰나의 순간을 예측해 주는 계산기에 가깝다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=FutureEyeOn].flavor
   limit: do 290 znaków
   EN: "The eye does not possess some supernatural power that shows its user the destined future. It is more akin to a computing device that analyzes everything it sees and provides the most likely scenario in the upcoming instant."
   PL: „Nie jest to magia ukazująca przyszłość. To oko przypomina raczej kalkulator, który analizuje wszystko, co wpada w pole widzenia, i przewiduje ulotną chwilę, jaka ma nadejść.”
308. [Status [FutureEyeOff] — nazwa] 예지안 과열
   źródło: Bufs-a1c9p3.json :: dataList[id=FutureEyeOff].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOff]`
   limit: do 50 znaków
   EN: Eye of Precognition - Overheat
   PL: Oko Prekognicji - Przegrzanie
309. [Status [FutureEyeOff] — opis] - 최댓값: 30\n- 공격 스킬로 가하는 피해량 -20%\n- 가속탄을 소모하는 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 턴 시작 시 10 증가\n- 수치가 30이면, ‘예지안’으로 변환
   źródło: Bufs-a1c9p3.json :: dataList[id=FutureEyeOff].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Attack Skills deal -20% damage\n- Convert all Coins on Skills that spend Acceleration Round to Unbreakable Coins\n- Turn Start: Gain 10 Stack\n- At 30 Stack, convert into "Eye of Precognition"
   PL: - Maks.: 30\n- Umiejętności ataku zadają -20% obrażeń\n- Wszystkie monety Umiejętności zużywających Pocisk Przyspieszenia stają się Niezniszczalnymi Monetami\n- Na początek tury rośnie o 10\n- Przy wartości 30 zamienia się w 'Oko Prekognicji'
310. [Status [LookingFuture] — nazwa] 가속하는 미래
   źródło: Bufs-a1c9p3.json :: dataList[id=LookingFuture].name
   kontekst: identyfikator statusu w tekstach: `[LookingFuture]`
   limit: do 40 znaków
   EN: Accelerating Future
   PL: Przyspieszająca Przyszłość
311. [Status [LookingFuture] — opis] - 최댓값: 10\n- 수치 1당, 합 위력 +1\n- 수치 5당, 코인 위력 +1\n- 스킬 종료 시 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=LookingFuture].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Clash Power +1 for every Stack\n- Coin Power +1 for every 5 Stack\n- Expires at Skill End
   PL: - Maks. stosów: 10\n- Moc Starcia +1 za każdy stos\n- Moc Monety +1 za każde 5 stosów\n- Znika na koniec Umiejętności
312. [Status [LookingFuture] — tekst klimatyczny] 합을 더 오래, 더 많이 맞댈수록 팔레르모는 가속한다.
   źródło: Bufs-a1c9p3.json :: dataList[id=LookingFuture].flavor
   limit: do 120 znaków
   EN: The Palermitan Style is known to accelerate the longer a duel lasts.
   PL: Im dłużej i częściej toczy się Starcie, tym bardziej przyspiesza styl palermitański.
313. [Status [ObsessionAndGreed] — nazwa] 신(心) - 발렌치나
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessionAndGreed].name
   kontekst: identyfikator statusu w tekstach: `[ObsessionAndGreed]`
   limit: do 40 znaków
   EN: Shin (心) - Valencina
   PL: Shin (心) - Valencina
314. [Status [ObsessionAndGreed] — opis] - 이전 턴에 합 패배한 횟수만큼 방어 레벨 +3 (최대 6)\n자신의 호흡 위력 1당, 가하는 피해량 +3% (최대 15%)
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessionAndGreed].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3 for every instance of Clash Lose in the last turn (max 6)\n- Deal +3% damage for every Poise Potency on self (max 15%)
   PL: - Poziom Obrony +3 za każdą przegraną w Starciu w poprzedniej turze (maks. 6)\nZadaje +3% obrażeń za każdą Siłę Oddechu (maks. 15%)
315. [Status [AccelBullet] — nazwa] 가속탄
   źródło: Bufs-a1c9p3.json :: dataList[id=AccelBullet].name
   kontekst: identyfikator statusu w tekstach: `[AccelBullet]`
   limit: do 40 znaków
   EN: Acceleration Round
   PL: Pocisk Przyspieszenia
316. [Status [AccelBullet] — opis] - 최댓값: 10\n- 특수 탄환\n- 특정 스킬 사용 시 소모
   źródło: Bufs-a1c9p3.json :: dataList[id=AccelBullet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Capacity: 10\n- Unique Ammo\n- Spent by certain Skills
   PL: - Maks. pojemności: 10\n- Specjalna amunicja\n- Zużywany przy użyciu określonych Umiejętności
317. [Status [TeachersPrey] — nazwa] 사냥 표적
   źródło: Bufs-a1c9p3.json :: dataList[id=TeachersPrey].name
   kontekst: identyfikator statusu w tekstach: `[TeachersPrey]`
   limit: do 40 znaków
   EN: Game Target
   PL: Cel Polowania
318. [Status [TeachersPrey] — opis] 속도가 1로 고정되며, ‘엄지 아비 - 발렌치나’ 모든 공격 스킬의 타겟으로 지정됨
   źródło: Bufs-a1c9p3.json :: dataList[id=TeachersPrey].desc
   limit: do 140 znaków
   EN: Fix this unit's Speed to 1; all Attack Skills of "The Thumb Nursefather - Valencina" targets this unit
   PL: Szybkość zostaje zablokowana na 1; wszystkie Umiejętności ataku „Ojca Kciuka - Valenciny” celują w tę jednostkę
319. [Status [TeachersPrey] — tekst klimatyczny] 보냐텔리 가의 표적이 되었다면 사냥은 피할 수 없다.
   źródło: Bufs-a1c9p3.json :: dataList[id=TeachersPrey].flavor
   limit: do 120 znaków
   EN: Prey marked by Famiglia Bognatelli will be hunted down without fail.
   PL: Kto raz stanie się celem rodu Bognatellich, nie uniknie polowania.
320. [Status [AaCfPcBiv2] — nazwa] 고열기전
   źródło: Bufs-a1c9p3.json :: dataList[id=AaCfPcBiv2].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBiv2]`
   limit: do 40 znaków
   EN: Superthermogenesis
   PL: Nadtermogeneza
321. [Status [AaCfPcBiv2] — opis] 턴 종료 시 수치에 비례하여 최대 체력의 (수치*0.5)%만큼 고정 피해를 받고 효과 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=AaCfPcBiv2].desc
   limit: do 120 znaków
   EN: Turn End: Take fixed damage equal to (Stack x 0.5)% of Max HP, then the effect expires
   PL: Na koniec tury otrzymuje obrażenia stałe równe (stosy x 0,5)% Maks. HP, po czym efekt znika
322. [Status [VergiliusSin] — nazwa] 신(心) - 붉은시선
   źródło: Bufs-a1c9p3.json :: dataList[id=VergiliusSin].name
   kontekst: identyfikator statusu w tekstach: `[VergiliusSin]`
   limit: do 40 znaków
   EN: Shin (心) - The Red Gaze
   PL: Shin (心) - Czerwone Spojrzenie
323. [Status [VergiliusSin] — opis] 분노 속성의 가하는 피해량 +50%
   źródło: Bufs-a1c9p3.json :: dataList[id=VergiliusSin].desc
   limit: do 120 znaków
   EN: Deal +50% Wrath damage
   PL: Zadaje +50% obrażeń Gniewu
324. [Status [VergiliusSin] — podsumowanie] 피해량 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=VergiliusSin].summary
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
325. [Status [BloodBranch] — nazwa] 망혈[盲血]
   źródło: Bufs-a1c9p3.json :: dataList[id=BloodBranch].name
   kontekst: identyfikator statusu w tekstach: `[BloodBranch]`
   limit: do 40 znaków
   EN: Blinding Blood [盲血]
   PL: Zaślepiająca Krew [盲血]
326. [Status [BloodBranch] — opis] 수치 1당, 다음 턴에 속박 1 얻음\n턴 종료 시 자신의 (출혈 위력 x 수치) 만큼 체력 피해를 입음\n전투 시작 시 수치 1당, 출혈 3 얻고 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=BloodBranch].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 1 Bind next turn for every Stack\nTurn End: Take (Bleed Potency x Stack) HP damage\nCombat Start: Gain 3 Bleed for every Stack, then expire
   PL: Zyskuje 1 Spętanie w następnej turze za każdy stos\nNa koniec tury otrzymuje (Siła Krwawienia x stosy) obrażeń HP\nNa początku walki zyskuje 3 Krwawienia za każdy stos, po czym znika
327. [Status [BloodBranch] — tekst klimatyczny] “피를 시선에 담아낼 수만 있다면, 모으고 응축해서 꿰뚫을 수 있어. 물론 눈을 멀게도 할 수 있을 거야.”
   źródło: Bufs-a1c9p3.json :: dataList[id=BloodBranch].flavor
   limit: do 190 znaków
   EN: "If blood can be contained within a gaze, it can also be accumulated and condensed for piercing. It can also, of course, be used to blind. Okay?"
   PL: „Jeżeli krew da się uwięzić w spojrzeniu, można ją też zgromadzić, skondensować i przebić nią wszystko. A nawet oślepić. Dobrze?”
328. [Status [Gebura_Reinforcement] — nazwa] 게부라의 칼날
   źródło: Bufs-a1c9p3.json :: dataList[id=Gebura_Reinforcement].name
   kontekst: identyfikator statusu w tekstach: `[Gebura_Reinforcement]`
   limit: do 40 znaków
   EN: Gebura's Blade
   PL: Ostrze Gebury
329. [Status [Gebura_Reinforcement] — opis] - 모든 스킬 코인이 파괴 불가 코인으로 변경됨\n- 피해량 +100%\n- 더하기 코인 스킬인 경우, 코인 위력 +1, 빼기 코인 스킬인 경우, 최종 위력 +1\n- 이번 턴에 모든 피해로 흐트러짐 상태가 되지 않음\n- 자신의 체력이 10 이하면, 10으로 회복함\n- 이번 턴 동안 피해로 인해 체력이 10 미만으로 감소하지 않음\n- 이번 턴동안 기본 공격 스킬과 반격 스킬의 코인 적중시 피해량의 10%만큼 체력 회복 (스킬당 최대 회복량 : 100) \n- 턴 종료시 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=Gebura_Reinforcement].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Convert all Skill Coins into Unbreakable Coins\n- Deal +100% damage\n- Plus Coin Skills gain Coin Power +1; Minus Coin Skills gain Final Power +1\n- For this turn, this unit cannot be Staggered from all sources of damage\n- At less than 10 HP, heal to 10 HP\n- For this turn, this unit's HP does not drop below 10\n- For this turn, every Coin Hit from Base Attack Skills and Counter Skills heals 10% of the damage dealt (max healing from each Skill: 100)\n- Expires at Turn End
   PL: - Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Zadaje +100% obrażeń\n- Umiejętności z Monetami Plus zyskują Moc Monety +1; Umiejętności z Monetami Minus zyskują Moc Końcowa +1\n- W tej turze nie przechodzi w Oszołomienie od żadnych obrażeń\n- Przy HP poniżej 10 leczy do 10 HP\n- W tej turze HP nie spada poniżej 10\n- W tej turze każde trafienie Monetą podstawowej Umiejętności ataku i Kontrą leczy 10% zadanych obrażeń (maks. leczenia na Umiejętność: 100)\n- Znika na koniec tury
330. [Status [Gebura_Reinforcement] — podsumowanie] 게부라의 칼날 효과 적용
   źródło: Bufs-a1c9p3.json :: dataList[id=Gebura_Reinforcement].summary
   limit: do 120 znaków
   EN: Gebura's Blade activated
   PL: Aktywne efekty Ostrza Gebury
331. [Status [ThreeMirrorpartYiSang] — nazwa] 깨어진 세계
   źródło: Bufs-a1c9p3.json :: dataList[id=ThreeMirrorpartYiSang].name
   kontekst: identyfikator statusu w tekstach: `[ThreeMirrorpartYiSang]`
   limit: do 40 znaków
   EN: Shattered World
   PL: Rozbity Świat
332. [Status [ThreeMirrorpartYiSang] — opis] - 최댓값: 1\n- 턴 종료시 소멸\n- 화상으로 받는 피해 1.2배 (소수점 버림, 특수 화상 제외)\n- 이상의 분노 속성과 우울 속성 기본 공격 스킬로 받는 피해량 +10%
   źródło: Bufs-a1c9p3.json :: dataList[id=ThreeMirrorpartYiSang].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Expires at Turn End\n- Take x1.2 damage from Burn (rounded down; except Unique Burn)\n- Take +10% damage from Yi Sang's Wrath and Gloom Base Attack Skills
   PL: - Maks. stosów: 1\n- Znika na koniec tury\n- Otrzymuje x1,2 obrażeń od Podpalenia (zaokrąglone w dół; poza Specjalnym Podpaleniem)\n- Otrzymuje +10% obrażeń od podstawowych ataków Yisanga z Gniewu i Posępności
333. [Status [RyoshuEGOPF] — nazwa] 나생[羅生]
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuEGOPF].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuEGOPF]`
   limit: do 40 znaków
   EN: Entangled Life [羅生]
   PL: Splecione Życie [羅生]
334. [Status [RyoshuEGOPF] — opis] 최댓값 : 999\n- 료슈가 가한 스킬 피해 1당 수치 1 증가\n- 수치 33당 기본 스킬 피해량 1% 증가 (최대 10%)
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuEGOPF].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 999\n- Gain 1 Stack for every HP damage dealt by Ryōshū's Skills\n- Deal +1% damage with Base Skills for every 33 Stack (max 10%)
   PL: Maks. stosów: 999\n- Zyskuje 1 stos za każde 1 obrażeń HP zadanych Umiejętnościami Ryōshū\n- Podstawowe Umiejętności zadają +1% obrażeń za każde 33 stosy (maks. 10%)
335. [Status [RyoshuEGOPF] — tekst klimatyczny] ‘꼬일 대로 꼬이고 꼬여, 엮여 만들어진 번데기. 실.삶.세상.’
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuEGOPF].flavor
   limit: do 120 znaków
   EN: 'Twisted and entangled beyond measure, bound and woven into a cocoon. Thread. Life. World.'
   PL: „Zwinięta i spleciona ponad miarę, uwiązana i utkana w kokon. Nić. Życie. Świat.”
336. [Status [OffenseBug] — nazwa] 공격 해충[바퀴]
   źródło: Bufs-a1c9p3.json :: dataList[id=OffenseBug].name
   kontekst: identyfikator statusu w tekstach: `[OffenseBug]`
   limit: do 40 znaków
   EN: Hurting Pest [Roaches]
   PL: Szkodnik Ataku [Karaluchy]
337. [Status [OffenseBug] — opis] - 최댓값: 50\n- 최대 체력이 수치당 1%씩 감소\n- 전투 시작 시 (수치x12)만큼 고정 피해를 입음\n- 수치가 감소 될 시, 감소된 수치만큼 무작위 E.G.O 자원을 얻음 (최대 15)
   źródło: Bufs-a1c9p3.json :: dataList[id=OffenseBug].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Lose 1% max HP per Stack\n- Combat Start: Take (Stack x 12) fixed damage\n- Whenever this unit loses Stack of this effect, gain E.G.O resources of random Affinities equal to Stack lost (max 15)
   PL: - Maks. stosów: 50\n- Maks. HP maleje o 1% za każdy stos\n- Na początku walki otrzymuje (stosy x 12) obrażeń stałych\n- Przy utracie stosów zyskuje losowe Zasoby E.G.O w liczbie utraconych stosów (maks. 15)
338. [Status [OffenseBug] — tekst klimatyczny] ‘해충이라 불리는 것 중에서 이것이 제일이다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=OffenseBug].flavor
   limit: do 120 znaków
   EN: "This creature is unmatched among those scorned as pests."
   PL: „Wśród istot zwanych szkodnikami ten jest niepokonany.”
339. [Status [DefenseBug] — nazwa] 방어 해충[바퀴]
   źródło: Bufs-a1c9p3.json :: dataList[id=DefenseBug].name
   kontekst: identyfikator statusu w tekstach: `[DefenseBug]`
   limit: do 40 znaków
   EN: Protecting Pest [Roaches]
   PL: Szkodnik Obrony [Karaluchy]
340. [Status [DefenseBug] — opis] - 최댓값: 50\n- 자신에게 (화상, 출혈, 진동, 파열, 침잠)의 위력 또는 횟수가 부여될 시, 부여될 효과의 수치만큼 감소하고, 해당 효과를 부여받지 않음\n- 턴 종료시 소멸
   źródło: Bufs-a1c9p3.json :: dataList[id=DefenseBug].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Whenever this unit is inflicted with (Burn, Bleed, Tremor, Rupture, Sinking) Potency or Count, instead of gaining those effects, lose the same amount of Stack of this effect instead\n- Expires at Turn End
   PL: - Maks. stosów: 50\n- Gdy zostają nałożone Siła lub Licznik (Podpalenia, Krwawienia, Wstrząsu, Rozdarcia, Zatonięcia), zamiast zdobywania efektu traci równą liczbę stosów tego efektu\n- Znika na koniec tury
341. [Status [DefenseBug] — tekst klimatyczny] ‘하나하나가 해롭고 징그럽고 질기다’
   źródło: Bufs-a1c9p3.json :: dataList[id=DefenseBug].flavor
   limit: do 120 znaków
   EN: "They are baleful and stubborn, not to mention tenacious."
   PL: „Każdy jest zdradliwy, ohydny i uporczywy.”
342. [Status [LvDownLittleFingerBossTwo] — nazwa] 천살성상[天殺星傷]
   źródło: Bufs-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].name
   kontekst: identyfikator statusu w tekstach: `[LvDownLittleFingerBossTwo]`
   limit: do 50 znaków
   EN: Tiansha Star's Bladewound [天殺星傷]
   PL: Rana Ostrza Gwiazdy Tiansha [天殺星傷]
343. [Status [LvDownLittleFingerBossTwo] — opis] - 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -15\n- Base Defense Level -15
   PL: - Podstawowy Poziom Ataku -15\n- Podstawowy Poziom Obrony -15
344. [Status [LvDownLittleFingerBossTwo] — podsumowanie] 기본 공격, 방어 레벨 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].summary
   limit: do 120 znaków
   EN: - Lose Base Offense and Base Defense Level
   PL: - Traci Podstawowy Poziom Ataku i Podstawowy Poziom Obrony
345. [Status [LvDownLittleFingerBossTwo] — tekst klimatyczny] 천살성도 - 아라야시키로 벤 것에는 타오르는 듯한 검흔이 남는다. 이 검흔은 어떤 방법으로도 사라지지 않는다.\n휘두른 자의 존재를 대가로 상대의 존재도 베어낸 것이기에.
   źródło: Bufs-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].flavor
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A cut from the Tiansha Star's Blade - Arayashiki leaves a blade wound that seems to burn with implacable fire.\nThis burning mark can never fade, for the wielder has slashed through the existence of their opponent at the cost of their own.
   PL: Cięcie Ostrzem Gwiazdy Tiansha - Arayashiki zostawia ranę płonącą jak nieugaszony żar.\nTen znak nigdy nie zblednie, bo zadający poświęcił własną egzystencję, by przeciąć egzystencję przeciwnika.
346. [Status [SojiAbiAgePast] — nazwa] 역행 - 미움
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgePast].name
   kontekst: identyfikator statusu w tekstach: `[SojiAbiAgePast]`
   limit: do 40 znaków
   EN: Backward Flow - Bitterness
   PL: Prąd Wstecz - Gorycz
347. [Status [SojiAbiAgePast] — opis] - 최댓값 : 20\n- 수치당 가하는 피해량, 받는 피해량 +2%
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgePast].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal and take +2% damage for every Stack
   PL: - Maks. stosów: 20\n- Zadaje i otrzymuje +2% obrażeń za każdy stos
348. [Status [SojiAbiAgePast] — podsumowanie] 가하는 피해량, 받는 피해량 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgePast].summary
   limit: do 120 znaków
   EN: Deal and take more damage
   PL: Zadaje i otrzymuje więcej obrażeń
349. [Status [SojiAbiAgePast] — tekst klimatyczny] ‘나를 잊어 버리고 간 기억이 매듭처럼 끊어지지가 않아.’
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgePast].flavor
   limit: do 160 znaków
   EN: 'The memory of being forgotten and abandoned by you refuses to let go... like a stubborn knot of thread that clings.'
   PL: „Wspomnienie, w którym odszedłeś i zapomniałeś o mnie, tkwi jak węzeł, którego nie da się przeciąć.”
350. [Status [SojiAbiAgeFuture] — nazwa] 순행 - 연민
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].name
   kontekst: identyfikator statusu w tekstach: `[SojiAbiAgeFuture]`
   limit: do 40 znaków
   EN: Forward Flow - Compassion
   PL: Prąd Naprzód - Współczucie
351. [Status [SojiAbiAgeFuture] — opis] - 최댓값 : 20\n- 수치당 가하는 피해량, 받는 피해량 -2%
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal and take -2% damage for every Stack
   PL: - Maks. stosów: 20\n- Zadaje i otrzymuje -2% obrażeń za każdy stos
352. [Status [SojiAbiAgeFuture] — podsumowanie] 가하는 피해량, 받는 피해량 감소
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].summary
   limit: do 120 znaków
   EN: Deal and take less damage
   PL: Zadaje i otrzymuje mniej obrażeń
353. [Status [SojiAbiAgeFuture] — tekst klimatyczny] ‘당신을 이해하고 안아줄 수 있을지도 모르겠다는 생각을 하게 된 건, 시간이 지나 나이가 들었기 때문일까.’
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].flavor
   limit: do 170 znaków
   EN: 'Perhaps it was the passage of time and the years weighing on me that led me to believe I could finally understand and embrace you.'
   PL: „Może dlatego, że czas płynął i zebrałem się w latach, zaczęło mi się wydawać, że mógłbym cię zrozumieć i przyjąć.”
354. [Status [TimeEntangleUnstable] — nazwa] 폭주 - 잔상 얽힘
   źródło: Bufs-a1c9p3.json :: dataList[id=TimeEntangleUnstable].name
   kontekst: identyfikator statusu w tekstach: `[TimeEntangleUnstable]`
   limit: do 50 znaków
   EN: Paroxysm - Afterimage Entanglement
   PL: Paroksyzm - Splot Powideł
355. [Status [TimeEntangleUnstable] — opis] - 최댓값 : 10\n- 자신의 공격 적중시 수치에 따라 아래 효과 적용\n  · (해당 코인 최종 피해량 / 10)만큼 참격 피해 (수치만큼 발동)\n  · 2 이상 : 화상 1 부여\n  · 3 이상 : 출혈 1 부여\n  · 4 이상 : 다음 턴에 속박 1 부여\n  · 5 이상 : 독 1 부여
   źródło: Bufs-a1c9p3.json :: dataList[id=TimeEntangleUnstable].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- On Hit, activate the following effects based on Stack:\n  · Deal Slash damage equal to (final damage of the Coin / 10) (activates (# of Stack) times)\n  · 2+: Inflict 1 Burn\n  · 3+: Inflict 1 Bleed\n  · 4+: Inflict 1 Bind next turn\n  · 5+: Inflict 1 Poison
   PL: - Maks. stosów: 10\n- Przy trafieniu działają następujące efekty zależnie od stosów:\n  · Zadaje obrażenia Cięcia równe (ostateczne obrażenia Monety / 10) (działa tyle razy, ile stosów)\n  · 2+: nakłada 1 Podpalenie\n  · 3+: nakłada 1 Krwawienie\n  · 4+: nakłada 1 Spętanie w następnej turze\n  · 5+: nakłada 1 Zatrucia
356. [Status [TimeEntangleUnstable] — podsumowanie] 버프 수치에 따라 공격에 추가 효과 적용
   źródło: Bufs-a1c9p3.json :: dataList[id=TimeEntangleUnstable].summary
   limit: do 120 znaków
   EN: Apply additional effects to this unit's attacks based on Stack
   PL: Nakłada dodatkowe efekty na ataki zależnie od liczby stosów
357. [Status [WillAwakenSinclair] — nazwa] 신(心) - 어느 싱클레어
   źródło: Bufs-a1c9p3.json :: dataList[id=WillAwakenSinclair].name
   kontekst: identyfikator statusu w tekstach: `[WillAwakenSinclair]`
   limit: do 50 znaków
   EN: Shin (心) - A Certain Sinclair
   PL: Shin (心) - Pewien Sinclair
358. [Status [WillAwakenSinclair] — opis] - 속도 최솟값, 최댓값 3 증가\n- 일방 공격으로 가하는 피해량 +20%\n- 자신의 스킬로 얻는 호흡 위력 +2, 호흡 횟수 +1\n- 정신력이 20 이상이면, 더하기 코인 앞면 나올 확률 +10%\n- 턴 종료 시 정신력 10당, 다음 턴에 신속 1 얻음 (최대 4)\n- 턴 종료 시 정신력 20당, 다음 턴에 위력 증가 1 얻음 (최대 2)
   źródło: Bufs-a1c9p3.json :: dataList[id=WillAwakenSinclair].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Deal +20% damage with Unopposed Attack\n- Gain 2 more Poise Potency and +1 more Poise Count from Skills\n- At 20+ SP, +10% chance to flip Heads for Plus Coins\n- Turn End: Gain 1 Haste next turn for every 10 SP (max 4)\n- Turn End: Gain 1 Power Up next turn for every 20 SP (max 2)
   PL: - Min. i Maks. Szybkość +3\n- Zadaje +20% obrażeń Atakami Jednostronnymi\n- Umiejętności zyskują +2 Siły Oddechu i +1 Licznika Oddechu\n- Przy Poczytalności 20+: +10% szans na Awers dla Monet Plus\n- Na koniec tury zyskuje 1 Pośpiech w następnej turze za każde 10 Poczytalności (maks. 4)\n- Na koniec tury zyskuje 1 Wzrost Mocy w następnej turze za każde 20 Poczytalności (maks. 2)
359. [Status [SignAwakenSinclair] — nazwa] 표지 - 미래현현
   źródło: Bufs-a1c9p3.json :: dataList[id=SignAwakenSinclair].name
   kontekst: identyfikator statusu w tekstach: `[SignAwakenSinclair]`
   limit: do 50 znaków
   EN: Sign - Manifestation of the Future
   PL: Znak - Manifestacja Przyszłości
360. [Status [SignAwakenSinclair] — opis] - 자신보다 레벨이 높은 적과 합 진행 시, 합 위력 +2\n- 턴 종료 시, 흐트러짐 상태면 다음 턴에 흐트러짐 상태를 해제함
   źródło: Bufs-a1c9p3.json :: dataList[id=SignAwakenSinclair].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Clashing against higher-level targets, Clash Power +2\n- Turn End: If Staggered, recover from Stagger next turn
   PL: - W Starciu z celami o wyższym poziomie Moc Starcia +2\n- Na koniec tury, jeżeli jest oszołomiony, w następnej turze wychodzi z Oszołomienia
361. [Status [SignAwakenSinclair] — tekst klimatyczny] Abraxas
   źródło: Bufs-a1c9p3.json :: dataList[id=SignAwakenSinclair].flavor
   limit: do 120 znaków
   EN: Abraxas
   PL: Abraxas
362. [Status [LimitedAwakenSinclair] — nazwa] 움브라 금제 해제
   źródło: Bufs-a1c9p3.json :: dataList[id=LimitedAwakenSinclair].name
   kontekst: identyfikator statusu w tekstach: `[LimitedAwakenSinclair]`
   limit: do 40 znaków
   EN: Umbra Unsealed
   PL: Odpięczętowana Umbra
363. [Status [LimitedAwakenSinclair] — opis] - 기본 공격 스킬로 가하는 피해량 +10%\n- 턴 시작 시, 더하기 코인 강화 1 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=LimitedAwakenSinclair].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage with Base Attack Skills\n- Turn Start: Gain 1 Plus Coin Boost
   PL: - Podstawowe Umiejętności ataku zadają +10% obrażeń\n- Na początku tury zyskuje 1 Wzmocnienia Monet Plus
364. [Status [Veteran_LowMorale] — nazwa] 제 2차 연기전쟁의
   źródło: Bufs-a1c9p3.json :: dataList[id=Veteran_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Veteran_LowMorale]`
   limit: do 40 znaków
   EN: Of the Second Smoke War
   PL: Drugiej Wojny Dymnej
365. [Status [Veteran_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 취약 1 얻음\n- 정신력 회복 효율 +2
   źródło: Bufs-a1c9p3.json :: dataList[id=Veteran_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile\n- SP Heal Efficiency +2
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości\n- Efektywność Leczenia Poczytalności +2
366. [Status [Veteran_Panic] — nazwa] 제 2차 연기전쟁의
   źródło: Bufs-a1c9p3.json :: dataList[id=Veteran_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Veteran_Panic]`
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Status [Veteran_Panic] — opis] - 패닉\n- 턴 시작 시, 취약 2, 합 위력 증가 2 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=Veteran_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Fragile and 2 Clash Power Up
   PL: - Panika\n- Na początku tury zyskuje 2 Wrażliwości i 2 Wzrostu Mocy Starcia
368. [Status [MiddleFatherSwordOne] — nazwa] 봉인된 검
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordOne]`
   limit: do 40 znaków
   EN: Sealed Sword
   PL: Pieczętowany Miecz
369. [Status [MiddleFatherSwordOne] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].desc
   limit: do 120 znaków
   EN: Unlocks access to certain Skills based on the state of the sword.
   PL: Otwiera dostęp do określonych Umiejętności zależnie od stanu miecza.
370. [Status [MiddleFatherSwordOne] — tekst klimatyczny] 우애 좋은 세 남매는 유적 깊은 곳으로 향했다
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].flavor
   limit: do 120 znaków
   EN: A trio of tight-knit siblings together journeyed into the depths of the Ruins.
   PL: Zgodne rodzeństwo wyruszyło w głębiny ruin.
371. [Status [MiddleFatherSwordTwo] — nazwa] 1단계 봉인 해제
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordTwo]`
   limit: do 40 znaków
   EN: First Seal Removed
   PL: Zdjęta Pierwsza Pieczęć
372. [Status [MiddleFatherSwordTwo] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Status [MiddleFatherSwordTwo] — tekst klimatyczny] 도착한 곳은, 뜨겁고 이글거리는 용암 위로 빌딩이 떠다니는 동굴이었다.\n열기의 근원에는 어느 검… 아니, 검이라 부르기도 힘든 이글거리는 쇳덩어리가 놓여 있었다.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There, they came upon a sweltering cavern where a river of lava flowed, carrying buildings on its currents.\nThey traced the river to the source of its heat, and found a sword... that could hardly be called a sword. It was more like a hunk of white-hot metal.
   PL: Znaleźli się w piekącej jaskini, gdzie po płynącej lawie dryfowały budynki.\nU źródła żaru leżał miecz... a raczej kawał białego gorącego metalu, którego nie dało się nazwać mieczem.
374. [Status [MiddleFatherSwordThree] — nazwa] 2단계 봉인 해제
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordThree]`
   limit: do 40 znaków
   EN: Second Seal Removed
   PL: Zdjęta Druga Pieczęć
375. [Status [MiddleFatherSwordThree] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Status [MiddleFatherSwordThree] — tekst klimatyczny] “이 검은 제일 형님인 내가 가져가마.”\n그 말을 들은 한 아우는 타오르는 욕망과 질투를 참을 수 없었다.\n\n형님과 누님을 죽이고 검을 취했다. 어떤 흔적도 남지 않았겠지.\n하지만 의심받았고, 저항 없이 나락에 떨어졌다.\n그래도 웃음을 잃지 않았다. \n이 전설의 검은 내 것이니까.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].flavor
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "As the eldest brother, I claim this sword as mine."\nThe eldest brother's declaration sparked the inappeasable flame of desire and envy in the youngest brother.\n\nSo, I killed my brother and sister both, and took the sword as my own. I left no evidence behind.\nBut the eyes still gazed upon me with doubt, and when they cast me into this hell, I fell without resistance.\nStill, I did not lose my smile.\nFor the sword of legends was mine.
   PL: „Jako najstarszy brat wezmę ten miecz dla siebie.”\nTe słowa rozpaliły w najmłodszym nieugaszoną pożądanie i zazdrość.\n\nZabiłem więc brata i siostrę, i wziąłem miecz. Ani śladu.\nLecz oczy patrzyły z podejrzeniem, a gdy wtrącili mnie do tego piekła, spadłem bez oporu.\nMimo to nie straciłem uśmiechu.\nBo miecz legend był mój.
377. [Status [MiddleFatherSwordFour] — nazwa] 레바테인
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordFour]`
   limit: do 40 znaków
   EN: Lævateinn
   PL: Lævateinn
378. [Status [MiddleFatherSwordFour] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.\n턴 시작 시 모든 캐릭터에게 화상 5 부여, 화상 횟수 2 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unlocks access to certain Skills based on the state of the sword.\nTurn Start: Inflict 5 Burn and +2 Burn Count against all units
   PL: Otwiera dostęp do określonych Umiejętności zależnie od stanu miecza.\nNa początku tury nakłada 5 Podpalenia i +2 Licznika Podpalenia na wszystkie postacie
379. [Status [MiddleFatherSwordFour] — tekst klimatyczny] 안타깝게도 마티아스는 이 검을 제대로 다루지 못했다.\n물론 보통의 사람들은 쥘 수조차 없을 만큼, 까다로운 유물이다.\n그저 쥐고 휘두르기엔 충분했으나, 온전히 다루기에는 적성이 모자랐을 뿐.\n하지만 그에겐 상관 없었다.\n어릴 적부터 꿈꿔왔던 전설의 검을, 자신이 소유하고 휘두를 수 있다는 게 중요했으니.
   źródło: Bufs-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].flavor
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ironically, the blade was beyond Matthias's ability to properly wield.\nOf course, he would not have been able to hold this sword at all had he not the aptitude for it. It was simply that fickle of a Relic.\nThe truth of the matter was, nevertheless, that his aptitude was nowhere near enough to handle the weapon to its fullest potential.\nBut the man was unconcerned.\nAll that mattered was that the selfsame sword of legends he had dreamed of wielding since childhood was now in his possession, to be swung at his whim.
   PL: Ironia losu: to ostrze przerastało umiejętności Matthiasa.\nOczywiście, bez odpowiedniej predyspozycji nie zdołałby go nawet podnieść — tak wybredny jest ten Relikt.\nPrawda była jednak taka, że jego talent był zbyt mały, by w pełni panować nad bronią.\nAle to człowieka nie obchodziło.\nLiczyło się tylko to, że legendarny miecz, o którym marzył od dzieciństwa, należał teraz do niego i mógł nim machać do woli.
380. [Status [SojiAbiBuffOne] — nazwa] 계명(雞鳴)
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffOne].name
   kontekst: identyfikator statusu w tekstach: `[SojiAbiBuffOne]`
   limit: do 40 znaków
   EN: Dawn's First Crow (雞鳴)
   PL: Świt Koguta (雞鳴)
381. [Status [SojiAbiBuffOne] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffOne].desc
   limit: do 120 znaków
   EN: Able to Clash with the enemy's specific Slot
   PL: Możliwe Starcie z określonym slotem wroga
382. [Status [SojiAbiBuffTwo] — nazwa] 일입(日入)
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffTwo].name
   kontekst: identyfikator statusu w tekstach: `[SojiAbiBuffTwo]`
   limit: do 40 znaków
   EN: The Sun's Descent (日入)
   PL: Zachód Słońca (日入)
383. [Status [SojiAbiBuffTwo] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffTwo].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Status [SojiAbiBuffThree] — nazwa] 황혼(黃昏)
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffThree].name
   kontekst: identyfikator statusu w tekstach: `[SojiAbiBuffThree]`
   limit: do 40 znaków
   EN: Eventide Glow (黃昏)
   PL: Zmierzch (黃昏)
385. [Status [SojiAbiBuffThree] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: Bufs-a1c9p3.json :: dataList[id=SojiAbiBuffThree].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Status [RyoshuParrySojiTwo] — nazwa] 끊어지지 않은 기억
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParrySojiTwo]`
   limit: do 40 znaków
   EN: Unsevered Memory
   PL: Niedocięte Wspomnienie
387. [Status [RyoshuParrySojiTwo] — opis] - 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음\n- 퇴각 불가능
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn\n- Cannot Retreat
   PL: - Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku\n- Wycofanie niemożliwe
388. [Status [RyoshuParrySojiTwo] — podsumowanie] 료슈 특수 효과
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].summary
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Status [RyoshuParrySojiThree] — nazwa] 끊어지지 않는 시간
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParrySojiThree]`
   limit: do 40 znaków
   EN: Unseverable Time
   PL: Niedocięty Czas
390. [Status [RyoshuParrySojiThree] — opis] - 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능 (아군 포함)
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat (including allies)
   PL: - Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe (w tym sojuszników)
391. [Status [RyoshuParrySojiThree] — podsumowanie] 료슈 특수 효과
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].summary
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Status [HeavenlyKillerStar] — nazwa] 천살성도 - 아라야시키 [天殺星刀阿賴耶識]
   źródło: Bufs-a1c9p3.json :: dataList[id=HeavenlyKillerStar].name
   kontekst: identyfikator statusu w tekstach: `[HeavenlyKillerStar]`
   limit: do 60 znaków
   EN: Tiansha Star's Blade - Arayashiki [天殺星刀阿賴耶識]
   PL: Ostrze Gwiazdy Tiansha - Arayashiki [天殺星刀阿賴耶識]
393. [Status [HeavenlyKillerStar] — opis] - 속도 최솟값, 최댓값 +6\n- 공격 레벨 +6\n- 스킬로 부여하는 출혈 위력 +3\n- 턴 시작 시, 이번 전투에서 처치한 적 하나당 공격 레벨 증가 3 얻음 (최대 6)
   źródło: Bufs-a1c9p3.json :: dataList[id=HeavenlyKillerStar].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +6\n- Offense Level +6\n- Inflict 3 more Bleed Potency with Skills\n- Turn Start: Gain 3 Offense Level Up for every enemy killed in this Encounter (max 6)
   PL: - Min. i Maks. Szybkość +6\n- Poziom Ataku +6\n- Umiejętności nakładają +3 więcej Siły Krwawienia\n- Na początku tury zyskuje 3 Wzrostu Poziomu Ataku za każdego zabitego wroga w tej walce (maks. 6)
394. [Status [HeavenlyKillerStar] — tekst klimatyczny] ‘하늘조차 죽인다. 하늘과 땅과 사람, 그리고 나. 이 별은 모든 존재와 시간을 하나로 인식하여 베어낼 수 있는 자에게 뜨는 별.’
   źródło: Bufs-a1c9p3.json :: dataList[id=HeavenlyKillerStar].flavor
   limit: do 230 znaków
   EN: 'The heavens themselves are not spared—heaven, earth, man, and the self. This star rises only for the one who perceives all existence and time as a single whole to sever them all.'
   PL: „Nie oszczędza nawet nieba — niebo, ziemię, człowieka i mnie. Ta gwiazda wschodzi tylko dla tego, kto widzi całą egzystencję i czas jako jedność i potrafi je wszystko przeciąć.”
395. [Status [CutoffRyoshu] — nazwa] 절사 [切絲]
   źródło: Bufs-a1c9p3.json :: dataList[id=CutoffRyoshu].name
   kontekst: identyfikator statusu w tekstach: `[CutoffRyoshu]`
   limit: do 40 znaków
   EN: Sever the Thread [切絲]
   PL: Przecięcie Nici [切絲]
396. [Status [CutoffRyoshu] — opis] - 턴 시작 시,\n· 출혈 3 얻음, 출혈 횟수 3 증가\n· (수치/3)만큼 참격 피해를 받음\n- 피격 시, (수치/5)만큼 참격 피해를 받음\n- 이 수치가 증가할수록......\n- 최대 100
   źródło: Bufs-a1c9p3.json :: dataList[id=CutoffRyoshu].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 3 Bleed and +3 Bleed Count\n· Take Slash damage equal to (Stack / 3)\n- When hit, take Slash damage equal to (Stack / 5)\n- The more this effect stacks...\n- Max Stack: 100
   PL: - Na początku tury,\n· Zyskuje 3 Krwawienia i +3 Licznika Krwawienia\n· Otrzymuje obrażenia Cięcia równe (stosy / 3)\n- Przy trafieniu otrzymuje obrażenia Cięcia równe (stosy / 5)\n- Im więcej stosów...\n- Maks. 100
397. [Status [CutoffRyoshu] — tekst klimatyczny] ‘모든 것을 끊어낸다. 너도 나도, 지금까지와 앞으로의 모든 것을.’\n\n‘그렇게 해서 아라야를 데리고 온다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=CutoffRyoshu].flavor
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'Let everything be severed—you, me, all that has been, and all that will be.'\n\n'Once it is done... I will take Araya back.'
   PL: „Niech wszystko zostanie odcięte — ty, ja, cała przeszłość i przyszłość.”\n\n„A wtedy przywrócę Arayę.”
398. [Status [CutbondRyoshu] — nazwa] 무아 [無我]
   źródło: Bufs-a1c9p3.json :: dataList[id=CutbondRyoshu].name
   kontekst: identyfikator statusu w tekstach: `[CutbondRyoshu]`
   limit: do 40 znaków
   EN: Muga [無我]
   PL: Muga [無我]
399. [Status [CutbondRyoshu] — opis] - 턴 시작 시, 수치 10당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 이 수치가 증가할수록......\n- 최대 100
   źródło: Bufs-a1c9p3.json :: dataList[id=CutbondRyoshu].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 10 Stack\n- The more this effect stacks...\n- Max Stack: 100
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 10 stosów\n- Im więcej stosów...\n- Maks. 100
400. [Status [CutbondRyoshu] — tekst klimatyczny] ‘그러니 칼날을 아낀다. 준비가 되었을 때, 다시 거미집으로 들어간다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=CutbondRyoshu].flavor
   limit: do 120 znaków
   EN: 'So I must hold back on using the blade. And once I'm ready, I will return to that House.'
   PL: „Dlatego muszę oszczędzać ostrze. A gdy będę gotowa, wrócę do Domu Pajęczyn.”
401. [Status [EsteemNeeds] — nazwa] 인정 욕구
   źródło: Bufs-a1c9p3.json :: dataList[id=EsteemNeeds].name
   kontekst: identyfikator statusu w tekstach: `[EsteemNeeds]`
   limit: do 40 znaków
   EN: Desire for Acknowledgement
   PL: Głód Uznania
402. [Status [EsteemNeeds] — opis] - 수치 1당 료슈에게 가하는 피해량과 받는 피해량 +5% (최대 100%)\n- 수치 5당, 료슈를 메인 타겟으로 공격 시 최종 위력 +1 (최대 4)\n- 수치가 10 이상이면, 합 패배 시 5만큼 정신력 피해\n- 최대 20
   źródło: Bufs-a1c9p3.json :: dataList[id=EsteemNeeds].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every Stack, Deal +5% damage to and take +5% damage from Ryōshū (max 100%)\n- Final Power +1 for every 5 Stack when attacking Ryōshū as the main target (max 4)\n- At 10+ Stack, lose 5 SP upon Clash Lose\n- Max Stack: 20
   PL: - Za każdy stos zadaje i otrzymuje +5% obrażeń od i wobec Ryōshū (maks. 100%)\n- Moc Końcowa +1 za każde 5 stosów przy ataku Ryōshū jako głównym celu (maks. 4)\n- Przy 10+ stosach po przegranej w Starciu traci 5 Poczytalności\n- Maks. 20 stosów
403. [Status [EsteemNeeds] — tekst klimatyczny] ‘돌아가면 뤼,뤼엔 씨에게 칭찬받아야지….’
   źródło: Bufs-a1c9p3.json :: dataList[id=EsteemNeeds].flavor
   limit: do 120 znaków
   EN: 'Once I'm back home, M-Mister Rien will tell me I did good...'
   PL: „Po powrocie M-Mister Rien powie mi, że dobrze zrobiłam…”
404. [Status [Fugacious] — nazwa] 검의 길
   źródło: Bufs-a1c9p3.json :: dataList[id=Fugacious].name
   kontekst: identyfikator statusu w tekstach: `[Fugacious]`
   limit: do 40 znaków
   EN: Way of the Blade
   PL: Droga Ostrza
405. [Status [Fugacious] — opis] - 턴 시작시,\n· 수치 5당 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n· 수치 10당 피해량 증가 1, 취약 1 얻음\n- 최댓값 : 50
   źródło: Bufs-a1c9p3.json :: dataList[id=Fugacious].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n· Gain 1 Damage Up and 1 Fragile for every 10 Stack\n- Max Stack: 50
   PL: - Na początku tury,\n· Zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 stosów\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości za każde 10 stosów\n- Maks. stosów: 50
406. [Status [Fugacious] — tekst klimatyczny] 덧없는 꿈이어도 괜찮다.\n이번 생에 별의 이름을 얻지 못해도, 검의 길을 걷는 것만으로 검은 예리해지고 검술은 단조될 테니.
   źródło: Bufs-a1c9p3.json :: dataList[id=Fugacious].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It matters not if this dream is but a fleeting one.\nThough I may fail to inherit the name of a Star in this life, walking the Way of the Blade shall sharpen and temper this sword of mine.
   PL: Nie szkodzi, jeśli to jedynie ulotny sen.\nChoć nie odziedziczę w tym życiu imienia Gwiazdy, sama droga ostrza naostrzy i utwardzi to ostrze.
407. [Status [ObsessedTeacher_LowMorale] — nazwa] 가문의 수치
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessedTeacher_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ObsessedTeacher_LowMorale]`
   limit: do 40 znaków
   EN: Shame of the Family
   PL: Wstyd Rodziny
408. [Status [ObsessedTeacher_LowMorale] — opis] - 턴 시작 시 참격 피해 증가 1, 합 위력 증가 1, 취약 1 얻음\n- 스킬 사용 시 망을 얻을 수 없음
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessedTeacher_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Slash DMG Up, 1 Clash Power Up, and 1 Fragile\n- Cannot gain Mang when using Skills
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń Cięcia, 1 Wzrost Mocy Starcia i 1 Wrażliwości\n- Przy użyciu Umiejętności nie może zdobyć Mangu
409. [Status [ObsessedTeacher_Panic] — nazwa] 가문의 수치
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessedTeacher_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ObsessedTeacher_Panic]`
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Status [ObsessedTeacher_Panic] — opis] - 턴 시작 시 참격 피해 증가 2, 합 위력 증가 2, 취약 2 얻음\n- 스킬 사용 시 망을 얻을 수 없음
   źródło: Bufs-a1c9p3.json :: dataList[id=ObsessedTeacher_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Slash DMG Up, 2 Clash Power Up, and 2 Fragile\n- Cannot gain Mang when using Skills
   PL: - Na początku tury zyskuje 2 Wzrostu Obrażeń Cięcia, 2 Wzrostu Mocy Starcia i 2 Wrażliwości\n- Przy użyciu Umiejętności nie może zdobyć Mangu
411. [Status [AgainstMyWill_LowMorale] — nazwa] ‘나, 날… 죽여줘..’
   źródło: Bufs-a1c9p3.json :: dataList[id=AgainstMyWill_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[AgainstMyWill_LowMorale]`
   limit: do 40 znaków
   EN: "K-kill... kill me..."
   PL: „Z-zabij... zabij mnie..”
412. [Status [AgainstMyWill_LowMorale] — opis] 턴 시작 시 합 위력 감소 8, 위력 감소 5 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=AgainstMyWill_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 8 Clash Power Down and 5 Power Down
   PL: Na początku tury zyskuje 8 Spadek Mocy Starcia i 5 Spadek Mocy
413. [Status [AgainstMyWill_Panic] — nazwa] ‘나, 날… 죽여줘..’
   źródło: Bufs-a1c9p3.json :: dataList[id=AgainstMyWill_Panic].name
   kontekst: identyfikator statusu w tekstach: `[AgainstMyWill_Panic]`
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Status [AgainstMyWill_Panic] — opis] 턴 시작 시 합 위력 감소 10, 위력 감소 5 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=AgainstMyWill_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 10 Clash Power Down and 5 Power Down
   PL: Na początku tury zyskuje 10 Spadek Mocy Starcia i 5 Spadek Mocy
415. [Status [IndexPrescriptRien_0] — nazwa] 지령[단말기] I
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptRien_0]`
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Status [IndexPrescriptRien_0] — opis] 지령 대상을 공격하여 적중한다. 기한은 첫 번째 턴까지.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_0].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target before the first turn ends.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Cel Nakazu i trafia. Termin: do końca pierwszej tury.\n\n- Na początku tury zdobywany przy braku Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
417. [Status [IndexPrescriptRien_1] — nazwa] 지령[단말기] II
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptRien_1]`
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Status [IndexPrescriptRien_1] — opis] 지령 대상을 공격하여 적중한다. 또는 이번 턴에 공격을 4회 이상 적중한다. 기한은 네 번째 턴까지.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target; or, before this turn passes, hit with 4 or more attacks. Complete before the 4th turn.\n\n- Turn Start: Gain this effect when this unit has Unlock - 1\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Atakuje Cel Nakazu i trafia; albo trafia 4 lub więcej ataków przed końcem tury. Termin: do czwartej tury.\n\n- Na początku tury zdobywany przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
419. [Status [IndexPrescriptRien_2] — nazwa] 지령[단말기] III
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptRien_2]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Status [IndexPrescriptRien_2] — opis] 아홉 종류의 무기를 사용하는 강력한 스킬을 사용한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a powerful Skill that uses 9 different weapon types.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Używa potężnej Umiejętności, która używa 9 różnych typów broni.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
421. [Status [IndexPrescriptRien_3] — nazwa] 지령[단말기] IV
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptRien_3]`
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Status [IndexPrescriptRien_3] — opis] 모든 방해물을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescriptRien_3].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Status [IndexPrescript_RienSecondPhase] — nazwa] 지령[단말기] - 경고
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescript_RienSecondPhase]`
   limit: do 50 znaków
   EN: Prescript: [Device] - Warning
   PL: Nakaz [Urządzenie] - Ostrzeżenie
424. [Status [IndexPrescript_RienSecondPhase] — opis] 지령 대상을 우선적으로 처치한다.\n\n- 두 번째 페이즈부터 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritize eliminating The Prescript's Target.\n\n- Gain this effect starting from the 2nd phase
   PL: Priorytetowo eliminuj Cel Nakazu.\n\n- Zdobywany od drugiej fazy
425. [Status [IndexPrescript_RienSecondPhase] — tekst klimatyczny] ‘지령이 수행되지 않을 때마다 단말기가 내는 비프음은 점차 빨라진다.’\n\n‘그 긴박한 울림에 나의 심박수도 높아져가는 것만 같다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'The Device's beeping accelerates with every second I let pass without fulfilling a Prescript.'\n\n'And with it, so do the intervals of my heartbeat.'
   PL: „Za każdym razem, gdy Nakaz pozostaje niewykonany, pikanie Urządzenia przyspiesza.”\n\n„Wyda się, że wraz z tym gorącym odgłosem przyspiesza też moje serce.”
426. [Status [UnlockBuff_Rien1] — nazwa] 해금 - I
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien1].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_Rien1]`
   (powtórzenie elementu 82 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Status [UnlockBuff_Rien1] — opis] - 공격 레벨 +1, 방어 레벨 +1\n- 전투 종료 시, 정신력 10 회복
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1, Defense Level +1\n- Combat End: Heal 10 SP
   PL: - Poziom Ataku +1, Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 10 Poczytalności
428. [Status [UnlockBuff_Rien2] — nazwa] 해금 - II
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien2].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_Rien2]`
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Status [UnlockBuff_Rien2] — opis] - 공격 레벨 +2, 방어 레벨 +2\n- 전투 종료 시, 정신력 20 회복
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2, Defense Level +2\n- Combat End: Heal 20 SP
   PL: - Poziom Ataku +2, Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 20 Poczytalności
430. [Status [UnlockBuff_Rien3] — nazwa] 해금 - III
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien3].name
   kontekst: identyfikator statusu w tekstach: `[UnlockBuff_Rien3]`
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Status [UnlockBuff_Rien3] — opis] - 공격 레벨 +3, 방어 레벨 +3\n- 전투 종료 시, 정신력 30 회복
   źródło: Bufs-a1c9p3.json :: dataList[id=UnlockBuff_Rien3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3, Defense Level +3\n- Combat End: Heal 30 SP
   PL: - Poziom Ataku +3, Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 30 Poczytalności
432. [Status [KarmaOfIndexRien] — nazwa] 카르마
   źródło: Bufs-a1c9p3.json :: dataList[id=KarmaOfIndexRien].name
   kontekst: identyfikator statusu w tekstach: `[KarmaOfIndexRien]`
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Status [KarmaOfIndexRien] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 수치 40당 합 위력 감소 1 얻음\n- 최대 100
   źródło: Bufs-a1c9p3.json :: dataList[id=KarmaOfIndexRien].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stack\n· Gain 1 Fragile for every 20 Stack\n· Gain 1 Clash Power Down for every 40 Stack\n- Max Stack: 100
   PL: - Na początku tury\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Zyskuje 1 Spadek Mocy Starcia za każde 40 stosów\n- Maks. 100
434. [Status [KarmaOfIndexRien_2Phase] — nazwa] 카르마 [포르투나]
   źródło: Bufs-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].name
   kontekst: identyfikator statusu w tekstach: `[KarmaOfIndexRien_2Phase]`
   limit: do 40 znaków
   EN: Karmic Consequence [Fortuna]
   PL: Karma [Fortuna]
435. [Status [KarmaOfIndexRien_2Phase] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 수치 40당 합 위력 감소 1 얻음\n- 최대 200
   źródło: Bufs-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stack\n· Gain 1 Fragile for every 20 Stack\n· Gain 1 Clash Power Down for every 40 Stack\n- Max Stack: 200
   PL: - Na początku tury\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Zyskuje 1 Spadek Mocy Starcia za każde 40 stosów\n- Maks. 200
436. [Status [KarmaOfIndexRien_2Phase] — tekst klimatyczny] O Fortúna velut luna statu variabilis
   źródło: Bufs-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].flavor
   limit: do 120 znaków
   EN: O Fortúna velut luna statu variabilis
   PL: O Fortúna velut luna statu variabilis
437. [Status [BurningWoundRien_Mask] — nazwa] 뤼엔의 가면
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].name
   kontekst: identyfikator statusu w tekstach: `[BurningWoundRien_Mask]`
   limit: do 40 znaków
   EN: Rien's Mask
   PL: Maska Rien
438. [Status [BurningWoundRien_Mask] — opis] - 공격 레벨 -5, 방어 레벨 -5\n- 수치 1당, 화상 또는 출혈을 부여하는 스킬(위력, 횟수, 특수 키워드 포함)로 받는 피해 +5%\n· 화상과 출혈 둘 다 부여 시, 대신 +7.5%\n- 최대 1
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -5, Defense Level -5\n- For every Stack, take +5% damage from Skills that inflict Burn or Bleed (includes Potency, Count, and Unique variants)\n· If the Skill inflicts both Burn and Bleed, take +7.5% damage for every Stack instead\n- Max Stack: 1
   PL: - Poziom Ataku -5, Poziom Obrony -5\n- Za każdy stos otrzymuje +5% obrażeń od Umiejętności nakładających Podpalenie lub Krwawienie (z Siłą, Licznikiem i wariantami Specjalnymi)\n· Jeżeli Umiejętność nakłada oba, zamiast tego +7,5% za stos\n- Maks. 1
439. [Status [BurningWoundRien_Mask] — tekst klimatyczny] “볼 때마다 아파서 가리고 있어.”
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].flavor
   limit: do 120 znaków
   EN: "I keep it covered because it hurts to even look at."
   PL: „Zasłaniam, bo samo patrzenie na to boli.”
440. [Status [BurningWoundRien] — nazwa] 이글거리는 상처
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien].name
   kontekst: identyfikator statusu w tekstach: `[BurningWoundRien]`
   limit: do 40 znaków
   EN: Sizzling Wound
   PL: Kipiąca Rana
441. [Status [BurningWoundRien] — opis] - 공격 레벨 -5, 방어 레벨 -5\n- 턴 시작 시 수치 1당, 화상 횟수 1, 출혈 횟수 1 증가\n- 수치 1당, 화상 또는 출혈을 부여하는 스킬(위력, 횟수, 특수 키워드 포함)로 받는 피해 +10%\n· 화상과 출혈 둘 다 부여 시, 대신 +15%\n- 최대 5
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -5, Defense Level -5\n- Turn Start: Gain +1 Burn Count and +1 Bleed Count for every Stack\n- For every Stack, take +10% damage from Skills that inflict Burn or Bleed (includes Potency, Count, and Unique variants)\n· If the Skill inflicts both Burn and Bleed, take +15% damage for every Stack instead\n- Max Stack: 5
   PL: - Poziom Ataku -5, Poziom Obrony -5\n- Na początku tury zyskuje +1 Licznika Podpalenia i +1 Licznika Krwawienia za każdy stos\n- Za każdy stos otrzymuje +10% obrażeń od Umiejętności nakładających Podpalenie lub Krwawienie (z Siłą, Licznikiem i wariantami Specjalnymi)\n· Jeżeli Umiejętność nakłada oba, zamiast tego +15% za stos\n- Maks. 5
442. [Status [BurningWoundRien] — tekst klimatyczny] 그 검이 가까워지면 상처는 아물지 않고, 검결의 열로 타들어간 살점이 다시 익어간다.
   źródło: Bufs-a1c9p3.json :: dataList[id=BurningWoundRien].flavor
   limit: do 130 znaków
   EN: When in proximity of the sword, the wound unheals and the flesh that once cooled burns once again.
   PL: W pobliżu tego miecza rana nie chce się goić, a raz ostudzone mięso znów zaczyna się palić.
443. [Status [Shin_Rien] — nazwa] 신(心) - 뤼엔
   źródło: Bufs-a1c9p3.json :: dataList[id=Shin_Rien].name
   kontekst: identyfikator statusu w tekstach: `[Shin_Rien]`
   limit: do 40 znaków
   EN: Shin (心) - Rien
   PL: Shin (心) - Rien
444. [Status [Shin_Rien] — opis] - 턴 시작 시 잃은 체력에 비례하여,\n· 15%당 피해량 증가 1 얻음 (최대 5)\n· 40%당 공격 위력 증가 1 얻음 (최대 2)\n- 자신의 스킬로 얻는 호흡 위력 +1, 호흡 횟수 +1\n- 자신의 정신력이 대상보다 높으면, 정신력 차이 2당 피해량 +1% (최대 30%)
   źródło: Bufs-a1c9p3.json :: dataList[id=Shin_Rien].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Based on the missing HP on this unit...\n· Gain 1 Damage Up for every 15% missing HP (max 5)\n· Gain 1 Attack Power Up for every 40% missing HP (max 2)\n- Gain +1 more Poise Potency and Count from this unit's Skills\n- If this unit's SP is higher than the target's, deal +1% damage for every 2 SP difference (max 30%)
   PL: - Na początku tury, zależnie od brakującego HP,\n· Zyskuje 1 Wzrost Obrażeń za każde 15% brakującego HP (maks. 5)\n· Zyskuje 1 Wzrost Mocy Ataku za każde 40% brakującego HP (maks. 2)\n- Umiejętności zyskują +1 więcej Siły Oddechu i Licznika Oddechu\n- Jeżeli Poczytalność jest wyższa niż celu, zadaje +1% obrażeń za każde 2 różnicy Poczytalności (maks. 30%)
445. [Status [StackRienSpecialSkill] — nazwa] 대행 [헤르메스]
   źródło: Bufs-a1c9p3.json :: dataList[id=StackRienSpecialSkill].name
   kontekst: identyfikator statusu w tekstach: `[StackRienSpecialSkill]`
   limit: do 40 znaków
   EN: Procuration [Hermes]
   PL: Procuration [Hermes]
446. [Status [StackRienSpecialSkill] — opis] - 공격 스킬 사용 시, 1 얻음 (스킬별 1회, 동일한 스킬로 2 이상 획득 불가)\n- 턴 시작 시 수치가 9면, 강력한 스킬을 사용\n- 특정 스킬에서 소모
   źródło: Bufs-a1c9p3.json :: dataList[id=StackRienSpecialSkill].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack when using an Attack Skill (once per Skill; does not gain Stack from the same Skill twice)\n- Turn Start: at 9 Stack, use a powerful Skill\n- Consumed when using a certain Skill
   PL: - Zyskuje 1 stos przy użyciu Umiejętności ataku (1 raz na Umiejętność; ta sama Umiejętność nie liczy się dwukrotnie)\n- Na początku tury przy 9 stosach używa potężnej Umiejętności\n- Zużywana przez określone Umiejętności
447. [Status [StackRienSpecialSkill] — tekst klimatyczny] “신의 뜻에 따라.”
   źródło: Bufs-a1c9p3.json :: dataList[id=StackRienSpecialSkill].flavor
   limit: do 120 znaków
   EN: "As my god commands."
   PL: „Z woli boga.”
448. [Status [RienWeapon01Hatchet] — nazwa] 손도끼로 갈비뼈를 찍어 내릴 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon01Hatchet].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon01Hatchet]`
   limit: do 70 znaków
   EN: When hacking through the ribs with a hatchet...
   PL: Kiedy ocierasz żebra toporkiem…
449. [Status [RienWeapon01Hatchet] — opis] - 타격 피해를 입힘\n- 파괴되지 않고 적중 시, 호흡 2 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon01Hatchet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- On Hit without Cracking, gain 2 Poise
   PL: - Zadaje obrażenia Obuchu\n- Przy trafieniu bez Roztrzaskania zyskuje 2 Oddechu
450. [Status [RienWeapon01Hatchet2phase] — nazwa] 손도끼로 갈비뼈를 찍어 내릴 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon01Hatchet2phase]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Status [RienWeapon01Hatchet2phase] — opis] - 타격 피해를 입힘\n- 파괴되지 않고 적중 시, 호흡 2 얻음, 호흡 횟수 2 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- On Hit without Cracking, gain 2 Poise and +2 Poise Count
   PL: - Zadaje obrażenia Obuchu\n- Przy trafieniu bez Roztrzaskania zyskuje 2 Oddechu i +2 Licznika Oddechu
452. [Status [RienWeapon01Hatchet2phase] — tekst klimatyczny] “이건 꽝에 가깝지만 포크보다는 낫지.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].flavor
   limit: do 120 znaków
   EN: "This is barely a weapon, but it's better than a fork."
   PL: „To ledwie narzędzie, ale lepsze niż widelec.”
453. [Status [RienWeapon02Stiletto] — nazwa] 스틸레토로 허파를 꿰뚫을 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon02Stiletto].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon02Stiletto]`
   limit: do 70 znaków
   EN: When penetrating the lungs with a stiletto...
   PL: Kiedy przebijasz płuca sztyletą…
454. [Status [RienWeapon02Stiletto] — opis] - 관통 피해를 입힘\n- 파괴되지 않고 적중 시, 침잠 2 부여
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon02Stiletto].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- On Hit Without Cracking, inflict 2 Sinking
   PL: - Zadaje obrażenia Kłucia\n- Przy trafieniu bez Roztrzaskania nakłada 2 Zatonięcia
455. [Status [RienWeapon02Stiletto2phase] — nazwa] 스틸레토로 허파를 꿰뚫을 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon02Stiletto2phase]`
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Status [RienWeapon02Stiletto2phase] — opis] - 관통 피해를 입힘\n- 파괴되지 않고 적중 시, 침잠 2 부여, 침잠 횟수 2 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- On Hit without Cracking, inflict 2 Sinking and +2 Sinking Count
   PL: - Zadaje obrażenia Kłucia\n- Przy trafieniu bez Roztrzaskania nakłada 2 Zatonięcia i +2 Licznika Zatonięcia
457. [Status [RienWeapon02Stiletto2phase] — tekst klimatyczny] “횡으로 휘둘러야 하는 상황에 이게 나왔을 때는 식은땀이 나더구나. 나하고는 맞지 않아.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].flavor
   limit: do 230 znaków
   EN: "I couldn't help but feel a dreadful chill run down my back whenever I'm given this weapon when the situation calls for a horizontal swing. I find it hard to work with this."
   PL: „Za każdym razem, gdy w sytuacji wymagającej cięcia poziomego trafia się to narzędzie, na plecach pojawia się zimny pot. To nie dla mnie.”
458. [Status [RienWeapon03Greatsword] — nazwa] 바스타드 소드로 어깨와 머리를 짓이길 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon03Greatsword].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon03Greatsword]`
   limit: do 100 znaków
   EN: When cleaving through the shoulder and the skull with a bastard sword...
   PL: Kiedy miażdzysz bark i czaszkę mieczem bastardowym…
459. [Status [RienWeapon03Greatsword] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 다음 턴에 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon03Greatsword].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +5% damage\n- On Hit without Cracking, gain 1 Offense Level Up next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania zyskuje 1 Wzrost Poziomu Ataku w następnej turze (2 razy na turę)
460. [Status [RienWeapon03Greatsword2phase] — nazwa] 바스타드 소드로 어깨와 머리를 짓이길 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon03Greatsword2phase]`
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Status [RienWeapon03Greatsword2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 다음 턴까지 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, gain 1 Offense Level Up until next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania zyskuje 1 Wzrost Poziomu Ataku do następnej tury (2 razy na turę)
462. [Status [RienWeapon03Greatsword2phase] — tekst klimatyczny] “이 검은 무난하지만, 너무 무난해서 아쉬울 때가 있지. 그래도 기본기를 갖췄다면 충분히 쓸 만하단다.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].flavor
   limit: do 240 znaków
   EN: "This sword, it's... passable, but that quality in and of itself leaves a lot to be desired. Nevertheless, it can still be a trusty weapon as long as your fundamental skills are solid."
   PL: „Ten miecz jest... przyzwoity, ale ta przyzwoitość sama w sobie pozostawia wiele do życzenia. Mimo to przy solidnych podstawach posłuży nieźle.”
463. [Status [RienWeapon04Rapier] — nazwa] 레이피어로 몸에 10개 이상의 구멍을 내야할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon04Rapier].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon04Rapier]`
   limit: do 80 znaków
   EN: When punching 10 or more holes in the torso with a rapier...
   PL: Kiedy musisz zrobić rapierem 10 lub więcej dziur w korpusie…
464. [Status [RienWeapon04Rapier] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 다음 턴에 방어 레벨 감소 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon04Rapier].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +5% damage\n- On Hit without Cracking, inflict 1 Defense Level Down next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Spadek Poziomu Obrony w następnej turze (2 razy na turę)
465. [Status [RienWeapon04Rapier2phase] — nazwa] 레이피어로 몸에 10개 이상의 구멍을 내야할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon04Rapier2phase]`
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Status [RienWeapon04Rapier2phase] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 다음 턴까지 방어 레벨 감소 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, inflict 1 Defense Level Down until next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Spadek Poziomu Obrony do następnej tury (2 razy na turę)
467. [Status [RienWeapon04Rapier2phase] — tekst klimatyczny] “스틸레토보다 예리하고 긴 무기지. 나는 기교를 좋아해서, 레이피어도 좋아한단다.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].flavor
   limit: do 180 znaków
   EN: "A weapon longer and sharper than the stiletto. I enjoy the rapier as well, as it lends itself quite well to more dexterous techniques."
   PL: „Broń dłuższa i ostrzejsza od stiletto. Lubię też rapiera — świetnie nadaje się do zwinnych technik.”
468. [Status [RienWeapon05Sledgehammer] — nazwa] 망치로 뒤통수를 으깨야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon05Sledgehammer]`
   limit: do 80 znaków
   EN: When caving in the back of the skull with a hammer...
   PL: Kiedy musisz roztrzaskać młotem potylicę…
469. [Status [RienWeapon05Sledgehammer] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 3만큼 흐트러짐 피해
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +5% damage\n- On Hit without Cracking, raise target's Stagger Threshold by 3
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania podnosi Próg Oszołomienia celu o 3
470. [Status [RienWeapon05Sledgehammer2phase] — nazwa] 망치로 뒤통수를 으깨야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon05Sledgehammer2phase]`
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Status [RienWeapon05Sledgehammer2phase] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 5만큼 흐트러짐 피해
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, raise target's Stagger Threshold by 5
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania podnosi Próg Oszołomienia celu o 5
472. [Status [RienWeapon05Sledgehammer2phase] — tekst klimatyczny] “단순하지만 확실하지. 손도끼처럼 애매하지 않아. 확실히 터트릴 수 있어.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].flavor
   limit: do 120 znaków
   EN: "Simple, but final. It's not a half-measure like a hatchet—it <i>will</i> crush whatever it hits."
   PL: „Prosto, ale definitywnie. To nie półśrodek jak siekiera — ta rzeczywiście roztrzaska to, w co trafi.”
473. [Status [RienWeapon06Ultragreatsword] — nazwa] 커다란 검으로 몸통을 갈라야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon06Ultragreatsword]`
   limit: do 60 znaków
   EN: When rending the body with a greatsword...
   PL: Kiedy musisz rozciąć wielkim mieczem korpus…
474. [Status [RienWeapon06Ultragreatsword] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 참격 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Slash Fragility (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Cięcie (2 razy na turę)
475. [Status [RienWeapon06Ultragreatsword2phase] — nazwa] 커다란 검으로 몸통을 갈라야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon06Ultragreatsword2phase]`
   limit: do 60 znaków
   EN: When rending the body with a great sword...
   PL: Kiedy musisz rozciąć wielkim mieczem korpus…
476. [Status [RienWeapon06Ultragreatsword2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 참격 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Slash Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Cięcie do następnej tury (2 razy na turę)
477. [Status [RienWeapon06Ultragreatsword2phase] — tekst klimatyczny] “이렇게 크고 무거운 검은 무엇보다 무게중심이 중요하단다.”\n“그리고 중량을 이용하는 게 좋지.”\n“5층 옥상에서 떨어지며 이걸로 1급 해결사를 암살했을 때가 생각나는구나.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].flavor
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "When it comes to wielding blades of ponderous size and weight, such as this one, it is important to find your center of gravity."\n"And of course, don't forget to take advantage of its sheer mass."\n"I once jumped from the rooftop of a five-story building with this weapon and dropped on top of a Grade 1 Fixer's head, killing him instantly."
   PL: „Przy tak wielkiej i ciężkiej broni najważniejszy jest środek ciężkości.”\n„I wykorzystuj jej masę.”\n„Przypominam sobie, jak, spadając z dachu pięciopiętrowego budynku, udało mi się jednym ciosem zabić tą bronią Fixera I klasy.”
478. [Status [RienWeapon07Lance] — nazwa] 랜스로 20인치의 구멍을 내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon07Lance].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon07Lance]`
   limit: do 60 znaków
   EN: When boring a 20-inch hole with a lance...
   PL: Kiedy musisz zrobić lancem 20-calową dziurę…
479. [Status [RienWeapon07Lance] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 관통 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon07Lance].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Pierce Fragility (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Kłucie (2 razy na turę)
480. [Status [RienWeapon07Lance2phase] — nazwa] 랜스로 20인치의 구멍을 내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon07Lance2phase]`
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Status [RienWeapon07Lance2phase] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 관통 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Pierce Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Kłucie do następnej tury (2 razy na turę)
482. [Status [RienWeapon07Lance2phase] — tekst klimatyczny] “당첨인 무기야. 이 랜스에는 자체적인 가속 기능도 있어서 저 멀리서도 벽이나 가로막는 자들을 다 뚫어가며 목표까지 꿰뚫을 수 있지.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].flavor
   limit: do 290 znaków
   EN: "I'd consider this weapon a jackpot. This lance has a self-propelling property as well, which is what allows it to punch through the target—and anything that stands between us as well, whether that is a wall or a person."
   PL: „To broń-jackpot. Ta lanca ma własny napęd, więc z daleka przebije wszystko, co stanie między nami a celem — ścianę czy człowieka.”
483. [Status [RienWeapon08Chain] — nazwa] 채찍으로 살점을 만 갈래 떼어내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon08Chain].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon08Chain]`
   limit: do 80 znaków
   EN: When ripping the flesh to ten thousand strips with a whip...
   PL: Kiedy musisz strzępić ciało biczem na 10 000 kawałków…
484. [Status [RienWeapon08Chain] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 타격 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon08Chain].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Blunt Fragility (2 times per turn)
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Obuch (2 razy na turę)
485. [Status [RienWeapon08Chain2phase] — nazwa] 채찍으로 살점을 만 갈래 떼어내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon08Chain2phase]`
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Status [RienWeapon08Chain2phase] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 타격 취약 1 부여 (턴당 2회)
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Blunt Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Obuch do następnej tury (2 razy na turę)
487. [Status [RienWeapon08Chain2phase] — tekst klimatyczny] “누군가에게는 꽝일 수 있겠지만… 나는 마음에 들어.”\n“이 채찍에 맞은 사람은 살점이 떨어져 피를 흘린단다. 그러다가 점점 고통과 탈진으로 허덕이지.”\n“점점 약해져 가는 모습을 볼 수 있는 게 좋아. 그리고 급할 때는 교살용으로도 쓸 수 있지.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].flavor
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "While some may equate this weapon to losing a lottery... I am quite fond of it."\n"When this whip cracks, it doesn't just make them bleed; it tears a strip off the target's flesh, and with it their resolve and energy."\n"I appreciate that it lets me observe the full process of how someone is deconstructed as they are weakened. Oh, and it can also be used to strangle in a pinch."
   PL: „Dla niektórych to przegrana w loterii... mnie się podoba.”\n„Kto dostaje tym biczem, traci strzępy mięsa i krwawi. Stopniowo pada od bólu i wyczerpania.”\n„Lubię patrzeć, jak ktoś rozpada się kawałek po kawałku. A w razie potrzeby służy też do duszenia.”
488. [Status [RienWeapon09Scythe] — nazwa] 낫으로… 누군가처럼 공간을 따라 베어내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon09Scythe].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon09Scythe]`
   limit: do 110 znaków
   EN: When lacerating through space itself with a scythe, like a certain someone...
   PL: Kiedy musisz ciąć kosą… przestrzeń, jak ktoś…
489. [Status [RienWeapon09Scythe] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +20%\n- 파괴되지 않고 적중 시, 반드시 크리티컬로 적중
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon09Scythe].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +20% damage\n- On Hit without Cracking, it hits a guaranteed Crit
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +20% obrażeń\n- Przy trafieniu bez Roztrzaskania trafia zawsze jako Cios Krytyczny
490. [Status [RienWeapon09Scythe2phase] — nazwa] 낫으로… 누군가처럼 공간을 따라 베어내야 할 때는…
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].name
   kontekst: identyfikator statusu w tekstach: `[RienWeapon09Scythe2phase]`
   (powtórzenie elementu 488 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Status [RienWeapon09Scythe2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +30%\n- 파괴되지 않고 적중 시, 반드시 크리티컬로 적중
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +30% damage\n- On Hit without Cracking, it hits a guaranteed Crit
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +30% obrażeń\n- Przy trafieniu bez Roztrzaskania trafia zawsze jako Cios Krytyczny
492. [Status [RienWeapon09Scythe2phase] — tekst klimatyczny] “낫은… 너무나 난해했지만, 푸른잔향이 싸우는 모습을 보니 감이 오더구나.”\n“그 후로도 한동안 지령이 내게 낫만을 쓰게 해서 어떤 무기보다 이 낫을 잘 다루고 좋아한단다.”\n“그리고 가장 잘 벨 수도 있지. 공간을 베는 기술에는 여러 가지가 있지만… 음. 이건 나중에 들려주는 게 좋겠어.”
   źródło: Bufs-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].flavor
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "The scythe... I could not for the life of me understand how to use this weapon until I saw that Blue Reverberation wield his own."\n"Even after I had observed him, the Prescript continued to give me no other weapons than the scythe for a while. Eventually, it became my favorite, most familiar, and sharpest weapon."\n"This weapon also cuts the best out of them all. While there are many techniques to cut through space itself— Hm. Perhaps this story is best saved for another time."
   PL: „Kosa... długo pozostawała dla mnie zagadką, ale gdy przyszło mi patrzeć, jak walczy Błękitny Pogłos, wszystko nagle stało się jasne.”\n„Potem Nakaz przez jakiś czas dawał mi tylko kosę — stała się moją ulubioną, najlepiej znaną bronią.”\n„I tnie z nich wszystkich najlepiej. Technik przecinania przestrzeni jest wiele... Hmm. Ta historia lepiej poczeka.”
493. [Status [Ryoshu_RienBattle_1Phase] — nazwa] 케츠엔 [けつえん]
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].name
   kontekst: identyfikator statusu w tekstach: `[Ryoshu_RienBattle_1Phase]`
   limit: do 40 znaków
   EN: Ketsuen [けつえん]
   PL: Ketsuen [けつえん]
494. [Status [Ryoshu_RienBattle_1Phase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 료슈의 체력이 1 미만으로 내려가지 않음\n- 합 위력 +1, 공격 적중 시 피해량 +10%\n- 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Clash Power +1; On Hit, deal +10% damage\n- On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Dopóki w tej walce żyje co najmniej 1 inny sojusznik, HP Ryōshū nie spada poniżej 1\n- Moc Starcia +1; przy trafieniu zadaje +10% obrażeń\n- Po wygranym Starciu zyskuje 1 Zasób E.G.O z każdego z 3 najmniej posiadanych Grzechów\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu)\n- Wycofanie niemożliwe
495. [Status [Ryoshu_RienBattle_1Phase] — tekst klimatyczny] 천살성도 - 아라야시키를 제어하기 위해서 만들어진 료슈만의 검집. 꺼지지 않는 불 속에서 단조된 아라야의 E.G.O.
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].flavor
   limit: do 190 znaków
   EN: Ryōshū's one and only scabbard, created to control the Tiansha Star's Blade - Arayashiki. This is Araya's E.G.O, forged in the eternal flame.
   PL: Jedyna pochwa Ryōshū, stworzona by kontrolować Ostrze Gwiazdy Tiansha - Arayashiki. To E.G.O Arayi, wykute w wiecznym ogniu.
496. [Status [Ryoshu_RienBattle_2Phase] — nazwa] 렌케츠엔 [れんけつえん]
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].name
   kontekst: identyfikator statusu w tekstach: `[Ryoshu_RienBattle_2Phase]`
   limit: do 40 znaków
   EN: Renketsuen [れんけつえん]
   PL: Renketsuen [れんけつえん]
497. [Status [Ryoshu_RienBattle_2Phase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 료슈의 체력이 1 미만으로 내려가지 않음\n- 합 위력 +2, 공격 적중 시 피해량 +25%\n- 대상의 이글거리는 상처 1당\n· 공격 레벨 +1, 방어 레벨 +1\n· 공격 적중 시 피해량 +5% (최대 25%), 기본 E.G.O 스킬을 사용했으면 대신 피해량 +50% (최대 250%)\n- 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Clash Power +2; On Hit, deal +25% damage\n- For every Sizzling Wound Stack on target:\n· Offense Level +1, Defense Level +1\n· Deal +5% damage On Hit (max 25%); if this unit used a Base E.G.O Skill, deal +50% damage per Stack instead (max 250%)\n- On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Dopóki w tej walce żyje co najmniej 1 inny sojusznik, HP Ryōshū nie spada poniżej 1\n- Moc Starcia +2; przy trafieniu zadaje +25% obrażeń\n- Za każdy stos Kipiącej Rany celu:\n· Poziom Ataku +1, Poziom Obrony +1\n· Przy trafieniu zadaje +5% obrażeń (maks. 25%); jeżeli użyła podstawowej Umiejętności E.G.O, zamiast tego +50% za stos (maks. 250%)\n- Po wygranym Starciu zyskuje 1 Zasób E.G.O z każdego z 3 najmniej posiadanych Grzechów\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu)\n- Wycofanie niemożliwe
498. [Status [Ryoshu_RienBattle_2Phase] — tekst klimatyczny] 희미한 자아만이 남아있는 역설적인 E.G.O.\n오직 상대를 위하는 것처럼 보이더라도, 이는 절대적인 이타성이 아니다.\n타인의 삶이 가진 의미를 자신의 삶보다 우선 시하기 위해서는 절대적인 이기심이 필요하다.\n\n“엄마가 나를 잊지 않았으면 좋겠지만, 이대로 엄마를 잃는 게 나는 더 싫어.”\n“그러니까 나를 먼저 잊고, 자신을 더 소중히 해.”
   źródło: Bufs-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].flavor
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An E.G.O of paradoxical existence, for its ego is faint.\nDo not equate what appears to be utter devotion toward someone else with absolute altruism.\nOne must possess absolute egoism to put the significance of another's life before one's own.\n\n"I don't want mommy to forget about me, but... more than that, I don't wanna lose her."\n"So forget me for now, and take care of yourself."
   PL: Paradoksalne E.G.O, w którym zostaje ledwie ślad ego.\nNawet jeśli wygląda jak pełne poświęcenie dla kogoś, nie jest absolutnym altruizmem.\nŻeby stawiać znaczenie czyjegoś życia ponad własne, trzeba absolutnego egoizmu.\n\n„Chciałabym, żeby mama mnie nie zapomniała, ale... bardziej niż to, nie chcę ją stracić.”\n„Więc zapomnij najpierw o mnie i dbaj o siebie.”
499. [Status [PainfulScar_Panic] — nazwa] 모조된 아비
   źródło: Bufs-a1c9p3.json :: dataList[id=PainfulScar_Panic].name
   kontekst: identyfikator statusu w tekstach: `[PainfulScar_Panic]`
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
500. [Status [PainfulScar_Panic] — opis] - 패닉\n- 턴 시작 시, 화상 5, 화상 횟수 3, 출혈 5, 출혈 횟수 3 얻음\n- 수감자 료슈에게 받는 피해량 +20%
   źródło: Bufs-a1c9p3.json :: dataList[id=PainfulScar_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 5 Burn, +3 Burn Count, 5 Bleed, and +3 Bleed Count\n- Take +20% damage from Sinner Ryōshū
   PL: - Panika\n- Na początku tury: 5 Podpalenia, 3 Licznika Podpalenia, 5 Krwawienia i 3 Licznika Krwawienia\n- Otrzymuje +20% obrażeń od Grzesznika Ryōshū
501. [Status [PainfulScar_LowMorale] — nazwa] 모조된 아비
   źródło: Bufs-a1c9p3.json :: dataList[id=PainfulScar_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[PainfulScar_LowMorale]`
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Status [PainfulScar_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 화상 5, 출혈 5 얻음\n- 수감자 료슈에게 받는 피해량 +10%
   źródło: Bufs-a1c9p3.json :: dataList[id=PainfulScar_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 5 Burn and 5 Bleed\n- Take +10% damage from Sinner Ryōshū
   PL: - Niskie Morale\n- Na początku tury zyskuje 5 Podpalenia i 5 Krwawienia\n- Otrzymuje +10% obrażeń od Grzesznika Ryōshū
503. [Status [BlackNightmare] — nazwa] 지령 탐닉
   źródło: Bufs-a1c9p3.json :: dataList[id=BlackNightmare].name
   kontekst: identyfikator statusu w tekstach: `[BlackNightmare]`
   limit: do 40 znaków
   EN: Indulgence in Prescripts
   PL: Indulgencja w Nakazach
504. [Status [BlackNightmare] — opis] - 부여하는 침잠 위력과 횟수 +2\n- 턴 종료 시, 사라지고 (이번 턴에 합 패배한 스킬 수 x 5)만큼 카르마 얻음
   źródło: Bufs-a1c9p3.json :: dataList[id=BlackNightmare].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Inflict +2 more Sinking Potency and Count\n- Expires at Turn End; then, gain (number of Skills that lost a Clash this turn x 5) Karmic Consequence
   PL: - Nakłada +2 więcej Siły i Licznika Zatonięcia\n- Znika na koniec tury, a następnie zyskuje (liczba Umiejętności, które przegrały Starcie w tej turze x 5) Karma
505. [Status [BlackNightmare] — tekst klimatyczny] 겉으로는 기꺼이 지령을 수행하는 듯 보이나, 그 이면에는 지령에 대한 원망 또한 엿보인다.\n그러나 모든 고통과 쾌락을 지령이라는 가면을 쓰고 행할 수 있었기에, 그 본망은 지령에 대한 감사함으로 귀결된다.
   źródło: Bufs-a1c9p3.json :: dataList[id=BlackNightmare].flavor
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The acceptance of the Prescripts is apparent in his execution of them; yet, on the other side of the mask, one may glimpse a hint of resentment for them.\nHowever, as he could indulge in all the suffering and pleasures of the world behind the mask of "Prescripts," his true immanent yearning is concluded by that of gratitude.
   PL: Z zewnątrz wykonuje Nakazy chętnie, lecz za maską prześwituje do nich uraza.\nPonieważ jednak mógł oddawać się całemu cierpieniu i przyjemnościom świata za maską „Nakazów”, jego ukryta tęsknota kończy się wdzięcznością.
506. [Status [RyoshuParrySojiWe] — nazwa] 붉은 실
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParrySojiWe]`
   limit: do 40 znaków
   EN: Red String
   PL: Czerwona Nić
507. [Status [RyoshuParrySojiWe] — opis] - 스킬 슬롯 수 +3\n소지 아비에게 가하는 피해량 +50%\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +3\n- Deal +50% damage to The Pinky Nursefather\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +3\nZadaje +50% obrażeń Ojcu Małego Palca\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
508. [Status [RyoshuParrySojiWe] — tekst klimatyczny] ‘이 가느다란 실 하나만이 너와 나를 이어주고 있다면, 나는 온 힘을 다해 이 실을 놓지 않을 거다.’
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].flavor
   limit: do 140 znaków
   EN: 'If this single thread is the only thing that connects you and me, I will cling to it with all my being.'
   PL: „Jeżeli ta jedna cienka nić łączy mnie z tobą, będę się jej kurczowo trzymać całym sobą.”
509. [Status [RyoshuParrySojiThey] — nazwa] 붉은 실
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParrySojiThey]`
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Status [RyoshuParrySojiThey] — opis] - 모든 스킬 코인이 파괴 불가 코인으로 변경됨\n- 최종 위력 +4
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Converts all Skill Coins into Unbreakable Coins\n- Final Power +4
   PL: - Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Moc Końcowa +4
511. [Status [RyoshuParrySojiThey] — tekst klimatyczny] ‘당신과 나는 이 실 때문에 결국 만나. 피하고 싶어도 계속 마주하게 돼. 이 실은 도무지 끊어지질 않아.’
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].flavor
   limit: do 160 znaków
   EN: 'Escape as we might, this stubborn thread will force us to cross paths still. It refuses to break, no matter what I do...'
   PL: „Dzięki tej nici w końcu się spotkamy. Choć byśmy chcieli uniknąć, wciąż się spotkamy. Ta nić nie chce się przeciąć.”
512. [Status [CriticalDamageUp] — nazwa] 크리티컬 피해량 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=CriticalDamageUp].name
   kontekst: identyfikator statusu w tekstach: `[CriticalDamageUp]`
   limit: do 40 znaków
   EN: Crit DMG Up
   PL: Wzrost Obrażeń Krytycznych
513. [Status [CriticalDamageUp] — opis] 한 턴 동안 스킬로 가하는 크리티컬 피해량이 수치당 10% 증가
   źródło: Bufs-a1c9p3.json :: dataList[id=CriticalDamageUp].desc
   limit: do 120 znaków
   EN: For this turn: Deal +10% damage on Critical Hit for every Stack
   PL: W tej turze obrażenia Krytyczne rosną o 10% za każdy stos
514. [Status [KAA1C9ActivateEffect] — nazwa] K사 앰플 사용
   źródło: Bufs-a1c9p3.json :: dataList[id=KAA1C9ActivateEffect].name
   kontekst: identyfikator statusu w tekstach: `[KAA1C9ActivateEffect]`
   limit: do 40 znaków
   EN: K Corp. Ampule Used
   PL: Użyta Ampułka Korporacji K
515. [Status [KAA1C9ActivateEffect] — opis] 사용된 K사 앰플
   źródło: Bufs-a1c9p3.json :: dataList[id=KAA1C9ActivateEffect].desc
   limit: do 120 znaków
   EN: Used K Corp. Ampule
   PL: Użyta Ampułka Korporacji K
516. [Status [RyoshuParryIndexFingerWe] — nazwa] 붉은 실
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParryIndexFingerWe].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParryIndexFingerWe]`
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Status [RyoshuParryIndexFingerThey] — nazwa] 붉은 실
   źródło: Bufs-a1c9p3.json :: dataList[id=RyoshuParryIndexFingerThey].name
   kontekst: identyfikator statusu w tekstach: `[RyoshuParryIndexFingerThey]`
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-cultivation
- plik gry: `Bufs-cultivation.json`

518. [Status [LegStrengthHorse] — nazwa] 각력【오】
   źródło: Bufs-cultivation.json :: dataList[id=LegStrengthHorse].name
   kontekst: identyfikator statusu w tekstach: `[LegStrengthHorse]`
   limit: do 40 znaków
   EN: Strider【Wu】
   PL: Kroczący【Wu】
519. [Status [LegStrengthHorse] — opis] - 최댓값: 3\n- 턴 종료 시 다음 턴에 신속 2, 방어 레벨 증가를 (수치 x 2)만큼 얻음\n- 스킬 적중시 진동 위력을 수치만큼 추가로 부여 (턴 당 최대 6)
   źródło: Bufs-cultivation.json :: dataList[id=LegStrengthHorse].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Haste and (Stack x 2) Defense Level Up next turn\n- On Hit with a Skill, inflict additional Tremor Potency equal to Stack (max 6 per turn)
   PL: - Maks. stosów: 3\n- Na koniec tury zyskuje 2 Pośpiechu i (stosy x 2) Wzrost Poziomu Obrony w następnej turze\n- Umiejętności nakładają dodatkowo Siłę Wstrząsu równą stosom przy trafieniu (maks. 6 na turę)
520. [Status [ConcussionWei] — nazwa] 뇌진탕
   źródło: Bufs-cultivation.json :: dataList[id=ConcussionWei].name
   kontekst: identyfikator statusu w tekstach: `[ConcussionWei]`
   limit: do 40 znaków
   EN: Concussion
   PL: Wstrząs Mózgu
521. [Status [ConcussionWei] — opis] - 최댓값: 3\n- 피격 시 피해량을 수치 당 30% 추가로 받음 (최대 90%)\n- 이 효과가 있는 동안 파열 피해와 진동 폭발로 인한 흐트러짐 손상을 1.5배로 받음. (소수점 버림)\n- 최대 수치에 도달했다면 턴 종료시 전부 소모되고 다음 턴 강제 흐트러짐
   źródło: Bufs-cultivation.json :: dataList[id=ConcussionWei].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When hit, take +30% damage for every Stack (max 90%)\n- Multiply the amount of Stagger Threshold raised by Tremor Burst and Rupture damage dealt against this unit by 1.5 (rounded down)\n- At max Stack, consume all of it at Turn End and enter forced Stagger state next turn
   PL: - Maks. stosów: 3\n- Przy trafieniu otrzymuje +30% obrażeń za każdy stos (maks. 90%)\n- Podczas tego efektu otrzymuje x1,5 podniesienia Progu Oszołomienia od Wyładowania Wstrząsu i obrażeń Rozdarcia (zaokrąglone w dół)\n- Przy Maks. stosów zużywa je wszystkie na koniec tury i przechodzi w wymuszone Oszołomienie w następnej turze
522. [Status [SweptAwayWei] — nazwa] 휩쓸림
   źródło: Bufs-cultivation.json :: dataList[id=SweptAwayWei].name
   kontekst: identyfikator statusu w tekstach: `[SweptAwayWei]`
   limit: do 40 znaków
   EN: Galestruck
   PL: Porwanie Wichrem
523. [Status [SweptAwayWei] — opis] - 최댓값: 10\n- 진동 폭발로 인한 흐트러짐 손상을 2배로 받음.\n- 턴 종료 시 1 감소
   źródło: Bufs-cultivation.json :: dataList[id=SweptAwayWei].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Double the amount of Stagger Threshold raised on this unit due to Tremor Burst\n- Reduced by 1 at Turn End
   PL: - Maks. stosów: 10\n- Podwaja podniesienie Progu Oszołomienia od Wyładowania Wstrząsu\n- Na koniec tury maleje o 1
524. [Status [ReboundWei] — nazwa] 반동
   źródło: Bufs-cultivation.json :: dataList[id=ReboundWei].name
   kontekst: identyfikator statusu w tekstach: `[ReboundWei]`
   limit: do 40 znaków
   EN: Recoiling
   PL: Odrzut
525. [Status [ReboundWei] — opis] - 최댓값: 5
   źródło: Bufs-cultivation.json :: dataList[id=ReboundWei].desc
   limit: do 120 znaków
   EN: - Max Stack: 5
   PL: - Maks.: 5
526. [Status [ReboundWei] — tekst klimatyczny] 잘못된 대상에게 진동 폭발을 입힘으로 생긴 반동이다.
   źródło: Bufs-cultivation.json :: dataList[id=ReboundWei].flavor
   limit: do 140 znaków
   EN: Triggered Tremor Burst against the wrong target. Every action has an equal and opposite reaction, after all.
   PL: To odrzut po wywołaniu Wyładowania Wstrząsu na niewłaściwym celu. Każde działanie ma równą i przeciwną reakcję.
527. [Status [SipOfAlcoholJin] — nazwa] 한 모금(眞)
   źródło: Bufs-cultivation.json :: dataList[id=SipOfAlcoholJin].name
   kontekst: identyfikator statusu w tekstach: `[SipOfAlcoholJin]`
   limit: do 40 znaków
   EN: Swig (眞)
   PL: Łyczek (眞)
528. [Status [SipOfAlcoholJin] — opis] - 최대값: 5\n- 턴 종료 시 다음 턴에 (수치 x 2) 만큼 호흡 위력 획득\n- 턴 종료 시 다음 턴에 (수치 / 2) 만큼 신속 획득 (소수점 버림)\n- 턴 종료 시 수치가 3 이상이면, 전체 체력의 1.5%만큼 회복 (본체, 부위)
   źródło: Bufs-cultivation.json :: dataList[id=SipOfAlcoholJin].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: gain (Stack x 2) Poise Potency next turn\n- Turn End: gain (Stack / 2) Haste next turn (rounded down)\n- Turn End: at 3+ Stack, heal 1.5% HP (both Core & Part)
   PL: - Maks. stosów: 5\n- Na koniec tury zyskuje (stosy x 2) Siły Oddechu w następnej turze\n- Na koniec tury zyskuje (stosy / 2) Pośpiechu w następnej turze (zaokrąglone w dół)\n- Na koniec tury przy 3+ stosach leczy 1,5% HP (korpus i części)
529. [Status [DrunkBlood] — nazwa] 혈주(血注)
   źródło: Bufs-cultivation.json :: dataList[id=DrunkBlood].name
   kontekst: identyfikator statusu w tekstach: `[DrunkBlood]`
   limit: do 40 znaków
   EN: Bloodpour (血注)
   PL: Rzut Krwi (血注)
530. [Status [DrunkBlood] — opis] - 최댓값: 5\n- 특수 출혈\n- 공격 스킬의 코인 판정 시, 수치만큼 고정 체력 피해를 받음
   źródło: Bufs-cultivation.json :: dataList[id=DrunkBlood].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Unique Bleed\n- When tossing an attack Coin, take fixed damage by the effect’s Stack.
   PL: - Maks. stosów: 5\n- Specjalne Krwawienie\n- Przy rzucie Monety Umiejętności ataku otrzymuje obrażenia stałe równe stosom tego efektu
531. [Status [DrunkAwakening] — nazwa] 정신 각성
   źródło: Bufs-cultivation.json :: dataList[id=DrunkAwakening].name
   kontekst: identyfikator statusu w tekstach: `[DrunkAwakening]`
   limit: do 40 znaków
   EN: Mental Awakening
   PL: Przebudzenie Umysłu
532. [Status [DrunkAwakening] — opis] - 최댓값: 1\n- 이 효과를 지니는 동안 최종 위력 4 증가, 받는 피해량 30% 증가\n- 출혈 위력 부여 코인 적중 시 추가로 출혈을 2 부여함 (턴 당 최대 10)\n- 자신에게 호흡이 있으면 크리티컬 피해량 +50%
   źródło: Bufs-cultivation.json :: dataList[id=DrunkAwakening].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- As long as this unit has this effect, gain 4 Final Power and take +30% damage\n- On Hit with a Coin that inflicts Bleed Potency: inflict +2 more Bleed On Hit (max 10 per turn)\n- If this unit has Poise, deal +50% damage
   PL: - Maks. stosów: 1\n- Dopóki posiada ten efekt: Moc Końcowa +4 i otrzymuje +30% obrażeń\n- Przy trafieniu Monetą nakładającą Siłę Krwawienia nakłada dodatkowo 2 Krwawienia (maks. 10 na turę)\n- Jeżeli posiada Oddech, zadaje +50% obrażeń Krytycznych
533. [Status [RunawayHorseWei_LowMorale] — nazwa] 고삐 풀린 말
   źródło: Bufs-cultivation.json :: dataList[id=RunawayHorseWei_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[RunawayHorseWei_LowMorale]`
   limit: do 40 znaków
   EN: Unbridled Steed
   PL: Rumak bez Wędzidła
534. [Status [RunawayHorseWei_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 2, 취약 1을 얻음
   źródło: Bufs-cultivation.json :: dataList[id=RunawayHorseWei_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Offense Level Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Wrażliwości
535. [Status [RunawayHorseWei_Panic] — nazwa] 고삐 풀린 말
   źródło: Bufs-cultivation.json :: dataList[id=RunawayHorseWei_Panic].name
   kontekst: identyfikator statusu w tekstach: `[RunawayHorseWei_Panic]`
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Status [RunawayHorseWei_Panic] — opis] - 패닉\n- 턴 시작 시, 최대 속도 1 증가, 공격 레벨 증가 2, 취약 2를 얻음
   źródło: Bufs-cultivation.json :: dataList[id=RunawayHorseWei_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Max Speed, 2 Offense Level Up, and 2 Fragile
   PL: - Panika\n- Zyskuje 1 Maks. Szybkość, 2 Wzrostu Poziomu Ataku i 2 Wrażliwości
537. [Status [DrunkDrifter_LowMorale] — nazwa] 취수야객
   źródło: Bufs-cultivation.json :: dataList[id=DrunkDrifter_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DrunkDrifter_LowMorale]`
   limit: do 50 znaków
   EN: Night Drifter of the Drunken Palm
   PL: Pijanica Nocny Wędrowiec
538. [Status [DrunkDrifter_LowMorale] — opis] - 사기 저하\n- 가시춘에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: Bufs-cultivation.json :: dataList[id=DrunkDrifter_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +10% damage from Jia Xichun; deal +30% damage with Counterattacks
   PL: - Niskie Morale\n- Otrzymuje +10% obrażeń od Jia Xichun; zadaje +30% obrażeń Kontrą
539. [Status [DrunkDrifter_Panic] — nazwa] 취수야객
   źródło: Bufs-cultivation.json :: dataList[id=DrunkDrifter_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DrunkDrifter_Panic]`
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Status [DrunkDrifter_Panic] — opis] - 패닉\n- 최종 위력 1 증가, 가시춘에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: Bufs-cultivation.json :: dataList[id=DrunkDrifter_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Final Power +1; take +20% damage from Jia Xichun; deal +50% damage with Counterattacks
   PL: - Panika\n- Moc Końcowa +1; otrzymuje +20% obrażeń od Jia Xichun; zadaje +50% obrażeń Kontrą
541. [Status [DarkBeastSnake_LowMorale] — nazwa] 암완
   źródło: Bufs-cultivation.json :: dataList[id=DarkBeastSnake_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DarkBeastSnake_LowMorale]`
   limit: do 40 znaków
   EN: Shadow Arm
   PL: Ciemna Wąż-Ręka
542. [Status [DarkBeastSnake_LowMorale] — opis] - 사기 저하\n- 합 위력 -1, 받는 피해량 -10%
   źródło: Bufs-cultivation.json :: dataList[id=DarkBeastSnake_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1; take -10% damage
   PL: - Niskie Morale\n- Moc Starcia -1; otrzymuje -10% obrażeń
543. [Status [DarkBeastSnake_Panic] — nazwa] 암완
   źródło: Bufs-cultivation.json :: dataList[id=DarkBeastSnake_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DarkBeastSnake_Panic]`
   (powtórzenie elementu 541 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Status [DarkBeastSnake_Panic] — opis] - 패닉\n- 합 위력 -2, 받는 피해량 -20%
   źródło: Bufs-cultivation.json :: dataList[id=DarkBeastSnake_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2; take -20% damage
   PL: - Panika\n- Moc Starcia -2; otrzymuje -20% obrażeń
545. [Status [NightDrifterGuilty] — nazwa] 미약한 죄책감
   źródło: Bufs-cultivation.json :: dataList[id=NightDrifterGuilty].name
   kontekst: identyfikator statusu w tekstach: `[NightDrifterGuilty]`
   limit: do 40 znaków
   EN: Faint Guilt
   PL: Słabe Poczucie Winy
546. [Status [NightDrifterGuilty] — opis] - 공격 레벨 15 감소\n- 방어 레벨 15 감소
   źródło: Bufs-cultivation.json :: dataList[id=NightDrifterGuilty].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -15\n- Defense Level -15
   PL: - Poziom Ataku -15\n- Poziom Obrony -15
547. [Status [StudyStatSinclair] — nazwa] 알에서 나오기 위한 몸부림
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair]`
   limit: do 40 znaków
   EN: Thrashing to Hatch
   PL: Tęsknota za Wykluciem
548. [Status [StudyStatSinclair] — opis] - 수업으로 얻는 인/지/용의 합에 비례하여 효과 강화
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair].desc
   limit: do 120 znaków
   EN: - Enhance effects based on the sum of Zhi, Yong, and Ren gained from classes
   PL: - Wzmacnia efekty zależnie od sumy Zhi, Yong i Ren zdobytych na zajęciach
549. [Status [StudyStatSinclair_A] — nazwa] 알에서 나오기 위한 몸부림 Ⅰ
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_A].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair_A]`
   limit: do 40 znaków
   EN: Thrashing to Hatch Ⅰ
   PL: Tęsknota za Wykluciem Ⅰ
550. [Status [StudyStatSinclair_A] — opis] - 매 턴 정신력 3 회복\n- 속도 최소값, 최대값 1 증가\n- 공격 레벨 2 증가\n- 방어 레벨 2 증가
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_A].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 3 SP every turn\n- Gain 1 Min & Max Speed\n- Gain 2 Offense Levels\n- Gain 2 Defense Levels
   PL: - Co turę odzyskuje 3 Poczytalności\n- Min. i Maks. Szybkość +1\n- Poziom Ataku +2\n- Poziom Obrony +2
551. [Status [StudyStatSinclair_B] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅠ
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_B].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair_B]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅠ
   PL: Tęsknota za Wykluciem Ⅱ
552. [Status [StudyStatSinclair_B] — opis] - 매 턴 정신력 5 회복\n- 속도 최소값, 최대값 1 증가,\n- 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 공격 레벨 2 증가\n- 방어 레벨 2 증가
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_B].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 5 SP every turn\n- Gain 1 Min & Max Speed\n- Gain 1 Attack Power Up and 1 Protection every turn\n- Gain 2 Offense Levels\n- Gain 2 Defense Levels
   PL: - Co turę odzyskuje 5 Poczytalności\n- Min. i Maks. Szybkość +1,\n- Co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Poziom Ataku +2\n- Poziom Obrony +2
553. [Status [StudyStatSinclair_C] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅠⅠ
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_C].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair_C]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅠⅠ
   PL: Tęsknota za Wykluciem Ⅲ
554. [Status [StudyStatSinclair_C] — opis] - 매 턴 정신력 5 회복\n- 속도 최소값, 최대값 1 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 공격 레벨 3 증가\n- 방어 레벨 3 증가
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_C].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 5 SP every turn\n- Gain 1 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Gain 3 Offense Levels\n- Gain 3 Defense Levels
   PL: - Co turę odzyskuje 5 Poczytalności\n- Min. i Maks. Szybkość +1; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Poziom Ataku +3\n- Poziom Obrony +3
555. [Status [StudyStatSinclair_D] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅤ
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_D].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair_D]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅤ
   PL: Tęsknota za Wykluciem Ⅳ
556. [Status [StudyStatSinclair_D] — opis] - 매 턴 정신력 10 회복\n- 속도 최소값, 최대값 1 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 공격 레벨 4 증가\n- 방어 레벨 4 증가
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_D].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 10 SP every turn\n- Gain 1 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Gain 4 Offense Levels\n- Gain 4 Defense Levels
   PL: - Co turę odzyskuje 10 Poczytalności\n- Min. i Maks. Szybkość +1; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Poziom Ataku +4\n- Poziom Obrony +4
557. [Status [StudyStatSinclair_E] — nazwa] 알에서 나오기 위한 몸부림 Ⅴ
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_E].name
   kontekst: identyfikator statusu w tekstach: `[StudyStatSinclair_E]`
   limit: do 40 znaków
   EN: Thrashing to Hatch Ⅴ
   PL: Tęsknota za Wykluciem Ⅴ
558. [Status [StudyStatSinclair_E] — opis] - 매 턴 정신력 15 회복\n- 속도 최소값, 최대값 2 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 기본 스킬 코인 위력 1 증가\n- 공격 레벨 5 증가\n- 방어 레벨 5 증가
   źródło: Bufs-cultivation.json :: dataList[id=StudyStatSinclair_E].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 15 SP every turn\n- Gain 2 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Base Skills gain 1 Coin Power\n- Gain 5 Offense Levels\n- Gain 5 Defense Levels
   PL: - Co turę odzyskuje 15 Poczytalności\n- Min. i Maks. Szybkość +2; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Podstawowe Umiejętności zyskują 1 Moc Monety\n- Poziom Ataku +5\n- Poziom Obrony +5
559. [Status [StudySignSinclair] — nazwa] 어느 표지
   źródło: Bufs-cultivation.json :: dataList[id=StudySignSinclair].name
   kontekst: identyfikator statusu w tekstach: `[StudySignSinclair]`
   limit: do 40 znaków
   EN: A Sign
   PL: Pewien Znak
560. [Status [StudySignSinclair] — opis] - 다음 턴 정신력 30 회복\n- 턴 종료 시, 사라짐
   źródło: Bufs-cultivation.json :: dataList[id=StudySignSinclair].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 30 SP next turn\n- Turn End: Expires
   PL: - Odzyskuje 30 Poczytalności w następnej turze\n- Znika na koniec tury
561. [Status [StudySignSinclair] — tekst klimatyczny] 태어나려는 자는 한 세계를 파괴해야만 한다.
   źródło: Bufs-cultivation.json :: dataList[id=StudySignSinclair].flavor
   limit: do 120 znaków
   EN: One who seeks to be born must first destroy a world.
   PL: Ten, kto pragnie się narodzić, musi najpierw zniszczyć świat.
562. [Status [CrazyWei] — nazwa] 광폭화
   źródło: Bufs-cultivation.json :: dataList[id=CrazyWei].name
   kontekst: identyfikator statusu w tekstach: `[CrazyWei]`
   limit: do 40 znaków
   EN: Berserking
   PL: Szalone Kwitnienie
563. [Status [CrazyWei] — opis] - 공격 레벨 15 감소\n- 방어 레벨 15 감소\n\n- 턴 종료 시 각력【오】 버프로 방어 레벨을 얻지 않고, 공격 레벨 증가를 각력【오】 수치 만큼 얻음
   źródło: Bufs-cultivation.json :: dataList[id=CrazyWei].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 15 Offense Level\n- Lose 15 Defense Level\n\n- Turn End: does not gain Defense Level from Strider【Wu】; instead, gain Offense Level Up equal to Strider【Wu】 Stack
   PL: - Poziom Ataku -15\n- Poziom Obrony -15\n\n- Na koniec tury nie zyskuje Poziomu Obrony z Siły Nóg 【Wu】; zamiast tego zyskuje Wzrost Poziomu Ataku równy stosom Siły Nóg 【Wu】
564. [Status [CrazyWei] — tekst klimatyczny] “…아가씨를 해하려는 모든 것들을… 짓밟아 죽이리…”
   źródło: Bufs-cultivation.json :: dataList[id=CrazyWei].flavor
   limit: do 120 znaków
   EN: "I'll trample anyone who dares to hurt my lady... I'll trample them to death... "
   PL: „...Wszystko, co ośmieli się skrzywdzić moją panią... zdeptam na śmierć…”
565. [Status [SnakePoisonJinWeak] — nazwa] 뱀 독
   źródło: Bufs-cultivation.json :: dataList[id=SnakePoisonJinWeak].name
   kontekst: identyfikator statusu w tekstach: `[SnakePoisonJinWeak]`
   limit: do 40 znaków
   EN: Snake Venom
   PL: Jad Węża
566. [Status [SnakePoisonJinWeak] — opis] - 공격 레벨 1 감소\n- 방어 레벨 1 감소
   źródło: Bufs-cultivation.json :: dataList[id=SnakePoisonJinWeak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -1\n- Defense Level -1
   PL: - Poziom Ataku -1\n- Poziom Obrony -1
567. [Status [SnakePoisonJin] — nazwa] 퍼지는 뱀 독
   źródło: Bufs-cultivation.json :: dataList[id=SnakePoisonJin].name
   kontekst: identyfikator statusu w tekstach: `[SnakePoisonJin]`
   limit: do 40 znaków
   EN: Spreading Snake Venom
   PL: Rozprzestrzeniający się Jad Węża
568. [Status [SnakePoisonJin] — opis] - 공격 레벨 7 감소\n- 방어 레벨 7 감소\n합 진행 시 최대 체력의 1%만큼 피해를 받음
   źródło: Bufs-cultivation.json :: dataList[id=SnakePoisonJin].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -7\n- Defense Level -7\nTake 1% HP damage with every Clash
   PL: - Poziom Ataku -7\n- Poziom Obrony -7\nOtrzymuje 1% HP obrażeń przy każdym Starciu

## Statusy i efekty bojowe — Bufs-exme
- plik gry: `Bufs-exme.json`

569. [Status [ScratchesHurt] — nazwa] 찢긴 상처
   źródło: Bufs-exme.json :: dataList[id=ScratchesHurt].name
   kontekst: identyfikator statusu w tekstach: `[ScratchesHurt]`
   limit: do 40 znaków
   EN: Avulsion Wound
   PL: Rozdarta Rana
570. [Status [ScratchesHurt] — opis] - 최댓값: 3\n- 턴 시작 시 수치 1당, 출혈 2 얻음\n• 수치가 최댓값이면, 출혈 횟수 1 추가 증가\n- 턴 종료 시 다음 턴에 수치 만큼 속박 1 얻음\n• 수치가 최댓값이면, 다음 턴에 공격 위력 감소 1 추가 얻음\n- 이번 턴 동안 크리티컬 피해를 받지 않았다면, 턴 종료 시 1 감소
   źródło: Bufs-exme.json :: dataList[id=ScratchesHurt].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Gain 2 Bleed for every Stack\n• At max Stack, gain +1 Bleed Count\n- Turn End: Gain Bind equal to Stack next turn\n• At Max Stack, gain 1 Attack Power Down as well next turn\n- Turn End: If this unit did not take any Critical Hit this turn, lose 1 Stack
   PL: - Maks. stosów: 3\n- Na początku tury zyskuje 2 Krwawienia za każdy stos\n• Przy Maks. stosów zyskuje dodatkowo +1 Licznika Krwawienia\n- Na koniec tury zyskuje Spętań równy stosom w następnej turze\n• Przy Maks. stosów zyskuje dodatkowo 1 Spadek Mocy Ataku w następnej turze\n- Na koniec tury traci 1 stos, jeżeli w tej turze nie otrzymał Ciosu Krytycznego
571. [Status [TiedRope] — nazwa] 포박
   źródło: Bufs-exme.json :: dataList[id=TiedRope].name
   kontekst: identyfikator statusu w tekstach: `[TiedRope]`
   limit: do 40 znaków
   EN: Trussed
   PL: Skuty
572. [Status [TiedRope] — opis] - 기본값: 3\n- 속도가 1로 고정됨\n- 기본 스킬의 코인 위력이 0으로 고정됨\n- 턴 종료 시 1 감소\n- 자신에게 효과를 부여한 대상의 ‘압송 채비’ 버프가 소멸하면, 해당 효과 함께 소멸
   źródło: Bufs-exme.json :: dataList[id=TiedRope].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Fix this unit's Speed to 1\n- Fix this unit's Base Skills' Coin Power to 0\n- Turn End: Lose 1 Stack\n- If the "Prisoner Transport Arrangements" buff on the inflicter expires, this effect expires as well
   PL: - Wartość bazowa: 3\n- Szybkość zostaje zablokowana na 1\n- Moc Monet podstawowych Umiejętności zostaje zablokowana na 0\n- Na koniec tury maleje o 1\n- Gdy na nałożycielu wygaśnie buff „Przygotowania Konwoju”, ten efekt znika razem z nim
573. [Status [TiedRope] — tekst klimatyczny] 아랫것이 아랫것을 잡아 위로 올린다.
   źródło: Bufs-exme.json :: dataList[id=TiedRope].flavor
   limit: do 120 znaków
   EN: Look how the baseborn hunt the other baseborn to serve them up to the powers that be.
   PL: Patrz, jak nędzny łapie nędznego, by podnieść go tym, którzy stoją wyżej.
574. [Status [TiedWithRope] — nazwa] 압송 채비
   źródło: Bufs-exme.json :: dataList[id=TiedWithRope].name
   kontekst: identyfikator statusu w tekstach: `[TiedWithRope]`
   limit: do 50 znaków
   EN: Prisoner Transport Arrangements
   PL: Przygotowania Konwoju
575. [Status [TiedWithRope] — opis] - 기본값: 1\n- {0} 포박중\n- 속도가 1로 고정됨\n- 자신이 대상에게 부여한 포박 효과가 소멸하거나, 자신(추노꾼)이 사망 혹은 흐트러짐 상태가 되면, 버프 소멸\n- 자신이 포박을 부여한 대상이 이번 턴에 사망한 경우, ‘압송 채비’ 버프 소멸
   źródło: Bufs-exme.json :: dataList[id=TiedWithRope].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Base Stack: 1\n- Currently Trussing {0}\n- Fix this unit's Speed to 1\n- If the Trussed effect this unit inflicted on target expires, or if this unit is defeated or Staggered, lose this effect\n- If the target this unit inflicted "Trussed" on is defeated this turn, lose the "Prisoner Transport Arrangements" effect
   PL: - Wartość bazowa: 1\n- Obecnie skuwa: {0}\n- Szybkość jest ustalona na 1\n- Jeśli efekt „Skuty” nadany przez tę jednostkę na cel wygaśnie, albo ta jednostka zginie lub popada w stan Oszołomienia, Wzmocnienie znika\n- Jeśli cel, na który ta jednostka nadała efekt „Skuty”, zginie w tej turze, Wzmocnienie „Przygotowania Konwoju” znika
576. [Status [RegretSCorp] — nazwa] 지끈거리는 기억
   źródło: Bufs-exme.json :: dataList[id=RegretSCorp].name
   kontekst: identyfikator statusu w tekstach: `[RegretSCorp]`
   limit: do 40 znaków
   EN: Headsplitting Memory
   PL: Kolące w Skroniach Wspomnienie
577. [Status [RegretSCorp] — opis] - 최댓값: 1\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 다음 턴에 (현재 턴 수 / 4)만큼 합 위력 증가 얻음 (소수점 버림, 최대 3)\n- 턴 종료 시 소멸
   źródło: Bufs-exme.json :: dataList[id=RegretSCorp].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Gain 1 Bind next turn\n- Turn End: Gain (current turn count / 4) Clash Power Up (rounded down, max 3)\n- Expires at Turn End
   PL: - Maks. stosów: 1\n- Na koniec tury zyskuje 1 Spętanie w następnej turze\n- Na koniec tury zyskuje (liczba tur / 4) Wzrostu Mocy Starcia (zaokrąglone w dół, maks. 3)\n- Znika na koniec tury
578. [Status [TakePicture] — nazwa] 정보 취득
   źródło: Bufs-exme.json :: dataList[id=TakePicture].name
   kontekst: identyfikator statusu w tekstach: `[TakePicture]`
   limit: do 40 znaków
   EN: Intelligence Gathering
   PL: Zbieranie Informacji
579. [Status [TakePicture] — opis] - 촬영된 스킬 등급과 동일한 등급의 스킬 사용 시 합 위력 -5\n(※수비 스킬, E.G.O 스킬은 별개로 구분)\n({0})\n- 턴 종료 시 소멸
   źródło: Bufs-exme.json :: dataList[id=TakePicture].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - When using a Skill of identical rank to the Skill photographed, Clash Power -5\n(※ Defense Skills and E.G.O Skills are counted separately)\n({0})\n- Expires at Turn End
   PL: - Po użyciu Umiejętności tej samej rangi co sfotografowana, Moc Starcia -5\n(※ Umiejętności obrony i Umiejętności E.G.O liczone są osobno)\n({0})\n- Znika na koniec tury
580. [Status [LensmanNail] — nazwa] 고정 못
   źródło: Bufs-exme.json :: dataList[id=LensmanNail].name
   kontekst: identyfikator statusu w tekstach: `[LensmanNail]`
   limit: do 40 znaków
   EN: Pinning Nail
   PL: Przypinający Gwóźdź
581. [Status [LensmanNail] — opis] - 최댓값 : 10\n- 턴 시작 시 속박 수치 2당, 공격 레벨 감소 1 얻음 (최대 3)\n- 턴 시작 시 수치 만큼 출혈 얻음\n- 진동 폭발 시 수치 만큼 출혈 횟수 증가 (턴당 1회)\n- 턴 종료 시 수치 만큼 다음 턴에 속박을 얻고 (최대 6), 수치 1 감소
   źródło: Bufs-exme.json :: dataList[id=LensmanNail].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Turn Start: Gain 1 Offense Level Down for every 2 Bind (max 3)\n- Turn Start: Gain Bleed equal to Stack\n- On Tremor Burst, gain Bleed Count equal to Stack (once per turn)\n- Turn End: Gain Bind equal to Stack next turn (max 6), then lose 1 Stack
   PL: - Maks. stosów: 10\n- Na początku tury zyskuje 1 Spadek Poziomu Ataku za każde 2 Spętań (maks. 3)\n- Na początku tury zyskuje Krwawienie równe stosom\n- Przy Wyładowaniu Wstrząsu zyskuje Licznik Krwawienia równy stosom (1 raz na turę)\n- Na koniec tury zyskuje Spętań równych stosom w następnej turze (maks. 6), a wartość maleje o 1
582. [Status [PhotoTransition] — nazwa] 기억 전환
   źródło: Bufs-exme.json :: dataList[id=PhotoTransition].name
   kontekst: identyfikator statusu w tekstach: `[PhotoTransition]`
   limit: do 40 znaków
   EN: Memory Transition
   PL: Przełączanie Wspomnień
583. [Status [PhotoTransition] — opis] - 기본값 : 3\n- 턴 종료 시 수치 1 감소. 턴 시작 시 수치가 0이면, 특정 유닛과 버프가 변경됨\n(흐트러짐 상태면, 흐트러짐 해제)\n\n- 위 효과 발동 후 기억 전환 수치는 기본값으로 돌아감
   źródło: Bufs-exme.json :: dataList[id=PhotoTransition].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack. If this unit has 0 Stacks of this effect at Turn Start, certain units and effects transform\n(when Staggered, recover from Stagger)\n\n- Once the above effect activates, reset Memory Transition Stack to Base Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury maleje o 1. Jeżeli na początku tury wartość wynosi 0, określone jednostki i buffy się zmieniają\n(przy Oszołomieniu wychodzi z Oszołomienia)\n\n- Po wywołaniu powyższego efektu stosy Przełączania Wspomnień wracają do wartości bazowej
584. [Status [AengduNewArm] — nazwa] 도깨비팔
   źródło: Bufs-exme.json :: dataList[id=AengduNewArm].name
   kontekst: identyfikator statusu w tekstach: `[AengduNewArm]`
   limit: do 40 znaków
   EN: Dokkaebi Arms
   PL: Ramiona Dokkaebi
585. [Status [AengduNewArm] — opis] - 기본 공격 레벨 4 증가\n- 기본 방어 레벨 4 증가\n- 받는 피해 20% 감소\n- 스킬 사용 시 다음 턴에 신속 1 얻음 (턴당 2회)\n- 전투 종료 시 호흡 횟수 2 증가
   źródło: Bufs-exme.json :: dataList[id=AengduNewArm].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +4\n- Base Defense Level +4\n- Take -20% damage\n- On Skill Use, gain 1 Haste next turn (2 times per turn)\n- Combat End: Gain +2 Poise Count
   PL: - Podstawowy Poziom Ataku +4\n- Podstawowy Poziom Obrony +4\n- Otrzymuje -20% obrażeń\n- Przy użyciu Umiejętności zyskuje 1 Pośpiech w następnej turze (2 na turę)\n- Po zakończeniu walki zyskuje +2 Licznika Oddechu
586. [Status [AengduNewArm] — tekst klimatyczny] “…도깨비팔? 옛이야기에서 종종 나오는 그 도깨비를 말하는 것인가. 으음…”\n“믿기진 않지만, 림버스 컴퍼니에 몸담고 봐온 것들을 생각하면, 민담 속의 도깨비가 있다 해도 이상하지 않을 터.”\n“그러고 보니 도깨비 부대… 라는 것은 들어본 적 있는 것 같소.”
   źródło: Bufs-exme.json :: dataList[id=AengduNewArm].flavor
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "... Dokkaebi Arms? Do you, perchance, speak of Dokkaebis that often appear in tales of old? Hmm..."\n"I can scarcely believe it, yet after all I have witnessed while relying on the hospitality of Limbus Company, the existence of Dokkaebis from folklore may well be within reason."\n"Come to think of it... I do recall hearing of a name called 'Dokkaebi Unit'..."
   PL: „...Ramiona Dokkaebi? Czy mówi pan o dokkaebi ze starych opowieści? Hm...”\n„Choć trudno w to uwierzyć, po tym, co widziałem w Limbus Company, istnienie dokkaebi z ludowych podań nie wydaje się dziwne.”\n„A tak zresztą... ‚oddział Dokkaebi’... chyba coś takiego słyszałem.”
587. [Status [WindBlade] — nazwa] 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불
   źródło: Bufs-exme.json :: dataList[id=WindBlade].name
   kontekst: identyfikator statusu w tekstach: `[WindBlade]`
   limit: do 100 znaków
   EN: Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   PL: Warsztat Mook - Ye [銳] II Dobycie Ostrza
588. [Status [WindBlade] — opis] - 최댓값: 20\n- 수치만큼 참격 피해량 +1% (최대 10%)\n- 수치 2당, 수비 스킬의 합 위력 -1 (최대 5)\n- 턴 종료 시 다음 턴에 수치 5당, 신속 1 얻음 (최대 3)
   źródło: Bufs-exme.json :: dataList[id=WindBlade].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal +1% Slash damage for every Stack (max 10%)\n- Defense Skills lose 1 Clash Power for every 2 Stacks (max 5)\n- Turn End: Gain 1 Haste next turn for every 5 Stacks (max 3)
   PL: - Maks. stosów: 20\n- Zadaje +1% obrażeń Cięcia za każdy stos (maks. 10%)\n- Umiejętności obrony tracą 1 Moc Starcia za każde 2 stosy (maks. 5)\n- Na koniec tury zyskuje 1 Pośpiech w następnej turze za każde 5 stosów (maks. 3)
589. [Status [WindBlade] — tekst klimatyczny] “뭐야? 혹시 그 모델 맘에 들어? 울 막둥이 보는 눈이 좋은데? 사장님~ 요 모델 시착해 봐도 괜찮을까요? 에이~ 그럼요! 망가뜨리면 살 테니까 걱정 마세요! 히히. 내가 말했지? 단골이라 이런 건 다 된다니까~ 검이랑 검집이랑 세트니까 같이 들어봐. 어때, 보기보다 좀 가볍지?”\n“호오…”\n“묵 공방에서 특허를 가지고 있는 입자? 가루? 그런 게 요 검집 안에 들어있어. 그래서 납도한 뒤에 발도할 때마다 날이 엄청 예리해지고, 순간적으로 검이 엄청 가벼워지거든? 그중에서도 예리함에 중점을 두고 만들어진 게 막둥이가 지금 들고 있는 모델이야. 아무튼 검을 검집에서 뽑을 때마다 삥~ 하고 버프가 걸린다는 느낌인 거지.”\n“묵 공방의 클래식 모델 중 하나인 예[銳] 시리즈 중 하나일 텐데… 마감 처리를 보면… 뭐야!? 이거 지금은 단종된 예[銳] 2식이잖아!? 이거 구하기 진짜 힘든 건데 여기 하나 남아있었네!?”\n“그리 귀한 것이오? 그렇다면 차라리 소저가 다루는 것이...”\n“으으으… 아냐! 척 봐도 막둥이 껀데 뭘! 의수에서 나오는 부스터 기능이랑 궁합도 괜찮을 거구. 익숙해지려면 시간이 좀 걸리긴 하겠지만, 제대로 다룰 수 있게 되면 어디 가서 꿇리진 않을걸? 아무튼 임시 떼고 정식으로 막둥이가 된 기념으로 이 선배가 사주는 거야!”\n“그렇다면… 감사히 받겠네. ”\n“아. 클래식 모델인 만큼 튼튼하긴 엄청 튼튼한데, 그래도 섬세한 부분이 있으니 부서지지 않게 조심… 아니, 부서지는 건 괜찮아. 그냥...”\n“죽지만 마.”\n“…그 말씀, 마음 깊이 새기겠소.”
   źródło: Bufs-exme.json :: dataList[id=WindBlade].flavor
   limit: do 2200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Hm? You like that model? Ooh, new girl's got an eye for quality! Excuse me~! Can we try this model? Oh, c'mon, relax! I know the deal—'You break it, you buy it.' Thanks! Hehe... See? Told ya I'm a regular here~ Okay, so the sword and the scabbard come as a set, so grab 'em both and feel the weight. How's that? Not as heavy as they look, huh?"\n"Oho..."\n"So there's this particle? Powder? Thingy in that scabbard under patent by Mook Workshop! Every time you sheathe and unsheathe the sword, for a brief moment, its blade comes out way sharper and lighter! And that model you're holding happens to focus on the <i>sharpness</i>! So it's like, *Ding!* and voila, you get a nice buff on your weapon!"\n"I think it's one of the Ye [銳] series models—that's Mook Workshop's classic lineup, by the way. Check out the finish here, it's... What the heck?! Hey, this is the Ye [銳] 'Type II' model that went out of production! You know what, this stuff really isn't easy to come by—we're lucky we found one here!"\n"If it's such a rarity, Lady Ezra, perhaps you ought to wield it instead..."\n"Hnngh... No, it's fine... Well, I can see it's literally made for you! And it'll work real nice with those boosters on your new prosthetic arms. It'll need some getting used to, but you'll be one heck of a fighter once you get the hang of it! Anyway, consider it a gift from yours truly—you're officially one of us now. Officially our new girl! No more temp ID."\n"Then... I shall accept with gratitude."\n"By the way... Remember that 'classic lineup' part? It's super durable, but there <i>are</i> delicate parts that you should watch out not to break—okay, you know what, let 'em break if it really comes to that. Just..."\n"Just don't die on us."\n"... I shall take your words to heart."
   PL: „Co takiego? Podoba ci się ten model? Nasza nowa dziewczyna ma dobre oko! Przepraszam~! Możemy przymierzyć ten model? No weź, spokojnie! Znam zasady — ‚kto zepsuje, kupuje’. Dzięki! Hihi... No co ty? Mówiłam, że tu bywam~ Dobra, miecz i pochwa idą w zestawie, więc chwyć oba i poczuj wagę. No i jak? Lżejsze, niż wyglądają, co?”\n„Oho...”\n„W tej pochwie siedzi jakiś pył? Proszek? Opatentowany przez Warsztat Mook! Za każdym razem, gdy miecz wraca i wychodzi z pochwy, na moment staje się o dużo ostrzejszy i lżejszy! A model, który trzymasz, stawia właśnie na ostrość! Czyli tak — cyk! — i broń dostaje buffa.”\n„Chyba to jeden z modeli serii Ye [銳] — klasyki Warsztatu Mook. Patrzę na wykończenie... Co!? To wycofany z produkcji Ye [銳] II Typ!? Tego się naprawdę trudno szukać — a tu akurat jeden został!?”\n„Coś tak cennego? W takim razie może raczej pani Ezra powinna nim władać...”\n„Yyy... Nie! Już widzę, że to dla naszej nowej dziewczyny! Do tego pasować będzie do boosterów w twoich nowych protezach. Przyzwyczajenie zajmie chwilę, ale jak ją opanujesz, to nikt cię nie zmusi do klęczki! A tak w ogóle — przyjmij to jako prezent, że przestałaś być na czasówce i oficjalnie jesteś nasza!”\n„W takim razie... przyjmuję z wdzięcznością.”\n„Aha — skoro to klasyk, jest cholernie wytrzymały, ale ma delikatne elementy, więc uważaj, żeby niczego nie połamać... nie, właściwie połamiesz, to trudno. Po prostu...”\n„Tylko nie umrzyj.”\n„...Zapiszę te słowa głęboko w sercu.”
590. [Status [Collage_LowMorale] — nazwa] 뒤섞인 기억
   źródło: Bufs-exme.json :: dataList[id=Collage_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Collage_LowMorale]`
   limit: do 40 znaków
   EN: Jumbled Memories
   PL: Przemieszane Wspomnienia
591. [Status [Collage_LowMorale] — opis] - 턴 시작 시 공격 레벨 증가 1~3, 방어 레벨 감소 1~3 얻음
   źródło: Bufs-exme.json :: dataList[id=Collage_LowMorale].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 1~3 Offense Level Up and 1~3 Defense Level Down
   PL: - Na początku tury zyskuje 1–3 Wzrostu Poziomu Ataku i 1–3 Spadek Poziomu Obrony
592. [Status [Collage_Panic] — nazwa] 뒤섞인 기억
   źródło: Bufs-exme.json :: dataList[id=Collage_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Collage_Panic]`
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Status [Collage_Panic] — opis] - 턴 시작 시 공격 레벨 증가 1~5, 방어 레벨 감소 1~5 얻음
   źródło: Bufs-exme.json :: dataList[id=Collage_Panic].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 1~5 Offense Level Up and 1~5 Defense Level Down
   PL: - Na początku tury zyskuje 1–5 Wzrostu Poziomu Ataku i 1–5 Spadek Poziomu Obrony
594. [Status [Lensman_LowMorale] — nazwa] 정보 집착
   źródło: Bufs-exme.json :: dataList[id=Lensman_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Lensman_LowMorale]`
   limit: do 40 znaków
   EN: Intelligence Obsession
   PL: Obsesja Informacyjna
595. [Status [Lensman_LowMorale] — opis] - 정보 취득을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +10%\n- 턴 시작 시 취약 1 얻음
   źródło: Bufs-exme.json :: dataList[id=Lensman_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash against targets that have Intelligence Gathering, Base Power +1 and deal +10% damage\n- Turn Start: Gain 1 Fragile
   PL: - W Starciu z celami posiadającymi Zbieranie Informacji Moc Bazowa +1 i zadaje +10% obrażeń\n- Na początku tury zyskuje 1 Wrażliwości
596. [Status [Lensman_Panic] — nazwa] 정보 집착
   źródło: Bufs-exme.json :: dataList[id=Lensman_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Lensman_Panic]`
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Status [Lensman_Panic] — opis] - 정보 취득을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +20%\n- 턴 시작 시 취약 2 얻음
   źródło: Bufs-exme.json :: dataList[id=Lensman_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash against targets that have Intelligence Gathering, Base Power +1 and deal +20% damage\n- Turn Start: Gain 2 Fragile
   PL: - W Starciu z celami posiadającymi Zbieranie Informacji Moc Bazowa +1 i zadaje +20% obrażeń\n- Na początku tury zyskuje 2 Wrażliwości
598. [Status [Aengdu_Lowmorale] — nazwa] 원망
   źródło: Bufs-exme.json :: dataList[id=Aengdu_Lowmorale].name
   kontekst: identyfikator statusu w tekstach: `[Aengdu_Lowmorale]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
599. [Status [Aengdu_Lowmorale] — opis] - 턴 시작 시 공격 위력 증가 1, 수비 위력 감소 1 얻음\n- 턴 종료 시 다음 턴에 신속 2 얻음
   źródło: Bufs-exme.json :: dataList[id=Aengdu_Lowmorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Attack Power Up and 1 Defense Power Down\n- Turn End: Gain 2 Haste next turn
   PL: - Na początku tury zyskuje 1 Wzrost Mocy Ataku i 1 Spadek Mocy Obrony\n- Na koniec tury zyskuje 2 Pośpiechu w następnej turze
600. [Status [Aengdu_Panic] — nazwa] 원망
   źródło: Bufs-exme.json :: dataList[id=Aengdu_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Aengdu_Panic]`
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Status [Aengdu_Panic] — opis] - 턴 시작 시 공격 위력 증가 2, 수비 위력 감소 2 얻음\n턴 종료 시 다음 턴에 신속 2 얻음
   źródło: Bufs-exme.json :: dataList[id=Aengdu_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Attack Power Up and 2 Defense Power Down\n- Turn End: Gain 2 Haste next turn
   PL: - Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 2 Spadek Mocy Obrony\nNa koniec tury zyskuje 2 Pośpiechu w następnej turze
602. [Status [BrandedKimSatgat] — nazwa] 낙인[奴]
   źródło: Bufs-exme.json :: dataList[id=BrandedKimSatgat].name
   kontekst: identyfikator statusu w tekstach: `[BrandedKimSatgat]`
   limit: do 40 znaków
   EN: Brand - No [奴]
   PL: Naznaczenie - No [奴]
603. [Status [BrandedKimSatgat] — opis] - 기본 공격 레벨 ?? 감소\n- 기본 방어 레벨 ?? 감소
   źródło: Bufs-exme.json :: dataList[id=BrandedKimSatgat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -??\n- Base Defense Level -??
   PL: - Podstawowy Poziom Ataku -??\n- Podstawowy Poziom Obrony -??
604. [Status [DimensionalBagEzraETwo] — nazwa] 차원가방 - 유리아 공방
   źródło: Bufs-exme.json :: dataList[id=DimensionalBagEzraETwo].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraETwo]`
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Status [DimensionalBagEzraETwo] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 유리아 공방 도끼\n- 다음 공방 무기: 알라스 공방 장갑
   źródło: Bufs-exme.json :: dataList[id=DimensionalBagEzraETwo].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: YuRia Atelier Axe\n- Next Workshop weapon: Allas Workshop Gloves
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Siekiera Warsztatu YuRia\n- Następna broń warsztatowa: Rękawice Warsztatu Allas
606. [Status [RestingKimSatgat_LowMorale] — nazwa] 가라앉은 회한
   źródło: Bufs-exme.json :: dataList[id=RestingKimSatgat_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[RestingKimSatgat_LowMorale]`
   limit: do 40 znaków
   EN: Deep-rooted Regret
   PL: Głęboko Zakorzeniony Żal
607. [Status [RestingKimSatgat_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 피해량 감소 2 얻고 자신의 체력 40 회복
   źródło: Bufs-exme.json :: dataList[id=RestingKimSatgat_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Damage Down and heal 40 HP
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Spadek Obrażeń i leczy 40 HP
608. [Status [RestingKimSatgat_Panic] — nazwa] 가라앉은 회한
   źródło: Bufs-exme.json :: dataList[id=RestingKimSatgat_Panic].name
   kontekst: identyfikator statusu w tekstach: `[RestingKimSatgat_Panic]`
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Status [RestingKimSatgat_Panic] — opis] - 패닉\n- 턴 시작 시 피해량 감소 3 얻고 자신의 체력 60 회복
   źródło: Bufs-exme.json :: dataList[id=RestingKimSatgat_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 3 Damage Down and heal 60 HP
   PL: - Panika\n- Na początku tury zyskuje 3 Spadek Obrażeń i leczy 60 HP
610. [Status [ChoiSwordsmanship] — nazwa] 본국검술[살]
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanship].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSwordsmanship]`
   limit: do 50 znaków
   EN: Swordplay of the Homeland [Sal]
   PL: Rodzima Szermierka [Sal]
611. [Status [ChoiSwordsmanship] — opis] - 최솟값: 1, 최댓값: 9\n- 스킬 사용시 수치가 최솟값이거나 최댓값이면, 자신이 사용하는 모든 코인이 <color=#ff6000><mark color=#ff000040><b><u>파괴 불가 코인</color></mark></b></u>으로 변경됨\n- <color=#ff6000><mark color=#ff000040><b><u>수치에 따라 스킬의 기본 위력과 코인 위력에 증감이 적용됨</color></mark></b></u>\n· 1 ~ 2: 기본 위력 -6, 코인 위력 +4\n· 3 ~ 4: 기본 위력 -3, 코인 위력 +2\n· 5: 효과 없음\n· 6 ~ 7: 기본 위력 +4, 코인 위력 -2\n· 8 ~ 9: 기본 위력 +8, 코인 위력 -3
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanship].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Min Stack 1; Max Stack 9\n- On Skill Use, at Min or Max Stacks, convert all Coins this unit uses to <color=#ff6000><mark color=#ff000040><b><u>Unbreakable Coins</color></mark></b></u>\n- <color=#ff6000><mark color=#ff000040><b><u>Skill Base Power and Coin Power shift based on Stack</color></mark></b></u>\n· 1 ~ 2 Stack: Base Power -6, Coin Power +4\n· 3 ~ 4 Stack: Base Power -3, Coin Power +2\n· 5 Stack: No effect\n· 6 ~ 7 Stack: Base Power +4, Coin Power -2\n· 8 ~ 9: Base Power +8, Coin Power -3
   PL: - Min. stosów: 1, Maks. stosów: 9\n- Przy użyciu Umiejętności, jeżeli wartość wynosi Min. lub Maks., wszystkie Monety stają się <color=#ff6000><mark color=#ff000040><b><u>Niezniszczalnymi Monetami</u></b></mark></color>\n- <color=#ff6000><mark color=#ff000040><b><u>Moc Bazowa i Moc Monety Umiejętności przesuwają się zależnie od stosów</u></b></mark></color>\n· 1–2 stosy: Moc Bazowa -6, Moc Monety +4\n· 3–4 stosy: Moc Bazowa -3, Moc Monety +2\n· 5 stosów: brak efektu\n· 6–7 stosów: Moc Bazowa +4, Moc Monety -2\n· 8–9: Moc Bazowa +8, Moc Monety -3
612. [Status [ChoiSwordsmanshipOne] — nazwa] 본국태세 - 곰 사냥
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipOne].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSwordsmanshipOne]`
   limit: do 60 znaków
   EN: Battleform of the Homeland - Bearhunt
   PL: Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia
613. [Status [ChoiSwordsmanshipOne] — opis] {0}턴 뒤 본국태세를 변경함\n<color=#ff6000><mark color=#ff000040><b><u>단일 코인</color></mark></b></u> 스킬로 이루어진 패턴을 사용함\n\n본국검술[살] 수치가 <color=#ff6000><mark color=#ff000040><b><u>높을수록</color></mark></b></u> 임경업이 유리함
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipOne].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, {0}, \n
   EN: Assume a different Battleform of the Homeland after {0} turns\nUse a pattern made of <color=#ff6000><mark color=#ff000040><b><u>single-coin</color></mark></b></u> Skills\n\nIm Gyeong-eop gains advantage at <color=#ff6000><mark color=#ff000040><b><u>higher</color></mark></b></u> Swordplay of the Homeland [Sal] Stack
   PL: Po {0} turach przyjmuje inną Rodzimą Postawę Bojową\nUżywa wzorca złożonego z <color=#ff6000><mark color=#ff000040><b><u>jednomonetowych</u></b></mark></color> Umiejętności\n\nIm Gyeong-eop ma przewagę przy <color=#ff6000><mark color=#ff000040><b><u>wyższej</u></b></mark></color> wartości Sztuki Miecza Ojczyzny [Sal]
614. [Status [ChoiSwordsmanshipOne] — tekst klimatyczny] S사가 있는 19구의 산에는 온갖 짐승이 산다.\n그중에서도 곰은 그 덩치와 힘이 절벽에서 굴러오는 바위와 같아, 첫 합에서 밀리지 않고 일격에 베어내야 한다.
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipOne].flavor
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The mountains of S Corp.'s District 19 are home to all manner of beasts.\nAmongst them, the bear, in particular, boasts strength and force akin to boulders falling from the cliff in a landslide. Giving ground to the creature's charge is ill-advised—one must aim to hew it down with the first slash of the blade.
   PL: W górach Dystryktu 19 Korporacji S żyją rozmaite bestie.\nSpośród nich niedźwiedź ma siłę i potęgę skał toczących się z urwiska — nie wolno dać się odepchnąć w pierwszym Starciu; trzeba ściąć go jednym ciosem.
615. [Status [ChoiSwordsmanshipMany] — nazwa] 본국태세 - 범 사냥
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipMany].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSwordsmanshipMany]`
   limit: do 60 znaków
   EN: Battleform of the Homeland - Tigerhunt
   PL: Rodzima Postawa Bojowa - Polowanie na Tygrysa
616. [Status [ChoiSwordsmanshipMany] — opis] {0}턴 뒤 본국태세를 변경함\n<color=#ff6000><mark color=#ff000040><b><u>다 코인</color></mark></b></u> 스킬로 이루어진 패턴을 사용함\n\n본국검술[살] 수치가 <color=#ff6000><mark color=#ff000040><b><u>낮을수록</color></mark></b></u> 임경업이 유리함
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipMany].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, {0}, \n
   EN: Assume a different Battleform of the Homeland after {0} turns\nUse a pattern made of <color=#ff6000><mark color=#ff000040><b><u>multi-coin</color></mark></b></u> Skills\n\nIm Gyeong-eop gains advantage at <color=#ff6000><mark color=#ff000040><b><u>lower</color></mark></b></u> Swordplay of the Homeland [Sal] Stack
   PL: Po {0} turach przyjmuje inną Rodzimą Postawę Bojową\nUżywa wzorca złożonego z <color=#ff6000><mark color=#ff000040><b><u>wielumonetowych</u></b></mark></color> Umiejętności\n\nIm Gyeong-eop ma przewagę przy <color=#ff6000><mark color=#ff000040><b><u>niższej</u></b></mark></color> wartości Sztuki Miecza Ojczyzny [Sal]
617. [Status [ChoiSwordsmanshipMany] — tekst klimatyczny] 범은 영리하고 포악하다.\n일격에 살을 내어주는 범은 없다. 끝없이 몰아치는 연격으로 범의 숨통을 조이고, 끝내 그 목숨을 쳐내야 한다.\n그러지 못해 살아남은 범은 언젠가 산군이 된다.\n그것이 사람에게 영험한 운수를 안겨줄지, 악독한 재액으로 되돌아올지는 알 수 없다.
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipMany].flavor
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tigers are cunning and ferocious.\nOne cannot hope to cut through a tiger's flesh with a single stroke. Only a relentless flurry of chained slashes can overwhelm the creature until it is felled at last.\nFail to do so, and the tiger will escape death—or best its opponent to one day grow into a Sangun, a Lord of the Mountain.\nWhether these beings will grant auspicious fortune on men or return as malevolent calamity is impossible to tell.
   PL: Tygrys jest sprytny i dziki.\nŻadnego tygrysa nie ściągnie się jednym ciosem. Tylko nieustanna fala kolejnych cięć dusi bestię, aż w końcu odbierze jej życie.\nTen, który przeżyje, kiedyś stanie się Sangun, Panem Gór.\nCzy zesle ludziom szczęście, czy wróci jako złośliwa klęska — nie sposób wiedzieć.
618. [Status [ChoiSwordsmanshipShield] — nazwa] 두정갑[살]
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipShield].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSwordsmanshipShield]`
   limit: do 40 znaków
   EN: Dujeong Brigandine [Sal]
   PL: Kolczuga Dujeong [Sal]
619. [Status [ChoiSwordsmanshipShield] — opis] - 최댓값: 5\n- 이 효과를 얻을 때, 수치당 자신의 최대 체력의 10%만큼의 보호막을 얻음 (최소 1, 소수점 버림, 이 효과로 얻은 보호막은 턴 종료시에도 사라지지 않음)\n- 전투 시작시, 수치 2당 방어 레벨 감소 1 얻음 (소수점 올림)\n- 참격 피해량 +(수치 x 2.5)%\n- <color=#ff6000><mark color=#ff000040><b><u>최대 체력의 10%에 해당하는 보호막 피해를 받았을 때 수치 1 감소</color></mark></b></u> (현재 수치 감소까지 남은 보호막 피해량 : {0})
   źródło: Bufs-exme.json :: dataList[id=ChoiSwordsmanshipShield].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, {0}, \n
   EN: - Max Stack: 5\n- When gaining this effect, gain Shield equal to 10% of this unit's max HP for every Stack (min 1, rounded down; Shield gained due to this effect does not expire at Turn End)\n- Combat Start: Gain 1 Defense Level Down for every 2 Stack (rounded up)\n- Deal +(Stack x 2.5)% Slash damage\n- <color=#ff6000><mark color=#ff000040><b><u>Lose 1 Stack when taking Shield damage equal to 10% of this unit's max HP</color></mark></b></u> (Remaining Shield damage until Stack loss: {0})
   PL: - Maks.: 5\n- Przy zyskaniu tego efektu zyskuje Tarczę równą 10% Maks. HP za każdą wartość (min. 1, zaokrąglona w dół; Tarcza zyskana dzięki temu efektowi nie znika na koniec tury)\n- Na początku walki za każde 2 wartości zyskuje 1 Spadek Poziomu Obrony (zaokrąglona w górę)\n- Zadaje +(wartość x 2.5)% obrażeń Cięcia\n- <color=#ff6000><mark color=#ff000040><b><u>Po otrzymaniu obrażeń Tarczy równych 10% Maks. HP traci 1 wartości</u></b></mark></color> (obrażenia Tarczy pozostałe do utraty wartości: {0})
620. [Status [PhotoTransitionChoi] — nazwa] 기억 전환
   źródło: Bufs-exme.json :: dataList[id=PhotoTransitionChoi].name
   kontekst: identyfikator statusu w tekstach: `[PhotoTransitionChoi]`
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Status [PhotoTransitionChoi] — opis] - 기본값: 3\n- 턴 종료 시 수치 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>턴 시작 시 수치가 0이면, 퇴각하고 맵이 변경됨</color></mark></b></u>\n- 복귀 시 퇴각해있던 턴 만큼 본국태세에 따라 본국검술[살]을 얻거나 잃음\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: Bufs-exme.json :: dataList[id=PhotoTransitionChoi].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>Turn Start: At 0 Stack, Retreat and transition into a different location</color></mark></b></u>\n- When Returning to the field, based on current Battleform of the Homeland, gain or lose (# of turns spent in Retreat) Swordplay of the Homeland [Sal] Stack\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury maleje o 1\n- <color=#ff6000><mark color=#ff000040><b><u>Na początku tury przy 0 stosów wycofuje się, a mapa się zmienia</u></b></mark></color>\n- Przy powrocie na pole, zależnie od aktualnej Rodzimej Postawy Bojowej, zyskuje lub traci Rodzimą Szermierkę [Sal] w liczbie tur spędzonych w odwrocie\n· Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia: zyskuje\n· Rodzima Postawa Bojowa - Polowanie na Tygrysa: traci
622. [Status [PhotoTransitionChoiCamera] — nazwa] 기억 전환
   źródło: Bufs-exme.json :: dataList[id=PhotoTransitionChoiCamera].name
   kontekst: identyfikator statusu w tekstach: `[PhotoTransitionChoiCamera]`
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Status [PhotoTransitionChoiCamera] — opis] - 기본값: 3\n- 턴 종료 시 수치 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>턴 시작 시 수치가 0이면, 소멸하고 맵이 변경됨</color></mark></b></u>\n- 임경업이 퇴각한 턴 만큼 복귀 시 임경업의 본국태세에 따라 임경업이 본국검술[살]을 얻거나 잃음 (현재 {0}턴)\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: Bufs-exme.json :: dataList[id=PhotoTransitionChoiCamera].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, {0}, \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>Turn Start: At 0 Stack, remove this unit and transition to a different location</color></mark></b></u>\n- When Returning to the field, based on Im Gyeong-eop's current Battleform of the Homeland, Im Gyeong-eop gains or loses (# of turns Im Gyeong-eop spent in Retreat) Swordplay of the Homeland [Sal] Stack (Currently at {0} turns)\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury wartość maleje o 1\n- <color=#ff6000><mark color=#ff000040><b><u>Na początek tury przy wartości 0 znika i mapa ulega zmianie</u></b></mark></color>\n- Po powrocie na pole walki, zależnie od liczby tur spędzonych na wycofaniu, Im Gyeong-eop zyskuje lub traci wartość Sztuki Miecza Ojczyzny [Sal] zgodnie z obecną Rodzimą Postawą Bojową (obecnie {0} tur)\n· Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia: zyskuje\n· Rodzima Postawa Bojowa - Polowanie na Tygrysa: traci
624. [Status [ChoiSword_LowMorale] — nazwa] 현상된 기억
   źródło: Bufs-exme.json :: dataList[id=ChoiSword_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSword_LowMorale]`
   limit: do 40 znaków
   EN: Developed Memories
   PL: Rozwinięte Wspomnienia
625. [Status [ChoiSword_LowMorale] — opis] - 사기 저하\n- 취약 1 얻음, 피해량 +10%, 크리티컬 피해량 +15%
   źródło: Bufs-exme.json :: dataList[id=ChoiSword_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile, deal +10% damage, and deal +15% damage on Critical Hit
   PL: - Niskie Morale\n- Zyskuje 1 Wrażliwości, zadaje +10% obrażeń i +15% obrażeń Krytycznych
626. [Status [ChoiSword_Panic] — nazwa] 현상된 기억
   źródło: Bufs-exme.json :: dataList[id=ChoiSword_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ChoiSword_Panic]`
   (powtórzenie elementu 624 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Status [ChoiSword_Panic] — opis] - 패닉\n- 취약 2 얻음, 피해량 +10%, 크리티컬 피해량 +30%, 본국궁[살] - 살 날리기의 코인으로 부여하는 효과 2배로 부여
   źródło: Bufs-exme.json :: dataList[id=ChoiSword_Panic].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Fragile, deal +10% damage, deal +30% damage on Critical Hit, and double the effects inflicted by the Coins of the "Bow of the Homeland [Sal] - Arrowloose" Skill
   PL: - Panika\n- Zyskuje 2 Wrażliwości, zadaje +10% obrażeń, +30% obrażeń Krytycznych i podwaja efekty nakładane przez Monety Umiejętności „Rodzimego Łuku [Sal] - Wypuszczenia Strzały”
628. [Status [DimensionalBagEzraDTwo] — nazwa] 차원가방 - 나미르 공방
   źródło: Bufs-exme.json :: dataList[id=DimensionalBagEzraDTwo].name
   kontekst: identyfikator statusu w tekstach: `[DimensionalBagEzraDTwo]`
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Status [DimensionalBagEzraDTwo] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 나미르 공방 건틀릿\n- 다음 공방 무기: 유리아 공방 도끼
   źródło: Bufs-exme.json :: dataList[id=DimensionalBagEzraDTwo].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Namir Workshop Gauntlets\n- Next Workshop weapon: YuRia Atelier Axe
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Gauntlety Warsztatu Namir\n- Następna broń warsztatowa: Siekiera Warsztatu YuRia
630. [Status [DimensionalBagEzraDTwo] — tekst klimatyczny] “G사 특이점인 구가 들어간 제품인데, 잘 쓰려면 공중에서 스위치를 눌러 발동시킨 다음, 무게로 찍어 눌러야 해. 제대로 꽂히면 진짜 아파!”
   źródło: Bufs-exme.json :: dataList[id=DimensionalBagEzraDTwo].flavor
   (powtórzenie elementu 221 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Status [SlaveHunersPower] — nazwa] 압송 명령
   źródło: Bufs-exme.json :: dataList[id=SlaveHunersPower].name
   kontekst: identyfikator statusu w tekstach: `[SlaveHunersPower]`
   limit: do 40 znaków
   EN: Prisoner Transport Order
   PL: Rozkaz Konwoju
632. [Status [SlaveHunersPower] — opis] - 기본 공격 레벨 5 증가\n- 기본 방어 레벨 5 증가
   źródło: Bufs-exme.json :: dataList[id=SlaveHunersPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +5\n- Base Defense Level +5
   PL: - Podstawowy Poziom Ataku +5\n- Podstawowy Poziom Obrony +5
633. [Status [LensmanPower] — nazwa] 조사 명령
   źródło: Bufs-exme.json :: dataList[id=LensmanPower].name
   kontekst: identyfikator statusu w tekstach: `[LensmanPower]`
   limit: do 40 znaków
   EN: Investigation Order
   PL: Rozkaz Śledztwa
634. [Status [LensmanPower] — opis] - 기본 공격 레벨 5 증가\n- 기본 방어 레벨 5 증가
   źródło: Bufs-exme.json :: dataList[id=LensmanPower].desc
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-fools
- plik gry: `Bufs-fools.json`

635. [Status [CandyForCharon] — nazwa] 사탕?
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon].name
   kontekst: identyfikator statusu w tekstach: `[CandyForCharon]`
   limit: do 40 znaków
   EN: Candy?
   PL: Cukierek?
636. [Status [CandyForCharon] — opis] - 최댓값: 1\n- 사탕을 가지고 있을까?
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Where's the candy?
   PL: - Maks. wartości: 1\n- Czy będzie miał cukierek?
637. [Status [TickTockTickTock] — nazwa] 째깍째깍?!
   źródło: Bufs-fools.json :: dataList[id=TickTockTickTock].name
   kontekst: identyfikator statusu w tekstach: `[TickTockTickTock]`
   limit: do 40 znaków
   EN: Tick-Tock?!
   PL: Tik-Tak?!
638. [Status [TickTockTickTock] — opis] - 턴 종료 시, 정신력을 10 회복
   źródło: Bufs-fools.json :: dataList[id=TickTockTickTock].desc
   limit: do 120 znaków
   EN: - Heal 10 SP at Turn End
   PL: - Na koniec tury odzyskuje 10 Poczytalności
639. [Status [CandyForCharon_LowMorale] — nazwa] 사탕
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[CandyForCharon_LowMorale]`
   limit: do 40 znaków
   EN: Candy
   PL: Cukierek
640. [Status [CandyForCharon_LowMorale] — opis] - 사기 저하\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +3, 그 외의 인격과 합 진행시, 합 위력 -1
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When Clashing against Identities with Candy, Clash Power +3; when clashing against other Identities, Clash Power -1
   PL: - Obniżone Morale\n- W Starciu z tożsamością posiadającą Cukierek Moc Starcia +3; w Starciu z pozostałymi tożsamościami Moc Starcia -1
641. [Status [CandyForCharon_LowMorale] — podsumowanie] 조건에 따라 합위력 증감
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_LowMorale].summary
   limit: do 120 znaków
   EN: Conditional Clash Power increase
   PL: Warunkowe Wahanie Mocy Starcia
642. [Status [CandyForCharon_Panic] — nazwa] 사탕
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_Panic].name
   kontekst: identyfikator statusu w tekstach: `[CandyForCharon_Panic]`
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Status [CandyForCharon_Panic] — opis] - 패닉\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +5, 그 외의 인격과 합 진행시, 합 위력 -2
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- When Clashing against Identities with Candy, Clash Power +5; when clashing against other Identities, Clash Power -2
   PL: - Panika\n- W Starciu z tożsamością posiadającą Cukierek Moc Starcia +5; w Starciu z pozostałymi tożsamościami Moc Starcia -2
644. [Status [CandyForCharon_Panic] — podsumowanie] 조건에 따라 합위력 증감
   źródło: Bufs-fools.json :: dataList[id=CandyForCharon_Panic].summary
   (powtórzenie elementu 641 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Statusy i efekty bojowe — Bufs-mowe
- plik gry: `Bufs-mowe.json`

645. [Status [KeptBlood] — nazwa] 머금은 피
   źródło: Bufs-mowe.json :: dataList[id=KeptBlood].name
   kontekst: identyfikator statusu w tekstach: `[KeptBlood]`
   limit: do 40 znaków
   EN: Stored Blood
   PL: Zmagazynowana Krew
646. [Status [KeptBlood] — opis] - 최대 10\n- 최대 체력의 5%를 잃을 때마다 1씩 감소함.\n- 적중 시 최대 체력의 1%만큼 체력 회복
   źródło: Bufs-mowe.json :: dataList[id=KeptBlood].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Lose 1 value every time this unit loses 5% HP.\n- On Hit, heal 1% of this unit's HP
   PL: - Maks. 10\n- Traci 1 wartości za każde utracone 5% Maks. HP.\n- Przy trafieniu leczy 1% HP
647. [Status [BloodyCrave] — nazwa] 핏빛 갈구
   źródło: Bufs-mowe.json :: dataList[id=BloodyCrave].name
   kontekst: identyfikator statusu w tekstach: `[BloodyCrave]`
   limit: do 40 znaków
   EN: Bloodtinged Craving
   PL: Krwawa Żądza
648. [Status [BloodyCrave] — opis] - 합 위력 증가 1 , 피해량 증가 1 얻음\n- 적중 시, 머금은 피를  1 얻음\n- 이번 턴에 머금은 피를 얻지 못했다면,  매 턴 얻는 효과 대신 다음 턴에 취약 2, 신속 1, 공격 레벨 증가 4 얻음
   źródło: Bufs-mowe.json :: dataList[id=BloodyCrave].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Clash Power Up and 1 Damage Up\n- On Hit, gain 1 Stored Blood\n- If this unit did not gain Stored Blood this turn, gain 2 Fragile, 1 Haste, and 4 Offense Level Up next turn instead of the above effect
   PL: - Zyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń\n- Przy trafieniu zyskuje 1 Zmagazynowanej Krwi\n- Jeżeli w tej turze nie zdobył Zmagazynowanej Krwi, zamiast powyższych efektów zyskuje w następnej turze 2 Wrażliwości, 1 Pośpiech i 4 Wzrostu Poziomu Ataku
649. [Status [BloodPocket_LowMorale] — nazwa] 흡혈 갈망
   źródło: Bufs-mowe.json :: dataList[id=BloodPocket_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BloodPocket_LowMorale]`
   limit: do 40 znaków
   EN: Bloodthirst
   PL: Krwiożerczość
