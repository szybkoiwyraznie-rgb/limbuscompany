# Paczka AI P17 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 3/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P17_2a_slowa_kluczowe_i_statusy_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P17_2a_slowa_kluczowe_i_statusy_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords-a1c9p3
- plik gry: `BattleKeywords-a1c9p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [MosesRedBreathCharge] — nazwa] 깊은 숨 - 붉은색
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathCharge].name
   kontekst: identyfikator tagu w tekstach: `[MosesRedBreathCharge]`
   limit: do 40 znaków
   EN: Deep Breath - Red
   PL: Głęboki Oddech - Czerwień
2. [Słowo kluczowe [MosesRedBreathCharge] — opis] - 최댓값: 3\n- <color=#ff6000><mark color=#ff000040><b><u>턴 종료시 최댓값이면, 강력한 스킬을 사용함</color></mark></b></u>\n- 특정 스킬 사용시 소모됨\n- 해당 버프가 있으면 패닉 상태가 되지 않음\n- 받는 피해 +(수치 x 20)%, 방어 레벨 수치만큼 감소\n- 턴 종료시 체력 피해 10, 정신력 피해 20 받음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathCharge].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Turn End: At Max Stack, use a powerful Skill</color></mark></b></u>\n- Consumed when using a certain Skill\n- Becomes immune to Panic under this effect\n- Take +(Stack x 20)% damage and lose Defense Level equal to Stack\n- Turn End: Take 10 HP damage and 20 SP damage
   PL: - Maks. stosów: 3\n- <color=#ff6000><mark color=#ff000040><b><u>Na koniec tury przy Maks. stosach używa potężnej Umiejętności</u></b></mark></color>\n- Zużywana przy użyciu określonych Umiejętności\n- Ten efekt chroni przed Paniką\n- Otrzymuje +(stosy x 20)% obrażeń i traci Poziom Obrony równy liczbie stosów\n- Na koniec tury otrzymuje 10 obrażeń HP i 20 obrażeń Poczytalności
3. [Słowo kluczowe [MosesRedBreathCharge] — tekst klimatyczny] 깊게 가라앉아, 호흡 하나마다 붉은색의 표상을 떠올리며 숨을 삼킨다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathCharge].flavor
   limit: do 120 znaków
   EN: Sink deeper and let the crimson images surface with every breath.
   PL: Pogrąża się głębiej, a z każdym oddechem połyka szkarłatne obrazy.
4. [Słowo kluczowe [MosesRedBreathAttack] — nazwa] 붉은 숨 - 내달리는 몸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathAttack].name
   kontekst: identyfikator tagu w tekstach: `[MosesRedBreathAttack]`
   limit: do 50 znaków
   EN: Red Breath - Push the Body's Limit
   PL: Czerwony Oddech - Granica Ciała
5. [Słowo kluczowe [MosesRedBreathAttack] — opis] - 공격 레벨 5 증가\n- 기본 스킬의 합 위력 +5
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathAttack].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 5 Offense Level\n- Base Skill Clash Power +5
   PL: - Zyskuje 5 Poziomu Ataku\n- Moc Starcia podstawowych Umiejętności +5
6. [Słowo kluczowe [MosesSin] — nazwa] 신(心) - 모제스
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesSin].name
   kontekst: identyfikator tagu w tekstach: `[MosesSin]`
   limit: do 40 znaków
   EN: Shin (心) - Moses
   PL: Shin (心) - Moses
7. [Słowo kluczowe [MosesSin] — opis] - 방어 레벨 +3, 수비 위력 +2\n- 스킬 효과로 자신의 정신력을 감소했으면, 다음 턴에 보호를 (정신력 감소량 / 5)만큼 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesSin].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3, Defense Power +2\n- If this unit lost SP due to its Skill's SP loss effects, gain Protection equal to (SP lost / 5) next turn
   PL: - Poziom Obrony +3, Moc Obrony +2\n- Jeżeli straciła Poczytalność przez efekty utraty Poczytalności swoich Umiejętności, w następnej turze zyskuje Ochronę równą (utracona Poczytalność / 5)
8. [Słowo kluczowe [MosesWarPTSD] — nazwa] 그 날의 기억
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesWarPTSD].name
   kontekst: identyfikator tagu w tekstach: `[MosesWarPTSD]`
   limit: do 40 znaków
   EN: Memories of that Day
   PL: Wspomnienia Tamtego Dnia
9. [Słowo kluczowe [MosesWarPTSD] — opis] - 기본 공격 레벨 -??\n- 기본 방어 레벨 -??\n- 턴 시작시 신속 5 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesWarPTSD].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Attack Level -??\n- Base Defense Level -??\n- Turn Start: Gain 5 Haste
   PL: - Podstawowy Poziom Ataku -??\n- Podstawowy Poziom Obrony -??\n- Na początku tury zyskuje 5 Pośpiechu
10. [Słowo kluczowe [MosesMiddle_LowMorale] — nazwa] 돌이킬 수 없이 망가진 몸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesMiddle_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[MosesMiddle_LowMorale]`
   limit: do 40 znaków
   EN: Body Broken Beyond Repair
   PL: Ciało Nieodwracalnie Złamane
11. [Słowo kluczowe [MosesMiddle_LowMorale] — opis] - 사기 저하\n- 턴 시작시 에즈라, 베스파에게 수비 위력 증가 +2 부여, 취약 1 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesMiddle_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile and apply +2 Defense Power Up to Ezra and Vespa
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości i nakłada +2 Wzrostu Mocy Obrony na Ezrę i Vespę
12. [Słowo kluczowe [MosesMiddle_Panic] — nazwa] 돌이킬 수 없이 망가진 몸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesMiddle_Panic].name
   kontekst: identyfikator tagu w tekstach: `[MosesMiddle_Panic]`
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Słowo kluczowe [MosesMiddle_Panic] — opis] - 패닉\n- 취약을 1 얻고, ‘숨 고르기’를 사용함
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesMiddle_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Fragile and use 'Steady the Breath'
   PL: - Panika\n- Zyskuje 1 Wrażliwości i używa „Wyrównania Oddechu”
14. [Słowo kluczowe [EzraMiddle_LowMorale] — nazwa] 자기 방어 - 가면
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EzraMiddle_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[EzraMiddle_LowMorale]`
   limit: do 40 znaków
   EN: Insecurity: Mask
   PL: Niepewność: Maska
15. [Słowo kluczowe [EzraMiddle_LowMorale] — opis] - 사기 저하\n- 공격 위력 감소 1 얻음\n- 방어 레벨 증가 2 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EzraMiddle_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Attack Power Down\n- Gain 2 Defense Level Up
   PL: - Niskie Morale\n- Zyskuje 1 Spadek Mocy Ataku\n- Zyskuje 2 Wzrostu Poziomu Obrony
16. [Słowo kluczowe [EzraMiddle_Panic] — nazwa] 자기 방어 - 가면
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EzraMiddle_Panic].name
   kontekst: identyfikator tagu w tekstach: `[EzraMiddle_Panic]`
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Słowo kluczowe [EzraMiddle_Panic] — opis] - 패닉\n- 공격 위력 감소 1 얻음\n- 방어 레벨 증가 3 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EzraMiddle_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Attack Power Down\n- Gain 3 Defense Level Up
   PL: - Panika\n- Zyskuje 1 Spadek Mocy Ataku\n- Zyskuje 3 Wzrostu Poziomu Obrony
18. [Słowo kluczowe [DimensionalBagEzraA] — nazwa] 차원가방 - 알라스 공방
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraA].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraA]`
   limit: do 50 znaków
   EN: Dimensional Bag - Allas Workshop
   PL: Worek Wymiarowy - Warsztat Allas
19. [Słowo kluczowe [DimensionalBagEzraA] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 알라스 공방 장갑\n- 다음 공방 무기: 네스터 공방 망치
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraA].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Allas Workshop Gloves\n- Next Workshop weapon: Nester Workshop Hammer
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Rękawice Warsztatu Allas\n- Następna broń warsztatowa: Młot Warsztatu Nester
20. [Słowo kluczowe [DimensionalBagEzraA] — tekst klimatyczny] “여기 제품들은 하나같이 가속력이 빵! 하고 터져 나와서 시원시원해!”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraA].flavor
   limit: do 140 znaków
   EN: "Everything from this Workshop kicks off the acceleration with a bang! It's super punchy and satisfying!"
   PL: „Każdy produkt stąd rozpędza się jak wybuch — bwam! I czujesz każde uderzenie!”
21. [Słowo kluczowe [DimensionalBagEzraB] — nazwa] 차원가방 - 네스터 공방
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraB].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraB]`
   limit: do 50 znaków
   EN: Dimensional Bag - Nester Workshop
   PL: Worek Wymiarowy - Warsztat Nester
22. [Słowo kluczowe [DimensionalBagEzraB] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 네스터 공방 망치\n- 다음 공방 무기: 스크류 아틀리에제 드릴 망치
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraB].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Nester Workshop Hammer\n- Next Workshop weapon: Screw Atelier Drill Hammer
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Młot Warsztatu Nester\n- Następna broń warsztatowa: Młot Wiertniczy Screw Atelier
23. [Słowo kluczowe [DimensionalBagEzraB] — tekst klimatyczny] “이게 참… 타격이 들어가는 절묘한 타이밍에 버튼을 눌러주면 진동과 함께 무기의 충격 면적이 극대화되는데, 적응만 잘하면 재밌어!”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraB].flavor
   limit: do 220 znaków
   EN: "Alright, so... Hit the button <i>right</i> as the strike lands, and bam! The vibration goes nuts and maximizes the area of the impact. It's a riot once you get the hang of it!"
   PL: „Słuchaj... Wciśniesz przycisk dokładnie w momencie uderzenia i bum! Wibracja szaleje, maksymalizując powierzchnię uderzenia. Gdy się przyzwyczaisz, to czysta frajda!”
24. [Słowo kluczowe [DimensionalBagEzraC] — nazwa] 차원가방 - 스크류 아틀리에
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraC].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraC]`
   limit: do 50 znaków
   EN: Dimensional Bag - Screw Atelier
   PL: Worek Wymiarowy - Screw Atelier
25. [Słowo kluczowe [DimensionalBagEzraC] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 스크류 아틀리에제 드릴 망치\n- 다음 공방 무기: 나미르 공방 건틀릿
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraC].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Screw Atelier Drill Hammer\n- Next Workshop weapon: Namir Workshop Gauntlets
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Młot Wiertniczy Screw Atelier\n- Następna broń warsztatowa: Gauntlety Warsztatu Namir
26. [Słowo kluczowe [DimensionalBagEzraC] — tekst klimatyczny] “여기 걸 다룰 땐 조심해야 해. 잘못했다간, 휘두른 사람이 감전될 수도 있어!”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraC].flavor
   limit: do 150 znaków
   EN: "Seriously, gotta be careful with this Workshop's babies. One bad slip and you'll end up zapping yourself instead!"
   PL: „Z tymi dziećmi Screw Atelier trzeba uważać. Jedna pomyłka i porażenie cię we własnym uzbrojeniu!”
27. [Słowo kluczowe [DimensionalBagEzraD] — nazwa] 차원가방 - 나미르 공방
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraD].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraD]`
   limit: do 50 znaków
   EN: Dimensional Bag - Namir Workshop
   PL: Worek Wymiarowy - Warsztat Namir
28. [Słowo kluczowe [DimensionalBagEzraD] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 나미르 공방 건틀릿\n- 다음 공방 무기: 알라스 공방 장갑
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraD].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Namir Workshop Gauntlets\n- Next Workshop weapon: Allas Workshop Gloves
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Gauntlety Warsztatu Namir\n- Następna broń warsztatowa: Rękawice Warsztatu Allas
29. [Słowo kluczowe [DimensionalBagEzraD] — tekst klimatyczny] “G사 특이점인 구가 들어간 제품인데, 잘 쓰려면 공중에서 스위치를 눌러 발동시킨 다음, 무게로 찍어 눌러야 해. 제대로 꽂히면 진짜 아파!”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraD].flavor
   limit: do 280 znaków
   EN: "Now this one's got G Corp.'s Singularity baked in—the Sphere! Here's how it works: You float up, pop the switch midair, and crush down with the weight of the gravity. Land a solid hit, and it's gonna be... brutal."
   PL: „Ten ma w sobie osobliwość Korporacji G — Kulę! Działa tak: wzlatujesz, wciskasz przełącznik w powietrzu i dociskasz ciężarem grawitacji. Jak trafi porządnie, to boli... brutalnie.”
30. [Słowo kluczowe [DimensionalBagEzraE] — nazwa] 차원가방 - 유리아 공방
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraE].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraE]`
   limit: do 50 znaków
   EN: Dimensional Bag - YuRia Atelier
   PL: Worek Wymiarowy - YuRia Atelier
31. [Słowo kluczowe [DimensionalBagEzraE] — opis] - 현재 공방 무기: 유리아 공방 특제 수제작 골든 리트리버 전용 도끼
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraE].desc
   limit: do 120 znaków
   EN: - Current Workshop Weapon: YuRia Atelier Special Handmade Golden Retriever-Exclusive Axe
   PL: - Obecna broń warsztatowa: Ręcznie robiona siekiera YuRia tylko dla Golden Retrievera
32. [Słowo kluczowe [DimensionalBagEzraE] — tekst klimatyczny] “유리아? 지금은 독립해서 공방을 운영하고 있어. 예전보다 더 잘나간다더라.”\n“인형에서 사람 몸으로 되돌렸던 그 사건이 진짜 대박이었는데.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DimensionalBagEzraE].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Oh, YuRia? Yeah, she's gone full solo now, and her Workshop—man, it's totally blowin' up."\n\n"Speaking of, I still remember her turning back from plush doll to human... Haha, that case sure was one hell of a bombshell."
   PL: „YuRia? Dziś działa solo i jej warsztat szaleje — mówią, że świetnie idzie.”\n„Ta sprawa, gdy wróciła z pluszowej lalki w człowieka? Prawdziwa bomba.”
33. [Słowo kluczowe [MiddleFingerEzraSin] — nazwa] 신(心) - 에즈라
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerEzraSin].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerEzraSin]`
   limit: do 40 znaków
   EN: Shin (心) - Ezra
   PL: Shin (心) - Ezra
34. [Słowo kluczowe [MiddleFingerEzraSin] — opis] - 기본 방어 레벨 +2\n- 기본 공격 위력 +1, 수비 위력 +2\n- 모제스의 깊은 숨 - 붉은색 1당 에즈라, 베스파가 사용하는 원호 방어로 에즈라가 받는 정신력 회복량 +4 (최대 12)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerEzraSin].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Defense Level +2\n- Base Attack Power +1, Defense Power +2\n For every 'Deep Breath - Red' Stack on Moses, Ezra and Vespa's Assist Defense heals 4 more SP for Ezra (max 12)
   PL: - Podstawowy Poziom Obrony +2\n- Podstawowa Moc Ataku +1, Moc Obrony +2\n- Za każdy stos Głębokiego Oddechu - Czerwieni Moses: Wsparcie Obrony używane przez Ezrę i Vespę odzyskuje dla Ezry +4 Poczytalności (maks. 12)
35. [Słowo kluczowe [VengeanceBookSpider] — nazwa] 앙갚음 장부
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VengeanceBookSpider].name
   kontekst: identyfikator tagu w tekstach: `[VengeanceBookSpider]`
   limit: do 40 znaków
   EN: The Book of Vengeance
   PL: Księga Zemsty
36. [Słowo kluczowe [VengeanceBookSpider] — opis] 중지 아비 - 마티아스나 중지 제자 - 키라가 이 효과를 보유한 대상에게 스킬 적중시 정신력 회복 7 (스킬당 1회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VengeanceBookSpider].desc
   limit: do 200 znaków
   EN: When The Middle Nursefather - Matthias or The Middle Apprentice - Kira uses a Skill to hit a target who has this effect, they heal 7 SP (once per Skill)
   PL: Gdy Ojciec Środkowego - Matthias albo Uczeń Środkowego - Kira trafi Umiejętnością cel z tym efektem, odzyskuje 7 Poczytalności (1 raz na Umiejętność)
37. [Słowo kluczowe [VengeanceBookSpider] — tekst klimatyczny] “네놈들… 즉결 처형이다.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VengeanceBookSpider].flavor
   limit: do 120 znaków
   EN: "Bastards... Prepare to face complete and total extermination."
   PL: „Wy... natychmiastowa egzekucja.”
38. [Słowo kluczowe [ResentmentSpider] — nazwa] 중지 - 원한
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ResentmentSpider].name
   kontekst: identyfikator tagu w tekstach: `[ResentmentSpider]`
   limit: do 40 znaków
   EN: The Middle - Grudge
   PL: Środkowy - Uraza
39. [Słowo kluczowe [ResentmentSpider] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ResentmentSpider].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced when using certain Skills\n- For every Stack, Offense Level +1, Defense Level -2, and Counter Skills deal +5% damage\n- At max Stack, take +20% damage
   PL: - Maks. stosów: 10\n- Maleje przy użyciu określonych Umiejętności\n- Za każdy stos Poziom Ataku +1, Poziom Obrony -2, Umiejętności Kontr zadają +5% obrażeń\n- Przy Maks. stosów otrzymuje +20% obrażeń
40. [Słowo kluczowe [ResentmentSpider] — tekst klimatyczny] 중지는 잊지 않아.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ResentmentSpider].flavor
   limit: do 120 znaków
   EN: The Middle never forgets.
   PL: Środkowy nie zapomina.
41. [Słowo kluczowe [ResentmentSpiderDaughter] — nazwa] 중지 - 원한
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ResentmentSpiderDaughter].name
   kontekst: identyfikator tagu w tekstach: `[ResentmentSpiderDaughter]`
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
42. [Słowo kluczowe [ResentmentSpiderDaughter] — opis] - 최댓값: 10\n- 특정 스킬 사용시 감소\n- 수치당 공격 레벨 +1, 방어 레벨 -2, 반격 스킬의 피해량 +5%\n- 최댓값일 시, 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ResentmentSpiderDaughter].desc
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Słowo kluczowe [GotACompliment] — nazwa] 칭찬 받았다!
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=GotACompliment].name
   kontekst: identyfikator tagu w tekstach: `[GotACompliment]`
   limit: do 40 znaków
   EN: I Got Praised!
   PL: Dostałem Pochwałę!
44. [Słowo kluczowe [GotACompliment] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치 2당 기본 위력 +1\n- 수치당 참격, 타격 스킬의 피해량 +8%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=GotACompliment].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced by 1 when this unit is hit by 2 Skills\n- Base Power +1 for every 2 Stack\n- Slash and Blunt Skills deal +8% damage for every Stack
   PL: - Maks. stosów: 10\n- Maleje o 1 przy trafieniu 2 Umiejętnościami\n- Moc Bazowa +1 za każde 2 stosy\n- Umiejętności Cięcia i Obuchu zadają +8% obrażeń za każdy stos
45. [Słowo kluczowe [DaughterEducationSpider] — nazwa] 잘 봐둬라 딸!
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DaughterEducationSpider].name
   kontekst: identyfikator tagu w tekstach: `[DaughterEducationSpider]`
   limit: do 40 znaków
   EN: Check This Out, Kiddo!
   PL: Patrz i Ucz się, Córeczko!
46. [Słowo kluczowe [DaughterEducationSpider] — opis] - 최댓값: 10\n- 스킬 2회 피격 시 1 감소\n- 수치 2당 기본 위력 +1\n- 수치당 참격, 타격 스킬의 피해량 +5%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DaughterEducationSpider].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Reduced by 1 when this unit is hit by 2 Skills\n- Base Power +1 for every 2 Stack\n- Slash and Blunt Skills deal +5% damage for every Stack
   PL: - Maks. stosów: 10\n- Maleje o 1 przy trafieniu 2 Umiejętnościami\n- Moc Bazowa +1 za każde 2 stosy\n- Umiejętności Cięcia i Obuchu zadają +5% obrażeń za każdy stos
47. [Słowo kluczowe [ReinforcedTattooSpider] — nazwa] 중지 - 원한 문신 [<s>큰 형님</s>]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].name
   kontekst: identyfikator tagu w tekstach: `[ReinforcedTattooSpider]`
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: The Middle - Vengeance Tattoo [<s>Great Brother</s>]
   PL: Środkowy - Tatuaż Zemsty [<s>Wielki Brat</s>]
48. [Słowo kluczowe [ReinforcedTattooSpider] — opis] - 최댓값: 2\n- 턴 종료시 소멸\n- 타격, 질투 속성의 피해량 +10%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Expires at Turn End\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 2\n- Znika na koniec tury\n- Zadaje +10% obrażeń Obuchu i Zawiści
49. [Słowo kluczowe [ReinforcedTattooSpider] — tekst klimatyczny] 누구보다 의리를 잘 지켜 큰 형님이 되었지만, 검 하나 때문에 의리를 저버린 놈.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ReinforcedTattooSpider].flavor
   limit: do 150 znaków
   EN: A Great Brother whose prestige was secured by his loyalty; a fool who has abandoned that very thing over a sword.
   PL: Z lojalności zrobił się Wielki Brat; tchórz z niego, gdy dla jednego miecza zdradził tę lojalność.
50. [Słowo kluczowe [ReinforcedTattooSpiderDaughter] — nazwa] 중지식 강화 문신
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ReinforcedTattooSpiderDaughter].name
   kontekst: identyfikator tagu w tekstach: `[ReinforcedTattooSpiderDaughter]`
   limit: do 60 znaków
   EN: The Middle Styled Augmentation Tattoos
   PL: Wzmocnione Tatuaże w Stylu Środkowego
51. [Słowo kluczowe [ReinforcedTattooSpiderDaughter] — opis] - 최댓값: 3\n- 턴 종료시 소멸\n- 타격, 질투 속성의 피해량 +10%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ReinforcedTattooSpiderDaughter].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Expires at Turn End\n- Deal +10% Blunt and Envy damage
   PL: - Maks. stosów: 3\n- Znika na koniec tury\n- Zadaje +10% obrażeń Obuchu i Zawiści
52. [Słowo kluczowe [HeatingWireOnSpider] — nazwa] 열선 ON
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOnSpider].name
   kontekst: identyfikator tagu w tekstach: `[HeatingWireOnSpider]`
   limit: do 40 znaków
   EN: Thermal Blades ON
   PL: Ostrza Termiczne - ON
53. [Słowo kluczowe [HeatingWireOnSpider] — opis] 열선 스킬의 코인 적중시 출혈 위력 및 횟수 부여량 만큼 화상 위력 및 횟수 추가 부여
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOnSpider].desc
   limit: do 170 znaków
   EN: On Hit with Thermal Blade Skill Coins: additionally inflict Burn Potency and Count equal to Bleed Potency and Count inflicted
   PL: Przy trafieniu Monet Umiejętności Rozgrzanych Ostrz nakłada dodatkowo Siłę i Licznik Podpalenia równe nakładanym Siłe i Licznikowi Krwawienia
54. [Słowo kluczowe [HeatingWireOnSpider] — tekst klimatyczny] 아빠 거만큼은 아니지만, 내 검으로도 녹이면서 벨 수 있어! 하지만 아빠 거처럼 계속 켜둘 순 없어…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOnSpider].flavor
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It's not as good as papa's, but I can also slice and sizzle at the same time!\nBut unlike papa's, I gotta let it cool from time to time...
   PL: To nie to co u taty, ale moje ostrze też potrafi ciąć i rozgrzewać! Tylko w przeciwieństwie do taty muszę czasem dać mu ostygnąć…
55. [Słowo kluczowe [HeatingWireOffSpider] — nazwa] 열선 OFF
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOffSpider].name
   kontekst: identyfikator tagu w tekstach: `[HeatingWireOffSpider]`
   limit: do 40 znaków
   EN: Thermal Blades OFF
   PL: Ostrza Termiczne - OFF
56. [Słowo kluczowe [HeatingWireOffSpider] — opis] 열선 스킬의 추가 효과가 발동되지 않음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOffSpider].desc
   limit: do 120 znaków
   EN: Additional effects of Thermal Blade Skills do not activate
   PL: Dodatkowe efekty Umiejętności Rozgrzanych Ostrz nie działają
57. [Słowo kluczowe [HeatingWireOffSpider] — tekst klimatyczny] 검의 열선이 꺼져있다
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeatingWireOffSpider].flavor
   limit: do 120 znaków
   EN: The sword's thermal wires are deactivated.
   PL: Ostrza miecza są wyłączone
58. [Słowo kluczowe [MiddleFatherGuts] — nazwa] 초근성
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherGuts].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFatherGuts]`
   limit: do 40 znaków
   EN: Ridiculous Grit
   PL: Niezwykła Wytrwałość
59. [Słowo kluczowe [MiddleFatherGuts] — opis] - 받는 피해를 1로 고정함 (키워드 피해 포함)\n- 합 승리시 (합 횟수 x 5)만큼 정신력 추가로 오름 (최대 15)\n- 턴 종료시 자신의 스킬 효과로 이번 턴 정신력이 감소했으면, 다음 턴에 피해량 증가 3 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherGuts].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Reduce all incoming damage to 1 (including Keyword damages)\n- On Clash Win, heal (Clash count x 5) more SP (max 15)\n- Turn End: If this unit lost SP this turn due to its Skill effects, gain 3 Damage Up next turn
   PL: - Otrzymywane obrażenia są blokowane na 1 (z obrażeniami słów kluczowych)\n- Po wygranym Starciu odzyskuje dodatkowo (liczba starć x 5) Poczytalności (maks. 15)\n- Na koniec tury, jeśli w tej turze stracił Poczytalność od Umiejętności, zyskuje w następnej turze 3 Wzrost Obrażeń
60. [Słowo kluczowe [MiddleFatherGuts] — tekst klimatyczny] “신(心)이니 뭐니 다 필요 없어. 이 악물고 지금까지 새겨 온 모든 문신의 힘을 끌어 올리면, 신(心) 같은 기술 없이도 난 충분히 강하다.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherGuts].flavor
   limit: do 250 znaków
   EN: "I don't need some stupid crutch like that "Shin (心)" crap. I just gotta pull as much power as I can from these tattoos and grit my teeth, and I'll overpower your fancy little tricks no problem."
   PL: „Nie potrzebuję żadnej pomocy typu Shin (心). Wystarczy, że zacisnę zęby i wyciągnę całą moc tych tatuaży — bez takich sztuczek i tak jestem wystarczająco silny.”
61. [Słowo kluczowe [MiddleFingerDaddy_LowMorale] — nazwa] 광분
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaddy_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerDaddy_LowMorale]`
   limit: do 40 znaków
   EN: Mad Rampage
   PL: Szał
62. [Słowo kluczowe [MiddleFingerDaddy_LowMorale] — opis] - 사기 저하\n턴 시작 시 공격 위력 증가 2, 방어 레벨 감소 4를 얻고,\n이전 턴에 받은 체력 피해량 30당 피해량 증가 1을 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaddy_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 2 Attack Power Up and 4 Defense Level Down; gain 1 Damage Up for every 30 HP damage taken last turn (max 5)
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Wzrostu Mocy Ataku i 4 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 30 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
63. [Słowo kluczowe [MiddleFingerDaddy_Panic] — nazwa] 광분
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaddy_Panic].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerDaddy_Panic]`
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Słowo kluczowe [MiddleFingerDaddy_Panic] — opis] - 패닉\n턴 시작 시 공격 위력 증가 3, 방어 레벨 감소 5를 얻고,\n이전 턴에 받은 체력 피해량 25당 피해량 증가 1을 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaddy_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 3 Attack Power Up and 5 Defense Level Down; gain 1 Damage Up for every 25 HP damage taken last turn (max 5)
   PL: - Panika\nNa początku tury zyskuje 3 Wzrostu Mocy Ataku i 5 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 25 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
65. [Słowo kluczowe [MiddleFingerDaughter_LowMorale] — nazwa] 흥분
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaughter_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerDaughter_LowMorale]`
   limit: do 40 znaków
   EN: Fervor
   PL: Podniecenie
66. [Słowo kluczowe [MiddleFingerDaughter_LowMorale] — opis] - 사기 저하\n턴 시작 시 방어 레벨 감소 2을 얻고,\n이전 턴에 받은 체력 피해량 30당 피해량 증가 1을 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaughter_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 2 Defense Level Down; gain 1 Damage Up for every 30 HP damage taken last turn (max 5)
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Spadek Poziomu Obrony,\ni 1 Wzrost Obrażeń za każde 30 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
67. [Słowo kluczowe [MiddleFingerDaughter_Panic] — nazwa] 흥분
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaughter_Panic].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerDaughter_Panic]`
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Słowo kluczowe [MiddleFingerDaughter_Panic] — opis] - 패닉\n턴 시작 시 공격 위력 증가 1,방어 레벨 감소 3를 얻고,\n이전 턴에 받은 체력 피해량 25당 피해량 증가 1을 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFingerDaughter_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 1 Attack Power Up and 3 Defense Level Down; gain 1 Damage Up for every 25 HP damage taken last turn (max 5)
   PL: - Panika\nNa początku tury zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony,\noraz 1 Wzrost Obrażeń za każde 25 otrzymanych w poprzedniej turze obrażeń HP (maks. 5)
69. [Słowo kluczowe [HumanBoneTheRings] — nazwa] 생체 재료(뼈)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HumanBoneTheRings].name
   kontekst: identyfikator tagu w tekstach: `[HumanBoneTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient (Bones)
   PL: Materiał Biologiczny (Kość)
70. [Słowo kluczowe [HumanBoneTheRings] — opis] - 최댓값: 206\n- 특수 충전 (위력 고정)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HumanBoneTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 206\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 206\n- Specjalny Ładunek (Siła zablokowana)
71. [Słowo kluczowe [HumanBloodTheRings] — nazwa] 생체 재료(피)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HumanBloodTheRings].name
   kontekst: identyfikator tagu w tekstach: `[HumanBloodTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient (Blood)
   PL: Materiał Biologiczny (Krew)
72. [Słowo kluczowe [HumanBloodTheRings] — opis] - 최댓값: 5\n- 특수 충전 (위력 고정)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HumanBloodTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 5\n- Specjalny Ładunek (Siła zblokowana)
73. [Słowo kluczowe [LivingSpecimenTheRings] — nazwa] 신체관극
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LivingSpecimenTheRings].name
   kontekst: identyfikator tagu w tekstach: `[LivingSpecimenTheRings]`
   limit: do 40 znaków
   EN: Corpus Theater
   PL: Teatr Ciała
74. [Słowo kluczowe [LivingSpecimenTheRings] — opis] - 버프, 체력, 정신력이 갱신되지 않는 행동 불가능 상태가 되고, 이 캐릭터와 연결된 신체관극이 생성됨
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LivingSpecimenTheRings].desc
   limit: do 170 znaków
   EN: - Enter an 'immobilized' state where this unit's buffs, HP, and SP cannot be changed. Forms a Corpus Theater connected to this unit
   PL: - Przechodzi w stan „Unieruchomienia”, w którym buffy, HP i Poczytalność nie mogą się zmieniać. Tworzy Teatr Ciała połączony z tą postacią
75. [Słowo kluczowe [MineTheRings] — nazwa] 작품명: 티비아
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MineTheRings].name
   kontekst: identyfikator tagu w tekstach: `[MineTheRings]`
   limit: do 40 znaków
   EN: Artwork: Tibia
   PL: Tytuł dzieła: Tibia
76. [Słowo kluczowe [MineTheRings] — opis] - 턴 시작 시, 위력 증가 4, 참격 위력 증가 2 얻음\n- 공격 스킬로 출혈 부여 시, 출혈 위력 2 추가 부여
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MineTheRings].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Power Up and 2 Slash Power Up\n- When inflicting Bleed with Attack Skills, inflict 2 more Bleed Potency
   PL: - Na początku tury zyskuje 4 Wzrost Mocy i 2 Wzrost Mocy Cięcia\n- Nakładając Krwawienie Umiejętnościami ataku, nakłada dodatkowo 2 Siły Krwawienia
77. [Słowo kluczowe [ObservationTheRings] — nazwa] 조망
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObservationTheRings].name
   kontekst: identyfikator tagu w tekstach: `[ObservationTheRings]`
   limit: do 40 znaków
   EN: Viewing the Tableau
   PL: Podziwianie Tableau
78. [Słowo kluczowe [ObservationTheRings] — opis] - 기본 공격 레벨 20 감소\n- 기본 방어 레벨 20 감소\n- 수감자 및 조력자의 퇴각 관련 기능이 작동하지 않음\n- 약지 제자가 전투 가능 상태면, 턴 시작 시 보호 7 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObservationTheRings].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -20\n- Base Defense Level -20\n- The Sinners & Assist Units' Retreat-related abilities do not activate\n- Turn Start: Gain 7 Protection if The Ring Apprentice has not retreated from this Encounter
   PL: - Podstawowy Poziom Ataku -20\n- Podstawowy Poziom Obrony -20\n- Funkcje wycofania Grzeszników i jednostek wsparcia nie działają\n- Jeżeli Uczeń Serdecznego jest gotów do walki, na początku tury zyskuje 7 Ochrony
79. [Słowo kluczowe [ObservationTheRings] — tekst klimatyczny] “갤러리에서 작품을 감상할 때는 느긋하고 여유롭게. 서두르지 않는 것이 중요하답니다.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObservationTheRings].flavor
   limit: do 180 znaków
   EN: "The appreciation of artwork in a gallery calls for unhurried contemplation. Please remember—impatience dulls the appreciation of art."
   PL: „Podziwianie dzieł w galerii wymaga spokoju i cierpliwości. Pośpiech przyćmiewa odbiór sztuki.”
80. [Słowo kluczowe [RedemptionTheRings] — nazwa] 재료가 떨어지는 상처
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RedemptionTheRings].name
   kontekst: identyfikator tagu w tekstach: `[RedemptionTheRings]`
   limit: do 40 znaków
   EN: Ingredient-shedding Wound
   PL: Rana Tracąca Materiał
81. [Słowo kluczowe [RedemptionTheRings] — opis] 스킬 사용 시, 공격 레벨 감소 2 얻음 (턴당 최대 3회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RedemptionTheRings].desc
   limit: do 120 znaków
   EN: Gain 2 Offense Level Down when using a Skill (max 3 times per turn)
   PL: Przy użyciu Umiejętności zyskuje 2 Spadek Poziomu Ataku (maks. 3 razy na turę)
82. [Słowo kluczowe [SpecimenTheRings] — nazwa] 전시회의 완성
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SpecimenTheRings].name
   kontekst: identyfikator tagu w tekstach: `[SpecimenTheRings]`
   limit: do 40 znaków
   EN: The Exhibition is Complete!
   PL: Wystawa Gotowa!
83. [Słowo kluczowe [SpecimenTheRings] — opis] 모든 수감자 및 조력자가 신체관극이 되면 전투에서 패배함
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SpecimenTheRings].desc
   limit: do 120 znaków
   EN: Lose the Encounter when all Sinners and Assist Units fall under the effect of Corpus Theater
   PL: Walka kończy się porażką, gdy wszyscy Grzesznicy i jednostki wsparcia przechodzą w Teatr Ciała
84. [Słowo kluczowe [SpecimenTheRings] — tekst klimatyczny] 모든 살과 근육이 있어야 할 그곳 그 제자리에.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SpecimenTheRings].flavor
   limit: do 130 znaków
   EN: That precise, delicate spot where all elements of flesh and muscles are arranged to perfection.
   PL: To precyzyjne, delikatne miejsce, gdzie każdy element mięśni i ciała zajmuje idealnie swoje miejsce.
85. [Słowo kluczowe [KAmpouleA1C94TH] — nazwa] 비상용 K사 앰플
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KAmpouleA1C94TH].name
   kontekst: identyfikator tagu w tekstach: `[KAmpouleA1C94TH]`
   limit: do 40 znaków
   EN: K Corp. Emergency Ampule
   PL: Ampułka Awaryjna Korporacji K
86. [Słowo kluczowe [KAmpouleA1C94TH] — opis] 자신을 제외한 아군이 생존했을 때, 자신의 체력이 0이 되는 피해를 받으면, 아래 효과 발동\n- 흐트러짐 상태면, 흐트러짐 상태 해제\n- 체력 전부 회복\n- 아군이 보유한 모든 비상용 K사 앰플 수치 1 감소\n- 이 효과는 인격/EGO 패시브로 체력이 1 미만으로 감소하지 않는 효과보다 우선적으로 발동함
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KAmpouleA1C94TH].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If at least one ally other than this unit is alive, activate the following effects upon taking damage that would reduce this unit's HP to 0:\n- If Staggered, recover from Stagger\n- Fully heal HP\n- All allies lose 1 K Corp. Emergency Ampule\n- This effect activates before the "X does not reduce HP below 1" effects from Identities & E.G.O Passives
   PL: Gdy co najmniej 1 sojusznik poza tą jednostką żyje, a otrzymane obrażenia obniżyłyby jej HP do 0, działają następujące efekty\n- Jeżeli jest oszołomiona, wychodzi z Oszołomienia\n- Pełne leczenie HP\n- Wszyscy sojusznicy tracą 1 Ampułki Awaryjnej Korporacji K\n- Ten efekt działa przed efektami „X nie obniża HP poniżej 1” z Tożsamości i pasywnych E.G.O
