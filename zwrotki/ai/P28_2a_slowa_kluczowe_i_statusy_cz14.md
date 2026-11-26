# Paczka AI P28 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 14/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P28_2a_slowa_kluczowe_i_statusy_cz14.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P28_2a_slowa_kluczowe_i_statusy_cz14.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs
- plik gry: `Bufs.json`

1. [Status [MiddleFingerTattooID] — opis] - 최댓값 : 20\n- 수치 1당 자신의 기본 스킬 피해량 +1%
   źródło: Bufs.json :: dataList[id=MiddleFingerTattooID].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Base Skills deal +1% damage for every Stack
   PL: - Maks.: 20\n- Bazowe Umiejętności zadają +1% obrażeń za każdą wartość
2. [Status [ScarletMothRodion] — nazwa] 주홍 나방
   źródło: Bufs.json :: dataList[id=ScarletMothRodion].name
   kontekst: identyfikator statusu w tekstach: `[ScarletMothRodion]`
   limit: do 40 znaków
   EN: Scarlet Moth
   PL: Cynobrowa Ćma
3. [Status [ScarletMothRodion] — opis] - 최댓값: 3\n- 턴 종료시 최대 체력의 수치% 만큼 체력 회복 (최소 체력 회복량: 1)\n- 턴 종료시 정신력을 수치만큼 회복\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=ScarletMothRodion].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: Heal (Stack)% HP (minimum HP healed: 1)\n- Turn End: Heal SP equal to Stack\n- Turn End: Lose 1 Stack
   PL: - Maks.: 3\n- Na koniec tury regeneruje HP równe wartości% maks. HP (min. 1)\n- Na koniec tury regeneruje Poczytalność równą wartości\n- Na koniec tury maleje o 1
4. [Status [SojiRyoshuEchoPast] — nazwa] 얽힘
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoPast].name
   kontekst: identyfikator statusu w tekstach: `[SojiRyoshuEchoPast]`
   limit: do 40 znaków
   EN: Entanglement
   PL: Splot
5. [Status [SojiRyoshuEchoPast] — opis] - 최댓값 : {0} ({1} 증가)
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoPast].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: - Max Stack: {0} ({1} gained)
   PL: - Maks. stosów: {0} (zyskano {1})
6. [Status [SojiRyoshuEchoPast] — tekst klimatyczny] 누군가와 만나 시간을 얼마나 보냈는지에 따라 인연이 얽힌다.\n너의 시간과 나의 시간이 겹쳐졌던 그 순간들이 좋았든 끔찍했든, 인연은 잔인하리만치 얽혀 버린다.\n이미 함께 보내 버린 시간은 어쩔 도리가 없다.
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoPast].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The threads of fate are entwined by encounter, and by the length of time surrendered unto another.\nThe myriad moments wherein one's time and another's overlap, be they fair or foul, will bind their strings in pitiless entanglement.\nThe time that has already been shared cannot be undone.
   PL: Wątki losu splatają się zależnie od tego, ile czasu spędzono po spotkaniu.\nTamte chwile, w których twój czas i mój się nakładały — piękne czy okropne — oplotły nasze losy z bezlitosną siłą.\nZ czasem już wspólnie spędzonym nic nie da się zrobić.
7. [Status [SojiRyoshuEchoFuture] — nazwa] 잔영
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoFuture].name
   kontekst: identyfikator statusu w tekstach: `[SojiRyoshuEchoFuture]`
   limit: do 40 znaków
   EN: Phantom Trace
   PL: Powidło
8. [Status [SojiRyoshuEchoFuture] — opis] - 최댓값 : 1\n- 거미집의 검 료슈의 기본 공격 스킬로 받는 피해 +5%
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoFuture].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +5% damage from Blade of the House of Spiders Ryōshū's Base Attack Skills
   PL: - Maks.: 1\n- Otrzymuje +5% obrażeń od bazowych Umiejętności ataku Ostrza Domu Pajęczyn Ryośu
9. [Status [SojiRyoshuEchoFuture] — tekst klimatyczny] 잔영(殘影)은 희미하게 남은 그림자가 아니다. 그것은 지난날 잔인하게 드리워졌던 옛 그림자다.
   źródło: Bufs.json :: dataList[id=SojiRyoshuEchoFuture].flavor
   limit: do 170 znaków
   EN: A phantom trace (殘影) is not simply a faint shade left in passing. It is the shadow of times past, cruelly drawn across bygone days.
   PL: Powidło (殘影) nie jest jedynie delikatnym cieniem pozostawionym w przejściu. To cień dawnych dni, okrutnie rzucany na minione czasy.
10. [Status [SojiRyoshuEntangle] — nazwa] 절연[絕緣]
   źródło: Bufs.json :: dataList[id=SojiRyoshuEntangle].name
   kontekst: identyfikator statusu w tekstach: `[SojiRyoshuEntangle]`
   limit: do 40 znaków
   EN: String Severance [絕緣]
   PL: Zerwanie Więzi [絕緣]
11. [Status [SojiRyoshuEntangle] — opis] - 최댓값 : 4\n- 사망한 아군 거미집 아비 인격 1명당 수치 1 증가\n- 사망한 아군 거미집 인격에 따라 고유 효과 얻음\n- 수치당 받는 피해 -7.5%
   źródło: Bufs.json :: dataList[id=SojiRyoshuEntangle].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Gain 1 Stack for every defeated The House of Spiders Nursefather Identity\n- Gain a different unique effect based on which of The House of Spiders ally was defeated\n- Take -7.5% damage for every Stack
   PL: - Maks.: 4\n- Zyskuje 1 wartości za każdą pokonaną osobowość sojuszniczego Ojca Domu Pajęczyn\n- Zyskuje unikalny efekt zależnie od tego, która sojusznicza osobowość Domu Pajęczyn poległa\n- Otrzymuje -7,5% obrażeń za każdą wartość
12. [Status [SojiRyoshuEntangle] — tekst klimatyczny] 그렇기에 끊어낸다. 도리에 어긋난다 하더라도.
   źródło: Bufs.json :: dataList[id=SojiRyoshuEntangle].flavor
   limit: do 120 znaków
   EN: And so, let it be cut and severed. Even if it strays from what must be.
   PL: I dlatego zrywa. Nawet jeśli wbrew temu, co należy uczynić.
13. [Status [SojiRyoshuShin] — nazwa] 신(心) - 지혜성[地慧星]
   źródło: Bufs.json :: dataList[id=SojiRyoshuShin].name
   kontekst: identyfikator statusu w tekstach: `[SojiRyoshuShin]`
   limit: do 40 znaków
   EN: Shin (心) - Dihui Star [地慧星]
   PL: Serce (心) - Gwiazda Dihui [地慧星]
14. [Status [SojiRyoshuShin] — opis] - 속도 최솟값, 최댓값 2 증가\n- 기본 공격 스킬 사용시 호흡 2, 호흡 횟수 1 얻음\n- 자신의 기본 공격 스킬 크리티컬 피해량 +10%\n- 일방 공격 또는 파괴 불가 코인으로 받는 피해량 -20%
   źródło: Bufs.json :: dataList[id=SojiRyoshuShin].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- Upon using a Base Attack Skill, gain 2 Poise Potency and +1 Poise Count\n- This unit's Base Attack Skills deal +10% damage on Critical Hit\n- Take -20% damage from Unopposed Attacks and Unbreakable Coins
   PL: - Minimalna i maksymalna Szybkość +2\n- Przy użyciu bazowej Umiejętności ataku zyskuje 2 Mocy Oddechu i 1 Licznik Oddechu\n- Zadaje +10% obrażeń krytycznych własnymi bazowymi Umiejętnościami ataku\n- Otrzymuje -20% obrażeń od ataków niekwestionowanych i Niezniszczalnych Monet
15. [Status [PhantomIncisionID] — nazwa] 검흔[잔상]
   źródło: Bufs.json :: dataList[id=PhantomIncisionID].name
   kontekst: identyfikator statusu w tekstach: `[PhantomIncisionID]`
   limit: do 40 znaków
   EN: Bladetrail [Afterimage]
   PL: Ślad Ostrza [Powidło]
16. [Status [PhantomIncisionID] — opis] - 최댓값 : 100\n- 수치 10당 참격 속성으로 받는 피해량 +1%
   źródło: Bufs.json :: dataList[id=PhantomIncisionID].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Take +1% damage from Slash Skills for every 10 Stacks
   PL: - Maks.: 100\n- Otrzymuje +1% obrażeń od Umiejętności Cięcia za każde 10 wartości
17. [Status [PhantomIncisionTotalID] — nazwa] 지혜성도
   źródło: Bufs.json :: dataList[id=PhantomIncisionTotalID].name
   kontekst: identyfikator statusu w tekstach: `[PhantomIncisionTotalID]`
   limit: do 40 znaków
   EN: Dihui Star's Blade
   PL: Ostrze Gwiazdy Dihui
18. [Status [PhantomIncisionTotalID] — opis] - 최댓값 : 70\n- 자신이 부여한 검흔 수치 총합\n- 턴당 최대 25까지 얻을 수 있음
   źródło: Bufs.json :: dataList[id=PhantomIncisionTotalID].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 70\n- Total sum of Bladetrail Stacks inflicted by this unit\n- Can gain up to 25 Stacks per turn
   PL: - Maks.: 70\n- Suma wartości Śladów Ostrza nadanych przez tę jednostkę\n- Można zyskać do 25 wartości na turę
19. [Status [PhantomIncisionTotalID] — tekst klimatyczny] 대지에 흔적을 남긴다. 이 검은 그러기 위한 검이다.\n이 땅에 무언가를 남기기 위한 별의 빛이 이 검에 녹여졌다.
   źródło: Bufs.json :: dataList[id=PhantomIncisionTotalID].flavor
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Etch a mark into the earth. Such is the purpose this blade was made to serve.\nInto this sword was poured the light of a star, so that something may be left behind in this land.
   PL: Pozostawia ślad na ziemi. W tym właśnie celu ten miecz istnieje.\nW to ostrze przetopiono światło gwiazdy, aby na tej ziemi coś po sobie zostawić.
20. [Status [RetaliationBookSpiderOutis] — nazwa] 앙갚음 장부 [거미집]
   źródło: Bufs.json :: dataList[id=RetaliationBookSpiderOutis].name
   kontekst: identyfikator statusu w tekstach: `[RetaliationBookSpiderOutis]`
   limit: do 60 znaków
   EN: Book of Vengeance [The House of Spiders]
   PL: Rejestr Odwetu [Dom Pajęczyn]
21. [Status [RetaliationBookSpiderOutis] — opis] - 거미집 중지 아비 오티스나 거미집 중지 제자 이스마엘이 이 효과를 보유한 대상에게 스킬 적중시 정신력 회복 5 (스킬당 1회, 턴당 2회)\n- 거미집 중지 아비 오티스나 거미집 중지 제자 이스마엘에게 스킬 적중시 대상이 중지 - 원한 1 추가로 얻음 (스킬당 1회, 턴당 2회,각 인격 별로 적용)\n- 턴 종료 시 사라짐
   źródło: Bufs.json :: dataList[id=RetaliationBookSpiderOutis].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Against units that have this effect, The House of Spiders: The Middle Nursefather Outis and The House of Spiders: The Middle Apprentice Ishmael heal 5 SP On Hit using a Skill (once per Skill, 2 times per turn)\n- On Hit using a Skill against The House of Spiders: The Middle Nursefather Outis, gain 1 additional Stack of The Middle - Grudge (once per Skill, 2 times per turn for each Identity)\n- On Hit using a Skill against The House of Spiders: The Middle Apprentice Ishmael, gain 1 additional Stack of The Middle - Grudge (once per Skill, 2 times per turn for each Identity)\n- Expires at Turn End
   PL: - Gdy Dom Pajęczyn: Ojciec Środkowego Outis lub Dom Pajęczyn: Uczeń Środkowego Ishmael trafi Umiejętnością jednostkę z tym efektem, regeneruje 5 Poczytalności (raz na Umiejętność, 2 razy na turę)\n- Gdy ta jednostka trafi Umiejętnością Dom Pajęczyn: Ojciec Środkowego Outis, zyskuje ona dodatkowo 1 wartości Środkowy - Uraza (raz na Umiejętność, 2 razy na turę, osobno dla każdej osobowości)\n- Gdy ta jednostka trafi Umiejętnością Dom Pajęczyn: Uczeń Środkowego Ishmael, zyskuje ona dodatkowo 1 wartości Środkowy - Uraza (raz na Umiejętność, 2 razy na turę, osobno dla każdej osobowości)\n- Znika na koniec tury
22. [Status [ResentmentSpiderOutis] — nazwa] 중지 - 원한
   źródło: Bufs.json :: dataList[id=ResentmentSpiderOutis].name
   kontekst: identyfikator statusu w tekstach: `[ResentmentSpiderOutis]`
   limit: do 40 znaków
   EN: The Middle - Grudge
   PL: Środkowy - Uraza
23. [Status [ResentmentSpiderOutis] — opis] - 최댓값: 15\n- 앙갚음 대상에게 주는 피해량 +20%
   źródło: Bufs.json :: dataList[id=ResentmentSpiderOutis].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- If target has Vengeance Mark, deal +20% damage
   PL: - Maks.: 15\n- Zadaje +20% obrażeń celom z Celem Odwetu
24. [Status [ReinforcedTattooSpiderOutis] — nazwa] 중지 - 원한 문신 [<s>큰 누님</s>]
   źródło: Bufs.json :: dataList[id=ReinforcedTattooSpiderOutis].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedTattooSpiderOutis]`
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: The Middle - Vengeance Tattoo [<s>Great Sister</s>]
   PL: Środkowy - Tatuaż Zemsty [<s>Wielka Siostra</s>]
25. [Status [ReinforcedTattooSpiderOutis] — opis] - 최댓값: 10\n- 수치 5당 기본 스킬의 최종 위력 +1 (최대 2)\n- 수치 1당 질투 속성이나 타격 속성 스킬 피해량 +5% (최대 50%)
   źródło: Bufs.json :: dataList[id=ReinforcedTattooSpiderOutis].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Final Power +1 for Base Skills for every 5 Stack (max 2)\n- Envy Skills and Blunt Skills deal +5% damage for every Stack (max 50%)
   PL: - Maks.: 10\n- Moc Końcowa bazowych Umiejętności +1 za każde 5 wartości (maks. 2)\n- Zadaje +5% obrażeń Umiejętnościami atrybutu Zazdrości lub typu Uderzenie za każdą wartość (maks. 50%)
26. [Status [DaughterEducationSpiderOutis] — nazwa] 잘 봐둬라 딸!
   źródło: Bufs.json :: dataList[id=DaughterEducationSpiderOutis].name
   kontekst: identyfikator statusu w tekstach: `[DaughterEducationSpiderOutis]`
   limit: do 40 znaków
   EN: Check This Out, Kiddo!
   PL: Dobrze się Przyjrzyj, Córeczko!
27. [Status [DaughterEducationSpiderOutis] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치가 5 이상이면, 기본 스킬의 최종 위력 +1\n- 수치당 타격 스킬의 피해량 +1% (최대 10%)
   źródło: Bufs.json :: dataList[id=DaughterEducationSpiderOutis].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced by 1 when this unit is hit by 2 Skills\n- At 5+ Stack, Base Skills gain Final Power +1\n- Blunt Skills deal +1% damage for every Stack (max 10%)
   PL: - Maks.: 10\n- Maleje o 1 po otrzymaniu 2 trafień Umiejętnościami\n- Przy 5 lub więcej wartości Moc Końcowa bazowych Umiejętności +1\n- Zadaje +1% obrażeń Umiejętnościami typu Uderzenie za każdą wartość (maks. 10%)
28. [Status [GotAComplimentIshmael] — nazwa] 칭찬 받았다!
   źródło: Bufs.json :: dataList[id=GotAComplimentIshmael].name
   kontekst: identyfikator statusu w tekstach: `[GotAComplimentIshmael]`
   limit: do 40 znaków
   EN: I Got Praised!
   PL: Dostałam Pochwałę!
29. [Status [GotAComplimentIshmael] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치가 5 이상이면, 기본 스킬의 최종 위력 +1\n- 수치당 타격 스킬의 피해량 +1% (최대 10%)
   źródło: Bufs.json :: dataList[id=GotAComplimentIshmael].desc
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
30. [Status [MiddleFatherGutsOutis] — nazwa] 초근성
   źródło: Bufs.json :: dataList[id=MiddleFatherGutsOutis].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherGutsOutis]`
   limit: do 40 znaków
   EN: Ridiculous Grit
   PL: Zwariowana Wytrwałość
31. [Status [MiddleFatherGutsOutis] — opis] - 최댓값: 3\n- 자신의 보통(1.0)을 초과하는 물리 내성을 보통(1.0)으로 변경 (흐트러진 경우 제외)\n- 스킬로 받는 피해량 30 + (중지 - 원한 문신 [<s>큰 누님</s>] 수치 x 4)%만큼 감소 (최대 50%, 소수점 버림)\n- 합 승리시 (합 횟수 x 5)만큼 정신력 추가로 오름 (최대 15)\n- 턴 종료시 자신의 스킬 효과로 이번 턴 정신력이 감소했으면, 다음 턴에 기본 스킬로 가하는 피해량 +10% (턴당 1회)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=MiddleFatherGutsOutis].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: <s>, </s>, \n
   EN: - Max Stack: 3\n- Fix any Attack Type Resistances that exceed Normal (1.0) to Normal (unless Staggered)\n- Take -(30 + (The Middle - Vengeance Tattoo [<s>Great Sister</s>] Stack x 4))% damage from Skills (max 50%; rounded down)\n- On Clash Win, heal an additional (Clash count x 5) SP (max 15)\n- Turn End: If this unit lost SP this turn due to its Skill effects, deal +10% damage next turn using Base Skills (once per turn)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 3\n- Przywraca każdą Odporność na Typy Ataku powyżej Normalnej (1.0) do Normalnej (1.0) (poza Stanem Oszołomienia)\n- Otrzymuje -(30 + (wartość Środkowy - Tatuaż Zemsty [<s>Wielka Siostra</s>] x 4))% obrażeń od Umiejętności (maks. 50%, zaokrąglona w dół)\n- Przy wygranej Starciu regeneruje dodatkowo (liczba Starć x 5) Poczytalności (maks. 15)\n- Na koniec tury, jeśli w tej turze Poczytalność tej jednostki spadła z powodu jej własnych Umiejętności, zadaje w następnej turze +10% obrażeń bazowymi Umiejętnościami (raz na turę)\n- Na koniec tury maleje o 1
32. [Status [MiddleFatherSwordOneOutis] — nazwa] 봉인된 검
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordOneOutis].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordOneOutis]`
   limit: do 40 znaków
   EN: Sealed Sword
   PL: Pieczętowany Miecz
33. [Status [MiddleFatherSwordOneOutis] — opis] - 턴 종료시 다음 턴에 신속 2 얻음\n- 적의 출혈 4당 타격 속성 기본 스킬로 가하는 피해량 +2% (최대 10%)\n- 기본 스킬의 마지막 코인 적중시 적의 출혈이 20 이상이면, 해당 코인 최종 피해량의 10%만큼 타격 피해 (소수점 버림)
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordOneOutis].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain 2 Haste next turn\n- Blunt Base Skills deal +2% damage for every 4 Bleed on target (max 10%)\n- On final Coin Hit using Base Skills, if target has 20+ Bleed, deal (10% of the Coin's final damage) Blunt damage (rounded down)
   PL: - Na koniec tury zyskuje w następnej turze 2 Pośpiechu\n- Zadaje +2% obrażeń Umiejętnościami ataku typu Uderzenie za każde 4 Krwawienia celu (maks. 10%)\n- Przy trafieniu ostatnią monetą, gdy cel ma 20+ Krwawienia, zadaje obrażenia Uderzeniem równe 10% końcowych obrażeń monety (zaokrąglona w dół)
34. [Status [MiddleFatherSwordTwoOutis] — nazwa] 1단계 봉인 해제
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordTwoOutis].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordTwoOutis]`
   limit: do 40 znaków
   EN: First Seal Removed
   PL: Zdjęta Pierwsza Pieczęć
35. [Status [MiddleFatherSwordTwoOutis] — opis] - 턴 종료시 다음 턴에 신속 1 얻음\n- 적의 화상과 출혈의 합 4당 타격 속성 기본 스킬로 가하는 피해량 +2% (최대 10%)\n- 기본 스킬의 마지막 코인 적중시 적의 화상과 출혈의 합이 20 이상이면, 해당 코인 최종 피해량의 10%만큼 타격 피해 (소수점 버림)
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordTwoOutis].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain 1 Haste next turn\n- Blunt Base Skills deal +2% damage for every 4 (Burn + Bleed) on target (max 10%)\n- On final Coin Hit using Base Skills, if target has 20+ (Burn + Bleed), deal (10% of the Coin's final damage) Blunt damage (rounded down)
   PL: - Na koniec tury zyskuje w następnej turze 1 Pośpiechu\n- Zadaje +2% obrażeń Umiejętnościami ataku typu Uderzenie za każde 4 (Podpalenie + Krwawienie) (maks. 10%)\n- Przy trafieniu ostatnią monetą, gdy cel ma 20+ (Podpalenie + Krwawienie), zadaje obrażenia Uderzeniem równe 10% końcowych obrażeń monety (zaokrąglona w dół)
36. [Status [MiddleFatherSwordThreeOutis] — nazwa] 2단계 봉인 해제
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordThreeOutis].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordThreeOutis]`
   limit: do 40 znaków
   EN: Second Seal Removed
   PL: Zdjęta Druga Pieczęć
37. [Status [MiddleFatherSwordThreeOutis] — opis] - 턴 종료시 다음 턴에 신속 1 얻음\n- 적의 화상과 출혈의 합 4당 타격 속성 기본 스킬로 가하는 피해량 +2% (최대 10%)\n- 기본 스킬의 마지막 코인 적중시 적의 화상과 출혈의 합이 20 이상이면, 해당 코인 최종 피해량의 10%만큼 참격 피해 (소수점 버림)
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordThreeOutis].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain 1 Haste next turn\n- Blunt Base Skills deal +2% damage for every 4 (Burn + Bleed) on target (max 10%)\n- On final Coin Hit using Base Skills, if target has 20+ (Burn + Bleed), deal (10% of the Coin's final damage) Slash damage (rounded down)
   PL: - Na koniec tury zyskuje w następnej turze 1 Pośpiechu\n- Zadaje +2% obrażeń Umiejętnościami ataku typu Uderzenie za każde 4 (Podpalenie + Krwawienie) (maks. 10%)\n- Przy trafieniu ostatnią monetą, gdy cel ma 20+ (Podpalenie + Krwawienie), zadaje obrażenia Cięciem równe 10% końcowych obrażeń monety (zaokrąglona w dół)
38. [Status [MiddleFatherSwordFourOutis] — nazwa] 레바테인
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordFourOutis].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFatherSwordFourOutis]`
   limit: do 40 znaków
   EN: Lævateinn
   PL: Lævateinn
39. [Status [MiddleFatherSwordFourOutis] — opis] - 턴 시작 시 전장에 있는 모든 캐릭터에게 화상 3 부여\n- 자신의 기본 스킬이 해당 스킬 등급에 해당하는 레바테인 전용 스킬로 변경됨\n- 적의 화상과 출혈의 합 4당 타격 속성 기본 스킬로 가하는 피해량 +2% (최대 10%)\n- 기본 스킬의 마지막 코인 적중시 적의 화상과 출혈의 합이 20 이상이면, 해당 코인 최종 피해량의 10%만큼 관통 피해 (소수점 버림)
   źródło: Bufs.json :: dataList[id=MiddleFatherSwordFourOutis].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Inflict 3 Burn on all units on the field\n- Replace this unit's Base Skills with Lævateinn-exclusive Skills corresponding to each Skill's rank\n- Blunt Base Skills deal +2% damage for every 4 (Burn + Bleed) on target (max 10%)\n- On final Coin Hit using Base Skills, if target has 20+ (Burn + Bleed), deal (10% of the Coin's final damage) Pierce damage (rounded down)
   PL: - Na początku tury nadaje 3 Podpalenia wszystkim jednostkom na polu\n- Własne bazowe Umiejętności zostają zastąpione wyłącznymi Umiejętnościami Lævateinn odpowiadającymi ich randze\n- Zadaje +2% obrażeń Umiejętnościami ataku typu Uderzenie za każde 4 (Podpalenie + Krwawienie) (maks. 10%)\n- Przy trafieniu ostatnią monetą bazowej Umiejętności, gdy cel ma 20+ (Podpalenie + Krwawienie), zadaje obrażenia Przebiciem równe 10% końcowych obrażeń monety (zaokrąglona w dół)
40. [Status [MidFamilyOutis] — nazwa] 가족의 복수
   źródło: Bufs.json :: dataList[id=MidFamilyOutis].name
   kontekst: identyfikator statusu w tekstach: `[MidFamilyOutis]`
   limit: do 40 znaków
   EN: Avenging My Family
   PL: Zemsta Rodziny
41. [Status [MidFamilyOutis] — opis] - 질투 속성의 기본 스킬 피해량 +20%\n- 기본 스킬의 최종 위력 +1
   źródło: Bufs.json :: dataList[id=MidFamilyOutis].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Envy Base Skills deal +20% damage\n- Base Skills gain Final Power +1
   PL: - Zadaje +20% obrażeń bazowymi Umiejętnościami atrybutu Zazdrości\n- Moc Końcowa bazowych Umiejętności +1
42. [Status [CountSkillMidOutis] — nazwa] 달아오르는 재미
   źródło: Bufs.json :: dataList[id=CountSkillMidOutis].name
   kontekst: identyfikator statusu w tekstach: `[CountSkillMidOutis]`
   limit: do 40 znaków
   EN: Rising Fever
   PL: Gorączka Zabawy
43. [Status [CountSkillMidOutis] — opis] 아래 조건으로 수치 1 감소 (턴당 1회)\n- ‘원한 스탬핑’ 사용 시 (반격으로 발동 포함)\n- 질투 완전 공명 수가 6 이상인 턴 종료시\n\n수치가 0이면, ‘포장을 뜯어볼까’를 사용함
   źródło: Bufs.json :: dataList[id=CountSkillMidOutis].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 1 Stack when meeting one of the following conditions (once per turn):\n- Using the "Stamp of Vengeance" Skill (including activation via Counter)\n- At Turn End after activating 6+ Envy A-Reson.\n\nAt 0 Stack, use the "Time to Unpack!" Skill
   PL: Gubi 1 wartości przy spełnieniu jednego z poniższych warunków (raz na turę):\n- Przy użyciu Umiejętności „Stempel Zemsty” (włącznie z aktywacją przez kontr)\n- Na koniec tury, gdy liczba Pełnych Rezonansów Zazdrości wynosi 6 lub więcej\n\nPrzy 0 wartości używa Umiejętności „Rozetniemy Opakowanie?”
44. [Status [MatchesPersonality] — nazwa] 타오름
   źródło: Bufs.json :: dataList[id=MatchesPersonality].name
   kontekst: identyfikator statusu w tekstach: `[MatchesPersonality]`
   limit: do 40 znaków
   EN: Blazing
   PL: Zapłon
45. [Status [MatchesPersonality] — opis] - 속도 최솟값, 최댓값 +1\n- 이번 턴에 처음으로 사용하는 기본 공격 스킬의 최종 위력 +2\n- 해당 스킬 적중시마다 최대 체력의 2%만큼 체력 피해를 입음 (최대 10%, 이 피해로 흐트러지거나 체력이 1 미만으로 감소하지 않음)\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=MatchesPersonality].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- This turn's first-used Base Attack Skill gains Final Power +2\n- Take 2% HP damage On Hit with the affected Skill (max 10%; this damage does not Stagger or reduce this unit's HP below 1)\n- Expires at Turn End
   PL: - Minimalna i maksymalna Szybkość +1\n- Pierwsza użyta w tej turze bazowa Umiejętność ataku zyskuje Moc Końcową +2\n- Przy każdym trafieniu tą Umiejętnością otrzymuje obrażenia HP równe 2% maks. HP (maks. 10%; te obrażenia nie Oszołomią ani nie obniżą HP poniżej 1)\n- Znika na koniec tury
46. [Status [ScratchesHurtID] — nazwa] 찢긴 상처
   źródło: Bufs.json :: dataList[id=ScratchesHurtID].name
   kontekst: identyfikator statusu w tekstach: `[ScratchesHurtID]`
   limit: do 40 znaków
   EN: Avulsion Wound
   PL: Rozdarta Rana
47. [Status [ScratchesHurtID] — opis] - 최댓값 : 3\n- 턴 시작 시, 출혈 2 얻음\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=ScratchesHurtID].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Gain 2 Bleed\n- Turn End: Gain 1 Bind next turn\n- Turn End: Lose 1 Stack
   PL: - Maks.: 3\n- Na początku tury zyskuje 2 Krwawienia\n- Na koniec tury zyskuje w nast. turze 1 Spętania\n- Na koniec tury maleje o 1
48. [Status [TiedRopeHonglu] — nazwa] 포박 [홍루]
   źródło: Bufs.json :: dataList[id=TiedRopeHonglu].name
   kontekst: identyfikator statusu w tekstach: `[TiedRopeHonglu]`
   limit: do 40 znaków
   EN: Trussed [Hong Lu]
   PL: Skuty [Hong Lu]
49. [Status [TiedRopeHonglu] — opis] - 기본값 : 3\n- 속도 최솟값, 최댓값 -2\n- 오만 속성으로 받는 피해량 +10%\n- 부여한 캐릭터가 퇴각 또는 사망하거나, 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 포박이 부여될 경우 교체됨.\n- 버프가 부여된 후, 부여자에게 공격받지 않았다면 턴 종료시 수치 1 감소
   źródło: Bufs.json :: dataList[id=TiedRopeHonglu].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Min & Max Speed -2\n- Take +10% Pride damage\n- Expires when the inflicter Retreats, is killed, or inflicts it on a different target. Replaced when Trussed by another unit\n- Turn End: Lose 1 Stack if the inflicter did not hit this unit this turn
   PL: - Wartość bazowa: 3\n- Minimalna i maksymalna Szybkość -2\n- Otrzymuje +10% obrażeń atrybutu Pychy\n- Znika, gdy nadający się wycofa, polegnie lub przeniesie ten efekt na inną jednostkę. Zastępowany, gdy inna jednostka nada Skucie.\n- Na koniec tury maleje o 1, jeśli nadający nie trafił tej jednostki w tej turze
50. [Status [TiedWithRopeID] — nazwa] 압송 채비
   źródło: Bufs.json :: dataList[id=TiedWithRopeID].name
   kontekst: identyfikator statusu w tekstach: `[TiedWithRopeID]`
   limit: do 50 znaków
   EN: Prisoner Transport Arrangements
   PL: Przygotowania Konwoju
51. [Status [TiedWithRopeID] — opis] - 기본값 : 1\n- {0} 포박중\n- 포박 [홍루]가 부여된 적과 합 진행 시 합 위력 +1\n- 포박 [홍루]가 부여된 적에게 적중시 출혈 1 부여, 호흡 1 얻음 (턴 당 스킬 2개에 발동 가능)\n- 포박이 부여된 대상이 없으면 소멸
   źródło: Bufs.json :: dataList[id=TiedWithRopeID].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Base Stack: 1\n- Currently Trussing {0}\n- In a Clash against enemies that have Trussed [Hong Lu], Clash Power +1\n- On Hit against enemies that have Trussed [Hong Lu], inflict 1 Bleed and gain 1 Poise (2 Skills per turn)\n- If there are no Trussed targets, expires
   PL: - Wartość bazowa: 1\n- Obecnie skuwa: {0}\n- W Starciu z wrogami ze Skutym [Hong Lu] zyskuje Moc Starcia +1\n- Przy trafieniu wrogów ze Skutym [Hong Lu] nadaje 1 Krwawienia i zyskuje 1 Oddechu (2 Umiejętności na turę)\n- Znika, gdy nie ma celów ze Skutym
52. [Status [AengduNewArmIshmael] — nazwa] 도깨비팔
   źródło: Bufs.json :: dataList[id=AengduNewArmIshmael].name
   kontekst: identyfikator statusu w tekstach: `[AengduNewArmIshmael]`
   limit: do 40 znaków
   EN: Dokkaebi Arms
   PL: Ramiona Dokkaebi
53. [Status [AengduNewArmIshmael] — opis] - 받는 피해 15% 감소\n- 스킬 사용 시 다음 턴에 신속 1 얻음 (턴당 2회)\n- 전투 종료 시 소멸하며, 호흡 횟수 2 얻음
   źródło: Bufs.json :: dataList[id=AengduNewArmIshmael].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take -15% damage\n- On Skill Use, gain 1 Haste next turn (2 times per turn)\n- Combat End: This effect expires, and gain +2 Poise Count
   PL: - Otrzymuje -15% obrażeń\n- Przy użyciu Umiejętności zyskuje w następnej turze 1 Pośpiechu (2 razy na turę)\n- Znika na koniec walki, zyskując 2 Liczniki Oddechu
54. [Status [BladelineagePride] — nazwa] 살수본위
   źródło: Bufs.json :: dataList[id=BladelineagePride].name
   kontekst: identyfikator statusu w tekstach: `[BladelineagePride]`
   limit: do 40 znaków
   EN: Bearing of a Salsu
   PL: Postawa Salsu
55. [Status [BladelineagePride] — opis] - 최댓값: 3\n- 수치만큼 공격 레벨 증가\n- 참격 스킬로 공격 적중시 호흡 1 얻음 (턴당 2회)\n- 검계 소속 아군 인격 사망 시 1 감소
   źródło: Bufs.json :: dataList[id=BladelineagePride].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain Offense Level for every Stack\n- On Attack Hit using Slash Skills, gain 1 Poise (2 times per turn) \n- Lose 1 Stack when an allied Blade Lineage Identity is defeated
   PL: - Maks.: 3\n- Zyskuje Poziom Ataku równy wartości\n- Przy trafieniu Umiejętnością typu Cięcie zyskuje 1 Oddechu (2 razy na turę)\n- Maleje o 1, gdy polegnie sojusznicza osobowość Rodu Ostrza
56. [Status [WindBladeIshmael] — nazwa] 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불
   źródło: Bufs.json :: dataList[id=WindBladeIshmael].name
   kontekst: identyfikator statusu w tekstach: `[WindBladeIshmael]`
   limit: do 100 znaków
   EN: Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   PL: Warsztat Mook - Ye [銳] II Dobycie Ostrza
57. [Status [WindBladeIshmael] — opis] - 최댓값: 20\n- 턴당 최대 10까지 얻을 수 있음\n- 수치 1당, 참격 속성인 기본 공격 스킬의 피해량 +1% (최대 10%)\n- 수치 2당, 수비 스킬의 합 위력 -1 (최대 5)\n- 턴 종료 시 다음 턴에 수치 5당, 신속 1 얻음 (최대 3)
   źródło: Bufs.json :: dataList[id=WindBladeIshmael].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Can gain up to 10 Stacks per turn\n- Slash Base Attack Skills deal +1% damage for every Stack (max 10%)\n- Defense Skills lose 1 Clash Power for every 2 Stacks (max 5)\n- Turn End: Gain 1 Haste next turn for every 5 Stacks (max 3)
   PL: - Maks.: 20\n- Można zyskać do 10 wartości na turę\n- Zadaje +1% obrażeń bazowymi Umiejętnościami ataku typu Cięcie za każdą wartość (maks. 10%)\n- Umiejętności Obrony tracą 1 Mocy Starcia za każde 2 wartości (maks. 5)\n- Na koniec tury zyskuje w następnej turze 1 Pośpiechu za każde 5 wartości (maks. 3)
