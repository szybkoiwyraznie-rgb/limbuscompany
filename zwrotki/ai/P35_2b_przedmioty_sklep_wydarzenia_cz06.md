# Paczka AI P35 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 6/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P35_2b_przedmioty_sklep_wydarzenia_cz06.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P35_2b_przedmioty_sklep_wydarzenia_cz06.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Wydarzenia i Przepustka: Walpu10EventText
- plik gry: `Walpu10EventText.json`

1. [Wydarzenia i Przepustka [missionConditionTitle_20089] — tekst] 쐐기 사무소 해결사들의 연계 스킬을 3회 이상 발동시키지 않고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20089].content
   limit: do 130 znaków
   EN: Complete the Reception with fewer than 3 activations of the Wedge Office Fixers' combo Skills
   PL: Ukończ Przyjęcie z mniej niż 3 aktywacjami Umiejętności łączonych Fikserów Biura Klina
2. [Wydarzenia i Przepustka [missionConditionTitle_20090] — tekst] 1회 전투에서 1턴 내에 파멜리, 파멜라를 동시에 처치한 채로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20090].content
   limit: do 130 znaków
   EN: Complete the Reception after defeating both Pameli and Pamela in the same turn in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy Pameli i Pamelę w tej samej turze w jednej walce
3. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20090] — tekst] 1회 전투에서 1턴 내에 ???, ???를 동시에 처치한 채로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20090].content
   limit: do 130 znaków
   EN: Complete the Reception after defeating both ??? and ??? in the same turn in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy ??? i ??? w tej samej turze w jednej walce
4. [Wydarzenia i Przepustka [missionConditionTitle_20091] — tekst] 1회 전투에서 고독한 해결사 효과를 받은 유나를 처치하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20091].content
   limit: do 160 znaków
   EN: Complete the Reception after defeating Yuna while Yuna is under the effects of "The Lone Fixer" effect in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy Yunę pod wpływem efektu „Samotny Fikser” w jednej walce
5. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20091] — tekst] 1회 전투에서 ??? 효과를 받은 ???를 처치하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20091].content
   limit: do 140 znaków
   EN: Complete the Reception after defeating ??? while ??? is under the effects of ??? in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy ??? pod wpływem efektu ??? w jednej walce
6. [Wydarzenia i Przepustka [missionConditionTitle_20092] — tekst] 모든 아군이 생존한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20092].content
   limit: do 120 znaków
   EN: Complete the Reception with all allies surviving
   PL: Ukończ Przyjęcie z wszystkimi sojusznikami przy życiu
7. [Wydarzenia i Przepustka [missionConditionTitle_20093] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20093].content
   limit: do 120 znaków
   EN: Complete the Reception without any ally reaching -45 SP
   PL: Ukończ Przyjęcie, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
8. [Wydarzenia i Przepustka [missionConditionTitle_20094] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20094].content
   limit: do 120 znaków
   EN: Complete all Missions in both Easy and Hard difficulties
   PL: Ukończ wszystkie misje na Poziomach Łatwym i Trudnym
9. [Wydarzenia i Przepustka [walpu_battle_3_wave] — tekst] 역사의 층
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_3_wave].content
   limit: do 120 znaków
   EN: Floor of History
   PL: Piętro Historii
10. [Wydarzenia i Przepustka [walpu_battle_name_10574] — tekst] 새벽 사무소 / 쐐기 사무소
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_name_10574].content
   limit: do 120 znaków
   EN: Dawn Office / Wedge Office
   PL: Biuro Świtu / Biuro Klina
11. [Wydarzenia i Przepustka [walpu_battle_name_10575] — tekst] 새벽 사무소 / 쐐기 사무소
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_name_10575].content
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
12. [Wydarzenia i Przepustka [walpu_battle_name_10576] — tekst] 새벽 사무소 / 쐐기 사무소
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_name_10576].content
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Wydarzenia i Przepustka [walpu_battle_name_10577] — tekst] 새벽 사무소 / 쐐기 사무소
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_name_10577].content
   (powtórzenie elementu 10 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Wydarzenia i Przepustka [walpu_battle_result_win_3] — tekst] {0} 접대 완료
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_result_win_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Reception Complete
   PL: Przyjęcie {0} ukończone
15. [Wydarzenia i Przepustka [walpu_battle_result_lose_3] — tekst] {0} 접대 실패
   źródło: Walpu10EventText.json :: dataList[id=walpu_battle_result_lose_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Reception Failed
   PL: Przyjęcie {0} nieudane
16. [Wydarzenia i Przepustka [mainui_battleresult_win_lor_stage_type_3] — tekst] 접대 완료
   źródło: Walpu10EventText.json :: dataList[id=mainui_battleresult_win_lor_stage_type_3].content
   limit: do 120 znaków
   EN: Reception Complete
   PL: Przyjęcie ukończone
17. [Wydarzenia i Przepustka [mainui_battleresult_defeat_lor_stage_type_3] — tekst] 접대 실패
   źródło: Walpu10EventText.json :: dataList[id=mainui_battleresult_defeat_lor_stage_type_3].content
   limit: do 120 znaków
   EN: Reception Failed
   PL: Przyjęcie nieudane
18. [Wydarzenia i Przepustka [Walpu10_normal_stage_name] — tekst] 초대장 보내기
   źródło: Walpu10EventText.json :: dataList[id=Walpu10_normal_stage_name].content
   limit: do 120 znaków
   EN: Send Invitation
   PL: Wyślij Zaproszenie
19. [Wydarzenia i Przepustka [Walpu10_hard_stage_name] — tekst] 초대장 보내기
   źródło: Walpu10EventText.json :: dataList[id=Walpu10_hard_stage_name].content
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
20. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_01_title] — tekst] 제10회 발푸르기스밤
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_01_title].content
   limit: do 120 znaków
   EN: The 10th Walpurgis Night
   PL: 10. Noc Walpurgii
21. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_01_title_01] — tekst] 제10회 발푸르기스밤
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_01_title_01].content
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
22. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_01_desc_01] — tekst] [제10회 발푸르기스밤]은 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_01_desc_01].content
   limit: do 190 znaków
   EN: [The 10th Walpurgis Night] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [10. Noc Walpurgii] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
23. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_02_title_01].content
   limit: do 120 znaków
   EN: Event Period
   PL: Czas trwania wydarzenia
24. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_02_desc_01] — tekst] 제10회 발푸르기스밤 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_02_desc_01].content
   limit: do 220 znaków
   EN: The duration of The 10th Walpurgis Night event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: Tutaj widnieje czas trwania wydarzenia 10. Nocy Walpurgii. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
25. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_03_title_01].content
   limit: do 120 znaków
   EN: Easy Difficulty Encounter
   PL: Walka na poziomie Łatwym
26. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다. 전투는 입장 시 엔케팔린 모듈을 소모합니다. 쉬움 난이도 전투에서는 인격의 레벨이 65보다 낮은 경우, 65로 상승합니다. 또한 인격의 동기화 단계, E.G.O의 환상해석 단계가 3단계보다 낮은 경우, 3단계로 상승합니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_03_desc_01].content
   limit: do 420 znaków
   EN: Select the door to begin the Easy difficulty Encounter. The Encounter consumes Enkephalin Module upon entry. On Easy difficulty, any Deployed Identities under Level 65 will be raised to Level 65. Also, any Deployed Identities and E.G.O under Tier 3 Uptie/Threadspinning Level will be raised to Tier 3 Uptie/Threadspinning Level.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym. Walka zużywa Moduł Enkefalinu przy wejściu. Na poziomie Łatwym Tożsamości na poziomie niższym niż 65 podnoszone są do poziomu 65. Ponadto Stopień Synchronizacji Tożsamości i Stopień Splotu Nici E.G.O niższy niż 3 podnoszony jest do 3.
27. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_03_title_02].content
   limit: do 120 znaków
   EN: Hard Difficulty Encounter
   PL: Walka na poziomie Trudnym
28. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다. 어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_03_desc_02].content
   limit: do 240 znaków
   EN: Clearing the Easy difficulty Encounter unlocks the Hard difficulty. In Hard difficulty, your Identities' current Levels, Uptie Tiers, and E.G.O Threadspinning Tiers will be reflected.
   PL: Ukończenie walki na poziomie Łatwym odblokowuje walkę na poziomie Trudnym. Na poziomie Trudnym obowiązują obecne Poziomy Tożsamości, Stopnie Synchronizacji Tożsamości i Stopnie Splotu Nici E.G.O.
29. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_04_title_01] — tekst] 지정 사서 [역사의 층]
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_04_title_01].content
   limit: do 120 znaków
   EN: Patron Librarian [Floor of History]
   PL: Wyznaczony Bibliotekarz [Piętro Historii]
30. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_04_desc_01] — tekst] 전투 편성에서 편성 순서 1번 수감자에게 ‘지정 사서 [역사의 층]’ 효과가 부여됩니다. 해당 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_04_desc_01].content
   limit: do 300 znaków
   EN: The #1 Sinner to be deployed in the Teams menu will be imbued with the "Patron Librarian [Floor of History]" effect. The Sinner with the "Patron Librarian [Floor of History]" effect will gain more Slots and other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Wyznaczony Bibliotekarz [Piętro Historii]”. Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
31. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_05_title_01] — tekst] 미션 목록
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_05_title_01].content
   limit: do 120 znaków
   EN: Missions
   PL: Lista misji
32. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_05_desc_01].content
   limit: do 170 znaków
   EN: You can enter the [Missions] page, where you can view the list of Missions to be completed during the Encounter and their rewards.
   PL: Przejdź na stronę [Listy misji], aby sprawdzić misje możliwe do wykonania w walce oraz przypisane do nich nagrody.
33. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_06_desc_01].content
   limit: do 120 znaków
   EN: You can view the Reward Exchange period in the [Missions] page.
   PL: Na stronie [Listy misji] wyświetlany jest okres odbioru nagród.
34. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_06_desc_02].content
   limit: do 120 znaków
   EN: Easy difficulty and Hard difficulty each has different sets of Missions to complete.
   PL: Poziomy Łatwy i Trudny mają osobne zestawy misji do wykonania.
35. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_06_desc_03].content
   limit: do 120 znaków
   EN: Complete these Missions and claim various rewards from the [Missions] page.
   PL: Ukończ misje, aby odebrać rozmaite nagrody z [Listy misji].
36. [Wydarzenia i Przepustka [tutorial_mainui_walpu10_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제10회 발푸르기스밤’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=tutorial_mainui_walpu10_07_desc_01].content
   limit: do 240 znaków
   EN: Even after the event fully ends, you will be able to experience the "The 10th Walpurgis Night" combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „10. Nocy Walpurgii” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].

## Wydarzenia i Przepustka: Walpu3EventText
- plik gry: `Walpu3EventText.json`

37. [Wydarzenia i Przepustka [Walpu3_reward_button] — tekst] 미션 목록
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_reward_button].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
38. [Wydarzenia i Przepustka [Walpu3_story_theater_button] — tekst] 상영관 이동
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_story_theater_button].content
   limit: do 120 znaków
   EN: To Theater
   PL: Do Teatru
39. [Wydarzenia i Przepustka [Walpu3_normal_stage] — tekst] 쉬움 난이도
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_normal_stage].content
   limit: do 120 znaków
   EN: Easy
   PL: Poziom Łatwy
40. [Wydarzenia i Przepustka [Walpu3_hard_stage] — tekst] 어려움 난이도
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_hard_stage].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
41. [Wydarzenia i Przepustka [Walpu3_normal_stage_name] — tekst] 요정들의 보살핌
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_normal_stage_name].content
   limit: do 120 znaków
   EN: The Fairies' Care
   PL: Opieka Wróżek
42. [Wydarzenia i Przepustka [Walpu3_hard_stage_name] — tekst] 포식
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_hard_stage_name].content
   limit: do 120 znaków
   EN: Predation
   PL: Pożeranie
43. [Wydarzenia i Przepustka [Walpu3_normal_stage_desc] — tekst] 요정들은 직원들을 지켜준다.\n보살핌을 받는 동안은 모든 것이 평화로워진다.
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_normal_stage_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The fairies protect our employees.\nEverything will be peaceful while you are under the fairies’ care.
   PL: Wróżki chronią pracowników.\nW czasie ich opieki wszystko staje się pokojowe.
44. [Wydarzenia i Przepustka [Walpu3_hard_stage_desc] — tekst] 장기들과 안구들은 뭔가한테 먹혀버린 듯 손실되어 있었다. 한편 요정들의 입가에는 누군가의 살점과 피가 묻어 있었다.
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_hard_stage_desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: His stomach and face were ripped off, and his eyeballs and organs were damaged as if they were eaten by something.\nMeanwhile, the fairies had someone’s blood and flesh smeared all over their mouths.
   PL: Żołądek i twarz zostały oderwane, a gałki oczne i organy utracono, jakby coś je zjadało. Tymczasem na ustach wróżek widać czyjś tłuszcz i krew.
45. [Wydarzenia i Przepustka [Walpu3_hard_stage_unlock_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu3EventText.json :: dataList[id=Walpu3_hard_stage_unlock_condition].content
   limit: do 120 znaków
   EN: Clear Easy Difficulty to Unlock
   PL: Odblokowanie po ukończeniu poziomu Łatwego
46. [Wydarzenia i Przepustka [EVENT_WALPU3_NORMAL] — tekst] 쉬움
   źródło: Walpu3EventText.json :: dataList[id=EVENT_WALPU3_NORMAL].content
   limit: do 120 znaków
   EN: Easy
   PL: Łatwy
47. [Wydarzenia i Przepustka [EVENT_WALPU3_HARD] — tekst] 어려움
   źródło: Walpu3EventText.json :: dataList[id=EVENT_WALPU3_HARD].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
48. [Wydarzenia i Przepustka [missionConditionTitle_10009] — tekst] 요정의 축제 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10009].content
   limit: do 120 znaków
   EN: Complete Suppression of Fairy Festival
   PL: Tłumienie Święta Wróżek udane
49. [Wydarzenia i Przepustka [missionConditionTitle_10010] — tekst] 10턴 내에 요정의 축제 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10010].content
   limit: do 120 znaków
   EN: Complete Suppression of Fairy Festival within 10 turns
   PL: Ukończ Tłumienie Święta Wróżek w 10 turach
50. [Wydarzenia i Przepustka [missionConditionTitle_10011] — tekst] 모든 아군이 생존한 상태로 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10011].content
   limit: do 120 znaków
   EN: Complete Suppression without any ally deaths
   PL: Ukończ Tłumienie bez śmierci żadnego sojusznika
51. [Wydarzenia i Przepustka [missionConditionTitle_10012] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10012].content
   limit: do 120 znaków
   EN: Complete Suppression without any of the allies' SP dropping to -45 SP
   PL: Ukończ Tłumienie, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
52. [Wydarzenia i Przepustka [missionConditionTitle_10013] — tekst] 역사의 층 사서가 적에게 피해를 10회 미만으로 받고 생존한 상태로 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10013].content
   limit: do 140 znaków
   EN: Complete Suppression with the Librarian of History surviving and taking less than 10 hits from the enemies
   PL: Ukończ Tłumienie, gdy Bibliotekarz Piętro Historii przeżyje, otrzymawszy mniej niż 10 trafień od wrogów
53. [Wydarzenia i Przepustka [missionConditionTitle_10014] — tekst] 1회 전투에서 여왕 요정의 양 팔 부위를 파괴하고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10014].content
   limit: do 120 znaków
   EN: Complete Suppression after breaking both of the Fairy Queen's Arms in a single Encounter
   PL: Ukończ Tłumienie, zniszczywszy obie części ramion Królowej Wróżek w jednej walce
54. [Wydarzenia i Przepustka [missionConditionTitle_10015] — tekst] 여왕 요정이 요정 덩이를 1마리도 처치하지 않고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10015].content
   limit: do 120 znaków
   EN: Complete Suppression without the Fairy Queen defeating any of the Fairy Masses
   PL: Ukończ Tłumienie, gdy Królowa Wróżek nie pokona ani jednej Zgraji Wróżek
55. [Wydarzenia i Przepustka [missionConditionTitle_10016] — tekst] 1회 전투에서 여왕 요정이 요정 덩이를 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10016].content
   limit: do 120 znaków
   EN: Let Fairy Queen defeat a Fairy Mass in a single Encounter
   PL: W jednej walce Królowa Wróżek pokonuje Zgraję Wróżek
56. [Wydarzenia i Przepustka [missionConditionTitle_10017] — tekst] 1회 전투에서 1턴에 여왕 요정이 요정 덩이를 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10017].content
   limit: do 120 znaków
   EN: Let Fairy Queen defeat a Fairy Mass in the first turn of a single Encounter
   PL: W jednej walce Królowa Wróżek pokonuje Zgraję Wróżek w pierwszej turze
57. [Wydarzenia i Przepustka [missionConditionTitle_10018] — tekst] 환상체 1개체에게 화상, 출혈, 파열, 침잠 중 1개 효과의 위력을 일정 수치 이상 부여
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10018].content
   limit: do 120 znaków
   EN: Inflict X+ Potency of (Burn, Bleed, Rupture, or Sinking) to a single Abnormality
   PL: Nałóż na jedną Anomalie określoną Siłę jednego z efektów: Podpalenie, Krwawienie, Rozdarcie albo Zatonięcie
58. [Wydarzenia i Przepustka [missionConditionTitle_10019] — tekst] 1회 전투에서 화상, 출혈, 파열, 침잠 피해로 환상체 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10019].content
   limit: do 120 znaków
   EN: Defeat an Abnormality with Burn, Bleed, Rupture, or Sinking damage in a single Encounter
   PL: Pokonaj Anomalie obrażeniami Podpalenia, Krwawienia, Rozdarcia albo Zatonięcia w jednej walce
59. [Wydarzenia i Przepustka [missionConditionTitle_10020] — tekst] 1회 전투에서 화상, 출혈, 파열, 침잠 피해로 여왕 요정 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_10020].content
   limit: do 120 znaków
   EN: Defeat the Fairy Queen with Burn, Bleed, Rupture, or Sinking damage in a single Encounter
   PL: Pokonaj Królową Wróżek obrażeniami Podpalenia, Krwawienia, Rozdarcia albo Zatonięcia w jednej walce
60. [Wydarzenia i Przepustka [missionConditionTitle_20009] — tekst] 요정의 축제 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20009].content
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Wydarzenia i Przepustka [missionConditionTitle_20010] — tekst] 10턴 내에 요정의 축제 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20010].content
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
62. [Wydarzenia i Przepustka [missionConditionTitle_20011] — tekst] 모든 아군이 생존한 상태로 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20011].content
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [Wydarzenia i Przepustka [missionConditionTitle_20012] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20012].content
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
64. [Wydarzenia i Przepustka [missionConditionTitle_20013] — tekst] 역사의 층 사서가 적에게 피해를 5회 미만으로 받고 생존한 상태로 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20013].content
   limit: do 140 znaków
   EN: Complete Suppression with Librarian of History surviving and taking less than 5 hits from the enemies
   PL: Ukończ Tłumienie, gdy Bibliotekarz Piętro Historii przeżyje, otrzymawszy mniej niż 5 trafień od wrogów
65. [Wydarzenia i Przepustka [missionConditionTitle_20014] — tekst] 1회 전투에서 여왕 요정의 양 팔 부위를 파괴하고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20014].content
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Wydarzenia i Przepustka [missionConditionTitle_20015] — tekst] 여왕 요정이 요정 덩이를 1마리도 처치하지 않고 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20015].content
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Wydarzenia i Przepustka [missionConditionTitle_20016] — tekst] 1회 전투에서 여왕 요정이 요정 덩이를 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20016].content
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
68. [Wydarzenia i Przepustka [missionConditionTitle_20017] — tekst] 1회 전투에서 1턴 안에 여왕 요정이 요정 덩이를 일정 수 이상 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20017].content
   limit: do 120 znaków
   EN: Let Fairy Queen defeat X+ Fairy Mass within a single turn of a single Encounter
   PL: W jednej walce Królowa Wróżek pokonuje określoną liczbę Zgraj Wróżek w ciągu jednej tury
69. [Wydarzenia i Przepustka [missionConditionTitle_20018] — tekst] 환상체 1개체에게 화상, 출혈, 파열, 침잠 중 1개 효과의 위력을 일정 수치 이상 부여
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20018].content
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Wydarzenia i Przepustka [missionConditionTitle_20019] — tekst] 1회 전투에서 화상, 출혈, 파열, 침잠 피해로 환상체 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20019].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
71. [Wydarzenia i Przepustka [missionConditionTitle_20020] — tekst] 1회 전투에서 화상, 출혈, 파열, 침잠 피해로 여왕 요정 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20020].content
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Wydarzenia i Przepustka [missionConditionTitle_20021] — tekst] 역사의 층 사서가 공격 스킬 1회 사용으로 동시에 환상체 일정 수 이상 처치
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_20021].content
   limit: do 120 znaków
   EN: Librarian of History defeats X+ Abnormalities with a single Attack Skill
   PL: Bibliotekarz Piętro Historii pokonuje określoną liczbę Anomalii jednym użyciem Umiejętności ataku
73. [Wydarzenia i Przepustka [missionConditionTitle_30002] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu3EventText.json :: dataList[id=missionConditionTitle_30002].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Wydarzenia i Przepustka [walpu3_reward_event_desc] — tekst] 요정의 축제를 쉬움, 어려움 난이도 전투에서 제압하며 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=walpu3_reward_event_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Suppress the Fairy Festival in 'Easy' and 'Hard' difficulties and complete the missions.\n\nEarn various rewards by clearing these missions.
   PL: Stłum Święto Wróżek w walkach na Poziomach Łatwym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
75. [Wydarzenia i Przepustka [walpu3_reward_normal_tab] — tekst] 쉬움 난이도
   źródło: Walpu3EventText.json :: dataList[id=walpu3_reward_normal_tab].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Wydarzenia i Przepustka [walpu3_reward_hard_tab] — tekst] 어려움 난이도
   źródło: Walpu3EventText.json :: dataList[id=walpu3_reward_hard_tab].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [Wydarzenia i Przepustka [walpu3_modal_yes] — tekst] 예
   źródło: Walpu3EventText.json :: dataList[id=walpu3_modal_yes].content
   limit: do 120 znaków
   EN: Yes
   PL: Tak
78. [Wydarzenia i Przepustka [walpu3_modal_no] — tekst] 아니오
   źródło: Walpu3EventText.json :: dataList[id=walpu3_modal_no].content
   limit: do 120 znaków
   EN: No
   PL: Nie
79. [Wydarzenia i Przepustka [walpu_modal_enterStage_10555] — tekst] 요정의 축제의 책 속으로 들어가시겠습니까?
   źródło: Walpu3EventText.json :: dataList[id=walpu_modal_enterStage_10555].content
   limit: do 120 znaków
   EN: Will you enter the book of Fairy Festival?
   PL: Wkroczyć do księgi Święta Wróżek?
80. [Wydarzenia i Przepustka [walpu_modal_enterStage_10556] — tekst] 요정의 축제의 책 속으로 들어가시겠습니까?
   źródło: Walpu3EventText.json :: dataList[id=walpu_modal_enterStage_10556].content
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
81. [Wydarzenia i Przepustka [walpu_battle_turn] — tekst] 제 {0}막
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_turn].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Scene {0}
   PL: Scena {0}
82. [Wydarzenia i Przepustka [walpu_battle_1_wave] — tekst] 역사의 층 - {0}번째 무대
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_1_wave].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Floor of History - Act {0}
   PL: Piętro Historii — akt {0}
83. [Wydarzenia i Przepustka [walpu_battle_name_10555] — tekst] 요정의 축제
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_name_10555].content
   limit: do 120 znaków
   EN: Fairy Festival
   PL: Święto Wróżek
84. [Wydarzenia i Przepustka [walpu_battle_name_10556] — tekst] 요정의 축제
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_name_10556].content
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
85. [Wydarzenia i Przepustka [walpu_battle_name_10557] — tekst] 요정의 축제
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_name_10557].content
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Wydarzenia i Przepustka [walpu_battle_result_win] — tekst] {0} 제압 성공
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_result_win].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Suppression of {0} Complete
   PL: Tłumienie {0} udane
87. [Wydarzenia i Przepustka [walpu_battle_result_lose] — tekst] {0} 제압 실패
   źródło: Walpu3EventText.json :: dataList[id=walpu_battle_result_lose].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Suppression of {0} Failed
   PL: Tłumienie {0} nieudane
88. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_01_title] — tekst] 제3회 발푸르기스밤 - 어느 도서관의 어떤 책 속으로
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_01_title].content
   limit: do 120 znaków
   EN: The 3rd Walpurgis Night - Into a Certain Library's Book
   PL: 3. Noc Walpurgii — Do pewnej księgi pewnej biblioteki
89. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_01_title_01] — tekst] 제3회 발푸르기스밤 - 어느 도서관의 어떤 책 속으로
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_01_title_01].content
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_01_desc_01] — tekst] [제3회 발푸르기스밤 - 어느 도서관의 어떤 책 속으로]는 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_01_desc_01].content
   limit: do 230 znaków
   EN: [The 3rd Walpurgis Night - Into a Certain Library's Book] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [3. Noc Walpurgii — Do pewnej księgi pewnej biblioteki] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
91. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_02_title_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_02_desc_01] — tekst] [제3회 발푸르기스밤 - 어느 도서관의 어떤 책 속으로] 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_02_desc_01].content
   limit: do 260 znaków
   EN: The duration of The 3rd Walpurgis Night - Into a Certain Library's Book event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: [3. Noc Walpurgii — Do pewnej księgi pewnej biblioteki] — tu widnieje czas trwania wydarzenia. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
93. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_03_title_01].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다.\n제 3회 발푸르기스의 밤 이벤트 기간 도중에는 전투 입장 시 엔케팔린 모듈을 소모합니다.\n쉬움 난이도 전투에서는 인격의 레벨이 45레벨보다 낮은 경우, 45레벨로 상승합니다.\n또한 인격의 동기화 단계가 3단계보다 낮은 경우,\n3단계로 상승합니다.\nE.G.O의 환상 해석 단계는 현재 육성 상태가 반영됩니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_03_desc_01].content
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the door to begin the Easy difficulty Encounter.\nDuring the 3rd Walpurgis Night Event period, the Encounter consumes an Enkephalin Module upon entry.\nOn Easy difficulty, any Deployed Identities under Level 45 will be raised to Level 45.\nAlso, any Deployed Identities under Tier 3 Uptie Level will be raised to Tier 3 Uptie Level.\nHowever, your current E.G.O Threadspinning Tiers will be reflected.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym.\nW okresie 3. Nocy Walpurgii walka zużywa Moduł Enkefalinu przy wejściu.\nNa poziomie Łatwym Tożsamości na poziomie niższym niż 45 podnoszone są do poziomu 45.\nPonadto Stopień Synchronizacji Tożsamości niższy niż 3\npodnoszony jest do 3.\nStopień Splotu Nici E.G.O pozostaje bez zmian.
95. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_03_title_02].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
96. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다.\n어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상 해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_03_desc_02].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the Easy difficulty Encounter unlocks the Hard difficulty.\nIn Hard difficulty, your Identities' current Levels, Uptie Tiers, and E.G.O Threadspinning Tiers will be reflected.
   PL: Ukończenie walki na poziomie Łatwym odblokowuje walkę na poziomie Trudnym.\nNa poziomie Trudnym obowiązują obecne Poziomy Tożsamości, Stopnie Synchronizacji Tożsamości i Stopnie Splotu Nici E.G.O.
97. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_04_title_01] — tekst] 역사의 층 사서 효과
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_04_title_01].content
   limit: do 120 znaków
   EN: Librarian of History Effect
   PL: Efekt Bibliotekarza Piętro Historii
98. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_04_desc_01] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘역사의 층 사서’ 효과가 부여됩니다. ‘역사의 층 사서’ 효과는 쉬움/어려움 난이도에 따라 효과가 달라지며, 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_04_desc_01].content
   limit: do 350 znaków
   EN: The #1 Sinner to be Deployed in the Teams menu will be imbued with the 'Librarian of History' effect. The effects of 'Librarian of History' differs between Easy/Hard difficulties. Sinner imbued with this effect will gain more Slots and various other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Bibliotekarz Piętro Historii”. Efekt różni się na poziomach Łatwym i Trudnym; Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
99. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_05_title_01] — tekst] 미션 목록
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_05_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
100. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_05_desc_01].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_06_desc_01].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
102. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_06_desc_02].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
103. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_06_desc_03].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Wydarzenia i Przepustka [tutorial_mainui_27_walpu3_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제3회 발푸르기스밤 - 어느 도서관의 어떤 책 속으로’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu3EventText.json :: dataList[id=tutorial_mainui_27_walpu3_07_desc_01].content
   limit: do 280 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 3rd Walpurgis Night - Into a Certain Library's Book' combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „3. Nocy Walpurgii — Do pewnej księgi pewnej biblioteki” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].
105. [Wydarzenia i Przepustka [walpu3_not_progress_event_date] — tekst] 이벤트 기간 종료
   źródło: Walpu3EventText.json :: dataList[id=walpu3_not_progress_event_date].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Zakończenie okresu wydarzenia

## Wydarzenia i Przepustka: Walpu4EventText
- plik gry: `Walpu4EventText.json`

106. [Wydarzenia i Przepustka [Walpu4_event_desc] — tekst] 자색 정오의 시련 쉬움, 어려움 난이도 전투에서 시련을 제압하며 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=Walpu4_event_desc].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Suppress Noon of Violet entities in 'Normal' and 'Hard' difficulties from the Noon of Violet Ordeal.\n\nEarn various rewards by clearing these missions.
   PL: Stłum istoty Próby Fioletowego Południa na Poziomach Łatwym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
