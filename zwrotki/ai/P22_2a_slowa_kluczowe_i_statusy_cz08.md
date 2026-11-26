# Paczka AI P22 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 8/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P22_2a_slowa_kluczowe_i_statusy_cz08.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P22_2a_slowa_kluczowe_i_statusy_cz08.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords_Refraction5
- plik gry: `BattleKeywords_Refraction5.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [MRR541] — opis] 모든 적이 출혈 위력이 가장 낮은 아군이 메인 타겟이면, 공격 시 스킬 최종 위력 +1
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR541].desc
   limit: do 140 znaków
   EN: When all enemies mainly target the ally with the least Bleed Potency, Skill Final Power +1 when attacking
   PL: Gdy głównym celem wszystkich wrogów jest sojusznik z najniższą Mocą Krwawienia, przy ataku zyskuje Moc Końcową Umiejętności +1
2. [Słowo kluczowe [MRR542] — nazwa] 체력 굴절
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR542].name
   kontekst: identyfikator tagu w tekstach: `[MRR542]`
   limit: do 40 znaków
   EN: Health Refraction
   PL: Załamanie HP
3. [Słowo kluczowe [MRR542] — opis] 적의 최대 체력 +10%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR542].desc
   limit: do 120 znaków
   EN: Enemy Max HP +10%
   PL: Maks. HP wrogów +10%
4. [Słowo kluczowe [MRR543] — nazwa] 이어지는 의지
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR543].name
   kontekst: identyfikator tagu w tekstach: `[MRR543]`
   limit: do 40 znaków
   EN: Lasting Determination
   PL: Trwała Wola
5. [Słowo kluczowe [MRR543] — opis] 사망시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻음.
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR543].desc
   limit: do 130 znaków
   EN: When defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this unit has.
   PL: Po śmierci zyskuje zasoby E.G.O zgodne z atrybutem posiadanych podstawowych Umiejętności ataku, w ilości równej ich randze
6. [Słowo kluczowe [FellBulletGroggy] — nazwa] 징표
   źródło: BattleKeywords_Refraction5.json :: dataList[id=FellBulletGroggy].name
   kontekst: identyfikator tagu w tekstach: `[FellBulletGroggy]`
   limit: do 40 znaków
   EN: Stigmatized
   PL: Napiętnowany
7. [Słowo kluczowe [FellBulletGroggy] — opis] - 해제 불가능\n- 턴 종료 시 0이 되면, 다음 턴에 흐트러짐 상태가 됨\n- 대상 지정 사격 스킬 사용시 타겟에게 징표가 없으면 1 감소\n- 대상 조정 사격 스킬이 합에서 패배하면 1 감소\n- 대상 조정 사격 스킬 사용 전 타겟으로 삼은 아군이 사망한 경우 1 감소
   źródło: BattleKeywords_Refraction5.json :: dataList[id=FellBulletGroggy].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot be removed\n- If at 0 at Turn End, become Staggered next turn\n- When using 'Designated Target Fire' Skill, if the target isn't Stigmatized, lose 1 Stack\n- If the 'Designated Target Fire' Skill loses the Clash, lose 1 Stack\n- If the ally this unit targeted before using the 'Designated Target Fire' Skill is killed, lose 1 Stack
   PL: - Nie można go usunąć\n- Jeśli na koniec tury osiąga 0, w następnej turze popada w stan Oszołomienia\n- Przy użyciu Umiejętności 'Wystrzał Wskazanego Celu', jeśli cel nie posiada Napiętnowania, maleje o 1\n- Jeśli Umiejętność 'Wystrzał Wskazanego Celu' przegra Starcie, maleje o 1\n- Jeśli sojusznik wskazany jako cel przed użyciem Umiejętności 'Wystrzał Wskazanego Celu' zginie, maleje o 1
8. [Słowo kluczowe [MRR544] — nazwa] 위력 룰렛
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR544].name
   kontekst: identyfikator tagu w tekstach: `[MRR544]`
   limit: do 40 znaków
   EN: Power Roulette
   PL: Ruletka Mocy
9. [Słowo kluczowe [MRR544] — opis] 턴 시작 시 모든 아군의 스킬 최종 위력  +1 ~ 3
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR544].desc
   limit: do 120 znaków
   EN: Turn Start: All ally Skills gain Final Power +1~3
   PL: Na początek tury Moc Końcowa Umiejętności wszystkich sojuszników +1~3
10. [Słowo kluczowe [MRR545] — nazwa] 유리 대포
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR545].name
   kontekst: identyfikator tagu w tekstach: `[MRR545]`
   limit: do 40 znaków
   EN: Glass Cannon
   PL: Szklane Działo
11. [Słowo kluczowe [MRR545] — opis] 모든 아군의 가하는 피해량 +20%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR545].desc
   limit: do 120 znaków
   EN: All allies deal +20% damage
   PL: Wszyscy sojusznicy zadają +20% obrażeń
12. [Słowo kluczowe [MRR546] — nazwa] 하이리스크
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR546].name
   kontekst: identyfikator tagu w tekstach: `[MRR546]`
   limit: do 40 znaków
   EN: High-risk
   PL: Wysokie Ryzyko
13. [Słowo kluczowe [MRR546] — opis] 모든 아군의 가하는 피해량 +10%\n3구간 최종 보스의 참격, 관통, 타격 내성이 약점(x1.3)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR546].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All allies deal +10% damage\nChange the Slash, Pierce, Blunt Resistance of the Final Boss of Section 3 to Weak(x1.3)
   PL: Wszyscy sojusznicy zadają +10% obrażeń\nOdporności Cięcia, Przebicia i Uderzenia ostatecznego bossa 3. odcinka zmieniają się na słabość (x1.3)
14. [Słowo kluczowe [MRR547] — nazwa] 위력 룰렛
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR547].name
   kontekst: identyfikator tagu w tekstach: `[MRR547]`
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
15. [Słowo kluczowe [MRR547] — opis] 턴 시작 시 적의 스킬 최종 위력 +1 ~ 3
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR547].desc
   limit: do 120 znaków
   EN: Turn Start: All enemy Skills gain Final Power +1~3
   PL: Na początek tury Moc Końcowa Umiejętności wrogów +1~3
16. [Słowo kluczowe [MRR548] — nazwa] 위태로운 승부
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR548].name
   kontekst: identyfikator tagu w tekstach: `[MRR548]`
   limit: do 40 znaków
   EN: Perilous Contest
   PL: Ryzykowny Pojedynek
17. [Słowo kluczowe [MRR548] — opis] 적의 합 위력 +2
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR548].desc
   limit: do 120 znaków
   EN: Enemy Clash Power +2
   PL: Moc Starcia wrogów +2
18. [Słowo kluczowe [MRR549] — nazwa] 사생결단
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR549].name
   kontekst: identyfikator tagu w tekstach: `[MRR549]`
   limit: do 40 znaków
   EN: Life or Death
   PL: Życie albo Śmierć
19. [Słowo kluczowe [MRR549] — opis] 모든 아군의 최대 체력 -25%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR549].desc
   limit: do 120 znaków
   EN: -25% to max HP on all allies
   PL: Maks. HP wszystkich sojuszników -25%
20. [Słowo kluczowe [MRR550] — nazwa] 약간의 리스크
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR550].name
   kontekst: identyfikator tagu w tekstach: `[MRR550]`
   limit: do 40 znaków
   EN: Moderate Risk
   PL: Umiarkowane Ryzyko
21. [Słowo kluczowe [MRR550] — opis] 적의 더하기 코인 위력 +1
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR550].desc
   limit: do 120 znaków
   EN: Enemy Plus Coin Power +1
   PL: Moc Monet Plus wrogów +1
22. [Słowo kluczowe [MRR551] — nazwa] 굴절된 출혈
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR551].name
   kontekst: identyfikator tagu w tekstach: `[MRR551]`
   limit: do 40 znaków
   EN: Refracted Bleed
   PL: Załamane Krwawienie
23. [Słowo kluczowe [MRR551] — opis] 턴 시작 시 체력이 최대인 적에게 출혈 위력 5 부여, 횟수 3 증가 (적 1명당 부위별 전투당 1회 발동)
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR551].desc
   limit: do 150 znaków
   EN: Turn Start: inflict 5 Bleed Potency and +3 Count to enemies at max HP (once per enemy per Part per Encounter)
   PL: Na początek tury nakłada na wrogów o pełnym HP Moc Krwawienia 5 i +3 Licznika Krwawienia (raz na walkę dla każdego Parta każdego wroga)
24. [Słowo kluczowe [MRR552] — opis] 적 사망 시마다 다음 턴에 현재 체력이 가장 낮은 순으로 적 1명이 합 위력 증가 2 얻음
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR552].desc
   limit: do 150 znaków
   EN: Whenever an enemy dies, an enemy gains 2 Clash Power Up next turn, starting from the enemy with the least current HP
   PL: Za każdym razem, gdy ginie wróg, wróg z najniższym obecnym HP zyskuje 2 Wzrosty Mocy Starcia w następnej turze
25. [Słowo kluczowe [MRR5BaseP] — nazwa] 적용 중인 버프
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR5BaseP].name
   kontekst: identyfikator tagu w tekstach: `[MRR5BaseP]`
   limit: do 40 znaków
   EN: Active Buffs
   PL: Aktywne Wzmocnienia
26. [Słowo kluczowe [MRR5BaseN] — nazwa] 적용 중인 고난
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR5BaseN].name
   kontekst: identyfikator tagu w tekstach: `[MRR5BaseN]`
   limit: do 40 znaków
   EN: Active Trials
   PL: Aktywne Utrapienia
27. [Słowo kluczowe [MRR553] — nazwa] 한번의 숨
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR553].name
   kontekst: identyfikator tagu w tekstach: `[MRR553]`
   limit: do 40 znaków
   EN: A Single Breath
   PL: Pojedynczy Oddech
28. [Słowo kluczowe [MRR553] — opis] E.G.O 스킬의 피해량 +30%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR553].desc
   limit: do 120 znaków
   EN: E.G.O Skills deal +30% damage
   PL: Umiejętności E.G.O zadają +30% obrażeń
29. [Słowo kluczowe [MRR554] — opis] 모든 아군의 가하는 피해량 +15%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR554].desc
   limit: do 120 znaków
   EN: All allies deal +15% damage
   PL: Wszyscy sojusznicy zadają +15% obrażeń
30. [Słowo kluczowe [MRR555] — nazwa] 합 위력 굴절
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR555].name
   kontekst: identyfikator tagu w tekstach: `[MRR555]`
   limit: do 40 znaków
   EN: Clash Power Refraction
   PL: Załamanie Mocy Starcia
31. [Słowo kluczowe [MRR555] — opis] 적의 합 위력 +1
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR555].desc
   limit: do 120 znaków
   EN: Enemy Clash Power +1
   PL: Moc Starcia wrogów +1
32. [Słowo kluczowe [MRR556] — nazwa] 유리 대포
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR556].name
   kontekst: identyfikator tagu w tekstach: `[MRR556]`
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Słowo kluczowe [MRR556] — opis] 모든 아군의 받는 피해량 +30%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR556].desc
   limit: do 120 znaków
   EN: All allies take +30% damage
   PL: Wszyscy sojusznicy otrzymują +30% obrażeń
34. [Słowo kluczowe [MRR557] — nazwa] 굴절된 호흡
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR557].name
   kontekst: identyfikator tagu w tekstach: `[MRR557]`
   limit: do 40 znaków
   EN: Refracted Poise
   PL: Załamany Oddech
35. [Słowo kluczowe [MRR557] — opis] 크리티컬 피해량 +(10 + 보유한 호흡 위력과 횟수의 합)% (최대 50%)
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR557].desc
   limit: do 120 znaków
   EN: Deal +(10 + Poise Potency + Poise Count)% damage on Critical Hit (max 50%)
   PL: Obrażenia krytyczne +(10 + suma posiadanej Mocy Oddechu i Licznika Oddechu)% (maks. 50%)
36. [Słowo kluczowe [MRR558] — nazwa] 굴절된 분노
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR558].name
   kontekst: identyfikator tagu w tekstach: `[MRR558]`
   limit: do 40 znaków
   EN: Refracted Wrath
   PL: Załamany Gniew
37. [Słowo kluczowe [MRR558] — opis] 분노 속성 스킬 피해량 +30%\n3구간 최종 보스의 분노 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR558].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wrath Skills deal +30% damage\nChange the Wrath Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Gniewu zadają +30% obrażeń\nOdporność na Gniew ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
38. [Słowo kluczowe [MRR559] — nazwa] 굴절된 색욕
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR559].name
   kontekst: identyfikator tagu w tekstach: `[MRR559]`
   limit: do 40 znaków
   EN: Refracted Lust
   PL: Załamana Żądza
39. [Słowo kluczowe [MRR559] — opis] 색욕 속성 스킬 피해량 +30%\n3구간 최종 보스의 색욕 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR559].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lust Skills deal +30% damage\nChange the Lust Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Żądzy zadają +30% obrażeń\nOdporność na Żądzę ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
40. [Słowo kluczowe [MRR560] — nazwa] 굴절된 나태
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR560].name
   kontekst: identyfikator tagu w tekstach: `[MRR560]`
   limit: do 40 znaków
   EN: Refracted Sloth
   PL: Załamane Lenistwo
41. [Słowo kluczowe [MRR560] — opis] 나태 속성 스킬 피해량 +30%\n3구간 최종 보스의 나태 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR560].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sloth Skills deal +30% damage\nChange the Sloth Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Lenistwa zadają +30% obrażeń\nOdporność na Lenistwo ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
42. [Słowo kluczowe [MRR561] — nazwa] 굴절된 탐식
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR561].name
   kontekst: identyfikator tagu w tekstach: `[MRR561]`
   limit: do 40 znaków
   EN: Refracted Gluttony
   PL: Załamane Obżarstwo
43. [Słowo kluczowe [MRR561] — opis] 탐식 속성 스킬 피해량 +30%\n3구간 최종 보스의 탐식 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR561].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gluttony Skills deal +30% damage\nChange the Gluttony Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Obżarstwa zadają +30% obrażeń\nOdporność na Obżarstwo ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
44. [Słowo kluczowe [MRR562] — nazwa] 굴절된 우울
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR562].name
   kontekst: identyfikator tagu w tekstach: `[MRR562]`
   limit: do 40 znaków
   EN: Refracted Gloom
   PL: Załamana Posępność
45. [Słowo kluczowe [MRR562] — opis] 우울 속성 스킬 피해량 +30%\n3구간 최종 보스의 우울 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR562].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gloom Skills deal +30% damage\nChange the Gloom Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Posępności zadają +30% obrażeń\nOdporność na Posępność ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
46. [Słowo kluczowe [MRR563] — nazwa] 굴절된 오만
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR563].name
   kontekst: identyfikator tagu w tekstach: `[MRR563]`
   limit: do 40 znaków
   EN: Refracted Pride
   PL: Załamana Pycha
47. [Słowo kluczowe [MRR563] — opis] 오만 속성 스킬 피해량 +30%\n3구간 최종 보스의 오만 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR563].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pride Skills deal +30% damage\nChange the Pride Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Pychy zadają +30% obrażeń\nOdporność na Pychę ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
48. [Słowo kluczowe [MRR564] — nazwa] 굴절된 질투
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR564].name
   kontekst: identyfikator tagu w tekstach: `[MRR564]`
   limit: do 40 znaków
   EN: Refracted Envy
   PL: Załamana Zazdrość
49. [Słowo kluczowe [MRR564] — opis] 질투 속성 스킬 피해량 +30%\n3구간 최종 보스의 질투 내성이 약점(x1.25)으로 변경
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR564].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Envy Skills deal +30% damage\nChange the Envy Resistance of the Final Boss of Section 3 to Weak(x1.25)
   PL: Umiejętności atrybutu Zazdrości zadają +30% obrażeń\nOdporność na Zazdrość ostatecznego bossa 3. odcinka zmienia się na słabość (x1.25)
50. [Słowo kluczowe [MRR565] — nazwa] 안락함
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR565].name
   kontekst: identyfikator tagu w tekstach: `[MRR565]`
   limit: do 40 znaków
   EN: Comfy
   PL: Komfort
51. [Słowo kluczowe [MRR565] — opis] 모든 아군의 속도 최솟값, 최댓값 +2, 최대 체력 +25%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR565].desc
   limit: do 120 znaków
   EN: Raise Min & Max Speed values by 2 for all allies; Max HP +25%
   PL: Minimalna i maksymalna Szybkość wszystkich sojuszników +2, Maks. HP +25%
52. [Słowo kluczowe [MRR566] — nazwa] 공격성 굴절
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR566].name
   kontekst: identyfikator tagu w tekstach: `[MRR566]`
   limit: do 40 znaków
   EN: Hostile Refraction
   PL: Załamanie Agresywności
53. [Słowo kluczowe [MRR566] — opis] 적의 합 위력 +1, 가하는 피해량 +10%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR566].desc
   limit: do 120 znaków
   EN: Enemy Clash Power +1; enemies deal +10% damage
   PL: Moc Starcia wrogów +1, zadają +10% obrażeń
54. [Słowo kluczowe [MRR567] — nazwa] 하이리스크
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR567].name
   kontekst: identyfikator tagu w tekstach: `[MRR567]`
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Słowo kluczowe [MRR567] — opis] 적의 더하기 코인 위력 +2
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR567].desc
   limit: do 120 znaków
   EN: Enemy Plus Coin Power +2
   PL: Moc Monet Plus wrogów +2
56. [Słowo kluczowe [MRR568] — nazwa] 방어 굴절
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR568].name
   kontekst: identyfikator tagu w tekstach: `[MRR568]`
   limit: do 40 znaków
   EN: Defensive Refraction
   PL: Załamanie Obrony
57. [Słowo kluczowe [MRR568] — opis] 적의 방어 레벨 +3
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR568].desc
   limit: do 120 znaków
   EN: Enemy Defense Level +3
   PL: Poziom Obrony wrogów +3
58. [Słowo kluczowe [MRR569] — nazwa] 피해량 굴절
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR569].name
   kontekst: identyfikator tagu w tekstach: `[MRR569]`
   limit: do 40 znaków
   EN: Damage Refraction
   PL: Załamanie Obrażeń
59. [Słowo kluczowe [MRR569] — opis] 적의 가하는 피해량 +10%
   źródło: BattleKeywords_Refraction5.json :: dataList[id=MRR569].desc
   limit: do 120 znaków
   EN: Enemies deal +10% damage
   PL: Wrogowie zadają +10% obrażeń

## Słowa kluczowe bitwy — BattleKeywords_Refraction6
- plik gry: `BattleKeywords_Refraction6.json` (opisy wyświetlane w dymkach pomocy podczas walki)

60. [Słowo kluczowe [NoeulNageuneBuffA3] — nazwa] 노을 나그네의 수액
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA3].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffA3]`
   limit: do 40 znaków
   EN: Sunset Wayfarer's Sap
   PL: Sok Wędrowca Zachodu Słońca
61. [Słowo kluczowe [NoeulNageuneBuffA3] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 자신의 첫번째 흐트러짐 구간 삭제
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- Remove this unit's first Stagger Threshold
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Usuwa pierwszy Próg Oszołomienia
62. [Słowo kluczowe [NoeulNageuneBuffA4] — nazwa] 노을 나그네의 수액
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA4].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffA4]`
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Słowo kluczowe [NoeulNageuneBuffA4] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 파괴 불가 코인으로 피격 시 받는 피해량 -20%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA4].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- When hit by Unbreakable Coins, take -20% damage
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Przy trafieniu Niezniszczalnymi Monetami otrzymuje -20% obrażeń
64. [Słowo kluczowe [NoeulNageuneBuffA5] — nazwa] 노을 나그네의 수액
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA5].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffA5]`
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
65. [Słowo kluczowe [NoeulNageuneBuffA5] — opis] - 자신의 최대 체력 +50% (최대 200, 질투 죄종 제외)\n- 자신의 첫번째 흐트러짐 구간 삭제\n- 턴 종료 시 정신력이 가장 낮은 아군 4명의 정신력 4 회복 (패닉, 침식 상태인 아군 제외)
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffA5].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +50% max HP (max 200; excluding Peccatula Invidiae)\n- Remove this unit's first Stagger Threshold\n- Turn End: 4 allies that have the lowest SP heal 4 SP (excluding Panicked or Corroded allies)
   PL: - Maks. HP +50% (maks. 200, z wyłączeniem Peccatulum Zazdrości)\n- Usuwa pierwszy Próg Oszołomienia\n- Na koniec tury 4 sojuszników z najniższą Poczytalnością odzyskuje 4 Poczytalności (z wyłączeniem sojuszników w stanie Paniki lub Korozji)
66. [Słowo kluczowe [NoeulNageuneBuffB3] — nazwa] 노을 나그네의 나방
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB3].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffB3]`
   limit: do 40 znaków
   EN: Sunset Wayfarer's Moth
   PL: Ćma Wędrowca Zachodu Słońca
67. [Słowo kluczowe [NoeulNageuneBuffB3] — opis] - 턴 시작 시 전장에 자신과 같은 소속인 아군(자신 포함) 1명당, 공격 레벨 증가 1 얻음 (최대 4)
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB3].desc
   limit: do 150 znaków
   EN: - Turn Start: Gain 1 Offense Level Up for every allied unit (including self) in the same faction as self (max 4)
   PL: - Na początek tury za każdego sojusznika tej samej frakcji na polu walki (wliczając siebie) zyskuje 1 Wzrost Poziomu Ataku (maks. 4)
68. [Słowo kluczowe [NoeulNageuneBuffB4] — nazwa] 노을 나그네의 나방
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB4].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffB4]`
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Słowo kluczowe [NoeulNageuneBuffB4] — opis] - 매 턴마다 참격 피해량 증가 1, 관통 피해량 증가 1, 타격 피해량 증가 1 중 무작위 1개 얻음. 해당 속성의 E.G.O 스킬 사용 시 가하는 피해량 +50%\n- 파괴 불가 코인으로 적중 시 가하는 피해량 +20%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB4].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack of a random status, chosen from Slash DMG Up, Pierce DMG Up, and Blunt DMG Up. When using an E.G.O Skill of the corresponding Attack Type, deal +50% damage\n- On Hit with Unbreakable Coins, deal +20% damage
   PL: - Co turę zyskuje 1 losowy z efektów: Wzrost Obrażeń Cięcia, Wzrost Obrażeń Przebicia i Wzrost Obrażeń Uderzenia. Umiejętności E.G.O atrybutu zyskanego efektu zadają +50% obrażeń\n- Przy trafieniu Niezniszczalnymi Monetami zadaje +20% obrażeń
70. [Słowo kluczowe [NoeulNageuneBuffB5] — nazwa] 노을 나그네의 나방
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB5].name
   kontekst: identyfikator tagu w tekstach: `[NoeulNageuneBuffB5]`
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Słowo kluczowe [NoeulNageuneBuffB5] — opis] - 턴 시작 시 이미 사망한 아군 1명당, 공격 레벨 증가 1 얻음 (최대 6)\n- 전투 시작 시 완전 공명했으면, 완전 공명한 스킬이 가하는 피해량 +20%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=NoeulNageuneBuffB5].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Offense Level Up for every ally defeated in this Encounter (max 6)\n- Combat Start: On A-Reson., Skills that are a part of the A-Reson. chain deal +20% damage
   PL: - Na początek tury za każdego sojusznika, który już zginął, zyskuje 1 Wzrost Poziomu Ataku (maks. 6)\n- Jeśli na początku walki wywołano Rezonans Absolutny, Umiejętności z Rezonansem Absolutnym zadają +20% obrażeń
72. [Słowo kluczowe [HeatedWingScalesExplain] — nazwa] 달궈진 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=HeatedWingScalesExplain].name
   kontekst: identyfikator tagu w tekstach: `[HeatedWingScalesExplain]`
   limit: do 40 znaków
   EN: Incandescent Scale Dust
   PL: Rozżarzony Pył Łusek
73. [Słowo kluczowe [HeatedWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 회귀’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=HeatedWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Regression" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Regres' Motyla Splątanych Żywotów::Poczwarki
74. [Słowo kluczowe [TransparentWingScalesExplain] — nazwa] 예리한 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TransparentWingScalesExplain].name
   kontekst: identyfikator tagu w tekstach: `[TransparentWingScalesExplain]`
   limit: do 40 znaków
   EN: Acuate Scale Dust
   PL: Ostry Pył Łusek
75. [Słowo kluczowe [TransparentWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 현현’과 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TransparentWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Manifestation" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Manifestacja' Motyla Splątanych Żywotów::Poczwarki
76. [Słowo kluczowe [RustedWingScalesExplain] — nazwa] 녹슨 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=RustedWingScalesExplain].name
   kontekst: identyfikator tagu w tekstach: `[RustedWingScalesExplain]`
   limit: do 40 znaków
   EN: Rusted Scale Dust
   PL: Zardzewiały Pył Łusek
77. [Słowo kluczowe [RustedWingScalesExplain] — opis] - 나생접::고치의 스킬 ‘나생 - 도래’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=RustedWingScalesExplain].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Advent" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z Umiejętnością 'Splątany Żywot - Nadejście' Motyla Splątanych Żywotów::Poczwarki
78. [Słowo kluczowe [HeatedWingScales] — nazwa] 달궈진 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=HeatedWingScales].name
   kontekst: identyfikator tagu w tekstach: `[HeatedWingScales]`
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Słowo kluczowe [HeatedWingScales] — opis] - 나생접::고치의 ‘나생 - 회귀’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=HeatedWingScales].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Regression" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z 'Splątany Żywot - Regres' Motyla Splątanych Żywotów::Poczwarki
80. [Słowo kluczowe [TransparentWingScales] — nazwa] 예리한 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TransparentWingScales].name
   kontekst: identyfikator tagu w tekstach: `[TransparentWingScales]`
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Słowo kluczowe [TransparentWingScales] — opis] - 나생접::고치의 ‘나생 - 현현’과 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TransparentWingScales].desc
   limit: do 220 znaków
   EN: - +0.25 to Resistances against Attack Types and Affinities of Skills that Clashed against "Entangled Life - Manifestation" Skill of "Butterfly of Entangled Lives::The Pupa"
   PL: - +0.25 do Odporności na Typy Ataku i Atrybuty Umiejętności, które prowadziły Starcie z 'Splątany Żywot - Manifestacja' Motyla Splątanych Żywotów::Poczwarki
82. [Słowo kluczowe [RustedWingScales] — nazwa] 녹슨 비늘 가루
   źródło: BattleKeywords_Refraction6.json :: dataList[id=RustedWingScales].name
   kontekst: identyfikator tagu w tekstach: `[RustedWingScales]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Słowo kluczowe [RustedWingScales] — opis] - 나생접::고치의 스킬 ‘나생 - 도래’와 합을 진행한 스킬의 공격 유형, 속성 유형에 해당하는 내성 +0.25
   źródło: BattleKeywords_Refraction6.json :: dataList[id=RustedWingScales].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Słowo kluczowe [StackPast] — nazwa] 과거 상태 (비활성화)
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPast].name
   kontekst: identyfikator tagu w tekstach: `[StackPast]`
   limit: do 40 znaków
   EN: In the Past (Deactivated)
   PL: Stan Przeszłości (Nieaktywny)
85. [Słowo kluczowe [StackPast] — opis] - 패시브 ‘과거 [過去]’ 비활성화\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPast].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Past [過去]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Przeszłość [過去]' nieaktywny\n- Maks. 30
86. [Słowo kluczowe [StackPresent] — nazwa] 현재 상태 (비활성화)
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPresent].name
   kontekst: identyfikator tagu w tekstach: `[StackPresent]`
   limit: do 40 znaków
   EN: In the Present (Deactivated)
   PL: Stan Teraźniejszości (Nieaktywny)
87. [Słowo kluczowe [StackPresent] — opis] - 패시브 ‘현재 [現在]’ 비활성화\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPresent].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Present [現在]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Teraźniejszość [現在]' nieaktywny\n- Maks. 30
88. [Słowo kluczowe [StackFuture] — nazwa] 미래 상태 (비활성화)
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackFuture].name
   kontekst: identyfikator tagu w tekstach: `[StackFuture]`
   limit: do 40 znaków
   EN: In the Future (Deactivated)
   PL: Stan Przyszłości (Nieaktywny)
89. [Słowo kluczowe [StackFuture] — opis] - 패시브 ‘미래 [未來]’ 비활성화\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackFuture].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Future [未來]" Deactivated\n- Max Stack: 30
   PL: - Pasyw 'Przyszłość [未來]' nieaktywny\n- Maks. 30
90. [Słowo kluczowe [StackPastActivate] — nazwa] 과거 상태
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPastActivate].name
   kontekst: identyfikator tagu w tekstach: `[StackPastActivate]`
   limit: do 40 znaków
   EN: In the Past
   PL: Stan Przeszłości
91. [Słowo kluczowe [StackPastActivate] — opis] - 패시브 ‘과거 [過去]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 부여하는 화상 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 부여하는 화상 위력 +2, 화상 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 부여하는 화상 위력 +3, 화상 횟수 +2\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPastActivate].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Past [過去]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills inflict +1 more Burn Potency and Count\n· 11~20: Clash Power +1; Skills inflict +2 more Burn Potency and +1 more Burn Count\n· 21~30: Final Power +2; Skills inflict +3 more Burn Potency and +2 more Burn Count\n- Max Stack: 30
   PL: - Pasyw 'Przeszłość [過去]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności nadają Moc Podpalenia i Licznik Podpalenia +1\n· 11~20: Moc Starcia +1, Umiejętności nadają Moc Podpalenia +2 i Licznik Podpalenia +1\n· 21~30: Moc Końcowa +2, Umiejętności nadają Moc Podpalenia +3 i Licznik Podpalenia +2\n- Maks. 30
92. [Słowo kluczowe [StackPresentActivate] — nazwa] 현재 상태
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPresentActivate].name
   kontekst: identyfikator tagu w tekstach: `[StackPresentActivate]`
   limit: do 40 znaków
   EN: In the Present
   PL: Stan Teraźniejszości
93. [Słowo kluczowe [StackPresentActivate] — opis] - 패시브 ‘현재 [現在]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 획득하는 호흡 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 획득하는 호흡 위력 +2, 호흡 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 획득하는 호흡 위력 +3, 호흡 횟수 +2\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackPresentActivate].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Present [現在]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills gain +1 more Poise Potency and Count\n· 11~20: Clash Power +1; Skills gain +2 more Poise Potency and +1 more Poise Count\n· 21~30: Final Power +2; Skills gain +3 more Poise Potency and +2 more Poise Count\n- Max Stack: 30
   PL: - Pasyw 'Teraźniejszość [現在]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności zyskują Moc Oddechu i Licznik Oddechu +1\n· 11~20: Moc Starcia +1, Umiejętności zyskują Moc Oddechu +2 i Licznik Oddechu +1\n· 21~30: Moc Końcowa +2, Umiejętności zyskują Moc Oddechu +3 i Licznik Oddechu +2\n- Maks. 30
94. [Słowo kluczowe [StackFutureActivate] — nazwa] 미래 상태
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackFutureActivate].name
   kontekst: identyfikator tagu w tekstach: `[StackFutureActivate]`
   limit: do 40 znaków
   EN: In the Future
   PL: Stan Przyszłości
95. [Słowo kluczowe [StackFutureActivate] — opis] - 패시브 ‘미래 [未來]’ 활성화\n- 수치에 따라 효과 적용\n· 0~10 : 스킬로 부여하는 출혈 위력, 횟수 +1\n· 11~20 : 합 위력 +1, 스킬로 부여하는 출혈 위력 +2, 출혈 횟수 +1\n· 21~30 : 최종 위력 +2, 스킬로 부여하는 출혈 위력 +3, 출혈 횟수 +2\n- 최대 30
   źródło: BattleKeywords_Refraction6.json :: dataList[id=StackFutureActivate].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Passive "Future [未來]" activated\n- Gain different effects based on Stack:\n· 0~10: Skills inflict +1 more Bleed Potency and Count\n· 11~20: Clash Power +1; Skills inflict +2 more Bleed Potency and +1 more Bleed Count\n· 21~30: Final Power +2; Skills inflict +3 more Bleed Potency and +2 more Bleed Count\n- Max Stack: 30
   PL: - Pasyw 'Przyszłość [未來]' aktywny\n- Efekty zależne od wartości\n· 0~10: Umiejętności nadają Moc Krwawienia i Licznik Krwawienia +1\n· 11~20: Moc Starcia +1, Umiejętności nadają Moc Krwawienia +2 i Licznik Krwawienia +1\n· 21~30: Moc Końcowa +2, Umiejętności nadają Moc Krwawienia +3 i Licznik Krwawienia +2\n- Maks. 30
96. [Słowo kluczowe [TimeGap] — nazwa] 시간 괴리
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TimeGap].name
   kontekst: identyfikator tagu w tekstach: `[TimeGap]`
   limit: do 40 znaków
   EN: Temporal Disjunction
   PL: Rozdźwięk Czasu
97. [Słowo kluczowe [TimeGap] — opis] - 과거 상태/현재 상태/미래 상태에서 다른 상태로 전환될 때마다 수치 1 증가\n- 받는 피해량 +(수치 x 15)% (최대 150%)\n- 턴 시작 시 수치가 10이면, 취약 5 얻음\n- 최대 10
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TimeGap].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack every time this unit switches between In the Past / In the Present / In the Future\n- Take +(Stack x 15)% damage (max 150%)\n- Turn Start: At 10 Stack, gain 5 Fragile\n- Max Stack: 10
   PL: - Za każdą zmianę między Stanem Przeszłości / Stanem Teraźniejszości / Stanem Przyszłości a innym stanem rośnie o 1\n- Otrzymuje +(wartość x 15)% obrażeń (maks. 150%)\n- Na początek tury przy wartości 10 zyskuje 5 Wrażliwości\n- Maks. 10
98. [Słowo kluczowe [YesdragonSelfRefraction] — nazwa] 매화침[埋花針]
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonSelfRefraction].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonSelfRefraction]`
   limit: do 40 znaków
   EN: Flower-burying Pin [埋花針]
   PL: Igła Pogrzebania Kwiatów [埋花針]
99. [Słowo kluczowe [YesdragonSelfRefraction] — opis] - 최댓값: 10\n- 수치 2당, 공격 레벨 1 증가, 방어 레벨 1 증가\n- 수치가 5 이상이면, 최종 위력 +1\n- 수치가 최댓값이면, 코인 위력 +1\n- 매화침이 소모되면 소모된 수치 1당, 적에게 가장 부족한 E.G.O 자원 1개씩 지급
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonSelfRefraction].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Gain 1 Offense Level and 1 Defense Level for every 2 Stack\n- At 5+ Stack, Final Power +1\n- At max Stack, Coin Power +1\n- When consuming Flower-burying Pin, give 1 E.G.O resource of the least-owned Affinity for every Stack consumed
   PL: - Maks.: 10\n- Za każde 2 wartości Poziom Ataku +1 i Poziom Obrony +1\n- Przy wartości 5 lub więcej Moc Końcowa +1\n- Przy maksymalnej wartości Moc Monet +1\n- Po zużyciu Igły Pogrzebania Kwiatów za każdą zużytą wartość przyznaje wrogowi po 1 najbardziej mu brakującego zasobu E.G.O
100. [Słowo kluczowe [CondensedBloodRefraction] — nazwa] 용혈[龍血]
   źródło: BattleKeywords_Refraction6.json :: dataList[id=CondensedBloodRefraction].name
   kontekst: identyfikator tagu w tekstach: `[CondensedBloodRefraction]`
   limit: do 40 znaków
   EN: Dragon's Blood [龍血]
   PL: Krew Smoka [龍血]
101. [Słowo kluczowe [CondensedBloodRefraction] — opis] - 위력 최댓값: 50\n- 턴 종료 시 수치당 최대 체력의 1%만큼 체력 피해를 받음 (최소 1, 해당 피해로 인해 흐트러지지 않음)\n- 수비 스킬 사용 시 횟수 1 감소 (턴당 1회)\n- 턴 종료 시 위력이 2배로 증가하고, 횟수 1 감소\n- 해당 효과는 횟수가 0이 되어야만 해제됨
   źródło: BattleKeywords_Refraction6.json :: dataList[id=CondensedBloodRefraction].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 50\n- Turn End: Take 1% HP damage per Potency (min 1; cannot be Staggered by this effect)\n- Lose 1 Count when using a Defense Skill (once per turn)\n- Turn End: Double Potency and lose 1 Count\n- This effect can be removed only by reducing Count to 0
   PL: - Maks. Mocy: 50\n- Na koniec tury otrzymuje obrażenia HP równe 1% Maks. HP za każdą wartość (min. 1; nie popada w Oszołomienie z tych obrażeń)\n- Przy użyciu Umiejętności obrony Licznik maleje o 1 (raz na turę)\n- Na koniec tury Moc rośnie dwukrotnie, a Licznik maleje o 1\n- Ten efekt znika dopiero przy Liczniku 0
102. [Słowo kluczowe [DragonLanceRefraction] — nazwa] 매화첨[埋花櫼]
   źródło: BattleKeywords_Refraction6.json :: dataList[id=DragonLanceRefraction].name
   kontekst: identyfikator tagu w tekstach: `[DragonLanceRefraction]`
   limit: do 40 znaków
   EN: Flower-burying Wedge [埋花櫼]
   PL: Klin Pogrzebania Kwiatów [埋花櫼]