58. [Status [AlcoholKimPersonal] — nazwa] 추모주
   źródło: Bufs.json :: dataList[id=AlcoholKimPersonal].name
   kontekst: identyfikator statusu w tekstach: `[AlcoholKimPersonal]`
   limit: do 40 znaków
   EN: Drink to the Fallen
   PL: Trunek Pamięci
59. [Status [AlcoholKimPersonal] — opis] - 최댓값: 4\n- 턴 시작 시 수치 1당, 호흡 1 얻음\n· 검계 우두머리 뫼르소면, 대신 호흡 2 얻음 \n- 기본 스킬의 크리티컬 피해량 +(자신의 호흡 위력 x 1.5)% (최대 15%)\n- 호흡 위력, 횟수를 얻는 기본 스킬의 합 위력 +1\n- 턴 종료 시 수치 1 감소
   źródło: Bufs.json :: dataList[id=AlcoholKimPersonal].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn Start: Gain 1 Poise for every Stack\n· Blade Lineage Mentor Meursault gains 2 Poise for every Stack instead\n- Base Skills deal +(Poise on self x 1.5)% damage on Critical Hit (max 15%)\n- Base Skills that gain Poise and Poise Count gain Clash Power +1\n- Turn End: Lose 1 Stack
   PL: - Maks.: 4\n- Na początku tury zyskuje 1 Oddechu za każdą wartość\n· Jeśli to Mentor Rodu Ostrza Meursault, zamiast tego zyskuje 2 Oddechu za każdą wartość\n- Zadaje +(Moc Oddechu x 1,5)% obrażeń krytycznych bazowymi Umiejętnościami (maks. 15%)\n- Bazowe Umiejętności zyskujące Moc i Licznik Oddechu zyskują Moc Starcia +1\n- Na koniec tury maleje o 1
60. [Status [GrudgePersonal] — nazwa] 맺혀가는 응어리
   źródło: Bufs.json :: dataList[id=GrudgePersonal].name
   kontekst: identyfikator statusu w tekstach: `[GrudgePersonal]`
   limit: do 40 znaków
   EN: Growing Resentment
   PL: Narastający Żal
61. [Status [GrudgePersonal] — opis] - 최댓값: 999\n- ‘골단’의 최종 위력이 (수치 / 100)만큼 증가 (최대 6, 소수점 버림)\n- ‘육참’, ‘골단’의 마지막 코인 적중 시 (수치 / 10)%만큼 피해량이 증가하고, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=GrudgePersonal].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 999\n- "To Claim Their Bones" gains (Stack / 100) Final Power (max 6; rounded down)\n- On Hit using the final Coins of either "Yield My Flesh" or "To Claim Their Bones", deal +(Stack / 10)% damage; then, this effect expires
   PL: - Maks.: 999\n- Moc Końcowa Umiejętności „Łamanie Kości” rośnie o (wartość / 100) (maks. 6, zaokrąglona w dół)\n- Przy trafieniu ostatnią monetą Umiejętności „Rzeź Ciała” lub „Łamanie Kości” zadaje +(wartość / 10)% obrażeń, po czym ten efekt znika
62. [Status [GhostKimPersonal] — nazwa] 원한
   źródło: Bufs.json :: dataList[id=GhostKimPersonal].name
   kontekst: identyfikator statusu w tekstach: `[GhostKimPersonal]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
63. [Status [GhostKimPersonal] — opis] - 속도 최솟값, 최댓값 +2\n- 공격 적중 시 스킬로 입힌 피해량의 10%만큼 자신의 체력 회복 (스킬당 최대 회복량: 자신의 최대 체력의 50%)
   źródło: Bufs.json :: dataList[id=GhostKimPersonal].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- On Hit, heal HP by 10% of damage dealt using the Skill (can heal up to 50% of this unit's max HP per Skill)
   PL: - Minimalna i maksymalna Szybkość +2\n- Przy trafieniu regeneruje HP równe 10% obrażeń zadanych Umiejętnością (maks. na Umiejętność: 50% maks. HP tej jednostki)
64. [Status [RootSoupKimPersonal] — nazwa] 한 서린 검집
   źródło: Bufs.json :: dataList[id=RootSoupKimPersonal].name
   kontekst: identyfikator statusu w tekstach: `[RootSoupKimPersonal]`
   limit: do 40 znaków
   EN: Resentful Scabbard
   PL: Pochwa Przesiąknięta Urazą
65. [Status [RootSoupKimPersonal] — opis] - 자신을 포함한 아군이 체력 피해를 받으면, 피해량만큼 맺혀가는 응어리 얻음\n- 추모 패시브가 조건을 무시하고 최대 효과로 발동함\n- 오만 공명 시 자신을 제외한 모든 검계 소속 아군에게 본국검 - 진전 전수를 부여함\n- ‘육참’ 사용 시 이 스킬 종료 시까지\n· 자신의 체력이 10 미만으로 내려가지 않음 (턴당 1회)\n· 합 위력이 (자신의 호흡 위력 / 2)만큼 감소 (소수점 버림)\n- '골단' 사용 시 호흡 4 얻음\n\n※ 본국검 - 진전 전수 효과\n- 기본 공격 스킬의 최종 위력이 (전장의 검계 소속 아군 수 / 3)만큼 증가 (최대 2, 소수점 버림)\n- 자신이 검계 살수면, 기본 스킬의 최종 위력 +1, 피해량 +(120 / 코인 수)%\n- 턴 종료 시 다음 턴에 신속 1 얻고 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RootSoupKimPersonal].desc
   limit: do 1060 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When an ally, including this unit, takes HP damage, gain Growing Resentment equal to damage taken\n- In Memoriam Passive now ignores conditionals and activates at max potential\n- When activating Pride Reson., apply Swordplay of the Homeland - The True Essence on all Blade Lineage allies other than this unit\n\n- On Using "Yield My Flesh", until Skill End:\n· This unit's HP does not drop below 10 (once per turn)\n· Lose (Poise on self / 2) Clash Power (rounded down)\n- On Using "To Claim Their Bones", gain 4 Poise\n\n※ Sword of the Homeland - The True Essence effects:\n- Base Attack Skills gain Final Power +(# of Blade Lineage allies on the field / 3) (max 2, rounded down)\n- If this unit is a Blade Lineage Salsu, Base Skills gain Final Power +1 and deal +(120 / # of Coins)% damage\n- Turn End: Gain 1 Haste next turn and this effect expires
   PL: - Gdy sojusznik, łącznie z tą jednostką, otrzyma obrażenia HP, zyskuje Narastający Żal równy otrzymanym obrażeniom\n- Pasyw Pamięci aktywuje się z pominięciem warunków, z pełnym efektem\n- Przy Rezonansie Pychy nadaje Szermierkę Ojczyzny - Prawdziwy Przekaz wszystkim sojusznikom Rodu Ostrza poza tą jednostką\n- Przy użyciu Umiejętności „Rzeź Ciała”, do końca tej Umiejętności:\n· HP tej jednostki nie spada poniżej 10 (raz na turę)\n· Traci Mocy Starcia równe (Moc Oddechu / 2) (zaokrąglona w dół)\n- Przy użyciu Umiejętności „Łamanie Kości” zyskuje 4 Oddechu\n\n※ Efekty Szermierki Ojczyzny - Prawdziwego Przekazu\n- Moc Końcowa bazowych Umiejętności ataku rośnie o (liczba sojuszników Rodu Ostrza na polu / 3) (maks. 2, zaokrąglona w dół)\n- Jeśli ta jednostka to Salsu Rodu Ostrza, bazowe Umiejętności zyskują Moc Końcową +1 i zadają +(120 / liczba monet)% obrażeń\n- Na koniec tury zyskuje w następnej turze 1 Pośpiechu, po czym ten efekt znika
66. [Status [RootSoupKimSatgat] — nazwa] 본국검 - 진전 전수
   źródło: Bufs.json :: dataList[id=RootSoupKimSatgat].name
   kontekst: identyfikator statusu w tekstach: `[RootSoupKimSatgat]`
   limit: do 60 znaków
   EN: Sword of the Homeland - The True Essence
   PL: Szermierka Ojczyzny - Prawdziwy Przekaz
67. [Status [RootSoupKimSatgat] — opis] - 기본 공격 스킬의 최종 위력이 (전장의 검계 소속 아군 수 / 3)만큼 증가 (최대 2, 소수점 버림)\n- 자신이 검계 살수면, 기본 스킬의 최종 위력 +1, 피해량 +(120 / 코인 수)%\n- 턴 종료 시 다음 턴에 신속 1 얻고 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RootSoupKimSatgat].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Attack Skills gain Final Power +(# of Blade Lineage allies on the field / 3) (max 2, rounded down)\n- If this unit is a Blade Lineage Salsu, Base Skills gain Final Power +1 and deal +(120 / # of Coins)% damage\n- Turn End: Gain 1 Haste next turn and this effect expires
   PL: - Moc Końcowa bazowych Umiejętności ataku rośnie o (liczba sojuszników Rodu Ostrza na polu / 3) (maks. 2, zaokrąglona w dół)\n- Jeśli ta jednostka to Salsu Rodu Ostrza, bazowe Umiejętności zyskują Moc Końcową +1 i zadają +(120 / liczba monet)% obrażeń\n- Na koniec tury zyskuje w następnej turze 1 Pośpiechu, po czym ten efekt znika
68. [Status [BongukGiftEnhance] — nazwa] 본국검 - 격법 전수
   źródło: Bufs.json :: dataList[id=BongukGiftEnhance].name
   kontekst: identyfikator statusu w tekstach: `[BongukGiftEnhance]`
   limit: do 50 znaków
   EN: Sword of the Homeland - Striking
   PL: Szermierka Ojczyzny - Przekaz Uderzeń
69. [Status [BongukGiftEnhance] — opis] - 최댓값: 1\n- 더하기 코인 위력 +1, 크리티컬 피해량 +15%\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=BongukGiftEnhance].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Plus Coin Power +1, deal +15% damage on Critical Hit\n- Expires at Turn End
   PL: - Maks.: 1\n- Moc Monety Plus +1, obrażenia krytyczne +15%\n- Znika na koniec tury
70. [Status [DuelEdgeAlly] — nazwa] 결투 고조
   źródło: Bufs.json :: dataList[id=DuelEdgeAlly].name
   kontekst: identyfikator statusu w tekstach: `[DuelEdgeAlly]`
   limit: do 40 znaków
   EN: The Duel Escalates
   PL: Eskalacja Pojedynku
71. [Status [DuelEdgeAlly] — opis] - 거미집 엄지 제자 히스클리프의 스킬, 패시브 효과에 영향을 끼침\n- 턴당 최대 3까지 얻을 수 있음\n- 최댓값 : 5
   źródło: Bufs.json :: dataList[id=DuelEdgeAlly].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Affects The House of Spiders: The Thumb Apprentice Heathcliff's Skills and Passive effects\n- Can gain up to 3 Stacks per turn\n- Max Stack: 5
   PL: - Wpływa na Umiejętności i efekty pasywów Dom Pajęczyn: Uczeń Kciuka Heathcliff\n- Można zyskać do 3 wartości na turę\n- Maks.: 5
72. [Status [DuelEdgeAlly] — podsumowanie] 거미집 엄지 제자 히스클리프의 스킬, 패시브 효과에 영향을 끼침
   źródło: Bufs.json :: dataList[id=DuelEdgeAlly].summary
   limit: do 120 znaków
   EN: Affects The House of Spiders: The Thumb Apprentice Heathcliff's Skills and Passive effects
   PL: Wpływa na Umiejętności i efekty pasywów Dom Pajęczyn: Uczeń Kciuka Heathcliff
73. [Status [SeveredTendonAlly] — nazwa] 힘줄 절단
   źródło: Bufs.json :: dataList[id=SeveredTendonAlly].name
   kontekst: identyfikator statusu w tekstach: `[SeveredTendonAlly]`
   limit: do 40 znaków
   EN: Severed Tendon
   PL: Przecięte Ścięgno
74. [Status [SeveredTendonAlly] — opis] - 기본 위력 -1\n- 턴 종료 시, 사라짐\n- 최댓값 : 1
   źródło: Bufs.json :: dataList[id=SeveredTendonAlly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Power -1\n- Expires at Turn End\n- Max Stack: 1
   PL: - Moc Bazowa -1\n- Znika na koniec tury\n- Maks.: 1
75. [Status [SeveredTendonAlly] — podsumowanie] 기본 위력 -1
   źródło: Bufs.json :: dataList[id=SeveredTendonAlly].summary
   limit: do 120 znaków
   EN: Base Power -1
   PL: Moc Bazowa -1
76. [Status [EvolvingManual] — nazwa] 완성되어가는 교본
   źródło: Bufs.json :: dataList[id=EvolvingManual].name
   kontekst: identyfikator statusu w tekstach: `[EvolvingManual]`
   limit: do 40 znaków
   EN: Maturing Textbook
   PL: Kształtujący się Podręcznik
77. [Status [EvolvingManual] — opis] - 기본 스킬의 피해량 +(10 + (수치 x 5))%\n- 턴당 최대 2까지 얻을 수 있음\n- 최댓값 : 3
   źródło: Bufs.json :: dataList[id=EvolvingManual].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Skills deal +(10 + (Stack x 5))% damage\n- Can gain up to 2 Stacks per turn\n- Max Stack: 3
   PL: - Zadaje +(10 + (wartość x 5))% obrażeń bazowymi Umiejętnościami\n- Można zyskać do 2 wartości na turę\n- Maks.: 3
78. [Status [EvolvingManual] — podsumowanie] 기본 스킬의 피해량이 증가
   źródło: Bufs.json :: dataList[id=EvolvingManual].summary
   limit: do 120 znaków
   EN: Base Skills deal more damage
   PL: Bazowe Umiejętności zadają więcej obrażeń
79. [Status [ObsessionAndGreedRodion] — nazwa] 신(心) - 불명예
   źródło: Bufs.json :: dataList[id=ObsessionAndGreedRodion].name
   kontekst: identyfikator statusu w tekstach: `[ObsessionAndGreedRodion]`
   limit: do 40 znaków
   EN: Shin (心) - Disgrace
   PL: Serce (心) - Hańba
80. [Status [ObsessionAndGreedRodion] — opis] - 속도 최솟값, 최댓값 1 증가\n- 기본 스킬로 부여하는 진동, 화상 위력과 횟수 부여량 +1\n- 자신의 호흡 위력 3당, 가하는 피해량 +3% (최대 15%)
   źródło: Bufs.json :: dataList[id=ObsessionAndGreedRodion].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Base Skills inflict +1 more Tremor and Burn Potency and Count\n- Deal +3% damage for every 3 Poise Potency on self (max 15%)
   PL: - Minimalna i maksymalna Szybkość +1\n- Bazowe Umiejętności nadają o 1 więcej Mocy i Licznika Wstrząsu oraz Podpalenia\n- Zadaje +3% obrażeń za każde 3 Mocy Oddechu (maks. 15%)
81. [Status [FutureEyeOnRodion] — nazwa] 예지안
   źródło: Bufs.json :: dataList[id=FutureEyeOnRodion].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOnRodion]`
   limit: do 40 znaków
   EN: Eye of Precognition
   PL: Oko Prekognicji
82. [Status [FutureEyeOnRodion] — opis] - 최댓값: 30\n- 턴당 최대 10까지 감소할 수 있음
   źródło: Bufs.json :: dataList[id=FutureEyeOnRodion].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Can lose up to 10 Stacks per turn
   PL: - Maks.: 30\n- Można stracić do 10 wartości na turę
83. [Status [FutureEyeOffRodion] — nazwa] 예지안 과열
   źródło: Bufs.json :: dataList[id=FutureEyeOffRodion].name
   kontekst: identyfikator statusu w tekstach: `[FutureEyeOffRodion]`
   limit: do 50 znaków
   EN: Eye of Precognition - Overheat
   PL: Oko Prekognicji - Przegrzanie
84. [Status [FutureEyeOffRodion] — opis] - 최댓값: 30\n- 공격 레벨 +3, 방어 레벨 -3\n- 턴 시작 시 10 증가\n- 수치가 30이면, '예지안'으로 변환
   źródło: Bufs.json :: dataList[id=FutureEyeOffRodion].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Offense Level +3, Defense Level -3\n- Turn Start: Gain 10 Stacks\n- At 30 Stacks, convert into "Eye of Precognition"
   PL: - Maks.: 30\n- Poziom Ataku +3, Poziom Obrony -3\n- Na początku tury zyskuje 10 wartości\n- Przy 30 wartości przekształca się w „Oko Prekognicji”
85. [Status [LookingFutureRodion] — nazwa] 가속하는 미래
   źródło: Bufs.json :: dataList[id=LookingFutureRodion].name
   kontekst: identyfikator statusu w tekstach: `[LookingFutureRodion]`
   limit: do 40 znaków
   EN: Accelerating Future
   PL: Przyspieszająca Przyszłość
86. [Status [LookingFutureRodion] — opis] - 최댓값: 5\n- 수치 1당, 기본 스킬로 가하는 피해량 +3% (최대 15%)\n- 수치 2당, 기본 스킬의 합 위력 +1\n- 수치가 5면, 기본 스킬의 코인 위력 +1\n- 스킬 종료 시 소멸
   źródło: Bufs.json :: dataList[id=LookingFutureRodion].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Base Skills deal +3% damage for every Stack (max 15%)\n- Base Skill Clash Power +1 for every 2 Stacks\n- At 5 Stacks, Base Skill Coin Power +1\n- Expires at Skill End
   PL: - Maks.: 5\n- Zadaje +3% obrażeń bazowymi Umiejętnościami za każdą wartość (maks. 15%)\n- Moc Starcia bazowych Umiejętności +1 za każde 2 wartości\n- Przy 5 wartości Moc Monety bazowych Umiejętności +1\n- Znika na koniec Umiejętności
87. [Status [TeachersPreyRodion] — nazwa] 사냥 표적
   źródło: Bufs.json :: dataList[id=TeachersPreyRodion].name
   kontekst: identyfikator statusu w tekstach: `[TeachersPreyRodion]`
   limit: do 40 znaków
   EN: Game Target
   PL: Cel Polowania
88. [Status [TeachersPreyRodion] — opis] - 거미집 엄지 아비 로쟈에게 기본 스킬로 받는 피해량 +15%
   źródło: Bufs.json :: dataList[id=TeachersPreyRodion].desc
   limit: do 130 znaków
   EN: - Take +15% damage from Base Skills used by The House of Spiders: The Thumb Nursefather Rodion
   PL: - Otrzymuje +15% obrażeń od bazowych Umiejętności Dom Pajęczyn: Ojciec Kciuka Rodion
89. [Status [StigmaWorkshopHandStep1] — nazwa] 새벽불
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep1].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopHandStep1]`
   limit: do 40 znaków
   EN: Light of Daybreak
   PL: Płomień Świtu
90. [Status [StigmaWorkshopHandStep1] — opis] - 최댓값: 30\n- 턴당 최대 20까지 얻을 수 있음\n- 턴 시작 시 수치 5당, 화상 1 얻은 뒤 수치 10당, 자신의 화상 횟수 1 증가\n- 기본 공격 스킬 적중 시 (1 + 대상의 화상 위력 / 3)만큼 수치 증가 (최대 3)\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep1].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Can gain up to 20 Stack per turn\n- Turn Start: Gain 1 Burn for every 5 Stack; then, gain +1 Burn Count for every 10 Stack\n- On Hit using a Base Attack Skill, gain (1 + (Burn on target / 3)) Stack (max 3)\n- At 10+ Stack, Base Skills inflict +1 more Burn Potency on enemies\n- At 20+ Stack, Base Skills inflict +1 more Burn Count on enemies
   PL: - Maks.: 30\n- Można zyskać do 20 wartości na turę\n- Na początku tury zyskuje 1 Podpalenia za każde 5 wartości, następnie 1 Licznik Podpalenia za każde 10 wartości\n- Przy trafieniu bazową Umiejętnością ataku zyskuje (1 + Moc Podpalenia celu / 3) wartości (maks. 3)\n- Przy 10 lub więcej wartości bazowe Umiejętności nadają wrogom o 1 więcej Mocy Podpalenia\n- Przy 20 lub więcej wartości bazowe Umiejętności nadają wrogom o 1 więcej Liczników Podpalenia
91. [Status [StigmaWorkshopHandStep1] — podsumowanie] 적중 시 수치 증가\n조건 만족 시 화상 위력, 횟수 부여량 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep1].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Stack On Hit\nWhen conditions are met, inflict more Burn Potency and Count
   PL: Zyskuje wartości przy trafieniu\nPo spełnieniu warunków nadaje więcej Mocy i Liczników Podpalenia
92. [Status [StigmaWorkshopHandStep1] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep1].flavor
   limit: do 120 znaków
   EN: The first flare of dawn is not a fire that scorches, but one that casts its glow on people.
   PL: Płomień, który rozświetla świt, nie jest ogniem, co pali, lecz ogniem, co oświetla ludzi.
93. [Status [StigmaWorkshopHandStep2] — nazwa] 새벽불
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep2].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopHandStep2]`
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Status [StigmaWorkshopHandStep2] — opis] - 최댓값: 30\n- 턴당 최대 20까지 얻을 수 있음\n- 턴 시작 시 수치 5당, 화상 1 얻은 뒤 수치 10당, 자신의 화상 횟수 1 증가\n- 기본 공격 스킬 적중 시 (1 + 대상의 화상 위력 / 3)만큼 수치 증가 (최대 3)\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep2].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
95. [Status [StigmaWorkshopHandStep2] — podsumowanie] 적중 시 수치 증가\n조건 만족 시 화상 위력, 횟수 부여량 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep2].summary
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Status [StigmaWorkshopHandStep2] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep2].flavor
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Status [StigmaWorkshopHandStep3] — nazwa] 새벽불
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep3].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopHandStep3]`
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Status [StigmaWorkshopHandStep3] — opis] - 최댓값: 30\n- 턴당 최대 20까지 얻을 수 있음\n- 턴 시작 시 수치 5당, 화상 1 얻은 뒤 수치 10당, 자신의 화상 횟수 1 증가\n- 기본 공격 스킬 적중 시 (1 + 대상의 화상 위력 / 3)만큼 수치 증가 (최대 3)\n- 수치가 10 이상이면, 적에게 기본 스킬로 부여하는 화상 위력 부여량 +1\n- 수치가 20 이상이면, 적에게 기본 스킬로 부여하는 화상 횟수 부여량 +1
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep3].desc
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Status [StigmaWorkshopHandStep3] — podsumowanie] 적중 시 수치 증가\n조건 만족 시 화상 위력, 횟수 부여량 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep3].summary
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Status [StigmaWorkshopHandStep3] — tekst klimatyczny] 새벽을 밝히는 불은, 무언가를 태우는 불이 아닌 누군가를 비추는 불이다.
   źródło: Bufs.json :: dataList[id=StigmaWorkshopHandStep3].flavor
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Status [DawnLight] — nazwa] 새벽맞이
   źródło: Bufs.json :: dataList[id=DawnLight].name
   kontekst: identyfikator statusu w tekstach: `[DawnLight]`
   limit: do 40 znaków
   EN: Dawnherald
   PL: Powitanie Świtu
102. [Status [DawnLight] — opis] - 최댓값: 3\n- 화상 위력, 화상 횟수 또는 특수 화상을 부여하는 기본 스킬로 가하는 피해량 +10%\n· 해당 스킬이 분노 속성 스킬일 경우 대신 피해량 +15%\n- 화상 위력, 화상 횟수 또는 특수 화상을 부여하는 기본 스킬의 합 위력 +1\n· 새벽 사무소 소속 인격이면, 대신 기본 위력 +1 \n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=DawnLight].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Base Skills that inflict Burn Potency, Count, or 'Unique Burn' deal +10% damage\n· If the said Skill is a Wrath Skill, deal +15% damage instead\n\n- Base Skills that inflict Burn Potency, Count, or 'Unique Burn', gain Clash Power +1\n· If this unit is a Dawn Office Identity, gain Base Power +1 instead\n- Turn End: Lose 1 Stack
   PL: - Maks.: 3\n- Zadaje +10% obrażeń bazowymi Umiejętnościami nadającymi Moc, Licznik lub Szczególne Podpalenie\n· Jeśli ta Umiejętność jest atrybutu Gniewu, zamiast tego zadaje +15% obrażeń\n- Bazowe Umiejętności nadające Moc, Licznik lub Szczególne Podpalenie zyskują Moc Starcia +1\n· Jeśli ta jednostka to osobowość Biura Świtu, zamiast tego zyskuje Moc Bazową +1\n- Na koniec tury maleje o 1
103. [Status [DawnLight] — tekst klimatyczny] “무작정 불태우기만 하는 불길이 만사는 아니야. 이런 열을 다루는 무기를 휘두를 때는 상황에 따라 열을 언제, 얼마나 올리는지가 중요하거든.”\n”내가 타이밍이 중요하다고 매번 말하는 이유가 그거야. 열을 다루는 무기만의 절묘하고 섬세한 감각이 있어. 하지만 모든 열을 다해 불사를 때에는 온 힘을 다하도록… 뭐? 가장 그 감각을 잘 다루는 해결사가 누구냐고?”\n”흐음… 이 분야에서 최고는 주홍십자겠지?”
   źródło: Bufs.json :: dataList[id=DawnLight].flavor
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Burn, burn, burn—y'see, Kid, fire's not the be-all, end-all solution to every problem you've got. When it comes to using heat-modulating weapons like these, the deciding factors often come down to <i>when</i> to spark the flame, and <i>how hot</i> you let it burn.\n"Yeah, that's why I'm always chewing your ear off about how important it is to feel the 'moment' that comes with the territory of using heat-modulating weapons. But on the other hand... when that 'moment' tells you to burn it all down, don't hold back and just let it rip. ... Hm? Oh, you want to know who's the best in the field?"\n"Hmm, let's see... Well, the best of the best's got to be the Vermilion Cross, I'd wager."
   PL: „Pospolite podpalanie to nie wszystko, Dzieciak. Władając bronią manipulującą ciepłem, decydujące jest to, kiedy wzniecić płomień i jak bardzo go rozpalić.”\n„Dlatego wciąż powtarzam ci o ważności chwili, która przynależy do władania taką bronią. Ta subtelna wrażliwość jest czymś osobnym. Ale gdy chwila nakazuje spalić wszystko — rzuć się w to na całego… Hm? Chcesz wiedzieć, kto jest najlepszy w tej dziedzinie?”\n„Hmm, zobaczmy… najlepszy z najlepszych to pewnie Cynobrowy Krzyż.”
104. [Status [RunSinclair] — nazwa] 도주 장치
   źródło: Bufs.json :: dataList[id=RunSinclair].name
   kontekst: identyfikator statusu w tekstach: `[RunSinclair]`
   limit: do 40 znaków
   EN: Escape Apparatus
   PL: Urządzenie Ucieczki
105. [Status [RunSinclair] — opis] - 체력이 10이 되는 피해를 받으면, 해당 턴 동안 체력이 10 미만으로 감소하지 않음\n- 위 효과가 발동한 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음, 이탈이 불가능한 전투에서는 이탈 효과가 발동되지 않으며 턴 종료 시 소멸)\n\n- 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동\n  (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n- 전투 복귀 시 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨\n  (정신력이 0 미만이면, 0으로 초기화)
   źródło: Bufs.json :: dataList[id=RunSinclair].desc
   limit: do 1150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When this unit takes damage that brings its HP down to 10, this unit's HP does not drop below 10 for the turn\n- Turn End after the above effect activates: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death; in Encounters where Retreat is disabled, the Retreat effect does not activate and expires at Turn End)\n  · In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n  · When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self save for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Po otrzymaniu obrażeń, które obniżają HP do 10, HP tej jednostki nie spada poniżej 10 w tej turze\n- Na koniec tury, w której aktywował się powyższy efekt, dochodzi do siebie z Oszołomienia i opuszcza walkę (poza Wymuszonym Oszołomieniem; nie liczy się jako śmierć; w walkach bez możliwości odwrotu efekt nie aktywuje się i znika na koniec tury)\n\n- W walkach łańcuchowych: przy odwrocie przekazuje liczbę swoich slotów jednostce zastępczej, zostaje wymieniona i przesuwa się na koniec kolejki jednostek rezerwowych\n  (jeśli w następnej turze nie ma rezerwowych do wymiany, opuszcza walkę całkowicie; przy powrocie wraca w kolejności odwrotu)\n- Przy powrocie do walki traci wszystkie efekty poza nielicznymi nadanymi jej efektami, zachowując HP i Poczytalność z momentu odwrotu\n  (przy Poczytalności poniżej 0 jest ona resetowana do 0)
106. [Status [RunSinclair] — tekst klimatyczny] ‘…살아남아라.’
   źródło: Bufs.json :: dataList[id=RunSinclair].flavor
   limit: do 120 znaków
   EN: '... Live.'
   PL: …Musisz przetrwać.
107. [Status [FireField] — nazwa] 작열지대
   źródło: Bufs.json :: dataList[id=FireField].name
   kontekst: identyfikator statusu w tekstach: `[FireField]`
   limit: do 40 znaków
   EN: Scorchfield
   PL: Strefa Żaru
108. [Status [FireField] — opis] - 최댓값: 999\n- 해당 장소에서 발생한 화상 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함
   źródło: Bufs.json :: dataList[id=FireField].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 999\n- Stores all Burn damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters
   PL: - Maks.: 999\n- Gromadzi wszystkie obrażenia Podpaleniem zadane w tej strefie\n- Resetuje się przy zmianie strefy walki\n- Wartość współdzielona przez wszystkie jednostki
109. [Status [FireField] — tekst klimatyczny] 뜨거운 열기로 격해진 불의 바람은, 거리낌 없이 숲을 태우고 그곳의 인간과 짐승들을 떠나게 만들지니.
   źródło: Bufs.json :: dataList[id=FireField].flavor
   limit: do 150 znaków
   EN: Heat turns air into a breeze, a gust, a firestorm, scorching the forest with abandon as men and beasts alike depart.
   PL: Gorąco rozżarzone wiatry ognia bez wahania pożerają las, zmuszając ludzi i zwierzęta do odejścia.
110. [Status [DawnGregor] — nazwa] 새벽에서 노을로
   źródło: Bufs.json :: dataList[id=DawnGregor].name
   kontekst: identyfikator statusu w tekstach: `[DawnGregor]`
   limit: do 40 znaków
   EN: From Dawnbreak to Sunset
   PL: Od Świtu do Zachodu Słońca
111. [Status [DawnGregor] — opis] - 흐트러짐 구간이 3개 이상이면, 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제\n- 턴 종료 시 흐트러짐 상태이면, 흐트러짐 상태를 해제하고 인격 동기화 단계가 3단계 이상이면, 기본 스킬 1개를 스킬 3으로 변경\n(강제 흐트러짐 제외, 전투당 1회, 등급이 가장 낮은 스킬 우선)\n\n- 턴 시작 시 정신력 5 회복\n- 패시브'불안정한 자아의 껍질'과 기본 공격 스킬의 효과와 불안정한 격정 효과로 인해, 정신력이 25 미만으로 감소하지 않음\n\n- 불안정 E.G.O::밀랍날개 상태일 시, 다음 효과 추가\n· 턴 시작 시 최대 체력의 15% 만큼 보호막을 얻음\n· 보호막이 있는 동안 피격 시, 공격자에게 화상 1 부여 (턴당 2회)\n· 해당 장소에서 작열지대 활성화\n\n※ 작열지대 효과\n- 해당 장소에서 발생한 화상 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함
   źródło: Bufs.json :: dataList[id=DawnGregor].desc
   limit: do 1100 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit has 3+ Stagger Thresholds, remove the first Stagger Threshold\n- Turn End: If this unit is Staggered, recover from Stagger; if this unit is at Uptie 3 or higher, replace 1 of its Base Skills with Skill 3\n(excluding forced Staggers; once per Encounter; prioritizes the Skill of lowest rank)\n\n- Turn Start: Heal 5 SP\n- Passive "Unstable Shell of Ego" effects, Base Attack Skill effects, and Volatile Passion effects cannot reduce this unit's SP below 25\n\n- When in Volatile E.G.O::Waxen Pinion state, gain the following effects:\n  · Turn Start: Gain Shield equal to 15% of max HP\n  · When hit while this unit has Shield, inflict 1 Burn against the attacker (2 times per turn)\n  · Activate Scorchfield on this field\n\n※ Scorchfield effects\n- Stores all Burn damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters
   PL: - Przy 3 lub więcej Progach Oszołomienia usuwa pierwszy z nich\n- Na koniec tury, jeśli jednostka jest Oszołomiona, dochodzi do siebie z Oszołomienia; a jeśli ma Uptie 3 lub wyższe, zamienia 1 bazową Umiejętność w Umiejętność 3\n(pomijając Wymuszone Oszołomienie; raz na walkę; priorytet dla Umiejętności najniższej rangi)\n\n- Na początku tury regeneruje 5 Poczytalności\n- Z powodu efektów pasywu „Niestabilnej Skorupy Jaźni”, efektów bazowych Umiejętności ataku i efektu Niestabilnej Żarliwości Poczytalność tej jednostki nie spada poniżej 25\n\n- W stanie Niestabilne E.G.O::Woskowe Skrzydło zyskuje następujące efekty:\n· Na początku tury zyskuje Tarczę równą 15% maks. HP\n· Przy trafieniu posiadając Tarczę, nadaje atakującemu 1 Podpalenia (2 razy na turę)\n· Aktywuje Strefę Żaru na tym polu\n\n※ Efekty Strefy Żaru\n- Gromadzi wszystkie obrażenia Podpaleniem zadane w tej strefie\n- Resetuje się przy zmianie strefy walki\n- Wartość współdzielona przez wszystkie jednostki
112. [Status [DawnGregor] — tekst klimatyczny] “허. 역시 향이 좋군. 쌍화차 타는 실력만큼은 특색이아. 특색 노란쌍화….”\n”내가 옆에 붙어서 가르쳐줄 테니, 잘 따라만 오면 좋겠군. 결국 모든 건 타이밍인데… 쌍화차에서 느껴지는 이 절묘한 타이밍이 심상치가 않아.”
   źródło: Bufs.json :: dataList[id=DawnGregor].flavor
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Ah... What a pleasant aroma. You're practically a Color Fixer when it comes to brewing ssanghwa-cha, you know that? I hereby anoint you Color Fixer "The Yellow Ssanghwa..."\n"That's settled, then. I'll be tutoring you myself, so you'd better keep up. I see real potential in you, Kid—your ssanghwa-cha brewing skills have this instinctive grasp of the 'moment'... And being able to recognize that 'moment' is the key to just about everything."
   PL: „Ho. Aromat istotnie przyjemny. O ile w parzeniu ssanghwa-cha — to prawdziwa osobliwość. Osobliwość Żółta Ssanghwa…”\n„Uczę cię osobiście, więc trzymaj się mnie jak najbliżej. W końcu wszystko sprowadza się do timingu… ten subtelny timing, który czuć w ssanghwa-cha, jest czymś nadzwyczajnym.”
113. [Status [DawnFaust] — nazwa] 정오
   źródło: Bufs.json :: dataList[id=DawnFaust].name
   kontekst: identyfikator statusu w tekstach: `[DawnFaust]`
   limit: do 40 znaków
   EN: High Noon
   PL: Samo Południe
114. [Status [DawnFaust] — opis] - 속도 최솟값 +2\n- 기본 공격 스킬 사용 시 기본 위력 +2, 피해량 +(45/코인수)%\n\n- ‘노을빛 검’에 아래 효과 추가\n· 마지막 코인 적중 시 대상의 화상이 15 이상이면, 대상의 화상 발동. 대상의 화상 횟수 1 감소\n\n- ‘타오르는 일격’에 아래 효과 추가\n· 피해량 +100%\n· 사용 시 모든 코인이 파괴 불가 코인으로 변경됨\n· 적에게 공격 적중 시 대상의 화상 발동. 대상의 화상 횟수 1 감소\n· 불안정한 격정이 3 이상이면, 사용 시 작열지대를 최대 100 소모\n· 소모한 수치 1당, 피해량 +1% (최대 100%)\n\n※ 작열지대 효과\n- 해당 장소에서 발생한 화상 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함
   źródło: Bufs.json :: dataList[id=DawnFaust].desc
   limit: do 930 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min Speed +2\n- On Base Attack Skill Use: Gain Base Power +2 and deal +(45 / # of Coins)% damage\n\n- Apply the following effects to "Sunset Blade"\n· On final Coin Hit: If target has 15+ Burn, activate Burn on target; then, reduce target's Burn Count by 1\n\n- Apply the following effects to "Blazing Strike"\n· Deal +100% damage\n· On Use: Convert all Coins into Unbreakable Coins\n· On Hit against an enemy, activate Burn on target; then, reduce target's Burn Count by 1\n· On Use: At 3+ Volatile Passion, consume up to 100 Scorchfield\n· Deal +1% damage for every Scorchfield consumed (max 100%)\n\n* Scorchfield Effects\n- Stores all Burn damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters
   PL: - Minimalna Szybkość +2\n- Przy użyciu bazowej Umiejętności ataku zyskuje Moc Bazową +2 i zadaje +(45 / liczba monet)% obrażeń\n\n- Dodaje następujące efekty do „Ostrza Zachodu Słońca”:\n· Przy trafieniu ostatnią monetą, jeśli cel ma 15 lub więcej Podpalenia, aktywuje Podpalenie celu. Traci 1 Licznik Podpalenia celu\n\n- Dodaje następujące efekty do „Płonącego Ciosu”:\n· Zadaje +100% obrażeń\n· Przy użyciu wszystkie monety stają się Niezniszczalnymi Monetami\n· Przy trafieniu wroga aktywuje Podpalenie celu. Traci 1 Licznik Podpalenia celu\n· Przy 3 lub więcej Niestabilnej Żarliwości zużywa przy użyciu do 100 Strefy Żaru\n· Zadaje +1% obrażeń za każdą zużytą wartość (maks. 100%)\n\n※ Efekty Strefy Żaru\n- Gromadzi wszystkie obrażenia Podpaleniem zadane w tej strefie\n- Resetuje się przy zmianie strefy walki\n- Wartość współdzielona przez wszystkie jednostki
115. [Status [DawnFaust] — podsumowanie] 기본 공격 스킬 강화
   źródło: Bufs.json :: dataList[id=DawnFaust].summary
   limit: do 120 znaków
   EN: Strengthen Base Attack Skills
   PL: Wzmocnienie bazowych Umiejętności ataku
116. [Status [DawnFaust] — tekst klimatyczny] “의뢰가 일찍 끝났군요. 그리고 날이 좋습니다. 다 같이 점심을 먹으러 가죠.”
   źródło: Bufs.json :: dataList[id=DawnFaust].flavor
   limit: do 180 znaków
   EN: "The request has been resolved ahead of schedule, and the weather conditions are optimal today for a team lunch. Shall we all proceed?"
   PL: „Zlecenie zakończyło się wcześniej. A pogoda dopisuje. Idziemy wszyscy razem na obiad.”
117. [Status [DawnGregorDying] — nazwa] 타오르는 노을
   źródło: Bufs.json :: dataList[id=DawnGregorDying].name
   kontekst: identyfikator statusu w tekstach: `[DawnGregorDying]`
   limit: do 40 znaków
   EN: Blazing Sunset
   PL: Płonący Zachód Słońca
118. [Status [DawnGregorDying] — opis] - 흐트러짐 구간이 3개 이상이면, 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제\n- 턴 종료 시 흐트러짐 상태이면, 흐트러짐 상태를 해제하고 인격 동기화 단계가 3단계 이상이면, 기본 스킬 1개를 스킬 3으로 변경\n(강제 흐트러짐 제외, 전투당 1회, 등급이 가장 낮은 스킬 우선)\n\n- 턴 시작 시 정신력 8 회복\n- 패시브'불안정한 자아의 껍질'과 기본 공격 스킬의 효과와 불안정한 격정 효과로 인해, 정신력이 45 미만으로 감소하지 않음\n\n- 턴 시작 시 불안정 E.G.O::밀랍날개 상태가 되며, 최대 체력의 50%만큼 체력 회복, 정신력 최대치로 회복 (전투당 1회)\n- 턴 시작 시 정신력이 0 이하여도 불안정 E.G.O::밀랍날개 상태가 유지됨\n\n- 불안정 E.G.O::밀랍날개 상태일 시, 다음 효과 추가\n· 턴 시작 시 최대 체력의 20% 만큼 보호막을 얻음\n· 보호막이 있는 동안 피격 시, 공격자에게 화상 2 부여 (턴당 2회)\n· 해당 장소에서 작열지대 활성화\n\n※ 작열지대 효과\n- 해당 장소에서 발생한 화상 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함
   źródło: Bufs.json :: dataList[id=DawnGregorDying].desc
   limit: do 1370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit has 3+ Stagger Thresholds, remove the first Stagger Threshold\n- Turn End: If this unit is Staggered, recover from Stagger; if this unit is at Uptie 3 or higher, replace 1 of its Base Skills with Skill 3\n(excluding forced Staggers; once per Encounter; prioritizes the Skill of lowest rank)\n\n- Turn Start: Heal 8 SP\n- Passive "Unstable Shell of Ego" effects, Base Attack Skill effects, and Volatile Passion effects cannot reduce this unit's SP below 45\n\n- Turn Start: enter the Volatile E.G.O::Waxen Pinion State, heal 50% HP, and heal SP to max (once per Encounter)\n- Volatile E.G.O::Waxen Pinion State is maintained even when this unit has 0 or lower SP at Turn Start\n\n- When in Volatile E.G.O::Waxen Pinion state, gain the following effects:\n  · Turn Start: Gain Shield equal to 20% of max HP\n  · When hit while this unit has Shield, inflict 2 Burn against the attacker (2 times per turn)\n  · Activate Scorchfield on this field\n\n※ Scorchfield effects\n- Stores all Burn damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters
   PL: - Przy 3 lub więcej Progach Oszołomienia usuwa pierwszy z nich\n- Na koniec tury, jeśli jednostka jest Oszołomiona, dochodzi do siebie z Oszołomienia; a jeśli ma Uptie 3 lub wyższe, zamienia 1 bazową Umiejętność w Umiejętność 3\n(pomijając Wymuszone Oszołomienie; raz na walkę; priorytet dla Umiejętności najniższej rangi)\n\n- Na początku tury regeneruje 8 Poczytalności\n- Z powodu efektów pasywu „Niestabilnej Skorupy Jaźni”, efektów bazowych Umiejętności ataku i efektu Niestabilnej Żarliwości Poczytalność tej jednostki nie spada poniżej 45\n\n- Na początku tury wchodzi w stan Niestabilne E.G.O::Woskowe Skrzydło, regeneruje HP równe 50% maks. HP i przywraca Poczytalność do maksimum (raz na walkę)\n- Stan Niestabilne E.G.O::Woskowe Skrzydło utrzymuje się nawet, gdy na początku tury Poczytalność wynosi 0 lub mniej\n\n- W stanie Niestabilne E.G.O::Woskowe Skrzydło zyskuje następujące efekty:\n· Na początku tury zyskuje Tarczę równą 20% maks. HP\n· Przy trafieniu posiadając Tarczę, nadaje atakującemu 2 Podpalenia (2 razy na turę)\n· Aktywuje Strefę Żaru na tym polu\n\n※ Efekty Strefy Żaru\n- Gromadzi wszystkie obrażenia Podpaleniem zadane w tej strefie\n- Resetuje się przy zmianie strefy walki\n- Wartość współdzielona przez wszystkie jednostki
119. [Status [DawnGregorDying] — tekst klimatyczny] “아직 가르쳐주실 게 많이 남았다고 말씀하셨잖아요…”\n아침을 열던 새벽은 언제까지 그 자리에 있지 않고, 저녁을 여는 노을을 남기고 사라진다.
   źródło: Bufs.json :: dataList[id=DawnGregorDying].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Master, please... I still have so much to learn... You said it yourself..."\nDawn is a fleeting thing; it soon gives way to morning and fades into daylight, with a promise of sunset that will bring about the evening.
   PL: „Mistrzu, przecież powiedział pan, że ma pan jeszcze wiele do nauczenia…”\nŚwit otwierający poranek nie pozostaje na swoim miejscu — zostawia po sobie zachód słońca otwierający wieczór i znika.
120. [Status [DawnFaustDying] — nazwa] 고독한 정오
   źródło: Bufs.json :: dataList[id=DawnFaustDying].name
   kontekst: identyfikator statusu w tekstach: `[DawnFaustDying]`
   limit: do 40 znaków
   EN: Loneliness at High Noon
   PL: Samotne Południe
121. [Status [DawnFaustDying] — opis] - 속도 최솟값 +2\n- 기본 공격 스킬 사용 시 기본 위력 +3, 피해량 +(90/코인수)%\n\n- ‘노을빛 검’에 아래 효과 추가\n· 마지막 코인 적중 시 대상의 화상이 15 이상이면, 대상의 화상 발동. 대상의 화상 횟수 1 감소\n\n- ‘타오르는 일격’에 아래 효과 추가\n· 피해량 +150%\n· 사용 시 모든 코인이 파괴 불가 코인으로 변경됨\n· 적에게 공격 적중 시 대상의 화상 발동. 대상의 화상 횟수 1 감소\n· 사용 시 작열지대를 최대 100 소모하고 소모한 수치 1당, 피해량 +1.5% (최대 150%)\n\n- 이번 턴에 체력이 0이 되는 피해를 받았을 때, 피해로 인한 흐트러짐 상태를 해제하고 해당 턴 동안 체력이 1 미만으로 감소하지 않음 (전투당 1회)\n\n※ 작열지대 효과\n- 해당 장소에서 발생한 화상 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함
   źródło: Bufs.json :: dataList[id=DawnFaustDying].desc
   limit: do 1150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min Speed +2\n- On Base Attack Skill Use: Gain Base Power +3 and deal +(90 / # of Coins)% damage\n\n- Apply the following effects to "Sunset Blade"\n· On final Coin Hit: If target has 15+ Burn, activate Burn on target; then, reduce target's Burn Count by 1\n\n- Apply the following effects to "Blazing Strike"\n· Deal +150% damage\n· On Use: Convert all Coins into Unbreakable Coins\n· On Hit against an enemy, activate Burn on target; then, reduce target's Burn Count by 1\n· On Use: Consume up to 100 Scorchfield and deal +1.5% damage for every Scorchfield consumed (max 150%)\n\n- When this unit takes damage that brings its HP down to 0 this turn, this unit's HP cannot drop below 1 for the turn, and recovers from Stagger when Staggered due to damage (once per Encounter)\n\n* Scorchfield Effects\n- Stores all Burn damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters
   PL: - Minimalna Szybkość +2\n- Przy użyciu bazowej Umiejętności ataku zyskuje Moc Bazową +3 i zadaje +(90 / liczba monet)% obrażeń\n\n- Dodaje następujące efekty do „Ostrza Zachodu Słońca”:\n· Przy trafieniu ostatnią monetą, jeśli cel ma 15 lub więcej Podpalenia, aktywuje Podpalenie celu. Traci 1 Licznik Podpalenia celu\n\n- Dodaje następujące efekty do „Płonącego Ciosu”:\n· Zadaje +150% obrażeń\n· Przy użyciu wszystkie monety stają się Niezniszczalnymi Monetami\n· Przy trafieniu wroga aktywuje Podpalenie celu. Traci 1 Licznik Podpalenia celu\n· Przy użyciu zużywa do 100 Strefy Żaru i zadaje +1,5% obrażeń za każdą zużytą wartość (maks. 150%)\n\n- Gdy w tej turze otrzyma obrażenia, które obniżają HP do 0, dochodzi do siebie z Oszołomienia spowodowanego tymi obrażeniami, a HP nie spada poniżej 1 w tej turze (raz na walkę)\n\n※ Efekty Strefy Żaru\n- Gromadzi wszystkie obrażenia Podpaleniem zadane w tej strefie\n- Resetuje się przy zmianie strefy walki\n- Wartość współdzielona przez wszystkie jednostki
122. [Status [DawnFaustDying] — podsumowanie] 기본 공격 스킬 강화
   źródło: Bufs.json :: dataList[id=DawnFaustDying].summary
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
123. [Status [DawnFaustDying] — tekst klimatyczny] “고독이 무엇인지 아시나요? 떠나버린 사람과는 해가 가장 높이 떴을 때, 더 이상 함께 식사를 할 수 없다는 것… 제게는 그것이 고독이더군요. 되도록… 싱클레어, 당신만큼은 고독이라는 것을 이해할 일이 없길 바라죠.”
   źródło: Bufs.json :: dataList[id=DawnFaustDying].flavor
   limit: do 470 znaków
   EN: "Do you understand what 'loneliness' means, Sinclair? Loneliness is being bathed in the light of the sun at high noon, only to realize that the ones you would have shared a luncheon with have departed you. That is how I would put into words the concept of 'loneliness'—for me, at least. I do hope, Sinclair, that you will never have cause to understand that concept."
   PL: „Czy rozumie pan, czym jest samotność? Samotność to odkrycie, że osoba, która odeszła, nie zasiądzie już z nami do stołu, gdy słońce stoi najwyżej… Dla mnie to właśnie jest samotność. Nade wszystko… Sinclair, oby pan nigdy nie musiał zrozumieć, czym jest samotność.”
124. [Status [DawnTeam] — nazwa] 새벽 사무소
   źródło: Bufs.json :: dataList[id=DawnTeam].name
   kontekst: identyfikator statusu w tekstach: `[DawnTeam]`
   limit: do 40 znaków
   EN: Dawn Office
   PL: Biuro Świtu
125. [Status [DawnTeam] — opis] - 최댓값: 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 턴 시작 시 정신력 5 회복\n- 턴 시작 시 자신을 제외하고 '새벽 사무소'를 보유한 아군 인격이 모두 사망했으면 소멸
   źródło: Bufs.json :: dataList[id=DawnTeam].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 1 Offense Level for every Stack\n- Turn Start: At 3 Stack, heal 5 SP\n- Turn Start: If all other allied Identities that have "Dawn Office" are defeated, expires
   PL: - Maks.: 3\n- Poziom Ataku +1 za każdą wartość\n- Przy 3 wartości na początku tury regeneruje 5 Poczytalności\n- Na początku tury znika, jeśli wszystkie inne sojusznicze osobowości z „Biurem Świtu” poległy
126. [Status [DawnTeam] — tekst klimatyczny] 이 거울세계의 새벽 사무소는 다른 거울세계에 비해 아직 열기가 완전히 식지 않았다. 그렇기에 사무소를 책임지는 두 사람의 전투력은 1급 해결사로 일하기에 부족함이 없는 수준으로 관측된다.\n\n그러나 사무소나 해결사의 등급까지 다른 거울세계와 달라진 것은 아니다. 사무소와 해결사의 등급은 전투력만으로 결정되지 않는다. 의뢰마다 요구되는 기준에 맞춰 일을 제대로 처리하지 못하거나, 등급 상승에 유의미한 영향을 주는 고위험 의뢰를 의도적으로 피한다면, 해결사 등급은 높아질래야 높아질 수 없다.
   źródło: Bufs.json :: dataList[id=DawnTeam].flavor
   limit: do 900 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Dawn Office of this Mirror World, unlike that of others, has yet to completely lose its fervor. One can reasonably conjecture that the two leading Fixers of this Office have sufficient competence to find work as Grade 1 of the vocation.\n\nHowever, it must be stated that the Office and its Fixers' grades do not vary from those of other observed Mirror Worlds, as combat capability is hardly the sole criterion by which the Grades are assigned. Failure to meet the conditions stipulated by the contract clauses to the client's satisfaction, eschewal of high-risk contracts that contribute to the advancement of Fixer Grades—these are all conditions that limit one's mobility along the ladder of Fixer Grades.
   PL: Biuro Świtu tego Świata Zwierciadlanego, w przeciwieństwie do innych, wciąż nie straciło całkiem swojego żaru. Można śmiało przypuszczać, że dwie wiodące postaci tego Biura mają kompetencje wystarczające do pracy na stanowisku Rozwiązującego 1. klasy.\n\nTrzeba jednak zaznaczyć, że klasy Biura i jego Rozwiązujących nie odbiegają od innych obserwowanych Światów Zwierciadlanych, gdyż zdolności bojowe to daleko nie jedyne kryterium nadawania klas. Nieoddanie sprawy zgodnie z warunkami klauzul kontraktu do satysfakcji zleceniodawcy czy umyślne omijanie wysokiego ryzyka, które wpływa na awans klas, uniemożliwiają Rozwiązującym wspinaczkę po drabinie klas.
127. [Status [StigmaWorkshopCelloCaseOne] — nazwa] 불꽃나비의 관
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseOne].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopCelloCaseOne]`
   limit: do 40 znaków
   EN: Fire Butterfly Coffin
   PL: Trumna Ognistych Motyli
