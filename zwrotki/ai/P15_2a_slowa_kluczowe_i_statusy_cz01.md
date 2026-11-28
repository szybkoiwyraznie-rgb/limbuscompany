# Paczka AI P15 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 1/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P15_2a_slowa_kluczowe_i_statusy_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P15_2a_slowa_kluczowe_i_statusy_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords-BossRaid
- plik gry: `BattleKeywords-BossRaid.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [FavorBuffTwth1stPhaseForUI] — nazwa] 사영 [루주]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth1stPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwth1stPhaseForUI]`
   limit: do 40 znaków
   EN: Shade of Reflection [Rouge]
   PL: Cień Projekcji [Rouge]
2. [Słowo kluczowe [FavorBuffTwth1stPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>색욕</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적이 <color=#f8c200>출혈</color>로 받는 피해량이 1.5배로 증가 (소수점 버림)\n- <color=#f8c200>완전 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth1stPhaseForUI].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Lust Skills</color> or <color=#f8c200>Skills that inflict Bleed or 'Unique Bleed'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Enemies take x1.5 damage from <color=#f8c200>Bleed</color> (rounded down)\n- Upon <color=#f8c200>A-Reson.</color>, gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for A-Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Krwawienie lub „Specjalne Krwawienie”</color> albo należą do Grzechu <color=#f8c200>Żądzy</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Wrogowie otrzymują 1,5x obrażeń od <color=#f8c200>Krwawienia</color> (zaokrąglane w dół)\n- Przy <color=#f8c200>Rezonansie Absolutnym</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
3. [Słowo kluczowe [FavorBuffTwth2ndPhaseForUI] — nazwa] 사영 [블뢰]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth2ndPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwth2ndPhaseForUI]`
   limit: do 40 znaków
   EN: Shade of Reflection [Bleu]
   PL: Cień Projekcji [Bleu]
4. [Słowo kluczowe [FavorBuffTwth2ndPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>침잠 또는 특수 침잠</color>을 부여하거나 <color=#f8c200>우울</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 턴 시작 시, <color=#f8c200>패닉 상태</color>인 적이 취약 3 얻음\n- <color=#f8c200>손가락 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -15%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth2ndPhaseForUI].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gloom Skills</color> or <color=#f8c200>Skills that inflict Sinking or 'Unique Sinking'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Turn Start: Enemies in <color=#f8c200>Panic</color> gain 3 Fragile\n- <color=#f8c200>The Finger-faction Identities</color> deal +15% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Zatonięcie lub „Specjalne Zatonięcie”</color> albo należą do Grzechu <color=#f8c200>Posępności</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Na początku tury wrogowie w stanie <color=#f8c200>Paniki</color> otrzymują 3 Wrażliwości\n- Tożsamości <color=#f8c200>frakcji Palca</color> zadają wrogom obrażenia +15%, a otrzymują -15%
5. [Słowo kluczowe [FavorBuffTwthHardForUI] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHardForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthHardForUI]`
   limit: do 40 znaków
   EN: Tribulation
   PL: Utrapienie
6. [Słowo kluczowe [FavorBuffTwthHardForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 부여하는 <color=#ff0000>출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰]</color> 부여량 +1\n- 대상에게 <color=#ff0000>강렬한 색채</color>가 있으면, 합 위력 +2, 기본 위력 +1\n- [2페이즈 전용] ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’를 사용하는 턴 시작 시, <color=#ff0000>강렬한 색채</color>를 보유한 수감자 1명당 <color=#ff0000>정신력 10 회복</color> (최대 30)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHardForUI].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills inflict +1 more <color=#ff0000>Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]</color>\n- If target has <color=#ff0000>Palette Vibrante</color>, Clash Power +2 and Base Power +1\n- [Phase 2 exclusive effect] Turn Start: If this unit will use "Burst Forth the Pulsing Crimson under Your Skin" this turn, <color=#ff0000>heal 10 SP on self</color> for every Sinner that has <color=#ff0000>Palette Vibrante</color> (max 30 SP)
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności nakładają o 1 więcej <color=#ff0000>Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]</color>\n- Jeżeli cel posiada <color=#ff0000>Palette Vibrante</color>, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury, w której ta jednostka użyje „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za każdego Grzesznika z <color=#ff0000>Palette Vibrante</color> <color=#ff0000>odzyskuje 10 Poczytalności</color> (maks. 30)
7. [Słowo kluczowe [FavorBuffTwth] — nazwa] 사영 [루주]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwth]`
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
8. [Słowo kluczowe [FavorBuffTwth] — opis] - 출혈 또는 특수 출혈을 부여하거나 색욕 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 완전 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Attack Skills that are Lust Skills or Skills that inflict Bleed or 'Unique Bleed' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Upon A-Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for A-Reson. (2 times per turn)
   PL: - Umiejętności ataku, które nakładają Krwawienie lub „Specjalne Krwawienie” albo należą do Grzechu Żądzy, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy Rezonansie Absolutnym zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
9. [Słowo kluczowe [FavorBuffTwth] — podsumowanie] 출혈, 특수 출혈, 색욕 속성 스킬 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwth].summary
   limit: do 120 znaków
   EN: Bleed Skills, 'Unique Bleed' Skills, and Lust Skills deal more damage
   PL: Umiejętności Krwawienia, „Specjalnego Krwawienia” i Grzechu Żądzy zadają więcej obrażeń
10. [Słowo kluczowe [FavorBuffTwthEnemy] — nazwa] 사영 [루주]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthEnemy]`
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Słowo kluczowe [FavorBuffTwthEnemy] — opis] - 출혈로 받는 피해량이 1.5배로 증가 (소수점 버림)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].desc
   limit: do 120 znaków
   EN: - Take x1.5 damage from Bleed (rounded down)
   PL: - Otrzymujesz 1,5x obrażeń od Krwawienia (zaokrąglane w dół)
12. [Słowo kluczowe [FavorBuffTwthEnemy] — podsumowanie] 출혈로 받는 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].summary
   limit: do 120 znaków
   EN: Take more damage from Bleed
   PL: Otrzymujesz więcej obrażeń od Krwawienia
13. [Słowo kluczowe [FavorBuffTwthTwo] — nazwa] 사영 [블뢰]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthTwo]`
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Słowo kluczowe [FavorBuffTwthTwo] — opis] - 침잠 또는 특수 침잠을 부여하거나 우울 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 손가락 소속 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -15%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthTwo].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Attack Skills that are Gloom Skills or Skills that inflict Sinking or 'Unique Sinking' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- The Finger-faction Identities deal +15% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku, które nakładają Zatonięcie lub „Specjalne Zatonięcie” albo należą do Grzechu Posępności, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Tożsamości frakcji Palca zadają wrogom obrażenia +15%, a otrzymują -15%
15. [Słowo kluczowe [FavorBuffTwthTwo] — podsumowanie] 침잠, 특수 침잠, 우울 속성 스킬 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthTwo].summary
   limit: do 120 znaków
   EN: Sinking Skills, 'Unique Sinking' Skills, and Gloom Skills deal more damage
   PL: Umiejętności Zatonięcia, „Specjalnego Zatonięcia” i Grzechu Posępności zadają więcej obrażeń
16. [Słowo kluczowe [FavorBuffTwthEnemyTwo] — nazwa] 사영 [블뢰]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthEnemyTwo]`
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Słowo kluczowe [FavorBuffTwthEnemyTwo] — opis] - 턴 시작 시, 패닉 상태면 취약 3 얻음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].desc
   limit: do 120 znaków
   EN: - Turn Start: When Panicked, gain 3 Fragile
   PL: - Na początku tury, jeżeli jednostka jest w stanie Paniki, otrzymuje 3 Wrażliwości
18. [Słowo kluczowe [FavorBuffTwthEnemyTwo] — podsumowanie] 패닉 상태면 취약 얻음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].summary
   limit: do 120 znaków
   EN: When Panicked, gain Fragile
   PL: W stanie Paniki jednostka otrzymuje Wrażliwość
19. [Słowo kluczowe [FavorBuffTwthHard] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHard].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthHard]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Słowo kluczowe [FavorBuffTwthHard] — opis] - 최대 체력 +25%\n- 스킬로 부여하는 출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰] 부여량 +1\n- 대상에게 강렬한 색채가 있으면, 합 위력 +2, 기본 위력 +1
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHard].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- Skills inflict +1 more Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]\n- If target has Palette Vibrante, Clash Power +2 and Base Power +1
   PL: - Maks. HP +25%\n- Umiejętności nakładają o 1 więcej Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]\n- Jeżeli cel posiada Palette Vibrante, Moc Starcia +2 i Moc Bazowa +1
21. [Słowo kluczowe [FavorBuffTwthHard] — podsumowanie] 출혈 위력, 침잠 위력, 찢긴 색채 부여량 증가\n대상에게 강렬한 색채가 있으면 합 위력, 기본 위력이 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHard].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict more Bleed Potency, Sinking Potency, and Mauled Color\nIf target has Palette Vibrante, gain Clash Power and Base Power
   PL: Umiejętności nakładają więcej Siły Krwawienia, Siły Zatonięcia i Rozdartych Barw\nJeżeli cel posiada Palette Vibrante, Moc Starcia i Moc Bazowa rosną
22. [Słowo kluczowe [FavorBuffTwthHardTwo] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffTwthHardTwo]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
23. [Słowo kluczowe [FavorBuffTwthHardTwo] — opis] - 최대 체력 +25%\n- 스킬로 부여하는 출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰] 부여량 +1\n- 대상에게 강렬한 색채가 있으면, 합 위력 +2, 기본 위력 +1\n- [2페이즈 전용] ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’를 사용하는 턴 시작 시, 강렬한 색채를 보유한 수감자 1명당 정신력 10 회복 (최대 30)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- Skills inflict +1 more Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]\n- If target has Palette Vibrante, Clash Power +2 and Base Power +1\n- [Phase 2 exclusive effect] Turn Start: If this unit will use "Burst Forth the Pulsing Crimson under Your Skin" this turn, heal 10 SP on self for every Sinner that has Palette Vibrante (max 30 SP)
   PL: - Maks. HP +25%\n- Umiejętności nakładają o 1 więcej Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]\n- Jeżeli cel posiada Palette Vibrante, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury, w której ta jednostka użyje „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za każdego Grzesznika z Palette Vibrante odzyskuje 10 Poczytalności (maks. 30)
24. [Słowo kluczowe [FavorBuffTwthHardTwo] — podsumowanie] 출혈 위력, 침잠 위력, 찢긴 색채 부여량 증가\n대상에게 강렬한 색채가 있으면 합 위력, 기본 위력이 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].summary
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Słowo kluczowe [FavorBuff5001FirstPhaseForUI] — nazwa] 사영 [중지]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001FirstPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001FirstPhaseForUI]`
   limit: do 50 znaków
   EN: Shade of Reflection [The Middle]
   PL: Cień Projekcji [Środkowy]
26. [Słowo kluczowe [FavorBuff5001FirstPhaseForUI] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 리카르도의 첫 번째, 두 번째 <color=#f8c200>패턴이 변경</color>되며, <color=#f8c200>모든 E.G.O 자원을 2개씩 얻음</color>\n- <color=#f8c200>수비 스킬을 장착</color>한 인격에게는 리카르도의 스킬 효과로 <color=#f8c200>마비가 부여되지 않음</color>\n- 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>질투</color> 속성에 해당하는 공격 스킬의 피해량 +30% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001FirstPhaseForUI].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, activate the following effects:\n · Ricardo's first and second <color=#f8c200>patterns change</color>\n · <color=#f8c200>Gain 2 E.G.O Resources for all Affinities</color>\n- Ricardo's Skill effects <color=#f8c200>do not inflict Paralyze</color> on Identities that have <color=#f8c200>equipped Defense Skills</color>\n- The Identities' Attack Skills that are <color=#f8c200>Envy</color> Skills or Skills that inflict <color=#f8c200>Bleed or 'Unique Bleed'</color> deal +30% damage (for E.G.O Skills, deal +100% damage instead)\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - Jeżeli na początku spotkania na polu jest co najmniej 4 Tożsamości <color=#f8c200>frakcji Środkowego</color>, pierwszy i drugi wzorzec Ricarda <color=#f8c200>ulega zmianie</color>, a Ty <color=#f8c200>zyskujesz po 2 Zasobów E.G.O każdego Grzechu</color>\n- Umiejętności Ricarda <color=#f8c200>nie nakładają Paraliżu</color> na Tożsamości, które mają <color=#f8c200>wyposażone Umiejętności obrony</color>\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Krwawienie lub „Specjalne Krwawienie”</color> albo należą do Grzechu <color=#f8c200>Zawiści</color>, zadają obrażenia +30% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Jeżeli na początku walki wywołano <color=#f8c200>Rezonans Absolutny</color>, 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O najmniej posiadanego Grzechu</color>
27. [Słowo kluczowe [FavorBuff5001SecondPhaseForUI] — nazwa] 사영 [급습]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001SecondPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001SecondPhaseForUI]`
   limit: do 50 znaków
   EN: Shade of Reflection [Ambuscade]
   PL: Cień Projekcji [Zasadzka]
28. [Słowo kluczowe [FavorBuff5001SecondPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- <color=#f8c200>H사 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -30%\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>\n- 리카르도가 <color=#f8c200>흐트러짐 상태</color>일 때 공격자의 속도가 더 빠르면, (속도 차이 x 2)% 만큼 <color=#f8c200>받는 피해량이 증가</color> (최대 20%)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001SecondPhaseForUI].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gluttony</color> Skills or Skills that inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- <color=#f8c200>H Corp.</color> Identities deal +15% damage and take -30% damage\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>\n- If the attacker's Speed is faster than Ricardo's when he is <color=#f8c200>Staggered</color>, Ricardo takes <color=#f8c200>+(Speed difference x 2)% damage</color> (max 20%)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Rozdarcie</color> albo należą do Grzechu <color=#f8c200>Obżarstwa</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Tożsamości <color=#f8c200>Korporacji H</color> zadają wrogom obrażenia +15%, a otrzymują -30%\n- Jeżeli na początku walki wywołano <color=#f8c200>Rezonans Absolutny</color>, 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O najmniej posiadanego Grzechu</color>\n- Gdy Ricardo jest w stanie <color=#f8c200>Oszołomienia</color>, a atakujący jest szybszy, jego <color=#f8c200>otrzymywane obrażenia rosną</color> o (różnica Szybkości x 2)% (maks. 20%)
29. [Słowo kluczowe [FavorBuff5001HardForUI] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001HardForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001HardForUI]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Słowo kluczowe [FavorBuff5001HardForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%\n- [2페이즈 전용]\n · 리카르도와 아우들의 정신력이 0 미만으로 감소하지 않음\n · 턴 시작시 이전 턴에 리카르도를 공격한 모든 적에게 [장부에 적힘] 2 부여
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001HardForUI].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills deal +20% damage\n- [Phase 2 Exclusive Effect]\n · Ricardo and his Siblings' SP do not fall below 0\n · Turn Start: Inflict 2 "Written in the Book" on all enemies that attacked Ricardo in the previous turn
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności zadają obrażenia +20%\n- [Efekt wyłącznie 2. fazy]\n · Poczytalność Ricarda i jego Braci nie spada poniżej 0\n · Na początku tury na wszystkich wrogów, którzy w poprzedniej turze zaatakowali Ricarda, nakładane są 2 „Zapisano w Księdzie”
31. [Słowo kluczowe [FavorBuff5001AllyFirst] — nazwa] 사영 [중지]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001AllyFirst]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Słowo kluczowe [FavorBuff5001AllyFirst] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 모든 E.G.O 자원을 2개씩 얻음\n- 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>질투</color> 속성에 해당하는 공격 스킬의 피해량 +30% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 E.G.O 자원 1개를 4회 획득
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, gain 2 E.G.O Resources for all Affinities\n- Attack Skills that are <color=#f8c200>Envy</color> Skills or Skills that inflict <color=#f8c200>Bleed or 'Unique Bleed'</color> deal +30% damage (for E.G.O Skills, deal +100% damage instead)\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności nakładają o 1 więcej <color=#ff0000>Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]</color>\n- Jeżeli cel posiada <color=#ff0000>Palette Vibrante</color>, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury użycia „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za Grzesznika z <color=#ff0000>Palette Vibrante</color> <color=#ff0000>odzyskuje 10 Poczytalności</color> (maks. 30)
33. [Słowo kluczowe [FavorBuff5001AllyFirst] — podsumowanie] 출혈 스킬 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].summary
   limit: do 120 znaków
   EN: Bleed Skills deal more damage
   PL: Umiejętności Krwawienia zadają więcej obrażeń
34. [Słowo kluczowe [FavorBuff5001EnemyFirst] — nazwa] 사영 [중지]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001EnemyFirst]`
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Słowo kluczowe [FavorBuff5001EnemyFirst] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 리카르도의 첫 번째, 두 번째 <color=#f8c200>패턴이 변경</color>됨\n- <color=#f8c200>수비 스킬을 장착</color>한 인격에게는 리카르도의 스킬 효과로 <color=#f8c200>마비가 부여되지 않음</color>
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, Ricardo's first and second <color=#f8c200>patterns change</color>\n- Ricardo's Skill effects <color=#f8c200>do not inflict Paralyze</color> on Identities that have <color=#f8c200>equipped Defense Skills</color>
   PL: - Jeżeli na początku spotkania na polu jest co najmniej 4 Tożsamości <color=#f8c200>frakcji Środkowego</color>, pierwszy i drugi wzorzec Ricarda <color=#f8c200>ulega zmianie</color>\n- Umiejętności Ricarda <color=#f8c200>nie nakładają Paraliżu</color> na Tożsamości, które mają <color=#f8c200>wyposażone Umiejętności obrony</color>
36. [Słowo kluczowe [FavorBuff5001EnemyFirst] — podsumowanie] 수비 스킬 장착 인격에게는 마비를 부여하지 않음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].summary
   limit: do 120 znaków
   EN: Does not inflict Paralyze on Identities that have equipped Defense Skills
   PL: Nie nakłada Paraliżu na Tożsamości z wyposażonymi Umiejętnościami obrony
37. [Słowo kluczowe [FavorBuff5001AllyTwo] — nazwa] 사영 [급습]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001AllyTwo]`
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Słowo kluczowe [FavorBuff5001AllyTwo] — opis] - 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- <color=#f8c200>H사 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -30%\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gluttony</color> Skills or Skills that inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- <color=#f8c200>H Corp.</color> Identities deal +15% damage and take -30% damage\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - Ataki <color=#f8c200>Obżarstwa</color> lub z <color=#f8c200>Rozdarciem</color>: +25% obrażeń (E.G.O +100%)\n- Tożsamości <color=#f8c200>Korporacji H</color>: +15% zadawanych, -30% otrzymywanych\n- Na początku walki przy <color=#f8c200>Rezonansie Absolutnym</color> 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O rzadkiego Grzechu</color>
39. [Słowo kluczowe [FavorBuff5001AllyTwo] — podsumowanie] 탐식 스킬 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].summary
   limit: do 120 znaków
   EN: Gluttony Skills deal more damage
   PL: Umiejętności Grzechu Obżarstwa zadają więcej obrażeń
40. [Słowo kluczowe [FavorBuff5001EnemySecond] — nazwa] 사영 [급습]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001EnemySecond]`
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
41. [Słowo kluczowe [FavorBuff5001EnemySecond] — opis] - 리카르도가 <color=#f8c200>흐트러짐 상태</color>일 때 공격자의 속도가 더 빠르면, (속도 차이 x 2)% 만큼 받는 <color=#f8c200>피해량이 증가</color> (최대 20%)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: - If the attacker's Speed is faster than Ricardo's when he is <color=#f8c200>Staggered</color>, Ricardo takes <color=#f8c200>+(Speed difference x 2)% damage</color> (max 20%)
   PL: - Gdy Ricardo jest w stanie <color=#f8c200>Oszołomienia</color>, a atakujący jest szybszy, jego <color=#f8c200>otrzymywane obrażenia rosną</color> o (różnica Szybkości x 2)% (maks. 20%)
42. [Słowo kluczowe [FavorBuff5001EnemySecond] — podsumowanie] 속도 차이에 비례하여 피해량 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].summary
   limit: do 120 znaków
   EN: Take more damage based on Speed difference
   PL: Otrzymywane obrażenia rosną proporcjonalnie do różnicy Szybkości
43. [Słowo kluczowe [FavorBuff5001Hard] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001Hard].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001Hard]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Słowo kluczowe [FavorBuff5001Hard] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001Hard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills deal +20% damage
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności zadają obrażenia +20%
45. [Słowo kluczowe [FavorBuff5001Hard] — podsumowanie] Hard 난이도 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001Hard].summary
   limit: do 120 znaków
   EN: Hard Difficulty Tribulation
   PL: Utrapienie na poziomie trudności Hard
46. [Słowo kluczowe [FavorBuff5001HardTwo] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5001HardTwo]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Słowo kluczowe [FavorBuff5001HardTwo] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%\n- [2페이즈 전용]\n · 리카르도와 아우들의 정신력이 0 미만으로 감소하지 않음\n · 턴 시작시 이전 턴에 리카르도를 공격한 모든 적에게 [장부에 적힘] 2 부여
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].desc
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Słowo kluczowe [FavorBuff5001HardTwo] — podsumowanie] Hard 난이도 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].summary
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Słowo kluczowe [RicardoBookRaid] — nazwa] 장부에 적힘
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoBookRaid].name
   kontekst: identyfikator tagu w tekstach: `[RicardoBookRaid]`
   limit: do 40 znaków
   EN: Written in the Book
   PL: Zapisano w Księdzie
50. [Słowo kluczowe [RicardoBookRaid] — opis] 최댓값 : 30\n수치당 받는 피해량 +3%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoBookRaid].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 30\nTake +3% damage for every Stack
   PL: Maks. ładunków: 30\nOtrzymywane obrażenia +3% za ładunek
51. [Słowo kluczowe [RicardoTattooRaid] — nazwa] 원한 문신
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoTattooRaid].name
   kontekst: identyfikator tagu w tekstach: `[RicardoTattooRaid]`
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL: Tatuaż Zemsty
52. [Słowo kluczowe [RicardoTattooRaid] — opis] 최댓값 : 300\n수치 10당 자신의 스킬 공격 레벨 +1
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoTattooRaid].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 300\nSkills gain Offense Level +1 for every 10 Stack
   PL: Maks. ładunków: 300\nZa każde 10 ładunków Umiejętności tej jednostki zyskują Poziom Ataku +1
53. [Słowo kluczowe [RicardoJokeRaid] — nazwa] 형님의 시험
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoJokeRaid].name
   kontekst: identyfikator tagu w tekstach: `[RicardoJokeRaid]`
   limit: do 40 znaków
   EN: Test of the Big Brother
   PL: Test Starszego Brata
54. [Słowo kluczowe [RicardoJokeRaid] — opis] 턴 종료시 1 감소\n이 효과가 있는 동안 스킬 피해, 진동 폭발로 인한 흐트러짐 손상을 2배로 받음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=RicardoJokeRaid].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 1 Stack\nWhile this effect is active, double damage taken from Skills, and double the amount of Stagger threshold raised from Tremor Burst
   PL: Na koniec tury traci 1 ładunek\nDopóki aktywny jest ten efekt, obrażenia od Umiejętności oraz obniżenie Progu Oszołomienia z Wyładowania Wstrząsu są podwajane
55. [Słowo kluczowe [FavorBuff5012AllyOne] — nazwa] 사영 [곰 사냥]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012AllyOne]`
   limit: do 50 znaków
   EN: Shade of Reflection [Bearhunt]
   PL: Cień Projekcji [Niedźwiedzi Łów]
56. [Słowo kluczowe [FavorBuff5012AllyOne] — opis] - 인격의 스킬 중 화상, 특수 화상을 부여하거나 분노 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적의 보호막에 진동 폭발로 흐트러짐 손상을 줄 때 대신 분노 피해를 줌\n· 위 효과로 분노 피해를 줄 때 보호막에 입히는 피해량 +50% (소수점 버림)\n- 죄악 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Identities' Attack Skills that are Wrath Skills or Skills that inflict Burn or 'Unique Burn' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When raising Stagger threshold via Tremor Burst against enemy Shield, deal Wrath damage instead\n· When dealing Wrath damage via the above effect, deal +50% damage against Shield (rounded down)\n- Upon Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które nakładają Podpalenie lub „Specjalne Podpalenie” albo należą do Grzechu Gniewu, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Wyładowanie Wstrząsu zadaje obrażenia Oszołomienia Tarczy wroga, zamiast tego zadaje obrażenia od Gniewu\n· Zadając w ten sposób obrażenia od Gniewu, zadaje Tarczy obrażenia +50% (zaokrąglane w dół)\n- Przy Rezonansie zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
57. [Słowo kluczowe [FavorBuff5012AllyOne] — podsumowanie] 화상 스킬 피해량 증가, 흐트러짐 손상으로 분노 피해
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].summary
   limit: do 130 znaków
   EN: Burn Skills and 'Unique Burn' Skills deal more damage; raising Stagger threshold deals Wrath damage
   PL: Umiejętności Podpalenia i „Specjalnego Podpalenia” zadają więcej obrażeń; obniżanie Progu Oszołomienia zadaje obrażenia od Gniewu
58. [Słowo kluczowe [FavorBuff5012EnemyOne] — nazwa] 사영 [곰 사냥]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012EnemyOne].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012EnemyOne]`
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Słowo kluczowe [FavorBuff5012EnemyOne] — opis] - 화상 및 특수 화상 피해를 입을 때 보호막이 받는 피해량 +50% (소수점 버림)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012EnemyOne].desc
   limit: do 120 znaków
   EN: - Shield takes +50% damage from Burn and 'Unique Burn' (rounded down)
   PL: - Tarcza otrzymuje obrażenia +50% od Podpalenia i „Specjalnego Podpalenia” (zaokrąglane w dół)
60. [Słowo kluczowe [FavorBuff5012AllyTwo] — nazwa] 사영 [범 사냥]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012AllyTwo]`
   limit: do 50 znaków
   EN: Shade of Reflection [Tigerhunt]
   PL: Cień Projekcji [Tygrysi Łów]
61. [Słowo kluczowe [FavorBuff5012AllyTwo] — opis] - 인격의 스킬 중 호흡 위력 또는 호흡 횟수를 부여하거나 획득하거나 소모하는 효과가 있는 공격 스킬 또는 오만 속성 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 오만 속성 스킬 사용 시 해당 스킬 등급에 해당하는 호흡 위력을 얻고, 호흡 횟수 2 증가 (수감자당 턴당 2회, E.G.O 스킬은 3등급으로 취급함)\n- 검계 소속 인격이면, 아래 효과 적용\n· 맨 앞의 흐트러짐 구간 1개 제거\n· 최종 위력 +2\n· 적에게 가하는 피해량 +30%, 받는 피해량 -15%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Identities' Attack Skills that are Pride Skills, or Attack Skills that apply, gain, or consume Poise deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When using Pride Skills, gain (Skill's Rank) Poise Potency and +2 Poise Count (2 times per turn per Sinner; E.G.O Skills are considered Skill 3 for this purpose)\n- For Blade Lineage Identities, apply the following effects:\n· Remove this unit's first Stagger Threshold\n· Final Power +2\n· Deal +30% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które należą do Grzechu Pychy albo nakładają, zyskują lub zużywają Siłę Oddechu bądź Licznik Oddechu, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy użyciu Umiejętności Grzechu Pychy zyskuj Siłę Oddechu równą randze Umiejętności oraz Licznik Oddechu +2 (2 razy na turę na Grzesznika; Umiejętności E.G.O liczą się jako ranga 3)\n- Tożsamości z Rodu Ostrza otrzymują następujące efekty:\n· Usunięcie pierwszego Progu Oszołomienia tej jednostki\n· Moc Końcowa +2\n· Obrażenia zadawane wrogom +30%, otrzymywane -15%
62. [Słowo kluczowe [FavorBuff5012AllyTwo] — podsumowanie] 호흡 스킬 또는 오만 스킬 피해량 증가, 오만 속성일 시 호흡 얻음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].summary
   limit: do 120 znaków
   EN: Poise Skills and Pride Skills deal more damage; gain Poise when using Pride Skills
   PL: Umiejętności Oddechu i Grzechu Pychy zadają więcej obrażeń; przy użyciu Umiejętności Grzechu Pychy zyskuje Oddech
63. [Słowo kluczowe [FavorBuff5012HardOne] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardOne].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012HardOne]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Słowo kluczowe [FavorBuff5012HardOne] — opis] - 최대 체력 +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 호흡 횟수가 5 이하면, 자신의 호흡 횟수 2 증가
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardOne].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" and "Sword of the Homeland [Sal] - Swordhoning", if this unit is at 5 or fewer Poise Count, gain +2 Poise Count
   PL: - Maks. HP +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” i „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli Licznik Oddechu tej jednostki wynosi 5 lub mniej, zyskuje Licznik Oddechu +2
65. [Słowo kluczowe [FavorBuff5012HardTwo] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012HardTwo]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Słowo kluczowe [FavorBuff5012HardTwo] — opis] - 최대 체력 +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 호흡 횟수가 5 이하면, 자신의 호흡 횟수 2 증가\n- [2페이즈 전용 효과] ‘본국검술[살] - 태세 변경’ 패시브의 효과로 본국검술[살]이 5로 초기화 될 때, 자신의 본국태세에 따라 본국검술[살] 2을 추가로 얻거나 잃음\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardTwo].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" and "Sword of the Homeland [Sal] - Swordhoning", if this unit is at 5 or fewer Poise Count, gain +2 Poise Count\n- [Phase 2 Exclusive Effect] When Swordplay of the Homeland [Sal] resets to 5 due to the effects of "Swordplay of the Homeland [Sal] - Shift Battleform" Passive, gain or lose 2 Swordplay of the Homeland [Sal] Stack based on Battleform of the Homeland on self\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Maks. HP +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” i „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli Licznik Oddechu tej jednostki wynosi 5 lub mniej, zyskuje Licznik Oddechu +2\n- [Efekt wyłącznie 2. fazy] Gdy Sztuka Miecza Ojczyzny [Sal] zostaje zresetowana do 5 przez pasywną Umiejętność „Sztuka Miecza Ojczyzny [Sal] – Zmiana Formy Walki”, w zależności od Formy Bojowej Ojczyzny tej jednostki dodatkowo zyskuje lub traci 2 Sztuki Miecza Ojczyzny [Sal]\n· Forma Bojowa Ojczyzny – Niedźwiedzi Łów: zyskuje\n· Forma Bojowa Ojczyzny – Tygrysi Łów: traci
67. [Słowo kluczowe [FavorBuff5012AllyOneForUI] — nazwa] 사영 [곰 사냥]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyOneForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012AllyOneForUI]`
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Słowo kluczowe [FavorBuff5012AllyOneForUI] — opis] - 인격의 스킬 중 <color=#f8c200>화상, 특수 화상을 부여하거나 분노 속성</color>에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적의 보호막에 <color=#f8c200>진동 폭발</color>로 흐트러짐 손상을 줄 때 대신 <color=#f8c200>분노 피해</color>를 줌\n· 위 효과로 <color=#f8c200>분노 피해</color>를 주거나 대상이 <color=#f8c200>화상 및 특수 화상</color> 피해를 입을 때 <color=#f8c200>보호막</color>이 받는 피해량 +50% (소수점 버림)\n- 죄악 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyOneForUI].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Wrath Skills or Skills that inflict Burn or 'Unique Burn'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When raising Stagger threshold via <color=#f8c200>Tremor Burst</color> against enemy Shield, deal <color=#f8c200>Wrath damage</color> instead\n· When dealing <color=#f8c200>Wrath damage</color> via the above effect against target, or when target takes <color=#f8c200>Burn or 'Unique Burn'</color> damage, target's <color=#f8c200>Shield</color> takes +50% damage (rounded down)\n- Upon Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Podpalenie lub „Specjalne Podpalenie” albo należą do Grzechu Gniewu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Wyładowanie Wstrząsu zadaje <color=#f8c200>obrażenia Oszołomienia</color> Tarczy wroga, zamiast tego zadaje <color=#f8c200>obrażenia od Gniewu</color>\n· Zadając w ten sposób <color=#f8c200>obrażenia od Gniewu</color> lub gdy cel otrzymuje obrażenia od <color=#f8c200>Podpalenia i „Specjalnego Podpalenia”</color>, jego <color=#f8c200>Tarcza</color> otrzymuje obrażenia +50% (zaokrąglane w dół)\n- Przy Rezonansie zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
69. [Słowo kluczowe [FavorBuff5012AllyTwoForUI] — nazwa] 사영 [범 사냥]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyTwoForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012AllyTwoForUI]`
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Słowo kluczowe [FavorBuff5012AllyTwoForUI] — opis] - 인격의 스킬 중 <color=#f8c200>호흡 위력 또는 호흡 횟수를 부여하거나 획득하거나 소모하는 효과가 있는 공격 스킬 또는 오만 속성</color>공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 오만 속성 스킬 사용 시 해당 스킬 등급에 해당하는 <color=#f8c200>호흡 위력을 얻고</color>, 호흡 횟수 2 증가 (수감자당 턴당 2회, E.G.O 스킬은 3등급으로 취급함)\n- <color=#f8c200>검계 소속 인격</color>이면, 아래 효과 적용\n· 맨 앞의 흐트러짐 구간 1개 제거\n· 최종 위력 +2\n· 적에게 가하는 피해량 +30%, 받는 피해량 -15%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012AllyTwoForUI].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' <color=#f8c200>Attack Skills that are Pride Skills, or Attack Skills that apply, gain, or consume Poise</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When using Pride Skills, <color=#f8c200>gain (Skill's Rank) Poise Potency</color> and +2 Poise Count (2 times per turn per Sinner; E.G.O Skills are considered Skill 3 for this purpose)\n- For <color=#f8c200>Blade Lineage Identities</color>, apply the following effects:\n· Remove this unit's first Stagger Threshold\n· Final Power +2\n· Deal +30% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>należą do Grzechu Pychy albo nakładają, zyskują lub zużywają Siłę Oddechu bądź Licznik Oddechu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy użyciu Umiejętności Grzechu Pychy <color=#f8c200>zyskuje Siłę Oddechu równą randze Umiejętności</color> oraz Licznik Oddechu +2 (2 razy na turę na Grzesznika; Umiejętności E.G.O liczą się jako ranga 3)\n- Tożsamości <color=#f8c200>z Rodu Ostrza</color> otrzymują następujące efekty:\n· Usunięcie pierwszego Progu Oszołomienia tej jednostki\n· Moc Końcowa +2\n· Obrażenia zadawane wrogom +30%, otrzymywane -15%
71. [Słowo kluczowe [FavorBuff5012HardTwoForUI] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardTwoForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuff5012HardTwoForUI]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Słowo kluczowe [FavorBuff5012HardTwoForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 <color=#ff0000>호흡 횟수가 5 이하</color>면, 자신의 호흡 횟수 2 증가\n- [2페이즈 전용 효과] ‘본국검술[살] - 태세 변경’ 패시브의 효과로 본국검술[살]이 <color=#ff0000>5로 초기화 될 때</color>, 자신의 본국태세에 따라 본국검술[살] <color=#ff0000>2을 추가로 얻거나 잃음</color>\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuff5012HardTwoForUI].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" or "Sword of the Homeland [Sal] - Swordhoning", if this unit is at <color=#ff0000>5- Poise Count</color>, gain +2 Poise Count\n- [Phase 2 Exclusive Effect] When Swordplay of the Homeland [Sal] <color=#ff0000>resets to 5</color> due to the effects of "Swordplay of the Homeland [Sal] - Shift Battleform" Passive, <color=#ff0000>gain or lose an additional 2</color> Swordplay of the Homeland [Sal] Stack based on Battleform of the Homeland on self\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” lub „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli <color=#ff0000>Licznik Oddechu tej jednostki wynosi 5 lub mniej</color>, zyskuje Licznik Oddechu +2\n- [Efekt wyłącznie 2. fazy] Gdy Sztuka Miecza Ojczyzny [Sal] <color=#ff0000>zostaje zresetowana do 5</color> przez pasywną Umiejętność „Sztuka Miecza Ojczyzny [Sal] – Zmiana Formy Walki”, w zależności od Formy Bojowej Ojczyzny tej jednostki <color=#ff0000>dodatkowo zyskuje lub traci 2</color> Sztuki Miecza Ojczyzny [Sal]\n· Forma Bojowa Ojczyzny – Niedźwiedzi Łów: zyskuje\n· Forma Bojowa Ojczyzny – Tygrysi Łów: traci
73. [Słowo kluczowe [FavorBuffLeiheng] — nazwa] 사영 [삽시호]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeiheng]`
   limit: do 50 znaków
   EN: Shade of Reflection [Chachihu]
   PL: Cień Projekcji [Chachihu]
74. [Słowo kluczowe [FavorBuffLeiheng] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +8 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 인격이 적과 합 진행 시, 메인 타겟의 <color=#f8c200>속박</color> 2당 합 위력 +1 (최대 2)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - If an Identity is on the field, <color=#f8c200>remove 1 Stagger Threshold</color> and gain +8 Base Offense Level and +8 Base Defense Level (effect does not stack)\n- On <color=#f8c200>Reson.,</color> gain 1 E.G.O resource for the respective Affinity and 1 random least-owned E.G.O resource (2 times per turn)\n- E.G.O Skills deal +50% damage\n- Identity Skills that either are <color=#f8c200>Gluttony</color> Skills or inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When an Identity Clashes with an enemy, the Identity gains +1 Clash Power for every 2 <color=#f8c200>Bind</color> on the main target (max 2)
   PL: - Każda Tożsamość na polu bitwy <color=#f8c200>usuwa 1 Próg Oszołomienia</color> i zyskuje +8 do Podstawowego Poziomu Ataku i +8 do Podstawowego Poziomu Obrony (nie kumuluje się)\n- Przy <color=#f8c200>Rezonansie</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)\n- Umiejętności E.G.O zadają obrażenia +50%\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Rozdarcie</color> albo należą do Grzechu <color=#f8c200>Obżarstwa</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Tożsamość prowadzi Starcie z wrogiem, zyskuje Moc Starcia +1 za każde 2 <color=#f8c200>Spętania</color> na głównym celu (maks. 2)
75. [Słowo kluczowe [FavorBuffLeihengTwo] — nazwa] 사영 [천퇴성]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeihengTwo]`
   limit: do 50 znaków
   EN: Shade of Reflection [Tiantui Star]
   PL: Cień Projekcji [Gwiazda Tiantui]
