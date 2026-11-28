# Paczka AI P18 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 4/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P18_2a_slowa_kluczowe_i_statusy_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P18_2a_slowa_kluczowe_i_statusy_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords-twth
- plik gry: `BattleKeywords-twth.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [IndexPrescriptEnemy_2] — nazwa] 지령[쪽지] III
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_2].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptEnemy_2]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] III
   PL: Nakaz [Kartka] III
2. [Słowo kluczowe [IndexPrescriptEnemy_2] — opis] 자신을 포함한 아군이 무작위 수감자를 흐트러뜨리거나 처치한다.\n\n- 턴 시작 시 지령의 가호가 6~8일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_2].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stagger or eliminate a random Sinner, either by you or your ally.\n\n- Turn Start: At 6~8 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Ty lub sojusznik oszołomiasz albo zabijasz losowego Grzesznika.\n\n- Na początku tury, przy 6–8 Łaskach Nakazu\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
3. [Słowo kluczowe [IndexPrescriptEnemy_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_2].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy trafiają do adresatów wieloma drogami, a ich forma — niczym wyrocznia — zostaje im narzucona raz na zawsze, bez prawa wyboru.
4. [Słowo kluczowe [IndexPrescriptEnemy_3] — nazwa] 지령[쪽지] IV
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_3].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptEnemy_3]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] IV
   PL: Nakaz [Kartka] IV
5. [Słowo kluczowe [IndexPrescriptEnemy_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 지령의 가호가 9일 때 얻음
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: At 9 Grace of the Prescript, gain this effect
   PL: Zabija wszystkich wrogów, zanim nadejdzie kolejny Nakaz.\n\n- Na początku tury, przy 9 Łaskach Nakazu
6. [Słowo kluczowe [IndexPrescriptEnemy_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_3].flavor
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
7. [Słowo kluczowe [KarmaOfIndexEnemy] — nazwa] 카르마
   źródło: BattleKeywords-twth.json :: dataList[id=KarmaOfIndexEnemy].name
   kontekst: identyfikator tagu w tekstach: `[KarmaOfIndexEnemy]`
   limit: do 40 znaków
   EN: Karmic Consequence
   PL: Karma
8. [Słowo kluczowe [KarmaOfIndexEnemy] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: BattleKeywords-twth.json :: dataList[id=KarmaOfIndexEnemy].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury:\n· 1 Spadek Poziomu Obrony za każde 10 stosów\n· 1 Wrażliwość za każde 20 stosów\n- Maks. stosów: 100
9. [Słowo kluczowe [KarmaOfIndexEnemy] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: BattleKeywords-twth.json :: dataList[id=KarmaOfIndexEnemy].flavor
   limit: do 200 znaków
   EN: Receive the Prescript and undertake it. Its execution is etched as karma, drawn into a ceaseless cycle that circles back to the hand of its executor.
   PL: Przyjmuje Nakaz i wypełnia go. Wypełnienie staje się karmą, która — krążąc bez końca — nawarstwia się znowu.
10. [Słowo kluczowe [ResentmentSpiderDaughterTwo] — nazwa] <s>중지</s> - 원한
   źródło: BattleKeywords-twth.json :: dataList[id=ResentmentSpiderDaughterTwo].name
   kontekst: identyfikator tagu w tekstach: `[ResentmentSpiderDaughterTwo]`
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle</s> - Grudge
   PL: <s>Środkowy</s> - Uraza
11. [Słowo kluczowe [ResentmentSpiderDaughterTwo] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: BattleKeywords-twth.json :: dataList[id=ResentmentSpiderDaughterTwo].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced when using certain Skills\n- For every Stack, Offense Level +1, Defense Level -2, and Counter Skills deal +5% damage\n- At max Stack, take +20% damage
   PL: - Maks. stosów: 10\n- Zmniejszana przy użyciu określonych Umiejętności\n- Za każdy stos: Poziom Ataku +1, Poziom Obrony -2, Obrażenia Umiejętności Kontratakujących +5%\n- Przy maks. stosach otrzymuje +20% obrażeń
12. [Słowo kluczowe [ReinforcedTattooSpiderDaughterTwo] — nazwa] <s>중지식</s> 강화문신
   źródło: BattleKeywords-twth.json :: dataList[id=ReinforcedTattooSpiderDaughterTwo].name
   kontekst: identyfikator tagu w tekstach: `[ReinforcedTattooSpiderDaughterTwo]`
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle Styled</s> Augmentation Tattoos
   PL: <s>Styl Środkowego</s> - Wzmacniane Tatuaże
13. [Słowo kluczowe [ReinforcedTattooSpiderDaughterTwo] — opis] - 최댓값: 3\n- 타격, 질투 속성의 피해량 +10%
   źródło: BattleKeywords-twth.json :: dataList[id=ReinforcedTattooSpiderDaughterTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 3\n- Zadaje +10% obrażeń atakami Uderzenia i Zazdrości
14. [Słowo kluczowe [HeatingWireOnSpiderTwo] — nazwa] 열선 ON
   źródło: BattleKeywords-twth.json :: dataList[id=HeatingWireOnSpiderTwo].name
   kontekst: identyfikator tagu w tekstach: `[HeatingWireOnSpiderTwo]`
   limit: do 40 znaków
   EN: Thermal Blades ON
   PL: Ostrza Termiczne - ON
15. [Słowo kluczowe [HeatingWireOnSpiderTwo] — opis] 열선 스킬의 코인 적중시 출혈 위력 및 횟수 부여량 만큼 화상 위력 및 횟수 추가 부여
   źródło: BattleKeywords-twth.json :: dataList[id=HeatingWireOnSpiderTwo].desc
   limit: do 170 znaków
   EN: On Hit with Thermal Blade Skill Coins: Additionally inflict Burn Potency and Count equal to Bleed Potency and Count inflicted
   PL: Przy trafieniu monetą Umiejętności Ostrzy Termicznych dodatkowo nadaje Podpalenie (Moc i Licznik) w wysokości nadawanego Krwawienia (Moc i Licznik)

## Słowa kluczowe bitwy — BattleKeywords-walpu10
- plik gry: `BattleKeywords-walpu10.json` (opisy wyświetlane w dymkach pomocy podczas walki)

16. [Słowo kluczowe [Emulation] — nazwa] 본받는 자세
   źródło: BattleKeywords-walpu10.json :: dataList[id=Emulation].name
   kontekst: identyfikator tagu w tekstach: `[Emulation]`
   limit: do 40 znaków
   EN: Learning by Example
   PL: Naśladowanie Przykładu
17. [Słowo kluczowe [Emulation] — opis] 최댓값: 30\n다음 조건에 따라서 수치가 상승\n- 자신이 합 승리 시 수치 2, 기본 공격 스킬 적중 시 수치 1, 공격 종료시 적이 사망했으면, 수치 3 얻음.\n- 자신을 제외한 아군이 기본 공격 스킬로 합 승리 시 수치 2 얻음.\n· 자신과 같은 소속사인 자신을 제외한 아군이 기본 공격 스킬로 합 승리 시 대신 수치 4 얻음.\n\n수치에 따라 다음 효과를 누적하여 적용.\n- 수치 1당, 기본 공격 스킬의 피해량 +1% (최대 30%)\n- 10 이상 : 기본 공격 스킬의 합 위력 +1.\n- 20 이상 : 기본 공격 스킬의 코인 위력 +1.
   źródło: BattleKeywords-walpu10.json :: dataList[id=Emulation].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 30\nGain Stacks based on the following conditions:\n- On Clash Win, gain 2 Stacks; On Hit using Base Attack Skills, gain 1 Stack; At Attack End, if the enemy was defeated, gain 3 Stacks\n- On Clash Win using Base Attack Skills by other allies, gain 2 Stacks\n · On Clash Win using Base Attack Skills by other allies in the same faction as this unit, gain 4 Stacks instead\n\nGain the following effects cumulatively based on Stacks:\n- Base Attack Skills deal +1% damage for every Stack (max 30%)\n- 10+: Base Attack Skills Clash Power +1\n- 20+: Base Attack Skills Coin Power +1
   PL: Maks. stosów: 30\nZyskuje stosy według następujących warunków:\n- Po wygranym Starciu: +2 stosy; przy trafieniu monetą podstawowej Umiejętności ataku: +1 stos; jeśli po zakończeniu ataku wrog ginie: +3 stosy\n- Po wygranym Starciu podstawową Umiejętnością ataku przez sojusznika (poza tą jednostką): +2 stosy\n · Jeśli podstawową Umiejętnością ataku wygra sojusznik tej samej frakcji (poza tą jednostką): zamiast tego +4 stosy\n\nWedług liczby stosów działają kumulatywnie następujące efekty:\n- Za każdy stos podstawowe Umiejętności ataku zadają +1% obrażeń (maks. 30%)\n- Od 10 stosów: Moc Starcia podstawowych Umiejętności ataku +1\n- Od 20 stosów: Moc Monet podstawowych Umiejętności ataku +1
18. [Słowo kluczowe [Emulation] — podsumowanie] 특정 조건에 따라 수치 증가\n수치에 따라 피해량, 합 위력, 코인 위력 증가
   źródło: BattleKeywords-walpu10.json :: dataList[id=Emulation].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Stacks based on certain conditions\nDeal more damage, gain Clash Power, gain Coin Power based on Stacks
   PL: Zyskuje stosy pod pewnymi warunkami\nWedług stosów: większe obrażenia, Moc Starcia i Moc Monet
19. [Słowo kluczowe [CursedBlessing] — nazwa] 절망의 시험
   źródło: BattleKeywords-walpu10.json :: dataList[id=CursedBlessing].name
   kontekst: identyfikator tagu w tekstach: `[CursedBlessing]`
   limit: do 40 znaków
   EN: A Test of Despair
   PL: Próba Rozpaczy
20. [Słowo kluczowe [CursedBlessing] — opis] - 모든 슬롯의 도발치 20 증가\n- 공격 스킬 사용 시 정신력 20 감소\n- 사망 시 자신을 제외한 모든 아군 정신력 20 감소
   źródło: BattleKeywords-walpu10.json :: dataList[id=CursedBlessing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All Slots gain +20 Aggro\n- On Attack Skill Use, lose 20 SP\n- On Death, all other allies lose 20 SP
   PL: - Prowokacja slotów +20\n- Umiejętność ataku: traci 20 Poczytalności\n- Po śmierci pozostali sojusznicy tracą 20 Poczytalności
21. [Słowo kluczowe [BeyondDespair] — nazwa] 절망을 넘어선 자
   źródło: BattleKeywords-walpu10.json :: dataList[id=BeyondDespair].name
   kontekst: identyfikator tagu w tekstach: `[BeyondDespair]`
   limit: do 40 znaków
   EN: The One Beyond Despair
   PL: Ten, Który Przekroczył Rozpacz
22. [Słowo kluczowe [BeyondDespair] — opis] - 턴 시작 시 보호 2, 공격 위력 증가 1 얻음\n- 수비 스킬 사용 시 수비 위력 증가 3 얻음 (턴당 1회)\n- 합 승리 시 정신력 5 회복 (턴당 2회)\n· 정신력이 최대치이면, 자신이 보유한 해제 가능한 부정적인 효과 1개 제거\n- 기본 스킬 종료 시 해당 스킬이 각 적에게 가한 피해량 10%만큼 오만 피해\n\n- 체력이 0이 되는 피해를 받으면, 해당 턴 피해를 받지 않음 (전투당 1회)\n· 위 효과가 발동한 다음 턴에 체력을 모두 회복하고, 전투 종료 시까지 자신의 보호 수치 1당, 가하는 피해량 +10% (최대 80%)
   źródło: BattleKeywords-walpu10.json :: dataList[id=BeyondDespair].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Protection and 1 Attack Power Up\n- On Defense Skill Use, gain 3 Defense Power Up (once per turn)\n- On Clash Win, heal 5 SP (2 times per turn)\n · At max SP, remove 1 removable negative effect applied to self\n- At Base Skill End, deal Pride damage equal to 10% of damage the said Skill dealt to each enemy\n\n- When this unit takes damage that brings its HP down to 0, it does not take damage for the turn (once per Encounter)\n · After the above effect activates, heal all HP next turn; then, deal +10% damage for every Protection on self until Combat End (max 80%)
   PL: - Na początku tury zyskuje 2 Ochrony i 1 Wzrost Mocy Ataku\n- Przy użyciu Umiejętności obrony zyskuje 3 Wzrosty Mocy Obrony (1 na turę)\n- Po wygranym Starciu odzyskuje 5 Poczytalności (2 na turę)\n · Przy maks. Poczytalności usuwa 1 usuwalny negatywny efekt nakładony na siebie\n- Po zakończeniu podstawowej Umiejętności zadaje każdemu wrogowi obrażenia Pychą równe 10% obrażeń zadanych przez nią\n\n- Gdy otrzymuje obrażenia obniżające jego HP do 0, nie przyjmuje ich w tej turze (1 na spotkanie)\n · W następnej turze po wywołaniu tego efektu w pełni leczy HP, a do końca walki zadaje +10% obrażeń za każdą Ochronę na sobie (maks. 80%)
23. [Słowo kluczowe [EmbeddedSpearhead] — nazwa] 박힌 창날
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmbeddedSpearhead].name
   kontekst: identyfikator tagu w tekstach: `[EmbeddedSpearhead]`
   limit: do 40 znaków
   EN: Embedded Spearhead
   PL: Wbite Ostrze Włóczni
24. [Słowo kluczowe [EmbeddedSpearhead] — opis] - 최댓값: 1\n- 이 효과를 부여한 대상 이외의 대상에게 관통 기본 공격 스킬로 크리티컬 피격 시, 받는 피해량 +15%\n- '연' 효과가 있는 스킬로 피격 시, 받는 피해량 + 20% 추가\n- 피격한 스킬 종료 후 소멸
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmbeddedSpearhead].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- On Crit using Pierce Base Attack Skills by targets other than the target that inflicted this effect, take +15% damage\n- When hit by Skills that have the "Joint Combo" effect, take an additional +20% damage\n- At Skill End of the Skill that hit, expires
   PL: - Maks. stosów: 1\n- Gdy krytycznie trafi ją podstawowa Umiejętność ataku Przebicia od celu innego niż ten, który nałożył ten efekt, otrzymuje +15% obrażeń\n- Przy trafieniu Umiejętnością z efektem „Łączenia” otrzymuje dodatkowo +20% obrażeń\n- Znika po zakończeniu Umiejętności, która trafiła
25. [Słowo kluczowe [WalpuTenWedgeOffice] — nazwa] 쐐기 사무소
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeOffice].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenWedgeOffice]`
   limit: do 40 znaków
   EN: Wedge Office
   PL: Biuro Klina
26. [Słowo kluczowe [WalpuTenWedgeOffice] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 턴 시작 시 관통 피해량 증가 1 얻음\n- 턴 시작 시 자신을 제외하고 ‘쐐기 사무소’를 보유한 아군이 모두 사망했으면 소멸
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeOffice].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack\n- Turn Start: At 3 Stacks, gain 1 Pierce DMG Up\n- Turn Start: If all other allies that have "Wedge Office" are defeated, this effect expires
   PL: - Maks. stosów: 3\n- Poziom Ataku +1 za każdy stos\n- Od 3 stosów: na początku tury zyskuje 1 Wzrost Obrażeń Przebicia\n- Na początku tury, jeśli wszyscy inni sojusznicy z „Biurem Klina” nie żyją, efekt znika
27. [Słowo kluczowe [WalpuTenComboWedge] — nazwa] 승기
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenComboWedge].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenComboWedge]`
   limit: do 40 znaków
   EN: Momentum
   PL: Przewaga
28. [Słowo kluczowe [WalpuTenComboWedge] — opis] - 최댓값 : 30\n- 특정 스킬에서 소모\n- 턴당 최대 20까지 얻을 수 있음
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenComboWedge].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Consumed by certain Skills\n- Can gain up to 20 Stacks per turn
   PL: - Maks. stosów: 30\n- Zużywana przez określone Umiejętności\n- Można zyskać do 20 stosów na turę
29. [Słowo kluczowe [WalpuTenBattleFieldKnow] — nazwa] 전장 파악
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenBattleFieldKnow].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenBattleFieldKnow]`
   limit: do 40 znaków
   EN: Field Analysis
   PL: Analiza Pola Bitwy
30. [Słowo kluczowe [WalpuTenBattleFieldKnow] — opis] - 최대값: 4\n- 이 효과를 얻을 때, 자신의 호흡 횟수 2 증가\n- 턴 종료 시 (수치 x 2)만큼 자신의 호흡 횟수 증가\n- 이 효과 수치에 따라 스킬이 아래 효과 얻음\n· 1 ~ : 적에게 가하는 피해량 +(수치 x 2.5)%\n· 2 ~ : 합 진행 시 2합당, 합 위력 +1 (최대 2)\n· 3 ~ : 코인 위력 +1, 마지막 코인이 파괴 불가 코인이 됨\n· 4 ~ : 공격 종료 시까지 공격 대상의 관통 내성 +0.1
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenBattleFieldKnow].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Gain +2 Poise Count when gaining this effect\n- Turn End: Gain +(Stack x 2) Poise Count\n- Skills gain the following effects based on Stack:\n · 1+: Deal +(Stack x 2.5)% damage against enemies\n · 2+: In a Clash, Clash Power +1 for every 2 Clashes (max 2)\n · 3+: Coin Power +1, the final Coin becomes Unbreakable Coin\n · 4+: Target's Pierce Resist. +0.1 until Attack End
   PL: - Maks. stosów: 4\n- Przy uzyskaniu tego efektu zyskuje +2 Licznika Oddechu\n- Na koniec tury zyskuje +(stosy x 2) Licznika Oddechu\n- Według liczby stosów Umiejętności zyskują:\n · Od 1: +(stosy x 2,5)% obrażeń zadanych wrogom\n · Od 2: podczas Starcia Moc Starcia +1 za każde 2 Starcia (maks. 2)\n · Od 3: Moc Monet +1, a ostatnia moneta staje się monetą niezniszczalną\n · Od 4: do końca ataku Odporność celu na Przebicie +0,1
31. [Słowo kluczowe [WalpuTenWedgeMarkSilver] — nazwa] 은색 표식[쐐기]
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeMarkSilver].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenWedgeMarkSilver]`
   limit: do 40 znaków
   EN: Silver Mark [Wedge]
   PL: Srebrne Oznaczenie [Klin]
32. [Słowo kluczowe [WalpuTenWedgeMarkSilver] — opis] - 최댓값 : 5\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 진영에 쐐기 사무소 소속이 없으면, 이 효과 소멸
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeMarkSilver].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: Gain +1 Tremor Count\n- Turn Start: If there are no "Wedge Office" enemies on the field, this effect expires
   PL: - Maks. stosów: 5\n- Na koniec tury zyskuje +1 Licznika Wstrząsu\n- Na początku tury, jeśli na polu nie ma wrogów z „Biura Klina”, efekt znika
33. [Słowo kluczowe [WalpuTenWedgeMarkGold] — nazwa] 금색 표식[쐐기]
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeMarkGold].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenWedgeMarkGold]`
   limit: do 40 znaków
   EN: Golden Mark [Wedge]
   PL: Złote Oznaczenie [Klin]
34. [Słowo kluczowe [WalpuTenWedgeMarkGold] — opis] - 최댓값 : 5\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 진영에 쐐기 사무소 소속이 없으면, 이 효과 소멸
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenWedgeMarkGold].desc
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Słowo kluczowe [DawnOfficeStigmaSOne] — nazwa] 새벽불
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaSOne]`
   limit: do 40 znaków
   EN: Light of Daybreak
   PL: Płomień Świtu
36. [Słowo kluczowe [DawnOfficeStigmaSOne] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start: Gain 1 Burn for every 5 Stacks\n- Turn Start: Gain +1 Burn Count for every 10 Stacks\n- At 10+ Stacks, inflict +1 more Burn Potency using Base Skills against the enemy\n- At 20+ Stacks, inflict +1 more Burn Count using Base Skills against the enemy
   PL: - Maks. stosów: 30\n- Na początku tury zyskuje 1 Podpalenie za każde 5 stosów\n- Na początku tury zyskuje +1 Licznika Podpalenia za każde 10 stosów\n- Od 10 stosów podstawowe Umiejętności nadają wrogom +1 więcej Mocy Podpalenia\n- Od 20 stosów podstawowe Umiejętności nadają wrogom +1 więcej Licznika Podpalenia
37. [Słowo kluczowe [DawnOfficeStigmaSOne] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSOne].flavor
   limit: do 120 znaków
   EN: The first flare of dawn is not a fire that scorches, but one that casts its glow on people.
   PL: Ogień rozjaśniający świt nie służy do wypalania — to ogień, który oświetla ludzi.
38. [Słowo kluczowe [DawnOfficeStigmaSTwo] — nazwa] 새벽불
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaSTwo]`
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
39. [Słowo kluczowe [DawnOfficeStigmaSTwo] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
40. [Słowo kluczowe [DawnOfficeStigmaSTwo] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSTwo].flavor
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Słowo kluczowe [DawnOfficeStigmaSThree] — nazwa] 새벽불
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaSThree]`
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Słowo kluczowe [DawnOfficeStigmaSThree] — opis] - 최댓값 : 30\n- 턴 시작 시 수치 5당 화상을 1 얻음\n- 턴 시작 시 수치 10당 자신의 화상 횟수 1 증가\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Słowo kluczowe [DawnOfficeStigmaSThree] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaSThree].flavor
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Słowo kluczowe [DawnOfficeStigmaYOne] — nazwa] 불꽃나비의 관
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaYOne]`
   limit: do 40 znaków
   EN: Fire Butterfly Coffin
   PL: Trumna Ognistych Motyli