128. [Status [StigmaWorkshopCelloCaseOne] — opis] - 최댓값 : 30\n- 턴당 최대 20까지 얻을 수 있음\n- 기본 스킬 적중 시, 수치 2 증가\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseOne].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Can gain up to 20 Stacks per turn\n- On Hit using a Base Skill, gain 2 Stacks\n- Turn End: At 20+ Stacks, gain Burn next turn equal to half of surplus Stacks past 20 (rounded down)\n· At 30 Stacks, gain 5 Burn and +2 Burn Count instead
   PL: - Maks.: 30\n- Można zyskać do 20 wartości na turę\n- Przy trafieniu bazową Umiejętnością zyskuje 2 wartości\n- Na koniec tury, przy ponad 20 wartości, zyskuje w następnej turze Podpalenie równe połowie nadwyżki ponad 20 (zaokrąglona w dół)\n· Przy 30 wartości zamiast tego zyskuje 5 Podpalenia i 2 Liczniki Podpalenia
129. [Status [StigmaWorkshopCelloCaseOne] — podsumowanie] 적중 시, 수치 증가\n수치에 비례하여 다음 턴에 화상 얻음
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseOne].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Stack On Hit, gain Burn next turn based on Stack
   PL: Zyskuje wartości przy trafieniu\nW zależności od wartości zyskuje Podpalenie w następnej turze
130. [Status [StigmaWorkshopCelloCaseOne] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n“싱클레어에겐 아직 이른 무기지만, 특성은 알아두는 게 좋겠죠.”\n“관 속의 여러 칼날은 통상적으로는 단독 수행이 불가능한 순간을 다투는 상황, 혹은 다수를 상대하는 전투에서 높은 편리성을 제공합니다.”
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseOne].flavor
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Heated to a smoldering temperature within the coffin are butterflies, the kaleidoscope spilling forth to melt and tear the target apart.\n\n"This type of weapon is still too premature for you to wield, Sinclair, but it is advisable that you familiarize yourself with its properties."\n\n"The array of blades within the coffin affords considerable convenience in circumstances where time constraints prove solitary handling of requests impossible, or in combat against multiple adversaries."
   PL: W trumnie rozgrzane motyle wydostają się, jakby rzucały się na ofiarę, topiąc ją i rozdzierając.\n„Dla Sinclaira to broń wciąż zbyt wczesna, ale warto poznać jej właściwości.”\n„Rzut ostrzy w trumnie zapewnia dużą wygodę w sytuacjach, gdy czas nie pozwala na samodzielne działanie, lub w walkach z wieloma przeciwnikami.”
131. [Status [StigmaWorkshopCelloCaseTwo] — nazwa] 불꽃나비의 관
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseTwo].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopCelloCaseTwo]`
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Status [StigmaWorkshopCelloCaseTwo] — opis] - 최댓값 : 30\n- 턴당 최대 20까지 얻을 수 있음\n- 기본 스킬 적중 시, 수치 2 증가\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseTwo].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
133. [Status [StigmaWorkshopCelloCaseTwo] — podsumowanie] 적중 시, 수치 증가\n수치에 비례하여 다음 턴에 화상 얻음
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseTwo].summary
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Status [StigmaWorkshopCelloCaseTwo] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n“싱클레어에겐 아직 이른 무기지만, 특성은 알아두는 게 좋겠죠.”\n“관 속의 여러 칼날은 통상적으로는 단독 수행이 불가능한 순간을 다투는 상황, 혹은 다수를 상대하는 전투에서 높은 편리성을 제공합니다.”
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseTwo].flavor
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Status [StigmaWorkshopCelloCaseThree] — nazwa] 불꽃나비의 관
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseThree].name
   kontekst: identyfikator statusu w tekstach: `[StigmaWorkshopCelloCaseThree]`
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Status [StigmaWorkshopCelloCaseThree] — opis] - 최댓값 : 30\n- 턴당 최대 20까지 얻을 수 있음\n- 기본 스킬 적중 시, 수치 2 증가\n- 턴 종료 시 수치가 20을 초과하면, 초과되는 수치의 절반만큼 다음 턴에 화상 얻음 (소수점 버림)\n· 수치가 30이면, 대신 화상 5 얻고 화상 횟수 2 증가
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseThree].desc
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Status [StigmaWorkshopCelloCaseThree] — podsumowanie] 적중 시, 수치 증가\n수치에 비례하여 다음 턴에 화상 얻음
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseThree].summary
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Status [StigmaWorkshopCelloCaseThree] — tekst klimatyczny] 관 속에서 달궈진 나비들이, 덮치듯 나와 대상을 녹이고 찢어 놓는다.\n“싱클레어에겐 아직 이른 무기지만, 특성은 알아두는 게 좋겠죠.”\n“관 속의 여러 칼날은 통상적으로는 단독 수행이 불가능한 순간을 다투는 상황, 혹은 다수를 상대하는 전투에서 높은 편리성을 제공합니다.”
   źródło: Bufs.json :: dataList[id=StigmaWorkshopCelloCaseThree].flavor
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [Status [Firstlight] — nazwa] 전투 감각
   źródło: Bufs.json :: dataList[id=Firstlight].name
   kontekst: identyfikator statusu w tekstach: `[Firstlight]`
   limit: do 40 znaków
   EN: Battle Instinct
   PL: Wyczucie Walki
140. [Status [Firstlight] — opis] - 최댓값 : 3\n- 속도 최솟값, 최댓값 +2\n- 적에게 기본 스킬로 부여하는 화상 위력과 화상 횟수 부여값 +1\n- 스킬 ‘사출’ 피해량 +(수치 x 5)%\n- 스킬 ‘사출-정오‘, ‘정오의 해체’ 피해량 +(수치 x 10)%
   źródło: Bufs.json :: dataList[id=Firstlight].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Min & Max Speed +2\n- Base Skills inflict +1 more Burn Potency and Burn Count on enemies\n- Skill "Eject" deals +(Stack x 5)% damage\n- Skills "Eject - High Noon" and "Dismemberment at High Noon" deal +(Stack x 10)% damage
   PL: - Maks.: 3\n- Minimalna i maksymalna Szybkość +2\n- Bazowe Umiejętności nadają wrogom o 1 więcej Mocy i Liczników Podpalenia\n- Umiejętność „Wystrzelenie” zadaje +(wartość x 5)% obrażeń\n- Umiejętności „Wystrzelenie - Południe” i „Rozłożenie o Południu” zadają +(wartość x 10)% obrażeń
141. [Status [Firstlight] — podsumowanie] 사출, 사출-정오, 정오의 해체 스킬 피해량 증가
   źródło: Bufs.json :: dataList[id=Firstlight].summary
   limit: do 120 znaków
   EN: Deal more damage using "Eject", "Eject - High Noon", "Dismemberment at High Noon"
   PL: Zadaje więcej obrażeń Umiejętnościami „Wystrzelenie”, „Wystrzelenie - Południe” i „Rozłożenie o Południu”
142. [Status [Firstlight] — tekst klimatyczny] “본론으로 돌아가자면, 특이점을 제외하고도 장비로 인해 발생하는 페널티를 극복할 수 있는 확실한 방법이 하나 있답니다. 그게 바로 노력이죠.”\n“진부한 이야기처럼 들릴 순 있지만, 쉬는 시간에도 의뢰를 해결할 때도 기초적인 체력 단련과 전투에 대한 센스를 갈고 닦는 걸 추천드립니다.”\n“물론 전투에 대한 감각은 대부분 전투가 무르익어서야 온전히 그 능력을 발휘합니다. 소위 말하는 예열이 필요하죠. 그렇게 고조된 전투 감각은 장비와 기술이 가진 구조적인 허점을 보완해 줍니다. 싱클레어, 당신의 저점을 높일 방법이죠. 이해가 되시나요?”
   źródło: Bufs.json :: dataList[id=Firstlight].flavor
   limit: do 990 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "To resume the subject at hand: aside from Singularities, there exists a means of overcoming the penalties incurred by using this type of weaponry. Namely, effort."\n\n"This may go without saying, but it is recommended that you focus on honing your body and battle instinct whenever time permits—both during downtime and when handling requests."\n\n"Granted, battle instinct, in most cases, can only be properly demonstrated in the heat of battle. One might refer to this process as a "warm up," although that term is perhaps <i>too</i> simple. In any case, a heightened natural battle instinct will help you offset the gear's structural and technical vulnerabilities. This is how you may raise the baseline of your performance threshold. Are you able to comprehend this explanation, Sinclair?"
   PL: „Wracając do sedna: poza osobliwościami istnieje jeden pewny sposób na pokonanie kar związanych z takim wyposażeniem. To ciężka praca.”\n„Może brzmi banalnie, ale polecam doszlifować podstawową kondycję i wyczucie walki zarówno w wolnym czasie, jak i przy zleceniach.”\n„Oczywiście wyczucie walki w większości przypadków ujawnia się dopiero, gdy walka się rozkręci. Potrzebna jest tak zwana rozgrzewka. Podniesione w ten sposób wyczucie walki uzupełnia luki strukturalne sprzętu i techniki. To sposób na podniesienie twojego minimum, Sinclair. Zrozumiał pan?”
143. [Status [CaseOverheating] — nazwa] 과열된 관
   źródło: Bufs.json :: dataList[id=CaseOverheating].name
   kontekst: identyfikator statusu w tekstach: `[CaseOverheating]`
   limit: do 40 znaków
   EN: Overheated Coffin
   PL: Przegrzana Trumna
144. [Status [CaseOverheating] — opis] - 최댓값 : 1\n- 턴 종료 시, 다음 턴에 화상 3 얻고 사라짐
   źródło: Bufs.json :: dataList[id=CaseOverheating].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End:\n· Gain 3 Burn next turn\n· This effect expires
   PL: - Maks.: 1\n- Na koniec tury zyskuje w następnej turze 3 Podpalenia, po czym znika
145. [Status [CaseOverheating] — tekst klimatyczny] “하지만 편리함에는 늘 대가가 따르기 마련입니다. 통상적인 형태의 스티그마 공방 무기에는 없을 구조적인 페널티가 생기고 말죠. 이 필연적인 페널티를 극복할 수 있도록 하는 것이 도시 기술의 정점에 있는 특이점입니다.”\n“특이점이 얼마나 대단한지 아시겠… 크흠. 이야기가 샜군요.”
   źródło: Bufs.json :: dataList[id=CaseOverheating].flavor
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Keep in mind, however, that convenience is always accompanied by a trade-off. A weapon of this structure comes with drawbacks that standard Stigma Workshop weapons would not possess—inevitable penalties that can only be mitigated by Singularities, the pinnacle of the myriad technological innovations of the City."\n\n"It would do justice to properly acknowledge the extraordinary qualities of Singulari—ahem. That was tangential to the subject. Let us return to the subject, Sinclair."
   PL: „Lecz wygoda zawsze wiąże się z pewną ceną. Broń o takiej konstrukcji ma wady strukturalne, jakich nie posiadają zwykłe bronie pracowni Stigmy — kary, których pokonać mogą tylko osobliwości, szczyt technologii Miasta.”\n„To zasługuje na odpowiednie docenienie jakości osobliwośc… hmm. Trochę odbiegłem od tematu.”
146. [Status [DriftingDimensionYisang] — nazwa] 차원 표류
   źródło: Bufs.json :: dataList[id=DriftingDimensionYisang].name
   kontekst: identyfikator statusu w tekstach: `[DriftingDimensionYisang]`
   limit: do 40 znaków
   EN: Dimensional Castaway
   PL: Dryf Wymiarowy
147. [Status [DriftingDimensionYisang] — opis] 최댓값 : 3\n피격 직전, 최대 체력의 (수치)%만큼 보호막 얻음 (턴당 최대 3회)
   źródło: Bufs.json :: dataList[id=DriftingDimensionYisang].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nBefore Getting Hit, gain Shield equal to (Stack)% HP (3 times per turn)
   PL: Maks.: 3\nPrzed otrzymaniem trafienia zyskuje Tarczę równą (wartość)% maks. HP (do 3 razy na turę)
148. [Status [FourDimensionYisang] — nazwa] 사색 차원
   źródło: Bufs.json :: dataList[id=FourDimensionYisang].name
   kontekst: identyfikator statusu w tekstach: `[FourDimensionYisang]`
   limit: do 40 znaków
   EN: Quadricolor Dimensions
   PL: Czterobarwne Wymiary
149. [Status [FourDimensionYisang] — opis] - 최댓값 : 4\n- 수치당 아래 효과 얻음\n· 1 ~ : 공격 레벨 +1\n· 2 ~ : 방어 레벨 +2\n· 3 ~ : 자신의 스킬로 얻는 충전 횟수 +1\n· 4 ~ : 자신의 스킬 피해량 +(충전 위력 x 4)% (최대 20%)\n\n- 이 효과의 최대치를 초과하여 얻으면, 초과값만큼 다음 턴에 얻음\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=FourDimensionYisang].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Gain the following effects based on Stack:\n· 1+: Offense Level +1\n· 2+: Defense Level +2\n· 3+: Gain +1 more Charge Count from this unit's Skills\n· 4+: This unit's Skills deal +(Charge Potency x 4)% damage (max 20%)\n\n- If this unit gains this effect past its max cap, this unit gains the surplus Stack next turn\n- Turn End: Lose 1 Stack
   PL: - Maks.: 4\n- Zyskuje następujące efekty zależnie od wartości:\n· 1 lub więcej: Poziom Ataku +1\n· 2 lub więcej: Poziom Obrony +2\n· 3 lub więcej: zyskuje o 1 więcej Liczników Ładowania z własnych Umiejętności\n· 4 lub więcej: Umiejętności zadają +(Moc Ładowania x 4)% obrażeń (maks. 20%)\n\n- Przy zyskaniu ponad maksimum zyskuje nadwyżkę w następnej turze\n- Na koniec tury maleje o 1
150. [Status [DianxueHongLu] — nazwa] 점혈 - 홍루
   źródło: Bufs.json :: dataList[id=DianxueHongLu].name
   kontekst: identyfikator statusu w tekstach: `[DianxueHongLu]`
   limit: do 40 znaków
   EN: Nerve Strike - Hong Lu
   PL: Punkt Witalny - Hong Lu
151. [Status [DianxueHongLu] — opis] - 최댓값 : 3\n- 점혈을 부여한 캐릭터가 대상(또는 부위)의 점혈 수치에 따라 다음 효과를 얻음\n· 1스택 : 합 위력 +1\n· 2스택 : 기본 위력 +1\n· 3스택 : 합 위력 +1, 기본 위력 +1\n- 부여한 캐릭터가 다른 대상(또는 부위)에게 이 효과를 부여하면 소멸\n- 다른 캐릭터의 점혈이 부여될 경우, 교체됨 (수치 유지)
   źródło: Bufs.json :: dataList[id=DianxueHongLu].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- The unit that inflicted this Nerve Strike gains the following effects based on target's (or targeted Part's) Nerve Strike Stack\n· 1x Stack: Gain Clash Power +1\n· 2x Stack: Gain Base Power +1\n· 3x Stack: Gain Clash Power +1 and Base Power +1\n- Expires if the unit that inflicted it inflicts this effect against a different target (or a different Part)\n- Replaced when another unit inflicts Nerve Strike (Stacks are preserved)
   PL: - Maks.: 3\n- Jednostka, która nadała Punkt Witalny, zyskuje następujące efekty zależnie od wartości Punktu Witalnego celu (lub części):\n· 1 stos: Moc Starcia +1\n· 2 stosy: Moc Bazowa +1\n· 3 stosy: Moc Starcia +1 i Moc Bazowa +1\n- Znika, gdy nadający nada ten efekt innemu celowi (lub innej części)\n- Zastępowany, gdy inna jednostka nada Punkt Witalny (wartość zachowana)
152. [Status [DuelSousTemoinsEast] — nazwa] 입회 - 동부 섕크
   źródło: Bufs.json :: dataList[id=DuelSousTemoinsEast].name
   kontekst: identyfikator statusu w tekstach: `[DuelSousTemoinsEast]`
   limit: do 40 znaków
   EN: Witnessed - Eastern Cinq
   PL: Przy Świadkach - Wschodni Cinq
153. [Status [DuelSousTemoinsEast] — opis] - 최댓값: 3\n- 공격 레벨 +(수치)\n- 수치가 2 이상이면, 기본 스킬의 호흡 위력 획득값 +1\n- 수치가 3 이상이면, 기본 스킬의 호흡 횟수 획득값 +1
   źródło: Bufs.json :: dataList[id=DuelSousTemoinsEast].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +(Stack)\n- At 2+ Stack, Base Skills gain +1 more Poise Potency\n- At 3+ Stack, Base Skills gain +1 more Poise Count
   PL: - Maks.: 3\n- Poziom Ataku +(wartość)\n- Przy 2+ wartości bazowe Umiejętności zyskują o 1 więcej Mocy Oddechu\n- Przy 3+ wartości bazowe Umiejętności zyskują o 1 więcej Liczników Oddechu
154. [Status [NoirSuitAlly] — nazwa] 르누아르 개버딘 원단 코트
   źródło: Bufs.json :: dataList[id=NoirSuitAlly].name
   kontekst: identyfikator statusu w tekstach: `[NoirSuitAlly]`
   limit: do 40 znaków
   EN: Le Noir: Gabardine Overcoat
   PL: Le Noir: Płaszcz z Gabardyny
155. [Status [NoirSuitAlly] — opis] - 최댓값 : 100\n- 수치 25당, 방어 레벨 +1\n- 가장 왼쪽 슬롯의 도발치 +5\n- 보호막이 있는 상태에서 피격 시, 5 증가 (턴당 최대 10)\n- 턴 종료 시 보호막이 남아있으면, 10 증가\n- 자신의 스킬, 패시브 효과로 보존 횟수를\n· 획득 시, 획득한 수치만큼 증가 (보존 횟수 최대치를 초과하여 얻는 수치 포함)\n· 소모 시, (소모한 수치 x 2)만큼 증가\n· 이 효과로 턴당 최대 30 획득 가능\n- 수치가 100이 되면, 다음 턴에 아르뮈르 에비이예로 변경됨
   źródło: Bufs.json :: dataList[id=NoirSuitAlly].desc
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Defense Level +1 for every 25 Stacks\n- Gain +5 Aggro to the leftmost Slot\n- When hit while this unit has Shield, gain 5 Stacks (10 per turn)\n- Turn End: If this unit has remaining Shield, gain 10 Stacks\n- Apply the following when this unit gains or consumes Preservation Count due to its Skill or Passive effects:\n · Gain Stack equal to Preservation Count gained (this effect's Stack is gained regardless of Preservation's max Count)\n · Gain Stack equal to (Preservation Count consumed x 2)\n · Can gain up to 30 Stacks per turn via this effect\n- At 100 Stacks, convert this effect into Armure Éveillée next turn
   PL: - Maks.: 100\n- Poziom Obrony +1 za każde 25 wartości\n- Wartość Prowokacji skrajnie lewego slotu +5\n- Przy trafieniu posiadając Tarczę zyskuje 5 wartości (do 10 na turę)\n- Na koniec tury, jeśli pozostała Tarcza, zyskuje 10 wartości\n- Zyskując lub zużywając Liczniki Zachowania przez własne Umiejętności lub Pasywy:\n· przy zysku rośnie o zyskaną wartość (łącznie z wartością ponad maksimum Liczników Zachowania)\n· przy zużyciu rośnie o (zużyta wartość x 2)\n· przez ten efekt można zyskać do 30 wartości na turę\n- Przy 100 wartości przekształca się w następnej turze w „Armure Éveillée”
156. [Status [NoirSuitAlly] — podsumowanie] 방어 레벨과 도발치 증가
   źródło: Bufs.json :: dataList[id=NoirSuitAlly].summary
   limit: do 120 znaków
   EN: Gain Defense Level and Aggro
   PL: Poziom Obrony i Wartość Prowokacji rosną
157. [Status [NoirSuitAlly] — tekst klimatyczny] 경사가 위사보다 훨씬 많도록 트윌하여 만든 코트.\n특유의 높은 밀도로 착용자를 외부로부터 보호한다.
   źródło: Bufs.json :: dataList[id=NoirSuitAlly].flavor
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An overcoat made from twill fabric, a type of weave made by threading several weft threads over fewer warp threads.\nIts characteristic high-density weave protects its wearer from external trauma.
   PL: Płaszcz utkany techniką twill, tak by wątku było znacznie więcej niż osnowy.\nJego charakterystyczna wysoka gęstość chroni noszącego przed urazami z zewnątrz.
158. [Status [ChargeNoirAlly] — nazwa] 보존
   źródło: Bufs.json :: dataList[id=ChargeNoirAlly].name
   kontekst: identyfikator statusu w tekstach: `[ChargeNoirAlly]`
   limit: do 40 znaków
   EN: Preservation
   PL: Zachowanie
159. [Status [ChargeNoirAlly] — opis] - 특수 충전\n- 횟수 최댓값 : 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료 시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs.json :: dataList[id=ChargeNoirAlly].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count\n\n<color=#1aece7>Cumulative Count consumed: {2}</color>
   PL: - Szczególne Ładowanie\n- Maks. Licznika: 20\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Ładowania\n- Na koniec tury Licznik maleje o 1\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
160. [Status [ChargeNoirAlly] — podsumowanie] 특수 충전
   źródło: Bufs.json :: dataList[id=ChargeNoirAlly].summary
   limit: do 120 znaków
   EN: Unique Charge
   PL: Szczególne Ładowanie
161. [Status [ChargeNoirAlly] — tekst klimatyczny] 응축하여 힘을 모아 고정한다. 변화시키지 않는 것이 변화시키는 것보다 더 큰 힘이 필요할 때가 있다.
   źródło: Bufs.json :: dataList[id=ChargeNoirAlly].flavor
   limit: do 160 znaków
   EN: Force is compressed, gathered, and fixed in place. Sometimes, it takes more force to prevent change than to cause it.
   PL: Siła jest kondensowana, zbierana i umacniana. Czasem potrzeba więcej siły, by powstrzymać zmianę, niż ją wywołać.
162. [Status [RealisationAlly] — nazwa] 아르뮈르 에비이예
   źródło: Bufs.json :: dataList[id=RealisationAlly].name
   kontekst: identyfikator statusu w tekstach: `[RealisationAlly]`
   limit: do 40 znaków
   EN: Armure Éveillée
   PL: Armure Éveillée
163. [Status [RealisationAlly] — opis] - 최댓값 : 100\n- 속도 최솟값 +2, 최댓값 +2\n- 수치 25당, 공격 레벨 +1, 방어 레벨 +1\n- 모든 기본 공격 스킬이 파괴 불가 코인으로 변경됨\n- 턴 시작 시, 정신력 8 회복\n- 수치가 0이 되면, 르누아르 개버딘 원단 코트로 변경됨
   źródło: Bufs.json :: dataList[id=RealisationAlly].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Min & Max Speed +2\n- Offense Level +1 and Defense Level +1 for every 25 Stacks\n- Convert all Base Attack Skill Coins into Unbreakable Coins\n- Turn Start: Heal 8 SP\n- At 0 Stacks, convert this effect into "Le Noir: Gabardine Overcoat"
   PL: - Maks.: 100\n- Minimalna i maksymalna Szybkość +2\n- Poziom Ataku +1 i Poziom Obrony +1 za każde 25 wartości\n- Wszystkie monety bazowych Umiejętności ataku stają się Niezniszczalnymi Monetami\n- Na początku tury regeneruje 8 Poczytalności\n- Przy 0 wartości przekształca się w „Le Noir: Płaszcz z Gabardyny”
164. [Status [RealisationAlly] — podsumowanie] 공격 레벨, 방어 레벨, 속도 증가\n기본 공격 스킬이 파괴 불가 코인으로 변경
   źródło: Bufs.json :: dataList[id=RealisationAlly].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Offense Level, Defense Level, and Speed\nConvert Base Attack Skill Coins into Unbreakable Coins
   PL: Poziom Ataku, Poziom Obrony i Szybkość rosną\nMonety bazowych Umiejętności ataku stają się Niezniszczalnymi Monetami
165. [Status [RealisationAlly] — tekst klimatyczny] 외부에서 가해진 힘이 착용자에게 도달하지 못하게 한 르누아르의 원단은, 최종적으로 외부로부터의 변화를 제거하기 위해 깨어난다.\n축적한 에너지를 방출하여 외부 요인을 제거하는 방향으로 작동한다.
   źródło: Bufs.json :: dataList[id=RealisationAlly].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Le Noir's fabric weave prevents external force from reaching its wearer. The purpose for which it awakens is to eliminate change imposed from the outside.\nThe fabric stores energy from attacks it absorbs, then expels all that force in a single burst to remove the external source of change.
   PL: Tkanina Le Noir nie pozwalała, by siła z zewnątrz docierała do noszącego. Ostatecznie przebudza się ona, by wyeliminować zmiany naciskające z zewnątrz.\nGromadzi energię z pochłoniętych ataków, by jednym wybuchem wyprzeć całą siłę i usunąć zewnętrzne źródło zmiany.
166. [Status [ChargeRougeAlly] — nazwa] 맥동
   źródło: Bufs.json :: dataList[id=ChargeRougeAlly].name
   kontekst: identyfikator statusu w tekstach: `[ChargeRougeAlly]`
   limit: do 40 znaków
   EN: Pulsation
   PL: Pulsacja
167. [Status [ChargeRougeAlly] — opis] - 특수 충전\n- 횟수 최댓값: 20\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs.json :: dataList[id=ChargeRougeAlly].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Unique Charge\n- Max Count: 20\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count\n\n<color=#1aece7>Cumulative Count consumed: {2}</color>
   PL: - Szczególne Ładowanie\n- Maks. Licznika: 20\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Ładowania\n- Na koniec tury Licznik maleje o 1\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
168. [Status [RougeIshmaelCocoon] — nazwa] 탈의실
   źródło: Bufs.json :: dataList[id=RougeIshmaelCocoon].name
   kontekst: identyfikator statusu w tekstach: `[RougeIshmaelCocoon]`
   limit: do 40 znaków
   EN: Changing Room
   PL: Przebieralnia
169. [Status [RougeIshmaelCocoon] — opis] - 최댓값 : 2\n- 속도가 1로 고정됨 \n- 스킬로 받는 피해량 -50%\n- 획득 즉시 흐트러짐 선을 제거 및 흐트러짐 상태일 때 흐트러짐을 해제함\n- 턴 시작시, 도발치 10 얻음\n- 피격 시, 맥동 횟수 1 얻음 (턴당 최대 20회)\n- 턴 종료시 1 감소\n- 퇴각 불가\n- E.G.O 침식 상태가 되지 않고 기본 패닉 상태가 됨 (패닉 변경 효과는 적용 받을 수 있음)\n- 이 상태일 때 ‘목소리에 따라 기꺼이 나의 안으로’가 아닌 수비 스킬을 장착하거나 E.G.O 스킬을 장착할 수 없음
   źródło: Bufs.json :: dataList[id=RougeIshmaelCocoon].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Fix this unit's Speed to 1\n- Take -50% damage from Skills\n- Immediately after gaining this effect, remove Stagger Thresholds; when Staggered, recover from Stagger\n- Turn Start: Gain 10 Aggro\n- When hit, gain +1 Pulsation Count (20 times per turn)\n- Turn End: Lose 1 Stack\n- Cannot Retreat\n- Cannot enter E.G.O Corrosion; instead, enters default Panic state (is affected by Panic-changing effects)\n- While in this state, aside from its exclusive Skill "As the Voice Says, I Gladly Withdraw into Myself", cannot equip Defense Skills or E.G.O Skills
   PL: - Maks.: 2\n- Szybkość zostaje ustalona na 1\n- Otrzymuje -50% obrażeń od Umiejętności\n- Przy zyskaniu tego efektu natychmiast usuwa Progi Oszołomienia, a będąc Oszołomioną, dochodzi do siebie\n- Na początku tury zyskuje 10 Wartości Prowokacji\n- Przy trafieniu zyskuje 1 Licznik Pulsacji (do 20 razy na turę)\n- Na koniec tury maleje o 1\n- Nie może się wycofać\n- Nie wchodzi w Korozję E.G.O; zamiast tego wchodzi w podstawowy stan Paniki (może podlegać efektom zmiany Paniki)\n- W tym stanie nie można wyposażyć Umiejętności Obrony ani Umiejętności E.G.O poza wyłączną Umiejętnością „Jak Głos Przykaże, Radośnie Wstępuję w Głąb Siebie”
170. [Status [RougeIshmaelCocoon] — tekst klimatyczny] 단단해지더라도 수동적이다. 수동적인 것은 아무리 단단하더라도, 르루주적인 관점에선 취약한 것이다.\n하지만 변화를 위해선 잠시 멈춰야할 필요가 있다. 그래서 이 과정은 괴롭다.
   źródło: Bufs.json :: dataList[id=RougeIshmaelCocoon].flavor
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Though it has become hardier, it has now become passive. When viewed through the lens of Le Rouge, however durable something might have become, what is passive is always fragile.\n\nBut one must first come to a halt in order to usher in change. And that is what makes this process painful.
   PL: Choć twardsza, stała się bierna. Z punktu widzenia Le Rouge, jednakowa twardość w bierności zawsze jest krucha.\nAle by nastąpiła zmiana, najpierw trzeba się na chwilę zatrzymać. Dlatego ten proces jest bolesny.
171. [Status [RougeIshmaelEclose] — nazwa] 새단장
   źródło: Bufs.json :: dataList[id=RougeIshmaelEclose].name
   kontekst: identyfikator statusu w tekstach: `[RougeIshmaelEclose]`
   limit: do 40 znaków
   EN: Full Makeover
   PL: Nowe Szaty
172. [Status [RougeIshmaelEclose] — opis] - 속도 최솟값, 최댓값 +1\n- 최대 체력의 25%만큼 체력 증가\n- 스킬로 받는 피해량 -10%\n- 기본 스킬로 적에게 부여하는 출혈 위력 부여량 +1
   źródło: Bufs.json :: dataList[id=RougeIshmaelEclose].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Max HP increased by 25%\n- Take -10% damage from Skills\n- Base Skills inflict +1 more Bleed Potency on enemies
   PL: - Minimalna i maksymalna Szybkość +1\n- Maks. HP rośnie o 25%\n- Otrzymuje -10% obrażeń od Umiejętności\n- Bazowe Umiejętności nadają wrogom o 1 więcej Mocy Krwawienia
173. [Status [RougeIshmaelEclose] — tekst klimatyczny] 고치에서 나왔지만, 그 속에서 진정으로 자신을 녹이고 재구성하지 못하여, 진실된 변화를 이루어내진 못했다. 그래도 기존의 옷이 강화되어 신체적인 능력은 향상되었다.
   źródło: Bufs.json :: dataList[id=RougeIshmaelEclose].flavor
   limit: do 260 znaków
   EN: Though she has emerged from the cocoon, she has failed to truly metamorphose—as that process involves the disintegration of the self. Still, the process has managed to boost her physical abilities.
   PL: Choć wyszła z kokonu, nie zdołała w nim prawdziwie rozpuścić i przebudować siebie, więc prawdziwa przemiana się nie dokonała. Mimo to ubranie zostało wzmocnione, a jej zdolności fizyczne wzrosły.
174. [Status [EmpathicDistressAlly] — nazwa] 감각 균열
   źródło: Bufs.json :: dataList[id=EmpathicDistressAlly].name
   kontekst: identyfikator statusu w tekstach: `[EmpathicDistressAlly]`
   limit: do 40 znaków
   EN: Fracturing of the Senses
   PL: Pęknięcie Zmysłów
175. [Status [EmpathicDistressAlly] — opis] - 최댓값: 5\n- 자신을 제외한 아군 피격 시 자신의 진동 횟수가 1 증가하고, 이 효과 수치 1 감소 (스킬당 1회)\n- 자신을 제외한 아군이 없으면, 피격 시 자신이 진동 위력을 2 얻고, 이 효과 수치 1 감소 (스킬당 1회)\n- 크리티컬 공격으로 피격 시, 받는 피해량 +(자신의 진동 위력)% (최대 15%)
   źródło: Bufs.json :: dataList[id=EmpathicDistressAlly].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- When other allies are hit, gain +1 Tremor Count, and lose 1 Stack (once per Skill)\n- If there are no other allies on the field, gain 2 Tremor Potency when hit, and lose 1 Stack (once per Skill)\n- When hit by Crit Attack, take +(Tremor Potency on self)% damage (max 15%)
   PL: - Maks.: 5\n- Gdy trafiony zostanie sojusznik poza tą jednostką, zyskuje 1 Licznik Wstrząsu i traci 1 wartości (raz na Umiejętność)\n- Gdy nie ma innych sojuszników, przy trafieniu zyskuje 2 Mocy Wstrząsu i traci 1 wartości (raz na Umiejętność)\n- Przy trafieniu atakiem krytycznym otrzymuje +(własna Moc Wstrząsu)% obrażeń (maks. 15%)
176. [Status [EmpathicDistressAlly] — tekst klimatyczny] 마음의 모습과 육체의 모습의 다름을 알 때 균열이 생긴다.
   źródło: Bufs.json :: dataList[id=EmpathicDistressAlly].flavor
   limit: do 140 znaków
   EN: The fracturing occurs when one first recognizes the incongruity between the forms of the body and the heart.
   PL: Pęknięcie pojawia się, gdy uświadomisz sobie odmienność między kształtem serca a kształtem ciała.
177. [Status [PersonalityVibration] — nazwa] 진동 인격
   źródło: Bufs.json :: dataList[id=PersonalityVibration].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityVibration]`
   limit: do 40 znaków
   EN: Tremor ID
   PL: Wstrząsowa Osobowość