87. [Słowo kluczowe [LanternHohenheimBigBird] — nazwa] 램프
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LanternHohenheimBigBird].name
   kontekst: identyfikator tagu w tekstach: `[LanternHohenheimBigBird]`
   limit: do 40 znaków
   EN: Lamp
   PL: Lampa
88. [Słowo kluczowe [LanternHohenheimBigBird] — opis] - 최댓값: 20\n- 다음 턴에 수치 2당 속박 1 얻음 (최대 10)\n- 턴 종료 시 다음 턴에 (수치 / 자신의 슬롯 수)만큼 자신의 각 슬롯의 도발치 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LanternHohenheimBigBird].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Gain 1 Bind for every 2 Stack next turn (max 10)\n- Turn End: Gain +(Stack / # of this unit's Slot) Aggro to each of this unit's Skill Slot next turn
   PL: - Maks. stosów: 20\n- W następnej turze zyskuje 1 Spętanie za każde 2 stosy (maks. 10)\n- Na koniec tury prowokacja każdego slotu rośnie o (stosy / liczba slotów tej jednostki) w następnej turze
89. [Słowo kluczowe [DelusionHohenheimBigBird] — nazwa] 현혹
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DelusionHohenheimBigBird].name
   kontekst: identyfikator tagu w tekstach: `[DelusionHohenheimBigBird]`
   limit: do 40 znaków
   EN: Dazzle
   PL: Iluzja
90. [Słowo kluczowe [DelusionHohenheimBigBird] — opis] - 턴 시작 시 흐트러짐 상태가 아니면, 마지막 스킬 슬롯에 장착한 공격 스킬은 대상 변경 불가 스킬이 되고, 호엔하임을 우선 공격함\n- 효과가 발동된 턴 종료 시 효과 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DelusionHohenheimBigBird].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: If this unit is not Staggered, the Attack Skill equipped in this unit's last Skill Slot prioritizes Hohenheim and cannot be redirected\n- This effect expires at the end of the turn it is activated
   PL: - Na początku tury, jeżeli nie jest oszołomiona, Umiejętność ataku w ostatnim slocie celuje priorytetowo w Hohenheima i nie może zmienić celu\n- Efekt znika na koniec tury, w której zadziałał
91. [Słowo kluczowe [LvUpHohenheimBigBird] — nazwa] E.G.O 감응도 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird].name
   kontekst: identyfikator tagu w tekstach: `[LvUpHohenheimBigBird]`
   limit: do 40 znaków
   EN: E.G.O Attunement Boost
   PL: Wzrost Dostrojenia E.G.O
92. [Słowo kluczowe [LvUpHohenheimBigBird] — opis] - 기본 공격 레벨 15 증가\n- 기본 방어 레벨 15 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +15\n- Base Defense Level +15
   PL: - Podstawowy Poziom Ataku +15\n- Podstawowy Poziom Obrony +15
93. [Słowo kluczowe [LvUpHohenheimBigBird_Over] — nazwa] E.G.O 감응도 과잉
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].name
   kontekst: identyfikator tagu w tekstach: `[LvUpHohenheimBigBird_Over]`
   limit: do 40 znaków
   EN: E.G.O Attunement Overload
   PL: Przeciążenie Dostrojenia E.G.O
94. [Słowo kluczowe [LvUpHohenheimBigBird_Over] — opis] - 기본 공격 레벨 15 증가\n- 기본 방어 레벨 15 증가\n- 턴 종료 시 램프를 20이 되도록 얻고, 얻은 수치 1당 체력 2, 정신력 1 소모 (이 효과로 체력이 1 미만이 되지 않음)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +15\n- Base Defense Level +15\n- Turn End: Increase Lamp Stack to 20; lose 2 HP and 1 SP for every Stack gained (this effect does not reduce this unit's HP below 1)
   PL: - Podstawowy Poziom Ataku +15\n- Podstawowy Poziom Obrony +15\n- Na koniec tury podnosi Lampę do 20 stosów; traci 2 HP i 1 Poczytalności za każdy zdobyty stos (ten efekt nie obniża HP poniżej 1)
95. [Słowo kluczowe [LvUpHohenheimBigBird_Over] — tekst klimatyczny] 추출된 E.G.O의 힘을 무리하게 끌어내고 있다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpHohenheimBigBird_Over].flavor
   limit: do 120 znaków
   EN: Overdrawing the power of the Extracted E.G.O.
   PL: Bezwstydnie drenuje moc wyekstrahowanego E.G.O.
96. [Słowo kluczowe [HohenheimBigBird_LowMorale] — nazwa] 쏟아지는 잠
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HohenheimBigBird_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[HohenheimBigBird_LowMorale]`
   limit: do 40 znaków
   EN: Wave of Somnolence
   PL: Zalew Senności
97. [Słowo kluczowe [HohenheimBigBird_LowMorale] — opis] - 사기 저하\n- 스킬로 얻는 램프 획득량 1 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HohenheimBigBird_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 fewer Lamp from Skills
   PL: - Niskie Morale\n- Umiejętności zyskują o 1 mniej Lampy
98. [Słowo kluczowe [HohenheimBigBird_Panic] — nazwa] 쏟아지는 잠
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HohenheimBigBird_Panic].name
   kontekst: identyfikator tagu w tekstach: `[HohenheimBigBird_Panic]`
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Słowo kluczowe [HohenheimBigBird_Panic] — opis] - 패닉\n- 한 턴 동안 행동하지 않음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HohenheimBigBird_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Does not act for this turn
   PL: - Panika\n- Nie działa przez tę turę
100. [Słowo kluczowe [LvUpFireFly] — nazwa] E.G.O 감응도 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpFireFly].name
   kontekst: identyfikator tagu w tekstach: `[LvUpFireFly]`
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Słowo kluczowe [LvUpFireFly] — opis] - 기본 공격 레벨 10 증가\n- 기본 방어 레벨 10 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpFireFly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +10\n- Base Defense Level +10
   PL: - Podstawowy Poziom Ataku +10\n- Podstawowy Poziom Obrony +10
102. [Słowo kluczowe [LvUpFireFly_Over] — nazwa] E.G.O 감응도 과잉
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpFireFly_Over].name
   kontekst: identyfikator tagu w tekstach: `[LvUpFireFly_Over]`
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Słowo kluczowe [LvUpFireFly_Over] — opis] - 기본 공격 레벨 10 증가\n- 기본 방어 레벨 10 증가\n- 턴 종료 시, 화상 4 얻음. 정신력 5 소모
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpFireFly_Over].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +10\n- Base Defense Level +10\n- Turn End: Gain 4 Burn and lose 5 SP
   PL: - Podstawowy Poziom Ataku +10\n- Podstawowy Poziom Obrony +10\n- Koniec tury: zyskuje 4 Podpalenia i traci 5 Poczytalności
104. [Słowo kluczowe [LvUpFireFly_Over] — tekst klimatyczny] 추출된 E.G.O의 힘을 무리하게 끌어내고 있다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvUpFireFly_Over].flavor
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [Słowo kluczowe [LCEFireFly_LowMorale] — nazwa] 열화침식
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LCEFireFly_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LCEFireFly_LowMorale]`
   limit: do 40 znaków
   EN: Degraded Corrosion
   PL: Zdegradowana Korozja
106. [Słowo kluczowe [LCEFireFly_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 취약 1 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LCEFireFly_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości
107. [Słowo kluczowe [LCEFireFly_Panic] — nazwa] 열화침식
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LCEFireFly_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LCEFireFly_Panic]`
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Słowo kluczowe [LCEFireFly_Panic] — opis] - 패닉\n- 턴 시작 시 취약 1, 화상 5 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LCEFireFly_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 1 Fragile and 5 Burn
   PL: - Panika\n- Na początku tury zyskuje 1 Wrażliwości i 5 Podpalenia
109. [Słowo kluczowe [Cubism_LowMorale] — nazwa] 한물간 예술
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Cubism_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Cubism_LowMorale]`
   limit: do 40 znaków
   EN: Outmoded Art
   PL: Przestarzała Sztuka
110. [Słowo kluczowe [Cubism_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 1 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Cubism_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku
111. [Słowo kluczowe [Cubism_Panic] — nazwa] 한물간 예술
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Cubism_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Cubism_Panic]`
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Słowo kluczowe [Cubism_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 증가 2 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Cubism_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Offense Level Up
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku
113. [Słowo kluczowe [FutureEyeOn] — nazwa] 예지안
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=FutureEyeOn].name
   kontekst: identyfikator tagu w tekstach: `[FutureEyeOn]`
   limit: do 40 znaków
   EN: Eye of Precognition
   PL: Oko Prekognicji
114. [Słowo kluczowe [FutureEyeOn] — opis] - 최댓값: 30\n- 합 위력 +2\n- 턴 시작 시 10 증가\n- 턴 시작 시 (수치/4)만큼 정신력 회복
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=FutureEyeOn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Clash Power +2\n- Turn Start: Gain 10 Stack\n- Turn Start: Heal (Stack / 4) SP
   PL: - Maks. stosów: 30\n- Moc Starcia +2\n- Na początku tury rośnie o 10\n- Na początku tury odzyskuje (stosy / 4) Poczytalności
115. [Słowo kluczowe [FutureEyeOn] — tekst klimatyczny] ‘마법처럼 미래를 보여 주는 건 아니다. 이 눈은 시야에 들어온 모든 것을 분석해 앞으로 다가올 찰나의 순간을 예측해 주는 계산기에 가깝다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=FutureEyeOn].flavor
   limit: do 290 znaków
   EN: "The eye does not possess some supernatural power that shows its user the destined future. It is more akin to a computing device that analyzes everything it sees and provides the most likely scenario in the upcoming instant."
   PL: „To oko nie ma magicznej mocy pokazywania przeznaczonej przyszłości. To raczej maszyna licząca, która analizuje wszystko w polu widzenia i podaje najbardziej prawdopodobny scenariusz najbliższej chwili.”
116. [Słowo kluczowe [FutureEyeOff] — nazwa] 예지안 과열
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=FutureEyeOff].name
   kontekst: identyfikator tagu w tekstach: `[FutureEyeOff]`
   limit: do 50 znaków
   EN: Eye of Precognition - Overheat
   PL: Oko Prekognicji - Przegrzanie
117. [Słowo kluczowe [FutureEyeOff] — opis] - 최댓값: 30\n- 공격 스킬로 가하는 피해량 -20%\n- 가속탄을 소모하는 스킬의 모든 코인이 파괴 불가 코인으로 변경됨\n- 턴 시작 시 10 증가\n- 수치가 30이면, ‘예지안’으로 변환
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=FutureEyeOff].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Attack Skills deal -20% damage\n- Convert all Coins on Skills that spend Acceleration Round to Unbreakable Coins\n- Turn Start: Gain 10 Stack\n- At 30 Stack, convert into "Eye of Precognition"
   PL: - Maks. stosów: 30\n- Umiejętności ataku zadają -20% obrażeń\n- Wszystkie Monety Umiejętności zużywających Pocisk Przyspieszenia stają się Niezniszczalnymi Monetami\n- Na początku tury rośnie o 10\n- Przy 30 stosach zamienia się w „Oko Prekognicji”
118. [Słowo kluczowe [LookingFuture] — nazwa] 가속하는 미래
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LookingFuture].name
   kontekst: identyfikator tagu w tekstach: `[LookingFuture]`
   limit: do 40 znaków
   EN: Accelerating Future
   PL: Przyspieszająca Przyszłość
119. [Słowo kluczowe [LookingFuture] — opis] - 최댓값: 10\n- 수치 1당, 합 위력 +1\n- 수치 5당, 코인 위력 +1\n- 스킬 종료 시 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LookingFuture].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Clash Power +1 for every Stack\n- Coin Power +1 for every 5 Stack\n- Expires at Skill End
   PL: - Maks. stosów: 10\n- Moc Starcia +1 za każdy stos\n- Moc Monety +1 za każde 5 stosów\n- Znika na koniec Umiejętności
120. [Słowo kluczowe [LookingFuture] — tekst klimatyczny] 합을 더 오래, 더 많이 맞댈수록 팔레르모는 가속한다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LookingFuture].flavor
   limit: do 120 znaków
   EN: The Palermitan Style is known to accelerate the longer a duel lasts.
   PL: Im dłużej i częściej toczy się Starcie, tym bardziej przyspiesza styl palermitański.
121. [Słowo kluczowe [ObsessionAndGreed] — nazwa] 신(心) - 발렌치나
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessionAndGreed].name
   kontekst: identyfikator tagu w tekstach: `[ObsessionAndGreed]`
   limit: do 40 znaków
   EN: Shin (心) - Valencina
   PL: Shin (心) - Valencina
122. [Słowo kluczowe [ObsessionAndGreed] — opis] - 이전 턴에 합 패배한 횟수만큼 방어 레벨 +3 (최대 6)\n자신의 호흡 위력 1당, 가하는 피해량 +3% (최대 15%)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessionAndGreed].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3 for every instance of Clash Lose in the last turn (max 6)\n- Deal +3% damage for every Poise Potency on self (max 15%)
   PL: - Poziom Obrony +3 za każdą przegraną w Starciu w poprzedniej turze (maks. 6)\nZadaje +3% obrażeń za każdą Siłę Oddechu (maks. 15%)
123. [Słowo kluczowe [AccelBullet] — nazwa] 가속탄
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AccelBullet].name
   kontekst: identyfikator tagu w tekstach: `[AccelBullet]`
   limit: do 40 znaków
   EN: Acceleration Round
   PL: Pocisk Przyspieszenia
124. [Słowo kluczowe [AccelBullet] — opis] - 최댓값: 10\n- 특수 탄환\n- 특정 스킬 사용 시 소모
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AccelBullet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Capacity: 10\n- Unique Ammo\n- Spent by certain Skills
   PL: - Maks. pojemności: 10\n- Specjalna amunicja\n- Zużywany przy użyciu określonych Umiejętności
125. [Słowo kluczowe [TeachersPrey] — nazwa] 사냥 표적
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TeachersPrey].name
   kontekst: identyfikator tagu w tekstach: `[TeachersPrey]`
   limit: do 40 znaków
   EN: Game Target
   PL: Cel Polowania
126. [Słowo kluczowe [TeachersPrey] — opis] 속도가 1로 고정되며, ‘엄지 아비 - 발렌치나’ 모든 공격 스킬의 타겟으로 지정됨
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TeachersPrey].desc
   limit: do 140 znaków
   EN: Fix this unit's Speed to 1; all Attack Skills of "The Thumb Nursefather - Valencina" targets this unit
   PL: Szybkość zostaje zablokowana na 1; wszystkie Umiejętności ataku „Ojca Kciuka - Valenciny” celują w tę jednostkę
127. [Słowo kluczowe [TeachersPrey] — tekst klimatyczny] 보냐텔리 가의 표적이 되었다면 사냥은 피할 수 없다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TeachersPrey].flavor
   limit: do 120 znaków
   EN: Prey marked by Famiglia Bognatelli will be hunted down without fail.
   PL: Jeżeli zostało się zwierzyną rodziny Bognatelli, polowania nie da się uniknąć.
128. [Słowo kluczowe [AaCfPcBiv2] — nazwa] 고열기전
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AaCfPcBiv2].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBiv2]`
   limit: do 40 znaków
   EN: Superthermogenesis
   PL: Nadtermogeneza
129. [Słowo kluczowe [AaCfPcBiv2] — opis] 턴 종료 시 수치에 비례하여 최대 체력의 (수치*0.5)%만큼 고정 피해를 받고 효과 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AaCfPcBiv2].desc
   limit: do 120 znaków
   EN: Turn End: Take fixed damage equal to (Stack x 0.5)% of Max HP, then the effect expires
   PL: Na koniec tury otrzymuje obrażenia stałe równe (stosy x 0,5)% Maks. HP, po czym efekt znika
130. [Słowo kluczowe [VergiliusSin] — nazwa] 신(心) - 붉은시선
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VergiliusSin].name
   kontekst: identyfikator tagu w tekstach: `[VergiliusSin]`
   limit: do 40 znaków
   EN: Shin (心) - The Red Gaze
   PL: Shin (心) - Czerwone Spojrzenie
131. [Słowo kluczowe [VergiliusSin] — opis] 분노 속성의 가하는 피해량 +50%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VergiliusSin].desc
   limit: do 120 znaków
   EN: Deal +50% Wrath damage
   PL: Zadaje +50% obrażeń Gniewu
132. [Słowo kluczowe [VergiliusSin] — podsumowanie] 피해량 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=VergiliusSin].summary
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
133. [Słowo kluczowe [BloodBranch] — nazwa] 망혈[盲血]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BloodBranch].name
   kontekst: identyfikator tagu w tekstach: `[BloodBranch]`
   limit: do 40 znaków
   EN: Blinding Blood [盲血]
   PL: Zaślepiająca Krew [盲血]
134. [Słowo kluczowe [BloodBranch] — opis] 수치 1당, 다음 턴에 속박 1 얻음\n턴 종료 시 자신의 (출혈 위력 x 수치) 만큼 체력 피해를 입음\n전투 시작 시 수치 1당, 출혈 3 얻고 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BloodBranch].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 1 Bind next turn for every Stack\nTurn End: Take (Bleed Potency x Stack) HP damage\nCombat Start: Gain 3 Bleed for every Stack, then expire
   PL: Zyskuje 1 Spętanie w następnej turze za każdy stos\nNa koniec tury otrzymuje (Siła Krwawienia x stosy) obrażeń HP\nNa początku walki zyskuje 3 Krwawienia za każdy stos, po czym znika
135. [Słowo kluczowe [BloodBranch] — tekst klimatyczny] “피를 시선에 담아낼 수만 있다면, 모으고 응축해서 꿰뚫을 수 있어. 물론 눈을 멀게도 할 수 있을 거야.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BloodBranch].flavor
   limit: do 190 znaków
   EN: "If blood can be contained within a gaze, it can also be accumulated and condensed for piercing. It can also, of course, be used to blind. Okay?"
   PL: „Jeżeli krew da się uwięzić w spojrzeniu, można ją też zgromadzić, skondensować i przebić nią wszystko. A nawet oślepić. Dobrze?”
136. [Słowo kluczowe [Gebura_Reinforcement] — nazwa] 게부라의 칼날
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Gebura_Reinforcement].name
   kontekst: identyfikator tagu w tekstach: `[Gebura_Reinforcement]`
   limit: do 40 znaków
   EN: Gebura's Blade
   PL: Ostrze Gebury
137. [Słowo kluczowe [Gebura_Reinforcement] — opis] - 모든 스킬 코인이 파괴 불가 코인으로 변경됨\n- 피해량 +100%\n- 더하기 코인 스킬인 경우, 코인 위력 +1, 빼기 코인 스킬인 경우, 최종 위력 +1\n- 이번 턴에 모든 피해로 흐트러짐 상태가 되지 않음\n- 자신의 체력이 10 이하면, 10으로 회복함\n- 이번 턴 동안 피해로 인해 체력이 10 미만으로 감소하지 않음\n- 이번 턴동안 기본 공격 스킬과 반격 스킬의 코인 적중시 피해량의 10%만큼 체력 회복 (스킬당 최대 회복량 : 100) \n- 턴 종료시 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Gebura_Reinforcement].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Convert all Skill Coins into Unbreakable Coins\n- Deal +100% damage\n- Plus Coin Skills gain Coin Power +1; Minus Coin Skills gain Final Power +1\n- For this turn, this unit cannot be Staggered from all sources of damage\n- At less than 10 HP, heal to 10 HP\n- For this turn, this unit's HP does not drop below 10\n- For this turn, every Coin Hit from Base Attack Skills and Counter Skills heals 10% of the damage dealt (max healing from each Skill: 100)\n- Expires at Turn End
   PL: - Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Zadaje +100% obrażeń\n- Umiejętności z Monetami Plus zyskują Moc Monety +1; Umiejętności z Monetami Minus zyskują Moc Końcowa +1\n- W tej turze nie przechodzi w Oszołomienie od żadnych obrażeń\n- Przy HP poniżej 10 leczy do 10 HP\n- W tej turze HP nie spada poniżej 10\n- W tej turze każde trafienie Monetą podstawowej Umiejętności ataku i Kontrą leczy 10% zadanych obrażeń (maks. leczenia na Umiejętność: 100)\n- Znika na koniec tury
138. [Słowo kluczowe [Gebura_Reinforcement] — podsumowanie] 게부라의 칼날 효과 적용
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Gebura_Reinforcement].summary
   limit: do 120 znaków
   EN: Gebura's Blade activated
   PL: Aktywne efekty Ostrza Gebury
139. [Słowo kluczowe [ThreeMirrorpartYiSang] — nazwa] 깨어진 세계
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ThreeMirrorpartYiSang].name
   kontekst: identyfikator tagu w tekstach: `[ThreeMirrorpartYiSang]`
   limit: do 40 znaków
   EN: Shattered World
   PL: Rozbity Świat
140. [Słowo kluczowe [ThreeMirrorpartYiSang] — opis] - 최댓값: 1\n- 턴 종료시 소멸\n- 화상으로 받는 피해 1.2배 (소수점 버림, 특수 화상 제외)\n- 이상의 분노 속성과 우울 속성 기본 공격 스킬로 받는 피해량 +10%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ThreeMirrorpartYiSang].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Expires at Turn End\n- Take x1.2 damage from Burn (rounded down; except Unique Burn)\n- Take +10% damage from Yi Sang's Wrath and Gloom Base Attack Skills
   PL: - Maks. stosów: 1\n- Znika na koniec tury\n- Otrzymuje x1,2 obrażeń od Podpalenia (zaokrąglone w dół; poza Specjalnym Podpaleniem)\n- Otrzymuje +10% obrażeń od podstawowych ataków Yisanga z Gniewu i Posępności
141. [Słowo kluczowe [RyoshuEGOPF] — nazwa] 나생[羅生]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuEGOPF].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuEGOPF]`
   limit: do 40 znaków
   EN: Entangled Life [羅生]
   PL: Splecione Życie [羅生]
142. [Słowo kluczowe [RyoshuEGOPF] — opis] 최댓값 : 999\n- 료슈가 가한 스킬 피해 1당 수치 1 증가\n- 수치 33당 기본 스킬 피해량 1% 증가 (최대 10%)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuEGOPF].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 999\n- Gain 1 Stack for every HP damage dealt by Ryōshū's Skills\n- Deal +1% damage with Base Skills for every 33 Stack (max 10%)
   PL: Maks. stosów: 999\n- Zyskuje 1 stos za każde 1 obrażeń HP zadanych Umiejętnościami Ryōshū\n- Podstawowe Umiejętności zadają +1% obrażeń za każde 33 stosy (maks. 10%)
143. [Słowo kluczowe [RyoshuEGOPF] — tekst klimatyczny] ‘꼬일 대로 꼬이고 꼬여, 엮여 만들어진 번데기. 실.삶.세상.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuEGOPF].flavor
   limit: do 120 znaków
   EN: 'Twisted and entangled beyond measure, bound and woven into a cocoon. Thread. Life. World.'
   PL: „Zwinięta i spleciona ponad miarę, uwiązana i utkana w kokon. Nić. Życie. Świat.”
144. [Słowo kluczowe [OffenseBug] — nazwa] 공격 해충[바퀴]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=OffenseBug].name
   kontekst: identyfikator tagu w tekstach: `[OffenseBug]`
   limit: do 40 znaków
   EN: Hurting Pest [Roaches]
   PL: Szkodnik Ataku [Karaluchy]
145. [Słowo kluczowe [OffenseBug] — opis] - 최댓값: 50\n- 최대 체력이 수치당 1%씩 감소\n- 전투 시작 시 (수치x12)만큼 고정 피해를 입음\n- 수치가 감소 될 시, 감소된 수치만큼 무작위 E.G.O 자원을 얻음 (최대 15)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=OffenseBug].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Lose 1% max HP per Stack\n- Combat Start: Take (Stack x 12) fixed damage\n- Whenever this unit loses Stack of this effect, gain E.G.O resources of random Affinities equal to Stack lost (max 15)
   PL: - Maks. stosów: 50\n- Maks. HP maleje o 1% za każdy stos\n- Na początku walki otrzymuje (stosy x 12) obrażeń stałych\n- Przy utracie stosów zyskuje losowe Zasoby E.G.O w liczbie utraconych stosów (maks. 15)
146. [Słowo kluczowe [OffenseBug] — tekst klimatyczny] ‘해충이라 불리는 것 중에서 이것이 제일이다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=OffenseBug].flavor
   limit: do 120 znaków
   EN: "This creature is unmatched among those scorned as pests."
   PL: „Wśród istot zwanych szkodnikami ten jest niepokonany.”
147. [Słowo kluczowe [DefenseBug] — nazwa] 방어 해충[바퀴]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DefenseBug].name
   kontekst: identyfikator tagu w tekstach: `[DefenseBug]`
   limit: do 40 znaków
   EN: Protecting Pest [Roaches]
   PL: Szkodnik Obrony [Karaluchy]
148. [Słowo kluczowe [DefenseBug] — opis] - 최댓값: 50\n- 자신에게 (화상, 출혈, 진동, 파열, 침잠)의 위력 또는 횟수가 부여될 시, 부여될 효과의 수치만큼 감소하고, 해당 효과를 부여받지 않음\n- 턴 종료시 소멸
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DefenseBug].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Whenever this unit is inflicted with (Burn, Bleed, Tremor, Rupture, Sinking) Potency or Count, instead of gaining those effects, lose the same amount of Stack of this effect instead\n- Expires at Turn End
   PL: - Maks. stosów: 50\n- Gdy zostają nałożone Siła lub Licznik (Podpalenia, Krwawienia, Wstrząsu, Rozdarcia, Zatonięcia), zamiast zdobywania efektu traci równą liczbę stosów tego efektu\n- Znika na koniec tury
149. [Słowo kluczowe [DefenseBug] — tekst klimatyczny] ‘하나하나가 해롭고 징그럽고 질기다’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=DefenseBug].flavor
   limit: do 120 znaków
   EN: "They are baleful and stubborn, not to mention tenacious."
   PL: „Każdy jest zdradliwy, ohydny i uporczywy.”
150. [Słowo kluczowe [LvDownLittleFingerBossTwo] — nazwa] 천살성상[天殺星傷]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].name
   kontekst: identyfikator tagu w tekstach: `[LvDownLittleFingerBossTwo]`
   limit: do 50 znaków
   EN: Tiansha Star's Bladewound [天殺星傷]
   PL: Rana Ostrza Gwiazdy Tiansha [天殺星傷]
151. [Słowo kluczowe [LvDownLittleFingerBossTwo] — opis] - 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -15\n- Base Defense Level -15
   PL: - Podstawowy Poziom Ataku -15\n- Podstawowy Poziom Obrony -15
152. [Słowo kluczowe [LvDownLittleFingerBossTwo] — podsumowanie] 기본 공격, 방어 레벨 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].summary
   limit: do 120 znaków
   EN: - Lose Base Offense and Base Defense Level
   PL: - Traci Podstawowy Poziom Ataku i Podstawowy Poziom Obrony
153. [Słowo kluczowe [LvDownLittleFingerBossTwo] — tekst klimatyczny] 천살성도 - 아라야시키로 벤 것에는 타오르는 듯한 검흔이 남는다. 이 검흔은 어떤 방법으로도 사라지지 않는다.\n휘두른 자의 존재를 대가로 상대의 존재도 베어낸 것이기에.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LvDownLittleFingerBossTwo].flavor
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A cut from the Tiansha Star's Blade - Arayashiki leaves a blade wound that seems to burn with implacable fire.\nThis burning mark can never fade, for the wielder has slashed through the existence of their opponent at the cost of their own.
   PL: Cięcie Ostrzem Gwiazdy Tiansha - Arayashiki zostawia ranę płonącą jak nieugaszony żar.\nTen znak nigdy nie zblednie, bo zadający poświęcił własną egzystencję, by przeciąć egzystencję przeciwnika.
154. [Słowo kluczowe [SojiAbiAgePast] — nazwa] 역행 - 미움
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgePast].name
   kontekst: identyfikator tagu w tekstach: `[SojiAbiAgePast]`
   limit: do 40 znaków
   EN: Backward Flow - Bitterness
   PL: Prąd Wstecz - Gorycz
155. [Słowo kluczowe [SojiAbiAgePast] — opis] - 최댓값 : 20\n- 수치당 가하는 피해량, 받는 피해량 +2%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgePast].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal and take +2% damage for every Stack
   PL: - Maks. stosów: 20\n- Zadaje i otrzymuje +2% obrażeń za każdy stos
156. [Słowo kluczowe [SojiAbiAgePast] — podsumowanie] 가하는 피해량, 받는 피해량 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgePast].summary
   limit: do 120 znaków
   EN: Deal and take more damage
   PL: Zadaje i otrzymuje więcej obrażeń
157. [Słowo kluczowe [SojiAbiAgePast] — tekst klimatyczny] ‘나를 잊어 버리고 간 기억이 매듭처럼 끊어지지가 않아.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgePast].flavor
   limit: do 160 znaków
   EN: 'The memory of being forgotten and abandoned by you refuses to let go... like a stubborn knot of thread that clings.'
   PL: „Wspomnienie, w którym odszedłeś i zapomniałeś o mnie, tkwi jak węzeł, którego nie da się przeciąć.”
158. [Słowo kluczowe [SojiAbiAgeFuture] — nazwa] 순행 - 연민
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].name
   kontekst: identyfikator tagu w tekstach: `[SojiAbiAgeFuture]`
   limit: do 40 znaków
   EN: Forward Flow - Compassion
   PL: Prąd Naprzód - Współczucie
159. [Słowo kluczowe [SojiAbiAgeFuture] — opis] - 최댓값 : 20\n- 수치당 가하는 피해량, 받는 피해량 -2%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal and take -2% damage for every Stack
   PL: - Maks. stosów: 20\n- Zadaje i otrzymuje -2% obrażeń za każdy stos
160. [Słowo kluczowe [SojiAbiAgeFuture] — podsumowanie] 가하는 피해량, 받는 피해량 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].summary
   limit: do 120 znaków
   EN: Deal and take less damage
   PL: Zadaje i otrzymuje mniej obrażeń
161. [Słowo kluczowe [SojiAbiAgeFuture] — tekst klimatyczny] ‘당신을 이해하고 안아줄 수 있을지도 모르겠다는 생각을 하게 된 건, 시간이 지나 나이가 들었기 때문일까.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiAgeFuture].flavor
   limit: do 170 znaków
   EN: 'Perhaps it was the passage of time and the years weighing on me that led me to believe I could finally understand and embrace you.'
   PL: „Może dlatego, że czas płynął i zebrałem się w latach, zaczęło mi się wydawać, że mógłbym cię zrozumieć i przyjąć.”
162. [Słowo kluczowe [TimeEntangleUnstable] — nazwa] 폭주 - 잔상 얽힘
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TimeEntangleUnstable].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleUnstable]`
   limit: do 50 znaków
   EN: Paroxysm - Afterimage Entanglement
   PL: Paroksyzm - Splot Powideł
163. [Słowo kluczowe [TimeEntangleUnstable] — opis] - 최댓값 : 10\n- 자신의 공격 적중시 수치에 따라 아래 효과 적용\n  · (해당 코인 최종 피해량 / 10)만큼 참격 피해 (수치만큼 발동)\n  · 2 이상 : 화상 1 부여\n  · 3 이상 : 출혈 1 부여\n  · 4 이상 : 다음 턴에 속박 1 부여\n  · 5 이상 : 독 1 부여
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TimeEntangleUnstable].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- On Hit, activate the following effects based on Stack:\n  · Deal Slash damage equal to (final damage of the Coin / 10) (activates (# of Stack) times)\n  · 2+: Inflict 1 Burn\n  · 3+: Inflict 1 Bleed\n  · 4+: Inflict 1 Bind next turn\n  · 5+: Inflict 1 Poison
   PL: - Maks. stosów: 10\n- Przy trafieniu działają następujące efekty zależnie od stosów:\n  · Zadaje obrażenia Cięcia równe (ostateczne obrażenia Monety / 10) (działa tyle razy, ile stosów)\n  · 2+: nakłada 1 Podpalenie\n  · 3+: nakłada 1 Krwawienie\n  · 4+: nakłada 1 Spętanie w następnej turze\n  · 5+: nakłada 1 Zatrucia
164. [Słowo kluczowe [TimeEntangleUnstable] — podsumowanie] 버프 수치에 따라 공격에 추가 효과 적용
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=TimeEntangleUnstable].summary
   limit: do 120 znaków
   EN: Apply additional effects to this unit's attacks based on Stack
   PL: Nakłada dodatkowe efekty na ataki zależnie od liczby stosów
165. [Słowo kluczowe [WillAwakenSinclair] — nazwa] 신(心) - 어느 싱클레어
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=WillAwakenSinclair].name
   kontekst: identyfikator tagu w tekstach: `[WillAwakenSinclair]`
   limit: do 50 znaków
   EN: Shin (心) - A Certain Sinclair
   PL: Shin (心) - Pewien Sinclair
166. [Słowo kluczowe [WillAwakenSinclair] — opis] - 속도 최솟값, 최댓값 3 증가\n- 일방 공격으로 가하는 피해량 +20%\n- 자신의 스킬로 얻는 호흡 위력 +2, 호흡 횟수 +1\n- 정신력이 20 이상이면, 더하기 코인 앞면 나올 확률 +10%\n- 턴 종료 시 정신력 10당, 다음 턴에 신속 1 얻음 (최대 4)\n- 턴 종료 시 정신력 20당, 다음 턴에 위력 증가 1 얻음 (최대 2)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=WillAwakenSinclair].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- Deal +20% damage with Unopposed Attack\n- Gain 2 more Poise Potency and +1 more Poise Count from Skills\n- At 20+ SP, +10% chance to flip Heads for Plus Coins\n- Turn End: Gain 1 Haste next turn for every 10 SP (max 4)\n- Turn End: Gain 1 Power Up next turn for every 20 SP (max 2)
   PL: - Min. i Maks. Szybkość +3\n- Zadaje +20% obrażeń Atakami Jednostronnymi\n- Umiejętności zyskują +2 Siły Oddechu i +1 Licznika Oddechu\n- Przy Poczytalności 20+: +10% szans na Awers dla Monet Plus\n- Na koniec tury zyskuje 1 Pośpiech w następnej turze za każde 10 Poczytalności (maks. 4)\n- Na koniec tury zyskuje 1 Wzrost Mocy w następnej turze za każde 20 Poczytalności (maks. 2)
167. [Słowo kluczowe [SignAwakenSinclair] — nazwa] 표지 - 미래현현
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SignAwakenSinclair].name
   kontekst: identyfikator tagu w tekstach: `[SignAwakenSinclair]`
   limit: do 50 znaków
   EN: Sign - Manifestation of the Future
   PL: Znak - Manifestacja Przyszłości
168. [Słowo kluczowe [SignAwakenSinclair] — opis] - 자신보다 레벨이 높은 적과 합 진행 시, 합 위력 +2\n- 턴 종료 시, 흐트러짐 상태면 다음 턴에 흐트러짐 상태를 해제함
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SignAwakenSinclair].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Clashing against higher-level targets, Clash Power +2\n- Turn End: If Staggered, recover from Stagger next turn
   PL: - W Starciu z celami o wyższym poziomie Moc Starcia +2\n- Na koniec tury, jeżeli jest oszołomiony, w następnej turze wychodzi z Oszołomienia
169. [Słowo kluczowe [SignAwakenSinclair] — tekst klimatyczny] Abraxas
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SignAwakenSinclair].flavor
   limit: do 120 znaków
   EN: Abraxas
   PL: Abraxas
170. [Słowo kluczowe [LimitedAwakenSinclair] — nazwa] 움브라 금제 해제
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LimitedAwakenSinclair].name
   kontekst: identyfikator tagu w tekstach: `[LimitedAwakenSinclair]`
   limit: do 40 znaków
   EN: Umbra Unsealed
   PL: Odpięczętowana Umbra
171. [Słowo kluczowe [LimitedAwakenSinclair] — opis] - 기본 공격 스킬로 가하는 피해량 +10%\n- 턴 시작 시, 더하기 코인 강화 1 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=LimitedAwakenSinclair].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage with Base Attack Skills\n- Turn Start: Gain 1 Plus Coin Boost
   PL: - Podstawowe Umiejętności ataku zadają +10% obrażeń\n- Na początku tury zyskuje 1 Wzmocnienia Monet Plus
172. [Słowo kluczowe [Veteran_LowMorale] — nazwa] 제 2차 연기전쟁의
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Veteran_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Veteran_LowMorale]`
   limit: do 40 znaków
   EN: Of the Second Smoke War
   PL: Drugiej Wojny Dymnej
173. [Słowo kluczowe [Veteran_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 취약 1 얻음\n- 정신력 회복 효율 +2
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Veteran_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Fragile\n- SP Heal Efficiency +2
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wrażliwości\n- Efektywność Leczenia Poczytalności +2
174. [Słowo kluczowe [Veteran_Panic] — nazwa] 제 2차 연기전쟁의
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Veteran_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Veteran_Panic]`
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Słowo kluczowe [Veteran_Panic] — opis] - 패닉\n- 턴 시작 시, 취약 2, 합 위력 증가 2 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Veteran_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Fragile and 2 Clash Power Up
   PL: - Panika\n- Na początku tury zyskuje 2 Wrażliwości i 2 Wzrostu Mocy Starcia