103. [Słowo kluczowe [DragonLanceRefraction] — opis] - 최댓값: 3\n- 응룡의 특정 스킬 강화
   źródło: BattleKeywords_Refraction6.json :: dataList[id=DragonLanceRefraction].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Enhances Yinglong's certain Skills
   PL: - Maks.: 3\n- Wzmacnia określone Umiejętności Yinglonga
104. [Słowo kluczowe [YesdragonPower] — nazwa] 용의 기운[龍氣]
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonPower].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonPower]`
   limit: do 40 znaków
   EN: Dragon's Spirit [龍氣]
   PL: Energia Smoka [龍氣]
105. [Słowo kluczowe [YesdragonPower] — opis] - 받는 피해량 -100%\n- 피격 후 해당 스킬 종료 시 소멸
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take -100% damage\n- When hit, expires at Skill End of the Skill that hit
   PL: - Otrzymuje -100% obrażeń\n- Znika po zakończeniu Umiejętności, która trafiła
106. [Słowo kluczowe [YesdragonWind] — nazwa] 변덕스러운 자비
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonWind].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonWind]`
   limit: do 40 znaków
   EN: Capricious Mercy
   PL: Kapryśne Miłosierdzie
107. [Słowo kluczowe [YesdragonWind] — opis] - 속도 최솟값, 최댓값 +3\n- 합 위력+2\n- 피격 후 해당 스킬 종료 시 소멸
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonWind].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Clash Power +2\n- When hit, expires at Skill End of the Skill that hit
   PL: - Minimalna i maksymalna Szybkość +3\n- Moc Starcia +2\n- Znika po zakończeniu Umiejętności, która trafiła
108. [Słowo kluczowe [TagGameBuff] — nazwa] 술래
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TagGameBuff].name
   kontekst: identyfikator tagu w tekstach: `[TagGameBuff]`
   limit: do 40 znaków
   EN: "It"
   PL: Berek
109. [Słowo kluczowe [TagGameBuff] — opis] - 일방 공격으로 가하는 피해량 -100%\n- 일방 공격으로 받는 피해량 +80%\n- 자신을 포함한 모든 질투 죄종은 스킬 슬롯에 수비 스킬만 장착함\n- 턴 종료 시 수치 1 감소
   źródło: BattleKeywords_Refraction6.json :: dataList[id=TagGameBuff].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal -100% damage using Unopposed Attacks\n- Take +80% damage from Unopposed Attacks\n- All Peccatulum Invidiae units, including this unit, equip only Defense Skills in their Skill Slots\n- Turn End: Lose 1 Stack
   PL: - Zadaje -100% obrażeń Atakami Niekwestionowanymi\n- Otrzymuje +80% obrażeń od Ataków Niekwestionowanych\n- Wszystkie Peccatulum Zazdrości, wliczając tę jednostkę, wyposażają w slotach Umiejętności wyłącznie Umiejętności obrony\n- Na koniec tury maleje o 1
110. [Słowo kluczowe [YesdragonScale] — nazwa] 뒤덮은 비늘
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonScale].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonScale]`
   limit: do 40 znaków
   EN: Scaleclad
   PL: Pokrywające Łuski
111. [Słowo kluczowe [YesdragonScale] — opis] - 최댓값: 20\n- 해당 효과는 수치가 0이 되더라도 소멸하지 않음\n- 매화침으로 인한 피해를 받을 시 수치가 1 감소\n- 수치가 1 감소할 때 마다, 받는 피해량 +10%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=YesdragonScale].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Does not expire at 0 Stack\n- Lose 1 Stack when taking damage due to Flower-burying Pin\n- Take +10% damage for every Stack lost
   PL: - Maks.: 20\n- Ten efekt nie znika nawet przy wartości 0\n- Przy otrzymaniu obrażeń od Igły Pogrzebania Kwiatów maleje o 1\n- Za każdy spadek o 1 otrzymuje +10% obrażeń
112. [Słowo kluczowe [ObservationTheRingsRail] — nazwa] 조망
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ObservationTheRingsRail].name
   kontekst: identyfikator tagu w tekstach: `[ObservationTheRingsRail]`
   limit: do 40 znaków
   EN: Viewing the Tableau
   PL: Podziwianie Tableau
113. [Słowo kluczowe [ObservationTheRingsRail] — opis] - 기본 공격 레벨 20 감소\n- 기본 방어 레벨 20 감소\n- 약지 제자가 전투 가능 상태면, 턴 시작 시 보호 7 얻음
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ObservationTheRingsRail].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -20\n- Base Defense Level -20\n- Turn Start: Gain 7 Protection if The Ring Apprentice has not retreated from this Encounter
   PL: - Bazowy Poziom Ataku -20\n- Bazowy Poziom Obrony -20\n- Jeśli Uczeń Pierścienia może walczyć, na początek tury zyskuje 7 Ochrony
114. [Słowo kluczowe [ObservationTheRingsRail] — tekst klimatyczny] “갤러리에서 작품을 감상할 때는 느긋하고 여유롭게. 서두르지 않는 것이 중요하답니다.”
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ObservationTheRingsRail].flavor
   limit: do 180 znaków
   EN: "The appreciation of artwork in a gallery calls for unhurried contemplation. Please remember—impatience dulls the appreciation of art."
   PL: „Podziwianie dzieł sztuki w galerii wymaga niespiesznej kontemplacji. Proszę pamiętać — niecierpliwość tępi wrażliwość na sztukę.”
115. [Słowo kluczowe [MiddleFingerLeashBuff] — nazwa] 억제된 힘
   źródło: BattleKeywords_Refraction6.json :: dataList[id=MiddleFingerLeashBuff].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerLeashBuff]`
   limit: do 40 znaków
   EN: Suppressed Might
   PL: Stłumiona Siła
116. [Słowo kluczowe [MiddleFingerLeashBuff] — opis] - 일방 공격으로 가하는 피해량 -100%\n- 이번 전투에 아군이 3명 이상 사망했으면, 턴 종료 시 이 효과 소멸
   źródło: BattleKeywords_Refraction6.json :: dataList[id=MiddleFingerLeashBuff].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unopposed Attacks deal -100% damage\n- Turn End: If 3+ allies are defeated in this Encounter, this effect expires
   PL: - Zadaje -100% obrażeń Atakami Niekwestionowanymi\n- Jeśli w tej walce zginęło 3 lub więcej sojuszników, ten efekt znika na koniec tury
117. [Słowo kluczowe [ScarBygoneDaysRefraction_LowMorale] — nazwa] 애증
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ScarBygoneDaysRefraction_LowMorale]`
   limit: do 40 znaków
   EN: Affection and Resentment
   PL: Miłość i Uraza
118. [Słowo kluczowe [ScarBygoneDaysRefraction_LowMorale] — opis] 가하는 피해량과 받는 피해량 +10%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_LowMorale].desc
   limit: do 120 znaków
   EN: Deal and take +10% damage
   PL: Zadaje i otrzymuje +10% obrażeń
119. [Słowo kluczowe [ScarBygoneDaysRefraction_Panic] — nazwa] 애증
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ScarBygoneDaysRefraction_Panic]`
   (powtórzenie elementu 117 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Słowo kluczowe [ScarBygoneDaysRefraction_Panic] — opis] 가하는 피해량과 받는 피해량 +20%
   źródło: BattleKeywords_Refraction6.json :: dataList[id=ScarBygoneDaysRefraction_Panic].desc
   limit: do 120 znaków
   EN: Deal and take +20% damage
   PL: Zadaje i otrzymuje +20% obrażeń
121. [Słowo kluczowe [PainfulScarRailway_Panic] — nazwa] 모조된 아비
   źródło: BattleKeywords_Refraction6.json :: dataList[id=PainfulScarRailway_Panic].name
   kontekst: identyfikator tagu w tekstach: `[PainfulScarRailway_Panic]`
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
122. [Słowo kluczowe [PainfulScarRailway_Panic] — opis] - 패닉\n- 턴 시작 시, 화상 5, 화상 횟수 3, 출혈 5, 출혈 횟수 3 얻음
   źródło: BattleKeywords_Refraction6.json :: dataList[id=PainfulScarRailway_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 5 Burn, +3 Burn Count, 5 Bleed, and +3 Bleed Count
   PL: - Panika\n- Na początek tury zyskuje Moc Podpalenia 5, Licznik Podpalenia 3, Moc Krwawienia 5 i Licznik Krwawienia 3
123. [Słowo kluczowe [PainfulScarRailway_LowMorale] — nazwa] 모조된 아비
   źródło: BattleKeywords_Refraction6.json :: dataList[id=PainfulScarRailway_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[PainfulScarRailway_LowMorale]`
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Słowo kluczowe [PainfulScarRailway_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 화상 5, 출혈 5 얻음
   źródło: BattleKeywords_Refraction6.json :: dataList[id=PainfulScarRailway_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 5 Burn and 5 Bleed
   PL: - Niskie Morale\n- Na początek tury zyskuje Moc Podpalenia 5 i Moc Krwawienia 5

## Słowa kluczowe bitwy — BattleKeywords_Synergy
- plik gry: `BattleKeywords_Synergy.json` (opisy wyświetlane w dymkach pomocy podczas walki)

125. [Słowo kluczowe [SynergyActivationConditions_ForthMatchFlame] — nazwa] 시너지 발동 조건
   źródło: BattleKeywords_Synergy.json :: dataList[id=SynergyActivationConditions_ForthMatchFlame].name
   kontekst: identyfikator tagu w tekstach: `[SynergyActivationConditions_ForthMatchFlame]`
   limit: do 40 znaków
   EN: Synergy Activation Condition
   PL: Warunki Aktywacji Synergii
126. [Słowo kluczowe [SynergyActivationConditions_ForthMatchFlame] — opis] - [4번째 성냥불] 이상 : 환상 해석 5단계\n- [4번째 성냥불] 료슈 : 환상 해석 5단계\n- [4번째 성냥불] 로쟈 : 환상 해석 5단계
   źródło: BattleKeywords_Synergy.json :: dataList[id=SynergyActivationConditions_ForthMatchFlame].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - [4th Match Flame] Yi Sang: Threadspin Tier 5\n- [4th Match Flame] Ryōshū: Threadspin Tier 5\n- [4th Match Flame] Rodion: Threadspin Tier 5
   PL: - [4. Płomyk Zapałki] Yi Sang: Splot Nici na 5. stopniu\n- [4. Płomyk Zapałki] Ryōshū: Splot Nici na 5. stopniu\n- [4. Płomyk Zapałki] Rodion: Splot Nici na 5. stopniu

## Statusy i efekty bojowe — Bufs-BossRaid
- plik gry: `Bufs-BossRaid.json`

127. [Status [FavorBuffTwth1stPhaseForUI] — nazwa] 사영 [루주]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth1stPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwth1stPhaseForUI]`
   limit: do 40 znaków
   EN: Shade of Reflection [Rouge]
   PL: Cień Projekcji [Rouge]
128. [Status [FavorBuffTwth1stPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>색욕</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적이 <color=#f8c200>출혈</color>로 받는 피해량이 1.5배로 증가 (소수점 버림)\n- <color=#f8c200>완전 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth1stPhaseForUI].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Lust Skills</color> or <color=#f8c200>Skills that inflict Bleed or 'Unique Bleed'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Enemies take x1.5 damage from <color=#f8c200>Bleed</color> (rounded down)\n- Upon <color=#f8c200>A-Reson.</color>, gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for A-Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Krwawienie lub „Specjalne Krwawienie”</color> albo należą do Grzechu <color=#f8c200>Żądzy</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Wrogowie otrzymują 1,5x obrażeń od <color=#f8c200>Krwawienia</color> (zaokrąglane w dół)\n- Przy <color=#f8c200>Rezonansie Absolutnym</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
129. [Status [FavorBuffTwth2ndPhaseForUI] — nazwa] 사영 [블뢰]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth2ndPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwth2ndPhaseForUI]`
   limit: do 40 znaków
   EN: Shade of Reflection [Bleu]
   PL: Cień Projekcji [Bleu]
130. [Status [FavorBuffTwth2ndPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>침잠 또는 특수 침잠</color>을 부여하거나 <color=#f8c200>우울</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 턴 시작 시, <color=#f8c200>패닉 상태</color>인 적이 취약 3 얻음\n- <color=#f8c200>손가락 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -15%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth2ndPhaseForUI].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gloom Skills</color> or <color=#f8c200>Skills that inflict Sinking or 'Unique Sinking'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Turn Start: Enemies in <color=#f8c200>Panic</color> gain 3 Fragile\n- <color=#f8c200>The Finger-faction Identities</color> deal +15% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Zatonięcie lub „Specjalne Zatonięcie”</color> albo należą do Grzechu <color=#f8c200>Posępności</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Na początku tury wrogowie w stanie <color=#f8c200>Paniki</color> otrzymują 3 Wrażliwości\n- Tożsamości <color=#f8c200>frakcji Palca</color> zadają wrogom obrażenia +15%, a otrzymują -15%
131. [Status [FavorBuffTwthHardForUI] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHardForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthHardForUI]`
   limit: do 40 znaków
   EN: Tribulation
   PL: Utrapienie
132. [Status [FavorBuffTwthHardForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 부여하는 <color=#ff0000>출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰]</color> 부여량 +1\n- 대상에게 <color=#ff0000>강렬한 색채</color>가 있으면, 합 위력 +2, 기본 위력 +1\n- [2페이즈 전용] ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’를 사용하는 턴 시작 시, <color=#ff0000>강렬한 색채</color>를 보유한 수감자 1명당 <color=#ff0000>정신력 10 회복</color> (최대 30)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHardForUI].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills inflict +1 more <color=#ff0000>Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]</color>\n- If target has <color=#ff0000>Palette Vibrante</color>, Clash Power +2 and Base Power +1\n- [Phase 2 exclusive effect] Turn Start: If this unit will use "Burst Forth the Pulsing Crimson under Your Skin" this turn, <color=#ff0000>heal 10 SP on self</color> for every Sinner that has <color=#ff0000>Palette Vibrante</color> (max 30 SP)
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności nakładają o 1 więcej <color=#ff0000>Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]</color>\n- Jeżeli cel posiada <color=#ff0000>Palette Vibrante</color>, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury, w której ta jednostka użyje „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za każdego Grzesznika z <color=#ff0000>Palette Vibrante</color> <color=#ff0000>odzyskuje 10 Poczytalności</color> (maks. 30)
133. [Status [FavorBuffTwth] — nazwa] 사영 [루주]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwth]`
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Status [FavorBuffTwth] — opis] - 출혈 또는 특수 출혈을 부여하거나 색욕 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 완전 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Attack Skills that are Lust Skills or Skills that inflict Bleed or 'Unique Bleed' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- Upon A-Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for A-Reson. (2 times per turn)
   PL: - Umiejętności ataku, które nakładają Krwawienie lub „Specjalne Krwawienie” albo należą do Grzechu Żądzy, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy Rezonansie Absolutnym zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
135. [Status [FavorBuffTwth] — podsumowanie] 출혈, 특수 출혈, 색욕 속성 스킬 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwth].summary
   limit: do 120 znaków
   EN: Bleed Skills, 'Unique Bleed' Skills, and Lust Skills deal more damage
   PL: Umiejętności Krwawienia, „Specjalnego Krwawienia” i Grzechu Żądzy zadają więcej obrażeń
136. [Status [FavorBuffTwthEnemy] — nazwa] 사영 [루주]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthEnemy]`
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Status [FavorBuffTwthEnemy] — opis] - 출혈로 받는 피해량이 1.5배로 증가 (소수점 버림)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].desc
   limit: do 120 znaków
   EN: - Take x1.5 damage from Bleed (rounded down)
   PL: - Otrzymujesz 1,5x obrażeń od Krwawienia (zaokrąglane w dół)
138. [Status [FavorBuffTwthEnemy] — podsumowanie] 출혈로 받는 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemy].summary
   limit: do 120 znaków
   EN: Take more damage from Bleed
   PL: Otrzymujesz więcej obrażeń od Krwawienia
139. [Status [FavorBuffTwthTwo] — nazwa] 사영 [블뢰]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthTwo]`
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Status [FavorBuffTwthTwo] — opis] - 침잠 또는 특수 침잠을 부여하거나 우울 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 손가락 소속 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -15%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthTwo].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Attack Skills that are Gloom Skills or Skills that inflict Sinking or 'Unique Sinking' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- The Finger-faction Identities deal +15% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku, które nakładają Zatonięcie lub „Specjalne Zatonięcie” albo należą do Grzechu Posępności, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Tożsamości frakcji Palca zadają wrogom obrażenia +15%, a otrzymują -15%
141. [Status [FavorBuffTwthTwo] — podsumowanie] 침잠, 특수 침잠, 우울 속성 스킬 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthTwo].summary
   limit: do 120 znaków
   EN: Sinking Skills, 'Unique Sinking' Skills, and Gloom Skills deal more damage
   PL: Umiejętności Zatonięcia, „Specjalnego Zatonięcia” i Grzechu Posępności zadają więcej obrażeń
142. [Status [FavorBuffTwthEnemyTwo] — nazwa] 사영 [블뢰]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthEnemyTwo]`
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [Status [FavorBuffTwthEnemyTwo] — opis] - 턴 시작 시, 패닉 상태면 취약 3 얻음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].desc
   limit: do 120 znaków
   EN: - Turn Start: When Panicked, gain 3 Fragile
   PL: - Na początku tury, jeżeli jednostka jest w stanie Paniki, otrzymuje 3 Wrażliwości
144. [Status [FavorBuffTwthEnemyTwo] — podsumowanie] 패닉 상태면 취약 얻음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthEnemyTwo].summary
   limit: do 120 znaków
   EN: When Panicked, gain Fragile
   PL: W stanie Paniki jednostka otrzymuje Wrażliwość
145. [Status [FavorBuffTwthHard] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHard].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthHard]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Status [FavorBuffTwthHard] — opis] - 최대 체력 +25%\n- 스킬로 부여하는 출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰] 부여량 +1\n- 대상에게 강렬한 색채가 있으면, 합 위력 +2, 기본 위력 +1
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHard].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- Skills inflict +1 more Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]\n- If target has Palette Vibrante, Clash Power +2 and Base Power +1
   PL: - Maks. HP +25%\n- Umiejętności nakładają o 1 więcej Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]\n- Jeżeli cel posiada Palette Vibrante, Moc Starcia +2 i Moc Bazowa +1
147. [Status [FavorBuffTwthHard] — podsumowanie] 출혈 위력, 침잠 위력, 찢긴 색채 부여량 증가\n대상에게 강렬한 색채가 있으면 합 위력, 기본 위력이 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHard].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict more Bleed Potency, Sinking Potency, and Mauled Color\nIf target has Palette Vibrante, gain Clash Power and Base Power
   PL: Umiejętności nakładają więcej Siły Krwawienia, Siły Zatonięcia i Rozdartych Barw\nJeżeli cel posiada Palette Vibrante, Moc Starcia i Moc Bazowa rosną
148. [Status [FavorBuffTwthHardTwo] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffTwthHardTwo]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Status [FavorBuffTwthHardTwo] — opis] - 최대 체력 +25%\n- 스킬로 부여하는 출혈 위력, 침잠 위력, 찢긴 색채 [루주], 찢긴 색채 [블뢰] 부여량 +1\n- 대상에게 강렬한 색채가 있으면, 합 위력 +2, 기본 위력 +1\n- [2페이즈 전용] ‘당신의 피부 아래 맥동하는 붉은 색감을 거칠게.’를 사용하는 턴 시작 시, 강렬한 색채를 보유한 수감자 1명당 정신력 10 회복 (최대 30)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- Skills inflict +1 more Bleed Potency, Sinking Potency, Mauled Color [Rouge], and Mauled Color [Bleu]\n- If target has Palette Vibrante, Clash Power +2 and Base Power +1\n- [Phase 2 exclusive effect] Turn Start: If this unit will use "Burst Forth the Pulsing Crimson under Your Skin" this turn, heal 10 SP on self for every Sinner that has Palette Vibrante (max 30 SP)
   PL: - Maks. HP +25%\n- Umiejętności nakładają o 1 więcej Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]\n- Jeżeli cel posiada Palette Vibrante, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury, w której ta jednostka użyje „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za każdego Grzesznika z Palette Vibrante odzyskuje 10 Poczytalności (maks. 30)
150. [Status [FavorBuffTwthHardTwo] — podsumowanie] 출혈 위력, 침잠 위력, 찢긴 색채 부여량 증가\n대상에게 강렬한 색채가 있으면 합 위력, 기본 위력이 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffTwthHardTwo].summary
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Status [FavorBuff5001FirstPhaseForUI] — nazwa] 사영 [중지]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001FirstPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001FirstPhaseForUI]`
   limit: do 50 znaków
   EN: Shade of Reflection [The Middle]
   PL: Cień Projekcji [Środkowy]
152. [Status [FavorBuff5001FirstPhaseForUI] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 리카르도의 첫 번째, 두 번째 <color=#f8c200>패턴이 변경</color>되며, <color=#f8c200>모든 E.G.O 자원을 2개씩 얻음</color>\n- <color=#f8c200>수비 스킬을 장착</color>한 인격에게는 리카르도의 스킬 효과로 <color=#f8c200>마비가 부여되지 않음</color>\n- 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>질투</color> 속성에 해당하는 공격 스킬의 피해량 +30% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001FirstPhaseForUI].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, activate the following effects:\n · Ricardo's first and second <color=#f8c200>patterns change</color>\n · <color=#f8c200>Gain 2 E.G.O Resources for all Affinities</color>\n- Ricardo's Skill effects <color=#f8c200>do not inflict Paralyze</color> on Identities that have <color=#f8c200>equipped Defense Skills</color>\n- The Identities' Attack Skills that are <color=#f8c200>Envy</color> Skills or Skills that inflict <color=#f8c200>Bleed or 'Unique Bleed'</color> deal +30% damage (for E.G.O Skills, deal +100% damage instead)\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - Jeżeli na początku spotkania na polu jest co najmniej 4 Tożsamości <color=#f8c200>frakcji Środkowego</color>, pierwszy i drugi wzorzec Ricarda <color=#f8c200>ulega zmianie</color>, a Ty <color=#f8c200>zyskujesz po 2 Zasobów E.G.O każdego Grzechu</color>\n- Umiejętności Ricarda <color=#f8c200>nie nakładają Paraliżu</color> na Tożsamości, które mają <color=#f8c200>wyposażone Umiejętności obrony</color>\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Krwawienie lub „Specjalne Krwawienie”</color> albo należą do Grzechu <color=#f8c200>Zawiści</color>, zadają obrażenia +30% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Jeżeli na początku walki wywołano <color=#f8c200>Rezonans Absolutny</color>, 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O najmniej posiadanego Grzechu</color>
153. [Status [FavorBuff5001SecondPhaseForUI] — nazwa] 사영 [급습]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001SecondPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001SecondPhaseForUI]`
   limit: do 50 znaków
   EN: Shade of Reflection [Ambuscade]
   PL: Cień Projekcji [Zasadzka]
154. [Status [FavorBuff5001SecondPhaseForUI] — opis] - 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- <color=#f8c200>H사 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -30%\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>\n- 리카르도가 <color=#f8c200>흐트러짐 상태</color>일 때 공격자의 속도가 더 빠르면, (속도 차이 x 2)% 만큼 <color=#f8c200>받는 피해량이 증가</color> (최대 20%)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001SecondPhaseForUI].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gluttony</color> Skills or Skills that inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- <color=#f8c200>H Corp.</color> Identities deal +15% damage and take -30% damage\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>\n- If the attacker's Speed is faster than Ricardo's when he is <color=#f8c200>Staggered</color>, Ricardo takes <color=#f8c200>+(Speed difference x 2)% damage</color> (max 20%)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Rozdarcie</color> albo należą do Grzechu <color=#f8c200>Obżarstwa</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Tożsamości <color=#f8c200>Korporacji H</color> zadają wrogom obrażenia +15%, a otrzymują -30%\n- Jeżeli na początku walki wywołano <color=#f8c200>Rezonans Absolutny</color>, 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O najmniej posiadanego Grzechu</color>\n- Gdy Ricardo jest w stanie <color=#f8c200>Oszołomienia</color>, a atakujący jest szybszy, jego <color=#f8c200>otrzymywane obrażenia rosną</color> o (różnica Szybkości x 2)% (maks. 20%)
155. [Status [FavorBuff5001HardForUI] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001HardForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001HardForUI]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Status [FavorBuff5001HardForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%\n- [2페이즈 전용]\n · 리카르도와 아우들의 정신력이 0 미만으로 감소하지 않음\n · 턴 시작시 이전 턴에 리카르도를 공격한 모든 적에게 [장부에 적힘] 2 부여
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001HardForUI].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills deal +20% damage\n- [Phase 2 Exclusive Effect]\n · Ricardo and his Siblings' SP do not fall below 0\n · Turn Start: Inflict 2 "Written in the Book" on all enemies that attacked Ricardo in the previous turn
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności zadają obrażenia +20%\n- [Efekt wyłącznie 2. fazy]\n · Poczytalność Ricarda i jego Braci nie spada poniżej 0\n · Na początku tury na wszystkich wrogów, którzy w poprzedniej turze zaatakowali Ricarda, nakładane są 2 „Zapisano w Księdzie”
157. [Status [FavorBuff5001AllyFirst] — nazwa] 사영 [중지]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001AllyFirst]`
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Status [FavorBuff5001AllyFirst] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 모든 E.G.O 자원을 2개씩 얻음\n- 인격의 스킬 중 <color=#f8c200>출혈 또는 특수 출혈</color>을 부여하거나 <color=#f8c200>질투</color> 속성에 해당하는 공격 스킬의 피해량 +30% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 E.G.O 자원 1개를 4회 획득
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, gain 2 E.G.O Resources for all Affinities\n- The Identities' Attack Skills that are <color=#f8c200>Envy</color> Skills or Skills that inflict <color=#f8c200>Bleed or 'Unique Bleed'</color> deal +30% damage (for E.G.O Skills, deal +100% damage instead)\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności nakładają o 1 więcej <color=#ff0000>Siły Krwawienia, Siły Zatonięcia, Rozdartej Barwy [Rouge] i Rozdartej Barwy [Bleu]</color>\n- Jeżeli cel posiada <color=#ff0000>Palette Vibrante</color>, Moc Starcia +2 i Moc Bazowa +1\n- [Efekt wyłącznie 2. fazy] Na początku tury użycia „Wybuchającego Pulsującego Szkarłatu pod Twoją Skórą”, za Grzesznika z <color=#ff0000>Palette Vibrante</color> <color=#ff0000>odzyskuje 10 Poczytalności</color> (maks. 30)
159. [Status [FavorBuff5001AllyFirst] — podsumowanie] 출혈 스킬 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyFirst].summary
   limit: do 120 znaków
   EN: Bleed Skills deal more damage
   PL: Umiejętności Krwawienia zadają więcej obrażeń
160. [Status [FavorBuff5001EnemyFirst] — nazwa] 사영 [중지]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001EnemyFirst]`
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Status [FavorBuff5001EnemyFirst] — opis] - 스테이지 시작 시 <color=#f8c200>중지 소속</color> 인격이 4명 이상 출전한 상태면, 리카르도의 첫 번째, 두 번째 <color=#f8c200>패턴이 변경</color>됨\n- <color=#f8c200>수비 스킬을 장착</color>한 인격에게는 리카르도의 스킬 효과로 <color=#f8c200>마비가 부여되지 않음</color>
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - Encounter Start: If 4+ <color=#f8c200>The Middle-faction</color> Identities are on the field, Ricardo's first and second <color=#f8c200>patterns change</color>\n- Ricardo's Skill effects <color=#f8c200>do not inflict Paralyze</color> on Identities that have <color=#f8c200>equipped Defense Skills</color>
   PL: - Jeżeli na początku spotkania na polu jest co najmniej 4 Tożsamości <color=#f8c200>frakcji Środkowego</color>, pierwszy i drugi wzorzec Ricarda <color=#f8c200>ulega zmianie</color>\n- Umiejętności Ricarda <color=#f8c200>nie nakładają Paraliżu</color> na Tożsamości, które mają <color=#f8c200>wyposażone Umiejętności obrony</color>
162. [Status [FavorBuff5001EnemyFirst] — podsumowanie] 수비 스킬 장착 인격에게는 마비를 부여하지 않음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemyFirst].summary
   limit: do 120 znaków
   EN: Does not inflict Paralyze on Identities that have equipped Defense Skills
   PL: Nie nakłada Paraliżu na Tożsamości z wyposażonymi Umiejętnościami obrony
163. [Status [FavorBuff5001AllyTwo] — nazwa] 사영 [급습]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001AllyTwo]`
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Status [FavorBuff5001AllyTwo] — opis] - 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당하는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- <color=#f8c200>H사 소속</color> 인격이 적에게 가하는 피해량 +15%, 받는 피해량 -30%\n- 전투 시작 시 <color=#f8c200>완전 공명</color>이 발동했으면, 가장 수량이 적은 속성의 <color=#f8c200>E.G.O 자원 1개를 4회 획득</color>
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Gluttony</color> Skills or Skills that inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- <color=#f8c200>H Corp.</color> Identities deal +15% damage and take -30% damage\n- Combat Start: Upon <color=#f8c200>A-Reson.</color>, gain <color=#f8c200>1 least-owned E.G.O resource 4 times</color>
   PL: - Ataki <color=#f8c200>Obżarstwa</color> lub z <color=#f8c200>Rozdarciem</color>: +25% obrażeń (E.G.O +100%)\n- Tożsamości <color=#f8c200>Korporacji H</color>: +15% zadawanych, -30% otrzymywanych\n- Na początku walki przy <color=#f8c200>Rezonansie Absolutnym</color> 4 razy zyskuj <color=#f8c200>1 Zasób E.G.O rzadkiego Grzechu</color>
165. [Status [FavorBuff5001AllyTwo] — podsumowanie] 탐식 스킬 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001AllyTwo].summary
   limit: do 120 znaków
   EN: Gluttony Skills deal more damage
   PL: Umiejętności Grzechu Obżarstwa zadają więcej obrażeń
166. [Status [FavorBuff5001EnemySecond] — nazwa] 사영 [급습]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001EnemySecond]`
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Status [FavorBuff5001EnemySecond] — opis] - 리카르도가 <color=#f8c200>흐트러짐 상태</color>일 때 공격자의 속도가 더 빠르면, (속도 차이 x 2)% 만큼 받는 <color=#f8c200>피해량이 증가</color> (최대 20%)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: - If the attacker's Speed is faster than Ricardo's when he is <color=#f8c200>Staggered</color>, Ricardo takes <color=#f8c200>+(Speed difference x 2)% damage</color> (max 20%)
   PL: - Gdy Ricardo jest w stanie <color=#f8c200>Oszołomienia</color>, a atakujący jest szybszy, jego <color=#f8c200>otrzymywane obrażenia rosną</color> o (różnica Szybkości x 2)% (maks. 20%)
168. [Status [FavorBuff5001EnemySecond] — podsumowanie] 속도 차이에 비례하여 피해량 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001EnemySecond].summary
   limit: do 120 znaków
   EN: Take more damage based on Speed difference
   PL: Otrzymywane obrażenia rosną proporcjonalnie do różnicy Szybkości
169. [Status [FavorBuff5001Hard] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001Hard].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001Hard]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Status [FavorBuff5001Hard] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001Hard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- Skills deal +20% damage
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Umiejętności zadają obrażenia +20%
171. [Status [FavorBuff5001Hard] — podsumowanie] Hard 난이도 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001Hard].summary
   limit: do 120 znaków
   EN: Hard Difficulty Tribulation
   PL: Utrapienie na poziomie trudności Hard
172. [Status [FavorBuff5001HardTwo] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5001HardTwo]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Status [FavorBuff5001HardTwo] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 스킬로 가하는 피해량 +20%\n- [2페이즈 전용]\n · 리카르도와 아우들의 정신력이 0 미만으로 감소하지 않음\n · 턴 시작시 이전 턴에 리카르도를 공격한 모든 적에게 [장부에 적힘] 2 부여
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].desc
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Status [FavorBuff5001HardTwo] — podsumowanie] Hard 난이도 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5001HardTwo].summary
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Status [RicardoBookRaid] — nazwa] 장부에 적힘
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoBookRaid].name
   kontekst: identyfikator statusu w tekstach: `[RicardoBookRaid]`
   limit: do 40 znaków
   EN: Written in the Book
   PL: Zapisano w Księdzie
176. [Status [RicardoBookRaid] — opis] 최댓값 : 30\n수치당 받는 피해량 +3%
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoBookRaid].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 30\nTake +3% damage for every Stack
   PL: Maks. ładunków: 30\nOtrzymywane obrażenia +3% za ładunek
177. [Status [RicardoTattooRaid] — nazwa] 원한 문신
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoTattooRaid].name
   kontekst: identyfikator statusu w tekstach: `[RicardoTattooRaid]`
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL: Tatuaż Zemsty
178. [Status [RicardoTattooRaid] — opis] 최댓값 : 300\n수치 10당 자신의 스킬 공격 레벨 +1
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoTattooRaid].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 300\nSkills gain Offense Level +1 for every 10 Stack
   PL: Maks. ładunków: 300\nZa każde 10 ładunków Umiejętności tej jednostki zyskują Poziom Ataku +1
179. [Status [RicardoJokeRaid] — nazwa] 형님의 시험
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoJokeRaid].name
   kontekst: identyfikator statusu w tekstach: `[RicardoJokeRaid]`
   limit: do 40 znaków
   EN: Test of the Big Brother
   PL: Test Starszego Brata
180. [Status [RicardoJokeRaid] — opis] 턴 종료시 1 감소\n이 효과가 있는 동안 스킬 피해, 진동 폭발로 인한 흐트러짐 손상을 2배로 받음
   źródło: Bufs-BossRaid.json :: dataList[id=RicardoJokeRaid].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 1 Stack\nWhile this effect is active, double damage taken from Skills, and double the amount of Stagger threshold raised from Tremor Burst
   PL: Na koniec tury traci 1 ładunek\nDopóki aktywny jest ten efekt, obrażenia od Umiejętności oraz obniżenie Progu Oszołomienia z Wyładowania Wstrząsu są podwajane
181. [Status [FavorBuff5012AllyOne] — nazwa] 사영 [곰 사냥]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012AllyOne]`
   limit: do 50 znaków
   EN: Shade of Reflection [Bearhunt]
   PL: Cień Projekcji [Niedźwiedzi Łów]
182. [Status [FavorBuff5012AllyOne] — opis] - 인격의 스킬 중 화상, 특수 화상을 부여하거나 분노 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적의 보호막에 진동 폭발로 흐트러짐 손상을 줄 때 대신 분노 피해를 줌\n· 위 효과로 분노 피해를 줄 때 보호막에 입히는 피해량 +50% (소수점 버림)\n- 죄악 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Identities' Attack Skills that are Wrath Skills or Skills that inflict Burn or 'Unique Burn' deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When raising Stagger threshold via Tremor Burst against enemy Shield, deal Wrath damage instead\n· When dealing Wrath damage via the above effect, deal +50% damage against Shield (rounded down)\n- Upon Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które nakładają Podpalenie lub „Specjalne Podpalenie” albo należą do Grzechu Gniewu, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Wyładowanie Wstrząsu zadaje obrażenia Oszołomienia Tarczy wroga, zamiast tego zadaje obrażenia od Gniewu\n· Zadając w ten sposób obrażenia od Gniewu, zadaje Tarczy obrażenia +50% (zaokrąglane w dół)\n- Przy Rezonansie zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
183. [Status [FavorBuff5012AllyOne] — podsumowanie] 화상 스킬 피해량 증가, 흐트러짐 손상으로 분노 피해
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyOne].summary
   limit: do 130 znaków
   EN: Burn Skills and 'Unique Burn' Skills deal more damage; raising Stagger threshold deals Wrath damage
   PL: Umiejętności Podpalenia i „Specjalnego Podpalenia” zadają więcej obrażeń; obniżanie Progu Oszołomienia zadaje obrażenia od Gniewu
184. [Status [FavorBuff5012EnemyOne] — nazwa] 사영 [곰 사냥]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012EnemyOne].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012EnemyOne]`
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Status [FavorBuff5012EnemyOne] — opis] - 화상 및 특수 화상 피해를 입을 때 보호막이 받는 피해량 +50% (소수점 버림)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012EnemyOne].desc
   limit: do 120 znaków
   EN: - Shield takes +50% damage from Burn and 'Unique Burn' (rounded down)
   PL: - Tarcza otrzymuje obrażenia +50% od Podpalenia i „Specjalnego Podpalenia” (zaokrąglane w dół)