178. [Status [PersonalityVibration] — opis] 진동 위력, 진동 횟수 또는 특수 진동을 부여하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityVibration].desc
   limit: do 130 znaków
   EN: Identities that have Base Attack Skills that inflict Tremor Potency, Tremor Count, or Unique Tremor
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające Moc Wstrząsu, Licznik Wstrząsu lub Szczególny Wstrząs
179. [Status [PersonalityBreath] — nazwa] 호흡 인격
   źródło: Bufs.json :: dataList[id=PersonalityBreath].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityBreath]`
   limit: do 40 znaków
   EN: Poise ID
   PL: Osobowość Oddechu
180. [Status [PersonalityBreath] — opis] 호흡 위력, 호흡 횟수를 부여하거나 얻는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityBreath].desc
   limit: do 120 znaków
   EN: Identities that have Base Attack Skills that apply or gain Poise Potency or Poise Count
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające lub zyskujące Moc Oddechu lub Licznik Oddechu
181. [Status [PersonalityCharge] — nazwa] 충전 인격
   źródło: Bufs.json :: dataList[id=PersonalityCharge].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityCharge]`
   limit: do 40 znaków
   EN: Charge ID
   PL: Osobowość Ładowania
182. [Status [PersonalityCharge] — opis] 충전 또는 특수 충전을 부여하거나 얻거나 소모하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityCharge].desc
   limit: do 120 znaków
   EN: Identities that have Base Attack Skills that apply, gain, or consume Charge or Unique Charge
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające, zyskujące lub zużywające Ładowanie lub Szczególne Ładowanie
183. [Status [ChargeKhakiAlly] — nazwa] 표류 관성
   źródło: Bufs.json :: dataList[id=ChargeKhakiAlly].name
   kontekst: identyfikator statusu w tekstach: `[ChargeKhakiAlly]`
   limit: do 40 znaków
   EN: Inertia of Drifting
   PL: Bezwładność Dryfu
184. [Status [ChargeKhakiAlly] — opis] - 횟수 최댓값 : 20\n- 특수 충전\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음\n- 턴 종료시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs.json :: dataList[id=ChargeKhakiAlly].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Max Count: 20\n- Unique Charge\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count\n\n<color=#1aece7>Cumulative Count consumed: {2}</color>
   PL: - Maks. Licznika: 20\n- Szczególne Ładowanie\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Ładowania\n- Na koniec tury Licznik maleje o 1\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
185. [Status [ChargeKhakiAlly] — tekst klimatyczny] 표류하는 자들은 흐름을 바꿀 수는 없어도 흐름을 공고히 하고 흐름 속에서 자신의 일을 한다.
   źródło: Bufs.json :: dataList[id=ChargeKhakiAlly].flavor
   limit: do 210 znaków
   EN: Those who are carried by the tide like buoys may not be able to change the flow of things, but they can still bolster the tide and commit to their acts within.
   PL: Dryfujący nie mogąc zmienić prądu, umacniają go i wykonują swoje dzieło w jego obrębie.
186. [Status [NoirScissorAlly] — nazwa] 마름질 표식
   źródło: Bufs.json :: dataList[id=NoirScissorAlly].name
   kontekst: identyfikator statusu w tekstach: `[NoirScissorAlly]`
   limit: do 40 znaków
   EN: Mark of Shearing
   PL: Znak Wykrawania
187. [Status [NoirScissorAlly] — opis] - 최댓값 : 4\n- 이 효과를 보유한 대상이 사망 시, 이 효과 부여자가 정신력을 5 회복하고 다음 턴에 공격 레벨 증가 1 얻음 (턴당 3회)
   źródło: Bufs.json :: dataList[id=NoirScissorAlly].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- When a target that has this effect is defeated, the unit that inflicted this effect heals 5 SP and gains 1 Offense Level Up next turn (3 times per turn)
   PL: - Maks.: 4\n- Po śmierci jednostki posiadającej ten efekt nadający regeneruje 5 Poczytalności i zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)
188. [Status [NoirScissorAlly] — tekst klimatyczny] 옷감이나 재목 따위를 치수에 맞게 베어 내기 위한 표식
   źródło: Bufs.json :: dataList[id=NoirScissorAlly].flavor
   limit: do 120 znaków
   EN: A cutting mark used to trim fabric and other materials to the required measurements.
   PL: Znak służący do wycinania tkanin i innych materiałów według właściwych wymiarów.
189. [Status [NoirScissorCut] — nazwa] 꽃가위
   źródło: Bufs.json :: dataList[id=NoirScissorCut].name
   kontekst: identyfikator statusu w tekstach: `[NoirScissorCut]`
   limit: do 40 znaków
   EN: Blossom Scissors
   PL: Kwiatowe Nożyczki
190. [Status [NoirScissorCut] — opis] - 최댓값 : 2\n- 수치당 가하는 피해량 +7%
   źródło: Bufs.json :: dataList[id=NoirScissorCut].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Deal +7% damage for every Stack
   PL: - Maks.: 2\n- Zadaje +7% obrażeń za każdą wartość
191. [Status [NoirScissorCut] — tekst klimatyczny] 지하에서 만들어진 원초의 재료를 끊어 내기 위한 가위는 더욱 특별하고 거대하다. 처음으로 직조된 천을 자르고 잘라 왔던 이 가위에서 꽃이 피어나는 건 근원을 잘라 왔기 때문이며, 자연스러운 현상이다.
   źródło: Bufs.json :: dataList[id=NoirScissorCut].flavor
   limit: do 370 znaków
   EN: The scissors used to sever the primordial materials produced underground are larger and more extraordinary still. These scissors have cut and recut the very first cloth ever woven. That flowers should bloom from them is only natural, for they have always cut things at their very roots.
   PL: Nożyczki służące do odcięcia pierwotnych materiałów powstałych pod ziemią są jeszcze bardziej szczególne i ogromne. To one tnęły i przycinały pierwszą utkaną tkaninę. Kwiaty kwitną na nich dlatego, że odcięły w samym źródle — to zjawisko naturalne.
192. [Status [SupportAlly] — nazwa] 양극성
   źródło: Bufs.json :: dataList[id=SupportAlly].name
   kontekst: identyfikator statusu w tekstach: `[SupportAlly]`
   limit: do 40 znaków
   EN: Duality
   PL: Dwubiegunowość
193. [Status [SupportAlly] — opis] 아군 인격을 스킬 대상으로 지정할 수 있음\n스킬 자동 지정 시 또는 일반 전투인 경우, 편성 순서가 가장 빠른 아군을 우선 지정\n- 대상이 아군이면, 공격이 적중하지 않고 수비 스킬을 발동시키지 않음 (합가능 수비 포함)\n아군을 지정했으면, 전투 시작시 스킬 발동
   źródło: Bufs.json :: dataList[id=SupportAlly].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skills can target allied Identities\nUpon auto-targeting Skills, or in Regular Encounters, prioritize the ally with the earliest Deployment Order\n- If target is an ally, the attack does not hit, and does not trigger Defense Skills (including Clashable Defense Skills)\nIf target is an ally, activate this Skill at Combat Start
   PL: Umiejętności mogą namierzać sojusznicze osobowości\nPrzy automatycznym namierzaniu Umiejętności lub w zwykłych walkach priorytet ma sojusznik z najwcześniejszą kolejnością rozmieszczenia\n- Jeśli celem jest sojusznik, atak nie trafia i nie wywołuje Umiejętności Obrony (łącznie z obroną zdatną do Starcia)\nJeśli namierzono sojusznika, Umiejętność aktywuje się na początku walki
194. [Status [SupportEnemy] — nazwa] 양극성
   źródło: Bufs.json :: dataList[id=SupportEnemy].name
   kontekst: identyfikator statusu w tekstach: `[SupportEnemy]`
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Status [SupportEnemy] — opis] 아군을 스킬 대상으로 지정할 수 있음\n스킬 자동 지정 시 또는 일반 전투인 경우, 무작위 아군을 지정\n- 대상이 아군이면, 공격이 적중하지 않고 수비 스킬을 발동시키지 않음 (합가능 수비 포함)\n아군을 지정했으면, 전투 시작시 스킬 발동
   źródło: Bufs.json :: dataList[id=SupportEnemy].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skills can target allies\nUpon auto-targeting Skills, or in Regular Encounters, target random allies\n- If target is an ally, the attack does not hit, and does not trigger Defense Skills (including Clashable Defense Skills)\nIf target is an ally, activate this Skill at Combat Start
   PL: Umiejętności mogą namierzać sojuszników\nPrzy automatycznym namierzaniu Umiejętności lub w zwykłych walkach namierza losowych sojuszników\n- Jeśli celem jest sojusznik, atak nie trafia i nie wywołuje Umiejętności Obrony (łącznie z obroną zdatną do Starcia)\nJeśli namierzono sojusznika, Umiejętność aktywuje się na początku walki
196. [Status [NoirScissorShield] — nazwa] 두 가위
   źródło: Bufs.json :: dataList[id=NoirScissorShield].name
   kontekst: identyfikator statusu w tekstach: `[NoirScissorShield]`
   limit: do 40 znaków
   EN: Second is Welcome-snipping
   PL: Drugie Cięcie
197. [Status [NoirScissorShield] — opis] - 최댓값 : 1\n- 공격 레벨 +3, 방어 레벨 +3\n- 충전 인격이면, 스킬 사용시 정신력 5 회복 (턴당 1회)\n- 기본 스킬 적중시, 해당 코인 최종 피해량의 5%만큼 참격 피해\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=NoirScissorShield].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Offense Level +3, Defense Level +3\n- On Skill Use, heal 5 SP if this unit is a Charge ID (once per turn)\n- On Base Skill Hit, deal Slash damage equal to 5% of each Coin's final damage\n- Expires at Turn End
   PL: - Maks.: 1\n- Poziom Ataku +3, Poziom Obrony +3\n- Jeśli to Osobowość Ładowania, przy użyciu Umiejętności regeneruje 5 Poczytalności (raz na turę)\n- Przy trafieniu bazową Umiejętnością zadaje obrażenia Cięciem równe 5% końcowych obrażeń każdej monety\n- Znika na koniec tury
198. [Status [NoirScissorShield] — tekst klimatyczny] 가위는 둘로써 하나가되고, 하나인것을 둘로 나눈다.
   źródło: Bufs.json :: dataList[id=NoirScissorShield].flavor
   limit: do 120 znaków
   EN: A pair of scissors becomes one through two, and makes two of what was one.
   PL: Nożyczki dwiema częściami stają się jednością, a jedność dzielą na dwie.
199. [Status [BlackWingHoleFaust] — nazwa] 검은 우산
   źródło: Bufs.json :: dataList[id=BlackWingHoleFaust].name
   kontekst: identyfikator statusu w tekstach: `[BlackWingHoleFaust]`
   limit: do 40 znaków
   EN: Black Umbrella
   PL: Czarny Parasol
200. [Status [BlackWingHoleFaust] — opis] - 최댓값 : 5
   źródło: Bufs.json :: dataList[id=BlackWingHoleFaust].desc
   limit: do 120 znaków
   EN: - Max Stack: 5
   PL: - Maks.: 5
201. [Status [BulletWoundHole] — nazwa] 총상
   źródło: Bufs.json :: dataList[id=BulletWoundHole].name
   kontekst: identyfikator statusu w tekstach: `[BulletWoundHole]`
   limit: do 40 znaków
   EN: Gunshot Wound
   PL: Rana Postrzałowa
202. [Status [BulletHole] — nazwa] 잿빛 탄환
   źródło: Bufs.json :: dataList[id=BulletHole].name
   kontekst: identyfikator statusu w tekstach: `[BulletHole]`
   limit: do 40 znaków
   EN: Ashen Bullet
   PL: Popielaty Pocisk
203. [Status [BulletHole] — opis] - 특수 탄환\n- 최댓값 : 5\n- 이 탄환은 ‘구멍’ E.G.O를 제외한 외부 효과로 얻거나, 값이 증가할 수 없음
   źródło: Bufs.json :: dataList[id=BulletHole].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Capacity: 5\n- This Ammo cannot be gained or raised due to external effects, excluding the "Hollow" E.G.O Skill
   PL: - Szczególna amunicja\n- Maks.: 5\n- Tego Pocisku nie można zyskać ani zwiększyć jego wartości efektami zewnętrznymi, z wyjątkiem Umiejętności E.G.O „Dziura”
204. [Status [BlackWingHole] — nazwa] 검은 날개
   źródło: Bufs.json :: dataList[id=BlackWingHole].name
   kontekst: identyfikator statusu w tekstach: `[BlackWingHole]`
   limit: do 40 znaków
   EN: Black Wings
   PL: Czarne Skrzydła
205. [Status [BlackWingHole] — opis] - 최댓값 : 12\n- 턴 시작 시 (수치 / 4)만큼 자신의 충전 횟수 증가 (소수점 버림)\n- 턴 시작 시 수치 4당 공격 레벨 증가 1 얻음\n- 자신의 충전, 호흡을 얻거나 소모하는 스킬 피해량 +(수치)%
   źródło: Bufs.json :: dataList[id=BlackWingHole].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 12\n- Turn Start: Gain (Stack / 4) Charge Count (rounded down)\n- Turn Start: Gain 1 Offense Level Up for every 4 Stacks\n- This unit's Skills that gain or consume Charge or Poise deal +(Stack)% damage
   PL: - Maks.: 12\n- Na początku tury zyskuje (wartość / 4) Liczników Ładowania (zaokrąglona w dół)\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 4 wartości\n- Umiejętności zyskujące lub zużywające Ładowanie lub Oddech zadają +(wartość)% obrażeń
206. [Status [OathFieldDonQuixote] — nazwa] 보존 신역
   źródło: Bufs.json :: dataList[id=OathFieldDonQuixote].name
   kontekst: identyfikator statusu w tekstach: `[OathFieldDonQuixote]`
   limit: do 40 znaków
   EN: Sanctum of Conservation
   PL: Domena Zachowania
207. [Status [OathFieldDonQuixote] — opis] - 최댓값: 5\n- 모든 아군 인격에게 아래 효과 부여\n· 스킬 사용 시 각 아군의 최대 체력의 (돈키호테의 보존 위력 x 2)%만큼 보호막 얻음 (턴당 1회, 최대 10%)\n\n- 모든 르누아르 소속 아군 인격에게 아래 효과 부여\n· 공격 레벨 +(돈키호테의 보존 위력/3) (소수점 버림, 최대 2)\n· 방어 레벨 +(돈키호테의 보존 위력/2) (소수점 버림, 최대 3)\n\n- 모든 적에게 아래 효과 부여\n· 속도 최솟값, 최댓값 -1 (이 효과로 속도 최솟값, 최댓값이 1 미만이 되지 않음)\n· 진동 폭발 시 받는 흐트러짐 피해량 +10%\n· 충전 횟수 또는 특수 충전을 소모하는 스킬로 받는 피해량 +10% (르누아르 소속 아군 인격의 스킬이면, 대신 2배로 적용)\n\n- 턴 종료 시 수치 1 감소
   źródło: Bufs.json :: dataList[id=OathFieldDonQuixote].desc
   limit: do 1000 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Apply the following effect on all allied Identities:\n  · On Skill Use, each ally gains Shield equal to (Preservation Potency on Don Quixote x 2)% of their respective max HP (once per turn, max 10%)\n\n- Apply the following effects on all "Le Noir" allied Identities:\n  · Offense Level +(Preservation Potency on Don Quixote / 3) (rounded down; max 2)\n  · Defense Level +(Preservation Potency on Don Quixote / 2) (rounded down; max 3)\n\n- Apply the following effects on all enemies:\n  · Min & Max Speed -1 (this effect cannot reduce Min & Max Speed below 1)\n  · Stagger Threshold raised by Tremor Burst +10%\n  · Take +10% damage from Skills that consume Charge Count or Unique Charge (from "Le Noir" allied Identities' Skills, take +20% damage instead)\n\n- Turn End: Lose 1 Stack
   PL: - Maks.: 5\n- Nadaje następujący efekt wszystkim sojuszniczym osobowościom:\n· Przy użyciu Umiejętności każdy sojusznik zyskuje Tarczę równą (Moc Zachowania Don Kichota x 2)% swojego maks. HP (raz na turę, maks. 10%)\n\n- Nadaje następujące efekty wszystkim sojuszniczym osobowościom Le Noir:\n· Poziom Ataku +(Moc Zachowania Don Kichota / 3) (zaokrąglona w dół, maks. 2)\n· Poziom Obrony +(Moc Zachowania Don Kichota / 2) (zaokrąglona w dół, maks. 3)\n\n- Nadaje następujące efekty wszystkim wrogom:\n· Minimalna i maksymalna Szybkość -1 (ten efekt nie obniża Minimalnej i maksymalnej Szybkości poniżej 1)\n· Przy Wybuchu Wstrząsu otrzymuje +10% obrażeń Oszołomieniem\n· Otrzymuje +10% obrażeń od Umiejętności zużywających Liczniki Ładowania lub Szczególne Ładowanie (z Umiejętności sojuszniczych osobowości Le Noir zamiast tego otrzymuje +20%)\n\n- Na koniec tury maleje o 1
208. [Status [OathFieldDonQuixote] — tekst klimatyczny] 르누아르가 추구하는 보존의 가치가 보존되는 영역. 보존하는것을 보존하기위한 모든 르누아르적 행동이 이 영역안에서 이롭게 보존된다.이 영역은 영원한 보존의 영역이자 죽음에 한없이 가까워지고자하는 충동이 자극되는 영역이다.
   źródło: Bufs.json :: dataList[id=OathFieldDonQuixote].flavor
   limit: do 320 znaków
   EN: A sanctuary in which the value of conservation pursued by Le Noir is preserved. Within it, the Noirs' preservative actions are retained to their benefit. It is a realm of eternal conservation—a place that stirs the drive to infinitely approach death.
   PL: Domena, w której zachowuje się wartość zachowania, jakiej wyznaje Le Noir. Wszystkie działania zachowujące w stylu Le Noir zostają w jej obrębie zachowane ku ich korzyści. To domena wiecznego zachowania — miejsce, w którym pobudzany jest popęd nieskończonego zbliżania się do śmierci.
209. [Status [NoirShieldUpDonQuixote] — nazwa] 검은 신의 가호
   źródło: Bufs.json :: dataList[id=NoirShieldUpDonQuixote].name
   kontekst: identyfikator statusu w tekstach: `[NoirShieldUpDonQuixote]`
   limit: do 40 znaków
   EN: Blessing of the Obsidian God
   PL: Łaska Czarnego Boga
210. [Status [NoirShieldUpDonQuixote] — opis] - 최댓값: 100\n- 턴 시작 시 자신의 최대 체력의 (수치/5)%만큼 보호막 얻음 (소수점 버림)\n- 수치가 25 이상이면, 기본 공격 스킬 사용 시 모든 코인이 파괴 불가 코인이 됨\n- 수치가 40 이상이면, 자신은 흐트러짐 상태가 되지 않음 (강제 흐트러짐 제외)
   źródło: Bufs.json :: dataList[id=NoirShieldUpDonQuixote].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- Turn Start: Gain Shield equal to (Stack / 5)% of this unit's max HP (rounded down)\n- At 25+ Stack, On Base Attack Skill Use, convert all Coins into Unbreakable Coins\n- At 40+ Stack, this unit cannot be Staggered (excluding forced Staggers)
   PL: - Maks.: 100\n- Na początku tury zyskuje Tarczę równą (wartość / 5)% maks. HP (zaokrąglona w dół)\n- Przy 25 lub więcej wartości, przy użyciu bazowej Umiejętności ataku, wszystkie monety stają się Niezniszczalnymi Monetami\n- Przy 40 lub więcej wartości ta jednostka nie może zostać Oszołomiona (poza wymuszonym Oszołomieniem)
211. [Status [NoirShieldUpDonQuixote] — tekst klimatyczny] 검은 신. 검은 거인. 망치의 신부. 보존의 권능을 담당하는 백화점의 검은 신이 가장 직접적인 접촉적 가호. 망치는 단단하며 검은색은 모든것을 흡수하여 정지시킨다. 마치 죽음의 속성처럼.
   źródło: Bufs.json :: dataList[id=NoirShieldUpDonQuixote].flavor
   limit: do 390 znaków
   EN: The Obsidian God. The Obsidian Giant. The Chaplain of the Hammer. The Obsidian God of the Grand Magasin, whose domain is the power of preservation, grants his blessing through direct contact. The hammer is hard, and its black hue absorbs all things and brings them to a halt... much like death itself.
   PL: Czarny Bóg. Czarny Gigant. Kapelan Młota. Czarny Bóg Wielkiego Sklepu, strzegący władzy zachowania, udziela swojej łaski poprzez najprostszy z kontaktów. Młot jest twardy, a czerń pochłania wszystko i zatrzymuje. Niczym atrybut śmierci.
212. [Status [NoirNailDonQuixote] — nazwa] 약속된 못
   źródło: Bufs.json :: dataList[id=NoirNailDonQuixote].name
   kontekst: identyfikator statusu w tekstach: `[NoirNailDonQuixote]`
   limit: do 40 znaków
   EN: Promised Nail
   PL: Obiecany Gwóźdź
213. [Status [NoirNailDonQuixote] — opis] - 최댓값: 30\n- 스킬 효과로 진동 폭발 시 이 효과 수치 1당, 나태 피해 1 입음 (최대 10, 스킬당 1회)\n- 턴 종료 시 수치가 4 이상이면, 다음 턴에 속박 1 얻음\n- 턴 시작 시 전장에 오트쿠튀르::르누아르 브랜드 매니저 돈키호테가 없으면, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=NoirNailDonQuixote].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Upon Tremor Burst due to Skill effects, take 1 Sloth damage for every Stack (max 10; once per Skill)\n- Turn End: At 4+ Stack, gain 1 Bind next turn\n- Turn Start: If Haute Couture::Le Noir Brand Manager Don Quixote is not on the field, expires
   PL: - Maks.: 30\n- Przy Wybuchu Wstrząsu z powodu efektu Umiejętności otrzymuje 1 obrażeń Lenistwa za każdą wartość (maks. 10, raz na Umiejętność)\n- Na koniec tury, przy 4 lub więcej wartości, zyskuje w następnej turze 1 Spętania\n- Na początku tury znika, jeśli na polu nie ma Haute Couture::Menedżerka Marki Le Noir Don Kichot