176. [Słowo kluczowe [MiddleFatherSwordOne] — nazwa] 봉인된 검
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFatherSwordOne]`
   limit: do 40 znaków
   EN: Sealed Sword
   PL: Pieczętowany Miecz
177. [Słowo kluczowe [MiddleFatherSwordOne] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].desc
   limit: do 120 znaków
   EN: Unlocks access to certain Skills based on the state of the sword.
   PL: Otwiera dostęp do określonych Umiejętności zależnie od stanu miecza.
178. [Słowo kluczowe [MiddleFatherSwordOne] — tekst klimatyczny] 우애 좋은 세 남매는 유적 깊은 곳으로 향했다
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordOne].flavor
   limit: do 120 znaków
   EN: A trio of tight-knit siblings together journeyed into the depths of the Ruins.
   PL: Zgodne rodzeństwo wyruszyło w głębiny ruin.
179. [Słowo kluczowe [MiddleFatherSwordTwo] — nazwa] 1단계 봉인 해제
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFatherSwordTwo]`
   limit: do 40 znaków
   EN: First Seal Removed
   PL: Zdjęta Pierwsza Pieczęć
180. [Słowo kluczowe [MiddleFatherSwordTwo] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Słowo kluczowe [MiddleFatherSwordTwo] — tekst klimatyczny] 도착한 곳은, 뜨겁고 이글거리는 용암 위로 빌딩이 떠다니는 동굴이었다.\n열기의 근원에는 어느 검… 아니, 검이라 부르기도 힘든 이글거리는 쇳덩어리가 놓여 있었다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordTwo].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There, they came upon a sweltering cavern where a river of lava flowed, carrying buildings on its currents.\nThey traced the river to the source of its heat, and found a sword... that could hardly be called a sword. It was more like a hunk of white-hot metal.
   PL: Znaleźli się w piekącej jaskini, gdzie po płynącej lawie dryfowały budynki.\nU źródła żaru leżał miecz... a raczej kawał białego gorącego metalu, którego nie dało się nazwać mieczem.
182. [Słowo kluczowe [MiddleFatherSwordThree] — nazwa] 2단계 봉인 해제
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFatherSwordThree]`
   limit: do 40 znaków
   EN: Second Seal Removed
   PL: Zdjęta Druga Pieczęć
183. [Słowo kluczowe [MiddleFatherSwordThree] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].desc
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Słowo kluczowe [MiddleFatherSwordThree] — tekst klimatyczny] “이 검은 제일 형님인 내가 가져가마.”\n그 말을 들은 한 아우는 타오르는 욕망과 질투를 참을 수 없었다.\n\n형님과 누님을 죽이고 검을 취했다. 어떤 흔적도 남지 않았겠지.\n하지만 의심받았고, 저항 없이 나락에 떨어졌다.\n그래도 웃음을 잃지 않았다. \n이 전설의 검은 내 것이니까.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordThree].flavor
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "As the eldest brother, I claim this sword as mine."\nThe eldest brother's declaration sparked the inappeasable flame of desire and envy in the youngest brother.\n\nSo, I killed my brother and sister both, and took the sword as my own. I left no evidence behind.\nBut the eyes still gazed upon me with doubt, and when they cast me into this hell, I fell without resistance.\nStill, I did not lose my smile.\nFor the sword of legends was mine.
   PL: „Jako najstarszy brat wezmę ten miecz dla siebie.”\nTe słowa rozpaliły w najmłodszym nieugaszoną pożądanie i zazdrość.\n\nZabiłem więc brata i siostrę, i wziąłem miecz. Ani śladu.\nLecz oczy patrzyły z podejrzeniem, a gdy wtrącili mnie do tego piekła, spadłem bez oporu.\nMimo to nie straciłem uśmiechu.\nBo miecz legend był mój.
185. [Słowo kluczowe [MiddleFatherSwordFour] — nazwa] 레바테인
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFatherSwordFour]`
   limit: do 40 znaków
   EN: Lævateinn
   PL: Lævateinn
186. [Słowo kluczowe [MiddleFatherSwordFour] — opis] 검의 상태에 따라 특정 스킬을 사용할 수 있다.\n턴 시작 시 모든 캐릭터에게 화상 5 부여, 화상 횟수 2 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unlocks access to certain Skills based on the state of the sword.\nTurn Start: Inflict 5 Burn and +2 Burn Count against all units
   PL: Otwiera dostęp do określonych Umiejętności zależnie od stanu miecza.\nNa początku tury nakłada 5 Podpalenia i +2 Licznika Podpalenia na wszystkie postacie
187. [Słowo kluczowe [MiddleFatherSwordFour] — tekst klimatyczny] 안타깝게도 마티아스는 이 검을 제대로 다루지 못했다.\n물론 보통의 사람들은 쥘 수조차 없을 만큼, 까다로운 유물이다.\n그저 쥐고 휘두르기엔 충분했으나, 온전히 다루기에는 적성이 모자랐을 뿐.\n하지만 그에겐 상관 없었다.\n어릴 적부터 꿈꿔왔던 전설의 검을, 자신이 소유하고 휘두를 수 있다는 게 중요했으니.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MiddleFatherSwordFour].flavor
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ironically, the blade was beyond Matthias's ability to properly wield.\nOf course, he would not have been able to hold this sword at all had he not the aptitude for it. It was simply that fickle of a Relic.\nThe truth of the matter was, nevertheless, that his aptitude was nowhere near enough to handle the weapon to its fullest potential.\nBut the man was unconcerned.\nAll that mattered was that the selfsame sword of legends he had dreamed of wielding since childhood was now in his possession, to be swung at his whim.
   PL: Ironia losu: to ostrze przerastało umiejętności Matthiasa.\nOczywiście, bez odpowiedniej predyspozycji nie zdołałby go nawet podnieść — tak wybredny jest ten Relikt.\nPrawda była jednak taka, że jego talent był zbyt mały, by w pełni panować nad bronią.\nAle to człowieka nie obchodziło.\nLiczyło się tylko to, że legendarny miecz, o którym marzył od dzieciństwa, należał teraz do niego i mógł nim machać do woli.
188. [Słowo kluczowe [SojiAbiBuffOne] — nazwa] 계명(雞鳴)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffOne].name
   kontekst: identyfikator tagu w tekstach: `[SojiAbiBuffOne]`
   limit: do 40 znaków
   EN: Dawn's First Crow (雞鳴)
   PL: Świt Koguta (雞鳴)
189. [Słowo kluczowe [SojiAbiBuffOne] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffOne].desc
   limit: do 120 znaków
   EN: Able to Clash with the enemy's specific Slot
   PL: Możliwe Starcie z określonym slotem wroga
190. [Słowo kluczowe [SojiAbiBuffTwo] — nazwa] 일입(日入)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffTwo].name
   kontekst: identyfikator tagu w tekstach: `[SojiAbiBuffTwo]`
   limit: do 40 znaków
   EN: The Sun's Descent (日入)
   PL: Zachód Słońca (日入)
191. [Słowo kluczowe [SojiAbiBuffTwo] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffTwo].desc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Słowo kluczowe [SojiAbiBuffThree] — nazwa] 황혼(黃昏)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffThree].name
   kontekst: identyfikator tagu w tekstach: `[SojiAbiBuffThree]`
   limit: do 40 znaków
   EN: Eventide Glow (黃昏)
   PL: Zmierzch (黃昏)
193. [Słowo kluczowe [SojiAbiBuffThree] — opis] 적의 특정 슬롯에 합이 가능해진 상태
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=SojiAbiBuffThree].desc
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Słowo kluczowe [RyoshuParrySojiTwo] — nazwa] 끊어지지 않은 기억
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParrySojiTwo]`
   limit: do 40 znaków
   EN: Unsevered Memory
   PL: Niedocięte Wspomnienie
195. [Słowo kluczowe [RyoshuParrySojiTwo] — opis] - 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn\n- Cannot Retreat
   PL: - Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku\n- Wycofanie niemożliwe
196. [Słowo kluczowe [RyoshuParrySojiTwo] — podsumowanie] 료슈 특수 효과
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiTwo].summary
   limit: do 120 znaków
   EN: Ryōshū Exclusive Effect
   PL: Efekt specjalny Ryōshū
197. [Słowo kluczowe [RyoshuParrySojiThree] — nazwa] 끊어지지 않는 시간
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParrySojiThree]`
   limit: do 40 znaków
   EN: Unseverable Time
   PL: Niedocięty Czas
198. [Słowo kluczowe [RyoshuParrySojiThree] — opis] - 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능 (아군 포함)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat (including allies)
   PL: - Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe (w tym sojuszników)
199. [Słowo kluczowe [RyoshuParrySojiThree] — podsumowanie] 료슈 특수 효과
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThree].summary
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Słowo kluczowe [HeavenlyKillerStar] — nazwa] 천살성도 - 아라야시키 [天殺星刀阿賴耶識]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeavenlyKillerStar].name
   kontekst: identyfikator tagu w tekstach: `[HeavenlyKillerStar]`
   limit: do 60 znaków
   EN: Tiansha Star's Blade - Arayashiki [天殺星刀阿賴耶識]
   PL: Ostrze Gwiazdy Tiansha - Arayashiki [天殺星刀阿賴耶識]
201. [Słowo kluczowe [HeavenlyKillerStar] — opis] - 속도 최솟값, 최댓값 +6\n- 공격 레벨 +6\n- 스킬로 부여하는 출혈 위력 +3\n- 턴 시작 시, 이번 전투에서 처치한 적 하나당 공격 레벨 증가 3 얻음 (최대 6)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeavenlyKillerStar].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +6\n- Offense Level +6\n- Inflict 3 more Bleed Potency with Skills\n- Turn Start: Gain 3 Offense Level Up for every enemy killed in this Encounter (max 6)
   PL: - Min. i Maks. Szybkość +6\n- Poziom Ataku +6\n- Umiejętności nakładają +3 więcej Siły Krwawienia\n- Na początku tury zyskuje 3 Wzrostu Poziomu Ataku za każdego zabitego wroga w tej walce (maks. 6)
202. [Słowo kluczowe [HeavenlyKillerStar] — tekst klimatyczny] ‘하늘조차 죽인다. 하늘과 땅과 사람, 그리고 나. 이 별은 모든 존재와 시간을 하나로 인식하여 베어낼 수 있는 자에게 뜨는 별.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=HeavenlyKillerStar].flavor
   limit: do 230 znaków
   EN: 'The heavens themselves are not spared—heaven, earth, man, and the self. This star rises only for the one who perceives all existence and time as a single whole to sever them all.'
   PL: „Nie oszczędza nawet nieba — niebo, ziemię, człowieka i mnie. Ta gwiazda wschodzi tylko dla tego, kto widzi całą egzystencję i czas jako jedność i potrafi je wszystko przeciąć.”
203. [Słowo kluczowe [CutoffRyoshu] — nazwa] 절사 [切絲]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutoffRyoshu].name
   kontekst: identyfikator tagu w tekstach: `[CutoffRyoshu]`
   limit: do 40 znaków
   EN: Sever the Thread [切絲]
   PL: Przecięcie Nici [切絲]
204. [Słowo kluczowe [CutoffRyoshu] — opis] - 턴 시작 시,\n· 출혈 3 얻음, 출혈 횟수 3 증가\n· (수치/3)만큼 참격 피해를 받음\n- 피격 시, (수치/5)만큼 참격 피해를 받음\n- 이 수치가 증가할수록......\n- 최대 100
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutoffRyoshu].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 3 Bleed and +3 Bleed Count\n· Take Slash damage equal to (Stack / 3)\n- When hit, take Slash damage equal to (Stack / 5)\n- The more this effect stacks...\n- Max Stack: 100
   PL: - Na początku tury,\n· Zyskuje 3 Krwawienia i +3 Licznika Krwawienia\n· Otrzymuje obrażenia Cięcia równe (stosy / 3)\n- Przy trafieniu otrzymuje obrażenia Cięcia równe (stosy / 5)\n- Im więcej stosów...\n- Maks. 100
205. [Słowo kluczowe [CutoffRyoshu] — tekst klimatyczny] ‘모든 것을 끊어낸다. 너도 나도, 지금까지와 앞으로의 모든 것을.’\n\n‘그렇게 해서 아라야를 데리고 온다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutoffRyoshu].flavor
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'Let everything be severed—you, me, all that has been, and all that will be.'\n\n'Once it is done... I will take Araya back.'
   PL: „Niech wszystko zostanie odcięte — ty, ja, cała przeszłość i przyszłość.”\n\n„A wtedy przywrócę Arayę.”
206. [Słowo kluczowe [CutbondRyoshu] — nazwa] 무아 [無我]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutbondRyoshu].name
   kontekst: identyfikator tagu w tekstach: `[CutbondRyoshu]`
   limit: do 40 znaków
   EN: Muga [無我]
   PL: Muga [無我]
207. [Słowo kluczowe [CutbondRyoshu] — opis] - 턴 시작 시, 수치 10당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 이 수치가 증가할수록......\n- 최대 100
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutbondRyoshu].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Offense Level Up and 1 Defense Level Up for every 10 Stack\n- The more this effect stacks...\n- Max Stack: 100
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 10 stosów\n- Im więcej stosów...\n- Maks. 100
208. [Słowo kluczowe [CutbondRyoshu] — tekst klimatyczny] ‘그러니 칼날을 아낀다. 준비가 되었을 때, 다시 거미집으로 들어간다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CutbondRyoshu].flavor
   limit: do 120 znaków
   EN: 'So I must hold back on using the blade. And once I'm ready, I will return to that House.'
   PL: „Dlatego muszę oszczędzać ostrze. A gdy będę gotowa, wrócę do Domu Pajęczyn.”
209. [Słowo kluczowe [EsteemNeeds] — nazwa] 인정 욕구
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EsteemNeeds].name
   kontekst: identyfikator tagu w tekstach: `[EsteemNeeds]`
   limit: do 40 znaków
   EN: Desire for Acknowledgement
   PL: Głód Uznania
210. [Słowo kluczowe [EsteemNeeds] — opis] - 수치 1당 료슈에게 가하는 피해량과 받는 피해량 +5% (최대 100%)\n- 수치 5당, 료슈를 메인 타겟으로 공격 시 최종 위력 +1 (최대 4)\n- 수치가 10 이상이면, 합 패배 시 5만큼 정신력 피해\n- 최대 20
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EsteemNeeds].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every Stack, Deal +5% damage to and take +5% damage from Ryōshū (max 100%)\n- Final Power +1 for every 5 Stack when attacking Ryōshū as the main target (max 4)\n- At 10+ Stack, lose 5 SP upon Clash Lose\n- Max Stack: 20
   PL: - Za każdy stos zadaje i otrzymuje +5% obrażeń od i wobec Ryōshū (maks. 100%)\n- Moc Końcowa +1 za każde 5 stosów przy ataku Ryōshū jako głównym celu (maks. 4)\n- Przy 10+ stosach po przegranej w Starciu traci 5 Poczytalności\n- Maks. 20 stosów
211. [Słowo kluczowe [EsteemNeeds] — tekst klimatyczny] ‘돌아가면 뤼,뤼엔 씨에게 칭찬받아야지….’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=EsteemNeeds].flavor
   limit: do 120 znaków
   EN: 'Once I'm back home, M-Mister Rien will tell me I did good...'
   PL: „Po powrocie M-Mister Rien powie mi, że dobrze zrobiłam…”
212. [Słowo kluczowe [Fugacious] — nazwa] 검의 길
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Fugacious].name
   kontekst: identyfikator tagu w tekstach: `[Fugacious]`
   limit: do 40 znaków
   EN: Way of the Blade
   PL: Droga Ostrza
213. [Słowo kluczowe [Fugacious] — opis] - 턴 시작시,\n· 수치 5당 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n· 수치 10당 피해량 증가 1, 취약 1 얻음\n- 최댓값 : 50
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Fugacious].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n· Gain 1 Damage Up and 1 Fragile for every 10 Stack\n- Max Stack: 50
   PL: - Na początku tury,\n· Zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 stosów\n· Zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości za każde 10 stosów\n- Maks. stosów: 50
214. [Słowo kluczowe [Fugacious] — tekst klimatyczny] 덧없는 꿈이어도 괜찮다.\n이번 생에 별의 이름을 얻지 못해도, 검의 길을 걷는 것만으로 검은 예리해지고 검술은 단조될 테니.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Fugacious].flavor
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It matters not if this dream is but a fleeting one.\nThough I may fail to inherit the name of a Star in this life, walking the Way of the Blade shall sharpen and temper this sword of mine.
   PL: Nie szkodzi, jeśli to jedynie ulotny sen.\nChoć nie odziedziczę w tym życiu imienia Gwiazdy, sama droga ostrza naostrzy i utwardzi to ostrze.
215. [Słowo kluczowe [ObsessedTeacher_LowMorale] — nazwa] 가문의 수치
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessedTeacher_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ObsessedTeacher_LowMorale]`
   limit: do 40 znaków
   EN: Shame of the Family
   PL: Wstyd Rodziny
216. [Słowo kluczowe [ObsessedTeacher_LowMorale] — opis] - 턴 시작 시 참격 피해 증가 1, 합 위력 증가 1, 취약 1 얻음\n- 스킬 사용 시 망을 얻을 수 없음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessedTeacher_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Slash DMG Up, 1 Clash Power Up, and 1 Fragile\n- Cannot gain Mang when using Skills
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń Cięcia, 1 Wzrost Mocy Starcia i 1 Wrażliwości\n- Przy użyciu Umiejętności nie może zdobyć Mangu
217. [Słowo kluczowe [ObsessedTeacher_Panic] — nazwa] 가문의 수치
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessedTeacher_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ObsessedTeacher_Panic]`
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Słowo kluczowe [ObsessedTeacher_Panic] — opis] - 턴 시작 시 참격 피해 증가 2, 합 위력 증가 2, 취약 2 얻음\n- 스킬 사용 시 망을 얻을 수 없음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=ObsessedTeacher_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Slash DMG Up, 2 Clash Power Up, and 2 Fragile\n- Cannot gain Mang when using Skills
   PL: - Na początku tury zyskuje 2 Wzrostu Obrażeń Cięcia, 2 Wzrostu Mocy Starcia i 2 Wrażliwości\n- Przy użyciu Umiejętności nie może zdobyć Mangu
219. [Słowo kluczowe [AgainstMyWill_LowMorale] — nazwa] ‘나, 날… 죽여줘..’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AgainstMyWill_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[AgainstMyWill_LowMorale]`
   limit: do 40 znaków
   EN: "K-kill... kill me..."
   PL: „Z-zabij... zabij mnie..”
220. [Słowo kluczowe [AgainstMyWill_LowMorale] — opis] 턴 시작 시 합 위력 감소 8, 위력 감소 5 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AgainstMyWill_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 8 Clash Power Down and 5 Power Down
   PL: Na początku tury zyskuje 8 Spadek Mocy Starcia i 5 Spadek Mocy
221. [Słowo kluczowe [AgainstMyWill_Panic] — nazwa] ‘나, 날… 죽여줘..’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AgainstMyWill_Panic].name
   kontekst: identyfikator tagu w tekstach: `[AgainstMyWill_Panic]`
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Słowo kluczowe [AgainstMyWill_Panic] — opis] 턴 시작 시 합 위력 감소 10, 위력 감소 5 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=AgainstMyWill_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 10 Clash Power Down and 5 Power Down
   PL: Na początku tury zyskuje 10 Spadek Mocy Starcia i 5 Spadek Mocy
223. [Słowo kluczowe [IndexPrescriptRien_0] — nazwa] 지령[단말기] I
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_0].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptRien_0]`
   limit: do 40 znaków
   EN: Prescript: [Device] I
   PL: Nakaz [Urządzenie] I
224. [Słowo kluczowe [IndexPrescriptRien_0] — opis] 지령 대상을 공격하여 적중한다. 기한은 첫 번째 턴까지.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_0].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target before the first turn ends.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Cel Nakazu i trafia. Termin: do końca pierwszej tury.\n\n- Na początku tury zdobywany przy braku Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
225. [Słowo kluczowe [IndexPrescriptRien_1] — nazwa] 지령[단말기] II
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_1].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptRien_1]`
   limit: do 40 znaków
   EN: Prescript: [Device] II
   PL: Nakaz [Urządzenie] II
226. [Słowo kluczowe [IndexPrescriptRien_1] — opis] 지령 대상을 공격하여 적중한다. 또는 이번 턴에 공격을 4회 이상 적중한다. 기한은 네 번째 턴까지.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_1].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target; or, before this turn passes, hit with 4 or more attacks. Complete before the 4th turn.\n\n- Turn Start: Gain this effect when this unit has Unlock - 1\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Atakuje Cel Nakazu i trafia; albo trafia 4 lub więcej ataków przed końcem tury. Termin: do czwartej tury.\n\n- Na początku tury zdobywany przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
227. [Słowo kluczowe [IndexPrescriptRien_2] — nazwa] 지령[단말기] III
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_2].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptRien_2]`
   limit: do 40 znaków
   EN: Prescript: [Device] III
   PL: Nakaz [Urządzenie] III
228. [Słowo kluczowe [IndexPrescriptRien_2] — opis] 아홉 종류의 무기를 사용하는 강력한 스킬을 사용한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a powerful Skill that uses 9 different weapon types.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Używa potężnej Umiejętności, która używa 9 różnych typów broni.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
229. [Słowo kluczowe [IndexPrescriptRien_3] — nazwa] 지령[단말기] IV
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_3].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptRien_3]`
   limit: do 40 znaków
   EN: Prescript: [Device] IV
   PL: Nakaz [Urządzenie] IV
230. [Słowo kluczowe [IndexPrescriptRien_3] — opis] 모든 방해물을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescriptRien_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all obstacles before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Wyeliminuj wszystkie przeszkody, zanim przyjdzie kolejny Nakaz.\n\n- Na początku tury zdobywany przy Odblokowaniu - III
231. [Słowo kluczowe [IndexPrescript_RienSecondPhase] — nazwa] 지령[단말기] - 경고
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescript_RienSecondPhase]`
   limit: do 50 znaków
   EN: Prescript: [Device] - Warning
   PL: Nakaz [Urządzenie] - Ostrzeżenie
232. [Słowo kluczowe [IndexPrescript_RienSecondPhase] — opis] 지령 대상을 우선적으로 처치한다.\n\n- 두 번째 페이즈부터 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Prioritize eliminating The Prescript's Target.\n\n- Gain this effect starting from the 2nd phase
   PL: Priorytetowo eliminuj Cel Nakazu.\n\n- Zdobywany od drugiej fazy
233. [Słowo kluczowe [IndexPrescript_RienSecondPhase] — tekst klimatyczny] ‘지령이 수행되지 않을 때마다 단말기가 내는 비프음은 점차 빨라진다.’\n\n‘그 긴박한 울림에 나의 심박수도 높아져가는 것만 같다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=IndexPrescript_RienSecondPhase].flavor
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'The Device's beeping accelerates with every second I let pass without fulfilling a Prescript.'\n\n'And with it, so do the intervals of my heartbeat.'
   PL: „Za każdym razem, gdy Nakaz pozostaje niewykonany, pikanie Urządzenia przyspiesza.”\n\n„Wyda się, że wraz z tym gorącym odgłosem przyspiesza też moje serce.”
234. [Słowo kluczowe [UnlockBuff_Rien1] — nazwa] 해금 - I
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien1].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_Rien1]`
   limit: do 40 znaków
   EN: Unlock - I
   PL: Odblokowanie - I
235. [Słowo kluczowe [UnlockBuff_Rien1] — opis] - 공격 레벨 +1, 방어 레벨 +1\n- 전투 종료 시, 정신력 10 회복
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1, Defense Level +1\n- Combat End: Heal 10 SP
   PL: - Poziom Ataku +1, Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 10 Poczytalności
236. [Słowo kluczowe [UnlockBuff_Rien2] — nazwa] 해금 - II
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien2].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_Rien2]`
   limit: do 40 znaków
   EN: Unlock - II
   PL: Odblokowanie - II
237. [Słowo kluczowe [UnlockBuff_Rien2] — opis] - 공격 레벨 +2, 방어 레벨 +2\n- 전투 종료 시, 정신력 20 회복
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2, Defense Level +2\n- Combat End: Heal 20 SP
   PL: - Poziom Ataku +2, Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 20 Poczytalności
238. [Słowo kluczowe [UnlockBuff_Rien3] — nazwa] 해금 - III
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien3].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_Rien3]`
   limit: do 40 znaków
   EN: Unlock - III
   PL: Odblokowanie - III
239. [Słowo kluczowe [UnlockBuff_Rien3] — opis] - 공격 레벨 +3, 방어 레벨 +3\n- 전투 종료 시, 정신력 30 회복
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=UnlockBuff_Rien3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3, Defense Level +3\n- Combat End: Heal 30 SP
   PL: - Poziom Ataku +3, Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 30 Poczytalności
240. [Słowo kluczowe [KarmaOfIndexRien] — nazwa] 카르마
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KarmaOfIndexRien].name
   kontekst: identyfikator tagu w tekstach: `[KarmaOfIndexRien]`
   limit: do 40 znaków
   EN: Karmic Consequence
   PL: Karma
241. [Słowo kluczowe [KarmaOfIndexRien] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 수치 40당 합 위력 감소 1 얻음\n- 최대 100
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KarmaOfIndexRien].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stack\n· Gain 1 Fragile for every 20 Stack\n· Gain 1 Clash Power Down for every 40 Stack\n- Max Stack: 100
   PL: - Na początku tury\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Zyskuje 1 Spadek Mocy Starcia za każde 40 stosów\n- Maks. 100
242. [Słowo kluczowe [KarmaOfIndexRien_2Phase] — nazwa] 카르마 [포르투나]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].name
   kontekst: identyfikator tagu w tekstach: `[KarmaOfIndexRien_2Phase]`
   limit: do 40 znaków
   EN: Karmic Consequence [Fortuna]
   PL: Karma [Fortuna]
243. [Słowo kluczowe [KarmaOfIndexRien_2Phase] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 수치 40당 합 위력 감소 1 얻음\n- 최대 200
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stack\n· Gain 1 Fragile for every 20 Stack\n· Gain 1 Clash Power Down for every 40 Stack\n- Max Stack: 200
   PL: - Na początku tury\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Zyskuje 1 Spadek Mocy Starcia za każde 40 stosów\n- Maks. 200
244. [Słowo kluczowe [KarmaOfIndexRien_2Phase] — tekst klimatyczny] O Fortúna velut luna statu variabilis
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KarmaOfIndexRien_2Phase].flavor
   limit: do 120 znaków
   EN: O Fortúna velut luna statu variabilis
   PL: O Fortúna velut luna statu variabilis
245. [Słowo kluczowe [BurningWoundRien_Mask] — nazwa] 뤼엔의 가면
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].name
   kontekst: identyfikator tagu w tekstach: `[BurningWoundRien_Mask]`
   limit: do 40 znaków
   EN: Rien's Mask
   PL: Maska Rien
246. [Słowo kluczowe [BurningWoundRien_Mask] — opis] - 공격 레벨 -5, 방어 레벨 -5\n- 수치 1당, 화상 또는 출혈을 부여하는 스킬(위력, 횟수, 특수 키워드 포함)로 받는 피해 +5%\n· 화상과 출혈 둘 다 부여 시, 대신 +7.5%\n- 최대 1
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -5, Defense Level -5\n- For every Stack, take +5% damage from Skills that inflict Burn or Bleed (includes Potency, Count, and Unique variants)\n· If the Skill inflicts both Burn and Bleed, take +7.5% damage for every Stack instead\n- Max Stack: 1
   PL: - Poziom Ataku -5, Poziom Obrony -5\n- Za każdy stos otrzymuje +5% obrażeń od Umiejętności nakładających Podpalenie lub Krwawienie (z Siłą, Licznikiem i wariantami Specjalnymi)\n· Jeżeli Umiejętność nakłada oba, zamiast tego +7,5% za stos\n- Maks. 1
247. [Słowo kluczowe [BurningWoundRien_Mask] — tekst klimatyczny] “볼 때마다 아파서 가리고 있어.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien_Mask].flavor
   limit: do 120 znaków
   EN: "I keep it covered because it hurts to even look at."
   PL: „Zasłaniam, bo samo patrzenie na to boli.”
248. [Słowo kluczowe [BurningWoundRien] — nazwa] 이글거리는 상처
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien].name
   kontekst: identyfikator tagu w tekstach: `[BurningWoundRien]`
   limit: do 40 znaków
   EN: Sizzling Wound
   PL: Kipiąca Rana
249. [Słowo kluczowe [BurningWoundRien] — opis] - 공격 레벨 -5, 방어 레벨 -5\n- 턴 시작 시 수치 1당, 화상 횟수 1, 출혈 횟수 1 증가\n- 수치 1당, 화상 또는 출혈을 부여하는 스킬(위력, 횟수, 특수 키워드 포함)로 받는 피해 +10%\n· 화상과 출혈 둘 다 부여 시, 대신 +15%\n- 최대 5
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -5, Defense Level -5\n- Turn Start: Gain +1 Burn Count and +1 Bleed Count for every Stack\n- For every Stack, take +10% damage from Skills that inflict Burn or Bleed (includes Potency, Count, and Unique variants)\n· If the Skill inflicts both Burn and Bleed, take +15% damage for every Stack instead\n- Max Stack: 5
   PL: - Poziom Ataku -5, Poziom Obrony -5\n- Na początku tury zyskuje +1 Licznika Podpalenia i +1 Licznika Krwawienia za każdy stos\n- Za każdy stos otrzymuje +10% obrażeń od Umiejętności nakładających Podpalenie lub Krwawienie (z Siłą, Licznikiem i wariantami Specjalnymi)\n· Jeżeli Umiejętność nakłada oba, zamiast tego +15% za stos\n- Maks. 5
250. [Słowo kluczowe [BurningWoundRien] — tekst klimatyczny] 그 검이 가까워지면 상처는 아물지 않고, 검결의 열로 타들어간 살점이 다시 익어간다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BurningWoundRien].flavor
   limit: do 130 znaków
   EN: When in proximity of the sword, the wound unheals and the flesh that once cooled burns once again.
   PL: W pobliżu tego miecza rana nie chce się goić, a raz ostudzone mięso znów zaczyna się palić.
251. [Słowo kluczowe [Shin_Rien] — nazwa] 신(心) - 뤼엔
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Shin_Rien].name
   kontekst: identyfikator tagu w tekstach: `[Shin_Rien]`
   limit: do 40 znaków
   EN: Shin (心) - Rien
   PL: Shin (心) - Rien
252. [Słowo kluczowe [Shin_Rien] — opis] - 턴 시작 시 잃은 체력에 비례하여,\n· 15%당 피해량 증가 1 얻음 (최대 5)\n· 40%당 공격 위력 증가 1 얻음 (최대 2)\n- 자신의 스킬로 얻는 호흡 위력 +1, 호흡 횟수 +1\n- 자신의 정신력이 대상보다 높으면, 정신력 차이 2당 피해량 +1% (최대 30%)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Shin_Rien].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Based on the missing HP on this unit...\n· Gain 1 Damage Up for every 15% missing HP (max 5)\n· Gain 1 Attack Power Up for every 40% missing HP (max 2)\n- Gain +1 more Poise Potency and Count from this unit's Skills\n- If this unit's SP is higher than the target's, deal +1% damage for every 2 SP difference (max 30%)
   PL: - Na początku tury, zależnie od brakującego HP,\n· Zyskuje 1 Wzrost Obrażeń za każde 15% brakującego HP (maks. 5)\n· Zyskuje 1 Wzrost Mocy Ataku za każde 40% brakującego HP (maks. 2)\n- Umiejętności zyskują +1 więcej Siły Oddechu i Licznika Oddechu\n- Jeżeli Poczytalność jest wyższa niż celu, zadaje +1% obrażeń za każde 2 różnicy Poczytalności (maks. 30%)
253. [Słowo kluczowe [StackRienSpecialSkill] — nazwa] 대행 [헤르메스]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=StackRienSpecialSkill].name
   kontekst: identyfikator tagu w tekstach: `[StackRienSpecialSkill]`
   limit: do 40 znaków
   EN: Procuration [Hermes]
   PL: Procuration [Hermes]
254. [Słowo kluczowe [StackRienSpecialSkill] — opis] - 공격 스킬 사용 시, 1 얻음 (스킬별 1회, 동일한 스킬로 2 이상 획득 불가)\n- 턴 시작 시 수치가 9면, 강력한 스킬을 사용\n- 특정 스킬에서 소모
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=StackRienSpecialSkill].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Stack when using an Attack Skill (once per Skill; does not gain Stack from the same Skill twice)\n- Turn Start: at 9 Stack, use a powerful Skill\n- Consumed when using a certain Skill
   PL: - Zyskuje 1 stos przy użyciu Umiejętności ataku (1 raz na Umiejętność; ta sama Umiejętność nie liczy się dwukrotnie)\n- Na początku tury przy 9 stosach używa potężnej Umiejętności\n- Zużywana przez określone Umiejętności
255. [Słowo kluczowe [StackRienSpecialSkill] — tekst klimatyczny] “신의 뜻에 따라.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=StackRienSpecialSkill].flavor
   limit: do 120 znaków
   EN: "As my god commands."
   PL: „Z woli boga.”
256. [Słowo kluczowe [RienWeapon01Hatchet] — nazwa] 손도끼로 갈비뼈를 찍어 내릴 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon01Hatchet].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon01Hatchet]`
   limit: do 70 znaków
   EN: When hacking through the ribs with a hatchet...
   PL: Gdy siekierą odłupuje się żebra…
257. [Słowo kluczowe [RienWeapon01Hatchet] — opis] - 타격 피해를 입힘\n- 파괴되지 않고 적중 시, 호흡 2 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon01Hatchet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- On Hit without Cracking, gain 2 Poise
   PL: - Zadaje obrażenia Obuchu\n- Przy trafieniu bez Roztrzaskania zyskuje 2 Oddechu
258. [Słowo kluczowe [RienWeapon01Hatchet2phase] — nazwa] 손도끼로 갈비뼈를 찍어 내릴 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon01Hatchet2phase]`
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Słowo kluczowe [RienWeapon01Hatchet2phase] — opis] - 타격 피해를 입힘\n- 파괴되지 않고 적중 시, 호흡 2 얻음, 호흡 횟수 2 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- On Hit without Cracking, gain 2 Poise and +2 Poise Count
   PL: - Zadaje obrażenia Obuchu\n- Przy trafieniu bez Roztrzaskania zyskuje 2 Oddechu i +2 Licznika Oddechu
260. [Słowo kluczowe [RienWeapon01Hatchet2phase] — tekst klimatyczny] “이건 꽝에 가깝지만 포크보다는 낫지.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon01Hatchet2phase].flavor
   limit: do 120 znaków
   EN: "This is barely a weapon, but it's better than a fork."
   PL: „To ledwie narzędzie, ale lepsze niż widelec.”
261. [Słowo kluczowe [RienWeapon02Stiletto] — nazwa] 스틸레토로 허파를 꿰뚫을 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon02Stiletto].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon02Stiletto]`
   limit: do 70 znaków
   EN: When penetrating the lungs with a stiletto...
   PL: Gdy stiletto przebija płuca…
262. [Słowo kluczowe [RienWeapon02Stiletto] — opis] - 관통 피해를 입힘\n- 파괴되지 않고 적중 시, 침잠 2 부여
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon02Stiletto].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- On Hit Without Cracking, inflict 2 Sinking
   PL: - Zadaje obrażenia Kłucia\n- Przy trafieniu bez Roztrzaskania nakłada 2 Zatonięcia
263. [Słowo kluczowe [RienWeapon02Stiletto2phase] — nazwa] 스틸레토로 허파를 꿰뚫을 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon02Stiletto2phase]`
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Słowo kluczowe [RienWeapon02Stiletto2phase] — opis] - 관통 피해를 입힘\n- 파괴되지 않고 적중 시, 침잠 2 부여, 침잠 횟수 2 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- On Hit without Cracking, inflict 2 Sinking and +2 Sinking Count
   PL: - Zadaje obrażenia Kłucia\n- Przy trafieniu bez Roztrzaskania nakłada 2 Zatonięcia i +2 Licznika Zatonięcia
265. [Słowo kluczowe [RienWeapon02Stiletto2phase] — tekst klimatyczny] “횡으로 휘둘러야 하는 상황에 이게 나왔을 때는 식은땀이 나더구나. 나하고는 맞지 않아.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon02Stiletto2phase].flavor
   limit: do 230 znaków
   EN: "I couldn't help but feel a dreadful chill run down my back whenever I'm given this weapon when the situation calls for a horizontal swing. I find it hard to work with this."
   PL: „Za każdym razem, gdy w sytuacji wymagającej cięcia poziomego trafia się to narzędzie, na plecach pojawia się zimny pot. To nie dla mnie.”
266. [Słowo kluczowe [RienWeapon03Greatsword] — nazwa] 바스타드 소드로 어깨와 머리를 짓이길 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon03Greatsword].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon03Greatsword]`
   limit: do 100 znaków
   EN: When cleaving through the shoulder and the skull with a bastard sword...
   PL: Gdy bastardem miażdży się bark i czaszkę…