186. [Status [FavorBuff5012AllyTwo] — nazwa] 사영 [범 사냥]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012AllyTwo]`
   limit: do 50 znaków
   EN: Shade of Reflection [Tigerhunt]
   PL: Cień Projekcji [Tygrysi Łów]
187. [Status [FavorBuff5012AllyTwo] — opis] - 인격의 스킬 중 호흡 위력 또는 호흡 횟수를 부여하거나 획득하거나 소모하는 효과가 있는 공격 스킬 또는 오만 속성 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 오만 속성 스킬 사용 시 해당 스킬 등급에 해당하는 호흡 위력을 얻고, 호흡 횟수 2 증가 (수감자당 턴당 2회, E.G.O 스킬은 3등급으로 취급함)\n- 검계 소속 인격이면, 아래 효과 적용\n· 맨 앞의 흐트러짐 구간 1개 제거\n· 최종 위력 +2\n· 적에게 가하는 피해량 +30%, 받는 피해량 -15%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Identities' Attack Skills that are Pride Skills, or Attack Skills that apply, gain, or consume Poise deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When using Pride Skills, gain (Skill's Rank) Poise Potency and +2 Poise Count (2 times per turn per Sinner; E.G.O Skills are considered Skill 3 for this purpose)\n- For Blade Lineage Identities, apply the following effects:\n· Remove this unit's first Stagger Threshold\n· Final Power +2\n· Deal +30% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które należą do Grzechu Pychy albo nakładają, zyskują lub zużywają Siłę Oddechu bądź Licznik Oddechu, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy użyciu Umiejętności Grzechu Pychy zyskuj Siłę Oddechu równą randze Umiejętności oraz Licznik Oddechu +2 (2 razy na turę na Grzesznika; Umiejętności E.G.O liczą się jako ranga 3)\n- Tożsamości z Rodu Ostrza otrzymują następujące efekty:\n· Usunięcie pierwszego Progu Oszołomienia tej jednostki\n· Moc Końcowa +2\n· Obrażenia zadawane wrogom +30%, otrzymywane -15%
188. [Status [FavorBuff5012AllyTwo] — podsumowanie] 호흡 스킬 또는 오만 스킬 피해량 증가, 오만 속성일 시 호흡 얻음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyTwo].summary
   limit: do 120 znaków
   EN: Poise Skills and Pride Skills deal more damage; gain Poise when using Pride Skills
   PL: Umiejętności Oddechu i Grzechu Pychy zadają więcej obrażeń; przy użyciu Umiejętności Grzechu Pychy zyskuje Oddech
189. [Status [FavorBuff5012HardOne] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardOne].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012HardOne]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Status [FavorBuff5012HardOne] — opis] - 최대 체력 +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 호흡 횟수가 5 이하면, 자신의 호흡 횟수 2 증가
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardOne].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" and "Sword of the Homeland [Sal] - Swordhoning", if this unit is at 5 or fewer Poise Count, gain +2 Poise Count
   PL: - Maks. HP +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” i „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli Licznik Oddechu tej jednostki wynosi 5 lub mniej, zyskuje Licznik Oddechu +2
191. [Status [FavorBuff5012HardTwo] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012HardTwo]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Status [FavorBuff5012HardTwo] — opis] - 최대 체력 +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 호흡 횟수가 5 이하면, 자신의 호흡 횟수 2 증가\n- [2페이즈 전용 효과] ‘본국검술[살] - 태세 변경’ 패시브의 효과로 본국검술[살]이 5로 초기화 될 때, 자신의 본국태세에 따라 본국검술[살] 2을 추가로 얻거나 잃음\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardTwo].desc
   limit: do 790 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max HP +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" and "Sword of the Homeland [Sal] - Swordhoning", if this unit is at 5 or fewer Poise Count, gain +2 Poise Count\n- [Phase 2 Exclusive Effect] When Swordplay of the Homeland [Sal] resets to 5 due to the effects of "Swordplay of the Homeland [Sal] - Shift Battleform" Passive, gain or lose 2 Swordplay of the Homeland [Sal] Stack based on Battleform of the Homeland on self\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Maks. HP +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” i „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli Licznik Oddechu tej jednostki wynosi 5 lub mniej, zyskuje Licznik Oddechu +2\n- [Efekt wyłącznie 2. fazy] Gdy Sztuka Miecza Ojczyzny [Sal] zostaje zresetowana do 5 przez pasywną Umiejętność „Sztuka Miecza Ojczyzny [Sal] – Zmiana Formy Walki”, w zależności od Formy Bojowej Ojczyzny tej jednostki dodatkowo zyskuje lub traci 2 Sztuki Miecza Ojczyzny [Sal]\n· Forma Bojowa Ojczyzny – Niedźwiedzi Łów: zyskuje\n· Forma Bojowa Ojczyzny – Tygrysi Łów: traci
193. [Status [FavorBuff5012AllyOneForUI] — nazwa] 사영 [곰 사냥]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyOneForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012AllyOneForUI]`
   (powtórzenie elementu 181 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Status [FavorBuff5012AllyOneForUI] — opis] - 인격의 스킬 중 <color=#f8c200>화상, 특수 화상을 부여하거나 분노 속성</color>에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 적의 보호막에 <color=#f8c200>진동 폭발</color>로 흐트러짐 손상을 줄 때 대신 <color=#f8c200>분노 피해</color>를 줌\n· 위 효과로 <color=#f8c200>분노 피해</color>를 주거나 대상이 <color=#f8c200>화상 및 특수 화상</color> 피해를 입을 때 <color=#f8c200>보호막</color>이 받는 피해량 +50% (소수점 버림)\n- 죄악 공명 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyOneForUI].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' Attack Skills that are <color=#f8c200>Wrath Skills or Skills that inflict Burn or 'Unique Burn'</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When raising Stagger threshold via <color=#f8c200>Tremor Burst</color> against enemy Shield, deal <color=#f8c200>Wrath damage</color> instead\n· When dealing <color=#f8c200>Wrath damage</color> via the above effect against target, or when target takes <color=#f8c200>Burn or 'Unique Burn'</color> damage, target's <color=#f8c200>Shield</color> takes +50% damage (rounded down)\n- Upon Reson., gain 1 random least-owned E.G.O resource and 1 E.G.O resource of the Affinity used for Reson. (2 times per turn)
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Podpalenie lub „Specjalne Podpalenie” albo należą do Grzechu Gniewu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Wyładowanie Wstrząsu zadaje <color=#f8c200>obrażenia Oszołomienia</color> Tarczy wroga, zamiast tego zadaje <color=#f8c200>obrażenia od Gniewu</color>\n· Zadając w ten sposób <color=#f8c200>obrażenia od Gniewu</color> lub gdy cel otrzymuje obrażenia od <color=#f8c200>Podpalenia i „Specjalnego Podpalenia”</color>, jego <color=#f8c200>Tarcza</color> otrzymuje obrażenia +50% (zaokrąglane w dół)\n- Przy Rezonansie zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)
195. [Status [FavorBuff5012AllyTwoForUI] — nazwa] 사영 [범 사냥]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyTwoForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012AllyTwoForUI]`
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Status [FavorBuff5012AllyTwoForUI] — opis] - 인격의 스킬 중 <color=#f8c200>호흡 위력 또는 호흡 횟수를 부여하거나 획득하거나 소모하는 효과가 있는 공격 스킬 또는 오만 속성</color>공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 오만 속성 스킬 사용 시 해당 스킬 등급에 해당하는 <color=#f8c200>호흡 위력을 얻고</color>, 호흡 횟수 2 증가 (수감자당 턴당 2회, E.G.O 스킬은 3등급으로 취급함)\n- <color=#f8c200>검계 소속 인격</color>이면, 아래 효과 적용\n· 맨 앞의 흐트러짐 구간 1개 제거\n· 최종 위력 +2\n· 적에게 가하는 피해량 +30%, 받는 피해량 -15%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012AllyTwoForUI].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - The Identities' <color=#f8c200>Attack Skills that are Pride Skills, or Attack Skills that apply, gain, or consume Poise</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When using Pride Skills, <color=#f8c200>gain (Skill's Rank) Poise Potency</color> and +2 Poise Count (2 times per turn per Sinner; E.G.O Skills are considered Skill 3 for this purpose)\n- For <color=#f8c200>Blade Lineage Identities</color>, apply the following effects:\n· Remove this unit's first Stagger Threshold\n· Final Power +2\n· Deal +30% damage to and take -15% damage from enemies
   PL: - Umiejętności ataku Tożsamości, które <color=#f8c200>należą do Grzechu Pychy albo nakładają, zyskują lub zużywają Siłę Oddechu bądź Licznik Oddechu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Przy użyciu Umiejętności Grzechu Pychy <color=#f8c200>zyskuje Siłę Oddechu równą randze Umiejętności</color> oraz Licznik Oddechu +2 (2 razy na turę na Grzesznika; Umiejętności E.G.O liczą się jako ranga 3)\n- Tożsamości <color=#f8c200>z Rodu Ostrza</color> otrzymują następujące efekty:\n· Usunięcie pierwszego Progu Oszołomienia tej jednostki\n· Moc Końcowa +2\n· Obrażenia zadawane wrogom +30%, otrzymywane -15%
197. [Status [FavorBuff5012HardTwoForUI] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardTwoForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuff5012HardTwoForUI]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Status [FavorBuff5012HardTwoForUI] — opis] - <color=#ff0000>최대 체력</color> +25%\n- 정신력이 0 미만으로 감소하지 않음\n- [임경업 전용 효과] ‘본국검[살] - 가다듬기’, ‘본국검[살] - 벼리기’ 사용 시 자신의 <color=#ff0000>호흡 횟수가 5 이하</color>면, 자신의 호흡 횟수 2 증가\n- [2페이즈 전용 효과] ‘본국검술[살] - 태세 변경’ 패시브의 효과로 본국검술[살]이 <color=#ff0000>5로 초기화 될 때</color>, 자신의 본국태세에 따라 본국검술[살] <color=#ff0000>2을 추가로 얻거나 잃음</color>\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuff5012HardTwoForUI].desc
   limit: do 810 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +25%\n- SP does not drop below 0\n- [Im Gyeong-eop Exclusive Effect] When using "Sword of the Homeland [Sal] - Reassume Stance" and "Sword of the Homeland [Sal] - Swordhoning", if this unit is at <color=#ff0000>5 or fewer Poise Count</color>, gain +2 Poise Count\n- [Phase 2 Exclusive Effect] When Swordplay of the Homeland [Sal] <color=#ff0000>resets to 5</color> due to the effects of "Swordplay of the Homeland [Sal] - Shift Battleform" Passive, <color=#ff0000>gain or lose an additional 2</color> Swordplay of the Homeland [Sal] Stack based on Battleform of the Homeland on self\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - <color=#ff0000>Maks. HP</color> +25%\n- Poczytalność nie spada poniżej 0\n- [Efekt wyłącznie dla Im Gyeong-eopa] Przy użyciu „Miecza Ojczyzny [Sal] – Powrót do Postawy” lub „Miecza Ojczyzny [Sal] – Doszlifowanie Ostrza”, jeżeli <color=#ff0000>Licznik Oddechu tej jednostki wynosi 5 lub mniej</color>, zyskuje Licznik Oddechu +2\n- [Efekt wyłącznie 2. fazy] Gdy Sztuka Miecza Ojczyzny [Sal] <color=#ff0000>zostaje zresetowana do 5</color> przez pasywną Umiejętność „Sztuka Miecza Ojczyzny [Sal] – Zmiana Formy Walki”, w zależności od Formy Bojowej Ojczyzny tej jednostki <color=#ff0000>dodatkowo zyskuje lub traci 2</color> Sztuki Miecza Ojczyzny [Sal]\n· Forma Bojowa Ojczyzny – Niedźwiedzi Łów: zyskuje\n· Forma Bojowa Ojczyzny – Tygrysi Łów: traci
199. [Status [FavorBuffLeiheng] — nazwa] 사영 [삽시호]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeiheng]`
   limit: do 50 znaków
   EN: Shade of Reflection [Chachihu]
   PL: Cień Projekcji [Chachihu]
200. [Status [FavorBuffLeiheng] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +8 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 인격이 적과 합 진행 시, 메인 타겟의 <color=#f8c200>속박</color> 2당 합 위력 +1 (최대 2)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - If an Identity is on the field, <color=#f8c200>remove 1 Stagger Threshold</color> and gain +8 Base Offense Level and +8 Base Defense Level (effect does not stack)\n- On <color=#f8c200>Reson.,</color> gain 1 E.G.O resource for the respective Affinity and 1 random least-owned E.G.O resource (2 times per turn)\n- E.G.O Skills deal +50% damage\n- Identity Skills that either are <color=#f8c200>Gluttony</color> Skills or inflict <color=#f8c200>Rupture</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)\n- When an Identity Clashes with an enemy, the Identity gains +1 Clash Power for every 2 <color=#f8c200>Bind</color> on the main target (max 2)
   PL: - Każda Tożsamość na polu bitwy <color=#f8c200>usuwa 1 Próg Oszołomienia</color> i zyskuje +8 do Podstawowego Poziomu Ataku i +8 do Podstawowego Poziomu Obrony (nie kumuluje się)\n- Przy <color=#f8c200>Rezonansie</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 1 losowy najmniej posiadany Zasób E.G.O (2 razy na turę)\n- Umiejętności E.G.O zadają obrażenia +50%\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Rozdarcie</color> albo należą do Grzechu <color=#f8c200>Obżarstwa</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)\n- Gdy Tożsamość prowadzi Starcie z wrogiem, zyskuje Moc Starcia +1 za każde 2 <color=#f8c200>Spętania</color> na głównym celu (maks. 2)
201. [Status [FavorBuffLeihengTwo] — nazwa] 사영 [천퇴성]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeihengTwo]`
   limit: do 50 znaków
   EN: Shade of Reflection [Tiantui Star]
   PL: Cień Projekcji [Gwiazda Tiantui]
202. [Status [FavorBuffLeihengTwo] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +15 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 2개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>화상, 특수 화상</color>을 부여하거나 <color=#f8c200>분노</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengTwo].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: - If an Identity is on the field, <color=#f8c200>remove 1 Stagger Threshold</color> and gain +15 Base Offense Level and +15 Base Defense Level (effect does not stack)\n- On <color=#f8c200>Reson.,</color> gain 1 E.G.O resource for the respective Affinity and 2 random least-owned E.G.O resources (2 times per turn)\n- E.G.O Skills deal +50% damage\n- Identity Skills that either are <color=#f8c200>Wrath</color> Skills or inflict <color=#f8c200>Burn or Unique Burn</color> deal +25% damage (for E.G.O Skills, deal +100% damage instead)
   PL: - Każda Tożsamość na polu bitwy <color=#f8c200>usuwa 1 Próg Oszołomienia</color> i zyskuje +15 do Podstawowego Poziomu Ataku i +15 do Podstawowego Poziomu Obrony (nie kumuluje się)\n- Przy <color=#f8c200>Rezonansie</color> zyskuj 1 Zasób E.G.O Grzechu, który go wywołał, oraz 2 losowe najmniej posiadane Zasoby E.G.O (2 razy na turę)\n- Umiejętności E.G.O zadają obrażenia +50%\n- Umiejętności ataku Tożsamości, które <color=#f8c200>nakładają Podpalenie lub „Specjalne Podpalenie”</color> albo należą do Grzechu <color=#f8c200>Gniewu</color>, zadają obrażenia +25% (w przypadku Umiejętności E.G.O zamiast tego obrażenia +100%)
203. [Status [FavorBuffLeihengHard] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHard].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeihengHard]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Status [FavorBuffLeihengHard] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHard].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +80%\n- SP does not drop below 0\n- Deal +50% damage against targets that have <color=#ff0000>Prey</color> (does not trigger if the target has Defense Skills equipped). Take -50% damage from targets that have <color=#ff0000>Prey</color>\n- <color=#ff0000>If this unit has 3+ Tigermark Rounds</color> when using the Blasting Shatterslash [爆碎斬] Skill, deal +100% damage
   PL: - <color=#ff0000>Maks. HP</color> +80%\n- Poczytalność nie spada poniżej 0\n- Celom posiadającym <color=#ff0000>Zdobycz</color> zadaje obrażenia +50% (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a otrzymuje od nich -50%\n- Jeżeli przy użyciu Umiejętności „Roztrzaskujące Cięcie [爆碎斬]” ma co najmniej 3 <color=#ff0000>Pociski Tygrysiego Znaku</color>, zadaje obrażenia +100%
205. [Status [FavorBuffLeihengHard] — podsumowanie] Hard 난이도 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHard].summary
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Status [FavorBuffLeihengHardTwo] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeihengHardTwo]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Status [FavorBuffLeihengHardTwo] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%\n- [2페이즈 전용 효과]\n· 스킬 사용 시 <color=#ff0000>메인 타겟이 사냥감</color>을 보유했으면, <color=#ff0000>기본 위력이 5 증가하고 피해량 +200%</color> (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 해당 스킬의 모든 코인이 <color=#ff0000>파괴 불가 코인</color>으로 변경됨\n· <color=#ff0000>사냥감</color>을 보유한 대상에게 합 패배 시, <color=#ff0000>절참 [切斬]</color> 1 얻음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Max HP</color> +80%\n- SP does not drop below 0\n- Deal +50% damage against targets that have <color=#ff0000>Prey</color> (does not trigger if the target has Defense Skills equipped). Take -50% damage from targets that have <color=#ff0000>Prey</color>\n- <color=#ff0000>If this unit has 3+ Tigermark Rounds</color> when using the Blasting Shatterslash [爆碎斬] Skill, deal +100% damage\n- [Phase 2 Exclusive Effect]\n· On Skill Use, <color=#ff0000>if the main target has Prey,</color> <color=#ff0000>gain Base Power +5, deal +200% damage</color> (does not trigger if the target has Defense Skills equipped), and convert all Coins on the Skill into <color=#ff0000>Unbreakable Coins</color>\n· On Clash Lose against targets that have <color=#ff0000>Prey</color>, gain 1 <color=#ff0000>Severing Slash [切斬]</color>
   PL: - <color=#ff0000>Maks. HP</color> +80%\n- Poczytalność nie spada poniżej 0\n- Celom posiadającym <color=#ff0000>Zdobycz</color> zadaje obrażenia +50% (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a otrzymuje od nich -50%\n- Jeżeli przy użyciu Umiejętności „Roztrzaskujące Cięcie [爆碎斬]” ma co najmniej 3 <color=#ff0000>Pociski Tygrysiego Znaku</color>, zadaje obrażenia +100%\n- [Efekt wyłącznie 2. fazy]\n· Przy użyciu Umiejętności, <color=#ff0000>jeżeli główny cel posiada Zdobycz</color>, <color=#ff0000>zyskuje Moc Bazową +5 i zadaje obrażenia +200%</color> (nie działa, jeśli cel ma wyposażone Umiejętności obrony), a wszystkie Monety tej Umiejętności stają się <color=#ff0000>Niezniszczalnymi Monetami</color>\n· Po przegranym Starciu z celem posiadającym <color=#ff0000>Zdobycz</color> zyskuje 1 <color=#ff0000>Przecinające Cięcie [切斬]</color>
208. [Status [FavorBuffLeihengHardTwo] — podsumowanie] Hard 난이도 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHardTwo].summary
   (powtórzenie elementu 171 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Status [FavorBuffLeiheng1stPhaseForUI] — nazwa] 사영 [삽시호]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng1stPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeiheng1stPhaseForUI]`
   (powtórzenie elementu 199 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Status [FavorBuffLeiheng1stPhaseForUI] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +8 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 1개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>파열</color>을 부여하거나 <color=#f8c200>탐식</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)\n- 인격이 적과 합 진행 시, 메인 타겟의 <color=#f8c200>속박</color> 2당 합 위력 +1 (최대 2)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng1stPhaseForUI].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Status [FavorBuffLeiheng2ndPhaseForUI] — nazwa] 사영 [천퇴성]
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng2ndPhaseForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeiheng2ndPhaseForUI]`
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Status [FavorBuffLeiheng2ndPhaseForUI] — opis] - 전장에 참여하는 모든 인격의 <color=#f8c200>흐트러짐 선 하나 제거</color>. 기본 공격 레벨, 기본 방어 레벨 +15 (중첩 불가)\n- <color=#f8c200>죄악 공명</color> 시, 해당 속성의 E.G.O 자원 1개, 가장 적은 무작위 E.G.O 자원 2개 획득 (턴당 2회)\n- E.G.O 스킬의 피해량 +50%\n- 인격의 스킬 중 <color=#f8c200>화상, 특수 화상</color>을 부여하거나 <color=#f8c200>분노</color> 속성에 해당되는 공격 스킬의 피해량 +25% (E.G.O 스킬일 경우, 대신 피해량 +100%)
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeiheng2ndPhaseForUI].desc
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Status [FavorBuffLeihengHardForUI] — nazwa] 고난
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHardForUI].name
   kontekst: identyfikator statusu w tekstach: `[FavorBuffLeihengHardForUI]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Status [FavorBuffLeihengHardForUI] — opis] - <color=#ff0000>최대 체력</color> +80%\n- 정신력이 0 미만으로 감소하지 않음\n- <color=#ff0000>사냥감</color>을 보유한 대상에게 가하는 피해량 +50% (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 받는 피해량 -50%\n- 폭쇄참 [爆碎斬] 사용 시 <color=#ff0000>호표탄이 3 이상</color>이면, 피해량 +100%\n- [2페이즈 전용 효과]\n· 스킬 사용 시 <color=#ff0000>메인 타겟이 사냥감</color>을 보유했으면, <color=#ff0000>기본 위력이 5 증가하고 피해량 +200%</color> (대상이 수비 스킬 장착 시, 이 효과는 발동하지 않음), 해당 스킬의 모든 코인이 <color=#ff0000>파괴 불가 코인</color>으로 변경됨\n· <color=#ff0000>사냥감</color>을 보유한 대상에게 합 패배 시, <color=#ff0000>절참 [切斬]</color> 1 얻음
   źródło: Bufs-BossRaid.json :: dataList[id=FavorBuffLeihengHardForUI].desc
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Status [HugeIrritationReflectrial] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: Bufs-BossRaid.json :: dataList[id=HugeIrritationReflectrial].name
   kontekst: identyfikator statusu w tekstach: `[HugeIrritationReflectrial]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
216. [Status [HugeIrritationReflectrial] — opis] - 턴 시작 시, 잃은 체력 15%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 5)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +3, 진동 횟수 증가량 +1\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 40%)\n- '이연참-폭', '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: Bufs-BossRaid.json :: dataList[id=HugeIrritationReflectrial].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Damage Up and 1 Power Up for every 15% missing HP on self (max 5 each)\n- Inflict +3 more Tremor Potency and +1 more Tremor Count with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 40%)\n- Convert the final Coins of "Double Slash - Blast" and "Triple Slash - Blast" to Unbreakable Coins
   PL: - Na początek tury: zyskuje 1 Wzrostu Obrażeń i 1 Wzrostu Mocy za każde 15% brakującego HP (każde maks. 5)\n- Wartość Siły Wstrząsu nadawanej Umiejętnościami wrogom +3, wartość nadawanego Licznika Wstrząsu +1\n- Jeśli Szybkość tej jednostki przewyższa Szybkość celu o 3 lub więcej, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 40%)\n- Ostatnie monety umiejętności 'Podwójne Cięcie - Wybuch' i 'Potrójne Cięcie - Seria' zmieniają się w Niezniszczalne Monety
217. [Status [Prey_leiheng] — nazwa] 사냥감
   źródło: Bufs-BossRaid.json :: dataList[id=Prey_leiheng].name
   kontekst: identyfikator statusu w tekstach: `[Prey_leiheng]`
   limit: do 40 znaków
   EN: Prey
   PL: Zdobycz
218. [Status [Prey_leiheng] — opis] - 적과 합 진행 시, 합 위력 - 5\n- 전투 시작 시,\n· 공격 스킬을 장착하였다면 공격 스킬로 뇌횡에게 가하는 피해량이 50%만큼 감소\n· 수비 스킬을 장착하였다면 뇌횡에게 받는 피해량이 75%만큼 감소\n- 이 효과를 보유한 상태에서 뇌횡과 합하여 승리 시, 제일 적게 보유한 E.G.O 자원 3개 획득\n- 턴 종료 시 사라지고, 자신의 정신력 10 회복
   źródło: Bufs-BossRaid.json :: dataList[id=Prey_leiheng].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash with an enemy, Clash Power -5\n- Combat Start:\n· If this unit equipped an Attack Skill, deal -50% damage against Lei Heng using Attack Skills\n· If this unit equipped a Defense Skill, take -75% damage from Lei Heng\n- If this unit wins a Clash against Lei Heng while under this effect, gain 3 of the least-owned E.G.O Resources\n- Expires at Turn End; this unit heals 10 SP
   PL: - W Starciu z wrogiem Moc Starcia -5\n- Na początku walki,\n· Jeżeli wyposażono Umiejętność ataku, zadaje o 50% mniej obrażeń Lei Hengowi Umiejętnościami ataku\n· Jeżeli wyposażono Umiejętność obrony, otrzymuje o 75% mniej obrażeń od Lei Henga\n- Jeżeli wygrywa Starcie z Lei Hengiem, mając ten efekt, zyskuje 3 najmniej posiadanych Zasobów E.G.O\n- Znika na koniec tury, a jednostka odzyskuje 10 Poczytalności

## Statusy i efekty bojowe — Bufs-Refraction1BokGak
- plik gry: `Bufs-Refraction1BokGak.json`

219. [Status [AggressiveBokgak] — nazwa] 본능
   źródło: Bufs-Refraction1BokGak.json :: dataList[id=AggressiveBokgak].name
   kontekst: identyfikator statusu w tekstach: `[AggressiveBokgak]`
   limit: do 40 znaków
   EN: Instincts
   PL: Instynkt
220. [Status [AggressiveBokgak] — opis] 최댓값: 5\n턴 종료 시 수치가 4 이상이면 상태가 공격적으로 변경됨.
   źródło: Bufs-Refraction1BokGak.json :: dataList[id=AggressiveBokgak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\nTurn End: At 4+ Stack, change to an “aggressive” state.
   PL: Maks. ładunków: 5\nNa koniec tury przy 4 lub więcej ładunkach stan zmienia się na „agresywny”.
221. [Status [DeadEGOResource] — nazwa] 남겨진 의지
   źródło: Bufs-Refraction1BokGak.json :: dataList[id=DeadEGOResource].name
   kontekst: identyfikator statusu w tekstach: `[DeadEGOResource]`
   limit: do 40 znaków
   EN: Lingering Determination
   PL: Zostawiona Determinacja
222. [Status [DeadEGOResource] — opis] 사망 시 인격이 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼  얻음
   źródło: Bufs-Refraction1BokGak.json :: dataList[id=DeadEGOResource].desc
   limit: do 140 znaków
   EN: When defeated, gain E.G.O Resources based on the Affinity & Rank of each Attack Skill this Identity has
   PL: Przy pokonaniu zyskujesz Zasoby E.G.O odpowiadające Grzechom i rangom każdej Umiejętności ataku tej Tożsamości

## Statusy i efekty bojowe — Bufs-Refraction2BokGak
- plik gry: `Bufs-Refraction2BokGak.json`

223. [Status [PassedPortal_GreenBokGak] — nazwa] 독이 들끓는 차원
   źródło: Bufs-Refraction2BokGak.json :: dataList[id=PassedPortal_GreenBokGak].name
   kontekst: identyfikator statusu w tekstach: `[PassedPortal_GreenBokGak]`
   limit: do 40 znaków
   EN: Poisonous Dimension
   PL: Wymiar Wrzącej Trucizny
224. [Status [PassedPortal_GreenBokGak] — opis] 차원을 통과해 수치당 본체 최대 체력 20% 증가
   źródło: Bufs-Refraction2BokGak.json :: dataList[id=PassedPortal_GreenBokGak].desc
   limit: do 120 znaków
   EN: Pass through the Dimensional Rift to gain +20% Core max HP
   PL: Za przejście przez Wymiar Maks. HP Korpusu rośnie o 20% za każdą wartość

## Statusy i efekty bojowe — Bufs-a1c10p1
- plik gry: `Bufs-a1c10p1.json`

225. [Status [NoirNoComply] — nazwa] 안내 불이행
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirNoComply].name
   kontekst: identyfikator statusu w tekstach: `[NoirNoComply]`
   limit: do 40 znaków
   EN: Instruction Incompliance
   PL: Nieprzestrzeganie Instrukcji
226. [Status [NoirNoComply] — opis] - 최댓값 : 3\n- 수치당 받는 피해량 +5%
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirNoComply].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Take +5% damage for every Stack
   PL: - Maks. ładunków: 3\n- Otrzymuje obrażenia +5% za każdy ładunek
227. [Status [NoirNoComply] — tekst klimatyczny] 브랜드 규정을 지켜주시지 않았기에 브랜드 방향성 보존을 위한 제재에 들어갈 수 있습니다.
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirNoComply].flavor
   limit: do 180 znaków
   EN: Failure to comply with the brand's doctrine instructions may result in corrective measures to preserve the brand's directional integrity.
   PL: Niestosowanie się do wytycznych doktryny marki może skutkować podjęciem działań naprawczych w celu zachowania spójności kierunku marki.
228. [Status [NoirBindArmor] — nazwa] 르누아르 우스티드 원단
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirBindArmor].name
   kontekst: identyfikator statusu w tekstach: `[NoirBindArmor]`
   limit: do 40 znaków
   EN: Le Noir: Worsted
   PL: Le Noir: Tkanina Czesankowa
229. [Status [NoirBindArmor] — opis] - 최댓값 : 15\n- 수치 5당 속도 최댓값 -1, 공격 레벨 +1, 방어 레벨 +1\n- 턴 종료시 수치 1 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirBindArmor].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- For every 5 Stacks, Max Speed -1, Offense Level +1, Defense Level +1\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 15\n- Za każde 5 ładunków Maks. Szybkość -1, Poziom Ataku +1, Poziom Obrony +1\n- Na koniec tury traci 1 ładunek
230. [Status [NoirBindArmor] — tekst klimatyczny] 르누아르 원단은 갑옷과 같이 탄탄하고 고정된 실루엣으로 고객의 체형을 보정해준다.
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirBindArmor].flavor
   limit: do 130 znaków
   EN: Le Noir's Worsted holds the body like armor, accentuating it beneath a firm, fixed silhouette.
   PL: Tkanina Le Noir, jak zbroja, podtrzymuje sylwetkę klienta twardym i stałym obrysem, korygując jego kształt.
231. [Status [ChargeNoir] — nazwa] 보존
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeNoir].name
   kontekst: identyfikator statusu w tekstach: `[ChargeNoir]`
   limit: do 40 znaków
   EN: Preservation
   PL: Zachowanie
232. [Status [ChargeNoir] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeNoir].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count\n\n<color=#1aece7>Cumulative Count consumed: {2}</color>
   PL: - Szczególne Ładowanie\n- Maks. Licznika: 20\n- Efekty zwiększające lub zmniejszające Moc i Licznik Ładowania działają na nią tak samo\n- Na koniec tury Licznik maleje o 1\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
233. [Status [ChargeNoir] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeNoir].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła jest kondensowana, zbierana i umacniana. Czasem potrzeba więcej siły, by powstrzymać zmianę, niż ją wywołać.
234. [Status [ChargeRouge] — nazwa] 맥동
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeRouge].name
   kontekst: identyfikator statusu w tekstach: `[ChargeRouge]`
   limit: do 40 znaków
   EN: Pulsation
   PL: Pulsacja
235. [Status [ChargeRouge] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeRouge].desc
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Status [ChargeRouge] — tekst klimatyczny] 살의 수축과 이완. 피의 흐름. 그 정도에 따라 터져나오는 힘.
   źródło: Bufs-a1c10p1.json :: dataList[id=ChargeRouge].flavor
   limit: do 130 znaków
   EN: Contraction and relaxation of flesh. The flow of blood. The explosive strength driven by them all.
   PL: Kurczenie i rozkurcz ciała. Przepływ krwi. Wybuchowa siła, którą wszystkie one napędzają.
237. [Status [RisingMadnessRouge] — nazwa] 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessRouge]`
   limit: do 40 znaków
   EN: Sunshine
   PL: Promienie Słońca
238. [Status [RisingMadnessRouge] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 자신의 맥동만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Pulsation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Pulsowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
239. [Status [RisingMadnessRouge] — tekst klimatyczny] …될 수 있어.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge].flavor
   limit: do 120 znaków
   EN: You can be...
   PL: …Możesz stać się...
240. [Status [RisingMadnessRouge2nd] — nazwa] 따가운 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessRouge2nd]`
   limit: do 40 znaków
   EN: Stinging Sunshine
   PL: Parzące Promienie Słońca
241. [Status [RisingMadnessRouge2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 자신의 맥동만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Pulsation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Pulsowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
242. [Status [RisingMadnessRouge2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessRouge2nd].flavor
   limit: do 240 znaków
   EN: The Sunlight whispers into all that it touches, beating down all the same even as its heat grows from a prickle on the skin to unbearable, burning pain and the subject is cooked alive.
   PL: Światło słoneczne szepta do wszystkiego, czego dotyka, i opada bezlitośnie — choć jego żar narasta od mrowienia na skórze po nieznośny, parzący ból, aż dotknięty gaśnie żywcem.
243. [Status [RisingMadnessNoir] — nazwa] 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessNoir]`
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Status [RisingMadnessNoir] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 자신의 보존 위력만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Preservation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Zachowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
245. [Status [RisingMadnessNoir] — tekst klimatyczny] …될 수 있어.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir].flavor
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Status [RisingMadnessNoir2nd] — nazwa] 따가운 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessNoir2nd]`
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Status [RisingMadnessNoir2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 자신의 보존 위력만큼 마지막 코인부터 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins, starting from the final Coin (number of Coins converted on each Skill is equal to Preservation Potency on self)\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Umiejętności zamieniają swoje Monety w Niezniszczalne, począwszy od ostatniej, w liczbie równej Siła Zachowania tej jednostki\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
248. [Status [RisingMadnessNoir2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessNoir2nd].flavor
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Status [RougeThreeNormal] — nazwa] 부티크 신상옷
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeNormal].name
   kontekst: identyfikator statusu w tekstach: `[RougeThreeNormal]`
   limit: do 40 znaków
   EN: Boutique: New Releases
   PL: Butik: Nowa Kolekcja
250. [Status [RougeThreeNormal] — opis] - 최댓값 : 20\n\n스킬 사용시 자신의 최대 체력의 1%를 소모하여, 자신의 스킬 피해량 +(소모한 체력)%
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeNormal].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n\nOn Skill Use, consume 1% of max HP on self to deal +(HP consumed) Skill damage
   PL: - Maks. ładunków: 20\n\nPrzy użyciu Umiejętności zużywa 1% swojego Maks. HP, a jego Umiejętności zadają obrażenia +(zużyte HP)
251. [Status [RougeThreeNormal] — tekst klimatyczny] 따듯한 목소리를 따라가면… 새로운 시즌으로…!
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeNormal].flavor
   limit: do 120 znaków
   EN: Follow the warm voice... into a new season...!
   PL: Idź za ciepłym głosem... w nowy sezon...!
252. [Status [RougeThreeCocoon] — nazwa] 탈의실
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoon].name
   kontekst: identyfikator statusu w tekstach: `[RougeThreeCocoon]`
   limit: do 40 znaków
   EN: Changing Room
   PL: Przebieralnia
253. [Status [RougeThreeCocoon] — opis] - 최댓값 : 3\n- 체력 피해를 받지 않음\n- 피격 시, 아래 효과 적용 (턴당 최대 20회)\n\n· 맥동 횟수 1 얻음\n· 피해량 증가 1 얻음\n· 다음 턴에 방어 레벨 감소 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoon].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Does not take HP damage\n- When hit, apply the following effects: (20 times per turn)\n· Gain +1 Pulsation Count\n· Gain 1 Damage Up\n· Gain 1 Defense Level Down next turn
   PL: - Maks. ładunków: 3\n- Nie otrzymuje obrażeń HP\n- Przy trafieniu stosowane są następujące efekty (maks. 20 razy na turę)\n\n· Zyskuje 1 Licznika Pulsowania\n· Zyskuje 1 Wzrost Obrażeń\n· W następnej turze zyskuje 1 Spadek Poziomu Obrony
254. [Status [RougeThreeCocoon] — tekst klimatyczny] 주의: 망가진 옷 다시 입는 중 입니다. 탈의실 매너는 다들 아시겠죠?
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoon].flavor
   limit: do 120 znaków
   EN: Warning: Fixing a misshapen dress. We all know the changing room manners, don't we?
   PL: Uwaga: obecnie poprawiamy zniekształconą suknię. O zasadach dobrego tonu w przymierzalni wie przecież każdy, prawda?
255. [Status [RougeThreeCocoonHit] — nazwa] 핍박
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].name
   kontekst: identyfikator statusu w tekstach: `[RougeThreeCocoonHit]`
   limit: do 40 znaków
   EN: Persecution
   PL: Prześladowanie
256. [Status [RougeThreeCocoonHit] — opis] - 최댓값 : 20
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].desc
   limit: do 120 znaków
   EN: - Max Stack: 20
   PL: - Maks. ładunków: 20
257. [Status [RougeThreeCocoonHit] — tekst klimatyczny] 탈의실 사용 중에 건들다니… 이건 믿음에 대한 핍박…
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonHit].flavor
   limit: do 150 znaków
   EN: Disturbing someone while they're in a changing room...? This is persecution, persecution against my faith...!
   PL: Przeszkadzać komuś w trakcie korzystania z przymierzalni...? To prześladowanie... prześladowanie mej wiary...!
258. [Status [SapsareeShield] — nazwa] 먹어줘...
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeShield].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeShield]`
   limit: do 40 znaków
   EN: Please, eat me...
   PL: Zjedz mnie, proszę...