214. [Status [NoirNailDonQuixote] — tekst klimatyczny] 약속의 망치는 반드시 못을 박기로 약속됐다. 그렇기에 망치가 휘둘러진다면 그곳에 못이 없더라도 못이 있어야한다.
   źródło: Bufs.json :: dataList[id=NoirNailDonQuixote].flavor
   limit: do 190 znaków
   EN: The promised hammer is bound by promise to drive in a nail. Therefore, whenever the hammer falls, a nail must exist there... even if there is none.
   PL: Obiecany młot jest związany przyrzeczeniem wbicia gwoździa. Dlatego za każdym razem, gdy młot spada, gwóźdź musi tam istnieć… nawet jeśli go nie ma.
215. [Status [PersonalityCombustion] — nazwa] 화상 인격
   źródło: Bufs.json :: dataList[id=PersonalityCombustion].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityCombustion]`
   limit: do 40 znaków
   EN: Burn ID
   PL: Osobowość Podpalenia
216. [Status [PersonalityCombustion] — opis] 화상 위력, 화상 횟수 또는 특수 화상을 부여하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityCombustion].desc
   limit: do 130 znaków
   EN: Identities that have Base Attack Skills that inflict Burn Potency, Burn Count, or Unique Burn
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające Moc Podpalenia, Licznik Podpalenia lub Szczególne Podpalenie
217. [Status [PersonalityLaceration] — nazwa] 출혈 인격
   źródło: Bufs.json :: dataList[id=PersonalityLaceration].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityLaceration]`
   limit: do 40 znaków
   EN: Bleed ID
   PL: Osobowość Krwawienia
218. [Status [PersonalityLaceration] — opis] 출혈 위력, 출혈 횟수 또는 특수 출혈을 부여하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityLaceration].desc
   limit: do 130 znaków
   EN: Identities that have Base Attack Skills that inflict Bleed Potency, Bleed Count, or Unique Bleed
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające Moc Krwawienia, Licznik Krwawienia lub Szczególne Krwawienie
219. [Status [PersonalityBurst] — nazwa] 파열 인격
   źródło: Bufs.json :: dataList[id=PersonalityBurst].name
   kontekst: identyfikator statusu w tekstach: `[PersonalityBurst]`
   limit: do 40 znaków
   EN: Rupture ID
   PL: Osobowość Rozdarcia
220. [Status [PersonalityBurst] — opis] 파열 위력, 파열 횟수 또는 특수 파열을 부여하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalityBurst].desc
   limit: do 140 znaków
   EN: Identities that have Base Attack Skills that inflict Rupture Potency, Rupture Count, or Unique Rupture
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające Moc Rozdarcia, Licznik Rozdarcia lub Szczególne Rozdarcie
221. [Status [PersonalitySinking] — nazwa] 침잠 인격
   źródło: Bufs.json :: dataList[id=PersonalitySinking].name
   kontekst: identyfikator statusu w tekstach: `[PersonalitySinking]`
   limit: do 40 znaków
   EN: Sinking ID
   PL: Osobowość Zatonięcia
222. [Status [PersonalitySinking] — opis] 침잠 위력, 침잠 횟수 또는 특수 침잠을 부여하는 기본 공격 스킬을 보유한 인격
   źródło: Bufs.json :: dataList[id=PersonalitySinking].desc
   limit: do 140 znaków
   EN: Identities that have Base Attack Skills that inflict Sinking Potency, Sinking Count, or Unique Sinking
   PL: Osobowości posiadające bazowe Umiejętności ataku nadające Moc Zatonięcia, Licznik Zatonięcia lub Szczególne Zatonięcie
223. [Status [Tiphereth_Heads] — nazwa] 티페리트의 기대
   źródło: Bufs.json :: dataList[id=Tiphereth_Heads].name
   kontekst: identyfikator statusu w tekstach: `[Tiphereth_Heads]`
   limit: do 40 znaków
   EN: Tiphereth's Expectation
   PL: Oczekiwanie Tiphereth
224. [Status [Tiphereth_Heads] — opis] - 모든 스킬 코인이 앞면으로 나올 확률 100% 고정 (이 효과는 자신의 스킬, 패시브, 다른 효과보다 우선 적용됨)\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=Tiphereth_Heads].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All of this unit's Skill Coins have a 100% chance to flip Heads (this effect takes precedence over the Skills, Passives, and other effects of this unit)\n- Expires at Turn End
   PL: - Wszystkie monety Umiejętności tej jednostki mają 100% szans na wypadnięcie Awersu (ten efekt ma pierwszeństwo przed Umiejętnościami, pasywami i innymi efektami tej jednostki)\n- Znika na koniec tury
225. [Status [Tiphereth_Tails] — nazwa] 티페리트의 기대[거울]
   źródło: Bufs.json :: dataList[id=Tiphereth_Tails].name
   kontekst: identyfikator statusu w tekstach: `[Tiphereth_Tails]`
   limit: do 50 znaków
   EN: Tiphereth's Expectation [Mirrored]
   PL: Oczekiwanie Tiphereth [Zwierciadło]
226. [Status [Tiphereth_Tails] — opis] - 모든 스킬 코인이 뒷면으로 나올 확률 100% 고정 (이 효과는 자신의 스킬, 패시브, 다른 효과보다 우선 적용됨)\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=Tiphereth_Tails].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - All of this unit's Skill Coins have a 100% chance to flip Tails (this effect takes precedence over the Skills, Passives, and other effects of this unit)\n- Expires at Turn End
   PL: - Wszystkie monety Umiejętności tej jednostki mają 100% szans na wypadnięcie Rewersu (ten efekt ma pierwszeństwo przed Umiejętnościami, pasywami i innymi efektami tej jednostki)\n- Znika na koniec tury
227. [Status [SewingKingMark] — nazwa] 바느질의 왕 표식
   źródło: Bufs.json :: dataList[id=SewingKingMark].name
   kontekst: identyfikator statusu w tekstach: `[SewingKingMark]`
   limit: do 50 znaków
   EN: Mark of the King of Needleworks
   PL: Znak Króla Szycia
228. [Status [SewingKingMark] — opis] - 최댓값: 1\n- 시지프 소속 인격에게 스킬로 받는 피해량 +20%\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 이번 턴에 수감자의 스킬로 받은 체력 피해(보호막 피해 포함)의 5%만큼 고정 피해를 받음\n- 사망 시 자신의 최대 체력의 10%만큼 무작위 아군 1명에게 고정 피해를 줌 (집중 전투인 경우, 부위로 판정)
   źródło: Bufs.json :: dataList[id=SewingKingMark].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +20% damage from "Sisyphe" Identities\n- Turn End: Gain 1 Bind next turn\n- Turn End: Take fixed damage equal to 5% of HP damage (including Shield damage) taken from the Sinners' Skills\n- On death, deal fixed damage equal to 10% of this unit's max HP on 1 random ally (in Focused Encounters, a Part)
   PL: - Maks.: 1\n- Otrzymuje +20% obrażeń od osobowości Sisyphe\n- Na koniec tury zyskuje w następnej turze 1 Spętania\n- Na koniec tury otrzymuje obrażenia stałe równe 5% obrażeń HP (łącznie z obrażeniami Tarczy) otrzymanych od Umiejętności więźniów\n- Po śmierci zadaje obrażenia stałe równe 10% własnego maks. HP 1 losowemu sojusznikowi (w walkach skupionych: części)
229. [Status [HungrySinclair] — nazwa] 끊임없는 허기
   źródło: Bufs.json :: dataList[id=HungrySinclair].name
   kontekst: identyfikator statusu w tekstach: `[HungrySinclair]`
   limit: do 40 znaków
   EN: Relentless Hunger
   PL: Nieustający Głód
230. [Status [HungrySinclair] — opis] - 최댓값: 150\n- 턴당 최대 50까지 얻을 수 있음
   źródło: Bufs.json :: dataList[id=HungrySinclair].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 150\n- Can gain up to 50 Stacks per turn
   PL: - Maks.: 150\n- Można zyskać do 50 wartości na turę
231. [Status [TransformSinclair] — nazwa] 고귀한 품격
   źródło: Bufs.json :: dataList[id=TransformSinclair].name
   kontekst: identyfikator statusu w tekstach: `[TransformSinclair]`
   limit: do 40 znaków
   EN: Noble Dignity
   PL: Szlachetna Duma
232. [Status [TransformSinclair] — opis] 자신의 맥동 위력에 따라 아래 효과 얻음\n- 2 ~ : 출혈로 받는 피해량 -25%\n- 3 ~ : 기본 스킬의 출혈 위력 및 횟수 부여량 +1\n- 4 ~ : 기본 스킬의 기본 위력 +1\n\n- 속도 최솟값, 최댓값 +1\n- 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않음 (전투당 1회)\n\n- 르루주 소속 아군 인격(자신 포함)에게 다음 효과 적용\n· 속도 최솟값, 최댓값 +1\n· 충전 횟수를 소모하는 스킬의 효과 발동에 필요한 횟수가 부족하면, 부족한 횟수 1당 뷔페 1을 소모하여 자신의 충전 횟수 1 증가
   źródło: Bufs.json :: dataList[id=TransformSinclair].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain all of the following effects based on Pulsation Potency on self:\n- 2+: Take -25% damage from Bleed\n- 3+: Base Skills inflict +1 more Bleed Potency and Count\n- 4+: Base Skill Base Power +1\n\n- Min & Max Speed +1\n- When this unit takes damage that brings its HP down to 0, this unit's HP does not drop below 1 for the turn (once per Encounter)\n\n- Apply the following effects to "Le Rouge" allied Identities (including this unit):\n  · Min & Max Speed +1\n  · If there is not enough Charge Count to activate the effects of Skills that consume Charge Count, consume 1 Buffet to gain 1 Charge Count for every missing Charge Count required for activation
   PL: Zyskuje następujące efekty zależnie od własnej Mocy Pulsacji:\n- 2 lub więcej: otrzymuje -25% obrażeń od Krwawienia\n- 3 lub więcej: bazowe Umiejętności nadają o 1 więcej Mocy i Liczników Krwawienia\n- 4 lub więcej: Moc Bazowa bazowych Umiejętności +1\n\n- Minimalna i maksymalna Szybkość +1\n- Po otrzymaniu obrażeń, które obniżają HP do 0, HP nie spada poniżej 1 w tej turze (raz na walkę)\n\n- Stosuje następujące efekty u sojuszniczych osobowości Le Rouge (łącznie z tą jednostką):\n· Minimalna i maksymalna Szybkość +1\n· Jeśli Liczników Ładowania jest za mało, by aktywować efekty Umiejętności je zużywających, zużywa 1 Bufetu za każdy brakujący Licznik Ładowania, zyskując 1 Licznik Ładowania
233. [Status [TransformSinclair] — podsumowanie] 조건에 따라 기본 스킬 강화
   źródło: Bufs.json :: dataList[id=TransformSinclair].summary
   limit: do 120 znaków
   EN: Strengthen Base Skills under certain conditions
   PL: Wzmocnienie bazowych Umiejętności w zależności od warunków
234. [Status [BoneNailSinclair] — nazwa] 라브젝트(l'abject)
   źródło: Bufs.json :: dataList[id=BoneNailSinclair].name
   kontekst: identyfikator statusu w tekstach: `[BoneNailSinclair]`
   limit: do 40 znaków
   EN: L'Abject
   PL: L'Abject
235. [Status [BoneNailSinclair] — opis] - 특수 출혈\n- 최댓값: 5\n- 수치 1당 르루주 소속 인격에게 받는 피해량 +2% (최대 10%)\n- 턴 시작 시 자신의 출혈 횟수 1 증가\n- 턴 종료 시 다음 턴에 (수치/2)만큼 속박 얻음 (소수점 버림)\n- 턴 시작 시 전장에 오트쿠튀르::르루주 붉은 신 싱클레어가 없으면, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=BoneNailSinclair].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- Max Stack: 5\n- Take +2% damage from "Le Rouge" Identities for every Stack (max 10%)\n- Turn Start: Gain +1 Bleed Count\n- Turn End: Gain (Stack / 2) Bind next turn (rounded down)\n- Turn Start: If Haute Couture::The Crimson God of Le Rouge Sinclair is not on the field, this effect expires
   PL: - Szczególne Krwawienie\n- Maks.: 5\n- Otrzymuje +2% obrażeń od osobowości Le Rouge za każdą wartość (maks. 10%)\n- Na początku tury zyskuje 1 Licznik Krwawienia\n- Na koniec tury zyskuje w następnej turze (wartość / 2) Spętania (zaokrąglona w dół)\n- Na początku tury znika, jeśli na polu nie ma Haute Couture::Czerwony Bóg Le Rouge Sinclair
236. [Status [BuffetSinclair] — nazwa] 폭주
   źródło: Bufs.json :: dataList[id=BuffetSinclair].name
   kontekst: identyfikator statusu w tekstach: `[BuffetSinclair]`
   limit: do 40 znaków
   EN: Uncontrollable Rampage
   PL: Paroksyzm
237. [Status [BuffetSinclair] — opis] - 최댓값: 3\n- 수치 1당 공격 레벨 +1 (최대 3)\n- 속도 최솟값, 최댓값 +1\n- 자신의 출혈 1당, 피해량 +1% (최대 15%)\n\n- 흐트러짐 상태가 되지 않음 (강제 흐트러짐 제외)\n- 출혈로 받는 피해량 -50%\n- 출혈 피해로 사망하지 않음\n\n- 기본 공격 스킬 사용 시 자신의 출혈 횟수 3 증가\n- 기본 공격 스킬 적중 시 폭주 수치만큼 출혈 얻음\n\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BuffetSinclair].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack (max 3)\n- Min & Max Speed +1\n- Deal +1% damage for every Bleed on self (max 15%)\n\n- Cannot become Staggered (excluding forced Stagger)\n- Take -50% damage from Bleed\n- Cannot be defeated by Bleed damage\n\n- On Base Attack Skill Use, gain +3 Bleed Count\n- On Base Attack Skill Hit, gain Bleed equal to Uncontrollable Rampage Stack\n\n- Turn End: Lose 1 Count
   PL: - Maks.: 3\n- Poziom Ataku +1 za każdą wartość (maks. 3)\n- Minimalna i maksymalna Szybkość +1\n- Zadaje +1% obrażeń za każde 1 własnego Krwawienia (maks. 15%)\n\n- Nie może zostać Oszołomiona (poza wymuszonym Oszołomieniem)\n- Otrzymuje -50% obrażeń od Krwawienia\n- Nie umiera od obrażeń Krwawienia\n\n- Przy użyciu bazowej Umiejętności ataku zyskuje 3 Liczniki Krwawienia\n- Przy trafieniu bazową Umiejętnością ataku zyskuje Krwawienie równe wartości Paroksyzmu\n\n- Na koniec tury maleje o 1
238. [Status [BuffetSinclair] — podsumowanie] 기본 공격 스킬 사용 시 자신의 출혈 횟수 증가\n 기본 공격 스킬 적중 시 폭주 수치만큼 출혈 얻음
   źródło: Bufs.json :: dataList[id=BuffetSinclair].summary
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Base Attack Skill Use, gain Bleed Count\nOn Base Attack Skill Hit, gain Bleed equal to Uncontrollable Rampage Stack
   PL: Przy użyciu bazowej Umiejętności ataku zyskuje Liczniki Krwawienia\nPrzy trafieniu bazową Umiejętnością ataku zyskuje Krwawienie równe wartości Paroksyzmu
239. [Status [DinnerField] — nazwa] 뷔페【Buffet】
   źródło: Bufs.json :: dataList[id=DinnerField].name
   kontekst: identyfikator statusu w tekstach: `[DinnerField]`
   limit: do 40 znaków
   EN: Buffet
   PL: Bufet【Buffet】
240. [Status [DinnerField] — opis] - 최댓값: 999\n- 전장에서 체력을 회복할 때마다 (실제로 회복한 체력 / 10)만큼 수치 증가\n(최대 100, 회복 건별 소수점 올림, E.G.O 기프트로 인한 회복 제외)\n\n- 모든 캐릭터가 수치를 공유함\n- 전투 장소 변경 시 초기화
   źródło: Bufs.json :: dataList[id=DinnerField].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 999\n- This value is increased by (actual HP healed / 10) whenever allies' or enemies' HP is healed on the field\n · Max 100 per instance of healing\n · Rounded up for each instance\n · Healing from E.G.O Gifts does not count\n\n- This value is shared by all characters\n- Resets when moving to a different zone
   PL: - Maks.: 999\n- Za każde regenerowanie HP na polu rośnie o (faktycznie zregenerowane HP / 10)\n(maks. 100 za każde pojedyncze leczenie, zaokrąglona w górę; nie liczy regeneracji z Darów E.G.O)\n\n- Wartość współdzielona przez wszystkie jednostki\n- Resetuje się przy zmianie strefy walki
241. [Status [DinnerField] — tekst klimatyczny] 살과 고기의 뷔페가 차려졌으니, 모두 여기서 만찬을.
   źródło: Bufs.json :: dataList[id=DinnerField].flavor
   limit: do 120 znaków
   EN: The Buffet of flesh and meat is served. Let this be a feasting hall for all.
   PL: Bufet z ciała i mięsa jest podany. Niech to będzie sala uczt dla wszystkich.
242. [Status [BuffetFriendShield] — nazwa] 보좌
   źródło: Bufs.json :: dataList[id=BuffetFriendShield].name
   kontekst: identyfikator statusu w tekstach: `[BuffetFriendShield]`
   limit: do 40 znaków
   EN: Attending the Divine
   PL: Asysta przy Boskości
243. [Status [BuffetFriendShield] — opis] - 특수 원호 방어\n- 최댓값: 1\n\n- 오트쿠튀르::르루주 붉은 신 싱클레어가 적에게 일방 공격을 받으면, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경\n· 오트쿠튀르::르루주 붉은 신 싱클레어의 ‘라 가르드(la garde)’를 복사하여 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 사용\n- 이 효과는 원호 방어로 간주되며, 원호 방어 수치를 계산할 때 합산됨\n\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=BuffetFriendShield].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Assist Defense\n- Max Stack: 1\n\n- When Haute Couture::The Crimson God of Le Rouge Sinclair is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self\n · Then, copy and use Haute Couture::The Crimson God of Le Rouge Sinclair's "La Garde"\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- This effect counts as Assist Defense, and is counted toward calculating Assist Defense Stacks\n\n- Turn End: This effect expires
   PL: - Szczególna Obrona Wsparcia\n- Maks.: 1\n\n- Gdy Haute Couture::Czerwony Bóg Le Rouge Sinclair ma otrzymać atak niekwestionowany od wroga, zużywa 1 wartości, by przekierować namierzanie wroga na siebie\n· Kopiuje i używa „La Garde” Haute Couture::Czerwonego Boga Le Rouge Sinclair\n- Jeśli kilku sojuszników posiada Obronę Wsparcia, priorytet aktywacji ma sojusznik z najwyższą wartością\n- Ten efekt liczy się jako Obrona Wsparcia i jest wliczany do obliczania wartości Obrony Wsparcia\n\n- Znika na koniec tury
244. [Status [BuffetFriendShield] — tekst klimatyczny] 우리의 새로운 신을 위하여.
   źródło: Bufs.json :: dataList[id=BuffetFriendShield].flavor
   limit: do 120 znaków
   EN: Let us attend to our new God.
   PL: Ku chwale naszego nowego Boga.
245. [Status [BuffetThirst] — nazwa] 절박한 허기
   źródło: Bufs.json :: dataList[id=BuffetThirst].name
   kontekst: identyfikator statusu w tekstach: `[BuffetThirst]`
   limit: do 40 znaków
   EN: Desperate Hunger
   PL: Rozpaczliwy Głód