267. [Słowo kluczowe [RienWeapon03Greatsword] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 다음 턴에 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon03Greatsword].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +5% damage\n- On Hit without Cracking, gain 1 Offense Level Up next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania zyskuje 1 Wzrost Poziomu Ataku w następnej turze (2 razy na turę)
268. [Słowo kluczowe [RienWeapon03Greatsword2phase] — nazwa] 바스타드 소드로 어깨와 머리를 짓이길 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon03Greatsword2phase]`
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Słowo kluczowe [RienWeapon03Greatsword2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 다음 턴까지 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, gain 1 Offense Level Up until next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania zyskuje 1 Wzrost Poziomu Ataku do następnej tury (2 razy na turę)
270. [Słowo kluczowe [RienWeapon03Greatsword2phase] — tekst klimatyczny] “이 검은 무난하지만, 너무 무난해서 아쉬울 때가 있지. 그래도 기본기를 갖췄다면 충분히 쓸 만하단다.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon03Greatsword2phase].flavor
   limit: do 240 znaków
   EN: "This sword, it's... passable, but that quality in and of itself leaves a lot to be desired. Nevertheless, it can still be a trusty weapon as long as your fundamental skills are solid."
   PL: „Ten miecz jest... przyzwoity, ale ta przyzwoitość sama w sobie pozostawia wiele do życzenia. Mimo to przy solidnych podstawach posłuży nieźle.”
271. [Słowo kluczowe [RienWeapon04Rapier] — nazwa] 레이피어로 몸에 10개 이상의 구멍을 내야할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon04Rapier].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon04Rapier]`
   limit: do 80 znaków
   EN: When punching 10 or more holes in the torso with a rapier...
   PL: Gdy rapierem trzeba zrobić w torsie 10 lub więcej dziur…
272. [Słowo kluczowe [RienWeapon04Rapier] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 다음 턴에 방어 레벨 감소 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon04Rapier].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +5% damage\n- On Hit without Cracking, inflict 1 Defense Level Down next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Spadek Poziomu Obrony w następnej turze (2 razy na turę)
273. [Słowo kluczowe [RienWeapon04Rapier2phase] — nazwa] 레이피어로 몸에 10개 이상의 구멍을 내야할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon04Rapier2phase]`
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Słowo kluczowe [RienWeapon04Rapier2phase] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 다음 턴까지 방어 레벨 감소 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, inflict 1 Defense Level Down until next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Spadek Poziomu Obrony do następnej tury (2 razy na turę)
275. [Słowo kluczowe [RienWeapon04Rapier2phase] — tekst klimatyczny] “스틸레토보다 예리하고 긴 무기지. 나는 기교를 좋아해서, 레이피어도 좋아한단다.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon04Rapier2phase].flavor
   limit: do 180 znaków
   EN: "A weapon longer and sharper than the stiletto. I enjoy the rapier as well, as it lends itself quite well to more dexterous techniques."
   PL: „Broń dłuższa i ostrzejsza od stiletto. Lubię też rapiera — świetnie nadaje się do zwinnych technik.”
276. [Słowo kluczowe [RienWeapon05Sledgehammer] — nazwa] 망치로 뒤통수를 으깨야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon05Sledgehammer]`
   limit: do 80 znaków
   EN: When caving in the back of the skull with a hammer...
   PL: Gdy młotem trzeba rozbić tył czaszki…
277. [Słowo kluczowe [RienWeapon05Sledgehammer] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시, 3만큼 흐트러짐 피해
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +5% damage\n- On Hit without Cracking, raise target's Stagger Threshold by 3
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania podnosi Próg Oszołomienia celu o 3
278. [Słowo kluczowe [RienWeapon05Sledgehammer2phase] — nazwa] 망치로 뒤통수를 으깨야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon05Sledgehammer2phase]`
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Słowo kluczowe [RienWeapon05Sledgehammer2phase] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +7.5%\n- 파괴되지 않고 적중 시, 5만큼 흐트러짐 피해
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +7.5% damage\n- On Hit without Cracking, raise target's Stagger Threshold by 5
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +7,5% obrażeń\n- Przy trafieniu bez Roztrzaskania podnosi Próg Oszołomienia celu o 5
280. [Słowo kluczowe [RienWeapon05Sledgehammer2phase] — tekst klimatyczny] “단순하지만 확실하지. 손도끼처럼 애매하지 않아. 확실히 터트릴 수 있어.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon05Sledgehammer2phase].flavor
   limit: do 120 znaków
   EN: "Simple, but final. It's not a half-measure like a hatchet—it <i>will</i> crush whatever it hits."
   PL: „Prosto, ale definitywnie. To nie półśrodek jak siekiera — ta rzeczywiście roztrzaska to, w co trafi.”
281. [Słowo kluczowe [RienWeapon06Ultragreatsword] — nazwa] 커다란 검으로 몸통을 갈라야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon06Ultragreatsword]`
   limit: do 60 znaków
   EN: When rending the body with a greatsword...
   PL: Gdy wielkim mieczem trzeba przeciąć ciało…
282. [Słowo kluczowe [RienWeapon06Ultragreatsword] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 참격 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Slash Fragility (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Cięcie (2 razy na turę)
283. [Słowo kluczowe [RienWeapon06Ultragreatsword2phase] — nazwa] 커다란 검으로 몸통을 갈라야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon06Ultragreatsword2phase]`
   limit: do 60 znaków
   EN: When rending the body with a great sword...
   PL: Gdy wielkim mieczem trzeba przeciąć ciało…
284. [Słowo kluczowe [RienWeapon06Ultragreatsword2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 참격 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Slash Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Cięcie do następnej tury (2 razy na turę)
285. [Słowo kluczowe [RienWeapon06Ultragreatsword2phase] — tekst klimatyczny] “이렇게 크고 무거운 검은 무엇보다 무게중심이 중요하단다.”\n“그리고 중량을 이용하는 게 좋지.”\n“5층 옥상에서 떨어지며 이걸로 1급 해결사를 암살했을 때가 생각나는구나.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon06Ultragreatsword2phase].flavor
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "When it comes to wielding blades of ponderous size and weight, such as this one, it is important to find your center of gravity."\n"And of course, don't forget to take advantage of its sheer mass."\n"I once jumped from the rooftop of a five-story building with this weapon and dropped on top of a Grade 1 Fixer's head, killing him instantly."
   PL: „Przy tak wielkiej i ciężkiej broni najważniejszy jest środek ciężkości.”\n„I wykorzystuj jej masę.”\n„Przypominam sobie, jak, spadając z dachu pięciopiętrowego budynku, udało mi się jednym ciosem zabić tą bronią Fixera I klasy.”
286. [Słowo kluczowe [RienWeapon07Lance] — nazwa] 랜스로 20인치의 구멍을 내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon07Lance].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon07Lance]`
   limit: do 60 znaków
   EN: When boring a 20-inch hole with a lance...
   PL: Gdy lancą trzeba zrobić 20-calową dziurę…
287. [Słowo kluczowe [RienWeapon07Lance] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 관통 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon07Lance].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Pierce Fragility (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Kłucie (2 razy na turę)
288. [Słowo kluczowe [RienWeapon07Lance2phase] — nazwa] 랜스로 20인치의 구멍을 내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon07Lance2phase]`
   (powtórzenie elementu 286 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Słowo kluczowe [RienWeapon07Lance2phase] — opis] - 관통 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 관통 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Pierce damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Pierce Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Kłucia\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Kłucie do następnej tury (2 razy na turę)
290. [Słowo kluczowe [RienWeapon07Lance2phase] — tekst klimatyczny] “당첨인 무기야. 이 랜스에는 자체적인 가속 기능도 있어서 저 멀리서도 벽이나 가로막는 자들을 다 뚫어가며 목표까지 꿰뚫을 수 있지.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon07Lance2phase].flavor
   limit: do 290 znaków
   EN: "I'd consider this weapon a jackpot. This lance has a self-propelling property as well, which is what allows it to punch through the target—and anything that stands between us as well, whether that is a wall or a person."
   PL: „To broń-jackpot. Ta lanca ma własny napęd, więc z daleka przebije wszystko, co stanie między nami a celem — ścianę czy człowieka.”
291. [Słowo kluczowe [RienWeapon08Chain] — nazwa] 채찍으로 살점을 만 갈래 떼어내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon08Chain].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon08Chain]`
   limit: do 80 znaków
   EN: When ripping the flesh to ten thousand strips with a whip...
   PL: Gdy biczem trzeba oderwać mięso na dziesięć tysięcy strzępów…
292. [Słowo kluczowe [RienWeapon08Chain] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +10%\n- 파괴되지 않고 적중 시, 타격 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon08Chain].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +10% damage\n- On Hit without Cracking, inflict 1 Blunt Fragility (2 times per turn)
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +10% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Obuch (2 razy na turę)
293. [Słowo kluczowe [RienWeapon08Chain2phase] — nazwa] 채찍으로 살점을 만 갈래 떼어내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon08Chain2phase]`
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Słowo kluczowe [RienWeapon08Chain2phase] — opis] - 타격 피해를 입힘\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시, 다음 턴까지 타격 취약 1 부여 (턴당 2회)
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Blunt damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Blunt Fragility until next turn (2 times per turn)
   PL: - Zadaje obrażenia Obuchu\n- Ta Moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nakłada 1 Wrażliwość na Obuch do następnej tury (2 razy na turę)
295. [Słowo kluczowe [RienWeapon08Chain2phase] — tekst klimatyczny] “누군가에게는 꽝일 수 있겠지만… 나는 마음에 들어.”\n“이 채찍에 맞은 사람은 살점이 떨어져 피를 흘린단다. 그러다가 점점 고통과 탈진으로 허덕이지.”\n“점점 약해져 가는 모습을 볼 수 있는 게 좋아. 그리고 급할 때는 교살용으로도 쓸 수 있지.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon08Chain2phase].flavor
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "While some may equate this weapon to losing a lottery... I am quite fond of it."\n"When this whip cracks, it doesn't just make them bleed; it tears a strip off the target's flesh, and with it their resolve and energy."\n"I appreciate that it lets me observe the full process of how someone is deconstructed as they are weakened. Oh, and it can also be used to strangle in a pinch."
   PL: „Dla niektórych to przegrana w loterii... mnie się podoba.”\n„Kto dostaje tym biczem, traci strzępy mięsa i krwawi. Stopniowo pada od bólu i wyczerpania.”\n„Lubię patrzeć, jak ktoś rozpada się kawałek po kawałku. A w razie potrzeby służy też do duszenia.”
296. [Słowo kluczowe [RienWeapon09Scythe] — nazwa] 낫으로… 누군가처럼 공간을 따라 베어내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon09Scythe].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon09Scythe]`
   limit: do 110 znaków
   EN: When lacerating through space itself with a scythe, like a certain someone...
   PL: Gdy kosą... jak pewien ktoś, trzeba ciąć samą przestrzeń…
297. [Słowo kluczowe [RienWeapon09Scythe] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +20%\n- 파괴되지 않고 적중 시, 반드시 크리티컬로 적중
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon09Scythe].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +20% damage\n- On Hit without Cracking, it hits a guaranteed Crit
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +20% obrażeń\n- Przy trafieniu bez Roztrzaskania trafia zawsze jako Cios Krytyczny
298. [Słowo kluczowe [RienWeapon09Scythe2phase] — nazwa] 낫으로… 누군가처럼 공간을 따라 베어내야 할 때는…
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].name
   kontekst: identyfikator tagu w tekstach: `[RienWeapon09Scythe2phase]`
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Słowo kluczowe [RienWeapon09Scythe2phase] — opis] - 참격 피해를 입힘\n- 해당 코인의 피해량 +30%\n- 파괴되지 않고 적중 시, 반드시 크리티컬로 적중
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals Slash damage\n- This Coin deals +30% damage\n- On Hit without Cracking, it hits a guaranteed Crit
   PL: - Zadaje obrażenia Cięcia\n- Ta Moneta zadaje +30% obrażeń\n- Przy trafieniu bez Roztrzaskania trafia zawsze jako Cios Krytyczny
300. [Słowo kluczowe [RienWeapon09Scythe2phase] — tekst klimatyczny] “낫은… 너무나 난해했지만, 푸른잔향이 싸우는 모습을 보니 감이 오더구나.”\n“그 후로도 한동안 지령이 내게 낫만을 쓰게 해서 어떤 무기보다 이 낫을 잘 다루고 좋아한단다.”\n“그리고 가장 잘 벨 수도 있지. 공간을 베는 기술에는 여러 가지가 있지만… 음. 이건 나중에 들려주는 게 좋겠어.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RienWeapon09Scythe2phase].flavor
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "The scythe... I could not for the life of me understand how to use this weapon until I saw that Blue Reverberation wield his own."\n"Even after I had observed him, the Prescript continued to give me no other weapons than the scythe for a while. Eventually, it became my favorite, most familiar, and sharpest weapon."\n"This weapon also cuts the best out of them all. While there are many techniques to cut through space itself— Hm. Perhaps this story is best saved for another time."
   PL: „Kosa... długo pozostawała dla mnie zagadką, ale gdy przyszło mi patrzeć, jak walczy Błękitny Pogłos, wszystko nagle stało się jasne.”\n„Potem Nakaz przez jakiś czas dawał mi tylko kosę — stała się moją ulubioną, najlepiej znaną bronią.”\n„I tnie z nich wszystkich najlepiej. Technik przecinania przestrzeni jest wiele... Hmm. Ta historia lepiej poczeka.”
301. [Słowo kluczowe [Ryoshu_RienBattle_1Phase] — nazwa] 케츠엔 [けつえん]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].name
   kontekst: identyfikator tagu w tekstach: `[Ryoshu_RienBattle_1Phase]`
   limit: do 40 znaków
   EN: Ketsuen [けつえん]
   PL: Ketsuen [けつえん]
302. [Słowo kluczowe [Ryoshu_RienBattle_1Phase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 료슈의 체력이 1 미만으로 내려가지 않음\n- 합 위력 +1, 공격 적중 시 피해량 +10%\n- 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Clash Power +1; On Hit, deal +10% damage\n- On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Dopóki w tej walce żyje co najmniej 1 inny sojusznik, HP Ryōshū nie spada poniżej 1\n- Moc Starcia +1; przy trafieniu zadaje +10% obrażeń\n- Po wygranym Starciu zyskuje 1 Zasób E.G.O z każdego z 3 najmniej posiadanych Grzechów\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu)\n- Wycofanie niemożliwe
303. [Słowo kluczowe [Ryoshu_RienBattle_1Phase] — tekst klimatyczny] 천살성도 - 아라야시키를 제어하기 위해서 만들어진 료슈만의 검집. 꺼지지 않는 불 속에서 단조된 아라야의 E.G.O.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_1Phase].flavor
   limit: do 190 znaków
   EN: Ryōshū's one and only scabbard, created to control the Tiansha Star's Blade - Arayashiki. This is Araya's E.G.O, forged in the eternal flame.
   PL: Jedyna pochwa Ryōshū, stworzona by kontrolować Ostrze Gwiazdy Tiansha - Arayashiki. To E.G.O Arayi, wykute w wiecznym ogniu.
304. [Słowo kluczowe [Ryoshu_RienBattle_2Phase] — nazwa] 렌케츠엔 [れんけつえん]
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].name
   kontekst: identyfikator tagu w tekstach: `[Ryoshu_RienBattle_2Phase]`
   limit: do 40 znaków
   EN: Renketsuen [れんけつえん]
   PL: Renketsuen [れんけつえん]
305. [Słowo kluczowe [Ryoshu_RienBattle_2Phase] — opis] - 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 료슈의 체력이 1 미만으로 내려가지 않음\n- 합 위력 +2, 공격 적중 시 피해량 +25%\n- 대상의 이글거리는 상처 1당\n· 공격 레벨 +1, 방어 레벨 +1\n· 공격 적중 시 피해량 +5% (최대 25%), 기본 E.G.O 스킬을 사용했으면 대신 피해량 +50% (최대 250%)\n- 합 승리 시, 수량이 가장 적은 E.G.O 자원 중 무작위 속성 자원 1개씩 총 3개 획득\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (전투당 횟수 제한 없음)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ryōshū's HP cannot drop below 1 as long as there is 1 or more surviving allies in this Encounter\n- Clash Power +2; On Hit, deal +25% damage\n- For every Sizzling Wound Stack on target:\n· Offense Level +1, Defense Level +1\n· Deal +5% damage On Hit (max 25%); if this unit used a Base E.G.O Skill, deal +50% damage per Stack instead (max 250%)\n- On Clash Win, gain 1 E.G.O resource for each of the 3 least-owned Affinities\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; and gain 1 Attack Power Up next turn (no activation cap)\n- Cannot Retreat
   PL: - Dopóki w tej walce żyje co najmniej 1 inny sojusznik, HP Ryōshū nie spada poniżej 1\n- Moc Starcia +2; przy trafieniu zadaje +25% obrażeń\n- Za każdy stos Kipiącej Rany celu:\n· Poziom Ataku +1, Poziom Obrony +1\n· Przy trafieniu zadaje +5% obrażeń (maks. 25%); jeżeli użyła podstawowej Umiejętności E.G.O, zamiast tego +50% za stos (maks. 250%)\n- Po wygranym Starciu zyskuje 1 Zasób E.G.O z każdego z 3 najmniej posiadanych Grzechów\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (bez limitu)\n- Wycofanie niemożliwe
306. [Słowo kluczowe [Ryoshu_RienBattle_2Phase] — tekst klimatyczny] 희미한 자아만이 남아있는 역설적인 E.G.O.\n오직 상대를 위하는 것처럼 보이더라도, 이는 절대적인 이타성이 아니다.\n타인의 삶이 가진 의미를 자신의 삶보다 우선 시하기 위해서는 절대적인 이기심이 필요하다.\n\n“엄마가 나를 잊지 않았으면 좋겠지만, 이대로 엄마를 잃는 게 나는 더 싫어.”\n“그러니까 나를 먼저 잊고, 자신을 더 소중히 해.”
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=Ryoshu_RienBattle_2Phase].flavor
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An E.G.O of paradoxical existence, for its ego is faint.\nDo not equate what appears to be utter devotion toward someone else with absolute altruism.\nOne must possess absolute egoism to put the significance of another's life before one's own.\n\n"I don't want mommy to forget about me, but... more than that, I don't wanna lose her."\n"So forget me for now, and take care of yourself."
   PL: Paradoksalne E.G.O, w którym zostaje ledwie ślad ego.\nNawet jeśli wygląda jak pełne poświęcenie dla kogoś, nie jest absolutnym altruizmem.\nŻeby stawiać znaczenie czyjegoś życia ponad własne, trzeba absolutnego egoizmu.\n\n„Chciałabym, żeby mama mnie nie zapomniała, ale... bardziej niż to, nie chcę ją stracić.”\n„Więc zapomnij najpierw o mnie i dbaj o siebie.”
307. [Słowo kluczowe [PainfulScar_Panic] — nazwa] 모조된 아비
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=PainfulScar_Panic].name
   kontekst: identyfikator tagu w tekstach: `[PainfulScar_Panic]`
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
308. [Słowo kluczowe [PainfulScar_Panic] — opis] - 패닉\n- 턴 시작 시, 화상 5, 화상 횟수 3, 출혈 5, 출혈 횟수 3 얻음\n- 수감자 료슈에게 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=PainfulScar_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 5 Burn, +3 Burn Count, 5 Bleed, and +3 Bleed Count\n- Take +20% damage from Sinner Ryōshū
   PL: - Panika\n- Na początku tury: 5 Podpalenia, 3 Licznika Podpalenia, 5 Krwawienia i 3 Licznika Krwawienia\n- Otrzymuje +20% obrażeń od Grzesznika Ryōshū
309. [Słowo kluczowe [PainfulScar_LowMorale] — nazwa] 모조된 아비
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=PainfulScar_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[PainfulScar_LowMorale]`
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Słowo kluczowe [PainfulScar_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 화상 5, 출혈 5 얻음\n- 수감자 료슈에게 받는 피해량 +10%
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=PainfulScar_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 5 Burn and 5 Bleed\n- Take +10% damage from Sinner Ryōshū
   PL: - Niskie Morale\n- Na początku tury zyskuje 5 Podpalenia i 5 Krwawienia\n- Otrzymuje +10% obrażeń od Grzesznika Ryōshū
311. [Słowo kluczowe [BlackNightmare] — nazwa] 지령 탐닉
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BlackNightmare].name
   kontekst: identyfikator tagu w tekstach: `[BlackNightmare]`
   limit: do 40 znaków
   EN: Indulgence in Prescripts
   PL: Indulgencja w Nakazach
312. [Słowo kluczowe [BlackNightmare] — opis] - 부여하는 침잠 위력과 횟수 +2\n- 턴 종료 시, 사라지고 (이번 턴에 합 패배한 스킬 수 x 5)만큼 카르마 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BlackNightmare].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Inflict +2 more Sinking Potency and Count\n- Expires at Turn End; then, gain (number of Skills that lost a Clash this turn x 5) Karmic Consequence
   PL: - Nakłada +2 więcej Siły i Licznika Zatonięcia\n- Znika na koniec tury, a następnie zyskuje (liczba Umiejętności, które przegrały Starcie w tej turze x 5) Karma
313. [Słowo kluczowe [BlackNightmare] — tekst klimatyczny] 겉으로는 기꺼이 지령을 수행하는 듯 보이나, 그 이면에는 지령에 대한 원망 또한 엿보인다.\n그러나 모든 고통과 쾌락을 지령이라는 가면을 쓰고 행할 수 있었기에, 그 본망은 지령에 대한 감사함으로 귀결된다.
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=BlackNightmare].flavor
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The acceptance of the Prescripts is apparent in his execution of them; yet, on the other side of the mask, one may glimpse a hint of resentment for them.\nHowever, as he could indulge in all the suffering and pleasures of the world behind the mask of "Prescripts," his true immanent yearning is concluded by that of gratitude.
   PL: Z zewnątrz wykonuje Nakazy chętnie, lecz za maską prześwituje do nich uraza.\nPonieważ jednak mógł oddawać się całemu cierpieniu i przyjemnościom świata za maską „Nakazów”, jego ukryta tęsknota kończy się wdzięcznością.
314. [Słowo kluczowe [RyoshuParrySojiWe] — nazwa] 붉은 실
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParrySojiWe]`
   limit: do 40 znaków
   EN: Red String
   PL: Czerwona Nić
315. [Słowo kluczowe [RyoshuParrySojiWe] — opis] - 스킬 슬롯 수 +3\n소지 아비에게 가하는 피해량 +50%\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +3\n- Deal +50% damage to The Pinky Nursefather\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +3\nZadaje +50% obrażeń Ojcu Małego Palca\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
316. [Słowo kluczowe [RyoshuParrySojiWe] — tekst klimatyczny] ‘이 가느다란 실 하나만이 너와 나를 이어주고 있다면, 나는 온 힘을 다해 이 실을 놓지 않을 거다.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiWe].flavor
   limit: do 140 znaków
   EN: 'If this single thread is the only thing that connects you and me, I will cling to it with all my being.'
   PL: „Jeżeli ta jedna cienka nić łączy mnie z tobą, będę się jej kurczowo trzymać całym sobą.”
317. [Słowo kluczowe [RyoshuParrySojiThey] — nazwa] 붉은 실
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParrySojiThey]`
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Słowo kluczowe [RyoshuParrySojiThey] — opis] - 모든 스킬 코인이 파괴 불가 코인으로 변경됨\n- 최종 위력 +4
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Converts all Skill Coins into Unbreakable Coins\n- Final Power +4
   PL: - Wszystkie Monety Umiejętności stają się Niezniszczalnymi Monetami\n- Moc Końcowa +4
319. [Słowo kluczowe [RyoshuParrySojiThey] — tekst klimatyczny] ‘당신과 나는 이 실 때문에 결국 만나. 피하고 싶어도 계속 마주하게 돼. 이 실은 도무지 끊어지질 않아.’
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParrySojiThey].flavor
   limit: do 160 znaków
   EN: 'Escape as we might, this stubborn thread will force us to cross paths still. It refuses to break, no matter what I do...'
   PL: „Dzięki tej nici w końcu się spotkamy. Choć byśmy chcieli uniknąć, wciąż się spotkamy. Ta nić nie chce się przeciąć.”
320. [Słowo kluczowe [CriticalDamageUp] — nazwa] 크리티컬 피해량 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CriticalDamageUp].name
   kontekst: identyfikator tagu w tekstach: `[CriticalDamageUp]`
   limit: do 40 znaków
   EN: Crit DMG Up
   PL: Wzrost Obrażeń Krytycznych
321. [Słowo kluczowe [CriticalDamageUp] — opis] 한 턴 동안 스킬로 가하는 크리티컬 피해량이 수치당 10% 증가
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=CriticalDamageUp].desc
   limit: do 120 znaków
   EN: For this turn: Deal +10% damage on Critical Hit for every Stack
   PL: W tej turze obrażenia Krytyczne rosną o 10% za każdy stos
322. [Słowo kluczowe [KAA1C9ActivateEffect] — nazwa] K사 앰플 사용
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KAA1C9ActivateEffect].name
   kontekst: identyfikator tagu w tekstach: `[KAA1C9ActivateEffect]`
   limit: do 40 znaków
   EN: K Corp. Ampule Used
   PL: Użyta Ampułka Korporacji K
323. [Słowo kluczowe [KAA1C9ActivateEffect] — opis] 사용된 K사 앰플
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=KAA1C9ActivateEffect].desc
   limit: do 120 znaków
   EN: Used K Corp. Ampule
   PL: Użyta Ampułka Korporacji K
324. [Słowo kluczowe [RyoshuParryIndexFingerWe] — nazwa] 붉은 실
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParryIndexFingerWe].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParryIndexFingerWe]`
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Słowo kluczowe [RyoshuParryIndexFingerThey] — nazwa] 붉은 실
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=RyoshuParryIndexFingerThey].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParryIndexFingerThey]`
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-cultivation
- plik gry: `BattleKeywords-cultivation.json` (opisy wyświetlane w dymkach pomocy podczas walki)

326. [Słowo kluczowe [LegStrengthHorse] — nazwa] 각력【오】
   źródło: BattleKeywords-cultivation.json :: dataList[id=LegStrengthHorse].name
   kontekst: identyfikator tagu w tekstach: `[LegStrengthHorse]`
   limit: do 40 znaków
   EN: Strider【Wu】
   PL: Siła Nóg 【Wu】
327. [Słowo kluczowe [LegStrengthHorse] — opis] - 최댓값: 3\n- 턴 종료 시 다음 턴에 신속 2, 방어 레벨 증가를 (수치 x 2)만큼 얻음\n- 스킬 적중시 진동 위력을 수치만큼 추가로 부여 (턴 당 최대 6)
   źródło: BattleKeywords-cultivation.json :: dataList[id=LegStrengthHorse].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Haste and (Stack x 2) Defense Level Up next turn\n- On Hit with a Skill, inflict additional Tremor Potency equal to Stack (max 6 per turn)
   PL: - Maks. stosów: 3\n- Na koniec tury zyskuje 2 Pośpiechu i (stosy x 2) Wzrost Poziomu Obrony w następnej turze\n- Umiejętności nakładają dodatkowo Siłę Wstrząsu równą stosom przy trafieniu (maks. 6 na turę)
328. [Słowo kluczowe [ConcussionWei] — nazwa] 뇌진탕
   źródło: BattleKeywords-cultivation.json :: dataList[id=ConcussionWei].name
   kontekst: identyfikator tagu w tekstach: `[ConcussionWei]`
   limit: do 40 znaków
   EN: Concussion
   PL: Wstrząśnienie Mózgu
329. [Słowo kluczowe [ConcussionWei] — opis] - 최댓값: 3\n- 피격 시 피해량을 수치 당 30% 추가로 받음 (최대 90%)\n- 이 효과가 있는 동안 파열 피해와 진동 폭발로 인한 흐트러짐 손상을 1.5배로 받음. (소수점 버림)\n- 최대 수치에 도달했다면 턴 종료시 전부 소모되고 다음 턴 강제 흐트러짐
   źródło: BattleKeywords-cultivation.json :: dataList[id=ConcussionWei].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When hit, take +30% damage for every Stack (max 90%)\n- Multiply the amount of Stagger Threshold raised by Tremor Burst and Rupture damage dealt against this unit by 1.5 (rounded down)\n- At max Stack, consume all of it at Turn End and enter forced Stagger state next turn
   PL: - Maks. stosów: 3\n- Przy trafieniu otrzymuje +30% obrażeń za każdy stos (maks. 90%)\n- Podczas tego efektu otrzymuje x1,5 podniesienia Progu Oszołomienia od Wyładowania Wstrząsu i obrażeń Rozdarcia (zaokrąglone w dół)\n- Przy Maks. stosów zużywa je wszystkie na koniec tury i przechodzi w wymuszone Oszołomienie w następnej turze
330. [Słowo kluczowe [SweptAwayWei] — nazwa] 휩쓸림
   źródło: BattleKeywords-cultivation.json :: dataList[id=SweptAwayWei].name
   kontekst: identyfikator tagu w tekstach: `[SweptAwayWei]`
   limit: do 40 znaków
   EN: Galestruck
   PL: Porwanie Wichrem
331. [Słowo kluczowe [SweptAwayWei] — opis] - 최댓값: 10\n- 진동 폭발로 인한 흐트러짐 손상을 2배로 받음.\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-cultivation.json :: dataList[id=SweptAwayWei].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Double the amount of Stagger Threshold raised on this unit due to Tremor Burst\n- Reduced by 1 at Turn End
   PL: - Maks. stosów: 10\n- Podwaja podniesienie Progu Oszołomienia od Wyładowania Wstrząsu\n- Na koniec tury maleje o 1
332. [Słowo kluczowe [ReboundWei] — nazwa] 반동
   źródło: BattleKeywords-cultivation.json :: dataList[id=ReboundWei].name
   kontekst: identyfikator tagu w tekstach: `[ReboundWei]`
   limit: do 40 znaków
   EN: Recoiling
   PL: Odrzut
333. [Słowo kluczowe [ReboundWei] — opis] - 최댓값: 5
   źródło: BattleKeywords-cultivation.json :: dataList[id=ReboundWei].desc
   limit: do 120 znaków
   EN: - Max Stack: 5
   PL: - Maks. stosów: 5
334. [Słowo kluczowe [ReboundWei] — tekst klimatyczny] 잘못된 대상에게 진동 폭발을 입힘으로 생긴 반동이다.
   źródło: BattleKeywords-cultivation.json :: dataList[id=ReboundWei].flavor
   limit: do 140 znaków
   EN: Triggered Tremor Burst against the wrong target. Every action has an equal and opposite reaction, after all.
   PL: To odrzut po wywołaniu Wyładowania Wstrząsu na niewłaściwym celu. Każde działanie ma równą i przeciwną reakcję.
335. [Słowo kluczowe [SipOfAlcoholJin] — nazwa] 한 모금(眞)
   źródło: BattleKeywords-cultivation.json :: dataList[id=SipOfAlcoholJin].name
   kontekst: identyfikator tagu w tekstach: `[SipOfAlcoholJin]`
   limit: do 40 znaków
   EN: Swig (眞)
   PL: Łyczek (眞)
336. [Słowo kluczowe [SipOfAlcoholJin] — opis] - 최대값: 5\n- 턴 종료 시 다음 턴에 (수치 x 2) 만큼 호흡 위력 획득\n- 턴 종료 시 다음 턴에 (수치 / 2) 만큼 신속 획득 (소수점 버림)\n- 턴 종료 시 수치가 3 이상이면, 전체 체력의 1.5%만큼 회복 (본체, 부위)
   źródło: BattleKeywords-cultivation.json :: dataList[id=SipOfAlcoholJin].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn End: gain (Stack x 2) Poise Potency next turn\n- Turn End: gain (Stack / 2) Haste next turn (rounded down)\n- Turn End: at 3+ Stack, heal 1.5% HP (both Core & Part)
   PL: - Maks. stosów: 5\n- Na koniec tury zyskuje (stosy x 2) Siły Oddechu w następnej turze\n- Na koniec tury zyskuje (stosy / 2) Pośpiechu w następnej turze (zaokrąglone w dół)\n- Na koniec tury przy 3+ stosach leczy 1,5% HP (korpus i części)
337. [Słowo kluczowe [DrunkBlood] — nazwa] 혈주(血注)
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkBlood].name
   kontekst: identyfikator tagu w tekstach: `[DrunkBlood]`
   limit: do 40 znaków
   EN: Bloodpour (血注)
   PL: Rzut Krwi (血注)
338. [Słowo kluczowe [DrunkBlood] — opis] - 최댓값: 5\n- 특수 출혈\n- 공격 스킬의 코인 판정 시, 수치만큼 고정 체력 피해를 받음
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkBlood].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Unique Bleed\n- When tossing an attack Coin, take fixed damage by the effect’s Stack.
   PL: - Maks. stosów: 5\n- Specjalne Krwawienie\n- Przy rzucie Monety Umiejętności ataku otrzymuje obrażenia stałe równe stosom tego efektu
339. [Słowo kluczowe [DrunkAwakening] — nazwa] 정신 각성
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkAwakening].name
   kontekst: identyfikator tagu w tekstach: `[DrunkAwakening]`
   limit: do 40 znaków
   EN: Mental Awakening
   PL: Przebudzenie Umysłu
340. [Słowo kluczowe [DrunkAwakening] — opis] - 최댓값: 1\n- 이 효과를 지니는 동안 최종 위력 4 증가, 받는 피해량 30% 증가\n- 출혈 위력 부여 코인 적중 시 추가로 출혈을 2 부여함 (턴 당 최대 10)\n- 자신에게 호흡이 있으면 크리티컬 피해량 +50%
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkAwakening].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- As long as this unit has this effect, gain 4 Final Power and take +30% damage\n- On Hit with a Coin that inflicts Bleed Potency: inflict +2 more Bleed On Hit (max 10 per turn)\n- If this unit has Poise, deal +50% damage
   PL: - Maks. stosów: 1\n- Dopóki posiada ten efekt: Moc Końcowa +4 i otrzymuje +30% obrażeń\n- Przy trafieniu Monetą nakładającą Siłę Krwawienia nakłada dodatkowo 2 Krwawienia (maks. 10 na turę)\n- Jeżeli posiada Oddech, zadaje +50% obrażeń Krytycznych
341. [Słowo kluczowe [RunawayHorseWei_LowMorale] — nazwa] 고삐 풀린 말
   źródło: BattleKeywords-cultivation.json :: dataList[id=RunawayHorseWei_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[RunawayHorseWei_LowMorale]`
   limit: do 40 znaków
   EN: Unbridled Steed
   PL: Rumak bez Wędzidła