76. [Słowo kluczowe [FavorBuffLeihengTwo] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +15 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 2개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>화상, 특수 화상</color>을 부여하거나 <color=#f8c200>분노</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengTwo].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - If an Identity is on the field, <color=#f8c200>remove 1 Stagger Threshold</color> and gain +15 Base Offense Level and +15 Base Defense Level (effect does not stack)\n- On <color=#f8c200>Reson.,</color> gain 1 E.G.O resource for the respective Affinity and 2 random least-owned E.G.O resources (2 times per turn)\n- E.G.O Skills deal +50% damage\n- Identity Skills that either are <color=#f8c200>Wrath</color> Skills or inflict <color=#f8c200>Burn or Unique Burn</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)
   PL: - Każda Tożsamość na polu bitwy <color=#f8c200>usuwa 1 Próg Oszołomienia</color> i zyskuje +15 do Podstawowego Poziomu Ataku i +15 do Podstawowego Poziomu Obrony (nie kumuluje się)\n- Przy <color=#f8c200>Rezonansie</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 2 losowe najmniej posiadane Zasoby E.G.O (2 razy na turę)\n- Umiejętności E.G.O zadają obrażenia +50%\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Podpalenie lub „Specjalne Podpalenie”</color> albo należą do Grzechu <color=#f8c200>Gniewu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)
77. [Słowo kluczowe [FavorBuffLeihengHard] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHard].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeihengHard]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Słowo kluczowe [FavorBuffLeihengHard] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHard].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +80%\n- SP does not drop below 0\n- Deal +50% damage against targets that have <color=#ff0000>Prey</color> (does not trigger if the target has Defense Skills equipped). Take -50% damage from targets that have <color=#ff0000>Prey</color>\n- <color=#ff0000>If this unit has 3+ Tigermark Rounds</color> when using the Blasting Shatterslash [爆碎斬] Skill, deal +100% damage
   PL: - <color=#ff0000>Maks. HP</color> +80%\n- Poczytalność nie spada poniżej 0\n- Celom posiadającym <color=#ff0000>Zdobycz</color> zadaje obrażenia +50% (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a otrzymuje od nich -50%\n- Jeżeli przy użyciu Umiejętności „Roztrzaskujące Cięcie [爆碎斬]” ma co najmniej 3 <color=#ff0000>Pociski Tygrysiego Znaku</color>, zadaje obrażenia +100%
79. [Słowo kluczowe [FavorBuffLeihengHard] — podsumowanie] Hard 난이도 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHard].summary
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Słowo kluczowe [FavorBuffLeihengHardTwo] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeihengHardTwo]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Słowo kluczowe [FavorBuffLeihengHardTwo] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%\n- [2페이즈 전용 효과]\n· 스킬 사용 시 <color=#ff0000>메인 타겟이 사냥감</color>을 보유했으면, <color=#ff0000>기본 위력이 5 증가하고 피해량 +200%</color> (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 해당 스킬의 모든 코인이 <color=#ff0000>파괴 불가 코인</color>으로 변경됨\n· <color=#ff0000>사냥감</color>을 보유한 대상에게 합 패배 시, <color=#ff0000>절참 [切斬]</color> 1 얻음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +80%\n- SP does not drop below 0\n- Deal +50% damage against targets that have <color=#ff0000>Prey</color> (does not trigger if the target has Defense Skills equipped). Take -50% damage from targets that have <color=#ff0000>Prey</color>\n- <color=#ff0000>If this unit has 3+ Tigermark Rounds</color> when using the Blasting Shatterslash [爆碎斬] Skill, deal +100% damage\n- [Phase 2 Exclusive Effect]\n· On Skill Use, <color=#ff0000>if the main target has Prey,</color> <color=#ff0000>gain Base Power +5, deal +200% damage</color> (does not trigger if the target has Defense Skills equipped), and convert all Coins on the Skill into <color=#ff0000>Unbreakable Coins</color>\n· On Clash Lose against targets that have <color=#ff0000>Prey</color>, gain 1 <color=#ff0000>Severing Slash [切斬]</color>
   PL: - <color=#ff0000>Maks. HP</color> +80%\n- Poczytalność nie spada poniżej 0\n- Celom posiadającym <color=#ff0000>Zdobycz</color> zadaje obrażenia +50% (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a otrzymuje od nich -50%\n- Jeżeli przy użyciu Umiejętności „Roztrzaskujące Cięcie [爆碎斬]” ma co najmniej 3 <color=#ff0000>Pociski Tygrysiego Znaku</color>, zadaje obrażenia +100%\n- [Efekt wyłącznie 2. fazy]\n· Przy użyciu Umiejętności, <color=#ff0000>jeżeli główny cel posiada Zdobycz</color>, <color=#ff0000>zyskuje Moc Bazową +5 i zadaje obrażenia +200%</color> (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a wszystkie Monety tej Umiejętności stają się <color=#ff0000>Niezniszczalnymi Monetami</color>\n· Po przegranym Starciu z celem posiadającym <color=#ff0000>Zdobycz</color> zyskuje 1 <color=#ff0000>Przecinające Cięcie [切斬]</color>
82. [Słowo kluczowe [FavorBuffLeihengHardTwo] — podsumowanie] Hard 난이도 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].summary
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Słowo kluczowe [FavorBuffLeiheng1stPhaseForUI] — nazwa] 사영 [삽시호]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng1stPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeiheng1stPhaseForUI]`
   (powtórzenie elementu 73 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Słowo kluczowe [FavorBuffLeiheng1stPhaseForUI] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +8 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 인격이 적과 합 진행 시, 메인 타겟의 <color=#f8c200>속박</color> 2당 합 위력 +1 (최대 2)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng1stPhaseForUI].desc
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Słowo kluczowe [FavorBuffLeiheng2ndPhaseForUI] — nazwa] 사영 [천퇴성]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng2ndPhaseForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeiheng2ndPhaseForUI]`
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Słowo kluczowe [FavorBuffLeiheng2ndPhaseForUI] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +15 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 2개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>화상, 특수 화상</color>을 부여하거나 <color=#f8c200>분노</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeiheng2ndPhaseForUI].desc
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
87. [Słowo kluczowe [FavorBuffLeihengHardForUI] — nazwa] 고난
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHardForUI].name
   kontekst: identyfikator tagu w tekstach: `[FavorBuffLeihengHardForUI]`
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Słowo kluczowe [FavorBuffLeihengHardForUI] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%\n- [2페이즈 전용 효과]\n· 스킬 사용 시 <color=#ff0000>메인 타겟이 사냥감</color>을 보유했으면, <color=#ff0000>기본 위력이 5 증가하고 피해량 +200%</color> (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 해당 스킬의 모든 코인이 <color=#ff0000>파괴 불가 코인</color>으로 변경됨\n· <color=#ff0000>사냥감</color>을 보유한 대상에게 합 패배 시, <color=#ff0000>절참 [切斬]</color> 1 얻음
   źródło: BattleKeywords-BossRaid.json :: dataList[id=FavorBuffLeihengHardForUI].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +80%\n- SP does not drop below 0\n- Deal +50% damage against targets that have <color=#ff0000>Prey</color> (does not trigger if the target has Defense Skills equipped). Take -50% damage from targets that have <color=#ff0000>Prey</color>.\n- <color=#ff0000>If this unit has 3+ Tigermark Rounds</color> when using the Blasting Shatterslash [爆碎斬] Skill, deal +100% damage\n- [Phase 2 Exclusive Effect]\n· On Skill Use, <color=#ff0000>if the main target has Prey,</color> <color=#ff0000>gain Base Power +5, deal +200% damage</color> (does not trigger if the target has Defense Skills equipped), and convert all Coins on the Skill into <color=#ff0000>Unbreakable Coins</color>\n· On Clash Lose against targets that have <color=#ff0000>Prey</color>, gain 1 <color=#ff0000>Severing Slash[切斬]</color>
   PL: - <color=#ff0000>Maks. HP</color> +80%\n- Poczytalność nie spada poniżej 0\n- Celom posiadającym <color=#ff0000>Zdobycz</color> zadaje obrażenia +50% (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a otrzymuje od nich -50%\n- Jeżeli przy użyciu Umiejętności „Roztrzaskujące Cięcie [爆碎斬]” ma co najmniej 3 <color=#ff0000>Pociski Tygrysiego Znaku</color>, zadaje obrażenia +100%\n- [Efekt wyłącznie 2. fazy]\n· Przy użyciu Umiejętności, <color=#ff0000>jeżeli główny cel posiada Zdobycz</color>, <color=#ff0000>zyskuje Moc Bazową +5 i zadaje obrażenia +200%</color> (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a wszystkie Monety tej Umiejętności stają się <color=#ff0000>Niezniszczalnymi Monetami</color>\n· Po przegranym Starciu z celem posiadającym <color=#ff0000>Zdobycz</color> zyskuje 1 <color=#ff0000>Przecinające Cięcie [切斬]</color>
89. [Słowo kluczowe [HugeIrritationReflectrial] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: BattleKeywords-BossRaid.json :: dataList[id=HugeIrritationReflectrial].name
   kontekst: identyfikator tagu w tekstach: `[HugeIrritationReflectrial]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
90. [Słowo kluczowe [HugeIrritationReflectrial] — opis] - 턴 시작 시, 잃은 체력 15%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 5)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +3, 진동 횟수 증가량 +1\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 40%)\n- '이연참-폭', '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: BattleKeywords-BossRaid.json :: dataList[id=HugeIrritationReflectrial].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Damage Up and 1 Power Up for every 15% missing HP on self (max 5 each)\n- Inflict +3 more Tremor Potency and +1 more Tremor Count with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 40%)\n- Convert the final Coins of "Double Slash - Blast" and "Triple Slash - Blast" to Unbreakable Coins
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy za każde 15% utraconego HP (każdy maks. 5)\n- Umiejętności nakładają o 3 więcej Siły Wstrząsu i o 1 więcej Licznika Wstrząsu\n- Jeżeli Szybkość tej jednostki jest wyższa od Szybkości celu o 3 lub więcej, zadaje obrażenia +(różnica Szybkości względem celu x 5)% (maks. 40%)\n- Ostatnie Monety Umiejętności „Podwójne Cięcie – Wybuch” i „Potrójne Cięcie – Wybuch” zamieniają się w Niezniszczalne Monety
91. [Słowo kluczowe [Prey_leiheng] — nazwa] 사냥감
   źródło: BattleKeywords-BossRaid.json :: dataList[id=Prey_leiheng].name
   kontekst: identyfikator tagu w tekstach: `[Prey_leiheng]`
   limit: do 40 znaków
   EN: Prey
   PL: Zdobycz
92. [Słowo kluczowe [Prey_leiheng] — opis] - 적과 합 진행 시, 합 위력 - 5\n- 전투 시작 시,\n· 공격 스킬을 장착하였다면 공격 스킬로 뇌횡에게 가하는 피해량이 50%만큼 감소\n· 수비 스킬을 장착하였다면 뇌횡에게 받는 피해량이 75%만큼 감소\n- 이 효과를 보유한 상태에서 뇌횡과 합하여 승리 시, 제일 적게 보유한 E.G.O 자원 3개 획득\n- 턴 종료 시 사라지고, 자신의 정신력 10 회복
   źródło: BattleKeywords-BossRaid.json :: dataList[id=Prey_leiheng].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash with an enemy, Clash Power -5\n- Combat Start:\n· If this unit equipped an Attack Skill, deal -50% damage against Lei Heng using Attack Skills\n· If this unit equipped a Defense Skill, take -75% damage from Lei Heng\n- If this unit wins a Clash against Lei Heng while under this effect, gain 3 of the least-owned E.G.O Resources\n- Expires at Turn End; this unit heals 10 SP
   PL: - Podczas Starcia z wrogiem Moc Starcia -5\n- Na początku walki:\n· Jeżeli wyposażona jest Umiejętność ataku, obrażenia zadawane Lei Hengowi Umiejętnościami ataku maleją o 50%\n· Jeżeli wyposażona jest Umiejętność obrony, obrażenia otrzymywane od Lei Henga maleją o 75%\n- Jeżeli ta jednostka wygra Starcie z Lei Hengiem mając ten efekt, zyskuje 3 najmniej posiadane Zasoby E.G.O\n- Znika na koniec tury, a jednostka odzyskuje 10 Poczytalności

## Słowa kluczowe bitwy — BattleKeywords-Refraction1BokGak
- plik gry: `BattleKeywords-Refraction1BokGak.json` (opisy wyświetlane w dymkach pomocy podczas walki)

93. [Słowo kluczowe [AggressiveBokgak] — nazwa] 본능
   źródło: BattleKeywords-Refraction1BokGak.json :: dataList[id=AggressiveBokgak].name
   kontekst: identyfikator tagu w tekstach: `[AggressiveBokgak]`
   limit: do 40 znaków
   EN: Instincts
   PL: Instynkt
94. [Słowo kluczowe [AggressiveBokgak] — opis] 최댓값: 5\n턴 종료 시 수치가 4 이상이면 상태가 공격적으로 변경됨.
   źródło: BattleKeywords-Refraction1BokGak.json :: dataList[id=AggressiveBokgak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\nTurn End: At 4+ Stack, change to an “aggressive” state.
   PL: Maks. ładunków: 5\nNa koniec tury przy 4 lub więcej ładunkach stan zmienia się na „agresywny”.
95. [Słowo kluczowe [DeadEGOResource] — nazwa] 남겨진 의지
   źródło: BattleKeywords-Refraction1BokGak.json :: dataList[id=DeadEGOResource].name
   kontekst: identyfikator tagu w tekstach: `[DeadEGOResource]`
   limit: do 40 znaków
   EN: Lingering Determination
   PL: Zostawiona Determinacja
96. [Słowo kluczowe [DeadEGOResource] — opis] 사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼  얻음
   źródło: BattleKeywords-Refraction1BokGak.json :: dataList[id=DeadEGOResource].desc
   limit: do 140 znaków
   EN: When defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this Identity has
   PL: Przy pokonaniu zyskujesz Zasoby E.G.O odpowiadające Grzechom i rangom każdej Umiejętności ataku tej Tożsamości

## Słowa kluczowe bitwy — BattleKeywords-Refraction2BokGak
- plik gry: `BattleKeywords-Refraction2BokGak.json` (opisy wyświetlane w dymkach pomocy podczas walki)

97. [Słowo kluczowe [PassedPortal_GreenBokGak] — nazwa] 독이 들끓는 차원
   źródło: BattleKeywords-Refraction2BokGak.json :: dataList[id=PassedPortal_GreenBokGak].name
   kontekst: identyfikator tagu w tekstach: `[PassedPortal_GreenBokGak]`
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL: Wymiar Wrzącej Trucizny
98. [Słowo kluczowe [PassedPortal_GreenBokGak] — opis] 본체 최대 체력이 20% 증가
   źródło: BattleKeywords-Refraction2BokGak.json :: dataList[id=PassedPortal_GreenBokGak].desc
   limit: do 120 znaków
   EN: Core's max HP +20%
   PL: Maks. HP Rdzenia +20%
99. [Słowo kluczowe [PassedPortal_GreenBokGak] — podsumowanie] 최대 체력 20% 증가
   źródło: BattleKeywords-Refraction2BokGak.json :: dataList[id=PassedPortal_GreenBokGak].summary
   limit: do 120 znaków
   EN: Max HP +20%
   PL: Maks. HP +20%

## Słowa kluczowe bitwy — BattleKeywords-a1c10p1
- plik gry: `BattleKeywords-a1c10p1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

100. [Słowo kluczowe [NoirNoComply] — nazwa] 안내 불이행
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirNoComply].name
   kontekst: identyfikator tagu w tekstach: `[NoirNoComply]`
   limit: do 40 znaków
   EN: Instruction Incompliance
   PL: Nieprzestrzeganie Instrukcji
101. [Słowo kluczowe [NoirNoComply] — opis] - 최댓값 : 3\n- 수치당 받는 피해량 +5%
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirNoComply].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Take +5% damage for every Stack
   PL: - Maks. ładunków: 3\n- Otrzymuje obrażenia +5% za każdy ładunek
102. [Słowo kluczowe [NoirNoComply] — tekst klimatyczny] 브랜드 규정을 지켜주시지 않았기에 브랜드 방향성 보존을 위한 제재에 들어갈 수 있습니다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirNoComply].flavor
   limit: do 180 znaków
   EN: Failure to comply with the brand's doctrine instructions may result in corrective measures to preserve the brand's directional integrity.
   PL: Niestosowanie się do wytycznych doktryny marki może skutkować podjęciem działań naprawczych w celu zachowania spójności kierunku marki.
103. [Słowo kluczowe [NoirBindArmor] — nazwa] 르누아르 우스티드 원단
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirBindArmor].name
   kontekst: identyfikator tagu w tekstach: `[NoirBindArmor]`
   limit: do 40 znaków
   EN: Le Noir: Worsted
   PL: Le Noir: Tkanina Czesankowa
104. [Słowo kluczowe [NoirBindArmor] — opis] - 최댓값 : 15\n- 수치 5당 속도 최댓값 -1, 공격 레벨 +1, 방어 레벨 +1\n- 턴 종료시 수치 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirBindArmor].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- For every 5 Stacks, Max Speed -1, Offense Level +1, Defense Level +1\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 15\n- Za każde 5 ładunków Maks. Szybkość -1, Poziom Ataku +1, Poziom Obrony +1\n- Na koniec tury traci 1 ładunek
105. [Słowo kluczowe [NoirBindArmor] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirBindArmor].flavor
   limit: do 130 znaków
   EN: Le Noir's Worsted holds the body like armor, accentuating it beneath a firm, fixed silhouette.
   PL: Tkanina Le Noir, jak zbroja, podtrzymuje sylwetkę klienta twardym i stałym obrysem, korygując jego kształt.
106. [Słowo kluczowe [ChargeNoir] — nazwa] 보존
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeNoir].name
   kontekst: identyfikator tagu w tekstach: `[ChargeNoir]`
   limit: do 40 znaków
   EN: Preservation
   PL: Zachowanie
107. [Słowo kluczowe [ChargeNoir] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeNoir].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count
   PL: - Specjalny Ładunek\n- Maks. licznika: 20\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Siłę i Licznik Ładunku\n- Na koniec tury traci 1 Licznika
108. [Słowo kluczowe [ChargeNoir] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeNoir].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła jest sprężana, gromadzona i unieruchamiana. Czasem większej siły wymaga niedopuszczenie do zmiany niż jej wywołanie.
109. [Słowo kluczowe [ChargeRouge] — nazwa] 맥동
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeRouge].name
   kontekst: identyfikator tagu w tekstach: `[ChargeRouge]`
   limit: do 40 znaków
   EN: Pulsation
   PL: Pulsowanie
110. [Słowo kluczowe [ChargeRouge] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeRouge].desc
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Słowo kluczowe [ChargeRouge] — tekst klimatyczny] 살의 수축과 이완. 피의 흐름. 그 정도에 따라 터져나오는 힘.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ChargeRouge].flavor
   limit: do 130 znaków
   EN: Contraction and relaxation of flesh. The flow of blood. The explosive strength driven by them all.
   PL: Kurczenie i rozkurcz ciała. Przepływ krwi. Wybuchowa siła, którą wszystkie one napędzają.
112. [Słowo kluczowe [RisingMadnessRouge] — nazwa] 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessRouge]`
   limit: do 40 znaków
   EN: Sunshine
   PL: Promienie Słońca
113. [Słowo kluczowe [RisingMadnessRouge] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 자신의 맥동만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Pulsation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Pulsowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
114. [Słowo kluczowe [RisingMadnessRouge] — tekst klimatyczny] …될 수 있어.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge].flavor
   limit: do 120 znaków
   EN: You can be...
   PL: …Możesz stać się...
115. [Słowo kluczowe [RisingMadnessRouge2nd] — nazwa] 따가운 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessRouge2nd]`
   limit: do 40 znaków
   EN: Stinging Sunshine
   PL: Parzące Promienie Słońca
116. [Słowo kluczowe [RisingMadnessRouge2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 자신의 맥동만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Pulsation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Pulsowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
117. [Słowo kluczowe [RisingMadnessRouge2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].flavor
   limit: do 240 znaków
   EN: The Sunlight whispers into all that it touches, beating down all the same even as its heat grows from a prickle on the skin to unbearable, burning pain and the subject is cooked alive.
   PL: Światło słoneczne szepta do wszystkiego, czego dotyka, i opada bezlitośnie — choć jego żar narasta od mrowienia na skórze po nieznośny, parzący ból, aż dotknięty gaśnie żywcem.
118. [Słowo kluczowe [RisingMadnessNoir] — nazwa] 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessNoir]`
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Słowo kluczowe [RisingMadnessNoir] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 자신의 보존 위력만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Preservation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Zachowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
120. [Słowo kluczowe [RisingMadnessNoir] — tekst klimatyczny] …될 수 있어.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir].flavor
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Słowo kluczowe [RisingMadnessNoir2nd] — nazwa] 따가운 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessNoir2nd]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Słowo kluczowe [RisingMadnessNoir2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 자신의 보존 위력만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Preservation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Zachowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
123. [Słowo kluczowe [RisingMadnessNoir2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].flavor
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Słowo kluczowe [RougeThreeNormal] — nazwa] 부티크 신상옷
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeNormal].name
   kontekst: identyfikator tagu w tekstach: `[RougeThreeNormal]`
   limit: do 40 znaków
   EN: Boutique: New Releases
   PL: Butik: Nowa Kolekcja
125. [Słowo kluczowe [RougeThreeNormal] — opis] - 최댓값 : 20\n\n스킬 사용시 자신의 최대 체력의 1%를 소모하여, 자신의 스킬 피해량 +(소모한 체력)%
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeNormal].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n\nOn Skill Use, consume 1% of max HP on self to deal +(HP consumed) Skill damage
   PL: - Maks. ładunków: 20\n\nPrzy użyciu Umiejętności zużywa 1% swojego Maks. HP, a jego Umiejętności zadają obrażenia +(zużyte HP)
126. [Słowo kluczowe [RougeThreeNormal] — tekst klimatyczny] 따듯한 목소리를 따라가면… 새로운 시즌으로…!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeNormal].flavor
   limit: do 120 znaków
   EN: Follow the warm voice... into a new season...!
   PL: Idź za ciepłym głosem... w nowy sezon...!
127. [Słowo kluczowe [RougeThreeCocoon] — nazwa] 탈의실
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoon].name
   kontekst: identyfikator tagu w tekstach: `[RougeThreeCocoon]`
   limit: do 40 znaków
   EN: Changing Room
   PL: Przymierzalnia
128. [Słowo kluczowe [RougeThreeCocoon] — opis] - 최댓값 : 3\n- 체력 피해를 받지 않음\n- 피격 시, 아래 효과 적용 (턴당 최대 20회)\n\n· 맥동 횟수 1 얻음\n· 피해량 증가 1 얻음\n· 다음 턴에 방어 레벨 감소 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoon].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Does not take HP damage\n- When hit, apply the following effects: (20 times per turn):\n· Gain +1 Pulsation Count\n· Gain 1 Damage Up\n· Gain 1 Defense Level Down next turn
   PL: - Maks. ładunków: 3\n- Nie otrzymuje obrażeń HP\n- Przy trafieniu stosowane są następujące efekty (maks. 20 razy na turę)\n\n· Zyskuje 1 Licznika Pulsowania\n· Zyskuje 1 Wzrost Obrażeń\n· W następnej turze zyskuje 1 Spadek Poziomu Obrony
129. [Słowo kluczowe [RougeThreeCocoon] — tekst klimatyczny] 주의: 망가진 옷 다시 입는 중 입니다. 탈의실 매너는 다들 아시겠죠?
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoon].flavor
   limit: do 120 znaków
   EN: Warning: Fixing a misshapen dress. We all know the changing room manners, don't we?
   PL: Uwaga: obecnie poprawiamy zniekształconą suknię. O zasadach dobrego tonu w przymierzalni wie przecież każdy, prawda?
130. [Słowo kluczowe [RougeThreeCocoonHit] — nazwa] 핍박
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].name
   kontekst: identyfikator tagu w tekstach: `[RougeThreeCocoonHit]`
   limit: do 40 znaków
   EN: Persecution
   PL: Prześladowanie
131. [Słowo kluczowe [RougeThreeCocoonHit] — opis] - 최댓값 : 20
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].desc
   limit: do 120 znaków
   EN: - Max Stack: 20
   PL: - Maks. ładunków: 20
132. [Słowo kluczowe [RougeThreeCocoonHit] — tekst klimatyczny] 탈의실 사용 중에 건들다니… 이건 믿음에 대한 핍박…
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].flavor
   limit: do 150 znaków
   EN: Disturbing someone while they're in a changing room...? This is persecution, persecution against my faith...!
   PL: Przeszkadzać komuś w trakcie korzystania z przymierzalni...? To prześladowanie... prześladowanie mej wiary...!
133. [Słowo kluczowe [SapsareeShield] — nazwa] 먹어줘...
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeShield].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeShield]`
   limit: do 40 znaków
   EN: Please, eat me...
   PL: Zjedz mnie, proszę...
134. [Słowo kluczowe [SapsareeShield] — opis] - 수셰프가 적에게 일방 공격을 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고 원호 방어 전용 스킬 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 사용\n- 이 효과는 원호 방어로 간주되며, 원호 방어 수치를 계산할 때 합산됨\n- 턴 종료 시 소멸
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeShield].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Sous Chef is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then use Assist Defense-exclusive Skill\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- This effect counts as Assist Defense, and is counted toward calculating Assist Defense Stacks\n- Expires at Turn End
   PL: - Gdy Sous-chef ma otrzymać Atak Jednostronny od wroga, zużywa 1 ładunek, aby przekierować celowanie wroga na siebie, i używa Umiejętności zarezerwowanej dla Obrony Wsparcia\n- Jeżeli kilku sojuszników posiada Obronę Wsparcia, pierwszeństwo ma ten z najwyższą liczbą ładunków\n- Ten efekt liczy się jako Obrona Wsparcia i jest uwzględniany przy obliczaniu ładunków Obrony Wsparcia\n- Znika na koniec tury
135. [Słowo kluczowe [SapsareeYammi] — nazwa] 맛있는거 먹고 힘난다는거예요
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeYammi].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeYammi]`
   limit: do 50 znaków
   EN: Eat yummies and perk up, you hear?
   PL: Smakołyki zjedzone, siła nabyta, jasne?
136. [Słowo kluczowe [SapsareeYammi] — opis] - 최댓값 : 5\n- 수치 1당, 공격 레벨 1 증가\n- 턴 시작 시 보유한 '배고픈 거예요' 1당, 수치 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeYammi].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +1 for every Stack\n- Turn Start: Lose 1 Stack for every "Got an appetite, you hear?" on self
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 za każdy ładunek\n- Na początku tury traci 1 ładunek za każdy „Głoduję, jasne?” na sobie
137. [Słowo kluczowe [SapsareeYammi] — tekst klimatyczny] 맛에 의한 만족이 아닌 포만감에 의한 만족일 뿐.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeYammi].flavor
   limit: do 120 znaków
   EN: Not satiation from flavor, but from unrefined fullness.
   PL: Nie zadowolenie ze smaku — zadowolenie z prowizjonalnego nasycenia.
138. [Słowo kluczowe [SapsareeCooking] — nazwa] 토막난 요리재료
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeCooking].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeCooking]`
   limit: do 40 znaków
   EN: Chopped Ingredients
   PL: Pokrojone Składniki
139. [Słowo kluczowe [SapsareeCooking] — opis] - 최댓값 : 5\n- 턴 종료 시 소멸
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeCooking].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Expires at Turn End
   PL: - Maks. ładunków: 5\n- Znika na koniec tury
140. [Słowo kluczowe [SapsareeCooking] — tekst klimatyczny] 입에 넣을 수만 있도록 잘랐다. 칼질에는 어떠한 철학도, 손길도 없다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeCooking].flavor
   limit: do 190 znaków
   EN: Hacked up haphazardly with no other purpose than to fit it down the gullet. Not even an ounce of culinary philosophy or care went into each chop.
   PL: Posiekane byle jak, po to jedynie, by dało się wcisnąć w przełyk. Ani kropli filozofii kulinarnej, ani cienia staranności w każdym cięciu.
141. [Słowo kluczowe [SapsareeHungry] — nazwa] 배고픈 거예요
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeHungry].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeHungry]`
   limit: do 40 znaków
   EN: Got an appetite, you hear?
   PL: Głoduję, jasne?
142. [Słowo kluczowe [SapsareeHungry] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 가하는 피해량 +50%\n- 수셰프가 스킬 '앗! 제 식사시간인거예요' 사용 시 소멸
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeHungry].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack\n- At 3 Stacks, deal +50% damage\n- Expires when Sous Chef uses the "Aah! I'm on lunch break, you hear?" Skill
   PL: - Maks. ładunków: 3\n- Poziom Ataku +1 za każdy ładunek\n- Przy 3 ładunkach zadaje obrażenia +50%\n- Znika, gdy Sous-chef użyje Umiejętności „Ach! To czas mojego posiłku, jasne?”
143. [Słowo kluczowe [SapsareeHungry] — tekst klimatyczny] 아무거나 배에 쑤셔넣기만 하면 만족되는 허기. 그게 여기 있는 것들의 본성.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeHungry].flavor
   limit: do 130 znaków
   EN: A hunger content with anything shoved into the gut. Such is the nature of those who subsist here.
   PL: Głód zadowolony ze wszystkiego, co wciśnięto do żołądka. Taka jest natura tych, którzy tu wegetują.
144. [Słowo kluczowe [SapsareeSpices] — nazwa] 매콤매콤소스
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeSpices].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeSpices]`
   limit: do 50 znaków
   EN: Fiery, Tongue-scorching Sauce
   PL: Pikantno-Pikantny Sos
145. [Słowo kluczowe [SapsareeSpices] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeSpices].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level -1 for every Stack
   PL: - Maks. ładunków: 3\n- Poziom Ataku -1 za każdy ładunek
146. [Słowo kluczowe [SapsareeSpices] — tekst klimatyczny] 재료의 질을 감추기 위한 안일한 방법.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SapsareeSpices].flavor
   limit: do 120 znaków
   EN: A lazy cook's solution for disguising substandard ingredient quality.
   PL: Leniwy sposób na zamaskowanie kiepskiej jakości składników.
147. [Słowo kluczowe [Sapsaree_LowMorale] — nazwa] 요리갈망
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Sapsaree_LowMorale]`
   limit: do 40 znaków
   EN: Culinary Yearning
   PL: Kulinarna Tęsknota
148. [Słowo kluczowe [Sapsaree_LowMorale] — opis] - 사기 저하\n- 자신의 '배고픈 거예요' 수치 1당, 공격 레벨 1 증가, 받는 피해량 +3%
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +1 and take +3% damage for every "Got an appetite, you hear?" Stack on self
   PL: - Niskie Morale\n- Poziom Ataku +1 i otrzymuje obrażenia +3% za każdy ładunek „Głoduję, jasne?” na sobie
149. [Słowo kluczowe [Sapsaree_LowMorale] — tekst klimatyczny] 넌 요리를 하고 싶은 게 아니다. 요리를 하는 느낌과 식사를 하는 흉내를 내고 싶은 것이지.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].flavor
   limit: do 170 znaków
   EN: Don't delude yourself; you're not yearning for "culinary arts." You just want to feel like you're cooking and pretend to dine.
   PL: Nie łudź się: nie tęsknisz za „sztuką kulinarną”. Chcesz jedynie poczuć, że gotujesz, i udawać, że ucztujesz.
150. [Słowo kluczowe [Sapsaree_Panic] — nazwa] 요리갈망
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Sapsaree_Panic]`
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Słowo kluczowe [Sapsaree_Panic] — opis] - 패닉\n- 자신의 '배고픈 거예요' 수치 1당, 공격 레벨 2 증가, 받는 피해량 +5%
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +2 and take +5% damage for every "Got an appetite, you hear?" Stack on self
   PL: - Panika\n- Poziom Ataku +2 i otrzymuje obrażenia +5% za każdy ładunek „Głoduję, jasne?” na sobie