246. [Status [BuffetThirst] — opis] - 공격 레벨 +2\n\n- 적에게 사용하는 기본 공격 스킬의 코인 시작 시, 자신의 충전 횟수 1을 소모하여 가하는 피해량 +5%\n· 출혈 위력 또는 횟수를 부여하는 스킬이면, 대신 가하는 피해량 +10% (특수 출혈 포함)\n· 전장에 뷔페가 1 이상이며, 자신의 충전 횟수가 최대가 아니면, 뷔페를 1 소모하여 자신의 충전 횟수 1 증가\n· 충전 횟수와 뷔페가 모두 없으면, 대신 자신의 최대 체력의 1%만큼 체력을 소모하여 효과 발동 (소수점 버림)\n(해당 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음. 체력이 1이어도 발동)\n\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=BuffetThirst].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2\n\n- At Coin Start of a Base Attack Skill used against an enemy, consume 1 Charge Count to deal +5% damage\n · Skills that inflict Bleed Potency or Count deal +10% damage instead (including Unique Bleed)\n · At 1+ Buffet Value on the field, if this unit is not at max Charge Count, consume 1 Buffet to gain +1 Charge Count\n · If both Charge Count and Buffet are at 0, consume 1% HP on self instead to activate the effect (rounded down; damage dealt by this effect does not Stagger or reduce this unit's HP below 1; activates even at 1 HP)\n\n- Turn End: This effect expires
   PL: - Poziom Ataku +2\n\n- Na początku monety bazowej Umiejętności ataku użytej przeciw wrogowi zużywa 1 Licznik Ładowania, zadając +5% obrażeń\n· Jeśli Umiejętność nadaje Moc lub Licznik Krwawienia, zamiast tego zadaje +10% obrażeń (łącznie ze Szczególnym Krwawieniem)\n· Jeśli na polu jest 1 lub więcej Bufetu, a Licznik Ładowania nie jest maksymalny, zużywa 1 Bufetu, zyskując 1 Licznik Ładowania\n· Jeśli ani Liczników Ładowania, ani Bufetu nie ma, zamiast tego zużywa 1% własnego maks. HP, by aktywować efekt (zaokrąglona w dół; te obrażenia nie Oszołomią ani nie obniżą HP poniżej 1; aktywuje się nawet przy 1 HP)\n\n- Znika na koniec tury
247. [Status [BuffetThirst] — podsumowanie] 충전 횟수를 사용하여 가하는 피해량 증가
   źródło: Bufs.json :: dataList[id=BuffetThirst].summary
   limit: do 120 znaków
   EN: Consume Charge Count to deal more damage
   PL: Zużywa Liczniki Ładowania, by zadawać więcej obrażeń
248. [Status [BuffetThirst] — tekst klimatyczny] 굶주릴수록 절박해지고, 내몰릴수록 절실해진다.
   źródło: Bufs.json :: dataList[id=BuffetThirst].flavor
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The sharper one hungers, the fiercer the desperation.\nThe further one is driven, the deeper the longing.
   PL: Im ostrzejszy głód, tym większe rozpaczanie.\nIm dalej się jest poganianym, tym głębsze pragnienie.
249. [Status [RougeFamilySinclair] — nazwa] 붉은 요람
   źródło: Bufs.json :: dataList[id=RougeFamilySinclair].name
   kontekst: identyfikator statusu w tekstach: `[RougeFamilySinclair]`
   limit: do 40 znaków
   EN: Crimson Cradle
   PL: Czerwona Kołyska
250. [Status [RougeFamilySinclair] — opis] 자신을 제외한 르루주 소속 아군이 조건 만족 시 다음 효과 발동\n- 해당 캐릭터가 사망한 상태여도 효과 유지
   źródło: Bufs.json :: dataList[id=RougeFamilySinclair].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When conditions are met by other "Le Rouge" allies, activate corresponding effects for Haute Couture::The Crimson God of Le Rouge Sinclair\n- Effects remain active even if the corresponding ally is defeated
   PL: - Gdy sojusznicy frakcji Le Rouge (poza tą jednostką) spełnią warunki, wywoływane są następujące efekty\n- Efekty pozostają aktywne nawet, gdy odpowiednia postać zginie
251. [Status [NiddlePinGather] — nazwa] 작고 뾰족한 못
   źródło: Bufs.json :: dataList[id=NiddlePinGather].name
   kontekst: identyfikator statusu w tekstach: `[NiddlePinGather]`
   limit: do 40 znaków
   EN: Tiny and Sharp Nails
   PL: Małe i Ostre Gwoździe
252. [Status [NiddlePinGather] — opis] - 최댓값 : 30
   źródło: Bufs.json :: dataList[id=NiddlePinGather].desc
   limit: do 120 znaków
   EN: - Max Stack: 30
   PL: - Maks.: 30
253. [Status [NiddlePinAlly] — nazwa] 바늘못
   źródło: Bufs.json :: dataList[id=NiddlePinAlly].name
   kontekst: identyfikator statusu w tekstach: `[NiddlePinAlly]`
   limit: do 40 znaków
   EN: Naildle
   PL: Gwoździk
254. [Status [NiddlePinAlly] — opis] - 특수 출혈\n- 최댓값 : 10\n- 턴 종료시 수치 1 감소\n\n- 이 효과의 수치가 감소할 때, 감소량 1당 효과 보유자의 출혈 위력이 1 증가하고 색욕 피해 3 받음\n\n- 전장에 적 오트쿠튀르::르루주 붉은 신 싱클레어 인격이 있으면, 턴 종료시 이 효과 보유자가 라브젝트(l'abject) 1 얻음
   źródło: Bufs.json :: dataList[id=NiddlePinAlly].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- Max Stack: 10\n- Turn End: Lose 1 Stack\n\n- When losing this effect's Stack, gain 1 Bleed Potency and take 3 Lust damage for every Stack lost\n\n- Turn End: If enemy Haute Couture::The Crimson God of Le Rouge Sinclair is on the field and this unit has this effect, this unit gains 1 L'Abject
   PL: - Szczególne Krwawienie\n- Maks.: 10\n- Na koniec tury maleje o 1\n\n- Przy utracie wartości tego efektu zyskuje 1 Mocy Krwawienia za każdą utraconą wartość i otrzymuje 3 obrażeń Pożądania\n\n- Jeśli na polu jest wroga osobowość Haute Couture::Czerwony Bóg Le Rouge Sinclair, na koniec tury posiadacz tego efektu zyskuje 1 L'Abject
255. [Status [NiddlePinnedAlly] — nazwa] 박제 상태
   źródło: Bufs.json :: dataList[id=NiddlePinnedAlly].name
   kontekst: identyfikator statusu w tekstach: `[NiddlePinnedAlly]`
   limit: do 40 znaków
   EN: Taxidermized
   PL: Zataksydermizowany
256. [Status [NiddlePinnedAlly] — opis] - 최댓값 : 1\n- 스킬 최종 위력 -1\n- 자신이 공격 스킬 사용 시, 자신의 출혈 발동, 출혈 횟수 1 감소 (스킬당 1회) \n- 턴 종료시 다음 턴에 출혈 횟수 2, 위력 감소 1, 속박 2 얻음\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=NiddlePinnedAlly].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Skill Final Power -1\n- On Attack Skill Use, activate Bleed on self and lose 1 Bleed Count (once per Skill)\n- Turn End: Gain +2 Bleed Count, 1 Power Down, and 2 Bind next turn\n- Turn End: This effect expires
   PL: - Maks.: 1\n- Moc Końcowa Umiejętności -1\n- Przy użyciu własnej Umiejętności ataku aktywuje własne Krwawienie, tracąc 1 Licznik Krwawienia (raz na Umiejętność)\n- Na koniec tury zyskuje w następnej turze 2 Liczniki Krwawienia, 1 Spadek Mocy i 2 Spętania\n- Znika na koniec tury
257. [Status [NeedlekinAlly] — nazwa] 바늘이
   źródło: Bufs.json :: dataList[id=NeedlekinAlly].name
   kontekst: identyfikator statusu w tekstach: `[NeedlekinAlly]`
   limit: do 40 znaków
   EN: Needlekin
   PL: Igiełka
258. [Status [NeedlekinAlly] — opis] - 최댓값 : 3\n- 수치 1당 공격 레벨 +1
   źródło: Bufs.json :: dataList[id=NeedlekinAlly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack
   PL: - Maks.: 3\n- Poziom Ataku +1 za każdą wartość
259. [Status [NeedlekinAlly] — tekst klimatyczny] 쪼용! 쪼용!
   źródło: Bufs.json :: dataList[id=NeedlekinAlly].flavor
   limit: do 120 znaków
   EN: Shaddap! Shaddap!
   PL: Cisza! Cisza!
260. [Status [HowlingCocoonAlly] — nazwa] 고치의 울음소리 - 미약
   źródło: Bufs.json :: dataList[id=HowlingCocoonAlly].name
   kontekst: identyfikator statusu w tekstach: `[HowlingCocoonAlly]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Frail
   PL: Krzyk Kokonu - Słabość
261. [Status [HowlingCocoonAlly] — opis] - 최댓값 : 5\n- 기본 스킬 최종 위력 +1\n- 기본 스킬 적중시 최대 체력의 3%만큼 체력 회복 (턴당 5회)\n\n- 턴 시작시 아군 오트쿠튀르::르루주 붉은 신 싱클레어가 전장에 없으면 이 효과 소멸
   źródło: Bufs.json :: dataList[id=HowlingCocoonAlly].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Base Skill Final Power +1\n- On Hit using Base Skills, heal 3% HP (5 times per turn)\n\n- Turn Start: If allied Haute Couture::The Crimson God of Le Rouge Sinclair is not on the field, this effect expires
   PL: - Maks.: 5\n- Moc Końcowa bazowych Umiejętności +1\n- Przy trafieniu bazową Umiejętnością regeneruje HP równe 3% maks. HP (5 razy na turę)\n\n- Na początku tury znika, jeśli sojuszniczy Haute Couture::Czerwony Bóg Le Rouge Sinclair nie jest na polu
262. [Status [HowlingCocoonTwoAlly] — nazwa] 고치의 울음소리 - 악성
   źródło: Bufs.json :: dataList[id=HowlingCocoonTwoAlly].name
   kontekst: identyfikator statusu w tekstach: `[HowlingCocoonTwoAlly]`
   limit: do 40 znaków
   EN: Cry of the Cocoon - Vicious
   PL: Krzyk Kokonu - Złośliwość
263. [Status [HowlingCocoonTwoAlly] — opis] - 최댓값 : 1\n- 기본 스킬 최종 위력 +1\n- 기본 스킬 피해량 +10%\n- 기본 스킬 적중시 최대 체력의 6%만큼 체력 회복 (턴당 5회)\n\n- 턴 시작시 아군 오트쿠튀르::르루주 붉은 신 싱클레어가 전장에 없으면 이 효과 소멸
   źródło: Bufs.json :: dataList[id=HowlingCocoonTwoAlly].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Base Skill Final Power +1\n- Deal +10% damage using Base Skills\n- On Hit using Base Skills, heal 6% HP (5 times per turn)\n\n- Turn Start: If allied Haute Couture::The Crimson God of Le Rouge Sinclair is not on the field, this effect expires
   PL: - Maks.: 1\n- Moc Końcowa bazowych Umiejętności +1\n- Zadaje +10% obrażeń bazowymi Umiejętnościami\n- Przy trafieniu bazową Umiejętnością regeneruje HP równe 6% maks. HP (5 razy na turę)\n\n- Na początku tury znika, jeśli sojuszniczy Haute Couture::Czerwony Bóg Le Rouge Sinclair nie jest na polu
264. [Status [NoirBindArmorAlly] — nazwa] 르누아르 우스티드 원단 코트
   źródło: Bufs.json :: dataList[id=NoirBindArmorAlly].name
   kontekst: identyfikator statusu w tekstach: `[NoirBindArmorAlly]`
   limit: do 40 znaków
   EN: Le Noir: Worsted Overcoat
   PL: Le Noir: Płaszcz z Wełny Czesanej
265. [Status [NoirBindArmorAlly] — opis] - 최댓값 : 15\n- 수치 5당, 공격 레벨 +1, 방어 레벨 +1\n- 보호막이 있는 상태에서 피격 시, 1 증가 (턴당 최대 5)\n- 턴 종료 시 다음 턴에 (수치 x 5)만큼 보호막 얻고 수치 1 감소
   źródło: Bufs.json :: dataList[id=NoirBindArmorAlly].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- Offense Level +1, Defense Level +1 for every 5 Stack\n- When hit while this unit has Shield, gain 1 Stack (5 Stacks per turn)\n- Turn End: Next turn, gain (Stack x 5) Shield and lose 1 Stack
   PL: - Maks.: 15\n- Poziom Ataku +1, Poziom Obrony +1 za każde 5 wartości\n- Przy trafieniu posiadając Tarczę zyskuje 1 wartości (do 5 na turę)\n- Na koniec tury zyskuje w następnej turze (wartość x 5) Tarczy, tracąc 1 wartości
266. [Status [ReadyToListenHonglu] — nazwa] 낭독 준비
   źródło: Bufs.json :: dataList[id=ReadyToListenHonglu].name
   kontekst: identyfikator statusu w tekstach: `[ReadyToListenHonglu]`
   limit: do 40 znaków
   EN: Ready to Narrate
   PL: Gotowość do Recytacji
267. [Status [ReadyToListenHonglu] — opis] - 최댓값 : 2\n- 턴 종료시 다음 턴에 수치만큼 보호 얻음\n- 턴 종료시 최댓값이면, 전부 소모하여 다음 턴에 경청의 시간을 2 얻음\n- 턴당 최대 1만 획득 가능\n- 경청의 시간이 있으면, 낭독 준비는 얻을 수 없음
   źródło: Bufs.json :: dataList[id=ReadyToListenHonglu].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Gain (Stack) Protection next turn\n- Turn End: At max Stack, consume all Stacks to gain 2 Time to Listen next turn\n- Can gain up to 1 Stack per turn\n- If this unit has Time to Listen, it cannot gain Ready to Narrate
   PL: - Maks.: 2\n- Na koniec tury zyskuje w następnej turze Ochronę równą wartości\n- Na koniec tury, przy maksimum, zużywa wszystkie wartości, zyskując w następnej turze 2 Czasu Uważnego Słuchu\n- Można zyskać do 1 wartości na turę\n- Posiadając Czas Uważnego Słuchu, nie można zyskać Gotowości do Recytacji
268. [Status [TimeToListenHonglu] — nazwa] 경청의 시간
   źródło: Bufs.json :: dataList[id=TimeToListenHonglu].name
   kontekst: identyfikator statusu w tekstach: `[TimeToListenHonglu]`
   limit: do 40 znaków
   EN: Time to Listen
   PL: Czas Uważnego Słuchu
269. [Status [TimeToListenHonglu] — opis] - 최댓값 : 2\n- 자신의 기본 스킬의 기본 위력 +1\n- 전투 시작시 가장 왼쪽 슬롯에 더하기 코인 스킬을 장착한 인격의 정신력 4 회복, 빼기 코인 스킬을 장착한 인격의 정신력 4 감소 (수감자 별 턴당 1회)\n· 해당 효과로 대상의 정신력이 -40 미만으로 내려가지 않음\n- 전투 시작시 더하기 코인 스킬을 장착한 인격의 정신력이 40 이상이거나 빼기 코인 스킬을 장착한 인격의 정신력이 -40 이하이면, 해당 인격에게 나태 피해량 증가 1 부여 (수감자 별 턴당 1회)\n· 해당 인격이 르누아르 소속이면, 추가로 기본 위력 증가 1 부여\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=TimeToListenHonglu].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Base Skill Base Power +1\n- Combat Start (once per turn per Sinner):\n  · Identities that equipped Plus Coin Skills in their leftmost Slots heal 4 SP\n  · Identities that equipped Minus Coin Skills in their leftmost Slots lose 4 SP (this effect cannot reduce the unit's SP below -40)\n- Combat Start: Apply 1 Sloth DMG Up on the following Identities (once per turn per Sinner):\n  · Identities that equipped Plus Coin Skills and have 40 or higher SP; Le Noir Identities additionally gain 1 Base Power Up\n  · Identities that equipped Minus Coin Skills and have -40 or lower SP; Le Noir Identities additionally gain 1 Base Power Up\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Moc Bazowa własnych bazowych Umiejętności +1\n- Na początku walki regeneruje 4 Poczytalności osobowości z Umiejętnościami Monet Plus w skrajnie lewych slotach i odbiera 4 Poczytalności osobowości z Umiejętnościami Monet Minus (raz na turę na więźnia)\n· Ten efekt nie obniża Poczytalności celu poniżej -40\n- Na początku walki nadaje 1 Wzrostu Obrażeń Lenistwa następującym osobowościom (raz na turę na więźnia):\n· Osobowości z Umiejętnościami Monet Plus, których Poczytalność wynosi 40 lub więcej; osobowości Le Noir zyskują dodatkowo 1 Wzrost Mocy Bazowej\n· Osobowości z Umiejętnościami Monet Minus, których Poczytalność wynosi -40 lub mniej; osobowości Le Noir zyskują dodatkowo 1 Wzrost Mocy Bazowej\n- Na koniec tury maleje o 1
270. [Status [WarinessHonglu] — nazwa] 경청 형벌
   źródło: Bufs.json :: dataList[id=WarinessHonglu].name
   kontekst: identyfikator statusu w tekstach: `[WarinessHonglu]`
   limit: do 40 znaków
   EN: Auditive Punishment
   PL: Słuchowa Kara
271. [Status [WarinessHonglu] — opis] - 최댓값 : 2\n- 수치만큼 공격 레벨 -1\n- 경청의 시간을 보유한 인격이 있을 때, 르누아르 소속 인격에게 받는 피해량 +(수치 x 10)%\n- 경청의 시간을 보유한 인격이 있을 때, 턴 종료시 1 감소 (이 효과를 부여한 인격이 퇴각 및 사망했으면, 소멸)
   źródło: Bufs.json :: dataList[id=WarinessHonglu].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Lose Offense Level equal to Stack\n- If there is an Identity that has Time to Listen, take +(Stack x 10)% damage from "Le Noir" Identities\n- Turn End: If there is an Identity that has Time to Listen, lose 1 Stack (if the Identity that inflicted this effect has been defeated or Retreated, expires)
   PL: - Maks.: 2\n- Poziom Ataku -1 za wartość\n- Gdy istnieje osobowość posiadająca Czas Uważnego Słuchu, otrzymuje +(wartość x 10)% obrażeń od osobowości Le Noir\n- Gdy istnieje osobowość posiadająca Czas Uważnego Słuchu, na koniec tury maleje o 1 (znika, jeśli nadająca osobowość poległa lub się wycofała)
272. [Status [WedgeOffice] — nazwa] 쐐기 사무소
   źródło: Bufs.json :: dataList[id=WedgeOffice].name
   kontekst: identyfikator statusu w tekstach: `[WedgeOffice]`
   limit: do 40 znaków
   EN: Wedge Office
   PL: Biuro Klinów
273. [Status [WedgeOffice] — opis] - 최댓값 : 3\n- 수치 1당, 공격 레벨 1 증가\n- 수치가 3이면, 전투 시작 시 관통 피해량 증가 1 얻음\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=WedgeOffice].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Offense Level +1 for every Stack\n- Combat Start: At 3 Stacks, gain 1 Pierce DMG Up\n- Expires at Turn End
   PL: - Maks.: 3\n- Poziom Ataku +1 za każdą wartość\n- Na początku walki, przy 3 wartości, zyskuje 1 Wzrostu Obrażeń Przebiciem\n- Znika na koniec tury
274. [Status [ComboWedge] — nazwa] 승기
   źródło: Bufs.json :: dataList[id=ComboWedge].name
   kontekst: identyfikator statusu w tekstach: `[ComboWedge]`
   limit: do 40 znaków
   EN: Momentum
   PL: Przewaga
275. [Status [ComboWedge] — opis] - 최댓값 : 30\n- 턴당 최대 20까지 얻을 수 있음\n턴 시작 시 자신이 흐트러짐 상태면, 흐트러짐 해제 (전투당 1회, 강제 흐트러짐 제외)
   źródło: Bufs.json :: dataList[id=ComboWedge].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Can gain up to 20 Stacks per turn\nTurn Start: If this unit is Staggered, recover from Stagger (once per Encounter; excluding forced Staggers)
   PL: - Maks.: 30\n- Można zyskać do 20 wartości na turę\nNa początku tury, jeśli jednostka jest Oszołomiona, dochodzi do siebie z Oszołomienia (raz na walkę, poza wymuszonym Oszołomieniem)
276. [Status [ComboWedgeDawn] — nazwa] 새벽의 유대
   źródło: Bufs.json :: dataList[id=ComboWedgeDawn].name
   kontekst: identyfikator statusu w tekstach: `[ComboWedgeDawn]`
   limit: do 40 znaków
   EN: Dawn's Camaraderie
   PL: Braterstwo Świtu
277. [Status [ComboWedgeDawn] — opis] - 최댓값 : 5
   źródło: Bufs.json :: dataList[id=ComboWedgeDawn].desc
   (powtórzenie elementu 200 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Status [DespairKnightEGOProtect] — nazwa] 기사의 수호
   źródło: Bufs.json :: dataList[id=DespairKnightEGOProtect].name
   kontekst: identyfikator statusu w tekstach: `[DespairKnightEGOProtect]`
   limit: do 50 znaków
   EN: The Knight's Loyal Protection
   PL: Ochrona Rycerza
279. [Status [DespairKnightEGOProtect] — opis] 기본값 : 3\n자신의 1.5를 초과하는 물리 내성이 1.5로 조정됨 (흐트러짐 상태 제외)\n자신이 흐트러짐 상태면, 받는 피해량 -30% (강제 흐트러짐 포함)\n\n턴 종료시 1 감소\n부여한 캐릭터가 퇴각 또는 사망하거나, 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 동일한 효과가 부여될 경우 교체됨.\n\n적에게 사망 시, 공격자에게 다음 턴에 취약 2를 부여하고, 이 효과 부여자가 다음 턴에 공격 위력 증가 2, 피해량 증가 3 얻음 (턴당 1회)
   źródło: Bufs.json :: dataList[id=DespairKnightEGOProtect].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 3\nThis unit's Attack Type Resist. that are higher than 1.5 are adjusted to 1.5 (except while Staggered)\nIf this unit is Staggered, take -30% damage (including forced Staggers)\n\nTurn End: Lose 1 Stack\nExpires when the character that applied this effect retreats, is defeated, or applies this effect to a different target; replaced when another character applies an equivalent effect\n\nIf this unit is defeated by an enemy, inflict 2 Fragile against the attacker next turn, and the unit that applied this effect gains 2 Attack Power Up and 3 Damage Up next turn (once per turn)
   PL: Wartość bazowa: 3\nOdporności na Typy Ataku tej jednostki powyżej 1.5 zostają doprowadzone do 1.5 (poza Stanem Oszołomienia)\nJeśli jednostka jest Oszołomiona, otrzymuje -30% obrażeń (łącznie z wymuszonym Oszołomieniem)\n\nNa koniec tury maleje o 1\nZnika, gdy nadający się wycofa, polegnie lub przeniesie ten efekt na inną jednostkę; zastępowany, gdy inna jednostka nada równoważny efekt\n\nPo śmierci z rąk wroga nadaje atakującemu w następnej turze 2 Wrażliwości, a nadający ten efekt zyskuje w następnej turze 2 Wzrosty Mocy Ataku i 3 Wzrosty Obrażeń (raz na turę)
280. [Status [DespairKnightEGOSword] — nazwa] 눈물로 벼려낸 검
   źródło: Bufs.json :: dataList[id=DespairKnightEGOSword].name
   kontekst: identyfikator statusu w tekstach: `[DespairKnightEGOSword]`
   limit: do 40 znaków
   EN: Sword Sharpened with Tears
   PL: Ostrze Wykute z Łez
281. [Status [DespairKnightEGOSword] — opis] - 최댓값 : 3\n- 충전을 얻거나 소모하는 스킬 피해량 +(충전 위력 x 2)% (최대 10%)\n- 관통 또는 오만 스킬 피해량 +(수치 x 5)%\n- 자신의 관통 또는 오만 스킬 적중시, (이 효과 수치 x 2) + (해당 코인 최종 피해량의 5%)만큼 오만 피해\n- 공격 종료시, 메인 타겟이 적이면 수치만큼 침잠 위력 부여
   źródło: Bufs.json :: dataList[id=DespairKnightEGOSword].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Skills that gain or consume Charge deal +(Charge Potency x 2)% damage (max 10%)\n- Pierce Skills and Pride Skills deal +(Stack x 5)% damage\n- On Hit using this unit's Pierce or Pride Skills, deal Pride damage equal to ((Stack x 2) + (5% of the Coin's final damage))\n- Attack End: If the main target is an enemy, inflict Sinking Potency equal to Stack
   PL: - Maks.: 3\n- Umiejętności zyskujące lub zużywające Ładowanie zadają +(Moc Ładowania x 2)% obrażeń (maks. 10%)\n- Umiejętności typu Przebicie lub atrybutu Pychy zadają +(wartość x 5)% obrażeń\n- Przy trafieniu własną Umiejętnością typu Przebicie lub atrybutu Pychy zadaje obrażenia Pychy równe ((wartość x 2) + (5% końcowych obrażeń monety))\n- Na koniec ataku, jeśli główny cel jest wrogiem, nadaje Mocy Zatonięcia równą wartości
282. [Status [DespairKnightEGOMind] — nazwa] 닳아버린 긍지
   źródło: Bufs.json :: dataList[id=DespairKnightEGOMind].name
   kontekst: identyfikator statusu w tekstach: `[DespairKnightEGOMind]`
   limit: do 40 znaków
   EN: Weathered Pride
   PL: Zwietrzała Duma
283. [Status [DespairKnightEGOMind] — opis] - 최댓값 : 999\n- 턴당 최대 500까지 얻을 수 있음
   źródło: Bufs.json :: dataList[id=DespairKnightEGOMind].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 999\n- Can gain up to 500 Stacks per turn
   PL: - Maks.: 999\n- Można zyskać do 500 wartości na turę
284. [Status [DespairKnightEGOAlly] — nazwa] 잊혀진 기사의 검
   źródło: Bufs.json :: dataList[id=DespairKnightEGOAlly].name
   kontekst: identyfikator statusu w tekstach: `[DespairKnightEGOAlly]`
   limit: do 40 znaków
   EN: Sword of a Forgotten Knight
   PL: Ostrze Zapomnianego Rycerza
285. [Status [DespairKnightEGOAlly] — opis] - 최댓값 : 3\n- 관통 또는 오만 스킬에 피격 시 수치 1 증가 (스킬당 1회)\n· 수치가 최대치면, 오만 피해를 50 받고 이 효과 소멸. 이번 턴과 다음 턴에 관통 취약 1 얻음\n- 이 효과는 동시에 하나의 캐릭터만 보유할 수 있음 (다른 대상에게 부여 시 기존의 효과 소멸)
   źródło: Bufs.json :: dataList[id=DespairKnightEGOAlly].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When hit by Pierce or Pride Skills, gain 1 Stack (once per Skill)\n · At max Stack, take 50 Pride damage; then, this effect expires. Gain 1 Pierce Fragility this turn and next turn\n- Only 1 character can have this effect at any given time (existing effect expires when this effect is inflicted on another target)
   PL: - Maks.: 3\n- Przy trafieniu Umiejętnością typu Przebicie lub atrybutu Pychy zyskuje 1 wartości (raz na Umiejętność)\n· Przy maksimum otrzymuje 50 obrażeń Pychy, po czym ten efekt znika. Zyskuje 1 Wrażliwość na Przebicie w tej i następnej turze\n- Ten efekt może posiadać tylko jedna jednostka naraz (nadanie tego efektu innej jednostce znosi istniejący efekt)
286. [Status [BattleFieldKnow] — nazwa] 전장 파악
   źródło: Bufs.json :: dataList[id=BattleFieldKnow].name
   kontekst: identyfikator statusu w tekstach: `[BattleFieldKnow]`
   limit: do 40 znaków
   EN: Field Analysis
   PL: Ocena Pola Walki
287. [Status [BattleFieldKnow] — opis] - 최댓값: 5\n- 이 효과의 수치가 증가할 때, 자신의 호흡 횟수 1 증가\n- 턴 종료 시 수치만큼 자신의 호흡 횟수 증가\n- 턴 시작 시 자신이 흐트러짐 상태면, 흐트러짐 해제 (전투당 2회, 강제 흐트러짐 제외)\n- 이 효과 수치에 따라 기본 공격 스킬이 아래 효과 얻음\n· 2 ~ : 스킬 사용 시 적에게 가하는 피해량 +(30/코인 수)% (소수점 버림)\n· 3 ~ : 코인 위력 +1, 스킬 사용 시 마지막 코인이 파괴 불가 코인이 됨\n· 4 ~ : 스킬 사용 시 적에게 가하는 피해량 +(30/코인 수)% (소수점 버림)\n· 5 ~ : 공격 시작 시부터 공격 종료 시까지 공격 대상의 관통 내성 +0.1\n- 피해량 증가와 파괴 불가 코인 변경은 스킬 사용 직전의 수치로 판정
   źródło: Bufs.json :: dataList[id=BattleFieldKnow].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Gain +1 Poise Count when gaining Stacks of this effect\n- Turn End: Gain +(Stack) Poise Count\n- Turn Start: If this unit is Staggered at Turn Start, recover from Stagger (2 times per Encounter; excluding forced Staggers)\n- Base Attack Skills gain the following effects based on Stack:\n  · 2+: On Skill Use, deal +(30 / # of Coins)% damage on enemies (rounded down)\n  · 3+: Coin Power +1; On Skill Use, convert the final Coin to Unbreakable Coin\n  · 4+: On Skill Use, deal +(30 / # of Coins)% damage on enemies (rounded down)\n  · 5+: Target's Pierce Resist. +0.1 from Attack Start to Attack End\n- The Stack immediately before Skill Use is used to determine whether the damage-boosting and Unbreakable Coin conversion effects are activated
   PL: - Maks.: 5\n- Przy zyskiwaniu wartości tego efektu zyskuje 1 Licznik Oddechu\n- Na koniec tury zyskuje Liczniki Oddechu równe wartości\n- Na początku tury, jeśli jednostka jest Oszołomiona, dochodzi do siebie z Oszołomienia (2 razy na walkę, poza wymuszonym Oszołomieniem)\n- Bazowe Umiejętności ataku zyskują następujące efekty zależnie od wartości:\n· 2 lub więcej: przy użyciu Umiejętności zadaje wrogom +(30 / liczba monet)% obrażeń (zaokrąglona w dół)\n· 3 lub więcej: Moc Monety +1; przy użyciu Umiejętności ostatnia moneta staje się Niezniszczalną Monetą\n· 4 lub więcej: przy użyciu Umiejętności zadaje wrogom +(30 / liczba monet)% obrażeń (zaokrąglona w dół)\n· 5 lub więcej: od początku do końca ataku odporność celu na Przebicie +0.1\n- O tym, czy aktywują się efekty zwiększające obrażenia i zamiany na Niezniszczalne Monety, decyduje wartość bezpośrednio przed użyciem Umiejętności
288. [Status [WedgeMarkYellow] — nazwa] 쐐기 - 돈키호테
   źródło: Bufs.json :: dataList[id=WedgeMarkYellow].name
   kontekst: identyfikator statusu w tekstach: `[WedgeMarkYellow]`
   limit: do 40 znaków
   EN: Wedge - Don Quixote
   PL: Klin - Don Kichot
289. [Status [WedgeMarkYellow] — opis] - 최댓값: 8\n- 이 효과가 일정 수치 이상이면, 쐐기 사무소 해결사 싱클레어의 특정 스킬이 강화됨\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 쐐기 사무소 소속 캐릭터가 없으면, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=WedgeMarkYellow].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 8\n- At sufficient Stacks, empower a certain Skill of Wedge Office Fixer Sinclair\n- Turn End: Gain +1 Tremor Count\n- Turn Start: If there are no enemy "Wedge Office" characters on the field, this effect expires
   PL: - Maks.: 8\n- Przy wystarczającej wartości wzmacnia określoną Umiejętność Rozwiązującego Biura Klinów Sinclaira\n- Na koniec tury zyskuje 1 Licznik Wstrząsu\n- Na początku tury znika, jeśli na polu nie ma wrogich jednostek Biura Klinów
290. [Status [WedgeMarkGreen] — nazwa] 쐐기 - 싱클레어
   źródło: Bufs.json :: dataList[id=WedgeMarkGreen].name
   kontekst: identyfikator statusu w tekstach: `[WedgeMarkGreen]`
   limit: do 40 znaków
   EN: Wedge - Sinclair
   PL: Klin - Sinclair
291. [Status [WedgeMarkGreen] — opis] - 최댓값: 8\n- 이 효과가 일정 수치 이상이면, 쐐기 사무소 해결사 돈키호테의 특정 스킬이 강화됨\n- 턴 종료 시 자신의 진동 횟수 1 증가\n- 턴 시작 시 전장에 적 쐐기 사무소 소속 캐릭터가 없으면, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=WedgeMarkGreen].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 8\n- At sufficient Stacks, empower a certain Skill of Wedge Office Fixer Don Quixote\n- Turn End: Gain +1 Tremor Count\n- Turn Start: If there are no enemy "Wedge Office" characters on the field, this effect expires
   PL: - Maks.: 8\n- Przy wystarczającej wartości wzmacnia określoną Umiejętność Rozwiązującego Biura Klinów Don Kichota\n- Na koniec tury zyskuje 1 Licznik Wstrząsu\n- Na początku tury znika, jeśli na polu nie ma wrogich jednostek Biura Klinów
292. [Status [ComboSkill] — nazwa] 연
   źródło: Bufs.json :: dataList[id=ComboSkill].name
   kontekst: identyfikator statusu w tekstach: `[ComboSkill]`
   limit: do 40 znaków
   EN: Joint Combo
   PL: Więź
293. [Status [ComboSkill] — opis] 해당하는 인격이 전장에 행동 가능한 상태로 생존해 있으면, 추가 효과 발동 (해당하는 인격이 모든 종류의 행동 불가 상태, E.G.O 침식, 흐트러짐 상태인 경우, 발동하지 않음)
   źródło: Bufs.json :: dataList[id=ComboSkill].desc
   limit: do 320 znaków
   EN: If the pertinent Identity is on the field, alive, and isn't immobilized, activate the linked effects (does not activate if the pertinent Identity is in any of the following states: all types of immobilized states, E.G.O Corrosions, and Staggers)
   PL: Jeśli odpowiednia osobowość jest na polu, żyje i może działać, aktywują się powiązane efekty (nie aktywują się, gdy odpowiednia osobowość jest w dowolnym stanie unieruchomienia, w Korozji E.G.O lub Oszołomiona)
294. [Status [BurningMatch] — nazwa] 4번째 성냥불
   źródło: Bufs.json :: dataList[id=BurningMatch].name
   kontekst: identyfikator statusu w tekstach: `[BurningMatch]`
   limit: do 40 znaków
   EN: 4th Match Flame
   PL: 4. Płomyk Zapałki
295. [Status [BurningMatch] — opis] - 위력/횟수 최대값 : 100/4\n- 화상 위력, 횟수, 특수 화상을 부여하는 스킬로 피격 후 피격받은 스킬의 공격 종료 시, 위력 5 증가 (스킬당 1회)\n- 턴 종료 시, 횟수 1 증가\n- 횟수가 4이면, (위력 x 횟수 + 44)만큼 분노 피해를 받고 이 효과 소멸
   źródło: Bufs.json :: dataList[id=BurningMatch].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency/Count cap: 100/4\n- When hit by Skills that inflict Burn Potency, Count, or Unique Burn: At Attack End of the said Skills, gain 5 Potency (once per Skill)\n- Turn End: Gain +1 Count\n- At 4 Count, take (Potency x Count + 44) Wrath damage; then, this effect expires
   PL: - Maks. Mocy/Licznika: 100/4\n- Po otrzymaniu trafienia Umiejętnością nadającą Moc, Licznik lub Szczególne Podpalenie, na zakończeniu ataku tej Umiejętności zyskuje 5 Mocy (raz na Umiejętność)\n- Na koniec tury zyskuje 1 Licznika\n- Przy 4 Liczników otrzymuje (Moc x Licznik + 44) obrażeń Gniewu, po czym ten efekt znika
296. [Status [BurningMatch] — tekst klimatyczny] ‘세 번째 성냥불이 꺼지고, 네 번째 성냥불에 불이 붙었을 때....’
   źródło: Bufs.json :: dataList[id=BurningMatch].flavor
   limit: do 120 znaków
   EN: "When the light of the third match goes out, and the fourth bursts into flame..."
   PL: Gdy trzeci płomyk zapałki zgasł, a czwarty rozpłonął….
297. [Status [BulletJoesu] — nazwa] 탄환 - 죄수
   źródło: Bufs.json :: dataList[id=BulletJoesu].name
   kontekst: identyfikator statusu w tekstach: `[BulletJoesu]`
   limit: do 40 znaków
   EN: Ammo - Prisoner
   PL: Pocisk - Więzień
298. [Status [BulletJoesu] — opis] - 특수 탄환\n- 최댓값: 6\n- 소모하여 적중 시 소모한 수치만큼 메인 타겟에게 무두질된 죄수 부여\n- 이 탄환은 인력 충원을 제외한 외부 효과로 얻거나, 값이 증가할 수 없음\n- 수치가 0이 되어도 이 효과는 소멸하지 않음
   źródło: Bufs.json :: dataList[id=BulletJoesu].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Capacity: 6\n- On Hit, if Ammo - Prisoner was spent, inflict (Ammo - Prisoner spent) Tanned Prisoner Stacks on the main target\n- This Ammo's count cannot be gained or raised due to external effects other than "Replenish Personnel"\n- Does not expire at 0 Stacks
   PL: - Szczególna amunicja\n- Maks.: 6\n- Zużywając, przy trafieniu nadaje głównemu celowi Wygarbowanych Więźniów równe zużytej wartości\n- Tego Pocisku nie można zyskać ani zwiększyć jego wartości efektami zewnętrznymi, poza „Uzupełnieniem Personelu”\n- Ten efekt nie znika, nawet gdy wartość spadnie do 0
299. [Status [MoodooJoesu] — nazwa] 무두질된 죄수
   źródło: Bufs.json :: dataList[id=MoodooJoesu].name
   kontekst: identyfikator statusu w tekstach: `[MoodooJoesu]`
   limit: do 40 znaków
   EN: Tanned Prisoner
   PL: Wygarbowany Więzień
300. [Status [MoodooJoesu] — opis] - 최댓값: 6\n- 공격 레벨 -(수치/3) (소수점 올림)\n- 방어 레벨 -(수치/2) (소수점 올림)\n- 턴 종료 시 수치 1 감소
   źródło: Bufs.json :: dataList[id=MoodooJoesu].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 6\n- Offense Level -(Stack / 3) (rounded up)\n- Defense Level -(Stack / 2) (rounded up)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 6\n- Poziom Ataku -(wartość / 3) (zaokrąglona w górę)\n- Poziom Obrony -(wartość / 2) (zaokrąglona w górę)\n- Na koniec tury maleje o 1
301. [Status [RuleDontA] — nazwa] 규칙: 르누아르 지정 금지
   źródło: Bufs.json :: dataList[id=RuleDontA].name
   kontekst: identyfikator statusu w tekstach: `[RuleDontA]`
   limit: do 50 znaków
   EN: Rule: Targeting Le Noir Prohibited
   PL: Zasada: Zakaz Namierzania Le Noir
302. [Status [RuleDontA] — opis] - <color=#ff0000>전투 시작 시</color> 자신의 스킬 슬롯에서 가장 왼쪽의 <color=#ff0000>공격 스킬로 지정한 적이 르누아르 소속</color>이면, 아래 효과 발동 (메인 타겟 기준, 조력자 포함)\n· 태너리 규칙 위반 1 얻음\n· 이 효과 소멸\n- 턴 종료 시 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RuleDontA].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Combat Start:</color> If the main target of this unit's leftmost <color=#ff0000>Attack Skill on its Skill Slots is a "Le Noir" enemy,</color> activate the following (including Assist Units):\n  · Gain 1 Tannery Rule Violation\n  · This effect expires\n- Turn End: This effect expires
   PL: - <color=#ff0000>Na początku walki</color> jeśli główny cel skrajnie lewej <color=#ff0000>Umiejętności Ataku na slotach Umiejętności tej jednostki jest wrogiem Le Noir</color>, aktywują się następujące efekty (wliczając jednostki wsparcia)\n· Zyskuje 1 Naruszenia Zasad Garbarni\n· Ten efekt znika\n- Na koniec tury ten efekt znika
303. [Status [RuleDontB] — nazwa] 규칙: 공격 스킬 지정 금지
   źródło: Bufs.json :: dataList[id=RuleDontB].name
   kontekst: identyfikator statusu w tekstach: `[RuleDontB]`
   limit: do 60 znaków
   EN: Rule: Targeting Attack Skills Prohibited
   PL: Zasada: Zakaz Namierzania Umiejętności Ataku
304. [Status [RuleDontB] — opis] - <color=#ff0000>전투 시작 시</color> 자신의 스킬 슬롯에서 가장 왼쪽의 <color=#ff0000>공격 스킬로 지정한 적의 스킬이 공격 스킬</color>이면, 아래 효과 발동 (메인 타겟 기준, 조력자 포함)\n· 태너리 규칙 위반 1 얻음\n· 이 효과 소멸\n- 턴 종료 시 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RuleDontB].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Combat Start:</color> If the main target of this unit's leftmost <color=#ff0000>Attack Skill on its Skill Slots is an enemy Attack Skill,</color> activate the following (including Assist Units):\n  · Gain 1 Tannery Rule Violation\n  · This effect expires\n- Turn End: This effect expires
   PL: - <color=#ff0000>Na początku walki</color> jeśli Umiejętność wroga namierzanego przez skrajnie lewą <color=#ff0000>Umiejętność Ataku na slotach Umiejętności tej jednostki jest Umiejętnością Ataku</color>, aktywują się następujące efekty (wliczając jednostki wsparcia)\n· Zyskuje 1 Naruszenia Zasad Garbarni\n· Ten efekt znika\n- Na koniec tury ten efekt znika
305. [Status [RuleDontC] — nazwa] 규칙: 수비 스킬 지정 금지
   źródło: Bufs.json :: dataList[id=RuleDontC].name
   kontekst: identyfikator statusu w tekstach: `[RuleDontC]`
   limit: do 60 znaków
   EN: Rule: Targeting Defense Skills Prohibited
   PL: Zasada: Zakaz Namierzania Umiejętności Obrony
306. [Status [RuleDontC] — opis] - <color=#ff0000>전투 시작 시</color> 자신의 스킬 슬롯에서 가장 왼쪽의 <color=#ff0000>공격 스킬로 지정한 적의 스킬이 수비 스킬</color>이면, 아래 효과 발동 (메인 타겟 기준, 조력자 포함)\n· 태너리 규칙 위반 1 얻음\n· 이 효과 소멸\n- 턴 종료 시 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RuleDontC].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - <color=#ff0000>Combat Start:</color> If the main target of this unit's leftmost <color=#ff0000>Attack Skill on its Skill Slots is an enemy Defense Skill,</color> activate the following (including Assist Units):\n  · Gain 1 Tannery Rule Violation\n  · This effect expires\n- Turn End: This effect expires
   PL: - <color=#ff0000>Na początku walki</color> jeśli Umiejętność wroga namierzanego przez skrajnie lewą <color=#ff0000>Umiejętność Ataku na slotach Umiejętności tej jednostki jest Umiejętnością Obrony</color>, aktywują się następujące efekty (wliczając jednostki wsparcia)\n· Zyskuje 1 Naruszenia Zasad Garbarni\n· Ten efekt znika\n- Na koniec tury ten efekt znika
307. [Status [RuleViolation] — nazwa] 태너리 규칙 위반
   źródło: Bufs.json :: dataList[id=RuleViolation].name
   kontekst: identyfikator statusu w tekstach: `[RuleViolation]`
   limit: do 40 znaków
   EN: Tannery Rule Violation
   PL: Naruszenie Zasad Garbarni
308. [Status [RuleViolation] — opis] - 최댓값: 3\n- 오트쿠튀르::르누아르 B3F 건조장 이상에게 기본 공격 스킬로 받는 피해량 +(수치 x 5)%\n- 오트쿠튀르::르누아르 B3F 건조장 이상의 ‘퍼니싱 버니싱 피니싱’ 스킬로 받는 피해량 +(수치 x 20)%\n- 자신이 사망했으면, 다음 턴 시작 시 본체 최대 체력이 가장 높은 아군(부위)에게 이 효과를 부여함 (수치 유지, 대상 지정이 불가능한 아군은 부여 대상에서 제외, 다음 웨이브로 넘어가지 않음)\n- 턴 시작 시 적 오트쿠튀르::르누아르 B3F 건조장 이상이 없으면, 이 효과 소멸
   źródło: Bufs.json :: dataList[id=RuleViolation].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Take +(Stack x 5)% damage from Haute Couture::Le Noir B3F Drying Room Yi Sang's Base Attack Skills\n- Take +(Stack x 20)% damage from Haute Couture::Le Noir B3F Drying Room Yi Sang's "Punishing Burnishing Finishing" Skill\n- If this unit is defeated, at the next Turn Start, inflict this effect on the ally (Part) that has the highest Core HP (Stack carries over; excluding untargetable allies; does not carry over to the next wave)\n- Turn Start: If there is no enemy Haute Couture::Le Noir B3F Drying Room Yi Sang, expires
   PL: - Maks.: 3\n- Otrzymuje +(wartość x 5)% obrażeń od bazowych Umiejętności ataku Haute Couture::Le Noir B3F Izba Suszenia Yi Sang\n- Otrzymuje +(wartość x 20)% obrażeń od Umiejętności „Punishing Burnishing Finishing” Haute Couture::Le Noir B3F Izba Suszenia Yi Sang\n- Po śmierci tej jednostki na początku następnej tury nadaje ten efekt sojusznikowi (części) z najwyższym maks. HP rdzenia (wartość przechodzi dalej; sojusznicy niemożliwi do namierzenia są wykluczeni; nie przechodzi do następnej fali)\n- Na początku tury znika, jeśli wroga Haute Couture::Le Noir B3F Izba Suszenia Yi Sang nie ma na polu
309. [Status [RuleSanction] — nazwa] 규칙위반에의하는벌칙
   źródło: Bufs.json :: dataList[id=RuleSanction].name
   kontekst: identyfikator statusu w tekstach: `[RuleSanction]`
   limit: do 40 znaków
   EN: <size=120%>V</size>IOLENCE<size=120%>F</size>OR<size=120%>R</size>ULES<size=120%>V</size>IOLATED
   PL: Kara za Naruszenie Zasad
310. [Status [RuleSanction] — opis] - 최댓값: 5
   źródło: Bufs.json :: dataList[id=RuleSanction].desc
   limit: do 120 znaków
   EN: - Max Stack: 5
   PL: - Maks.: 5
311. [Status [MoreJoesu] — nazwa] 인력 충원
   źródło: Bufs.json :: dataList[id=MoreJoesu].name
   kontekst: identyfikator statusu w tekstach: `[MoreJoesu]`
   limit: do 40 znaków
   EN: Replenish Personnel
   PL: Uzupełnienie Personelu
312. [Status [MoreJoesu] — opis] - 탄환 - 죄수에 적용되는 효과\n- 탄환 - 죄수가 최대치가 될 때까지 필요한 만큼 자신의 보존 횟수를 소모하고, 소모한 보존 횟수 2당 탄환 - 죄수 1 얻음\n- 자신의 보존 횟수가 2 미만이면, 이 효과 발동하지 않음
   źródło: Bufs.json :: dataList[id=MoreJoesu].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Effect applied to Ammo - Prisoner\n- Consume Preservation Count until this unit has max Ammo - Prisoner Stacks. (Gain 1 Ammo - Prisoner for every 2 Preservation Count consumed)\n- If this unit has fewer than 2 Preservation Count, does not activate
   PL: - Efekt stosowany do Pocisku - Więzień\n- Zużywa Liczniki Zachowania, aż wartość Pocisku - Więzień osiągnie maksimum (zyskuje 1 Pocisku - Więzień za każde 2 zużyte Liczniki Zachowania)\n- Nie aktywuje się, gdy Liczników Zachowania jest mniej niż 2
313. [Status [RougeGregRed] — nazwa] 욕망의 붉은 실
   źródło: Bufs.json :: dataList[id=RougeGregRed].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregRed]`
   limit: do 40 znaków
   EN: Ruby Thread of Desire
   PL: Czerwona Nić Pożądania
314. [Status [RougeGregRed] — opis] - 자신의 맥동 횟수 최대치를 초과하여 맥동 횟수를 얻었으면, 초과값만큼 이어진 실을 보유한 아군에게 충전 횟수를 부여 (턴당 최대 10)
   źródło: Bufs.json :: dataList[id=RougeGregRed].desc
   limit: do 210 znaków
   EN: - If this unit gained Pulsation Count past its max cap, apply Charge Count equal to surplus Pulsation Count to allies that have Thread Tether (max 10 per turn)
   PL: - Jeśli jednostka zyskała Liczniki Pulsacji ponad maksimum, nadaje Liczniki Ładowania równe nadwyżce sojusznikom z Połączoną Nicią (do 10 na turę)
315. [Status [RougeGregYellow] — nazwa] 원망의 황금 실
   źródło: Bufs.json :: dataList[id=RougeGregYellow].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregYellow]`
   limit: do 40 znaków
   EN: Golden Thread of Yearning
   PL: Złota Nić Tęsknoty
316. [Status [RougeGregYellow] — opis] - 이어진 실을 보유한 아군의 스킬 피해량 +(색욕 공명 수 x 5)% (최대 20%)
   źródło: Bufs.json :: dataList[id=RougeGregYellow].desc
   limit: do 120 znaków
   EN: - Allies that have Thread Tether deal +(Lust Reson. x 5)% damage using Skills (max 20%)
   PL: - Sojusznicy z Połączoną Nicią zadają +(liczba Rezonansów Pożądania x 5)% obrażeń Umiejętnościami (maks. 20%)
317. [Status [RougeGregBlue] — nazwa] 안락의 푸른 실
   źródło: Bufs.json :: dataList[id=RougeGregBlue].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregBlue]`
   limit: do 40 znaków
   EN: Sapphire Thread of Comfort
   PL: Błękitna Nić Ukojenia
318. [Status [RougeGregBlue] — opis] - 자신의 체력을 회복할 때, 회복량만큼 이어진 실을 보유한 아군의 체력 회복 (최대 체력 초과값 포함)
   źródło: Bufs.json :: dataList[id=RougeGregBlue].desc
   limit: do 160 znaków
   EN: - When healing HP on self, heal HP on the ally that has Thread Tether by an equal amount (including surplus healing amount)
   PL: - Przy regenerowaniu własnego HP regeneruje HP sojusznikowi z Połączoną Nicią w takiej samej ilości (łącznie z nadwyżką ponad maks. HP)
319. [Status [RougeGregWarmUp] — nazwa] 붉은 결속
   źródło: Bufs.json :: dataList[id=RougeGregWarmUp].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregWarmUp]`
   limit: do 40 znaków
   EN: Bound in Crimson
   PL: Czerwony Węzeł
320. [Status [RougeGregWarmUp] — opis] - 최댓값 : 2\n- 수치당 자신의 스킬 피해량 +5% (E.G.O 스킬 포함)
   źródło: Bufs.json :: dataList[id=RougeGregWarmUp].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Skills deal +5% damage for every Stack (including E.G.O Skills)
   PL: - Maks.: 2\n- Zadaje +5% obrażeń Umiejętnościami za każdą wartość (łącznie z Umiejętnościami E.G.O)
321. [Status [RougeGregLink] — nazwa] 이어진 실
   źródło: Bufs.json :: dataList[id=RougeGregLink].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregLink]`
   limit: do 40 znaków
   EN: Thread Tether
   PL: Połączona Nić