45. [Słowo kluczowe [DawnOfficeStigmaYOne] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- On Hit using Base Skills, gain 3 Stacks\n · If the said Skill is Skill 1 used via the "Dawn Office - Seonbae" Passive, gain 1 more Stack\n · If target has Burn, gain 1 more Stack\n- Turn End: At more than 20 Stacks, gain (excess Stack / 2) Burn next turn (rounded down)\n · At 30 Stacks, gain 5 Burn and +2 Burn Count instead
   PL: - Maks. stosów: 30\n- Przy trafieniu podstawową Umiejętnością zyskuje 3 stosy\n · Jeśli to Umiejętność 1 użyta przez pasyw „Biuro Świtu - Seonbae”, dodatkowo +1 stos\n · Jeśli cel ma Podpalenie, dodatkowo +1 stos\n- Na koniec tury, powyżej 20 stosów, w następnej turze otrzymuje Podpalenie równe połowie nadwyżki (zaokrąglone w dół)\n · Przy 30 stosach zamiast tego otrzymuje 5 Podpalenia i +2 Licznika Podpalenia
46. [Słowo kluczowe [DawnOfficeStigmaYOne] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYOne].flavor
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heated to a smoldering temperature within the coffin are butterflies, the kaleidoscope spilling forth to melt and tear the target apart.\n\n"This type of weapon is still too premature for you to wield, Philip, but it shouldn't hurt to at least learn how it works."\n\n"All those blades inside the coffin make it much easier to deal with multiple opponents at once. That way, you can even take on jobs that would normally be too much for a single Fixer to handle."
   PL: Rozgrzane do żaru w trumnie motyle wylatują rojem i topią, rozrywając cel.\n\n“Philipie, to broń jeszcze zbyt wczesna dla ciebie, ale poznanie jej działania z wyprzedzeniem niczego nie zaszkodzi.”\n“Dzięki ostrzom ukrytym w trumnie łatwiej radzę sobie z wieloma przeciwnikami naraz. Mogę nawet przyjmować zlecenia, z którymi pojedynczy Fixer zwykle sobie nie poradzi.”
47. [Słowo kluczowe [DawnOfficeStigmaYTwo] — nazwa] 불꽃나비의 관
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaYTwo]`
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Słowo kluczowe [DawnOfficeStigmaYTwo] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Słowo kluczowe [DawnOfficeStigmaYTwo] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYTwo].flavor
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Słowo kluczowe [DawnOfficeStigmaYThree] — nazwa] 불꽃나비의 관
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].name
   kontekst: identyfikator tagu w tekstach: `[DawnOfficeStigmaYThree]`
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Słowo kluczowe [DawnOfficeStigmaYThree] — opis] - 최댓값 : 30\n- 기본 스킬 적중시 3 얻음\n· 새벽 사무소 - 선배 패시브로 사용하는 스킬 1이면, 1 추가로 얻음\n· 대상에게 화상이 있으면, 1 추가로 얻음\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].desc
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Słowo kluczowe [DawnOfficeStigmaYThree] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n\n“필립, 너에겐 아직 이른 무기지만, 특성을 미리 공부하는 것도 괜찮겠네..”\n“관 속에 있는 여러 칼날 덕에 여러 명을 상대할 때 편해. 보통은 혼자 수행하기 어려운 의뢰도 맡을 수 있고.”
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOfficeStigmaYThree].flavor
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [Słowo kluczowe [LoneFixer] — nazwa] 고독한 해결사
   źródło: BattleKeywords-walpu10.json :: dataList[id=LoneFixer].name
   kontekst: identyfikator tagu w tekstach: `[LoneFixer]`
   limit: do 40 znaków
   EN: The Lone Fixer
   PL: Samotny Fixer
54. [Słowo kluczowe [LoneFixer] — opis] - 최종 위력 +3\n- 공격 레벨 +3\n- 방어 레벨 +3
   źródło: BattleKeywords-walpu10.json :: dataList[id=LoneFixer].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +3\n- Offense Level +3\n- Defense Level +3
   PL: - Moc Końcowa +3\n- Poziom Ataku +3\n- Poziom Obrony +3
55. [Słowo kluczowe [PhilipReady] — nazwa] 타오르는 일격 준비
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipReady].name
   kontekst: identyfikator tagu w tekstach: `[PhilipReady]`
   limit: do 40 znaków
   EN: Readying Blazing Strike
   PL: Przygotowanie Płonącego Ciosu
56. [Słowo kluczowe [PhilipReady] — opis] 일정 턴 후에 타오르는 일격 사용
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipReady].desc
   limit: do 120 znaków
   EN: Use "Blazing Strike" after a certain number of turns
   PL: Po upływie określonej liczby tur używa „Płonącego Ciosu”
57. [Słowo kluczowe [PhilipShield] — nazwa] 깃털 방패
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipShield].name
   kontekst: identyfikator tagu w tekstach: `[PhilipShield]`
   limit: do 40 znaków
   EN: Feather Shield
   PL: Tarcza z Piór
58. [Słowo kluczowe [PhilipShield] — opis] - 피격 시 공격자에게 화상 2 부여\n- 공격으로 받는 피해 5% 감소
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipShield].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When hit, inflict 2 Burn on the attacker\n- Take -5% damage from Attack Skills
   PL: - Przy trafieniu nadaje atakującemu 2 Podpalenia\n- Otrzymuje -5% obrażeń od ataków
59. [Słowo kluczowe [PhilipSword] — nazwa] 이글거리는 검
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipSword].name
   kontekst: identyfikator tagu w tekstach: `[PhilipSword]`
   limit: do 40 znaków
   EN: Searing Sword
   PL: Kipiący Miecz
60. [Słowo kluczowe [PhilipSword] — opis] 공격 적중시 대상에게 화상 2 부여
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipSword].desc
   limit: do 120 znaków
   EN: On Hit, inflict 2 Burn
   PL: Przy trafieniu nadaje celowi 2 Podpalenia
61. [Słowo kluczowe [PhilipPower] — nazwa] 슬픔과 함께 일어설 수 있는 길
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipPower].name
   kontekst: identyfikator tagu w tekstach: `[PhilipPower]`
   limit: do 60 znaków
   EN: Getting Back on One's Feet Amid Sadness
   PL: Droga Powstania w Smutku
62. [Słowo kluczowe [PhilipPower] — opis] - 자신의 스킬 종료 후 정신력 5 회복\n- 진동을 보유한 적에게 가하는 피해량 +20%\n- 턴 시작시 흐트러짐 상태면, 흐트러짐을 해제하고 해당 턴 동안 자신의 모든 내성을 1.5로 고정함
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipPower].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At Skill End, heal 5 SP\n- Deal +20% damage to enemies that have Tremor\n- Turn Start: When Staggered, recover from Stagger; then, all Resist. on self are fixed to 1.5 for the turn
   PL: - Po zakończeniu Umiejętności odzyskuje 5 Poczytalności\n- Zadaje +20% obrażeń wrogom z Wstrząsem\n- Na początku tury, jeśli jest oszołomiony, wychodzi z Oszołomienia, a wszystkie jego Odporności są przez tę turę ustalone na 1,5
63. [Słowo kluczowe [PhilipPower] — tekst klimatyczny] ‘그 누구보다 슬퍼하고 있는 나를 위해서…’
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipPower].flavor
   limit: do 120 znaków
   EN: 'For me, who's feeling sadder than anyone...'
   PL: ‚…dla mnie, który smuci się bardziej niż ktokolwiek inny…’
64. [Słowo kluczowe [PhilipWax] — nazwa] 불확실한 슬픔의 감정
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipWax].name
   kontekst: identyfikator tagu w tekstach: `[PhilipWax]`
   limit: do 40 znaków
   EN: Emotion of Uncertain Sorrow
   PL: Emocja Niepewnego Smutku
65. [Słowo kluczowe [PhilipWax] — opis] - 최댓값 : 5\n- 수치 1당 화상 위력 최댓값 +10\n· 이 효과 감소 및 소멸 시, 초과되는 화상 위력은 소멸함\n- 수치 1당 화상 발동으로 받는 피해 +10%\n- 화상 발동 시 1 감소
   źródło: BattleKeywords-walpu10.json :: dataList[id=PhilipWax].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Burn Potency Cap +10 for every Stack\n · When this effect expires or is reduced, the surplus Burn Potency expires\n- Take +10% damage from Burn activation for every Stack\n- When Burn activates, lose 1 Stack
   PL: - Maks. stosów: 5\n- Za każdy stos Maks. Moc Podpalenia +10\n · Gdy efekt maleje lub znika, nadwyżka Mocy Podpalenia znika\n- Za każdy stos otrzymuje +10% obrażeń przy aktywacji Podpalenia\n- Przy aktywacji Podpalenia traci 1 stos
66. [Słowo kluczowe [PatronLibrarianofHistorysPage] — nazwa] 지정 사서 [역사의 층]
   źródło: BattleKeywords-walpu10.json :: dataList[id=PatronLibrarianofHistorysPage].name
   kontekst: identyfikator tagu w tekstach: `[PatronLibrarianofHistorysPage]`
   limit: do 50 znaków
   EN: Patron Librarian [Floor of History]
   PL: Wyznaczony Bibliotekarz [Piętro Historii]
67. [Słowo kluczowe [PatronLibrarianofHistorysPage] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동을 부여할 때, 부여값 +1(특수 상태이상 포함)\n- 자신이 스킬로 호흡, 충전(특수 충전)을 얻을 때, 부여값 +1\n- 관통 속성 스킬 사용시 피해량 +30%\n- 스킬 적중시 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 +1 (스킬당 2회)
   źródło: BattleKeywords-walpu10.json :: dataList[id=PatronLibrarianofHistorysPage].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1, lose 1 use of Skill 1, gain 1 use of Skill 3\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor inflicted using Skills by +1 (including Unique Status Effects)\n- Increase the amount of Poise or Charge (including Unique Charge) gained from Skills by +1\n- Pierce Skills deal +30% damage On Use\n- On Hit using Skills, gain 1 random least-owned E.G.O resource (2 times per Skill)
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Podpalenie, Krwawienie, Rozdarcie, Zatonięcie lub Wstrząs, wartość nadania +1 (również szczególne stany)\n- Gdy Umiejętnościami zyskuje Oddech lub Ładowanie (również szczególne ładowanie), wartość +1\n- Umiejętności Przebicia zadają +30% obrażeń przy użyciu\n- Przy trafieniu Umiejętnością zyskuje +1 losowego zasobu E.G.O, którego ma najmniej (2 na Umiejętność)
68. [Słowo kluczowe [EmotionLevelZero] — nazwa] 감정 0단계
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelZero].name
   kontekst: identyfikator tagu w tekstach: `[EmotionLevelZero]`
   limit: do 40 znaków
   EN: Emotion Level 0
   PL: Poziom Emocji 0
69. [Słowo kluczowe [EmotionLevelZero] — opis] - 최댓값 : 30\n- 모든 아군의 감정 단계 수치가 9가 될 때까지 9 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 9면, 1 추가로 얻고 감정 단계 증가
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelZero].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Does not increase beyond 9 Stacks until all allies are at 9 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 9 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage
   PL: - Maks. stosów: 30\n- Nie rośnie powyżej 9 stosów, dopóki wszyscy sojusznicy nie osiągną 9 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 9 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji
70. [Słowo kluczowe [EmotionLevelOne] — nazwa] 감정 1단계
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelOne].name
   kontekst: identyfikator tagu w tekstach: `[EmotionLevelOne]`
   limit: do 40 znaków
   EN: Emotion Level 1
   PL: Poziom Emocji 1
71. [Słowo kluczowe [EmotionLevelOne] — opis] - 최댓값 : 30\n- 최종 위력 +1\n- 모든 아군의 감정 단계 수치가 19가 될 때까지 19 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 19면, 1 추가로 얻고 감정 단계 증가\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelOne].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +1\n- Does not increase beyond 19 Stacks until all allies are at 19 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 19 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)
   PL: - Maks. stosów: 30\n- Moc Końcowa +1\n- Nie rośnie powyżej 19 stosów, dopóki wszyscy sojusznicy nie osiągną 19 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 19 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)
72. [Słowo kluczowe [EmotionLevelTwo] — nazwa] 감정 2단계
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelTwo].name
   kontekst: identyfikator tagu w tekstach: `[EmotionLevelTwo]`
   limit: do 40 znaków
   EN: Emotion Level 2
   PL: Poziom Emocji 2
73. [Słowo kluczowe [EmotionLevelTwo] — opis] - 최댓값 : 30\n- 최종 위력 +2\n- 모든 아군의 감정 단계 수치가 29가 될 때까지 29 초과로 증가하지 않음\n- 합 승리 시, 코인 앞면 적중 시, 적 처치 시 3 증가\n- 합 패배, 코인 뒷면 적중 시, 아군 사망 시 1 증가\n- 턴 종료시 모든 아군의 감정 단계 수치가 29면, 1 추가로 얻고 감정 단계 증가\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)\n- 그리웠던 옛날의 포옹 : 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelTwo].desc
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +2\n- Does not increase beyond 29 Stacks until all allies are at 29 Emotion Level Stacks\n- Gain 3 Stacks On Clash Win, On Heads Hit, and On Kill\n- Gain 1 Stack On Clash Lose, On Tails Hit, and on Ally Death\n- Turn End: If all allies are at 29 Emotion Level Stacks, gain 1 more Stack and increase Emotion Level stage\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)\n- Nostalgic Embrace of the Old Days: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)
   PL: - Maks. stosów: 30\n- Moc Końcowa +2\n- Nie rośnie powyżej 29 stosów, dopóki wszyscy sojusznicy nie osiągną 29 stosów Poziomu Emocji\n- +3 stosy po wygranym Starciu, trafieniu awersem monety i zabiciu wroga\n- +1 stos po przegranej w Starciu, trafieniu rewersem monety i śmierci sojusznika\n- Na koniec tury, jeśli wszyscy sojusznicy mają 29 stosów Poziomu Emocji, zyskuje +1 stos i przechodzi do kolejnego etapu emocji\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)\n- Tęskny Uścisk Dawnych Dni: po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)
74. [Słowo kluczowe [EmotionLevelThree] — nazwa] 감정 3단계
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelThree].name
   kontekst: identyfikator tagu w tekstach: `[EmotionLevelThree]`
   limit: do 40 znaków
   EN: Emotion Level 3
   PL: Poziom Emocji 3
75. [Słowo kluczowe [EmotionLevelThree] — opis] - 최댓값 : 30\n- 최종 위력 +3\n\n[지정 사서 전용 효과]\n- 재 : 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)\n- 그리웠던 옛날의 포옹 : 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)\n- 식탐 : 자신의 공격 대상이 이번 턴에 피해를 받았다면, 적중 시 피해량이 1-3 증가하고, 체력을 2-5 회복함
   źródło: BattleKeywords-walpu10.json :: dataList[id=EmotionLevelThree].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Final Power +3\n\n[Patron Librarian Exclusive Effect]\n- Ashes: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)\n- Nostalgic Embrace of the Old Days: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)\n- Gluttony: If this unit's attack target has taken damage this turn, deal 1-3 additional damage On Hit and heal 2-5 HP
   PL: - Maks. stosów: 30\n- Moc Końcowa +3\n\n[Efekt wyznaczonego Bibliotekarza]\n- Popiół: przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)\n- Tęskny Uścisk Dawnych Dni: po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)\n- Łakomstwo: jeśli cel ataku otrzymał w tej turze obrażenia, przy trafieniu zadaje 1–3 obrażeń dodatkowych i leczy 2–5 HP
76. [Słowo kluczowe [WalpuTenHard] — nazwa] 어려움 난이도
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenHard].name
   kontekst: identyfikator tagu w tekstach: `[WalpuTenHard]`
   limit: do 40 znaków
   EN: Hard Difficulty
   PL: Poziom Trudności: Trudny
77. [Słowo kluczowe [WalpuTenHard] — opis] - 최대 체력 50% 증가\n- 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제\n- 공격 레벨 +3\n- 화상, 출혈, 진동, 파열, 침잠의 위력이 최대 30까지 누적되고 횟수는 최대 10까지 누적됨\n- 출혈, 진동, 파열, 침잠으로 받는 피해량 -30%
   źródło: BattleKeywords-walpu10.json :: dataList[id=WalpuTenHard].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +50%\n- Remove the first Stagger Threshold\n- Offense Level +3\n- Max Potency cap for Burn, Bleed, Tremor, Rupture, Sinking: 30\n- Max Count cap for Burn, Bleed, Tremor, Rupture, Sinking: 10\n- Take -30% damage from Bleed, Tremor, Rupture, Sinking
   PL: - Maks. HP +50%\n- Usuwa pierwszy Próg Oszołomienia\n- Poziom Ataku +3\n- Maks. Mocy Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia: 30\n- Maks. Liczników Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia: 10\n- Otrzymuje -30% obrażeń od Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
78. [Słowo kluczowe [HistoryAshes] — nazwa] 도서관의 책장 - 재
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryAshes].name
   kontekst: identyfikator tagu w tekstach: `[HistoryAshes]`
   limit: do 40 znaków
   EN: Pages of the Library - Ashes
   PL: Karta Biblioteki - Popiół
79. [Słowo kluczowe [HistoryAshes] — opis] 피격 시 공격자에게 화상을 1~3 부여. 피격 시 40% 확률로 다음 턴 동안 '스킬 적중 시 화상 1 부여' 능력을 얻음 (중첩불가)
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryAshes].desc
   limit: do 200 znaków
   EN: When hit, inflict 1~3 Burn on the attacker and 40% chance to gain the "On Hit using Skills, inflict 1 Burn" effect for the next turn (does not Stack)
   PL: Przy trafieniu nadaje atakującemu 1–3 Podpalenia, a z 40% szansą zyskuje na następną turę zdolność „Przy trafieniu Umiejętnością nadaje 1 Podpalenie” (bez kumulowania)
80. [Słowo kluczowe [HistoryAshes] — tekst klimatyczny] “까맣게 타버린 몸은 그 아이의 부서진 희망, 그럼에도 여전히 타오르는 촛불은 애정을 갈구하는 집착이라고 볼 수 있습니다.”
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryAshes].flavor
   limit: do 170 znaków
   EN: "The charred body represents the child's crumbled hope, while the ever-blazing flame represents the obsession for affection."
   PL: “Zwęglone ciało wyobraża rozpadłe nadzieje dziecka, a wiecznie płonący płomień — obsesję pragnącą czułości.”
81. [Słowo kluczowe [HistoryNostalgicEmbraceOfTheOldDays] — nazwa] 도서관의 책장 - 그리웠던 옛날의 포옹
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].name
   kontekst: identyfikator tagu w tekstach: `[HistoryNostalgicEmbraceOfTheOldDays]`
   limit: do 80 znaków
   EN: Pages of the Library - Nostalgic Embrace of the Old Days
   PL: Karta Biblioteki - Tęskny Uścisk Dawnych Dni
82. [Słowo kluczowe [HistoryNostalgicEmbraceOfTheOldDays] — opis] 합 승리 시 20% 확률로 대상에게 진동 폭발. 동일한 대상과 합을 할수록 확률이 증가함 (1합당 2%, 최대 50%)
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].desc
   limit: do 190 znaków
   EN: On Clash Win, 20% chance to trigger Tremor Burst on target; chance increases with every Clash against the same target (2% for every Clash, max 50%)
   PL: Po wygranym Starciu 20% szans na wywołanie Wybuchu Wstrząsu u celu; szansa rośnie z każdym Starciem z tym samym celem (2% na Starcie, maks. 50%)
83. [Słowo kluczowe [HistoryNostalgicEmbraceOfTheOldDays] — tekst klimatyczny] 테디가 누군가를 꽉 껴안고 있었죠. 테디는 포옹을 매우 좋아했거든요. 그런데 조금 이상했어요.
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryNostalgicEmbraceOfTheOldDays].flavor
   limit: do 120 znaków
   EN: Teddy was hugging someone tightly. Teddy loved hugs. But something was odd.
   PL: Teddy mocno przytulał kogoś. Teddy bardzo lubił przytulanie. Ale coś było w tym dziwnego.
84. [Słowo kluczowe [HistoryGluttony] — nazwa] 도서관의 책장 - 식탐
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryGluttony].name
   kontekst: identyfikator tagu w tekstach: `[HistoryGluttony]`
   limit: do 50 znaków
   EN: Pages of the Library - Gluttony
   PL: Karta Biblioteki - Łakomstwo
85. [Słowo kluczowe [HistoryGluttony] — opis] 자신의 공격 대상이 이번 턴에 피해를 받았다면, 적중 시 피해량이 1-3 증가하고, 체력을 2-5 회복함
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryGluttony].desc
   limit: do 140 znaków
   EN: If this unit's attack target has taken damage this turn, deal 1-3 additional damage On Hit and heal 2-5 HP
   PL: Jeśli cel ataku otrzymał w tej turze obrażenia, przy trafieniu zadaje 1–3 obrażeń dodatkowych i leczy 2–5 HP
86. [Słowo kluczowe [HistoryGluttony] — tekst klimatyczny] 요정들은 단지 고기를 좋아하는 괴물이었고, '보호하는' 행위는 고기의 신선도가 떨어지는 걸 방지하기 위해서였다.
   źródło: BattleKeywords-walpu10.json :: dataList[id=HistoryGluttony].flavor
   limit: do 150 znaków
   EN: The fairies were no more than carnivorous monsters, and their "protection" was their method to keep the meat fresh.
   PL: Wróżki były jedynie mięsożernymi potworami, a ich „ochrona” służyła utrzymaniu świeżości mięsa.
87. [Słowo kluczowe [DawnOffice_LowMorale] — nazwa] 새벽 사무소
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOffice_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DawnOffice_LowMorale]`
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu
88. [Słowo kluczowe [DawnOffice_LowMorale] — opis] - 사기 저하\n- 화상이 있는 적에게 가하는 피해량 -5%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOffice_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -5% damage to enemies that have Burn\n- +5% to Stagger Threshold raised against enemies that have Tremor
   PL: - Spadek Moralu\n- Zadaje -5% obrażeń wrogom z Podpaleniem\n- +5% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
89. [Słowo kluczowe [DawnOffice_Panic] — nazwa] 새벽 사무소
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOffice_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DawnOffice_Panic]`
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Słowo kluczowe [DawnOffice_Panic] — opis] - 패닉\n- 화상이 있는 적에게 가하는 피해량 -10%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: BattleKeywords-walpu10.json :: dataList[id=DawnOffice_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal -10% damage to enemies that have Burn\n- +10% to Stagger Threshold raised against enemies that have Tremor
   PL: - Panika\n- Zadaje -10% obrażeń wrogom z Podpaleniem\n- +10% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
91. [Słowo kluczowe [WedgeOffice_LowMorale] — nazwa] 쐐기 사무소
   źródło: BattleKeywords-walpu10.json :: dataList[id=WedgeOffice_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WedgeOffice_LowMorale]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Słowo kluczowe [WedgeOffice_LowMorale] — opis] - 사기 저하\n- 크리티컬 피해량 -5%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: BattleKeywords-walpu10.json :: dataList[id=WedgeOffice_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -5% damage on Critical Hit\n- +5% to Stagger Threshold raised against enemies that have Tremor
   PL: - Spadek Moralu\n- Zadaje -5% obrażeń krytycznych\n- +5% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
93. [Słowo kluczowe [WedgeOffice_Panic] — nazwa] 쐐기 사무소
   źródło: BattleKeywords-walpu10.json :: dataList[id=WedgeOffice_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WedgeOffice_Panic]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Słowo kluczowe [WedgeOffice_Panic] — opis] - 패닉\n- 크리티컬 피해량 -10%\n- 진동이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: BattleKeywords-walpu10.json :: dataList[id=WedgeOffice_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal -10% damage on Critical Hit\n- +10% to Stagger Threshold raised against enemies that have Tremor
   PL: - Panika\n- Zadaje -10% obrażeń krytycznych\n- +10% do Progu Oszołomienia podnoszonego wrogom z Wstrząsem
95. [Słowo kluczowe [WaxWing_LowMorale] — nazwa] 밀랍날개
   źródło: BattleKeywords-walpu10.json :: dataList[id=WaxWing_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WaxWing_LowMorale]`
   limit: do 40 znaków
   EN: Waxen Pinion
   PL: Woskowe Skrzydło