259. [Status [SapsareeShield] — opis] - 수셰프가 적에게 일방 공격을 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고 원호 방어 전용 스킬 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 사용\n- 이 효과는 원호 방어로 간주되며, 원호 방어 수치를 계산할 때 합산됨\n- 턴 종료 시 소멸
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeShield].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Sous Chef is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then use Assist Defense-exclusive Skill\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- This effect counts as Assist Defense, and is counted toward calculating Assist Defense Stacks\n- Expires at Turn End
   PL: - Gdy Sous-chef ma otrzymać Atak Jednostronny od wroga, zużywa 1 ładunek, aby przekierować celowanie wroga na siebie, i używa Umiejętności zarezerwowanej dla Obrony Wsparcia\n- Jeżeli kilku sojuszników posiada Obronę Wsparcia, pierwszeństwo ma ten z najwyższą liczbą ładunków\n- Ten efekt liczy się jako Obrona Wsparcia i jest uwzględniany przy obliczaniu ładunków Obrony Wsparcia\n- Znika na koniec tury
260. [Status [SapsareeYammi] — nazwa] 맛있는거 먹고 힘난다는거예요
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeYammi].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeYammi]`
   limit: do 50 znaków
   EN: Eat yummies and perk up, you hear?
   PL: Smakołyki zjedzone, siła nabyta, jasne?
261. [Status [SapsareeYammi] — opis] - 최댓값 : 5\n- 수치 1당, 공격 레벨 1 증가\n- 턴 시작 시 보유한 '배고픈 거예요' 1당, 수치 1 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeYammi].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +1 for every Stack\n- Turn Start: Lose 1 Stack for every "Got an appetite, you hear?" on self
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 za każdy ładunek\n- Na początku tury traci 1 ładunek za każdy „Głoduję, jasne?” na sobie
262. [Status [SapsareeYammi] — tekst klimatyczny] 맛에 의한 만족이 아닌 포만감에 의한 만족일 뿐.
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeYammi].flavor
   limit: do 120 znaków
   EN: Not satiation from flavor, but from unrefined fullness.
   PL: Nie zadowolenie ze smaku — zadowolenie z prowizjonalnego nasycenia.
263. [Status [SapsareeCooking] — nazwa] 토막난 요리재료
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeCooking].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeCooking]`
   limit: do 40 znaków
   EN: Chopped Ingredients
   PL: Pokrojone Składniki
264. [Status [SapsareeCooking] — opis] - 최댓값 : 5\n- 턴 종료 시 소멸
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeCooking].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Expires at Turn End
   PL: - Maks. ładunków: 5\n- Znika na koniec tury
265. [Status [SapsareeCooking] — tekst klimatyczny] 입에 넣을 수만 있도록 잘랐다. 칼질에는 어떠한 철학도, 손길도 없다.
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeCooking].flavor
   limit: do 190 znaków
   EN: Hacked up haphazardly with no other purpose than to fit it down the gullet. Not even an ounce of culinary philosophy or care went into each chop.
   PL: Posiekane byle jak, po to jedynie, by dało się wcisnąć w przełyk. Ani kropli filozofii kulinarnej, ani cienia staranności w każdym cięciu.
266. [Status [SapsareeHungry] — nazwa] 배고픈 거예요
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeHungry].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeHungry]`
   limit: do 40 znaków
   EN: Got an appetite, you hear?
   PL: Głoduję, jasne?
267. [Status [SapsareeHungry] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 가하는 피해량 +50%\n- 수셰프가 스킬 '앗! 제 식사시간인거예요' 사용 시 소멸
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeHungry].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack\n- At 3 Stacks, deal +50% damage\n- Expires when Sous Chef uses the "Aah! I'm on lunch break, you hear?" Skill
   PL: - Maks. ładunków: 3\n- Poziom Ataku +1 za każdy ładunek\n- Przy 3 ładunkach zadaje obrażenia +50%\n- Znika, gdy Sous-chef użyje Umiejętności „Ach! To czas mojego posiłku, jasne?”
268. [Status [SapsareeHungry] — tekst klimatyczny] 아무거나 배에 쑤셔넣기만 하면 만족되는 허기. 그게 여기 있는 것들의 본성.
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeHungry].flavor
   limit: do 130 znaków
   EN: A hunger content with anything shoved into the gut. Such is the nature of those who subsist here.
   PL: Głód zadowolony ze wszystkiego, co wciśnięto do żołądka. Taka jest natura tych, którzy tu wegetują.
269. [Status [SapsareeSpices] — nazwa] 매콤매콤소스
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeSpices].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeSpices]`
   limit: do 50 znaków
   EN: Fiery, Tongue-scorching Sauce
   PL: Pikantno-Pikantny Sos
270. [Status [SapsareeSpices] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeSpices].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level -1 for every Stack
   PL: - Maks. ładunków: 3\n- Poziom Ataku -1 za każdy ładunek
271. [Status [SapsareeSpices] — tekst klimatyczny] 재료의 질을 감추기 위한 안일한 방법.
   źródło: Bufs-a1c10p1.json :: dataList[id=SapsareeSpices].flavor
   limit: do 120 znaków
   EN: A lazy cook's solution for disguising substandard ingredient quality.
   PL: Leniwy sposób na zamaskowanie kiepskiej jakości składników.
272. [Status [Sapsaree_LowMorale] — nazwa] 요리갈망
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Sapsaree_LowMorale]`
   limit: do 40 znaków
   EN: Culinary Yearning
   PL: Kulinarna Tęsknota
273. [Status [Sapsaree_LowMorale] — opis] - 사기 저하\n- 자신의 '배고픈 거예요' 수치 1당, 공격 레벨 1 증가, 받는 피해량 +3%
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +1 and take +3% damage for every "Got an appetite, you hear?" Stack on self
   PL: - Niskie Morale\n- Poziom Ataku +1 i otrzymuje obrażenia +3% za każdy ładunek „Głoduję, jasne?” na sobie
274. [Status [Sapsaree_LowMorale] — tekst klimatyczny] 넌 요리를 하고 싶은 게 아니다. 요리를 하는 느낌과 식사를 하는 흉내를 내고 싶은 것이지.
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_LowMorale].flavor
   limit: do 170 znaków
   EN: Don't delude yourself; you're not yearning for "culinary arts." You just want to feel like you're cooking and pretend to dine.
   PL: Nie łudź się: nie tęsknisz za „sztuką kulinarną”. Chcesz jedynie poczuć, że gotujesz, i udawać, że ucztujesz.
275. [Status [Sapsaree_Panic] — nazwa] 요리갈망
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Sapsaree_Panic]`
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Status [Sapsaree_Panic] — opis] - 패닉\n- 자신의 '배고픈 거예요' 수치 1당, 공격 레벨 2 증가, 받는 피해량 +5%
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +2 and take +5% damage for every "Got an appetite, you hear?" Stack on self
   PL: - Panika\n- Poziom Ataku +2 i otrzymuje obrażenia +5% za każdy ładunek „Głoduję, jasne?” na sobie
277. [Status [Sapsaree_Panic] — tekst klimatyczny] 넌 요리를 하고 싶은 게 아니다. 요리를 하는 느낌과 식사를 하는 흉내를 내고 싶은 것이지.
   źródło: Bufs-a1c10p1.json :: dataList[id=Sapsaree_Panic].flavor
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Status [HungryPeople_LowMorale] — nazwa] FOMO
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[HungryPeople_LowMorale]`
   limit: do 40 znaków
   EN: FOMO
   PL: FOMO
279. [Status [HungryPeople_LowMorale] — opis] - 사기 저하\n- 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n- 취약 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level +1 for every 20% missing HP on self (max 2)\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Poziom Ataku +1 za każde 20% utraconego HP (maks. 2)\n- Zyskuje 1 Wrażliwości
280. [Status [HungryPeople_LowMorale] — tekst klimatyczny] 이번 유행은 놓치면 안 되는데…!
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_LowMorale].flavor
   limit: do 120 znaków
   EN: Not again—I'm not gonna miss out on this season's trend!
   PL: Znów to samo — nie mogę przecież odpuścić tegorocznego trendu!
281. [Status [HungryPeople_Panic] — nazwa] FOMO
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_Panic].name
   kontekst: identyfikator statusu w tekstach: `[HungryPeople_Panic]`
   (powtórzenie elementu 278 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Status [HungryPeople_Panic] — opis] - 패닉\n- 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n- 취약 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level +1 for every 20% missing HP on self (max 2)\n- Gain 1 Fragile
   PL: - Panika\n- Poziom Ataku +1 za każde 20% utraconego HP (maks. 2)\n- Zyskuje 1 Wrażliwości
283. [Status [HungryPeople_Panic] — tekst klimatyczny] 이번 유행은 놓치면 안 되는데…!
   źródło: Bufs-a1c10p1.json :: dataList[id=HungryPeople_Panic].flavor
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Status [UnresolvedFeelings] — nazwa] 다층 레이어 패치워크
   źródło: Bufs-a1c10p1.json :: dataList[id=UnresolvedFeelings].name
   kontekst: identyfikator statusu w tekstach: `[UnresolvedFeelings]`
   limit: do 40 znaków
   EN: Layered Patchwork
   PL: Warstwowy Patchwork
285. [Status [UnresolvedFeelings] — opis] - 최댓값 : 30\n- 수치만큼 방어 레벨 증가\n- 경청에 대한 감사를 보유한 대상에게 피격 시 경청에 대한 감사 수치만큼 감소 (인격 별로 턴당 2회)\n- '들어줘서… 고맙다…' 스킬 합 패배 시 5 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=UnresolvedFeelings].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Gain Defense Level equal to Stack\n- When hit by target that has "Gratitude for Listening", lose Stack equal to "Gratitude for Listening" (2 times per turn per Identity)\n- On Clash Lose using the "Thank you... for listening..." Skill, lose 5 Stacks
   PL: - Maks. ładunków: 30\n- Zyskuje Poziom Obrony równy liczbie ładunków\n- Przy trafieniu przez cel posiadający „Wdzięczność za Wysłuchanie” traci ładunki w liczbie jego ładunków (2 razy na turę na Tożsamość)\n- Po przegranej w Starciu Umiejętnością „Dziękuję... za wysłuchanie...” traci 5 ładunków
286. [Status [UnresolvedFeelings] — tekst klimatyczny] 정작 자신은 이렇게 두꺼운 이불 속에 있는 채로 소리를 듣지 않는다.
   źródło: Bufs-a1c10p1.json :: dataList[id=UnresolvedFeelings].flavor
   limit: do 130 znaków
   EN: Ironically, it has deafened itself to any voice by hiding under wraps upon wraps of thick blankets.
   PL: Ironicznie ogłuchło na każdy głos, zakopawszy się pod warstwami grubych koców.
287. [Status [Wariness] — nazwa] 경계심
   źródło: Bufs-a1c10p1.json :: dataList[id=Wariness].name
   kontekst: identyfikator statusu w tekstach: `[Wariness]`
   limit: do 40 znaków
   EN: Guarded Caution
   PL: Czujność
288. [Status [Wariness] — opis] - 최댓값 : 10\n- 수치만큼 공격 레벨 감소, 방어 레벨 감소\n- 이 캐릭터가 합 패배 시, 3 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=Wariness].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Lose Offense Level and Defense Level equal to Stack\n- If this unit loses a Clash, lose 3 Stacks
   PL: - Maks. ładunków: 10\n- Traci Poziom Ataku i Poziom Obrony równy liczbie ładunków\n- Po przegranej tej jednostki w Starciu traci 3 ładunków
289. [Status [Wariness] — tekst klimatyczny] 처음 듣는 목소리라서 경계하는 게 아니다. 마음을 두드리려 하기에 경계하게 되는 것이다.
   źródło: Bufs-a1c10p1.json :: dataList[id=Wariness].flavor
   limit: do 150 znaków
   EN: The unfamiliarity of the Voice is not what makes one wary; it is the Voice knocking on the heart that does so.
   PL: Nie obcość Głosu budzi czujność — czujność budzi Głos pukający do serca.
290. [Status [ReliefSense] — nazwa] 경청에 대한 감사
   źródło: Bufs-a1c10p1.json :: dataList[id=ReliefSense].name
   kontekst: identyfikator statusu w tekstach: `[ReliefSense]`
   limit: do 40 znaków
   EN: Gratitude for Listening
   PL: Wdzięczność za Wysłuchanie
291. [Status [ReliefSense] — opis] - 최댓값 : 3\n- 턴 시작 시 수치 1 증가하고 정신력 10 회복\n- 이 스테이지의 보스에게 스킬로 피해를 입힐 때, 피해량 +(수치 x 50)%. 이후 해당 스킬 공격 종료 시 소멸\n- 수치가 3이면, 다층 레이어 패치워크의 방어 레벨 효과를 무시하고 피해를 입힘
   źródło: Bufs-a1c10p1.json :: dataList[id=ReliefSense].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Gain 1 Stack and heal 10 SP\n- Skills against this Stage's boss deal +(Stack x 50)% damage; then, this effect expires on Attack End of the Skill used\n- At 3 Stacks, damage dealt by this unit disregards Layered Patchwork's Defense Level effects
   PL: - Maks. ładunków: 3\n- Na początku tury zyskuje 1 ładunek i odzyskuje 10 Poczytalności\n- Umiejętności zadające obrażenia bossowi tego etapu zadają obrażenia +(ładunki x 50)%; po zakończeniu ataku tej Umiejętności efekt znika\n- Przy 3 ładunkach zadawane obrażenia ignorują efekt Poziomu Obrony „Warstwowego Patchworku”
292. [Status [ReliefSense] — tekst klimatyczny] 들어줘서… 고마워…
   źródło: Bufs-a1c10p1.json :: dataList[id=ReliefSense].flavor
   limit: do 120 znaków
   EN: Thank you... for listening...
   PL: Dziękuję... za wysłuchanie...
293. [Status [HorribleTerror] — nazwa] 끔찍한 반복 재생
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleTerror].name
   kontekst: identyfikator statusu w tekstach: `[HorribleTerror]`
   limit: do 40 znaków
   EN: Horribly Infinite Replay
   PL: Przerażające Nieskończone Odtwarzanie
294. [Status [HorribleTerror] — opis] - 최댓값 : 1\n- 턴 시작 시 E.G.O 침식 상태면, 이번 턴 동안 모든 대상에게 가하는 피해량 -50%\n- 턴 종료 시, 현재 체력의 50%만큼 체력 피해를 받고 소멸 (소수점 버림, 이 효과로 흐트러지지 않음)
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleTerror].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn Start: If this unit is in E.G.O Corrosion state, deal -50% damage to all targets this turn\n- Turn End: This unit takes 50% HP damage; then, this effect expires (rounded down, this effect cannot Stagger this unit)
   PL: - Maks. ładunków: 1\n- Na początku tury, jeżeli jednostka jest w stanie Korozji E.G.O, zadaje wszystkim celom obrażenia -50% w tej turze\n- Na koniec tury otrzymuje obrażenia HP w wysokości 50% obecnego HP i znika (zaokrąglane w dół; ten efekt nie oszołamia jednostki)
295. [Status [HorribleTerror] — tekst klimatyczny] 들을 때까지… 백화점 방송을 제대로 들을 때까지… 계속… 계속… 들어라…
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleTerror].flavor
   limit: do 140 znaków
   EN: Until you listen... until you truly hear the Grand Magasin's announcement... again... and again... listen...
   PL: Dopóki nie posłuchasz... dopóki naprawdę nie usłyszysz komunikatu Grand Magasin... jeszcze raz... i jeszcze raz... słuchaj...
296. [Status [HorribleEat] — nazwa] 반복 재생 반복
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleEat].name
   kontekst: identyfikator statusu w tekstach: `[HorribleEat]`
   limit: do 40 znaków
   EN: Repeat on Repeat
   PL: Powtarzanie Powtórzeń
297. [Status [HorribleEat] — opis] - 최댓값 : 15\n- 수치만큼 공격 레벨 증가
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleEat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- Gain Offense Level equal to Stack
   PL: - Maks. ładunków: 15\n- Zyskuje Poziom Ataku równy liczbie ładunków
298. [Status [HorribleEat] — tekst klimatyczny] 모두가 들을 때까지 반복되는 방송은 메아리가 되고, 메아리는 또 다시 반복되고 공명한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=HorribleEat].flavor
   limit: do 160 znaków
   EN: The broadcast is repeated until everyone hears it. It becomes an echo, and the echo repeats in turn until it resonates.
   PL: Komunikat powtarza się, dopóki nie usłyszy go każdy. Staje się echem, a echo z kolei powtarza się, aż dźwięk rezonuje.
299. [Status [NoirSuit] — nazwa] 르누아르 개버딘 원단 코트
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirSuit].name
   kontekst: identyfikator statusu w tekstach: `[NoirSuit]`
   limit: do 40 znaków
   EN: Le Noir: Gabardine Overcoat
   PL: Le Noir: Płaszcz z Gabardyny
300. [Status [NoirSuit] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 방어 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬, 패시브 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 30, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 보호막이 있는 상태에서 피격 시, 2 증가 (턴당 최대 20)\n- 턴 종료 시 보호막이 남아있으면, 10 증가\n- 수치가 100이 되면, 다음 턴에 아르뮈르 에비이예로 변경됨
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirSuit].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Defense Level Up for every 20 Stacks (max 4)\n- Gain Stack equal to Preservation Count this unit consumes or gains due to its Skill or Passive effects (max 30 per turn; this effect's Stack is gained regardless of Preservation's max Count)\n- When hit while this unit has Shield, gain 2 Stacks (20 per turn)\n- Turn End: If this unit has Shield, gain 10 Stacks\n- At 100 Stacks, convert this effect into "Armure Éveillée" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Obrony za każde 20 ładunków (maks. 4)\n- Gdy przez Umiejętności lub umiejętności pasywne zużyje albo zyska Licznik Zachowania, zyskuje ładunki w tej liczbie (maks. 30 na turę, łącznie z liczbą ponad Maks. licznika Zachowania)\n- Przy trafieniu, gdy posiada Tarczę, zyskuje 2 ładunki (maks. 20 na turę)\n- Na koniec tury, jeżeli nadal posiada Tarczę, zyskuje 10 ładunków\n- Przy 100 ładunkach w następnej turze zamienia się w „Armure Éveillée”
301. [Status [NoirSuit] — tekst klimatyczny] 경사가 위사보다 훨씬 많도록 트윌하여 만든 코트.\n특유의 높은 밀도로 착용자를 외부로부터 보호한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=NoirSuit].flavor
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An overcoat made from twill fabric, a type of weave made by threading several weft threads over fewer warp threads.\nIts characteristic high-density weave protects its wearer from external trauma.
   PL: Płaszcz utkany techniką twill, tak by wątku było znacznie więcej niż osnowy.\nJego charakterystyczna wysoka gęstość chroni noszącego przed urazami z zewnątrz.
302. [Status [Realisation] — nazwa] 아르뮈르 에비이예
   źródło: Bufs-a1c10p1.json :: dataList[id=Realisation].name
   kontekst: identyfikator statusu w tekstach: `[Realisation]`
   limit: do 40 znaków
   EN: Armure Éveillée
   PL: Armure Éveillée
303. [Status [Realisation] — opis] - 최댓값 : 100\n- 턴 시작시 수치 10당 정신력 5 회복\n- 턴 시작시 수치 20당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 기본 공격 스킬이 파괴 불가 코인으로 변경됨\n- 변경된 이후 다음 턴부터 턴 종료 시, 10 감소\n- 수치가 0이 되면, 르누아르 개버딘 원단 코트로 변경됨
   źródło: Bufs-a1c10p1.json :: dataList[id=Realisation].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Heal 5 SP for every 10 Stacks\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 each)\n- Convert all Base Attack Skill Coins into Unbreakable Coins\n- After this effect is converted, starting from the end of the next turn, lose 10 Stacks\n- At 0 Stacks, convert this effect into "Le Noir: Gabardine Overcoat"
   PL: - Maks. ładunków: 100\n- Na początku tury odzyskuje 5 Poczytalności za każde 10 ładunków\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności ataku podstawowego stają się Niezniszczalnymi Monetami\n- Począwszy od końca tury następnej po zamianie, traci na koniec tury 10 ładunków\n- Przy 0 ładunków zamienia się z powrotem w „Le Noir: Płaszcz Gabardynowy”
304. [Status [Realisation] — tekst klimatyczny] 외부에서 가해진 힘이 착용자에게 도달하지 못하게 한 르누아르의 원단은, 최종적으로 외부로부터의 변화를 제거하기 위해 깨어난다.\n축적한 에너지를 방출하여 외부 요인을 제거하는 방향으로 작동한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=Realisation].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Le Noir's fabric weave prevents external force from reaching its wearer. The purpose for which it awakens is to eliminate change imposed from the outside.\nThe fabric stores energy from attacks it absorbs, then expels all that force in a single burst to remove the external source of change.
   PL: Tkanina Le Noir nie pozwalała, by siła z zewnątrz docierała do noszącego. Ostatecznie przebudza się ona, by wyeliminować zmiany naciskające z zewnątrz.\nGromadzi energię z pochłoniętych ataków, by jednym wybuchem wyprzeć całą siłę i usunąć zewnętrzne źródło zmiany.
305. [Status [LaRouge_LowMorale] — nazwa] 가죽 밖으로!
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LaRouge_LowMorale]`
   limit: do 40 znaków
   EN: Leave the Leather Behind!
   PL: Skóra na Zewnątrz!
306. [Status [LaRouge_LowMorale] — opis] - 사기 저하\n방어 레벨 -3\n공격 레벨 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -3\n- Offense Level +1
   PL: - Niskie Morale\nPoziom Obrony -3\nPoziom Ataku +1
307. [Status [LaRouge_LowMorale] — tekst klimatyczny] 급한 마음에 튀어나가려는 몸의 내용물들이 피부를 뚫고 나올 지경이다.
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_LowMorale].flavor
   limit: do 160 znaków
   EN: Organs that ought to stay inside are wriggling in impatient excitement, trying to break through the skin to the other side.
   PL: Narządy, którym przystało zostawać w środku, dygoczą niecierpliwie, próbując przebić się przez skórę na drugą stronę.
308. [Status [LaRouge_Panic] — nazwa] 가죽 밖으로!
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LaRouge_Panic]`
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Status [LaRouge_Panic] — opis] - 패닉\n방어 레벨 -5\n공격 레벨 +2
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5\n- Offense Level +2
   PL: - Panika\nPoziom Obrony -5\nPoziom Ataku +2
310. [Status [LaRouge_Panic] — tekst klimatyczny] 급한 마음에 튀어나가려는 몸의 내용물들이 피부를 뚫고 나올 지경이다.
   źródło: Bufs-a1c10p1.json :: dataList[id=LaRouge_Panic].flavor
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Status [LaNoir_LowMorale] — nazwa] 껍질 속으로…
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LaNoir_LowMorale]`
   limit: do 40 znaków
   EN: Back into My Shell...
   PL: Z powrotem do Skorupy...
312. [Status [LaNoir_LowMorale] — opis] - 사기 저하\n속도 최댓값 -1\n방어 레벨 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Max Speed -1\n- Defense Level +1
   PL: - Niskie Morale\nMaks. Szybkość -1\nPoziom Obrony +1
313. [Status [LaNoir_LowMorale] — tekst klimatyczny] 이대로 단단하게 속으로, 안으로 움츠러든다.
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_LowMorale].flavor
   limit: do 120 znaków
   EN: Curl inward. Deeper. Tighter. Let the shell harden around what remains.
   PL: Zwinąć się do wewnątrz. Głębiej. Ciasniej. Niech skorupa stwardnieje wokół tego, co zostało.
314. [Status [LaNoir_Panic] — nazwa] 껍질 속으로…
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LaNoir_Panic]`
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Status [LaNoir_Panic] — opis] - 패닉\n속도 최댓값 -5\n방어 레벨 +3
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Max Speed -5\n- Defense Level +3
   PL: - Panika\nMaks. Szybkość -5\nPoziom Obrony +3
316. [Status [LaNoir_Panic] — tekst klimatyczny] 이대로 단단하게 속으로, 안으로 움츠러든다.
   źródło: Bufs-a1c10p1.json :: dataList[id=LaNoir_Panic].flavor
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [Status [NiddlePinned] — nazwa] 박제 상태
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddlePinned].name
   kontekst: identyfikator statusu w tekstach: `[NiddlePinned]`
   limit: do 40 znaków
   EN: Taxidermized
   PL: Zataksydermizowany
318. [Status [NiddlePinned] — opis] - 최댓값 : 2\n\n- 피격시, 출혈 횟수 1 증가 (턴당 3회)\n- 이 효과를 보유한 동안, 행동 불가 상태가 됨\n\n- 턴 종료시 체력 피해 15를 받고 자신의 바늘못 5 감소\n- 턴 종료시 1 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddlePinned].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n\n- When hit, gain +1 Bleed Count (3 times per turn)\n- Becomes Immobilized while this unit has this effect\n\n- Turn End: Lose 15 HP and 5 Naildle on self\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 2\n\n- Przy trafieniu zyskuje 1 Licznika Krwawienia (3 razy na turę)\n- Dopóki posiada ten efekt, pozostaje w stanie Unieruchomienia\n\n- Na koniec tury otrzymuje 15 obrażeń HP i traci 5 Igłogwoźdź\n- Na koniec tury traci 1 ładunek
319. [Status [NiddlePinned] — tekst klimatyczny] 원하는대로….핸드메이드! 비스포크! 핸드쏜!
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddlePinned].flavor
   limit: do 120 znaków
   EN: As you wish... Hand-made! Bespoke! Hand-sown!
   PL: Zgodnie z życzeniem... Ręcznie robione! Na miarę! Ręcznie szyte!
320. [Status [NiddleExpected] — nazwa] 혀에 꽂힌 바늘
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddleExpected].name
   kontekst: identyfikator statusu w tekstach: `[NiddleExpected]`
   limit: do 40 znaków
   EN: Tongue-pinning Needle
   PL: Igła Zakłuta w Języku
321. [Status [NiddleExpected] — opis] - 수비 스킬 장착시\n  - 자신의 바늘못 1 감소\n  - 이 효과 소멸\n\n- 턴 종료시, 바늘못 3을 얻고 이 효과 소멸
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddleExpected].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit equipped Defense Skills:\n· Lose 1 Naildle on self\n· This effect expires\n\n- Turn End: Gain 3 Naildle; then, this effect expires
   PL: - Jeżeli wyposażono Umiejętności obrony:\n· Traci 1 własnych Igłogwoźdź\n· Ten efekt znika\n\n- Na koniec tury zyskuje 3 Igłogwoźdź; po czym ten efekt znika
322. [Status [NiddleExpected] — tekst klimatyczny] 박힌 못을 빼기 위해서 잠시 멈춰야한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddleExpected].flavor
   limit: do 120 znaków
   EN: To remove a fixed nail, one must first come to a brief halt.
   PL: Aby wybić wbity gwóźdź, najpierw trzeba na chwilę przystanąć.
323. [Status [HowlingCocoon] — nazwa] 고치의 울음소리 - 미약
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoon].name
   kontekst: identyfikator statusu w tekstach: `[HowlingCocoon]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Frail
   PL: Krzyk Kokonu - Słabość
324. [Status [HowlingCocoon] — opis] - 가끔씩 고치의 울음소리가 들린다.\n- 스킬 최종 위력 +2
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Cocoon is crying intermittently.\n- Skill Final Power +2
   PL: - Kokon odzywa się płaczem co jakiś czas.\n- Moc Końcowa Umiejętności +2
325. [Status [HowlingCocoon] — tekst klimatyczny] 맞는 정보와 틀린 정보를 뒤섞어 말하는 자들은 되려 무지에서 비롯되어 당당하고 그래서 오히려 그 말들을 무시하기 어렵다고한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoon].flavor
   limit: do 170 znaków
   EN: Those who speak in half-truths and misinformation source their confidence from ignorance, which is what makes them so convincing.
   PL: Ci, którzy mówią półprawdami i dezinformacją, czerpią pewność siebie z niewiedzy — i właśnie to czyni ich tak przekonującymi.
326. [Status [HowlingCocoonTwo] — nazwa] 고치의 울음소리 - 악성
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoonTwo].name
   kontekst: identyfikator statusu w tekstach: `[HowlingCocoonTwo]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Vicious
   PL: Krzyk Kokonu - Złośliwość
327. [Status [HowlingCocoonTwo] — opis] - 고치의 울음소리가 멈추지 않는다.\n- 스킬 최종 위력 +3
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoonTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The Cocoon does not cease its cries.\n- Skill Final Power +3
   PL: - Płacz Kokonu nie ustaje.\n- Moc Końcowa Umiejętności +3
328. [Status [HowlingCocoonTwo] — tekst klimatyczny] 리지드랑… 셀비지는… 서로 관계없는거라고…. 으드득… 일부러! 일부러! 알고 그러는거지!!!
   źródło: Bufs-a1c10p1.json :: dataList[id=HowlingCocoonTwo].flavor
   limit: do 200 znaków
   EN: Rigid denim... and selvage... have jack to do with each other... Gnnnngh... You know this! You're just tryin' to piss me off, aren't you?! I knew it!!!
   PL: Sztywny dżins... i selvage... nie mają ze sobą nic wspólnego, mówię ci.... Wrrr... Celowo! Celowo! Ty to robisz specjalnie, nie?!!!
329. [Status [MeursaultBuffet] — nazwa] 못 박는 자
   źródło: Bufs-a1c10p1.json :: dataList[id=MeursaultBuffet].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBuffet]`
   limit: do 40 znaków
   EN: He Who Nails
   PL: Ten, Który Przybija
330. [Status [MeursaultBuffet] — opis] - 이번 전투에서 자신의 스킬 사용 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 2회)\n- 턴 시작 시 전장에 다른 아군이 있으면, 이번 턴에 피해로 사망하지 않음\n- 퇴각 불가능
   źródło: Bufs-a1c10p1.json :: dataList[id=MeursaultBuffet].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In this Encounter, if this unit uses its Skill, gain 2 E.G.O Resource of the corresponding Affinity (2 times per turn)\n- Turn Start: If another ally is on the field, damage taken by this unit does not kill this unit this turn\n- Cannot Retreat
   PL: - W tej walce przy użyciu Umiejętności dodatkowo zyskuje 2 Zasoby E.G.O odpowiedniego Grzechu (2 razy na turę)\n- Na początku tury, jeżeli na polu bitwy jest inny sojusznik, obrażenia nie pozbawiają go życia w tej turze\n- Nie może się wycofać
331. [Status [MeursaultBuffet] — tekst klimatyczny] 황금못을 쥐고 요람을 찢었고 신을 못 박는다.
   źródło: Bufs-a1c10p1.json :: dataList[id=MeursaultBuffet].flavor
   limit: do 120 znaków
   EN: Gripping the Golden Nail, he has rent the Cradle open and now nails a god upon a point.
   PL: Ściskając Złoty Gwóźdź, rozdarł Kołyskę — a teraz przybija boga jednym gwoździem.
332. [Status [Nutrition] — nazwa] 탈취해낸 무언가.
   źródło: Bufs-a1c10p1.json :: dataList[id=Nutrition].name
   kontekst: identyfikator statusu w tekstach: `[Nutrition]`
   limit: do 40 znaków
   EN: A Seized Something.
   PL: Coś Skonfiskowane.
333. [Status [Nutrition] — opis] - 최댓값 : 5\n- 턴 종료 시 다음 턴에 (수치 x 2)만큼 자신의 맥동 횟수가 증가하고 소멸\n- 소멸 시 수치가 최댓값이면, 다음 턴에 본체 최대 체력의 3%만큼 모든 부위가 보호막 얻음 (이 효과로 획득한 보호막은 턴 종료시에도 사라지지 않음)
   źródło: Bufs-a1c10p1.json :: dataList[id=Nutrition].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: Gain +(Stack x 2) Pulsation Count next turn; then, this effect expires\n- If this effect is at max Stack when expiring, all Parts gain Shield equal to 3% of the Core's HP next turn (Shield gained due to this effect does not expire at Turn End)
   PL: - Maks. ładunków: 5\n- Na koniec tury w następnej turze zyskuje Licznik Pulsowania +(ładunki x 2), po czym znika\n- Jeżeli przy znikaniu ma Maks. ładunków, w następnej turze wszystkie Części zyskują Tarczę równą 3% Maks. HP Rdzenia (Tarcza z tego efektu nie znika na koniec tury)
334. [Status [Nutrition] — tekst klimatyczny] 상대가 가진 좋아보이는 모든 것은 본래 자신의 것이어야만 하기에, 이것은 탈취가 아닌 정당한 회수일 뿐.
   źródło: Bufs-a1c10p1.json :: dataList[id=Nutrition].flavor
   limit: do 180 znaków
   EN: Everything desirable in another's possession should have belonged to me from the start. This is not theft, then, but rightful repossession.
   PL: Wszystko pożądane, co tkwi w cudzych rękach, od początku powinno należeć do mnie. To nie kradzież — to jedynie słuszne odzyskanie.
335. [Status [Gourmandise] — nazwa] 폭주
   źródło: Bufs-a1c10p1.json :: dataList[id=Gourmandise].name
   kontekst: identyfikator statusu w tekstach: `[Gourmandise]`
   limit: do 40 znaków
   EN: Uncontrollable Rampage
   PL: Paroksyzm
336. [Status [Gourmandise] — opis] - 기본값 : 3\n- 자신의 출혈 3당, 가하는 피해량 +5% (최대 30%)\n- 모든 부위가 흐트러짐 상태가 되지 않으며, 출혈로 받는 피해량 -75%\n- 턴 종료 시 1 감소\n- 효과가 소멸할 때 맥동 횟수를 모두 소모
   źródło: Bufs-a1c10p1.json :: dataList[id=Gourmandise].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Deal +5% damage for every 3 Bleed on self (max 30%)\n- All Parts cannot be Staggered; take -75% damage from Bleed\n- Turn End: Lose 1 Stack\n- Consume all Pulsation Count when this effect expires
   PL: - Wartość początkowa: 3\n- Zadaje obrażenia +5% za każde 3 własne Krwawienia (maks. 30%)\n- Żadna Część nie może ulec Oszołomieniu; otrzymuje -75% obrażeń od Krwawienia\n- Na koniec tury traci 1 ładunek\n- Gdy efekt znika, zużywa cały Licznik Pulsowania
337. [Status [Gourmandise] — tekst klimatyczny] 파편화된 육체 기관마다 갈기갈기 찢겨 나갈듯 뛰쳐나가려 한다. 주체할 수 없는 폭주는 되레 몸이 하나가 되게 한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=Gourmandise].flavor
   limit: do 200 znaków
   EN: Every disparate fragment of its anatomy jerks and convulses, trying to rip itself away. Such uncontrollable rampage brings the body together, ironically.
   PL: Każdy rozdrobniony okruch ciała szarpie się i konwulsyjnie wyrywa, pragnąc oderwać się od reszty. Ironicznie to właśnie taka niepowstrzymana furia skleja ciało w całość.
338. [Status [BuffetSick] — nazwa] 고통 주머니
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetSick].name
   kontekst: identyfikator statusu w tekstach: `[BuffetSick]`
   limit: do 40 znaków
   EN: Sac of Suffering
   PL: Worek Cierpienia
339. [Status [BuffetSick] — opis] - 최댓값 : 30\n- 턴 종료 시 폭주 효과가 소멸할 때 함께 소멸하며, 다음 턴에 수치 5당 취약 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetSick].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn End: This effect expires when Uncontrollable Rampage effect expires. Then, this unit gains 1 Fragile next turn for every 5 Stacks
   PL: - Maks. ładunków: 30\n- Na koniec tury znika razem z efektem Niepowstrzymanej Furii; w następnej turze zyskuje 1 Wrażliwości za każde 5 ładunków
340. [Status [BuffetSick] — tekst klimatyczny] 아픔은 모두 여기에 모인다. 따라서 이 기관이 터질 때 아픔은 더 오롯해진다.
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetSick].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This organ is the terminus of all painful sensory inputs.\nWhen it bursts, it will drown out all reason and reveal pain in its most unalloyed form.
   PL: Cały ból gromadzi się właśnie tutaj. Dlatego gdy ten organ pęka, ból ukazuje się w czystej, niezłomnej postaci.
341. [Status [SavePlacenta] — nazwa] 자기 보호
   źródło: Bufs-a1c10p1.json :: dataList[id=SavePlacenta].name
   kontekst: identyfikator statusu w tekstach: `[SavePlacenta]`
   limit: do 40 znaków
   EN: Self-preservation
   PL: Samozachowanie
342. [Status [SavePlacenta] — opis] - 생명줄이 적에게 일방 공격을 당할 때, 수치를 1 소모하여 적의 공격 대상을 몸통으로 변경하고 원호 방어 전용 스킬 사용\n- 턴 종료 시 소멸
   źródło: Bufs-a1c10p1.json :: dataList[id=SavePlacenta].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Lifecord is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to the Body; then, use Assist Defense-exclusive Skill\n- Turn End: This effect expires
   PL: - Gdy Linka Życia ma otrzymać Atak Jednostronny od wroga, zużywa 1 ładunek, aby przekierować celowanie wroga na Tułów, i używa Umiejętności zarezerwowanej dla Obrony Wsparcia\n- Znika na koniec tury