322. [Status [RougeGregLink] — opis] - 부여한 캐릭터가 퇴각 또는 사망하거나, 다른 대상에게 이 효과를 부여하면 소멸.
   źródło: Bufs.json :: dataList[id=RougeGregLink].desc
   limit: do 160 znaków
   EN: - Expires when the character that applied this effect retreats, is defeated, or applies this effect on another target
   PL: Znika, gdy nadający się wycofa, polegnie lub przeniesie ten efekt na inną jednostkę.
323. [Status [RougeGregAutoHeal] — nazwa] 스티치
   źródło: Bufs.json :: dataList[id=RougeGregAutoHeal].name
   kontekst: identyfikator statusu w tekstach: `[RougeGregAutoHeal]`
   limit: do 40 znaków
   EN: Stitched
   PL: Zaszyty
324. [Status [RougeGregAutoHeal] — opis] - 최댓값 : 3\n- 자신의 체력이 감소하면 최대 체력의 6% 회복하고 이 효과 수치 1 감소
   źródło: Bufs.json :: dataList[id=RougeGregAutoHeal].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Upon losing HP, heal 6% HP and lose 1 Stack
   PL: - Maks.: 3\n- Przy utracie HP regeneruje 6% HP i traci 1 wartości tego efektu
325. [Status [GoldBuffet] — nazwa] 황금 수의
   źródło: Bufs.json :: dataList[id=GoldBuffet].name
   kontekst: identyfikator statusu w tekstach: `[GoldBuffet]`
   limit: do 40 znaków
   EN: Golden Shroud
   PL: Złoty Całun
326. [Status [GoldBuffet] — opis] - 최댓값 : 1\n- 방어 레벨 +3\n- 이번 전투에서 처음으로 흐트러지면, 턴 종료시 흐트러짐을 해제 (강제 흐트러짐 제외. 전투당 1회)
   źródło: Bufs.json :: dataList[id=GoldBuffet].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Defense Level +3\n- Turn End: If this unit was Staggered for the first time in this Encounter, recover from Stagger (excluding forced Stagger; once per Encounter)
   PL: - Maks.: 1\n- Poziom Obrony +3\n- Przy pierwszym Oszołomieniu w tej walce na koniec tury dochodzi do siebie z Oszołomienia (poza wymuszonym Oszołomieniem; raz na walkę)

## Statusy i efekty bojowe — Bufs_Mirror3
- plik gry: `Bufs_Mirror3.json`

327. [Status [MDcFaBa] — nazwa] 화상 추가 부여
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBa].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBa]`
   limit: do 40 znaków
   EN: Inflict additional Burn
   PL: Nadanie Dodatkowego Podpalenia
328. [Status [MDcFaBa] — opis] 스킬로 부여하는 화상 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBa].desc
   limit: do 120 znaków
   EN: Inflict +1 more Burn with Skills
   PL: Umiejętności nadają o 1 więcej Podpalenia
329. [Status [MDcFaBb] — nazwa] 출혈 추가 부여
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBb].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBb]`
   limit: do 40 znaków
   EN: Inflict additional Bleed
   PL: Nadanie Dodatkowego Krwawienia
330. [Status [MDcFaBb] — opis] 스킬로 부여하는 출혈 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBb].desc
   limit: do 120 znaków
   EN: Inflict +1 more Bleed with Skills
   PL: Umiejętności nadają o 1 więcej Krwawienia
331. [Status [MDcFaBc] — nazwa] 진동 추가 부여
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBc].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBc]`
   limit: do 40 znaków
   EN: Inflict additional Tremor
   PL: Nadanie Dodatkowego Wstrząsu
332. [Status [MDcFaBc] — opis] 스킬로 부여하는 진동 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBc].desc
   limit: do 120 znaków
   EN: Inflict +1 more Tremor with Skills
   PL: Umiejętności nadają o 1 więcej Wstrząsu
333. [Status [MDcFaBd] — nazwa] 파열 추가 부여
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBd].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBd]`
   limit: do 40 znaków
   EN: Inflict additional Rupture
   PL: Nadanie Dodatkowego Rozdarcia
334. [Status [MDcFaBd] — opis] 스킬로 부여하는 파열 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBd].desc
   limit: do 120 znaków
   EN: Inflict +1 more Rupture with Skills
   PL: Umiejętności nadają o 1 więcej Rozdarcia
335. [Status [MDcFaBe] — nazwa] 침잠 추가 부여
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBe].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBe]`
   limit: do 40 znaków
   EN: Inflict additional Sinking
   PL: Nadanie Dodatkowego Zatonięcia
336. [Status [MDcFaBe] — opis] 스킬로 부여하는 침잠 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBe].desc
   limit: do 120 znaków
   EN: Inflict +1 more Sinking with Skills
   PL: Umiejętności nadają o 1 więcej Zatonięcia
337. [Status [MDcFaBf] — nazwa] 참격 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBf].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBf]`
   limit: do 40 znaków
   EN: Slash Boost
   PL: Wzmocnienie Cięcia
338. [Status [MDcFaBf] — opis] 참격 속성으로 가하는 피해량 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBf].desc
   limit: do 120 znaków
   EN: Slash damage +15%
   PL: Zadaje +15% obrażeń typu Cięcie
339. [Status [MDcFaBg] — nazwa] 관통 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBg].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBg]`
   limit: do 40 znaków
   EN: Pierce Boost
   PL: Wzmocnienie Przebicia
340. [Status [MDcFaBg] — opis] 관통 속성으로 가하는 피해량 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBg].desc
   limit: do 120 znaków
   EN: Pierce damage +15%
   PL: Zadaje +15% obrażeń typu Przebicie
341. [Status [MDcFaBh] — nazwa] 타격 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBh].name
   kontekst: identyfikator statusu w tekstach: `[MDcFaBh]`
   limit: do 40 znaków
   EN: Blunt Boost
   PL: Wzmocnienie Uderzenia
342. [Status [MDcFaBh] — opis] 타격 속성으로 가하는 피해량 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFaBh].desc
   limit: do 120 znaków
   EN: Blunt damage +15%
   PL: Zadaje +15% obrażeń typu Uderzenie
343. [Status [MDcFbBa] — nazwa] 속성 내성 강화 (분노 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBa].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBa]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Wrath)
   PL: Odporność Atrybutów (poza Gniewem)
344. [Status [MDcFbBa] — opis] 분노 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBa].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Wrath)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Gniewem)
345. [Status [MDcFbBb] — nazwa] 속성 내성 강화 (색욕 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBb].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBb]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Lust)
   PL: Odporność Atrybutów (poza Pożądaniem)
346. [Status [MDcFbBb] — opis] 색욕 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBb].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Lust)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Pożądaniem)
347. [Status [MDcFbBc] — nazwa] 속성 내성 강화 (나태 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBc].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBc]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Sloth)
   PL: Odporność Atrybutów (poza Lenistwem)
348. [Status [MDcFbBc] — opis] 나태 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBc].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Sloth)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Lenistwem)
349. [Status [MDcFbBd] — nazwa] 속성 내성 강화 (탐식 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBd].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBd]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Glut.)
   PL: Odporność Atrybutów (poza Obżarstwem)
350. [Status [MDcFbBd] — opis] 탐식 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBd].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Gluttony)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Obżarstwem)
351. [Status [MDcFbBe] — nazwa] 속성 내성 강화 (우울 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBe].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBe]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Gloom)
   PL: Odporność Atrybutów (poza Posępnością)
352. [Status [MDcFbBe] — opis] 우울 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBe].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Gloom)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Posępnością)
353. [Status [MDcFbBf] — nazwa] 속성 내성 강화 (오만 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBf].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBf]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Pride)
   PL: Odporność Atrybutów (poza Pychą)
354. [Status [MDcFbBf] — opis] 오만 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBf].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Pride)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Pychą)
355. [Status [MDcFbBg] — nazwa] 속성 내성 강화 (질투 제외)
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBg].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBg]`
   limit: do 40 znaków
   EN: Affinity Res Up (Exc. Envy)
   PL: Odporność Atrybutów (poza Zazdrością)
356. [Status [MDcFbBg] — opis] 질투 속성을 제외한 속성의 내성 -0.1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBg].desc
   limit: do 120 znaków
   EN: Resistance against all Affinities -0.1 (Except Envy)
   PL: Odporność na wszystkie atrybuty -0.1 (poza Zazdrością)
357. [Status [MDcFbBh] — nazwa] 체력 증진
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBh].name
   kontekst: identyfikator statusu w tekstach: `[MDcFbBh]`
   limit: do 40 znaków
   EN: Max HP+
   PL: Wzrost Maks. HP
358. [Status [MDcFbBh] — opis] 최대 체력 15% 증가
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFbBh].desc
   limit: do 120 znaków
   EN: Max HP +15%
   PL: Maks. HP +15%
359. [Status [MDcFcBa] — nazwa] 슬롯 가중치 증가
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBa].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBa]`
   limit: do 40 znaków
   EN: Slot Weight +
   PL: Waga Slotów +
360. [Status [MDcFcBa] — opis] 슬롯 가중치 1 증가
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBa].desc
   limit: do 120 znaków
   EN: Slot Weight +1
   PL: Waga Slotów +1
361. [Status [MDcFcBb] — nazwa] 피해량 흡수
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBb].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBb]`
   limit: do 40 znaków
   EN: Siphon Damage
   PL: Pochłanianie Obrażeń
362. [Status [MDcFcBb] — opis] 적중 시 가한 피해량의 5%만큼 체력 회복
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBb].desc
   limit: do 120 znaków
   EN: On Hit, heal 5% of damage dealt as HP
   PL: Przy trafieniu regeneruje HP równe 5% zadanych obrażeń
363. [Status [MDcFcBc] — nazwa] 속도 증가
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBc].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBc]`
   limit: do 40 znaków
   EN: Boost Speed
   PL: Wzrost Szybkości
364. [Status [MDcFcBc] — opis] 속도 최댓값 1 증가
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBc].desc
   limit: do 120 znaków
   EN: Max Speed +1
   PL: Maksymalna Szybkość +1
365. [Status [MDcFcBd] — nazwa] 정신 공격
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBd].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBd]`
   limit: do 40 znaków
   EN: Sanity Attack
   PL: Atak na Poczytalność
366. [Status [MDcFcBd] — opis] 적중 시, 정신력 고정 피해 2 입힘
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBd].desc
   limit: do 120 znaków
   EN: On Hit, deal 2 fixed SP damage
   PL: Przy trafieniu zadaje 2 stałych obrażeń Poczytalności
367. [Status [MDcFcBe] — nazwa] 예리함
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBe].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBe]`
   limit: do 40 znaków
   EN: Keenness
   PL: Ostrość
368. [Status [MDcFcBe] — opis] 이전 턴 동안 한 번이라도 피해를 입혔다면 턴 시작 시 피해량 증가 1 얻음
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBe].desc
   limit: do 120 znaków
   EN: Turn Start: gain 1 Damage Up if this unit dealt damage at least once last turn
   PL: Jeśli w poprzedniej turze choć raz zadano obrażenia, na początku tury zyskuje 1 Wzrost Obrażeń
369. [Status [MDcFcBf] — nazwa] 재정비
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBf].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBf]`
   limit: do 40 znaków
   EN: Regroup
   PL: Reorganizacja
370. [Status [MDcFcBf] — opis] 이전 턴 동안 체력 피해를 받지 않았다면 턴 시작 시 공격 레벨 증가 3 얻음
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBf].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 3 Offense Level Up if this unit did not take HP damage last turn
   PL: Jeśli w poprzedniej turze nie otrzymano obrażeń HP, na początku tury zyskuje 3 Wzrosty Poziomu Ataku
371. [Status [MDcFcBg] — nazwa] 일방 공격 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBg].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBg]`
   limit: do 40 znaków
   EN: Unopposed Attack Boost
   PL: Wzmocnienie Ataku Niekwestionowanego
372. [Status [MDcFcBg] — opis] 일방 공격 시 최종 위력 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBg].desc
   limit: do 120 znaków
   EN: Final Power +1 to Unopposed Attacks
   PL: Moc Końcowa ataków niekwestionowanych +1
373. [Status [MDcFcBh] — nazwa] 합 공격 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBh].name
   kontekst: identyfikator statusu w tekstach: `[MDcFcBh]`
   limit: do 40 znaków
   EN: Clash Attack Boost
   PL: Wzmocnienie Ataku w Starciu
374. [Status [MDcFcBh] — opis] 합 진행 시 최종 위력 +1
   źródło: Bufs_Mirror3.json :: dataList[id=MDcFcBh].desc
   limit: do 120 znaków
   EN: Final Power +1 in a Clash
   PL: Moc Końcowa w Starciu +1
375. [Status [MDHcFaBa] — nazwa] 방어 레벨 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBa].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFaBa]`
   limit: do 40 znaków
   EN: Defense Level Up
   PL: Wzrost Poziomu Obrony
376. [Status [MDHcFaBa] — opis] 방어 레벨 +4
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBa].desc
   limit: do 120 znaków
   EN: Defense Level +4
   PL: Poziom Obrony +4
377. [Status [MDHcFaBb] — nazwa] 수비 위력 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBb].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFaBb]`
   limit: do 40 znaków
   EN: Defense Power Up
   PL: Wzrost Mocy Obrony
378. [Status [MDHcFaBb] — opis] 수비 스킬 기본 위력 +2
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBb].desc
   limit: do 120 znaków
   EN: Defense Skill Base Power +2
   PL: Moc Bazowa Umiejętności Obrony +2
379. [Status [MDHcFaBc] — nazwa] 최대 체력 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBc].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFaBc]`
   limit: do 40 znaków
   EN: Max HP Up
   PL: Wzrost Maks. HP
380. [Status [MDHcFaBc] — opis] 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBc].desc
   limit: do 120 znaków
   EN: Max HP +10%
   PL: Maks. HP +10%
381. [Status [MDHcFaBd] — nazwa] 받는 피해량 경감
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBd].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFaBd]`
   limit: do 40 znaków
   EN: Damage Taken Down
   PL: Zmniejszone Otrzymywane Obrażenia
382. [Status [MDHcFaBd] — opis] 받는 피해량 -10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFaBd].desc
   limit: do 120 znaków
   EN: Damage Taken -10%
   PL: Otrzymuje -10% obrażeń
383. [Status [MDHcFbBa] — nazwa] 공격 레벨 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBa].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFbBa]`
   limit: do 40 znaków
   EN: Offense Level Up
   PL: Wzrost Poziomu Ataku
384. [Status [MDHcFbBa] — opis] 공격 레벨 +3, 최대 체력 +5%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBa].desc
   limit: do 120 znaków
   EN: Offense Level +3, Max HP +5%
   PL: Poziom Ataku +3, Maks. HP +5%
385. [Status [MDHcFbBb] — nazwa] 최종 위력 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBb].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFbBb]`
   limit: do 40 znaków
   EN: Final Power Up
   PL: Wzrost Mocy Końcowej
386. [Status [MDHcFbBb] — opis] 최종 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBb].desc
   limit: do 120 znaków
   EN: Final Power +1, Max HP +5%
   PL: Moc Końcowa +1, Maks. HP +5%
387. [Status [MDHcFbBc] — nazwa] 기본 위력 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBc].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFbBc]`
   limit: do 40 znaków
   EN: Base Power Up
   PL: Wzrost Mocy Bazowej
388. [Status [MDHcFbBc] — opis] 기본 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBc].desc
   limit: do 120 znaków
   EN: Base Power +1, Max HP +5%
   PL: Moc Bazowa +1, Maks. HP +5%
389. [Status [MDHcFbBd] — nazwa] 가하는 피해량 강화
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBd].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFbBd]`
   limit: do 40 znaków
   EN: Damage Dealt Up
   PL: Wzrost Zadawanych Obrażeń
390. [Status [MDHcFbBd] — opis] 가하는 피해량 +15%, 최대 체력 +5%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFbBd].desc
   limit: do 120 znaków
   EN: Deal +15% damage, Max HP +5%
   PL: Zadaje +15% obrażeń, Maks. HP +5%
391. [Status [MDHcFcBa] — nazwa] 최종 위력 증폭 I
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBa].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBa]`
   limit: do 40 znaków
   EN: Final Power Up I
   PL: Amplifikacja Mocy Końcowej I
392. [Status [MDHcFcBa] — opis] 최종 위력 +1, 최대 체력 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBa].desc
   limit: do 120 znaków
   EN: Final Power +1, Max HP +15%
   PL: Moc Końcowa +1, Maks. HP +15%
393. [Status [MDHcFcBb] — nazwa] 최종 위력 증폭 II
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBb].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBb]`
   limit: do 40 znaków
   EN: Final Power Up II
   PL: Amplifikacja Mocy Końcowej II
394. [Status [MDHcFcBb] — opis] 최종 위력 +2, 방어 레벨 -4, 최대 체력 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBb].desc
   limit: do 120 znaków
   EN: Final Power +2, Defense Level -4, Max HP +15%
   PL: Moc Końcowa +2, Poziom Obrony -4, Maks. HP +15%
395. [Status [MDHcFcBc] — nazwa] 기본 위력 증폭 I
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBc].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBc]`
   limit: do 40 znaków
   EN: Base Power Up I
   PL: Amplifikacja Mocy Bazowej I
396. [Status [MDHcFcBc] — opis] 기본 위력 +1, 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBc].desc
   limit: do 120 znaków
   EN: Base Power +1, Max HP +10%
   PL: Moc Bazowa +1, Maks. HP +10%
397. [Status [MDHcFcBd] — nazwa] 기본 위력 증폭 II
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBd].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBd]`
   limit: do 40 znaków
   EN: Base Power Up II
   PL: Amplifikacja Mocy Bazowej II
398. [Status [MDHcFcBd] — opis] 기본 위력 +2, 방어 레벨 -4, 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBd].desc
   limit: do 120 znaków
   EN: Base Power +2, Defense Level -4, Max HP +10%
   PL: Moc Bazowa +2, Poziom Obrony -4, Maks. HP +10%
399. [Status [MDHcFcBe] — nazwa] 코인 위력 증폭 I
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBe].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBe]`
   limit: do 40 znaków
   EN: Coin Power Up I
   PL: Amplifikacja Mocy Monet I
400. [Status [MDHcFcBe] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBe].desc
   limit: do 120 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1
   PL: Moc Monet Plus +1, Moc Monet Minus -1
401. [Status [MDHcFcBf] — nazwa] 과부하 I
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBf].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFcBf]`
   limit: do 40 znaków
   EN: Overload I
   PL: Przeciążenie I
402. [Status [MDHcFcBf] — opis] 공격 레벨 +7, 방어 레벨 -7
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFcBf].desc
   limit: do 120 znaków
   EN: Offense Level +7, Defense Level -7
   PL: Poziom Ataku +7, Poziom Obrony -7
403. [Status [MDHcFdBa] — nazwa] 최종 위력 증폭 III
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBa].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBa]`
   limit: do 40 znaków
   EN: Final Power Up III
   PL: Amplifikacja Mocy Końcowej III
404. [Status [MDHcFdBa] — opis] 최종 위력 +2, 방어 레벨 +6, 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBa].desc
   limit: do 120 znaków
   EN: Final Power +2, Defense Level +6, Max HP +10%
   PL: Moc Końcowa +2, Poziom Obrony +6, Maks. HP +10%
405. [Status [MDHcFdBb] — nazwa] 최종 위력 증폭 IV
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBb].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBb]`
   limit: do 40 znaków
   EN: Final Power Up IV
   PL: Amplifikacja Mocy Końcowej IV
406. [Status [MDHcFdBb] — opis] 최종 위력 +3, 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBb].desc
   limit: do 120 znaków
   EN: Final Power +3, Max HP +10%
   PL: Moc Końcowa +3, Maks. HP +10%
407. [Status [MDHcFdBc] — nazwa] 코인 위력 증폭 II
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBc].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBc]`
   limit: do 40 znaków
   EN: Coin Power Up II
   PL: Amplifikacja Mocy Monet II
408. [Status [MDHcFdBc] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1, 최대 체력 +15%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBc].desc
   limit: do 120 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Max HP +15%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Maks. HP +15%
409. [Status [MDHcFdBd] — nazwa] 기본 위력 증폭 III
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBd].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBd]`
   limit: do 40 znaków
   EN: Base Power Up III
   PL: Amplifikacja Mocy Bazowej III
410. [Status [MDHcFdBd] — opis] 기본 위력 +2, 방어 레벨 +3, 최대 체력 +10%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBd].desc
   limit: do 120 znaków
   EN: Base Power +2, Defense Level +3, Max HP +10%
   PL: Moc Bazowa +2, Poziom Obrony +3, Maks. HP +10%
411. [Status [MDHcFdBe] — nazwa] 과부하 II
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBe].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBe]`
   limit: do 40 znaków
   EN: Overload II
   PL: Przeciążenie II
412. [Status [MDHcFdBe] — opis] 공격 레벨 +10, 방어 레벨 -7
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBe].desc
   limit: do 120 znaków
   EN: Offense Level +10, Defense Level -7
   PL: Poziom Ataku +10, Poziom Obrony -7
413. [Status [MDHcFdBf] — nazwa] 강인함
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBf].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBf]`
   limit: do 40 znaków
   EN: Resilient
   PL: Twardość
414. [Status [MDHcFdBf] — opis] 최대 체력 +25%, 방어 레벨 +5
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBf].desc
   limit: do 120 znaków
   EN: Max HP +25%, Defense Level +5
   PL: Maks. HP +25%, Poziom Obrony +5
415. [Status [MDHcFdBg] — nazwa] 완강함
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBg].name
   kontekst: identyfikator statusu w tekstach: `[MDHcFdBg]`
   limit: do 40 znaków
   EN: Headstrong
   PL: Nieustępliwość
416. [Status [MDHcFdBg] — opis] 가하는 피해량 +50%, 받는 피해량 -50%
   źródło: Bufs_Mirror3.json :: dataList[id=MDHcFdBg].desc
   limit: do 120 znaków
   EN: Deal +50% damage and take -50% damage
   PL: Zadaje +50% obrażeń i otrzymuje -50% obrażeń

## Statusy i efekty bojowe — Bufs_Mirror4
- plik gry: `Bufs_Mirror4.json`

417. [Status [MDEMaa] — nazwa] 방어 레벨 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMaa].name
   kontekst: identyfikator statusu w tekstach: `[MDEMaa]`
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Status [MDEMaa] — opis] 방어 레벨 +2
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMaa].desc
   limit: do 120 znaków
   EN: Defense Level +2
   PL: Poziom Obrony +2
419. [Status [MDEMab] — nazwa] 수비 스킬 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMab].name
   kontekst: identyfikator statusu w tekstach: `[MDEMab]`
   limit: do 40 znaków
   EN: Defense Skill Up
   PL: Wzmocnienie Umiejętności Obrony
420. [Status [MDEMab] — opis] 수비 스킬 최종 위력 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMab].desc
   limit: do 120 znaków
   EN: Defense Skill Final Power +1
   PL: Moc Końcowa Umiejętności Obrony +1
421. [Status [MDEMac] — nazwa] 공격 레벨 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMac].name
   kontekst: identyfikator statusu w tekstach: `[MDEMac]`
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Status [MDEMac] — opis] 공격 레벨 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMac].desc
   limit: do 120 znaków
   EN: Offense Level +1
   PL: Poziom Ataku +1
423. [Status [MDEMad] — nazwa] 최대 체력 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMad].name
   kontekst: identyfikator statusu w tekstach: `[MDEMad]`
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Status [MDEMad] — opis] 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMad].desc
   limit: do 120 znaków
   EN: Max HP +5%
   PL: Maks. HP +5%
425. [Status [MDEMae] — nazwa] 받는 피해량 감소 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMae].name
   kontekst: identyfikator statusu w tekstach: `[MDEMae]`
   limit: do 40 znaków
   EN: Take Less Damage
   PL: Spadek Otrzymywanych Obrażeń
426. [Status [MDEMae] — opis] 받는 피해량 -5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMae].desc
   limit: do 120 znaków
   EN: Damage Taken -5%
   PL: Otrzymuje -5% obrażeń
427. [Status [MDEMca] — nazwa] 육체 비대
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMca].name
   kontekst: identyfikator statusu w tekstach: `[MDEMca]`
   limit: do 40 znaków
   EN: Body Corpulence
   PL: Otyłość Ciała
428. [Status [MDEMca] — opis] 공격 레벨 +2, 방어 레벨 +2, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMca].desc
   limit: do 120 znaków
   EN: Offense Level +2, Defense Level +2, Max HP +5%
   PL: Poziom Ataku +2, Poziom Obrony +2, Maks. HP +5%
429. [Status [MDEMcb] — nazwa] 육체 강대
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcb].name
   kontekst: identyfikator statusu w tekstach: `[MDEMcb]`
   limit: do 40 znaków
   EN: Body Reinforcement
   PL: Wzmocnienie Ciała
430. [Status [MDEMcb] — opis] 공격 레벨 +2, 방어 레벨 +4
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcb].desc
   limit: do 120 znaków
   EN: Offense Level +2, Defense Level +4
   PL: Poziom Ataku +2, Poziom Obrony +4
431. [Status [MDEMcc] — nazwa] 최대 체력 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcc].name
   kontekst: identyfikator statusu w tekstach: `[MDEMcc]`
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Status [MDEMcc] — opis] 최대 체력 +20%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcc].desc
   limit: do 120 znaków
   EN: Max HP +20%
   PL: Maks. HP +20%
433. [Status [MDEMcd] — nazwa] 최종 공격 증강
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcd].name
   kontekst: identyfikator statusu w tekstach: `[MDEMcd]`
   limit: do 40 znaków
   EN: Final Attack Boost
   PL: Wzmocnienie Ataku Końcowego
434. [Status [MDEMcd] — opis] 최종 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcd].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Status [MDEMce] — nazwa] 기본 공격 증강
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMce].name
   kontekst: identyfikator statusu w tekstach: `[MDEMce]`
   limit: do 40 znaków
   EN: Base Attack Boost
   PL: Wzmocnienie Ataku Bazowego
436. [Status [MDEMce] — opis] 기본 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMce].desc
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Status [MDEMcf] — nazwa] 합 공격 증강
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcf].name
   kontekst: identyfikator statusu w tekstach: `[MDEMcf]`
   limit: do 40 znaków
   EN: Clash Attack Boost
   PL: Wzmocnienie Ataku w Starciu
438. [Status [MDEMcf] — opis] 합 위력 +2, 방어 레벨 -3
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcf].desc
   limit: do 120 znaków
   EN: Clash Power +2, Defense Level -3
   PL: Moc Starcia +2, Poziom Obrony -3
439. [Status [MDEMcg] — nazwa] 최종 위력 강화
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcg].name
   kontekst: identyfikator statusu w tekstach: `[MDEMcg]`
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Status [MDEMcg] — opis] 최종 위력 +1, 수비 스킬 최종 위력 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMcg].desc
   limit: do 120 znaków
   EN: Final Power +1, Defense Skill Final Power+1
   PL: Moc Końcowa +1, Moc Końcowa Umiejętności Obrony +1
441. [Status [MDEMda] — nazwa] 육체 신장
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMda].name
   kontekst: identyfikator statusu w tekstach: `[MDEMda]`
   limit: do 40 znaków
   EN: Body Growth
   PL: Rozrost Ciała
442. [Status [MDEMda] — opis] 공격 레벨 +3, 방어 레벨 +2, 최대 체력 +10%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMda].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +2, Max HP +10%
   PL: Poziom Ataku +3, Poziom Obrony +2, Maks. HP +10%
443. [Status [MDEMdb] — nazwa] 육체 보강
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdb].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdb]`
   limit: do 40 znaków
   EN: Body Fortification
   PL: Umacnianie Ciała
444. [Status [MDEMdb] — opis] 공격 레벨 +5, 최대 체력 +7.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdb].desc
   limit: do 120 znaków
   EN: Offense Level +5, Max HP +7.5%
   PL: Poziom Ataku +5, Maks. HP +7.5%
445. [Status [MDEMdc] — nazwa] 기본 전투 장비
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdc].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdc]`
   limit: do 40 znaków
   EN: Base Combat Gear
   PL: Podstawowy Ekwipunek Bojowy
446. [Status [MDEMdc] — opis] 기본 위력 +1, 방어 레벨 +3, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdc].desc
   limit: do 120 znaków
   EN: Base Power +1, Defense Level +3, Max HP +5%
   PL: Moc Bazowa +1, Poziom Obrony +3, Maks. HP +5%
447. [Status [MDEMdd] — nazwa] 최종 전투 장비
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdd].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdd]`
   limit: do 40 znaków
   EN: Final Combat Gear
   PL: Końcowy Ekwipunek Bojowy
448. [Status [MDEMdd] — opis] 최종 위력 +1, 방어 레벨 -2, 최대 체력 +17.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdd].desc
   limit: do 120 znaków
   EN: Final Power +1, Defense Level -2, Max HP +17.5%
   PL: Moc Końcowa +1, Poziom Obrony -2, Maks. HP +17.5%
449. [Status [MDEMde] — nazwa] 방어 장비
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMde].name
   kontekst: identyfikator statusu w tekstach: `[MDEMde]`
   limit: do 40 znaków
   EN: Defense Gear
   PL: Ekwipunek Obronny
450. [Status [MDEMde] — opis] 방어 레벨+3, 최대 체력 +22.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMde].desc
   limit: do 120 znaków
   EN: Defense Level +3, Max HP +22.5%
   PL: Poziom Obrony +3, Maks. HP +22.5%
451. [Status [MDEMdf] — nazwa] 코인 공격 증강
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdf].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdf]`
   limit: do 40 znaków
   EN: Coin Attack Boost
   PL: Wzmocnienie Ataku Monet
452. [Status [MDEMdf] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1, 방어 레벨 +2
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdf].desc
   limit: do 120 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Defense Level +2
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Poziom Obrony +2
453. [Status [MDEMdg] — nazwa] 강대무비
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdg].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdg]`
   limit: do 40 znaków
   EN: Peerless Might
   PL: Niezrównana Siła
454. [Status [MDEMdg] — opis] 기본 위력 +1, 더하기 코인 위력 +1, 빼기 코인 위력 -1
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdg].desc
   limit: do 120 znaków
   EN: Base Power +1, Plus Coin Power +1, Minus Coin Power -1
   PL: Moc Bazowa +1, Moc Monet Plus +1, Moc Monet Minus -1
455. [Status [MDEMdh] — nazwa] 되와 말로 주기
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdh].name
   kontekst: identyfikator statusu w tekstach: `[MDEMdh]`
   limit: do 40 znaków
   EN: Eyes and Teeth for an Eye
   PL: Oczy i Zęby za Oko
456. [Status [MDEMdh] — opis] 받는 피해량 -25%, 가하는 피해량 +25%
   źródło: Bufs_Mirror4.json :: dataList[id=MDEMdh].desc
   limit: do 120 znaków
   EN: Damage Taken -25%, Damage Dealt +25%
   PL: Otrzymuje -25% obrażeń, zadaje +25% obrażeń
457. [Status [MDHMaa] — nazwa] 육체 증폭 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMaa].name
   kontekst: identyfikator statusu w tekstach: `[MDHMaa]`
   limit: do 40 znaków
   EN: Amplify Body I
   PL: Amplifikacja Ciała Ⅰ
458. [Status [MDHMaa] — opis] 공격 레벨 +1, 방어 레벨 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMaa].desc
   limit: do 120 znaków
   EN: Offense Level +1, Defense Level +1
   PL: Poziom Ataku +1, Poziom Obrony +1
459. [Status [MDHMab] — nazwa] 단단함
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMab].name
   kontekst: identyfikator statusu w tekstach: `[MDHMab]`
   limit: do 40 znaków
   EN: Durable
   PL: Wytrzymałość
460. [Status [MDHMab] — opis] 방어 레벨 +2, 수비 스킬 최종 위력 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMab].desc
   limit: do 120 znaków
   EN: Defense Level +2, Defense Skill Final Power +1
   PL: Poziom Obrony +2, Moc Końcowa Umiejętności Obrony +1
461. [Status [MDHMac] — nazwa] 육체 확대 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMac].name
   kontekst: identyfikator statusu w tekstach: `[MDHMac]`
   limit: do 40 znaków
   EN: Expand Body I
   PL: Powiększenie Ciała Ⅰ
462. [Status [MDHMac] — opis] 방어 레벨 +1, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMac].desc
   limit: do 120 znaków
   EN: Defense Level +1, Max HP +5%
   PL: Poziom Obrony +1, Maks. HP +5%
463. [Status [MDHMad] — nazwa] 최대 체력 증강 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMad].name
   kontekst: identyfikator statusu w tekstach: `[MDHMad]`
   limit: do 40 znaków
   EN: Max HP Boost I
   PL: Wzmocnienie Maks. HP Ⅰ
464. [Status [MDHMad] — opis] 최대 체력 +7.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMad].desc
   limit: do 120 znaków
   EN: Max HP +7.5%
   PL: Maks. HP +7.5%
465. [Status [MDHMae] — nazwa] 받는 피해량 경감
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMae].name
   kontekst: identyfikator statusu w tekstach: `[MDHMae]`
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Status [MDHMae] — opis] 받는 피해량 -7.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMae].desc
   limit: do 120 znaków
   EN: Damage Taken -7.5%
   PL: Otrzymuje -7.5% obrażeń
467. [Status [MDHMba] — nazwa] 육체 증폭 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMba].name
   kontekst: identyfikator statusu w tekstach: `[MDHMba]`
   limit: do 40 znaków
   EN: Amplify Body II
   PL: Amplifikacja Ciała Ⅱ