96. [Słowo kluczowe [WaxWing_LowMorale] — opis] - 사기 저하\n- 취약 1 얻음\n- 화상이 있는 적에게 가하는 피해량 +10%
   źródło: BattleKeywords-walpu10.json :: dataList[id=WaxWing_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile\n- Deal +10% damage to enemies that have Burn
   PL: - Spadek Moralu\n- Zyskuje 1 Wrażliwość\n- Zadaje +10% obrażeń wrogom z Podpaleniem
97. [Słowo kluczowe [WaxWing_Panic] — nazwa] 밀랍날개
   źródło: BattleKeywords-walpu10.json :: dataList[id=WaxWing_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WaxWing_Panic]`
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Słowo kluczowe [WaxWing_Panic] — opis] - 패닉\n- 취약 1 얻음\n- 화상이 있는 적에게 가하는 피해량 +25%
   źródło: BattleKeywords-walpu10.json :: dataList[id=WaxWing_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Fragile\n- Deal +25% damage to enemies that have Burn
   PL: - Panika\n- Zyskuje 1 Wrażliwość\n- Zadaje +25% obrażeń wrogom z Podpaleniem

## Słowa kluczowe bitwy — BattleKeywords-walpu4
- plik gry: `BattleKeywords-walpu4.json` (opisy wyświetlane w dymkach pomocy podczas walki)

99. [Słowo kluczowe [RedEyeFirst] — nazwa] 적안
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeFirst].name
   kontekst: identyfikator tagu w tekstach: `[RedEyeFirst]`
   limit: do 40 znaków
   EN: Red Eyes
   PL: Czerwone Oko
100. [Słowo kluczowe [RedEyeFirst] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +1\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeFirst].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +1 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +1 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
101. [Słowo kluczowe [RedEyeSecond] — nazwa] 적안 - 경계
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeSecond].name
   kontekst: identyfikator tagu w tekstach: `[RedEyeSecond]`
   limit: do 40 znaków
   EN: Red Eyes - Alert
   PL: Czerwone Oko - Czujność
102. [Słowo kluczowe [RedEyeSecond] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +2\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeSecond].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +2 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +2 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
103. [Słowo kluczowe [RedEyeThird] — nazwa] 적안 - 포식
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeThird].name
   kontekst: identyfikator tagu w tekstach: `[RedEyeThird]`
   limit: do 40 znaków
   EN: Red Eyes - Devouring
   PL: Czerwone Oko - Pożeranie
104. [Słowo kluczowe [RedEyeThird] — opis] - 기본 스킬 코인 효과의 출혈 부여 값 +3\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 적안\n· 2단계 (8~15) : 적안 - 경계\n· 3단계 (16~20) : 적안 - 포식\n- 버프를 강화하면 기본 스킬 코인 효과의 출혈 부여량이 강화 단계만큼 증가 (최대 3)
   źródło: BattleKeywords-walpu4.json :: dataList[id=RedEyeThird].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skill Coin effects inflict +3 more Bleed\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Resource used by certain Skills for additional effects\n- Enhances the buff based on Value\n· Stage 1 (1~7) : Red Eyes\n· Stage 2 (8~15) : Red Eyes - Alert\n· Stage 3 (16~20) : Red Eyes - Devouring\n- The amount of additional bleed inflicted by the first line of this buff is equal to the buff enhancement Stage (max 3)
   PL: - Podstawowe monety Umiejętności ataku nadają +3 więcej Krwawienia\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Czerwone Oko\n · Etap 2 (8–15): Czerwone Oko - Czujność\n · Etap 3 (16–20): Czerwone Oko - Pożeranie\n- Pierwsza linia tego wzmocnienia nadaje dodatkowe Krwawienie równe etapowi wzmocnienia (maks. 3)
105. [Słowo kluczowe [PenanceFirst] — nazwa] 참회
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceFirst].name
   kontekst: identyfikator tagu w tekstach: `[PenanceFirst]`
   limit: do 40 znaków
   EN: Penitence
   PL: Skrucha
106. [Słowo kluczowe [PenanceFirst] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 2만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceFirst].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 2 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 2 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
107. [Słowo kluczowe [PenanceSecond] — nazwa] 참회 - 경계
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceSecond].name
   kontekst: identyfikator tagu w tekstach: `[PenanceSecond]`
   limit: do 40 znaków
   EN: Penitence - Periphery
   PL: Skrucha - Czujność
108. [Słowo kluczowe [PenanceSecond] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 4만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceSecond].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 4 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 4 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
109. [Słowo kluczowe [PenanceThird] — nazwa] 참회 - 고해
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceThird].name
   kontekst: identyfikator tagu w tekstach: `[PenanceThird]`
   limit: do 40 znaków
   EN: Penitence - Confession
   PL: Skrucha - Wyznanie
110. [Słowo kluczowe [PenanceThird] — opis] - 참회를 얻는 기본 스킬 코인 적중 시, 6만큼 정신력 회복\n- 최댓값 : 20\n- 특수 충전 (위력 고정)\n- 턴 시작 시, 최대 체력의 (참회)%만큼 보호막을 얻음\n- 소모 시, 특정 스킬의 능력이 상승함\n- 수치에 따라 버프가 강화됨\n· 1단계 (1~7) : 참회\n· 2단계 (8~15) : 참회 - 경계\n· 3단계 (16~20) : 참회 - 고해\n- 버프를 강화하면 참회를 얻는 기본 스킬 코인 적중 시, (강화 단계 x 2)만큼 정신력 회복.
   źródło: BattleKeywords-walpu4.json :: dataList[id=PenanceThird].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 6 SP On Hit with Base Skill Coins that gain Penitence\n- Max Value : 20\n- Unique Charge (fixed Potency)\n- Turn Start: gain (Penitence)% of max HP as Shield\n- Resource used by certain Skills for additional effects\n- Enhances the buff Stage based on Value\n· Stage 1 (1~7) : Penitence\n· Stage 2 (8~15) : Penitence - Periphery\n· Stage 3 (16~20) : Penitence - Confession\n- The amount of SP healed by the first line of this buff is based on the enhancement Stage (enhancement Stage x 2)
   PL: - Zyskuje 6 Poczytalności przy trafieniu monetą podstawowej Umiejętności ataku dającej Skruchę\n- Maks. wartość: 20\n- Szczególne ładowanie (stała moc)\n- Na początku tury zyskuje Tarczę równą (Skrucha)% Maks. HP\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Według wartości wzmocnienie przechodzi przez etapy:\n · Etap 1 (1–7): Skrucha\n · Etap 2 (8–15): Skrucha - Czujność\n · Etap 3 (16–20): Skrucha - Wyznanie\n- Pierwsza linia tego wzmocnienia leczy Poczytalność według etapu wzmocnienia (etap x 2)
111. [Słowo kluczowe [Emptiness] — nazwa] 하얗게 태워버렸군
   źródło: BattleKeywords-walpu4.json :: dataList[id=Emptiness].name
   kontekst: identyfikator tagu w tekstach: `[Emptiness]`
   limit: do 40 znaków
   EN: Only Ashes Remain
   PL: Ostały się Tylko Popioły
112. [Słowo kluczowe [Emptiness] — opis] - 적안과 참회를 보유할 수 없음\n- 기본 스킬 효과로 적안 획득 시, 자신과 현재 체력 비율이 가장 낮은 아군의 체력을 자신의 최대 체력의 (적안 획득량)%만큼 회복 (턴 당 2회)\n- 기본 스킬 효과로 참회 획득 시, 자신과 현재 정신력이 가장 낮은 아군의 정신력을 (참회 획득량/2)만큼 회복 (턴 당 2회)\n- 턴 종료 시 효과 소멸됨
   źródło: BattleKeywords-walpu4.json :: dataList[id=Emptiness].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot maintain Red Eyes & Penitence\n- When gaining Red Eyes with Base Skill effects, heal self and 1 ally with the lowest HP percentage by (Red Eyes gained)% of this unit's max HP (2 times per turn)\n- When gaining Penitence with Base Skill effects, heal self and 1 ally with the least SP by ((Penitence gained)/2) SP (2 times per turn)\n- Turn End: this effect expires
   PL: - Nie może posiadać Czerwonego Oka ani Skruchy\n- Gdy efektem podstawowej Umiejętności zyskuje Czerwone Oko, leczy siebie i sojusznika z najniższym procentem HP o (uzyskane Czerwone Oko)% własnego Maks. HP (2 na turę)\n- Gdy efektem podstawowej Umiejętności zyskuje Skruchę, leczy siebie i sojusznika z najniższą Poczytalnością o (uzyskana Skrucha/2) Poczytalności (2 na turę)\n- Na koniec tury efekt znika
113. [Słowo kluczowe [SinkingWhite] — nazwa] 나비
   źródło: BattleKeywords-walpu4.json :: dataList[id=SinkingWhite].name
   kontekst: identyfikator tagu w tekstach: `[SinkingWhite]`
   limit: do 40 znaków
   EN: Butterfly
   PL: Motyl
114. [Słowo kluczowe [SinkingWhite] — opis] - 특수 침잠\n- 기본값 : 0, 최댓값 : 15\n- 이 효과의 위력을 산나비, 횟수를 죽은나비로 간주함.\n- 피격 시 공격자의 정신력을 (산나비/4)만큼 회복 (최소 1. 소수점 버림).\n- 피격 시 정신력이 0 미만이면, 죽은나비 1당 (침잠 위력/5)만큼 우울 피해를 받음. (최대 우울 피해 값 : 30. 소수점 버림. 정신력이 없는 대상에게는 피해가 절반으로 적용.)\n- 턴 종료 시 이 효과의 죽은나비 0으로 초기화, 이 효과의 산나비만큼 침잠 부여 후 산나비가 죽은나비로 변환.\n- 이 효과의 부여값은 외부 효과로 늘릴 수 없음. 침잠 부여값+ 효과를 받으면, 추가 부여값만큼 나비 대신 침잠이 부여됨.\n- 산나비와 죽은나비가 모두 0이 되면 효과가 제거됨.
   źródło: BattleKeywords-walpu4.json :: dataList[id=SinkingWhite].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Sinking\n- Base Value: 0, Max Value: 15\n- The Potency and the Count of this effect are called "The Living" and "The Departed", respectively.\n- When hit, the attacker heals (The Living/4) SP. (min 1; rounded down)\n- When hit, and if this unit's SP is at less than 0, take (Sinking Potency/5) Gloom damage for every value of The Departed. (max Gloom damage 30; rounded down; deals half damage to targets that are Non-SP Units.)\n- Turn End: Reset The Departed of this effect to 0; then, gain Sinking equal to The Living and convert The Living into The Departed.\n- No external effects can raise the amount of Butterfly inflicted. "Inflict additional Sinking" effects inflict additional Sinking instead of additional Butterfly.\n- This effect expires when both The Living and The Departed reach 0.
   PL: - Szczególne Zatonięcie\n- Wartość bazowa: 0, maks.: 15\n- Moc tego efektu to „Żywe Motyle”, a Licznik — „Martwe Motyle”.\n- Przy trafieniu atakujący odzyskuje (Żywe Motyle/4) Poczytalności (min. 1, zaokrąglone w dół).\n- Przy trafieniu, jeśli Poczytalność jest niższa od 0, otrzymuje za każdego Martwego Motyla (Moc Zatonięcia/5) obrażeń Posępnością (maks. obrażeń: 30, zaokrąglone w dół; jednostki bez Poczytalności otrzymują połowę).\n- Na koniec tury Martwe Motyle tego efektu resetują się do 0, po czym zyskuje Zatonięcie równe Żywym Motylom, które stają się Martwymi Motylami.\n- Wartości tego efektu nie można zwiększać efektami zewnętrznymi. Efekty „+ do nadawania Zatonięcia” nadają dodatkowe Zatonięcie zamiast Motyli.\n- Efekt znika, gdy Żywe i Martwe Motyle osiągną 0.
115. [Słowo kluczowe [SinkingBlack] — nazwa] 구버전 효과
   źródło: BattleKeywords-walpu4.json :: dataList[id=SinkingBlack].name
   kontekst: identyfikator tagu w tekstach: `[SinkingBlack]`
   limit: do 40 znaków
   EN: !!!OUDATED EFFECT!!!
   PL: Efekt Starej Wersji
116. [Słowo kluczowe [BulletLament] — nazwa] 산나비·죽은나비
   źródło: BattleKeywords-walpu4.json :: dataList[id=BulletLament].name
   kontekst: identyfikator tagu w tekstach: `[BulletLament]`
   limit: do 40 znaków
   EN: The Living & The Departed
   PL: Żywe i Martwe Motyle
117. [Słowo kluczowe [BulletLament] — opis] - 특수 탄환\n- 위력 + 횟수의 최댓값 : 20\n- 특정 스킬 사용 시 소모.\n- 소모 시 이 효과의 산나비(위력)와 죽은나비(횟수)를 무작위로 소모.\n- 소모 시 수치가 부족한 경우, 공격이 취소됨.
   źródło: BattleKeywords-walpu4.json :: dataList[id=BulletLament].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- The sum of Potency and Count maxes out at 20.\n- Consumed for certain Skills.\n- Whether The Living(Potency) or The Departed(Count) will be consumed for each shot is randomly determined\n- Some attacks cancel if this unit runs out of ammo.
   PL: - Szczególna amunicja\n- Suma Mocy i Licznika: maks. 20\n- Zużywana przez określone Umiejętności.\n- Przy zużyciu losowo zużywa Żywe Motyle (Moc) albo Martwe Motyle (Licznik).\n- Gdy wartości są niewystarczające, atak zostaje anulowany.
118. [Słowo kluczowe [TrainTeamCaptain] — nazwa] 교육팀 팀장
   źródło: BattleKeywords-walpu4.json :: dataList[id=TrainTeamCaptain].name
   kontekst: identyfikator tagu w tekstach: `[TrainTeamCaptain]`
   limit: do 40 znaków
   EN: Training Team Captain
   PL: Kapitan Zespołu Szkoleniowego
119. [Słowo kluczowe [TrainTeamCaptain] — opis] 해당 캐릭터의 슬롯 +1\n1스킬 수량 -1, 3스킬 수량 +1\n턴 시작 시 정신력 15 회복\n자신이 스킬로 화상, 출혈, 파열, 침잠, 진동을 부여할 때, 부여값 +1(특수 상태이상 포함)\n자신이 스킬로 호흡, 충전(특수 충전)을 얻을 때, 부여값 +1\n적 처치시 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1
   źródło: BattleKeywords-walpu4.json :: dataList[id=TrainTeamCaptain].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Slot +1\nModify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\nTurn Start: heal 15 SP\nIncrease the amount of Burn, Bleed, Rupture, Sinking, or Tremor inflicted by +1 (including 'Unique Status Effects')\nIncrease the amount of Poise or Charge(including 'Unique Charge') gained by +1\nOn Kill, Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: Sloty tej postaci: +1\nLiczba Umiejętności 1: -1, liczba Umiejętności 3: +1\nNa początku tury odzyskuje 15 Poczytalności\nGdy Umiejętnościami nadaje Podpalenie, Krwawienie, Rozdarcie, Zatonięcie lub Wstrząs, wartość nadania +1 (również szczególne stany)\nGdy Umiejętnościami zyskuje Oddech lub Ładowanie (również szczególne ładowanie), wartość +1\nPrzy zabiciu wroga: +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu
120. [Słowo kluczowe [VioletUnderstand] — nazwa] 이해
   źródło: BattleKeywords-walpu4.json :: dataList[id=VioletUnderstand].name
   kontekst: identyfikator tagu w tekstach: `[VioletUnderstand]`
   limit: do 40 znaków
   EN: Understanding
   PL: Zrozumienie
121. [Słowo kluczowe [VioletUnderstand] — opis] 스택당 가하는 피해량 +5%\n스택당 받는 피해량 + 5%\n(최댓값 : 5)
   źródło: BattleKeywords-walpu4.json :: dataList[id=VioletUnderstand].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +5% damage per Stack\n- Take +5% damage per Stack\n(max value : 5)
   PL: Za każdy stos zadaje +5% obrażeń\nZa każdy stos otrzymuje +5% obrażeń\n(maks. 5)
122. [Słowo kluczowe [MentalCrack] — nazwa] 정신 균열
   źródło: BattleKeywords-walpu4.json :: dataList[id=MentalCrack].name
   kontekst: identyfikator tagu w tekstach: `[MentalCrack]`
   limit: do 40 znaków
   EN: Mental Fracture
   PL: Pęknięcie Umysłu
123. [Słowo kluczowe [MentalCrack] — opis] 스택당 정신력 감소 효율 +1 (최대 5)\n5스택에 도달하면 스택이 소멸하고 정신력 10 피해\n턴 당 스택 1 감소
   źródło: BattleKeywords-walpu4.json :: dataList[id=MentalCrack].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SP Loss Efficiency +1 per Stack (max 5)\nExpires when it reaches 5 Stack, and take 10 SP damage\nLose 1 Stack per turn
   PL: Wydajność Spadku Poczytalności +1 za stos (maks. 5)\nPo 5 stosach stosy znikają, a jednostka traci 10 Poczytalności\nCo turę traci 1 stos
124. [Słowo kluczowe [ImpendingCollapse] — nazwa] 붕괴 임박
   źródło: BattleKeywords-walpu4.json :: dataList[id=ImpendingCollapse].name
   kontekst: identyfikator tagu w tekstach: `[ImpendingCollapse]`
   limit: do 40 znaków
   EN: Imminent Decay
   PL: Nieuchronny Upadek
125. [Słowo kluczowe [ImpendingCollapse] — opis] 턴 종료 시 스택 1 감소\n턴 시작 시 스택이 1 이하면, 특수 스킬을 사용함
   źródło: BattleKeywords-walpu4.json :: dataList[id=ImpendingCollapse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 1 Stack\nTurn Start: At 1- Stack, use a special Skill
   PL: Na koniec tury traci 1 stos\nNa początku tury, przy 1 stosie lub mniej, używa specjalnej Umiejętności
126. [Słowo kluczowe [ReloadLament] — nazwa] 재장전
   źródło: BattleKeywords-walpu4.json :: dataList[id=ReloadLament].name
   kontekst: identyfikator tagu w tekstach: `[ReloadLament]`
   limit: do 40 znaków
   EN: Reload
   PL: Przeładowanie
127. [Słowo kluczowe [ReloadLament] — opis] - 산나비·죽은나비(특수 탄환)에 적용되는 효과\n- 정신력을 ((30 - 보유한 산나비·죽은나비)/2)만큼 소모. (소수점 버림)\n- 보유한 산나비·죽은나비를 0으로 만들고, 산나비·죽은나비를 합하여 최댓값만큼 '죽어가는나비를본다.' 패시브의 확률에 따라 얻음.\n- 재장전 시 산나비와 죽은나비를 최소 1씩 얻음.
   źródło: BattleKeywords-walpu4.json :: dataList[id=ReloadLament].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Effect applied to The Living & The Departed(Unique Ammo)\n- Consume (30 - (The Living + The Departed))/2 SP. (rounded down)\n- Reset both The Living and The Departed values on self to 0, and gain the max value of their sum based on the probabilities listed in the Passive 'ISeeTheDyingButterfly.'\n- On Reload, gain at least 1 of The Living and The Departed.
   PL: - Działa na Żywe i Martwe Motyle (szczególna amunicja)\n- Zużywa ((30 - posiadane Żywe i Martwe Motyle)/2) Poczytalności (zaokrąglone w dół)\n- Zeruje posiadane Żywe i Martwe Motyle, a ich sumę przywraca do maksimum według szans z pasywu „Widzę Umierające Motyle”.\n- Przy Przeładowaniu zyskuje co najmniej 1 Żywe i 1 Martwego Motyla.

## Słowa kluczowe bitwy — BattleKeywords-walpu5
- plik gry: `BattleKeywords-walpu5.json` (opisy wyświetlane w dymkach pomocy podczas walki)

128. [Słowo kluczowe [Smoke] — nazwa] 연기
   źródło: BattleKeywords-walpu5.json :: dataList[id=Smoke].name
   kontekst: identyfikator tagu w tekstach: `[Smoke]`
   limit: do 40 znaków
   EN: Smoke
   PL: Dym
129. [Słowo kluczowe [Smoke] — opis] - 위력 최댓값: 10\n- 횟수 최댓값: 5\n- 수치가 9 이상이면, 최종 위력 +1\n- 수치당 받는 피해량 +5%\n- 턴 종료 시 횟수 1 감소
   źródło: BattleKeywords-walpu5.json :: dataList[id=Smoke].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 10\n- Max Count: 5\n- At 9+ Potency, Final Power +1\n- Take +5% damage for every Potency\n- Lose 1 Count at Turn End
   PL: - Maks. Mocy: 10\n- Maks. Licznika: 5\n- Od 9 Mocy: Moc Końcowa +1\n- Otrzymuje +5% obrażeń za każdą Moc\n- Na koniec tury traci 1 Licznik
130. [Słowo kluczowe [Church_LowMorale] — nazwa] 교단
   źródło: BattleKeywords-walpu5.json :: dataList[id=Church_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Church_LowMorale]`
   limit: do 40 znaków
   EN: The Church
   PL: Zakon
131. [Słowo kluczowe [Church_LowMorale] — opis] - 사기저하\n- 전투 중 연기 혹은 연기 횟수를 얻을 때, 추가로 1 얻음.\n- 턴 시작 시 취약 3, 피해량 증가 2, 수비 위력 증가 1 얻음
   źródło: BattleKeywords-walpu5.json :: dataList[id=Church_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 additional Smoke or Smoke Count when gaining them\n- Turn Start: gain 3 Fragility, 2 Damage Up, and 1 Defense Power Up
   PL: - Spadek Moralu\n- Gdy podczas walki zyskuje Dym lub Licznik Dymu, zyskuje dodatkowo 1\n- Na początku tury zyskuje 3 Wrażliwości, 2 Wzrosty Obrażeń i 1 Wzrost Mocy Obrony
132. [Słowo kluczowe [Church_Panic] — nazwa] 교단
   źródło: BattleKeywords-walpu5.json :: dataList[id=Church_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Church_Panic]`
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Słowo kluczowe [Church_Panic] — opis] - 패닉\n- 전투 중 연기 혹은 연기 횟수를 얻을 때, 추가로 2 얻음.\n- 턴 시작 시 취약 3, 피해량 증가 4, 수비 위력 증가 2 얻음
   źródło: BattleKeywords-walpu5.json :: dataList[id=Church_Panic].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 additional Smoke or Smoke Count when gaining them\n- Turn Start: gain 3 Fragility, 4 Damage Up, and 2 Defense Power Up
   PL: - Panika\n- Gdy podczas walki zyskuje Dym lub Licznik Dymu, zyskuje dodatkowo 2\n- Na początku tury zyskuje 3 Wrażliwości, 4 Wzrosty Obrażeń i 2 Wzrosty Mocy Obrony
134. [Słowo kluczowe [MeatGearForce] — nazwa] 고기 톱니:강제
   źródło: BattleKeywords-walpu5.json :: dataList[id=MeatGearForce].name
   kontekst: identyfikator tagu w tekstach: `[MeatGearForce]`
   limit: do 40 znaków
   EN: Meat Gear: Coercion
   PL: Mięsna Zębatka: Przymus
135. [Słowo kluczowe [MeatGearForce] — opis] - 체력이 1이 되더라도 전투 중에 죽지않음.\n- 턴 종료시 체력이 1 이라면, 사망함.
   źródło: BattleKeywords-walpu5.json :: dataList[id=MeatGearForce].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - HP does not drop below 1 HP during the Combat Phase.\n- This unit dies if it has 1 HP at Turn End.
   PL: - Nie umiera podczas walki, nawet gdy HP spadnie do 1.\n- Jeśli na koniec tury ma 1 HP, umiera.
136. [Słowo kluczowe [AllSetForShooting] — nazwa] 사격 준비 만전
   źródło: BattleKeywords-walpu5.json :: dataList[id=AllSetForShooting].name
   kontekst: identyfikator tagu w tekstach: `[AllSetForShooting]`
   limit: do 40 znaków
   EN: Ready to Fire
   PL: Pełna Gotowość do Strzału
137. [Słowo kluczowe [AllSetForShooting] — opis] - 스킬 슬롯 수 +1\n- 스킬 3 수량 +1, 대신 스킬 1 수량 -1\n- 사용하는 기본 공격 스킬에서 탄환을 소모하는 수만큼 피해량 +10%\n- 사용하는 공격 스킬에서 탄환을 얻는 스킬은 현재 보유한 마탄만큼 피해량 +10% (가장 높은 피해량 증가가 반영됨)\n- 스킬로 적 처치 시 자신을 포함하여 정신력이 가장 낮은 아군 2명 정신력 25 회복, 적을 처치한 스킬 속성의 E.G.O 자원 +2, 나머지 속성의 E.G.O 자원 +1
   źródło: BattleKeywords-walpu5.json :: dataList[id=AllSetForShooting].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- Deal +10% damage for every Ammo the Base Attack Skill spends\n- Attack Skills that gain Ammo deal +10% damage for every Magic Bullet (applies whichever that has the highest damage gain)\n- On Kill with a Skill: heal 25 SP for 2 allies(including self) with the least SP; +2 E.G.O resources for the Affinity of the Skill that defeated the target; +1 E.G.O resource for all other Affinities
   PL: - Liczba slotów Umiejętności +1\n- Liczba Umiejętności 3: +1, w zamian liczba Umiejętności 1: -1\n- Zadaje +10% obrażeń za każdą Amunicję zużytą przez użytą podstawową Umiejętność ataku\n- Podstawowe Umiejętności ataku, które zyskują Amunicję, zadają +10% obrażeń za każdą Magiczną Amunicję (liczy się wariant dający najwyższy wzrost obrażeń)\n- Przy zabiciu wroga Umiejętnością leczy 25 Poczytalności u 2 sojuszników (w tym siebie) z najniższą Poczytalnością; +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu

## Słowa kluczowe bitwy — BattleKeywords-walpu6
- plik gry: `BattleKeywords-walpu6.json` (opisy wyświetlane w dymkach pomocy podczas walki)

138. [Słowo kluczowe [ColdBlackTear] — nazwa] 차갑고 검은 눈물
   źródło: BattleKeywords-walpu6.json :: dataList[id=ColdBlackTear].name
   kontekst: identyfikator tagu w tekstach: `[ColdBlackTear]`
   limit: do 40 znaków
   EN: Cold, Black Tears
   PL: Zimne, Czarne Łzy
139. [Słowo kluczowe [ColdBlackTear] — opis] - 최댓값: 5\n- 턴 시작시 합 위력 감소 1 얻음\n- 이 효과가 있는 상태로 피격 시 정신력이 (스택 x 2)만큼 감소함 (턴 당 1회, 적중한 코인이 파괴되었다면 발동 하지 않음)\n- 이 효과가 증오의 여왕에 의해 감소되었다면, 정신력 5 회복\n- 이 효과로 감소하는 정신력은 -40 이하로 내려가지 않음
   źródło: BattleKeywords-walpu6.json :: dataList[id=ColdBlackTear].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain 1 Clash Power Down\n- If this unit is hit while it has this effect, lose (Stack x 2) SP (once per turn; does not activate when hit by a Cracked Coin)\n- If Queen of Hatred reduced this effect, heal 5 SP\n- This effect cannot reduce this unit's SP below -40
   PL: - Maks. stosów: 5\n- Na początku tury zyskuje 1 Spadek Mocy Starcia\n- Przy trafieniu z tym efektem traci (stosy x 2) Poczytalności (1 na turę; nie działa, gdy trafiła pęknięta moneta)\n- Jeśli efekt zmniejszyła Królowa Nienawiści, odzyskuje 5 Poczytalności\n- Ten efekt nie może obniżyć Poczytalności poniżej -40
140. [Słowo kluczowe [HelplessTear] — nazwa] 무력한 눈물
   źródło: BattleKeywords-walpu6.json :: dataList[id=HelplessTear].name
   kontekst: identyfikator tagu w tekstach: `[HelplessTear]`
   limit: do 40 znaków
   EN: Helpless Tears
   PL: Bezsilne Łzy
141. [Słowo kluczowe [HelplessTear] — opis] - 최댓값: 1\n- 공격 레벨 증가 3\n- 방어 레벨 감소 6\n- 모든 스킬의 가중치가 1 늘어남\n- 모든 스킬이 파괴 불가 코인이 됨\n- 침잠 위력 및 횟수 부여량 1 증가
   źródło: BattleKeywords-walpu6.json :: dataList[id=HelplessTear].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Gain 3 Offense Levels\n- Lose 6 Defense Levels\n- All Skills gain +1 Atk Weight\n- All Skills become Unbreakable Coins\n- Inflict +1 more Sinking Potency and Count
   PL: - Maks. stosów: 1\n- Poziom Ataku +3\n- Poziom Obrony -6\n- Waga ataku wszystkich Umiejętności +1\n- Wszystkie monety Umiejętności stają się monetami niezniszczalnymi\n- Nadaje +1 więcej Mocy i Licznika Zatonięcia
142. [Słowo kluczowe [WornOutKnight] — nazwa] 닳디 닳은 기사
   źródło: BattleKeywords-walpu6.json :: dataList[id=WornOutKnight].name
   kontekst: identyfikator tagu w tekstach: `[WornOutKnight]`
   limit: do 40 znaków
   EN: Weathered Knight
   PL: Zwietczały Rycerz
143. [Słowo kluczowe [WornOutKnight] — opis] 이번 턴 동안 받는 피해량 +100%
   źródło: BattleKeywords-walpu6.json :: dataList[id=WornOutKnight].desc
   limit: do 120 znaków
   EN: Take +100% damage this turn
   PL: Otrzymuje +100% obrażeń w tej turze
144. [Słowo kluczowe [WornOutKnight] — tekst klimatyczny] <color=#2e72b9>다른 이를 구함으로써 스스로를 구하고 싶었던 기사는, 이제 절망의 기사라는 불명예로 불리운 채, 다른 이들과 마찬가지로 사람들의 기억 속에서 사라져갔다.</color>
   źródło: BattleKeywords-walpu6.json :: dataList[id=WornOutKnight].flavor
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#2e72b9>, </color>
   EN: <color=#2e72b9>The knight who wanted to redeem herself by saving others was now dishonorably called the Knight of Despair; forgotten from the people's memory, just like the others.</color>
   PL: <color=#2e72b9>Rycerz, który chciał ocalić samego siebie, ratując innych, nosi dziś niechlubny przydomek Rycerza Rozpaczy i — jak wszyscy inni — znika z pamięci ludzi.</color>
145. [Słowo kluczowe [SignOfDespair] — nazwa] 절망의 가호
   źródło: BattleKeywords-walpu6.json :: dataList[id=SignOfDespair].name
   kontekst: identyfikator tagu w tekstach: `[SignOfDespair]`
   limit: do 40 znaków
   EN: Blessing of Despair
   PL: Błogosławieństwo Rozpaczy
146. [Słowo kluczowe [SignOfDespair] — opis] 공격 종료 시 차갑고 검은 눈물이 없는 대상이 있을 경우, 다음 턴에 해제됨\n\n합 위력 증가 1, 피해량 증가 1 얻음\n차갑고 검은 눈물 부여량 1 증가
   źródło: BattleKeywords-walpu6.json :: dataList[id=SignOfDespair].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack End: If there are targets without Cold, Black Tears, removes this effect next turn\n\nGain 1 Clash Power Up and 1 Damage Up\nInflict +1 more Cold, Black Tears
   PL: Po zakończeniu ataku, jeśli istnieją cele bez Zimnych, Czarnych Łez, efekt zostanie zdjęty w następnej turze\n\nZyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń\nNadaje +1 więcej Zimnych, Czarnych Łez
147. [Słowo kluczowe [CollapsedPride] — nazwa] 무너져 내린 긍지
   źródło: BattleKeywords-walpu6.json :: dataList[id=CollapsedPride].name
   kontekst: identyfikator tagu w tekstach: `[CollapsedPride]`
   limit: do 40 znaków
   EN: Crumbled Pride
   PL: Pokruszona Duma
148. [Słowo kluczowe [CollapsedPride] — opis] 닳디 닳은 기사 패시브에서 사용됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=CollapsedPride].desc
   limit: do 120 znaków
   EN: Used for "Weathered Knight" Passive
   PL: Używana przez pasyw „Zwietczały Rycerz”
149. [Słowo kluczowe [CollapsedPride] — tekst klimatyczny] <color=#2e72b9>남은 건 닳디 닳은 기사라는 볼품없는 긍지 하나뿐이다.</color>
   źródło: BattleKeywords-walpu6.json :: dataList[id=CollapsedPride].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#2e72b9>, </color>
   EN: <color=#2e72b9>All that remains is the hollow pride of a weathered knight.</color>
   PL: <color=#2e72b9>Ostała się jedynie pokruszona duma zwietczałego rycerza.</color>
150. [Słowo kluczowe [FailedToAssistQueen] — nazwa] 내가… 무슨 쓸모…야?
   źródło: BattleKeywords-walpu6.json :: dataList[id=FailedToAssistQueen].name
   kontekst: identyfikator tagu w tekstach: `[FailedToAssistQueen]`
   limit: do 40 znaków
   EN: What use... am I...?
   PL: Do czego ja... jeszcze... służę...?
151. [Słowo kluczowe [FailedToAssistQueen] — opis] - 최댓값: 1\n- 공격 레벨 감소 3\n- 방어 레벨 감소 3
   źródło: BattleKeywords-walpu6.json :: dataList[id=FailedToAssistQueen].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Lose 3 Offense Levels\n- Lose 3 Defense Levels
   PL: - Maks. stosów: 1\n- Poziom Ataku -3\n- Poziom Obrony -3
152. [Słowo kluczowe [UsedTooMuchPower] — nazwa] 힘을 너무 많이 썼나봐
   źródło: BattleKeywords-walpu6.json :: dataList[id=UsedTooMuchPower].name
   kontekst: identyfikator tagu w tekstach: `[UsedTooMuchPower]`
   limit: do 40 znaków
   EN: I used too much power
   PL: Chyba użyłam zbyt dużej mocy
153. [Słowo kluczowe [UsedTooMuchPower] — opis] - 최댓값: 1\n- 턴 종료 시 전투에서 이탈함
   źródło: BattleKeywords-walpu6.json :: dataList[id=UsedTooMuchPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: escapes from the Encounter
   PL: - Maks. stosów: 1\n- Na koniec tury opuszcza walkę
154. [Słowo kluczowe [UsedTooMuchPower] — tekst klimatyczny] <color=#ff3d8f>힘이 다해 움직일 수 없다</color>
   źródło: BattleKeywords-walpu6.json :: dataList[id=UsedTooMuchPower].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff3d8f>, </color>
   EN: <color=#ff3d8f>Exhausted and unable to move.</color>
   PL: <color=#ff3d8f>Siła wyczerpana — nie może się ruszać.</color>
155. [Słowo kluczowe [ChasingArcana] — nazwa] 영창 - 아르카나 슬레이브
   źródło: BattleKeywords-walpu6.json :: dataList[id=ChasingArcana].name
   kontekst: identyfikator tagu w tekstach: `[ChasingArcana]`
   limit: do 40 znaków
   EN: Chanting - Arcana Slave
   PL: Inkantacja - Arcana Slave
156. [Słowo kluczowe [ChasingArcana] — opis] - 최댓값: 3\n- 턴 시작 시 1 증가\n- 스택이 3이 되면, 다음 턴에 속도 20을 얻고 아르카나 슬레이브를 사용함
   źródło: BattleKeywords-walpu6.json :: dataList[id=ChasingArcana].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 1 at Turn Start\n- At 3 Stack, gains 20 Speed and uses ARCANA SLAVE next turn
   PL: - Maks. stosów: 3\n- +1 na początku tury\n- Przy 3 stosach w następnej turze zyskuje 20 Szybkości i używa ARCANA SLAVE
157. [Słowo kluczowe [PowerOfLoveAndJustice] — nazwa] 사랑/정의
   źródło: BattleKeywords-walpu6.json :: dataList[id=PowerOfLoveAndJustice].name
   kontekst: identyfikator tagu w tekstach: `[PowerOfLoveAndJustice]`
   limit: do 40 znaków
   EN: Love/Justice
   PL: Miłość/Sprawiedliwość
158. [Słowo kluczowe [PowerOfLoveAndJustice] — opis] - 위력 당 파열 위력 부여량 1 증가
   źródło: BattleKeywords-walpu6.json :: dataList[id=PowerOfLoveAndJustice].desc
   limit: do 120 znaków
   EN: - For every Stack, inflict +1 more Rupture Potency
   PL: - Za każdą Moc nadaje +1 więcej Mocy Rozdarcia
159. [Słowo kluczowe [CentralCommandTeamCaptain] — nazwa] 중앙본부팀 팀장
   źródło: BattleKeywords-walpu6.json :: dataList[id=CentralCommandTeamCaptain].name
   kontekst: identyfikator tagu w tekstach: `[CentralCommandTeamCaptain]`
   limit: do 40 znaków
   EN: Central Command Team Captain
   PL: Kapitan Zespołu Dowodzenia Centrali
160. [Słowo kluczowe [CentralCommandTeamCaptain] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +1 (특수 상태이상 포함)\n- 자신이 스킬로 호흡 위력, 충전 횟수(특수 충전 포함)를 얻을 때, 획득값 +1\n- 패닉 및 침식 상태를 무시하고, 다음 턴에 정신력 0이 됨 (전투 당 1회)\n- 공격 가중치가 2 이상인 기본 스킬의 피해량 +30%\n- 적 처치시 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1
   źródło: BattleKeywords-walpu6.json :: dataList[id=CentralCommandTeamCaptain].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor Potency inflicted with Skills by +1 (including 'Unique Status Effects')\n- Increase the amount of Poise Potency or Charge Count(including 'Unique Charge') gained from Skills by +1\n- Instead of Panicking or Corroding, reset SP to 0 next turn (once per Encounter)\n- Base Attack Skills with 2+ Atk Weight deal +30% damage\n- On Kill, Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +1 (również szczególne stany)\n- Gdy Umiejętnościami zyskuje Moc Oddechu lub Licznik Ładowania (również szczególne ładowanie), wartość +1\n- Ignoruje Panikę i Korozję, a w następnej turze Poczytalność spada do 0 (1 na walkę)\n- Podstawowe Umiejętności ataku o Wadze 2+ zadają +30% obrażeń\n- Przy zabiciu wroga: +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu
161. [Słowo kluczowe [BestWelfareTeamMember] — nazwa] 복지팀 우수 직원
   źródło: BattleKeywords-walpu6.json :: dataList[id=BestWelfareTeamMember].name
   kontekst: identyfikator tagu w tekstach: `[BestWelfareTeamMember]`
   limit: do 40 znaków
   EN: Welfare Team Model Employee
   PL: Wzorowy Pracownik Zespołu Dobrobytu
162. [Słowo kluczowe [BestWelfareTeamMember] — opis] - 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +1 (특수 상태이상 포함)\n- 패닉 및 침식 상태를 무시하고, 다음 턴에 정신력 0이 됨 (전투 당 1회)\n- 이 효과를 받는 게 로보토미 E.G.O::눈물로 벼려낸 검 로쟈라면, 매 턴 시작시 관통 피해량 증가 1 얻음
   źródło: BattleKeywords-walpu6.json :: dataList[id=BestWelfareTeamMember].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When inflicting Burn, Bleed, Rupture, Sinking, and Tremor Potency with this unit's Skills, inflict +1 more of each (including 'Unique Status Effects')\n- Instead of Panicking or Corroding, reset this unit's SP to 0 next turn (once per Encounter)\n- If this effect is applied to Lobotomy E.G.O::The Sword Sharpened with Tears Rodion, gain 1 Pierce DMG Up at every Turn Start
   PL: - Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +1 (również szczególne stany)\n- Ignoruje Panikę i Korozję, a w następnej turze Poczytalność spada do 0 (1 na walkę)\n- Jeśli ten efekt działa na Lobotomy E.G.O::Miecz Ostrzony Łzami Rodion, na początku każdej tury zyskuje 1 Wzrost Obrażeń Przebicia
163. [Słowo kluczowe [ChasingArcanahard] — nazwa] 영창 - 아르카나 슬레이브
   źródło: BattleKeywords-walpu6.json :: dataList[id=ChasingArcanahard].name
   kontekst: identyfikator tagu w tekstach: `[ChasingArcanahard]`
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Słowo kluczowe [ChasingArcanahard] — opis] - 최댓값: 3\n- 턴 시작 시 1 증가\n- 스택이 3이 되면, 다음 턴에 속박을 20 얻고 아르카나 슬레이브를 사용함
   źródło: BattleKeywords-walpu6.json :: dataList[id=ChasingArcanahard].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 1 at Turn Start\n- At 3 Stack: next turn, gain 20 Bind and use ARCANA SLAVE
   PL: - Maks. stosów: 3\n- +1 na początku tury\n- Przy 3 stosach w następnej turze zyskuje 20 Spętań i używa ARCANA SLAVE
165. [Słowo kluczowe [HystericGauge] — nazwa] 히스테리
   źródło: BattleKeywords-walpu6.json :: dataList[id=HystericGauge].name
   kontekst: identyfikator tagu w tekstach: `[HystericGauge]`
   limit: do 40 znaków
   EN: Hysteria
   PL: Histeria
166. [Słowo kluczowe [HystericGauge] — opis] - 기본값: 0\n- 최댓값: 3\n- 턴 종료 시\n· 정신력이 0 이상이면, 1 감소\n· 정신력이 0 미만이면, 1 증가
   źródło: BattleKeywords-walpu6.json :: dataList[id=HystericGauge].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 0\n- Max Stack: 3\n- At Turn End...\n· At 0 or higher SP, lose 1 Stack\n· At less than 0 SP, gain 1 Stack
   PL: - Wartość bazowa: 0\n- Maks.: 3\n- Na koniec tury:\n· przy Poczytalności 0 lub wyższej traci 1 stos\n· przy Poczytalności niższej od 0 zyskuje 1 stos
167. [Słowo kluczowe [MagicalGirlAppear] — nazwa] 마법소녀 등장!
   źródło: BattleKeywords-walpu6.json :: dataList[id=MagicalGirlAppear].name
   kontekst: identyfikator tagu w tekstach: `[MagicalGirlAppear]`
   limit: do 40 znaków
   EN: Here Comes Magical Girl!
   PL: Pojawia się Czarodziejka!
168. [Słowo kluczowe [MagicalGirlAppear] — opis] - 이번 턴에 사용하는 기본 공격 스킬이 더하기 코인 스킬로 변경됨\n\n- 자신의 사랑/증오당 기본 공격 스킬의 피해량 +3% (최대 15%)
   źródło: BattleKeywords-walpu6.json :: dataList[id=MagicalGirlAppear].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For this turn, this unit uses Plus Coin Base Attack Skills\n\n- Base Attack Skills deal +3% damage for every Love/Hate on self (max 15%)
   PL: - W tej turze podstawowe Umiejętności ataku stają się Umiejętnościami z monetami plus\n\n- Za każdą Miłość/Nienawiść podstawowe Umiejętności ataku zadają +3% obrażeń (maks. 15%)
169. [Słowo kluczowe [NoVillain] — nazwa] 역변-리버스드
   źródło: BattleKeywords-walpu6.json :: dataList[id=NoVillain].name
   kontekst: identyfikator tagu w tekstach: `[NoVillain]`
   limit: do 50 znaków
   EN: Regressive Transformation - Reversed
   PL: Transformacja Wsteczna - Odwrócona
170. [Słowo kluczowe [NoVillain] — opis] - 이번 턴에 사용하는 기본 공격 스킬이 빼기 코인 스킬로 변경됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=NoVillain].desc
   limit: do 120 znaków
   EN: - For this turn, this unit uses Minus Coin Base Attack Skills
   PL: - W tej turze podstawowe Umiejętności ataku stają się Umiejętnościami z monetami minus
171. [Słowo kluczowe [VillainMark] — nazwa] 악당 표식
   źródło: BattleKeywords-walpu6.json :: dataList[id=VillainMark].name
   kontekst: identyfikator tagu w tekstach: `[VillainMark]`
   limit: do 40 znaków
   EN: Mark of Villainy
   PL: Znak Złoczyńcy
172. [Słowo kluczowe [VillainMark] — opis] - 돈키호테의 공격에 받는 피해량 +10%\n\n- 턴마다 가장 먼저 부여 받은 대상에게만 부여됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=VillainMark].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Don Quixote\n\n- Applies only to the first target to receive the effect in each turn
   PL: - Otrzymuje +10% obrażeń od ataków Don Kichota\n\n- W każdej turze nakładany tylko na pierwszego celu, który go otrzymał
173. [Słowo kluczowe [ArcanaQueenOfHate] — nazwa] 매지컬 아르카나
   źródło: BattleKeywords-walpu6.json :: dataList[id=ArcanaQueenOfHate].name
   kontekst: identyfikator tagu w tekstach: `[ArcanaQueenOfHate]`
   limit: do 40 znaków
   EN: Magical Arcana
   PL: Magiczna Arcana
174. [Słowo kluczowe [ArcanaQueenOfHate] — opis] - 최댓값: 3\n- 자신의 기본 공격 스킬의  피해량 +(수치 X 5)%\n- 턴 종료 시 수치가 3이고 정신력이 -25이상이면, 정신력이 -25가 됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=ArcanaQueenOfHate].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Base Attack Skills deal +(Stack x 5)% damage\n- Turn End: At 3 Stack and with -25 or higher SP, change SP to -25
   PL: - Maks. stosów: 3\n- Podstawowe ataki zadają +(stosy x 5)% obrażeń\n- Na koniec tury, przy 3 stosach i Poczytalności -25 lub wyższej, Poczytalność zmienia się na -25
175. [Słowo kluczowe [ThePowerOfLoveAndHate] — nazwa] 사랑/증오
   źródło: BattleKeywords-walpu6.json :: dataList[id=ThePowerOfLoveAndHate].name
   kontekst: identyfikator tagu w tekstach: `[ThePowerOfLoveAndHate]`
   limit: do 40 znaków
   EN: Love/Hate
   PL: Miłość/Nienawiść
176. [Słowo kluczowe [ThePowerOfLoveAndHate] — opis] - 횟수 최댓값: 20\n- 특수 충전\n- 소모 시 특정 스킬의 능력이 상승함. 횟수를 최대 20까지 얻을 수 있음. 턴 종료 시 횟수 1 감소\n(충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-walpu6.json :: dataList[id=ThePowerOfLoveAndHate].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Count: 20\n- Unique Charge\n- Resource used by certain skills for additional effects. Its Count can go up to 20. Count lowers by 1 at the end of each turn.\n(Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency/Count)
   PL: - Maks. Licznika: 20\n- Szczególne ładowanie\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów. Licznik może osiągnąć do 20. Na koniec tury maleje o 1.\n(Efekty zmieniające Moc i Licznik ładowania działają na niego tak samo)
177. [Słowo kluczowe [MagicalGirlResponse] — nazwa] 마법소녀의 영창
   źródło: BattleKeywords-walpu6.json :: dataList[id=MagicalGirlResponse].name
   kontekst: identyfikator tagu w tekstach: `[MagicalGirlResponse]`
   limit: do 40 znaków
   EN: Magical Girl's Chant
   PL: Inkantacja Czarodziejki
178. [Słowo kluczowe [MagicalGirlResponse] — opis] - 최댓값: 2\n- 이 효과를 얻으면, 공격 위력 증가 1, 피해량 증가 1 얻음\n- 자신의 충전 횟수를 증가하거나 충전 횟수를 소모하는 공격 스킬의 최종 위력 +1, 피해량 +10%\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-walpu6.json :: dataList[id=MagicalGirlResponse].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- When gaining this effect, gain 1 Attack Power Up and 1 Damage Up\n- This unit's Attack Skills that gain or consume Charge Count gain Final Power +1 and deal +10% damage\n- Reduced by 1 at Turn End
   PL: - Maks. stosów: 2\n- Przy uzyskaniu tego efektu zyskuje 1 Wzrost Mocy Ataku i 1 Wzrost Obrażeń\n- Podstawowe Umiejętności ataku, które zyskują lub zużywają Licznik Ładowania, zyskują Moc Końcową +1 i zadają +10% obrażeń\n- Na koniec tury maleje o 1
179. [Słowo kluczowe [BlessingAlly] — nazwa] 가호
   źródło: BattleKeywords-walpu6.json :: dataList[id=BlessingAlly].name
   kontekst: identyfikator tagu w tekstach: `[BlessingAlly]`
   limit: do 40 znaków
   EN: Blessing
   PL: Błogosławieństwo
180. [Słowo kluczowe [BlessingAlly] — opis] - 턴 시작 시 정신력 8당, 지키는 검 1 얻음 (최대 5)\n- 합 종료 시, 대상에게 침잠 2 부여 (턴당 1회)\n- 피격 시, 공격한 대상에게 침잠 2 부여 (턴당 1회)\n- 정신력 20당, 이 버프 효과로 부여하는 침잠 위력 부여값 +1 (최대 2)\n- 사용하는 기본 스킬이 더하기 코인 스킬로 변경됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=BlessingAlly].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Protecting Sword for every 8 SP (max 5)\n- When Clash ends, inflict 2 Sinking (once per turn)\n- When hit, inflict 2 Sinking on the attacker (once per turn)\n- For every 20 SP, inflict +1 more Sinking Potency with above effects (max 2)\n- Replace this unit's Base Skills with Plus Coin Skills
   PL: - Na początku tury zyskuje 1 Miecz Obrońcy za każde 8 Poczytalności (maks. 5)\n- Po zakończeniu Starcia nadaje celowi 2 Zatonięcia (1 na turę)\n- Przy trafieniu nadaje atakującemu 2 Zatonięcia (1 na turę)\n- Za każde 20 Poczytalności Zatonięcie nadawane tym błogosławieństwem zyskuje +1 więcej Mocy (maks. 2)\n- Podstawowe Umiejętności stają się Umiejętnościami z monetami plus
181. [Słowo kluczowe [ProtectiveSword] — nazwa] 지키는 검
   źródło: BattleKeywords-walpu6.json :: dataList[id=ProtectiveSword].name
   kontekst: identyfikator tagu w tekstach: `[ProtectiveSword]`
   limit: do 40 znaków
   EN: Protecting Sword
   PL: Miecz Obrońcy
182. [Słowo kluczowe [ProtectiveSword] — opis] - 턴 시작 시, 수치 1당 방어 레벨 증가 1 얻음 (최대 5)\n- 턴 시작 시, 조작 패널에서 가장 왼쪽의 스킬 슬롯 도발치가 (수치 x 3)만큼 증가 (최대 15)\n- 최댓값 : 5\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-walpu6.json :: dataList[id=ProtectiveSword].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Defense Level Up for every Stack (max 5)\n- Turn Start: +(Stack x 3) Aggro to the leftmost Skill Slot on the Dashboard (max 15)\n- Max Stack: 5\n- Expires at Turn End
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Obrony za każdy stos (maks. 5)\n- Na początku tury Wartość Prowokacji skrajnie lewego slotu Umiejętności w panelu rośnie o (stosy x 3) (maks. 15)\n- Maks. stosów: 5\n- Znika na koniec tury
183. [Słowo kluczowe [DespairAlly] — nazwa] 절망
   źródło: BattleKeywords-walpu6.json :: dataList[id=DespairAlly].name
   kontekst: identyfikator tagu w tekstach: `[DespairAlly]`
   limit: do 40 znaków
   EN: Despair
   PL: Rozpacz
184. [Słowo kluczowe [DespairAlly] — opis] - 턴 시작 시, 정신력 -8당 꿰뚫는 검 1 얻음 (최대 5)\n- 합 종료 시, 대상의 침잠 횟수 1 증가 (턴당 1회)\n- 기본 공격 스킬의 첫 번째 코인 적중 시, 대상의 침잠 횟수 1 증가 (턴당 1회)\n- 정신력 -20당, 이 버프 효과로 부여하는 침잠 횟수의 부여값 +1 (최대 2)\n- 사용하는 기본 스킬이 빼기 코인 스킬로 변경됨
   źródło: BattleKeywords-walpu6.json :: dataList[id=DespairAlly].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Piercing Sword for every -8 SP (max 5)\n- When Clash ends, inflict +1 Sinking Count (once per turn)\n- On Hit with the first Coin of a Base Attack Skill, inflict +1 Sinking Count (once per turn)\n- For every -20 SP, inflict +1 more Sinking Count with above effects (max 2)\n- Replace this unit's Base Skills with Minus Coin Skills
   PL: - Na początku tury zyskuje 1 Miecz Przebijający za każde -8 Poczytalności (maks. 5)\n- Po zakończeniu Starcia Licznik Zatonięcia celu +1 (1 na turę)\n- Przy trafieniu pierwszą monetą podstawowej Umiejętności ataku Licznik Zatonięcia celu +1 (1 na turę)\n- Za każde -20 Poczytalności Licznik Zatonięcia nadawany tym błogosławieństwem zyskuje +1 więcej (maks. 2)\n- Podstawowe Umiejętności stają się Umiejętnościami z monetami minus
185. [Słowo kluczowe [PenetratingSword] — nazwa] 꿰뚫는 검
   źródło: BattleKeywords-walpu6.json :: dataList[id=PenetratingSword].name
   kontekst: identyfikator tagu w tekstach: `[PenetratingSword]`
   limit: do 40 znaków
   EN: Piercing Sword
   PL: Miecz Przebijający
186. [Słowo kluczowe [PenetratingSword] — opis] - 턴 시작 시, 수치 1당 공격 레벨 증가 1 얻음 (최대 5)\n- 턴 시작 시, 모든 스킬 슬롯의 도발치가 (수치 x 0.15)만큼 감소 (최대 0.75)\n- 최댓값 : 5\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-walpu6.json :: dataList[id=PenetratingSword].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Offense Level Up for every Stack (max 5)\n- Turn Start: -(Stack x 0.15) Aggro to all Skill Slots on the Dashboard (max 0.75)\n- Max Stack: 5\n- Expires at Turn End
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każdy stos (maks. 5)\n- Na początku tury Wartość Prowokacji wszystkich slotów Umiejętności w panelu maleje o (stosy x 0,15) (maks. 0,75)\n- Maks. stosów: 5\n- Znika na koniec tury
187. [Słowo kluczowe [SwordCutwithTear] — nazwa] 눈물 벼리기
   źródło: BattleKeywords-walpu6.json :: dataList[id=SwordCutwithTear].name
   kontekst: identyfikator tagu w tekstach: `[SwordCutwithTear]`
   limit: do 40 znaków
   EN: Tear-sharpened
   PL: Ostrzone Łzami
188. [Słowo kluczowe [SwordCutwithTear] — opis] - 턴 시작 시, 깊은 눈물 5 얻음\n· 수치가 3이면, 깊은 눈물 5 추가로 얻음\n- 턴 종료 시, (수치 x 15)만큼 정신력 감소\n- 기본 공격 스킬의 피해량이 (수치 x 10)%만큼 증가 (최대 30%)\n- 가호 상태면, 턴 시작 시 수치만큼 합 위력 증가 얻음\n- 절망 상태면, 턴 시작 시 수치만큼 관통 위력 증가 얻음\n- 최댓값 : 3
   źródło: BattleKeywords-walpu6.json :: dataList[id=SwordCutwithTear].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 5 Deep Tears\n· At 3 Stack, gain additional 5 Deep Tears\n- Turn End: lose (Stack x 15) SP\n- Base Attack Skills deal +(Stack x 10)% damage (max 30%)\n- If this unit has Blessing, gain Clash Power Up by the effect's Stack at Turn Start\n- If this unit has Despair, gain Pierce Power Up by the effect's Stack at Turn Start\n- Max Stack: 3
   PL: - Na początku tury zyskuje 5 Głębokich Łez\n · Przy 3 stosach dodatkowo 5 Głębokich Łez\n- Na koniec tury traci (stosy x 15) Poczytalności\n- Podstawowe Umiejętności ataku zadają +(stosy x 10)% obrażeń (maks. 30%)\n- W stanie Błogosławieństwa na początku tury zyskuje tyle Wzrostów Mocy Starcia, ile wynosi stos tego efektu\n- W stanie Rozpaczy na początku tury zyskuje tyle Wzrostów Mocy Przebicia, ile wynosi stos tego efektu\n- Maks. stosów: 3
189. [Słowo kluczowe [BlackTearsAlly] — nazwa] 깊은 눈물
   źródło: BattleKeywords-walpu6.json :: dataList[id=BlackTearsAlly].name
   kontekst: identyfikator tagu w tekstach: `[BlackTearsAlly]`
   limit: do 40 znaków
   EN: Deep Tears
   PL: Głębokie Łzy
190. [Słowo kluczowe [BlackTearsAlly] — opis] - 특수 충전 (위력 고정)\n- 소모 시, 특정 스킬의 능력이 상승함\n- 최댓값 : 20
   źródło: BattleKeywords-walpu6.json :: dataList[id=BlackTearsAlly].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Charge (fixed Potency)\n- Resource used by certain skills for additional effects\n- Max Stack: 20
   PL: - Szczególne ładowanie (stała moc)\n- Zasób zużywany przez określone Umiejętności dla dodatkowych efektów\n- Maks.: 20
191. [Słowo kluczowe [KnightBless] — nazwa] 가호
   źródło: BattleKeywords-walpu6.json :: dataList[id=KnightBless].name
   kontekst: identyfikator tagu w tekstach: `[KnightBless]`
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Słowo kluczowe [KnightBless] — opis] - 턴 시작 시 보호 2 얻음\n- 1을 초과하는 물리 내성이 1로 조정됨 (흐트러짐 상태 제외)
   źródło: BattleKeywords-walpu6.json :: dataList[id=KnightBless].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 2 Protection\n- Adjust any Attack Type Resistances exceeding 1 to 1 (unless Staggered)
   PL: - Na początku tury zyskuje 2 Ochrony\n- Wszystkie Odporności fizyczne powyżej 1 są korygowane do 1 (poza stanem Oszołomienia)
193. [Słowo kluczowe [TraumaShield] — nazwa] 트라우마 방지장
   źródło: BattleKeywords-walpu6.json :: dataList[id=TraumaShield].name
   kontekst: identyfikator tagu w tekstach: `[TraumaShield]`
   limit: do 40 znaków
   EN: Trauma Shield
   PL: Osłona Przed Traumą
194. [Słowo kluczowe [TraumaShield] — opis] - 적에게 받는 정신력 피해 80% 감소\n- 침잠 피해 80% 감소\n- 턴 종료시 수치 1 감소
   źródło: BattleKeywords-walpu6.json :: dataList[id=TraumaShield].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Reduce SP damage from enemies by 80%\n- Reduce Sinking damage taken by 80%\n- Reduced by 1 at Turn End
   PL: - Otrzymuje -80% obrażeń Poczytalności od wrogów\n- Otrzymuje -80% obrażeń od Zatonięcia\n- Na koniec tury maleje o 1

## Słowa kluczowe bitwy — BattleKeywords-walpu8
- plik gry: `BattleKeywords-walpu8.json` (opisy wyświetlane w dymkach pomocy podczas walki)

195. [Słowo kluczowe [DesperadoBuff] — nazwa] 데스페라도
   źródło: BattleKeywords-walpu8.json :: dataList[id=DesperadoBuff].name
   kontekst: identyfikator tagu w tekstach: `[DesperadoBuff]`
   limit: do 40 znaków
   EN: Desperado
   PL: Desperado
196. [Słowo kluczowe [DesperadoBuff] — opis] - 최댓값: 2\n- 수치 1당, 기본 공격 스킬의 합 위력 +1, 기본 위력 +1\n- 수치가 2면, 기본 공격 스킬의 더하기 코인 위력 +1, 빼기 코인 위력 -1\n- 턴 종료 시 효과 소멸
   źródło: BattleKeywords-walpu8.json :: dataList[id=DesperadoBuff].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- For every Stack, Base Attack Skill Clash Power +1, Base Power +1\n- At 2 Stack, Base Attack Skill Plus Coin Power +1, Minus Coin Power -1\n- Expires at Turn End
   PL: - Maks. stosów: 2\n- Za każdy stos Moc Starcia podstawowych Umiejętności ataku +1, Moc bazowa +1\n- Przy 2 stosach monety plus podstawowych Umiejętności ataku zyskują +1 Mocy, a monety minus -1 Mocy\n- Znika na koniec tury
197. [Słowo kluczowe [TensionUp] — nazwa] 텐션 업
   źródło: BattleKeywords-walpu8.json :: dataList[id=TensionUp].name
   kontekst: identyfikator tagu w tekstach: `[TensionUp]`
   limit: do 40 znaków
   EN: Hyped-up
   PL: Rozkręcony
198. [Słowo kluczowe [TensionUp] — opis] - 최댓값: 3\n- 수치 1당, 분노, 색욕 속성 스킬로 가하는 피해량 +5%\n- 피격 시 (5 x 수치)만큼 흐트러짐 피해 입음\n- 턴 종료 시 효과 소멸
   źródło: BattleKeywords-walpu8.json :: dataList[id=TensionUp].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- For every Stack, deal +5% damage with Wrath and Lust Skills\n- When hit, raise this unit's Stagger Threshold by (5 x Stack)\n- Expires at Turn End
   PL: - Maks. stosów: 3\n- Za każdy stos zadaje +5% obrażeń Umiejętnościami Gniewu i Żądzy\n- Przy trafieniu otrzymuje (5 x stosy) obrażeń Oszołomienia\n- Znika na koniec tury
199. [Słowo kluczowe [PinkPetals] — nazwa] 분홍 꽃잎
   źródło: BattleKeywords-walpu8.json :: dataList[id=PinkPetals].name
   kontekst: identyfikator tagu w tekstach: `[PinkPetals]`
   limit: do 40 znaków
   EN: Pink Petals
   PL: Różowe Płatki
200. [Słowo kluczowe [PinkPetals] — opis] - 최댓값: 30\n- 수치 1당, 우울 속성 스킬로 피격 시 받는 피해량 +1% (최대 15%)\n- 수치 10당, 피격 시 침잠 횟수 1 증가 (턴당 2회)\n- 진동 폭발 시 (침잠 위력과 분홍 꽃잎 수치의 합/5)만큼 우울 피해\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-walpu8.json :: dataList[id=PinkPetals].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- For every Stack, take +1% damage when hit by Gloom Skills (max 15%)\n- For every 10 Stack, gain +1 Sinking Count when hit (2 times per turn)\n- When Tremor Burst is triggered on this unit, take ((Sinking Potency + Pink Petals) / 5) Gloom damage\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 30\n- Za każdy stos otrzymuje +1% obrażeń przy trafieniu Umiejętnościami Posępności (maks. 15%)\n- Za każde 10 stosów zyskuje +1 Licznika Zatonięcia przy trafieniu (2 na turę)\n- Po wywołaniu Wybuchu Wstrząsu otrzymuje (Moc Zatonięcia + Różowe Płatki)/5 obrażeń Posępnością\n- Na koniec tury maleje o 1
201. [Słowo kluczowe [QueenBeepheromone] — nazwa] 페로몬
   źródło: BattleKeywords-walpu8.json :: dataList[id=QueenBeepheromone].name
   kontekst: identyfikator tagu w tekstach: `[QueenBeepheromone]`
   limit: do 40 znaków
   EN: Pheromone
   PL: Feromon
202. [Słowo kluczowe [QueenBeepheromone] — opis] - 도발치 10 증가\n- 피격 시 대상에게 화상 3 부여
   źródło: BattleKeywords-walpu8.json :: dataList[id=QueenBeepheromone].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +10 Aggro\n- When hit, inflict 3 Burn on target
   PL: - Wartość Prowokacji +10\n- Przy trafieniu nadaje celowi 3 Podpalenia
203. [Słowo kluczowe [QueenBeeMark] — nazwa] 페로몬 표식
   źródło: BattleKeywords-walpu8.json :: dataList[id=QueenBeeMark].name
   kontekst: identyfikator tagu w tekstach: `[QueenBeeMark]`
   limit: do 40 znaków
   EN: Pheromone Mark
   PL: Znak Feromonów
204. [Słowo kluczowe [QueenBeeMark] — opis] - 자신의 화상 수치 3당, 피격시 받는 피해량 +1% (최대 20%)\n- 턴 종료 시 효과 소멸
   źródło: BattleKeywords-walpu8.json :: dataList[id=QueenBeeMark].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 3 Burn on self, take +1% damage when hit (max 20%)\n- Expires at Turn End
   PL: - Za każde 3 Podpalenia na sobie otrzymuje +1% obrażeń przy trafieniu (maks. 20%)\n- Znika na koniec tury
205. [Słowo kluczowe [RunHallway] — nazwa] 무리 이동 준비
   źródło: BattleKeywords-walpu8.json :: dataList[id=RunHallway].name
   kontekst: identyfikator tagu w tekstach: `[RunHallway]`
   limit: do 40 znaków
   EN: Preparing Herd Migration
   PL: Przygotowanie do Wędrówki Stada
206. [Słowo kluczowe [RunHallway] — opis] - 최댓값: 3\n- 전투 시작 시 1 감소\n- 0이 되면, 턴 시작 시 '무리 이동' 스킬 사용
   źródło: BattleKeywords-walpu8.json :: dataList[id=RunHallway].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Combat Start: Lose 1 Stack\n- At 0 Stack, use 'Herd Migration' at Turn Start
   PL: - Maks. stosów: 3\n- Na początku walki traci 1 stos\n- Przy 0 stosach używa na początku tury Umiejętności „Wędrówka Stada”
207. [Słowo kluczowe [NextHallway] — nazwa] 무리 이주
   źródło: BattleKeywords-walpu8.json :: dataList[id=NextHallway].name
   kontekst: identyfikator tagu w tekstach: `[NextHallway]`
   limit: do 40 znaków
   EN: Herd Relocation
   PL: Wędrówka Stada
208. [Słowo kluczowe [NextHallway] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함\n(강제 흐트러짐 제외, 사망으로 처리되지 않음)\n- 연속 전투 인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동
   źródło: BattleKeywords-walpu8.json :: dataList[id=NextHallway].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and escape from the Encounter\n(excluding forced Stagger; does not count as death)\n- In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order
   PL: - Na koniec tury wychodzi z Oszołomienia i opuszcza walkę\n(poza wymuszonym Oszołomieniem; nie liczy się jako śmierć)\n- W walkach łańcuchowych przy odwrocie przekazuje liczbę swoich slotów jednostce zastępującej, po czym przenosi się na koniec kolejki jednostek rezerwowych
209. [Słowo kluczowe [PumpkinJelly] — nazwa] 오렌지맛 뀽뀽이
   źródło: BattleKeywords-walpu8.json :: dataList[id=PumpkinJelly].name
   kontekst: identyfikator tagu w tekstach: `[PumpkinJelly]`
   limit: do 40 znaków
   EN: BongBong Orange
   PL: Pomarańczowy BongBong
210. [Słowo kluczowe [PumpkinJelly] — opis] - 최댓값: 1\n턴 시작 시 현재 체력이 최대 체력의 60% 미만이면, 최대 체력의 30% 만큼 체력 회복하고 버프 소멸
   źródło: BattleKeywords-walpu8.json :: dataList[id=PumpkinJelly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\nTurn Start: At less than 60% HP, heal 30% HP and lose this effect
   PL: - Maks. stosów: 1\nNa początku tury, przy HP poniżej 60% maks., leczy 30% Maks. HP, a błogosławieństwo znika
211. [Słowo kluczowe [BestWelfareTeamCaptain] — nazwa] 복지팀 팀장
   źródło: BattleKeywords-walpu8.json :: dataList[id=BestWelfareTeamCaptain].name
   kontekst: identyfikator tagu w tekstach: `[BestWelfareTeamCaptain]`
   limit: do 40 znaków
   EN: Welfare Team Captain
   PL: Kapitan Zespołu Dobrobytu
212. [Słowo kluczowe [BestWelfareTeamCaptain] — opis] - 해당 캐릭터의 슬롯 +1, 1스킬 수량 -1, 3스킬 수량 +1\n- 자신이 스킬로 화상, 출혈, 파열, 침잠, 진동 위력을 부여할 때, 부여값 +2  (특수 상태이상 포함)\n- 탄환을 얻음 또는 소모하는 기본 스킬의 피해량 + 30%\n- 탄환을 얻음 또는 소모하는 기본 스킬 사용 시 자신을 포함하여, 정신력이 가장 낮은 아군 1명 정신력 10 회복\n- 적 처치시 다음 효과 발동\n· 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1\n· 다음 턴에 해당 적이 보유했던 화상, 출혈, 파열, 침잠, 진동의 위력과 횟수를 각각 모든 적에게 무작위로 부여. (최소 1)
   źródło: BattleKeywords-walpu8.json :: dataList[id=BestWelfareTeamCaptain].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n  - Modify Skill pool: Gain 1 copy of Skill 3, but lose 1 copy of Skill 1\n- Increase the amount of Burn, Bleed, Rupture, Sinking, or Tremor Potency inflicted with Skills by +2 (including 'Unique Status Effects')\n- Base Skills that gain or spend Ammo deal +30% damage\n- On Use with Base Skills that gain or spend Ammo, heal 10 SP for 1 ally with the lowest SP (including this unit)\n- On Kill, activate the following:\n· E.G.O Resource +2 to the Affinity that killed the enemy; E.G.O Resource +1 to all Affinities\n· Next turn, inflict the remaining Burn, Bleed, Rupture, Sinking, and Tremor Potency and Count on the said enemy randomly between all enemies (min 1)
   PL: - Sloty tej postaci: +1; liczba Umiejętności 1: -1; liczba Umiejętności 3: +1\n- Gdy Umiejętnościami nadaje Moc Podpalenia, Krwawienia, Rozdarcia, Zatonięcia lub Wstrząsu, wartość nadania +2 (również szczególne stany)\n- Podstawowe Umiejętności, które zyskują lub zużywają Amunicję, zadają +30% obrażeń\n- Przy użyciu takich podstawowych Umiejętności leczy 10 Poczytalności u 1 sojusznika z najniższą Poczytalnością (wliczając siebie)\n- Przy zabiciu wroga:\n· +2 zasobu E.G.O atrybutu zabijającej Umiejętności, +1 zasobu każdego pozostałego atrybutu\n· W następnej turze losowo rozdziela pozostałą wrogu Moc i Licznik Podpalenia, Krwawienia, Rozdarcia, Zatonięcia i Wstrząsu między wszystkich wrogów (min. 1)

## Słowa kluczowe bitwy — BattleKeywords-x1p1c1
- plik gry: `BattleKeywords-x1p1c1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

213. [Słowo kluczowe [LeakedOutSauce] — nazwa] 새어나온 양념장
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=LeakedOutSauce].name
   kontekst: identyfikator tagu w tekstach: `[LeakedOutSauce]`
   limit: do 40 znaków
   EN: Leaking Marinade
   PL: Wyciekająca Marynata
214. [Słowo kluczowe [LeakedOutSauce] — opis] - 턴 종료 시 수치 2당, 다음 턴에 신속 1 얻음 (최대 10)\n- 턴 종료 시 소멸
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=LeakedOutSauce].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain 1 Haste next turn for every 2 Stack (max 10)\n- Expires at Turn End
   PL: - Na koniec tury: 1 Pośpiech w następnej turze za każde 2 stosy (maks. 10)\n- Znika na koniec tury