343. [Status [BloodyMucus] — nazwa] 세례[적]
   źródło: Bufs-a1c10p1.json :: dataList[id=BloodyMucus].name
   kontekst: identyfikator statusu w tekstach: `[BloodyMucus]`
   limit: do 40 znaków
   EN: Baptism [Crimson]
   PL: Chrzest [Czerwień]
344. [Status [BloodyMucus] — opis] - 최댓값 : 5\n- 자신의 출혈 위력 3당, 공격 레벨 1 증가 (최대 3)\n- 수치가 최댓값이면, 출혈 피해를 2배로 받으며 출혈 피해로 인해 사망하지 않음\n- 기본 공격 스킬 사용 시, (수치x2)만큼 자신의 출혈 횟수 증가\n- E.G.O 스킬 혹은 수비 스킬 사용 시, 수치 3 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=BloodyMucus].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Effect: 5\n- Offense Level +1 for every 3 Bleed Potency on self (max 3)\n- At max Stack, double the amount of damage taken from Bleed; this unit cannot be defeated due to Bleed damage\n- On Base Attack Skill Use, gain +(Stack x 2) Bleed Count\n- On E.G.O Skill or Defense Skill Use, lose 3 Stacks
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 za każde 3 Siły Krwawienia na sobie (maks. 3)\n- Przy Maks. ładunków otrzymuje podwójne obrażenia od Krwawienia, ale nie może zginąć od obrażeń Krwawienia\n- Przy użyciu Umiejętności ataku podstawowego zyskuje Licznik Krwawienia +(ładunki x 2)\n- Przy użyciu Umiejętności E.G.O lub Umiejętności obrony traci 3 ładunków
345. [Status [BloodyMucus] — tekst klimatyczny] ‘피로 살을 씻어내라’
   źródło: Bufs-a1c10p1.json :: dataList[id=BloodyMucus].flavor
   limit: do 120 znaków
   EN: "Let blood baptize the flesh"
   PL: „Niech krew obmyje ciało”
346. [Status [DeterioratingBody] — nazwa] 생의 본능
   źródło: Bufs-a1c10p1.json :: dataList[id=DeterioratingBody].name
   kontekst: identyfikator statusu w tekstach: `[DeterioratingBody]`
   limit: do 40 znaków
   EN: Instinctive Cling to Life
   PL: Instynkt Życia
347. [Status [DeterioratingBody] — opis] - 최댓값 : 5\n- 체력이 1 미만으로 감소하지 않음\n- 피격 시 1 감소 (스킬당 2회)\n- 턴 종료 시 1 감소. 효과가 소멸하면 사망
   źródło: Bufs-a1c10p1.json :: dataList[id=DeterioratingBody].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- HP does not drop below 1\n- When hit, lose 1 Stack (2 times per Skill)\n- Turn End: Lose 1 Stack; this unit is defeated when this effect expires
   PL: - Maks. ładunków: 5\n- HP nie spada poniżej 1\n- Przy trafieniu traci 1 ładunek (2 razy na Umiejętność)\n- Na koniec tury traci 1 ładunek; gdy efekt znika, jednostka ginie
348. [Status [DeterioratingBody] — tekst klimatyczny] 살고자 발악하는 그 모습은 끈질기지만, 결국 끝은 있다.
   źródło: Bufs-a1c10p1.json :: dataList[id=DeterioratingBody].flavor
   limit: do 140 znaków
   EN: Its instinct to cling to life is tenacious indeed, but in the end, the time comes when one must let go.
   PL: Ten zawzięty, ostatni instynkt przetrwania jest nieugięty — lecz i on ma swój kres.
349. [Status [BuffetFailed] — nazwa] 탈진
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetFailed].name
   kontekst: identyfikator statusu w tekstach: `[BuffetFailed]`
   limit: do 40 znaków
   EN: Exhausted
   PL: Wyczerpany
350. [Status [BuffetFailed] — opis] - 최댓값 : 3\n- 수치 1당, 속도 최솟값 -1, 최댓값 -1\n- 턴 시작 시 취약 1 얻음\n- 턴 종료 시 1 감소\n(모든 부위에 적용)
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetFailed].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Min & Max Speed -1 for every Stack\n- Turn Start: Gain 1 Fragile\n- Turn End: Lose 1 Stack\n(Applies on all Parts)
   PL: - Maks. ładunków: 3\n- Min. i Maks. Szybkość -1 za każdy ładunek\n- Na początku tury zyskuje 1 Wrażliwości\n- Na koniec tury traci 1 ładunek\n(Na wszystkie Części)
351. [Status [BuffetFailed] — tekst klimatyczny] 폭주 후에 찾아오는 제약. 힘의 속도와 크기에 따라 세계는 저마다의 형태로 대가를 치르게 한다.
   źródło: Bufs-a1c10p1.json :: dataList[id=BuffetFailed].flavor
   limit: do 170 znaków
   EN: Every outburst is followed by limitation. The world levies payment in forms proportionate to force and velocity of the outburst.
   PL: Po każdym wybuchu przychodzi ograniczenie. Świat wymaga zapłaty w formie proporcjonalnej do siły i prędkości wybuchu.
352. [Status [EarlyBuffet_LowMorale] — nazwa] 분열
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[EarlyBuffet_LowMorale]`
   limit: do 40 znaków
   EN: Inner Schism
   PL: Wewnętrzny Rozłam
353. [Status [EarlyBuffet_LowMorale] — opis] - 사기 저하\n- 방어 레벨 -3\n- 공격 레벨 +3\n- 세례[적]을 5 보유한 대상과 합 진행 시, 합 위력 +2
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Defense Level -3\n- Offense Level +3\n- In a Clash against targets that have 5 Baptism [Crimson], Clash Power +2
   PL: - Niskie Morale\n- Poziom Obrony -3\n- Poziom Ataku +3\n- Podczas Starcia z celem posiadającym 5 „Chrzest [Czerwień]” Moc Starcia +2
354. [Status [EarlyBuffet_LowMorale] — tekst klimatyczny] 대체…왜? 나는 어떻게 생겼어? 나는… 뭐야?
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_LowMorale].flavor
   limit: do 120 znaków
   EN: Why... ? How did I... come to exist? What... am I?
   PL: Czemu...? Jak to się stało, że... istnieję? Czym... ja jestem?
355. [Status [EarlyBuffet_Panic] — nazwa] 분열
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].name
   kontekst: identyfikator statusu w tekstach: `[EarlyBuffet_Panic]`
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Status [EarlyBuffet_Panic] — opis] - 패닉\n- 방어 레벨 -5\n- 공격 레벨 +3\n- 가하는 피해량 +10%\n- 세례[적]을 3 이상 보유한 대상과 합 진행 시, 합 위력 +3
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Defense Level -5 \n- Offense Level +3\n- Deal +10% damage\n- In a Clash against targets that have 3+ Baptism [Crimson], Clash Power +3
   PL: - Panika\n- Poziom Obrony -5\n- Poziom Ataku +3\n- Zadaje obrażenia +10%\n- Podczas Starcia z celem posiadającym 3 lub więcej „Chrzest [Czerwień]” Moc Starcia +3
357. [Status [EarlyBuffet_Panic] — tekst klimatyczny] 대체…왜? 나는 어떻게 생겼어? 나는… 뭐야?
   źródło: Bufs-a1c10p1.json :: dataList[id=EarlyBuffet_Panic].flavor
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Status [SisyphusTopaz] — nazwa] 토파즈
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusTopaz].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusTopaz]`
   limit: do 40 znaków
   EN: Topaz
   PL: Topaz
359. [Status [SisyphusTopaz] — opis] - 효과 없음
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusTopaz].desc
   limit: do 120 znaków
   EN: - No effect
   PL: - Brak efektu
360. [Status [SisyphusAmethyst] — nazwa] 아메시스트
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusAmethyst].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusAmethyst]`
   limit: do 40 znaków
   EN: Amethyst
   PL: Ametyst
361. [Status [SisyphusAmethyst] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusAmethyst].desc
   limit: do 130 znaków
   EN: - Inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency using Skills against enemies
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia
362. [Status [SisyphusAmber] — nazwa] 앰버
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusAmber].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusAmber]`
   limit: do 40 znaków
   EN: Amber
   PL: Bursztyn
363. [Status [SisyphusAmber] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusAmber].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu
364. [Status [SisyphusEmerald] — nazwa] 에메랄드
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusEmerald].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusEmerald]`
   limit: do 40 znaków
   EN: Emerald
   PL: Szmaragd
365. [Status [SisyphusEmerald] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusEmerald].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)
366. [Status [SisyphusGold] — nazwa] 골드
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusGold].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusGold]`
   limit: do 40 znaków
   EN: Gold
   PL: Złoto
367. [Status [SisyphusGold] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusGold].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1
368. [Status [SisyphusRuby] — nazwa] 루비
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusRuby].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusRuby]`
   limit: do 40 znaków
   EN: Ruby
   PL: Rubin
369. [Status [SisyphusRuby] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +1\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1\n- 최종 위력 +1
   źródło: Bufs-a1c10p1.json :: dataList[id=SisyphusRuby].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +1 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 1 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1\n- Moc Końcowa +1
370. [Status [RougeThreeCocoonShield] — nazwa] 믿음
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].name
   kontekst: identyfikator statusu w tekstach: `[RougeThreeCocoonShield]`
   limit: do 40 znaków
   EN: Devotion
   PL: Wiara
371. [Status [RougeThreeCocoonShield] — opis] - 턴 시작시 수치만큼 보호막을 얻음\n- 보호막이 감소하면 수치도 감소함
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain Shield equal to Stack\n- Lose Stack when losing Shield
   PL: - Na początku tury zyskuje Tarczę równą liczbie ładunków\n- Gdy traci Tarczę, traci też ładunki
372. [Status [RougeThreeCocoonShield] — tekst klimatyczny] ‘믿음은 바라는 것들의 실상이요, 바라는 것들의…’
   źródło: Bufs-a1c10p1.json :: dataList[id=RougeThreeCocoonShield].flavor
   limit: do 120 znaków
   EN: "Now faith is the substance of things hoped for, the          of things not seen."
   PL: „Wiara zaś jest poręką tego, czego się spodziewamy, i dowodem…”
373. [Status [RisingMadnessSisyphe] — nazwa] 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessSisyphe]`
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Status [RisingMadnessSisyphe] — opis] - 최댓값 : 2\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 피해량 증가 1, 취약 1 얻음\n· 모든 스킬이 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 1 Damage Up and 1 Fragile\n· Convert Coins on all Skills to Unbreakable Coins\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 2\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości\n· Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
375. [Status [RisingMadnessSisyphe] — tekst klimatyczny] …될 수 있어.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe].flavor
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Status [RisingMadnessSisyphe2nd] — nazwa] 따가운 햇살
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].name
   kontekst: identyfikator statusu w tekstach: `[RisingMadnessSisyphe2nd]`
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Status [RisingMadnessSisyphe2nd] — opis] - 최댓값 : 1\n- 턴 종료 시, 1 감소\n- 턴 시작 시 수치가 0이면 다음 효과가 적용됨\n· 위력 증가 2, 피해량 증가 2, 취약 3 얻음\n· 모든 스킬이 파괴 불가 코인으로 변경됨\n· 턴 종료 시, 다음 턴에 최댓값으로 회복
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Lose 1 Stack\n- Turn Start: At 0 Stack, apply the following effects:\n· Gain 2 Power Up, 2 Damage Up, and 3 Fragile\n· Convert Coins on all Skills to Unbreakable Coins\n· Turn End: Restore this effect to Max Stack next turn
   PL: - Maks. ładunków: 1\n- Na koniec tury traci 1 ładunek\n- Na początku tury przy 0 ładunkach stosowane są następujące efekty:\n· Zyskuje 2 Wzrost Mocy, 2 Wzrost Obrażeń i 3 Wrażliwości\n· Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Na koniec tury odzyskuje Maks. ładunków w następnej turze
378. [Status [RisingMadnessSisyphe2nd] — tekst klimatyczny] 햇빛은 닿는 모든것에 속삭인다. 뜨겁고 따가워져 익어가고 타들어갈지라도 내리쬔다.
   źródło: Bufs-a1c10p1.json :: dataList[id=RisingMadnessSisyphe2nd].flavor
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Status [WeakWithering_LowMorale] — nazwa] 헝클어진 재봉
   źródło: Bufs-a1c10p1.json :: dataList[id=WeakWithering_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WeakWithering_LowMorale]`
   limit: do 40 znaków
   EN: Messy Sewing
   PL: Poplątane Szycie
380. [Status [WeakWithering_LowMorale] — opis] - 사기 저하\n- 턴 시작시 공격 위력 감소 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=WeakWithering_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Spadku Mocy Ataku
381. [Status [WeakWithering_Panic] — nazwa] 헝클어진 재봉
   źródło: Bufs-a1c10p1.json :: dataList[id=WeakWithering_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WeakWithering_Panic]`
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Status [WeakWithering_Panic] — opis] - 패닉\n- 턴 시작시 공격 위력 감소 1, 피해량 감소 1 얻음
   źródło: Bufs-a1c10p1.json :: dataList[id=WeakWithering_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down and 1 Damage Down
   PL: - Panika\n- Na początku tury zyskuje 1 Spadku Mocy Ataku i 1 Spadku Obrażeń
383. [Status [NiddlePin] — nazwa] 바늘못
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddlePin].name
   kontekst: identyfikator statusu w tekstach: `[NiddlePin]`
   limit: do 40 znaków
   EN: Naildle
   PL: Gwoździk
384. [Status [NiddlePin] — opis] - 특수 출혈\n- 관통 피해를 받으면, 출혈 횟수 1 증가하고 수치 1 감소\n- 턴 종료시 출혈 1 얻고 수치 1 감소
   źródło: Bufs-a1c10p1.json :: dataList[id=NiddlePin].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- When taking Pierce damage, gain +1 Bleed Count and reduce this effect's Stack by 1\n- Turn End: Gain 1 Bleed and reduce this effect's Stack by 1
   PL: - Specjalne Krwawienie\n- Przy otrzymaniu obrażeń kłutych zyskuje 1 Licznika Krwawienia i traci 1 ładunek\n- Na koniec tury zyskuje 1 Krwawienia i traci 1 ładunek

## Statusy i efekty bojowe — Bufs-a1c10p2
- plik gry: `Bufs-a1c10p2.json`

385. [Status [TangleBlackYarn] — nazwa] 뒤엉킴
   źródło: Bufs-a1c10p2.json :: dataList[id=TangleBlackYarn].name
   kontekst: identyfikator statusu w tekstach: `[TangleBlackYarn]`
   limit: do 40 znaków
   EN: Tangling
   PL: Splątanie
386. [Status [TangleBlackYarn] — opis] - 최댓값 : 30\n- 수치당 받는 피해량 +1%\n- 수치 10당 기본 위력 -1\n- 턴 종료 시 수치 3당, 다음 턴에 속박 1 얻음 (최대 10)\n- <color=#ff6000><mark color=#ff000040><b><u>수비 스킬 사용 시</color></mark></b></u> 수치 절반 감소 (소수점 올림)
   źródło: Bufs-a1c10p2.json :: dataList[id=TangleBlackYarn].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 30\n- Take +1% damage for every Stack\n- Base Power -1 for every 10 Stacks\n- Turn End: Gain 1 Bind next turn for every 3 Stacks (max 10)\n- <color=#ff6000><mark color=#ff000040><b><u>On Defense Skill Use,</color></mark></b></u> lose half of the Stacks (rounded up)
   PL: - Maks. ładunków: 30\n- Otrzymuje obrażenia +1% za każdy ładunek\n- Moc Bazowa -1 za każde 10 ładunków\n- Na koniec tury zyskuje w następnej turze 1 Spętania za każde 3 ładunków (maks. 10)\n- <color=#ff6000><mark color=#ff000040><b><u>Przy użyciu Umiejętności obrony</u></b></mark></color> traci połowę ładunków (zaokrąglane w górę)
387. [Status [TangleBlackYarn] — tekst klimatyczny] 백화점은 실과 바늘로 얽힌 봉제의 세계. 이제는 바다에서 온것이라해도 그 몸은 실로 변하여 검은 물이 검은 실로 엉켜간다.
   źródło: Bufs-a1c10p2.json :: dataList[id=TangleBlackYarn].flavor
   limit: do 240 znaków
   EN: The department store is a world of sewing, bound together by thread and needle. Even that which came from the sea now finds its body turned to thread, black water tangling into black yarn.
   PL: Grand Magasin to świat szycia, spleciony nitką i igłą. Nawet to, co przyszło z morza, zamieniło się w nić — czarna woda plącze się w czarną przędzę.
388. [Status [SickBlackYarn] — nazwa] 뜯겨져 나가는 검은실밥
   źródło: Bufs-a1c10p2.json :: dataList[id=SickBlackYarn].name
   kontekst: identyfikator statusu w tekstach: `[SickBlackYarn]`
   limit: do 40 znaków
   EN: Bursting Blackstitch
   PL: Pękające Czarne Szwy
389. [Status [SickBlackYarn] — opis] - 최댓값 : 50\n- 수치당 받는 피해량 +1%\n- 턴 시작 시 수치 25당 취약 1 얻음
   źródło: Bufs-a1c10p2.json :: dataList[id=SickBlackYarn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Take +1% damage for every Stack\n- Turn Start: Gain 1 Fragile for every 25 Stacks
   PL: - Maks. ładunków: 50\n- Otrzymuje obrażenia +1% za każdy ładunek\n- Na początku tury zyskuje 1 Wrażliwości za każde 25 ładunków
390. [Status [SickBlackYarn] — tekst klimatyczny] 검은실에서 터져나온 실밥이 터질때마다 비릿하지만 어딘가 그리운 눈물 냄새가 난다.
   źródło: Bufs-a1c10p2.json :: dataList[id=SickBlackYarn].flavor
   limit: do 170 znaków
   EN: Each time a loose strand bursts from the black yarn, it carries the briny scent of tears... strangely nostalgic despite itself.
   PL: Każdy strzęp czarnej przędzy, gdy pęka, pachnie słonawymi łzami... dziwnie nostalgicznym, mimo wszystko.
391. [Status [HeavyBlackYarn] — nazwa] 검게 뭉친 실
   źródło: Bufs-a1c10p2.json :: dataList[id=HeavyBlackYarn].name
   kontekst: identyfikator statusu w tekstach: `[HeavyBlackYarn]`
   limit: do 40 znaków
   EN: Clumped Black Threads
   PL: Sklejone Czarne Nici
392. [Status [HeavyBlackYarn] — opis] - 최댓값 : 5\n- 수치 만큼 부위 별 슬롯 가중치 증가\n- 수치 1당, 받는 피해량 +10%
   źródło: Bufs-a1c10p2.json :: dataList[id=HeavyBlackYarn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Gain Slot Weight equal to Stack (per Part)\n- Take +10% damage for every Stack
   PL: - Maks. ładunków: 5\n- Zyskuje Wagę Slotu równą liczbie ładunków (na każdą Część)\n- Otrzymuje obrażenia +10% za każdy ładunek
393. [Status [HeavyBlackYarn] — tekst klimatyczny] 검은 것은 죽음과 질량의 도상. 검은 바닷물의 물기를 머금은것이 무거워지는것처럼 검은실이 뭉쳐가는것도 같은 결과를 낸다. 모든것을 품고 응어리져 가라앉고 멈춘다.
   źródło: Bufs-a1c10p2.json :: dataList[id=HeavyBlackYarn].flavor
   limit: do 270 znaków
   EN: Black is an image of death and mass. Just as black seawater grows heavy with what it holds, black thread gains weight as it clumps together. It gathers everything into itself, knots tight, sinks, and stops.
   PL: Czerń to wyobrażenie śmierci i masy. Jak to, co nasączono czarną wodą morską, staje się ciężkie, tak i sklejające się czarne nici dają ten sam rezultat. Wszystko obejmują, tężeją jak grudka, toną i zastygają.
394. [Status [HideBlackYarn] — nazwa] 검은 물 웅덩이
   źródło: Bufs-a1c10p2.json :: dataList[id=HideBlackYarn].name
   kontekst: identyfikator statusu w tekstach: `[HideBlackYarn]`
   limit: do 40 znaków
   EN: Pool of Black Water
   PL: Kałuża Czarnej Wody
395. [Status [HideBlackYarn] — opis] - 위력 최댓값 : 6\n- 횟수 최댓값 : 2\n- <color=#ff6000><mark color=#ff000040><b><u>피격 시 위력 1 감소</color></mark></b></u> (스킬당 1회)\n- 턴 종료 시 횟수 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>위력이나 횟수가 0이 되면 소멸</color></mark></b></u>\n- 흐트러짐 상태가 되지 않음\n- 일방 공격 시 가하는 피해량 +100%\n- 받는 피해량 -100%
   źródło: Bufs-a1c10p2.json :: dataList[id=HideBlackYarn].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Potency: 6\n- Max Count: 2\n- <color=#ff6000><mark color=#ff000040><b><u>When hit, lose 1 Potency</color></mark></b></u> (once per Skill)\n- Turn End: Lose 1 Count\n- <color=#ff6000><mark color=#ff000040><b><u>Expires if Potency or Count reaches 0</color></mark></b></u>\n- Cannot be Staggered\n- On Unopposed Attack, deal +100% damage\n- Take -100% damage
   PL: - Maks. Siły: 6\n- Maks. licznika: 2\n- <color=#ff6000><mark color=#ff000040><b><u>Przy trafieniu traci 1 Siły</u></b></mark></color> (1 raz na Umiejętność)\n- Na koniec tury traci 1 Licznika\n- <color=#ff6000><mark color=#ff000040><b><u>Znika, gdy Siła lub Licznik osiągną 0</u></b></mark></color>\n- Nie może ulec Oszołomieniu\n- Przy Ataku Jednostronnym zadaje obrażenia +100%\n- Otrzymuje obrażenia -100%
396. [Status [HideBlackYarn] — tekst klimatyczny] 이제는 바다도. 수족관도 아닌. 고인 물 웅덩이지만 그 곳은 큰 그리움을 품고있어서 잠시 몸을 숨길 정도의 넉넉한 슬픔은 고여있다.
   źródło: Bufs-a1c10p2.json :: dataList[id=HideBlackYarn].flavor
   limit: do 200 znaków
   EN: It is neither sea nor aquarium now, only a stagnant pond. Yet the great longing that has settled there holds enough sorrow to momentarily hide the body.
   PL: To już nie morze, ani akwarium — tylko stojąca kałuża. Ale wielka tęsknota, która się w niej osadziła, gromadzi tyle żalu, by na chwilę ukryć ciało.
397. [Status [AngryBlackYarn] — nazwa] 옛 포식자의 본능
   źródło: Bufs-a1c10p2.json :: dataList[id=AngryBlackYarn].name
   kontekst: identyfikator statusu w tekstach: `[AngryBlackYarn]`
   limit: do 50 znaków
   EN: Instinct of the Predator of Eld
   PL: Instynkt Dawnego Drapieżnika
398. [Status [AngryBlackYarn] — opis] - 이 효과를 보유한 부위 1개당, 모든 부위의 합 위력 +2\n- 대상의 뒤엉킴 수치 3당, 가하는 피해량 +5% (최대 50%)\n- 턴 종료 시 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=AngryBlackYarn].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All Parts gain Clash Power +2 for every Part that has this effect\n- Deal +5% damage for every 3 Tangling Stacks on target (max 50%)\n- Expires at Turn End
   PL: - Za każdą Część posiadającą ten efekt wszystkie Części zyskują Moc Starcia +2\n- Zadaje obrażenia +5% za każde 3 Splątania na celu (maks. 50%)\n- Znika na koniec tury
399. [Status [AngryBlackYarn] — tekst klimatyczny] 수족관 마다 포식자가 있었다. 백화점의 플로어 매니저처럼. 지금 포식자는 물고기의 모습이지만, 과거 시지프 시스템에서 아쿠아리움에 물고기의 모습은 없었다. 아쿠아리움속에 살았던 자들의 정신은 물고기여도 모습은 사람이었다.
   źródło: Bufs-a1c10p2.json :: dataList[id=AngryBlackYarn].flavor
   limit: do 380 znaków
   EN: Every aquarium had its predator, much like a Floor Manager in the department store. The predator now wears the shape of a fish, but in an earlier Sisyphe System, there were no fish-shaped beings in the Aquarium. The minds of those who lived there may have been fish, but their forms were human.
   PL: W każdym akwarium był swój drapieżnik — niczym Menedżer Piętra w Grand Magasin. Drapieżnik nosi dziś postać ryby, lecz w dawnym Systemie Sisyphe w Akwarium nie było istot o ciele ryby. Umysły tych, którzy tam żyli, były rybimi, ale ich postaci — ludzkie.
400. [Status [BlackYarn_LowMorale] — nazwa] 자식 잃은 것
   źródło: Bufs-a1c10p2.json :: dataList[id=BlackYarn_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BlackYarn_LowMorale]`
   limit: do 40 znaków
   EN: Bereaved of Child
   PL: Pogrążone w Żałobie po Dziecku
401. [Status [BlackYarn_LowMorale] — opis] - 사기 저하\n- 스킬 사용 시 메인 타겟이 뿌이면, 합 위력 +3, 기본 위력 +2\n- 피격 시 뒤엉킴 1 부여 (스킬당 3회)
   źródło: Bufs-a1c10p2.json :: dataList[id=BlackYarn_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Skill Use, if Pwie is the main target, Clash Power +3, Base Power +2\n- When hit, inflict 1 Tangling (3 times per Skill)
   PL: - Niskie Morale\n- Przy użyciu Umiejętności, jeżeli głównym celem jest Pwie, Moc Starcia +3, Moc Bazowa +2\n- Przy trafieniu nakłada 1 Splątania (3 razy na Umiejętność)
402. [Status [BlackYarn_Panic] — nazwa] 자식 잃은 것
   źródło: Bufs-a1c10p2.json :: dataList[id=BlackYarn_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BlackYarn_Panic]`
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Status [BlackYarn_Panic] — opis] - 패닉\n- 모든 공격의 대상을 뿌이로 지정\n- 스킬 사용 시 메인 타겟이 뿌이면, 합 위력 +6, 기본 위력 +4\n- 전투 시작 시 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 피격 시 뒤엉킴 1 부여 (스킬당 6회)
   źródło: Bufs-a1c10p2.json :: dataList[id=BlackYarn_Panic].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- All Attacks target Pwie\n- On Skill Use, if Pwie is the main target, Clash Power +6, Base Power +4\n- Combat Start: Convert all Skill Coins into Unbreakable Coins\n- When hit, inflict 1 Tangling (6 times per Skill)
   PL: - Panika\n- Wszystkie Ataki celują w Pwie\n- Przy użyciu Umiejętności, jeżeli głównym celem jest Pwie, Moc Starcia +6, Moc Bazowa +4\n- Na początku walki wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Przy trafieniu nakłada 1 Splątania (6 razy na Umiejętność)
404. [Status [FlowerLaurelWreath] — nazwa] 속죄의 월계관
   źródło: Bufs-a1c10p2.json :: dataList[id=FlowerLaurelWreath].name
   kontekst: identyfikator statusu w tekstach: `[FlowerLaurelWreath]`
   limit: do 40 znaków
   EN: Laurel Wreath of Atonement
   PL: Wieniec Laurowy Zadośćuczynienia
405. [Status [FlowerLaurelWreath] — opis] - 자신의 흐트러짐 선 모두 제거\n- 합 위력 +2\n- 침잠으로 받는 정신 피해 -50% (소수점 버림)\n- 턴 종료시 정신력 10 회복, 다음 턴에 신속 5 얻음\n- <color=#ff6000><mark color=#ff000040><b><u>합 승리시 본인과 조력자를 포함한 모든 아군의 정신력 5 회복</color></mark></b></u>
   źródło: Bufs-a1c10p2.json :: dataList[id=FlowerLaurelWreath].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Remove all Stagger Thresholds\n- Clash Power +2\n- Take -50% SP damage from Sinking (rounded down)\n- Turn End: Heal 10 SP and gain 5 Haste next turn\n- <color=#ff6000><mark color=#ff000040><b><u>Clash Win: Heal 5 SP for all allies including this unit and Assist Units</color></mark></b></u>
   PL: - Usuwa wszystkie Progi Oszołomienia\n- Moc Starcia +2\n- Otrzymuje -50% obrażeń Poczytalności od Zatonięcia (zaokr. w dół)\n- Na koniec tury odzyskuje 10 Poczytalności i 5 Pośpiechu w następnej turze\n- <color=#ff6000><mark color=#ff000040><b><u>Po wygranej w Starciu wszyscy sojusznicy (łącznie z Wsparciem) odzyskują 5 Poczytalności</u></b></mark></color>
406. [Status [FlowerLaurelWreath] — tekst klimatyczny] 죄를 고하는 그 모습, 꽃향기 아래에서 피어나라
   źródło: Bufs-a1c10p2.json :: dataList[id=FlowerLaurelWreath].flavor
   limit: do 120 znaków
   EN: Let the confession of its sins bloom beneath the fragrance of flowers.
   PL: Niech wyznanie grzechów rozkwita pod kwiatową wonią.
407. [Status [AlriuneSillage] — nazwa] 잔향
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriuneSillage].name
   kontekst: identyfikator statusu w tekstach: `[AlriuneSillage]`
   limit: do 40 znaków
   EN: Faint Aroma
   PL: Pogłos
408. [Status [AlriuneSillage] — opis] - 최댓값 : 30\n- 턴 종료 시 수치만큼 정신력 피해\n- 침잠 피해를 받으면, 수치 1 증가\n- 진동 폭발시, 자신을 제외한 무작위 아군 3명에게 잔향 1 ~ 2 부여\n- 수치가 최대면 진동을 2 얻고 진동 폭발, 자신의 침잠만큼 우울 피해를 받고 잔향 소멸. 이번 턴 동안 잔향을 얻을 수 없음\n- 사망 시, 아군에게 자신의 잔향을 수치의 절반만큼 무작위로 나눠서 부여 (소수점 버림)
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriuneSillage].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn End: Take SP damage equal to Stack\n- If this unit took Sinking damage, gain 1 Stack\n- On Tremor Burst, apply 1 ~ 2 Faint Aroma on 3 other random allies\n- At max Stack:\n · Gain 2 Tremor and trigger Tremor Burst on self\n · Take Gloom damage equal to Sinking on self\n · Faint Aroma expires\n · Cannot gain for the rest of the turn\n- On death, apply half of this unit's Faint Aroma Stack randomly between this unit's allies (rounded down)
   PL: - Maks. ładunków: 30\n- Na koniec tury otrzymuje obrażenia Poczytalności równe liczbie ładunków\n- Przy otrzymaniu obrażeń od Zatonięcia zyskuje 1 ładunek\n- Przy Wyładowaniu Wstrząsu nakłada 1–2 „Subtelnego Aromatu” na 3 innych losowych sojuszników\n- Przy Maks. ładunków zyskuje 2 Wstrząsu i wywołuje Wyładowanie Wstrząsu, otrzymuje obrażenia Posępności równe własnemu Zatonięciu, a Subtelny Aromat znika; do końca tury nie można go zyskać\n- Przy śmierci rozdziela losowo między sojuszników połowę własnych ładunków „Subtelnego Aromatu” (zaokrąglane w dół)
409. [Status [AlriuneSillage] — tekst klimatyczny] 향기는 그리움을. 그리움은 사무침을.
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriuneSillage].flavor
   limit: do 120 znaków
   EN: Fragrance begets longing. Longing, in turn, becomes yearning.
   PL: Zapach rodzi tęsknotę. A tęsknota — serdeczny ból.
410. [Status [AlriunePetal] — nazwa] 꽃잎
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriunePetal].name
   kontekst: identyfikator statusu w tekstach: `[AlriunePetal]`
   limit: do 40 znaków
   EN: Petals
   PL: Płatki
411. [Status [AlriunePetal] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>3이면 해당 턴에 강력한 스킬을 사용함</color></mark></b></u>\n- 흐트러진 대상에게 가하는 피해량 (자신의 꽃잎 x 10)% 만큼 증가\n- 턴 종료시 1 증가
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriunePetal].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>At 3 Stacks, use a powerful Skill that turn</color></mark></b></u>\n- Deal +(Petals Stack on self x 10)% damage to Staggered targets\n- Turn End: Gain 1 Stack
   PL: - Maks. ładunków: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Przy 3 ładunkach w tej turze używa potężnej Umiejętności</u></b></mark></color>\n- Zadaje oszołomionym celom obrażenia +(Płatki na sobie x 10)%\n- Na koniec tury zyskuje 1 ładunek
412. [Status [AlriunePetal] — tekst klimatyczny] 꽃잎 하나, 꽃잎 둘. 그리고 셋.
   źródło: Bufs-a1c10p2.json :: dataList[id=AlriunePetal].flavor
   limit: do 120 znaków
   EN: One petal, two petals... and then, three.
   PL: Płatek pierwszy, płatek drugi. A potem trzeci.
413. [Status [ThreadDye] — nazwa] 염색실
   źródło: Bufs-a1c10p2.json :: dataList[id=ThreadDye].name
   kontekst: identyfikator statusu w tekstach: `[ThreadDye]`
   limit: do 40 znaków
   EN: Dyed Thread
   PL: Barwiona Nić
414. [Status [ThreadDye] — opis] - 최댓값: 3\n- 효과 보유 시 신속 효과 획득 불가\n- 턴 종료시 다음 턴에 부여될 신속 제거\n- 턴 종료시 위력 만큼 다음 턴에 속박 부여 후 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>최댓값이면, 이번 턴과 다음 턴에 행동 불가를 얻고 소멸</color></mark></b></u>
   źródło: Bufs-a1c10p2.json :: dataList[id=ThreadDye].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- Cannot gain Haste while having this effect\n- Turn End: Remove Haste that will be applied next turn\n- Turn End: Gain Bind next turn equal to Potency and lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>At max Stack, gain Immobilize this turn and next turn; then, this effect expires</color></mark></b></u>
   PL: - Maks. ładunków: 3\n- Posiadając ten efekt, nie może zyskać Pośpiechu\n- Na koniec tury usuwa Pośpiech, który miał zostać nałożony w następnej turze\n- Na koniec tury nakłada w następnej turze Spętanie w wysokości Siły, po czym traci 1 ładunek\n- <color=#ff6000><mark color=#ff000040><b><u>Przy Maks. ładunków zyskuje Unieruchomienie na tę i następną turę, po czym znika</u></b></mark></color>
415. [Status [ThreadDye] — tekst klimatyczny] 실도 못과 같이 당신을 붙잡아 고정시킨다. 정해진 색으로.
   źródło: Bufs-a1c10p2.json :: dataList[id=ThreadDye].flavor
   limit: do 120 znaków
   EN: Like nails, threads will hold you fast, the color of its binds predetermined.
   PL: Jak gwóźdź, nić również przytrzymuje i unieruchamia. W z góry wyznaczonym kolorze.
416. [Status [SpreadingDye] — nazwa] 글로스 미디엄
   źródło: Bufs-a1c10p2.json :: dataList[id=SpreadingDye].name
   kontekst: identyfikator statusu w tekstach: `[SpreadingDye]`
   limit: do 40 znaków
   EN: Gloss Medium
   PL: Gloss Medium
417. [Status [SpreadingDye] — opis] - 대상에게 속박이 있으면, 출혈 위력 및 횟수 부여량 +1\n- 스킬 사용시 메인 타겟이 염색실이나 타르 염료를 보유했으면, 해당 스킬의 최종 위력 +1, 가하는 피해량 +20%
   źródło: Bufs-a1c10p2.json :: dataList[id=SpreadingDye].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If target has Bind, inflict 1 more Bleed Potency and Bleed Count\n- On Skill Use, if the main target has Dyed Thread or Tar Dye, the said Skill gains Final Power +1 and deals +20% damage
   PL: - Jeżeli cel posiada Spętanie, nakłada o 1 więcej Siły Krwawienia i Licznika Krwawienia\n- Przy użyciu Umiejętności, jeżeli główny cel posiada Barwioną Nić lub Barwnik Smołowy, ta Umiejętność zyskuje Moc Końcową +1 i zadaje obrażenia +20%
418. [Status [SpreadingDye] — tekst klimatyczny] 대부분의 염료는 색이 정해져 있다.\n하지만 이자의 염료에는 정해진 색이 없다.\n거칠게 칠해져 순수한 빛의 반사·굴절만으로 다양한 색을 내비친다.
   źródło: Bufs-a1c10p2.json :: dataList[id=SpreadingDye].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Most dyes are meant to have a color.\nBut this one's dye has none.\n\nApplied in rough, uneven strokes, it reveals a spectrum of colors through nothing but the reflection and refraction of pure light.
   PL: Większość barwników ma przypisany kolor.\nTen barwnik koloru nie ma.\nRzucony grubymi, nierównymi pociągnięciami, odsłania spektrum barw jedynie odbiciem i załamaniem czystego światła.
419. [Status [StickyDye] — nazwa] 타르 염료
   źródło: Bufs-a1c10p2.json :: dataList[id=StickyDye].name
   kontekst: identyfikator statusu w tekstach: `[StickyDye]`
   limit: do 40 znaków
   EN: Tar Dye
   PL: Barwnik Smołowy
