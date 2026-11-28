# Paczka AI P67 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 3/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P67_3c_przeciwnicy_i_anomalie_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P67_3c_przeciwnicy_i_anomalie_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [a1c10p1] Pasywka wroga: Passives_Abnormality-a1c10p1
- plik gry: `Passives_Abnormality-a1c10p1.json`

1. [[a1c10p1] Pasywka wroga [149402] — opis] 자신의 [ChargeRouge] 위력 1당 자신의 스킬 피해량 +1% (최대 10%)\n\n스킬 사용 시 자신의 체력이 50% 미만이면, 해당 스킬로 얻는 [ChargeRouge] 횟수 +2\n자신의 잃은 체력 1%당 스킬 피해량 +1%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149402].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Skills deal +1% damage for every [ChargeRouge] Potency on self (max 10%)\n\nOn Skill Use, if this unit has less than 50% HP, the said Skill gains +2 more [ChargeRouge] Count\nSkills deal +1% damage for every 1% missing HP on self
   PL: Umiejętności zadają +1% obrażeń za każde 1 Siły [ChargeRouge] tej jednostki (maks. 10%)\n\nprzy użyciu Umiejętności, jeżeli ta jednostka ma mniej niż 50% HP, ta Umiejętność zyskuje dodatkowo 2 Licznika [ChargeRouge]\nUmiejętności zadają +1% obrażeń za każde 1% utraconego HP tej jednostki
2. [[a1c10p1] Pasywka wroga [149301] — nazwa] 르루주 자켓
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149301].name
   limit: do 40 znaków
   EN: Le Rouge: Jacket
   PL: Le Rouge: Jacket
3. [[a1c10p1] Pasywka wroga [149301] — opis] 턴 종료시, [ChargeRouge] 횟수를 최대 10까지 얻거나 잃음\n\n자신이 피격당할 때, 공격자가 [Charge]을 얻는 스킬을 사용했으면 [Charge] 횟수 1을 공격자에게 옮김 (공격자 스킬당 1회)\n해당 효과가 발동될 때마다 [AttackUp] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149301].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [Charge], [AttackUp]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Charge] = 충전 / Charge; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn End: Gain or lose up to 10 [ChargeRouge] Count\n\nWhen hit, if the attacker used Skills that gain [Charge], transfer 1 [ChargeRouge] Count as [Charge] Count to the attacker (once per the attacker's Skill)\nGain 1 [AttackUp] every time the effect above activates
   PL: Koniec tury: zyskuje lub traci do 10 Licznika [ChargeRouge]\n\nPrzy trafieniu, jeżeli atakujący użył Umiejętności zyskujących [Charge], przenosi na atakującego 1 Licznika [ChargeRouge] jako 1 Licznika [Charge] (1 raz na Umiejętność atakującego)\nza każde uruchomienie powyższego efektu zyskuje 1 [AttackUp]
4. [[a1c10p1] Pasywka wroga [149302] — nazwa] 절박함
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149302].name
   limit: do 40 znaków
   EN: Desperation
   PL: Desperation
5. [[a1c10p1] Pasywka wroga [149302] — opis] 턴 시작 시 자신의 [ChargeRouge]이 3, [ChargeRouge] 횟수가 10 이상이면 '공격적 마케팅' 사용\n\n자신의 잃은 체력 1%당 스킬 피해량 +1%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149302].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Turn Start: At 3+ [ChargeRouge] Potency and 10+ [ChargeRouge] Count, use "Aggressive Marketing" Skill\n\nSkills deal +1% damage for every 1% missing HP on self
   PL: Początek tury: przy 3+ Siły [ChargeRouge] i 10+ Licznika [ChargeRouge] używa Umiejętności „Aggressive Marketing”\n\nUmiejętności zadają +1% obrażeń za każde 1% utraconego HP tej jednostki
6. [[a1c10p1] Pasywka wroga [149303] — nazwa] 들려… 또 다른 신의 목소리가…
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149303].name
   limit: do 60 znaków
   EN: I hear it... the Voice of another god...!
   PL: I hear it... the Voice of another god...!
7. [[a1c10p1] Pasywka wroga [149303] — opis] 스테이지 시작 시, [RisingMadnessRouge] 얻음\n- 턴 시작 시 이번 전투에서 체력이 처음으로 50% 이하가 되면,\n[RisingMadnessRouge]이 [RisingMadnessRouge2nd]로 변경됨\n\n합 패배 시, [ChargeRouge] 횟수 2 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149303].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [RisingMadnessRouge], [RisingMadnessRouge2nd], [ChargeRouge]
   znaczenie tagów: [RisingMadnessRouge] = 햇살 / Sunshine; [RisingMadnessRouge2nd] = 따가운 햇살 / Stinging Sunshine; [ChargeRouge] = 맥동 / Pulsation
   EN: Encounter Start: Gain [RisingMadnessRouge]\n- Turn Start: When this unit's HP drops below 50% for the first time in this Encounter, convert [RisingMadnessRouge] into [RisingMadnessRouge2nd]\n\nOn Clash Lose, gain +2 [ChargeRouge] Count
   PL: Na początku etapu: zyskuje [RisingMadnessRouge]\n- Początek tury: gdy HP tej jednostki po raz pierwszy w tej walce spadnie poniżej 50%, [RisingMadnessRouge] zamienia się w [RisingMadnessRouge2nd]\n\nPo przegranej w Starciu zyskuje 2 Licznika [ChargeRouge]
8. [[a1c10p1] Pasywka wroga [149303] — tekst klimatyczny] 따듯한 목소리를 들었지만 더 변하지 못하고 육신에 정신이 갇힌 채 분열로 광증에 빠졌다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149303].flavor
   limit: do 200 znaków
   EN: They heard the warm Voice, yet could change no further. With the mind trapped within the flesh, the self schismatized from itself and fell into madness.
   PL: Usłyszeli ciepły Głos, lecz nie mogli już dalej się zmienić. Z umysłem uwięzionym w ciele jaźń rozpadła się sama ze sobą i popadła w obłęd.
9. [[a1c10p1] Pasywka wroga [146601] — nazwa] 르루주 부티크 신상 룩북
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146601].name
   limit: do 60 znaków
   EN: Boutique du Rouge: New Arrivals Lookbook
   PL: Boutique du Rouge: New Arrivals Lookbook
10. [[a1c10p1] Pasywka wroga [146601] — opis] [RougeThreeNormal] 패턴\n\n보유한 [RougeThreeCocoon], [RougeThreeCocoonShield]을 제거하고, [RougeThreeNormal]을 얻음\n<color=#ff6000><mark=#ff000040><b><u>피격 시, [RougeThreeNormal] 1 얻음\n턴 종료시 [RougeThreeNormal]이 20이면, 다음 턴에 [RougeThreeCocoon] 패턴으로 변경됨</u></b></mark></color>\n\n[RougeThreeNormal] 상태에서 체력이 10 미만이 되는 피해를 받으면, 해당 피해를 받지 않고 최대 체력의 30%만큼 체력 회복하고 턴을 종료. 이후 [RougeThreeCocoon] 상태로 변경되고 이번 전투 동안 [Enhancement] 2 얻음 (전투당 1회)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146601].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RougeThreeNormal], [RougeThreeCocoon], [RougeThreeCocoonShield], [Enhancement]
   znaczenie tagów: [RougeThreeNormal] = 부티크 신상옷 / Boutique: New Releases; [RougeThreeCocoon] = 탈의실 / Changing Room; [RougeThreeCocoonShield] = 믿음 / Devotion; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: [RougeThreeNormal] Pattern\n\nRemove [RougeThreeCocoon] and [RougeThreeCocoonShield] on self, and gain [RougeThreeNormal]\n<color=#ff6000><mark=#ff000040><b><u>When hit, gain 1 [RougeThreeNormal]\nTurn End: At 20 [RougeThreeNormal], enter [RougeThreeCocoon] pattern next turn</u></b></mark></color>\n\nWhile in [RougeThreeNormal] state:\nIf this unit takes damage that brings its HP below 10, nullify that damage, heal 30% HP, and end the turn. Then, this unit enters [RougeThreeCocoon] state and gains 2 [Enhancement] for the rest of this Encounter (once per Encounter)
   PL: wzorzec [RougeThreeNormal]\n\nusuwa [RougeThreeCocoon] i [RougeThreeCocoonShield] z tej jednostki i zyskuje [RougeThreeNormal]\n<color=#ff6000><mark=#ff000040><b><u>przy trafieniu zyskuje 1 [RougeThreeNormal]\nKoniec tury: przy 20 [RougeThreeNormal] w następnej turze wchodzi we wzorzec [RougeThreeCocoon]</u></b></mark></color>\n\nw stanie [RougeThreeNormal]:\njeżeli ta jednostka otrzyma obrażenia sprowadzające jej HP poniżej 10, niweluje te obrażenia, przywraca 30% HP i kończy turę. Następnie wchodzi w stan [RougeThreeCocoon] i na resztę tej walki zyskuje 2 [Enhancement] (1 raz na walkę)
11. [[a1c10p1] Pasywka wroga [146602] — nazwa] 탈의실 속으로
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146602].name
   limit: do 40 znaków
   EN: Into the Changing Room
   PL: Into the Changing Room
12. [[a1c10p1] Pasywka wroga [146602] — opis] [RougeThreeCocoon] 패턴\n\n보유한 [RougeThreeNormal]을 제거하고 [RougeThreeCocoon] 1, [RougeThreeCocoonShield] 500 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>피격 시, [RougeThreeCocoonHit]을 얻음</u></b></mark></color>\n[RougeThreeCocoonShield]이 0이 되거나 [RougeThreeCocoon]이 3이 되면 정신력이 20 감소하고 턴 종료. 다음 턴에 [RougeThreeNormal] 패턴으로 변경되고 이번 전투 동안 [AttackDmgUp] 1 얻음 (흐트러짐 상태였으면 흐트러짐 상태를 해제)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=146602].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RougeThreeCocoon], [RougeThreeNormal], [RougeThreeCocoonShield], [RougeThreeCocoonHit], [AttackDmgUp]
   znaczenie tagów: [RougeThreeCocoon] = 탈의실 / Changing Room; [RougeThreeNormal] = 부티크 신상옷 / Boutique: New Releases; [RougeThreeCocoonShield] = 믿음 / Devotion; [RougeThreeCocoonHit] = 핍박 / Persecution; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [RougeThreeCocoon] Pattern\n\nRemove [RougeThreeNormal] on self. Gain 1 [RougeThreeCocoon] and 500 [RougeThreeCocoonShield]\n\n<color=#ff6000><mark=#ff000040><b><u>When hit, gain [RougeThreeCocoonHit]</u></b></mark></color>\nAt 0 [RougeThreeCocoonShield] or 3 [RougeThreeCocoon], lose 20 SP and end the turn. Then, enter [RougeThreeNormal] pattern next turn and gain 1 [AttackDmgUp] for the rest of this Encounter (if this unit is Staggered, recover from Stagger)
   PL: wzorzec [RougeThreeCocoon]\n\nusuwa [RougeThreeNormal] z tej jednostki. Zyskuje 1 [RougeThreeCocoon] i 500 [RougeThreeCocoonShield]\n\n<color=#ff6000><mark=#ff000040><b><u>przy trafieniu zyskuje [RougeThreeCocoonHit]</u></b></mark></color>\nprzy 0 [RougeThreeCocoonShield] lub 3 [RougeThreeCocoon] traci 20 SP i kończy turę. Następnie wchodzi w następnej turze we wzorzec [RougeThreeNormal] i na resztę tej walki zyskuje 1 [AttackDmgUp] (jeżeli ta jednostka jest Oszołamiona, dochodzi do siebie)
13. [[a1c10p1] Pasywka wroga [147401] — nazwa] 수셰프
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147401].name
   limit: do 40 znaków
   EN: Sous Chef
   PL: Sous Chef
14. [[a1c10p1] Pasywka wroga [147401] — opis] <color=#ff6000><mark=#ff000040><b><u>공격 스킬로 대상 처치 시 [SapsareeCooking] 1 얻음</u></b></mark></color>\n- 스킬 사용 시 대상이 보유했던 효과 3개당, [SapsareeCooking] 1 추가 얻음 (최대 2 얻음)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147401].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SapsareeCooking]
   znaczenie tagów: [SapsareeCooking] = 토막난 요리재료 / Chopped Ingredients
   EN: <color=#ff6000><mark=#ff000040><b><u>Upon killing a target using Attack Skills, gain 1 [SapsareeCooking]</u></b></mark></color>\n- On Skill Use, gain 1 more [SapsareeCooking] for every 3 status effects on the said target (max 2)
   PL: <color=#ff6000><mark=#ff000040><b><u>przy zabiciu celu Umiejętnością ataku zyskuje 1 [SapsareeCooking]</u></b></mark></color>\n- przy użyciu Umiejętności zyskuje dodatkowo 1 [SapsareeCooking] za każde 3 efektów statusu tego celu (maks. 2)
15. [[a1c10p1] Pasywka wroga [147401] — tekst klimatyczny] 칭호는 셰프지만, 5층 레스토랑에서는 결코 인정받지 못한다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147401].flavor
   limit: do 120 znaków
   EN: She may wear the title, but the restaurant on 5F would laugh her out of the kitchen.
   PL: Choć nosi ten tytuł, restauracja na 5F wyśmiałaby ją z kuchni.
16. [[a1c10p1] Pasywka wroga [147402] — nazwa] 요리를 잘한다는 거예요
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147402].name
   limit: do 70 znaków
   EN: I can cook up delicious dishes so good, you hear?
   PL: I can cook up delicious dishes so good, you hear?
17. [[a1c10p1] Pasywka wroga [147402] — opis] <color=#ff6000><mark=#ff000040><b><u>[SapsareeCooking] 보유 시, 턴의 마지막 순서에 ‘앗! 제 식사시간인거예요’ 스킬 사용</u></b></mark></color>\n(자신을 제외한 모든 대상이 사망했거나, 흐트러짐 상태에서는 발동하지 않음)\n턴 종료 시 ‘앗! 제 식사시간인거예요’ 스킬을 사용하지 못했다면, [SapsareeHungry] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147402].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SapsareeCooking], [SapsareeHungry]
   znaczenie tagów: [SapsareeCooking] = 토막난 요리재료 / Chopped Ingredients; [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: <color=#ff6000><mark=#ff000040><b><u>If this unit has [SapsareeCooking], use the "Aah! I'm on lunch break, you hear?" Skill at the very end of the turn</u></b></mark></color>\n(does not activate if all other targets are defeated, or if this unit is Staggered)\nTurn End: If this unit failed to use the "Aah! I'm on lunch break, you hear?" Skill, gain 1 [SapsareeHungry]
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli ta jednostka ma [SapsareeCooking], używa na samym końcu tury Umiejętności „Aah! I'm on lunch break, you hear?”</u></b></mark></color>\n(nie uruchamia się, jeżeli wszystkie inne cele zostały pokonane albo ta jednostka jest Oszołamiona)\nKoniec tury: jeżeli ta jednostka nie użyła Umiejętności „Aah! I'm on lunch break, you hear?”, zyskuje 1 [SapsareeHungry]
18. [[a1c10p1] Pasywka wroga [147402] — tekst klimatyczny] 5층 레스토랑에서 이런 건 요리라 불러주지도 않는다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147402].flavor
   limit: do 120 znaków
   EN: The restaurant on 5F would not dignify this with the word "cooking."
   PL: Restauracja na 5F nie raczyłaby nazwać tego słowem „gotowanie”.
19. [[a1c10p1] Pasywka wroga [147403] — nazwa] 요리욕구
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147403].name
   limit: do 40 znaków
   EN: Culinary Ambitions
   PL: Culinary Ambitions
20. [[a1c10p1] Pasywka wroga [147403] — opis] 4턴마다 강력한 탐식 스킬 사용\n(흐트러짐으로 발동되지 못한 경우, 다음 턴에 발동)\n- 턴 종료 시 [SapsareeYammi]가 5 이상이면, 다음 턴에 강력한 탐식 스킬 사용\n\n턴 종료 시 [SapsareeHungry]가 3 이상이면, 다음 턴에 강력한 분노 스킬 사용
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147403].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [SapsareeYammi], [SapsareeHungry]
   znaczenie tagów: [SapsareeYammi] = 맛있는거 먹고 힘난다는거예요 / Eat yummies and perk up, you hear?; [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: Use a powerful Gluttony Skill every 4 turns\n(If this effect could not be activated due to Stagger, activate it next turn)\n- Turn End: At 5+ [SapsareeYammi], use a powerful Gluttony Skill next turn\n\nTurn End: At 3+ [SapsareeHungry], use a powerful Wrath Skill next turn
   PL: co 4 tury używa potężnej Umiejętności Obżarstwa\n(jeżeli efekt nie mógł się uruchomić przez Oszołamienie, uruchamia się w następnej turze)\n- Koniec tury: przy 5+ [SapsareeYammi] używa w następnej turze potężnej Umiejętności Obżarstwa\n\nKoniec tury: przy 3+ [SapsareeHungry] używa w następnej turze potężnej Umiejętności Gniewu
21. [[a1c10p1] Pasywka wroga [147403] — tekst klimatyczny] 먹을 것을 만드는 것과 요리를 하는 것은 다르다. 너는 그냥… 먹을 수 있게만 할 뿐.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147403].flavor
   limit: do 190 znaków
   EN: There is a world of difference between the culinary arts and making something edible. As for you... well, you fall solidly into the latter category.
   PL: Między sztuką kulinarną a robieniem czegoś zjadliwego dzieli przepaść. A ty... cóż, zaliczasz się do tej drugiej kategorii.
22. [[a1c10p1] Pasywka wroga [147404] — nazwa] 맛있는 거예요!!!
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147404].name
   limit: do 40 znaków
   EN: Yummies yummers, you hear?
   PL: Yummies yummers, you hear?
23. [[a1c10p1] Pasywka wroga [147404] — opis] 턴 시작 시 보유한 [SapsareeYammi] 1당, 정신력 3 회복
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147404].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SapsareeYammi]
   znaczenie tagów: [SapsareeYammi] = 맛있는거 먹고 힘난다는거예요 / Eat yummies and perk up, you hear?
   EN: Turn Start: Heal 3 SP for every [SapsareeYammi] on self
   PL: Początek tury: przywraca 3 SP za każde 1 [SapsareeYammi] tej jednostki
24. [[a1c10p1] Pasywka wroga [147404] — tekst klimatyczny] 푸드코트에 있는 것들이 맛을 논할 수나 있을까?
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147404].flavor
   limit: do 130 znaków
   EN: Do they even deserve to engage in discourse on flavor? They live in a Food Court, for heaven's sake.
   PL: Czy oni w ogóle zasługują na roztrząsanie smaku? Przecież mieszkają w Food Courcie.
25. [[a1c10p1] Pasywka wroga [147405] — nazwa] 도망가는 거예요!
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147405].name
   limit: do 40 znaków
   EN: Flit and flee, you hear?
   PL: Flit and flee, you hear?
26. [[a1c10p1] Pasywka wroga [147405] — opis] 수셰프의 체력이 30% 미만이 되면, 전투가 종료됨
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147405].desc
   limit: do 120 znaków
   EN: End the Encounter when Sous Chef's HP falls below 30%
   PL: walka kończy się, gdy HP Sous Chefa spadnie poniżej 30%
27. [[a1c10p1] Pasywka wroga [147405] — tekst klimatyczny] 죽고 싶진 않다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147405].flavor
   limit: do 120 znaków
   EN: Not willing to die for this.
   PL: Not willing to die for this.
28. [[a1c10p1] Pasywka wroga [147501] — nazwa] 맛있는 요리 재료.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147501].name
   limit: do 50 znaków
   EN: Flavorful Cooking Ingredient.
   PL: Flavorful Cooking Ingredient.
29. [[a1c10p1] Pasywka wroga [147501] — opis] 자신이 보유한 효과가 5개 이상이면 공격 레벨 3, 방어 레벨 3 증가
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147501].desc
   limit: do 120 znaków
   EN: If this unit has 5 or more status effects, gain 3 Offense Level and 3 Defense Level
   PL: jeżeli ta jednostka ma 5+ efektów statusu, zyskuje 3 Poziomu Ataku i 3 Poziomu Obrony
30. [[a1c10p1] Pasywka wroga [147501] — tekst klimatyczny] 이런 건 식재료도 아니다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147501].flavor
   limit: do 120 znaków
   EN: This isn't even a cooking ingredient.
   PL: To nawet nie jest składnik kuchenny.
31. [[a1c10p1] Pasywka wroga [147502] — nazwa] 연육작용
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147502].name
   limit: do 40 znaków
   EN: Enzymatic Tenderization
   PL: Enzymatic Tenderization
32. [[a1c10p1] Pasywka wroga [147502] — opis] 피격 시 다음 턴에 방어 레벨 감소 1 얻음, 공격 레벨 증가 1 얻음 (턴당 최대 3)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147502].desc
   limit: do 120 znaków
   EN: When hit, gain 1 Defense Level Down and 1 Offense Level Up next turn (3 per turn)
   PL: przy trafieniu zyskuje w następnej turze 1 Spadek Poziomu Obrony i 1 Wzrost Poziomu Ataku (maks. 3 na turę)
33. [[a1c10p1] Pasywka wroga [147502] — tekst klimatyczny] 질긴 지갑 가죽이 부드러워져 봤자다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147502].flavor
   limit: do 120 znaków
   EN: The tough leather wallet may be tenderized, but that won't change anything worth mentioning.
   PL: Twarda skóra portfela może i zmięknie, ale nie zmieni niczego godnego wzmianki.
34. [[a1c10p1] Pasywka wroga [147503] — nazwa] 배고파…
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147503].name
   limit: do 40 znaków
   EN: Hungry...
   PL: Hungry...
35. [[a1c10p1] Pasywka wroga [147503] — opis] 턴 종료 시 수셰프가 스킬 '앗! 제 식사시간인거예요'를 사용하지 못했다면, [SapsareeHungry] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147503].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [SapsareeHungry]
   znaczenie tagów: [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: Turn End: If Sous Chef failed to use the "Aah! I'm on lunch break, you hear?" Skill, gain 1 [SapsareeHungry]
   PL: Koniec tury: jeżeli Sous Chef nie użył Umiejętności „Aah! I'm on lunch break, you hear?”, zyskuje 1 [SapsareeHungry]
36. [[a1c10p1] Pasywka wroga [147503] — tekst klimatyczny] 식재료 용으로 만들지 않은 지갑이지만 식재료로 사육되고 있으니 배고플 수밖에.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=147503].flavor
   limit: do 130 znaków
   EN: It's a <b>wallet</b> being raised as livestock for consumption. And like cattle, it hungers to be fed.
   PL: To <b>portfel</b> hodowany jak inwentarz na konsumpcję. I jak bydło, głoduje, czekając na karmę.
37. [[a1c10p1] Pasywka wroga [148101] — nazwa] 패치워크
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148101].name
   limit: do 40 znaków
   EN: Patchwork
   PL: Patchwork
38. [[a1c10p1] Pasywka wroga [148101] — opis] 스테이지 시작 시, [UnresolvedFeelings] 30 얻음\n체력이 50% 이하면 특정 패턴에 사용하는 스킬이 강력한 스킬로 교체됨
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148101].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [UnresolvedFeelings]
   znaczenie tagów: [UnresolvedFeelings] = 다층 레이어 패치워크 / Layered Patchwork
   EN: Encounter Start: Gain 30 [UnresolvedFeelings]\nAt 50% or lower HP, convert a Skill used in a certain pattern into a powerful Skill
   PL: Na początku etapu: zyskuje 30 [UnresolvedFeelings]\nprzy HP 50% lub mniej Umiejętność używana w pewnym wzorcu zostaje zastąpiona potężną Umiejętnością
39. [[a1c10p1] Pasywka wroga [148101] — tekst klimatyczny] 수선하고 남아 버려질 원단들을 겹겹이 꿰어 쌓아올렸다. 자투리 원단 하나 하나만 보면 가치가 없다 하지만 그것들이 지닌 원단적 물성은 남아있기에 플로어 매니저가 긁어모으는 것이다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148101].flavor
   limit: do 300 znaków
   EN: Leftover fabric scraps, otherwise marked for disposal, are stitched together and stacked into layers upon layers. Each scrap is worthless on its own, but its fabric materiality lingers. That is why the Floor Manager gathers them up.
   PL: Łatki odpadowego materiału, nominalnie przeznaczone do wyrzucenia, zszywa się i układa warstwa po warstwie. Każdy skrawek sam w sobie nie ma wartości, ale materiałowa istota tkaniny w nim pozostaje. Dlatego Floor Manager je zgarnia.
40. [[a1c10p1] Pasywka wroga [148102] — nazwa] 경계심 체크
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148102].name
   limit: do 40 znaków
   EN: Cautionary Inspection
   PL: Cautionary Inspection
41. [[a1c10p1] Pasywka wroga [148102] — opis] 턴 시작 시, 다음 효과 발동\n<color=#ff6000><mark=#ff000040><b><u>- [Wariness]이 10인 수감자가 1명 이상 있으면, 공격 슬롯 하나가 추가되고 해당 슬롯에 스킬 '경고방송' 장착</u></b></mark></color>\n- [ReliefSense]를 보유하지 않은 모든 수감자에게 [Wariness] 1 부여\n- [HorribleTerror]을 보유한 인격 1명당, [HorribleEat] 1 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>수감자에게 스킬로 적중당하면,</u></b></mark></color> 해당 스킬 공격 종료 시 그 스킬로 적중당한 횟수만큼 대상 수감자에게 <color=#ff6000><mark=#ff000040><b><u>[Wariness] 부여</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148102].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Wariness], [ReliefSense], [HorribleTerror], [HorribleEat]
   znaczenie tagów: [Wariness] = 경계심 / Guarded Caution; [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening; [HorribleTerror] = 끔찍한 반복 재생 / Horribly Infinite Replay; [HorribleEat] = 반복 재생 반복 / Repeat on Repeat
   EN: Turn Start: Activate the effects below\n<color=#ff6000><mark=#ff000040><b><u>-If 1 or more Sinners have 10 [Wariness], gain an Attack Slot and equip the "Warning Announcement" Skill on the said Slot</u></b></mark></color>\n- Apply 1 [Wariness] on all Sinners that do not have [ReliefSense]\n- Gain 1 [HorribleEat] for every Identity that has [HorribleTerror]\n\n<color=#ff6000><mark=#ff000040><b><u>When hit by a Sinner's Skill:</u></b></mark></color>\nAt Attack End of the said Skill, <color=#ff6000><mark=#ff000040><b><u>apply [Wariness]</u></b></mark></color> on the said Sinner equal to the number of times this unit was hit by that Skill
   PL: Początek tury: uruchamia następujące efekty\n<color=#ff6000><mark=#ff000040><b><u>- jeżeli 1+ Grzeszników ma 10 [Wariness], zyskuje dodatkowy slot ataku i zakłada na tym slocie Umiejętność „Warning Announcement”</u></b></mark></color>\n- nakłada 1 [Wariness] na wszystkich Grzeszników nieposiadających [ReliefSense]\n- zyskuje 1 [HorribleEat] za każdą Tożsamość mającą [HorribleTerror]\n\n<color=#ff6000><mark=#ff000040><b><u>przy trafieniu Umiejętnością Grzesznika,</u></b></mark></color> po zakończeniu ataku tej Umiejętności <color=#ff6000><mark=#ff000040><b><u>nakłada [Wariness]</u></b></mark></color> na tego Grzesznika w liczbie równej liczbie trafień tą Umiejętnością
42. [[a1c10p1] Pasywka wroga [148102] — tekst klimatyczny] 목소리를 들으려면 귀가 아닌 마음부터 열어야 한다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148102].flavor
   limit: do 120 znaków
   EN: To hear the Voice, one must open the heart before the ears.
   PL: By usłyszeć Głos, trzeba najpierw otworzyć serce, a dopiero potem uszy.
43. [[a1c10p1] Pasywka wroga [148103] — nazwa] 감사
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148103].name
   limit: do 40 znaków
   EN: Gratitude
   PL: Gratitude
44. [[a1c10p1] Pasywka wroga [148103] — opis] 턴 시작 시 <color=#ff6000><mark=#ff000040><b><u>[ReliefSense]가 3인 수감자가 1명 이상 있으면, 공격 슬롯 하나가 추가되고 해당 슬롯에 스킬 '들어줘서… 고맙다…' 장착</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148103].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [ReliefSense]
   znaczenie tagów: [ReliefSense] = 경청에 대한 감사 / Gratitude for Listening
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>-If 1 or more Sinners have 3 [ReliefSense], gain an Attack Slot and equip the "Thank you... for listening..." Skill on the said Slot</u></b></mark></color>
   PL: Początek tury: <color=#ff6000><mark=#ff000040><b><u>- jeżeli 1+ Grzeszników ma 3 [ReliefSense], zyskuje dodatkowy slot ataku i zakłada na tym slocie Umiejętność „Thank you... for listening...”</u></b></mark></color>
45. [[a1c10p1] Pasywka wroga [148103] — tekst klimatyczny] 안내방송을 제대로 안 듣고 흘려버리는 고객들이 너무 많았어… 들어줘서 고마워…
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148103].flavor
   limit: do 140 znaków
   EN: Too many customers let the announcements go in one ear and out the other... Thank you for listening...
   PL: Too many customers let the announcements go in one ear and out the other... Thank you for listening...
46. [[a1c10p1] Pasywka wroga [148104] — nazwa] 패닉사살
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148104].name
   limit: do 40 znaków
   EN: Expunge the Panicked
   PL: Expunge the Panicked
47. [[a1c10p1] Pasywka wroga [148104] — opis] 패닉 상태인 대상에게 가하는 피해량 +200%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148104].desc
   limit: do 120 znaków
   EN: Deal +200% damage to targets that are in Panic
   PL: zadaje +200% obrażeń celom w Panice
48. [[a1c10p1] Pasywka wroga [148104] — tekst klimatyczny] 정신이 무너졌을 때 육체도 쉽게 무너뜨릴 수 있는 기술들이 있다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148104].flavor
   limit: do 140 znaków
   EN: Collapse the mind, then the body quickly follows. There exist methods that quicken this even further.
   PL: Gdy umysł się załamie, ciało wkrótce podąża za nim. Istnieją metody, które potrafią przyspieszyć ten proces.
49. [[a1c10p1] Pasywka wroga [149201] — nazwa] 르누아르 원단
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149201].name
   limit: do 40 znaków
   EN: Le Noir: Fabric
   PL: Le Noir: Fabric
50. [[a1c10p1] Pasywka wroga [149201] — opis] 스테이지 시작 시, [NoirBindArmor] 5 얻음\n\n턴 시작 시, 자신의 최대 체력의 ([NoirBindArmor] 수치/2)%만큼 보호막 얻음\n\n흐트러짐 상태가 되면 [NoirBindArmor]을 모두 잃고,\n턴 시작 시 흐트러짐 상태가 해제되면 [NoirBindArmor] 5 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149201].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [NoirBindArmor]
   znaczenie tagów: [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Encounter Start: Gain 5 [NoirBindArmor]\n\nTurn Start: Gain Shield equal to ([NoirBindArmor] Stack / 2)% of this unit's max HP\n\nWhen Staggered, lose all [NoirBindArmor]\nTurn Start: When this unit recovers from Stagger, gain 5 [NoirBindArmor]
   PL: Na początku etapu: zyskuje 5 [NoirBindArmor]\n\nPoczątek tury: zyskuje Tarczę równą (Stosy [NoirBindArmor] / 2)% Maks. HP tej jednostki\n\ngdy staje się Oszołamiona, traci wszystkie [NoirBindArmor]\nPoczątek tury: gdy ta jednostka dochodzi do siebie po Oszołamieniu, zyskuje 5 [NoirBindArmor]
51. [[a1c10p1] Pasywka wroga [149201] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149201].flavor
   limit: do 130 znaków
   EN: Le Noir's Worsted holds the body like armor, accentuating it beneath a firm, fixed silhouette.
   PL: Tkanina Le Noir trzyma ciało jak zbroję, eksponując je pod twardą, niezmienną sylwetką.
52. [[a1c10p1] Pasywka wroga [149202] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149202].name
   limit: do 40 znaków
   EN: Preservation
   PL: Preservation
53. [[a1c10p1] Pasywka wroga [149202] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n- 5 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 1 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149202].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Gain 1 [NoirBindArmor] for every 5 cumulative [ChargeNoir] Count this unit consumes in this Encounter\nGain 1 [ChargeNoir] for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter
   PL: zyskuje 1 [NoirBindArmor] za każde 5 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\nzyskuje 1 [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce
54. [[a1c10p1] Pasywka wroga [149202] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149202].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła zostaje sprężona, skupiona i utrwalona. Czasem potrzeba więcej siły, by powstrzymać zmianę, niż ją wywołać.
55. [[a1c10p1] Pasywka wroga [149203] — nazwa] 정지를 위한 변화
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149203].name
   limit: do 40 znaków
   EN: Change for Inertness
   PL: Change for Inertness
56. [[a1c10p1] Pasywka wroga [149203] — opis] 턴 시작 시 자신의 [ChargeNoir] 횟수가 10 이상이면 강력한 스킬을 사용\n\n스킬 사용 시 자신의 [ChargeNoir] 횟수가 15 이상이면,\n자신의 [ChargeNoir] 횟수를 3 소모하여 피해량 +20%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149203].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Turn Start: At 10+ [ChargeNoir] Count, use a powerful Skill\n\nOn Skill Use, at 15+ [ChargeNoir] Count, consume 3 [ChargeNoir] Count to deal +20% damage
   PL: Początek tury: przy 10+ Licznika [ChargeNoir] używa potężnej Umiejętności\n\nprzy użyciu Umiejętności, przy 15+ Licznika [ChargeNoir], zużywa 3 Licznika [ChargeNoir], aby zadać +20% obrażeń
57. [[a1c10p1] Pasywka wroga [149203] — tekst klimatyczny] 이 새로운 목소리는 내가 변하지 않을 수 있게 나를 바꿔줄 거라고 말해줘…
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149203].flavor
   limit: do 120 znaków
   EN: This new Voice tells me that it will help change me... so that I'll never change again.
   PL: Ten nowy Głos mówi mi, że przemieni mnie... tak, abym już nigdy nie musiał się zmieniać.
58. [[a1c10p1] Pasywka wroga [149204] — nazwa] 들려… 또 다른 신의 목소리가…
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149204].name
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [[a1c10p1] Pasywka wroga [149204] — opis] 스테이지 시작 시, [RisingMadnessNoir] 2 얻음\n- 턴 시작 시 이번 전투에서 체력이 처음으로 50% 이하가 되면,\n[RisingMadnessNoir]이 [RisingMadnessNoir2nd]로 변경됨\n\n합 패배 시, [ChargeNoir] 횟수 2 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149204].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [RisingMadnessNoir], [RisingMadnessNoir2nd], [ChargeNoir]
   znaczenie tagów: [RisingMadnessNoir] = 햇살 / Sunshine; [RisingMadnessNoir2nd] = 따가운 햇살 / Stinging Sunshine; [ChargeNoir] = 보존 / Preservation
   EN: Encounter Start: Gain 2 [RisingMadnessNoir]\n- Turn Start: When this unit's HP drops below 50% for the first time in this Encounter, convert [RisingMadnessNoir] into [RisingMadnessNoir2nd]\n\nOn Clash Lose, gain +2 [ChargeNoir] Count
   PL: Na początku etapu: zyskuje 2 [RisingMadnessNoir]\n- Początek tury: gdy HP tej jednostki po raz pierwszy w tej walce spadnie poniżej 50%, [RisingMadnessNoir] zamienia się w [RisingMadnessNoir2nd]\n\nPo przegranej w Starciu zyskuje 2 Licznika [ChargeNoir]
60. [[a1c10p1] Pasywka wroga [149204] — tekst klimatyczny] 따듯한 목소리를 들었지만 더 변하지 못하고 육신에 정신이 갇힌 채 분열로 광증에 빠졌다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149204].flavor
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [[a1c10p1] Pasywka wroga [148201] — nazwa] 르누아르 원단
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148201].name
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [[a1c10p1] Pasywka wroga [148201] — opis] 스테이지 시작 시, [NoirBindArmor] 3 얻음\n\n턴 시작 시, 자신의 최대 체력의 ([NoirBindArmor] 수치)%만큼 보호막 얻음 (흐트러진 경우 제외)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148201].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [NoirBindArmor]
   znaczenie tagów: [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Encounter Start: Gain 3 [NoirBindArmor]\n\nTurn Start: Gain Shield equal to ([NoirBindArmor] Stack)% of this unit's max HP (unless Staggered)
   PL: Na początku etapu: zyskuje 3 [NoirBindArmor]\n\nPoczątek tury: zyskuje Tarczę równą (Stosy [NoirBindArmor])% Maks. HP tej jednostki (chyba że jest Oszołamiona)
63. [[a1c10p1] Pasywka wroga [148201] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148201].flavor
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [[a1c10p1] Pasywka wroga [148202] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148202].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [[a1c10p1] Pasywka wroga [148202] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n- 3 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n\n자신의 [ChargeNoir] 위력이 3 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148202].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Gain 1 [NoirBindArmor] for every 3 cumulative [ChargeNoir] Count this unit consumes in this Encounter\nGain 1 [ChargeNoir] for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n\nAt 3+ [ChargeNoir] Potency, max [ChargeNoir] Count +5
   PL: zyskuje 1 [NoirBindArmor] za każde 3 łącznie zużyte Liczniki [ChargeNoir] tej jednostki w tej walce\nzyskuje 1 [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\n\nprzy 3+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5
66. [[a1c10p1] Pasywka wroga [148202] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148202].flavor
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [[a1c10p1] Pasywka wroga [148203] — nazwa] 응축의 발산
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148203].name
   limit: do 40 znaków
   EN: Unleash the Condensed
   PL: Unleash the Condensed
68. [[a1c10p1] Pasywka wroga [148203] — opis] 턴 시작 시 자신의 [ChargeNoir] 위력이 3, [ChargeNoir] 횟수가 10 이상이면 강력한 스킬을 사용
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148203].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Turn Start: At 3+ [ChargeNoir] Potency and 10+ [ChargeNoir] Count, use a powerful Skill
   PL: Początek tury: przy 3+ Siły [ChargeNoir] i 10+ Licznika [ChargeNoir] używa potężnej Umiejętności
69. [[a1c10p1] Pasywka wroga [148203] — tekst klimatyczny] 정지시키기 위해 한곳으로 모아진 힘은 언젠가 터져나온다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148203].flavor
   limit: do 120 znaków
   EN: Force condensed into one point to impose inertness will one day burst free.
   PL: Siła skupiona w jednym punkcie, by wymusić bezruch, pewnego dnia wybucha na zewnątrz.
70. [[a1c10p1] Pasywka wroga [148204] — nazwa] 보존 전환 역설
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148204].name
   limit: do 50 znaków
   EN: Conservation-Conversion Paradox
   PL: Conservation-Conversion Paradox
71. [[a1c10p1] Pasywka wroga [148204] — opis] 보호막을 보유한 상태면, 수감자에게 피격 시\n자신의 [ChargeNoir] 횟수 1 증가 (스킬별 1회, 턴당 3회)\n- 자신의 [ChargeNoir] 위력이 3/5 이상이면, 대신 자신의 [ChargeNoir] 횟수 2/3 증가\n\n턴 종료 시 보호막이 남아있다면,\n다음 턴에 [ChargeNoir] 위력만큼 [ChargeNoir] 횟수 1, [DefenseUp] 1 얻음 (각각 최대 3)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148204].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [DefenseUp]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: If this unit has Shield, gain +1 [ChargeNoir] Count when hit by a Sinner (once per Skill, 3 times per turn)\n- At 3+/5+ [ChargeNoir] Potency, gain +2/+3 [ChargeNoir] Count instead\n\nTurn End: If this unit has Shield,\nGain +1 [ChargeNoir] Count and 1 [DefenseUp] next turn for every [ChargeNoir] Potency on self (max 3 each)
   PL: jeżeli ta jednostka ma Tarczę, przy trafieniu przez Grzesznika zyskuje 1 Licznika [ChargeNoir] (1 raz na Umiejętność, 3 razy na turę)\n- przy 3+/5+ Siły [ChargeNoir] zamiast tego zyskuje 2/3 Licznika [ChargeNoir]\n\nKoniec tury: jeżeli ta jednostka ma Tarczę,\nw następnej turze zyskuje 1 Licznika [ChargeNoir] i 1 [DefenseUp] za każde 1 Siły [ChargeNoir] tej jednostki (maks. 3 każde)
72. [[a1c10p1] Pasywka wroga [148204] — tekst klimatyczny] 자신을 변화시키려는 외부의 힘을, 스스로를 보존하고자 하는 힘으로 전환한다.\n\n아무리 변화를 원치 않고 정지하려 해도 무언가를 반드시 변화시켜야만 하는 세계.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148204].flavor
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Convert an external force of change into a force of self-conservation. Yet this is a world where, however fiercely one rejects change or seeks inertness, something must change.
   PL: Przemienia zewnętrzną siłę zmiany w siłę własnego zachowania.\n\nA przecież to świat, w którym — choćby jak najostrzej odrzucano zmianę czy dążono do bezruchu — coś i tak musi się zmienić.
73. [[a1c10p1] Pasywka wroga [148301] — nazwa] 르누아르 개버딘 원단
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148301].name
   limit: do 40 znaków
   EN: Le Noir: Gabardine Fabric
   PL: Le Noir: Gabardine Fabric
74. [[a1c10p1] Pasywka wroga [148301] — opis] 스테이지 시작 시, [NoirSuit] 30 얻음\n\n턴 시작 시,\n- 자신의 최대 체력의 ([NoirSuit]/5)%만큼 보호막 얻음 (흐트러진 경우 제외)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148301].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSuit]
   znaczenie tagów: [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat
   EN: Encounter Start: Gain 30 [NoirSuit]\n\nTurn Start: Gain Shield equal to ([NoirSuit] / 5)% of this unit's max HP (unless Staggered)
   PL: Na początku etapu: zyskuje 30 [NoirSuit]\n\nPoczątek tury: zyskuje Tarczę równą (Stosy [NoirSuit] / 5)% Maks. HP tej jednostki (chyba że jest Oszołamiona)
75. [[a1c10p1] Pasywka wroga [148301] — tekst klimatyczny] 포멀하면서도 탄탄함을 지향하는 르누아르가 선보이는 플래그쉽 원단.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148301].flavor
   limit: do 120 znaków
   EN: The Noirs' flagship gabardine, tailored toward formality without sacrificing firmness.
   PL: Flagowy gabardyn Le Noir — szyty z myślą o formalności, niekosztem twardości.
76. [[a1c10p1] Pasywka wroga [148302] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148302].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [[a1c10p1] Pasywka wroga [148302] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n\n자신의 [ChargeNoir] 위력이 3 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148302].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n\nAt 3+ [ChargeNoir] Potency, max [ChargeNoir] Count +5
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\n\nprzy 3+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5
78. [[a1c10p1] Pasywka wroga [148302] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148302].flavor
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [[a1c10p1] Pasywka wroga [148303] — nazwa] 되먹임
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148303].name
   limit: do 40 znaków
   EN: Feedback
   PL: Feedback
80. [[a1c10p1] Pasywka wroga [148303] — opis] 턴 시작 시 [Realisation]가 있으면, ‘원 킥’이 ‘원 킥 - 쿠튀르 뮐티플’로 적용됨\n\n[VibrationExplosion] 시, [VibrationExplosion]의 흐트러짐 피해량 +20%\n- 자신의 [ChargeNoir] 횟수가 12 이상이면, 대신 [VibrationExplosion] 시 자신의 [ChargeNoir] 횟수 1을\n소모하여 [VibrationExplosion]의 흐트러짐 피해량 +40% (대상별로 적용)\n\n[VibrationExplosion] 시 타겟에게 흐트러짐 구간이 없으면,\n자신의 [DefenseUp] 수치만큼 고정 피해를 입힘 (최대 20)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148303].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n, [Realisation], [VibrationExplosion], [ChargeNoir], [DefenseUp]
   znaczenie tagów: [Realisation] = 아르뮈르 에비이예 / Armure Éveillée; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [ChargeNoir] = 보존 / Preservation; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: If this unit has [Realisation], activate "Single Kick" as "Single Kick - Couture Multiple" instead\n\nWhen triggering [VibrationExplosion], apply +20% to Stagger Threshold raised by [VibrationExplosion]\n- At 12+ [ChargeNoir] Count, when triggering [VibrationExplosion], consume 1 [ChargeNoir] Count on self and instead apply +40% to Stagger Threshold raised by [VibrationExplosion] (per-target)\n\nWhen triggering [VibrationExplosion], if target does not have a Stagger threshold, deal fixed damage equal to [DefenseUp] Stack on self (max 20)
   PL: Początek tury: jeżeli ta jednostka ma [Realisation], zamiast „Single Kick” stosuje „Single Kick - Couture Multiple”\n\nprzy wywołaniu [VibrationExplosion] podniesienie Progu Oszołomienia przez [VibrationExplosion] zwiększa się o 20%\n- przy 12+ Licznika [ChargeNoir] wywołując [VibrationExplosion] zużywa 1 Licznika [ChargeNoir] tej jednostki, a podniesienie Progu Oszołomienia przez [VibrationExplosion] zwiększa się zamiast tego o 40% (na każdego celu)\n\njeżeli przy wywołaniu [VibrationExplosion] cel nie ma Progu Oszołomienia, zadaje obrażenia stałe równe Stosom [DefenseUp] tej jednostki (maks. 20)
81. [[a1c10p1] Pasywka wroga [148303] — tekst klimatyczny] 르누아르는 상대에게 강한 진동을 주어 흔들리게 함으로써 가치를 붕괴시킬 수 있다고 믿는다.\n\n대상이 격렬하게 진동할수록 매 순간 변화를 겪는 것이라 생각하기 때문이다.\n\n이러한 믿음 위에서 르누아르의 전투 기술들은 만들어진다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148303].flavor
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Noirs believe they can collapse their opponents' worth by subjecting them to violent tremors—the more violently the target vibrates, the more changes it must undergo from moment to moment.\n\nThe combat techniques of the Noirs were built upon that conviction.
   PL: Le Noir wierzy, że potrafi zdruzotać wartość przeciwnika, poddając go gwałtownym wibracjom — im mocniej cel drga, tym więcej zmian musi przechodzić z chwili na chwilę.\n\nTechniki walki Le Noir zbudowano na tym przekonaniu.
82. [[a1c10p1] Pasywka wroga [148304] — nazwa] 보존 전환 역설의 역설
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148304].name
   limit: do 70 znaków
   EN: Paradox of the Conservation-Conversion Paradox
   PL: Paradox of the Conservation-Conversion Paradox
83. [[a1c10p1] Pasywka wroga [148304] — opis] 보호막을 보유한 상태면, 수감자에게 피격 시\n- 대상 수감자에게 [Vibration] 1 부여 (스킬별 1회)\n- 자신의 [ChargeNoir] 횟수 1 증가 (스킬별 1회, 턴당 3회)\n· 자신의 [ChargeNoir] 위력이 3/5 이상이면, 대신 자신의 [ChargeNoir] 횟수 2/3 증가\n\n턴 종료 시 보호막이 남아있다면,\n다음 턴에 [ChargeNoir] 위력 1당, [ChargeNoir] 횟수 1, [DefenseUp] 2 얻음 (각각 최대 3, 최대 6)
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148304].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [ChargeNoir], [DefenseUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: If this unit has Shield, when hit by a Sinner,\n- Inflict 1 [Vibration] on the Sinner (once per Skill)\n- Gain +1 [ChargeNoir] Count (once per Skill, 3 times per turn)\n  · At 3+/5+ [ChargeNoir] Potency, gain +2/+3 [ChargeNoir] Count instead\n\nTurn End: If this unit has Shield,\nGain +1 [ChargeNoir] Count and 2 [DefenseUp] next turn for every [ChargeNoir] Potency on self (max 3, max 6 respectively)
   PL: jeżeli ta jednostka ma Tarczę, przy trafieniu przez Grzesznika:\n- nakłada 1 [Vibration] na Grzesznika (1 raz na Umiejętność)\n- zyskuje 1 Licznika [ChargeNoir] (1 raz na Umiejętność, 3 razy na turę)\n  · przy 3+/5+ Siły [ChargeNoir] zamiast tego zyskuje 2/3 Licznika [ChargeNoir]\n\nKoniec tury: jeżeli ta jednostka ma Tarczę,\nw następnej turze zyskuje 1 Licznika [ChargeNoir] i 2 [DefenseUp] za każde 1 Siły [ChargeNoir] tej jednostki (maks. 3, maks. 6)
84. [[a1c10p1] Pasywka wroga [148304] — tekst klimatyczny] 변하지 않으려 애쓸수록, 존재는 변화하는 상태로 향한다.\n\n존재하는 것은 항상 어딘가로 향하고 있고, 어딘가로 향하는 이상 변화는 따라올 수밖에 없다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148304].flavor
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The harder an existence struggles to remain the same, the more surely it changes. To exist is always to be going somewhere, and wherever there is motion, change follows.
   PL: Im bardziej istnienie usiłuje pozostać takie samo, tym pewniej ulega zmianie.\n\nIstnieć to zawsze zmierzać dokądś, a tam, gdzie jest ruch, zmiana podąża za tym.
85. [[a1c10p1] Pasywka wroga [149601] — nazwa] 봉제시작
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149601].name
   limit: do 40 znaków
   EN: The Sewing Commences
   PL: The Sewing Commences
86. [[a1c10p1] Pasywka wroga [149601] — opis] 턴 시작시, 무작위 적 2명에게 [NiddleExpected] 부여
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NiddleExpected]
   znaczenie tagów: [NiddleExpected] = 혀에 꽂힌 바늘 / Tongue-pinning Needle
   EN: Turn Start: Inflict [NiddleExpected] on 2 random enemies
   PL: Początek tury: nakłada [NiddleExpected] na 2 losowych wrogów
87. [[a1c10p1] Pasywka wroga [149602] — nazwa] 핸드메이드
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149602].name
   limit: do 40 znaków
   EN: Handmade
   PL: Handmade
88. [[a1c10p1] Pasywka wroga [149602] — opis] 전장의 바늘이[TabExplain] 1개당 스킬 최종 위력 +1
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Skill Final Power +1 for every Needlekin[TabExplain] on the field
   PL: Moc Końcowa Umiejętności +1 za każdego 1 Needlekin[TabExplain] na polu
89. [[a1c10p1] Pasywka wroga [149602] — tekst klimatyczny] 손 바느질은 숙련된 기능공들의 수가 생명이다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149602].flavor
   limit: do 150 znaków
   EN: No hand sewing survives on one pair of hands alone. A host of practiced artisans are needed to breathe life into it.
   PL: Ręczne szycie nie daje rady na jednej parze rąk. Żeby tchnąć w nie życie, potrzeba rzeszy wprawionych rzemieślników.
90. [[a1c10p1] Pasywka wroga [149603] — nazwa] 귀를 막아도 보이는 클레임
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149603].name
   limit: do 70 znaków
   EN: Unending, Unavoidable Stream of Customer Complaints
   PL: Unending, Unavoidable Stream of Customer Complaints
91. [[a1c10p1] Pasywka wroga [149603] — opis] 3배수 턴마다 고치의 울음소리가 들림\n2페이즈 진입시 고치의 울음소리가 매 턴 지속됨\n\n고치의 울음소리가 들리는 턴에는 행동불가상태에 면역\n\n흐트러짐 구간을 지나면 다음 턴에 [Vulnerable] 2 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149603].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: "Cry of the Cocoon" is heard every "multiple of 3" turns\nUpon entering Phase 2, "Cry of the Cocoon" continues to be heard every turn\n\nThis unit cannot be immobilized in the turn "Cry of the Cocoon" is heard\n\nIf this unit's HP is brought past its Stagger Threshold, gain 2 [Vulnerable] next turn
   PL: „Cry of the Cocoon” słychać w turach będących wielokrotnością 3\nod wejścia do Fazy 2 „Cry of the Cocoon” słychać w każdej turze\n\nw turze, w której słychać „Cry of the Cocoon”, ta jednostka jest odporna na stan unieruchomienia\n\njeżeli HP tej jednostki spadnie poniżej jej Progu Oszołomienia, zyskuje w następnej turze 2 [Vulnerable]
92. [[a1c10p1] Pasywka wroga [149603] — tekst klimatyczny] 고치에서 소리가 들려온다.\n‘80수 2합 아래는 원단 취급 안함.’ ‘단추구멍 왜 가로 아님?’\n‘구직기에 천축인가요?’ ‘셀비지 색 왜 빨간색 아니에요?’\n‘이거 방축가공처리 안됐네.’ ‘Super 150이하면 싸구려 원단이죠’\n‘Super 넘버가 그냥 실 굵기라고요? 직경이랑 번수랑 다른데 그것도 모르시네.’\n‘유니온스페셜로 당연히 처리 밑단 처리해주죠?’ ‘이거 리지드에요? 아, 셀비지인가?’\n‘자세히보니까 땀수가 너무 균일하네. 기계썼죠?’ ‘손 바느질 아니면 비스포크 아님.’\n‘아 이거 홀 밀라네제 아니네.’ ‘번수가 200은 넘어야 셔츠 원단이죠.’\n‘아 겉에 박음선 보이네.’ ‘박음선 두 줄 보이네. 탈락.’\n‘시접처리 왜 이래.’ ‘3플라이는 넘겨줘야지’
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149603].flavor
   limit: do 1120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Voices seep from the cocoon.\n\n"Anything under 80-count two-ply? Not even fabric!"\n"Why aren't the buttonholes horizontal?"\n"Jersey knit on machine? Really?"\n"Why isn't the selvage red?"\n"This hasn't even been shrink-proofed."\n"Anything below Super 150 is cheap cloth, obviously."\n"You think the Super scale is just yarn thickness? Diameter and yarn count aren't even the same thing. Don't you know that?"\n"You're finishing the hem with a Union Special, right? Of course you are!"\n"Is this Rigid? ... Oh. Selvage?"\n"Wait... the stitch-per-inch count is way too even. You used a machine, didn't you?"\n"It's not bespoke if it's not hand-stitched."\n"... That's not even a Milanese buttonhole."\n"Shirting needs to be over 200-count."\n"Ugh, I can see the stitching on the outside."\n"There, I can see two rows of stitching there. Rejected."\n"What's with this seam finish?"\n"Three-ply, minimum."
   PL: Z kokonu sączą się Głosy.\n\n„Poniżej przędzy 80/2? Nawet nie tkanina!”\n„Dlaczego dziurki na guziki nie są poziome?”\n„Dżersej na maszynie? Serio?”\n„Dlaczego selwedżyn nie jest czerwony?”\n„To nawet nie przeszło obróbki antyosadzającej.”\n„Cokolwiek poniżej Super 150 to oczywista tandeta.”\n„Myślisz, że skala Super to po prostu grubość przędzy? Średnica i numer to dwie różne rzeczy. Nie wiesz nawet tego?”\n„Rąbek wykańczasz Union Specialem, prawda? No pewnie, że tak!”\n„To jest Rigid? ... A. Selwedżyn?”\n„Zaraz... liczba ściegów na cal jest zbyt równa. Użyłeś maszyny, co?”\n„Bez ręcznego szycia to nie bespoke.”\n„... To nawet nie jest dziurka mediolańska.”\n„Tkanina na koszulę musi mieć ponad 200 numeru.”\n„Ależ widać ścieg na zewnątrz.”\n„No proszę, tam widać dwa rzędy ściegu. Odrzucone.”\n„Co to za wykończenie szwu?”\n„Trzy nitki, minimum.”
93. [[a1c10p1] Pasywka wroga [148401] — nazwa] 미숙한 붉은 신
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148401].name
   limit: do 40 znaków
   EN: The Preterm Crimson God
   PL: The Preterm Crimson God
94. [[a1c10p1] Pasywka wroga [148401] — opis] 턴 종료 시 [ChargeRouge] 횟수가 감소하지 않음\n<color=#ff6000><mark=#ff000040><b><u>합 진행 시 대상의 [Laceration]이 발동</u></b></mark></color>할 때마다 자신의 [ChargeRouge] 횟수 1 증가\n대상 처치 시 대상의 ([Laceration] 위력 + [Laceration] 횟수)만큼 자신의 [ChargeRouge] 횟수 증가\n턴 시작 시 자신의 [ChargeRouge] 횟수 1당, 정신력 3 회복
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148401].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ChargeRouge], [Laceration]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: Turn End: Does not lose [ChargeRouge] Count\n<color=#ff6000><mark=#ff000040><b><u>In a Clash, gain +1 [ChargeRouge] Count every time target's [Laceration] is activated</u></b></mark></color>\nOn Kill, gain [ChargeRouge] Count equal to ([Laceration] Potency + [Laceration] Count) on target\nTurn Start: Heal 3 SP for every [ChargeRouge] Count on self
   PL: Koniec tury: nie traci Licznika [ChargeRouge]\n<color=#ff6000><mark=#ff000040><b><u>podczas Starcia zyskuje 1 Licznika [ChargeRouge] za każdym razem, gdy zostanie aktywowane [Laceration] celu</u></b></mark></color>\nprzy zabiciu celu zyskuje Liczniki [ChargeRouge] równe (Siła [Laceration] + Licznik [Laceration]) celu\nPoczątek tury: przywraca 3 SP za każde 1 Licznika [ChargeRouge] tej jednostki
95. [[a1c10p1] Pasywka wroga [148401] — tekst klimatyczny] 갈망에 의해 태어나져버린 신. 탄생조차 온전하지 못했다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148401].flavor
   limit: do 130 znaków
   EN: A god conceived by yearning, brought into the world before its time. Even its birth was incomplete.
   PL: Bóg poczęty z tęsknoty, przyniesiony na świat przed czasem. Nawet jego narodziny były niedokończone.
96. [[a1c10p1] Pasywka wroga [148402] — nazwa] 장밋빛으로 맥동하는 근육
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148402].name
   limit: do 50 znaków
   EN: Roseate Pulsation of Musculature
   PL: Roseate Pulsation of Musculature
97. [[a1c10p1] Pasywka wroga [148402] — opis] 턴 시작 시 자신에게 [Gourmandise]가 없으며, <color=#ff6000><mark=#ff000040><b><u>자신의 [ChargeRouge] 횟수가 15 이상이면, [ChargeRouge] 횟수를 모두 소모하고 [Gourmandise] 얻음</u></b></mark></color>\n\n[Gourmandise]가 있는 상태에서 다음 효과 얻음\n- 스킬 사용 시 자신의 [Laceration] 횟수 3 증가\n- 스킬 적중 시 [Laceration] 1 얻음\n- 부위 피격 시 [BuffetSick] 1 얻음\n- 합 패배 시 [BuffetSick] 3 얻음\n- 대상 처치 시 대상의 [BloodyMucus]이 3 이상이면, 다음 턴에 '붉은 신의 뜯긴 살점' 생성\n- 전투 종료 시 [BloodyMucus]을 보유한 적 1명당 정신력 3 회복\n\n턴 종료 시 [Gourmandise] 효과가 소멸할 때, <color=#ff6000><mark=#ff000040><b><u>자신이 보유한 [BuffetSick]의 총합이 30 이상이면</u></b></mark></color>, 다음 턴에 패턴이 약화되며 전장의 '붉은 신의 뜯긴 살점'이 흐트러짐 상태가 됨\n\n※[BloodyMucus]은 <color=#ff6000><mark=#ff000040><b><u>E.G.O 스킬, 수비 스킬 사용</u></b></mark></color>으로 수치를 감소시킬 수 있음\n※'붉은 신의 뜯긴 살점'은 사망한 대상의 [BloodyMucus]만큼 [DeterioratingBody]을 얻음\n※[DeterioratingBody]을 보유한 '붉은 신의 뜯긴 살점'은 사망하지 않음\n※'붉은 신의 뜯긴 살점'은 전장에 최대 3마리까지 생성됨
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148402].desc
   limit: do 1350 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Gourmandise], [ChargeRouge], [Laceration], [BuffetSick], [BloodyMucus], [DeterioratingBody]
   znaczenie tagów: [Gourmandise] = 폭주 / Uncontrollable Rampage; [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed; [BuffetSick] = 고통 주머니 / Sac of Suffering; [BloodyMucus] = 세례[적] / Baptism [Crimson]; [DeterioratingBody] = 생의 본능 / Instinctive Cling to Life
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>At 15+ [ChargeRouge] Count, if this unit does not have [Gourmandise], consume all [ChargeRouge] Count on self and gain [Gourmandise]</u></b></mark></color>\n\nGain the following effects while this unit has [Gourmandise]:\n- On Skill Use, gain +3 [Laceration] Count\n- On Hit, gain 1 [Laceration]\n- When hit on one of its Parts, gain 1 [BuffetSick]\n- On Clash Lose, gain 3 [BuffetSick]\n- On Kill, if target has 3+ [BloodyMucus], generate "Ripped Flesh of the Crimson God" next turn\n- Combat End: Heal 3 SP for every enemy that has [BloodyMucus]\n\nTurn End: <color=#ff6000><mark=#ff000040><b><u>If this unit has 30+ [BuffetSick]</u></b></mark></color> when [Gourmandise] expires, next turn, weaken this unit's patterns and Stagger "Ripped Flesh of the Crimson God" units on the field\n\n※ [BloodyMucus] Stack can be reduced by the following means: <color=#ff6000><mark=#ff000040><b>E.G.O Skill Use and Defense Skill Use</u></b></mark></color>\n※ "Ripped Flesh of the Crimson God" gains [DeterioratingBody] equal to [BloodyMucus] on the defeated target\n※ "Ripped Flesh of the Crimson God" that has [DeterioratingBody] cannot be defeated\n※ Up to 3 "Ripped Flesh of the Crimson God" can be generated on the field
   PL: Początek tury: <color=#ff6000><mark=#ff000040><b><u>przy 15+ Licznika [ChargeRouge], jeżeli ta jednostka nie ma [Gourmandise], zużywa wszystkie Liczniki [ChargeRouge] tej jednostki i zyskuje [Gourmandise]</u></b></mark></color>\n\ndopóki ta jednostka ma [Gourmandise], zyskuje następujące efekty:\n- przy użyciu Umiejętności zyskuje 3 Licznika [Laceration]\n- przy trafieniu zyskuje 1 [Laceration]\n- przy trafieniu w którąś ze swoich Części zyskuje 1 [BuffetSick]\n- Po przegranej w Starciu zyskuje 3 [BuffetSick]\n- przy zabiciu celu mającego 3+ [BloodyMucus] generuje w następnej turze „Ripped Flesh of the Crimson God”\n- koniec walki: przywraca 3 SP za każdego wroga mającego [BloodyMucus]\n\nKoniec tury: <color=#ff6000><mark=#ff000040><b><u>jeżeli suma [BuffetSick] tej jednostki wynosi 30+</u></b></mark></color> w momencie wygaśnięcia [Gourmandise], w następnej turze osłabia swoje wzorce i Oszołamia jednostki „Ripped Flesh of the Crimson God” na polu\n\n※ Stosy [BloodyMucus] można zmniejszyć przez: <color=#ff6000><mark=#ff000040><b><u>użycie Umiejętności E.G.O i Umiejętności obrony</u></b></mark></color>\n※ „Ripped Flesh of the Crimson God” zyskuje [DeterioratingBody] równe [BloodyMucus] pokonanego celu\n※ „Ripped Flesh of the Crimson God” mający [DeterioratingBody] nie zostaje pokonany\n※ na polu może powstać maks. 3 „Ripped Flesh of the Crimson God”
98. [[a1c10p1] Pasywka wroga [148402] — tekst klimatyczny] 팔과 다리가 미친 듯이 허우적댄다. 원래 자신의 몸에 달려 있는 게 아니었던 것처럼.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148402].flavor
   limit: do 120 znaków
   EN: Its limbs thrash and twitch frantically as though they were never its own.
   PL: Kończyny szamocą się i drgają w frenetycznym rytmie, jakby nigdy nie były jego własne.
99. [[a1c10p1] Pasywka wroga [148403] — nazwa] 격차
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148403].name
   limit: do 40 znaków
   EN: Disparity
   PL: Disparity
100. [[a1c10p1] Pasywka wroga [148403] — opis] 자신보다 느린 대상에게 가하는 피해량 +50%
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148403].desc
   limit: do 120 znaków
   EN: Deal +50% damage against slower targets
   PL: zadaje +50% obrażeń celom wolniejszym niż ta jednostka
101. [[a1c10p1] Pasywka wroga [148403] — tekst klimatyczny] 보이는 모든 것들은 제각각의 속도로 움직인다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148403].flavor
   limit: do 120 znaków
   EN: Everything in sight skitters around at disparate speeds.
   PL: Wszystko, co widać, pędzi chaotycznie w różnych tempach.
102. [[a1c10p1] Pasywka wroga [148404] — nazwa] 생존본능
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148404].name
   limit: do 40 znaków
   EN: Survival Instinct
   PL: Survival Instinct
103. [[a1c10p1] Pasywka wroga [148404] — opis] 턴 시작 시 [SavePlacenta] 1 얻으며, 생명줄 부위에 [Protection] 5 부여\n[Gourmandise]를 갖고 있거나 흐트러짐 상태이면, 해당 패시브가 발동하지 않음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148404].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [SavePlacenta], [Protection], [Gourmandise]
   znaczenie tagów: [SavePlacenta] = 자기 보호 / Self-preservation; [Protection] = 보호 / Protection; [Gourmandise] = 폭주 / Uncontrollable Rampage
   EN: Turn Start: Gain 1 [SavePlacenta] and apply 5 [Protection] on the Lifecord Part\nIf this unit has [Gourmandise], or if it is Staggered, this Passive does not activate
   PL: Początek tury: zyskuje 1 [SavePlacenta] i nakłada 5 [Protection] na Część Lifecord\njeżeli ta jednostka ma [Gourmandise] albo jest Oszołamiona, ta pasywka się nie uruchamia
104. [[a1c10p1] Pasywka wroga [148404] — tekst klimatyczny] 신체는 의식과 무관하게 몸을 지키기 위해 발버둥친다. 어디까지가 자신의 몸인지도 모르면서.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148404].flavor
   limit: do 190 znaków
   EN: Consciousness has no hand in the body's struggles to survive and protect itself, which it does without even knowing where it begins and ends.
   PL: Świadomość nie ma nic do rzeczy w zmaganiach ciała o przetrwanie i samoobronę — ciało walczy, nie wiedząc nawet, gdzie się zaczyna i kończy.
105. [[a1c10p1] Pasywka wroga [148405] — nazwa] 끊어진 생명줄
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148405].name
   limit: do 40 znaków
   EN: Severed Lifecord
   PL: Severed Lifecord
106. [[a1c10p1] Pasywka wroga [148405] — opis] 생명줄 부위가 파괴된 상태이면, 턴 종료 시 다음 턴에 몸통 부위가 [Vulnerable] 3 얻음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148405].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn End: If the Lifecord Part is broken, the Body Part gains 3 [Vulnerable] next turn
   PL: Koniec tury: jeżeli Część Lifecord jest zniszczona, Część Korpus zyskuje w następnej turze 3 [Vulnerable]
107. [[a1c10p1] Pasywka wroga [148405] — tekst klimatyczny] 몸에 붙어있는 것들, 이 덜렁거리는 것들, 어디까지가 나인지 헤아리기 어려워한다.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148405].flavor
   limit: do 150 znaków
   EN: What are these dangling, floppy things attached to my body? Are these a part of "me"? It's so difficult to tell.
   PL: What are these dangling, floppy things attached to my body? Are these a part of "me"? It's so difficult to tell.
108. [[a1c10p1] Pasywka wroga [148406] — nazwa] 폭력적인 탄생의 폭주
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148406].name
   limit: do 60 znaków
   EN: Rampage of a Violent, Traumatic Birth
   PL: Rampage of a Violent, Traumatic Birth
109. [[a1c10p1] Pasywka wroga [148406] — opis] 생명줄 부위가 파괴되지 않은 상태에서, 턴 종료 시 본체 체력이 50% 미만이면 [Gourmandise]를 얻음\n이후 생명줄 부위가 파괴되기 전까지 [Gourmandise] 수치가 감소하지 않음
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148406].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Gourmandise]
   znaczenie tagów: [Gourmandise] = 폭주 / Uncontrollable Rampage
   EN: Turn End: If the Lifecord Part isn't broken, and at lower than 50% Core HP, gain [Gourmandise]\nThen, does not lose [Gourmandise] Stack until the Lifecord Part is broken
   PL: Koniec tury: jeżeli Część Lifecord nie jest zniszczona, a HP rdzenia tej jednostki jest niższe niż 50%, zyskuje [Gourmandise]\nnastępnie nie traci Stosów [Gourmandise], dopóki Część Lifecord nie zostanie zniszczona
110. [[a1c10p1] Pasywka wroga [148406] — tekst klimatyczny] 몸은 따듯했던 곳에서 차가운 곳으로. 의식은 서늘했던 곳에서 뜨거운 곳으로. 그렇게 모든 것은 강제로.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=148406].flavor
   limit: do 150 znaków
   EN: The body is torn from warmth into cold; the mind, from cool calmness to fiery chaos. None of it is voluntary.
   PL: Ciało rwie się z ciepła w zimno; umysł — z chłodnego spokoju w ognisty chaos. I nic z tego nie jest dobrowolne.
111. [[a1c10p1] Pasywka wroga [149701] — nazwa] 지성 없는 맥동
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149701].name
   limit: do 40 znaków
   EN: Mindless Pulsation
   PL: Mindless Pulsation
112. [[a1c10p1] Pasywka wroga [149701] — opis] - 생성 시 사망했던 대상의 [BloodyMucus] 수치만큼 [DeterioratingBody] 얻음\n\n[DeterioratingBody] 소멸 시 사망
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149701].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [BloodyMucus], [DeterioratingBody]
   znaczenie tagów: [BloodyMucus] = 세례[적] / Baptism [Crimson]; [DeterioratingBody] = 생의 본능 / Instinctive Cling to Life
   EN: - When generated, gain [DeterioratingBody] equal to [BloodyMucus] Stack on target that was defeated to generate this unit\n\nDefeated when [DeterioratingBody] expires
   PL: - przy powstaniu zyskuje [DeterioratingBody] równe Stosom [BloodyMucus] celu pokonanego, aby tę jednostkę wygenerować\n\njednostka zostaje pokonana, gdy [DeterioratingBody] wygaśnie
113. [[a1c10p1] Pasywka wroga [149701] — tekst klimatyczny] 이것은 살아있다. 하지만 뇌는 없다. 의식은 뇌가 아닌 맥동하는 근육에서도 나올 수 있던가.
   źródło: Passives_Abnormality-a1c10p1.json :: dataList[id=149701].flavor
   limit: do 120 znaków
   EN: It lives, yet it has no brain. Can the mind arise from pulsing muscle instead?
   PL: To żyje, ale nie ma mózgu. Czy umysł może rodzić się z pulsujących mięśni?

## [a1c10p1] Pasywka wroga: Passives_Enemy-a1c10p1
- plik gry: `Passives_Enemy-a1c10p1.json`

114. [[a1c10p1] Pasywka wroga [9105901] — nazwa] 유리병은 조심해서 다뤄야하는데…!
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105901].name
   limit: do 70 znaków
   EN: Glass bottles need to be handled carefully...!
   PL: Glass bottles need to be handled carefully...!
115. [[a1c10p1] Pasywka wroga [9105901] — opis] 스킬에 피격 시 [Laceration] 3 얻음 (스킬당 1회)\n\n위 효과 발동 시 다음 턴에 [ResultEnhancement] 1 얻음 (최대 2)
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105901].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [ResultEnhancement]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [ResultEnhancement] = 위력 증가 / Power Up
   EN: When hit by a Skill, gain 3 [Laceration] (once per Skill)\n\nWhen the above effect activates, gain 1 [ResultEnhancement] next turn (max 2)
   PL: przy trafieniu Umiejętnością zyskuje 3 [Laceration] (1 raz na Umiejętność)\n\nprzy uruchomieniu powyższego efektu zyskuje w następnej turze 1 [ResultEnhancement] (maks. 2)
116. [[a1c10p1] Pasywka wroga [9105902] — nazwa] 내 병은 안전해
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105902].name
   limit: do 40 znaków
   EN: Phew, my bottle's safe
   PL: Phew, my bottle's safe
117. [[a1c10p1] Pasywka wroga [9105902] — opis] 자신에게 [Laceration]이 없는 상태로 턴 종료 시, 정신력 5 회복
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Turn End: If this unit does not have [Laceration], heal 5 SP
   PL: Koniec tury: jeżeli ta jednostka nie ma [Laceration], przywraca 5 SP
118. [[a1c10p1] Pasywka wroga [9105903] — nazwa] 병을 채워야 해
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105903].name
   limit: do 40 znaków
   EN: I must fill the bottle
   PL: I must fill the bottle
119. [[a1c10p1] Pasywka wroga [9105903] — opis] 자신의 체력이 최대가 아닐 때, 자신의 스킬이 적중한 대상이 [Laceration]을 보유 중이면, 최대 체력의 2% 회복 (턴당 2회, 소수점 내림)
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9105903].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If the target hit by this unit's Skill has [Laceration], and if this unit is not at max HP, heal 2% HP (2 times pre turn; rounded down)
   PL: jeżeli cel trafiony Umiejętnością tej jednostki ma [Laceration], a ta jednostka nie ma pełnego HP, przywraca 2% HP (2 razy na turę; zaokrąglone w dół)
120. [[a1c10p1] Pasywka wroga [9106601] — nazwa] 르누아르 원단
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106601].name
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [[a1c10p1] Pasywka wroga [9106601] — opis] 전투에 첫 등장 시, [NoirBindArmor] 5 얻음\n\n턴 시작 시, 10 + 자신의 최대 체력의 ([NoirBindArmor] 수치)%만큼 보호막 얻음
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106601].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [NoirBindArmor]
   znaczenie tagów: [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Upon entering the Encounter for the first time, gain 5 [NoirBindArmor]\n\nTurn Start: Gain Shield equal to (10 + [NoirBindArmor] Stack)% of this unit's max HP
   PL: Przy pierwszym pojawieniu się w walce zyskuje 5 [NoirBindArmor]\n\nPoczątek tury: zyskuje Tarczę równą (10 + Stosy [NoirBindArmor])% Maks. HP tej jednostki
122. [[a1c10p1] Pasywka wroga [9106601] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106601].flavor
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [[a1c10p1] Pasywka wroga [9106602] — nazwa] 보존
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106602].name
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [[a1c10p1] Pasywka wroga [9106602] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를\n- 5 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 1 얻음
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106602].desc
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [[a1c10p1] Pasywka wroga [9106602] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106602].flavor
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [[a1c10p1] Pasywka wroga [9106603] — nazwa] 정지를 위한 변화
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106603].name
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [[a1c10p1] Pasywka wroga [9106603] — opis] 턴 시작 시 자신의 [ChargeNoir] 횟수가 10 이상이면 강력한 스킬을 사용\n\n스킬 사용 시 자신의 [ChargeNoir] 횟수가 15 이상이면,\n자신의 [ChargeNoir] 횟수를 3 소모하여 피해량 +20%
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106603].desc
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [[a1c10p1] Pasywka wroga [9106603] — tekst klimatyczny] 이 새로운 목소리는 내가 변하지 않을 수 있게 나를 바꿔줄 거라고 말해줘…
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106603].flavor
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [[a1c10p1] Pasywka wroga [9106604] — nazwa] 들려… 또 다른 신의 목소리가…
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106604].name
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [[a1c10p1] Pasywka wroga [9106604] — opis] 전투에 첫 등장 시, [RisingMadnessNoir] 2 얻음\n- 턴 시작 시 이번 전투에서 체력이 처음으로 50% 이하가 되면,\n[RisingMadnessNoir]이 [RisingMadnessNoir2nd]로 변경됨\n\n합 패배 시, [ChargeNoir] 횟수 2 얻음
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106604].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [RisingMadnessNoir], [RisingMadnessNoir2nd], [ChargeNoir]
   znaczenie tagów: [RisingMadnessNoir] = 햇살 / Sunshine; [RisingMadnessNoir2nd] = 따가운 햇살 / Stinging Sunshine; [ChargeNoir] = 보존 / Preservation
   EN: Upon entering the Encounter for the first time, gain 2 [RisingMadnessNoir]\n- Turn Start: When this unit's HP drops below 50% for the first time in this Encounter, convert [RisingMadnessNoir] into [RisingMadnessNoir2nd]\n\nOn Clash Lose, gain +2 [ChargeNoir] Count
   PL: Przy pierwszym pojawieniu się w walce zyskuje 2 [RisingMadnessNoir]\n- Początek tury: gdy HP tej jednostki po raz pierwszy w tej walce spadnie poniżej 50%, [RisingMadnessNoir] zamienia się w [RisingMadnessNoir2nd]\n\nPo przegranej w Starciu zyskuje 2 Licznika [ChargeNoir]
131. [[a1c10p1] Pasywka wroga [9106604] — tekst klimatyczny] 따듯한 목소리를 들었지만 더 변하지 못하고 육신에 정신이 갇힌 채 분열로 광증에 빠졌다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106604].flavor
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [[a1c10p1] Pasywka wroga [9106001] — nazwa] 디깅
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106001].name
   limit: do 40 znaków
   EN: Digging
   PL: Digging
133. [[a1c10p1] Pasywka wroga [9106001] — opis] 합 시작 시 대상이 보유한 효과 1개당, 다음 턴에 [Breath] 위력 2 얻음 (최대 10)\n- 보유한 효과가 3개 이상이면, 다음 턴에 자신의 [Breath] 횟수 3 증가
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106001].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Clash Start: Gain 2 [Breath] Potency next turn for every type of effect on target (max 10)\n- If target has 3+ types of effects, gain +3 [Breath] Count next turn
   PL: Początek Starcia: zyskuje w następnej turze 2 Siły [Breath] za każdy rodzaj efektu celu (maks. 10)\n- jeżeli cel ma 3+ rodzajów efektów, zyskuje w następnej turze 3 Licznika [Breath]
134. [[a1c10p1] Pasywka wroga [9106001] — tekst klimatyczny] 가치를 만들어낼 수 없는 르카키들이기에 가치 있는 것을 뒤집어 찾아내야 한다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106001].flavor
   limit: do 200 znaków
   EN: Unable to create worth or value of their own, the Kakis dig through the pockets of the valued in the department store, searching for things of worth.
   PL: Kaki nie potrafią sami tworzyć wartości — dlatego muszą wygrzebywać cenne rzeczy z kieszeni tych, którzy wartość posiadają.
135. [[a1c10p1] Pasywka wroga [9106002] — nazwa] 트렌드 기다림
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106002].name
   limit: do 40 znaków
   EN: Awaiting Seasonal Trend
   PL: Awaiting Seasonal Trend
136. [[a1c10p1] Pasywka wroga [9106002] — opis] 자신의 [Breath] 위력이 6 이상이면, 코인 위력 +1
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106002].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 6+ [Breath] Potency, Coin Power +1
   PL: przy 6+ Siły [Breath] Moc Monety +1
137. [[a1c10p1] Pasywka wroga [9106002] — tekst klimatyczny] 이번에는 어떤 코어가 트렌드인 거야?!
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106002].flavor
   limit: do 120 znaków
   EN: So, what's the core trend this season? Tell me before everyone else gets one!
   PL: So, what's the core trend this season? Tell me before everyone else gets one!
138. [[a1c10p1] Pasywka wroga [9106003] — nazwa] 지키기 위한 발악
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106003].name
   limit: do 50 znaków
   EN: Clinging to What Little Remains
   PL: Clinging to What Little Remains
139. [[a1c10p1] Pasywka wroga [9106003] — opis] 턴 시작 시 자신의 잃은 체력 10%당, 정신력 3 회복 (최대 15)
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106003].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 3 SP for every 10% missing HP on self (max 15)
   PL: Początek tury: przywraca 3 SP za każde 10% utraconego HP tej jednostki (maks. 15)
140. [[a1c10p1] Pasywka wroga [9106004] — nazwa] 들려… 또 다른 신의 목소리가…
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106004].name
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [[a1c10p1] Pasywka wroga [9106004] — opis] 전투에 첫 등장 시, [RisingMadnessSisyphe] 2 얻음\n- 턴 시작 시 이번 전투에서 체력이 처음으로 50% 이하가 되면,\n[RisingMadnessSisyphe]이 [RisingMadnessSisyphe2nd]로 변경됨
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106004].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [RisingMadnessSisyphe], [RisingMadnessSisyphe2nd]
   znaczenie tagów: [RisingMadnessSisyphe] = 햇살 / Sunshine; [RisingMadnessSisyphe2nd] = 따가운 햇살 / Stinging Sunshine
   EN: Upon entering the Encounter for the first time, gain 2 [RisingMadnessSisyphe]\n- Turn Start: When this unit's HP drops below 50% for the first time in this Encounter, convert [RisingMadnessSisyphe] into [RisingMadnessSisyphe2nd]
   PL: Przy pierwszym pojawieniu się w walce zyskuje 2 [RisingMadnessSisyphe]\n- Początek tury: gdy HP tej jednostki po raz pierwszy w tej walce spadnie poniżej 50%, [RisingMadnessSisyphe] zamienia się w [RisingMadnessSisyphe2nd]
142. [[a1c10p1] Pasywka wroga [9106004] — tekst klimatyczny] 따듯한 목소리를 들었지만 더 변하지 못하고 육신에 정신이 갇힌 채 분열로 광증에 빠졌다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106004].flavor
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [[a1c10p1] Pasywka wroga [9106301] — nazwa] 바느질
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106301].name
   limit: do 40 znaków
   EN: Sewing
   PL: Sewing
144. [[a1c10p1] Pasywka wroga [9106301] — opis] 관통 내성 또는 질투 내성이 1.5 이상인 대상에게 부여하는 [NiddlePin] 수치 +1
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106301].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [NiddlePin]
   znaczenie tagów: [NiddlePin] = 바늘못 / Naildle
   EN: Inflict +1 more [NiddlePin] Stack against targets that have 1.5+ Pierce Resist. or Envy Resist.
   PL: nakłada o 1 więcej Stosów [NiddlePin] na cele mające 1.5+ Odporności na Kłucie lub Zawiść
145. [[a1c10p1] Pasywka wroga [9106301] — tekst klimatyczny] 재봉 땀수가 중요해 땀수
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106301].flavor
   limit: do 120 znaków
   EN: Ends per inch, picks per inch, stitch per inch. Important!
   PL: Ends per inch, picks per inch, stitch per inch. Important!
146. [[a1c10p1] Pasywka wroga [9106302] — nazwa] 작고 뾰족한 못
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106302].name
   limit: do 40 znaków
   EN: Tiny and Sharp Nails
   PL: Tiny and Sharp Nails
147. [[a1c10p1] Pasywka wroga [9106302] — opis] [NiddlePin]을 보유한 적에게 스킬로 [Laceration] 위력을 부여할 때, 부여량 (대상의 [NiddlePin] 수치)만큼 증가 (최대 3)
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106302].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [NiddlePin], [Laceration]
   znaczenie tagów: [NiddlePin] = 바늘못 / Naildle; [Laceration] = 출혈 / Bleed
   EN: When using Skills to inflict [Laceration] Potency against enemies that have [NiddlePin], inflict +([NiddlePin] Stack on target) more [Laceration] Potency (max 3)
   PL: nakładając Umiejętnościami Siłę [Laceration] na wrogów mających [NiddlePin], nakłada dodatkowo (Stosy [NiddlePin] celu) Siły [Laceration] (maks. 3)
148. [[a1c10p1] Pasywka wroga [9106302] — tekst klimatyczny] 못과 바늘은 다르지 않다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106302].flavor
   limit: do 120 znaków
   EN: A needle is no different from a nail.
   PL: Igła nie różni się od gwoździa.
149. [[a1c10p1] Pasywka wroga [9106701] — nazwa] 절박함
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106701].name
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [[a1c10p1] Pasywka wroga [9106701] — opis] 턴 시작 시 자신의 [ChargeRouge] 위력이 3, [ChargeRouge] 횟수가 10 이상이면 강력한 스킬을 사용\n\n자신의 잃은 체력 1%당 스킬 피해량 +1%
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106701].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Turn Start: At 3+ [ChargeRouge] Potency and 10+ [ChargeRouge] Count, use a powerful Skill\n\nSkills deal +1% damage for every 1% missing HP on self
   PL: Początek tury: przy 3+ Siły [ChargeRouge] i 10+ Licznika [ChargeRouge] używa potężnej Umiejętności\n\nUmiejętności zadają +1% obrażeń za każde 1% utraconego HP tej jednostki
151. [[a1c10p1] Pasywka wroga [9106701] — tekst klimatyczny] 더 나답게… 옷만으로 표현되지 않는 진짜 나의 모습을…!
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106701].flavor
   limit: do 120 znaków
   EN: So that I can be myself... My true self, expressed beyond what mere clothes can express!
   PL: So that I can be myself... My true self, expressed beyond what mere clothes can express!
152. [[a1c10p1] Pasywka wroga [9106702] — nazwa] 들려… 또 다른 신의 목소리가…
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106702].name
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [[a1c10p1] Pasywka wroga [9106702] — opis] 스테이지 시작 시, [RisingMadnessRouge] 얻음\n- 턴 시작 시 이번 전투에서 체력이 처음으로 50% 이하가 되면,\n[RisingMadnessRouge]이 [RisingMadnessRouge2nd]로 변경됨\n\n합 패배 시, [ChargeRouge] 횟수 2 얻음
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106702].desc
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [[a1c10p1] Pasywka wroga [9106702] — tekst klimatyczny] 따듯한 목소리를 들었지만 더 변하지 못하고 육신에 정신이 갇힌 채 분열로 광증에 빠졌다.
   źródło: Passives_Enemy-a1c10p1.json :: dataList[id=9106702].flavor
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p2] Wróg / część: Enemies-a1c10p2
- plik gry: `Enemies-a1c10p2.json`

155. [[a1c10p2] Wróg / część [1503] — nazwa] 옛 바다의 검은 실
   źródło: Enemies-a1c10p2.json :: dataList[id=1503].name
   limit: do 40 znaków
   EN: Blackthread of the Elden Sea
   PL: Blackthread of the Elden Sea
156. [[a1c10p2] Wróg / część [150301] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=150301].name
   limit: do 40 znaków
   EN: Body
   PL: Korpus
157. [[a1c10p2] Wróg / część [150302] — nazwa] 왼팔
   źródło: Enemies-a1c10p2.json :: dataList[id=150302].name
   limit: do 40 znaków
   EN: Left Arm
   PL: Lewe Ramie
158. [[a1c10p2] Wróg / część [150303] — nazwa] 오른팔
   źródło: Enemies-a1c10p2.json :: dataList[id=150303].name
   limit: do 40 znaków
   EN: Right Arm
   PL: Prawe Ramie
159. [[a1c10p2] Wróg / część [1501] — nazwa] ???
   źródło: Enemies-a1c10p2.json :: dataList[id=1501].name
   limit: do 40 znaków
   EN: ???
   PL: ???
160. [[a1c10p2] Wróg / część [150101] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=150101].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [[a1c10p2] Wróg / część [1519] — nazwa] 퍼티
   źródło: Enemies-a1c10p2.json :: dataList[id=1519].name
   limit: do 40 znaków
   EN: Putty
   PL: Putty
162. [[a1c10p2] Wróg / część [151901] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=151901].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [[a1c10p2] Wróg / część [1531] — nazwa] 르누아르 점원
   źródło: Enemies-a1c10p2.json :: dataList[id=1531].name
   limit: do 40 znaków
   EN: Le Noir Sales Associate
   PL: Le Noir Sales Associate
164. [[a1c10p2] Wróg / część [1504] — nazwa] 플라넬
   źródło: Enemies-a1c10p2.json :: dataList[id=1504].name
   limit: do 40 znaków
   EN: Flannel
   PL: Flannel
165. [[a1c10p2] Wróg / część [150401] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=150401].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [[a1c10p2] Wróg / część [1505] — nazwa] 르누아르 메종
   źródło: Enemies-a1c10p2.json :: dataList[id=1505].name
   limit: do 40 znaków
   EN: Maison du Noir
   PL: Maison du Noir
167. [[a1c10p2] Wróg / część [150501] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=150501].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [[a1c10p2] Wróg / część [1495] — nazwa] 수선사 아네트
   źródło: Enemies-a1c10p2.json :: dataList[id=1495].name
   limit: do 40 znaków
   EN: Annette the Alterationist
   PL: Annette the Alterationist
169. [[a1c10p2] Wróg / część [149501] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=149501].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [[a1c10p2] Wróg / część [1488] — nazwa] 통제자
   źródło: Enemies-a1c10p2.json :: dataList[id=1488].name
   limit: do 40 znaków
   EN: The Overseer
   PL: The Overseer
171. [[a1c10p2] Wróg / część [1491] — nazwa] 무두질된 죄수
   źródło: Enemies-a1c10p2.json :: dataList[id=1491].name
   limit: do 40 znaków
   EN: Tanned Prisoner
   PL: Tanned Prisoner
172. [[a1c10p2] Wróg / część [1502] — nazwa] 흙에서 태어난 자
   źródło: Enemies-a1c10p2.json :: dataList[id=1502].name
   limit: do 50 znaków
   EN: One Who Emerged from the Earth
   PL: One Who Emerged from the Earth
173. [[a1c10p2] Wróg / część [150201] — nazwa] 몸통
   źródło: Enemies-a1c10p2.json :: dataList[id=150201].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [[a1c10p2] Wróg / część [1506] — nazwa] 르누아르 브랜드 매니저
   źródło: Enemies-a1c10p2.json :: dataList[id=1506].name
   limit: do 40 znaków
   EN: Le Noir's Brand Manager
   PL: Le Noir's Brand Manager
175. [[a1c10p2] Wróg / część [1513] — nazwa] 르누아르 점원
   źródło: Enemies-a1c10p2.json :: dataList[id=1513].name
   (powtórzenie elementu 163 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p2] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c10p2
- grupa rozdziału/trybu: `a1c10p2` · plik: `Skills_Abnormality-a1c10p2.json`

176. [Umiejętność wroga [150301] (ulepszenie 1) — nazwa] 돌려줘…
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].name
   limit: do 40 znaków
   EN: Give It Back...
   PL: Give It Back...
177. [Umiejętność wroga [150301] (ulepszenie 1) — opis] 대상이 수비 스킬을 장착했으면 피해량 -90%\n자신의 [HeavyBlackYarn]만큼 합위력 +1\n[WhenUse] 대상의 [TangleBlackYarn] 5당, 기본 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [HeavyBlackYarn], [WhenUse], [TangleBlackYarn]
   znaczenie tagów: [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: If target has equipped Defense Skills, deal -90% damage\nClash Power +1 for every [HeavyBlackYarn] on self\n[WhenUse] Base Power +1 for every 5 [TangleBlackYarn] on target (max 2)
   PL: jeżeli cel ma założoną Umiejętność obrony, zadaje -90% obrażeń\nzyskuje Moc Starcia +1 za każde 1 [HeavyBlackYarn] tej jednostki\n[WhenUse] Moc Bazowa +1 za każde 5 [TangleBlackYarn] celu (maks. 2)
178. [Umiejętność wroga [150301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL: [OnSucceedAttack] nakłada 2 [Burst]
179. [Umiejętność wroga [150301] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [OnSucceedAttack] Inflict 2 [TangleBlackYarn]
   PL: [OnSucceedAttack] nakłada 2 [TangleBlackYarn]
180. [Umiejętność wroga [150301] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [150301] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150301].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Umiejętność wroga [150302] (ulepszenie 1) — nazwa] 내놔….
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].name
   limit: do 40 znaków
   EN: Hand It Over...
   PL: Hand It Over...
183. [Umiejętność wroga [150302] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n자신의 [HeavyBlackYarn]만큼 합위력 +1\n[WhenUse] 메인 타겟의 [TangleBlackYarn] 3당, 합 위력 +1 (최대 8)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HeavyBlackYarn], [WhenUse], [TangleBlackYarn]
   znaczenie tagów: [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\nGain Clash Power equal to [HeavyBlackYarn] on self\n[WhenUse] Clash Power +1 for every 3 [TangleBlackYarn] on the main target (max 8)
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\nzyskuje Moc Starcia równą wartości [HeavyBlackYarn] tej jednostki\n[WhenUse] Moc Starcia +1 za każde 3 [TangleBlackYarn] głównego celu (maks. 8)
184. [Umiejętność wroga [150302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Umiejętność wroga [150302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Umiejętność wroga [150302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Umiejętność wroga [150302] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [OnSucceedAttack] Inflict 3 [TangleBlackYarn]
   PL: [OnSucceedAttack] nakłada 3 [TangleBlackYarn]
188. [Umiejętność wroga [150302] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]이 15 이상이면, 대상을 흐트러짐 상태로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150302].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [UnBrokenCoinOnSucceedAttack] If target <color=#ff6000><mark=#ff000040><b><u>has 15+ [TangleBlackYarn], Stagger target</u></b></mark></color>
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>15+ [TangleBlackYarn], Oszołamia cel</u></b></mark></color>
189. [Umiejętność wroga [150303] (ulepszenie 1) — nazwa] 앗아가지마….
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150303].levelList[level=1].name
   limit: do 50 znaków
   EN: Don't Take It Away From Me...
   PL: Don't Take It Away From Me...
190. [Umiejętność wroga [150303] (ulepszenie 1) — opis] 자신의 [HeavyBlackYarn]만큼 합위력 +1\n[WhenUse] 메인 타겟의 [TangleBlackYarn] 5당, 기본 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150303].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [HeavyBlackYarn], [WhenUse], [TangleBlackYarn]
   znaczenie tagów: [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: Gain Clash Power equal to [HeavyBlackYarn] on self\n[WhenUse] Base Power +1 for every 5 [TangleBlackYarn] on the main target (max 2)
   PL: zyskuje Moc Starcia równą wartości [HeavyBlackYarn] tej jednostki\n[WhenUse] Moc Bazowa +1 za każde 5 [TangleBlackYarn] głównego celu (maks. 2)
191. [Umiejętność wroga [150303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +3 [Burst] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Burst]
192. [Umiejętność wroga [150303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [150304] (ulepszenie 1) — nazwa] 엉키고 엉킨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].name
   limit: do 40 znaków
   EN: Coiled and Tangled
   PL: Coiled and Tangled
194. [Umiejętność wroga [150304] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n자신의 [HeavyBlackYarn]만큼 합위력 +1\n[WhenUse] 대상의 [TangleBlackYarn] 3당, 합 위력 +1 (최대 8)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HeavyBlackYarn], [WhenUse], [TangleBlackYarn]
   znaczenie tagów: [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\nGain Clash Power equal to [HeavyBlackYarn] on self\n[WhenUse] Clash Power +1 for every 3 [TangleBlackYarn] on target (max 8)
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\nzyskuje Moc Starcia równą wartości [HeavyBlackYarn] tej jednostki\n[WhenUse] Moc Starcia +1 za każde 3 [TangleBlackYarn] celu (maks. 8)
195. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 4 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +4 [Burst] Count
   PL: [OnSucceedAttack] nakłada 4 Licznika [Burst]
196. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [TangleBlackYarn] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [TangleBlackYarn]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [TangleBlackYarn]
198. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [TangleBlackYarn] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 197 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Umiejętność wroga [150304] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]이 15 이상이면, 대상을 흐트러짐 상태로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150304].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Umiejętność wroga [150305] (ulepszenie 1) — nazwa] 옛것의 몸부림
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].name
   limit: do 40 znaków
   EN: Thrashing of an Elden Being
   PL: Thrashing of an Elden Being
205. [Umiejętność wroga [150305] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n자신의 [HeavyBlackYarn]만큼 합위력 -1\n[WhenUse] 메인 타겟의 [TangleBlackYarn] 3당, 기본 위력 +1 (최대 3)\n[WhenUse] 메인 타겟의 [TangleBlackYarn]이 15 이상이면, 기본 위력 +3
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [HeavyBlackYarn], [WhenUse], [TangleBlackYarn]
   znaczenie tagów: [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\nLose Clash Power equal to [HeavyBlackYarn] on self\n[WhenUse] Base Power +1 for every 3 [TangleBlackYarn] on the main target (max 3)\n[WhenUse] If the main target has 15+ [TangleBlackYarn], Base Power +3
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\ntraci Moc Starcia równą wartości [HeavyBlackYarn] tej jednostki\n[WhenUse] Moc Bazowa +1 za każde 3 [TangleBlackYarn] głównego celu (maks. 3)\n[WhenUse] jeżeli główny cel ma 15+ [TangleBlackYarn], Moc Bazowa +3
206. [Umiejętność wroga [150305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Umiejętność wroga [150305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Umiejętność wroga [150305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [150305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Umiejętność wroga [150305] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]이 15 이상이면, 대상을 흐트러짐 상태로 만듦</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150305].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Umiejętność wroga [150306] (ulepszenie 1) — nazwa] 뒤엉킴
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].name
   limit: do 40 znaków
   EN: Tangling
   PL: Tangling
212. [Umiejętność wroga [150306] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n자신의 [HeavyBlackYarn]만큼 합위력 -1\n[WhenUse] 메인 타겟의 [TangleBlackYarn] 3당, 기본 위력 +1 (최대 3)\n[WhenUse] 메인 타겟의 [TangleBlackYarn]이 15 이상이면, 기본 위력 +3
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].desc
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Umiejętność wroga [150306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Burst]
214. [Umiejętność wroga [150306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [OnSucceedAttack] Inflict 5 [TangleBlackYarn]
   PL: [OnSucceedAttack] nakłada 5 [TangleBlackYarn]
215. [Umiejętność wroga [150306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL: [OnSucceedAttack] nakłada 3 [Burst]
216. [Umiejętność wroga [150306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [TangleBlackYarn] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 214 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Umiejętność wroga [150307] (ulepszenie 1) — nazwa] 무저갱의 아가리
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].name
   limit: do 40 znaków
   EN: Abyssal Maw
   PL: Abyssal Maw
218. [Umiejętność wroga [150307] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[StartBattle] 대상의 [TangleBlackYarn] 2당, 기본 위력 +1, 피해량 +10%
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [TangleBlackYarn]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[StartBattle] Base Power +1 and deal +10% damage for every 2 [TangleBlackYarn] on target
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[StartBattle] Moc Bazowa +1 i zadaje +10% obrażeń za każde 2 [TangleBlackYarn] celu
219. [Umiejętność wroga [150307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [TangleBlackYarn] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [TangleBlackYarn]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [TangleBlackYarn]
220. [Umiejętność wroga [150307] (ulepszenie 1) — moneta 1, efekt 2 — opis] [DefeatDuelAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn] 10 제거</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [DefeatDuelAttack], [TangleBlackYarn]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>Remove 10 [TangleBlackYarn]</u></b></mark></color> on target
   PL: [DefeatDuelAttack] <color=#ff6000><mark=#ff000040><b><u>usuwa 10 [TangleBlackYarn]</u></b></mark></color> celu
221. [Umiejętność wroga [150307] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 <color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태</u></b></mark></color>이거나 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]이 20 이상</u></b></mark></color>이면, 이 코인 재사용 (스킬당 1회)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [TangleBlackYarn]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: [OnSucceedAttack] If target is <color=#ff6000><mark=#ff000040><b><u>Staggered</u></b></mark></color> or if target <color=#ff6000><mark=#ff000040><b><u>has 20+ [TangleBlackYarn]</u></b></mark></color>, Reuse this Coin (once per Skill)
   PL: [OnSucceedAttack] jeżeli cel jest <color=#ff6000><mark=#ff000040><b><u>Oszołamiony</u></b></mark></color> albo cel ma <color=#ff6000><mark=#ff000040><b><u>20+ [TangleBlackYarn]</u></b></mark></color>, używa tej Monety ponownie (1 raz na Umiejętność)
222. [Umiejętność wroga [150307] (ulepszenie 1) — moneta 1, efekt 4 — opis] [ReUseOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상 최대 체력의 150%만큼 고정 피해</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150307].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [ReUseOnSucceedAttack]
   znaczenie tagów: [ReUseOnSucceedAttack] = [재사용 적중시] / [Reuse - On Hit]
   EN: [ReUseOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal fixed damage equal to 150% of target's max HP</u></b></mark></color>
   PL: [ReUseOnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje obrażenia stałe równe 150% Maks. HP celu</u></b></mark></color>
223. [Umiejętność wroga [150308] (ulepszenie 1) — nazwa] 씻어내기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150308].levelList[level=1].name
   limit: do 40 znaków
   EN: Cleansing
   PL: Cleansing
224. [Umiejętność wroga [150308] (ulepszenie 1) — opis] [DuelCounter]\n[WhenUse] 대상의 [TangleBlackYarn] 2당, 기본 위력 +1\n[WinDuel] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]을 모두 제거</u></b></mark></color>하고, 이 스킬을 사용한 부위의 [SickBlackYarn]을 모두 제거\n[DefeatDuel] 대상의 <color=#ff6000><mark=#ff000040><b><u>[TangleBlackYarn]을 모두 제거</u></b></mark></color>하고, 이 스킬을 사용한 부위의 [SickBlackYarn] 절반 감소 (소수점 올림)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150308].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DuelCounter], [WhenUse], [TangleBlackYarn], [WinDuel], [SickBlackYarn], [DefeatDuel]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [WhenUse] = [사용시] / [On Use]; [TangleBlackYarn] = 뒤엉킴 / Tangling; [WinDuel] = [합 승리시] / [Clash Win]; [SickBlackYarn] = 뜯겨져 나가는 검은실밥 / Bursting Blackstitch; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DuelCounter]\n[WhenUse] Base Power +1 for every 2 [TangleBlackYarn] on target\n[WinDuel] <color=#ff6000><mark=#ff000040><b><u>Remove all [TangleBlackYarn] on target</u></b></mark></color>, then remove all [SickBlackYarn] from the Part that used this Skill\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>Remove all [TangleBlackYarn] on target</u></b></mark></color>, then halve the [SickBlackYarn] from the Part that used this Skill (rounded up)
   PL: [DuelCounter]\n[WhenUse] Moc Bazowa +1 za każde 2 [TangleBlackYarn] celu\n[WinDuel] <color=#ff6000><mark=#ff000040><b><u>usuwa wszystkie [TangleBlackYarn] celu</u></b></mark></color>, po czym usuwa wszystkie [SickBlackYarn] z Części, która użyła tej Umiejętności\n[DefeatDuel] <color=#ff6000><mark=#ff000040><b><u>usuwa wszystkie [TangleBlackYarn] celu</u></b></mark></color>, po czym zmniejsza o połowę [SickBlackYarn] Części, która użyła tej Umiejętności (zaokrąglone w górę)
225. [Umiejętność wroga [150308] (ulepszenie 1) — tekst klimatyczny] 하지만 백화점의 시대에서 옛 시대의 잔재는 씻겨지지 않는다.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150308].levelList[level=1].flavor
   limit: do 130 znaków
   EN: Alas, the remnants of the elden age cannot be cleansed away in the Age of the Department Store.
   PL: A jednak pozostałości dawnego wieku nie dadzą się obmyć w Erze Domu Towarowego.
226. [Umiejętność wroga [150308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [150308] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150308].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 3 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 3 [Binding] w następnej turze
228. [Umiejętność wroga [150101] (ulepszenie 1) — nazwa] 봄의 탄생
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].name
   limit: do 40 znaków
   EN: Spring's Genesis
   PL: Spring's Genesis
229. [Umiejętność wroga [150101] (ulepszenie 1) — opis] [EndSkill] <color=#ff6000><mark color=#ff000040><b><u>대상의 정신력 -5</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [EndSkill], [FlowerLaurelWreath]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: [EndSkill] <color=#ff6000><mark color=#ff000040><b><u>Target loses 5 SP</color></mark></b></u>\n- Except targets that have [FlowerLaurelWreath]
   PL: [EndSkill] <color=#ff6000><mark color=#ff000040><b><u>cel traci 5 SP</u></b></mark></color>\n- z wyjątkiem celów mających [FlowerLaurelWreath]
230. [Umiejętność wroga [150101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
231. [Umiejętność wroga [150101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Sinking]
232. [Umiejętność wroga [150101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [150101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Vibration]
234. [Umiejętność wroga [150102] (ulepszenie 1) — nazwa] 가을의 저뭄
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150102].levelList[level=1].name
   limit: do 40 znaków
   EN: Autumn's Passing
   PL: Autumn's Passing
235. [Umiejętność wroga [150102] (ulepszenie 1) — opis] [EndSkill] <color=#ff6000><mark color=#ff000040><b><u>대상의 정신력 -5</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150102].levelList[level=1].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Umiejętność wroga [150102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Sinking]
237. [Umiejętność wroga [150102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration]
   PL: [OnSucceedAttack] nakłada 2 [Vibration]
238. [Umiejętność wroga [150103] (ulepszenie 1) — nazwa] 사람이 되고 싶었던 인형
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150103].levelList[level=1].name
   limit: do 50 znaków
   EN: A Doll Who Yearned to be Human
   PL: A Doll Who Yearned to be Human
239. [Umiejętność wroga [150103] (ulepszenie 1) — opis] [WhenUse] 대상의 [Vibration] 위력과 [Sinking] 위력의 합 3당 최종 위력 +1 (최대 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>대상의 정신력 -10</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150103].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Vibration], [Sinking], [EndSkill], [FlowerLaurelWreath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: [WhenUse] Final Power +1 for every 3 ([Vibration] Potency + [Sinking] Potency) on target (max 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>Target loses 10 SP</color></mark></b></u>\n- Does not activate for targets that have [FlowerLaurelWreath]
   PL: [WhenUse] Moc Końcowa +1 za każde 3 (Siła [Vibration] + Siła [Sinking]) celu (maks. 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>cel traci 10 SP</u></b></mark></color>\n- nie uruchamia się na celach mających [FlowerLaurelWreath]
240. [Umiejętność wroga [150103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
241. [Umiejętność wroga [150103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [Sinking] 위력만큼 정신력 피해
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Deal SP damage equal to [Sinking] Potency on target
   PL: [OnSucceedAttack] zadaje obrażenia SP równe Siły [Sinking] celu
242. [Umiejętność wroga [150104] (ulepszenie 1) — nazwa] 인형이 되고 싶었던 사람
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].name
   limit: do 50 znaków
   EN: A Human Who Yearned to be a Doll
   PL: A Human Who Yearned to be a Doll
243. [Umiejętność wroga [150104] (ulepszenie 1) — opis] [WideAreaRampage]\n[WhenUse] 메인 타겟의 [Vibration] 위력과 [Sinking] 위력의 합 3당 최종 위력 +1 (최대 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>모든 대상의 정신력 -10</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WideAreaRampage], [WhenUse], [Vibration], [Sinking], [EndSkill], [FlowerLaurelWreath]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: [WideAreaRampage]\n[WhenUse] Final Power +1 for every 3 ([Vibration] Potency + [Sinking] Potency) on the main target (max 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>All targets lose 10 SP</color></mark></b></u>\n- Does not activate for targets that have [FlowerLaurelWreath]
   PL: [WideAreaRampage]\n[WhenUse] Moc Końcowa +1 za każde 3 (Siła [Vibration] + Siła [Sinking]) głównego celu (maks. 2)\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>wszystkie cele tracą 10 SP</u></b></mark></color>\n- nie uruchamia się na celach mających [FlowerLaurelWreath]
244. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [AlriuneSillage] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneSillage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneSillage] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 5 [AlriuneSillage]
   PL: [OnSucceedAttack] nakłada 5 [AlriuneSillage]
246. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [AlriuneSillage] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 3, efekt 2 — opis] 이 코인은 모든 공격 대상에게 적중함
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin hits all targets of the attack
   PL: ta Moneta trafia wszystkie cele ataku
250. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 1 [Vibration]
   PL: [OnSucceedAttack] nakłada 1 [Vibration]
251. [Umiejętność wroga [150104] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150104].levelList[level=1].coinlist[#2].coindescs[#3].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Umiejętność wroga [150105] (ulepszenie 1) — nazwa] 좋은 향기가 나는 월계관
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150105].levelList[level=1].name
   limit: do 40 znaków
   EN: Fragrant Laurel Wreath
   PL: Fragrant Laurel Wreath
253. [Umiejętność wroga [150105] (ulepszenie 1) — opis] <color=#ff6000><mark color=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</color></mark></b></u>\n이 스킬은 피해를 주지 않고, 대상의 [Sinking]을 발동 시키지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>대상에게 [FlowerLaurelWreath]을 부여함 (턴당 1회)</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150105].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Sinking], [EndSkill], [FlowerLaurelWreath]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [EndSkill] = [공격 종료시] / [Attack End]; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: <color=#ff6000><mark color=#ff000040><b><u>Can Clash with this Skill regardless of Speed</color></mark></b></u>\nThis Skill does not deal damage and does not activate [Sinking] on target\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>Apply [FlowerLaurelWreath] on target (once per turn)</color></mark></b></u>
   PL: <color=#ff6000><mark color=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\nta Umiejętność nie zadaje obrażeń i nie uruchamia [Sinking] celu\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>nakłada [FlowerLaurelWreath] na cel (1 raz na turę)</u></b></mark></color>
254. [Umiejętność wroga [150105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [150105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 정신력 20 회복
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target heals 20 SP
   PL: [OnSucceedAttack] cel przywraca 20 SP
256. [Umiejętność wroga [150106] (ulepszenie 1) — nazwa] 흙으로 돌아가고자 하는 소망을 품고
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].name
   limit: do 60 znaków
   EN: Bearing the hope to return to dust...
   PL: Bearing the hope to return to dust...
257. [Umiejętność wroga [150106] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [Vibration] 위력과 [Sinking] 위력의 합 3당 최종 위력 +1 (최대 8)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>메인 타겟에게 [FlowerLaurelWreath]이 없으면, 최종 위력 +5</color></mark></b></u>\n[DefeatDuel]\n- 피해량 80%만큼 감소\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n- 대상의 [Sinking]을 발동 시키지 않음\n\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>모든 대상의 정신력 -10</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외\n[EndSkillAll] 자신의 [AlriunePetal]을 0으로 초기화
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WhenUse], [Vibration], [Sinking], [FlowerLaurelWreath], [DefeatDuel], [EndSkill], [EndSkillAll], [AlriunePetal]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [Sinking] = 침잠 / Sinking; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]; [EndSkillAll] = [스킬 종료시] / [Skill End]; [AlriunePetal] = 꽃잎 / Petals
   EN: [WhenUse] Final Power +1 for every 3 ([Vibration] Potency + [Sinking] Potency) on the main target (max 8)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>If the main target does not have [FlowerLaurelWreath], Final Power +5</color></mark></b></u>\n[DefeatDuel]\n- Deal -80% damage\n- Damage dealt by this Skill cannot Stagger the target\n- Does not activate [Sinking] on target\n\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>All targets lose 10 SP</color></mark></b></u>\n- Does not activate for targets that have [FlowerLaurelWreath]\n[EndSkillAll] Reset [AlriunePetal] on self to 0 Stack
   PL: [WhenUse] Moc Końcowa +1 za każde 3 (Siła [Vibration] + Siła [Sinking]) głównego celu (maks. 8)\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>jeżeli główny cel nie ma [FlowerLaurelWreath], Moc Końcowa +5</u></b></mark></color>\n[DefeatDuel]\n- zadaje -80% obrażeń\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n- nie uruchamia [Sinking] celu\n\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>wszystkie cele tracą 10 SP</u></b></mark></color>\n- nie uruchamia się na celach mających [FlowerLaurelWreath]\n[EndSkillAll] zeruje Stosy [AlriunePetal] tej jednostki do 0
258. [Umiejętność wroga [150106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [150106] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [AlriuneSillage]만큼 [Vibration] 위력 부여 (각자 적용)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AlriuneSillage], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AlriuneSillage] = 잔향 / Faint Aroma; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict [Vibration] Potency equal to [AlriuneSillage] on target (calculated per-target)
   PL: [UnBrokenCoinOnSucceedAttack] nakłada Siłę [Vibration] równą wartości [AlriuneSillage] celu (rozpatrywane osobno dla każdego celu)
260. [Umiejętność wroga [150106] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [AlriuneSillage]만큼 [Sinking] 위력 부여 (각자 적용)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [AlriuneSillage], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [AlriuneSillage] = 잔향 / Faint Aroma; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict [Sinking] Potency equal to [AlriuneSillage] on target (calculated per-target)
   PL: [UnBrokenCoinOnSucceedAttack] nakłada Siłę [Sinking] równą wartości [AlriuneSillage] celu (rozpatrywane osobno dla każdego celu)
261. [Umiejętność wroga [150106] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150106].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
262. [Umiejętność wroga [150107] (ulepszenie 1) — nazwa] 살고자 하는 모든 것들과 무덤으로 돌아가리
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150107].levelList[level=1].name
   limit: do 90 znaków
   EN: ... It shall go back to the grave with all that desires to live
   PL: ... It shall go back to the grave with all that desires to live
263. [Umiejętność wroga [150107] (ulepszenie 1) — opis] [CantDuel] [CantChangeTarget]\n이 스킬은 대상의 수비 스킬을 발동 시키지 않음\n대상이 패닉 또는 침식 상태가 아니면 공격이 취소됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150107].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]
   EN: [CantDuel] [CantChangeTarget]\nThis Skill does not trigger the target's Defense Skill\nIf target is not Panicked or Corroded, cancel this attack
   PL: [CantDuel] [CantChangeTarget]\nta Umiejętność nie uruchamia Umiejętności obrony celu\njeżeli cel nie jest w Panice ani w Korozji, atak zostaje anulowany
264. [Umiejętność wroga [150107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상 최대 체력의 120%만큼 고정 피해
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal fixed damage equal to 120% of target's max HP
   PL: [OnSucceedAttack] zadaje obrażenia stałe równe 120% Maks. HP celu
265. [Umiejętność wroga [150108] (ulepszenie 1) — nazwa] 모두의 마음 속 욕망이 꽃으로 대체될 때가 온다면...
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150108].levelList[level=1].name
   limit: do 90 znaków
   EN: When flowers substitute all the desire in everyone's hearts...
   PL: When flowers substitute all the desire in everyone's hearts...
266. [Umiejętność wroga [150108] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n이 스킬은 피해를 주지 않음\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>대상의 정신력 -25</color></mark></b></u>\n- [FlowerLaurelWreath]을 보유한 대상은 제외
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150108].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [EndSkill], [FlowerLaurelWreath]
   znaczenie tagów: [EndSkill] = [공격 종료시] / [Attack End]; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: Can Clash with this Skill regardless of Speed\nThis Skill does not deal damage\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>Target loses 25 SP</color></mark></b></u>\n- Except targets that have [FlowerLaurelWreath]
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nta Umiejętność nie zadaje obrażeń\n[EndSkill] <color=#ff6000><mark color=#ff000040><b><u>cel traci 25 SP</u></b></mark></color>\n- z wyjątkiem celów mających [FlowerLaurelWreath]
267. [Umiejętność wroga [150108] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150108].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [150108] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 침잠 10 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150108].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 10 [Sinking]
269. [Umiejętność wroga [150201] (ulepszenie 1) — nazwa] 꽃무더기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150201].levelList[level=1].name
   limit: do 40 znaków
   EN: Flower Mound
   PL: Flower Mound
270. [Umiejętność wroga [150201] (ulepszenie 1) — opis] 이 스킬의 피해는 0으로 고정됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150201].levelList[level=1].desc
   limit: do 120 znaków
   EN: This Skill's damage is fixed to 0
   PL: obrażenia tej Umiejętności są ustalone na 0
271. [Umiejętność wroga [150201] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [AlriuneSillage] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AlriuneSillage]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AlriuneSillage] = 잔향 / Faint Aroma
   EN: [OnSucceedAttack] Inflict 1 [AlriuneSillage]
   PL: [OnSucceedAttack] nakłada 1 [AlriuneSillage]
272. [Umiejętność wroga [150201] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [AlriuneSillage] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150201].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [150202] (ulepszenie 1) — nazwa] 마음의 균열
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150202].levelList[level=1].name
   limit: do 40 znaków
   EN: A Crack in the Heart
   PL: A Crack in the Heart
274. [Umiejętność wroga [150202] (ulepszenie 1) — opis] 이 스킬의 피해는 0으로 고정됨\n[WhenUse] 대상의 부정적인 효과의 위력 합 3개당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150202].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: This Skill's damage is fixed to 0\n[WhenUse] Final Power +1 for every 3 (sum of Potency of negative effects on target) (max 2)
   PL: obrażenia tej Umiejętności są ustalone na 0\n[WhenUse] Moc Końcowa +1 za każde 3 (suma Siły negatywnych efektów celu) (maks. 2)
275. [Umiejętność wroga [150202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] nakłada 4 [Sinking]
276. [Umiejętność wroga [150202] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150202].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 4 [Vibration]
   PL: [OnSucceedAttack] nakłada 4 [Vibration]
277. [Umiejętność wroga [150202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 1 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 1 [Vulnerable] w następnej turze
278. [Umiejętność wroga [150203] (ulepszenie 1) — nazwa] 휘감아드는 절망
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150203].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangling Despair
   PL: Entangling Despair
279. [Umiejętność wroga [150203] (ulepszenie 1) — opis] 이 스킬의 피해는 0으로 고정됨\n[WhenUse] 대상의 부정적인 효과의 합 3개당 최종 위력 +1 (최대 3)\n[DefeatDuel]\n- 대상의 [Sinking]을 발동 시키지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150203].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [DefeatDuel], [Sinking]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Sinking] = 침잠 / Sinking
   EN: This Skill's damage is fixed to 0\n[WhenUse] Final Power +1 for every 3 types of negative effects on target (max 3)\n[DefeatDuel]\n- Does not activate [Sinking] on target
   PL: obrażenia tej Umiejętności są ustalone na 0\n[WhenUse] Moc Końcowa +1 za każde 3 rodzaje negatywnych efektów celu (maks. 3)\n[DefeatDuel]\n- nie uruchamia [Sinking] celu
280. [Umiejętność wroga [150203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [150203] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150203].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Umiejętność wroga [150203] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>대상의 [Sinking] 위력만큼 정신력 피해</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150203].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>Deal SP damage equal to [Sinking] Potency on target</color></mark></b></u>
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>zadaje obrażenia SP równe Siły [Sinking] celu</u></b></mark></color>
283. [Umiejętność wroga [151901] (ulepszenie 1) — nazwa] 시동
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151901].levelList[level=1].name
   limit: do 40 znaków
   EN: Revving Up
   PL: Revving Up
284. [Umiejętność wroga [151901] (ulepszenie 1) — opis] [StartBattle]\n<color=#ff6000><mark color=#ff000040><b><u>- 자신의 최대 체력의 30%만큼 보호막을 얻음</color></mark></b></u>\n- 자신의 [ChargeKhaki] 횟수를 최대로 회복\n- 다음 턴에 [SpreadingDye] 1 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151901].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [StartBattle], [ChargeKhaki], [SpreadingDye]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [SpreadingDye] = 글로스 미디엄 / Gloss Medium
   EN: [StartBattle]\n<color=#ff6000><mark color=#ff000040><b><u>- Gain Shield equal to 30% of this unit's max HP</color></mark></b></u>\n- Regain [ChargeKhaki] Count up to the maximum cap\n- Gain 1 [SpreadingDye] next turn
   PL: [StartBattle]\n<color=#ff6000><mark color=#ff000040><b><u>- zyskuje Tarczę równą 30% Maks. HP tej jednostki</u></b></mark></color>\n- odzyskuje Liczniki [ChargeKhaki] do maksymalnego limitu\n- zyskuje 1 [SpreadingDye] w następnej turze
285. [Umiejętność wroga [151902] (ulepszenie 1) — nazwa] 실 걸기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151902].levelList[level=1].name
   limit: do 40 znaków
   EN: Threading
   PL: Threading
286. [Umiejętność wroga [151902] (ulepszenie 1) — opis] 자신의 [ChargeKhaki] 위력 2당 합 위력 +1 (최대 3)\n[WhenUse] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151902].levelList[level=1].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeKhaki], [WhenUse], [Agility]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: Clash Power +1 for every 2 [ChargeKhaki] Potency on self (max 3)\n[WhenUse] Gain 1 [Agility] next turn
   PL: Moc Starcia +1 za każde 2 Siły [ChargeKhaki] tej jednostki (maks. 3)\n[WhenUse] zyskuje 1 [Agility] w następnej turze
287. [Umiejętność wroga [151902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Umiejętność wroga [151902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>다음 턴에 [Binding] 1 부여</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [UnBrokenCoinOnSucceedAttack], [Binding]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Binding] = 속박 / Bind
   EN: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>Inflict 1 [Binding] next turn</color></mark></b></u>
   PL: [UnBrokenCoinOnSucceedAttack] <color=#ff6000><mark color=#ff000040><b><u>nakłada 1 [Binding] w następnej turze</u></b></mark></color>
289. [Umiejętność wroga [151903] (ulepszenie 1) — nazwa] 환봉
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].name
   limit: do 40 znaków
   EN: Lockstitch
   PL: Lockstitch
290. [Umiejętność wroga [151903] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높으면, 피해량 +20%\n자신의 [ChargeKhaki] 위력 2당 코인 위력 +1 (최대 2)\n[WhenUse] [ChargeKhaki] 횟수 4 소모하여, 코인 위력 +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 속도가 대상보다 빠르거나 자신의 체력이 50% 미만일 때,</color></mark></b></u>\n- 모든 코인이 [SuperCoin]으로 변경됨\n- (대상과의 속도 차이 x 15)%만큼 피해량 증가[TabExplain] (최대 40%)\n<color=#ff6000><mark color=#ff000040><b><u>[DefeatDuel] 다음 턴에 [Binding] 1 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChargeKhaki], [WhenUse], [SuperCoin], [TabExplain], [DefeatDuel], [Binding]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [DefeatDuel] = [합 패배] / [Clash Lose]; [Binding] = 속박 / Bind
   EN: If this unit's Speed is faster than the target's, deal +20% damage\nCoin Power +1 for every 2 [ChargeKhaki] Potency on self (max 2)\n[WhenUse] Consume 4 [ChargeKhaki] Count to gain Coin Power +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>If this unit's Speed is faster than the target's, or if this unit has lower than 50% HP</color></mark></b></u>:\n- Convert all Coins to [SuperCoin]s\n- Deal +(Speed difference x 15)% damage (max 40%)\n<color=#ff6000><mark color=#ff000040><b><u>[DefeatDuel] Gain 1 [Binding] next turn</color></mark></b></u>
   PL: jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +20% obrażeń\nMoc Monety +1 za każde 2 Siły [ChargeKhaki] tej jednostki (maks. 2)\n[WhenUse] zużywa 4 Licznika [ChargeKhaki], aby zyskać Moc Monety +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>jeżeli Szybkość tej jednostki jest większa niż celu albo HP tej jednostki jest poniżej 50%,</u></b></mark></color>:\n- wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n- zadaje +(różnica Szybkości względem celu x 15)% obrażeń[TabExplain] (maks. 40%)\n<color=#ff6000><mark color=#ff000040><b><u>[DefeatDuel] zyskuje 1 [Binding] w następnej turze</u></b></mark></color>
291. [Umiejętność wroga [151903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 4 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 4 [Laceration]
   PL: [OnSucceedAttack] nakłada 4 [Laceration]
292. [Umiejętność wroga [151903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ThreadDye] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ThreadDye]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ThreadDye] = 염색실 / Dyed Thread
   EN: [OnSucceedAttack] Inflict 1 [ThreadDye]
   PL: [OnSucceedAttack] nakłada 1 [ThreadDye]
293. [Umiejętność wroga [151903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ThreadDye] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ThreadDye]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ThreadDye] = 염색실 / Dyed Thread
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [ThreadDye]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [ThreadDye]
294. [Umiejętność wroga [151903] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인이 [SuperCoin]이면, <color=#ff6000><mark color=#ff000040><b><u>[ChargeKhaki] 횟수 4 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151903].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [OnSucceedAttack], [SuperCoin], [ChargeKhaki]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: [OnSucceedAttack] If this is an [SuperCoin], <color=#ff6000><mark color=#ff000040><b><u>Gain +4 [ChargeKhaki] Count</color></mark></b></u>
   PL: [OnSucceedAttack] jeżeli ta Moneta jest [SuperCoin], <color=#ff6000><mark color=#ff000040><b><u>zyskuje 4 Licznika [ChargeKhaki]</u></b></mark></color>
295. [Umiejętność wroga [151904] (ulepszenie 1) — nazwa] 본봉
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].name
   limit: do 40 znaków
   EN: Chainstitch
   PL: Chainstitch
296. [Umiejętność wroga [151904] (ulepszenie 1) — opis] 자신의 속도가 대상보다 높으면, 피해량 +20%\n자신의 [ChargeKhaki] 위력 2당 코인 위력 +1 (최대 2)\n[WhenUse] [ChargeKhaki] 횟수 4 소모하여, 코인 위력 +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>자신의 속도가 대상보다 빠르거나 자신의 체력이 50% 미만일 때,</color></mark></b></u>\n- 모든 코인이 [SuperCoin]으로 변경됨\n- (대상과의 속도 차이 x 15)%만큼 피해량 증가[TabExplain] (최대 40%)\n[WinDuel] 다음 턴에 [Agility] 1 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChargeKhaki], [WhenUse], [SuperCoin], [TabExplain], [WinDuel], [Agility]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [WhenUse] = [사용시] / [On Use]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WinDuel] = [합 승리시] / [Clash Win]; [Agility] = 신속 / Haste
   EN: If this unit's Speed is faster than the target's, deal +20% damage\nCoin Power +1 for every 2 [ChargeKhaki] Potency on self (max 2)\n[WhenUse] Consume 4 [ChargeKhaki] Count to gain Coin Power +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>If this unit's Speed is faster than the target's, or if this unit has lower than 50% HP</color></mark></b></u>:\n- Convert all Coins to [SuperCoin]s\n- Deal +(Speed difference x 15)% damage (max 40%)\n[WinDuel] Gain 1 [Agility] next turn
   PL: jeżeli Szybkość tej jednostki jest większa niż celu, zadaje +20% obrażeń\nMoc Monety +1 za każde 2 Siły [ChargeKhaki] tej jednostki (maks. 2)\n[WhenUse] zużywa 4 Licznika [ChargeKhaki], aby zyskać Moc Monety +2\n[WhenUse] <color=#ff6000><mark color=#ff000040><b><u>jeżeli Szybkość tej jednostki jest większa niż celu albo HP tej jednostki jest poniżej 50%,</u></b></mark></color>:\n- wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n- zadaje +(różnica Szybkości względem celu x 15)% obrażeń[TabExplain] (maks. 40%)\n[WinDuel] zyskuje 1 [Agility] w następnej turze
297. [Umiejętność wroga [151904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Laceration]
298. [Umiejętność wroga [151904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [ThreadDye] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 292 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Umiejętność wroga [151904] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [ThreadDye] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Umiejętność wroga [151904] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 이 코인이 [SuperCoin]이면, <color=#ff6000><mark color=#ff000040><b><u>[ChargeKhaki] 횟수 4 얻음</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151904].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Umiejętność wroga [151905] (ulepszenie 1) — nazwa] 삼봉 레인보우 오버로크
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].name
   limit: do 60 znaków
   EN: 2-needle Bottom Coverstitch Rainbow Overlock
   PL: 2-needle Bottom Coverstitch Rainbow Overlock
302. [Umiejętność wroga [151905] (ulepszenie 1) — opis] [WideAreaRampage]\n속도와 상관없이 이 스킬과 합을 할 수 있음\n자신의 [ChargeKhaki] 위력 2당 최종 위력 +1 (최대 3)\n[WhenUse] 자신의 [ChargeKhaki] 횟수 전부 소모하여, 소모한 [ChargeKhaki] 횟수 1당 피해량 +5%\n[WhenUse] 메인 타겟의 [Laceration] 위력과 [Laceration] 횟수의 합 3당 코인 위력 +1 (최대 3)\n[DefeatDuel]\n- [AttackDmgDown] 10, [Paralysis] 4 얻음\n- 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkillAll] <color=#ff6000><mark color=#ff000040><b><u>이번 턴 종료</color></mark></b></u>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [WideAreaRampage], [ChargeKhaki], [WhenUse], [Laceration], [DefeatDuel], [AttackDmgDown], [Paralysis], [EndSkillAll]
   znaczenie tagów: [WideAreaRampage] = 광역 난사 / Unfocused Volley; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [DefeatDuel] = [합 패배] / [Clash Lose]; [AttackDmgDown] = 피해량 감소 / Damage Down; [Paralysis] = 마비 / Paralyze; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [WideAreaRampage]\nCan Clash with this Skill regardless of Speed\nFinal Power +1 for every 2 [ChargeKhaki] Potency on self (max 3)\n[WhenUse] Consume all [ChargeKhaki] Count on self and deal +5% damage for every [ChargeKhaki] Count consumed\n[WhenUse] Coin Power +1 for every 3 ([Laceration] Potency + [Laceration] Count) on the main target (max 3)\n[DefeatDuel]\n- Gain 10 [AttackDmgDown] and 4 [Paralysis]\n- This Skill cannot Stagger the target\n[EndSkillAll] <color=#ff6000><mark color=#ff000040><b><u>End this turn</color></mark></b></u>
   PL: [WideAreaRampage]\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nMoc Końcowa +1 za każde 2 Siły [ChargeKhaki] tej jednostki (maks. 3)\n[WhenUse] zużywa wszystkie Liczniki [ChargeKhaki] tej jednostki i zadaje +5% obrażeń za każde 1 zużytego Licznika [ChargeKhaki]\n[WhenUse] Moc Monety +1 za każde 3 (Siła [Laceration] + Licznik [Laceration]) głównego celu (maks. 3)\n[DefeatDuel]\n- zyskuje 10 [AttackDmgDown] i 4 [Paralysis]\n- obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkillAll] <color=#ff6000><mark color=#ff000040><b><u>kończy tę turę</u></b></mark></color>
303. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL: [OnSucceedAttack] nakłada 2 [Laceration]
305. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Laceration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Laceration]
306. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 2 — opis] 이 코인은 모든 대상에게 적중
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   EN: This Coin hits all targets
   PL: ta Moneta trafia wszystkie cele
314. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] 대상의 [Laceration] 1회 발동 ([Laceration] 횟수 1 감소)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Laceration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Laceration] = 출혈 / Bleed
   EN: [UnBrokenCoinOnSucceedAttack] Activate [Laceration] on target once (target loses 1 [Laceration] Count)
   PL: [UnBrokenCoinOnSucceedAttack] aktywuje [Laceration] na celu 1 raz (cel traci 1 Licznika [Laceration])
315. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 다음 턴에 [ThreadDye] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ThreadDye]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ThreadDye] = 염색실 / Dyed Thread
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [ThreadDye] next turn
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [ThreadDye] w następnej turze
316. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 5 — opis] [OnSucceedAttack] [Inactible] 효과를 보유한 대상에게 아래 효과 적용
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Inactible]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Inactible] = 행동 불가 / Immobilized
   EN: [OnSucceedAttack] Apply the following on targets that have [Inactible]
   PL: [OnSucceedAttack] stosuje poniższe efekty na celach mających [Inactible]
317. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 6 — opis] - 다음 턴에 흐트러짐 상태로 만듦
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#5].desc
   limit: do 120 znaków
   EN: - Become Staggered next turn
   PL: - w następnej turze Oszołamia cel
318. [Umiejętność wroga [151905] (ulepszenie 1) — moneta 4, efekt 7 — opis] - 이 코인 최종 피해량의 20%만큼 색욕 피해
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=151905].levelList[level=1].coinlist[#3].coindescs[#6].desc
   limit: do 120 znaków
   EN: - Take (20% of this Coin's final damage) Lust damage
   PL: - otrzymuje obrażenia Pożądania równe (20% końcowych obrażeń tej Monety)
319. [Umiejętność wroga [149501] (ulepszenie 1) — nazwa] 트리밍
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149501].levelList[level=1].name
   limit: do 40 znaków
   EN: Trimming
   PL: Trimming
320. [Umiejętność wroga [149501] (ulepszenie 1) — opis] [WhenUse]\n- 자신의 [ChargeKhaki] 횟수가 10 이상이면, 코인 위력 +1\n- [LargeTailoringShears]가 있으면, 피해량 +([LargeTailoringShears] 수치 x 10)% (최대 30%)\n[WhenUse] 자신의 [ChargeKhaki] 횟수가 15 미만이면, 자신의 [ChargeKhaki] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149501].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeKhaki], [LargeTailoringShears]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [LargeTailoringShears] = 꽃가위 / Blossom Scissors
   EN: [WhenUse]\n- At 10+ [ChargeKhaki] Count, Coin Power +1\n- If this unit has [LargeTailoringShears], deal +([LargeTailoringShears] Stack x 10)% damage (max 30%)\n[WhenUse] At fewer than 15 [ChargeKhaki] Count, gain +2 [ChargeKhaki] Count
   PL: [WhenUse]\n- przy 10+ Licznika [ChargeKhaki] Moc Monety +1\n- jeżeli ta jednostka ma [LargeTailoringShears], zadaje +(Wartość [LargeTailoringShears] x 10)% obrażeń (maks. 30%)\n[WhenUse] przy mniej niż 15 Licznika [ChargeKhaki] zyskuje 2 Licznika [ChargeKhaki]
321. [Umiejętność wroga [149501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 2 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 [Vibration] i zwiększa Licznik [Vibration] o 2
322. [Umiejętność wroga [149501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeKhaki] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeKhaki]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: [OnSucceedAttack] Gain +2 [ChargeKhaki] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeKhaki]
323. [Umiejętność wroga [149501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [ScissorsMark] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScissorsMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScissorsMark] = 마름질 표식 / Mark of Shearing
   EN: [OnSucceedAttack] Inflict 2 [ScissorsMark]
   PL: [OnSucceedAttack] nakłada 2 [ScissorsMark]
324. [Umiejętność wroga [149502] (ulepszenie 1) — nazwa] 커팅
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].name
   limit: do 40 znaków
   EN: Cutting
   PL: Cutting
325. [Umiejętność wroga [149502] (ulepszenie 1) — opis] [WhenUse]\n- [LargeTailoringShears]가 2 이상이면, 공격 가중치 +1\n- 자신의 [ChargeKhaki] 횟수가 10 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [ChargeKhaki] 횟수 4 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [LargeTailoringShears], [ChargeKhaki]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LargeTailoringShears] = 꽃가위 / Blossom Scissors; [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: [WhenUse]\n- At 2+ [LargeTailoringShears], gain +1 Atk Weight\n- At 10+ [ChargeKhaki] Count, Coin Power +1\n[WhenUse] Gain +4 [ChargeKhaki] Count
   PL: [WhenUse]\n- przy 2+ [LargeTailoringShears] Waga Ataku +1\n- przy 10+ Licznika [ChargeKhaki] Moc Monety +1\n[WhenUse] zyskuje 4 Licznika [ChargeKhaki]
326. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration] and +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 [Vibration] i zwiększa Licznik [Vibration] o 2
327. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeKhaki] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeKhaki]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: [OnSucceedAttack] Gain +3 [ChargeKhaki] Count
   PL: [OnSucceedAttack] zyskuje 3 Licznika [ChargeKhaki]
328. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [ScissorsMark] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 323 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [ScissorsMark] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScissorsMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScissorsMark] = 마름질 표식 / Mark of Shearing
   EN: [OnSucceedAttack] Inflict 3 [ScissorsMark]
   PL: [OnSucceedAttack] nakłada 3 [ScissorsMark]
331. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 3, efekt 3 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 다음 턴에 [FinishedFabric] 1 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [FinishedFabric]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [FinishedFabric] = 재단된 원단 / Cut Fabric
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] Gain 1 [FinishedFabric] next turn</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] zyskuje 1 [FinishedFabric] w następnej turze</u></b></mark></color>
332. [Umiejętność wroga [149502] (ulepszenie 1) — moneta 3, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeKhaki] 횟수가 12 이상이면, [ChargeKhaki] 횟수 4를 소모하여 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149502].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ChargeKhaki], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] At 12+ [ChargeKhaki] Count, consume 4 [ChargeKhaki] Count to trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [UnBrokenCoinOnSucceedAttack] przy 12+ Licznika [ChargeKhaki] zużywa 4 Licznika [ChargeKhaki], aby wywołać [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
333. [Umiejętność wroga [149503] (ulepszenie 1) — nazwa] 고정 그리고 패턴 따라 재단
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].name
   limit: do 50 znaków
   EN: Pin and Trim Along the Patterns
   PL: Pin and Trim Along the Patterns
334. [Umiejętność wroga [149503] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[WhenUse]\n- 자신의 [ChargeKhaki] 횟수가 10 이상이면, [ChargeKhaki] 횟수 10을 소모하여 코인 위력 +2\n· 자신의 남은 [ChargeKhaki] 횟수를 최대 20까지 소모하여, 소모한 수치 1당 피해량 +1% (최대 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- 자신의 [FinishedFabric] 3 감소\n- 피해량 -75%\n- [Paralysis] 4 얻음</u></b></mark></color>\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [ChargeKhaki], [DefeatDuel], [FinishedFabric], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [DefeatDuel] = [합 패배] / [Clash Lose]; [FinishedFabric] = 재단된 원단 / Cut Fabric; [Paralysis] = 마비 / Paralyze
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[WhenUse]\n- At 10+ [ChargeKhaki] Count, consume 10 [ChargeKhaki] Count to gain Coin Power +2\n- Consume up to 20 remaining [ChargeKhaki] Count to deal +1% damage for every Count consumed (max 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- Lose 3 [FinishedFabric]\n- Deal -75% damage\n- Gain 4 [Paralysis]</u></b></mark></color>\n- Damage dealt by this Skill cannot Stagger the target
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse]\n- przy 10+ Licznika [ChargeKhaki] zużywa 10 Licznika [ChargeKhaki], aby zyskać Moc Monety +2\n· zużywa do 20 pozostałych Liczników [ChargeKhaki], zadając +1% obrażeń za każde 1 zużytego Licznika (maks. 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- traci 3 [FinishedFabric]\n- zadaje -75% obrażeń\n- zyskuje 4 [Paralysis]</u></b></mark></color>\n- obrażenia z tej Umiejętności nie Oszołamiają celu
335. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeKhaki] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 327 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 4 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Vibration]
339. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Vibration]
341. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [ScissorsMark] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScissorsMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScissorsMark] = 마름질 표식 / Mark of Shearing
   EN: [OnSucceedAttack] Inflict 5 [ScissorsMark]
   PL: [OnSucceedAttack] nakłada 5 [ScissorsMark]
343. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 4, efekt 4 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 다음 턴에 [FinishedFabric] 3 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#3].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [UnBrokenCoinOnSucceedAttack], [FinishedFabric]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [FinishedFabric] = 재단된 원단 / Cut Fabric
   EN: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] Gain 3 [FinishedFabric] next turn</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] zyskuje 3 [FinishedFabric] w następnej turze</u></b></mark></color>
345. [Umiejętność wroga [149503] (ulepszenie 1) — moneta 4, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149503].levelList[level=1].coinlist[#3].coindescs[#4].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [149504] (ulepszenie 1) — nazwa] 쿠페 당 르 비에
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].name
   limit: do 40 znaków
   EN: Coupez dans le Biais
   PL: Coupez dans le Biais
347. [Umiejętność wroga [149504] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>속도에 상관없이 이 스킬과 합을 할 수 있음</u></b></mark></color>\n[WhenUse]\n- [LargeTailoringShears] 수치만큼 공격 가중치 증가 (최대 3)\n- 자신의 [ChargeKhaki] 횟수가 10 이상이면, [ChargeKhaki] 횟수 10을 소모하여 코인 위력 +2\n- 자신의 남은 [ChargeKhaki] 횟수를 최대 20까지 소모하여, 소모한 수치 1당 피해량 +1% (최대 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- 자신의 [FinishedFabric] 3 감소\n- 피해량 -90%\n- [Paralysis] 4 얻음</u></b></mark></color>\n- 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [LargeTailoringShears], [ChargeKhaki], [DefeatDuel], [FinishedFabric], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [LargeTailoringShears] = 꽃가위 / Blossom Scissors; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [DefeatDuel] = [합 패배] / [Clash Lose]; [FinishedFabric] = 재단된 원단 / Cut Fabric; [Paralysis] = 마비 / Paralyze
   EN: <color=#ff6000><mark=#ff000040><b><u>Can Clash with this Skill regardless of Speed</u></b></mark></color>\n[WhenUse]\n- Gain +([LargeTailoringShears] Stack) Atk Weight (max 3)\n- At 10+ [ChargeKhaki] Count, consume 10 [ChargeKhaki] Count to gain Coin Power +2\n- Consume up to 20 remaining [ChargeKhaki] Count to deal +1% damage for every Count consumed (max 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- Lose 3 [FinishedFabric]\n- Deal -90% damage\n- Gain 4 [Paralysis]</u></b></mark></color>\n- Damage dealt by this Skill cannot Stagger the target
   PL: <color=#ff6000><mark=#ff000040><b><u>może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości</u></b></mark></color>\n[WhenUse]\n- zyskuje +(Stosy [LargeTailoringShears]) Wagi Ataku (maks. 3)\n- przy 10+ Licznika [ChargeKhaki] zużywa 10 Licznika [ChargeKhaki], aby zyskać Moc Monety +2\n· zużywa do 20 pozostałych Liczników [ChargeKhaki], zadając +1% obrażeń za każde 1 zużytego Licznika (maks. 20%)\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel]\n- traci 3 [FinishedFabric]\n- zadaje -90% obrażeń\n- zyskuje 4 [Paralysis]</u></b></mark></color>\n- obrażenia z tej Umiejętności nie Oszołamiają celu
348. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이면, [ScissorsMark] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ScissorsMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScissorsMark] = 마름질 표식 / Mark of Shearing
   EN: [OnSucceedAttack] If it is the main target, inflict 5 [ScissorsMark]
   PL: [OnSucceedAttack] jeżeli to główny cel, nakłada 5 [ScissorsMark]
356. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
357. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 4, efekt 4 — opis] <color=#ff6000><mark=#ff000040><b><u>[UnBrokenCoinOnSucceedAttack] 다음 턴에 [FinishedFabric] 1 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#3].coindescs[#3].desc
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność wroga [149504] (ulepszenie 1) — moneta 4, efekt 5 — opis] [UnBrokenCoinOnSucceedAttack] 메인 타겟이면 [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149504].levelList[level=1].coinlist[#3].coindescs[#4].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] If it is the main target, trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [UnBrokenCoinOnSucceedAttack] jeżeli to główny cel, wywołuje [VibrationExplosion] 2 razy, po czym zmniejsza Licznik [Vibration] celu o 2
359. [Umiejętność wroga [149505] (ulepszenie 1) — nazwa] 패턴 따기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149505].levelList[level=1].name
   limit: do 40 znaków
   EN: Patterning
   PL: Patterning
360. [Umiejętność wroga [149505] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\n[TailoringTarget]을 타겟함</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149505].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [TailoringTarget]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [TailoringTarget] = 수선 대상 / Alteration Target
   EN: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\nTargets [TailoringTarget]</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\nceluje w [TailoringTarget]</u></b></mark></color>
361. [Umiejętność wroga [149505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Umiejętność wroga [149505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Umiejętność wroga [149505] (ulepszenie 1) — moneta 2, efekt 2 — opis] <color=#ff6000><mark=#ff000040><b><u>[OnSucceedAttack] [ScissorsMark] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149505].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [ScissorsMark]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ScissorsMark] = 마름질 표식 / Mark of Shearing
   EN: <color=#ff6000><mark=#ff000040><b><u>[OnSucceedAttack] Inflict 9 [ScissorsMark]</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[OnSucceedAttack] nakłada 9 [ScissorsMark]</u></b></mark></color>
364. [Umiejętność wroga [149506] (ulepszenie 1) — nazwa] 쉬르필 아 라 셴
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].name
   limit: do 40 znaków
   EN: Surfile à la Chaîne
   PL: Surfile à la Chaîne
365. [Umiejętność wroga [149506] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\n[TailoringTarget]을 타겟함</u></b></mark></color>\n자신의 [LargeTailoringShears] 1당,\n최종 위력 +1, 피해량  +20% (각각 최대 3, 60%)\n자신의 [ChargeKhaki] 위력 1당,\n피해량 +4% (최대 20%)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] 대상 수감자가 수비 스킬을\n- 장착했으면, [Paralysis] 4 얻고 이 스킬의 피해로 대상이 흐트러지지 않음\n- 장착하지 않았으면, 다음 턴에 [FinishedFabric] 10 얻음</u></b></mark></color>\n[EndSkill]\n- <color=#ff6000><mark=#ff000040><b><u>합을 진행했으면,</u></b></mark></color> 해당 수감자 스킬의 최종 합 위력 수치의 절반만큼 대상에게 [DamagedFabric] 부여 (최대 20)\n<color=#ff6000><mark=#ff000040><b><u>- 대상의 [ScissorsMark] 전부 소모</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[EndBattle] 다음 턴에 [LargeTailoringShears] 1 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [TailoringTarget], [LargeTailoringShears], [ChargeKhaki], [WhenUse], [Paralysis], [FinishedFabric], [EndSkill], [DamagedFabric], [ScissorsMark], [EndBattle]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [TailoringTarget] = 수선 대상 / Alteration Target; [LargeTailoringShears] = 꽃가위 / Blossom Scissors; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [WhenUse] = [사용시] / [On Use]; [Paralysis] = 마비 / Paralyze; [FinishedFabric] = 재단된 원단 / Cut Fabric; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\nTargets [TailoringTarget]</u></b></mark></color>\nFinal Power +1 and deal +20% damage for every [LargeTailoringShears] on self (max 3, 60 respectively)\nDeal +4% damage for every [ChargeKhaki] Potency (max 20%)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] If the targeted Sinner...\n- ... has equipped Defense Skills, gain 4 [Paralysis]; damage dealt by this Skill cannot Stagger the target\n- ... has not equipped Defense Skills, gain 10 [FinishedFabric] next turn</u></b></mark></color>\n[EndSkill]\n- <color=#ff6000><mark=#ff000040><b><u>After a Clash,</u></b></mark></color> inflict (Clashing Sinner's final Clash Power / 2) [DamagedFabric] on target (max 20)\n<color=#ff6000><mark=#ff000040><b><u>- Consume all [ScissorsMark] on target</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[EndBattle] Gain 1 [LargeTailoringShears] next turn</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]\nceluje w [TailoringTarget]</u></b></mark></color>\nMoc Końcowa +1 i zadaje +20% obrażeń za każde 1 [LargeTailoringShears] tej jednostki (maks. 3, maks. 60%)\nzadaje +4% obrażeń za każde 1 Siły [ChargeKhaki] tej jednostki (maks. 20%)\n<color=#ff6000><mark=#ff000040><b><u>[WhenUse] jeżeli wskazany Grzesznik...\n- ... ma założoną Umiejętność obrony, zyskuje 4 [Paralysis], a obrażenia z tej Umiejętności nie Oszołamiają celu\n- ... nie ma założonej Umiejętności obrony, zyskuje 10 [FinishedFabric] w następnej turze</u></b></mark></color>\n[EndSkill]\n- <color=#ff6000><mark=#ff000040><b><u>jeżeli stoczono Starcie,</u></b></mark></color> nakłada na cel (końcowa Moc Starcia Grzesznika staczającego Starcie / 2) [DamagedFabric] (maks. 20)\n<color=#ff6000><mark=#ff000040><b><u>- zużywa wszystkie [ScissorsMark] celu</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>[EndBattle] zyskuje 1 [LargeTailoringShears] w następnej turze</u></b></mark></color>
366. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL: [OnSucceedAttack] nakłada 3 [Vibration]
370. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion] 1회. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Umiejętność wroga [149506] (ulepszenie 1) — moneta 4, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149506].levelList[level=1].coinlist[#3].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 2 times; then, reduce target's [Vibration] Count by 2
   PL: [UnBrokenCoinOnSucceedAttack] wywołuje [VibrationExplosion] 2 razy, po czym zmniejsza Licznik [Vibration] celu o 2
374. [Umiejętność wroga [150601] (ulepszenie 1) — nazwa] 못 박히라
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].name
   limit: do 40 znaków
   EN: Cometh the Nail
   PL: Cometh the Nail
375. [Umiejętność wroga [150601] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 위력 3당 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] Coin Power +1 for every 3 [ChargeNoir] Potency on self (max 3)
   PL: [WhenUse] Moc Monety +1 za każde 3 Siły [ChargeNoir] tej jednostki (maks. 3)
376. [Umiejętność wroga [150601] (ulepszenie 1) — tekst klimatyczny] 못은 망치로 박히기 위해 존재한다. 망치가 박는 것은 못이다.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nails exist to be driven in by hammers.\nWhat the hammer falls upon are nails.
   PL: Gwoździe istnieją po to, by wbijał je młot.\nTo, co wbija młot, to gwoździe.
377. [Umiejętność wroga [150601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 5 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +5 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 5 Licznika [ChargeNoir]
378. [Umiejętność wroga [150601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 3 Licznika [Vibration]
379. [Umiejętność wroga [150601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 5 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Umiejętność wroga [150601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Umiejętność wroga [150601] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150601].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirNail] = 약속된 못 / Promised Nail
   EN: [OnSucceedAttack] Inflict 1 [NoirNail]
   PL: [OnSucceedAttack] nakłada 1 [NoirNail]
382. [Umiejętność wroga [150602] (ulepszenie 1) — nazwa] 못 생기라
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].name
   limit: do 40 znaków
   EN: Summoneth the Nail
   PL: Summoneth the Nail
383. [Umiejętność wroga [150602] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 위력 3당 코인 위력 +1 (최대 3)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 3 [ChargeNoir] Potency on self (max 3)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Monety +1 za każde 3 Siły [ChargeNoir] tej jednostki (maks. 3)\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
384. [Umiejętność wroga [150602] (ulepszenie 1) — tekst klimatyczny] 망치가 휘둘러진 곳에 못은 존재한다.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Where hammers have fallen, nails exist.
   PL: Tam, gdzie upadły młoty, istnieją gwoździe.
385. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Umiejętność wroga [150602] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150602].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Umiejętność wroga [150603] (ulepszenie 1) — nazwa] 두드림
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150603].levelList[level=1].name
   limit: do 40 znaków
   EN: Rapping
   PL: Rapping
395. [Umiejętność wroga [150603] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 위력 3당 코인 위력 +1 (최대 3)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150603].levelList[level=1].desc
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Umiejętność wroga [150603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Umiejętność wroga [150603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Umiejętność wroga [150603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Umiejętność wroga [150604] (ulepszenie 1) — nazwa] 묵시
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150604].levelList[level=1].name
   limit: do 40 znaków
   EN: Witness Ye in Silence
   PL: Witness Ye in Silence
400. [Umiejętność wroga [150604] (ulepszenie 1) — opis] [WinDuel] 대상의 [Vibration] 횟수 3 증가\n[WinDuel] [VibrationExplosion]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150604].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WinDuel], [Vibration], [VibrationExplosion]
   znaczenie tagów: [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [WinDuel] Inflict +3 [Vibration] Count\n[WinDuel] [VibrationExplosion]
   PL: [WinDuel] nakłada 3 Licznika [Vibration]\n[WinDuel] [VibrationExplosion]
401. [Umiejętność wroga [150604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Umiejętność wroga [150604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable]
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable]
403. [Umiejętność wroga [150604] (ulepszenie 1) — moneta 1, efekt 3 — opis] <color=#ff6000><mark=#ff000040><b><u>[DefeatDuelAttack] [NoirShieldPiece] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [DefeatDuelAttack], [NoirShieldPiece]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance
   EN: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuelAttack] Inflict 1 [NoirShieldPiece]</u></b></mark></color>
   PL: <color=#ff6000><mark=#ff000040><b><u>[DefeatDuelAttack] nakłada 1 [NoirShieldPiece]</u></b></mark></color>
404. [Umiejętność wroga [150605] (ulepszenie 1) — nazwa] 보존 신역 선포
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].name
   limit: do 60 znaków
   EN: Proclamation: Sanctum of Conservation
   PL: Proclamation: Sanctum of Conservation
405. [Umiejętność wroga [150605] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음. 이 스킬을 사용하기 전까지 흐트러지지 않음\n\n[StartBattle] 적이 장착한 수비 스킬 1개당 합 위력 -2 (최대 -10)\n\n[WhenUse] 메인 타겟이 <color=#ff6000><mark=#ff000040><b><u>[NoirShieldPiece]이 없으면, 이 스킬 최종 위력 +5</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir] 횟수를 모두 소모\n- 소모값 3당 최종 위력 +1\n- 피해량 +(소모값 x5)%\n<color=#ff6000><mark=#ff000040><b><u>- [NoirField] 1 얻음</u></b></mark></color>\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [WhenUse], [NoirShieldPiece], [ChargeNoir], [NoirField], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance; [ChargeNoir] = 보존 / Preservation; [NoirField] = 보존 신역 / Sanctum of Conservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Can Clash with this Skill regardless of Speed; cannot be Staggered before using this Skill\n\n[StartBattle] Clash Power -2 for every Defense Skill equipped by enemies (-10 max)\n\n[WhenUse] If the main target <color=#ff6000><mark=#ff000040><b><u>does not have [NoirShieldPiece], Final Power +5 for this Skill</u></b></mark></color>\n[WhenUse] Consume all [ChargeNoir] Count on self\n- Final Power +1 for every 3 [ChargeNoir] Count consumed\n- Deal +([ChargeNoir] Count consumed x 5)% damage\n<color=#ff6000><mark=#ff000040><b><u>- Gain 1 [NoirField]</u></b></mark></color>\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n\n[StartBattle] Moc Starcia -2 za każdą założoną wrogom Umiejętność obrony (maks. -10)\n\n[WhenUse] jeżeli główny cel <color=#ff6000><mark=#ff000040><b><u>nie ma [NoirShieldPiece], Moc Końcowa tej Umiejętności +5</u></b></mark></color>\n[WhenUse] zużywa wszystkie Liczniki [ChargeNoir] tej jednostki\n- Moc Końcowa +1 za każde 3 zużytego Licznika [ChargeNoir]\n- zadaje +(zużyte Liczniki [ChargeNoir] x 5)% obrażeń\n<color=#ff6000><mark=#ff000040><b><u>- zyskuje 1 [NoirField]</u></b></mark></color>\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
406. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 [NoirShieldPiece]을 보유한 상태면,
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirShieldPiece]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance
   EN: [OnSucceedAttack] If target has [NoirShieldPiece]:
   PL: [OnSucceedAttack] jeżeli cel ma [NoirShieldPiece]:
408. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 3 — opis] - 이 코인으로 받는 최종 피해량 -95%
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   EN: - Target takes -95% final damage from this Coin
   PL: - cel otrzymuje -95% końcowych obrażeń od tej Monety
409. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 4 — opis] - 이 코인 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   EN: - This Coin's damage cannot Stagger the target
   PL: - obrażenia tej Monety nie Oszołamiają celu
410. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 5 — opis] - 대상의 [NoirShieldPiece]을 제거하고, [VibrationResonance] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#4].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NoirShieldPiece], [VibrationResonance]
   znaczenie tagów: [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance; [VibrationResonance] = 보존 상쇄 / Negation of Conservation
   EN: - Remove [NoirShieldPiece] on target and apply 2 [VibrationResonance]
   PL: - usuwa [NoirShieldPiece] celu i nakłada 2 [VibrationResonance]
411. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#5].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL: [OnSucceedAttack] nakłada 5 [Vibration]
412. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 7 — opis] [OnSucceedAttack] [VibrationExplosion] 3회. 대상의 [Vibration] 횟수 3 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#6].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 3 times; then, reduce target's [Vibration] Count by 3
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion] 3 razy, po czym zmniejsza Licznik [Vibration] celu o 3
413. [Umiejętność wroga [150605] (ulepszenie 1) — moneta 1, efekt 8 — opis] [OnSucceedAttack] 이 코인 최종 피해량만큼 흐트러짐 손상
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150605].levelList[level=1].coinlist[#0].coindescs[#7].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold equal to this Coin's final damage
   PL: [OnSucceedAttack] podnosi Próg Oszołomienia o wartość końcowych obrażeń tej Monety
414. [Umiejętność wroga [150606] (ulepszenie 1) — nazwa] 계시
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150606].levelList[level=1].name
   limit: do 40 znaków
   EN: Revelations
   PL: Revelations
415. [Umiejętność wroga [150606] (ulepszenie 1) — opis] 이 스킬을 사용하기 전까지 흐트러지지 않음\n<color=#ff6000><mark=#ff000040><b><u>[StartBattle] [NoirShieldUp] 999 얻음</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150606].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [NoirShieldUp]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [NoirShieldUp] = 검은 신의 가호 / Blessing of the Obsidian God
   EN: Cannot be Staggered before using this Skill\n<color=#ff6000><mark=#ff000040><b><u>[StartBattle] Gain 999 [NoirShieldUp]</u></b></mark></color>
   PL: nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n<color=#ff6000><mark=#ff000040><b><u>[StartBattle] zyskuje 999 [NoirShieldUp]</u></b></mark></color>
416. [Umiejętność wroga [150607] (ulepszenie 1) — nazwa] 언약
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150607].levelList[level=1].name
   limit: do 40 znaków
   EN: Covenant
   PL: Covenant
417. [Umiejętność wroga [150607] (ulepszenie 1) — opis] [SupportEnemy]\n\n[EndSkill] 대상이 아군이면, [AttackUp] 6 부여\n[EndSkill] 대상 아군이 무작위 공격 스킬 발동\n\n[DefeatDuel] [Vulnerable] 1 얻음\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] 자신의 [NoirShieldUp] 150 감소</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150607].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SupportEnemy], [EndSkill], [AttackUp], [DefeatDuel], [Vulnerable], [NoirShieldUp]
   znaczenie tagów: [SupportEnemy] = 양극성 / Duality; [EndSkill] = [공격 종료시] / [Attack End]; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [NoirShieldUp] = 검은 신의 가호 / Blessing of the Obsidian God
   EN: [SupportEnemy]\n\n[EndSkill] If target is an ally, apply 6 [AttackUp]\n[EndSkill] Targeted ally uses a random Attack Skill\n\n[DefeatDuel] Gain 1 [Vulnerable]\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] Lose 150 [NoirShieldUp]</u></b></mark></color>
   PL: [SupportEnemy]\n\n[EndSkill] jeżeli cel jest sojusznikiem, nakłada 6 [AttackUp]\n[EndSkill] wskazany sojusznik używa losowej Umiejętności ataku\n\n[DefeatDuel] zyskuje 1 [Vulnerable]\n<color=#ff6000><mark=#ff000040><b><u>[DefeatDuel] traci 150 [NoirShieldUp]</u></b></mark></color>
418. [Umiejętność wroga [150608] (ulepszenie 1) — nazwa] 탄생을 끊으리라.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].name
   limit: do 40 znaków
   EN: I sever thine advent.
   PL: I sever thine advent.
419. [Umiejętność wroga [150608] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음. 이 스킬을 사용하기 전까지 흐트러지지 않음\n[WhenUse] 자신의 [NoirShieldUp] 100당 최종 위력 +1\n[WhenUse] 대상이 [NoirShieldPiece]을 보유하고 있으면, 합 위력 -5\n[DefeatDuel] 이 스킬 피해량 -80%, 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NoirShieldUp], [NoirShieldPiece], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NoirShieldUp] = 검은 신의 가호 / Blessing of the Obsidian God; [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed; Cannot be Staggered before using this Skill\n[WhenUse] Final Power +1 for every 100 [NoirShieldUp] on self\n[WhenUse] If target has [NoirShieldPiece], Clash Power -5\n[DefeatDuel] This Skill deals -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] End this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[WhenUse] Moc Końcowa +1 za każde 100 [NoirShieldUp] tej jednostki\n[WhenUse] jeżeli cel ma [NoirShieldPiece], Moc Starcia -5\n[DefeatDuel] ta Umiejętność zadaje -80% obrażeń, a jej obrażenia nie Oszołamiają celu\n[EndSkill] kończy tę turę
420. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [NoirNail] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [NoirNail]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [NoirNail] = 약속된 못 / Promised Nail
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [NoirNail]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [NoirNail]
424. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [NoirShieldUp] 200당 [VibrationExplosion] 1회 추가 (최대 4회)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NoirShieldUp], [VibrationExplosion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NoirShieldUp] = 검은 신의 가호 / Blessing of the Obsidian God; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] 1 additional time for every 200 [NoirShieldUp] on self (4 times max)
   PL: [OnSucceedAttack] wywołuje dodatkowo [VibrationExplosion] 1 raz za każde 200 [NoirShieldUp] tej jednostki (maks. 4 razy)
427. [Umiejętność wroga [150608] (ulepszenie 1) — moneta 2, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 3회.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150608].levelList[level=1].coinlist[#1].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [VibrationExplosion]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: [UnBrokenCoinOnSucceedAttack] Trigger [VibrationExplosion] 3 times
   PL: [UnBrokenCoinOnSucceedAttack] wywołuje [VibrationExplosion] 3 razy
428. [Umiejętność wroga [150609] (ulepszenie 1) — nazwa] 거듭 내리쳐, 탄생을 끊으리라!
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].name
   limit: do 60 znaków
   EN: With each smite, I sever thine advent!
   PL: With each smite, I sever thine advent!
429. [Umiejętność wroga [150609] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음. 이 스킬을 사용하기 전까지 흐트러지지 않음\n\n[WhenUse] 자신의 [ChargeNoir] 횟수를 모두 소모\n- 소모값 3당 최종 위력 +1\n- 피해량 +(소모값 x5)%\n\n[WhenUse] 메인 타겟이 [NoirShieldPiece]을 보유하고 있으면, 합 위력 -5\n[WhenUse] 메인 타겟이 [NoirShieldPiece]이 없으면, 이 스킬 최종 위력 +5\n[DefeatDuel] 이 스킬 피해량 -80%, 이 스킬 피해로 대상이 흐트러지지 않음\n[EndSkill] 이번 턴 종료
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [NoirShieldPiece], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [NoirShieldPiece] = 묵시적 형벌 / Apocalyptic Vengeance; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Can Clash with this Skill regardless of Speed; Cannot be Staggered before using this Skill\n\n[WhenUse] Consume all [ChargeNoir] Count on self\n- Final Power -1 for every 3 [ChargeNoir] Count consumed\n- Deal +([ChargeNoir] Count consumed x 5)% damage\n\n[WhenUse] If the main target has [NoirShieldPiece], Clash Power -5\n[WhenUse] If the main target does not have [NoirShieldPiece], Final Power +5 for this Skill\n[DefeatDuel] This Skill deals -80% damage and damage dealt by this Skill cannot Stagger the target\n[EndSkill] End this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości; nie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n\n[WhenUse] zużywa wszystkie Liczniki [ChargeNoir] tej jednostki\n- Moc Końcowa -1 za każde 3 zużytego Licznika [ChargeNoir]\n- zadaje +(zużyte Liczniki [ChargeNoir] x 5)% obrażeń\n\n[WhenUse] jeżeli główny cel ma [NoirShieldPiece], Moc Starcia -5\n[WhenUse] jeżeli główny cel nie ma [NoirShieldPiece], Moc Końcowa tej Umiejętności +5\n[DefeatDuel] ta Umiejętność zadaje -80% obrażeń, a jej obrażenia nie Oszołamiają celu\n[EndSkill] kończy tę turę
430. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NoirNail] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 1, efekt 4 — opis] [UnBrokenCoinOnSucceedAttack] [NoirNail] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 [NoirShieldPiece]을 보유한 상태면,
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 3 — opis] - 이 코인으로 받는 최종 피해량 -95%
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 4 — opis] - 이 코인 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 5 — opis] - 대상의 [NoirShieldPiece]을 제거하고, [VibrationResonance] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#4].desc
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 6 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#5].desc
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Umiejętność wroga [150609] (ulepszenie 1) — moneta 2, efekt 7 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150609].levelList[level=1].coinlist[#1].coindescs[#6].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Umiejętność wroga [150610] (ulepszenie 1) — nazwa] 신도들은 부름에 답하라
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150610].levelList[level=1].name
   limit: do 40 znaków
   EN: Heed the calling, O faithful
   PL: Heed the calling, O faithful
442. [Umiejętność wroga [150610] (ulepszenie 1) — opis] [StartBattle] 다음 턴에 르누아르 아군 5명 소환 (자신을 제외한 전장의 아군 수는 5명을 초과할 수 없음)\n[DefeatDuel] 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150610].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [StartBattle] Summon 5 Le Noir allies next turn (the number of other allies on the field cannot exceed 5)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: [StartBattle] przywołuje w następnej turze 5 sojuszników Le Noir (łączna liczba pozostałych sojuszników na polu nie może przekroczyć 5)\n[DefeatDuel] zadaje -80% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
443. [Umiejętność wroga [150610] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150610].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Umiejętność wroga [150610] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150610].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Umiejętność wroga [150401] (ulepszenie 1) — nazwa] 구매 이력은?
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150401].levelList[level=1].name
   limit: do 50 znaków
   EN: Your purchase history, please?
   PL: Your purchase history, please?
446. [Umiejętność wroga [150401] (ulepszenie 1) — opis] 피해량 +(자신의 보호막 수치)% (최대 20%)\n[WhenUse] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150401].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: Deal +(Shield on self)% damage (max 20%)\n[WhenUse] Gain +2 [ChargeNoir] Count
   PL: zadaje +(wartość Tarczy tej jednostki)% obrażeń (maks. 20%)\n[WhenUse] zyskuje 2 Licznika [ChargeNoir]
447. [Umiejętność wroga [150401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Gain +2 [ChargeNoir] Count
   PL: [OnSucceedAttack] zyskuje 2 Licznika [ChargeNoir]
448. [Umiejętność wroga [150401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Umiejętność wroga [150402] (ulepszenie 1) — nazwa] 구매 자격은?
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].name
   limit: do 50 znaków
   EN: Your purchasing rights, please?
   PL: Your purchasing rights, please?
450. [Umiejętność wroga [150402] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수와 대상의 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoir] 횟수 3 증가\n[WinDuel] 자신의 [ChargeNoir] 횟수 2 증가\n[WhenUse] 자신의 [ChargeNoir] 위력이 3 이상이면, 마지막 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [Vibration], [WinDuel], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Vibration] = 진동 / Tremor; [WinDuel] = [합 승리시] / [Clash Win]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [WhenUse] Coin Power +1 for every 6 ([ChargeNoir] Count on self + [Vibration] Potency on target) (max 2)\n[WhenUse] Gain +3 [ChargeNoir] Count\n[WinDuel] Gain +2 [ChargeNoir] Count\n[WhenUse] At 3+ [ChargeNoir] Potency, convert the final coin to [SuperCoin]
   PL: [WhenUse] Moc Monety +1 za każde 6 (Licznik [ChargeNoir] tej jednostki + Siła [Vibration] celu) (maks. 2)\n[WhenUse] zyskuje 3 Licznika [ChargeNoir]\n[WinDuel] zyskuje 2 Licznika [ChargeNoir]\n[WhenUse] przy 3+ Siły [ChargeNoir] ostatnia Moneta zamienia się w [SuperCoin]
451. [Umiejętność wroga [150402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Umiejętność wroga [150402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Umiejętność wroga [150402] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Umiejętność wroga [150402] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150402].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność wroga [150403] (ulepszenie 1) — nazwa] 스탬핑[플라넬]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamping [Flannel]
   PL: Stamping [Flannel]
456. [Umiejętność wroga [150403] (ulepszenie 1) — opis] 피해량 +(자신의 보호막 수치)% (최대 50%)\n[WhenUse] 대상의 [Vibration] 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoir] 횟수를 최대 15 소모하고,\n최대 체력의 (소모한 [ChargeNoir] 횟수x2)% 만큼 다음 턴까지 유지되는 보호막 얻음\n[WhenUse] 자신의 [ChargeNoir] 횟수를 10 이상 소모하였다면, 코인 위력 +2, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Deal +(Shield on self)% damage (max 50%)\n[WhenUse] Final Power +1 for every 6 [Vibration] on target (max 2)\n[WhenUse] Consume up to 15 [ChargeNoir] Count on self, and gain Shield equal to ([ChargeNoir] Count consumed x 2)% of this unit's max HP; Shield gained due to this effect lasts until next turn\n[WhenUse] If this unit has consumed 10+ [ChargeNoir] Count, Coin Power +2 and convert all Coins to [SuperCoin]s
   PL: zadaje +(wartość Tarczy tej jednostki)% obrażeń (maks. 50%)\n[WhenUse] Moc Końcowa +1 za każde 6 [Vibration] celu (maks. 2)\n[WhenUse] zużywa do 15 Liczników [ChargeNoir] tej jednostki i zyskuje Tarczę równą (zużyte Liczniki [ChargeNoir] x 2)% Maks. HP tej jednostki; Tarcza zyskana tym efektem utrzymuje się do następnej tury\n[WhenUse] jeżeli zużyto 10+ Licznika [ChargeNoir], Moc Monety +2, a wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y
457. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeNoir] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ChargeNoir] = 보존 / Preservation
   EN: [UnBrokenCoinOnSucceedAttack] Gain +3 [ChargeNoir] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 3 Licznika [ChargeNoir]
459. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Vibration]
460. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ChargeNoir]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ChargeNoir] = 보존 / Preservation
   EN: [UnBrokenCoinOnSucceedAttack] Gain +2 [ChargeNoir] Count
   PL: [UnBrokenCoinOnSucceedAttack] zyskuje 2 Licznika [ChargeNoir]
461. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationCollapse], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] Trigger [Switch_Vibration] into [VibrationCollapse]
   PL: [OnSucceedAttack] uruchamia [Switch_Vibration] zamieniający [Vibration] tej jednostki na [VibrationCollapse]
462. [Umiejętność wroga [150403] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소\n- 자신의 [ChargeNoir] 위력 2당, 효과 1회 추가 (최대 2회)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150403].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [VibrationExplosion], [Vibration], [ChargeNoir]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1\n- Trigger an additional time for every 2 [ChargeNoir] Potency on self (max 2)
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] o 1\n- wywołuje dodatkowo 1 raz za każde 2 Siły [ChargeNoir] tej jednostki (maks. 2 razy)
463. [Umiejętność wroga [150404] (ulepszenie 1) — nazwa] 원단 강화
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150404].levelList[level=1].name
   limit: do 40 znaków
   EN: Reinforce Fabric
   PL: Reinforce Fabric
464. [Umiejętność wroga [150404] (ulepszenie 1) — opis] 아군에게 사용. 아군에게 피해량 0으로 고정\n[WhenUse] 대상의 [Vibration] 4당, 최종 위력 +2 (최대 6)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150404].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: This Skill is used on allies; damage dealt to allies is fixed to 0\n[WhenUse] Final Power +2 for every 4 [Vibration] on target (max 6)
   PL: ta Umiejętność jest używana na sojusznikach; obrażenia zadawane sojusznikom są ustalone na 0\n[WhenUse] Moc Końcowa +2 za każde 4 [Vibration] celu (maks. 6)
465. [Umiejętność wroga [150404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [DefenseUp] 3 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 3 [DefenseUp] this turn and next turn
   PL: [OnSucceedAttack] zyskuje 3 [DefenseUp] w tej i w następnej turze
466. [Umiejętność wroga [150404] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수만큼 대상의 [Charge] 횟수 증가\n- 대상의 [Charge] 횟수가 최댓값에 도달했으면, 다음 턴에 [DefenseUp] 3, [NoirBindArmor] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150404].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [ChargeNoir], [Charge], [DefenseUp], [NoirBindArmor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [Charge] = 충전 / Charge; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: [OnSucceedAttack] Target gains [Charge] Count equal to [ChargeNoir] Count on self\n- If target's [Charge] Count is at max, apply 3 [DefenseUp] and 5 [NoirBindArmor] next turn
   PL: [OnSucceedAttack] cel zyskuje Liczniki [Charge] równe Licznikowi [ChargeNoir] tej jednostki\n- jeżeli Licznik [Charge] celu osiągnął maksimum, nakłada w następnej turze 3 [DefenseUp] i 5 [NoirBindArmor]
467. [Umiejętność wroga [150405] (ulepszenie 1) — nazwa] 보존을 위하여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150405].levelList[level=1].name
   limit: do 40 znaków
   EN: For Conservation
   PL: For Conservation
468. [Umiejętność wroga [150405] (ulepszenie 1) — opis] 아군에게 사용. 아군에게 피해량 0으로 고정\n[WhenUse] 대상의 [Vibration] 4당, 최종 위력 +2 (최대 6)\n[WhenUse] 자신의 [ChargeNoir] 위력이 3 이상이면, 모든 코인이 [SuperCoin]으로 변경됨\n[WhenUse] 자신의 [ChargeNoir] 횟수가 10 미만이면, [ChargeNoir] 횟수를 10이 되도록 얻고, 얻은 수치 2당 [Vulnerable] 1 얻음\n[DefeatDuel] 자신 [ChargeNoir] 횟수 절반 소모\n[EndSkill] 자신의 [ChargeNoir] 횟수 모두 소모
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150405].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [ChargeNoir], [SuperCoin], [Vulnerable], [DefeatDuel], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [ChargeNoir] = 보존 / Preservation; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [Vulnerable] = 취약 / Fragile; [DefeatDuel] = [합 패배] / [Clash Lose]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: This Skill is used on allies; damage dealt to allies is fixed to 0\n[WhenUse] Final Power +2 for every 4 [Vibration] on target (max 6)\n[WhenUse] At 3+ [ChargeNoir] Potency, convert all Coins to [SuperCoin]s\n[WhenUse] At fewer than 10 [ChargeNoir] Count, gain up to 10 [ChargeNoir] Count; then, gain 1 [Vulnerable] for every 2 Count gained\n[DefeatDuel] Consume half of [ChargeNoir] Count on self\n[EndSkill] Consume all [ChargeNoir] Count on self
   PL: ta Umiejętność jest używana na sojusznikach; obrażenia zadawane sojusznikom są ustalone na 0\n[WhenUse] Moc Końcowa +2 za każde 4 [Vibration] celu (maks. 6)\n[WhenUse] przy 3+ Siły [ChargeNoir] wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y\n[WhenUse] przy mniej niż 10 Licznika [ChargeNoir] zyskuje Liczniki [ChargeNoir] do 10, a następnie zyskuje 1 [Vulnerable] za każde 2 zyskanych Liczników\n[DefeatDuel] zużywa połowę Liczników [ChargeNoir] tej jednostki\n[EndSkill] zużywa wszystkie Liczniki [ChargeNoir] tej jednostki
469. [Umiejętność wroga [150405] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 이번 턴과 다음 턴에 [DefenseUp] 2 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150405].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Gain 2 [DefenseUp] this turn and next turn
   PL: [OnSucceedAttack] zyskuje 2 [DefenseUp] w tej i w następnej turze
470. [Umiejętność wroga [150405] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수만큼 대상의 [Charge] 횟수 증가\n- 대상의 [ChargeNoir] 횟수가 최댓값에 도달했으면, 다음 턴에 [DefenseUp] 3, [NoirBindArmor] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150405].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [ChargeNoir], [Charge], [DefenseUp], [NoirBindArmor]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [Charge] = 충전 / Charge; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: [OnSucceedAttack] Target gains [Charge] Count equal to [ChargeNoir] Count on self\n- If target's [ChargeNoir] Count is at max, apply 3 [DefenseUp] and 5 [NoirBindArmor] next turn
   PL: [OnSucceedAttack] cel zyskuje Liczniki [Charge] równe Licznikowi [ChargeNoir] tej jednostki\n- jeżeli Licznik [ChargeNoir] celu osiągnął maksimum, nakłada w następnej turze 3 [DefenseUp] i 5 [NoirBindArmor]
471. [Umiejętność wroga [150501] (ulepszenie 1) — nazwa] 당신 가격은?
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150501].levelList[level=1].name
   limit: do 40 znaków
   EN: Your price range, please?
   PL: Your price range, please?
472. [Umiejętność wroga [150501] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeNoir]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation
   EN: [WhenUse] Gain +2 [ChargeNoir] Count
   PL: [WhenUse] zyskuje 2 Licznika [ChargeNoir]
473. [Umiejętność wroga [150501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność wroga [150501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność wroga [150502] (ulepszenie 1) — nazwa] 하자 투성이군
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].name
   limit: do 50 znaków
   EN: Disqualifying defects, all over
   PL: Disqualifying defects, all over
476. [Umiejętność wroga [150502] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수와 대상의 [Vibration]의 합 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoir] 횟수 3 증가\n[WinDuel] 자신의 [ChargeNoir] 횟수 2 증가\n[WhenUse] 자신의 [ChargeNoir] 위력이 3 이상이면, 마지막 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Umiejętność wroga [150502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신의 [ChargeNoir] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność wroga [150502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność wroga [150502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność wroga [150502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność wroga [150503] (ulepszenie 1) — nazwa] 스탬핑[펠트]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamping [Felt]
   PL: Stamping [Felt]
482. [Umiejętność wroga [150503] (ulepszenie 1) — opis] 피해량 +(자신의 보호막 수치)% (최대 50%)\n[WhenUse] 대상의 [Vibration] 6당, 최종 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeNoir] 횟수를 최대 15 소모하고,\n최대 체력의 (소모한 [ChargeNoir] 횟수x2)% 만큼 다음 턴까지 유지되는 보호막 얻음\n[WhenUse] 자신의 [ChargeNoir] 횟수를 10 이상 소모하였다면, 코인 위력 +2, 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [Vibration]
485. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [VibrationCollapse]로 [Switch_Vibration]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [ChargeNoir] 횟수를 10 이상 소모하였다면, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeNoir], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeNoir] = 보존 / Preservation; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] If this unit has consumed 10+ [ChargeNoir] Count, trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] jeżeli ta jednostka zużyła 10+ Licznika [ChargeNoir], wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] celu o 1
489. [Umiejętność wroga [150503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Umiejętność wroga [150504] (ulepszenie 1) — nazwa] 스탬핑[반향]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150504].levelList[level=1].name
   limit: do 40 znaków
   EN: Stamping [Reverb]
   PL: Stamping [Reverb]
491. [Umiejętność wroga [150504] (ulepszenie 1) — opis] 보호막이 있는 동안 적에게 피격 시 (자신의 [ChargeNoir] 위력 x [NoirBindArmor] 수치)만큼 적에게 피해를 입힘\n[WhenUse] [ChargeNoir] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=150504].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor], [WhenUse]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted; [WhenUse] = [사용시] / [On Use]
   EN: When hit while this unit has Shield, deal ([ChargeNoir] Potency on self x [NoirBindArmor] Stack) damage on the attacker\n[WhenUse] Gain +3 [ChargeNoir] Count
   PL: przy trafieniu, gdy ta jednostka ma Tarczę, zadaje atakującemu (Siła [ChargeNoir] tej jednostki x Stosy [NoirBindArmor]) obrażeń\n[WhenUse] zyskuje 3 Licznika [ChargeNoir]
492. [Umiejętność wroga [148801] (ulepszenie 1) — nazwa] 가죽 뜯기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148801].levelList[level=1].name
   limit: do 40 znaków
   EN: Flaying
   PL: Flaying
493. [Umiejętność wroga [148801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 297 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Umiejętność wroga [148801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 191 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Umiejętność wroga [148801] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148801].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Umiejętność wroga [148801] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148801].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Umiejętność wroga [148802] (ulepszenie 1) — nazwa] 육면 제거
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].name
   limit: do 40 znaków
   EN: Fleshing
   PL: Fleshing
498. [Umiejętność wroga [148802] (ulepszenie 1) — opis] 전장에 <color=#ff6000><mark=#ff000040><b><u>생존한 무두질된 죄수 1명당 피해량 +10%</u></b></mark></color>\n[DefeatDuel] 이 스킬 피해량 -80%, 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <color=#ff6000><mark=#ff000040><b><u>Deal +10% damage for every surviving Tanned Prisoner</u></b></mark></color> on the field\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje <color=#ff6000><mark=#ff000040><b><u>+10% obrażeń za każdego żywego Tanned Prisoner</u></b></mark></color> na polu\n[DefeatDuel] ta Umiejętność zadaje -80% obrażeń, a jej obrażenia nie Oszołamiają celu
499. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Laceration]
501. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL: [OnSucceedAttack] nakłada 3 [Laceration]
504. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność wroga [148802] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Vulnerable] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148802].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vulnerable]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vulnerable] = 취약 / Fragile
   EN: [OnSucceedAttack] Inflict 2 [Vulnerable] next turn
   PL: [OnSucceedAttack] nakłada 2 [Vulnerable] w następnej turze
507. [Umiejętność wroga [148803] (ulepszenie 1) — nazwa] 브레인 태닝
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148803].levelList[level=1].name
   limit: do 40 znaków
   EN: Brain Tanning
   PL: Brain Tanning
508. [Umiejętność wroga [148803] (ulepszenie 1) — opis] 대상 변경 불가\n이 스킬은 체력이 가장 낮은 아군을 우선으로 지정함\n\n지정한 대상을 공격하지 못했으면, 스킬이 취소됨
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148803].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Target Fixed\nThis Skill prioritizes allies that have the lowest HP\n\nIf this unit failed to attack the targeted unit, cancel this Skill
   PL: nie można zmienić celu\npriorytet: sojusznicy o najniższym HP\n\njeżeli atak na wskazaną jednostkę się nie powiódł, Umiejętność zostaje anulowana
509. [Umiejętność wroga [148803] (ulepszenie 1) — tekst klimatyczny] 정육된 원피들의 뇌 기름으로 처리하는 무두질. 지하 3층의 비법소스.
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148803].levelList[level=1].flavor
   limit: do 150 znaków
   EN: Tanning treatment technique using the brain fat of the butchered original hides. This is B3F's secret recipe.
   PL: Garbowanie prowadzone mózgowym tłuszczem ubiczych pierwotnych skór. Tajemny przepis B3F.
510. [Umiejętność wroga [148803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면 아래 효과 적용\n- 대상을 등에 다시 넣음\n- 자신의 최대 체력의 1%만큼 체력 회복\n- 정신력 20 회복\n- 이번 턴과 다음 턴에 [AttackDmgUp] 2 얻음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [AttackDmgUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [OnSucceedAttack] If the target is an ally, apply the following effects:\n- Re-insert the target into its back\n- Heal 1% HP\n- Heal 20 SP\n- Gain 2 [AttackDmgUp] this turn and next turn
   PL: [OnSucceedAttack] jeżeli cel jest sojusznikiem, stosuje poniższe efekty:\n- ponownie osadza cel na swoim grzbiecie\n- przywraca 1% HP\n- przywraca 20 SP\n- zyskuje 2 [AttackDmgUp] w tej i w następnej turze
511. [Umiejętność wroga [148804] (ulepszenie 1) — nazwa] 스플리팅
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148804].levelList[level=1].name
   limit: do 40 znaków
   EN: Splitting
   PL: Splitting
512. [Umiejętność wroga [148804] (ulepszenie 1) — opis] [EndBattle] 다음 턴에 무두질된 죄수를 2명까지 소환하고 [B3FreshMob] 부여\n\n- 전장에 생존한 무두질된 죄수가 6명을 초과하도록 소환할 수 없음\n- 소환한 무두질된 죄수 1명당, 최대 체력의 0.5% 소모\n- <color=#ff6000><mark=#ff000040><b><u>아래 조건 만족시 이 효과 비활성화</u></b></mark></color>\n· 이 스킬을 사용하는 슬롯에 메인 타겟으로 지정된 공격 스킬이 2개 이상\n· 전장에 생존한 무두질된 죄수가 6명 이상
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148804].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [EndBattle], [B3FreshMob]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [B3FreshMob] = 주름잡히지 않은 가죽 / Uncreased Hide
   EN: [EndBattle] Summon up to 2 Tanned Prisoner next turn and apply [B3FreshMob]\n\n- Summoned Tanned Prisoners cannot exceed 6 units\n- Consume 0.5% HP for every summoned Tanned Prisoner\n- <color=#ff6000><mark=#ff000040><b><u>Disable this effect if either of the following conditions is met:</u></b></mark></color>\n· If the Skill Slot using this Skill is a main target of 2+ Attack Skills\n· If there are 6 or more surviving Tanned Prisoners on the field
   PL: [EndBattle] przywołuje w następnej turze do 2 Tanned Prisoner i nakłada [B3FreshMob]\n\n- liczba przywołanych Tanned Prisoner nie może sprawić, by na polu było ich więcej niż 6\n- zużywa 0.5% Maks. HP za każdego przywołanego Tanned Prisoner\n- <color=#ff6000><mark color=#ff000040><b><u>dezaktywuje ten efekt, jeżeli spełniony jest którykolwiek z poniższych warunków:</u></b></mark></color>\n· jeżeli slot, w którym użyto tej Umiejętności, jest głównym celem 2+ Umiejętności ataku\n· jeżeli na polu przeżywa 6+ Tanned Prisoner
513. [Umiejętność wroga [148804] (ulepszenie 1) — tekst klimatyczny] 원죄와 원피를 분할하는 작업
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148804].levelList[level=1].flavor
   limit: do 120 znaków
   EN: A treatment process separating the Original Sin from the Original Hide
   PL: Proces rozdzielający Grzech Pierworodny od Pierwotnej Skóry
514. [Umiejętność wroga [148804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność wroga [148805] (ulepszenie 1) — nazwa] 매시브 스플리팅
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148805].levelList[level=1].name
   limit: do 40 znaków
   EN: Massive Splitting
   PL: Massive Splitting
516. [Umiejętność wroga [148805] (ulepszenie 1) — opis] [EndBattle] 다음 턴에 무두질된 죄수를 4명까지 소환하고 [B3FreshMob] 부여\n- 전장에 생존한 무두질된 죄수가 6명을 초과하도록 소환할 수 없음\n- 소환한 무두질된 죄수 1명당, 최대 체력의 0.5% 소모\n\n[StartBattle] 모든 아군에게 다음 턴에 [AttackDmgUp] 1 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148805].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [EndBattle], [B3FreshMob], [StartBattle], [AttackDmgUp]
   znaczenie tagów: [EndBattle] = [턴 종료 시] / [Turn End]; [B3FreshMob] = 주름잡히지 않은 가죽 / Uncreased Hide; [StartBattle] = [전투 시작시] / [Combat Start]; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [EndBattle] Summon up to 4 Tanned Prisoner next turn and apply [B3FreshMob]\n\n- Summoned Tanned Prisoners cannot exceed 6 units\n- Consume 0.5% HP for every summoned Tanned Prisoner\n\n[StartBattle] Apply 1 [AttackDmgUp] next turn on all allies
   PL: [EndBattle] przywołuje w następnej turze do 4 Tanned Prisoner i nakłada [B3FreshMob]\n- po przywołaniu na polu nie może być więcej niż 6 Tanned Prisoner\n- zużywa 0.5% Maks. HP za każdego przywołanego Tanned Prisoner\n\n[StartBattle] nakłada w następnej turze 1 [AttackDmgUp] na wszystkich sojuszników
517. [Umiejętność wroga [148805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Umiejętność wroga [148806] (ulepszenie 1) — nazwa] 원죄적 뇌유 텀블링
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].name
   limit: do 70 znaków
   EN: Leather Tumbling in Brain Fat: Original Sin Style
   PL: Leather Tumbling in Brain Fat: Original Sin Style
519. [Umiejętność wroga [148806] (ulepszenie 1) — opis] 전장에 <color=#ff6000><mark=#ff000040><b><u>생존한 무두질된 죄수 1명당 피해량 +10%</u></b></mark></color>\n[StartBattle] 자신을 제외한 모든 아군에게 [Enhancement] 2 부여\n[WhenUse] 자신의 현재 체력이 최대 체력의 50% 미만이면, 전장에 존재하는 무두질된 죄수 1명당 최종 위력 +1\n[DefeatDuel] 이 스킬 피해량 -80%, 이 스킬의 피해로 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [StartBattle], [Enhancement], [WhenUse], [DefeatDuel]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <color=#ff6000><mark=#ff000040><b><u>Deal +10% damage for every surviving Tanned Prisoner</u></b></mark></color> on the field\n[StartBattle] Apply 2 [Enhancement] on all other allies\n[WhenUse] If this unit has lower than 50% HP, gain Final Power +1 for every Tanned Prisoner on the field\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: zadaje <color=#ff6000><mark color=#ff000040><b><u>+10% obrażeń za każdego żywego Tanned Prisoner</u></b></mark></color> na polu\n[StartBattle] nakłada 2 [Enhancement] na wszystkich innych sojuszników\n[WhenUse] jeżeli aktualne HP tej jednostki jest niższe niż 50% Maks. HP, Moc Końcowa +1 za każdego Tanned Prisoner na polu\n[DefeatDuel] ta Umiejętność zadaje -80% obrażeń, a jej obrażenia nie Oszołamiają celu
520. [Umiejętność wroga [148806] (ulepszenie 1) — tekst klimatyczny] 그것의 뇌속에서 죄인의 뇌들이 흔들리고 뒤섞여 뇌유와 함께 무두질된 가죽이 흩뿌려진다
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].flavor
   limit: do 140 znaków
   EN: Within its brain are the brains of sinners, tumbling and mixing as they are tanned by its cerebral fluid.
   PL: Wewnątrz jego mózgu bujają się mózgi grzeszników, kołysząc się i mieszając, garbowane przez jego mózgowy płyn
521. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Umiejętność wroga [148806] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148806].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Umiejętność wroga [148807] (ulepszenie 1) — nazwa] 퍼니싱 버니싱 피니싱
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].name
   limit: do 50 znaków
   EN: Punishing Burnishing Finishing
   PL: Punishing Burnishing Finishing
528. [Umiejętność wroga [148807] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 수비 스킬을 발동시키지 않음 (합 가능 수비 포함)\n\n[EndSkill] 무작위 무두질된 죄수 3명이 대상에게 무작위 스킬을 사용하도록 명령 (흐트러지지 않은 아군 우선)
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [EndSkill]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: [CantDuel]\nThis Skill does not trigger Defense Skills (including Clashable Defense Skills)\n\n[EndSkill] Order 3 random Tanned Prisoners to use random Skills against the target (prioritizes allies that are not Staggered)
   PL: [CantDuel]\nta Umiejętność nie uruchamia Umiejętności obrony (łącznie z Obronami zdolnymi do Starcia)\n\n[EndSkill] rozkazuje 3 losowym Tanned Prisoner użycie losowych Umiejętności na celu (priorytet: sojusznicy spoza Oszołamienia)
529. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 1 — opis] 피해량 +100%
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: Deal +100% damage
   PL: zadaje +100% obrażeń
530. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 10 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 10 [Vibration]
   PL: [OnSucceedAttack] nakłada 10 [Vibration]
531. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL: [OnSucceedAttack] wywołuje [VibrationExplosion], po czym zmniejsza Licznik [Vibration] o 1
533. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 5 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#4].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Umiejętność wroga [148807] (ulepszenie 1) — moneta 1, efekt 6 — opis] [OnSucceedAttack] [VibrationExplosion]. [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=148807].levelList[level=1].coinlist[#0].coindescs[#5].desc
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Umiejętność wroga [149101] (ulepszenie 1) — nazwa] 뇌유 뿌리기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149101].levelList[level=1].name
   limit: do 40 znaków
   EN: Brain Fat Spray
   PL: Brain Fat Spray
536. [Umiejętność wroga [149101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Umiejętność wroga [149101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Reduction] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Reduction]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: [OnSucceedAttack] Inflict 2 [Reduction] next turn
   PL: [OnSucceedAttack] nakłada 2 [Reduction] w następnej turze
538. [Umiejętność wroga [149102] (ulepszenie 1) — nazwa] 뇌유 문대기
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149102].levelList[level=1].name
   limit: do 40 znaków
   EN: Brain Fat Buffing
   PL: Brain Fat Buffing
539. [Umiejętność wroga [149102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność wroga [149102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [DefenseDown] 5 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 5 [DefenseDown] next turn
   PL: [OnSucceedAttack] nakłada 5 [DefenseDown] w następnej turze
541. [Umiejętność wroga [149102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 2 부여
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis] next turn
   PL: [OnSucceedAttack] nakłada 2 [Paralysis] w następnej turze
542. [Umiejętność wroga [149103] (ulepszenie 1) — nazwa] 속죄적 엠보싱
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149103].levelList[level=1].name
   limit: do 40 znaków
   EN: Expiatory Embossing
   PL: Expiatory Embossing
543. [Umiejętność wroga [149103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 통제자의 최대 체력의 1%만큼 통제자의 부위 및 본체 체력을 회복
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 1% HP to Overseer's Parts and Core
   PL: [OnSucceedAttack] przywraca 1% HP Częściom i rdzeniu The Overseer
544. [Umiejętność wroga [149103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Umiejętność wroga [149103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 통제자의 최대 체력의 1%만큼 통제자의 부위 및 본체체력을 회복
   źródło: Skills_Abnormality-a1c10p2.json :: dataList[id=149103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 1% HP to Overseer's Parts and Core
   PL: [OnSucceedAttack] przywraca 1% HP Częściom i rdzeniu The Overseer

## [a1c10p2] Pasywka wroga: Passives_Abnormality-a1c10p2
- plik gry: `Passives_Abnormality-a1c10p2.json`

546. [[a1c10p2] Pasywka wroga [150301] — nazwa] 멎지 않는 곡성
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150301].name
   limit: do 40 znaków
   EN: Ceaseless Wailing
   PL: Ceaseless Wailing
547. [[a1c10p2] Pasywka wroga [150301] — opis] 스테이지 시작시 패닉 상태로 전투 시작\n\n패닉 상태일 때, 아래 효과 적용\n- <color=#ff6000><mark color=#ff000040><b><u>모든 공격의 대상을 뿌이로 지정</color></mark></b></u>\n- 스킬 사용 시 메인 타겟이 뿌이면 합 위력, 기본 위력 증가[TabExplain]\n- 전투 시작 시 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150301].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [TabExplain], [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Encounter Start: Enter Panic state\n\nIf this unit is in Panic state, apply the following effects:\n- <color=#ff6000><mark color=#ff000040><b><u>All Attacks target Pwie</color></mark></b></u>\n- On Skill Use, if Pwie is the main target, gain Clash Power and Base Power\n- Combat Start: Convert all Coins into [SuperCoin]s
   PL: Na początku etapu: rozpoczyna walkę w Panice\n\nw Panice stosuje następujące efekty:\n- <color=#ff6000><mark color=#ff000040><b><u>wszystkie ataki celują w Pwie</u></b></mark></color>\n- przy użyciu Umiejętności, jeżeli Pwie jest głównym celem, zwiększa Moc Starcia i Moc Bazową[TabExplain]\n- na początku walki wszystkie Monety tej Umiejętności zamieniają się w [SuperCoin]y
548. [[a1c10p2] Pasywka wroga [150301] — tekst klimatyczny] 옛것의 아이들은 더 이상 남지 않게되어버렸다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150301].flavor
   limit: do 120 znaków
   EN: The children of the thing of eld are no more.
   PL: Dzieci dawnej rzeczy już nie istnieją.
549. [[a1c10p2] Pasywka wroga [150302] — nazwa] 엉킨 검은실
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150302].name
   limit: do 40 znaków
   EN: Tangled Black Thread
   PL: Tangled Black Thread
550. [[a1c10p2] Pasywka wroga [150302] — opis] 스킬과 사기저하, 패닉 효과로 적에게 [TangleBlackYarn] 부여\n※[TangleBlackYarn]은 <color=#ff6000><mark color=#ff000040><b><u>수비 스킬을 사용하거나 특정 스킬을 통해 감소 가능</color></mark></b></u>\n\n피격 시 다음 효과 발동\n- 피격시 [SickBlackYarn] 1 얻음\n- 피격 당한 스킬이 <color=#ff6000><mark color=#ff000040><b><u>참격 속성</color></mark></b></u>이면, [SickBlackYarn] 1 추가 얻음\n- <color=#ff6000><mark color=#ff000040><b><u>가중치 5 이상</color></mark></b></u>인 스킬로 피격 시 다음 턴에 [HeavyBlackYarn] 얻음 (턴당 1회)
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150302].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [TangleBlackYarn], [SickBlackYarn], [HeavyBlackYarn]
   znaczenie tagów: [TangleBlackYarn] = 뒤엉킴 / Tangling; [SickBlackYarn] = 뜯겨져 나가는 검은실밥 / Bursting Blackstitch; [HeavyBlackYarn] = 검게 뭉친 실 / Clumped Black Threads
   EN: The effects of this unit's Skills, Low Morale, and Panic inflict [TangleBlackYarn] on the enemy\n※ [TangleBlackYarn] can be reduced either by <color=#ff6000><mark color=#ff000040><b><u>using Defense Skills or via certain Skills of this unit</color></mark></b></u>\nWhen hit, activate the following effects:\n- Gain 1 [SickBlackYarn]\n- If the Skill that hit this unit is a <color=#ff6000><mark color=#ff000040><b><u>Slash Skill</color></mark></b></u>, gain 1 additional [SickBlackYarn]\n- If the Skill that hit this unit has <color=#ff6000><mark color=#ff000040><b><u>5+ Atk Weight</color></mark></b></u>, gain [HeavyBlackYarn] next turn (once per turn)
   PL: Umiejętności tej jednostki, Niski Moral oraz Panika nakładają [TangleBlackYarn] na wroga\n※ [TangleBlackYarn] można zmniejszyć, <color=#ff6000><mark color=#ff000040><b><u>używając Umiejętności obrony lub przez określone Umiejętności tej jednostki</u></b></mark></color>\n\nprzy trafieniu uruchamia następujące efekty:\n- zyskuje 1 [SickBlackYarn]\n- jeżeli Umiejętność, którą trafiono tę jednostkę, ma <color=#ff6000><mark color=#ff000040><b><u>Afiniczność Cięcia</u></b></mark></color>, zyskuje dodatkowo 1 [SickBlackYarn]\n- przy trafieniu Umiejętnością o <color=#ff6000><mark color=#ff000040><b><u>Wadze Ataku 5+</u></b></mark></color> zyskuje w następnej turze [HeavyBlackYarn] (1 raz na turę)
551. [[a1c10p2] Pasywka wroga [150302] — tekst klimatyczny] 이것의 몸에 감긴 검은실은 이전에 없었다. 운좋게도 시대가 바뀌는 때에 실들이 옛것의 몸에 감겼고, 실로 감겨진 몸 덕분에 백화점의 시대에서 살아남을수있었다. 그리고 그 검은실이 이제 헤쳐풀어진다.\n\n아쿠아리움의 시대 이전에는 플라자의 시대, 방공호의 시대, 재판장의 시대 여러 시대가 있었고 그 이름과 형식은 다를지언정 시지프 시스템을 작동시키는 본질은 같았다.\n\n그리고 시대가 바뀔 때마다 사람들은 바뀐 세계에 인간의 모습을 한 채 적응해가며 시지프 속에서 시대를 견뎌왔다.\n\n지금 이 엉킨 실은 두 시대만이 아닌 퇴적되어온 모든 시대의 엉킴인 것이다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150302].flavor
   limit: do 1040 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The black thread wound around its body was not there before. By sheer fortune, when the previous age gave way to the next, those threads coiled around the body of the thing of eld. Wrapped in thread, it survived into the Age of the Department Store. Now, those black threads begin to come undone.\n\nBefore the Age of the Aquarium, came the Age of the Plaza, the Age of the Bomb Shelters, the Age of the Courtroom, and many others. Their names and forms may have differed, but the essence that drove the workings of the Sisyphe System remained ever the same.\n\nWith each passing Age, people adapted to the transformed world, enduring one era after another in their human form.\n\nWhat lies tangled in the threads of the present Age is not merely that of the two preceding Ages, but every Age that has settled here, layer upon layer.
   PL: Czarne włókno oplatające jego ciało nie znajdowało się tam wcześniej. Z czystego szczęścia, gdy poprzednia era ustępowała następnej, włókna oplotły ciało dawnej rzeczy. Oplecione włóknem ciało pozwoliło mu przetrwać Erę Domu Towarowego. A teraz te czarne włókna zaczynają się rozplatać.\n\nPrzed Erą Akwarium była Era Placu, Era Schronów, Era Sali Rozpraw i wiele innych. Różniły się nazwami i formą, lecz istota napędzająca System Sisyphe pozostawała niezmienna.\n\nZ każdą zmianą ery ludzie dostosowywali się do przemienionego świata, odcierając cierpienia kolejnych czasów w ludzkiej postaci.\n\nWłókna splątane w obecnej Erze nie są jedynie spleceniem dwóch poprzednich, lecz wszystkich er, które osiadały tu warstwa po warstwie.
552. [[a1c10p2] Pasywka wroga [150303] — nazwa] 옛 바다속으로
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150303].name
   limit: do 40 znaków
   EN: Into the Waters of Eld
   PL: Into the Waters of Eld
553. [[a1c10p2] Pasywka wroga [150303] — opis] 부위가 <color=#ff6000><mark color=#ff000040><b><u>흐트러짐 상태</color></mark></b></u>가 되면, 다른 부위의 <color=#ff6000><mark color=#ff000040><b><u>흐트러짐 구간을 1개씩 제거하고 턴 종료</color></mark></b></u>\n이후 다음 턴 모든 부위에 [HideBlackYarn] 얻음\n\n<color=#ff6000><mark color=#ff000040><b><u>피격으로 [HideBlackYarn]가 소멸</color></mark></b></u>했으면,\n- [SickBlackYarn] 10 얻음\n- [SickBlackYarn]의 최댓값을 초과하여 얻었으면, 이번 턴과 다음 턴에 취약 3 얻음\n\n턴 종료 시 [HideBlackYarn]가 소멸했으면,\n- [SickBlackYarn]을 (7 - 남은 위력)만큼 얻음\n- 다음 턴에 [AngryBlackYarn] 1 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150303].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [HideBlackYarn], [SickBlackYarn], [AngryBlackYarn]
   znaczenie tagów: [HideBlackYarn] = 검은 물 웅덩이 / Pool of Black Water; [SickBlackYarn] = 뜯겨져 나가는 검은실밥 / Bursting Blackstitch; [AngryBlackYarn] = 옛 포식자의 본능 / Instinct of the Predator of Eld
   EN: If a Part becomes <color=#ff6000><mark color=#ff000040><b><u>Staggered</color></mark></b></u>, remove <color=#ff6000><mark color=#ff000040><b><u>1 Stagger Threshold from other Parts and end the turn</color></mark></b></u>; then, all Parts gain [HideBlackYarn] next turn\n\n<color=#ff6000><mark color=#ff000040><b><u>If [HideBlackYarn] expired due to being hit</color></mark></b></u>,\n- Gain 10 [SickBlackYarn]\n- If [SickBlackYarn] was gained beyond its max cap, gain 3 Fragile this turn and next turn\n\nTurn End: If [HideBlackYarn] expired,\n- Gain (7 - remaining Potency) [SickBlackYarn]\n- Gain 1 [AngryBlackYarn] next turn
   PL: gdy <color=#ff6000><mark color=#ff000040><b><u>Część przechodzi w Oszołamienie</u></b></mark></color>, <color=#ff6000><mark color=#ff000040><b><u>usuwa po 1 Próg Oszołomienia z innych Części i kończy turę</u></b></mark></color>, a następnie wszystkie Części zyskują [HideBlackYarn] w następnej turze\n\n<color=#ff6000><mark color=#ff000040><b><u>jeżeli [HideBlackYarn] wygasło przez trafienie</u></b></mark></color>,\n- zyskuje 10 [SickBlackYarn]\n- jeżeli zyskane [SickBlackYarn] przekroczyło maksimum, zyskuje w tej i w następnej turze 3 Kruchości\n\njeżeli [HideBlackYarn] wygasło na koniec tury,\n- zyskuje (7 - pozostała Siła) [SickBlackYarn]\n- zyskuje 1 [AngryBlackYarn] w następnej turze
554. [[a1c10p2] Pasywka wroga [150303] — tekst klimatyczny] 한때 당연하고도 자유롭게 헤엄쳤던, 이제는 사라진 시대의 바다의 품속으로.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150303].flavor
   limit: do 140 znaków
   EN: Into the embrace of the sea from a bygone age, where once it swam as naturally and freely as could be.
   PL: W objęcia morza minionej ery, gdzie niegdyś pływało tak swobodnie i naturalnie, jak tylko się dało.
555. [[a1c10p2] Pasywka wroga [150304] — nazwa] 아직 마르지 않은 물기
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150304].name
   limit: do 40 znaków
   EN: Lingering Dampness
   PL: Lingering Dampness
556. [[a1c10p2] Pasywka wroga [150304] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력, 흐트러짐 손상 피해량 -50%\n\n패닉 유형이 변경되지 않으며, 턴 종료 시 패닉 상태라면 정신력이 0이 됨
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150304].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Take less HP and SP damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]; -50% to Stagger Threshold raised by [Vibration]\n\nThis unit's Panic Type does not change when inflicted with an effect that changes Panic Types\nTurn End: If this unit is in Panic, SP returns to 0
   PL: otrzymuje -50% obrażeń HP i SP od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]; podniesienie Progu Oszołomienia przez [Vibration] zmniejsza się o 50%\n\ntyp Paniki tej jednostki nie ulega zmianie\nKoniec tury: jeżeli ta jednostka jest w Panice, jej SP wynosi 0
557. [[a1c10p2] Pasywka wroga [150304] — tekst klimatyczny] 시지프 아쿠아리움은 사라졌지만, 이 몸에는 아직 실로 변하지 않은 미약한 그때 그 물기가 남아있다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150304].flavor
   limit: do 180 znaków
   EN: Aquarium Sisyphe is gone, yet this body still retains a faint trace of the water from those days—moisture that has not yet turned to thread.
   PL: Aquarium Sisyphe odszedł, lecz w tym ciele wciąż kryje się nikłe mokre piętno tamtych czasów — wilgoć, która nie zdążyła stać się włóknem.
558. [[a1c10p2] Pasywka wroga [150101] — nazwa] 흙으로 빚어진 인형
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150101].name
   limit: do 40 znaków
   EN: A Doll Molded from Clay
   PL: A Doll Molded from Clay
559. [[a1c10p2] Pasywka wroga [150101] — opis] 스테이지 시작시 체력을 최대로 회복함\n\n본체와 부위가 [Combustion], [Laceration]로 피해를 받지 않음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150101].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: Encounter Start: Heal to max HP\n\nThe Core and the Part do not take damage from [Combustion] and [Laceration]
   PL: Na początku etapu: przywraca HP do maksimum\n\nrdzeń i Części nie otrzymują obrażeń od [Combustion] i [Laceration]
560. [[a1c10p2] Pasywka wroga [150101] — tekst klimatyczny] 도자기와 같은 피부는 흙으로부터 왔다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150101].flavor
   limit: do 120 znaków
   EN: That porcelain-like skin came from clay.
   PL: Porcelanowa skóra pochodzi z gliny.
561. [[a1c10p2] Pasywka wroga [150102] — nazwa] 시들지 않는 꽃
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150102].name
   limit: do 40 znaków
   EN: Unwithering Flower
   PL: Unwithering Flower
562. [[a1c10p2] Pasywka wroga [150102] — opis] 전투 시작시 [AlriunePetal]을 1 얻음\n\n자신이 흐트러지면,\n- 다음 턴에 [Vulnerable]을 2 얻음\n- 수감자 및 조력자의 정신력을 20 회복\n- 흐트러짐에서 회복한 턴 시작시 [AlriunePetal]을 1로 초기화\n\n턴 시작시 [FlowerLaurelWreath]을 보유한 적이 없으면 <color=#ff6000><mark color=#ff000040><b><u>‘좋은 향기가 나는 월계관’을 장착함</color></mark></b></u>\n- ‘흙으로 돌아가고자 하는 소망을 품고’을 장착했을 경우 다음 턴에 장착함\n\n<color=#ff6000><mark color=#ff000040><b><u>[FlowerLaurelWreath] 효과를 보유하지 않은 적에게 스킬로 받는 피해량 -50%</color></mark></b></u>\n<color=#ff6000><mark color=#ff000040><b><u>[FlowerLaurelWreath] 효과를 보유한 적에게 스킬로 받는 피해량 +150%</color></mark></b></u>
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150102].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [AlriunePetal], [Vulnerable], [FlowerLaurelWreath]
   znaczenie tagów: [AlriunePetal] = 꽃잎 / Petals; [Vulnerable] = 취약 / Fragile; [FlowerLaurelWreath] = 속죄의 월계관 / Laurel Wreath of Atonement
   EN: Combat Start: Gain 1 [AlriunePetal]\n\nIf this unit becomes Staggered,\n- Gain 2 [Vulnerable] next turn\n- Heal 20 SP on Sinners and Assist Units\n- Turn Start: If this unit recovered from Stagger, reset [AlriunePetal] to 1\n\nTurn Start: If no enemies have [FlowerLaurelWreath], <color=#ff6000><mark color=#ff000040><b><u>equip the "Fragrant Laurel Wreath" Skill</color></mark></b></u>\n- Equip the said Skill next turn if this unit equipped "Bearing the hope to return to dust..." this turn\n\n<color=#ff6000><mark color=#ff000040><b><u>Take -50% damage from Skills used by enemies that do not have [FlowerLaurelWreath]</color></mark></b></u>\n<color=#ff6000><mark color=#ff000040><b><u> Take +150% damage from enemies that have [FlowerLaurelWreath]</color></mark></b></u>
   PL: Początek walki: zyskuje 1 [AlriunePetal]\n\njeżeli ta jednostka przechodzi w Oszołamienie:\n- zyskuje 2 [Vulnerable] w następnej turze\n- przywraca 20 SP Grzesznikom i jednostkom wsparcia\n- Początek tury, w której doszła do siebie po Oszołamieniu: resetuje [AlriunePetal] do 1\n\nPoczątek tury: jeżeli żaden wróg nie ma [FlowerLaurelWreath], <color=#ff6000><mark color=#ff000040><b><u>zakłada Umiejętność „Fragrant Laurel Wreath”</u></b></mark></color>\n- jeżeli w tej turze założono „Bearing the hope to return to dust...”, zakłada ją w następnej turze\n\n<color=#ff6000><mark color=#ff000040><b><u>otrzymuje -50% obrażeń z Umiejętności wrogów nieposiadających [FlowerLaurelWreath]</u></b></mark></color>\n<color=#ff6000><mark color=#ff000040><b><u>otrzymuje +150% obrażeń od wrogów mających [FlowerLaurelWreath]</u></b></mark></color>
563. [[a1c10p2] Pasywka wroga [150102] — tekst klimatyczny] 꽃은 시든다. 그리고 다시 피어난다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150102].flavor
   limit: do 120 znaków
   EN: Flowers wilt. Then they bloom again.
   PL: Kwiaty więdną. I znów zakwitają.
564. [[a1c10p2] Pasywka wroga [150103] — nazwa] 입춘
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150103].name
   limit: do 40 znaków
   EN: Spring's Advent
   PL: Spring's Advent
565. [[a1c10p2] Pasywka wroga [150103] — opis] 적이 흐트러졌으면, 대상에게 정신력 피해 20\n\n턴 시작 시 <color=#ff6000><mark color=#ff000040><b><u>패닉 또는 침식 상태인 대상이 있으면, 해당 대상에게 ‘살고자 하는 모든 것들과 무덤으로 돌아가리’를 사용함</color></mark></b></u> (턴당 2회, 속도가 느린 대상 순으로 사용, 조력자 제외)\n\n해당 대상이 해당 스킬로 사망했으면, 다음 턴에 흙에서 태어난 자 1명이 생성됨\n- 전투에 흙에서 태어난 자가 4명이면, 생성되지 않음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150103].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Deal 20 SP damage to Staggered enemies\n\nTurn Start: <color=#ff6000><mark color=#ff000040><b><u>If there is a target in Panic or in Corrosion, use "... It shall go back to the grave with all that desires to live" on the said target</color></mark></b></u> (max 2 times per turn, prioritizes the slowest enemies in ascending order of Speed, excluding Assist Units)\n\nIf the said Skill killed the target, summon 1 "One Who Emerged from the Earth" next turn\n- This effect does not activate when there are 4 "One Who Emerged from the Earth" on the field
   PL: zadaje 20 obrażeń SP oszołamionym wrogom\n\nPoczątek tury: <color=#ff6000><mark color=#ff000040><b><u>jeżeli istnieje cel w Panice lub w Korozji, używa „... It shall go back to the grave with all that desires to live” na tym celu</u></b></mark></color> (maks. 2 razy na turę, używa na celach od najwolniejszych, z wyłączeniem jednostek wsparcia)\n\njeżeli ta Umiejętność pokonała cel, w następnej turze powstaje 1 One Who Emerged from the Earth\n- efekt nie uruchamia się, jeżeli na polu są 4 One Who Emerged from the Earth
566. [[a1c10p2] Pasywka wroga [150103] — tekst klimatyczny] 봄이 오면 피어나리
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150103].flavor
   limit: do 120 znaków
   EN: When spring comes, it shall bloom.
   PL: Gdy przyjdzie wiosna, zakwitnie.
567. [[a1c10p2] Pasywka wroga [150201] — nazwa] 흙으로부터
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150201].name
   limit: do 40 znaków
   EN: From the Earth
   PL: From the Earth
568. [[a1c10p2] Pasywka wroga [150201] — opis] [Combustion], [Laceration]으로 피해를 받지 않음\n\n<color=#ff6000><mark color=#ff000040><b><u>[Vibration]으로 받는 흐트러짐 피해 +100%</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>자신이 흐트러짐이 되면 사망함</color></mark></b></u>
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150201].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [Combustion], [Laceration], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor
   EN: This unit does not take damage from [Combustion] and [Laceration]\n\n<color=#ff6000><mark color=#ff000040><b><u>+100% to Stagger Threshold raised by [Vibration]</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>This unit is defeated when Staggered</color></mark></b></u>
   PL: ta jednostka nie otrzymuje obrażeń od [Combustion] i [Laceration]\n\n<color=#ff6000><mark color=#ff000040><b><u>podniesienie Progu Oszołomienia przez [Vibration] zwiększa się o 100%</u></b></mark></color>\n\n<color=#ff6000><mark color=#ff000040><b><u>ta jednostka zostaje pokonana, gdy przechodzi w Oszołamienie</u></b></mark></color>
569. [[a1c10p2] Pasywka wroga [150201] — tekst klimatyczny] 다시 흙으로
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150201].flavor
   limit: do 120 znaków
   EN: Back to the earth.
   PL: Z powrotem do ziemi.
570. [[a1c10p2] Pasywka wroga [151901] — nazwa] 초고속 SPM
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151901].name
   limit: do 40 znaków
   EN: Ultra-High-Speed SPM
   PL: Ultra-High-Speed SPM
571. [[a1c10p2] Pasywka wroga [151901] — opis] 자신이 공격하는 대상의 <color=#ff6000><mark color=#ff000040><b><u>속도가 자신보다 낮으면, 합 위력 +3</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>[ChargeKhaki] 횟수를 소모하는 스킬 사용 턴 종료 시 자신의 [ChargeKhaki] 횟수가 11 이상이면,</color></mark></b></u> 강력한 스킬을 사용함\n\n자신의 체력이 50% 이하면, 강력한 스킬을 사용함 (전투당 1회)
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151901].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [ChargeKhaki]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: If target's <color=#ff6000><mark color=#ff000040><b><u>Speed is slower than this unit's, Clash Power +3</color></mark></b></u>\n\n<color=#ff6000><mark color=#ff000040><b><u>If this unit has 11+ [ChargeKhaki] Count at the end of the turn this unit used a Skill that consumes [ChargeKhaki] Count</color></mark></b></u>, use a powerful Skill\n\nAt 50% or less HP, use a powerful Skill (once per Encounter)
   PL: jeżeli <color=#ff6000><mark color=#ff000040><b><u>Szybkość atakowanego celu jest niższa niż tej jednostki, Moc Starcia +3</u></b></mark></color>\n\n<color=#ff6000><mark color=#ff000040><b><u>jeżeli na koniec tury, w której ta jednostka użyła Umiejętności zużywającej Liczniki [ChargeKhaki], ma ona 11+ Licznika [ChargeKhaki],</u></b></mark></color> używa potężnej Umiejętności\n\nprzy HP 50% lub mniej używa potężnej Umiejętności (1 raz na walkę)
572. [[a1c10p2] Pasywka wroga [151901] — podsumowanie] 대상의 속도가 자신보다 낮으면, 합 위력 증가
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151901].summary
   limit: do 120 znaków
   EN: If target's Speed is slower than this unit's, gain Clash Power
   PL: jeżeli Szybkość celu jest niższa niż tej jednostki, zwiększa Moc Starcia
573. [[a1c10p2] Pasywka wroga [151901] — tekst klimatyczny] 언니는 10000 SPM까지 도달할 수 있어
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151901].flavor
   limit: do 120 znaków
   EN: Big Sis can reach 10,000 SPM.
   PL: Big Sis can reach 10,000 SPM.
574. [[a1c10p2] Pasywka wroga [151902] — nazwa] 네일드 스티치
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151902].name
   limit: do 40 znaków
   EN: Nailed Stitch
   PL: Nailed Stitch
575. [[a1c10p2] Pasywka wroga [151902] — opis] 흐트러지거나 행동 불가인 대상에게 가하는 피해 +40%
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151902].desc
   limit: do 120 znaków
   EN: Deal +40% damage to Staggered or immobilized targets
   PL: zadaje +40% obrażeń celom oszołamionym lub unieruchomionym
576. [[a1c10p2] Pasywka wroga [151902] — tekst klimatyczny] 멈춰있는 것을 박음질하는 것만큼 손쉬운 것은 없다
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151902].flavor
   limit: do 120 znaków
   EN: Nothing is easier than stitching something that cannot move.
   PL: Nic nie jest łatwiejsze niż zszywanie czegoś, co nie może się ruszać.
577. [[a1c10p2] Pasywka wroga [151903] — nazwa] 컬러 스티치
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151903].name
   limit: do 40 znaków
   EN: Color Stitch
   PL: Color Stitch
578. [[a1c10p2] Pasywka wroga [151903] — opis] 자신에게 [SpreadingDye]이 있으면, 자신의 스킬이 적중한 대상에게 [StickyDye] 1 부여\n\n[ThreadDye]이 있는 대상에게 아래의 효과 적용\n- 스킬로 부여하는 [Laceration] 위력, 횟수가 [ThreadDye] 위력 만큼 증가\n- 위 효과로 [StickyDye] 부여 시, 부여된 대상을 제외한 [ThreadDye]을 가지고 있는 무작위 적군 1명에게 [StickyDye] 1 부여\n\n자신의 스킬 대상이 [Inactible]를 보유하고 있는 경우, [ThreadDye]을 부여하지 않음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151903].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [SpreadingDye], [StickyDye], [ThreadDye], [Laceration], [Inactible]
   znaczenie tagów: [SpreadingDye] = 글로스 미디엄 / Gloss Medium; [StickyDye] = 타르 염료 / Tar Dye; [ThreadDye] = 염색실 / Dyed Thread; [Laceration] = 출혈 / Bleed; [Inactible] = 행동 불가 / Immobilized
   EN: If this unit has [SpreadingDye], inflict 1 [StickyDye] against targets this unit's Skill hit\n\nApply the following effects to targets that have [ThreadDye]:\n- Skills inflict +([ThreadDye] Potency) more [Laceration] Potency and Count\n- When inflicting [StickyDye] via the effect above, inflict 1 [StickyDye] on a random enemy that has [ThreadDye], excluding the target that has been inflicted \n\nDoes not inflict [ThreadDye] on Skill targets that have [Inactible]
   PL: jeżeli ta jednostka ma [SpreadingDye], nakłada 1 [StickyDye] na cele trafione Umiejętnością tej jednostki\n\nstosuje poniższe efekty na celach mających [ThreadDye]:\n- Umiejętności nakładają dodatkowo (Siła [ThreadDye]) Siły [Laceration] i Licznika [Laceration]\n- nakładając [StickyDye] tym efektem, nakłada 1 [StickyDye] na 1 losowego wroga mającego [ThreadDye], z wyłączeniem celu, któremu nakładano\n\nnie nakłada [ThreadDye] na cele Umiejętności mające [Inactible]
579. [[a1c10p2] Pasywka wroga [151903] — tekst klimatyczny] 언니가 천을 꿰매면, 동시에 내가 색을 입히는 거야.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151903].flavor
   limit: do 120 znaków
   EN: You stitch the fabric, Big Sis. I'll dye with you.
   PL: You stitch the fabric, Big Sis. I'll dye with you.
580. [[a1c10p2] Pasywka wroga [151904] — nazwa] 땀수조절장치 조정
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151904].name
   limit: do 50 znaków
   EN: Stitch Count Regulator Adjustment
   PL: Stitch Count Regulator Adjustment
581. [[a1c10p2] Pasywka wroga [151904] — opis] 스테이지 시작시 체력을 최대로 회복하고 정신력을 45 회복함\n\n전투 중 누적으로 자신의 [ChargeKhaki] 횟수 10을 소모할 때마다 [ChargeKhaki] 1 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151904].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeKhaki]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: Encounter Start: Heal max HP and 45 SP\n\nGain 1 [ChargeKhaki] for every 10 cumulative [ChargeKhaki] Count this unit consumed in this Encounter
   PL: Na początku etapu: przywraca HP do maksimum i 45 SP\n\nzyskuje 1 [ChargeKhaki] za każde 10 łącznie zużytych Liczników [ChargeKhaki] tej jednostki w tej walce
582. [[a1c10p2] Pasywka wroga [149501] — nazwa] 수선
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149501].name
   limit: do 40 znaków
   EN: Alteration
   PL: Alteration
583. [[a1c10p2] Pasywka wroga [149501] — opis] 턴 시작 시, 직전 턴에 자신에게 <color=#ff6000><mark=#ff000040><b><u>가장 많은 피해를 입힌 수감자</u></b></mark></color>에게\n<color=#ff6000><mark=#ff000040><b><u>[TailoringTarget] 1을 부여</u></b></mark></color>하고 ‘패턴 따기’ 사용\n- [TailoringTarget]인 수감자가 <color=#ff6000><mark=#ff000040><b><u>[ScissorsMark]을 9만큼 보유</u></b></mark></color>했으면,\n‘패턴 따기’가 <color=#ff6000><mark=#ff000040><b><u>‘쉬르필 아 라 셴’</u></b></mark></color>로 발동됨\n\n수감자에게 피격받을 때마다\n- 해당 수감자에게 [ScissorsMark] 1 부여 (수감자별 턴당 최대 5)\n- 자신의 [ChargeKhaki] 횟수 1 증가 (수감자별 턴당 최대 5)\n\n<color=#ff6000><mark=#ff000040><b><u>[TailoringTarget]을 보유한 수감자에게 공격 스킬로 피격받을 때마다\n[ResultEnhancement] 3 얻음 (턴당 최대 9)</u></b></mark></color>
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149501].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TailoringTarget], [ScissorsMark], [ChargeKhaki], [ResultEnhancement]
   znaczenie tagów: [TailoringTarget] = 수선 대상 / Alteration Target; [ScissorsMark] = 마름질 표식 / Mark of Shearing; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Turn Start: <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [TailoringTarget] on the Sinner that dealt the most damage</u></b></mark></color> to this unit last turn and use the "Patterning" Skill\n- If the [TailoringTarget] Sinner <color=#ff6000><mark=#ff000040><b><u>has 9 [ScissorsMark]</u></b></mark></color>, activate "Patterning" as <color=#ff6000><mark=#ff000040><b><u>"Surfile à la Chaîne"</u></b></mark></color> instead\n\nEvery time this unit is hit by a Sinner,\n- Inflict 1 [ScissorsMark] on the said Sinner (max 5 per turn per Sinner)\n- Gain +1 [ChargeKhaki] Count (max 5 per turn per Sinner)\n\n<color=#ff6000><mark=#ff000040><b><u>Gain 3 [ResultEnhancement] every time this unit is hit by a Sinner that has [TailoringTarget] (max 9 per turn)</u></b></mark></color>
   PL: Początek tury: <color=#ff6000><mark=#ff000040><b><u>nakłada 1 [TailoringTarget] na Grzesznika, który zadał najwięcej obrażeń</u></b></mark></color> tej jednostce w poprzedniej turze, i używa „Patterning”\n- jeżeli Grzesznik z [TailoringTarget] <color=#ff6000><mark=#ff000040><b><u>ma 9 [ScissorsMark]</u></b></mark></color>, „Patterning” uruchamia się jako <color=#ff6000><mark=#ff000040><b><u>„Surfile à la Chaîne”</u></b></mark></color>\n\nza każdym razem, gdy ta jednostka zostanie trafiona przez Grzesznika:\n- nakłada 1 [ScissorsMark] na tego Grzesznika (maks. 5 na turę na Grzesznika)\n- zyskuje 1 Licznika [ChargeKhaki] (maks. 5 na turę na Grzesznika)\n\n<color=#ff6000><mark=#ff000040><b><u>za każdym razem, gdy ta jednostka zostanie trafiona Umiejętnością ataku Grzesznika mającego [TailoringTarget], zyskuje 3 [ResultEnhancement] (maks. 9 na turę)</u></b></mark></color>
584. [[a1c10p2] Pasywka wroga [149501] — tekst klimatyczny] 옷은 수선으로 완성된다고들 한다. 맞춤으로 만들어진 옷이 아닌 이상, 수선을 통해 자신에게 맞춰 가야 한다.\n\n그리고 이는 옷에만 한정된 이야기가 아니다. 밖에서 얻은 것 역시 수선하여 걸쳐야, 비로소 자신의 마음에 맞게 입고 살아갈 수 있다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149501].flavor
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: They say a garment is only truly finished through alteration. Unless it was made to measure, it has to be adjusted until it fits the wearer.\n\nAnd that is not true of clothing alone. Whatever is taken in from the outside must first be altered to suit oneself before it can be worn, lived in, and made to fit the heart.
   PL: Mówi się, że ubranie naprawdę powstaje dopiero dzięki przeróbce. Dopóki nie uszyto go na miarę, trzeba je dopasowywać, aż leży na noszącym.\n\nA nie dotyczy to tylko odzieży. Cokolwiek nabytego z zewnątrz trzeba najpierw przerobić na własną miarę — dopiero wtedy można je nosić, żyć w tym i dopasować do serca.
585. [[a1c10p2] Pasywka wroga [149503] — nazwa] 재단
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149503].name
   limit: do 40 znaków
   EN: Tailoring
   PL: Tailoring
586. [[a1c10p2] Pasywka wroga [149503] — opis] 스테이지 시작 시 또는 흐트러짐 상태에서 벗어난 이후 턴 시작 시,\n[FinishedFabric] 30 얻음\n\n[PanicChangeLock] 효과가 적용되며,\n턴 종료 시 패닉 상태면 정신력이 30으로 변경됨\n\n턴 시작 시,\n- 자신의 <color=#ff6000><mark=#ff000040><b><u>최대 체력의 ([FinishedFabric] 수치)%만큼 보호막</u></b></mark></color> 얻음 (최대 30%)\n- [FinishedFabric] 수치만큼 정신력 회복
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149503].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [FinishedFabric], [PanicChangeLock]
   znaczenie tagów: [FinishedFabric] = 재단된 원단 / Cut Fabric; [PanicChangeLock] = 패닉 변경 불가 / Fixed Panic
   EN: At Encounter Start or at the start of the turn this unit recovered from Stagger, gain 30 [FinishedFabric]\n\nApply the [PanicChangeLock] effect\nTurn End: If this unit is in Panic, change SP to 30\n\nTurn Start:\n- <color=#ff6000><mark=#ff000040><b><u>Gain Shield equal to ([FinishedFabric] Stack)% HP</u></b></mark></color> (max 30%)\n- Heal SP equal to [FinishedFabric] Stack
   PL: Na początku etapu albo na początku tury, w której ta jednostka doszła do siebie po Oszołamieniu, zyskuje 30 [FinishedFabric]\n\nstosuje efekt [PanicChangeLock]\nKoniec tury: jeżeli ta jednostka jest w Panice, jej SP wynosi 30\n\nPoczątek tury:\n- <color=#ff6000><mark=#ff000040><b><u>zyskuje Tarczę równą (Stosy [FinishedFabric])% HP</u></b></mark></color> (maks. 30%)\n- przywraca SP równe Stosom [FinishedFabric]
587. [[a1c10p2] Pasywka wroga [149503] — tekst klimatyczny] 재단은 원단을 패턴에 맞게 자르는 것. 수선이 옷을 사람에게 맞추는 과정이라면, 재단은 원단을 옷에 맞추는 과정이다.\n\n그러므로 원단에게 재단은 곧 수선과 같다. 한 번 잘려 나간 원단은 그 성질을 남긴 채, 수선사가 의도한 하나의 옷으로 못박힌다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149503].flavor
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cutting means shaping fabric to a pattern. Cutting gives a garment its form, while alteration makes it wearable.\n\nTo fabric, then, cutting itself is a form of alteration. Once cut, the fabric takes on a shape that reflects its own properties, becoming the garment the cutter intended.
   PL: Cięcie to nadawanie materiałowi kształtu zgodnego ze wzorem. Cięcie nadaje ubraniu formę, przeróbka czyni je noszalnym.\n\nDla materiału więc samo cięcie jest formą przeróbki. Gdy już zostanie pocięty, materiał przybiera kształt odzwierciedlający jego własne właściwości, stając się ubraniem, o które chodziło krojczyni.
588. [[a1c10p2] Pasywka wroga [149504] — nazwa] 끊을 수 없는 가위질
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149504].name
   limit: do 40 znaków
   EN: Scissors That Do Not Rest
   PL: Scissors That Do Not Rest
589. [[a1c10p2] Pasywka wroga [149504] — opis] 수선사 아네트가\n- <color=#ff6000><mark=#ff000040><b><u>수감자에게 피격받을 때마다 자신의 최대 체력 0.8%만큼 흐트러짐 피해를 받음</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>흐트러짐 상태가 되면,\n자신의 보호막, [FinishedFabric], [LargeTailoringShears]를 전부 잃고 [Vulnerable] 3 얻음</u></b></mark></color>\n\n턴 시작 시 자신의 체력이 60% 이하면,\n- 잃은 체력 20%당 [ResultEnhancement] 1, [SlashDamageUp] 1 얻음 (각각 최대 3)\n- ‘트리밍’의 마지막 코인, ‘커팅’의 두 번째 코인이 [SuperCoin]으로 변경됨
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149504].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [FinishedFabric], [LargeTailoringShears], [Vulnerable], [ResultEnhancement], [SlashDamageUp], [SuperCoin]
   znaczenie tagów: [FinishedFabric] = 재단된 원단 / Cut Fabric; [LargeTailoringShears] = 꽃가위 / Blossom Scissors; [Vulnerable] = 취약 / Fragile; [ResultEnhancement] = 위력 증가 / Power Up; [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Every time Annette the Alterationist is hit by a Sinner, <color=#ff6000><mark=#ff000040><b><u>raise Stagger Threshold equal to 0.8% HP</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>If this unit is Staggered, lose all Shield, [FinishedFabric], and [LargeTailoringShears]; then, gain 3 [Vulnerable]</u></b></mark></color>\n\nTurn Start: At 60% or less HP,\n- Gain 1 [ResultEnhancement] and 1 [SlashDamageUp] for every 20% missing HP (max 3 respectively)\n- Convert the final Coin of "Trimming" and Coin 2 of "Cutting" to [SuperCoin]
   PL: za każde trafienie Annette the Alterationist przez Grzesznika <color=#ff6000><mark=#ff000040><b><u>podnosi Próg Oszołomienia o wartość 0.8% HP</u></b></mark></color>\n\n<color=#ff6000><mark=#ff000040><b><u>gdy przechodzi w Oszołamienie, traci całą Tarczę, wszystkie [FinishedFabric] i [LargeTailoringShears], a następnie zyskuje 3 [Vulnerable]</u></b></mark></color>\n\nPoczątek tury: przy HP 60% lub mniej:\n- zyskuje 1 [ResultEnhancement] i 1 [SlashDamageUp] za każde 20% utraconego HP (maks. 3 każde)\n- ostatnia Moneta „Trimming” i druga Moneta „Cutting” zamieniają się w [SuperCoin]
590. [[a1c10p2] Pasywka wroga [149504] — tekst klimatyczny] 수선을 가치로 삼아 형성된 몸은, 끝없이 수선하고 재단하기 위해 가위질을 멈추지 않는다.\n\n몸이 부서져 가더라도, 수선하고 재단하는 것을 끊어낼 수는 없다. 끊어 내는 일을 하면서도, 정작 자신은 끊어 낼 수 없는 것이다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149504].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A body whose very worth was shaped by the work of alteration goes on cutting without end, driven to alter and tailor forever.\n\nEven as the body breaks apart, she cannot bring herself to stop altering and cutting. She is made to cut things away, yet cannot cut herself free.
   PL: Ciało ukształtowane z przeróbki jako wartości nie przestaje ciąć — nieustannie przerabia i kroi.\n\nNawet gdy ciało się rozpada, nie potrafi przestać przerabiać i kroić. Została stworzona, by wycinać, ale samej siebie wyciąć nie potrafi.
591. [[a1c10p2] Pasywka wroga [149505] — nazwa] 표류 관성
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149505].name
   limit: do 40 znaków
   EN: Inertia of Drifting
   PL: Inertia of Drifting
592. [[a1c10p2] Pasywka wroga [149505] — opis] 전투 중 누적으로 자신의 [ChargeKhaki] 횟수를\n10 소모할 때마다 [ChargeKhaki] 위력 1 얻음\n\n자신의 [ChargeKhaki] 위력이 3/5 이상이면,\n자신의 [ChargeKhaki] 횟수 최대치 +5/+10
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149505].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeKhaki]
   znaczenie tagów: [ChargeKhaki] = 표류 관성 / Inertia of Drifting
   EN: Gain 1 [ChargeKhaki] Potency for every 10 cumulative [ChargeKhaki] Count this unit consumes in this Encounter\n\nAt 3+/5+ [ChargeKhaki] Potency, [ChargeKhaki] Count max cap +5/+10
   PL: zyskuje 1 Siły [ChargeKhaki] za każde 10 łącznie zużytych Liczników [ChargeKhaki] tej jednostki w tej walce\n\nprzy 3+/5+ Siły [ChargeKhaki] maks. wartość Liczników [ChargeKhaki] +5/+10
593. [[a1c10p2] Pasywka wroga [149505] — tekst klimatyczny] 백화점의 시대가 만들어 낸 가치에 따라 표류하고 그 관성에 휩쓸리고 관성이 강해질수록 표류를 더욱 멈출 수 없다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149505].flavor
   limit: do 230 znaków
   EN: They drift along the values shaped by the Age of the Department Store, swept onward by their inertia; and the stronger that inertia grows, the less able they are to stop drifting.
   PL: Dryfują zgodnie z wartościami ukształtowanymi przez Erę Domu Towarowego, niesione własną inercją; im silniejsza staje się inercja, tym trudniej im przestać dryfować.
594. [[a1c10p2] Pasywka wroga [150601] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150601].name
   limit: do 40 znaków
   EN: Conservation
   PL: Conservation
595. [[a1c10p2] Pasywka wroga [150601] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를 10 소모할 때마다 [ChargeNoir] 위력 1 얻음\n[ChargeNoir] 횟수 최대치 +10
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150601].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: Gain 1 [ChargeNoir] Potency for every 10 cumulative [ChargeNoir] Count this unit consumes in this Encounter\n[ChargeNoir] Count max cap +10
   PL: zyskuje 1 Siły [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce\nmaks. wartość Liczników [ChargeNoir] +10
596. [[a1c10p2] Pasywka wroga [150602] — nazwa] 말레우스 프로미시오니스
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150602].name
   limit: do 40 znaków
   EN: Malleus Promissionis
   PL: Malleus Promissionis
597. [[a1c10p2] Pasywka wroga [150602] — opis] 자신의 공격이 적중하거나, 자신이 피격당할 때마다 자신의 [ChargeNoir] 횟수 1 증가
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150602].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: On Hit, or when hit, gain +1 [ChargeNoir] Count
   PL: przy trafieniu lub gdy ta jednostka zostanie trafiona, zyskuje 1 Licznika [ChargeNoir]
598. [[a1c10p2] Pasywka wroga [150602] — tekst klimatyczny] 망치는 못을 박는다. 이 망치가 두드리는 것은 못뿐이다. 망치에 맞는것은 못이다. 그렇게 약속 됐다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150602].flavor
   limit: do 160 znaków
   EN: A hammer drives nails. This hammer strikes nothing but nails. Whatever it strikes is a nail. That is what was agreed upon.
   PL: Młot wbija gwoździe. Ten młot uderza wyłącznie w gwoździe. W co uderzy, tym jest gwóźdź. Tak została zawarta umowa.
599. [[a1c10p2] Pasywka wroga [150603] — nazwa] 진형 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150603].name
   limit: do 40 znaków
   EN: Formation Conservation
   PL: Formation Conservation
600. [[a1c10p2] Pasywka wroga [150603] — opis] 르누아르 소속 아군의 레벨이 대폭 증가\n\n전장에 생존한 르누아르 소속 아군 1명당 모든 르누아르 소속 아군이 받는 피해량 -5%\n르누아르 소속 아군 사망시, 이번 전투 동안 모든 르누아르 소속 아군이 [NoirSquareCollapse] 1 얻음 (새로 등장하는 유닛 포함)
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150603].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSquareCollapse]
   znaczenie tagów: [NoirSquareCollapse] = 진형 붕괴 / Formation Collapse
   EN: Boost the level of "Le Noir" allies\n\nAll "Le Noir" allies take -5% damage for every living "Le Noir" ally on the field\nOn death of a "Le Noir" ally, all "Le Noir" allies gain 1 [NoirSquareCollapse] for the rest of this Encounter (including newly summoned units)
   PL: znacznie podnosi poziom sojuszników Le Noir\n\nwszyscy sojusznicy Le Noir otrzymują -5% obrażeń za każdego żywego sojusznika Le Noir na polu\npo śmierci sojusznika Le Noir wszyscy sojusznicy Le Noir zyskują 1 [NoirSquareCollapse] na resztę tej walki (łącznie z nowo przywołanymi jednostkami)
601. [[a1c10p2] Pasywka wroga [150603] — tekst klimatyczny] 하나하나 자리를 지켜 업무를 수행하고 그 모습들이 모여 하나의 진형이되고 그 진형은 전체를 보존하기 위한 도상이되니, 각자의 자리에서 맡은 바를 충실히 이행하라.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150603].flavor
   limit: do 300 znaków
   EN: Each stays at their post and faithfully performs the duty entrusted to them. Together, they form a formation, and that formation becomes an image that preserves the whole. Fulfill thy charge faithfully, each in thine appointed place.
   PL: Każdy strzeże swego stanowiska i wiernie wykonuje powierzoną mu służbę. Razem tworzą szyk, a szyk ten staje się obrazem, który zachowuje całość. Wykonuj wiernie swój obowiązek, każdy na wyznaczonym miejscu.
602. [[a1c10p2] Pasywka wroga [150401] — nazwa] 르누아르 원단
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150401].name
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [[a1c10p2] Pasywka wroga [150401] — opis] 스테이지 첫 등장 시, [NoirBindArmor] 5 얻음\n\n턴 시작 시, 자신의 최대 체력의 ([NoirBindArmor] 수치)%만큼 보호막 얻음\n\n흐트러짐 상태가 되면 [NoirBindArmor]을 모두 잃고,\n턴 시작 시 흐트러짐 상태가 해제되면 [NoirBindArmor] 5 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150401].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [NoirBindArmor]
   znaczenie tagów: [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Upon entering the Encounter for the first time, gain 5 [NoirBindArmor]\n\nTurn Start: Gain Shield equal to ([NoirBindArmor] Stack)% of this unit's max HP\n\nWhen Staggered, lose all [NoirBindArmor]\nTurn Start: When this unit recovers from Stagger, gain 5 [NoirBindArmor]
   PL: Przy pierwszym pojawieniu się w walce zyskuje 5 [NoirBindArmor]\n\nPoczątek tury: zyskuje Tarczę równą (Stosy [NoirBindArmor])% Maks. HP tej jednostki\n\ngdy staje się Oszołamiona, traci wszystkie [NoirBindArmor]\nPoczątek tury: gdy ta jednostka dochodzi do siebie po Oszołamieniu, zyskuje 5 [NoirBindArmor]
604. [[a1c10p2] Pasywka wroga [150401] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150401].flavor
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [[a1c10p2] Pasywka wroga [150402] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150402].name
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [[a1c10p2] Pasywka wroga [150402] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를 소모할 때마다 다음 효과 발동\n- 3 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 1 얻음\n\n자신의 [ChargeNoir] 위력이 3 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150402].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Apply the following effects based on cumulative [ChargeNoir] Count this unit consumes in this Encounter:\n- Gain 1 [NoirBindArmor] for every 3 cumulative [ChargeNoir] Count consumed\n- Gain 1 [ChargeNoir] for every 10 cumulative [ChargeNoir] Count consumed\n\nAt 3+ [ChargeNoir] Potency, max [ChargeNoir] Count +5
   PL: uruchamia następujące efekty, zależnie od łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce:\n- zyskuje 1 [NoirBindArmor] za każde 3 łącznie zużyte Liczniki [ChargeNoir]\n- zyskuje 1 [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir]\n\nprzy 3+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5
607. [[a1c10p2] Pasywka wroga [150402] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150402].flavor
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [[a1c10p2] Pasywka wroga [150403] — nazwa] 품질 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150403].name
   limit: do 40 znaków
   EN: Quality Preservation
   PL: Quality Preservation
609. [[a1c10p2] Pasywka wroga [150403] — opis] 보호막이 있는 동안 적에게 피격 시 [ChargeNoir] 횟수 1 증가\n\n[ChargeNoir] 횟수가 10 이상이면, 강력한 스킬 사용
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150403].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: When hit while this unit has Shield, gain +1 [ChargeNoir] Count\n\nAt 10+ [ChargeNoir] Count, use a powerful Skill
   PL: przy trafieniu, gdy ta jednostka ma Tarczę, zyskuje 1 Licznika [ChargeNoir]\n\nprzy 10+ Licznika [ChargeNoir] używa potężnej Umiejętności
610. [[a1c10p2] Pasywka wroga [150403] — tekst klimatyczny] 상품의 품질은 엄격하게 관리되고 보존되어야합니다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150403].flavor
   limit: do 120 znaków
   EN: The quality of merchandise must be strictly managed and preserved.
   PL: Jakość towarów musi być ściśle zarządzana i zachowana.
611. [[a1c10p2] Pasywka wroga [150404] — nazwa] 원단 밀도 격차
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150404].name
   limit: do 40 znaków
   EN: Fabric Density Disparity
   PL: Fabric Density Disparity
612. [[a1c10p2] Pasywka wroga [150404] — opis] [ChargeNoir] 위력이 3/5 이상이면, [Vibration] 위력 부여량 +1 /+2 증가\n\n스킬 사용 시 대상보다 방어 레벨이 높을 경우, 방어 레벨 차이 1당, 가하는 피해량 +3% (최대 30%)\n- 방어 레벨이 5 이상 높으면, 기본 위력 +1
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150404].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [Vibration]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: At 3+/5+ [ChargeNoir] Potency, inflict +1/+2 more [Vibration] Potency\n\nOn Skill Use, if this unit's Defense Level is higher than the target's, deal +3% damage for every Defense Level difference (max 30%)\n- If this unit's Defense Level is 5+ levels higher, Base Power +1
   PL: przy 3+/5+ Siły [ChargeNoir] nakłada dodatkowo +1/+2 Siły [Vibration]\n\nprzy użyciu Umiejętności, jeżeli Poziom Obrony tej jednostki jest wyższy niż celu, zadaje +3% obrażeń za każdą 1 różnicy Poziomu Obrony (maks. 30%)\n- przy Poziomie Obrony wyższym o 5+ Moc Bazowa +1
613. [[a1c10p2] Pasywka wroga [150404] — tekst klimatyczny] 르누아르는 자신의 원단 보다 무른것을 짓누른다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150404].flavor
   limit: do 120 znaków
   EN: The Noirs crush whatever is softer than their own fabric.
   PL: Le Noir miażdży wszystko, co miększe niż jego własna tkanina.
614. [[a1c10p2] Pasywka wroga [150501] — nazwa] 르누아르 원단
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150501].name
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [[a1c10p2] Pasywka wroga [150501] — opis] 스테이지 첫 등장 시, [NoirBindArmor] 5 얻음\n\n턴 시작 시, 자신의 최대 체력의 ([NoirBindArmor] 수치)%만큼 보호막 얻음\n\n흐트러짐 상태가 되면 [NoirBindArmor]을 모두 잃고,\n턴 시작 시 흐트러짐 상태가 해제되면 [NoirBindArmor] 5 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150501].desc
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [[a1c10p2] Pasywka wroga [150501] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150501].flavor
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [[a1c10p2] Pasywka wroga [150502] — nazwa] 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150502].name
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [[a1c10p2] Pasywka wroga [150502] — opis] 전투 중 누적으로 자신의 [ChargeNoir] 횟수를 소모할 때마다 다음 효과 발동\n- 3 소모할 때마다 [NoirBindArmor] 1 얻음\n- 10 소모할 때마다 [ChargeNoir] 1 얻음\n\n자신의 [ChargeNoir] 위력이 3 이상이면, 자신의 [ChargeNoir] 횟수 최대치 +5
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150502].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [NoirBindArmor]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [NoirBindArmor] = 르누아르 우스티드 원단 / Le Noir: Worsted
   EN: Apply the following effects based on cumulative [ChargeNoir] Count this unit consumes in this Encounter:\n- Gain 1 [NoirBindArmor] for every 3 cumulative [ChargeNoir] Count consumed\n- Gain 1 [ChargeNoir] for every 10 cumulative [ChargeNoir] Count consumed\n\nAt 3+ [ChargeNoir] Potency, [ChargeNoir] Count max cap +5
   PL: uruchamia następujące efekty, zależnie od łącznie zużytych Liczników [ChargeNoir] tej jednostki w tej walce:\n- zyskuje 1 [NoirBindArmor] za każde 3 łącznie zużyte Liczniki [ChargeNoir]\n- zyskuje 1 [ChargeNoir] za każde 10 łącznie zużytych Liczników [ChargeNoir]\n\nprzy 3+ Siły [ChargeNoir] maks. wartość Liczników [ChargeNoir] +5
619. [[a1c10p2] Pasywka wroga [150502] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150502].flavor
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [[a1c10p2] Pasywka wroga [150503] — nazwa] 검수 보존
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150503].name
   limit: do 40 znaków
   EN: Inspection Preservation
   PL: Inspection Preservation
621. [[a1c10p2] Pasywka wroga [150503] — opis] [ChargeNoir] 횟수가 10 이상이면, 강력한 스킬 사용
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150503].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: At 10+ [ChargeNoir] Count, use a powerful Skill
   PL: przy 10+ Licznika [ChargeNoir] używa potężnej Umiejętności
622. [[a1c10p2] Pasywka wroga [150503] — tekst klimatyczny] 품질을 위해 검수절차를 밟고 이 과정에서 보존이 망가져서는 안됩니다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150503].flavor
   limit: do 120 znaków
   EN: Quality must pass inspection, and preservation must not be compromised in the process.
   PL: Jakość musi przejść kontrolę, a w tym procesie zachowanie nie może ucierpieć.
623. [[a1c10p2] Pasywka wroga [150504] — nazwa] 원단 밀도 격차
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150504].name
   (powtórzenie elementu 611 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [[a1c10p2] Pasywka wroga [150504] — opis] [ChargeNoir] 위력이 3/5 이상이면, [Vibration] 위력 부여량 +1 /+2 증가\n\n공격 스킬 사용 시 대상보다 방어 레벨이 높을 경우, 방어 레벨 차이 1당, 가하는 피해량 +3% (최대 30%)\n- 방어 레벨이 5 이상 높으면, 기본 위력 +1
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150504].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir], [Vibration]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation; [Vibration] = 진동 / Tremor
   EN: At 3+/5+ [ChargeNoir] Potency, inflict +1/+2 more [Vibration] Potency\n\nOn Attack Skill Use, if this unit's Defense Level is higher than the target's, deal +3% damage for every Defense Level difference (max 30%)\n- If this unit's Defense Level is 5+ levels higher, Base Power +1
   PL: przy 3+/5+ Siły [ChargeNoir] nakłada dodatkowo +1/+2 Siły [Vibration]\n\nprzy użyciu Umiejętności ataku, jeżeli Poziom Obrony tej jednostki jest wyższy niż celu, zadaje +3% obrażeń za każdą 1 różnicy Poziomu Obrony (maks. 30%)\n- przy Poziomie Obrony wyższym o 5+ Moc Bazowa +1
625. [[a1c10p2] Pasywka wroga [150504] — tekst klimatyczny] 르누아르는 자신의 원단 보다 무른것을 짓누른다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150504].flavor
   limit: do 120 znaków
   EN: Le Noir crushes whatever is softer than their own fabric.
   PL: Le Noir miażdży wszystko, co miększe niż ich własna tkanina.
626. [[a1c10p2] Pasywka wroga [148801] — nazwa] 원죄적 원피수급
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148801].name
   limit: do 50 znaków
   EN: Reaping Raw Hide: Original Sin Style
   PL: Reaping Raw Hide: Original Sin Style
627. [[a1c10p2] Pasywka wroga [148801] — opis] 턴 시작시 전장에 존재하는 무두질된 죄수가 2개체 이하면, 추가 슬롯 생성\n턴 종료시 <color=#ff6000><mark=#ff000040><b><u>전장에 존재하는 무두질된 죄수</u></b></mark></color> 1개체당, 다음 턴에 [AttackDmgUp] 1 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148801].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: When there are 2 or fewer Tanned Prisoners on the field, gain additional Slot\nTurn End: Gain 1 [AttackDmgUp] next turn for every <color=#ff6000><mark=#ff000040><b><u>Tanned Prisoner on the field</u></b></mark></color>
   PL: Początek tury: jeżeli na polu jest 2 lub mniej Tanned Prisoner, tworzy dodatkowy slot\nKoniec tury: zyskuje 1 [AttackDmgUp] w następnej turze za każdego <color=#ff6000><mark=#ff000040><b><u>Tanned Prisoner na polu</u></b></mark></color>
628. [[a1c10p2] Pasywka wroga [148801] — tekst klimatyczny] 죄인의 가죽을 뜯어내고 붙어있는 죄를 긁어내어 가죽을 수급한다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148801].flavor
   limit: do 160 znaków
   EN: The transgressor's hide is torn away, and the sin clinging to it is scraped clean, leaving only the hide to be harvested.
   PL: Skórę przestępcy zdejmuje się i zdrapuje z niej grzech, który się na niej przywarował — pozostaje tylko skóra do zbioru.
629. [[a1c10p2] Pasywka wroga [148802] — nazwa] 재무두질 준비
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148802].name
   limit: do 40 znaków
   EN: Retanning Preparation
   PL: Retanning Preparation
630. [[a1c10p2] Pasywka wroga [148802] — opis] 전장에 자신을 제외하고 현재 체력이 최대 체력의 80% 미만인 아군이 있으면 추가 슬롯 생성
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148802].desc
   limit: do 130 znaków
   EN: Gain additional Slot when there is an ally, excluding this unit, with less than 80% HP on the field
   PL: tworzy dodatkowy slot, jeżeli na polu jest sojusznik — z wyłączeniem tej jednostki — mający mniej niż 80% HP
631. [[a1c10p2] Pasywka wroga [148802] — tekst klimatyczny] 다시 죄로 더럽혀진 가죽은 태너리로 회수하여 다시 무두질을 한다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148802].flavor
   limit: do 130 znaków
   EN: Once sin seeps back into the leather, the Tannery takes it in and works it clean all over again.
   PL: Gdy grzech ponownie przesiąknie skórę, garbarnia odbiera ją i garbuje od nowa.
632. [[a1c10p2] Pasywka wroga [148803] — nazwa] 원죄가죽 태너리 풀 가동
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148803].name
   limit: do 60 znaków
   EN: Tannery of the Original Sin: Full Operation
   PL: Tannery of the Original Sin: Full Operation
633. [[a1c10p2] Pasywka wroga [148803] — opis] 자신의 본체 체력이 최대 체력의 50% 미만이 되면, 턴을 종료하고 패턴이 변경되며, 자신을 포함한 모든 아군이 이번 전투 동안 [RestrictFailed]를 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148803].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [RestrictFailed]
   znaczenie tagów: [RestrictFailed] = 규칙의 붕괴 / Rule Collapse
   EN: At less than 50% Core HP, end the turn and enter a new pattern; all allies, including this unit, gain [RestrictFailed] for the rest of this Encounter
   PL: gdy HP rdzenia tej jednostki spadnie poniżej 50% Maks. HP, kończy turę, przechodzi do nowego wzorca, a wszyscy sojusznicy — łącznie z tą jednostką — zyskują [RestrictFailed] na resztę tej walki
634. [[a1c10p2] Pasywka wroga [148803] — tekst klimatyczny] 가죽 수요 폭주. 원피 수급의 어려움. 원죄 가죽은 한때 쳐다보지도 않던 종류의 가죽이었지만 어떤 시즌을 계기로 수요가 폭주하여 가격이 높아져버렸다. 분명 예전에는 헐값에 팔리거나 폐기되거나하는 가죽이었다. 이제는 원죄 가죽 표면의 하자까지 감성의 영역으로 포장되어 소비된다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148803].flavor
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Demand has gone through the roof, while raw hides have only grown harder to come by. The hide of the original sinners was once the sort nobody would so much as glance at. Then one season changed everything: demand surged, prices soared, and what used to be sold for scraps or simply thrown away became coveted material.\n\nNow even the blemishes on its surface are dressed up as character and sold as part of the appeal.
   PL: Popyt eksplodował, a skór surowych coraz trudniej zdobyć. Skóra grzeszników pierworodnych była niegdyś tego rodzaju, na który nikt nie chciał patrzeć. Potem jeden sezon zmienił wszystko: popyt wystrzelił, ceny poszybowały, a to, co kiedyś sprzedawano za grosze albo wyrzucano, stało się pożądanym materiałem.\n\nDziś nawet skazy na powierzchni skóry pierworodnego grzechu opakowuje się w estetykę i sprzedaje jako część jej uroku.
635. [[a1c10p2] Pasywka wroga [148804] — nazwa] 태너리 규칙
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148804].name
   limit: do 40 znaków
   EN: Rules of the Tannery
   PL: Rules of the Tannery
636. [[a1c10p2] Pasywka wroga [148804] — opis] 2턴부터 매 턴 시작시 무작위 적 3명에게 아래 효과 중 하나를 무작위로 부여함\n- [RestrictMob]\n- [RestrictBoss]\n- [RestrictTier1]\n- [RestrictDef]\n\n규칙 위반시, [RestrictDenied] 1 부여
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148804].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [RestrictMob], [RestrictBoss], [RestrictTier1], [RestrictDef], [RestrictDenied]
   znaczenie tagów: [RestrictMob] = 규칙: 원피 손상 금지 / Rule: Raw Hide Damage Prohibited; [RestrictBoss] = 규칙: 무두질 재촉 금지 / Rule: Tanning Rush Prohibited; [RestrictTier1] = 규칙: 공격적 태도 금지 / Rule: Offensive Behavior Prohibited; [RestrictDef] = 규칙: 방어적 태도 금지 / Rule: Defensive Behavior Prohibited; [RestrictDenied] = 태너리 규칙 위반 / Tannery Rule Violation
   EN: Starting from Turn 2, randomly inflict 1 of the following effects on 3 random enemies at the start of each turn\n- [RestrictMob]\n- [RestrictBoss]\n- [RestrictTier1]\n- [RestrictDef]\n\nWhen a Rule is violated, inflict 1 [RestrictDenied]
   PL: od tury 2 na początku każdej tury nakłada losowo 1 z poniższych efektów na 3 losowych wrogów\n- [RestrictMob]\n- [RestrictBoss]\n- [RestrictTier1]\n- [RestrictDef]\n\nprzy naruszeniu reguły nakłada 1 [RestrictDenied]
637. [[a1c10p2] Pasywka wroga [148804] — tekst klimatyczny] 고깃덩이와 가죽을 구분하는 것은 엄정한 무두질 절차와 규칙하에 구분지어진다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148804].flavor
   limit: do 130 znaków
   EN: What separates a slab of meat from hide is a strict regime of tanning, governed by exacting rules.
   PL: To, co oddziela bryłę mięsa od skóry, to rygorystyczny reżim garbowania, rządzony bezlitosnymi regułami.
638. [[a1c10p2] Pasywka wroga [149101] — nazwa] 무두질된 죄수
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149101].name
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [[a1c10p2] Pasywka wroga [149101] — opis] 사망 시, 이번 전투 동안 통제자의 방어 레벨이 영구적으로 1 감소
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149101].desc
   limit: do 120 znaków
   EN: On Death, the Overseer permanently loses 1 Defense Level for the rest of this Encounter
   PL: po śmierci Poziom Obrony The Overseer trwale maleje o 1 na resztę tej walki
640. [[a1c10p2] Pasywka wroga [150604] — nazwa] 전투 속행
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150604].name
   limit: do 40 znaków
   EN: The Battle Continues
   PL: The Battle Continues
641. [[a1c10p2] Pasywka wroga [150604] — opis] 스테이지 시작시, 체력이 80%, 정신력이 45인 상태로 시작
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=150604].desc
   limit: do 120 znaków
   EN: Start this Encounter with 80% HP and 45 SP
   PL: rozpoczyna tę walkę z 80% HP i 45 SP
642. [[a1c10p2] Pasywka wroga [151001] — nazwa] 봉제시작
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151001].name
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [[a1c10p2] Pasywka wroga [151001] — opis] 턴 시작시, 무작위 적 2명에게 [NiddleExpected] 부여
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151001].desc
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [[a1c10p2] Pasywka wroga [151002] — nazwa] 핸드메이드
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151002].name
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [[a1c10p2] Pasywka wroga [151002] — opis] 전장의 바늘이[TabExplain] 1개당 스킬 최종 위력 +1
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151002].desc
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [[a1c10p2] Pasywka wroga [151002] — tekst klimatyczny] 손 바느질은 숙련된 기능공들의 수가 생명이다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151002].flavor
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [[a1c10p2] Pasywka wroga [151003] — nazwa] 귀를 막아도 보이는 클레임
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151003].name
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [[a1c10p2] Pasywka wroga [151003] — opis] 3배수 턴마다 고치의 울음소리가 들림\n2페이즈 진입시 고치의 울음소리가 매 턴 지속됨\n\n고치의 울음소리가 들리는 턴에는 행동불가상태에 면역\n\n흐트러짐 구간을 지나면 다음 턴에 [Vulnerable] 2 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151003].desc
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [[a1c10p2] Pasywka wroga [151003] — tekst klimatyczny] 고치에서 소리가 들려온다.\n‘80수 2합 아래는 원단 취급 안함.’ ‘단추구멍 왜 가로 아님?’\n‘구직기에 천축인가요?’ ‘셀비지 색 왜 빨간색 아니에요?’\n‘이거 방축가공처리 안됐네.’ ‘Super 150이하면 싸구려 원단이죠’\n‘Super 넘버가 그냥 실 굵기라고요? 직경이랑 번수랑 다른데 그것도 모르시네.’\n‘유니온스페셜로 당연히 처리 밑단 처리해주죠?’ ‘이거 리지드에요? 아, 셀비지인가?’\n‘자세히보니까 땀수가 너무 균일하네. 기계썼죠?’ ‘손 바느질 아니면 비스포크 아님.’\n‘아 이거 홀 밀라네제 아니네.’ ‘번수가 200은 넘어야 셔츠 원단이죠.’\n‘아 겉에 박음선 보이네.’ ‘박음선 두 줄 보이네. 탈락.’\n‘시접처리 왜 이래.’ ‘3플라이는 넘겨줘야지’
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151003].flavor
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [[a1c10p2] Pasywka wroga [149604] — nazwa] 따갑게 내리쬐는 햇살
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149604].name
   limit: do 40 znaków
   EN: Shower of Stinging Sunshine
   PL: Shower of Stinging Sunshine
651. [[a1c10p2] Pasywka wroga [149604] — opis] 햇살의 영향으로 레벨이 증가한 상태\n\n스테이지 시작시, [GoldenLeatherEnhance] 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149604].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [GoldenLeatherEnhance]
   znaczenie tagów: [GoldenLeatherEnhance] = 따갑게 내리쬐는 햇살[바느질의 왕] / Shower of Stinging Sunshine [King of Needleworks]
   EN: This unit's level is raised due to the influence of the sunshine\n\nEncounter Start: Gain [GoldenLeatherEnhance]
   PL: poziom tej jednostki jest podniesiony pod wpływem słońca\n\nNa początku etapu: zyskuje [GoldenLeatherEnhance]
652. [[a1c10p2] Pasywka wroga [149604] — tekst klimatyczny] 햇빛의 온기에 귀 기울인 자들에게 햇살은 더욱 따갑고 눈부시고 강렬하게 들려온다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149604].flavor
   limit: do 150 znaków
   EN: To those who heed the warmth of the sunlight, its shine rings out all the more searing, dazzling, and intense.
   PL: Tym, którzy wsłuchują się w ciepło promieni słonecznych, blask brzmi tym bardziej przypiekająco, olśniewająco i intensywnie.
653. [[a1c10p2] Pasywka wroga [148805] — nazwa] 전투 속행
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148805].name
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [[a1c10p2] Pasywka wroga [148805] — opis] 스테이지 시작시, 체력이 90%, 정신력이 45인 상태로 시작
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148805].desc
   limit: do 120 znaków
   EN: Start this Encounter with 90% HP and 45 SP
   PL: rozpoczyna tę walkę z 90% HP i 45 SP
655. [[a1c10p2] Pasywka wroga [148305] — nazwa] 따갑게 내리쬐는 햇살
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148305].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [[a1c10p2] Pasywka wroga [148305] — opis] 따갑게 내리쬐는 햇살의 영향으로 레벨이 상승한 상태\n\n스테이지 시작 시 [ChargeNoir] 위력 2, 횟수 15 얻음\n\n스테이지 시작 시 정신력 30으로 시작하고, 비휘발성 보호막 1000 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148305].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: This unit's level is raised due to the influence of the shower of stinging sunshine\n\nEncounter Start: Gain 2 [ChargeNoir] Potency and +15 [ChargeNoir] Count\n\nStart the Encounter with 30 SP and 1000 persistent Shield
   PL: poziom tej jednostki jest podniesiony pod wpływem Shower of Stinging Sunshine\n\nNa początku etapu: zyskuje 2 Siły [ChargeNoir] i +15 Licznika [ChargeNoir]\n\nrozpoczyna tę walkę z 30 SP i 1000 trwałej Tarczy
657. [[a1c10p2] Pasywka wroga [148305] — tekst klimatyczny] 햇빛의 온기에 귀 기울인 자들에게 햇살은 더욱 따갑고 눈부시고 강렬하게 들려온다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=148305].flavor
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [[a1c10p2] Pasywka wroga [1590001] — nazwa] 따갑게 내리쬐는 햇살
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=1590001].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [[a1c10p2] Pasywka wroga [1590001] — opis] 햇살의 영향으로 레벨이 증가한 상태
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=1590001].desc
   limit: do 120 znaków
   EN: This unit's level is raised due to the influence of the sunshine
   PL: poziom tej jednostki jest podniesiony pod wpływem słońca
660. [[a1c10p2] Pasywka wroga [1590001] — tekst klimatyczny] 햇빛의 온기에 귀 기울인 자들에게 햇살은 더욱 따갑고 눈부시고 강렬하게 들려온다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=1590001].flavor
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [[a1c10p2] Pasywka wroga [149608] — nazwa] 귀를 막아도 보이는 클레임
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149608].name
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [[a1c10p2] Pasywka wroga [149608] — opis] 고치의 울음소리가 매 턴 지속됨\n행동불가상태에 면역
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=149608].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: "Cry of the Cocoon" continues to be heard every turn\nCannot be immobilized[TabExplain]
   PL: „Cry of the Cocoon” słychać w każdej turze\nnie może zostać unieruchomiona[TabExplain]
663. [[a1c10p2] Pasywka wroga [151101] — nazwa] 따갑게 내리쬐는 햇살
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151101].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [[a1c10p2] Pasywka wroga [151101] — opis] 따갑게 내리쬐는 햇살의 영향으로 레벨이 상승한 상태\n스테이지 시작 시 [SapsareeGold] 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151101].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [SapsareeGold]
   znaczenie tagów: [SapsareeGold] = 따갑게 내리쬐는 햇살[수셰프] / Shower of Stinging Sunshine [Sous Chef]
   EN: This unit's level is raised due to the influence of the shower of stinging sunshine\n\nEncounter Start: Gain [SapsareeGold]
   PL: poziom tej jednostki jest podniesiony pod wpływem Shower of Stinging Sunshine\nNa początku etapu: zyskuje [SapsareeGold]
665. [[a1c10p2] Pasywka wroga [151101] — tekst klimatyczny] 햇빛의 온기에 귀 기울인 자들에게 햇살은 더욱 따갑고 눈부시고 강렬하게 들려온다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151101].flavor
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [[a1c10p2] Pasywka wroga [151201] — nazwa] 따갑게 내리쬐는 햇살
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151201].name
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [[a1c10p2] Pasywka wroga [151201] — opis] 따갑게 내리쬐는 햇살의 영향으로 레벨이 상승한 상태\n스테이지 시작 시 체력을 전부 회복하고, [GoldenManager] 얻음
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151201].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [GoldenManager]
   znaczenie tagów: [GoldenManager] = 따갑게 내리쬐는 햇살[3층 플로어 매니저] / Shower of Stinging Sunshine [3F Floor Manager]
   EN: This unit's level is raised due to the influence of the shower of stinging sunshine\n\nEncounter Start: Heal all HP and gain [GoldenManager]
   PL: poziom tej jednostki jest podniesiony pod wpływem Shower of Stinging Sunshine\n\nNa początku etapu: przywraca całe HP i zyskuje [GoldenManager]
668. [[a1c10p2] Pasywka wroga [151201] — tekst klimatyczny] 햇빛의 온기에 귀 기울인 자들에게 햇살은 더욱 따갑고 눈부시고 강렬하게 들려온다.
   źródło: Passives_Abnormality-a1c10p2.json :: dataList[id=151201].flavor
   (powtórzenie elementu 652 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p3] Wróg / część: Enemies-a1c10p3
- plik gry: `Enemies-a1c10p3.json`

669. [[a1c10p3] Wróg / część [1485] — nazwa] 간수
   źródło: Enemies-a1c10p3.json :: dataList[id=1485].name
   limit: do 40 znaków
   EN: The Warden
   PL: The Warden
670. [[a1c10p3] Wróg / część [148501] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=148501].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [[a1c10p3] Wróg / część [1486] — nazwa] 간수
   źródło: Enemies-a1c10p3.json :: dataList[id=1486].name
   (powtórzenie elementu 669 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [[a1c10p3] Wróg / część [148601] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=148601].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [[a1c10p3] Wróg / część [1487] — nazwa] 신부
   źródło: Enemies-a1c10p3.json :: dataList[id=1487].name
   limit: do 40 znaków
   EN: The Chaplain
   PL: The Chaplain
674. [[a1c10p3] Wróg / część [148701] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=148701].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [[a1c10p3] Wróg / część [1520] — nazwa] 형벌 촛대
   źródło: Enemies-a1c10p3.json :: dataList[id=1520].name
   limit: do 40 znaków
   EN: Candle of Retribution
   PL: Candle of Retribution
676. [[a1c10p3] Wróg / część [152001] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152001].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [[a1c10p3] Wróg / część [1522] — nazwa] 재단사 잔느 사르트르
   źródło: Enemies-a1c10p3.json :: dataList[id=1522].name
   limit: do 50 znaków
   EN: Jeanne Sartre, the Sartorial Tailor
   PL: Jeanne Sartre, the Sartorial Tailor
678. [[a1c10p3] Wróg / część [152201] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152201].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [[a1c10p3] Wróg / część [1523] — nazwa] 잔느 마리 사르트르
   źródło: Enemies-a1c10p3.json :: dataList[id=1523].name
   limit: do 40 znaków
   EN: Jeanne-Marie Sartre
   PL: Jeanne-Marie Sartre
680. [[a1c10p3] Wróg / część [152301] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152301].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [[a1c10p3] Wróg / część [1524] — nazwa] 물랑루주 - 잔느 마리 사르트르
   źródło: Enemies-a1c10p3.json :: dataList[id=1524].name
   limit: do 50 znaków
   EN: Moulin Rouge - Jeanne-Marie Sartre
   PL: Moulin Rouge - Jeanne-Marie Sartre
682. [[a1c10p3] Wróg / część [152401] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152401].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [[a1c10p3] Wróg / część [1525] — nazwa] 시지프 백화점 설계도
   źródło: Enemies-a1c10p3.json :: dataList[id=1525].name
   limit: do 50 znaków
   EN: Grand Magasin Sisyphe Blueprint
   PL: Grand Magasin Sisyphe Blueprint
684. [[a1c10p3] Wróg / część [152501] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152501].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [[a1c10p3] Wróg / część [1526] — nazwa] 시지프 시스템 설계도 - 르루주
   źródło: Enemies-a1c10p3.json :: dataList[id=1526].name
   limit: do 50 znaków
   EN: Sisyphe System Blueprint - Le Rouge
   PL: Sisyphe System Blueprint - Le Rouge
686. [[a1c10p3] Wróg / część [152601] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152601].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [[a1c10p3] Wróg / część [1527] — nazwa] 시지프 시스템 설계도 - 르누아르
   źródło: Enemies-a1c10p3.json :: dataList[id=1527].name
   limit: do 50 znaków
   EN: Sisyphe System Blueprint - Le Noir
   PL: Sisyphe System Blueprint - Le Noir
688. [[a1c10p3] Wróg / część [152701] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152701].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [[a1c10p3] Wróg / część [1517] — nazwa] 붉은 신[완숙]
   źródło: Enemies-a1c10p3.json :: dataList[id=1517].name
   limit: do 40 znaków
   EN: The Crimson God [Adulthood]
   PL: The Crimson God [Adulthood]
690. [[a1c10p3] Wróg / część [151701] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=151701].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [[a1c10p3] Wróg / część [1518] — nazwa] 붉은 신의 뜯긴 살점
   źródło: Enemies-a1c10p3.json :: dataList[id=1518].name
   limit: do 50 znaków
   EN: Ripped Flesh of the Crimson God
   PL: Ripped Flesh of the Crimson God
692. [[a1c10p3] Wróg / część [151801] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=151801].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [[a1c10p3] Wróg / część [1521] — nazwa] 르루주 고위 스태프
   źródło: Enemies-a1c10p3.json :: dataList[id=1521].name
   limit: do 40 znaków
   EN: Le Rouge Senior Staff
   PL: Le Rouge Senior Staff
694. [[a1c10p3] Wróg / część [152101] — nazwa] 몸통
   źródło: Enemies-a1c10p3.json :: dataList[id=152101].name
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [a1c10p3] Umiejętności wrogów / Anomalii — Skills_Abnormality-a1c10p3
- grupa rozdziału/trybu: `a1c10p3` · plik: `Skills_Abnormality-a1c10p3.json`

695. [Umiejętność wroga [148501] (ulepszenie 1) — nazwa] 죄를 범했군…
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148501].levelList[level=1].name
   limit: do 40 znaków
   EN: Thou hast sinned...
   PL: Thou hast sinned...
696. [Umiejętność wroga [148501] (ulepszenie 1) — opis] [WhenUse]\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 1당, 최종 위력 +1 (최대 4)</u></b></mark></color>\n- 자신의 [ChargeNoir] 횟수가 10 이상이면, 합 위력 +1\n[WhenUse] 자신의 [ChargeNoir] 횟수 3 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148501].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse]\n- <color=#ff6000><mark=#ff000040><b><u>Final Power +1 for every Candle of Retribution on the field</u></b></mark></color> (max 4)\n- At 10+ [ChargeNoir] Count, Clash Power +1\n[WhenUse] Gain +3 [ChargeNoir] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse]\n- <color=#ff6000><mark=#ff000040><b><u>Moc Końcowa +1 za każdą 1 Candle of Retribution na polu</u></b></mark></color> (maks. 4)\n- przy 10+ Licznika [ChargeNoir] Moc Starcia +1\n[WhenUse] zyskuje 3 Licznika [ChargeNoir]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
697. [Umiejętność wroga [148501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność wroga [148501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność wroga [148502] (ulepszenie 1) — nazwa] 뉘우쳐라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].name
   limit: do 40 znaków
   EN: Atone.
   PL: Atone.
700. [Umiejętność wroga [148502] (ulepszenie 1) — opis] [WhenUse]\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 1당, 최종 위력 +2 (최대 8)</u></b></mark></color>\n- 자신의 [ChargeNoir] 횟수가 15 이상이면, 5 소모하여 최종 위력 +2\n[WhenUse] 자신의 [ChargeNoir] 횟수 5 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse]\n- <color=#ff6000><mark=#ff000040><b><u>Final Power +2 for every Candle of Retribution on the field</u></b></mark></color> (max 8)\n- At 15+ [ChargeNoir] Count, consume 5 [ChargeNoir] Count to gain Final Power +2\n[WhenUse] Gain +5 [ChargeNoir] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse]\n- <color=#ff6000><mark=#ff000040><b><u>Moc Końcowa +2 za każdą 1 Candle of Retribution na polu</u></b></mark></color> (maks. 8)\n- przy 15+ Licznika [ChargeNoir] zużywa 5 Licznika [ChargeNoir], aby zyskać Moc Końcową +2\n[WhenUse] zyskuje 5 Licznika [ChargeNoir]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
701. [Umiejętność wroga [148502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność wroga [148502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Umiejętność wroga [148502] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking]
704. [Umiejętność wroga [148502] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[Binding] 1 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148502].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [Binding]</u></b></mark></color> next turn
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 1 [Binding]</u></b></mark></color> w następnej turze
705. [Umiejętność wroga [148503] (ulepszenie 1) — nazwa] 단죄
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].name
   limit: do 40 znaków
   EN: Condemnation
   PL: Condemnation
706. [Umiejętność wroga [148503] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BeforeAttack] 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 수만큼 공격 가중치 증가 (최대 2)</u></b></mark></color>\n[WhenUse]\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>속도가 1</u></b></mark></color>이면, 피해량 +50%\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 1당, 최종 위력 +2 (최대 8)</u></b></mark></color>\n- 자신의 [ChargeNoir] 횟수가 15 이상이면, 10 소모하여 코인 위력 +1\n[DefeatDuel] [Paralysis] 3 얻음, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BeforeAttack], [WhenUse], [ChargeNoir], [DefeatDuel], [Paralysis]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>Gain +(# of Candle of Retribution on the field) Atk Weight (max 2)</u></b></mark></color>\n[WhenUse]\n- If the main target <color=#ff6000><mark=#ff000040><b><u>has 1 Speed</u></b></mark></color>, deal +50% damage\n- <color=#ff6000><mark=#ff000040><b><u>Final Power +2 for every Candle of Retribution on the field (max 8)</u></b></mark></color>\n- At 15+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Coin Power +1\n[DefeatDuel] Gain 3 [Paralysis], deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>zyskuje Wagę Ataku równą liczbie Candle of Retribution na polu (maks. 2)</u></b></mark></color>\n[WhenUse]\n- jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>Szybkość 1</u></b></mark></color>, zadaje +50% obrażeń\n- <color=#ff6000><mark=#ff000040><b><u>Moc Końcowa +2 za każdą 1 Candle of Retribution na polu (maks. 8)</u></b></mark></color>\n- przy 15+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Monety +1\n[DefeatDuel] zyskuje 3 [Paralysis], zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
707. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 [Sinking] i 1 Licznika [Sinking]
708. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 3 [Sinking] i 2 Licznika [Sinking]
709. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[Binding] 2 부여</u></b></mark></color>\n- 메인 타겟이면, 대신 <color=#ff6000><mark=#ff000040><b><u>[Binding] 4 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 2 [Binding]</u></b></mark></color> next turn\n- <color=#ff6000><mark=#ff000040><b><u>Inflict 4 [Binding]</u></b></mark></color> instead to main targets
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 2 [Binding]</u></b></mark></color> w następnej turze\n- na głównym celu zamiast tego <color=#ff6000><mark=#ff000040><b><u>nakłada 4 [Binding]</u></b></mark></color>
711. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 3, efekt 2 — podsumowanie] 다음 턴에 [Binding] 2 부여, 메인 타겟이면 대신 4 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#2].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Inflict 2 [Binding] next turn; 4 instead on the main target
   PL: nakłada 2 [Binding] w następnej turze; na głównym celu zamiast tego 4
712. [Umiejętność wroga [148503] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148503].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking] and +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking] i 3 Licznika [Sinking]
713. [Umiejętność wroga [148504] (ulepszenie 1) — nazwa] 죄악감이 그대를 옥죈다
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].name
   limit: do 50 znaków
   EN: Your sinfulness shall constrict you.
   PL: Your sinfulness shall constrict you.
714. [Umiejętność wroga [148504] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[BeforeAttack] 전장의 형벌 촛대 수만큼 공격 가중치 증가 (최대 4)\n[WhenUse]\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>속도가 1</u></b></mark></color>이면, 피해량 +100%\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 1당, 최종 위력 +2 (최대 8)</u></b></mark></color>\n- 전장에 형벌 촛대가 없으면, 합 위력 -3\n- 자신의 [ChargeNoir] 횟수가 15 이상이면, 10 소모하여 최종 위력 +1, 코인 위력 +1\n[DefeatDuel] [Paralysis] 4 얻음, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [BeforeAttack], [WhenUse], [ChargeNoir], [DefeatDuel], [Paralysis]
   znaczenie tagów: [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\n[BeforeAttack] Gain +(# of Candle of Retribution on the field) Atk Weight (max 4)\n[WhenUse]\n- If the main target <color=#ff6000><mark=#ff000040><b><u>has 1 Speed</u></b></mark></color>, deal +100% damage\n- <color=#ff6000><mark=#ff000040><b><u>Final Power +2 for every Candle of Retribution on the field (max 8)</u></b></mark></color>\n- If there are no Candle of Retribution on the field, Clash Power -3\n- At 15+ [ChargeNoir] Count, consume 10 [ChargeNoir] Count to gain Final Power +1 and Coin Power +1\n[DefeatDuel] Gain 4 [Paralysis], deal -50% damage, and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[BeforeAttack] zyskuje Wagę Ataku równą liczbie Candle of Retribution na polu (maks. 4)\n[WhenUse]\n- jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>Szybkość 1</u></b></mark></color>, zadaje +100% obrażeń\n- <color=#ff6000><mark=#ff000040><b><u>Moc Końcowa +2 za każdą 1 Candle of Retribution na polu (maks. 8)</u></b></mark></color>\n- jeżeli na polu nie ma Candle of Retribution, Moc Starcia -3\n- przy 15+ Licznika [ChargeNoir] zużywa 10 Licznika [ChargeNoir], aby zyskać Moc Końcową +1 i Moc Monety +1\n[DefeatDuel] zyskuje 4 [Paralysis], zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
715. [Umiejętność wroga [148504] (ulepszenie 1) — tekst klimatyczny] ‘마네킹들은 지저귀고…’
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].flavor
   limit: do 120 znaków
   EN: "Mannequins are singing..."
   PL: "Mannequins are singing..."
716. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[Binding] 1 부여</u></b></mark></color>\n- 메인 타겟이면, 대신 <color=#ff6000><mark=#ff000040><b><u>[Binding] 3 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 1 [Binding]</u></b></mark></color> next turn\n- <color=#ff6000><mark=#ff000040><b><u>Inflict 3 [Binding]</u></b></mark></color> instead to main targets
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 1 [Binding]</u></b></mark></color> w następnej turze\n- na głównym celu zamiast tego <color=#ff6000><mark=#ff000040><b><u>nakłada 3 [Binding]</u></b></mark></color>
718. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 1, efekt 2 — podsumowanie] 다음 턴에 [Binding] 1 부여, 메인 타겟이면 대신 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#0].coindescs[#1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Inflict 1 [Binding] next turn; 3 instead on the main target
   PL: nakłada 1 [Binding] w następnej turze; na głównym celu zamiast tego 3
719. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Sinking]
720. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 <color=#ff6000><mark=#ff000040><b><u>[Binding] 1 부여</u></b></mark></color>\n- 메인 타겟이면, 대신 <color=#ff6000><mark=#ff000040><b><u>[Binding] 3 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 717 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 2, efekt 2 — podsumowanie] 다음 턴에 [Binding] 1 부여, 메인 타겟이면 대신 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#1].coindescs[#1].summary
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking] i 2 Licznika [Sinking]
726. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Umiejętność wroga [148504] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [BlackStigmata] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148504].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BlackStigmata]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackStigmata] = 죄악감 / Compunction
   EN: [OnSucceedAttack] Inflict 2 [BlackStigmata] next turn
   PL: [OnSucceedAttack] nakłada 2 [BlackStigmata] w następnej turze
728. [Umiejętność wroga [148505] (ulepszenie 1) — nazwa] 징벌
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].name
   limit: do 40 znaków
   EN: Divine Retribution
   PL: Divine Retribution
729. [Umiejętność wroga [148505] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse]\n- 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>속도가 1</u></b></mark></color>이면, 피해량 +100%\n- 전장의 <color=#ff6000><mark=#ff000040><b><u>형벌 촛대 1당, 최종 위력 +2 (최대 8)</u></b></mark></color>\n- 전장에 형벌 촛대가 없으면, 합 위력 -5\n- 자신에게 [ChargeNoir] 횟수가 있으면, 전부 소모하여 코인 위력 +2\n[DefeatDuel] [Paralysis] 4 얻음, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [WhenUse], [ChargeNoir], [DefeatDuel], [Paralysis]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\n[WhenUse]\n- If the main target has <color=#ff6000><mark=#ff000040><b><u>1 Speed</u></b></mark></color>, deal +100% damage\n- <color=#ff6000><mark=#ff000040><b><u>Final Power +2 for every Candle of Retribution on the field (max 8)</u></b></mark></color>\n- If there are no Candle of Retribution on the field, Clash Power -5\n- If this unit has [ChargeNoir] Count, consume all [ChargeNoir] Count on self to gain Coin Power +2\n[DefeatDuel] Gain 4 [Paralysis], deal -50% damage, and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse]\n- jeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>Szybkość 1</u></b></mark></color>, zadaje +100% obrażeń\n- <color=#ff6000><mark=#ff000040><b><u>Moc Końcowa +2 za każdą 1 Candle of Retribution na polu (maks. 8)</u></b></mark></color>\n- jeżeli na polu nie ma Candle of Retribution, Moc Starcia -5\n- jeżeli ta jednostka ma Liczniki [ChargeNoir], zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Monety +2\n[DefeatDuel] zyskuje 4 [Paralysis], zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
730. [Umiejętność wroga [148505] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Umiejętność wroga [148505] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Umiejętność wroga [148505] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Umiejętność wroga [148505] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Umiejętność wroga [148505] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148505].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Umiejętność wroga [148601] (ulepszenie 1) — nazwa] 속죄의 못
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].name
   limit: do 40 znaków
   EN: Nail of Penance
   PL: Nail of Penance
736. [Umiejętność wroga [148601] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>간수의 체력이 50% 이하</u></b></mark></color>면,\n이 스킬의 <color=#ff6000><mark=#ff000040><b><u>첫 번째 코인이 [SuperCoin]</u></b></mark></color>으로 변경됨\n대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 9</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir] 횟수 4 증가\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 1 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SuperCoin], [ConfessionSecondPhase], [WhenUse], [ChargeNoir], [Breath], [DefeatDuel]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <color=#ff6000><mark=#ff000040><b><u>If the Warden is at 50% or lower HP</u></b></mark></color>, convert the <color=#ff6000><mark=#ff000040><b><u>first Coin of this Skill into an [SuperCoin]</u></b></mark></color>\nIf target has <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionSecondPhase], Final Power +2</u></b></mark></color>\n[WhenUse] Gain +4 [ChargeNoir] Count\n[WhenUse] Gain 1 [Breath] and +1 [Breath] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli HP The Warden wynosi 50% lub mniej</u></b></mark></color>, pierwsza <color=#ff6000><mark=#ff000040><b><u>Moneta tej Umiejętności zamienia się w [SuperCoin]</u></b></mark></color>\njeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionSecondPhase], Moc Końcowa +2</u></b></mark></color>\n[WhenUse] zyskuje 4 Licznika [ChargeNoir]\n[WhenUse] zyskuje 1 [Breath] i 1 Licznika [Breath]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
737. [Umiejętność wroga [148601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MarkingNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkingNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkingNail] = 못[속죄] / Nail [Penance]
   EN: [OnSucceedAttack] Inflict 1 [MarkingNail]
   PL: [OnSucceedAttack] nakłada 1 [MarkingNail]
738. [Umiejętność wroga [148601] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Umiejętność wroga [148601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Umiejętność wroga [148601] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [MarkingNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MarkingNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MarkingNail] = 못[속죄] / Nail [Penance]
   EN: [OnSucceedAttack] Inflict 2 [MarkingNail]
   PL: [OnSucceedAttack] nakłada 2 [MarkingNail]
741. [Umiejętność wroga [148601] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148601].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Umiejętność wroga [148602] (ulepszenie 1) — nazwa] 형벌의 못
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].name
   limit: do 40 znaków
   EN: Nail of Punishment
   PL: Nail of Punishment
743. [Umiejętność wroga [148602] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>간수의 체력이 50% 이하</u></b></mark></color>면,\n이 스킬의 <color=#ff6000><mark=#ff000040><b><u>첫 번째 코인이 [SuperCoin]</u></b></mark></color>으로 변경됨\n대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir] 횟수 4 증가\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SuperCoin], [ConfessionSecondPhase], [WhenUse], [ChargeNoir], [Breath], [DefeatDuel]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: <color=#ff6000><mark=#ff000040><b><u>If the Warden is at 50% or lower HP</u></b></mark></color>, convert the <color=#ff6000><mark=#ff000040><b><u>first Coin of this Skill into an [SuperCoin]</u></b></mark></color>\nIf target has <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionSecondPhase], Final Power +2/+3</u></b></mark></color>\n[WhenUse] Gain +4 [ChargeNoir] Count\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli HP The Warden wynosi 50% lub mniej</u></b></mark></color>, pierwsza <color=#ff6000><mark=#ff000040><b><u>Moneta tej Umiejętności zamienia się w [SuperCoin]</u></b></mark></color>\njeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionSecondPhase], Moc Końcowa +2/+3</u></b></mark></color>\n[WhenUse] zyskuje 4 Licznika [ChargeNoir]\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
744. [Umiejętność wroga [148602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [CeremonialNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CeremonialNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CeremonialNail] = 못[형벌] / Nail [Punishment]
   EN: [OnSucceedAttack] Inflict 1 [CeremonialNail]
   PL: [OnSucceedAttack] nakłada 1 [CeremonialNail]
745. [Umiejętność wroga [148602] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 Licznika [Sinking]
746. [Umiejętność wroga [148602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Umiejętność wroga [148602] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [CeremonialNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [CeremonialNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [CeremonialNail] = 못[형벌] / Nail [Punishment]
   EN: [OnSucceedAttack] Inflict 2 [CeremonialNail]
   PL: [OnSucceedAttack] nakłada 2 [CeremonialNail]
748. [Umiejętność wroga [148602] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148602].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Umiejętność wroga [148603] (ulepszenie 1) — nazwa] 심판
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].name
   limit: do 40 znaków
   EN: Judgment
   PL: Judgment
750. [Umiejętność wroga [148603] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 3/6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3/+5</u></b></mark></color>\n[BeforeAttack] 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 5/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>공격 가중치 +1/+3</u></b></mark></color>\n[WhenUse] 자신에게 [ChargeNoir] 횟수가 있으면, 전부 소모하여 코인 위력 +2\n[DefeatDuel] [Paralysis] 3 얻음, 피해량 -50%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionSecondPhase], [BeforeAttack], [WhenUse], [ChargeNoir], [DefeatDuel], [Paralysis]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\nIf the main target has <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionSecondPhase], Final Power +2/+3/+5</u></b></mark></color>\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>If the main target has 5+/9+ [ConfessionSecondPhase], gain +1/+3 Atk Weight</u></b></mark></color>\n[WhenUse] If this unit has [ChargeNoir] Count, consume all [ChargeNoir] Count on self to gain Coin Power +2\n[DefeatDuel] Gain 3 [Paralysis], deal -50% damage, and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionSecondPhase], Moc Końcowa +2/+3/+5</u></b></mark></color>\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma 5+/9+ [ConfessionSecondPhase], zyskuje +1/+3 Wagi Ataku</u></b></mark></color>\n[WhenUse] jeżeli ta jednostka ma Liczniki [ChargeNoir], zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Monety +2\n[DefeatDuel] zyskuje 3 [Paralysis], zadaje -50% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
751. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 3, efekt 2 — opis] 이 코인은 <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게만 적중함</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>
   EN: This Coin <color=#ff6000><mark=#ff000040><b><u>hits only the main target</u></b></mark></color>
   PL: ta Moneta <color=#ff6000><mark=#ff000040><b><u>trafia wyłącznie główny cel</u></b></mark></color>
755. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 3, efekt 3 — opis] 피해량 +(자신의 잃은 체력 비율)% (최대 100%)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   EN: Deal +(missing HP percentage on self)% damage (max 100%)
   PL: zadaje +(procent utraconego HP tej jednostki)% obrażeń (maks. 100%)
756. [Umiejętność wroga [148603] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[ExecutionNailSecondPhase] 4 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148603].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [ExecutionNailSecondPhase]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ExecutionNailSecondPhase] = 망치 못[심판] / Hammernail [Judgment]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 4 [ExecutionNailSecondPhase]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 4 [ExecutionNailSecondPhase]</u></b></mark></color>
757. [Umiejętność wroga [148604] (ulepszenie 1) — nazwa] 신 앞에 뉘우쳐라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148604].levelList[level=1].name
   limit: do 40 znaków
   EN: Atone before God.
   PL: Atone before God.
758. [Umiejętność wroga [148604] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[GoldenFabricWarderSecondPhase]를 보유한 수감자</u></b></mark></color>가 명령 페이즈 시점에 이 스킬이 장착된 슬롯을 메인 타겟하여 공격 시, 해당 스킬의 피해량 +100% (E.G.O 스킬이면, 대신 피해량 +200%)\n[EndBattle] [EncompassingVoiceSecondPhase]가 100 미만이면, 100까지 증가\n- 증가한 수치만큼 간수의 정신력 감소 (최대 45)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148604].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [GoldenFabricWarderSecondPhase], [EndBattle], [EncompassingVoiceSecondPhase]
   znaczenie tagów: [GoldenFabricWarderSecondPhase] = 정지 / Stillness; [EndBattle] = [턴 종료 시] / [Turn End]; [EncompassingVoiceSecondPhase] = 검은 신의 목소리 / Voice of the Obsidian God
   EN: <color=#ff6000><mark=#ff000040><b><u>When the Sinner that has [GoldenFabricWarderSecondPhase]</u></b></mark></color> attacks the Slot equipped with this Skill as its main target in the Chaining Phase, the said Skill used by the Sinner deals +100% damage (for E.G.O Skills, +200% damage)\n[EndBattle] At fewer than 100 [EncompassingVoiceSecondPhase] Stack, gain up to 100 Stack\n- The Warden loses SP equal to Stack gained (max 45)
   PL: <color=#ff6000><mark=#ff000040><b><u>gdy Grzesznik mający [GoldenFabricWarderSecondPhase]</u></b></mark></color> atakuje w Fazie Łączenia slot z założoną tą Umiejętnością jako główny cel, ta Umiejętność Grzesznika zadaje +100% obrażeń (dla Umiejętności E.G.O zamiast tego +200% obrażeń)\n[EndBattle] jeżeli Stosy [EncompassingVoiceSecondPhase] są niższe niż 100, zyskuje do 100 Stosów\n- The Warden traci SP równe zyskanym Stosom (maks. 45)
759. [Umiejętność wroga [148605] (ulepszenie 1) — nazwa] 속죄하라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].name
   limit: do 40 znaków
   EN: Repent.
   PL: Repent.
760. [Umiejętność wroga [148605] (ulepszenie 1) — opis] 대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 9</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2</u></b></mark></color>\n[WhenUse] [SpreadingVoiceSecondPhase] 최대 15 소모\n- 최종 위력 +1, 피해량 +15%\n[WhenUse] 자신의 [ChargeNoir] 횟수 4 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionSecondPhase], [WhenUse], [SpreadingVoiceSecondPhase], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [WhenUse] = [사용시] / [On Use]; [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionSecondPhase], Final Power +2</u></b></mark></color>\n[WhenUse] Consume up to 15 [SpreadingVoiceSecondPhase]\n- Final Power +1, deal +15% damage\n[WhenUse] Gain +4 [ChargeNoir] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionSecondPhase], Moc Końcowa +2</u></b></mark></color>\n[WhenUse] zużywa do 15 [SpreadingVoiceSecondPhase]\n- Moc Końcowa +1, zadaje +15% obrażeń\n[WhenUse] zyskuje 4 Licznika [ChargeNoir]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
761. [Umiejętność wroga [148605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MarkingNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 737 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Umiejętność wroga [148605] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 703 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Umiejętność wroga [148605] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [MarkingNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 737 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Umiejętność wroga [148605] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking]
765. [Umiejętność wroga [148605] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [MarkingNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148605].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 737 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Umiejętność wroga [148606] (ulepszenie 1) — nazwa] 형벌받으라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].name
   limit: do 40 znaków
   EN: Receive thy punishment.
   PL: Receive thy punishment.
767. [Umiejętność wroga [148606] (ulepszenie 1) — opis] 대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3</u></b></mark></color>\n[WhenUse] [SpreadingVoiceSecondPhase] 최대 15 소모\n- 최종 위력 +2, 피해량 +30%\n[WhenUse] 자신의 [ChargeNoir] 횟수 4 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionSecondPhase], [WhenUse], [SpreadingVoiceSecondPhase], [ChargeNoir], [DefeatDuel]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [WhenUse] = [사용시] / [On Use]; [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: If target has <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionSecondPhase], Final Power +2/+3</u></b></mark></color>\n[WhenUse] Consume up to 15 [SpreadingVoiceSecondPhase]\n- Final Power +2, deal +30% damage\n[WhenUse] Gain +4 [ChargeNoir] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionSecondPhase], Moc Końcowa +2/+3</u></b></mark></color>\n[WhenUse] zużywa do 15 [SpreadingVoiceSecondPhase]\n- Moc Końcowa +2, zadaje +30% obrażeń\n[WhenUse] zyskuje 4 Licznika [ChargeNoir]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
768. [Umiejętność wroga [148606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [CeremonialNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Umiejętność wroga [148606] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 719 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Umiejętność wroga [148606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [CeremonialNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Umiejętność wroga [148606] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 Licznika [Sinking]
772. [Umiejętność wroga [148606] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [CeremonialNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148606].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 744 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Umiejętność wroga [148607] (ulepszenie 1) — nazwa] 심판…! 선고…! 단죄…!
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148607].levelList[level=1].name
   limit: do 60 znaków
   EN: Judgment... Sentencing... Condemnation!
   PL: Judgment... Sentencing... Condemnation!
774. [Umiejętność wroga [148607] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n대상의 수비 스킬을 발동시키지 않음\n이 스킬을 사용하기 전까지 흐트러지지 않음\n메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionSecondPhase]가 3/6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게 [GoldenFabricWarderSecondPhase]가 있으면,</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- 최종 위력 -5, 합 위력 -5</u></b></mark></color>\n[WhenUse] [SpreadingVoiceSecondPhase] 최대 40 소모\n- 최종 위력 +3, 피해량 +50%\n[WhenUse] 피해량 +(보유한 [SpreadingVoiceSecondPhase])%. 공격 종료 시, 보유한 [SpreadingVoiceSecondPhase] 전부 소모\n- <color=#ff6000><mark=#ff000040><b><u>합 패배 시, 이 효과가 발동하지 않음</u></b></mark></color>\n[WhenUse] 자신에게 [ChargeNoir] 횟수가 있으면, 전부 소모하여 코인 위력 +2\n[DefeatDuel] [Paralysis] 5 얻음, 피해량 -75%, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill]\n- 다음 턴에 [Vulnerable] 2 얻음\n- 이번 턴 종료
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148607].levelList[level=1].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionSecondPhase], [WhenUse], [GoldenFabricWarderSecondPhase], [SpreadingVoiceSecondPhase], [ChargeNoir], [DefeatDuel], [Paralysis], [EndSkill], [Vulnerable]
   znaczenie tagów: [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession; [WhenUse] = [사용시] / [On Use]; [GoldenFabricWarderSecondPhase] = 정지 / Stillness; [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: Can Clash with this Skill regardless of Speed\nThis Skill does not trigger the target's Defense Skill\nCannot be Staggered before using this Skill\nIf the main target has <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionSecondPhase], Final Power +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the main target has [GoldenFabricWarderSecondPhase]:</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- Final Power -5, Clash Power -5</u></b></mark></color>\n[WhenUse] Consume up to 40 [SpreadingVoiceSecondPhase] to:\n- Gain Final Power +3\n- Deal +50% damage\n[WhenUse] Deal +([SpreadingVoiceSecondPhase] Stack)% damage; at Attack End, consume all [SpreadingVoiceSecondPhase] on self\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose, this effect does not activate</u></b></mark></color>\n[WhenUse] If this unit has [ChargeNoir] Count, consume all [ChargeNoir] Count on self to gain Coin Power +2\n[DefeatDuel] Gain 5 [Paralysis], deal -75% damage, and damage dealt by this Skill cannot Stagger the target\n[EndSkill]\n- Gain 2 [Vulnerable] next turn\n- End this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nta Umiejętność nie uruchamia Umiejętności obrony celu\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\njeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionSecondPhase], Moc Końcowa +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma [GoldenFabricWarderSecondPhase]:</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- Moc Końcowa -5, Moc Starcia -5</u></b></mark></color>\n[WhenUse] zużywa do 40 [SpreadingVoiceSecondPhase]:\n- zyskuje Moc Końcową +3\n- zadaje +50% obrażeń\n[WhenUse] zadaje +(Stosy [SpreadingVoiceSecondPhase])% obrażeń; po zakończeniu ataku zużywa wszystkie [SpreadingVoiceSecondPhase] tej jednostki\n- <color=#ff6000><mark=#ff000040><b><u>po przegranej w Starciu ten efekt się nie uruchamia</u></b></mark></color>\n[WhenUse] jeżeli ta jednostka ma Liczniki [ChargeNoir], zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Monety +2\n[DefeatDuel] zyskuje 5 [Paralysis], zadaje -75% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill]\n- zyskuje 2 [Vulnerable] w następnej turze\n- kończy tę turę
775. [Umiejętność wroga [148607] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상이 보유한 [ConfessionSecondPhase] 효과를 발동시키고\n전부 소모</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148607].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [ConfessionSecondPhase]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ConfessionSecondPhase] = 고해의 증거 / Proof of Confession
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate the effects of [ConfessionSecondPhase] on target, then consume them all</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>uruchamia efekty [ConfessionSecondPhase] celu,\npo czym zużywa je wszystkie</u></b></mark></color>
776. [Umiejętność wroga [148607] (ulepszenie 1) — moneta 5, efekt 1 — opis] <color=#ff6000><mark=#ff000040><b><u>합에서 패배</u></b></mark></color>했으면, 이 코인은 <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게만 적중</u></b></mark></color>함\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] [RestrainingNailSecondPhase] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148607].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [RestrainingNailSecondPhase]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [RestrainingNailSecondPhase] = 망치 못[단죄] / Hammernail [Condemnation]
   EN: On <color=#ff6000><mark=#ff000040><b><u>Clash Lose</u></b></mark></color>, this Coin <color=#ff6000><mark=#ff000040><b><u>hits only the main target</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] Inflict 9 [RestrainingNailSecondPhase]</u></b></mark></color>
   PL: po <color=#ff6000><mark=#ff000040><b><u>przegranej w Starciu</u></b></mark></color> ta Moneta <color=#ff6000><mark=#ff000040><b><u>trafia wyłącznie główny cel</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] nakłada 9 [RestrainingNailSecondPhase]</u></b></mark></color>
777. [Umiejętność wroga [148607] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 메인 타겟이면, [BlackStigmata] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148607].levelList[level=1].coinlist[#4].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BlackStigmata]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BlackStigmata] = 죄악감 / Compunction
   EN: [OnSucceedAttack] If it is the main target, inflict 3 [BlackStigmata]
   PL: [OnSucceedAttack] jeżeli to główny cel, nakłada 3 [BlackStigmata]
778. [Umiejętność wroga [148608] (ulepszenie 1) — nazwa] 사형 집행
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148608].levelList[level=1].name
   limit: do 40 znaków
   EN: Death Unto the Condemned
   PL: Death Unto the Condemned
779. [Umiejętność wroga [148608] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderSecondPhase]을 보유한 수감자</u></b></mark></color>는 속도에 상관없이 <color=#ff6000><mark=#ff000040><b><u>이 스킬과 합을 진행</u></b></mark></color>할 수 있음\n[RestrainingNailSecondPhase]를 보유한 수감자를 우선으로 지정\n대상의 수비 스킬을 발동시키지 않음\n이 스킬을 사용하기 전까지 흐트러지지 않음\n[WhenUse] 대상에게 <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderSecondPhase]이 있으면, 합 위력 -15</u></b></mark></color>\n[DefeatDuel] 다음 턴에 [Vulnerable] 5 얻음\n[EndBattle] [SpreadingVoiceSecondPhase] 전부 소모
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148608].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [GoldenHideWarderSecondPhase], [RestrainingNailSecondPhase], [WhenUse], [DefeatDuel], [Vulnerable], [EndBattle], [SpreadingVoiceSecondPhase]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [GoldenHideWarderSecondPhase] = 박동 / Thumping Pulse; [RestrainingNailSecondPhase] = 망치 못[단죄] / Hammernail [Condemnation]; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndBattle] = [턴 종료 시] / [Turn End]; [SpreadingVoiceSecondPhase] = 검은 신의 권능 / Divinity of the Obsidian God
   EN: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Sinners that have [GoldenHideWarderSecondPhase] can Clash with this Skill</u></b></mark></color> regardless of Speed\nPrioritizes Sinners that have [RestrainingNailSecondPhase]\nDoes not trigger the target's Defense Skill\nCannot be Staggered before using this Skill\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If target has [GoldenHideWarderSecondPhase], Clash Power -15</u></b></mark></color>\n[DefeatDuel] Gain 5 [Vulnerable] next turn\n[EndBattle] Consume all [SpreadingVoiceSecondPhase] on self
   PL: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Grzesznicy mający [GoldenHideWarderSecondPhase] mogą stoczyć Starcie z tą Umiejętnością</u></b></mark></color> niezależnie od Szybkości\npriorytet: Grzesznicy mający [RestrainingNailSecondPhase]\nta Umiejętność nie uruchamia Umiejętności obrony celu\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[WhenUse] jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderSecondPhase], Moc Starcia -15</u></b></mark></color>\n[DefeatDuel] zyskuje 5 [Vulnerable] w następnej turze\n[EndBattle] zużywa wszystkie [SpreadingVoiceSecondPhase] tej jednostki
780. [Umiejętność wroga [148608] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148608].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Umiejętność wroga [148608] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상 <color=#ff6000><mark=#ff000040><b><u>최대 체력의 200%만큼 고정 피해</u></b></mark></color>를 입힘
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148608].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal fixed damage equal to 200% of target's max HP</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje obrażenia stałe równe 200% Maks. HP celu</u></b></mark></color>
782. [Umiejętność wroga [148609] (ulepszenie 1) — nazwa] 죄를 범했군…
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148609].levelList[level=1].name
   (powtórzenie elementu 695 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Umiejętność wroga [148609] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수 2 증가\n[WhenUse] [Breath] 1 얻음, 자신의 [Breath] 횟수 2 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148609].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +2 [ChargeNoir] Count\n[WhenUse] Gain 1 [Breath] and +2 [Breath] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zyskuje 2 Licznika [ChargeNoir]\n[WhenUse] zyskuje 1 [Breath] i 2 Licznika [Breath]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
784. [Umiejętność wroga [148609] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148609].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Umiejętność wroga [148609] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148609].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Umiejętność wroga [148610] (ulepszenie 1) — nazwa] 뉘우쳐라
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148610].levelList[level=1].name
   (powtórzenie elementu 699 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Umiejętność wroga [148610] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeNoir] 횟수 2 증가\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 1 증가\n[DefeatDuel] 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148610].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeNoir], [Breath], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Gain +2 [ChargeNoir] Count\n[WhenUse] Gain 2 [Breath] and +1 [Breath] Count\n[DefeatDuel] Damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] zyskuje 2 Licznika [ChargeNoir]\n[WhenUse] zyskuje 2 [Breath] i 1 Licznika [Breath]\n[DefeatDuel] obrażenia z tej Umiejętności nie Oszołamiają celu
788. [Umiejętność wroga [148610] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148610].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 1 Licznika [Sinking]
789. [Umiejętność wroga [148610] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148610].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 745 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Umiejętność wroga [148701] (ulepszenie 1) — nazwa] 하아… 이제 좀 돌아가 주지?
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148701].levelList[level=1].name
   limit: do 60 znaków
   EN: *sigh* Can you just... get rewound already?
   PL: *sigh* Can you just... get rewound already?
791. [Umiejętność wroga [148701] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>대상의 [ConfessionThirdPhase]가 5 이상</u></b></mark></color>이면,\n이 스킬의 <color=#ff6000><mark=#ff000040><b><u>첫 번째 코인이 [SuperCoin]</u></b></mark></color>으로 변경됨\n대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 9</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir] 횟수 3 증가\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 1 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148701].levelList[level=1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [SuperCoin], [WhenUse], [ChargeNoir], [Breath]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise
   EN: <color=#ff6000><mark=#ff000040><b><u>If target has 5+ [ConfessionThirdPhase], convert the first Coin of this Skill into [SuperCoin]</u></b></mark></color>\nIf target has <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionThirdPhase], Final Power +2</u></b></mark></color>\n[WhenUse] Gain +3 [ChargeNoir] Count\n[WhenUse] Gain 2 [Breath] and +1 [Breath] Count
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma 5+ [ConfessionThirdPhase], pierwsza Moneta tej Umiejętności zamienia się w [SuperCoin]</u></b></mark></color>\njeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionThirdPhase], Moc Końcowa +2</u></b></mark></color>\n[WhenUse] zyskuje 3 Licznika [ChargeNoir]\n[WhenUse] zyskuje 2 [Breath] i 1 Licznika [Breath]
792. [Umiejętność wroga [148701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Umiejętność wroga [148701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Umiejętność wroga [148702] (ulepszenie 1) — nazwa] 퇴근 좀 하자고.
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].name
   limit: do 70 znaków
   EN: Come on, let a guy clock out on time for once.
   PL: Come on, let a guy clock out on time for once.
795. [Umiejętność wroga [148702] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>대상의 [ConfessionThirdPhase]가 5 이상</u></b></mark></color>이면,\n이 스킬의 <color=#ff6000><mark=#ff000040><b><u>첫 번째 코인이 [SuperCoin]</u></b></mark></color>으로 변경됨\n대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3</u></b></mark></color>\n[WhenUse] 자신의 [ChargeNoir] 횟수 5 증가\n[WhenUse] [Breath] 2 얻음, 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [SuperCoin], [WhenUse], [ChargeNoir], [Breath]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [Breath] = 호흡 / Poise
   EN: <color=#ff6000><mark=#ff000040><b><u>If target has 5+ [ConfessionThirdPhase], convert the first Coin of this Skill into [SuperCoin]</u></b></mark></color>\nIf target has <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionThirdPhase], Final Power +2/+3</u></b></mark></color>\n[WhenUse] Gain +5 [ChargeNoir] Count\n[WhenUse] Gain 2 [Breath] and +2 [Breath] Count
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli cel ma 5+ [ConfessionThirdPhase], pierwsza Moneta tej Umiejętności zamienia się w [SuperCoin]</u></b></mark></color>\njeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionThirdPhase], Moc Końcowa +2/+3</u></b></mark></color>\n[WhenUse] zyskuje 5 Licznika [ChargeNoir]\n[WhenUse] zyskuje 2 [Breath] i 2 Licznika [Breath]
796. [Umiejętność wroga [148702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GoldenNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GoldenNail] = 못[Console] / Nail [Console]
   EN: [OnSucceedAttack] Inflict 1 [GoldenNail]
   PL: [OnSucceedAttack] nakłada 1 [GoldenNail]
797. [Umiejętność wroga [148702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Umiejętność wroga [148702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Umiejętność wroga [148702] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [GoldenNail] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GoldenNail]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GoldenNail] = 못[Console] / Nail [Console]
   EN: [OnSucceedAttack] Inflict 2 [GoldenNail]
   PL: [OnSucceedAttack] nakłada 2 [GoldenNail]
800. [Umiejętność wroga [148702] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148702].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Vibration] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 Licznika [Vibration]
801. [Umiejętność wroga [148703] (ulepszenie 1) — nazwa] ‘심판’
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].name
   limit: do 40 znaków
   EN: "Judgment."
   PL: "Judgment."
802. [Umiejętność wroga [148703] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 3/6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3/+5</u></b></mark></color>\n[BeforeAttack] 메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 5/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>공격 가중치 +1/+3</u></b></mark></color>\n[WhenUse] 자신에게 [ChargeNoir] 횟수가 있으면, 전부 소모하여 코인 위력 +2\n[DefeatDuel] [Paralysis] 3 얻음, 피해량 -75%, 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [BeforeAttack], [WhenUse], [ChargeNoir], [DefeatDuel], [Paralysis]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze
   EN: Can Clash with this Skill regardless of Speed\nIf the main target has <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionThirdPhase], Final Power +2/+3/+5</u></b></mark></color>\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>If the main target has 5+/9+ [ConfessionThirdPhase], gain +1/+3 Atk Weight</u></b></mark></color>\n[WhenUse] If this unit has [ChargeNoir] Count, consume all [ChargeNoir] Count on self to gain Coin Power +2\n[DefeatDuel] Gain 3 [Paralysis], deal -75% damage, and damage dealt by this Skill cannot Stagger the target
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\njeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionThirdPhase], Moc Końcowa +2/+3/+5</u></b></mark></color>\n[BeforeAttack] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma 5+/9+ [ConfessionThirdPhase], zyskuje +1/+3 Wagi Ataku</u></b></mark></color>\n[WhenUse] jeżeli ta jednostka ma Liczniki [ChargeNoir], zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Monety +2\n[DefeatDuel] zyskuje 3 [Paralysis], zadaje -75% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu
803. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 3, efekt 2 — opis] 이 코인은 <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게만 적중함</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 754 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 3, efekt 3 — opis] 피해량 +(자신의 잃은 체력 비율)% (최대 100%)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 755 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Umiejętność wroga [148703] (ulepszenie 1) — moneta 3, efekt 4 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[ExecutionNailThirdPhase] 4 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148703].levelList[level=1].coinlist[#2].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [ExecutionNailThirdPhase]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ExecutionNailThirdPhase] = 못[Breakpoint] / Nail [Breakpoint]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Inflict 4 [ExecutionNailThirdPhase]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>nakłada 4 [ExecutionNailThirdPhase]</u></b></mark></color>
809. [Umiejętność wroga [148704] (ulepszenie 1) — nazwa] ‘신 앞에 뉘우쳐라’던가?
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148704].levelList[level=1].name
   limit: do 50 znaków
   EN: "Atone before God"... was it?
   PL: "Atone before God"... was it?
810. [Umiejętność wroga [148704] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[GoldenFabricWarderThirdPhase]를 보유한 수감자</u></b></mark></color>가 명령 페이즈 시점에 이 스킬이 장착된 슬롯을 메인 타겟하여 공격 시, 해당 스킬의 피해량 +100% (E.G.O 스킬이면, 대신 피해량 +200%)\n[EndBattle] [EncompassingVoiceThirdPhase]가 100 미만이면, 100까지 증가\n- 증가한 수치만큼 신부의 정신력 감소 (최대 45)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148704].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [GoldenFabricWarderThirdPhase], [EndBattle], [EncompassingVoiceThirdPhase]
   znaczenie tagów: [GoldenFabricWarderThirdPhase] = 정지 / Stillness; [EndBattle] = [턴 종료 시] / [Turn End]; [EncompassingVoiceThirdPhase] = 검은 신의 목소리 / Voice of the Obsidian God
   EN: <color=#ff6000><mark=#ff000040><b><u>When the Sinner that has [GoldenFabricWarderThirdPhase]</u></b></mark></color> attacks the Slot equipped with this Skill as its main target in the Chaining Phase, the said Skill used by the Sinner deals +100% damage (for E.G.O Skills, +200% damage)\n[EndBattle] At fewer than 100 [EncompassingVoiceThirdPhase] Stack, gain up to 100 Stack\n- The Chaplain loses SP equal to Stack gained (max 45)
   PL: <color=#ff6000><mark=#ff000040><b><u>gdy Grzesznik mający [GoldenFabricWarderThirdPhase]</u></b></mark></color> atakuje w Fazie Łączenia slot z założoną tą Umiejętnością jako główny cel, ta Umiejętność Grzesznika zadaje +100% obrażeń (dla Umiejętności E.G.O zamiast tego +200% obrażeń)\n[EndBattle] jeżeli Stosy [EncompassingVoiceThirdPhase] są niższe niż 100, zyskuje do 100 Stosów\n- The Chaplain traci SP równe zyskanym Stosom (maks. 45)
811. [Umiejętność wroga [148705] (ulepszenie 1) — nazwa] ‘속죄하라’
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].name
   limit: do 40 znaków
   EN: "Repent."
   PL: "Repent."
812. [Umiejętność wroga [148705] (ulepszenie 1) — opis] 대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 9</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2</u></b></mark></color>\n[WhenUse] [SpreadingVoiceThirdPhase] 최대 15 소모\n- 최종 위력 +1, 피해량 +15%\n[WhenUse] 자신의 [ChargeNoir] 횟수 5 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [WhenUse], [SpreadingVoiceThirdPhase], [ChargeNoir]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [WhenUse] = [사용시] / [On Use]; [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation
   EN: If target has <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionThirdPhase], Final Power +2</u></b></mark></color>\n[WhenUse] Consume up to 15 [SpreadingVoiceThirdPhase]\n- Final Power +1, deal +15% damage\n[WhenUse] Gain +5 [ChargeNoir] Count
   PL: jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>9 [ConfessionThirdPhase], Moc Końcowa +2</u></b></mark></color>\n[WhenUse] zużywa do 15 [SpreadingVoiceThirdPhase]\n- Moc Końcowa +1, zadaje +15% obrażeń\n[WhenUse] zyskuje 5 Licznika [ChargeNoir]
813. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 2 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Vibration]
815. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Vibration]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Vibration] = 진동 / Tremor
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Vibration]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Vibration]
817. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Umiejętność wroga [148705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Umiejętność wroga [148706] (ulepszenie 1) — nazwa] ‘형벌받으라’
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].name
   limit: do 40 znaków
   EN: "Receive thy punishment."
   PL: "Receive thy punishment."
820. [Umiejętność wroga [148706] (ulepszenie 1) — opis] 대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3</u></b></mark></color>\n[WhenUse] [SpreadingVoiceThirdPhase] 최대 15 소모\n- 최종 위력 +2, 피해량 +30%\n[WhenUse] 자신의 [ChargeNoir] 횟수 6 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [WhenUse], [SpreadingVoiceThirdPhase], [ChargeNoir]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [WhenUse] = [사용시] / [On Use]; [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation
   EN: If target has <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionThirdPhase], Final Power +2/+3</u></b></mark></color>\n[WhenUse] Consume up to 15 [SpreadingVoiceThirdPhase]\n- Final Power +2, deal +30% damage\n[WhenUse] Gain +6 [ChargeNoir] Count
   PL: jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>6+/9+ [ConfessionThirdPhase], Moc Końcowa +2/+3</u></b></mark></color>\n[WhenUse] zużywa do 15 [SpreadingVoiceThirdPhase]\n- Moc Końcowa +2, zadaje +30% obrażeń\n[WhenUse] zyskuje 6 Licznika [ChargeNoir]
821. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 800 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [GoldenNail] 1 부여
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Umiejętność wroga [148706] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148706].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Umiejętność wroga [148707] (ulepszenie 1) — nazwa] 시지프 시스템을 진짜 망가트리려고?
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].name
   limit: do 70 znaków
   EN: Do you seriously mean to break the Sisyphe System?
   PL: Do you seriously mean to break the Sisyphe System?
828. [Umiejętność wroga [148707] (ulepszenie 1) — opis] 속도에 상관없이 이 스킬과 합을 할 수 있음\n대상의 수비 스킬을 발동시키지 않음\n이 스킬을 사용하기 전까지 흐트러지지 않음\n대상의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase] 1당, 피해량 +5%</u></b></mark></color> (대상 별로 판정)\n메인 타겟의 <color=#ff6000><mark=#ff000040><b><u>[ConfessionThirdPhase]가 3/6/9 이상</u></b></mark></color>이면, <color=#ff6000><mark=#ff000040><b><u>최종 위력 +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게 [GoldenFabricWarderThirdPhase]가 있으면,\n- 최종 위력 -5, 합 위력 -5</u></b></mark></color>\n- 이 스킬로 타겟된 모든 대상이 <color=#ff6000><mark=#ff000040><b><u>최대 체력 50%만큼 보호막 얻음.</u></b></mark></color> 공격 종료 시, 이 효과로 얻은 보호막 수치만큼 수감자가 보유한 보호막에서 차감함\n[WhenUse] [SpreadingVoiceThirdPhase] 최대 40 소모\n- 최종 위력 +3, 피해량 +50%\n[WhenUse] 피해량 +(보유한 [SpreadingVoiceThirdPhase])%. 공격 종료 시, 보유한 [SpreadingVoiceThirdPhase] 전부 소모\n- <color=#ff6000><mark=#ff000040><b><u>합 패배 시, 이 효과가 발동하지 않음</u></b></mark></color>\n[WhenUse] 자신에게 [ChargeNoir] 횟수가 있으면, 전부 소모하여 코인 위력 +2\n[DefeatDuel] [Paralysis] 5 얻음, 피해량 -90%, 이 스킬의 피해로 대상이 흐트러지지 않음\n[EndSkill]\n- 다음 턴에 [Vulnerable] 2 얻음\n- 이번 턴 종료
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].desc
   limit: do 1420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [ConfessionThirdPhase], [WhenUse], [GoldenFabricWarderThirdPhase], [SpreadingVoiceThirdPhase], [ChargeNoir], [DefeatDuel], [Paralysis], [EndSkill], [Vulnerable]
   znaczenie tagów: [ConfessionThirdPhase] = 〜 / 〜; [WhenUse] = [사용시] / [On Use]; [GoldenFabricWarderThirdPhase] = 정지 / Stillness; [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God; [ChargeNoir] = 보존 / Preservation; [DefeatDuel] = [합 패배] / [Clash Lose]; [Paralysis] = 마비 / Paralyze; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: Can Clash with this Skill regardless of Speed\nThis Skill does not trigger the target's Defense Skill\nCannot be Staggered before using this Skill\nDeal +5% damage for every [ConfessionThirdPhase] on target (against each target separately)\n<color=#ff6000><mark=#ff000040><b><u>If the main target has 3+/6+/9+ [ConfessionThirdPhase], Final Power +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If the main target has [GoldenFabricWarderThirdPhase]:\n- Final Power -5\n- Clash Power -5</u></b></mark></color>\n- All targets of this Skill <color=#ff6000><mark=#ff000040><b><u>gain Shield equal to 50% of their max HP, respectively</u></b></mark></color>; Shield gained from this effect is removed from the Sinner's total Shield at Attack End\n[WhenUse] Consume up to 40 [SpreadingVoiceThirdPhase] to:\n- Gain Final Power +3\n- Deal +50% damage\n[WhenUse] Deal +([SpreadingVoiceThirdPhase] Stack)% damage; at Attack End, consume all [SpreadingVoiceThirdPhase] on self\n- <color=#ff6000><mark=#ff000040><b><u>On Clash Lose, this effect does not activate</u></b></mark></color>\n[WhenUse] If this unit has [ChargeNoir] Count, consume all [ChargeNoir] Count on self to gain Coin Power +2\n[DefeatDuel] Gain 5 [Paralysis], deal -90% damage, and damage dealt by this Skill cannot Stagger the target\n[EndSkill]\n- Gain 2 [Vulnerable] next turn\n- End this turn
   PL: może stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\nta Umiejętność nie uruchamia Umiejętności obrony celu\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\nzadaje +5% obrażeń za każdą 1 [ConfessionThirdPhase] celu (rozpatrywane osobno dla każdego celu)\njeżeli główny cel ma <color=#ff6000><mark=#ff000040><b><u>3+/6+/9+ [ConfessionThirdPhase], Moc Końcowa +2/+3/+5</u></b></mark></color>\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>jeżeli główny cel ma [GoldenFabricWarderThirdPhase]:\n- Moc Końcowa -5\n- Moc Starcia -5</u></b></mark></color>\n- wszystkie cele tej Umiejętności <color=#ff6000><mark=#ff000040><b><u>zyskują Tarczę równą 50% ich Maks. HP, każdy osobno</u></b></mark></color>; po zakończeniu ataku Tarcza zyskana tym efektem zostaje odjęta od Tarczy Grzesznika\n[WhenUse] zużywa do 40 [SpreadingVoiceThirdPhase]:\n- zyskuje Moc Końcową +3\n- zadaje +50% obrażeń\n[WhenUse] zadaje +(Stosy [SpreadingVoiceThirdPhase])% obrażeń; po zakończeniu ataku zużywa wszystkie [SpreadingVoiceThirdPhase] tej jednostki\n- <color=#ff6000><mark=#ff000040><b><u>po przegranej w Starciu ten efekt się nie uruchamia</u></b></mark></color>\n[WhenUse] jeżeli ta jednostka ma Liczniki [ChargeNoir], zużywa wszystkie [ChargeNoir] tej jednostki, aby zyskać Moc Monety +2\n[DefeatDuel] zyskuje 5 [Paralysis], zadaje -90% obrażeń, a obrażenia z tej Umiejętności nie Oszołamiają celu\n[EndSkill]\n- zyskuje 2 [Vulnerable] w następnej turze\n- kończy tę turę
829. [Umiejętność wroga [148707] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>[VibrationFocusing]으로 [Switch_Vibration]</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack], [VibrationFocusing], [Switch_Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationFocusing] = 진동 - 보존 / Tremor - Conservation; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Trigger [Switch_Vibration] into [VibrationFocusing]</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>uruchamia przekształcenie [Switch_Vibration] w [VibrationFocusing]</u></b></mark></color>
830. [Umiejętność wroga [148707] (ulepszenie 1) — moneta 4, efekt 1 — opis] [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>대상이 보유한 [ConfessionThirdPhase] 효과를 발동시키고\n전부 소모</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack], [ConfessionThirdPhase]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ConfessionThirdPhase] = 〜 / 〜
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Activate the effects of [ConfessionThirdPhase] on target, then consume them all</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>uruchamia efekty [ConfessionThirdPhase] celu,\npo czym zużywa je wszystkie</u></b></mark></color>
831. [Umiejętność wroga [148707] (ulepszenie 1) — moneta 5, efekt 1 — opis] <color=#ff6000><mark=#ff000040><b><u>합에서 패배</u></b></mark></color>했으면, 이 코인은 <color=#ff6000><mark=#ff000040><b><u>메인 타겟에게만 적중</u></b></mark></color>함\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] [RestrainingNailThirdPhase] 9 부여</u></b></mark></color>
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].coinlist[#4].coindescs[#0].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuelAttack], [RestrainingNailThirdPhase]
   znaczenie tagów: [DefeatDuelAttack] = [합 패배 후 적중] / [Hit after Clash Lose]; [RestrainingNailThirdPhase] = 못[Exception] / Nail [Exception]
   EN: On <color=#ff6000><mark=#ff000040><b><u>Clash Lose</u></b></mark></color>, this Coin <color=#ff6000><mark=#ff000040><b><u>hits only the main target</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] Inflict 9 [RestrainingNailThirdPhase]</u></b></mark></color>
   PL: po <color=#ff6000><mark=#ff000040><b><u>przegranej w Starciu</u></b></mark></color> ta Moneta <color=#ff6000><mark=#ff000040><b><u>trafia wyłącznie główny cel</u></b></mark></color>\n<color=#ff6000><mark=#ff000040><b><u>- [DefeatDuelAttack] nakłada 9 [RestrainingNailThirdPhase]</u></b></mark></color>
832. [Umiejętność wroga [148707] (ulepszenie 1) — moneta 5, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148707].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Umiejętność wroga [148708] (ulepszenie 1) — nazwa] 강제 퇴장
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148708].levelList[level=1].name
   limit: do 40 znaków
   EN: Systemwide Ban
   PL: Systemwide Ban
834. [Umiejętność wroga [148708] (ulepszenie 1) — opis] <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderThirdPhase]을 보유한 수감자</u></b></mark></color>는 속도에 상관없이 <color=#ff6000><mark=#ff000040><b><u>이 스킬과 합을 진행</u></b></mark></color>할 수 있음\n[RestrainingNailThirdPhase]을 보유한 수감자를 우선으로 지정\n대상의 수비 스킬을 발동시키지 않음\n이 스킬을 사용하기 전까지 흐트러지지 않음\n[WhenUse] 대상에게 <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderThirdPhase]이 있으면, 합 위력 -15</u></b></mark></color>\n[DefeatDuel] 다음 턴에 [Vulnerable] 5 얻음\n[EndBattle] [SpreadingVoiceThirdPhase] 전부 소모
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148708].levelList[level=1].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantChangeTarget], [GoldenHideWarderThirdPhase], [RestrainingNailThirdPhase], [WhenUse], [DefeatDuel], [Vulnerable], [EndBattle], [SpreadingVoiceThirdPhase]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [GoldenHideWarderThirdPhase] = 박동 / Thumping Pulse; [RestrainingNailThirdPhase] = 못[Exception] / Nail [Exception]; [WhenUse] = [사용시] / [On Use]; [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndBattle] = [턴 종료 시] / [Turn End]; [SpreadingVoiceThirdPhase] = 검은 신의 권능 / Divinity of the Obsidian God
   EN: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Sinners that have [GoldenHideWarderThirdPhase] can Clash with this Skill</u></b></mark></color> regardless of Speed\nPrioritizes Sinners that have [RestrainingNailThirdPhase]\nDoes not trigger the target's Defense Skill\nCannot be Staggered before using this Skill\n[WhenUse] <color=#ff6000><mark=#ff000040><b><u>If target has [GoldenHideWarderThirdPhase], Clash Power -15</u></b></mark></color>\n[DefeatDuel] Gain 5 [Vulnerable] next turn\n[EndBattle] Consume all [SpreadingVoiceThirdPhase] on self
   PL: <color=#ff6000><mark=#ff000040><b><u>[CantChangeTarget]</u></b></mark></color>\n- <color=#ff6000><mark=#ff000040><b><u>Grzesznicy mający [GoldenHideWarderThirdPhase] mogą stoczyć Starcie z tą Umiejętnością</u></b></mark></color> niezależnie od Szybkości\npriorytet: Grzesznicy mający [RestrainingNailThirdPhase]\nta Umiejętność nie uruchamia Umiejętności obrony celu\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[WhenUse] jeżeli cel ma <color=#ff6000><mark=#ff000040><b><u>[GoldenHideWarderThirdPhase], Moc Starcia -15</u></b></mark></color>\n[DefeatDuel] zyskuje 5 [Vulnerable] w następnej turze\n[EndBattle] zużywa wszystkie [SpreadingVoiceThirdPhase] tej jednostki
835. [Umiejętność wroga [148708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ExtractCoin]
   znaczenie tagów: [ExtractCoin] = 적출 코인 / Excision Coin
   EN: [ExtractCoin]
   PL: [ExtractCoin]
836. [Umiejętność wroga [148708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상 <color=#ff6000><mark=#ff000040><b><u>최대 체력의 200%만큼 고정 피해</u></b></mark></color>를 입힘
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 781 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Umiejętność wroga [148709] (ulepszenie 1) — nazwa] Shift + Delete
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].name
   limit: do 40 znaków
   EN: Shift + Delete
   PL: Shift + Delete
838. [Umiejętność wroga [148709] (ulepszenie 1) — opis] 대상의 수비 스킬을 발동시키지 않음\n뫼르소 이외의 수감자를 우선으로 지정\n<color=#ff6000><mark=#ff000040><b><u>뫼르소와 합 진행 시,</u></b></mark></color> 합 위력 -20\n이 스킬을 사용하기 전까지 흐트러지지 않음\n[DefeatDuel] 이번 턴과 다음 턴에 [Vulnerable] 10 얻음\n[EndSkill] 신부가 합에서 패배했으면, <color=#ff6000><mark=#ff000040><b><u>신부가 현재 보유한 보호막이 50%만큼 감소</u></b></mark></color> (최소 0)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [DefeatDuel], [Vulnerable], [EndSkill]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]; [Vulnerable] = 취약 / Fragile; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Does not trigger the target's Defense Skill\nPrioritizes Sinners other than Meursault\n<color=#ff6000><mark=#ff000040><b><u>In a Clash against Meursault</u></b></mark></color>, Clash Power -20\nCannot be Staggered before using this Skill\n[DefeatDuel] Gain 10 [Vulnerable] this turn and next turn\n[EndSkill] If the Chaplain lost the Clash, <color=#ff6000><mark=#ff000040><b><u>the Chaplain loses 50% of its current Shield</u></b></mark></color> (min 0)
   PL: ta Umiejętność nie uruchamia Umiejętności obrony celu\npriorytet: Grzesznicy inni niż Meursault\n<color=#ff6000><mark=#ff000040><b><u>w Starciu z Meursaultem</u></b></mark></color> Moc Starcia -20\nnie przechodzi w Oszołamienie przed użyciem tej Umiejętności\n[DefeatDuel] zyskuje 10 [Vulnerable] w tej turze i następnej\n[EndSkill] jeżeli The Chaplain przegrał Starcie, <color=#ff6000><mark=#ff000040><b><u>The Chaplain traci 50% swojej aktualnej Tarczy</u></b></mark></color> (min. 0)
839. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 835 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>현재 체력 50%만큼 고정 피해</u></b></mark></color>를 입힘\n(최소 0)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal fixed damage equal to 50% of target's current HP</u></b></mark></color> (min 0)
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje obrażenia stałe równe 50% aktualnego HP celu</u></b></mark></color>\n(min. 0)
841. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 2, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 835 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>현재 체력 50%만큼 고정 피해</u></b></mark></color>를 입힘\n(최소 0)
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 3, efekt 1 — opis] [ExtractCoin]
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 835 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Umiejętność wroga [148709] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 <color=#ff6000><mark=#ff000040><b><u>최대 체력 200%만큼 고정 피해</u></b></mark></color>를 입힘
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=148709].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>Deal fixed damage equal to 200% of target's max HP</u></b></mark></color>
   PL: [OnSucceedAttack] <color=#ff6000><mark=#ff000040><b><u>zadaje obrażenia stałe równe 200% Maks. HP celu</u></b></mark></color>
845. [Umiejętność wroga [152201] (ulepszenie 1) — nazwa] 재단 못 준비
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152201].levelList[level=1].name
   limit: do 40 znaków
   EN: Readying the Sartorial Nails
   PL: Readying the Sartorial Nails
846. [Umiejętność wroga [152201] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeKhaki] 횟수 3 증가\n[WhenUse] 자신의 [Breath] 횟수 2 증가
   źródło: Skills_Abnormality-a1c10p3.json :: dataList[id=152201].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeKhaki], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeKhaki] = 표류 관성 / Inertia of Drifting; [Breath] = 호흡 / Poise
   EN: [WhenUse] Gain +3 [ChargeKhaki] Count\n[WhenUse] Gain +2 [Breath] Count
   PL: [WhenUse] zyskuje 3 Licznika [ChargeKhaki]\n[WhenUse] zyskuje 2 Licznika [Breath]