152. [Słowo kluczowe [Sapsaree_Panic] — tekst klimatyczny] 넌 요리를 하고 싶은 게 아니다. 요리를 하는 느낌과 식사를 하는 흉내를 내고 싶은 것이지.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Sapsaree_Panic].flavor
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Słowo kluczowe [HungryPeople_LowMorale] — nazwa] FOMO
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[HungryPeople_LowMorale]`
   limit: do 40 znaków
   EN: FOMO
   PL: FOMO
154. [Słowo kluczowe [HungryPeople_LowMorale] — opis] - 사기 저하\n- 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n- 취약 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +1 for every 20% missing HP on self (max 2)\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Poziom Ataku +1 za każde 20% utraconego HP (maks. 2)\n- Zyskuje 1 Wrażliwości
155. [Słowo kluczowe [HungryPeople_LowMorale] — tekst klimatyczny] 이번 유행은 놓치면 안 되는데…!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].flavor
   limit: do 120 znaków
   EN: Not again—I'm not gonna miss out on this season's trend!
   PL: Znów to samo — nie mogę przecież odpuścić tegorocznego trendu!
156. [Słowo kluczowe [HungryPeople_Panic] — nazwa] FOMO
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_Panic].name
   kontekst: identyfikator tagu w tekstach: `[HungryPeople_Panic]`
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Słowo kluczowe [HungryPeople_Panic] — opis] - 패닉\n- 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n- 취약 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +1 for every 20% missing HP on self (max 2)\n- Gain 1 Fragile
   PL: - Panika\n- Poziom Ataku +1 za każde 20% utraconego HP (maks. 2)\n- Zyskuje 1 Wrażliwości
158. [Słowo kluczowe [HungryPeople_Panic] — tekst klimatyczny] 이번 유행은 놓치면 안 되는데…!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HungryPeople_Panic].flavor
   (powtórzenie elementu 155 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Słowo kluczowe [UnresolvedFeelings] — nazwa] 다층 레이어 패치워크
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=UnresolvedFeelings].name
   kontekst: identyfikator tagu w tekstach: `[UnresolvedFeelings]`
   limit: do 40 znaków
   EN: Layered Patchwork
   PL: Warstwowy Patchwork
160. [Słowo kluczowe [UnresolvedFeelings] — opis] - 최댓값 : 30\n- 수치만큼 방어 레벨 증가\n- 경청에 대한 감사를 보유한 대상에게 피격 시 경청에 대한 감사 수치만큼 감소 (인격 별로 턴당 2회)\n- '들어줘서… 고맙다…' 스킬 합 패배 시 5 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=UnresolvedFeelings].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Gain Defense Level equal to Stack\n- When hit by target that has "Gratitude for Listening", lose Stack equal to "Gratitude for Listening" (2 times per turn per Identity)\n- On Clash Lose using the "Thank you... for listening..." Skill, lose 5 Stacks
   PL: - Maks. ładunków: 30\n- Zyskuje Poziom Obrony równy liczbie ładunków\n- Przy trafieniu przez cel posiadający „Wdzięczność za Wysłuchanie” traci ładunki w liczbie jego ładunków (2 razy na turę na Tożsamość)\n- Po przegranej w Starciu Umiejętnością „Dziękuję... za wysłuchanie...” traci 5 ładunków
161. [Słowo kluczowe [UnresolvedFeelings] — tekst klimatyczny] 정작 자신은 이렇게 두꺼운 이불 속에 있는 채로 소리를 듣지 않는다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=UnresolvedFeelings].flavor
   limit: do 130 znaków
   EN: Ironically, it has deafened itself to any voice by hiding under wraps upon wraps of thick blankets.
   PL: Ironicznie ogłuchło na każdy głos, zakopawszy się pod warstwami grubych koców.
162. [Słowo kluczowe [Wariness] — nazwa] 경계심
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Wariness].name
   kontekst: identyfikator tagu w tekstach: `[Wariness]`
   limit: do 40 znaków
   EN: Guarded Caution
   PL: Czujność
163. [Słowo kluczowe [Wariness] — opis] - 최댓값 : 10\n- 수치만큼 공격 레벨 감소, 방어 레벨 감소\n- 이 캐릭터가 합 패배 시, 3 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Wariness].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Lose Offense Level and Defense Level equal to Stack\n- If this unit loses a Clash, lose 3 Stacks
   PL: - Maks. ładunków: 10\n- Traci Poziom Ataku i Poziom Obrony równy liczbie ładunków\n- Po przegranej tej jednostki w Starciu traci 3 ładunków
164. [Słowo kluczowe [Wariness] — tekst klimatyczny] 처음 듣는 목소리라서 경계하는 게 아니다. 마음을 두드리려 하기에 경계하게 되는 것이다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Wariness].flavor
   limit: do 150 znaków
   EN: The unfamiliarity of the Voice is not what makes one wary; it is the Voice knocking on the heart that does so.
   PL: Nie obcość Głosu budzi czujność — czujność budzi Głos pukający do serca.
165. [Słowo kluczowe [ReliefSense] — nazwa] 경청에 대한 감사
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ReliefSense].name
   kontekst: identyfikator tagu w tekstach: `[ReliefSense]`
   limit: do 40 znaków
   EN: Gratitude for Listening
   PL: Wdzięczność za Wysłuchanie
166. [Słowo kluczowe [ReliefSense] — opis] - 최댓값 : 3\n- 턴 시작 시 수치 1 증가하고 정신력 10 회복\n- 이 스테이지의 보스에게 스킬로 피해를 입힐 때, 피해량 +(수치 x 50)%. 이후 해당 스킬 공격 종료 시 소멸\n- 수치가 3이면, 다층 레이어 패치워크의 방어 레벨 효과를 무시하고 피해를 입힘
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ReliefSense].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Gain 1 Stack and heal 10 SP\n- Skills against this Stage's boss deal +(Stack x 50)% damage; then, this effect expires on Attack End of the Skill used\n- At 3 Stacks, damage dealt by this unit disregards Layered Patchwork's Defense Level effects
   PL: - Maks. ładunków: 3\n- Na początku tury zyskuje 1 ładunek i odzyskuje 10 Poczytalności\n- Umiejętności zadające obrażenia bossowi tego etapu zadają obrażenia +(ładunki x 50)%; po zakończeniu ataku tej Umiejętności efekt znika\n- Przy 3 ładunkach zadawane obrażenia ignorują efekt Poziomu Obrony „Warstwowego Patchworku”
167. [Słowo kluczowe [ReliefSense] — tekst klimatyczny] 들어줘서… 고마워…
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=ReliefSense].flavor
   limit: do 120 znaków
   EN: Thank you... for listening...
   PL: Dziękuję... za wysłuchanie...
168. [Słowo kluczowe [HorribleTerror] — nazwa] 끔찍한 반복 재생
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleTerror].name
   kontekst: identyfikator tagu w tekstach: `[HorribleTerror]`
   limit: do 40 znaków
   EN: Horribly Infinite Replay
   PL: Przerażające Nieskończone Odtwarzanie
169. [Słowo kluczowe [HorribleTerror] — opis] - 최댓값 : 1\n- 턴 시작 시 E.G.O 침식 상태면, 이번 턴 동안 모든 대상에게 가하는 피해량 -50%\n- 턴 종료 시, 현재 체력의 50%만큼 체력 피해를 받고 소멸 (소수점 버림, 이 효과로 흐트러지지 않음)
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleTerror].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn Start: If this unit is in E.G.O Corrosion state, deal -50% damage to all targets this turn\n- Turn End: This unit takes 50% HP damage; then, this effect expires (rounded down, this effect cannot Stagger this unit)
   PL: - Maks. ładunków: 1\n- Na początku tury, jeżeli jednostka jest w stanie Korozji E.G.O, zadaje wszystkim celom obrażenia -50% w tej turze\n- Na koniec tury otrzymuje obrażenia HP w wysokości 50% obecnego HP i znika (zaokrąglane w dół; ten efekt nie oszołamia jednostki)
170. [Słowo kluczowe [HorribleTerror] — tekst klimatyczny] 들을 때까지… 백화점 방송을 제대로 들을 때까지… 계속… 계속… 들어라…
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleTerror].flavor
   limit: do 140 znaków
   EN: Until you listen... until you truly hear the Grand Magasin's announcement... again... and again... listen...
   PL: Dopóki nie posłuchasz... dopóki naprawdę nie usłyszysz komunikatu Grand Magasin... jeszcze raz... i jeszcze raz... słuchaj...
171. [Słowo kluczowe [HorribleEat] — nazwa] 반복 재생 반복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleEat].name
   kontekst: identyfikator tagu w tekstach: `[HorribleEat]`
   limit: do 40 znaków
   EN: Repeat on Repeat
   PL: Powtarzanie Powtórzeń
172. [Słowo kluczowe [HorribleEat] — opis] - 최댓값 : 15\n- 수치만큼 공격 레벨 증가
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleEat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- Gain Offense Level equal to Stack
   PL: - Maks. ładunków: 15\n- Zyskuje Poziom Ataku równy liczbie ładunków
173. [Słowo kluczowe [HorribleEat] — tekst klimatyczny] 모두가 들을 때까지 반복되는 방송은 메아리가 되고, 메아리는 또 다시 반복되고 공명한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HorribleEat].flavor
   limit: do 160 znaków
   EN: The broadcast is repeated until everyone hears it. It becomes an echo, and the echo repeats in turn until it resonates.
   PL: Komunikat powtarza się, dopóki nie usłyszy go każdy. Staje się echem, a echo z kolei powtarza się, aż dźwięk rezonuje.
174. [Słowo kluczowe [NoirSuit] — nazwa] 르누아르 개버딘 원단 코트
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirSuit].name
   kontekst: identyfikator tagu w tekstach: `[NoirSuit]`
   limit: do 40 znaków
   EN: Le Noir: Gabardine Overcoat
   PL: Le Noir: Płaszcz Gabardynowy
175. [Słowo kluczowe [NoirSuit] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 방어 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬, 패시브 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 30, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 보호막이 있는 상태에서 피격 시, 2 증가 (턴당 최대 20)\n- 턴 종료 시 보호막이 남아있으면, 10 증가\n- 수치가 100이 되면, 다음 턴에 아르뮈르 에비이예로 변경됨
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirSuit].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Defense Level Up for every 20 Stacks (max 4)\n- Gain Stack equal to Preservation Count this unit consumes or gains due to its Skill or Passive effects (max 30 per turn; this effect's Stack is gained regardless of Preservation's max Count)\n- When hit while this unit has Shield, gain 2 Stacks (20 per turn)\n- Turn End: If this unit has Shield, gain 10 Stacks\n- At 100 Stacks, convert this effect into "Armure Éveillée" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Obrony za każde 20 ładunków (maks. 4)\n- Gdy przez Umiejętności lub umiejętności pasywne zużyje albo zyska Licznik Zachowania, zyskuje ładunki w tej liczbie (maks. 30 na turę, łącznie z liczbą ponad Maks. licznika Zachowania)\n- Przy trafieniu, gdy posiada Tarczę, zyskuje 2 ładunki (maks. 20 na turę)\n- Na koniec tury, jeżeli nadal posiada Tarczę, zyskuje 10 ładunków\n- Przy 100 ładunkach w następnej turze zamienia się w „Armure Éveillée”
176. [Słowo kluczowe [NoirSuit] — tekst klimatyczny] 경사가 위사보다 훨씬 많도록 트윌하여 만든 코트.\n특유의 높은 밀도로 착용자를 외부로부터 보호한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NoirSuit].flavor
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An overcoat made from twill fabric, a type of weave made by threading several weft threads over fewer warp threads.\nIts characteristic high-density weave protects its wearer from external trauma.
   PL: Płaszcz z tkaniny skośnej, utkanej tak, by osnowy było znacznie więcej niż wątku.\nGęsty, charakterystyczny splot chroni noszącego przed urazami z zewnątrz.
177. [Słowo kluczowe [Realisation] — nazwa] 아르뮈르 에비이예
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Realisation].name
   kontekst: identyfikator tagu w tekstach: `[Realisation]`
   limit: do 40 znaków
   EN: Armure Éveillée
   PL: Armure Éveillée
178. [Słowo kluczowe [Realisation] — opis] - 최댓값 : 100\n- 턴 시작시 수치 10당 정신력 5 회복\n- 턴 시작시 수치 20당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 기본 공격 스킬이 파괴 불가 코인으로 변경됨\n- 변경된 이후 다음 턴부터 턴 종료 시, 10 감소\n- 수치가 0이 되면, 르누아르 개버딘 원단 코트로 변경됨
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Realisation].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Heal 5 SP for every 10 Stacks\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 each)\n- Convert all Base Attack Skill Coins into Unbreakable Coins\n- After this effect is converted, starting from the end of the next turn, lose 10 Stacks\n- At 0 Stacks, convert this effect into "Le Noir: Gabardine Overcoat"
   PL: - Maks. ładunków: 100\n- Na początku tury odzyskuje 5 Poczytalności za każde 10 ładunków\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności ataku podstawowego stają się Niezniszczalnymi Monetami\n- Począwszy od końca tury następnej po zamianie, traci na koniec tury 10 ładunków\n- Przy 0 ładunków zamienia się z powrotem w „Le Noir: Płaszcz Gabardynowy”
179. [Słowo kluczowe [Realisation] — tekst klimatyczny] 외부에서 가해진 힘이 착용자에게 도달하지 못하게 한 르누아르의 원단은, 최종적으로 외부로부터의 변화를 제거하기 위해 깨어난다.\n축적한 에너지를 방출하여 외부 요인을 제거하는 방향으로 작동한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Realisation].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Le Noir's fabric weave prevents external force from reaching its wearer. The purpose for which it awakens is to eliminate change imposed from the outside.\nThe fabric stores energy from attacks it absorbs, then expels all that force in a single burst to remove the external source of change.
   PL: Tkanina Le Noir, która nie pozwoliła zewnętrznej sile dotrzeć do noszącego, ostatecznie wybudza się, by usunąć zmiany narzucone z zewnątrz.\nGromadzoną z pochłoniętych ataków energię uwalnia jednym wybuchem, eliminując zewnętrzne źródło zmiany.
180. [Słowo kluczowe [LaRouge_LowMorale] — nazwa] 가죽 밖으로!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LaRouge_LowMorale]`
   limit: do 40 znaków
   EN: Leave the Leather Behind!
   PL: Skóra na Zewnątrz!
181. [Słowo kluczowe [LaRouge_LowMorale] — opis] - 사기 저하\n방어 레벨 -3\n공격 레벨 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -3\n- Offense Level +1
   PL: - Niskie Morale\nPoziom Obrony -3\nPoziom Ataku +1
182. [Słowo kluczowe [LaRouge_LowMorale] — tekst klimatyczny] 급한 마음에 튀어나가려는 몸의 내용물들이 피부를 뚫고 나올 지경이다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_LowMorale].flavor
   limit: do 160 znaków
   EN: Organs that ought to stay inside are wriggling in impatient excitement, trying to break through the skin to the other side.
   PL: Narządy, którym przystało zostawać w środku, dygoczą niecierpliwie, próbując przebić się przez skórę na drugą stronę.
183. [Słowo kluczowe [LaRouge_Panic] — nazwa] 가죽 밖으로!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LaRouge_Panic]`
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Słowo kluczowe [LaRouge_Panic] — opis] - 패닉\n방어 레벨 -5\n공격 레벨 +2
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5\n- Offense Level +2
   PL: - Panika\nPoziom Obrony -5\nPoziom Ataku +2
185. [Słowo kluczowe [LaRouge_Panic] — tekst klimatyczny] 급한 마음에 튀어나가려는 몸의 내용물들이 피부를 뚫고 나올 지경이다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaRouge_Panic].flavor
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Słowo kluczowe [LaNoir_LowMorale] — nazwa] 껍질 속으로…
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LaNoir_LowMorale]`
   limit: do 40 znaków
   EN: Back into My Shell...
   PL: Z powrotem do Skorupy...
187. [Słowo kluczowe [LaNoir_LowMorale] — opis] - 사기 저하\n속도 최댓값 -1\n방어 레벨 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Max Speed -1\n- Defense Level +1
   PL: - Niskie Morale\nMaks. Szybkość -1\nPoziom Obrony +1
188. [Słowo kluczowe [LaNoir_LowMorale] — tekst klimatyczny] 이대로 단단하게 속으로, 안으로 움츠러든다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_LowMorale].flavor
   limit: do 120 znaków
   EN: Curl inward. Deeper. Tighter. Let the shell harden around what remains.
   PL: Zwinąć się do wewnątrz. Głębiej. Ciasniej. Niech skorupa stwardnieje wokół tego, co zostało.
189. [Słowo kluczowe [LaNoir_Panic] — nazwa] 껍질 속으로…
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LaNoir_Panic]`
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Słowo kluczowe [LaNoir_Panic] — opis] - 패닉\n속도 최댓값 -5\n방어 레벨 +3
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Max Speed -5\n- Defense Level +3
   PL: - Panika\nMaks. Szybkość -5\nPoziom Obrony +3
191. [Słowo kluczowe [LaNoir_Panic] — tekst klimatyczny] 이대로 단단하게 속으로, 안으로 움츠러든다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=LaNoir_Panic].flavor
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Słowo kluczowe [NiddlePinned] — nazwa] 박제 상태
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddlePinned].name
   kontekst: identyfikator tagu w tekstach: `[NiddlePinned]`
   limit: do 40 znaków
   EN: Taxidermized
   PL: Zataksydermizowany
193. [Słowo kluczowe [NiddlePinned] — opis] - 최댓값 : 2\n\n- 피격시, 출혈 횟수 1 증가 (턴당 3회)\n- 이 효과를 보유한 동안, 행동 불가 상태가 됨\n\n- 턴 종료시 체력 피해 15를 받고 자신의 바늘못 5 감소\n- 턴 종료시 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddlePinned].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n\n- When hit, gain +1 Bleed Count (3 times per turn)\n- Becomes Immobilized while this unit has this effect\n\n- Turn End: Lose 15 HP and 5 Naildle on self\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 2\n\n- Przy trafieniu zyskuje 1 Licznika Krwawienia (3 razy na turę)\n- Dopóki posiada ten efekt, pozostaje w stanie Unieruchomienia\n\n- Na koniec tury otrzymuje 15 obrażeń HP i traci 5 Igłogwoźdź\n- Na koniec tury traci 1 ładunek
194. [Słowo kluczowe [NiddlePinned] — tekst klimatyczny] 원하는대로….핸드메이드! 비스포크! 핸드쏜!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddlePinned].flavor
   limit: do 120 znaków
   EN: As you wish... Hand-made! Bespoke! Hand-sown!
   PL: Zgodnie z życzeniem... Ręcznie robione! Na miarę! Ręcznie szyte!
195. [Słowo kluczowe [NiddleExpected] — nazwa] 혀에 꽂힌 바늘
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddleExpected].name
   kontekst: identyfikator tagu w tekstach: `[NiddleExpected]`
   limit: do 40 znaków
   EN: Tongue-pinning Needle
   PL: Igła Zakłuta w Języku
196. [Słowo kluczowe [NiddleExpected] — opis] - 수비 스킬 장착시\n  - 자신의 바늘못 1 감소\n  - 이 효과 소멸\n\n- 턴 종료시, 바늘못 3을 얻고 이 효과 소멸
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddleExpected].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit equipped Defense Skills:\n· Lose 1 Naildle on self\n· This effect expires\n\n- Turn End: Gain 3 Naildle; then, this effect expires
   PL: - Jeżeli wyposażono Umiejętności obrony:\n· Traci 1 własnych Igłogwoźdź\n· Ten efekt znika\n\n- Na koniec tury zyskuje 3 Igłogwoźdź; po czym ten efekt znika
197. [Słowo kluczowe [NiddleExpected] — tekst klimatyczny] 박힌 못을 빼기 위해서 잠시 멈춰야한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddleExpected].flavor
   limit: do 120 znaków
   EN: To remove a fixed nail, one must first come to a brief halt.
   PL: Aby wybić wbity gwóźdź, najpierw trzeba na chwilę przystanąć.
198. [Słowo kluczowe [HowlingCocoon] — nazwa] 고치의 울음소리 - 미약
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoon].name
   kontekst: identyfikator tagu w tekstach: `[HowlingCocoon]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Frail
   PL: Płacz Kokonu – Wątły
199. [Słowo kluczowe [HowlingCocoon] — opis] - 가끔씩 고치의 울음소리가 들린다.\n- 스킬 최종 위력 +2
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Cocoon is crying intermittently.\n- Skill Final Power +2
   PL: - Kokon odzywa się płaczem co jakiś czas.\n- Moc Końcowa Umiejętności +2
200. [Słowo kluczowe [HowlingCocoon] — tekst klimatyczny] 맞는 정보와 틀린 정보를 뒤섞어 말하는 자들은 되려 무지에서 비롯되어 당당하고 그래서 오히려 그 말들을 무시하기 어렵다고한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoon].flavor
   limit: do 170 znaków
   EN: Those who speak in half-truths and misinformation source their confidence from ignorance, which is what makes them so convincing.
   PL: Ci, którzy mówią półprawdami i dezinformacją, czerpią pewność siebie z niewiedzy — i właśnie to czyni ich tak przekonującymi.
201. [Słowo kluczowe [HowlingCocoonTwo] — nazwa] 고치의 울음소리 - 악성
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoonTwo].name
   kontekst: identyfikator tagu w tekstach: `[HowlingCocoonTwo]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Vicious
   PL: Płacz Kokonu – Złośliwy
202. [Słowo kluczowe [HowlingCocoonTwo] — opis] - 고치의 울음소리가 멈추지 않는다.\n- 스킬 최종 위력 +3
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoonTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Cocoon does not cease its cries.\n- Skill Final Power +3
   PL: - Płacz Kokonu nie ustaje.\n- Moc Końcowa Umiejętności +3
203. [Słowo kluczowe [HowlingCocoonTwo] — tekst klimatyczny] 리지드랑… 셀비지는… 서로 관계없는거라고…. 으드득… 일부러! 일부러! 알고 그러는거지!!!
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=HowlingCocoonTwo].flavor
   limit: do 200 znaków
   EN: Rigid denim... and selvage... have jack to do with each other... Gnnnngh... You know this! You're just tryin' to piss me off, aren't you?! I knew it!!!
   PL: Sztywny dżins... i selvage... nie mają ze sobą nic wspólnego, mówię ci.... Wrrr... Celowo! Celowo! Ty to robisz specjalnie, nie?!!!
204. [Słowo kluczowe [MeursaultBuffet] — nazwa] 못 박는 자
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=MeursaultBuffet].name
   kontekst: identyfikator tagu w tekstach: `[MeursaultBuffet]`
   limit: do 40 znaków
   EN: He Who Nails
   PL: Ten, Który Przybija
205. [Słowo kluczowe [MeursaultBuffet] — opis] - 이번 전투에서 자신의 스킬 사용 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 2회)\n- 턴 시작 시 전장에 다른 아군이 있으면, 이번 턴에 피해로 사망하지 않음\n- 퇴각 불가능
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=MeursaultBuffet].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In this Encounter, if this unit uses its Skill, gain 2 E.G.O Resource of the corresponding Affinity (2 times per turn)\n- Turn Start: If another ally is on the field, damage taken by this unit does not kill this unit this turn\n- Cannot Retreat
   PL: - W tej walce przy użyciu Umiejętności dodatkowo zyskuje 2 Zasoby E.G.O odpowiedniego Grzechu (2 razy na turę)\n- Na początku tury, jeżeli na polu bitwy jest inny sojusznik, obrażenia nie pozbawiają go życia w tej turze\n- Nie może się wycofać
206. [Słowo kluczowe [MeursaultBuffet] — tekst klimatyczny] 황금못을 쥐고 요람을 찢었고 신을 못 박는다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=MeursaultBuffet].flavor
   limit: do 120 znaków
   EN: Gripping the Golden Nail, he has rent the Cradle open and now nails a god upon a point.
   PL: Ściskając Złoty Gwóźdź, rozdarł Kołyskę — a teraz przybija boga jednym gwoździem.
207. [Słowo kluczowe [Nutrition] — nazwa] 탈취해낸 무언가.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Nutrition].name
   kontekst: identyfikator tagu w tekstach: `[Nutrition]`
   limit: do 40 znaków
   EN: A Seized Something.
   PL: Coś Skonfiskowane.
208. [Słowo kluczowe [Nutrition] — opis] - 최댓값 : 5\n- 턴 종료 시 다음 턴에 (수치 x 2)만큼 자신의 맥동 횟수가 증가하고 소멸\n- 소멸 시 수치가 최댓값이면, 다음 턴에 본체 최대 체력의 3%만큼 모든 부위가 보호막 얻음 (이 효과로 획득한 보호막은 턴 종료시에도 사라지지 않음)
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Nutrition].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: Gain +(Stack x 2) Pulsation Count next turn; then, this effect expires\n- If this effect is at max Stack when expiring, all Parts gain Shield equal to 3% of the Core's HP next turn (Shield gained due to this effect does not expire at Turn End)
   PL: - Maks. ładunków: 5\n- Na koniec tury w następnej turze zyskuje Licznik Pulsowania +(ładunki x 2), po czym znika\n- Jeżeli przy znikaniu ma Maks. ładunków, w następnej turze wszystkie Części zyskują Tarczę równą 3% Maks. HP Rdzenia (Tarcza z tego efektu nie znika na koniec tury)
209. [Słowo kluczowe [Nutrition] — tekst klimatyczny] 상대가 가진 좋아보이는 모든 것은 본래 자신의 것이어야만 하기에, 이것은 탈취가 아닌 정당한 회수일 뿐.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Nutrition].flavor
   limit: do 180 znaków
   EN: Everything desirable in another's possession should have belonged to me from the start. This is not theft, then, but rightful repossession.
   PL: Wszystko pożądane, co tkwi w cudzych rękach, od początku powinno należeć do mnie. To nie kradzież — to jedynie słuszne odzyskanie.
210. [Słowo kluczowe [Gourmandise] — nazwa] 폭주
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Gourmandise].name
   kontekst: identyfikator tagu w tekstach: `[Gourmandise]`
   limit: do 40 znaków
   EN: Uncontrollable Rampage
   PL: Niepowstrzymana Furia
211. [Słowo kluczowe [Gourmandise] — opis] - 기본값 : 3\n- 자신의 출혈 3당, 가하는 피해량 +5% (최대 30%)\n- 모든 부위가 흐트러짐 상태가 되지 않으며, 출혈로 받는 피해량 -75%\n- 턴 종료 시 1 감소\n- 효과가 소멸할 때 맥동 횟수를 모두 소모
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Gourmandise].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Deal +5% damage for every 3 Bleed on self (max 30%)\n- All Parts cannot be Staggered; take -75% damage from Bleed\n- Turn End: Lose 1 Stack\n- Consume all Pulsation Count when this effect expires
   PL: - Wartość początkowa: 3\n- Zadaje obrażenia +5% za każde 3 własne Krwawienia (maks. 30%)\n- Żadna Część nie może ulec Oszołomieniu; otrzymuje -75% obrażeń od Krwawienia\n- Na koniec tury traci 1 ładunek\n- Gdy efekt znika, zużywa cały Licznik Pulsowania
212. [Słowo kluczowe [Gourmandise] — tekst klimatyczny] 파편화된 육체 기관마다 갈기갈기 찢겨 나갈듯 뛰쳐나가려 한다. 주체할 수 없는 폭주는 되레 몸이 하나가 되게 한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=Gourmandise].flavor
   limit: do 200 znaków
   EN: Every disparate fragment of its anatomy jerks and convulses, trying to rip itself away. Such uncontrollable rampage brings the body together, ironically.
   PL: Każdy rozdrobniony okruch ciała szarpie się i konwulsyjnie wyrywa, pragnąc oderwać się od reszty. Ironicznie to właśnie taka niepowstrzymana furia skleja ciało w całość.
213. [Słowo kluczowe [BuffetSick] — nazwa] 고통 주머니
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetSick].name
   kontekst: identyfikator tagu w tekstach: `[BuffetSick]`
   limit: do 40 znaków
   EN: Sac of Suffering
   PL: Worek Cierpienia
214. [Słowo kluczowe [BuffetSick] — opis] - 최댓값 : 30\n- 턴 종료 시 폭주 효과가 소멸할 때 함께 소멸하며, 다음 턴에 수치 5당 취약 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetSick].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn End: This effect expires when Uncontrollable Rampage effect expires. Then, this unit gains 1 Fragile next turn for every 5 Stacks
   PL: - Maks. ładunków: 30\n- Na koniec tury znika razem z efektem Niepowstrzymanej Furii; w następnej turze zyskuje 1 Wrażliwości za każde 5 ładunków
215. [Słowo kluczowe [BuffetSick] — tekst klimatyczny] 아픔은 모두 여기에 모인다. 따라서 이 기관이 터질 때 아픔은 더 오롯해진다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetSick].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This organ is the terminus of all painful sensory inputs.\nWhen it bursts, it will drown out all reason and reveal pain in its most unalloyed form.
   PL: Cały ból gromadzi się właśnie tutaj. Dlatego gdy ten organ pęka, ból ukazuje się w czystej, niezłomnej postaci.
216. [Słowo kluczowe [SavePlacenta] — nazwa] 자기 보호
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SavePlacenta].name
   kontekst: identyfikator tagu w tekstach: `[SavePlacenta]`
   limit: do 40 znaków
   EN: Self-preservation
   PL: Samozachowanie
217. [Słowo kluczowe [SavePlacenta] — opis] - 생명줄이 적에게 일방 공격을 당할 때, 수치를 1 소모하여 적의 공격 대상을 몸통으로 변경하고 원호 방어 전용 스킬 사용\n- 턴 종료 시 소멸
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SavePlacenta].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Lifecord is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to the Body; then, use Assist Defense-exclusive Skill\n- Turn End: This effect expires
   PL: - Gdy Linka Życia ma otrzymać Atak Jednostronny od wroga, zużywa 1 ładunek, aby przekierować celowanie wroga na Tułów, i używa Umiejętności zarezerwowanej dla Obrony Wsparcia\n- Znika na koniec tury
218. [Słowo kluczowe [BloodyMucus] — nazwa] 세례[적]
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BloodyMucus].name
   kontekst: identyfikator tagu w tekstach: `[BloodyMucus]`
   limit: do 40 znaków
   EN: Baptism [Crimson]
   PL: Chrzest [Czerwień]
219. [Słowo kluczowe [BloodyMucus] — opis] - 최댓값 : 5\n- 자신의 출혈 위력 3당, 공격 레벨 1 증가 (최대 3)\n- 수치가 최댓값이면, 출혈 피해를 2배로 받으며 출혈 피해로 인해 사망하지 않음\n- 기본 공격 스킬 사용 시, (수치x2)만큼 자신의 출혈 횟수 증가\n- E.G.O 스킬 혹은 수비 스킬 사용 시, 수치 3 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BloodyMucus].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Effect: 5\n- Offense Level +1 for every 3 Bleed Potency on self (max 3)\n- At max Stack, double the amount of damage taken from Bleed; this unit cannot be defeated due to Bleed damage\n- On Base Attack Skill Use, gain +(Stack x 2) Bleed Count\n- On E.G.O Skill or Defense Skill Use, lose 3 Stacks
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 za każde 3 Siły Krwawienia na sobie (maks. 3)\n- Przy Maks. ładunków otrzymuje podwójne obrażenia od Krwawienia, ale nie może zginąć od obrażeń Krwawienia\n- Przy użyciu Umiejętności ataku podstawowego zyskuje Licznik Krwawienia +(ładunki x 2)\n- Przy użyciu Umiejętności E.G.O lub Umiejętności obrony traci 3 ładunków
220. [Słowo kluczowe [BloodyMucus] — tekst klimatyczny] ‘피로 살을 씻어내라’
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BloodyMucus].flavor
   limit: do 120 znaków
   EN: "Let blood baptize the flesh"
   PL: „Niech krew obmyje ciało”
221. [Słowo kluczowe [DeterioratingBody] — nazwa] 생의 본능
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=DeterioratingBody].name
   kontekst: identyfikator tagu w tekstach: `[DeterioratingBody]`
   limit: do 40 znaków
   EN: Instinctive Cling to Life
   PL: Instynkt Życia
222. [Słowo kluczowe [DeterioratingBody] — opis] - 최댓값 : 5\n- 체력이 1 미만으로 감소하지 않음\n- 피격 시 1 감소 (스킬당 2회)\n- 턴 종료 시 1 감소. 효과가 소멸하면 사망
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=DeterioratingBody].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- HP does not drop below 1\n- When hit, lose 1 Stack (2 times per Skill)\n- Turn End: Lose 1 Stack; this unit is defeated when this effect expires
   PL: - Maks. ładunków: 5\n- HP nie spada poniżej 1\n- Przy trafieniu traci 1 ładunek (2 razy na Umiejętność)\n- Na koniec tury traci 1 ładunek; gdy efekt znika, jednostka ginie
223. [Słowo kluczowe [DeterioratingBody] — tekst klimatyczny] 살고자 발악하는 그 모습은 끈질기지만, 결국 끝은 있다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=DeterioratingBody].flavor
   limit: do 140 znaków
   EN: Its instinct to cling to life is tenacious indeed, but in the end, the time comes when one must let go.
   PL: Ten zawzięty, ostatni instynkt przetrwania jest nieugięty — lecz i on ma swój kres.
224. [Słowo kluczowe [BuffetFailed] — nazwa] 탈진
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetFailed].name
   kontekst: identyfikator tagu w tekstach: `[BuffetFailed]`
   limit: do 40 znaków
   EN: Exhausted
   PL: Wyczerpany
225. [Słowo kluczowe [BuffetFailed] — opis] - 최댓값 : 3\n- 수치 1당, 속도 최솟값 -1, 최댓값 -1\n- 턴 시작 시 취약 1 얻음\n- 턴 종료 시 1 감소\n(모든 부위에 적용)
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetFailed].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Min & Max Speed -1 for every Stack\n- Turn Start: Gain 1 Fragile\n- Turn End: Lose 1 Stack\n(Applies on all Parts)
   PL: - Maks. ładunków: 3\n- Min. i Maks. Szybkość -1 za każdy ładunek\n- Na początku tury zyskuje 1 Wrażliwości\n- Na koniec tury traci 1 ładunek\n(Na wszystkie Części)
226. [Słowo kluczowe [BuffetFailed] — tekst klimatyczny] 폭주 후에 찾아오는 제약. 힘의 속도와 크기에 따라 세계는 저마다의 형태로 대가를 치르게 한다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=BuffetFailed].flavor
   limit: do 170 znaków
   EN: Every outburst is followed by limitation. The world levies payment in forms proportionate to force and velocity of the outburst.
   PL: Po każdym wybuchu przychodzi ograniczenie. Świat wymaga zapłaty w formie proporcjonalnej do siły i prędkości wybuchu.
227. [Słowo kluczowe [EarlyBuffet_LowMorale] — nazwa] 분열
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[EarlyBuffet_LowMorale]`
   limit: do 40 znaków
   EN: Inner Schism
   PL: Wewnętrzny Rozłam
228. [Słowo kluczowe [EarlyBuffet_LowMorale] — opis] - 사기 저하\n- 방어 레벨 -3\n- 공격 레벨 +3\n- 세례[적]을 5 보유한 대상과 합 진행 시, 합 위력 +2
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -3\n- Offense Level +3\n- In a Clash against targets that have 5 Baptism [Crimson], Clash Power +2
   PL: - Niskie Morale\n- Poziom Obrony -3\n- Poziom Ataku +3\n- Podczas Starcia z celem posiadającym 5 „Chrzest [Czerwień]” Moc Starcia +2
229. [Słowo kluczowe [EarlyBuffet_LowMorale] — tekst klimatyczny] 대체…왜? 나는 어떻게 생겼어? 나는… 뭐야?
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].flavor
   limit: do 120 znaków
   EN: Why... ? How did I... come to exist? What... am I?
   PL: Czemu...? Jak to się stało, że... istnieję? Czym... ja jestem?
230. [Słowo kluczowe [EarlyBuffet_Panic] — nazwa] 분열
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].name
   kontekst: identyfikator tagu w tekstach: `[EarlyBuffet_Panic]`
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Słowo kluczowe [EarlyBuffet_Panic] — opis] - 패닉\n- 방어 레벨 -5\n- 공격 레벨 +3\n- 가하는 피해량 +10%\n- 세례[적]을 3 이상 보유한 대상과 합 진행 시, 합 위력 +3
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5\n- Offense Level +3\n- Deal +10% damage\n- In a Clash against targets that have 3+ Baptism [Crimson], Clash Power +3
   PL: - Panika\n- Poziom Obrony -5\n- Poziom Ataku +3\n- Zadaje obrażenia +10%\n- Podczas Starcia z celem posiadającym 3 lub więcej „Chrzest [Czerwień]” Moc Starcia +3
232. [Słowo kluczowe [EarlyBuffet_Panic] — tekst klimatyczny] 대체…왜? 나는 어떻게 생겼어? 나는… 뭐야?
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].flavor
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Słowo kluczowe [SisyphusTopaz] — nazwa] 토파즈
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusTopaz].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusTopaz]`
   limit: do 40 znaków
   EN: Topaz
   PL: Topaz
234. [Słowo kluczowe [SisyphusTopaz] — opis] - 효과 없음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusTopaz].desc
   limit: do 120 znaków
   EN: - No effect
   PL: - Brak efektu
235. [Słowo kluczowe [SisyphusAmethyst] — nazwa] 아메시스트
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusAmethyst].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusAmethyst]`
   limit: do 40 znaków
   EN: Amethyst
   PL: Ametyst
236. [Słowo kluczowe [SisyphusAmethyst] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusAmethyst].desc
   limit: do 120 znaków
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
237. [Słowo kluczowe [SisyphusAmber] — nazwa] 앰버
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusAmber].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusAmber]`
   limit: do 40 znaków
   EN: Amber
   PL: Bursztyn
238. [Słowo kluczowe [SisyphusAmber] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusAmber].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu
239. [Słowo kluczowe [SisyphusEmerald] — nazwa] 에메랄드
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusEmerald].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusEmerald]`
   limit: do 40 znaków
   EN: Emerald
   PL: Szmaragd
240. [Słowo kluczowe [SisyphusEmerald] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusEmerald].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)
241. [Słowo kluczowe [SisyphusGold] — nazwa] 골드
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusGold].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusGold]`
   limit: do 40 znaków
   EN: Gold
   PL: Złoto
242. [Słowo kluczowe [SisyphusGold] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusGold].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1
243. [Słowo kluczowe [SisyphusRuby] — nazwa] 루비
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusRuby].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusRuby]`
   limit: do 40 znaków
   EN: Ruby
   PL: Rubin