107. [Wydarzenia i Przepustka [LobotomyStartTypo_Title_2] — tekst] 자색 여명의 시련
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Title_2].content
   limit: do 120 znaków
   EN: The Dawn of Violet
   PL: Próba Fioletowego Świtu
108. [Wydarzenia i Przepustka [LobotomyStartTypo_Name_2] — tekst] 이해의 과실
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Name_2].content
   limit: do 120 znaków
   EN: Fruit of Understanding
   PL: Owoc Zrozumienia
109. [Wydarzenia i Przepustka [LobotomyStartTypo_Desc_2] — tekst] 이해를 벗어난 것을 이해하기 위해 바라보며 꿈꾼다.
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Desc_2].content
   limit: do 120 znaków
   EN: To gain an understanding of what is incomprehensible, they dream, staring.
   PL: Aby pojąć to, czego pojąć się nie da, śnią, patrząc.
110. [Wydarzenia i Przepustka [LobotomyStartTypo_KillCountTitle_2] — tekst] 제압 현황
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_KillCountTitle_2].content
   limit: do 120 znaków
   EN: Suppression Status
   PL: Stan Tłumienia
111. [Wydarzenia i Przepustka [LobotomyClearTypo_Title_2] — tekst] 자색 여명의 시련
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Title_2].content
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Wydarzenia i Przepustka [LobotomyClearTypo_Name_2] — tekst] 이해의 과실
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Name_2].content
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Wydarzenia i Przepustka [missionConditionTitle_10026] — tekst] 자색 여명의 시련 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10026].content
   limit: do 120 znaków
   EN: Complete Suppression of the Dawn of Violet
   PL: Tłumienie Próby Fioletowego Świtu udane
114. [Wydarzenia i Przepustka [missionConditionTitle_10027] — tekst] 7턴 안에 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10027].content
   limit: do 120 znaków
   EN: Complete Suppression in 7 turns
   PL: Ukończ Tłumienie w 7 turach
115. [Wydarzenia i Przepustka [missionConditionTitle_10028] — tekst] 교육팀 팀장이 1회 전투에서 이해의 과실을 3개체 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10028].content
   limit: do 120 znaków
   EN: Training Team Captain defeats 3 Fruits of Understanding in an Encounter
   PL: Kapitan Zespołu Szkoleniowego pokonuje 3 Owoców Zrozumienia w jednej walce
116. [Wydarzenia i Przepustka [missionConditionTitle_10029] — tekst] 이해의 과실이 단 한 번도 ‘붕괴’ 스킬을 사용하지 못하게 하고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10029].content
   limit: do 120 znaków
   EN: Complete Suppression before Fruit of Understanding uses the 'Decay' Skill
   PL: Ukończ Tłumienie, nie pozwalając Owocowi Zrozumienia ani razu użyć Umiejętności „Rozpad”
117. [Wydarzenia i Przepustka [missionConditionTitle_10030] — tekst] 한 턴에 적 하나에게 화상(특수 화상), 출혈, 파열, 침잠(특수 침잠) 피해를 8회 이상 입히고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10030].content
   limit: do 160 znaków
   EN: Complete Suppression after dealing (Unique)Burn, Bleed, Rupture, or (Unique)Sinking damage 8+ times to a single enemy
   PL: Ukończ Tłumienie, zadając jednemu wrogowi w jednej turze Podpalenie (specjalne), Krwawienie, Rozdarcie albo Zatonięcie (specjalne) 8 razy lub więcej
118. [Wydarzenia i Przepustka [missionConditionTitle_10031] — tekst] 모든 아군이 생존한 상태로 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10031].content
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Wydarzenia i Przepustka [missionConditionTitle_10032] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10032].content
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
120. [Wydarzenia i Przepustka [missionConditionTitle_10033] — tekst] 1회 전투에서 현재 체력이 최대 체력의 80% 이상인 적을 스킬 1개로 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10033].content
   limit: do 120 znaków
   EN: In a single Encounter, defeat an enemy with 80%+ HP with a single Skill
   PL: W jednej walce pokonaj wroga z HP 80% lub wyższym pojedynczą Umiejętnością
121. [Wydarzenia i Przepustka [missionConditionTitle_10034] — tekst] 교육팀 팀장이 적의 공격 스킬로 피해를 10회 미만으로 받고, 생존한 상태로 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10034].content
   limit: do 150 znaków
   EN: Complete Suppression with Training Team Captain surviving and taking less than 10 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy Kapitan Zespołu Szkoleniowego przeżyje, otrzymawszy mniej niż 10 trafień Umiejętnościami ataku wroga
122. [Wydarzenia i Przepustka [missionConditionTitle_10035] — tekst] 한 턴에 적 하나에게 8종류 이상의 부정적인 효과 부여
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10035].content
   limit: do 120 znaków
   EN: In a single turn, inflict 8+ different types of negative effects on a single enemy
   PL: Nałóż w jednej turze 8 lub więcej różnych negatywnych efektów na jednego wroga
123. [Wydarzenia i Przepustka [missionConditionTitle_10036] — tekst] 한 턴에 적을 2개체 이상 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_10036].content
   limit: do 120 znaków
   EN: Defeat 2+ enemies in a single turn
   PL: Pokonaj 2 lub więcej wrogów w jednej turze
124. [Wydarzenia i Przepustka [missionConditionTitle_20026] — tekst] 자색 정오의 시련 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20026].content
   limit: do 120 znaków
   EN: Complete Suppression of the Noon of Violet
   PL: Tłumienie Próby Fioletowego Południa udane
125. [Wydarzenia i Przepustka [missionConditionTitle_20027] — tekst] 12턴 안에 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20027].content
   limit: do 120 znaków
   EN: Complete Suppression in 12 turns
   PL: Ukończ Tłumienie w 12 turach
126. [Wydarzenia i Przepustka [missionConditionTitle_20028] — tekst] 교육팀 팀장이 1회 전투에서 이해의 과실을 3개체 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20028].content
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Wydarzenia i Przepustka [missionConditionTitle_20029] — tekst] 이해의 과실이 단 한 번도 ‘붕괴’ 스킬을 사용하지 못하게 하고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20029].content
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Wydarzenia i Przepustka [missionConditionTitle_20030] — tekst] 한 턴에 적 하나에게 화상(특수 화상), 출혈, 파열, 침잠(특수 침잠) 피해를 18회 이상 입히고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20030].content
   limit: do 160 znaków
   EN: Complete Suppression after dealing (Unique)Burn, Bleed, Rupture, or (Unique)Sinking damage 18+ times to a single enemy
   PL: Ukończ Tłumienie, zadając jednemu wrogowi w jednej turze Podpalenie (specjalne), Krwawienie, Rozdarcie albo Zatonięcie (specjalne) 18 razy lub więcej
129. [Wydarzenia i Przepustka [missionConditionTitle_20031] — tekst] 모든 아군이 생존한 상태로 전투 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20031].content
   limit: do 120 znaków
   EN: Complete Suppression without any ally deaths
   PL: Ukończ Tłumienie walki bez śmierci żadnego sojusznika
130. [Wydarzenia i Przepustka [missionConditionTitle_20032] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20032].content
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Wydarzenia i Przepustka [missionConditionTitle_20033] — tekst] 1회 전투에서 현재 체력이 최대 체력의 80% 이상인 적을 스킬 1개로 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20033].content
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Wydarzenia i Przepustka [missionConditionTitle_20034] — tekst] 교육팀 팀장이 적의 공격 스킬로 피해를 5회 미만으로 받고, 생존한 상태로 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20034].content
   limit: do 150 znaków
   EN: Complete Suppression with Training Team Captain surviving and taking less than 5 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy Kapitan Zespołu Szkoleniowego przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
133. [Wydarzenia i Przepustka [missionConditionTitle_20035] — tekst] 한 턴에 적 하나에게 6종류 이상의 부정적인 효과 부여
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20035].content
   limit: do 120 znaków
   EN: In a single turn, inflict 6+ different types of negative effects on a single enemy
   PL: Nałóż w jednej turze 6 lub więcej różnych negatywnych efektów na jednego wroga
134. [Wydarzenia i Przepustka [missionConditionTitle_20036] — tekst] 한 턴에 적을 2개체 이상 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20036].content
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Wydarzenia i Przepustka [missionConditionTitle_20037] — tekst] 사랑을 주소서의 몸통을 제외한 모든 부위를 파괴하고 제압 성공
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20037].content
   limit: do 120 znaków
   EN: Complete Suppression after breaking every Part of Grant Us Love except its Body
   PL: Ukończ Tłumienie, zniszczywszy wszystkie części Obdarz Nas Miłością poza jej Korpusem
136. [Wydarzenia i Przepustka [missionConditionTitle_20038] — tekst] 교육팀 팀장이 사랑을 주소서 처치
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_20038].content
   limit: do 120 znaków
   EN: Defeat Grant Us Love with Training Team Captain
   PL: Kapitan Zespołu Szkoleniowego pokonuje Obdarz Nas Miłością
137. [Wydarzenia i Przepustka [missionConditionTitle_30003] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu4EventText.json :: dataList[id=missionConditionTitle_30003].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Wydarzenia i Przepustka [LobotomyClearTypo_Desc_2] — tekst] 이해하기 위해 기울이지 않는다. 그저 행할 뿐이다.
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Desc_2].content
   limit: do 120 znaków
   EN: They complied with nothing in their bid to understand. They simply did so.
   PL: Nie wysiłku dla zrozumienia. Po prostu działają.
139. [Wydarzenia i Przepustka [walpu4_hard_stage_unlock_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu4EventText.json :: dataList[id=walpu4_hard_stage_unlock_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Wydarzenia i Przepustka [LobotomyStartTypo_Title_3] — tekst] 자색 정오의 시련
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Title_3].content
   limit: do 120 znaków
   EN: The Noon of Violet
   PL: Próba Fioletowego Południa
141. [Wydarzenia i Przepustka [LobotomyStartTypo_Name_3] — tekst] 사랑을 주소서
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Name_3].content
   limit: do 120 znaków
   EN: Grant Us Love
   PL: Obdarz Nas Miłością
142. [Wydarzenia i Przepustka [LobotomyStartTypo_Desc_3] — tekst] 하릴없이 미약한 행동만이 우리에게 들렸으며, 그들에게 자비와 사랑을 구했다.
   źródło: Walpu4EventText.json :: dataList[id=LobotomyStartTypo_Desc_3].content
   limit: do 140 znaków
   EN: We could only hear the weakest and faintest of their acts. We sought for love and compassion from them.
   PL: Słyszaliśmy tylko ich nędzne, śladowe czyny — błagaliśmy o ich litość i miłość.
143. [Wydarzenia i Przepustka [LobotomyClearTypo_Title_3] — tekst] 자색 정오의 시련
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Title_3].content
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [Wydarzenia i Przepustka [LobotomyClearTypo_Name_3] — tekst] 사랑을 주소서
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Name_3].content
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Wydarzenia i Przepustka [LobotomyClearTypo_Desc_3] — tekst] 이해하지 못함과 더불어 그들 또한 우리를 이해하지 못하리라.
   źródło: Walpu4EventText.json :: dataList[id=LobotomyClearTypo_Desc_3].content
   limit: do 120 znaków
   EN: We cannot understand them, nor will they understand us.
   PL: Nie rozumiemy ich — a oni i tak nie zrozumieją nas.
146. [Wydarzenia i Przepustka [KillCount_Title_2] — tekst] 자색 여명의 시련
   źródło: Walpu4EventText.json :: dataList[id=KillCount_Title_2].content
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Wydarzenia i Przepustka [KillCount_Title_1] — tekst] 녹색 여명의 시련
   źródło: Walpu4EventText.json :: dataList[id=KillCount_Title_1].content
   limit: do 120 znaków
   EN: The Dawn of Green
   PL: Próba Zielonego Świtu
148. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_01_title] — tekst] 제4회 발푸르기스밤 - 자색 정오의 시련
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_01_title].content
   limit: do 120 znaków
   EN: The Noon of Violet Event
   PL: 4. Noc Walpurgii — Próba Fioletowego Południa
149. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_01_title_01] — tekst] 제4회 발푸르기스밤 - 자색 정오의 시련
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_01_title_01].content
   limit: do 120 znaków
   EN: The 4th Walpurgis Night - The Noon of Violet
   PL: 4. Noc Walpurgii — Próba Fioletowego Południa
150. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_01_desc_01] — tekst] [제4회 발푸르기스밤 - 자색 정오의 시련]은 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_01_desc_01].content
   limit: do 220 znaków
   EN: [The 4th Walpurgis Night - The Noon of Violet] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [4. Noc Walpurgii — Próba Fioletowego Południa] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
151. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_02_title_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_02_desc_01] — tekst] 제4회 발푸르기스밤 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_02_desc_01].content
   limit: do 220 znaków
   EN: The duration of The 4th Walpurgis Night event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: Tutaj widnieje czas trwania wydarzenia 4. Nocy Walpurgii. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
153. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_03_title_01].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다.\n제 4회 발푸르기스의 밤 이벤트 기간 도중에는 전투 입장 시 엔케팔린 모듈을 소모합니다.\n쉬움 난이도 전투에서는 인격의 레벨이 45레벨보다 낮은 경우, 45레벨로 상승합니다.\n또한 인격의 동기화 단계, E.G.O의 환상 해석 단계가 3단계보다 낮은 경우, 3단계로 상승합니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_03_desc_01].content
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the door to begin the Easy difficulty Encounter.\nDuring the 4th Walpurgis Night Event period, the Encounter consumes an Enkephalin Module upon entry. \nOn Easy difficulty, any Deployed Identities under Level 45 will be raised to Level 45.\nAlso, any Deployed Identities and E.G.O under Tier 3 Uptie/Threadspinning Level will be raised to Tier 3 Uptie Level.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym.\nW okresie 4. Nocy Walpurgii walka zużywa Moduł Enkefalinu przy wejściu.\nNa poziomie Łatwym Tożsamości na poziomie niższym niż 45 podnoszone są do poziomu 45.\nPonadto Stopień Synchronizacji Tożsamości i Stopień Splotu Nici E.G.O niższy niż 3 podnoszony jest do 3.
155. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_03_title_02].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다. 어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_03_desc_02].content
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_04_title_01] — tekst] 교육팀 팀장 효과
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_04_title_01].content
   limit: do 120 znaków
   EN: Training Team Captain Effects
   PL: Efekty Kapitana Zespołu Szkoleniowego
158. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_04_desc_01] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘교육팀 팀장’ 효과가 부여됩니다. ‘교육팀 팀장’ 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_04_desc_01].content
   limit: do 260 znaków
   EN: The #1 Sinner to be deployed in the Teams menu will be imbued with the 'Training Team Captain' effect. The Sinner with the 'Training Team Captain' effect will gain more Slots and other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Kapitan Zespołu Szkoleniowego”. Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
159. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_05_title_01] — tekst] 미션 목록
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_05_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_05_desc_01].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_06_desc_01].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_06_desc_02].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_06_desc_03].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Wydarzenia i Przepustka [tutorial_mainui_walpu4_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제4회 발푸르기스밤 - 자색 정오의 시련’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu4EventText.json :: dataList[id=tutorial_mainui_walpu4_07_desc_01].content
   limit: do 270 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 4th Walpurgis Night - The Noon of Violet' combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „4. Nocy Walpurgii — Próby Fioletowego Południa” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].

## Wydarzenia i Przepustka: Walpu5EventText
- plik gry: `Walpu5EventText.json`

165. [Wydarzenia i Przepustka [Walpu5_reward_button] — tekst] 미션 목록
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_reward_button].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Wydarzenia i Przepustka [Walpu5_story_theater_button] — tekst] 상영관 이동
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_story_theater_button].content
   (powtórzenie elementu 38 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [Wydarzenia i Przepustka [Walpu5_normal_stage] — tekst] 쉬움 난이도 입장
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_normal_stage].content
   limit: do 120 znaków
   EN: Enter Easy Difficulty
   PL: Wejdź (Łatwy)
168. [Wydarzenia i Przepustka [Walpu5_hard_stage] — tekst] 어려움 난이도 입장
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_hard_stage].content
   limit: do 120 znaków
   EN: Enter Hard Difficulty
   PL: Wejdź (Trudny)
169. [Wydarzenia i Przepustka [Walpu5_normal_stage_name] — tekst] 톱니교단의 책
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_normal_stage_name].content
   limit: do 120 znaków
   EN: Book of the Church of Gears
   PL: Księga Kościoła Trybów
170. [Wydarzenia i Przepustka [Walpu5_hard_stage_name] — tekst] 톱니교단의 책
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_hard_stage_name].content
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Wydarzenia i Przepustka [Walpu5_hard_stage_unlock_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_hard_stage_unlock_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Wydarzenia i Przepustka [EVENT_Walpu5_NORMAL] — tekst] 쉬움
   źródło: Walpu5EventText.json :: dataList[id=EVENT_Walpu5_NORMAL].content
   (powtórzenie elementu 46 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Wydarzenia i Przepustka [EVENT_Walpu5_HARD] — tekst] 어려움
   źródło: Walpu5EventText.json :: dataList[id=EVENT_Walpu5_HARD].content
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Wydarzenia i Przepustka [missionConditionTitle_10037] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10037].content
   limit: do 120 znaków
   EN: Defeat a Gear Worshipper in an Encounter
   PL: Pokonaj Wyznawcę Kościoła Trybów w jednej walce
175. [Wydarzenia i Przepustka [missionConditionTitle_10038] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10038].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Wydarzenia i Przepustka [missionConditionTitle_10039] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10039].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Wydarzenia i Przepustka [missionConditionTitle_10040] — tekst] 1회 전투에서 저돌적인 톱니 광신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10040].content
   limit: do 120 znaków
   EN: Defeat an Aggressive Gear Fanatic in an Encounter
   PL: Pokonaj Agresywnego Fanatyka Trybów w jednej walce
178. [Wydarzenia i Przepustka [missionConditionTitle_10041] — tekst] 모든 아군이 생존한 상태로 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10041].content
   limit: do 120 znaków
   EN: Complete Encounter without any ally deaths
   PL: Ukończ Tłumienie bez śmierci żadnego sojusznika
179. [Wydarzenia i Przepustka [missionConditionTitle_10042] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10042].content
   limit: do 120 znaków
   EN: Complete Encounter without any of the allies' SP dropping to -45 SP
   PL: Ukończ Tłumienie, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
180. [Wydarzenia i Przepustka [missionConditionTitle_10043] — tekst] '사격 준비 만전' 효과를 보유한 아군이 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10043].content
   limit: do 120 znaków
   EN: Defeat a Gear Worshipper with an ally with the 'Ready to Fire' effect in an Encounter
   PL: W jednej walce sojusznik z efektem „Pełna Gotowość do Strzału” pokonuje Wyznawcę Kościoła Trybów
181. [Wydarzenia i Przepustka [missionConditionTitle_10044] — tekst] '사격 준비 만전' 효과를 보유한 아군이 적의 공격 스킬로 피해를 5회 미만으로 받고, 생존한 상태로 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10044].content
   limit: do 170 znaków
   EN: Complete the Encounter with an ally with the 'Ready to Fire' effect surviving and taking less than 5 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy sojusznik z efektem „Pełna Gotowość do Strzału” przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
182. [Wydarzenia i Przepustka [missionConditionTitle_10045] — tekst] 공격 스킬 1회 사용으로 톱니교단 신도 4명 이상 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10045].content
   limit: do 120 znaków
   EN: Defeat 4+ Gear Worshippers with a single Attack Skill
   PL: Pokonaj 4 lub więcej Wyznawców Kościoła Trybów jednym użyciem Umiejętności ataku
183. [Wydarzenia i Przepustka [missionConditionTitle_10046] — tekst] 현재 체력이 최대 체력의 80% 이상인 저돌적인 톱니 광신도를 공격 스킬 1회 사용으로 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_10046].content
   limit: do 120 znaków
   EN: Defeat an Aggressive Gear Fanatic with 80%+ HP with a single Attack Skill
   PL: Pokonaj Agresywnego Fanatyka Trybów z HP 80% lub wyższym jednym użyciem Umiejętności ataku
184. [Wydarzenia i Przepustka [missionConditionTitle_20039] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20039].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Wydarzenia i Przepustka [missionConditionTitle_20040] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20040].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Wydarzenia i Przepustka [missionConditionTitle_20041] — tekst] 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20041].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Wydarzenia i Przepustka [missionConditionTitle_20042] — tekst] 1회 전투에서 저돌적인 톱니 광신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20042].content
   (powtórzenie elementu 177 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Wydarzenia i Przepustka [missionConditionTitle_20043] — tekst] 모든 아군이 생존한 상태로 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20043].content
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Wydarzenia i Przepustka [missionConditionTitle_20044] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20044].content
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Wydarzenia i Przepustka [missionConditionTitle_20045] — tekst] 연기 위력이 10에 도달한 아군 없이 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20045].content
   limit: do 120 znaków
   EN: Complete Encounter without any allies reaching 10 Smoke Potency
   PL: Ukończ Tłumienie bez sojuszników z Siłą Dymu 10 lub wyższą
191. [Wydarzenia i Przepustka [missionConditionTitle_20046] — tekst] '사격 준비 만전' 효과를 보유한 아군이 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20046].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Wydarzenia i Przepustka [missionConditionTitle_20047] — tekst] '사격 준비 만전' 효과를 보유한 아군이 1회 전투에서 톱니교단 신도 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20047].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Wydarzenia i Przepustka [missionConditionTitle_20048] — tekst] '사격 준비 만전' 효과를 보유한 아군이 적의 공격 스킬로 피해를 3회 미만으로 받고, 생존한 상태로 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20048].content
   limit: do 170 znaków
   EN: Complete the Encounter with an ally with the 'Ready to Fire' effect surviving and taking less than 3 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy sojusznik z efektem „Pełna Gotowość do Strzału” przeżyje, otrzymawszy mniej niż 3 trafienia Umiejętnościami ataku wroga
194. [Wydarzenia i Przepustka [missionConditionTitle_20049] — tekst] 공격 스킬 1회 사용으로 톱니교단 신도 7명 이상 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20049].content
   limit: do 120 znaków
   EN: Defeat 7+ Gear Worshippers with a single Attack Skill
   PL: Pokonaj 7 lub więcej Wyznawców Kościoła Trybów jednym użyciem Umiejętności ataku
195. [Wydarzenia i Przepustka [missionConditionTitle_20050] — tekst] 현재 체력이 최대 체력의 80% 이상인 저돌적인 톱니 광신도를 공격 스킬 1회 사용으로 처치
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20050].content
   (powtórzenie elementu 183 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Wydarzenia i Przepustka [missionConditionTitle_20051] — tekst] 1회 전투에서 공격 스킬 1개로 가한 크리티컬 피해량 300 이상 달성
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_20051].content
   limit: do 120 znaków
   EN: Deal 300+ Crit Damage with a single Attack Skill in an Encounter
   PL: W jednej walce zadaj 300 lub więcej obrażeń krytycznych pojedynczą Umiejętnością ataku
197. [Wydarzenia i Przepustka [missionConditionTitle_30004] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu5EventText.json :: dataList[id=missionConditionTitle_30004].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Wydarzenia i Przepustka [Walpu5_reward_event_desc] — tekst] 톱니교단 신도를 쉬움, 어려움 난이도 전투에서 처치하며 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_reward_event_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Defeat the Gear Worshippers in 'Easy' and 'Hard' difficulties and complete the missions.\n\nEarn various rewards by clearing these missions.
   PL: Pokonaj Wyznawców Kościoła Trybów w walkach na Poziomach Łatwym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
199. [Wydarzenia i Przepustka [Walpu5_reward_normal_tab] — tekst] 쉬움 난이도
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_reward_normal_tab].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Wydarzenia i Przepustka [Walpu5_reward_hard_tab] — tekst] 어려움 난이도
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_reward_hard_tab].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Wydarzenia i Przepustka [Walpu5_modal_yes] — tekst] 예
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_modal_yes].content
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [Wydarzenia i Przepustka [Walpu5_modal_no] — tekst] 아니오
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_modal_no].content
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Wydarzenia i Przepustka [walpu_modal_enterStage_10562] — tekst] 톱니교단의 책 속으로 들어가시겠습니까?
   źródło: Walpu5EventText.json :: dataList[id=walpu_modal_enterStage_10562].content
   limit: do 120 znaków
   EN: Will you enter the book of The Church of Gears?
   PL: Wkroczyć do księgi Kościoła Trybów?
204. [Wydarzenia i Przepustka [walpu_modal_enterStage_10563] — tekst] 톱니교단의 책 속으로 들어가시겠습니까?
   źródło: Walpu5EventText.json :: dataList[id=walpu_modal_enterStage_10563].content
   (powtórzenie elementu 203 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Wydarzenia i Przepustka [walpu_battle_2_wave] — tekst] 톱니교단 예배당
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_2_wave].content
   limit: do 120 znaków
   EN: The Church of Gears Oratory
   PL: Oratorium Kościoła Trybów
206. [Wydarzenia i Przepustka [walpu_battle_name_10562] — tekst] 톱니교단 신도
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_name_10562].content
   limit: do 120 znaków
   EN: Gear Worshipper
   PL: Wyznawca Kościoła Trybów
207. [Wydarzenia i Przepustka [walpu_battle_name_10563] — tekst] 톱니교단 신도
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_name_10563].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Wydarzenia i Przepustka [walpu_battle_name_10564] — tekst] 톱니교단 신도
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_name_10564].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_01_title] — tekst] 제5회 발푸르기스밤 - 탄환이 찍은 마침표
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_01_title].content
   limit: do 120 znaków
   EN: The 5th Walpurgis Night - Full-Stopped by a Bullet
   PL: 5. Noc Walpurgii — Kropka Postawiona Kulą
210. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_01_title_01] — tekst] 제5회 발푸르기스밤 - 탄환이 찍은 마침표
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_01_title_01].content
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_01_desc_01] — tekst] [제5회 발푸르기스밤 - 탄환이 찍은 마침표]는 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_01_desc_01].content
   limit: do 220 znaków
   EN: [The 5th Walpurgis Night - Full-Stopped by a Bullet] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [5. Noc Walpurgii — Kropka Postawiona Kulą] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
212. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_02_title_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_02_desc_01] — tekst] [제5회 발푸르기스밤 - 탄환이 찍은 마침표] 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_02_desc_01].content
   limit: do 220 znaków
   EN: The duration of The 5th Walpurgis Night event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: [5. Noc Walpurgii — Kropka Postawiona Kulą] — tu widnieje czas trwania wydarzenia. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
214. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_03_title_01].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다.\n제 5회 발푸르기스의 밤 이벤트 기간 도중에는 전투 입장 시 엔케팔린 모듈을 소모합니다.\n쉬움 난이도 전투에서는 인격의 레벨이 50레벨보다 낮은 경우, 50레벨로 상승합니다.\n또한 인격의 동기화 단계가 3단계보다 낮은 경우,\n3단계로 상승합니다.\nE.G.O의 환상 해석 단계는 현재 육성 상태가 반영됩니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_03_desc_01].content
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the door to begin the Easy difficulty Encounter.\nDuring the 5th Walpurgis Night Event period, the Encounter consumes an Enkephalin Module upon entry. On Easy difficulty, any Deployed Identities under Level 50 will be raised to Level 50.\nAlso, any Deployed Identities under Tier 3 Uptie Level will be raised to Tier 3 Uptie Level.\nHowever, your current E.G.O Threadspinning Tiers will be reflected.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym.\nW okresie 5. Nocy Walpurgii walka zużywa Moduł Enkefalinu przy wejściu. Na poziomie Łatwym Tożsamości na poziomie niższym niż 50 podnoszone są do poziomu 50.\nPonadto Stopień Synchronizacji Tożsamości niższy niż 3\npodnoszony jest do 3.\nStopień Splotu Nici E.G.O pozostaje bez zmian.
216. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_03_title_02].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다.\n어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상 해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_03_desc_02].content
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_04_title_01] — tekst] 사격 준비 만전 효과
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_04_title_01].content
   limit: do 120 znaków
   EN: 'Ready to Fire' Effect
   PL: Efekt „Pełna Gotowość do Strzału”
219. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_04_desc_01] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘사격 준비 만전’ 효과가 부여됩니다. ‘사격 준비 만전’ 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_04_desc_01].content
   limit: do 240 znaków
   EN: The #1 Sinner to be deployed in the Teams menu will be imbued with the 'Ready to Fire' effect. The Sinner with the 'Ready to Fire' effect will gain more Slots and other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Pełna Gotowość do Strzału”. Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
220. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_05_title_01] — tekst] 미션 목록
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_05_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_05_desc_01].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_06_desc_01].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_06_desc_02].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_06_desc_03].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [Wydarzenia i Przepustka [tutorial_mainui_27_Walpu5_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제5회 발푸르기스밤 - 탄환이 찍은 마침표’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu5EventText.json :: dataList[id=tutorial_mainui_27_Walpu5_07_desc_01].content
   limit: do 280 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 5th Walpurgis Night - Full-Stopped by a Bullet' combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „5. Nocy Walpurgii — Kropka Postawiona Kulą” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].
226. [Wydarzenia i Przepustka [Walpu5_not_progress_event_date] — tekst] 이벤트 기간 종료
   źródło: Walpu5EventText.json :: dataList[id=Walpu5_not_progress_event_date].content
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Wydarzenia i Przepustka [KillCount_Title_LOR_2] — tekst] 처치 현황
   źródło: Walpu5EventText.json :: dataList[id=KillCount_Title_LOR_2].content
   limit: do 120 znaków
   EN: Foes Slain
   PL: Liczba pokonanych wrogów
228. [Wydarzenia i Przepustka [LOR_KillCountTitle_2] — tekst] 톱니교단 신도
   źródło: Walpu5EventText.json :: dataList[id=LOR_KillCountTitle_2].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Wydarzenia i Przepustka [walpu_battle_result_win_2] — tekst] {0} 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_result_win_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Battle Completed
   PL: {0} — Tłumienie ukończone