420. [Status [StickyDye] — opis] - 최댓값: 1\n- 속도 최솟값, 최댓값 1 감소 (최소 1)
   źródło: Bufs-a1c10p2.json :: dataList[id=StickyDye].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Min & Max Speed -1 (min 1)
   PL: - Maks. ładunków: 1\n- Min. i Maks. Szybkość -1 (min. 1)
421. [Status [StickyDye] — tekst klimatyczny] 염료가 달라 붙어 발을 떼기 어렵다.
   źródło: Bufs-a1c10p2.json :: dataList[id=StickyDye].flavor
   limit: do 120 znaków
   EN: The dye clings, making every step harder to take.
   PL: Barwnik przykleja się, utrudniając każdy krok.
422. [Status [ChargeKhaki] — nazwa] 표류 관성
   źródło: Bufs-a1c10p2.json :: dataList[id=ChargeKhaki].name
   kontekst: identyfikator statusu w tekstach: `[ChargeKhaki]`
   limit: do 40 znaków
   EN: Inertia of Drifting
   PL: Bezwładność Dryfu
423. [Status [ChargeKhaki] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료 시, 횟수 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=ChargeKhaki].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count
   PL: - Specjalny Ładunek\n- Maks. licznika: 20\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Siłę i Licznik Ładunku\n- Na koniec tury traci 1 Licznika
424. [Status [ChargeKhaki] — tekst klimatyczny] 표류하는 자들은 흐름을 바꿀 수는 없어도 흐름을 공고히 하고 흐름 속에서 자신의 일을 한다.
   źródło: Bufs-a1c10p2.json :: dataList[id=ChargeKhaki].flavor
   limit: do 210 znaków
   EN: Those who are carried by the tide like buoys may not be able to change the flow of things, but they can still bolster the tide and commit to their acts within.
   PL: Dryfujący nie mogąc zmienić prądu, umacniają go i wykonują swoje dzieło w jego obrębie.
425. [Status [FinishedFabric] — nazwa] 재단된 원단
   źródło: Bufs-a1c10p2.json :: dataList[id=FinishedFabric].name
   kontekst: identyfikator statusu w tekstach: `[FinishedFabric]`
   limit: do 40 znaków
   EN: Cut Fabric
   PL: Skrojona Tkanina
426. [Status [FinishedFabric] — opis] - 최댓값 : 30\n- 충전 횟수(특수 충전 포함)를 획득하거나 소모하는 스킬의 피해량 +(수치)% (최대 30%)\n- 턴 종료 시, 5 감소\n· 이번 턴에 보호막이 파괴되었으면, 대신 10 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=FinishedFabric].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Skills that gain or consume Charge Count (including Unique Charge) deal +(Stack)% damage (max 30%)\n- Turn End: Lose 5 Stacks\n  · If Shield was broken this turn, lose 10 Stacks instead
   PL: - Maks. ładunków: 30\n- Umiejętności, które zyskują lub zużywają Licznik Ładunku (w tym Specjalny Ładunek), zadają obrażenia +(ładunki)% (maks. 30%)\n- Na koniec tury traci 5 ładunków\n· Jeżeli w tej turze Tarcza została złamana, zamiast tego traci 10 ładunków
427. [Status [FinishedFabric] — tekst klimatyczny] 저마다의 기능을 가진 원단은 제대로 재단되어야만 제 기능을 발휘한다.
   źródło: Bufs-a1c10p2.json :: dataList[id=FinishedFabric].flavor
   limit: do 120 znaków
   EN: Fabrics with functions of their own can only serve their purpose when properly cut.
   PL: Tkaniny, każda z własnym przeznaczeniem, spełniają swoją rolę tylko wtedy, gdy właściwie je się skroje.
428. [Status [LargeTailoringShears] — nazwa] 꽃가위
   źródło: Bufs-a1c10p2.json :: dataList[id=LargeTailoringShears].name
   kontekst: identyfikator statusu w tekstach: `[LargeTailoringShears]`
   limit: do 40 znaków
   EN: Blossom Scissors
   PL: Kwiatowe Nożyczki
429. [Status [LargeTailoringShears] — opis] - 최댓값 : 3\n- 수감자에게 가하는 피해량 +(5 + 수치 x 5)% (최대 20%)\n- 수선 대상을 보유한 수감자에게 스킬 사용 시, 수치만큼 합 위력이 증가
   źródło: Bufs-a1c10p2.json :: dataList[id=LargeTailoringShears].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Deal +(5 + Stack x 5)% damage against Sinners (max 20%)\n- On Skill Use against Alteration Target Sinners, gain Clash Power equal to Stack
   PL: - Maks. ładunków: 3\n- Zadaje Grzesznikom obrażenia +(5 + ładunki x 5)% (maks. 20%)\n- Przy użyciu Umiejętności na Grzesznika będącego Celem Poprawek zyskuje Moc Starcia równą liczbie ładunków
430. [Status [LargeTailoringShears] — tekst klimatyczny] 지하에서 만들어진 원초의 재료를 끊어 내기 위한 가위는 더욱 특별하고 거대하다. 처음으로 직조된 천을 자르고 잘라 왔던 이 가위에서 꽃이 피어나는 건 근원을 잘라 왔기 때문이며, 자연스러운 현상이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=LargeTailoringShears].flavor
   limit: do 370 znaków
   EN: The scissors used to sever the primordial materials produced underground are larger and more extraordinary still. These scissors have cut and recut the very first cloth ever woven. That flowers should bloom from them is only natural, for they have always cut things at their very roots.
   PL: Nożyczki służące do odcięcia pierwotnych materiałów powstałych pod ziemią są jeszcze bardziej szczególne i ogromne. To one tnęły i przycinały pierwszą utkaną tkaninę. Kwiaty kwitną na nich dlatego, że odcięły w samym źródle — to zjawisko naturalne.
431. [Status [TailoringTarget] — nazwa] 수선 대상
   źródło: Bufs-a1c10p2.json :: dataList[id=TailoringTarget].name
   kontekst: identyfikator statusu w tekstach: `[TailoringTarget]`
   limit: do 40 znaków
   EN: Alteration Target
   PL: Cel Poprawek
432. [Status [TailoringTarget] — opis] - 속도 최솟값, 최댓값 +5\n- 이번 턴에 처음으로 사용하는 스킬의 합 위력 +3\n- 전투 시작 시 수비 스킬을 장착하였다면, 수선사 아네트에게 받는 피해량이 80%만큼 감소\n- 턴 종료 시, 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=TailoringTarget].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +5\n- This turn's first-used Skill gains Clash Power +3\n- Combat Start: If this unit has an equipped Defense Skill, take -80% damage from Annette the Alterationist\n- Turn End: Lose 1 Stack
   PL: - Min. i Maks. Szybkość +5\n- Pierwsza Umiejętność użyta w tej turze zyskuje Moc Starcia +3\n- Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymuje od Annette, Krawcowej, obrażenia -80%\n- Na koniec tury traci 1 ładunek
433. [Status [TailoringTarget] — tekst klimatyczny] 사람에 맞춰 옷을 수선하는 것이 아니라, 옷에 맞춰 사람을 수선한다. 이곳에서는 옷이 사람을 결정하기에, 옷은 보존하고 대신 사람을 수선하는 것이 가치를 지키고, 고객을 위하는 일이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=TailoringTarget].flavor
   limit: do 310 znaków
   EN: Rather than altering the clothes to fit the person, she alters the person to fit the clothes. Here, clothes are what define the wearer; preserving the garment and altering the person is how worth is protected and how the customer is served.
   PL: Zamiast dopasowywać ubrania do człowieka, dopasowuje człowieka do ubrań. Tutaj to ubranie określa człowieka — zachować szatę, a poprawić człowieka, znaczy chronić wartość i służyć klientowi.
434. [Status [ScissorsMark] — nazwa] 마름질 표식
   źródło: Bufs-a1c10p2.json :: dataList[id=ScissorsMark].name
   kontekst: identyfikator statusu w tekstach: `[ScissorsMark]`
   limit: do 40 znaków
   EN: Mark of Shearing
   PL: Znak Wykrawania
435. [Status [ScissorsMark] — opis] - 최댓값 : 9\n- 수치만큼 방어 레벨이 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=ScissorsMark].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- Lose Defense Level equal to Stack
   PL: - Maks. ładunków: 9\n- Traci Poziom Obrony równy liczbie ładunków
436. [Status [ScissorsMark] — tekst klimatyczny] 옷감이나 재목 따위를 치수에 맞게 베어 내기 위한 표식
   źródło: Bufs-a1c10p2.json :: dataList[id=ScissorsMark].flavor
   limit: do 120 znaków
   EN: A cutting mark used to trim fabric and other materials to the required measurements.
   PL: Znak służący do wycinania tkanin i innych materiałów według właściwych wymiarów.
437. [Status [DamagedFabric] — nazwa] 재단되어버린
   źródło: Bufs-a1c10p2.json :: dataList[id=DamagedFabric].name
   kontekst: identyfikator statusu w tekstach: `[DamagedFabric]`
   limit: do 40 znaków
   EN: Sheared Apart
   PL: Rozcięte
438. [Status [DamagedFabric] — opis] - 최댓값 : 30\n- 턴 시작 시, 수치 6당 체력 회복 감소 1 얻음 (최대 5)\n- ‘패턴 따기’, ‘쉬르필 아 라 셴’ 스킬과 합 진행 시, 수치만큼 합 위력이 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=DamagedFabric].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start : Gain 1 HP Healing Down for every 6 Stacks (max 5)\n- Upon Clashing against "Patterning" or "Surfile à la Chaîne", lose Clash Power equal to Stack
   PL: - Maks. ładunków: 30\n- Na początku tury zyskuje 1 Spadku Regeneracji HP za każde 6 ładunków (maks. 5)\n- Podczas Starcia z Umiejętnościami „Wycinanie Wzoru” i „Surfile à la Chaîne” traci Moc Starcia równą liczbie ładunków
439. [Status [DamagedFabric] — tekst klimatyczny] 마름질된 천은 다시 꿰매더라도 패치워크가 될 뿐, 여러 가닥으로 이어졌던 원래의 천으로는 되돌아갈 수 없다.
   źródło: Bufs-a1c10p2.json :: dataList[id=DamagedFabric].flavor
   limit: do 210 znaków
   EN: Once the fabric has been cut apart, sewing the scraps back together only makes patchwork. It can never return to a single fabric woven from its original threads.
   PL: Posiekane płótno, choćby je zszyć, staje się tylko patchworkiem — nigdy nie wróci do jednej tkaniny utkanej z pierwotnych nici.
440. [Status [ThirdTailor_LowMorale] — nazwa] 손떨림
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ThirdTailor_LowMorale]`
   limit: do 40 znaków
   EN: Trembling Hands
   PL: Drżące Dłonie
441. [Status [ThirdTailor_LowMorale] — opis] - 사기 저하\n받는 피해량 +7.5%\n피격받을 때마다 자신의 진동 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +7.5% damage\n- Every time this unit is hit, gain +1 Tremor Count (once per Skill, max 5 per turn)
   PL: - Niskie Morale\nOtrzymuje obrażenia +7,5%\nPrzy każdym trafieniu zyskuje +1 Licznika Wstrząsu (1 raz na Umiejętność, maks. 5 na turę)
442. [Status [ThirdTailor_LowMorale] — tekst klimatyczny] 손이 떨리면, 가위질도 흔들려… 이대로는 재단할 수 없어…
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_LowMorale].flavor
   limit: do 160 znaków
   EN: My hands are starting to shake, and even the scissors won't stay steady... I won't be able to cut the pattern anymore...
   PL: Dłonie mi drżą, nożyce też chwiała... W ten sposób nie skroję już wzoru...
443. [Status [ThirdTailor_Panic] — nazwa] 손떨림
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ThirdTailor_Panic]`
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Status [ThirdTailor_Panic] — opis] - 패닉\n받는 피해량 +15%\n피격받을 때마다 자신의 진동 위력 1, 진동 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +15% damage\n- Every time this unit is hit, gain 1 Tremor Potency and +1 Tremor Count (once per Skill, max 5 per turn)
   PL: - Panika\nOtrzymuje obrażenia +15%\nPrzy każdym trafieniu zyskuje 1 Siły Wstrząsu i +1 Licznika Wstrząsu (1 raz na Umiejętność, maks. 5 na turę)
445. [Status [ThirdTailor_Panic] — tekst klimatyczny] 손이 떨리면, 가위질도 흔들려… 이대로는 재단할 수 없어…
   źródło: Bufs-a1c10p2.json :: dataList[id=ThirdTailor_Panic].flavor
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Status [GoldenLeatherEnhance] — nazwa] 따갑게 내리쬐는 햇살[바느질의 왕]
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].name
   kontekst: identyfikator statusu w tekstach: `[GoldenLeatherEnhance]`
   limit: do 70 znaków
   EN: Shower of Stinging Sunshine [King of Needleworks]
   PL: Parzące Promienie Słońca [Król Szycia]
447. [Status [GoldenLeatherEnhance] — opis] 대상의 바늘못 3당 자신의 스킬 최종 위력 +1 (최대 3)
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].desc
   limit: do 120 znaków
   EN: Skill Final Power +1 for every 3 Naildle on the target (max 3)
   PL: Moc Końcowa Umiejętności +1 za każde 3 Igłogwoźdź na celu (maks. 3)
448. [Status [GoldenLeatherEnhance] — tekst klimatyczny] ‘듣지 않아도돼. 들리지 않게하면돼. 네가 원한다면 그렇게 하는거야. 부정하지 않아도돼.’
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenLeatherEnhance].flavor
   limit: do 170 znaków
   EN: "You don't have to listen anymore. You only have to make it so you cannot hear them. Simply do what you want. Don't deny yourself."
   PL: „Nie musisz słuchać. Wystarczy sprawić, żebyś nie mógł słyszeć. Jeżeli tego chcesz, tak właśnie zrób. Nie musisz tego negować.”
449. [Status [NoirShieldUp] — nazwa] 검은 신의 가호
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldUp].name
   kontekst: identyfikator statusu w tekstach: `[NoirShieldUp]`
   limit: do 40 znaków
   EN: Blessing of the Obsidian God
   PL: Łaska Czarnego Boga
450. [Status [NoirShieldUp] — opis] - 위력 최댓값 : 999\n- 횟수 기본값 : 2\n- 흐트러짐 면역\n- 턴 시작시 수치만큼 부위가 보호막 얻음\n- 이 효과는 보호막 관리 효과로 취급됨\n- 보호막이 감소하면 수치도 감소함\n- 턴 종료시 횟수 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldUp].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 999\n- Base Count: 2\n- Cannot be Staggered\n- Turn Start: The Part gains Shield equal to Stack\n- This effect counts as a "Shield Management" effect\n- Lose Stack when losing Shield\n- Turn End: Lose 1 Count
   PL: - Maks. Siły: 999\n- Początkowy Licznik: 2\n- Nie może ulec Oszołomieniu\n- Na początku tury Część zyskuje Tarczę równą liczbie ładunków\n- Ten efekt liczy się jako efekt zarządzania Tarczą\n- Gdy traci Tarczę, traci też ładunki\n- Na koniec tury traci 1 Licznika
451. [Status [NoirShieldUp] — tekst klimatyczny] 검은 신. 검은 거인. 망치의 신부. 보존의 권능을 담당하는 백화점의 검은 신이 가장 직접적인 접촉적 가호. 망치는 단단하며 검은색은 모든것을 흡수하여 정지시킨다. 마치 죽음의 속성처럼.
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldUp].flavor
   limit: do 390 znaków
   EN: The Obsidian God. The Obsidian Giant. The Chaplain of the Hammer. The Obsidian God of the Grand Magasin, whose domain is the power of preservation, grants his blessing through direct contact. The hammer is hard, and its black hue absorbs all things and brings them to a halt... much like death itself.
   PL: Czarny Bóg. Czarny Gigant. Kapelan Młota. Czarny Bóg Wielkiego Sklepu, strzegący władzy zachowania, udziela swojej łaski poprzez najprostszy z kontaktów. Młot jest twardy, a czerń pochłania wszystko i zatrzymuje. Niczym atrybut śmierci.
452. [Status [NoirShieldPiece] — nazwa] 묵시적 형벌
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldPiece].name
   kontekst: identyfikator statusu w tekstach: `[NoirShieldPiece]`
   limit: do 40 znaków
   EN: Apocalyptic Vengeance
   PL: Apokaliptyczna Zemsta
453. [Status [NoirShieldPiece] — opis] - 최댓값 : 2\n- 받는 피해량 -10%\n- 수치가 2면, 최종 위력 -2
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldPiece].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take -10% damage\n- At 2 Stacks, Final Power -2
   PL: - Maks. ładunków: 2\n- Otrzymuje obrażenia -10%\n- Przy 2 ładunkach Moc Końcowa -2
454. [Status [NoirShieldPiece] — tekst klimatyczny] 가상의 질량 조각이 몸을 짓누르는듯하다. 거인의 형벌을 유사하게 구현한것. 언약에 따르면 높은곳으로 향하는것은 무거운 돌을 떠안고 묵묵히 오르는 형벌과 같다고 한다.
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirShieldPiece].flavor
   limit: do 300 znaków
   EN: It feels as though a fragment of imaginary mass is pressing down upon the body—a crude imitation of a Giant's punishment. According to the covenant, ascending to a higher place is akin to bearing a heavy boulder and climbing in silence.
   PL: Ciało zdaje się uciskać kawałek urojonej masy — prymitywne naśladowanie kary Giganta. Według Przymierza wstępowanie w górę niczym jest ponoszeniem ciężkiego głazu i milczącym wstępowaniem.
455. [Status [VibrationResonance] — nazwa] 보존 상쇄
   źródło: Bufs-a1c10p2.json :: dataList[id=VibrationResonance].name
   kontekst: identyfikator statusu w tekstach: `[VibrationResonance]`
   limit: do 40 znaków
   EN: Negation of Conservation
   PL: Negacja Zachowania
456. [Status [VibrationResonance] — opis] - 최댓값 : 2\n- 진동 폭발로 받는 피해량, 흐트러짐 피해량 -90%\n- 가하는 피해량 +20%\n- 턴 종료시 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=VibrationResonance].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take -90% damage from Tremor Burst; -90% to Stagger Threshold raised\n- Deal +20% damage\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 2\n- Otrzymuje -90% obrażeń od Wyładowania Wstrząsu i -90% obniżenia Progu Oszołomienia\n- Zadaje obrażenia +20%\n- Na koniec tury traci 1 ładunek
457. [Status [VibrationResonance] — tekst klimatyczny] 보존하고자하는 그 모든 움직임에 대한 반대 파장으로의 흔들림은 보존이 성립되지 못하게 한다.
   źródło: Bufs-a1c10p2.json :: dataList[id=VibrationResonance].flavor
   limit: do 170 znaków
   EN: A counterwave set against every motion that seeks preservation shakes preservation itself apart, preventing it from taking hold.
   PL: Przeciwfalowanie wobec każdego ruchu, który chce coś zachować, wstrząsa Zachowaniem tak, że nie może się utrwalić.
458. [Status [NoirField] — nazwa] 보존 신역
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirField].name
   kontekst: identyfikator statusu w tekstach: `[NoirField]`
   limit: do 40 znaków
   EN: Sanctum of Conservation
   PL: Domena Zachowania
459. [Status [NoirField] — opis] - 최댓값 : 2\n- 턴 시작 시, 잃은 체력 20%당 위력 증가 1, 피해량 증가 1 얻음 (각각 최대 3)\n- 턴 시작시 모든 누아르 소속 아군의 스킬 최종 위력이 이 버프 수치만큼 증가\n\n- 수치가 1 이상이면, 턴 시작시 자신을 포함한 누아르 소속인 모든 대상에게 아래 효과 적용\n· 정신력 +10\n· 공격 위력 +2\n· 방어 레벨 +2\n\n- 수치가 2 이상이면, 턴 시작시 누아르 소속이 아닌 모든 적에게 아래 효과 적용\n· 속도 최댓값 -1\n· 공격 레벨 -6\n· 방어 레벨 -2
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirField].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn Start: Gain 1 Power Up and 1 Damage Up for every 20% missing HP (max 3 respectively)\n- Turn Start: All "Le Noir" allies' Skills gain Final Power equal to Stack\n\n- Turn Start: At 1+ Stack, apply the following effects to all "Le Noir" allies, including this unit:\n · SP +10\n · Attack Power +2\n · Defense Level +2\n\n- Turn Start: At 2+ Stacks, apply the following effects to all non-"Le Noir" enemies:\n · Max Speed -1\n · Offense Level -6\n · Defense Level -2
   PL: - Maks. ładunków: 2\n- Na początku tury zyskuje 1 Wzrost Mocy i 1 Wzrost Obrażeń za każde 20% utraconego HP (każdy maks. 3)\n- Na początku tury Umiejętności wszystkich sojuszników z Le Noir zyskują Moc Końcową równą liczbie ładunków tego efektu\n\n- Przy 1 lub więcej ładunkach na początku tury stosuje następujące efekty na wszystkich jednostkach z Le Noir, włącznie z sobą:\n· Poczytalność +10\n· Moc Ataku +2\n· Poziom Obrony +2\n\n- Przy 2 lub więcej ładunkach na początku tury stosuje następujące efekty na wszystkich wrogach bez Le Noir:\n· Maks. Szybkość -1\n· Poziom Ataku -6\n· Poziom Obrony -2
460. [Status [NoirField] — tekst klimatyczny] 르누아르가 추구하는 보존의 가치가 보존되는 영역. 보존하는것을 보존하기위한 모든 르누아르적 행동이 이 영역안에서 이롭게 보존된다.이 영역은 영원한 보존의 영역이자 죽음에 한없이 가까워지고자하는 충동이 자극되는 영역이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirField].flavor
   limit: do 320 znaków
   EN: A sanctuary in which the value of conservation pursued by Le Noir is preserved. Within it, the Noirs' preservative actions are retained to their benefit. It is a realm of eternal conservation—a place that stirs the drive to infinitely approach death.
   PL: Domena, w której zachowuje się wartość zachowania, jakiej wyznaje Le Noir. Wszystkie działania zachowujące w stylu Le Noir zostają w jej obrębie zachowane ku ich korzyści. To domena wiecznego zachowania — miejsce, w którym pobudzany jest popęd nieskończonego zbliżania się do śmierci.
461. [Status [NoirSquareCollapse] — nazwa] 진형 붕괴
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirSquareCollapse].name
   kontekst: identyfikator statusu w tekstach: `[NoirSquareCollapse]`
   limit: do 40 znaków
   EN: Formation Collapse
   PL: Rozpad Szyku
462. [Status [NoirSquareCollapse] — opis] - 최댓값 : 10\n- 수치만큼 방어 레벨 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirSquareCollapse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Lose Defense Level equal to Stack
   PL: - Maks. ładunków: 10\n- Traci Poziom Obrony równy liczbie ładunków
463. [Status [NoirSquareCollapse] — tekst klimatyczny] 각자가 맡은 바를 자리에서 충실히 이행할거라 생각한 믿음이 무너질때 균열에서 의심이 싹튼다.
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirSquareCollapse].flavor
   limit: do 170 znaków
   EN: When faith—the faith that each will dutifully carry out their assigned role—begins to crumble, doubt takes root in the cracks.
   PL: Gdy wierzenie — że każdy sumiennie wypełni powierzoną mu rolę — zaczyna się kruszyć, w pęknięciach kiełkuje podejrzenie.
464. [Status [NoirNail] — nazwa] 약속된 못
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirNail].name
   kontekst: identyfikator statusu w tekstach: `[NoirNail]`
   limit: do 40 znaków
   EN: Promised Nail
   PL: Obiecany Gwóźdź
465. [Status [NoirNail] — opis] - 최댓값 : 3\n- 자신에게 진동 폭발 발생 시,\n· 자신의 진동 위력만큼 나태 피해를 입음\n· 취약 1 얻음\n· 수치 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirNail].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When Tremor Burst is triggered on this unit,\n · Take Sloth damage equal to Tremor Potency on self\n · Gain 1 Fragile\n · Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Gdy na tej jednostce wywołane zostaje Wyładowanie Wstrząsu,\n· otrzymuje obrażenia Lenistwa równe własnej Siły Wstrząsu\n· zyskuje 1 Wrażliwości\n· traci 1 ładunek
466. [Status [NoirNail] — tekst klimatyczny] 약속의 망치는 반드시 못을 박기로 약속됐다. 그렇기에 망치가 휘둘러진다면 그곳에 못이 없더라도 못이 있어야한다.
   źródło: Bufs-a1c10p2.json :: dataList[id=NoirNail].flavor
   limit: do 190 znaków
   EN: The promised hammer is bound by promise to drive in a nail. Therefore, whenever the hammer falls, a nail must exist there... even if there is none.
   PL: Obiecany młot jest związany przyrzeczeniem wbicia gwoździa. Dlatego za każdym razem, gdy młot spada, gwóźdź musi tam istnieć… nawet jeśli go nie ma.
467. [Status [BuffetField] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField].name
   kontekst: identyfikator statusu w tekstach: `[BuffetField]`
   limit: do 40 znaków
   EN: Le Vomissement
   PL: Le Vomissement
468. [Status [BuffetField] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨\n· 1단계 : 뿌이\n· 2단계 : 모든 아군 수감자에게 적용\n· 3단계 : 모든 대상에게 적용
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - After entering the Encounter, Le Vomissement's influence expands at Turn Start every 2 turns\n· Stage 1: Pwie\n· Stage 2: All allied Sinners\n· Stage 3: All targets
   PL: - Po pojawieniu się w walce co 2 tury na początku tury obszar wpływu Le Vomissement się rozszerza\n· Etap 1: Pwie\n· Etap 2: wszyscy sojusznicy Grzesznicy\n· Etap 3: wszystkie jednostki
469. [Status [BuffetField] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What is devoured for survival, for growth, incorporates what was outside into what is mine. Then it is expelled once more, and what was mine becomes part of the outside.\n\nIt is cyclical, expansive, and consumptive.
   PL: To, co pożerano, by przetrwać i rosnąć, czyniło z zewnątrz wnętrze — „moje”. Potem zostaje wyrzucone ponownie, a „moje” znów staje się „zewnętrznym”. To cykl, ekspansja i wyczerpanie.
470. [Status [BuffetField_0] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_0].name
   kontekst: identyfikator statusu w tekstach: `[BuffetField_0]`
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Status [BuffetField_0] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_0].desc
   limit: do 130 znaków
   EN: - After entering the Encounter, Le Vomissement's influence expands at Turn Start every 2 turns
   PL: - Po pojawieniu się w walce co 2 tury na początku tury obszar wpływu Le Vomissement się rozszerza
472. [Status [BuffetField_0] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_0].flavor
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Status [BuffetField_1] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_1].name
   kontekst: identyfikator statusu w tekstach: `[BuffetField_1]`
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Status [BuffetField_1] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_1].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Status [BuffetField_1] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_1].flavor
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Status [BuffetField_2] — nazwa] 르 보미스망 (Le Vomissement)
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_2].name
   kontekst: identyfikator statusu w tekstach: `[BuffetField_2]`
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Status [BuffetField_2] — opis] - 전투에 등장한 후, 2턴마다 턴 시작시 르 보미스망의 영향 범위가 확산됨
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_2].desc
   (powtórzenie elementu 471 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Status [BuffetField_2] — tekst klimatyczny] 생존하기 위해, 성장하기 위해 먹어치운 것들은 밖의 것은 내 것이되었고, 다시 분출되어 내 것은 밖의 것이 되어버린다. 이것은 반복적이고 확장적이며 고갈적이다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetField_2].flavor
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Status [GourmandiseAlly] — nazwa] 폭주
   źródło: Bufs-a1c10p2.json :: dataList[id=GourmandiseAlly].name
   kontekst: identyfikator statusu w tekstach: `[GourmandiseAlly]`
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Status [GourmandiseAlly] — opis] - 기본 위력 +1, 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 자신의 출혈 3당, 가하는 피해량 +5% (최대 30%), 대상의 체력 회복량 +10% (최대 100%, 소수점 버림)\n- 흐트러짐 상태가 되지 않으며, 출혈로 받는 피해량 -90% (강제 흐트러짐 제외)\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=GourmandiseAlly].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Power +1, convert all Coins on all Skills into Unbreakable Coins\n- Deal +5% damage for every 3 Bleed on self (max 30%); heal +10% more HP on target (max 100%, rounded down)\n- Cannot be Staggered; take -90% damage from Bleed (excluding forced Staggers)\n- Turn End: Lose 1 Stack
   PL: - Moc Bazowa +1, wszystkie Monety wszystkich Umiejętności stają się Niezniszczalnymi Monetami\n- Zadaje obrażenia +5% za każde 3 własne Krwawienia (maks. 30%); leczy cele o 10% więcej HP (maks. 100%, zaokrąglane w dół)\n- Nie może ulec Oszołomieniu; otrzymuje -90% obrażeń od Krwawienia (z wyłączeniem wymuszonych Oszołomień)\n- Na koniec tury traci 1 ładunek
481. [Status [GourmandiseAlly] — podsumowanie] 스킬이 강화됨
   źródło: Bufs-a1c10p2.json :: dataList[id=GourmandiseAlly].summary
   limit: do 120 znaków
   EN: Skills are strengthened
   PL: Umiejętności są wzmocnione
482. [Status [BloodyMucusAlly] — nazwa] 세례[적]
   źródło: Bufs-a1c10p2.json :: dataList[id=BloodyMucusAlly].name
   kontekst: identyfikator statusu w tekstach: `[BloodyMucusAlly]`
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Status [BloodyMucusAlly] — opis] - 최댓값 : 3\n- 공격 스킬 사용 시, 수치만큼 자신의 출혈 횟수 증가 (스킬당 1회)\n- 수비 스킬 사용 시, 수치 1 감소\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c10p2.json :: dataList[id=BloodyMucusAlly].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- On Attack Skill Use, gain Bleed Count equal to Stack (once per Skill)\n- On Defense Skill Use, lose 1 Stack\n- Turn End: Lose 1 Stack
   PL: - Maks. ładunków: 3\n- Umiejętności ataku zyskują Licznik Krwawienia równy ładunkom (1 raz na Umiejętność)\n- Przy użyciu Umiejętności obrony traci 1 ładunek\n- Na koniec tury traci 1 ładunek
484. [Status [BuffetGold] — nazwa] 황금계시
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGold].name
   kontekst: identyfikator statusu w tekstach: `[BuffetGold]`
   limit: do 40 znaków
   EN: Golden Revelation
   PL: Złote Objawienie
485. [Status [BuffetGold] — opis] - 최댓값 : 5\n- 수치 1당, 받는 피해량 +5%\n- 수치가 최댓값이면, 출혈이 있을 때 받는 피해량 +10%
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGold].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed: 5\n- Take +5% damage for every Stack\n- At max Stack, take +10% damage if this unit has Bleed
   PL: - Maks. ładunków: 5\n- Otrzymuje obrażenia +5% za każdy ładunek\n- Przy Maks. ładunków, jeżeli posiada Krwawienie, otrzymuje obrażenia +10%
486. [Status [BuffetGold] — tekst klimatyczny] 금빛은 아이를 인도한다. 다음은 누구를 해해야하는지. 그 유도에도 아이는 그 판단이 자신의 선택이라 여기게 된다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGold].flavor
   limit: do 200 znaków
   EN: The golden light guides the child toward whom they should harm next. Even under that guidance, the child believes the judgment to be entirely their own.
   PL: Złota poświata wskazuje dziecku, kogo skrzywdzić następnym razem. A mimo tej wskazówki dziecko wierzy, że wyrok jest w całości jego własnym wyborem.
487. [Status [BuffetShoes] — nazwa] 분홍색 메리 제인
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetShoes].name
   kontekst: identyfikator statusu w tekstach: `[BuffetShoes]`
   limit: do 40 znaków
   EN: Pink Mary Janes
   PL: Różowe Mary Jane
488. [Status [BuffetShoes] — opis] - 속도 최솟값 +3, 최댓값 +3
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetShoes].desc
   limit: do 120 znaków
   EN: - Min & Max Speed +3
   PL: - Min. Szybkość +3, Maks. Szybkość +3
489. [Status [BuffetShoes] — tekst klimatyczny] 신발… 고마워. 이걸 신으면 어디든 갈수있는거야? 같이 여행… 가고 싶어.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetShoes].flavor
   limit: do 120 znaków
   EN: Thanks... for the shoes. Can I go anywhere if I put these on? I wanna... travel with you.
   PL: Buty... dziękuję. Czy w nich mogę pójść dokądkolwiek? Chcę... pojechać z tobą w podróż.
490. [Status [BuffetGoldenClothes] — nazwa] 황금 수의
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGoldenClothes].name
   kontekst: identyfikator statusu w tekstach: `[BuffetGoldenClothes]`
   limit: do 40 znaków
   EN: Golden Shroud
   PL: Złoty Całun
491. [Status [BuffetGoldenClothes] — opis] - 방어 레벨 +10\n- 턴 종료 시 흐트러짐 상태이면, 흐트러짐 상태를 해제하고 최대 체력의 50%만큼 체력 회복 (전투당 1회)
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGoldenClothes].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +10\n- Turn End: If this unit is Staggered, recover from Stagger and heal 50% HP (once per Encounter)
   PL: - Poziom Obrony +10\n- Na koniec tury, jeżeli jednostka jest oszołomiona, wychodzi z Oszołomienia i odzyskuje 50% Maks. HP (1 raz na walkę)
492. [Status [BuffetGoldenClothes] — tekst klimatyczny] 아이는 어른의 옷을 걸쳤다. 다른 옷도아닌 누군가의 죽음으로 만들어진 가죽 옷이기에  어른으로 한걸음 나아갈수있다.
   źródło: Bufs-a1c10p2.json :: dataList[id=BuffetGoldenClothes].flavor
   limit: do 220 znaków
   EN: The child has donned the clothes of an adult. Not just any clothes, but a hide garment made from another's death. And so, the child takes one step closer to adulthood.
   PL: Dziecko przyodziało ubrania dorosłego. Nie byle jakie — szatę ze skóry zrobioną z czyjejś śmierci. I tak dziecko robi o krok bliżej dorosłości.
493. [Status [Buffet_LowMorale] — nazwa] 잊혀지지 않은 아픔
   źródło: Bufs-a1c10p2.json :: dataList[id=Buffet_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Buffet_LowMorale]`
   limit: do 40 znaków
   EN: Unforgotten Pain
   PL: Niezapomniany Ból
494. [Status [Buffet_LowMorale] — opis] - 사기 저하\n- 보호 3 얻음
   źródło: Bufs-a1c10p2.json :: dataList[id=Buffet_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 3 Protection
   PL: - Niskie Morale\n- Zyskuje 3 Ochrony
495. [Status [Buffet_Panic] — nazwa] 잊혀지지 않은 아픔
   źródło: Bufs-a1c10p2.json :: dataList[id=Buffet_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Buffet_Panic]`
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Status [Buffet_Panic] — opis] - 패닉\n- 보호 5 얻음
   źródło: Bufs-a1c10p2.json :: dataList[id=Buffet_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 5 Protection
   PL: - Panika\n- Zyskuje 5 Ochrony
497. [Status [RestrictMob] — nazwa] 규칙: 원피 손상 금지
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictMob].name
   kontekst: identyfikator statusu w tekstach: `[RestrictMob]`
   limit: do 50 znaków
   EN: Rule: Raw Hide Damage Prohibited
   PL: Zasada: Zakaz Uszkadzania Surowej Skóry
498. [Status [RestrictMob] — opis] 무두질된 죄수에게 공격 스킬을 지정하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictMob].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When Tanned Prisoner is targeted with an Attack Skill, this effect expires, and the attacker gains 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Gdy na początku walki Umiejętność ataku celuje w Wygarbowanego Więźnia, ten efekt znika, a atakujący zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
499. [Status [RestrictBoss] — nazwa] 규칙: 무두질 재촉 금지
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictBoss].name
   kontekst: identyfikator statusu w tekstach: `[RestrictBoss]`
   limit: do 50 znaków
   EN: Rule: Tanning Rush Prohibited
   PL: Zasada: Zakaz Ponaglania Garbowania
500. [Status [RestrictBoss] — opis] 통제자에게 공격 스킬을 지정하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictBoss].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When the Overseer is targeted with an Attack Skill, this effect expires, and the attacker gains 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Gdy na początku walki Umiejętność ataku celuje w Nadzorcę, ten efekt znika, a atakujący zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
501. [Status [RestrictTier1] — nazwa] 규칙: 공격적 태도 금지
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictTier1].name
   kontekst: identyfikator statusu w tekstach: `[RestrictTier1]`
   limit: do 50 znaków
   EN: Rule: Offensive Behavior Prohibited
   PL: Zasada: Zakaz Postawy Ofensywnej
502. [Status [RestrictTier1] — opis] 공격 스킬을 장착하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음 (EGO 스킬 제외)\n턴 종료시 이 버프 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictTier1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When an Attack Skill is equipped, this effect expires and gain 1 Tannery Rule Violation (excluding E.G.O Skills)\n- Turn End: This effect expires
   PL: Jeżeli na początku walki wyposażono Umiejętność ataku, ten efekt znika, a jednostka zyskuje 1 Naruszenia Zasad Garbarni (z wyłączeniem Umiejętności E.G.O)\nNa koniec tury ten efekt znika