215. [Słowo kluczowe [DeliciousSauce] — nazwa] 황금 비법 소스
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=DeliciousSauce].name
   kontekst: identyfikator tagu w tekstach: `[DeliciousSauce]`
   limit: do 40 znaków
   EN: Golden Recipe Sauce
   PL: Złoty Sekretny Sos
216. [Słowo kluczowe [DeliciousSauce] — opis] - 합 위력 +2
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=DeliciousSauce].desc
   limit: do 120 znaków
   EN: - Clash Power +2
   PL: - Moc Starcia +2
217. [Słowo kluczowe [Yummy_Lowmorale] — nazwa] 맛있어짐
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Lowmorale].name
   kontekst: identyfikator tagu w tekstach: `[Yummy_Lowmorale]`
   limit: do 40 znaków
   EN: Yummers
   PL: Coraz Smaczniejsze
218. [Słowo kluczowe [Yummy_Lowmorale] — opis] - 사기 저하\n- 턴 시작시 취약 1 얻음
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Lowmorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile
   PL: - Spadek Moralu\n- Na początku tury zyskuje 1 Wrażliwość
219. [Słowo kluczowe [Yummy_Lowmorale] — podsumowanie] 취약 얻음
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Lowmorale].summary
   limit: do 120 znaków
   EN: Gain Fragile
   PL: Zyskuje Wrażliwość
220. [Słowo kluczowe [Yummy_Panic] — nazwa] 맛있어짐
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Yummy_Panic]`
   (powtórzenie elementu 217 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Słowo kluczowe [Yummy_Panic] — opis] - 패닉\n- 턴 시작시 취약 2 얻음
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wrażliwości
222. [Słowo kluczowe [Yummy_Panic] — podsumowanie] 취약 얻음
   źródło: BattleKeywords-x1p1c1.json :: dataList[id=Yummy_Panic].summary
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-ycgd
- plik gry: `BattleKeywords-ycgd.json` (opisy wyświetlane w dymkach pomocy podczas walki)

223. [Słowo kluczowe [Grudge] — nazwa] 맺혀가는 응어리
   źródło: BattleKeywords-ycgd.json :: dataList[id=Grudge].name
   kontekst: identyfikator tagu w tekstach: `[Grudge]`
   limit: do 40 znaków
   EN: Growing Resentment
   PL: Narastający Żal
224. [Słowo kluczowe [Grudge] — opis] 버프가 있을 때, 받은 피해량만큼 수치를 얻음. 턴 종료 시 소멸됨
   źródło: BattleKeywords-ycgd.json :: dataList[id=Grudge].desc
   limit: do 140 znaków
   EN: When this unit has a relevant buff: gain Growing Resentment equal to damage taken. Expires at Turn End
   PL: Mając odpowiednie błogosławieństwo, zyskuje wartość równą otrzymanym obrażeniom. Znika na koniec tury
225. [Słowo kluczowe [AaCePbBg] — nazwa] 원한
   źródło: BattleKeywords-ycgd.json :: dataList[id=AaCePbBg].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBg]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
226. [Słowo kluczowe [AaCePbBg] — opis] 턴 시작 시 피해량 증가 2, 방어 레벨 감소 3을 얻음
   źródło: BattleKeywords-ycgd.json :: dataList[id=AaCePbBg].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Damage Up and 3 Defense Level Down
   PL: Na początku tury zyskuje 2 Wzrosty Obrażeń i 3 Spadki Poziomu Obrony
227. [Słowo kluczowe [AaCePbBh] — nazwa] 원한
   źródło: BattleKeywords-ycgd.json :: dataList[id=AaCePbBh].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBh]`
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Słowo kluczowe [AaCePbBh] — opis] 턴 시작 시 공격 위력 증가 1, 방어 레벨 감소 5를 얻음
   źródło: BattleKeywords-ycgd.json :: dataList[id=AaCePbBh].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Attack Power Up and 5 Defense Level Down
   PL: Na początku tury zyskuje 1 Wzrost Mocy Ataku i 5 Spadków Poziomu Obrony

## Słowa kluczowe bitwy — BattleKeywords
- plik gry: `BattleKeywords.json` (opisy wyświetlane w dymkach pomocy podczas walki)