244. [Słowo kluczowe [SisyphusRuby] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1\n- 최종 위력 +1
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=SisyphusRuby].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1\n- Moc Końcowa +1
245. [Słowo kluczowe [RougeThreeCocoonShield] — nazwa] 믿음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].name
   kontekst: identyfikator tagu w tekstach: `[RougeThreeCocoonShield]`
   limit: do 40 znaków
   EN: Devotion
   PL: Wiara
246. [Słowo kluczowe [RougeThreeCocoonShield] — opis] - 턴 시작시 수치만큼 보호막을 얻음\n- 보호막이 감소하면 수치도 감소함
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain Shield equal to Stack\n- Lose Stack when losing Shield
   PL: - Na początku tury zyskuje Tarczę równą liczbie ładunków\n- Gdy traci Tarczę, traci też ładunki
247. [Słowo kluczowe [RougeThreeCocoonShield] — tekst klimatyczny] ‘믿음은 바라는 것들의 실상이요, 바라는 것들의…’
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].flavor
   limit: do 120 znaków
   EN: "Now faith is the substance of things hoped for, the          of things not seen."
   PL: „Wiara zaś jest poręką tego, czego się spodziewamy, i dowodem…”
248. [Słowo kluczowe [RisingMadnessSisyphe] — nazwa] 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessSisyphe]`
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Słowo kluczowe [RisingMadnessSisyphe] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
250. [Słowo kluczowe [RisingMadnessSisyphe] — tekst klimatyczny] …될 수 있어.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].flavor
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Słowo kluczowe [RisingMadnessSisyphe2nd] — nazwa] 따가운 햇살
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].name
   kontekst: identyfikator tagu w tekstach: `[RisingMadnessSisyphe2nd]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Słowo kluczowe [RisingMadnessSisyphe2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
253. [Słowo kluczowe [RisingMadnessSisyphe2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].flavor
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Słowo kluczowe [WeakWithering_LowMorale] — nazwa] 헝클어진 재봉
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=WeakWithering_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WeakWithering_LowMorale]`
   limit: do 40 znaków
   EN: Messy Sewing
   PL: Poplątane Szycie
255. [Słowo kluczowe [WeakWithering_LowMorale] — opis] - 사기 저하\n- 턴 시작시 공격 위력 감소 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=WeakWithering_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Spadku Mocy Ataku
256. [Słowo kluczowe [WeakWithering_Panic] — nazwa] 헝클어진 재봉
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=WeakWithering_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WeakWithering_Panic]`
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Słowo kluczowe [WeakWithering_Panic] — opis] - 패닉\n- 턴 시작시 공격 위력 감소 1, 피해량 감소 1 얻음
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=WeakWithering_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down and 1 Damage Down
   PL: - Panika\n- Na początku tury zyskuje 1 Spadku Mocy Ataku i 1 Spadku Obrażeń
258. [Słowo kluczowe [NiddlePin] — nazwa] 바늘못
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddlePin].name
   kontekst: identyfikator tagu w tekstach: `[NiddlePin]`
   limit: do 40 znaków
   EN: Naildle
   PL: Igłogwóźdź
259. [Słowo kluczowe [NiddlePin] — opis] - 특수 출혈\n- 관통 피해를 받으면, 출혈 횟수 1 증가하고 수치 1 감소\n- 턴 종료시 출혈 1 얻고 수치 1 감소
   źródło: BattleKeywords-a1c10p1.json :: dataList[id=NiddlePin].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- When taking Pierce damage, gain +1 Bleed Count and reduce this effect's Stack by 1\n- Turn End: Gain 1 Bleed and reduce this effect's Stack by 1
   PL: - Specjalne Krwawienie\n- Przy otrzymaniu obrażeń kłutych zyskuje 1 Licznika Krwawienia i traci 1 ładunek\n- Na koniec tury zyskuje 1 Krwawienia i traci 1 ładunek

## Słowa kluczowe bitwy — BattleKeywords-a1c10p2
- plik gry: `BattleKeywords-a1c10p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

260. [Słowo kluczowe [TangleBlackYarn] — nazwa] 뒤엉킴
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TangleBlackYarn].name
   kontekst: identyfikator tagu w tekstach: `[TangleBlackYarn]`
   limit: do 40 znaków
   EN: Tangling
   PL: Splątanie
261. [Słowo kluczowe [TangleBlackYarn] — opis] - 최댓값 : 30\n- 수치당 받는 피해량 +1%\n- 수치 10당 기본 위력 -1\n- 턴 종료 시 수치 3당, 다음 턴에 속박 1 얻음 (최대 10)\n- <color=#ff6000><mark color=#ff000040><b><u>수비 스킬 사용 시</color></mark></b></u> 수치 절반 감소 (소수점 올림)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TangleBlackYarn].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 30\n- Take +1% damage for every Stack\n- Base Power -1 for every 10 Stacks\n- Turn End: Gain 1 Bind next turn for every 3 Stacks (max 10)\n- <color=#ff6000><mark color=#ff000040><b><u>On Defense Skill Use,</color></mark></b></u> lose half of the Stacks (rounded up)
   PL: - Maks. ładunków: 30\n- Otrzymuje obrażenia +1% za każdy ładunek\n- Moc Bazowa -1 za każde 10 ładunków\n- Na koniec tury zyskuje w następnej turze 1 Spętania za każde 3 ładunków (maks. 10)\n- <color=#ff6000><mark color=#ff000040><b><u>Przy użyciu Umiejętności obrony</u></b></mark></color> traci połowę ładunków (zaokrąglane w górę)
262. [Słowo kluczowe [TangleBlackYarn] — tekst klimatyczny] 백화점은 실과 바늘로 얽힌 봉제의 세계. 이제는 바다에서 온것이라해도 그 몸은 실로 변하여 검은 물이 검은 실로 엉켜간다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TangleBlackYarn].flavor
   limit: do 240 znaków
   EN: The department store is a world of sewing, bound together by thread and needle. Even that which came from the sea now finds its body turned to thread, black water tangling into black yarn.
   PL: Grand Magasin to świat szycia, spleciony nitką i igłą. Nawet to, co przyszło z morza, zamieniło się w nić — czarna woda plącze się w czarną przędzę.
263. [Słowo kluczowe [SickBlackYarn] — nazwa] 뜯겨져 나가는 검은실밥
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SickBlackYarn].name
   kontekst: identyfikator tagu w tekstach: `[SickBlackYarn]`
   limit: do 40 znaków
   EN: Bursting Blackstitch
   PL: Pękające Czarne Szwy
264. [Słowo kluczowe [SickBlackYarn] — opis] - 최댓값 : 50\n- 수치당 받는 피해량 +1%\n- 턴 시작 시 수치 25당 취약 1 얻음
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SickBlackYarn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Take +1% damage for every Stack\n- Turn Start: Gain 1 Fragile for every 25 Stacks
   PL: - Maks. ładunków: 50\n- Otrzymuje obrażenia +1% za każdy ładunek\n- Na początku tury zyskuje 1 Wrażliwości za każde 25 ładunków
265. [Słowo kluczowe [SickBlackYarn] — tekst klimatyczny] 검은실에서 터져나온 실밥이 터질때마다 비릿하지만 어딘가 그리운 눈물 냄새가 난다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SickBlackYarn].flavor
   limit: do 170 znaków
   EN: Each time a loose strand bursts from the black yarn, it carries the briny scent of tears... strangely nostalgic despite itself.
   PL: Każdy strzęp czarnej przędzy, gdy pęka, pachnie słonawymi łzami... dziwnie nostalgicznym, mimo wszystko.
266. [Słowo kluczowe [HeavyBlackYarn] — nazwa] 검게 뭉친 실
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HeavyBlackYarn].name
   kontekst: identyfikator tagu w tekstach: `[HeavyBlackYarn]`
   limit: do 40 znaków
   EN: Clumped Black Threads
   PL: Sklejone Czarne Nici
267. [Słowo kluczowe [HeavyBlackYarn] — opis] - 최댓값 : 5\n- 수치 만큼 부위 별 슬롯 가중치 증가\n- 수치 1당, 받는 피해량 +10%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HeavyBlackYarn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Gain Slot Weight equal to Stack (per Part)\n- Take +10% damage for every Stack
   PL: - Maks. ładunków: 5\n- Zyskuje Wagę Slotu równą liczbie ładunków (na każdą Część)\n- Otrzymuje obrażenia +10% za każdy ładunek
268. [Słowo kluczowe [HeavyBlackYarn] — tekst klimatyczny] 검은 것은 죽음과 질량의 도상. 검은 바닷물의 물기를 머금은것이 무거워지는것처럼 검은실이 뭉쳐가는것도 같은 결과를 낸다. 모든것을 품고 응어리져 가라앉고 멈춘다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HeavyBlackYarn].flavor
   limit: do 260 znaków
   EN: Black is an image of death and mass. Just as what holds black seawater grows heavy, black thread gains weight as it clumps together. It gathers everything into itself, knots tight, sinks, and stops.
   PL: Czerń to wyobrażenie śmierci i masy. Jak to, co nasączono czarną wodą morską, staje się ciężkie, tak i sklejające się czarne nici dają ten sam rezultat. Wszystko obejmują, tężeją jak grudka, toną i zastygają.
269. [Słowo kluczowe [HideBlackYarn] — nazwa] 검은 물 웅덩이
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HideBlackYarn].name
   kontekst: identyfikator tagu w tekstach: `[HideBlackYarn]`
   limit: do 40 znaków
   EN: Pool of Black Water
   PL: Kałuża Czarnej Wody
270. [Słowo kluczowe [HideBlackYarn] — opis] - 위력 최댓값 : 6\n- 횟수 최댓값 : 2\n- <color=#ff6000><mark color=#ff000040><b><u>피격 시 위력 1 감소</color></mark></b></u> (스킬당 1회)\n- 턴 종료 시 횟수 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>위력이나 횟수가 0이 되면 소멸</color></mark></b></u>\n- 흐트러짐 상태가 되지 않음\n- 일방 공격 시 가하는 피해량 +100%\n- 받는 피해량 -100%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HideBlackYarn].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Potency: 6\n- Max Count: 2\n- <color=#ff6000><mark color=#ff000040><b><u>When hit, lose 1 Potency</color></mark></b></u> (once per Skill)\n- Turn End: Lose 1 Count\n- <color=#ff6000><mark color=#ff000040><b><u>Expires if Potency or Count reaches 0</color></mark></b></u>\n- Cannot be Staggered\n- On Unopposed Attack, deal +100% damage\n- Take -100% damage
   PL: - Maks. Siły: 6\n- Maks. licznika: 2\n- <color=#ff6000><mark color=#ff000040><b><u>Przy trafieniu traci 1 Siły</u></b></mark></color> (1 raz na Umiejętność)\n- Na koniec tury traci 1 Licznika\n- <color=#ff6000><mark color=#ff000040><b><u>Znika, gdy Siła lub Licznik osiągną 0</u></b></mark></color>\n- Nie może ulec Oszołomieniu\n- Przy Ataku Jednostronnym zadaje obrażenia +100%\n- Otrzymuje obrażenia -100%
271. [Słowo kluczowe [HideBlackYarn] — tekst klimatyczny] 이제는 바다도. 수족관도 아닌. 고인 물 웅덩이지만 그 곳은 큰 그리움을 품고있어서 잠시 몸을 숨길 정도의 넉넉한 슬픔은 고여있다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=HideBlackYarn].flavor
   limit: do 200 znaków
   EN: It is neither sea nor aquarium now, only a stagnant pond. Yet the great longing that has settled there holds enough sorrow to momentarily hide the body.
   PL: To już nie morze, ani akwarium — tylko stojąca kałuża. Ale wielka tęsknota, która się w niej osadziła, gromadzi tyle żalu, by na chwilę ukryć ciało.
272. [Słowo kluczowe [AngryBlackYarn] — nazwa] 옛 포식자의 본능
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AngryBlackYarn].name
   kontekst: identyfikator tagu w tekstach: `[AngryBlackYarn]`
   limit: do 50 znaków
   EN: Instinct of the Predator of Eld
   PL: Instynkt Dawnego Drapieżnika
273. [Słowo kluczowe [AngryBlackYarn] — opis] - 이 효과를 보유한 부위 1개당, 모든 부위의 합 위력 +2\n- 대상의 뒤엉킴 수치 3당, 가하는 피해량 +5% (최대 50%)\n- 턴 종료 시 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AngryBlackYarn].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All Parts gain Clash Power +2 for every Part that has this effect\n- Deal +5% damage for every 3 Tangling Stacks on target (max 50%)\n- Expires at Turn End
   PL: - Za każdą Część posiadającą ten efekt wszystkie Części zyskują Moc Starcia +2\n- Zadaje obrażenia +5% za każde 3 Splątania na celu (maks. 50%)\n- Znika na koniec tury
274. [Słowo kluczowe [AngryBlackYarn] — tekst klimatyczny] 수족관 마다 포식자가 있었다. 백화점의 플로어 매니저처럼. 지금 포식자는 물고기의 모습이지만, 과거 시지프 시스템에서 아쿠아리움에 물고기의 모습은 없었다. 아쿠아리움속에 살았던 자들의 정신은 물고기여도 모습은 사람이었다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AngryBlackYarn].flavor
   limit: do 380 znaków
   EN: Every aquarium had its predator, much like a Floor Manager in the department store. The predator now wears the shape of a fish, but in an earlier Sisyphe System, there were no fish-shaped beings in the Aquarium. The minds of those who lived there may have been fish, but their forms were human.
   PL: W każdym akwarium był swój drapieżnik — niczym Menedżer Piętra w Grand Magasin. Drapieżnik nosi dziś postać ryby, lecz w dawnym Systemie Sisyphe w Akwarium nie było istot o ciele ryby. Umysły tych, którzy tam żyli, były rybimi, ale ich postaci — ludzkie.
275. [Słowo kluczowe [BlackYarn_LowMorale] — nazwa] 자식 잃은 것
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BlackYarn_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BlackYarn_LowMorale]`
   limit: do 40 znaków
   EN: Bereaved of Child
   PL: Pogrążone w Żałobie po Dziecku
276. [Słowo kluczowe [BlackYarn_LowMorale] — opis] - 사기 저하\n- 스킬 사용 시 메인 타겟이 뿌이면, 합 위력 +3, 기본 위력 +2\n- 피격 시 뒤엉킴 1 부여 (스킬당 3회)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BlackYarn_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Skill Use, if Pwie is the main target, Clash Power +3, Base Power +2\n- When hit, inflict 1 Tangling (3 times per Skill)
   PL: - Niskie Morale\n- Przy użyciu Umiejętności, jeżeli głównym celem jest Pwie, Moc Starcia +3, Moc Bazowa +2\n- Przy trafieniu nakłada 1 Splątania (3 razy na Umiejętność)
277. [Słowo kluczowe [BlackYarn_Panic] — nazwa] 자식 잃은 것
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BlackYarn_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BlackYarn_Panic]`
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Słowo kluczowe [BlackYarn_Panic] — opis] - 패닉\n- 모든 공격의 대상을 뿌이로 지정\n- 스킬 사용 시 메인 타겟이 뿌이면, 합 위력 +6, 기본 위력 +4\n- 전투 시작 시 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 피격 시 뒤엉킴 1 부여 (스킬당 6회)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BlackYarn_Panic].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- All Attacks target Pwie\n- On Skill Use, if Pwie is the main target, Clash Power +6, Base Power +4\n- Combat Start: Convert all Skill Coins into Unbreakable Coins\n- When hit, inflict 1 Tangling (6 times per Skill)
   PL: - Panika\n- Wszystkie Ataki celują w Pwie\n- Przy użyciu Umiejętności, jeżeli głównym celem jest Pwie, Moc Starcia +6, Moc Bazowa +4\n- Na początku walki wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Przy trafieniu nakłada 1 Splątania (6 razy na Umiejętność)
279. [Słowo kluczowe [FlowerLaurelWreath] — nazwa] 속죄의 월계관
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FlowerLaurelWreath].name
   kontekst: identyfikator tagu w tekstach: `[FlowerLaurelWreath]`
   limit: do 40 znaków
   EN: Laurel Wreath of Atonement
   PL: Wieniec Laurowy Zadośćuczynienia
280. [Słowo kluczowe [FlowerLaurelWreath] — opis] - 자신의 흐트러짐 선 모두 제거\n- 합 위력 +2\n- 침잠으로 받는 정신 피해 -50% (소수점 버림)\n- 턴 종료시 정신력 10 회복, 다음 턴에 신속 5 얻음\n- <color=#ff6000><mark color=#ff000040><b><u>합 승리시 본인과 조력자를 포함한 모든 아군의 정신력 5 회복</color></mark></b></u>
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FlowerLaurelWreath].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Remove all Stagger Thresholds\n- Clash Power +2\n- Take -50% SP damage from Sinking (rounded down)\n- Turn End: Heal 10 SP and gain 5 Haste next turn\n- <color=#ff6000><mark color=#ff000040><b><u>Clash Win: Heal 5 SP for all allies including this unit and Assist Units</color></mark></b></u>
   PL: - Usuwa wszystkie Progi Oszołomienia\n- Moc Starcia +2\n- Otrzymuje -50% obrażeń Poczytalności od Zatonięcia (zaokr. w dół)\n- Na koniec tury odzyskuje 10 Poczytalności i 5 Pośpiechu w następnej turze\n- <color=#ff6000><mark color=#ff000040><b><u>Po wygranej w Starciu wszyscy sojusznicy (łącznie z Wsparciem) odzyskują 5 Poczytalności</u></b></mark></color>
281. [Słowo kluczowe [FlowerLaurelWreath] — tekst klimatyczny] 죄를 고하는 그 모습, 꽃향기 아래에서 피어나라
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FlowerLaurelWreath].flavor
   limit: do 120 znaków
   EN: Let the confession of its sins bloom beneath the fragrance of flowers.
   PL: Niech wyznanie grzechów rozkwita pod kwiatową wonią.
282. [Słowo kluczowe [AlriuneSillage] — nazwa] 잔향
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriuneSillage].name
   kontekst: identyfikator tagu w tekstach: `[AlriuneSillage]`
   limit: do 40 znaków
   EN: Faint Aroma
   PL: Subtelny Aromat
283. [Słowo kluczowe [AlriuneSillage] — opis] - 최댓값 : 30\n- 턴 종료 시 수치만큼 정신력 피해\n- 침잠 피해를 받으면, 수치 1 증가\n- 진동 폭발시, 자신을 제외한 무작위 아군 3명에게 잔향 1 ~ 2 부여\n- 수치가 최대면 진동을 2 얻고 진동 폭발, 자신의 침잠만큼 우울 피해를 받고 잔향 소멸. 이번 턴 동안 잔향을 얻을 수 없음\n- 사망 시, 아군에게 자신의 잔향을 수치의 절반만큼 무작위로 나눠서 부여 (소수점 버림)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriuneSillage].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn End: Take SP damage equal to Stack\n- If this unit took Sinking damage, gain 1 Stack\n- On Tremor Burst, apply 1 ~ 2 Faint Aroma on 3 other random allies\n- At max Stack:\n · Gain 2 Tremor and trigger Tremor Burst on self\n · Take Gloom damage equal to Sinking on self\n · Faint Aroma expires\n · Cannot gain for the rest of the turn\n- On death, apply half of this unit's Faint Aroma Stack randomly between this unit's allies (rounded down)
   PL: - Maks. ładunków: 30\n- Na koniec tury otrzymuje obrażenia Poczytalności równe liczbie ładunków\n- Przy otrzymaniu obrażeń od Zatonięcia zyskuje 1 ładunek\n- Przy Wyładowaniu Wstrząsu nakłada 1–2 „Subtelnego Aromatu” na 3 innych losowych sojuszników\n- Przy Maks. ładunków zyskuje 2 Wstrząsu i wywołuje Wyładowanie Wstrząsu, otrzymuje obrażenia Posępności równe własnemu Zatonięciu, a Subtelny Aromat znika; do końca tury nie można go zyskać\n- Przy śmierci rozdziela losowo między sojuszników połowę własnych ładunków „Subtelnego Aromatu” (zaokrąglane w dół)
284. [Słowo kluczowe [AlriuneSillage] — tekst klimatyczny] 향기는 그리움을. 그리움은 사무침을.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriuneSillage].flavor
   limit: do 120 znaków
   EN: Fragrance begets longing. Longing, in turn, becomes yearning.
   PL: Zapach rodzi tęsknotę. A tęsknota — serdeczny ból.
285. [Słowo kluczowe [AlriunePetal] — nazwa] 꽃잎
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriunePetal].name
   kontekst: identyfikator tagu w tekstach: `[AlriunePetal]`
   limit: do 40 znaków
   EN: Petals
   PL: Płatki
286. [Słowo kluczowe [AlriunePetal] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>3이면 해당 턴에 강력한 스킬을 사용함</color></mark></b></u>\n- 흐트러진 대상에게 가하는 피해량 (자신의 꽃잎 x 10)% 만큼 증가\n- 턴 종료시 1 증가
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriunePetal].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>At 3 Stacks, use a powerful Skill that turn</color></mark></b></u>\n- Deal +(Petals Stack on self x 10)% damage to Staggered targets\n- Turn End: Gain 1 Stack
   PL: - Maks. ładunków: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Przy 3 ładunkach w tej turze używa potężnej Umiejętności</u></b></mark></color>\n- Zadaje oszołomionym celom obrażenia +(Płatki na sobie x 10)%\n- Na koniec tury zyskuje 1 ładunek
287. [Słowo kluczowe [AlriunePetal] — tekst klimatyczny] 꽃잎 하나, 꽃잎 둘. 그리고 셋.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=AlriunePetal].flavor
   limit: do 120 znaków
   EN: One petal, two petals... and then, three.
   PL: Płatek pierwszy, płatek drugi. A potem trzeci.
288. [Słowo kluczowe [ThreadDye] — nazwa] 염색실
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThreadDye].name
   kontekst: identyfikator tagu w tekstach: `[ThreadDye]`
   limit: do 40 znaków
   EN: Dyed Thread
   PL: Barwiona Nić
289. [Słowo kluczowe [ThreadDye] — opis] - 최댓값: 3\n- 효과 보유 시 신속 효과 획득 불가\n- 턴 종료시 다음 턴에 부여될 신속 제거\n- 턴 종료시 위력 만큼 다음 턴에 속박 부여 후 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>최댓값이면, 이번 턴과 다음 턴에 행동 불가를 얻고 소멸</color></mark></b></u>
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThreadDye].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- Cannot gain Haste while having this effect\n- Turn End: Remove Haste that will be applied next turn\n- Turn End: Gain Bind next turn equal to Potency and lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>At max Stack, gain Immobilize this turn and next turn; then, this effect expires</color></mark></b></u>
   PL: - Maks. ładunków: 3\n- Posiadając ten efekt, nie może zyskać Pośpiechu\n- Na koniec tury usuwa Pośpiech, który miał zostać nałożony w następnej turze\n- Na koniec tury nakłada w następnej turze Spętanie w wysokości Siły, po czym traci 1 ładunek\n- <color=#ff6000><mark color=#ff000040><b><u>Przy Maks. ładunków zyskuje Unieruchomienie na tę i następną turę, po czym znika</u></b></mark></color>
290. [Słowo kluczowe [ThreadDye] — tekst klimatyczny] 실도 못과 같이 당신을 붙잡아 고정시킨다. 정해진 색으로.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThreadDye].flavor
   limit: do 120 znaków
   EN: Like nails, threads will hold you fast, the color of its binds predetermined.
   PL: Jak gwóźdź, nić również przytrzymuje i unieruchamia. W z góry wyznaczonym kolorze.
291. [Słowo kluczowe [SpreadingDye] — nazwa] 글로스 미디엄
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SpreadingDye].name
   kontekst: identyfikator tagu w tekstach: `[SpreadingDye]`
   limit: do 40 znaków
   EN: Gloss Medium
   PL: Gloss Medium
292. [Słowo kluczowe [SpreadingDye] — opis] - 대상에게 속박이 있으면, 출혈 위력 및 횟수 부여량 +1\n- 스킬 사용시 메인 타겟이 염색실이나 타르 염료를 보유했으면, 해당 스킬의 최종 위력 +1, 가하는 피해량 +20%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SpreadingDye].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If target has Bind, inflict 1 more Bleed Potency and Bleed Count\n- On Skill Use, if the main target has Dyed Thread or Tar Dye, the said Skill gains Final Power +1 and deals +20% damage
   PL: - Jeżeli cel posiada Spętanie, nakłada o 1 więcej Siły Krwawienia i Licznika Krwawienia\n- Przy użyciu Umiejętności, jeżeli główny cel posiada Barwioną Nić lub Barwnik Smołowy, ta Umiejętność zyskuje Moc Końcową +1 i zadaje obrażenia +20%
293. [Słowo kluczowe [SpreadingDye] — tekst klimatyczny] 대부분의 염료는 색이 정해져 있다.\n하지만 이자의 염료에는 정해진 색이 없다.\n거칠게 칠해져 순수한 빛의 반사·굴절만으로 다양한 색을 내비친다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SpreadingDye].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Most dyes are meant to have a color.\nBut this one's dye has none.\n\nApplied in rough, uneven strokes, it reveals a spectrum of colors through nothing but the reflection and refraction of pure light.
   PL: Większość barwników ma przypisany kolor.\nTen barwnik koloru nie ma.\nRzucony grubymi, nierównymi pociągnięciami, odsłania spektrum barw jedynie odbiciem i załamaniem czystego światła.
294. [Słowo kluczowe [StickyDye] — nazwa] 타르 염료
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=StickyDye].name
   kontekst: identyfikator tagu w tekstach: `[StickyDye]`
   limit: do 40 znaków
   EN: Tar Dye
   PL: Barwnik Smołowy
295. [Słowo kluczowe [StickyDye] — opis] - 최댓값: 1\n- 속도 최솟값, 최댓값 1 감소 (최소 1)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=StickyDye].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Min & Max Speed -1 (min 1)
   PL: - Maks. ładunków: 1\n- Min. i Maks. Szybkość -1 (min. 1)
296. [Słowo kluczowe [StickyDye] — tekst klimatyczny] 염료가 달라 붙어 발을 떼기 어렵다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=StickyDye].flavor
   limit: do 120 znaków
   EN: The dye clings, making every step harder to take.
   PL: Barwnik przykleja się, utrudniając każdy krok.
297. [Słowo kluczowe [ChargeKhaki] — nazwa] 표류 관성
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ChargeKhaki].name
   kontekst: identyfikator tagu w tekstach: `[ChargeKhaki]`
   limit: do 40 znaków
   EN: Inertia of Drifting
   PL: Bezwładność Dryfowania
298. [Słowo kluczowe [ChargeKhaki] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료 시, 횟수 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ChargeKhaki].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count
   PL: - Specjalny Ładunek\n- Maks. licznika: 20\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Siłę i Licznik Ładunku\n- Na koniec tury traci 1 Licznika
299. [Słowo kluczowe [ChargeKhaki] — tekst klimatyczny] 표류하는 자들은 흐름을 바꿀 수는 없어도 흐름을 공고히 하고 흐름 속에서 자신의 일을 한다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ChargeKhaki].flavor
   limit: do 210 znaków
   EN: Those who are carried by the tide like buoys may not be able to change the flow of things, but they can still bolster the tide and commit to their acts within.
   PL: Ci, którzy dryfują, choć nie zdołają zmienić prądu, umacniają go i wypełniają swoje zadania w jego łonie.
300. [Słowo kluczowe [FinishedFabric] — nazwa] 재단된 원단
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FinishedFabric].name
   kontekst: identyfikator tagu w tekstach: `[FinishedFabric]`
   limit: do 40 znaków
   EN: Cut Fabric
   PL: Skrojona Tkanina
301. [Słowo kluczowe [FinishedFabric] — opis] - 최댓값 : 30\n- 충전 횟수(특수 충전 포함)를 획득하거나 소모하는 스킬의 피해량 +(수치)% (최대 30%)\n- 턴 종료 시, 5 감소\n· 이번 턴에 보호막이 파괴되었으면, 대신 10 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FinishedFabric].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Skills that gain or consume Charge Count (including Unique Charge) deal +(Stack)% damage (max 30%)\n- Turn End: Lose 5 Stacks\n  · If Shield was broken this turn, lose 10 Stacks instead
   PL: - Maks. ładunków: 30\n- Umiejętności, które zyskują lub zużywają Licznik Ładunku (w tym Specjalny Ładunek), zadają obrażenia +(ładunki)% (maks. 30%)\n- Na koniec tury traci 5 ładunków\n· Jeżeli w tej turze Tarcza została złamana, zamiast tego traci 10 ładunków
302. [Słowo kluczowe [FinishedFabric] — tekst klimatyczny] 저마다의 기능을 가진 원단은 제대로 재단되어야만 제 기능을 발휘한다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=FinishedFabric].flavor
   limit: do 120 znaków
   EN: Fabrics with functions of their own can only serve their purpose when properly cut.
   PL: Tkaniny, każda z własnym przeznaczeniem, spełniają swoją rolę tylko wtedy, gdy właściwie je się skroje.
303. [Słowo kluczowe [LargeTailoringShears] — nazwa] 꽃가위
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LargeTailoringShears].name
   kontekst: identyfikator tagu w tekstach: `[LargeTailoringShears]`
   limit: do 40 znaków
   EN: Blossom Scissors
   PL: Kwiatowe Nożyczki
304. [Słowo kluczowe [LargeTailoringShears] — opis] - 최댓값 : 3\n- 수감자에게 가하는 피해량 +(5 + 수치 x 5)% (최대 20%)\n- 수선 대상을 보유한 수감자에게 스킬 사용 시, 수치만큼 합 위력이 증가
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LargeTailoringShears].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Deal +(5 + Stack x 5)% damage against Sinners (max 20%)\n- On Skill Use against Alteration Target Sinners, gain Clash Power equal to Stack
   PL: - Maks. ładunków: 3\n- Zadaje Grzesznikom obrażenia +(5 + ładunki x 5)% (maks. 20%)\n- Przy użyciu Umiejętności na Grzesznika będącego Celem Poprawek zyskuje Moc Starcia równą liczbie ładunków
305. [Słowo kluczowe [LargeTailoringShears] — tekst klimatyczny] 지하에서 만들어진 원초의 재료를 끊어 내기 위한 가위는 더욱 특별하고 거대하다. 처음으로 직조된 천을 자르고 잘라 왔던 이 가위에서 꽃이 피어나는 건 근원을 잘라 왔기 때문이며, 자연스러운 현상이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LargeTailoringShears].flavor
   limit: do 370 znaków
   EN: The scissors used to sever the primordial materials produced underground are larger and more extraordinary still. These scissors have cut and recut the very first cloth ever woven. That flowers should bloom from them is only natural, for they have always cut things at their very roots.
   PL: Nożyczki służące do odcinania pierwotnych materiałów rodzących się w podziemiach są jeszcze bardziej wyjątkowe i ogromne. To one od zawsze kroiły i wycinały pierwotnie utkane płótno — kwiaty kwitnące z nich są naturalną konsekwencją siekania u samych korzeni.
306. [Słowo kluczowe [TailoringTarget] — nazwa] 수선 대상
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TailoringTarget].name
   kontekst: identyfikator tagu w tekstach: `[TailoringTarget]`
   limit: do 40 znaków
   EN: Alteration Target
   PL: Cel Poprawek
307. [Słowo kluczowe [TailoringTarget] — opis] - 속도 최솟값, 최댓값 +5\n- 이번 턴에 처음으로 사용하는 스킬의 합 위력 +3\n- 전투 시작 시 수비 스킬을 장착하였다면, 수선사 아네트에게 받는 피해량이 80%만큼 감소\n- 턴 종료 시, 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TailoringTarget].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +5\n- This turn's first-used Skill gains Clash Power +3\n- Combat Start: If this unit has an equipped Defense Skill, take -80% damage from Annette the Alterationist\n- Turn End: Lose 1 Stack
   PL: - Min. i Maks. Szybkość +5\n- Pierwsza Umiejętność użyta w tej turze zyskuje Moc Starcia +3\n- Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymuje od Annette, Krawcowej, obrażenia -80%\n- Na koniec tury traci 1 ładunek
308. [Słowo kluczowe [TailoringTarget] — tekst klimatyczny] 사람에 맞춰 옷을 수선하는 것이 아니라, 옷에 맞춰 사람을 수선한다. 이곳에서는 옷이 사람을 결정하기에, 옷은 보존하고 대신 사람을 수선하는 것이 가치를 지키고, 고객을 위하는 일이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=TailoringTarget].flavor
   limit: do 310 znaków
   EN: Rather than altering the clothes to fit the person, she alters the person to fit the clothes. Here, clothes are what define the wearer; preserving the garment and altering the person is how worth is protected and how the customer is served.
   PL: Zamiast dopasowywać ubrania do człowieka, dopasowuje człowieka do ubrań. Tutaj to ubranie określa człowieka — zachować szatę, a poprawić człowieka, znaczy chronić wartość i służyć klientowi.
309. [Słowo kluczowe [ScissorsMark] — nazwa] 마름질 표식
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ScissorsMark].name
   kontekst: identyfikator tagu w tekstach: `[ScissorsMark]`
   limit: do 40 znaków
   EN: Mark of Shearing
   PL: Znak Krojenia
310. [Słowo kluczowe [ScissorsMark] — opis] - 최댓값 : 9\n- 수치만큼 방어 레벨이 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ScissorsMark].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- Lose Defense Level equal to Stack
   PL: - Maks. ładunków: 9\n- Traci Poziom Obrony równy liczbie ładunków
311. [Słowo kluczowe [ScissorsMark] — tekst klimatyczny] 옷감이나 재목 따위를 치수에 맞게 베어 내기 위한 표식
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ScissorsMark].flavor
   limit: do 120 znaków
   EN: A cutting mark used to trim fabric and other materials to the required measurements.
   PL: Znak służący do wycinania tkanin i innych materiałów na wymiar.
312. [Słowo kluczowe [DamagedFabric] — nazwa] 재단되어버린
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=DamagedFabric].name
   kontekst: identyfikator tagu w tekstach: `[DamagedFabric]`
   limit: do 40 znaków
   EN: Sheared Apart
   PL: Rozcięte
313. [Słowo kluczowe [DamagedFabric] — opis] - 최댓값 : 30\n- 턴 시작 시, 수치 6당 체력 회복 감소 1 얻음 (최대 5)\n- ‘패턴 따기’, ‘쉬르필 아 라 셴’ 스킬과 합 진행 시, 수치만큼 합 위력이 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=DamagedFabric].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start : Gain 1 HP Healing Down for every 6 Stacks (max 5)\n- Upon Clashing against "Patterning" or "Surfile à la Chaîne", lose Clash Power equal to Stack
   PL: - Maks. ładunków: 30\n- Na początku tury zyskuje 1 Spadku Regeneracji HP za każde 6 ładunków (maks. 5)\n- Podczas Starcia z Umiejętnościami „Wycinanie Wzoru” i „Surfile à la Chaîne” traci Moc Starcia równą liczbie ładunków
314. [Słowo kluczowe [DamagedFabric] — tekst klimatyczny] 마름질된 천은 다시 꿰매더라도 패치워크가 될 뿐, 여러 가닥으로 이어졌던 원래의 천으로는 되돌아갈 수 없다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=DamagedFabric].flavor
   limit: do 210 znaków
   EN: Once the fabric has been cut apart, sewing the scraps back together only makes patchwork. It can never return to a single fabric woven from its original threads.
   PL: Posiekane płótno, choćby je zszyć, staje się tylko patchworkiem — nigdy nie wróci do jednej tkaniny utkanej z pierwotnych nici.
315. [Słowo kluczowe [ThirdTailor_LowMorale] — nazwa] 손떨림
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ThirdTailor_LowMorale]`
   limit: do 40 znaków
   EN: Trembling Hands
   PL: Drżące Dłonie
316. [Słowo kluczowe [ThirdTailor_LowMorale] — opis] - 사기 저하\n받는 피해량 +7.5%\n피격받을 때마다 자신의 진동 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +7.5% damage\n- Every time this unit is hit, gain +1 Tremor Count (once per Skill, max 5 per turn)
   PL: - Niskie Morale\nOtrzymuje obrażenia +7,5%\nPrzy każdym trafieniu zyskuje +1 Licznika Wstrząsu (1 raz na Umiejętność, maks. 5 na turę)