503. [Status [RestrictDef] — nazwa] 규칙: 방어적 태도 금지
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictDef].name
   kontekst: identyfikator statusu w tekstach: `[RestrictDef]`
   limit: do 50 znaków
   EN: Rule: Defensive Behavior Prohibited
   PL: Zasada: Zakaz Postawy Defensywnej
504. [Status [RestrictDef] — opis] 수비 스킬을 장착하고 전투 시작시, 이 버프가 소멸하고 태너리 규칙 위반 1 얻음\n턴 종료시 이 버프 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictDef].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Combat Start: When a Defense Skill is equipped, this effect expires and gain 1 Tannery Rule Violation\n- Turn End: This effect expires
   PL: Jeżeli na początku walki wyposażono Umiejętności obrony, ten efekt znika, a jednostka zyskuje 1 Naruszenia Zasad Garbarni\nNa koniec tury ten efekt znika
505. [Status [RestrictDenied] — nazwa] 태너리 규칙 위반
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictDenied].name
   kontekst: identyfikator statusu w tekstach: `[RestrictDenied]`
   limit: do 40 znaków
   EN: Tannery Rule Violation
   PL: Naruszenie Zasad Garbarni
506. [Status [RestrictDenied] — opis] 최댓값 : 1\n통제자에게 받는 피해량 +30%\n자신의 공격 종료시, 통제자가 자신에게 ‘퍼니싱 버니싱 피니싱’ 스킬을 사용하고 버프 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictDenied].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +30% damage from the Overseer\n- At this unit's Attack End, the Overseer uses the "Punishing Burnishing Finishing" Skill on this unit; then, this effect expires
   PL: Maks. ładunków: 1\nOtrzymuje od Nadzorce obrażenia +30%\nPo zakończeniu ataku tej jednostki Nadzorca używa na niej Umiejętności „Punishing Burnishing Finishing”, po czym efekt znika
507. [Status [RestrictDenied] — tekst klimatyczny] 대상은 이 세계에 정의된 규칙을 위반한 죄인
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictDenied].flavor
   limit: do 120 znaków
   EN: The target is a transgressor who has violated the rules by which this world is bound.
   PL: Cel jest grzesznikiem, który naruszył reguły, którymi świat ten jest związany.
508. [Status [B3FreshMob] — nazwa] 주름잡히지 않은 가죽
   źródło: Bufs-a1c10p2.json :: dataList[id=B3FreshMob].name
   kontekst: identyfikator statusu w tekstach: `[B3FreshMob]`
   limit: do 40 znaków
   EN: Uncreased Hide
   PL: Skóra Bez Zagnieceń
509. [Status [B3FreshMob] — opis] 최댓값 : 1\n턴 시작시 보호막 20 얻음\n턴 시작시 보호 2 얻음\n턴 종료시 소멸
   źródło: Bufs-a1c10p2.json :: dataList[id=B3FreshMob].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn Start: Gain 20 Shield\n- Turn End: Gain 2 Protection\n- Expires at Turn End
   PL: Maks. ładunków: 1\nNa początku tury zyskuje 20 Tarczy\nNa początku tury zyskuje 2 Ochrony\nZnika na koniec tury
510. [Status [B3FreshMob] — tekst klimatyczny] 다룰 때 조심해주세요. 가죽 옷을 시착하고 몸을 구부리면 주름이 생겨버려 가치가 떨어지니까요.
   źródło: Bufs-a1c10p2.json :: dataList[id=B3FreshMob].flavor
   limit: do 160 znaków
   EN: Please handle with care. If you try on a hide garment and bend too much, it will crease... and that lowers its worth.
   PL: Proszę obchodzić się ostrożnie. Gdy przymierzysz szatę ze skóry i nadmiernie sięgniesz, powstaną zagniecenia... a to obniża jej wartość.
511. [Status [RestrictFailed] — nazwa] 규칙의 붕괴
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictFailed].name
   kontekst: identyfikator statusu w tekstach: `[RestrictFailed]`
   limit: do 40 znaków
   EN: Rule Collapse
   PL: Rozpad Zasad
512. [Status [RestrictFailed] — opis] 공격 레벨 +3\n방어 레벨 -3
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictFailed].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3\n- Defense Level -3
   PL: Poziom Ataku +3\nPoziom Obrony -3
513. [Status [RestrictFailed] — tekst klimatyczny] 규칙과 법칙의 차이를 아는가?
   źródło: Bufs-a1c10p2.json :: dataList[id=RestrictFailed].flavor
   limit: do 120 znaków
   EN: Do you know the difference between a rule and a law?
   PL: Czy wiesz, czym różni się zasada od prawa?
514. [Status [targetDye_LowMorale] — nazwa] 머신 잼
   źródło: Bufs-a1c10p2.json :: dataList[id=targetDye_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[targetDye_LowMorale]`
   limit: do 40 znaków
   EN: Jammed Machine
   PL: Zacięta Maszyna
515. [Status [targetDye_LowMorale] — opis] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -5%
   źródło: Bufs-a1c10p2.json :: dataList[id=targetDye_LowMorale].desc
   limit: do 120 znaków
   EN: Skills deal -5% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają celom o mniejszej Szybkości niż własna obrażenia -5%
516. [Status [targetDye_Panic] — nazwa] 머신 잼
   źródło: Bufs-a1c10p2.json :: dataList[id=targetDye_Panic].name
   kontekst: identyfikator statusu w tekstach: `[targetDye_Panic]`
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Status [targetDye_Panic] — opis] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -10%
   źródło: Bufs-a1c10p2.json :: dataList[id=targetDye_Panic].desc
   limit: do 120 znaków
   EN: Skills deal -10% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają celom o mniejszej Szybkości niż własna obrażenia -10%
518. [Status [targetDye_Panic] — tekst klimatyczny] 자신보다 빠른 것을 고정시킬 수 있는가?
   źródło: Bufs-a1c10p2.json :: dataList[id=targetDye_Panic].flavor
   limit: do 120 znaków
   EN: Can that which moves faster than oneself truly be fixed in place?
   PL: Czy to, co porusza się szybciej od ciebie, da się naprawdę zatrzymać w miejscu?
519. [Status [RouteBOneLeg] — opis] - 기본 공격 레벨 +25\n- 기본 방어 레벨 +25
   źródło: Bufs-a1c10p2.json :: dataList[id=RouteBOneLeg].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +25\n- Base Defense Level +25
   PL: - Podstawowy Poziom Ataku +25\n- Podstawowy Poziom Obrony +25
520. [Status [SapsareeGold] — nazwa] 따갑게 내리쬐는 햇살[수셰프]
   źródło: Bufs-a1c10p2.json :: dataList[id=SapsareeGold].name
   kontekst: identyfikator statusu w tekstach: `[SapsareeGold]`
   limit: do 60 znaków
   EN: Shower of Stinging Sunshine [Sous Chef]
   PL: Parzące Promienie Słońca [Sous-chef]
521. [Status [SapsareeGold] — opis] - 스킬 사용 시 대상의 매콤매콤소스 1당, 최종 위력 +1 (최대 3)\n- 자신의 스킬로 아군 처치 시 정신력 15 증가
   źródło: Bufs-a1c10p2.json :: dataList[id=SapsareeGold].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Skill Use, Final Power +1 for every "Fiery, Tongue-scorching Sauce" on target (max 3)\n- Gain 15 SP upon killing an ally with this unit's Skill
   PL: - Przy użyciu Umiejętności Moc Końcowa +1 za każdy ładunek „Pikantno-Pikantnego Sosu” na celu (maks. 3)\n- Gdy własna Umiejętność zabije sojusznika, zyskuje 15 Poczytalności
522. [Status [SapsareeGold] — tekst klimatyczny] ‘수셰프는 마음이 뜨끈한거예요. 자신감이 배부른 거예요!’
   źródło: Bufs-a1c10p2.json :: dataList[id=SapsareeGold].flavor
   limit: do 130 znaków
   EN: "Sous-chef has a warm, hearty heart, you hear? Sous-chef is stuffed full of confidence, you hear?!"
   PL: „Sous-chef ma serce gorące, jasne? Sous-chef jest nabity pewnością siebie, jasne?!”
523. [Status [GoldenManager] — nazwa] 따갑게 내리쬐는 햇살[3층 플로어 매니저]
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenManager].name
   kontekst: identyfikator statusu w tekstach: `[GoldenManager]`
   limit: do 70 znaków
   EN: Shower of Stinging Sunshine [3F Floor Manager]
   PL: Parzące Promienie Słońca [Menedżer Piętra 3]
524. [Status [GoldenManager] — opis] - 대상의 경계심 1당, 가하는 피해량 +5% (최대 50%)\n- 정신력 0 이하의 대상에게 스킬 사용 시 기본 위력 +3
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenManager].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +5% damage for every Guarded Caution on target (max 50%)\n- Base Power +3 On Skill Use against target that has 0 or less SP
   PL: - Zadaje obrażenia +5% za każdy ładunek Czujności na celu (maks. 50%)\n- Przy użyciu Umiejętności na cel z Poczytalnością 0 lub niższą Moc Bazowa +3
525. [Status [GoldenManager] — tekst klimatyczny] 햇빛이 뜨겁지만 천들을 떨쳐내지 못하고 마음은 이불속으로… 이불속으로…
   źródło: Bufs-a1c10p2.json :: dataList[id=GoldenManager].flavor
   limit: do 180 znaków
   EN: The sunshine burns hot, yet the cloth cannot be cast aside, and the heart retreats beneath the blankets... deeper beneath the blankets...
   PL: Słońce pali gorąco, lecz kołdry nie da się zrzucić, a serce chowa się pod kołdrę... głębiej pod kołdrę...
526. [Status [SisyphusSapphire] — nazwa] 사파이어
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusSapphire].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusSapphire]`
   limit: do 40 znaków
   EN: Sapphire
   PL: Szafir
527. [Status [SisyphusSapphire] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +1\n- 최종 위력 +1
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusSapphire].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +1\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +1\n- Moc Końcowa +1
528. [Status [SisyphusOnyx] — nazwa] 오닉스
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusOnyx].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusOnyx]`
   limit: do 40 znaków
   EN: Onyx
   PL: Onyks
529. [Status [SisyphusOnyx] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +2\n- 최종 위력 +1
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusOnyx].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +2\n- Final Power +1
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +2\n- Moc Końcowa +1
530. [Status [SisyphusDiamond] — nazwa] 다이아몬드
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusDiamond].name
   kontekst: identyfikator statusu w tekstach: `[SisyphusDiamond]`
   limit: do 40 znaków
   EN: Diamond
   PL: Diament
531. [Status [SisyphusDiamond] — opis] - 적에게 스킬로 부여하는 화상, 출혈, 진동, 파열, 침잠 위력 부여량 +1\n- 충전 횟수, 호흡 횟수 획득량 +2\n- 이 효과 획득 시 충전 횟수 10 얻음 (전투당 1회)\n- 합 위력 +2\n- 최종 위력 +1\n- 가하는 피해량 +10%
   źródło: Bufs-a1c10p2.json :: dataList[id=SisyphusDiamond].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skills inflict 1 more Burn, Bleed, Tremor, Rupture, and Sinking Potency against enemies\n- Gain +2 more Count when gaining Charge Count and Poise Count\n- Gain +10 Charge Count when gaining this effect (once per Encounter)\n- Clash Power +2\n- Final Power +1\n- Deal +10% damage
   PL: - Umiejętności nakładają na wrogów o 1 więcej Siły Podpalenia, Krwawienia, Wstrząsu, Rozdarcia i Zatonięcia\n- Zyskuje o 2 więcej Licznika przy zdobywaniu Licznika Ładunku i Licznika Oddechu\n- Przy zdobyciu tego efektu zyskuje 10 Licznika Ładunku (1 raz na walkę)\n- Moc Starcia +2\n- Moc Końcowa +1\n- Zadaje obrażenia +10%
532. [Status [OutOfControl_LowMorale] — nazwa] 통제 불능
   źródło: Bufs-a1c10p2.json :: dataList[id=OutOfControl_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[OutOfControl_LowMorale]`
   limit: do 40 znaków
   EN: Disabled Overseeing
   PL: Brak Kontroli
533. [Status [OutOfControl_LowMorale] — opis] - 사기 저하\n스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 공격 위력 감소 1 부여
   źródło: Bufs-a1c10p2.json :: dataList[id=OutOfControl_LowMorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Skill Final Power +1\n- Turn Start: Apply 1 Attack Power Down to all other allies
   PL: - Niskie Morale\nMoc Końcowa Umiejętności +1\nNa początku tury nakłada 1 Spadku Mocy Ataku na wszystkich innych sojuszników
534. [Status [OutOfControl_Panic] — nazwa] 통제 불능
   źródło: Bufs-a1c10p2.json :: dataList[id=OutOfControl_Panic].name
   kontekst: identyfikator statusu w tekstach: `[OutOfControl_Panic]`
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Status [OutOfControl_Panic] — opis] - 패닉\n스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 공격 위력 감소 1, 피해량 감소 1 부여
   źródło: Bufs-a1c10p2.json :: dataList[id=OutOfControl_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Skill Final Power +1\n- Turn Start: Apply 1 Attack Power Down and 1 Damage Down to all other allies
   PL: - Panika\nMoc Końcowa Umiejętności +1\nNa początku tury nakłada 1 Spadku Mocy Ataku i 1 Spadku Obrażeń na wszystkich innych sojuszników
536. [Status [LaNoirSuperior_LowMorale] — nazwa] 첫 껍질속으로…
   źródło: Bufs-a1c10p2.json :: dataList[id=LaNoirSuperior_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[LaNoirSuperior_LowMorale]`
   limit: do 40 znaków
   EN: Into the First Shell...
   PL: W Głąb Pierwszej Skorupy...
537. [Status [LaNoirSuperior_LowMorale] — opis] - 사기 저하\n공격 레벨 -2\n방어 레벨 +2
   źródło: Bufs-a1c10p2.json :: dataList[id=LaNoirSuperior_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Offense Level -2\n- Defense Level +2
   PL: - Niskie Morale\nPoziom Ataku -2\nPoziom Obrony +2
538. [Status [LaNoirSuperior_Panic] — nazwa] 첫 껍질속으로…
   źródło: Bufs-a1c10p2.json :: dataList[id=LaNoirSuperior_Panic].name
   kontekst: identyfikator statusu w tekstach: `[LaNoirSuperior_Panic]`
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Status [LaNoirSuperior_Panic] — opis] - 패닉\n공격 레벨 -3\n방어 레벨 +4
   źródło: Bufs-a1c10p2.json :: dataList[id=LaNoirSuperior_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Offense Level -3\n- Defense Level +4
   PL: - Panika\nPoziom Ataku -3\nPoziom Obrony +4

## Statusy i efekty bojowe — Bufs-a1c10p3
- plik gry: `Bufs-a1c10p3.json`

540. [Status [GoldenHideWarderFirstPhase] — nazwa] 박동
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenHideWarderFirstPhase]`
   limit: do 40 znaków
   EN: Thumping Pulse
   PL: Tętnienie
541. [Status [GoldenHideWarderFirstPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 합 위력 +1, 받는 피해량 -25%\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Clash Power +1, take -25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Starcia +1, otrzymuje obrażenia -25%\n- Na koniec tury znika
542. [Status [GoldenHideWarderFirstPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].summary
   limit: do 120 znaków
   EN: Gain Clash Power, take less damage
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń
543. [Status [GoldenHideWarderFirstPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: The domain of life. The will of change and birth.
   PL: Władza życia. Wola zmiany i narodzin.
544. [Status [GoldenFabricWarderFirstPhase] — nazwa] 정지
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenFabricWarderFirstPhase]`
   limit: do 40 znaków
   EN: Stillness
   PL: Bezruch
545. [Status [GoldenFabricWarderFirstPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +1, 가하는 피해량 +15%\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +1, deal +15% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +1, zadaje obrażenia +15%\n- Na koniec tury znika
546. [Status [GoldenFabricWarderFirstPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].summary
   limit: do 120 znaków
   EN: Gain Final Power, deal more damage
   PL: Moc Końcowa rośnie, zadaje więcej obrażeń
547. [Status [GoldenFabricWarderFirstPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: The domain of death. The urge for conservation and stillness.
   PL: Władza śmierci. Popęd Zachowania i Bezruchu.
548. [Status [MeursaultBuffWarderFirstPhase] — nazwa] 이방인
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBuffWarderFirstPhase]`
   limit: do 40 znaków
   EN: The Stranger
   PL: Obcy
549. [Status [MeursaultBuffWarderFirstPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 간수와 합 진행 시,\n· 합 위력 +1\n· 피해량 +(자신의 잃은 체력 비율/2)% (최대 20%)\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 2개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- When Clashing against the Warden:\n · Clash Power +1\n · Deal +(missing HP percentage on self / 2)% damage (max 20%)\n · On Clash Win, gain 1 E.G.O resource for each of the 2 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Podczas Starcia ze Strażnikiem:\n· Moc Starcia +1\n· Zadaje obrażenia +(procent utraconego HP na sobie / 2)% (maks. 20%)\n· Po wygranym Starciu zyskuje w sumie 2 Zasoby E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
550. [Status [MeursaultBuffWarderFirstPhase] — podsumowanie] 간수와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and deal more damage when Clashing with the Warden\nCannot be Staggered, cannot be defeated when there are other surviving allies
   PL: - Podczas Starcia ze Strażnikiem Moc Starcia i obrażenia rosną\n- Nie zostaje oszołomiony; gdy żyją inni sojusznicy, nie ginie
551. [Status [MeursaultBuffWarderFirstPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderFirstPhase].flavor
   limit: do 120 znaków
   EN: Was I an alien, a foreign element in both the department store and the City?
   PL: Czy i w Grand Magasin, i w Mieście byłem Obcym — obcym ciałem?
552. [Status [UnstableConnection] — nazwa] 불안정한 현현
   źródło: Bufs-a1c10p3.json :: dataList[id=UnstableConnection].name
   kontekst: identyfikator statusu w tekstach: `[UnstableConnection]`
   limit: do 40 znaków
   EN: Precarious Theophany
   PL: Chwiejna Teofania
553. [Status [UnstableConnection] — opis] - 최댓값 : 2\n- 턴 시작 시, (수치 x 4)만큼 합 위력 감소, 취약 얻음\n- 턴 종료 시, (45 - 현재 정신력)/2만큼 정신력 회복(소수점 버림)하고 수치 1 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=UnstableConnection].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn Start: Gain (Stack x 4) Clash Power Down and Fragile\n- Turn End: Heal ((45 - current SP) / 2) SP (rounded down); then, lose 1 Stack
   PL: - Maks. ładunków: 2\n- Na początku tury zyskuje (ładunki x 4) Spadku Mocy Starcia oraz Wrażliwości\n- Na koniec tury odzyskuje Poczytalność ((45 - obecna) / 2) (zaokr. w dół) i traci 1 ładunek
554. [Status [UnstableConnection] — podsumowanie] 턴 시작 시 합 위력 감소, 취약 얻음\n턴 종료 시 정신력 회복
   źródło: Bufs-a1c10p3.json :: dataList[id=UnstableConnection].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power Down and Fragile at Turn Start\nHeal SP at Turn End
   PL: - Na początku tury traci Moc Starcia i zyskuje Wrażliwość\n- Na koniec tury odzyskuje Poczytalność
555. [Status [UnstableConnection] — tekst klimatyczny] “어휴. 하필 이럴 때 연결이…”
   źródło: Bufs-a1c10p3.json :: dataList[id=UnstableConnection].flavor
   limit: do 120 znaków
   EN: "*sigh* Bad time for connection issues..."
   PL: „No ale co to ma być. Właśnie teraz połączenie…”
556. [Status [Dominion] — nazwa] 시지프 시스템 보존
   źródło: Bufs-a1c10p3.json :: dataList[id=Dominion].name
   kontekst: identyfikator statusu w tekstach: `[Dominion]`
   limit: do 40 znaków
   EN: Sisyphe System Preservation
   PL: Zachowanie Systemu Sisyphe
557. [Status [Dominion] — opis] - 최댓값 : 25\n- 가하는 피해량 +(수치)% (최대 25%)\n- 받는 피해량 -(수치)% (최대 25%)
   źródło: Bufs-a1c10p3.json :: dataList[id=Dominion].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 25\n- Deal +(Stack)% damage (max 25%)\n- Take -(Stack)% damage (max 25%)
   PL: - Maks. ładunków: 25\n- Zadaje obrażenia +(ładunki)% (maks. 25%)\n- Otrzymuje obrażenia -(ładunki)% (maks. 25%)
558. [Status [Dominion] — podsumowanie] 가하는 피해량 증가, 받는 피해량 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=Dominion].summary
   limit: do 120 znaków
   EN: Deal more and take less damage
   PL: Zadaje więcej obrażeń i otrzymuje mniej
559. [Status [Dominion] — tekst klimatyczny] “다른 구역에서 와서 그런가? 왜 이렇게 몰라주는지 모르겠군. 시지프 탑이 무너지면, 말레우스 말레피카룸이니 뭐니 하는 놈들이… 하아.”\n\n“이방인들이 다 그렇지 뭐. N사 사정이나 세상 돌아가는 거엔 관심도 없고. 어휴… 됐다, 됐어. 어디 끝까지 해보자고.”
   źródło: Bufs-a1c10p3.json :: dataList[id=Dominion].flavor
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Is it because you're from another District or something? How do you people still not get it? If Sisyphe Tower goes down, those Malleus Maleficarum or whatever they're called are going to—*sigh*"\n\n"Same old strangers and outsiders, I suppose. You people don't give two hoots what happens to N Corp. or what the world is coming to. Ugh... never mind. Now let's see just how far you're willing to take this."
   PL: „Bo żeś z innego Dystryktu? Nie pojmuję, czemu nikt tego nie docenia. Jeżeli Wieża Sisyphe runie, to ci tamci Malleus Maleficarum czy jak ich tam... Aaaah.”\n\n„Obcy to obcy. Nie obchodzi ich ani los N Corp., ani to, co się dzieje ze światem. Ufff... przestań, przestań. Zobaczymy, jak daleko zajdziesz.”
560. [Status [BlackStigmata] — nazwa] 죄악감
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata].name
   kontekst: identyfikator statusu w tekstach: `[BlackStigmata]`
   limit: do 40 znaków
   EN: Compunction
   PL: Poczucie Winy
561. [Status [BlackStigmata] — opis] - 정신력이 있는 대상이면, 패닉 유형이 '죄악감'으로 변경됨\n- 정신력이 없는 대상이면, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 죄악감 패닉 효과\n- 사기 저하 : 속도 최솟값, 최댓값 -1, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 패닉 : 속도 최솟값, 최댓값 -2, 자신보다 속도가 높은 대상에게 받는 피해량 +15%
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Panic Type changes to "Compunction"\n- Non-SP Units: Take +10% damage from targets with faster Speed than self\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Units without SP" conditional to certain enemies that have SP but cannot change their Panic Types\n\n※ Compunction Panic Effect:\n- Low Morale: Min & Max Speed -1; take +10% damage from targets with faster Speed than this unit's\n- Panic: Min & Max Speed -2; take +15% damage from targets with faster Speed than this unit's
   PL: - Jeżeli cel posiada Poczytalność, jego typ Paniki zmienia się na „Poczucie Winy”\n- Jeżeli cel nie posiada Poczytalności, otrzymuje obrażenia +10% od celów o większej Szybkości niż własna\n- Na koniec tury traci 1 ładunek\n- Ten efekt się nie kumuluje — jest odnawiany\n- U pewnych wrogów posiadających Poczytalność, którzy nie mogą zmienić typu Paniki, stosuje się efekt dla celów bez Poczytalności\n\n※ Efekt Paniki „Poczucia Winy”\n- Niskie Morale: Min. i Maks. Szybkość -1; otrzymuje obrażenia +10% od celów o większej Szybkości niż własna\n- Panika: Min. i Maks. Szybkość -2; otrzymuje obrażenia +15% od celów o większej Szybkości niż własna
562. [Status [BlackStigmata] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose Min & Max Speed\nTake more damage from targets with faster Speed than self
   PL: Traci Min. i Maks. Szybkość\nOtrzymuje więcej obrażeń od celów o większej Szybkości niż własna
563. [Status [BlackStigmata] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata].flavor
   limit: do 120 znaków
   EN: "You feel your sins crawling on your back."
   PL: „Czujesz, jak grzechy wpełzają ci po plecach.”
564. [Status [BlackStigmata_Main] — nazwa] 죄악감
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Main].name
   kontekst: identyfikator statusu w tekstach: `[BlackStigmata_Main]`
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Status [BlackStigmata_Main] — opis] - 정신력이 있는 대상이면, 패닉 유형이 '죄악감'으로 변경됨\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Main].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Change their Panic Type to "Compunction"\n- Turn End: Lose 1 Stack
   PL: - Jeżeli cel posiada Poczytalność, zmienia swój typ Paniki na „Poczucie Winy”\n- Na koniec tury traci 1 ładunek
566. [Status [BlackStigmata_Main] — podsumowanie] 패닉 유형이 '죄악감'으로 변경
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Main].summary
   limit: do 120 znaków
   EN: Change Panic Type to "Compunction"
   PL: Zmienia typ Paniki na „Poczucie Winy”
567. [Status [BlackStigmata_Main] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Main].flavor
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Status [BlackStigmata_Sub] — nazwa] 죄악감
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Sub].name
   kontekst: identyfikator statusu w tekstach: `[BlackStigmata_Sub]`
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Status [BlackStigmata_Sub] — opis] - 정신력이 없는 대상이면, 자신보다 속도가 높은 대상에게 받는 피해량 +10%\n- 턴 종료 시 1 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Sub].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Non-SP Units: Take +10% damage from targets with faster Speed than self\n- Turn End: Lose 1 Stack
   PL: - Jeżeli cel nie posiada Poczytalności, otrzymuje obrażenia +10% od szybszych celów\n- Na koniec tury traci 1 ładunek
570. [Status [BlackStigmata_Sub] — podsumowanie] 자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Sub].summary
   limit: do 120 znaków
   EN: Take more damage from targets with faster Speed than self
   PL: Otrzymuje więcej obrażeń od celów o większej Szybkości niż własna
571. [Status [BlackStigmata_Sub] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Sub].flavor
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Status [BlackStigmata_LowMorale] — nazwa] 죄악감
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BlackStigmata_LowMorale]`
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Status [BlackStigmata_LowMorale] — opis] - 사기 저하\n- 속도 최솟값, 최댓값 -1, 자신보다 속도가 높은 대상에게 받는 피해량 +10%
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Min & Max Speed -1; take +10% damage from targets with faster Speed than self
   PL: - Niskie Morale\n- Min. i Maks. Szybkość -1; otrzymuje obrażenia +10% od celów o większej Szybkości niż własna
574. [Status [BlackStigmata_LowMorale] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].summary
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Status [BlackStigmata_LowMorale] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_LowMorale].flavor
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Status [BlackStigmata_Panic] — nazwa] 죄악감
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BlackStigmata_Panic]`
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Status [BlackStigmata_Panic] — opis] - 패닉\n- 속도 최솟값, 최댓값 -2, 자신보다 속도가 높은 대상에게 받는 피해량 +15%
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Min & Max Speed -2; take +15% damage from targets with faster Speed than self
   PL: - Panika\n- Min. i Maks. Szybkość -2; otrzymuje obrażenia +15% od celów o większej Szybkości niż własna
578. [Status [BlackStigmata_Panic] — podsumowanie] 속도 최솟값, 최댓값 감소\n자신보다 속도가 높은 대상에게 받는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Panic].summary
   (powtórzenie elementu 562 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Status [BlackStigmata_Panic] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: Bufs-a1c10p3.json :: dataList[id=BlackStigmata_Panic].flavor
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Status [GoldenHideWarderSecondPhase] — nazwa] 박동
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenHideWarderSecondPhase]`
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Status [GoldenHideWarderSecondPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 이 효과를 보유한 수감자가 간수의 <color=#ff6000><mark=#ff000040><b><u>‘사형 집행’</u></b></mark></color> 스킬과 <color=#ff6000><mark=#ff000040><b><u>합하여 승리</u></b></mark></color>했으면, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 250%만큼 보호막</u></b></mark></color> 얻음 (간수의 ‘사형 집행’ 공격 종료 시, 이 효과로 얻은 보호막 수치만큼 수감자가 보유한 보호막에서 차감함)\n- 합 위력 +2, 받는 피해량 -25%\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Turn Start: A random Sinner gains this effect\n- On Clash Win, if the Sinner who has this effect <color=#ff6000><mark=#ff000040><b><u>won the Clash</u></b></mark></color> against the Warden's <color=#ff6000><mark=#ff000040><b><u>"Death Unto the Condemned"</u></b></mark></color> Skill, gain <color=#ff6000><mark=#ff000040><b><u>Shield equal to 250% of the Sinner's max HP</u></b></mark></color> (Shield gained from this effect is removed from the Sinner's total Shield at Attack End of the Warden's "Death Unto the Condemned")\n- Clash Power +2, take -25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Jeżeli Grzesznik posiadający ten efekt <color=#ff6000><mark=#ff000040><b><u>wygrywa Starcie</u></b></mark></color> z Umiejętnością Strażnika <color=#ff6000><mark=#ff000040><b><u>„Śmierć Skazanym”</u></b></mark></color>, zyskuje <color=#ff6000><mark=#ff000040><b><u>Tarczę równą 250% Maks. HP Grzesznika</u></b></mark></color> (po zakończeniu ataku „Śmierć Skazanym” Strażnika odejmuje z Tarczy Grzesznika tyle, ile wynosiła Tarcza z tego efektu)\n- Moc Starcia +2, otrzymuje obrażenia -25%\n- Na koniec tury znika
582. [Status [GoldenHideWarderSecondPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소\n'사형 집행'과 합 승리 시 보호막 얻음
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and take less damage\nOn Clash Win against "Death Unto the Condemned", gain Shield
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń\nPo wygranym Starciu z Umiejętnością „Śmierć Skazanym” zyskuje Tarczę
583. [Status [GoldenHideWarderSecondPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderSecondPhase].flavor
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Status [GoldenFabricWarderSecondPhase] — nazwa] 정지
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenFabricWarderSecondPhase]`
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Status [GoldenFabricWarderSecondPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +2, 가하는 피해량 +25%\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +2, deal +25% damage\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +2, zadaje obrażenia +25%\n- Na koniec tury znika
586. [Status [GoldenFabricWarderSecondPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].summary
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Status [GoldenFabricWarderSecondPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderSecondPhase].flavor
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Status [MeursaultBuffWarderSecondPhase] — nazwa] 이방인
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBuffWarderSecondPhase]`
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Status [MeursaultBuffWarderSecondPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 속도 최솟값, 최댓값 +1\n- 간수와 합 진행 시,\n· 합 위력 +2\n· 피해량 +(자신의 잃은 체력 비율/2)% (최대 40%)\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 2 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Min & Max Speed +1\n- When Clashing against the Warden:\n · Clash Power +2\n · Deal +(missing HP percentage on self / 2)% damage (max 40%)\n · On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 2 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Min. i Maks. Szybkość +1\n- Podczas Starcia ze Strażnikiem:\n· Moc Starcia +2\n· Zadaje obrażenia +(procent utraconego HP na sobie / 2)% (maks. 40%)\n· Po wygranym Starciu zyskuje w sumie 3 Zasoby E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 2 Wzrostu Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
590. [Status [MeursaultBuffWarderSecondPhase] — podsumowanie] 간수와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].summary
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Status [MeursaultBuffWarderSecondPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderSecondPhase].flavor
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Status [EncompassingVoiceSecondPhase] — nazwa] 검은 신의 목소리
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[EncompassingVoiceSecondPhase]`
   limit: do 40 znaków
   EN: Voice of the Obsidian God
   PL: Głos Czarnego Boga
593. [Status [EncompassingVoiceSecondPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 40, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 턴 종료 시, 10 증가\n- 수치가 100이 되면, 다음 턴에 검은 신의 권능으로 변경됨
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up for every 20 Stacks (max 4)\n- Gain Stack equal to Preservation Count this unit consumes or gains due to its Skill effects (max 40 per turn; this effect's Stack is gained regardless of Preservation's max Count)\n- Turn End: Gain 10 Stacks\n- At 100 Stacks, convert this effect into "Divinity of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 20 ładunków (maks. 4)\n- Gdy przez Umiejętności tej jednostki zużyty albo zdobyty zostaje Licznik Zachowania, zyskuje ładunki w tej liczbie (maks. 40 na turę, łącznie z liczbą ponad Maks. licznika Zachowania)\n- Na koniec tury zyskuje 10 ładunków\n- Przy 100 ładunkach w następnej turze zamienia się w „Wszechmoc Czarnego Boga”
594. [Status [EncompassingVoiceSecondPhase] — podsumowanie] 수치에 따라 공격 레벨 증가\n수치가 최대가 되면 검은 신의 권능으로 변경
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level based on Stack\nAt max Stack, converted into "Divinity of the Obsidian God"
   PL: Poziom Ataku rośnie zależnie od ładunków\nPrzy Maks. ładunków zamienia się w „Wszechmoc Czarnego Boga”
595. [Status [EncompassingVoiceSecondPhase] — tekst klimatyczny] 보존의 규율을 설파하는 목소리.\n다시 야만으로 돌아갈 수는 없다.
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceSecondPhase].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A voice preaching the Rule of Conservation.\nThere can be no return to barbarism.
   PL: Głos, który głosi Regułę Zachowania.\nPowrotu do barbarzyństwa nie może być.
596. [Status [EncompassingVoiceThirdPhase] — nazwa] 검은 신의 목소리
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[EncompassingVoiceThirdPhase]`
   (powtórzenie elementu 592 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Status [EncompassingVoiceThirdPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1 얻음 (최대 4)\n- 자신의 스킬 효과로 보존 횟수를 소모하거나 획득하면 그 수치만큼 증가 (턴당 최대 40, 보존 횟수 최대치를 초과하여 얻는 수치 포함)\n- 턴 종료 시, 10 증가\n- 수치가 100이 되면, 다음 턴에 검은 신의 권능으로 변경됨
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].desc
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Status [EncompassingVoiceThirdPhase] — podsumowanie] 수치에 따라 공격 레벨 증가\n수치가 최대가 되면 검은 신의 권능으로 변경
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].summary
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Status [EncompassingVoiceThirdPhase] — tekst klimatyczny] 보존의 규율을 설파하는 목소리.\n다시 야만으로 돌아갈 수는 없다.
   źródło: Bufs-a1c10p3.json :: dataList[id=EncompassingVoiceThirdPhase].flavor
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Status [SpreadingVoiceSecondPhase] — nazwa] 검은 신의 권능
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[SpreadingVoiceSecondPhase]`
   limit: do 40 znaków
   EN: Divinity of the Obsidian God
   PL: Wszechmoc Czarnego Boga
601. [Status [SpreadingVoiceSecondPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 스킬의 코인이 파괴 불가 코인으로 변경됨\n- 수치가 0이 되면, 다음 턴에 검은 신의 목소리로 변경됨
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 respectively)\n- Convert all Skill Coins into Unbreakable Coins\n- At 0 Stacks, convert this effect into "Voice of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Przy 0 ładunkach w następnej turze zamienia się w „Głos Czarnego Boga”
602. [Status [SpreadingVoiceSecondPhase] — podsumowanie] 모든 스킬의 코인이 파괴 불가 코인으로 변경\n수치에 따라 공격 레벨, 방어 레벨 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Convert all Skill Coins into Unbreakable Coins\nGain Offense Level and Defense Level based on Stack
   PL: Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\nPoziom Ataku i Poziom Obrony rosną zależnie od ładunków
603. [Status [SpreadingVoiceSecondPhase] — tekst klimatyczny] 검은 신. 시지프 시스템에서 창조와 시간을 관장한다.
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceSecondPhase].flavor
   limit: do 120 znaków
   EN: The Obsidian God—He whose domain is creation and time itself within the Sisyphe System.
   PL: Czarny Bóg. W Systemie Sisyphe to on zawiaduje tworzeniem i czasem.
604. [Status [SpreadingVoiceThirdPhase] — nazwa] 검은 신의 권능
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[SpreadingVoiceThirdPhase]`
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Status [SpreadingVoiceThirdPhase] — opis] - 최댓값 : 100\n- 턴 시작 시 수치 20당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음 (각각 최대 4)\n- 모든 스킬의 코인이 파괴 불가 코인으로 변경됨 (적출 코인 제외)\n- 수치가 0이 되면, 다음 턴에 검은 신의 목소리로 변경됨
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 20 Stacks (max 4 respectively)\n- Convert all Skill Coins into Unbreakable Coins (excluding Excision Coins)\n- At 0 Stacks, convert this effect into "Voice of the Obsidian God" next turn
   PL: - Maks. ładunków: 100\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 20 ładunków (każdy maks. 4)\n- Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami (z wyłączeniem Monet Wycięcia)\n- Przy 0 ładunkach w następnej turze zamienia się w „Głos Czarnego Boga”
606. [Status [SpreadingVoiceThirdPhase] — podsumowanie] 모든 스킬의 코인이 파괴 불가 코인으로 변경 (적출 코인 제외)\n수치에 따라 공격 레벨, 방어 레벨 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Convert all Skill Coins into Unbreakable Coins (excluding Excision Coins)\nGain Offense Level and Defense Level based on Stack
   PL: Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami (z wyłączeniem Monet Wycięcia)\nPoziom Ataku i Poziom Obrony rosną zależnie od ładunków
607. [Status [SpreadingVoiceThirdPhase] — tekst klimatyczny] 검은 신. 시지프 시스템에서 창조와 시간을 관장한다.
   źródło: Bufs-a1c10p3.json :: dataList[id=SpreadingVoiceThirdPhase].flavor
   (powtórzenie elementu 603 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Status [LeaderVoiceSecondPhase] — nazwa] 시지프 형벌의 간수
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[LeaderVoiceSecondPhase]`
   limit: do 50 znaków
   EN: Warden of the Sisyphe Penalty
   PL: Strażnik Wyroku Sisyphe
609. [Status [LeaderVoiceSecondPhase] — opis] - 최댓값 : 5\n- 수치 1당 공격 레벨 +1, 방어 레벨 +2\n- 수치가 3 이상이면, 스킬로 부여하는 못[형벌], 못[속죄] 부여량 +1
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +1 and Defense Level +2 for every Stack\n- At 3+ Stacks, inflict +1 more "Nail [Punishment]" and "Nail [Penance]" using Skills
   PL: - Maks. ładunków: 5\n- Poziom Ataku +1 i Poziom Obrony +2 za każdy ładunek\n- Przy 3 lub więcej ładunkach Umiejętności nakładają o 1 więcej „Gwóźdź [Kara]” i „Gwóźdź [Pokuta]”
610. [Status [LeaderVoiceSecondPhase] — podsumowanie] 수치에 따라 공격 레벨, 방어 레벨 증가\n수치 3 이상이면 못[형벌], 못[속죄] 부여량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level and Defense Level based on Stack\nAt 3+ Stack, inflict more "Nail [Punishment]" and "Nail [Penance]"
   PL: Poziom Ataku i Poziom Obrony rosną zależnie od ładunków\nPrzy 3 lub więcej ładunkach nakłada więcej „Gwóźdź [Kara]” i „Gwóźdź [Pokuta]”
611. [Status [LeaderVoiceSecondPhase] — tekst klimatyczny] 뜻대로 행동하지 않는 자들에게 간수가 나타난다. 이것은 시스템이기 때문이다.
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceSecondPhase].flavor
   limit: do 130 znaków
   EN: The Warden appears before those who refuse to act as intended. For that is how the system works.
   PL: Strażnik stawia się przed tymi, którzy nie działają według woli systemu. Bo tak działa system.