468. [Status [MDHMba] — opis] 공격 레벨 +2, 방어 레벨 +2, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMba].desc
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Status [MDHMbb] — nazwa] 육체 확대 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbb].name
   kontekst: identyfikator statusu w tekstach: `[MDHMbb]`
   limit: do 40 znaków
   EN: Expand Body II
   PL: Powiększenie Ciała Ⅱ
470. [Status [MDHMbb] — opis] 공격 레벨 +2, 최대 체력 +10%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbb].desc
   limit: do 120 znaków
   EN: Offense Level +2, Max HP +10%
   PL: Poziom Ataku +2, Maks. HP +10%
471. [Status [MDHMbc] — nazwa] 최종 위력 증강 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbc].name
   kontekst: identyfikator statusu w tekstach: `[MDHMbc]`
   limit: do 40 znaków
   EN: Final Power Boost I
   PL: Wzmocnienie Mocy Końcowej Ⅰ
472. [Status [MDHMbc] — opis] 최종 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbc].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Status [MDHMbd] — nazwa] 기본 위력 증강 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbd].name
   kontekst: identyfikator statusu w tekstach: `[MDHMbd]`
   limit: do 40 znaków
   EN: Base Power Boost I
   PL: Wzmocnienie Mocy Bazowej Ⅰ
474. [Status [MDHMbd] — opis] 기본 위력 +1, 방어 레벨 +1
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbd].desc
   limit: do 120 znaków
   EN: Base Power +1, Defense Level +1
   PL: Moc Bazowa +1, Poziom Obrony +1
475. [Status [MDHMbe] — nazwa] 강인함 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbe].name
   kontekst: identyfikator statusu w tekstach: `[MDHMbe]`
   limit: do 40 znaków
   EN: Resilient I
   PL: Twardość Ⅰ
476. [Status [MDHMbe] — opis] 방어 레벨 +4, 최대 체력 +10%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbe].desc
   limit: do 120 znaków
   EN: Defense Level +4, Max HP +10%
   PL: Poziom Obrony +4, Maks. HP +10%
477. [Status [MDHMbf] — nazwa] 말로 주기Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbf].name
   kontekst: identyfikator statusu w tekstach: `[MDHMbf]`
   limit: do 40 znaków
   EN: Take an Eye I
   PL: Zęby za Oko Ⅰ
478. [Status [MDHMbf] — opis] 받는 피해량 -10%, 가하는 피해량 +10%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMbf].desc
   limit: do 120 znaków
   EN: Damage Taken -10%, Damage Dealt +10%
   PL: Otrzymuje -10% obrażeń, zadaje +10% obrażeń
479. [Status [MDHMca] — nazwa] 육체 증폭 Ⅲ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMca].name
   kontekst: identyfikator statusu w tekstach: `[MDHMca]`
   limit: do 40 znaków
   EN: Amplify Body III
   PL: Amplifikacja Ciała Ⅲ
480. [Status [MDHMca] — opis] 공격 레벨 +4, 방어 레벨 +3, 최대 체력 +7.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMca].desc
   limit: do 120 znaków
   EN: Offense Level +4, Defense Level +3, Max HP +7.5%
   PL: Poziom Ataku +4, Poziom Obrony +3, Maks. HP +7.5%
481. [Status [MDHMcb] — nazwa] 육체 확대 Ⅲ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcb].name
   kontekst: identyfikator statusu w tekstach: `[MDHMcb]`
   limit: do 40 znaków
   EN: Expand Body III
   PL: Powiększenie Ciała Ⅲ
482. [Status [MDHMcb] — opis] 공격 레벨 +4, 최대 체력 +15%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcb].desc
   limit: do 120 znaków
   EN: Offense Level +4, Max HP +15%
   PL: Poziom Ataku +4, Maks. HP +15%
483. [Status [MDHMcc] — nazwa] 최종 위력 증강 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcc].name
   kontekst: identyfikator statusu w tekstach: `[MDHMcc]`
   limit: do 40 znaków
   EN: Final Power Boost II
   PL: Wzmocnienie Mocy Końcowej Ⅱ
484. [Status [MDHMcc] — opis] 최종 위력 +1, 방어 레벨 +6
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcc].desc
   limit: do 120 znaków
   EN: Final Power +1, Defense Level +6
   PL: Moc Końcowa +1, Poziom Obrony +6
485. [Status [MDHMcd] — nazwa] 기본 위력 증강 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcd].name
   kontekst: identyfikator statusu w tekstach: `[MDHMcd]`
   limit: do 40 znaków
   EN: Base Power Boost II
   PL: Wzmocnienie Mocy Bazowej Ⅱ
486. [Status [MDHMcd] — opis] 기본 위력 +1, 방어 레벨 +5
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcd].desc
   limit: do 120 znaków
   EN: Base Power +1, Defense Level +5
   PL: Moc Bazowa +1, Poziom Obrony +5
487. [Status [MDHMce] — nazwa] 최종 위력 증강 Ⅲ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMce].name
   kontekst: identyfikator statusu w tekstach: `[MDHMce]`
   limit: do 40 znaków
   EN: Final Power Boost III
   PL: Wzmocnienie Mocy Końcowej Ⅲ
488. [Status [MDHMce] — opis] 최종 위력 +2, 방어 레벨 -2, 최대 체력 +5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMce].desc
   limit: do 120 znaków
   EN: Final Power +2, Defense Level -2, Max HP +5%
   PL: Moc Końcowa +2, Poziom Obrony -2, Maks. HP +5%
489. [Status [MDHMcf] — nazwa] 최대 체력 증강 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcf].name
   kontekst: identyfikator statusu w tekstach: `[MDHMcf]`
   limit: do 40 znaków
   EN: Max HP Boost II
   PL: Wzmocnienie Maks. HP Ⅱ
490. [Status [MDHMcf] — opis] 최대 체력 +30%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcf].desc
   limit: do 120 znaków
   EN: Max HP +30%
   PL: Maks. HP +30%
491. [Status [MDHMcg] — nazwa] 합 공격 증강 Ⅰ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcg].name
   kontekst: identyfikator statusu w tekstach: `[MDHMcg]`
   limit: do 40 znaków
   EN: Clash Attack Boost I
   PL: Wzmocnienie Ataku w Starciu Ⅰ
492. [Status [MDHMcg] — opis] 합 위력 +2, 최대 체력 +7.5%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMcg].desc
   limit: do 120 znaków
   EN: Clash Power +2, Max HP +7.5%
   PL: Moc Starcia +2, Maks. HP +7.5%
493. [Status [MDHMda] — nazwa] 육체 증폭  Ⅳ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMda].name
   kontekst: identyfikator statusu w tekstach: `[MDHMda]`
   limit: do 40 znaków
   EN: Amplify Body IV
   PL: Amplifikacja Ciała Ⅳ
494. [Status [MDHMda] — opis] 공격 레벨 +6, 방어 레벨 +6, 최대 체력 +15%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMda].desc
   limit: do 120 znaków
   EN: Offense Level +6, Defense Level +6, Max HP +15%
   PL: Poziom Ataku +6, Poziom Obrony +6, Maks. HP +15%
495. [Status [MDHMdb] — nazwa] 육체 확대  Ⅳ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdb].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdb]`
   limit: do 40 znaków
   EN: Expand Body IV
   PL: Powiększenie Ciała Ⅳ
496. [Status [MDHMdb] — opis] 공격 레벨 +4, 방어 레벨 +3, 최대 체력 +30%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdb].desc
   limit: do 120 znaków
   EN: Offense Level +4, Defense Level +3, Max HP +30%
   PL: Poziom Ataku +4, Poziom Obrony +3, Maks. HP +30%
497. [Status [MDHMdc] — nazwa] 최종 위력 증강 Ⅳ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdc].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdc]`
   limit: do 40 znaków
   EN: Final Power Boost IV
   PL: Wzmocnienie Mocy Końcowej Ⅳ
498. [Status [MDHMdc] — opis] 최종 위력 +2, 최대 체력 +25%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdc].desc
   limit: do 120 znaków
   EN: Final Power +2, Max HP +25%
   PL: Moc Końcowa +2, Maks. HP +25%
499. [Status [MDHMdd] — nazwa] 기본 위력 증강 Ⅲ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdd].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdd]`
   limit: do 40 znaków
   EN: Base Power Boost III
   PL: Wzmocnienie Mocy Bazowej Ⅲ
500. [Status [MDHMdd] — opis] 기본 위력 +1, 최종 위력 +1, 최대 체력 +20%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdd].desc
   limit: do 120 znaków
   EN: Base Power +1, Final Power +1, Max HP +20%
   PL: Moc Bazowa +1, Moc Końcowa +1, Maks. HP +20%
501. [Status [MDHMde] — nazwa] 강인함 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMde].name
   kontekst: identyfikator statusu w tekstach: `[MDHMde]`
   limit: do 40 znaków
   EN: Resilient II
   PL: Twardość Ⅱ
502. [Status [MDHMde] — opis] 방어 레벨+9, 최대 체력 +30%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMde].desc
   limit: do 120 znaków
   EN: Defense Level +9, Max HP +30%
   PL: Poziom Obrony +9, Maks. HP +30%
503. [Status [MDHMdf] — nazwa] 코인 위력 증강
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdf].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdf]`
   limit: do 40 znaków
   EN: Coin Power Boost
   PL: Wzmocnienie Mocy Monet
504. [Status [MDHMdf] — opis] 더하기 코인 위력 +2, 빼기 코인 위력 -2
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdf].desc
   limit: do 120 znaków
   EN: Plus Coin Power +2, Minus Coin Power -2
   PL: Moc Monet Plus +2, Moc Monet Minus -2
505. [Status [MDHMdg] — nazwa] 합 공격 증강 Ⅱ
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdg].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdg]`
   limit: do 40 znaków
   EN: Clash Attack Boost II
   PL: Wzmocnienie Ataku w Starciu Ⅱ
506. [Status [MDHMdg] — opis] 합 위력 +2, 최대 체력 +30%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdg].desc
   limit: do 120 znaków
   EN: Clash Power +2, Max HP +30%
   PL: Moc Starcia +2, Maks. HP +30%
507. [Status [MDHMdh] — nazwa] 완강함
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdh].name
   kontekst: identyfikator statusu w tekstach: `[MDHMdh]`
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Status [MDHMdh] — opis] 받는 피해량 -50%, 가하는 피해량 +50%
   źródło: Bufs_Mirror4.json :: dataList[id=MDHMdh].desc
   limit: do 120 znaków
   EN: Damage Taken -50%, Damage Dealt +50%
   PL: Otrzymuje -50% obrażeń, zadaje +50% obrażeń
509. [Status [AccumulatedPastMirror] — nazwa] 축적된 과거
   źródło: Bufs_Mirror4.json :: dataList[id=AccumulatedPastMirror].name
   kontekst: identyfikator statusu w tekstach: `[AccumulatedPastMirror]`
   limit: do 40 znaków
   EN: Accumulated Past
   PL: Zakumulowana Przeszłość
510. [Status [AccumulatedPastMirror] — opis] 턴 종료 시, 11씩 증가함.\n몸통 부위 파괴 시, 전부 소모됨.
   źródło: Bufs_Mirror4.json :: dataList[id=AccumulatedPastMirror].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 11 at the end of the Turn.\nSpent completely when the Body Part is broken.
   PL: Na koniec tury rośnie o 11.\nZużywana całkowicie przy zniszczeniu części Tułowia.

## Statusy i efekty bojowe — Bufs_Mirror5
- plik gry: `Bufs_Mirror5.json`

511. [Status [MD511] — nazwa] 공격 레벨 강화 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD511].name
   kontekst: identyfikator statusu w tekstach: `[MD511]`
   limit: do 40 znaków
   EN: Offense Level Up I
   PL: Wzrost Poziomu Ataku I
512. [Status [MD511] — opis] 공격 레벨 +1
   źródło: Bufs_Mirror5.json :: dataList[id=MD511].desc
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Status [MD512] — nazwa] 방어 레벨 강화
   źródło: Bufs_Mirror5.json :: dataList[id=MD512].name
   kontekst: identyfikator statusu w tekstach: `[MD512]`
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Status [MD512] — opis] 방어 레벨 +2
   źródło: Bufs_Mirror5.json :: dataList[id=MD512].desc
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Status [MD513] — nazwa] 강인함 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD513].name
   kontekst: identyfikator statusu w tekstach: `[MD513]`
   limit: do 40 znaków
   EN: Resilient I
   PL: Twardość I
516. [Status [MD513] — opis] 방어 레벨 +1, 최대 체력 +2.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD513].desc
   limit: do 120 znaków
   EN: Defense Level +1, Max HP +2.5%
   PL: Poziom Obrony +1, Maks. HP +2.5%
517. [Status [MD514] — nazwa] 성장 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD514].name
   kontekst: identyfikator statusu w tekstach: `[MD514]`
   limit: do 40 znaków
   EN: Growth I
   PL: Rozwój I
518. [Status [MD514] — opis] 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD514].desc
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Status [MD515] — nazwa] 수비 스킬 강화
   źródło: Bufs_Mirror5.json :: dataList[id=MD515].name
   kontekst: identyfikator statusu w tekstach: `[MD515]`
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Status [MD515] — opis] 수비 스킬 최종 위력 +1
   źródło: Bufs_Mirror5.json :: dataList[id=MD515].desc
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Status [MD516] — nazwa] 받는 피해량 감소 강화
   źródło: Bufs_Mirror5.json :: dataList[id=MD516].name
   kontekst: identyfikator statusu w tekstach: `[MD516]`
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Status [MD516] — opis] 받는 피해량 -5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD516].desc
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Status [MD521] — nazwa] 공격 레벨 강화 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD521].name
   kontekst: identyfikator statusu w tekstach: `[MD521]`
   limit: do 40 znaków
   EN: Offense Level Up II
   PL: Wzrost Poziomu Ataku II
524. [Status [MD521] — opis] 공격 레벨 +2
   źródło: Bufs_Mirror5.json :: dataList[id=MD521].desc
   limit: do 120 znaków
   EN: Offense Level +2
   PL: Poziom Ataku +2
525. [Status [MD522] — nazwa] 육체 강화 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD522].name
   kontekst: identyfikator statusu w tekstach: `[MD522]`
   limit: do 40 znaków
   EN: Body Up I
   PL: Umocnienie Ciała I
526. [Status [MD522] — opis] 공격 레벨 +1, 방어 레벨 +1, 최대 체력 +2.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD522].desc
   limit: do 120 znaków
   EN: Offense Level +1, Defense Level +1, Max HP +2.5%
   PL: Poziom Ataku +1, Poziom Obrony +1, Maks. HP +2.5%
527. [Status [MD523] — nazwa] 예리 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD523].name
   kontekst: identyfikator statusu w tekstach: `[MD523]`
   limit: do 40 znaków
   EN: Keen I
   PL: Ostrość I
528. [Status [MD523] — opis] 공격 레벨 +1, 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD523].desc
   limit: do 120 znaków
   EN: Offense Level +1, Max HP +5%
   PL: Poziom Ataku +1, Maks. HP +5%
529. [Status [MD524] — nazwa] 강인함 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD524].name
   kontekst: identyfikator statusu w tekstach: `[MD524]`
   limit: do 40 znaków
   EN: Resilient II
   PL: Twardość II
530. [Status [MD524] — opis] 방어 레벨 +1, 최대 체력 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD524].desc
   limit: do 120 znaków
   EN: Defense Level +1, Max HP +7.5%
   PL: Poziom Obrony +1, Maks. HP +7.5%
531. [Status [MD525] — nazwa] 강인함 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD525].name
   kontekst: identyfikator statusu w tekstach: `[MD525]`
   limit: do 40 znaków
   EN: Resilient III
   PL: Twardość III
532. [Status [MD525] — opis] 방어 레벨 +2, 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD525].desc
   limit: do 120 znaków
   EN: Defense Level +2, Max HP +5%
   PL: Poziom Obrony +2, Maks. HP +5%
533. [Status [MD526] — nazwa] 성장 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD526].name
   kontekst: identyfikator statusu w tekstach: `[MD526]`
   limit: do 40 znaków
   EN: Growth II
   PL: Rozwój II
534. [Status [MD526] — opis] 최대 체력 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD526].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Status [MD527] — nazwa] 완강함 I
   źródło: Bufs_Mirror5.json :: dataList[id=MD527].name
   kontekst: identyfikator statusu w tekstach: `[MD527]`
   limit: do 40 znaków
   EN: Headstrong I
   PL: Nieustępliwość I
536. [Status [MD527] — opis] 받는 피해량 -7.5%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD527].desc
   limit: do 120 znaków
   EN: Damage Taken -7.5%, Damage Dealt +7.5%
   PL: Otrzymuje -7.5% obrażeń, zadaje +7.5% obrażeń
537. [Status [MD531] — nazwa] 예리 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD531].name
   kontekst: identyfikator statusu w tekstach: `[MD531]`
   limit: do 40 znaków
   EN: Keen II
   PL: Ostrość II
538. [Status [MD531] — opis] 공격 레벨 +2, 최대 체력 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD531].desc
   limit: do 120 znaków
   EN: Offense Level +2, Max HP +7.5%
   PL: Poziom Ataku +2, Maks. HP +7.5%
539. [Status [MD532] — nazwa] 예리 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD532].name
   kontekst: identyfikator statusu w tekstach: `[MD532]`
   limit: do 40 znaków
   EN: Keen III
   PL: Ostrość III
540. [Status [MD532] — opis] 공격 레벨 +3, 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD532].desc
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Status [MD533] — nazwa] 강인함 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD533].name
   kontekst: identyfikator statusu w tekstach: `[MD533]`
   limit: do 40 znaków
   EN: Resilient IV
   PL: Twardość IV
542. [Status [MD533] — opis] 방어 레벨 +3, 최대 체력 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD533].desc
   limit: do 120 znaków
   EN: Defense Level +3, Max HP +7.5%
   PL: Poziom Obrony +3, Maks. HP +7.5%
543. [Status [MD534] — nazwa] 강인함 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD534].name
   kontekst: identyfikator statusu w tekstach: `[MD534]`
   limit: do 40 znaków
   EN: Resilient V
   PL: Twardość V
544. [Status [MD534] — opis] 방어 레벨 +4, 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD534].desc
   limit: do 120 znaków
   EN: Defense Level +4, Max HP +5%
   PL: Poziom Obrony +4, Maks. HP +5%
545. [Status [MD535] — nazwa] 성장 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD535].name
   kontekst: identyfikator statusu w tekstach: `[MD535]`
   limit: do 40 znaków
   EN: Growth III
   PL: Rozwój III
546. [Status [MD535] — opis] 최대 체력 +15%
   źródło: Bufs_Mirror5.json :: dataList[id=MD535].desc
   limit: do 120 znaków
   EN: Max HP +15%
   PL: Maks. HP +15%
547. [Status [MD536] — nazwa] 합 위력 증폭
   źródło: Bufs_Mirror5.json :: dataList[id=MD536].name
   kontekst: identyfikator statusu w tekstach: `[MD536]`
   limit: do 40 znaków
   EN: Clash Power Boost
   PL: Amplifikacja Mocy Starcia
548. [Status [MD536] — opis] 합 위력 +1, 최대 체력 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD536].desc
   limit: do 120 znaków
   EN: Clash Power +1, Max HP +7.5%
   PL: Moc Starcia +1, Maks. HP +7.5%
549. [Status [MD537] — nazwa] 최종 위력 증폭
   źródło: Bufs_Mirror5.json :: dataList[id=MD537].name
   kontekst: identyfikator statusu w tekstach: `[MD537]`
   limit: do 40 znaków
   EN: Final Power Boost
   PL: Amplifikacja Mocy Końcowej
550. [Status [MD537] — opis] 최종 위력 +1, 최대 체력 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD537].desc
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Status [MD538] — nazwa] 기본 위력 증폭
   źródło: Bufs_Mirror5.json :: dataList[id=MD538].name
   kontekst: identyfikator statusu w tekstach: `[MD538]`
   limit: do 40 znaków
   EN: Base Power Boost
   PL: Amplifikacja Mocy Bazowej
552. [Status [MD538] — opis] 기본 위력 +1, 최대 체력 +2.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD538].desc
   limit: do 120 znaków
   EN: Base Power +1, Max HP +2.5%
   PL: Moc Bazowa +1, Maks. HP +2.5%
553. [Status [MD541] — nazwa] 예리 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD541].name
   kontekst: identyfikator statusu w tekstach: `[MD541]`
   limit: do 40 znaków
   EN: Keen IV
   PL: Ostrość IV
554. [Status [MD541] — opis] 공격 레벨 +3, 최대 체력 +15%
   źródło: Bufs_Mirror5.json :: dataList[id=MD541].desc
   limit: do 120 znaków
   EN: Offense Level +3, Max HP +15%
   PL: Poziom Ataku +3, Maks. HP +15%
555. [Status [MD542] — nazwa] 육체 강화 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD542].name
   kontekst: identyfikator statusu w tekstach: `[MD542]`
   limit: do 40 znaków
   EN: Body Up II
   PL: Umocnienie Ciała II
556. [Status [MD542] — opis] 공격 레벨 +2, 방어 레벨 +3, 최대 체력 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD542].desc
   limit: do 120 znaków
   EN: Offense Level +2, Defense Level +3, Max HP +10%
   PL: Poziom Ataku +2, Poziom Obrony +3, Maks. HP +10%
557. [Status [MD543] — nazwa] 육체 강화 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD543].name
   kontekst: identyfikator statusu w tekstach: `[MD543]`
   limit: do 40 znaków
   EN: Body Up III
   PL: Umocnienie Ciała III
558. [Status [MD543] — opis] 공격 레벨 +3, 방어 레벨 +2, 최대 체력 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD543].desc
   (powtórzenie elementu 442 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Status [MD544] — nazwa] 성장 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD544].name
   kontekst: identyfikator statusu w tekstach: `[MD544]`
   limit: do 40 znaków
   EN: Growth IV
   PL: Rozwój IV
560. [Status [MD544] — opis] 최대 체력 +30%
   źródło: Bufs_Mirror5.json :: dataList[id=MD544].desc
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Status [MD545] — nazwa] 합 위력 증강
   źródło: Bufs_Mirror5.json :: dataList[id=MD545].name
   kontekst: identyfikator statusu w tekstach: `[MD545]`
   limit: do 40 znaków
   EN: Clash Power Spurt
   PL: Wzmocnienie Mocy Starcia
562. [Status [MD545] — opis] 합 위력 +1, 최대 체력 +15%
   źródło: Bufs_Mirror5.json :: dataList[id=MD545].desc
   limit: do 120 znaków
   EN: Clash Power +1, Max HP +15%
   PL: Moc Starcia +1, Maks. HP +15%
563. [Status [MD546] — nazwa] 최종 위력 증강
   źródło: Bufs_Mirror5.json :: dataList[id=MD546].name
   kontekst: identyfikator statusu w tekstach: `[MD546]`
   limit: do 40 znaków
   EN: Final Power Spurt
   PL: Wzmocnienie Mocy Końcowej
564. [Status [MD546] — opis] 최종 위력 +1, 최대 체력 +12.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD546].desc
   limit: do 120 znaków
   EN: Final Power +1, Max HP +12.5%
   PL: Moc Końcowa +1, Maks. HP +12.5%
565. [Status [MD547] — nazwa] 기본 위력 증강
   źródło: Bufs_Mirror5.json :: dataList[id=MD547].name
   kontekst: identyfikator statusu w tekstach: `[MD547]`
   limit: do 40 znaków
   EN: Base Power Spurt
   PL: Wzmocnienie Mocy Bazowej
566. [Status [MD547] — opis] 기본 위력 +1, 최대 체력 +10%
   źródło: Bufs_Mirror5.json :: dataList[id=MD547].desc
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Status [MD548] — nazwa] 파괴력
   źródło: Bufs_Mirror5.json :: dataList[id=MD548].name
   kontekst: identyfikator statusu w tekstach: `[MD548]`
   limit: do 40 znaków
   EN: Brutality
   PL: Siła Niszczenia
568. [Status [MD548] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1
   źródło: Bufs_Mirror5.json :: dataList[id=MD548].desc
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Status [MD549] — nazwa] 완강함 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD549].name
   kontekst: identyfikator statusu w tekstach: `[MD549]`
   limit: do 40 znaków
   EN: Headstrong II
   PL: Nieustępliwość II
570. [Status [MD549] — opis] 받는 피해량 -25%, 가하는 피해량 +25%
   źródło: Bufs_Mirror5.json :: dataList[id=MD549].desc
   (powtórzenie elementu 456 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Status [MD5Base] — nazwa] 추가되는 고난
   źródło: Bufs_Mirror5.json :: dataList[id=MD5Base].name
   kontekst: identyfikator statusu w tekstach: `[MD5Base]`
   limit: do 40 znaków
   EN: Mounting Trials
   PL: Narastające Utrapienie
572. [Status [MD551] — nazwa] 예리 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD551].name
   kontekst: identyfikator statusu w tekstach: `[MD551]`
   limit: do 40 znaków
   EN: Keen V
   PL: Ostrość V
573. [Status [MD551] — opis] 공격 레벨 +4, 최대 체력 +10%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD551].desc
   limit: do 120 znaków
   EN: Offense Level +4, Max HP +10%, Damage Dealt +5%
   PL: Poziom Ataku +4, Maks. HP +10%, Zadawane Obrażenia +5%
574. [Status [MD552] — nazwa] 육체 강화 IV
   źródło: Bufs_Mirror5.json :: dataList[id=MD552].name
   kontekst: identyfikator statusu w tekstach: `[MD552]`
   limit: do 40 znaków
   EN: Body Up IV
   PL: Umocnienie Ciała IV
575. [Status [MD552] — opis] 공격 레벨 +3, 방어 레벨 +3, 최대 체력 +7.5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD552].desc
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +3, Max HP +7.5%, Damage Dealt +5%
   PL: Poziom Ataku +3, Poziom Obrony +3, Maks. HP +7.5%, Zadawane Obrażenia +5%
576. [Status [MD553] — nazwa] 육체 강화 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD553].name
   kontekst: identyfikator statusu w tekstach: `[MD553]`
   limit: do 40 znaków
   EN: Body Up V
   PL: Umocnienie Ciała V
577. [Status [MD553] — opis] 공격 레벨 +4, 방어 레벨 +2, 최대 체력 +5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD553].desc
   limit: do 120 znaków
   EN: Offense Level +4, Defense Level +2, Max HP +5%, Damage Dealt +5%
   PL: Poziom Ataku +4, Poziom Obrony +2, Maks. HP +5%, Zadawane Obrażenia +5%
578. [Status [MD554] — nazwa] 성장 V
   źródło: Bufs_Mirror5.json :: dataList[id=MD554].name
   kontekst: identyfikator statusu w tekstach: `[MD554]`
   limit: do 40 znaków
   EN: Growth V
   PL: Rozwój V
579. [Status [MD554] — opis] 공격 레벨 +1, 최대 체력 +25%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD554].desc
   limit: do 120 znaków
   EN: Offense Level +1, Max HP +25%, Damage Dealt +5%
   PL: Poziom Ataku +1, Maks. HP +25%, Zadawane Obrażenia +5%
580. [Status [MD555] — nazwa] 합 위력 증강 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD555].name
   kontekst: identyfikator statusu w tekstach: `[MD555]`
   limit: do 40 znaków
   EN: Clash Power Up II
   PL: Wzmocnienie Mocy Starcia II
581. [Status [MD555] — opis] 합 위력 +1, 공격 레벨 +1, 최대 체력 +10%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD555].desc
   limit: do 120 znaków
   EN: Clash Power +1, Offense Level +1, Max HP +10%, Damage Dealt +5%
   PL: Moc Starcia +1, Poziom Ataku +1, Maks. HP +10%, Zadawane Obrażenia +5%
582. [Status [MD556] — nazwa] 최종 위력 증강 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD556].name
   kontekst: identyfikator statusu w tekstach: `[MD556]`
   limit: do 40 znaków
   EN: Final Power Up II
   PL: Wzmocnienie Mocy Końcowej II
583. [Status [MD556] — opis] 최종 위력 +1, 공격 레벨 +1, 최대 체력 +7.5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD556].desc
   limit: do 120 znaków
   EN: Final Power +1, Offense Level +1, Max HP +7.5%, Damage Dealt +5%
   PL: Moc Końcowa +1, Poziom Ataku +1, Maks. HP +7.5%, Zadawane Obrażenia +5%
584. [Status [MD557] — nazwa] 기본 위력 증강 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD557].name
   kontekst: identyfikator statusu w tekstach: `[MD557]`
   limit: do 40 znaków
   EN: Base Power Up II
   PL: Wzmocnienie Mocy Bazowej II
585. [Status [MD557] — opis] 기본 위력 +1, 공격 레벨 +1, 최대 체력 +5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD557].desc
   limit: do 120 znaków
   EN: Base Power +1, Offense Level +1, Max HP +5%, Damage Dealt +5%
   PL: Moc Bazowa +1, Poziom Ataku +1, Maks. HP +5%, Zadawane Obrażenia +5%
586. [Status [MD558] — nazwa] 파괴력 II
   źródło: Bufs_Mirror5.json :: dataList[id=MD558].name
   kontekst: identyfikator statusu w tekstach: `[MD558]`
   limit: do 40 znaków
   EN: Brutality II
   PL: Siła Niszczenia II
587. [Status [MD558] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD558].desc
   limit: do 120 znaków
   EN: Plus Coin Power +1, Minus Coin Power -1, Damage Dealt +5%
   PL: Moc Monet Plus +1, Moc Monet Minus -1, Zadawane Obrażenia +5%
588. [Status [MD561] — nazwa] 예리 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD561].name
   kontekst: identyfikator statusu w tekstach: `[MD561]`
   limit: do 40 znaków
   EN: Keen VI
   PL: Ostrość VI
589. [Status [MD561] — opis] 공격 레벨 +5, 최대 체력 +10%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD561].desc
   limit: do 120 znaków
   EN: Offense Level +5, Max HP +10%, Damage Dealt +5%
   PL: Poziom Ataku +5, Maks. HP +10%, Zadawane Obrażenia +5%
590. [Status [MD562] — nazwa] 강인함 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD562].name
   kontekst: identyfikator statusu w tekstach: `[MD562]`
   limit: do 40 znaków
   EN: Resilient VI
   PL: Twardość VI
591. [Status [MD562] — opis] 공격 레벨 +2, 방어 레벨 +6, 최대 체력 +10%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD562].desc
   limit: do 120 znaków
   EN: Offense Level +2, Defense Level +6, Max HP +10%, Damage Dealt +5%
   PL: Poziom Ataku +2, Poziom Obrony +6, Maks. HP +10%, Zadawane Obrażenia +5%
592. [Status [MD563] — nazwa] 육체 강화 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD563].name
   kontekst: identyfikator statusu w tekstach: `[MD563]`
   limit: do 40 znaków
   EN: Body Up VI
   PL: Umocnienie Ciała VI
593. [Status [MD563] — opis] 공격 레벨 +5, 방어 레벨 +2, 최대 체력 +5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD563].desc
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +2, Max HP +5%, Damage Dealt +5%
   PL: Poziom Ataku +5, Maks. HP +20%, Zadawane Obrażenia +7.5%
594. [Status [MD564] — nazwa] 성장 VI
   źródło: Bufs_Mirror5.json :: dataList[id=MD564].name
   kontekst: identyfikator statusu w tekstach: `[MD564]`
   limit: do 40 znaków
   EN: Growth VI
   PL: Rozwój VI
595. [Status [MD564] — opis] 공격 레벨 +2, 최대 체력 +25%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD564].desc
   limit: do 120 znaków
   EN: Offense Level +2, Max HP +25%, Damage Dealt +5%
   PL: Poziom Ataku +2, Poziom Obrony +6, Maks. HP +20%, Zadawane Obrażenia +7.5%
596. [Status [MD565] — nazwa] 합 위력 증강 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD565].name
   kontekst: identyfikator statusu w tekstach: `[MD565]`
   limit: do 40 znaków
   EN: Clash Power Up III
   PL: Wzmocnienie Mocy Starcia III
597. [Status [MD565] — opis] 합 위력 +1, 공격 레벨 +2, 최대 체력 +10%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD565].desc
   limit: do 120 znaków
   EN: Clash Power +1, Offense Level +2, Max HP +10%, Damage Dealt +5%
   PL: Moc Starcia +1, Poziom Ataku +2, Maks. HP +10%, Zadawane Obrażenia +5%
598. [Status [MD566] — nazwa] 최종 위력 증강 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD566].name
   kontekst: identyfikator statusu w tekstach: `[MD566]`
   limit: do 40 znaków
   EN: Final Power Up III
   PL: Wzmocnienie Mocy Końcowej III
599. [Status [MD566] — opis] 최종 위력 +1, 공격 레벨 +2, 최대 체력 +7.5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD566].desc
   limit: do 120 znaków
   EN: Final Power +1, Offense Level +2, Max HP +7.5%, Damage Dealt +5%
   PL: Moc Końcowa +1, Poziom Ataku +2, Maks. HP +7.5%, Zadawane Obrażenia +5%
600. [Status [MD567] — nazwa] 기본 위력 증강 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD567].name
   kontekst: identyfikator statusu w tekstach: `[MD567]`
   limit: do 40 znaków
   EN: Base Power Up III
   PL: Wzmocnienie Mocy Bazowej III
601. [Status [MD567] — opis] 기본 위력 +1, 공격 레벨 +2, 최대 체력 +5%, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD567].desc
   limit: do 120 znaków
   EN: Base Power +1, Offense Level +2, Max HP +5%, Damage Dealt +5%
   PL: Moc Bazowa +1, Poziom Ataku +2, Maks. HP +5%, Zadawane Obrażenia +5%
602. [Status [MD568] — nazwa] 파괴력 III
   źródło: Bufs_Mirror5.json :: dataList[id=MD568].name
   kontekst: identyfikator statusu w tekstach: `[MD568]`
   limit: do 40 znaków
   EN: Brutality III
   PL: Siła Niszczenia III
603. [Status [MD568] — opis] 더하기 코인 위력 +1, 빼기 코인 위력 -1, 가하는 피해량 +5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD568].desc
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Status [MD571] — nazwa] 예리 VII
   źródło: Bufs_Mirror5.json :: dataList[id=MD571].name
   kontekst: identyfikator statusu w tekstach: `[MD571]`
   limit: do 40 znaków
   EN: Keen VII
   PL: Ostrość VII
605. [Status [MD571] — opis] 공격 레벨 +5, 최대 체력 +20%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD571].desc
   limit: do 120 znaków
   EN: Offense Level +5, Max HP +20%, Damage Dealt +7.5%
   PL: Poziom Ataku +5, Maks. HP +20%, Zadawane Obrażenia +7.5%
606. [Status [MD572] — nazwa] 강인함 VII
   źródło: Bufs_Mirror5.json :: dataList[id=MD572].name
   kontekst: identyfikator statusu w tekstach: `[MD572]`
   limit: do 40 znaków
   EN: Resilient VII
   PL: Twardość VII
607. [Status [MD572] — opis] 공격 레벨 +2, 방어 레벨 +6, 최대 체력 +20%, 가하는 피해량 +7.5%
   źródło: Bufs_Mirror5.json :: dataList[id=MD572].desc
   limit: do 120 znaków
   EN: Offense Level +2, Defense Level +6, Max HP +20%, Damage Dealt +7.5%
   PL: Poziom Ataku +2, Poziom Obrony +6, Maks. HP +20%, Zadawane Obrażenia +7.5%
608. [Status [MD573] — nazwa] 육체 강화 VII
   źródło: Bufs_Mirror5.json :: dataList[id=MD573].name
   kontekst: identyfikator statusu w tekstach: `[MD573]`
   limit: do 40 znaków
   EN: Body Up VII
   PL: Umocnienie Ciała VII