230. [Wydarzenia i Przepustka [walpu_battle_result_lose_2] — tekst] {0} 토벌 실패
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_result_lose_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Elimination Failed
   PL: {0} — Tłumienie nieudane
231. [Wydarzenia i Przepustka [walpu_battle_result_win_1] — tekst] {0} 토벌 성공
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_result_win_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Eliminated
   PL: {0} — Pokonani
232. [Wydarzenia i Przepustka [walpu_battle_result_lose_1] — tekst] {0} 토벌 실패
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_result_lose_1].content
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Wydarzenia i Przepustka [mainui_battleresult_win_lor_stage_type_2] — tekst] 토벌 완료
   źródło: Walpu5EventText.json :: dataList[id=mainui_battleresult_win_lor_stage_type_2].content
   limit: do 120 znaków
   EN: Battle Completed
   PL: Tłumienie ukończone
234. [Wydarzenia i Przepustka [mainui_battleresult_defeat_lor_stage_type_2] — tekst] 토벌 실패
   źródło: Walpu5EventText.json :: dataList[id=mainui_battleresult_defeat_lor_stage_type_2].content
   limit: do 120 znaków
   EN: Elimination Failed
   PL: Tłumienie nieudane
235. [Wydarzenia i Przepustka [mainui_battleresult_reward_title_lor_stage_type_2] — tekst] 토벌한 개체
   źródło: Walpu5EventText.json :: dataList[id=mainui_battleresult_reward_title_lor_stage_type_2].content
   limit: do 120 znaków
   EN: Vanquished Entities
   PL: Pokonane jednostki
236. [Wydarzenia i Przepustka [walpu5_battle_entrance] — tekst] 전투 시작
   źródło: Walpu5EventText.json :: dataList[id=walpu5_battle_entrance].content
   limit: do 120 znaków
   EN: To Battle!
   PL: Do Boju!
237. [Wydarzenia i Przepustka [walpu5_on_end_event] — tekst] 이벤트 종료
   źródło: Walpu5EventText.json :: dataList[id=walpu5_on_end_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Wydarzenie zakończone
238. [Wydarzenia i Przepustka [walpu_battle_name_10565] — tekst] 톱니교단 신도
   źródło: Walpu5EventText.json :: dataList[id=walpu_battle_name_10565].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: Walpu6EventText
- plik gry: `Walpu6EventText.json`

239. [Wydarzenia i Przepustka [Walpu6_event_desc] — tekst] 증오와 절망 쉬움, 어려움 난이도 전투에서 환상체를 제압하며 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=Walpu6_event_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Suppress the Abnormality in 'Easy' and 'Hard' difficulties of the Hatred and Despair Encounter.\n\nEarn various rewards by clearing these missions.
   PL: Stłum Anomalie Nienawiści i Rozpaczy na Poziomach Łatwym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
240. [Wydarzenia i Przepustka [missionConditionTitle_10047] — tekst] 아르카나 슬레이브로 닳디 닳은 기사 버프를 가진 절망의 기사 제압 성공
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10047].content
   limit: do 120 znaków
   EN: Use Arcana Slave to suppress the Knight of Despair with the 'Weathered Knight' effect
   PL: Ukończ Tłumienie Rycerza Rozpaczy z efektem „Zwietrzały Rycerz” Umiejętnością Arcana Slave
241. [Wydarzenia i Przepustka [missionConditionTitle_10048] — tekst] 증오의 여왕이 적의 공격 스킬로 피해를 3회 미만으로 받고 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10048].content
   limit: do 120 znaków
   EN: Clear Encounter with The Queen of Hatred taking less than 3 hits from enemy Attack Skills
   PL: Ukończ walkę, gdy Królowa Nienawiści otrzyma mniej niż 3 trafienia Umiejętnościami ataku wroga
242. [Wydarzenia i Przepustka [missionConditionTitle_10049] — tekst] 1회 전투에서 잊혀진 기사의 검 소환 후 1회 이상 부활하지 않고 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10049].content
   limit: do 150 znaków
   EN: Complete the Encounter without letting Sword of a Forgotten Knight revive once or more after they are summoned
   PL: W jednej walce ukończ walkę bez odrodzenia Ostrza Zapomnianego Rycerza po przywołaniu
243. [Wydarzenia i Przepustka [missionConditionTitle_10050] — tekst] 1회 전투에서 중앙 본부 팀장 버프가 있는 아군이 무력한 눈물이 있는 검을 3번 처치하고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10050].content
   limit: do 160 znaków
   EN: Complete the Encounter with the Central Command Team Captain surviving and defeating 3 Swords that have 'Helpless Tears'
   PL: W jednej walce ukończ walkę, gdy sojusznik z efektem Kapitana Zespołu Dowodzenia Centrali przeżyje i pokona 3 Ostrza z Bezsilnymi Łzami
244. [Wydarzenia i Przepustka [missionConditionTitle_10051] — tekst] 중앙 본부 팀장 버프가 있는 아군이 충전 위력을 3 이상 얻고, 생존한 상태로 클리어 (특수 충전 포함)
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10051].content
   limit: do 170 znaków
   EN: Complete the Encounter with the Central Command Team Captain surviving and with 3+ Charge Potency (including 'Unique Charge')
   PL: Ukończ walkę, gdy sojusznik z efektem Kapitana Zespołu Dowodzenia Centrali przeżyje z Siłą Ładunku 3 lub wyższą (w tym Specjalny Ładunek)
245. [Wydarzenia i Przepustka [missionConditionTitle_10052] — tekst] 중앙 본부 팀장 버프가 있는 아군이 적의 공격 스킬로 피해를 8회 미만으로 받고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10052].content
   limit: do 160 znaków
   EN: Complete the Encounter with the Central Command Team Captain surviving and taking less than 8 hits from enemy Attack Skills
   PL: Ukończ walkę, gdy sojusznik z efektem Kapitana Zespołu Dowodzenia Centrali przeżyje, otrzymawszy mniej niż 8 trafień Umiejętnościami ataku wroga
246. [Wydarzenia i Przepustka [missionConditionTitle_10053] — tekst] 1회 전투에서 복지팀 우수 직원 버프가 있는 아군의 스킬로 적에게 침잠 또는 파열 위력을 일정 수치 이상 부여
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10053].content
   limit: do 160 znaków
   EN: Have the Welfare Team Model Employee inflict a certain amount of Sinking or Rupture Potency with its Skills in an Encounter
   PL: W jednej walce Wzorowy Pracownik Zespołu Dobrobytu nakłada Umiejętnościami określoną Siłę Zatonięcia albo Rozdarcia na wroga
247. [Wydarzenia i Przepustka [missionConditionTitle_10054] — tekst] 복지팀 우수 직원 버프가 있는 아군이 적의 공격 스킬로 피해를 8회 미만으로 받고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10054].content
   limit: do 160 znaków
   EN: Complete the Encounter with the Welfare Team Model Employee surviving and taking less than 8 hits from enemy Attack Skills
   PL: Ukończ walkę, gdy Wzorowy Pracownik Zespołu Dobrobytu przeżyje, otrzymawszy mniej niż 8 trafień Umiejętnościami ataku wroga
248. [Wydarzenia i Przepustka [missionConditionTitle_10055] — tekst] 1회 전투에서 빼기 코인 스킬을 일정 횟수 이상 사용
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10055].content
   limit: do 120 znaków
   EN: Use Minus Coin Skills a certain number of times in an Encounter
   PL: Użyj Umiejętności z Monetą Minus określoną liczbę razy w jednej walce
249. [Wydarzenia i Przepustka [missionConditionTitle_10056] — tekst] 모든 아군이 생존한 상태로 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10056].content
   limit: do 120 znaków
   EN: Clear Encounter without any ally deaths
   PL: Ukończ walkę bez śmierci żadnego sojusznika
250. [Wydarzenia i Przepustka [missionConditionTitle_10057] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10057].content
   limit: do 120 znaków
   EN: Clear Encounter without any of the allies reaching -45 SP
   PL: Ukończ walkę, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
251. [Wydarzenia i Przepustka [missionConditionTitle_10058] — tekst] 모든 아군의 차갑고 검은 눈물이 부여된 횟수가 20 이상 도달하지 않고 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_10058].content
   limit: do 120 znaków
   EN: Clear Encounter without any of the allies reaching 20 Cold, Black Tears
   PL: Ukończ walkę, nie dopuszczając, by jakikolwiek sojusznik otrzymał 20 lub więcej Zimnych, Czarnych Łez
252. [Wydarzenia i Przepustka [missionConditionTitle_20052] — tekst] 아르카나 슬레이브로 닳디 닳은 기사 버프를 가진 절망의 기사 제압 성공
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20052].content
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Wydarzenia i Przepustka [missionConditionTitle_20053] — tekst] 증오의 여왕이 적의 공격 스킬로 피해를 3회 미만으로 받고 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20053].content
   (powtórzenie elementu 241 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Wydarzenia i Przepustka [missionConditionTitle_20054] — tekst] 1회 전투에서 마음을 부수는 검, 마음을 찢는 검, 마음을 꿰뚫는 검 소환 후 1회 이상 부활하지 않고 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20054].content
   limit: do 200 znaków
   EN: Complete the Encounter without letting Heart-breaking Sword, Heart-tearing Sword, and Heart-piercing Sword revive once or more after they are summoned
   PL: W jednej walce ukończ walkę bez odrodzenia Ostrza Rozbijającego Serce, Ostrza Rozdzierającego Serce i Ostrza Przeszywającego Serce po ich przywołaniu
255. [Wydarzenia i Przepustka [missionConditionTitle_20055] — tekst] 1회 전투에서 중앙 본부 팀장 버프가 있는 아군이 무력한 눈물이 있는 검을 3번 처치하고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20055].content
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Wydarzenia i Przepustka [missionConditionTitle_20056] — tekst] 중앙 본부 팀장 버프가 있는 아군이 충전 위력을 5 이상 얻고, 생존한 상태로 클리어 (특수 충전 포함)
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20056].content
   limit: do 170 znaków
   EN: Complete the Encounter with the Central Command Team Captain surviving and with 5+ Charge Potency (including 'Unique Charge')
   PL: Ukończ walkę, gdy sojusznik z efektem Kapitana Zespołu Dowodzenia Centrali przeżyje z Siłą Ładunku 5 lub wyższą (w tym Specjalny Ładunek)
257. [Wydarzenia i Przepustka [missionConditionTitle_20057] — tekst] 중앙 본부 팀장 버프가 있는 아군이 적의 공격 스킬로 피해를 5회 미만으로 받고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20057].content
   limit: do 160 znaków
   EN: Complete the Encounter with the Central Command Team Captain surviving and taking less than 5 hits from enemy Attack Skills
   PL: Ukończ walkę, gdy sojusznik z efektem Kapitana Zespołu Dowodzenia Centrali przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
258. [Wydarzenia i Przepustka [missionConditionTitle_20058] — tekst] 1회 전투에서 복지팀 우수 직원 버프가 있는 아군의 스킬로 적에게 침잠 또는 파열 위력을 일정 수치 이상 부여
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20058].content
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Wydarzenia i Przepustka [missionConditionTitle_20059] — tekst] 1회 전투에서 복지팀 우수 직원 버프가 있는 아군이 마음을 부수는 검, 마음을 찢는 검, 마음을 꿰뚫는 검과 1번씩 합하기
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20059].content
   limit: do 210 znaków
   EN: Have the Welfare Team Model Employee clash against 'Heart-breaking Sword', 'Heart-tearing Sword', and 'Heart-piercing Sword' once, respectively, in an Encounter
   PL: W jednej walce Wzorowy Pracownik Zespołu Dobrobytu stacza Starcie z każdym z Ostrzy: Rozbijającym Serce, Rozdzierającym Serce i Przeszywającym Serce
260. [Wydarzenia i Przepustka [missionConditionTitle_20060] — tekst] 복지팀 우수 직원 버프가 있는 아군이 적의 공격 스킬로 피해를 5회 미만으로 받고, 생존한 상태로 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20060].content
   limit: do 160 znaków
   EN: Complete the Encounter with the Welfare Team Model Employee surviving and taking less than 5 hits from enemy Attack Skills
   PL: Ukończ walkę, gdy Wzorowy Pracownik Zespołu Dobrobytu przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
261. [Wydarzenia i Przepustka [missionConditionTitle_20061] — tekst] 1회 전투에서 빼기 코인 스킬을 일정 횟수 이상 사용
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20061].content
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Wydarzenia i Przepustka [missionConditionTitle_20062] — tekst] 모든 아군이 생존한 상태로 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20062].content
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Wydarzenia i Przepustka [missionConditionTitle_20063] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20063].content
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Wydarzenia i Przepustka [missionConditionTitle_20064] — tekst] 모든 아군의 차갑고 검은 눈물이 부여된 횟수가 10 이상 도달하지 않고 전투 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_20064].content
   limit: do 120 znaków
   EN: Clear Encounter without any of the allies reaching 10 Cold, Black Tears
   PL: Ukończ walkę, nie dopuszczając, by jakikolwiek sojusznik otrzymał 10 lub więcej Zimnych, Czarnych Łez
265. [Wydarzenia i Przepustka [missionConditionTitle_30005] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu6EventText.json :: dataList[id=missionConditionTitle_30005].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Wydarzenia i Przepustka [walpu6_hard_stage_unlock_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu6EventText.json :: dataList[id=walpu6_hard_stage_unlock_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_01_title] — tekst] 제6회 발푸르기스밤 - 증오와 절망
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_01_title].content
   limit: do 120 znaków
   EN: The 6th Walpurgis Night - Hatred and Despair
   PL: 6. Noc Walpurgii — Nienawiść i Rozpacz
268. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_01_title_01] — tekst] 제6회 발푸르기스밤 - 증오와 절망
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_01_title_01].content
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_01_desc_01] — tekst] [제6회 발푸르기스밤 - 증오와 절망]은 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_01_desc_01].content
   limit: do 220 znaków
   EN: [The 6th Walpurgis Night - Hatred and Despair] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [6. Noc Walpurgii — Nienawiść i Rozpacz] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
270. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_02_title_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_02_desc_01] — tekst] 제6회 발푸르기스밤 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_02_desc_01].content
   limit: do 220 znaków
   EN: The duration of The 6th Walpurgis Night event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: Tutaj widnieje czas trwania wydarzenia 6. Nocy Walpurgii. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
272. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_03_title_01].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다.\n제 6회 발푸르기스의 밤 이벤트 기간 도중에는 전투 입장 시 엔케팔린 모듈을 소모합니다.\n쉬움 난이도 전투에서는 인격의 레벨이 55레벨보다 낮은 경우, 55레벨로 상승합니다.\n또한 인격의 동기화 단계, E.G.O의 환상 해석 단계가 3단계보다 낮은 경우, 3단계로 상승합니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_03_desc_01].content
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the door to begin the Easy difficulty Encounter.\nDuring the 6th Walpurgis Night Event period, the Encounter consumes an Enkephalin Module upon entry. \nOn Easy difficulty, any Deployed Identities under Level 55 will be raised to Level 55.\nAlso, any Deployed Identities and E.G.O under Tier 3 Uptie/Threadspinning Level will be raised to Tier 3 Uptie Level.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym.\nW okresie 6. Nocy Walpurgii walka zużywa Moduł Enkefalinu przy wejściu.\nNa poziomie Łatwym Tożsamości na poziomie niższym niż 55 podnoszone są do poziomu 55.\nPonadto Stopień Synchronizacji Tożsamości i Stopień Splotu Nici E.G.O niższy niż 3 podnoszony jest do 3.
274. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_03_title_02].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다. 어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_03_desc_02].content
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_04_title_01] — tekst] 중앙본부팀 팀장 효과
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_04_title_01].content
   limit: do 120 znaków
   EN: Central Command Team Captain Effects
   PL: Efekty Kapitana Zespołu Dowodzenia Centrali
277. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_04_desc_01] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘중앙본부팀 팀장’ 효과가 부여됩니다. ‘중앙본부팀 팀장’ 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_04_desc_01].content
   limit: do 260 znaków
   EN: The #1 Sinner in the Deployment order will be imbued with the 'Central Command Team Captain' effect. The Sinner with the 'Central Command Captain' effect will gain more Slots and other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Kapitan Zespołu Dowodzenia Centrali”. Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
278. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_04_title_02] — tekst] 복지팀 우수 직원 효과
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_04_title_02].content
   limit: do 120 znaków
   EN: Welfare Team Model Employee Effects
   PL: Efekty Wzorowego Pracownika Zespołu Dobrobytu
279. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_04_desc_02] — tekst] 전투 편성에서 2번으로 선택한 수감자에게 ‘복지팀 우수 직원’ 효과가 부여됩니다. ‘복지팀 우수 직원’ 효과를 받은 수감자는 전투에서 이로운 효과를 얻습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_04_desc_02].content
   limit: do 240 znaków
   EN: The #2 Sinner in the Deployment order will be imbued with the 'Welfare Team Model Employee' effect. The Sinner with the 'Welfare Team Model Employee' effect will gain beneficial effects.
   PL: Drugi Grzesznik w kolejności składu bojowego otrzymuje efekt „Wzorowy Pracownik Zespołu Dobrobytu”. Grzesznik z tym efektem zyskuje pozytywne efekty w walce.
280. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_05_title_01] — tekst] 미션 목록
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_05_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_05_desc_01].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_06_desc_01].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_06_desc_02].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_06_desc_03].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Wydarzenia i Przepustka [tutorial_mainui_walpu6_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제6회 발푸르기스밤 - 증오와 절망’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu6EventText.json :: dataList[id=tutorial_mainui_walpu6_07_desc_01].content
   limit: do 270 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 6th Walpurgis Night - Hatred and Despair' combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „6. Nocy Walpurgii — Nienawiści i Rozpaczy” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].
286. [Wydarzenia i Przepustka [walpu6_reward_button_normal] — tekst] 쉬움 난이도
   źródło: Walpu6EventText.json :: dataList[id=walpu6_reward_button_normal].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Wydarzenia i Przepustka [walpu6_reward_button_hard] — tekst] 어려움 난이도
   źródło: Walpu6EventText.json :: dataList[id=walpu6_reward_button_hard].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Wydarzenia i Przepustka [walpu6_normal_difficulty] — tekst] 쉬움 난이도
   źródło: Walpu6EventText.json :: dataList[id=walpu6_normal_difficulty].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Wydarzenia i Przepustka [walpu6_hard_difficulty] — tekst] 어려움 난이도
   źródło: Walpu6EventText.json :: dataList[id=walpu6_hard_difficulty].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Wydarzenia i Przepustka [walpu6_hard_open_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu6EventText.json :: dataList[id=walpu6_hard_open_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: Walpu7EventText
- plik gry: `Walpu7EventText.json`

291. [Wydarzenia i Przepustka [walpu7_reward_event_desc] — tekst] 이벤트 기간 동안 실제 소모한 엔케팔린 수치가 반영됩니다.\n모듈 제작에 사용된 엔케팔린은 집계에 포함되지 않으며,\n엔케팔린 모듈을 소모할 경우\n개당 <color=#22ffe4>20의 엔케팔린</color>이 소모된 것으로 반영됩니다.
   źródło: Walpu7EventText.json :: dataList[id=walpu7_reward_event_desc].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#22ffe4>, </color>, \n
   EN: The actual amount of Enkephalin spent during the event period will be recorded.\nSpending Enkephalin to assemble Enkephalin Modules does not count toward your spent Enkephalin count.\nHowever, each Enkephalin Module spent counts as <color=#22ffe4>20 Enkephalin</color> spent.
   PL: Odzwierciedlona zostaje rzeczywista ilość zużytej Enkefaliny w okresie wydarzenia.\nEnkefalina zużyta na produkcję Modułów nie wlicza się do bilansu,\na każdy zużyty Moduł Enkefalinu liczy się\njako <color=#22ffe4>20 Enkefaliny</color>.
292. [Wydarzenia i Przepustka [walpu7_consumed_enkephalin] — tekst] 엔케팔린 소모 현황
   źródło: Walpu7EventText.json :: dataList[id=walpu7_consumed_enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin Spent
   PL: Zużyta Enkefalina

## Wydarzenia i Przepustka: Walpu8EventText
- plik gry: `Walpu8EventText.json`

293. [Wydarzenia i Przepustka [Walpu8_event_desc] — tekst] 호박색 어스름의 시련 쉬움, 어려움 난이도 전투에서 시련을 제압하고 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=Walpu8_event_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Suppress Dusk of Amber entities in 'Easy' and 'Hard' difficulties from the Dusk of Amber Ordeal.\n\nEarn various rewards by clearing these missions.
   PL: Stłum istoty Próby Bursztynowego Zmierzchu na Poziomach Łatwym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
294. [Wydarzenia i Przepustka [missionConditionTitle_10117] — tekst] 1회 전투에서 뀽뀽이[오렌지맛] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10117].content
   limit: do 120 znaków
   EN: Complete Suppression after defeating a BongBong [Orange] unit in a single Encounter
   PL: Ukończ Tłumienie, pokonawszy Pomarańczowego BongBonga w jednej walce
295. [Wydarzenia i Przepustka [missionConditionTitle_10118] — tekst] 1회 전투에서 뀽뀽이[오렌지맛] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10118].content
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Wydarzenia i Przepustka [missionConditionTitle_10119] — tekst] 1회 전투에서 큥큥이[오렌지맛 착즙기] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10119].content
   limit: do 130 znaków
   EN: Complete Suppression after defeating a BunBun [Juicy Squeezer - Orange] unit in a single Encounter
   PL: Ukończ Tłumienie, pokonawszy BunBuna [Pomarańczowa Wyciskarka] w jednej walce
297. [Wydarzenia i Przepustka [missionConditionTitle_10120] — tekst] 뀽뀽이[오렌지맛]이 퇴각하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10120].content
   limit: do 120 znaków
   EN: Complete Suppression without BongBong [Orange] unit retreating
   PL: Ukończ Tłumienie bez Odwrotu Pomarańczowego BongBonga
298. [Wydarzenia i Przepustka [missionConditionTitle_10121] — tekst] 복지팀 팀장 버프가 있는 아군이 1회 전투에서 적 5명 이상 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10121].content
   limit: do 120 znaków
   EN: Complete Suppression after the Welfare Team Captain defeats 5+ enemies in a single Encounter
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu pokona 5 lub więcej wrogów w jednej walce
299. [Wydarzenia i Przepustka [missionConditionTitle_10122] — tekst] 복지팀 팀장 버프가 있는 아군이 적의 공격 스킬로 피해를 5회 미만으로 받고, 생존한 상태로 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10122].content
   limit: do 150 znaków
   EN: Complete Suppression with the Welfare Team Captain surviving and taking less than 5 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
300. [Wydarzenia i Przepustka [missionConditionTitle_10123] — tekst] 복지팀 팀장 버프가 있는 아군이 1회 전투에서  큥큥이[오렌지맛 착즙기] 1개체 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10123].content
   limit: do 170 znaków
   EN: Complete Suppression after the Welfare Team Captain defeats at least 1 BunBun [Juicy Squeezer - Orange] in a single Encounter
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu pokona co najmniej 1 BunBuna [Pomarańczowa Wyciskarka] w jednej walce
301. [Wydarzenia i Przepustka [missionConditionTitle_10124] — tekst] 아군이 3명 이상 오렌지맛 뀽뀽이를 각각 1회 획득하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10124].content
   limit: do 120 znaków
   EN: Complete Suppression after 3+ allies each gain BongBong Orange at least once
   PL: Ukończ Tłumienie, gdy 3 lub więcej sojuszników zdobędzie po jednym Pomarańczowym BongBongu
302. [Wydarzenia i Przepustka [missionConditionTitle_10125] — tekst] 1회 전투에서 공격 스킬 1개로 가한 피해량 300 이상 달성하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10125].content
   limit: do 130 znaków
   EN: Complete Suppression after dealing 300+ Damage with a single Attack Skill in a single Encounter
   PL: Ukończ Tłumienie, zadając 300 lub więcej obrażeń pojedynczą Umiejętnością ataku w jednej walce
303. [Wydarzenia i Przepustka [missionConditionTitle_10126] — tekst] 모든 아군이 생존한 상태로 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10126].content
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Wydarzenia i Przepustka [missionConditionTitle_10127] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10127].content
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Wydarzenia i Przepustka [missionConditionTitle_10128] — tekst] 모든 아군의 출혈 위력이 10 이상 도달하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_10128].content
   limit: do 120 znaków
   EN: Complete Suppression without any of the allies reaching 10 Bleed Potency
   PL: Ukończ Tłumienie, nie dopuszczając, by jakikolwiek sojusznik osiągnął Siłę Krwawienia 10 lub wyższą
306. [Wydarzenia i Przepustka [missionConditionTitle_20065] — tekst] 1회 전투에서 뀽뀽이[오렌지맛] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20065].content
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Wydarzenia i Przepustka [missionConditionTitle_20066] — tekst] 1회 전투에서 뀽뀽이[오렌지맛] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20066].content
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Wydarzenia i Przepustka [missionConditionTitle_20067] — tekst] 1회 전투에서 큥큥이[오렌지맛 착즙기] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20067].content
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Wydarzenia i Przepustka [missionConditionTitle_20068] — tekst] 1회 전투에서 큥큥이[오렌지맛 착즙기] 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20068].content
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Wydarzenia i Przepustka [missionConditionTitle_20069] — tekst] 큥큥이[오렌지맛 착즙기]가 퇴각하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20069].content
   limit: do 120 znaków
   EN: Complete Suppression without BunBun [Juicy Squeezer - Orange] unit retreating
   PL: Ukończ Tłumienie bez Odwrotu BunBuna [Pomarańczowa Wyciskarka]
311. [Wydarzenia i Przepustka [missionConditionTitle_20070] — tekst] 복지팀 팀장 버프가 있는 아군이 1회 전투에서 큥큥이[오렌지맛 착즙기] 1개체 이상 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20070].content
   limit: do 170 znaków
   EN: Complete Suppression after the Welfare Team Captain defeats at least 1 BunBun [Juicy Squeezer - Orange] in a single Encounter
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu pokona 1 lub więcej BunBunów [Pomarańczowa Wyciskarka] w jednej walce
312. [Wydarzenia i Przepustka [missionConditionTitle_20071] — tekst] 복지팀 팀장 버프가 있는 아군이 1회 전투에서 적 10명 이상 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20071].content
   limit: do 130 znaków
   EN: Complete Suppression after the Welfare Team Captain defeats 10+ enemies in a single Encounter
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu pokona 10 lub więcej wrogów w jednej walce
313. [Wydarzenia i Przepustka [missionConditionTitle_20072] — tekst] 복지팀 팀장 버프가 있는 아군이 적의 공격 스킬로 피해를 3회 미만으로 받고, 생존한 상태로 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20072].content
   limit: do 150 znaków
   EN: Complete Suppression with the Welfare Team Captain surviving and taking less than 3 hits from enemy Attack Skills
   PL: Ukończ Tłumienie, gdy sojusznik z efektem Kapitana Zespołu Dobrobytu przeżyje, otrzymawszy mniej niż 3 trafienia Umiejętnościami ataku wroga
314. [Wydarzenia i Przepustka [missionConditionTitle_20073] — tekst] 공격 스킬 1회 사용으로 적 3명 이상 처치하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20073].content
   limit: do 120 znaków
   EN: Complete Suppression after defeating 3+ enemies with a single Attack Skill
   PL: Ukończ Tłumienie, pokonawszy 3 lub więcej wrogów jednym użyciem Umiejętności ataku
315. [Wydarzenia i Przepustka [missionConditionTitle_20074] — tekst] 모든 아군이 오렌지맛 뀽뀽이를 각각 1회 획득하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20074].content
   limit: do 120 znaków
   EN: Complete Suppression after all allies each gain Bongbong Orange at least once
   PL: Ukończ Tłumienie, gdy wszyscy sojusznicy zdobędą po jednym Pomarańczowym BongBongu
316. [Wydarzenia i Przepustka [missionConditionTitle_20075] — tekst] 1회 전투에서 공격 스킬 1개로 가한 피해량 500 이상 달성하고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20075].content
   limit: do 130 znaków
   EN: Complete Suppression after dealing 500+ Damage with a single Attack Skill in a single Encounter
   PL: Ukończ Tłumienie, zadając 500 lub więcej obrażeń pojedynczą Umiejętnością ataku w jednej walce
317. [Wydarzenia i Przepustka [missionConditionTitle_20076] — tekst] 모든 아군이 생존한 상태로 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20076].content
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Wydarzenia i Przepustka [missionConditionTitle_20077] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20077].content
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Wydarzenia i Przepustka [missionConditionTitle_20078] — tekst] 모든 아군의 출혈 위력이 10 이상 도달하지 않고 제압 성공
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20078].content
   (powtórzenie elementu 305 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Wydarzenia i Przepustka [missionConditionTitle_20079] — tekst] 쉬움, 어려움 난이도의 모든 미션 클리어
   źródło: Walpu8EventText.json :: dataList[id=missionConditionTitle_20079].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_01_title] — tekst] 제8회 발푸르기스밤 - 호박색 어스름의 시련
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_01_title].content
   limit: do 120 znaków
   EN: The 8th Walpurgis Night - The Dusk of Amber
   PL: 8. Noc Walpurgii — Próba Bursztynowego Zmierzchu
322. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_01_title_01] — tekst] 제8회 발푸르기스밤 - 호박색 어스름의 시련
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_01_title_01].content
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_01_desc_01] — tekst] [제8회 발푸르기스밤 - 호박색 어스름의 시련]은 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_01_desc_01].content
   limit: do 210 znaków
   EN: [The 8th Walpurgis Night - The Dusk of Amber] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window and the Drive tabs.
   PL: [8. Noc Walpurgii — Próba Bursztynowego Zmierzchu] odblokowuje się niezależnie od postępu Głównej Opowieści. Wejdź przez banner wydarzenia w zakładce Okno albo Jazda.
324. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_02_title_01] — tekst] 이벤트 기간
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_02_title_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_02_desc_01] — tekst] 제8회 발푸르기스밤 이벤트 기간이 표시됩니다. 이벤트 기간 동안 쉬움 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_02_desc_01].content
   limit: do 220 znaków
   EN: The duration of The 8th Walpurgis Night event is shown here. During the event, complete Missions for Easy and Hard difficulty event Encounters and claim their rewards.
   PL: Tutaj widnieje czas trwania wydarzenia 8. Nocy Walpurgii. W trakcie wydarzenia tocz walki na Poziomach Łatwym i Trudnym, wykonuj misje i odbieraj nagrody za ukończone misje.
326. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_03_title_01] — tekst] 쉬움 난이도 전투
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_03_title_01].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_03_desc_01] — tekst] 문을 눌러 쉬움 난이도 전투에 입장할 수 있습니다.\n제 8회 발푸르기스의 밤 이벤트 기간 도중에는 전투 입장 시 엔케팔린 모듈을 소모합니다.\n쉬움 난이도 전투에서는 인격의 레벨이 60레벨보다 낮은 경우, 60레벨로 상승합니다.\n또한 인격의 동기화 단계, E.G.O의 환상 해석 단계가 3단계보다 낮은 경우, 3단계로 상승합니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_03_desc_01].content
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the door to begin the Easy difficulty Encounter.\nDuring the 8th Walpurgis Night Event period, the Encounter consumes an Enkephalin Module upon entry. \nOn Easy difficulty, any Deployed Identities under Level 60 will be raised to Level 60.\nAlso, any Deployed Identities and E.G.O under Tier 3 Uptie/Threadspinning Level will be raised to Tier 3 Uptie Level.
   PL: Dotknij drzwi, aby wejść do walki na poziomie Łatwym.\nW okresie 8. Nocy Walpurgii walka zużywa Moduł Enkefalinu przy wejściu.\nNa poziomie Łatwym Tożsamości na poziomie niższym niż 60 podnoszone są do poziomu 60.\nPonadto Stopień Synchronizacji Tożsamości i Stopień Splotu Nici E.G.O niższy niż 3 podnoszony jest do 3.
328. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_03_title_02] — tekst] 어려움 난이도 전투
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_03_title_02].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_03_desc_02] — tekst] 쉬움 난이도 전투를 클리어하면 어려움 난이도 전투가 개방됩니다. 어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_03_desc_02].content
   (powtórzenie elementu 28 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_04_title_01] — tekst] 복지팀 팀장 효과
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_04_title_01].content
   limit: do 120 znaków
   EN: Welfare Team Captain Effects
   PL: Efekty Kapitana Zespołu Dobrobytu
331. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_04_desc_01] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘복지팀 팀장’ 효과가 부여됩니다. ‘복지팀 팀장’ 효과를 받은 수감자는 전투에서 행동 수가 증가하고, 이로운 효과를 얻습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_04_desc_01].content
   limit: do 260 znaków
   EN: The #1 Sinner to be deployed in the Teams menu will be imbued with the 'Welfare Team Captain' effect. The Sinner with the 'Welfare Team Captain' effect will gain more Slots and other beneficial effects.
   PL: Pierwszy Grzesznik w kolejności składu bojowego otrzymuje efekt „Kapitan Zespołu Dobrobytu”. Grzesznik z tym efektem zyskuje więcej akcji w walce oraz pozytywne efekty.
332. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_05_title_01] — tekst] 미션 목록
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_05_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_05_desc_01].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_06_desc_01].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_06_desc_02] — tekst] 쉬움 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_06_desc_02].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_06_desc_03].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Wydarzenia i Przepustka [tutorial_mainui_walpu8_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제8회 발푸르기스밤 - 호박색 어스름의 시련’의 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: Walpu8EventText.json :: dataList[id=tutorial_mainui_walpu8_07_desc_01].content
   limit: do 260 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 8th Walpurgis Night - The Dusk of Amber' combat Encounters and view its story anytime on the Drive tab or Theater - [Detour Tales].
   PL: Po zakończeniu wydarzenia nadal będziesz mógł toczyć walki „8. Nocy Walpurgii — Próby Bursztynowego Zmierzchu” i oglądać jej opowieść w zakładce Jazda oraz w Teatrze — [Opowieści Poboczne].
338. [Wydarzenia i Przepustka [walpu8_reward_button_normal] — tekst] 쉬움 난이도
   źródło: Walpu8EventText.json :: dataList[id=walpu8_reward_button_normal].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Wydarzenia i Przepustka [walpu8_reward_button_hard] — tekst] 어려움 난이도
   źródło: Walpu8EventText.json :: dataList[id=walpu8_reward_button_hard].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Wydarzenia i Przepustka [walpu8_normal_difficulty] — tekst] 쉬움 난이도
   źródło: Walpu8EventText.json :: dataList[id=walpu8_normal_difficulty].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Wydarzenia i Przepustka [walpu8_hard_difficulty] — tekst] 어려움 난이도
   źródło: Walpu8EventText.json :: dataList[id=walpu8_hard_difficulty].content
   (powtórzenie elementu 40 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Wydarzenia i Przepustka [walpu8_hard_open_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu8EventText.json :: dataList[id=walpu8_hard_open_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Wydarzenia i Przepustka [KillCount_Title_4] — tekst] 호박색 어스름의 시련
   źródło: Walpu8EventText.json :: dataList[id=KillCount_Title_4].content
   limit: do 120 znaków
   EN: The Dusk of Amber
   PL: Próba Bursztynowego Zmierzchu
344. [Wydarzenia i Przepustka [LobotomyStartTypo_KillCountTitle_4] — tekst] 제압 현황
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_KillCountTitle_4].content
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Wydarzenia i Przepustka [LobotomyStartTypo_Title_Walpu8_Start] — tekst] 호박색 여명의 시련
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Title_Walpu8_Start].content
   limit: do 120 znaków
   EN: The Dusk of Amber
   PL: Próba Bursztynowego Zmierzchu
346. [Wydarzenia i Przepustka [LobotomyStartTypo_Name_Walpu8_Start] — tekst] 완전 식품
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Name_Walpu8_Start].content
   limit: do 120 znaków
   EN: The Perfect Food
   PL: Idealne Jedzenie
347. [Wydarzenia i Przepustka [LobotomyStartTypo_Desc_Walpu8_Start] — tekst] 완전한 음식, 완벽한 대체제
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Desc_Walpu8_Start].content
   limit: do 120 znaków
   EN: A perfect meal, an excellent substitute
   PL: Idealny posiłek, doskonały zamiennik
348. [Wydarzenia i Przepustka [LobotomyClearTypo_Title_Walpu8_Win] — tekst] 호박색 어스름의 시련
   źródło: Walpu8EventText.json :: dataList[id=LobotomyClearTypo_Title_Walpu8_Win].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Wydarzenia i Przepustka [LobotomyClearTypo_Name_Walpu8_Win] — tekst] 먹이 사슬
   źródło: Walpu8EventText.json :: dataList[id=LobotomyClearTypo_Name_Walpu8_Win].content
   limit: do 120 znaków
   EN: The Food Chain
   PL: Łańcuch Pokarmowy
350. [Wydarzenia i Przepustka [LobotomyClearTypo_Desc_Walpu8_Win] — tekst] 우리는 살아갈 수 있었다. 계속 먹을 수 있었다.
   źródło: Walpu8EventText.json :: dataList[id=LobotomyClearTypo_Desc_Walpu8_Win].content
   limit: do 120 znaków
   EN: We could live. We could continue eating.
   PL: Mogliśmy żyć. Mogliśmy jeść dalej.
351. [Wydarzenia i Przepustka [LobotomyStartTypo_Title_Walpu8_Appear] — tekst] 호박색 어스름의 시련
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Title_Walpu8_Appear].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Wydarzenia i Przepustka [LobotomyStartTypo_Name_Walpu8_Appear] — tekst] 먹이 사슬
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Name_Walpu8_Appear].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Wydarzenia i Przepustka [LobotomyStartTypo_Desc_Walpu8_Appear] — tekst] 그 맛을 알게 되는 것은 피할 수 없는 과정이었다.
   źródło: Walpu8EventText.json :: dataList[id=LobotomyStartTypo_Desc_Walpu8_Appear].content
   limit: do 120 znaków
   EN: To accustom oneself to the taste was an inevitable process.
   PL: Poznanie tego smaku było nieuniknionym procesem.
354. [Wydarzenia i Przepustka [walpu8_hard_stage_unlock_condition] — tekst] 쉬움 난이도 클리어 시 개방
   źródło: Walpu8EventText.json :: dataList[id=walpu8_hard_stage_unlock_condition].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: CouponUIText
- plik gry: `CouponUIText.json`

355. [Przedmioty, sklep i profil gracza [coupon_InputField_block] — tekst] 쿠폰 코드 입력 불가
   źródło: CouponUIText.json :: dataList[id=coupon_InputField_block].content
   limit: do 120 znaków
   EN: Cannot Input Coupon Codes
   PL: Nie można wprowadzić kodu kuponu
356. [Przedmioty, sklep i profil gracza [coupon_InputField] — tekst] 쿠폰 코드 입력
   źródło: CouponUIText.json :: dataList[id=coupon_InputField].content
   limit: do 120 znaków
   EN: Input coupon codes here
   PL: Wprowadź kod kuponu tutaj
357. [Przedmioty, sklep i profil gracza [coupon_popup_title] — tekst] 쿠폰 입력
   źródło: CouponUIText.json :: dataList[id=coupon_popup_title].content
   limit: do 120 znaków
   EN: Input Coupon Code
   PL: Wprowadź kod kuponu
358. [Przedmioty, sklep i profil gracza [coupon_popup_desc] — tekst] -쿠폰은 대문자 + 숫자로만 조합됩니다.\n- 같은 쿠폰은 계정마다 한 번만 등록할 수 있습니다.\n- 유효기간이 만료된 쿠폰은 등록할 수 없습니다.\n- 단기간에 다수의 등록 실패 시, 일정 기간 쿠폰 등록이 제한될 수 있습니다.
   źródło: CouponUIText.json :: dataList[id=coupon_popup_desc].content
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Coupons are always combinations of upper-case English alphabets and numbers.\n- No same coupon can be registered more than once for the same account.\n- Coupons past their expiry date cannot be registered.\n- Repeated coupon code input failure within a short timeframe may restrict coupon code for a set amount of time.
   PL: - Kupony składają się wyłącznie z wielkich liter i cyfr.\n- Ten sam kupon można zarejestrować tylko raz na konto.\n- Kuponu po terminie ważności nie da się zarejestrować.\n- Po wielu nieudanych próbach w krótkim czasie rejestracja kuponów może zostać na jakiś czas zablokowana.
359. [Przedmioty, sklep i profil gracza [coupon_use_failed_2] — tekst] 유효하지 않은 쿠폰입니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_2].content
   limit: do 120 znaków
   EN: This coupon is invalid.
   PL: Ten kupon jest nieważny.
360. [Przedmioty, sklep i profil gracza [coupon_use_failed_3] — tekst] 유효하지 않은 쿠폰입니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_3].content
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Przedmioty, sklep i profil gracza [coupon_use_failed_4] — tekst] 유효기간이 만료된 쿠폰입니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_4].content
   limit: do 120 znaków
   EN: This coupon is expired.
   PL: Ten kupon stracił ważność.
362. [Przedmioty, sklep i profil gracza [coupon_use_failed_5] — tekst] 이미 사용된 쿠폰입니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_5].content
   limit: do 120 znaków
   EN: This coupon has already been claimed.
   PL: Ten kupon został już wykorzystany.
363. [Przedmioty, sklep i profil gracza [coupon_use_failed_6] — tekst] 이미 사용된 쿠폰입니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_6].content
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Przedmioty, sklep i profil gracza [coupon_use_failed_7] — tekst] 연속 등록 실패로 인해 {0}까지 쿠폰 등록이 중단 중단되었습니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_7].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Repeated coupon code input failure. Coupon code input restricted until {0}.
   PL: Wielokrotne nieudane próby — rejestracja kuponów wstrzymana do {0}.
365. [Przedmioty, sklep i profil gracza [coupon_InputField_block_desc] — tekst] {0}까지 등록 중단
   źródło: CouponUIText.json :: dataList[id=coupon_InputField_block_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Coupon code input restricted until {0}
   PL: Rejestracja wstrzymana do {0}
366. [Przedmioty, sklep i profil gracza [coupon_use_failed_unknown] — tekst] 알 수 없는 오류가 발생했습니다.
   źródło: CouponUIText.json :: dataList[id=coupon_use_failed_unknown].content
   limit: do 120 znaków
   EN: An unknown error has occurred.
   PL: Wystąpił nieznany błąd.

## Przedmioty, sklep i profil gracza: GachaNotice
- plik gry: `GachaNotice.json`

367. [Przedmioty, sklep i profil gracza [10316] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며, 등장 시 두 인격을 항상 함께 획득합니다.
   źródło: GachaNotice.json :: dataList[id=10316].content
   limit: do 240 znaków
   EN: Wedge Office Fixer Don Quixote and Wedge Office Fixer Sinclair are treated as a single 3★ Identity in the Extraction. Obtaining either Identity will always yield the other in the pair.
   PL: Fikserka Biura Klina Don Quixote oraz Fikser Biura Klina Sinclair są traktowani w Ekstrakcji jako pojedyncza Tożsamość 3★ — wylosowanie jednej z nich zawsze przyznaje obie naraz.
368. [Przedmioty, sklep i profil gracza [11017] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며, 등장 시 두 인격을 항상 함께 획득합니다.
   źródło: GachaNotice.json :: dataList[id=11017].content
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Przedmioty, sklep i profil gracza [11116] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며, 등장 시 두 인격을 항상 함께 획득합니다.
   źródło: GachaNotice.json :: dataList[id=11116].content
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Przedmioty, sklep i profil gracza [20611] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며, 등장 시 두 인격을 항상 함께 획득합니다.
   źródło: GachaNotice.json :: dataList[id=20611].content
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Przedmioty, sklep i profil gracza: GachaTitle
- plik gry: `GachaTitle.json`

371. [Przedmioty, sklep i profil gracza [1] — tekst] 일반 추출
   źródło: GachaTitle.json :: dataList[id=1].content
   limit: do 120 znaków
   EN: Standard Extraction
   PL: Ekstrakcja Standardowa
372. [Przedmioty, sklep i profil gracza [2] — tekst] 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości
373. [Przedmioty, sklep i profil gracza [3] — tekst] 신입 관리자 기념 추출
   źródło: GachaTitle.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: New Manager’s Welcome Extraction
   PL: Ekstrakcja Powitalna Nowego Kierownika
374. [Przedmioty, sklep i profil gracza [4] — tekst] 시즌 1 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=4].content
   limit: do 120 znaków
   EN: [Season 1] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 1
375. [Przedmioty, sklep i profil gracza [101] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=101].content
   limit: do 120 znaków
   EN: Target Extraction: Gregor
   PL: Ekstrakcja Celowana: Gregor
376. [Przedmioty, sklep i profil gracza [102] — tekst] 신규 특정 추출 N사-#1
   źródło: GachaTitle.json :: dataList[id=102].content
   limit: do 120 znaków
   EN: New Target Extraction: N Corp. #1
   PL: Nowa Ekstrakcja Celowana: Korp. N #1
377. [Przedmioty, sklep i profil gracza [103] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=103].content
   limit: do 120 znaków
   EN: Target Extraction: Rodion
   PL: Ekstrakcja Celowana: Rodion
378. [Przedmioty, sklep i profil gracza [104] — tekst] 신규 특정 추출 N사-#2
   źródło: GachaTitle.json :: dataList[id=104].content
   limit: do 120 znaków
   EN: New Target Extraction: N Corp. #2
   PL: Nowa Ekstrakcja Celowana: Korp. N #2
379. [Przedmioty, sklep i profil gracza [105] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=105].content
   limit: do 120 znaków
   EN: Target Extraction: Heathcliff
   PL: Ekstrakcja Celowana: Heathcliff
380. [Przedmioty, sklep i profil gracza [106] — tekst] 신규 특정 추출 세븐 협회 6과 부장 오티스, 리우 협회 5과 홍루
   źródło: GachaTitle.json :: dataList[id=106].content
   limit: do 120 znaków
   EN: New Target Extraction: Seven S6 Director Outis & Liu S5 Hong Lu
   PL: Nowa Ekstrakcja Celowana: Dyrektorka Sekcji 6 Stowarzyszenia Seven Outis i Sekcja 5 Stowarzyszenia Liu Hong Lu
381. [Przedmioty, sklep i profil gracza [107] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=107].content
   limit: do 120 znaków
   EN: Target Extraction: Don Quixote
   PL: Ekstrakcja Celowana: Don Quixote
382. [Przedmioty, sklep i profil gracza [108] — tekst] 신규 특정 추출 헬스 치킨
   źródło: GachaTitle.json :: dataList[id=108].content
   limit: do 120 znaków
   EN: New Target Extraction: Hell’s Chicken
   PL: Nowa Ekstrakcja Celowana: Piekielny Kurczak
383. [Przedmioty, sklep i profil gracza [109] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=109].content
   limit: do 120 znaków
   EN: Target Extraction: Hong Lu
   PL: Ekstrakcja Celowana: Hong Lu
384. [Przedmioty, sklep i profil gracza [110] — tekst] 신규 특정 추출 N사-#3
   źródło: GachaTitle.json :: dataList[id=110].content
   limit: do 120 znaków
   EN: New Target Extraction: N Corp. #3
   PL: Nowa Ekstrakcja Celowana: Korp. N #3
385. [Przedmioty, sklep i profil gracza [111] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=111].content
   limit: do 120 znaków
   EN: Target Extraction: Faust
   PL: Ekstrakcja Celowana: Faust
386. [Przedmioty, sklep i profil gracza [112] — tekst] 특정 추출 E.G.O 차원찢개 이상 · 홍루
   źródło: GachaTitle.json :: dataList[id=112].content
   limit: do 120 znaków
   EN: Target Extraction: Dimension Shredder for Yi Sang & Hong Lu
   PL: Ekstrakcja Celowana: Rozpruwacz Wymiarów dla Yi Sanga i Hong Lu
387. [Przedmioty, sklep i profil gracza [113] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=113].content
   limit: do 120 znaków
   EN: Target Extraction: Meursault
   PL: Ekstrakcja Celowana: Meursault
388. [Przedmioty, sklep i profil gracza [114] — tekst] 신규 특정 추출 장미스패너 공방 사무소
   źródło: GachaTitle.json :: dataList[id=114].content
   limit: do 120 znaków
   EN: New Target Extraction: Rosespanner Workshop
   PL: Nowa Ekstrakcja Celowana: Warsztat Różanego Klucza
389. [Przedmioty, sklep i profil gracza [5] — tekst] 시즌 2 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: [Season 2] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 2
390. [Przedmioty, sklep i profil gracza [115] — tekst] 신규 특정 추출 기술해방연합 · 장미스패너 공방
   źródło: GachaTitle.json :: dataList[id=115].content
   limit: do 120 znaków
   EN: New Target Extraction: Technology Liberation Alliance & Rosespanner Workshop
   PL: Nowa Ekstrakcja Celowana: Sojusz Wyzwolenia Technologii i Warsztat Różanego Klucza
391. [Przedmioty, sklep i profil gracza [116] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=116].content
   limit: do 120 znaków
   EN: Target Extraction: Outis
   PL: Ekstrakcja Celowana: Outis
392. [Przedmioty, sklep i profil gracza [117] — tekst] 신규 특정 추출 기술해방연합#2
   źródło: GachaTitle.json :: dataList[id=117].content
   limit: do 120 znaków
   EN: New Target Extraction: Technology Liberation Alliance #2
   PL: Nowa Ekstrakcja Celowana: Sojusz Wyzwolenia Technologii #2
393. [Przedmioty, sklep i profil gracza [118] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=118].content
   limit: do 120 znaków
   EN: Target Extraction: Sinclair
   PL: Ekstrakcja Celowana: Sinclair
394. [Przedmioty, sklep i profil gracza [119] — tekst] 신규 특정 추출 K사 · 기술해방연합#3
   źródło: GachaTitle.json :: dataList[id=119].content
   limit: do 120 znaków
   EN: New Target Extraction: K Corp & Technology Liberation Alliance #3
   PL: Nowa Ekstrakcja Celowana: Korp. K i Sojusz Wyzwolenia Technologii #3
395. [Przedmioty, sklep i profil gracza [120] — tekst] 신규 E.G.O 특정 추출 적안 · 적안(開)
   źródło: GachaTitle.json :: dataList[id=120].content
   limit: do 120 znaków
   EN: Target Extraction: Red Eyes & Red Eyes (Open)
   PL: Nowa Ekstrakcja Celowana E.G.O: Czerwone Oczy i Czerwone Oczy (Otwarte)
396. [Przedmioty, sklep i profil gracza [121] — tekst] 신규 특정 추출 남부 리우 협회 4과 이스마엘
   źródło: GachaTitle.json :: dataList[id=121].content
   limit: do 120 znaków
   EN: New Target Extraction: Liu South Section 4 Ishmael
   PL: Nowa Ekstrakcja Celowana: Sekcja 4 Południowego Stowarzyszenia Liu Ishmael
397. [Przedmioty, sklep i profil gracza [122] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=122].content
   limit: do 120 znaków
   EN: Target Extraction: Yi Sang
   PL: Ekstrakcja Celowana: Yi Sang
398. [Przedmioty, sklep i profil gracza [123] — tekst] 신규 특정 추출 R사 제 4무리 코뿔소 팀 뫼르소 · 남부 츠바이 협회 5과 로쟈
   źródło: GachaTitle.json :: dataList[id=123].content
   limit: do 120 znaków
   EN: New Target Extraction: R Corp. 4th Pack Rhino Meursault & Zwei South Section 5 Rodion
   PL: Nowa Ekstrakcja Celowana: Zespół Nosorożców 4. Stada R Corp. Meursault i Sekcja 5 Południowego Stow. Zwei Rodion
399. [Przedmioty, sklep i profil gracza [124] — tekst] 신규 특정 추출 남부 섕크 협회 5과 부장 돈키호테
   źródło: GachaTitle.json :: dataList[id=124].content
   limit: do 120 znaków
   EN: New Target Extraction: Cinq South Section 5 Director Don Quixote
   PL: Nowa Ekstrakcja Celowana: Dyrektorka Sekcji 5 Południowego Stowarzyszenia Cinq Don Quixote
400. [Przedmioty, sklep i profil gracza [125] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=125].content
   limit: do 120 znaków
   EN: Target Extraction: Ryōshū
   PL: Ekstrakcja Celowana: Ryōshū
401. [Przedmioty, sklep i profil gracza [126] — tekst] 신규 인격 · E.G.O 특정 추출 우.미.다
   źródło: GachaTitle.json :: dataList[id=126].content
   limit: do 120 znaków
   EN: New Target Extraction: Identity & E.G.O - S.E.A
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — M.O.R.Z.E.
402. [Przedmioty, sklep i profil gracza [127] — tekst] 신규 특정 추출 남부 츠바이 협회 4과 그레고르 · 파우스트
   źródło: GachaTitle.json :: dataList[id=127].content
   limit: do 120 znaków
   EN: New Target Extraction: Zwei South Section 4 Gregor & Faust
   PL: Nowa Ekstrakcja Celowana: Sekcja 4 Południowego Stowarzyszenia Zwei Gregor i Faust
403. [Przedmioty, sklep i profil gracza [128] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=128].content
   limit: do 120 znaków
   EN: Target Extraction: Ishmael
   PL: Ekstrakcja Celowana: Ishmael
404. [Przedmioty, sklep i profil gracza [129] — tekst] 신규 특정 추출 W사 3등급 정리요원 료슈 · 2등급 정리요원 홍루
   źródło: GachaTitle.json :: dataList[id=129].content
   limit: do 120 znaków
   EN: New Target Extraction: W Corp. L3 Cleanup Agent Ryōshū & L2 Cleanup Agent Hong Lu
   PL: Nowa Ekstrakcja Celowana: Agentka Oczyszczania L3 W Corp. Ryōshū i Agent Oczyszczania L2 W Corp. Hong Lu
405. [Przedmioty, sklep i profil gracza [130] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=130].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Przedmioty, sklep i profil gracza [131] — tekst] 신규 특정 추출 남부 세븐 협회 4과 파우스트 · 히스클리프
   źródło: GachaTitle.json :: dataList[id=131].content
   limit: do 120 znaków
   EN: New Target Extraction: Seven South Section 4 Faust & Heathcliff
   PL: Nowa Ekstrakcja Celowana: Sekcja 4 Południowego Stowarzyszenia Seven Faust i Heathcliff
407. [Przedmioty, sklep i profil gracza [132] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=132].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Przedmioty, sklep i profil gracza [133] — tekst] 신규 특정 추출 남부 디에치 협회 4과 로쟈
   źródło: GachaTitle.json :: dataList[id=133].content
   limit: do 120 znaków
   EN: New Target Extraction: Dieci South Section 4 Rodion
   PL: Nowa Ekstrakcja Celowana: Sekcja 4 Południowego Stowarzyszenia Dieci Rodion
409. [Przedmioty, sklep i profil gracza [134] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=134].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Przedmioty, sklep i profil gracza [135] — tekst] 신규 E.G.O 특정 추출 초롱 싱클레어
   źródło: GachaTitle.json :: dataList[id=135].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Lantern for Sinclair
   PL: Nowa Ekstrakcja Celowana E.G.O: Latarnia dla Sinclaira
411. [Przedmioty, sklep i profil gracza [136] — tekst] 신규 E.G.O 특정 추출 공즉시색 히스클리프
   źródło: GachaTitle.json :: dataList[id=136].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Ya Śūnyatā Tad Rūpam for Heathcliff
   PL: Nowa Ekstrakcja Celowana E.G.O: Ya Śūnyatā Tad Rūpam dla Heathcliffa
412. [Przedmioty, sklep i profil gracza [137] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=137].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Przedmioty, sklep i profil gracza [138] — tekst] 제1회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=138].content
   limit: do 120 znaków
   EN: The 1st Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 1. Nocy Walpurgii
414. [Przedmioty, sklep i profil gracza [139] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=139].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Przedmioty, sklep i profil gracza [140] — tekst] 신규 특정 추출 W사 3등급 정리 요원 이상
   źródło: GachaTitle.json :: dataList[id=140].content
   limit: do 120 znaków
   EN: New Target Extraction: W Corp. L3 Cleanup Agent Yi Sang
   PL: Nowa Ekstrakcja Celowana: Agentka Oczyszczania L3 W Corp. Yi Sang
416. [Przedmioty, sklep i profil gracza [141] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=141].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Przedmioty, sklep i profil gracza [142] — tekst] 신규 특정 추출 쌍갈고리 해적단 부선장 그레고르 · LCCB 대리 료슈
   źródło: GachaTitle.json :: dataList[id=142].content
   limit: do 120 znaków
   EN: New Target Extraction: Twinhook Pirates First mate Gregor & LCCB Assistant Manager Ryōshū
   PL: Nowa Ekstrakcja Celowana: Pierwszy Oficer Piratów Podwójnego Haka Gregor i Zastępca Kierownika LCCB Ryōshū
418. [Przedmioty, sklep i profil gracza [143] — tekst] 신규 특정 추출 중지 작은 아우 돈키호테 · 뫼르소
   źródło: GachaTitle.json :: dataList[id=143].content
   limit: do 120 znaków
   EN: New Target Extraction: The Middle Little Sister Don Quixote & Little Brother Meursault
   PL: Nowa Ekstrakcja Celowana: Młodsza Siostra Środkowego Don Quixote i Młodszy Brat Środkowego Meursault
419. [Przedmioty, sklep i profil gracza [6] — tekst] 시즌 3 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=6].content
   limit: do 120 znaków
   EN: [Season 3] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 3
420. [Przedmioty, sklep i profil gracza [144] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=144].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Przedmioty, sklep i profil gracza [145] — tekst] 신규 특정 추출 피쿼드호 작살잡이 히스클리프 · 일등 항해사 이상
   źródło: GachaTitle.json :: dataList[id=145].content
   limit: do 120 znaków
   EN: New Target Extraction: The Pequod Harpooneer Heathcliff & First Mate Yi Sang
   PL: Nowa Ekstrakcja Celowana: Harpunnik Pequoda Heathcliff i Pierwszy Oficer Yi Sang
422. [Przedmioty, sklep i profil gracza [146] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=146].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Przedmioty, sklep i profil gracza [147] — tekst] 신규 E.G.O 특정 추출 집행 로쟈
   źródło: GachaTitle.json :: dataList[id=147].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Pursuance for Rodion
   PL: Nowa Ekstrakcja Celowana E.G.O: Egzekucja dla Rodion
424. [Przedmioty, sklep i profil gracza [148] — tekst] 신규 특정 추출 남부 섕크 협회 4과 부장 싱클레어 · 4과 오티스
   źródło: GachaTitle.json :: dataList[id=148].content
   limit: do 120 znaków
   EN: New Target Extraction: Cinq South S4 Director Sinclair & S4 Outis
   PL: Nowa Ekstrakcja Celowana: Dyrektorka Sekcji 4 Południowego Stowarzyszenia Cinq Sinclair i Sekcja 4 Outis