342. [Słowo kluczowe [RunawayHorseWei_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 2, 취약 1을 얻음
   źródło: BattleKeywords-cultivation.json :: dataList[id=RunawayHorseWei_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Offense Level Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Wrażliwości
343. [Słowo kluczowe [RunawayHorseWei_Panic] — nazwa] 고삐 풀린 말
   źródło: BattleKeywords-cultivation.json :: dataList[id=RunawayHorseWei_Panic].name
   kontekst: identyfikator tagu w tekstach: `[RunawayHorseWei_Panic]`
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Słowo kluczowe [RunawayHorseWei_Panic] — opis] - 패닉\n- 턴 시작 시, 최대 속도 1 증가, 공격 레벨 증가 2, 취약 2를 얻음
   źródło: BattleKeywords-cultivation.json :: dataList[id=RunawayHorseWei_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 1 Max Speed, 2 Offense Level Up, and 2 Fragile
   PL: - Panika\n- Zyskuje 1 Maks. Szybkość, 2 Wzrostu Poziomu Ataku i 2 Wrażliwości
345. [Słowo kluczowe [DrunkDrifter_LowMorale] — nazwa] 취수야객
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkDrifter_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DrunkDrifter_LowMorale]`
   limit: do 50 znaków
   EN: Night Drifter of the Drunken Palm
   PL: Pijanica Nocny Wędrowiec
346. [Słowo kluczowe [DrunkDrifter_LowMorale] — opis] - 사기 저하\n- 가시춘에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkDrifter_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +10% damage from Jia Xichun; deal +30% damage with Counterattacks
   PL: - Niskie Morale\n- Otrzymuje +10% obrażeń od Jia Xichun; zadaje +30% obrażeń Kontrą
347. [Słowo kluczowe [DrunkDrifter_Panic] — nazwa] 취수야객
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkDrifter_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DrunkDrifter_Panic]`
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Słowo kluczowe [DrunkDrifter_Panic] — opis] - 패닉\n- 최종 위력 1 증가, 가시춘에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: BattleKeywords-cultivation.json :: dataList[id=DrunkDrifter_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Final Power +1; take +20% damage from Jia Xichun; deal +50% damage with Counterattacks
   PL: - Panika\n- Moc Końcowa +1; otrzymuje +20% obrażeń od Jia Xichun; zadaje +50% obrażeń Kontrą
349. [Słowo kluczowe [DarkBeastSnake_LowMorale] — nazwa] 암완
   źródło: BattleKeywords-cultivation.json :: dataList[id=DarkBeastSnake_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DarkBeastSnake_LowMorale]`
   limit: do 40 znaków
   EN: Shadow Arm
   PL: Ciemna Wąż-Ręka
350. [Słowo kluczowe [DarkBeastSnake_LowMorale] — opis] - 사기 저하\n- 합 위력 -1, 받는 피해량 -10%
   źródło: BattleKeywords-cultivation.json :: dataList[id=DarkBeastSnake_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1; take -10% damage
   PL: - Niskie Morale\n- Moc Starcia -1; otrzymuje -10% obrażeń
351. [Słowo kluczowe [DarkBeastSnake_Panic] — nazwa] 암완
   źródło: BattleKeywords-cultivation.json :: dataList[id=DarkBeastSnake_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DarkBeastSnake_Panic]`
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Słowo kluczowe [DarkBeastSnake_Panic] — opis] - 패닉\n- 합 위력 -2, 받는 피해량 -20%
   źródło: BattleKeywords-cultivation.json :: dataList[id=DarkBeastSnake_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2; take -20% damage
   PL: - Panika\n- Moc Starcia -2; otrzymuje -20% obrażeń
353. [Słowo kluczowe [NightDrifterGuilty] — nazwa] 미약한 죄책감
   źródło: BattleKeywords-cultivation.json :: dataList[id=NightDrifterGuilty].name
   kontekst: identyfikator tagu w tekstach: `[NightDrifterGuilty]`
   limit: do 40 znaków
   EN: Faint Guilt
   PL: Słabe Poczucie Winy
354. [Słowo kluczowe [NightDrifterGuilty] — opis] - 공격 레벨 15 감소\n- 방어 레벨 15 감소
   źródło: BattleKeywords-cultivation.json :: dataList[id=NightDrifterGuilty].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -15\n- Defense Level -15
   PL: - Poziom Ataku -15\n- Poziom Obrony -15
355. [Słowo kluczowe [StudyStatSinclair] — nazwa] 알에서 나오기 위한 몸부림
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair]`
   limit: do 40 znaków
   EN: Thrashing to Hatch
   PL: Tęsknota za Wykluciem
356. [Słowo kluczowe [StudyStatSinclair] — opis] - 수업으로 얻는 인/지/용의 합에 비례하여 효과 강화
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair].desc
   limit: do 120 znaków
   EN: - Enhance effects based on the sum of Zhi, Yong, and Ren gained from classes
   PL: - Wzmacnia efekty zależnie od sumy Zhi, Yong i Ren zdobytych na zajęciach
357. [Słowo kluczowe [StudyStatSinclair_A] — nazwa] 알에서 나오기 위한 몸부림 Ⅰ
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_A].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair_A]`
   limit: do 40 znaków
   EN: Thrashing to Hatch Ⅰ
   PL: Tęsknota za Wykluciem Ⅰ
358. [Słowo kluczowe [StudyStatSinclair_A] — opis] - 매 턴 정신력 3 회복\n- 속도 최소값, 최대값 1 증가\n- 공격 레벨 2 증가\n- 방어 레벨 2 증가
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_A].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 3 SP every turn\n- Gain 1 Min & Max Speed\n- Gain 2 Offense Levels\n- Gain 2 Defense Levels
   PL: - Co turę odzyskuje 3 Poczytalności\n- Min. i Maks. Szybkość +1\n- Poziom Ataku +2\n- Poziom Obrony +2
359. [Słowo kluczowe [StudyStatSinclair_B] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅠ
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_B].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair_B]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅠ
   PL: Tęsknota za Wykluciem Ⅱ
360. [Słowo kluczowe [StudyStatSinclair_B] — opis] - 매 턴 정신력 5 회복\n- 속도 최소값, 최대값 1 증가,\n- 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 공격 레벨 2 증가\n- 방어 레벨 2 증가
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_B].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 5 SP every turn\n- Gain 1 Min & Max Speed\n- Gain 1 Attack Power Up and 1 Protection every turn\n- Gain 2 Offense Levels\n- Gain 2 Defense Levels
   PL: - Co turę odzyskuje 5 Poczytalności\n- Min. i Maks. Szybkość +1,\n- Co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Poziom Ataku +2\n- Poziom Obrony +2
361. [Słowo kluczowe [StudyStatSinclair_C] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅠⅠ
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_C].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair_C]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅠⅠ
   PL: Tęsknota za Wykluciem Ⅲ
362. [Słowo kluczowe [StudyStatSinclair_C] — opis] - 매 턴 정신력 5 회복\n- 속도 최소값, 최대값 1 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 공격 레벨 3 증가\n- 방어 레벨 3 증가
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_C].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 5 SP every turn\n- Gain 1 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Gain 3 Offense Levels\n- Gain 3 Defense Levels
   PL: - Co turę odzyskuje 5 Poczytalności\n- Min. i Maks. Szybkość +1; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Poziom Ataku +3\n- Poziom Obrony +3
363. [Słowo kluczowe [StudyStatSinclair_D] — nazwa] 알에서 나오기 위한 몸부림 ⅠⅤ
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_D].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair_D]`
   limit: do 40 znaków
   EN: Thrashing to Hatch ⅠⅤ
   PL: Tęsknota za Wykluciem Ⅳ
364. [Słowo kluczowe [StudyStatSinclair_D] — opis] - 매 턴 정신력 10 회복\n- 속도 최소값, 최대값 1 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 공격 레벨 4 증가\n- 방어 레벨 4 증가
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_D].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 10 SP every turn\n- Gain 1 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Gain 4 Offense Levels\n- Gain 4 Defense Levels
   PL: - Co turę odzyskuje 10 Poczytalności\n- Min. i Maks. Szybkość +1; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Poziom Ataku +4\n- Poziom Obrony +4
365. [Słowo kluczowe [StudyStatSinclair_E] — nazwa] 알에서 나오기 위한 몸부림 Ⅴ
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_E].name
   kontekst: identyfikator tagu w tekstach: `[StudyStatSinclair_E]`
   limit: do 40 znaków
   EN: Thrashing to Hatch Ⅴ
   PL: Tęsknota za Wykluciem Ⅴ
366. [Słowo kluczowe [StudyStatSinclair_E] — opis] - 매 턴 정신력 15 회복\n- 속도 최소값, 최대값 2 증가, 매 턴 공격 위력 증가 1, 보호 1 얻음\n- 기본 스킬 합 위력 1 증가\n- 기본 스킬 코인 위력 1 증가\n- 공격 레벨 5 증가\n- 방어 레벨 5 증가
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudyStatSinclair_E].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 15 SP every turn\n- Gain 2 Min & Max Speed; gain 1 Attack Power Up and 1 Protection every turn\n- Base Skills gain 1 Clash Power\n- Base Skills gain 1 Coin Power\n- Gain 5 Offense Levels\n- Gain 5 Defense Levels
   PL: - Co turę odzyskuje 15 Poczytalności\n- Min. i Maks. Szybkość +2; co turę zyskuje 1 Wzrost Mocy Ataku i 1 Ochrony\n- Podstawowe Umiejętności zyskują 1 Moc Starcia\n- Podstawowe Umiejętności zyskują 1 Moc Monety\n- Poziom Ataku +5\n- Poziom Obrony +5
367. [Słowo kluczowe [StudySignSinclair] — nazwa] 어느 표지
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudySignSinclair].name
   kontekst: identyfikator tagu w tekstach: `[StudySignSinclair]`
   limit: do 40 znaków
   EN: A Sign
   PL: Pewien Znak
368. [Słowo kluczowe [StudySignSinclair] — opis] - 다음 턴 정신력 30 회복\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudySignSinclair].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Heal 30 SP next turn\n- Turn End: Expires
   PL: - Odzyskuje 30 Poczytalności w następnej turze\n- Znika na koniec tury
369. [Słowo kluczowe [StudySignSinclair] — tekst klimatyczny] 태어나려는 자는 한 세계를 파괴해야만 한다.
   źródło: BattleKeywords-cultivation.json :: dataList[id=StudySignSinclair].flavor
   limit: do 120 znaków
   EN: One who seeks to be born must first destroy a world.
   PL: Ten, kto pragnie się narodzić, musi najpierw zniszczyć świat.
370. [Słowo kluczowe [CrazyWei] — nazwa] 광폭화
   źródło: BattleKeywords-cultivation.json :: dataList[id=CrazyWei].name
   kontekst: identyfikator tagu w tekstach: `[CrazyWei]`
   limit: do 40 znaków
   EN: Berserking
   PL: Szalone Kwitnienie
371. [Słowo kluczowe [CrazyWei] — opis] - 공격 레벨 15 감소\n- 방어 레벨 15 감소\n\n- 턴 종료 시 각력【오】 버프로 방어 레벨을 얻지 않고, 공격 레벨 증가를 각력【오】 수치 만큼 얻음
   źródło: BattleKeywords-cultivation.json :: dataList[id=CrazyWei].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 15 Offense Level\n- Lose 15 Defense Level\n\n- Turn End: does not gain Defense Level from Strider【Wu】; instead, gain Offense Level Up equal to Strider【Wu】 Stack
   PL: - Poziom Ataku -15\n- Poziom Obrony -15\n\n- Na koniec tury nie zyskuje Poziomu Obrony z Siły Nóg 【Wu】; zamiast tego zyskuje Wzrost Poziomu Ataku równy stosom Siły Nóg 【Wu】
372. [Słowo kluczowe [CrazyWei] — tekst klimatyczny] “…아가씨를 해하려는 모든 것들을… 짓밟아 죽이리…”
   źródło: BattleKeywords-cultivation.json :: dataList[id=CrazyWei].flavor
   limit: do 120 znaków
   EN: "I'll trample anyone who dares to hurt my lady... I'll trample them to death... "
   PL: „...Wszystko, co ośmieli się skrzywdzić moją panią... zdeptam na śmierć…”
373. [Słowo kluczowe [SnakePoisonJinWeak] — nazwa] 뱀 독
   źródło: BattleKeywords-cultivation.json :: dataList[id=SnakePoisonJinWeak].name
   kontekst: identyfikator tagu w tekstach: `[SnakePoisonJinWeak]`
   limit: do 40 znaków
   EN: Snake Venom
   PL: Jad Węża
374. [Słowo kluczowe [SnakePoisonJinWeak] — opis] - 공격 레벨 1 감소\n- 방어 레벨 1 감소
   źródło: BattleKeywords-cultivation.json :: dataList[id=SnakePoisonJinWeak].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -1\n- Defense Level -1
   PL: - Poziom Ataku -1\n- Poziom Obrony -1
375. [Słowo kluczowe [SnakePoisonJin] — nazwa] 퍼지는 뱀 독
   źródło: BattleKeywords-cultivation.json :: dataList[id=SnakePoisonJin].name
   kontekst: identyfikator tagu w tekstach: `[SnakePoisonJin]`
   limit: do 40 znaków
   EN: Spreading Snake Venom
   PL: Rozprzestrzeniający się Jad Węża
376. [Słowo kluczowe [SnakePoisonJin] — opis] - 공격 레벨 7 감소\n- 방어 레벨 7 감소\n합 진행 시 최대 체력의 1%만큼 피해를 받음
   źródło: BattleKeywords-cultivation.json :: dataList[id=SnakePoisonJin].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -7\n- Defense Level -7\nTake 1% HP damage with every Clash
   PL: - Poziom Ataku -7\n- Poziom Obrony -7\nOtrzymuje 1% HP obrażeń przy każdym Starciu

## Słowa kluczowe bitwy — BattleKeywords-exme
- plik gry: `BattleKeywords-exme.json` (opisy wyświetlane w dymkach pomocy podczas walki)

377. [Słowo kluczowe [ScratchesHurt] — nazwa] 찢긴 상처
   źródło: BattleKeywords-exme.json :: dataList[id=ScratchesHurt].name
   kontekst: identyfikator tagu w tekstach: `[ScratchesHurt]`
   limit: do 40 znaków
   EN: Avulsion Wound
   PL: Rozdarta Rana
378. [Słowo kluczowe [ScratchesHurt] — opis] - 최댓값: 3\n- 턴 시작 시 수치 1당, 출혈 2 얻음\n• 수치가 최댓값이면, 출혈 횟수 1 추가 증가\n- 턴 종료 시 다음 턴에 수치 만큼 속박 1 얻음\n• 수치가 최댓값이면, 다음 턴에 공격 위력 감소 1 추가 얻음\n- 이번 턴 동안 크리티컬 피해를 받지 않았다면, 턴 종료 시 1 감소
   źródło: BattleKeywords-exme.json :: dataList[id=ScratchesHurt].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Gain 2 Bleed for every Stack\n• At max Stack, gain +1 Bleed Count\n- Turn End: Gain Bind equal to Stack next turn\n• At Max Stack, gain 1 Attack Power Down as well next turn\n- Turn End: If this unit did not take any Critical Hit this turn, lose 1 Stack
   PL: - Maks. stosów: 3\n- Na początku tury zyskuje 2 Krwawienia za każdy stos\n• Przy Maks. stosów zyskuje dodatkowo +1 Licznika Krwawienia\n- Na koniec tury zyskuje Spętań równy stosom w następnej turze\n• Przy Maks. stosów zyskuje dodatkowo 1 Spadek Mocy Ataku w następnej turze\n- Na koniec tury traci 1 stos, jeżeli w tej turze nie otrzymał Ciosu Krytycznego
379. [Słowo kluczowe [TiedRope] — nazwa] 포박
   źródło: BattleKeywords-exme.json :: dataList[id=TiedRope].name
   kontekst: identyfikator tagu w tekstach: `[TiedRope]`
   limit: do 40 znaków
   EN: Trussed
   PL: Skuty
380. [Słowo kluczowe [TiedRope] — opis] - 기본값: 3\n- 속도가 1로 고정됨\n- 기본 스킬의 코인 위력이 0으로 고정됨\n- 턴 종료 시 1 감소\n- 자신에게 효과를 부여한 대상의 ‘압송 채비’ 버프가 소멸하면, 해당 효과 함께 소멸
   źródło: BattleKeywords-exme.json :: dataList[id=TiedRope].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Fix this unit's Speed to 1\n- Fix this unit's Base Skills' Coin Power to 0\n- Turn End: Lose 1 Stack\n- If the "Prisoner Transport Arrangements" buff on the inflicter expires, this effect expires as well
   PL: - Wartość bazowa: 3\n- Szybkość zostaje zablokowana na 1\n- Moc Monet podstawowych Umiejętności zostaje zablokowana na 0\n- Na koniec tury maleje o 1\n- Gdy na nałożycielu wygaśnie buff „Przygotowania Konwoju”, ten efekt znika razem z nim
381. [Słowo kluczowe [TiedRope] — tekst klimatyczny] 아랫것이 아랫것을 잡아 위로 올린다.
   źródło: BattleKeywords-exme.json :: dataList[id=TiedRope].flavor
   limit: do 120 znaków
   EN: Look how the baseborn hunt the other baseborn to serve them up to the powers that be.
   PL: Patrz, jak nędzny łapie nędznego, by podnieść go tym, którzy stoją wyżej.
382. [Słowo kluczowe [TiedWithRope] — nazwa] 압송 채비
   źródło: BattleKeywords-exme.json :: dataList[id=TiedWithRope].name
   kontekst: identyfikator tagu w tekstach: `[TiedWithRope]`
   limit: do 50 znaków
   EN: Prisoner Transport Arrangements
   PL: Przygotowania Konwoju
383. [Słowo kluczowe [TiedWithRope] — opis] - 기본값: 1\n- 속도가 1로 고정됨\n- 자신이 대상에게 부여한 포박 효과가 소멸하거나, 자신(추노꾼)이 사망 혹은 흐트러짐 상태가 되면, 버프 소멸\n- 자신이 포박을 부여한 대상이 이번 턴에 사망한 경우, ‘압송 채비’ 버프 소멸
   źródło: BattleKeywords-exme.json :: dataList[id=TiedWithRope].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 1\n- Fix this unit's Speed to 1\n- If the Trussed effect this unit inflicted on target expires, or if this unit is defeated or Staggered, lose this effect\n- If the target this unit inflicted "Trussed" on is defeated this turn, lose the "Prisoner Transport Arrangements" effect
   PL: - Wartość bazowa: 1\n- Szybkość zostaje zablokowana na 1\n- Gdy nałożone przez tę jednostkę Skucie wygaśnie lub gdy nałożyciel (łowca) ginie albo zostaje oszołomiony, buff znika\n- Jeżeli cel ze Skuciem ginie w tej turze, buff „Przygotowania Konwoju” znika
384. [Słowo kluczowe [RegretSCorp] — nazwa] 지끈거리는 기억
   źródło: BattleKeywords-exme.json :: dataList[id=RegretSCorp].name
   kontekst: identyfikator tagu w tekstach: `[RegretSCorp]`
   limit: do 40 znaków
   EN: Headsplitting Memory
   PL: Kolące w Skroniach Wspomnienie
385. [Słowo kluczowe [RegretSCorp] — opis] - 최댓값: 1\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 다음 턴에 (현재 턴 수 / 4)만큼 합 위력 증가 얻음 (소수점 버림, 최대 3)\n- 턴 종료 시 소멸
   źródło: BattleKeywords-exme.json :: dataList[id=RegretSCorp].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Turn End: Gain 1 Bind next turn\n- Turn End: Gain (current turn count / 4) Clash Power Up (rounded down, max 3)\n- Expires at Turn End
   PL: - Maks. stosów: 1\n- Na koniec tury zyskuje 1 Spętanie w następnej turze\n- Na koniec tury zyskuje (liczba tur / 4) Wzrostu Mocy Starcia (zaokrąglone w dół, maks. 3)\n- Znika na koniec tury
386. [Słowo kluczowe [TakePicture] — nazwa] 정보 취득
   źródło: BattleKeywords-exme.json :: dataList[id=TakePicture].name
   kontekst: identyfikator tagu w tekstach: `[TakePicture]`
   limit: do 40 znaków
   EN: Intelligence Gathering
   PL: Zbieranie Informacji
387. [Słowo kluczowe [TakePicture] — opis] - 촬영된 스킬 등급과 동일한 등급의 스킬 사용 시 합 위력 -5\n(※수비 스킬, E.G.O 스킬은 별개로 구분)\n- 턴 종료 시 소멸
   źródło: BattleKeywords-exme.json :: dataList[id=TakePicture].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When using a Skill of identical rank to the Skill photographed, Clash Power -5\n(※ Defense Skills and E.G.O Skills are counted separately)\n- Expires at Turn End
   PL: - Przy użyciu Umiejętności tego samego stopnia co sfotografowana Umiejętność Moc Starcia -5\n(※ Umiejętności obrony i E.G.O liczone osobno)\n- Znika na koniec tury
388. [Słowo kluczowe [LensmanNail] — nazwa] 고정 못
   źródło: BattleKeywords-exme.json :: dataList[id=LensmanNail].name
   kontekst: identyfikator tagu w tekstach: `[LensmanNail]`
   limit: do 40 znaków
   EN: Pinning Nail
   PL: Przypinający Gwóźdź
389. [Słowo kluczowe [LensmanNail] — opis] - 최댓값 : 10\n- 턴 시작 시 속박 수치 2당, 공격 레벨 감소 1 얻음 (최대 3)\n- 턴 시작 시 수치 만큼 출혈 얻음\n- 진동 폭발 시 수치 만큼 출혈 횟수 증가 (턴당 1회)\n- 턴 종료 시 수치 만큼 다음 턴에 속박을 얻고 (최대 6), 수치 1 감소
   źródło: BattleKeywords-exme.json :: dataList[id=LensmanNail].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Turn Start: Gain 1 Offense Level Down for every 2 Bind (max 3)\n- Turn Start: Gain Bleed equal to Stack\n- On Tremor Burst, gain Bleed Count equal to Stack (once per turn)\n- Turn End: Gain Bind equal to Stack next turn (max 6), then lose 1 Stack
   PL: - Maks. stosów: 10\n- Na początku tury zyskuje 1 Spadek Poziomu Ataku za każde 2 Spętań (maks. 3)\n- Na początku tury zyskuje Krwawienie równe stosom\n- Przy Wyładowaniu Wstrząsu zyskuje Licznik Krwawienia równy stosom (1 raz na turę)\n- Na koniec tury zyskuje Spętań równych stosom w następnej turze (maks. 6), a wartość maleje o 1
390. [Słowo kluczowe [PhotoTransition] — nazwa] 기억 전환
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransition].name
   kontekst: identyfikator tagu w tekstach: `[PhotoTransition]`
   limit: do 40 znaków
   EN: Memory Transition
   PL: Przełączanie Wspomnień
391. [Słowo kluczowe [PhotoTransition] — opis] - 기본값 : 3\n- 턴 종료 시 수치 1 감소. 턴 시작 시 수치가 0이면, 특정 유닛과 버프가 변경됨\n(흐트러짐 상태면, 흐트러짐 해제)\n\n- 위 효과 발동 후 기억 전환 수치는 기본값으로 돌아감
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransition].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack. If this unit has 0 Stacks of this effect at Turn Start, certain units and effects transform\n(when Staggered, recover from Stagger)\n\n- Once the above effect activates, reset Memory Transition Stack to Base Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury maleje o 1. Jeżeli na początku tury wartość wynosi 0, określone jednostki i buffy się zmieniają\n(przy Oszołomieniu wychodzi z Oszołomienia)\n\n- Po wywołaniu powyższego efektu stosy Przełączania Wspomnień wracają do wartości bazowej
392. [Słowo kluczowe [AengduNewArm] — nazwa] 도깨비팔
   źródło: BattleKeywords-exme.json :: dataList[id=AengduNewArm].name
   kontekst: identyfikator tagu w tekstach: `[AengduNewArm]`
   limit: do 40 znaków
   EN: Dokkaebi Arms
   PL: Ramiona Dokkaebi
393. [Słowo kluczowe [AengduNewArm] — opis] - 기본 공격 레벨 4 증가\n- 기본 방어 레벨 4 증가\n- 받는 피해 20% 감소\n- 스킬 사용 시 다음 턴에 신속 1 얻음 (턴당 2회)\n- 전투 종료 시 호흡 횟수 2 증가
   źródło: BattleKeywords-exme.json :: dataList[id=AengduNewArm].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +4\n- Base Defense Level +4\n- Take -20% damage\n- On Skill Use, gain 1 Haste next turn (2 times per turn)\n- Combat End: Gain +2 Poise Count
   PL: - Podstawowy Poziom Ataku +4\n- Podstawowy Poziom Obrony +4\n- Otrzymuje -20% obrażeń\n- Przy użyciu Umiejętności zyskuje 1 Pośpiech w następnej turze (2 na turę)\n- Po zakończeniu walki zyskuje +2 Licznika Oddechu
394. [Słowo kluczowe [AengduNewArm] — tekst klimatyczny] “…도깨비팔? 옛이야기에서 종종 나오는 그 도깨비를 말하는 것인가. 으음…”\n“믿기진 않지만, 림버스 컴퍼니에 몸담고 봐온 것들을 생각하면, 민담 속의 도깨비가 있다 해도 이상하지 않을 터.”\n“그러고 보니 도깨비 부대… 라는 것은 들어본 적 있는 것 같소.”
   źródło: BattleKeywords-exme.json :: dataList[id=AengduNewArm].flavor
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "... Dokkaebi Arms? Do you, perchance, speak of Dokkaebis that often appear in tales of old? Hmm..."\n"I can scarcely believe it, yet after all I have witnessed while relying on the hospitality of Limbus Company, the existence of Dokkaebis from folklore may well be within reason."\n"Come to think of it... I do recall hearing of a name called 'Dokkaebi Unit'..."
   PL: „...Ramiona Dokkaebi? Czy mówi pan o dokkaebi ze starych opowieści? Hm...”\n„Choć trudno w to uwierzyć, po tym, co widziałem w Limbus Company, istnienie dokkaebi z ludowych podań nie wydaje się dziwne.”\n„A tak zresztą... ‚oddział Dokkaebi’... chyba coś takiego słyszałem.”
395. [Słowo kluczowe [WindBlade] — nazwa] 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불
   źródło: BattleKeywords-exme.json :: dataList[id=WindBlade].name
   kontekst: identyfikator tagu w tekstach: `[WindBlade]`
   limit: do 100 znaków
   EN: Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire
   PL: Warsztat Mook - Ye [銳] II Typ, Dobycie Ostrza / Siła Pchnięcia: Ogień Dokkaebi
396. [Słowo kluczowe [WindBlade] — opis] - 최댓값: 20\n- 수치만큼 참격 피해량 +1% (최대 10%)\n- 수치 2당, 수비 스킬의 합 위력 -1 (최대 5)\n- 턴 종료 시 다음 턴에 수치 5당, 신속 1 얻음 (최대 3)
   źródło: BattleKeywords-exme.json :: dataList[id=WindBlade].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Deal +1% Slash damage for every Stack (max 10%)\n- Defense Skills lose 1 Clash Power for every 2 Stacks (max 5)\n- Turn End: Gain 1 Haste next turn for every 5 Stacks (max 3)
   PL: - Maks. stosów: 20\n- Zadaje +1% obrażeń Cięcia za każdy stos (maks. 10%)\n- Umiejętności obrony tracą 1 Moc Starcia za każde 2 stosy (maks. 5)\n- Na koniec tury zyskuje 1 Pośpiech w następnej turze za każde 5 stosów (maks. 3)
397. [Słowo kluczowe [WindBlade] — tekst klimatyczny] “뭐야? 혹시 그 모델 맘에 들어? 울 막둥이 보는 눈이 좋은데? 사장님~ 요 모델 시착해 봐도 괜찮을까요? 에이~ 그럼요! 망가뜨리면 살 테니까 걱정 마세요! 히히. 내가 말했지? 단골이라 이런 건 다 된다니까~ 검이랑 검집이랑 세트니까 같이 들어봐. 어때, 보기보다 좀 가볍지?”\n“호오…”\n“묵 공방에서 특허를 가지고 있는 입자? 가루? 그런 게 요 검집 안에 들어있어. 그래서 납도한 뒤에 발도할 때마다 날이 엄청 예리해지고, 순간적으로 검이 엄청 가벼워지거든? 그중에서도 예리함에 중점을 두고 만들어진 게 막둥이가 지금 들고 있는 모델이야. 아무튼 검을 검집에서 뽑을 때마다 삥~ 하고 버프가 걸린다는 느낌인 거지.”\n“묵 공방의 클래식 모델 중 하나인 예[銳] 시리즈 중 하나일 텐데… 마감 처리를 보면… 뭐야!? 이거 지금은 단종된 예[銳] 2식이잖아!? 이거 구하기 진짜 힘든 건데 여기 하나 남아있었네!?”\n“그리 귀한 것이오? 그렇다면 차라리 소저가 다루는 것이...”\n“으으으… 아냐! 척 봐도 막둥이 껀데 뭘! 의수에서 나오는 부스터 기능이랑 궁합도 괜찮을 거구. 익숙해지려면 시간이 좀 걸리긴 하겠지만, 제대로 다룰 수 있게 되면 어디 가서 꿇리진 않을걸? 아무튼 임시 떼고 정식으로 막둥이가 된 기념으로 이 선배가 사주는 거야!”\n“그렇다면… 감사히 받겠네. ”\n“아. 클래식 모델인 만큼 튼튼하긴 엄청 튼튼한데, 그래도 섬세한 부분이 있으니 부서지지 않게 조심… 아니, 부서지는 건 괜찮아. 그냥...”\n“죽지만 마.”\n“…그 말씀, 마음 깊이 새기겠소.”
   źródło: BattleKeywords-exme.json :: dataList[id=WindBlade].flavor
   limit: do 2200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Hm? You like that model? Ooh, new girl's got an eye for quality! Excuse me~! Can we try this model? Oh, c'mon, relax! I know the deal—'You break it, you buy it.' Thanks! Hehe... See? Told ya I'm a regular here~ Okay, so the sword and the scabbard come as a set, so grab 'em both and feel the weight. How's that? Not as heavy as they look, huh?"\n"Oho..."\n"So there's this particle? Powder? Thingy in that scabbard under patent by Mook Workshop! Every time you sheathe and unsheathe the sword, for a brief moment, its blade comes out way sharper and lighter! And that model you're holding happens to focus on the <i>sharpness</i>! So it's like, *Ding!* and voila, you get a nice buff on your weapon!"\n"I think it's one of the Ye [銳] series models—that's Mook Workshop's classic lineup, by the way. Check out the finish here, it's... What the heck?! Hey, this is the Ye [銳] 'Type II' model that went out of production! You know what, this stuff really isn't easy to come by—we're lucky we found one here!"\n"If it's such a rarity, Lady Ezra, perhaps you ought to wield it instead..."\n"Hnngh... No, it's fine... Well, I can see it's literally made for you! And it'll work real nice with those boosters on your new prosthetic arms. It'll need some getting used to, but you'll be one heck of a fighter once you get the hang of it! Anyway, consider it a gift from yours truly—you're officially one of us now. Officially our new girl! No more temp ID."\n"Then... I shall accept with gratitude."\n"By the way... Remember that 'classic lineup' part? It's super durable, but there <i>are</i> delicate parts that you should watch out not to break—okay, you know what, let 'em break if it really comes to that. Just..."\n"Just don't die on us."\n"... I shall take your words to heart."
   PL: „Co takiego? Podoba ci się ten model? Nasza nowa dziewczyna ma dobre oko! Przepraszam~! Możemy przymierzyć ten model? No weź, spokojnie! Znam zasady — ‚kto zepsuje, kupuje’. Dzięki! Hihi... No co ty? Mówiłam, że tu bywam~ Dobra, miecz i pochwa idą w zestawie, więc chwyć oba i poczuj wagę. No i jak? Lżejsze, niż wyglądają, co?”\n„Oho...”\n„W tej pochwie siedzi jakiś pył? Proszek? Opatentowany przez Warsztat Mook! Za każdym razem, gdy miecz wraca i wychodzi z pochwy, na moment staje się o dużo ostrzejszy i lżejszy! A model, który trzymasz, stawia właśnie na ostrość! Czyli tak — cyk! — i broń dostaje buffa.”\n„Chyba to jeden z modeli serii Ye [銳] — klasyki Warsztatu Mook. Patrzę na wykończenie... Co!? To wycofany z produkcji Ye [銳] II Typ!? Tego się naprawdę trudno szukać — a tu akurat jeden został!?”\n„Coś tak cennego? W takim razie może raczej pani Ezra powinna nim władać...”\n„Yyy... Nie! Już widzę, że to dla naszej nowej dziewczyny! Do tego pasować będzie do boosterów w twoich nowych protezach. Przyzwyczajenie zajmie chwilę, ale jak ją opanujesz, to nikt cię nie zmusi do klęczki! A tak w ogóle — przyjmij to jako prezent, że przestałaś być na czasówce i oficjalnie jesteś nasza!”\n„W takim razie... przyjmuję z wdzięcznością.”\n„Aha — skoro to klasyk, jest cholernie wytrzymały, ale ma delikatne elementy, więc uważaj, żeby niczego nie połamać... nie, właściwie połamiesz, to trudno. Po prostu...”\n„Tylko nie umrzyj.”\n„...Zapiszę te słowa głęboko w sercu.”
398. [Słowo kluczowe [Collage_LowMorale] — nazwa] 뒤섞인 기억
   źródło: BattleKeywords-exme.json :: dataList[id=Collage_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Collage_LowMorale]`
   limit: do 40 znaków
   EN: Jumbled Memories
   PL: Przemieszane Wspomnienia
399. [Słowo kluczowe [Collage_LowMorale] — opis] - 턴 시작 시 공격 레벨 증가 1~3, 방어 레벨 감소 1~3 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Collage_LowMorale].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 1~3 Offense Level Up and 1~3 Defense Level Down
   PL: - Na początku tury zyskuje 1–3 Wzrostu Poziomu Ataku i 1–3 Spadek Poziomu Obrony
400. [Słowo kluczowe [Collage_Panic] — nazwa] 뒤섞인 기억
   źródło: BattleKeywords-exme.json :: dataList[id=Collage_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Collage_Panic]`
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
401. [Słowo kluczowe [Collage_Panic] — opis] - 턴 시작 시 공격 레벨 증가 1~5, 방어 레벨 감소 1~5 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Collage_Panic].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 1~5 Offense Level Up and 1~5 Defense Level Down
   PL: - Na początku tury zyskuje 1–5 Wzrostu Poziomu Ataku i 1–5 Spadek Poziomu Obrony
402. [Słowo kluczowe [Lensman_LowMorale] — nazwa] 정보 집착
   źródło: BattleKeywords-exme.json :: dataList[id=Lensman_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Lensman_LowMorale]`
   limit: do 40 znaków
   EN: Intelligence Obsession
   PL: Obsesja Informacyjna
403. [Słowo kluczowe [Lensman_LowMorale] — opis] - 정보 취득을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +10%\n- 턴 시작 시 취약 1 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Lensman_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash against targets that have Intelligence Gathering, Base Power +1 and deal +10% damage\n- Turn Start: Gain 1 Fragile
   PL: - W Starciu z celami posiadającymi Zbieranie Informacji Moc Bazowa +1 i zadaje +10% obrażeń\n- Na początku tury zyskuje 1 Wrażliwości
404. [Słowo kluczowe [Lensman_Panic] — nazwa] 정보 집착
   źródło: BattleKeywords-exme.json :: dataList[id=Lensman_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Lensman_Panic]`
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Słowo kluczowe [Lensman_Panic] — opis] - 정보 취득을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +20%\n- 턴 시작 시 취약 2 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Lensman_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash against targets that have Intelligence Gathering, Base Power +1 and deal +20% damage\n- Turn Start: Gain 2 Fragile
   PL: - W Starciu z celami posiadającymi Zbieranie Informacji Moc Bazowa +1 i zadaje +20% obrażeń\n- Na początku tury zyskuje 2 Wrażliwości
406. [Słowo kluczowe [Aengdu_Lowmorale] — nazwa] 원망
   źródło: BattleKeywords-exme.json :: dataList[id=Aengdu_Lowmorale].name
   kontekst: identyfikator tagu w tekstach: `[Aengdu_Lowmorale]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
407. [Słowo kluczowe [Aengdu_Lowmorale] — opis] - 턴 시작 시 공격 위력 증가 1, 수비 위력 감소 1 얻음\n- 턴 종료 시 다음 턴에 신속 2 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Aengdu_Lowmorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 1 Attack Power Up and 1 Defense Power Down\n- Turn End: Gain 2 Haste next turn
   PL: - Na początku tury zyskuje 1 Wzrost Mocy Ataku i 1 Spadek Mocy Obrony\n- Na koniec tury zyskuje 2 Pośpiechu w następnej turze