317. [Słowo kluczowe [ThirdTailor_LowMorale] — tekst klimatyczny] 손이 떨리면, 가위질도 흔들려… 이대로는 재단할 수 없어…
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].flavor
   limit: do 160 znaków
   EN: My hands are starting to shake, and even the scissors won't stay steady... I won't be able to cut the pattern anymore...
   PL: Dłonie mi drżą, nożyce też chwiała... W ten sposób nie skroję już wzoru...
318. [Słowo kluczowe [ThirdTailor_Panic] — nazwa] 손떨림
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ThirdTailor_Panic]`
   (powtórzenie elementu 315 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Słowo kluczowe [ThirdTailor_Panic] — opis] - 패닉\n받는 피해량 +15%\n피격받을 때마다 자신의 진동 위력 1, 진동 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +15% damage\n- Every time this unit is hit, gain 1 Tremor Potency and +1 Tremor Count (once per Skill, max 5 per turn)
   PL: - Panika\nOtrzymuje obrażenia +15%\nPrzy każdym trafieniu zyskuje 1 Siły Wstrząsu i +1 Licznika Wstrząsu (1 raz na Umiejętność, maks. 5 na turę)
320. [Słowo kluczowe [ThirdTailor_Panic] — tekst klimatyczny] 손이 떨리면, 가위질도 흔들려… 이대로는 재단할 수 없어…
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=ThirdTailor_Panic].flavor
   (powtórzenie elementu 317 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Słowo kluczowe [GoldenLeatherEnhance] — nazwa] 따갑게 내리쬐는 햇살[바느질의 왕]
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].name
   kontekst: identyfikator tagu w tekstach: `[GoldenLeatherEnhance]`
   limit: do 70 znaków
   EN: Shower of Stinging Sunshine [King of Needleworks]
   PL: Parzące Promienie Słońca [Król Szycia]
322. [Słowo kluczowe [GoldenLeatherEnhance] — opis] 대상의 바늘못 3당 자신의 스킬 최종 위력 +1 (최대 3)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].desc
   limit: do 120 znaków
   EN: Skill Final Power +1 for every 3 Naildle on the target (max 3)
   PL: Moc Końcowa Umiejętności +1 za każde 3 Igłogwoźdź na celu (maks. 3)
323. [Słowo kluczowe [GoldenLeatherEnhance] — tekst klimatyczny] ‘듣지 않아도돼. 들리지 않게하면돼. 네가 원한다면 그렇게 하는거야. 부정하지 않아도돼.’
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].flavor
   limit: do 170 znaków
   EN: "You don't have to listen anymore. You only have to make it so you cannot hear them. Simply do what you want. Don't deny yourself."
   PL: „Nie musisz słuchać. Wystarczy sprawić, żebyś nie mógł słyszeć. Jeżeli tego chcesz, tak właśnie zrób. Nie musisz tego negować.”
324. [Słowo kluczowe [NoirShieldUp] — nazwa] 검은 신의 가호
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldUp].name
   kontekst: identyfikator tagu w tekstach: `[NoirShieldUp]`
   limit: do 40 znaków
   EN: Blessing of the Obsidian God
   PL: Błogosławieństwo Czarnego Boga
325. [Słowo kluczowe [NoirShieldUp] — opis] - 위력 최댓값 : 999\n- 횟수 기본값 : 2\n- 흐트러짐 면역\n- 턴 시작시 수치만큼 부위가 보호막 얻음\n- 이 효과는 보호막 관리 효과로 취급됨\n- 보호막이 감소하면 수치도 감소함\n- 턴 종료시 횟수 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldUp].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 999\n- Base Count: 2\n- Cannot be Staggered\n- Turn Start: The Part gains Shield equal to Stack\n- This effect counts as a "Shield Management" effect\n- Lose Stack when losing Shield\n- Turn End: Lose 1 Count
   PL: - Maks. Siły: 999\n- Początkowy Licznik: 2\n- Nie może ulec Oszołomieniu\n- Na początku tury Część zyskuje Tarczę równą liczbie ładunków\n- Ten efekt liczy się jako efekt zarządzania Tarczą\n- Gdy traci Tarczę, traci też ładunki\n- Na koniec tury traci 1 Licznika
326. [Słowo kluczowe [NoirShieldUp] — tekst klimatyczny] 검은 신. 검은 거인. 망치의 신부. 보존의 권능을 담당하는 백화점의 검은 신이 가장 직접적인 접촉적 가호. 망치는 단단하며 검은색은 모든것을 흡수하여 정지시킨다. 마치 죽음의 속성처럼.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldUp].flavor
   limit: do 390 znaków
   EN: The Obsidian God. The Obsidian Giant. The Chaplain of the Hammer. The Obsidian God of the Grand Magasin, whose domain is the power of preservation, grants his blessing through direct contact. The hammer is hard, and its black hue absorbs all things and brings them to a halt... much like death itself.
   PL: Czarny Bóg. Czarny Gigant. Kapłan Młota. Czarny Bóg Grand Magasin, odpowiedzialny za władzę Zachowania, udziela błogosławieństwa w formie bezpośredniego dotyku. Młot jest twardy, a czerń pochłania wszystko i sprowadza do zastoju... niczym śmierć.
327. [Słowo kluczowe [NoirShieldPiece] — nazwa] 묵시적 형벌
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldPiece].name
   kontekst: identyfikator tagu w tekstach: `[NoirShieldPiece]`
   limit: do 40 znaków
   EN: Apocalyptic Vengeance
   PL: Apokaliptyczna Zemsta
328. [Słowo kluczowe [NoirShieldPiece] — opis] - 최댓값 : 2\n- 받는 피해량 -10%\n- 수치가 2면, 최종 위력 -2
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldPiece].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take -10% damage\n- At 2 Stacks, Final Power -2
   PL: - Maks. ładunków: 2\n- Otrzymuje obrażenia -10%\n- Przy 2 ładunkach Moc Końcowa -2
329. [Słowo kluczowe [NoirShieldPiece] — tekst klimatyczny] 가상의 질량 조각이 몸을 짓누르는듯하다. 거인의 형벌을 유사하게 구현한것. 언약에 따르면 높은곳으로 향하는것은 무거운 돌을 떠안고 묵묵히 오르는 형벌과 같다고 한다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirShieldPiece].flavor
   limit: do 300 znaków
   EN: It feels as though a fragment of imaginary mass is pressing down upon the body—a crude imitation of a Giant's punishment. According to the covenant, ascending to a higher place is akin to bearing a heavy boulder and climbing in silence.
   PL: Ciało zdaje się uciskać kawałek urojonej masy — prymitywne naśladowanie kary Giganta. Według Przymierza wstępowanie w górę niczym jest ponoszeniem ciężkiego głazu i milczącym wstępowaniem.
330. [Słowo kluczowe [VibrationResonance] — nazwa] 보존 상쇄
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=VibrationResonance].name
   kontekst: identyfikator tagu w tekstach: `[VibrationResonance]`
   limit: do 40 znaków
   EN: Negation of Conservation
   PL: Negacja Zachowania
331. [Słowo kluczowe [VibrationResonance] — opis] - 최댓값 : 2\n- 진동 폭발로 받는 피해량, 흐트러짐 피해량 -90%\n- 가하는 피해량 +20%\n- 턴 종료시 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=VibrationResonance].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take -90% damage from Tremor Burst; -90% to Stagger Threshold raised\n- Deal +20% damage\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 2\n- Otrzymuje -90% obrażeń od Wyładowania Wstrząsu i -90% obniżenia Progu Oszołomienia\n- Zadaje obrażenia +20%\n- Na koniec tury traci 1 ładunek
332. [Słowo kluczowe [VibrationResonance] — tekst klimatyczny] 보존하고자하는 그 모든 움직임에 대한 반대 파장으로의 흔들림은 보존이 성립되지 못하게 한다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=VibrationResonance].flavor
   limit: do 170 znaków
   EN: A counterwave set against every motion that seeks preservation shakes preservation itself apart, preventing it from taking hold.
   PL: Przeciwfalowanie wobec każdego ruchu, który chce coś zachować, wstrząsa Zachowaniem tak, że nie może się utrwalić.
333. [Słowo kluczowe [NoirField] — nazwa] 보존 신역
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirField].name
   kontekst: identyfikator tagu w tekstach: `[NoirField]`
   limit: do 40 znaków
   EN: Sanctum of Conservation
   PL: Sanktuarium Zachowania
334. [Słowo kluczowe [NoirField] — opis] - 최댓값 : 2\n- 턴 시작 시, 잃은 체력 20%당 위력 증가 1, 피해량 증가 1 얻음 (각각 최대 3)\n- 턴 시작시 모든 누아르 소속 아군의 스킬 최종 위력이 이 버프 수치만큼 증가\n\n- 수치가 1 이상이면, 턴 시작시 자신을 포함한 누아르 소속인 모든 대상에게 아래 효과 적용\n· 정신력 +10\n· 공격 위력 +2\n· 방어 레벨 +2\n\n- 수치가 2 이상이면, 턴 시작시 누아르 소속이 아닌 모든 적에게 아래 효과 적용\n· 속도 최댓값 -1\n· 공격 레벨 -6\n· 방어 레벨 -2
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirField].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn Start: Gain 1 Power Up and 1 Damage Up for every 20% missing HP (max 3 respectively)\n- Turn Start: All "Le Noir" allies' Skills gain Final Power equal to Stack\n\n- Turn Start: At 1+ Stack, apply the following effects to all "Le Noir" allies, including this unit:\n · SP +10\n · Attack Power +2\n · Defense Level +2\n\n- Turn Start: At 2+ Stacks, apply the following effects to all non-"Le Noir" enemies:\n · Max Speed -1\n · Offense Level -6\n · Defense Level -2
   PL: - Maks. ładunków: 2\n- Na początku tury zyskuje 1 Wzrost Mocy i 1 Wzrost Obrażeń za każde 20% utraconego HP (każdy maks. 3)\n- Na początku tury Umiejętności wszystkich sojuszników z Le Noir zyskują Moc Końcową równą liczbie ładunków tego efektu\n\n- Przy 1 lub więcej ładunkach na początku tury stosuje następujące efekty na wszystkich jednostkach z Le Noir, włącznie z sobą:\n· Poczytalność +10\n· Moc Ataku +2\n· Poziom Obrony +2\n\n- Przy 2 lub więcej ładunkach na początku tury stosuje następujące efekty na wszystkich wrogach bez Le Noir:\n· Maks. Szybkość -1\n· Poziom Ataku -6\n· Poziom Obrony -2
335. [Słowo kluczowe [NoirField] — tekst klimatyczny] 르누아르가 추구하는 보존의 가치가 보존되는 영역. 보존하는것을 보존하기위한 모든 르누아르적 행동이 이 영역안에서 이롭게 보존된다.이 영역은 영원한 보존의 영역이자 죽음에 한없이 가까워지고자하는 충동이 자극되는 영역이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirField].flavor
   limit: do 320 znaków
   EN: A sanctuary in which the value of conservation pursued by Le Noir is preserved. Within it, the Noirs' preservative actions are retained to their benefit. It is a realm of eternal conservation—a place that stirs the drive to infinitely approach death.
   PL: Obszar, w którym zachowywana jest wartość Zachowania dążona przez Le Noir. Wszystkie działania Le Noir, które zachowują to, co zachowujące, utrwala się tu na korzyść. To sfera wiecznego Zachowania — i sfera, w której pobudzany jest popęd nieskończonego zbliżania się do śmierci.
336. [Słowo kluczowe [NoirSquareCollapse] — nazwa] 진형 붕괴
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirSquareCollapse].name
   kontekst: identyfikator tagu w tekstach: `[NoirSquareCollapse]`
   limit: do 40 znaków
   EN: Formation Collapse
   PL: Rozpad Szyku
337. [Słowo kluczowe [NoirSquareCollapse] — opis] - 최댓값 : 10\n- 수치만큼 방어 레벨 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirSquareCollapse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Lose Defense Level equal to Stack
   PL: - Maks. ładunków: 10\n- Traci Poziom Obrony równy liczbie ładunków
338. [Słowo kluczowe [NoirSquareCollapse] — tekst klimatyczny] 각자가 맡은 바를 자리에서 충실히 이행할거라 생각한 믿음이 무너질때 균열에서 의심이 싹튼다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirSquareCollapse].flavor
   limit: do 170 znaków
   EN: When faith—the faith that each will dutifully carry out their assigned role—begins to crumble, doubt takes root in the cracks.
   PL: Gdy wierzenie — że każdy sumiennie wypełni powierzoną mu rolę — zaczyna się kruszyć, w pęknięciach kiełkuje podejrzenie.
339. [Słowo kluczowe [NoirNail] — nazwa] 약속된 못
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirNail].name
   kontekst: identyfikator tagu w tekstach: `[NoirNail]`
   limit: do 40 znaków
   EN: Promised Nail
   PL: Obiecany Gwóźdź
340. [Słowo kluczowe [NoirNail] — opis] - 최댓값 : 3\n- 자신에게 진동 폭발 발생 시,\n· 자신의 진동 위력만큼 나태 피해를 입음\n· 취약 1 얻음\n· 수치 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirNail].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When Tremor Burst is triggered on this unit,\n · Take Sloth damage equal to Tremor Potency on self\n · Gain 1 Fragile\n · Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Gdy na tej jednostce wywołane zostaje Wyładowanie Wstrząsu,\n· otrzymuje obrażenia Lenistwa równe własnej Siły Wstrząsu\n· zyskuje 1 Wrażliwości\n· traci 1 ładunek
341. [Słowo kluczowe [NoirNail] — tekst klimatyczny] 약속의 망치는 반드시 못을 박기로 약속됐다. 그렇기에 망치가 휘둘러진다면 그곳에 못이 없더라도 못이 있어야한다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=NoirNail].flavor
   limit: do 190 znaków
   EN: The promised hammer is bound by promise to drive in a nail. Therefore, whenever the hammer falls, a nail must exist there... even if there is none.
   PL: Obiecany Młot został zaprzysiężony do przybijania gwoździ. Dlatego gdy młot zamachnie się, tam musi być gwóźdź — nawet jeśli go nie ma.
342. [Słowo kluczowe [BuffetField] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField].name
   kontekst: identyfikator tagu w tekstach: `[BuffetField]`
   limit: do 40 znaków
   EN: Le Vomissement
   PL: Le Vomissement
343. [Słowo kluczowe [BuffetField] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨\n· 1단계 : 뿌이\n· 2단계 : 모든 아군 수감자에게 적용\n· 3단계 : 모든 대상에게 적용
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - After entering the Encounter, Le Vomissement's influence expands at Turn Start every 2 turns\n· Stage 1: Pwie\n· Stage 2: All allied Sinners\n· Stage 3: All targets
   PL: - Po pojawieniu się w walce co 2 tury na początku tury obszar wpływu Le Vomissement się rozszerza\n· Etap 1: Pwie\n· Etap 2: wszyscy sojusznicy Grzesznicy\n· Etap 3: wszystkie jednostki
344. [Słowo kluczowe [BuffetField] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What is devoured for survival, for growth, incorporates what was outside into what is mine. Then it is expelled once more, and what was mine becomes part of the outside.\n\nIt is cyclical, expansive, and consumptive.
   PL: To, co pożerano, by przetrwać i rosnąć, czyniło z zewnątrz wnętrze — „moje”. Potem zostaje wyrzucone ponownie, a „moje” znów staje się „zewnętrznym”. To cykl, ekspansja i wyczerpanie.
345. [Słowo kluczowe [BuffetField_0] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_0].name
   kontekst: identyfikator tagu w tekstach: `[BuffetField_0]`
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Słowo kluczowe [BuffetField_0] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_0].desc
   limit: do 130 znaków
   EN: - After entering the Encounter, Le Vomissement's influence expands at Turn Start every 2 turns
   PL: - Po pojawieniu się w walce co 2 tury na początku tury obszar wpływu Le Vomissement się rozszerza
347. [Słowo kluczowe [BuffetField_0] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_0].flavor
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Słowo kluczowe [BuffetField_1] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_1].name
   kontekst: identyfikator tagu w tekstach: `[BuffetField_1]`
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Słowo kluczowe [BuffetField_1] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_1].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Słowo kluczowe [BuffetField_1] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_1].flavor
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Słowo kluczowe [BuffetField_2] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_2].name
   kontekst: identyfikator tagu w tekstach: `[BuffetField_2]`
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Słowo kluczowe [BuffetField_2] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_2].desc
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Słowo kluczowe [BuffetField_2] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetField_2].flavor
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Słowo kluczowe [GourmandiseAlly] — nazwa] 폭주
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GourmandiseAlly].name
   kontekst: identyfikator tagu w tekstach: `[GourmandiseAlly]`
   (powtórzenie elementu 210 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Słowo kluczowe [GourmandiseAlly] — opis] - 기본 위력 +1, 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 자신의 출혈 3당, 가하는 피해량 +5% (최대 30%), 대상의 체력 회복량 +10% (최대 100%, 소수점 버림)\n- 흐트러짐 상태가 되지 않으며, 출혈로 받는 피해량 -90% (강제 흐트러짐 제외)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GourmandiseAlly].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Power +1, convert all Coins on all Skills into Unbreakable Coins\n- Deal +5% damage for every 3 Bleed on self (max 30%); heal +10% more HP on target (max 100%, rounded down)\n- Cannot be Staggered; take -90% damage from Bleed (excluding forced Staggers)\n- Turn End: Lose 1 Stack
   PL: - Moc Bazowa +1, wszystkie Monety wszystkich Umiejętności stają się Niezniszczalnymi Monetami\n- Zadaje obrażenia +5% za każde 3 własne Krwawienia (maks. 30%); leczy cele o 10% więcej HP (maks. 100%, zaokrąglane w dół)\n- Nie może ulec Oszołomieniu; otrzymuje -90% obrażeń od Krwawienia (z wyłączeniem wymuszonych Oszołomień)\n- Na koniec tury traci 1 ładunek
356. [Słowo kluczowe [GourmandiseAlly] — podsumowanie] 스킬이 강화됨
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GourmandiseAlly].summary
   limit: do 120 znaków
   EN: Skills are strengthened
   PL: Umiejętności są wzmocnione
357. [Słowo kluczowe [BloodyMucusAlly] — nazwa] 세례[적]
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BloodyMucusAlly].name
   kontekst: identyfikator tagu w tekstach: `[BloodyMucusAlly]`
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Słowo kluczowe [BloodyMucusAlly] — opis] - 최댓값 : 3\n- 공격 스킬 사용 시, 수치만큼 자신의 출혈 횟수 증가 (스킬당 1회)\n- 수비 스킬 사용 시, 수치 1 감소\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BloodyMucusAlly].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- On Attack Skill Use, gain Bleed Count equal to Stack (once per Skill)\n- On Defense Skill Use, lose 1 Stack\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Umiejętności ataku zyskują Licznik Krwawienia równy ładunkom (1 raz na Umiejętność)\n- Przy użyciu Umiejętności obrony traci 1 ładunek\n- Na koniec tury traci 1 ładunek
359. [Słowo kluczowe [BuffetGold] — nazwa] 황금계시
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGold].name
   kontekst: identyfikator tagu w tekstach: `[BuffetGold]`
   limit: do 40 znaków
   EN: Golden Revelation
   PL: Złote Objawienie
360. [Słowo kluczowe [BuffetGold] — opis] - 최댓값 : 5\n- 수치 1당, 받는 피해량 +5%\n- 수치가 최댓값이면, 출혈이 있을 때 받는 피해량 +10%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGold].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed: 5\n- Take +5% damage for every Stack\n- At max Stack, take +10% damage if this unit has Bleed
   PL: - Maks. ładunków: 5\n- Otrzymuje obrażenia +5% za każdy ładunek\n- Przy Maks. ładunków, jeżeli posiada Krwawienie, otrzymuje obrażenia +10%
361. [Słowo kluczowe [BuffetGold] — tekst klimatyczny] 금빛은 아이를 인도한다. 다음은 누구를 해해야하는지. 그 유도에도 아이는 그 판단이 자신의 선택이라 여기게 된다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGold].flavor
   limit: do 200 znaków
   EN: The golden light guides the child toward whom they should harm next. Even under that guidance, the child believes the judgment to be entirely their own.
   PL: Złota poświata wskazuje dziecku, kogo skrzywdzić następnym razem. A mimo tej wskazówki dziecko wierzy, że wyrok jest w całości jego własnym wyborem.
362. [Słowo kluczowe [BuffetShoes] — nazwa] 분홍색 메리 제인
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetShoes].name
   kontekst: identyfikator tagu w tekstach: `[BuffetShoes]`
   limit: do 40 znaków
   EN: Pink Mary Janes
   PL: Różowe Mary Jane
363. [Słowo kluczowe [BuffetShoes] — opis] - 속도 최솟값 +3, 최댓값 +3
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetShoes].desc
   limit: do 120 znaków
   EN: - Min & Max Speed +3
   PL: - Min. Szybkość +3, Maks. Szybkość +3
364. [Słowo kluczowe [BuffetShoes] — tekst klimatyczny] 신발… 고마워. 이걸 신으면 어디든 갈수있는거야? 같이 여행… 가고 싶어.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetShoes].flavor
   limit: do 120 znaków
   EN: Thanks... for the shoes. Can I go anywhere if I put these on? I wanna... travel with you.
   PL: Buty... dziękuję. Czy w nich mogę pójść dokądkolwiek? Chcę... pojechać z tobą w podróż.
365. [Słowo kluczowe [BuffetGoldenClothes] — nazwa] 황금 수의
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGoldenClothes].name
   kontekst: identyfikator tagu w tekstach: `[BuffetGoldenClothes]`
   limit: do 40 znaków
   EN: Golden Shroud
   PL: Złoty Całun
366. [Słowo kluczowe [BuffetGoldenClothes] — opis] - 방어 레벨 +10\n- 턴 종료 시 흐트러짐 상태이면, 흐트러짐 상태를 해제하고 최대 체력의 50%만큼 체력 회복 (전투당 1회)
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGoldenClothes].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +10\n- Turn End: If this unit is Staggered, recover from Stagger and heal 50% HP (once per Encounter)
   PL: - Poziom Obrony +10\n- Na koniec tury, jeżeli jednostka jest oszołomiona, wychodzi z Oszołomienia i odzyskuje 50% Maks. HP (1 raz na walkę)
367. [Słowo kluczowe [BuffetGoldenClothes] — tekst klimatyczny] 아이는 어른의 옷을 걸쳤다. 다른 옷도아닌 누군가의 죽음으로 만들어진 가죽 옷이기에  어른으로 한걸음 나아갈수있다.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=BuffetGoldenClothes].flavor
   limit: do 220 znaków
   EN: The child has donned the clothes of an adult. Not just any clothes, but a hide garment made from another's death. And so, the child takes one step closer to adulthood.
   PL: Dziecko przyodziało ubrania dorosłego. Nie byle jakie — szatę ze skóry zrobioną z czyjejś śmierci. I tak dziecko robi o krok bliżej dorosłości.
368. [Słowo kluczowe [Buffet_LowMorale] — nazwa] 잊혀지지 않은 아픔
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=Buffet_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Buffet_LowMorale]`
   limit: do 40 znaków
   EN: Unforgotten Pain
   PL: Niezapomniany Ból
369. [Słowo kluczowe [Buffet_LowMorale] — opis] - 사기 저하\n- 보호 3 얻음
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=Buffet_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 3 Protection
   PL: - Niskie Morale\n- Zyskuje 3 Ochrony
370. [Słowo kluczowe [Buffet_Panic] — nazwa] 잊혀지지 않은 아픔
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=Buffet_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Buffet_Panic]`
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Słowo kluczowe [Buffet_Panic] — opis] - 패닉\n- 보호 5 얻음
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=Buffet_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 5 Protection
   PL: - Panika\n- Zyskuje 5 Ochrony
372. [Słowo kluczowe [RestrictMob] — nazwa] 규칙: 원피 손상 금지
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictMob].name
   kontekst: identyfikator tagu w tekstach: `[RestrictMob]`
   limit: do 50 znaków
   EN: Rule: Raw Hide Damage Prohibited
   PL: Zasada: Zakaz Uszkadzania Surowej Skóry
373. [Słowo kluczowe [RestrictMob] — opis] 무두질된 죄수에게 공격 스킬을 지정하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictMob].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When Tanned Prisoner is targeted with an Attack Skill, this effect expires, and the attacker gains 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Gdy na początku walki Umiejętność ataku celuje w Wygarbowanego Więźnia, ten efekt znika, a atakujący zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
374. [Słowo kluczowe [RestrictBoss] — nazwa] 규칙: 무두질 재촉 금지
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictBoss].name
   kontekst: identyfikator tagu w tekstach: `[RestrictBoss]`
   limit: do 50 znaków
   EN: Rule: Tanning Rush Prohibited
   PL: Zasada: Zakaz Ponaglania Garbowania
375. [Słowo kluczowe [RestrictBoss] — opis] 통제자에게 공격 스킬을 지정하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictBoss].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When the Overseer is targeted with an Attack Skill, this effect expires, and the attacker gains 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Gdy na początku walki Umiejętność ataku celuje w Nadzorcę, ten efekt znika, a atakujący zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
376. [Słowo kluczowe [RestrictTier1] — nazwa] 규칙: 공격적 태도 금지
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictTier1].name
   kontekst: identyfikator tagu w tekstach: `[RestrictTier1]`
   limit: do 50 znaków
   EN: Rule: Offensive Behavior Prohibited
   PL: Zasada: Zakaz Postawy Ofensywnej
377. [Słowo kluczowe [RestrictTier1] — opis] 공격 스킬을 장착하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음 (EGO 스킬 제외)\n턴 종료시 이 버프 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictTier1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When an Attack Skill is equipped, this effect expires and gain 1 Tannery Rule Violation (excluding E.G.O Skills)\n- Turn End: This effect expires
   PL: Jeżeli na początku walki wyposażono Umiejętność ataku, ten efekt znika, a jednostka zyskuje 1 Naruszenia Zasad Garbarni (z wyłączeniem Umiejętności E.G.O)\nNa koniec tury ten efekt znika
378. [Słowo kluczowe [RestrictDef] — nazwa] 규칙: 방어적 태도 금지
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictDef].name
   kontekst: identyfikator tagu w tekstach: `[RestrictDef]`
   limit: do 50 znaków
   EN: Rule: Defensive Behavior Prohibited
   PL: Zasada: Zakaz Postawy Defensywnej
379. [Słowo kluczowe [RestrictDef] — opis] 수비 스킬을 장착하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictDef].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When a Defense Skill is equipped, this effect expires and gain 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Jeżeli na początku walki wyposażono Umiejętności obrony, ten efekt znika, a jednostka zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
380. [Słowo kluczowe [RestrictDenied] — nazwa] 태너리 규칙 위반
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictDenied].name
   kontekst: identyfikator tagu w tekstach: `[RestrictDenied]`
   limit: do 40 znaków
   EN: Tannery Rule Violation
   PL: Naruszenie Zasad Garbarni
381. [Słowo kluczowe [RestrictDenied] — opis] 최댓값 : 1\n통제자에게 받는 피해량 +30%\n자신의 공격 종료시, 통제자가 자신에게 ‘퍼니싱 버니싱 피니싱’ 스킬을 사용하고 버프 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictDenied].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +30% damage from the Overseer\n- At this unit's Attack End, the Overseer uses the "Punishing Burnishing Finishing" Skill on this unit; then, this effect expires
   PL: Maks. ładunków: 1\nOtrzymuje od Nadzorce obrażenia +30%\nPo zakończeniu ataku tej jednostki Nadzorca używa na niej Umiejętności „Punishing Burnishing Finishing”, po czym efekt znika
382. [Słowo kluczowe [RestrictDenied] — tekst klimatyczny] 대상은 이 세계에 정의된 규칙을 위반한 죄인
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictDenied].flavor
   limit: do 120 znaków
   EN: The target is a transgressor who has violated the rules by which this world is bound.
   PL: Cel jest grzesznikiem, który naruszył reguły, którymi świat ten jest związany.
383. [Słowo kluczowe [B3FreshMob] — nazwa] 주름잡히지 않은 가죽
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=B3FreshMob].name
   kontekst: identyfikator tagu w tekstach: `[B3FreshMob]`
   limit: do 40 znaków
   EN: Uncreased Hide
   PL: Skóra Bez Zagnieceń
384. [Słowo kluczowe [B3FreshMob] — opis] 최댓값 : 1\n턴 시작시 보호막 20 얻음\n턴 시작시 보호 2 얻음\n턴 종료시 소멸
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=B3FreshMob].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn Start: Gain 20 Shield\n- Turn End: Gain 2 Protection\n- Expires at Turn End
   PL: Maks. ładunków: 1\nNa początku tury zyskuje 20 Tarczy\nNa początku tury zyskuje 2 Ochrony\nZnika na koniec tury
385. [Słowo kluczowe [B3FreshMob] — tekst klimatyczny] 다룰 때 조심해주세요. 가죽 옷을 시착하고 몸을 구부리면 주름이 생겨버려 가치가 떨어지니까요.
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=B3FreshMob].flavor
   limit: do 160 znaków
   EN: Please handle with care. If you try on a hide garment and bend too much, it will crease... and that lowers its worth.
   PL: Proszę obchodzić się ostrożnie. Gdy przymierzysz szatę ze skóry i nadmiernie sięgniesz, powstaną zagniecenia... a to obniża jej wartość.
386. [Słowo kluczowe [RestrictFailed] — nazwa] 규칙의 붕괴
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictFailed].name
   kontekst: identyfikator tagu w tekstach: `[RestrictFailed]`
   limit: do 40 znaków
   EN: Rule Collapse
   PL: Rozpad Zasad
387. [Słowo kluczowe [RestrictFailed] — opis] 공격 레벨 +3\n방어 레벨 -3
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictFailed].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3\n- Defense Level -3
   PL: Poziom Ataku +3\nPoziom Obrony -3
388. [Słowo kluczowe [RestrictFailed] — tekst klimatyczny] 규칙과 법칙의 차이를 아는가?
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RestrictFailed].flavor
   limit: do 120 znaków
   EN: Do you know the difference between a rule and a law?
   PL: Czy wiesz, czym różni się zasada od prawa?
389. [Słowo kluczowe [targetDye_LowMorale] — nazwa] 머신 잼
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=targetDye_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[targetDye_LowMorale]`
   limit: do 40 znaków
   EN: Jammed Machine
   PL: Zacięta Maszyna
390. [Słowo kluczowe [targetDye_LowMorale] — opis] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -5%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=targetDye_LowMorale].desc
   limit: do 120 znaków
   EN: Skills deal -5% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają celom o mniejszej Szybkości niż własna obrażenia -5%
391. [Słowo kluczowe [targetDye_Panic] — nazwa] 머신 잼
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=targetDye_Panic].name
   kontekst: identyfikator tagu w tekstach: `[targetDye_Panic]`
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Słowo kluczowe [targetDye_Panic] — opis] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -10%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=targetDye_Panic].desc
   limit: do 120 znaków
   EN: Skills deal -10% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają celom o mniejszej Szybkości niż własna obrażenia -10%
393. [Słowo kluczowe [targetDye_Panic] — tekst klimatyczny] 자신보다 빠른 것을 고정시킬 수 있는가?
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=targetDye_Panic].flavor
   limit: do 120 znaków
   EN: Can that which moves faster than oneself truly be fixed in place?
   PL: Czy to, co porusza się szybciej od ciebie, da się naprawdę zatrzymać w miejscu?
394. [Słowo kluczowe [RouteBOneLeg] — opis] - 기본 공격 레벨 +25\n- 기본 방어 레벨 +25
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=RouteBOneLeg].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +25\n- Base Defense Level +25
   PL: - Podstawowy Poziom Ataku +25\n- Podstawowy Poziom Obrony +25
395. [Słowo kluczowe [SapsareeGold] — nazwa] 따갑게 내리쬐는 햇살[수셰프]
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SapsareeGold].name
   kontekst: identyfikator tagu w tekstach: `[SapsareeGold]`
   limit: do 60 znaków
   EN: Shower of Stinging Sunshine [Sous Chef]
   PL: Parzące Promienie Słońca [Sous-chef]
396. [Słowo kluczowe [SapsareeGold] — opis] - 스킬 사용 시 대상의 매콤매콤소스 1당, 최종 위력 +1 (최대 3)\n- 자신의 스킬로 아군 처치 시 정신력 15 증가
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SapsareeGold].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Skill Use, Final Power +1 for every "Fiery, Tongue-scorching Sauce" on target (max 3)\n- Gain 15 SP upon killing an ally with this unit's Skill
   PL: - Przy użyciu Umiejętności Moc Końcowa +1 za każdy ładunek „Pikantno-Pikantnego Sosu” na celu (maks. 3)\n- Gdy własna Umiejętność zabije sojusznika, zyskuje 15 Poczytalności
397. [Słowo kluczowe [SapsareeGold] — tekst klimatyczny] ‘수셰프는 마음이 뜨끈한거예요. 자신감이 배부른 거예요!’
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SapsareeGold].flavor
   limit: do 130 znaków
   EN: "Sous-chef has a warm, hearty heart, you hear? Sous-chef is stuffed full of confidence, you hear?!"
   PL: „Sous-chef ma serce gorące, jasne? Sous-chef jest nabity pewnością siebie, jasne?!”
398. [Słowo kluczowe [GoldenManager] — nazwa] 따갑게 내리쬐는 햇살[3층 플로어 매니저]
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenManager].name
   kontekst: identyfikator tagu w tekstach: `[GoldenManager]`
   limit: do 70 znaków
   EN: Shower of Stinging Sunshine [3F Floor Manager]
   PL: Parzące Promienie Słońca [Menedżer Piętra 3]
399. [Słowo kluczowe [GoldenManager] — opis] - 대상의 경계심 1당, 가하는 피해량 +5% (최대 50%)\n- 정신력 0 이하의 대상에게 스킬 사용 시 기본 위력 +3
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenManager].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +5% damage for every Guarded Caution on target (max 50%)\n- Base Power +3 On Skill Use against target that has 0 or less SP
   PL: - Zadaje obrażenia +5% za każdy ładunek Czujności na celu (maks. 50%)\n- Przy użyciu Umiejętności na cel z Poczytalnością 0 lub niższą Moc Bazowa +3
400. [Słowo kluczowe [GoldenManager] — tekst klimatyczny] 햇빛이 뜨겁지만 천들을 떨쳐내지 못하고 마음은 이불속으로… 이불속으로…
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=GoldenManager].flavor
   limit: do 180 znaków
   EN: The sunshine burns hot, yet the cloth cannot be cast aside, and the heart retreats beneath the blankets... deeper beneath the blankets...
   PL: Słońce pali gorąco, lecz kołdry nie da się zrzucić, a serce chowa się pod kołdrę... głębiej pod kołdrę...
401. [Słowo kluczowe [SisyphusSapphire] — nazwa] 사파이어
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusSapphire].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusSapphire]`
   limit: do 40 znaków
   EN: Sapphire
   PL: Szafir
402. [Słowo kluczowe [SisyphusSapphire] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1\n- 최종 위력 +1
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusSapphire].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1\n- Moc Końcowa +1
403. [Słowo kluczowe [SisyphusOnyx] — nazwa] 오닉스
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusOnyx].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusOnyx]`
   limit: do 40 znaków
   EN: Onyx
   PL: Onyks
404. [Słowo kluczowe [SisyphusOnyx] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +2\n- 최종 위력 +1
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusOnyx].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +2\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +2\n- Moc Końcowa +1
405. [Słowo kluczowe [SisyphusDiamond] — nazwa] 다이아몬드
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusDiamond].name
   kontekst: identyfikator tagu w tekstach: `[SisyphusDiamond]`
   limit: do 40 znaków
   EN: Diamond
   PL: Diament