425. [Przedmioty, sklep i profil gracza [149] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=149].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Przedmioty, sklep i profil gracza [150] — tekst] 신규 E.G.O 특정 추출 20번구의 기적
   źródło: GachaTitle.json :: dataList[id=150].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Miracle in District 20
   PL: Nowa Ekstrakcja Celowana E.G.O: Cud w Dystrykcie 20
427. [Przedmioty, sklep i profil gracza [151] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=151].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Przedmioty, sklep i profil gracza [152] — tekst] 제2회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=152].content
   limit: do 120 znaków
   EN: The 2nd Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 2. Nocy Walpurgii
429. [Przedmioty, sklep i profil gracza [153] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=153].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Przedmioty, sklep i profil gracza [154] — tekst] 신규 특정 추출 남부 디에치 협회 4과 홍루 · 이상
   źródło: GachaTitle.json :: dataList[id=154].content
   limit: do 120 znaków
   EN: New Target Extraction: Dieci South Section 4 Hong Lu & Yi Sang
   PL: Nowa Ekstrakcja Celowana: Sekcja 4 Południowego Stowarzyszenia Dieci Hong Lu i Yi Sang
431. [Przedmioty, sklep i profil gracza [155] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=155].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Przedmioty, sklep i profil gracza [156] — tekst] 신규 특정 추출 피쿼드호 선장 이스마엘
   źródło: GachaTitle.json :: dataList[id=156].content
   limit: do 120 znaków
   EN: New Target Extraction: The Pequod Captain Ishmael
   PL: Nowa Ekstrakcja Celowana: Kapitan Pequoda Ishmael
433. [Przedmioty, sklep i profil gracza [157] — tekst] 신규 E.G.O 특정 추출 소망석 돈키호테
   źródło: GachaTitle.json :: dataList[id=157].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Wishing Cairn for Don Quixote
   PL: Nowa Ekstrakcja Celowana E.G.O: Kopczyk Życzeń dla Don Quixote
434. [Przedmioty, sklep i profil gracza [158] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=158].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Przedmioty, sklep i profil gracza [159] — tekst] 신규 특정 추출 육참골단
   źródło: GachaTitle.json :: dataList[id=159].content
   limit: do 120 znaków
   EN: New Target Extraction: Yield My Flesh to Claim Their Bones
   PL: Nowa Ekstrakcja Celowana: Oddam Ciało, by Złamać Ich Kości
436. [Przedmioty, sklep i profil gracza [160] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=160].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Przedmioty, sklep i profil gracza [161] — tekst] 신규 특정 추출 남부 리우 협회 4과 부장 로쟈 · 4과 료슈
   źródło: GachaTitle.json :: dataList[id=161].content
   limit: do 120 znaków
   EN: New Target Extraction: Liu South S4 Director Rodion & S4 Ryōshū
   PL: Nowa Ekstrakcja Celowana: Dyrektorka Sekcji 4 Południowego Stowarzyszenia Liu Rodion i Sekcja 4 Ryōshū
438. [Przedmioty, sklep i profil gracza [162] — tekst] 신규 E.G.O 특정 추출 가시 화원 그레고르
   źródło: GachaTitle.json :: dataList[id=162].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Garden of Thorns for Gregor
   PL: Nowa Ekstrakcja Celowana E.G.O: Ogród Cierni dla Gregora
439. [Przedmioty, sklep i profil gracza [163] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=163].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Przedmioty, sklep i profil gracza [164] — tekst] 신규 특정 추출 남부 외우피 협회 3과 히스클리프
   źródło: GachaTitle.json :: dataList[id=164].content
   limit: do 120 znaków
   EN: New Target Extraction: Öufi South Section 3 Heathcliff
   PL: Nowa Ekstrakcja Celowana: Sekcja 3 Południowego Stowarzyszenia Öufi Heathcliff
441. [Przedmioty, sklep i profil gracza [7] — tekst] 시즌 4 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=7].content
   limit: do 120 znaków
   EN: [Season 4] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 4
442. [Przedmioty, sklep i profil gracza [165] — tekst] 신규 특정 추출 워더링하이츠 치프 버틀러 오티스 · 데드레빗츠 보스 뫼르소
   źródło: GachaTitle.json :: dataList[id=165].content
   limit: do 120 znaków
   EN: New Target Extraction: Wuthering Heights Chief Butler Outis & Dead Rabbits Boss Meursault
   PL: Nowa Ekstrakcja Celowana: Główna Kamerdynerka Wichrowych Wzgórz Outis i Szef Martwych Królików Meursault
443. [Przedmioty, sklep i profil gracza [166] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=166].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Przedmioty, sklep i profil gracza [167] — tekst] 신규 특정 추출 에드가 가문 승계자 그레고르 · 워더링하이츠 버틀러 파우스트
   źródło: GachaTitle.json :: dataList[id=167].content
   limit: do 120 znaków
   EN: New Target Extraction: Edgar Family Heir Gregor & Wuthering Heights Butler Faust
   PL: Nowa Ekstrakcja Celowana: Dziedzic Rodu Edgarów Gregor i Kamerdyner Wichrowych Wzgórz Faust
445. [Przedmioty, sklep i profil gracza [168] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=168].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Przedmioty, sklep i profil gracza [169] — tekst] 신규 특정 추출 에드가 가문 치프 버틀러 료슈 · 버틀러 이스마엘
   źródło: GachaTitle.json :: dataList[id=169].content
   limit: do 120 znaków
   EN: New Target Extraction: Edgar Family Chief Butler Ryōshū & Butler Ishmael
   PL: Nowa Ekstrakcja Celowana: Główna Kamerdynerka Rodu Edgarów Ryōshū i Kamerdyner Ishmael
447. [Przedmioty, sklep i profil gracza [170] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=170].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Przedmioty, sklep i profil gracza [171] — tekst] 제3회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=171].content
   limit: do 120 znaków
   EN: The 3rd Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 3. Nocy Walpurgii
449. [Przedmioty, sklep i profil gracza [172] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=172].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Przedmioty, sklep i profil gracza [173] — tekst] 신규 특정 추출 약지 점묘파 스튜던트 이상 · 오티스
   źródło: GachaTitle.json :: dataList[id=173].content
   limit: do 120 znaków
   EN: New Target Extraction: The Ring Pointillist Student Yi Sang & Outis
   PL: Nowa Ekstrakcja Celowana: Student Pointylizmu Serdecznego Yi Sang i Outis
451. [Przedmioty, sklep i profil gracza [174] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=174].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Przedmioty, sklep i profil gracza [175] — tekst] 신규 E.G.O 특정 추출 낮은울음 홍루 · 싱클레어
   źródło: GachaTitle.json :: dataList[id=175].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Cavernous Wailing for Hong Lu & Sinclair
   PL: Nowa Ekstrakcja Celowana E.G.O: Głębokie Wyjenie dla Hong Lu i Sinclaira
453. [Przedmioty, sklep i profil gracza [176] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=176].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Przedmioty, sklep i profil gracza [177] — tekst] 신규 특정 추출 시간살인시간
   źródło: GachaTitle.json :: dataList[id=177].content
   limit: do 120 znaków
   EN: New Target Extraction: Timekilling Time
   PL: Nowa Ekstrakcja Celowana: Czas Zabijania Czasu
455. [Przedmioty, sklep i profil gracza [178] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=178].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Przedmioty, sklep i profil gracza [179] — tekst] 신규 특정 추출 T사 3등급 징수직 직원 돈키호테 · 2등급 징수직 직원 로쟈
   źródło: GachaTitle.json :: dataList[id=179].content
   limit: do 140 znaków
   EN: New Target Extraction: T Corp. Class 3 Collection Staff Don Quixote & Class 2 Collection Staff Rodion
   PL: Nowa Ekstrakcja Celowana: Poborca 3. klasy T Corp. Don Quixote i Poborca 2. klasy T Corp. Rodion
457. [Przedmioty, sklep i profil gracza [180] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=180].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Przedmioty, sklep i profil gracza [181] — tekst] 신규 인격 · E.G.O 특정 추출 남부 디에치 협회 4과 부장 뫼르소 · 경멸, 경외 료슈
   źródło: GachaTitle.json :: dataList[id=181].content
   limit: do 120 znaków
   EN: New Target Extraction: Dieci South S4 Director Meursault & Contempt, Awe Ryōshū
   PL: Nowa Ekstrakcja Celowana Tożsamości i E.G.O: Dyrektorka Sekcji 4 Stow. Dieci Południa Meursault i Pogarda, Trwoga Ryōshū
459. [Przedmioty, sklep i profil gracza [182] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=182].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Przedmioty, sklep i profil gracza [183] — tekst] 신규 인격 · E.G.O 특정 추출 W사 3등급 정리 요원 팀장 오티스 · 흉탄 히스클리프
   źródło: GachaTitle.json :: dataList[id=183].content
   limit: do 120 znaków
   EN: New Target Extraction: W Corp. L3 Cleanup Captain Outis & Fell Bullet Heathcliff
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Kapitan Agentek Oczyszczania L3 W Corp. Outis i Złowroga Kula Heathcliff
461. [Przedmioty, sklep i profil gracza [184] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=184].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Przedmioty, sklep i profil gracza [185] — tekst] 신규 인격 · E.G.O 특정 추출 멀티크랙 사무소 대표 파우스트 · 차원찢개 오티스
   źródło: GachaTitle.json :: dataList[id=185].content
   limit: do 120 znaków
   EN: New Target Extraction: MultiCrack Office Rep Faust & Dimension Shredder Outis
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Szefowa Biura MultiCrack Faust i Rozpruwacz Wymiarów Outis
463. [Przedmioty, sklep i profil gracza [186] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=186].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Przedmioty, sklep i profil gracza [187] — tekst] 신규 인격 특정 추출 와일드헌트 히스클리프
   źródło: GachaTitle.json :: dataList[id=187].content
   limit: do 120 znaków
   EN: New Target Extraction: Wild Hunt Heathcliff
   PL: Nowa Ekstrakcja Celowana Tożsamości: Dziki Gon Heathcliff
465. [Przedmioty, sklep i profil gracza [188] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=188].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Przedmioty, sklep i profil gracza [189] — tekst] 제4회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=189].content
   limit: do 120 znaków
   EN: The 4th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 4. Nocy Walpurgii
467. [Przedmioty, sklep i profil gracza [190] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=190].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Przedmioty, sklep i profil gracza [191] — tekst] 신규 인격 · E.G.O 특정 추출 북부 제바찌 협회 3과 로쟈 · 지난 날 이스마엘
   źródło: GachaTitle.json :: dataList[id=191].content
   limit: do 120 znaków
   EN: New Identity & E.G.O Target Extraction: Devyat' North Section 3 Rodion & Bygone Days Ishmael
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Sekcja 3 Północnego Stowarzyszenia Diewiat' Rodion i Przeszłe Dni Ishmael
469. [Przedmioty, sklep i profil gracza [192] — tekst] 신규 인격 특정 추출 서부 츠바이 협회 3과 이스마엘
   źródło: GachaTitle.json :: dataList[id=192].content
   limit: do 120 znaków
   EN: New Target Extraction: Zwei West Section 3 Ishmael
   PL: Nowa Ekstrakcja Celowana Tożsamości: Sekcja 3 Zachodniego Stowarzyszenia Zwei Ishmael
470. [Przedmioty, sklep i profil gracza [193] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=193].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Przedmioty, sklep i profil gracza [194] — tekst] 신규 인격 특정 추출 서부 섕크 협회 3과 뫼르소 · 서부 츠바이 협회 3과 싱클레어
   źródło: GachaTitle.json :: dataList[id=194].content
   limit: do 120 znaków
   EN: New Target Extraction: Cinq West Section 3 Meursault & Zwei West Section 3 Sinclair
   PL: Nowa Ekstrakcja Celowana Tożsamości: Sekcja 3 Zach. Stow. Cinq Meursault i Sekcja 3 Zach. Stow. Zwei Sinclair
472. [Przedmioty, sklep i profil gracza [195] — tekst] 신규 인격 특정 추출 라만차랜드 이발사 오티스 · 송곳니 사냥 사무소 해결사 홍루
   źródło: GachaTitle.json :: dataList[id=195].content
   limit: do 120 znaków
   EN: New Target Extraction: The Barber of La Manchaland Outis & Fanghunt Office Fixer Hong Lu
   PL: Nowa Ekstrakcja Celowana Tożsamości: Cyruliczka La Manchalandu Outis i Fikser Biura Łowców Kłów Hong Lu
473. [Przedmioty, sklep i profil gracza [8] — tekst] 시즌 5 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=8].content
   limit: do 120 znaków
   EN: [Season 5] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 5
474. [Przedmioty, sklep i profil gracza [196] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=196].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Przedmioty, sklep i profil gracza [197] — tekst] 신규 인격 특정 추출 라만차랜드 신부 그레고르
   źródło: GachaTitle.json :: dataList[id=197].content
   limit: do 120 znaków
   EN: New Target Extraction: The Priest of La Manchaland Gregor
   PL: Nowa Ekstrakcja Celowana Tożsamości: Kapelan La Manchalandu Gregor
476. [Przedmioty, sklep i profil gracza [198] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=198].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Przedmioty, sklep i profil gracza [199] — tekst] 신규 인격 · E.G.O 특정 추출 라만차랜드 공주 로쟈 · 흉탄 이상
   źródło: GachaTitle.json :: dataList[id=199].content
   limit: do 130 znaków
   EN: New Identity & E.G.O Target Extraction: The Princess of La Manchaland Rodion & Fell Bullet Yi Sang
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Księżniczka La Manchalandu Rodion i Złowroga Kula Yi Sang
478. [Przedmioty, sklep i profil gracza [200] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=200].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Przedmioty, sklep i profil gracza [201] — tekst] 신규 인격 · E.G.O  특정 추출 북부 제뱌찌 협회 3과 싱클레어 · 쏠린 관성 히스클리프
   źródło: GachaTitle.json :: dataList[id=201].content
   limit: do 140 znaków
   EN: New Identity & E.G.O Target Extraction: Devyat' North Section 3 Sinclair & Asymmetrical Inertia Heathcliff
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Sekcja 3 Północnego Stowarzyszenia Diewiat' Sinclair i Asymetryczna Bezwładność Heathcliff
480. [Przedmioty, sklep i profil gracza [202] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=202].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Przedmioty, sklep i profil gracza [203] — tekst] 신규 인격 특정 추출 라만차랜드 실장 돈키호테
   źródło: GachaTitle.json :: dataList[id=203].content
   limit: do 120 znaków
   EN: New Target Extraction: The Manager of La Manchaland Don Quixote
   PL: Nowa Ekstrakcja Celowana Tożsamości: Zarządczyni La Manchalandu Don Quixote
482. [Przedmioty, sklep i profil gracza [204] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=204].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Przedmioty, sklep i profil gracza [205] — tekst] 신규 E.G.O 특정 추출 20번구의 기적 BokGak
   źródło: GachaTitle.json :: dataList[id=205].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Miracle in District 20 BokGak
   PL: Nowa Ekstrakcja Celowana E.G.O: Cud w Dystrykcie 20 BokGak
484. [Przedmioty, sklep i profil gracza [206] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=206].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Przedmioty, sklep i profil gracza [207] — tekst] 제5회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=207].content
   limit: do 120 znaków
   EN: The 5th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 5. Nocy Walpurgii
486. [Przedmioty, sklep i profil gracza [208] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=208].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Przedmioty, sklep i profil gracza [209] — tekst] 신규 특정 추출 LCB 정기검진
   źródło: GachaTitle.json :: dataList[id=209].content
   limit: do 120 znaków
   EN: New Target Extraction: LCB Regular Check-up
   PL: Nowa Ekstrakcja Celowana: Okresowe Badania LCB
488. [Przedmioty, sklep i profil gracza [210] — tekst] 특정 추출 검계 · 흑운회
   źródło: GachaTitle.json :: dataList[id=210].content
   limit: do 120 znaków
   EN: Target Extraction: Blade Lineage & Kurokumo Clan
   PL: Ekstrakcja Celowana: Ród Ostrza i Klan Kurokumo
489. [Przedmioty, sklep i profil gracza [211] — tekst] 신규 특정 추출 흑운회 부조장 이스마엘
   źródło: GachaTitle.json :: dataList[id=211].content
   limit: do 120 znaków
   EN: New Target Extraction: Kurokumo Clan Captain Ishmael
   PL: Nowa Ekstrakcja Celowana: Kapitan Klanu Kurokumo Ishmael
490. [Przedmioty, sklep i profil gracza [212] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=212].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Przedmioty, sklep i profil gracza [213] — tekst] 신규 인격 · E.G.O 특정 추출 남부 리우 협회 3과 이상 · 흉통 파우스트
   źródło: GachaTitle.json :: dataList[id=213].content
   limit: do 120 znaków
   EN: New Identity & E.G.O Target Extraction: Liu South Section 3 Yi Sang & Thoracalgia Faust
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Sekcja 3 Południowego Stowarzyszenia Liu Yi Sang i Torakalgia Faust
492. [Przedmioty, sklep i profil gracza [214] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=214].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Przedmioty, sklep i profil gracza [215] — tekst] 신규 특정 추출 불주먹 사무소 생존자 그레고르 · 동부 섕크 협회 3과 돈키호테
   źródło: GachaTitle.json :: dataList[id=215].content
   limit: do 120 znaków
   EN: New Target Extraction: Firefist Office Survivor Gregor & Cinq East Section 3 Don Quixote
   PL: Nowa Ekstrakcja Celowana: Ocalały z Biura Ognistej Pięści Gregor i Sekcja 3 Wschodniego Stowarzyszenia Cinq Don Quixote
494. [Przedmioty, sklep i profil gracza [216] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=216].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Przedmioty, sklep i profil gracza [217] — tekst] 신규 특정 추출 심야청소
   źródło: GachaTitle.json :: dataList[id=217].content
   limit: do 120 znaków
   EN: New Target Extraction: Nocturnal Sweeping
   PL: Nowa Ekstrakcja Celowana: Nocne Sprzątanie
496. [Przedmioty, sklep i profil gracza [218] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=218].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Przedmioty, sklep i profil gracza [219] — tekst] 신규 특정 추출 중지 작은 아우 싱클레어
   źródło: GachaTitle.json :: dataList[id=219].content
   limit: do 120 znaków
   EN: New Target Extraction: The Middle Little Brother Sinclair
   PL: Nowa Ekstrakcja Celowana: Młodszy Brat Środkowego Sinclair
498. [Przedmioty, sklep i profil gracza [220] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=220].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Przedmioty, sklep i profil gracza [221] — tekst] 신규 E.G.O 특정 추출 지정 재판 로쟈
   źródło: GachaTitle.json :: dataList[id=221].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Indicant's Trial for Rodion
   PL: Nowa Ekstrakcja Celowana E.G.O: Próba Wskazującego dla Rodion
500. [Przedmioty, sklep i profil gracza [222] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=222].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Przedmioty, sklep i profil gracza [223] — tekst] 신규 특정 추출 R사 제 4무리 순록팀 홍루
   źródło: GachaTitle.json :: dataList[id=223].content
   limit: do 120 znaków
   EN: New Target Extraction: R Corp. 4th Pack Reindeer Hong Lu
   PL: Nowa Ekstrakcja Celowana: Zespół Reniferów 4. Stada R Corp. Hong Lu
502. [Przedmioty, sklep i profil gracza [9] — tekst] 시즌 6 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=9].content
   limit: do 120 znaków
   EN: [Season 6] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 6
503. [Przedmioty, sklep i profil gracza [224] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=224].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
504. [Przedmioty, sklep i profil gracza [225] — tekst] 신규 특정 추출 흑수 - 사 로쟈 · 그레고르
   źródło: GachaTitle.json :: dataList[id=225].content
   limit: do 120 znaków
   EN: New Target Extraction: Heishou Pack - Si Branch Rodion & Gregor
   PL: Nowa Ekstrakcja Celowana: Wataha Heishou - Gałąź Si Rodion i Gregor
505. [Przedmioty, sklep i profil gracza [226] — tekst] 신규 특정 추출 흑수 - 묘 필두 파우스트
   źródło: GachaTitle.json :: dataList[id=226].content
   limit: do 120 znaków
   EN: New Target Extraction: Heishou Pack - Mao Branch Adept Faust
   PL: Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź Mao Faust
506. [Przedmioty, sklep i profil gracza [227] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=227].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Przedmioty, sklep i profil gracza [228] — tekst] 신규 특정 추출 가주 후보 이스마엘
   źródło: GachaTitle.json :: dataList[id=228].content
   limit: do 120 znaków
   EN: New Target Extraction: Family Hierarch Candidate Ishmael
   PL: Nowa Ekstrakcja Celowana: Kandydatka na Głowę Rodu Ishmael
508. [Przedmioty, sklep i profil gracza [229] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=229].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Przedmioty, sklep i profil gracza [230] — tekst] 신규 특정 추출 동부 엄지 카포 IIII 뫼르소 · 솔다토 II 싱클레어
   źródło: GachaTitle.json :: dataList[id=230].content
   limit: do 120 znaków
   EN: New Target Extraction: The Thumb East Capo IIII Meursault & Soldato II Sinclair
   PL: Nowa Ekstrakcja Celowana: Kapo IIII Kciuka ze Wschodu Meursault i Soldato II Sinclair
510. [Przedmioty, sklep i profil gracza [231] — tekst] 특정 추출 라만차랜드 - 혈귀
   źródło: GachaTitle.json :: dataList[id=231].content
   limit: do 120 znaków
   EN: Target Extraction: La Manchaland - Bloodfiends
   PL: Ekstrakcja Celowana: La Manchaland — Krwiopijcy
511. [Przedmioty, sklep i profil gracza [232] — tekst] 신규 특정 추출 N사 E.G.O::흉탄 이상
   źródło: GachaTitle.json :: dataList[id=232].content
   limit: do 120 znaków
   EN: New Target Extraction: N Corp. E.G.O::Fell Bullet Yi Sang
   PL: Nowa Ekstrakcja Celowana: Korp. N E.G.O::Złowroga Kula Yi Sang
512. [Przedmioty, sklep i profil gracza [233] — tekst] 제1·2회 발푸르기스의 밤 특정 추출 BokGak
   źródło: GachaTitle.json :: dataList[id=233].content
   limit: do 120 znaków
   EN: The 1st & 2nd Walpurgis Night Target Extraction BokGak
   PL: Ekstrakcja Celowana 1. i 2. Nocy Walpurgii BokGak
513. [Przedmioty, sklep i profil gracza [234] — tekst] 제6회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=234].content
   limit: do 120 znaków
   EN: The 6th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 6. Nocy Walpurgii
514. [Przedmioty, sklep i profil gracza [235] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=235].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Przedmioty, sklep i profil gracza [236] — tekst] 신규 특정 추출 시간살인시간 BokGak
   źródło: GachaTitle.json :: dataList[id=236].content
   limit: do 120 znaków
   EN: New Target Extraction: Timekilling Time BokGak
   PL: Nowa Ekstrakcja Celowana: Czas Zabijania Czasu BokGak
516. [Przedmioty, sklep i profil gracza [237] — tekst] 특정 추출 흑수
   źródło: GachaTitle.json :: dataList[id=237].content
   limit: do 120 znaków
   EN: Target Extraction: Heishou Pack
   PL: Ekstrakcja Celowana: Wataha Heishou
517. [Przedmioty, sklep i profil gracza [238] — tekst] 신규 특정 추출 홍원 군주 홍루
   źródło: GachaTitle.json :: dataList[id=238].content
   limit: do 120 znaków
   EN: New Target Extraction: The Lord of Hongyuan Hong Lu
   PL: Nowa Ekstrakcja Celowana: Władca Hongyuanu Hong Lu
518. [Przedmioty, sklep i profil gracza [239] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=239].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Przedmioty, sklep i profil gracza [240] — tekst] 신규 특정 추출 절차탁춘
   źródło: GachaTitle.json :: dataList[id=240].content
   limit: do 120 znaków
   EN: New Target Extraction: Spring Cultivation
   PL: Nowa Ekstrakcja Celowana: Wiosenny Szlif
520. [Przedmioty, sklep i profil gracza [241] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=241].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Przedmioty, sklep i profil gracza [242] — tekst] 신규 특정 추출 N사 E.G.O::경멸, 경외 료슈
   źródło: GachaTitle.json :: dataList[id=242].content
   limit: do 120 znaków
   EN: New Target Extraction: N Corp. E.G.O::Contempt, Awe Ryōshū
   PL: Nowa Ekstrakcja Celowana: Korp. N E.G.O::Pogarda, Trwoga Ryōshū
522. [Przedmioty, sklep i profil gracza [243] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=243].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Przedmioty, sklep i profil gracza [244] — tekst] 신규 E.G.O 특정 추출 선의의 순례
   źródło: GachaTitle.json :: dataList[id=244].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Pilgrimage of Compassion
   PL: Nowa Ekstrakcja Celowana E.G.O: Pielgrzymka Współczucia
524. [Przedmioty, sklep i profil gracza [245] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=245].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Przedmioty, sklep i profil gracza [246] — tekst] 신규 특정 추출 동부 시 협회 3과 파우스트
   źródło: GachaTitle.json :: dataList[id=246].content
   limit: do 120 znaków
   EN: New Target Extraction: Shi East Section 3 Faust
   PL: Nowa Ekstrakcja Celowana: Sekcja 3 Wschodniego Stowarzyszenia Shi Faust
526. [Przedmioty, sklep i profil gracza [247] — tekst] 특정 추출 W사
   źródło: GachaTitle.json :: dataList[id=247].content
   limit: do 120 znaków
   EN: Target Extraction: W Corp.
   PL: Ekstrakcja Celowana: W Corp.
527. [Przedmioty, sklep i profil gracza [248] — tekst] 신규 특정 추출 워프특급 살인사건 BokGak
   źródło: GachaTitle.json :: dataList[id=248].content
   limit: do 120 znaków
   EN: New Target Extraction: Murder on the WARP Express BokGak
   PL: Nowa Ekstrakcja Celowana: Morderstwo w Ekspresie WARP BokGak
528. [Przedmioty, sklep i profil gracza [249] — tekst] 제2·3회 발푸르기스의 밤 특정 추출 BokGak
   źródło: GachaTitle.json :: dataList[id=249].content
   limit: do 120 znaków
   EN: The 2nd & 3rd Walpurgis Night Target Extraction BokGak
   PL: Ekstrakcja Celowana 2. i 3. Nocy Walpurgii BokGak
529. [Przedmioty, sklep i profil gracza [250] — tekst] 제7회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=250].content
   limit: do 120 znaków
   EN: The 7th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 7. Nocy Walpurgii
530. [Przedmioty, sklep i profil gracza [251] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=251].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Przedmioty, sklep i profil gracza [252] — tekst] 신규 특정 추출 흑수 - 유 필두 히스클리프 · 흑수 미 돈키호테
   źródło: GachaTitle.json :: dataList[id=252].content
   limit: do 120 znaków
   EN: New Target Extraction: Heishou Pack - You Branch Adept Heathcliff & Wei Branch Don Quixote
   PL: Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź You Heathcliff i Wataha Heishou - Gałąź Wei Don Quixote
532. [Przedmioty, sklep i profil gracza [253] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=253].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Przedmioty, sklep i profil gracza [254] — tekst] 신규 특정 추출 홍원 방랑무사 료슈
   źródło: GachaTitle.json :: dataList[id=254].content
   limit: do 120 znaków
   EN: New Target Extraction: Drifting Blade of Hongyuan Ryōshū
   PL: Nowa Ekstrakcja Celowana: Wędrowna Szermierka z Hongyuanu Ryōshū
534. [Przedmioty, sklep i profil gracza [255] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=255].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Przedmioty, sklep i profil gracza [256] — tekst] 신규 특정 추출 R사 제 4무리 순록팀 로쟈
   źródło: GachaTitle.json :: dataList[id=256].content
   limit: do 120 znaków
   EN: New Target Extraction: R Corp. 4th Pack Reindeer Rodion
   PL: Nowa Ekstrakcja Celowana: Zespół Reniferów 4. Stada R Corp. Rodion
536. [Przedmioty, sklep i profil gracza [10] — tekst] 시즌 7 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=10].content
   limit: do 120 znaków
   EN: [Season 7] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 7
537. [Przedmioty, sklep i profil gracza [257] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=257].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Przedmioty, sklep i profil gracza [258] — tekst] 신규 특정 추출 검지 수행자:【쪽지】 파우스트 · LCA 우제트 선봉 3팀 팀장 오티스
   źródło: GachaTitle.json :: dataList[id=258].content
   limit: do 140 znaków
   EN: New Target Extraction: The Index Proselyte:【Paper Slip】 Faust & LCA Udjat Vanguard Team 3 Leader Outis
   PL: Nowa Ekstrakcja Celowana: Akolitka Wskazującego:【Karteczka】 Faust i Dowódczyni 3. Zespołu Szpicy Udjat LCA Outis
539. [Przedmioty, sklep i profil gracza [259] — tekst] 신규 특정 추출 검지 대행자 - 개화 E.G.O::대행 돈키호테
   źródło: GachaTitle.json :: dataList[id=259].content
   limit: do 120 znaków
   EN: New Target Extraction: The Index Proxy - Effloresced E.G.O::Procuration Don Quixote
   PL: Nowa Ekstrakcja Celowana: Pełnomocniczka Wskazującego - Rozkwitłe E.G.O::Pełnomocnictwo Don Quixote
540. [Przedmioty, sklep i profil gracza [260] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=260].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Przedmioty, sklep i profil gracza [261] — tekst] 신규 특정 추출 거미집 중지 제자 이스마엘
   źródło: GachaTitle.json :: dataList[id=261].content
   limit: do 120 znaków
   EN: New Target Extraction: The House of Spiders: The Middle Apprentice Ishmael
   PL: Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Środkowego Ishmael
