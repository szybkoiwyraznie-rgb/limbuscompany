# Paczka AI P78 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 14/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P78_3c_przeciwnicy_i_anomalie_cz14.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P78_3c_przeciwnicy_i_anomalie_cz14.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## [mr7] Pasywka wroga: Passives_Abnormality-mr7
- plik gry: `Passives_Abnormality-mr7.json`

1. [[mr7] Pasywka wroga [138201] — opis] [Combustion], [Laceration], [Vibration], [Burst]로 받는 피해량 -30% (소수점 버림)\n받는 흐트러짐 피해량 -50% (소수점 버림)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138201].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture
   EN: Takes -30% damage from [Combustion], [Laceration], [Vibration], and [Burst] (rounded down)\n-50% to the amount of Stagger Threshold raised (rounded down)
   PL: otrzymuje o 30% mniej obrażeń od [Combustion], [Laceration], [Vibration] i [Burst] (zaokrąglone w dół)\noprócz tego o 50% mniej podnosi Próg Oszołomienia (zaokrąglone w dół)
2. [[mr7] Pasywka wroga [138202] — nazwa] 앙갚음 장부
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138202].name
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: The Book of Vengeance
3. [[mr7] Pasywka wroga [138202] — opis] 스테이지 시작시 모든 수감자에게 [VengeanceBookSpider]를 부여함\n\n이번 턴 적중한 스킬 수가 3개를 초과 했으면, 초과된 스킬 수만큼 다음 턴에 [ReinforcedTattooSpider] 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138202].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [VengeanceBookSpider], [ReinforcedTattooSpider]
   znaczenie tagów: [VengeanceBookSpider] = 앙갚음 장부 / The Book of Vengeance; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]
   EN: Encounter Start: Inflict [VengeanceBookSpider] on all Sinners\n\nIf this unit hit with more than 3 Skills this turn, gain 1 [ReinforcedTattooSpider] next turn for every excess Skill that hit
   PL: przy wejściu na etap, nakłada [VengeanceBookSpider] na wszystkich Grzeszników\n\njeżeli w tej turze jednostka trafiła więcej niż 3 Umiejętności, zyskuje 1 [ReinforcedTattooSpider] w następnej turze za każdą nadwyżkową Umiejętność
4. [[mr7] Pasywka wroga [138203] — nazwa] 딸램 교육
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138203].name
   limit: do 40 znaków
   EN: My Daughter's Education
   PL: My Daughter's Education
5. [[mr7] Pasywka wroga [138203] — opis] 합 승리시 [DaughterEducationSpider] 1 얻음\n\n스킬 적중시 [DaughterEducationSpider] 1 얻음 (스킬당 1회, 파괴된 코인일 경우 얻지 않음)\n\n턴의 가장 처음 사용하는 스킬의 합 승리시 [DaughterEducationSpider]을 1 추가로 얻고, 해당 스킬의 코인 위력 +1
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138203].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [DaughterEducationSpider]
   znaczenie tagów: [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: On Clash Win, gain 1 [DaughterEducationSpider]\n\nOn Hit with a Skill, gain 1 [DaughterEducationSpider] (once per Skill; this effect does not activate for Cracked Coins)\n\nOn Clash Win with the first-used Skill in a turn, gain 1 more [DaughterEducationSpider] and the Skill gains Coin Power +1
   PL: po wygranej w Starciu, zyskuje 1 [DaughterEducationSpider]\n\nprzy trafieniu Umiejętnością, zyskuje 1 [DaughterEducationSpider] (1 raz na Umiejętność; nie uruchamia się dla Rozerwanych Monet)\n\npo wygranej w Starciu pierwszą używaną w turze Umiejętnością, zyskuje dodatkowo 1 [DaughterEducationSpider], a ta Umiejętność zyskuje Moc Monety +1
6. [[mr7] Pasywka wroga [138204] — nazwa] 원한
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138204].name
   limit: do 40 znaków
   EN: Resentment
   PL: Resentment
7. [[mr7] Pasywka wroga [138204] — opis] 스킬 2회 피격 시 [ResentmentSpider] 1 획득, [DaughterEducationSpider] 1 감소 (피격 횟수는 누적됨)\n\n[ResentmentSpider]이 최댓값이면 강력한 공격을 사용함\n\n턴 종료시 체력이 90%, 60%, 40% 미만이면, [ResentmentSpider] 최댓값으로 획득함
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138204].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [ResentmentSpider], [DaughterEducationSpider]
   znaczenie tagów: [ResentmentSpider] = 중지 - 원한 / The Middle - Grudge; [DaughterEducationSpider] = 잘 봐둬라 딸! / Check This Out, Kiddo!
   EN: When hit by 2 Skills, gain 1 [ResentmentSpider] and lose 1 [DaughterEducationSpider] (number of hits taken is always tracked)\n\nAt max [ResentmentSpider] Stack, use a powerful attack\n\nTurn End: At less than 90% / 60% / 40% HP, max out this unit's [ResentmentSpider] Stack
   PL: gdy jednostka zostanie trafiona 2 Umiejętnościami, zyskuje 1 [ResentmentSpider] i traci 1 [DaughterEducationSpider] (liczba otrzymanych trafień jest zawsze zliczana)\n\nprzy maksymalnym Liczniku [ResentmentSpider] używa potężnego ataku\n\nna koniec tury, jeżeli HP jednostki poniżej 90%, 60% albo 40%, zyskuje [ResentmentSpider] do maksymalnego Licznika
8. [[mr7] Pasywka wroga [138205] — nazwa] 원한 문신 최고 출력… 레바테인 봉인 해제다!
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138205].name
   limit: do 70 znaków
   EN: Vengeance Tattoos Max Output... Unseal Lævateinn!
   PL: Vengeance Tattoos Max Output... Unseal Lævateinn!
9. [[mr7] Pasywka wroga [138205] — opis] [MiddleFatherSwordFour] 해방 시 [MiddleFatherGutsMirror]을 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138205].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MiddleFatherSwordFour], [MiddleFatherGutsMirror]
   znaczenie tagów: [MiddleFatherSwordFour] = 레바테인 / Lævateinn; [MiddleFatherGutsMirror] = 초근성 / Ridiculous Grit
   EN: When [MiddleFatherSwordFour] is unsealed, this unit gains [MiddleFatherGutsMirror]
   PL: gdy [MiddleFatherSwordFour] zostaje uwolniony, jednostka zyskuje [MiddleFatherGutsMirror]
10. [[mr7] Pasywka wroga [138801] — nazwa] 이렇게 하면 되는거죠 아빠!
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138801].name
   limit: do 50 znaków
   EN: Am I doing this right, Papa?!
   PL: Am I doing this right, Papa?!
11. [[mr7] Pasywka wroga [138801] — opis] 스테이지 시작시 [HeatingWireOffSpider]를 가지고 시작함\n\n턴 시작 시 자신이 보유한 [GotACompliment]가 3 이상이면 [HeatingWireOnSpider]으로 바뀌고, [Laceration]을 부여하는 스킬로 [Combustion]을 추가로 부여함\n- 턴 종료시 자신이 보유한 [GotACompliment]가 3 미만이면 [HeatingWireOnSpider]이 [HeatingWireOffSpider]로 전환됨\n\n중지 아비 - 마티아스가 [MiddleFatherSwordFour] 보유 시, [HeatingWireOffSpider] 상태가 되지 않음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138801].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOffSpider], [GotACompliment], [HeatingWireOnSpider], [Laceration], [Combustion], [MiddleFatherSwordFour]
   znaczenie tagów: [HeatingWireOffSpider] = 열선 OFF / Thermal Blades OFF; [GotACompliment] = 칭찬 받았다! / I Got Praised!; [HeatingWireOnSpider] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn; [MiddleFatherSwordFour] = 레바테인 / Lævateinn
   EN: Begins Encounter with [HeatingWireOffSpider]\n\nTurn Start: At 3+ [GotACompliment], gain [HeatingWireOnSpider] and also inflict [Combustion] with Skills that inflict [Laceration]\n- Turn End: At less than 3 [GotACompliment], convert this unit's [HeatingWireOnSpider] to [HeatingWireOffSpider]\n\nIf "The Middle Nursefather - Matthias" has [MiddleFatherSwordFour], this unit does not enter [HeatingWireOffSpider] state
   PL: rozpoczyna walkę ze stanem [HeatingWireOffSpider]\n\nna początku tury, jeżeli jednostka ma 3+ [GotACompliment], zyskuje [HeatingWireOnSpider] i dodatkowo nakłada [Combustion] Umiejętnościami nakładającymi [Laceration]\n- na koniec tury, jeżeli jednostka ma mniej niż 3 [GotACompliment], zmienia [HeatingWireOnSpider] w [HeatingWireOffSpider]\n\njeżeli „Ojciec Środkowego - Matthias” ma [MiddleFatherSwordFour], jednostka nie przechodzi w stan [HeatingWireOffSpider]
12. [[mr7] Pasywka wroga [138801] — tekst klimatyczny] ‘아빠는 늘 칭찬해주고 만화책을 사줘서 좋아’
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138801].flavor
   limit: do 120 znaków
   EN: "I like my papa because he always praises me and buys me comic books."
   PL: „Lubię tatę, bo zawsze mnie chwali i kupuje mi komiksy.”
13. [[mr7] Pasywka wroga [138802] — nazwa] 중지식 문신
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138802].name
   limit: do 40 znaków
   EN: The Middle Styled Tattoos
   PL: The Middle Styled Tattoos
14. [[mr7] Pasywka wroga [138802] — opis] 이번 턴 적중한 스킬 수가 2개를 초과했으면, 초과된 스킬 수만큼 다음 턴에 [ReinforcedTattooSpiderDaughter] 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138802].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [ReinforcedTattooSpiderDaughter]
   znaczenie tagów: [ReinforcedTattooSpiderDaughter] = 중지식 강화 문신 / The Middle Styled Augmentation Tattoos
   EN: If this unit hit with more than 2 Skills, gain 1 [ReinforcedTattooSpiderDaughter] next turn for every excess Skill that hit
   PL: jeżeli w tej turze jednostka trafiła więcej niż 2 Umiejętnościami, zyskuje 1 [ReinforcedTattooSpiderDaughter] w następnej turze za każdą nadwyżkową Umiejętność
15. [[mr7] Pasywka wroga [138802] — tekst klimatyczny] “나도 언젠간 중지에서 가족으로 인정받고, 누님이랑 형님들이랑 계속 같이 살 수 있는 거야?”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138802].flavor
   limit: do 160 znaków
   EN: 'Will the bigger Sisters and Brothers of the Middle accept me as their family one day, so I can continue to live with them?'
   PL: „Czy kiedyś Środkowy uzna mnie za rodzinę, żebym mógł dalej mieszkać z Siostrami i Braćmi?”
16. [[mr7] Pasywka wroga [138803] — nazwa] 칭찬은 키라도 춤추게 한다
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138803].name
   limit: do 50 znaków
   EN: Praise is the Wind in Her Sail
   PL: Praise is the Wind in Her Sail
17. [[mr7] Pasywka wroga [138803] — opis] 합 승리시 [GotACompliment] 1 얻음\n\n스킬 적중시 [GotACompliment] 1 얻음 (스킬당 1회, 파괴된 코인일 경우 얻지 않음)\n\n턴의 가장 처음 사용하는 스킬의 합 승리시 [GotACompliment]를 1 추가로 얻고, 해당 스킬의 코인 위력 +1
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138803].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [GotACompliment]
   znaczenie tagów: [GotACompliment] = 칭찬 받았다! / I Got Praised!
   EN: On Clash Win, gain 1 [GotACompliment]\n\nOn Hit with a Skill, gain 1 [GotACompliment] (once per Skill; this effect does not activate for Cracked Coins)\n\nOn Clash Win with the first-used Skill in a turn, gain 1 more [GotACompliment] and the Skill gains Coin Power +1
   PL: po wygranej w Starciu, zyskuje 1 [GotACompliment]\n\nprzy trafieniu Umiejętnością, zyskuje 1 [GotACompliment] (1 raz na Umiejętność; nie uruchamia się dla Rozerwanych Monet)\n\npo wygranej w Starciu pierwszą używaną w turze Umiejętnością, zyskuje dodatkowo 1 [GotACompliment], a ta Umiejętność zyskuje Moc Monety +1
18. [[mr7] Pasywka wroga [138804] — nazwa] 중지는 반드시 갚는 거라 했어
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138804].name
   limit: do 60 znaków
   EN: I'm pretty sure the Middle never forgets
   PL: I'm pretty sure the Middle never forgets
19. [[mr7] Pasywka wroga [138804] — opis] 스킬 2회 피격 시 [ResentmentSpiderDaughter] 1 얻음, [GotACompliment] 1 감소 (피격 횟수는 누적됨)\n\n자신의 [ResentmentSpiderDaughter]이 최댓값이면 강력한 공격을 사용함\n\n턴 종료시 자신의 체력이 80%, 60%, 40% 미만이면, [ResentmentSpiderDaughter] 최댓값으로 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138804].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [ResentmentSpiderDaughter], [GotACompliment]
   znaczenie tagów: [ResentmentSpiderDaughter] = 중지 - 원한 / The Middle - Grudge; [GotACompliment] = 칭찬 받았다! / I Got Praised!
   EN: When hit by 2 Skills, gain 1 [ResentmentSpiderDaughter] and lose 1 [GotACompliment] (number of hits taken is always tracked)\n\nAt max [ResentmentSpiderDaughter] Stack, use a powerful attack\n\nTurn End: At less than 80% / 60% / 40% HP, max out this unit's [ResentmentSpiderDaughter] Stack
   PL: gdy jednostka zostanie trafiona 2 Umiejętnościami, zyskuje 1 [ResentmentSpiderDaughter] i traci 1 [GotACompliment] (liczba otrzymanych trafień jest zawsze zliczana)\n\nprzy maksymalnym Liczniku [ResentmentSpiderDaughter] używa potężnego ataku\n\nna koniec tury, jeżeli HP jednostki poniżej 80%, 60% albo 40%, zyskuje [ResentmentSpiderDaughter] do maksymalnego Licznika
20. [[mr7] Pasywka wroga [138001] — nazwa] 검지 아비 뤼엔
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138001].name
   limit: do 40 znaków
   EN: Rien, The Index Nursefather
   PL: Rien, The Index Nursefather
21. [[mr7] Pasywka wroga [138001] — opis] <color=#ff6000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -50%</u></b></mark></color>\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -50%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 15 미만이면, 정신력을 15까지 회복\n\n스테이지 시작 시, [BurningWoundRien_Mask] 얻고 정신력을 30까지 회복\n\n체력이 55% 이하면, 턴이 종료되고 페이즈 변경\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- [StackRienSpecialSkill]이 9 미만이면, 9로 변경
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138001].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [BurningWoundRien_Mask], [StackRienSpecialSkill]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [BurningWoundRien_Mask] = 뤼엔의 가면 / Rien's Mask; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: <color=#ff6000><mark=#ff000040><b><u>Take -50% damage from Unopposed Attacks</u></b></mark></color>\nTake -50% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 15, heal SP up to 15\n\nEncounter Start: Gain [BurningWoundRien_Mask] and heal SP up to 30\n\nAt 55%- HP, end the turn and gain a new pattern\n- Remove all effects other than those exclusive to this unit\n- At less than 9 [StackRienSpecialSkill], change [StackRienSpecialSkill] Stack to 9
   PL: <color=#ff6000><mark=#ff000040><b><u>otrzymuje o 50% mniej obrażeń od Ataków Jednostronnych</u></b></mark></color>\notrzymuje o 50% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\ngdy przywraca SP z [UnlockBuff_Base], jeżeli SP jednostki poniżej 15, przywraca SP do 15\n\nprzy wejściu na etap, zyskuje [BurningWoundRien_Mask] i przywraca SP do 30\n\njeżeli HP jednostki spadnie do 55% lub mniej, tura się kończy i zmienia się faza\n- usuwa wszystkie efekty poza tymi wyłącznymi dla tej jednostki\n- jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, zmienia go na 9
22. [[mr7] Pasywka wroga [138001] — tekst klimatyczny] 지령이 말한 대로 그때를 기다렸다고.\n딸이 나가도 기다리고 기다렸지.\n\n그러다 림버스 컴퍼니에서 연락이 왔고 뒷문이 열려있더구나.\n그리고 단말기가 울려서 딸을 데리러 가야 할 때가 되었다는 것을 알았지.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138001].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I waited for "the moment" as the Prescript told me to.\nEven after my darling daughter left, I waited.\n\nAnd after a while, I was contacted by Limbus Company, and saw that the Backdoor was open.\nThat's when the device beeped and let me know that it was finally time to bring my daughter home.
   PL: Czekałem na „tę chwilę”, jak przykazywały Nakazy.\nNawet gdy moja droga córka wyszła, czekałem i czekałem.\n\nPewnego razu skontaktowało się ze mną Limbus Company, a ja zobaczyłem, że tylne drzwi stoją otworem.\nI wtedy urządzenie zapiszczało, dając mi znać, że przyszedł wreszcie czas, by zabrać córkę do domu.
23. [[mr7] Pasywka wroga [138002] — nazwa] 신탁 단말기 [카두세우스]
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138002].name
   limit: do 40 znaków
   EN: Oracle Device [Caduceus]
   PL: Oracle Device [Caduceus]
24. [[mr7] Pasywka wroga [138002] — opis] <color=#ff6000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2를 초과하여 얻을 수 없음)\n\n<color=#ff6000><mark=#ff000040><b><u>턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬 사용</u></b></mark></color>\n- 첫 사용 후 공격 종료 시, [Shin_Rien] 얻음\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +15\n- 턴 종료 시 다음 턴에, [Vulnerable] 1, [ResultReduction] 2 얻음\n\n세 번째 턴 시작 시, [StackRienSpecialSkill]가 9 미만이면, 9까지 증가하고 (증가한 수치 x 3)만큼 [KarmaOfIndexRien] 얻음\n- 이후 세 턴마다 이 효과 발동
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138002].desc
   limit: do 1140 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet], [RienWeapon02Stiletto], [RienWeapon03Greatsword], [RienWeapon04Rapier], [RienWeapon05Sledgehammer], [RienWeapon06Ultragreatsword], [RienWeapon07Lance], [RienWeapon08Chain], [RienWeapon09Scythe], [StackRienSpecialSkill], [Shin_Rien], [Vulnerable], [ResultReduction], [KarmaOfIndexRien]
   znaczenie tagów: [RienWeapon01Hatchet] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a greatsword...; [RienWeapon07Lance] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff6000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n\n<color=#ff6000><mark=#ff000040><b><u>Turn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill</u></b></mark></color>\n- Attack End: After using the powerful Skill for the first time, gain [Shin_Rien]\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +15\n- Turn End: Gain 1 [Vulnerable] and 2 [ResultReduction] next turn\n\nTurn 3 Start: At less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 3) [KarmaOfIndexRien]\n- Then, activate this effect every 3 turns
   PL: <color=#ff6000><mark=#ff000040><b><u>do każdej Monety przypisywana jest losowa broń; każda broń ma unikalny efekt</u></b></mark></color>\n- [RienWeapon01Hatchet]\n- [RienWeapon02Stiletto]\n- [RienWeapon03Greatsword]\n- [RienWeapon04Rapier]\n- [RienWeapon05Sledgehammer]\n- [RienWeapon06Ultragreatsword]\n- [RienWeapon07Lance]\n- [RienWeapon08Chain]\n- [RienWeapon09Scythe]\n\nprzy użyciu Umiejętności ataku, zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zyskać 1 raz na Umiejętność (nie można zyskać 2 razy od tej samej Umiejętności)\n\n<color=#ff6000><mark=#ff000040><b><u>na początku tury, przy 9 Licznikach [StackRienSpecialSkill], używa potężnej Umiejętności</u></b></mark></color>\n- po zakończeniu Ataku: po pierwszym użyciu potężnej Umiejętności, zyskuje [Shin_Rien]\n- resetuje limit zyskiwania [StackRienSpecialSkill] na Umiejętność\n- Minimalna i Maksymalna Szybkość +15\n- na koniec tury, w następnej turze zyskuje 1 [Vulnerable] i 2 [ResultReduction]\n\nna początku 3. tury, jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, zwiększa go do 9 i zyskuje (zyskana wartość x 3) [KarmaOfIndexRien]\n- następnie efekt uruchamia się co 3 tury
25. [[mr7] Pasywka wroga [138002] — tekst klimatyczny] 단말기 안에는 특이점과 유사한 기술을 이용해 형태와 질량을 변동시킬 수 있는, 금속 같은 액체가 들어 있다.\n이 액체는 단말기가 수령한 지령에 따라 모습을 바꾸며, 살해 대상의 정보와 주어진 제한 시간에 맞춰 무기로 변환된다.\n어느 날에는 지나치게 작은 단검이 배정되어 다른 무기로 바뀌기를 기다렸지만, 살해 제한 시간이 다가올 때까지 쓸만한 무기가 나오지 않았다. 결국, 마지막까지 기다려 나온 것이 포크였기에, 그 포크로 대상을 죽여야만 했다.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138002].flavor
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A vial of what looks like liquid metal capable of changing its shape and mass, its qualities almost like those of Singularities, swishes inside the Device.\nThe form the fluid takes is contingent on the Prescript the Device receives. The weapons it produces depend on the information regarding the target and the time limit given to carry out the assassination.\nOne day, as he received a dagger too small for the task, he elected to wait until it produced a different weapon. However, despite the approaching deadline, it refused to provide him a proper weapon; he had no choice but to kill his target with a fork.
   PL: Wewnątrz Urządzenia pluska się zbiornik płynu wyglądającego jak ciekły metal, zdolny zmieniać kształt i masę — jego właściwości niemal jak te Singularności.\nPłyn przybiera formę zależną od Nakazu otrzymanego przez Urządzenie; broń, którą wytwarza, zależy od informacji o celu i wyznaczonego limitu czasu na wykonanie zabójstwa.\nPewnego dnia, gdy otrzymał sztylet zbyt mały do zadania, postanowił poczekać, aż Urządzenie wytworzy inną broń. Jednak mimo zbliżającego się terminu nie doczekał się porządnej broni; nie pozostało mu nic innego, jak zabić cel widelcem.
26. [[mr7] Pasywka wroga [138003] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138003].name
   limit: do 40 znaków
   EN: Will of the Prescript
   PL: Will of the Prescript
27. [[mr7] Pasywka wroga [138003] — opis] 턴 시작 시,\n- [UnlockBuff_Base] 단계에 따라 [IndexPrescript_Base_2nd] 얻음\n- 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff6000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n\n공격 시 [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우,\n<color=#ff6000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 무작위 수감자에게 사용\n- 현재 체력이 가장 낮은 대상 우선 (체력 1인 경우 제외)</u></b></mark></color>\n- 무작위로 선택된 수감자가 사망하거나 체력이 1이 될 경우, 다른 수감자에게 반복\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +2.5% (최대 20%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +30%
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138003].desc
   limit: do 1090 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [UnlockBuff_Base], [IndexPrescript_Base_2nd], [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy]
   znaczenie tagów: [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_Base_2nd] = 지령 / Prescript; [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript
   EN: Turn Start:\n- Gain [IndexPrescript_Base_2nd] based on [UnlockBuff_Base] stage on self\n- Apply [IndexPrescriptTargetToPersonality] against a random Sinner, and prioritize attacking them\n<color=#ff6000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n\nWhen attacking, if [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff6000><mark=#ff000040><b><u>use the remaining Skills against a random other Sinner\n- Prioritizes targets with the least current HP, unless they have 1 HP</u></b></mark></color>\n- When the randomly chosen Sinner is killed, or if the said Sinner's HP is brought down to 1, repeat this effect on another Sinner\n\nDeal +2.5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 20%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +30% damage against all targets
   PL: na początku tury:\n- zyskuje [IndexPrescript_Base_2nd] zależnie od etapu [UnlockBuff_Base]\n- nakłada [IndexPrescriptTargetToPersonality] losowemu Grzesznikowi i priorytet: atakowanie go\n<color=#ff6000><mark=#ff000040><b><u>- gdy używa Umiejętności na [IndexPrescriptTargetToPersonality], wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y</u></b></mark></color>\n\ngdy atakuje, jeżeli [IndexPrescriptTargetToPersonality] zginie albo jednostka nie może już zaatakować tego celu, <color=#ff6000><mark=#ff000040><b><u>używa pozostałych Umiejętności na losowym innym Grzeszniku\n- priorytet: cele z najmniejszym aktualnym HP, z wyjątkiem celów z 1 HP</u></b></mark></color>\n- jeżeli losowo wybrany Grzesznik zginie albo jego HP spadnie do 1, powtarza ten efekt na innym Grzeszniku\n\nzadaje +2.5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 20%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +30% obrażeń wszystkim celom
28. [[mr7] Pasywka wroga [138003] — tekst klimatyczny] 제가 가족을 꾸리길 원하십니까. \n\n“당신 같은 남편을 어쩜 이렇게 운명적으로 만날 수 있었을까요.”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138003].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to raise a family?\n\n"It must've been fate that brought us together. To think that I'd ever meet a husband like you..."
   PL: Czy pragniesz, bym założył rodzinę?\n\n„To musiał być los, że spotkałam męża takiego jak ty…”
29. [[mr7] Pasywka wroga [138004] — nazwa] 지령 수행
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138004].name
   limit: do 40 znaków
   EN: Undertake Prescript
   PL: Undertake Prescript
30. [[mr7] Pasywka wroga [138004] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 10 회복, [BlessingOfIndexPrescriptEnemy] 3 얻음 (턴당 1회)\n\n이번 턴에<color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien] 8 얻음</u></b></mark></color>\n- [UnlockBuff_Base]이 없으면, 턴 종료 시 [BlessingOfIndexPrescriptEnemy] 1 얻음\n- [BlessingOfIndexPrescriptEnemy]가 9면, [KarmaOfIndexRien]를 얻지 않음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138004].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien], [UnlockBuff_Base]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien] = 카르마 / Karmic Consequence; [UnlockBuff_Base] = 해금 / Unlock
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 10 SP and gain 3 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff6000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 8 [KarmaOfIndexRien]</u></b></mark></color>\n- If this unit does not have [UnlockBuff_Base], gain 1 [BlessingOfIndexPrescriptEnemy] at Turn End\n- At 9 [BlessingOfIndexPrescriptEnemy], does not gain [KarmaOfIndexRien]
   PL: na koniec tury: jeżeli [IndexPrescript_Base_2nd] został wykonany w tej turze, przywraca 10 SP i zyskuje 3 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff6000><mark=#ff000040><b><u>na koniec tury: jeżeli [IndexPrescript_Base_2nd] nie został wykonany w tej turze, zyskuje 8 [KarmaOfIndexRien]</u></b></mark></color>\n- jeżeli jednostka nie ma [UnlockBuff_Base], na koniec tury zyskuje 1 [BlessingOfIndexPrescriptEnemy]\n- przy 9 [BlessingOfIndexPrescriptEnemy], nie zyskuje [KarmaOfIndexRien]
31. [[mr7] Pasywka wroga [138004] — tekst klimatyczny] 제가 가족을 잃기를 원하십니까.\n\n“여보. 잠시 북부에 좀 다녀올게.”\n“아, 오후에 택배가 오기로 했으니 대신 받아줄 수 있겠니, 딸?”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138004].flavor
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Do you wish me to lose my family?\n\n"Honey, I gotta take a quick trip up north today."\n"Ah, also—hey, buddy. I'm expecting a package this afternoon, so would you be a dear and pick it up for me, sweetheart?"
   PL: Czy pragniesz, bym stracił rodzinę?\n\n„Kochanie, wybiję się na chwilę na północ.”\n„A, po południu ma przyjść paczka. Odebrałabyś ją za mnie, córeczko?”
32. [[mr7] Pasywka wroga [138005] — nazwa] 해금
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138005].name
   limit: do 40 znaków
   EN: Unlock
   PL: Unlock
33. [[mr7] Pasywka wroga [138005] — opis] 턴 종료 시 [BlessingOfIndexPrescriptEnemy]가 3/6/9거나 체력이 95%/85%/75% 이하면,\n- [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3] 얻음\n\n첫 번째/두 번째 턴 종료 시 [UnlockBuff_Base] 단계가 1/2 미만이면,\n[UnlockBuff_Rien1]/[UnlockBuff_Rien2] 얻음\n\n[UnlockBuff_Base]을 보유하지 않은 상태에서 처음으로 획득할 때\n정신력이 15 미만이면, 정신력을 15까지 회복\n\n\n체력 또는 턴 조건으로 [UnlockBuff_Base] 시,\n- [BlessingOfIndexPrescriptEnemy]가 3/6/9 미만이면, 3/6/9로 변경,\n증가한 수치 1당 다음 턴 시작 시 [KarmaOfIndexRien] 5 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138005].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n, [BlessingOfIndexPrescriptEnemy], [UnlockBuff_Rien1], [UnlockBuff_Rien2], [UnlockBuff_Rien3], [UnlockBuff_Base], [KarmaOfIndexRien]
   znaczenie tagów: [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_Rien1] = 해금 - I / Unlock - I; [UnlockBuff_Rien2] = 해금 - II / Unlock - II; [UnlockBuff_Rien3] = 해금 - III / Unlock - III; [UnlockBuff_Base] = 해금 / Unlock; [KarmaOfIndexRien] = 카르마 / Karmic Consequence
   EN: Turn End: At 3/6/9 [BlessingOfIndexPrescriptEnemy] or at 95%-/85%-/75%- HP,\n- Gain [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nTurn 1 End: At lower than [UnlockBuff_Base] stage 1, gain [UnlockBuff_Rien1]\nTurn 2 End: At lower than [UnlockBuff_Base] stage 2, gain [UnlockBuff_Rien2]\n\nWhen gaining [UnlockBuff_Base] for the first time, if this unit's SP is below 15, heal up to 15 SP\n\nWhen [UnlockBuff_Base] is activated due to HP or Turn conditionals:\n- At less than 3/6/9 [BlessingOfIndexPrescriptEnemy] Stack, raise the Stack to 3/6/9 and gain 5 [KarmaOfIndexRien] at the next Turn Start for every Stack gained
   PL: na koniec tury: przy 3/6/9 [BlessingOfIndexPrescriptEnemy] albo przy HP 95%/85%/75% lub mniej:\n- zyskuje [UnlockBuff_Rien1]/[UnlockBuff_Rien2]/[UnlockBuff_Rien3]\n\nna koniec 1. tury: jeżeli etap [UnlockBuff_Base] jest niższy niż 1, zyskuje [UnlockBuff_Rien1]\nna koniec 2. tury: jeżeli etap [UnlockBuff_Base] jest niższy niż 2, zyskuje [UnlockBuff_Rien2]\n\nprzy pierwszym zyskaniu [UnlockBuff_Base], jeżeli SP jednostki poniżej 15, przywraca SP do 15\n\n\ngdy [UnlockBuff_Base] zostaje aktywowany wskutek warunku HP albo tury:\n- przy mniej niż 3/6/9 Licznikach [BlessingOfIndexPrescriptEnemy], zwiększa je do 3/6/9 i zyskuje 5 [KarmaOfIndexRien] na początku następnej tury za każdy zyskany Licznik
34. [[mr7] Pasywka wroga [138005] — tekst klimatyczny] “지령을 따라가다 보면 닫힌 것들이 풀리기 마련.”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138005].flavor
   limit: do 120 znaków
   EN: "Following the Prescripts is to unlock what is locked."
   PL: „Podążanie za Nakazami odblokowuje to, co zamknięte.”
35. [[mr7] Pasywka wroga [138101] — nazwa] 아비 뤼엔 [모조품]
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138101].name
   limit: do 40 znaków
   EN: Rien, the Father [Imitation]
   PL: Rien, the Father [Imitation]
36. [[mr7] Pasywka wroga [138101] — opis] <color=#ff6000><mark=#ff000040><b><u>일방 공격으로 받는 피해량 -75%</u></b></mark></color>\n[Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -75%\n[UnlockBuff_Base]으로 정신력 회복 시 정신력이 15 미만이면, 정신력을 15까지 회복\n\n체력이 55% 이하가 되어 페이즈 변경 시, 다음 효과 적용\n- 자신의 고유 효과 외 나머지 효과 전부 소멸\n- [IndexPrescript_RienSecondPhase] 얻음\n- [BurningWoundRien_Mask]이 [BurningWoundRien]로 변경\n- [KarmaOfIndexRien]가 [KarmaOfIndexRien_2Phase]로 변경되고 10 얻음\n- [Shin_Rien]이 없으면 즉시 얻음\n\n체력이 25% 이하면 패턴이 변경되어 특정 스킬이 더욱 강력해짐
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138101].desc
   limit: do 870 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [UnlockBuff_Base], [IndexPrescript_RienSecondPhase], [BurningWoundRien_Mask], [BurningWoundRien], [KarmaOfIndexRien], [KarmaOfIndexRien_2Phase], [Shin_Rien]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [UnlockBuff_Base] = 해금 / Unlock; [IndexPrescript_RienSecondPhase] = 지령[단말기] - 경고 / Prescript: [Device] - Warning; [BurningWoundRien_Mask] = 뤼엔의 가면 / Rien's Mask …
   EN: <color=#ff6000><mark=#ff000040><b><u>Take -75% damage from Unopposed Attacks</u></b></mark></color>\nTake -75% damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]\nWhen healing SP from [UnlockBuff_Base], if this unit's SP is below 15, heal up to 15 SP\n\nWhen this unit enters a new phase at 55% HP, gain the following effects:\n- Remove all effects other than those exclusive to this unit\n- Gain [IndexPrescript_RienSecondPhase]\n- Convert [BurningWoundRien_Mask] to [BurningWoundRien]\n- Convert [KarmaOfIndexRien] to [KarmaOfIndexRien_2Phase]; then gain 10 Stacks of that effect\n- If this unit does not have [Shin_Rien], immediately gain that effect\n\nAt 25% or lower HP, gain a new pattern and greatly enhance a certain Skill
   PL: <color=#ff6000><mark=#ff000040><b><u>otrzymuje o 75% mniej obrażeń od Ataków Jednostronnych</u></b></mark></color>\notrzymuje o 75% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\ngdy przywraca SP z [UnlockBuff_Base], jeżeli SP jednostki poniżej 15, przywraca SP do 15\n\ngdy jednostka wchodzi w nową fazę przy 55% HP, zyskuje następujące efekty:\n- usuwa wszystkie efekty poza tymi wyłącznymi dla tej jednostki\n- zyskuje [IndexPrescript_RienSecondPhase]\n- zmienia [BurningWoundRien_Mask] w [BurningWoundRien]\n- zmienia [KarmaOfIndexRien] w [KarmaOfIndexRien_2Phase]; następnie zyskuje 10 Liczników tego efektu\n- jeżeli jednostka nie ma [Shin_Rien], natychmiast go zyskuje\n\nprzy HP 25% lub mniej, zmienia wzorzec i znacznie wzmacnia pewną Umiejętność
37. [[mr7] Pasywka wroga [138101] — tekst klimatyczny] 누군가를 따라해야 하는 것만 같았고 그게 누군지 몰라 지령을 의심하고 거스를 뻔했지만, 뒤늦게 자신이 누구를 닮게 되었는지 깨닫고, 지령의 뜻을 받아들여 완성된 거짓 아비.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138101].flavor
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once, he harbored a suspicion that he was being shaped into an imitation of someone; he doubted the Will and nearly defied it, for he did not know whom he was to mimic. Only when it was too late did he understand its intent and come to accept the Prescript's will.\nOnly then was the false father completed.
   PL: Wydawało mu się, że musi naśladować kogoś — nie wiedział jednak kogo, więc wątpił w Wolę i niemal się jej sprzeciwił. Dopiero, gdy było już za późno, zrozumiał jej zamiar i przyjął wolę Nakazu.\nDopiero wtedy ukończono fałszywego ojca.
38. [[mr7] Pasywka wroga [138102] — nazwa] 신탁 단말기 [카두세우스] - 완전 해금
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138102].name
   limit: do 60 znaków
   EN: Oracle Device [Caduceus] - Full Unlock
   PL: Oracle Device [Caduceus] - Full Unlock
39. [[mr7] Pasywka wroga [138102] — opis] <color=#ff6000><mark=#ff000040><b><u>코인마다 무기가 무작위로 정해지며 특수 효과 적용</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\n공격 스킬 사용 시, [StackRienSpecialSkill] 1 얻음 (최대 9)\n- 스킬별 1회 획득 가능 (동일한 스킬로 2 이상 획득 불가)\n- 특수 패턴에서만 사용하는 스킬로는 얻지 않음\n\n턴 시작 시 [StackRienSpecialSkill]가 9면, 강력한 스킬 사용\n- 스킬 종류별 [StackRienSpecialSkill] 획득 여부 초기화\n- 속도 최솟값, 최댓값 +15\n- 턴 종료 시 다음 턴에, [Vulnerable] 2, [ResultReduction] 3 얻음\n\n페이즈가 변경된 턴부터 효과 발동\n- 세 턴마다 [StackRienSpecialSkill]가 9 미만이면,\n9까지 증가하고 (증가한 수치 x 5)만큼 [KarmaOfIndexRien_2Phase] 얻음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138102].desc
   limit: do 1240 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [RienWeapon01Hatchet2phase], [RienWeapon02Stiletto2phase], [RienWeapon03Greatsword2phase], [RienWeapon04Rapier2phase], [RienWeapon05Sledgehammer2phase], [RienWeapon06Ultragreatsword2phase], [RienWeapon07Lance2phase], [RienWeapon08Chain2phase], [RienWeapon09Scythe2phase], [StackRienSpecialSkill], [Vulnerable], [ResultReduction], [KarmaOfIndexRien_2Phase]
   znaczenie tagów: [RienWeapon01Hatchet2phase] = 손도끼로 갈비뼈를 찍어 내릴 때는… / When hacking through the ribs with a hatchet...; [RienWeapon02Stiletto2phase] = 스틸레토로 허파를 꿰뚫을 때는… / When penetrating the lungs with a stiletto...; [RienWeapon03Greatsword2phase] = 바스타드 소드로 어깨와 머리를 짓이길 때는… / When cleaving through the shoulder and the skull with a bastard sword...; [RienWeapon04Rapier2phase] = 레이피어로 몸에 10개 이상의 구멍을 내야할 때는… / When punching 10 or more holes in the torso with a rapier...; [RienWeapon05Sledgehammer2phase] = 망치로 뒤통수를 으깨야 할 때는… / When caving in the back of the skull with a hammer...; [RienWeapon06Ultragreatsword2phase] = 커다란 검으로 몸통을 갈라야 할 때는… / When rending the body with a great sword...; [RienWeapon07Lance2phase] = 랜스로 20인치의 구멍을 내야 할 때는… / When boring a 20-inch hole with a lance...; [RienWeapon08Chain2phase] = 채찍으로 살점을 만 갈래 떼어내야 할 때는… / When ripping the flesh to ten thousand strips with a whip... …
   EN: <color=#ff6000><mark=#ff000040><b><u>A random weapon is assigned to every Coin. Each weapon has a unique effect.</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nWhen using an Attack Skill, gain 1 [StackRienSpecialSkill] (max 9)\n- Can be gained once per Skill; does not gain Stack from the same Skill twice\n- Does not gain Stack from a Skill used only in a special pattern\n\nTurn Start: At 9 [StackRienSpecialSkill] Stacks, use a powerful Skill\n- Reset the per-Skill [StackRienSpecialSkill] cap\n- Min & Max Speed +15\n- Turn End: Gain 2 [Vulnerable] and 3 [ResultReduction] next turn\n\nActivate the following, starting from the turn in which the phase changed\n- Every 3 turns, at less than 9 [StackRienSpecialSkill], bring its Stack to 9; then, gain (Stack gained x 5) [KarmaOfIndexRien_2Phase]
   PL: <color=#ff6000><mark=#ff000040><b><u>do każdej Monety przypisywana jest losowa broń; każda broń ma unikalny efekt</u></b></mark></color>\n- [RienWeapon01Hatchet2phase]\n- [RienWeapon02Stiletto2phase]\n- [RienWeapon03Greatsword2phase]\n- [RienWeapon04Rapier2phase]\n- [RienWeapon05Sledgehammer2phase]\n- [RienWeapon06Ultragreatsword2phase]\n- [RienWeapon07Lance2phase]\n- [RienWeapon08Chain2phase]\n- [RienWeapon09Scythe2phase]\n\nprzy użyciu Umiejętności ataku, zyskuje 1 [StackRienSpecialSkill] (maks. 9)\n- można zyskać 1 raz na Umiejętność (nie można zyskać 2 razy od tej samej Umiejętności)\n- nie zyskuje Liczników od Umiejętności używanej tylko w specjalnym wzorcu\n\nna początku tury, przy 9 Licznikach [StackRienSpecialSkill], używa potężnej Umiejętności\n- resetuje limit zyskiwania [StackRienSpecialSkill] na Umiejętność\n- Minimalna i Maksymalna Szybkość +15\n- na koniec tury, w następnej turze zyskuje 2 [Vulnerable] i 3 [ResultReduction]\n\nuruchamia następujące efekty od tury, w której zmieniono fazę\n- co 3 tury, jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, zwiększa go do 9 i zyskuje (zyskana wartość x 5) [KarmaOfIndexRien_2Phase]
40. [[mr7] Pasywka wroga [138102] — tekst klimatyczny] 전파를 통해 지령을 보내는 도시의 신, 헤르메스가 선사한 최고의 무기이자 저주.
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138102].flavor
   limit: do 160 znaków
   EN: An unparalleled weapon and a curse bestowed by Hermes, a god of the City whose Prescripts are distributed by radio waves.
   PL: Bezkonkurencyjna broń i klątwa — dar Hermesa, boga Miasta, którego Nakazy rozsyłane są falami radiowymi.
41. [[mr7] Pasywka wroga [138103] — nazwa] 지령의 뜻
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138103].name
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [[mr7] Pasywka wroga [138103] — opis] 턴 시작 시,\n- 무작위 수감자에게 [IndexPrescriptTargetToPersonality]을 부여하고, 우선 공격함\n<color=#ff6000><mark=#ff000040><b><u>- [IndexPrescriptTargetToPersonality]에게 사용하는 스킬의 코인이 전부 [SuperCoin]으로 변경됨</u></b></mark></color>\n- [BlessingOfIndexPrescriptEnemy]만큼 [Protection] 얻음 (최대 9)\n<color=#ff6000><mark=#ff000040><b><u>· [KarmaOfIndexRien_2Phase] 20당, 1 감소</u></b></mark></color>\n\n공격 시 [IndexPrescriptTargetToPersonality]이 사망하거나 대상을 공격하지 못하게 될 경우,\n<color=#ff6000><mark=#ff000040><b><u>사용하지 않은 나머지 스킬을 다른 무작위 수감자에게 사용\n- 현재 체력이 가장 낮은 대상 우선 (체력 1인 경우 제외)\n- 무작위로 선택된 수감자가 사망하거나 체력이 1이 될 경우, 다른 수감자에게 반복</u></b></mark></color>\n\n[BlessingOfIndexPrescriptEnemy]당 [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +5% (최대 40%)\n- [BlessingOfIndexPrescriptEnemy]가 9면, 대신 모든 대상에게 가하는 피해량 +50%\n\n페이즈가 변경된 턴부터 효과 발동\n- 턴 시작 시 [BlackNightmare] 얻음\n· 직전 턴에 강력한 스킬을 사용하였으면, 해당 턴에는 [BlackNightmare] 사라짐\n- [BlackNightmare]을 얻을 때 [StackRienSpecialSkill]가 9 미만이면, 특수 패턴 발동
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138103].desc
   limit: do 1570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescriptTargetToPersonality], [SuperCoin], [BlessingOfIndexPrescriptEnemy], [Protection], [KarmaOfIndexRien_2Phase], [BlackNightmare], [StackRienSpecialSkill]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [Protection] = 보호 / Protection; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]; [BlackNightmare] = 지령 탐닉 / Indulgence in Prescripts; [StackRienSpecialSkill] = 대행 [헤르메스] / Procuration [Hermes]
   EN: Turn Start:\n- Apply [IndexPrescriptTargetToPersonality] against a random Sinner, and prioritize attacking them\n<color=#ff6000><mark=#ff000040><b><u>- When using a Skill against [IndexPrescriptTargetToPersonality], convert all Coins on that Skill to [SuperCoin]s</u></b></mark></color>\n- Gain [Protection] equal to [BlessingOfIndexPrescriptEnemy] (max 9)\n<color=#ff6000><mark=#ff000040><b><u>\n· Lose 1 Stack for every 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\nWhen attacking, if [IndexPrescriptTargetToPersonality] is killed, or if this unit can no longer attack that target, <color=#ff6000><mark=#ff000040><b><u>use the remaining Skills against a random other Sinner\n- Prioritizes targets with the least current HP, unless they have 1 HP\n- When the randomly chosen Sinner is killed, or if the said Sinner's HP is brought down to 1, repeat this effect on another Sinner</u></b></mark></color>\n\nDeal +5% damage against [IndexPrescriptTargetToPersonality] for every [BlessingOfIndexPrescriptEnemy] (max 40%)\n- At 9 [BlessingOfIndexPrescriptEnemy], deal +50% damage against all targets\n\nStarting from the first turn after the phase change, activate the following effects:\n- Turn Start: Gain [BlackNightmare]\n· If this unit used a powerful attack in the previous turn, lose [BlackNightmare] for that turn\n- When gaining [BlackNightmare], if this unit has fewer than 9 [StackRienSpecialSkill] Stacks, activate a unique pattern
   PL: na początku tury:\n- nakłada [IndexPrescriptTargetToPersonality] losowemu Grzesznikowi i priorytet: atakowanie go\n<color=#ff6000><mark=#ff000040><b><u>- gdy używa Umiejętności na [IndexPrescriptTargetToPersonality], wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y</u></b></mark></color>\n- zyskuje [Protection] równe [BlessingOfIndexPrescriptEnemy] (maks. 9)\n<color=#ff6000><mark=#ff000040><b><u>\n· traci 1 Licznika za każde 20 [KarmaOfIndexRien_2Phase]</u></b></mark></color>\n\ngdy atakuje, jeżeli [IndexPrescriptTargetToPersonality] zginie albo jednostka nie może już zaatakować tego celu, <color=#ff6000><mark=#ff000040><b><u>używa pozostałych Umiejętności na losowym innym Grzeszniku\n- priorytet: cele z najmniejszym aktualnym HP, z wyjątkiem celów z 1 HP\n- jeżeli losowo wybrany Grzesznik zginie albo jego HP spadnie do 1, powtarza ten efekt na innym Grzeszniku</u></b></mark></color>\n\nzadaje +5% obrażeń [IndexPrescriptTargetToPersonality] za każdy [BlessingOfIndexPrescriptEnemy] (maks. 40%)\n- przy 9 [BlessingOfIndexPrescriptEnemy], zamiast tego zadaje +50% obrażeń wszystkim celom\n\nuruchamia następujące efekty od pierwszej tury po zmianie fazy:\n- na początku tury, zyskuje [BlackNightmare]\n· jeżeli jednostka użyła potężnego ataku w poprzedniej turze, w tej turze nie ma [BlackNightmare]\n- przy zyskiwaniu [BlackNightmare], jeżeli Licznik [StackRienSpecialSkill] jest niższy niż 9, uruchamia specjalny wzorzec
43. [[mr7] Pasywka wroga [138103] — tekst klimatyczny] 가족을 꾸렸습니다.\n\n“당신은 지금 이곳에 있으면 안될 텐데.”\n“아직 작업이 한창이다. 무엇보다 섬세하고 아름답게 장식하고 있거든.”\n“…네놈, 설마 지령을 거스를 셈인가.”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138103].flavor
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I raised a family.\n\n"You're not supposed to be here right now."\n"My work is still much underway, and I'd like to carve them up in peace so they can attain the most exquisite beauty I can sculpt."\n"... Don't tell me, are you here to defy the Prescript?"
   PL: Założyłem rodzinę.\n\n„Nie powinieneś tu teraz być.”\n„Moje dzieło wciąż trwa. Wolałbym rzeźbić je w spokoju, by osiągnęło najdoskonalsze piękno, jakie potrafię wyrzeźbić.”\n„…Nie mów mi, że przyszedłeś sprzeniewierzyć się Nakazowi.”
44. [[mr7] Pasywka wroga [138104] — nazwa] 지령 수행
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138104].name
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [[mr7] Pasywka wroga [138104] — opis] 이번 턴에 [IndexPrescript_Base_2nd]을 수행했으면,\n턴 종료 시 정신력 15 회복, [BlessingOfIndexPrescriptEnemy] 1 얻음 (턴당 1회)\n\n이번 턴에 <color=#ff6000><mark=#ff000040><b><u>[IndexPrescript_Base_2nd]을 수행하지 못했으면,\n턴 종료 시 [KarmaOfIndexRien_2Phase] 8 얻고 [BlessingOfIndexPrescriptEnemy] 1 잃음</u></b></mark></color>\n- 강력한 스킬을 사용한 턴일 경우, 대신 [KarmaOfIndexRien_2Phase] 12 얻고 [BlessingOfIndexPrescriptEnemy] 2 잃음
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138104].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [IndexPrescript_Base_2nd], [BlessingOfIndexPrescriptEnemy], [KarmaOfIndexRien_2Phase]
   znaczenie tagów: [IndexPrescript_Base_2nd] = 지령 / Prescript; [BlessingOfIndexPrescriptEnemy] = 지령의 가호 / Grace of the Prescript; [KarmaOfIndexRien_2Phase] = 카르마 [포르투나] / Karmic Consequence [Fortuna]
   EN: Turn End: If [IndexPrescript_Base_2nd] was executed this turn, heal 15 SP and gain 1 [BlessingOfIndexPrescriptEnemy] (once per turn)\n\n<color=#ff6000><mark=#ff000040><b><u>Turn End: If [IndexPrescript_Base_2nd] was not executed this turn, gain 8 [KarmaOfIndexRien_2Phase] and lose 1 [BlessingOfIndexPrescriptEnemy]</u></b></mark></color>\n- If this unit used a powerful Skill this turn, gain 12 [KarmaOfIndexRien_2Phase] and lose 2 [BlessingOfIndexPrescriptEnemy] instead
   PL: na koniec tury: jeżeli [IndexPrescript_Base_2nd] został wykonany w tej turze, przywraca 15 SP i zyskuje 1 [BlessingOfIndexPrescriptEnemy] (1 raz na turę)\n\n<color=#ff6000><mark=#ff000040><b><u>na koniec tury: jeżeli [IndexPrescript_Base_2nd] nie został wykonany w tej turze, zyskuje 8 [KarmaOfIndexRien_2Phase] i traci 1 [BlessingOfIndexPrescriptEnemy]</u></b></mark></color>\n- jeżeli jednostka użyła potężnej Umiejętności w tej turze, zamiast tego zyskuje 12 [KarmaOfIndexRien_2Phase] i traci 2 [BlessingOfIndexPrescriptEnemy]
46. [[mr7] Pasywka wroga [138104] — tekst klimatyczny] 가족을… 잃었습니다.\n \n“가지마…”\n“이대로 가지마… 아빠…  우리… 살려줘…”
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138104].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I... lost my family.\n\n"Don't go..."\n"Don't go... Not... like this... Daddy... Please... help us..."
   PL: Straciłem… rodzinę.\n \n„Nie odchodź…”\n„Nie odchodź… nie… tato… ratuj nas…”
47. [[mr7] Pasywka wroga [138301] — nazwa] 제 모든 신체 요소는 이미 티비아에
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138301].name
   limit: do 60 znaków
   EN: All of My Corpus has been Given to Tibia
   PL: All of My Corpus has been Given to Tibia
48. [[mr7] Pasywka wroga [138301] — opis] [Combustion], [Vibration], [Burst], [Sinking]으로 받는 체력, 정신력 피해량 -30%\n[Laceration]로 받는 피해량 -50%\n\n턴 시작 시, 흐트러짐 상태면 흐트러짐 해제. 이후 [CrimsonTakeDamageUp] 2 얻고 다음 턴까지 ‘설치 미술 제 3호 ‘간이늑골’’ 사용 불가능 (전투당 1회)\n\n턴 종료 시 자신의 [Combustion] 4당, 다음 턴에 [DefenseDown] 1 얻음 (최대 15)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138301].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration], [Burst], [Sinking], [Laceration], [CrimsonTakeDamageUp], [DefenseDown]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Laceration] = 출혈 / Bleed; [CrimsonTakeDamageUp] = 분노 취약 / Wrath Fragility; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Take -30% HP, SP damage from [Combustion], [Vibration], [Burst], and [Sinking]\nTake -50% damage from [Laceration]\n\nTurn Start: If this unit is Staggered, recover from Stagger. Afterward, gain 2 [CrimsonTakeDamageUp] and becomes unable to use 'Installation Art no. 3: Improvised Ribcage' until next turn (once per Encounter)\n\nTurn End: Gain 1 [DefenseDown] next turn for every 4 [Combustion] on self (max 15)
   PL: otrzymuje o 30% mniej obrażeń HP i SP od [Combustion], [Vibration], [Burst] i [Sinking]\notrzymuje o 50% mniej obrażeń od [Laceration]\n\nna początku tury, jeżeli jednostka jest Oszołomiona, dochodzi do siebie z Oszołamienia. następnie zyskuje 2 [CrimsonTakeDamageUp] i do następnej tury nie może używać „Installation Art no. 3: Improvised Ribcage” (1 raz na walkę)\n\nna koniec tury, zyskuje 1 [DefenseDown] w następnej turze za każde 4 [Combustion] jednostki (maks. 15)
49. [[mr7] Pasywka wroga [138306] — nazwa] 제자의 전시를 잠시 감상해 볼까요
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138306].name
   limit: do 70 znaków
   EN: Allow Me to Briefly Enjoy My Pupil's Exhibition
   PL: Allow Me to Briefly Enjoy My Pupil's Exhibition
50. [[mr7] Pasywka wroga [138306] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138306].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, [SupportProtect]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense
   EN: If this unit has [SupportProtect], <color=#ff6000><mark=#ff000040><b><u>lose 1 [SupportProtect] on Clash Start</u></b></mark></color> (once per Skill)
   PL: jeżeli jednostka ma [SupportProtect], <color=#ff6000><mark=#ff000040><b><u>na początku Starcia traci 1 [SupportProtect]</u></b></mark></color> (1 raz na Umiejętność)
51. [[mr7] Pasywka wroga [141704] — nazwa] 갤러리에서는 갤러리만의 감상 규칙이 있는 법
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141704].name
   limit: do 70 znaków
   EN: Visitors Must Respect the Rules of the Gallery
   PL: Visitors Must Respect the Rules of the Gallery
52. [[mr7] Pasywka wroga [141704] — opis] 자신에게 [SupportProtect]가 있으면, <color=#ff6000><mark=#ff000040><b><u>합 시작 시 [SupportProtect] 1 감소</u></b></mark></color> (스킬당 1회)
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141704].desc
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [[mr7] Pasywka wroga [141706] — nazwa] 마에스트로님의 앞에서 작품으로 증명해 보이겠어
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141706].name
   limit: do 80 znaków
   EN: With this Artwork, I will Prove Myself before the Maestro
   PL: With this Artwork, I will Prove Myself before the Maestro
54. [[mr7] Pasywka wroga [141706] — opis] 약지 아비 등장 시 자신의 정신력이 20미만이면, 정신력이 20이 됨
   źródło: Passives_Abnormality-mr7.json :: dataList[id=141706].desc
   limit: do 120 znaków
   EN: At less than 20 SP when the Ring Nursefather enters the Encounter, heal SP to 20
   PL: gdy Ojciec Serdecznego wchodzi na etap, jeżeli SP jednostki poniżej 20, przywraca SP do 20
55. [[mr7] Pasywka wroga [138302] — nazwa] 뛰어다니는 관객은 의자에 앉아 감상하시죠
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138302].name
   limit: do 60 znaków
   EN: Please, Do Stop Running and Be Seated
   PL: Please, Do Stop Running and Be Seated
56. [[mr7] Pasywka wroga [138302] — opis] 턴 종료 시 속도가 가장 빠른 수감자에게 다음 턴에 [RedemptionTheRings] 부여
   źródło: Passives_Abnormality-mr7.json :: dataList[id=138302].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedemptionTheRings]
   znaczenie tagów: [RedemptionTheRings] = 재료가 떨어지는 상처 / Ingredient-shedding Wound
   EN: Turn End: Inflict [RedemptionTheRings] next turn to the Sinner with the fastest Speed
   PL: na koniec tury, nakłada [RedemptionTheRings] w następnej turze na Grzesznika z najwyższą Szybkością

## [mr8] Pasywka wroga: Passives_Abnormality-mr8
- plik gry: `Passives_Abnormality-mr8.json`

57. [[mr8] Pasywka wroga [155101] — nazwa] 요리를 잘한다는 거예요
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155101].name
   limit: do 70 znaków
   EN: I can cook up delicious dishes so good, you hear?
   PL: I can cook up delicious dishes so good, you hear?
58. [[mr8] Pasywka wroga [155101] — opis] <color=#ff6000><mark=#ff000040><b><u>[SapsareeCooking] 보유 시, 턴의 마지막 순서에 ‘앗! 제 식사시간인거예요’ 스킬 사용</u></b></mark></color>\n(자신을 제외한 모든 대상이 사망했거나, 흐트러짐 상태에서는 발동하지 않음)\n턴 종료 시 ‘앗! 제 식사시간인거예요’ 스킬을 사용하지 못했다면, [SapsareeHungry] 1 얻음
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155101].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [SapsareeCooking], [SapsareeHungry]
   znaczenie tagów: [SapsareeCooking] = 토막난 요리재료 / Chopped Ingredients; [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: <color=#ff6000><mark=#ff000040><b><u>If this unit has [SapsareeCooking], use the "Aah! I'm on lunch break, you hear?" Skill at the very end of the turn</u></b></mark></color>\n(does not activate if all other targets are defeated, or if this unit is Staggered)\nTurn End: If this unit failed to use the "Aah! I'm on lunch break, you hear?" Skill, gain 1 [SapsareeHungry]
   PL: <color=#ff6000><mark=#ff000040><b><u>jeżeli jednostka ma [SapsareeCooking], używa Umiejętności „Aah! I'm on lunch break, you hear?” na samym końcu tury</u></b></mark></color>\n(nie uruchamia się, jeżeli wszystkie inne cele zostały pokonane albo jednostka jest Oszołomiona)\nna koniec tury, jeżeli jednostka nie użyła Umiejętności „Aah! I'm on lunch break, you hear?”, zyskuje 1 [SapsareeHungry]
59. [[mr8] Pasywka wroga [155101] — tekst klimatyczny] 5층 레스토랑에서 이런 건 요리라 불러주지도 않는다.
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155101].flavor
   limit: do 120 znaków
   EN: The restaurant on 5F would not dignify this with the word "cooking."
   PL: Restauracja na 5. piętrze nie nazwałaby tego nawet „gotowaniem”.
60. [[mr8] Pasywka wroga [155702] — nazwa] 핸드메이드
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155702].name
   limit: do 40 znaków
   EN: Handmade
   PL: Handmade
61. [[mr8] Pasywka wroga [155702] — opis] 전장의 바늘이[TabExplain] 1개당 스킬 최종 위력 +1
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155702].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Skill Final Power +1 for every Needlekin[TabExplain] on the field
   PL: Moc Końcowa Umiejętności +1 za każdego Needlekin[TabExplain] na polu walki
62. [[mr8] Pasywka wroga [155702] — tekst klimatyczny] 손 바느질은 숙련된 기능공들의 수가 생명이다.
   źródło: Passives_Abnormality-mr8.json :: dataList[id=155702].flavor
   limit: do 150 znaków
   EN: No hand sewing survives on one pair of hands alone. A host of practiced artisans are needed to breathe life into it.
   PL: Ręczne szycie nie przetrwa na jednej parze rąk. Potrzeba tłumu wprawionych rzemieślników, by tchnąć w nie życie.
63. [[mr8] Pasywka wroga [156301] — nazwa] 르누아르 개버딘 원단
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156301].name
   limit: do 40 znaków
   EN: Le Noir: Gabardine Fabric
   PL: Le Noir: Gabardine Fabric
64. [[mr8] Pasywka wroga [156301] — opis] 스테이지 시작 시, [NoirSuit] 30 얻음\n\n턴 시작 시,\n- 자신의 최대 체력의 ([NoirSuit]/5)%만큼 보호막 얻음 (흐트러진 경우 제외)
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156301].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSuit]
   znaczenie tagów: [NoirSuit] = 르누아르 개버딘 원단 코트 / Le Noir: Gabardine Overcoat
   EN: Encounter Start: Gain 30 [NoirSuit]\n\nTurn Start: Gain Shield equal to ([NoirSuit] / 5)% of this unit's max HP (unless Staggered)
   PL: przy wejściu na etap, zyskuje 30 [NoirSuit]\n\nna początku tury, zyskuje Tarczę równą ([NoirSuit] / 5)% Maks. HP jednostki (chyba że jest Oszołomiona)
65. [[mr8] Pasywka wroga [156301] — tekst klimatyczny] 포멀하면서도 탄탄함을 지향하는 르누아르가 선보이는 플래그쉽 원단.
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156301].flavor
   limit: do 120 znaków
   EN: The Noirs' flagship gabardine, tailored toward formality without sacrificing firmness.
   PL: Flagowe sukno Le Noir — uszyte z myślą o formalności, bez poświęcania stabilności.
66. [[mr8] Pasywka wroga [156403] — nazwa] 진형 보존
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156403].name
   limit: do 40 znaków
   EN: Formation Conservation
   PL: Formation Conservation
67. [[mr8] Pasywka wroga [156403] — opis] 르누아르 소속 아군의 레벨이 대폭 증가\n\n전장에 생존한 르누아르 소속 아군 1명당 모든 르누아르 소속 아군이 받는 피해량 -5%\n르누아르 소속 아군 사망시, 이번 전투 동안 모든 르누아르 소속 아군이 [NoirSquareCollapse] 1 얻음 (새로 등장하는 유닛 포함)
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156403].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [NoirSquareCollapse]
   znaczenie tagów: [NoirSquareCollapse] = 진형 붕괴 / Formation Collapse
   EN: Boost the level of "Le Noir" allies\n\nAll "Le Noir" allies take -5% damage for every living "Le Noir" ally on the field\nOn death of a "Le Noir" ally, all "Le Noir" allies gain 1 [NoirSquareCollapse] for the rest of this Encounter (including newly summoned units)
   PL: zwiększa Poziom sojuszników „Le Noir”\n\nwszyscy sojusznicy „Le Noir” otrzymują o 5% mniej obrażeń za każdego żywego sojusznika „Le Noir” na polu walki\npo śmierci sojusznika „Le Noir”, wszyscy sojusznicy „Le Noir” zyskują 1 [NoirSquareCollapse] przez resztę tej walki (łącznie z nowo przywołanymi jednostkami)
68. [[mr8] Pasywka wroga [156403] — tekst klimatyczny] 하나하나 자리를 지켜 업무를 수행하고 그 모습들이 모여 하나의 진형이되고 그 진형은 전체를 보존하기 위한 도상이되니, 각자의 자리에서 맡은 바를 충실히 이행하라.
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156403].flavor
   limit: do 300 znaków
   EN: Each stays at their post and faithfully performs the duty entrusted to them. Together, they form a formation, and that formation becomes an image that preserves the whole. Fulfill thy charge faithfully, each in thine appointed place.
   PL: Każdy trwa na swoim posterunku i wiernie spełnia powierzoną mu powinność. Razem tworzą szyk, a szyk ten staje się wyobrażeniem zachowującym całość. Wiernie wypełnij twój obowiązek, każdy na twoim wyznaczonym miejscu.
69. [[mr8] Pasywka wroga [156404] — nazwa] 전투 속행
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156404].name
   limit: do 40 znaków
   EN: The Battle Continues
   PL: The Battle Continues
70. [[mr8] Pasywka wroga [156404] — opis] 스테이지 시작시, 정신력이 45인 상태로 시작
   źródło: Passives_Abnormality-mr8.json :: dataList[id=156404].desc
   limit: do 120 znaków
   EN: Start this Encounter with 45 SP
   PL: rozpoczyna tę walkę z 45 SP

## [night-clean-up-re] Pasywka wroga: Passives_Abnormality-night-clean-up-re
- plik gry: `Passives_Abnormality-night-clean-up-re.json`

71. [[night-clean-up-re] Pasywka wroga [9018601] — nazwa] 하달받은 명령
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=9018601].name
   limit: do 40 znaków
   EN: Received Mission
   PL: Received Mission
72. [[night-clean-up-re] Pasywka wroga [9018601] — opis] 스테이지 시작 시, [RepressedMurderousIntendHard]를 얻음
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=9018601].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RepressedMurderousIntendHard]
   znaczenie tagów: [RepressedMurderousIntendHard] = 억눌린 살기 / Repressed Bloodthirst
   EN: Encounter Start: Gain [RepressedMurderousIntendHard]
   PL: przy wejściu na etap, zyskuje [RepressedMurderousIntendHard]
73. [[night-clean-up-re] Pasywka wroga [9018705] — nazwa] 뒷골목의 밤
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=9018705].name
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
74. [[night-clean-up-re] Pasywka wroga [9018705] — opis] 2웨이브 이후로 등장할 경우, 정신력 30으로 등장함\n이 전투에 참여중인 모든 유닛은 퇴각 불가
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=9018705].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When joining after Wave 2, enter with 30 SP\nAll units participating in this battle cannot retreat
   PL: jeżeli wchodzi po Drugiej Fali, wchodzi z 30 SP\nwszystkie jednostki biorące udział w tej walce nie mogą się wycofać
75. [[night-clean-up-re] Pasywka wroga [142001] — nazwa] 부여받은 명령
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=142001].name
   limit: do 40 znaków
   EN: Bestowed Mission
   PL: Bestowed Mission
76. [[night-clean-up-re] Pasywka wroga [142001] — opis] 스테이지 시작 시, [WeighedMurderousIntendHard]를 얻음
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=142001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WeighedMurderousIntendHard]
   znaczenie tagów: [WeighedMurderousIntendHard] = 짓눌린 살기 / Crushed Bloodthirst
   EN: Encounter Start: Gain [WeighedMurderousIntendHard]
   PL: przy wejściu na etap, zyskuje [WeighedMurderousIntendHard]
77. [[night-clean-up-re] Pasywka wroga [142101] — nazwa] 전투 부상
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=142101].name
   limit: do 40 znaków
   EN: Wounded in Battle
   PL: Wounded in Battle
78. [[night-clean-up-re] Pasywka wroga [142101] — opis] 최대 체력의 10% 만큼 체력이 감소한 상태로 전투 시작 (부위 포함)
   źródło: Passives_Abnormality-night-clean-up-re.json :: dataList[id=142101].desc
   limit: do 120 znaków
   EN: Begins Encounter with 10% less HP (including Parts)
   PL: rozpoczyna walkę z 10% mniej HP (łącznie z Częściami)

## [pilgrimage] Wróg / część: Enemies-pilgrimage
- plik gry: `Enemies-pilgrimage.json`

79. [[pilgrimage] Wróg / część [91027] — nazwa] 해안의 폭주자
   źródło: Enemies-pilgrimage.json :: dataList[id=91027].name
   limit: do 40 znaków
   EN: Shell Sea Runner
   PL: Shell Sea Runner
80. [[pilgrimage] Wróg / część [91027] — opis] 일반 적
   źródło: Enemies-pilgrimage.json :: dataList[id=91027].desc
   limit: do 120 znaków
   EN: Regular Enemy
   PL: Regular Enemy
81. [[pilgrimage] Wróg / część [91028] — nazwa] 저해의 활주자
   źródło: Enemies-pilgrimage.json :: dataList[id=91028].name
   limit: do 40 znaków
   EN: Deep Sea Slider
   PL: Deep Sea Slider
82. [[pilgrimage] Wróg / część [91028] — opis] 일반 적
   źródło: Enemies-pilgrimage.json :: dataList[id=91028].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [[pilgrimage] Wróg / część [91029] — nazwa] 발해의 수확자
   źródło: Enemies-pilgrimage.json :: dataList[id=91029].name
   limit: do 40 znaków
   EN: Basin Sea Reaper
   PL: Basin Sea Reaper
84. [[pilgrimage] Wróg / część [91029] — opis] 일반 적
   źródło: Enemies-pilgrimage.json :: dataList[id=91029].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [[pilgrimage] Wróg / część [91030] — nazwa] 심해의 정초자
   źródło: Enemies-pilgrimage.json :: dataList[id=91030].name
   limit: do 40 znaków
   EN: Nethersea Founder
   PL: Nethersea Founder
86. [[pilgrimage] Wróg / część [91030] — opis] 일반 적
   źródło: Enemies-pilgrimage.json :: dataList[id=91030].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [[pilgrimage] Wróg / część [91031] — nazwa] 심해의 분출자
   źródło: Enemies-pilgrimage.json :: dataList[id=91031].name
   limit: do 40 znaków
   EN: Nethersea Spewer
   PL: Nethersea Spewer
88. [[pilgrimage] Wróg / część [91031] — opis] 일반 적
   źródło: Enemies-pilgrimage.json :: dataList[id=91031].desc
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [[pilgrimage] Wróg / część [91032] — nazwa] 성도의 손
   źródło: Enemies-pilgrimage.json :: dataList[id=91032].name
   limit: do 40 znaków
   EN: Hand of the Saint
   PL: Hand of the Saint
90. [[pilgrimage] Wróg / część [91032] — opis] 기믹용
   źródło: Enemies-pilgrimage.json :: dataList[id=91032].desc
   limit: do 120 znaków
   EN: Gimmick
   PL: Gimmick
91. [[pilgrimage] Wróg / część [1292] — nazwa] 해안의 폭주자
   źródło: Enemies-pilgrimage.json :: dataList[id=1292].name
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [[pilgrimage] Wróg / część [1292] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1292].desc
   limit: do 120 znaków
   EN: Core
   PL: Core
93. [[pilgrimage] Wróg / część [1293] — nazwa] 저해의 활주자
   źródło: Enemies-pilgrimage.json :: dataList[id=1293].name
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [[pilgrimage] Wróg / część [1293] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1293].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [[pilgrimage] Wróg / część [1294] — nazwa] 발해의 수확자
   źródło: Enemies-pilgrimage.json :: dataList[id=1294].name
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [[pilgrimage] Wróg / część [1294] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1294].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [[pilgrimage] Wróg / część [1295] — nazwa] 심해의 정초자
   źródło: Enemies-pilgrimage.json :: dataList[id=1295].name
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [[pilgrimage] Wróg / część [1295] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1295].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [[pilgrimage] Wróg / część [1296] — nazwa] 심해의 분출자
   źródło: Enemies-pilgrimage.json :: dataList[id=1296].name
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [[pilgrimage] Wróg / część [1296] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1296].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [[pilgrimage] Wróg / część [1289] — nazwa] 날렵한 심해 신도
   źródło: Enemies-pilgrimage.json :: dataList[id=1289].name
   limit: do 40 znaków
   EN: Swift Cultist of the Deep
   PL: Swift Cultist of the Deep
102. [[pilgrimage] Wróg / część [1289] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1289].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [[pilgrimage] Wróg / część [1290] — nazwa] 끈질긴 심해 신도
   źródło: Enemies-pilgrimage.json :: dataList[id=1290].name
   limit: do 50 znaków
   EN: Steadfast Cultist of the Deep
   PL: Steadfast Cultist of the Deep
104. [[pilgrimage] Wróg / część [1290] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1290].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [[pilgrimage] Wróg / część [1291] — nazwa] 파비우스
   źródło: Enemies-pilgrimage.json :: dataList[id=1291].name
   limit: do 40 znaków
   EN: Fabius
   PL: Fabius
106. [[pilgrimage] Wróg / część [1291] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1291].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [[pilgrimage] Wróg / część [1298] — nazwa] 파비우스
   źródło: Enemies-pilgrimage.json :: dataList[id=1298].name
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [[pilgrimage] Wróg / część [1298] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1298].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [[pilgrimage] Wróg / część [1288] — nazwa] 마지막 기사
   źródło: Enemies-pilgrimage.json :: dataList[id=1288].name
   limit: do 40 znaków
   EN: The Last Knight
   PL: The Last Knight
110. [[pilgrimage] Wróg / część [1288] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1288].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [[pilgrimage] Wróg / część [1297] — nazwa] 선망하여 표류하는 메이어스
   źródło: Enemies-pilgrimage.json :: dataList[id=1297].name
   limit: do 40 znaków
   EN: Mayors, the Yearning Flotsam
   PL: Mayors, the Yearning Flotsam
112. [[pilgrimage] Wróg / część [1297] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1297].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [[pilgrimage] Wróg / część [1299] — nazwa] 성도의 손
   źródło: Enemies-pilgrimage.json :: dataList[id=1299].name
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [[pilgrimage] Wróg / część [1299] — opis] 본체
   źródło: Enemies-pilgrimage.json :: dataList[id=1299].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [[pilgrimage] Wróg / część [129901] — nazwa] 장치
   źródło: Enemies-pilgrimage.json :: dataList[id=129901].name
   limit: do 40 znaków
   EN: Device
   PL: Device
116. [[pilgrimage] Wróg / część [129901] — opis] 부위
   źródło: Enemies-pilgrimage.json :: dataList[id=129901].desc
   limit: do 120 znaków
   EN: Part
   PL: Część

## [pilgrimage] Umiejętności wrogów / Anomalii — Skills_Abnormality-pilgrimage
- grupa rozdziału/trybu: `pilgrimage` · plik: `Skills_Abnormality-pilgrimage.json`

117. [Umiejętność wroga [128801] (ulepszenie 1) — nazwa] 파도를 꿰뚫는 창
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128801].levelList[level=1].name
   limit: do 40 znaków
   EN: Tidepiercer Lance
   PL: Tidepiercer Lance
118. [Umiejętność wroga [128801] (ulepszenie 1) — opis] [WhenUse] [ColdAirDOQ]를 보유한 적 2명 당, 합 위력 +1 (최대 2)\n[WhenUse] 대상의 [ColdAirDOQ] 1당 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128801].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ColdAirDOQ]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ColdAirDOQ] = 냉기 / Cold
   EN: [WhenUse] Clash Power +1 for every 2 enemies with [ColdAirDOQ] (max 2)\n[WhenUse] Final Power +1 for every [ColdAirDOQ] on target (max 2)
   PL: [WhenUse] Moc Starcia +1 za każdych 2 wrogów z [ColdAirDOQ] (maks. 2)\n[WhenUse] Moc Końcowa +1 za każdy [ColdAirDOQ] celu (maks. 2)
119. [Umiejętność wroga [128801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada +2 Licznika [Sinking]
120. [Umiejętność wroga [128802] (ulepszenie 1) — nazwa] 파도를 부수는 창
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128802].levelList[level=1].name
   limit: do 40 znaków
   EN: Tidebreaker Lance
   PL: Tidebreaker Lance
121. [Umiejętność wroga [128802] (ulepszenie 1) — opis] [WhenUse] [ColdAirDOQ]를 보유한 적 2명 당, 기본 위력 +1 (최대 2)\n[WhenUse] 메인 타겟에게 [ColdAirDOQ]가 존재할 시 가중치 + 1\n[WhenUse] 메인 타겟의 [ColdAirDOQ] 1당 최종 위력 +1 (최대 2)\n[DefeatDuel] 피해량이 50% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128802].levelList[level=1].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ColdAirDOQ], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ColdAirDOQ] = 냉기 / Cold; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Base Power +1 for every 2 enemies with [ColdAirDOQ] (max 2)\n[WhenUse] If the main target has [ColdAirDOQ], gain +1 Atk Weight\n[WhenUse] Final Power +1 for every [ColdAirDOQ] on the main target (max 2)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: [WhenUse] Moc Bazowa +1 za każdych 2 wrogów z [ColdAirDOQ] (maks. 2)\n[WhenUse] jeżeli główny cel ma [ColdAirDOQ], Waga Ataku +1\n[WhenUse] Moc Końcowa +1 za każdy [ColdAirDOQ] głównego celu (maks. 2)\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
122. [Umiejętność wroga [128802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가\n- 대상이 [ColdAirDOQ]를 보유하고 있으면 [Sinking] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [OnSucceedAttack], [Sinking], [ColdAirDOQ]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [ColdAirDOQ] = 냉기 / Cold
   EN: [OnSucceedAttack] Inflict +2 [Sinking] Count\n- If target has [ColdAirDOQ], inflict 1 [Sinking]
   PL: [OnSucceedAttack] nakłada +2 Licznika [Sinking]\n- jeżeli cel ma [ColdAirDOQ], nakłada 1 [Sinking]
123. [Umiejętność wroga [128802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL: [SuperCoin]
124. [Umiejętność wroga [128802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking]
125. [Umiejętność wroga [128803] (ulepszenie 1) — nazwa] 파도 사냥
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].name
   limit: do 40 znaków
   EN: Tide-Hunt
   PL: Tide-Hunt
126. [Umiejętność wroga [128803] (ulepszenie 1) — opis] [FreezingDOQ]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] [FreezingDOQ]을 보유한 대상을 공격할 시 공격 가중치 + 2\n[WhenUse] [ColdAirDOQ]를 보유한 적 2명당, 코인 위력 +1 (최대 2)\n[DefeatDuel] 피해량이 50% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [FreezingDOQ], [WhenUse], [ColdAirDOQ], [DefeatDuel]
   znaczenie tagów: [FreezingDOQ] = 빙결 / Frozen; [WhenUse] = [사용시] / [On Use]; [ColdAirDOQ] = 냉기 / Cold; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [FreezingDOQ]\nCan Clash with this Skill regardless of Speed\n[WhenUse] When attacking targets with [FreezingDOQ], gain +2 Atk Weight\n[WhenUse] Coin Power +1 for every 2 enemies with [ColdAirDOQ] (max 2)\n[DefeatDuel] Deal -50% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cele z [FreezingDOQ]\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] atakując cele z [FreezingDOQ], zyskuje Wagę Ataku +2\n[WhenUse] Moc Monety +1 za każdych 2 wrogów z [ColdAirDOQ] (maks. 2)\n[DefeatDuel] zadaje o 50% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
127. [Umiejętność wroga [128803] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 3 [Sinking]
   PL: [OnSucceedAttack] nakłada 3 [Sinking]
128. [Umiejętność wroga [128803] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [AttackUp] 3 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [AttackUp]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttackHead] Gain 3 [AttackUp] (once per turn)
   PL: [OnSucceedAttackHead] zyskuje 3 [AttackUp] (1 raz na turę)
129. [Umiejętność wroga [128803] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Umiejętność wroga [128803] (ulepszenie 1) — moneta 3, efekt 2 — opis] [EnemyKill] 대상이 [FreezingDOQ]을 보유한 상태라면 정신력 20 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128803].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EnemyKill], [FreezingDOQ]
   znaczenie tagów: [EnemyKill] = [적 처치 시] / [On Kill]; [FreezingDOQ] = 빙결 / Frozen
   EN: [EnemyKill] If target has [FreezingDOQ], heal 20 SP
   PL: [EnemyKill] jeżeli cel ma [FreezingDOQ], przywraca 20 SP
131. [Umiejętność wroga [128804] (ulepszenie 1) — nazwa] 바다를 죽여라, 바다를 죽여!!
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].name
   limit: do 50 znaków
   EN: Slay the Ocean, Slay the Ocean!!
   PL: Slay the Ocean, Slay the Ocean!!
132. [Umiejętność wroga [128804] (ulepszenie 1) — opis] [CantDuel]\n[WhenUse] [ColdAirDOQ]를 보유한 적 1명 당, 피해량 +5% (최대 30%)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [ColdAirDOQ]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [ColdAirDOQ] = 냉기 / Cold
   EN: [CantDuel]\n[WhenUse] Deal +5% damage for every enemy with [ColdAirDOQ] (max 30%)
   PL: [CantDuel]\n[WhenUse] zadaje +5% obrażeń za każdego wroga z [ColdAirDOQ] (maks. 30%)
133. [Umiejętność wroga [128804] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 5 [Sinking]
   PL: [OnSucceedAttack] nakłada 5 [Sinking]
134. [Umiejętność wroga [128804] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [OnSucceedAttack] nakłada +1 Licznika [Sinking]
135. [Umiejętność wroga [128804] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] [AttackUp] 3 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Umiejętność wroga [128804] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] (1 + 대상의 [ColdAirDOQ] 수치) x 10 만큼 추가 우울 피해
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ColdAirDOQ]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ColdAirDOQ] = 냉기 / Cold
   EN: [OnSucceedAttack] Inflict 10(1 + [ColdAirDOQ] on target) bonus Gloom damage
   PL: [OnSucceedAttack] zadaje dodatkowe obrażenia Posępności równe 10(1 + Licznik [ColdAirDOQ] celu)
137. [Umiejętność wroga [128804] (ulepszenie 1) — moneta 3, efekt 2 — opis] [EnemyKill] 대상이 [FreezingDOQ]을 보유한 상태라면 정신력 20 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128804].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Umiejętność wroga [128805] (ulepszenie 1) — nazwa] 바다를 죽여라, 바다를 죽여!!
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].name
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Umiejętność wroga [128805] (ulepszenie 1) — opis] [FreezingDOQ]을 보유한 대상을 우선으로 지정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[WhenUse] [ColdAirDOQ]를 보유한 걸린 적 1명 당, 피해량 +5% (최대 30%)\n[WhenUse] [ColdAirDOQ]를 보유한 적 2명 당, 코인 위력 +1 (최대 3)\n[DefeatDuel] 피해량이 80% 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [FreezingDOQ], [WhenUse], [ColdAirDOQ], [DefeatDuel]
   znaczenie tagów: [FreezingDOQ] = 빙결 / Frozen; [WhenUse] = [사용시] / [On Use]; [ColdAirDOQ] = 냉기 / Cold; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: Prioritizes targets with [FreezingDOQ]\nCan Clash with this Skill regardless of Speed\n[WhenUse] Deal +5% damage for every enemy with [ColdAirDOQ] (max 30%)\n[WhenUse] Coin Power +1 for every 2 enemies with [ColdAirDOQ] (max 3)\n[DefeatDuel] Deal -80% damage and damage dealt by this Skill cannot Stagger the target
   PL: priorytet: cele z [FreezingDOQ]\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n[WhenUse] zadaje +5% obrażeń za każdego wroga z [ColdAirDOQ] (maks. 30%)\n[WhenUse] Moc Monety +1 za każdych 2 wrogów z [ColdAirDOQ] (maks. 3)\n[DefeatDuel] zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu
140. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 5 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [Sinking]
142. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +1 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +1 Licznika [Sinking]
144. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttackHead] [AttackUp] 3 얻음 (턴 당 1회)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] (1 + 대상의 [ColdAirDOQ] 수치) x 10 만큼 추가 우울 피해
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [ColdAirDOQ]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [ColdAirDOQ] = 냉기 / Cold
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 10(1 + [ColdAirDOQ] on target) bonus Gloom damage
   PL: [UnBrokenCoinOnSucceedAttack] zadaje dodatkowe obrażenia Posępności równe 10(1 + Licznik [ColdAirDOQ] celu)
147. [Umiejętność wroga [128805] (ulepszenie 1) — moneta 3, efekt 3 — opis] [EnemyKill] 대상이 [FreezingDOQ]을 보유한 상태라면 정신력 20 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128805].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Umiejętność wroga [128806] (ulepszenie 1) — nazwa] 굴복하지 않는 기사
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128806].levelList[level=1].name
   limit: do 40 znaków
   EN: The Indomitable Knight
   PL: The Indomitable Knight
149. [Umiejętność wroga [128806] (ulepszenie 1) — opis] [CanDuelGuard]\n[WhenUse] 다음 턴에 [Agility] 2 얻음 (턴 당 1회)\n[WinDuel] 정신력 15 회복\n[DefeatDuel] 정신력 10 감소
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128806].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [WhenUse], [Agility], [WinDuel], [DefeatDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste; [WinDuel] = [합 승리시] / [Clash Win]; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CanDuelGuard]\n[WhenUse] Gain 2 [Agility] next turn (once per turn)\n[WinDuel] Heal 15 SP\n[DefeatDuel] Lose 10 SP
   PL: [CanDuelGuard]\n[WhenUse] zyskuje 2 [Agility] w następnej turze (1 raz na turę)\n[WinDuel] przywraca 15 SP\n[DefeatDuel] traci 10 SP
150. [Umiejętność wroga [128806] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128806].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Umiejętność wroga [128901] (ulepszenie 1) — nazwa] 세포 주입
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128901].levelList[level=1].name
   limit: do 40 znaków
   EN: Cell Injection
   PL: Cell Injection
152. [Umiejętność wroga [128901] (ulepszenie 1) — opis] [OnDirectAttack] 이 스킬 코인 위력 +2
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128901].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnDirectAttack]
   znaczenie tagów: [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]
   EN: [OnDirectAttack] Coin Power +2 for this Skill
   PL: [OnDirectAttack] Moc Monety +2 dla tej Umiejętności
153. [Umiejętność wroga [128901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Umiejętność wroga [128901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [NervousImpairment] 5 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 5 [NervousImpairment]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 5 [NervousImpairment]
155. [Umiejętność wroga [128901] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [SeaTerrorCell] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128901].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [SeaTerrorCell]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [SeaTerrorCell] = 시테러 동화 / Sea Terror Assimilation
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 1 [SeaTerrorCell]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 1 [SeaTerrorCell]
156. [Umiejętność wroga [128902] (ulepszenie 1) — nazwa] 찢어베기
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128902].levelList[level=1].name
   limit: do 40 znaków
   EN: Ripping Slice
   PL: Ripping Slice
157. [Umiejętność wroga [128902] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128902].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Final Power +1 for every 6 [Sinking] on target (max 2)
   PL: Moc Końcowa +1 za każde 6 [Sinking] celu (maks. 2)
158. [Umiejętność wroga [128902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Umiejętność wroga [128902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 1 [Binding] w następnej turze
160. [Umiejętność wroga [128903] (ulepszenie 1) — nazwa] 휘둘러 베기
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128903].levelList[level=1].name
   limit: do 40 znaków
   EN: Swinging Slice
   PL: Swinging Slice
161. [Umiejętność wroga [128903] (ulepszenie 1) — opis] [WhenUse] 대상의 [Binding] 1 당, 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128903].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Binding]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind
   EN: [WhenUse] Coin Power +1 for every 1 [Binding] on target (max 2)
   PL: [WhenUse] Moc Monety +1 za każdy 1 [Binding] celu (maks. 2)
162. [Umiejętność wroga [128903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Umiejętność wroga [128903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Umiejętność wroga [128903] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [Paralysis] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128903].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 2 [Paralysis]
   PL: [OnSucceedAttack] nakłada 2 [Paralysis]
165. [Umiejętność wroga [128904] (ulepszenie 1) — nazwa] 연속 찌르기
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128904].levelList[level=1].name
   limit: do 40 znaków
   EN: Multiple Jabs
   PL: Multiple Jabs
166. [Umiejętność wroga [128904] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당, 최종 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128904].levelList[level=1].desc
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Umiejętność wroga [128904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Umiejętność wroga [128904] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상의 [NervousImpairment]만큼 우울 피해
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=128904].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict Gloom damage equal to [NervousImpairment] on target
   PL: [OnSucceedAttack] zadaje obrażenia Posępności równe [NervousImpairment] celu
169. [Umiejętność wroga [129101] (ulepszenie 1) — nazwa] 하나된 의지
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129101].levelList[level=1].name
   limit: do 40 znaków
   EN: United Will
   PL: United Will
170. [Umiejętność wroga [129101] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n[StartBattle] 속도가 가장 느린 아군 심해신도에게 다음 턴에 [Agility] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129101].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [Agility]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [Agility] = 신속 / Haste
   EN: Coin Power +1 for every 6 [Sinking] on target (max 2)\n[StartBattle] Apply 2 [Agility] next turn to the allied Cultist of the Deep with the slowest Speed
   PL: Moc Monety +1 za każde 6 [Sinking] celu (maks. 2)\n[StartBattle] nakłada 2 [Agility] w następnej turze na sojuszniczego Cultist of the Deep z najniższą Szybkością
171. [Umiejętność wroga [129101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Umiejętność wroga [129101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict 1 [NervousImpairment]
   PL: [OnSucceedAttack] nakłada 1 [NervousImpairment]
173. [Umiejętność wroga [129101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Umiejętność wroga [129102] (ulepszenie 1) — nazwa] 퍼지는 환희
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129102].levelList[level=1].name
   limit: do 40 znaków
   EN: Propagating Bliss
   PL: Propagating Bliss
175. [Umiejętność wroga [129102] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n[StartBattle] 속도가 가장 빠른 아군 심해신도에게 [Enhancement] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129102].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Coin Power +1 for every 6 [Sinking] on target (max 2)\n[StartBattle] Apply 2 [Enhancement] next turn to the allied Cultist of the Deep with the fastest Speed
   PL: Moc Monety +1 za każde 6 [Sinking] celu (maks. 2)\n[StartBattle] nakłada 2 [Enhancement] w następnej turze na sojuszniczego Cultist of the Deep z najwyższą Szybkością
176. [Umiejętność wroga [129102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Umiejętność wroga [129102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict 2 [NervousImpairment]
   PL: [OnSucceedAttack] nakłada 2 [NervousImpairment]
178. [Umiejętność wroga [129103] (ulepszenie 1) — nazwa] 해방의 의식
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].name
   limit: do 40 znaków
   EN: Rite of Liberation
   PL: Rite of Liberation
179. [Umiejętność wroga [129103] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n[WhenUse] 대상에게 [Binding]이 있으면, 최종 위력 +2\n[WinDuel] [Sinking] 6 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WhenUse], [Binding], [WinDuel]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind; [WinDuel] = [합 승리시] / [Clash Win]
   EN: Coin Power +1 for every 6 [Sinking] on target (max 2)\n[WhenUse] If target has [Binding], Final Power +2\n[WinDuel] Inflict 6 [Sinking]
   PL: Moc Monety +1 za każde 6 [Sinking] celu (maks. 2)\n[WhenUse] jeżeli cel ma [Binding], Moc Końcowa +2\n[WinDuel] nakłada 6 [Sinking]
180. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking]
   PL: [OnSucceedAttack] nakłada 2 [Sinking]
182. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 2 [Binding] next turn
   PL: [OnSucceedAttack] nakłada 2 [Binding] w następnej turze
183. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 3 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict 3 [NervousImpairment]
   PL: [OnSucceedAttack] nakłada 3 [NervousImpairment]
185. [Umiejętność wroga [129103] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129103].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [NervousImpairment]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [NervousImpairment]
186. [Umiejętność wroga [129104] (ulepszenie 1) — nazwa] 환경 적응
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129104].levelList[level=1].name
   limit: do 40 znaków
   EN: Environmental Adaptation
   PL: Environmental Adaptation
187. [Umiejętność wroga [129104] (ulepszenie 1) — opis] 대상의 [Sinking] 6 당 최종 위력 +1 (최대 2)\n[StartBattle] 보호막 50 얻음\n[EndBattle] 자신에게 보호막이 남아있으면, 다음 턴에 [Enhancement] 2 얻음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129104].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [EndBattle], [Enhancement]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [EndBattle] = [턴 종료 시] / [Turn End]; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Final Power +1 for every 6 [Sinking] on target (max 2)\n[StartBattle] Gain 50 Shield\n[EndBattle] If this unit has remaining Shield, gain 2 [Enhancement] next turn
   PL: Moc Końcowa +1 za każde 6 [Sinking] celu (maks. 2)\n[StartBattle] zyskuje 50 Tarczy\n[EndBattle] jeżeli jednostka ma pozostałą Tarczę, zyskuje 2 [Enhancement] w następnej turze
188. [Umiejętność wroga [129105] (ulepszenie 1) — nazwa] 육지의 동포를 위하여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].name
   limit: do 40 znaków
   EN: For the Landbound Kins
   PL: For the Landbound Kins
189. [Umiejętność wroga [129105] (ulepszenie 1) — opis] [WhenUse] 현재 맵에 [NetherseaBrandUnit]이 활성화되어있으면, 최종 위력 +3\n- [NetherseaBrandUnit] 단계 1 당 추가로 최종 위력 +1\n\n[WhenUse] 메인 대상의 [Sinking] 6 당 코인 위력 +1 (최대 2)\n[NetherseaBrandUnit]이 2단계 이상이면. 이 스킬에서 부여하는 [NervousImpairment] +1
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NetherseaBrandUnit], [Sinking], [NervousImpairment]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [Sinking] = 침잠 / Sinking; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [WhenUse] If [NetherseaBrandUnit] is activated here, Final Power +3\n- Gain additional 1 Final Power for every 1 Stage of [NetherseaBrandUnit]\n\n[WhenUse] Coin Power +1 for every 6 [Sinking] on the main target (max 2)\nAt Stage 2 or higher [NetherseaBrandUnit], inflict +1 more [NervousImpairment] with this Skill
   PL: [WhenUse] jeżeli [NetherseaBrandUnit] jest aktywowane tutaj, Moc Końcowa +3\n- zyskuje dodatkowo Moc Końcowa +1 za każdy 1 Etap [NetherseaBrandUnit]\n\n[WhenUse] Moc Monety +1 za każde 6 [Sinking] głównego celu (maks. 2)\nprzy 2. Etapie lub wyższym [NetherseaBrandUnit], ta Umiejętność nakłada o 1 więcej [NervousImpairment]
190. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 1, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [SeaTerrorCell] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 2, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [SeaTerrorCell] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Umiejętność wroga [129105] (ulepszenie 1) — moneta 3, efekt 3 — opis] [UnBrokenCoinOnSucceedAttack] [SeaTerrorCell] 1 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129105].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Umiejętność wroga [129701] (ulepszenie 1) — nazwa] 조급한 자아의 샛길
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129701].levelList[level=1].name
   limit: do 40 znaków
   EN: The Impatient Ego's Byway
   PL: The Impatient Ego's Byway
200. [Umiejętność wroga [129701] (ulepszenie 1) — opis] [CantDuel]\n이 스킬로 대상에게 피해를 입히지 않음\n[EndSkill] [AbyssalVitality] 100 얻음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129701].levelList[level=1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [EndSkill], [AbyssalVitality]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [EndSkill] = [공격 종료시] / [Attack End]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality
   EN: [CantDuel]\nThis Skill does not deal damage against targets\n[EndSkill] Gain 100 [AbyssalVitality]
   PL: [CantDuel]\nta Umiejętność nie zadaje celom obrażeń\n[EndSkill] zyskuje 100 [AbyssalVitality]
201. [Umiejętność wroga [129702] (ulepszenie 1) — nazwa] 안식의 메아리
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129702].levelList[level=1].name
   limit: do 40 znaków
   EN: Echoes of Respite
   PL: Echoes of Respite
202. [Umiejętność wroga [129702] (ulepszenie 1) — opis] [CantIdentify]\n아군을 우선으로 지정하며, 그 중 현재 체력이 가장 낮은 아군을 메인 타겟으로 지정\n대상이 아군이면 피해량이 0으로 고정\n대상의 [Sinking] 3당 합 위력 +1 (최대 4)\n[StartBattle] 대상이 아군이면, 대상의 최대 체력 20%만큼 체력 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129702].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Sinking], [StartBattle]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]
   EN: [CantIdentify]\nPrioritizes allies; among them, prioritize allies with the least current HP\nWhen targeting allies, deal 0 damage\nClash Power +1 for every 3 [Sinking] on target (max 4)\n[StartBattle] When targeting allies, heal (20% of target's max HP) HP
   PL: [CantIdentify]\npriorytet: sojusznicy; wśród nich cel: sojusznik z najmniejszym aktualnym HP\njeżeli Umiejętność celuje w sojusznika, zadaje 0 obrażeń\nMoc Starcia +1 za każde 3 [Sinking] celu (maks. 4)\n[StartBattle] jeżeli Umiejętność celuje w sojusznika, przywraca HP równe 20% Maks. HP celu
203. [Umiejętność wroga [129702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면, 대상 소환 시 소모한 [AbyssalVitality] 4당, 이번 턴과 다음 턴에 [DefenseUp] 1 부여 (최대 5)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AbyssalVitality], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] When targeting an ally, apply 1 [DefenseUp] this turn and next turn for every 4 [AbyssalVitality] consumed to summon the target (max 5)
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w sojusznika, nakłada 1 [DefenseUp] w tej i następnej turze za każde 4 [AbyssalVitality] zużyte na przywołanie celu (maks. 5)
204. [Umiejętność wroga [129702] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 3, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129702].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] When targeting an enemy, inflict 3 [Sinking] and 2 [NervousImpairment]
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w wroga, nakłada 3 [Sinking] i 2 [NervousImpairment]
205. [Umiejętność wroga [129703] (ulepszenie 1) — nazwa] 상승의 메아리
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129703].levelList[level=1].name
   limit: do 40 znaków
   EN: Echoes of Ascending
   PL: Echoes of Ascending
206. [Umiejętność wroga [129703] (ulepszenie 1) — opis] [CantIdentify]\n현재 체력이 가장 높은 아군을 우선으로 지정\n대상이 아군이면 피해량이 0으로 고정\n대상의 [Sinking] 3당 합 위력 +1 (최대 4)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129703].levelList[level=1].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [Sinking]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [Sinking] = 침잠 / Sinking
   EN: [CantIdentify]\nPrioritize allies with the most current HP\nWhen targeting an ally, deal 0 damage\nClash Power +1 for every 3 [Sinking] on target (max 4)
   PL: [CantIdentify]\npriorytet: sojusznik z największym aktualnym HP\njeżeli Umiejętność celuje w sojusznika, zadaje 0 obrażeń\nMoc Starcia +1 za każde 3 [Sinking] celu (maks. 4)
207. [Umiejętność wroga [129703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면, 대상 소환 시 소모한 [AbyssalVitality] 4당, 이번 턴과 다음 턴에 [AttackUp] 1 부여 (최대 5)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [AbyssalVitality], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] When targeting an ally, apply 1 [AttackUp] this turn and next turn for every 4 [AbyssalVitality] consumed to summon the target (max 5)
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w sojusznika, nakłada 1 [AttackUp] w tej i następnej turze za każde 4 [AbyssalVitality] zużyte na przywołanie celu (maks. 5)
208. [Umiejętność wroga [129703] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 3, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129703].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Umiejętność wroga [129704] (ulepszenie 1) — nazwa] 순환하는 생태계
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129704].levelList[level=1].name
   limit: do 40 znaków
   EN: Cyclical Ecosystem
   PL: Cyclical Ecosystem
210. [Umiejętność wroga [129704] (ulepszenie 1) — opis] [CanDuelGuard]\n[EndBattle] 생존한 아군 수만큼 [AbyssalVitality]을 소모하는 대신, 모든 아군에게 대상이 생존한 턴 수만큼 다음 턴에 [AttackDmgUp] 부여 (최대 3)\n- [DefeatDuel] 다음 턴에 [AttackDmgUp]를 부여하지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129704].levelList[level=1].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [EndBattle], [AbyssalVitality], [AttackDmgUp], [DefeatDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [EndBattle] = [턴 종료 시] / [Turn End]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [AttackDmgUp] = 피해량 증가 / Damage Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [CanDuelGuard]\n[EndBattle] Consume [AbyssalVitality] for every surviving ally; however, apply (# of turns target survived) [AttackDmgUp] next turn to all allies (max 3)\n- [DefeatDuel] Does not apply [AttackDmgUp] next turn
   PL: [CanDuelGuard]\n[EndBattle] zużywa [AbyssalVitality] za każdego ocalałego sojusznika, lecz nakłada (liczba tur, które przetrwał cel) [AttackDmgUp] w następnej turze wszystkim sojusznikom (maks. 3)\n- [DefeatDuel] nie nakłada [AttackDmgUp] w następnej turze
211. [Umiejętność wroga [129704] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129704].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Umiejętność wroga [129705] (ulepszenie 1) — nazwa] 짙푸른 온정으로.
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].name
   limit: do 40 znaków
   EN: With Deep Blue Charity.
   PL: With Deep Blue Charity.
213. [Umiejętność wroga [129705] (ulepszenie 1) — opis] [CantIdentify]\n메인 타겟 대상의 [NervousImpairment] 3당 기본 위력 +1 (최대 9)\n대상이 아군이면 피해량이 0으로 고정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[DefeatDuel]\n- [ResultReduction] 3, [Paralysis] 3 얻음\n- 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n- 이 스킬로 부여하는 [NervousImpairment] 부여량이 절반으로 감소하고 [Sinking], [Sinking] 횟수를 부여하지 않음\n- 이 스킬로 얻는 [AbyssalVitality]이 절반으로 감소\n[EndSkill] [AbyssalVitality] 100 얻음\n[EndBattle] 다음 턴 시작 시 아군 전장에 [NetherseaBrandUnit] 생성
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n, [CantIdentify], [NervousImpairment], [DefeatDuel], [ResultReduction], [Paralysis], [Sinking], [AbyssalVitality], [EndSkill], [EndBattle], [NetherseaBrandUnit]
   znaczenie tagów: [CantIdentify] = [피아식별불가] / [Indiscriminate]; [NervousImpairment] = 신경 손상 / Nervous Impairment; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [EndSkill] = [공격 종료시] / [Attack End] …
   EN: [CantIdentify]\nBase Power +1 for every 3 [NervousImpairment] on the main target (max 9)\nWhen targeting allies, deal 0 damage\nCan Clash with this Skill regardless of Speed\n\n[DefeatDuel]\n- Gain 3 [ResultReduction] and 3 [Paralysis]\n- Deal -80% damage, and damage dealt by this Skill cannot Stagger the target\n- Halve the amount of [NervousImpairment] inflicted by this Skill, and does not inflict [Sinking] or [Sinking] Count\n- Halve the amount of [AbyssalVitality] gained from this Skill\n[EndSkill] Gain 100 [AbyssalVitality]\n[EndBattle] At the start of the next turn, generate [NetherseaBrandUnit] in the ally territory
   PL: [CantIdentify]\nMoc Bazowa +1 za każde 3 [NervousImpairment] głównego celu (maks. 9)\njeżeli Umiejętność celuje w sojusznika, zadaje 0 obrażeń\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n\n[DefeatDuel]\n- zyskuje 3 [ResultReduction] i 3 [Paralysis]\n- zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n- nakłada o połowę mniejszą wartość [NervousImpairment] tą Umiejętnością i nie nakłada [Sinking] ani Licznika [Sinking]\n- zyskiwane [AbyssalVitality] z tej Umiejętności jest zmniejszone o połowę\n[EndSkill] zyskuje 100 [AbyssalVitality]\n[EndBattle] na początku następnej tury, tworzy [NetherseaBrandUnit] na terenie sojuszników
214. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] When targeting an ally, heal 10% of their max HP
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w sojusznika, przywraca 10% Maks. HP celu
216. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] When targeting an enemy, inflict 2 [NervousImpairment]
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w wroga, nakłada 2 [NervousImpairment]
217. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Umiejętność wroga [129705] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 4, [Sinking] 횟수 4, [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129705].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] When targeting an enemy, inflict 4 [Sinking], +4 [Sinking] Count, and 4 [NervousImpairment]
   PL: [OnSucceedAttack] jeżeli Umiejętność celuje w wroga, nakłada 4 [Sinking], +4 Licznika [Sinking] i 4 [NervousImpairment]
223. [Umiejętność wroga [129706] (ulepszenie 1) — nazwa] 파도의 궤적
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].name
   limit: do 40 znaków
   EN: Tidal Arc
   PL: Tidal Arc
224. [Umiejętność wroga [129706] (ulepszenie 1) — opis] [WhenUse] [AbyssalVitality]이 50 이상이면, 수치를 5 소모하여 이 스킬에서 부여하는 신경 손상 부여값 +2\n[WhenUse] 대상의 [NervousImpairment] 5당, [AbyssalVitality]을 1 소모하여 합 위력 +1 (최대 5)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AbyssalVitality], [NervousImpairment]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [WhenUse] At 50+ [AbyssalVitality], consume 5 [AbyssalVitality] to inflict +2 more [NervousImpairment] with this Skill's effects\n[WhenUse] For every 5 [NervousImpairment] on target, consume 1 [AbyssalVitality] to gain Clash Power +1 (max 5)
   PL: [WhenUse] przy 50+ [AbyssalVitality], zużywa 5 [AbyssalVitality], by nakładać o 2 więcej [NervousImpairment] efektami tej Umiejętności\n[WhenUse] za każde 5 [NervousImpairment] celu, zużywa 1 [AbyssalVitality], by zyskać Moc Starcia +1 (maks. 5)
225. [Umiejętność wroga [129706] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [Umiejętność wroga [129706] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Umiejętność wroga [129706] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Umiejętność wroga [129706] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Sinking]
229. [Umiejętność wroga [129706] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129706].levelList[level=1].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict 4 [NervousImpairment]
   PL: [OnSucceedAttack] nakłada 4 [NervousImpairment]
230. [Umiejętność wroga [129707] (ulepszenie 1) — nazwa] 거센 난류
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].name
   limit: do 40 znaków
   EN: Fierce Currents
   PL: Fierce Currents
231. [Umiejętność wroga [129707] (ulepszenie 1) — opis] [WhenUse] [AbyssalVitality]이 50 이상이면, 수치를 4 소모하여 코인 위력 +1\n[WhenUse] 대상의 [NervousImpairment] 10당, [AbyssalVitality]을 3 소모하여 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AbyssalVitality], [NervousImpairment]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [WhenUse] At 50+ [AbyssalVitality], consume 4 [AbyssalVitality] to gain Coin Power +1\n[WhenUse] For every 10 [NervousImpairment] on target, consume 3 [AbyssalVitality] to gain Coin Power +1 (max 2)
   PL: [WhenUse] przy 50+ [AbyssalVitality], zużywa 4 [AbyssalVitality], by zyskać Moc Monety +1\n[WhenUse] za każde 10 [NervousImpairment] celu, zużywa 3 [AbyssalVitality], by zyskać Moc Monety +1 (maks. 2)
232. [Umiejętność wroga [129707] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Umiejętność wroga [129707] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Umiejętność wroga [129707] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Umiejętność wroga [129707] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +3 Licznika [Sinking]
236. [Umiejętność wroga [129707] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129707].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Umiejętność wroga [129708] (ulepszenie 1) — nazwa] 일렁이는 파도
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129708].levelList[level=1].name
   limit: do 40 znaków
   EN: Undulating Waves
   PL: Undulating Waves
238. [Umiejętność wroga [129708] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [NervousImpairment] 3당 코인 위력 +1 (최대 9)\n[EndBattle] [AbyssalVitality]을 최대 10만큼 소모하는 대신, 소모한 수치의 절반 만큼 다음 턴에 [AttackUp] 얻음 (최대 5, 소수점 올림)\n- [DefeatDuel] 다음 턴에 [AttackUp]를 얻지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129708].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NervousImpairment], [EndBattle], [AbyssalVitality], [AttackUp], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NervousImpairment] = 신경 손상 / Nervous Impairment; [EndBattle] = [턴 종료 시] / [Turn End]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 3 [NervousImpairment] on the main target (max 9)\n[EndBattle] Consume up to 10 [AbyssalVitality] and gain half of consumed Stack as [AttackUp] next turn (max 5, rounded up)\n- [DefeatDuel] Does not gain [AttackUp] next turn
   PL: [WhenUse] Moc Monety +1 za każde 3 [NervousImpairment] głównego celu (maks. 9)\n[EndBattle] zużywa do 10 [AbyssalVitality] i zyskuje połowę zużytych Liczników jako [AttackUp] w następnej turze (maks. 5, zaokrąglone w górę)\n- [DefeatDuel] nie zyskuje [AttackUp] w następnej turze
239. [Umiejętność wroga [129708] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129708].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Umiejętność wroga [129708] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3, [Sinking] 횟수 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129708].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking] and +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking] i +2 Licznika [Sinking]
241. [Umiejętność wroga [129708] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 6 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129708].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [NervousImpairment]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [OnSucceedAttack] Inflict 6 [NervousImpairment]
   PL: [OnSucceedAttack] nakłada 6 [NervousImpairment]
242. [Umiejętność wroga [129709] (ulepszenie 1) — nazwa] 저들이 믿는 선의가 가치를 잃기 전에.
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].name
   limit: do 80 znaków
   EN: Before the compassion they believe in loses its worth.
   PL: Before the compassion they believe in loses its worth.
243. [Umiejętność wroga [129709] (ulepszenie 1) — opis] [NervousImpairment]이 제일 높은 대상을 우선으로 지정\n메인 타겟 대상의 [NervousImpairment] 3당 기본 위력 +1 (최대 9)\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[DefeatDuel] \n- [ResultReduction] 3, [Paralysis] 3 얻음\n- 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n- 이 스킬로 부여하는 [NervousImpairment] 부여량이 절반으로 감소하고 [Sinking], [Sinking] 횟수를 부여하지 않음\n- 이 스킬로 얻는 [AbyssalVitality], 보호막이 절반으로 감소\n[EndSkill]\n- [AbyssalVitality] 100 얻음\n- 최대 체력의 20%만큼 보호막 얻음\n- 이번 턴 종료\n[EndBattle] 다음 턴 시작 시 전장 전체에 [NetherseaBrandUnit] 생성
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: \n, [NervousImpairment], [DefeatDuel], [ResultReduction], [Paralysis], [Sinking], [AbyssalVitality], [EndSkill], [EndBattle], [NetherseaBrandUnit]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment; [DefeatDuel] = [합 패배] / [Clash Lose]; [ResultReduction] = 위력 감소 / Power Down; [Paralysis] = 마비 / Paralyze; [Sinking] = 침잠 / Sinking; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [EndSkill] = [공격 종료시] / [Attack End]; [EndBattle] = [턴 종료 시] / [Turn End] …
   EN: Prioritizes targets with the most [NervousImpairment]\nBase Power +1 for every 3 [NervousImpairment] on the main target (max 9)\nCan Clash with this Skill regardless of Speed\n\n[DefeatDuel]\n- Gain 3 [ResultReduction] and 3 [Paralysis]\n- Deal -80% damage, and damage dealt by this Skill cannot Stagger the target\n- Halve the amount of [NervousImpairment] inflicted by this Skill, and does not inflict [Sinking] or [Sinking] Count\n- Halve the amount of [AbyssalVitality] and Shield gained from this Skill\n[EndSkill]\n- Gain 100 [AbyssalVitality]\n- Gain Shield equal to 20% of this unit's max HP\n- Ends this turn\n[EndBattle] At the start of the next turn, generate [NetherseaBrandUnit] in the ally territory
   PL: priorytet: cele z największą liczbą [NervousImpairment]\nMoc Bazowa +1 za każde 3 [NervousImpairment] głównego celu (maks. 9)\nmoże stoczyć Starcie z tą Umiejętnością niezależnie od Szybkości\n\n[DefeatDuel]\n- zyskuje 3 [ResultReduction] i 3 [Paralysis]\n- zadaje o 80% mniej obrażeń, a obrażenia zadawane tą Umiejętnością nie mogą Oszołomić celu\n- nakłada o połowę mniejszą wartość [NervousImpairment] tą Umiejętnością i nie nakłada [Sinking] ani Licznika [Sinking]\n- zyskiwane [AbyssalVitality] i Tarcza z tej Umiejętności są zmniejszone o połowę\n[EndSkill]\n- zyskuje 100 [AbyssalVitality]\n- zyskuje Tarczę równą 20% Maks. HP jednostki\n- kończy tę turę\n[EndBattle] na początku następnej tury, tworzy [NetherseaBrandUnit] na terenie sojuszników
244. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 4 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +4 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +4 Licznika [Sinking]
249. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
250. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 4, [Sinking] 횟수 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 4 [Sinking] and +4 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 4 [Sinking] i +4 Licznika [Sinking]
252. [Umiejętność wroga [129709] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 6 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=129709].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Umiejętność wroga [130301] (ulepszenie 1) — nazwa] 조급한 자아의 샛길
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130301].levelList[level=1].name
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Umiejętność wroga [130301] (ulepszenie 1) — opis] [CantDuel]\n이 스킬로 대상에게 피해를 입히지 않음\n[EndSkill] [AbyssalVitality] 100 얻음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130301].levelList[level=1].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
255. [Umiejętność wroga [130302] (ulepszenie 1) — nazwa] 안식의 메아리
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130302].levelList[level=1].name
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Umiejętność wroga [130302] (ulepszenie 1) — opis] [CantIdentify]\n아군을 우선으로 지정하며, 그 중 현재 체력이 가장 낮은 아군을 메인 타겟으로 지정\n대상이 아군이면 피해량이 0으로 고정\n대상의 [Sinking] 3당 합 위력 +1 (최대 4)\n[StartBattle] 대상이 아군이면, 대상의 최대 체력 20%만큼 체력 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130302].levelList[level=1].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Umiejętność wroga [130302] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면, 대상 소환 시 소모한 [AbyssalVitality] 4당, 이번 턴과 다음 턴에 [DefenseUp] 1 부여 (최대 5)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130302].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Umiejętność wroga [130302] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 3, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130302].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Umiejętność wroga [130303] (ulepszenie 1) — nazwa] 상승의 메아리
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130303].levelList[level=1].name
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Umiejętność wroga [130303] (ulepszenie 1) — opis] [CantIdentify]\n현재 체력이 가장 높은 아군을 우선으로 지정\n대상이 아군이면 피해량이 0으로 고정\n대상의 [Sinking] 3당 합 위력 +1 (최대 4)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130303].levelList[level=1].desc
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Umiejętność wroga [130303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상이 아군이면, 대상 소환 시 소모한 [AbyssalVitality] 4당, 이번 턴과 다음 턴에 [AttackUp] 1 부여 (최대 5)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Umiejętność wroga [130303] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 3, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130303].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Umiejętność wroga [130304] (ulepszenie 1) — nazwa] 순환하는 생태계
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130304].levelList[level=1].name
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Umiejętność wroga [130304] (ulepszenie 1) — opis] [CanDuelGuard]\n[EndBattle] 생존한 아군 수만큼 [AbyssalVitality]을 소모하는 대신, 모든 아군에게 대상이 생존한 턴 수만큼 다음 턴에 [AttackDmgUp] 부여 (최대 3)\n- [DefeatDuel] 다음 턴에 [AttackDmgUp]를 부여하지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130304].levelList[level=1].desc
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Umiejętność wroga [130304] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130304].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Umiejętność wroga [130305] (ulepszenie 1) — nazwa] 짙푸른 온정으로.
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].name
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Umiejętność wroga [130305] (ulepszenie 1) — opis] [CantIdentify]\n메인 타겟 대상의 [NervousImpairment] 3당 기본 위력 +1 (최대 9)\n대상이 아군이면 피해량이 0으로 고정\n속도에 상관없이 이 스킬과 합을 할 수 있음\n[DefeatDuel]\n- [ResultReduction] 3, [Paralysis] 3 얻음\n- 피해량이 80%만큼 감소하고 이 스킬의 피해로 대상이 흐트러지지 않음\n- 이 스킬로 부여하는 [NervousImpairment] 부여량이 절반으로 감소하고 [Sinking], [Sinking] 횟수를 부여하지 않음\n- 이 스킬로 얻는 [AbyssalVitality]이 절반으로 감소\n[EndSkill] [AbyssalVitality] 100 얻음\n[EndBattle] 다음 턴 시작 시 아군 전장에 [NetherseaBrandUnit] 생성
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].desc
   (powtórzenie elementu 213 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 216 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상이 아군이면, 대상의 최대 체력 10% 회복
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Umiejętność wroga [130305] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] 대상이 적이면, [Sinking] 4, [Sinking] 횟수 4, [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130305].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 222 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Umiejętność wroga [130306] (ulepszenie 1) — nazwa] 파도의 궤적
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].name
   (powtórzenie elementu 223 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Umiejętność wroga [130306] (ulepszenie 1) — opis] [WhenUse] [AbyssalVitality]이 50 이상이면, 수치를 5 소모하여 이 스킬에서 부여하는 신경 손상 부여값 +2\n[WhenUse] 대상의 [NervousImpairment] 10당, [AbyssalVitality]을 1 소모하여 합 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [AbyssalVitality], [NervousImpairment]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: [WhenUse] At 50+ [AbyssalVitality], consume 5 [AbyssalVitality] to inflict +2 more [NervousImpairment] with this Skill's effects\n[WhenUse] For every 10 [NervousImpairment] on target, consume 1 [AbyssalVitality] to gain Clash Power +1 (max 2)
   PL: [WhenUse] przy 50+ [AbyssalVitality], zużywa 5 [AbyssalVitality], by nakładać o 2 więcej [NervousImpairment] efektami tej Umiejętności\n[WhenUse] za każde 10 [NervousImpairment] celu, zużywa 1 [AbyssalVitality], by zyskać Moc Starcia +1 (maks. 2)
279. [Umiejętność wroga [130306] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Umiejętność wroga [130306] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Umiejętność wroga [130306] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 4 [Sinking]
   PL: [OnSucceedAttack] nakłada 4 [Sinking]
282. [Umiejętność wroga [130306] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130306].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Umiejętność wroga [130307] (ulepszenie 1) — nazwa] 거센 난류
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Umiejętność wroga [130307] (ulepszenie 1) — opis] [WhenUse] [AbyssalVitality]이 50 이상이면, 수치를 4 소모하여 코인 위력 +1\n[WhenUse] 대상의 [NervousImpairment] 10당, [AbyssalVitality]을 3 소모하여 코인 위력 +1 (최대 2)
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].desc
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Umiejętność wroga [130307] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Umiejętność wroga [130307] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Umiejętność wroga [130307] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Umiejętność wroga [130307] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Umiejętność wroga [130307] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130307].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Umiejętność wroga [130308] (ulepszenie 1) — nazwa] 일렁이는 파도
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130308].levelList[level=1].name
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [Umiejętność wroga [130308] (ulepszenie 1) — opis] [WhenUse] 메인 타겟의 [NervousImpairment] 5당 코인 위력 +1 (최대 5)\n[EndBattle] [AbyssalVitality]을 최대 10만큼 소모하는 대신, 소모한 수치의 절반 만큼 다음 턴에 [AttackUp] 얻음 (최대 5, 소수점 올림)\n- [DefeatDuel] 다음 턴에 [AttackUp]를 얻지 않음
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130308].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [NervousImpairment], [EndBattle], [AbyssalVitality], [AttackUp], [DefeatDuel]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [NervousImpairment] = 신경 손상 / Nervous Impairment; [EndBattle] = [턴 종료 시] / [Turn End]; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [WhenUse] Coin Power +1 for every 5 [NervousImpairment] on the main target (max 5)\n[EndBattle] Consume up to 10 [AbyssalVitality] and gain half of consumed Stack as [AttackUp] next turn (max 5, rounded up)\n- [DefeatDuel] Does not gain [AttackUp] next turn
   PL: [WhenUse] Moc Monety +1 za każde 5 [NervousImpairment] głównego celu (maks. 5)\n[EndBattle] zużywa do 10 [AbyssalVitality] i zyskuje połowę zużytych Liczników jako [AttackUp] w następnej turze (maks. 5, zaokrąglone w górę)\n- [DefeatDuel] nie zyskuje [AttackUp] w następnej turze
292. [Umiejętność wroga [130308] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130308].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Umiejętność wroga [130308] (ulepszenie 1) — moneta 1, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3, [Sinking] 횟수 2 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130308].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Umiejętność wroga [130308] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Abnormality-pilgrimage.json :: dataList[id=130308].levelList[level=1].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [pilgrimage] Umiejętności wrogów / Anomalii — Skills_Enemy-pilgrimage
- grupa rozdziału/trybu: `pilgrimage` · plik: `Skills_Enemy-pilgrimage.json`

295. [Umiejętność wroga [9102701] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102701].levelList[level=1].name
   limit: do 40 znaków
   EN: Bite
   PL: Bite
296. [Umiejętność wroga [9102701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 1 [Sinking]
   PL: [OnSucceedAttack] nakłada 1 [Sinking]
297. [Umiejętność wroga [9102701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Umiejętność wroga [9102702] (ulepszenie 1) — nazwa] 강습
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102702].levelList[level=1].name
   limit: do 40 znaków
   EN: Assault
   PL: Assault
299. [Umiejętność wroga [9102702] (ulepszenie 1) — opis] 대상의 [Sinking]이 6 이상이면, 합 위력 +1
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102702].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: If target has 6+ [Sinking], Clash Power +1
   PL: jeżeli cel ma 6+ [Sinking], Moc Starcia +1
300. [Umiejętność wroga [9102702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Sinking]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Sinking] = 침잠 / Sinking
   EN: [OnSucceedAttack] Inflict 2 [Sinking] and +2 [Sinking] Count
   PL: [OnSucceedAttack] nakłada 2 [Sinking] i zwiększa Licznik [Sinking] o 2
301. [Umiejętność wroga [9102801] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102801].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam Down
   PL: Slam Down
302. [Umiejętność wroga [9102801] (ulepszenie 1) — opis] 대상의 [Sinking]이 6 이상이면, 합 위력 +1\n[StartBattle] 체력이 33% 이하면, 이 스킬의 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102801].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [SuperCoin]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: If target has 6+ [Sinking], Clash Power +1\n[StartBattle] At 33%- HP, convert all Coins on this Skill to [SuperCoin]s
   PL: jeżeli cel ma 6+ [Sinking], Moc Starcia +1\n[StartBattle] przy HP 33% lub mniej, wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y
303. [Umiejętność wroga [9102801] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102801].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Umiejętność wroga [9102801] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102801].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Umiejętność wroga [9102802] (ulepszenie 1) — nazwa] 찢어 발기기
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].name
   limit: do 40 znaków
   EN: Ripping Mutilation
   PL: Ripping Mutilation
306. [Umiejętność wroga [9102802] (ulepszenie 1) — opis] 대상의 [Sinking]이 6 이상이면, 합 위력 +1\n[StartBattle] 체력이 33% 이하면, 이 스킬의 마지막 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [SuperCoin]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: If target has 6+ [Sinking], Clash Power +1\n[StartBattle] At 33%- HP, convert the final Coin on this Skill to [SuperCoin]
   PL: jeżeli cel ma 6+ [Sinking], Moc Starcia +1\n[StartBattle] przy HP 33% lub mniej, ostatnia Moneta tej Umiejętności zmienia się w [SuperCoin]
307. [Umiejętność wroga [9102802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Umiejętność wroga [9102802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Umiejętność wroga [9102802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking]
310. [Umiejętność wroga [9102802] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102802].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Umiejętność wroga [9102901] (ulepszenie 1) — nazwa] 생명 절삭
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].name
   limit: do 40 znaków
   EN: Incision of Life
   PL: Incision of Life
312. [Umiejętność wroga [9102901] (ulepszenie 1) — opis] 대상의 [Sinking] 6당, 최종 위력 +1 (최대 3)\n[StartBattle] 체력이 50% 이하면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [StartBattle], [SuperCoin]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [StartBattle] = [전투 시작시] / [Combat Start]; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Final Power +1 for every 6 [Sinking] on target (max 3)\n[StartBattle] At 50%- HP, convert all Coins on this Skill to [SuperCoin]s
   PL: Moc Końcowa +1 za każde 6 [Sinking] celu (maks. 3)\n[StartBattle] przy HP 50% lub mniej, wszystkie Monety tej Umiejętności zmieniają się w [SuperCoin]y
313. [Umiejętność wroga [9102901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Umiejętność wroga [9102901] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Umiejętność wroga [9102901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Umiejętność wroga [9102901] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 4 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Umiejętność wroga [9102901] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102901].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Umiejętność wroga [9102902] (ulepszenie 1) — nazwa] 광란
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].name
   limit: do 40 znaków
   EN: Frenzy
   PL: Frenzy
319. [Umiejętność wroga [9102902] (ulepszenie 1) — opis] 대상의 [Sinking] 6당, 최종 위력 +1 (최대 3)\n[StartBattle] 체력이 50% 이하면, 이 스킬의 모든 코인이 [SuperCoin]으로 변경됨
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 6 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 6 [Sinking]
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 6 [Sinking]
326. [Umiejętność wroga [9102902] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102902].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Umiejętność wroga [9102903] (ulepszenie 1) — nazwa] 영양분 수확
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102903].levelList[level=1].name
   limit: do 40 znaków
   EN: Reap Nutrients
   PL: Reap Nutrients
328. [Umiejętność wroga [9102903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Umiejętność wroga [9102903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9102903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Umiejętność wroga [9103001] (ulepszenie 1) — nazwa] 베어물기
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].name
   limit: do 40 znaków
   EN: Lacerating Bite
   PL: Lacerating Bite
331. [Umiejętność wroga [9103001] (ulepszenie 1) — opis] 대상의 [Sinking] 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Final Power +1 for every 6 [Sinking] on target (max 2)
   PL: Moc Końcowa +1 za każde 6 [Sinking] celu (maks. 2)
332. [Umiejętność wroga [9103001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Umiejętność wroga [9103001] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Umiejętność wroga [9103001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Umiejętność wroga [9103001] (ulepszenie 1) — moneta 2, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada +2 Licznika [Sinking]
336. [Umiejętność wroga [9103001] (ulepszenie 1) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103001].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Umiejętność wroga [9103002] (ulepszenie 1) — nazwa] 연속 포식
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].name
   limit: do 40 znaków
   EN: Persistent Devouring
   PL: Persistent Devouring
338. [Umiejętność wroga [9103002] (ulepszenie 1) — opis] 대상의 [Sinking] 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].desc
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 3, efekt 2 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Umiejętność wroga [9103002] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [NervousImpairment] 3 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103002].levelList[level=1].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Umiejętność wroga [9103101] (ulepszenie 1) — nazwa] 생명 관통
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].name
   limit: do 40 znaków
   EN: Puncturing of Life
   PL: Puncturing of Life
347. [Umiejętność wroga [9103101] (ulepszenie 1) — opis] 메인 타겟 대상의 [Sinking] 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Final Power +1 for every 6 [Sinking] on the main target (max 2)
   PL: Moc Końcowa +1 za każde 6 [Sinking] głównego celu (maks. 2)
348. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 1 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 3 부여, [Sinking] 횟수 2 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 3 [Sinking] and +2 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 3 [Sinking] i zwiększa Licznik [Sinking] o 2
353. [Umiejętność wroga [9103101] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103101].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Umiejętność wroga [9103102] (ulepszenie 1) — nazwa] 분출
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].name
   limit: do 40 znaków
   EN: Discharge
   PL: Discharge
355. [Umiejętność wroga [9103102] (ulepszenie 1) — opis] 메인 타겟 대상의 [Sinking] 6당, 최종 위력 +1 (최대 2)
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].desc
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 2 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 횟수 1 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 3 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 184 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [UnBrokenCoinOnSucceedAttack] [Sinking] 2 부여, [Sinking] 횟수 3 증가
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [UnBrokenCoinOnSucceedAttack], [Sinking]
   znaczenie tagów: [UnBrokenCoinOnSucceedAttack] = [파괴되지 않고 적중시] / [On Hit without Cracking]; [Sinking] = 침잠 / Sinking
   EN: [UnBrokenCoinOnSucceedAttack] Inflict 2 [Sinking] and +3 [Sinking] Count
   PL: [UnBrokenCoinOnSucceedAttack] nakłada 2 [Sinking] i zwiększa Licznik [Sinking] o 3
361. [Umiejętność wroga [9103102] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [NervousImpairment] 4 부여
   źródło: Skills_Enemy-pilgrimage.json :: dataList[id=9103102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [pilgrimage] Pasywka wroga: Passives_Abnormality-pilgrimage
- plik gry: `Passives_Abnormality-pilgrimage.json`

362. [[pilgrimage] Pasywka wroga [128801] — nazwa] 고투
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128801].name
   limit: do 40 znaków
   EN: Struggle
   PL: Struggle
363. [[pilgrimage] Pasywka wroga [128801] — opis] 전투 시작 시 [Protection] 8 얻음\n- 전투 시작 시 사기 저하 상태인 경우, 얻는 [Protection] 수치가 절반으로 감소\n- 전투 시작 시 흐트러짐 혹은 패닉 상태인 경우, [Protection]를 얻지 않음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128801].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Combat Start: gain 8 [Protection]\n- Combat Start: if this unit has Low Morale, halve the amount of [Protection] gained\n- Combat Start: if this unit is Staggered or Panicked, it does not gain [Protection]
   PL: początek walki: zyskuje 8 [Protection]\n- początek walki: jeżeli jednostka ma Niskie Morale, zyskiwane [Protection] jest zmniejszone o połowę\n- początek walki: jeżeli jednostka jest Oszołomiona albo w Panice, nie zyskuje [Protection]
364. [[pilgrimage] Pasywka wroga [128802] — nazwa] 격랑의 포효
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128802].name
   limit: do 40 znaków
   EN: Roar of the Rogue Waves
   PL: Roar of the Rogue Waves
365. [[pilgrimage] Pasywka wroga [128802] — opis] 피격 시 대상에게 [ColdAirDOQ] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ColdAirDOQ]
   znaczenie tagów: [ColdAirDOQ] = 냉기 / Cold
   EN: When hit, inflict 1 [ColdAirDOQ] against the attacker (once per Skill)
   PL: przy otrzymaniu trafienia, nakłada 1 [ColdAirDOQ] na atakującego (1 raz na Umiejętność)
366. [[pilgrimage] Pasywka wroga [128803] — nazwa] 내려다보는 창생
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128803].name
   limit: do 40 znaków
   EN: Overlook of All-life
   PL: Overlook of All-life
367. [[pilgrimage] Pasywka wroga [128803] — opis] 패시브 '운명의 총아'가 발동되면 다음 효과 발동\n- 턴 종료 시 다음 턴에 [Binding] 1 얻음\n- 피격 시 대상에게 [ColdAirDOQ] 1 부여 (스킬당 1회)
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128803].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [ColdAirDOQ]
   znaczenie tagów: [Binding] = 속박 / Bind; [ColdAirDOQ] = 냉기 / Cold
   EN: When the Passive "Fate's Favored Child" triggers, activate the following:\n- Turn End: gain 1 [Binding] next turn\n- When hit, inflict 1 [ColdAirDOQ] against the target (once per Skill)
   PL: gdy uruchamia się passivka „Fate's Favored Child”, uruchamia następujące efekty:\n- na koniec tury, zyskuje 1 [Binding] w następnej turze\n- przy otrzymaniu trafienia, nakłada 1 [ColdAirDOQ] na cel (1 raz na Umiejętność)
368. [[pilgrimage] Pasywka wroga [128804] — nazwa] 파도의 대적자
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128804].name
   limit: do 40 znaków
   EN: Adversary of the Tides
   PL: Adversary of the Tides
369. [[pilgrimage] Pasywka wroga [128804] — opis] [FreezingDOQ]을 보유한 적 공격 시 피해량 +175%
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128804].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [FreezingDOQ]
   znaczenie tagów: [FreezingDOQ] = 빙결 / Frozen
   EN: When attacking targets with [FreezingDOQ], deal +175% damage
   PL: atakując cele z [FreezingDOQ], zadaje +175% obrażeń
370. [[pilgrimage] Pasywka wroga [128805] — nazwa] 운명의 총아
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128805].name
   limit: do 40 znaków
   EN: Fate's Favored Child
   PL: Fate's Favored Child
371. [[pilgrimage] Pasywka wroga [128805] — opis] 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고 체력과 정신력이 최대치로 회복되며 패턴이 변경됨 (전투 당 1회)
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128805].desc
   limit: do 230 znaków
   EN: When this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit is healed back to 100% HP and SP, and gains a new pattern (once per Encounter)
   PL: gdy jednostka otrzyma obrażenia sprowadzające HP do 0, niweluje je; następnie jednostka zostaje wyleczona do 100% HP i SP, a wzorzec zostaje zmieniony (1 raz na walkę)
372. [[pilgrimage] Pasywka wroga [128806] — nazwa] 파도를 향한 분노
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128806].name
   limit: do 40 znaków
   EN: Rage Against the Waves
   PL: Rage Against the Waves
373. [[pilgrimage] Pasywka wroga [128806] — opis] 턴 시작 시 [ColdAirDOQ]를 보유한 적이 1명 당 [AttackUp] 1 얻음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128806].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ColdAirDOQ], [AttackUp]
   znaczenie tagów: [ColdAirDOQ] = 냉기 / Cold; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: gain 1 [AttackUp] for every enemy with [ColdAirDOQ]
   PL: na początku tury, zyskuje 1 [AttackUp] za każdego wroga z [ColdAirDOQ]
374. [[pilgrimage] Pasywka wroga [128807] — nazwa] 질주하는 로시난테
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128807].name
   limit: do 40 znaków
   EN: Galloping Rocinante
   PL: Galloping Rocinante
375. [[pilgrimage] Pasywka wroga [128807] — opis] 턴 시작 시 [ColdAirDOQ]를 보유한 적이 6명 이상이라면 [ParryingResultUp] 2 얻음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128807].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ColdAirDOQ], [ParryingResultUp]
   znaczenie tagów: [ColdAirDOQ] = 냉기 / Cold; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: if there are 6+ enemies with [ColdAirDOQ], gain 2 [ParryingResultUp]
   PL: na początku tury, jeżeli jest 6+ wrogów z [ColdAirDOQ], zyskuje 2 [ParryingResultUp]
376. [[pilgrimage] Pasywka wroga [128808] — nazwa] 기사의 망념
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128808].name
   limit: do 40 znaków
   EN: The Knight's Delusion
   PL: The Knight's Delusion
377. [[pilgrimage] Pasywka wroga [128808] — opis] 스테이지 시작 시 [WeakenDOQ] 얻음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=128808].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WeakenDOQ]
   znaczenie tagów: [WeakenDOQ] = 재난과 시련 / Misery and Calamity
   EN: Encounter Start: gain [WeakenDOQ]
   PL: przy wejściu na etap, zyskuje [WeakenDOQ]
378. [[pilgrimage] Pasywka wroga [129101] — nazwa] 신경 손상
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129101].name
   limit: do 40 znaków
   EN: Nervous Impairment
   PL: Nervous Impairment
379. [[pilgrimage] Pasywka wroga [129101] — opis] 대상의 [NervousImpairment] 1 당, 자신의 스킬 피해량 +1%
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NervousImpairment]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: This unit's Skills deal +1% damage for every 1 [NervousImpairment] on target
   PL: Umiejętności jednostki zadają +1% obrażeń za każdy 1 [NervousImpairment] celu
380. [[pilgrimage] Pasywka wroga [129102] — nazwa] 시본
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129102].name
   limit: do 40 znaków
   EN: Seaborn
   PL: Seaborn
381. [[pilgrimage] Pasywka wroga [129102] — opis] 스테이지 시작 시, [SeaTerrorCell] 5 얻음\n[SeaTerrorCell] 버프의 [AttackDown], [DefenseDown]를 얻지 않고 대신 [AttackUp], [DefenseUp]를 얻음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129102].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [SeaTerrorCell], [AttackDown], [DefenseDown], [AttackUp], [DefenseUp]
   znaczenie tagów: [SeaTerrorCell] = 시테러 동화 / Sea Terror Assimilation; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Encounter Start: gain 5 [SeaTerrorCell]\nInstead of [AttackDown] and [DefenseDown] effects of [SeaTerrorCell], gain [AttackUp] and [DefenseUp]
   PL: przy wejściu na etap, zyskuje 5 [SeaTerrorCell]\nzamiast efektów [AttackDown] i [DefenseDown] z [SeaTerrorCell], zyskuje [AttackUp] i [DefenseUp]
382. [[pilgrimage] Pasywka wroga [129104] — nazwa] 동포의 부름
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129104].name
   limit: do 40 znaków
   EN: Call of the Bloodkin
   PL: Call of the Bloodkin
383. [[pilgrimage] Pasywka wroga [129104] — opis] 턴 종료 시, 생존한 아군이 2명 이하면 자신의 정신력을 10 소모하여 “해안의 폭주자” 2개체를 전장에 부름\n\n턴 종료시 현재 스테이지에 [NetherseaBrandUnit]이 존재하면, 다음 턴에 모든 시테러 개체에게 [Enhancement] 2 부여\n- [NetherseaBrandUnit] 단계 당 추가로 [AttackUp] 1 부여
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129104].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [NetherseaBrandUnit], [Enhancement], [AttackUp]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn End: if there are 2 or fewer surviving allies, consume 10 SP on self to summon 2 "Shell Sea Runner" units to the battlefield\n\nTurn End: if [NetherseaBrandUnit] exists in this Stage, apply 2 [Enhancement] next turn to all Sea Terror units\n- Apply 1 [AttackUp] as well for every Stage of [NetherseaBrandUnit]
   PL: na koniec tury, jeżeli ocalałych sojuszników jest 2 lub mniej, zużywa 10 SP jednostki, by przywołać 2 jednostki „Shell Sea Runner” na pole walki\n\nna koniec tury, jeżeli [NetherseaBrandUnit] istnieje na tym etapie, nakłada 2 [Enhancement] w następnej turze wszystkim jednostkom Sea Terror\n- dodatkowo nakłada 1 [AttackUp] za każdy Etap [NetherseaBrandUnit]
384. [[pilgrimage] Pasywka wroga [129104] — podsumowanie] [NetherseaBrandUnit]이 존재하면, 다음 턴에 모든 시테러 개체에게 공격 버프 부여
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129104].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: If there is [NetherseaBrandUnit] on the field, apply offensive buff next turn to all Sea Terror units
   PL: jeżeli istnieje [NetherseaBrandUnit] na polu walki, nakłada buff ofensywny w następnej turze wszystkim jednostkom Sea Terror
385. [[pilgrimage] Pasywka wroga [129701] — nazwa] 주광성 행렬
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129701].name
   limit: do 40 znaków
   EN: Phototaxic Procession
   PL: Phototaxic Procession
386. [[pilgrimage] Pasywka wroga [129701] — opis] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 -90%\n턴 시작 시, [Protection] 10 얻음\n\n턴 종료 시, [AbyssalVitality]을 소모하여 시테러 무리를 불러옴\n- 해안의 폭주자 또는 저해의 활주자가 전장에 셋 미만이면, 다음 턴에 대상의 합이 셋이 될 때까지 무작위로 불러오고 (소환한 수 x 4)만큼 소모\n- 심해의 정초자가 전장에 없으면, 다음 턴에 불러오고 8 소모\n- 심해의 분출자가 전장에 없으면, 다음 턴에 불러오고 12 소모\n- 발해의 수확자가 전장에 없으면, 다음 턴에 불러오고 20 소모
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129701].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst], [Sinking], [Protection], [AbyssalVitality]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking; [Protection] = 보호 / Protection; [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality
   EN: Take -90% damage from [Combustion], [Laceration], [Vibration], [Burst], [Sinking]\nTurn Start: gain 10 [Protection]\n\nTurn End: consume [AbyssalVitality] to summon Sea Terror horde\n- If there are fewer than 3 Shell Sea Runners or Deep Sea Sliders on the battlefield, randomly summon either of those units until there are a sum of 3 of them next turn and consume (# of summoned units x 4) [AbyssalVitality]\n- If Nethersea Founder isn't on the battlefield, consume 8 [AbyssalVitality] to summon it next turn\n- If Nethersea Spewer isn't on the battlefield, consume 12 [AbyssalVitality] to summon it next turn\n- If Basin Sea Reaper isn't on the battlefield, consume 20 [AbyssalVitality] to summon it next turn
   PL: otrzymuje o 90% mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]\nna początku tury, zyskuje 10 [Protection]\n\nna koniec tury, zużywa [AbyssalVitality], by przywołać hordę Sea Terror\n- jeżeli na polu walki jest mniej niż 3 jednostek Shell Sea Runner albo Deep Sea Slider, losowo przywołuje jedną z tych jednostek, aż ich suma wyniesie 3 w następnej turze, i zużywa (liczba przywołanych jednostek x 4) [AbyssalVitality]\n- jeżeli Nethersea Founder nie ma na polu walki, zużywa 8 [AbyssalVitality], by przywołać go w następnej turze\n- jeżeli Nethersea Spewer nie ma na polu walki, zużywa 12 [AbyssalVitality], by przywołać go w następnej turze\n- jeżeli Basin Sea Reaper nie ma na polu walki, zużywa 20 [AbyssalVitality], by przywołać go w następnej turze
387. [[pilgrimage] Pasywka wroga [129701] — podsumowanie] [Combustion], [Laceration], [Vibration], [Burst], [Sinking]으로 받는 피해량 감소
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129701].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion], [Laceration], [Vibration], [Burst], [Sinking]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture; [Sinking] = 침잠 / Sinking
   EN: Take less damage from [Combustion], [Laceration], [Vibration], [Burst], and [Sinking]
   PL: otrzymuje mniej obrażeń od [Combustion], [Laceration], [Vibration], [Burst] i [Sinking]
388. [[pilgrimage] Pasywka wroga [129702] — nazwa] 책임 자아
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129702].name
   limit: do 40 znaków
   EN: Ego of Responsibility
   PL: Ego of Responsibility
389. [[pilgrimage] Pasywka wroga [129702] — opis] 자신이 불러온 시테러가 사망할 때마다, 대상의 최대 체력 100%만큼 고정 체력 피해를 입음
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129702].desc
   limit: do 140 znaków
   EN: Every time a Sea Terror this unit summoned is killed, take fixed HP damage equal to the unit's max HP
   PL: za każdym razem, gdy przywołany przez jednostkę Sea Terror zginie, jednostka otrzymuje stałe obrażenia HP równe Maks. HP tej jednostki
390. [[pilgrimage] Pasywka wroga [129703] — nazwa] 표류하는 선의
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129703].name
   limit: do 40 znaków
   EN: Adrift Compassion
   PL: Adrift Compassion
391. [[pilgrimage] Pasywka wroga [129703] — opis] 체력이 50% 이하가 되면, 전투가 즉시 종료되고 패턴이 변경됨\n- '주광성 행렬' 패시브 비활성화\n- [AbyssalVitality] 100 얻음\n- 이 패시브를 얻거나 혹은 흐트러짐 상태에서 해제되면, 잃은 체력 만큼의 보호막 얻음 (턴당 최대 1회)\n- 자신이 보호막 획득 시, [IndelibleGoodwill] 효과가 적용됨\n\n턴 시작 시,\n- [NervousImpairment]이 15 미만인 모든 적에게 [NervousImpairment] 5 부여\n- ('저들이 믿는 선의가 가치를 잃기 전에'를 이번 전투 동안 사용한 횟수 x 2)만큼 [Vulnerable] 얻음 (최대 6)\n\n패턴 변경 이후에는 매 턴마다 흐트러진 적 수만큼 자신의 스킬 슬롯 수 감소 (최대 6, 강력한 스킬 사용하는 턴에는 적용되지 않음)
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129703].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n, [AbyssalVitality], [IndelibleGoodwill], [NervousImpairment], [Vulnerable]
   znaczenie tagów: [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality; [IndelibleGoodwill] = 지워지지 않을 선의 / Indelible Compassion; [NervousImpairment] = 신경 손상 / Nervous Impairment; [Vulnerable] = 취약 / Fragile
   EN: At 50%- HP, immediately ends combat phase and gains a new pattern\n- Disable the Phototaxic Procession Passive\n- Gain 100 [AbyssalVitality]\n- When gaining this Passive, or when recovering from Stagger, gain Shield equal to the amount of HP lost (once per turn)\n- When gaining Shield, activate the effects of [IndelibleGoodwill]\n\nTurn Start:\n- Apply 5 [NervousImpairment] to all enemies with less than 15 [NervousImpairment]\n- Gain [Vulnerable] equal to double the number of times ("Before the compassion they believe in loses its worth.") was used during this Encounter. (max 6)\n\nAfter gaining a new pattern: reduce this unit's Skill Slots by the number of Staggered enemies every turn (by 6 max; does not apply to turns when this unit uses a powerful Skill)
   PL: przy HP 50% lub mniej, natychmiast kończy fazę walki i zmienia wzorzec\n- dezaktywuje passivkę Phototaxic Procession\n- zyskuje 100 [AbyssalVitality]\n- przy zyskiwaniu tej passivki albo dochodzeniu do siebie z Oszołamienia, zyskuje Tarczę równą utraconemu HP (maks. 1 raz na turę)\n- przy zyskiwaniu Tarczy, uruchamia efekty [IndelibleGoodwill]\n\nna początku tury:\n- nakłada 5 [NervousImpairment] wszystkim wrogom z mniej niż 15 [NervousImpairment]\n- zyskuje [Vulnerable] równe dwukrotności liczby użyć („Before the compassion they believe in loses its worth.”) w tej walce (maks. 6)\n\npo zmianie wzorca: co turę zmniejsza liczbę slotów Umiejętności jednostki o liczbę Oszołomionych wrogów (maks. 6; nie dotyczy tur, w których jednostka używa potężnej Umiejętności)
392. [[pilgrimage] Pasywka wroga [129703] — podsumowanie] [AbyssalVitality]을 소모할 때, 정신력 회복
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129703].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AbyssalVitality]
   znaczenie tagów: [AbyssalVitality] = 깊은 바다의 생명력 / Abyssal Vitality
   EN: When consuming [AbyssalVitality], heal SP
   PL: przy zużywaniu [AbyssalVitality], przywraca SP
393. [[pilgrimage] Pasywka wroga [129704] — nazwa] 명흔 낙원
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129704].name
   limit: do 40 znaków
   EN: Nethersea Brand Utopia
   PL: Nethersea Brand Utopia
394. [[pilgrimage] Pasywka wroga [129704] — opis] [NetherseaBrandUnit] 위에 있을 경우, 최종 위력과 코인 위력이 각각 3만큼 증가하고 공격 적중 시 부여하는 [NervousImpairment] 부여값이 2배로 증가
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129704].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit], [NervousImpairment]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: When on top of [NetherseaBrandUnit]: gain Final Power +3 and Coin Power +3, and double the amount of [NervousImpairment] inflicted On Hit
   PL: gdy jednostka znajduje się na [NetherseaBrandUnit]: zyskuje Moc Końcowa +3 i Moc Monety +3, a nakładane przy trafieniu [NervousImpairment] są podwojone
395. [[pilgrimage] Pasywka wroga [129705] — nazwa] 동족 회유
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129705].name
   limit: do 40 znaków
   EN: Coaxing Kins
   PL: Coaxing Kins
396. [[pilgrimage] Pasywka wroga [129705] — opis] 발해의 수확자에게 자신의 스킬 적중 시, 발해의 수확자가 [WaitingforCommandMod] 상태에서 [ParticipationMod] 상태로 전환됨
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129705].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [WaitingforCommandMod], [ParticipationMod]
   znaczenie tagów: [WaitingforCommandMod] = 명령 대기 / Standby State; [ParticipationMod] = 참전 / Combat-Ready State
   EN: When hitting a Basin Sea Reaper with this unit's Skill, convert it from [WaitingforCommandMod] to [ParticipationMod]
   PL: gdy Umiejętność jednostki trafi Basin Sea Reaper, zmienia go ze stanu [WaitingforCommandMod] w stan [ParticipationMod]
397. [[pilgrimage] Pasywka wroga [129103] — nazwa] 세포막
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129103].name
   limit: do 40 znaków
   EN: Cell Membrane
   PL: Cell Membrane
398. [[pilgrimage] Pasywka wroga [129103] — opis] 자신이 피격당한 후 자신에게 보호막이 남아있으면, 대상에게 [Sinking] 2 부여
   źródło: Passives_Abnormality-pilgrimage.json :: dataList[id=129103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: If this unit has remaining Shield after getting hit, inflict 2 [Sinking] against the target
   PL: jeżeli po otrzymaniu trafienia jednostka ma pozostałą Tarczę, nakłada 2 [Sinking] na cel

## [pilgrimage] Pasywka wroga: Passives_Enemy-pilgrimage
- plik gry: `Passives_Enemy-pilgrimage.json`

399. [[pilgrimage] Pasywka wroga [128901] — nazwa] 주의 분산
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128901].name
   limit: do 40 znaków
   EN: Diversion
   PL: Diversion
400. [[pilgrimage] Pasywka wroga [128901] — opis] 턴 종료 시, 자신이 이번 턴에 피해를 받지 않았으면 다음 턴에 [Agility] 2 얻음\n자신이 공격 대상보다 속도가 빠르면, 속도 차이 1 당 스킬 피해량 +5% (최대 50%)
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128901].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Turn End: if this unit did not take damage this turn, gain 2 [Agility] next turn\nIf this unit's Speed is faster than the attack target's, deal +5% damage for every 1 Speed difference (max 50%)
   PL: na koniec tury, jeżeli jednostka nie otrzymała obrażeń w tej turze, zyskuje 2 [Agility] w następnej turze\njeżeli Szybkość jednostki jest wyższa niż Szybkość celu ataku, zadaje +5% obrażeń za każdą 1 różnicę Szybkości (maks. 50%)
401. [[pilgrimage] Pasywka wroga [128902] — nazwa] 도포된 검
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128902].name
   limit: do 40 znaków
   EN: Dipped Blade
   PL: Dipped Blade
402. [[pilgrimage] Pasywka wroga [128902] — opis] 일방 공격 적중 시, [NervousImpairment] 1 부여
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128902].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NervousImpairment]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: On Hit with an Unopposed Attack, inflict 1 [NervousImpairment]
   PL: przy trafieniu Atakiem Jednostronnym, nakłada 1 [NervousImpairment]
403. [[pilgrimage] Pasywka wroga [128903] — nazwa] 심해 숭배
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128903].name
   limit: do 40 znaków
   EN: Abyssal Worship
   PL: Abyssal Worship
404. [[pilgrimage] Pasywka wroga [128903] — opis] 턴 시작시 생존한 아군 1명 당 정신력 3 회복
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=128903].desc
   limit: do 120 znaków
   EN: Turn Start: heal 3 SP for every surviving ally
   PL: na początku tury, przywraca 3 SP za każdego ocalałego sojusznika
405. [[pilgrimage] Pasywka wroga [9102701] — nazwa] 심해의 공포
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102701].name
   limit: do 40 znaków
   EN: Abyssal Horror
   PL: Abyssal Horror
406. [[pilgrimage] Pasywka wroga [9102701] — opis] [Sinking]이 없는 대상에게 공격 적중 시 부여하는 [Sinking] 위력 부여값 +1
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict +1 more [Sinking] Potency On Hit against targets without [Sinking]
   PL: nakłada o 1 więcej Siły [Sinking] przy trafieniu celów bez [Sinking]
407. [[pilgrimage] Pasywka wroga [9102801] — nazwa] 심해의 공포
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102801].name
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [[pilgrimage] Pasywka wroga [9102801] — opis] [Sinking]이 없는 대상에게 공격 적중 시 부여하는 [Sinking] 위력 부여값 +2
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict +2 more [Sinking] Potency On Hit against targets without [Sinking]
   PL: nakłada o 2 więcej Siły [Sinking] przy trafieniu celów bez [Sinking]
409. [[pilgrimage] Pasywka wroga [9102802] — nazwa] 명흔 낙원
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102802].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [[pilgrimage] Pasywka wroga [9102802] — opis] [NetherseaBrandUnit] 위에 있을 경우, 합 위력이 2만큼 증가하고 공격 적중 시 부여하는 [NervousImpairment] 부여값이 2배로 증가
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102802].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit], [NervousImpairment]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: When on top of [NetherseaBrandUnit]: gain Clash Power +2 and double the amount of [NervousImpairment] inflicted On Hit
   PL: gdy jednostka znajduje się na [NetherseaBrandUnit]: zyskuje Moc Starcia +2, a nakładane przy trafieniu [NervousImpairment] są podwojone
411. [[pilgrimage] Pasywka wroga [9102901] — nazwa] 명령 대기
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102901].name
   limit: do 40 znaków
   EN: Standby
   PL: Standby
412. [[pilgrimage] Pasywka wroga [9102901] — opis] [WaitingforCommandMod] 상태에서는 피해를 입기 전까지 공격 스킬을 사용하지 않음\n\n[WaitingforCommandMod] 상태에서 피해를 입을 시, [ParticipationMod] 상태에 돌입하여 다음 턴부터 공격 스킬을 사용
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102901].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [WaitingforCommandMod], [ParticipationMod]
   znaczenie tagów: [WaitingforCommandMod] = 명령 대기 / Standby State; [ParticipationMod] = 참전 / Combat-Ready State
   EN: When in [WaitingforCommandMod], does not use Attack Skills until taking damage.\n\nWhen this unit takes damage while in [WaitingforCommandMod], enter [ParticipationMod] and start using Attack Skills starting next turn
   PL: w stanie [WaitingforCommandMod] nie używa Umiejętności ataku, dopóki nie otrzyma obrażeń.\n\ngdy jednostka otrzyma obrażenia w stanie [WaitingforCommandMod], przechodzi w stan [ParticipationMod] i od następnej tury używa Umiejętności ataku
413. [[pilgrimage] Pasywka wroga [9102902] — nazwa] 참전
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102902].name
   limit: do 40 znaków
   EN: Combat-Ready
   PL: Combat-Ready
414. [[pilgrimage] Pasywka wroga [9102902] — opis] [ParticipationMod] 상태에서 턴 시작 시,\n- [NervousImpairment]이 15 미만인 모든 적에게 [NervousImpairment] 3 부여\n- 속도 최솟값, 최댓값 3 증가\n- 잃은 체력 10%당 [AttackUp] 1 얻음 (최대 8)\n\n[ParticipationMod] 상태에서 턴 종료 시, 최대 체력의 10%만큼 고정 체력 피해를 입음
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102902].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [ParticipationMod], [NervousImpairment], [AttackUp]
   znaczenie tagów: [ParticipationMod] = 참전 / Combat-Ready State; [NervousImpairment] = 신경 손상 / Nervous Impairment; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start in [ParticipationMod]:\n- Inflict 3 [NervousImpairment] to all enemies with less than 15 [NervousImpairment]\n- Min & Max Speed +3\nGain 1 [AttackUp] for every 10% missing HP (max 8)\n\nTurn End in [ParticipationMod]: take fixed damage equal to 10% HP
   PL: na początku tury w stanie [ParticipationMod]:\n- nakłada 3 [NervousImpairment] wszystkim wrogom z mniej niż 15 [NervousImpairment]\n- Minimalna i Maksymalna Szybkość +3\nzyskuje 1 [AttackUp] za każde 10% brakującego HP (maks. 8)\n\nna koniec tury w stanie [ParticipationMod], otrzymuje stałe obrażenia równe 10% HP
415. [[pilgrimage] Pasywka wroga [9102903] — nazwa] 생존 반사
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102903].name
   limit: do 40 znaków
   EN: Survival Reflexes
   PL: Survival Reflexes
416. [[pilgrimage] Pasywka wroga [9102903] — opis] 대상과 합을 진행하거나 일방 공격 적중 시, 대상에게 [NervousImpairment] 2 부여\n- 자신이 [NetherseaBrandUnit] 위에 있을 경우, [NervousImpairment] 1 추가로 부여
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102903].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [NervousImpairment], [NetherseaBrandUnit]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment; [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: When Clashing with the target, or On Hit with an Unopposed attack, inflict 2 [NervousImpairment]\n- If this unit is on top of [NetherseaBrandUnit], inflict 1 more [NervousImpairment]
   PL: podczas Starcia z celem albo przy trafieniu Atakiem Jednostronnym, nakłada 2 [NervousImpairment] na cel\n- jeżeli jednostka znajduje się na [NetherseaBrandUnit], nakłada dodatkowo 1 [NervousImpairment]
417. [[pilgrimage] Pasywka wroga [9102904] — nazwa] 명흔 낙원
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102904].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [[pilgrimage] Pasywka wroga [9102904] — opis] [NetherseaBrandUnit] 위에 있을 경우, 최종 위력과 코인 위력이 각각 2만큼 증가하고 공격 적중 시 부여하는 [NervousImpairment] 부여값이 2배로 증가
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9102904].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit], [NervousImpairment]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: When on top of [NetherseaBrandUnit]: gain Final Power +2 and Coin Power +2, and double the amount of [NervousImpairment] inflicted On Hit
   PL: gdy jednostka znajduje się na [NetherseaBrandUnit]: zyskuje Moc Końcowa +2 i Moc Monety +2, a nakładane przy trafieniu [NervousImpairment] są podwojone
419. [[pilgrimage] Pasywka wroga [9103001] — nazwa] 심층 인지
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103001].name
   limit: do 40 znaków
   EN: In-depth Cognition
   PL: In-depth Cognition
420. [[pilgrimage] Pasywka wroga [9103001] — opis] 모든 속성 내성 -0.5
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103001].desc
   limit: do 120 znaków
   EN: -0.5 to all Affinity Resistances
   PL: -0.5 do wszystkich Odporności Afiniczności
421. [[pilgrimage] Pasywka wroga [9103002] — nazwa] 확산 본능
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103002].name
   limit: do 40 znaków
   EN: Propagatory Instinct
   PL: Propagatory Instinct
422. [[pilgrimage] Pasywka wroga [9103002] — opis] 사망 시 다음 턴에 자신의 진영에 [NetherseaBrandUnit]을 생성한다.
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103002].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: On death, generate [NetherseaBrandUnit] in the allied units' territory next turn.
   PL: po śmierci, tworzy [NetherseaBrandUnit] na terenie jednostek sojuszniczych w następnej turze.
423. [[pilgrimage] Pasywka wroga [9103003] — nazwa] 명흔 낙원
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103003].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [[pilgrimage] Pasywka wroga [9103003] — opis] [NetherseaBrandUnit] 위에 있을 경우, 최종 위력과 코인 위력이 각각 1만큼 증가하고 공격 적중 시 부여하는 [NervousImpairment] 부여값이 2배로 증가
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103003].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit], [NervousImpairment]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: When on top of [NetherseaBrandUnit]: gain Final Power +1 and Coin Power +1, and double the amount of [NervousImpairment] inflicted On Hit
   PL: gdy jednostka znajduje się na [NetherseaBrandUnit]: zyskuje Moc Końcowa +1 i Moc Monety +1, a nakładane przy trafieniu [NervousImpairment] są podwojone
425. [[pilgrimage] Pasywka wroga [9103101] — nazwa] 명흔 낙원
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103101].name
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [[pilgrimage] Pasywka wroga [9103101] — opis] 공격 스킬이 가장 가까운 대상을 메인 타겟으로 지정하며, 앞에 있는 순서대로 서브 타겟을 지정\n\n\n[NetherseaBrandUnit] 위에 있을 경우,\n- 제일 멀리 떨어진 대상을 타겟으로 지정하고 모든 스킬 코인이 [SuperCoin]으로 변경됨\n- 최종 위력과 코인 위력이 각각 2만큼 증가하고 공격 적중 시 부여하는 [NervousImpairment] 부여값이 2배로 증가
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103101].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [NetherseaBrandUnit], [SuperCoin], [NervousImpairment]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [NervousImpairment] = 신경 손상 / Nervous Impairment
   EN: Attack Skills designate the closest enemy as the main target, and select sub-targets from the front\n\n\nWhen on top of [NetherseaBrandUnit]...\n- Designates the furthest enemy as the target, and converts all coins to [SuperCoin]s\n- Gain Final Power +2 and Coin Power +2; double the amount of [NervousImpairment] inflicted On Hit
   PL: Umiejętności ataku wyznaczają najbliższego wroga jako główny cel i wybierają cele drugorzędne od przodu\n\n\ngdy jednostka znajduje się na [NetherseaBrandUnit]...\n- wyznacza najdalszego wroga jako cel, a wszystkie Monety Umiejętności zmieniają się w [SuperCoin]y\n- zyskuje Moc Końcowa +2 i Moc Monety +2; nakładane przy trafieniu [NervousImpairment] są podwojone
427. [[pilgrimage] Pasywka wroga [9103101] — podsumowanie] [NetherseaBrandUnit] 위에 있을 경우, 스킬이 강화됨
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103101].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: When on top of [NetherseaBrandUnit], enhance Skills
   PL: gdy jednostka znajduje się na [NetherseaBrandUnit], Umiejętności są wzmocnione
428. [[pilgrimage] Pasywka wroga [9103201] — nazwa] 잔해 제거
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103201].name
   limit: do 40 znaków
   EN: Debris Removal
   PL: Debris Removal
429. [[pilgrimage] Pasywka wroga [9103201] — opis] 속도가 1로 고정되며, [NetherseaBrandUnit]이 등장할 수 있는 전투에서 비활성화 상태로 배치됨\n\n전장에 [NetherseaBrandUnit]이 등장하면 활성화되어 피해를 받을 수 있는 상태로 변경됨\n- 피해를 받아 체력이 1이 되면, 성도의 손이 가동되어 전장의 [NetherseaBrandUnit]을 전부 제거. 이 효과 발동 시, 다음 턴 동안 성도의 손이 비활성화됨\n- 자신을 메인 타겟으로 한 스킬의 피해만 받으며, 그 외의 피해를 받지 않음\n- 비활성화 상태가 되면 보유한 효과를 전부 제거하고 체력이 최대로 변경
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103201].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n, [NetherseaBrandUnit]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: This unit's Speed is fixed to 1. Spawns in an inactive state in battles that [NetherseaBrandUnit] may appear.\n\nWhen [NetherseaBrandUnit] appears on the battlefield, this unit becomes active and damageable.\n- When this unit's HP drops to 1 from damage, trigger Hand of the Saint and remove all [NetherseaBrandUnit] from the battlefield. When this effect triggers, Hand of the Saint becomes inactive for the next turn.\n- This unit takes damage only from Skills mainly targeting this unit, and it takes no other damage.\n- When it becomes inactive, it removes all effects from self and heals back to max HP.
   PL: Szybkość jednostki jest stała: 1. pojawia się w stanie nieaktywnym w walkach, w których może wystąpić [NetherseaBrandUnit].\n\ngdy [NetherseaBrandUnit] pojawi się na polu walki, jednostka staje się aktywna i podatna na obrażenia.\n- gdy HP jednostki spadnie do 1 od obrażeń, uruchamia Hand of the Saint i usuwa całe [NetherseaBrandUnit] z pola walki. po uruchomieniu tego efektu, Hand of the Saint jest nieaktywna przez następną turę.\n- jednostka otrzymuje obrażenia tylko od Umiejętności celujących głównie w tę jednostkę i nie otrzymuje żadnych innych obrażeń.\n- gdy przechodzi w stan nieaktywny, usuwa wszystkie swoje efekty i przywraca HP do maksimum
430. [[pilgrimage] Pasywka wroga [9103201] — podsumowanie] 전장의 [NetherseaBrandUnit]을 전부 제거
   źródło: Passives_Enemy-pilgrimage.json :: dataList[id=9103201].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NetherseaBrandUnit]
   znaczenie tagów: [NetherseaBrandUnit] = 명흔 / Nethersea Brand
   EN: Remove all [NetherseaBrandUnit] on the battlefield
   PL: usuwa całe [NetherseaBrandUnit] z pola walki

## [podstawowe] Wróg / część: Enemies-schema
- plik gry: `Enemies-schema.json`

431. [[podstawowe] Wróg / część [6002] — nazwa] 흑운회 제3조장 미네
   źródło: Enemies-schema.json :: dataList[id=6002].name
   limit: do 70 znaków
   EN: Mine, Patriarch of the Kurokumo Clan's Third Family
   PL: Mine, Patriarcha Trzeciej Rodziny Klanu Kurokumo

## [podstawowe] Wróg / część: Enemies
- plik gry: `Enemies.json`

432. [[podstawowe] Wróg / część [8001] — nazwa] 흑단여왕의 사과
   źródło: Enemies.json :: dataList[id=8001].name
   limit: do 40 znaków
   EN: Ebony Queen's Apple
   PL: Ebony Queen's Apple
433. [[podstawowe] Wróg / część [8001] — opis] 본체
   źródło: Enemies.json :: dataList[id=8001].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [[podstawowe] Wróg / część [800101] — nazwa] 열매
   źródło: Enemies.json :: dataList[id=800101].name
   limit: do 40 znaków
   EN: Fruit
   PL: Fruit
435. [[podstawowe] Wróg / część [800101] — opis] 부위
   źródło: Enemies.json :: dataList[id=800101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [[podstawowe] Wróg / część [800102] — nazwa] 왼쪽 줄기
   źródło: Enemies.json :: dataList[id=800102].name
   limit: do 40 znaków
   EN: Left Stem
   PL: Left Stem
437. [[podstawowe] Wróg / część [800102] — opis] 부위
   źródło: Enemies.json :: dataList[id=800102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [[podstawowe] Wróg / część [800103] — nazwa] 오른쪽 줄기
   źródło: Enemies.json :: dataList[id=800103].name
   limit: do 40 znaków
   EN: Right Stem
   PL: Right Stem
439. [[podstawowe] Wróg / część [800103] — opis] 부위
   źródło: Enemies.json :: dataList[id=800103].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [[podstawowe] Wróg / część [800104] — nazwa] 뿌리
   źródło: Enemies.json :: dataList[id=800104].name
   limit: do 40 znaków
   EN: Roots
   PL: Roots
441. [[podstawowe] Wróg / część [800104] — opis] 부위
   źródło: Enemies.json :: dataList[id=800104].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [[podstawowe] Wróg / część [90004] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=90004].name
   limit: do 40 znaków
   EN: Number-nuts Hooligan
   PL: Number-nuts Hooligan
443. [[podstawowe] Wróg / część [90004] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90004].desc
   limit: do 120 znaków
   EN: Enemy Unit
   PL: Enemy Unit
444. [[podstawowe] Wróg / część [90005] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=90005].name
   limit: do 40 znaków
   EN: Sharp Hooligan
   PL: Sharp Hooligan
445. [[podstawowe] Wróg / część [90005] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90005].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [[podstawowe] Wróg / część [90006] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=90006].name
   limit: do 40 znaków
   EN: Famished Hooligan
   PL: Famished Hooligan
447. [[podstawowe] Wróg / część [90006] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90006].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [[podstawowe] Wróg / część [90007] — nazwa] 대가리 불한당
   źródło: Enemies.json :: dataList[id=90007].name
   limit: do 40 znaków
   EN: Head Hooligan
   PL: Head Hooligan
449. [[podstawowe] Wróg / część [90007] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90007].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [[podstawowe] Wróg / część [90008] — nazwa] 화난 패잔병
   źródło: Enemies.json :: dataList[id=90008].name
   limit: do 40 znaków
   EN: Fiery Veteran
   PL: Fiery Veteran
451. [[podstawowe] Wróg / część [90008] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90008].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [[podstawowe] Wróg / część [90009] — nazwa] 의아한 패잔병
   źródło: Enemies.json :: dataList[id=90009].name
   limit: do 40 znaków
   EN: Puzzled Veteran
   PL: Puzzled Veteran
453. [[podstawowe] Wróg / część [90009] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90009].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [[podstawowe] Wróg / część [90010] — nazwa] 허름한 패잔병
   źródło: Enemies.json :: dataList[id=90010].name
   limit: do 40 znaków
   EN: Scruffy Veteran
   PL: Scruffy Veteran
455. [[podstawowe] Wróg / część [90010] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90010].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [[podstawowe] Wróg / część [90011] — nazwa] 야비한 패잔병
   źródło: Enemies.json :: dataList[id=90011].name
   limit: do 40 znaków
   EN: Crooked Veteran
   PL: Crooked Veteran
457. [[podstawowe] Wróg / część [90011] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90011].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [[podstawowe] Wróg / część [90012] — nazwa] 입이 험한 패잔병
   źródło: Enemies.json :: dataList[id=90012].name
   limit: do 40 znaków
   EN: Vulgar Veteran
   PL: Vulgar Veteran
459. [[podstawowe] Wróg / część [90012] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90012].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [[podstawowe] Wróg / część [90013] — nazwa] 날이 선 패잔병
   źródło: Enemies.json :: dataList[id=90013].name
   limit: do 40 znaków
   EN: Razor-sharp Veteran
   PL: Razor-sharp Veteran
461. [[podstawowe] Wróg / część [90013] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90013].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [[podstawowe] Wróg / część [90001] — nazwa] 강해진 패잔병
   źródło: Enemies.json :: dataList[id=90001].name
   limit: do 40 znaków
   EN: Hardened Veteran
   PL: Hardened Veteran
463. [[podstawowe] Wróg / część [90001] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90001].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [[podstawowe] Wróg / część [90002] — nazwa] 짙어진 패잔병
   źródło: Enemies.json :: dataList[id=90002].name
   limit: do 40 znaków
   EN: Downcast Veteran
   PL: Downcast Veteran
465. [[podstawowe] Wróg / część [90002] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90002].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [[podstawowe] Wróg / część [90003] — nazwa] 모질어진 패잔병
   źródło: Enemies.json :: dataList[id=90003].name
   limit: do 40 znaków
   EN: Embittered Veteran
   PL: Embittered Veteran
467. [[podstawowe] Wróg / część [90003] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90003].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [[podstawowe] Wróg / część [90014] — nazwa] 기억속 어긋난 패잔병
   źródło: Enemies.json :: dataList[id=90014].name
   limit: do 40 znaków
   EN: Recollected Awry Soldier
   PL: Recollected Awry Soldier
469. [[podstawowe] Wróg / część [90014] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90014].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [[podstawowe] Wróg / część [90015] — nazwa] 기억속 절망하는 패잔병
   źródło: Enemies.json :: dataList[id=90015].name
   limit: do 50 znaków
   EN: Recollected Wallowing Soldier
   PL: Recollected Wallowing Soldier
471. [[podstawowe] Wróg / część [90015] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90015].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [[podstawowe] Wróg / część [90016] — nazwa] 기억속 침식된 패잔병
   źródło: Enemies.json :: dataList[id=90016].name
   limit: do 50 znaków
   EN: Recollected Overtaken Soldier
   PL: Recollected Overtaken Soldier
473. [[podstawowe] Wróg / część [90016] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90016].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [[podstawowe] Wróg / część [91001] — nazwa] 옛 G사 부장
   źródło: Enemies.json :: dataList[id=91001].name
   limit: do 40 znaków
   EN: Old G Corp. Head Manager
   PL: Old G Corp. Head Manager
475. [[podstawowe] Wróg / część [91001] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91001].desc
   limit: do 120 znaków
   EN: Enemy Boss
   PL: Enemy Boss
476. [[podstawowe] Wróg / część [91002] — nazwa] 기억속 짓물린 G사 부장
   źródło: Enemies.json :: dataList[id=91002].name
   limit: do 60 znaków
   EN: Recollected Festered G Corp. H. Manager
   PL: Recollected Festered G Corp. H. Manager
477. [[podstawowe] Wróg / część [91002] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91002].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [[podstawowe] Wróg / część [8901] — nazwa] 탐식 죄종
   źródło: Enemies.json :: dataList[id=8901].name
   limit: do 40 znaków
   EN: Peccatulum Gulae
   PL: Peccatulum Gulae
479. [[podstawowe] Wróg / część [8901] — opis] 본체
   źródło: Enemies.json :: dataList[id=8901].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [[podstawowe] Wróg / część [8005] — nazwa] 탐식 죄종
   źródło: Enemies.json :: dataList[id=8005].name
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [[podstawowe] Wróg / część [8005] — opis] 본체
   źródło: Enemies.json :: dataList[id=8005].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [[podstawowe] Wróg / część [8006] — nazwa] 나태 죄종
   źródło: Enemies.json :: dataList[id=8006].name
   limit: do 40 znaków
   EN: Peccatulum Pigritiae
   PL: Peccatulum Pigritiae
483. [[podstawowe] Wróg / część [8006] — opis] 본체
   źródło: Enemies.json :: dataList[id=8006].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [[podstawowe] Wróg / część [8007] — nazwa] 분노 죄종
   źródło: Enemies.json :: dataList[id=8007].name
   limit: do 40 znaków
   EN: Peccatulum Irae
   PL: Peccatulum Irae
485. [[podstawowe] Wróg / część [8007] — opis] 본체
   źródło: Enemies.json :: dataList[id=8007].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [[podstawowe] Wróg / część [8002] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=8002].name
   limit: do 40 znaków
   EN: Doomsday Calendar
   PL: Doomsday Calendar
487. [[podstawowe] Wróg / część [8002] — opis] 본체
   źródło: Enemies.json :: dataList[id=8002].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [[podstawowe] Wróg / część [80022] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=80022].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [[podstawowe] Wróg / część [80022] — opis] 본체
   źródło: Enemies.json :: dataList[id=80022].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [[podstawowe] Wróg / część [80023] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=80023].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [[podstawowe] Wróg / część [80023] — opis] 본체
   źródło: Enemies.json :: dataList[id=80023].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [[podstawowe] Wróg / część [80024] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=80024].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [[podstawowe] Wróg / część [80024] — opis] 본체
   źródło: Enemies.json :: dataList[id=80024].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [[podstawowe] Wróg / część [8003] — nazwa] 종말 토우
   źródło: Enemies.json :: dataList[id=8003].name
   limit: do 40 znaków
   EN: Doomsday Clay Doll
   PL: Doomsday Clay Doll
495. [[podstawowe] Wróg / część [8003] — opis] 본체
   źródło: Enemies.json :: dataList[id=8003].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [[podstawowe] Wróg / część [8004] — nazwa] 불타는 종말 토우
   źródło: Enemies.json :: dataList[id=8004].name
   limit: do 40 znaków
   EN: Burning Clay Doll
   PL: Burning Clay Doll
497. [[podstawowe] Wróg / część [8004] — opis] 본체
   źródło: Enemies.json :: dataList[id=8004].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [[podstawowe] Wróg / część [8008] — nazwa] 황금빛의 사과
   źródło: Enemies.json :: dataList[id=8008].name
   limit: do 40 znaków
   EN: Golden Apple
   PL: Golden Apple
499. [[podstawowe] Wróg / część [8008] — opis] 본체
   źródło: Enemies.json :: dataList[id=8008].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [[podstawowe] Wróg / część [8009] — nazwa] 거짓 사과
   źródło: Enemies.json :: dataList[id=8009].name
   limit: do 40 znaków
   EN: False Apple
   PL: False Apple
501. [[podstawowe] Wróg / część [8009] — opis] 본체
   źródło: Enemies.json :: dataList[id=8009].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [[podstawowe] Wróg / część [8010] — nazwa] 나 강해졌나? 정말?
   źródło: Enemies.json :: dataList[id=8010].name
   limit: do 40 znaków
   EN: Become Strong? Genuinely?
   PL: Become Strong? Genuinely?
503. [[podstawowe] Wróg / część [8010] — opis] 본체
   źródło: Enemies.json :: dataList[id=8010].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [[podstawowe] Wróg / część [8011] — nazwa] 나 세졌어! 진짜?
   źródło: Enemies.json :: dataList[id=8011].name
   limit: do 50 znaków
   EN: Grown Powerful! For Realsies?
   PL: Grown Powerful! For Realsies?
505. [[podstawowe] Wróg / część [8011] — opis] 본체
   źródło: Enemies.json :: dataList[id=8011].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [[podstawowe] Wróg / część [8012] — nazwa] 너 맞아볼래? 매우?
   źródło: Enemies.json :: dataList[id=8012].name
   limit: do 50 znaków
   EN: You Want To Get Beat? Hurtily?
   PL: You Want To Get Beat? Hurtily?
507. [[podstawowe] Wróg / część [8012] — opis] 본체
   źródło: Enemies.json :: dataList[id=8012].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [[podstawowe] Wróg / część [8013] — nazwa] 매혹하는 분홍신
   źródło: Enemies.json :: dataList[id=8013].name
   limit: do 40 znaków
   EN: Pink Shoes Enchantee
   PL: Pink Shoes Enchantee
509. [[podstawowe] Wróg / część [8013] — opis] 본체
   źródło: Enemies.json :: dataList[id=8013].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [[podstawowe] Wróg / część [8014] — nazwa] 홀리는 분홍신
   źródło: Enemies.json :: dataList[id=8014].name
   limit: do 40 znaków
   EN: Pink Shoes Possessee
   PL: Pink Shoes Possessee
511. [[podstawowe] Wróg / część [8014] — opis] 본체
   źródło: Enemies.json :: dataList[id=8014].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [[podstawowe] Wróg / część [8015] — nazwa] 또각또각? 걸어!
   źródło: Enemies.json :: dataList[id=8015].name
   limit: do 40 znaków
   EN: Clippity-cloppity? Tap Away!
   PL: Clippity-cloppity? Tap Away!
513. [[podstawowe] Wróg / część [8015] — opis] 본체
   źródło: Enemies.json :: dataList[id=8015].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [[podstawowe] Wróg / część [8016] — nazwa] 우울 죄종
   źródło: Enemies.json :: dataList[id=8016].name
   limit: do 40 znaków
   EN: Peccatulum Morositatis
   PL: Peccatulum Morositatis
515. [[podstawowe] Wróg / część [8016] — opis] 본체
   źródło: Enemies.json :: dataList[id=8016].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [[podstawowe] Wróg / część [8017] — nazwa] 색욕 죄종
   źródło: Enemies.json :: dataList[id=8017].name
   limit: do 40 znaków
   EN: Peccatulum Luxuriae
   PL: Peccatulum Luxuriae
517. [[podstawowe] Wróg / część [8017] — opis] 본체
   źródło: Enemies.json :: dataList[id=8017].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [[podstawowe] Wróg / część [8018] — nazwa] 오만 죄종
   źródło: Enemies.json :: dataList[id=8018].name
   limit: do 40 znaków
   EN: Peccatulum Superbiae
   PL: Peccatulum Superbiae
519. [[podstawowe] Wróg / część [8018] — opis] 본체
   źródło: Enemies.json :: dataList[id=8018].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [[podstawowe] Wróg / część [8019] — nazwa] 잠에서 깬 이웃
   źródło: Enemies.json :: dataList[id=8019].name
   limit: do 40 znaków
   EN: Slumber-broken Neighbor
   PL: Slumber-broken Neighbor
521. [[podstawowe] Wróg / część [8019] — opis] 본체
   źródło: Enemies.json :: dataList[id=8019].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [[podstawowe] Wróg / część [8020] — nazwa] 다시 일어난 이웃
   źródło: Enemies.json :: dataList[id=8020].name
   limit: do 40 znaków
   EN: Rearisen Neighbor
   PL: Rearisen Neighbor
523. [[podstawowe] Wróg / część [8020] — opis] 본체
   źródło: Enemies.json :: dataList[id=8020].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [[podstawowe] Wróg / część [8021] — nazwa] 얼어가는 광산 노예
   źródło: Enemies.json :: dataList[id=8021].name
   limit: do 40 znaków
   EN: Freezing Miner Slave
   PL: Freezing Miner Slave
525. [[podstawowe] Wróg / część [8021] — opis] 본체
   źródło: Enemies.json :: dataList[id=8021].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [[podstawowe] Wróg / część [8022] — nazwa] 추워하는 광산 노예
   źródło: Enemies.json :: dataList[id=8022].name
   limit: do 40 znaków
   EN: Shivering Miner Slave
   PL: Shivering Miner Slave
527. [[podstawowe] Wróg / część [8022] — opis] 본체
   źródło: Enemies.json :: dataList[id=8022].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [[podstawowe] Wróg / część [8023] — nazwa] 바바 야가
   źródło: Enemies.json :: dataList[id=8023].name
   limit: do 40 znaków
   EN: Baba Yaga
   PL: Baba Yaga
529. [[podstawowe] Wróg / część [8023] — opis] 본체
   źródło: Enemies.json :: dataList[id=8023].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
530. [[podstawowe] Wróg / część [8024] — nazwa] 나아가려 하는 이단심문관
   źródło: Enemies.json :: dataList[id=8024].name
   limit: do 40 znaków
   EN: Proceeding Inquisitor
   PL: Proceeding Inquisitor
531. [[podstawowe] Wróg / część [8024] — opis] 본체
   źródło: Enemies.json :: dataList[id=8024].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [[podstawowe] Wróg / część [8025] — nazwa] 네 발 짐승
   źródło: Enemies.json :: dataList[id=8025].name
   limit: do 40 znaków
   EN: Four-legged Beast
   PL: Four-legged Beast
533. [[podstawowe] Wróg / część [8025] — opis] 본체
   źródło: Enemies.json :: dataList[id=8025].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [[podstawowe] Wróg / część [8026] — nazwa] 모든 것이 있는 이단 심문관
   źródło: Enemies.json :: dataList[id=8026].name
   limit: do 50 znaków
   EN: Everything There of an Inquisitor
   PL: Everything There of an Inquisitor
535. [[podstawowe] Wróg / część [8026] — opis] 본체
   źródło: Enemies.json :: dataList[id=8026].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [[podstawowe] Wróg / część [8027] — nazwa] 기어다니는 이단 심문관
   źródło: Enemies.json :: dataList[id=8027].name
   limit: do 40 znaków
   EN: Crawling Inquisitor
   PL: Crawling Inquisitor
537. [[podstawowe] Wróg / część [8027] — opis] 본체
   źródło: Enemies.json :: dataList[id=8027].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [[podstawowe] Wróg / część [8028] — nazwa] 꿈틀거리는 이단 심문관
   źródło: Enemies.json :: dataList[id=8028].name
   limit: do 40 znaków
   EN: Slithering Inquisitor
   PL: Slithering Inquisitor
539. [[podstawowe] Wróg / część [8028] — opis] 본체
   źródło: Enemies.json :: dataList[id=8028].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [[podstawowe] Wróg / część [8029] — nazwa] 크로머
   źródło: Enemies.json :: dataList[id=8029].name
   limit: do 40 znaków
   EN: Kromer
   PL: Kromer
541. [[podstawowe] Wróg / część [8029] — opis] 본체
   źródło: Enemies.json :: dataList[id=8029].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [[podstawowe] Wróg / część [8030] — nazwa] 온전한 인간을 꿈꾸는 크로머
   źródło: Enemies.json :: dataList[id=8030].name
   limit: do 60 znaków
   EN: Kromer the Dreamer of Human Wholeness
   PL: Kromer the Dreamer of Human Wholeness
543. [[podstawowe] Wróg / część [8030] — opis] 본체
   źródło: Enemies.json :: dataList[id=8030].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [[podstawowe] Wróg / część [8031] — nazwa] 단수어
   źródło: Enemies.json :: dataList[id=8031].name
   limit: do 40 znaków
   EN: Headless Ichthys
   PL: Headless Ichthys
545. [[podstawowe] Wróg / część [8031] — opis] 본체
   źródło: Enemies.json :: dataList[id=8031].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [[podstawowe] Wróg / część [8032] — nazwa] 골목파수견
   źródło: Enemies.json :: dataList[id=8032].name
   limit: do 40 znaków
   EN: Alleyway Watchdog
   PL: Alleyway Watchdog
547. [[podstawowe] Wróg / część [8032] — opis] 본체
   źródło: Enemies.json :: dataList[id=8032].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [[podstawowe] Wróg / część [890101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=890101].name
   limit: do 40 znaków
   EN: Body
   PL: Body
549. [[podstawowe] Wróg / część [890101] — opis] 부위
   źródło: Enemies.json :: dataList[id=890101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [[podstawowe] Wróg / część [800501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=800501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [[podstawowe] Wróg / część [800501] — opis] 부위
   źródło: Enemies.json :: dataList[id=800501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [[podstawowe] Wróg / część [800601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=800601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [[podstawowe] Wróg / część [800601] — opis] 부위
   źródło: Enemies.json :: dataList[id=800601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [[podstawowe] Wróg / część [800701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=800701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [[podstawowe] Wróg / część [800701] — opis] 부위
   źródło: Enemies.json :: dataList[id=800701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [[podstawowe] Wróg / część [800201] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=800201].name
   limit: do 40 znaków
   EN: Left Arm
   PL: Left Arm
557. [[podstawowe] Wróg / część [800201] — opis] 부위
   źródło: Enemies.json :: dataList[id=800201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [[podstawowe] Wróg / część [800202] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=800202].name
   limit: do 40 znaków
   EN: Right Arm
   PL: Right Arm
559. [[podstawowe] Wróg / część [800202] — opis] 부위
   źródło: Enemies.json :: dataList[id=800202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [[podstawowe] Wróg / część [800203] — nazwa] 얼굴
   źródło: Enemies.json :: dataList[id=800203].name
   limit: do 40 znaków
   EN: Face
   PL: Face
561. [[podstawowe] Wróg / część [800203] — opis] 부위
   źródło: Enemies.json :: dataList[id=800203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [[podstawowe] Wróg / część [800301] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=800301].name
   limit: do 40 znaków
   EN: Head
   PL: Head
563. [[podstawowe] Wróg / część [800301] — opis] 부위
   źródło: Enemies.json :: dataList[id=800301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [[podstawowe] Wróg / część [800401] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=800401].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [[podstawowe] Wróg / część [800401] — opis] 부위
   źródło: Enemies.json :: dataList[id=800401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [[podstawowe] Wróg / część [800801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=800801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [[podstawowe] Wróg / część [800801] — opis] 부위
   źródło: Enemies.json :: dataList[id=800801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [[podstawowe] Wróg / część [800901] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=800901].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [[podstawowe] Wróg / część [800901] — opis] 부위
   źródło: Enemies.json :: dataList[id=800901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [[podstawowe] Wróg / część [800902] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=800902].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [[podstawowe] Wróg / część [800902] — opis] 부위
   źródło: Enemies.json :: dataList[id=800902].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [[podstawowe] Wróg / część [800903] — nazwa] 다리
   źródło: Enemies.json :: dataList[id=800903].name
   limit: do 40 znaków
   EN: Legs
   PL: Legs
573. [[podstawowe] Wróg / część [800903] — opis] 부위
   źródło: Enemies.json :: dataList[id=800903].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [[podstawowe] Wróg / część [801001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [[podstawowe] Wróg / część [801001] — opis] 부위
   źródło: Enemies.json :: dataList[id=801001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [[podstawowe] Wróg / część [801101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [[podstawowe] Wróg / część [801101] — opis] 부위
   źródło: Enemies.json :: dataList[id=801101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [[podstawowe] Wróg / część [801201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [[podstawowe] Wróg / część [801201] — opis] 부위
   źródło: Enemies.json :: dataList[id=801201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [[podstawowe] Wróg / część [801202] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=801202].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [[podstawowe] Wróg / część [801202] — opis] 부위
   źródło: Enemies.json :: dataList[id=801202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [[podstawowe] Wróg / część [801301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [[podstawowe] Wróg / część [801301] — opis] 부위
   źródło: Enemies.json :: dataList[id=801301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [[podstawowe] Wróg / część [801401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [[podstawowe] Wróg / część [801401] — opis] 부위
   źródło: Enemies.json :: dataList[id=801401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [[podstawowe] Wróg / część [801501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [[podstawowe] Wróg / część [801501] — opis] 부위
   źródło: Enemies.json :: dataList[id=801501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [[podstawowe] Wróg / część [801502] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=801502].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [[podstawowe] Wróg / część [801502] — opis] 부위
   źródło: Enemies.json :: dataList[id=801502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [[podstawowe] Wróg / część [801601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [[podstawowe] Wróg / część [801601] — opis] 부위
   źródło: Enemies.json :: dataList[id=801601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [[podstawowe] Wróg / część [801701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [[podstawowe] Wróg / część [801701] — opis] 부위
   źródło: Enemies.json :: dataList[id=801701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [[podstawowe] Wróg / część [801801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [[podstawowe] Wróg / część [801801] — opis] 부위
   źródło: Enemies.json :: dataList[id=801801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [[podstawowe] Wróg / część [801901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=801901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [[podstawowe] Wróg / część [801901] — opis] 부위
   źródło: Enemies.json :: dataList[id=801901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [[podstawowe] Wróg / część [802001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [[podstawowe] Wróg / część [802001] — opis] 부위
   źródło: Enemies.json :: dataList[id=802001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [[podstawowe] Wróg / część [802101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [[podstawowe] Wróg / część [802101] — opis] 부위
   źródło: Enemies.json :: dataList[id=802101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [[podstawowe] Wróg / część [802201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [[podstawowe] Wróg / część [802201] — opis] 부위
   źródło: Enemies.json :: dataList[id=802201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [[podstawowe] Wróg / część [802301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [[podstawowe] Wróg / część [802301] — opis] 부위
   źródło: Enemies.json :: dataList[id=802301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [[podstawowe] Wróg / część [802401] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=802401].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [[podstawowe] Wróg / część [802401] — opis] 부위
   źródło: Enemies.json :: dataList[id=802401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [[podstawowe] Wróg / część [802402] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802402].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [[podstawowe] Wróg / część [802402] — opis] 부위
   źródło: Enemies.json :: dataList[id=802402].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [[podstawowe] Wróg / część [802501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [[podstawowe] Wróg / część [802501] — opis] 부위
   źródło: Enemies.json :: dataList[id=802501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [[podstawowe] Wróg / część [802601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [[podstawowe] Wróg / część [802601] — opis] 부위
   źródło: Enemies.json :: dataList[id=802601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [[podstawowe] Wróg / część [802701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [[podstawowe] Wróg / część [802701] — opis] 부위
   źródło: Enemies.json :: dataList[id=802701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [[podstawowe] Wróg / część [802801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [[podstawowe] Wróg / część [802801] — opis] 부위
   źródło: Enemies.json :: dataList[id=802801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [[podstawowe] Wróg / część [802802] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=802802].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [[podstawowe] Wróg / część [802802] — opis] 부위
   źródło: Enemies.json :: dataList[id=802802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [[podstawowe] Wróg / część [802803] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=802803].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [[podstawowe] Wróg / część [802803] — opis] 부위
   źródło: Enemies.json :: dataList[id=802803].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [[podstawowe] Wróg / część [802901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=802901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [[podstawowe] Wróg / część [802901] — opis] 부위
   źródło: Enemies.json :: dataList[id=802901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [[podstawowe] Wróg / część [803001] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=803001].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [[podstawowe] Wróg / część [803001] — opis] 부위
   źródło: Enemies.json :: dataList[id=803001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [[podstawowe] Wróg / część [803002] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=803002].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [[podstawowe] Wróg / część [803002] — opis] 부위
   źródło: Enemies.json :: dataList[id=803002].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [[podstawowe] Wróg / część [803003] — nazwa] 큰입
   źródło: Enemies.json :: dataList[id=803003].name
   limit: do 40 znaków
   EN: Maw
   PL: Maw
629. [[podstawowe] Wróg / część [803003] — opis] 부위
   źródło: Enemies.json :: dataList[id=803003].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [[podstawowe] Wróg / część [803004] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803004].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [[podstawowe] Wróg / część [803004] — opis] 부위
   źródło: Enemies.json :: dataList[id=803004].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [[podstawowe] Wróg / część [803101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [[podstawowe] Wróg / część [803101] — opis] 부위
   źródło: Enemies.json :: dataList[id=803101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [[podstawowe] Wróg / część [803102] — nazwa] 오른다리
   źródło: Enemies.json :: dataList[id=803102].name
   limit: do 40 znaków
   EN: Right Leg
   PL: Right Leg
635. [[podstawowe] Wróg / część [803102] — opis] 부위
   źródło: Enemies.json :: dataList[id=803102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [[podstawowe] Wróg / część [803103] — nazwa] 왼다리
   źródło: Enemies.json :: dataList[id=803103].name
   limit: do 40 znaków
   EN: Left Leg
   PL: Left Leg
637. [[podstawowe] Wróg / część [803103] — opis] 부위
   źródło: Enemies.json :: dataList[id=803103].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [[podstawowe] Wróg / część [803104] — nazwa] 꼬리
   źródło: Enemies.json :: dataList[id=803104].name
   limit: do 40 znaków
   EN: Tail
   PL: Tail
639. [[podstawowe] Wróg / część [803104] — opis] 부위
   źródło: Enemies.json :: dataList[id=803104].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [[podstawowe] Wróg / część [803201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [[podstawowe] Wróg / część [803201] — opis] 부위
   źródło: Enemies.json :: dataList[id=803201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [[podstawowe] Wróg / część [803202] — nazwa] 전봇대
   źródło: Enemies.json :: dataList[id=803202].name
   limit: do 40 znaków
   EN: Telepole
   PL: Telepole
643. [[podstawowe] Wróg / część [803202] — opis] 부위
   źródło: Enemies.json :: dataList[id=803202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [[podstawowe] Wróg / część [803203] — nazwa] 사람
   źródło: Enemies.json :: dataList[id=803203].name
   limit: do 40 znaków
   EN: Person
   PL: Person
645. [[podstawowe] Wróg / część [803203] — opis] 부위
   źródło: Enemies.json :: dataList[id=803203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [[podstawowe] Wróg / część [803204] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=803204].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [[podstawowe] Wróg / część [803204] — opis] 부위
   źródło: Enemies.json :: dataList[id=803204].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [[podstawowe] Wróg / część [90017] — nazwa] 촌스러운 말투의 콩콩이파 조직원
   źródło: Enemies.json :: dataList[id=90017].name
   limit: do 40 znaków
   EN: Rustic-sounding Tingtanger
   PL: Rustic-sounding Tingtanger
649. [[podstawowe] Wróg / część [90017] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90017].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [[podstawowe] Wróg / część [90018] — nazwa] 세 보이고 싶었던 콩콩이파 조직원
   źródło: Enemies.json :: dataList[id=90018].name
   limit: do 40 znaków
   EN: Chest-puffing Tingtanger
   PL: Chest-puffing Tingtanger
651. [[podstawowe] Wróg / część [90018] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90018].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [[podstawowe] Wróg / część [90019] — nazwa] 콩을 싫어하는 콩콩이파 조직원
   źródło: Enemies.json :: dataList[id=90019].name
   limit: do 40 znaków
   EN: Bean-hating Tingtanger
   PL: Bean-hating Tingtanger
653. [[podstawowe] Wróg / część [90019] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90019].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [[podstawowe] Wróg / część [91003] — nazwa] 콩콩이파 보스
   źródło: Enemies.json :: dataList[id=91003].name
   limit: do 40 znaków
   EN: Tingtang Boss
   PL: Tingtang Boss
655. [[podstawowe] Wróg / część [91003] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91003].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [[podstawowe] Wróg / część [90020] — nazwa] 각 잡힌 카지노 경호원
   źródło: Enemies.json :: dataList[id=90020].name
   limit: do 40 znaków
   EN: Rigid Casino Security
   PL: Rigid Casino Security
657. [[podstawowe] Wróg / część [90020] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90020].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [[podstawowe] Wróg / część [90021] — nazwa] 자신있는 카지노 경호원
   źródło: Enemies.json :: dataList[id=90021].name
   limit: do 40 znaków
   EN: Confident Casino Security
   PL: Confident Casino Security
659. [[podstawowe] Wróg / część [90021] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90021].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [[podstawowe] Wróg / część [90022] — nazwa] 마음 다잡는 카지노 경호원
   źródło: Enemies.json :: dataList[id=90022].name
   limit: do 40 znaków
   EN: Collected Casino Security
   PL: Collected Casino Security
661. [[podstawowe] Wróg / część [90022] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90022].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [[podstawowe] Wróg / część [90023] — nazwa] 카지노 경호원 대장
   źródło: Enemies.json :: dataList[id=90023].name
   limit: do 40 znaków
   EN: Casino Security Chief
   PL: Casino Security Chief
663. [[podstawowe] Wróg / część [90023] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90023].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [[podstawowe] Wróg / część [90024] — nazwa] 흥겨운 마리아치 조직원
   źródło: Enemies.json :: dataList[id=90024].name
   limit: do 40 znaków
   EN: Mariachi Alegre
   PL: Mariachi Alegre
665. [[podstawowe] Wróg / część [90024] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90024].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [[podstawowe] Wróg / część [90025] — nazwa] 경쾌한 마리아치 조직원
   źródło: Enemies.json :: dataList[id=90025].name
   limit: do 40 znaków
   EN: Mariachi Vivaz
   PL: Mariachi Vivaz
667. [[podstawowe] Wróg / część [90025] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90025].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [[podstawowe] Wróg / część [91004] — nazwa] 아이드
   źródło: Enemies.json :: dataList[id=91004].name
   limit: do 40 znaków
   EN: Aida
   PL: Aida
669. [[podstawowe] Wróg / część [91004] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91004].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [[podstawowe] Wróg / część [90026] — nazwa] 위협적인 철공회 조직원
   źródło: Enemies.json :: dataList[id=90026].name
   limit: do 40 znaków
   EN: Threatening Tieqiu Crewman
   PL: Threatening Tieqiu Crewman
671. [[podstawowe] Wróg / część [90026] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90026].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [[podstawowe] Wróg / część [90027] — nazwa] 몸 푸는 철공회 조직원
   źródło: Enemies.json :: dataList[id=90027].name
   limit: do 40 znaków
   EN: Flexing Tieqiu Crewman
   PL: Flexing Tieqiu Crewman
673. [[podstawowe] Wróg / część [90027] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90027].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [[podstawowe] Wróg / część [90028] — nazwa] 침착한 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90028].name
   limit: do 50 znaków
   EN: Calm K Corp. Checkpoint Security
   PL: Calm K Corp. Checkpoint Security
675. [[podstawowe] Wróg / część [90028] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90028].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [[podstawowe] Wróg / część [90029] — nazwa] 말없는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90029].name
   limit: do 50 znaków
   EN: Quiet K Corp. Checkpoint Security
   PL: Quiet K Corp. Checkpoint Security
677. [[podstawowe] Wróg / część [90029] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90029].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [[podstawowe] Wróg / część [90030] — nazwa] 우직한 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90030].name
   limit: do 50 znaków
   EN: Stern K Corp. Checkpoint Security
   PL: Stern K Corp. Checkpoint Security
679. [[podstawowe] Wróg / część [90030] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90030].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [[podstawowe] Wróg / część [90031] — nazwa] 든든한 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90031].name
   limit: do 50 znaków
   EN: Reliable K Corp. Checkpoint Security
   PL: Reliable K Corp. Checkpoint Security
681. [[podstawowe] Wróg / część [90031] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90031].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [[podstawowe] Wróg / część [90032] — nazwa] 받드는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90032].name
   limit: do 40 znaków
   EN: Servile N Corp. Inquisitor
   PL: Servile N Corp. Inquisitor
683. [[podstawowe] Wróg / część [90032] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90032].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [[podstawowe] Wróg / część [90033] — nazwa] 따르는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90033].name
   limit: do 40 znaków
   EN: Compliant N Corp. Inquisitor
   PL: Compliant N Corp. Inquisitor
685. [[podstawowe] Wróg / część [90033] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90033].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [[podstawowe] Wróg / część [90034] — nazwa] 섬기는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90034].name
   limit: do 50 znaków
   EN: Worshipping N Corp. Inquisitor
   PL: Worshipping N Corp. Inquisitor
687. [[podstawowe] Wróg / część [90034] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90034].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [[podstawowe] Wróg / część [90035] — nazwa] 고문하는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90035].name
   limit: do 40 znaków
   EN: Scourging N Corp. Inquisitor
   PL: Scourging N Corp. Inquisitor
689. [[podstawowe] Wróg / część [90035] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90035].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [[podstawowe] Wróg / część [90036] — nazwa] 심문에 능한 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90036].name
   limit: do 50 znaków
   EN: Interrogative N Corp. Inquisitor
   PL: Interrogative N Corp. Inquisitor
691. [[podstawowe] Wróg / część [90036] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90036].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [[podstawowe] Wróg / część [90037] — nazwa] 고통을 즐기는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90037].name
   limit: do 40 znaków
   EN: Sadistic N Corp. Inquisitor
   PL: Sadistic N Corp. Inquisitor
693. [[podstawowe] Wróg / część [90037] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90037].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [[podstawowe] Wróg / część [90038] — nazwa] 집착하는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90038].name
   limit: do 40 znaków
   EN: Obsessive N Corp. Inquisitor
   PL: Obsessive N Corp. Inquisitor
695. [[podstawowe] Wróg / część [90038] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90038].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [[podstawowe] Wróg / część [90039] — nazwa] 으뜸 기쁨의 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90039].name
   limit: do 40 znaków
   EN: Joyous N Corp. Inquisitor
   PL: Joyous N Corp. Inquisitor
697. [[podstawowe] Wróg / część [90039] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90039].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [[podstawowe] Wróg / część [90040] — nazwa] 두려움 없는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=90040].name
   limit: do 40 znaków
   EN: Fearless N Corp. Inquisitor
   PL: Fearless N Corp. Inquisitor
699. [[podstawowe] Wróg / część [90040] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90040].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [[podstawowe] Wróg / część [91005] — nazwa] 집념의 귀도
   źródło: Enemies.json :: dataList[id=91005].name
   limit: do 40 znaków
   EN: Guido the Persistent
   PL: Guido the Persistent
701. [[podstawowe] Wróg / część [91005] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=91005].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [[podstawowe] Wróg / część [91006] — nazwa] 집념의 귀도
   źródło: Enemies.json :: dataList[id=91006].name
   (powtórzenie elementu 700 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [[podstawowe] Wróg / część [91006] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=91006].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [[podstawowe] Wróg / część [99004] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99004].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [[podstawowe] Wróg / część [99004] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99004].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [[podstawowe] Wróg / część [99005] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99005].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [[podstawowe] Wróg / część [99005] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99005].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [[podstawowe] Wróg / część [99006] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99006].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [[podstawowe] Wróg / część [99006] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99006].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [[podstawowe] Wróg / część [99007] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99007].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [[podstawowe] Wróg / część [99007] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99007].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [[podstawowe] Wróg / część [99008] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99008].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [[podstawowe] Wróg / część [99008] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99008].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [[podstawowe] Wróg / część [99009] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99009].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [[podstawowe] Wróg / część [99009] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99009].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [[podstawowe] Wróg / część [99010] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99010].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [[podstawowe] Wróg / część [99010] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99010].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [[podstawowe] Wróg / część [99011] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99011].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [[podstawowe] Wróg / część [99011] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99011].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [[podstawowe] Wróg / część [99012] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99012].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [[podstawowe] Wróg / część [99012] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99012].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [[podstawowe] Wróg / część [99013] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99013].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [[podstawowe] Wróg / część [99013] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99013].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [[podstawowe] Wróg / część [99014] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99014].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [[podstawowe] Wróg / część [99014] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99014].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [[podstawowe] Wróg / część [99015] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99015].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [[podstawowe] Wróg / część [99015] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99015].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [[podstawowe] Wróg / część [99016] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99016].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [[podstawowe] Wróg / część [99016] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99016].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [[podstawowe] Wróg / część [99017] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99017].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [[podstawowe] Wróg / część [99017] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99017].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [[podstawowe] Wróg / część [99018] — nazwa] 대가리 불한당
   źródło: Enemies.json :: dataList[id=99018].name
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [[podstawowe] Wróg / część [99018] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99018].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [[podstawowe] Wróg / część [99019] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99019].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [[podstawowe] Wróg / część [99019] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99019].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [[podstawowe] Wróg / część [99020] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99020].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [[podstawowe] Wróg / część [99020] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99020].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [[podstawowe] Wróg / część [99021] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99021].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [[podstawowe] Wróg / część [99021] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=99021].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [[podstawowe] Wróg / część [90041] — nazwa] 노예
   źródło: Enemies.json :: dataList[id=90041].name
   limit: do 40 znaków
   EN: Slave
   PL: Slave
741. [[podstawowe] Wróg / część [90041] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90041].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [[podstawowe] Wróg / część [8033] — nazwa] 꿈틀거리는 짐승
   źródło: Enemies.json :: dataList[id=8033].name
   limit: do 40 znaków
   EN: Wriggling Beast
   PL: Wriggling Beast
743. [[podstawowe] Wróg / część [8033] — opis] 본체
   źródło: Enemies.json :: dataList[id=8033].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [[podstawowe] Wróg / część [803301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [[podstawowe] Wróg / część [803301] — opis] 부위
   źródło: Enemies.json :: dataList[id=803301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [[podstawowe] Wróg / część [803302] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=803302].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [[podstawowe] Wróg / część [803302] — opis] 부위
   źródło: Enemies.json :: dataList[id=803302].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [[podstawowe] Wróg / część [97101] — nazwa] 야비한 패잔병
   źródło: Enemies.json :: dataList[id=97101].name
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [[podstawowe] Wróg / część [97101] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97101].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [[podstawowe] Wróg / część [97102] — nazwa] 입이 험한 패잔병
   źródło: Enemies.json :: dataList[id=97102].name
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [[podstawowe] Wróg / część [97102] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97102].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [[podstawowe] Wróg / część [97103] — nazwa] 날이 선 패잔병
   źródło: Enemies.json :: dataList[id=97103].name
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [[podstawowe] Wróg / część [97103] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97103].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [[podstawowe] Wróg / część [97104] — nazwa] 강해진 패잔병
   źródło: Enemies.json :: dataList[id=97104].name
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [[podstawowe] Wróg / część [97104] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97104].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [[podstawowe] Wróg / część [97105] — nazwa] 짙어진 패잔병
   źródło: Enemies.json :: dataList[id=97105].name
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [[podstawowe] Wróg / część [97105] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97105].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [[podstawowe] Wróg / część [97106] — nazwa] 모질어진 패잔병
   źródło: Enemies.json :: dataList[id=97106].name
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [[podstawowe] Wróg / część [97106] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97106].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [[podstawowe] Wróg / część [97107] — nazwa] 기억속 어긋난 패잔병
   źródło: Enemies.json :: dataList[id=97107].name
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [[podstawowe] Wróg / część [97107] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97107].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [[podstawowe] Wróg / część [97108] — nazwa] 기억속 절망하는 패잔병
   źródło: Enemies.json :: dataList[id=97108].name
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [[podstawowe] Wróg / część [97108] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97108].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [[podstawowe] Wróg / część [97109] — nazwa] 기억속 침식된 패잔병
   źródło: Enemies.json :: dataList[id=97109].name
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [[podstawowe] Wróg / część [97109] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97109].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [[podstawowe] Wróg / część [97151] — nazwa] 옛 G사 부장
   źródło: Enemies.json :: dataList[id=97151].name
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [[podstawowe] Wróg / część [97151] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=97151].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [[podstawowe] Wróg / część [97152] — nazwa] 기억속 짓물린 G사 부장
   źródło: Enemies.json :: dataList[id=97152].name
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [[podstawowe] Wróg / część [97152] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=97152].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [[podstawowe] Wróg / część [97201] — nazwa] 각 잡힌 카지노 경호원
   źródło: Enemies.json :: dataList[id=97201].name
   (powtórzenie elementu 656 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [[podstawowe] Wróg / część [97201] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97201].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [[podstawowe] Wróg / część [97202] — nazwa] 자신있는 카지노 경호원
   źródło: Enemies.json :: dataList[id=97202].name
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [[podstawowe] Wróg / część [97202] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97202].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [[podstawowe] Wróg / część [97203] — nazwa] 마음 다잡는 카지노 경호원
   źródło: Enemies.json :: dataList[id=97203].name
   (powtórzenie elementu 660 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [[podstawowe] Wróg / część [97203] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97203].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [[podstawowe] Wróg / część [97204] — nazwa] 흥겨운 마리아치 조직원
   źródło: Enemies.json :: dataList[id=97204].name
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [[podstawowe] Wróg / część [97204] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97204].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [[podstawowe] Wróg / część [97205] — nazwa] 경쾌한 마리아치 조직원
   źródło: Enemies.json :: dataList[id=97205].name
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [[podstawowe] Wróg / część [97205] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97205].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [[podstawowe] Wróg / część [97206] — nazwa] 위협적인 철공회 조직원
   źródło: Enemies.json :: dataList[id=97206].name
   (powtórzenie elementu 670 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [[podstawowe] Wróg / część [97206] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97206].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [[podstawowe] Wróg / część [97207] — nazwa] 몸 푸는 철공회 조직원
   źródło: Enemies.json :: dataList[id=97207].name
   (powtórzenie elementu 672 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [[podstawowe] Wróg / część [97207] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97207].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [[podstawowe] Wróg / część [97251] — nazwa] 카지노 경호원 대장
   źródło: Enemies.json :: dataList[id=97251].name
   (powtórzenie elementu 662 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [[podstawowe] Wróg / część [97251] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97251].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [[podstawowe] Wróg / część [97252] — nazwa] 아이드
   źródło: Enemies.json :: dataList[id=97252].name
   (powtórzenie elementu 668 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [[podstawowe] Wróg / część [97252] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=97252].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [[podstawowe] Wróg / część [97301] — nazwa] 받드는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97301].name
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [[podstawowe] Wróg / część [97301] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97301].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [[podstawowe] Wróg / część [97302] — nazwa] 따르는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97302].name
   (powtórzenie elementu 684 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [[podstawowe] Wróg / część [97302] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97302].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [[podstawowe] Wróg / część [97303] — nazwa] 섬기는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97303].name
   (powtórzenie elementu 686 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [[podstawowe] Wróg / część [97303] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97303].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [[podstawowe] Wróg / część [97304] — nazwa] 고문하는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97304].name
   (powtórzenie elementu 688 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [[podstawowe] Wróg / część [97304] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97304].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [[podstawowe] Wróg / część [97305] — nazwa] 심문에 능한 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97305].name
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [[podstawowe] Wróg / część [97305] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97305].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [[podstawowe] Wróg / część [97306] — nazwa] 고통을 즐기는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97306].name
   (powtórzenie elementu 692 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [[podstawowe] Wróg / część [97306] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97306].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [[podstawowe] Wróg / część [97307] — nazwa] 집착하는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97307].name
   (powtórzenie elementu 694 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [[podstawowe] Wróg / część [97307] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97307].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [[podstawowe] Wróg / część [97308] — nazwa] 으뜸 기쁨의 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97308].name
   (powtórzenie elementu 696 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [[podstawowe] Wróg / część [97308] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97308].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [[podstawowe] Wróg / część [97309] — nazwa] 두려움 없는 N사 이단 심문관
   źródło: Enemies.json :: dataList[id=97309].name
   (powtórzenie elementu 698 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [[podstawowe] Wróg / część [97309] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97309].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [[podstawowe] Wróg / część [97351] — nazwa] 집념의 귀도
   źródło: Enemies.json :: dataList[id=97351].name
   (powtórzenie elementu 700 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [[podstawowe] Wróg / część [97351] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=97351].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [[podstawowe] Wróg / część [8701] — nazwa] 흑단여왕의 사과
   źródło: Enemies.json :: dataList[id=8701].name
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [[podstawowe] Wróg / część [8701] — opis] 본체
   źródło: Enemies.json :: dataList[id=8701].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [[podstawowe] Wróg / część [870101] — nazwa] 열매
   źródło: Enemies.json :: dataList[id=870101].name
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [[podstawowe] Wróg / część [870101] — opis] 부위
   źródło: Enemies.json :: dataList[id=870101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [[podstawowe] Wróg / część [870102] — nazwa] 왼쪽 줄기
   źródło: Enemies.json :: dataList[id=870102].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [[podstawowe] Wróg / część [870102] — opis] 부위
   źródło: Enemies.json :: dataList[id=870102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [[podstawowe] Wróg / część [870103] — nazwa] 오른쪽 줄기
   źródło: Enemies.json :: dataList[id=870103].name
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [[podstawowe] Wróg / część [870103] — opis] 부위
   źródło: Enemies.json :: dataList[id=870103].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [[podstawowe] Wróg / część [870104] — nazwa] 뿌리
   źródło: Enemies.json :: dataList[id=870104].name
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [[podstawowe] Wróg / część [870104] — opis] 부위
   źródło: Enemies.json :: dataList[id=870104].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [[podstawowe] Wróg / część [8702] — nazwa] 단수어
   źródło: Enemies.json :: dataList[id=8702].name
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [[podstawowe] Wróg / część [8702] — opis] 본체
   źródło: Enemies.json :: dataList[id=8702].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [[podstawowe] Wróg / część [870201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [[podstawowe] Wróg / część [870201] — opis] 부위
   źródło: Enemies.json :: dataList[id=870201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [[podstawowe] Wróg / część [870202] — nazwa] 오른다리
   źródło: Enemies.json :: dataList[id=870202].name
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [[podstawowe] Wróg / część [870202] — opis] 부위
   źródło: Enemies.json :: dataList[id=870202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [[podstawowe] Wróg / część [870203] — nazwa] 왼다리
   źródło: Enemies.json :: dataList[id=870203].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [[podstawowe] Wróg / część [870203] — opis] 부위
   źródło: Enemies.json :: dataList[id=870203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [[podstawowe] Wróg / część [870204] — nazwa] 꼬리
   źródło: Enemies.json :: dataList[id=870204].name
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [[podstawowe] Wróg / część [870204] — opis] 부위
   źródło: Enemies.json :: dataList[id=870204].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [[podstawowe] Wróg / część [8703] — nazwa] 황금빛의 사과
   źródło: Enemies.json :: dataList[id=8703].name
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [[podstawowe] Wróg / część [8703] — opis] 본체
   źródło: Enemies.json :: dataList[id=8703].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [[podstawowe] Wróg / część [870301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [[podstawowe] Wróg / część [870301] — opis] 부위
   źródło: Enemies.json :: dataList[id=870301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [[podstawowe] Wróg / część [8704] — nazwa] 거짓 사과
   źródło: Enemies.json :: dataList[id=8704].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [[podstawowe] Wróg / część [8704] — opis] 본체
   źródło: Enemies.json :: dataList[id=8704].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [[podstawowe] Wróg / część [870401] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=870401].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [[podstawowe] Wróg / część [870401] — opis] 부위
   źródło: Enemies.json :: dataList[id=870401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [[podstawowe] Wróg / część [870402] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870402].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [[podstawowe] Wróg / część [870402] — opis] 부위
   źródło: Enemies.json :: dataList[id=870402].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [[podstawowe] Wróg / część [870403] — nazwa] 다리
   źródło: Enemies.json :: dataList[id=870403].name
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [[podstawowe] Wróg / część [870403] — opis] 부위
   źródło: Enemies.json :: dataList[id=870403].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [[podstawowe] Wróg / część [8705] — nazwa] 골목파수견
   źródło: Enemies.json :: dataList[id=8705].name
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [[podstawowe] Wróg / część [8705] — opis] 본체
   źródło: Enemies.json :: dataList[id=8705].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [[podstawowe] Wróg / część [870501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [[podstawowe] Wróg / część [870501] — opis] 부위
   źródło: Enemies.json :: dataList[id=870501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [[podstawowe] Wróg / część [870502] — nazwa] 전봇대
   źródło: Enemies.json :: dataList[id=870502].name
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [[podstawowe] Wróg / część [870502] — opis] 부위
   źródło: Enemies.json :: dataList[id=870502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [[podstawowe] Wróg / część [870503] — nazwa] 사람
   źródło: Enemies.json :: dataList[id=870503].name
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [[podstawowe] Wróg / część [870503] — opis] 부위
   źródło: Enemies.json :: dataList[id=870503].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [[podstawowe] Wróg / część [870504] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=870504].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [[podstawowe] Wróg / część [870504] — opis] 부위
   źródło: Enemies.json :: dataList[id=870504].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [[podstawowe] Wróg / część [8706] — nazwa] 나 강해졌나? 정말?
   źródło: Enemies.json :: dataList[id=8706].name
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [[podstawowe] Wróg / część [8706] — opis] 본체
   źródło: Enemies.json :: dataList[id=8706].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [[podstawowe] Wróg / część [870601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [[podstawowe] Wróg / część [870601] — opis] 부위
   źródło: Enemies.json :: dataList[id=870601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [[podstawowe] Wróg / część [8707] — nazwa] 나 세졌어! 진짜?
   źródło: Enemies.json :: dataList[id=8707].name
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [[podstawowe] Wróg / część [8707] — opis] 본체
   źródło: Enemies.json :: dataList[id=8707].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [[podstawowe] Wróg / część [870701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [[podstawowe] Wróg / część [870701] — opis] 부위
   źródło: Enemies.json :: dataList[id=870701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [[podstawowe] Wróg / część [8708] — nazwa] 너 맞아볼래? 매우?
   źródło: Enemies.json :: dataList[id=8708].name
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [[podstawowe] Wróg / część [8708] — opis] 본체
   źródło: Enemies.json :: dataList[id=8708].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [[podstawowe] Wróg / część [870801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [[podstawowe] Wróg / część [870801] — opis] 부위
   źródło: Enemies.json :: dataList[id=870801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [[podstawowe] Wróg / część [870802] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=870802].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [[podstawowe] Wróg / część [870802] — opis] 부위
   źródło: Enemies.json :: dataList[id=870802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [[podstawowe] Wróg / część [8709] — nazwa] 매혹하는 분홍신
   źródło: Enemies.json :: dataList[id=8709].name
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [[podstawowe] Wróg / część [8709] — opis] 본체
   źródło: Enemies.json :: dataList[id=8709].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [[podstawowe] Wróg / część [870901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=870901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [[podstawowe] Wróg / część [870901] — opis] 부위
   źródło: Enemies.json :: dataList[id=870901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [[podstawowe] Wróg / część [8710] — nazwa] 홀리는 분홍신
   źródło: Enemies.json :: dataList[id=8710].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [[podstawowe] Wróg / część [8710] — opis] 본체
   źródło: Enemies.json :: dataList[id=8710].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [[podstawowe] Wróg / część [871001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=871001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [[podstawowe] Wróg / część [871001] — opis] 부위
   źródło: Enemies.json :: dataList[id=871001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [[podstawowe] Wróg / część [8711] — nazwa] 또각또각? 걸어!
   źródło: Enemies.json :: dataList[id=8711].name
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
873. [[podstawowe] Wróg / część [8711] — opis] 본체
   źródło: Enemies.json :: dataList[id=8711].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [[podstawowe] Wróg / część [871101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=871101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [[podstawowe] Wróg / część [871101] — opis] 부위
   źródło: Enemies.json :: dataList[id=871101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [[podstawowe] Wróg / część [871102] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=871102].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [[podstawowe] Wróg / część [871102] — opis] 부위
   źródło: Enemies.json :: dataList[id=871102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [[podstawowe] Wróg / część [8712] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=8712].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [[podstawowe] Wróg / część [8712] — opis] 본체
   źródło: Enemies.json :: dataList[id=8712].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [[podstawowe] Wróg / część [871201] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=871201].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [[podstawowe] Wróg / część [871201] — opis] 부위
   źródło: Enemies.json :: dataList[id=871201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [[podstawowe] Wróg / część [871202] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=871202].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [[podstawowe] Wróg / część [871202] — opis] 부위
   źródło: Enemies.json :: dataList[id=871202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [[podstawowe] Wróg / część [871203] — nazwa] 얼굴
   źródło: Enemies.json :: dataList[id=871203].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [[podstawowe] Wróg / część [871203] — opis] 부위
   źródło: Enemies.json :: dataList[id=871203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [[podstawowe] Wróg / część [87122] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87122].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [[podstawowe] Wróg / część [87122] — opis] 본체
   źródło: Enemies.json :: dataList[id=87122].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [[podstawowe] Wróg / część [87123] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87123].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [[podstawowe] Wróg / część [87123] — opis] 본체
   źródło: Enemies.json :: dataList[id=87123].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [[podstawowe] Wróg / część [87124] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87124].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [[podstawowe] Wróg / część [87124] — opis] 본체
   źródło: Enemies.json :: dataList[id=87124].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [[podstawowe] Wróg / część [8713] — nazwa] 종말 토우
   źródło: Enemies.json :: dataList[id=8713].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [[podstawowe] Wróg / część [8713] — opis] 본체
   źródło: Enemies.json :: dataList[id=8713].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [[podstawowe] Wróg / część [871301] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=871301].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [[podstawowe] Wróg / część [871301] — opis] 부위
   źródło: Enemies.json :: dataList[id=871301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [[podstawowe] Wróg / część [8714] — nazwa] 불타는 종말 토우
   źródło: Enemies.json :: dataList[id=8714].name
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [[podstawowe] Wróg / część [8714] — opis] 본체
   źródło: Enemies.json :: dataList[id=8714].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [[podstawowe] Wróg / część [871401] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=871401].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [[podstawowe] Wróg / część [871401] — opis] 부위
   źródło: Enemies.json :: dataList[id=871401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [[podstawowe] Wróg / część [8721] — nazwa] 흑단여왕의 사과
   źródło: Enemies.json :: dataList[id=8721].name
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [[podstawowe] Wróg / część [8721] — opis] 본체
   źródło: Enemies.json :: dataList[id=8721].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [[podstawowe] Wróg / część [872101] — nazwa] 열매
   źródło: Enemies.json :: dataList[id=872101].name
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [[podstawowe] Wróg / część [872101] — opis] 부위
   źródło: Enemies.json :: dataList[id=872101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [[podstawowe] Wróg / część [872102] — nazwa] 왼쪽 줄기
   źródło: Enemies.json :: dataList[id=872102].name
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [[podstawowe] Wróg / część [872102] — opis] 부위
   źródło: Enemies.json :: dataList[id=872102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [[podstawowe] Wróg / część [872103] — nazwa] 오른쪽 줄기
   źródło: Enemies.json :: dataList[id=872103].name
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [[podstawowe] Wróg / część [872103] — opis] 부위
   źródło: Enemies.json :: dataList[id=872103].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [[podstawowe] Wróg / część [872104] — nazwa] 뿌리
   źródło: Enemies.json :: dataList[id=872104].name
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [[podstawowe] Wróg / część [872104] — opis] 부위
   źródło: Enemies.json :: dataList[id=872104].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [[podstawowe] Wróg / część [8722] — nazwa] 단수어
   źródło: Enemies.json :: dataList[id=8722].name
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [[podstawowe] Wróg / część [8722] — opis] 본체
   źródło: Enemies.json :: dataList[id=8722].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [[podstawowe] Wróg / część [872201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [[podstawowe] Wróg / część [872201] — opis] 부위
   źródło: Enemies.json :: dataList[id=872201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [[podstawowe] Wróg / część [872202] — nazwa] 오른다리
   źródło: Enemies.json :: dataList[id=872202].name
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
915. [[podstawowe] Wróg / część [872202] — opis] 부위
   źródło: Enemies.json :: dataList[id=872202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [[podstawowe] Wróg / część [872203] — nazwa] 왼다리
   źródło: Enemies.json :: dataList[id=872203].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [[podstawowe] Wróg / część [872203] — opis] 부위
   źródło: Enemies.json :: dataList[id=872203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [[podstawowe] Wróg / część [872204] — nazwa] 꼬리
   źródło: Enemies.json :: dataList[id=872204].name
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [[podstawowe] Wróg / część [872204] — opis] 부위
   źródło: Enemies.json :: dataList[id=872204].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [[podstawowe] Wróg / część [8723] — nazwa] 황금빛의 사과
   źródło: Enemies.json :: dataList[id=8723].name
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [[podstawowe] Wróg / część [8723] — opis] 본체
   źródło: Enemies.json :: dataList[id=8723].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [[podstawowe] Wróg / część [872301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [[podstawowe] Wróg / część [872301] — opis] 부위
   źródło: Enemies.json :: dataList[id=872301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [[podstawowe] Wróg / część [8724] — nazwa] 거짓 사과
   źródło: Enemies.json :: dataList[id=8724].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [[podstawowe] Wróg / część [8724] — opis] 본체
   źródło: Enemies.json :: dataList[id=8724].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [[podstawowe] Wróg / część [872401] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=872401].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [[podstawowe] Wróg / część [872401] — opis] 부위
   źródło: Enemies.json :: dataList[id=872401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [[podstawowe] Wróg / część [872402] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872402].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [[podstawowe] Wróg / część [872402] — opis] 부위
   źródło: Enemies.json :: dataList[id=872402].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [[podstawowe] Wróg / część [872403] — nazwa] 다리
   źródło: Enemies.json :: dataList[id=872403].name
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [[podstawowe] Wróg / część [872403] — opis] 부위
   źródło: Enemies.json :: dataList[id=872403].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [[podstawowe] Wróg / część [8725] — nazwa] 골목파수견
   źródło: Enemies.json :: dataList[id=8725].name
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [[podstawowe] Wróg / część [8725] — opis] 본체
   źródło: Enemies.json :: dataList[id=8725].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [[podstawowe] Wróg / część [872501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
935. [[podstawowe] Wróg / część [872501] — opis] 부위
   źródło: Enemies.json :: dataList[id=872501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
936. [[podstawowe] Wróg / część [872502] — nazwa] 전봇대
   źródło: Enemies.json :: dataList[id=872502].name
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [[podstawowe] Wróg / część [872502] — opis] 부위
   źródło: Enemies.json :: dataList[id=872502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [[podstawowe] Wróg / część [872503] — nazwa] 사람
   źródło: Enemies.json :: dataList[id=872503].name
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [[podstawowe] Wróg / część [872503] — opis] 부위
   źródło: Enemies.json :: dataList[id=872503].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [[podstawowe] Wróg / część [872504] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=872504].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [[podstawowe] Wróg / część [872504] — opis] 부위
   źródło: Enemies.json :: dataList[id=872504].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [[podstawowe] Wróg / część [8726] — nazwa] 나 강해졌나? 정말?
   źródło: Enemies.json :: dataList[id=8726].name
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [[podstawowe] Wróg / część [8726] — opis] 본체
   źródło: Enemies.json :: dataList[id=8726].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [[podstawowe] Wróg / część [872601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [[podstawowe] Wróg / część [872601] — opis] 부위
   źródło: Enemies.json :: dataList[id=872601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [[podstawowe] Wróg / część [8727] — nazwa] 나 세졌어! 진짜?
   źródło: Enemies.json :: dataList[id=8727].name
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [[podstawowe] Wróg / część [8727] — opis] 본체
   źródło: Enemies.json :: dataList[id=8727].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [[podstawowe] Wróg / część [872701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [[podstawowe] Wróg / część [872701] — opis] 부위
   źródło: Enemies.json :: dataList[id=872701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
950. [[podstawowe] Wróg / część [8728] — nazwa] 너 맞아볼래? 매우?
   źródło: Enemies.json :: dataList[id=8728].name
   (powtórzenie elementu 506 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
951. [[podstawowe] Wróg / część [8728] — opis] 본체
   źródło: Enemies.json :: dataList[id=8728].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [[podstawowe] Wróg / część [872801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [[podstawowe] Wróg / część [872801] — opis] 부위
   źródło: Enemies.json :: dataList[id=872801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
954. [[podstawowe] Wróg / część [872802] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=872802].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [[podstawowe] Wróg / część [872802] — opis] 부위
   źródło: Enemies.json :: dataList[id=872802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [[podstawowe] Wróg / część [8729] — nazwa] 매혹하는 분홍신
   źródło: Enemies.json :: dataList[id=8729].name
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [[podstawowe] Wróg / część [8729] — opis] 본체
   źródło: Enemies.json :: dataList[id=8729].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [[podstawowe] Wróg / część [872901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=872901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [[podstawowe] Wróg / część [872901] — opis] 부위
   źródło: Enemies.json :: dataList[id=872901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [[podstawowe] Wróg / część [8730] — nazwa] 홀리는 분홍신
   źródło: Enemies.json :: dataList[id=8730].name
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [[podstawowe] Wróg / część [8730] — opis] 본체
   źródło: Enemies.json :: dataList[id=8730].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [[podstawowe] Wróg / część [873001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=873001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [[podstawowe] Wróg / część [873001] — opis] 부위
   źródło: Enemies.json :: dataList[id=873001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [[podstawowe] Wróg / część [8731] — nazwa] 또각또각? 걸어!
   źródło: Enemies.json :: dataList[id=8731].name
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [[podstawowe] Wróg / część [8731] — opis] 본체
   źródło: Enemies.json :: dataList[id=8731].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [[podstawowe] Wróg / część [873101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=873101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [[podstawowe] Wróg / część [873101] — opis] 부위
   źródło: Enemies.json :: dataList[id=873101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [[podstawowe] Wróg / część [873102] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=873102].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [[podstawowe] Wróg / część [873102] — opis] 부위
   źródło: Enemies.json :: dataList[id=873102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [[podstawowe] Wróg / część [8732] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=8732].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [[podstawowe] Wróg / część [8732] — opis] 본체
   źródło: Enemies.json :: dataList[id=8732].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [[podstawowe] Wróg / część [873201] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=873201].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [[podstawowe] Wróg / część [873201] — opis] 부위
   źródło: Enemies.json :: dataList[id=873201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [[podstawowe] Wróg / część [873202] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=873202].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [[podstawowe] Wróg / część [873202] — opis] 부위
   źródło: Enemies.json :: dataList[id=873202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [[podstawowe] Wróg / część [873203] — nazwa] 얼굴
   źródło: Enemies.json :: dataList[id=873203].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [[podstawowe] Wróg / część [873203] — opis] 부위
   źródło: Enemies.json :: dataList[id=873203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [[podstawowe] Wróg / część [87322] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87322].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [[podstawowe] Wróg / część [87322] — opis] 본체
   źródło: Enemies.json :: dataList[id=87322].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [[podstawowe] Wróg / część [87323] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87323].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [[podstawowe] Wróg / część [87323] — opis] 본체
   źródło: Enemies.json :: dataList[id=87323].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
982. [[podstawowe] Wróg / część [87324] — nazwa] 종말 달력
   źródło: Enemies.json :: dataList[id=87324].name
   (powtórzenie elementu 486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [[podstawowe] Wróg / część [87324] — opis] 본체
   źródło: Enemies.json :: dataList[id=87324].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [[podstawowe] Wróg / część [8733] — nazwa] 종말 토우
   źródło: Enemies.json :: dataList[id=8733].name
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
985. [[podstawowe] Wróg / część [8733] — opis] 본체
   źródło: Enemies.json :: dataList[id=8733].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [[podstawowe] Wróg / część [873301] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=873301].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [[podstawowe] Wróg / część [873301] — opis] 부위
   źródło: Enemies.json :: dataList[id=873301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [[podstawowe] Wróg / część [8734] — nazwa] 불타는 종말 토우
   źródło: Enemies.json :: dataList[id=8734].name
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [[podstawowe] Wróg / część [8734] — opis] 본체
   źródło: Enemies.json :: dataList[id=8734].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [[podstawowe] Wróg / część [873401] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=873401].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [[podstawowe] Wróg / część [873401] — opis] 부위
   źródło: Enemies.json :: dataList[id=873401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
992. [[podstawowe] Wróg / część [90042] — nazwa] 혼란스런 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90042].name
   limit: do 50 znaków
   EN: Confused K Corp. Checkpoint Security
   PL: Confused K Corp. Checkpoint Security
993. [[podstawowe] Wróg / część [90042] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90042].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [[podstawowe] Wróg / część [90043] — nazwa] 정신없는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90043].name
   limit: do 50 znaków
   EN: Swamped K Corp. Checkpoint Security
   PL: Swamped K Corp. Checkpoint Security
995. [[podstawowe] Wróg / część [90043] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90043].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [[podstawowe] Wróg / część [90044] — nazwa] 어지러운 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90044].name
   limit: do 50 znaków
   EN: Hazed K Corp. Checkpoint Security
   PL: Hazed K Corp. Checkpoint Security
997. [[podstawowe] Wróg / część [90044] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90044].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [[podstawowe] Wróg / część [90045] — nazwa] 앞이 캄캄한 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90045].name
   limit: do 50 znaków
   EN: Stunned K Corp. Checkpoint Security
   PL: Stunned K Corp. Checkpoint Security
999. [[podstawowe] Wróg / część [90045] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90045].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1000. [[podstawowe] Wróg / część [8034] — nazwa] 닭도리 - a.k.a 봉이
   źródło: Enemies.json :: dataList[id=8034].name
   limit: do 40 znaków
   EN: Headchicken a.k.a. Bongy
   PL: Headchicken a.k.a. Bongy
1001. [[podstawowe] Wróg / część [8034] — opis] 본체
   źródło: Enemies.json :: dataList[id=8034].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [[podstawowe] Wróg / część [803401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1003. [[podstawowe] Wróg / część [803401] — opis] 부위
   źródło: Enemies.json :: dataList[id=803401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [[podstawowe] Wróg / część [8035] — nazwa] 닭도리 - a.k.a 봉이
   źródło: Enemies.json :: dataList[id=8035].name
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [[podstawowe] Wróg / część [8035] — opis] 본체
   źródło: Enemies.json :: dataList[id=8035].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1006. [[podstawowe] Wróg / część [803501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1007. [[podstawowe] Wróg / część [803501] — opis] 부위
   źródło: Enemies.json :: dataList[id=803501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1008. [[podstawowe] Wróg / część [8036] — nazwa] 닭도리 - a.k.a 봉이
   źródło: Enemies.json :: dataList[id=8036].name
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1009. [[podstawowe] Wróg / część [8036] — opis] 본체
   źródło: Enemies.json :: dataList[id=8036].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [[podstawowe] Wróg / część [803601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1011. [[podstawowe] Wróg / część [803601] — opis] 부위
   źródło: Enemies.json :: dataList[id=803601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [[podstawowe] Wróg / część [8037] — nazwa] 닭도리 - a.k.a 봉이
   źródło: Enemies.json :: dataList[id=8037].name
   (powtórzenie elementu 1000 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [[podstawowe] Wróg / część [8037] — opis] 본체
   źródło: Enemies.json :: dataList[id=8037].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1014. [[podstawowe] Wróg / część [803701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1015. [[podstawowe] Wróg / część [803701] — opis] 부위
   źródło: Enemies.json :: dataList[id=803701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [[podstawowe] Wróg / część [8038] — nazwa] 봉이 아빠
   źródło: Enemies.json :: dataList[id=8038].name
   limit: do 40 znaków
   EN: Papa Bongy
   PL: Papa Bongy
1017. [[podstawowe] Wróg / część [8038] — opis] 본체
   źródło: Enemies.json :: dataList[id=8038].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1018. [[podstawowe] Wróg / część [803801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [[podstawowe] Wróg / część [803801] — opis] 부위
   źródło: Enemies.json :: dataList[id=803801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [[podstawowe] Wróg / część [8039] — nazwa] 봉이 아빠
   źródło: Enemies.json :: dataList[id=8039].name
   (powtórzenie elementu 1016 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1021. [[podstawowe] Wróg / część [8039] — opis] 본체
   źródło: Enemies.json :: dataList[id=8039].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1022. [[podstawowe] Wróg / część [803901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=803901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [[podstawowe] Wróg / część [803901] — opis] 부위
   źródło: Enemies.json :: dataList[id=803901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [[podstawowe] Wróg / część [803902] — nazwa] 닭통
   źródło: Enemies.json :: dataList[id=803902].name
   limit: do 40 znaków
   EN: Chicken Bucket
   PL: Chicken Bucket
1025. [[podstawowe] Wróg / część [803902] — opis] 부위
   źródło: Enemies.json :: dataList[id=803902].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1026. [[podstawowe] Wróg / część [8040] — nazwa] 매워진 봉이 아빠
   źródło: Enemies.json :: dataList[id=8040].name
   limit: do 40 znaków
   EN: Spiced-up Papa Bongy
   PL: Spiced-up Papa Bongy
1027. [[podstawowe] Wróg / część [8040] — opis] 본체
   źródło: Enemies.json :: dataList[id=8040].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [[podstawowe] Wróg / część [804001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1029. [[podstawowe] Wróg / część [804001] — opis] 부위
   źródło: Enemies.json :: dataList[id=804001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1030. [[podstawowe] Wróg / część [804002] — nazwa] 닭통
   źródło: Enemies.json :: dataList[id=804002].name
   (powtórzenie elementu 1024 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1031. [[podstawowe] Wróg / część [804002] — opis] 부위
   źródło: Enemies.json :: dataList[id=804002].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [[podstawowe] Wróg / część [8041] — nazwa] 놋쇠 황소 - 눈물 흘리는
   źródło: Enemies.json :: dataList[id=8041].name
   limit: do 40 znaków
   EN: Brazen Bull - Tearful
   PL: Brazen Bull - Tearful
1033. [[podstawowe] Wróg / część [8041] — opis] 본체
   źródło: Enemies.json :: dataList[id=8041].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1034. [[podstawowe] Wróg / część [804101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [[podstawowe] Wróg / część [804101] — opis] 부위
   źródło: Enemies.json :: dataList[id=804101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1036. [[podstawowe] Wróg / część [804102] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=804102].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [[podstawowe] Wróg / część [804102] — opis] 부위
   źródło: Enemies.json :: dataList[id=804102].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1038. [[podstawowe] Wróg / część [8042] — nazwa] K사 촬영 드론
   źródło: Enemies.json :: dataList[id=8042].name
   limit: do 40 znaków
   EN: K Corp. Filming Drone
   PL: K Corp. Filming Drone
1039. [[podstawowe] Wróg / część [8042] — opis] 본체
   źródło: Enemies.json :: dataList[id=8042].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1040. [[podstawowe] Wróg / część [804201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [[podstawowe] Wróg / część [804201] — opis] 부위
   źródło: Enemies.json :: dataList[id=804201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [[podstawowe] Wróg / część [8043] — nazwa] 로보토미 E.G.O::여우비 - 동백
   źródło: Enemies.json :: dataList[id=8043].name
   limit: do 50 znaków
   EN: Lobotomy E.G.O::Sunshower - Dongbaek
   PL: Lobotomy E.G.O::Sunshower - Dongbaek
1043. [[podstawowe] Wróg / część [8043] — opis] 본체
   źródło: Enemies.json :: dataList[id=8043].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [[podstawowe] Wróg / część [804301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1045. [[podstawowe] Wróg / część [804301] — opis] 부위
   źródło: Enemies.json :: dataList[id=804301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1046. [[podstawowe] Wróg / część [8044] — nazwa] 동백 E.G.O::동백
   źródło: Enemies.json :: dataList[id=8044].name
   limit: do 40 znaków
   EN: Dongbaek E.G.O::Spicebush
   PL: Dongbaek E.G.O::Spicebush
1047. [[podstawowe] Wróg / część [8044] — opis] 본체
   źródło: Enemies.json :: dataList[id=8044].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1048. [[podstawowe] Wróg / część [804401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [[podstawowe] Wróg / część [804401] — opis] 부위
   źródło: Enemies.json :: dataList[id=804401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1050. [[podstawowe] Wróg / część [8045] — nazwa] 충격지네
   źródło: Enemies.json :: dataList[id=8045].name
   limit: do 40 znaków
   EN: Shock Centipede
   PL: Shock Centipede
1051. [[podstawowe] Wróg / część [8045] — opis] 본체
   źródło: Enemies.json :: dataList[id=8045].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1052. [[podstawowe] Wróg / część [804501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [[podstawowe] Wróg / część [804501] — opis] 부위
   źródło: Enemies.json :: dataList[id=804501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [[podstawowe] Wróg / część [804502] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=804502].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [[podstawowe] Wróg / część [804502] — opis] 부위
   źródło: Enemies.json :: dataList[id=804502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1056. [[podstawowe] Wróg / część [8046] — nazwa] 떠돌이 여우
   źródło: Enemies.json :: dataList[id=8046].name
   limit: do 40 znaków
   EN: Drifting Fox
   PL: Drifting Fox
1057. [[podstawowe] Wróg / część [8046] — opis] 본체
   źródło: Enemies.json :: dataList[id=8046].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1058. [[podstawowe] Wróg / część [804601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1059. [[podstawowe] Wróg / część [804601] — opis] 부위
   źródło: Enemies.json :: dataList[id=804601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1060. [[podstawowe] Wróg / część [804602] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=804602].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1061. [[podstawowe] Wróg / część [804602] — opis] 부위
   źródło: Enemies.json :: dataList[id=804602].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1062. [[podstawowe] Wróg / część [8047] — nazwa] 누구도 울지 않도록
   źródło: Enemies.json :: dataList[id=8047].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL: So That No One Will Cry
1063. [[podstawowe] Wróg / część [8047] — opis] 본체
   źródło: Enemies.json :: dataList[id=8047].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1064. [[podstawowe] Wróg / część [804701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1065. [[podstawowe] Wróg / część [804701] — opis] 부위
   źródło: Enemies.json :: dataList[id=804701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [[podstawowe] Wróg / część [804702] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=804702].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1067. [[podstawowe] Wróg / część [804702] — opis] 부위
   źródło: Enemies.json :: dataList[id=804702].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1068. [[podstawowe] Wróg / część [8048] — nazwa] 신사 요정
   źródło: Enemies.json :: dataList[id=8048].name
   limit: do 40 znaków
   EN: Fairy Gentleman
   PL: Fairy Gentleman
1069. [[podstawowe] Wróg / część [8048] — opis] 본체
   źródło: Enemies.json :: dataList[id=8048].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1070. [[podstawowe] Wróg / część [804801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1071. [[podstawowe] Wróg / część [804801] — opis] 부위
   źródło: Enemies.json :: dataList[id=804801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1072. [[podstawowe] Wróg / część [804802] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=804802].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [[podstawowe] Wróg / część [804802] — opis] 부위
   źródło: Enemies.json :: dataList[id=804802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1074. [[podstawowe] Wróg / część [8049] — nazwa] 모든 것을 부정하는 동랑
   źródło: Enemies.json :: dataList[id=8049].name
   limit: do 40 znaków
   EN: Dongrang, Who Denies All
   PL: Dongrang, Who Denies All
1075. [[podstawowe] Wróg / część [8049] — opis] 본체
   źródło: Enemies.json :: dataList[id=8049].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1076. [[podstawowe] Wróg / część [8050] — nazwa] 개화 E.G.O::마름
   źródło: Enemies.json :: dataList[id=8050].name
   limit: do 40 znaków
   EN: Effloresced E.G.O::Farmwatch
   PL: Effloresced E.G.O::Farmwatch
1077. [[podstawowe] Wróg / część [8050] — opis] 본체
   źródło: Enemies.json :: dataList[id=8050].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1078. [[podstawowe] Wróg / część [8051] — nazwa] 요정주
   źródło: Enemies.json :: dataList[id=8051].name
   limit: do 40 znaków
   EN: Fairy Wine
   PL: Fairy Wine
1079. [[podstawowe] Wróg / część [8051] — opis] 본체
   źródło: Enemies.json :: dataList[id=8051].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1080. [[podstawowe] Wróg / część [805101] — nazwa] 술통
   źródło: Enemies.json :: dataList[id=805101].name
   limit: do 40 znaków
   EN: Wine Barrel
   PL: Wine Barrel
1081. [[podstawowe] Wróg / część [805101] — opis] 부위
   źródło: Enemies.json :: dataList[id=805101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1082. [[podstawowe] Wróg / część [8052] — nazwa] 낡은 우산
   źródło: Enemies.json :: dataList[id=8052].name
   limit: do 40 znaków
   EN: Old Umbrella
   PL: Old Umbrella
1083. [[podstawowe] Wróg / część [8052] — opis] 본체
   źródło: Enemies.json :: dataList[id=8052].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1084. [[podstawowe] Wróg / część [805201] — nazwa] 우산
   źródło: Enemies.json :: dataList[id=805201].name
   limit: do 40 znaków
   EN: Umbrella
   PL: Umbrella
1085. [[podstawowe] Wróg / część [805201] — opis] 부위
   źródło: Enemies.json :: dataList[id=805201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [[podstawowe] Wróg / część [8053] — nazwa] 낡은 우산
   źródło: Enemies.json :: dataList[id=8053].name
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1087. [[podstawowe] Wróg / część [8053] — opis] 본체
   źródło: Enemies.json :: dataList[id=8053].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1088. [[podstawowe] Wróg / część [805301] — nazwa] 우산
   źródło: Enemies.json :: dataList[id=805301].name
   (powtórzenie elementu 1084 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [[podstawowe] Wróg / część [805301] — opis] 부위
   źródło: Enemies.json :: dataList[id=805301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1090. [[podstawowe] Wróg / część [8054] — nazwa] 곧 피어날 꽃
   źródło: Enemies.json :: dataList[id=8054].name
   limit: do 40 znaków
   EN: Soon-to-bloom Flower
   PL: Soon-to-bloom Flower
1091. [[podstawowe] Wróg / część [8054] — opis] 본체
   źródło: Enemies.json :: dataList[id=8054].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1092. [[podstawowe] Wróg / część [805401] — nazwa] 봉우리
   źródło: Enemies.json :: dataList[id=805401].name
   limit: do 40 znaków
   EN: Bud
   PL: Bud
1093. [[podstawowe] Wróg / część [805401] — opis] 부위
   źródło: Enemies.json :: dataList[id=805401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1094. [[podstawowe] Wróg / część [90046] — nazwa] K사 촬영 드론
   źródło: Enemies.json :: dataList[id=90046].name
   (powtórzenie elementu 1038 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [[podstawowe] Wróg / część [90046] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90046].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1096. [[podstawowe] Wróg / część [90047] — nazwa] 조잡한 톱니 기계 로봇
   źródło: Enemies.json :: dataList[id=90047].name
   limit: do 40 znaków
   EN: Crude Sawblade Bot
   PL: Crude Sawblade Bot
1097. [[podstawowe] Wróg / część [90047] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90047].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [[podstawowe] Wróg / część [90048] — nazwa] 조잡한 철공 기계 로봇
   źródło: Enemies.json :: dataList[id=90048].name
   limit: do 40 znaków
   EN: Crude Wrecking Ball Bot
   PL: Crude Wrecking Ball Bot
1099. [[podstawowe] Wróg / część [90048] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90048].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1100. [[podstawowe] Wróg / część [90049] — nazwa] 완성된 톱니 기계 로봇
   źródło: Enemies.json :: dataList[id=90049].name
   limit: do 40 znaków
   EN: Complete Sawblade Bot
   PL: Complete Sawblade Bot
1101. [[podstawowe] Wróg / część [90049] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90049].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1102. [[podstawowe] Wróg / część [90050] — nazwa] 완성된 철공 기계 로봇
   źródło: Enemies.json :: dataList[id=90050].name
   limit: do 40 znaków
   EN: Complete Wrecking Ball Bot
   PL: Complete Wrecking Ball Bot
1103. [[podstawowe] Wróg / część [90050] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90050].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [[podstawowe] Wróg / część [91007] — nazwa] 단단한 복합 기계 로봇
   źródło: Enemies.json :: dataList[id=91007].name
   limit: do 40 znaków
   EN: Solid Combined Bot
   PL: Solid Combined Bot
1105. [[podstawowe] Wróg / część [91007] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91007].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1106. [[podstawowe] Wróg / część [90051] — nazwa] 자신있는 장미스패너 공방 해결사
   źródło: Enemies.json :: dataList[id=90051].name
   limit: do 50 znaków
   EN: Confident Rosespanner Workshop Fixer
   PL: Confident Rosespanner Workshop Fixer
1107. [[podstawowe] Wróg / część [90051] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90051].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1108. [[podstawowe] Wróg / część [90052] — nazwa] 당당한 장미스패너 공방 해결사
   źródło: Enemies.json :: dataList[id=90052].name
   limit: do 50 znaków
   EN: Prideful Rosespanner Workshop Fixer
   PL: Prideful Rosespanner Workshop Fixer
1109. [[podstawowe] Wróg / część [90052] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90052].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1110. [[podstawowe] Wróg / część [90053] — nazwa] 떨고있는 장미스패너 공방 해결사
   źródło: Enemies.json :: dataList[id=90053].name
   limit: do 50 znaków
   EN: Shaking Rosespanner Workshop Fixer
   PL: Shaking Rosespanner Workshop Fixer
1111. [[podstawowe] Wróg / część [90053] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90053].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1112. [[podstawowe] Wróg / część [91008] — nazwa] 장미스패너 공방 대표 니코
   źródło: Enemies.json :: dataList[id=91008].name
   limit: do 50 znaków
   EN: Rosespanner Workshop Rep Niko
   PL: Rosespanner Workshop Rep Niko
1113. [[podstawowe] Wróg / część [91008] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91008].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1114. [[podstawowe] Wróg / część [90054] — nazwa] 위협받는 K사 1등급 직원
   źródło: Enemies.json :: dataList[id=90054].name
   limit: do 50 znaków
   EN: Threatened K Corp. Class 1 Staff
   PL: Threatened K Corp. Class 1 Staff
1115. [[podstawowe] Wróg / część [90054] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90054].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1116. [[podstawowe] Wróg / część [90055] — nazwa] 불안한 K사 1등급 직원
   źródło: Enemies.json :: dataList[id=90055].name
   limit: do 50 znaków
   EN: Unnerved K Corp. Class 1 Staff
   PL: Unnerved K Corp. Class 1 Staff
1117. [[podstawowe] Wróg / część [90055] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90055].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1118. [[podstawowe] Wróg / część [90056] — nazwa] 해킹된 K사 재생 드론
   źródło: Enemies.json :: dataList[id=90056].name
   limit: do 40 znaków
   EN: Hacked K Corp. Regen Drone
   PL: Hacked K Corp. Regen Drone
1119. [[podstawowe] Wróg / część [90056] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90056].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1120. [[podstawowe] Wróg / część [90057] — nazwa] 해킹된 K사 재생 드론
   źródło: Enemies.json :: dataList[id=90057].name
   (powtórzenie elementu 1118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1121. [[podstawowe] Wróg / część [90057] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90057].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1122. [[podstawowe] Wróg / część [90058] — nazwa] 로보토미 E.G.O::출렁임
   źródło: Enemies.json :: dataList[id=90058].name
   limit: do 40 znaków
   EN: Lobotomy E.G.O::Sloshing
   PL: Lobotomy E.G.O::Sloshing
1123. [[podstawowe] Wróg / część [90058] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90058].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1124. [[podstawowe] Wróg / część [90059] — nazwa] 로보토미 E.G.O::홍적
   źródło: Enemies.json :: dataList[id=90059].name
   limit: do 40 znaków
   EN: Lobotomy E.G.O::Red Sheet
   PL: Lobotomy E.G.O::Red Sheet
1125. [[podstawowe] Wróg / część [90059] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90059].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1126. [[podstawowe] Wróg / część [90060] — nazwa] 로보토미 E.G.O::출렁임
   źródło: Enemies.json :: dataList[id=90060].name
   (powtórzenie elementu 1122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1127. [[podstawowe] Wróg / część [90060] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90060].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1128. [[podstawowe] Wróg / część [90061] — nazwa] 로보토미 E.G.O::홍적
   źródło: Enemies.json :: dataList[id=90061].name
   (powtórzenie elementu 1124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1129. [[podstawowe] Wróg / część [90061] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90061].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1130. [[podstawowe] Wróg / część [91009] — nazwa] 로보토미 E.G.O::홍적 - 마리르
   źródło: Enemies.json :: dataList[id=91009].name
   limit: do 50 znaków
   EN: Lobotomy E.G.O::Red Sheet - Marile
   PL: Lobotomy E.G.O::Red Sheet - Marile
1131. [[podstawowe] Wróg / część [91009] — opis] 적 보스
   źródło: Enemies.json :: dataList[id=91009].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1132. [[podstawowe] Wróg / część [90062] — nazwa] 되살아난 로보토미 E.G.O::출렁임
   źródło: Enemies.json :: dataList[id=90062].name
   limit: do 50 znaków
   EN: Reawakened Lobotomy E.G.O::Sloshing
   PL: Reawakened Lobotomy E.G.O::Sloshing
1133. [[podstawowe] Wróg / część [90062] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90062].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1134. [[podstawowe] Wróg / część [90063] — nazwa] 되살아난 로보토미 E.G.O::홍적
   źródło: Enemies.json :: dataList[id=90063].name
   limit: do 50 znaków
   EN: Reawakened Lobotomy E.G.O::Red Sheet
   PL: Reawakened Lobotomy E.G.O::Red Sheet
1135. [[podstawowe] Wróg / część [90063] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90063].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1136. [[podstawowe] Wróg / część [90064] — nazwa] 되살아난 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90064].name
   limit: do 40 znaków
   EN: Revived K Corp. Security
   PL: Revived K Corp. Security
1137. [[podstawowe] Wróg / część [90064] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90064].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1138. [[podstawowe] Wróg / część [90065] — nazwa] 되살아난 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90065].name
   (powtórzenie elementu 1136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1139. [[podstawowe] Wróg / część [90065] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90065].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1140. [[podstawowe] Wróg / część [90066] — nazwa] 되살아난 K사 1등급 직원
   źródło: Enemies.json :: dataList[id=90066].name
   limit: do 50 znaków
   EN: Revived K Corp. Class 1 Staff
   PL: Revived K Corp. Class 1 Staff
1141. [[podstawowe] Wróg / część [90066] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90066].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1142. [[podstawowe] Wróg / część [90067] — nazwa] 되살아난 K사 1등급 직원
   źródło: Enemies.json :: dataList[id=90067].name
   (powtórzenie elementu 1140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1143. [[podstawowe] Wróg / część [90067] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90067].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1144. [[podstawowe] Wróg / część [90068] — nazwa] 되살아난 K사 3등급 직원
   źródło: Enemies.json :: dataList[id=90068].name
   limit: do 50 znaków
   EN: Revived K Corp. Class 3 Staff
   PL: Revived K Corp. Class 3 Staff
1145. [[podstawowe] Wróg / część [90068] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90068].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1146. [[podstawowe] Wróg / część [90069] — nazwa] 되살아난 K사 3등급 직원 - 강화
   źródło: Enemies.json :: dataList[id=90069].name
   limit: do 60 znaków
   EN: Revived K Corp. Class 3 Empowered Staff
   PL: Revived K Corp. Class 3 Empowered Staff
1147. [[podstawowe] Wróg / część [90069] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90069].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1148. [[podstawowe] Wróg / część [90070] — nazwa] 심상속 T사 징수직 3등급 직원
   źródło: Enemies.json :: dataList[id=90070].name
   limit: do 50 znaków
   EN: Imagined T Corp. Class 3 Collector
   PL: Imagined T Corp. Class 3 Collector
1149. [[podstawowe] Wróg / część [90070] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90070].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1150. [[podstawowe] Wróg / część [91010] — nazwa] 되살아난 로보토미 E.G.O::홍적 - 마리르
   źródło: Enemies.json :: dataList[id=91010].name
   limit: do 70 znaków
   EN: Reawakened Lobotomy E.G.O::Red Sheet - Marile
   PL: Reawakened Lobotomy E.G.O::Red Sheet - Marile
1151. [[podstawowe] Wróg / część [91010] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=91010].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1152. [[podstawowe] Wróg / część [90071] — nazwa] K사 구속 드론
   źródło: Enemies.json :: dataList[id=90071].name
   limit: do 40 znaków
   EN: K Corp. Arrest Drone
   PL: K Corp. Arrest Drone
1153. [[podstawowe] Wróg / część [90071] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90071].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1154. [[podstawowe] Wróg / część [90072] — nazwa] K사 촬영 드론
   źródło: Enemies.json :: dataList[id=90072].name
   (powtórzenie elementu 1038 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1155. [[podstawowe] Wróg / część [90072] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90072].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1156. [[podstawowe] Wróg / część [90073] — nazwa] 두려워하는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90073].name
   limit: do 60 znaków
   EN: Terrified K Corp. Checkpoint Security
   PL: Terrified K Corp. Checkpoint Security
1157. [[podstawowe] Wróg / część [90073] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90073].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1158. [[podstawowe] Wróg / część [90074] — nazwa] 떨고있는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90074].name
   limit: do 50 znaków
   EN: Shaking K Corp. Checkpoint Security
   PL: Shaking K Corp. Checkpoint Security
1159. [[podstawowe] Wróg / część [90074] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90074].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1160. [[podstawowe] Wróg / część [90075] — nazwa] 굳어있는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90075].name
   limit: do 60 znaków
   EN: Stiffened K Corp. Checkpoint Security
   PL: Stiffened K Corp. Checkpoint Security
1161. [[podstawowe] Wróg / część [90075] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90075].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1162. [[podstawowe] Wróg / część [90076] — nazwa] 눈치보는 K사 검문소 요원
   źródło: Enemies.json :: dataList[id=90076].name
   limit: do 50 znaków
   EN: Timid K Corp. Checkpoint Security
   PL: Timid K Corp. Checkpoint Security
1163. [[podstawowe] Wróg / część [90076] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=90076].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1164. [[podstawowe] Wróg / część [8055] — nazwa] 만개한 꽃
   źródło: Enemies.json :: dataList[id=8055].name
   limit: do 40 znaków
   EN: Fully Bloomed Flower
   PL: Fully Bloomed Flower
1165. [[podstawowe] Wróg / część [8055] — opis] 본체
   źródło: Enemies.json :: dataList[id=8055].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1166. [[podstawowe] Wróg / część [805501] — nazwa] 봉우리
   źródło: Enemies.json :: dataList[id=805501].name
   (powtórzenie elementu 1092 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1167. [[podstawowe] Wróg / część [805501] — opis] 부위
   źródło: Enemies.json :: dataList[id=805501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1168. [[podstawowe] Wróg / część [80442] — nazwa] 동백 E.G.O::동백
   źródło: Enemies.json :: dataList[id=80442].name
   (powtórzenie elementu 1046 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1169. [[podstawowe] Wróg / część [80442] — opis] 본체
   źródło: Enemies.json :: dataList[id=80442].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1170. [[podstawowe] Wróg / część [8056] — nazwa] 허영의 나무
   źródło: Enemies.json :: dataList[id=8056].name
   limit: do 40 znaków
   EN: Tree of Vanity
   PL: Tree of Vanity
1171. [[podstawowe] Wróg / część [8056] — opis] 본체
   źródło: Enemies.json :: dataList[id=8056].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1172. [[podstawowe] Wróg / część [805601] — nazwa] 허영의 열매
   źródło: Enemies.json :: dataList[id=805601].name
   limit: do 40 znaków
   EN: Fruit of Vanity
   PL: Fruit of Vanity
1173. [[podstawowe] Wróg / część [805601] — opis] 부위
   źródło: Enemies.json :: dataList[id=805601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1174. [[podstawowe] Wróg / część [8057] — nazwa] 응어리가 맺힌 나무
   źródło: Enemies.json :: dataList[id=8057].name
   limit: do 40 znaków
   EN: Resentful Tree
   PL: Resentful Tree
1175. [[podstawowe] Wróg / część [8057] — opis] 본체
   źródło: Enemies.json :: dataList[id=8057].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1176. [[podstawowe] Wróg / część [805701] — nazwa] 응어리
   źródło: Enemies.json :: dataList[id=805701].name
   limit: do 40 znaków
   EN: Resentment
   PL: Resentment
1177. [[podstawowe] Wróg / część [805701] — opis] 부위
   źródło: Enemies.json :: dataList[id=805701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1178. [[podstawowe] Wróg / część [8060] — nazwa] 욕망의 나무
   źródło: Enemies.json :: dataList[id=8060].name
   limit: do 40 znaków
   EN: Tree of Desires
   PL: Tree of Desires
1179. [[podstawowe] Wróg / część [8060] — opis] 본체
   źródło: Enemies.json :: dataList[id=8060].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1180. [[podstawowe] Wróg / część [806001] — nazwa] 욕망
   źródło: Enemies.json :: dataList[id=806001].name
   limit: do 40 znaków
   EN: Desire
   PL: Desire
1181. [[podstawowe] Wróg / część [806001] — opis] 부위
   źródło: Enemies.json :: dataList[id=806001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1182. [[podstawowe] Wróg / część [804901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=804901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1183. [[podstawowe] Wróg / część [804901] — opis] 부위
   źródło: Enemies.json :: dataList[id=804901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1184. [[podstawowe] Wróg / część [8058] — nazwa] 요정초롱
   źródło: Enemies.json :: dataList[id=8058].name
   limit: do 40 znaków
   EN: Faelantern
   PL: Faelantern
1185. [[podstawowe] Wróg / część [8058] — opis] 본체
   źródło: Enemies.json :: dataList[id=8058].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1186. [[podstawowe] Wróg / część [805801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=805801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1187. [[podstawowe] Wróg / część [805801] — opis] 부위
   źródło: Enemies.json :: dataList[id=805801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1188. [[podstawowe] Wróg / część [80492] — nazwa] 모든 것을 부정하는 동랑
   źródło: Enemies.json :: dataList[id=80492].name
   (powtórzenie elementu 1074 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1189. [[podstawowe] Wróg / część [80492] — opis] 본체
   źródło: Enemies.json :: dataList[id=80492].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1190. [[podstawowe] Wróg / część [80493] — nazwa] 모든 것을 부정하는 동랑
   źródło: Enemies.json :: dataList[id=80493].name
   (powtórzenie elementu 1074 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1191. [[podstawowe] Wróg / część [80493] — opis] 본체
   źródło: Enemies.json :: dataList[id=80493].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1192. [[podstawowe] Wróg / część [8061] — nazwa] 흡수하는 나무
   źródło: Enemies.json :: dataList[id=8061].name
   limit: do 40 znaków
   EN: Absorbing Tree
   PL: Absorbing Tree
1193. [[podstawowe] Wróg / część [8061] — opis] 본체
   źródło: Enemies.json :: dataList[id=8061].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1194. [[podstawowe] Wróg / część [806101] — nazwa] 나무
   źródło: Enemies.json :: dataList[id=806101].name
   limit: do 40 znaków
   EN: Tree
   PL: Tree
1195. [[podstawowe] Wróg / część [806101] — opis] 부위
   źródło: Enemies.json :: dataList[id=806101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1196. [[podstawowe] Wróg / część [805001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=805001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1197. [[podstawowe] Wróg / część [805001] — opis] 부위
   źródło: Enemies.json :: dataList[id=805001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1198. [[podstawowe] Wróg / część [805802] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=805802].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1199. [[podstawowe] Wróg / część [805802] — opis] 부위
   źródło: Enemies.json :: dataList[id=805802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1200. [[podstawowe] Wróg / część [805803] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=805803].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1201. [[podstawowe] Wróg / część [805803] — opis] 부위
   źródło: Enemies.json :: dataList[id=805803].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1202. [[podstawowe] Wróg / część [8059] — nazwa] 키다리 요정
   źródło: Enemies.json :: dataList[id=8059].name
   limit: do 40 znaków
   EN: Fairy-Long-Legs
   PL: Fairy-Long-Legs
1203. [[podstawowe] Wróg / część [8059] — opis] 본체
   źródło: Enemies.json :: dataList[id=8059].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1204. [[podstawowe] Wróg / część [805901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=805901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1205. [[podstawowe] Wróg / część [805901] — opis] 부위
   źródło: Enemies.json :: dataList[id=805901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1206. [[podstawowe] Wróg / część [805902] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=805902].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1207. [[podstawowe] Wróg / część [805902] — opis] 부위
   źródło: Enemies.json :: dataList[id=805902].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1208. [[podstawowe] Wróg / część [8064] — nazwa] 탐식 죄종
   źródło: Enemies.json :: dataList[id=8064].name
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1209. [[podstawowe] Wróg / część [8064] — opis] 본체
   źródło: Enemies.json :: dataList[id=8064].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1210. [[podstawowe] Wróg / część [8065] — nazwa] 나태 죄종
   źródło: Enemies.json :: dataList[id=8065].name
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1211. [[podstawowe] Wróg / część [8065] — opis] 본체
   źródło: Enemies.json :: dataList[id=8065].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1212. [[podstawowe] Wróg / część [8066] — nazwa] 분노 죄종
   źródło: Enemies.json :: dataList[id=8066].name
   (powtórzenie elementu 484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1213. [[podstawowe] Wróg / część [8066] — opis] 본체
   źródło: Enemies.json :: dataList[id=8066].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1214. [[podstawowe] Wróg / część [8067] — nazwa] 우울 죄종
   źródło: Enemies.json :: dataList[id=8067].name
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1215. [[podstawowe] Wróg / część [8067] — opis] 본체
   źródło: Enemies.json :: dataList[id=8067].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1216. [[podstawowe] Wróg / część [8068] — nazwa] 색욕 죄종
   źródło: Enemies.json :: dataList[id=8068].name
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1217. [[podstawowe] Wróg / część [8068] — opis] 본체
   źródło: Enemies.json :: dataList[id=8068].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1218. [[podstawowe] Wróg / część [8069] — nazwa] 오만 죄종
   źródło: Enemies.json :: dataList[id=8069].name
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1219. [[podstawowe] Wróg / część [8069] — opis] 본체
   źródło: Enemies.json :: dataList[id=8069].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1220. [[podstawowe] Wróg / część [806401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1221. [[podstawowe] Wróg / część [806401] — opis] 부위
   źródło: Enemies.json :: dataList[id=806401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1222. [[podstawowe] Wróg / część [806501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1223. [[podstawowe] Wróg / część [806501] — opis] 부위
   źródło: Enemies.json :: dataList[id=806501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1224. [[podstawowe] Wróg / część [806601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1225. [[podstawowe] Wróg / część [806601] — opis] 부위
   źródło: Enemies.json :: dataList[id=806601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1226. [[podstawowe] Wróg / część [806701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1227. [[podstawowe] Wróg / część [806701] — opis] 부위
   źródło: Enemies.json :: dataList[id=806701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1228. [[podstawowe] Wróg / część [806801] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806801].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1229. [[podstawowe] Wróg / część [806801] — opis] 부위
   źródło: Enemies.json :: dataList[id=806801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1230. [[podstawowe] Wróg / część [806901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1231. [[podstawowe] Wróg / część [806901] — opis] 부위
   źródło: Enemies.json :: dataList[id=806901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1232. [[podstawowe] Wróg / część [805903] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=805903].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1233. [[podstawowe] Wróg / część [805903] — opis] 부위
   źródło: Enemies.json :: dataList[id=805903].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1234. [[podstawowe] Wróg / część [8062] — nazwa] 거대한 잎사귀
   źródło: Enemies.json :: dataList[id=8062].name
   limit: do 40 znaków
   EN: Giant Leaf
   PL: Giant Leaf
1235. [[podstawowe] Wróg / część [8062] — opis] 본체
   źródło: Enemies.json :: dataList[id=8062].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1236. [[podstawowe] Wróg / część [806201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=806201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1237. [[podstawowe] Wróg / część [806201] — opis] 부위
   źródło: Enemies.json :: dataList[id=806201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1238. [[podstawowe] Wróg / część [8075] — nazwa] 울음 두꺼비
   źródło: Enemies.json :: dataList[id=8075].name
   limit: do 40 znaków
   EN: Blubbering Toad
   PL: Blubbering Toad
1239. [[podstawowe] Wróg / część [8075] — opis] 본체
   źródło: Enemies.json :: dataList[id=8075].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1240. [[podstawowe] Wróg / część [807501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=807501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1241. [[podstawowe] Wróg / część [807501] — opis] 부위
   źródło: Enemies.json :: dataList[id=807501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1242. [[podstawowe] Wróg / część [807502] — nazwa] 왼쪽 눈
   źródło: Enemies.json :: dataList[id=807502].name
   limit: do 40 znaków
   EN: Left Eye
   PL: Left Eye
1243. [[podstawowe] Wróg / część [807502] — opis] 부위
   źródło: Enemies.json :: dataList[id=807502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1244. [[podstawowe] Wróg / część [807503] — nazwa] 오른쪽 눈
   źródło: Enemies.json :: dataList[id=807503].name
   limit: do 40 znaków
   EN: Right Eye
   PL: Right Eye
1245. [[podstawowe] Wróg / część [807503] — opis] 부위
   źródło: Enemies.json :: dataList[id=807503].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1246. [[podstawowe] Wróg / część [8076] — nazwa] kqe-1j-23
   źródło: Enemies.json :: dataList[id=8076].name
   limit: do 40 znaków
   EN: kqe-1j-23
   PL: kqe-1j-23
1247. [[podstawowe] Wróg / część [8076] — opis] 본체
   źródło: Enemies.json :: dataList[id=8076].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1248. [[podstawowe] Wróg / część [807601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=807601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1249. [[podstawowe] Wróg / część [807601] — opis] 부위
   źródło: Enemies.json :: dataList[id=807601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1250. [[podstawowe] Wróg / część [8077] — nazwa] 마을 주민의 심장
   źródło: Enemies.json :: dataList[id=8077].name
   limit: do 40 znaków
   EN: Heart of the Townsfolk
   PL: Heart of the Townsfolk
1251. [[podstawowe] Wróg / część [8077] — opis] 본체
   źródło: Enemies.json :: dataList[id=8077].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1252. [[podstawowe] Wróg / część [807701] — nazwa] 심장
   źródło: Enemies.json :: dataList[id=807701].name
   limit: do 40 znaków
   EN: Heart
   PL: Heart
1253. [[podstawowe] Wróg / część [807701] — opis] 부위
   źródło: Enemies.json :: dataList[id=807701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1254. [[podstawowe] Wróg / część [8078] — nazwa] 나는 비워내느니
   źródło: Enemies.json :: dataList[id=8078].name
   limit: do 40 znaków
   EN: My Form Empties
   PL: My Form Empties
1255. [[podstawowe] Wróg / część [8078] — opis] 본체
   źródło: Enemies.json :: dataList[id=8078].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1256. [[podstawowe] Wróg / część [807801] — nazwa] 불상
   źródło: Enemies.json :: dataList[id=807801].name
   limit: do 40 znaków
   EN: Buddha Mūrti
   PL: Buddha Mūrti
1257. [[podstawowe] Wróg / część [807801] — opis] 부위
   źródło: Enemies.json :: dataList[id=807801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1258. [[podstawowe] Wróg / część [807802] — nazwa] 석좌
   źródło: Enemies.json :: dataList[id=807802].name
   limit: do 40 znaków
   EN: Stone Seat
   PL: Stone Seat
1259. [[podstawowe] Wróg / część [807802] — opis] 부위
   źródło: Enemies.json :: dataList[id=807802].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1260. [[podstawowe] Wróg / część [8079] — nazwa] 이끌린 귀도
   źródło: Enemies.json :: dataList[id=8079].name
   limit: do 40 znaków
   EN: Lured Guido
   PL: Lured Guido
1261. [[podstawowe] Wróg / część [8079] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=8079].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1262. [[podstawowe] Wróg / część [807901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=807901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1263. [[podstawowe] Wróg / część [807901] — opis] 부위
   źródło: Enemies.json :: dataList[id=807901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1264. [[podstawowe] Wróg / część [8080] — nazwa] 이끌린 아이드
   źródło: Enemies.json :: dataList[id=8080].name
   limit: do 40 znaków
   EN: Lured Aida
   PL: Lured Aida
1265. [[podstawowe] Wróg / część [8080] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=8080].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1266. [[podstawowe] Wróg / część [808001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1267. [[podstawowe] Wróg / część [808001] — opis] 부위
   źródło: Enemies.json :: dataList[id=808001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1268. [[podstawowe] Wróg / część [8081] — nazwa] 이끌린 짓물린 G사 부장
   źródło: Enemies.json :: dataList[id=8081].name
   limit: do 50 znaków
   EN: Lured Festered G Corp. H. Manager
   PL: Lured Festered G Corp. H. Manager
1269. [[podstawowe] Wróg / część [8081] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=8081].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1270. [[podstawowe] Wróg / część [808101] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1271. [[podstawowe] Wróg / część [808101] — opis] 부위
   źródło: Enemies.json :: dataList[id=808101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1272. [[podstawowe] Wróg / część [8082] — nazwa] 크로머
   źródło: Enemies.json :: dataList[id=8082].name
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1273. [[podstawowe] Wróg / część [8082] — opis] 적 잡몹
   źródło: Enemies.json :: dataList[id=8082].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1274. [[podstawowe] Wróg / część [808201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1275. [[podstawowe] Wróg / część [808201] — opis] 부위
   źródło: Enemies.json :: dataList[id=808201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1276. [[podstawowe] Wróg / część [8083] — nazwa] 온전한 인간을 꿈꾸는 크로머
   źródło: Enemies.json :: dataList[id=8083].name
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1277. [[podstawowe] Wróg / część [8083] — opis] 본체
   źródło: Enemies.json :: dataList[id=8083].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1278. [[podstawowe] Wróg / część [808301] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=808301].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1279. [[podstawowe] Wróg / część [808301] — opis] 부위
   źródło: Enemies.json :: dataList[id=808301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1280. [[podstawowe] Wróg / część [808302] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=808302].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1281. [[podstawowe] Wróg / część [808302] — opis] 부위
   źródło: Enemies.json :: dataList[id=808302].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1282. [[podstawowe] Wróg / część [808303] — nazwa] 큰입
   źródło: Enemies.json :: dataList[id=808303].name
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1283. [[podstawowe] Wróg / część [808303] — opis] 부위
   źródło: Enemies.json :: dataList[id=808303].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1284. [[podstawowe] Wróg / część [90082] — nazwa] K사 3등급 적출직 직원
   źródło: Enemies.json :: dataList[id=90082].name
   limit: do 50 znaków
   EN: K Corp. Class 3 Excision Staff
   PL: K Corp. Class 3 Excision Staff
1285. [[podstawowe] Wróg / część [90082] — opis] 적
   źródło: Enemies.json :: dataList[id=90082].desc
   limit: do 120 znaków
   EN: Enemy Unit
   PL: Enemy Unit
1286. [[podstawowe] Wróg / część [8084] — nazwa] 단수어
   źródło: Enemies.json :: dataList[id=8084].name
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1287. [[podstawowe] Wróg / część [8084] — opis] 본체
   źródło: Enemies.json :: dataList[id=8084].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1288. [[podstawowe] Wróg / część [808401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1289. [[podstawowe] Wróg / część [808401] — opis] 부위
   źródło: Enemies.json :: dataList[id=808401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1290. [[podstawowe] Wróg / część [808402] — nazwa] 오른다리
   źródło: Enemies.json :: dataList[id=808402].name
   (powtórzenie elementu 634 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1291. [[podstawowe] Wróg / część [808402] — opis] 부위
   źródło: Enemies.json :: dataList[id=808402].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1292. [[podstawowe] Wróg / część [808403] — nazwa] 왼다리
   źródło: Enemies.json :: dataList[id=808403].name
   (powtórzenie elementu 636 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1293. [[podstawowe] Wróg / część [808403] — opis] 부위
   źródło: Enemies.json :: dataList[id=808403].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1294. [[podstawowe] Wróg / część [808404] — nazwa] 꼬리
   źródło: Enemies.json :: dataList[id=808404].name
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1295. [[podstawowe] Wróg / część [808404] — opis] 부위
   źródło: Enemies.json :: dataList[id=808404].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1296. [[podstawowe] Wróg / część [8085] — nazwa] 골목파수견
   źródło: Enemies.json :: dataList[id=8085].name
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1297. [[podstawowe] Wróg / część [8085] — opis] 본체
   źródło: Enemies.json :: dataList[id=8085].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1298. [[podstawowe] Wróg / część [808501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1299. [[podstawowe] Wróg / część [808501] — opis] 부위
   źródło: Enemies.json :: dataList[id=808501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1300. [[podstawowe] Wróg / część [808502] — nazwa] 전봇대
   źródło: Enemies.json :: dataList[id=808502].name
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1301. [[podstawowe] Wróg / część [808502] — opis] 부위
   źródło: Enemies.json :: dataList[id=808502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1302. [[podstawowe] Wróg / część [808503] — nazwa] 사람
   źródło: Enemies.json :: dataList[id=808503].name
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1303. [[podstawowe] Wróg / część [808503] — opis] 부위
   źródło: Enemies.json :: dataList[id=808503].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1304. [[podstawowe] Wróg / część [808504] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=808504].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1305. [[podstawowe] Wróg / część [808504] — opis] 부위
   źródło: Enemies.json :: dataList[id=808504].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1306. [[podstawowe] Wróg / część [8086] — nazwa] 충격지네
   źródło: Enemies.json :: dataList[id=8086].name
   (powtórzenie elementu 1050 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1307. [[podstawowe] Wróg / część [8086] — opis] 본체
   źródło: Enemies.json :: dataList[id=8086].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1308. [[podstawowe] Wróg / część [808601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1309. [[podstawowe] Wróg / część [808601] — opis] 부위
   źródło: Enemies.json :: dataList[id=808601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1310. [[podstawowe] Wróg / część [808602] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=808602].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1311. [[podstawowe] Wróg / część [808602] — opis] 부위
   źródło: Enemies.json :: dataList[id=808602].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1312. [[podstawowe] Wróg / część [8087] — nazwa] 떠돌이 여우
   źródło: Enemies.json :: dataList[id=8087].name
   (powtórzenie elementu 1056 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1313. [[podstawowe] Wróg / część [8087] — opis] 본체
   źródło: Enemies.json :: dataList[id=8087].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1314. [[podstawowe] Wróg / część [808701] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808701].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1315. [[podstawowe] Wróg / część [808701] — opis] 부위
   źródło: Enemies.json :: dataList[id=808701].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1316. [[podstawowe] Wróg / część [808702] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=808702].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1317. [[podstawowe] Wróg / część [808702] — opis] 부위
   źródło: Enemies.json :: dataList[id=808702].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1318. [[podstawowe] Wróg / część [8088] — nazwa] 낡은 우산
   źródło: Enemies.json :: dataList[id=8088].name
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1319. [[podstawowe] Wróg / część [8088] — opis] 본체
   źródło: Enemies.json :: dataList[id=8088].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1320. [[podstawowe] Wróg / część [808801] — nazwa] 우산
   źródło: Enemies.json :: dataList[id=808801].name
   (powtórzenie elementu 1084 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1321. [[podstawowe] Wróg / część [808801] — opis] 부위
   źródło: Enemies.json :: dataList[id=808801].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1322. [[podstawowe] Wróg / część [8089] — nazwa] 누구도 울지 않도록
   źródło: Enemies.json :: dataList[id=8089].name
   (powtórzenie elementu 1062 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1323. [[podstawowe] Wróg / część [8089] — opis] 본체
   źródło: Enemies.json :: dataList[id=8089].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1324. [[podstawowe] Wróg / część [808901] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=808901].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1325. [[podstawowe] Wróg / część [808901] — opis] 부위
   źródło: Enemies.json :: dataList[id=808901].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1326. [[podstawowe] Wróg / część [808902] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=808902].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1327. [[podstawowe] Wróg / część [808902] — opis] 부위
   źródło: Enemies.json :: dataList[id=808902].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1328. [[podstawowe] Wróg / część [8090] — nazwa] 신사 요정
   źródło: Enemies.json :: dataList[id=8090].name
   (powtórzenie elementu 1068 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1329. [[podstawowe] Wróg / część [8090] — opis] 본체
   źródło: Enemies.json :: dataList[id=8090].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1330. [[podstawowe] Wróg / część [809001] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1331. [[podstawowe] Wróg / część [809001] — opis] 부위
   źródło: Enemies.json :: dataList[id=809001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1332. [[podstawowe] Wróg / część [809002] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=809002].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1333. [[podstawowe] Wróg / część [809002] — opis] 부위
   źródło: Enemies.json :: dataList[id=809002].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1334. [[podstawowe] Wróg / część [8091] — nazwa] 요정주
   źródło: Enemies.json :: dataList[id=8091].name
   (powtórzenie elementu 1078 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1335. [[podstawowe] Wróg / część [8091] — opis] 본체
   źródło: Enemies.json :: dataList[id=8091].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1336. [[podstawowe] Wróg / część [809101] — nazwa] 술통
   źródło: Enemies.json :: dataList[id=809101].name
   (powtórzenie elementu 1080 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1337. [[podstawowe] Wróg / część [809101] — opis] 부위
   źródło: Enemies.json :: dataList[id=809101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1338. [[podstawowe] Wróg / część [8092] — nazwa] 키다리 요정
   źródło: Enemies.json :: dataList[id=8092].name
   limit: do 40 znaków
   EN: Fairy Longlegs
   PL: Fairy Longlegs
1339. [[podstawowe] Wróg / część [8092] — opis] 본체
   źródło: Enemies.json :: dataList[id=8092].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1340. [[podstawowe] Wróg / część [809201] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1341. [[podstawowe] Wróg / część [809201] — opis] 부위
   źródło: Enemies.json :: dataList[id=809201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1342. [[podstawowe] Wróg / część [809202] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=809202].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1343. [[podstawowe] Wróg / część [809202] — opis] 부위
   źródło: Enemies.json :: dataList[id=809202].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1344. [[podstawowe] Wróg / część [809203] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=809203].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1345. [[podstawowe] Wróg / część [809203] — opis] 부위
   źródło: Enemies.json :: dataList[id=809203].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1346. [[podstawowe] Wróg / część [8093] — nazwa] 거대한 잎사귀
   źródło: Enemies.json :: dataList[id=8093].name
   (powtórzenie elementu 1234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1347. [[podstawowe] Wróg / część [8093] — opis] 본체
   źródło: Enemies.json :: dataList[id=8093].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1348. [[podstawowe] Wróg / część [809301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1349. [[podstawowe] Wróg / część [809301] — opis] 부위
   źródło: Enemies.json :: dataList[id=809301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1350. [[podstawowe] Wróg / część [8094] — nazwa] 황금빛의 사과
   źródło: Enemies.json :: dataList[id=8094].name
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1351. [[podstawowe] Wróg / część [8094] — opis] 본체
   źródło: Enemies.json :: dataList[id=8094].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1352. [[podstawowe] Wróg / część [8095] — nazwa] 거짓 사과
   źródło: Enemies.json :: dataList[id=8095].name
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1353. [[podstawowe] Wróg / część [8095] — opis] 본체
   źródło: Enemies.json :: dataList[id=8095].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1354. [[podstawowe] Wróg / część [809401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1355. [[podstawowe] Wróg / część [809401] — opis] 부위
   źródło: Enemies.json :: dataList[id=809401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1356. [[podstawowe] Wróg / część [809501] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=809501].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1357. [[podstawowe] Wróg / część [809501] — opis] 부위
   źródło: Enemies.json :: dataList[id=809501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1358. [[podstawowe] Wróg / część [809502] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809502].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1359. [[podstawowe] Wróg / część [809502] — opis] 부위
   źródło: Enemies.json :: dataList[id=809502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1360. [[podstawowe] Wróg / część [8096] — nazwa] 놋쇠 황소 - 눈물 흘리는
   źródło: Enemies.json :: dataList[id=8096].name
   (powtórzenie elementu 1032 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1361. [[podstawowe] Wróg / część [8096] — opis] 본체
   źródło: Enemies.json :: dataList[id=8096].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1362. [[podstawowe] Wróg / część [809601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=809601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1363. [[podstawowe] Wróg / część [809601] — opis] 부위
   źródło: Enemies.json :: dataList[id=809601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1364. [[podstawowe] Wróg / część [809602] — nazwa] 머리
   źródło: Enemies.json :: dataList[id=809602].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1365. [[podstawowe] Wróg / część [809602] — opis] 부위
   źródło: Enemies.json :: dataList[id=809602].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1366. [[podstawowe] Wróg / część [8263] — nazwa] 여왕 요정
   źródło: Enemies.json :: dataList[id=8263].name
   limit: do 40 znaków
   EN: Fairy Queen
   PL: Fairy Queen
1367. [[podstawowe] Wróg / część [8263] — opis] 본체
   źródło: Enemies.json :: dataList[id=8263].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1368. [[podstawowe] Wróg / część [826301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=826301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1369. [[podstawowe] Wróg / część [826301] — opis] 부위
   źródło: Enemies.json :: dataList[id=826301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1370. [[podstawowe] Wróg / część [826302] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=826302].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1371. [[podstawowe] Wróg / część [826302] — opis] 부위
   źródło: Enemies.json :: dataList[id=826302].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1372. [[podstawowe] Wróg / część [826303] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=826303].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1373. [[podstawowe] Wróg / część [826303] — opis] 부위
   źródło: Enemies.json :: dataList[id=826303].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1374. [[podstawowe] Wróg / część [8264] — nazwa] 요정 덩이
   źródło: Enemies.json :: dataList[id=8264].name
   limit: do 40 znaków
   EN: Fairy Mass
   PL: Fairy Mass
1375. [[podstawowe] Wróg / część [8264] — opis] 본체
   źródło: Enemies.json :: dataList[id=8264].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1376. [[podstawowe] Wróg / część [826401] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=826401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1377. [[podstawowe] Wróg / część [826401] — opis] 부위
   źródło: Enemies.json :: dataList[id=826401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1378. [[podstawowe] Wróg / część [8265] — nazwa] 여왕 요정
   źródło: Enemies.json :: dataList[id=8265].name
   (powtórzenie elementu 1366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1379. [[podstawowe] Wróg / część [8265] — opis] 본체
   źródło: Enemies.json :: dataList[id=8265].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1380. [[podstawowe] Wróg / część [826501] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=826501].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1381. [[podstawowe] Wróg / część [826501] — opis] 부위
   źródło: Enemies.json :: dataList[id=826501].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1382. [[podstawowe] Wróg / część [826502] — nazwa] 오른팔
   źródło: Enemies.json :: dataList[id=826502].name
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1383. [[podstawowe] Wróg / część [826502] — opis] 부위
   źródło: Enemies.json :: dataList[id=826502].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1384. [[podstawowe] Wróg / część [826503] — nazwa] 왼팔
   źródło: Enemies.json :: dataList[id=826503].name
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1385. [[podstawowe] Wróg / część [826503] — opis] 부위
   źródło: Enemies.json :: dataList[id=826503].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1386. [[podstawowe] Wróg / część [8266] — nazwa] 요정 덩이
   źródło: Enemies.json :: dataList[id=8266].name
   (powtórzenie elementu 1374 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1387. [[podstawowe] Wróg / część [8266] — opis] 본체
   źródło: Enemies.json :: dataList[id=8266].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1388. [[podstawowe] Wróg / część [826601] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=826601].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1389. [[podstawowe] Wróg / część [826601] — opis] 부위
   źródło: Enemies.json :: dataList[id=826601].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1390. [[podstawowe] Wróg / część [1058] — nazwa] 어느 날의 초상
   źródło: Enemies.json :: dataList[id=1058].name
   limit: do 40 znaków
   EN: Portrait of a Certain Day
   PL: Portrait of a Certain Day
1391. [[podstawowe] Wróg / część [1058] — opis] 본체
   źródło: Enemies.json :: dataList[id=1058].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1392. [[podstawowe] Wróg / część [1059] — nazwa] 초상화
   źródło: Enemies.json :: dataList[id=1059].name
   limit: do 40 znaków
   EN: Portrait
   PL: Portrait
1393. [[podstawowe] Wróg / część [1059] — opis] 본체
   źródło: Enemies.json :: dataList[id=1059].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1394. [[podstawowe] Wróg / część [1060] — nazwa] 초상화
   źródło: Enemies.json :: dataList[id=1060].name
   (powtórzenie elementu 1392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1395. [[podstawowe] Wróg / część [1060] — opis] 본체
   źródło: Enemies.json :: dataList[id=1060].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1396. [[podstawowe] Wróg / część [1061] — nazwa] 꿈꾸는 전기양
   źródło: Enemies.json :: dataList[id=1061].name
   limit: do 40 znaków
   EN: Dreaming Electric Sheep
   PL: Dreaming Electric Sheep
1397. [[podstawowe] Wróg / część [1061] — opis] 본체
   źródło: Enemies.json :: dataList[id=1061].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1398. [[podstawowe] Wróg / część [1062] — nazwa] 발전기
   źródło: Enemies.json :: dataList[id=1062].name
   limit: do 40 znaków
   EN: Generator
   PL: Generator
1399. [[podstawowe] Wróg / część [1062] — opis] 본체
   źródło: Enemies.json :: dataList[id=1062].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1400. [[podstawowe] Wróg / część [1063] — nazwa] 묶인 왕
   źródło: Enemies.json :: dataList[id=1063].name
   limit: do 40 znaków
   EN: The King in Binds
   PL: The King in Binds
1401. [[podstawowe] Wróg / część [99022] — nazwa] 숫자 세는 불한당
   źródło: Enemies.json :: dataList[id=99022].name
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1402. [[podstawowe] Wróg / część [99023] — nazwa] 예리한 불한당
   źródło: Enemies.json :: dataList[id=99023].name
   (powtórzenie elementu 444 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1403. [[podstawowe] Wróg / część [99024] — nazwa] 대가리 불한당
   źródło: Enemies.json :: dataList[id=99024].name
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1404. [[podstawowe] Wróg / część [99025] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99025].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1405. [[podstawowe] Wróg / część [99026] — nazwa] 허기진 불한당
   źródło: Enemies.json :: dataList[id=99026].name
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1406. [[podstawowe] Wróg / część [1142] — nazwa] 탐식 죄종
   źródło: Enemies.json :: dataList[id=1142].name
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1407. [[podstawowe] Wróg / część [1142] — opis] 본체
   źródło: Enemies.json :: dataList[id=1142].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1408. [[podstawowe] Wróg / część [1143] — nazwa] 탐식 죄종
   źródło: Enemies.json :: dataList[id=1143].name
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1409. [[podstawowe] Wróg / część [1143] — opis] 본체
   źródło: Enemies.json :: dataList[id=1143].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1410. [[podstawowe] Wróg / część [114301] — nazwa] 몸통
   źródło: Enemies.json :: dataList[id=114301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1411. [[podstawowe] Wróg / część [114301] — opis] 부위
   źródło: Enemies.json :: dataList[id=114301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1412. [[podstawowe] Wróg / część [1222] — nazwa] 흉탄의 사수
   źródło: Enemies.json :: dataList[id=1222].name
   limit: do 40 znaków
   EN: Der Fluchschütze
   PL: Der Fluchschütze
1413. [[podstawowe] Wróg / część [1222] — opis] 본체
   źródło: Enemies.json :: dataList[id=1222].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1414. [[podstawowe] Wróg / część [1174] — nazwa] 지난 날의 침낭
   źródło: Enemies.json :: dataList[id=1174].name
   limit: do 40 znaków
   EN: Sleeping Bag of a Bygone Day
   PL: Sleeping Bag of a Bygone Day
1415. [[podstawowe] Wróg / część [1174] — opis] 본체
   źródło: Enemies.json :: dataList[id=1174].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1416. [[podstawowe] Wróg / część [1175] — nazwa] 사백송이의 장미
   źródło: Enemies.json :: dataList[id=1175].name
   limit: do 40 znaków
   EN: Four-hundred Roses
   PL: Four-hundred Roses
1417. [[podstawowe] Wróg / część [1175] — opis] 본체
   źródło: Enemies.json :: dataList[id=1175].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1418. [[podstawowe] Wróg / część [1172] — nazwa] 옛 G사 부장
   źródło: Enemies.json :: dataList[id=1172].name
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1419. [[podstawowe] Wróg / część [1172] — opis] 본체
   źródło: Enemies.json :: dataList[id=1172].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1420. [[podstawowe] Wróg / część [1173] — nazwa] 옛 G사 부장
   źródło: Enemies.json :: dataList[id=1173].name
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1421. [[podstawowe] Wróg / część [1173] — opis] 본체
   źródło: Enemies.json :: dataList[id=1173].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [podstawowe] Wróg / część: Enemies91-4
- plik gry: `Enemies91-4.json`

1422. [[podstawowe] Wróg / część [90077] — nazwa] 날카로운 크랲게
   źródło: Enemies91-4.json :: dataList[id=90077].name
   limit: do 40 znaków
   EN: Sharp Trash Crab
   PL: Sharp Trash Crab
1423. [[podstawowe] Wróg / część [90077] — opis] 적 잡몹
   źródło: Enemies91-4.json :: dataList[id=90077].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1424. [[podstawowe] Wróg / część [90078] — nazwa] 뾰족한 크랲게
   źródło: Enemies91-4.json :: dataList[id=90078].name
   limit: do 40 znaków
   EN: Pointy Trash Crab
   PL: Pointy Trash Crab
1425. [[podstawowe] Wróg / część [90078] — opis] 적 잡몹
   źródło: Enemies91-4.json :: dataList[id=90078].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1426. [[podstawowe] Wróg / część [90079] — nazwa] 딱딱한 크랲게
   źródło: Enemies91-4.json :: dataList[id=90079].name
   limit: do 40 znaków
   EN: Hard Trash Crab
   PL: Hard Trash Crab
1427. [[podstawowe] Wróg / część [90079] — opis] 적 잡몹
   źródło: Enemies91-4.json :: dataList[id=90079].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1428. [[podstawowe] Wróg / część [90080] — nazwa] 잔탄 크랲게
   źródło: Enemies91-4.json :: dataList[id=90080].name
   limit: do 40 znaków
   EN: Cannoneer Crab
   PL: Cannoneer Crab
1429. [[podstawowe] Wróg / część [90080] — opis] 적 잡몹
   źródło: Enemies91-4.json :: dataList[id=90080].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1430. [[podstawowe] Wróg / część [90081] — nazwa] 포검 크랲게
   źródło: Enemies91-4.json :: dataList[id=90081].name
   limit: do 40 znaków
   EN: Bayonet Artillery Crab
   PL: Bayonet Artillery Crab
1431. [[podstawowe] Wróg / część [90081] — opis] 적 잡몹
   źródło: Enemies91-4.json :: dataList[id=90081].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1432. [[podstawowe] Wróg / część [8063] — nazwa] 킹크랲게
   źródło: Enemies91-4.json :: dataList[id=8063].name
   limit: do 40 znaków
   EN: King Trash Crab
   PL: King Trash Crab
1433. [[podstawowe] Wróg / część [8063] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8063].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1434. [[podstawowe] Wróg / część [806301] — nazwa] 머리
   źródło: Enemies91-4.json :: dataList[id=806301].name
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1435. [[podstawowe] Wróg / część [806301] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=806301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1436. [[podstawowe] Wróg / część [806302] — nazwa] 소라
   źródło: Enemies91-4.json :: dataList[id=806302].name
   limit: do 40 znaków
   EN: Shell
   PL: Shell
1437. [[podstawowe] Wróg / część [806302] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=806302].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1438. [[podstawowe] Wróg / część [8070] — nazwa] 날카로운 크랲게
   źródło: Enemies91-4.json :: dataList[id=8070].name
   (powtórzenie elementu 1422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1439. [[podstawowe] Wróg / część [8070] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8070].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1440. [[podstawowe] Wróg / część [807001] — nazwa] 몸통
   źródło: Enemies91-4.json :: dataList[id=807001].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1441. [[podstawowe] Wróg / część [807001] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=807001].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1442. [[podstawowe] Wróg / część [8071] — nazwa] 뾰족한 크랲게
   źródło: Enemies91-4.json :: dataList[id=8071].name
   (powtórzenie elementu 1424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1443. [[podstawowe] Wróg / część [8071] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8071].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1444. [[podstawowe] Wróg / część [807101] — nazwa] 몸통
   źródło: Enemies91-4.json :: dataList[id=807101].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1445. [[podstawowe] Wróg / część [807101] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=807101].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1446. [[podstawowe] Wróg / część [8072] — nazwa] 딱딱한 크랲게
   źródło: Enemies91-4.json :: dataList[id=8072].name
   (powtórzenie elementu 1426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1447. [[podstawowe] Wróg / część [8072] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8072].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1448. [[podstawowe] Wróg / część [807201] — nazwa] 몸통
   źródło: Enemies91-4.json :: dataList[id=807201].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1449. [[podstawowe] Wróg / część [807201] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=807201].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1450. [[podstawowe] Wróg / część [8073] — nazwa] 잔탄 크랲게
   źródło: Enemies91-4.json :: dataList[id=8073].name
   (powtórzenie elementu 1428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1451. [[podstawowe] Wróg / część [8073] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8073].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1452. [[podstawowe] Wróg / część [807301] — nazwa] 몸통
   źródło: Enemies91-4.json :: dataList[id=807301].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1453. [[podstawowe] Wróg / część [807301] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=807301].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1454. [[podstawowe] Wróg / część [8074] — nazwa] 포검 크랲게
   źródło: Enemies91-4.json :: dataList[id=8074].name
   (powtórzenie elementu 1430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1455. [[podstawowe] Wróg / część [8074] — opis] 본체
   źródło: Enemies91-4.json :: dataList[id=8074].desc
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1456. [[podstawowe] Wróg / część [807401] — nazwa] 몸통
   źródło: Enemies91-4.json :: dataList[id=807401].name
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1457. [[podstawowe] Wróg / część [807401] — opis] 부위
   źródło: Enemies91-4.json :: dataList[id=807401].desc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## [podstawowe] Umiejętności wrogów / Anomalii — Skills_Abnormality
- grupa rozdziału/trybu: `podstawowe` · plik: `Skills_Abnormality.json`

1458. [Umiejętność wroga [800001] (ulepszenie 1) — nazwa] 방어
   źródło: Skills_Abnormality.json :: dataList[id=800001].levelList[level=1].name
   limit: do 40 znaków
   EN: Guard
   PL: Guard
1459. [Umiejętność wroga [800002] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality.json :: dataList[id=800002].levelList[level=1].name
   limit: do 40 znaków
   EN: Evade
   PL: Evade
1460. [Umiejętność wroga [800003] (ulepszenie 1) — nazwa] 반격
   źródło: Skills_Abnormality.json :: dataList[id=800003].levelList[level=1].name
   limit: do 40 znaków
   EN: Counter
   PL: Counter
1461. [Umiejętność wroga [800004] (ulepszenie 1) — nazwa] 회피
   źródło: Skills_Abnormality.json :: dataList[id=800004].levelList[level=1].name
   (powtórzenie elementu 1459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1462. [Umiejętność wroga [8001001] (ulepszenie 1) — nazwa] 불신
   źródło: Skills_Abnormality.json :: dataList[id=8001001].levelList[level=1].name
   limit: do 40 znaków
   EN: Distrust
   PL: Distrust
1463. [Umiejętność wroga [8001002] (ulepszenie 1) — nazwa] 빛바랜 줄기
   źródło: Skills_Abnormality.json :: dataList[id=8001002].levelList[level=1].name
   limit: do 40 znaków
   EN: Pale Stem
   PL: Pale Stem
1464. [Umiejętność wroga [8001003] (ulepszenie 1) — nazwa] 빛바랜 줄기
   źródło: Skills_Abnormality.json :: dataList[id=8001003].levelList[level=1].name
   (powtórzenie elementu 1463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1465. [Umiejętność wroga [8001004] (ulepszenie 1) — nazwa] 뿌리 가시
   źródło: Skills_Abnormality.json :: dataList[id=8001004].levelList[level=1].name
   limit: do 40 znaków
   EN: Root Spike
   PL: Root Spike
1466. [Umiejętność wroga [8001004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=8001004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +3 Bleed Count next turn
   PL: [OnSucceedAttackHead] Zwiększa Licznik Krwawienia o 3 w następnej turze
1467. [Umiejętność wroga [8001005] (ulepszenie 1) — nazwa] 모두의 아픔
   źródło: Skills_Abnormality.json :: dataList[id=8001005].levelList[level=1].name
   limit: do 40 znaków
   EN: Shared Pain
   PL: Shared Pain
1468. [Umiejętność wroga [8001005] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=8001005].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Fragile next turn
   PL: [OnSucceedAttackHead] nakłada 1 Wrażliwości w następnej turze
1469. [Umiejętność wroga [8001006] (ulepszenie 1) — nazwa] 허무의 열매
   źródło: Skills_Abnormality.json :: dataList[id=8001006].levelList[level=1].name
   limit: do 40 znaków
   EN: Vain Fruit
   PL: Vain Fruit
1470. [Umiejętność wroga [800501] (ulepszenie 1) — nazwa] 물어뜯기
   źródło: Skills_Abnormality.json :: dataList[id=800501].levelList[level=1].name
   limit: do 40 znaków
   EN: Nibble
   PL: Nibble
1471. [Umiejętność wroga [800502] (ulepszenie 1) — nazwa] 탐욕스러운 식사
   źródło: Skills_Abnormality.json :: dataList[id=800502].levelList[level=1].name
   limit: do 40 znaków
   EN: Greedy Gluttons
   PL: Greedy Gluttons
1472. [Umiejętność wroga [800502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=800502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Heal 1 HP
   PL: [OnSucceedAttackHead] przywraca 1 HP
1473. [Umiejętność wroga [800502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=800502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1474. [Umiejętność wroga [800502] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 체력 1 회복
   źródło: Skills_Abnormality.json :: dataList[id=800502].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1475. [Umiejętność wroga [800601] (ulepszenie 1) — nazwa] 구르기
   źródło: Skills_Abnormality.json :: dataList[id=800601].levelList[level=1].name
   limit: do 40 znaków
   EN: Roll
   PL: Roll
1476. [Umiejętność wroga [800602] (ulepszenie 1) — nazwa] 나태한 손아귀
   źródło: Skills_Abnormality.json :: dataList[id=800602].levelList[level=1].name
   limit: do 40 znaków
   EN: Slothful Grip
   PL: Slothful Grip
1477. [Umiejętność wroga [800602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 속박 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=800602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Bind next turn
   PL: [OnSucceedAttackHead] nakłada 3 Spętania w następnej turze
1478. [Umiejętność wroga [800701] (ulepszenie 1) — nazwa] 지지기
   źródło: Skills_Abnormality.json :: dataList[id=800701].levelList[level=1].name
   limit: do 40 znaków
   EN: Sear
   PL: Sear
1479. [Umiejętność wroga [800702] (ulepszenie 1) — nazwa] 폭발하는 분노
   źródło: Skills_Abnormality.json :: dataList[id=800702].levelList[level=1].name
   limit: do 40 znaków
   EN: Explosive Wrath
   PL: Explosive Wrath
1480. [Umiejętność wroga [800702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 화상 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=800702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Burn next turn
   PL: [OnSucceedAttackHead] nakłada 2 Podpalenia w następnej turze
1481. [Umiejętność wroga [800201] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Abnormality.json :: dataList[id=800201].levelList[level=1].name
   limit: do 40 znaków
   EN: Slam
   PL: Slam
1482. [Umiejętność wroga [800202] (ulepszenie 1) — nazwa] 내려치기
   źródło: Skills_Abnormality.json :: dataList[id=800202].levelList[level=1].name
   (powtórzenie elementu 1481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1483. [Umiejętność wroga [800203] (ulepszenie 1) — nazwa] 땅울림
   źródło: Skills_Abnormality.json :: dataList[id=800203].levelList[level=1].name
   limit: do 40 znaków
   EN: Quake
   PL: Quake
1484. [Umiejętność wroga [800203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=800203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Bind next turn
   PL: [OnSucceedAttack] nakłada 1 Spętania w następnej turze
1485. [Umiejętność wroga [800204] (ulepszenie 1) — nazwa] 산제물 의식
   źródło: Skills_Abnormality.json :: dataList[id=800204].levelList[level=1].name
   limit: do 40 znaków
   EN: Live Offering
   PL: Live Offering
1486. [Umiejętność wroga [800204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=800204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict +3 Bleed Count next turn
   PL: [OnSucceedAttack] Zwiększa Licznik Krwawienia o 3 w następnej turze
1487. [Umiejętność wroga [800205] (ulepszenie 1) — nazwa] 타오르는 우주
   źródło: Skills_Abnormality.json :: dataList[id=800205].levelList[level=1].name
   limit: do 40 znaków
   EN: Universe Aflame
   PL: Universe Aflame
1488. [Umiejętność wroga [800206] (ulepszenie 1) — nazwa] 굳건한 제단
   źródło: Skills_Abnormality.json :: dataList[id=800206].levelList[level=1].name
   limit: do 40 znaków
   EN: Stalwart Altar
   PL: Stalwart Altar
1489. [Umiejętność wroga [800207] (ulepszenie 1) — nazwa] 타오르는 우주
   źródło: Skills_Abnormality.json :: dataList[id=800207].levelList[level=1].name
   (powtórzenie elementu 1487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1490. [Umiejętność wroga [800207] (ulepszenie 1) — opis] [CantDuel] 아군을 타겟으로 지정
   źródło: Skills_Abnormality.json :: dataList[id=800207].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel] Targets allies
   PL: [CantDuel] celuje w sojuszników
1491. [Umiejętność wroga [800301] (ulepszenie 1) — nazwa] 찌르기
   źródło: Skills_Abnormality.json :: dataList[id=800301].levelList[level=1].name
   limit: do 40 znaków
   EN: Lunge
   PL: Lunge
1492. [Umiejętność wroga [800301] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800301].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Bleed Count next turn
   PL: [OnSucceedAttackHead] Zwiększa Licznik Krwawienia o 1 w następnej turze
1493. [Umiejętność wroga [800302] (ulepszenie 1) — nazwa] 할퀴기
   źródło: Skills_Abnormality.json :: dataList[id=800302].levelList[level=1].name
   limit: do 40 znaków
   EN: Claw
   PL: Claw
1494. [Umiejętność wroga [800302] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800302].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1495. [Umiejętność wroga [800402] (ulepszenie 1) — nazwa] 고통스러운 찌르기
   źródło: Skills_Abnormality.json :: dataList[id=800402].levelList[level=1].name
   limit: do 40 znaków
   EN: Severe Lunge
   PL: Severe Lunge
1496. [Umiejętność wroga [800402] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800402].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1497. [Umiejętność wroga [800402] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 화상 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800402].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict +1 Burn Count next turn
   PL: [OnSucceedAttackHead] Zwiększa Licznik Podpalenia o 1 w następnej turze
1498. [Umiejętność wroga [800403] (ulepszenie 1) — nazwa] 고통스러운 할퀴기
   źródło: Skills_Abnormality.json :: dataList[id=800403].levelList[level=1].name
   limit: do 40 znaków
   EN: Raw Claw
   PL: Raw Claw
1499. [Umiejętność wroga [800403] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800403].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1492 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1500. [Umiejętność wroga [800403] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttackHead] 다음 턴에 화상 횟수 1 증가
   źródło: Skills_Abnormality.json :: dataList[id=800403].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 1497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1501. [Umiejętność wroga [800401] (ulepszenie 1) — nazwa] 불 뿜기
   źródło: Skills_Abnormality.json :: dataList[id=800401].levelList[level=1].name
   limit: do 40 znaków
   EN: Belch Fire
   PL: Belch Fire
1502. [Umiejętność wroga [800401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 화상 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=800401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Burn next turn
   PL: [OnSucceedAttack] nakłada 1 Podpalenia w następnej turze
1503. [Umiejętność wroga [800801] (ulepszenie 1) — nazwa] 발아
   źródło: Skills_Abnormality.json :: dataList[id=800801].levelList[level=1].name
   limit: do 40 znaków
   EN: Sprout
   PL: Sprout
1504. [Umiejętność wroga [800802] (ulepszenie 1) — nazwa] 황금 과실
   źródło: Skills_Abnormality.json :: dataList[id=800802].levelList[level=1].name
   limit: do 40 znaków
   EN: Golden Fruit
   PL: Golden Fruit
1505. [Umiejętność wroga [800802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [DefeatDuel] 자신에게 피해 20
   źródło: Skills_Abnormality.json :: dataList[id=800802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Take 20 damage
   PL: [DefeatDuel] otrzymuje 20 obrażeń
1506. [Umiejętność wroga [800802] (ulepszenie 1) — moneta 1, efekt 2 — opis] [DefeatDuel] 황금빛 1 잃음
   źródło: Skills_Abnormality.json :: dataList[id=800802].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefeatDuel]
   znaczenie tagów: [DefeatDuel] = [합 패배] / [Clash Lose]
   EN: [DefeatDuel] Lose 1 Golden Sheen
   PL: [DefeatDuel] traci 1 Złotego Blasku
1507. [Umiejętność wroga [800803] (ulepszenie 1) — nazwa] 단단한 황금
   źródło: Skills_Abnormality.json :: dataList[id=800803].levelList[level=1].name
   limit: do 40 znaków
   EN: Solid Gold
   PL: Solid Gold
1508. [Umiejętność wroga [800901] (ulepszenie 1) — nazwa] 영양분 흡수
   źródło: Skills_Abnormality.json :: dataList[id=800901].levelList[level=1].name
   limit: do 40 znaków
   EN: Absorb Nutrients
   PL: Absorb Nutrients
1509. [Umiejętność wroga [800901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 3 회복
   źródło: Skills_Abnormality.json :: dataList[id=800901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Main body heals 3 HP
   PL: [OnSucceedAttack] główne ciało przywraca 3 HP
1510. [Umiejętność wroga [800902] (ulepszenie 1) — nazwa] 허물어지는 과육
   źródło: Skills_Abnormality.json :: dataList[id=800902].levelList[level=1].name
   limit: do 40 znaków
   EN: Deteriorating Flesh
   PL: Deteriorating Flesh
1511. [Umiejętność wroga [800902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 횟수 3 증가
   źródło: Skills_Abnormality.json :: dataList[id=800902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1486 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1512. [Umiejętność wroga [800902] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 취약 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=800902].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Fragile next turn
   PL: [OnSucceedAttack] nakłada 2 Wrażliwości w następnej turze
1513. [Umiejętność wroga [800903] (ulepszenie 1) — nazwa] 포획
   źródło: Skills_Abnormality.json :: dataList[id=800903].levelList[level=1].name
   limit: do 40 znaków
   EN: Entangle
   PL: Entangle
1514. [Umiejętność wroga [800903] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 본체의 체력 10 회복
   źródło: Skills_Abnormality.json :: dataList[id=800903].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Main body heals 10 HP
   PL: [OnSucceedAttack] główne ciało przywraca 10 HP
1515. [Umiejętność wroga [800903] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 출혈 5 부여
   źródło: Skills_Abnormality.json :: dataList[id=800903].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 5 Bleed next turn
   PL: [OnSucceedAttack] nakłada 5 Krwawienia w następnej turze
1516. [Umiejętność wroga [801001] (ulepszenie 1) — nazwa] 일을 하자...
   źródło: Skills_Abnormality.json :: dataList[id=801001].levelList[level=1].name
   limit: do 40 znaków
   EN: Let’s Get to Work…
   PL: Let’s Get to Work…
1517. [Umiejętność wroga [801002] (ulepszenie 1) — nazwa] 열심히!
   źródło: Skills_Abnormality.json :: dataList[id=801002].levelList[level=1].name
   limit: do 40 znaków
   EN: Work Hard!
   PL: Work Hard!
1518. [Umiejętność wroga [801002] (ulepszenie 1) — opis] [WhenUse] 자신에게 피해 10.\n 스킬 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=801002].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 10 HP; Skill Power +1
   PL: [WhenUse] traci 10 HP;\n Moc Umiejętności +1
1519. [Umiejętność wroga [801003] (ulepszenie 1) — nazwa] 바빠...
   źródło: Skills_Abnormality.json :: dataList[id=801003].levelList[level=1].name
   limit: do 40 znaków
   EN: So Busy…
   PL: So Busy…
1520. [Umiejętność wroga [801101] (ulepszenie 1) — nazwa] 해치우자...
   źródło: Skills_Abnormality.json :: dataList[id=801101].levelList[level=1].name
   limit: do 40 znaków
   EN: Best Get It Over With…
   PL: Best Get It Over With…
1521. [Umiejętność wroga [801102] (ulepszenie 1) — nazwa] 부지런히!
   źródło: Skills_Abnormality.json :: dataList[id=801102].levelList[level=1].name
   limit: do 40 znaków
   EN: Stay Diligent!
   PL: Stay Diligent!
1522. [Umiejętność wroga [801102] (ulepszenie 1) — opis] [WhenUse] 자신에게 피해 10.\n 스킬 위력 +1
   źródło: Skills_Abnormality.json :: dataList[id=801102].levelList[level=1].desc
   (powtórzenie elementu 1518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1523. [Umiejętność wroga [801103] (ulepszenie 1) — nazwa] 바빠...
   źródło: Skills_Abnormality.json :: dataList[id=801103].levelList[level=1].name
   (powtórzenie elementu 1519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1524. [Umiejętność wroga [801201] (ulepszenie 1) — nazwa] 일할 시간이다!
   źródło: Skills_Abnormality.json :: dataList[id=801201].levelList[level=1].name
   limit: do 40 znaków
   EN: Worktime!
   PL: Worktime!
1525. [Umiejętność wroga [801202] (ulepszenie 1) — nazwa] 일하자!
   źródło: Skills_Abnormality.json :: dataList[id=801202].levelList[level=1].name
   limit: do 40 znaków
   EN: Get to Work!
   PL: Get to Work!
1526. [Umiejętność wroga [801202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 2 얻음
   źródło: Skills_Abnormality.json :: dataList[id=801202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Gain 2 Haste next turn
   PL: [OnSucceedAttack] zyskuje 2 Pośpiechu w następnej turze
1527. [Umiejętność wroga [801203] (ulepszenie 1) — nazwa] 신난다!!
   źródło: Skills_Abnormality.json :: dataList[id=801203].levelList[level=1].name
   limit: do 40 znaków
   EN: So Excited!!
   PL: So Excited!!
1528. [Umiejętność wroga [801203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Take 3 damage
   PL: [OnSucceedAttack] otrzymuje 3 obrażeń
1529. [Umiejętność wroga [801203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1530. [Umiejętność wroga [801204] (ulepszenie 1) — nazwa] 응☆징
   źródło: Skills_Abnormality.json :: dataList[id=801204].levelList[level=1].name
   limit: do 40 znaków
   EN: PUNISH☆MENT
   PL: PUNISH☆MENT
1531. [Umiejętność wroga [801204] (ulepszenie 1) — opis] [WhenUse] 자신에게 피해 10.\n 스킬 위력 +2
   źródło: Skills_Abnormality.json :: dataList[id=801204].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: [WhenUse] Lose 10 HP; Skill Power +2
   PL: [WhenUse] traci 10 HP;\n Moc Umiejętności +2
1532. [Umiejętność wroga [801205] (ulepszenie 1) — nazwa] 비.상.이.다!!!
   źródło: Skills_Abnormality.json :: dataList[id=801205].levelList[level=1].name
   limit: do 40 znaków
   EN: E-MER-GEN-CY!!!
   PL: E-MER-GEN-CY!!!
1533. [Umiejętność wroga [801205] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801205].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1534. [Umiejętność wroga [801205] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801205].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1535. [Umiejętność wroga [801205] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801205].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1536. [Umiejętność wroga [801206] (ulepszenie 1) — nazwa] 방해하지마?!
   źródło: Skills_Abnormality.json :: dataList[id=801206].levelList[level=1].name
   limit: do 40 znaków
   EN: Don’t Stop Me?!
   PL: Don’t Stop Me?!
1537. [Umiejętność wroga [801301] (ulepszenie 1) — nazwa] 억압된 몸짓
   źródło: Skills_Abnormality.json :: dataList[id=801301].levelList[level=1].name
   limit: do 40 znaków
   EN: Repressed Gesture
   PL: Repressed Gesture
1538. [Umiejętność wroga [801302] (ulepszenie 1) — nazwa] 조여드는 욕망
   źródło: Skills_Abnormality.json :: dataList[id=801302].levelList[level=1].name
   limit: do 40 znaków
   EN: Constricting Desires
   PL: Constricting Desires
1539. [Umiejętność wroga [801303] (ulepszenie 1) — nazwa] 분홍빛 춤
   źródło: Skills_Abnormality.json :: dataList[id=801303].levelList[level=1].name
   limit: do 40 znaków
   EN: Rosy Dance
   PL: Rosy Dance
1540. [Umiejętność wroga [801303] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 욕망 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=801303].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 1 Urge next turn
   PL: [OnSucceedAttack] nakłada 1 Urge w następnej turze
1541. [Umiejętność wroga [801303] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 욕망 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=801303].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1542. [Umiejętność wroga [801401] (ulepszenie 1) — nazwa] 억압된 몸짓
   źródło: Skills_Abnormality.json :: dataList[id=801401].levelList[level=1].name
   (powtórzenie elementu 1537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1543. [Umiejętność wroga [801402] (ulepszenie 1) — nazwa] 조여드는 욕망
   źródło: Skills_Abnormality.json :: dataList[id=801402].levelList[level=1].name
   (powtórzenie elementu 1538 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1544. [Umiejętność wroga [801403] (ulepszenie 1) — nazwa] 분홍빛 춤
   źródło: Skills_Abnormality.json :: dataList[id=801403].levelList[level=1].name
   (powtórzenie elementu 1539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1545. [Umiejętność wroga [801403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 욕망 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=801403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 2 Urge next turn
   PL: [OnSucceedAttack] nakłada 2 Urge w następnej turze
1546. [Umiejętność wroga [801501] (ulepszenie 1) — nazwa] 돈 벌 시간이다!
   źródło: Skills_Abnormality.json :: dataList[id=801501].levelList[level=1].name
   limit: do 40 znaków
   EN: Breadwinning!
   PL: Breadwinning!
1547. [Umiejętność wroga [801502] (ulepszenie 1) — nazwa] 돈 벌자!
   źródło: Skills_Abnormality.json :: dataList[id=801502].levelList[level=1].name
   limit: do 40 znaków
   EN: Make Some Riches!
   PL: Make Some Riches!
1548. [Umiejętność wroga [801502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 신속 2 얻음
   źródło: Skills_Abnormality.json :: dataList[id=801502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1549. [Umiejętność wroga [801503] (ulepszenie 1) — nazwa] 재미난다!!
   źródło: Skills_Abnormality.json :: dataList[id=801503].levelList[level=1].name
   limit: do 40 znaków
   EN: Thoroughly Amusing!!
   PL: Thoroughly Amusing!!
1550. [Umiejętność wroga [801503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Take 3 damage
   PL: [OnSucceedAttackHead] otrzymuje 3 obrażeń
1551. [Umiejętność wroga [801503] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 자신에게 피해 3
   źródło: Skills_Abnormality.json :: dataList[id=801503].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1552. [Umiejętność wroga [801504] (ulepszenie 1) — nazwa] 반짝☆반짝 돌아!?
   źródło: Skills_Abnormality.json :: dataList[id=801504].levelList[level=1].name
   limit: do 40 znaków
   EN: Twinkle☆Sprinkle Spinny!?
   PL: Twinkle☆Sprinkle Spinny!?
1553. [Umiejętność wroga [801504] (ulepszenie 1) — opis] [WhenUse] 자신에게 피해 10.\n 스킬 위력 +2
   źródło: Skills_Abnormality.json :: dataList[id=801504].levelList[level=1].desc
   (powtórzenie elementu 1531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1554. [Umiejętność wroga [801504] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 욕망 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=801504].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 3 Urge next turn
   PL: [OnSucceedAttack] nakłada 3 Urge w następnej turze
1555. [Umiejętność wroga [801601] (ulepszenie 1) — nazwa] 쏘아대기
   źródło: Skills_Abnormality.json :: dataList[id=801601].levelList[level=1].name
   limit: do 40 znaków
   EN: Fire Off
   PL: Fire Off
1556. [Umiejętność wroga [801602] (ulepszenie 1) — nazwa] 터져나오는 우울
   źródło: Skills_Abnormality.json :: dataList[id=801602].levelList[level=1].name
   limit: do 40 znaków
   EN: Bursting Gloom
   PL: Bursting Gloom
1557. [Umiejętność wroga [801602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 침잠 3 부여
   źródło: Skills_Abnormality.json :: dataList[id=801602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 3 Sinking next turn
   PL: [OnSucceedAttackHead] nakłada 3 Zatonięcia w następnej turze
1558. [Umiejętność wroga [801701] (ulepszenie 1) — nazwa] 내려찍기
   źródło: Skills_Abnormality.json :: dataList[id=801701].levelList[level=1].name
   limit: do 40 znaków
   EN: Strike Down
   PL: Strike Down
1559. [Umiejętność wroga [801702] (ulepszenie 1) — nazwa] 꿰뚫는 욕망
   źródło: Skills_Abnormality.json :: dataList[id=801702].levelList[level=1].name
   limit: do 40 znaków
   EN: Piercing Lust
   PL: Piercing Lust
1560. [Umiejętność wroga [801702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 2 부여
   źródło: Skills_Abnormality.json :: dataList[id=801702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 2 Bleed next turn
   PL: [OnSucceedAttackHead] nakłada 2 Krwawienia w następnej turze
1561. [Umiejętność wroga [801801] (ulepszenie 1) — nazwa] 갈아내기
   źródło: Skills_Abnormality.json :: dataList[id=801801].levelList[level=1].name
   limit: do 40 znaków
   EN: Grind
   PL: Grind
1562. [Umiejętność wroga [801802] (ulepszenie 1) — nazwa] 교만한 분쇄
   źródło: Skills_Abnormality.json :: dataList[id=801802].levelList[level=1].name
   limit: do 40 znaków
   EN: Prideful Runover
   PL: Prideful Runover
1563. [Umiejętność wroga [801802] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=801802].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1564. [Umiejętność wroga [801802] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=801802].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1565. [Umiejętność wroga [801901] (ulepszenie 1) — nazwa] 부리 찍기
   źródło: Skills_Abnormality.json :: dataList[id=801901].levelList[level=1].name
   limit: do 40 znaków
   EN: Beak Pick
   PL: Beak Pick
1566. [Umiejętność wroga [801902] (ulepszenie 1) — nazwa] 후려베기
   źródło: Skills_Abnormality.json :: dataList[id=801902].levelList[level=1].name
   limit: do 40 znaków
   EN: Slicing Smack
   PL: Slicing Smack
1567. [Umiejętność wroga [801903] (ulepszenie 1) — nazwa] 발길질
   źródło: Skills_Abnormality.json :: dataList[id=801903].levelList[level=1].name
   limit: do 40 znaków
   EN: Foot Stomp
   PL: Foot Stomp
1568. [Umiejętność wroga [801903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 취약 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=801903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1569. [Umiejętność wroga [802101] (ulepszenie 1) — nazwa] 부리 쪼기
   źródło: Skills_Abnormality.json :: dataList[id=802101].levelList[level=1].name
   limit: do 40 znaków
   EN: Beak Peck
   PL: Beak Peck
1570. [Umiejętność wroga [802102] (ulepszenie 1) — nazwa] 얼음 뱉기
   źródło: Skills_Abnormality.json :: dataList[id=802102].levelList[level=1].name
   limit: do 40 znaków
   EN: Ice Chuck
   PL: Ice Chuck
1571. [Umiejętność wroga [802103] (ulepszenie 1) — nazwa] 부리 부수기
   źródło: Skills_Abnormality.json :: dataList[id=802103].levelList[level=1].name
   limit: do 40 znaków
   EN: Beak Smash
   PL: Beak Smash
1572. [Umiejętność wroga [802103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 속박 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1484 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1573. [Umiejętność wroga [802401] (ulepszenie 1) — nazwa] 기괴한 눈동자
   źródło: Skills_Abnormality.json :: dataList[id=802401].levelList[level=1].name
   limit: do 40 znaków
   EN: Eerie Eyes
   PL: Eerie Eyes
1574. [Umiejętność wroga [802401] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신피해 5
   źródło: Skills_Abnormality.json :: dataList[id=802401].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 SP damage
   PL: [OnSucceedAttack] zadaje celowi 5 obrażeń Poczytalności
1575. [Umiejętność wroga [802401] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 대상에게 정신피해 5
   źródło: Skills_Abnormality.json :: dataList[id=802401].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1576. [Umiejętność wroga [802402] (ulepszenie 1) — nazwa] 어설픈 모방
   źródło: Skills_Abnormality.json :: dataList[id=802402].levelList[level=1].name
   limit: do 40 znaków
   EN: Imperfect Imitation
   PL: Imperfect Imitation
1577. [Umiejętność wroga [802402] (ulepszenie 1) — opis] 피격 당한 공격을 모방하여 사용.\n[WhenUse] 대상에게 정신피해 10
   źródło: Skills_Abnormality.json :: dataList[id=802402].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: Copies a skill that hit this unit\n[WhenUse] Deal 10 SP damage
   PL: kopiuje Umiejętność, która trafiła tę jednostkę\n[WhenUse] zadaje 10 obrażeń Poczytalności
1578. [Umiejętność wroga [802403] (ulepszenie 1) — nazwa] 껍데기 고치기
   źródło: Skills_Abnormality.json :: dataList[id=802403].levelList[level=1].name
   limit: do 40 znaków
   EN: Adjust Shell
   PL: Adjust Shell
1579. [Umiejętność wroga [802403] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 10%만큼 체력 회복. 본능을 1 얻음
   źródło: Skills_Abnormality.json :: dataList[id=802403].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10% of Max HP; Gain 1 Instincts
   PL: [OnSucceedAttack] przywraca HP równe 10% Maks. HP; zyskuje 1 Instynkt
1580. [Umiejętność wroga [802404] (ulepszenie 1) — nazwa] 뼈 폭발
   źródło: Skills_Abnormality.json :: dataList[id=802404].levelList[level=1].name
   limit: do 40 znaków
   EN: Bone Blast
   PL: Bone Blast
1581. [Umiejętność wroga [802404] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 최대 체력의 10%만큼 체력 회복
   źródło: Skills_Abnormality.json :: dataList[id=802404].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Heal 10% of Max HP
   PL: [OnSucceedAttack] przywraca HP równe 10% Maks. HP
1582. [Umiejętność wroga [802404] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 10 부여
   źródło: Skills_Abnormality.json :: dataList[id=802404].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 10 Bleed next turn
   PL: [OnSucceedAttack] nakłada 10 Krwawienia w następnej turze
1583. [Umiejętność wroga [802501] (ulepszenie 1) — nazwa] 거친 할퀴기
   źródło: Skills_Abnormality.json :: dataList[id=802501].levelList[level=1].name
   limit: do 40 znaków
   EN: Violent Scratch
   PL: Violent Scratch
1584. [Umiejętność wroga [802501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]
   EN: [OnSucceedAttackHead] Inflict 1 Bleed next turn
   PL: [OnSucceedAttackHead] nakłada 1 Krwawienia w następnej turze
1585. [Umiejętność wroga [802501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1586. [Umiejętność wroga [802501] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttackHead] 다음 턴에 출혈 1 부여
   źródło: Skills_Abnormality.json :: dataList[id=802501].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 1584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1587. [Umiejętność wroga [802502] (ulepszenie 1) — nazwa] 광적인 돌진
   źródło: Skills_Abnormality.json :: dataList[id=802502].levelList[level=1].name
   limit: do 40 znaków
   EN: Rabid Ram
   PL: Rabid Ram
1588. [Umiejętność wroga [802502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Inflict 4 Bleed next turn
   PL: [OnSucceedAttack] nakłada 4 Krwawienia w następnej turze
1589. [Umiejętność wroga [802502] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802502].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 1588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1590. [Umiejętność wroga [802503] (ulepszenie 1) — nazwa] 갈기갈기
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].name
   limit: do 40 znaków
   EN: Tear Apart
   PL: Tear Apart
1591. [Umiejętność wroga [802503] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 출혈 4 부여
   źródło: Skills_Abnormality.json :: dataList[id=802503].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 1588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