229. [Słowo kluczowe [AreaAtk] — nazwa] 광역 공격
   źródło: BattleKeywords.json :: dataList[id=AreaAtk].name
   kontekst: identyfikator tagu w tekstach: `[AreaAtk]`
   limit: do 40 znaków
   EN: AoE Attack
   PL: Atak Obszarowy
230. [Słowo kluczowe [AreaAtk] — opis] 2명 이상의 적을 공격
   źródło: BattleKeywords.json :: dataList[id=AreaAtk].desc
   limit: do 120 znaków
   EN: Targets 2 or more foes.
   PL: Atakuje 2 lub więcej wrogów
231. [Słowo kluczowe [Enhancement] — nazwa] 공격 위력 증가
   źródło: BattleKeywords.json :: dataList[id=Enhancement].name
   kontekst: identyfikator tagu w tekstach: `[Enhancement]`
   limit: do 40 znaków
   EN: Attack Power Up
   PL: Wzrost Mocy Ataku
232. [Słowo kluczowe [Enhancement] — opis] 한 턴동안 공격 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=Enhancement].desc
   limit: do 120 znaków
   EN: Attack skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności ataku rośnie o wartość efektu
233. [Słowo kluczowe [Agility] — nazwa] 신속
   źródło: BattleKeywords.json :: dataList[id=Agility].name
   kontekst: identyfikator tagu w tekstach: `[Agility]`
   limit: do 40 znaków
   EN: Haste
   PL: Pośpiech
234. [Słowo kluczowe [Agility] — opis] 한 턴 동안 속도가 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=Agility].desc
   limit: do 120 znaków
   EN: Speed increases by the effect’s Count for one turn.
   PL: W tej turze Szybkość rośnie o wartość efektu
235. [Słowo kluczowe [Endurance] — nazwa] 수비 위력 증가
   źródło: BattleKeywords.json :: dataList[id=Endurance].name
   kontekst: identyfikator tagu w tekstach: `[Endurance]`
   limit: do 40 znaków
   EN: Defense Power Up
   PL: Wzrost Mocy Obrony
236. [Słowo kluczowe [Endurance] — opis] 한 턴 동안 수비 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=Endurance].desc
   limit: do 120 znaków
   EN: Defense skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności obrony rośnie o wartość efektu
237. [Słowo kluczowe [Reduction] — nazwa] 공격 위력 감소
   źródło: BattleKeywords.json :: dataList[id=Reduction].name
   kontekst: identyfikator tagu w tekstach: `[Reduction]`
   limit: do 40 znaków
   EN: Attack Power Down
   PL: Spadek Mocy Ataku
238. [Słowo kluczowe [Reduction] — opis] 한 턴 동안 공격 스킬의 최종 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=Reduction].desc
   limit: do 120 znaków
   EN: Attack skills lose final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności ataku maleje o wartość efektu
239. [Słowo kluczowe [Binding] — nazwa] 속박
   źródło: BattleKeywords.json :: dataList[id=Binding].name
   kontekst: identyfikator tagu w tekstach: `[Binding]`
   limit: do 40 znaków
   EN: Bind
   PL: Spętanie
240. [Słowo kluczowe [Binding] — opis] 한 턴 동안 속도가 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=Binding].desc
   limit: do 120 znaków
   EN: Speed decreases by the effect’s Count for one turn.
   PL: W tej turze Szybkość maleje o wartość efektu
241. [Słowo kluczowe [Vulnerable] — nazwa] 취약
   źródło: BattleKeywords.json :: dataList[id=Vulnerable].name
   kontekst: identyfikator tagu w tekstach: `[Vulnerable]`
   limit: do 40 znaków
   EN: Fragile
   PL: Wrażliwość
242. [Słowo kluczowe [Vulnerable] — opis] 한 턴 동안 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=Vulnerable].desc
   limit: do 120 znaków
   EN: Take more damage from skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności rosną proporcjonalnie do wartości efektu (maks. 10)
243. [Słowo kluczowe [Vulnerable] — podsumowanie] 받는 피해량 +{0}0
   źródło: BattleKeywords.json :: dataList[id=Vulnerable].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}0% Damage Taken
   PL: Otrzymywane Obrażenia +{0}0
244. [Słowo kluczowe [Taunt] — nazwa] 도발
   źródło: BattleKeywords.json :: dataList[id=Taunt].name
   kontekst: identyfikator tagu w tekstach: `[Taunt]`
   limit: do 40 znaków
   EN: Taunt
   PL: Prowokacja
245. [Słowo kluczowe [Stun] — nazwa] 기절
   źródło: BattleKeywords.json :: dataList[id=Stun].name
   kontekst: identyfikator tagu w tekstach: `[Stun]`
   limit: do 40 znaków
   EN: Stun
   PL: Ogłuszenie
246. [Słowo kluczowe [ElectricShock] — nazwa] 감전
   źródło: BattleKeywords.json :: dataList[id=ElectricShock].name
   kontekst: identyfikator tagu w tekstach: `[ElectricShock]`
   limit: do 40 znaków
   EN: Shock
   PL: Porażenie
247. [Słowo kluczowe [ElectricShock] — opis] 이번 턴동안 받는 피해가 수치만큼 고정 증가
   źródło: BattleKeywords.json :: dataList[id=ElectricShock].desc
   limit: do 120 znaków
   EN: Take more damage by the effect’s value for the turn
   PL: W tej turze otrzymywane obrażenia rosną o wartość efektu
248. [Słowo kluczowe [Burn] — nazwa] 화상
   źródło: BattleKeywords.json :: dataList[id=Burn].name
   kontekst: identyfikator tagu w tekstach: `[Burn]`
   limit: do 40 znaków
   EN: Burn
   PL: Podpalenie
249. [Słowo kluczowe [Burn] — opis] 턴 종료 시 스택만큼 고정 피해를 받고 절반 감소
   źródło: BattleKeywords.json :: dataList[id=Burn].desc
   limit: do 120 znaków
   EN: At the end of the turn, take fixed damage by the effect’s Count, then halve it.
   PL: Na koniec tury otrzymuje obrażenia stałe równe Licznikowi, po czym Licznik maleje o połowę
250. [Słowo kluczowe [Bleeding] — nazwa] 출혈
   źródło: BattleKeywords.json :: dataList[id=Bleeding].name
   kontekst: identyfikator tagu w tekstach: `[Bleeding]`
   limit: do 40 znaków
   EN: Bleed
   PL: Krwawienie
251. [Słowo kluczowe [Bleeding] — opis] 공격 시작 시 현재 체력의 (스택)%만큼 고정 피해를 받고 절반 감소
   źródło: BattleKeywords.json :: dataList[id=Bleeding].desc
   limit: do 120 znaków
   EN: When attacking, take fixed damage equal to (Count)% of current HP, then halve it.
   PL: Na początku ataku otrzymuje obrażenia stałe równe (Licznik)% aktualnego HP, po czym Licznik maleje o połowę
252. [Słowo kluczowe [Target] — nazwa] 표적
   źródło: BattleKeywords.json :: dataList[id=Target].name
   kontekst: identyfikator tagu w tekstach: `[Target]`
   limit: do 40 znaków
   EN: Marked
   PL: Oznaczony
253. [Słowo kluczowe [Target] — opis] [날카로운 칼] 패시브를 가지고 있는 캐릭터의 공격 대상이 됨
   źródło: BattleKeywords.json :: dataList[id=Target].desc
   limit: do 120 znaków
   EN: Targeted by the character with the Passive [Sharp Edge].
   PL: Staje się celem postaci posiadającej pasyw [Ostre Ostrze]
254. [Słowo kluczowe [SelfHarm_LowMorale] — nazwa] 자해
   źródło: BattleKeywords.json :: dataList[id=SelfHarm_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[SelfHarm_LowMorale]`
   limit: do 40 znaków
   EN: Compulsion
   PL: Samookaleczenie
255. [Słowo kluczowe [SelfHarm_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 신속, 취약 2를 얻음
   źródło: BattleKeywords.json :: dataList[id=SelfHarm_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Haste and 2 Fragile
   PL: - Spadek Moralu\n- Na początku tury zyskuje 2 Pośpiechu i 2 Wrażliwości
256. [Słowo kluczowe [SelfHarm_Panic] — nazwa] 자해
   źródło: BattleKeywords.json :: dataList[id=SelfHarm_Panic].name
   kontekst: identyfikator tagu w tekstach: `[SelfHarm_Panic]`
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Słowo kluczowe [SelfHarm_Panic] — opis] - 패닉\n- 턴 시작 시 자신의 체력 -10
   źródło: BattleKeywords.json :: dataList[id=SelfHarm_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Lose 10 HP
   PL: - Panika\n- Na początku tury traci 10 HP
258. [Słowo kluczowe [Blame_LowMorale] — nazwa] 비난
   źródło: BattleKeywords.json :: dataList[id=Blame_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Blame_LowMorale]`
   limit: do 40 znaków
   EN: Outlash
   PL: Pogarda
259. [Słowo kluczowe [Blame_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 공격 위력 증가, 취약 2를 얻음
   źródło: BattleKeywords.json :: dataList[id=Blame_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Attack Power Up and 2 Fragile
   PL: - Spadek Moralu\n- Na początku tury zyskuje 2 Wzrosty Mocy Ataku i 2 Wrażliwości
260. [Słowo kluczowe [Blame_Panic] — nazwa] 비난
   źródło: BattleKeywords.json :: dataList[id=Blame_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Blame_Panic]`
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Słowo kluczowe [Blame_Panic] — opis] - 패닉\n- 턴 시작 시 무작위 아군의 정신력 -20
   źródło: BattleKeywords.json :: dataList[id=Blame_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: A random ally loses 20 SP
   PL: - Panika\n- Na początku tury losowy sojusznik traci 20 Poczytalności
262. [Słowo kluczowe [Charge] — nazwa] 충전
   źródło: BattleKeywords.json :: dataList[id=Charge].name
   kontekst: identyfikator tagu w tekstach: `[Charge]`
   limit: do 40 znaków
   EN: Charge
   PL: Ładowanie
263. [Słowo kluczowe [Charge] — opis] 소모 시 특정 스킬의 능력이 상승함. 횟수를 최대 20까지 얻을 수 있음. 턴 종료 시 횟수 1 감소.
   źródło: BattleKeywords.json :: dataList[id=Charge].desc
   limit: do 170 znaków
   EN: Resource used by certain skills for additional effects. Its Count can go up to 20. Count lowers by 1 at the end of each turn.
   PL: Zasób zużywany przez określone Umiejętności dla dodatkowych efektów. Licznik może osiągnąć do 20. Na koniec tury Licznik maleje o 1.
264. [Słowo kluczowe [DamageOverTime] — nazwa] 지속 피해
   źródło: BattleKeywords.json :: dataList[id=DamageOverTime].name
   kontekst: identyfikator tagu w tekstach: `[DamageOverTime]`
   limit: do 40 znaków
   EN: Ongoing Damage
   PL: Obrażenia Ciągłe
265. [Słowo kluczowe [DamageOverTime] — opis] 턴 시작 시 스택만큼 고정 피해를 입음
   źródło: BattleKeywords.json :: dataList[id=DamageOverTime].desc
   limit: do 120 znaków
   EN: At the start of the turn, take fixed damage by the effect’s Count.
   PL: Na początku tury otrzymuje obrażenia stałe równe Licznikowi
266. [Słowo kluczowe [ResultEnhancement] — nazwa] 위력 증가
   źródło: BattleKeywords.json :: dataList[id=ResultEnhancement].name
   kontekst: identyfikator tagu w tekstach: `[ResultEnhancement]`
   limit: do 40 znaków
   EN: Power Up
   PL: Wzrost Mocy
267. [Słowo kluczowe [ResultEnhancement] — opis] 한 턴 동안 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=ResultEnhancement].desc
   limit: do 120 znaków
   EN: Skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności rośnie o wartość efektu
268. [Słowo kluczowe [ResultEnhancement] — podsumowanie] 스킬의 최종 위력 +{0}
   źródło: BattleKeywords.json :: dataList[id=ResultEnhancement].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności +{0}
269. [Słowo kluczowe [Protection] — nazwa] 보호
   źródło: BattleKeywords.json :: dataList[id=Protection].name
   kontekst: identyfikator tagu w tekstach: `[Protection]`
   limit: do 40 znaków
   EN: Protection
   PL: Ochrona
270. [Słowo kluczowe [Protection] — opis] 한 턴 동안 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=Protection].desc
   limit: do 120 znaków
   EN: Take less damage from skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności maleją proporcjonalnie do wartości efektu (maks. 10)
271. [Słowo kluczowe [Protection] — podsumowanie] 받는 피해량 -{0}
   źródło: BattleKeywords.json :: dataList[id=Protection].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: -{0}0% Damage Taken
   PL: Otrzymywane Obrażenia -{0}
272. [Słowo kluczowe [AttackDmgUp] — nazwa] 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=AttackDmgUp].name
   kontekst: identyfikator tagu w tekstach: `[AttackDmgUp]`
   limit: do 40 znaków
   EN: Damage Up
   PL: Wzrost Obrażeń
273. [Słowo kluczowe [AttackDmgUp] — opis] 한 턴 동안 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AttackDmgUp].desc
   limit: do 120 znaków
   EN: Deal more damage with skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia od Umiejętności rosną proporcjonalnie do wartości efektu (maks. 10)
274. [Słowo kluczowe [AttackDmgUp] — podsumowanie] 가하는 피해량 +{0}0%
   źródło: BattleKeywords.json :: dataList[id=AttackDmgUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}0% Damage Dealt
   PL: Zadawane Obrażenia +{0}0%
275. [Słowo kluczowe [DefenseUp] — nazwa] 방어 레벨 증가
   źródło: BattleKeywords.json :: dataList[id=DefenseUp].name
   kontekst: identyfikator tagu w tekstach: `[DefenseUp]`
   limit: do 40 znaków
   EN: Defense Level Up
   PL: Wzrost Poziomu Obrony
276. [Słowo kluczowe [DefenseUp] — opis] 한 턴 동안 방어 레벨이 수치에 비례하여 증가
   źródło: BattleKeywords.json :: dataList[id=DefenseUp].desc
   limit: do 120 znaków
   EN: Defense Level increases based on the effect's Potency for one turn.
   PL: W tej turze Poziom Obrony rośnie proporcjonalnie do Mocy efektu
277. [Słowo kluczowe [DefenseUp] — podsumowanie] 방어 레벨 +{0}
   źródło: BattleKeywords.json :: dataList[id=DefenseUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level +{0}
   PL: Poziom Obrony +{0}
278. [Słowo kluczowe [PlusCoinValueUp] — nazwa] 더하기 코인 강화
   źródło: BattleKeywords.json :: dataList[id=PlusCoinValueUp].name
   kontekst: identyfikator tagu w tekstach: `[PlusCoinValueUp]`
   limit: do 40 znaków
   EN: Plus Coin Boost
   PL: Wzmocnienie Monet Plus
279. [Słowo kluczowe [PlusCoinValueUp] — opis] 더하기 코인 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=PlusCoinValueUp].desc
   limit: do 120 znaków
   EN: Raise the Power of Plus Coins by the effect’s Count.
   PL: Moc monet plus rośnie o wartość efektu
280. [Słowo kluczowe [MinusCoinValueUp] — nazwa] 빼기 코인 강화
   źródło: BattleKeywords.json :: dataList[id=MinusCoinValueUp].name
   kontekst: identyfikator tagu w tekstach: `[MinusCoinValueUp]`
   limit: do 40 znaków
   EN: Minus Coin Boost
   PL: Wzmocnienie Monet Minus
281. [Słowo kluczowe [MinusCoinValueUp] — opis] 빼기 코인 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=MinusCoinValueUp].desc
   limit: do 120 znaków
   EN: Raise the Power of Minus Coins by the effect’s Count.
   PL: Moc monet minus rośnie o wartość efektu
282. [Słowo kluczowe [TimesCoinValueUp] — nazwa] 곱하기 코인 강화
   źródło: BattleKeywords.json :: dataList[id=TimesCoinValueUp].name
   kontekst: identyfikator tagu w tekstach: `[TimesCoinValueUp]`
   limit: do 40 znaków
   EN: Multiply Coin Boost
   PL: Wzmocnienie Monet Mnożenia
283. [Słowo kluczowe [TimesCoinValueUp] — opis] 곱하기 코인 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=TimesCoinValueUp].desc
   limit: do 120 znaków
   EN: Raise the Power of Multiply Coins by the effect’s Count.
   PL: Moc monet mnożenia rośnie o wartość efektu
284. [Słowo kluczowe [Disarming] — nazwa] 수비 위력 감소
   źródło: BattleKeywords.json :: dataList[id=Disarming].name
   kontekst: identyfikator tagu w tekstach: `[Disarming]`
   limit: do 40 znaków
   EN: Defense Power Down
   PL: Spadek Mocy Obrony
285. [Słowo kluczowe [Disarming] — opis] 한 턴 동안 수비 스킬의 최종 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=Disarming].desc
   limit: do 120 znaków
   EN: Defense skills lose final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności obrony maleje o wartość efektu
286. [Słowo kluczowe [ResultReduction] — nazwa] 위력 감소
   źródło: BattleKeywords.json :: dataList[id=ResultReduction].name
   kontekst: identyfikator tagu w tekstach: `[ResultReduction]`
   limit: do 40 znaków
   EN: Power Down
   PL: Spadek Mocy
287. [Słowo kluczowe [ResultReduction] — opis] 한 턴 동안 스킬의 최종 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=ResultReduction].desc
   limit: do 120 znaków
   EN: All skills lose final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności maleje o wartość efektu
288. [Słowo kluczowe [ResultReduction] — podsumowanie] 스킬의 최종 위력 -{0}
   źródło: BattleKeywords.json :: dataList[id=ResultReduction].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności -{0}
289. [Słowo kluczowe [AttackDmgDown] — nazwa] 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=AttackDmgDown].name
   kontekst: identyfikator tagu w tekstach: `[AttackDmgDown]`
   limit: do 40 znaków
   EN: Damage Down
   PL: Spadek Obrażeń
290. [Słowo kluczowe [AttackDmgDown] — opis] 한 턴 동안 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AttackDmgDown].desc
   limit: do 120 znaków
   EN: Deal less damage with skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia od Umiejętności maleją proporcjonalnie do wartości efektu (maks. 10)
291. [Słowo kluczowe [AttackDmgDown] — podsumowanie] 가하는 피해량 -{0}0%
   źródło: BattleKeywords.json :: dataList[id=AttackDmgDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: -{0}0% Damage Dealt
   PL: Zadawane Obrażenia -{0}0%
292. [Słowo kluczowe [DefenseDown] — nazwa] 방어 레벨 감소
   źródło: BattleKeywords.json :: dataList[id=DefenseDown].name
   kontekst: identyfikator tagu w tekstach: `[DefenseDown]`
   limit: do 40 znaków
   EN: Defense Level Down
   PL: Spadek Poziomu Obrony
293. [Słowo kluczowe [DefenseDown] — opis] 한 턴 동안 방어 레벨이 수치에 비례하여 감소
   źródło: BattleKeywords.json :: dataList[id=DefenseDown].desc
   limit: do 120 znaków
   EN: Defense Level decreases based on the effect's Potency for one turn.
   PL: W tej turze Poziom Obrony maleje proporcjonalnie do Mocy efektu
294. [Słowo kluczowe [DefenseDown] — podsumowanie] 방어 레벨 -{0}
   źródło: BattleKeywords.json :: dataList[id=DefenseDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level -{0}
   PL: Poziom Obrony -{0}
295. [Słowo kluczowe [Paralysis] — nazwa] 마비
   źródło: BattleKeywords.json :: dataList[id=Paralysis].name
   kontekst: identyfikator tagu w tekstach: `[Paralysis]`
   limit: do 40 znaków
   EN: Paralyze
   PL: Paraliż
296. [Słowo kluczowe [Paralysis] — opis] 한 턴 동안 수치만큼 코인 위력이 0으로 고정
   źródło: BattleKeywords.json :: dataList[id=Paralysis].desc
   limit: do 120 znaków
   EN: Fix the Power of Coins to 0 for one turn, with one Coin per the effect’s Count.
   PL: W tej turze Moc tylu monet, ile wynosi wartość efektu, zostaje ustalona na 0
297. [Słowo kluczowe [PlusCoinValueDown] — nazwa] 더하기 코인 약화
   źródło: BattleKeywords.json :: dataList[id=PlusCoinValueDown].name
   kontekst: identyfikator tagu w tekstach: `[PlusCoinValueDown]`
   limit: do 40 znaków
   EN: Plus Coin Drop
   PL: Osłabienie Monet Plus
298. [Słowo kluczowe [PlusCoinValueDown] — opis] 한 턴 동안 더하기 코인 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=PlusCoinValueDown].desc
   limit: do 120 znaków
   EN: Reduce the power of Plus Coins by the effect’s Count.
   PL: W tej turze Moc monet plus maleje o wartość efektu
299. [Słowo kluczowe [MinusCoinValueDown] — nazwa] 빼기 코인 약화
   źródło: BattleKeywords.json :: dataList[id=MinusCoinValueDown].name
   kontekst: identyfikator tagu w tekstach: `[MinusCoinValueDown]`
   limit: do 40 znaków
   EN: Minus Coin Drop
   PL: Osłabienie Monet Minus
300. [Słowo kluczowe [MinusCoinValueDown] — opis] 한 턴 동안 빼기 코인 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=MinusCoinValueDown].desc
   limit: do 120 znaków
   EN: Reduce the power of Minus Coins by the effect’s Count.
   PL: W tej turze Moc monet minus maleje o wartość efektu
301. [Słowo kluczowe [TimesCoinValueDown] — nazwa] 곱하기 코인 약화
   źródło: BattleKeywords.json :: dataList[id=TimesCoinValueDown].name
   kontekst: identyfikator tagu w tekstach: `[TimesCoinValueDown]`
   limit: do 40 znaków
   EN: Multiply Coin Drop
   PL: Osłabienie Monet Mnożenia
302. [Słowo kluczowe [TimesCoinValueDown] — opis] 한 턴 동안 곱하기 코인 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=TimesCoinValueDown].desc
   limit: do 120 znaków
   EN: Reduce the power of Multiply Coins by the effect’s Count.
   PL: W tej turze Moc monet mnożenia maleje o wartość efektu
303. [Słowo kluczowe [MoonLight] — nazwa] 달빛
   źródło: BattleKeywords.json :: dataList[id=MoonLight].name
   kontekst: identyfikator tagu w tekstach: `[MoonLight]`
   limit: do 40 znaków
   EN: Moonlight
   PL: Światło Księżyca
304. [Słowo kluczowe [MoonLight] — opis] 특정 스킬 사용 시 달빛을 소모하여 추가 효과가 발동함
   źródło: BattleKeywords.json :: dataList[id=MoonLight].desc
   limit: do 120 znaków
   EN: Resource used by certain skills for additional effects.
   PL: Zasób zużywany przez określone Umiejętności dla dodatkowych efektów.
305. [Słowo kluczowe [Anger] — nazwa] 분노
   źródło: BattleKeywords.json :: dataList[id=Anger].name
   kontekst: identyfikator tagu w tekstach: `[Anger]`
   limit: do 40 znaków
   EN: Rage
   PL: Gniew
306. [Słowo kluczowe [Anger] — opis] 특정 스킬에 의해 소모됨. 분노를 소모하여 특정 스킬 사용
   źródło: BattleKeywords.json :: dataList[id=Anger].desc
   limit: do 120 znaków
   EN: Spent by certain skills. Required for the use of certain skills.
   PL: Zużywany przez określone Umiejętności. Niektóre Umiejętności wymagają jego zużycia.
307. [Słowo kluczowe [Inactible] — nazwa] 행동 불가
   źródło: BattleKeywords.json :: dataList[id=Inactible].name
   kontekst: identyfikator tagu w tekstach: `[Inactible]`
   limit: do 40 znaków
   EN: Immobilize
   PL: Unieruchomienie
308. [Słowo kluczowe [Inactible] — opis] 이번 턴 동안 행동하지 않음
   źródło: BattleKeywords.json :: dataList[id=Inactible].desc
   limit: do 120 znaków
   EN: Does not act for the turn.
   PL: Nie podejmuje działań w tej turze
309. [Słowo kluczowe [Combustion] — nazwa] 화상
   źródło: BattleKeywords.json :: dataList[id=Combustion].name
   kontekst: identyfikator tagu w tekstach: `[Combustion]`
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Słowo kluczowe [Combustion] — opis] 턴 종료 시, 효과 위력만큼 고정 체력 피해를 받음\n턴 종료 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Combustion].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the end of the turn, take fixed damage by the effect’s Potency.\nThen, reduce its Count by 1.
   PL: Na koniec tury otrzymuje obrażenia stałe równe Mocy efektu\nNastępnie Licznik maleje o 1
311. [Słowo kluczowe [Laceration] — nazwa] 출혈
   źródło: BattleKeywords.json :: dataList[id=Laceration].name
   kontekst: identyfikator tagu w tekstach: `[Laceration]`
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Słowo kluczowe [Laceration] — opis] 공격 스킬의 코인 판정 시, 효과 위력만큼 고정 체력 피해를 받음\n공격 스킬의 코인 판정 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Laceration].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When tossing an attack Coin, take fixed damage by the effect’s Potency.\nThen, reduce its Count by 1.
   PL: Przy rzucie monetą Umiejętności ataku otrzymuje obrażenia stałe równe Mocy efektu\nNastępnie Licznik maleje o 1
313. [Słowo kluczowe [Vibration] — nazwa] 진동
   źródło: BattleKeywords.json :: dataList[id=Vibration].name
   kontekst: identyfikator tagu w tekstach: `[Vibration]`
   limit: do 40 znaków
   EN: Tremor
   PL: Wstrząs
314. [Słowo kluczowe [Vibration] — opis] 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n턴 종료 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Vibration].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked by skills that trigger Tremor Burst, raise the Stagger Threshold by the effect’s Potency.\nAt the end of the turn, reduce the Count by 1.
   PL: Przy trafieniu Umiejętnością wywołującą Wybuch Wstrząsu podnosi Próg Oszołomienia o Moc efektu\nNa koniec tury Licznik maleje o 1
315. [Słowo kluczowe [Burst] — nazwa] 파열
   źródło: BattleKeywords.json :: dataList[id=Burst].name
   kontekst: identyfikator tagu w tekstach: `[Burst]`
   limit: do 40 znaków
   EN: Rupture
   PL: Rozdarcie
316. [Słowo kluczowe [Burst] — opis] 공격 스킬로 피격 시, 효과 위력만큼 고정 체력 피해를 받음\n피격 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Burst].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit by an attack, take fixed damage by the effect’s Potency.\nThen, reduce its Count by 1.
   PL: Przy trafieniu atakiem otrzymuje obrażenia stałe równe Mocy efektu\nNastępnie Licznik maleje o 1
317. [Słowo kluczowe [Sinking] — nazwa] 침잠
   źródło: BattleKeywords.json :: dataList[id=Sinking].name
   kontekst: identyfikator tagu w tekstach: `[Sinking]`
   limit: do 40 znaków
   EN: Sinking
   PL: Zatonięcie
318. [Słowo kluczowe [Sinking] — opis] 공격 스킬로 피격 시, 효과 위력만큼 고정 정신력 피해를 받음 (정신력이 없는 대상에게는 우울 속성 피해로 적용됨)\n피격 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Sinking].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When hit by an attack, take fixed SP damage by the effect’s Potency.\n(Non-SP Units take Gloom damage instead.)\nThen, reduce its Count by 1.
   PL: Przy trafieniu atakiem traci Poczytalność równą Mocy efektu (jednostki bez Poczytalności otrzymują obrażenia Posępnością)\nNastępnie Licznik maleje o 1
319. [Słowo kluczowe [Breath] — nazwa] 호흡
   źródło: BattleKeywords.json :: dataList[id=Breath].name
   kontekst: identyfikator tagu w tekstach: `[Breath]`
   limit: do 40 znaków
   EN: Poise
   PL: Oddech
320. [Słowo kluczowe [Breath] — opis] 적중 시 효과 위력에 비례한 확률로 치명타 피해를 입힘\n턴 종료 시, 치명타 발동 후 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=Breath].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On hit, gain a Potency-based chance to deal critical damage, reducing the Count by 1 if successful.\nAt the end of the turn, reduce the Count by 1.
   PL: Przy trafieniu zyskuje szansę na obrażenia krytyczne proporcjonalną do Mocy efektu; przy skutecznym trafieniu Licznik maleje o 1\nNa koniec tury Licznik maleje o 1
321. [Słowo kluczowe [BloodPocket] — nazwa] 피주머니
   źródło: BattleKeywords.json :: dataList[id=BloodPocket].name
   kontekst: identyfikator tagu w tekstach: `[BloodPocket]`
   limit: do 40 znaków
   EN: Blood Sac
   PL: Sakiewka Krwi
322. [Słowo kluczowe [BloodPocket] — opis] 특정 수치에 강력한 공격을 사용함.
   źródło: BattleKeywords.json :: dataList[id=BloodPocket].desc
   limit: do 120 znaków
   EN: Use a powerful attack after the Count reaches a certain amount.
   PL: Po osiągnięciu określonej wartości używa potężnego ataku.
323. [Słowo kluczowe [WaterPocket] — nazwa] 물주머니
   źródło: BattleKeywords.json :: dataList[id=WaterPocket].name
   kontekst: identyfikator tagu w tekstach: `[WaterPocket]`
   limit: do 40 znaków
   EN: Fluid Sac
   PL: Sakiewka Wody
324. [Słowo kluczowe [WaterPocket] — opis] 수치에 비례하여 체력을 회복함
   źródło: BattleKeywords.json :: dataList[id=WaterPocket].desc
   limit: do 120 znaków
   EN: Heals HP based on the Count.
   PL: Leczy HP proporcjonalnie do wartości
325. [Słowo kluczowe [DogThunder] — nazwa] 번개
   źródło: BattleKeywords.json :: dataList[id=DogThunder].name
   kontekst: identyfikator tagu w tekstach: `[DogThunder]`
   limit: do 40 znaków
   EN: Lightning
   PL: Piorun
326. [Słowo kluczowe [DogThunder] — opis] 특정 수치에 자신을 강화함.
   źródło: BattleKeywords.json :: dataList[id=DogThunder].desc
   limit: do 120 znaków
   EN: Powers up after the Count reaches a certain amount.
   PL: Po osiągnięciu określonej wartości się wzmacnia.
327. [Słowo kluczowe [Run_Panic] — nazwa] 압도
   źródło: BattleKeywords.json :: dataList[id=Run_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Run_Panic]`
   limit: do 40 znaków
   EN: Oppression
   PL: Przytłoczenie
328. [Słowo kluczowe [Run_Panic] — opis] 한 턴 동안 행동 불가. 피격 시 공격자의 스킬이 종료된 후 도주함.
   źródło: BattleKeywords.json :: dataList[id=Run_Panic].desc
   limit: do 120 znaków
   EN: Cannot act for one turn. When hit, flees battle after the attacker’s skill has finished.
   PL: Nie może działać przez jedną turę. Przy trafieniu ucieka z walki po zakończeniu Umiejętności atakującego.
329. [Słowo kluczowe [Operation] — nazwa] 시술
   źródło: BattleKeywords.json :: dataList[id=Operation].name
   kontekst: identyfikator tagu w tekstach: `[Operation]`
   limit: do 40 znaków
   EN: Surgery
   PL: Zabieg
330. [Słowo kluczowe [Operation] — opis] 이 수치가 5가 되면 사망함\n최대 체력이 수치에 비례하여 20%씩 감소 \n가하는 피해량이 수치에 비례하여 20%씩 증가\n매 턴마다 수치만큼 신속을 얻음
   źródło: BattleKeywords.json :: dataList[id=Operation].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Die when Count reaches 5.\nReduce Max HP by 20% (per Count).\nDeal 20% (per Count) more damage.\nAt the start of the turn, gain Haste by the effect’s Count.
   PL: Umiera, gdy Licznik osiągnie 5\nMaks. HP maleje o 20% za każdą wartość\nZadawane obrażenia rosną o 20% za każdą wartość\nNa początku każdej tury zyskuje tyle Pośpiechu, ile wynosi wartość
331. [Słowo kluczowe [Emergency_Operation] — nazwa] 긴급_시술
   źródło: BattleKeywords.json :: dataList[id=Emergency_Operation].name
   kontekst: identyfikator tagu w tekstach: `[Emergency_Operation]`
   limit: do 40 znaków
   EN: Makeshift Surgery
   PL: Zabieg Polowy
332. [Słowo kluczowe [Emergency_Operation] — opis] 자신의 '긴급 시술' 수에 비례하여 최대 체력이 25%, 위력이 1만큼 증가함.\nn매 턴마다 '긴급 시술'을 1 얻음\n'긴급 시술'이 5가 될 경우, 사망함
   źródło: BattleKeywords.json :: dataList[id=Emergency_Operation].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boost Max HP by 25% and skill Power by 1 per this effect’s Count.\nEach turn, increase this effect’s Count by 1.\nDie when Count reaches 5.
   PL: Maks. HP rośnie o 25%, a Moc Umiejętności o 1, proporcjonalnie do liczby własnych „Zabiegów Polowych”.\nCo turę zyskuje 1 „Zabiegu Polowego”\nGdy „Zabieg Polowy” osiągnie 5, umiera
333. [Słowo kluczowe [BabayagaTimeLimit] — nazwa] 다가오는 바바야가
   źródło: BattleKeywords.json :: dataList[id=BabayagaTimeLimit].name
   kontekst: identyfikator tagu w tekstach: `[BabayagaTimeLimit]`
   limit: do 40 znaków
   EN: Baba Yaga’s Coming!
   PL: Nadchodząca Baba Jaga
334. [Słowo kluczowe [PinkRibbon] — nazwa] 분홍 리본
   źródło: BattleKeywords.json :: dataList[id=PinkRibbon].name
   kontekst: identyfikator tagu w tekstach: `[PinkRibbon]`
   limit: do 40 znaków
   EN: Pink Ribbons
   PL: Różowa Wstążka
335. [Słowo kluczowe [PinkRibbon] — opis] 턴 종료 시 스택이 5 이상되면, 스택을 초기화하고 다음 턴 동안 '탐욕' 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=PinkRibbon].desc
   limit: do 120 znaków
   EN: At the end of the turn, if at 5+ Potency, remove this effect and apply ‘Desirous’ next turn.
   PL: Na koniec tury, jeśli Moc osiągnie 5 lub więcej, resetuje ją, a w następnej turze jednostka wpada w stan „Chciwości”
336. [Słowo kluczowe [Greedy] — nazwa] 탐욕
   źródło: BattleKeywords.json :: dataList[id=Greedy].name
   kontekst: identyfikator tagu w tekstach: `[Greedy]`
   limit: do 40 znaków
   EN: Desirous
   PL: Chciwość
337. [Słowo kluczowe [Greedy] — opis] 턴 시작 시 속박 10 얻음\n모든 물리 내성이 취약으로 변경됨\n공격 스킬의 스킬 위력 +2\n수비 스킬의 스킬 위력 -2
   źródło: BattleKeywords.json :: dataList[id=Greedy].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, gain 10 Bind.\nAll phys. resistances change to ‘Fatal’.\nAttack Skill Power +2.\nDefense Skill Power -2.
   PL: Na początku tury zyskuje 10 Spętań\nWszystkie Odporności fizyczne zmieniają się na „Wrażliwość”\nMoc Umiejętności ataku +2\nMoc Umiejętności obrony -2
338. [Słowo kluczowe [PinkRibbon_Ishmael] — nazwa] 분홍 리본
   źródło: BattleKeywords.json :: dataList[id=PinkRibbon_Ishmael].name
   kontekst: identyfikator tagu w tekstach: `[PinkRibbon_Ishmael]`
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Słowo kluczowe [PinkRibbon_Ishmael] — opis] 이번 턴 동안 공격 스킬의 코인을 사용할 때마다 수치 증가.\n턴 종료 시 수치만큼 속박을 얻은 뒤 효과 소멸
   źródło: BattleKeywords.json :: dataList[id=PinkRibbon_Ishmael].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Count increases by 1 whenever the affected unit tosses an attack skill Coin.\nAt the end of the turn, inflict Bind by the effect’s Count, then remove the effect.
   PL: W tej turze wartość rośnie przy każdym rzucie monetą Umiejętności ataku.\nNa koniec tury nadaje tyle Spętań, ile wynosi wartość, po czym efekt znika
340. [Słowo kluczowe [Muckworm] — nazwa] 구더기
   źródło: BattleKeywords.json :: dataList[id=Muckworm].name
   kontekst: identyfikator tagu w tekstach: `[Muckworm]`
   limit: do 40 znaków
   EN: Maggots
   PL: Czerwie
341. [Słowo kluczowe [Muckworm] — opis] 턴 종료 시 수치만큼 탐식 피해를 받고, 출혈 횟수가 1 증가한 뒤 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=Muckworm].desc
   limit: do 120 znaków
   EN: Turn End: Take Gluttony damage by the Count, then lower it by 1; Bleed Count +1.
   PL: Na koniec tury otrzymuje tyle obrażeń Obżarstwem, ile wynosi Licznik; Licznik Krwawienia +1, a wartość maleje o 1
342. [Słowo kluczowe [AttackUp] — nazwa] 공격 레벨 증가
   źródło: BattleKeywords.json :: dataList[id=AttackUp].name
   kontekst: identyfikator tagu w tekstach: `[AttackUp]`
   limit: do 40 znaków
   EN: Offense Level Up
   PL: Wzrost Poziomu Ataku
343. [Słowo kluczowe [AttackUp] — opis] 한 턴 동안 공격 레벨이 수치에 비례하여 증가
   źródło: BattleKeywords.json :: dataList[id=AttackUp].desc
   limit: do 120 znaków
   EN: Offense level increases based on the effect's Potency for one turn.
   PL: W tej turze Poziom Ataku rośnie proporcjonalnie do Mocy efektu
344. [Słowo kluczowe [AttackDown] — nazwa] 공격 레벨 감소
   źródło: BattleKeywords.json :: dataList[id=AttackDown].name
   kontekst: identyfikator tagu w tekstach: `[AttackDown]`
   limit: do 40 znaków
   EN: Offense Level Down
   PL: Spadek Poziomu Ataku
345. [Słowo kluczowe [AttackDown] — opis] 한 턴 동안 공격 레벨이 수치에 비례하여 감소
   źródło: BattleKeywords.json :: dataList[id=AttackDown].desc
   limit: do 120 znaków
   EN: Offense level decreases based on the effect's Potency for one turn.
   PL: W tej turze Poziom Ataku maleje proporcjonalnie do Mocy efektu
346. [Słowo kluczowe [Liu_Meursault_Guard_Buff] — nazwa] 태산
   źródło: BattleKeywords.json :: dataList[id=Liu_Meursault_Guard_Buff].name
   kontekst: identyfikator tagu w tekstach: `[Liu_Meursault_Guard_Buff]`
   limit: do 40 znaków
   EN: Great Mountain
   PL: Wielka Góra
347. [Słowo kluczowe [Liu_Meursault_Guard_Buff] — opis] 피격 시 대상에게 화상 횟수 1 증가
   źródło: BattleKeywords.json :: dataList[id=Liu_Meursault_Guard_Buff].desc
   limit: do 120 znaków
   EN: When attacked, inflict +1 Burn Count on the attacker.
   PL: Przy otrzymaniu ataku nadaje atakującemu +1 Licznika Podpalenia
348. [Słowo kluczowe [SlashResistUp] — nazwa] 참격 내성 강화
   źródło: BattleKeywords.json :: dataList[id=SlashResistUp].name
   kontekst: identyfikator tagu w tekstach: `[SlashResistUp]`
   limit: do 40 znaków
   EN: Slash Resist Up
   PL: Wzmocnienie Odporności na Cięcie
349. [Słowo kluczowe [SlashResistUp] — opis] 대상의 참격 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=SlashResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Slash Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Cięcie o (stosy x 0,1)
350. [Słowo kluczowe [PenetrateResistUp] — nazwa] 관통 내성 강화
   źródło: BattleKeywords.json :: dataList[id=PenetrateResistUp].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateResistUp]`
   limit: do 40 znaków
   EN: Pierce Resist Up
   PL: Wzmocnienie Odporności na Przebicie
351. [Słowo kluczowe [PenetrateResistUp] — opis] 대상의 관통 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=PenetrateResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Pierce Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Przebicie o (stosy x 0,1)
352. [Słowo kluczowe [HitResistUp] — nazwa] 타격 내성 강화
   źródło: BattleKeywords.json :: dataList[id=HitResistUp].name
   kontekst: identyfikator tagu w tekstach: `[HitResistUp]`
   limit: do 40 znaków
   EN: Blunt Resist Up
   PL: Wzmocnienie Odporności na Uderzenie
353. [Słowo kluczowe [HitResistUp] — opis] 대상의 타격 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=HitResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Blunt Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Uderzenie o (stosy x 0,1)
354. [Słowo kluczowe [SlashDamageUp] — nazwa] 참격 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=SlashDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[SlashDamageUp]`
   limit: do 40 znaków
   EN: Slash DMG Up
   PL: Wzrost Obrażeń Cięcia