542. [Przedmioty, sklep i profil gracza [262] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=262].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Przedmioty, sklep i profil gracza [263] — tekst] 신규 특정 추출 거미집 소지 제자 싱클레어 · 로보토미 E.G.O::램프 그레고르
   źródło: GachaTitle.json :: dataList[id=263].content
   limit: do 140 znaków
   EN: New Target Extraction: The House of Spiders: The Pinky Apprentice Sinclair & Lobotomy E.G.O::Lamp Gregor
   PL: Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Małego Palca Sinclair i Lobotomy E.G.O::Lampa Gregor
544. [Przedmioty, sklep i profil gracza [264] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=264].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Przedmioty, sklep i profil gracza [265] — tekst] 특정 추출 홍원
   źródło: GachaTitle.json :: dataList[id=265].content
   limit: do 120 znaków
   EN: Target Extraction: Hongyuan
   PL: Ekstrakcja Celowana: Hongyuan
546. [Przedmioty, sklep i profil gracza [266] — tekst] 신규 특정 추출 거미집 검지 아비 이상
   źródło: GachaTitle.json :: dataList[id=266].content
   limit: do 120 znaków
   EN: New Target Extraction: The House of Spiders: The Index Nursefather Yi Sang
   PL: Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Wskazującego Yi Sang
547. [Przedmioty, sklep i profil gracza [267] — tekst] 제3·4회 발푸르기스의 밤 특정 추출 BokGak
   źródło: GachaTitle.json :: dataList[id=267].content
   limit: do 120 znaków
   EN: The 3rd & 4th Walpurgis Night Target Extraction BokGak
   PL: Ekstrakcja Celowana 3. i 4. Nocy Walpurgii BokGak
548. [Przedmioty, sklep i profil gracza [268] — tekst] 제8회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=268].content
   limit: do 120 znaków
   EN: The 8th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 8. Nocy Walpurgii
549. [Przedmioty, sklep i profil gracza [269] — tekst] 특정 추출 히스클리프
   źródło: GachaTitle.json :: dataList[id=269].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Przedmioty, sklep i profil gracza [270] — tekst] 신규 특정 추출 LCB 정기검진 BokGak
   źródło: GachaTitle.json :: dataList[id=270].content
   limit: do 120 znaków
   EN: New Target Extraction: LCB Regular Check-up BokGak
   PL: Nowa Ekstrakcja Celowana: Okresowe Badania LCB BokGak
551. [Przedmioty, sklep i profil gracza [271] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=271].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Przedmioty, sklep i profil gracza [272] — tekst] 신규 특정 추출 거미집 약지 아비 홍루 · 약지 제자 파우스트
   źródło: GachaTitle.json :: dataList[id=272].content
   limit: do 120 znaków
   EN: New Target Extraction: The House of Spiders: The Ring Nursefather Hong Lu & Apprentice Faust
   PL: Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Serdecznego Hong Lu i Uczennica Serdecznego Faust
553. [Przedmioty, sklep i profil gracza [273] — tekst] 특정 추출 돈키호테
   źródło: GachaTitle.json :: dataList[id=273].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Przedmioty, sklep i profil gracza [274] — tekst] 신규 인격 특정 추출 타래 엮기
   źródło: GachaTitle.json :: dataList[id=274].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Twining Threads
   PL: Nowa Ekstrakcja Celowana Tożsamości: Splatanie Pasm
555. [Przedmioty, sklep i profil gracza [275] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=275].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Przedmioty, sklep i profil gracza [276] — tekst] 신규 인격 특정 추출 심야청소 BokGak
   źródło: GachaTitle.json :: dataList[id=276].content
   limit: do 120 znaków
   EN: New Target Extraction: Nocturnal Sweeping BokGak
   PL: Nowa Ekstrakcja Celowana: Nocne Sprzątanie BokGak
557. [Przedmioty, sklep i profil gracza [277] — tekst] 특정 추출 싱클레어
   źródło: GachaTitle.json :: dataList[id=277].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Przedmioty, sklep i profil gracza [278] — tekst] 신규 인격 특정 추출 거미집의 검 료슈
   źródło: GachaTitle.json :: dataList[id=278].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Blade of the House of Spiders Ryōshū
   PL: Nowa Ekstrakcja Celowana Tożsamości: Ostrze Domu Pajęczyn Ryōshū
559. [Przedmioty, sklep i profil gracza [279] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=279].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Przedmioty, sklep i profil gracza [280] — tekst] 신규 인격 특정 추출 거미집 중지 아비 오티스
   źródło: GachaTitle.json :: dataList[id=280].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: The House of Spiders: The Middle Nursefather Outis
   PL: Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Środkowego Outis
561. [Przedmioty, sklep i profil gracza [281] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=281].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Przedmioty, sklep i profil gracza [282] — tekst] 신규 인격 · E.G.O 특정 추출 경험기억
   źródło: GachaTitle.json :: dataList[id=282].content
   limit: do 120 znaków
   EN: New Identity & E.G.O Target Extraction - Mnestic Experience
   PL: Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Pamięć Doświadczenia
563. [Przedmioty, sklep i profil gracza [283] — tekst] 특정 추출 오티스
   źródło: GachaTitle.json :: dataList[id=283].content
   (powtórzenie elementu 391 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Przedmioty, sklep i profil gracza [284] — tekst] 신규 인격 특정 추출 거미집 엄지 아비 로쟈 · 엄지 제자 히스클리프
   źródło: GachaTitle.json :: dataList[id=284].content
   limit: do 140 znaków
   EN: New Identity Target Extraction: The House of Spiders: The Thumb Nursefather Rodion & Apprentice Heathcliff
   PL: Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Kciuka Rodion i Uczeń Kciuka Heathcliff
565. [Przedmioty, sklep i profil gracza [285] — tekst] 제4·5회 발푸르기스의 밤 특정 추출 BokGak
   źródło: GachaTitle.json :: dataList[id=285].content
   limit: do 120 znaków
   EN: The 4th & 5th Walpurgis Night Target Extraction BokGak
   PL: Ekstrakcja Celowana 4. i 5. Nocy Walpurgii BokGak
566. [Przedmioty, sklep i profil gracza [286] — tekst] 제9회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=286].content
   limit: do 120 znaków
   EN: The 9th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 9. Nocy Walpurgii
567. [Przedmioty, sklep i profil gracza [287] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=287].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Przedmioty, sklep i profil gracza [288] — tekst] 신규 인격 특정 추출 LCE E.G.O::차원찢개 이상
   źródło: GachaTitle.json :: dataList[id=288].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: LCE E.G.O::Dimension Shredder Yi Sang
   PL: Nowa Ekstrakcja Celowana Tożsamości: LCE E.G.O::Rozpruwacz Wymiarów Yi Sang
569. [Przedmioty, sklep i profil gracza [289] — tekst] 특정 추출 홍루
   źródło: GachaTitle.json :: dataList[id=289].content
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Przedmioty, sklep i profil gracza [290] — tekst] 신규 E.G.O 특정 추출 난 가위를 낼게, 너는? 돈키호테
   źródło: GachaTitle.json :: dataList[id=290].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: I'll Go fer Scissors, How 'Bout You? Don Quixote
   PL: Nowa Ekstrakcja Celowana E.G.O: Idę po Nożyce, a Ty? Don Quixote
571. [Przedmioty, sklep i profil gracza [291] — tekst] 특정 추출 파우스트
   źródło: GachaTitle.json :: dataList[id=291].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Przedmioty, sklep i profil gracza [292] — tekst] 신규 인격 특정 추출 동부 섕크 협회 3과 홍루
   źródło: GachaTitle.json :: dataList[id=292].content
   limit: do 120 znaków
   EN: New Target Extraction: Cinq East Section 3 Hong Lu
   PL: Nowa Ekstrakcja Celowana: Sekcja 3 Wschodniego Stowarzyszenia Cinq Hong Lu
573. [Przedmioty, sklep i profil gracza [293] — tekst] 특정 추출 료슈
   źródło: GachaTitle.json :: dataList[id=293].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Przedmioty, sklep i profil gracza [294] — tekst] 신규 E.G.O 특정 추출 입주 신고 그레고르
   źródło: GachaTitle.json :: dataList[id=294].content
   limit: do 120 znaków
   EN: New E.G.O Target Extraction: Move-in Reg. Gregor
   PL: Nowa Ekstrakcja Celowana E.G.O: Zgłoszenie Zameldowania dla Gregora
575. [Przedmioty, sklep i profil gracza [295] — tekst] 특정 추출 뫼르소
   źródło: GachaTitle.json :: dataList[id=295].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Przedmioty, sklep i profil gracza [296] — tekst] 신규 인격 특정 추출 오트쿠튀르::르루주 부티크 이스마엘 · 오트쿠튀르::르누아르 신발관 료슈
   źródło: GachaTitle.json :: dataList[id=296].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Boutique du Rouge Ishmael & Le Noir Footwear Hall Ryōshū
   PL: Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Boutique du Rouge Ishmael i Pawilon Obuwia Le Noir Ryōshū
577. [Przedmioty, sklep i profil gracza [297] — tekst] 신규 인격 특정 추출 오트쿠튀르::수선실 로쟈
   źródło: GachaTitle.json :: dataList[id=297].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Haute Couture::Alteration Shop Rodion
   PL: Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Pracownia Poprawek Rodion
578. [Przedmioty, sklep i profil gracza [298] — tekst] 특정 추출 그레고르
   źródło: GachaTitle.json :: dataList[id=298].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Przedmioty, sklep i profil gracza [299] — tekst] 신규 인격 특정 추출 오트쿠튀르::르누아르 브랜드 매니저 돈키호테
   źródło: GachaTitle.json :: dataList[id=299].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Haute Couture::Le Noir Brand Manager Don Quixote
   PL: Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Menedżerka Marki Le Noir Don Quixote
580. [Przedmioty, sklep i profil gracza [11] — tekst] 시즌 8 - 3성 인격 확정 추출
   źródło: GachaTitle.json :: dataList[id=11].content
   limit: do 120 znaków
   EN: [Season 8] Assured Extraction: 3★ Identity
   PL: Ekstrakcja Gwarantowana 3★ Tożsamości Sezonu 8
581. [Przedmioty, sklep i profil gracza [300] — tekst] 특정 추출 이스마엘
   źródło: GachaTitle.json :: dataList[id=300].content
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Przedmioty, sklep i profil gracza [301] — tekst] 특정 추출 약지
   źródło: GachaTitle.json :: dataList[id=301].content
   limit: do 120 znaków
   EN: Target Extraction: The Ring
   PL: Ekstrakcja Celowana: Serdeczny
583. [Przedmioty, sklep i profil gracza [302] — tekst] 신규 인격 특정 추출 오트쿠튀르::르루주 붉은 신 싱클레어
   źródło: GachaTitle.json :: dataList[id=302].content
   limit: do 120 znaków
   EN: New Identity Target Extraction: Haute Couture::The Crimson God of Le Rouge Sinclair
   PL: Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Czerwony Bóg Le Rouge Sinclair
584. [Przedmioty, sklep i profil gracza [303] — tekst] 특정 추출 이상
   źródło: GachaTitle.json :: dataList[id=303].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Przedmioty, sklep i profil gracza [304] — tekst] 특정 추출 엄지
   źródło: GachaTitle.json :: dataList[id=304].content
   limit: do 120 znaków
   EN: Target Extraction: The Thumb
   PL: Ekstrakcja Celowana: Kciuk
586. [Przedmioty, sklep i profil gracza [305] — tekst] 신규 인격 특정 추출 오트쿠튀르::르루주 바느질의 왕 히스클리프 · 오트쿠튀르::르누아르 3F 방송실 홍루
   źródło: GachaTitle.json :: dataList[id=305].content
   limit: do 170 znaków
   EN: New Identity Target Extraction: Haute Couture::Le Rouge King of Needleworks Heathcliff & Le Noir 3F Public Address Room Hong Lu
   PL: Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Król Szycia Le Rouge Heathcliff i Haute Couture::Radiowęzeł 3F Le Noir Hong Lu
587. [Przedmioty, sklep i profil gracza [306] — tekst] 제5·6회 발푸르기스의 밤 특정 추출 BokGak
   źródło: GachaTitle.json :: dataList[id=306].content
   limit: do 120 znaków
   EN: The 5th & 6th Walpurgis Night Target Extraction BokGak
   PL: Ekstrakcja Celowana 5. i 6. Nocy Walpurgii BokGak
588. [Przedmioty, sklep i profil gracza [307] — tekst] 제10회 발푸르기스의 밤 특정 추출
   źródło: GachaTitle.json :: dataList[id=307].content
   limit: do 120 znaków
   EN: The 10th Walpurgis Night Target Extraction
   PL: Ekstrakcja Celowana 10. Nocy Walpurgii
589. [Przedmioty, sklep i profil gracza [308] — tekst] 특정 추출 로쟈
   źródło: GachaTitle.json :: dataList[id=308].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Przedmioty, sklep i profil gracza [309] — tekst] 특정 추출 중지
   źródło: GachaTitle.json :: dataList[id=309].content
   limit: do 120 znaków
   EN: Target Extraction: The Middle
   PL: Ekstrakcja Celowana: Środkowy
591. [Przedmioty, sklep i profil gracza [310] — tekst] 신규 인격 특정 추출 오트쿠튀르::르루주 B2F 타래둥지 그레고르 · 오트쿠튀르::르누아르 B3F 건조장 이상
   źródło: GachaTitle.json :: dataList[id=310].content
   limit: do 170 znaków
   EN: New Identity Target Extraction - Haute Couture::Le Rouge B2F Skein Nest Gregor & Haute Couture::Le Noir B3F Drying Room Yi Sang
   PL: Nowa Ekstrakcja Celowana Tożsamości — Haute Couture::Gniazdo Pasm B2F Le Rouge Gregor i Haute Couture::Suszarnia B3F Le Noir Yi Sang

## Przedmioty, sklep i profil gracza: IAPProduct-a1c10
- plik gry: `IAPProduct-a1c10.json`

592. [Przedmioty, sklep i profil gracza [607] — nazwa] 시즌 8 시작 광기 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=607].name
   limit: do 50 znaków
   EN: Season 8 Commencement Lunacy Pack
   PL: Pakiet Szaleństwa Startowego Sezonu 8
593. [Przedmioty, sklep i profil gracza [607] — opis] 매 시즌마다 초기화되는 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1300
   źródło: IAPProduct-a1c10.json :: dataList[id=607].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Seasonal offer that contains the following:\n\n· Paid Lunacy x1300
   PL: Oferta sezonowa — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1300
594. [Przedmioty, sklep i profil gracza [608] — nazwa] 시즌 8 정착 지원품
   źródło: IAPProduct-a1c10.json :: dataList[id=608].name
   limit: do 40 znaków
   EN: Season 8 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 8
595. [Przedmioty, sklep i profil gracza [608] — opis] 시즌 8 푼크툼 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40\n· 끈 x 80\n· 시즌 8 자아 파편 선택 상자 x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=608].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during Season 8. The pack contains the following:\n\n· Paid Lunacy x5040\n· Decaextraction Ticket x3\n· Identity Training Ticket IV x90\n· Identity Training Ticket III x40\n· Thread x80\n· Season 8 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 8: PUNCTUM — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 8 x 40
596. [Przedmioty, sklep i profil gracza [162] — nazwa] 주간 경험치 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=162].name
   limit: do 40 znaków
   EN: Weekly EXP Pack
   PL: Tygodniowy Pakiet PD
597. [Przedmioty, sklep i profil gracza [162] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c10.json :: dataList[id=162].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Identity Training Ticket IV x60\n· Identity Training Ticket III x30
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
598. [Przedmioty, sklep i profil gracza [163] — nazwa] 월간 경험치 패키지 I
   źródło: IAPProduct-a1c10.json :: dataList[id=163].name
   limit: do 40 znaków
   EN: Monthly EXP Pack I
   PL: Miesięczny Pakiet PD I
599. [Przedmioty, sklep i profil gracza [163] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 140\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=163].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x140\n· Identity Training Ticket III x40
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 140\n· Bilet Treningu Tożsamości III x 40
600. [Przedmioty, sklep i profil gracza [164] — nazwa] 월간 경험치 패키지 II
   źródło: IAPProduct-a1c10.json :: dataList[id=164].name
   limit: do 40 znaków
   EN: Monthly EXP Pack II
   PL: Miesięczny Pakiet PD II
601. [Przedmioty, sklep i profil gracza [164] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 270\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=164].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x270\n· Identity Training Ticket III x40
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 270\n· Bilet Treningu Tożsamości III x 40
602. [Przedmioty, sklep i profil gracza [165] — nazwa] 월간 경험치 패키지 III
   źródło: IAPProduct-a1c10.json :: dataList[id=165].name
   limit: do 40 znaków
   EN: Monthly EXP Pack III
   PL: Miesięczny Pakiet PD III
603. [Przedmioty, sklep i profil gracza [165] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 500\n· 인격 학습 티켓 III x 170
   źródło: IAPProduct-a1c10.json :: dataList[id=165].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x500\n· Identity Training Ticket III x170
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 500\n· Bilet Treningu Tożsamości III x 170
604. [Przedmioty, sklep i profil gracza [109] — nazwa] 월간 성장 지원 패키지 I
   źródło: IAPProduct-a1c10.json :: dataList[id=109].name
   limit: do 40 znaków
   EN: Monthly Training Pack I
   PL: Miesięczny Pakiet Wsparcia Rozwoju I
605. [Przedmioty, sklep i profil gracza [109] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1690\n· 추출 10회 티켓 x 2\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c10.json :: dataList[id=109].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x1690\n· Decaextraction Ticket x2\n· Identity Training Ticket IV x60\n· Identity Training Ticket III x30
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
606. [Przedmioty, sklep i profil gracza [504] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=504].name
   limit: do 40 znaków
   EN: Target Extraction Pack
   PL: Pakiet Ekstrakcji Celowanej
607. [Przedmioty, sklep i profil gracza [504] — opis] 「신규 인격 특정 추출 오트쿠튀르::르누아르 신발관 료슈 · 오트쿠튀르::르루주 부티크 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=504].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Boutique du Rouge Ishmael & Haute Couture::Le Noir Footwear Hall Ryōshū」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Pawilon Obuwia Le Noir Ryōshū i Haute Couture::Boutique du Rouge Ishmael” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
608. [Przedmioty, sklep i profil gracza [505] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=505].name
   limit: do 40 znaków
   EN: Identity Growth Pack
   PL: Pakiet Rozwoju Tożsamości
609. [Przedmioty, sklep i profil gracza [505] — opis] 「신규 인격 특정 추출 오트쿠튀르::르누아르 신발관 료슈 · 오트쿠튀르::르루주 부티크 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=505].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Boutique du Rouge Ishmael & Haute Couture::Le Noir Footwear Hall Ryōshū」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Pawilon Obuwia Le Noir Ryōshū i Haute Couture::Boutique du Rouge Ishmael” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
610. [Przedmioty, sklep i profil gracza [506] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=506].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Przedmioty, sklep i profil gracza [506] — opis] 「신규 인격 특정 추출 오트쿠튀르::수선실 로쟈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=506].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Alteration Shop Rodion」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Pracownia Poprawek Rodion” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
612. [Przedmioty, sklep i profil gracza [507] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=507].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Przedmioty, sklep i profil gracza [507] — opis] 「신규 인격 특정 추출 오트쿠튀르::수선실 로쟈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=507].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Alteration Shop Rodion」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Pracownia Poprawek Rodion” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
614. [Przedmioty, sklep i profil gracza [508] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=508].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Przedmioty, sklep i profil gracza [508] — opis] 「신규 인격 특정 추출 오트쿠튀르::르누아르 브랜드 매니저 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=508].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Noir Brand Manager Don Quixote」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Menedżerka Marki Le Noir Don Quixote” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
616. [Przedmioty, sklep i profil gracza [509] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=509].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Przedmioty, sklep i profil gracza [509] — opis] 「신규 인격 특정 추출 오트쿠튀르::르누아르 브랜드 매니저 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=509].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Noir Brand Manager Don Quixote」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Menedżerka Marki Le Noir Don Quixote” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
618. [Przedmioty, sklep i profil gracza [510] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=510].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Przedmioty, sklep i profil gracza [510] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 붉은 신 싱클레어」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=510].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::The Crimson God of Le Rouge Sinclair」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Czerwony Bóg Le Rouge Sinclair” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
620. [Przedmioty, sklep i profil gracza [511] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=511].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Przedmioty, sklep i profil gracza [511] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 붉은 신 싱클레어」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=511].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::The Crimson God of Le Rouge Sinclair」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Czerwony Bóg Le Rouge Sinclair” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
622. [Przedmioty, sklep i profil gracza [512] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=512].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
623. [Przedmioty, sklep i profil gracza [512] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 바느질의 왕 히스클리프 · 오트쿠튀르::르누아르 3F 방송실 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=512].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Rouge King of Needleworks Heathcliff & Le Noir 3F Public Address Room Hong Lu」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Król Szycia Le Rouge Heathcliff i Haute Couture::Radiowęzeł 3F Le Noir Hong Lu” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
624. [Przedmioty, sklep i profil gracza [513] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=513].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Przedmioty, sklep i profil gracza [513] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 바느질의 왕 히스클리프 · 오트쿠튀르::르누아르 3F 방송실 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=513].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Rouge King of Needleworks Heathcliff & Le Noir 3F Public Address Room Hong Lu」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Haute Couture::Król Szycia Le Rouge Heathcliff i Haute Couture::Radiowęzeł 3F Le Noir Hong Lu” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
626. [Przedmioty, sklep i profil gracza [514] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=514].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Przedmioty, sklep i profil gracza [514] — opis] 「제10회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=514].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 10th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 10. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
628. [Przedmioty, sklep i profil gracza [515] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=515].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Przedmioty, sklep i profil gracza [515] — opis] 「제10회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=515].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 10th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 10. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40
630. [Przedmioty, sklep i profil gracza [516] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=516].name
   limit: do 40 znaków
   EN: E.G.O Upgrade Pack
   PL: Pakiet Rozwoju E.G.O
631. [Przedmioty, sklep i profil gracza [516] — opis] 「제10회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c10.json :: dataList[id=516].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 10th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 10. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
632. [Przedmioty, sklep i profil gracza [517] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=517].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Przedmioty, sklep i profil gracza [517] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 B2F 타래둥지 그레고르 · 오트쿠튀르::르누아르 B3F 건조장 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c10.json :: dataList[id=517].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Rouge B2F Skein Nest Gregor & Haute Couture::Le Noir B3F Drying Room Yi Sang」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości — Haute Couture::Gniazdo Pasm B2F Le Rouge Gregor i Haute Couture::Suszarnia B3F Le Noir Yi Sang” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
634. [Przedmioty, sklep i profil gracza [518] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c10.json :: dataList[id=518].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Przedmioty, sklep i profil gracza [518] — opis] 「신규 인격 특정 추출 오트쿠튀르::르루주 B2F 타래둥지 그레고르 · 오트쿠튀르::르누아르 B3F 건조장 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 90\n· 인격 학습 티켓 III x 40
   źródło: IAPProduct-a1c10.json :: dataList[id=518].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Haute Couture::Le Rouge B2F Skein Nest Gregor & Haute Couture::Le Noir B3F Drying Room Yi Sang」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 90\n· Identity Training Ticket III x 40
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości — Haute Couture::Gniazdo Pasm B2F Le Rouge Gregor i Haute Couture::Suszarnia B3F Le Noir Yi Sang” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 90\n· Bilet Treningu Tożsamości III x 40

## Przedmioty, sklep i profil gracza: IAPProduct-a1c7
- plik gry: `IAPProduct-a1c7.json`

636. [Przedmioty, sklep i profil gracza [106] — nazwa] 월간 성장 지원 패키지 I
   źródło: IAPProduct-a1c7.json :: dataList[id=106].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Przedmioty, sklep i profil gracza [106] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 1690\n· 추출 10회 티켓 x 2\n· 인격 학습 티켓 IV x 30
   źródło: IAPProduct-a1c7.json :: dataList[id=106].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Lunacy x1690\n· Decaextraction Ticket x2\n· Identity Training Ticket IV x30
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Bilet Treningu Tożsamości IV x 30
638. [Przedmioty, sklep i profil gracza [601] — nazwa] 시즌 5 시작 광기 패키지
   źródło: IAPProduct-a1c7.json :: dataList[id=601].name
   limit: do 50 znaków
   EN: Season 5 Commencement Lunacy Pack
   PL: Pakiet Szaleństwa Startowego Sezonu 5
639. [Przedmioty, sklep i profil gracza [601] — opis] 매 시즌마다 초기화되는 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 1300
   źródło: IAPProduct-a1c7.json :: dataList[id=601].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Seasonal offer that contains the following:\n\n· Lunacy x1300\n\n※ Please note that all Lunacy contained in this pack is Paid Lunacy.
   PL: Oferta sezonowa — zawiera następujące składniki:\n\n· Szaleństwo x 1300\n\n※ Całe Szaleństwo z tego pakietu to Płatne Szaleństwo.
640. [Przedmioty, sklep i profil gracza [602] — nazwa] 시즌 5 정착 지원품
   źródło: IAPProduct-a1c7.json :: dataList[id=602].name
   limit: do 40 znaków
   EN: Season 5 Settler Supplies
   PL: Zestaw Startowy Sezonu 5
641. [Przedmioty, sklep i profil gracza [602] — opis] 시즌 5 오블리비언 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 학습 티켓 IV x 60\n· 끈 x 80\n· 시즌 5 자아 파편 선택 상자 x 40
   źródło: IAPProduct-a1c7.json :: dataList[id=602].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during Season 5. The pack contains the following:\n\n· Lunacy x5040\n· Decaextraction Ticket x3\n· Identity Training Ticket IV x60\n· Thread x80\n· Season 5 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 5: Oblivion — zawiera następujące składniki:\n\n· Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Treningu Tożsamości IV x 60\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 5 x 40

## Przedmioty, sklep i profil gracza: IAPProduct-a1c8
- plik gry: `IAPProduct-a1c8.json`

642. [Przedmioty, sklep i profil gracza [603] — nazwa] 시즌 6 시작 광기 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=603].name
   limit: do 50 znaków
   EN: Season 6 Commencement Lunacy Pack
   PL: Pakiet Szaleństwa Startowego Sezonu 6
643. [Przedmioty, sklep i profil gracza [603] — opis] 매 시즌마다 초기화되는 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1300
   źródło: IAPProduct-a1c8.json :: dataList[id=603].desc
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Przedmioty, sklep i profil gracza [604] — nazwa] 시즌 6 정착 지원품
   źródło: IAPProduct-a1c8.json :: dataList[id=604].name
   limit: do 40 znaków
   EN: Season 6 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 6
645. [Przedmioty, sklep i profil gracza [604] — opis] 시즌 6 장화인 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30\n· 끈 x 80\n· 시즌 6 자아 파편 선택 상자 x 40
   źródło: IAPProduct-a1c8.json :: dataList[id=604].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during Season 6. The pack contains the following:\n\n· Paid Lunacy x5040\n· Decaextraction Ticket x3\n· Identity Training Ticket IV x60\n· Identity Training Ticket III x30\n· Thread x80\n· Season 6 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 6: Zàng Huā Yín — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 6 x 40