408. [Słowo kluczowe [Aengdu_Panic] — nazwa] 원망
   źródło: BattleKeywords-exme.json :: dataList[id=Aengdu_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Aengdu_Panic]`
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Słowo kluczowe [Aengdu_Panic] — opis] - 턴 시작 시 공격 위력 증가 2, 수비 위력 감소 2 얻음\n턴 종료 시 다음 턴에 신속 2 얻음
   źródło: BattleKeywords-exme.json :: dataList[id=Aengdu_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 2 Attack Power Up and 2 Defense Power Down\n- Turn End: Gain 2 Haste next turn
   PL: - Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 2 Spadek Mocy Obrony\nNa koniec tury zyskuje 2 Pośpiechu w następnej turze
410. [Słowo kluczowe [BrandedKimSatgat] — nazwa] 낙인[奴]
   źródło: BattleKeywords-exme.json :: dataList[id=BrandedKimSatgat].name
   kontekst: identyfikator tagu w tekstach: `[BrandedKimSatgat]`
   limit: do 40 znaków
   EN: Brand - No [奴]
   PL: Naznaczenie - No [奴]
411. [Słowo kluczowe [BrandedKimSatgat] — opis] - 기본 공격 레벨 ?? 감소\n- 기본 방어 레벨 ?? 감소
   źródło: BattleKeywords-exme.json :: dataList[id=BrandedKimSatgat].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -??\n- Base Defense Level -??
   PL: - Podstawowy Poziom Ataku -??\n- Podstawowy Poziom Obrony -??
412. [Słowo kluczowe [DimensionalBagEzraETwo] — nazwa] 차원가방 - 유리아 공방
   źródło: BattleKeywords-exme.json :: dataList[id=DimensionalBagEzraETwo].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraETwo]`
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Słowo kluczowe [DimensionalBagEzraETwo] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 유리아 공방 도끼\n- 다음 공방 무기: 알라스 공방 장갑
   źródło: BattleKeywords-exme.json :: dataList[id=DimensionalBagEzraETwo].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: YuRia Atelier Axe\n- Next Workshop weapon: Allas Workshop Gloves
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Siekiera Warsztatu YuRia\n- Następna broń warsztatowa: Rękawice Warsztatu Allas
414. [Słowo kluczowe [RestingKimSatgat_LowMorale] — nazwa] 가라앉은 회한
   źródło: BattleKeywords-exme.json :: dataList[id=RestingKimSatgat_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[RestingKimSatgat_LowMorale]`
   limit: do 40 znaków
   EN: Deep-rooted Regret
   PL: Głęboko Zakorzeniony Żal
415. [Słowo kluczowe [RestingKimSatgat_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 피해량 감소 2 얻고 자신의 체력 40 회복
   źródło: BattleKeywords-exme.json :: dataList[id=RestingKimSatgat_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Damage Down and heal 40 HP
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Spadek Obrażeń i leczy 40 HP
416. [Słowo kluczowe [RestingKimSatgat_Panic] — nazwa] 가라앉은 회한
   źródło: BattleKeywords-exme.json :: dataList[id=RestingKimSatgat_Panic].name
   kontekst: identyfikator tagu w tekstach: `[RestingKimSatgat_Panic]`
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Słowo kluczowe [RestingKimSatgat_Panic] — opis] - 패닉\n- 턴 시작 시 피해량 감소 3 얻고 자신의 체력 60 회복
   źródło: BattleKeywords-exme.json :: dataList[id=RestingKimSatgat_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 3 Damage Down and heal 60 HP
   PL: - Panika\n- Na początku tury zyskuje 3 Spadek Obrażeń i leczy 60 HP
418. [Słowo kluczowe [ChoiSwordsmanship] — nazwa] 본국검술[살]
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanship].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSwordsmanship]`
   limit: do 50 znaków
   EN: Swordplay of the Homeland [Sal]
   PL: Rodzima Szermierka [Sal]
419. [Słowo kluczowe [ChoiSwordsmanship] — opis] - 최솟값: 1, 최댓값: 9\n- 스킬 사용시 수치가 최솟값이거나 최댓값이면, 자신이 사용하는 모든 코인이 <color=#ff6000><mark color=#ff000040><b><u>파괴 불가 코인</color></mark></b></u>으로 변경됨\n- <color=#ff6000><mark color=#ff000040><b><u>수치에 따라 스킬의 기본 위력과 코인 위력에 증감이 적용됨</color></mark></b></u>\n· 1 ~ 2: 기본 위력 -6, 코인 위력 +4\n· 3 ~ 4: 기본 위력 -3, 코인 위력 +2\n· 5: 효과 없음\n· 6 ~ 7: 기본 위력 +4, 코인 위력 -2\n· 8 ~ 9: 기본 위력 +8, 코인 위력 -3
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanship].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Min Stack 1; Max Stack 9\n- On Skill Use, at Min or Max Stacks, convert all Coins this unit uses to <color=#ff6000><mark color=#ff000040><b><u>Unbreakable Coins</color></mark></b></u>\n- <color=#ff6000><mark color=#ff000040><b><u>Skill Base Power and Coin Power shift based on Stack</color></mark></b></u>\n· 1 ~ 2 Stack: Base Power -6, Coin Power +4\n· 3 ~ 4 Stack: Base Power -3, Coin Power +2\n· 5 Stack: No effect\n· 6 ~ 7 Stack: Base Power +4, Coin Power -2\n· 8 ~ 9: Base Power +8, Coin Power -3
   PL: - Min. stosów: 1, Maks. stosów: 9\n- Przy użyciu Umiejętności, jeżeli wartość wynosi Min. lub Maks., wszystkie Monety stają się <color=#ff6000><mark color=#ff000040><b><u>Niezniszczalnymi Monetami</u></b></mark></color>\n- <color=#ff6000><mark color=#ff000040><b><u>Moc Bazowa i Moc Monety Umiejętności przesuwają się zależnie od stosów</u></b></mark></color>\n· 1–2 stosy: Moc Bazowa -6, Moc Monety +4\n· 3–4 stosy: Moc Bazowa -3, Moc Monety +2\n· 5 stosów: brak efektu\n· 6–7 stosów: Moc Bazowa +4, Moc Monety -2\n· 8–9: Moc Bazowa +8, Moc Monety -3
420. [Słowo kluczowe [ChoiSwordsmanshipOne] — nazwa] 본국태세 - 곰 사냥
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipOne].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSwordsmanshipOne]`
   limit: do 60 znaków
   EN: Battleform of the Homeland - Bearhunt
   PL: Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia
421. [Słowo kluczowe [ChoiSwordsmanshipOne] — opis] <color=#ff6000><mark color=#ff000040><b><u>단일 코인</color></mark></b></u> 스킬로 이루어진 패턴을 사용함\n\n본국검술[살] 수치가 <color=#ff6000><mark color=#ff000040><b><u>높을수록</color></mark></b></u> 임경업이 유리함
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipOne].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Use a pattern made of <color=#ff6000><mark color=#ff000040><b><u>single-coin</color></mark></b></u> Skills\n\nIm Gyeong-eop gains advantage at <color=#ff6000><mark color=#ff000040><b><u>higher</color></mark></b></u> Swordplay of the Homeland [Sal] Stack
   PL: Używa wzorca z Umiejętności <color=#ff6000><mark color=#ff000040><b><u>jednomonetowych</u></b></mark></color>\n\nIm <color=#ff6000><mark color=#ff000040><b><u>wyższa</u></b></mark></color> wartość Rodzimej Szermierki [Sal], tym większa przewaga Im Gyeong-eopa
422. [Słowo kluczowe [ChoiSwordsmanshipOne] — tekst klimatyczny] S사가 있는 19구의 산에는 온갖 짐승이 산다.\n그중에서도 곰은 그 덩치와 힘이 절벽에서 굴러오는 바위와 같아, 첫 합에서 밀리지 않고 일격에 베어내야 한다.
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipOne].flavor
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The mountains of S Corp.'s District 19 are home to all manner of beasts.\nAmongst them, the bear, in particular, boasts strength and force akin to boulders falling from the cliff in a landslide. Giving ground to the creature's charge is ill-advised—one must aim to hew it down with the first slash of the blade.
   PL: W górach Dystryktu 19 Korporacji S żyją rozmaite bestie.\nSpośród nich niedźwiedź ma siłę i potęgę skał toczących się z urwiska — nie wolno dać się odepchnąć w pierwszym Starciu; trzeba ściąć go jednym ciosem.
423. [Słowo kluczowe [ChoiSwordsmanshipMany] — nazwa] 본국태세 - 범 사냥
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipMany].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSwordsmanshipMany]`
   limit: do 60 znaków
   EN: Battleform of the Homeland - Tigerhunt
   PL: Rodzima Postawa Bojowa - Polowanie na Tygrysa
424. [Słowo kluczowe [ChoiSwordsmanshipMany] — opis] <color=#ff6000><mark color=#ff000040><b><u>다 코인</color></mark></b></u> 스킬로 이루어진 패턴을 사용함\n\n본국검술[살] 수치가 <color=#ff6000><mark color=#ff000040><b><u>낮을수록</color></mark></b></u> 임경업이 유리함
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipMany].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: Use a pattern made of <color=#ff6000><mark color=#ff000040><b><u>multi-coin</color></mark></b></u> Skills\n\nIm Gyeong-eop gains advantage at <color=#ff6000><mark color=#ff000040><b><u>lower</color></mark></b></u> Swordplay of the Homeland [Sal] Stack
   PL: Używa wzorca z Umiejętności <color=#ff6000><mark color=#ff000040><b><u>wielomonetowych</u></b></mark></color>\n\nIm <color=#ff6000><mark color=#ff000040><b><u>niższa</u></b></mark></color> wartość Rodzimej Szermierki [Sal], tym większa przewaga Im Gyeong-eopa
425. [Słowo kluczowe [ChoiSwordsmanshipMany] — tekst klimatyczny] 범은 영리하고 포악하다.\n일격에 살을 내어주는 범은 없다. 끝없이 몰아치는 연격으로 범의 숨통을 조이고, 끝내 그 목숨을 쳐내야 한다.\n그러지 못해 살아남은 범은 언젠가 산군이 된다.\n그것이 사람에게 영험한 운수를 안겨줄지, 악독한 재액으로 되돌아올지는 알 수 없다.
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipMany].flavor
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Tigers are cunning and ferocious.\nOne cannot hope to cut through a tiger's flesh with a single stroke. Only a relentless flurry of chained slashes can overwhelm the creature until it is felled at last.\nFail to do so, and the tiger will escape death—or best its opponent to one day grow into a Sangun, a Lord of the Mountain.\nWhether these beings will grant auspicious fortune on men or return as malevolent calamity is impossible to tell.
   PL: Tygrys jest sprytny i dziki.\nŻadnego tygrysa nie ściągnie się jednym ciosem. Tylko nieustanna fala kolejnych cięć dusi bestię, aż w końcu odbierze jej życie.\nTen, który przeżyje, kiedyś stanie się Sangun, Panem Gór.\nCzy zesle ludziom szczęście, czy wróci jako złośliwa klęska — nie sposób wiedzieć.
426. [Słowo kluczowe [ChoiSwordsmanshipShield] — nazwa] 두정갑[살]
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipShield].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSwordsmanshipShield]`
   limit: do 40 znaków
   EN: Dujeong Brigandine [Sal]
   PL: Kolczuga Dujeong [Sal]
427. [Słowo kluczowe [ChoiSwordsmanshipShield] — opis] - 최댓값: 5\n- 이 효과를 얻을 때, 수치당 자신의 최대 체력의 10%만큼의 보호막을 얻음 (최소 1, 소수점 버림, 이 효과로 얻은 보호막은 턴 종료시에도 사라지지 않음)\n- 전투 시작시, 수치 2당 방어 레벨 감소 1 얻음 (소수점 올림)\n- 참격 피해량 +(수치 x 2.5)%\n- <color=#ff6000><mark color=#ff000040><b><u>최대 체력의 10%에 해당하는 보호막 피해를 받았을 때 수치 1 감소</color></mark></b></u>
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSwordsmanshipShield].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Max Stack: 5\n- When gaining this effect, gain Shield equal to 10% of this unit's max HP for every Stack (min 1, rounded down; Shield gained due to this effect does not expire at Turn End)\n- Combat Start: Gain 1 Defense Level Down for every 2 Stack (rounded up)\n- Deal +(Stack x 2.5)% Slash damage\n- <color=#ff6000><mark color=#ff000040><b><u>Lose 1 Stack when taking Shield damage equal to 10% of this unit's max HP</color></mark></b></u>
   PL: - Maks. stosów: 5\n- Przy zdobyciu tego efektu zyskuje Tarczę równą 10% Maks. HP za każdy stos (min. 1, zaokrąglone w dół; ta Tarcza nie znika na koniec tury)\n- Na początku walki zyskuje 1 Spadek Poziomu Obrony za każde 2 stosy (zaokrąglone w górę)\n- Zadaje +(stosy x 2,5)% obrażeń Cięcia\n- <color=#ff6000><mark color=#ff000040><b><u>Traci 1 stos przy otrzymaniu obrażeń w Tarczę równych 10% Maks. HP</u></b></mark></color>
428. [Słowo kluczowe [PhotoTransitionChoi] — nazwa] 기억 전환
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransitionChoi].name
   kontekst: identyfikator tagu w tekstach: `[PhotoTransitionChoi]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Słowo kluczowe [PhotoTransitionChoi] — opis] - 기본값: 3\n- 턴 종료 시 수치 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>턴 시작 시 수치가 0이면, 퇴각하고 맵이 변경됨</color></mark></b></u>\n- 복귀 시 퇴각해있던 턴 만큼 본국태세에 따라 본국검술[살]을 얻거나 잃음\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransitionChoi].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>Turn Start: At 0 Stack, Retreat and transition into a different location</color></mark></b></u>\n- When Returning to the field, based on current Battleform of the Homeland, gain or lose (# of turns spent in Retreat) Swordplay of the Homeland [Sal] Stack\n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury maleje o 1\n- <color=#ff6000><mark color=#ff000040><b><u>Na początku tury przy 0 stosów wycofuje się, a mapa się zmienia</u></b></mark></color>\n- Przy powrocie na pole, zależnie od aktualnej Rodzimej Postawy Bojowej, zyskuje lub traci Rodzimą Szermierkę [Sal] w liczbie tur spędzonych w odwrocie\n· Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia: zyskuje\n· Rodzima Postawa Bojowa - Polowanie na Tygrysa: traci
430. [Słowo kluczowe [PhotoTransitionChoiCamera] — nazwa] 기억 전환
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransitionChoiCamera].name
   kontekst: identyfikator tagu w tekstach: `[PhotoTransitionChoiCamera]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Słowo kluczowe [PhotoTransitionChoiCamera] — opis] - 기본값: 3\n- 턴 종료 시 수치 1 감소\n- <color=#ff6000><mark color=#ff000040><b><u>턴 시작 시 수치가 0이면, 소멸하고 맵이 변경됨</color></mark></b></u>\n- 임경업이 퇴각한 턴 만큼 복귀 시 임경업의 본국태세에 따라 임경업이 본국검술[살]을 얻거나 잃음\n· 본국태세 - 곰 사냥: 얻음\n· 본국태세 - 범 사냥: 잃음
   źródło: BattleKeywords-exme.json :: dataList[id=PhotoTransitionChoiCamera].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: - Base Stack: 3\n- Turn End: Lose 1 Stack\n- <color=#ff6000><mark color=#ff000040><b><u>Turn Start: At 0 Stack, remove this unit and transition to a different location</color></mark></b></u>\n- When Returning to the field, based on Im Gyeong-eop's current Battleform of the Homeland, Im Gyeong-eop gains or loses (# of turns Im Gyeong-eop spent in Retreat) Swordplay of the Homeland [Sal] Stack \n· When in Battleform of the Homeland - Bearhunt: Gain Stack\n· When in Battleform of the Homeland - Tigerhunt: Lose Stack
   PL: - Wartość bazowa: 3\n- Na koniec tury maleje o 1\n- <color=#ff6000><mark color=#ff000040><b><u>Na początku tury przy 0 stosów znika, a mapa się zmienia</u></b></mark></color>\n- Przy powrocie Im Gyeong-eopa, zależnie od jego aktualnej Rodzimej Postawy Bojowej, zyskuje lub traci Rodzimą Szermierkę [Sal] w liczbie tur spędzonych w odwrocie\n· Rodzima Postawa Bojowa - Polowanie na Niedźwiedzia: zyskuje\n· Rodzima Postawa Bojowa - Polowanie na Tygrysa: traci
432. [Słowo kluczowe [ChoiSword_LowMorale] — nazwa] 현상된 기억
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSword_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSword_LowMorale]`
   limit: do 40 znaków
   EN: Developed Memories
   PL: Rozwinięte Wspomnienia
433. [Słowo kluczowe [ChoiSword_LowMorale] — opis] - 사기 저하\n- 취약 1 얻음, 피해량 +10%, 크리티컬 피해량 +15%
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSword_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Fragile, deal +10% damage, and deal +15% damage on Critical Hit
   PL: - Niskie Morale\n- Zyskuje 1 Wrażliwości, zadaje +10% obrażeń i +15% obrażeń Krytycznych
434. [Słowo kluczowe [ChoiSword_Panic] — nazwa] 현상된 기억
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSword_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ChoiSword_Panic]`
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Słowo kluczowe [ChoiSword_Panic] — opis] - 패닉\n- 취약 2 얻음, 피해량 +10%, 크리티컬 피해량 +30%, 본국궁[살] - 살 날리기의 코인으로 부여하는 효과 2배로 부여
   źródło: BattleKeywords-exme.json :: dataList[id=ChoiSword_Panic].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Fragile, deal +10% damage, deal +30% damage on Critical Hit, and double the effects inflicted by the Coins of the "Bow of the Homeland [Sal] - Arrowloose" Skill
   PL: - Panika\n- Zyskuje 2 Wrażliwości, zadaje +10% obrażeń, +30% obrażeń Krytycznych i podwaja efekty nakładane przez Monety Umiejętności „Rodzimego Łuku [Sal] - Wypuszczenia Strzały”
436. [Słowo kluczowe [DimensionalBagEzraDTwo] — nazwa] 차원가방 - 나미르 공방
   źródło: BattleKeywords-exme.json :: dataList[id=DimensionalBagEzraDTwo].name
   kontekst: identyfikator tagu w tekstach: `[DimensionalBagEzraDTwo]`
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Słowo kluczowe [DimensionalBagEzraDTwo] — opis] 차원가방에서 다음 공방 무기를 꺼냄\n- 현재 공방 무기: 나미르 공방 건틀릿\n- 다음 공방 무기: 유리아 공방 도끼
   źródło: BattleKeywords-exme.json :: dataList[id=DimensionalBagEzraDTwo].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Draws the next Workshop weapon from the Dimensional Bag\n- Current Workshop weapon: Namir Workshop Gauntlets\n- Next Workshop weapon: YuRia Atelier Axe
   PL: Wyjmuje z Worka Wymiarowego następną broń warsztatową\n- Obecna broń warsztatowa: Gauntlety Warsztatu Namir\n- Następna broń warsztatowa: Siekiera Warsztatu YuRia
438. [Słowo kluczowe [DimensionalBagEzraDTwo] — tekst klimatyczny] “G사 특이점인 구가 들어간 제품인데, 잘 쓰려면 공중에서 스위치를 눌러 발동시킨 다음, 무게로 찍어 눌러야 해. 제대로 꽂히면 진짜 아파!”
   źródło: BattleKeywords-exme.json :: dataList[id=DimensionalBagEzraDTwo].flavor
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Słowo kluczowe [SlaveHunersPower] — nazwa] 압송 명령
   źródło: BattleKeywords-exme.json :: dataList[id=SlaveHunersPower].name
   kontekst: identyfikator tagu w tekstach: `[SlaveHunersPower]`
   limit: do 40 znaków
   EN: Prisoner Transport Order
   PL: Rozkaz Konwoju
440. [Słowo kluczowe [SlaveHunersPower] — opis] - 기본 공격 레벨 5 증가\n- 기본 방어 레벨 5 증가
   źródło: BattleKeywords-exme.json :: dataList[id=SlaveHunersPower].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +5\n- Base Defense Level +5
   PL: - Podstawowy Poziom Ataku +5\n- Podstawowy Poziom Obrony +5
441. [Słowo kluczowe [LensmanPower] — nazwa] 조사 명령
   źródło: BattleKeywords-exme.json :: dataList[id=LensmanPower].name
   kontekst: identyfikator tagu w tekstach: `[LensmanPower]`
   limit: do 40 znaków
   EN: Investigation Order
   PL: Rozkaz Śledztwa
442. [Słowo kluczowe [LensmanPower] — opis] - 기본 공격 레벨 5 증가\n- 기본 방어 레벨 5 증가
   źródło: BattleKeywords-exme.json :: dataList[id=LensmanPower].desc
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-fools
- plik gry: `BattleKeywords-fools.json` (opisy wyświetlane w dymkach pomocy podczas walki)

443. [Słowo kluczowe [CandyForCharon] — nazwa] 사탕?
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon].name
   kontekst: identyfikator tagu w tekstach: `[CandyForCharon]`
   limit: do 40 znaków
   EN: Candy?
   PL: Cukierek?
444. [Słowo kluczowe [CandyForCharon] — opis] - 최댓값: 1\n- 사탕을 가지고 있을까?
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Where's the candy?
   PL: - Maks. wartości: 1\n- Czy będzie miał cukierek?
445. [Słowo kluczowe [TickTockTickTock] — nazwa] 째깍째깍?!
   źródło: BattleKeywords-fools.json :: dataList[id=TickTockTickTock].name
   kontekst: identyfikator tagu w tekstach: `[TickTockTickTock]`
   limit: do 40 znaków
   EN: Tick-Tock?!
   PL: Tik-Tak?!
446. [Słowo kluczowe [TickTockTickTock] — opis] - 턴 종료 시, 정신력을 10 회복
   źródło: BattleKeywords-fools.json :: dataList[id=TickTockTickTock].desc
   limit: do 120 znaków
   EN: - Heal 10 SP at Turn End
   PL: - Na koniec tury odzyskuje 10 Poczytalności
447. [Słowo kluczowe [CandyForCharon_LowMorale] — nazwa] 사탕
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[CandyForCharon_LowMorale]`
   limit: do 40 znaków
   EN: Candy
   PL: Cukierek
448. [Słowo kluczowe [CandyForCharon_LowMorale] — opis] - 사기 저하\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +3, 그 외의 인격과 합 진행시, 합 위력 -1
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_LowMorale].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When Clashing against Identities with Candy, Clash Power +3; when clashing against other Identities, Clash Power -1
   PL: - Niskie Morale\n- W Starciu z Tożsamościami z Cukierkiem Moc Starcia +3; w Starciu z innymi Tożsamościami Moc Starcia -1
449. [Słowo kluczowe [CandyForCharon_LowMorale] — podsumowanie] 조건에 따라 합위력 증감
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_LowMorale].summary
   limit: do 120 znaków
   EN: Conditional Clash Power fluctuation
   PL: Zmiana Mocy Starcia zależnie od warunków
450. [Słowo kluczowe [CandyForCharon_Panic] — nazwa] 사탕
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_Panic].name
   kontekst: identyfikator tagu w tekstach: `[CandyForCharon_Panic]`
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Słowo kluczowe [CandyForCharon_Panic] — opis] - 패닉\n- 사탕을 가지고 있는 인격과 합 진행 시, 합 위력 +5, 그 외의 인격과 합 진행시, 합 위력 -2
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_Panic].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- When Clashing against Identities with Candy, Clash Power +5; when clashing against other Identities, Clash Power -2
   PL: - Panika\n- W Starciu z Tożsamościami z Cukierkiem Moc Starcia +5; w Starciu z innymi Tożsamościami Moc Starcia -2
452. [Słowo kluczowe [CandyForCharon_Panic] — podsumowanie] 조건에 따라 합위력 증감
   źródło: BattleKeywords-fools.json :: dataList[id=CandyForCharon_Panic].summary
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-mowe
- plik gry: `BattleKeywords-mowe.json` (opisy wyświetlane w dymkach pomocy podczas walki)

453. [Słowo kluczowe [KeptBlood] — nazwa] 머금은 피
   źródło: BattleKeywords-mowe.json :: dataList[id=KeptBlood].name
   kontekst: identyfikator tagu w tekstach: `[KeptBlood]`
   limit: do 40 znaków
   EN: Stored Blood
   PL: Zmagazynowana Krew
454. [Słowo kluczowe [KeptBlood] — opis] - 최대 10\n- 최대 체력의 5%를 잃을 때마다 1씩 감소함.\n- 적중 시 최대 체력의 1%만큼 체력 회복
   źródło: BattleKeywords-mowe.json :: dataList[id=KeptBlood].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Lose 1 value every time this unit loses 5% HP.\n- On Hit, heal 1% of this unit's HP
   PL: - Maks. 10\n- Traci 1 wartości za każde utracone 5% Maks. HP.\n- Przy trafieniu leczy 1% HP
455. [Słowo kluczowe [BloodyCrave] — nazwa] 핏빛 갈구
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodyCrave].name
   kontekst: identyfikator tagu w tekstach: `[BloodyCrave]`
   limit: do 40 znaków
   EN: Bloodtinged Craving
   PL: Krwawa Żądza
456. [Słowo kluczowe [BloodyCrave] — opis] - 합 위력 증가 1 , 피해량 증가 1 얻음\n- 적중 시, 머금은 피를  1 얻음\n- 이번 턴에 머금은 피를 얻지 못했다면,  매 턴 얻는 효과 대신 다음 턴에 취약 2, 신속 1, 공격 레벨 증가 4 얻음
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodyCrave].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Clash Power Up and 1 Damage Up\n- On Hit, gain 1 Stored Blood\n- If this unit did not gain Stored Blood this turn, gain 2 Fragile, 1 Haste, and 4 Offense Level Up next turn instead of the above effect
   PL: - Zyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń\n- Przy trafieniu zyskuje 1 Zmagazynowanej Krwi\n- Jeżeli w tej turze nie zdobył Zmagazynowanej Krwi, zamiast powyższych efektów zyskuje w następnej turze 2 Wrażliwości, 1 Pośpiech i 4 Wzrostu Poziomu Ataku
457. [Słowo kluczowe [BloodPocket_LowMorale] — nazwa] 흡혈 갈망
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodPocket_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BloodPocket_LowMorale]`
   limit: do 40 znaków
   EN: Bloodthirst
   PL: Krwiożerczość
458. [Słowo kluczowe [BloodPocket_LowMorale] — opis] 턴 시작 시 취약, 피해량 증가 1 얻음
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodPocket_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Fragile and Damage Up
   PL: Na początku tury zyskuje 1 Wrażliwości i 1 Wzrost Obrażeń
459. [Słowo kluczowe [BloodPocket_Panic] — nazwa] 흡혈 갈망
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodPocket_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BloodPocket_Panic]`
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Słowo kluczowe [BloodPocket_Panic] — opis] 턴 시작시 취약, 피해량 증가 2 얻음
   źródło: BattleKeywords-mowe.json :: dataList[id=BloodPocket_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Fragile and Damage Up
   PL: Na początku tury zyskuje 2 Wrażliwości i 2 Wzrostu Obrażeń
461. [Słowo kluczowe [HardenedBlood] — nazwa] 경화 혈액
   źródło: BattleKeywords-mowe.json :: dataList[id=HardenedBlood].name
   kontekst: identyfikator tagu w tekstach: `[HardenedBlood]`
   limit: do 40 znaków
   EN: Coagulated Blood
   PL: Skrzepnięta Krew
462. [Słowo kluczowe [HardenedBlood] — opis] 수치만큼 자신의 공격 레벨과 방어 레벨이 증가 (최대 5)
   źródło: BattleKeywords-mowe.json :: dataList[id=HardenedBlood].desc
   limit: do 120 znaków
   EN: Gain Offense Level and Defense Level equal to the value (max 5)
   PL: Zyskuje Poziom Ataku i Poziom Obrony równy wartości (maks. 5)

## Słowa kluczowe bitwy — BattleKeywords-night-clean-up-re
- plik gry: `BattleKeywords-night-clean-up-re.json` (opisy wyświetlane w dymkach pomocy podczas walki)

463. [Słowo kluczowe [RepressedMurderousIntendHard] — nazwa] 억눌린 살기
   źródło: BattleKeywords-night-clean-up-re.json :: dataList[id=RepressedMurderousIntendHard].name
   kontekst: identyfikator tagu w tekstach: `[RepressedMurderousIntendHard]`
   limit: do 40 znaków
   EN: Repressed Bloodthirst
   PL: Stłumiona Krwiożerczość
464. [Słowo kluczowe [RepressedMurderousIntendHard] — opis] 기본 공격 레벨 -5, 기본 방어 레벨 -5
   źródło: BattleKeywords-night-clean-up-re.json :: dataList[id=RepressedMurderousIntendHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -5\nBase Defense Level -5
   PL: Podstawowy Poziom Ataku -5\nPodstawowy Poziom Obrony -5
465. [Słowo kluczowe [WeighedMurderousIntendHard] — nazwa] 짓눌린 살기
   źródło: BattleKeywords-night-clean-up-re.json :: dataList[id=WeighedMurderousIntendHard].name
   kontekst: identyfikator tagu w tekstach: `[WeighedMurderousIntendHard]`
   limit: do 40 znaków
   EN: Crushed Bloodthirst
   PL: Rozgnieciona Krwiożerczość
466. [Słowo kluczowe [WeighedMurderousIntendHard] — opis] 기본 공격 레벨 -15, 기본 방어 레벨 -15
   źródło: BattleKeywords-night-clean-up-re.json :: dataList[id=WeighedMurderousIntendHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -15\nBase Defense Level -15
   PL: Podstawowy Poziom Ataku -15\nPodstawowy Poziom Obrony -15

## Słowa kluczowe bitwy — BattleKeywords-pilgrimage
- plik gry: `BattleKeywords-pilgrimage.json` (opisy wyświetlane w dymkach pomocy podczas walki)

467. [Słowo kluczowe [NetherseaBrand] — nazwa] 명흔
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrand].name
   kontekst: identyfikator tagu w tekstach: `[NetherseaBrand]`
   limit: do 40 znaków
   EN: Nethersea Brand
   PL: Piętno Głębin
468. [Słowo kluczowe [NetherseaBrand] — opis] 턴이 지날 때마다 명흔의 영향 범위가 수감자 진영으로 확산\n- 1단계 : 시테러 진영\n- 2단계 : 전방 수감자 2명\n- 3단계 : 전방 수감자 5명\n- 4단계 : 모든 수감자
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrand].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nethersea Brand expands toward the Sinners with each passing turn.\n- Stage 1 : Sea Terror territory\n- Stage 2 : 2 frontmost Sinners\n- Stage 3 : 5 frontmost Sinners\n- Stage 4 : All Sinners
   PL: Z każdą turą wpływy Piętna Głębin rozszerzają się na Grzeszników.\n- 1. stopień: terytorium Sea Terror\n- 2. stopień: 2 Grzeszników z przodu\n- 3. stopień: 5 Grzeszników z przodu\n- 4. stopień: wszyscy Grzesznicy
469. [Słowo kluczowe [NetherseaBrand] — podsumowanie] 턴이 지날 때마다 명흔 확산
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrand].summary
   limit: do 120 znaków
   EN: The Nethersea Brand expands with each turn
   PL: Piętno Głębin rozszerza się z każdą turą
470. [Słowo kluczowe [NetherseaBrandUnit] — nazwa] 명흔
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrandUnit].name
   kontekst: identyfikator tagu w tekstach: `[NetherseaBrandUnit]`
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Słowo kluczowe [NetherseaBrandUnit] — opis] - 명흔 위의 수감자가 턴 종료 시 최대 체력의 5%만큼 고정 피해를 입고 신경 손상 3 얻음\n- 명흔 위의 시테러가 수감자에게 가하는 신경 손상이 크게 증가\n- 턴이 지날 때마다 명흔의 영향 범위가 수감자 진영으로 확산\n· 1단계 : 시테러 진영\n· 2단계 : 제일 앞에 있는 수감자 2명까지 적용\n· 3단계 : 제일 앞에 있는 수감자 5명까지 적용\n· 4단계 : 모든 수감자에게 적용
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrandUnit].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Sinners on top of Nethersea Brand: at Turn End, take fixed damage equal to 5% HP and gain 3 Nervous Impairment\n- Greatly increases the Nervous Impairment Stack Sea Terrors on top of Nethersea Brand inflict against Sinners\n- Nethersea Brand's influence expands toward Sinner territory with each passing turn\n· Stage 1 : Sea Terror territory\n· Stage 2 : Affects 2 frontmost Sinners\n· Stage 3 : Affects 5 frontmost Sinners\n· Stage 4 : Affects all Sinners
   PL: - Grzesznicy na Piętnie Głębin na koniec tury otrzymują obrażenia stałe równe 5% HP i zyskują 3 Uszkodzenia Nerwów\n- Sea Terror na Piętnie Głębin znacznie zwiększa nakładane na Grzeszników Uszkodzenia Nerwów\n- Z każdą turą wpływy Piętna Głębin rozszerzają się na Grzeszników\n· 1. stopień: terytorium Sea Terror\n· 2. stopień: 2 Grzeszników z przodu\n· 3. stopień: 5 Grzeszników z przodu\n· 4. stopień: wszyscy Grzesznicy
472. [Słowo kluczowe [NetherseaBrandUnit] — podsumowanie] 명흔 위의 아군이 고정 피해와 신경 손상 얻음.\n명흔 위의 적이 아군에게 가하는 신경 손상 크게 증가
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NetherseaBrandUnit].summary
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Allies on top of Nethersea Brand takes fixed damage and gain Nervous Impairment.\nGreatly increase the amount of Nervous Impairment inflicted against allies by enemies on top of Nethersea Brand
   PL: Sojusznicy na Piętnie Głębin otrzymują obrażenia stałe i zyskują Uszkodzenia Nerwów.\nWrogowie na Piętnie Głębin znacznie zwiększają nakładane na sojuszników Uszkodzenia Nerwów
473. [Słowo kluczowe [SeaTerrorCell] — nazwa] 시테러 동화
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=SeaTerrorCell].name
   kontekst: identyfikator tagu w tekstach: `[SeaTerrorCell]`
   limit: do 40 znaków
   EN: Sea Terror Assimilation
   PL: Asymilacja Sea Terror
474. [Słowo kluczowe [SeaTerrorCell] — opis] - 최댓값 : 5\n- 턴 시작 시 수치 1 증가\n- 수치 1 당 공격 레벨 감소 1, 방어 레벨 감소 1 얻음\n- 턴 종료시 아군 수감자의 버프 수치가 5면 전장 이탈.\n- 아군 수감자가 버프 보유시, 수비 스킬을 장착하고 전투를 시작하면, 턴 종료시 전장 이탈
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=SeaTerrorCell].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 5\n- Gain 1 Stack at Turn Start\n- Gain 1 Offense Level Down and 1 Defense Level Down per Stack\n- Turn End: if an allied Sinner has 5 Stacks of this effect, it Escapes Battlefield.\n- When an allied Sinner has a Defense Skill equipped while it has this effect, they Escape Battlefield at Combat Start
   PL: - Maks. stosów: 5\n- Na początku tury rośnie o 1\n- Zyskuje 1 Spadek Poziomu Ataku i 1 Spadek Poziomu Obrony za każdy stos\n- Na koniec tury, jeżeli sojuszniczy Grzesznik ma 5 stosów, opuszcza pole bitwy.\n- Jeżeli sojuszniczy Grzesznik ma ten efekt i rozpoczął walkę z wyposażoną Umiejętnością obrony, opuszcza pole bitwy na koniec tury
475. [Słowo kluczowe [SeaTerrorCell] — podsumowanie] 수치에 비례하여 공격 레벨 감소, 방어 레벨 감소 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=SeaTerrorCell].summary
   limit: do 120 znaków
   EN: Gains Offense Level Down and Defense Level Down based on the Stack
   PL: Zyskuje Spadek Poziomu Ataku i Spadek Poziomu Obrony zależnie od stosów
476. [Słowo kluczowe [NervousImpairment] — nazwa] 신경 손상
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NervousImpairment].name
   kontekst: identyfikator tagu w tekstach: `[NervousImpairment]`
   limit: do 40 znaków
   EN: Nervous Impairment
   PL: Uszkodzenie Nerwów
477. [Słowo kluczowe [NervousImpairment] — opis] - 최댓값 : 30\n- 수치가 30이면, 흐트러진 다음 최대 체력의 25%만큼 고정 피해를 입고 이 효과 제거
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NervousImpairment].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 30\n- At 30 Stack, become Staggered; then, take fixed damage equal to 25% HP, and remove this effect
   PL: - Maks. stosów: 30\n- Przy 30 stosach zostaje oszołomiony, a następnie otrzymuje obrażenia stałe równe 25% HP i traci ten efekt
478. [Słowo kluczowe [NervousImpairment] — podsumowanie] 흐트러지고 큰 체력 피해를 입음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=NervousImpairment].summary
   limit: do 120 znaków
   EN: Become Staggered and take significant HP damage
   PL: Zostaje oszołomiony i otrzymuje znaczne obrażenia HP
479. [Słowo kluczowe [WaitingforCommandMod] — nazwa] 명령 대기
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WaitingforCommandMod].name
   kontekst: identyfikator tagu w tekstach: `[WaitingforCommandMod]`
   limit: do 40 znaków
   EN: Standby State
   PL: Stan Oczekiwania
480. [Słowo kluczowe [WaitingforCommandMod] — opis] - 명령 대기 상태에서는 피해를 입기 전까지 공격 스킬을 사용하지 않음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WaitingforCommandMod].desc
   limit: do 120 znaków
   EN: - When in Standby State, this unit does not use Attack Skills until it takes damage
   PL: - W stanie Oczekiwania jednostka nie używa Umiejętności ataku, dopóki nie otrzyma obrażeń
481. [Słowo kluczowe [WaitingforCommandMod] — podsumowanie] 명령 대기 상태에서는 피해를 입기 전까지 공격 스킬을 사용하지 않음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WaitingforCommandMod].summary
   limit: do 120 znaków
   EN: When in Standby State, this unit does not use Attack Skills until it takes damage
   PL: W stanie Oczekiwania jednostka nie używa Umiejętności ataku, dopóki nie otrzyma obrażeń
482. [Słowo kluczowe [ParticipationMod] — nazwa] 참전
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ParticipationMod].name
   kontekst: identyfikator tagu w tekstach: `[ParticipationMod]`
   limit: do 40 znaków
   EN: Combat-Ready State
   PL: Stan Bojowy
483. [Słowo kluczowe [ParticipationMod] — opis] - 피해를 받아 공격 스킬을 사용하는 상태로 돌입\n- 참전 상태에서 턴 시작 시,\n· 모든 적에게 신경 손상 3 부여\n· 속도 최솟값, 최댓값 3 증가\n· 잃은 체력 10%당 공격 레벨 증가 1 얻음 (최대 8)\n- 참전 상태에서 턴 종료 시, 최대 체력의 10%만큼 고정 체력 피해를 입음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ParticipationMod].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - After taking damage, this unit has begun to use its Attack Skills.\n- Turn Start while in Combat-Ready State:\n· Inflict 3 Nervous Impairment to all enemies\n· Min & Max Speed +3\n· Gain 1 Offense Level Up for every 10% missing HP (max 8)\n- Turn End while in Combat-Ready State: take fixed damage equal to 10% HP
   PL: - Po otrzymaniu obrażeń jednostka przystępuje do używania Umiejętności ataku.\n- Na początku tury w stanie Bojowym:\n· Nakłada 3 Uszkodzenia Nerwów wszystkim wrogom\n· Min. i Maks. Szybkość +3\n· Zyskuje 1 Wzrost Poziomu Ataku za każde 10% brakującego HP (maks. 8)\n- Na koniec tury w stanie Bojowym otrzymuje obrażenia stałe równe 10% HP