406. [Słowo kluczowe [SisyphusDiamond] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +2\n- 최종 위력 +1\n- 가하는 피해량 +10%
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=SisyphusDiamond].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +2\n- Final Power +1\n- Deal +10% damage
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +2\n- Moc Końcowa +1\n- Zadaje obrażenia +10%
407. [Słowo kluczowe [OutOfControl_LowMorale] — nazwa] 통제 불능
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=OutOfControl_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[OutOfControl_LowMorale]`
   limit: do 40 znaków
   EN: Disabled Overseeing
   PL: Brak Kontroli
408. [Słowo kluczowe [OutOfControl_LowMorale] — opis] - 사기 저하\n스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 공격 위력 감소 1 부여
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=OutOfControl_LowMorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Skill Final Power +1\n- Turn Start: Apply 1 Attack Power Down to all other allies
   PL: - Niskie Morale\nMoc Końcowa Umiejętności +1\nNa początku tury nakłada 1 Spadku Mocy Ataku na wszystkich innych sojuszników
409. [Słowo kluczowe [OutOfControl_Panic] — nazwa] 통제 불능
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=OutOfControl_Panic].name
   kontekst: identyfikator tagu w tekstach: `[OutOfControl_Panic]`
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Słowo kluczowe [OutOfControl_Panic] — opis] - 패닉\n스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 공격 위력 감소 1, 피해량 감소 1 부여
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=OutOfControl_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Skill Final Power +1\n- Turn Start: Apply 1 Attack Power Down and 1 Damage Down to all other allies
   PL: - Panika\nMoc Końcowa Umiejętności +1\nNa początku tury nakłada 1 Spadku Mocy Ataku i 1 Spadku Obrażeń na wszystkich innych sojuszników
411. [Słowo kluczowe [LaNoirSuperior_LowMorale] — nazwa] 첫 껍질속으로…
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LaNoirSuperior_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LaNoirSuperior_LowMorale]`
   limit: do 40 znaków
   EN: Into the First Shell...
   PL: W Głąb Pierwszej Skorupy...
412. [Słowo kluczowe [LaNoirSuperior_LowMorale] — opis] - 사기 저하\n공격 레벨 -2\n방어 레벨 +2
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LaNoirSuperior_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level -2\n- Defense Level +2
   PL: - Niskie Morale\nPoziom Ataku -2\nPoziom Obrony +2
413. [Słowo kluczowe [LaNoirSuperior_Panic] — nazwa] 첫 껍질속으로…
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LaNoirSuperior_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LaNoirSuperior_Panic]`
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Słowo kluczowe [LaNoirSuperior_Panic] — opis] - 패닉\n공격 레벨 -3\n방어 레벨 +4
   źródło: BattleKeywords-a1c10p2.json :: dataList[id=LaNoirSuperior_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level -3\n- Defense Level +4
   PL: - Panika\nPoziom Ataku -3\nPoziom Obrony +4

## Słowa kluczowe bitwy — BattleKeywords-a1c10p3
- plik gry: `BattleKeywords-a1c10p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

415. [Słowo kluczowe [GoldenHideWarderFirstPhase] — nazwa] 박동
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenHideWarderFirstPhase]`
   limit: do 40 znaków
   EN: Thumping Pulse
   PL: Tętnienie
416. [Słowo kluczowe [GoldenHideWarderFirstPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 합 위력 +1, 받는 피해량 -25%\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Clash Power +1, take -25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Starcia +1, otrzymuje obrażenia -25%\n- Na koniec tury znika
417. [Słowo kluczowe [GoldenHideWarderFirstPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].summary
   limit: do 120 znaków
   EN: Gain Clash Power, take less damage
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń
418. [Słowo kluczowe [GoldenHideWarderFirstPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: The domain of life. The will of change and birth.
   PL: Władza życia. Wola zmiany i narodzin.
419. [Słowo kluczowe [GoldenFabricWarderFirstPhase] — nazwa] 정지
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenFabricWarderFirstPhase]`
   limit: do 40 znaków
   EN: Stillness
   PL: Bezruch
420. [Słowo kluczowe [GoldenFabricWarderFirstPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +1, 가하는 피해량 +15%\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +1, deal +15% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +1, zadaje obrażenia +15%\n- Na koniec tury znika
421. [Słowo kluczowe [GoldenFabricWarderFirstPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].summary
   limit: do 120 znaków
   EN: Gain Final Power, deal more damage
   PL: Moc Końcowa rośnie, zadaje więcej obrażeń
422. [Słowo kluczowe [GoldenFabricWarderFirstPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: The domain of death. The urge for conservation and stillness.
   PL: Władza śmierci. Popęd Zachowania i Bezruchu.
423. [Słowo kluczowe [MeursaultBuffWarderFirstPhase] — nazwa] 이방인
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].name
   kontekst: identyfikator tagu w tekstach: `[MeursaultBuffWarderFirstPhase]`
   limit: do 40 znaków
   EN: The Stranger
   PL: Obcy
424. [Słowo kluczowe [MeursaultBuffWarderFirstPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 간수와 합 진행 시,\n· 합 위력 +1\n· 피해량 +(자신의 잃은 체력 비율/2)% (최대 20%)\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 2개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- When Clashing against the Warden:\n · Clash Power +1\n · Deal +(missing HP percentage on self / 2)% damage (max 20%)\n · On Clash Win, gain 1 E.G.O resource for each of the 2 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Podczas Starcia ze Strażnikiem:\n· Moc Starcia +1\n· Zadaje obrażenia +(procent utraconego HP na sobie / 2)% (maks. 20%)\n· Po wygranym Starciu zyskuje w sumie 2 Zasoby E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
425. [Słowo kluczowe [MeursaultBuffWarderFirstPhase] — podsumowanie] 간수와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and deal more damage when Clashing with the Warden\nCannot be Staggered, cannot be defeated when there are other surviving allies
   PL: - Podczas Starcia ze Strażnikiem Moc Starcia i obrażenia rosną\n- Nie zostaje oszołomiony; gdy żyją inni sojusznicy, nie ginie
426. [Słowo kluczowe [MeursaultBuffWarderFirstPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: Was I an alien, a foreign element in both the department store and the City?
   PL: Czy i w Grand Magasin, i w Mieście byłem Obcym — obcym ciałem?
427. [Słowo kluczowe [UnstableConnection] — nazwa] 불안정한 현현
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=UnstableConnection].name
   kontekst: identyfikator tagu w tekstach: `[UnstableConnection]`
   limit: do 40 znaków
   EN: Precarious Theophany
   PL: Chwiejna Teofania
428. [Słowo kluczowe [UnstableConnection] — opis] - 최댓값 : 2\n- 턴 시작 시, (수치 x 4)만큼 합 위력 감소, 취약 얻음\n- 턴 종료 시, (45 - 현재 정신력)/2만큼 정신력 회복(소수점 버림)하고 수치 1 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=UnstableConnection].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn Start: Gain (Stack x 4) Clash Power Down and Fragile\n- Turn End: Heal ((45 - current SP) / 2) SP (rounded down); then, lose 1 Stack
   PL: - Maks. ładunków: 2\n- Na początku tury zyskuje (ładunki x 4) Spadku Mocy Starcia oraz Wrażliwości\n- Na koniec tury odzyskuje Poczytalność ((45 - obecna) / 2) (zaokr. w dół) i traci 1 ładunek
429. [Słowo kluczowe [UnstableConnection] — podsumowanie] 턴 시작 시 합 위력 감소, 취약 얻음\n턴 종료 시 정신력 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=UnstableConnection].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power Down and Fragile at Turn Start\nHeal SP at Turn End
   PL: - Na początku tury traci Moc Starcia i zyskuje Wrażliwość\n- Na koniec tury odzyskuje Poczytalność
430. [Słowo kluczowe [UnstableConnection] — tekst klimatyczny] “어휴. 하필 이럴 때 연결이…”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=UnstableConnection].flavor
   limit: do 120 znaków
   EN: "*sigh* Bad time for connection issues..."
   PL: „No ale co to ma być. Właśnie teraz połączenie…”
431. [Słowo kluczowe [Dominion] — nazwa] 시지프 시스템 보존
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Dominion].name
   kontekst: identyfikator tagu w tekstach: `[Dominion]`
   limit: do 40 znaków
   EN: Sisyphe System Preservation
   PL: Zachowanie Systemu Sisyphe
432. [Słowo kluczowe [Dominion] — opis] - 최댓값 : 25\n- 가하는 피해량 +(수치)% (최대 25%)\n- 받는 피해량 -(수치)% (최대 25%)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Dominion].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 25\n- Deal +(Stack)% damage (max 25%)\n- Take -(Stack)% damage (max 25%)
   PL: - Maks. ładunków: 25\n- Zadaje obrażenia +(ładunki)% (maks. 25%)\n- Otrzymuje obrażenia -(ładunki)% (maks. 25%)
433. [Słowo kluczowe [Dominion] — podsumowanie] 가하는 피해량 증가, 받는 피해량 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Dominion].summary
   limit: do 120 znaków
   EN: Deal more and take less damage
   PL: Zadaje więcej obrażeń i otrzymuje mniej
434. [Słowo kluczowe [Dominion] — tekst klimatyczny] “다른 구역에서 와서 그런가? 왜 이렇게 몰라주는지 모르겠군. 시지프 탑이 무너지면, 말레우스 말레피카룸이니 뭐니 하는 놈들이… 하아.”\n\n“이방인들이 다 그렇지 뭐. N사 사정이나 세상 돌아가는 거엔 관심도 없고. 어휴… 됐다, 됐어. 어디 끝까지 해보자고.”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Dominion].flavor
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Is it because you're from another District or something? How do you people still not get it? If Sisyphe Tower goes down, those Malleus Maleficarum or whatever they're called are going to—*sigh*"\n\n"Same old strangers and outsiders, I suppose. You people don't give two hoots what happens to N Corp. or what the world is coming to. Ugh... never mind. Now let's see just how far you're willing to take this."
   PL: „Bo żeś z innego Dystryktu? Nie pojmuję, czemu nikt tego nie docenia. Jeżeli Wieża Sisyphe runie, to ci tamci Malleus Maleficarum czy jak ich tam... Aaaah.”\n\n„Obcy to obcy. Nie obchodzi ich ani los N Corp., ani to, co się dzieje ze światem. Ufff... przestań, przestań. Zobaczymy, jak daleko zajdziesz.”
435. [Słowo kluczowe [BlackStigmata] — nazwa] 죄악감
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata].name
   kontekst: identyfikator tagu w tekstach: `[BlackStigmata]`
   limit: do 40 znaków
   EN: Compunction
   PL: Poczucie Winy
436. [Słowo kluczowe [BlackStigmata] — opis] - 정신력이 있는 대상이면, 패닉 유형이 '죄악감'으로 변경됨\n- 정신력이 없는 대상이면, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 죄악감 패닉 효과\n- 사기 저하 : 속도 최솟값, 최댓값 -1, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 패닉 : 속도 최솟값, 최댓값 -2, 자신보다 속도가 높은 대상에게 받는 피해량 +15%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Panic Type changes to "Compunction"\n- Non-SP Units: Take +10% damage from targets with faster Speed than self\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Units without SP" conditional to certain enemies that have SP but cannot change their Panic Types\n\n※ Compunction Panic Effect:\n- Low Morale: Min & Max Speed -1; take +10% damage from targets with faster Speed than this unit's\n- Panic: Min & Max Speed -2; take +15% damage from targets with faster Speed than this unit's
   PL: - Jeżeli cel posiada Poczytalność, jego typ Paniki zmienia się na „Poczucie Winy”\n- Jeżeli cel nie posiada Poczytalności, otrzymuje obrażenia +10% od celów o większej Szybkości niż własna\n- Na koniec tury traci 1 ładunek\n- Ten efekt się nie kumuluje — jest odnawiany\n- U pewnych wrogów posiadających Poczytalność, którzy nie mogą zmienić typu Paniki, stosuje się efekt dla celów bez Poczytalności\n\n※ Efekt Paniki „Poczucia Winy”\n- Niskie Morale: Min. i Maks. Szybkość -1; otrzymuje obrażenia +10% od celów o większej Szybkości niż własna\n- Panika: Min. i Maks. Szybkość -2; otrzymuje obrażenia +15% od celów o większej Szybkości niż własna
437. [Słowo kluczowe [BlackStigmata] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose Min & Max Speed\nTake more damage from targets with faster Speed than self
   PL: Traci Min. i Maks. Szybkość\nOtrzymuje więcej obrażeń od celów o większej Szybkości niż własna
438. [Słowo kluczowe [BlackStigmata] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata].flavor
   limit: do 120 znaków
   EN: "You feel your sins crawling on your back."
   PL: „Czujesz, jak grzechy wpełzają ci po plecach.”
439. [Słowo kluczowe [BlackStigmata_Main] — nazwa] 죄악감
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Main].name
   kontekst: identyfikator tagu w tekstach: `[BlackStigmata_Main]`
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Słowo kluczowe [BlackStigmata_Main] — opis] - 정신력이 있는 대상이면, 패닉 유형이 '죄악감'으로 변경됨\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Main].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Change their Panic Type to "Compunction"\n- Turn End: Lose 1 Stack
   PL: - Jeżeli cel posiada Poczytalność, zmienia swój typ Paniki na „Poczucie Winy”\n- Na koniec tury traci 1 ładunek
441. [Słowo kluczowe [BlackStigmata_Main] — podsumowanie] 패닉 유형이 '죄악감'으로 변경
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Main].summary
   limit: do 120 znaków
   EN: Change Panic Type to "Compunction"
   PL: Zmienia typ Paniki na „Poczucie Winy”
442. [Słowo kluczowe [BlackStigmata_Main] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Main].flavor
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Słowo kluczowe [BlackStigmata_Sub] — nazwa] 죄악감
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Sub].name
   kontekst: identyfikator tagu w tekstach: `[BlackStigmata_Sub]`
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Słowo kluczowe [BlackStigmata_Sub] — opis] - 정신력이 없는 대상이면, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Sub].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Non-SP Units: Take +10% damage from targets with faster Speed than self\n- Turn End: Lose 1 Stack
   PL: - Jeżeli cel nie posiada Poczytalności, otrzymuje obrażenia +10% od szybszych celów\n- Na koniec tury traci 1 ładunek
445. [Słowo kluczowe [BlackStigmata_Sub] — podsumowanie] 자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Sub].summary
   limit: do 120 znaków
   EN: Take more damage from targets with faster Speed than self
   PL: Otrzymuje więcej obrażeń od celów o większej Szybkości niż własna
446. [Słowo kluczowe [BlackStigmata_Sub] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Sub].flavor
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Słowo kluczowe [BlackStigmata_LowMorale] — nazwa] 죄악감
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BlackStigmata_LowMorale]`
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Słowo kluczowe [BlackStigmata_LowMorale] — opis] - 사기 저하\n- 속도 최솟값, 최댓값 -1, 자신보다 속도가 높은 대상에게 받는 피해량 +10%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Min & Max Speed -1; take +10% damage from targets with faster Speed than self
   PL: - Niskie Morale\n- Min. i Maks. Szybkość -1; otrzymuje obrażenia +10% od celów o większej Szybkości niż własna
449. [Słowo kluczowe [BlackStigmata_LowMorale] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].summary
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Słowo kluczowe [BlackStigmata_LowMorale] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].flavor
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Słowo kluczowe [BlackStigmata_Panic] — nazwa] 죄악감
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BlackStigmata_Panic]`
   (powtórzenie elementu 435 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Słowo kluczowe [BlackStigmata_Panic] — opis] - 패닉\n- 속도 최솟값, 최댓값 -2, 자신보다 속도가 높은 대상에게 받는 피해량 +15%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Min & Max Speed -2; take +15% damage from targets with faster Speed than self
   PL: - Panika\n- Min. i Maks. Szybkość -2; otrzymuje obrażenia +15% od celów o większej Szybkości niż własna
453. [Słowo kluczowe [BlackStigmata_Panic] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Panic].summary
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Słowo kluczowe [BlackStigmata_Panic] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BlackStigmata_Panic].flavor
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Słowo kluczowe [GoldenHideWarderSecondPhase] — nazwa] 박동
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenHideWarderSecondPhase]`
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Słowo kluczowe [GoldenHideWarderSecondPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 이 효과를 보유한 수감자가 간수의 <color=#ff6000><mark=#ff000040><b><u>‘사형 집행’</u></b></mark></color> 스킬과 <color=#ff6000><mark=#ff000040><b><u>합하여 승리</u></b></mark></color>했으면, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 250%만큼 보호막</u></b></mark></color> 얻음 (간수의 ‘사형 집행’ 공격 종료 시, 이 효과로 얻은 보호막 수치만큼 수감자가 보유한 보호막에서 차감함)\n- 합 위력 +2, 받는 피해량 -25%\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Turn Start: A random Sinner gains this effect\n- On Clash Win, if the Sinner who has this effect <color=#ff6000><mark=#ff000040><b><u>won the Clash</u></b></mark></color> against the Warden's <color=#ff6000><mark=#ff000040><b><u>"Death Unto the Condemned"</u></b></mark></color> Skill, gain <color=#ff6000><mark=#ff000040><b><u>Shield equal to 250% of the Sinner's max HP</u></b></mark></color> (Shield gained from this effect is removed from the Sinner's total Shield at Attack End of the Warden's "Death Unto the Condemned")\n- Clash Power +2, take -25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Jeżeli Grzesznik posiadający ten efekt <color=#ff6000><mark=#ff000040><b><u>wygrywa Starcie</u></b></mark></color> z Umiejętnością Strażnika <color=#ff6000><mark=#ff000040><b><u>„Śmierć Skazanym”</u></b></mark></color>, zyskuje <color=#ff6000><mark=#ff000040><b><u>Tarczę równą 250% Maks. HP Grzesznika</u></b></mark></color> (po zakończeniu ataku „Śmierć Skazanym” Strażnika odejmuje z Tarczy Grzesznika tyle, ile wynosiła Tarcza z tego efektu)\n- Moc Starcia +2, otrzymuje obrażenia -25%\n- Na koniec tury znika
457. [Słowo kluczowe [GoldenHideWarderSecondPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소\n'사형 집행'과 합 승리 시 보호막 얻음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and take less damage\nOn Clash Win against "Death Unto the Condemned", gain Shield
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń\nPo wygranym Starciu z Umiejętnością „Śmierć Skazanym” zyskuje Tarczę
458. [Słowo kluczowe [GoldenHideWarderSecondPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].flavor
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Słowo kluczowe [GoldenFabricWarderSecondPhase] — nazwa] 정지
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenFabricWarderSecondPhase]`
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Słowo kluczowe [GoldenFabricWarderSecondPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +2, 가하는 피해량 +25%\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +2, deal +25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +2, zadaje obrażenia +25%\n- Na koniec tury znika
461. [Słowo kluczowe [GoldenFabricWarderSecondPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].summary
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Słowo kluczowe [GoldenFabricWarderSecondPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].flavor
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Słowo kluczowe [MeursaultBuffWarderSecondPhase] — nazwa] 이방인
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[MeursaultBuffWarderSecondPhase]`
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Słowo kluczowe [MeursaultBuffWarderSecondPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 속도 최솟값, 최댓값 +1\n- 간수와 합 진행 시,\n· 합 위력 +2\n· 피해량 +(자신의 잃은 체력 비율/2)% (최대 40%)\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 2 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Min & Max Speed +1\n- When Clashing against the Warden:\n · Clash Power +2\n · Deal +(missing HP percentage on self / 2)% damage (max 40%)\n · On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 2 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Min. i Maks. Szybkość +1\n- Podczas Starcia ze Strażnikiem:\n· Moc Starcia +2\n· Zadaje obrażenia +(procent utraconego HP na sobie / 2)% (maks. 40%)\n· Po wygranym Starciu zyskuje w sumie 3 Zasoby E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 2 Wzrostu Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
465. [Słowo kluczowe [MeursaultBuffWarderSecondPhase] — podsumowanie] 간수와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].summary
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Słowo kluczowe [MeursaultBuffWarderSecondPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].flavor
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Słowo kluczowe [EncompassingVoiceSecondPhase] — nazwa] 검은 신의 목소리
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[EncompassingVoiceSecondPhase]`
   limit: do 40 znaków
   EN: Voice of the Obsidian God
   PL: Głos Czarnego Boga
468. [Słowo kluczowe [EncompassingVoiceSecondPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 40, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 턴 종료 시, 10 증가\n- 수치가 100이 되면, 다음 턴에 검은 신의 권능으로 변경됨
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up for every 20 Stacks (max 4)\n- Gain Stack equal to Preservation Count this unit consumes or gains due to its Skill effects (max 40 per turn; this effect's Stack is gained regardless of Preservation's max Count)\n- Turn End: Gain 10 Stacks\n- At 100 Stacks, convert this effect into "Divinity of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 20 ładunków (maks. 4)\n- Gdy przez Umiejętności tej jednostki zużyty albo zdobyty zostaje Licznik Zachowania, zyskuje ładunki w tej liczbie (maks. 40 na turę, łącznie z liczbą ponad Maks. licznika Zachowania)\n- Na koniec tury zyskuje 10 ładunków\n- Przy 100 ładunkach w następnej turze zamienia się w „Wszechmoc Czarnego Boga”
469. [Słowo kluczowe [EncompassingVoiceSecondPhase] — podsumowanie] 수치에 따라 공격 레벨 증가\n수치가 최대가 되면 검은 신의 권능으로 변경
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level based on Stack\nAt max Stack, converted into "Divinity of the Obsidian God"
   PL: Poziom Ataku rośnie zależnie od ładunków\nPrzy Maks. ładunków zamienia się w „Wszechmoc Czarnego Boga”
470. [Słowo kluczowe [EncompassingVoiceSecondPhase] — tekst klimatyczny] 보존의 규율을 설파하는 목소리.\n다시 야만으로 돌아갈 수는 없다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A voice preaching the Rule of Conservation.\nThere can be no return to barbarism.
   PL: Głos, który głosi Regułę Zachowania.\nPowrotu do barbarzyństwa nie może być.
471. [Słowo kluczowe [EncompassingVoiceThirdPhase] — nazwa] 검은 신의 목소리
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[EncompassingVoiceThirdPhase]`
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Słowo kluczowe [EncompassingVoiceThirdPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 40, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 턴 종료 시, 10 증가\n- 수치가 100이 되면, 다음 턴에 검은 신의 권능으로 변경됨
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].desc
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Słowo kluczowe [EncompassingVoiceThirdPhase] — podsumowanie] 수치에 따라 공격 레벨 증가\n수치가 최대가 되면 검은 신의 권능으로 변경
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].summary
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Słowo kluczowe [EncompassingVoiceThirdPhase] — tekst klimatyczny] 보존의 규율을 설파하는 목소리.\n다시 야만으로 돌아갈 수는 없다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].flavor
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Słowo kluczowe [SpreadingVoiceSecondPhase] — nazwa] 검은 신의 권능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[SpreadingVoiceSecondPhase]`
   limit: do 40 znaków
   EN: Divinity of the Obsidian God
   PL: Wszechmoc Czarnego Boga
476. [Słowo kluczowe [SpreadingVoiceSecondPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 스킬의 코인이 파괴 불가 코인으로 변경됨\n- 수치가 0이 되면, 다음 턴에 검은 신의 목소리로 변경됨
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 respectively)\n- Convert all Skill Coins into Unbreakable Coins\n- At 0 Stacks, convert this effect into "Voice of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Przy 0 ładunkach w następnej turze zamienia się w „Głos Czarnego Boga”
477. [Słowo kluczowe [SpreadingVoiceSecondPhase] — podsumowanie] 모든 스킬의 코인이 파괴 불가 코인으로 변경\n수치에 따라 공격 레벨, 방어 레벨 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Convert all Skill Coins into Unbreakable Coins\nGain Offense Level and Defense Level based on Stack
   PL: Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\nPoziom Ataku i Poziom Obrony rosną zależnie od ładunków
478. [Słowo kluczowe [SpreadingVoiceSecondPhase] — tekst klimatyczny] 검은 신. 시지프 시스템에서 창조와 시간을 관장한다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].flavor
   limit: do 120 znaków
   EN: The Obsidian God—He whose domain is creation and time itself within the Sisyphe System.
   PL: Czarny Bóg. W Systemie Sisyphe to on zawiaduje tworzeniem i czasem.
479. [Słowo kluczowe [SpreadingVoiceThirdPhase] — nazwa] 검은 신의 권능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[SpreadingVoiceThirdPhase]`
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Słowo kluczowe [SpreadingVoiceThirdPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 스킬의 코인이 파괴 불가 코인으로 변경됨 (적출 코인 제외)\n- 수치가 0이 되면, 다음 턴에 검은 신의 목소리로 변경됨
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 respectively)\n- Convert all Skill Coins into Unbreakable Coins (excluding Excision Coins)\n- At 0 Stacks, convert this effect into "Voice of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami (z wyłączeniem Monet Wycięcia)\n- Przy 0 ładunkach w następnej turze zamienia się w „Głos Czarnego Boga”
481. [Słowo kluczowe [SpreadingVoiceThirdPhase] — podsumowanie] 모든 스킬의 코인이 파괴 불가 코인으로 변경 (적출 코인 제외)\n수치에 따라 공격 레벨, 방어 레벨 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Convert all Skill Coins into Unbreakable Coins (excluding Excision Coins)\nGain Offense Level and Defense Level based on Stack
   PL: Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami (z wyłączeniem Monet Wycięcia)\nPoziom Ataku i Poziom Obrony rosną zależnie od ładunków
482. [Słowo kluczowe [SpreadingVoiceThirdPhase] — tekst klimatyczny] 검은 신. 시지프 시스템에서 창조와 시간을 관장한다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].flavor
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Słowo kluczowe [LeaderVoiceSecondPhase] — nazwa] 시지프 형벌의 간수
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[LeaderVoiceSecondPhase]`
   limit: do 50 znaków
   EN: Warden of the Sisyphe Penalty
   PL: Strażnik Wyroku Sisyphe
484. [Słowo kluczowe [LeaderVoiceSecondPhase] — opis] - 최댓값 : 5\n- 수치 1당 공격 레벨 +1, 방어 레벨 +2\n- 수치가 3 이상이면, 스킬로 부여하는 못[형벌], 못[속죄] 부여량 +1
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +1 and Defense Level +2 for every Stack\n- At 3+ Stacks, inflict +1 more "Nail [Punishment]" and "Nail [Penance]" using Skills
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 i Poziom Obrony +2 za każdy ładunek\n- Przy 3 lub więcej ładunkach Umiejętności nakładają o 1 więcej „Gwóźdź [Kara]” i „Gwóźdź [Pokuta]”
485. [Słowo kluczowe [LeaderVoiceSecondPhase] — podsumowanie] 수치에 따라 공격 레벨, 방어 레벨 증가\n수치 3 이상이면 못[형벌], 못[속죄] 부여량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level and Defense Level based on Stack\nAt 3+ Stack, inflict more "Nail [Punishment]" and "Nail [Penance]"
   PL: Poziom Ataku i Poziom Obrony rosną zależnie od ładunków\nPrzy 3 lub więcej ładunkach nakłada więcej „Gwóźdź [Kara]” i „Gwóźdź [Pokuta]”
486. [Słowo kluczowe [LeaderVoiceSecondPhase] — tekst klimatyczny] 뜻대로 행동하지 않는 자들에게 간수가 나타난다. 이것은 시스템이기 때문이다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].flavor
   limit: do 130 znaków
   EN: The Warden appears before those who refuse to act as intended. For that is how the system works.
   PL: Strażnik stawia się przed tymi, którzy nie działają według woli systemu. Bo tak działa system.
487. [Słowo kluczowe [ConfessionSecondPhase] — nazwa] 고해의 증거
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[ConfessionSecondPhase]`
   limit: do 40 znaków
   EN: Proof of Confession
   PL: Dowód Spowiedzi
488. [Słowo kluczowe [ConfessionSecondPhase] — opis] - 다음 효과를 아울러 고해의 증거로 지칭함\n· 망치 못[단죄]\n· 망치 못[심판]\n· 못[형벌]\n· 못[속죄]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionSecondPhase].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The following effects are collectively referred to as "Proof of Confession":\n · Hammernail [Condemnation]\n · Hammernail [Judgment]\n · Nail [Punishment]\n · Nail [Penance]
   PL: - Następujące efekty są zbiorczo nazywane „Dowodem Spowiedzi”:\n· Młotogwóźdź [Potępienie]\n· Młotogwóźdź [Sąd]\n· Gwóźdź [Kara]\n· Gwóźdź [Pokuta]
489. [Słowo kluczowe [ConfessionSecondPhase] — podsumowanie] 간수가 부여하는 못과 망치 못을 아울러 지칭
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionSecondPhase].summary
   limit: do 120 znaków
   EN: Collectively refers to "Nails" and "Hammernails" the Warden inflicts
   PL: Zbiorcza nazwa Gwóździ i Młotogwoździ nakładanych przez Strażnika
490. [Słowo kluczowe [ConfessionSecondPhase] — tekst klimatyczny] 업보만큼 못을 박아, 속죄하였음을 증명하라.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionSecondPhase].flavor
   limit: do 120 znaków
   EN: Drive in as many nails as thy sins demand, and prove thy repentance.
   PL: Wbijaj tyle gwoździ, ile grzechów — niech służy to za dowód pokuty.
491. [Słowo kluczowe [LeaderVoiceThirdPhase] — nazwa] 시지프 형벌의 신부
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[LeaderVoiceThirdPhase]`
   limit: do 50 znaków
   EN: Chaplain of the Sisyphe Penalty
   PL: Kapłan Wyroku Sisyphe
492. [Słowo kluczowe [LeaderVoiceThirdPhase] — opis] - 최댓값 : 5\n- 수치 1당 공격 레벨 +2, 방어 레벨 +3\n- 수치가 3 이상이면, 스킬로 부여하는 못[Console] 부여량 +1
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +2 and Defense Level +3 for every Stack\n- At 3+ Stacks, inflict +1 more "Nail [Console]" using Skills
   PL: - Maks. ładunków: 5\n- Poziom Ataku +2 i Poziom Obrony +3 za każdy ładunek\n- Przy 3 lub więcej ładunkach Umiejętności nakładają o 1 więcej „Gwóźdź [Console]”
493. [Słowo kluczowe [LeaderVoiceThirdPhase] — podsumowanie] 수치에 따라 공격 레벨, 방어 레벨 증가\n수치 3 이상이면 못[Console] 부여량 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level and Defense Level based on Stack\nAt 3+ Stack, inflict more "Nail [Console]"
   PL: Poziom Ataku i Poziom Obrony rosną zależnie od ładunków\nPrzy 3 lub więcej ładunkach nakłada więcej „Gwóźdź [Console]”
494. [Słowo kluczowe [LeaderVoiceThirdPhase] — tekst klimatyczny] 뜻대로 행동하지 않는 자들에게 신부가 나타난다. 이것은 시스템이기 때문이다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].flavor
   limit: do 130 znaków
   EN: The Chaplain appears before those who refuse to act as intended. For that is how the system works.
   PL: Kapłan stawia się przed tymi, którzy nie działają według woli systemu. Bo tak działa system.
495. [Słowo kluczowe [ConfessionThirdPhase] — nazwa] 〜
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[ConfessionThirdPhase]`
   limit: do 40 znaków
   EN: 〜
   PL: 〜
496. [Słowo kluczowe [ConfessionThirdPhase] — opis] - 다음 효과를 아울러 〜로 지칭함\n· 못[Exception]\n· 못[Breakpoint]\n· 못[Console]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionThirdPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The following effects are collectively referred to as "〜":\n· Nail [Exception]\n· Nail [Breakpoint]\n· Nail [Console]
   PL: - Następujące efekty są zbiorczo nazywane „〜”:\n· Gwóźdź [Exception]\n· Gwóźdź [Breakpoint]\n· Gwóźdź [Console]
497. [Słowo kluczowe [ConfessionThirdPhase] — podsumowanie] 신부가 부여하는 못을 아울러 지칭
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionThirdPhase].summary
   limit: do 120 znaków
   EN: Collectively refers to "Nails" the Chaplain inflicts
   PL: Zbiorcza nazwa Gwóździ nakładanych przez Kapłana
498. [Słowo kluczowe [ConfessionThirdPhase] — tekst klimatyczny] “너희가 이 시스템에 있으면 안 될 이물질이라는 걸 확실히 알겠군. 그러니까… 이제라도 매뉴얼을 봐야겠어. 규율과 규칙에는 없는 게 없거든.”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConfessionThirdPhase].flavor
   limit: do 250 znaków
   EN: "Now I'm sure of it. You're all foreign elements that shouldn't be allowed into this system. I guess it's time I actually checked the manual. There's nothing the laws and rules don't account for."
   PL: „Więc na pewno jesteś obcym ciałem, które nie powinno istnieć w tym systemie. W takim razie... najwyższy czas zajrzeć w instrukcję. W przepisach i zasadach nie ma niczego, czego by nie uwzględniono.”
499. [Słowo kluczowe [ExecutionNailSecondPhase] — nazwa] 망치 못[심판]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[ExecutionNailSecondPhase]`
   limit: do 40 znaków
   EN: Hammernail [Judgment]
   PL: Młotogwóźdź [Sąd]
500. [Słowo kluczowe [ExecutionNailSecondPhase] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 (수치 x 5)%만큼 고정 피해</u></b></mark></color>를 입음 (최소 10)\n· 전투 시작 시 수비 스킬을 장착하였다면, 받는 피해가 절반으로 줄어들고 이 효과로 사망하거나 흐트러지지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to (Stack x 5%) of max HP</u></b></mark></color> (min 10)\n · Combat Start: If this unit has equipped a Defense Skill, halve damage taken and this unit cannot be killed or Staggered by this effect
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe (ładunki x 5)% Maks. HP</u></b></mark></color> (min. 10)\n· Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymywane obrażenia maleją o połowę i ten efekt nie pozbawia życia ani nie oszołamia
501. [Słowo kluczowe [ExecutionNailSecondPhase] — podsumowanie] 발동 시 고정 피해 입음\n수비 스킬 장착 시 피해 절반, 사망하지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activated, take fixed damage\nWhen Defense Skill is equipped, halve damage taken and this unit cannot be killed
   PL: Po wywołaniu otrzymuje obrażenia stałe\nZ wyposażonymi Umiejętnościami obrony otrzymuje połowę obrażeń i nie ginie
502. [Słowo kluczowe [ExecutionNailSecondPhase] — tekst klimatyczny] 이는 못이되, 못이 아니요, 심판을 선고하는 망치일지니라.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].flavor
   limit: do 120 znaków
   EN: For this is a nail, yet no nail. 'Tis a hammer that pronounceth judgment.
   PL: Jest gwoździem, a nie gwoździem — młotem, który ogłasza sąd.
503. [Słowo kluczowe [RestrainingNailSecondPhase] — nazwa] 망치 못[단죄]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[RestrainingNailSecondPhase]`
   limit: do 40 znaków
   EN: Hammernail [Condemnation]
   PL: Młotogwóźdź [Potępienie]
504. [Słowo kluczowe [RestrainingNailSecondPhase] — opis] - 최댓값 : 9\n- 턴 시작 시 이 효과가 있으면, <color=#ff6000><mark=#ff000040><b><u>흐트러짐</u></b></mark></color> 상태로 변경됨\n· 이 효과가 발동했으면, 턴 종료 시 사라짐\n· 박동을 보유했으면, 이 효과로 흐트러지지 않고 해당 턴 종료 시 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Turn Start: If this unit has this effect, become <color=#ff6000><mark=#ff000040><b><u>Staggered</u></b></mark></color>\n · Turn End: This effect expires if triggered this turn\n · If this unit has "Thumping Pulse", it cannot be Staggered via this effect, and this effect expires at Turn End
   PL: - Maks. ładunków: 9\n- Na początku tury, jeżeli jednostka posiada ten efekt, zmienia się w stan <color=#ff6000><mark=#ff000040><b><u>Oszołomienia</u></b></mark></color>\n· Po wywołaniu tego efektu znika na koniec tury\n· Jeżeli posiada Tętnienie, nie zostaje nim oszołomiony i znika na koniec tej tury
505. [Słowo kluczowe [RestrainingNailSecondPhase] — podsumowanie] 턴 시작 시 흐트러짐 상태로 변경\n박동 보유 시 흐트러지지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Become Staggered\nIf this unit has "Thumping Pulse", does not become Staggered
   PL: Na początku tury zmienia się w stan Oszołomienia\nPosiadając Tętnienie, nie zostaje oszołomiony
506. [Słowo kluczowe [RestrainingNailSecondPhase] — tekst klimatyczny] 네가 뽑아내지 못한 못마다 네 업보의 증거가 되리니, 심판의 날이 도래하여 뽑히지 아니한 못들이 네 몸과 마음에 더욱 깊숙이 박히리라.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].flavor
   limit: do 250 znaków
   EN: Each nail thou hast failed to draw forth shall stand as witness to thy sins; and when the Day of Judgment cometh, every nail left within thee shall be driven deeper still into thy flesh and soul.
   PL: Każdy gwóźdź, którego nie wydobyłeś, będzie dowodem twoich grzechów; gdy nadejdzie Dzień Sądu, każdy nie wydobyty gwóźdź wbije się jeszcze głębiej w twe ciało i duszę.
507. [Słowo kluczowe [CeremonialNail] — nazwa] 못[형벌]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=CeremonialNail].name
   kontekst: identyfikator tagu w tekstach: `[CeremonialNail]`
   limit: do 40 znaków
   EN: Nail [Punishment]
   PL: Gwóźdź [Kara]
508. [Słowo kluczowe [CeremonialNail] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, 수치만큼 침잠 얻음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=CeremonialNail].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", gain Sinking equal to Stack
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, zyskuje Zatonięcie równe liczbie ładunków
509. [Słowo kluczowe [CeremonialNail] — podsumowanie] 발동 시 침잠 얻음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=CeremonialNail].summary
   limit: do 120 znaków
   EN: When activated, gain Sinking
   PL: Po wywołaniu zyskuje Zatonięcie
510. [Słowo kluczowe [CeremonialNail] — tekst klimatyczny] 형벌은 규율과 규범을 어긴 자의 도덕적 가책이라.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=CeremonialNail].flavor
   limit: do 120 znaków
   EN: For punishment is the pang of conscience borne by those who transgress rule and ordinance.
   PL: Kara jest — mówię — moralnym wyrzutem sumienia tych, którzy przekroczyli regułę i normę.
511. [Słowo kluczowe [MarkingNail] — nazwa] 못[속죄]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MarkingNail].name
   kontekst: identyfikator tagu w tekstach: `[MarkingNail]`
   limit: do 40 znaków
   EN: Nail [Penance]
   PL: Gwóźdź [Pokuta]
512. [Słowo kluczowe [MarkingNail] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, (수치 x 2)만큼 흐트러짐 손상
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MarkingNail].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", raise Stagger Threshold by (Stack x 2)
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, podnosi Próg Oszołomienia o (ładunki x 2)
513. [Słowo kluczowe [MarkingNail] — podsumowanie] 발동 시 흐트러짐 손상
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MarkingNail].summary
   limit: do 120 znaków
   EN: When activated raise Stagger Threshold
   PL: Po wywołaniu podnosi Próg Oszołomienia
514. [Słowo kluczowe [MarkingNail] — tekst klimatyczny] 속죄하지 않은 자의 가슴에 박히는 못.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MarkingNail].flavor
   limit: do 120 znaków
   EN: This is a nail driven into the hearts of the impenitent.
   PL: To gwóźdź wbity w serca tych, którzy nie pokutowali.
515. [Słowo kluczowe [GoldenHideWarderThirdPhase] — nazwa] 박동
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenHideWarderThirdPhase]`
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Słowo kluczowe [GoldenHideWarderThirdPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 이 효과를 보유한 수감자가 신부의 <color=#ff6000><mark=#ff000040><b><u>‘강제 퇴장’</u></b></mark></color> 스킬과 <color=#ff6000><mark=#ff000040><b><u>합하여 승리</u></b></mark></color>했으면, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 250%만큼 보호막</u></b></mark></color> 얻음 (신부의 ‘강제 퇴장’ 공격 종료 시, 이 효과로 얻은 보호막 수치만큼 수감자가 보유한 보호막에서 차감함)\n- 합 위력 +3, 받는 피해량 -50%\n- 적중 시, 공격 레벨 감소 1 부여 (최대 9)\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Turn Start: A random Sinner gains this effect\n- On Clash Win, if the Sinner who has this effect <color=#ff6000><mark=#ff000040><b><u>won the Clash</u></b></mark></color> against the Chaplain's <color=#ff6000><mark=#ff000040><b><u>"Systemwide Ban"</u></b></mark></color> Skill, gain <color=#ff6000><mark=#ff000040><b><u>Shield equal to 250% of the Sinner's max HP</u></b></mark></color> (Shield gained from this effect is removed from the Sinner's total Shield at Attack End of the Chaplain's "Systemwide Ban")\n- Clash Power +3, take -50% damage\n- On Hit, inflict 1 Offense Level Down (max 9)\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Jeżeli Grzesznik posiadający ten efekt <color=#ff6000><mark=#ff000040><b><u>wygrywa Starcie</u></b></mark></color> z Umiejętnością Kapłana <color=#ff6000><mark=#ff000040><b><u>„Przymusowe Wygnanie”</u></b></mark></color>, zyskuje <color=#ff6000><mark=#ff000040><b><u>Tarczę równą 250% Maks. HP Grzesznika</u></b></mark></color> (po zakończeniu ataku „Przymusowe Wygnanie” Kapłana odejmuje z Tarczy Grzesznika tyle, ile wynosiła Tarcza z tego efektu)\n- Moc Starcia +3, otrzymuje obrażenia -50%\n- Przy trafieniu nakłada 1 Spadku Poziomu Ataku (maks. 9)\n- Na koniec tury znika
517. [Słowo kluczowe [GoldenHideWarderThirdPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소\n'강제 퇴장'과 합 승리 시 보호막 얻음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and take less damage\nOn Clash Win against "Systemwide Ban", gain Shield
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń\nPo wygranym Starciu z Umiejętnością „Przymusowe Wygnanie” zyskuje Tarczę
518. [Słowo kluczowe [GoldenHideWarderThirdPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].flavor
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Słowo kluczowe [GoldenFabricWarderThirdPhase] — nazwa] 정지
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[GoldenFabricWarderThirdPhase]`
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Słowo kluczowe [GoldenFabricWarderThirdPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +2, 가하는 피해량 +25%\n- 적중 시, 방어 레벨 감소 1 부여 (최대 9)\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +2, deal +25% damage\n- On Hit, inflict 1 Defense Level Down (max 9)\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +2, zadaje obrażenia +25%\n- Przy trafieniu nakłada 1 Spadku Poziomu Obrony (maks. 9)\n- Na koniec tury znika
521. [Słowo kluczowe [GoldenFabricWarderThirdPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가\n적중 시 방어 레벨 감소 부여
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Final Power and deal more damage\nOn Hit, inflict Defense Level Down
   PL: Moc Końcowa rośnie, zadaje więcej obrażeń\nPrzy trafieniu nakłada Spadek Poziomu Obrony
522. [Słowo kluczowe [GoldenFabricWarderThirdPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].flavor
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Słowo kluczowe [MeursaultBuffWarderThirdPhase] — nazwa] 이방인
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[MeursaultBuffWarderThirdPhase]`
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Słowo kluczowe [MeursaultBuffWarderThirdPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 속도 최솟값, 최댓값 +3\n- 최종 위력 +3, 피해량 +30%\n- 신부와 합 진행 시,\n· 피해량 +(자신의 잃은 체력 비율)% (최대 90%)\n· 합 승리 시, 정신력 8 회복\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 5개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 3 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Min & Max Speed +3\n- Final Power +3 and deal +30% damage\n- When Clashing against the Chaplain:\n · Deal +(missing HP percentage on self)% damage (max 90%)\n · On Clash Win, heal 8 SP\n · On Clash Win, gain 1 E.G.O resource for each of the 5 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 3 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Min. i Maks. Szybkość +3\n- Moc Końcowa +3, zadaje obrażenia +30%\n- Podczas Starcia z Kapłanem:\n· Zadaje obrażenia +(procent utraconego HP na sobie)% (maks. 90%)\n· Po wygranym Starciu odzyskuje 8 Poczytalności\n· Po wygranym Starciu zyskuje w sumie 5 Zasobów E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 3 Wzrostu Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
525. [Słowo kluczowe [MeursaultBuffWarderThirdPhase] — podsumowanie] 신부와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and deal more damage when Clashing with the Chaplain\nCannot be Staggered, cannot be defeated when there are other surviving allies
   PL: - Podczas Starcia z Kapłanem Moc Starcia i obrażenia rosną\n- Nie zostaje oszołomiony; gdy żyją inni sojusznicy, nie ginie
526. [Słowo kluczowe [MeursaultBuffWarderThirdPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].flavor
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Słowo kluczowe [GoldenNail] — nazwa] 못[Console]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenNail].name
   kontekst: identyfikator tagu w tekstach: `[GoldenNail]`
   limit: do 40 znaków
   EN: Nail [Console]
   PL: Gwóźdź [Console]
528. [Słowo kluczowe [GoldenNail] — opis] - 최댓값 : 9\n- 전투 시작 시 <color=#ff6000><mark=#ff000040><b><u>수치가 9</u></b></mark></color>이면, 이번 턴 동안 이 효과를 보유한 수감자가 신부에게 <color=#ff6000><mark=#ff000040><b><u>공격 적중 시 자신의 최대 체력 2%만큼 고정 체력 피해</u></b></mark></color>를 입음 (이 효과로 흐트러지지 않음)\n- ‘시지프 시스템을 진짜 망가트리려고?’로 인하여 이 효과가 발동될 때, 수치만큼 침잠 얻고 (수치 x 2)만큼 흐트러짐 손상
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenNail].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Combat Start: <color=#ff6000><mark=#ff000040><b><u>At 9 Stacks, On Hit against the Chaplain</u></b></mark></color>, the Sinner who has this effect for this turn <color=#ff6000><mark=#ff000040><b><u>takes fixed damage equal to 2% of max HP</u></b></mark></color> (this effect cannot Stagger this unit)\n- If this effect is triggered by "Do you seriously mean to break the Sisyphe System?", gain Sinking equal to Stack and raise Stagger Threshold by (Stack x 2)
   PL: - Maks. ładunków: 9\n- Na początku walki przy <color=#ff6000><mark=#ff000040><b><u>9 ładunkach</u></b></mark></color> Grzesznik posiadający ten efekt w tej turze <color=#ff6000><mark=#ff000040><b><u>otrzymuje przy trafieniu atakiem w Kapłana obrażenia HP stałe równe 2% Maks. HP</u></b></mark></color> (ten efekt nie oszołamia)\n- Gdy ten efekt zostaje wywołany przez „Czy naprawdę próbujesz zepsuć System Sisyphe?”, zyskuje Zatonięcie równe liczbie ładunków i podnosi Próg Oszołomienia o (ładunki x 2)
529. [Słowo kluczowe [GoldenNail] — podsumowanie] 발동 시 침잠 얻음, 흐트러짐 손상\n최대 수치면 공격 적중 시 고정 피해 입음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenNail].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activated, gain Sinking and raise Stagger Threshold\nAt max Stack, take fixed damage when hit
   PL: Po wywołaniu zyskuje Zatonięcie i podnosi Próg Oszołomienia\nPrzy Maks. ładunków otrzymuje obrażenia stałe przy trafieniu
530. [Słowo kluczowe [GoldenNail] — tekst klimatyczny] “어디 보자, 이 못에 대한 매뉴얼이… ‘당신은 죄악이 등을 타고…’ 음, 이건 아니고,”\n\n“여기 이쪽 42번째 서랍에… 있었는데… 아, 여기 있었군! ‘르누아르를 담당하는 시지프 시스템 관리자를 위한 콘솔 매뉴얼’.”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GoldenNail].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Let's see, the manual for this nail... 'You feel your sins crawling on your back...' Mm, no, not this one."\n\n"It should be in Drawer 42 over here... I know I put it... ah, there it is! 'Le Noir Administrator's Guide to the Sisyphe System Console Commands'."
   PL: „Zobaczmy, instrukcja dla tego gwoźdźia... 'Czujesz, jak grzechy wpełzają ci po plecach...' Mmm, nie, to nie to.”\n\n„Powinna być w czterdziestym drugim szufladzie... wkładałem tam... o, proszę! 'Instrukcja konsoli dla administratora Systemu Sisyphe odpowiadającego za Le Noir'.”
531. [Słowo kluczowe [VibrationFocusing] — nazwa] 진동 - 보존
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=VibrationFocusing].name
   kontekst: identyfikator tagu w tekstach: `[VibrationFocusing]`
   limit: do 40 znaków
   EN: Tremor - Conservation
   PL: Wstrząs - Zachowanie