646. [Przedmioty, sklep i profil gracza [425] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=425].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Przedmioty, sklep i profil gracza [425] — opis] 「신규 특정 추출 흑수 사 - 로쟈 · 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=425].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - Si Branch Rodion & Gregor」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wataha Heishou - Gałąź Si Rodion i Gregor” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
648. [Przedmioty, sklep i profil gracza [426] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=426].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Przedmioty, sklep i profil gracza [426] — opis] 「신규 특정 추출 흑수 사 - 로쟈 · 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=426].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - Si Branch Rodion & Gregor」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wataha Heishou - Gałąź Si Rodion i Gregor” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
650. [Przedmioty, sklep i profil gracza [154] — nazwa] 주간 경험치 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=154].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Przedmioty, sklep i profil gracza [154] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 35\n· 인격 학습 티켓 III x 25
   źródło: IAPProduct-a1c8.json :: dataList[id=154].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Identity Training Ticket IV x35\n· Identity Training Ticket III x25
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 35\n· Bilet Treningu Tożsamości III x 25
652. [Przedmioty, sklep i profil gracza [155] — nazwa] 월간 경험치 패키지 I
   źródło: IAPProduct-a1c8.json :: dataList[id=155].name
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Przedmioty, sklep i profil gracza [155] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 70
   źródło: IAPProduct-a1c8.json :: dataList[id=155].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x80\n· Identity Training Ticket III x70
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 70
654. [Przedmioty, sklep i profil gracza [156] — nazwa] 월간 경험치 패키지 II
   źródło: IAPProduct-a1c8.json :: dataList[id=156].name
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Przedmioty, sklep i profil gracza [156] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 160\n· 인격 학습 티켓 III x 95
   źródło: IAPProduct-a1c8.json :: dataList[id=156].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x160\n· Identity Training Ticket III x95
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 160\n· Bilet Treningu Tożsamości III x 95
656. [Przedmioty, sklep i profil gracza [157] — nazwa] 월간 경험치 패키지 III
   źródło: IAPProduct-a1c8.json :: dataList[id=157].name
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Przedmioty, sklep i profil gracza [157] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 325\n· 인격 학습 티켓 III x 165
   źródło: IAPProduct-a1c8.json :: dataList[id=157].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x325\n· Identity Training Ticket III x165
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 325\n· Bilet Treningu Tożsamości III x 165
658. [Przedmioty, sklep i profil gracza [107] — nazwa] 월간 성장 지원 패키지 I
   źródło: IAPProduct-a1c8.json :: dataList[id=107].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Przedmioty, sklep i profil gracza [107] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1690\n· 추출 10회 티켓 x 2\n· 인격 학습 티켓 IV x 35\n· 인격 학습 티켓 III x 25
   źródło: IAPProduct-a1c8.json :: dataList[id=107].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x1690\n· Decaextraction Ticket x2\n· Identity Training Ticket IV x35\n· Identity Training Ticket III x25
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Bilet Treningu Tożsamości IV x 35\n· Bilet Treningu Tożsamości III x 25
660. [Przedmioty, sklep i profil gracza [427] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=427].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Przedmioty, sklep i profil gracza [427] — opis] 「신규 특정 추출 흑수 - 묘 필두 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=427].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - Mao Branch Adept Faust」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź Mao Faust” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
662. [Przedmioty, sklep i profil gracza [428] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=428].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Przedmioty, sklep i profil gracza [428] — opis] 「신규 특정 추출 흑수 - 묘 필두 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=428].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - Mao Branch Adept Faust」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź Mao Faust” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
664. [Przedmioty, sklep i profil gracza [429] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=429].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
665. [Przedmioty, sklep i profil gracza [429] — opis] 「신규 특정 추출 가주 후보 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=429].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Family Hierarch Candidate Ishmael」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Kandydatka na Głowę Rodu Ishmael” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
666. [Przedmioty, sklep i profil gracza [430] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=430].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Przedmioty, sklep i profil gracza [430] — opis] 「신규 특정 추출 가주 후보 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=430].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Family Hierarch Candidate Ishmael」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Kandydatka na Głowę Rodu Ishmael” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
668. [Przedmioty, sklep i profil gracza [431] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=431].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Przedmioty, sklep i profil gracza [431] — opis] 「신규 특정 추출 동부 엄지 카포 IIII 뫼르소 · 엄지 솔다토 II 싱클레어」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=431].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Thumb East Capo IIII Meursault & Soldato II Sinclair」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Kapo IIII Kciuka ze Wschodu Meursault i Soldato II Sinclair” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
670. [Przedmioty, sklep i profil gracza [432] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=432].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Przedmioty, sklep i profil gracza [432] — opis] 「신규 특정 추출 동부 엄지 카포 IIII 뫼르소 · 엄지 솔다토 II 싱클레어」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=432].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Thumb East Capo IIII Meursault & Soldato II Sinclair」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Kapo IIII Kciuka ze Wschodu Meursault i Soldato II Sinclair” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
672. [Przedmioty, sklep i profil gracza [433] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=433].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Przedmioty, sklep i profil gracza [433] — opis] 「신규 특정 추출 N사 E.G.O::흉탄 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=433].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - N Corp. E.G.O::Fell Bullet Yi Sang」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Korp. N E.G.O::Złowroga Kula Yi Sang” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
674. [Przedmioty, sklep i profil gracza [434] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=434].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Przedmioty, sklep i profil gracza [434] — opis] 「신규 특정 추출 N사 E.G.O::흉탄 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=434].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - N Corp. E.G.O::Fell Bullet Yi Sang」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Korp. N E.G.O::Złowroga Kula Yi Sang” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
676. [Przedmioty, sklep i profil gracza [435] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=435].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Przedmioty, sklep i profil gracza [435] — opis] 「제6회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=435].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 6th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 6. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
678. [Przedmioty, sklep i profil gracza [436] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=436].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Przedmioty, sklep i profil gracza [436] — opis] 「제6회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=436].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 6th Walpurgis Night」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 6. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
680. [Przedmioty, sklep i profil gracza [437] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=437].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Przedmioty, sklep i profil gracza [437] — opis] 「제6회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [WAW] x 1
   źródło: IAPProduct-a1c8.json :: dataList[id=437].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 6th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [WAW] x 1
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 6. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1
682. [Przedmioty, sklep i profil gracza [438] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=438].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Przedmioty, sklep i profil gracza [438] — opis] 「6.5장 시간살인시간 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=438].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo IV: Timekilling Time BokGak」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo IV: Czas Zabijania Czasu BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
684. [Przedmioty, sklep i profil gracza [439] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=439].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Przedmioty, sklep i profil gracza [439] — opis] 「6.5장 시간살인시간 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=439].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo IV: Timekilling Time BokGak」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Intervallo IV: Czas Zabijania Czasu BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
686. [Przedmioty, sklep i profil gracza [440] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=440].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Przedmioty, sklep i profil gracza [440] — opis] 「6.5장 시간살인시간 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [WAW] x 1
   źródło: IAPProduct-a1c8.json :: dataList[id=440].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo IV: Timekilling Time BokGak」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [WAW] x 1
   PL: Pakiet z okazji premiery „Intervallo IV: Czas Zabijania Czasu BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1
688. [Przedmioty, sklep i profil gracza [441] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=441].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Przedmioty, sklep i profil gracza [441] — opis] 「신규 특정 추출 홍원 군주 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=441].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Lord of Hongyuan Hong Lu」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Władca Hongyuanu Hong Lu” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
690. [Przedmioty, sklep i profil gracza [442] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=442].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Przedmioty, sklep i profil gracza [442] — opis] 「신규 특정 추출 홍원 군주 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=442].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Lord of Hongyuan Hong Lu」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Władca Hongyuanu Hong Lu” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
692. [Przedmioty, sklep i profil gracza [443] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=443].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Przedmioty, sklep i profil gracza [443] — opis] 「8.5장 절차탁춘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=443].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo VI: Spring Cultivation」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo VI: Wiosenny Szlif” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
694. [Przedmioty, sklep i profil gracza [444] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=444].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Przedmioty, sklep i profil gracza [444] — opis] 「8.5장 절차탁춘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=444].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo VI: Spring Cultivation」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Intervallo VI: Wiosenny Szlif” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
696. [Przedmioty, sklep i profil gracza [445] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=445].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Przedmioty, sklep i profil gracza [445] — opis] 「신규 특정 추출 N사 E.G.O::경멸, 경외 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=445].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - N Corp. E.G.O::Contempt, Awe Ryōshū」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Korp. N E.G.O::Pogarda, Trwoga Ryōshū” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
698. [Przedmioty, sklep i profil gracza [446] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=446].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Przedmioty, sklep i profil gracza [446] — opis] 「신규 특정 추출 N사 E.G.O::경멸, 경외 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=446].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - N Corp. E.G.O::Contempt, Awe Ryōshū」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Korp. N E.G.O::Pogarda, Trwoga Ryōshū” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
700. [Przedmioty, sklep i profil gracza [447] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=447].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Przedmioty, sklep i profil gracza [447] — opis] 「8.5장 - EX 선의의 순례」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=447].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Ch. 8.5: EX - Pilgrimage of Compassion」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo VI - EX: Pielgrzymka Współczucia” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
702. [Przedmioty, sklep i profil gracza [448] — nazwa] E.G.O [WAW]\n성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=448].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O [WAW]\nUpgrade Pack
   PL: Pakiet Rozwoju\nE.G.O [WAW]
703. [Przedmioty, sklep i profil gracza [448] — opis] 「8.5장 - EX 선의의 순례」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [WAW] x 1
   źródło: IAPProduct-a1c8.json :: dataList[id=448].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Ch. 8.5: EX - Pilgrimage of Compassion」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [WAW] x 1
   PL: Pakiet z okazji premiery „Intervallo VI - EX: Pielgrzymka Współczucia” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1
704. [Przedmioty, sklep i profil gracza [449] — nazwa] E.G.O [HE]\n성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=449].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O [HE]\nUpgrade Pack
   PL: Pakiet Rozwoju\nE.G.O [HE]
705. [Przedmioty, sklep i profil gracza [449] — opis] 「8.5장 - EX 선의의 순례」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c8.json :: dataList[id=449].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Ch. 8.5: EX - Pilgrimage of Compassion」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Intervallo VI - EX: Pielgrzymka Współczucia” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
706. [Przedmioty, sklep i profil gracza [209] — nazwa] 아미야 아나운서 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=209].name
   limit: do 40 znaków
   EN: Amiya Announcer Pack
   PL: Pakiet Komentatorki Amiya
707. [Przedmioty, sklep i profil gracza [209] — opis] 림버스 컴퍼니 X 명일방주 콜라보레이션 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 아미야 아나운서\n· 추출 10회 티켓 x 2
   źródło: IAPProduct-a1c8.json :: dataList[id=209].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this Limbus Company X Arknights Collaboration release commemorative Pack.\n\n· Amiya Announcer\n· Decaextraction Ticket x2
   PL: Pakiet z okazji kolaboracji Limbus Company X Arknights — zawiera następujące składniki:\n\n· Komentatorka Amiya\n· Bilet Dekaekstrakcji x 2
708. [Przedmioty, sklep i profil gracza [206] — nazwa] Full Moon 2025\n기념 인격 성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=206].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2025\nCommemorative\nID Upgrade Pack
   PL: Pakiet Rozwoju Tożsamości\nFull Moon 2025
709. [Przedmioty, sklep i profil gracza [206] — opis] Full Moon 2025 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 140\n\n※ 도약 모듈 - 인격 동기화 사용 시, 선택한 인격의 동기화 단계가 4단계까지 증가합니다.
   źródło: IAPProduct-a1c8.json :: dataList[id=206].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2025 Campaign Commemorative Pack. Contains the following items:\n\n· Takeoff Module - ID Uptie x1\n· Identity Training Ticket IV x140\n\n※ Using the Takeoff Module - ID Uptie raises the selected Identity's Uptie Tier to 4.
   PL: Pakiet limitowany z okazji kampanii Full Moon 2025 — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 140\n\n※ Moduł Skoku — Synchronizacja Tożsamości podnosi Stopień Synchronizacji wybranej Tożsamości do 4.
710. [Przedmioty, sklep i profil gracza [207] — nazwa] Full Moon 2025\n기념 E.G.O 성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=207].name
   limit: do 70 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2025\nCommemorative\nE.G.O Upgrade Pack
   PL: Pakiet Rozwoju E.G.O\nFull Moon 2025
711. [Przedmioty, sklep i profil gracza [207] — opis] Full Moon 2025 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 3\n· 도약 모듈 - E.G.O 해석 [WAW] x 1\n\n※ 도약 모듈 - E.G.O 해석 [WAW] 사용 시, 선택한 E.G.O의 환상 해석 단계가 4단계까지 증가합니다. (최대 WAW 등급까지 적용 가능)
   źródło: IAPProduct-a1c8.json :: dataList[id=207].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2025 Campaign Commemorative Pack. Contains the following items:\n\n· Decaextraction Ticket x3\n· Takeoff Module - E.G.O Spinning [WAW] x1\n\n※ Using the Takeoff Module - E.G.O Spinning [WAW] raises the selected E.G.O's Threadspinning tier to 4. (Usable only on E.G.Os WAW Level or lower)
   PL: Pakiet limitowany z okazji kampanii Full Moon 2025 — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 3\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1\n\n※ Moduł Skoku — Splot Nici E.G.O [WAW] podnosi Stopień Splotu Nici wybranego E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi WAW lub niższej)
712. [Przedmioty, sklep i profil gracza [208] — nazwa] Full Moon 2025\n기념 종합 성장 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=208].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Full Moon 2025\nCommemorative\nComplete Pack
   PL: Pakiet Kompleksowy\nFull Moon 2025
713. [Przedmioty, sklep i profil gracza [208] — opis] Full Moon 2025 캠페인 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4\n· 도약 모듈 - 인격 동기화 x 1\n· 도약 모듈 - E.G.O 해석 [WAW] x 1\n· 인격 학습 티켓 IV x 140\n· 끈 x 100\n\n※ 도약 모듈 - 인격 동기화 사용 시, 선택한 인격의 동기화 단계가 4단계까지 증가합니다.\n\n※ 도약 모듈 - E.G.O 해석 [WAW] 사용 시, 선택한 E.G.O의 환상 해석 단계가 4단계까지 증가합니다. (최대 WAW 등급까지 적용 가능)
   źródło: IAPProduct-a1c8.json :: dataList[id=208].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited Full Moon 2025 Campaign Commemorative Pack. Contains the following items:\n\n· Decaextraction Ticket x4\n· Takeoff Module - ID Uptie x1\n· Takeoff Module - E.G.O Spinning [WAW] x1\n· Identity Training Ticket IV x140\n· Threads x100\n\n※ Using the Takeoff Module - ID Uptie raises the selected Identity's Uptie Tier to 4.\n\n※ Using the Takeoff Module - E.G.O Spinning [WAW] raises the selected E.G.O's Threadspinning tier to 4. (Usable only on E.G.Os WAW Level or lower)
   PL: Pakiet limitowany z okazji kampanii Full Moon 2025 — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Moduł Skoku — Splot Nici E.G.O [WAW] x 1\n· Bilet Treningu Tożsamości IV x 140\n· Nić x 100\n\n※ Moduł Skoku — Synchronizacja Tożsamości podnosi Stopień Synchronizacji wybranej Tożsamości do 4.\n\n※ Moduł Skoku — Splot Nici E.G.O [WAW] podnosi Stopień Splotu Nici wybranego E.G.O do 4. (Można stosować wyłącznie do E.G.O rangi WAW lub niższej)
714. [Przedmioty, sklep i profil gracza [450] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=450].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Przedmioty, sklep i profil gracza [450] — opis] 「신규 특정 추출 동부 시 협회 3과 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=450].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Shi East Section 3 Faust」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Sekcja 3 Wschodniego Stowarzyszenia Shi Faust” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
716. [Przedmioty, sklep i profil gracza [451] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=451].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Przedmioty, sklep i profil gracza [451] — opis] 「6.5장 워프특급 살인사건 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=451].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo IV: Murder on the WARP Express BokGak」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo IV: Morderstwo w Ekspresie WARP BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
718. [Przedmioty, sklep i profil gracza [452] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=452].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Przedmioty, sklep i profil gracza [452] — opis] 「6.5장 워프특급 살인사건 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=452].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo IV: Murder on the WARP Express BokGak」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Intervallo IV: Morderstwo w Ekspresie WARP BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
720. [Przedmioty, sklep i profil gracza [453] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=453].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Przedmioty, sklep i profil gracza [453] — opis] 「제7회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=453].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 7th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 7. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
722. [Przedmioty, sklep i profil gracza [454] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=454].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Przedmioty, sklep i profil gracza [454] — opis] 「제7회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=454].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 7th Walpurgis Night」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 7. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
724. [Przedmioty, sklep i profil gracza [455] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=455].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Przedmioty, sklep i profil gracza [455] — opis] 「신규 특정 추출 흑수 - 유 필두 히스클리프 · 흑수 - 미 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=455].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - You Branch Adept Heathcliff & Wei Branch Don Quixote」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź You Heathcliff i Wataha Heishou - Gałąź Wei Don Quixote” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
726. [Przedmioty, sklep i profil gracza [456] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=456].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Przedmioty, sklep i profil gracza [456] — opis] 「신규 특정 추출 흑수 - 유 필두 히스클리프 · 흑수 - 미 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=456].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - Heishou Pack - You Branch Adept Heathcliff & Wei Branch Don Quixote」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Adept Watahy Heishou - Gałąź You Heathcliff i Wataha Heishou - Gałąź Wei Don Quixote” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
728. [Przedmioty, sklep i profil gracza [457] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=457].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Przedmioty, sklep i profil gracza [457] — opis] 「신규 특정 추출 홍원 방랑무사 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c8.json :: dataList[id=457].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Drifting Blade of Hongyuan Ryōshū」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wędrowna Szermierka z Hongyuanu Ryōshū” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
730. [Przedmioty, sklep i profil gracza [458] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=458].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Przedmioty, sklep i profil gracza [458] — opis] 「신규 특정 추출 홍원 방랑무사 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=458].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Drifting Blade of Hongyuan Ryōshū」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wędrowna Szermierka z Hongyuanu Ryōshū” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30
732. [Przedmioty, sklep i profil gracza [459] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c8.json :: dataList[id=459].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Przedmioty, sklep i profil gracza [459] — opis] 「신규 특정 추출 R사 제 4무리 순록팀 로쟈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 60\n· 인격 학습 티켓 III x 30
   źródło: IAPProduct-a1c8.json :: dataList[id=459].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - R Corp. 4th Pack Reindeer Rodion」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 60\n· Identity Training Ticket III x 30
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Zespół Reniferów 4. Stada R Corp. Rodion” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 60\n· Bilet Treningu Tożsamości III x 30

## Przedmioty, sklep i profil gracza: IAPProduct-a1c9
- plik gry: `IAPProduct-a1c9.json`

734. [Przedmioty, sklep i profil gracza [605] — nazwa] 시즌 7 시작 광기 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=605].name
   limit: do 50 znaków
   EN: Season 7 Commencement Lunacy Pack
   PL: Pakiet Szaleństwa Startowego Sezonu 7
735. [Przedmioty, sklep i profil gracza [605] — opis] 매 시즌마다 초기화되는 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1300
   źródło: IAPProduct-a1c9.json :: dataList[id=605].desc
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Przedmioty, sklep i profil gracza [606] — nazwa] 시즌 7 정착 지원품
   źródło: IAPProduct-a1c9.json :: dataList[id=606].name
   limit: do 40 znaków
   EN: Season 7 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 7
737. [Przedmioty, sklep i profil gracza [606] — opis] 시즌 7 쿠모노 이토 · 아카노 이토 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20\n· 끈 x 80\n· 시즌 7 자아 파편 선택 상자 x 40
   źródło: IAPProduct-a1c9.json :: dataList[id=606].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during Season 7. The pack contains the following:\n\n· Paid Lunacy x5040\n· Decaextraction Ticket x3\n· Identity Training Ticket IV x80\n· Identity Training Ticket III x20\n· Thread x80\n· Season 7 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 7: Kumo no Ito · otI on akA — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 7 x 40
738. [Przedmioty, sklep i profil gracza [158] — nazwa] 주간 경험치 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=158].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Przedmioty, sklep i profil gracza [158] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=158].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Identity Training Ticket IV x50\n· Identity Training Ticket III x20
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
740. [Przedmioty, sklep i profil gracza [159] — nazwa] 월간 경험치 패키지 I
   źródło: IAPProduct-a1c9.json :: dataList[id=159].name
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Przedmioty, sklep i profil gracza [159] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 100\n· 인격 학습 티켓 III x 80
   źródło: IAPProduct-a1c9.json :: dataList[id=159].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x100\n· Identity Training Ticket III x80
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 100\n· Bilet Treningu Tożsamości III x 80
742. [Przedmioty, sklep i profil gracza [160] — nazwa] 월간 경험치 패키지 II
   źródło: IAPProduct-a1c9.json :: dataList[id=160].name
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Przedmioty, sklep i profil gracza [160] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 210\n· 인격 학습 티켓 III x 72
   źródło: IAPProduct-a1c9.json :: dataList[id=160].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x210\n· Identity Training Ticket III x72
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 210\n· Bilet Treningu Tożsamości III x 72
744. [Przedmioty, sklep i profil gracza [161] — nazwa] 월간 경험치 패키지 III
   źródło: IAPProduct-a1c9.json :: dataList[id=161].name
   (powtórzenie elementu 602 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Przedmioty, sklep i profil gracza [161] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 학습 티켓 IV x 400\n· 인격 학습 티켓 III x 192
   źródło: IAPProduct-a1c9.json :: dataList[id=161].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Identity Training Ticket IV x400\n· Identity Training Ticket III x192
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Treningu Tożsamości IV x 400\n· Bilet Treningu Tożsamości III x 192
746. [Przedmioty, sklep i profil gracza [108] — nazwa] 월간 성장 지원 패키지 I
   źródło: IAPProduct-a1c9.json :: dataList[id=108].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Przedmioty, sklep i profil gracza [108] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1690\n· 추출 10회 티켓 x 2\n· 인격 학습 티켓 IV x 50\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=108].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x1690\n· Decaextraction Ticket x2\n· Identity Training Ticket IV x50\n· Identity Training Ticket III x20
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Bilet Treningu Tożsamości IV x 50\n· Bilet Treningu Tożsamości III x 20
748. [Przedmioty, sklep i profil gracza [460] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=460].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
749. [Przedmioty, sklep i profil gracza [460] — opis] 「신규 특정 추출 검지 수행자:【쪽지】 파우스트 · LCA 우제트 선봉 3팀 팀장 오티스」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=460].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Index Proselyte:【Paper Slip】 Faust & LCA Udjat Vanguard Team 3 Leader Outis」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Akolitka Wskazującego:【Karteczka】 Faust i Dowódczyni 3. Zespołu Szpicy Udjat LCA Outis” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
750. [Przedmioty, sklep i profil gracza [461] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=461].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Przedmioty, sklep i profil gracza [461] — opis] 「신규 특정 추출 검지 수행자:【쪽지】 파우스트 · LCA 우제트 선봉 3팀 팀장 오티스」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=461].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Index Proselyte:【Paper Slip】 Faust & LCA Udjat Vanguard Team 3 Leader Outis」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Akolitka Wskazującego:【Karteczka】 Faust i Dowódczyni 3. Zespołu Szpicy Udjat LCA Outis” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
752. [Przedmioty, sklep i profil gracza [462] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=462].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Przedmioty, sklep i profil gracza [462] — opis] 「신규 특정 추출 검지 @#$#:【단말기】 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=462].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Index @#$#: 【Device】 Don Quixote」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wskazujący @#$#:【Urządzenie】 Don Quixote” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
754. [Przedmioty, sklep i profil gracza [463] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=463].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Przedmioty, sklep i profil gracza [463] — opis] 「신규 특정 추출 검지 @#$#:【단말기】 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=463].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The Index @#$#: 【Device】 Don Quixote」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Wskazujący @#$#:【Urządzenie】 Don Quixote” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
756. [Przedmioty, sklep i profil gracza [464] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=464].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Przedmioty, sklep i profil gracza [464] — opis] 「신규 특정 추출 거미집 중지 제자 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=464].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Middle Apprentice Ishmael」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Środkowego Ishmael” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
758. [Przedmioty, sklep i profil gracza [465] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=465].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Przedmioty, sklep i profil gracza [465] — opis] 「신규 특정 추출 거미집 중지 제자 이스마엘」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=465].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Middle Apprentice Ishmael」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Środkowego Ishmael” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
760. [Przedmioty, sklep i profil gracza [466] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=466].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Przedmioty, sklep i profil gracza [466] — opis] 「신규 특정 추출 거미집 소지 제자 싱클레어 · 로보토미 E.G.O::램프 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=466].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Pinky Apprentice Sinclair & Lobotomy E.G.O::Lamp Gregor」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Małego Palca Sinclair i Lobotomy E.G.O::Lampa Gregor” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
762. [Przedmioty, sklep i profil gracza [467] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=467].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Przedmioty, sklep i profil gracza [467] — opis] 「신규 특정 추출 거미집 소지 제자 싱클레어 · 로보토미 E.G.O::램프 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=467].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Pinky Apprentice Sinclair & Lobotomy E.G.O::Lamp Gregor」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Uczeń Małego Palca Sinclair i Lobotomy E.G.O::Lampa Gregor” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
764. [Przedmioty, sklep i profil gracza [468] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=468].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
765. [Przedmioty, sklep i profil gracza [468] — opis] 「신규 특정 추출 거미집 검지 아비 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=468].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Index Nursefather Yi Sang」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Wskazującego Yi Sang” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
766. [Przedmioty, sklep i profil gracza [469] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=469].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Przedmioty, sklep i profil gracza [469] — opis] 「신규 특정 추출 거미집 검지 아비 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=469].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction - The House of Spiders: The Index Nursefather Yi Sang」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Wskazującego Yi Sang” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
768. [Przedmioty, sklep i profil gracza [210] — nazwa] 3주년 기념 패키지 I
   źródło: IAPProduct-a1c9.json :: dataList[id=210].name
   limit: do 40 znaków
   EN: 3rd Anniversary Pack I
   PL: Pakiet 3. Rocznicy I
769. [Przedmioty, sklep i profil gracza [210] — opis] 3주년 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 앤젤라 (도서관 관장 - 초기) 아나운서 즉시 이용 가능\n· 3성 인격 출현 추출 티켓 x1\n· 인격 성장 도약 티켓 - ver.3 x1\n\n※ 앤젤라 (도서관 관장 - 초기) 아나운서를 이미 보유한 경우, 끈 상자 x50을 획득합니다.\n※ 인격 성장 도약 티켓 - ver.3 사용 시, 선택한 인격의 레벨이 60, 동기화 단계가 4단계까지 증가합니다.
   źródło: IAPProduct-a1c9.json :: dataList[id=210].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 3rd Anniversary Pack. Contains the following items:\n\n· Immediate access to Angela (Library Director - Early Days) Announcer\n· 3★ Guarantee Decaextraction Ticket x1\n· Identity Takeoff Ticket - ver.3 x1\n\n※ If you have already obtained the Angela (Library Director - Early Days) Announcer, acquire x50 Thread Crates instead.\n※ Identity Takeoff Ticket - ver.3 raises an Identity’s level up to 60, and Uptie Tier up to Tier 4.
   PL: Pakiet limitowany na 3. Rocznicy — zawiera następujące składniki:\n\n· Natychmiastowy dostęp do Komentatorki Angela (Dyrektorka Biblioteki — Pierwsze Dni)\n· Bilet Dekstrakcji Gwarantowanej 3★ x 1\n· Bilet Skoku Rozwoju Tożsamości - ver.3 x 1\n\n※ Jeśli już posiadasz Komentatorkę Angela (Dyrektorka Biblioteki — Pierwsze Dni), otrzymasz zamiast niej 50 Skrzynek Nici.\n※ Bilet Skoku Rozwoju Tożsamości - ver.3 podnosi poziom wybranej Tożsamości do 60, a Stopień Synchronizacji do 4.
770. [Przedmioty, sklep i profil gracza [211] — nazwa] 3주년 기념 패키지 II
   źródło: IAPProduct-a1c9.json :: dataList[id=211].name
   limit: do 40 znaków
   EN: 3rd Anniversary Pack II
   PL: Pakiet 3. Rocznicy II
771. [Przedmioty, sklep i profil gracza [211] — opis] 3주년 기념 한정 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 3주년 기념 인격 선택권 x1\n\n※ 3주년 기념 인격 선택권 사용 시, 시즌 7 시작 이전에 출시된 인격 (상시 인격과 이벤트를 포함한 시즌 1 ~ 시즌 6 인격) 중 하나를 선택하여 얻을 수 있습니다.\n※ 발푸르기스의 밤 인격과 시즌 7 시작 이후에 출시된 인격은 해당 선택권에 등장하지 않습니다.
   źródło: IAPProduct-a1c9.json :: dataList[id=211].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 3rd Anniversary Pack. Contains the following item:\n\n· 3rd Anniversary Nominable Identity Ticket x1\n\n※ Use this item to select a Season 1~6 Identity released prior to Season 7 (including Standard Fare and Event Identities) to obtain.\n※ Post-Season 7 commencement and Walpurgis Night Identities are not featured in this ticket.
   PL: Pakiet limitowany na 3. Rocznicy — zawiera następujący składnik:\n\n· Kupon wyboru Tożsamości 3. rocznicy x 1\n\n※ Kupon wyboru Tożsamości 3. rocznicy pozwala wybrać jedną Tożsamość wydaną przed startem Sezonu 7 (Tożsamości Standardowe oraz Eventowe z Sezonów 1–6).\n※ Tożsamości z Nocy Walpurgii oraz wydane po starcie Sezonu 7 nie pojawiają się w tym kuponie.
772. [Przedmioty, sklep i profil gracza [470] — nazwa] 3주년 기념 추출 티켓 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=470].name
   limit: do 60 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 3rd Anniversary\nExtraction Ticket Pack
   PL: Pakiet Biletów Ekstrakcji\n3. Rocznicy
773. [Przedmioty, sklep i profil gracza [470] — opis] 3주년 기념 한정 상품으로, 추출과 관련된 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 5
   źródło: IAPProduct-a1c9.json :: dataList[id=470].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 3rd Anniversary Pack. Contains the following items:\n\n· Decaextraction Ticket x5
   PL: Pakiet limitowany na 3. Rocznicy — zawiera następujące składniki związane z Ekstrakcją:\n\n· Bilet Dekaekstrakcji x 5
774. [Przedmioty, sklep i profil gracza [471] — nazwa] 3주년 기념 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=471].name
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 3rd Anniversary\nIdentity Growth Pack
   PL: Pakiet Rozwoju Tożsamości\n3. Rocznicy
775. [Przedmioty, sklep i profil gracza [471] — opis] 3주년 기념 한정 상품으로, 인격 육성과 관련된 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 2\n· 인격 학습 티켓 IV x 200
   źródło: IAPProduct-a1c9.json :: dataList[id=471].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A limited 3rd Anniversary Pack. Contains the following items:\n\n· Takeoff Module - ID Uptie x2\n· Identity Training Ticket IV x200
   PL: Pakiet limitowany na 3. Rocznicy — zawiera składniki związane z rozwojem Tożsamości:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 2\n· Bilet Treningu Tożsamości IV x 200