612. [Status [ConfessionSecondPhase] — nazwa] 고해의 증거
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[ConfessionSecondPhase]`
   limit: do 40 znaków
   EN: Proof of Confession
   PL: Dowód Spowiedzi
613. [Status [ConfessionSecondPhase] — opis] - 다음 효과를 아울러 고해의 증거로 지칭함\n· 망치 못[단죄]\n· 망치 못[심판]\n· 못[형벌]\n· 못[속죄]
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionSecondPhase].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The following effects are collectively referred to as "Proof of Confession":\n · Hammernail [Condemnation]\n · Hammernail [Judgment]\n · Nail [Punishment]\n · Nail [Penance]
   PL: - Następujące efekty są zbiorczo nazywane „Dowodem Spowiedzi”:\n· Młotogwóźdź [Potępienie]\n· Młotogwóźdź [Sąd]\n· Gwóźdź [Kara]\n· Gwóźdź [Pokuta]
614. [Status [ConfessionSecondPhase] — podsumowanie] 간수가 부여하는 못과 망치 못을 아울러 지칭
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionSecondPhase].summary
   limit: do 120 znaków
   EN: Collectively refers to "Nails" and "Hammernails" the Warden inflicts
   PL: Zbiorcza nazwa Gwóździ i Młotogwoździ nakładanych przez Strażnika
615. [Status [ConfessionSecondPhase] — tekst klimatyczny] 업보만큼 못을 박아, 속죄하였음을 증명하라.
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionSecondPhase].flavor
   limit: do 120 znaków
   EN: Drive in as many nails as thy sins demand, and prove thy repentance.
   PL: Wbijaj tyle gwoździ, ile grzechów — niech służy to za dowód pokuty.
616. [Status [LeaderVoiceThirdPhase] — nazwa] 시지프 형벌의 신부
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[LeaderVoiceThirdPhase]`
   limit: do 50 znaków
   EN: Chaplain of the Sisyphe Penalty
   PL: Kapłan Wyroku Sisyphe
617. [Status [LeaderVoiceThirdPhase] — opis] - 최댓값 : 5\n- 수치 1당 공격 레벨 +2, 방어 레벨 +3\n- 수치가 3 이상이면, 스킬로 부여하는 못[Console] 부여량 +1
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Offense Level +2 and Defense Level +3 for every Stack\n- At 3+ Stacks, inflict +1 more "Nail [Console]" using Skills
   PL: - Maks. ładunków: 5\n- Poziom Ataku +2 i Poziom Obrony +3 za każdy ładunek\n- Przy 3 lub więcej ładunkach Umiejętności nakładają o 1 więcej „Gwóźdź [Console]”
618. [Status [LeaderVoiceThirdPhase] — podsumowanie] 수치에 따라 공격 레벨, 방어 레벨 증가\n수치 3 이상이면 못[Console] 부여량 증가
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level and Defense Level based on Stack\nAt 3+ Stack, inflict more "Nail [Console]"
   PL: Poziom Ataku i Poziom Obrony rosną zależnie od ładunków\nPrzy 3 lub więcej ładunkach nakłada więcej „Gwóźdź [Console]”
619. [Status [LeaderVoiceThirdPhase] — tekst klimatyczny] 뜻대로 행동하지 않는 자들에게 신부가 나타난다. 이것은 시스템이기 때문이다.
   źródło: Bufs-a1c10p3.json :: dataList[id=LeaderVoiceThirdPhase].flavor
   limit: do 130 znaków
   EN: The Chaplain appears before those who refuse to act as intended. For that is how the system works.
   PL: Kapłan stawia się przed tymi, którzy nie działają według woli systemu. Bo tak działa system.
620. [Status [ConfessionThirdPhase] — nazwa] 〜
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[ConfessionThirdPhase]`
   limit: do 40 znaków
   EN: 〜
   PL: 〜
621. [Status [ConfessionThirdPhase] — opis] - 다음 효과를 아울러 〜로 지칭함\n· 못[Exception]\n· 못[Breakpoint]\n· 못[Console]
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionThirdPhase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The following effects are collectively referred to as "〜":\n· Nail [Exception]\n· Nail [Breakpoint]\n· Nail [Console]
   PL: - Następujące efekty są zbiorczo nazywane „〜”:\n· Gwóźdź [Exception]\n· Gwóźdź [Breakpoint]\n· Gwóźdź [Console]
622. [Status [ConfessionThirdPhase] — podsumowanie] 신부가 부여하는 못을 아울러 지칭
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionThirdPhase].summary
   limit: do 120 znaków
   EN: Collectively refers to "Nails" the Chaplain inflicts
   PL: Zbiorcza nazwa Gwóździ nakładanych przez Kapłana
623. [Status [ConfessionThirdPhase] — tekst klimatyczny] “너희가 이 시스템에 있으면 안 될 이물질이라는 걸 확실히 알겠군. 그러니까… 이제라도 매뉴얼을 봐야겠어. 규율과 규칙에는 없는 게 없거든.”
   źródło: Bufs-a1c10p3.json :: dataList[id=ConfessionThirdPhase].flavor
   limit: do 250 znaków
   EN: "Now I'm sure of it. You're all foreign elements that shouldn't be allowed into this system. I guess it's time I actually checked the manual. There's nothing the laws and rules don't account for."
   PL: „Więc na pewno jesteś obcym ciałem, które nie powinno istnieć w tym systemie. W takim razie... najwyższy czas zajrzeć w instrukcję. W przepisach i zasadach nie ma niczego, czego by nie uwzględniono.”
624. [Status [ExecutionNailSecondPhase] — nazwa] 망치 못[심판]
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[ExecutionNailSecondPhase]`
   limit: do 40 znaków
   EN: Hammernail [Judgment]
   PL: Młotogwóźdź [Sąd]
625. [Status [ExecutionNailSecondPhase] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 (수치 x 5)%만큼 고정 피해</u></b></mark></color>를 입음 (최소 10)\n· 전투 시작 시 수비 스킬을 장착하였다면, 받는 피해가 절반으로 줄어들고 이 효과로 사망하거나 흐트러지지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to (Stack x 5%) of max HP</u></b></mark></color> (min 10)\n · Combat Start: If this unit has equipped a Defense Skill, halve damage taken and this unit cannot be killed or Staggered by this effect
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe (ładunki x 5)% Maks. HP</u></b></mark></color> (min. 10)\n· Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymywane obrażenia maleją o połowę i ten efekt nie pozbawia życia ani nie oszołamia
626. [Status [ExecutionNailSecondPhase] — podsumowanie] 발동 시 고정 피해 입음\n수비 스킬 장착 시 피해 절반, 사망하지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activated, take fixed damage\nWhen Defense Skill is equipped, halve damage taken and this unit cannot be killed
   PL: Po wywołaniu otrzymuje obrażenia stałe\nZ wyposażonymi Umiejętnościami obrony otrzymuje połowę obrażeń i nie ginie
627. [Status [ExecutionNailSecondPhase] — tekst klimatyczny] 이는 못이되, 못이 아니요, 심판을 선고하는 망치일지니라.
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailSecondPhase].flavor
   limit: do 120 znaków
   EN: For this is a nail, yet no nail. 'Tis a hammer that pronounceth judgment.
   PL: Jest gwoździem, a nie gwoździem — młotem, który ogłasza sąd.
628. [Status [RestrainingNailSecondPhase] — nazwa] 망치 못[단죄]
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].name
   kontekst: identyfikator statusu w tekstach: `[RestrainingNailSecondPhase]`
   limit: do 40 znaków
   EN: Hammernail [Condemnation]
   PL: Młotogwóźdź [Potępienie]
629. [Status [RestrainingNailSecondPhase] — opis] - 최댓값 : 9\n- 턴 시작 시 이 효과가 있으면, <color=#ff6000><mark=#ff000040><b><u>흐트러짐</u></b></mark></color> 상태로 변경됨\n· 이 효과가 발동했으면, 턴 종료 시 사라짐\n· 박동을 보유했으면, 이 효과로 흐트러지지 않고 해당 턴 종료 시 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Turn Start: If this unit has this effect, become <color=#ff6000><mark=#ff000040><b><u>Staggered</u></b></mark></color>\n · Turn End: This effect expires if triggered this turn\n · If this unit has "Thumping Pulse", it cannot be Staggered via this effect, and this effect expires at Turn End
   PL: - Maks. ładunków: 9\n- Na początku tury, jeżeli jednostka posiada ten efekt, zmienia się w stan <color=#ff6000><mark=#ff000040><b><u>Oszołomienia</u></b></mark></color>\n· Po wywołaniu tego efektu znika na koniec tury\n· Jeżeli posiada Tętnienie, nie zostaje nim oszołomiony i znika na koniec tej tury
630. [Status [RestrainingNailSecondPhase] — podsumowanie] 턴 시작 시 흐트러짐 상태로 변경\n박동 보유 시 흐트러지지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Become Staggered\nIf this unit has "Thumping Pulse", does not become Staggered
   PL: Na początku tury zmienia się w stan Oszołomienia\nPosiadając Tętnienie, nie zostaje oszołomiony
631. [Status [RestrainingNailSecondPhase] — tekst klimatyczny] 네가 뽑아내지 못한 못마다 네 업보의 증거가 되리니, 심판의 날이 도래하여 뽑히지 아니한 못들이 네 몸과 마음에 더욱 깊숙이 박히리라.
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailSecondPhase].flavor
   limit: do 250 znaków
   EN: Each nail thou hast failed to draw forth shall stand as witness to thy sins; and when the Day of Judgment cometh, every nail left within thee shall be driven deeper still into thy flesh and soul.
   PL: Każdy gwóźdź, którego nie wydobyłeś, będzie dowodem twoich grzechów; gdy nadejdzie Dzień Sądu, każdy nie wydobyty gwóźdź wbije się jeszcze głębiej w twe ciało i duszę.
632. [Status [CeremonialNail] — nazwa] 못[형벌]
   źródło: Bufs-a1c10p3.json :: dataList[id=CeremonialNail].name
   kontekst: identyfikator statusu w tekstach: `[CeremonialNail]`
   limit: do 40 znaków
   EN: Nail [Punishment]
   PL: Gwóźdź [Kara]
633. [Status [CeremonialNail] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, 수치만큼 침잠 얻음
   źródło: Bufs-a1c10p3.json :: dataList[id=CeremonialNail].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", gain Sinking equal to Stack
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, zyskuje Zatonięcie równe liczbie ładunków
634. [Status [CeremonialNail] — podsumowanie] 발동 시 침잠 얻음
   źródło: Bufs-a1c10p3.json :: dataList[id=CeremonialNail].summary
   limit: do 120 znaków
   EN: When activated, gain Sinking
   PL: Po wywołaniu zyskuje Zatonięcie
635. [Status [CeremonialNail] — tekst klimatyczny] 형벌은 규율과 규범을 어긴 자의 도덕적 가책이라.
   źródło: Bufs-a1c10p3.json :: dataList[id=CeremonialNail].flavor
   limit: do 120 znaków
   EN: For punishment is the pang of conscience borne by those who transgress rule and ordinance.
   PL: Kara jest — mówię — moralnym wyrzutem sumienia tych, którzy przekroczyli regułę i normę.
636. [Status [MarkingNail] — nazwa] 못[속죄]
   źródło: Bufs-a1c10p3.json :: dataList[id=MarkingNail].name
   kontekst: identyfikator statusu w tekstach: `[MarkingNail]`
   limit: do 40 znaków
   EN: Nail [Penance]
   PL: Gwóźdź [Pokuta]
637. [Status [MarkingNail] — opis] - 최댓값 : 9\n- ‘심판…! 선고…! 단죄…!’로 인하여 이 효과가 발동될 때, (수치 x 2)만큼 흐트러짐 손상
   źródło: Bufs-a1c10p3.json :: dataList[id=MarkingNail].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Judgment... Sentencing... Condemnation!", raise Stagger Threshold by (Stack x 2)
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Sąd...! Wyrok...! Potępienie...!”, podnosi Próg Oszołomienia o (ładunki x 2)
638. [Status [MarkingNail] — podsumowanie] 발동 시 흐트러짐 손상
   źródło: Bufs-a1c10p3.json :: dataList[id=MarkingNail].summary
   limit: do 120 znaków
   EN: When activated raise Stagger Threshold
   PL: Po wywołaniu podnosi Próg Oszołomienia
639. [Status [MarkingNail] — tekst klimatyczny] 속죄하지 않은 자의 가슴에 박히는 못.
   źródło: Bufs-a1c10p3.json :: dataList[id=MarkingNail].flavor
   limit: do 120 znaków
   EN: This is a nail driven into the hearts of the impenitent.
   PL: To gwóźdź wbity w serca tych, którzy nie pokutowali.
640. [Status [GoldenHideWarderThirdPhase] — nazwa] 박동
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenHideWarderThirdPhase]`
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Status [GoldenHideWarderThirdPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 이 효과를 보유한 수감자가 신부의 <color=#ff6000><mark=#ff000040><b><u>‘강제 퇴장’</u></b></mark></color> 스킬과 <color=#ff6000><mark=#ff000040><b><u>합하여 승리</u></b></mark></color>했으면, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 250%만큼 보호막</u></b></mark></color> 얻음 (신부의 ‘강제 퇴장’ 공격 종료 시, 이 효과로 얻은 보호막 수치만큼 수감자가 보유한 보호막에서 차감함)\n- 합 위력 +3, 받는 피해량 -50%\n- 적중 시, 공격 레벨 감소 1 부여 (최대 9)\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Turn Start: A random Sinner gains this effect\n- On Clash Win, if the Sinner who has this effect <color=#ff6000><mark=#ff000040><b><u>won the Clash</u></b></mark></color> against the Chaplain's <color=#ff6000><mark=#ff000040><b><u>"Systemwide Ban"</u></b></mark></color> Skill, gain <color=#ff6000><mark=#ff000040><b><u>Shield equal to 250% of the Sinner's max HP</u></b></mark></color> (Shield gained from this effect is removed from the Sinner's total Shield at Attack End of the Chaplain's "Systemwide Ban")\n- Clash Power +3, take -50% damage\n- On Hit, inflict 1 Offense Level Down (max 9)\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Jeżeli Grzesznik posiadający ten efekt <color=#ff6000><mark=#ff000040><b><u>wygrywa Starcie</u></b></mark></color> z Umiejętnością Kapłana <color=#ff6000><mark=#ff000040><b><u>„Przymusowe Wygnanie”</u></b></mark></color>, zyskuje <color=#ff6000><mark=#ff000040><b><u>Tarczę równą 250% Maks. HP Grzesznika</u></b></mark></color> (po zakończeniu ataku „Przymusowe Wygnanie” Kapłana odejmuje z Tarczy Grzesznika tyle, ile wynosiła Tarcza z tego efektu)\n- Moc Starcia +3, otrzymuje obrażenia -50%\n- Przy trafieniu nakłada 1 Spadku Poziomu Ataku (maks. 9)\n- Na koniec tury znika
642. [Status [GoldenHideWarderThirdPhase] — podsumowanie] 합 위력 증가, 받는 피해량 감소\n'강제 퇴장'과 합 승리 시 보호막 얻음
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and take less damage\nOn Clash Win against "Systemwide Ban", gain Shield
   PL: Moc Starcia rośnie, otrzymuje mniej obrażeń\nPo wygranym Starciu z Umiejętnością „Przymusowe Wygnanie” zyskuje Tarczę
643. [Status [GoldenHideWarderThirdPhase] — tekst klimatyczny] 생의 권능. 변화와 탄생의 의지.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenHideWarderThirdPhase].flavor
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Status [GoldenFabricWarderThirdPhase] — nazwa] 정지
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[GoldenFabricWarderThirdPhase]`
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Status [GoldenFabricWarderThirdPhase] — opis] - 턴 시작 시, 무작위 수감자가 이 효과 얻음\n- 최종 위력 +2, 가하는 피해량 +25%\n- 적중 시, 방어 레벨 감소 1 부여 (최대 9)\n- 턴 종료 시, 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: A random Sinner gains this effect\n- Final Power +2, deal +25% damage\n- On Hit, inflict 1 Defense Level Down (max 9)\n- Turn End: This effect expires
   PL: - Na początku tury losowy Grzesznik zyskuje ten efekt\n- Moc Końcowa +2, zadaje obrażenia +25%\n- Przy trafieniu nakłada 1 Spadku Poziomu Obrony (maks. 9)\n- Na koniec tury znika
646. [Status [GoldenFabricWarderThirdPhase] — podsumowanie] 최종 위력, 가하는 피해량 증가\n적중 시 방어 레벨 감소 부여
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Final Power and deal more damage\nOn Hit, inflict Defense Level Down
   PL: Moc Końcowa rośnie, zadaje więcej obrażeń\nPrzy trafieniu nakłada Spadek Poziomu Obrony
647. [Status [GoldenFabricWarderThirdPhase] — tekst klimatyczny] 죽음의 권능. 보존과 정지의 충동.
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenFabricWarderThirdPhase].flavor
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Status [MeursaultBuffWarderThirdPhase] — nazwa] 이방인
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBuffWarderThirdPhase]`
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Status [MeursaultBuffWarderThirdPhase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 뫼르소의 체력이 1 미만으로 내려가지 않음\n- 속도 최솟값, 최댓값 +3\n- 최종 위력 +3, 피해량 +30%\n- 신부와 합 진행 시,\n· 피해량 +(자신의 잃은 체력 비율)% (최대 90%)\n· 합 승리 시, 정신력 8 회복\n· 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 5개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 3 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Meursault's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Min & Max Speed +3\n- Final Power +3 and deal +30% damage\n- When Clashing against the Chaplain:\n · Deal +(missing HP percentage on self)% damage (max 90%)\n · On Clash Win, heal 8 SP\n · On Clash Win, gain 1 E.G.O resource for each of the 5 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 3 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Jeżeli w tej walce przeżywa co najmniej 1 inny sojusznik, HP Meursaulta nie spada poniżej 1\n- Min. i Maks. Szybkość +3\n- Moc Końcowa +3, zadaje obrażenia +30%\n- Podczas Starcia z Kapłanem:\n· Zadaje obrażenia +(procent utraconego HP na sobie)% (maks. 90%)\n· Po wygranym Starciu odzyskuje 8 Poczytalności\n· Po wygranym Starciu zyskuje w sumie 5 Zasobów E.G.O — po 1 Zasobie losowego Grzechu spośród najmniej posiadanych\n- Przy otrzymaniu obrażeń, które oszołomiłyby go, nie zostaje oszołomiony i usuwa dany Próg Oszołomienia; następnie w następnej turze zyskuje 3 Wzrostu Mocy Ataku (bez limitu na walkę)\n- Nie może się wycofać
650. [Status [MeursaultBuffWarderThirdPhase] — podsumowanie] 신부와 합 진행 시 합 위력, 피해량 증가\n흐트러지지 않고, 다른 아군 생존 시 사망하지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power and deal more damage when Clashing with the Chaplain\nCannot be Staggered, cannot be defeated when there are other surviving allies
   PL: - Podczas Starcia z Kapłanem Moc Starcia i obrażenia rosną\n- Nie zostaje oszołomiony; gdy żyją inni sojusznicy, nie ginie
651. [Status [MeursaultBuffWarderThirdPhase] — tekst klimatyczny] 백화점에서도, 도시에서도, 나는 이질적이었으며 이물질이었는가.
   źródło: Bufs-a1c10p3.json :: dataList[id=MeursaultBuffWarderThirdPhase].flavor
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Status [GoldenNail] — nazwa] 못[Console]
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenNail].name
   kontekst: identyfikator statusu w tekstach: `[GoldenNail]`
   limit: do 40 znaków
   EN: Nail [Console]
   PL: Gwóźdź [Console]
653. [Status [GoldenNail] — opis] - 최댓값 : 9\n- 전투 시작 시 <color=#ff6000><mark=#ff000040><b><u>수치가 9</u></b></mark></color>이면, 이번 턴 동안 이 효과를 보유한 수감자가 신부에게 <color=#ff6000><mark=#ff000040><b><u>공격 적중 시 자신의 최대 체력 2%만큼 고정 체력 피해</u></b></mark></color>를 입음 (이 효과로 흐트러지지 않음)\n- ‘시지프 시스템을 진짜 망가트리려고?’로 인하여 이 효과가 발동될 때, 수치만큼 침잠 얻고 (수치 x 2)만큼 흐트러짐 손상
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenNail].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Combat Start: <color=#ff6000><mark=#ff000040><b><u>At 9 Stacks, On Hit against the Chaplain</u></b></mark></color>, the Sinner who has this effect for this turn <color=#ff6000><mark=#ff000040><b><u>takes fixed damage equal to 2% of max HP</u></b></mark></color> (this effect cannot Stagger this unit)\n- If this effect is triggered by "Do you seriously mean to break the Sisyphe System?", gain Sinking equal to Stack and raise Stagger Threshold by (Stack x 2)
   PL: - Maks. ładunków: 9\n- Na początku walki przy <color=#ff6000><mark=#ff000040><b><u>9 ładunkach</u></b></mark></color> Grzesznik posiadający ten efekt w tej turze <color=#ff6000><mark=#ff000040><b><u>otrzymuje przy trafieniu atakiem w Kapłana obrażenia HP stałe równe 2% Maks. HP</u></b></mark></color> (ten efekt nie oszołamia)\n- Gdy ten efekt zostaje wywołany przez „Czy naprawdę próbujesz zepsuć System Sisyphe?”, zyskuje Zatonięcie równe liczbie ładunków i podnosi Próg Oszołomienia o (ładunki x 2)
654. [Status [GoldenNail] — podsumowanie] 발동 시 침잠 얻음, 흐트러짐 손상\n최대 수치면 공격 적중 시 고정 피해 입음
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenNail].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activated, gain Sinking and raise Stagger Threshold\nAt max Stack, take fixed damage when hit
   PL: Po wywołaniu zyskuje Zatonięcie i podnosi Próg Oszołomienia\nPrzy Maks. ładunków otrzymuje obrażenia stałe przy trafieniu
655. [Status [GoldenNail] — tekst klimatyczny] “어디 보자, 이 못에 대한 매뉴얼이… ‘당신은 죄악이 등을 타고…’ 음, 이건 아니고,”\n\n“여기 이쪽 42번째 서랍에… 있었는데… 아, 여기 있었군! ‘르누아르를 담당하는 시지프 시스템 관리자를 위한 콘솔 매뉴얼’.”
   źródło: Bufs-a1c10p3.json :: dataList[id=GoldenNail].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Let's see, the manual for this nail... 'You feel your sins crawling on your back...' Mm, no, not this one."\n\n"It should be in Drawer 42 over here... I know I put it... ah, there it is! 'Le Noir Administrator's Guide to the Sisyphe System Console Commands'."
   PL: „Zobaczmy, instrukcja dla tego gwoźdźia... 'Czujesz, jak grzechy wpełzają ci po plecach...' Mmm, nie, to nie to.”\n\n„Powinna być w czterdziestym drugim szufladzie... wkładałem tam... o, proszę! 'Instrukcja konsoli dla administratora Systemu Sisyphe odpowiadającego za Le Noir'.”
656. [Status [VibrationFocusing] — nazwa] 진동 - 보존
   źródło: Bufs-a1c10p3.json :: dataList[id=VibrationFocusing].name
   kontekst: identyfikator statusu w tekstach: `[VibrationFocusing]`
   limit: do 40 znaków
   EN: Tremor - Conservation
   PL: Wstrząs - Zachowanie
657. [Status [VibrationFocusing] — opis] - 진동 폭발 시 진동 위력의 (60 + 공격자의 충전 위력 또는 특수 충전 x 8)%만큼\n나태 피해를 입고 횟수 1 감소 (최대 120%)\n· 르누아르 소속 캐릭터의 스킬, 패시브 효과로 진동 폭발 시 이 효과로 횟수가 감소하지 않음\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs-a1c10p3.json :: dataList[id=VibrationFocusing].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Sloth Damage equal to (60 + sum of Charge Potency or Unique Charge on the attacker x 8)% of Tremor Potency, and reduce the Count by 1 (max 120%)\n · When "Le Noir" units' Skills and Passives trigger Tremor Burst, the above effect does not reduce the Count\n- When hit by Tremor Burst Skills, raise Stagger Threshold by this effect's Potency\n- Turn End: Lose 1 Count\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Lenistwa równe (60 + suma Siły Ładunku lub Specjalnego Ładunku atakującego x 8)% Siły Wstrząsu\ni traci 1 Licznika (maks. 120%)\n· Gdy Wyładowanie Wstrząsu wywołują Umiejętności lub umiejętności pasywne jednostek z Le Noir, ten efekt nie zmniejsza Licznika\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Na koniec tury traci 1 Licznika\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Siłę i Licznik Wstrząsu)
658. [Status [VibrationFocusing] — podsumowanie] 진동 폭발 시 나태 피해 입음\n진동 폭발 스킬로 피격 시 흐트러짐 손상
   źródło: Bufs-a1c10p3.json :: dataList[id=VibrationFocusing].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Tremor Burst, take Sloth Damage\nWhen hit by Skills that trigger Tremor Burst, raise Stagger Threshold
   PL: Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Lenistwa\nPrzy trafieniu Umiejętnościami z Wyładowaniem Wstrząsu podnosi Próg Oszołomienia
659. [Status [ExecutionNailThirdPhase] — nazwa] 못[Breakpoint]
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[ExecutionNailThirdPhase]`
   limit: do 40 znaków
   EN: Nail [Breakpoint]
   PL: Gwóźdź [Breakpoint]
660. [Status [ExecutionNailThirdPhase] — opis] - 최댓값 : 9\n- '시지프 시스템을 진짜 망가트리려고?'로 인하여 이 효과가 발동될 때, <color=#ff6000><mark=#ff000040><b><u>최대 체력의 (수치 x 10)%만큼 고정 피해</u></b></mark></color>를 입음 (최소 10)\n· 전투 시작 시 수비 스킬을 장착하였다면, 받는 피해가 절반으로 줄어들고 이 효과로 사망하거나 흐트러지지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- If this effect is triggered by "Do you seriously mean to break the Sisyphe System?", <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to (Stack x 10%) of max HP</u></b></mark></color> (min 10)\n · Combat Start: If this unit has equipped a Defense Skill, halve damage taken and this unit cannot be killed or Staggered by this effect
   PL: - Maks. ładunków: 9\n- Gdy ten efekt zostaje wywołany przez „Czy naprawdę próbujesz zepsuć System Sisyphe?”, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe (ładunki x 10)% Maks. HP</u></b></mark></color> (min. 10)\n· Na początku walki, jeżeli wyposażono Umiejętności obrony, otrzymywane obrażenia maleją o połowę i ten efekt nie pozbawia życia ani nie oszołamia
661. [Status [ExecutionNailThirdPhase] — podsumowanie] 발동 시 고정 피해 입음\n수비 스킬 장착 시 피해 절반, 사망하지 않음
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].summary
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Status [ExecutionNailThirdPhase] — tekst klimatyczny] “관리 매뉴얼에 써 있더라고. 시스템 안에서 이 명령어에 못 박히면, 아무것도 못 한다고.”
   źródło: Bufs-a1c10p3.json :: dataList[id=ExecutionNailThirdPhase].flavor
   limit: do 150 znaków
   EN: "The admin manual says it plain enough. Once this command nails you down inside the system, you can't do a thing."
   PL: „W instrukcji administratora pisali to wprost. Kiedy ta komenda przybija cię w systemie, nie zrobisz już niczego.”
663. [Status [RestrainingNailThirdPhase] — nazwa] 못[Exception]
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].name
   kontekst: identyfikator statusu w tekstach: `[RestrainingNailThirdPhase]`
   limit: do 40 znaków
   EN: Nail [Exception]
   PL: Gwóźdź [Exception]
664. [Status [RestrainingNailThirdPhase] — opis] - 최댓값 : 9\n- 턴 시작 시 이 효과가 있으면, <color=#ff6000><mark=#ff000040><b><u>현재 체력의 50%만큼 고정 피해</u></b></mark></color>를 입고 <color=#ff6000><mark=#ff000040><b><u>흐트러짐</u></b></mark></color> 상태로 변경됨\n· 이 효과가 발동했으면, 턴 종료 시 사라짐\n· 박동을 보유했으면, 이 효과로 흐트러지지 않고 받는 피해가 절반으로 줄어들며, 해당 턴 종료 시 사라짐
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n
   EN: - Max Stack: 9\n- Turn Start: If this unit has this effect, <color=#ff6000><mark=#ff000040><b><u>take fixed damage equal to 50% current HP</u></b></mark></color> and become <color=#ff6000><mark=#ff000040><b><u>Staggered</u></b></mark></color>\n · Turn End: This effect expires if triggered this turn\n · If this unit has "Thumping Pulse", it cannot be Staggered via this effect, halve damage taken, and this effect expires at Turn End
   PL: - Maks. ładunków: 9\n- Na początku tury, jeżeli jednostka posiada ten efekt, <color=#ff6000><mark=#ff000040><b><u>otrzymuje obrażenia stałe równe 50% obecnego HP</u></b></mark></color> i zmienia się w stan <color=#ff6000><mark=#ff000040><b><u>Oszołomienia</u></b></mark></color>\n· Po wywołaniu tego efektu znika na koniec tury\n· Jeżeli posiada Tętnienie, nie zostaje nim oszołomiony, otrzymywane obrażenia maleją o połowę, a efekt znika na koniec tej tury
665. [Status [RestrainingNailThirdPhase] — podsumowanie] 턴 시작 시 고정 피해 입고 흐트러짐 상태로 변경\n박동 보유 시 흐트러지지 않고 피해 절반
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].summary
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Take fixed damage and become Staggered\nIf this unit has "Thumping Pulse", does not become Staggered and take only half damage
   PL: Na początku tury otrzymuje obrażenia stałe i zmienia się w stan Oszołomienia\nPosiadając Tętnienie, nie zostaje oszołomiony i otrzymuje tylko połowę obrażeń
666. [Status [RestrainingNailThirdPhase] — tekst klimatyczny] “예외적인 모든 것들도, 이 못에는 걸릴 수밖에 없지.”
   źródło: Bufs-a1c10p3.json :: dataList[id=RestrainingNailThirdPhase].flavor
   limit: do 120 znaków
   EN: "Even the exceptions can't help but get caught on this nail."
   PL: „Nawet wyjątki nie potrafią uchronić się przed tym gwoździem.”
667. [Status [ConnectionError_LowMorale] — nazwa] 싱크 오류
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[ConnectionError_LowMorale]`
   limit: do 40 znaków
   EN: Sync Error
   PL: Błąd Synchronizacji
668. [Status [ConnectionError_LowMorale] — opis] - 사기 저하\n- 받는 피해량 +12.5%\n- 속도 최솟값, 최댓값 -1\n- 보존을 소모하는 스킬의 피해량 -15%
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +12.5% damage\n- Min & Max Speed -1\n- Deal -15% damage using Skills that consume Preservation
   PL: - Niskie Morale\n- Otrzymuje obrażenia +12,5%\n- Min. i Maks. Szybkość -1\n- Umiejętności zużywające Zachowanie zadają obrażenia -15%
669. [Status [ConnectionError_LowMorale] — podsumowanie] 속도 최솟값, 최댓값 감소, 받는 피해량 증가\n보존을 소모하는 스킬의 피해량 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_LowMorale].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose Min & Max Speed, take more damage\nSkills that consume Preservation deal less damage
   PL: Traci Min. i Maks. Szybkość, otrzymuje więcej obrażeń\nUmiejętności zużywające Zachowanie zadają mniej obrażeń
670. [Status [ConnectionError_Panic] — nazwa] 싱크 오류
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_Panic].name
   kontekst: identyfikator statusu w tekstach: `[ConnectionError_Panic]`
   (powtórzenie elementu 667 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Status [ConnectionError_Panic] — opis] - 패닉\n- 받는 피해량 +20%\n- 속도 최솟값, 최댓값 -2\n- 보존을 소모하는 스킬의 피해량 -25%
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +20% damage\n- Min & Max Speed -2\n- Deal -25% damage using Skills that consume Preservation
   PL: - Panika\n- Otrzymuje obrażenia +20%\n- Min. i Maks. Szybkość -2\n- Umiejętności zużywające Zachowanie zadają obrażenia -25%
672. [Status [ConnectionError_Panic] — podsumowanie] 속도 최솟값, 최댓값 감소, 받는 피해량 증가\n보존을 소모하는 스킬의 피해량 감소
   źródło: Bufs-a1c10p3.json :: dataList[id=ConnectionError_Panic].summary
   (powtórzenie elementu 669 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Status [JeanneDesign] — nazwa] 못 박힘
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneDesign].name
   kontekst: identyfikator statusu w tekstach: `[JeanneDesign]`
   limit: do 40 znaków
   EN: Nailed
   PL: Przybity
674. [Status [JeanneDesign] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>코인 앞면 확률 95% 고정</color></mark></b></u>\n- 2이면, 자신과 합 하는 <color=#ff6000><mark color=#ff000040><b><u>대상의 합 위력 -2</color></mark></b></u>\n- 3이면, 전부 소모하여 다음 턴에 <color=#ff6000><mark color=#ff000040><b><u>앙가즈망(engagement)</color></mark></b></u>을 얻음\n- 턴 종료시 1 감소 (해당 효과를 얻은 턴에는 감소하지 않음)\n- 앙가즈망(engagement)이 있을 경우, 획득할 수 없음
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneDesign].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>This unit has 95% chance to flip Heads</color></mark></b></u>\n- At 2 Stacks, <color=#ff6000><mark color=#ff000040><b><u>Clash Power -2 for targets</color></mark></b></u> Clashing with this unit\n- At 3 Stacks, consume all Stacks and gain <color=#ff6000><mark color=#ff000040><b><u>Engagement</color></mark></b></u> next turn\n- Turn End: Lose 1 Stack (does not lose Stack in the turn this effect is gained)\n- Cannot gain this effect if this unit has Engagement
   PL: - Maks. ładunków: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Szanse na Awers Monet zamrożone na 95%</u></b></mark></color>\n- Przy 2 ładunkach Moc Starcia celów, którzy prowadzą z nim Starcie, wynosi <color=#ff6000><mark color=#ff000040><b><u>-2</u></b></mark></color>\n- Przy 3 ładunkach zużywa je wszystkie, a w następnej turze zyskuje <color=#ff6000><mark color=#ff000040><b><u>Engagement</u></b></mark></color>\n- Na koniec tury traci 1 ładunek (w turze zdobycia tego efektu nie traci)\n- Jeżeli jednostka posiada Engagement, nie może zdobyć tego efektu
675. [Status [JeanneDesign] — tekst klimatyczny] 실존은 본질에 앞선다.
   źródło: Bufs-a1c10p3.json :: dataList[id=JeanneDesign].flavor
   limit: do 120 znaków
   EN: Existence precedes essence.
   PL: Egzystencja poprzedza esencję.