484. [Słowo kluczowe [ParticipationMod] — podsumowanie] 피해를 받아 공격 스킬을 사용하는 상태로 돌입
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ParticipationMod].summary
   limit: do 120 znaków
   EN: After taking damage, this unit begins to use its Attack Skills
   PL: Po otrzymaniu obrażeń jednostka przystępuje do używania Umiejętności ataku
485. [Słowo kluczowe [AbyssalVitality] — nazwa] 깊은 바다의 생명력
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=AbyssalVitality].name
   kontekst: identyfikator tagu w tekstach: `[AbyssalVitality]`
   limit: do 40 znaków
   EN: Abyssal Vitality
   PL: Witalność Otchłani
486. [Słowo kluczowe [AbyssalVitality] — opis] - 최댓값 : 100\n- 특정 스킬 사용 시 소모됨\n- 소모될 때마다 그 수치만큼 자신의 정신력 회복
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=AbyssalVitality].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack : 100\n- Consumed when using certain Skills\n- Every time this effect is consumed, Heal SP on self by the amount consumed
   PL: - Maks. stosów: 100\n- Zużywana przy użyciu określonych Umiejętności\n- Za każdym razem, gdy jest zużywana, odzyskuje Poczytalność równą zużytej liczbie
487. [Słowo kluczowe [AbyssalVitality] — podsumowanie] 특정 스킬 사용 시 소모\n- 소모될 때마다 정신력 회복
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=AbyssalVitality].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Consumed when using certain Skills\n- Every time this effect is consumed, Heal SP
   PL: Zużywana przy użyciu określonych Umiejętności\n- Za każdym zużyciem odzyskuje Poczytalność
488. [Słowo kluczowe [IndelibleGoodwill] — nazwa] 지워지지 않을 선의
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IndelibleGoodwill].name
   kontekst: identyfikator tagu w tekstach: `[IndelibleGoodwill]`
   limit: do 40 znaków
   EN: Indelible Compassion
   PL: Niewymazywalne Współczucie
489. [Słowo kluczowe [IndelibleGoodwill] — opis] - 턴 종료 시 보호막이 사라지지 않음 (피해, 효과로 사라지는 경우는 제외)\n- 보호막이 피격을 받아 파괴되면, 흐트러지고 다음 턴까지 취약 5 얻음\n- 흐트러짐 손상으로 흐트러지면, 다음 턴까지 취약 5 얻음\n- 이 버프 효과로 얻는 취약은 중첩되지 않음\n- 보호막 수치는 중첩 가능하며, 이 효과가 적용 중인 경우에는 보호막의 수치가 보호막 적용 대상의 최대 체력 50%를 넘을 수 없음\n- 이 효과는 보호막 관리 효과로 취급됨 (다른 보호막 관리 효과 적용 시, 교체됨)
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IndelibleGoodwill].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This unit does not lose Shield at Turn End (unless removed by damage or certain effects)\n- When the Shield breaks due to getting hit, become Staggered and gain 5 Fragile until next turn\n- When becoming Staggered due to raised Stagger threshold, gain 5 Fragile until next turn\n- Fragile gained due to this buff's effects do not stack\n- Shield HP can stack, however; when this effect is active, the shield HP cannot be more than 50% of the Shielded unit's max HP\n- This effect counts as a 'Shield Management' effect. (replaced when gaining a different Shield Management effect)
   PL: - Na koniec tury Tarcza nie znika (chyba że zniknęła od obrażeń lub efektów)\n- Gdy Tarcza pęknie od trafienia, zostaje oszołomiona i zyskuje 5 Wrażliwości do następnej tury\n- Gdy zostaje oszołomiona przez podniesiony Próg Oszołomienia, zyskuje 5 Wrażliwości do następnej tury\n- Wrażliwości zdobyte dzięki temu buffowi się nie kumulują\n- HP Tarczy może się kumulować; podczas tego efektu HP Tarczy nie może przekraczać 50% Maks. HP chronionej jednostki\n- Ten efekt liczy się jako „Zarządzanie Tarczą” (zastępowany przy zdobyciu innego efektu Zarządzania Tarczą)
490. [Słowo kluczowe [IndelibleGoodwill] — podsumowanie] 턴 종료 시 보호막이 사라지지 않음\n보호막이 파괴되면 크게 약해짐
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IndelibleGoodwill].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Does not lose Shield at Turn End\nWhen the Shield breaks, become very fragile
   PL: Na koniec tury Tarcza nie znika\nGdy Tarcza pęknie, jednostka staje się bardzo podatna
491. [Słowo kluczowe [ColdAirDOQ] — nazwa] 냉기
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ColdAirDOQ].name
   kontekst: identyfikator tagu w tekstach: `[ColdAirDOQ]`
   limit: do 40 znaków
   EN: Cold
   PL: Chłód
492. [Słowo kluczowe [ColdAirDOQ] — opis] - 최댓값 : 3\n- 냉기 1당, 속도 1 감소\n- 스킬 종료 시 수치가 3이면, 우울 피해 20과 정신력 피해 20을 받고, 이번 턴과 다음 턴에 빙결 1 얻음 모든 효과 발동 후 냉기 소멸\n- 턴 종료 시 이번 턴에 마지막 기사를 공격하지 않았으면, 소멸
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ColdAirDOQ].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Lose 1 Speed for every Cold Stack\n- If this unit has 3 Stacks after Skill End: take 20 Gloom damage and 20 SP damage; then, gain 1 Frozen this turn and next turn.\n- Cold Stack expires after all effects are activated\n- Turn End: if this unit did not attack The Last Knight, expires
   PL: - Maks. stosów: 3\n- Traci 1 Szybkości za każdy stos Chłodu\n- Jeżeli na koniec Umiejętności ma 3 stosy: otrzymuje 20 obrażeń Posępności i 20 obrażeń Poczytalności, a w tej i następnej turze zyskuje 1 Zamarznięcia\n- Chłód znika po wywołaniu wszystkich efektów\n- Na koniec tury znika, jeżeli w tej turze nie zaatakował Ostatniego Rycerza
493. [Słowo kluczowe [FreezingDOQ] — nazwa] 빙결
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=FreezingDOQ].name
   kontekst: identyfikator tagu w tekstach: `[FreezingDOQ]`
   limit: do 40 znaków
   EN: Frozen
   PL: Zamarznięcie
494. [Słowo kluczowe [FreezingDOQ] — opis] - 특수 냉기\n- 이번 턴동안 행동할 수 없음\n- 체력이 1이 될 시 일부 스킬 발동을 무효화함
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=FreezingDOQ].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Cold\n- Cannot act for this turn\n- Certain Skill activations become nullified at 1 HP
   PL: - Specjalny Chłód\n- Nie może działać w tej turze\n- Przy HP 1 wybrane aktywacje Umiejętności są unieważniane
495. [Słowo kluczowe [BloodborneDOQ] — nazwa] 기사의 피와 뼈
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=BloodborneDOQ].name
   kontekst: identyfikator tagu w tekstach: `[BloodborneDOQ]`
   limit: do 40 znaków
   EN: The Knight's Corpus
   PL: Ciało Rycerza
496. [Słowo kluczowe [BloodborneDOQ] — opis] 받는 피해량 +80%
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=BloodborneDOQ].desc
   limit: do 120 znaków
   EN: Take +80% damage
   PL: Otrzymuje +80% obrażeń
497. [Słowo kluczowe [WeakenDOQ] — nazwa] 재난과 시련
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WeakenDOQ].name
   kontekst: identyfikator tagu w tekstach: `[WeakenDOQ]`
   limit: do 40 znaków
   EN: Misery and Calamity
   PL: Nędza i Klęska
498. [Słowo kluczowe [WeakenDOQ] — opis] - 공격 레벨 ?? 감소\n- 방어 레벨 ?? 감소
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WeakenDOQ].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level -??\n- Defense Level -??
   PL: - Poziom Ataku -??\n- Poziom Obrony -??
499. [Słowo kluczowe [DOQ_LowMorale] — nazwa] 군체 의식
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DOQ_LowMorale]`
   limit: do 40 znaków
   EN: Hive Mind
   PL: Świadomość Roju
500. [Słowo kluczowe [DOQ_LowMorale] — opis] 모든 내성이 보통 상태가 됨
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_LowMorale].desc
   limit: do 120 znaków
   EN: All Resistances change to 'Normal'
   PL: Wszystkie odporności zmieniają się na Zwykłą
501. [Słowo kluczowe [DOQ_LowMorale] — podsumowanie] 모든 내성이 보통 상태가 됨
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_LowMorale].summary
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Słowo kluczowe [DOQ_Panic] — nazwa] 군체 의식
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DOQ_Panic]`
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Słowo kluczowe [DOQ_Panic] — opis] 모든 내성이 보통 상태가 됨\n스킬로 받는 화상, 출혈, 진동, 파열의 위력을 2배로 받음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All Resistances change to 'Normal'\nDouble the amount of Burn, Bleed, Tremor, and Rupture Potency gained due to Skill effects
   PL: Wszystkie odporności zmieniają się na Zwykłą\nPodwaja Siłę Podpalenia, Krwawienia, Wstrząsu i Rozdarcia otrzymywaną przez Umiejętności
504. [Słowo kluczowe [DOQ_Panic] — podsumowanie] 모든 내성이 보통 상태가 됨\n스킬로 받는 화상, 출혈, 진동, 파열의 위력을 2배로 받음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DOQ_Panic].summary
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [Słowo kluczowe [CallOfSea_LowMorale] — nazwa] 동족의 부름
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[CallOfSea_LowMorale]`
   limit: do 40 znaków
   EN: Call of the Bloodkin
   PL: Wołanie Pokrewnych
506. [Słowo kluczowe [CallOfSea_LowMorale] — opis] 턴 종료시 자신의 체력을 최대 체력의 3% 소모하여 자신을 포함한 모든 아군에게 다음 턴에 공격 위력 증가 1, 취약 1 부여
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].desc
   limit: do 150 znaków
   EN: Turn End: consume 3% HP to apply 1 Attack Power Up and 1 Fragile to all allies, including this unit, next turn
   PL: Na koniec tury zużywa 3% HP, by nakładać na wszystkich sojuszników, łącznie z sobą, 1 Wzrost Mocy Ataku i 1 Wrażliwości w następnej turze
507. [Słowo kluczowe [CallOfSea_LowMorale] — podsumowanie] 체력을 소모하여 아군에게 공격 위력 증가, 취약 부여
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_LowMorale].summary
   limit: do 120 znaków
   EN: Consume HP to apply Attack Power Up and Fragile to allies
   PL: Zużywa HP, by nakładać na sojuszników Wzrost Mocy Ataku i Wrażliwość
508. [Słowo kluczowe [CallOfSea_Panic] — nazwa] 동족의 부름
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_Panic].name
   kontekst: identyfikator tagu w tekstach: `[CallOfSea_Panic]`
   (powtórzenie elementu 505 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Słowo kluczowe [CallOfSea_Panic] — opis] 턴 종료시 자신의 체력을 최대 체력의 5% 소모하여 취약 1을 얻고 자신을 포함한 모든 아군에게 다음 턴에 공격 위력 증가 1, 취약 1 부여
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_Panic].desc
   limit: do 170 znaków
   EN: Turn End: consume 5% HP and gain 1 Fragile to apply 1 Attack Power Up and 1 Fragile to all allies, including this unit, next turn
   PL: Na koniec tury zużywa 5% HP i zyskuje 1 Wrażliwości, by nakładać na wszystkich sojuszników, łącznie z sobą, 1 Wzrost Mocy Ataku i 1 Wrażliwości w następnej turze
510. [Słowo kluczowe [CallOfSea_Panic] — podsumowanie] 체력을 소모하여 아군에게 공격 위력 증가, 취약 부여
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=CallOfSea_Panic].summary
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Słowo kluczowe [BitOfEmotion] — nazwa] 감정 공유
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=BitOfEmotion].name
   kontekst: identyfikator tagu w tekstach: `[BitOfEmotion]`
   limit: do 40 znaków
   EN: Emotional Connection
   PL: Więź Emocjonalna
512. [Słowo kluczowe [BitOfEmotion] — opis] - 적에게 공격 적중 시, (50/스킬의 코인 수)% 확률로 사용한 스킬 속성의 E.G.O 자원 1개 얻음\n- 아군의 스킬 공격 종료 시 적이 사망했다면, 가장 적게 보유한 무작위 E.G.O 자원 2개 얻음\n- 이번 전투에서 다음 E.G.O 스킬 사용 시, 소모한 자원을 종류 별로 1개씩 획득 (오버클록 시, 2개씩 획득)\n· 영작오 홍루\n· 명령 : 용해 파우스트\n· 눈부시지 않은 영광 그레고르\n· 파도의 만가 이스마엘
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=BitOfEmotion].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Hit against enemies: (50 / # of Coins)% chance to gain 1 E.G.O resource corresponding to the used Skill's Affinity\n- When an enemy dies after an allied unit's Skill attack ends, gain 2 least-owned E.G.O Resources\n- In an Encounter, gain 1 E.G.O resource of each Affinity consumed when using the following E.G.O Skills (2 of each when using Overclocked Skills)\n· To Remain Oneself Hong Lu\n· Command : Meltdown Faust\n· Unbrilliant Glory Gregor\n· Tidal Elegy Ishmael
   PL: - Przy trafieniu wrogów: (50 / liczba Monet Umiejętności)% szans na 1 Zasób E.G.O Grzechu użytej Umiejętności\n- Gdy po zakończeniu ataku Umiejętnością sojusznika ginie wrog, zyskuje 2 najmniej posiadanych Zasobów E.G.O\n- W tej walce przy użyciu następujących Umiejętności E.G.O odzyskuje po 1 Zasobie E.G.O każdego zużytego Grzechu (2 sztuki przy Przeciążeniu)\n· Pozostać Sobą Hong Lu\n· Rozkaz : Roztopienie Faust\n· Nieolśniewająca Chwała Gregor\n· Elegia Fal Ishmael
513. [Słowo kluczowe [BitOfEmotion] — podsumowanie] 공격이 적중하거나 적 사망 시, E.G.O 자원 얻음\n특정 E.G.O 스킬 사용 시, E.G.O 자원 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=BitOfEmotion].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Hit, or on enemyt death, gain E.G.O Resources\nWhen using certain E.G.O Skills, gain E.G.O Resources
   PL: Przy trafieniu lub śmierci wroga zyskuje Zasoby E.G.O\nPrzy użyciu określonych Umiejętności E.G.O zyskuje Zasoby E.G.O
514. [Słowo kluczowe [WildernessSurvivalModule] — nazwa] 조력자 - 야외 생존 유닛
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WildernessSurvivalModule].name
   kontekst: identyfikator tagu w tekstach: `[WildernessSurvivalModule]`
   limit: do 60 znaków
   EN: Little Handy - Wilderness Survival Module
   PL: Little Handy - Moduł Przetrwania w Terenie
515. [Słowo kluczowe [WildernessSurvivalModule] — opis] - 최대 체력이 20% 증가하고 스킬, 패시브, 버프 효과로 회복하는 체력 회복량이 40%만큼 증가
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WildernessSurvivalModule].desc
   limit: do 120 znaków
   EN: - Max HP +20%. Heal +40% more from Skills, Passives, and buff effects
   PL: - Maks. HP +20%. Leczy +40% więcej przez Umiejętności, pasywne i efekty buffów
516. [Słowo kluczowe [WildernessSurvivalModule] — podsumowanie] 최대 체력과 체력 회복량이 증가
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=WildernessSurvivalModule].summary
   limit: do 120 znaków
   EN: Gain max HP and heal more
   PL: Zwiększa Maks. HP i ilość leczenia
517. [Słowo kluczowe [HousekeepingAssistantModule] — nazwa] 조력자 - 가사 보조 모듈
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].name
   kontekst: identyfikator tagu w tekstach: `[HousekeepingAssistantModule]`
   limit: do 60 znaków
   EN: Little Handy - Housekeeping Assistant Module
   PL: Little Handy - Moduł Pomocy Gospodarczej
518. [Słowo kluczowe [HousekeepingAssistantModule] — opis] - 성도의 손 사용 시, 다음 턴에 1회 추가로 발동\n- 턴 시작 시, 이번 전투 동안 성도의 손으로 명흔을 제거한 횟수만큼 공격 레벨 증가, 방어 레벨 증가 얻음 (각각 최대 4)
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When activating the Hand of the Saint, it activates again once next turn\n- Turn Start: gain Offense Level Up and Defense Level Up equal to the number of times Nethersea Brand was removed by using the Hand of the Saint during this Encounter (max 4 each)
   PL: - Przy aktywacji Ręki Świętego aktywuje się ponownie raz w następnej turze\n- Na początku tury zyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony równy liczbie usunięć Piętna Głębin przez Rękę Świętego w tej walce (każdy maks. 4)
519. [Słowo kluczowe [HousekeepingAssistantModule] — podsumowanie] 성도의 손 사용 시, 다음 턴에 1회 추가 발동\n명흔 제거한 횟수만큼 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=HousekeepingAssistantModule].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When activating the Hand of the Saint, it activates again once next turn\nTurn Start: gain Offense Level Up and Defense Level Up equal to the number of times Nethersea Brand was removed
   PL: Przy aktywacji Ręki Świętego aktywuje się ponownie raz w następnej turze\nZyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony równy liczbie usunięć Piętna Głębin
520. [Słowo kluczowe [IncrementalMotionFirmware] — nazwa] 조력자 - 운동 증량 펌웨어
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].name
   kontekst: identyfikator tagu w tekstach: `[IncrementalMotionFirmware]`
   limit: do 60 znaków
   EN: Little Handy - Incremental Motion Firmware
   PL: Little Handy - Firmware Przyrostowego Ruchu
521. [Słowo kluczowe [IncrementalMotionFirmware] — opis] - 모든 아군의 제일 앞에 있는 흐트러짐 선을 하나 제거\n- 흐트러질 경우, 1회에 한하여 다음 턴 시작 시 흐트러짐 상태에서 즉시 해제
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Remove 1 highest Stagger threshold from every allied unit\n- When Staggered, immediately recover from Stagger at the start of the next turn (once)
   PL: - Usuwa 1 najwyższy Próg Oszołomienia z każdej jednostki sojusznika\n- Przy Oszołomieniu natychmiast wychodzi z Oszołomienia na początku następnej tury (1 raz)
522. [Słowo kluczowe [IncrementalMotionFirmware] — podsumowanie] 흐트러짐 선 하나 제거\n흐트러질 시, 다음 턴에 흐트러짐 상태에서 즉시 해제
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=IncrementalMotionFirmware].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remove one Stagger Threshold\nWhen Staggered, immediately recover next turn
   PL: Usuwa jeden Próg Oszołomienia\nPrzy Oszołomieniu natychmiast wychodzi z Oszołomienia w następnej turze
523. [Słowo kluczowe [MiniDecontaminationKit] — nazwa] 조력자 - 얼룩 제거 세트
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=MiniDecontaminationKit].name
   kontekst: identyfikator tagu w tekstach: `[MiniDecontaminationKit]`
   limit: do 60 znaków
   EN: Little Handy - Mini Decontamination Kit
   PL: Little Handy - Mini Zestaw Odkażający
524. [Słowo kluczowe [MiniDecontaminationKit] — opis] - 명흔이 아군에게 더 이상 피해를 입히지 않고 신경 손상을 부여하지 않음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=MiniDecontaminationKit].desc
   limit: do 120 znaków
   EN: - Nethersea Brand no longer inflicts Nervous Impairment or deals damage to allies
   PL: - Piętno Głębin nie zadaje już sojusznikom obrażeń ani nie nakłada Uszkodzeń Nerwów
525. [Słowo kluczowe [MiniDecontaminationKit] — podsumowanie] 명흔이 아군에게 더 이상 피해를 입히지 않고 신경 손상을 부여하지 않음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=MiniDecontaminationKit].summary
   limit: do 120 znaków
   EN: Nethersea Brand no longer inflicts Nervous Impairment or deals damage to allies
   PL: Piętno Głębin nie zadaje już sojusznikom obrażeń ani nie nakłada Uszkodzeń Nerwów
526. [Słowo kluczowe [ExternalUpgradeModule] — nazwa] 조력자 - 외장 강화 장치
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ExternalUpgradeModule].name
   kontekst: identyfikator tagu w tekstach: `[ExternalUpgradeModule]`
   limit: do 60 znaków
   EN: Little Handy - External Upgrade Module
   PL: Little Handy - Moduł Zewnętrznych Ulepszeń
527. [Słowo kluczowe [ExternalUpgradeModule] — opis] - 효과 획득 이후 3턴 동안 턴 시작 시 위력 증가 2, 피해량 증가 2 얻음 (대기 해제된 인격은 대기 해제된 턴부터 적용)
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ExternalUpgradeModule].desc
   limit: do 210 znaków
   EN: - For 3 turns after gaining this effect: gain 2 Power Up and 2 Damage Up at the start of each turn (Substituting units earn it in the turn they Substitute in)
   PL: - Przez 3 tury po zdobyciu tego efektu zyskuje na początku każdej tury 2 Wzrost Mocy i 2 Wzrost Obrażeń (jednostki wchodzące z Rezerwy zyskują od tury wejścia)
528. [Słowo kluczowe [ExternalUpgradeModule] — podsumowanie] 효과 획득 후 3턴 동안 위력 증가, 피해량 증가 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=ExternalUpgradeModule].summary
   limit: do 120 znaków
   EN: For 3 turns after gaining this effect: gain Power Up and Damage Up
   PL: Przez 3 tury po zdobyciu efektu zyskuje Wzrost Mocy i Wzrost Obrażeń
529. [Słowo kluczowe [DesireToSave_LowMorale] — nazwa] 선의의 마음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DesireToSave_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Compassion
   PL: Serce Współczucia
530. [Słowo kluczowe [DesireToSave_LowMorale] — opis] - 가하는 피해량이 (대상이 보유한 신경 손상/2)%만큼 증가 (최대 15%)\n턴 시작 시, 피해량 증가 1, 취약 2 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +(Nervous Impairment on target / 2)% damage (max 15%)\n- Turn Start: gain 1 Damage Up and 2 Fragile
   PL: - Zadaje +(Uszkodzenia Nerwów celu / 2)% obrażeń (maks. 15%)\nNa początku tury zyskuje 1 Wzrost Obrażeń i 2 Wrażliwości
531. [Słowo kluczowe [DesireToSave_LowMorale] — podsumowanie] 대상의 신경 손상에 비례하여 피해량 증가
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_LowMorale].summary
   limit: do 120 znaków
   EN: Deal more damage based on Nervous Impairment on target
   PL: Zadaje więcej obrażeń zależnie od Uszkodzeń Nerwów celu
532. [Słowo kluczowe [DesireToSave_Panic] — nazwa] 선의의 마음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DesireToSave_Panic]`
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Słowo kluczowe [DesireToSave_Panic] — opis] - 가하는 피해량이 (대상이 보유한 신경 손상)%만큼 증가 (최대 30%)\n- 턴 시작 시, 피해량 증가 2, 취약 3 얻음
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_Panic].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +(Nervous Impairment on target)% damage (max 30%)\n- Turn Start: gain 2 Damage Up and 3 Fragile
   PL: - Zadaje +(Uszkodzenia Nerwów celu)% obrażeń (maks. 30%)\n- Na początku tury zyskuje 2 Wzrostu Obrażeń i 3 Wrażliwości