355. [Słowo kluczowe [SlashDamageUp] — opis] 한 턴 동안 참격 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=SlashDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Slash skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Cięcia rosną proporcjonalnie do wartości efektu (maks. 10)
356. [Słowo kluczowe [PenetrateDamageUp] — nazwa] 관통 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=PenetrateDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateDamageUp]`
   limit: do 40 znaków
   EN: Pierce DMG Up
   PL: Wzrost Obrażeń Przebicia
357. [Słowo kluczowe [PenetrateDamageUp] — opis] 한 턴 동안 관통 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=PenetrateDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Pierce skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Przebicia rosną proporcjonalnie do wartości efektu (maks. 10)
358. [Słowo kluczowe [HitDamageUp] — nazwa] 타격 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=HitDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[HitDamageUp]`
   limit: do 40 znaków
   EN: Blunt DMG Up
   PL: Wzrost Obrażeń Uderzenia
359. [Słowo kluczowe [HitDamageUp] — opis] 한 턴 동안 타격 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=HitDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Blunt skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Uderzenia rosną proporcjonalnie do wartości efektu (maks. 10)
360. [Słowo kluczowe [SlashResistDown] — nazwa] 참격 내성 약화
   źródło: BattleKeywords.json :: dataList[id=SlashResistDown].name
   kontekst: identyfikator tagu w tekstach: `[SlashResistDown]`
   limit: do 40 znaków
   EN: Slash Resist Down
   PL: Osłabienie Odporności na Cięcie
361. [Słowo kluczowe [SlashResistDown] — opis] 대상의 참격 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=SlashResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Slash Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Cięcie o (stosy x 0,1)
362. [Słowo kluczowe [PenetrateResistDown] — nazwa] 관통 내성 약화
   źródło: BattleKeywords.json :: dataList[id=PenetrateResistDown].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateResistDown]`
   limit: do 40 znaków
   EN: Pierce Resist Down
   PL: Osłabienie Odporności na Przebicie
363. [Słowo kluczowe [PenetrateResistDown] — opis] 대상의 관통 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=PenetrateResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Pierce Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Przebicie o (stosy x 0,1)
364. [Słowo kluczowe [HitResistDown] — nazwa] 타격 내성 약화
   źródło: BattleKeywords.json :: dataList[id=HitResistDown].name
   kontekst: identyfikator tagu w tekstach: `[HitResistDown]`
   limit: do 40 znaków
   EN: Blunt Resist Down
   PL: Osłabienie Odporności na Uderzenie
365. [Słowo kluczowe [HitResistDown] — opis] 대상의 타격 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=HitResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Blunt Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Uderzenie o (stosy x 0,1)
366. [Słowo kluczowe [SlashDamageDown] — nazwa] 참격 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=SlashDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[SlashDamageDown]`
   limit: do 40 znaków
   EN: Slash DMG Down
   PL: Spadek Obrażeń Cięcia
367. [Słowo kluczowe [SlashDamageDown] — opis] 한 턴 동안 참격 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=SlashDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Slash skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Cięcia maleją proporcjonalnie do wartości efektu (maks. 10)
368. [Słowo kluczowe [PenetrateDamageDown] — nazwa] 관통 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=PenetrateDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateDamageDown]`
   limit: do 40 znaków
   EN: Pierce DMG Down
   PL: Spadek Obrażeń Przebicia
369. [Słowo kluczowe [PenetrateDamageDown] — opis] 한 턴 동안 관통 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=PenetrateDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Pierce skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Przebicia maleją proporcjonalnie do wartości efektu (maks. 10)
370. [Słowo kluczowe [HitDamageDown] — nazwa] 타격 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=HitDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[HitDamageDown]`
   limit: do 40 znaków
   EN: Blunt DMG Down
   PL: Spadek Obrażeń Uderzenia
371. [Słowo kluczowe [HitDamageDown] — opis] 한 턴 동안 타격 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=HitDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Blunt skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Uderzenia maleją proporcjonalnie do wartości efektu (maks. 10)
372. [Słowo kluczowe [CrimsonResistDown] — nazwa] 분노 내성 약화
   źródło: BattleKeywords.json :: dataList[id=CrimsonResistDown].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonResistDown]`
   limit: do 40 znaków
   EN: Wrath Resist Down
   PL: Osłabienie Odporności na Gniew
373. [Słowo kluczowe [CrimsonResistDown] — opis] 대상의 분노 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=CrimsonResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Wrath Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Gniew o (stosy x 0,1)
374. [Słowo kluczowe [ScarletResistDown] — nazwa] 색욕 내성 약화
   źródło: BattleKeywords.json :: dataList[id=ScarletResistDown].name
   kontekst: identyfikator tagu w tekstach: `[ScarletResistDown]`
   limit: do 40 znaków
   EN: Lust Resist Down
   PL: Osłabienie Odporności na Żądzę
375. [Słowo kluczowe [ScarletResistDown] — opis] 대상의 색욕 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=ScarletResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Lust Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Żądzę o (stosy x 0,1)
376. [Słowo kluczowe [AmberResistDown] — nazwa] 나태 내성 약화
   źródło: BattleKeywords.json :: dataList[id=AmberResistDown].name
   kontekst: identyfikator tagu w tekstach: `[AmberResistDown]`
   limit: do 40 znaków
   EN: Sloth Resist Down
   PL: Osłabienie Odporności na Lenistwo
377. [Słowo kluczowe [AmberResistDown] — opis] 대상의 나태 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=AmberResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Sloth Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Lenistwo o (stosy x 0,1)
378. [Słowo kluczowe [ShamrockResistDown] — nazwa] 탐식 내성 약화
   źródło: BattleKeywords.json :: dataList[id=ShamrockResistDown].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockResistDown]`
   limit: do 40 znaków
   EN: Gluttony Resist Down
   PL: Osłabienie Odporności na Obżarstwo
379. [Słowo kluczowe [ShamrockResistDown] — opis] 대상의 탐식 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=ShamrockResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Gluttony Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Obżarstwo o (stosy x 0,1)
380. [Słowo kluczowe [AzureResistDown] — nazwa] 우울 내성 약화
   źródło: BattleKeywords.json :: dataList[id=AzureResistDown].name
   kontekst: identyfikator tagu w tekstach: `[AzureResistDown]`
   limit: do 40 znaków
   EN: Gloom Resist Down
   PL: Osłabienie Odporności na Posępność
381. [Słowo kluczowe [AzureResistDown] — opis] 대상의 우울 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=AzureResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Gloom Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Posępność o (stosy x 0,1)
382. [Słowo kluczowe [IndigoResistDown] — nazwa] 오만 내성 약화
   źródło: BattleKeywords.json :: dataList[id=IndigoResistDown].name
   kontekst: identyfikator tagu w tekstach: `[IndigoResistDown]`
   limit: do 40 znaków
   EN: Pride Resist Down
   PL: Osłabienie Odporności na Pychę
383. [Słowo kluczowe [IndigoResistDown] — opis] 대상의 오만 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=IndigoResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Pride Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Pychę o (stosy x 0,1)
384. [Słowo kluczowe [VioletResistDown] — nazwa] 질투 내성 약화
   źródło: BattleKeywords.json :: dataList[id=VioletResistDown].name
   kontekst: identyfikator tagu w tekstach: `[VioletResistDown]`
   limit: do 40 znaków
   EN: Envy Resist Down
   PL: Osłabienie Odporności na Zazdrość
385. [Słowo kluczowe [VioletResistDown] — opis] 대상의 질투 내성을 (스택 * 0.1) 증가
   źródło: BattleKeywords.json :: dataList[id=VioletResistDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increase Envy Resistance based on Stack.\n(0.1 per Stack)
   PL: Zwiększa Odporność celu na Zazdrość o (stosy x 0,1)
386. [Słowo kluczowe [CrimsonResistUp] — nazwa] 분노 내성 강화
   źródło: BattleKeywords.json :: dataList[id=CrimsonResistUp].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonResistUp]`
   limit: do 40 znaków
   EN: Wrath Resist Up
   PL: Wzmocnienie Odporności na Gniew
387. [Słowo kluczowe [CrimsonResistUp] — opis] 대상의 분노 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=CrimsonResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduce Wrath Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Gniew o (stosy x 0,1)
388. [Słowo kluczowe [ScarletResistUp] — nazwa] 색욕 내성 강화
   źródło: BattleKeywords.json :: dataList[id=ScarletResistUp].name
   kontekst: identyfikator tagu w tekstach: `[ScarletResistUp]`
   limit: do 40 znaków
   EN: Lust Resist Up
   PL: Wzmocnienie Odporności na Żądzę
389. [Słowo kluczowe [ScarletResistUp] — opis] 대상의 색욕 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=ScarletResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduce Lust Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Żądzę o (stosy x 0,1)
390. [Słowo kluczowe [AmberResistUp] — nazwa] 나태 내성 강화
   źródło: BattleKeywords.json :: dataList[id=AmberResistUp].name
   kontekst: identyfikator tagu w tekstach: `[AmberResistUp]`
   limit: do 40 znaków
   EN: Sloth Resist Up
   PL: Wzmocnienie Odporności na Lenistwo
391. [Słowo kluczowe [AmberResistUp] — opis] 대상의 나태 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=AmberResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Sloth Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Lenistwo o (stosy x 0,1)
392. [Słowo kluczowe [ShamrockResistUp] — nazwa] 탐식 내성 강화
   źródło: BattleKeywords.json :: dataList[id=ShamrockResistUp].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockResistUp]`
   limit: do 40 znaków
   EN: Gluttony Resist Up
   PL: Wzmocnienie Odporności na Obżarstwo
393. [Słowo kluczowe [ShamrockResistUp] — opis] 대상의 탐식 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=ShamrockResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Gluttony Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Obżarstwo o (stosy x 0,1)
394. [Słowo kluczowe [AzureResistUp] — nazwa] 우울 내성 강화
   źródło: BattleKeywords.json :: dataList[id=AzureResistUp].name
   kontekst: identyfikator tagu w tekstach: `[AzureResistUp]`
   limit: do 40 znaków
   EN: Gloom Resist Up
   PL: Wzmocnienie Odporności na Posępność
395. [Słowo kluczowe [AzureResistUp] — opis] 대상의 우울 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=AzureResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Gloom Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Posępność o (stosy x 0,1)
396. [Słowo kluczowe [IndigoResistUp] — nazwa] 오만 내성 강화
   źródło: BattleKeywords.json :: dataList[id=IndigoResistUp].name
   kontekst: identyfikator tagu w tekstach: `[IndigoResistUp]`
   limit: do 40 znaków
   EN: Pride Resist Up
   PL: Wzmocnienie Odporności na Pychę
397. [Słowo kluczowe [IndigoResistUp] — opis] 대상의 오만 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=IndigoResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Pride Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Pychę o (stosy x 0,1)
398. [Słowo kluczowe [VioletResistUp] — nazwa] 질투 내성 강화
   źródło: BattleKeywords.json :: dataList[id=VioletResistUp].name
   kontekst: identyfikator tagu w tekstach: `[VioletResistUp]`
   limit: do 40 znaków
   EN: Envy Resist Up
   PL: Wzmocnienie Odporności na Zazdrość
399. [Słowo kluczowe [VioletResistUp] — opis] 대상의 질투 내성을 (스택 * 0.1) 감소
   źródło: BattleKeywords.json :: dataList[id=VioletResistUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decrease Envy Resistance based on Stack.\n(0.1 per Stack)
   PL: Zmniejsza Odporność celu na Zazdrość o (stosy x 0,1)
400. [Słowo kluczowe [CrimsonDamageDown] — nazwa] 분노 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=CrimsonDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonDamageDown]`
   limit: do 40 znaków
   EN: Wrath DMG Down
   PL: Spadek Obrażeń Gniewu
401. [Słowo kluczowe [CrimsonDamageDown] — opis] 한 턴 동안 분노 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=CrimsonDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Wrath skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Gniewu maleją proporcjonalnie do wartości efektu (maks. 10)
402. [Słowo kluczowe [ScarletDamageDown] — nazwa] 색욕 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=ScarletDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[ScarletDamageDown]`
   limit: do 40 znaków
   EN: Lust DMG Down
   PL: Spadek Obrażeń Żądzy
403. [Słowo kluczowe [ScarletDamageDown] — opis] 한 턴 동안 색욕 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ScarletDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Lust skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Żądzy maleją proporcjonalnie do wartości efektu (maks. 10)
404. [Słowo kluczowe [AmberDamageDown] — nazwa] 나태 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=AmberDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[AmberDamageDown]`
   limit: do 40 znaków
   EN: Sloth DMG Down
   PL: Spadek Obrażeń Lenistwa
405. [Słowo kluczowe [AmberDamageDown] — opis] 한 턴 동안 나태 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AmberDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Sloth skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Lenistwa maleją proporcjonalnie do wartości efektu (maks. 10)
406. [Słowo kluczowe [ShamrockDamageDown] — nazwa] 탐식 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=ShamrockDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockDamageDown]`
   limit: do 40 znaków
   EN: Gluttony DMG Down
   PL: Spadek Obrażeń Obżarstwa
407. [Słowo kluczowe [ShamrockDamageDown] — opis] 한 턴 동안 탐식 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ShamrockDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Gluttony skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Obżarstwa maleją proporcjonalnie do wartości efektu (maks. 10)
408. [Słowo kluczowe [AzureDamageDown] — nazwa] 우울 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=AzureDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[AzureDamageDown]`
   limit: do 40 znaków
   EN: Gloom DMG Down
   PL: Spadek Obrażeń Posępności
409. [Słowo kluczowe [AzureDamageDown] — opis] 한 턴 동안 우울 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AzureDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Gloom skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Posępności maleją proporcjonalnie do wartości efektu (maks. 10)
410. [Słowo kluczowe [IndigoDamageDown] — nazwa] 오만 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=IndigoDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[IndigoDamageDown]`
   limit: do 40 znaków
   EN: Pride DMG Down
   PL: Spadek Obrażeń Pychy
411. [Słowo kluczowe [IndigoDamageDown] — opis] 한 턴 동안 오만 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=IndigoDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Pride skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Pychy maleją proporcjonalnie do wartości efektu (maks. 10)
412. [Słowo kluczowe [VioletDamageDown] — nazwa] 질투 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=VioletDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[VioletDamageDown]`
   limit: do 40 znaków
   EN: Envy DMG Down
   PL: Spadek Obrażeń Zazdrości
413. [Słowo kluczowe [VioletDamageDown] — opis] 한 턴 동안 질투 속성 스킬로 가하는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=VioletDamageDown].desc
   limit: do 120 znaków
   EN: Deal less damage with Envy skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Zazdrości maleją proporcjonalnie do wartości efektu (maks. 10)
414. [Słowo kluczowe [CrimsonDamageUp] — nazwa] 분노 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=CrimsonDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonDamageUp]`
   limit: do 40 znaków
   EN: Wrath DMG Up
   PL: Wzrost Obrażeń Gniewu
415. [Słowo kluczowe [CrimsonDamageUp] — opis] 한 턴 동안 분노 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=CrimsonDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Wrath skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Gniewu rosną proporcjonalnie do wartości efektu (maks. 10)
416. [Słowo kluczowe [ScarletDamageUp] — nazwa] 색욕 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=ScarletDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[ScarletDamageUp]`
   limit: do 40 znaków
   EN: Lust DMG Up
   PL: Wzrost Obrażeń Żądzy
417. [Słowo kluczowe [ScarletDamageUp] — opis] 한 턴 동안 색욕 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ScarletDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Lust skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Żądzy rosną proporcjonalnie do wartości efektu (maks. 10)
418. [Słowo kluczowe [AmberDamageUp] — nazwa] 나태 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=AmberDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[AmberDamageUp]`
   limit: do 40 znaków
   EN: Sloth DMG Up
   PL: Wzrost Obrażeń Lenistwa
419. [Słowo kluczowe [AmberDamageUp] — opis] 한 턴 동안 나태 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AmberDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Sloth skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Lenistwa rosną proporcjonalnie do wartości efektu (maks. 10)
420. [Słowo kluczowe [ShamrockDamageUp] — nazwa] 탐식 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=ShamrockDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockDamageUp]`
   limit: do 40 znaków
   EN: Gluttony DMG Up
   PL: Wzrost Obrażeń Obżarstwa
421. [Słowo kluczowe [ShamrockDamageUp] — opis] 한 턴 동안 탐식 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ShamrockDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Gluttony skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Obżarstwa rosną proporcjonalnie do wartości efektu (maks. 10)
422. [Słowo kluczowe [AzureDamageUp] — nazwa] 우울 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=AzureDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[AzureDamageUp]`
   limit: do 40 znaków
   EN: Gloom DMG Up
   PL: Wzrost Obrażeń Posępności
423. [Słowo kluczowe [AzureDamageUp] — opis] 한 턴 동안 우울 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AzureDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Gloom skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Posępności rosną proporcjonalnie do wartości efektu (maks. 10)
424. [Słowo kluczowe [IndigoDamageUp] — nazwa] 오만 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=IndigoDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[IndigoDamageUp]`
   limit: do 40 znaków
   EN: Pride DMG Up
   PL: Wzrost Obrażeń Pychy
425. [Słowo kluczowe [IndigoDamageUp] — opis] 한 턴 동안 오만 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=IndigoDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Pride skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Pychy rosną proporcjonalnie do wartości efektu (maks. 10)
426. [Słowo kluczowe [VioletDamageUp] — nazwa] 질투 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=VioletDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[VioletDamageUp]`
   limit: do 40 znaków
   EN: Envy DMG Up
   PL: Wzrost Obrażeń Zazdrości
427. [Słowo kluczowe [VioletDamageUp] — opis] 한 턴 동안 질투 속성 스킬로 가하는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=VioletDamageUp].desc
   limit: do 120 znaków
   EN: Deal more damage with Envy skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze zadawane obrażenia Umiejętnościami Zazdrości rosną proporcjonalnie do wartości efektu (maks. 10)
428. [Słowo kluczowe [Curse] — nazwa] 저주
   źródło: BattleKeywords.json :: dataList[id=Curse].name
   kontekst: identyfikator tagu w tekstach: `[Curse]`
   limit: do 40 znaków
   EN: Curse
   PL: Klątwa
429. [Słowo kluczowe [Curse] — opis] 턴 종료 시 다음 턴에 공격 위력 감소 1, 수비 위력 감소 1, 공격 레벨 감소 2, 방어 레벨 감소 2 중 무작위 1개의 효과를 얻고, 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=Curse].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Next turn, randomly gain one of the following, then reduce this effect’s Count by 1.\n1 Attack Power Down/1 Defense Power Down/2 Offense Level Down/2 Defense Level Down.
   PL: Na koniec tury zyskuje na następną turę 1 losowy efekt spośród: 1 Spadek Mocy Ataku, 1 Spadek Mocy Obrony, 2 Spadki Poziomu Ataku, 2 Spadki Poziomu Obrony, po czym Licznik maleje o 1
430. [Słowo kluczowe [AttackDmgUp_Weak] — nazwa] 약점 공격 시 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=AttackDmgUp_Weak].name
   kontekst: identyfikator tagu w tekstach: `[AttackDmgUp_Weak]`
   limit: do 40 znaków
   EN: Weak-resist DMG Boost
   PL: Wzrost Obrażeń przy Słabocie