532. [Słowo kluczowe [VibrationFocusing] — opis] - 진동 폭발 시 진동 위력의 (60 + 공격자의 충전 위력 또는 특수 충전 x 8)%만큼\n나태 피해를 입고 횟수 1 감소 (최대 120%)\n· 르누아르 소속 캐릭터의 스킬, 패시브 효과로 진동 폭발 시 이 효과로 횟수가 감소하지 않음\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=VibrationFocusing].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Sloth Damage equal to (60 + sum of Charge Potency or Unique Charge on the attacker x 8)% of Tremor Potency, and reduce the Count by 1 (max 120%)\n · When "Le Noir" units' Skills and Passives trigger Tremor Burst, the above effect does not reduce the Count\n- When hit by Tremor Burst Skills, raise Stagger Threshold by this effect's Potency\n- Turn End: Lose 1 Count\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Lenistwa równe (60 + suma Siły Ładunku lub Specjalnego Ładunku atakującego x 8)% Siły Wstrząsu\ni traci 1 Licznika (maks. 120%)\n· Gdy Wyładowanie Wstrząsu wywołują Umiejętności lub umiejętności pasywne jednostek z Le Noir, ten efekt nie zmniejsza Licznika\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Na koniec tury traci 1 Licznika\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Siłę i Licznik Wstrząsu)
533. [Słowo kluczowe [VibrationFocusing] — podsumowanie] 진동 폭발 시 나태 피해 입음\n진동 폭발 스킬로 피격 시 흐트러짐 손상
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=VibrationFocusing].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Tremor Burst, take Sloth Damage\nWhen hit by Skills that trigger Tremor Burst, raise Stagger Threshold
   PL: Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Lenistwa\nPrzy trafieniu Umiejętnościami z Wyładowaniem Wstrząsu podnosi Próg Oszołomienia
534. [Słowo kluczowe [ExecutionNailThirdPhase] — nazwa] 못[Breakpoint]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[ExecutionNailThirdPhase]`
   limit: do 40 znaków
   EN: Nail [Breakpoint]
   PL: Gwóźdź [Breakpoint]
535. [Słowo kluczowe [ExecutionNailThirdPhase] — opis] - 최댓값 : 9\n- '시지프 시스템을 진짜 망가트리려고?'로 인하여 이 효과가 발동될 때, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 (수치 x 10)%만큼 고정 피해</u></b></mark></color>를 입음 (최소 10)\n· 전투 시작 시 수비 스킬을 장착하였다면, 받는 피해가 절반으로 줄어들고 이 효과로 사망하거나 흐트러지지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Do you seriously mean to break the Sisyphe System?", <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to (Stack x 10%) of max HP</u></b></mark></color> (min 10)\n · Combat Start: If this unit has equipped a Defense Skill, halve damage taken and this unit cannot be killed or Staggered by this effect
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Czy naprawdę próbujesz zepsuć System Sisyphe?”, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe (ładunki x 10)% Maks. HP</u></b></mark></color> (min. 10)\n· Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymywane obrażenia maleją o połowę i ten efekt nie pozbawia życia ani nie oszołamia
536. [Słowo kluczowe [ExecutionNailThirdPhase] — podsumowanie] 발동 시 고정 피해 입음\n수비 스킬 장착 시 피해 절반, 사망하지 않음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].summary
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Słowo kluczowe [ExecutionNailThirdPhase] — tekst klimatyczny] “관리 매뉴얼에 써 있더라고. 시스템 안에서 이 명령어에 못 박히면, 아무것도 못 한다고.”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].flavor
   limit: do 150 znaków
   EN: "The admin manual says it plain enough. Once this command nails you down inside the system, you can't do a thing."
   PL: „W instrukcji administratora pisali to wprost. Kiedy ta komenda przybija cię w systemie, nie zrobisz już niczego.”
538. [Słowo kluczowe [RestrainingNailThirdPhase] — nazwa] 못[Exception]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].name
   kontekst: identyfikator tagu w tekstach: `[RestrainingNailThirdPhase]`
   limit: do 40 znaków
   EN: Nail [Exception]
   PL: Gwóźdź [Exception]
539. [Słowo kluczowe [RestrainingNailThirdPhase] — opis] - 최댓값 : 9\n- 턴 시작 시 이 효과가 있으면, <color=#ff6000><mark=#ff000040><b><u>현재 체력의 50%만큼 고정 피해</u></b></mark></color>를 입고 <color=#ff6000><mark=#ff000040><b><u>흐트러짐</u></b></mark></color> 상태로 변경됨\n· 이 효과가 발동했으면, 턴 종료 시 사라짐\n· 박동을 보유했으면, 이 효과로 흐트러지지 않고 받는 피해가 절반으로 줄어들며, 해당 턴 종료 시 사라짐
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Turn Start: If this unit has this effect, <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to 50% current HP</u></b></mark></color> and become <color=#ff6000><mark=#ff000040><b><u>Staggered</u></b></mark></color>\n · Turn End: This effect expires if triggered this turn\n · If this unit has "Thumping Pulse", it cannot be Staggered via this effect, halve damage taken, and this effect expires at Turn End
   PL: - Maks. ładunków: 9\n- Na początku tury, jeżeli jednostka posiada ten efekt, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe 50% obecnego HP</u></b></mark></color> i zmienia się w stan <color=#ff6000><mark=#ff000040><b><u>Oszołomienia</u></b></mark></color>\n· Po wywołaniu tego efektu znika na koniec tury\n· Jeżeli posiada Tętnienie, nie zostaje nim oszołomiony, otrzymywane obrażenia maleją o połowę, a efekt znika na koniec tej tury
540. [Słowo kluczowe [RestrainingNailThirdPhase] — podsumowanie] 턴 시작 시 고정 피해 입고 흐트러짐 상태로 변경\n박동 보유 시 흐트러지지 않고 피해 절반
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Take fixed damage and become Staggered\nIf this unit has "Thumping Pulse", does not become Staggered and take only half damage
   PL: Na początku tury otrzymuje obrażenia stałe i zmienia się w stan Oszołomienia\nPosiadając Tętnienie, nie zostaje oszołomiony i otrzymuje tylko połowę obrażeń
541. [Słowo kluczowe [RestrainingNailThirdPhase] — tekst klimatyczny] “예외적인 모든 것들도, 이 못에는 걸릴 수밖에 없지.”
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].flavor
   limit: do 120 znaków
   EN: "Even the exceptions can't help but get caught on this nail."
   PL: „Nawet wyjątki nie potrafią uchronić się przed tym gwoździem.”
542. [Słowo kluczowe [ConnectionError_LowMorale] — nazwa] 싱크 오류
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ConnectionError_LowMorale]`
   limit: do 40 znaków
   EN: Sync Error
   PL: Błąd Synchronizacji
543. [Słowo kluczowe [ConnectionError_LowMorale] — opis] - 사기 저하\n- 받는 피해량 +12.5%\n- 속도 최솟값, 최댓값 -1\n- 보존을 소모하는 스킬의 피해량 -15%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +12.5% damage\n- Min & Max Speed -1\n- Deal -15% damage using Skills that consume Preservation
   PL: - Niskie Morale\n- Otrzymuje obrażenia +12,5%\n- Min. i Maks. Szybkość -1\n- Umiejętności zużywające Zachowanie zadają obrażenia -15%
544. [Słowo kluczowe [ConnectionError_LowMorale] — podsumowanie] 속도 최솟값, 최댓값 감소, 받는 피해량 증가\n보존을 소모하는 스킬의 피해량 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose Min & Max Speed, take more damage\nSkills that consume Preservation deal less damage
   PL: Traci Min. i Maks. Szybkość, otrzymuje więcej obrażeń\nUmiejętności zużywające Zachowanie zadają mniej obrażeń
545. [Słowo kluczowe [ConnectionError_Panic] — nazwa] 싱크 오류
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ConnectionError_Panic]`
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Słowo kluczowe [ConnectionError_Panic] — opis] - 패닉\n- 받는 피해량 +20%\n- 속도 최솟값, 최댓값 -2\n- 보존을 소모하는 스킬의 피해량 -25%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +20% damage\n- Min & Max Speed -2\n- Deal -25% damage using Skills that consume Preservation
   PL: - Panika\n- Otrzymuje obrażenia +20%\n- Min. i Maks. Szybkość -2\n- Umiejętności zużywające Zachowanie zadają obrażenia -25%
547. [Słowo kluczowe [ConnectionError_Panic] — podsumowanie] 속도 최솟값, 최댓값 감소, 받는 피해량 증가\n보존을 소모하는 스킬의 피해량 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=ConnectionError_Panic].summary
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Słowo kluczowe [JeanneDesign] — nazwa] 못 박힘
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneDesign].name
   kontekst: identyfikator tagu w tekstach: `[JeanneDesign]`
   limit: do 40 znaków
   EN: Nailed
   PL: Przybity
549. [Słowo kluczowe [JeanneDesign] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>코인 앞면 확률 95% 고정</color></mark></b></u>\n- 2이면, 자신과 합 하는 <color=#ff6000><mark color=#ff000040><b><u>대상의 합 위력 -2</color></mark></b></u>\n- 3이면, 전부 소모하여 다음 턴에 <color=#ff6000><mark color=#ff000040><b><u>앙가즈망(engagement)</color></mark></b></u>을 얻음\n- 턴 종료시 1 감소 (해당 효과를 얻은 턴에는 감소하지 않음)\n- 앙가즈망(engagement)이 있을 경우, 획득할 수 없음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneDesign].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>This unit has 95% chance to flip Heads</color></mark></b></u>\n- At 2 Stacks, <color=#ff6000><mark color=#ff000040><b><u>Clash Power -2 for targets</color></mark></b></u> Clashing with this unit\n- At 3 Stacks, consume all Stacks and gain <color=#ff6000><mark color=#ff000040><b><u>Engagement</color></mark></b></u> next turn\n- Turn End: Lose 1 Stack (does not lose Stack in the turn this effect is gained)\n- Cannot gain this effect if this unit has Engagement
   PL: - Maks. ładunków: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Szanse na Awers Monet zamrożone na 95%</u></b></mark></color>\n- Przy 2 ładunkach Moc Starcia celów, którzy prowadzą z nim Starcie, wynosi <color=#ff6000><mark color=#ff000040><b><u>-2</u></b></mark></color>\n- Przy 3 ładunkach zużywa je wszystkie, a w następnej turze zyskuje <color=#ff6000><mark color=#ff000040><b><u>Engagement</u></b></mark></color>\n- Na koniec tury traci 1 ładunek (w turze zdobycia tego efektu nie traci)\n- Jeżeli jednostka posiada Engagement, nie może zdobyć tego efektu
550. [Słowo kluczowe [JeanneDesign] — tekst klimatyczny] 실존은 본질에 앞선다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneDesign].flavor
   limit: do 120 znaków
   EN: Existence precedes essence.
   PL: Egzystencja poprzedza esencję.
551. [Słowo kluczowe [JeanneManager] — nazwa] 앙가즈망(engagement)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneManager].name
   kontekst: identyfikator tagu w tekstach: `[JeanneManager]`
   limit: do 40 znaków
   EN: Engagement
   PL: Engagement
552. [Słowo kluczowe [JeanneManager] — opis] - <color=#ff6000><mark color=#ff000040><b><u>자신의 코인 앞면 확률 100% 고정</color></mark></b></u>\n- 자신과 합을 진행하거나 자신을 공격하는 <color=#ff6000><mark color=#ff000040><b><u>대상의 스킬 더하기 코인 뒷면 확률 100% 고정</color></mark></b></u>\n· 빼기 코인이면, 앞면 코인 확률 100% 고정\n- 포착 스킬 장착 또는 흐트러짐 시 효과 해제
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneManager].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - <color=#ff6000><mark color=#ff000040><b><u>This unit has 100% chance to flip Heads</color></mark></b></u>\n- Targets Clashing with or attacking this unit have <color=#ff6000><mark color=#ff000040><b><u>100% chance to flip Tails for Plus Coins</color></mark></b></u>\n · The said units' Minus Coins have 100% chance to flip Heads\n- Remove this effect upon equipping the "Focusing" Skill, or if this unit becomes Staggered
   PL: - <color=#ff6000><mark color=#ff000040><b><u>Szanse na Awers własnych Monet zamrożone na 100%</u></b></mark></color>\n- Cele prowadzące z nim Starcie lub atakujące go mają <color=#ff6000><mark color=#ff000040><b><u>Monety Plus o zamrożonych szansach na Rewers wynoszących 100%</u></b></mark></color>\n· Monety Minus tych jednostek mają 100% szans na Awers\n- Efekt znika po wyposażeniu Umiejętności „Skupienie” lub gdy jednostka zostanie oszołomiona
553. [Słowo kluczowe [JeanneManager] — tekst klimatyczny] 나는 백화점을 세웠어. 그리고 지금은 런웨이 위의 모델이자, 무대 위의 배우지.\n\n마 퓌스, 당신은… 시네마겠지?
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneManager].flavor
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I designed the department store. And now, I'm a model on its runway, an actress on its stage.\n\nAnd you, ma puce... you'd be the cinéma itself, wouldn't you?
   PL: Zaprojektowałam Grand Magasin. A teraz jestem modelą na jego wybiegu i aktorką na jego scenie.\n\nA ty, ma puce... tobą będzie samo kino, nieprawdaż?
554. [Słowo kluczowe [JeannePartner] — nazwa] 에트르 뿌르 오트뤼(être-pour-autrui)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartner].name
   kontekst: identyfikator tagu w tekstach: `[JeannePartner]`
   limit: do 40 znaków
   EN: Être-pour-autrui
   PL: Être-pour-autrui
555. [Słowo kluczowe [JeannePartner] — opis] - 이 효과 획득 시 대상의 모든 부정적인 효과 제거\n- 정신력을 45로 고정\n· 빼기 코인을 사용하는 인격일 경우, 정신력을 -30으로 고정\n- 흐트러짐 상태가 되지 않음\n- 잔느의 페이즈 변경 시 제거
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartner].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Targets that gain this effect lose all negative effects\n- Fix SP to 45\n · For Minus Coin Identities, fix SP to -30\n- Cannot be Staggered\n- Remove this effect when Jeanne enters a new phase
   PL: - Przy zdobyciu tego efektu cel traci wszystkie negatywne efekty\n- Zamraża Poczytalność na 45\n· Dla Tożsamości używających Monet Minus zamraża Poczytalność na -30\n- Nie może ulec Oszołomieniu\n- Znika, gdy Jeanne zmienia fazę
556. [Słowo kluczowe [JeannePartner] — tekst klimatyczny] 당신은 내게 어떻게 보여지고 있을 것 같아?\n당신이 보는 자기 자신과 내가 보는 당신은 전혀 다를 거야.\n마 퓌스, 당신은 내 안에서 못 박혔어.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartner].flavor
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: How do you suppose you look to me? The self you see and the you I see must be entirely different.\nMa puce... you've already been nailed into place within me.
   PL: Jak sądzisz, jak wyglądasz w moich oczach?\nTy, którego widzisz siebie, a ty, którego widzę ja, będą zupełnie różne.\nMa puce... jesteś już przybity gwoździem we mnie.
557. [Słowo kluczowe [JeannePartnerTwo] — nazwa] 에트르 뿌르 수아(être-pour-soi)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartnerTwo].name
   kontekst: identyfikator tagu w tekstach: `[JeannePartnerTwo]`
   limit: do 40 znaków
   EN: Être-pour-soi
   PL: Être-pour-soi
558. [Słowo kluczowe [JeannePartnerTwo] — opis] - 정신력을 45로 고정\n- 피해를 받지 않음\n- 잔느의 페이즈 변경 시 제거
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartnerTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Fix SP to 45\n- Does not take damage\n- Remove this effect when Jeanne enters a new phase
   PL: - Zamraża Poczytalność na 45\n- Nie otrzymuje obrażeń\n- Znika, gdy Jeanne zmienia fazę
559. [Słowo kluczowe [JeannePartnerTwo] — tekst klimatyczny] 의식을 가진다는 건 무서운 일이야. 어딘가 구멍이 생겨버릴 수밖에 없거든.\n\n채워줄래, 마 퓌스?
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePartnerTwo].flavor
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Consciousness is a frightening thing, you know. Somewhere within it, a hollow is bound to open.\n\nWill you fill it for me, ma puce?
   PL: Posiadanie świadomości to przerażająca rzecz. Gdzieś w niej nieuchronnie otwiera się dziura.\n\nWypełnisz ją dla mnie, ma puce?
560. [Słowo kluczowe [JeannePathos] — nazwa] 파토스 - 데지르 데트르(désir d'être)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePathos].name
   kontekst: identyfikator tagu w tekstach: `[JeannePathos]`
   limit: do 40 znaków
   EN: Pathos - Désir d'être
   PL: Pathos - Désir d'être
561. [Słowo kluczowe [JeannePathos] — opis] - 최댓값: 100\n- 합 승리시 3 증가\n- 합 패배시 5 증가\n- 합 횟수만큼 증가\n- 턴 종료시 최댓값이면, 페이즈를 변경함
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePathos].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Clash Win, gain 3 Stacks\n- On Clash Lose, gain 5 Stacks\n- Gain Stack equal to Clash count\n- Turn End: At max Stack, enter a new phase
   PL: - Maks. ładunków: 100\n- Po wygranym Starciu zyskuje 3 ładunków\n- Po przegranej w Starciu zyskuje 5 ładunków\n- Zyskuje ładunki w liczbie Stareć\n- Na koniec tury przy Maks. ładunków zmienia fazę
562. [Słowo kluczowe [JeannePathos] — tekst klimatyczny] 열정과 정열. 붉은 파토스로 난 붉게 피어나고 싶었어.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeannePathos].flavor
   limit: do 140 znaków
   EN: I wanted to bloom red... with all that red passion, all that fervor, all that pathos burning within me.
   PL: Pasja i namiętność. Chciałam rozkwitnąć czerwono — w tym czerwonym patosie.
563. [Słowo kluczowe [JeanneLogos] — nazwa] 로고스 - 망끄 데트르(manque d'être)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneLogos].name
   kontekst: identyfikator tagu w tekstach: `[JeanneLogos]`
   limit: do 40 znaków
   EN: Logos - Manque d'être
   PL: Logos - Manque d'être
564. [Słowo kluczowe [JeanneLogos] — opis] - 최댓값: 100\n- 합 승리시 5 증가\n- 합 횟수만큼 증가\n- 수치 10당 공격 레벨 +1\n- 수치 20당 합 위력 +1
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneLogos].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Clash Win, gain 5 Stacks\n- Gain Stack equal to Clash count\n- Offense Level +1 for every 10 Stacks\n- Clash Power +1 for every 20 Stacks
   PL: - Maks. ładunków: 100\n- Po wygranym Starciu zyskuje 5 ładunków\n- Zyskuje ładunki w liczbie odbytych Stareć\n- Poziom Ataku +1 za każde 10 ładunków\n- Moc Starcia +1 za każde 20 ładunków
565. [Słowo kluczowe [JeanneLogos] — tekst klimatyczny] 당신에게는 무언가 결여되어 있어. 나도 그렇지. 그러니까 서로 채워줄 수 있어.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneLogos].flavor
   limit: do 120 znaków
   EN: There's something missing in you—in me, too. We can fill each other.
   PL: Czemuś w tobie czegoś brakuje. We mnie także. Dlatego możemy się nawzajem wypełnić.
566. [Słowo kluczowe [JeanneCheat] — nazwa] 데제스푸아르(désespoir)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneCheat].name
   kontekst: identyfikator tagu w tekstach: `[JeanneCheat]`
   limit: do 40 znaków
   EN: Désespoir
   PL: Désespoir
567. [Słowo kluczowe [JeanneCheat] — opis] - 코인 뒷면 확률 100%로 고정 (빼기 코인일 경우, 앞면으로 고정)\n- 턴 종료시 1 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneCheat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This unit has 100% chance to flip Tails (for Minus Coins, Heads)\n- Turn End: Lose 1 Stack
   PL: - Szanse na Rewers Monet zamrożone na 100% (dla Monet Minus — na Awers)\n- Na koniec tury traci 1 ładunek
568. [Słowo kluczowe [JeanneCheat] — tekst klimatyczny] …마 퓌스, 도피할 거야? 판단으로부터, 이 빛으로부터…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneCheat].flavor
   limit: do 120 znaków
   EN: ... Ma puce, are you running away? From judgment, from this light...?
   PL: ...Ma puce, uciekasz? Od sądu, od tego światła...?
569. [Słowo kluczowe [JeanneBlueprint] — nazwa] 델레스망(délaissement)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneBlueprint].name
   kontekst: identyfikator tagu w tekstach: `[JeanneBlueprint]`
   limit: do 40 znaków
   EN: Délaissement
   PL: Délaissement
570. [Słowo kluczowe [JeanneBlueprint] — opis] - 최댓값: 5\n- 수치당 합 위력 +1\n- 수치당 스킬로 받는 피해량 +10%\n- 턴 시작시 4이상이면, 아래 효과 적용\n· 모든 흐트러짐 선 제거\n· 흐트러짐 시 흐트러짐 상태 해제\n· 슬롯 가중치 +1
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneBlueprint].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Clash Power +1 for every Stack\n- Take +10% damage from Skills for every Stack\n- Turn Start: At 4+ Stacks, apply the following effects:\n · Remove all Stagger Thresholds\n · When Staggered, recover from Stagger\n · Slot Weight +1
   PL: - Maks. ładunków: 5\n- Moc Starcia +1 za każdy ładunek\n- Otrzymuje obrażenia +10% od Umiejętności za każdy ładunek\n- Na początku tury przy 4 lub więcej ładunkach stosowane są następujące efekty:\n· Usunięcie wszystkich Progów Oszołomienia\n· Po Oszołomieniu wychodzi z Oszołomienia\n· Waga Slotu +1
571. [Słowo kluczowe [JeanneBlueprint] — tekst klimatyczny] 그 무엇도 보장해 주지 않는 절망적 자유 속에서도, 시지프 백화점 안에서만큼은 설계와 시선에 따라 재단되고, 유지되는 축복을 누릴 수 있다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=JeanneBlueprint].flavor
   limit: do 250 znaków
   EN: Amid the freedom of despair that promises nothing, Grand Magasin Sisyphe alone offers a blessing: to be cut to measure by design and gaze, and in doing so, be given certainty and continuity.
   PL: Nawet w rozpaczliwej wolności, która niczego nie gwarantuje, wewnątrz Grand Magasin Sisyphe można cieszyć się błogosławieństwem bycia skrojonym wedle projektu i spojrzenia — i utrwalonym.
572. [Słowo kluczowe [BoneNail] — nazwa] 라브젝트(l'abject)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BoneNail].name
   kontekst: identyfikator tagu w tekstach: `[BoneNail]`
   limit: do 40 znaków
   EN: L'Abject
   PL: L'Abject
573. [Słowo kluczowe [BoneNail] — opis] - 최댓값 : 5\n- 수치 1당, 속도 1 감소\n- 수치 1당, 출혈로 받는 피해 +20% (소수점 버림)\n- 기본 공격 스킬 사용 시, 수치만큼 자신의 출혈 횟수 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BoneNail].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Lose 1 Speed for every Stack\n- Take +20% damage from Bleed for every Stack (rounded down)\n- On Base Attack Skill Use, gain Bleed Count equal to Stack
   PL: - Maks. ładunków: 5\n- Traci 1 Szybkości za każdy ładunek\n- Otrzymuje +20% obrażeń od Krwawienia za każdy ładunek (zaokr. w dół)\n- Przy użyciu Umiejętności ataku podstawowego zyskuje Licznik Krwawienia równy ładunkom
574. [Słowo kluczowe [BoneNail] — tekst klimatyczny] 내던져진 부속기관. 뷔페가 밀어내고, 뱉어내고, 쏟아냈다.\n\n자신의 몸에서 나왔으나, 밖으로 나온 이상 자신의 것이 아니다. 그러나 설령 상대에게 박히게 되더라도, 그것은 상대의 것이 아니다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BoneNail].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A cast-off appendage. Buffet pushed it out, spat it forth, spilled it from within.\n\nThough it came from one's own body, once cast outside, it ceased to belong to the self. And even should it be inserted into another, it would never belong to that body either.
   PL: Odrzucona przydatka. Buffet ją wypchnął, wypluł, wylał z siebie.\n\nChoć przyszła z własnego ciała, skoro znalazła się na zewnątrz, przestała być swoją. A nawet gdyby przybić ją w czyimś ciele, nie stanie się jego.
575. [Słowo kluczowe [BuffetDream] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream]`
   limit: do 40 znaków
   EN: Pwie's Memories
   PL: Wspomnienia Pwie