534. [Słowo kluczowe [DesireToSave_Panic] — podsumowanie] 대상의 신경 손상에 비례하여 피해량 증가
   źródło: BattleKeywords-pilgrimage.json :: dataList[id=DesireToSave_Panic].summary
   (powtórzenie elementu 531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Słowa kluczowe bitwy — BattleKeywords-schema
- plik gry: `BattleKeywords-schema.json` (opisy wyświetlane w dymkach pomocy podczas walki)

535. [Słowo kluczowe [BlackCloudBladeEnemy] — nazwa] 흑운도
   źródło: BattleKeywords-schema.json :: dataList[id=BlackCloudBladeEnemy].name
   kontekst: identyfikator tagu w tekstach: `[BlackCloudBladeEnemy]`
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL: Klinga Czarnego Obłoku
536. [Słowo kluczowe [BlackCloudBladeEnemy] — opis] - 최댓값 : 1\n- 참격 위력 1 증가\n- 참격 스킬로 공격 적중시 출혈 1 부여
   źródło: BattleKeywords-schema.json :: dataList[id=BlackCloudBladeEnemy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Slash Power +1\n- On Hit using Slash Skills, inflict 1 Bleed
   PL: - Maks. stosów: 1\n- Siła Cięcia +1\n- Przy trafieniu Umiejętnościami Cięcia nakłada 1 Krwawienie
537. [Słowo kluczowe [EngageToBattleEnemy] — nazwa] 임전
   źródło: BattleKeywords-schema.json :: dataList[id=EngageToBattleEnemy].name
   kontekst: identyfikator tagu w tekstach: `[EngageToBattleEnemy]`
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
538. [Słowo kluczowe [EngageToBattleEnemy] — opis] - 최댓값 : 1\n- 자신의 스킬, 코인 효과로 출혈 위력, 횟수를 부여할 때 부여하는 값 +1\n- 이번 전투 동안 참격 위력 증가 1, 참격 피해량 증가 3 얻음
   źródło: BattleKeywords-schema.json :: dataList[id=EngageToBattleEnemy].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Bleed Potency and Count inflicted using this unit's Skill or Coin effects: +1\n- Gain 1 Slash Power Up and 3 Slash DMG Up for the duration of this Encounter
   PL: - Maks. stosów: 1\n- Siła i Licznik Krwawienia nakładane efektami Umiejętności lub Monet: +1\n- Na czas tej walki zyskuje 1 Wzrost Mocy Cięcia i 3 Wzrost Obrażeń Cięcia
539. [Słowo kluczowe [SharpSensibility] — nazwa] 칼질의 재미
   źródło: BattleKeywords-schema.json :: dataList[id=SharpSensibility].name
   kontekst: identyfikator tagu w tekstach: `[SharpSensibility]`
   limit: do 40 znaków
   EN: Delightful Swordbutchery
   PL: Rozkosz Rzeźbienia Ostrzem
540. [Słowo kluczowe [SharpSensibility] — opis] - 최댓값 : 100\n- 스킬 슬롯에 ‘발도 자세’가 장착된 상태에서 자신의 스킬 코인 적중 시, 10 얻음 (스킬당 1회)\n- 특정 스킬에서 소모됨
   źródło: BattleKeywords-schema.json :: dataList[id=SharpSensibility].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- On Hit using Skill Coins while "Battō Shisei" is equipped on Skill Slot, gain 10 Stacks (once per Skill)\n- Consumed by certain Skills
   PL: - Maks. stosów: 100\n- Przy trafieniu Monetami Umiejętności, gdy „Battō Shisei” jest wyposażone w slot, zyskuje 10 stosów (1 raz na Umiejętność)\n- Zużywana przez określone Umiejętności
541. [Słowo kluczowe [SharpSensibility] — tekst klimatyczny] ‘검에 집중하고 검을 뽑고 누군가가 쓰러지고. 이렇게 삶과 죽음이 교차하는 검 놀이가 제일 재밌단 말이지.’
   źródło: BattleKeywords-schema.json :: dataList[id=SharpSensibility].flavor
   limit: do 330 znaków
   EN: 'The mind settles on the hilt grasped within my palms, then the blade leaps outta its sheath. Blink, and somebody's already hittin' the floor. Swords go <i>clang</i>, and crossroads of life and death flash before our eyes... There ain't no better game than that.'
   PL: „Umysł skupia się na trzonie w dłoni, ostrze wyskakuje z pochwy. Mgnienie oka — i ktoś już leży na deskach. Miecze brzęczą, a przed oczami przebiega granica życia i śmierci... Nie ma lepszej zabawy.”
542. [Słowo kluczowe [InkwashShadow_LowMorale] — nazwa] 안하무인
   źródło: BattleKeywords-schema.json :: dataList[id=InkwashShadow_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[InkwashShadow_LowMorale]`
   limit: do 40 znaków
   EN: Overbearing Hubris
   PL: Bezczelna Pycha
543. [Słowo kluczowe [InkwashShadow_LowMorale] — opis] - 사기 저하\n- 턴 시작 시 피해량 증가 1, 취약 1을 얻음
   źródło: BattleKeywords-schema.json :: dataList[id=InkwashShadow_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Damage Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości
544. [Słowo kluczowe [InkwashShadow_Panic] — nazwa] 안하무인
   źródło: BattleKeywords-schema.json :: dataList[id=InkwashShadow_Panic].name
   kontekst: identyfikator tagu w tekstach: `[InkwashShadow_Panic]`
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Słowo kluczowe [InkwashShadow_Panic] — opis] - 패닉\n- 턴 시작 시 피해량 증가 2, 취약 2를 얻음
   źródło: BattleKeywords-schema.json :: dataList[id=InkwashShadow_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Damage Up and 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Obrażeń i 2 Wrażliwości
546. [Słowo kluczowe [ElectricPolePower] — nazwa] 고압 방전
   źródło: BattleKeywords-schema.json :: dataList[id=ElectricPolePower].name
   kontekst: identyfikator tagu w tekstach: `[ElectricPolePower]`
   limit: do 40 znaków
   EN: High-voltage Discharge
   PL: Wysokonapięciowe Wyładowanie
547. [Słowo kluczowe [ElectricPolePower] — opis] - 최댓값 : 10\n- 진동 폭발 피격 시 5 감소 (스킬당 1회)\n- 나태 속성 스킬 피격 시 1 감소 (스킬당 1회)\n- 나태 속성이 아닌 스킬에 받는 피해량 -100%\n- 흐트러짐 상태가 되지 않음
   źródło: BattleKeywords-schema.json :: dataList[id=ElectricPolePower].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- When hit by Tremor Burst, lose 5 Stacks (once per Skill)\n- When hit by Sloth Skills, lose 1 Stack (once per Skill)\n- Take -100% damage from non-Sloth Skills\n- Cannot become Staggered
   PL: - Maks. stosów: 10\n- Przy trafieniu Wyładowaniem Wstrząsu traci 5 stosów (raz na Umiejętność)\n- Przy trafieniu Umiejętnościami Lenistwa traci 1 stos (raz na Umiejętność)\n- Otrzymuje -100% obrażeń od Umiejętności poza Lenistwem\n- Nie może zostać oszołomiony
548. [Słowo kluczowe [SweeperSchema] — nazwa] 청소 시간
   źródło: BattleKeywords-schema.json :: dataList[id=SweeperSchema].name
   kontekst: identyfikator tagu w tekstach: `[SweeperSchema]`
   limit: do 40 znaków
   EN: Time to <i>Sweep</i>
   PL: Czas na Sprzątanie
549. [Słowo kluczowe [SweeperSchema] — opis] {0}턴 후 청소 종료
   źródło: BattleKeywords-schema.json :: dataList[id=SweeperSchema].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The Sweeping ends after {0} turn(s)
   PL: Sprzątanie kończy się po {0} turach

## Słowa kluczowe bitwy — BattleKeywords-tkt-re
- plik gry: `BattleKeywords-tkt-re.json` (opisy wyświetlane w dymkach pomocy podczas walki)

550. [Słowo kluczowe [AccumulatedPastSinner] — nazwa] 축적된 과거
   źródło: BattleKeywords-tkt-re.json :: dataList[id=AccumulatedPastSinner].name
   kontekst: identyfikator tagu w tekstach: `[AccumulatedPastSinner]`
   limit: do 40 znaków
   EN: Accumulated Past
   PL: Skumulowana Przeszłość
551. [Słowo kluczowe [AccumulatedPastSinner] — opis] - 최대값 : 12\n- 턴 시작시 수치 3 당, 합 위력 증가 1, 공격 레벨 증가 1 얻음
   źródło: BattleKeywords-tkt-re.json :: dataList[id=AccumulatedPastSinner].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 12\n- Turn Start: gain 1 Clash Power Up and 1 Offense Level Up for every 3 Stack
   PL: - Maks. stosów: 12\n- Na początku tury zyskuje 1 Wzrost Mocy Starcia i 1 Wzrost Poziomu Ataku za każde 3 stosy
552. [Słowo kluczowe [OutisNoHat] — nazwa] 강력 징수 집행
   źródło: BattleKeywords-tkt-re.json :: dataList[id=OutisNoHat].name
   kontekst: identyfikator tagu w tekstach: `[OutisNoHat]`
   limit: do 40 znaków
   EN: Violent Collections
   PL: Gwałtowne Windykacje
553. [Słowo kluczowe [OutisNoHat] — opis] - 자신에게 신속이 있을 때, 자신의 기본 스킬로 얻는 자신의 진동 횟수 +1\n- 자신의 속도가 대상보다 빠르면, 피해량 (대상과의 속도 차이 x 3)% (최대 15%)
   źródło: BattleKeywords-tkt-re.json :: dataList[id=OutisNoHat].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit has Haste, gain +1 more Tremor Count from its Base Skills\n- If this unit's Speed is faster than the target's, deal +(Speed difference x 3)% damage (max 15%)
   PL: - Jeżeli ma Pośpiech, podstawowe Umiejętności zyskują +1 więcej Licznika Wstrząsu\n- Jeżeli Szybkość jest większa niż celu, zadaje +(różnica Szybkości x 3)% obrażeń (maks. 15%)

## Słowa kluczowe bitwy — BattleKeywords-tkt
- plik gry: `BattleKeywords-tkt.json` (opisy wyświetlane w dymkach pomocy podczas walki)

554. [Słowo kluczowe [FusionVibration] — nazwa] 진폭 얽힘
   źródło: BattleKeywords-tkt.json :: dataList[id=FusionVibration].name
   kontekst: identyfikator tagu w tekstach: `[FusionVibration]`
   limit: do 40 znaków
   EN: Amplitude Entanglement
   PL: Splątanie Amplitudy
555. [Słowo kluczowe [FusionVibration] — opis] - 얽힘시키는 진동 효과와 대상의 진동 계열을 진동 - 중첩으로 합침.\n- 얽힘 시 기존 진동의 위력, 횟수가 유지됨.\n- 진동 - 중첩에 진폭 변환 발동 시 변환시키려는 진동 효과가 얽힘으로 적용됨.\n- 턴 종료시, 진동으로 변환됨
   źródło: BattleKeywords-tkt.json :: dataList[id=FusionVibration].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Fuses the effects of the Tremor type added by Amplitude Entanglement and the Tremor type currently on target together under Tremor - Superposition.\n- Potency and Count values do not change over Entanglement.\n- When triggering Amplitude Conversion on Tremor - Superposition, it activates as Amplitude Entanglement instead.\n- Turn End: converted into base Tremor.
   PL: - Scala efekt Wstrząsu dodawany przez Splątanie Amplitudy z typem Wstrząsu na celu w Wstrząs - Superpozycja.\n- Podczas Splątania Siła i Licznik obecnego Wstrząsu zostają zachowane.\n- Przy wywołaniu Konwersji Amplitudy na Wstrząsie - Superpozycji efekt Wstrząsu zadziała jako Splątanie Amplitudy.\n- Na koniec tury zamienia się w zwykły Wstrząs
556. [Słowo kluczowe [VibrationNesting] — nazwa] 진동 - 중첩
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationNesting].name
   kontekst: identyfikator tagu w tekstach: `[VibrationNesting]`
   limit: do 40 znaków
   EN: Tremor - Superposition
   PL: Wstrząs - Superpozycja
557. [Słowo kluczowe [VibrationNesting] — opis] - 진폭 얽힘을 통해 얻을 수 얻을 수 있음.\n- 진폭 변환시 진동 - 중첩에 해당 특수 진동이 추가됨.
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationNesting].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gained through Amplitude Entanglement\n- When triggering Amplitude Conversion, add the effects of the resulting Tremor type to the list of active Tremor effects under Tremor - Superposition.
   PL: - Zdobywany przez Splątanie Amplitudy\n- Przy wywołaniu Konwersji Amplitudy do listy aktywnych efektów Wstrząsu w Wstrząsie - Superpozycji dołącza wynikowy Specjalny Wstrząs
558. [Słowo kluczowe [VibrationDistribution] — nazwa] 진동 - 분배
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationDistribution].name
   kontekst: identyfikator tagu w tekstach: `[VibrationDistribution]`
   limit: do 40 znaków
   EN: Tremor - Distribution
   PL: Wstrząs - Dystrybucja
559. [Słowo kluczowe [VibrationDistribution] — opis] - 턴 종료 시 (아군 전체의 진동 횟수의 합 / 살아있는 아군 수)만큼 다음 턴에 공격 레벨 증가를 얻음 (최대 5)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationDistribution].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Gain ((sum of all allies' Tremor Count) / (# of surviving allies)) Offense Level Up next turn (max 5)\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Na koniec tury zyskuje (suma Liczników Wstrząsu wszystkich sojuszników / liczba żyjących sojuszników) Wzrost Poziomu Ataku w następnej turze (maks. 5)\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Po zakończeniu tury traci 1 Licznika\n- (Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających lub zmniejszających Siłę i Licznik Wstrząsu)
560. [Słowo kluczowe [TcorpSpecialInvestigator] — nazwa] T사 특별 수사관 배지
   źródło: BattleKeywords-tkt.json :: dataList[id=TcorpSpecialInvestigator].name
   kontekst: identyfikator tagu w tekstach: `[TcorpSpecialInvestigator]`
   limit: do 50 znaków
   EN: T Corp. Special Investigator Badge
   PL: Odznaka Specjalnego Śledczego Korporacji T
561. [Słowo kluczowe [TcorpSpecialInvestigator] — opis] - 체력이 0이 될 때, 체력이 1 미만으로 감소하지 않고, 전체 체력의 80%만큼 즉시 회복. 흐트러짐 상태 해제 (전투당 1회 발동)\n- 버프 효과 발동 시 다음 턴부터 5턴 동안 턴 시작 시 공격 위력 증가 2 얻음.
   źródło: BattleKeywords-tkt.json :: dataList[id=TcorpSpecialInvestigator].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: -When this unit takes lethal damage, their HP does not drop below 1, instantly heals 80% of their max HP, and recovers from Stagger. (Once per Encounter)\n- When this buff effect activates, starting next turn, this unit gains 2 Attack Power Up at every Turn Start for 5 turns.
   PL: - Przy śmiertelnych obrażeniach HP nie spada poniżej 1, natychmiast leczy 80% Maks. HP i wychodzi z Oszołomienia (1 raz na walkę)\n- Po wywołaniu tego efektu, od następnej tury, zyskuje 2 Wzrostu Mocy Ataku na początku każdej tury przez 5 tur.
562. [Słowo kluczowe [VibrationChain] — nazwa] 진동 - 사슬
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationChain].name
   kontekst: identyfikator tagu w tekstach: `[VibrationChain]`
   limit: do 40 znaków
   EN: Tremor - Chain
   PL: Wstrząs - Łańcuch
563. [Słowo kluczowe [VibrationChain] — opis] - 진동 위력 10 당 합 위력 1 감소 (최대 3)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-tkt.json :: dataList[id=VibrationChain].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 1 Clash Power for every 10 Tremor Potency on self (max 3)\n- When Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Traci 1 Moc Starcia za każde 10 Siły Wstrząsu (maks. 3)\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Po zakończeniu tury traci 1 Licznika\n- (Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających lub zmniejszających Siłę i Licznik Wstrząsu)
564. [Słowo kluczowe [TimeRentalTwo] — nazwa] T사의 시간 대여
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeRentalTwo].name
   kontekst: identyfikator tagu w tekstach: `[TimeRentalTwo]`
   limit: do 40 znaków
   EN: T Corp. Borrowed Time
   PL: Pożyczony Czas Korporacji T
565. [Słowo kluczowe [TimeRentalTwo] — opis] 턴 종료시\n-다음 턴에 신속, 합 위력 증가, 취약을 (시간 대여 횟수 - 1)만큼 얻음.\n- 횟수가 1이면, 턴 종료시 효과를 대신하여 다음 턴에 속박을 (시간 대여 위력-1) X 2만큼 얻음\n- 위력 1 증가, 횟수 1 감소\n- 가지고 있는 신속보다 속박이 많을 경우 시간 대여 해제, 흐트러짐 상태가 됨.
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeRentalTwo].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End:\n- Gain (Borrowed Time Count - 1) Haste, Clash Power Up, and Fragile next turn.\n- At 1 Count, gain (2 x (Borrowed Time Stack - 1) Bind next turn instead.\n- Gain 1 Stack and lose 1 Count\n- If this unit has more Bind than it has Haste, the Borrowed Time effect expires and this unit gets Staggered.
   PL: Na koniec tury\n- Zyskuje (Licznik Pożyczonego Czasu - 1) Pośpiechu, Wzrostu Mocy Starcia i Wrażliwości w następnej turze.\n- Przy 1 Liczniku zamiast powyższego efektu zyskuje (2 x (Siła Pożyczonego Czasu - 1)) Spętań w następnej turze\n- Zyskuje 1 Siły i traci 1 Licznika\n- Jeżeli ma więcej Spętań niż Pośpiechu, efekt Pożyczonego Czasu znika, a jednostka zostaje oszołomiona.
566. [Słowo kluczowe [TimeAccumulation] — nazwa] 시간 누진
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeAccumulation].name
   kontekst: identyfikator tagu w tekstach: `[TimeAccumulation]`
   limit: do 40 znaków
   EN: Time Delay
   PL: Opóźnienie Czasu
567. [Słowo kluczowe [TimeAccumulation] — opis] 이 효과가 있는 동안 피해를 받지 않고 저장함.\n턴 종료 시 1 감소\n턴 종료 시 수치가 1이면, 저장한 피해의 2배만큼 나태 피해를 주고 효과 제거\n이 효과가 존재할 때, 추가로 얻거나 갱신되지 않음
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeAccumulation].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As long as this effect is active, damage dealt against this unit is stored and not taken.\nTurn End: reduce value by 1\nTurn End: If there is only 1 value left of this effect, the effect expires after dealing (2 x stored damage) Sloth damage to this unit\nWhen this effect is active, its value cannot be gained or be refreshed.
   PL: Dopóki ten efekt jest aktywny, otrzymywane obrażenia są magazynowane i nie są przyjmowane.\nNa koniec tury maleje o 1\nNa koniec tury, jeżeli zostaje tylko 1 wartość, efekt znika po zadaniu (2 x zmagazynowane obrażenia) obrażeń Lenistwa\nPodczas istnienia tego efektu jego wartość nie może zostać zdobyta ani odnowiona
568. [Słowo kluczowe [ParryingResultDown] — nazwa] 합 위력 감소
   źródło: BattleKeywords-tkt.json :: dataList[id=ParryingResultDown].name
   kontekst: identyfikator tagu w tekstach: `[ParryingResultDown]`
   limit: do 40 znaków
   EN: Clash Power Down
   PL: Spadek Mocy Starcia
569. [Słowo kluczowe [ParryingResultDown] — opis] 합 진행 시, 합 위력이 수치만큼 감소
   źródło: BattleKeywords-tkt.json :: dataList[id=ParryingResultDown].desc
   limit: do 120 znaków
   EN: In a Clash, lose Clash Power equal to the value
   PL: W Starciu traci Moc Starcia równą wartości
570. [Słowo kluczowe [ParryingResultUp] — nazwa] 합 위력 증가
   źródło: BattleKeywords-tkt.json :: dataList[id=ParryingResultUp].name
   kontekst: identyfikator tagu w tekstach: `[ParryingResultUp]`
   limit: do 40 znaków
   EN: Clash Power Up
   PL: Wzrost Mocy Starcia
571. [Słowo kluczowe [ParryingResultUp] — opis] 합 진행 시, 합 위력이 수치만큼 증가
   źródło: BattleKeywords-tkt.json :: dataList[id=ParryingResultUp].desc
   limit: do 120 znaków
   EN: In a Clash, gain Clash Power equal to the value
   PL: W Starciu zyskuje Moc Starcia równą wartości
572. [Słowo kluczowe [ParryingResultUp] — podsumowanie] 합 진행 시, 합 위력이 수치만큼 증가
   źródło: BattleKeywords-tkt.json :: dataList[id=ParryingResultUp].summary
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Słowo kluczowe [LimitedTime] — nazwa] 빼앗은 시간
   źródło: BattleKeywords-tkt.json :: dataList[id=LimitedTime].name
   kontekst: identyfikator tagu w tekstach: `[LimitedTime]`
   limit: do 40 znaków
   EN: Stolen Time
   PL: Skradziony Czas
574. [Słowo kluczowe [LimitedTime] — opis] - 턴 시작 시 수치가 200 이상이면, (수치 - 200)/50만큼 공격 레벨 증가, 방어 레벨 증가를 얻음.\n- 턴 시작 시 수치가 200 미만이면, (200 - 수치)/50 만큼 공격 레벨 감소, 방어 레벨 감소를 얻음.
   źródło: BattleKeywords-tkt.json :: dataList[id=LimitedTime].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: At 200+ value, gain (value - 200)/50 Offense Level Up & Defense Level Up.\n- Turn Start: At less than 200 value, gain (200 - value)/50 Offense Level Down & Defense Level Down.
   PL: - Na początku tury przy wartości 200+: zyskuje (wartość - 200)/50 Wzrost Poziomu Ataku i Wzrost Poziomu Obrony.\n- Na początku tury przy wartości poniżej 200: zyskuje (200 - wartość)/50 Spadek Poziomu Ataku i Spadek Poziomu Obrony.
575. [Słowo kluczowe [OwnTime] — nazwa] 분담 시간
   źródło: BattleKeywords-tkt.json :: dataList[id=OwnTime].name
   kontekst: identyfikator tagu w tekstach: `[OwnTime]`
   limit: do 40 znaków
   EN: Shared Time
   PL: Współdzielony Czas
576. [Słowo kluczowe [OwnTime] — opis] - 턴 시작 시 수치가 40 이상이면, (수치 - 40)/10 만큼 공격 레벨 증가, 방어 레벨 증가를 얻음.\n- 턴 시작 시 수치가 40 미만이면, (40 - 수치)/10 만큼 공격 레벨 감소, 방어 레벨 감소를 얻음.
   źródło: BattleKeywords-tkt.json :: dataList[id=OwnTime].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: At 40+ value, gain (value - 40)/10 Offense Level Up & Defense Level Up.\n- Turn Start: At less than 40 value, gain (40 - value)/10 Offense Level Down & Defense Level Down.
   PL: - Na początku tury przy wartości 40+: zyskuje (wartość - 40)/10 Wzrost Poziomu Ataku i Wzrost Poziomu Obrony.\n- Na początku tury przy wartości poniżej 40: zyskuje (40 - wartość)/10 Spadek Poziomu Ataku i Spadek Poziomu Obrony.
577. [Słowo kluczowe [EquitableDistribution] — nazwa] 시간 공동 분담 지출
   źródło: BattleKeywords-tkt.json :: dataList[id=EquitableDistribution].name
   kontekst: identyfikator tagu w tekstach: `[EquitableDistribution]`
   limit: do 40 znaków
   EN: Joint Time Expenditure
   PL: Wspólny Wydatek Czasu
578. [Słowo kluczowe [EquitableDistribution] — opis] 분담 시간이 소모될 때, 모든 뇌가 공정하게 시간을 지출함.
   źródło: BattleKeywords-tkt.json :: dataList[id=EquitableDistribution].desc
   limit: do 120 znaków
   EN: When spending Shared Time, the Brains spend an equal amount of time across the board.
   PL: Gdy Współdzielony Czas jest wydawany, Mózgi wydawają go uczciwie, po równo.
579. [Słowo kluczowe [UnfairDistribution] — nazwa] 내부 분열
   źródło: BattleKeywords-tkt.json :: dataList[id=UnfairDistribution].name
   kontekst: identyfikator tagu w tekstach: `[UnfairDistribution]`
   limit: do 40 znaków
   EN: Infighting
   PL: Konflikt Wewnętrzny
580. [Słowo kluczowe [UnfairDistribution] — opis] 분담 시간이 소모될 때 각 뇌가 내키는대로 시간을 지출함.\n턴 시작 시 남은 시간이 동일하지 않은 부위의 수만큼 모든 부위가 보호를 잃음.
   źródło: BattleKeywords-tkt.json :: dataList[id=UnfairDistribution].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When spending Shared Time, the Brains no longer spend an equal amount of time across the board.\nTurn Start: all parts lose Protection equal to the number of Parts with different remaining Time values.
   PL: Gdy Współdzielony Czas jest wydawany, każdy Mózg wydaje go wedle własnego uznania.\nNa początku tury wszystkie części tracą Ochronę równą liczbie części o różnej pozostałej wartości Czasu.
581. [Słowo kluczowe [TimeAcceleration] — nazwa] 시간 가속
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeAcceleration].name
   kontekst: identyfikator tagu w tekstach: `[TimeAcceleration]`
   limit: do 40 znaków
   EN: Time Acceleration
   PL: Przyspieszenie Czasu
582. [Słowo kluczowe [TimeAcceleration] — opis] - 자신의 속도 5 증가\n- 자신의 스킬이 강화됨.\n- 취약 1을 얻고, 진동 폭발, 스킬, 코인 효과로 받는 흐트러짐 손상이 50% 증가함.
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeAcceleration].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 5 Speed\n- Enhances this unit's Skills.\n- Gain 1 Fragile; when Tremor Burst, Skill or Coin effect raises this unit's Stagger Threshold, it raises it by +50% more.
   PL: - Zyskuje 5 Szybkości\n- Wzmacnia Umiejętności tej jednostki.\n- Zyskuje 1 Wrażliwości; podniesienie Progu Oszołomienia przez Wyładowanie Wstrząsu, Umiejętności lub efekty Monet rośnie o 50%
583. [Słowo kluczowe [Yurodivy_LowMorale] — nazwa] 어긋난 단결
   źródło: BattleKeywords-tkt.json :: dataList[id=Yurodivy_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Yurodivy_LowMorale]`
   limit: do 40 znaków
   EN: Broken Unity
   PL: Rozbita Jedność
584. [Słowo kluczowe [Yurodivy_LowMorale] — opis] - 사기 저하\n취약 1 얻음. 피격시, 자신의 진동 횟수 1 증가. (최대 3회)
   źródło: BattleKeywords-tkt.json :: dataList[id=Yurodivy_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nGain 1 Fragile. Gain 1 Tremor Count when hit. (3 times max)
   PL: - Niskie Morale\nZyskuje 1 Wrażliwości. Przy trafieniu zyskuje 1 Licznika Wstrząsu. (maks. 3 razy)
585. [Słowo kluczowe [Yurodivy_Panic] — nazwa] 어긋난 단결
   źródło: BattleKeywords-tkt.json :: dataList[id=Yurodivy_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Yurodivy_Panic]`
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Słowo kluczowe [Yurodivy_Panic] — opis] - 패닉\n취약 2 얻음. 피격 시, 자신의 진동 횟수 2 증가. (최대 3회)
   źródło: BattleKeywords-tkt.json :: dataList[id=Yurodivy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nGain 2 Fragile. Gain 2 Tremor Count when hit. (3 times max)
   PL: - Panika\nZyskuje 2 Wrażliwości. Przy trafieniu zyskuje 2 Licznika Wstrząsu. (maks. 3 razy)
587. [Słowo kluczowe [TimeKillerWatch] — nazwa] 시간 구제 대상
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeKillerWatch].name
   kontekst: identyfikator tagu w tekstach: `[TimeKillerWatch]`
   limit: do 40 znaków
   EN: Time Rescue Target
   PL: Cel Ratowania Czasu
588. [Słowo kluczowe [TimeKillerWatch] — opis] 시간 가속 상태동안 시간 살인마의 공격 대상이 됨.
   źródło: BattleKeywords-tkt.json :: dataList[id=TimeKillerWatch].desc
   limit: do 120 znaków
   EN: Targeted by the Time Ripper while Time Acceleration is active.
   PL: Podczas Przyspieszenia Czasu staje się celem ataków Zabójcy Czasu.
589. [Słowo kluczowe [UltraPrecisionTimeAcceleration] — nazwa] 초정밀 시간 가속
   źródło: BattleKeywords-tkt.json :: dataList[id=UltraPrecisionTimeAcceleration].name
   kontekst: identyfikator tagu w tekstach: `[UltraPrecisionTimeAcceleration]`
   limit: do 50 znaków
   EN: Microprecision Time Acceleration
   PL: Mikroprecyzyjne Przyspieszenie Czasu
590. [Słowo kluczowe [UltraPrecisionTimeAcceleration] — opis] 수치만큼 자신의 속도 최저 기본값과 최고 기본값이 증가\n진동 위력, 횟수를 부여하거나, 진동 폭발 효과를 보유한 스킬의 기본 위력 +(수치), 적에게 가하는 피해량 +(수치 X 10)%, 적에게 진동 폭발로 가하는 흐트러짐 손상 (수치 X 10)% 증가 (E.G.O 스킬 포함)\n턴 종료 시 1 감소\n수치가 1이면, 0이 되지 않고 스테이지동안 유지됨
   źródło: BattleKeywords-tkt.json :: dataList[id=UltraPrecisionTimeAcceleration].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This unit gains base Min and Max Speed by Stack\nSkills that inflict Tremor Potency, Count, or trigger Tremor Burst: gain Base Power +(Stack), deal +(Stack x 10)% damage against enemies, and when raising Stagger Thresholds via Tremor Burst, increase the amount raised by (Stack x 10)% (including E.G.O Skills)\nReduced by 1 at Turn End\nAt 1 Stack, the Stack does not drop below 0, and is maintained through the Encounter.
   PL: Zyskuje bazowe Min. i Maks. Szybkość równe stosom\nUmiejętności nakładające Siłę lub Licznik Wstrząsu albo wywołujące Wyładowanie Wstrząsu zyskują Moc Bazową +(stosy), zadają +(stosy x 10)% obrażeń wrogom, a podniesienie Progu Oszołomienia przez Wyładowanie Wstrząsu rośnie o (stosy x 10)% (w tym Umiejętności E.G.O)\nNa koniec tury maleje o 1\nPrzy 1 stosie wartość nie spada do 0 i utrzymuje się przez całą walkę

## Słowa kluczowe bitwy — BattleKeywords-twth
- plik gry: `BattleKeywords-twth.json` (opisy wyświetlane w dymkach pomocy podczas walki)

591. [Słowo kluczowe [BearClawWound] — nazwa] 찢긴 색채 [루주]
   źródło: BattleKeywords-twth.json :: dataList[id=BearClawWound].name
   kontekst: identyfikator tagu w tekstach: `[BearClawWound]`
   limit: do 40 znaków
   EN: Mauled Color [Rouge]
   PL: Rwana Barwa [Rouge]
592. [Słowo kluczowe [BearClawWound] — opis] - 최댓값 : 9\n- 피격 시 수치 3당, 출혈 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 다음 턴에 수치 4당 방어 레벨 감소 1 얻음 (최대 2)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-twth.json :: dataList[id=BearClawWound].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Bleed Potency for every 3 Stack (once per turn)\n- Turn End: Gain 1 Defense Level Down next turn for every 4 Stack (max 2)\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 9\n- Przy trafieniu zyskuje 1 Siły Krwawienia za każde 3 stosy (1 raz na turę)\n- Na koniec tury zyskuje 1 Spadek Poziomu Obrony w następnej turze za każde 4 stosy (maks. 2)\n- Na koniec tury maleje o 1
593. [Słowo kluczowe [BearClawWound] — tekst klimatyczny] ‘약지의 물감은 강화 문신과 재료가 같다는 말이 있죠. 한 번 새겨지면 색이 쉽게 빠지지 않고 지워지지 않으니까.’
   źródło: BattleKeywords-twth.json :: dataList[id=BearClawWound].flavor
   limit: do 240 znaków
   EN: 'Some say that the Ring's paint is made from the same base material as Augmentation Tattoos—they are both nigh-indelible pigments that take considerable effort to erase, let alone bleach.'
   PL: „Mówią, że farby Serdecznego mają tę samą bazę co wzmocnione tatuaże — raz utrwalone, kolor prawie nie schodzi i nie da się go zatrzeć.”
594. [Słowo kluczowe [EagleClawWound] — nazwa] 찢긴 색채 [블뢰]
   źródło: BattleKeywords-twth.json :: dataList[id=EagleClawWound].name
   kontekst: identyfikator tagu w tekstach: `[EagleClawWound]`
   limit: do 40 znaków
   EN: Mauled Color [Bleu]
   PL: Rwana Barwa [Bleu]
595. [Słowo kluczowe [EagleClawWound] — opis] - 최댓값 : 9\n- 피격 시 수치 3당, 침잠 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 수치가 5 이상이면, 정신력 5 감소\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-twth.json :: dataList[id=EagleClawWound].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Sinking Potency for every 3 Stack (once per turn)\n- Turn End: At 5+ Stack, lose 5 SP\n- Turn End: Lose 1 Stack
   PL: - Maks. stosów: 9\n- Przy trafieniu zyskuje 1 Siły Zatonięcia za każde 3 stosy (1 raz na turę)\n- Na koniec tury przy 5+ stosach traci 5 Poczytalności\n- Na koniec tury maleje o 1
596. [Słowo kluczowe [EagleClawWound] — tekst klimatyczny] ‘중지의 문신이 스스로 새겨 넣어 강화하는 것이라면, 약지의 문신은 대상에게 강제로 새겨 약화시키는 것일까?’
   źródło: BattleKeywords-twth.json :: dataList[id=EagleClawWound].flavor
   limit: do 200 znaków
   EN: 'If the Middle uses their tattoos for self-augmentation, does that make the Ring's tattoos more brands that, when forcibly applied, weaken their enemies?'
   PL: „Jeżeli Środkowy tuszuje się sam dla wzmocnienia, to tatuaże Serdecznego to raczej piętna, które nakłada się na wrogów, by ich osłabić?”
597. [Słowo kluczowe [BoldBrushstrokes] — nazwa] 과감한 터치
   źródło: BattleKeywords-twth.json :: dataList[id=BoldBrushstrokes].name
   kontekst: identyfikator tagu w tekstach: `[BoldBrushstrokes]`
   limit: do 40 znaków
   EN: Touche Hardie
   PL: Touche Hardie
598. [Słowo kluczowe [BoldBrushstrokes] — opis] - 이 효과가 있는 동안 출혈과 침잠으로 인한 체력 피해와 정신력 피해를 2배로 받음\n- 턴 종료 시 1 감소\n- 최댓값 : 1
   źródło: BattleKeywords-twth.json :: dataList[id=BoldBrushstrokes].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - While this unit has this effect, double the amount of HP and SP damage this unit takes from Bleed and Sinking\n- Turn End: Lose 1 Stack\n- Max Stack: 1
   PL: - Dopóki posiada ten efekt, podwaja obrażenia HP i Poczytalności otrzymywane od Krwawienia i Zatonięcia\n- Na koniec tury maleje o 1\n- Maks. stosów: 1
599. [Słowo kluczowe [BoldBrushstrokes] — tekst klimatyczny] “늑대의 발톱과 스라소니의 발톱, 그리고 잘 보이지 않는 여러 거북이의 발톱으로 디테일을 챙기다니… 과감하군요.”
   źródło: BattleKeywords-twth.json :: dataList[id=BoldBrushstrokes].flavor
   limit: do 160 znaków
   EN: "Wolven claws, lynx claws... and even those of turtles, so minuscule yet intricately arranged... What a bold expression."
   PL: „Pazury wilka, pazury rysia... i nawet żółwi, tak maleńkie, a tak mistycznie ułożone... Jak odważny wyraz.”
600. [Słowo kluczowe [IntenseColors] — nazwa] 강렬한 색채
   źródło: BattleKeywords-twth.json :: dataList[id=IntenseColors].name
   kontekst: identyfikator tagu w tekstach: `[IntenseColors]`
   limit: do 40 znaków
   EN: Palette Vibrante
   PL: Palette Vibrante
601. [Słowo kluczowe [IntenseColors] — opis] - 약지 소속에게 받는 피해량 +(수치x5)%\n· 대상이 약지 야수파 소속이면 효과가 강화되어, 대신 피해량 +(수치x10)%\n- 전투 시작 시 (수치+1)만큼 출혈, 침잠 얻고 출혈 횟수, 침잠 횟수 증가\n- 전투 종료 시 이 효과가 소멸되고 찢긴 색채 [루주], 찢긴 색채 [블뢰] 수치가 절반으로 감소 (소수점 버림)\n- 최댓값 : 4
   źródło: BattleKeywords-twth.json :: dataList[id=IntenseColors].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +(Stack x 5)% damage from The Ring-faction units\n· If the attacker is in The Ring School of Fauvism faction, take +(Stack x 10)% damage instead\n- Combat Start: Gain (Stack +1) Bleed, Sinking, Bleed Count, and Sinking Count\n- Combat End: This effect expires. Halve Mauled Color [Rouge] and Mauled Color [Bleu] Stacks on this unit (rounded down)\n- Max Stack: 4
   PL: - Otrzymuje +(stosy x 5)% obrażeń od Stronnictwa Serdecznego\n· Jeżeli atakujący należy do Szkoły Fowizmu Stronnictwa Serdecznego, zamiast tego +(stosy x 10)%\n- Na początku walki zyskuje (stosy +1) Krwawienia i Zatonięcia oraz ich Liczniki\n- Po zakończeniu walki ten efekt znika, a stosy Rwanej Barwy [Rouge] i Rwanej Barwy [Bleu] są zmniejszane o połowę (zaokrąglone w dół)\n- Maks. stosów: 4
602. [Słowo kluczowe [FaubismWolfMask] — nazwa] 야수파 - 마스크 드 루
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMask].name
   kontekst: identyfikator tagu w tekstach: `[FaubismWolfMask]`
   limit: do 40 znaków
   EN: Le Fauvisme - Masque de Loup
   PL: Le Fauvisme - Masque de Loup
603. [Słowo kluczowe [FaubismWolfMask] — opis] - 속도 최솟값, 최댓값 +1\n- 스킬로 부여하는 출혈, 침잠 위력 부여량 +1\n- 적중 전 대상에게 침잠이 없으면, 대상의 침잠 횟수 2 증가 (턴당 수감자별 1회)\n- 피격 직전 대상에게 출혈이 없으면, 대상의 출혈 횟수 2 증가 (턴당 수감자별 1회)
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMask].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Inflict +1 more Bleed and Sinking Potency with Skills\n- Before hitting, if target does not have Sinking, inflict +2 Sinking Count (once per Sinner per turn)\n- Before Getting Hit, if target does not have Bleed, inflict +2 Bleed Count (once per Sinner per turn)
   PL: - Min. i Maks. Szybkość +1\n- Umiejętności nakładają +1 więcej Siły Krwawienia i Zatonięcia\n- Przed trafieniem, jeżeli cel nie ma Zatonięcia, zyskuje +2 Licznika Zatonięcia (1 raz na Grzesznika na turę)\n- Przed otrzymaniem trafienia, jeżeli cel nie ma Krwawienia, zyskuje +2 Licznika Krwawienia (1 raz na Grzesznika na turę)
604. [Słowo kluczowe [FaubismWolfMask] — tekst klimatyczny] “흑수, R사 혹은 다른 짐승을 이용한 무언가들과 야수파가 무엇이 다른가 싶을 수 있죠.”\n\n“흑수가 짐승을 몸에 박아 넣은 것이라면, 야수파는 덧씌워 입는 작품으로 표현해내는 것.”
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMask].flavor
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "One might ask: What even distinguishes les Fauves from factions such as Heishous, R Corp. Packs, and more that incorporate beasts into their identities?"\n\n"A reasonable query, of that there is no doubt; to that I say we are distinguished by the transcendence of beastliness into artistic costumery, while the Heishous have mindlessly jammed it into their anatomies, disregarding their aesthetic qualities."
   PL: „Można pytać: co odróżnia les Fauves od frakcji takich jak Heishou, stada Korporacji R i innych, które wplatają bestie w swoją tożsamość?”\n\n„Słuszne pytanie; odpowiem tak: my przemieniamy dzikość w dzieło sztuki nakładane na siebie, podczas gdy Heishou bezmyślnie wpisują je we własne ciała, nie dbając o walory estetyczne.”
605. [Słowo kluczowe [FaubismWolfMaskBlooded] — nazwa] 야수파 - 마스크 드 루 앙상글랑테
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMaskBlooded].name
   kontekst: identyfikator tagu w tekstach: `[FaubismWolfMaskBlooded]`
   limit: do 60 znaków
   EN: Le Fauvisme - Masque de Loup Ensanglanté
   PL: Le Fauvisme - Masque de Loup Ensanglanté
606. [Słowo kluczowe [FaubismWolfMaskBlooded] — opis] - 피해량 +20%, 모든 코인이 파괴 불가 코인으로 변경됨\n- 속도 최솟값, 최댓값 +1\n- 스킬로 부여하는 다음 부정적인 효과의 부여량 +1\n· 출혈 위력과 횟수\n· 침잠 위력과 횟수\n- 적중 전 대상에게 침잠이 없으면, 대상의 침잠 횟수 2 증가 (턴당 수감자별 3회)\n- 피격 직전 대상에게 출혈이 없으면, 대상의 출혈 횟수 2 증가 (턴당 수감자별 3회)
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMaskBlooded].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage; convert all Coins into Unbreakable Coins\n- Min & Max Speed +1\n- Inflict +1 more of the following negative effects with Skills\n· Bleed Potency and Count\n· Sinking Potency and Count\n- Before hitting, if target does not have Sinking, inflict +2 Sinking Count (3 times per Sinner per turn)\n- Before Getting Hit, if target does not have Bleed, inflict +2 Bleed Count (3 times per Sinner per turn)
   PL: - Zadaje +20% obrażeń; wszystkie Monety stają się Niezniszczalnymi Monetami\n- Min. i Maks. Szybkość +1\n- Umiejętności nakładają +1 więcej następujących negatywnych efektów\n· Siła i Licznik Krwawienia\n· Siła i Licznik Zatonięcia\n- Przed trafieniem, jeżeli cel nie ma Zatonięcia, zyskuje +2 Licznika Zatonięcia (3 razy na Grzesznika na turę)\n- Przed otrzymaniem trafienia, jeżeli cel nie ma Krwawienia, zyskuje +2 Licznika Krwawienia (3 razy na Grzesznika na turę)
607. [Słowo kluczowe [FaubismWolfMaskBlooded] — tekst klimatyczny] 단순히 짐승 탈을 머리에 쓴다고 해서 야성이 일깨워지고 전투력이 상승하는 것은 아니다.\n탈 안에는 야수파의 물감으로 칠해진 수많은 바늘이 있어, 탈을 뒤집어쓰는 것만으로도 바늘들이 몸속으로 물감을 주입한다.\n\n약지의 물감. 결국 모든 약지는 물감을 사용할 수밖에 없다.
   źródło: BattleKeywords-twth.json :: dataList[id=FaubismWolfMaskBlooded].flavor
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One does not simply awaken the power of one's inner ferity by donning a beastly mask.\nThe interior of each headgear worn by these artists is lined with a mat of needles dipped in the Fauvist paint, which is injected into the body upon equipment. \n\nThus is the paint of the Ring—and these artists, regardless of their School, are all bound to use it.
   PL: Samo założenie maski bestii nie budzi wewnętrznej dzikości.\nWnętrze każdego nakrycia głowy tych artystów wyścieła matowina igieł zanurzonych w farbie Le Fauvisme, która wstrzykuje się do ciała przy złożeniu.\n\nTak jest z farbą Stronnictwa Serdecznego — a ci artyści, niezależnie od Szkoły, wszyscy muszą jej używać.
608. [Słowo kluczowe [PanicChangeLock] — nazwa] 패닉 변경 불가
   źródło: BattleKeywords-twth.json :: dataList[id=PanicChangeLock].name
   kontekst: identyfikator tagu w tekstach: `[PanicChangeLock]`
   limit: do 40 znaków
   EN: Fixed Panic
   PL: Zablokowana Panika
609. [Słowo kluczowe [PanicChangeLock] — opis] - 패닉 유형을 변경하는 버프 획득 시, 패닉 유형이 변경되지 않는 대신 정신력이 없는 대상에게 부여되는 효과가 부여됨
   źródło: BattleKeywords-twth.json :: dataList[id=PanicChangeLock].desc
   limit: do 240 znaków
   EN: This unit's Panic Type does not change when inflicted with an effect that changes Panic Types. Instead, this unit is inflicted with an effect that is inflicted against Non-SP Units.
   PL: - Przy zdobyciu efektu zmieniającego typ Paniki typ nie ulega zmianie; zamiast tego nakładany jest efekt stosowany wobec jednostek bez Poczytalności
610. [Słowo kluczowe [Fauvism_Lowmorale] — nazwa] 떨어지는 영감
   źródło: BattleKeywords-twth.json :: dataList[id=Fauvism_Lowmorale].name
   kontekst: identyfikator tagu w tekstach: `[Fauvism_Lowmorale]`
   limit: do 40 znaków
   EN: Faltering Inspiration
   PL: Wygasająca Inspiracja
611. [Słowo kluczowe [Fauvism_Lowmorale] — opis] - 사기 저하\n- 자신이 공격하는 대상에게 찢긴 색채가 있으면, 피해량 10% 증가\n- 취약 1 얻음
   źródło: BattleKeywords-twth.json :: dataList[id=Fauvism_Lowmorale].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If target this unit attacks has Mauled Color, deal +10% damage\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Jeżeli cel ataku ma Rwaną Barwę, zadaje +10% obrażeń\n- Zyskuje 1 Wrażliwości
612. [Słowo kluczowe [Fauvism_Panic] — nazwa] 떨어지는 영감
   źródło: BattleKeywords-twth.json :: dataList[id=Fauvism_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Fauvism_Panic]`
   (powtórzenie elementu 610 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Słowo kluczowe [Fauvism_Panic] — opis] - 패닉\n- 자신이 공격하는 대상에게 찢긴 색채가 있으면, 피해량 20% 증가\n- 취약 2 얻음
   źródło: BattleKeywords-twth.json :: dataList[id=Fauvism_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- If target this unit attacks has Mauled Color, deal +20% damage\n- Gain 2 Fragile
   PL: - Panika\n- Jeżeli cel ataku ma Rwaną Barwę, zadaje +20% obrażeń\n- Zyskuje 2 Wrażliwości
614. [Słowo kluczowe [FauvismDocent_Lowmorale] — nazwa] 충동적인 채색
   źródło: BattleKeywords-twth.json :: dataList[id=FauvismDocent_Lowmorale].name
   kontekst: identyfikator tagu w tekstach: `[FauvismDocent_Lowmorale]`
   limit: do 40 znaków
   EN: Coloriage Impulsif
   PL: Coloriage Impulsif
615. [Słowo kluczowe [FauvismDocent_Lowmorale] — opis] - 사기 저하\n- 자신이 공격하는 대상이 보유한 부정적인 효과 1개당, 피해량 +2.5% (최대 15%)\n- 취약 1 얻음
   źródło: BattleKeywords-twth.json :: dataList[id=FauvismDocent_Lowmorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +2.5% damage for every type of negative effect on target this unit attacks (max 15%)\n- Gain 1 Fragile
   PL: - Niskie Morale\n- Zadaje +2,5% obrażeń za każdy rodzaj negatywnego efektu na atakowanym celu (maks. 15%)\n- Zyskuje 1 Wrażliwości
616. [Słowo kluczowe [FauvismDocent_Panic] — nazwa] 충동적인 채색
   źródło: BattleKeywords-twth.json :: dataList[id=FauvismDocent_Panic].name
   kontekst: identyfikator tagu w tekstach: `[FauvismDocent_Panic]`
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Słowo kluczowe [FauvismDocent_Panic] — opis] - 패닉\n- 자신이 공격하는 대상이 보유한 부정적인 효과 1개당, 피해량 +5% (최대 30%)\n- 취약 2 얻음
   źródło: BattleKeywords-twth.json :: dataList[id=FauvismDocent_Panic].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +5% damage for every type of negative effect on target this unit attacks (max 30%)\n- Gain 2 Fragile
   PL: - Panika\n- Zadaje +5% obrażeń za każdy rodzaj negatywnego efektu na atakowanym celu (maks. 30%)\n- Zyskuje 2 Wrażliwości
618. [Słowo kluczowe [IndexPrescriptEnemy_0] — nazwa] 지령[쪽지] I
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_0].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptEnemy_0]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] I
   PL: Nakaz [Kartka] I
619. [Słowo kluczowe [IndexPrescriptEnemy_0] — opis] 수감자를 공격하여 적중한다.\n\n- 턴 시작 시 지령의 가호가 0~2일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_0].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Sinner.\n\n- Turn Start: At 0~2 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Grzesznika i trafia.\n\n- Na początku tury zdobywany przy Łasce Nakazu 0–2\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
620. [Słowo kluczowe [IndexPrescriptEnemy_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_0].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy przekazywane są na wiele sposobów — ich forma jest wybierana jednostronnie, niczym wyrocznia.
621. [Słowo kluczowe [IndexPrescriptEnemy_1] — nazwa] 지령[쪽지] II
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_1].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptEnemy_1]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] II
   PL: Nakaz [Kartka] II
622. [Słowo kluczowe [IndexPrescriptEnemy_1] — opis] 지령 대상을 공격하여 적중한다.\n\n- 턴 시작 시 지령의 가호가 3~5일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target.\n\n- Turn Start: At 3~5 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Atakuje Cel Nakazu i trafia.\n\n- Na początku tury zdobywany przy Łasce Nakazu 3–5\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
623. [Słowo kluczowe [IndexPrescriptEnemy_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-twth.json :: dataList[id=IndexPrescriptEnemy_1].flavor
   (powtórzenie elementu 620 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