431. [Słowo kluczowe [AttackDmgUp_Weak] — opis] 약점 공격 시 피해 (스택)% 증가
   źródło: BattleKeywords.json :: dataList[id=AttackDmgUp_Weak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Boost the damage of attacks against Weak resistances by a % based on Count.\n(10% per Count)
   PL: Zwiększa obrażenia ataków na słabe Odporności o procent równy Licznikowi.\n(10% za Licznik)
432. [Słowo kluczowe [Bullet] — nazwa] 탄환
   źródło: BattleKeywords.json :: dataList[id=Bullet].name
   kontekst: identyfikator tagu w tekstach: `[Bullet]`
   limit: do 40 znaków
   EN: Ammo
   PL: Amunicja
433. [Słowo kluczowe [Bullet] — opis] 특정 스킬 사용 시 탄환이 소모됨\n탄환이 없을 때 공격이 취소됨
   źródło: BattleKeywords.json :: dataList[id=Bullet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Spent by certain skills.\nSome attacks cancel if lacking Ammo.
   PL: Zużywana przez określone Umiejętności\nAtak zostaje anulowany przy braku Amunicji
434. [Słowo kluczowe [Meursault_Last_Remodeling] — nazwa] 마지막 개조
   źródło: BattleKeywords.json :: dataList[id=Meursault_Last_Remodeling].name
   kontekst: identyfikator tagu w tekstach: `[Meursault_Last_Remodeling]`
   limit: do 40 znaków
   EN: Final Augment
   PL: Ostateczna Przeróbka
435. [Słowo kluczowe [Meursault_Last_Remodeling] — opis] 매 턴마다 공격 위력 증가, 수비 위력 증가, 신속 3을 얻고, 3턴 뒤 사망함
   źródło: BattleKeywords.json :: dataList[id=Meursault_Last_Remodeling].desc
   limit: do 130 znaków
   EN: At the start of the turn, gain 3 Attack Power Up, Defense Power Up, and Haste; die after 3 turns.
   PL: Na początku każdej tury zyskuje 3 Wzrosty Mocy Ataku, 3 Wzrosty Mocy Obrony i 3 Pośpiechu; umiera po 3 turach
436. [Słowo kluczowe [Choice_90103301] — nazwa] 바둥거림
   źródło: BattleKeywords.json :: dataList[id=Choice_90103301].name
   kontekst: identyfikator tagu w tekstach: `[Choice_90103301]`
   limit: do 40 znaków
   EN: Struggle
   PL: Wiercenie się
437. [Słowo kluczowe [Choice_90103301] — opis] 이번 전투 동안 속도 +1
   źródło: BattleKeywords.json :: dataList[id=Choice_90103301].desc
   limit: do 120 znaków
   EN: Speed +1 for this battle.
   PL: W tej walce Szybkość +1
438. [Słowo kluczowe [Choice_90103301] — podsumowanie] 속도 +1
   źródło: BattleKeywords.json :: dataList[id=Choice_90103301].summary
   limit: do 120 znaków
   EN: SPD +1
   PL: Szybkość +1
439. [Słowo kluczowe [Choice_90103402] — nazwa] 후련함
   źródło: BattleKeywords.json :: dataList[id=Choice_90103402].name
   kontekst: identyfikator tagu w tekstach: `[Choice_90103402]`
   limit: do 40 znaków
   EN: Relief
   PL: Ukojenie
440. [Słowo kluczowe [Choice_90103402] — opis] 이번 전투 동안 속도 +2
   źródło: BattleKeywords.json :: dataList[id=Choice_90103402].desc
   limit: do 120 znaków
   EN: Speed +2 for this battle.
   PL: W tej walce Szybkość +2
441. [Słowo kluczowe [Choice_90103402] — podsumowanie] 속도 +2
   źródło: BattleKeywords.json :: dataList[id=Choice_90103402].summary
   limit: do 120 znaków
   EN: SPD +2
   PL: Szybkość +2
442. [Słowo kluczowe [Choice_901001] — nazwa] 불번짐
   źródło: BattleKeywords.json :: dataList[id=Choice_901001].name
   kontekst: identyfikator tagu w tekstach: `[Choice_901001]`
   limit: do 40 znaków
   EN: Spreading Flame
   PL: Niegasnący Płomień
443. [Słowo kluczowe [Choice_901001] — opis] 전투 시작 시 분노 속성 공격 스킬을 보유하지 않은 인격이 분노 피해 5를 입음
   źródło: BattleKeywords.json :: dataList[id=Choice_901001].desc
   limit: do 120 znaków
   EN: Combat Start: Allies without Wrath Affinity Attack Skill take 5 Wrath damage
   PL: Na początku walki osobowości bez podstawowego ataku atrybutu Gniewu otrzymują 5 obrażeń Gniewem
444. [Słowo kluczowe [Choice_901007] — nazwa] 나긋한 배웅
   źródło: BattleKeywords.json :: dataList[id=Choice_901007].name
   kontekst: identyfikator tagu w tekstach: `[Choice_901007]`
   limit: do 40 znaków
   EN: Gentle Sendoff
   PL: Łagodne Pożegnanie
445. [Słowo kluczowe [Choice_901007] — opis] 턴 시작 시 10만큼 체력과 정신력 회복 (최대 3턴)
   źródło: BattleKeywords.json :: dataList[id=Choice_901007].desc
   limit: do 120 znaków
   EN: Turn Start: Heal 10 HP and SP. (Up to 3 turns)
   PL: Na początku tury leczy 10 HP i 10 Poczytalności (do 3 tur)
446. [Słowo kluczowe [Choice_901007] — podsumowanie] 체력, 정신력 +10
   źródło: BattleKeywords.json :: dataList[id=Choice_901007].summary
   limit: do 120 znaków
   EN: HP & SP +10
   PL: HP i Poczytalność +10
447. [Słowo kluczowe [Choice_901009] — nazwa] 명순응
   źródło: BattleKeywords.json :: dataList[id=Choice_901009].name
   kontekst: identyfikator tagu w tekstach: `[Choice_901009]`
   limit: do 40 znaków
   EN: Photopia
   PL: Fotopia
448. [Słowo kluczowe [Choice_901009] — opis] 전투 시작 시 스킬 최종 위력 -1
   źródło: BattleKeywords.json :: dataList[id=Choice_901009].desc
   limit: do 120 znaków
   EN: Combat Start: Skill Final Power -1.
   PL: Na początku walki Moc Końcowa Umiejętności -1
449. [Słowo kluczowe [Choice_901009] — podsumowanie] 스킬 최종 위력 -1
   źródło: BattleKeywords.json :: dataList[id=Choice_901009].summary
   limit: do 120 znaków
   EN: Skill Final Power -1
   PL: Moc Końcowa Umiejętności -1
450. [Słowo kluczowe [Choice_901010] — nazwa] 비워짐
   źródło: BattleKeywords.json :: dataList[id=Choice_901010].name
   kontekst: identyfikator tagu w tekstach: `[Choice_901010]`
   limit: do 40 znaków
   EN: Emptied
   PL: Opróżnienie
451. [Słowo kluczowe [Choice_901010] — opis] 전투 시작 시 색욕 속성 공격 스킬을 보유하지 않은 인격이 흐트러짐 상태로 시작함
   źródło: BattleKeywords.json :: dataList[id=Choice_901010].desc
   limit: do 120 znaków
   EN: Combat Start: Allies without Lust Affinity Attack Skill are Staggered.
   PL: Na początku walki osobowości bez podstawowego ataku atrybutu Żądzy rozpoczynają walkę oszołomione
452. [Słowo kluczowe [Choice_901019] — nazwa] 오물
   źródło: BattleKeywords.json :: dataList[id=Choice_901019].name
   kontekst: identyfikator tagu w tekstach: `[Choice_901019]`
   limit: do 40 znaków
   EN: Contamination
   PL: Zanieczyszczenie
453. [Słowo kluczowe [Choice_901019] — opis] 전투 시작 시 속도 -2
   źródło: BattleKeywords.json :: dataList[id=Choice_901019].desc
   limit: do 120 znaków
   EN: Combat Start: Speed -2.
   PL: Na początku walki Szybkość -2
454. [Słowo kluczowe [Choice_901019] — podsumowanie] 속도 -2
   źródło: BattleKeywords.json :: dataList[id=Choice_901019].summary
   limit: do 120 znaków
   EN: SPD -2
   PL: Szybkość -2
455. [Słowo kluczowe [Aggressive] — nazwa] 본능
   źródło: BattleKeywords.json :: dataList[id=Aggressive].name
   kontekst: identyfikator tagu w tekstach: `[Aggressive]`
   limit: do 40 znaków
   EN: Instincts
   PL: Instynkt
456. [Słowo kluczowe [Aggressive] — opis] 턴 종료 시 수치가 4 이상이면 상태가 공격적으로 변경됨.
   źródło: BattleKeywords.json :: dataList[id=Aggressive].desc
   limit: do 120 znaków
   EN: Turn End: At 4+ Stack, change to an “aggressive” state.
   PL: Na koniec tury, przy 4 lub więcej stosach, przechodzi w stan agresywny.
457. [Słowo kluczowe [Cromer_Target] — nazwa] 쥐는 자의 주시
   źródło: BattleKeywords.json :: dataList[id=Cromer_Target].name
   kontekst: identyfikator tagu w tekstach: `[Cromer_Target]`
   limit: do 40 znaków
   EN: Gaze of the One Who Grips
   PL: Spojrzenie Tej, Która Ściska
458. [Słowo kluczowe [Cromer_Target] — opis] 한 턴 동안 흐트러짐 상태가 되고, 크로머에게 받는 피해량 +100%
   źródło: BattleKeywords.json :: dataList[id=Cromer_Target].desc
   limit: do 120 znaków
   EN: Staggered for one turn. Take +100% damage from Kromer.
   PL: Oszołomienie na jedną turę; otrzymuje +100% obrażeń od Kromer
459. [Słowo kluczowe [Poison] — nazwa] 독
   źródło: BattleKeywords.json :: dataList[id=Poison].name
   kontekst: identyfikator tagu w tekstach: `[Poison]`
   limit: do 40 znaków
   EN: Poison
   PL: Trucizna
460. [Słowo kluczowe [Poison] — opis] 턴 종료 시 수치만큼 피해를 주고, 수치가 반으로 감소
   źródło: BattleKeywords.json :: dataList[id=Poison].desc
   limit: do 120 znaków
   EN: At the end of the turn, take fixed damage by the Count, then halve the Count.
   PL: Na koniec tury otrzymuje obrażenia równe Licznikowi, po czym Licznik maleje o połowę
461. [Słowo kluczowe [Desire] — nazwa] 욕망
   źródło: BattleKeywords.json :: dataList[id=Desire].name
   kontekst: identyfikator tagu w tekstach: `[Desire]`
   limit: do 40 znaków
   EN: Urge
   PL: Pożądanie
462. [Słowo kluczowe [Desire] — opis] 턴 종료 시 스택이 5 이상이면 정신 피해를 30 주고, 다음 턴에 취약 2, 속박 10을 부여한 뒤 소멸.
   źródło: BattleKeywords.json :: dataList[id=Desire].desc
   limit: do 150 znaków
   EN: At the end of the turn, if at 5+ stacks, take 30 SP damage, gain 2 Fragile and 10 Bind, and remove this effect.
   PL: Na koniec tury, przy 5 lub więcej stosach, otrzymuje 30 obrażeń Poczytalności, a w następnej turze 2 Wrażliwości i 10 Spętań, po czym efekt znika.
463. [Słowo kluczowe [Assemble] — nazwa] 광신
   źródło: BattleKeywords.json :: dataList[id=Assemble].name
   kontekst: identyfikator tagu w tekstach: `[Assemble]`
   limit: do 40 znaków
   EN: Fanatic
   PL: Fanatyzm
464. [Słowo kluczowe [Assemble] — opis] 이번 턴 동안 못이 부여된 대상 공격 시 최종 위력이 수치만큼 증가 (합 진행 시에도 적용됨)
   źródło: BattleKeywords.json :: dataList[id=Assemble].desc
   limit: do 160 znaków
   EN: Raise Skill Final Power by the effect’s Count against units that have Nails for the turn. (Applies to clashes as well)
   PL: W tej turze Moc Końcowa przy atakowaniu celów z Gwoździem rośnie o wartość efektu (działa także podczas Stareć)
465. [Słowo kluczowe [Nail] — nazwa] N사의 못
   źródło: BattleKeywords.json :: dataList[id=Nail].name
   kontekst: identyfikator tagu w tekstach: `[Nail]`
   limit: do 40 znaków
   EN: N Corp’s Nails
   PL: Gwóźdź Korporacji N
466. [Słowo kluczowe [Nail] — opis] 턴 시작 시 출혈 1을 주고, 출혈 횟수가 수치만큼 증가. 턴 종료 시 1 감소.
   źródło: BattleKeywords.json :: dataList[id=Nail].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, gain 1 Bleed and increase the Bleed Count by this effect’s Count.\nAt the end of the turn, reduce the Count by 1.
   PL: Na początku tury nadaje 1 Krwawienia i zwiększa Licznik Krwawienia o wartość efektu. Na koniec tury Licznik maleje o 1.
467. [Słowo kluczowe [BeingGolden] — nazwa] 황금빛
   źródło: BattleKeywords.json :: dataList[id=BeingGolden].name
   kontekst: identyfikator tagu w tekstach: `[BeingGolden]`
   limit: do 40 znaków
   EN: Golden Sheen
   PL: Złoty Blask
468. [Słowo kluczowe [BeingGolden] — opis] 턴 시작 시 수치당 10만큼 체력 회복
   źródło: BattleKeywords.json :: dataList[id=BeingGolden].desc
   limit: do 120 znaków
   EN: At the start of the turn, heal 10 HP per Count.
   PL: Na początku tury leczy 10 HP za każdą wartość
469. [Słowo kluczowe [SlashTakeDamageDown] — nazwa] 참격 보호
   źródło: BattleKeywords.json :: dataList[id=SlashTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[SlashTakeDamageDown]`
   limit: do 40 znaków
   EN: Slash Protection
   PL: Ochrona przed Cięciem
470. [Słowo kluczowe [SlashTakeDamageDown] — opis] 한 턴 동안 참격 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=SlashTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Slash skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Cięcia maleją proporcjonalnie do wartości efektu (maks. 10)
471. [Słowo kluczowe [PenetrateTakeDamageDown] — nazwa] 관통 보호
   źródło: BattleKeywords.json :: dataList[id=PenetrateTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateTakeDamageDown]`
   limit: do 40 znaków
   EN: Pierce Protection
   PL: Ochrona przed Przebiciem
472. [Słowo kluczowe [PenetrateTakeDamageDown] — opis] 한 턴 동안 관통 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=PenetrateTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Pierce skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Przebicia maleją proporcjonalnie do wartości efektu (maks. 10)
473. [Słowo kluczowe [HitTakeDamageDown] — nazwa] 타격 보호
   źródło: BattleKeywords.json :: dataList[id=HitTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[HitTakeDamageDown]`
   limit: do 40 znaków
   EN: Blunt Protection
   PL: Ochrona przed Uderzeniem
474. [Słowo kluczowe [HitTakeDamageDown] — opis] 한 턴 동안 타격 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=HitTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Blunt skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Uderzenia maleją proporcjonalnie do wartości efektu (maks. 10)
475. [Słowo kluczowe [CrimsonTakeDamageDown] — nazwa] 분노 보호
   źródło: BattleKeywords.json :: dataList[id=CrimsonTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonTakeDamageDown]`
   limit: do 40 znaków
   EN: Wrath Protection
   PL: Ochrona przed Gniewem
476. [Słowo kluczowe [CrimsonTakeDamageDown] — opis] 한 턴 동안 분노 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=CrimsonTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Wrath skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Gniewu maleją proporcjonalnie do wartości efektu (maks. 10)
477. [Słowo kluczowe [ScarletTakeDamageDown] — nazwa] 색욕 보호
   źródło: BattleKeywords.json :: dataList[id=ScarletTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[ScarletTakeDamageDown]`
   limit: do 40 znaków
   EN: Lust Protection
   PL: Ochrona przed Żądzą
478. [Słowo kluczowe [ScarletTakeDamageDown] — opis] 한 턴 동안 색욕 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ScarletTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Lust skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Żądzy maleją proporcjonalnie do wartości efektu (maks. 10)
479. [Słowo kluczowe [AmberTakeDamageDown] — nazwa] 나태 보호
   źródło: BattleKeywords.json :: dataList[id=AmberTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[AmberTakeDamageDown]`
   limit: do 40 znaków
   EN: Sloth Protection
   PL: Ochrona przed Lenistwem
480. [Słowo kluczowe [AmberTakeDamageDown] — opis] 한 턴 동안 나태 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AmberTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Sloth skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Lenistwa maleją proporcjonalnie do wartości efektu (maks. 10)
481. [Słowo kluczowe [ShamrockTakeDamageDown] — nazwa] 탐식 보호
   źródło: BattleKeywords.json :: dataList[id=ShamrockTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockTakeDamageDown]`
   limit: do 40 znaków
   EN: Gluttony Protection
   PL: Ochrona przed Obżarstwem
482. [Słowo kluczowe [ShamrockTakeDamageDown] — opis] 한 턴 동안 탐식 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ShamrockTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Gluttony skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Obżarstwa maleją proporcjonalnie do wartości efektu (maks. 10)
483. [Słowo kluczowe [AzureTakeDamageDown] — nazwa] 우울 보호
   źródło: BattleKeywords.json :: dataList[id=AzureTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[AzureTakeDamageDown]`
   limit: do 40 znaków
   EN: Gloom Protection
   PL: Ochrona przed Posępnością
484. [Słowo kluczowe [AzureTakeDamageDown] — opis] 한 턴 동안 우울 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AzureTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Gloom skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Posępności maleją proporcjonalnie do wartości efektu (maks. 10)
485. [Słowo kluczowe [IndigoTakeDamageDown] — nazwa] 오만 보호
   źródło: BattleKeywords.json :: dataList[id=IndigoTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[IndigoTakeDamageDown]`
   limit: do 40 znaków
   EN: Pride Protection
   PL: Ochrona przed Pychą
486. [Słowo kluczowe [IndigoTakeDamageDown] — opis] 한 턴 동안 오만 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=IndigoTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Pride skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Pychy maleją proporcjonalnie do wartości efektu (maks. 10)
487. [Słowo kluczowe [VioletTakeDamageDown] — nazwa] 질투 보호
   źródło: BattleKeywords.json :: dataList[id=VioletTakeDamageDown].name
   kontekst: identyfikator tagu w tekstach: `[VioletTakeDamageDown]`
   limit: do 40 znaków
   EN: Envy Protection
   PL: Ochrona przed Zazdrością
488. [Słowo kluczowe [VioletTakeDamageDown] — opis] 한 턴 동안 질투 속성 스킬로 받는 피해가 수치에 비례하여 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=VioletTakeDamageDown].desc
   limit: do 120 znaków
   EN: Take less damage from Envy skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Zazdrości maleją proporcjonalnie do wartości efektu (maks. 10)
489. [Słowo kluczowe [SlashTakeDamageUp] — nazwa] 참격 취약
   źródło: BattleKeywords.json :: dataList[id=SlashTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[SlashTakeDamageUp]`
   limit: do 40 znaków
   EN: Slash Fragility
   PL: Wrażliwość na Cięcie
490. [Słowo kluczowe [SlashTakeDamageUp] — opis] 한 턴 동안 참격 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=SlashTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Slash skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Cięcia rosną proporcjonalnie do wartości efektu (maks. 10)
491. [Słowo kluczowe [PenetrateTakeDamageUp] — nazwa] 관통 취약
   źródło: BattleKeywords.json :: dataList[id=PenetrateTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateTakeDamageUp]`
   limit: do 40 znaków
   EN: Pierce Fragility
   PL: Wrażliwość na Przebicie
492. [Słowo kluczowe [PenetrateTakeDamageUp] — opis] 한 턴 동안 관통 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=PenetrateTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Pierce skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Przebicia rosną proporcjonalnie do wartości efektu (maks. 10)
493. [Słowo kluczowe [HitTakeDamageUp] — nazwa] 타격 취약
   źródło: BattleKeywords.json :: dataList[id=HitTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[HitTakeDamageUp]`
   limit: do 40 znaków
   EN: Blunt Fragility
   PL: Wrażliwość na Uderzenie
494. [Słowo kluczowe [HitTakeDamageUp] — opis] 한 턴 동안 타격 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=HitTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Blunt skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Uderzenia rosną proporcjonalnie do wartości efektu (maks. 10)
495. [Słowo kluczowe [CrimsonTakeDamageUp] — nazwa] 분노 취약
   źródło: BattleKeywords.json :: dataList[id=CrimsonTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonTakeDamageUp]`
   limit: do 40 znaków
   EN: Wrath Fragility
   PL: Wrażliwość na Gniew
496. [Słowo kluczowe [CrimsonTakeDamageUp] — opis] 한 턴 동안 분노 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=CrimsonTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Wrath skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Gniewu rosną proporcjonalnie do wartości efektu (maks. 10)
497. [Słowo kluczowe [ScarletTakeDamageUp] — nazwa] 색욕 취약
   źródło: BattleKeywords.json :: dataList[id=ScarletTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[ScarletTakeDamageUp]`
   limit: do 40 znaków
   EN: Lust Fragility
   PL: Wrażliwość na Żądzę
498. [Słowo kluczowe [ScarletTakeDamageUp] — opis] 한 턴 동안 색욕 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ScarletTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Lust skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Żądzy rosną proporcjonalnie do wartości efektu (maks. 10)
499. [Słowo kluczowe [AmberTakeDamageUp] — nazwa] 나태 취약
   źródło: BattleKeywords.json :: dataList[id=AmberTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[AmberTakeDamageUp]`
   limit: do 40 znaków
   EN: Sloth Fragility
   PL: Wrażliwość na Lenistwo
500. [Słowo kluczowe [AmberTakeDamageUp] — opis] 한 턴 동안 나태 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AmberTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Sloth skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Lenistwa rosną proporcjonalnie do wartości efektu (maks. 10)
501. [Słowo kluczowe [ShamrockTakeDamageUp] — nazwa] 탐식 취약
   źródło: BattleKeywords.json :: dataList[id=ShamrockTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockTakeDamageUp]`
   limit: do 40 znaków
   EN: Gluttony Fragility
   PL: Wrażliwość na Obżarstwo
502. [Słowo kluczowe [ShamrockTakeDamageUp] — opis] 한 턴 동안 탐식 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ShamrockTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Gluttony skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Obżarstwa rosną proporcjonalnie do wartości efektu (maks. 10)
503. [Słowo kluczowe [AzureTakeDamageUp] — nazwa] 우울 취약
   źródło: BattleKeywords.json :: dataList[id=AzureTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[AzureTakeDamageUp]`
   limit: do 40 znaków
   EN: Gloom Fragility
   PL: Wrażliwość na Posępność
504. [Słowo kluczowe [AzureTakeDamageUp] — opis] 한 턴 동안 우울 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=AzureTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Gloom skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Posępności rosną proporcjonalnie do wartości efektu (maks. 10)
505. [Słowo kluczowe [IndigoTakeDamageUp] — nazwa] 오만 취약
   źródło: BattleKeywords.json :: dataList[id=IndigoTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[IndigoTakeDamageUp]`
   limit: do 40 znaków
   EN: Pride Fragility
   PL: Wrażliwość na Pychę
506. [Słowo kluczowe [IndigoTakeDamageUp] — opis] 한 턴 동안 오만 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=IndigoTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Pride skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Pychy rosną proporcjonalnie do wartości efektu (maks. 10)
507. [Słowo kluczowe [VioletTakeDamageUp] — nazwa] 질투 취약
   źródło: BattleKeywords.json :: dataList[id=VioletTakeDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[VioletTakeDamageUp]`
   limit: do 40 znaków
   EN: Envy Fragility
   PL: Wrażliwość na Zazdrość
508. [Słowo kluczowe [VioletTakeDamageUp] — opis] 한 턴 동안 질투 속성 스킬로 받는 피해가 수치에 비례하여 증가 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=VioletTakeDamageUp].desc
   limit: do 120 znaków
   EN: Take more damage from Envy skills based on the effect’s Count for one turn. (Max 10)
   PL: W tej turze otrzymywane obrażenia od Umiejętności Zazdrości rosną proporcjonalnie do wartości efektu (maks. 10)
509. [Słowo kluczowe [NailPersonality] — nazwa] 못
   źródło: BattleKeywords.json :: dataList[id=NailPersonality].name
   kontekst: identyfikator tagu w tekstach: `[NailPersonality]`
   limit: do 40 znaków
   EN: Nails
   PL: Gwóźdź
510. [Słowo kluczowe [NailPersonality] — opis] 특수 출혈\n턴 시작 시 출혈 1을 주고, 출혈 횟수가 수치만큼 증가. 턴 종료 시 수치가 절반 감소 (소수점 버림)
   źródło: BattleKeywords.json :: dataList[id=NailPersonality].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unique Bleed\nTurn Start: Gain 1 Bleed and increase the Bleed Count by this effect’s Count.\nTurn End: Halve the Count. (Rounded down)
   PL: Szczególne Krwawienie\nNa początku tury nadaje 1 Krwawienia i zwiększa Licznik Krwawienia o wartość efektu. Na koniec tury Licznik maleje o połowę (zaokrąglona w dół)
511. [Słowo kluczowe [AssemblePersonality] — nazwa] 광신
   źródło: BattleKeywords.json :: dataList[id=AssemblePersonality].name
   kontekst: identyfikator tagu w tekstach: `[AssemblePersonality]`
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Słowo kluczowe [AssemblePersonality] — opis] 이번 턴 동안 못이 부여된 대상 공격 시 최종 위력이 수치만큼 증가 (합 진행 시에도 적용됨)
   źródło: BattleKeywords.json :: dataList[id=AssemblePersonality].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Słowo kluczowe [MarkOfHeresy] — nazwa] 주시
   źródło: BattleKeywords.json :: dataList[id=MarkOfHeresy].name
   kontekst: identyfikator tagu w tekstach: `[MarkOfHeresy]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
514. [Słowo kluczowe [MarkOfHeresy] — opis] 한 턴동안 관통, 타격 속성 스킬로 받는 피해 20% 증가. 표적이 찍힌 적 처치 시 처치한 아군의 정신력이 10 회복되며, 해당 아군이 N사 광신도면 다음 턴에 광신 1을 얻음
   źródło: BattleKeywords.json :: dataList[id=MarkOfHeresy].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +20% damage from Pierce and Blunt skills for one turn.\nThe ally that defeats the marked unit heals 10 SP; if the ally is an 'N Corp. Fanatic', also apply 1 Fanatic next turn.
   PL: W tej turze otrzymuje +20% obrażeń od Umiejętności Przebicia i Uderzenia. Sojusznik, który zabije oznaczonego wroga, leczy 10 Poczytalności; jeśli to fanatyk Korporacji N, w następnej turze zyskuje 1 Fanatyzmu
515. [Słowo kluczowe [HitResultUp] — nazwa] 타격 위력 증가
   źródło: BattleKeywords.json :: dataList[id=HitResultUp].name
   kontekst: identyfikator tagu w tekstach: `[HitResultUp]`
   limit: do 40 znaków
   EN: Blunt Power Up
   PL: Wzrost Mocy Uderzenia
516. [Słowo kluczowe [HitResultUp] — opis] 한 턴 동안 타격 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=HitResultUp].desc
   limit: do 120 znaków
   EN: Blunt skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Uderzenia rośnie o wartość efektu
517. [Słowo kluczowe [WeaknessAnalysis] — nazwa] 약점 분석
   źródło: BattleKeywords.json :: dataList[id=WeaknessAnalysis].name
   kontekst: identyfikator tagu w tekstach: `[WeaknessAnalysis]`
   limit: do 40 znaków
   EN: Weakness Analyzed
   PL: Przeanalizowana Słabość
518. [Słowo kluczowe [WeaknessAnalysis] — opis] 한 턴 동안 공격 유형 내성에서 '견딤', '보통' 내성 중 무작위 하나를 선택하여 약화[+0.2]시킴
   źródło: BattleKeywords.json :: dataList[id=WeaknessAnalysis].desc
   limit: do 140 znaków
   EN: A random “Endure” or “Normal” attack type resistance is weakened [+0.2 to damage multiplier] for one turn.
   PL: W tej turze jedna z Odporności na typy ataków o wartości „Znośna” lub „Zwykła” zostaje losowo osłabiona [+0,2 do mnożnika obrażeń]
519. [Słowo kluczowe [Cycle] — nazwa] 업보
   źródło: BattleKeywords.json :: dataList[id=Cycle].name
   kontekst: identyfikator tagu w tekstach: `[Cycle]`
   limit: do 40 znaków
   EN: Karma
   PL: Karma
520. [Słowo kluczowe [Cycle] — opis] 수치당 받는 피해량이 1% 증가한다. 턴 종료 시 수치가 108이 되면 사망한다.
   źródło: BattleKeywords.json :: dataList[id=Cycle].desc
   limit: do 120 znaków
   EN: Take +1% damage per Count. At the end of the turn, if at 108+ Count, the unit dies.
   PL: Otrzymuje +1% obrażeń za każdą wartość. Na koniec tury, przy 108 lub więcej, umiera
521. [Słowo kluczowe [Duress] — nazwa] 구속
   źródło: BattleKeywords.json :: dataList[id=Duress].name
   kontekst: identyfikator tagu w tekstach: `[Duress]`
   limit: do 40 znaków
   EN: Captivity
   PL: Niewola
522. [Słowo kluczowe [Duress] — opis] 3턴간 흐트러짐 상태가 되고 퇴각 관련 기능이 작동하지 않음\nkqe-1j-23이 흐트러짐 상태인 경우 해제됨
   źródło: BattleKeywords.json :: dataList[id=Duress].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Become Staggered for 3 turns; disable any Retreat-related abilities\nRemove this effect when kqe-1j-23 becomes Staggered
   PL: Pozostaje oszołomiona przez 3 tury; zdolności odwrotu są wyłączone\nEfekt znika, gdy kqe-1j-23 zostanie oszołomione
523. [Słowo kluczowe [ShamrockResultUp] — nazwa] 탐식 위력 증가
   źródło: BattleKeywords.json :: dataList[id=ShamrockResultUp].name
   kontekst: identyfikator tagu w tekstach: `[ShamrockResultUp]`
   limit: do 40 znaków
   EN: Gluttony Power Up
   PL: Wzrost Mocy Obżarstwa
524. [Słowo kluczowe [ShamrockResultUp] — opis] 한 턴 동안 탐식 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=ShamrockResultUp].desc
   limit: do 120 znaków
   EN: Gluttony Skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Obżarstwa rośnie o wartość efektu
525. [Słowo kluczowe [VioletResultUp] — nazwa] 질투 위력 증가
   źródło: BattleKeywords.json :: dataList[id=VioletResultUp].name
   kontekst: identyfikator tagu w tekstach: `[VioletResultUp]`
   limit: do 40 znaków
   EN: Envy Power Up
   PL: Wzrost Mocy Zazdrości
526. [Słowo kluczowe [VioletResultUp] — opis] 한 턴 동안 질투 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=VioletResultUp].desc
   limit: do 120 znaków
   EN: Envy skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Zazdrości rośnie o wartość efektu
527. [Słowo kluczowe [CyclingKarma] — nazwa] 순환하는 업보
   źródło: BattleKeywords.json :: dataList[id=CyclingKarma].name
   kontekst: identyfikator tagu w tekstach: `[CyclingKarma]`
   limit: do 40 znaków
   EN: Cyclical Karma
   PL: Krążąca Karma
528. [Słowo kluczowe [CyclingKarma] — opis] 모든 캐릭터가 공격 적중 시마다 업보를 공격 대상에게 옮긴다. 아군이 살아있는동안에는 나는 비워내느니에게는 업보가 옮겨지지 않는다.
   źródło: BattleKeywords.json :: dataList[id=CyclingKarma].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All units transfer their Karma to their targets after a successful attack.\nKarma is not transferred to My Form Empties as long as its allies are alive.
   PL: Wszystkie postacie przy każdym trafieniu atakiem przenoszą Karmę na cel ataku. Dopóki żyją sojusznicy, Karma nie jest przenoszona na „Formę, Którą Wypełnia Pustka”
529. [Słowo kluczowe [CyclingKarma] — podsumowanie] 합 승리 시 업보 이동
   źródło: BattleKeywords.json :: dataList[id=CyclingKarma].summary
   limit: do 120 znaków
   EN: Karma transferred on Clash win
   PL: Karma przenoszona po wygranej w Starciu
530. [Słowo kluczowe [Cromer_Ecstasy] — nazwa] 희열
   źródło: BattleKeywords.json :: dataList[id=Cromer_Ecstasy].name
   kontekst: identyfikator tagu w tekstach: `[Cromer_Ecstasy]`
   limit: do 40 znaków
   EN: Ecstatic
   PL: Uniesienie
531. [Słowo kluczowe [Cromer_Ecstasy] — opis] 입 부위의 모든 물리 내성이 취약으로 변경됨.
   źródło: BattleKeywords.json :: dataList[id=Cromer_Ecstasy].desc
   limit: do 120 znaków
   EN: All the Maw’s physical resistances change to ‘Fatal’.
   PL: Wszystkie Odporności fizyczne Paszczy zmieniają się na „Wrażliwość”
532. [Słowo kluczowe [Cromer_Madness] — nazwa] 순수
   źródło: BattleKeywords.json :: dataList[id=Cromer_Madness].name
   kontekst: identyfikator tagu w tekstach: `[Cromer_Madness]`
   limit: do 40 znaków
   EN: Purity
   PL: Czystość
533. [Słowo kluczowe [Cromer_Madness] — opis] 모든 부위가 속박 3, 피해량 증가 3을 얻고, 모든 물리 내성이 취약으로 변경됨.
   źródło: BattleKeywords.json :: dataList[id=Cromer_Madness].desc
   limit: do 120 znaków
   EN: All parts gain 3 Bind and 3 Damage Up, and their phys. resistances change to ‘Fatal’.
   PL: Wszystkie części zyskują 3 Spętań i 3 Wzrosty Obrażeń, a ich Odporności fizyczne zmieniają się na „Wrażliwość”
534. [Słowo kluczowe [TakeHpHealReduce] — nazwa] 체력 회복 감소
   źródło: BattleKeywords.json :: dataList[id=TakeHpHealReduce].name
   kontekst: identyfikator tagu w tekstach: `[TakeHpHealReduce]`
   limit: do 40 znaków
   EN: HP Healing Down
   PL: Spadek Leczenia HP
535. [Słowo kluczowe [TakeHpHealReduce] — opis] 패시브, 스킬, 코인의 효과로 회복하는 체력이 수치에 비례하여 감소 (최대 5)
   źródło: BattleKeywords.json :: dataList[id=TakeHpHealReduce].desc
   limit: do 150 znaków
   EN: HP healed by Passives, Skill effects, or Coin effects decreases proportionally to the value of this effect. (Max 5)
   PL: HP leczone pasywami, Umiejętnościami lub monetami maleje proporcjonalnie do wartości efektu (maks. 5)
536. [Słowo kluczowe [AttackLevelAdder] — nazwa] 공격 레벨+
   źródło: BattleKeywords.json :: dataList[id=AttackLevelAdder].name
   kontekst: identyfikator tagu w tekstach: `[AttackLevelAdder]`
   limit: do 40 znaków
   EN: Offense level+
   PL: Poziom Ataku+
537. [Słowo kluczowe [AttackLevelAdder] — opis] 한 턴 동안 공격 레벨이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=AttackLevelAdder].desc
   limit: do 120 znaków
   EN: Offense Level increases by the effect’s Count for one turn.
   PL: W tej turze Poziom Ataku rośnie o wartość efektu
538. [Słowo kluczowe [Thirst] — nazwa] 갈증
   źródło: BattleKeywords.json :: dataList[id=Thirst].name
   kontekst: identyfikator tagu w tekstach: `[Thirst]`
   limit: do 40 znaków
   EN: Appetite
   PL: Pragnienie
539. [Słowo kluczowe [Thirst] — opis] 즉흥 조리 패시브의 회복량이 수치에 비례하여 증가. 패시브 발동 시 전부 소모.
   źródło: BattleKeywords.json :: dataList[id=Thirst].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Increases the healing provided by the Passive [Rustle Up].\nSpent when the Passive activates.
   PL: Zwiększa leczenie z pasywu „Improwizowane Gotowanie” proporcjonalnie do wartości. Zużywane przy aktywacji pasywu.
540. [Słowo kluczowe [GainSinStockAdder] — nazwa] E.G.O 자원 획득량 +
   źródło: BattleKeywords.json :: dataList[id=GainSinStockAdder].name
   kontekst: identyfikator tagu w tekstach: `[GainSinStockAdder]`
   limit: do 40 znaków
   EN: E.G.O Resource Amp
   PL: Zysk Zasobów E.G.O +
541. [Słowo kluczowe [GainSinStockAdder] — opis] 한 턴 동안 스킬 사용 시 획득하는 E.G.O 자원 수가 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=GainSinStockAdder].desc
   limit: do 130 znaków
   EN: Increases the amount of E.G.O resources earned from skills by the effect’s Count for one turn.
   PL: W tej turze liczba zasobów E.G.O zyskiwanych przy użyciu Umiejętności rośnie o wartość efektu
542. [Słowo kluczowe [Enrage] — nazwa] 광란
   źródło: BattleKeywords.json :: dataList[id=Enrage].name
   kontekst: identyfikator tagu w tekstach: `[Enrage]`
   limit: do 40 znaków
   EN: Frenzy
   PL: Furia
543. [Słowo kluczowe [Enrage] — opis] 이번 턴동안 공격 위력 증가 3, 취약 3을 얻고, 스킬 패턴이 변경됨. 피격 시 본능을 얻지 않음.
   źródło: BattleKeywords.json :: dataList[id=Enrage].desc
   limit: do 140 znaków
   EN: Gain 3 Attack Power Up and 3 Fragile this turn, and change behavior. Does not gain Instincts when attacked.
   PL: W tej turze zyskuje 3 Wzrosty Mocy Ataku i 3 Wrażliwości, a wzorce Umiejętności się zmieniają. Nie zyskuje Instynktu przy trafieniu.
544. [Słowo kluczowe [DimensionRift] — nazwa] 차원 균열
   źródło: BattleKeywords.json :: dataList[id=DimensionRift].name
   kontekst: identyfikator tagu w tekstach: `[DimensionRift]`
   limit: do 40 znaków
   EN: Dimensional Rift
   PL: Szczelina Wymiarowa
545. [Słowo kluczowe [DimensionRift] — opis] 턴 종료 시 파열 횟수가 수치만큼 증가한 뒤 이 효과 소멸
   źródło: BattleKeywords.json :: dataList[id=DimensionRift].desc
   limit: do 120 znaków
   EN: At the end of the turn, gain Rupture Count by this effect’s Stack. Then, remove this effect.
   PL: Na koniec tury Licznik Rozdarcia rośnie o wartość tego efektu, po czym efekt znika
546. [Słowo kluczowe [ShardOfUmbrella] — nazwa] 우산 파편
   źródło: BattleKeywords.json :: dataList[id=ShardOfUmbrella].name
   kontekst: identyfikator tagu w tekstach: `[ShardOfUmbrella]`
   limit: do 40 znaków
   EN: Umbrella Splinters
   PL: Odłamki Parasola
547. [Słowo kluczowe [ShardOfUmbrella] — opis] 턴 종료 시 수치당 5만큼 파열 얻음
   źródło: BattleKeywords.json :: dataList[id=ShardOfUmbrella].desc
   limit: do 120 znaków
   EN: Gain 5 Rupture per Count at turn end
   PL: Na koniec tury zyskuje 5 Rozdarcia za każdą wartość
548. [Słowo kluczowe [ShardOfUmbrella] — podsumowanie] 턴 종료 시 수치당 5만큼 파열 얻음
   źródło: BattleKeywords.json :: dataList[id=ShardOfUmbrella].summary
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Słowo kluczowe [WrappedCurseTag] — nazwa] 얽혀온 저주 부적
   źródło: BattleKeywords.json :: dataList[id=WrappedCurseTag].name
   kontekst: identyfikator tagu w tekstach: `[WrappedCurseTag]`
   limit: do 40 znaków
   EN: Entangled Curse Talisman
   PL: Opleciony Talizman Klątwy
550. [Słowo kluczowe [WrappedCurseTag] — opis] 가하는 피해량 수치당 1% 증가\n수치가 9이상이라면, 턴 시작 시 공격 위력 감소 2 얻음
   źródło: BattleKeywords.json :: dataList[id=WrappedCurseTag].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +1% damage per Stack\nAt 9+ Stack, gain 2 Attack Power Down at turn start
   PL: Zadawane obrażenia rosną o 1% za każdy stos\nPrzy 9 lub więcej stosach na początku tury zyskuje 2 Spadki Mocy Ataku
551. [Słowo kluczowe [WrappedCurseTag] — podsumowanie] 가하는 피해량 수치당 1%, 9이상이라면, 턴 시작 시 공격 위력 감소 2 얻음
   źródło: BattleKeywords.json :: dataList[id=WrappedCurseTag].summary
   limit: do 120 znaków
   EN: Deal +1% damage per Stack; at 9+ Stack, gain 2 Attack Power Down at turn start
   PL: Zadawane obrażenia +1% za stos; przy 9 lub więcej stosach 2 Spadki Mocy Ataku na początku tury
552. [Słowo kluczowe [ReattachedCurseTag] — nazwa] 다시 붙여진 저주 부적
   źródło: BattleKeywords.json :: dataList[id=ReattachedCurseTag].name
   kontekst: identyfikator tagu w tekstach: `[ReattachedCurseTag]`
   limit: do 40 znaków
   EN: Reattached Curse Talisman
   PL: Ponownie Przyklejony Talizman Klątwy
553. [Słowo kluczowe [ReattachedCurseTag] — opis] 수치가 9이상이라면, 턴 시작 시 속박 5 얻음.\n12이상이라면, 턴 시작 시 공격 위력 감소 5 얻음.
   źródło: BattleKeywords.json :: dataList[id=ReattachedCurseTag].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At 9+, gain 5 Bind at the start of the turn.\nAt 12+, gain 5 Attack Power Down at the start of the turn.
   PL: Przy 9 lub więcej wartości na początku tury zyskuje 5 Spętań.\nPrzy 12 lub więcej zyskuje 5 Spadków Mocy Ataku na początku tury.
554. [Słowo kluczowe [ReattachedCurseTag] — podsumowanie] 수치가 9이상이라면, 턴 시작 시 속박 5 얻음.\n12이상이라면, 턴 시작 시 공격 위력 감소 5 얻음.
   źródło: BattleKeywords.json :: dataList[id=ReattachedCurseTag].summary
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Słowo kluczowe [ElectricStorage] — nazwa] 축전
   źródło: BattleKeywords.json :: dataList[id=ElectricStorage].name
   kontekst: identyfikator tagu w tekstach: `[ElectricStorage]`
   limit: do 40 znaków
   EN: Capacitor
   PL: Kondensator
556. [Słowo kluczowe [ElectricStorage] — opis] 몸에 전류가 쌓이는 것 같다.
   źródło: BattleKeywords.json :: dataList[id=ElectricStorage].desc
   limit: do 120 znaków
   EN: It seems to be storing electricity in its body.
   PL: Wydaje się, że w jego ciele gromadzi się prąd.
557. [Słowo kluczowe [SelfCharge] — nazwa] 자가 충전
   źródło: BattleKeywords.json :: dataList[id=SelfCharge].name
   kontekst: identyfikator tagu w tekstach: `[SelfCharge]`
   limit: do 40 znaków
   EN: Self-charge
   PL: Samoładowanie
558. [Słowo kluczowe [SelfCharge] — opis] 몸 주변으로 전류가 흐르는 것 같다.\n죽음을 맞이한 후 자가 충전이 남아있다면 전부 소모하기 전까지 체력 1로 고정. (최대 20)
   źródło: BattleKeywords.json :: dataList[id=SelfCharge].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Electric currents seem to flow around its body.\nAfter the unit faces death, as long as it has Self-charge, its HP is fixed at 1 until it is fully consumed. (Max 20)
   PL: Wokół ciała zdają się płynąć prądy.\nPo doświadczeniu śmierci, dopóki pozostaje Samoładowanie, HP zostaje ustalone na 1, aż do pełnego zużycia. (maks. 20)
559. [Słowo kluczowe [Exalted] — nazwa] 고양
   źródło: BattleKeywords.json :: dataList[id=Exalted].name
   kontekst: identyfikator tagu w tekstach: `[Exalted]`
   limit: do 40 znaków
   EN: Morale Boost
   PL: Podniesienie Moralu
560. [Słowo kluczowe [Exalted] — opis] 매 턴마다 피해량 증가를 수치만큼 얻음 (최대 5)\n취기가 있을 때, 얻을 수 없음.
   źródło: BattleKeywords.json :: dataList[id=Exalted].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Damage Up by the the effect's Count every turn (Max 5)\nCannot gain the status while Tipsy
   PL: Co turę zyskuje tyle Wzrostów Obrażeń, ile wynosi wartość (maks. 5)\nNie można zyskać w stanie Pijaństwa
561. [Słowo kluczowe [Exalted] — podsumowanie] 매 턴마다 피해량 증가를 수치만큼 얻음 취기가 있을 때, 얻을 수 없음.
   źródło: BattleKeywords.json :: dataList[id=Exalted].summary
   limit: do 120 znaków
   EN: Gain Damage Up by the effect's Count every turn; Cannot gain the status while Tipsy
   PL: Co turę zyskuje tyle Wzrostów Obrażeń, ile wynosi wartość; nie można zyskać w stanie Pijaństwa
562. [Słowo kluczowe [Tipsiness] — nazwa] 취기
   źródło: BattleKeywords.json :: dataList[id=Tipsiness].name
   kontekst: identyfikator tagu w tekstach: `[Tipsiness]`
   limit: do 40 znaków
   EN: Tipsy
   PL: Pijaństwo
563. [Słowo kluczowe [Tipsiness] — opis] 합 위력이 수치만큼 감소 (최대 5)
   źródło: BattleKeywords.json :: dataList[id=Tipsiness].desc
   limit: do 120 znaków
   EN: Lose Clash Power equal to Stack (max 5)
   PL: Moc Starcia maleje o wartość stosów (maks. 5)
564. [Słowo kluczowe [Tipsiness] — podsumowanie] 합 위력이 수치만큼 감소
   źródło: BattleKeywords.json :: dataList[id=Tipsiness].summary
   limit: do 120 znaków
   EN: Lose Clash Power equal to Stack
   PL: Moc Starcia maleje o wartość stosów
565. [Słowo kluczowe [Predation] — nazwa] 포식
   źródło: BattleKeywords.json :: dataList[id=Predation].name
   kontekst: identyfikator tagu w tekstach: `[Predation]`
   limit: do 40 znaków
   EN: Predation
   PL: Drapieżność
566. [Słowo kluczowe [Predation] — opis] 강력한 기술을 사용하는 것 같다.
   źródło: BattleKeywords.json :: dataList[id=Predation].desc
   limit: do 120 znaków
   EN: It seems to be preparing a powerful move.
   PL: Wydaje się, że przygotowuje potężny atak.
567. [Słowo kluczowe [ATL_EndureCombustion] — nazwa] 화상 저항
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureCombustion].name
   kontekst: identyfikator tagu w tekstach: `[ATL_EndureCombustion]`
   limit: do 40 znaków
   EN: Burn Resistance
   PL: Odporność na Podpalenie
568. [Słowo kluczowe [ATL_EndureCombustion] — opis] 화상에 피해를 입을 때, 수치당 10%만큼 피해량 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureCombustion].desc
   limit: do 120 znaków
   EN: When taking damage from Burn, reduce the damage by 10% per Count (Max 10)
   PL: Otrzymując obrażenia od Podpalenia, zmniejsza je o 10% za każdą wartość (maks. 10)