576. [Słowo kluczowe [BuffetDream] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- For every Stack,\n · Base Offense Level -5\n · Base Defense Level -5\n · Clash Power -1\n- Turn Start: Heal (8 x Stack) SP
   PL: - Maks. ładunków: 5\n- Za każdy ładunek Podstawowy Poziom Ataku -5, Podstawowy Poziom Obrony -5, Moc Starcia -1\n- Na początku tury odzyskuje Poczytalność (8 x ładunki)
577. [Słowo kluczowe [BuffetDream1] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream1].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream1]`
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Słowo kluczowe [BuffetDream1] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream1].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Słowo kluczowe [BuffetDream1] — tekst klimatyczny] 신발… 기뻤어…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream1].flavor
   limit: do 120 znaków
   EN: The shoes... made me really happy...
   PL: Buty... ucieszyły mnie...
580. [Słowo kluczowe [BuffetDream2] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream2].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream2]`
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Słowo kluczowe [BuffetDream2] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream2].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Słowo kluczowe [BuffetDream2] — tekst klimatyczny] 눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream2].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Thanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Dziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
583. [Słowo kluczowe [BuffetDream3] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream3].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream3]`
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Słowo kluczowe [BuffetDream3] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream3].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Słowo kluczowe [BuffetDream3] — tekst klimatyczny] 같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream3].flavor
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Bawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
586. [Słowo kluczowe [BuffetDream4] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream4].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream4]`
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Słowo kluczowe [BuffetDream4] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream4].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Słowo kluczowe [BuffetDream4] — tekst klimatyczny] 배고팠어… 아프게 하고 싶지 않았어… 괴로웠어…\n\n같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream4].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I was hungry... I didn't want to hurt anybody... It hurt so much...\n\nWe went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Byłem głodny... nie chciałem nikogo ranić... bolało...\n\nBawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
589. [Słowo kluczowe [BuffetDream5] — nazwa] 뿌이의 기억
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream5].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDream5]`
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Słowo kluczowe [BuffetDream5] — opis] - 최댓값 : 5\n- 수치 1당, 기본 공격 레벨 -5, 기본 방어 레벨 -5, 합 위력 -1\n- 턴 시작 시 정신력 (8 x 수치) 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream5].desc
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Słowo kluczowe [BuffetDream5] — tekst klimatyczny] 멈출 수 없었어… 보고 싶었어… 계속 혼자여서… 같이 가고 싶었어…\n\n배고팠어… 아프게 하고 싶지 않았어… 괴로웠어…\n\n같이 모험했어… 재밌었어…\n\n눈 맞춰줘서… 고마웠어…\n\n신발… 기뻤어…
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDream5].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I couldn't stop... I missed you... I was all alone, so... I wanted to come with you...\n\nI was hungry... I didn't want to hurt anybody... It hurt so much...\n\nWe went on an adventure... It was fun...\n\nThanks... for meeting my eyes...\n\nThe shoes... made me really happy...
   PL: Nie mogłem przestać... tęskniłem... ciągle byłem sam... chciałem iść z tobą...\n\nByłem głodny... nie chciałem nikogo ranić... bolało...\n\nBawiliśmy się w przygodę... było fajnie...\n\nDziękuję... za spojrzenie mi w oczy...\n\nButy... ucieszyły mnie...
592. [Słowo kluczowe [BuffetDreamEnd] — nazwa] 나는… ‘뿌이’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDreamEnd].name
   kontekst: identyfikator tagu w tekstach: `[BuffetDreamEnd]`
   limit: do 40 znaków
   EN: I... am "Pwie".
   PL: Jestem... „Pwie”
593. [Słowo kluczowe [BuffetDreamEnd] — opis] - 기본 공격 레벨 -30\n- 기본 방어 레벨 -30\n- 받는 피해량 +100%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDreamEnd].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -30\n- Base Defense Level -30\n- Take +100% damage
   PL: - Podstawowy Poziom Ataku -30\n- Podstawowy Poziom Obrony -30\n- Otrzymuje obrażenia +100%
594. [Słowo kluczowe [BuffetDreamEnd] — tekst klimatyczny] 날 뿌이라 기억해줘.\n고마워.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetDreamEnd].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remember me as "Pwie," okay?\nThank you... for everything.
   PL: Zapamiętaj mnie jako „Pwie”.\nDziękuję... za wszystko.
595. [Słowo kluczowe [BuffetRevival] — nazwa] 붉은 신의 목소리
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRevival].name
   kontekst: identyfikator tagu w tekstach: `[BuffetRevival]`
   limit: do 40 znaków
   EN: Voice of the Crimson God
   PL: Głos Czerwonego Boga
596. [Słowo kluczowe [BuffetRevival] — opis] - 최댓값 : 3\n- 사망하지 않음\n- 턴 종료 시 1 감소\n- 이 효과 소멸 시 본래의 모습(르루주 고위 스태프)으로 돌아가며, 붉은 신의 뜯긴 살점 상태에서 남아있던 체력 10당, 정신력 5 회복. 맥동 횟수 2 얻음\n· 얻은 맥동 횟수가 10 이상이면, 맥동 횟수를 모두 소모하고 소모한 수치 5당, 다음 턴에 폭주[르 데지르] 1 얻음
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRevival].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Cannot be defeated\n- Turn End: Lose 1 Stack\n- When this effect expires,\n · Return to "Le Rouge Senior Staff" form\n · Heal 5 SP for every 10 HP that remained while this unit was in "Ripped Flesh of the Crimson God" form; gain +2 Pulsation Count\n · If this unit gained 10+ Pulsation Count, consume all Pulsation Count; then, gain 1 Uncontrollable Rampage [Le Désir] next turn for every 5 Stacks consumed
   PL: - Maks. ładunków: 3\n- Nie ginie\n- Na koniec tury traci 1 ładunek\n- Gdy ten efekt znika, wraca do pierwotnej postaci (starszy personel Le Rouge); za każde 10 HP, jakie pozostało mu w stanie Rozdartego Mięsa Czerwonego Boga, odzyskuje 5 Poczytalności; zyskuje 2 Licznika Pulsowania\n· Jeżeli zdobyte Liczniki Pulsowania wynoszą 10 lub więcej, zużywa je wszystkie i za każde 5 zużytych zyskuje w następnej turze 1 Niepowstrzymanej Furii [Le Désir]
597. [Słowo kluczowe [BuffetRevival] — tekst klimatyczny] 살고 또 살아라.\n\n경험한다는 것은, 산다는 것은.\n\n의식이 현재가 아닌 미래에 가 있는 것.\n기대하기 때문에 경험하고 싶은 것. 경험하고 싶기 때문에 살려는 것.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRevival].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Live, and live again.\n\nTo experience, to live, is for the mind to dwell not in the present, but already in the future.\n\nBecause one looks forward to what is yet to come, one longs to experience. And because one longs to experience, one chooses to go on living.
   PL: Żyj i żyj dalej.\n\nDoświadczanie, życie — polega na tym, że świadomość przebywa nie w teraźniejszości, lecz już w przyszłości.\nBo czemu człowiek oczekuje — dlatego chce doświadczać; a bo chce doświadczać — dlatego chce żyć.
598. [Słowo kluczowe [BuffetRouge] — nazwa] 폭주[르 데지르]
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRouge].name
   kontekst: identyfikator tagu w tekstach: `[BuffetRouge]`
   limit: do 50 znaków
   EN: Uncontrollable Rampage [Le Désir]
   PL: Niepowstrzymana Furia [Le Désir]
599. [Słowo kluczowe [BuffetRouge] — opis] - 최댓값 : 3\n- 속도 최솟값 +1, 최댓값 +1\n- 출혈로 받는 피해량 -50%\n- 출혈 피해로 사망하지 않음\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRouge].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Min & Max Speed +1\n- Take -50% damage from Bleed\n- Cannot be defeated by Bleed damage\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Min. Szybkość +1, Maks. Szybkość +1\n- Otrzymuje -50% obrażeń od Krwawienia\n- Nie ginie od obrażeń Krwawienia\n- Na koniec tury traci 1 ładunek
600. [Słowo kluczowe [BuffetRouge] — tekst klimatyczny] 절대 만족할 수 없다. 내 욕망이 아님에도, 내 것이라 착각하고 있기 때문에.\n\n이건 당신으로 인한, 당신으로부터 터져 나오는 욕망.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetRouge].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I can never be satisfied.\n\nEven though the desire is not truly mine, I mistake it for something that belongs to me.\n\nThis is a desire born of you—a desire that bursts forth from you, because of you.
   PL: Nigdy nie nasycę się dosyć.\n\nChoć ta żądza nie jest naprawdę moją, biorę ją za własną.\n\nTo żądza zrodzona z ciebie — żądza wybuchająca z ciebie, przez ciebie.
601. [Słowo kluczowe [BuffetScruple] — nazwa] 뿌이와의 경험
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetScruple].name
   kontekst: identyfikator tagu w tekstach: `[BuffetScruple]`
   limit: do 40 znaków
   EN: Shared with Pwie
   PL: Doświadczenie z Pwie
602. [Słowo kluczowe [BuffetScruple] — opis] - 속도 최솟값 +3, 최댓값 +3\n- 턴 시작 시 정신력 15 회복\n- 붉은 신[완숙]에게 받는 최종 피해량 -75%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetScruple].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Turn Start: Heal 15 SP\n- Take -75% final damage from The Crimson God [Adulthood]
   PL: - Min. i Maks. Szybkość +3\n- Na początku tury +15 Poczytalności\n- Otrzymuje -75% obrażeń końcowych od Czerwonego Boga [Dojrzałość]
603. [Słowo kluczowe [BuffetScruple] — tekst klimatyczny] 분명 우리는 뿌이와 함께했다.\n\n망설임이, 그런 느낌이 떠오른다.
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetScruple].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We shared an experience with Pwie. Together. That much is certain.\n\nHesitation begins to surface.
   PL: Na pewno dzieliliśmy doświadczenie z Pwie. Wspólnie. Na pewno.\n\nNarasta wahanie.
604. [Słowo kluczowe [BuffetResolve] — nazwa] 결단
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetResolve].name
   kontekst: identyfikator tagu w tekstach: `[BuffetResolve]`
   limit: do 40 znaków
   EN: Decision
   PL: Decyzja
605. [Słowo kluczowe [BuffetResolve] — opis] - 최댓값 : 1\n- 붉은 신[완숙]에게 가하는 피해량 +30%\n- 턴 시작 시 정신력 15 회복
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetResolve].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Deal +30% damage to The Crimson God [Adulthood]\n- Turn Start: Heal 15 SP
   PL: - Maks. ładunków: 1\n- Zadaje Czerwonemu Bogowi [Dojrzałość] obrażenia +30%\n- Na początku tury odzyskuje 15 Poczytalności
606. [Słowo kluczowe [BuffetResolve] — tekst klimatyczny] ‘관리자로서 선택해야만 하겠지.’\n‘그렇습니다.’\n‘…….’\n‘…….’\n‘…결정했어.’
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=BuffetResolve].flavor
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "As Manager... I have to choose, don't I?"\n\n"Correct, Manager."\n\n"......."\n\n"......."\n\n"... I've made my decision."
   PL: „Jako Kierownik... muszę wybrać, prawda?”\n„Zupełnie tak, Kierowniku.”\n„.......”\n„.......”\n„... podjąłem decyzję.”
607. [Słowo kluczowe [MeursaultBuffetEnd] — nazwa] 못 박는 자
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffetEnd].name
   kontekst: identyfikator tagu w tekstach: `[MeursaultBuffetEnd]`
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Słowo kluczowe [MeursaultBuffetEnd] — opis] - 속도 최솟값 +3, 최댓값 +3\n- 최종 위력 +3\n- 이번 전투에서 자신의 스킬 사용 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 2회)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=MeursaultBuffetEnd].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Final Power +3\n- On Skill Use, gain 2 additional E.G.O Resource for the said Skill's Affinity (2 times per turn)\n- Cannot Retreat
   PL: - Min. Szybkość +3, Maks. Szybkość +3\n- Moc Końcowa +3\n- W tej walce przy użyciu Umiejętności dodatkowo zyskuje 2 Zasoby E.G.O Grzechu tej Umiejętności (2 razy na turę)\n- Nie może się wycofać
609. [Słowo kluczowe [GrandBuffet_LowMorale] — nazwa] 르 데지르(le désir)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GrandBuffet_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[GrandBuffet_LowMorale]`
   limit: do 40 znaków
   EN: Le Désir
   PL: Le Désir
610. [Słowo kluczowe [GrandBuffet_LowMorale] — opis] - 사기 저하\n- 공격 레벨 3 증가\n- 방어 레벨 3 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GrandBuffet_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +3\n- Defense Level +3
   PL: - Niskie Morale\n- Poziom Ataku +3\n- Poziom Obrony +3
611. [Słowo kluczowe [GrandBuffet_Panic] — nazwa] 르 데지르(le désir)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GrandBuffet_Panic].name
   kontekst: identyfikator tagu w tekstach: `[GrandBuffet_Panic]`
   (powtórzenie elementu 609 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Słowo kluczowe [GrandBuffet_Panic] — opis] - 패닉\n- 공격 레벨 5 증가\n- 방어 레벨 5 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=GrandBuffet_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +5\n- Defense Level +5
   PL: - Panika\n- Poziom Ataku +5\n- Poziom Obrony +5
613. [Słowo kluczowe [LaRougeSuperior_LowMorale] — nazwa] 좀 더 가죽 밖으로!
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LaRougeSuperior_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LaRougeSuperior_LowMorale]`
   limit: do 40 znaków
   EN: Farther Past the Hide!
   PL: Skóra Jeszcze Dalej na Zewnątrz!
614. [Słowo kluczowe [LaRougeSuperior_LowMorale] — opis] - 사기 저하\n- 방어 레벨 2 감소\n- 공격 레벨 2 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LaRougeSuperior_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -2\n- Offense Level +2
   PL: - Niskie Morale\n- Poziom Obrony -2\n- Poziom Ataku +2
615. [Słowo kluczowe [LaRougeSuperior_Panic] — nazwa] 좀 더 가죽 밖으로!
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LaRougeSuperior_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LaRougeSuperior_Panic]`
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Słowo kluczowe [LaRougeSuperior_Panic] — opis] - 패닉\n- 방어 레벨 5 감소\n- 공격 레벨 3 증가
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=LaRougeSuperior_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5\n- Offense Level +3
   PL: - Panika\n- Poziom Obrony -5\n- Poziom Ataku +3
617. [Słowo kluczowe [Jeanne_LowMorale] — nazwa] 라 노제(la nausée)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Jeanne_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Jeanne_LowMorale]`
   limit: do 40 znaków
   EN: La Nausée
   PL: La Nausée
618. [Słowo kluczowe [Jeanne_LowMorale] — opis] - 사기 저하\n- 가하는 피해량 -10%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Jeanne_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal -10% damage
   PL: - Niskie Morale\n- Zadaje obrażenia -10%
619. [Słowo kluczowe [Jeanne_Panic] — nazwa] 라 노제(la nausée)
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Jeanne_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Jeanne_Panic]`
   (powtórzenie elementu 617 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Słowo kluczowe [Jeanne_Panic] — opis] - 패닉\n- 기본 위력 -1\n가하는 피해량 -10%
   źródło: BattleKeywords-a1c10p3.json :: dataList[id=Jeanne_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Base Power -1\n- Deal -10% damage
   PL: - Panika\n- Moc Bazowa -1\nZadaje obrażenia -10%

## Słowa kluczowe bitwy — BattleKeywords-a1c5p1
- plik gry: `BattleKeywords-a1c5p1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

621. [Słowo kluczowe [AaCePaBa] — nazwa] 강박
   źródło: BattleKeywords-a1c5p1.json :: dataList[id=AaCePaBa].name
   kontekst: identyfikator tagu w tekstach: `[AaCePaBa]`
   limit: do 40 znaków
   EN: Compulsion
   PL: Kompulsja
622. [Słowo kluczowe [AaCePaBa] — opis] 정신력 -25상태로 전투 시작. 턴 시작 시 정신력이 0 미만일 때 공격 위력 증가 3을 얻음.
   źródło: BattleKeywords-a1c5p1.json :: dataList[id=AaCePaBa].desc
   limit: do 120 znaków
   EN: Starts encounter with -25 SP. At less than 0 SP at Turn Start, gain 3 Attack Power Up.
   PL: Rozpoczyna walkę z Poczytalnością -25. Na początku tury przy Poczytalności poniżej 0 zyskuje 3 Wzrostu Mocy Ataku.
623. [Słowo kluczowe [AaCePaBa] — podsumowanie] 정신력이 0 미만일 때 공격 위력 증가 3을 얻음
   źródło: BattleKeywords-a1c5p1.json :: dataList[id=AaCePaBa].summary
   limit: do 120 znaków
   EN: At less than 0 SP, gain 3 Attack Power Up
   PL: Na początku tury przy Poczytalności poniżej 0 zyskuje 3 Wzrostu Mocy Ataku

## Słowa kluczowe bitwy — BattleKeywords-a1c5p2
- plik gry: `BattleKeywords-a1c5p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

624. [Słowo kluczowe [AaCePbBa] — nazwa] 창백한 소음
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBa].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBa]`
   limit: do 40 znaków
   EN: Pallid Noise
   PL: Blady Szum
625. [Słowo kluczowe [AaCePbBa] — opis] 정신력 감소 효율 +2.\n이 버프를 가지고 있을 때, 정신력이 -45이하라면 다음 턴에 소음 공황을 얻는다.\n턴 종료시 1 감소
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBa].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SP Loss Efficiency +2\nIf at less than or equal to -45 SP and inflicted with this buff, gain Noise Panic next turn.\nTurn End: Reduce this effect by 1
   PL: Wydajność utraty Poczytalności +2.\nPosiadając ten efekt, przy Poczytalności -45 lub niższej zyskuje w następnej turze Panikę Szumu.\nNa koniec tury traci 1 ładunek
626. [Słowo kluczowe [AaCePbBa] — podsumowanie] 정신력 감소 효율 +2
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBa].summary
   limit: do 120 znaków
   EN: SP Loss Efficiency +2
   PL: Wydajność utraty Poczytalności +2
627. [Słowo kluczowe [AaCePbBb] — nazwa] 소음 공황
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBb].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBb]`
   limit: do 40 znaków
   EN: Noise Panic
   PL: Panika Szumu
628. [Słowo kluczowe [AaCePbBb] — opis] 자신이 사용하는 모든 코인이 뒷면이 나옴.\n다음 턴에 사라짐
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBb].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every Coin this unit flips lands on tails.\nExpires next turn
   PL: Wszystkie Monety tej jednostki zawsze wypadają jako Rewers.\nZnika w następnej turze
629. [Słowo kluczowe [AaCePbBb] — podsumowanie] 모든 코인이 뒷면이 나옴
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBb].summary
   limit: do 120 znaków
   EN: Every Coin lands on tails
   PL: Wszystkie Monety wypadają jako Rewers
630. [Słowo kluczowe [AaCePbBc] — nazwa] 불순
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBc].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBc]`
   limit: do 40 znaków
   EN: Impurity
   PL: Nieczystość
631. [Słowo kluczowe [AaCePbBc] — opis] - 사기 저하\n- 취약 1을 얻음. 합 패배시 대상의 정신력 -2
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBc].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile. If this unit loses a clash, the target loses 2 SP
   PL: - Niskie Morale\n- Zyskuje 1 Wrażliwości. Po przegranej w Starciu cel traci 2 Poczytalności
632. [Słowo kluczowe [AaCePbBc] — podsumowanie] 합 패배시 대상의 정신력 -2
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBc].summary
   limit: do 120 znaków
   EN: Target loses 2 SP if this unit loses the clash
   PL: Po przegranej w Starciu cel traci 2 Poczytalności
633. [Słowo kluczowe [AaCePbBd] — nazwa] 불순
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBd].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBd]`
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Słowo kluczowe [AaCePbBd] — opis] - 패닉\n- 취약 2를 얻음. 합 패배시 대상의 정신력 -5
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBd].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Fragile. If this unit loses a clash, the target loses 5 SP
   PL: - Panika\n- Zyskuje 2 Wrażliwości. Po przegranej w Starciu cel traci 5 Poczytalności
635. [Słowo kluczowe [AaCePbBd] — podsumowanie] 합 패배시 대상의 정신력 -5
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBd].summary
   limit: do 120 znaków
   EN: Target loses 5 SP if this unit loses the clash
   PL: Po przegranej w Starciu cel traci 5 Poczytalności
636. [Słowo kluczowe [AaCePbBi] — nazwa] 형님의 시험
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBi].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBi]`
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Słowo kluczowe [AaCePbBi] — opis] 턴 종료 시 1 감소\n이 효과가 있는 동안 스킬 피해, 진동 폭발로 인한 흐트러짐 손상을 3배로 받음.\n이 효과가 사라질 때 흐트러짐 상태가 아닌 경우, 다음 턴 시작 시 피해량 증가 5를 얻음
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBi].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Lose 1 Stack\n- While this effect is active, triple the damage taken from Skills and the amount of Stagger Threshold raised from Tremor Burst\n- If this unit is not Staggered when this effect expires, gain 5 Damage Up at the next Turn Start
   PL: Na koniec tury traci 1 ładunek\nDopóki aktywny jest ten efekt, obrażenia od Umiejętności oraz obniżenie Progu Oszołomienia z Wyładowania Wstrząsu są potrajane.\nJeżeli przy znikaniu tego efektu jednostka nie jest oszołomiona, na początku następnej tury zyskuje 5 Wzrostu Obrażeń
638. [Słowo kluczowe [AaCePbBe] — nazwa] 앙갚음
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBe].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBe]`
   limit: do 40 znaków
   EN: Vengeance
   PL: Zemsta
639. [Słowo kluczowe [AaCePbBe] — opis] - 사기 저하\n- 턴 시작 시 공격 위력 증가 1, 방어 레벨 감소 3을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음. (최대 체력의 3%당 피해량 증가 1을 얻음)
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBe].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Attack Power Up and 3 Defense Level Down. Gain Damage Up based on the amount of damage taken last turn (1 Damage Up for every 3% of Max HP lost)
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrostu Mocy Ataku i 3 Spadku Poziomu Obrony, a Wzrost Obrażeń zależnie od obrażeń otrzymanych w poprzedniej turze (1 Wzrost Obrażeń za każde 3% Maks. HP utraconego)
640. [Słowo kluczowe [AaCePbBe] — podsumowanie] 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음.
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBe].summary
   limit: do 120 znaków
   EN: Gain Damage Up based on total damage taken last turn.
   PL: Zyskuje Wzrost Obrażeń zależnie od łącznych obrażeń otrzymanych w poprzedniej turze.
641. [Słowo kluczowe [AaCePbBf] — nazwa] 앙갚음
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBf].name
   kontekst: identyfikator tagu w tekstach: `[AaCePbBf]`
   (powtórzenie elementu 638 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Słowo kluczowe [AaCePbBf] — opis] - 패닉\n- 턴 시작 시 공격 위력 증가 2, 방어 레벨 감소 6을 얻고, 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음. (최대 체력의 3%당 피해량 증가 1을 얻음)
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBf].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Attack Power Up and 6 Defense Level Down. Gain Damage Up based on the amount of damage taken last turn\n(1 Damage Up for every 3% of Max HP lost)
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 6 Spadku Poziomu Obrony, a Wzrost Obrażeń zależnie od obrażeń otrzymanych w poprzedniej turze\n(1 Wzrost Obrażeń za każde 3% Maks. HP utraconego)
643. [Słowo kluczowe [AaCePbBf] — podsumowanie] 이전 턴에 받은 누적 피해량에 비례하여 피해량 증가를 얻음.
   źródło: BattleKeywords-a1c5p2.json :: dataList[id=AaCePbBf].summary
   (powtórzenie elementu 640 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-a1c5p3
- plik gry: `BattleKeywords-a1c5p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

644. [Słowo kluczowe [AaCePcBa] — nazwa] 표식
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBa].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBa]`
   limit: do 40 znaków
   EN: Marked
   PL: Oznaczony
645. [Słowo kluczowe [AaCePcBa] — opis] 우선 공격 지정 대상이 됨.\n피격시 얻는 모든 화상 위력, 화상 횟수의 2배를 추가로 얻음
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBa].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Will be primarily targeted.\nWhen hit, gain additional Burn Potency and Burn Count equal to 2 times the amount gained.
   PL: Staje się głównym celem ataków.\nPrzy trafieniu zyskuje dodatkowo podwójną ilość Siły Podpalenia i Licznika Podpalenia
646. [Słowo kluczowe [AaCePcBb] — nazwa] 형광등 파편
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBb].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBb]`
   limit: do 40 znaków
   EN: Fluorescence Shard
   PL: Odłamek Świetlówki
647. [Słowo kluczowe [AaCePcBb] — opis] 턴 시작 시 호흡 3 얻음, 호흡 횟수 2 증가
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBb].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 3 Poise and +2 Poise Count
   PL: Na początku tury zyskuje 3 Oddechu i Licznik Oddechu +2
648. [Słowo kluczowe [AaCePcBc] — nazwa] 맹목
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBc].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBc]`
   limit: do 40 znaków
   EN: Blind Obsession
   PL: Zaślepiona Obsesja
649. [Słowo kluczowe [AaCePcBc] — opis] 수치가 3이 되면 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBc].desc
   limit: do 120 znaków
   EN: At 3+ value, this unit becomes staggered.
   PL: Przy wartości 3 lub większej jednostka zostaje oszołomiona.
650. [Słowo kluczowe [AaCePcBg] — nazwa] 유충
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBg].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBg]`
   limit: do 40 znaków
   EN: Larva
   PL: Larwa
651. [Słowo kluczowe [AaCePcBg] — opis] 턴 종료 시 현재 체력이 가장 높은 아군에게 유충이 옮겨감.\n턴 시작 시 수치만큼 정신력 피해를 얻음.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBg].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Move Larva to the ally with the highest HP.\nTurn Start: Lose SP equal to the value of Larva on self.
   PL: Na koniec tury Larwa przenosi się na sojusznika z najwyższym HP.\nNa początku tury traci Poczytalność równą wartości Larwy.
652. [Słowo kluczowe [AaCePcBh] — nazwa] 녹색 점액
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBh].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBh]`
   limit: do 40 znaków
   EN: Green Slime
   PL: Zielony Śluz
653. [Słowo kluczowe [AaCePcBh] — opis] 감소할 때마다, 다음 턴에 녹색 점액을 생성함.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBh].desc
   limit: do 120 znaków
   EN: Generates Green Slime next turn every time this value shrinks
   PL: Za każdym razem, gdy wartość maleje, w następnej turze tworzy Zielony Śluz.
654. [Słowo kluczowe [AaCePcBi] — nazwa] 거친 호흡
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBi].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBi]`
   limit: do 40 znaków
   EN: Uneven Breathing
   PL: Nierówny Oddech
655. [Słowo kluczowe [AaCePcBi] — opis] 턴 종료 시 호흡을 5 잃음.\n가하는 피해량 +50%, 받는 피해량 +50%
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBi].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 5 Poise.\nDeal +50% damage and receive +50% damage
   PL: Na koniec tury traci 5 Oddechu.\nZadaje obrażenia +50% i otrzymuje +50%.
656. [Słowo kluczowe [AaCePcBj] — nazwa] 사냥감의 징표
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBj].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBj]`
   limit: do 40 znaków
   EN: Prey Mark
   PL: Piętno Zdobyczy
657. [Słowo kluczowe [AaCePcBj] — opis] 모든 피쿼드 선원의 타겟이 됨\n피쿼드 선원에게 받는 피해 50% 증가
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBj].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Pequod crew targets this unit\nTake +50% damage from Pequod crew
   PL: Wszyscy członkowie załogi Pequoda celują w tę jednostkę\nOtrzymuje +50% obrażeń od członków załogi Pequoda
658. [Słowo kluczowe [AaCePcBk] — nazwa] 결박
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBk].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBk]`
   limit: do 40 znaków
   EN: Tangle
   PL: Splecenie
659. [Słowo kluczowe [AaCePcBk] — opis] 포획 과 같은 대상에게 부여되면, 대상이 흐트러짐 상태가 됨. 이미 흐트러짐 상태인 대상에게는 이 효과가 적용되지 않음.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBk].desc
   limit: do 150 znaków
   EN: If inflicted against targets with Capture, Stagger target. Does not work against targets that are already Staggered.
   PL: Jeżeli nałożony na cel posiadający „Pojmanie”, cel zostaje oszołomiony. Na celach, które już są oszołomione, ten efekt nie działa.
660. [Słowo kluczowe [AaCePcBl] — nazwa] 포획
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBl].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBl]`
   limit: do 40 znaków
   EN: Capture
   PL: Pojmanie
661. [Słowo kluczowe [AaCePcBl] — opis] 결박 과 같은 대상에게 부여되면, 대상이 흐트러짐 상태가 됨. 이미 흐트러짐 상태인 대상에게는 이 효과가 적용되지 않음.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBl].desc
   limit: do 150 znaków
   EN: If inflicted against targets with Tangle, Stagger target. Does not work against targets that are already Staggered.
   PL: Jeżeli nałożony na cel posiadający „Splecenie”, cel zostaje oszołomiony. Na celach, które już są oszołomione, ten efekt nie działa.
662. [Słowo kluczowe [AaCePcBn] — nazwa] 거역할 수 없는 명령
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBn].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBn]`
   limit: do 40 znaków
   EN: Undefiable Command
   PL: Rozkaz Bez Dyskusji
663. [Słowo kluczowe [AaCePcBn] — opis] 스킬 사용 시 체력이 현재 체력의 10%만큼 감소. 스킬 최종 위력 +1,\n적중 시 에이해브의 정신력 8 회복, 자신과 에이해브에게 호흡 2 부여
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBn].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 10% of current HP when using a Skill. Skill Final Power +1\nOn Hit, Ahab heals 8 SP; apply 2 Poise to self and Ahab
   PL: Przy użyciu Umiejętności traci 10% obecnego HP; Moc Końcowa +1,\nPrzy trafieniu Ahab odzyskuje 8 Poczytalności, a jednostka i Ahab otrzymują 2 Oddechu
664. [Słowo kluczowe [AaCePcBn] — podsumowanie] 스킬 사용 시 체력 감소, 최종 위력 +1.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBn].summary
   limit: do 120 znaków
   EN: Lose HP when using a Skill; Final Power +1
   PL: Przy użyciu Umiejętności traci HP; Moc Końcowa +1.
665. [Słowo kluczowe [AaCePcBo] — nazwa] 핍의 자아
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBo].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBo]`
   limit: do 40 znaków
   EN: Pip's Ego
   PL: Ego Pipa
666. [Słowo kluczowe [AaCePcBo] — opis] 턴 시작 시 수치 1당 정신력 3 회복.\n회피 실패 시, 죄책감의 무게 스킬 사용 시 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBo].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Heal 3 SP per value.\nDecreases when using Weight of Guilt after failing Evade.\nTurn End: If at 0, get Staggered.
   PL: Na początku tury odzyskuje 3 Poczytalności za wartość.\nMaleje przy nieudanym Uniku i użyciu „Ciężaru Poczucia Winy”.\nNa koniec tury przy 0 — Oszołomienie.
667. [Słowo kluczowe [AaCePcBo] — podsumowanie] 수치에 비례하여 정신력 회복. 회피 실패 시, 특정 스킬 사용 시 감소.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBo].summary
   limit: do 120 znaków
   EN: Heal SP by value. Reduce value when using a certain Skill after failing Evade.
   PL: Odzyskuje Poczytalność zależnie od wartości. Maleje przy nieudanym Uniku oraz przy użyciu pewnej Umiejętności.
668. [Słowo kluczowe [AaCePcBp] — nazwa] 스타벅의 자아
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBp].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBp]`
   limit: do 40 znaków
   EN: Starbuck's Ego
   PL: Ego Starbucka
669. [Słowo kluczowe [AaCePcBp] — opis] 턴 시작 시 수치 5당 보호 1 얻음.\n사냥감의 징표 가 있는 대상과의 합 패배 시 합에서 파괴된 코인 수만큼 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBp].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Gain 1 Protection for every 5 value.\nDecreases for every Coin destroyed in Clash against targets with Prey Mark.\nTurn End: If at 0, get Staggered.
   PL: Na początku tury zyskuje 1 Ochrony za każde 5 wartości.\nMaleje o liczbę Monet zniszczonych w Starciu z celem posiadającym „Piętno Zdobyczy”.\nNa koniec tury przy wartości 0 jednostka zostaje oszołomiona.
670. [Słowo kluczowe [AaCePcBp] — podsumowanie] 수치에 비례하여 보호 얻음. 특정 대상과의 합 패배 시 감소.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBp].summary
   limit: do 120 znaków
   EN: Gain Protection by value. Reduce value when losing Clash against certain targets.
   PL: Zyskuje Ochronę zależnie od wartości. Maleje po przegranej w Starciu z pewnymi celami.
671. [Słowo kluczowe [AaCePcBq] — nazwa] 퀴케그의 자아
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBq].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBq]`
   limit: do 40 znaków
   EN: Queequeg's Ego
   PL: Ego Queequeg
672. [Słowo kluczowe [AaCePcBq] — opis] 턴 종료 시 보호막이 남아있으면 수치 증가\n턴 종료 시 보호막이 없거나 탈색된 참회 스킬 사용시 감소.\n턴 종료 시 수치가 0이면 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBq].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Gain value if Shielded\nTurn End: Lose value when without Shield or when using Bleached Atonement.\nTurn End: At 0, get Staggered.
   PL: Na koniec tury, gdy jest Tarcza, wartość rośnie\nNa koniec tury maleje bez Tarczy lub przy użyciu „Wybielonej Pokuty”.\nNa koniec tury przy 0 — Oszołomienie.
673. [Słowo kluczowe [AaCePcBq] — podsumowanie] 턴 종료 시 보호막 유무에 따라 수치 증가 또는 감소.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBq].summary
   limit: do 120 znaków
   EN: Turn End: Depending on whether this unit is Shielded or not, lose or gain value.
   PL: Na koniec tury wartość rośnie lub maleje zależnie od obecności Tarczy.
674. [Słowo kluczowe [AaCePcBe] — nazwa] 하얀 공황
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBe].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBe]`
   limit: do 40 znaków
   EN: Pallid Panic
   PL: Blada Panika
675. [Słowo kluczowe [AaCePcBe] — opis] 정신력 감소 효율 +2
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBe].desc
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Słowo kluczowe [AaCePcBf] — nazwa] 하얀 공황
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBf].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBf]`
   (powtórzenie elementu 674 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Słowo kluczowe [AaCePcBf] — opis] 턴 종료 시 속박 2를 얻음.\n자신이 사용하는 모든 코인이 뒷면이 나옴.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBf].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 2 Bind at Turn End.\nEvery Coin this unit flips lands on tails.
   PL: Na koniec tury zyskuje 2 Spętania.\nWszystkie Monety tej jednostki zawsze wypadają jako Rewers.
678. [Słowo kluczowe [AaCePcBr] — nazwa] 원호 방어 보호막
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBr].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBr]`
   limit: do 40 znaków
   EN: Assist Barrier
   PL: Tarcza Obrony Wsparcia
679. [Słowo kluczowe [AaCePcBr] — opis] 피격 시 피해만큼 수치 감소.\n턴 종료 시 사라지지 않음.\n턴 종료 시 수치가 0이 되면 다음 턴에 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBr].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduce value by the amount of damage taken.\nDoes not expire at the end of the turn.\nTurn End: If this value is at 0, get Staggered next turn.
   PL: Przy trafieniu maleje o ilość otrzymanych obrażeń.\nNie znika na koniec tury.\nNa koniec tury przy wartości 0 jednostka zostaje oszołomiona w następnej turze.
680. [Słowo kluczowe [AaCePcBs] — nazwa] 원호 방어
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBs].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBs]`
   limit: do 40 znaków
   EN: Assist Defense
   PL: Obrona Wsparcia
681. [Słowo kluczowe [AaCePcBs] — opis] 에이해브를 공격하는 스킬의 타겟팅이 자신의 슬롯으로 이동됨.\n이 효과를 가진 캐릭터의 슬롯 가중치가 무제한으로 증가함.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBs].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pull skills targeting Ahab to this unit's slot.\nThe unit with this effect has unlimited Slot Weight.
   PL: Umiejętności atakujące Ahaba przenoszą celowanie na slot tej jednostki.\nWaga Slotu jednostki z tym efektem rośnie bez limitu.
