# Paczka AI P59 (Fala 3 · 3B) — Dary E.G.O (Lustrzane Lochy i fabularne) (część 4/5)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P59_3b_dary_ego_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P59_3b_dary_ego_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Dar E.G.O: EGOgift_MirrorDungeon
- plik gry: `EGOgift_MirrorDungeon.json`

1. [Dar E.G.O [9199] — nazwa] 튿어진 소매
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9199].name
   limit: do 40 znaków
   EN: Torn Hems
   PL: — nazwa] Podarte Rękawy
2. [Dar E.G.O [9199] — opis] 관통 유형인 스킬 2의 공격 레벨 +2, 코인 수가 2개 이하인 경우에는 효과가 강화되어 공격 레벨 +2, 합 위력 +(2/코인 수).\n- 기술해방연합 소속 인격은 효과가 변경되어, 관통 유형인 모든 기본 공격 스킬에 효과 적용\n\n기술해방연합 소속 인격이 턴 시작 시 자신이 보유한 부정적인 효과 수만큼 [AttackUp]를 얻음 (최대 3).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9199].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Pierce Attack Type Skill 2: Offense Level +2; if the Skill has 2 Coins or fewer, Offense Level +2 and Clash Power (2/# of Coins) instead.\n- For Technology Liberation Alliance Identities: above effect applies to all Pierce Attack Type Base Attack Skills\n\nTurn Start: Technology Liberation Alliance Identities gain (# of negative effects on self) [AttackUp]. (max 3)
   PL: — opis] Umiejętność 2 typu Kłucia zyskuje Poziom Ataku +2; przy 2 monetach lub mniej efekt jest wzmocniony: Poziom Ataku +2 i Moc Starcia +(2/liczba monet).\n- Tożsamości Sojuszu Wyzwolenia Technologii: efekt zmienia się i stosuje do wszystkich podstawowych Umiejętności ataku typu Kłucia\n\nNa początku tury Tożsamości Sojuszu Wyzwolenia Technologii zyskują [AttackUp] w liczbie równej liczbie posiadanych ujemnych efektów (maks. 3).
3. [Dar E.G.O [9199] — opis skrócony] 공격 레벨 증가, 코인 수 2개 이하의 스킬은 추가로 합 위력 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9199].simpleDesc[abilityID=9199].simpleDesc
   limit: do 120 znaków
   EN: Offense Level Up; Skills with 2 Coins or fewer gain Clash Power
   PL: — opis skrócony] Wzrost Poziomu Ataku; Umiejętności z 2 monetami lub mniej zyskują dodatkowo Moc Starcia
4. [Dar E.G.O [9199] — opis skrócony] 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9199].simpleDesc[abilityID=91991].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level Up
   PL: — opis skrócony] Zyskuje Wzrost Poziomu Ataku
5. [Dar E.G.O [19199] — nazwa] 튿어진 소매+
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19199].name
   limit: do 40 znaków
   EN: Torn Hems+
   PL: — nazwa] Podarte Rękawy+
6. [Dar E.G.O [19199] — opis] 관통 유형인 스킬 2의 공격 레벨 +2, 코인 수가 2개 이하인 경우에는 효과가 강화되어 공격 레벨 +2, 합 위력 +(2/코인 수).\n- 기술해방연합 소속 인격은 효과가 변경되어, 관통 유형 <style="upgradeHighlight">또는 탐식 속성</style>인 모든 기본 공격 스킬에 효과 적용\n\n기술해방연합 소속 인격이 턴 시작 시 <style="upgradeHighlight">(자신이 보유한 부정적인 효과 수 + 1)</style>만큼 [AttackUp]를 얻음 (최대 <style="upgradeHighlight">4</style>).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19199].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Pierce Attack Type Skill 2: Offense Level +2; if the Skill has 2 Coins or fewer, Offense Level +2 and Clash Power (2/# of Coins) instead.\n- For Technology Liberation Alliance Identities: above effect applies to all Pierce Attack Type <style="upgradeHighlight">or Gluttony Affinity</style> Base Attack Skills\n\nTurn Start: Technology Liberation Alliance Identities gain <style="upgradeHighlight">(# of negative effects on self + 1)</style> [AttackUp]. (max <style="upgradeHighlight">4</style>)
   PL: — opis] Umiejętność 2 typu Kłucia zyskuje Poziom Ataku +2; przy 2 monetach lub mniej efekt jest wzmocniony: Poziom Ataku +2 i Moc Starcia +(2/liczba monet).\n- Tożsamości Sojuszu Wyzwolenia Technologii: efekt zmienia się i stosuje do wszystkich podstawowych Umiejętności ataku typu Kłucia <style="upgradeHighlight">lub Grzechu Obżarstwa</style>\n\nNa początku tury Tożsamości Sojuszu Wyzwolenia Technologii zyskują <style="upgradeHighlight">(liczba posiadanych ujemnych efektów + 1)</style> [AttackUp] (maks. <style="upgradeHighlight">4</style>).
7. [Dar E.G.O [19199] — opis skrócony] 공격 레벨 증가, 코인 수 2개 이하의 스킬은 추가로 합 위력 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19199].simpleDesc[abilityID=19199].simpleDesc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Dar E.G.O [19199] — opis skrócony] 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19199].simpleDesc[abilityID=191991].simpleDesc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [Dar E.G.O [29199] — nazwa] 튿어진 소매++
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29199].name
   limit: do 40 znaków
   EN: Torn Hems++
   PL: — nazwa] Podarte Rękawy++
10. [Dar E.G.O [29199] — opis] 관통 유형인 스킬 2의 공격 레벨 +2, 코인 수가 2개 이하인 경우에는 효과가 강화되어 공격 레벨 +2, 합 위력 +(2/코인 수).\n- 기술해방연합 소속 인격은 효과가 변경되어, <style="upgradeHighlight">모든</style> 기본 공격 스킬에 효과 적용\n\n기술해방연합 소속 인격이 턴 시작 시 <style="upgradeHighlight">합 위력 증가 1</style>,(자신이 보유한 부정적인 효과 중 가장 높은 수치의 값 +1)만큼 [AttackUp]를 얻음 (최대 <style="upgradeHighlight">5</style>).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29199].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Pierce Attack Type Skill 2: Offense Level +2; if the Skill has 2 Coins or fewer, Offense Level +2 and Clash Power (2/# of Coins) instead.\n- For Technology Liberation Alliance Identities: above effect applies to <style="upgradeHighlight">all</style> Base Attack Skills\n\nTurn Start: Technology Liberation Alliance Identities gain <style="upgradeHighlight">1 Clash Power Up</style> and (value of highest Stack among negative effects on self + 1) [AttackUp]. (max <style="upgradeHighlight">5</style>)
   PL: — opis] Umiejętność 2 typu Kłucia zyskuje Poziom Ataku +2; przy 2 monetach lub mniej efekt jest wzmocniony: Poziom Ataku +2 i Moc Starcia +(2/liczba monet).\n- Tożsamości Sojuszu Wyzwolenia Technologii: efekt zmienia się i stosuje do <style="upgradeHighlight">wszystkich</style> podstawowych Umiejętności ataku\n\nNa początku tury Tożsamości Sojuszu Wyzwolenia Technologii zyskują <style="upgradeHighlight">1 Wzrost Mocy Starcia</style> oraz [AttackUp] w liczbie równej (najwyższa wartość posiadanych ujemnych efektów +1) (maks. <style="upgradeHighlight">5</style>).
11. [Dar E.G.O [29199] — opis skrócony] 공격 레벨 증가, 코인 수 2개 이하의 스킬은 추가로 합 위력 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29199].simpleDesc[abilityID=29199].simpleDesc
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Dar E.G.O [29199] — opis skrócony] 합 위력 증가, 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29199].simpleDesc[abilityID=291991].simpleDesc
   limit: do 120 znaków
   EN: Gain Clash Power and Offense Level Up
   PL: — opis skrócony] Zyskuje Moc Starcia i Wzrost Poziomu Ataku
13. [Dar E.G.O [9200] — nazwa] 듀엘교본 3권
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].name
   limit: do 40 znaków
   EN: Dueling Manual Book 3
   PL: — nazwa] Podręcznik Pojedynków Tom 3
14. [Dar E.G.O [9200] — opis] 관통 기본 공격 스킬의 합 위력 +2. 전투 시작 시, 자신을 제외하고 이번 턴에 관통 기본 공격 스킬을 사용하는 인격 수만큼 [AttackUp] 얻음 (최대 3).\n\n보유한 모든 기본 공격 스킬이 관통 유형인 아군이 턴 시작 시 [PenetrateDamageUp] 2 얻음 (강화되거나 특수 발동하는 경우 제외).\n\n회피 스킬 위력 +2. 아군 인격이 이번 턴 동안 회피를 2회 성공할 때마다 다음 턴에 [AttackDmgUp] 1 얻음 (최대 3).\n\n섕크 협회 소속 인격이 턴 시작 시 [PenetrateResultUp] 1, [PenetrateDamageUp] 2 얻음. 섕크 협회 소속 인격이 본인이 부여한 결투 선포, 점혈 또는 집중 공격을 보유한 적에게 기본 스킬로 공격 적중 시 피해를 입혔다면, 다음 턴에 [PenetrateDamageUp] 2, [Agility] 1 얻음 (인격 별로 턴 당 1회).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [PenetrateDamageUp], [AttackDmgUp], [PenetrateResultUp], [Agility]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Agility] = 신속 / Haste
   EN: Pierce Base Attack Skills gain Clash Power +2. On Combat Start, gain [AttackUp] equal to the number of Identities who are using Pierce base Attack Skills this turn. (max 3)\n\nAllies with Pierce Attack Type for all of their base Attack Skills gain 2 [PenetrateDamageUp] at Turn Start. (except for Empowered Skills or Skills that need unique conditionals)\n\nEvade Skill Power +2. Every time an allied Identity successfully Evades 2 times within a single turn, they gain 1 [AttackDmgUp] next turn (max 3)\n\nAt Turn Start, Cinq Association Identities gain 1 [PenetrateResultUp] and 2 [PenetrateDamageUp]; if a Cinq Association Identity, using Base Skills to attack, dealt damage On Hit against an enemy inflicted by their 'Declared Duel', 'Nerve Strike', or 'Focused Attack', gain 2 [PenetrateDamageUp] and 1 [Agility] next turn. (once per Identity per turn)
   PL: — opis] Moc Starcia podstawowych Umiejętności ataku Kłucia +2. Na początku walki zyskuje [AttackUp] w liczbie równej liczbie Tożsamości używających podstawowych Umiejętności ataku Kłucia w tej turze (maks. 3).\n\nSojusznicy, których wszystkie podstawowe Umiejętności ataku są typu Kłucia, zyskują na początku tury 2 [PenetrateDamageUp] (z pominięciem Umiejętności wzmocnionych lub wymagających specjalnych warunków).\n\nMoc Umiejętności Uniku +2. Za każde 2 udane Uniki sojuszniczej Tożsamości w tej turze zyskuje ona 1 [AttackDmgUp] na następną turę (maks. 3).\n\nTożsamości Stowarzyszenia Cinq zyskują na początku tury 1 [PenetrateResultUp] i 2 [PenetrateDamageUp]. Przy trafieniu podstawową Umiejętnością wroga posiadającego Wyzwanie na Pojedynek, Punkt Witalny lub Atak Skupiony nałożone przez tę Tożsamość, jeżeli zadano obrażenia, zyskuje ona 2 [PenetrateDamageUp] i 1 [Agility] na następną turę (1 raz na turę na Tożsamość).
15. [Dar E.G.O [9200] — opis skrócony] 합 위력 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].simpleDesc[abilityID=9200].simpleDesc
   limit: do 120 znaków
   EN: Clash Power Up
   PL: Wzrost Mocy Starcia
16. [Dar E.G.O [9200] — opis skrócony] 관통 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].simpleDesc[abilityID=92001].simpleDesc
   limit: do 120 znaków
   EN: Pierce DMG Up
   PL: Wzrost Obrażeń Przebicia
17. [Dar E.G.O [9200] — opis skrócony] 회피 스킬 위력 증가. 회피 3회 성공시마다 관통 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].simpleDesc[abilityID=92002].simpleDesc
   limit: do 120 znaków
   EN: Gain Evade Skill Power. Gain Pierce DMG Up after every 3 successful Evade
   PL: — opis skrócony] Wzrost Mocy Umiejętności Uniku. Za każde 3 udane Uniki Wzrost Obrażeń Kłucia
18. [Dar E.G.O [9200] — opis skrócony] 관통 위력 증가, 관통 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9200].simpleDesc[abilityID=92003].simpleDesc
   limit: do 120 znaków
   EN: Gain Pierce Power Up and deal more Pierce damage
   PL: — opis skrócony] Wzrost Mocy Kłucia i Wzrost Obrażeń Kłucia
19. [Dar E.G.O [9201] — nazwa] 차원분리수거함
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9201].name
   limit: do 40 znaków
   EN: Dimensional Recycle Bin
   PL: — nazwa] Wymiarowy Kosz Segregacyjny
20. [Dar E.G.O [9201] — opis] [편성 3번 인격 전용 효과]\n\n타격 스킬 공격 레벨 +(보유한 타격 기본 공격 스킬 수) (동일한 스킬은 하나로 계산, 최대 3).\n\n스킬을 사용하여 적 공격 시 다른 스킬을 [Discard]하였다면, 타격 피해량 +(10+버린 스킬의 등급 x5)% (가장 높은 등급으로 계산, 최대 25%).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9201].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [Discard]
   znaczenie tagów: [Discard] = 버림 / Discard
   EN: [Effects apply only to the #3 Deployed Identity]\n\nBlunt Skills gain (# of Blunt Base Attack Skills) Offense Level. (same Skills don't count twice; max 3)\n\nWhen using a Skill to attack an enemy, if a different Skill was [Discard]ed, deal +(10 + (rank of the Discarded Skill x 5))% more Blunt damage. (if multiple were discarded, take the highest value; max 25%)
   PL: — opis] [Efekt wyłącznie dla Tożsamości na Przydziale #3]\n\nUmiejętności Uderzenia zyskują Poziom Ataku równy liczbie posiadanych podstawowych Umiejętności ataku Uderzenia (te same Umiejętności liczone raz; maks. 3).\n\nGdy przy ataku na wroga Umiejętnością odrzucono inną Umiejętność [Discard], zadaje +(10+Ranga odrzuconej Umiejętności x 5)% obrażeń Uderzenia (liczone wg najwyższej rangi; maks. 25%).
21. [Dar E.G.O [9201] — opis skrócony] 타격 스킬의 공격 레벨 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9201].simpleDesc[abilityID=9201].simpleDesc
   limit: do 120 znaków
   EN: Blunt Skills gain Offense Level
   PL: — opis skrócony] Wzrost Poziomu Ataku Umiejętności Uderzenia
22. [Dar E.G.O [9201] — opis skrócony] 타격 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9201].simpleDesc[abilityID=92011].simpleDesc
   limit: do 120 znaków
   EN: Deal more Blunt damage
   PL: Wzrost Obrażeń Uderzenia
23. [Dar E.G.O [9202] — nazwa] 포켓 암기 노트
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9202].name
   limit: do 40 znaków
   EN: Pocket Flashcards
   PL: — nazwa] Kieszonkowe Fiszki
24. [Dar E.G.O [9202] — opis] 타격 기본 공격 스킬로 합 승리 시, 대상 적에게 다음 턴에 방어 레벨 감소 2 부여 (인격 별로 턴 당 1회, 동일한 적에게 중첩 불가).\n- 디에치 협회 소속 인격은 참격, 관통 기본 공격 스킬에도 효과가 적용되고 방어 레벨 감소 1 추가로 부여\n\n디에치 협회 소속 인격이 버림 스킬을 사용하여 자신의 스킬을 버렸다면, 다음 턴 시작 시 버린 스킬의 등급만큼 공격 레벨 증가 얻음 (가장 높은 등급으로 계산, 최대 3).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9202].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When winning a Clash with a Blunt Base Attack Skill, inflict 2 Defense Level Down next turn against the target. (once per turn per Identity; effect cannot stack against the same enemy)\n- For Dieci Association Identities: above effect applies to Slash and Pierce Base Attack Skills as well; inflict 1 additional Defense Level Down\n\nIf a Dieci Association Identity Discarded their own Skill using a Discard Skill, gain (rank of the Discarded Skill) Offense Level Up at the next Turn Start. (if multiple are discarded, take the highest value; max 3)
   PL: — opis] Przy wygranej Starciu podstawową Umiejętnością ataku Uderzenia nakłada na cel 2 Spadku Poziomu Obrony na następną turę (1 raz na turę na Tożsamość; nie kumuluje się na tym samym wrogu).\n- Tożsamości Stowarzyszenia Dieci: efekt stosuje się również do podstawowych Umiejętności ataku Cięcia i Kłucia oraz nakłada dodatkowo 1 Spadek Poziomu Obrony\n\nJeżeli Tożsamość Stowarzyszenia Dieci odrzuciła własną Umiejętność Umiejętnością Odrzucenia, na początku następnej tury zyskuje Wzrost Poziomu Ataku równy Rangi odrzuconej Umiejętności (liczone wg najwyższej rangi; maks. 3).
25. [Dar E.G.O [9202] — opis skrócony] 다음 턴에 방어 레벨 감소 부여
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9202].simpleDesc[abilityID=9202].simpleDesc
   limit: do 120 znaków
   EN: Inflict Defense Level Down next turn
   PL: — opis skrócony] Nakłada Spadek Poziomu Obrony na następną turę
26. [Dar E.G.O [9202] — opis skrócony] 다음 턴에 버린 스킬의 등급만큼 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9202].simpleDesc[abilityID=92021].simpleDesc
   limit: do 120 znaków
   EN: Gain (rank of the Discarded Skill) Offense Level Up
   PL: — opis skrócony] Zyskuje Wzrost Poziomu Ataku równy Rangi odrzuconej Umiejętności
27. [Dar E.G.O [19202] — nazwa] 포켓 암기 노트+
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19202].name
   limit: do 40 znaków
   EN: Pocket Flashcards+
   PL: — nazwa] Kieszonkowe Fiszki+
28. [Dar E.G.O [19202] — opis] 타격 기본 공격 스킬로 합 승리 시, 대상 적에게 다음 턴에 방어 레벨 감소 2 부여 (인격 별로 턴 당 1회, 동일한 적에게 중첩 불가).\n- 디에치 협회 소속 인격은 참격, 관통 기본 공격 스킬에도 효과가 적용되고 방어 레벨 감소 1 추가로 부여\n\n디에치 협회 소속 인격이 버림 스킬을 사용하여 자신의 스킬을 버렸다면, 다음 턴 시작 시 <style="upgradeHighlight">(버린 스킬의 등급 + 1)</style>만큼 공격 레벨 증가 얻음 (가장 높은 등급으로 계산, 최대 <style="upgradeHighlight">4</style>).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19202].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n
   EN: When winning a Clash with a Blunt Base Attack Skill, inflict 2 Defense Level Down next turn against the target. (once per turn per Identity; effect cannot stack against the same enemy)\n- For Dieci Association Identities: above effect applies to Slash and Pierce Base Attack Skills as well; inflict 1 additional Defense Level Down\n\nIf a Dieci Association Identity Discarded their own Skill using a Discard Skill, gain <style="upgradeHighlight">(rank of the Discarded Skill + 1)</style> Offense Level Up at the next Turn Start. (if multiple are discarded, take the highest value; max <style="upgradeHighlight">4</style>)
   PL: — opis] Przy wygranej Starciu podstawową Umiejętnością ataku Uderzenia nakłada na cel 2 Spadku Poziomu Obrony na następną turę (1 raz na turę na Tożsamość; nie kumuluje się na tym samym wrogu).\n- Tożsamości Stowarzyszenia Dieci: efekt stosuje się również do podstawowych Umiejętności ataku Cięcia i Kłucia oraz nakłada dodatkowo 1 Spadek Poziomu Obrony\n\nJeżeli Tożsamość Stowarzyszenia Dieci odrzuciła własną Umiejętność Umiejętnością Odrzucenia, na początku następnej tury zyskuje Wzrost Poziomu Ataku równy (Ranga odrzuconej Umiejętności<style="upgradeHighlight"> + 1</style>) (liczone wg najwyższej rangi; maks. <style="upgradeHighlight">4</style>).
29. [Dar E.G.O [19202] — opis skrócony] 다음 턴에 방어 레벨 감소 부여
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19202].simpleDesc[abilityID=19202].simpleDesc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Dar E.G.O [19202] — opis skrócony] 다음 턴에 버린 스킬의 등급만큼 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=19202].simpleDesc[abilityID=192021].simpleDesc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
31. [Dar E.G.O [29202] — nazwa] 포켓 암기 노트++
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29202].name
   limit: do 40 znaków
   EN: Pocket Flashcards++
   PL: — nazwa] Kieszonkowe Fiszki++
32. [Dar E.G.O [29202] — opis] 타격 기본 공격 스킬로 합 승리 시, 대상 적에게 다음 턴에 방어 레벨 감소 2 부여 (인격 별로 턴 당 1회, 동일한 적에게 중첩 불가).\n- 디에치 협회 소속 인격은 참격, 관통 기본 공격 스킬에도 효과가 적용되고 방어 레벨 감소 1 추가로 부여\n\n디에치 협회 소속 인격이 버림 스킬을 사용하여 자신의 스킬을 버렸다면, 다음 턴 시작 시 <style="upgradeHighlight">(버린 스킬의 등급+2)</style>만큼 공격 레벨 증가 얻음 (가장 높은 등급으로 계산, 최대 <style="upgradeHighlight">5</style>).
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29202].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n
   EN: When winning a Clash with a Blunt Base Attack Skill, inflict 2 Defense Level Down next turn against the target. (once per turn per Identity; effect cannot stack against the same enemy)\n- For Dieci Association Identities: above effect applies to Slash and Pierce Base Attack Skills as well; inflict 1 additional Defense Level Down\n\nIf a Dieci Association Identity Discarded their own Skill using a Discard Skill, gain <style="upgradeHighlight">(rank of the Discarded Skill + 2)</style> Offense Level Up at the next Turn Start. (if multiple are discarded, take the highest value; max <style="upgradeHighlight">5</style>)
   PL: — opis] Przy wygranej Starciu podstawową Umiejętnością ataku Uderzenia nakłada na cel 2 Spadku Poziomu Obrony na następną turę (1 raz na turę na Tożsamość; nie kumuluje się na tym samym wrogu).\n- Tożsamości Stowarzyszenia Dieci: efekt stosuje się również do podstawowych Umiejętności ataku Cięcia i Kłucia oraz nakłada dodatkowo 1 Spadek Poziomu Obrony\n\nJeżeli Tożsamość Stowarzyszenia Dieci odrzuciła własną Umiejętność Umiejętnością Odrzucenia, na początku następnej tury zyskuje Wzrost Poziomu Ataku równy (Ranga odrzuconej Umiejętności<style="upgradeHighlight">+2</style>) (liczone wg najwyższej rangi; maks. <style="upgradeHighlight">5</style>).
33. [Dar E.G.O [29202] — opis skrócony] 다음 턴에 방어 레벨 감소 부여
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29202].simpleDesc[abilityID=29202].simpleDesc
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
34. [Dar E.G.O [29202] — opis skrócony] 다음 턴에 버린 스킬의 등급만큼 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=29202].simpleDesc[abilityID=292021].simpleDesc
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Dar E.G.O [9203] — nazwa] 차원지각변환체
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9203].name
   limit: do 50 znaków
   EN: Dimensional Perception Modifier
   PL: — nazwa] Wymiarowy Modyfikator Percepcji
36. [Dar E.G.O [9203] — opis] 타격 유형인 스킬 1, 스킬 2의 공격 레벨 +(코인 수-1) (최대 2)\n- 버림 효과가 있는 스킬일 경우 효과가 강화되어, 공격 레벨 +(코인 수) (최대 4)\n\n버림 스킬을 사용하여 자신의 스킬을 버렸다면, 다음 턴 시작 시 피해량 증가 1, 버린 스킬의 등급만큼 공격 레벨 증가 얻음 (인격 별로 턴 당 1회 적용되며 가장 높은 등급으로 계산, 최대 3).\n- 타격 유형 스킬을 버렸다면 효과가 강화되어, 타격 피해량 증가 1 추가로 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9203].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Blunt Attack Type Skill 1 & 2: Offense Level +(# of Coins - 1) (max 2)\n- Skills with Discard effects gain Offense Level +(# of Coins) instead (max 4)\n\nIf a unit used a Discard Skill to discard their Skill, gain 1 Damage Up and (rank of the Discarded Skill) Offense Level Up. (once per turn per Identity; if multiple were discarded, take the highest value; max 3)\n- If a Blunt Attack Type Skill was Discarded, gain 1 Blunt DMG Up as well
   PL: — opis] Umiejętności 1 i 2 typu Uderzenia: Poziom Ataku +(liczba monet-1) (maks. 2)\n- Umiejętności z efektem Odrzucenia: zamiast tego Poziom Ataku +(liczba monet) (maks. 4)\n\nGdy jednostka odrzuci własną Umiejętność Umiejętnością Odrzucenia, na początku następnej tury zyskuje 1 Wzrost Obrażeń i Wzrost Poziomu Ataku równy Rangi odrzuconej Umiejętności (1 raz na turę na Tożsamość; liczone wg najwyższej rangi; maks. 3).\n- Jeżeli odrzucono Umiejętność typu Uderzenia, dodatkowo zyskuje 1 Wzrost Obrażeń Uderzenia
37. [Dar E.G.O [9203] — opis skrócony] 공격 레벨 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9203].simpleDesc[abilityID=9203].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level
   PL: Wzrost Poziomu Ataku
38. [Dar E.G.O [9203] — opis skrócony] 피해량 증가, 공격 레벨 증가 얻음. 타격 스킬을 버렸다면 타격 피해량 증가 추가로 얻음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9203].simpleDesc[abilityID=92031].simpleDesc
   limit: do 130 znaków
   EN: Gain Damage Up and Offense Level Up. If a Blunt Skill was Discarded, gain Blunt DMG Up as well
   PL: — opis skrócony] Wzrost Obrażeń i Poziomu Ataku. Jeżeli odrzucono Umiejętność Uderzenia, dodatkowo Wzrost Obrażeń Uderzenia
39. [Dar E.G.O [9204] — nazwa] 앙갚음 장부
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].name
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: Księga Zemsty
40. [Dar E.G.O [9204] — opis] 타격 기본 공격 스킬의 합 위력 +2. 전투 시작 시, 자신을 제외하고 이번 턴에 타격 기본 공격 스킬을 사용하는 인격 수만큼 [AttackUp] 얻음 (최대 3).\n\n보유한 모든 기본 공격 스킬이 타격 유형인 아군이 턴 시작 시 [HitDamageUp] 2 얻음 (강화되거나 특수 발동하는 경우 제외).\n\n반격 스킬 사용 시 (강화 반격 제외), 최대 체력의 7.5%만큼 보호막을 얻고 피해량 +20%. 반격 스킬 사용 중 피격 시 피해로 흐트러지지 않음 (인격 별로 전투당 1회).\n\n중지 소속 인격이 턴 시작 시 [HitResultUp] 1, [Endurance] 2 얻음. 중지 소속 인격이 반격 스킬 사용 시, 위의 반격 스킬 강화 효과가 전투당 2회 발동하고 반격 스킬의 피해량이 +40%로 강화됨.
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [HitDamageUp], [HitResultUp], [Endurance]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [HitResultUp] = 타격 위력 증가 / Blunt Power Up; [Endurance] = 수비 위력 증가 / Defense Power Up
   EN: Blunt Base Attack Skills gain Clash Power +2. On Combat Start, gain [AttackUp] equal to the number of Identities who are using Blunt base Attack Skills this turn. (max 3)\n\nAllies with Blunt Attack Type for all of their base Attack Skills gain 2 [HitDamageUp] at Turn Start. (except for Empowered Skills or Skills that need unique conditionals)\n\nWhen using a Counter Skill(except Power Counters), gain 7.5% of this unit's max HP as Shield HP and deal +20% damage. Cannot be Staggered by damage when using a Counter Skill (once per Identity per Encounter)\n\nAt Turn Start, The Middle Identities gain 1 [HitResultUp] and 2 [Endurance]; when The Middle Identity uses a Counter Skill, the above Counter Skill enhancement activates twice per Encounter and deals +40% damage instead.
   PL: — opis] Umiejętności podstawowe ataku Uderzenia zyskują Moc Starcia +2. Na początku walki zyskuje [AttackUp] w liczbie równej liczbie Tożsamości używających Umiejętności podstawowych ataku Uderzenia w tej turze (maks. 3).\n\nSojusznicy, których wszystkie Umiejętności podstawowe ataku są typu Uderzenia, zyskują na początku tury 2 [HitDamageUp] (z pominięciem Umiejętności wzmocnionych lub wymagających specjalnych warunków).\n\nPrzy użyciu Umiejętności Kontry (z pominięciem Wzmocnionej Kontry) zyskuje Tarczę równą 7.5% Maks. HP i zadaje +20% obrażeń. Przy otrzymaniu obrażeń podczas używania Umiejętności Kontry nie ulega Oszołomieniu (1 raz na walkę na Tożsamość).\n\nTożsamości frakcji Środkowego zyskują na początku tury 1 [HitResultUp] i 2 [Endurance]. Przy użyciu Umiejętności Kontry przez Tożsamości frakcji Środkowego powyższy efekt wzmocnienia Kontry uruchamia się 2 razy na walkę, a obrażenia Kontry są wzmocnione do +40%.
41. [Dar E.G.O [9204] — opis skrócony] 합 위력, 공격 레벨 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].simpleDesc[abilityID=9204].simpleDesc
   limit: do 120 znaków
   EN: Gain Clash Power and Offense Level Up
   PL: — opis skrócony] Wzrost Mocy Starcia i Poziomu Ataku
42. [Dar E.G.O [9204] — opis skrócony] 타격 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].simpleDesc[abilityID=92041].simpleDesc
   limit: do 120 znaków
   EN: Gain Blunt DMG Up
   PL: Wzrost Obrażeń Uderzenia
43. [Dar E.G.O [9204] — opis skrócony] 반격 스킬 사용시 피해로 흐트러지지 않음
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].simpleDesc[abilityID=92042].simpleDesc
   limit: do 120 znaków
   EN: Cannot be Staggered from damage when counterattacking
   PL: — opis skrócony] Nie ulega Oszołomieniu od obrażeń przy użyciu Umiejętności Kontry
44. [Dar E.G.O [9204] — opis skrócony] 타격 위력 증가, 수비 위력 증가, 반격 피해량 증가
   źródło: EGOgift_MirrorDungeon.json :: dataList[id=9204].simpleDesc[abilityID=92042#2].simpleDesc
   limit: do 120 znaków
   EN: Gain Blunt DMG Up, Defense Power Up, and deal more damage with Counterattacks
   PL: — opis skrócony] Wzrost Mocy Uderzenia, Wzrost Mocy Obrony, Wzrost Obrażeń Kontry

## Dar E.G.O: EGOgift_MirrorDungeon_2
- plik gry: `EGOgift_MirrorDungeon_2.json`

45. [Dar E.G.O [9156] — nazwa] 만년 화롯불
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9156].name
   limit: do 40 znaków
   EN: Decamillennial Hearthflame
   PL: — nazwa] Ognisko 10 000 Lat
46. [Dar E.G.O [9156] — opis] 턴 종료시, [Combustion] 횟수를 3 이상 보유한 적이 [Combustion]을 1회 더 발동함 ([Combustion] 횟수 1 감소)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9156].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn End: enemies with 3+ [Combustion] Count activates [Combustion] one more time (reduce [Combustion] Count by 1)
   PL: — opis] Na koniec tury wrogowie z co najmniej 3 Licznikami [Combustion] wywołują [Combustion] 1 dodatkowy raz (Liczniki [Combustion] maleją o 1)
47. [Dar E.G.O [9158] — nazwa] 훔쳐온 불꽃
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].name
   limit: do 40 znaków
   EN: Purloined Flame
   PL: — nazwa] Ukradziony Płomień
48. [Dar E.G.O [9158] — opis] 턴 시작 시, [Combustion] 및 특수 화상을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n스킬(E.G.O 스킬 포함) 적중 시 대상의 [Combustion] 횟수가 3 이상이면, 대상의 [Combustion]을 1회 발동함. ([Combustion] 횟수 1 감소, 스킬당 1회 발동)\n\n턴 종료시, [Combustion] 횟수를 3 이상 보유한 적이 [Combustion]을 1회 더 발동함 ([Combustion] 횟수 1 감소)\n\n[Combustion] 상태인 적이 사망하였을 경우(환상체일 경우, 본체 사망 시), 남은 [Combustion] 위력 수치만큼을 다음 턴 시작 시 [Combustion] 위력 수치가 제일 적은 적 중 하나에게 부여.\n\n턴 시작 시 [Combustion] 상태인 적에게 이번 턴 동안 [AttackDown] 4 부여\n\n[Combustion]을 보유한 적이 사망하였을 경우, 다음 턴 시작시, [Combustion] 부여 스킬을 보유한 아군 (사망한 적의 [Combustion] 위력/15)명이 [AttackDmgUp] 2 얻음. (턴 당 1회 발동)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].desc
   limit: do 1240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [AttackDown], [AttackDmgUp]
   znaczenie tagów: [Combustion] = 화상 / Burn; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Combustion] or 'Unique Burn'. (except E.G.O Skills; except Backup Units)\n\nOn Hit with a Skill(including E.G.O Skills): if the target has 3+ [Combustion] Count, activate [Combustion] once on the target. (target loses 1 [Combustion] Count; activates once per Skill)\n\nTurn End: targets with 3+ [Combustion] Count activates [Combustion] one more time (target loses 1 [Combustion] Count)\n\nIf a target with [Combustion] is defeated(for Abnormalities, when the Core is defeated), inflict its remaining [Combustion] Potency to one of the enemies with the least [Combustion] Potency at the next Turn Start.\n\nTurn Start: for this turn, inflict 4 [AttackDown] to enemies with [Combustion]\n\nIf a target with [Combustion] is defeated, at the next Turn Start, (defeated enemy's [Combustion] Potency / 15) allies with Skills that inflict [Combustion] gain 2 [AttackDmgUp]. (once per turn)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające [Combustion] lub Szczególne Podpalenie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nPrzy trafieniu Umiejętnością (z wliczeniem Umiejętności E.G.O), jeżeli cel ma co najmniej 3 Liczniki [Combustion], wywołuje [Combustion] na celu 1 raz (Liczniki [Combustion] maleją o 1; wywoływane 1 raz na Umiejętność)\n\nNa koniec tury wrogowie z co najmniej 3 Licznikami [Combustion] wywołują [Combustion] 1 dodatkowy raz (Liczniki [Combustion] maleją o 1)\n\nGdy ginie wróg w stanie [Combustion] (w przypadku Anomalii — śmierć korpusu), na początku następnej tury nakłada Moc [Combustion] równą pozostałej Mocy [Combustion] na 1 wroga z najniższą Mocą [Combustion]\n\nNa początku tury nakłada 4 [AttackDown] na wrogów w stanie [Combustion] na czas tej tury\n\nGdy ginie wróg z [Combustion], na początku następnej tury (liczba pozostałej Mocy [Combustion] pokonanego wroga/15) sojuszników z Umiejętnościami nakładającymi [Combustion] zyskuje 2 [AttackDmgUp] (1 wywołanie na turę)
49. [Dar E.G.O [9158] — opis skrócony] [Combustion] 1회 발동
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].simpleDesc[abilityID=9158].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Activate [Combustion] once
   PL: — opis skrócony] Wywołuje [Combustion] 1 raz
50. [Dar E.G.O [9158] — opis skrócony] [Combustion] 1회 추가 발동
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].simpleDesc[abilityID=91581].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Activate [Combustion] 1 more time
   PL: — opis skrócony] Wywołuje [Combustion] 1 dodatkowy raz
51. [Dar E.G.O [9158] — opis skrócony] 사망한 적의 남은 화상 위력 수치만큼 [Combustion] 위력 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].simpleDesc[abilityID=91582].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Inflict [Combustion] Potency equal to (remaining [Combustion] Stack on defeated enemy)
   PL: — opis skrócony] Nakłada Moc [Combustion] równą pozostałej Mocy Podpalenia pokonanego wroga
52. [Dar E.G.O [9158] — opis skrócony] [AttackDown] 4 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].simpleDesc[abilityID=91583].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: Inflict 4 [AttackDown]
   PL: — opis skrócony] Nakłada 4 [AttackDown]
53. [Dar E.G.O [9158] — opis skrócony] [AttackDmgUp] 2 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9158].simpleDesc[abilityID=91583#2].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Gain 2 [AttackDmgUp]
   PL: — opis skrócony] Zyskuje 2 [AttackDmgUp]
54. [Dar E.G.O [9160] — nazwa] 찢어진 피주머니
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9160].name
   limit: do 40 znaków
   EN: Ruptured Blood Sac
   PL: — nazwa] Rozdarty Worek Krwi
55. [Dar E.G.O [9160] — opis] 아군이 합 승리 시, 적의 [Laceration]을 1회 발동시키고, [Laceration] 횟수 1 감소 (턴 당 3회 발동)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9160].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On ally Clash Win: activate the enemy's [Laceration] once and reduce [Laceration] Count by 1 (3 times per turn)
   PL: — opis] Przy wygranej Starciu sojusznika wywołuje [Laceration] wroga 1 raz, a Liczniki [Laceration] maleją o 1 (3 razy na turę)
56. [Dar E.G.O [9160] — opis skrócony] 출혈 1회 발동 (출혈 횟수 1 감소)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9160].simpleDesc[abilityID=9160].simpleDesc
   limit: do 120 znaków
   EN: Activate Bleed once (reduce Bleed Count by 1)
   PL: — opis skrócony] Wywołuje Krwawienie 1 raz (Liczniki Krwawienia maleją o 1)
57. [Dar E.G.O [9162] — nazwa] 출혈성 쇼크
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].name
   limit: do 40 znaków
   EN: Hemorrhagic Shock
   PL: — nazwa] Wstrząs Krwotoczny
58. [Dar E.G.O [9162] — opis] 턴 시작 시, [Laceration] 및 특수 출혈을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n아군이 합 승리 시, 적의 [Laceration]을 1회 발동시키고, [Laceration] 횟수 1 감소 (아군 1명당 턴 당 1회)\n\n적이 [Laceration] 피해로 흐트러질 수 있으며, 적이 합 진행 중 [Laceration] 피해로 흐트러지면, 적의 남은 코인 수만큼 [Laceration]을 발동시키고, 발동한 횟수만큼 [Laceration] 횟수 감소 \n\n모든 적이 [Laceration]이 부여되어 있으면 방어 레벨 2 감소. 턴 종료 시 ([Laceration]이 발동한 횟수 X 2)만큼 다음 턴에 [DefenseDown]를 얻음 (최대 20)\n\n스킬 효과로 [Laceration] 위력 또는 특수 출혈을 부여할 때마다 대상에게 [Laceration] 위력 3, [Laceration] 횟수 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Laceration] or 'Unique Bleed'. (except E.G.O Skills; except Backup Units)\n\nOn ally Clash Win: activate the enemy's [Laceration] once and reduce [Laceration] Count by 1 (once per turn for each ally)\n\nEnemies become Staggerable by [Laceration] Damage; if an enemy gets Staggered due to [Laceration] damage mid-Clash, activate [Laceration] (# of remaining enemy Coins) times and reduce [Laceration] Count by (# of [Laceration] activations)\n\nIf all enemies have [Laceration], they lose 2 Defense Levels. At Turn End, inflict (# of [Laceration] activations x 2) [DefenseDown] next turn (max 20)\n\nWhen inflicting [Laceration] Potency or 'Unique Bleed' with Skill effects, inflict 3 [Laceration] Potency and +1 [Laceration] Count on the target
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające [Laceration] lub Szczególne Krwawienie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nPrzy wygranej Starciu sojusznika wywołuje [Laceration] wroga 1 raz, a Liczniki [Laceration] maleją o 1 (1 raz na turę na sojusznika)\n\nWrogowie mogą ulegać Oszołomieniu od obrażeń [Laceration]; jeżeli wróg ulega Oszołomieniu od obrażeń [Laceration] w trakcie Starcia, wywołuje [Laceration] tyle razy, ile wynosi liczba pozostałych monet wroga, a Liczniki [Laceration] maleją o liczbę wywołań\n\nJeżeli wszyscy wrogowie mają nałożone [Laceration], ich Poziom Obrony maleje o 2. Na koniec tury zyskują (liczba wywołanych [Laceration] x 2) [DefenseDown] na następną turę (maks. 20)\n\nZa każde nałożenie Mocy [Laceration] lub Szczególnego Krwawienia efektem Umiejętności nakłada na cel 3 Moc [Laceration] i 1 Licznik [Laceration]
59. [Dar E.G.O [9162] — opis skrócony] 합 승리 시, 적의 출혈 1회 발동 (출혈 횟수 1 감소)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].simpleDesc[abilityID=9162].simpleDesc
   limit: do 120 znaków
   EN: On Clash Win, activate Bleed on the target once (reduce Bleed Count by 1)
   PL: — opis skrócony] Przy wygranej Starciu wywołuje Krwawienie wroga 1 raz (Liczniki Krwawienia maleją o 1)
60. [Dar E.G.O [9162] — opis skrócony] 합 종료 후 남은 코인 수만큼 적의 출혈 발동 (발동한 횟수 만큼 출혈 횟수 감소)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].simpleDesc[abilityID=91621].simpleDesc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: After Clashing, activate the enemy's [Laceration] (# of remaining Coins on self) times and reduce [Laceration] Count by (# of [Laceration] activations)
   PL: — opis skrócony] Po zakończeniu Starcia wywołuje Krwawienie wroga tyle razy, ile wynosi liczba pozostałych monet (Liczniki Krwawienia maleją o liczbę wywołań)
61. [Dar E.G.O [9162] — opis skrócony] (출혈이 발동한 횟수 X 2)만큼 방어 레벨 감소 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].simpleDesc[abilityID=91622].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Inflict (# of [Laceration] activations x 2) [DefenseDown] (max 20)
   PL: — opis skrócony] Zyskuje (liczba wywołanych Krwawień x 2) Spadek Poziomu Obrony
62. [Dar E.G.O [9162] — opis skrócony] 출혈 위력 3, 출혈 횟수 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9162].simpleDesc[abilityID=91623].simpleDesc
   limit: do 120 znaków
   EN: Inflict 3 Bleed Potency and +1 Bleed Count
   PL: — opis skrócony] Nakłada 3 Moc Krwawienia i 1 Licznik Krwawienia
63. [Dar E.G.O [9163] — nazwa] 보석 진동자
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9163].name
   limit: do 40 znaków
   EN: Gemstone Oscillator
   PL: — nazwa] Oscylator z Klejnotu
64. [Dar E.G.O [9163] — opis] [Vibration] 횟수를 소모한 스킬로 합 승리시, 대상에게 [Vibration]이 없다면 대상의 [Vibration] 횟수 2 증가.\n\n해당 공격 스킬을 포함하여 나태 공명 3 이상이면, 대신 대상의 [Vibration] 횟수 3 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9163].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When winning a Clash with a Skill that consumed [Vibration] Count: if the target does not have [Vibration], inflict +2 [Vibration] Count\n\nAt 3+ Sloth Reson. including this Skill, inflict +3 [Vibration] Count instead
   PL: — opis] Przy wygranej Starciu Umiejętnością zużywającą Liczniki [Vibration], jeżeli cel nie ma [Vibration], zwiększa Liczniki [Vibration] celu o 2.\n\nPrzy Rezonansie Lenistwa 3 lub wyższym (z wliczeniem tej Umiejętności), zamiast tego zwiększa Liczniki [Vibration] celu o 3
65. [Dar E.G.O [9163] — opis skrócony] 진동 횟수를 소모하는 스킬로 합 승리 시, 대상의 [Vibration] 횟수 2 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9163].simpleDesc[abilityID=9163].simpleDesc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When winning a Clash with a Skill that consumed [Vibration] Count, inflict +2 [Vibration] Count
   PL: — opis skrócony] Przy wygranej Starciu Umiejętnością zużywającą Liczniki Wstrząsu, zwiększa Liczniki [Vibration] celu o 2
66. [Dar E.G.O [9163] — opis skrócony] 진동 횟수를 소모하는 스킬 포함 나태 공명 3 이상으로 합 승리 시, 대상의 [Vibration] 횟수 3 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9163].simpleDesc[abilityID=91631].simpleDesc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When winning a Clash with a Skill that consumed [Vibration] Count and is a part of a 3+ Sloth Reson.: inflict +3 [Vibration] Count
   PL: — opis skrócony] Przy wygranej Starciu Umiejętnością zużywającą Liczniki Wstrząsu i Rezonansie Lenistwa 3 lub wyższym, zwiększa Liczniki [Vibration] celu o 3
67. [Dar E.G.O [9164] — nazwa] 흔들리는 술통
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9164].name
   limit: do 40 znaków
   EN: Wobbling Keg
   PL: — nazwa] Chwiejna Beczka
68. [Dar E.G.O [9164] — opis] 턴 시작 시, 자신의 [Vibration] 횟수가 8 이상이면 합 위력 +1\n\n자신의 [Vibration] 횟수를 소모하는 스킬로 적을 처치하거나 흐트러짐 상태로 만들었으면, (소모한 [Vibration] 횟수 / 4)만큼 자신의 [Vibration] 횟수 증가 (스킬당 1회)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9164].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Turn Start: at 8+ [Vibration] Count, Clash Power +1\n\nWhen defeating or Staggering an enemy with a Skill that consumes [Vibration] Count on self: gain +([Vibration] Count consumed / 4) [Vibration] Count (once per Skill)
   PL: — opis] Na początku tury przy co najmniej 8 Licznikach [Vibration] Moc Starcia +1\n\nGdy pokona wroga lub oszołomi go Umiejętnością zużywającą własne Liczniki [Vibration], zwiększa własne Liczniki [Vibration] o (zużyte Liczniki [Vibration]/4) (1 raz na Umiejętność)
69. [Dar E.G.O [9164] — opis skrócony] 자신의 진동 횟수가 8 이상이면, 합 위력 +1
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9164].simpleDesc[abilityID=9164].simpleDesc
   limit: do 120 znaków
   EN: At 8+ Tremor Count, Clash Power +1
   PL: — opis skrócony] Przy co najmniej 8 własnych Licznikach Wstrząsu Moc Starcia +1
70. [Dar E.G.O [9164] — opis skrócony] 진동 횟수를 소모하는 스킬로 적을 처치하거나 흐트러트리면, 자신의 진동 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9164].simpleDesc[abilityID=91641].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When winning a Clash with a Skill that consumes [Vibration] Count: gain [Vibration] Count
   PL: — opis skrócony] Gdy pokona wroga lub oszołomi go Umiejętnością zużywającą Liczniki Wstrząsu, zwiększa Liczniki Wstrząsu
71. [Dar E.G.O [9166] — nazwa] 진원점
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9166].name
   limit: do 40 znaków
   EN: Epicenter
   PL: — nazwa] Epicentrum
72. [Dar E.G.O [9166] — opis] 턴 시작 시, [Vibration] 위력 또는 [Vibration] 횟수를 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외. 인격이 스스로 [Vibration] 횟수를 얻는 경우에는 발동 x)\n\n자신의 [Vibration] 횟수를 소모한 스킬로 합 승리시, 대상에게 [Vibration] 이 없다면 대상의 [Vibration] 횟수 3 증가\n\n턴 시작 시 합 위력이 (자신의 [Vibration] 횟수/5)만큼 증가. (최대 3)\n\n자신의 [Vibration] 횟수를 소모하는 스킬을 사용했을 때, 적 처치 혹은 흐트러짐 상태로 만들경우 (소모한 [Vibration] 횟수 / 2)만큼 자신의 [Vibration] 횟수 증가  (스킬당 1회)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9166].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency or Count. (except E.G.O Skills; except Backup Units)\n(If an Identity only has Attack Skills that gain [Vibration] Count on self, this E.G.O Gift does not activate for them)\n\nWhen winning a Clash with a Skill that consumed [Vibration] Count on self: if the target does not have [Vibration], inflict +3 [Vibration] Count\n\nTurn Start: gain Clash Power +([Vibration] Count on self / 5) (max 3)\n\nWhen using a Skill that consumes [Vibration] Count on self: if the target is defeated or Staggered, gain +([Vibration] Count consumed / 2) [Vibration] Count (once per Skill)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration] lub Liczniki [Vibration], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych; nie uruchamia się dla Tożsamości zyskujących same Liczniki [Vibration])\n\nPrzy wygranej Starciu Umiejętnością zużywającą własne Liczniki [Vibration], jeżeli cel nie ma [Vibration], zwiększa Liczniki [Vibration] celu o 3\n\nNa początku tury Moc Starcia rośnie o (własne Liczniki [Vibration]/5) (maks. 3)\n\nPrzy użyciu Umiejętności zużywającej własne Liczniki [Vibration], gdy pokona wroga lub oszołomi go, zwiększa własne Liczniki [Vibration] o (zużyte Liczniki [Vibration]/2) (1 raz na Umiejętność)
73. [Dar E.G.O [9166] — opis skrócony] 자신의 [Vibration] 횟수를 소모한 스킬로 합 승리시, 대상에게 [Vibration] 이 없다면 대상의 [Vibration] 횟수 3 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9166].simpleDesc[abilityID=9166].simpleDesc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When winning a Clash with a Skill that consumed [Vibration] Count on self: if the target does not have [Vibration], inflict +3 [Vibration] Count
   PL: — opis skrócony] Przy wygranej Starciu Umiejętnością zużywającą własne Liczniki [Vibration], jeżeli cel nie ma [Vibration], zwiększa Liczniki [Vibration] celu o 3
74. [Dar E.G.O [9166] — opis skrócony] 턴 시작 시 합 위력이 (자신의 [Vibration] 횟수/5)만큼 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9166].simpleDesc[abilityID=91661].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Turn Start: gain ([Vibration] Count on self / 5) Clash Power
   PL: — opis skrócony] Na początku tury Moc Starcia rośnie o (własne Liczniki [Vibration]/5)
75. [Dar E.G.O [9166] — opis skrócony] 진동 횟수를 소모하는 스킬로 적을 처치하거나 흐트러트리면, 자신의 진동 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9166].simpleDesc[abilityID=91662].simpleDesc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Dar E.G.O [9167] — nazwa] 무진팔방종
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].name
   limit: do 40 znaków
   EN: Omnivibro-octovecti-bell
   PL: — nazwa] Dzwon Ośmiu Kierunków
77. [Dar E.G.O [9167] — opis] 턴 시작 시, [Vibration] 위력, [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외. 인격이 스스로 [Vibration] 횟수를 얻는 경우에는 발동 x)\n\n[Vibration] 위력 또는 [Vibration] 횟수를 부여하거나 자신의 [Vibration] 횟수를 소모하는 스킬로 합 승리 시 남은 코인만큼 대상에게 [Vibration] 위력 부여. 자신의 진동 횟수 증가 (스킬당 자신의 진동 횟수 최대 3 증가). 대상에게 [Vibration]이 없으면, 대상의 [Vibration] 횟수 3 증가.\n\n턴 시작 시 [ParryingResultUp]를 1 + (자신의 [Vibration] 횟수/5)만큼 얻음. (최대 3)\n\n자신의 [Vibration] 횟수를 소모하는 스킬을 사용했을 때, 적 처치 혹은 흐트러짐 상태로 만들경우 (소모한 [Vibration] 횟수 / 2)만큼 자신의 [Vibration] 횟수 증가 (스킬당 1회)\n\n스킬의 피해량 +(자신이 소모한 [Vibration] 횟수 + 적이 보유한 [Vibration] 위력 + 5)% (E.G.O 스킬 제외, 최대 50%)\n대상에게 [VibrationNesting]이 있을 때, 그 대상에게 중첩되지 않은 유형의 [Vibration]으로 [Switch_Vibration], [FusionVibration]을 사용하면, 턴 종료 시 대상이 보유한 [VibrationNesting]을 다음 턴까지 연장함
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].desc
   limit: do 1640 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [ParryingResultUp], [VibrationNesting], [Switch_Vibration], [FusionVibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [VibrationNesting] = 진동 - 중첩 / Tremor - Superposition; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency, Count, or 'Unique Tremor'. (except E.G.O Skills; except Backup Units)\n(If an Identity only has Attack Skills that gain [Vibration] Count on self, this E.G.O Gift does not activate for them)\n\nWhen winning a Clash with a Skill that inflicts [Vibration] Potency or Count, or consumes [Vibration] Count on self: inflict (# of remaining Coins) [Vibration] Potency against the target and gain (# of remaining Coins) Tremor Count (max +3 Tremor Count gained per Skill). If the target does not have [Vibration], inflict +3 [Vibration] Count\n\nTurn Start: gain (1 + ([Vibration] Count on self / 5)) [ParryingResultUp]. (max 3)\n\nWhen using a Skill that consumes [Vibration] Count on self: when defeating or Staggering a target, gain ([Vibration] Count consumed / 2) [Vibration] Count (once per Skill)\n\nSkills deal +([Vibration] consumed on self + [Vibration] Potency on the enemy + 5)% damage (except E.G.O Skills; max 50%)\nWhen the target has [VibrationNesting], when triggering either [Switch_Vibration] or [FusionVibration] against the enemy with a type of [Vibration] they don't have in their [VibrationNesting], extend the [VibrationNesting] on target at Turn End to the next turn
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych; nie uruchamia się dla Tożsamości zyskujących same Liczniki [Vibration])\n\nPrzy wygranej Starciu Umiejętnością nakładającą Moc [Vibration] lub Liczniki [Vibration] albo zużywającą własne Liczniki [Vibration] nakłada na cel Moc [Vibration] równą pozostałym monetom; zwiększa własne Liczniki Wstrząsu (maks. +3 Liczników Wstrząsu na Umiejętność). Jeżeli cel nie ma [Vibration], zwiększa Liczniki [Vibration] celu o 3.\n\nNa początku tury zyskuje 1 [ParryingResultUp] + (własne Liczniki [Vibration]/5) (maks. 3)\n\nPrzy użyciu Umiejętności zużywającej własne Liczniki [Vibration], gdy pokona wroga lub oszołomi go, zwiększa własne Liczniki [Vibration] o (zużyte Liczniki [Vibration]/2) (1 raz na Umiejętność)\n\nUmiejętność zadaje +(zużyte własne Liczniki [Vibration] + Moc [Vibration] wroga + 5)% obrażeń (poza Umiejętnościami E.G.O; maks. 50%)\nGdy cel ma [VibrationNesting] i użyto [Switch_Vibration] lub [FusionVibration] typu [Vibration] nienakładającego się z typem celu, na koniec tury przedłuża [VibrationNesting] celu na następną turę
78. [Dar E.G.O [9167] — opis skrócony] 합 승리 시, 남은 코인만큼 진동 부여. 대상에게 [Vibration]이 없으면, 진동 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].simpleDesc[abilityID=9167].simpleDesc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: On Clash Win, inflict Tremor equal to the # of remaining Coins. If the target does not have [Vibration], inflict Tremor Count
   PL: — opis skrócony] Przy wygranej Starciu nakłada Wstrząs równy pozostałym monetom. Jeżeli cel nie ma [Vibration], zwiększa Liczniki Wstrząsu
79. [Dar E.G.O [9167] — opis skrócony] 턴 시작 시 합 위력 증가를 자신의 진동 횟수에 비례하여 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].simpleDesc[abilityID=91671].simpleDesc
   limit: do 120 znaków
   EN: Turm Start: gain Clash Power Up based on Tremor Count on self
   PL: — opis skrócony] Na początku tury zyskuje Wzrost Mocy Starcia proporcjonalny do Liczników Wstrząsu
80. [Dar E.G.O [9167] — opis skrócony] 진동 횟수를 소모하는 스킬로 적을 처치하거나 흐트러트리면, 자신의 진동 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].simpleDesc[abilityID=91672].simpleDesc
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Dar E.G.O [9167] — opis skrócony] 자신의 진동 횟수를 소모하는 스킬의 피해량 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].simpleDesc[abilityID=91673].simpleDesc
   limit: do 120 znaków
   EN: Skills that consume [Tremor] Count deal more damage
   PL: — opis skrócony] Umiejętności zużywające własne Liczniki Wstrząsu zadają więcej obrażeń
82. [Dar E.G.O [9167] — opis skrócony] 턴 종료 시 대상이 보유한 진동 - 중첩을 다음 턴까지 연장함
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9167].simpleDesc[abilityID=91674].simpleDesc
   limit: do 120 znaków
   EN: Extends the Tremor - Superposition on target at Turn End until next turn
   PL: — opis skrócony] Na koniec tury przedłuża Wstrząs - Superpozycja celu na następną turę
83. [Dar E.G.O [9168] — nazwa] 종말의 파편
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9168].name
   limit: do 40 znaków
   EN: Shard of Apocalypse
   PL: — nazwa] Odłamek Apokalipsy
84. [Dar E.G.O [9168] — opis] 대상의 [Burst] 위력이 15 미만이면, [Burst] 위력 부여 시 추가 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9168].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If the target has less than 15 [Burst] Potency, inflict 1 additional Potency when inflicting [Burst] Potency
   PL: — opis] Jeżeli cel ma Moc [Burst] niższą niż 15, przy nakładaniu Mocy [Burst] nakłada dodatkowo 1 Moc [Burst]
85. [Dar E.G.O [9168] — opis skrócony] [Burst] 위력 부여 시 추가 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9168].simpleDesc[abilityID=9168].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Inflict 1 additional [Burst] Potency
   PL: — opis skrócony] Przy nakładaniu Mocy [Burst] nakłada dodatkowo 1 Moc [Burst]
86. [Dar E.G.O [9170] — nazwa] 기괴한 석상
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9170].name
   limit: do 40 znaków
   EN: Eerie Effigy
   PL: — nazwa] Dziwaczny Posąg
87. [Dar E.G.O [9170] — opis] 턴 시작 시, [Burst] 위력 또는 [Burst] 횟수를 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Burst] 효과가 적이 보유한 보호막에 입히는 피해량+100%\n대상의 [Burst] 위력이 15 미만이면, [Burst] 위력 부여 시 추가 2 부여\n\n스킬 효과로 인해 [Burst]을 부여하지 못하는 경우 더하기 코인 위력 + 1\n- 빼기 코인 스킬일 경우, 더하기 코인 위력 대신 기본 위력 +(4/코인 수) (최소 1, 소수점 버림)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9170].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Burst] Potency or Count. (except E.G.O Skills; except Backup Units)\n\n[Burst] effects deal +100% damage against enemy Shields\nIf the target has less than 15 [Burst] Potency, inflict 2 more Potency when inflicting [Burst] Potency\n\nIf [Burst] cannot be applied due to Skill effects, gain Plus Coin Power +1 instead\n- Minus Coin Skills: Instead of gaining Plus Coin Power, gain Base Power +(4 / # of Coins) (min 1; rounded down)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Burst] lub Liczniki [Burst], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nEfekty [Burst] zadają +100% obrażeń Tarczom wroga\nJeżeli cel ma Moc [Burst] niższą niż 15, przy nakładaniu Mocy [Burst] nakłada dodatkowo 2 Moc [Burst]\n\nGdy Umiejętność nie może nałożyć [Burst] z powodu efektów Umiejętności, zamiast tego zyskuje Moc Monety Plus +1\n- Umiejętności z monetą Minus: zamiast Mocy Monety Plus zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)
88. [Dar E.G.O [9170] — opis skrócony] 파열 효과가 보호막에 입히는 피해량 +100%
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9170].simpleDesc[abilityID=9170].simpleDesc
   limit: do 120 znaków
   EN: Rupture effects deal +100% damage against Shields
   PL: — opis skrócony] Efekty Rozdarcia zadają +100% obrażeń Tarczom
89. [Dar E.G.O [9170] — opis skrócony] [Burst] 위력 부여 시 추가 2 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9170].simpleDesc[abilityID=91701].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Inflict 2 additional [Burst] Potency
   PL: — opis skrócony] Przy nakładaniu Mocy [Burst] nakłada dodatkowo 2 Moc [Burst]
90. [Dar E.G.O [9170] — opis skrócony] 스킬 효과로 인해 [Burst]을 부여하지 못하는 경우 코인/기본 위력 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9170].simpleDesc[abilityID=91702].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: If [Burst] cannot be applied due to Skill effects, gain Coin/Base Power instead
   PL: — opis skrócony] Gdy [Burst] nie może być nałożony z powodu efektów Umiejętności, zyskuje Moc Monet/Bazową
91. [Dar E.G.O [9171] — nazwa] 파탄
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].name
   limit: do 40 znaków
   EN: Ruin
   PL: Ruina
92. [Dar E.G.O [9171] — opis] 턴 시작 시, [Burst] 위력, [Burst] 횟수를 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Burst] 효과가 적이 보유한 보호막에 입히는 피해량 +150%\n\n턴 시작 시, [Burst] 상태인 적 또는 부위의 공격 레벨과 방어 레벨이 (3 + [Burst] 위력/2) 만큼 감소. (최대 6)\n\n스킬 효과로 [Burst] 위력, [Burst] 횟수를 부여할 때마다 대상에게 [Burst] 위력 2, [Burst] 횟수 1 부여. 대상의 [Burst] 위력이 15 미만이면, [Burst] 위력 부여 시 추가 2 부여.\n\n[Burst] 위력, 횟수 또는 특수 파열을 부여하는 더하기 코인 스킬의 코인 위력 +1\n[Burst] 위력, 횟수 또는 특수 파열을 부여하는 빼기 코인 스킬의 기본 위력 + (4/코인 수) (최소 1. 소수점 버림)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].desc
   limit: do 1000 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Burst] Potency or Count. (except E.G.O Skills; except Backup Units)\n\n[Burst] effects deal +150% damage against enemy Shield\n\nTurn Start: enemies or Parts with [Burst] lose (3 + ([Burst] Potency / 2)) Offense Level and Defense Level. (max 6)\n\nWhen inflicting [Burst] Potency or Count with Skill effects, inflict 2 [Burst] Potency and +1 [Burst] Count against the target. If the target has less than 15 [Burst] Potency, inflict 2 additional [Burst] Potency.\n\nCoin Power +1 for Plus Coin Skills that inflict [Burst] Potency, Count, or 'Unique Rupture'\nBase Power +(4 / # of Coins) (min. 1; rounded down) for Minus Coin Skills that inflict [Burst] Potency, Count, or 'Unique Rupture'
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Burst] lub Liczniki [Burst], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nEfekty [Burst] zadają +150% obrażeń Tarczom wroga\n\nNa początku tury Poziom Ataku i Poziom Obrony wrogów lub Partii w stanie [Burst] maleje o (3 + Moc [Burst]/2) (maks. 6)\n\nZa każde nałożenie Mocy [Burst] lub Liczników [Burst] efektem Umiejętności nakłada na cel 2 Moc [Burst] i 1 Licznik [Burst]. Jeżeli cel ma Moc [Burst] niższą niż 15, przy nakładaniu Mocy [Burst] nakłada dodatkowo 2 Moc [Burst].\n\nUmiejętności monety Plus nakładające Moc [Burst], Liczniki [Burst] lub Szczególne Rozdarcie zyskują Moc Monet +1\nUmiejętności monety Minus nakładające Moc [Burst], Liczniki [Burst] lub Szczególne Rozdarcie zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)
93. [Dar E.G.O [9171] — opis skrócony] [Burst] 효과가 보호막에 입히는 피해량 +150%
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].simpleDesc[abilityID=9171].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: [Burst] effects deal +150% damage against Shields
   PL: — opis skrócony] Efekty [Burst] zadają +150% obrażeń Tarczom
94. [Dar E.G.O [9171] — opis skrócony] [Burst]이 부여된 적의 공격 레벨과 방어 레벨 감소
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].simpleDesc[abilityID=91711].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Enemies with [Burst] lose Offense and Defense Levels
   PL: — opis skrócony] Wrogowie z nałożonym [Burst] mają obniżony Poziom Ataku i Obrony
95. [Dar E.G.O [9171] — opis skrócony] 스킬 효과로 [Burst] 위력을 부여할 때마다 대상에게 [Burst] 위력 2, [Burst] 횟수 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].simpleDesc[abilityID=91712].simpleDesc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: When inflicting [Burst] Potency with Skill effects, Inflict 2 [Burst] Potency and +1 [Burst] Count on target
   PL: — opis skrócony] Za każde nałożenie Mocy [Burst] efektem Umiejętności nakłada na cel 2 Moc [Burst] i 1 Licznik [Burst]
96. [Dar E.G.O [9171] — opis skrócony] 코인 위력 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9171].simpleDesc[abilityID=91713].simpleDesc
   limit: do 120 znaków
   EN: Gain Coin Power
   PL: — opis skrócony] Zyskuje Moc Monet
97. [Dar E.G.O [9172] — nazwa] 칸타빌레
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9172].name
   limit: do 40 znaków
   EN: Cantabile
   PL: — nazwa] Cantabile
98. [Dar E.G.O [9172] — opis] 기본 공격 스킬 사용시, 적이 [Sinking] 위력이 5 이상이면, 대상의 ([Sinking] 위력 / 10)만큼 자신의 정신력 회복 (최대 3)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9172].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: When using base Attack Skills, if the target has 5+ [Sinking] Potency, heal ([Sinking] Potency on the target / 10) SP on self (max 3)
   PL: — opis] Przy użyciu Umiejętności podstawowej ataku, jeżeli wróg ma co najmniej 5 Mocy [Sinking], odzyskuje Poczytalność równą (Moc [Sinking] celu/10) (maks. 3)
99. [Dar E.G.O [9172] — opis skrócony] 대상의 침잠에 비례하여 정신력 회복
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9172].simpleDesc[abilityID=9172].simpleDesc
   limit: do 120 znaków
   EN: Heal SP based on Sinking on the target
   PL: — opis skrócony] Odzyskuje Poczytalność proporcjonalnie do Zatonięcia celu
100. [Dar E.G.O [9173] — nazwa] 빛바랜 외투
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9173].name
   limit: do 40 znaków
   EN: Faded Overcoat
   PL: — nazwa] Wyblakły Płaszcz
101. [Dar E.G.O [9173] — opis] 턴 종료 시 정신력이 -45인 적이 3명 이상이면, 다음 턴에 모든 아군이 [AttackUp] 2 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9173].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn End: if there are 3+ enemies with -45 SP, all allies gain 2 [AttackUp] next turn
   PL: — opis] Na koniec tury przy 3+ wrogach z Poczytalnością -45 sojusznicy zyskują 2 [AttackUp] na następną turę
102. [Dar E.G.O [9173] — opis skrócony] 모든 아군이 [AttackUp] 2 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9173].simpleDesc[abilityID=9173].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: All allies gain 2 [AttackUp]
   PL: — opis skrócony] Wszyscy sojusznicy zyskują 2 [AttackUp]
103. [Dar E.G.O [9175] — nazwa] 서지 글로브
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9175].name
   limit: do 40 znaków
   EN: Surging Globe
   PL: — nazwa] Falująca Kula
104. [Dar E.G.O [9175] — opis] 턴 시작 시, [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n기본 공격 스킬 사용시, 적이 [Sinking] 위력이 5 이상이면, 대상의 ([Sinking] 위력 / 10)만큼 자신의 정신력 회복 (최대 5)\n\n턴 종료 시 정신력이 -45인 적의 수만큼 다음 턴에 모든 아군이 [AttackUp] 얻음 (최대 3)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9175].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [AttackUp]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Sinking] Potency, Count, or 'Unique Sinking'. (except E.G.O Skills; except Backup Units)\n\nWhen using a base Attack Skill, if the enemy has 5+ [Sinking] Potency, heal ([Sinking] Potency on the target / 10) SP on self (max 5)\n\nTurn End: next turn, all allies gain [AttackUp] equal to the number of enemies with -45 SP (max 3)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nPrzy użyciu Umiejętności podstawowej ataku, jeżeli wróg ma co najmniej 5 Mocy [Sinking], odzyskuje Poczytalność równą (Moc [Sinking] celu/10) (maks. 5)\n\nNa koniec tury wszyscy sojusznicy zyskują [AttackUp] w liczbie równej liczbie wrogów z Poczytalnością -45 (maks. 3)
105. [Dar E.G.O [9175] — opis skrócony] 대상의 침잠에 비례하여 정신력 회복
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9175].simpleDesc[abilityID=9175].simpleDesc
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Dar E.G.O [9175] — opis skrócony] 정신력이 -45인 적의 수만큼 모든 아군이 [AttackUp] 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9175].simpleDesc[abilityID=91751].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: All allies gain [AttackUp] equal to the number of enemies with -45 SP (max 3)
   PL: — opis skrócony] Wszyscy sojusznicy zyskują [AttackUp] w liczbie równej liczbie wrogów z Poczytalnością -45
107. [Dar E.G.O [9176] — nazwa] 덮칠 파도
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].name
   limit: do 40 znaków
   EN: Impending Wave
   PL: — nazwa] Nadchodząca Fala
108. [Dar E.G.O [9176] — opis] 턴 시작 시, [Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n턴 시작시, 무작위 적 하나에게 [WaveSinking] 1 부여\n\n[WaveSinking]를 보유한 적 사망 시, 대상의 [WaveSinking] 수치만큼 [WaveSinking] 수치가 최대치가 아닌 가장 높은 적에게 다음 턴 시작 시 [WaveSinking] 부여.\n\n[Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하는 스킬을 사용하여 적에게 적중 시 체력 피해를 입혔다면, 턴 종료 시 대상에게 [Sinking] 위력 4, [Sinking] 횟수 3 부여 (적 1명 당 턴 당 1회 발동)\n우울 또는 색욕 완전 공명을 발동하였다면, 전투 시작 시, 모든 적 (환상체일 경우, 무작위 부위 하나)에게 [Sinking] 위력 3, [Sinking] 횟수 3 부여.\n\n기본 공격 스킬 공격 종료 시, 적이 [Sinking] 위력이 10 이상이면, 대상의 ([Sinking] 위력 / 10)만큼 자신의 정신력 회복 (최대 5), 대상에게 [DefenseDown] 부여 (최대 5, 적 1명당 턴 당 1회 발동)\n\n턴 종료 시 정신력이 -45거나, 정신력이 없는 적의 수만큼 다음 턴에 모든 아군이 [AttackUp] 얻음 (최대 6)\n\n[Sinking] 위력, 횟수 또는 특수 침잠을 부여하는 더하기 코인 스킬의 코인 위력 +1\n[Sinking] 위력, 횟수 또는 특수 침잠을 부여하는 빼기 코인 스킬의 기본 위력 + (4/코인 수) (최소 1. 소수점 버림)\n\n[Sinking] 위력, [Sinking] 횟수 또는 특수 침잠을 부여하거나 획득하는 기본 공격 스킬을 사용하여 적에게 적중 시, 대상이 보유한 [Sinking] 효과(특수 침잠을 포함)를 발동시킬 때마다 턴 종료 시 자신의 정신력 5 회복 (인격 별로 턴 당 2회).\n턴 시작 시 정신력이 45일 경우 효과가 변경되어, 기본 공격 스킬을 사용하여 적중 시 대상이 보유한 [Sinking] 효과(특수 침잠을 포함)를 발동시킬 때마다 대상 적에게 [Sinking] 횟수 3 부여 (인격 별로 턴 당 2회)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].desc
   limit: do 2430 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [WaveSinking], [DefenseDown], [AttackUp]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [WaveSinking] = 역류 / Reflux; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Sinking] Potency, Count, or 'Unique Sinking'. (except E.G.O Skills; except Backup Units)\n\nTurn Start: inflict 1 [WaveSinking] against a random enemy\n\nWhen an enemy with [WaveSinking] is killed, at the next Turn Start, transfer the [WaveSinking] Stack from the said enemy to an enemy with the highest, but not maxed, [WaveSinking] Stack\n\nWhen hitting and dealing HP damage to an enemy with a Skill that inflicts [Sinking] Potency, Count, or 'Unique Sinking', inflict 4 [Sinking] Potency and +3 [Sinking] Count at Turn End (once per turn for each enemy)\nCombat Start: when activating Gloom or Lust A-Reson., inflict 3 [Sinking] and +3 [Sinking] on all enemies (for Abnormalities, a random Part)\n\nAfter using a base Attack Skill, if the target has 10+ [Sinking] Potency, heal ([Sinking] Potency on the target / 10) SP on self (max 5) and inflict the same amount as [DefenseDown] against the target (max 5; once per turn for each enemy)\n\nTurn End: all allies gain [AttackUp] equal to the number of enemies that have -45 SP or are Non-SP Units next turn (max 6)\n\nCoin Power +1 for Plus Coin Skills that inflict [Sinking] Potency, Count, or 'Unique Sinking'\nBase Power +(4 / # of Coins) (min. 1; rounded down) for Minus Coin Skills that inflict [Sinking] Potency, Count, or 'Unique Sinking'\n\nWhen activating the [Sinking] effect(including 'Unique Sinking') on the target with an On Hit effect from a Base Attack Skill that inflicts or gains [Sinking] Potency, [Sinking] Count, or 'Unique Sinking', heal 5 SP at Turn End (2 times per turn per Identity)\nIf the unit was at 45 SP at Turn Start, the effect changes to the following: when hitting and activating the [Sinking] effect(including 'Unique Sinking') on the target with a base Attack Skill, inflict +3 [Sinking] Count against the targeted enemy (2 times per turn per Identity)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa początku tury nakłada 1 [WaveSinking] na 1 losowego wroga\n\nGdy ginie wróg posiadający [WaveSinking], na początku następnej tury nakłada na wroga z najwyższą wartością [WaveSinking] poniżej maksimum tyle [WaveSinking], ile wynosiła wartość [WaveSinking] pokonanego wroga.\n\nPrzy trafieniu wroga Umiejętnością nakładającą Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, jeżeli zadano obrażenia HP, na koniec tury nakłada na cel 4 Moc [Sinking] i 3 Liczniki [Sinking] (1 wywołanie na turę na wroga)\nPrzy wywołaniu Pełnego Rezonansu Posępności lub Żądzy, na początku walki nakłada na wszystkich wrogów (w przypadku Anomalii — 1 losową Partię) 3 Moc [Sinking] i 3 Liczniki [Sinking].\n\nNa koniec ataku Umiejętnością podstawową, jeżeli wróg ma co najmniej 10 Mocy [Sinking], odzyskuje Poczytalność równą (Moc [Sinking] celu/10) (maks. 5) i nakłada na cel [DefenseDown] (do maks. 5; 1 wywołanie na turę na wroga)\n\nNa koniec tury wszyscy sojusznicy zyskują [AttackUp] w liczbie równej liczbie wrogów z Poczytalnością -45 lub bez Poczytalności (maks. 6)\n\nUmiejętności monety Plus nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie zyskują Moc Monet +1\nUmiejętności monety Minus nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)\n\nPrzy trafieniu wroga Umiejętnością podstawową ataku nakładającą lub zyskującą Moc [Sinking], Licznik [Sinking] lub Szczególne Zatonięcie, za każde wywołanie efektu [Sinking] celu (wliczając Szczególne Zatonięcie) odzyskuje na koniec tury 5 Poczytalności (2 razy na turę na Tożsamość).\nNa początku tury przy Poczytalności 45 efekt się zmienia: przy trafieniu wroga Umiejętnością podstawową, za każde wywołanie efektu [Sinking] celu (wliczając Szczególne Zatonięcie) nakłada 3 Liczniki [Sinking] na wroga (2 razy na turę na Tożsamość)
109. [Dar E.G.O [9176] — opis skrócony] 침잠 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=9176].simpleDesc
   limit: do 120 znaków
   EN: Inflict Sinking
   PL: — opis skrócony] Nakłada Zatonięcie
110. [Dar E.G.O [9176] — opis skrócony] 방어 레벨 감소 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91761].simpleDesc
   limit: do 120 znaków
   EN: Inflict Defense Level Down
   PL: — opis skrócony] Nakłada Spadek Poziomu Obrony
111. [Dar E.G.O [9176] — opis skrócony] 공격 레벨 증가 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91762].simpleDesc
   limit: do 120 znaków
   EN: Apply Offense Level Up
   PL: — opis skrócony] Nakłada Wzrost Poziomu Ataku
112. [Dar E.G.O [9176] — opis skrócony] 정신력 회복
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91763].simpleDesc
   limit: do 120 znaków
   EN: Heal SP
   PL: Odzyskiwanie Poczytalności
113. [Dar E.G.O [9176] — opis skrócony] 침잠 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91764].simpleDesc
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Dar E.G.O [9176] — opis skrócony] 코인 위력 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91765].simpleDesc
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Dar E.G.O [9176] — opis skrócony] 기본 위력 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91766].simpleDesc
   limit: do 120 znaków
   EN: Gain Base Power
   PL: Zyskuje Moc Bazową
116. [Dar E.G.O [9176] — opis skrócony] 역류 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91767].simpleDesc
   limit: do 120 znaków
   EN: Inflict Reflux
   PL: — opis skrócony] Nakłada Refluks
117. [Dar E.G.O [9176] — opis skrócony] 역류 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9176].simpleDesc[abilityID=91768].simpleDesc
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Dar E.G.O [9178] — nazwa] 엔젤스 컷
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9178].name
   limit: do 40 znaków
   EN: Angel's Cut
   PL: — nazwa] Cięcie Anioła
119. [Dar E.G.O [9178] — opis] 턴 종료시, 각 아군이 자신의 호흡 위력이 20을 초과했으면, 호흡 위력을 1 소모하여 호흡 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9178].desc
   limit: do 150 znaków
   EN: Turn End: when an ally has more than 20 Poise Potency, the said unit consumes 1 Poise Potency to gain +1 Poise Count
   PL: — opis] Na koniec tury, jeżeli sojusznik przekroczył 20 Mocy Oddechu, zużywa 1 Moc Oddechu, by zwiększyć Liczniki Oddechu o 1
120. [Dar E.G.O [9178] — opis skrócony] 호흡 위력 1 소모, 호흡 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9178].simpleDesc[abilityID=9178].simpleDesc
   limit: do 120 znaków
   EN: Consume 1 Poise Potency to gain 1 Poise Count
   PL: — opis skrócony] Zużywa 1 Moc Oddechu, by zwiększyć Liczniki Oddechu o 1
121. [Dar E.G.O [9180] — nazwa] 캐스크 스피리츠
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].name
   limit: do 40 znaków
   EN: Cask Spirits
   PL: — nazwa] Trunek z Beczki
122. [Dar E.G.O [9180] — opis] 턴 시작 시, [Breath] 위력 또는 [Breath] 횟수를 부여하거나 획득하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n턴 종료시, 각 아군이 자신의 [Breath] 위력이 20을 초과했으면, [Breath] 위력을 1 소모하여 [Breath] 횟수 1 증가\n\n턴 종료 시, [Breath] 위력이 제일 높은 아군 하나와 [Breath] 횟수가 제일 높은 아군 하나에게 다음 턴에 [Agility] 2, [AttackUp] 1, [AttackDmgUp] 1 부여 (같은 인격일 경우 중복 가능)\n\n스킬 효과로 [Breath]위력을 획득할 때마다 해당 캐릭터가 [Breath] 위력 2, [Breath] 횟수 2 얻음. 보유한 [Breath] 위력과 횟수의 합이 20 미만이면, 대신 [Breath] 위력 3, [Breath] 횟수 3 얻음.\n\n전투 종료 시, 자신의 [Breath] 위력이 40을 초과하면, [Breath] 위력을 15 소모하여 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 [Discard] (캐릭터 당, 턴 당 1회)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].desc
   limit: do 1160 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [Agility], [AttackUp], [AttackDmgUp], [Discard]
   znaczenie tagów: [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Discard] = 버림 / Discard
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply or gain [Breath] Potency or Count. (except E.G.O Skills; except Backup Units)\n\nTurn End: If an ally has more than 20 [Breath] Potency on self, the ally consumes 1 [Breath] Potency to gain 1 [Breath] Count\n\nTurn End: 1 ally with the highest [Breath] Potency and 1 ally with the highest [Breath] Count gain 2 [Agility], 1 [AttackUp], and 1 [AttackDmgUp] next turn (can activate on the same Identity)\n\nWhen gaining [Breath] Potency from Skill effects, gain additional 2 [Breath] Potency and +2 [Breath] Count. If the sum of [Breath] Potency and Count on self is less than 20, gain 3 [Breath] Potency and +3 [Breath] Count instead.\n\nCombat End: at more than 40 [Breath] Potency, consume 15 [Breath] Potency to [Discard] 1 Skill of the lowest rank in all of that unit's Skill Slots (once per turn for each character)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające lub zyskujące Moc [Breath] lub Liczniki [Breath], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa koniec tury, jeżeli sojusznik przekroczył 20 Mocy [Breath], zużywa 1 Moc [Breath], by zwiększyć Liczniki [Breath] o 1\n\nNa koniec tury nakłada 2 [Agility], 1 [AttackUp] i 1 [AttackDmgUp] na następną turę 1 sojusznikowi z najwyższą Mocą [Breath] i 1 sojusznikowi z najwyższymi Licznikami [Breath] (może się nakładać na tę samą Tożsamość)\n\nZa każde zyskanie Mocy [Breath] efektem Umiejętności ta Tożsamość zyskuje 2 Moc [Breath] i 2 Liczniki [Breath]. Jeżeli suma posiadanej Mocy [Breath] i Liczników [Breath] jest niższa niż 20, zamiast tego zyskuje 3 Moc [Breath] i 3 Liczniki [Breath].\n\nNa koniec walki, jeżeli Moc [Breath] przekracza 40, zużywa 15 Mocy [Breath], by [Discard] 1 Umiejętność o najniższej Randze ze swoich slotów Umiejętności (1 raz na turę na Postać)
123. [Dar E.G.O [9180] — opis skrócony] 호흡 횟수 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].simpleDesc[abilityID=9180].simpleDesc
   limit: do 120 znaków
   EN: Gain Poise Count
   PL: — opis skrócony] Zyskuje Liczniki Oddechu
124. [Dar E.G.O [9180] — opis skrócony] 신속 2, 공격 레벨 증가 1, 피해량 증가 1 부여
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].simpleDesc[abilityID=91801].simpleDesc
   limit: do 120 znaków
   EN: Apply 2 Haste, 1 Offense Level Up, and 1 Damage Up
   PL: — opis skrócony] Nakłada 2 Pośpiech, 1 Wzrost Poziomu Ataku i 1 Wzrost Obrażeń
125. [Dar E.G.O [9180] — opis skrócony] 스킬 효과로 호흡 위력을 획득할 때마다 위력, 횟수를 추가로 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].simpleDesc[abilityID=91802].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When gaining [Breath] Potency with Skill effects, gain additional Potency and Count
   PL: — opis skrócony] Za każde zyskanie Mocy Oddechu efektem Umiejętności zyskuje dodatkowo Moc i Liczniki
126. [Dar E.G.O [9180] — opis skrócony] 자신의 스킬 슬롯에서 등급이 가장 낮은 스킬 버림
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9180].simpleDesc[abilityID=91803].simpleDesc
   limit: do 120 znaków
   EN: Discard a Skill of the lowest rank in this unit's Skill Slot
   PL: — opis skrócony] Odrzuca Umiejętność o najniższej Randze ze slotów Umiejętności
127. [Dar E.G.O [9181] — nazwa] 미니어처 전봇대
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9181].name
   limit: do 40 znaków
   EN: Miniature Telepole
   PL: — nazwa] Miniatura Telepole
128. [Dar E.G.O [9181] — opis] 자신의 [Charge] 횟수를 7 이상 소모한 스킬 공격 종료 시 대상이 사망한 경우, (해당 스킬로 소모한 [Charge] 횟수/4)만큼 자신의 [Charge] 횟수 증가 (특수 충전을 포함)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9181].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Attack End with a Skill Attack that consumed 7+ [Charge] Count on self: if the target is defeated, gain ([Charge] Count consumed by the Skill / 4) [Charge] Count (including 'Unique Charge')
   PL: — opis] Na koniec ataku Umiejętnością zużywającą co najmniej 7 własnych Liczników [Charge], jeżeli cel ginie, zwiększa własne Liczniki [Charge] o (zużyte przez tę Umiejętność Liczniki [Charge]/4) (wliczając Szczególne Ładowanie)
129. [Dar E.G.O [9181] — opis skrócony] 소모한 [Charge] 횟수에 비례해서 자신의 [Charge] 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9181].simpleDesc[abilityID=9181].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Gain [Charge] Count based on [Charge] Count consumed
   PL: — opis skrócony] Zwiększa własne Liczniki [Charge] proporcjonalnie do zużytych Liczników [Charge]
130. [Dar E.G.O [9183] — nazwa] 인슐레이터
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9183].name
   limit: do 40 znaków
   EN: Insulator
   PL: — nazwa] Izolator
131. [Dar E.G.O [9183] — opis] 턴 시작 시, [Charge] 횟수 또는 특수 충전을 획득하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n자신의 [Charge] 횟수를 소모한 스킬 공격 종료 시 대상이 사망한 경우, (해당 스킬로 소모한 [Charge] 횟수/3)만큼 자신의 [Charge] 횟수 증가\n\n턴 시작 시 [Charge] 횟수가 3 미만인 경우, [Charge] 횟수 3 증가. 턴 시작 시 충전 횟수가 3 이상인 경우, [AttackDmgUp] 1 얻음.
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9183].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that gain [Charge] Count or 'Unique Charge'. (except E.G.O Skills; except Backup Units)\n\nAttack End with a Skill Attack that consumes [Charge] Count on self: If the target is defeated, gain ([Charge] Count consumed by the Skill / 3) [Charge] Count\n\nTurn Start: At less than 3 [Charge] Count, gain +3 [Charge] Count\nTurn Start: At 3+ [Charge] Count, gain 1 [AttackDmgUp]
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku zyskujące Licznik [Charge] lub Szczególne Ładowanie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa koniec ataku Umiejętnością zużywającą własne Liczniki [Charge], jeżeli cel ginie, zwiększa własne Liczniki [Charge] o (zużyte przez tę Umiejętność Liczniki [Charge]/3)\n\nNa początku tury przy Licznikach [Charge] niższych niż 3, zyskuje +3 Liczniki [Charge]. Na początku tury przy Licznikach Ładowania co najmniej 3, zyskuje 1 [AttackDmgUp].
132. [Dar E.G.O [9183] — opis skrócony] 소모한 [Charge] 횟수에 비례해서 자신의 [Charge] 횟수 증가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9183].simpleDesc[abilityID=9183].simpleDesc
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Dar E.G.O [9183] — opis skrócony] [Charge] 횟수에 따라 [Charge] 횟수 또는 [AttackDmgUp] 1 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9183].simpleDesc[abilityID=91831].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [AttackDmgUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Gain 1 [AttackDmgUp] or [Charge] Count based on [Charge] Count
   PL: — opis skrócony] Zyskuje Liczniki [Charge] lub 1 [AttackDmgUp] zależnie od Liczników [Charge]
134. [Dar E.G.O [9184] — nazwa] 제 5종 영구기관
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9184].name
   limit: do 40 znaków
   EN: T-5 Perpetual Motion Machine
   PL: — nazwa] Silnik Wieczny Typu T-5
135. [Dar E.G.O [9184] — opis] 턴 시작 시, [Charge] 횟수 또는 특수 충전을 획득하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n턴 시작 시 [Charge] 횟수가 3 미만인 경우, [Charge] 횟수 5 증가. 턴 시작 시 충전 횟수가 5 이상인 경우, 속도 최솟값, 속도 최댓값 +2, [Enhancement] 1, [AttackDmgUp] 2 얻음. (특수 충전을 포함)\n\n모든 아군이 전투 참여 턴 시작 시 [ShareCharge]를 얻음.\n\n자신의 [Charge] 횟수를 소모하거나 얻는 스킬 3 공격 종료 시 대상이 사망하였거나 [Charge]이 3 이상이면, 스킬 3 1개를 다음 턴에 사용할 스킬 목록에 추가함. (아군 당 턴 당 1회 발동. 특수 충전을 포함)
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9184].desc
   limit: do 910 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Enhancement], [AttackDmgUp], [ShareCharge]
   znaczenie tagów: [Charge] = 충전 / Charge; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [ShareCharge] = 자가 공진 회로 / Self Resonance Circuitry
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that gain [Charge] Count or 'Unique Charge'. (except E.G.O Skills; except Backup Units)\n\nTurn Start: At less than 3 [Charge] Count, gain +5 [Charge] Count.\nTurn Start: At 5+ [Charge] Count, gain +2 min/max Speed, 1 [Enhancement], and 2 [AttackDmgUp]. (including 'Unique Charge')\n\nAll allies on the field gain [ShareCharge] at Turn Start.\n\nAttack End with a Skill 3 that consumes or gains [Charge] Count on self: If the target is defeated, or if the ally who used the Skill is at 3+ [Charge], they add 1 Skill 3 to the list of Skills for the next upcoming turn. (once per turn for each ally; including 'Unique Charge')
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku zyskujące Licznik [Charge] lub Szczególne Ładowanie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa początku tury przy Licznikach [Charge] niższych niż 3, zyskuje +5 Liczniki [Charge]. Na początku tury przy Licznikach Ładowania co najmniej 5, zyskuje minimalną i maksymalną Szybkość +2, 1 [Enhancement] i 2 [AttackDmgUp] (wliczając Szczególne Ładowanie).\n\nWszyscy sojusznicy na polu zyskują [ShareCharge] na początku tury.\n\nNa koniec ataku Umiejętnością 3 zużywającą lub zyskującą Liczniki [Charge], jeżeli cel ginie lub Liczniki [Charge] wynoszą co najmniej 3, dodaje 1 Umiejętność 3 do listy Umiejętności na następną turę (1 wywołanie na turę na sojusznika; wliczając Szczególne Ładowanie)
136. [Dar E.G.O [9184] — opis skrócony] [Charge] 횟수에 따라 [Charge] 횟수 또는 [AttackDmgUp] 1 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9184].simpleDesc[abilityID=9184].simpleDesc
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Dar E.G.O [9184] — opis skrócony] 소모한 [Charge] 횟수에 비례해서 자신의 [Charge] 횟수 증가. 다음 턴에 [PlusCoinValueUp] 얻음
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9184].simpleDesc[abilityID=91841].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge], [PlusCoinValueUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: Gain [Charge] Count based on [Charge] Count consumed. Next turn, gain [PlusCoinValueUp]
   PL: — opis skrócony] Zwiększa Liczniki [Charge] proporcjonalnie do zużytych; na następną turę zyskuje [PlusCoinValueUp]
138. [Dar E.G.O [9184] — opis skrócony] [Charge] 횟수를 소모한 스킬 3 공격 종료 시 스킬 3 1개를 스킬 목록에 추가
   źródło: EGOgift_MirrorDungeon_2.json :: dataList[id=9184].simpleDesc[abilityID=91842].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Charge]
   znaczenie tagów: [Charge] = 충전 / Charge
   EN: Attack End with a Skill 3 that consumed [Charge] Count: Add 1 Skill 3 to the Skill list
   PL: — opis skrócony] Na koniec ataku Umiejętnością 3 zużywającą [Charge] dodaje 1 Umiejętność 3 do listy Umiejętności

## Dar E.G.O: EGOgift_MirrorDungeon_6
- plik gry: `EGOgift_MirrorDungeon_6.json`

139. [Dar E.G.O [9799] — nazwa] 어떤 철학
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9799].name
   limit: do 40 znaków
   EN: A Certain Philosophy
   PL: — nazwa] Pewna Filozofia
140. [Dar E.G.O [9799] — opis] 기프트 합성 확률이 항상 100%로 적용됨
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9799].desc
   limit: do 120 znaków
   EN: Fix Fusion Probability forecast to 100%
   PL: — opis] Prognoza prawdopodobieństwa syntezy Darów zawsze wynosi 100%
141. [Dar E.G.O [9800] — nazwa] 부
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9800].name
   limit: do 40 znaków
   EN: Wealth
   PL: — nazwa] Bogactwo
142. [Dar E.G.O [9800] — opis] 모든 기프트 구매 및 강화 비용이 1로 고정됨.\n\n보유한 코스트 500 당 모든 아군이 [AttackUp] 1 얻음 (최대 20)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9800].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Fix all E.G.O Gift Purchase & Enhancement Cost to 1.\n\nAllies gain 1 [AttackUp] for every 500 Cost on self (max 20)
   PL: — opis] Koszt zakupu i ulepszania wszystkich Darów E.G.O jest ustalony na 1.\n\nWszyscy sojusznicy zyskują 1 [AttackUp] za każde 500 Kosztu (maks. 20)
143. [Dar E.G.O [9800] — opis skrócony] 공격 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9800].simpleDesc[abilityID=980001].simpleDesc
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Dar E.G.O [9801] — nazwa] 강인환
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9801].name
   limit: do 40 znaków
   EN: Tenacity Bolus
   PL: — nazwa] Bolus Wytrwałości
145. [Dar E.G.O [9801] — opis] 턴 시작 시 최대 체력이 가장 높은 아군 1명이 (이번 전투 동안 적에게 스킬 공격으로 피해를 받은 횟수)만큼 [DefenseUp] 얻음 (최대 6).
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9801].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: 1 ally with the highest max HP gains [DefenseUp] equal to the number of times that unit was hit by the enemies' Skill Attacks (max 6)
   PL: — opis] Na początku tury 1 sojusznik z najwyższym Maks. HP zyskuje [DefenseUp] w liczbie równej liczbie otrzymanych obrażeń od Umiejętności ataku wrogów w tej walce (maks. 6).
146. [Dar E.G.O [9801] — opis skrócony] 방어 레벨 증가 얻음
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9801].simpleDesc[abilityID=9801].simpleDesc
   limit: do 120 znaków
   EN: Gain Defense Level Up
   PL: — opis skrócony] Zyskuje Wzrost Poziomu Obrony
147. [Dar E.G.O [9802] — nazwa] 전격부
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9802].name
   limit: do 40 znaków
   EN: Lightning Axe
   PL: — nazwa] Topór Piorunowy
148. [Dar E.G.O [9802] — opis] [Charge] 횟수를 소모하는 스킬 적중 시 [Burst] 1 부여 (스킬 당 3회 발동. 특수 충전을 포함)\n\n[Burst], [Charge]을 부여하거나 획득하는 공격 스킬을 보유한 인격이 편성된 수에 따라 기프트 효과 강화 (E.G.O 스킬 제외, 편성 인원 포함).\n\n- 6인 이상\n적에게 [Burst] 피해를 입히면, [Charge] 횟수 1 증가 (스킬 당 3회)\n\n- 8인 이상\n[Charge] 횟수를 소모하는 스킬 적중 시 [Burst] 횟수 1 증가 (스킬 당 3회. 특수 충전을 포함)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9802].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Burst]
   znaczenie tagów: [Charge] = 충전 / Charge; [Burst] = 파열 / Rupture
   EN: On Hit with Skills that consume [Charge] Count: inflict 1 [Burst] (3 times per Skill; including 'Unique Charge')\n\nThis E.G.O Gift's effects are enhanced based on the number of Identities in the Team loadout with Attack Skills that apply [Burst] or gain [Charge]. (except E.G.O Skills; counts all units in the Team)\n\n- At 6+...\nWhen dealing [Burst] damage to enemies, gain +1 [Charge] Count (3 times per Skill)\n\n- At 8+...\nOn Hit with Skills that consume [Charge] Count, inflict +1 [Burst] Count (3 times per Skill; including 'Unique Charge')
   PL: — opis] Przy trafieniu Umiejętnością zużywającą Liczniki [Charge], nakłada 1 [Burst] (3 wywołania na Umiejętność; wliczając Szczególne Ładowanie)\n\nEfekty tego Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi [Burst] lub zyskującymi [Charge] (poza Umiejętnościami E.G.O; wlicza wszystkie jednostki zespołu).\n\n- Przy co najmniej 6 Tożsamościach\nPrzy zadaniu obrażeń [Burst] wrogowi, zwiększa Liczniki [Charge] o 1 (3 razy na Umiejętność)\n\n- Przy co najmniej 8 Tożsamościach\nPrzy trafieniu Umiejętnością zużywającą Liczniki [Charge], zwiększa Liczniki [Burst] o 1 (3 razy na Umiejętność; wliczając Szczególne Ładowanie)
149. [Dar E.G.O [9802] — opis skrócony] 파열 1 부여
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9802].simpleDesc[abilityID=9802].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 Rupture
   PL: — opis skrócony] Nakłada 1 Rozdarcie
150. [Dar E.G.O [9802] — opis skrócony] 충전 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9802].simpleDesc[abilityID=980202].simpleDesc
   limit: do 120 znaków
   EN: Gain +1 Charge Count
   PL: — opis skrócony] Zwiększa Liczniki Ładowania o 1
151. [Dar E.G.O [9802] — opis skrócony] 파열 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9802].simpleDesc[abilityID=980203].simpleDesc
   limit: do 120 znaków
   EN: Inflict +1 Rupture Count
   PL: — opis skrócony] Zwiększa Liczniki Rozdarcia o 1
152. [Dar E.G.O [9803] — nazwa] 거울 속의 꽃
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9803].name
   limit: do 40 znaków
   EN: Flower in the Mirror
   PL: — nazwa] Kwiat w Lustrze
153. [Dar E.G.O [9803] — opis] 매 턴 시작 시 모든 적에게 [Burst] 위력 3 부여, [Burst] 횟수 1 증가 (집중 전투일 경우, 모든 부위에 적용).\n\n[Burst], [Breath]을 부여하거나 획득하는 공격 스킬을 보유한 인격이 편성된 수에 따라 기프트 효과 강화 (E.G.O 스킬 제외, 편성 인원 포함).\n\n- 6인 이상\n스킬 적중 시 [Burst] 피해가 발생했다면, [Breath] 횟수 1 얻음 (스킬 당 3회)\n\n- 10인 이상\n스킬 적중 시 크리티컬이 발생했다면, [Burst] 횟수 1 증가 (스킬 당 3회)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9803].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: Every Turn Start: inflict 3 [Burst] Potency and +1 [Burst] Count against all enemies (for Focused Encounters, all Parts)\n\nThis E.G.O Gift's effects are enhanced based on the number of Identities in the Team loadout with Attack Skills that apply [Burst] or gain [Breath]. (except E.G.O Skills; counts all units in the Team)\n\n- At 6+...\nWhen [Burst] damage occurs On Hit with a Skill, gain +1 [Breath] Count (3 times per Skill)\n\n- At 10+...\nOn Crit with a Skill, inflict +1 [Burst] Count (3 times per Skill)
   PL: — opis] Przy każdym początku tury nakłada 3 Moc [Burst] na wszystkich wrogach i zwiększa Liczniki [Burst] o 1 (walki Skupione — wszystkie Partie).\n\nEfekty Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi lub zyskującymi [Burst] lub [Breath] (poza Umiejętnościami E.G.O; wlicza cały zespół).\n\n- Przy co najmniej 6 Tożsamościach\nPrzy trafieniu z obrażeniami [Burst], zyskuje 1 Licznik [Breath] (3 razy na Umiejętność)\n\n- Przy co najmniej 10 Tożsamościach\nPrzy Trafieniu Krytycznym Umiejętnością, zwiększa Liczniki [Burst] o 1 (3 razy na Umiejętność)
154. [Dar E.G.O [9803] — opis skrócony] 파열 위력 3 부여, 파열 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9803].simpleDesc[abilityID=9803].simpleDesc
   limit: do 120 znaków
   EN: Inflict 3 Rupture Potency and +1 Rupture Count
   PL: — opis skrócony] Nakłada 3 Moc Rozdarcia i zwiększa Liczniki Rozdarcia o 1
155. [Dar E.G.O [9803] — opis skrócony] 호흡 횟수 1 얻음
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9803].simpleDesc[abilityID=980302].simpleDesc
   limit: do 120 znaków
   EN: Gain +1 Poise Count
   PL: — opis skrócony] Zyskuje 1 Licznik Oddechu
156. [Dar E.G.O [9803] — opis skrócony] 파열 횟수 1 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9803].simpleDesc[abilityID=980303].simpleDesc
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Dar E.G.O [9804] — nazwa] 물 속의 달
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9804].name
   limit: do 40 znaków
   EN: Moon in the Water
   PL: — nazwa] Księżyc na Wodzie
158. [Dar E.G.O [9804] — opis] [Burst] 위력이 5 이상 부여된 적에게 공격 적중 시 [Breath] 위력 1을 얻고, 자신의 [Breath] 횟수 1 증가 (스킬당 최대 3회).\n\n[Burst], [Breath]을 부여하거나 획득하는 공격 스킬을 보유한 인격이 편성된 수에 따라 기프트 효과 강화 (E.G.O 스킬 제외, 편성 인원 포함).\n\n스킬 적중 시 대상의 [Burst]이 20 이상이면, 크리티컬 피해량 +10% (편성 인원 수 1명당 크리티컬 피해량 3% 추가로 증가)\n\n- 12인 이상\n스킬 적중 시 크리티컬이 발생했다면, 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거 (턴 당, 인격 당 1회)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9804].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: On Hit against enemies with 5+ [Burst] Potency: gain 1 [Breath] Potency and +1 [Breath] Count (3 times per Skill)\n\nThis E.G.O Gift's effects are enhanced based on the number of Identities in the Team loadout with Attack Skills that apply [Burst] or gain [Breath]. (except E.G.O Skills; counts all units in the Team)\n\nOn Hit with a Skill: if target has 20+ [Burst], deal +10% damage on Critical Hit (additional +3% damage on Critical Hit for every 1 Deployed Identity that fit the above condition)\n\n- At 12+...\nOn Hit with a Skill: if it hit Critically, remove 1 random removable negative effect applied to self (once per turn, per Identity)
   PL: — opis] Przy trafieniu atakiem wroga z nałożoną Mocą [Burst] co najmniej 5, zyskuje 1 Moc [Breath] i zwiększa własne Liczniki [Breath] o 1 (maks. 3 razy na Umiejętność).\n\nEfekty tego Daru są wzmocnione w zależności od liczby Tożsamości w zespole z Umiejętnościami ataku nakładającymi lub zyskującymi [Burst] lub [Breath] (poza Umiejętnościami E.G.O; wlicza wszystkie jednostki zespołu).\n\nPrzy trafieniu Umiejętnością, jeżeli [Burst] celu wynosi co najmniej 20, Obrażenia Krytyczne +10% (Obrażenia Krytyczne dodatkowo +3% na każdą Tożsamość w zespole)\n\n- Przy co najmniej 12 Tożsamościach\nPrzy trafieniu Umiejętnością, jeżeli wystąpiło Trafienie Krytyczne, usuwa 1 losowy ujemny efekt z odwracalnych nałożonych na siebie (1 raz na turę na Tożsamość)
159. [Dar E.G.O [9804] — opis skrócony] 호흡 위력, 횟수 얻음
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9804].simpleDesc[abilityID=9804].simpleDesc
   limit: do 120 znaków
   EN: Gain Poise Potency and Count
   PL: — opis skrócony] Zyskuje Moc Oddechu i Liczniki Oddechu
160. [Dar E.G.O [9804] — opis skrócony] 크리티컬 피해량 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9804].simpleDesc[abilityID=980402].simpleDesc
   limit: do 120 znaków
   EN: Deal more Damage on Critical Hit
   PL: Wzrost Obrażeń Krytycznych
161. [Dar E.G.O [9804] — opis skrócony] 부정적인 효과 무작위 제거
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9804].simpleDesc[abilityID=980403].simpleDesc
   limit: do 120 znaków
   EN: Remove a random negative effect
   PL: — opis skrócony] Usuwa 1 losowy ujemny efekt
162. [Dar E.G.O [9795] — nazwa] 떨어진 한 방울
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9795].name
   limit: do 40 znaków
   EN: A Drop
   PL: — nazwa] Kropla
163. [Dar E.G.O [9795] — opis] 턴 시작 시, [BloodDinner]을 소모하는 스킬을 보유한 인격이 3인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n전투 시작 시 [BloodDinner]을 소모하는 인격이 공격하는 대상의 [Laceration] 위력이 30 이상일 때, 대상의 [Laceration] 위력을 15로 감소시키고, 감소한 [Laceration] 위력만큼 [BloodDinner]을 생성함. (턴 당 적 전체에서 1회 발동, 광역 스킬의 경우 메인 타겟에게만 적용됨)\n\n해당 효과로 생성된 [BloodDinner] 10 당, [BloodDinner]을 소모하는 스킬을 보유한 인격에게 다음 턴에 위력 증가 1, 피해량 증가 1 부여 (최대 4)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9795].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Laceration]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed
   EN: Turn Start: This Gift activates for the whole Encounter when 3 or more Identities have Skills that consume [BloodDinner]. (except E.G.O Skills; except Backup Units)\n\nCombat Start: if the target getting attacked by an Identity that consumes [BloodDinner] has 30+ [Laceration] Potency, reduce their [Laceration] Potency to 15. Then, increase [BloodDinner] equal to the amount of [Laceration] Potency reduced. (once per turn for the enemy group as a whole; only activates against the main target when using multi-Atk Weight Skills)\n\nFor Identities with Skills that consume [BloodDinner], apply 1 Power Up and 1 Damage Up next turn for every 10 [BloodDinner] generated with the above effect (max 4)
   PL: — opis] Na początku tury, jeżeli co najmniej 3 Tożsamości ma Umiejętności zużywające [BloodDinner], Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nNa początku walki, jeżeli [Laceration] celu atakowanego przez Tożsamość zużywającą [BloodDinner] wynosi co najmniej 30, zmniejsza Moc [Laceration] celu do 15 i generuje [BloodDinner] równy zredukowanej Mocy [Laceration] (1 wywołanie na turę na wszystkich wrogów; w przypadku Umiejętności obszarowych stosowane tylko do głównego celu).\n\nZa każde 10 [BloodDinner] wygenerowanych tym efektem nakłada na Tożsamości z Umiejętnościami zużywającymi [BloodDinner] 1 Wzrost Mocy i 1 Wzrost Obrażeń na następną turę (maks. 4)
164. [Dar E.G.O [9795] — opis skrócony] 출혈 위력 감소, 혈찬 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9795].simpleDesc[abilityID=9795].simpleDesc
   limit: do 120 znaków
   EN: Reduce Bleed Potency and increase Bloodfeast
   PL: — opis skrócony] Zmniejsza Moc Krwawienia i zwiększa Krwawą Ucztę
165. [Dar E.G.O [9795] — opis skrócony] 위력 증가, 피해량 증가 부여
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9795].simpleDesc[abilityID=979501].simpleDesc
   limit: do 120 znaków
   EN: Apply Power Up and Damage Up
   PL: — opis skrócony] Nakłada Wzrost Mocy i Wzrost Obrażeń
166. [Dar E.G.O [9796] — nazwa] 애달픈 날숨
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9796].name
   limit: do 40 znaków
   EN: Sorrowful Exhale
   PL: — nazwa] Smutny Wydech
167. [Dar E.G.O [9796] — opis] 편성 순서 5번 아군의 [Breath] 위력과 [Breath] 횟수의 합이 50 이상일 경우, 합 승리 또는 일방 공격시 사용하는 스킬 코인이 반드시 앞면(마이너스 코인일 경우 뒷면)으로 결정되고, 치명타로 가하는 피해량 +80% (전투 당 1회, E.G.O 스킬 제외)\n\n편성된 인원 중 [Breath] 위력 또는 [Breath] 횟수를 부여 또는 획득하는 공격 스킬을 보유한 인격이 5인 이상 일 때, 편성 순서 5번 아군의 크리티컬 피해량 +60% (조건 초과 편성 인원 수 1명당 크리티컬 피해량 20% 추가로 증가, 편성 인원 포함)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9796].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: If the #5 Deployed ally has 50+ (sum of [Breath] Potency and [Breath] Count): their Skill Coins, when attacking after Clash Win or when using Unopposed Attacks, always flip Heads(for Minus Coins, Tails), and deal +80% damage on Critical Hit. (once per Encounter, except E.G.O Skills)\n\nIf there are 5 or more allies in the Team loadout with Attack Skills that apply or gain [Breath] Potency or [Breath] Count, #5 Deployed ally deals +60% damage on Critical Hit (additional +20% damage on Critical Hit for every 1 Deployed Identity beyond the conditional, including Backup Units)
   PL: — opis] Jeżeli suma Mocy [Breath] i Liczników [Breath] sojusznika przydzielonego na 5. pozycji wynosi co najmniej 50, Monety Umiejętności używanych przy wygranej Starciu lub ataku jednostronnym wypadają zawsze jako Awers (w przypadku monet Minus — Rewers), a zadawane Obrażenia Krytyczne +80% (1 raz na walkę; poza Umiejętnościami E.G.O)\n\nJeżeli co najmniej 5 Tożsamości w zespole ma Umiejętności ataku nakładające lub zyskujące Moc [Breath] lub Liczniki [Breath], sojusznik przydzielony na 5. pozycji zadaje Obrażenia Krytyczne +60% (dodatkowo +20% Obrażeń Krytycznych na każdą Tożsamość w zespole ponad warunek, wliczając w zespół)
168. [Dar E.G.O [9796] — opis skrócony] 크리티컬 피해량 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9796].simpleDesc[abilityID=9796].simpleDesc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Dar E.G.O [9796] — opis skrócony] 크리티컬 피해량 증가
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9796].simpleDesc[abilityID=979601].simpleDesc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Dar E.G.O [9797] — nazwa] 깨어질 화포
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9797].name
   limit: do 40 znaków
   EN: Shatterbound Cannon
   PL: — nazwa] Działo Roztrzaskania
171. [Dar E.G.O [9797] — opis] 턴 시작 시, 매 턴마다 [GiftCannon] 2, [GiftGlass] 2 얻음\n2번째 턴부터, 매 턴마다 획득하는 값이 각각 1씩 증가함 (최대 8회 증가)
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9797].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [GiftCannon], [GiftGlass]
   znaczenie tagów: [GiftCannon] = 화력 / Firepower; [GiftGlass] = 연약 / Delicateness
   EN: Turn Start: Gain 2 [GiftCannon] and 2 [GiftGlass] every turn\n\nStarting from the 2nd turn, Stacks of [GiftCannon] and [GiftGlass] gained from the above effect increase by 1 each (up to 8 times)
   PL: — opis] Na początku tury zyskuje co turę 2 [GiftCannon] i 2 [GiftGlass]\nOd 2. tury wartości zyskiwane co turę rosną o 1 każda (maks. 8 zwiększeń)
172. [Dar E.G.O [9797] — opis skrócony] 화력, 연약 얻음
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9797].simpleDesc[abilityID=9797].simpleDesc
   limit: do 120 znaków
   EN: Gain Firepower and Delicateness
   PL: — opis skrócony] Zyskuje Siłę Ognia i Delikatność
173. [Dar E.G.O [9798] — nazwa] 탐하는 가시
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9798].name
   limit: do 40 znaków
   EN: Coveting Thorn
   PL: — nazwa] Pożądający Cierń
174. [Dar E.G.O [9798] — opis] 스테이지 시작시, [BloodDinner]을 100 생성\n턴 시작 시, [Laceration]이 있는 적 (부위)에 [RoseThorn]을 2 부여함.\n모든 적 (부위)에 [Laceration]이 있으면, [RoseThorn]을 4 부여함.
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9798].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Laceration], [RoseThorn]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [RoseThorn] = 탐식극(貪食棘) / Gluttonous Thorn (貪食棘)
   EN: Encounter Start: Increase [BloodDinner] by 100\nTurn Start: Inflict 2 [RoseThorn] against enemies (or Parts) with [Laceration].\nIf all enemies (or all Parts) have [Laceration], inflict 4 [RoseThorn].
   PL: — opis] Na początku spotkania generuje 100 [BloodDinner]\nNa początku tury nakłada 2 [RoseThorn] na wrogów (Partie) z [Laceration].\nJeżeli wszyscy wrogowie (wszystkie Partie) mają [Laceration], nakłada 4 [RoseThorn].
175. [Dar E.G.O [9798] — opis skrócony] 탐식극(貪食棘) 부여
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9798].simpleDesc[abilityID=9798].simpleDesc
   limit: do 120 znaków
   EN: Inflict Gluttonous Thorn (貪食棘)
   PL: — opis skrócony] Nakłada Kolec Obżarstwa (貪食棘)
176. [Dar E.G.O [9798] — opis skrócony] 탐식극(貪食棘) 부여
   źródło: EGOgift_MirrorDungeon_6.json :: dataList[id=9798].simpleDesc[abilityID=979801].simpleDesc
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Dar E.G.O: EGOgift_MirrorDungeon_7
- plik gry: `EGOgift_MirrorDungeon_7.json`

177. [Dar E.G.O [9209] — nazwa] 도시를 사랑하는 당신을 위한
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9209].name
   limit: do 40 znaków
   EN: For You Who Love the City
   PL: — nazwa] Dla miłujących Miasto
178. [Dar E.G.O [9209] — opis] 피격된 아군의 체력이 30% 미만이면, 다음 턴에 해당 아군이 최대 체력의 80% 만큼 체력을 회복하고, 나머지 아군이 최대 체력의 40% 만큼 체력을 회복 (전투당 1회)\n- 최대 체력 이상의 초과 회복량은 보호막으로 부여\n- 해당 효과로 체력을 50 이상 회복 했으면, [AttackUp] 3, [DefenseDown] 3 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9209].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: If an ally is at less than 30% HP when hit, said ally heals 80% HP and other allies heal 40% HP next turn (once per Encounter)\n- Excess healing beyond max HP is applied as Shield\n- If an ally healed 50+ HP due to the above effect, gain 3 [AttackUp] and 3 [DefenseDown]
   PL: — opis] Jeżeli trafiony sojusznik ma mniej niż 30% HP, na następną turę odzyskuje HP równe 80% Maks. HP, a pozostali sojusznicy odzyskują 40% Maks. HP (1 raz na walkę)\n- Nadwyżka odzyskanego HP ponad Maks. HP jest nakładana jako Tarcza\n- Jeżeli dzięki temu efektowi odzyskano co najmniej 50 HP, zyskuje 3 [AttackUp] i 3 [DefenseDown]
179. [Dar E.G.O [9209] — opis skrócony] 체력 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9209].simpleDesc[abilityID=9209].simpleDesc
   limit: do 120 znaków
   EN: Heal HP
   PL: Odzyskiwanie HP
180. [Dar E.G.O [9210] — nazwa] 연육 망치
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9210].name
   limit: do 40 znaków
   EN: Meat Tenderizer
   PL: — nazwa] Tłuczek do Mięsa
181. [Dar E.G.O [9210] — opis] [편성 4번 인격 전용 효과]\n\n타격 공격 스킬을 2개 이상 보유한 경우, 턴 시작 시 [ParryingResultUp] 1 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9210].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: [Effects apply only to #4 Deployed Identity]\n\nIf this unit has 2+ Blunt Attack Skills, gain 1 [ParryingResultUp] at Turn Start
   PL: — opis] [Efekt wyłącznie dla Tożsamości na Przydziale #4]\n\nJeżeli posiada co najmniej 2 Umiejętności ataku typu Uderzenia, na początku tury zyskuje 1 [ParryingResultUp]
182. [Dar E.G.O [9210] — opis skrócony] [ParryingResultUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9210].simpleDesc[abilityID=9210].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Gain [ParryingResultUp]
   PL: — opis skrócony] Zyskuje [ParryingResultUp]
183. [Dar E.G.O [19210] — nazwa] 연육 망치+
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19210].name
   limit: do 40 znaków
   EN: Meat Tenderizer+
   PL: — nazwa] Tłuczek do Mięsa+
184. [Dar E.G.O [19210] — opis] [편성 4번 인격 전용 효과]\n\n타격 공격 스킬을 2개 이상 보유한 경우, 턴 시작 시 [ParryingResultUp] <style="upgradeHighlight">2</style> 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19210].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: [Effects apply only to #4 Deployed Identity]\n\nIf this unit has 2+ Blunt Attack Skills, gain <style="upgradeHighlight">2</style> [ParryingResultUp] at Turn Start
   PL: — opis] [Efekt wyłącznie dla Tożsamości na Przydziale #4]\n\nJeżeli posiada co najmniej 2 Umiejętności ataku typu Uderzenia, na początku tury zyskuje [ParryingResultUp] <style="upgradeHighlight">2</style>
185. [Dar E.G.O [19210] — opis skrócony] [ParryingResultUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19210].simpleDesc[abilityID=19210].simpleDesc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Dar E.G.O [29210] — nazwa] 연육 망치++
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29210].name
   limit: do 40 znaków
   EN: Meat Tenderizer++
   PL: — nazwa] Tłuczek do Mięsa++
187. [Dar E.G.O [29210] — opis] [편성 4번, <style="upgradeHighlight">5번</style> 인격 전용 효과]\n\n타격 공격 스킬을 2개 이상 보유한 경우, 턴 시작 시 [ParryingResultUp] 2 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29210].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [ParryingResultUp]
   znaczenie tagów: [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: [Effects apply only to #4, <style="upgradeHighlight">#5</style> Deployed Identities]\n\nIf this unit has 2+ Blunt Attack Skills, gain 2 [ParryingResultUp] at Turn Start
   PL: — opis] [Efekt wyłącznie dla Tożsamości na Przydziale #4, <style="upgradeHighlight">#5</style>]\n\nJeżeli ma co najmniej 2 Umiejętności ataku typu Uderzenia, na początku tury zyskuje 2 [ParryingResultUp]
188. [Dar E.G.O [29210] — opis skrócony] [ParryingResultUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29210].simpleDesc[abilityID=29210].simpleDesc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Dar E.G.O [9207] — nazwa] 확률과 선택
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9207].name
   limit: do 40 znaków
   EN: Chance & Choice
   PL: — nazwa] Szansa i Wybór
190. [Dar E.G.O [9207] — opis] 가장 왼쪽 슬롯에 등록한 E.G.O 스킬의 피해량이 -50%나 +150% 중 랜덤하게 적용 (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9207].desc
   limit: do 140 znaków
   EN: Random chance for the leftmost Slot's E.G.O Skill to deal -50% damage or +150% damage (once per turn)
   PL: — opis] Obrażenia Umiejętności E.G.O zapisanej w skrajnie lewym slocie losowo otrzymują -50% lub +150% (1 raz na turę)
191. [Dar E.G.O [9207] — opis skrócony] E.G.O 스킬의 피해량 증가 또는 감소
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9207].simpleDesc[abilityID=9207].simpleDesc
   limit: do 120 znaków
   EN: E.G.O Skills deal more(or less) damage
   PL: — opis skrócony] Umiejętności E.G.O zadają więcej (lub mniej) obrażeń
192. [Dar E.G.O [9208] — nazwa] 인연 얽힘
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9208].name
   limit: do 40 znaków
   EN: Entangled Fate
   PL: Splot Przeznaczenia
193. [Dar E.G.O [9208] — opis] 전투 시작 시 완전 공명이 7 이상이면, 모든 아군이 이번 턴 동안 최종 위력 +5 (전투당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9208].desc
   limit: do 130 znaków
   EN: Combat Start: At 7+ A-Reson., all allies gain Final Power +5 for this turn (once per Encounter)
   PL: — opis] Na początku walki przy Pełnym Rezonansie co najmniej 7, sojusznicy zyskują Moc Końcową +5 w tej turze (1 raz na walkę)
194. [Dar E.G.O [9208] — opis skrócony] 최종 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9208].simpleDesc[abilityID=9208].simpleDesc
   limit: do 120 znaków
   EN: Gain Final Power
   PL: — opis skrócony] Zyskuje Moc Końcową
195. [Dar E.G.O [9211] — nazwa] 먹장구름
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9211].name
   limit: do 40 znaków
   EN: Raincloud
   PL: — nazwa] Deszczowa Chmura
196. [Dar E.G.O [9211] — opis] 턴 시작시, 적 전체의 [Sinking] 위력과 [Sinking] 횟수의 합이 30 이상이면, 아래 효과 적용\n\n- [Sinking] 위력, 횟수를 부여하는 스킬의 최종 위력 +1 (특수 침잠 포함, E.G.O 스킬 제외)\n\n- [Sinking] 위력 또는 [Sinking] 횟수 또는 특수 침잠을 부여하는 공격 스킬을 보유한 인격이 6인 이상이면, 추가로 [Sinking] 위력, 횟수를 부여하는 스킬의 피해량 +20% (특수 침잠 포함, E.G.O 스킬 제외, 대기 인원 포함)\n · 공격 대상이 정신력이 -45이면, 추가 피해량 +10%\n\n- [Sinking] 위력 또는 [Sinking] 횟수 또는 특수 침잠을 부여하는 공격 스킬을 보유한 인격이 10인 이상이면, 추가로 [Sinking] 위력, 횟수를 부여하는 더하기 코인 스킬의 코인 위력 +1 (특수 침잠 포함, E.G.O 스킬 제외, 대기 인원 포함)\n · 빼기 코인 스킬일 경우, 코인 위력 대신 기본 위력 +(4/코인 수) (최소 1, 소수점 버림)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9211].desc
   limit: do 1140 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Turn Start: At 30+ total sum of [Sinking] Potency and [Sinking] Count on all enemies, apply the following effects:\n\n- Skills that inflict [Sinking] Potency or Count: Final Power +1 (including 'Unique Sinking'; excluding E.G.O Skills)\n\n- When 6 or more Identities have Attack Skills that inflict [Sinking] Potency, Count, or 'Unique Sinking', Skills that inflict [Sinking] Potency or Count also deal +20% damage (including 'Unique Sinking' and Backup Units; excluding E.G.O Skills)\n · If the target is at -45 SP, deal additional +10% damage\n\n- When 10 or more Identities have Attack Skills that inflict [Sinking] Potency, Count, or 'Unique Sinking', Plus Coin Skills that inflict [Sinking] Potency or Count also gain Coin Power +1 (including 'Unique Sinking' and Backup Units; excluding E.G.O Skills)\n · Minus Coin Skills: Instead of gaining Coin Power, gain Base Power +(4 / # of Coins) (min 1; rounded down)
   PL: — opis] Na początku tury, jeżeli suma Mocy [Sinking] i Liczników [Sinking] wszystkich wrogów wynosi co najmniej 30, stosuje poniższe efekty\n\n- Umiejętności nakładające Moc [Sinking] lub Liczniki [Sinking] zyskują Moc Końcową +1 (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O)\n\n- Jeżeli co najmniej 6 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Umiejętności nakładające Moc [Sinking] lub Liczniki [Sinking] zadają dodatkowo +20% obrażeń (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O; wliczając jednostki zapasowe)\n · Jeżeli Poczytalność atakowanego celu wynosi -45, dodatkowe obrażenia +10%\n\n- Jeżeli co najmniej 10 Tożsamości ma Umiejętności ataku nakładające Moc [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie, Umiejętności monety Plus nakładające Moc [Sinking] lub Liczniki [Sinking] zyskują dodatkowo Moc Monet +1 (wliczając Szczególne Zatonięcie; poza Umiejętnościami E.G.O; wliczając jednostki zapasowe)\n · Umiejętności monety Minus zamiast Mocy Monet zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)
197. [Dar E.G.O [9211] — opis skrócony] 침잠 스킬의 최종 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9211].simpleDesc[abilityID=9211].simpleDesc
   limit: do 120 znaków
   EN: Sinking Skills gain Final Power
   PL: — opis skrócony] Umiejętności Zatonięcia zyskują Moc Końcową
198. [Dar E.G.O [9211] — opis skrócony] 침잠 스킬의 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9211].simpleDesc[abilityID=92111].simpleDesc
   limit: do 120 znaków
   EN: Sinking Skills deal more damage
   PL: — opis skrócony] Umiejętności Zatonięcia zadają więcej obrażeń
199. [Dar E.G.O [9211] — opis skrócony] 침잠 스킬의 코인/기본 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9211].simpleDesc[abilityID=92112].simpleDesc
   limit: do 120 znaków
   EN: Sinking Skills gain Coin/Base Power
   PL: — opis skrócony] Umiejętności Zatonięcia zyskują Moc Monet/Bazową
200. [Dar E.G.O [9212] — nazwa] 모든 악의 끝
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].name
   limit: do 40 znaków
   EN: The End of all Evil
   PL: — nazwa] Koniec wszelkiego Zła
201. [Dar E.G.O [9212] — opis] 편성된 피쿼드호 소속 인격이 3인 이상일 때 발동 (대기 인원 포함)\n\n[Laceration] 또는 특수 출혈이 부여된 적에게 공격 스킬 적중 시 [Breath] 횟수 2 증가 또는 [Breath] 3 얻음 (인격별 턴당 3회 발동)\n\n스킬 적중 시 크리티컬이 발생했다면, 80% 확률로 다음 턴에 [PenetrateResultUp] 1 얻음 (인격별 턴당 2회 발동, E.G.O 스킬 포함, 반격 포함)\n- 피쿼드호 소속 인격이면, 추가로 다음 턴에 [PlusCoinValueUp] 1 얻음 (인격별 턴당 1회 발동)\n\n기본 스킬로 크리티컬 앞면 적중 시 해당 코인으로 부여하는 부정적인 효과의 수치가 1 증가함 (인격별 턴당 1회 발동, E.G.O 스킬 제외, 반격 포함)\n\n적 또는 아군 사망 시 이번 전투동안 피쿼드호 소속 인격이 매턴 [PenetrateResultUp] 1, [Protection] 1, [CriticalDamageUp] 1 얻음 (전투당 최대 3회 발동)\n\n피쿼드호 소속의 인원이 공격을 적중했으면, 편성 순서가 가장 빠른 피쿼드호 소속 인격의 정신력 7 회복 (스킬당 1회)\n\n아군이 적 처치 시 편성 순서가 가장 빠른 피쿼드호 소속 인격의 정신력이 감소했으면, 정신력 15 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].desc
   limit: do 1430 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Breath], [PenetrateResultUp], [PlusCoinValueUp], [Protection], [CriticalDamageUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Breath] = 호흡 / Poise; [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [Protection] = 보호 / Protection; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: Activates when there are 3 or more The Pequod-faction Identities (counting Backup units)\n\nOn Hit with an Attack Skill against enemies with [Laceration] or 'Unique Bleed': Gain 3 [Breath] or +2 [Breath] Count (3 times per turn per Identity)\n\nOn Crit: 80% chance to gain 1 [PenetrateResultUp] next turn (2 times per turn per Identity; including E.G.O Skills and Counter Skills)\n- The Pequod-faction Identities gain 1 [PlusCoinValueUp] next turn as well (once per turn per Identity)\n\nOn Crit Heads Hit with a Base Skill: Inflict +1 more of the negative effect with that Coin (once per turn per Identity; including Counter Skills and excluding E.G.O Skills)\n\nOn enemy or ally death, The Pequod-faction Identities gain 1 [PenetrateResultUp], 1 [Protection], and 1 [CriticalDamageUp] each turn for the rest of this Encounter (3 times per Encounter)\n\nIf one of The Pequod-faction Identities attacks and hits an enemy, heal 7 SP for The Pequod-faction Identity with the earliest Deployment order (once per Skill)\n\nWhen an ally kills an enemy, heal 15 SP for The Pequod-faction Identity with the earliest Deployment order if said Identity lost SP
   PL: — opis] Uruchamia się, gdy w zespole są co najmniej 3 Tożsamości załogi Pequod (wliczając jednostki zapasowe)\n\nPrzy trafieniu Umiejętnością ataku wroga z nałożonym [Laceration] lub Szczególnym Krwawieniem, zwiększa Liczniki [Breath] o 2 lub zyskuje 3 [Breath] (3 razy na turę na Tożsamość)\n\nPrzy trafieniu Umiejętnością z Trafieniem Krytycznym, z 80% szansą zyskuje 1 [PenetrateResultUp] na następną turę (2 razy na turę na Tożsamość; wliczając Umiejętności E.G.O i Kontry)\n- Jeżeli Tożsamość należy do załogi Pequod, dodatkowo zyskuje 1 [PlusCoinValueUp] na następną turę (1 raz na turę na Tożsamość)\n\nPrzy trafieniu Awersu z Trafieniem Krytycznym Umiejętnością podstawową, wartość ujemnych efektów nakładanych tą monetą rośnie o 1 (1 raz na turę na Tożsamość; poza Umiejętnościami E.G.O; wliczając Kontry)\n\nGdy ginie wróg lub sojusznik, przez resztę tej walki Tożsamości załogi Pequod zyskują co turę 1 [PenetrateResultUp], 1 [Protection] i 1 [CriticalDamageUp] (maks. 3 razy na walkę)\n\nJeżeli Tożsamość załogi Pequod trafiła wroga atakiem, Tożsamość załogi Pequod przydzielona najwcześniej w kolejności odzyskuje 7 Poczytalności (1 raz na Umiejętność)\n\nGdy sojusznik pokona wroga, jeżeli Poczytalność Tożsamości załogi Pequod przydzielonej najwcześniej w kolejności jest obniżona, odzyskuje ona 15 Poczytalności
202. [Dar E.G.O [9212] — opis skrócony] 호흡 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].simpleDesc[abilityID=9212].simpleDesc
   limit: do 120 znaków
   EN: Gain Poise
   PL: — opis skrócony] Zyskuje Oddech
203. [Dar E.G.O [9212] — opis skrócony] 크리티컬 적중시 일정 확률로 다음 턴에 [PenetrateResultUp] 얻음, 조건 만족 시 다음 턴에 [PlusCoinValueUp] 얻음, 부정적인 효과 부여량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].simpleDesc[abilityID=92121].simpleDesc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: [PenetrateResultUp], [PlusCoinValueUp]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: On Crit: Chance to gain [PenetrateResultUp] next turn; gain [PlusCoinValueUp] and increase the amount of negative effect inflicted when conditions are met
   PL: — opis skrócony] Przy Trafieniu Krytycznym z pewną szansą zyskuje [PenetrateResultUp] na następną turę; gdy warunek spełniony, zyskuje [PlusCoinValueUp] i zwiększa wartość ujemnych efektów
204. [Dar E.G.O [9212] — opis skrócony] [PenetrateResultUp], [Protection], [CriticalDamageUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].simpleDesc[abilityID=92122].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateResultUp], [Protection], [CriticalDamageUp]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [Protection] = 보호 / Protection; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: Gain [PenetrateResultUp], [Protection], and [CriticalDamageUp]
   PL: — opis skrócony] Zyskuje [PenetrateResultUp], [Protection] i [CriticalDamageUp]
205. [Dar E.G.O [9212] — opis skrócony] 정신력 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9212].simpleDesc[abilityID=92123].simpleDesc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Dar E.G.O [9213] — nazwa] 미니어처 대관람차
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].name
   limit: do 40 znaków
   EN: Miniature Ferris Wheel
   PL: — nazwa] Miniatura Kolejki Górskiej
207. [Dar E.G.O [9213] — opis] 혈귀인 모든 아군의 기본 스킬 코인 위력 +1, 자신의 ([BloodDinner_Accumulation] / 10)%만큼 스킬 <noparse>피해량 증가</noparse>\n\n턴 종료 시, [Laceration]을 보유한 아군 중 가장 체력이 적은 인격 2명이 자신의 최대 체력의 5%만큼 체력을 회복하고 다음 턴 시작시 [SwirlingBloodPersonality] 10 얻음\n\n적 처치시, 해당 적의 (본체 최대 체력/10)만큼 [BloodDinner] 생성 (최대 50)\n\n턴 종료시 이번 턴에 사망한 아군이 있으면, 다음 턴에 모든 아군이 [Enhancement] 2 얻음\n\n적이 증원되는 전투에서 새로운 적이 등장하면, 전투 시작 시 해당 적에게 [Laceration] 5, [Laceration] 횟수 3 부여.\n아군에 <혈귀>가 있다면, 적이 증원될 때 모든 적의 [Laceration]을 2회 발동시키고, 모든 적의 [Laceration] 횟수 2 감소
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [BloodDinner_Accumulation], [Laceration], [SwirlingBloodPersonality], [BloodDinner], [Enhancement]
   znaczenie tagów: [BloodDinner_Accumulation] = 누적 소모 혈찬 / Bloodfeast Consumed; [Laceration] = 출혈 / Bleed; [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】; [BloodDinner] = 혈찬 / Bloodfeast; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: All Bloodfiend allies: Base Skill Coin Power +1, deal +([BloodDinner_Accumulation] / 10)% Skill damage\n\nTurn End: Among allies with [Laceration], 2 allies with the least HP heal 5% HP and gain 10 [SwirlingBloodPersonality] at next Turn Start\n\nOn enemy Kill, increase [BloodDinner] by (enemy Core max HP / 10) (max 50)\n\nTurn End: If an ally died this turn, all allies gain 2 [Enhancement] next turn\n\nIn Encounters where backup enemies appear: When new enemies appear, inflict 5 [Laceration] and +3 [Laceration] Count against them at Combat Start.\nIf there is a <Bloodfiend> among allies: When new enemies enter the battle, activate [Laceration] on all enemies twice and reduce their [Laceration] Count by 2
   PL: — opis] Podstawowe Umiejętności wszystkich sojuszników Krwiożerców zyskują Moc Monet +1, a Umiejętności zadają obrażenia <noparse>+([BloodDinner_Accumulation] / 10)%</noparse>\n\nNa koniec tury 2 Tożsamości z najmniej HP spośród sojuszników z [Laceration] odzyskują HP równe 5% własnego Maks. HP i zyskują 10 [SwirlingBloodPersonality] na początku następnej tury\n\nPrzy zabiciu wroga generuje [BloodDinner] w wysokości (Maks. HP korpusu wroga/10) (maks. 50)\n\nNa koniec tury, jeżeli w tej turze zginął sojusznik, wszyscy sojusznicy zyskują 2 [Enhancement] na następną turę\n\nW potyczkach, w których wrogowie mają posiłki: gdy pojawi się nowy wróg, nakłada na niego na początku walki 5 [Laceration] i 3 Licznika [Laceration].\nJeżeli wśród sojuszników jest <Krwiożerca>: gdy pojawia się nowy wróg, wywołuje [Laceration] na wszystkich wrogach 2 razy i zmniejsza Liczniki [Laceration] wszystkich wrogów o 2
208. [Dar E.G.O [9213] — opis skrócony] 기본 스킬 코인 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].simpleDesc[abilityID=9213].simpleDesc
   limit: do 120 znaków
   EN: Gain Base Skill Coin Power
   PL: — opis skrócony] Zyskuje Moc Monet podstawowych Umiejętności
209. [Dar E.G.O [9213] — opis skrócony] 체력을 회복하고, [SwirlingBloodPersonality] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].simpleDesc[abilityID=92131].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SwirlingBloodPersonality]
   znaczenie tagów: [SwirlingBloodPersonality] = 일렁임【혈귀】 / Shimmering【Bloodfiend】
   EN: Heal HP and gain [SwirlingBloodPersonality]
   PL: — opis skrócony] Odzyskuje HP i zyskuje [SwirlingBloodPersonality]
210. [Dar E.G.O [9213] — opis skrócony] 공격 위력 증가 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].simpleDesc[abilityID=92132].simpleDesc
   limit: do 120 znaków
   EN: Gain Attack Power Up
   PL: — opis skrócony] Zyskuje Wzrost Mocy Ataku
211. [Dar E.G.O [9213] — opis skrócony] 출혈 위력, 횟수 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9213].simpleDesc[abilityID=92133].simpleDesc
   limit: do 120 znaków
   EN: Inflict Bleed Potency and Count
   PL: — opis skrócony] Nakłada Moc Krwawienia i Liczniki Krwawienia
212. [Dar E.G.O [9214] — nazwa] 달궈진 망치
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9214].name
   limit: do 40 znaków
   EN: Searing Hammer
   PL: — nazwa] Żarzący się Młot
213. [Dar E.G.O [9214] — opis] 적에게 [VibrationIgnition]이 있을 경우 다음 효과 적용\n- 기본 스킬 적중 시 [Combustion] 위력 1 부여 (스킬당 최대 3회)\n- 기본 스킬 적중 시 [VibrationIgnition]이 15 이상이면, [Combustion] 횟수 1 증가 (스킬당 최대 2회)\n- [Combustion] 3당, [VibrationExplosion]로 인한 흐트러짐 손상 +1% (최대 15%)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9214].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [VibrationIgnition], [Combustion], [VibrationExplosion]
   znaczenie tagów: [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Combustion] = 화상 / Burn; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: If the enemy has [VibrationIgnition], apply the following effects:\n- On Base Skill Hit, inflict 1 [Combustion] (3 times per Skill)\n- On Base Skill Hit, if the enemy has 15+ [VibrationIgnition], inflict +1 [Combustion] Count (2 times per Skill)\n- For every 3 [Combustion], +1% to Stagger Threshold raised by [VibrationExplosion] (max 15%)
   PL: — opis] Jeżeli wróg ma [VibrationIgnition], stosuje efekty:\n- Przy trafieniu Umiejętnością podstawową nakłada 1 Moc [Combustion] (maks. 3 razy na Umiejętność)\n- Przy trafieniu Umiejętnością podstawową, jeżeli wróg ma [VibrationIgnition] co najmniej 15, zwiększa Liczniki [Combustion] o 1 (maks. 2 razy na Umiejętność)\n- Za każde 3 [Combustion] Oszołomienie wywołane przez [VibrationExplosion] podnosi Próg +1% (maks. 15%)
214. [Dar E.G.O [9214] — opis skrócony] 화상 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9214].simpleDesc[abilityID=9214].simpleDesc
   limit: do 120 znaków
   EN: Inflict Burn
   PL: — opis skrócony] Nakłada Podpalenie
215. [Dar E.G.O [9214] — opis skrócony] 진동 폭발 피해 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9214].simpleDesc[abilityID=92141].simpleDesc
   limit: do 120 znaków
   EN: Tremor Burst increases Stagger threshold further
   PL: — opis skrócony] Wybuch Wstrząsu dodatkowo podnosi Próg Oszołomienia
216. [Dar E.G.O [9215] — nazwa] 붉은색 넥타이
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9215].name
   limit: do 40 znaków
   EN: Red Necktie
   PL: — nazwa] Czerwony Krawat
217. [Dar E.G.O [9215] — opis] [Combustion] 위력 또는 [Combustion] 횟수 또는 특수 화상을 부여하는 스킬 3의 합 위력 +2, 피해량 +30%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9215].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Skill 3 that inflicts [Combustion] Potency, Count, or 'Unique Burn': Clash Power +2 and deal +30% damage
   PL: — opis] Umiejętności 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zyskują Moc Starcia +2 i +30% obrażeń
218. [Dar E.G.O [9215] — opis skrócony] 합 위력, 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9215].simpleDesc[abilityID=9215].simpleDesc
   limit: do 120 znaków
   EN: Gain Clash Power and deal more damage
   PL: — opis skrócony] Zyskuje Moc Starcia i zadaje więcej obrażeń
219. [Dar E.G.O [9216] — nazwa] 제식 복장 - 리우 협회
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9216].name
   limit: do 40 znaków
   EN: Uniform - Liu Assoc.
   PL: — nazwa] Mundur - Stowarzyszenie Liu
220. [Dar E.G.O [9216] — opis] 턴 시작 시, [Combustion] 위력 또는 [Combustion] 횟수 또는 특수 화상을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n리우 협회 소속 인격의 기본 공격 스킬의 더하기 코인 위력 +2 (빼기 코인 스킬일 경우, 기본 위력 +(8/코인 수) (최소 1, 소수점 버림))\n\n[Combustion] 위력 또는 [Combustion] 횟수 또는 특수 화상을 부여하는 스킬 3이 아닌 스킬의 피해량 +20%. (E.G.O 스킬 포함)\n\n[Combustion] 위력 또는 [Combustion] 횟수 또는 특수 화상을 부여하는 스킬 3의 더하기 코인 위력 +1 (빼기 코인 스킬일 경우, 기본 위력 +(4/코인 수) (최소 1, 소수점 버림)), 피해량 +30%.\n- 동일한 소속 인격을 편성한 수당 해당 소속 인격의 해당 스킬 피해량 5% 증가 (최대 20%, 대기 인원 포함)\n\n턴 종료 시 정신력이 가장 낮은 아군 2명의 정신력 8 회복\n- 대상의 정신력이 0 이하면, 추가로 5 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9216].desc
   limit: do 1120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Combustion] Potency, Count, or 'Unique Burn'. (except E.G.O Skills; except Backup Units)\n\nLiu Association Identities: Base Attack Skills gain Plus Coin Power +2 (Minus Coin Skills gain Base Power +(8 / # of Coins) (min 1; rounded down))\n\nNon-Skill 3 Skills (including E.G.O Skills) that inflict [Combustion] Potency, Count or 'Unique Burn' deal +20% damage\n\nSkill 3 that inflicts [Combustion] Potency, Count, or 'Unique Burn' gain Plus Coin Power +1 (Minus Coin Skills gain Base Power +(4 / # of Coins) (min 1; rounded down)) and deal +30% damage \n- Identities in a faction deal +5% damage for every same-faction Identity in the Team (max 20%; including Backup Units)\n\nTurn End: 2 allies with the least SP heal 8 SP\n- If affected allies are at 0 SP or lower, heal 5 additional SP
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; bez jednostek zapasowych)\n\nPodstawowe Umiejętności ataku Tożsamości Stowarzyszenia Liu zyskują Moc Monety Plus +2 (Umiejętności monety Minus zyskują Moc Bazową +(8/liczba monet) (min. 1, zaokrąglając w dół))\n\nUmiejętności inne niż Umiejętność 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zadają +20% obrażeń (wliczając Umiejętności E.G.O).\n\nUmiejętności 3 nakładające Moc [Combustion], Liczniki [Combustion] lub Szczególne Podpalenie zyskują Moc Monety Plus +1 (Umiejętności monety Minus zyskują Moc Bazową +(4/liczba monet) (min. 1, zaokrąglając w dół)) i zadają +30% obrażeń.\n- Za każdą Tożsamość tego samego Stowarzyszenia w zespole Umiejętności te zadają +5% obrażeń (maks. 20%, z jednostkami zapasowymi)\n\nNa koniec tury 2 sojuszników o najniższej Poczytalności odzyskuje 8 Poczytalności\n- Jeżeli Poczytalność celu wynosi 0 lub mniej, odzyskuje dodatkowo 5
221. [Dar E.G.O [9216] — opis skrócony] 스킬 위력, 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9216].simpleDesc[abilityID=9216].simpleDesc
   limit: do 120 znaków
   EN: Gain Skill Power and deal more damage
   PL: — opis skrócony] Umiejętności zyskują Moc i zadają więcej obrażeń
222. [Dar E.G.O [9217] — nazwa] 누군가의 단말기
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9217].name
   limit: do 40 znaków
   EN: Someone's Device
   PL: — nazwa] Czyjeś Urządzenie
223. [Dar E.G.O [9217] — opis] 공격 종료 시 [IndexPrescriptTargetToEnemy]이 사망했으면, [IndexPrescriptTargetToEnemy]을 처치한 아군이 다음 턴에 [AzureResultUp] 1 얻고 생존한 무작위 적 1명의 [Sinking] 횟수 3 증가 (턴당 1회)\n- [IndexPrescriptTargetToEnemy]을 처치한 아군이 검지 소속 인격이면, [AzureResultUp] 대신 다음 턴에 [Enhancement] 1 얻음. (턴당 1회)\n\n턴 종료 시 검지 소속이면, 최대 체력의 (보유한 [KarmaOfIndexAlly] 수치)%만큼 피해를 입음.\n(이 효과로 흐트러짐 상태가 되지 않으며, 최대 체력의 20% 미만으로 체력이 감소하지 않음)\n이후 해당 효과로 피해를 입은 인격이 다음 턴에 (보유한 [KarmaOfIndexAlly] 수치/5) 만큼 [ResultEnhancement] 얻음 (최대 2)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9217].desc
   limit: do 900 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToEnemy], [AzureResultUp], [Sinking], [Enhancement], [KarmaOfIndexAlly], [ResultEnhancement]
   znaczenie tagów: [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target; [AzureResultUp] = 우울 위력 증가 / Gloom Power Up; [Sinking] = 침잠 / Sinking; [Enhancement] = 공격 위력 증가 / Attack Power Up; [KarmaOfIndexAlly] = 카르마 / Karmic Consequence; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Attack End: If [IndexPrescriptTargetToEnemy] is killed, the Identity who attacked and killed [IndexPrescriptTargetToEnemy] gains 1 [AzureResultUp] next turn; inflict +3 [Sinking] Count to 1 random surviving enemy (once per turn)\n- If the unit that killed [IndexPrescriptTargetToEnemy] is in The Index faction, gain 1 [Enhancement] instead of [AzureResultUp] next turn (once per turn)\n\nTurn End: The Index faction units take ([KarmaOfIndexAlly] Stack on self)% HP damage.\n(Does not get Staggered due to this effect; this damage does not reduce the allies' HP below 20% HP)\nThen, Identities who took damage due to the above effect gain ([KarmaOfIndexAlly] Stack on self / 5) [ResultEnhancement] next turn (max 2)
   PL: — opis] Na koniec ataku, jeżeli [IndexPrescriptTargetToEnemy] ginie, sojusznik, który pokonał [IndexPrescriptTargetToEnemy], zyskuje 1 [AzureResultUp] na następną turę, a Liczniki [Sinking] 1 losowego przeżyłego wroga rosną o 3 (1 raz na turę)\n- Jeżeli sojusznikiem, który pokonał [IndexPrescriptTargetToEnemy], jest Tożsamość Wskazującego, zamiast [AzureResultUp] zyskuje 1 [Enhancement] na następną turę (1 raz na turę)\n\nNa koniec tury jednostki Wskazującego otrzymują obrażenia równe (posiadana wartość [KarmaOfIndexAlly])% Maks. HP.\n(Z powodu tego efektu nie ulega Oszołomieniu, a HP nie maleje poniżej 20% Maks. HP)\nNastępnie Tożsamość, która otrzymała obrażenia od tego efektu, zyskuje (posiadana wartość [KarmaOfIndexAlly]/5) [ResultEnhancement] na następną turę (maks. 2)
224. [Dar E.G.O [9217] — opis skrócony] 우울 위력 증가 얻음. 검지 소속이면 공격 위력 증가 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9217].simpleDesc[abilityID=9217].simpleDesc
   limit: do 120 znaków
   EN: Gain Gloom Power Up. The Index Identities gain Attack Power Up instead
   PL: — opis skrócony] Zyskuje Wzrost Mocy Posępności. Jeżeli Tożsamość jest z Wskazującego, zamiast tego Wzrost Mocy Ataku
225. [Dar E.G.O [9217] — opis skrócony] 검지 소속이면 피해를 입고, 다음 턴에 위력 증가 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9217].simpleDesc[abilityID=92171].simpleDesc
   limit: do 120 znaków
   EN: The Index Identities take damage and gain Power Up next turn
   PL: — opis skrócony] Tożsamości Wskazującego otrzymują obrażenia i zyskują Wzrost Mocy na następną turę
226. [Dar E.G.O [9218] — nazwa] 지령의 보살핌
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9218].name
   limit: do 40 znaków
   EN: Providence of the Prescript
   PL: — nazwa] Opatrzność Nakazu
227. [Dar E.G.O [9218] — opis] 전 턴에 스킬 효과로 [Sinking], [Sinking] 횟수 또는 특수 침잠을 부여했으면, 턴 시작 시 [Breath] 위력 3 또는 [Breath] 횟수 2 얻음 (인격 별로 턴당 1회)\n\n이번 전투 동안 해당 효과로 [Breath]을 누적 3회 이상 얻었으면, 다음 턴 부터 해당 수감자의 크리티컬 피해량 +30%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9218].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Sinking], [Breath]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Breath] = 호흡 / Poise
   EN: Identities that inflicted [Sinking], [Sinking] Count, or 'Unique Sinking', gain 3 [Breath] or +2 [Breath] Count at Turn Start (once per turn per Identity)\n\nDuring the Encounter, if an Identity has gained [Breath] 3 times due to the above effect, starting from the next turn, the said Sinner deals +30% damage on Critical Hit
   PL: — opis] Tożsamości, które w poprzedniej turze nałożyły [Sinking], Liczniki [Sinking] lub Szczególne Zatonięcie efektem Umiejętności, na początku tury zyskują 3 Moc [Breath] lub 2 Liczniki [Breath] (1 raz na turę na Tożsamość)\n\nJeżeli w tej walce Tożsamość zyskała dzięki temu efektowi [Breath] łącznie 3 razy lub więcej, począwszy od następnej tury ten Grzesznik zadaje +30% obrażeń Trafieniami Krytycznymi
228. [Dar E.G.O [9218] — opis skrócony] 호흡 위력, 횟수 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9218].simpleDesc[abilityID=9218].simpleDesc
   (powtórzenie elementu 159 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Dar E.G.O [9218] — opis skrócony] 크리티컬 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9218].simpleDesc[abilityID=92181].simpleDesc
   (powtórzenie elementu 160 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Dar E.G.O [9219] — nazwa] 만능 도구
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9219].name
   limit: do 40 znaków
   EN: Omni-tool
   PL: — nazwa] Uniwersalne Narzędzie
231. [Dar E.G.O [9219] — opis] 적에게 동일한 공격 유형의 스킬이 12번 적중 할 시 해당 공격 유형의 물리 내성 +0.1 (환상체일 경우 모든 부위, 적 별로 전투당 3회 적용, 이 효과로 내성은 2.0 초과가 될 수 없음)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9219].desc
   limit: do 280 znaków
   EN: When Skills of the same Attack Type hit an enemy 12 times, the enemy gains +0.1 Resistance against that Attack Type (3 times per Encounter per enemy/Abnormality Parts; this effect cannot raise Resistance value over 2.0)
   PL: — opis] Gdy wroga trafią 12 razy Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)
232. [Dar E.G.O [9219] — opis skrócony] 물리 내성 약화
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9219].simpleDesc[abilityID=9219].simpleDesc
   limit: do 120 znaków
   EN: Target becomes more vulnerable to an Attack Type
   PL: — opis skrócony] Cel staje się podatniejszy na dany typ ataku
233. [Dar E.G.O [19219] — nazwa] 만능 도구+
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19219].name
   limit: do 40 znaków
   EN: Omni-tool+
   PL: — nazwa] Uniwersalne Narzędzie+
234. [Dar E.G.O [19219] — opis] 적에게 동일한 공격 유형의 스킬이 <style="upgradeHighlight">9번</style> 적중 할 시 해당 공격 유형의 물리 내성 +0.1 (환상체일 경우 모든 부위, 적 별로 전투당 3회 적용, 이 효과로 내성은 2.0 초과가 될 수 없음)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19219].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>
   EN: When Skills of the same Attack Type hit an enemy <style="upgradeHighlight">9 times</style>, the enemy gains +0.1 Resistance against that Attack Type (3 times per Encounter per enemy/Abnormality Parts; this effect cannot raise Resistance value over 2.0)
   PL: — opis] Gdy wroga trafią <style="upgradeHighlight">9 razy</style> Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)
235. [Dar E.G.O [19219] — opis skrócony] 물리 내성 약화
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19219].simpleDesc[abilityID=19219].simpleDesc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Dar E.G.O [29219] — nazwa] 만능 도구++
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29219].name
   limit: do 40 znaków
   EN: Omni-tool++
   PL: — nazwa] Uniwersalne Narzędzie++
237. [Dar E.G.O [29219] — opis] 적에게 동일한 공격 유형의 스킬이 <style="upgradeHighlight">6번</style> 적중 할 시 해당 공격 유형의 물리 내성 +0.1 (환상체일 경우 모든 부위, 적 별로 전투당 3회 적용, 이 효과로 내성은 2.0 초과가 될 수 없음)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29219].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>
   EN: When Skills of the same Attack Type hit an enemy <style="upgradeHighlight">6 times</style>, the enemy gains +0.1 Resistance against that Attack Type (3 times per Encounter per enemy/Abnormality Parts; this effect cannot raise Resistance value over 2.0)
   PL: — opis] Gdy wroga trafią <style="upgradeHighlight">6 razy</style> Umiejętności tego samego typu ataku, jego odporność fizyczna na ten typ ataku +0,1 (w przypadku Anomalii — wszystkie Partie; 3 razy na walkę na wroga; dzięki temu efektowi odporność nie może przekroczyć 2.0)
238. [Dar E.G.O [29219] — opis skrócony] 물리 내성 약화
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29219].simpleDesc[abilityID=29219].simpleDesc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Dar E.G.O [9220] — nazwa] 도둑맞은 해결사 잡지
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9220].name
   limit: do 40 znaków
   EN: Stolen Fixer Magazine
   PL: — nazwa] Skradzione Czasopismo Fixerów
240. [Dar E.G.O [9220] — opis] 턴 시작 시, [HitResultUp] 1 얻음\n\n질투 완전 공명을 발동하였다면, 전투 시작 시 [HitDamageUp] 1 얻음\n\n중지 소속 인격이 4인 이상 있다면, 스테이지 시작 시 무작위 적 1명에게 [RetaliationBook] 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9220].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [HitResultUp], [HitDamageUp], [RetaliationBook]
   znaczenie tagów: [HitResultUp] = 타격 위력 증가 / Blunt Power Up; [HitDamageUp] = 타격 피해량 증가 / Blunt DMG Up; [RetaliationBook] = 앙갚음 대상 / Vengeance Mark
   EN: Turn Start: Gain 1 [HitResultUp]\n\nCombat Start: Gain 1 [HitDamageUp] if Envy A-Reson. is activated\n\nEncounter Start: If there are 4 or more The Middle-faction Identities on the battlefield, apply [RetaliationBook] to a random enemy
   PL: — opis] Na początku tury zyskuje 1 [HitResultUp]\n\nPrzy wywołaniu Pełnego Rezonansu Zazdrości, zyskuje na początku walki 1 [HitDamageUp]\n\nJeżeli na polu są co najmniej 4 Tożsamości Środkowego, na początku spotkania nakłada [RetaliationBook] na 1 losowego wroga
241. [Dar E.G.O [9221] — nazwa] 열선 무기
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9221].name
   limit: do 40 znaków
   EN: Thermal Weapon
   PL: Broń Termiczna
242. [Dar E.G.O [9221] — opis] 질투 속성 스킬 또는 반격 스킬 적중 시 [Laceration] 횟수 또는 [Combustion] 횟수 1 증가 (턴당 3회)\n\n전투 중 적의 [Laceration] 횟수가 1 아래로 떨어질 때, 해당 적이 보유한 [Combustion] 횟수가 2 이상이면, [Laceration] 횟수 대신 [Combustion] 횟수 감소 (턴당 3회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9221].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Combustion]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: On Hit with Envy Skill or Counter Skill, inflict +1 [Laceration] Count or +1 [Combustion] Count (3 times per turn)\n\nWhen [Laceration] Count on an enemy drops below 1 during combat, reduce [Combustion] Count instead if said enemy has 2+ [Combustion] Count (3 times per turn)
   PL: — opis] Przy trafieniu Umiejętnością Grzechu Zazdrości lub Umiejętnością Kontry, zwiększa Liczniki [Laceration] lub Liczniki [Combustion] o 1 (3 razy na turę)\n\nGdy w trakcie walki Liczniki [Laceration] wroga spadną poniżej 1, jeżeli ten wróg ma co najmniej 2 Liczniki [Combustion], zmniejsza zamiast tego Liczniki [Combustion] (3 razy na turę)
243. [Dar E.G.O [9221] — opis skrócony] 출혈, 화상 횟수 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9221].simpleDesc[abilityID=9221].simpleDesc
   limit: do 120 znaków
   EN: Inflict Bleed Count and Burn Count
   PL: — opis skrócony] Zwiększa Liczniki Krwawienia i Podpalenia
244. [Dar E.G.O [9221] — opis skrócony] 화상 횟수 감소
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9221].simpleDesc[abilityID=92211].simpleDesc
   limit: do 120 znaków
   EN: Reduce Burn Count
   PL: — opis skrócony] Zmniejsza Liczniki Podpalenia
245. [Dar E.G.O [9222] — nazwa] 새하얀 캔버스
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9222].name
   limit: do 40 znaków
   EN: Pure-white Canvas
   PL: — nazwa] Śnieżnobiałe Płótno
246. [Dar E.G.O [9222] — opis] [Laceration]이 15이상 있는 적에게 더하기 코인 공격 스킬 적중 시 정신력 3 회복 (인격 별로 턴당 1회)\n- 자신 혹은 대상이 부정적인 효과가 3개 이상이면, 대신 정신력 6 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9222].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: On Hit with Plus Coin Attack Skills against an enemy that has 15+ [Laceration], heal 3 SP (once per turn for each Identity)\n- If said Identity or target has 3+ types of negative effects, heal 6 SP instead
   PL: — opis] Przy trafieniu Umiejętnością ataku z monetą Plus wroga z co najmniej 15 [Laceration], odzyskuje 3 Poczytalności (1 raz na turę na Tożsamość)\n- Jeżeli ta Tożsamość lub cel ma co najmniej 3 ujemne efekty, zamiast tego odzyskuje 6 Poczytalności
247. [Dar E.G.O [9222] — opis skrócony] 정신력 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9222].simpleDesc[abilityID=9222].simpleDesc
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Dar E.G.O [9223] — nazwa] 범작
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9223].name
   limit: do 40 znaków
   EN: Average Artwork
   PL: — nazwa] Przeciętne Dzieło
249. [Dar E.G.O [9223] — opis] 약지 소속 인격이 [Inspire]을 얻음\n\n[Inspire]을 보유한 약지 소속 인격의 색욕 속성 또는 참격 속성 스킬이 적중한 적에게 다음 턴에 [ObjectOfExploration] 부여\n- 적이 [ObjectOfExploration]를 이미 보유했을 시, [ObjectOfExploration]이 [PaintingMaterial]로 교체됨\n\n[PaintingMaterial]가 있는 대상을 [Inspire]을 보유한 약지 소속 인격이 처치했으면, 다음 턴에 [PlusCoinValueUp] 1 얻음 (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9223].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [Inspire], [ObjectOfExploration], [PaintingMaterial], [PlusCoinValueUp]
   znaczenie tagów: [Inspire] = 영감 / Spark of Inspiration; [ObjectOfExploration] = 탐구 대상 / Curio; [PaintingMaterial] = 그림 재료 / Art Medium; [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: The Ring-faction Identities gain [Inspire]\n\nIf The Ring-faction Identity with [Inspire] hits an enemy with Lust or Slash Skills, inflict [ObjectOfExploration] on said enemy next turn\n- If the enemy already has [ObjectOfExploration], replace [ObjectOfExploration] with [PaintingMaterial]\n\nIf The Ring-faction Identity with [Inspire] kills an enemy that has [PaintingMaterial], said Identity gains 1 [PlusCoinValueUp] next turn (once per turn)
   PL: — opis] Tożsamości Serdecznego zyskują [Inspire]\n\nWrogowie trafieni Umiejętnościami Grzechu Żądzy lub Cięcia Tożsamości Serdecznego z [Inspire] otrzymują [ObjectOfExploration] na następną turę\n- Jeżeli wróg już posiada [ObjectOfExploration], [ObjectOfExploration] zostaje zastąpiony [PaintingMaterial]\n\nJeżeli Tożsamość Serdecznego z [Inspire] pokona cel z [PaintingMaterial], zyskuje 1 [PlusCoinValueUp] na następną turę (1 raz na turę)
250. [Dar E.G.O [9223] — opis skrócony] [ObjectOfExploration] 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9223].simpleDesc[abilityID=9223].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ObjectOfExploration]
   znaczenie tagów: [ObjectOfExploration] = 탐구 대상 / Curio
   EN: Inflict [ObjectOfExploration]
   PL: — opis skrócony] Nakłada [ObjectOfExploration]
251. [Dar E.G.O [9223] — opis skrócony] [PlusCoinValueUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9223].simpleDesc[abilityID=92231].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PlusCoinValueUp]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost
   EN: Gain [PlusCoinValueUp]
   PL: — opis skrócony] Zyskuje [PlusCoinValueUp]
252. [Dar E.G.O [9224] — nazwa] 수작
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9224].name
   limit: do 40 znaków
   EN: Exquisite Artwork
   PL: — nazwa] Mistrzowskie Dzieło
253. [Dar E.G.O [9224] — opis] 약지 소속 인격이 [Inspire]을 얻음\n\n[Inspire]을 보유한 약지 소속 인격의 공격 스킬이 적중한 적에게 [ObjectOfExploration] 부여\n- 적이 [ObjectOfExploration]를 이미 보유했을 시, [ObjectOfExploration]이 [PaintingMaterial]로 교체됨\n\n[PaintingMaterial]가 있는 대상을 [Inspire]을 보유한 약지 소속 인격이 처치했으면,\n해당 약지 소속 인격이 [Inspire]을 잃고 [GreatAesthetics]을 얻음\n\n[Laceration]이 15이상 있는 적에게 더하기 코인 공격 스킬 적중 시 정신력 3 회복 (인격 별로 턴당 1회)\n- 자신 혹은 대상이 부정적인 효과가 3개 이상이면, 대신 정신력 6 회복
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9224].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n, [Inspire], [ObjectOfExploration], [PaintingMaterial], [GreatAesthetics], [Laceration]
   znaczenie tagów: [Inspire] = 영감 / Spark of Inspiration; [ObjectOfExploration] = 탐구 대상 / Curio; [PaintingMaterial] = 그림 재료 / Art Medium; [GreatAesthetics] = 훌륭한 미감 / Exquisite Aesthetics; [Laceration] = 출혈 / Bleed
   EN: The Ring-faction Identities gain [Inspire]\n\nIf The Ring-faction Identity with [Inspire] hits an enemy, inflict [ObjectOfExploration] on said enemy\n- If the enemy already has [ObjectOfExploration], replace [ObjectOfExploration] with [PaintingMaterial]\n\nIf The Ring-faction Identity with [Inspire] kills an enemy that has [PaintingMaterial], said Identity loses [Inspire] and gains [GreatAesthetics]\n\nOn Hit with Plus Coin Attack Skills against an enemy that has 15+ [Laceration], heal 3 SP (once per turn for each Identity)\n- If said Identity or target has 3+ types of negative effects, heal 6 SP instead
   PL: — opis] Tożsamości Serdecznego zyskują [Inspire]\n\nWrogowie trafieni Umiejętnościami ataku Tożsamości Serdecznego z [Inspire] otrzymują [ObjectOfExploration]\n- Jeżeli wróg już posiada [ObjectOfExploration], [ObjectOfExploration] zostaje zastąpiony [PaintingMaterial]\n\nJeżeli Tożsamość Serdecznego z [Inspire] pokona cel z [PaintingMaterial],\nta Tożsamość Serdecznego traci [Inspire] i zyskuje [GreatAesthetics]\n\nPrzy trafieniu Umiejętnością ataku z monetą Plus wroga z co najmniej 15 [Laceration], odzyskuje 3 Poczytalności (1 raz na turę na Tożsamość)\n- Jeżeli ta Tożsamość lub cel ma co najmniej 3 ujemne efekty, zamiast tego odzyskuje 6 Poczytalności
254. [Dar E.G.O [9224] — opis skrócony] [Inspire] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9224].simpleDesc[abilityID=9224].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Inspire]
   znaczenie tagów: [Inspire] = 영감 / Spark of Inspiration
   EN: Gain [Inspire]
   PL: — opis skrócony] Zyskuje [Inspire]
255. [Dar E.G.O [9224] — opis skrócony] [ObjectOfExploration] 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9224].simpleDesc[abilityID=92241].simpleDesc
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Dar E.G.O [9224] — opis skrócony] [GreatAesthetics] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9224].simpleDesc[abilityID=92242].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GreatAesthetics]
   znaczenie tagów: [GreatAesthetics] = 훌륭한 미감 / Exquisite Aesthetics
   EN: Gain [GreatAesthetics]
   PL: — opis skrócony] Zyskuje [GreatAesthetics]
257. [Dar E.G.O [9225] — nazwa] 거미줄
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9225].name
   limit: do 40 znaków
   EN: The Spider's Thread
   PL: Pajęcza Nić
258. [Dar E.G.O [9225] — opis] 수비 스킬 사용 시 다음 턴에 스킬 3 피해량 +10% (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9225].desc
   limit: do 120 znaków
   EN: Allies who use Defense Skill deal +10% damage with Skill 3 next turn (once per turn)
   PL: — opis] Przy użyciu Umiejętności obronnej zyskuje +10% obrażeń Umiejętności 3 na następną turę (1 raz na turę)
259. [Dar E.G.O [9225] — opis skrócony] 스킬 3 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9225].simpleDesc[abilityID=9225].simpleDesc
   limit: do 120 znaków
   EN: Skill 3 deals more damage
   PL: — opis skrócony] Umiejętność 3 zadaje więcej obrażeń
260. [Dar E.G.O [19225] — nazwa] 거미줄+
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19225].name
   limit: do 40 znaków
   EN: The Spider's Thread+
   PL: — nazwa] Pajęcza Nić+
261. [Dar E.G.O [19225] — opis] 수비 스킬 사용 시 다음 턴에 스킬 3 피해량 <style="upgradeHighlight">+15%</style> (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19225].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>
   EN: Allies who use Defense Skill deal <style="upgradeHighlight">+15%</style> damage with Skill 3 next turn (once per turn)
   PL: — opis] Przy użyciu Umiejętności obronnej zyskuje <style="upgradeHighlight">+15%</style> obrażeń Umiejętności 3 na następną turę (1 raz na turę)
262. [Dar E.G.O [19225] — opis skrócony] 스킬 3 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=19225].simpleDesc[abilityID=19225].simpleDesc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Dar E.G.O [29225] — nazwa] 거미줄++
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29225].name
   limit: do 40 znaków
   EN: The Spider's Thread++
   PL: — nazwa] Pajęcza Nić++
264. [Dar E.G.O [29225] — opis] 수비 스킬 사용 시 다음 턴에 스킬 3 피해량 <style="upgradeHighlight">+20%</style> (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29225].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>
   EN: Allies who use Defense Skill deal <style="upgradeHighlight">+20%</style> damage with Skill 3 next turn (once per turn)
   PL: — opis] Przy użyciu Umiejętności obronnej zyskuje <style="upgradeHighlight">+20%</style> obrażeń Umiejętności 3 na następną turę (1 raz na turę)
265. [Dar E.G.O [29225] — opis skrócony] 스킬 3 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=29225].simpleDesc[abilityID=29225].simpleDesc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Dar E.G.O [9226] — nazwa] 누군가의 푸른 검
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9226].name
   limit: do 40 znaków
   EN: Someone's Azure Blade
   PL: — nazwa] Czyjś Błękitny Miecz
267. [Dar E.G.O [9226] — opis] 전투 시작 시 보호막이 있으면, [CriticalDamageUp] 1 얻음\n아군의 스킬이 크리티컬 적중 시, 다음 턴에 해당 아군이 ([Breath] 수치/5)만큼 보호막을 얻음 (최대 15)\n\n[거미집 소지 제자 싱클레어 전용 효과]\n전투 종료 시, 자신의 [Breath] 횟수가 30을 초과하면, [Breath] 횟수를 10 소모하여 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림 (턴당 1회)\nE.G.O 기프트 ‘캐스크 스피리츠’의 효과 중 전투 종료 시, 자신의 [Breath] 위력이 40을 초과하면, [Breath] 위력을 15 소모하여 자신의 모든 스킬 슬롯에서 등급이 가장 낮은 스킬 1개를 버림 효과를 적용 받지 않음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9226].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n, [CriticalDamageUp], [Breath]
   znaczenie tagów: [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up; [Breath] = 호흡 / Poise
   EN: Combat Start: Allies with Shield gain 1 [CriticalDamageUp]\nOn Crit with ally Skill, said ally gains Shield equal to ([Breath] / 5) for the next turn (max 15)\n\n[The House of Spiders: The Pinky Apprentice Sinclair exclusive effect]\nCombat End: At more than 30 [Breath] Count, consume 10 [Breath] Count to Discard 1 Skill of the lowest Rank in all of this unit's Skill Slots (once per turn)\n\nAmong the E.G.O Gift "Cask Spirits" effects, the following does not apply to this unit:\n"Combat End: at more than 40 [Breath] Potency, consume 15 [Breath] Potency to Discard 1 Skill of the lowest rank in all of that unit's Skill Slots (once per turn for each character)"
   PL: — opis] Na początku walki sojusznicy z Tarczą zyskują 1 [CriticalDamageUp]\nPrzy trafieniu Umiejętnością sojusznika z Trafieniem Krytycznym, ta Tożsamość zyskuje Tarczę równą (wartość [Breath]/5) na następną turę (maks. 15)\n\n[Efekt wyłącznie dla Domu Pajęczyn: Ucznia Małego Palca Sinclaira]\nNa koniec walki, jeżeli Liczniki [Breath] przekraczają 30, zużywa 10 Liczników [Breath], by odrzucić 1 Umiejętność o najniższej Randze ze wszystkich swoich slotów Umiejętności (1 raz na turę)\nNie stosuje efektu Daru E.G.O „Trunek z Beczki”: na koniec walki, jeżeli Moc [Breath] przekracza 40, zużycia 15 Mocy [Breath], by odrzucić 1 Umiejętność o najniższej Randze ze wszystkich swoich slotów Umiejętności
268. [Dar E.G.O [9226] — opis skrócony] [CriticalDamageUp] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9226].simpleDesc[abilityID=9226].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalDamageUp]
   znaczenie tagów: [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: Gain [CriticalDamageUp]
   PL: — opis skrócony] Zyskuje [CriticalDamageUp]
269. [Dar E.G.O [9226] — opis skrócony] 보호막 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9226].simpleDesc[abilityID=92261].simpleDesc
   limit: do 120 znaków
   EN: Gain Shield
   PL: Zyskuje Tarczę
270. [Dar E.G.O [9226] — opis skrócony] 거미집 소지 제자 싱클레어 전용 효과
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9226].simpleDesc[abilityID=92262].simpleDesc
   limit: do 120 znaków
   EN: The House of Spiders: The Pinky Apprentice Sinclair exclusive effect
   PL: — opis skrócony] Efekt wyłącznie dla Domu Pajęczyn: Ucznia Małego Palca Sinclaira
271. [Dar E.G.O [9227] — nazwa] 귀기 서린 환도
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9227].name
   limit: do 40 znaków
   EN: Baleful Hwando
   PL: — nazwa] Hwando Przesiąknięte Złem
272. [Dar E.G.O [9227] — opis] 전투를 6회 승리할 시 해당 E.G.O 기프트가 변경됨\n{0}\n\n모든 아군이 받는 피해 20% 증가, 합위력 -1
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9227].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: This E.G.O Gift changes after 6 Encounter wins\n{0}\n\nFor all allies: Take +20% damage, Clash Power -1
   PL: — opis] Po 6 wygranych walkach ten Dar E.G.O się zmienia\n{0}\n\nWszyscy sojusznicy otrzymują +20% obrażeń, Moc Starcia maleje o 1
273. [Dar E.G.O [9227] — opis skrócony] 받는 피해 증가, 합위력 감소
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9227].simpleDesc[abilityID=9227].simpleDesc
   limit: do 120 znaków
   EN: Take more damage and lose Clash Power
   PL: — opis skrócony] Otrzymuje więcej obrażeń i traci Moc Starcia
274. [Dar E.G.O [9228] — nazwa] 신검합일
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9228].name
   limit: do 40 znaków
   EN: One with the Blade
   PL: — nazwa] Jedność z Ostrzem
275. [Dar E.G.O [9228] — opis] 모든 아군이 가하는 피해 25% 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9228].desc
   limit: do 120 znaków
   EN: All allies deal +25% damage
   PL: — opis] Wszyscy sojusznicy zadają +25% obrażeń
276. [Dar E.G.O [9228] — opis skrócony] 가하는 피해 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9228].simpleDesc[abilityID=9228].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage
   PL: — opis skrócony] Zadaje więcej obrażeń
277. [Dar E.G.O [9229] — nazwa] 빛바랜 건틀릿
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9229].name
   limit: do 40 znaków
   EN: Tarnished Gauntlet
   PL: — nazwa] Wyblakły Gauntlet
278. [Dar E.G.O [9229] — opis] 전투를 6회 승리할 시 해당 E.G.O 기프트가 변경됨\n{0}\n\n모든 아군의 속도 최소, 최댓값 5 감소 (1미만으로 내려가지 않음)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9229].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: This E.G.O Gift changes after 6 Encounter wins\n{0}\n\nMin & Max Speed -5 for all allies (this effect cannot reduce Speed below 1)
   PL: — opis] Po 6 wygranych walkach ten Dar E.G.O się zmienia\n{0}\n\nMin. i Maks. Szybkość wszystkich sojuszników maleje o 5 (nie maleje poniżej 1)
279. [Dar E.G.O [9229] — opis skrócony] 속도 감소
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9229].simpleDesc[abilityID=9229].simpleDesc
   limit: do 120 znaków
   EN: Reduce Speed
   PL: — opis skrócony] Zmniejsza Szybkość
280. [Dar E.G.O [9230] — nazwa] 황금빛 시간
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9230].name
   limit: do 40 znaków
   EN: Golden Hour
   PL: — nazwa] Złota Godzina
281. [Dar E.G.O [9230] — opis] 모든 아군의 속도 최소, 최댓값 3 증가\n자신보다 속도가 4 이상 느린 대상에게 스킬의 최종 위력 +2\n적에게 공격 적중 시 다음 턴에 속박 1 부여 (턴당 4회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9230].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Min & Max Speed +3 for all allies\nFinal Power +2 when using Skills against slower targets with 4+ Speed difference\nOn Hit against an enemy, inflict 1 Bind next turn (4 times per turn)
   PL: — opis] Min. i Maks. Szybkość wszystkich sojuszników rośnie o 3\nUmiejętności zyskują Moc Końcową +2 na celach wolniejszych o co najmniej 4 Szybkości\nPrzy trafieniu atakiem wroga, nakłada 1 Spętania na następną turę (4 razy na turę)
282. [Dar E.G.O [9230] — opis skrócony] 속도 증가, 최종 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9230].simpleDesc[abilityID=9230].simpleDesc
   limit: do 120 znaków
   EN: Gain Speed and Final Power
   PL: — opis skrócony] Zwiększa Szybkość i Moc Końcową
283. [Dar E.G.O [9231] — nazwa] 그날의 기록
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9231].name
   limit: do 40 znaków
   EN: Record Logs of That Day
   PL: — nazwa] Zapisy Tamtego Dnia
284. [Dar E.G.O [9231] — opis] 전투를 6회 승리할 시 해당 E.G.O 기프트가 변경됨\n{0}\n\n턴 시작 시 흐트러짐 상태가 아닌 무작위 아군 1명 강제 흐트러짐 발생
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9231].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: This E.G.O Gift changes after 6 Encounter wins\n{0}\n\nTurn Start: A random ally who is not Staggered enters a forced Stagger state
   PL: — opis] Po 6 wygranych walkach ten Dar E.G.O się zmienia\n{0}\n\nNa początku tury 1 losowy sojusznik nieoszołomiony doznaje wymuszonego Oszołomienia
285. [Dar E.G.O [9231] — opis skrócony] 흐트러짐
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9231].simpleDesc[abilityID=9231].simpleDesc
   limit: do 120 znaków
   EN: Gets Staggered
   PL: OSZOŁOMIENIE
286. [Dar E.G.O [9232] — nazwa] 가능성
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9232].name
   limit: do 40 znaków
   EN: Potentialities
   PL: Możliwości
287. [Dar E.G.O [9232] — opis] 피해로 인한 흐트러짐 상태가 되었을 때 흐트러짐 상태를 해제. 최대 체력의 50%만큼 보호막을 얻고, 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거\n(강제 흐트러짐 제외, 전투당 2회 발동)\n위 효과 발동 후 다음 턴 시작 시 호흡 위력 20 얻음 (턴당 1회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9232].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When Staggered due to damage, recover from Stagger; then gain Shield equal to 50% of Max HP and remove 1 random removable negative effect on self (excluding forced Staggers, 2 times per Encounter)\n\nGain 20 Poise at the start of the next turn after activating the above effect (once per turn)
   PL: — opis] Gdy jednostka ulega Oszołomieniu od obrażeń, wychodzi z Oszołomienia; zyskuje Tarczę równą 50% Maks. HP i usuwa 1 losowy ujemny efekt z odwracalnych nałożonych na siebie\n(poza wymuszonym Oszołomieniem; 2 razy na walkę)\nNa początku tury następującej po wywołaniu powyższego efektu zyskuje 20 Mocy Oddechu (1 raz na turę)
288. [Dar E.G.O [9232] — opis skrócony] 흐트러짐 상태 해제, 부정적인 효과 제거
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9232].simpleDesc[abilityID=9232].simpleDesc
   limit: do 120 znaków
   EN: Recover from Stagger; remove negative effect
   PL: — opis skrócony] Wychodzi z Oszołomienia; usuwa ujemny efekt
289. [Dar E.G.O [9242] — nazwa] 봉이 인형
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9242].name
   limit: do 40 znaków
   EN: Bongy Plush
   PL: Pluszak Bongy
290. [Dar E.G.O [9242] — opis] 층 클리어 시 보유한 코스트가 1.5배씩 늘어남\n\n- 보유한 기프트 개수 1개당, 피해량 0.5% 증가 (현재 {0}%. 최대 100%)\n- 보유한 기프트 개수 20개당, 턴 시작 시 [Enhancement] 1 얻음 (현재 {1} 얻음. 최대 10)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9242].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Multiply Cost owned by 1.5 upon clearing a Floor\n\n- Deal +0.5% damage for every E.G.O Gift owned (Current: +{0}%; max 100%)\n- Turn Start: Gain 1 [Enhancement] for every 20 E.G.O Gift owned (Current Stack: {1}; max 10)
   PL: — opis] Po ukończeniu piętra posiadany Koszt rośnie 1,5 razy\n\n- Za każdy posiadany Dar E.G.O obrażenia +0,5% (obecnie {0}%. maks. 100%)\n- Za każde 20 posiadanych Darów E.G.O na początku tury zyskuje 1 [Enhancement] (obecnie zyskuje {1}. maks. 10)
291. [Dar E.G.O [9242] — opis skrócony] 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9242].simpleDesc[abilityID=9242].simpleDesc
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
292. [Dar E.G.O [9242] — opis skrócony] [Enhancement] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9242].simpleDesc[abilityID=92421].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Gain [Enhancement]
   PL: — opis skrócony] Zyskuje [Enhancement]
293. [Dar E.G.O [9256] — nazwa] 불완전한 예지안
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9256].name
   limit: do 50 znaków
   EN: Imperfect Eye of Precognition
   PL: — nazwa] Niedoskonałe Oko Prekognicji
294. [Dar E.G.O [9256] — opis] 아군이 사용하는 스킬의 코인 위력 +(8/ 코인 수) (더하기 코인 적용), 최종 위력 +(8 / 코인 수) (빼기 코인 적용) (최소 증가 값 1, 소수점 <noparse>버림</noparse>, E.G.O 스킬 포함)\n\n[편성 1번 인격 전용 효과]\n- 합 진행 시 매 합마다 자신이 [LookingFutureMirror] 1 얻음. 대상에게 [Vibration]과 [Combustion] 2 부여 (스킬당 최대 10회)\n- 합 승리 시 메인 타겟에게 [VibrationIgnition]로 [Switch_Vibration]하고, [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소\n- 스킬 적중 시 대상이 흐트러짐 상태라면, 가하는 피해량 +30%\n- 크리티컬 적중 시 [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소 (스킬당 2회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9256].desc
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [LookingFutureMirror], [Vibration], [Combustion], [VibrationIgnition], [Switch_Vibration], [VibrationExplosion]
   znaczenie tagów: [LookingFutureMirror] = 순간의 예지 / Glimpse of Precognition; [Vibration] = 진동 / Tremor; [Combustion] = 화상 / Burn; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: Allies' Plus Coin Skills: Gain Coin Power +(8 / # of Coins) (gains at least 1 Coin Power, includes E.G.O Skills; rounded down)\n\nAllies' Minus Coin Skills: Gain Final Power +(8 / # of Coins) (gains at least 1 Final Power, includes E.G.O Skills; rounded down)\n\n[Effects apply only to #1 Deployed Identity]\n- In a Clash, gain 1 [LookingFutureMirror] with every Clash. Inflict 2 [Vibration] and [Combustion] on target (10 times per Skill)\n- On Clash Win, trigger [Switch_Vibration] into [VibrationIgnition] and trigger [VibrationExplosion] on the main target. Target loses 1 [Vibration] Count\n- On Hit with a Skill, if target is Staggered, deal +30% damage\n- On Crit, trigger [VibrationExplosion]. Target loses 1 [Vibration] Count (2 times per Skill)
   PL: — opis] Umiejętności używane przez sojuszników zyskują Moc Monet +(8/liczba monet) (moneta Plus), Moc Końcową +(8/liczba monet) (moneta Minus) (minimalny wzrost 1, zaokrąglając w dół, wliczając Umiejętności E.G.O)\n\n[Efekt wyłącznie dla Tożsamości na Przydziale #1]\n- Przy Starciu zyskuje 1 [LookingFutureMirror] w każdym Starciu. Nakłada 2 [Vibration] i [Combustion] na cel (maks. 10 razy na Umiejętność)\n- Przy wygranej Starciu [Switch_Vibration] na [VibrationIgnition] głównego celu i [VibrationExplosion]. Liczniki [Vibration] celu maleją o 1\n- Przy trafieniu Umiejętnością, jeżeli cel jest oszołomiony, zadaje +30% obrażeń\n- Przy trafieniu Trafieniem Krytycznym [VibrationExplosion]. Liczniki [Vibration] celu maleją o 1 (2 razy na Umiejętność)
295. [Dar E.G.O [9257] — nazwa] 남겨진 신탁
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].name
   limit: do 40 znaków
   EN: The Abandoned Oracle
   PL: — nazwa] Porzucona Wyrocznia
296. [Dar E.G.O [9257] — opis] 아군이 사용하는 스킬의 코인 위력 +(8/ 코인 수) (더하기 코인 적용), 최종 위력 +(8 / 코인 수) (빼기 코인 적용) (최소 증가 값 1, 소수점 <noparse>버림</noparse>, E.G.O 스킬 포함)\n\n합 진행 시, 대상의 [Sinking]과 자신의 [Breath]의 합 30당, 합 위력 +1 (최대 5)\n\n[SuperCoin]의 피해량 +25%\n[SuperCoin]으로 피해를 받을 때, 피해량 -25%,\n\n[검지 소속 인격 전용 효과]\n- 전장에 처음으로 등장할 때, [BlessingOfIndexPrescriptAlly] 6 얻음\n· [UnlockBuff_Base]을 획득 가능한 인격일 경우, 추가로 [UnlockBuffAlly_2] 얻음\n- [IndexPrescriptTargetToEnemy]을 보유한 적에게 입히는 피해량 +50%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].desc
   limit: do 880 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Sinking], [Breath], [SuperCoin], [BlessingOfIndexPrescriptAlly], [UnlockBuff_Base], [UnlockBuffAlly_2], [IndexPrescriptTargetToEnemy]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [Breath] = 호흡 / Poise; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin; [BlessingOfIndexPrescriptAlly] = 지령의 가호 / Grace of the Prescript; [UnlockBuff_Base] = 해금 / Unlock; [UnlockBuffAlly_2] = 해금 - II / Unlock - II; [IndexPrescriptTargetToEnemy] = 지령 대상 / The Prescript's Target
   EN: Allies' Plus Coin Skills: Gain Coin Power +(8 / # of Coins) (gains at least 1 Coin Power, includes E.G.O Skills; rounded down)\n\nAllies' Minus Coin Skills: Gain Final Power +(8 / # of Coins) (gains at least 1 Final Power, includes E.G.O Skills; rounded down)\n\nIn a Clash, gain Clash Power +1 for every 30 ([Sinking] on target + [Breath] on self) (max 5)\n\nDeal +25% damage with [SuperCoin]s\nTake -25% damage from [SuperCoin]s\n\n[The Index-faction Exclusive Effect]\n- Upon entering the Encounter for the first time, gain 6 [BlessingOfIndexPrescriptAlly]\n· If the unit is an Identity that can gain [UnlockBuff_Base], gain [UnlockBuffAlly_2] as well\n- Deal +50% damage against [IndexPrescriptTargetToEnemy]
   PL: — opis] Umiejętności używane przez sojuszników zyskują Moc Monet +(8/liczba monet) (moneta Plus), Moc Końcową +(8/liczba monet) (moneta Minus) (minimalny wzrost 1, zaokrąglając w dół, wliczając Umiejętności E.G.O)\n\nPrzy Starciu Moc Starcia +1 za każdą sumę 30 (Moc [Sinking] celu + Moc [Breath] jednostki) (maks. 5)\n\nObrażenia [SuperCoin] +25%\nObrażenia otrzymywane od [SuperCoin] -25%,\n\n[Efekt wyłącznie dla Tożsamości Wskazującego]\n- Przy pierwszym pojawieniu się na polu zyskuje 6 [BlessingOfIndexPrescriptAlly]\n· Jeżeli Tożsamość może zdobyć [UnlockBuff_Base], dodatkowo zyskuje [UnlockBuffAlly_2]\n- Zadaje +50% obrażeń wrogom z [IndexPrescriptTargetToEnemy]
297. [Dar E.G.O [9257] — opis skrócony] 아군의 코인 위력 또는 최종 위력이 크게 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].simpleDesc[abilityID=98270].simpleDesc
   limit: do 120 znaków
   EN: Allies gain a significant amount of Coin Power or Final Power
   PL: — opis skrócony] Sojusznicy znacząco zyskują Moc Monet lub Moc Końcową
298. [Dar E.G.O [9257] — opis skrócony] 대상의 침잠과 자신의 호흡의 합에 비례하여 합 위력 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].simpleDesc[abilityID=9257].simpleDesc
   limit: do 120 znaków
   EN: Gain Clash Power based on the sum of Sinking on target and Poise on self
   PL: — opis skrócony] Zyskuje Moc Starcia proporcjonalnie do sumy Zatonięcia celu i Oddechu jednostki
299. [Dar E.G.O [9257] — opis skrócony] 파괴 불가 코인의 피해량 +25%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].simpleDesc[abilityID=92571].simpleDesc
   limit: do 120 znaków
   EN: Deal +25% damage with Unbreakable Coins
   PL: — opis skrócony] Zadaje +25% obrażeń Niezniszczalnymi Monetami
300. [Dar E.G.O [9257] — opis skrócony] 지령 대상을 보유한 적에게 가하는 피해량 +50%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9257].simpleDesc[abilityID=92572].simpleDesc
   limit: do 120 znaków
   EN: Deal +50% damage against The Prescript's Target
   PL: — opis skrócony] Zadaje +50% obrażeń wrogom z Celem Nakazu
301. [Dar E.G.O [9258] — nazwa] 앙갚음 장부 : 번외
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9258].name
   limit: do 40 znaków
   EN: The Book of Vengeance: Annex
   PL: — nazwa] Księga Zemsty : Aneks
302. [Dar E.G.O [9258] — opis] 아군이 사용하는 스킬의 코인 위력 +(8/ 코인 수) (더하기 코인 적용), 최종 위력 +(8 / 코인 수) (빼기 코인 적용) (최소 증가 값 1, 소수점 <noparse>버림</noparse>, E.G.O 스킬 포함)\n\n스테이지 시작시 전장에 있는 중지 소속 아군 1명당 모든 아군이 보호막 50씩 얻음 (대기 인원 미포함, 이 효과로 획득한 보호막은 턴 종료시에도 사라지지 않음)\n\n 중지 소속 아군이 질투 속성이나 타격 속성 기본 스킬 공격 종료 시 입힌 스킬 피해량의 10%만큼 체력 회복\n- 반격 스킬로 발동했을 경우, 대신 입힌 스킬 피해량의 20%만큼 체력 회복\n- 초과된 체력 회복량은 보호막으로 획득함 (이 효과로 획득한 보호막은 턴 종료시에도 사라지지 않음)\n\n전투 시작시, 장착한 수비 스킬 수만큼 해당 턴 동안 중지 소속 아군의 공격 레벨이 증가 (최대 12)\n- 장착한 수비 스킬 수가 6 이상이면, 질투 속성 기본 스킬 피해량 +30%, 초과한 수비 스킬 수만큼 추가로 +10% (최대 추가 증가량 60%)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9258].desc
   limit: do 1320 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: Allies' Plus Coin Skills: Gain Coin Power +(8 / # of Coins) (gains at least 1 Coin Power, includes E.G.O Skills; rounded down)\n\nAllies' Minus Coin Skills: Gain Final Power +(8 / # of Coins) (gains at least 1 Final Power, includes E.G.O Skills; rounded down)\n\nEncounter Start: All allies gain 50 Shield for every The Middle-faction allied unit on the field (excluding Backup units; Shield gained via this effect does not expire at Turn End)\n\nAttack End with The Middle-faction allied units' Envy or Blunt Base Skills: Heal 10% of Skill damage dealt\n- If this effect is triggered by a Counter Skill, heal 20% of Skill damage dealt instead\n- Excess HP healed is converted into Shield (Shield gained via this effect does not expire at Turn End)\n\nCombat Start: The Middle-faction allied units gain Offense Level for the turn based on the number of Defense Skills equipped (max 12 Offense Level)\n- If 6+ Defense Skills are equipped, deal +30% damage with Envy Base Skills\n- Deal an additional +10% damage for every Defense Skill equipped beyond 6 (max 60%)
   PL: — opis] Umiejętności używane przez sojuszników zyskują Moc Monet +(8/liczba monet) (moneta Plus), Moc Końcową +(8/liczba monet) (moneta Minus) (minimalny wzrost 1, zaokrąglając w dół, wliczając Umiejętności E.G.O)\n\nNa początku spotkania wszyscy sojusznicy zyskują Tarczę 50 za każdą Tożsamość frakcji Środkowego na polu (bez jednostek zapasowych; Tarcza zdobyta dzięki temu efektowi nie znika na koniec tury)\n\nNa koniec ataku podstawową Umiejętnością Grzechu Zazdrości lub typu Uderzenia Tożsamości frakcji Środkowego odzyskuje HP równe 10% zadanych obrażeń Umiejętnością\n- Jeżeli wywołano Umiejętnością Kontry, odzyskuje zamiast tego HP równe 20% zadanych obrażeń Umiejętnością\n- Nadwyżka odzyskanego HP ponad Maks. HP jest zdobywana jako Tarcza (Tarcza zdobyta dzięki temu efektowi nie znika na koniec tury)\n\nNa początku walki Poziom Ataku Tożsamości frakcji Środkowego rośnie na czas tej tury w zależności od liczby założonych Umiejętności obronnych (maks. 12)\n- Jeżeli założone Umiejętności obronne to co najmniej 6, Umiejętności podstawowe Grzechu Zazdrości zadają +30% obrażeń, dodatkowo +10% za każdą Umiejętność obronną ponad warunek (maks. dodatkowy wzrost 60%)
303. [Dar E.G.O [9259] — nazwa] 작품이 된 마에스트로 링
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9259].name
   limit: do 50 znaków
   EN: A Maestro's Ring-Turned-Artwork
   PL: — nazwa] Pierścień Maestra Zamieniony w Dzieło
304. [Dar E.G.O [9259] — opis] 아군이 사용하는 스킬의 코인 위력 +(8/ 코인 수) (더하기 코인 적용), 최종 위력 +(8 / 코인 수) (빼기 코인 적용) (최소 증가 값 1, 소수점 <noparse>버림</noparse>, E.G.O 스킬 포함)\n\n약지 소속 인격이 기본 공격 스킬 사용 시, 대상에게 부여된 부정적인 효과의 개수에 따라 해당 스킬에 아래 효과 적용\n- 2 ~ : 합 위력 +2\n- 4 ~ : 피해량 +15%\n- 6 ~ : 코인 효과로 부여하는 부정적인 효과의 위력, 횟수 부여값 +1\n- 7 ~ : 기본 위력 +2\n- 8 ~ : 피해량 +35%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9259].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n
   EN: Allies' Plus Coin Skills: Gain Coin Power +(8 / # of Coins) (gains at least 1 Coin Power, includes E.G.O Skills; rounded down)\n\nAllies' Minus Coin Skills: Gain Final Power +(8 / # of Coins) (gains at least 1 Final Power, includes E.G.O Skills; rounded down)\n\nWhen The Ring-faction Identities use Base Attack Skills, apply the following effects based on the number of negative effect types on the target:\n- 2+: Clash Power +2\n- 4+: Deal +15% damage\n- 6+: Inflict +1 more Potency and Count of negative effects via Coin effects\n- 7+: Base Power +2\n- 8+: Deal +35% damage
   PL: — opis] Umiejętności używane przez sojuszników zyskują Moc Monet +(8/liczba monet) (moneta Plus), Moc Końcową +(8/liczba monet) (moneta Minus) (minimalny wzrost 1, zaokrąglając w dół, wliczając Umiejętności E.G.O)\n\nGdy Tożsamości Serdecznego użyją podstawowej Umiejętności ataku, stosuje na tej Umiejętności poniższe efekty w zależności od liczby ujemnych efektów nałożonych na cel:\n- 2+: Moc Starcia +2\n- 4+: obrażenia +15%\n- 6+: wartość ujemnych efektów nakładanych efektem Monety (Moc i Liczniki) +1\n- 7+: Moc Bazowa +2\n- 8+: obrażenia +35%
305. [Dar E.G.O [9250] — nazwa] 보급형 K사 앰플
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9250].name
   limit: do 40 znaków
   EN: Mid-range K Corp. Ampule
   PL: — nazwa] Ampułka Seryjna Korporacji K
306. [Dar E.G.O [9250] — opis] [편성 순서 1번 인격 전용 효과]\n스테이지 시작시, [KAmpouleMirror] 1 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9250].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [KAmpouleMirror]
   znaczenie tagów: [KAmpouleMirror] = 비상용 K사 앰플 / K Corp. Emergency Ampule
   EN: [Effects apply only to #1 Deployed Identity]\nEncounter Start: Gain 1 [KAmpouleMirror]
   PL: — opis] [Efekt wyłącznie dla Tożsamości przydzielonej na 1. pozycji]\nNa początku spotkania zyskuje 1 [KAmpouleMirror]
307. [Dar E.G.O [9251] — nazwa] 불타는 운명
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9251].name
   limit: do 40 znaków
   EN: Burning Fate
   PL: — nazwa] Płonący Los
308. [Dar E.G.O [9251] — opis] [Combustion] 위력 최댓값 +30\n\n[Combustion]을 보유한 대상과 합 승리시, 대상의 [Combustion] 1회 발동, 대상의 [Combustion] 횟수 1 감소 (인격당 1회)\n\n[Combustion]을 보유한 적에게 스킬 사용시, 메인 타겟의 ([Combustion] 위력 / 10) 만큼 해당 스킬의 공격 레벨이 증가 (최대 8)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9251].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Max [Combustion] Potency +30\n \nOn Clash Win against targets that have [Combustion], activate [Combustion] on target once and reduce the target's [Combustion] Count by 1 (once per Identity)\n\nOn Skill Use against enemies that have [Combustion], the said Skill gains Offense Level equal to ([Combustion] Potency on the main target / 10) (max 8)
   PL: — opis] Maks. Mocy [Combustion] +30\n\nPrzy wygranej Starciu z celem posiadającym [Combustion], wywołuje [Combustion] celu 1 raz, a Liczniki [Combustion] celu maleją o 1 (1 raz na Tożsamość)\n\nPrzy użyciu Umiejętności na wrogu posiadającym [Combustion], Poziom Ataku tej Umiejętności rośnie o (Moc [Combustion] głównego celu/10) (maks. 8)
309. [Dar E.G.O [9252] — nazwa] 못과 망치
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9252].name
   limit: do 40 znaków
   EN: Nail and Hammer
   PL: Nagel und Hammer
310. [Dar E.G.O [9252] — opis] N사 광신도 소속이면, 기본 스킬의 기본 위력 +3\n\nN사 광신도 소속 인격이 [AssemblePersonality]을 얻을 때, 모든 N사 광신도 소속 인격도 해당 수치만큼 [AssemblePersonality] 얻음 (턴당 1회, 본인 포함)\n- 색욕 완전 공명이 있으면, 부여량 3배로 적용\n\n스테이지 시작시 모든 적에게 [NailPersonality] 2 부여\n\nN사 광신도 소속 인격이 [NailPersonality]이 있는 대상과 기본 스킬로 합 진행 시 [Laceration] 3 부여 (스킬당 1회)\n\nN사 광신도 소속 인격이 [NailPersonality]이 있는 대상에게 기본 스킬로 가하는 피해량 +100%
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9252].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n, [AssemblePersonality], [NailPersonality], [Laceration]
   znaczenie tagów: [AssemblePersonality] = 광신 / Fanatic; [NailPersonality] = 못 / Nails; [Laceration] = 출혈 / Bleed
   EN: <noparse>N Corp. Fanatic</noparse> Identities: Base Skills gain Base Power +3\n\nWhen an <noparse>N Corp. Fanatic</noparse> Identity gains [AssemblePersonality], all <noparse>N Corp. Fanatic</noparse> Identities gain the same Stack of [AssemblePersonality] (once per turn including the first unit)\n- If there is a Lust A-Reson., triple the Stack gained\n\nEncounter Start: Inflict 2 [NailPersonality] on all enemies\n\nWhen an <noparse>N Corp. Fanatic</noparse> Identity uses a Base Skill to Clash against a target that has [NailPersonality], inflict 3 [Laceration] (once per Skill)\n\n<noparse>N Corp. Fanatic</noparse> Identities deal +100% damage using Base Skills against targets that have [NailPersonality]
   PL: — opis] Jeżeli Tożsamość jest Fanatykiem Korporacji N, podstawowe Umiejętności zyskują Moc Bazową +3\n\nGdy Tożsamość Fanatyka Korporacji N zyskuje [AssemblePersonality], wszystkie Tożsamości Fanatyków Korporacji N zyskują tę samą liczbę [AssemblePersonality] (1 raz na turę, wliczając jednostkę)\n- Przy Pełnym Rezonansie Żądzy wartość nakładana jest 3 razy większa\n\nNa początku spotkania nakłada 2 [NailPersonality] na wszystkich wrogów\n\nGdy Tożsamość Fanatyka Korporacji N prowadzi Starcie podstawową Umiejętnością z celem mającym [NailPersonality], nakłada 3 [Laceration] (1 raz na Umiejętność)\n\nTożsamości Fanatyków Korporacji N zadają +100% obrażeń podstawową Umiejętnością celom posiadającym [NailPersonality]
311. [Dar E.G.O [9253] — nazwa] 회전 목마 모형
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9253].name
   limit: do 40 znaków
   EN: Carousel Figurine
   PL: — nazwa] Figurka Karuzeli
312. [Dar E.G.O [9253] — opis] 첫 턴 시작시, [BloodDinner] 300 얻음\n[BloodDinner]이 [Laceration] 효과로 생성될 때 2배로 생성됨\n[BloodDinner]을 소모하는 스킬 사용시 해당 스킬에서 소모한 값만큼 공격 종료 시에 [BloodDinner]을 추가 소모함\n\n[라만차랜드 인격 전용 효과]\n라만차랜드 소속 인격 전투 참여 시, 인격에 따라 아래 효과 적용\n- 라만차랜드 실장 돈키호테: [BloodArmorPersonalityFirst] 15 얻음\n- 라만차랜드 공주 로쟈: [BloomingThornsRodionFirst] 15 얻음\n- 라만차랜드 신부 그레고르: [BloodyHandGregFirst] 15 얻음\n- 라만차랜드 이발사 오티스: [BloodScissorPersonalityFirst] 15 얻음\n- 라만차랜드 왕자 뫼르소: [BloodArmorMeursault] 3 얻음\n\n[라만차랜드 실장 돈키호테 전용 효과]\n- 자신을 제외한 라만차랜드 소속 인격 1명당 라만차랜드 실장 돈키호테 기본 스킬의 최종 위력 +1, 가하는 피해량 +30% (최대 4, 120%, 대기 인원 포함, 사망 인원 포함, 미 편성 인원 제외)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9253].desc
   limit: do 1290 znaków
   tokeny: zachowaj dokładnie: \n, [BloodDinner], [Laceration], [BloodArmorPersonalityFirst], [BloomingThornsRodionFirst], [BloodyHandGregFirst], [BloodScissorPersonalityFirst], [BloodArmorMeursault]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast; [Laceration] = 출혈 / Bleed; [BloodArmorPersonalityFirst] = 경혈 / Hardblood; [BloomingThornsRodionFirst] = 피어나는 가시 / Blooming Thorn; [BloodyHandGregFirst] = 피로 물든 손 / Bloodied Hand; [BloodScissorPersonalityFirst] = 핏빛 가위날 / Blood-tinged Scissorblades; [BloodArmorMeursault] = 경혈 갑주 / Hardblood Armor
   EN: First Turn Start: Increase [BloodDinner] by 300\nDouble the amount of [BloodDinner] increased by [Laceration]\nOn Use of a Skill that consumes [BloodDinner], at Attack End, consume additional [BloodDinner] equal to the amount consumed by the Skill\n\n[La Manchaland Identities Only]\nWhen a La Manchaland Identity enters the field, the Identity gains their respective effect:\n- The Manager of La Manchaland Don Quixote: Gain 15 [BloodArmorPersonalityFirst]\n- The Princess of La Manchaland Rodion: Gain 15 [BloomingThornsRodionFirst]\n- The Priest of La Manchaland Gregor: Gain 15 [BloodyHandGregFirst]\n- The Barber of La Manchaland Outis: Gain 15 [BloodScissorPersonalityFirst]\n- The Prince of La Manchaland Meursault: Gain 3 [BloodArmorMeursault]\n\n[The Manager of La Manchaland Don Quixote Only]\nThe Manager of La Manchaland Don Quixote's Base Skills gain Final Power +1 and deal +30% damage for every La Manchaland Identity in the Team (max 4; max 120%; including Backup Units; including defeated units; excluding undeployed units)
   PL: — opis] Na początku pierwszej tury zyskuje 300 [BloodDinner]\n[BloodDinner] jest generowany 2 razy więcej, gdy powstaje przez efekt [Laceration]\nPrzy użyciu Umiejętności zużywającej [BloodDinner], na koniec ataku dodatkowo zużywa [BloodDinner] w wysokości zużytej przez tę Umiejętność wartości\n\n[Efekt wyłącznie dla Tożsamości La Manchaland]\nGdy Tożsamość La Manchaland wchodzi na pole walki, stosuje następujące efekty w zależności od Tożsamości:\n- Zarządczyni La Manchalandu Don Quixote: zyskuje 15 [BloodArmorPersonalityFirst]\n- Księżniczka La Manchalandu Rodion: zyskuje 15 [BloomingThornsRodionFirst]\n- Kapelan La Manchalandu Gregor: zyskuje 15 [BloodyHandGregFirst]\n- Cyruliczka La Manchalandu Outis: zyskuje 15 [BloodScissorPersonalityFirst]\n- Książę La Manchalandu Meursault: zyskuje 3 [BloodArmorMeursault]\n\n[Efekt wyłącznie dla Zarządczyni La Manchalandu Don Quixote]\n- Za każdą Tożsamość La Manchaland poza sobą podstawowe Umiejętności Zarządczyni La Manchalandu Don Quixote zyskują Moc Końcową +1 i zadają +30% obrażeń (maks. 4, 120%; wliczając jednostki zapasowe i pokonane; z pominięciem nieprzydzielonych)
313. [Dar E.G.O [9254] — nazwa] 한 잔 더!
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9254].name
   limit: do 40 znaków
   EN: Another Round!
   PL: — nazwa] Jeszcze Jedno!
314. [Dar E.G.O [9254] — opis] [Vibration] 횟수나 [Charge] 횟수를 소모하는 기본 스킬의 피해량 +20% (특수 <noparse>충전</noparse> 포함, 위력 고정 특수 <noparse>충전</noparse> 제외)\n\n기본 스킬로 [Vibration] 횟수나 [Charge] 횟수를 소모했으면, 스킬 종료 시 소모한 횟수의 절반 돌려받음 (최소 1, 소수점 <noparse>버림</noparse>, 특수 <noparse>충전</noparse> 포함, 위력 고정 특수 <noparse>충전</noparse> 제외)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9254].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Vibration], [Charge]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [Charge] = 충전 / Charge
   EN: Base Skills that consume [Vibration] Count or [Charge] Count deal +20% damage (including 'Unique Charge'; excluding 'Unique Charge'(fixed Potency))\n\nWhen consuming [Vibration] Count or [Charge] Count by using Base Skills, regain the half of consumed Count at Skill End (min 1, rounded down; including 'Unique Charge', excluding 'Unique Charge'(fixed Potency))
   PL: — opis] Podstawowe Umiejętności zużywające Liczniki [Vibration] lub Liczniki [Charge] zadają +20% obrażeń (wliczając Szczególne Ładowanie; z pominięciem Szczególnego Ładowania o zablokowanej Mocy)\n\nJeżeli podstawowa Umiejętność zużyła Liczniki [Vibration] lub Liczniki [Charge], na koniec Umiejętności odzyskuje połowę zużytych Liczników (min. 1, zaokrąglając w dół; wliczając Szczególne Ładowanie; z pominięciem Szczególnego Ładowania o zablokowanej Mocy)
315. [Dar E.G.O [9255] — nazwa] 박수 짝짝!
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9255].name
   limit: do 40 znaków
   EN: Clappity Clap!
   PL: — nazwa] Klask-Klask!
316. [Dar E.G.O [9255] — opis] 적에게 [Vibration] 위력, [Vibration] 횟수 또는 특수 진동을 부여하는 기본 스킬로 합 승리시 아래 특수 <noparse>진동</noparse> 중 무작위 특수 <noparse>진동</noparse>으로 [FusionVibration] (턴당 최대 1회)\n- [VibrationIgnition]\n- [VibrationBleeding]\n- [VibrationEcho]\n- [VibrationCollapse]\n- [VibrationChainPersonality]
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9255].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Vibration], [FusionVibration], [VibrationIgnition], [VibrationBleeding], [VibrationEcho], [VibrationCollapse], [VibrationChainPersonality]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [VibrationCollapse] = 진동 - 붕괴 / Tremor - Decay; [VibrationChainPersonality] = 진동 - 사슬 / Tremor - Chain
   EN: On Clash Win using a Base Skill that inflicts [Vibration] Potency, Count, or 'Unique Tremor' against an enemy, trigger [FusionVibration] into a random 'Unique Tremor' from the following (once per turn):\n- [VibrationIgnition]\n- [VibrationBleeding]\n- [VibrationEcho]\n- [VibrationCollapse]\n- [VibrationChainPersonality]
   PL: — opis] Przy wygranej Starciu podstawową Umiejętnością nakładającą Moc [Vibration], Liczniki [Vibration] lub Szczególny <noparse>Wstrząs</noparse> na wroga, wywołuje [FusionVibration] w losowy Szczególny <noparse>Wstrząs</noparse> spośród poniższych (maks. 1 raz na turę)\n- [VibrationIgnition]\n- [VibrationBleeding]\n- [VibrationEcho]\n- [VibrationCollapse]\n- [VibrationChainPersonality]
317. [Dar E.G.O [9273] — nazwa] 붉게 얽힌 거미집
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].name
   limit: do 40 znaków
   EN: Spiderweb Entangled in Red
   PL: — nazwa] Pajęczyna Splątana na Czerwono
318. [Dar E.G.O [9273] — opis] 사망한 아군 인격 1명당, 모든 아군의 공격 레벨 1, 방어 레벨 1 증가 (최대 10)\n\n거미집의 검 료슈가 덱에 편성되어 있으면, 거미집의 검 료슈 이외의 인격이 사망할 시 전투 종료 후 부활이 발동하지 않음 (보스층, 히든 노드 클리어)\n\n[편성 1번 인격 전용 효과]\n\n턴 시작 시 자신을 제외한 모든 아군이 사망했을 경우, [RedButterfly] 얻음\n\n[거미집의 검 료슈 전용 효과]\n\n스테이지에 첫 등장 시 사망한 거미집 소속 아군 인격 1명당, [PhantomIncisionTotalID] 5 얻음\n사망한 거미집 소속 아군 인격 2명당, 최종 위력 +1, 코인 위력 +1, 가하는 피해량 10% (각각 최대 3, 30%)\n거미집의 검 료슈 외에 생존한 아군이 없으면, 모든 선택지 보정 +12
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].desc
   limit: do 1160 znaków
   tokeny: zachowaj dokładnie: \n, [RedButterfly], [PhantomIncisionTotalID]
   znaczenie tagów: [RedButterfly] = 찢겨나온나비 / Torn-out Butterfly; [PhantomIncisionTotalID] = 지혜성도 / Dihui Star's Blade
   EN: All allies gain 1 Offense Level and 1 Defense Level for every defeated ally (max 10)\n\nIf Blade of the House of Spiders Ryōshū is in the Team loadout, any defeated Identities excluding Blade of the House of Spiders Ryōshū will not be revived after clearing an Encounter (Floor final boss nodes and Hidden nodes)\n\n[Effects apply only to #1 Deployed Identity]\n\nTurn Start: If there are no surviving allies apart from this unit, gain [RedButterfly]\n\n[Effects apply only to Blade of the House of Spiders Ryōshū]\n\nUpon entering the Encounter for the first time, for every The House of Spiders allied Identity that is defeated, gain 5 [PhantomIncisionTotalID]\nFor every 2 defeated The House of Spiders allies, Final Power +1, Coin Power +1, and deal +10% damage (max 3 and 30%, respectively)\nIf there are no surviving allies apart from Blade of the House of Spiders Ryōshū, gain +12 modifier for all Choice Event Skill checks
   PL: — opis] Za każdą pokonaną Tożsamość sojusznika Poziom Ataku i Poziom Obrony wszystkich sojuszników rośnie o 1 (maks. 10)\n\nJeżeli Ostrze Domu Pajęczyn Ryōshū jest w składzie decku, po śmierci Tożsamości innej niż Ostrze Domu Pajęczyn Ryōshū nie następuje wskrzeszenie po zakończeniu walki (piętra bossów, ukończenie Ukrytego Węzła)\n\n[Efekt wyłącznie dla Tożsamości na Przydziale #1]\n\nNa początku tury, jeżeli wszyscy sojusznicy poza jednostką są pokonani, zyskuje [RedButterfly]\n\n[Efekt wyłącznie dla Ostrza Domu Pajęczyn Ryōshū]\n\nPrzy pierwszym pojawieniu się na polu spotkania zyskuje 5 [PhantomIncisionTotalID] za każdą pokonaną Tożsamość sojusznika frakcji Domu Pajęczyn\nZa każde 2 pokonane Tożsamości sojusznika frakcji Domu Pajęczyn zyskuje Moc Końcową +1, Moc Monet +1 i +10% zadawanych obrażeń (każdy maks. 3, 30%)\nJeżeli nie ma żywych sojuszników poza Ostrzem Domu Pajęczyn Ryōshū, wszystkie korekty wyborów +12
319. [Dar E.G.O [9273] — opis skrócony] 공격 레벨, 방어 레벨 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].simpleDesc[abilityID=9273].simpleDesc
   limit: do 120 znaków
   EN: Gain Offense Level and Defense Level
   PL: — opis skrócony] Zwiększa Poziom Ataku i Poziom Obrony
320. [Dar E.G.O [9273] — opis skrócony] [RedButterfly] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].simpleDesc[abilityID=92731].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RedButterfly]
   znaczenie tagów: [RedButterfly] = 찢겨나온나비 / Torn-out Butterfly
   EN: Gain [RedButterfly]
   PL: — opis skrócony] Zyskuje [RedButterfly]
321. [Dar E.G.O [9273] — opis skrócony] [PhantomIncisionTotalID] 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].simpleDesc[abilityID=92732].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PhantomIncisionTotalID]
   znaczenie tagów: [PhantomIncisionTotalID] = 지혜성도 / Dihui Star's Blade
   EN: Gain [PhantomIncisionTotalID]
   PL: — opis skrócony] Zyskuje [PhantomIncisionTotalID]
322. [Dar E.G.O [9273] — opis skrócony] 최종 위력, 코인 위력, 가하는 피해량 증가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9273].simpleDesc[abilityID=92733].simpleDesc
   limit: do 120 znaków
   EN: Gain Final Power, Coin Power, deal more damage
   PL: — opis skrócony] Zyskuje Moc Końcową, Moc Monet i zadaje więcej obrażeń
323. [Dar E.G.O [9274] — nazwa] 오랏줄
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9274].name
   limit: do 40 znaków
   EN: Ohra Bond
   PL: — nazwa] Wiązadła Ohra
324. [Dar E.G.O [9274] — opis] 적에게 크리티컬 적중시 다음 턴에 [Binding] 1 부여 (턴당 2회)\n[Binding]을 보유한 적에게 스킬 적중시, [Breath] 1 얻음. (인격당 턴당 2회)\n\n턴 시작 시 [Laceration]을 보유한 모든 적이 자신의 [Binding] 수치만큼 [AttackDown] 얻음 (최대 5)\n\n턴 시작 시 모든 적(집중 전투면 부위로 판정)에게 [Binding]이 부여되어있다면, 모든 아군이 [Breath] 3 얻음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9274].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [Breath], [Laceration], [AttackDown]
   znaczenie tagów: [Binding] = 속박 / Bind; [Breath] = 호흡 / Poise; [Laceration] = 출혈 / Bleed; [AttackDown] = 공격 레벨 감소 / Offense Level Down
   EN: On Crit against an enemy, inflict 1 [Binding] next turn (2 times per turn)\nOn Hit using a Skill against an enemy that has [Binding], gain 1 [Breath] (2 times per turn per Identity)\n\nTurn Start: All enemies that have [Laceration] gain [AttackDown] equal to [Binding] on themselves (max 5)\n\nTurn Start: If all enemies(for Focused Encounters, all Parts) have [Binding], all allies gain 3 [Breath]
   PL: — opis] Przy trafieniu Trafieniem Krytycznym na wroga, nakłada 1 [Binding] na następną turę (2 razy na turę)\nPrzy trafieniu Umiejętnością wroga posiadającego [Binding], zyskuje 1 [Breath] (2 razy na turę na Tożsamość)\n\nNa początku tury wszyscy wrogowie posiadający [Laceration] zyskują [AttackDown] równy posiadanej wartości [Binding] (maks. 5)\n\nJeżeli wszyscy wrogowie (w walkach Skupionych — Partie) mają nałożony [Binding], wszyscy sojusznicy zyskują 3 [Breath]
325. [Dar E.G.O [9275] — nazwa] N사 고정팀 가방
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9275].name
   limit: do 50 znaków
   EN: N Corp. Service des Clous Briefcase
   PL: — nazwa] Walizka Pinframing Korporacji N
326. [Dar E.G.O [9275] — opis] [Laceration] 위력, [Laceration] 횟수 또는 특수 출혈을 부여하는 스킬로 적에게 적중 시 [NailPersonality] 1 부여 (스킬당 1회)\n[NailPersonality]을 보유한 적에게 [VibrationExplosion]을 적용했으면 다음 턴에 [Binding] 1 부여 (턴당 3회)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9275].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [NailPersonality], [VibrationExplosion], [Binding]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [NailPersonality] = 못 / Nails; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Binding] = 속박 / Bind
   EN: When hitting an enemy using a Skill that inflicts [Laceration] Potency, Count, or 'Unique Bleed', inflict 1 [NailPersonality] (once per Skill)\nWhen triggering [VibrationExplosion] on an enemy that has [NailPersonality], inflict 1 [Binding] next turn (3 times per turn)
   PL: — opis] Przy trafieniu wroga Umiejętnością nakładającą Moc [Laceration], Liczniki [Laceration] lub Szczególne Krwawienie, nakłada 1 [NailPersonality] (1 raz na Umiejętność)\nPrzy wywołaniu [VibrationExplosion] na wrogu posiadającym [NailPersonality], nakłada 1 [Binding] na następną turę (3 razy na turę)
327. [Dar E.G.O [9276] — nazwa] 백자연적
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9276].name
   limit: do 40 znaków
   EN: Baekja Water Dropper
   PL: — nazwa] Porcelanowa Pluwka
328. [Dar E.G.O [9276] — opis] 아군 인격이 [SupportProtect]를 얻을 때 [AttackDmgUp] 2, [Protection] 2 얻음\n\n[편성 1번 전용 효과]\n턴 종료시 다음 턴에 [Agility] 2 얻음\n인격의 속도가 적보다 빠르면, 속도 차이당 피해량 +3% (최대 30%)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9276].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [SupportProtect], [AttackDmgUp], [Protection], [Agility]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense; [AttackDmgUp] = 피해량 증가 / Damage Up; [Protection] = 보호 / Protection; [Agility] = 신속 / Haste
   EN: When an allied Identity gains [SupportProtect], the said ally gains 2 [AttackDmgUp] and 2 [Protection]\n\n[Effects apply only to #1 Deployed Identity]\nTurn End: Gain 2 [Agility] next turn\nWhen an Identity's Speed is faster than the enemy's, deal +3% damage for every Speed difference (max 30%)
   PL: — opis] Gdy sojusznicza Tożsamość zyskuje [SupportProtect], ta Tożsamość zyskuje 2 [AttackDmgUp] i 2 [Protection]\n\n[Efekt wyłącznie dla Przydziału #1]\nNa koniec tury zyskuje 2 [Agility] na następną turę\nJeżeli Szybkość Tożsamości jest większa niż wroga, zadaje +3% obrażeń za każdy punkt różnicy Szybkości (maks. 30%)
329. [Dar E.G.O [9277] — nazwa] 창포검
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9277].name
   limit: do 40 znaków
   EN: Flagroot Cane Sword
   PL: — nazwa] Miecz-Laska z Tataraku
330. [Dar E.G.O [9277] — opis] 아군이 이번 턴에 적에게 피격당하지 않았으면, 다음 턴에 [SlashDamageUp] 1 얻음\n아군이 적에게 피격 시, [Breath]을 4 얻고 이번 턴과 다음 턴에 [CriticalDamageUp] 1 얻음 (인격당 턴당 1회)\n- 검계 소속 인격이면, 이 기프트의 효과를 2배로 받음
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9277].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp], [Breath], [CriticalDamageUp]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [Breath] = 호흡 / Poise; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up
   EN: If an ally was not hit by an enemy this turn, the said ally gains 1 [SlashDamageUp] next turn\nWhen an ally is hit by an enemy, the said ally gains 4 [Breath], and gains 1 [CriticalDamageUp] this turn and next turn (once per turn per Identity)\n- If the affected ally is a Blade Lineage Identity, gain double the effects of this E.G.O Gift
   PL: — opis] Jeżeli sojusznik nie został trafiony przez wroga w tej turze, zyskuje 1 [SlashDamageUp] na następną turę\nGdy sojusznik zostaje trafiony przez wroga, zyskuje 4 [Breath] oraz 1 [CriticalDamageUp] w tej turze i następnej (1 raz na turę na Tożsamość)\n- Jeżeli sojusznikiem jest Tożsamość Rodu Ostrza, otrzymuje 2 razy większe efekty tego Daru
331. [Dar E.G.O [9278] — nazwa] 바스라진 목제 형구
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9278].name
   limit: do 40 znaków
   EN: Crushed Wooden Manacle
   PL: — nazwa] Zgniecione Drewniane Kajdanki
332. [Dar E.G.O [9278] — opis] 참격 스킬을 사용하여 적에게 적중 시 다음 턴에 [DefenseDown] 1 부여 (스킬당 2회)\n아군이 공격하는 적보다 속도가 빠르면, 속도 차이 1당 기본 공격 스킬 피해량 +3% (최대 12%)\n- 적이 [Binding] 상태면, 피해량 증가량과 최대치가 2배로 적용됨
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9278].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n, [DefenseDown], [Binding]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [Binding] = 속박 / Bind
   EN: On Hit against an enemy using a Slash Skill, inflict 1 [DefenseDown] next turn (2 times per Skill)\nIf an ally is faster than the enemy, the said ally deals +3% damage using Base Attack Skills for every 1 Speed Difference (max 12%)\n- If the enemy has [Binding], double the above damage boost and its maximum cap
   PL: — opis] Przy trafieniu wroga Umiejętnością Cięcia, nakłada 1 [DefenseDown] na następną turę (2 razy na Umiejętność)\nJeżeli sojusznik jest szybszy niż atakowany wróg, zadaje podstawowymi Umiejętnościami ataku +3% obrażeń za każdy punkt różnicy Szybkości (maks. 12%)\n- Jeżeli wróg ma stan [Binding], wzrost obrażeń i jego maksimum są stosowane podwójnie
333. [Dar E.G.O [9279] — nazwa] 민무늬 코등이
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9279].name
   limit: do 40 znaków
   EN: Unadorned Sword-guard
   PL: — nazwa] Niezdobiony Jelec
334. [Dar E.G.O [9279] — opis] [Breath] 1당, 참격 스킬의 피해량 +1% (최대 15%)
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9279].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Slash Skills deal +1% damage for every [Breath] (max 15%)
   PL: — opis] Umiejętności Cięcia zadają +1% obrażeń za każdy [Breath] (maks. 15%)
335. [Dar E.G.O [9280] — nazwa] 본국검보[本國劍譜]
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9280].name
   limit: do 60 znaków
   EN: The Book of the Homeland Swordplay [本國劍譜]
   PL: — nazwa] Księga Szermierki Ojczyzny [本國劍譜]
336. [Dar E.G.O [9280] — opis] 적의 참격 내성이 1.5 이하인 경우, 참격 내성 +0.3\n참격 스킬 공격 레벨 +2\n참격 내성이 약점(내성 1.0 초과, 흐트러짐 제외)인 적 공격 시, 참격 피해량 +(5+대상의 참격 내성 x10)% (최대 25%).\n\n[Breath] 1당, 참격 스킬의 피해량 +1.5% (최대 30%)\n\n검계 소속 인격을 제외한 편성 순서가 가장 빠른 S사 소속 인격 1인을 검계 소속으로 취급하고, 매 턴 [BongukGiftEnhance] 부여\n\n턴 시작시, 검계 소속 인격이 3인 이상일 때 발동 (출격 인원을 기준으로 함)\n- 전투 시작 시 분노, 오만 스킬을 장착한 검계 소속 아군 인격에게 [BongukGiftEnhance] 1 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9280].desc
   limit: do 890 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [BongukGiftEnhance]
   znaczenie tagów: [Breath] = 호흡 / Poise; [BongukGiftEnhance] = 본국검 - 격법 전수 / Sword of the Homeland - Striking
   EN: If an enemy has 1.5 or lower Slash Resist., Slash Resist. +0.3\nSlash Skills gain Offense Level +2\nWhen attacking enemies that are Weak (greater than 1.0 Resist.; Staggered states do not count) to Slash, deal +(5 + (target's Slash Resist. x 10))% damage (max 25%)\n\nSlash Skills deal +1.5% damage for every [Breath] (max 30%)\n\nCount 1 non-Blade Lineage S Corp. Identity with the earliest Deployment order as a Blade Lineage Identity and apply [BongukGiftEnhance] on it every turn\n\nTurn Start: Activates when there are 3 or more Blade Lineage Identities (only counts Identities on the field)\n- Combat Start: Apply 1 [BongukGiftEnhance] on allied Blade Lineage Identities that have equipped Wrath or Pride Skills
   PL: — opis] Jeżeli Odporność wroga na Cięcie wynosi co najwyżej 1,5, Odporność na Cięcie +0,3\nUmiejętności Cięcia zyskują Poziom Ataku +2\nPrzy atakowaniu wrogów słabych na Cięcie (Odporność powyżej 1,0; stany Oszołomienia się nie liczą), zadaje +(5+Odporność celu na Cięcie x 10)% obrażeń Cięcia (maks. 25%).\n\nUmiejętności Cięcia zadają +1,5% obrażeń za każdy [Breath] (maks. 30%)\n\nTraktuje 1 Tożsamość Korp. S przydzieloną najwcześniej w kolejności (poza Tożsamościami Rodu Ostrza) jako Tożsamość Rodu Ostrza i nakłada co turę [BongukGiftEnhance]\n\nNa początku tury uruchamia się, gdy na polu są co najmniej 3 Tożsamości Rodu Ostrza (liczone na polu)\n- Na początku walki nakłada 1 [BongukGiftEnhance] na sojusznicze Tożsamości Rodu Ostrza wyposażone w Umiejętności Gniewu lub Pychy
337. [Dar E.G.O [9282] — nazwa] 날개 모양 양초
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9282].name
   limit: do 40 znaków
   EN: Wing-shaped Waxen Candle
   PL: — nazwa] Świeca w Kształcie Skrzydła
338. [Dar E.G.O [9282] — opis] 턴 시작시, <noparse>새벽 사무소</noparse> 소속 인격이 3인 이상일 때 발동 (대기 인원 포함)\n첫 턴이면, 모든 아군에게 [DawnLight] 2 부여\n<noparse>새벽 사무소</noparse> 해결사 싱클레어가 전투 시작시 정신력을 10 회복하고, '불안정한 자아의 껍질' 패시브 효과로 불안정 E.G.O 밀랍날개 상태가 되는 정신력 조건이 25로 감소\n\n[<noparse>새벽 사무소</noparse> 소속 인격 전용 효과]\n기본 스킬의 공격 적중 시 대상에게 [Combustion] 2, [Vibration] 2 부여 (스킬당 1회)\n<noparse>새벽 사무소</noparse> 소속 인격을 [Combustion], [Vibration]을 부여하는 인격으로 취급됨\n- 이 효과로 인해서 기본 스킬이 [Combustion], [Vibration]을 부여하는 스킬로 취급됨\n스테이지 시작시 <noparse>새벽 사무소</noparse> 해결사 파우스트 인격이 전투에 등장해 있으면, [Firstlight] 1 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9282].desc
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [DawnLight], [Combustion], [Vibration], [Firstlight]
   znaczenie tagów: [DawnLight] = 새벽맞이 / Dawnherald; [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor; [Firstlight] = 전투 감각 / Battle Instinct
   EN: Turn Start: Activates when there are 3 or more <noparse>Dawn Office</noparse> Identities (counts Backup Identities)\n\nTurn 1: Apply 2 [DawnLight] on all allies\nCombat Start: <noparse>Dawn Office</noparse> Fixer Sinclair heals 10 SP, and the said Identity may enter the "<noparse>Volatile E.G.O::Waxen Pinion</noparse>" state via the Passive effect of "Unstable Shell of Ego" at 25+ SP instead of 40+ SP\n\n[<noparse>Dawn Office</noparse> Identities Exclusive Effect]\nOn Hit using Base Skills, inflict 2 [Combustion] and 2 [Vibration] on target (once per Skill)\n<noparse>Dawn Office</noparse> Identities are considered "Identities that inflict [Combustion] and [Vibration]"\n- <noparse>Dawn Office</noparse> Identities' Base Skills count as "Skills that inflict [Combustion] and [Vibration]"\nEncounter Start: If <noparse>Dawn Office</noparse> Faust is on the field, apply 1 [Firstlight] on the said Identity
   PL: — opis] Na początku tury uruchamia się, gdy są co najmniej 3 Tożsamości <noparse>Biura Świtu</noparse> (wliczając jednostki zapasowe)\nJeżeli to pierwsza tura, nakłada 2 [DawnLight] na wszystkich sojuszników\nNa początku walki Biuro Świtu Fikser Sinclair odzyskuje 10 Poczytalności, a próg Poczytalności wejścia w stan Niestabilne E.G.O::Woskowe Skrzydło przez efekt pasywki „Niestabilna Skorupa Ego” maleje do 25\n\n[Efekt wyłącznie dla Tożsamości <noparse>Biura Świtu</noparse>]\nPrzy trafieniu atakiem podstawową Umiejętnością nakłada na cel 2 [Combustion] i 2 [Vibration] (1 raz na Umiejętność)\nTożsamości <noparse>Biura Świtu</noparse> są traktowane jako Tożsamości nakładające [Combustion] i [Vibration]\n- Dzięki temu efektowi podstawowe Umiejętności są traktowane jako Umiejętności nakładające [Combustion] i [Vibration]\nJeżeli na początku spotkania Tożsamość Biuro Świtu Fikser Faust jest na polu, nakłada 1 [Firstlight]
339. [Dar E.G.O [9283] — nazwa] 상납된 시가
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9283].name
   limit: do 40 znaków
   EN: Tributary Cigar
   PL: — nazwa] Cygaro Trybutowe
340. [Dar E.G.O [9283] — opis] 턴 시작시, 엄지 소속 인격이 3인 이상일 때 발동 (출격 인원을 기준으로 함)\n엄지 소속 인격이 턴 시작 시 [PlusCoinValueUp] 1, [AttackDmgUp] 2 얻음\n엄지 소속 인격 1명당 엄지 소속 인격이 [AttackUp] 1 얻음 (최대 4)\n대상이 보유한 [VibrationIgnition] 1당 피해량 +1% (최대 20%)\n- [Bullet]을 소모하는 스킬이면, 추가로 +1% (최대 20%)\n- 엄지 소속이면, 추가로 +1% (최대 20%)\n\n자신의 스킬 효과로 [VibrationExplosion]이 발동되었다면, 다음 턴에 [AttackUp] 2 얻음 (턴당 3회)\n\n거미집 엄지 아비 로쟈의 스킬 3 공격 종료시 거미집 엄지 제자 히스클리프에게 [EvolvingManual] 1 부여
   źródło: EGOgift_MirrorDungeon_7.json :: dataList[id=9283].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n, [PlusCoinValueUp], [AttackDmgUp], [AttackUp], [VibrationIgnition], [Bullet], [VibrationExplosion], [EvolvingManual]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [AttackDmgUp] = 피해량 증가 / Damage Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [VibrationIgnition] = 진동 - 작열 / Tremor - Scorch; [Bullet] = 탄환 / Ammo; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [EvolvingManual] = 완성되어가는 교본 / Maturing Textbook
   EN: Turn Start: Activates when there are 3 or more "The Thumb" Identities (only counts Identities on the field)\nTurn Start: "The Thumb" Identities gain 1 [PlusCoinValueUp] and 2 [AttackDmgUp]\n"The Thumb" Identities gain 1 [AttackUp] for every "The Thumb" Identity on the field (max 4)\nDeal +1% damage for every [VibrationIgnition] on target (max 20%)\n- Skills that spend [Bullet] deal an additional +1% damage (max 20%)\n- "The Thumb" Identities deal an additional +1% damage (max 20%)\n\nUnits that triggered [VibrationExplosion] with their Skill effects gain 2 [AttackUp] next turn (3 times per turn)\n\nAt Attack End of The House of Spiders: The Thumb Nursefather Rodion's Skill 3, apply 1 [EvolvingManual] on The House of Spiders: The Thumb Apprentice Heathcliff
   PL: — opis] Na początku tury uruchamia się, gdy są co najmniej 3 Tożsamości Kciuka (liczone na polu)\nTożsamości Kciuka zyskują na początku tury 1 [PlusCoinValueUp] i 2 [AttackDmgUp]\nTożsamości Kciuka zyskują 1 [AttackUp] za każdą Tożsamość Kciuka na polu (maks. 4)\nZadaje +1% obrażeń za każdą wartość [VibrationIgnition] celu (maks. 20%)\n- Jeżeli Umiejętność zużywa [Bullet], dodatkowo +1% (maks. 20%)\n- Jeżeli Tożsamość należy do Kciuka, dodatkowo +1% (maks. 20%)\n\nJeżeli [VibrationExplosion] zostało wywołane efektem Umiejętności jednostki, zyskuje 2 [AttackUp] na następną turę (3 razy na turę)\n\nNa koniec ataku Umiejętnością 3 Dom Pajęczyn: Ojciec Kciuka Rodion nakłada 1 [EvolvingManual] na Dom Pajęczyn: Ucznia Kciuka Heathcliff

## Dar E.G.O: EGOgift_MirrorDungeon_8
- plik gry: `EGOgift_MirrorDungeon_8.json`

341. [Dar E.G.O [9284] — nazwa] 철 지난 르루주 옷
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9284].name
   limit: do 40 znaków
   EN: Out-of-style Rouge Clothing
   PL: Przestarzałe Ubranie Le Rouge
342. [Dar E.G.O [9284] — opis] 아군이 기본 공격 스킬의 스킬 효과, 코인 효과로 체력 회복 시 50%만큼 추가 회복함 (턴당 3회, 소수점 <noparse>버림</noparse>)\n\n[오트쿠튀르::르루주 부티크 이스마엘 전용 효과]\n오트쿠튀르::르루주 붉은 신 싱클레어가 자신과 함께 전장에 있으면, 턴 시작시 [RougeIshmaelCocoon]을 1 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)\n- '<noparse>탈의실</noparse> 속으로...' 패시브 효과 중 '이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 즉시 [RougeIshmaelCocoon] 2를 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)' 효과가 발동했으면, 전용 효과는 발동 하지 않음\n- 전용 효과 발동 시 '<noparse>탈의실</noparse> 속으로...' 패시브 효과 중 '이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 즉시 [RougeIshmaelCocoon] 2를 얻고 [RougeIshmaelCocoon] 상태가 됨 (전투당 1회)' 효과가 발동하지 않음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9284].desc
   limit: do 1250 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [RougeIshmaelCocoon]
   znaczenie tagów: [RougeIshmaelCocoon] = 탈의실 / Changing Room
   EN: When allies heal HP through Base Attack Skills' Skill or Coin effects, heal +50% HP (3 times per turn; rounded down)\n\n[Haute Couture::Boutique du Rouge Ishmael Exclusive Effect]\nIf Haute Couture::The Crimson God of Le Rouge Sinclair is with this unit on the field, gain 1 [RougeIshmaelCocoon] at Turn Start and enter [RougeIshmaelCocoon] state (once per Encounter)\n- If "In this Encounter, when this unit takes damage that brings its HP down to 0, nullify that damage; then, immediately gain 2 [RougeIshmaelCocoon] and enter the [RougeIshmaelCocoon] state (once per Encounter)" from the Passive "Into the <noparse>Changing Room</noparse>…" activated, the exclusive effect does not activate\n- When the exclusive effect activates, the effect "In this Encounter, when this unit takes damage that brings its HP down to 0, nullify that damage; then, immediately gain 2 [RougeIshmaelCocoon] and enter the [RougeIshmaelCocoon] state (once per Encounter)" from the Passive "Into the <noparse>Changing Room</noparse>…" does not activate
   PL: — opis] Gdy sojusznicy odzyskują HP efektem Umiejętności lub Monety podstawowej Umiejętności ataku, odzyskują dodatkowo 50% (3 razy na turę, zaokrąglając w dół)\n\n[Efekt wyłącznie dla Haute Couture::Boutique du Rouge Ishmael]\nJeżeli Haute Couture::Czerwony Bóg Le Rouge Sinclair jest na polu wraz z jednostką, na początku tury zyskuje 1 [RougeIshmaelCocoon] i wchodzi w stan [RougeIshmaelCocoon] (1 raz na walkę)\n- Jeżeli wystąpił efekt pasywki „W głąb <noparse>Przymierzalni</noparse>...”: „W tej walce, gdy jednostka otrzyma obrażenia redukujące HP do 0, nie otrzymuje tych obrażeń i natychmiast zyskuje 2 [RougeIshmaelCocoon] oraz wchodzi w stan [RougeIshmaelCocoon] (1 raz na walkę)”, efekt wyłącznie nie wywołuje się\n- Gdy wywołano efekt wyłącznie, efekt pasywki „W głąb <noparse>Przymierzalni</noparse>...” — „W tej walce, gdy jednostka otrzyma obrażenia redukujące HP do 0, nie otrzymuje tych obrażeń i natychmiast zyskuje 2 [RougeIshmaelCocoon] oraz wchodzi w stan [RougeIshmaelCocoon] (1 raz na walkę)” — nie wywołuje się
343. [Dar E.G.O [9284] — opis skrócony] 즉시 [RougeIshmaelCocoon] 상태가 됨
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9284].simpleDesc[abilityID=9284].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [RougeIshmaelCocoon]
   znaczenie tagów: [RougeIshmaelCocoon] = 탈의실 / Changing Room
   EN: Immediately enter [RougeIshmaelCocoon]
   PL: — opis skrócony] Natychmiast wchodzi w stan [RougeIshmaelCocoon]
344. [Dar E.G.O [9284] — opis skrócony] 체력 추가 회복
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9284].simpleDesc[abilityID=92841].simpleDesc
   limit: do 120 znaków
   EN: Heal more HP
   PL: — opis skrócony] Odzyskuje dodatkowe HP
345. [Dar E.G.O [9285] — nazwa] 탄산 음료
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9285].name
   limit: do 40 znaków
   EN: Soda Pop
   PL: Gazowany Napój
346. [Dar E.G.O [9285] — opis] 이번 턴에 자신의 스킬 및 코인 효과로 체력 회복을 한 번 이상 시도한 수감자가 다음 턴에 스킬로 가하는 피해량 +10%, (해당 턴 시도된 회복 수치의 합 / 10)만큼 [AttackUp] 얻음 (최대 6, 소수점 <noparse>버림</noparse>)\n\n전장에 같은 소속 인격이 있으면, 자신을 제외한 같은 소속 인격이 위 효과로 얻은 [AttackUp]의 절반만큼 [AttackUp] 얻음 (최소 1, 턴당 최대 3까지 얻음, 소수점 <noparse>버림</noparse>)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9285].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Sinners who attempt to heal HP on self this turn using Skill or Coin effects gain the following effects next turn:\n- Skills deal +10% damage\n- Gain [AttackUp] equal to (sum of HP healed during the turn (including excess healing) / 10) (max 6; rounded down)\n\nIf there are other Identities on the field that are in the same faction as the units that activated the above effect, they gain half of the [AttackUp] the above units gained (min 1, max 3 per turn; rounded down)
   PL: — opis] Grzesznicy, którzy w tej turze przynajmniej raz odzyskali HP efektem Umiejętności lub Monety, zyskują na następną turę +10% obrażeń Umiejętnościami i [AttackUp] równy (suma odzyskanego HP w tej turze/10) (maks. 6, zaokrąglając w dół)\n\nJeżeli na polu są Tożsamości tej samej frakcji, Tożsamości tej samej frakcji poza jednostką zyskują [AttackUp] równy połowie [AttackUp] uzyskanego przez powyższy efekt (min. 1, maks. 3 na turę, zaokrąglając w dół)
347. [Dar E.G.O [9285] — opis skrócony] 피해량 증가[TabExplain], [AttackUp] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9285].simpleDesc[abilityID=9285].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Deal more damage and gain [AttackUp]
   PL: — opis skrócony] Zadaje więcej obrażeń[TabExplain], zyskuje [AttackUp]
348. [Dar E.G.O [9286] — nazwa] 르누아르 메종 슬랙스
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9286].name
   limit: do 40 znaków
   EN: Maison du Noir Slacks
   PL: Slacks Maison du Noir
349. [Dar E.G.O [9286] — opis] [Charge] 위력이 2 이상인 아군이 [VibrationExplosion] 시 아래 효과 적용\n- (자신의 [Charge] 위력 x 횟수)만큼 질투 피해를 줌 (스킬당 2회, 1회당 최대 100)\n- 위 효과로 질투 피해를 2번 주었으면, 다음 턴에 대상에게 [Binding] 3 부여\n\n아군이 스킬로 [VibrationExplosion] 시 [VibrationExplosion]마다 (자신의 [Charge] 위력 / 3)만큼 다음 턴에 [AttackUp] 얻음 (턴당 최대 5, 소수점 <noparse>버림</noparse>)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9286].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Charge], [VibrationExplosion], [Binding], [AttackUp]
   znaczenie tagów: [Charge] = 충전 / Charge; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Binding] = 속박 / Bind; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: When allies that have 2+ [Charge] Potency trigger [VibrationExplosion], apply the following effects:\n- Deal ([Charge] Potency on self x [Charge] Count) Envy Damage (2 times per skill, max 100 damage per tick)\n- Every 2 times the above effect deals Envy Damage, inflict 3 [Binding] next turn on target\n\nEvery time an ally triggers [VibrationExplosion] using a Skill, gain ([Charge] Potency on self / 3) [AttackUp] next turn (max 5 per turn; rounded down)
   PL: — opis] Gdy sojusznik z Mocą [Charge] co najmniej 2 wywołuje [VibrationExplosion], stosuje poniższe efekty:\n- Zadaje obrażenia Żądzy równe (Moc [Charge] jednostki x Liczniki) (2 razy na Umiejętność; maks. 100 obrażeń na 1 wywołanie)\n- Jeżeli powyższy efekt zadał obrażenia Żądzy 2 razy, nakłada 3 [Binding] na cel na następną turę\n\nGdy sojusznik wywołuje [VibrationExplosion] Umiejętnością, za każde [VibrationExplosion] zyskuje (Moc [Charge] jednostki/3) [AttackUp] na następną turę (maks. 5 na turę, zaokrąglając w dół)
350. [Dar E.G.O [9286] — opis skrócony] 질투 피해를 주고 [Binding] 부여
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9286].simpleDesc[abilityID=9286].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Deal Envy Damage and inflict [Binding]
   PL: — opis skrócony] Zadaje obrażenia Żądzy i nakłada [Binding]
351. [Dar E.G.O [9286] — opis skrócony] [AttackUp] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9286].simpleDesc[abilityID=92861].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Gain [AttackUp]
   PL: — opis skrócony] Zyskuje [AttackUp]
352. [Dar E.G.O [9287] — nazwa] 르누아르 메리 제인
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9287].name
   limit: do 40 znaków
   EN: Le Noir Mary Janes
   PL: Balerinki Mary Jane Le Noir
353. [Dar E.G.O [9287] — opis] 전투 시작 시 가장 보호막을 많이 보유한 인격의 공격 적중 시 현재 보호막의 50%만큼 나태 피해를 줌 (스킬당 2회, 1회당 최대 100, 소수점 <noparse>버림</noparse>)\n- 보호막 수치가 동일한 인격이 2명 이상이면, 편성 순서 순으로 적용\n\n[PersonalityCharge]이면, 대신 보호막의 100%만큼 나태 피해를 줌 (스킬당 3회, 1회당 최대 100, 소수점 <noparse>버림</noparse>)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9287].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: Combat Start: On Hit from an Identity that has the highest Shield, deal (current Shield / 2) Sloth Damage (2 times per Skill, max 100 damage per tick; rounded down)\n- If 2+ Identities have the same Shield HP, applies to the Identity with the earlier Deployment Order\n\nIf the affected Identity is a [PersonalityCharge], deal Sloth Damage equal to current Shield instead (3 times per skill, max 100 per tick; rounded down)
   PL: — opis] Na początku walki, gdy atak trafi z Tożsamości posiadającej najwięcej Tarczy, zadaje obrażenia Lenistwa równe 50% obecnej Tarczy (2 razy na Umiejętność; maks. 100 na 1 wywołanie, zaokrąglając w dół)\n- Jeżeli 2 lub więcej Tożsamości ma tę samą wartość Tarczy, stosuje według kolejności przydziału\n\nJeżeli Tożsamość jest [PersonalityCharge], zadaje zamiast tego obrażenia Lenistwa równe 100% Tarczy (3 razy na Umiejętność; maks. 100 na 1 wywołanie, zaokrąglając w dół)
354. [Dar E.G.O [9287] — opis skrócony] 보호막에 비례해 나태 피해를 줌
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9287].simpleDesc[abilityID=9287].simpleDesc
   limit: do 120 znaków
   EN: Deal Sloth Damage based on Shield
   PL: — opis skrócony] Zadaje obrażenia Lenistwa proporcjonalnie do Tarczy
355. [Dar E.G.O [9288] — nazwa] 바느질의 왕의 시침핀
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9288].name
   limit: do 60 znaków
   EN: Straight Pin of the King of Needleworks
   PL: Szpilka Króla Szycia
356. [Dar E.G.O [9288] — opis] 턴 시작 시 [SewingKingMark]이 있는 적이 없으면, 무작위 적에게 [SewingKingMark] 부여 (집중 전투인 경우, 부위로 판정)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9288].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [SewingKingMark]
   znaczenie tagów: [SewingKingMark] = 바느질의 왕 표식 / Mark of the King of Needleworks
   EN: Turn Start: If no enemies have [SewingKingMark], inflict [SewingKingMark] on a random enemy (in Focused Encounters, a Part)
   PL: — opis] Na początku tury, jeżeli żaden wróg nie ma [SewingKingMark], nakłada [SewingKingMark] na losowego wroga (w walkach Skupionych — na Partię)
357. [Dar E.G.O [9288] — opis skrócony] [SewingKingMark] 부여, 사망 시 고정 피해를 줌
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9288].simpleDesc[abilityID=9288].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SewingKingMark]
   znaczenie tagów: [SewingKingMark] = 바느질의 왕 표식 / Mark of the King of Needleworks
   EN: Inflict [SewingKingMark]; deal fixed damage on death
   PL: — opis skrócony] Nakłada [SewingKingMark]; zadaje stałe obrażenia po śmierci
358. [Dar E.G.O [9289] — nazwa] 연골
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9289].name
   limit: do 40 znaków
   EN: Cartilage
   PL: Chrząstka
359. [Dar E.G.O [9289] — opis] [Charge] 횟수 또는 특수 [Charge]을 소모하는 스킬의 피해량 +(자신의 [Charge] 위력 x 2)% (최대 10%)\n\n턴 종료 시 이번 턴에 [Charge] 횟수 또는 특수 [Charge]을 소모했으면, 다음 턴에 [Agility] 1 얻음\n\n대상의 속도가 자신보다 낮으면, 합 위력 +1\n- 자신이 시지프 소속이면, 대신 최종 위력 +1
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9289].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [Agility]
   znaczenie tagów: [Charge] = 충전 / Charge; [Agility] = 신속 / Haste
   EN: Skills that consume [Charge] Count or Unique [Charge] deal +([Charge] Potency on self x 2)% damage (max 10%)\n\nTurn End: Units that consumed [Charge] Count or Unique [Charge] this turn gain 1 [Agility] next turn\n\nIf a unit's Speed is faster than the target's, Clash Power +1\n- If the said unit is a "Sisyphe" Identity, gain Final Power +1 instead
   PL: — opis] Umiejętności zużywające Liczniki [Charge] lub Szczególne [Charge] zadają +(Moc [Charge] jednostki x 2)% obrażeń (maks. 10%)\n\nNa koniec tury jednostki, które w tej turze zużyły Liczniki [Charge] lub Szczególne [Charge], zyskują 1 [Agility] na następną turę\n\nJeżeli Szybkość celu jest niższa niż jednostki, Moc Starcia +1\n- Jeżeli Tożsamość należy do Sisyphe, zamiast tego zyskuje Moc Końcową +1
360. [Dar E.G.O [9289] — opis skrócony] 피해량, 합 위력 또는 최종 위력 증가[TabExplain], [Agility] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9289].simpleDesc[abilityID=9289].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Deal more damage, gain [Agility], and gain Clash/Final Power
   PL: — opis skrócony] Zadaje więcej obrażeń, zyskuje Moc Starcia lub Moc Końcową[TabExplain], zyskuje [Agility]
361. [Dar E.G.O [9290] — nazwa] 담요
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9290].name
   limit: do 40 znaków
   EN: Blanket
   PL: Koc
362. [Dar E.G.O [9290] — opis] 이번 턴에 수비 스킬을 장착한 인격이 적의 공격으로 받는 피해량 -20%\n- 전투 종료 시 자신이 [PersonalityCharge]이면, 다음 턴에 [AttackUp] 2 얻음\n- 전투 종료 시 자신이 시지프 소속이면, 다음 턴에 [ResultEnhancement] 1 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9290].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [PersonalityCharge], [AttackUp], [ResultEnhancement]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Identities that equipped Defense Skills this turn take -20% damage from enemy attacks\n- Combat End: If the affected Identity is a [PersonalityCharge], gain 2 [AttackUp] next turn\n- Combat End: If the affected Identity is a "Sisyphe" Identity, gain 1 [ResultEnhancement] next turn
   PL: — opis] Tożsamości, które w tej turze założyły Umiejętności obronne, otrzymują -20% obrażeń od ataków wrogów\n- Na koniec walki jeżeli jednostka jest [PersonalityCharge], zyskuje 2 [AttackUp] na następną turę\n- Na koniec walki jeżeli Tożsamość należy do Sisyphe, zyskuje 1 [ResultEnhancement] na następną turę
363. [Dar E.G.O [9290] — opis skrócony] 받는 피해량 감소[TabExplain], [AttackUp] 또는 [ResultEnhancement] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9290].simpleDesc[abilityID=9290].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [AttackUp], [ResultEnhancement]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [ResultEnhancement] = 위력 증가 / Power Up
   EN: Take less damage and gain [AttackUp]/[ResultEnhancement]
   PL: — opis skrócony] Otrzymuje mniej obrażeń[TabExplain], zyskuje [AttackUp] lub [ResultEnhancement]
364. [Dar E.G.O [9291] — nazwa] 꽃가위
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9291].name
   limit: do 40 znaków
   EN: Blossom Scissors
   PL: Kwiatowe Nożyczki
365. [Dar E.G.O [9291] — opis] [편성 순서 1번 인격 전용 효과]\n\n시지프 소속 인격 또는 [PersonalityCharge]의 기본 스킬의 마지막 코인 적중 시 메인 타겟에게 해당 코인 최종 피해량의 5%만큼 참격 피해를 줌 (스킬당 1회)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9291].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n, [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: [Effects apply only to #1 Deployed Identity]\n\n"Sisyphe" Identity or [PersonalityCharge]: On Base Skill final Coin Hit, deal Slash Damage equal to 5% of the said Coin's final damage on the main target (once per Skill)
   PL: — opis] [Efekt wyłącznie dla Tożsamości przydzielonej na 1. pozycji]\n\nPrzy trafieniu ostatnią monetą podstawowej Umiejętności Tożsamości Sisyphe lub [PersonalityCharge], zadaje na głównym celu obrażenia Cięcia równe 5% końcowych obrażeń tej monety (1 raz na Umiejętność)
366. [Dar E.G.O [9291] — opis skrócony] 메인 타겟에게 참격 피해[TabExplain]
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9291].simpleDesc[abilityID=9291].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [TabExplain]
   EN: Deal Slash Damage on the main target
   PL: — opis skrócony] Zadaje obrażenia Cięcia[TabExplain] na głównym celu
367. [Dar E.G.O [19291] — nazwa] 꽃가위+
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=19291].name
   limit: do 40 znaków
   EN: Blossom Scissors+
   PL: — nazwa] Kwiatowe Nożyczki+
368. [Dar E.G.O [19291] — opis] [편성 순서 1번 인격 전용 효과]\n\n시지프 소속 인격 또는 [PersonalityCharge]의 기본 스킬의 마지막 코인 적중 시 메인 타겟에게 해당 코인 최종 피해량의 <style="upgradeHighlight">10%</style>만큼 참격 피해를 줌 (스킬당 1회)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=19291].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: [Effects apply only to #1 Deployed Identity]\n\n"Sisyphe" Identity or [PersonalityCharge]: On Base Skill final Coin Hit, deal Slash Damage equal to <style="upgradeHighlight">10%</style> of the said Coin's final damage on the main target (once per Skill)
   PL: — opis] [Efekt wyłącznie dla Tożsamości przydzielonej na 1. pozycji]\n\nPrzy trafieniu ostatnią monetą podstawowej Umiejętności Tożsamości Sisyphe lub [PersonalityCharge], zadaje na głównym celu obrażenia Cięcia równe <style="upgradeHighlight">10%</style> końcowych obrażeń tej monety (1 raz na Umiejętność)
369. [Dar E.G.O [19291] — opis skrócony] 메인 타겟에게 참격 피해[TabExplain]
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=19291].simpleDesc[abilityID=19291].simpleDesc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Dar E.G.O [29291] — nazwa] 꽃가위++
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=29291].name
   limit: do 40 znaków
   EN: Blossom Scissors++
   PL: — nazwa] Kwiatowe Nożyczki++
371. [Dar E.G.O [29291] — opis] [편성 순서 1번 인격 전용 효과]\n\n시지프 소속 인격 또는 [PersonalityCharge]의 기본 스킬의 마지막 코인 적중 시 메인 타겟에게 해당 코인 최종 피해량의 <style="upgradeHighlight">15%</style>만큼 참격 피해를 줌 (스킬당 1회)
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=29291].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <style="upgradeHighlight">, </style>, \n, [PersonalityCharge]
   znaczenie tagów: [PersonalityCharge] = 충전 인격 / Charge ID
   EN: [Effects apply only to #1 Deployed Identity]\n\n"Sisyphe" Identity or [PersonalityCharge]: On Base Skill final Coin Hit, deal Slash Damage equal to <style="upgradeHighlight">15%</style> of the said Coin's final damage on the main target (once per Skill)
   PL: — opis] [Efekt wyłącznie dla Tożsamości przydzielonej na 1. pozycji]\n\nPrzy trafieniu ostatnią monetą podstawowej Umiejętności Tożsamości Sisyphe lub [PersonalityCharge], zadaje na głównym celu obrażenia Cięcia równe <style="upgradeHighlight">15%</style> końcowych obrażeń tej monety (1 raz na Umiejętność)
372. [Dar E.G.O [29291] — opis skrócony] 메인 타겟에게 참격 피해[TabExplain]
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=29291].simpleDesc[abilityID=29291].simpleDesc
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Dar E.G.O [9301] — nazwa] 폭풍이 치는 언덕
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].name
   limit: do 40 znaków
   EN: Wuthering Heights
   PL: — nazwa] Wichrowe Wzgórza
374. [Dar E.G.O [9301] — opis] 턴 종료시 흐트러짐 상태가 되었을 때, 흐트러짐 상태가 해제되고, 다음 턴 시작 시 모든 적에게 [Sinking] 위력 4, [Sinking] 횟수 4 부여 (전투당 1회 발동, 집중 전투에서는 부위로 판정)\n- 편성된 인격 중 워더링하이츠 소속과 에드가 가문 소속 인격의 합 2명당 전투당 발동 횟수가 1씩 증가 (최대 전투당 4회까지 발동 가능, 대기인원 포함)\n\n적 처치 시 [Sinking] 횟수가 가장 낮은 적 1명의 [Sinking] 횟수 2 증가 (집중 전투에서는 부위로 판정)\n\n정신력을 보유한 적에게 공격 적중시, 대상의 정신력이 -45이면, 대상의 [Sinking] 위력만큼 우울 피해를 입힘\n\n집중 전투에서 [Sinking] 위력과 [Sinking] 횟수의 합이 10 이상인 적에게 공격 적중시, 대상의 ([Sinking] 위력/2) 만큼 우울 피해를 입힘 (스킬당 1회 발동)\n\n적에게 공격 적중한 스킬이 [Sinking](횟수, 특수 [Sinking] 포함)을 부여하는 스킬일 경우, ([Sinking] 위력/2) 대신 ([Sinking] 위력)만큼 우울 피해를 입힘\n(턴에서 처음으로 공격 적중한 [Sinking] 부여 스킬에만 적용)\n\n[<noparse>와일드헌트</noparse> 히스클리프 전용 효과]\n턴 시작시 자신에게 [NightPathfinding]이 없으면, [NightPathfinding]을 1 얻음\n- 자신의 [Coffin]이 5/10이면, 대신 [NightPathfinding]을 2/3 얻음\n- 워더링하이츠, 에드가 가문 소속 인격에게 [SoundOfStorm] 1 부여 (전투 중 인격당 3회)\n\n[Coffin]을 획득할 때 2배로 얻음\n- 워더링하이츠, 에드가 가문 소속 인격이 적 처치 시에도 [Coffin] 2 얻음\n\n‘비탄하고, 애탄하며, 파탄하라’의 사용시 효과로 감소하는 정신력 수치 15 증가\n- 해당 스킬 및 기프트의 효과로 정신력이 -40 미만으로 내려가지 않음\n\n‘비탄하고, 애탄하며, 파탄하라’의 마지막 코인 적중시 적의 [Sinking]이 20 이상이면, 해당 코인 최종 피해량의 100%만큼 우울 피해
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].desc
   limit: do 2230 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [Sinking], [NightPathfinding], [Coffin], [SoundOfStorm]
   znaczenie tagów: [Sinking] = 침잠 / Sinking; [NightPathfinding] = 듀라한 / Dullahan; [Coffin] = 관 / Coffin; [SoundOfStorm] = 우레 / Thundercrack
   EN: Turn End: when Staggered, recover from Stagger; then, at the next Turn Start, inflict 4 [Sinking] Potency and +4 [Sinking] Count to all enemies (once per Encounter; in Focused Encounters, on all Parts)\n- The above effect activates ((deployed "Wuthering Heights" Identities + deployed "Edgar Family" Identities) / 2) more times per Encounter (max 4 times per Encounter; including Backup Units)\n\nOn Kill, 1 enemy that has the least [Sinking] Count gains +2 [Sinking] Count (in Focused Encounters, the Part)\n\nOn Hit against SP Units, if target has -45 SP, deal Gloom damage equal to [Sinking] Potency on target\n\nIn Focused Encounters, On Hit against enemies that have 10+ ([Sinking] Potency + [Sinking] Count):\nDeal (([Sinking] Potency on target) / 2) Gloom damage (once per Skill)\n\nIf the Skill that hit an enemy inflicts [Sinking] (including [Sinking] Count and Unique [Sinking]), instead of dealing ([Sinking] Potency on target / 2) Gloom damage, deal ([Sinking] Potency on target) Gloom damage\n(Each turn, this applies only to the first Sinking-inflicting Skill that hits)\n\n[<noparse>Wild Hunt</noparse> Heathcliff exclusive effect]\nTurn Start: If this unit does not have [NightPathfinding], gain 1 [NightPathfinding]\n- At 5/10 [Coffin], gain 2/3 [NightPathfinding]\n- Apply 1 [SoundOfStorm] on "Wuthering Heights" and "Edgar Family" Identities (3 times per Identity per Encounter)\n\nDouble the amount of [Coffin] gained\n- Gain 2 [Coffin] when "Wuthering Heights" or "Edgar Family" Identities defeat an enemy\n\n"Lament, Mourn, and Despair" Skill effects:\n- Lose 15 more SP from the "On Use" effect\n  · The effects of the Skill or this E.G.O Gift cannot reduce this unit's SP below -40\n- On final Coin Hit, if the enemy has 20+ [Sinking] deal Gloom damage equal to 100% of this Coin's final damage
   PL: — opis] Na koniec tury, gdy jednostka ulega Oszołomieniu, wychodzi z Oszołomienia, a na początku następnej tury nakłada na wszystkich wrogów 4 Moc [Sinking] i 4 Liczniki [Sinking] (1 wywołanie na walkę; w walkach Skupionych — na Partie)\n- Za każde 2 Tożsamości Wichrowych Wzgórz i Rodu Edgarów w składzie wywołania na walkę rosną o 1 (maks. 4 wywołania na walkę, wliczając jednostki zapasowe)\n\nPrzy zabiciu wroga Liczniki [Sinking] 1 wroga o najniższych Licznikach [Sinking] rosną o 2 (w walkach Skupionych — na Partie)\n\nPrzy trafieniu atakiem wroga posiadającego Poczytalność, jeżeli Poczytalność celu wynosi -45, zadaje obrażenia Posępności równe Mocy [Sinking] celu\n\nW walkach Skupionych przy trafieniu atakiem wroga o sumie Mocy [Sinking] i Liczników [Sinking] co najmniej 10, zadaje obrażenia Posępności równe (Moc [Sinking] celu/2) (1 wywołanie na Umiejętność)\n\nJeżeli Umiejętność, która trafiła wroga atakiem, nakłada [Sinking] (wliczając Liczniki i Szczególne [Sinking]), zadaje zamiast tego obrażenia Posępności równe (Moc [Sinking] celu)\n(stosowane tylko dla Umiejętności nakładającej [Sinking], która pierwsza trafiła atakiem w tej turze)\n\n[Efekt wyłącznie dla Dzikiego Gonu Heathcliff]\nNa początku tury, jeżeli nie ma [NightPathfinding], zyskuje 1 [NightPathfinding]\n- Jeżeli [Coffin] jednostki wynosi 5/10, zamiast tego zyskuje 2/3 [NightPathfinding]\n- Nakłada 1 [SoundOfStorm] na Tożsamości Wichrowych Wzgórz i Rodu Edgarów (3 razy na walkę na Tożsamość)\n\nZa każde zyskanie [Coffin] zyskuje 2 razy więcej\n- Tożsamości Wichrowych Wzgórz i Rodu Edgarów zyskują również 2 [Coffin] przy zabiciu wroga\n\nWartość Poczytalności zmniejszana efektem użycia „Zalujcie, Opłakujcie, Rozpaczajcie” rośnie o 15\n- Dzięki temu Umiejętność i Dar nie pozwalają Poczytalności spaść poniżej -40\n\nPrzy trafieniu ostatnią monetą „Zalujcie, Opłakujcie, Rozpaczajcie”, jeżeli [Sinking] wroga wynosi co najmniej 20, zadaje obrażenia Posępności równe 100% końcowych obrażeń tej monety
375. [Dar E.G.O [9301] — opis skrócony] 다음 턴에 모든 적에게 [Sinking] 위력, 횟수 4 부여
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=9432].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Inflict 4 [Sinking] Potency and Count against all enemies next turn
   PL: — opis skrócony] Nakłada 4 Moc [Sinking] i 4 Liczniki [Sinking] na wszystkich wrogach na następną turę
376. [Dar E.G.O [9301] — opis skrócony] [Sinking] 횟수가 가장 낮은 적 [Sinking] 횟수 2 증가
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=94321].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: The enemy with the least [Sinking] Count gains +2 [Sinking] Count
   PL: — opis skrócony] Wróg o najniższych Licznikach [Sinking] zyskuje +2 Liczniki [Sinking]
377. [Dar E.G.O [9301] — opis skrócony] 대상의 [Sinking]에 비례해 우울 피해
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=9436].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: Deal Gloom damage based on [Sinking] on target
   PL: — opis skrócony] Zadaje obrażenia Posępności proporcjonalnie do [Sinking] celu
378. [Dar E.G.O [9301] — opis skrócony] 대상의 [Sinking]에 비례해 우울 피해
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=94361].simpleDesc
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Dar E.G.O [9301] — opis skrócony] [NightPathfinding] 얻음, 특정 소속 인격에게 [SoundOfStorm] 부여
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=93011].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [NightPathfinding], [SoundOfStorm]
   znaczenie tagów: [NightPathfinding] = 듀라한 / Dullahan; [SoundOfStorm] = 우레 / Thundercrack
   EN: Gain [NightPathfinding]; apply [SoundOfStorm] to Identities of certain trait keywords
   PL: — opis skrócony] Zyskuje [NightPathfinding], nakłada [SoundOfStorm] na Tożsamości określonych frakcji
380. [Dar E.G.O [9301] — opis skrócony] [Coffin]을 획득할 때 2배로 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=93012].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Coffin]
   znaczenie tagów: [Coffin] = 관 / Coffin
   EN: Double the amount of [Coffin] gained
   PL: — opis skrócony] Za każde zyskanie [Coffin] zyskuje 2 razy więcej
381. [Dar E.G.O [9301] — opis skrócony] 특정 소속 인격이 적 처치 시 [Coffin] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=93013].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Coffin]
   znaczenie tagów: [Coffin] = 관 / Coffin
   EN: Gain [Coffin] when Identities of certain trait keywords defeat an enemy
   PL: — opis skrócony] Tożsamości określonych frakcji zyskują [Coffin] przy zabiciu wroga
382. [Dar E.G.O [9301] — opis skrócony] ‘비탄하고, 애탄하며, 파탄하라’ 사용시 감소하는 정신력 증가
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=93014].simpleDesc
   limit: do 120 znaków
   EN: "Lament, Mourn, and Despair" loses more SP On Use
   PL: — opis skrócony] Użycie „Zalujcie, Opłakujcie, Rozpaczajcie” kosztuje więcej Poczytalności
383. [Dar E.G.O [9301] — opis skrócony] ‘비탄하고, 애탄하며, 파탄하라’ 마지막 코인 적중시 우울 피해
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9301].simpleDesc[abilityID=93015].simpleDesc
   limit: do 120 znaków
   EN: "Lament, Mourn, and Despair" deals Gloom damage on final Coin Hit
   PL: — opis skrócony] „Zalujcie, Opłakujcie, Rozpaczajcie” zadaje obrażenia Posępności przy trafieniu ostatnią monetą
384. [Dar E.G.O [9302] — nazwa] 서리 온도
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].name
   limit: do 40 znaków
   EN: The Measure of Frost
   PL: — nazwa] Miara Mrozu
385. [Dar E.G.O [9302] — opis] 턴 시작시 정신력이 40 이상이거나 -40 이하이면, [GainSinStockAdder] 1 얻음\n\n[빼기 코인 스킬을 2개 이상 보유한 인격 전용 효과]\n턴 시작시 정신력 15 감소 (해당 효과로 정신력이 -40 미만으로 내려가지 않음)\n\n이번 전투에서 정신력이 -45가 되는 피해를 받았을 때, 해당 턴 동안 정신력이 -44로 유지됨 (전투당 1회)\n(※ 정신력 피해에만 적용되며, 정신력이 변경되거나 E.G.O 스킬 사용과 같이 정신력을 소모하는 경우에는 적용되지 않음)\n\n스킬 3 또는 E.G.O 스킬 공격 시작 전, 스킬 속성과 동일 속성의 E.G.O 자원을 최대 5개 소모하여, (소모한 값 x 10)%만큼 <noparse>피해량 증가</noparse>
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>, \n, [GainSinStockAdder]
   znaczenie tagów: [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp
   EN: Turn Start: At 40+ SP, or at -40 SP or lower, gain 1 [GainSinStockAdder]\n\n[Effect exclusive to Identities that have 2 or more Minus Coin Skills]\nTurn Start: Lose 15 SP (this unit's SP does not drop below -40 from this effect)\n\nIn this Encounter, when taking SP damage that would reduce this unit's SP to -45, this unit's SP cannot drop below -44 for the turn (once per Encounter)\n(※ Applies only to SP damage; does not apply to SP-changing effects, or SP-consuming effects such as using E.G.O Skills)\n\nBefore Attack using Skill 3 or an E.G.O Skill, consume up to 5 E.G.O Resources of the same Affinity as the said Skill to deal +(E.G.O Resources consumed x 10)% damage
   PL: — opis] Na początku tury, jeżeli Poczytalność wynosi co najmniej 40 lub co najwyżej -40, zyskuje 1 [GainSinStockAdder]\n\n[Efekt wyłącznie dla Tożsamości posiadających co najmniej 2 Umiejętności monety Minus]\nNa początku tury traci 15 Poczytalności (dzięki temu efektowi Poczytalność nie spada poniżej -40)\n\nW tej walce, gdy jednostka otrzyma obrażenia Poczytalności obniżające ją do -45, jej Poczytalność pozostaje na -44 przez tę turę (1 raz na walkę)\n(※ stosowane tylko do obrażeń Poczytalności; nie stosuje się, gdy Poczytalność się zmienia lub jest zużywana, np. przez użycie Umiejętności E.G.O)\n\nPrzed rozpoczęciem ataku Umiejętnością 3 lub Umiejętnością E.G.O, zużywa do 5 Zasobów E.G.O tego samego Grzechu co Umiejętność, zadając <noparse>wzrost Obrażeń</noparse> o (zużyta wartość x 10)%
386. [Dar E.G.O [9302] — opis skrócony] 정신력 조건 만족 시 [GainSinStockAdder] 얻음
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].simpleDesc[abilityID=9302].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [GainSinStockAdder]
   znaczenie tagów: [GainSinStockAdder] = E.G.O 자원 획득량 + / E.G.O Resource Amp
   EN: Gain [GainSinStockAdder] when SP conditions are met
   PL: — opis skrócony] Zyskuje [GainSinStockAdder] przy spełnieniu warunku Poczytalności
387. [Dar E.G.O [9302] — opis skrócony] 턴 시작시 정신력 감소
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].simpleDesc[abilityID=93021].simpleDesc
   limit: do 120 znaków
   EN: Turn Start: Lose SP
   PL: — opis skrócony] Na początku tury traci Poczytalność
388. [Dar E.G.O [9302] — opis skrócony] 정신력이 -45 되는 피해를 받으면 1회 버팀
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].simpleDesc[abilityID=93022].simpleDesc
   limit: do 120 znaków
   EN: Maintain SP at -44 once when taking SP damage that would reduce SP to -45
   PL: — opis skrócony] Utrzymuje Poczytalność na -44, gdy otrzyma obrażenia obniżające ją do -45 (1 raz)
389. [Dar E.G.O [9302] — opis skrócony] E.G.O 자원을 소모해 스킬 3, E.G.O 스킬 <noparse>피해량 증가</noparse>
   źródło: EGOgift_MirrorDungeon_8.json :: dataList[id=9302].simpleDesc[abilityID=93023].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <noparse>, </noparse>
   EN: Consume E.G.O Resources to deal more damage using Skill 3 and E.G.O Skills
   PL: — opis skrócony] Zużywa Zasoby E.G.O, by zadawać więcej obrażeń Umiejętnością 3 i Umiejętnościami E.G.O

## Dar E.G.O: EGOgift_StoryDungeon-a1c5p3
- plik gry: `EGOgift_StoryDungeon-a1c5p3.json`

390. [Dar E.G.O [2017] — nazwa] 목 조르는 밧줄
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2017].name
   limit: do 40 znaków
   EN: Noose
   PL: — nazwa] Pętla
391. [Dar E.G.O [2017] — opis] 이스마엘의 레벨이 40레벨로 상승\n이스마엘 인격의 동기화 단계, 에고의 환상해석 단계가 4단계로 상승\n이스마엘은 매 전투마다 [AaCePaBa]을 얻음.
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2017].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [AaCePaBa]
   znaczenie tagów: [AaCePaBa] = 강박 / Compulsion
   EN: Ishmael's level rises to 40.\nIshmael's Uptie and Threadspin Tiers rise to Tier 4.\nIshmael gains [AaCePaBa] at the start of every encounter.
   PL: — opis] Poziom Ishmael rośnie do 40\nEtap Synchronizacji Tożsamości Ishmael i etap Splotu Nici jej E.G.O rosną do 4. etapu\nIshmael zyskuje [AaCePaBa] w każdej walce.
392. [Dar E.G.O [2018] — nazwa] 역방향 매듭
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2018].name
   limit: do 40 znaków
   EN: Reverse Knot
   PL: — nazwa] Węzeł Odwrotny
393. [Dar E.G.O [2018] — opis] 우울 속성 스킬로 합 승리 시 정신력이 가장 낮은 아군 1명의 정신력 5 회복
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2018].desc
   limit: do 120 znaków
   EN: When winning a clash using a Gloom affinity Skill, 1 ally with the lowest SP heals 5 SP
   PL: — opis] Przy wygranej Starciu Umiejętnością Posępności, 1 sojusznik o najniższej Poczytalności odzyskuje 5 Poczytalności
394. [Dar E.G.O [2019] — nazwa] 녹아내린 LCCB 사원증
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2019].name
   limit: do 40 znaków
   EN: Melted LCCB Employee Badge
   PL: — nazwa] Roztopiona Karta LCCB
395. [Dar E.G.O [2019] — opis] 오만 속성 스킬로 받는 피해 -10%
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2019].desc
   limit: do 120 znaków
   EN: Pride damage taken -10%
   PL: — opis] Otrzymuje -10% obrażeń Umiejętnościami Grzechu Pychy
396. [Dar E.G.O [2020] — nazwa] 절박 매듭
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2020].name
   limit: do 40 znaków
   EN: Desperate's Knot
   PL: — nazwa] Węzeł Rozpaczy
397. [Dar E.G.O [2020] — opis] 질투, 분노, 우울 속성 스킬의 피해량 +10%\n해당 속성 스킬의 공명 수가 6 이상이면 해당 속성의 스킬의 피해량 10% 추가 증가
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2020].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +10% damage with Envy, Wrath, and Gloom affinity Skills\nDeal additional +10% corresponding affinity damage when activating 6+ Reson. with one of these affinities
   PL: — opis] Umiejętności Grzechów Zazdrości, Gniewu i Posępności zadają +10% obrażeń\nPrzy Rezonansie 6 lub wyższym jednego z tych Grzechów Umiejętności tego Grzechu zadają dodatkowo +10% obrażeń
398. [Dar E.G.O [2021] — nazwa] 인어 기름
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2021].name
   limit: do 40 znaków
   EN: Mermaid Oil
   PL: — nazwa] Olej Syreny
399. [Dar E.G.O [2021] — opis] [Vibration]을 부여하는 스킬의 진동 부여 값 +1
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2021].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 1 additional [Vibration] with a Skill that inflicts Tremor
   PL: — opis] Umiejętności nakładające [Vibration] nakładają o 1 więcej [Vibration]
400. [Dar E.G.O [2022] — nazwa] 교차 매듭
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2022].name
   limit: do 40 znaków
   EN: Crossed Knot
   PL: — nazwa] Skrzyżowany Węzeł
401. [Dar E.G.O [2022] — opis] 턴 종료 시 이번 턴에 체력이 최대 체력의 15% 이상 감소하였을 때, 다음 턴에 공격 위력 증가 2를 얻음
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2022].desc
   limit: do 130 znaków
   EN: Turn End: if more than 15% of the Max HP was lost this turn, gain 2 Attack Power Up next turn
   PL: — opis] Na koniec tury, jeżeli w tej turze HP spadło o co najmniej 15% Maks. HP, zyskuje 2 Wzrostu Mocy Ataku na następną turę
402. [Dar E.G.O [2023] — nazwa] 강박 매듭
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2023].name
   limit: do 40 znaków
   EN: Compulsive's Knot
   PL: — nazwa] Węzeł Natręctwa
403. [Dar E.G.O [2023] — opis] 정신력이 0 미만일 때 질투, 분노, 우울 속성의 최종 위력 +1
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2023].desc
   limit: do 120 znaków
   EN: When at less than 0 SP, Final Power +1 to Envy, Wrath, and Gloom affinities
   PL: — opis] Przy Poczytalności poniżej 0 Umiejętności Grzechów Zazdrości, Gniewu i Posępności zyskują Moc Końcową +1
404. [Dar E.G.O [2024] — nazwa] 녹슨 갈고리
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2024].name
   limit: do 40 znaków
   EN: Rusted Hook
   PL: — nazwa] Zardzewiały Hak
405. [Dar E.G.O [2024] — opis] [Laceration]이 부여된 적에게 스킬의 첫번째 코인 앞면 적중 시 호흡 1을 얻음
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2024].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Gain 1 Poise when a Skill's first coin Heads Hits against an enemy with [Laceration]
   PL: — opis] Przy trafieniu pierwszą monetą Awersu Umiejętnością na wroga z nałożonym [Laceration], zyskuje 1 Oddech
406. [Dar E.G.O [2025] — nazwa] 보급 탄창
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2025].name
   limit: do 40 znaków
   EN: Standard Issue Mag
   PL: — nazwa] Standardowy Magazynek
407. [Dar E.G.O [2025] — opis] [Bullet]을 보유한 캐릭터의 탄환 최대 값 +3
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2025].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Bullet]
   znaczenie tagów: [Bullet] = 탄환 / Ammo
   EN: Identities with [Bullet] start encounters with +3 max Ammo
   PL: — opis] Postacie posiadające [Bullet] zyskują maksymalną wartość amunicji +3
408. [Dar E.G.O [2026] — nazwa] 풀리지 않는 매듭
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2026].name
   limit: do 40 znaków
   EN: Unbreakable Knot
   PL: — nazwa] Nierozwiązywalny Węzeł
409. [Dar E.G.O [2026] — opis] 이스마엘의 모든 스킬의 최종 위력 +2\n아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 신속, 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: EGOgift_StoryDungeon-a1c5p3.json :: dataList[id=2026].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ishmael's Skills gain +2 Final Power\nWhen an ally dies, remaining allies gain 1 Haste and 1 Attack Power Up next turn (Once per turn)
   PL: — opis] Wszystkie Umiejętności Ishmael zyskują Moc Końcową +2\nGdy sojusznik ginie, pozostali sojusznicy zyskują 1 Pośpiech i 1 Wzrost Mocy Ataku na następną turę (1 raz na turę)

## Dar E.G.O: EGOgift_StoryDungeon-a1c7p3
- plik gry: `EGOgift_StoryDungeon-a1c7p3.json`

410. [Dar E.G.O [2047] — nazwa] 깨어진 꿈
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2047].name
   limit: do 40 znaków
   EN: A Broken Dream
   PL: — nazwa] Rozbite Marzenie
411. [Dar E.G.O [2047] — opis] 에고 기프트 획득 시 던전 내에서 아래의 효과 적용\n• 돈키호테의 레벨이 50레벨로 상승\n• 돈키호테 인격의 동기화 단계, E.G.O의 환상해석 단계가 4단계로 상승\n(레벨, 동기화, 환상해석 단계가 더 높은 경우 유지함.)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2047].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon obtaining this E.G.O Gift, gain the following effects:\n• Don Quixote's level rises to 50\n• Don Quixote's Uptie and Threadspin Tiers rise to Tier 4\n(If the Level, Uptie Tier, or Threadspin Tier are higher than the above values, then maintain those values.)
   PL: — opis] Przy zdobyciu tego Daru E.G.O stosuje w lochu następujące efekty\n• Poziom Don Kichota rośnie do 50\n• Etap Synchronizacji Tożsamości Don Kichota i etap Splotu Nici E.G.O rosną do 4. etapu\n(jeżeli Poziom, Synchronizacja lub Splot Nici mają wyższe wartości, są zachowywane.)
412. [Dar E.G.O [2047] — opis skrócony] 돈키호테의 레벨이 50레벨로 상승
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2047].simpleDesc[abilityID=2047].simpleDesc
   limit: do 120 znaków
   EN: Don Quixote's level rises to 50
   PL: — opis skrócony] Poziom Don Kichota rośnie do 50
413. [Dar E.G.O [2047] — opis skrócony] 돈키호테 인격의 동기화 단계, E.G.O의 환상해석 단계가 4단계로 상승
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2047].simpleDesc[abilityID=204701].simpleDesc
   limit: do 120 znaków
   EN: Don Quixote's Uptie and Threadspin Tiers rise to Tier 4
   PL: — opis skrócony] Etap Synchronizacji Tożsamości Don Kichota i etap Splotu Nici E.G.O rosną do 4. etapu
414. [Dar E.G.O [2048] — nazwa] 라만차랜드 자유이용권
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2048].name
   limit: do 40 znaków
   EN: La Manchaland All-day Pass
   PL: — nazwa] Bilet Całodniowy La Manchaland
415. [Dar E.G.O [2048] — opis] [Laceration], 특수 출혈과 [Burst]의 합이 10 이상 부여된 적에게 공격 적중 시 [Breath] 위력 1을 얻고, 자신의 [Breath] 횟수 1 증가 (스킬당 최대 3회 발동)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2048].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Burst], [Breath]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: On Hit against targets with 10+ (sum of [Laceration], 'Unique Bleed', and [Burst]): gain 1 [Breath] Potency and Count (3 times per Skill)
   PL: — opis] Przy trafieniu celu z sumą [Laceration], Szczególnego Krwawienia i [Burst] co najmniej 10, zyskuje 1 Moc [Breath] i Liczniki [Breath] +1 (maks. 3 razy na Umiejętność)
416. [Dar E.G.O [2048] — opis skrócony] [Laceration], 특수 출혈과 [Burst]의 합이 10 이상 부여된 적에게 공격 적중 시, [Breath] 위력 1을 얻고, 자신의 [Breath] 횟수 1 증가
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2048].simpleDesc[abilityID=2048].simpleDesc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Burst], [Breath]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: On Hit against targets with 10+ (sum of [Laceration], 'Unique Bleed', and [Burst]): gain 1 [Breath] Potency and Count
   PL: — opis skrócony] Przy trafieniu celu z sumą [Laceration], Szczególnego Krwawienia i [Burst] co najmniej 10, zyskuje 1 Moc [Breath] i Liczniki [Breath] +1
417. [Dar E.G.O [2049] — nazwa] 라만차랜드 일반이용권
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2049].name
   limit: do 40 znaków
   EN: La Manchaland Standard Pass
   PL: — nazwa] Przepustek La Manchalandu
418. [Dar E.G.O [2049] — opis] 스테이지 1턴 시작 시 모든 캐릭터가 [Laceration] 위력 4, [Laceration] 횟수 4를 얻음.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2049].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: First Turn Start of an Encounter: all units gain 4 [Laceration] Potency and Count.
   PL: — opis] Na początku 1. tury spotkania wszystkie Postacie zyskują 4 Moc [Laceration] i 4 Liczniki [Laceration].
419. [Dar E.G.O [2049] — opis skrócony] 스테이지 1턴 시작 시 모든 캐릭터가 [Laceration] 위력 4, [Laceration] 횟수 4를 얻음.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2049].simpleDesc[abilityID=2049].simpleDesc
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Dar E.G.O [2050] — nazwa] 승리의 증표
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2050].name
   limit: do 40 znaków
   EN: Token of Victory
   PL: — nazwa] Znak Zwycięstwa
421. [Dar E.G.O [2050] — opis] 스킬 피해로 적 처치 시 현재 정신력이 가장 낮은 아군 1명의 정신력 8 회복.\n공격 종료 시 [Laceration], 특수 출혈과 [Burst]의 합이 10 이상 부여된 적이 사망한 경우, 다음 턴에 처치한 캐릭터가 [AttackUp] 2 얻음. (턴 당 3회 발동)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2050].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: On Kill with a Skill damage: 1 ally with the least SP heals 8 SP.\nAttack End: If an enemy with 10+ (sum of [Laceration], 'Unique Bleed', and [Burst]) is defeated, the unit who killed that enemy gains 2 [AttackUp] next turn. (3 times per turn)
   PL: — opis] Przy zabiciu wroga obrażeniami Umiejętności, 1 sojusznik o najniższej Poczytalności odzyskuje 8 Poczytalności.\nNa koniec ataku, jeżeli ginie wróg z sumą [Laceration], Szczególnego Krwawienia i [Burst] co najmniej 10, pokonująca go Postać zyskuje 2 [AttackUp] na następną turę. (3 razy na turę)
422. [Dar E.G.O [2050] — opis skrócony] 적 처치 시 현재 정신력이 가장 낮은 아군 1명의 정신력 8 회복.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2050].simpleDesc[abilityID=2050].simpleDesc
   limit: do 120 znaków
   EN: On Kill, 1 ally with the least SP heals 8 SP.
   PL: — opis skrócony] Przy zabiciu wroga, 1 sojusznik o najniższej obecnej Poczytalności odzyskuje 8 Poczytalności.
423. [Dar E.G.O [2050] — opis skrócony] 공격 종료 시 [Laceration], 특수 출혈과 [Burst]의 총합이 10 이상 부여된 적이 사망한 경우, 다음 턴에 처치한 캐릭터가 [AttackUp] 2 얻음.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2050].simpleDesc[abilityID=205001].simpleDesc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Burst], [AttackUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Attack End: If an enemy with 10+ (sum of [Laceration], 'Unique Bleed', and [Burst]) is defeated, the unit who killed that enemy gains 2 [AttackUp] next turn.
   PL: — opis skrócony] Na koniec ataku, jeżeli ginie wróg z sumą [Laceration], Szczególnego Krwawienia i [Burst] co najmniej 10, pokonująca go Postać zyskuje 2 [AttackUp] na następną turę.
424. [Dar E.G.O [2051] — nazwa] 고해 채찍
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2051].name
   limit: do 40 znaków
   EN: Self-flagellation Whip
   PL: — nazwa] Bicz Samoumęczenia
425. [Dar E.G.O [2051] — opis] 현재 체력 비율이 가장 높은 아군 1명이 공격 스킬 사용 시 [Laceration]을 10 얻고, [AttackUp] 3, [DefenseUp] 3 얻음.(턴 당 최대 1회)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2051].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Laceration], [AttackUp], [DefenseUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: When 1 ally with currently the highest HP percentage uses an Attack Skill, gain 10 [Laceration], 3 [AttackUp], and 3 [DefenseUp]. (once per turn)
   PL: — opis] Gdy 1 sojusznik o najwyższym aktualnym HP% użyje Umiejętności ataku, zyskuje 10 [Laceration], 3 [AttackUp] i 3 [DefenseUp]. (maks. 1 raz na turę)
426. [Dar E.G.O [2051] — opis skrócony] 현재 체력 비율이 가장 높은 아군 1명이 공격 스킬 사용 시 [Laceration]을 10 얻고, [AttackUp] 3, [DefenseUp] 3 얻음.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2051].simpleDesc[abilityID=2051].simpleDesc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [Laceration], [AttackUp], [DefenseUp]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: When 1 ally with currently the highest HP percentage uses an Attack Skill, gain 10 [Laceration], 3 [AttackUp], and 3 [DefenseUp].
   PL: — opis skrócony] Gdy 1 sojusznik o najwyższym aktualnym HP% użyje Umiejętności ataku, zyskuje 10 [Laceration], 3 [AttackUp] i 3 [DefenseUp].
427. [Dar E.G.O [2052] — nazwa] 퍼레이드의 가면
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2052].name
   limit: do 40 znaków
   EN: Mask of the Parade
   PL: — nazwa] Maska Parady
428. [Dar E.G.O [2052] — opis] 연속 전투에서 새로운 적이 등장하면, 전투 시작 시 해당 적에게 [Laceration] 5, [Laceration] 횟수 3 부여.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2052].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Chain Battles: when a new enemy enters the battle, inflict 5 [Laceration] and +3 [Laceration] Count against that enemy at Combat Start.
   PL: — opis] Walki Łańcuchowe: gdy pojawi się nowy wróg, nakłada na niego na początku walki 5 [Laceration] i 3 Liczniki [Laceration].
429. [Dar E.G.O [2052] — opis skrócony] 연속 전투에서 새로운 적이 등장하면, 전투 시작 시 해당 적에게 [Laceration] 5, [Laceration] 횟수 3 부여.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2052].simpleDesc[abilityID=2052].simpleDesc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Dar E.G.O [2053] — nazwa] 먹어치우는 큐브
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2053].name
   limit: do 40 znaków
   EN: Devouring Cube
   PL: — nazwa] Żarłoczny Sześcian
431. [Dar E.G.O [2053] — opis] 아군 사망 시 해당 아군의 1,2,3스킬 속성의 E.G.O 자원 1개씩과 무작위 E.G.O 자원 1개 획득\n공격 종료 시 적이 사망했다면, 무작위 E.G.O 자원 1개 획득 (스킬당 최대 1회)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2053].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When an ally dies, gain 1 E.G.O resource for each of that ally's Skills 1, 2, and 3 and 1 random E.G.O resource\nAttack End: If the enemy is killed, gain 1 random E.G.O resource (once per Skill)
   PL: — opis] Gdy ginie sojusznik, zyskuje po 1 Zasobie E.G.O Grzechu Umiejętności 1, 2 i 3 tego sojusznika oraz 1 losowy Zasób E.G.O\nNa koniec ataku, jeżeli wróg ginie, zyskuje 1 losowy Zasób E.G.O (maks. 1 raz na Umiejętność)
432. [Dar E.G.O [2053] — opis skrócony] 아군 사망 시 해당 아군의 1,2,3스킬 속성의 E.G.O 자원 1개씩과 무작위 E.G.O 자원 1개 획득
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2053].simpleDesc[abilityID=2053].simpleDesc
   limit: do 150 znaków
   EN: When an ally dies, gain 1 E.G.O resource for each of that ally's Skills 1, 2, and 3 and 1 random E.G.O resource
   PL: — opis skrócony] Gdy ginie sojusznik, zyskuje po 1 Zasobie E.G.O Grzechu Umiejętności 1, 2 i 3 tego sojusznika oraz 1 losowy Zasób E.G.O
433. [Dar E.G.O [2053] — opis skrócony] 공격 종료 시 적이 사망했다면, 무작위 E.G.O 자원 1개 획득
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2053].simpleDesc[abilityID=205301].simpleDesc
   limit: do 120 znaków
   EN: Attack End: If the enemy is killed, gain 1 random E.G.O resource (once per Skill)
   PL: — opis skrócony] Na koniec ataku, jeżeli wróg ginie, zyskuje 1 losowy Zasób E.G.O
434. [Dar E.G.O [2054] — nazwa] 끝없는 허기
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2054].name
   limit: do 40 znaków
   EN: Endless Hunger
   PL: — nazwa] Nieustający Głód
435. [Dar E.G.O [2054] — opis] 스테이지 1턴 시작 시 전투에 배치된 인격의 정신력이 5 감소하고, 해당 인격이 3턴동안 [Enhancement] 1 얻음.\n혈귀 인격인 경우, 정신력 10 감소. 3턴동안 [Enhancement] 2를 얻고, 스킬, 코인의 효과로 [Laceration] 위력, 횟수를 부여할 때 부여량 +1
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2054].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Laceration]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Laceration] = 출혈 / Bleed
   EN: First Turn Start of an Encounter: every Identity on the field loses 5 SP and gains 1 [Enhancement] for 3 turns.\nIf the said Identity is a Bloodfiend, lose 10 SP, gain 2 [Enhancement] for 3 turns, and inflict +1 more [Laceration] Potency and Count with its Skill & Coin effects
   PL: — opis] Na początku 1. tury spotkania Poczytalność Tożsamości na polu maleje o 5, a ta Tożsamość zyskuje 1 [Enhancement] na 3 tury.\nJeżeli Tożsamość jest Krwiożercą, traci 10 Poczytalności; zyskuje 2 [Enhancement] na 3 tury, a przy nakładaniu Mocy [Laceration] i Liczników [Laceration] efektem Umiejętności lub Monety nakłada o 1 więcej
436. [Dar E.G.O [2054] — opis skrócony] 스테이지 1턴 시작 시 전투에 배치된 인격의 정신력이 5 감소하고, 해당 인격이 3턴동안 [Enhancement] 1 얻음.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2054].simpleDesc[abilityID=2054].simpleDesc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: First Turn Start of an Encounter: every Identity on the field loses 5 SP and gains 1 [Enhancement] for 3 turns.
   PL: — opis skrócony] Na początku 1. tury spotkania Poczytalność Tożsamości na polu maleje o 5, a ta Tożsamość zyskuje 1 [Enhancement] na 3 tury.
437. [Dar E.G.O [2054] — opis skrócony] 혈귀 인격인 경우, 정신력 10 감소하고, 3턴동안 [Enhancement] 2를 얻고, 스킬, 코인의 효과로 부여하는 [Laceration] 위력, 횟수 +1
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2054].simpleDesc[abilityID=205401].simpleDesc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Laceration]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Laceration] = 출혈 / Bleed
   EN: If the said Identity is a Bloodfiend, lose 10 SP, gain 2 [Enhancement] for 3 turns, and inflict +1 more [Laceration] Potency and Count with its Skill & Coin effects
   PL: — opis skrócony] Jeżeli Tożsamość jest Krwiożercą, traci 10 Poczytalności; zyskuje 2 [Enhancement] na 3 tury, a przy nakładaniu Mocy i Liczników [Laceration] efektem Umiejętności lub Monety nakłada o 1 więcej
438. [Dar E.G.O [2055] — nazwa] 작은 꿈
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2055].name
   limit: do 40 znaków
   EN: A Little Dream
   PL: — nazwa] Małe Marzenie
439. [Dar E.G.O [2055] — opis] 오만 속성의 스킬로 합 승리 시 정신력 5 회복.\n해당 스킬로 합 승리 후 적중 시 대상의 [Laceration] 횟수, [Burst] 횟수 1 증가 (스킬 당 최대 4회)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2055].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [Burst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: On Clash Win with a Pride Skill: heal 5 SP.\nOn Hit after Clash Win with the said Skill: inflict +1 [Laceration] Count and +1 [Burst] Count (4 times per Skill)
   PL: — opis] Przy wygranej Starciu Umiejętnością Grzechu Pychy odzyskuje 5 Poczytalności.\nPrzy trafieniu po wygranej tą Umiejętnością, zwiększa Liczniki [Laceration] i [Burst] celu o 1 (maks. 4 na Umiejętność)
440. [Dar E.G.O [2055] — opis skrócony] 오만 속성의 스킬로 합 승리 시 정신력 5 회복하고, 합 승리 후 적중시 대상의 [Laceration] 횟수, [Burst] 횟수 1 증가
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2055].simpleDesc[abilityID=2055].simpleDesc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Burst]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Burst] = 파열 / Rupture
   EN: On Clash Win with a Pride Skill: heal 5 SP, and On Hit after Clash Win with the said Skill, inflict +1 [Laceration] Count and +1 [Burst] Count
   PL: — opis skrócony] Przy wygranej Starciu Umiejętnością Grzechu Pychy odzyskuje 5 Poczytalności, a przy trafieniu po wygranej Starciu zwiększa Liczniki [Laceration] i Liczniki [Burst] celu o 1
441. [Dar E.G.O [2056] — nazwa] 허황된 꿈
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2056].name
   limit: do 40 znaków
   EN: A Hollow Dream
   PL: — nazwa] Puste Marzenie
442. [Dar E.G.O [2056] — opis] [Laceration] 또는 특수 출혈이 부여된 대상에게 공격 적중 시 체력 2-5 회복.\n[BloodDinner]을 소모하는 스킬의 코인 위력 +1
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2056].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [BloodDinner]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [BloodDinner] = 혈찬 / Bloodfeast
   EN: On Hit against targets with [Laceration] or 'Unique Bleed': heal 2~5 HP.\nSkills that consume [BloodDinner]: Coin Power +1
   PL: — opis] Przy trafieniu celu z [Laceration] lub Szczególnym Krwawieniem, odzyskuje 2-5 HP.\nUmiejętności zużywające [BloodDinner] zyskują Moc Monet +1
443. [Dar E.G.O [2056] — opis skrócony] [Laceration] 또는 특수 출혈이 부여된 대상에게 공격 적중 시 체력 회복.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2056].simpleDesc[abilityID=2056].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Heal HP On Hit against targets with [Laceration] or 'Unique Bleed'.
   PL: — opis skrócony] Odzyskuje HP przy trafieniu atakiem celu z nałożonym [Laceration] lub Szczególnym Krwawieniem.
444. [Dar E.G.O [2056] — opis skrócony] [BloodDinner]을 소모하는 스킬의 코인 위력 +1
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2056].simpleDesc[abilityID=205601].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BloodDinner]
   znaczenie tagów: [BloodDinner] = 혈찬 / Bloodfeast
   EN: Skills that consume [BloodDinner]: Coin Power +1
   PL: — opis skrócony] Umiejętności zużywające [BloodDinner] zyskują Moc Monet +1
445. [Dar E.G.O [2057] — nazwa] 다시 꾸는 꿈
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2057].name
   limit: do 40 znaków
   EN: The Dream Begins Anew
   PL: — nazwa] Marzenie na Nowo
446. [Dar E.G.O [2057] — opis] 돈키호테의 모든 스킬의 최종 위력 +2\n아군이 사망한 경우, 남은 아군이 정신력을 15 회복하고, 턴 종료 시 다음 턴에 [Enhancement] 1을 얻음 (최대 [Enhancement] 획득량 : 3)
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2057].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: All of Don Quixote's Skills gain Final Power +2\nWhen an ally dies, the remaining allies heal 15 SP, and at Turn End, gain 1 [Enhancement] next turn (max [Enhancement]: 3)
   PL: — opis] Wszystkie Umiejętności Don Kichota zyskują Moc Końcową +2\nGdy ginie sojusznik, sojusznicy odzyskują 15 Poczytalności, a na koniec tury zyskują 1 [Enhancement] na następną turę (maks. zdobytych [Enhancement]: 3)
447. [Dar E.G.O [2057] — opis skrócony] 돈키호테의 모든 스킬의 최종 위력 +2
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2057].simpleDesc[abilityID=2057].simpleDesc
   limit: do 120 znaków
   EN: Don Quixote's Skill Final Power +2
   PL: — opis skrócony] Wszystkie Umiejętności Don Kichota zyskują Moc Końcową +2
448. [Dar E.G.O [2057] — opis skrócony] 아군이 사망한 경우, 남은 아군이 정신력을 15 회복하고, 턴 종료 시 다음 턴에 [Enhancement] 1을 얻음
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2057].simpleDesc[abilityID=205701].simpleDesc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Enhancement]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: When an ally dies, the remaining allies heal 15 SP, and at Turn End, gain 1 [Enhancement] next turn
   PL: — opis skrócony] Gdy ginie sojusznik, sojusznicy odzyskują 15 Poczytalności i zyskują 1 [Enhancement] na następną turę
449. [Dar E.G.O [2058] — nazwa] 늘어붙은 쇠말뚝
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2058].name
   limit: do 40 znaków
   EN: Grimy Iron Stake
   PL: Oblepiony Żelazny Pal
450. [Dar E.G.O [2058] — opis] 단일 코인 스킬을 사용하여 적에게 적중 시, 대상에게 [Laceration] 위력 1 부여하고 다음 턴까지 [DefenseDown] 2 부여.\n\n대상이 [Laceration]또는 특수 출혈에 걸린 상태일 경우, 효과가 강화되어 [Laceration] 위력 3 부여.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2058].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [Laceration], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: When hitting an enemy using a single-Coin Skill, inflict 1 [Laceration] Potency. Inflict 2 [DefenseDown] until the end of the next turn.\nIf the target already has [Laceration] or 'Unique Bleed', inflict 3 [Laceration] Potency instead.
   PL: — opis] Przy trafieniu wroga Umiejętnością z jedną monetą, nakłada 1 Moc [Laceration] i 2 [DefenseDown] do końca następnej tury.\n\nJeżeli cel jest w stanie [Laceration] lub 'Szczególnego Krwawienia', efekt jest wzmocniony i nakłada 3 Moc [Laceration].
451. [Dar E.G.O [2058] — opis skrócony] [Laceration] 위력 1 부여. 다음 턴까지 [DefenseDown] 2 부여
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2058].simpleDesc[abilityID=2058].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [DefenseDown]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Inflict 1 [Laceration] Potency. Inflict 2 [DefenseDown] until the end of the next turn
   PL: — opis skrócony] Nakłada 1 Moc [Laceration]. Nakłada 2 [DefenseDown] do końca następnej tury
452. [Dar E.G.O [2058] — opis skrócony] [Laceration] 위력 3 부여
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2058].simpleDesc[abilityID=205801].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Inflict 3 [Laceration] Potency
   PL: — opis skrócony] Nakłada 3 Moc [Laceration]
453. [Dar E.G.O [2059] — nazwa] 가시 올가미
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2059].name
   limit: do 40 znaków
   EN: Barbed Lasso
   PL: Kolczaste Lasso
454. [Dar E.G.O [2059] — opis] 턴 종료 시, 모든 적에게 현재 속도만큼 [Burst] 위력을 부여.\n\n색욕 완전 공명을 발동하였다면 전투 시작 시, 무작위 적 하나에게 [Burst] 위력 3, [Burst] 횟수 3 부여.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2059].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Turn End: Inflict [Burst] Potency on all enemies equal to their current Speed values.\n\nWhen activating Lust Absolute Resonance, apply 3 [Burst] Potency and +3 [Burst] Count to a random enemy at Combat Start.
   PL: — opis] Na koniec tury nakłada Moc [Burst] równą ich bieżącej Szybkości wszystkim wrogom.\n\nPrzy wywołaniu Pełnego Rezonansu Żądzy, na początku walki nakłada 3 Moc [Burst] i 3 Liczniki [Burst] na losowego wroga.
455. [Dar E.G.O [2059] — opis skrócony] 현재 속도만큼 [Burst] 위력 부여
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2059].simpleDesc[abilityID=2059].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Inflict [Burst] Potency by Speed
   PL: — opis skrócony] Nakłada Moc [Burst] równą Szybkości
456. [Dar E.G.O [2059] — opis skrócony] [Burst] 위력 3, [Burst] 횟수 3 부여
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2059].simpleDesc[abilityID=205901].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Inflict 3 [Burst] Potency and +3 [Burst] Count
   PL: — opis skrócony] Nakłada 3 Moc [Burst] i +3 Liczniki [Burst]
457. [Dar E.G.O [2060] — nazwa] 카르밀라
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2060].name
   limit: do 40 znaków
   EN: Carmilla
   PL: Carmilla
458. [Dar E.G.O [2060] — opis] 집중 전투 방식이 아닌 전투 스테이지 입장 시, 모든 적에게 최대 체력 20%만큼 고정 피해를 입힘.
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2060].desc
   limit: do 130 znaków
   EN: At the start of a non-Focused Encounter, all enemies take fixed damage equal to 20% of their Max HP.
   PL: — opis] Na początku spotkania innego niż potyczki skupione zadaje obrażenia stałe równe 20% Maks. HP wszystkim wrogom.
459. [Dar E.G.O [2060] — opis skrócony] 최대 체력 20%만큼 고정 피해
   źródło: EGOgift_StoryDungeon-a1c7p3.json :: dataList[id=2060].simpleDesc[abilityID=2060].simpleDesc
   limit: do 120 znaków
   EN: Deal 20% of Max HP as fixed damage
   PL: — opis skrócony] Zadaje obrażenia stałe równe 20% Maks. HP

## Dar E.G.O: EGOgift_StoryDungeon-tkt
- plik gry: `EGOgift_StoryDungeon-tkt.json`

460. [Dar E.G.O [2036] — nazwa] 은빛 시계 케이스
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2036].name
   limit: do 40 znaków
   EN: Silver Watch Case
   PL: — nazwa] Srebrne Etui na Zegarek
461. [Dar E.G.O [2036] — opis] [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬(E.G.O 스킬 제외)로 적에게 피해를 입힐 때, 가하는 피해량 +10%.\n\n해당 스킬로 적에게 이번 턴 동안 처음으로 [VibrationExplosion]을 적용하였다면, 다음 턴에 [Vibration] 횟수 2 부여 (턴 당 1회).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2036].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [VibrationExplosion]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: When dealing damage to an enemy with Attack Skills(Not counting E.G.O Skills) that inflict [Vibration] Potency, Count, or Unique Tremor, deal +10% damage.\n\nIf the Skill triggered [VibrationExplosion] on the enemy for the first time this turn, inflict +2 [Vibration] Count next turn (once per turn)
   PL: — opis] Gdy Umiejętność ataku (poza Umiejętnościami E.G.O) nakładająca Moc [Vibration], Licznik [Vibration] lub 'Szczególny Wstrząs' zadaje wrogowi obrażenia, zadaje +10% obrażeń.\n\nJeżeli ta Umiejętność po raz pierwszy w tej turze wywoła [VibrationExplosion] na wrogu, nakłada w następnej turze +2 Licznika [Vibration] (1 raz na turę).
462. [Dar E.G.O [2036] — opis skrócony] 가하는 피해량 +10%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2036].simpleDesc[abilityID=2036].simpleDesc
   limit: do 120 znaków
   EN: Deal +10% damage
   PL: — opis skrócony] Zadaje +10% obrażeń
463. [Dar E.G.O [2036] — opis skrócony] 다음 턴에 [Vibration] 횟수 2 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2036].simpleDesc[abilityID=20361].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict +2 [Vibration] Count next turn
   PL: — opis skrócony] Nakłada w następnej turze +2 Licznika [Vibration]
464. [Dar E.G.O [2037] — nazwa] 빛바랜 시계 케이스
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2037].name
   limit: do 40 znaków
   EN: Faded Watch Case
   PL: — nazwa] Wyblakłe Etui na Zegarek
465. [Dar E.G.O [2037] — opis] 자신보다 속도가 높은 적과 합을 진행할 때, 합 위력 +1.\n\n자신보다 속도가 높은 적에게 피해를 가할 때, 다음 턴에 대상에게 [Vibration] 위력 3, [Vibration] 횟수 2 부여 (턴 당 1회).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2037].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When Clashing with a faster enemy, Clash Power +1.\n\nWhen dealing damage to a faster enemy, inflict 3 [Vibration] Potency and +2 [Vibration] Count next turn. (once per turn)
   PL: — opis] Podczas starcia z wrogiem szybszym niż jednostka, Moc Starcia +1.\n\nGdy zadaje obrażenia wrogowi szybszemu, nakłada w następnej turze 3 Moc [Vibration] i +2 Licznika [Vibration] na cel (1 raz na turę).
466. [Dar E.G.O [2037] — opis skrócony] 합 위력 +1
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2037].simpleDesc[abilityID=2037].simpleDesc
   limit: do 120 znaków
   EN: Clash Power +1
   PL: — opis skrócony] Moc Starcia +1
467. [Dar E.G.O [2037] — opis skrócony] 다음 턴에 [Vibration] 위력 3, [Vibration] 횟수 2 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2037].simpleDesc[abilityID=20371].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 3 [Vibration] Potency and +2 [Vibration] Count next turn
   PL: — opis skrócony] Nakłada w następnej turze 3 Moc [Vibration] i +2 Licznika [Vibration]
468. [Dar E.G.O [2038] — nazwa] 경고장
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2038].name
   limit: do 40 znaków
   EN: Warning Notice
   PL: — nazwa] Ostrzeżenie
469. [Dar E.G.O [2038] — opis] 턴 종료 시, 속도가 제일 빠른 적 1명에게 다음 턴에 [Binding] 1 부여 (환상체일 경우, 부위 하나).\n\n대상이 [Vibration] 또는 특수 진동을 보유한 경우, 효과가 강화되어 [Binding] 2 부여.\n\n아군이 [Binding]을 보유한 대상을 공격할 때, 가하는 피해량 +(5 + [[Binding] 수치x2.5])% (최대 15%).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2038].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [Vibration]
   znaczenie tagów: [Binding] = 속박 / Bind; [Vibration] = 진동 / Tremor
   EN: Turn End: Inflict 1 [Binding] to the fastest enemy next turn. (for Abnormalities, a Part)\n\nIf the target has [Vibration] or 'Unique Tremor', inflict 2 [Binding] instead.\n\nWhen an ally attacks targets with [Binding], deal +(5 + (2.5 x [Binding] value)) more damage. (max 15%)
   PL: — opis] Na koniec tury nakłada w następnej turze 1 [Binding] na najszybszego wroga (w przypadku Anomalii — jedna Partia).\n\nJeżeli cel ma [Vibration] lub 'Szczególny Wstrząs', zamiast tego nakłada 2 [Binding].\n\nGdy sojusznik atakuje cel z [Binding], zadaje +(5 + (2.5 x wartość [Binding]))% obrażeń (maks. 15%).
470. [Dar E.G.O [2038] — opis skrócony] 다음 턴에 [Binding] 1 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2038].simpleDesc[abilityID=2038].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Apply 1 [Binding] next turn
   PL: — opis skrócony] Nakłada 1 [Binding] w następnej turze
471. [Dar E.G.O [2038] — opis skrócony] 가하는 피해량 +(5 + [[Binding] 수치x2.5])%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2038].simpleDesc[abilityID=20381].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding]
   znaczenie tagów: [Binding] = 속박 / Bind
   EN: Deal +(5 + (2.5 x [Binding] value)) more damage
   PL: — opis skrócony] Zadaje +(5 + (2.5 x wartość [Binding]))% obrażeń
472. [Dar E.G.O [2039] — nazwa] 에칭 시계침
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2039].name
   limit: do 40 znaków
   EN: Etched Clock Hands
   PL: — nazwa] Grawerowane Wskazówki Zegara
473. [Dar E.G.O [2039] — opis] 웨이브 첫 턴 시작 시, 속도가 제일 낮은 적 3명에게 (9-현재 속도)만큼 [Vibration] 위력 부여 (최소 3).\n\n턴 시작 시 [Vibration] 또는 특수 진동을 12 이상 보유한 적을 대상으로 가하는 피해량 +10%.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2039].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: First Turn Start of a wave: inflict (9 - current Speed) [Vibration] Potency to 3 enemies with the slowest Speed. (min. 3)\n\nDeal +10% damage against targets with 12+ [Vibration] or 'Unique Tremor' at Turn Start.
   PL: — opis] Na pierwszym początku tury fali nakłada Moc [Vibration] równą (9-bieżąca Szybkość) na 3 wrogów z najniższą Szybkością (min. 3).\n\nZadaje +10% obrażeń celom z 12+ Moc [Vibration] lub 'Szczególny Wstrząs' na początku tury.
474. [Dar E.G.O [2039] — opis skrócony] (9-현재 속도)만큼 [Vibration] 위력 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2039].simpleDesc[abilityID=2039].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict (9 - current Speed) [Vibration] Potency
   PL: — opis skrócony] Nakłada Moc [Vibration] równą (9-bieżąca Szybkość)
475. [Dar E.G.O [2039] — opis skrócony] 가하는 피해량 +10%.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2039].simpleDesc[abilityID=20391].simpleDesc
   limit: do 120 znaków
   EN: Deal +10% damage
   PL: — opis skrócony] Zadaje +10% obrażeń.
476. [Dar E.G.O [2040] — nazwa] 녹슨 시계침
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2040].name
   limit: do 40 znaków
   EN: Rusted Clock Hands
   PL: — nazwa] Zardzewiałe Wskazówki Zegara
477. [Dar E.G.O [2040] — opis] 웨이브 첫 턴 시작 시, 속도가 제일 높은 적 1명에게 (9-현재 속도)만큼 [Vibration] 위력(최소 3)과 그 수치의 절반만큼 [Vibration] 횟수를 부여(올림하여 처리, 환상체일 경우 부위 하나).\n\n턴 시작 시 [Vibration] 또는 특수 진동을 12 이상 보유한 적에게 받는 피해량 -10%.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2040].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: First Turn Start of a wave: inflict (9 - current Speed) [Vibration] Potency (min. 3) and (9 - current Speed)/2 [Vibration] Count to 1 enemy with the fastest Speed. (rounded up; for Abnormalities, a Part)\n\nTake -10% damage from targets with 12+ [Vibration] or 'Unique Tremor' at Turn Start.
   PL: — opis] Na pierwszym początku tury fali nakłada (9-bieżąca Szybkość) Moc [Vibration] (min. 3) i tyle samo Licznika [Vibration], ile wynosi połowa tej wartości (zaokrąglone w górę; w przypadku Anomalii — jedna Partia) na 1 wroga z najwyższą Szybkością.\n\nOtrzymuje -10% obrażeń od celów z 12+ Moc [Vibration] lub 'Szczególny Wstrząs' na początku tury.
478. [Dar E.G.O [2040] — opis skrócony] (9-현재 속도)만큼 [Vibration] 위력과 그 수치의 절반만큼 [Vibration] 횟수 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2040].simpleDesc[abilityID=2040].simpleDesc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict (9 - current Speed) [Vibration] Potency (min. 3) and (9 - current Speed)/2 [Vibration] Count
   PL: — opis skrócony] Nakłada (9-bieżąca Szybkość) Moc [Vibration] i połowę tej wartości Licznika [Vibration]
479. [Dar E.G.O [2040] — opis skrócony] 받는 피해량 -10%.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2040].simpleDesc[abilityID=20401].simpleDesc
   limit: do 120 znaków
   EN: Damage Taken -10%.
   PL: — opis skrócony] Otrzymuje -10% obrażeń.
480. [Dar E.G.O [2041] — nazwa] 낙수의 잔
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2041].name
   limit: do 40 znaków
   EN: Chalice of Trickle-down
   PL: — nazwa] Kielich Kapnących Kropli
481. [Dar E.G.O [2041] — opis] [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬(E.G.O 스킬 제외)을 보유한 아군이 적과 합하여 승리 시, [Vibration] 위력 2, [Vibration] 횟수 2 부여 (턴 당 2회).\n\n유로지비 소속 인격일 경우 효과가 강화되어, [Vibration] 위력 3, [Vibration] 횟수 3 부여 (턴 당 3회)\n\n해당 인격이 자신보다 공격 레벨이 높은 적과 합 진행 시 합 위력 +2, 합하여 승리 시 가하는 피해량 +20%.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2041].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: When an ally with Attack Skills(Not E.G.O Skills) that inflict [Vibration] Potency, Count, or 'Unique Tremor' wins a Clash, inflict 2 [Vibration] Potency and +2 [Vibration] Count. (2 times per turn)\n\nYurodivy Identities: inflict 3 [Vibration] Potency and +3 [Vibration] Count instead (3 times per turn)\n\nIf the affected Identity Clashes against targets with higher Offense Levels, Clash Power +2; deal +20% damage when attacking after winning the Clash.
   PL: — opis] Gdy sojusznik z Umiejętnością ataku (poza Umiejętnościami E.G.O) nakładającą Moc [Vibration], Licznik [Vibration] lub 'Szczególny Wstrząs' wygrywa starcie z wrogiem, nakłada 2 Moc [Vibration] i +2 Licznika [Vibration] (2 razy na turę).\n\nTożsamości Yurodivy: efekt jest wzmocniony i nakładają 3 Moc [Vibration] i +3 Licznika [Vibration] (3 razy na turę).\n\nGdy ta Tożsamość prowadzi starcie z wrogiem o wyższym Poziomie Ataku, zyskuje Moc Starcia +2, a gdy atakuje po wygranej w starciu, zadaje +20% obrażeń.
482. [Dar E.G.O [2041] — opis skrócony] [Vibration] 위력 2, [Vibration] 횟수 2 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2041].simpleDesc[abilityID=2041].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 2 [Vibration] Potency and +2 [Vibration] Count
   PL: — opis skrócony] Nakłada 2 Moc [Vibration] i +2 Licznika [Vibration]
483. [Dar E.G.O [2041] — opis skrócony] [Vibration] 위력 3, [Vibration] 횟수 3 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2041].simpleDesc[abilityID=20411].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict 3 [Vibration] Potency and +3 [Vibration] Count
   PL: — opis skrócony] Nakłada 3 Moc [Vibration] i +3 Licznika [Vibration]
484. [Dar E.G.O [2041] — opis skrócony] 합 위력+2, 가하는 피해량 +20%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2041].simpleDesc[abilityID=20412].simpleDesc
   limit: do 120 znaków
   EN: Clash Power +2, deal +20% damage
   PL: — opis skrócony] Moc Starcia +2, zadaje +20% obrażeń
485. [Dar E.G.O [2042] — nazwa] 선불 시간 영수증
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2042].name
   limit: do 40 znaków
   EN: Prepaid Time Receipt
   PL: — nazwa] Rachunek za Przedpłacony Czas
486. [Dar E.G.O [2042] — opis] 자신보다 속도가 2 이상 높은 적에게 가하는 피해량 +(5 + 속도 차이x2.5)% (최대 15%).\n\n턴 종료 시 이번 턴 동안 자신보다 속도가 2 이상 높은 적에게 공격 스킬(E.G.O 스킬 제외)을 사용하여 한 번이라도 피해를 입혔다면, 다음 턴에 대상에게 [Binding] 2, [ResultReduction] 1을 부여 (턴 당 1회).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2042].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [Binding], [ResultReduction]
   znaczenie tagów: [Binding] = 속박 / Bind; [ResultReduction] = 위력 감소 / Power Down
   EN: Deal +(5 + (2.5 x Speed difference))% damage against faster enemies with 2+ Speed difference. (max 15%)\n\nTurn End: If an ally dealt damage with an Attack Skill (Not counting E.G.O Skills) this turn against faster enemies with 2+ Speed difference, inflict 2 [Binding] and 1 [ResultReduction] to the enemy next turn. (once per turn)
   PL: — opis] Zadaje +(5 + różnica Szybkości x 2.5)% obrażeń wrogom szybszym o co najmniej 2 Szybkości (maks. 15%).\n\nNa koniec tury, jeżeli w tej turze zadano wrogom szybszym o co najmniej 2 Szybkości obrażenia Umiejętnością ataku (poza Umiejętnościami E.G.O) chociaż raz, nakłada w następnej turze na wroga 2 [Binding] i 1 [ResultReduction] (1 raz na turę).
487. [Dar E.G.O [2042] — opis skrócony] 가하는 피해량 +(5 + 속도 차이x2.5)%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2042].simpleDesc[abilityID=2042].simpleDesc
   limit: do 120 znaków
   EN: Deal +(5 + (2.5 x Speed difference))% damage against
   PL: — opis skrócony] Zadaje +(5 + różnica Szybkości x 2.5)% obrażeń
488. [Dar E.G.O [2042] — opis skrócony] 다음 턴에 [Binding] 2, [ResultReduction] 1을 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2042].simpleDesc[abilityID=20421].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding], [ResultReduction]
   znaczenie tagów: [Binding] = 속박 / Bind; [ResultReduction] = 위력 감소 / Power Down
   EN: Inflict 2 [Binding] and 1 [ResultReduction] to the enemy next turn
   PL: — opis skrócony] Nakłada w następnej turze 2 [Binding] i 1 [ResultReduction] na wroga
489. [Dar E.G.O [2043] — nazwa] 회중시계 : 타입 L
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2043].name
   limit: do 40 znaków
   EN: Pocket Watch : Type L
   PL: — nazwa] Zegarek Kieszonkowy : Typ L
490. [Dar E.G.O [2043] — opis] 턴 시작 시, [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 사용하는 스킬 3의 코인 위력 +2, 피해량 +25%.\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 공격 스킬(E.G.O 스킬 포함)을 사용하여 적을 [Switch_Vibration]할 경우, 변환되는 [Vibration] 위력과 [Vibration] 횟수 값이 1.5배로 적용(다른 유형으로 변환되는 경우에만 적용)되고 다음 턴에 [DefenseDown] 5를 부여 (턴 당 1회).\n\n턴 시작 시, 속도가 제일 낮은 적 3명에게 (12-현재 속도)만큼 [Vibration] 위력 부여 (최소 6, 웨이브 당 최대 1회).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2043].desc
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [Switch_Vibration], [DefenseDown]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency, Count, or 'Unique Tremor'. (except E.G.O Skills; except Backup Units)\n\nTo allies' Skill 3s that inflict [Vibration] Potency, Count, or 'Unique Tremor': Coin Power +2 and deal +25% damage.\n\nWhen an ally that inflicts [Vibration] Potency, Count, or 'Unique Tremor' triggers [Switch_Vibration] on an enemy with Attack Skills(Including E.G.O Skills): multiply the [Vibration] Potency and Count by 1.5(only when actually Converting them into different 'Tremor' types) and inflict 5 [DefenseDown] next turn. (once per turn)\n\nTurn Start: inflict (12 - current Speed) [Vibration] Potency (min. 6) to 3 enemies with the slowest Speed. (once per wave)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nGdy sojusznik nakładający Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs [Switch_Vibration] wroga Umiejętnością ataku (wliczając Umiejętności E.G.O), przekształcana Moc [Vibration] i Liczniki [Vibration] są stosowane 1,5 razy większe (tylko przy przekształceniu w inny typ) i nakłada 5 [DefenseDown] na następną turę (1 raz na turę).\n\nNa początku tury 3 wrogów o najniższej Szybkości zyskuje Moc [Vibration] równą (12-obecna Szybkość) (min. 6; maks. 1 raz na falę).
491. [Dar E.G.O [2043] — opis skrócony] 스킬 3의 코인 위력 +2, 피해량 +25%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2043].simpleDesc[abilityID=2043].simpleDesc
   limit: do 120 znaków
   EN: Skill 3 gains Coin Power +2 and deals +25% damage
   PL: — opis skrócony] Umiejętność 3 zyskuje Moc Monet +2 i zadaje +25% obrażeń
492. [Dar E.G.O [2043] — opis skrócony] 변환되는 [Vibration] 위력과 [Vibration] 횟수 값이 1.5배로 적용
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2043].simpleDesc[abilityID=20431].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Multiply [Vibration] Potency and Count by 1.5 when triggering Amplitude Conversion
   PL: — opis skrócony] Przekształcana Moc [Vibration] i Licznik [Vibration] są mnożone x 1.5
493. [Dar E.G.O [2043] — opis skrócony] (12-현재 속도)만큼 [Vibration] 위력 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2043].simpleDesc[abilityID=20432].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict (12 - current Speed) [Vibration] Potency
   PL: — opis skrócony] Nakłada (12-bieżąca Szybkość) Moc [Vibration]
494. [Dar E.G.O [2044] — nazwa] 회중시계 : 타입 E
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2044].name
   limit: do 40 znaków
   EN: Pocket Watch : Type E
   PL: — nazwa] Zegarek Kieszonkowy : Typ E
495. [Dar E.G.O [2044] — opis] 턴 시작 시, [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 사용하는 스킬 3의 코인 위력 +2, 피해량 +25%.\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 자신보다 속도가 2 이상 느린 적에게 피해를 입힐 때 가하는 피해량 +(대상이 보유한 [Vibration] 위력, 최대 25)%, 피해를 입힐 때마다 [DefenseDown] 2 부여 (최대 6).\n\n턴 시작 시, 속도가 제일 높은 적 1명에게 (12-현재 속도)만큼 [Vibration] 위력(최소 6)과 그 수치의 절반만큼 [Vibration] 횟수를 부여(올림하여 처리, 환상체일 경우 부위 하나, 웨이브 당 최대 1회).
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2044].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [DefenseDown]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency, Count, or 'Unique Tremor' effects. (except E.G.O Skills; except Backup Units)\n\nTo allies' Skill 3s that inflict [Vibration] Potency, Count, or 'Unique Tremor': Coin Power +2 and deal +25% damage.\n\nWhen an ally that inflicts [Vibration] Potency, Count, or 'Unique Tremor' deals damage to a slower enemy with 2+ Speed difference between them: deal +([Vibration] Potency on target, max 25)% damage and inflict 2 [DefenseDown] every time the ally deals damage (max 6)\n\nTurn Start: inflict (12 - current Speed) [Vibration] Potency (min. 6) and (12 - current Speed)/2 [Vibration] Count to 1 enemy with the fastest Speed. (rounded up; for Abnormalities, a Part; once per wave)
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nGdy sojusznik nakładający Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zadaje obrażenia wrogowi o co najmniej 2 Szybkości wolniejszemu od niego, zadaje +(Moc [Vibration] celu, maks. 25)% obrażeń, a przy każdym zadaniu obrażeń nakłada 2 [DefenseDown] (maks. 6).\n\nNa początku tury nakłada 1 wrogowi z najwyższą Szybkością Moc [Vibration] równą (12-obecna Szybkość) (min. 6) i Liczniki [Vibration] równe połowie tej wartości (zaokrąglając w górę; w przypadku Anomalii — 1 Partię; maks. 1 raz na falę).
496. [Dar E.G.O [2044] — opis skrócony] 스킬 3의 코인 위력 +2, 피해량 +25%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2044].simpleDesc[abilityID=2044].simpleDesc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Dar E.G.O [2044] — opis skrócony] 가하는 피해량 +(대상이 보유한 [Vibration] 위력)%, 피해를 입힐 때마다 [DefenseDown] 2 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2044].simpleDesc[abilityID=20441].simpleDesc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vibration], [DefenseDown]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Deal +([Vibration] Potency on target)% damage; inflict 2 [DefenseDown] every time the ally deals damage
   PL: — opis skrócony] Zadaje +(Moc [Vibration] celu)% obrażeń i nakłada 2 [DefenseDown] za każdym razem, gdy zadaje obrażenia
498. [Dar E.G.O [2044] — opis skrócony] (12-현재 속도)만큼 [Vibration] 위력과 그 수치의 절반만큼 [Vibration] 횟수 부여
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2044].simpleDesc[abilityID=20442].simpleDesc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Inflict (12 - current Speed) [Vibration] Potency (min. 3) and (9 - current Speed)/2 [Vibration] Count
   PL: — opis skrócony] Nakłada (12-bieżąca Szybkość) Moc [Vibration] i połowę tej wartości Licznika [Vibration]
499. [Dar E.G.O [2045] — nazwa] 회중시계 : 타입 Y
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2045].name
   limit: do 40 znaków
   EN: Pocket Watch : Type Y
   PL: — nazwa] Zegarek Kieszonkowy : Typ Y
500. [Dar E.G.O [2045] — opis] 턴 시작 시, [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 사용하는 스킬 3의 코인 위력 +2, 피해량 +25%.\n\n유로지비 소속 인격일 경우 효과가 강화되어 스킬 3의 코인 위력 +2, 피해량 +(25 + 대상이 보유한 [Vibration] 위력과 [Vibration] 횟수의 합, 최대 100)%.\n\n유로지비 소속 인격이 턴 시작 시, 자신의 [Vibration] 횟수 3 증가.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2045].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency, Count, or 'Unique Tremor' effects. (except E.G.O Skills; except Backup Units)\n\nTo allies' Skill 3s that inflict [Vibration] Potency, Count, or 'Unique Tremor': Coin Power +2 and deal +25% damage.\n\nYurodivy Identities: Skill 3 gains Coin Power +2 and deal +(25 + (sum of [Vibration] Potency and Count on target))% damage. (max 100%)\n\nYurodivy Identities: gain +3 [Vibration] Count at Turn Start.
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nJeżeli Tożsamość należy do Jurodiwi, efekt jest wzmocniony: Umiejętność 3 zyskuje Moc Monet +2 i zadaje +(25 + suma Mocy [Vibration] i Liczników [Vibration] celu, maks. 100)% obrażeń.\n\nTożsamości Jurodiwi zwiększają na początku tury własne Liczniki [Vibration] o 3.
501. [Dar E.G.O [2045] — opis skrócony] 스킬 3의 코인 위력 +2, 피해량 +25%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2045].simpleDesc[abilityID=2045].simpleDesc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Dar E.G.O [2045] — opis skrócony] 스킬 3의 코인 위력 +2, 피해량 +(25 + 대상이 보유한 [Vibration] 위력과 [Vibration] 횟수의 합)%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2045].simpleDesc[abilityID=20451].simpleDesc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Skill 3 gains Coin Power +2 and deal +(25 + (sum of [Vibration] Potency and Count on target))% damage.
   PL: — opis skrócony] Umiejętność 3 zyskuje Moc Monet +2 i zadaje +(25 + suma Mocy [Vibration] i Licznika [Vibration] celu)% obrażeń
503. [Dar E.G.O [2045] — opis skrócony] [Vibration] 횟수 3 증가
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2045].simpleDesc[abilityID=20452].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Gain +3 [Vibration] Count
   PL: — opis skrócony] Zyskuje +3 Licznika [Vibration]
504. [Dar E.G.O [2046] — nazwa] 회중시계 : 타입 P
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2046].name
   limit: do 40 znaków
   EN: Pocket Watch : Type P
   PL: — nazwa] Zegarek Kieszonkowy : Typ P
505. [Dar E.G.O [2046] — opis] 턴 시작 시, [Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 공격 스킬을 보유한 인격이 5인 이상이면, 이번 전투 동안 발동 (E.G.O 스킬 제외. 대기 인원 제외)\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 사용하는 스킬 3의 코인 위력 +2, 피해량 +25%.\n\n[Vibration] 위력 또는 [Vibration] 횟수 또는 특수 진동을 부여하는 아군이 합을 진행할 때, 자신보다 속도가 2 이상 높은 적과 진행할 경우 합 위력 +2, 가하는 피해량 +(대상이 보유한 [Vibration] 위력, 최대 50)%.\n\n 턴 시작 시, 속도가 제일 느린 아군 셋이 속도가 느린 순으로 [AttackUp] 5, [AttackUp] 3, [AttackUp] 2를 얻음.
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2046].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [AttackUp]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: This Gift activates for the whole Encounter when 5 or more Identities have Attack Skills that apply [Vibration] Potency, Count, or 'Unique Tremor' effects. (except E.G.O Skills; except Backup Units)\n\nTo allies' Skill 3s that inflict [Vibration] Potency, Count, or 'Unique Tremor': Coin Power +2 and deal +25% damage.\n\nWhen an ally that inflicts [Vibration] Potency, Count, or 'Unique Tremor' Clashes against a faster enemy with 2+ Speed difference: Clash Power +2 and deal +([Vibration] Potency on target)% damage. (max 50%)\n\nTurn Start: from slowest to fastest, the 3 slowest allies gain 5 [AttackUp], 3 [AttackUp], and 2 [AttackUp] respectively.
   PL: — opis] Na początku tury, jeżeli co najmniej 5 Tożsamości ma Umiejętności ataku nakładające Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs, Dar ten uruchamia się na całą walkę (poza Umiejętnościami E.G.O; z pominięciem jednostek zapasowych)\n\nUmiejętności 3 sojuszników nakładających Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs zyskują Moc Monet +2 i zadają +25% obrażeń.\n\nGdy sojusznik nakładający Moc [Vibration], Liczniki [Vibration] lub Szczególny Wstrząs prowadzi Starcie z wrogiem o co najmniej 2 Szybkości szybszym od niego, zyskuje Moc Starcia +2 i zadaje +(Moc [Vibration] celu, maks. 50)% obrażeń.\n\nNa początku tury 3 najwolniejsi sojusznicy zyskują, w kolejności od najwolniejszego, 5 [AttackUp], 3 [AttackUp] i 2 [AttackUp].
506. [Dar E.G.O [2046] — opis skrócony] 스킬 3의 코인 위력 +2, 피해량 +25%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2046].simpleDesc[abilityID=2046].simpleDesc
   (powtórzenie elementu 491 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Dar E.G.O [2046] — opis skrócony] 합 위력 +2, 가하는 피해량 +(대상이 보유한 [Vibration] 위력)%
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2046].simpleDesc[abilityID=20461].simpleDesc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Clash Power +2 and deal +([Vibration] Potency on target)% damage
   PL: — opis skrócony] Zyskuje Moc Starcia +2 i zadaje +(Moc [Vibration] celu)% obrażeń
508. [Dar E.G.O [2046] — opis skrócony] [AttackUp] 얻음
   źródło: EGOgift_StoryDungeon-tkt.json :: dataList[id=2046].simpleDesc[abilityID=20462].simpleDesc
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Dar E.G.O: EGOgift_StoryDungeon
- plik gry: `EGOgift_StoryDungeon.json`

509. [Dar E.G.O [1001] — nazwa] 신도의 가면
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1001].name
   limit: do 40 znaków
   EN: Mask of a Devotee
   PL: — nazwa] Maska Wyznawcy
510. [Dar E.G.O [1001] — opis] 모든 아군의 방어 레벨 +5
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1001].desc
   limit: do 120 znaków
   EN: All allies gain +5 Defense Level.
   PL: — opis] Poziom Obrony wszystkich sojuszników +5.
511. [Dar E.G.O [1001] — opis skrócony] 방어 레벨 +5
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1001].simpleDesc[abilityID=1001].simpleDesc
   limit: do 120 znaków
   EN: Defense Level +5
   PL: — opis skrócony] Poziom Obrony +5
512. [Dar E.G.O [1002] — nazwa] 허름한 붕대
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1002].name
   limit: do 40 znaków
   EN: Shoddy Dressing
   PL: — nazwa] Lichy Opatrunek
513. [Dar E.G.O [1002] — opis] 모든 아군 최대 체력 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1002].desc
   limit: do 120 znaków
   EN: All allies gain +10% max HP.
   PL: — opis] Maks. HP wszystkich sojuszników +10%.
514. [Dar E.G.O [1002] — opis skrócony] 최대 체력 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1002].simpleDesc[abilityID=1002].simpleDesc
   limit: do 120 znaków
   EN: +10% max HP
   PL: Maks. HP +10%
515. [Dar E.G.O [1003] — nazwa] 짓물린 파편
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1003].name
   limit: do 40 znaków
   EN: Festered Fragment
   PL: — nazwa] Zagniły Odłamek
516. [Dar E.G.O [1003] — opis] 턴 시작 시 체력이 50% 미만인 아군의 체력 5 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1003].desc
   limit: do 120 znaków
   EN: At the start of the turn, allies with 50% or less health heal 5 HP.
   PL: — opis] Na początku tury sojusznicy z HP poniżej 50% odzyskują 5 HP
517. [Dar E.G.O [1003] — opis skrócony] 체력 50%미만 아군 체력 5 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1003].simpleDesc[abilityID=1003].simpleDesc
   limit: do 120 znaków
   EN: Allies at <50% health heal 5 HP
   PL: — opis skrócony] Sojusznicy z HP poniżej 50% odzyskują 5 HP
518. [Dar E.G.O [1004] — nazwa] 피 묻은 신도의 가면
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1004].name
   limit: do 40 znaków
   EN: Bloodied Mask of a Devotee
   PL: — nazwa] Krwawa Maska Wyznawcy
519. [Dar E.G.O [1004] — opis] 모든 아군의 공격 레벨 +5, 방어 레벨 +5
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1004].desc
   limit: do 120 znaków
   EN: All allies gain +5 Offense Level and +5 Defense Level
   PL: — opis] Poziom Ataku i Poziom Obrony wszystkich sojuszników +5
520. [Dar E.G.O [1004] — opis skrócony] 공격 레벨 +5, 방어 레벨 +5
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1004].simpleDesc[abilityID=1004].simpleDesc
   limit: do 120 znaków
   EN: Offense & Defense Levels +5
   PL: Poziom Ataku +5, Poziom Obrony +5
521. [Dar E.G.O [1005] — nazwa] 흑단 브로치
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1005].name
   limit: do 40 znaków
   EN: Ebony Brooch
   PL: — nazwa] Hebanowa Broszka
522. [Dar E.G.O [1005] — opis] 매 전투에서 3턴동안 모든 적에게 속박 2 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1005].desc
   limit: do 120 znaków
   EN: For the first 3 turns of battle, inflict 2 Bind on all enemies.
   PL: — opis] W każdej walce przez pierwsze 3 tury nakłada 2 Spętania na wszystkich wrogów.
523. [Dar E.G.O [1005] — opis skrócony] 속박 2 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1005].simpleDesc[abilityID=1005].simpleDesc
   limit: do 120 znaków
   EN: Inflict 2 Bind
   PL: — opis skrócony] Nakłada 2 Spętania
524. [Dar E.G.O [1006] — nazwa] 종말의 부조
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1006].name
   limit: do 40 znaków
   EN: Etched Doomsday
   PL: — nazwa] Rzeźba Zagłady
525. [Dar E.G.O [1006] — opis] 매 전투의 첫 턴마다 모든 적에게 화상 1(5회 발동) 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1006].desc
   limit: do 120 znaków
   EN: On the first turn of battle, inflict 1 Burn on all enemies 5 times.
   PL: — opis] W pierwszej turze każdej walki nakłada 1 Podpalenie na wszystkich wrogach (5 wywołań)
526. [Dar E.G.O [1006] — opis skrócony] 화상 1 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1006].simpleDesc[abilityID=1006].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 Burn
   PL: — opis skrócony] Nakłada 1 Podpalenie
527. [Dar E.G.O [1011] — nazwa] 장난감 주먹
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1011].name
   limit: do 40 znaków
   EN: Toy Fist
   PL: — nazwa] Zabawkowa Pięść
528. [Dar E.G.O [1011] — opis] 모든 아군의 가하는 피해량 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1011].desc
   limit: do 120 znaków
   EN: All allies deal +10% damage.
   PL: — opis] Wszyscy sojusznicy zadają +10% obrażeń.
529. [Dar E.G.O [1011] — opis skrócony] 가하는 피해량 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1011].simpleDesc[abilityID=1011].simpleDesc
   limit: do 120 znaków
   EN: Damage +10%
   PL: — opis skrócony] Zadaje +10% obrażeń
530. [Dar E.G.O [1012] — nazwa] 장난감 발
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1012].name
   limit: do 40 znaków
   EN: Toy Foot
   PL: — nazwa] Zabawkowa Stopa
531. [Dar E.G.O [1012] — opis] 모든 아군의 속도 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1012].desc
   limit: do 120 znaków
   EN: All allies gain +1 Speed.
   PL: — opis] Szybkość wszystkich sojuszników +1.
532. [Dar E.G.O [1012] — opis skrócony] 속도 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1012].simpleDesc[abilityID=1012].simpleDesc
   limit: do 120 znaków
   EN: SPD +1
   PL: Szybkość +1
533. [Dar E.G.O [1013] — nazwa] 장난감 나사
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1013].name
   limit: do 40 znaków
   EN: Toy Screw
   PL: — nazwa] Zabawkowa Śruba
534. [Dar E.G.O [1013] — opis] 모든 아군의 최대 체력 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1013].desc
   limit: do 120 znaków
   EN: All allies gain +10% max HP
   PL: — opis] Maks. HP wszystkich sojuszników +10%
535. [Dar E.G.O [1013] — nazwa Anomalii] 강화 인간
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1013].abnormalityName
   limit: do 40 znaków
   EN: Cyborg
   PL: — nazwa Anomalii] Cyborg
536. [Dar E.G.O [1013] — opis skrócony] 최대 체력 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1013].simpleDesc[abilityID=1013].simpleDesc
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Dar E.G.O [1014] — nazwa] 무지개 태엽
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1014].name
   limit: do 40 znaków
   EN: Rainbow Mainspring
   PL: — nazwa] Tęczowa Sprężyna
538. [Dar E.G.O [1014] — opis] 매 턴 시작 시 현재 체력이 가장 낮은 아군 1명이 보호 2를 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1014].desc
   limit: do 120 znaków
   EN: At the start of the turn, apply 2 Protection to the ally with the least HP.
   PL: — opis] Na początku każdej tury 1 sojusznik o najniższym aktualnym HP zyskuje 2 Ochrony
539. [Dar E.G.O [1014] — opis skrócony] 보호 2 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1014].simpleDesc[abilityID=1014].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 Protection
   PL: — opis skrócony] Zyskuje 2 Ochrony
540. [Dar E.G.O [1015] — nazwa] 녹슨 태엽
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1015].name
   limit: do 40 znaków
   EN: Rusty Mainspring
   PL: — nazwa] Zardzewiała Sprężyna
541. [Dar E.G.O [1015] — opis] 매 턴 시작 시 현재 체력이 가장 낮은 아군 1명이 보호 1을 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1015].desc
   limit: do 120 znaków
   EN: At the start of the turn, apply 1 Protection to the ally with the least HP.
   PL: — opis] Na początku każdej tury 1 sojusznik o najniższym aktualnym HP zyskuje 1 Ochrony
542. [Dar E.G.O [1015] — opis skrócony] 보호 1 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1015].simpleDesc[abilityID=1015].simpleDesc
   limit: do 120 znaków
   EN: Gain 1 Protection
   PL: — opis skrócony] Zyskuje 1 Ochrony
543. [Dar E.G.O [1016] — nazwa] 긴급 시술 장치
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1016].name
   limit: do 40 znaków
   EN: Emergency Surgical Kit
   PL: — nazwa] Awaryjny Zestaw Zabiegowy
544. [Dar E.G.O [1016] — opis] 전투에서 체력이 0이 되는 피해를 입을 때, 체력이 1 미만으로 감소하지 않음\n다음 턴에 체력을 최대로 회복하고, 시술 3을 얻음\n전투 종료 시 체력이 남아있어도 사망함.(던전 내 1회 발동 후 소멸)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1016].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During battle, if an ally takes lethal damage, their HP won’t go below 1.\nOn the next turn, fully heal their HP and gain 3 Surgery.\nThey will die at the end of the battle.\n(Activates once per dungeon, then the Gift expires.)
   PL: — opis] Gdy w walce sojusznik otrzyma obrażenia redukujące HP do 0, HP nie maleje poniżej 1\nNa następną turę odzyskuje HP do maksimum i zyskuje 3 Zabiegów\nNa koniec walki ginie, nawet jeżeli ma pozostałe HP. (wywoływane raz w lochu, po czym Dar znika)
545. [Dar E.G.O [1016] — opis skrócony] 체력 전부 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1016].simpleDesc[abilityID=1016].simpleDesc
   limit: do 120 znaków
   EN: Fully heal HP
   PL: — opis skrócony] Odzyskuje pełne HP
546. [Dar E.G.O [1016] — opis skrócony] 시술 3 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1016].simpleDesc[abilityID=10161].simpleDesc
   limit: do 120 znaków
   EN: Gain 3 Surgery
   PL: — opis skrócony] Zyskuje 3 Zabiegów
547. [Dar E.G.O [1018] — nazwa] 꿈틀거리는 리본
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1018].name
   limit: do 40 znaków
   EN: Writhing Ribbon
   PL: — nazwa] Wierzgająca Wstążka
548. [Dar E.G.O [1018] — opis] 색욕 속성 스킬로 합 승리 시 다음 턴에 속박, 취약 1 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1018].desc
   limit: do 120 znaków
   EN: After winning a Clash using a Lust skill, inflict 1 Bind and 1 Fragile next turn.
   PL: — opis] Przy wygranej Starciu Umiejętnością Grzechu Żądzy, nakłada 1 Spętania i 1 Wrażliwości na następną turę.
549. [Dar E.G.O [1018] — opis skrócony] 속박 1 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1018].simpleDesc[abilityID=1018].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 Bind
   PL: — opis skrócony] Nakłada 1 Spętania
550. [Dar E.G.O [1018] — opis skrócony] 취약 1 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1018].simpleDesc[abilityID=10181].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 Fragile
   PL: — opis skrócony] Nakłada 1 Wrażliwości
551. [Dar E.G.O [1021] — nazwa] 어느 표지
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1021].name
   limit: do 40 znaków
   EN: A Sign
   PL: Pewien Znak
552. [Dar E.G.O [1021] — opis] 크로머에 맞서고자 하는 싱클레어의 마음. 획이 3번 그어지면...
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1021].desc
   limit: do 120 znaków
   EN: Sinclair’s determination to stand up to Kromer. After three strokes have been drawn…
   PL: Zdeterminowanie Sinclaira, by stawić czoła Kromer. Gdy trzy kreski zostaną naniesione...
553. [Dar E.G.O [1021] — opis skrócony] 싱클레어의 마음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1021].simpleDesc[abilityID=1021].simpleDesc
   limit: do 120 znaków
   EN: Sinclair’s Will
   PL: Wola Sinclaira
554. [Dar E.G.O [1022] — nazwa] 어느 표지
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1022].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Dar E.G.O [1022] — opis] 크로머에 맞서고자 하는 싱클레어의 마음. 획이 3번 그어지면...
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1022].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Dar E.G.O [1022] — opis skrócony] 싱클레어의 마음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1022].simpleDesc[abilityID=1022].simpleDesc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [Dar E.G.O [1023] — nazwa] 어느 표지
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1023].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Dar E.G.O [1023] — opis] 크로머에 맞서고자 하는 싱클레어의 마음. 획이 3번 그어지면...
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1023].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Dar E.G.O [1023] — opis skrócony] 싱클레어의 마음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1023].simpleDesc[abilityID=1023].simpleDesc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Dar E.G.O [1024] — nazwa] 어느 표지
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1024].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Dar E.G.O [1024] — opis] 크로머에 맞서고자 하는 싱클레어의 마음. 획이 3번 그어지면...
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1024].desc
   (powtórzenie elementu 552 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Dar E.G.O [1024] — opis skrócony] 싱클레어의 마음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1024].simpleDesc[abilityID=1024].simpleDesc
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Dar E.G.O [1032] — nazwa] 횃불 더미
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1032].name
   limit: do 40 znaków
   EN: Torch Stack
   PL: — nazwa] Stos Pochodni
564. [Dar E.G.O [1032] — opis] 다음 3번의 전투 동안 신속 3을 얻은 상태로 전투 시작.\n전투 3회 종료 후 소멸
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1032].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Start the next 3 battles with 3 Haste.\nExpires afterward.
   PL: — opis] Zaczyna następne 3 walki z 3 Pośpiechu.\nZnika po 3 ukończonych walkach
565. [Dar E.G.O [1032] — opis skrócony] 신속 3 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1032].simpleDesc[abilityID=1032].simpleDesc
   limit: do 120 znaków
   EN: Gain 3 Haste
   PL: — opis skrócony] Zyskuje 3 Pośpiechu
566. [Dar E.G.O [1033] — nazwa] 옛 창고의 열쇠
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1033].name
   limit: do 40 znaków
   EN: Old Warehouse’s Key
   PL: — nazwa] Klucz do Starego Magazynu
567. [Dar E.G.O [1033] — opis] 특정 선택지에서 사용 가능. 사용 시 소멸.
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1033].desc
   limit: do 120 znaków
   EN: Used in certain events. Expires on use.
   PL: — opis] Można użyć w określonych wydarzeniach. Znika po użyciu.
568. [Dar E.G.O [1033] — opis skrócony] 선택지에 사용
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1033].simpleDesc[abilityID=1033].simpleDesc
   limit: do 120 znaków
   EN: Used in events
   PL: — opis skrócony] Używa w wydarzeniach
569. [Dar E.G.O [1034] — nazwa] 핏빛 갈기
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1034].name
   limit: do 40 znaków
   EN: Blood-red Mane
   PL: — nazwa] Krwistoczerwona Grzywa
570. [Dar E.G.O [1034] — opis] 색욕 속성 스킬을 가진 수감자에게만 적용\n이번 턴에 공격으로 피해를 받지 않았으면, 다음 턴에 신속 2, 수비 위력 증가 2를 얻음\n이번 턴에 공격으로 피해를 받았으면, 다음 턴에 속박 2, 공격 위력 증가 2를 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1034].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Allies with Lust skills gain the following effects:\nIf the unit took no damage from attacks this turn, gain 2 Haste and 2 Defense Power Up next turn.\nIf the unit took damage from attacks this turn, gain 2 Bind and 2 Attack Power Up next turn.
   PL: — opis] Stosowane tylko u Grzeszników z Umiejętnościami Żądzy\nJeżeli jednostka nie otrzymała w tej turze obrażeń od ataków, zyskuje 2 Pośpiechu i 2 Wzrostu Mocy Obrony na następną turę\nJeżeli jednostka otrzymała w tej turze obrażenia od ataków, zyskuje 2 Spętania i 2 Wzrostu Mocy Ataku na następną turę
571. [Dar E.G.O [1034] — opis skrócony] 신속 2, 수비 위력 증가 2 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1034].simpleDesc[abilityID=1034].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 Haste and Defense Power Up
   PL: — opis skrócony] Zyskuje 2 Pośpiechu i 2 Wzrostu Mocy Obrony
572. [Dar E.G.O [1034] — opis skrócony] 속박 2, 공격 위력 증가 2 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1034].simpleDesc[abilityID=10341].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 Bind and Attack Power Up
   PL: — opis skrócony] Zyskuje 2 Spętania i 2 Wzrostu Mocy Ataku
573. [Dar E.G.O [1037] — nazwa] N사의 인장
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1037].name
   limit: do 40 znaków
   EN: N Corp. Seal
   PL: — nazwa] Pieczęć Korporacji N
574. [Dar E.G.O [1037] — opis] 특정 선택지에서 사용 가능. 사용 시 소멸
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1037].desc
   limit: do 120 znaków
   EN: Used in certain events. Expires on use
   PL: — opis] Można użyć w określonych wydarzeniach. Znika po użyciu
575. [Dar E.G.O [1037] — opis skrócony] 선택지에 사용
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1037].simpleDesc[abilityID=1037].simpleDesc
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Dar E.G.O [1038] — nazwa] 순수함의 증표
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1038].name
   limit: do 40 znaków
   EN: Token of Innocence
   PL: — nazwa] Znak Niewinności
577. [Dar E.G.O [1038] — opis] 해당 의식을 진행한 인격의 분노 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1038].desc
   limit: do 120 znaków
   EN: For the Identity that undertook the rite: Boost the Power of Wrath skills by 2.
   PL: — opis] Moc Umiejętności Grzechu Gniewu Tożsamości, która wykonała rytuał, +2
578. [Dar E.G.O [1038] — opis skrócony] 분노 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1038].simpleDesc[abilityID=1038].simpleDesc
   limit: do 120 znaków
   EN: Wrath Skill Power +2
   PL: — opis skrócony] Moc Umiejętności Grzechu Gniewu +2
579. [Dar E.G.O [1039] — nazwa] 눈물의 증표
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1039].name
   limit: do 40 znaków
   EN: Token of Tears
   PL: — nazwa] Znak Łez
580. [Dar E.G.O [1039] — opis] 해당 의식을 진행한 인격의 우울 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1039].desc
   limit: do 120 znaków
   EN: For the Identity that undertook the rite: Boost the Power of Gloom skills by 2.
   PL: — opis] Moc Umiejętności Grzechu Posępności Tożsamości, która wykonała rytuał, +2
581. [Dar E.G.O [1039] — opis skrócony] 우울 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1039].simpleDesc[abilityID=1039].simpleDesc
   limit: do 120 znaków
   EN: Gloom Skill Power +2
   PL: — opis skrócony] Moc Umiejętności Grzechu Posępności +2
582. [Dar E.G.O [1040] — nazwa] 빛나는 두개골
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1040].name
   limit: do 40 znaków
   EN: Sparkling Skull
   PL: — nazwa] Lśniąca Czaszka
583. [Dar E.G.O [1040] — opis] 이전 턴에 피해를 10 이상 받았으면, 턴 시작 시 체력 5-15 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1040].desc
   limit: do 120 znaków
   EN: At the start of the turn, if the character took 10+ damage last turn, heal 5-15 HP.
   PL: — opis] Na początku tury, jeżeli Postać otrzymała w poprzedniej turze co najmniej 10 obrażeń, odzyskuje 5-15 HP
584. [Dar E.G.O [1040] — opis skrócony] 체력 5 - 15 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1040].simpleDesc[abilityID=1040].simpleDesc
   limit: do 120 znaków
   EN: Heal 5-15 HP
   PL: — opis skrócony] Odzyskuje 5-15 HP
585. [Dar E.G.O [1041] — nazwa] 피 흘리는 손
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1041].name
   limit: do 40 znaków
   EN: Hemorrhagic Hand
   PL: — nazwa] Krwawiąca Dłoń
586. [Dar E.G.O [1041] — opis] 턴 시작 시 체력이 25% 미만이 공격 위력 증가 2 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1041].desc
   limit: do 120 znaków
   EN: At the start of the turn, apply 2 Attack Power Up to allies at 25% or lower health.
   PL: — opis] Na początku tury Postacie z HP poniżej 25% zyskują 2 Wzrostu Mocy Ataku
587. [Dar E.G.O [1041] — opis skrócony] 공격 위력 증가 2 얻음
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1041].simpleDesc[abilityID=1041].simpleDesc
   limit: do 120 znaków
   EN: Gain 2 Attack Power Up
   PL: Zyskuje 2 Wzrosty Mocy Ataku
588. [Dar E.G.O [1042] — nazwa] 조롱하는 혓바닥
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1042].name
   limit: do 40 znaków
   EN: Sniggering Tongue
   PL: — nazwa] Kpiący Język
589. [Dar E.G.O [1042] — opis] 합 승리 시 가하는 피해량 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1042].desc
   limit: do 120 znaków
   EN: Deal +10% damage in a won clash.
   PL: — opis] Zadaje +10% obrażeń przy wygranej Starciu.
590. [Dar E.G.O [1042] — opis skrócony] 가하는 피해량 +10%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1042].simpleDesc[abilityID=1042].simpleDesc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Dar E.G.O [1043] — nazwa] 속죄의 증표
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1043].name
   limit: do 40 znaków
   EN: Token of Atonement
   PL: — nazwa] Znak Zadośćuczynienia
592. [Dar E.G.O [1043] — opis] 해당 의식을 진행한 인격의 색욕 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1043].desc
   limit: do 120 znaków
   EN: For the Identity that undertook the rite: Boost the Power of Lust skills by 2.
   PL: — opis] Moc Umiejętności Grzechu Żądzy Tożsamości, która wykonała rytuał, +2
593. [Dar E.G.O [1043] — opis skrócony] 색욕 속성 스킬 위력 +2
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1043].simpleDesc[abilityID=1043].simpleDesc
   limit: do 120 znaków
   EN: Lust Skill Power +2
   PL: — opis skrócony] Moc Umiejętności Grzechu Żądzy +2
594. [Dar E.G.O [1044] — nazwa] 의식의 자격
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1044].name
   limit: do 40 znaków
   EN: Ritualist’s Right
   PL: — nazwa] Uprawnienie Rytualisty
595. [Dar E.G.O [1044] — opis] 모든 아군이 색욕 속성으로 받는 피해량 20% 감소
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1044].desc
   limit: do 120 znaków
   EN: All allies take -20% damage from Lust attacks.
   PL: — opis] Wszyscy sojusznicy otrzymują -20% obrażeń od ataków Grzechu Żądzy.
596. [Dar E.G.O [1044] — opis skrócony] 받는 피해량 -20%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1044].simpleDesc[abilityID=1044].simpleDesc
   limit: do 120 znaków
   EN: Damage Taken -20%
   PL: — opis skrócony] Otrzymywane obrażenia -20%
597. [Dar E.G.O [1046] — nazwa] 초록빛 허물
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1046].name
   limit: do 40 znaków
   EN: Green Skin
   PL: — nazwa] Zielony Zrzut
598. [Dar E.G.O [1046] — opis] 피격 시 아군 1명의 체력이 1 미만이 될 때, 해당 캐릭터가 체력을 최대 체력의 50%만큼 회복함\n(던전 내 1회 발동 후 소멸)
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1046].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If an ally takes a lethal attack, they heal 50% of their max HP.\n(Once per dungeon and expires after activation.)
   PL: — opis] Gdy HP 1 sojusznika spadnie poniżej 1, ta Postać odzyskuje HP równe 50% Maks. HP\n(wywoływane raz w lochu, po czym znika)
599. [Dar E.G.O [1046] — opis skrócony] 최대 체력의 50%만큼 회복
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1046].simpleDesc[abilityID=1046].simpleDesc
   limit: do 120 znaków
   EN: Heal 50% of max HP
   PL: — opis skrócony] Odzyskuje 50% Maks. HP
600. [Dar E.G.O [1048] — nazwa] 투구
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1048].name
   limit: do 40 znaków
   EN: Topfhelm
   PL: — nazwa] Topfhelm
601. [Dar E.G.O [1048] — opis] 수비 스킬의 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1048].desc
   limit: do 120 znaków
   EN: Defense Skill Power +1
   PL: — opis] Moc Umiejętności obronnych +1
602. [Dar E.G.O [1048] — opis skrócony] 수비 스킬 위력 +1
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1048].simpleDesc[abilityID=1048].simpleDesc
   limit: do 120 znaków
   EN: Defense Skill Power +1
   PL: — opis skrócony] Moc Umiejętności obronnych +1
603. [Dar E.G.O [1049] — nazwa] 망치
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1049].name
   limit: do 40 znaków
   EN: Hammer
   PL: Młotek
604. [Dar E.G.O [1049] — opis] 스킬로 진동 부여 시 50% 확률로 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1049].desc
   limit: do 120 znaków
   EN: When inflicting Tremor with skill effects, inflict 1 more at a 50% chance.
   PL: — opis] Przy nakładaniu Wstrząsu Umiejętnością, 50% szans na nałożenie 1 dodatkowego.
605. [Dar E.G.O [1049] — opis skrócony] 진동 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1049].simpleDesc[abilityID=1049].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 additional Tremor
   PL: — opis skrócony] Nakłada 1 dodatkowy Wstrząs
606. [Dar E.G.O [1050] — nazwa] 못
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1050].name
   limit: do 40 znaków
   EN: Nagel
   PL: Gwóźdź
607. [Dar E.G.O [1050] — opis] 스킬로 출혈 부여 시 50% 확률로 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1050].desc
   limit: do 120 znaków
   EN: When inflicting Bleed with skill effects, inflict 1 more at a 50% chance.
   PL: — opis] Przy nakładaniu Krwawienia Umiejętnością, 50% szans na nałożenie 1 dodatkowego.
608. [Dar E.G.O [1050] — opis skrócony] 출혈 1 추가 부여
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1050].simpleDesc[abilityID=1050].simpleDesc
   limit: do 120 znaków
   EN: Inflict 1 additional Bleed
   PL: — opis skrócony] Nakłada 1 dodatkowe Krwawienie
609. [Dar E.G.O [1051] — nazwa] 못과 망치의 책
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1051].name
   limit: do 40 znaków
   EN: Nagel und Hammer Scriptures
   PL: — nazwa] Pisma Gwóźdź i Młot
610. [Dar E.G.O [1051] — opis] 오만 속성 스킬 사용 시 정신력 -5, 오만 속성 스킬의 가하는 피해량 +5%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1051].desc
   limit: do 120 znaków
   EN: When using a Pride skill, lose 5 SP, but boost its damage by 5%
   PL: — opis] Przy użyciu Umiejętności Grzechu Pychy, traci 5 Poczytalności, a te Umiejętności zadają +5% obrażeń
611. [Dar E.G.O [1051] — opis skrócony] 조건 충족한 정신력 -5
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1051].simpleDesc[abilityID=1051].simpleDesc
   limit: do 120 znaków
   EN: Pride skills cost 5 SP
   PL: — opis skrócony] Umiejętności Pychy kosztują 5 Poczytalności
612. [Dar E.G.O [1051] — opis skrócony] 조건 충족한 가하는 피해량 +5%
   źródło: EGOgift_StoryDungeon.json :: dataList[id=1051].simpleDesc[abilityID=10511].simpleDesc
   limit: do 120 znaków
   EN: Pride skill damage +5%
   PL: — opis skrócony] Umiejętności Pychy zadają +5% obrażeń