569. [Słowo kluczowe [ATL_EndureCombustion] — podsumowanie] 화상에 피해를 입을 때, 수치당 10%만큼 감소한 피해를 입는다.
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureCombustion].summary
   limit: do 120 znaków
   EN: When taking damage from Burn, take 10% less damage per Count
   PL: Otrzymując obrażenia od Podpalenia, otrzymuje o 10% mniej obrażeń za każdą wartość
570. [Słowo kluczowe [Resonate] — nazwa] 공진
   źródło: BattleKeywords.json :: dataList[id=Resonate].name
   kontekst: identyfikator tagu w tekstach: `[Resonate]`
   limit: do 40 znaków
   EN: Resonant
   PL: Rezonans
571. [Słowo kluczowe [Resonate] — opis] 대상에게 진동 폭발 또는 흐트러짐 손상을 줄 때, 추가로 고정 피해량을 수치당 3만큼 입힘. 흐트러짐 손상을 수치당 3%만큼 입힘.
   źródło: BattleKeywords.json :: dataList[id=Resonate].desc
   limit: do 180 znaków
   EN: When triggering Tremor Burst or raising Stagger Threshold, deal 3 fixed damage per Count and further raise stagger threshold by 3% per Count
   PL: Wywołując Wybuch Wstrząsu lub podnosząc Próg Oszołomienia, zadaje dodatkowo 3 obrażeń stałych za każdą wartość i podnosi Próg Oszołomienia o 3% za każdą wartość
572. [Słowo kluczowe [Resonate] — podsumowanie] 진동 폭발 혹은 흐트러짐 손상을 줄 때, 피해량과 흐트러짐 손상을 추가로 줌.
   źródło: BattleKeywords.json :: dataList[id=Resonate].summary
   limit: do 140 znaków
   EN: When triggering Tremor Burst or raising Stagger Thresholds, deal damage and raise Stagger Threshold further
   PL: Wywołując Wybuch Wstrząsu lub podnosząc Próg Oszołomienia, zadaje dodatkowe obrażenia i podnosi Próg Oszołomienia
573. [Słowo kluczowe [VibrationAssimilation] — nazwa] 진동 동화
   źródło: BattleKeywords.json :: dataList[id=VibrationAssimilation].name
   kontekst: identyfikator tagu w tekstach: `[VibrationAssimilation]`
   limit: do 40 znaków
   EN: Tremor Sync
   PL: Synchronizacja Wstrząsu
574. [Słowo kluczowe [VibrationAssimilation] — opis] 대상이 가지고 있는 진동 5마다, 대상의 합 위력 -1
   źródło: BattleKeywords.json :: dataList[id=VibrationAssimilation].desc
   limit: do 120 znaków
   EN: In a clash, the opponent has -1 Clash Power for every 5 Tremor they have
   PL: Podczas Starcia przeciwnik ma -1 Mocy Starcia za każde 5 Wstrząsu, które posiada
575. [Słowo kluczowe [VibrationAssimilation] — podsumowanie] 대상이 가지고 있는 진동 5마다, 대상의 합 위력 -1
   źródło: BattleKeywords.json :: dataList[id=VibrationAssimilation].summary
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Słowo kluczowe [CollapseAmpoule] — nazwa] 붕괴 앰플
   źródło: BattleKeywords.json :: dataList[id=CollapseAmpoule].name
   kontekst: identyfikator tagu w tekstach: `[CollapseAmpoule]`
   limit: do 40 znaków
   EN: Decay Ampule
   PL: Ampułka Rozpadu
577. [Słowo kluczowe [CollapseAmpoule] — opis] 최대 체력의 수치당 2%만큼 피해 입힘.
   źródło: BattleKeywords.json :: dataList[id=CollapseAmpoule].desc
   limit: do 120 znaków
   EN: Take damage by 2% of Max HP per Count
   PL: Otrzymuje obrażenia równe 2% Maks. HP za każdą wartość
578. [Słowo kluczowe [CollapseAmpoule] — podsumowanie] 최대 체력의 수치당 2%만큼 피해 입힘.
   źródło: BattleKeywords.json :: dataList[id=CollapseAmpoule].summary
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Słowo kluczowe [InterlockingTime] — nazwa] 맞물리는 시간
   źródło: BattleKeywords.json :: dataList[id=InterlockingTime].name
   kontekst: identyfikator tagu w tekstach: `[InterlockingTime]`
   limit: do 40 znaków
   EN: Interlocking Time
   PL: Sprzężony Czas
580. [Słowo kluczowe [InterlockingTime] — opis] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 1.5배만큼 고정 피해를 입음.
   źródło: BattleKeywords.json :: dataList[id=InterlockingTime].desc
   limit: do 150 znaków
   EN: Reduce final damage by 30% and store it. At 3 Stacks, take fixed damage equal to 1.5 times the accumulated damage
   PL: Redukuje 30% obrażeń końcowych i gromadzi je. Przy 3 stosach otrzymuje obrażenia stałe równe 1,5 gromadzonych obrażeń
581. [Słowo kluczowe [InterlockingTime] — podsumowanie] 최종 피해의 30%만큼 감소 및 저장. 수치가 3이 되면, 쌓인 피해량의 1.5배만큼 고정 피해를 입음.
   źródło: BattleKeywords.json :: dataList[id=InterlockingTime].summary
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Słowo kluczowe [TimeRental] — nazwa] 심상 속 시간 대여
   źródło: BattleKeywords.json :: dataList[id=TimeRental].name
   kontekst: identyfikator tagu w tekstach: `[TimeRental]`
   limit: do 40 znaków
   EN: Borrowed Time of the Fathoms
   PL: Pożyczony Czas Wyobraźni
583. [Słowo kluczowe [TimeRental] — opis] 턴 종료 시 신속 3, 피해량 증가 2 얻음. 턴 종료 시 수치가 1 남았다면, 다음 턴에 속박 4, 공격 위력 감소 1 얻음
   źródło: BattleKeywords.json :: dataList[id=TimeRental].desc
   limit: do 160 znaków
   EN: At the end of the turn, gain 3 Haste and 2 Damage Up; If only 1 Stack remains, gain 4 Bind and 1 Attack Power Down next turn
   PL: Na koniec tury zyskuje 3 Pośpiechu i 2 Wzrosty Obrażeń. Jeśli na koniec tury pozostaje 1 wartość, w następnej turze zyskuje 4 Spętań i 1 Spadek Mocy Ataku
584. [Słowo kluczowe [TimeRental] — podsumowanie] 턴 종료 시 신속 3, 피해량 증가 2 얻음. 턴 종료 시 수치가 1 남았다면, 다음 턴에 속박 4, 공격 위력 감소 1 얻음
   źródło: BattleKeywords.json :: dataList[id=TimeRental].summary
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Słowo kluczowe [ATL_EndureLaceration] — nazwa] 출혈 저항
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureLaceration].name
   kontekst: identyfikator tagu w tekstach: `[ATL_EndureLaceration]`
   limit: do 40 znaków
   EN: Bleed Resistance
   PL: Odporność na Krwawienie
586. [Słowo kluczowe [ATL_EndureLaceration] — opis] 출혈에 피해를 입을 때, 수치당 10%만큼 피해량 감소 (최대 10)
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureLaceration].desc
   limit: do 120 znaków
   EN: When taking damage from Bleed, reduce the damage by 10% per Count (Max 10)
   PL: Otrzymując obrażenia od Krwawienia, zmniejsza je o 10% za każdą wartość (maks. 10)
587. [Słowo kluczowe [ATL_EndureLaceration] — podsumowanie] 출혈에 피해를 입을 때, 수치당 10%만큼 감소한 피해를 입는다.
   źródło: BattleKeywords.json :: dataList[id=ATL_EndureLaceration].summary
   limit: do 120 znaków
   EN: When taking damage from Bleed, take 10% less damage per Count
   PL: Otrzymując obrażenia od Krwawienia, otrzymuje o 10% mniej obrażeń za każdą wartość
588. [Słowo kluczowe [Bull_Sadness] — nazwa] 해소되지 않은 슬픔
   źródło: BattleKeywords.json :: dataList[id=Bull_Sadness].name
   kontekst: identyfikator tagu w tekstach: `[Bull_Sadness]`
   limit: do 40 znaków
   EN: Unresolved Sorrow
   PL: Nierozwiązany Smutek
589. [Słowo kluczowe [Bull_Sadness] — opis] 턴 시작 시 수치만큼 공격 위력 감소를 얻음\n턴 종료 시 수치가 3 이상이면, 팽창하는 슬픔 으로 교체됨
   źródło: BattleKeywords.json :: dataList[id=Bull_Sadness].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, gain Attack Power Down by the Count.\nAt the end of the turn, if this effect is at 3+ Count, changes to Expanding Sorrow
   PL: Na początku tury zyskuje tyle Spadków Mocy Ataku, ile wynosi wartość\nNa koniec tury, przy 3 lub więcej wartości, zmienia się w „Rozszerzający Smutek”
590. [Słowo kluczowe [Bull_BuzzingEmotion] — nazwa] 울렁이는 감정
   źródło: BattleKeywords.json :: dataList[id=Bull_BuzzingEmotion].name
   kontekst: identyfikator tagu w tekstach: `[Bull_BuzzingEmotion]`
   limit: do 40 znaków
   EN: Wavering Emotions
   PL: Wahające się Emocje
591. [Słowo kluczowe [Bull_BuzzingEmotion] — opis] 턴 시작 시 공격 위력 감소, 마비, 속박 중 무작위로 수치만큼 얻고 소멸
   źródło: BattleKeywords.json :: dataList[id=Bull_BuzzingEmotion].desc
   limit: do 150 znaków
   EN: Turn Start: Randomly gain Attack Power Down, Paralyze, or Bind by this effect's Count, then remove this effect
   PL: Na początku tury zyskuje losowo tyle Spadków Mocy Ataku, Paraliżu albo Spętań, ile wynosi wartość, po czym efekt znika
592. [Słowo kluczowe [Bull_BuzzingEmotion] — podsumowanie] 턴 시작 시 공격 위력 감소, 마비, 속박 중 무작위로 수치만큼 얻고 소멸
   źródło: BattleKeywords.json :: dataList[id=Bull_BuzzingEmotion].summary
   (powtórzenie elementu 591 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Słowo kluczowe [Scared] — nazwa] 두려움
   źródło: BattleKeywords.json :: dataList[id=Scared].name
   kontekst: identyfikator tagu w tekstach: `[Scared]`
   limit: do 40 znaków
   EN: Fear
   PL: Lęk
594. [Słowo kluczowe [Scared] — opis] 정신력이 -20이하일 때, 턴 종료 시 다음 턴에 보호 1 얻음.
   źródło: BattleKeywords.json :: dataList[id=Scared].desc
   limit: do 120 znaków
   EN: Turn End: At -20 SP or lower, gain 1 Protection next turn.
   PL: Przy Poczytalności -20 lub niższej, na koniec tury zyskuje 1 Ochrony w następnej turze
595. [Słowo kluczowe [Scared] — podsumowanie] 정신력이 -20이하일 때, 턴 종료 시 다음 턴에 보호 1 얻음.
   źródło: BattleKeywords.json :: dataList[id=Scared].summary
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Słowo kluczowe [Stressed] — nazwa] 스트레스
   źródło: BattleKeywords.json :: dataList[id=Stressed].name
   kontekst: identyfikator tagu w tekstach: `[Stressed]`
   limit: do 40 znaków
   EN: Stressed
   PL: Stres
597. [Słowo kluczowe [Stressed] — opis] 정신력이 -25이하일 때, 턴 종료 시 다음 턴에 수비 위력 증가 1 얻음.
   źródło: BattleKeywords.json :: dataList[id=Stressed].desc
   limit: do 120 znaków
   EN: Turn End: At -25 SP or lower, gain 1 Defense Power Up next turn
   PL: Przy Poczytalności -25 lub niższej, na koniec tury zyskuje 1 Wzrost Mocy Obrony w następnej turze
598. [Słowo kluczowe [Stressed] — podsumowanie] 정신력이 -25이하일 때, 턴 종료 시 다음 턴에 수비 위력 증가 1 얻음.
   źródło: BattleKeywords.json :: dataList[id=Stressed].summary
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Słowo kluczowe [Nervous] — nazwa] 초조함
   źródło: BattleKeywords.json :: dataList[id=Nervous].name
   kontekst: identyfikator tagu w tekstach: `[Nervous]`
   limit: do 40 znaków
   EN: Nervous
   PL: Nerwowość
600. [Słowo kluczowe [Nervous] — opis] 정신력이 -15이하일 때, 턴 종료 시 다음 턴에 방어 레벨 증가 5 얻음.
   źródło: BattleKeywords.json :: dataList[id=Nervous].desc
   limit: do 120 znaków
   EN: Turn End: At -15 SP or lower, gain 5 Defense Level Up next turn
   PL: Przy Poczytalności -15 lub niższej, na koniec tury zyskuje 5 Wzrostów Poziomu Obrony w następnej turze
601. [Słowo kluczowe [Nervous] — podsumowanie] 정신력이 -15이하일 때, 턴 종료 시 다음 턴에 방어 레벨 증가 5 얻음.
   źródło: BattleKeywords.json :: dataList[id=Nervous].summary
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