776. [Przedmioty, sklep i profil gracza [472] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=472].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Przedmioty, sklep i profil gracza [472] — opis] 「제8회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=472].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 8th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 8. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
778. [Przedmioty, sklep i profil gracza [473] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=473].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Przedmioty, sklep i profil gracza [473] — opis] 「제8회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=473].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 8th Walpurgis Night」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 8. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
780. [Przedmioty, sklep i profil gracza [474] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=474].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Przedmioty, sklep i profil gracza [474] — opis] 「제8회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=474].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 8th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 8. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
782. [Przedmioty, sklep i profil gracza [475] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=475].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Przedmioty, sklep i profil gracza [475] — opis] 「7.5장 LCB 정기검진 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=475].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo V: LCB Regular Check-up BokGak」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Intervallo V: Okresowe Badania LCB BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
784. [Przedmioty, sklep i profil gracza [476] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=476].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Przedmioty, sklep i profil gracza [476] — opis] 「7.5장 LCB 정기검진 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=476].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo V: LCB Regular Check-up BokGak」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Intervallo V: Okresowe Badania LCB BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
786. [Przedmioty, sklep i profil gracza [477] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=477].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Przedmioty, sklep i profil gracza [477] — opis] 「7.5장 LCB 정기검진 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=477].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「Intervallo V: LCB Regular Check-up BokGak」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Intervallo V: Okresowe Badania LCB BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
788. [Przedmioty, sklep i profil gracza [478] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=478].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Przedmioty, sklep i profil gracza [478] — opis] 「신규 특정 추출 거미집 약지 아비 홍루 · 약지 제자 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=478].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction: The House of Spiders: The Ring Nursefather Hong Lu & Apprentice Faust」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Serdecznego Hong Lu i Uczennica Serdecznego Faust” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
790. [Przedmioty, sklep i profil gracza [479] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=479].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Przedmioty, sklep i profil gracza [479] — opis] 「신규 특정 추출 거미집 약지 아비 홍루 · 약지 제자 파우스트」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=479].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Target Extraction: The House of Spiders: The Ring Nursefather Hong Lu & Apprentice Faust」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Dom Pajęczyn — Ojciec Serdecznego Hong Lu i Uczennica Serdecznego Faust” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
792. [Przedmioty, sklep i profil gracza [480] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=480].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Przedmioty, sklep i profil gracza [480] — opis] 「신규 인격 특정 추출 타래 엮기」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=480].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Twining Threads」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Splatanie Pasm” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
794. [Przedmioty, sklep i profil gracza [481] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=481].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Przedmioty, sklep i profil gracza [481] — opis] 「신규 인격 특정 추출 타래 엮기」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=481].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Twining Threads」 release commemorative pack.\n\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Splatanie Pasm” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
796. [Przedmioty, sklep i profil gracza [482] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=482].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Przedmioty, sklep i profil gracza [482] — opis] 「신규 인격 · E.G.O 특정 추출 심야청소 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=482].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Nocturnal Sweeping BokGak」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Nocne Sprzątanie BokGak” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
798. [Przedmioty, sklep i profil gracza [483] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=483].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Przedmioty, sklep i profil gracza [483] — opis] 「신규 인격 · E.G.O 특정 추출 심야청소 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=483].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Nocturnal Sweeping BokGak」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Nocne Sprzątanie BokGak” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
800. [Przedmioty, sklep i profil gracza [484] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=484].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [Przedmioty, sklep i profil gracza [484] — opis] 「신규 인격 · E.G.O 특정 추출 심야청소 BokGak」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [ZAYIN] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=484].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Nocturnal Sweeping BokGak」 release commemorative pack.\n· Takeoff Module - E.G.O Spinning [ZAYIN] x 1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Nocne Sprzątanie BokGak” — zawiera następujące składniki:\n· Moduł Skoku — Splot Nici E.G.O [ZAYIN] x 1
802. [Przedmioty, sklep i profil gracza [485] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=485].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Przedmioty, sklep i profil gracza [485] — opis] 「신규 인격 특정 추출 거미집의 검 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=485].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Blade of the House of Spiders Ryōshū」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Ostrze Domu Pajęczyn Ryōshū” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
804. [Przedmioty, sklep i profil gracza [486] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=486].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Przedmioty, sklep i profil gracza [486] — opis] 「신규 인격 특정 추출 거미집의 검 료슈」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=486].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Blade of the House of Spiders Ryōshū」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Ostrze Domu Pajęczyn Ryōshū” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
806. [Przedmioty, sklep i profil gracza [487] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=487].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Przedmioty, sklep i profil gracza [487] — opis] 「신규 인격 특정 추출 거미집 중지 아비 오티스」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=487].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - The House of Spiders: The Middle Nursefather Outis」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Środkowego Outis” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
808. [Przedmioty, sklep i profil gracza [488] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=488].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Przedmioty, sklep i profil gracza [488] — opis] 「신규 인격 특정 추출 거미집 중지 아비 오티스」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=488].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - The House of Spiders: The Middle Nursefather Outis」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Środkowego Outis” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
810. [Przedmioty, sklep i profil gracza [489] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=489].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Przedmioty, sklep i profil gracza [489] — opis] 「신규 인격 · E.G.O 특정 추출 경험기억」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=489].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Mnestic Experience」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Pamięć Doświadczenia” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
812. [Przedmioty, sklep i profil gracza [490] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=490].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Przedmioty, sklep i profil gracza [490] — opis] 「신규 인격 · E.G.O 특정 추출 경험기억」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=490].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Mnestic Experience」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Pamięć Doświadczenia” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
814. [Przedmioty, sklep i profil gracza [491] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=491].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Przedmioty, sklep i profil gracza [491] — opis] 「신규 인격 · E.G.O 특정 추출 경험기억」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=491].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity & E.G.O Target Extraction - Mnestic Experience」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana: Tożsamość i E.G.O — Pamięć Doświadczenia” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
816. [Przedmioty, sklep i profil gracza [492] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=492].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Przedmioty, sklep i profil gracza [492] — opis] 「신규 인격 특정 추출 거미집 엄지 아비 로쟈 · 엄지 제자 히스클리프」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=492].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction: The House of Spiders: The Thumb Nursefather Rodion & Apprentice Heathcliff」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Kciuka Rodion i Uczeń Kciuka Heathcliff” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
818. [Przedmioty, sklep i profil gracza [493] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=493].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Przedmioty, sklep i profil gracza [493] — opis] 「신규 인격 특정 추출 거미집 엄지 아비 로쟈 · 엄지 제자 히스클리프」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=493].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction: The House of Spiders: The Thumb Nursefather Rodion & Apprentice Heathcliff」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Dom Pajęczyn — Ojciec Kciuka Rodion i Uczeń Kciuka Heathcliff” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
820. [Przedmioty, sklep i profil gracza [494] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=494].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
821. [Przedmioty, sklep i profil gracza [494] — opis] 「제9회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=494].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 9th Walpurgis Night」 release commemorative pack.\n\n· Decaextraction Ticket x 4
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 9. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
822. [Przedmioty, sklep i profil gracza [495] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=495].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [Przedmioty, sklep i profil gracza [495] — opis] 「제9회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=495].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this「The 9th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 9. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
824. [Przedmioty, sklep i profil gracza [496] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=496].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Przedmioty, sklep i profil gracza [496] — opis] 「제9회 발푸르기스의 밤 특정 추출」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n·  도약 모듈 - E.G.O 해석 [HE] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=496].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「The 9th Walpurgis Night」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [HE] x 1
   PL: Pakiet z okazji premiery „Ekstrakcja Celowana 9. Nocy Walpurgii” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [HE] x 1
826. [Przedmioty, sklep i profil gracza [497] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=497].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Przedmioty, sklep i profil gracza [497] — opis] 「신규 인격 특정 추출 LCE E.G.O::차원찢개 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=497].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - LCE E.G.O::Dimension Shredder Yi Sang」 release commemorative Pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: LCE E.G.O::Rozpruwacz Wymiarów Yi Sang” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
828. [Przedmioty, sklep i profil gracza [498] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=498].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Przedmioty, sklep i profil gracza [498] — opis] 「신규 인격 특정 추출 LCE E.G.O::차원찢개 이상」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=498].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - LCE E.G.O::Dimension Shredder Yi Sang」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: LCE E.G.O::Rozpruwacz Wymiarów Yi Sang” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
830. [Przedmioty, sklep i profil gracza [499] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=499].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Przedmioty, sklep i profil gracza [499] — opis] 「신규 E.G.O 특정 추출 난 가위를 낼게, 너는? 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=499].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - I'll Go fer Scissors, How 'Bout You? Don Quixote」 release commemorative pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Idę po Nożyce, a Ty? Don Quixote” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
832. [Przedmioty, sklep i profil gracza [500] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=500].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Przedmioty, sklep i profil gracza [500] — opis] 「신규 E.G.O 특정 추출 난 가위를 낼게, 너는? 돈키호테」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [ZAYIN] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=500].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - I'll Go fer Scissors, How 'Bout You? Don Quixote」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [ZAYIN] x1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Idę po Nożyce, a Ty? Don Quixote” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [ZAYIN] x 1
834. [Przedmioty, sklep i profil gracza [501] — nazwa] 인격 육성 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=501].name
   (powtórzenie elementu 608 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Przedmioty, sklep i profil gracza [501] — opis] 「신규 인격 특정 추출 동부 섕크 협회 3과 홍루」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - 인격 동기화 x 1\n· 인격 학습 티켓 IV x 80\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct-a1c9.json :: dataList[id=501].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「New Identity Target Extraction - Cinq East Section 3 Hong Lu」 release commemorative Pack.\n\n· Takeoff Module - ID Uptie x 1\n· Identity Training Ticket IV x 80\n· Identity Training Ticket III x 20
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana Tożsamości: Sekcja 3 Wschodniego Stowarzyszenia Cinq Hong Lu” — zawiera następujące składniki:\n\n· Moduł Skoku — Synchronizacja Tożsamości x 1\n· Bilet Treningu Tożsamości IV x 80\n· Bilet Treningu Tożsamości III x 20
836. [Przedmioty, sklep i profil gracza [502] — nazwa] 특별 추출 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=502].name
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Przedmioty, sklep i profil gracza [502] — opis] 「신규 E.G.O 특정 추출 입주 신고 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 추출 10회 티켓 x 4
   źródło: IAPProduct-a1c9.json :: dataList[id=502].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - Move-in Reg. Gregor」 release commemorative pack.\n\n· Decaextraction Ticket x4
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Zgłoszenie Zameldowania dla Gregora” — zawiera następujące składniki:\n\n· Bilet Dekaekstrakcji x 4
838. [Przedmioty, sklep i profil gracza [503] — nazwa] E.G.O 성장 패키지
   źródło: IAPProduct-a1c9.json :: dataList[id=503].name
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Przedmioty, sklep i profil gracza [503] — opis] 「신규 E.G.O 특정 추출 입주 신고 그레고르」 출시 기념 상품으로, 다음 구성품을 획득할 수 있습니다.\n\n· 도약 모듈 - E.G.O 해석 [TETH] x 1
   źródło: IAPProduct-a1c9.json :: dataList[id=503].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can obtain the following items from this 「E.G.O Target Extraction - Move-in Reg. Gregor」 release commemorative pack.\n\n· Takeoff Module - E.G.O Spinning [TETH] x1
   PL: Pakiet z okazji premiery „Nowa Ekstrakcja Celowana E.G.O: Zgłoszenie Zameldowania dla Gregora” — zawiera następujące składniki:\n\n· Moduł Skoku — Splot Nici E.G.O [TETH] x 1

## Przedmioty, sklep i profil gracza: IAPProduct
- plik gry: `IAPProduct.json`

840. [Przedmioty, sklep i profil gracza [1] — nazwa] 광기
   źródło: IAPProduct.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Lunacy
   PL: Szaleństwo
841. [Przedmioty, sklep i profil gracza [1] — opis] 유료 광기를 140만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=1].desc
   limit: do 120 znaków
   EN: Contains 140 Paid Lunacy.
   PL: Otrzymasz 140 Płatnego Szaleństwa.
842. [Przedmioty, sklep i profil gracza [2] — nazwa] 광기 묶음
   źródło: IAPProduct.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Lunacy Bundle
   PL: Pęk Szaleństwa
843. [Przedmioty, sklep i profil gracza [2] — opis] 유료 광기를 588만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=2].desc
   limit: do 120 znaków
   EN: Contains 588 Paid Lunacy.
   PL: Otrzymasz 588 Płatnego Szaleństwa.
844. [Przedmioty, sklep i profil gracza [3] — nazwa] 광기 다발
   źródło: IAPProduct.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Lunacy Bouquet
   PL: Bukiet Szaleństwa
845. [Przedmioty, sklep i profil gracza [3] — opis] 유료 광기를 2028만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=3].desc
   limit: do 120 znaków
   EN: Contains 2028 Paid Lunacy.
   PL: Otrzymasz 2028 Płatnego Szaleństwa.
846. [Przedmioty, sklep i profil gracza [4] — nazwa] 광기 상자
   źródło: IAPProduct.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Lunacy Crate
   PL: Skrzynia Szaleństwa
847. [Przedmioty, sklep i profil gracza [4] — opis] 유료 광기를 4294만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=4].desc
   limit: do 120 znaków
   EN: Contains 4294 Paid Lunacy.
   PL: Otrzymasz 4294 Płatnego Szaleństwa.
848. [Przedmioty, sklep i profil gracza [5] — nazwa] 광기 더미
   źródło: IAPProduct.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Lunacy Mound
   PL: Kopiec Szaleństwa
849. [Przedmioty, sklep i profil gracza [5] — opis] 유료 광기를 8206만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=5].desc
   limit: do 120 znaków
   EN: Contains 8206 Paid Lunacy.
   PL: Otrzymasz 8206 Płatnego Szaleństwa.
850. [Przedmioty, sklep i profil gracza [6] — nazwa] 광기 모음
   źródło: IAPProduct.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Lunacy Hoard
   PL: Zbiór Szaleństwa
851. [Przedmioty, sklep i profil gracza [6] — opis] 유료 광기를 16672만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=6].desc
   limit: do 120 znaków
   EN: Contains 16672 Paid Lunacy.
   PL: Otrzymasz 16672 Płatnego Szaleństwa.
852. [Przedmioty, sklep i profil gracza [11] — nazwa] 광기
   źródło: IAPProduct.json :: dataList[id=11].name
   (powtórzenie elementu 840 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Przedmioty, sklep i profil gracza [11] — opis] 유료 광기를 70만큼 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=11].desc
   limit: do 120 znaków
   EN: Contains 70 Paid Lunacy.
   PL: Otrzymasz 70 Płatnego Szaleństwa.
854. [Przedmioty, sklep i profil gracza [12] — nazwa] 광기 묶음
   źródło: IAPProduct.json :: dataList[id=12].name
   (powtórzenie elementu 842 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Przedmioty, sklep i profil gracza [12] — opis] 유료 광기를 294만큼 획득할 수 있습니다.\n보너스로 무료 광기가 31만큼 추가로 제공됩니다.
   źródło: IAPProduct.json :: dataList[id=12].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains 294 Paid Lunacy.\nYou will also receive 31 Free Lunacy as a bonus.
   PL: Otrzymasz 294 Płatnego Szaleństwa.\nBonusowo dostaniesz dodatkowo 31 darmowego Szaleństwa.
856. [Przedmioty, sklep i profil gracza [13] — nazwa] 광기 다발
   źródło: IAPProduct.json :: dataList[id=13].name
   (powtórzenie elementu 844 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Przedmioty, sklep i profil gracza [13] — opis] 유료 광기를 1014만큼 획득할 수 있습니다.\n보너스로 무료 광기가 156만큼 추가로 제공됩니다.
   źródło: IAPProduct.json :: dataList[id=13].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains 1014 Paid Lunacy.\nYou will also receive 156 Free Lunacy as a bonus.
   PL: Otrzymasz 1014 Płatnego Szaleństwa.\nBonusowo dostaniesz dodatkowo 156 darmowego Szaleństwa.
858. [Przedmioty, sklep i profil gracza [14] — nazwa] 광기 상자
   źródło: IAPProduct.json :: dataList[id=14].name
   (powtórzenie elementu 846 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Przedmioty, sklep i profil gracza [14] — opis] 유료 광기를 2147만큼 획득할 수 있습니다.\n보너스로 무료 광기가 323만큼 추가로 제공됩니다.
   źródło: IAPProduct.json :: dataList[id=14].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains 2147 Paid Lunacy.\nYou will also receive 323 Free Lunacy as a bonus.
   PL: Otrzymasz 2147 Płatnego Szaleństwa.\nBonusowo dostaniesz dodatkowo 323 darmowego Szaleństwa.
860. [Przedmioty, sklep i profil gracza [15] — nazwa] 광기 더미
   źródło: IAPProduct.json :: dataList[id=15].name
   (powtórzenie elementu 848 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Przedmioty, sklep i profil gracza [15] — opis] 유료 광기를 4103만큼 획득할 수 있습니다.\n보너스로 무료 광기가 642만큼 추가로 제공됩니다.
   źródło: IAPProduct.json :: dataList[id=15].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains 4103 Paid Lunacy.\nYou will also receive 642 Free Lunacy as a bonus.
   PL: Otrzymasz 4103 Płatnego Szaleństwa.\nBonusowo dostaniesz dodatkowo 642 darmowego Szaleństwa.
862. [Przedmioty, sklep i profil gracza [16] — nazwa] 광기 모음
   źródło: IAPProduct.json :: dataList[id=16].name
   (powtórzenie elementu 850 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Przedmioty, sklep i profil gracza [16] — opis] 유료 광기를 8336만큼 획득할 수 있습니다.\n보너스로 무료 광기가 1349만큼 추가로 제공됩니다.
   źródło: IAPProduct.json :: dataList[id=16].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Contains 8336 Paid Lunacy.\nYou will also receive 1349 Free Lunacy as a bonus.
   PL: Otrzymasz 8336 Płatnego Szaleństwa.\nBonusowo dostaniesz dodatkowo 1349 darmowego Szaleństwa.
864. [Przedmioty, sklep i profil gracza [21] — nazwa] 월간 광기
   źródło: IAPProduct.json :: dataList[id=21].name
   limit: do 40 znaków
   EN: Monthly Lunacy Supply
   PL: Miesięczny Pakiet Szaleństwa
865. [Przedmioty, sklep i profil gracza [21] — opis] 유료 광기를 650만큼 획득할 수 있습니다.\n매일 접속 시, 무료 광기를 65만큼 30일 동안 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=21].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Get 650 Paid Lunacy instantly upon purchase.\nReceive an additional 65 Free Lunacy each day you log in for 30 days.
   PL: Natychmiast po zakupie otrzymasz 650 Płatnego Szaleństwa.\nZa każde logowanie przez 30 dni otrzymasz dodatkowo 65 darmowego Szaleństwa.
866. [Przedmioty, sklep i profil gracza [22] — nazwa] 월간 광기 소형
   źródło: IAPProduct.json :: dataList[id=22].name
   limit: do 40 znaków
   EN: Monthly Lunacy Batch
   PL: Miesięczny Półpakiet Szaleństwa
867. [Przedmioty, sklep i profil gracza [22] — opis] 유료 광기를 130만큼 획득할 수 있습니다.\n매일 접속 시, 무료 광기를 39만큼 30일 동안 획득할 수 있습니다.
   źródło: IAPProduct.json :: dataList[id=22].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Get 130 Paid Lunacy instantly upon purchase.\nReceive an additional 39 Free Lunacy each day you log in for 30 days.
   PL: Natychmiast po zakupie otrzymasz 130 Płatnego Szaleństwa.\nZa każde logowanie przez 30 dni otrzymasz dodatkowo 39 darmowego Szaleństwa.
868. [Przedmioty, sklep i profil gracza [101] — nazwa] 월간 추출 패키지
   źródło: IAPProduct.json :: dataList[id=101].name
   limit: do 40 znaków
   EN: Monthly Extraction Pack
   PL: Miesięczny Pakiet Ekstrakcji
869. [Przedmioty, sklep i profil gracza [101] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 650\n· 추출 10회 티켓 x 1
   źródło: IAPProduct.json :: dataList[id=101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x650\n· Decaextraction Ticket x1
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 650\n· Bilet Dekaekstrakcji x 1
870. [Przedmioty, sklep i profil gracza [102] — nazwa] 월간 성장 지원 패키지 I
   źródło: IAPProduct.json :: dataList[id=102].name
   (powtórzenie elementu 604 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Przedmioty, sklep i profil gracza [102] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1690\n· 추출 10회 티켓 x 2\n· 인격 특수 강화 티켓 II x 1\n· 인격 특수 강화 티켓 I x 2\n· 인격 학습 티켓 III x 10\n· 인격 학습 티켓 II x 30
   źródło: IAPProduct.json :: dataList[id=102].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x1690\n· Decaextraction Ticket x2\n· Level Boost Ticket II x1\n· Level Boost Ticket I x2\n· Identity Training Ticket III x10\n· Identity Training Ticket II x30
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Bilet Specjalnego Wzmocnienia Tożsamości II x 1\n· Bilet Specjalnego Wzmocnienia Tożsamości I x 2\n· Bilet Treningu Tożsamości III x 10\n· Bilet Treningu Tożsamości II x 30
872. [Przedmioty, sklep i profil gracza [103] — nazwa] 월간 성장 지원 패키지 II
   źródło: IAPProduct.json :: dataList[id=103].name
   limit: do 40 znaków
   EN: Monthly Training Pack II
   PL: Miesięczny Pakiet Wsparcia Rozwoju II
873. [Przedmioty, sklep i profil gracza [103] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 1690\n· 추출 10회 티켓 x 2\n· 끈 x 120
   źródło: IAPProduct.json :: dataList[id=103].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Paid Lunacy x1690\n· Decaextraction Ticket x2\n· Thread x120
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 1690\n· Bilet Dekaekstrakcji x 2\n· Nić x 120
874. [Przedmioty, sklep i profil gracza [104] — nazwa] 월간 경험치 패키지
   źródło: IAPProduct.json :: dataList[id=104].name
   limit: do 40 znaków
   EN: Monthly EXP Pack
   PL: Miesięczny Pakiet PD
875. [Przedmioty, sklep i profil gracza [104] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 특수 강화 티켓 IV x 2\n· 인격 학습 티켓 IV x 20\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=104].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Level Boost Ticket IV x2\n· Identity Training Ticket IV x20\n· Identity Training Ticket III x20
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Bilet Specjalnego Wzmocnienia Tożsamości IV x 2\n· Bilet Treningu Tożsamości IV x 20\n· Bilet Treningu Tożsamości III x 20
876. [Przedmioty, sklep i profil gracza [105] — nazwa] 월간 끈 패키지
   źródło: IAPProduct.json :: dataList[id=105].name
   limit: do 40 znaków
   EN: Monthly Thread Pack
   PL: Miesięczny Pakiet Nici
877. [Przedmioty, sklep i profil gracza [105] — opis] 매월 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x 300
   źródło: IAPProduct.json :: dataList[id=105].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A monthly offer that contains the following:\n\n· Thread x300
   PL: Oferta comiesięczna — zawiera następujące składniki:\n\n· Nić x 300
878. [Przedmioty, sklep i profil gracza [111] — nazwa] 관리자 입사 지원 패키지
   źródło: IAPProduct.json :: dataList[id=111].name
   limit: do 50 znaków
   EN: New Manager’s Onboarding Pack
   PL: Pakiet Wdrożenia Nowego Kierownika
879. [Przedmioty, sklep i profil gracza [111] — opis] 신입 관리자를 위한 상품으로 단 한 번만 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 3성 인격 출현 추출 티켓 x 1\n· 추출 10회 티켓 x 1
   źródło: IAPProduct.json :: dataList[id=111].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A one-time offer for newly recruited managers. The pack contains the following:\n\n· 3★ Guarantee Decaextraction Ticket x1\n· Decaextraction Ticket x1
   PL: Oferta jednorazowa dla świeżo zrekrutowanych Kierowników — zawiera następujące składniki:\n\n· Bilet Dekstrakcji Gwarantowanej 3★ x 1\n· Bilet Dekaekstrakcji x 1
880. [Przedmioty, sklep i profil gracza [121] — nazwa] 시즌 1 정착 지원품
   źródło: IAPProduct.json :: dataList[id=121].name
   limit: do 40 znaków
   EN: Season 1 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 1
881. [Przedmioty, sklep i profil gracza [121] — opis] 시즌 1 오리엔테이션 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 특수 강화 티켓 III x 1\n· 인격 학습 티켓 II x 40\n· 끈 x 80\n· 시즌 1 자아 파편 선택 상자 x 40
   źródło: IAPProduct.json :: dataList[id=121].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during the orientation period of Season 1. The pack contains the following:\n\n· Lunacy x5040\n· Decaextraction Ticket x3\n· Level Boost Ticket III x1\n· Identity Training Ticket II x40\n· Thread x80\n· Season 1 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 1: Orientation — zawiera następujące składniki:\n\n· Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Specjalnego Wzmocnienia Tożsamości III x 1\n· Bilet Treningu Tożsamości II x 40\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 1 x 40
882. [Przedmioty, sklep i profil gracza [122] — nazwa] 시즌 2 정착 지원품
   źródło: IAPProduct.json :: dataList[id=122].name
   limit: do 40 znaków
   EN: Season 2 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 2
883. [Przedmioty, sklep i profil gracza [122] — opis] 시즌 2 레미니센스 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 특수 강화 티켓 III x 1\n· 인격 학습 티켓 III x 30\n· 끈 x 80\n· 시즌 2 자아 파편 선택 상자 x 40
   źródło: IAPProduct.json :: dataList[id=122].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during the orientation period of Season 2. The pack contains the following:\n\n· Lunacy x5040\n· Decaextraction Ticket x3\n· Level Boost Ticket III x1\n· Identity Training Ticket III x30\n· Thread x80\n· Season 2 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 2: Reminiscence — zawiera następujące składniki:\n\n· Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Specjalnego Wzmocnienia Tożsamości III x 1\n· Bilet Treningu Tożsamości III x 30\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 2 x 40
884. [Przedmioty, sklep i profil gracza [123] — nazwa] 시즌 3 정착 지원품
   źródło: IAPProduct.json :: dataList[id=123].name
   limit: do 40 znaków
   EN: Season 3 Settler Supplies
   PL: Wsparcie Osadnika Sezonu 3
885. [Przedmioty, sklep i profil gracza [123] — opis] 시즌 3 본 보야지 기간 동안 구입할 수 있으며, 다음 구성품을 획득할 수 있습니다.\n\n· 광기 x 5040\n· 추출 10회 티켓 x 3\n· 인격 특수 강화 티켓 III x 1\n· 인격 학습 티켓 III x 30\n· 끈 x 80\n· 시즌 3 자아 파편 선택 상자 x 40
   źródło: IAPProduct.json :: dataList[id=123].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Only available for purchase during the orientation period of Season 3. The pack contains the following:\n\n· Lunacy x5040\n· Decaextraction Ticket x3\n· Level Boost Ticket III x1\n· Identity Training Ticket III x30\n· Thread x80\n· Season 3 Nominable Egoshard Crate x40
   PL: Dostępny do zakupu w okresie Sezonu 3: Bon Voyage — zawiera następujące składniki:\n\n· Szaleństwo x 5040\n· Bilet Dekaekstrakcji x 3\n· Bilet Specjalnego Wzmocnienia Tożsamości III x 1\n· Bilet Treningu Tożsamości III x 30\n· Nić x 80\n· Imienna Skrzynka Odłamków E.G.O Sezonu 3 x 40
886. [Przedmioty, sklep i profil gracza [131] — nazwa] 주간 추출 패키지
   źródło: IAPProduct.json :: dataList[id=131].name
   limit: do 40 znaków
   EN: Weekly Extraction Pack
   PL: Tygodniowy Pakiet Ekstrakcji
887. [Przedmioty, sklep i profil gracza [131] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 유료 광기 x 273\n· 추출 티켓 x 5
   źródło: IAPProduct.json :: dataList[id=131].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Paid Lunacy x273\n· Extraction Ticket x5
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Płatne Szaleństwo x 273\n· Bilet Ekstrakcji x 5
888. [Przedmioty, sklep i profil gracza [133] — nazwa] 주간 끈 패키지
   źródło: IAPProduct.json :: dataList[id=133].name
   limit: do 40 znaków
   EN: Weekly Thread Pack
   PL: Tygodniowy Pakiet Nici
889. [Przedmioty, sklep i profil gracza [133] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x 75
   źródło: IAPProduct.json :: dataList[id=133].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Thread x75
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Nić x 75
890. [Przedmioty, sklep i profil gracza [134] — nazwa] 주간 엔케팔린 패키지
   źródło: IAPProduct.json :: dataList[id=134].name
   limit: do 40 znaków
   EN: Weekly Enkephalin Pack
   PL: Tygodniowy Pakiet Enkefaliny
891. [Przedmioty, sklep i profil gracza [134] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 엔케팔린 박스 x 20
   źródło: IAPProduct.json :: dataList[id=134].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Enkephalin Box x20
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Skrzynka Enkefaliny x 20
892. [Przedmioty, sklep i profil gracza [135] — nazwa] 주간 경험치 패키지
   źródło: IAPProduct.json :: dataList[id=135].name
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Przedmioty, sklep i profil gracza [135] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 인격 특수 강화 티켓 III x 1\n· 인격 학습 티켓 IV x 12\n· 인격 학습 티켓 III x 20
   źródło: IAPProduct.json :: dataList[id=135].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Level Boost Ticket III x1\n· Identity Training Ticket IV x12\n· Identity Training Ticket III x20
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Bilet Specjalnego Wzmocnienia Tożsamości III x 1\n· Bilet Treningu Tożsamości IV x 12\n· Bilet Treningu Tożsamości III x 20
894. [Przedmioty, sklep i profil gracza [136] — nazwa] 주간 끈 패키지
   źródło: IAPProduct.json :: dataList[id=136].name
   (powtórzenie elementu 888 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Przedmioty, sklep i profil gracza [136] — opis] 매주 초기화되는 상품으로 다음 구성품을 획득할 수 있습니다.\n\n· 끈 x 100
   źródło: IAPProduct.json :: dataList[id=136].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A weekly offer that contains the following:\n\n· Thread x100
   PL: Oferta cotygodniowa — zawiera następujące składniki:\n\n· Nić x 100
896. [Przedmioty, sklep i profil gracza [141] — nazwa] 월간 추출 티켓 패키지 I
   źródło: IAPProduct.json :: dataList[id=141].name
   limit: do 50 znaków
   EN: Monthly Extraction Ticket Pack I
   PL: Miesięczny Pakiet Biletów Ekstrakcji I
