# Paczka AI P12 (Fala 1 · 1D) — Samouczki systemowe i wskazówki ekranu ładowania (część 2/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P12_1d_samouczki_i_wskazowki_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P12_1d_samouczki_i_wskazowki_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Samouczek i wskazówki: TutorialMainUIText
- plik gry: `TutorialMainUIText.json`

1. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_05_desc_02] — tekst] 해당 역을 클리어 시 얻는 보상이 하단에 표시됩니다. 일부 역의 보상은 일정 횟수 이상의 순환 횟수 조건이 추가로 요구됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_05_desc_02].content
   limit: do 180 znaków
   EN: Rewards for clearing this Station are displayed below. Some Stations' rewards will unlock only after meeting certain Cycle Count conditions.
   PL: Poniżej widnieją nagrody za ukończenie danej stacji. Niektóre nagrody wymagają dodatkowo osiągnięcia określonej liczby cykli.
2. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_06_title_01] — tekst] 전투 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_06_title_01].content
   limit: do 120 znaków
   EN: Team Setup
   PL: Ustawienie drużyny
3. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_06_desc_01] — tekst] 전투는 최대 7인까지 편성할 수 있습니다. 단, 7인 미만의 인격이 입장하였을 때 턴이 진행되어도 슬롯 수가 증가하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_06_desc_01].content
   limit: do 240 znaków
   EN: You can select up to 7 participants for an encounter. While you can select less than 7 combat participants, no additional Skill slots will be given for them throughout the encounter.
   PL: Do walki możesz wystawić maksymalnie 7 uczestników. Jeśli wejdzie mniej niż 7 Tożsamości, liczba slotów umiejętności nie zwiększy się wraz z kolejnymi turami.
4. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_07_title_01] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_07_title_01].content
   limit: do 120 znaków
   EN: Encounter
   PL: Walka
5. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_07_desc_01] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_07_desc_01].content
   limit: do 180 znaków
   EN: Every battle in the Refraction Railway will allow you to directly match ally skills against enemy skills, just like in Focused Encounters.
   PL: Wszystkie walki odbywają się w trybie starcia skupionego, w którym bezpośrednio kierujesz umiejętności sojuszników przeciwko umiejętnościom wrogów.
6. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_07_desc_02] — tekst] 클리어 시 전투에 참여한 인격의 체력, 정신력, 조작 패널에 배치된 스킬, 인격 별로 사용한 스킬과 남은 스킬 상태가 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_07_desc_02].content
   limit: do 150 znaków
   EN: Upon completion, your Identities' HP, SP, Skills in the Dashboard, used Skills, and remaining Skills are saved.
   PL: Po ukończeniu zapisywane są PŻ i PP uczestniczących Tożsamości, umiejętności na panelu dowodzenia oraz zużyte i pozostałe umiejętności każdej z nich.
7. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_08_desc_01] — tekst] 전투 이후 남은 E.G.O 자원은 다음 역에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_08_desc_01].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a Station can be carried over to the next Station.
   PL: Zasoby E.G.O pozostałe po walce można wykorzystać na następnej stacji.
8. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_08_desc_02] — tekst] 순환한 횟수와 현재 역에 도달하기까지 걸린 누적 턴 수가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_08_desc_02].content
   limit: do 120 znaków
   EN: Your Cycle Count and Total Turns up to this Station are displayed here.
   PL: Wyświetlana jest liczba cykli oraz łączna liczba tur potrzebnych na dotarcie do bieżącej stacji.
9. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_08_desc_03] — tekst] 편성한 인격의 체력, 정신력, 사망 상태가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_08_desc_03].content
   limit: do 120 znaków
   EN: The HP, SP, and availability of your Identities are shown here.
   PL: Wyświetlane są PŻ, PP oraz stan poległych Tożsamości w składzie.
10. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_09_desc_01] — tekst] 다음 역 입장 시 지난 역에서 저장된 항목을 불러옵니다.\n아군 · 적 속도의 경우에는 역 입장 시점에서 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_09_desc_01].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon entering the next Station, information saved in the last Station will be loaded.\nThe Speed of allies & enemies are saved upon entering a Station.
   PL: Po wejściu na kolejną stację wczytywane są dane zapisane na poprzedniej stacji.\nSzybkość sojuszników i wrogów zapisywana jest w momencie wejścia na stację.
11. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_09_desc_02] — tekst] 아군 · 적 속도의 경우에는 역 입장 시점에서 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_09_desc_02].content
   limit: do 120 znaków
   EN: The Speed of allies & enemies are saved upon entering a Station.
   PL: Szybkość sojuszników i wrogów zapisywana jest w momencie wejścia na stację.
12. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_10_desc_01] — tekst] 스테이지 포기 시, 해당 역을 입장하기 직전 상태로 되돌아갑니다.\n직전 전투 시작 시점의 인격 체력, 정신력, 속도, 조작 패널의 스킬, 인격 별 스킬 사용 상태, 적의 속도가 동일하게 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_10_desc_01].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon forfeiting a Stage, you will be returned to the state immediately before entering this stage.\nIdentities' HP, SP, Speed, Skills in the Dashboard, used Skills, remaining Skills, and enemy Speed at the state immediately before entering the Station will not be changed.
   PL: Poddanie etapu cofa stan gry do momentu tuż przed wejściem na daną stację.\nPŻ, PP i Szybkość Tożsamości, umiejętności na panelu dowodzenia, stan zużycia umiejętności oraz Szybkość wrogów z początku poprzedniej walki pozostają bez zmian.
13. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_10_desc_02] — tekst] 직전 전투 시작 시점의 인격 체력, 정신력, 속도, 조작 패널의 스킬, 인격 별 스킬 사용 상태, 적의 속도가 동일하게 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_10_desc_02].content
   limit: do 220 znaków
   EN: Identities' HP, SP, Speed, Skills in the Dashboard, used Skills, remaining Skills, and enemy Speed at the state immediately before entering the Station will not be changed.
   PL: PŻ, PP i Szybkość Tożsamości, umiejętności na panelu dowodzenia, stan zużycia umiejętności oraz Szybkość wrogów z początku poprzedniej walki pozostają bez zmian.
14. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_11_desc_01] — tekst] 스테이지 패배 시, 해당 역을 입장하기 직전 상태로 되돌아가거나 남은 인격으로 이어서 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_11_desc_01].content
   limit: do 180 znaków
   EN: Upon defeat, you can either return to the state immediately before entering that Station or continue using your surviving Identities.
   PL: W razie porażki na etapie możesz wrócić do stanu tuż przed wejściem na stację lub kontynuować walkę ocalałymi Tożsamościami.
15. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_11_desc_02] — tekst] 이어서 진행할 경우 등장하는 적의 체력이 유지되며, 남은 체력 비율이 역 위쪽에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_11_desc_02].content
   limit: do 170 znaków
   EN: Should you choose to continue, enemies' current HP will be saved. Their remaining HP percentages will be shown above the Station.
   PL: Jeśli zdecydujesz się kontynuować, aktualne PŻ wrogów zostaną zachowane, a procent pozostałych PŻ pojawi się nad stacją.
16. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_12_title_01] — tekst] 순환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_12_title_01].content
   limit: do 120 znaków
   EN: Cycle
   PL: Cykl
17. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_12_desc_01] — tekst] 노선 위에 있는 개방된 역을 모두 클리어하였다면 첫 번째 역(시착역)으로 이동하여 순환할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_12_desc_01].content
   limit: do 150 znaków
   EN: After clearing all open Stations on the Line, you can return to Station #1(First Stop) and continue the Cycle.
   PL: Po ukończeniu wszystkich otwartych stacji na linii możesz przejechać na pierwszą stację (Stację początkową) i rozpocząć kolejny cykl.
18. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_12_desc_02] — tekst] 순환을 진행할 경우, 순환 횟수가 1 증가합니다. 일부 역은 순환 횟수에 따라 추가로 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_12_desc_02].content
   limit: do 180 znaków
   EN: Should you choose to continue the Cycle, you will gain 1 Cycle Count. Some Stations will open only after reaching certain Cycle Counts.
   PL: Kontynuowanie cyklu zwiększa liczbę cykli o 1. Niektóre stacje odblokowują się dopiero po osiągnięciu określonej liczby cykli.
19. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_13_title_01] — tekst] 버프 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_13_title_01].content
   limit: do 120 znaków
   EN: Select Buffs
   PL: Wybór wzmocnień
20. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_13_desc_01] — tekst] 순환을 진행할 때마다 아군 버프, 적 버프를 각각 1개씩 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_13_desc_01].content
   limit: do 120 znaków
   EN: At the end of every Cycle, you can choose 1 Ally Buff and 1 Enemy Buff.
   PL: Przy każdym kolejnym cyklu wybierasz po 1 wzmocnieniu sojuszników oraz 1 wzmocnieniu wrogów.
21. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_13_desc_02] — tekst] 선택한 모든 효과들은 이후의 전투에서 누적되어 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_13_desc_02].content
   limit: do 120 znaków
   EN: All selected Buffs will carry over to the coming encounters.
   PL: Wszystkie wybrane efekty kumulują się i obowiązują w kolejnych walkach.
22. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_14_desc_01] — tekst] 아군 버프 1종을 선택합니다. 직전 순환에서 선택한 효과는 고를 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_14_desc_01].content
   limit: do 120 znaków
   EN: Select 1 Ally Buff. You cannot select the same Buff you selected in the last Cycle.
   PL: Wybierz 1 wzmocnienie sojuszników. Nie możesz wybrać efektu wybranego w bezpośrednio poprzedzającym cyklu.
23. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_15_desc_01] — tekst] 적 버프를 1종 선택합니다. 이전에 선택한 효과를 고를 수 없습니다.\n단, 모든 효과를 한 번씩 선택하였다면 선택 기회가 초기화되어 다시 원하는 효과를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_15_desc_01].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select 1 Enemy Buff. You cannot select the same Buff you selected in the last Cycle.\nHowever, if all Buffs had been selected at least once, selection limits will reset and you can select any Buff you want again.
   PL: Wybierz 1 wzmocnienie wrogów. Nie możesz wybrać efektu wybranego wcześniej.\nJeśli jednak wszystkie efekty zostały już wybrane po razie, pula wyboru się resetuje i znów możesz wybrać dowolny efekt.
24. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_15_desc_03] — tekst] 직접 선택할 수 있는 버프 이외에 매 순환 시마다 1개의 고정 버프가 추가로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_15_desc_03].content
   limit: do 120 znaków
   EN: Aside from the Buffs you select, every Cycle also gives 1 fixed Buff.
   PL: Oprócz wybieranych wzmocnień każdy cykl nakłada dodatkowo 1 stałe wzmocnienie.
25. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_16_desc_01] — tekst] 순환을 5번 진행할 때마다 사망한 아군 인격 중 하나를 부활시킬 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_16_desc_01].content
   limit: do 120 znaków
   EN: Every 5 Cycles, you will have a chance to revive one of your dead allied Identities.
   PL: Co 5 ukończonych cykli możesz wskrzesić jedną z poległych sojuszniczych Tożsamości.
26. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_17_title_01] — tekst] 종착역
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_17_title_01].content
   limit: do 120 znaków
   EN: The Terminus
   PL: Stacja końcowa
27. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_17_desc_01] — tekst] 순환을 진행하였다면 (순환 횟수가 1 이상이면) 노선 중앙에 있는 종착역이 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_17_desc_01].content
   limit: do 170 znaków
   EN: If you have completed a Cycle (If you have 1 or more Cycle Counts), the Terminus in the middle of this Line will be activated.
   PL: Po ukończeniu cyklu (gdy liczba cykli wynosi co najmniej 1) aktywuje się Stacja końcowa pośrodku linii.
28. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_17_desc_02] — tekst] 종착역이 활성화되면 어느 역에서든 자유롭게 종착역에 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_17_desc_02].content
   limit: do 120 znaków
   EN: Once the Terminus is activated, you can access it from any Station.
   PL: Po aktywacji Stacji końcowej możesz swobodnie wejść na nią z dowolnej stacji.
29. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_18_desc_01] — tekst] 종착역에 입장하면 더이상 이전 역으로 되돌아갈 수 없기 때문에 신중한 선택이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_18_desc_01].content
   limit: do 120 znaków
   EN: You cannot go back to the previous Station once you enter the Terminus. Choose carefully.
   PL: Po wejściu na Stację końcową nie można już wrócić na poprzednią stację — podejmij decyzję rozważnie.
30. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_18_desc_02] — tekst] 종착역을 클리어하는 것이 거울굴절철도 2호선의 최종 목표이며, 클리어하게 되면 순환 횟수와 누적 턴 수, 참여한 인격과 E.G.O, 버프 목록이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_18_desc_02].content
   limit: do 250 znaków
   EN: The ultimate goal of Refraction Railway Line 2 is to complete the Terminus. Upon completion, your Cycle Count, Total Turns, participating Identities & E.G.O, and selected Buffs will be recorded.
   PL: Ukończenie Stacji końcowej to ostateczny cel Kolei Załamania — Linii 2. Po jej przejściu zapisywane są liczba cykli, łączna liczba tur, uczestniczące Tożsamości i E.G.O oraz lista wzmocnień.
31. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_19_title_01] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_19_title_01].content
   limit: do 120 znaków
   EN: Banner Requisites
   PL: Warunki zdobycia banerów
32. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_19_desc_01] — tekst] 이벤트 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_19_desc_01].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów wydarzenia.
33. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_19_desc_02] — tekst] 획득 조건이 어려울수록 더욱 특별한 배너를 얻게 됩니다.\n배너를 획득하면 가장 높은 기록의 순환 횟수와 누적 턴 수가 배너에 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_19_desc_02].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: More special banners have harder acquisition conditions.\nUpon acquisition of the banner, your best Cycle Count and Total Turn records will be displayed on them.
   PL: Im trudniejszy warunek zdobycia, tym bardziej wyjątkowy baner otrzymasz.\nPo zdobyciu baneru widnieją na nim liczba cykli oraz łączna liczba tur z twojego najlepszego rekordu.
34. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_19_desc_03] — tekst] 배너를 획득하면 가장 높은 기록의 순환 횟수와 누적 턴 수가 배너에 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_19_desc_03].content
   limit: do 140 znaków
   EN: Upon acquisition of the banner, your best Cycle Count and Total Turn records will be displayed on them.
   PL: Po zdobyciu baneru widnieją na nim liczba cykli oraz łączna liczba tur z twojego najlepszego rekordu.
35. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_20_title_01] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_20_title_01].content
   limit: do 120 znaków
   EN: Lost & Found
   PL: Biuro Rzeczy Znalezionych
36. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_20_desc_01] — tekst] 스테이지를 처음으로 클리어하거나 특정 조건을 만족할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_20_desc_01].content
   limit: do 170 znaków
   EN: After clearing a stage in the Line for the first time or meeting a certain condition, the rewards will be sent to the Lost & Found.
   PL: Po pierwszym ukończeniu etapu lub spełnieniu określonego warunku nagroda trafia do Biura Rzeczy Znalezionych i zostaje aktywowana.
37. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_20_desc_02] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다. 이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_20_desc_02].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To gain access to a reward for the first time at Lost & Found, a number of Enkephalin Modules will be required.\nAfterward, you may freely access it and claim rewards you’ve earned at no additional cost.
   PL: Aby po raz pierwszy odebrać nagrody w Biurze Rzeczy Znalezionych, należy jednorazowo zapłacić określoną liczbę Modułów Enkefaliny.\nWszystkie kolejne odblokowane nagrody odbierzesz w dowolnej chwili bez dodatkowych Modułów Enkefaliny.
38. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_21_title_01] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_21_title_01].content
   limit: do 120 znaków
   EN: Total Record
   PL: Historia rekordów
39. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_21_desc_01] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_21_desc_01].content
   limit: do 150 znaków
   EN: Upon clearing the final stage, your Refraction Railway play record will be saved. Up to 20 records can be viewed.
   PL: Po ukończeniu finałowego etapu zapisywany jest rekord przejścia Kolei Załamania; możesz przeglądać maksymalnie 20 rekordów.
40. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_21_desc_02] — tekst] 기록이 20개를 넘어갈 경우에는 순환 횟수가 적은 기록이 먼저 사라지게 되며, 순환 횟수가 동일할 경우에는 누적 턴 수가 많은 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_21_desc_02].content
   limit: do 280 znaków
   EN: When you have made more than 20 records, records with the least Cycle Count will be deleted first. If there are two lowest records with the same Cycle Count, the one with a higher Total Turn Count will be deleted.
   PL: Po przekroczeniu 20 rekordów w pierwszej kolejności usuwane są zapisy z najmniejszą liczbą cykli, a przy równej liczbie cykli — te z większą łączną liczbą tur.
41. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_1_title_01] — tekst] 노선 이동 버튼
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_1_title_01].content
   limit: do 120 znaków
   EN: Alter Line Button
   PL: Przycisk zmiany linii
42. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_1_desc_01] — tekst] 노선 위에 있는 개방된 역을 모두 클리어하였다면 다음 노선으로 이동할 수 있는 버튼이 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_1_desc_01].content
   limit: do 130 znaków
   EN: Upon clearing all open Stations on the Line, a button to continue to the next Line will appear.
   PL: Po ukończeniu wszystkich otwartych stacji na linii pojawia się przycisk przejścia na kolejną linię.
43. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_2_title_01] — tekst] 순환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_2_title_01].content
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_2_desc_01] — tekst] 노선을 타고 첫 번째 역(시착역)으로 이동할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_2_desc_01].content
   limit: do 120 znaków
   EN: You can take the Line to return to Station #1(First Stop).
   PL: Możesz pojechać linią z powrotem na pierwszą stację (Stację początkową).
45. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_2_desc_02] — tekst] 이 과정에서 순환 횟수가 1 증가하며, 이후 전투에서 적용될 아군 버프 · 적 버프를 각각 선택하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_2_desc_02].content
   limit: do 190 znaków
   EN: In this process, you will gain 1 Cycle Count, and be asked to select 1 Ally Buff and 1 Enemy Buff that will be applied to the upcoming encounters.
   PL: Zwiększa to liczbę cykli o 1, a następnie wybierasz po jednym wzmocnieniu sojuszników i wrogów na nadchodzące walki.
46. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_3_title_01] — tekst] 버프 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_3_title_01].content
   (powtórzenie elementu 19 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_3_desc_01] — tekst] 순환을 진행할 때마다 아군 버프, 적 버프를 각각 1개씩 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_3_desc_01].content
   (powtórzenie elementu 20 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_3_desc_02] — tekst] 선택한 모든 효과들은 이후의 전투에서 누적되어 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_3_desc_02].content
   (powtórzenie elementu 21 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_4_desc_01] — tekst] 아군 버프 1종을 선택합니다. 직전 순환에서 선택한 효과는 고를 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_4_desc_01].content
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
50. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_5_desc_01] — tekst] 적 버프를 1종 선택합니다. 이전에 선택한 효과를 고를 수 없습니다.\n단, 모든 효과를 한 번씩 선택하였다면 선택 기회가 초기화되어 다시 원하는 효과를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_5_desc_01].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_5_desc_03] — tekst] 직접 선택할 수 있는 버프 이외에 매 순환 시마다 1개의 고정 버프가 추가로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_5_desc_03].content
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_6_title_01] — tekst] 종착역 이동 버튼
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_6_title_01].content
   limit: do 120 znaków
   EN: Button to the Terminus
   PL: Przycisk Stacji końcowej
53. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_6_desc_01] — tekst] 버프 선택을 완료하면 노선을 타고 첫 번째 역(시착역)으로 이동합니다. 일부 역은 순환 횟수에 따라 추가로 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_6_desc_01].content
   limit: do 180 znaków
   EN: Once you've selected your Buffs, take the Line to Station #1(First Stop). Some Stations will open only after reaching certain Cycle Counts.
   PL: Po wybraniu wzmocnień przejedziesz linią na pierwszą stację (Stację początkową). Niektóre stacje otwierają się dodatkowo wraz ze wzrostem liczby cykli.
54. [Samouczek i wskazówki [tutorial_mainui_22_railway2_page_6_desc_02] — tekst] 순환을 진행한 이후에는 노선 중앙에 있는 종착역이 활성화되며, 종착역으로 이동하는 버튼이 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_22_railway2_page_6_desc_02].content
   limit: do 180 znaków
   EN: After completing a Cycle, the Terminus in the middle of the Line will be activated. A button to enter the Terminus will also be activated.
   PL: Po ukończeniu cyklu aktywuje się Stacja końcowa pośrodku linii oraz przycisk przejazdu na Stację końcową.
55. [Samouczek i wskazówki [tutorial_mainui_23_railway2_page_1_desc_01] — tekst] 종착역에 입장하면 더이상 이전 역으로 되돌아갈 수 없기 때문에 신중한 선택이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_23_railway2_page_1_desc_01].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Samouczek i wskazówki [tutorial_mainui_23_railway2_page_1_desc_02] — tekst] 종착역을 클리어하는 것이 거울굴절철도 2호선의 최종 목표이며, 클리어하게 되면 순환 횟수와 누적 턴 수, 참여한 인격과 E.G.O, 버프 목록이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_23_railway2_page_1_desc_02].content
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [Samouczek i wskazówki [tutorial_mainui_railway2_mainTitle] — tekst] 거울굴절철도 2호선
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway2_mainTitle].content
   limit: do 120 znaków
   EN: Refraction Railway Line 2
   PL: Kolej Załamania — Linia 2
58. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_08_title_01] — tekst] 종착역 이동 버튼
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_08_title_01].content
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_04_desc_02] — tekst] 입장 시점에는 제 3역까지만 개방되어있으며, 순환 횟수에 따라 제 4역에서부터 제 8역까지가 차례대로 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_04_desc_02].content
   limit: do 170 znaków
   EN: Only 3 Stations will be open upon entry. Growing your Cycle Count will sequentially open the subsequent Stations (Station #4 ~ #8).
   PL: Na początku otwarte są tylko stacje do Stacji 3; wraz ze wzrostem liczby cykli kolejno odblokowują się Stacje od 4 do 8.
60. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction] — tekst] 발푸르기스의 밤
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction].content
   limit: do 120 znaków
   EN: Walpurgis Night
   PL: Noc Walpurgii
61. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction_page_01_desc_01] — tekst] 이벤트 기간 동안 발푸르기스의 밤 특정 추출이 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction_page_01_desc_01].content
   limit: do 120 znaków
   EN: Walpurgis Night Target Extractions will be available during the event period.
   PL: W trakcie wydarzenia dostępna jest Ekstrakcja Celowana Nocy Walpurgii.
62. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction_page_01_desc_02] — tekst] 발푸르기스의 밤 특정 추출에서는 이번 회차의 발푸르기스의 밤 인격 및 E.G.O의 등장 확률이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction_page_01_desc_02].content
   limit: do 190 znaków
   EN: Walpurgis Night Target Extractions will have higher Extraction rates for Identities and E.G.O from the currently active Walpurgis Night event.
   PL: W Ekstrakcji Celowanej Nocy Walpurgii zwiększona jest szansa wylosowania Tożsamości oraz E.G.O z bieżącej edycji Nocy Walpurgii.
63. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction_page_02_desc_01] — tekst] 이벤트 기간 동안 다른 추출(시즌 관련 추출 제외)에서도 이번 회차의 발푸르기스의 밤 인격 및 E.G.O가 등장합니다.\n\n단, 이러한 경우에는 등장 확률이 별도로 상승하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction_page_02_desc_01].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During the event period, Identities & E.G.O from the current Walpurgis Night event will be Extractable from other Extraction banners(save for Season relevant Extraction banners) as well.\n\nHowever, their extraction rates will be identical to those of other Identities & E.G.O.
   PL: W trakcie wydarzenia Tożsamości oraz E.G.O z bieżącej Nocy Walpurgii mogą pojawić się także w innych Ekstrakcjach (z wyjątkiem Ekstrakcji powiązanych z sezonem).\n\nW takich Ekstrakcjach szansa ich pojawienia się nie jest jednak dodatkowo zwiększona.
64. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction_page_03_desc_01] — tekst] 이벤트 기간 동안 모든 추출(시즌 관련 추출 제외)에서 다른 회차의 발푸르기스의 밤 인격 및 E.G.O가 등장합니다.\n\n단, 이러한 경우에는 다른 인격 및 E.G.O와 등장 확률이 동일합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction_page_03_desc_01].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During the event period, previous Walpurgis Night Identities & E.G.O will be Extractable from all Extraction banners(save for Season relevant Extraction banners).\n\nHowever, they will not receive increased rates for those Extractions.
   PL: W trakcie wydarzenia we wszystkich Ekstrakcjach (z wyjątkiem powiązanych z sezonem) mogą pojawić się Tożsamości i E.G.O z poprzednich edycji Nocy Walpurgii.\n\nSzansa ich wylosowania jest wówczas taka sama jak dla pozostałych Tożsamości i E.G.O.
65. [Samouczek i wskazówki [tutorial_walpurgisnacht_extraction_page_04_desc_01] — tekst] 이벤트 기간이 종료되면 발푸르기스의 밤 인격과 E.G.O가 모든 추출 목록에서 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_extraction_page_04_desc_01].content
   limit: do 130 znaków
   EN: Once the event period is over, Walpurgis Night Identities and E.G.O will no longer be Extractable.
   PL: Po zakończeniu wydarzenia Tożsamości i E.G.O Nocy Walpurgii znikają ze wszystkich list Ekstrakcji.
66. [Samouczek i wskazówki [tutorial_walpurgisnacht_vendingmachine] — tekst] 발푸르기스의 밤
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_vendingmachine].content
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
67. [Samouczek i wskazówki [tutorial_walpurgisnacht_vendingmachine_page_01_desc_01] — tekst] 이벤트 기간 동안 이전 회차까지의 발푸르기스의 밤 인격 및 E.G.O를 자판기에서 구매할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_vendingmachine_page_01_desc_01].content
   limit: do 160 znaków
   EN: During the event period, Identities and E.G.O from all previous Walpurgis Night events are available from the Dispenser.
   PL: W trakcie wydarzenia Tożsamości oraz E.G.O ze wszystkich poprzednich edycji Nocy Walpurgii można kupić w Automacie.
68. [Samouczek i wskazówki [tutorial_walpurgisnacht_vendingmachine_page_02_desc_01] — tekst] 현재 진행 중인 회차의 발푸르기스의 밤 인격과 E.G.O는 자판기에서 구매할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_walpurgisnacht_vendingmachine_page_02_desc_01].content
   limit: do 140 znaków
   EN: Identities and E.G.O from the currently active Walpurgis Night event are not available from the Dispenser.
   PL: Tożsamości oraz E.G.O z aktualnie trwającej edycji Nocy Walpurgii nie są dostępne w Automacie.
69. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_01_title_01] — tekst] 호수의 거울
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_01_title_01].content
   limit: do 120 znaków
   EN: Mirror of the Lake
   PL: Lustro Jeziora
70. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_01_desc_01] — tekst] 시즌 3 거울 던전의 명칭은 호수의 거울로 불립니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_01_desc_01].content
   limit: do 120 znaków
   EN: Season 3's Mirror Dungeon is called 'Mirror of the Lake'.
   PL: Lustrzane Lochy Sezonu 3 noszą nazwę „Lustro Jeziora”.
71. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_01_desc_02] — tekst] 일반 난이도와 어려움 난이도 중 하나를 선택하여 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_01_desc_02].content
   limit: do 120 znaków
   EN: Choose between 'Normal' and 'Hard' difficulties to enter.
   PL: Przed wejściem wybierz poziom trudności: Normalny lub Trudny.
72. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_02_title_01] — tekst] 주간 추가 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_02_title_01].content
   limit: do 120 znaków
   EN: Weekly Bonuses
   PL: Cotygodniowa Premia
73. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_02_desc_01] — tekst] 거울 던전에서는 매주 추가 보상 기회가 제공됩니다. 보상 수령 시점에 추가 보상 기회를 사용하면 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_02_desc_01].content
   limit: do 200 znaków
   EN: Every week, Mirror Dungeons offer Weekly Bonuses. Use Weekly Bonuses when you're claiming the rewards for the run—and receive greatly increased rewards.
   PL: Co tydzień w Lustrzanych Lochach otrzymujesz szanse na Cotygodniową Premię. Wykorzystanie ich przy odbiorze nagród znacznie zwiększa zdobywane łupy.
74. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_02_desc_02] — tekst] 일반 난이도는 매주 3회, 어려움 난이도는 매주 1회의 추가 보상을 받을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_02_desc_02].content
   limit: do 120 znaków
   EN: 'Normal' difficulty offers 3 Weekly Bonuses, and 'Hard' difficulty offers 1 Weekly Bonus.
   PL: Poziom Normalny zapewnia 3 Cotygodniowe Premie tygodniowo, a Trudny — 1 tygodniowo.
75. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_02_desc_03] — tekst] 어려움 난이도를 클리어할 경우, 남은 일반 난이도 추가 보상 기회를 함께 소모하여 대량의 보상의 효율을 극대화할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_02_desc_03].content
   limit: do 250 znaków
   EN: Clearing the 'Hard' Difficulty Mirror Dungeon will allow you to spend the rest of the Normal Difficulty Weekly Bonuses as well, maximizing the amount of rewards you gain from the Mirror Dungeon.
   PL: Ukończenie poziomu Trudnego pozwala zużyć naraz także pozostałe szanse premii z poziomu Normalnego, maksymalizując wydajność nagród.
76. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_title_01] — tekst] 수감자
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_title_01].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
77. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_desc_01] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can view your currently deployed Sinners here.
   PL: Tutaj sprawdzisz bieżące ustawienie Grzeszników.
78. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_title_02] — tekst] 시작 버프
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_title_02].content
   limit: do 120 znaków
   EN: Starter Buffs
   PL: Wzmocnienia startowe
79. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_desc_02] — tekst] 거울 던전 클리어 시 획득하는 별빛을 사용하여 거울 던전 진행에 도움이 되는 다양한 버프를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_desc_02].content
   limit: do 180 znaków
   EN: Collect Starlight from completing Mirror Dungeons and use them to obtain several Starter Buffs that will help you in the Mirror Dungeon.
   PL: Wykorzystaj Gwiezdny Blask zdobywany za kończenie Lustrzanych Lochów, aby odblokować rozmaite wzmocnienia ułatwiające wyprawy.
80. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_title_03] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_title_03].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
81. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_03_desc_03] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다. 거울 던전을 진행하며 E.G.O 기프트를 획득하면 기록집에 해당 E.G.O 기프트의 기록이 추가됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_03_desc_03].content
   limit: do 220 znaków
   EN: You can view the list of E.G.O Gifts that appear in the Mirror Dungeon. Obtaining an E.G.O Gift in the Mirror Dungeon will add an entry to your E.G.O Gift Compendium.
   PL: Tutaj przejrzysz Dary E.G.O występujące w Lustrzanych Lochach. Zdobycie Daru E.G.O podczas wyprawy dodaje jego wpis do Kompendium.
82. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_title_01] — tekst] 시작 버프
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_title_01].content
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
83. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_desc_01] — tekst] 호수의 거울에서는 시작 버프를 많이 활성화할수록, 진행 과정에서 좋은 등급의 E.G.O 기프트를 획득할 기회가 많아집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_desc_01].content
   limit: do 200 znaków
   EN: In Mirror of the Lake, you can increase your chances of obtaining higher Tier E.G.O Gifts during your Mirror Dungeon run by activating more Starter Buffs.
   PL: W Lustrze Jeziora im więcej wzmocnień startowych aktywujesz, tym większa szansa na zdobycie Darów E.G.O wyższej rangi w trakcie wyprawy.
84. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_desc_02] — tekst] 시작 버프는 던전의 난이도 상관없이 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_desc_02].content
   limit: do 120 znaków
   EN: Starter Buffs do not change with the Mirror Dungeon difficulties.
   PL: Wzmocnienia startowe obowiązują niezależnie od wybranego poziomu trudności lochu.
85. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_title_02] — tekst] 별빛
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_title_02].content
   limit: do 120 znaków
   EN: Starlight
   PL: Gwiezdny Blask
86. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_desc_03] — tekst] 별빛은 거울 던전 클리어 시 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_desc_03].content
   limit: do 120 znaków
   EN: You can obtain Starlight from completing Mirror Dungeon runs.
   PL: Gwiezdny Blask zdobywasz za ukończenie Lustrzanych Lochów.
87. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_04_desc_04] — tekst] 높은 층에 오를 수록 더 많은 별빛을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_04_desc_04].content
   limit: do 120 znaków
   EN: The higher you rise through the Mirror Dungeon floors, the more Starlight you will obtain.
   PL: Im wyższe piętro osiągniesz, tym więcej Gwiezdnego Blasku otrzymasz.
88. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_05_title_01] — tekst] 최초 E.G.O 기프트 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_05_title_01].content
   limit: do 120 znaków
   EN: Starting E.G.O Gift Choice
   PL: Wybór początkowego Daru E.G.O
89. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_05_desc_01] — tekst] 거울 던전 입장 시, 총 8개의 E.G.O 기프트 카테고리가 제시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_05_desc_01].content
   limit: do 120 znaków
   EN: Upon Mirror Dungeon entry, you will be given 8 E.G.O Gift categories to choose from.
   PL: Przy wejściu do Lustrzanych Lochów prezentowanych jest łącznie 8 kategorii Darów E.G.O.
90. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_05_desc_02] — tekst] 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_05_desc_02].content
   limit: do 120 znaków
   EN: You can choose as many E.G.O Gifts as it is available to you from the same category.
   PL: Z wybranej kategorii możesz odebrać tyle Darów E.G.O, na ile pozwala twój limit wyboru.
91. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_05_desc_03] — tekst] 거울 던전 전투를 진행하는 과정에서 E.G.O 기프트의 특별한 효과를 통해 도움을 받을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_05_desc_03].content
   limit: do 120 znaków
   EN: E.G.O Gifts provide special effects in the Mirror Dungeon to assist you in your journey.
   PL: Specjalne efekty Darów E.G.O wspomogą twoją drużynę podczas walk w Lustrzanych Lochach.
92. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_05_desc_04] — tekst] 만약 이전 클리어 시 선택하지 않은 E.G.O 기프트 카테고리를 선택하여 거울 던전을 클리어한다면 별빛을 추가로 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_05_desc_04].content
   limit: do 160 znaków
   EN: You can obtain extra Starlight by choosing an E.G.O Gift category that you did not use in your immediately preceding run.
   PL: Ukończenie Lustrzanych Lochów z kategorią Darów E.G.O niewybraną w poprzedniej wyprawie zapewnia dodatkowy Gwiezdny Blask.
93. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_06_title_01] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_06_title_01].content
   limit: do 120 znaków
   EN: Forming the Team
   PL: Wybór Grzeszników
94. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_06_desc_01] — tekst] 거울 던전에 참여할 수감자를 선택하여 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_06_desc_01].content
   limit: do 120 znaków
   EN: Select Sinners who will participate in the Mirror Dungeon run.
   PL: Wybierz i ustaw Grzeszników, którzy wezmą udział w wyprawie do Lustrzanych Lochów.
95. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_06_desc_02] — tekst] 거울 던전 편성 단계에서는 인격의 레벨에 보정치를 반영하여 40으로 적용됩니다. 어려움 난이도에서는 보유한 인격의 레벨이 적용됩니다. (최대 레벨 40)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_06_desc_02].content
   limit: do 210 znaków
   EN: In the Mirror Dungeon deployment stage, all Identity Levels will be fixed to 40. In 'Hard' difficulty, your current Identity levels will be reflected instead.
   PL: Na etapie ustawiania składu poziom Tożsamości jest korygowany do 40. Na poziomie Trudnym obowiązuje aktualny poziom posiadanych Tożsamości (maks. 40).
96. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_06_desc_03] — tekst] 1성, 2성 인격을 편성할 경우, 입장 시 코스트를 추가로 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_06_desc_03].content
   limit: do 120 znaków
   EN: Deploy 1★ or 2★ Identities to gain additional Cost upon entry.
   PL: Wystawienie Tożsamości 1★ lub 2★ zapewnia dodatkowy Koszt na starcie.
97. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_06_desc_04] — tekst] 만약 이전 클리어 과정에서 교체를 포함해 한 번도 선택하지 않은 인격을 편성할 경우, 입장 시 코스트를 추가로 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_06_desc_04].content
   limit: do 150 znaków
   EN: Deploy Identities that have not been used in your immediately preceding Run to gain additional Cost upon entry.
   PL: Wystawienie Tożsamości, które nie były używane w poprzedniej ukończonej wyprawie (wliczając wymiany), zapewnia dodatkowy Koszt na starcie.
98. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_07_title_01] — tekst] 휴식 보너스
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_07_title_01].content
   limit: do 120 znaków
   EN: Rest Bonus
   PL: Premia Odpoczynku
99. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_07_desc_01] — tekst] 거울 던전 클리어 시, 편성한 인격의 휴식 보너스가 전부 소모되고 그 수치의 총합만큼 별빛을 추가로 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_07_desc_01].content
   limit: do 210 znaków
   EN: The deployed Identity's Rest Bonus will be completely exhausted upon clearing the Mirror Dungeon. The more Rest Bonus you exhaust, the more Starlight you will earn.
   PL: Po ukończeniu Lustrzanych Lochów cała Premia Odpoczynku wystawionych Tożsamości zostaje zużyta, a jej suma zapewnia dodatkowy Gwiezdny Blask.
100. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_07_desc_02] — tekst] 단, 게임 진행 과정에서 한 번이라도 교체된 인격은 휴식 보너스가 소모되지 않아 별빛을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_07_desc_02].content
   limit: do 210 znaków
   EN: However, Identities that have been swapped in or out during the Mirror Dungeon run will not spend their Rest Bonuses, and will not provide additional Starlight.
   PL: Tożsamości wymienione choć raz w trakcie wyprawy nie zużywają jednak Premii Odpoczynku i nie dają dodatkowego Gwiezdnego Blasku.
101. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_07_desc_03] — tekst] 휴식 보너스를 소모하였거나 한 번이라도 교체된 인격을 제외한 나머지 모든 인격은 휴식 보너스가 한 칸 증가합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_07_desc_03].content
   limit: do 170 znaków
   EN: Identities that did not spend their Rest Bonuses, and Identities that were not swapped in or out will gain 1 Bar of Rest Bonus.
   PL: Wszystkie pozostałe Tożsamości, które nie zużyły Premii Odpoczynku ani nie były wymieniane, zyskują 1 pasek Premii Odpoczynku.
102. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_08_title_01] — tekst] 거울 던전 입장
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_08_title_01].content
   limit: do 120 znaków
   EN: Entering the Mirror Dungeon
   PL: Wejście do Lustrzanych Lochów
103. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_08_desc_01] — tekst] 인격과 E.G.O 편성을 완료하였다면 확인 버튼을 통해 거울 던전 스테이지로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_08_desc_01].content
   limit: do 120 znaków
   EN: After finishing up the initial Team setup, press 'Confirm' to enter the Mirror Dungeon.
   PL: Po zakończeniu ustawiania Tożsamości i E.G.O naciśnij przycisk potwierdzenia, aby wejść do Lustrzanych Lochów.
104. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_08_desc_02] — tekst] 편성 과정에서 획득하게 된 추가 코스트 수량 합계가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_08_desc_02].content
   limit: do 120 znaków
   EN: This area displays the additional Cost you have gained over the deployment process.
   PL: Tutaj wyświetlana jest łączna suma dodatkowego Kosztu uzyskanego podczas ustawiania składu.
105. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_09_title_01] — tekst] 거울 던전 탐사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_09_title_01].content
   limit: do 120 znaków
   EN: Exploring Mirror Dungeons
   PL: Eksploracja Lustrzanych Lochów
106. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_09_desc_01] — tekst] 거울 던전에 입장하게 되면 방과 경로가 무작위로 생성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_09_desc_01].content
   limit: do 120 znaków
   EN: The Mirror Dungeon rooms and paths are randomly generated.
   PL: Po wejściu do Lustrzanych Lochów komnaty oraz ścieżki generowane są losowo.
107. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_09_desc_02] — tekst] 현재 방에서 연결된 방을 선택해 진행하며, 각 방에선 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_09_desc_02].content
   limit: do 170 znaków
   EN: You proceed by moving to nodes adjacent to your current node. You may find various events or combat encounters in each of the nodes.
   PL: Poruszasz się, wybierając komnaty połączone z bieżącą; w każdej z nich losowo pojawiają się rozmaite walki oraz wydarzenia.
108. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_09_title_02] — tekst] 코스트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_09_title_02].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
109. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_09_desc_03] — tekst] 거울 던전 진행 과정에서 코스트를 획득할 수 있으며, 코스트를 소모하여 상점이나 쉼터의 기능을 이용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_09_desc_03].content
   limit: do 160 znaków
   EN: You will earn 'Cost' as you proceed through the Mirror Dungeon. 'Cost' you earned can be spent at Shops and Rest Stops.
   PL: Podczas wyprawy przez Lustrzane Lochy zdobywasz Koszt, który możesz wydawać na funkcje Sklepów oraz Przystanków Odpoczynku.
110. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_10_title_01] — tekst] E.G.O 기프트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_10_title_01].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
111. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_10_desc_01] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_10_desc_01].content
   limit: do 170 znaków
   EN: Acquired E.G.O Gifts are displayed here. E.G.O Gifts are items that offer powerful effects that last until the end of the Dungeon.
   PL: Tutaj widnieją zdobyte Dary E.G.O — przedmioty zapewniające potężne efekty działające wewnątrz lochu.
112. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_10_title_02] — tekst] 스테이지 유효 속성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_10_title_02].content
   limit: do 120 znaków
   EN: Effective Attacks
   PL: Skuteczne atrybuty etapu
113. [Samouczek i wskazówki [tutorial_mirrordungeon03_page10_desc_02] — tekst] 거울 던전의 전투 방 하단에는 해당 스테이지에서 유효한 속성이 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page10_desc_02].content
   limit: do 160 znaków
   EN: Below the combat Encounter nodes in Mirror Dungeons are types and affinities effective against the enemies in each node.
   PL: Pod węzłami walk w Lustrzanych Lochach wyświetlane są typy ataków i grzechy skuteczne na danym etapie.
114. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_10_title_03] — tekst] 수감자 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_10_title_03].content
   limit: do 120 znaków
   EN: Sinner Status
   PL: Stan Grzeszników
115. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_10_desc_03] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_10_desc_03].content
   limit: do 120 znaków
   EN: The HP, SP, and lost lives of your Sinners will carry over between encounters.
   PL: Przez cały czas trwania wyprawy PŻ, PP oraz stan poległych Grzeszników przechodzą między walkami.
116. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_11_title_01] — tekst] 상점
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_11_title_01].content
   limit: do 120 znaków
   EN: Shops
   PL: Sklep
117. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_11_desc_01] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 아군 회복, 추가 편성, 제시된 인격 강화를 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_11_desc_01].content
   limit: do 190 znaków
   EN: At Shops, you can spend your 'Cost' to purchase E.G.O Gifts, heal allies, deploy/swap out additional Identities or power up selected Identities.
   PL: W Sklepie możesz wydawać Koszt, aby kupować Dary E.G.O, leczyć sojuszników, dobierać skład lub wzmacniać wskazane Tożsamości.
118. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_11_desc_02] — tekst] 사용하지 않는 E.G.O 기프트를 상점에서 판매하여 코스트를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_11_desc_02].content
   limit: do 120 znaków
   EN: At Shops, you can sell E.G.O Gifts you don't use to obtain 'Cost'.
   PL: W Sklepie możesz sprzedawać nieużywane Dary E.G.O, aby zyskać Koszt.
119. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_12_title_01] — tekst] 쉼터
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_12_title_01].content
   limit: do 120 znaków
   EN: Rest Stops
   PL: Przystanek Odpoczynku
120. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_12_desc_01] — tekst] 코스트를 소모하여 아군 회복, 추가 편성, E.G.O 기프트 강화를 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_12_desc_01].content
   limit: do 160 znaków
   EN: At Rest Stops, you can spend your 'Cost' to heal allies, deploy/swap out additional Identities or enhance E.G.O Gifts.
   PL: Na Przystanku Odpoczynku możesz wydać Koszt na leczenie sojuszników, dobór składu oraz ulepszanie Darów E.G.O.
121. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_12_desc_02] — tekst] E.G.O 기프트를 합성하여 다른 E.G.O 기프트를 노려볼 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_12_desc_02].content
   limit: do 120 znaków
   EN: You can Fuse E.G.O Gifts to obtain different E.G.O Gifts.
   PL: Możesz też syntezować Dary E.G.O, aby spróbować zdobyć inny Dar E.G.O.
122. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_13_title_01] — tekst] 층 버프
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_13_title_01].content
   limit: do 120 znaków
   EN: Floor Buffs
   PL: Wzmocnienia piętra
123. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_13_desc_01] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 무작위 적 버프를 획득하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_13_desc_01].content
   limit: do 120 znaków
   EN: Upon clearing a floor, you will obtain random enemy buffs tied to each E.G.O Gifts.
   PL: Po ukończeniu piętra wraz z Darem E.G.O nakładane jest powiązane z nim losowe wzmocnienie wrogów.
124. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_13_desc_02] — tekst] 층을 클리어할 때마다 적 버프는 누적됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_13_desc_02].content
   limit: do 120 znaków
   EN: Enemy Buffs will continue to stack with every floor cleared.
   PL: Wzmocnienia wrogów kumulują się z każdym ukończonym piętrem.
125. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_14_title_01] — tekst] 거울 던전 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_14_title_01].content
   limit: do 120 znaków
   EN: Mirror Dungeon Rewards
   PL: Nagrody Lustrzanych Lochów
126. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_14_desc_01] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_14_desc_01].content
   limit: do 120 znaków
   EN: Upon clearing a Mirror Dungeon run, spend Enkephalin Modules to claim your rewards.
   PL: Po ukończeniu Lustrzanych Lochów wydaj Moduły Enkefaliny, aby odebrać nagrody.
127. [Samouczek i wskazówki [tutorial_mirrordungeon03_page_14_desc_02] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mirrordungeon03_page_14_desc_02].content
   limit: do 160 znaków
   EN: The amount of rewards depends on the number of cleared Floors. You can use Weekly Bonus chances to claim even more rewards.
   PL: Liczba nagród zależy od ukończonych pięter; użyj szans Cotygodniowej Premii, aby zdobyć ich jeszcze więcej.
128. [Samouczek i wskazówki [tutorial_mainui_24_miracle_01_title] — tekst] 20번구의 기적
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_01_title].content
   limit: do 120 znaków
   EN: Miracle in District 20
   PL: Cud w Dystrykcie 20
129. [Samouczek i wskazówki [tutorial_mainui_24_miracle_01_title_01] — tekst] 20번구의 기적 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_01_title_01].content
   limit: do 120 znaków
   EN: Unlock Miracle in District 20
   PL: Odblokowanie Cudu w Dystrykcie 20
130. [Samouczek i wskazówki [tutorial_mainui_24_miracle_01_desc_01] — tekst] [20번구의 기적 이벤트 스테이지]는 주요 이야기의 5-36을 클리어할 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_01_desc_01].content
   limit: do 220 znaków
   EN: The [Miracle in District 20 Event Stages] opens after clearing Stage 5-36 of the Main Story. You may enter the event page via the banner on the Window or the Driverside.
   PL: [Etapy wydarzenia Cud w Dystrykcie 20] odblokowują się po ukończeniu etapu 5-36 Głównej Opowieści. Wejdziesz do nich przez baner wydarzenia w Oknie lub Jeździe.
131. [Samouczek i wskazówki [tutorial_mainui_24_miracle_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_02_title_01].content
   limit: do 120 znaków
   EN: Event Period
   PL: Czas trwania wydarzenia
132. [Samouczek i wskazówki [tutorial_mainui_24_miracle_02_desc_01] — tekst] 20번구의 기적 이벤트 기간이 표시됩니다. 이벤트 기간 동안 20번구의 기적 혹은 주요 이야기의 스테이지와 던전을 클리어하면 [장식 꾸러미]를 획득할 수 있습니다.\n※ 단, 채광에서는 [장식 꾸러미]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_02_desc_01].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of The Miracle in District 20 event is shown here. During the event, you can earn [Trinkets Sack] by clearing Stages and Dungeons in the event and Main Story.\n※ However, [Trinkets Sack] cannot be obtained in Luxcavations.
   PL: Tutaj wyświetlany jest czas trwania wydarzenia Cud w Dystrykcie 20. W trakcie wydarzenia ukończenie etapów lub lochów wydarzenia i Głównej Opowieści zapewnia [Worki Ozdób].\n※ [Worków Ozdób] nie można jednak zdobyć w Lochach Wydobywczych.
133. [Samouczek i wskazówki [tutorial_mainui_24_miracle_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_03_title_01].content
   limit: do 120 znaków
   EN: Event Encounters
   PL: Walki wydarzenia
134. [Samouczek i wskazówki [tutorial_mainui_24_miracle_03_desc_01] — tekst] 20번구의 기적 전투는 스토리 스테이지를 포함하여 총 13개의 스테이지로 구성됩니다.\n20번구의 기적 전투에서는 클리어 보상과 별개로 초회 클리어 보상으로 [장식 꾸러미]를 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_03_desc_01].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Miracle in District 20 consists of 13 stages, including story stages.\nSaid stages also offer batches of [Trinkets Sack] as a first-time Clear bonus.
   PL: Cud w Dystrykcie 20 obejmuje łącznie 13 etapów wraz z etapami fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Worki Ozdób] za pierwsze ukończenie (1 raz).
135. [Samouczek i wskazówki [tutorial_mainui_24_miracle_03_desc_02] — tekst] 20번구의 기적 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [장식 꾸러미]를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_03_desc_02].content
   limit: do 150 znaków
   EN: You can earn considerably more [Trinkets Sack] from the Miracle in District 20 stages compared to Main Story stages.
   PL: Etapy Cudu w Dystrykcie 20 zapewniają znacznie więcej [Worków Ozdób] niż etapy Głównej Opowieści.
136. [Samouczek i wskazówki [tutorial_mainui_24_miracle_04_title_01] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_04_title_01].content
   limit: do 120 znaków
   EN: Event Bonus Units
   PL: Jednostki premiowane w wydarzeniu
137. [Samouczek i wskazówki [tutorial_mainui_24_miracle_04_desc_01] — tekst] 20번구의 기적 이벤트 E.G.O를 편성하여 스테이지, 던전을 클리어하면 [장식 꾸러미]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_04_desc_01].content
   limit: do 180 znaków
   EN: Having E.G.O from the Miracle in District 20 event on your team increases the amount of [Trinkets Sack] earned from stages and dungeons.
   PL: Umieszczenie w drużynie E.G.O z wydarzenia Cud w Dystrykcie 20 zwiększa liczbę [Worków Ozdób] zdobywanych na etapach i w lochach.
138. [Samouczek i wskazówki [tutorial_mainui_24_miracle_05_title_01] — tekst] 선물 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_05_title_01].content
   limit: do 120 znaków
   EN: Gift Exchange
   PL: Wymiana prezentów
139. [Samouczek i wskazówki [tutorial_mainui_24_miracle_05_desc_01] — tekst] 획득한 [장식 꾸러미]의 수에 비례하여 [선물 교환]에서 다양한 보상을 얻을 수 있습니다.\n[장식 꾸러미]는 최대 4천개까지 수집할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_05_desc_01].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can redeem various rewards from the [Gift Exchange] based on the number of [Trinkets Sack] you have.\nYou can collect up to 4,000 [Trinkets Sack].
   PL: W [Wymianie prezentów] odbierzesz rozmaite nagrody proporcjonalnie do liczby zebranych [Worków Ozdób].\nMożesz zebrać maksymalnie 4000 [Worków Ozdób].
140. [Samouczek i wskazówki [tutorial_mainui_24_miracle_06_desc_01] — tekst] [선물 교환] 페이지에서 각종 재화와 이벤트 배포 E.G.O를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_06_desc_01].content
   limit: do 140 znaków
   EN: You can acquire event reward Identities and E.G.O, as well as various currencies from the [Gift Exchange].
   PL: Na stronie [Wymiany prezentów] zdobędziesz różnorodne waluty oraz darmowe E.G.O wydarzenia.
141. [Samouczek i wskazówki [tutorial_mainui_24_miracle_06_desc_02] — tekst] [선물 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_06_desc_02].content
   limit: do 120 znaków
   EN: The [Gift Exchange]'s open duration is shown here.
   PL: Tutaj widnieje okres odbioru nagród na stronie [Wymiany prezentów].
142. [Samouczek i wskazówki [tutorial_mainui_24_miracle_07_title_01] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_07_title_01].content
   limit: do 120 znaków
   EN: Event Stages
   PL: Etapy wydarzenia
143. [Samouczek i wskazówki [tutorial_mainui_24_miracle_07_desc_01] — tekst] 20번구의 기적에서는 던전이 등장하지 않으며, 다른 스테이지보다 더 많은 장식 꾸러미를 얻을 수 있는 특수 스테이지가 등장합니다. 특수 스테이지는 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_07_desc_01].content
   limit: do 240 znaków
   EN: Miracle in District 20 does not feature a dungeon; instead, there's a special stage where you can earn larger amounts of Trinkets Sack. The special stage consumes Enkephalin Modules.
   PL: W Cudzie w Dystrykcie 20 nie ma lochu — zamiast tego dostępny jest etap specjalny zapewniający więcej Worków Ozdób niż pozostałe etapy. Wejście zużywa Moduły Enkefaliny.
144. [Samouczek i wskazówki [tutorial_mainui_24_miracle_08_title_01] — tekst] 장식 꾸러미
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_08_title_01].content
   limit: do 120 znaków
   EN: Trinkets Sack
   PL: Worek Ozdób
145. [Samouczek i wskazówki [tutorial_mainui_24_miracle_08_desc_01] — tekst] 전투에서 승리할 경우, 낮은 확률로 거대한 장식 꾸러미를 획득할 수 있습니다. 획득한 거대한 장식 꾸러미는 장식 꾸러미 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_08_desc_01].content
   limit: do 200 znaków
   EN: There is a small chance to obtain a Huge Trinkets Sack upon clearing an Encounter. Huge Trinkets Sacks are automatically converted to 20 Trinkets Sacks.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie Wielkiego Worka Ozdób. Zdobyty Wielki Worek Ozdób jest automatycznie zamieniany na 20 Worków Ozdób.
146. [Samouczek i wskazówki [tutorial_mainui_24_miracle_09_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 20번구의 기적 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_24_miracle_09_desc_01].content
   limit: do 260 znaków
   EN: Even after the event fully ends, you will be able to experience the Miracle in District 20 combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Cudu w Dystrykcie 20 możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
147. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_01_title] — tekst] 제2회 발푸르기스의 밤 - 녹빛 여명의 시련
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_01_title].content
   limit: do 120 znaków
   EN: The 2nd Walpurgis Night - The Dawn of Green
   PL: 2. Noc Walpurgii — Próba Zielonego Świtu
148. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_01_title_01] — tekst] 제2회 발푸르기스의 밤 - 녹빛 여명의 시련 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_01_title_01].content
   limit: do 120 znaków
   EN: Unlocking The 2nd Walpurgis Night - The Dawn of Green
   PL: Odblokowanie 2. Nocy Walpurgii — Próby Zielonego Świtu
149. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_01_desc_01] — tekst] [제2회 발푸르기스의 밤 - 녹빛 여명의 시련]은 주요 이야기의 진행도에 관계 없이 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_01_desc_01].content
   limit: do 220 znaków
   EN: [The 2nd Walpurgis Night - The Dawn of Green] unlocks regardless of your progress in the Main Story. Enter via the event banner on the Window or the Driverside tabs.
   PL: [2. Noc Walpurgii — Próba Zielonego Świtu] odblokowuje się niezależnie od postępów w Głównej Opowieści. Wejdziesz do niej przez baner w Oknie lub Jeździe.
150. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_02_title_01].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_02_desc_01] — tekst] 제2회 발푸르기스의 밤 - 녹빛 여명의 시련 이벤트 기간이 표시됩니다. 이벤트 기간 동안 녹빛 여명의 시련 일반 난이도, 어려움 난이도의 전투를 진행하여 미션을 수행하고, 완료한 미션의 보상을 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_02_desc_01].content
   limit: do 260 znaków
   EN: The duration of The 2nd Walpurgis Night - The Dawn of Green event is shown here. During the event, complete Missions for Normal and Hard difficulty Dawn of Green Ordeal Encounters and claim their rewards.
   PL: Wyświetlany jest czas trwania wydarzenia 2. Noc Walpurgii — Próba Zielonego Świtu. W tym okresie rozgrywaj walki Próby Zielonego Świtu na poziomie Normalnym i Trudnym, wykonuj misje i odbieraj nagrody.
152. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_03_title_01] — tekst] 일반 난이도 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_03_title_01].content
   limit: do 120 znaków
   EN: Normal Difficulty Encounter
   PL: Walka na poziomie Normalnym
153. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_03_desc_01] — tekst] 문을 눌러 녹빛 여명의 시련 전투 일반 난이도에 입장할 수 있습니다. 녹빛 여명의 시련 전투는 전투 종료 시 엔케팔린 모듈을 소모합니다. 일반 난이도 전투는 인격의 레벨이 40레벨보다 낮은 경우, 40레벨로 상승합니다. 인격의 동기화 단계, E.G.O의 환상 해석 단계는 현재 육성 상태를 반영합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_03_desc_01].content
   limit: do 410 znaków
   EN: Select the door to begin the Normal difficulty Dawn of Green Ordeal. Dawn of Green Ordeal consumes an Enkephalin Module upon completion. In Normal difficulty, any deployed Identities under Level 40 will be raised to Level 40. However, your Identities' current Uptie Tiers and E.G.O Threadspinning Tiers will be reflected.
   PL: Kliknij drzwi, aby rozpocząć walkę Próby Zielonego Świtu na poziomie Normalnym. Walka zużywa Moduł Enkefaliny po zakończeniu. Na poziomie Normalnym Tożsamości poniżej 40. poziomu zostają podniesione do poziomu 40, natomiast stopień Synchronizacji Tożsamości i Splotu Nici E.G.O odpowiadają twojemu aktualnemu rozwojowi.
154. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_03_title_02] — tekst] 어려움 난이도 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_03_title_02].content
   limit: do 120 znaków
   EN: Hard Difficulty Encounter
   PL: Walka na poziomie Trudnym
155. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_03_desc_02] — tekst] 녹빛 여명의 시련 전투 일반 난이도를 클리어하면 어려움 난이도가 개방됩니다. 어려움 난이도 전투는 인격의 레벨, 인격의 동기화 단계, E.G.O의 환상해석 단계가 현재 육성 상태로 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_03_desc_02].content
   limit: do 250 znaków
   EN: Clearing the Normal difficulty Dawn of Green Ordeal unlocks the Hard difficulty. In Hard difficulty, your Identities' current Levels, Uptie Tiers, and E.G.O Threadspinning Tiers will be reflected.
   PL: Ukończenie Próby Zielonego Świtu na poziomie Normalnym odblokowuje poziom Trudny. Na poziomie Trudnym poziomy Tożsamości, stopnie Synchronizacji oraz stopnie Splotu Nici E.G.O odpowiadają aktualnemu rozwojowi.
156. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_04_title_01] — tekst] 특별 아나운서
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_04_title_01].content
   limit: do 120 znaków
   EN: Special Announcer
   PL: Specjalny Komentator
157. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_04_desc_01] — tekst] 녹빛 여명의 시련 전투에서는 특별한 아나운서를 고정으로 사용합니다. 그렇기 때문에 이번 이벤트 전투에서는 아나운서를 교체할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_04_desc_01].content
   limit: do 200 znaków
   EN: There will be a special, fixed Announcer for the Dawn of Green Ordeal Encounter. Therefore, you cannot select your own Announcers for this event Encounter.
   PL: W walce Próby Zielonego Świtu używany jest na stałe specjalny Komentator, dlatego w tej walce wydarzenia nie można zmienić Komentatora.
158. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_04_title_02] — tekst] 지휘팀 팀장 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_04_title_02].content
   limit: do 120 znaków
   EN: Control Team Captain Effects
   PL: Efekty Kapitana Zespołu Dowodzenia
159. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_04_desc_02] — tekst] 전투 편성에서 1번으로 선택한 수감자에게 ‘지휘팀 팀장’ 효과가 부여됩니다. ‘지휘팀 팀장’ 효과를 받은 수감자는 녹빛 여명의 시련 전투에서 행동 수가 증가하고, 스킬 수량이 변경되며, 이로운 효과를 얻습니다
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_04_desc_02].content
   limit: do 320 znaków
   EN: The #1 Sinner to be deployed in the Teams menu will be imbued with the 'Control Team Captain' effect. The Sinner with the 'Control Team Captain' effect will gain more Slots, their Skill composition will change, and will gain more beneficial effects.
   PL: Grzesznik wybrany jako nr 1 w ustawieniu drużyny otrzymuje efekt „Kapitana Zespołu Dowodzenia”. W walce Próby Zielonego Świtu zyskuje on dodatkowe sloty akcji, zmienioną pulę umiejętności oraz korzystne wzmocnienia.
160. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_05_title_01] — tekst] 미션 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_05_title_01].content
   limit: do 120 znaków
   EN: Missions
   PL: Lista misji
161. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_05_desc_01] — tekst] 전투 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [미션 목록] 페이지로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_05_desc_01].content
   limit: do 170 znaków
   EN: You can enter the [Missions] page, where you can view the list of Missions to be completed during the Encounter and their rewards.
   PL: Przejdź na stronę [Listy misji], aby sprawdzić misje możliwe do wykonania w walce oraz przypisane do nich nagrody.
162. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_06_desc_01] — tekst] [미션 목록] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_06_desc_01].content
   limit: do 120 znaków
   EN: You can view the Reward Exchange period in the [Missions] page.
   PL: Na stronie [Listy misji] wyświetlany jest okres odbioru nagród.
163. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_06_desc_02] — tekst] 일반 난이도 전투와 어려움 난이도 전투의 미션을 각각 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_06_desc_02].content
   limit: do 120 znaków
   EN: Normal difficulty and Hard difficulty each has different sets of Missions to complete.
   PL: Możesz osobno sprawdzić misje dla walk na poziomie Normalnym i Trudnym.
164. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_06_desc_03] — tekst] 미션을 완료하면 [미션 목록]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_06_desc_03].content
   limit: do 120 znaków
   EN: Complete these Missions and claim various rewards from the [Missions] page.
   PL: Ukończ misje, aby odebrać rozmaite nagrody z [Listy misji].
165. [Samouczek i wskazówki [tutorial_mainui_25_walpu2_07_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 ‘제2회 발푸르기스의 밤 - 녹빛 여명의 시련 전투’를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_25_walpu2_07_desc_01].content
   limit: do 270 znaków
   EN: Even after the event fully ends, you will be able to experience the 'The 2nd Walpurgis Night - The Dawn of Green' combat Encounters and view its story anytime at the Driverside and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę „2. Nocy Walpurgii — Próby Zielonego Świtu” możesz w każdej chwili odtworzyć w menu Jazda oraz Teatr — [Opowieści Poboczne].
166. [Samouczek i wskazówki [tutorial_mainui_railway3_title_01] — tekst] 거울굴절철도 3호선
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_title_01].content
   limit: do 120 znaków
   EN: Refraction Railway Line 3
   PL: Kolej Załamania — Linia 3
167. [Samouczek i wskazówki [tutorial_mainui_railway3_page_01_title_01] — tekst] 입장 방법
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_01_title_01].content
   limit: do 120 znaków
   EN: How to Enter
   PL: Sposób wejścia
168. [Samouczek i wskazówki [tutorial_mainui_railway3_page_01_desc_01] — tekst] 활성화된 노선을 선택하여 입장합니다. 거울굴절철도 입장 시에는 재화를 소모하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_01_desc_01].content
   limit: do 140 znaków
   EN: Select the activated Line to enter. Entering the Refraction Railway does not cost any currency or resources.
   PL: Wybierz aktywną linię, aby wejść. Wejście do Kolei Załamania nie zużywa żadnych walut ani zasobów.
169. [Samouczek i wskazówki [tutorial_mainui_railway3_page_02_title_01] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_02_title_01].content
   limit: do 120 znaków
   EN: Creating your Team
   PL: Skład drużyny
170. [Samouczek i wskazówki [tutorial_mainui_railway3_page_02_desc_01] — tekst] 입장 시, 보유한 인격과 E.G.O를 선택하여 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_02_desc_01].content
   limit: do 120 znaków
   EN: You will choose a number of Identities and E.G.O to begin the expedition with.
   PL: Przy wejściu wybierz posiadane Tożsamości oraz E.G.O, aby uformować skład.
171. [Samouczek i wskazówki [tutorial_mainui_railway3_page_03_title_01] — tekst] 3호선 역
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_03_title_01].content
   limit: do 120 znaków
   EN: Line 3 Stations
   PL: Stacje Linii 3
172. [Samouczek i wskazówki [tutorial_mainui_railway3_page_03_desc_01] — tekst] 거울굴절철도 3호선은 총 13개의 역으로 구성되며, 그 중 10개의 역에서 전투를 진행합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_03_desc_01].content
   limit: do 140 znaków
   EN: There are a total of 13 Stations in Refraction Railway Line 3. 10 of those Stations are combat Encounters.
   PL: Kolej Załamania — Linia 3 składa się łącznie z 13 stacji, z czego na 10 stacjach toczą się walki.
173. [Samouczek i wskazówki [tutorial_mainui_railway3_page_03_desc_02] — tekst] 전투를 진행하지 않는 제 4역, 제 8역, 제 12역에서는 인격을 회복 또는 부활시키고 편성을 교체할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_03_desc_02].content
   limit: do 140 znaków
   EN: Station #4, #8, and #12 are not combat Encounters. There, you can heal, revive, or change your Team Loadout.
   PL: Stacje 4, 8 i 12 to stacje bez walk — możesz tam uleczyć lub wskrzesić Tożsamości oraz zmienić skład drużyny.
174. [Samouczek i wskazówki [tutorial_mainui_railway3_page_04_desc_01] — tekst] 역을 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_04_desc_01].content
   limit: do 120 znaków
   EN: Select the Station to enter.
   PL: Wybierz stację, aby wejść.
175. [Samouczek i wskazówki [tutorial_mainui_railway3_page_04_desc_02] — tekst] 해당 역 클리어 시 분실물보관소를 통해 얻을 수 있는 보상이 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_04_desc_02].content
   limit: do 140 znaków
   EN: Below each Station, you can view the rewards for clearing that Station. Claim them at the Lost & Found.
   PL: Poniżej widnieją nagrody za ukończenie danej stacji, które odbierzesz w Biurze Rzeczy Znalezionych.
176. [Samouczek i wskazówki [tutorial_mainui_railway3_page_05_title_01] — tekst] 전투 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_05_title_01].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Samouczek i wskazówki [tutorial_mainui_railway3_page_05_desc_01] — tekst] 전투는 최대 6인까지 편성할 수 있습니다. 단, 6인 미만의 인격이 입장하였을 때 턴이 진행되어도 슬롯 수가 증가하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_05_desc_01].content
   limit: do 240 znaków
   EN: You can select up to 6 participants for an encounter. While you can select less than 6 combat participants, no additional Skill slots will be given for them throughout the encounter.
   PL: Do walki możesz wystawić maksymalnie 6 uczestników. Jeśli wejdzie mniej niż 6 Tożsamości, liczba slotów umiejętności nie zwiększy się wraz z kolejnymi turami.
178. [Samouczek i wskazówki [tutorial_mainui_railway3_page_06_title_01] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_06_title_01].content
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Samouczek i wskazówki [tutorial_mainui_railway3_page_06_desc_01] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_06_desc_01].content
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Samouczek i wskazówki [tutorial_mainui_railway3_page_07_title_01] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_07_title_01].content
   limit: do 120 znaków
   EN: Observation Logs
   PL: Kompendium
181. [Samouczek i wskazówki [tutorial_mainui_railway3_page_07_desc_01] — tekst] 스토리 던전 전투를 통해 관찰 단계가 활성화된 환상체를 조우할 경우, 그 내용이 환상체 도감에 반영되어 확인할 수 있게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_07_desc_01].content
   limit: do 310 znaków
   EN: If you have already unlocked the Abnormalities' Observation Levels through the Story Dungeon Encounters, their Observation Levels will be reflected in the Refraction Railway and you can view their information as you would in those Dungeons.
   PL: Jeśli napotkasz Anomalie, których Poziomy Obserwacji odblokowano już podczas walk w Lochach Fabularnych, zostaną one odzwierciedlone w Kompendium Anomalii w Kolei Załamania.
182. [Samouczek i wskazówki [tutorial_mainui_railway3_page_07_desc_02] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_07_desc_02].content
   limit: do 130 znaków
   EN: However, the damage bonus based on Observation Levels do not apply in the Refraction Railway.
   PL: Premia do obrażeń wynikająca z Poziomu Obserwacji nie jest jednak aktywna.
183. [Samouczek i wskazówki [tutorial_mainui_railway3_page_07_desc_03] — tekst] 거울굴절철도 3호선에서는 전투 중 포기를 선택하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_07_desc_03].content
   limit: do 140 znaków
   EN: In Refraction Railway Line 3, the updated Observation Level will be saved even if you give up mid-Encounter.
   PL: W Kolei Załamania — Linii 3 zaktualizowane wpisy Kompendium zostają zapisane nawet wtedy, gdy poddasz walkę w jej trakcie.
184. [Samouczek i wskazówki [tutorial_mainui_railway3_page_08_desc_01] — tekst] 전투 이후 남은 E.G.O 자원은 다음 역에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_08_desc_01].content
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Samouczek i wskazówki [tutorial_mainui_railway3_page_08_desc_02] — tekst] 해당 역을 클리어하는 데 걸린 클리어 턴과 시착역으로부터 해당 역까지를 클리어하기까지 걸린 누적 턴이 역 상단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_08_desc_02].content
   limit: do 150 znaków
   EN: Total Turns taken to clear the Station and Total Turns taken since the First Stop will be shown above each Station.
   PL: Nad stacją wyświetlana jest liczba tur ukończenia danej stacji oraz łączna liczba tur od Stacji początkowej do tej stacji.
186. [Samouczek i wskazówki [tutorial_mainui_railway3_page_08_desc_03] — tekst] 편성한 인격의 체력, 정신력, 사망 상태가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_08_desc_03].content
   (powtórzenie elementu 9 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Samouczek i wskazówki [tutorial_mainui_railway3_page_09_desc_01] — tekst] 전투 패배 시, 해당 역을 입장하기 직전 상태로 되돌아가거나 남은 인격으로 이어서 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_09_desc_01].content
   limit: do 180 znaków
   EN: Upon defeat, you can either return to the state immediately before entering that Station or continue using your surviving Identities.
   PL: W razie porażki w walce możesz wrócić do stanu tuż przed wejściem na stację lub kontynuować ocalałymi Tożsamościami.
188. [Samouczek i wskazówki [tutorial_mainui_railway3_page_09_desc_02] — tekst] 이어서 진행할 경우 등장하는 적의 체력이 유지되며, 남은 체력 비율이 역 위쪽에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_09_desc_02].content
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Samouczek i wskazówki [tutorial_mainui_railway3_page_10_desc_01] — tekst] 초기화 버튼을 통해 해당 역 입장 직전 상태로 되돌아갈 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_10_desc_01].content
   limit: do 120 znaków
   EN: Select the Reset button to return to the state immediately before entering that Station.
   PL: Użyj przycisku resetu, aby wrócić do stanu tuż przed wejściem na daną stację.
190. [Samouczek i wskazówki [tutorial_mainui_railway3_page_11_title_01] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_11_title_01].content
   limit: do 120 znaków
   EN: Breaking Records
   PL: Bicie rekordów
191. [Samouczek i wskazówki [tutorial_mainui_railway3_page_11_desc_01] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다. 특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_11_desc_01].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During an expedition, you can choose to start over from previously cleared Stations.\nWhen you do so, the battle will start with the Sinners’ statuses and E.G.O resources reverted to that point, and any progress you've made since that Station will be reset.
   PL: W trakcie wyprawy możesz rozpocząć grę od nowa od dowolnego ukończonego wcześniej etapu.\nWalka rozpocznie się wówczas ze stanem Tożsamości i zasobami E.G.O z momentu wejścia na ten etap, a postępy z późniejszych etapów zostaną zresetowane.
192. [Samouczek i wskazówki [tutorial_mainui_railway3_page_12_title_01] — tekst] 휴게역
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_12_title_01].content
   limit: do 120 znaków
   EN: Rest Station
   PL: Stacja postojowa
193. [Samouczek i wskazówki [tutorial_mainui_railway3_page_12_desc_01] — tekst] 제 4역, 제 8역, 제 12역은 휴게역으로, 도착 시 모든 아군의 체력이 회복되며, 사망한 인격이 부활합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_12_desc_01].content
   limit: do 160 znaków
   EN: Station #4, #8, and #12 are Rest Stations. Reaching those Stations will fully heal all allies and revive dead Identities.
   PL: Stacje 4, 8 i 12 to stacje postojowe — po dotarciu na nie wszyscy sojusznicy odzyskują pełne PŻ, a poległe Tożsamości zostają wskrzeszone.
194. [Samouczek i wskazówki [tutorial_mainui_railway3_page_12_desc_02] — tekst] 인격의 정신력이 0 이상인 경우에는 그대로 유지되며, 정신력이 0 미만인 경우에는 0으로 회복합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_12_desc_02].content
   limit: do 150 znaków
   EN: Identities with 0 or positive SP will maintain their SP, but Identities with negative SP will recover to 0 SP.
   PL: Tożsamości mające 0 lub więcej PP zachowują swoje PP, natomiast u Tożsamości z ujemnymi PP wartość ta wraca do 0.
195. [Samouczek i wskazówki [tutorial_mainui_railway3_page_12_desc_03] — tekst] 또한 휴게역에서는 편성을 교체할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_12_desc_03].content
   limit: do 120 znaków
   EN: You can also change your Team Loadout in Rest Stations.
   PL: Na stacji postojowej możesz również zmienić skład drużyny.
196. [Samouczek i wskazówki [tutorial_mainui_railway3_page_13_desc_01] — tekst] 종착역에 입장하면 더이상 이전 역으로 되돌아갈 수 없기 때문에 신중한 선택이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_13_desc_01].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Samouczek i wskazówki [tutorial_mainui_railway3_page_13_desc_02] — tekst] 종착역을 클리어하는 것이 거울굴절철도 3호선의 최종 목표입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_13_desc_02].content
   limit: do 120 znaków
   EN: Clearing the Terminus is the ultimate objective of Refraction Railway Line 3.
   PL: Ukończenie Stacji końcowej to ostateczny cel Kolei Załamania — Linii 3.
198. [Samouczek i wskazówki [tutorial_mainui_railway3_page_14_title_01] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_14_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Samouczek i wskazówki [tutorial_mainui_railway3_page_14_desc_01] — tekst] 거울굴절철도 3호선 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_14_desc_01].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 3 banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 3.
200. [Samouczek i wskazówki [tutorial_mainui_railway3_page_14_desc_02] — tekst] 획득 조건이 어려울수록 더욱 특별한 배너를 얻게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_14_desc_02].content
   limit: do 120 znaków
   EN: You can acquire more lavishly ornamented banners as you meet more difficult conditions.
   PL: Im trudniejszy warunek zdobycia, tym bardziej wyjątkowy baner otrzymasz.
201. [Samouczek i wskazówki [tutorial_mainui_railway3_page_14_desc_03] — tekst] 배너를 획득하면 제일 좋은 기록의 누적 턴 수가 배너에 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_14_desc_03].content
   limit: do 130 znaków
   EN: Upon acquisition of these banners, the Total Turns of your best record will be displayed on them.
   PL: Po zdobyciu baneru widnieje na nim łączna liczba tur z twojego najlepszego rekordu.
202. [Samouczek i wskazówki [tutorial_mainui_railway3_page_15_title_01] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_15_title_01].content
   limit: do 120 znaków
   EN: The Lost & Found
   PL: Biuro Rzeczy Znalezionych
203. [Samouczek i wskazówki [tutorial_mainui_railway3_page_15_desc_01] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_15_desc_01].content
   limit: do 140 znaków
   EN: After clearing a Station in the Line for the first time, the rewards will be sent to the Lost & Found.
   PL: Po pierwszym ukończeniu etapu jego nagrody trafiają do Biura Rzeczy Znalezionych i zostają aktywowane.
204. [Samouczek i wskazówki [tutorial_mainui_railway3_page_15_desc_02] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다. 이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_15_desc_02].content
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Samouczek i wskazówki [tutorial_mainui_railway3_page_16_title_01] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_16_title_01].content
   limit: do 120 znaków
   EN: Travel Collection
   PL: Historia rekordów
206. [Samouczek i wskazówki [tutorial_mainui_railway3_page_16_desc_01] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_16_desc_01].content
   limit: do 150 znaków
   EN: Upon clearing the final Station, your Refraction Railway play record will be saved. Up to 20 records can be viewed.
   PL: Po ukończeniu finałowego etapu zapisywany jest rekord przejścia Kolei Załamania; możesz przeglądać maksymalnie 20 rekordów.
207. [Samouczek i wskazówki [tutorial_mainui_railway3_page_16_desc_02] — tekst] 기록이 20개를 넘어갈 경우에는 누적 턴 수가 많은 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway3_page_16_desc_02].content
   limit: do 130 znaków
   EN: If you have more than 20 records, records with the highest Total Turns will be deleted first.
   PL: Po przekroczeniu 20 rekordów w pierwszej kolejności usuwane są zapisy z największą łączną liczbą tur.
208. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_01_title] — tekst] 육참골단
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_01_title].content
   limit: do 120 znaków
   EN: Yield My Flesh to Claim Their Bones
   PL: Oddam Ciało, by Złamać Ich Kości
209. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_01_title_01] — tekst] 육참골단 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_01_title_01].content
   limit: do 120 znaków
   EN: Unlocking Yield My Flesh to Claim Their Bones
   PL: Odblokowanie: Oddam Ciało, by Złamać Ich Kości
210. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_01_desc_01] — tekst] [육참골단 이벤트 페이지]는 주요 이야기의 5.5-12를 클리어한 경우 개방됩니다.\n\n유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_01_desc_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The [Yield My Flesh to Claim Their Bones Event Page] opens after clearing Stage 5.5-12 of the Main Story.\n\nYou may enter the event page via the banner on the Window or the Driverside.
   PL: [Strona wydarzenia Oddam Ciało, by Złamać Ich Kości] odblokowuje się po ukończeniu etapu 5.5-12 Głównej Opowieści.\n\nWejdziesz na nią przez baner wydarzenia w Oknie lub Jeździe.
211. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_02_title_01].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_02_desc_01] — tekst] 육참골단 이벤트 기간이 표시됩니다.\n\n이벤트 스테이지와 던전을 클리어할 때마다 [피에 절은 검집]을 획득할 수 있습니다. 이외에도 주요 이야기 스테이지와 던전을 최초로 클리어하거나 거울 던전 클리어 시, [피에 절은 검집]을 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [피에 절은 검집]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_02_desc_01].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Yield My Flesh to Claim Their Bones event is shown here.\n\nDuring the event, you can earn [Bloodied Scabbard] by clearing Event Stages and Event Dungeons. You can also earn [Bloodied Scabbard] by clearing the Mirror Dungeons or clearing Main Story Stages or Dungeons for the first time.\n\n※ However, [Bloodied Scabbard] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Oddam Ciało, by Złamać Ich Kości.\n\nZa każde ukończenie etapów i lochu wydarzenia otrzymasz [Zakrwawione Pochwy]. Zdobędziesz je także za pierwsze ukończenie etapów i lochów Głównej Opowieści oraz za przejście Lustrzanych Lochów.\n\n※ [Zakrwawionych Pochew] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
213. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_03_title_01].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_03_desc_01] — tekst] 육참골단 전투는 스토리 스테이지를 포함하여 총 12개의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_03_desc_01].content
   limit: do 130 znaków
   EN: Including Story Stages, the Yield My Flesh to Claim Their Bones event is composed of 12 Stages.
   PL: Walki wydarzenia Oddam Ciało, by Złamać Ich Kości obejmują łącznie 12 etapów wraz z etapami fabularnymi.
215. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_03_desc_02] — tekst] 육참골단 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [피에 절은 검집]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_03_desc_02].content
   limit: do 170 znaków
   EN: You can earn considerably more [Bloodied Scabbard] from Yield My Flesh to Claim Their Bones Stages compared to Main Story Stages.
   PL: Etapy wydarzenia Oddam Ciało, by Złamać Ich Kości zapewniają znacznie więcej [Zakrwawionych Pochew] niż etapy Głównej Opowieści.
216. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_04_title_01] — tekst] 이벤트 보너스 캐릭터
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_04_title_01].content
   limit: do 120 znaków
   EN: Event Bonus Identities
   PL: Premiowane postacie wydarzenia
217. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_04_desc_01] — tekst] 육참골단 기간 동안 이벤트 인격을 편성하여 스테이지 또는 던전을 클리어하면 [피에 절은 검집]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_04_desc_01].content
   limit: do 210 znaków
   EN: Having Event Identities from the Yield My Flesh to Claim Their Bones event on your team increases the amount of [Bloodied Scabbard] earned from Stages and Dungeons.
   PL: Umieszczenie w drużynie Tożsamości z wydarzenia Oddam Ciało, by Złamać Ich Kości zwiększa liczbę [Zakrwawionych Pochew] zdobywanych na etapach i w lochach.
218. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_05_title_01] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_05_title_01].content
   limit: do 120 znaków
   EN: Reward Exchange
   PL: Wymiana nagród
219. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_05_desc_01] — tekst] [보상 교환] 창에서 [피에 절은 검집]을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_05_desc_01].content
   limit: do 150 znaków
   EN: At the Reward Exchange window, you can submit [Bloodied Scabbard] you've collected to purchase various rewards.
   PL: W oknie [Wymiany nagród] wymienisz zebrane [Zakrwawione Pochwy] na rozmaite nagrody.
220. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_06_desc_01] — tekst] 보상을 수령할 수 있는 기간이 다음과 같이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_06_desc_01].content
   limit: do 120 znaków
   EN: The duration to claim the rewards is shown here.
   PL: Tutaj wyświetlany jest okres odbioru nagród.
221. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_06_desc_02] — tekst] 이곳에서는 각종 재화와 이벤트 배포 인격을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_06_desc_02].content
   limit: do 120 znaków
   EN: Here, you can obtain various currencies and the Event Identity.
   PL: Zdobędziesz tu rozmaite waluty oraz darmową Tożsamość wydarzenia.
222. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_07_title_01] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_07_title_01].content
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_07_desc_01] — tekst] 육참골단 마지막 전투는 거울 던전 방식으로 진행됩니다.\n\n입장 시, 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_07_desc_01].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The final battle of Yield My Flesh to Claim Their Bones is like a Mirror Dungeon.\n\nEntering the Dungeon costs Enkephalin Modules.
   PL: Ostatnia walka wydarzenia Oddam Ciało, by Złamać Ich Kości przebiega na zasadach Lustrzanych Lochów.\n\nWejście zużywa Moduły Enkefaliny.
224. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_08_title_01] — tekst] 한 서린 검집
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_08_title_01].content
   limit: do 120 znaków
   EN: Resentful Scabbard
   PL: Przepełniona Żalem Pochwa
225. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_08_desc_01] — tekst] 전투에서 승리할 경우, 낮은 확률로 [한 서린 검집]을 획득할 수 있습니다.\n\n[한 서린 검집]은 획득 시, 피에 절은 검집 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_08_desc_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rarely, you may obtain [Resentful Scabbard] from clearing Encounters.\n\n[Resentful Scabbard] is automatically converted to 20 [Bloodied Scabbard] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Przepełnionej Żalem Pochwy].\n\nZdobyta [Przepełniona Żalem Pochwa] jest automatycznie zamieniana na 20 [Zakrwawionych Pochew].
226. [Samouczek i wskazówki [tutorial_mainui_26_ycgd_09_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 육참골단 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_26_ycgd_09_desc_01].content
   limit: do 270 znaków
   EN: Even after the event fully ends, you will be able to experience the Yield My Flesh to Claim Their Bones combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę „Oddam Ciało, by Złamać Ich Kości” możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
227. [Samouczek i wskazówki [tutorial_mainui_28_tkt_01_title] — tekst] 시간살인시간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_01_title].content
   limit: do 120 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
228. [Samouczek i wskazówki [tutorial_mainui_28_tkt_01_title_01] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_01_title_01].content
   limit: do 120 znaków
   EN: Accessing the Event
   PL: Odblokowanie wydarzenia
229. [Samouczek i wskazówki [tutorial_mainui_28_tkt_01_desc_01] — tekst] [시간살인시간 이벤트 창]은 주요 이야기의 6-48을 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_01_desc_01].content
   limit: do 210 znaków
   EN: The [Timekilling Time Event Page] opens after clearing Stage 6-48 of the Main Story.You may enter the event page via the banner on the Window or the Driverside.
   PL: [Okno wydarzenia Czas Zabijania Czasu] odblokowuje się po ukończeniu etapu 6-48 Głównej Opowieści. Wejdziesz do niego przez baner wydarzenia w Oknie lub Jeździe.
230. [Samouczek i wskazówki [tutorial_mainui_28_tkt_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_02_title_01].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Samouczek i wskazówki [tutorial_mainui_28_tkt_02_desc_01] — tekst] 시간살인시간 이벤트 기간이 표시됩니다.\n이벤트 기간 동안 시간살인시간 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [회중시계]를 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [회중시계]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_02_desc_01].content
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Timekilling Time event is shown here.\n\nDuring the event, you can earn [Pocket Watch] by clearing Event Stages. You can also earn [Pocket Watch] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Pocket Watch] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Czas Zabijania Czasu.\nW trakcie wydarzenia ukończenie etapów Czasu Zabijania Czasu, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Zegarki Kieszonkowe].\n\n※ [Zegarków Kieszonkowych] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
232. [Samouczek i wskazówki [tutorial_mainui_28_tkt_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_03_title_01].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Samouczek i wskazówki [tutorial_mainui_28_tkt_03_desc_01] — tekst] 시간살인시간 이벤트는 스토리 스테이지를 포함하여 총 14개의 스테이지와 1개의 던전으로 구성됩니다.\n\n이벤트 전투에서는 클리어 보상과 별개로 초회 보상을 통해 매우 많은 [회중시계]를 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_03_desc_01].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Timekilling Time consists of 14 stages, including story stages, and a single dungeon.\n\nEvent Encounters also offer batches of [Pocket Watch] as a first-time Clear bonus.
   PL: Wydarzenie Czas Zabijania Czasu obejmuje łącznie 14 etapów (wraz z fabularnymi) oraz 1 loch.\n\nWalki wydarzenia zapewniają bardzo dużo [Zegarków Kieszonkowych] jako nagrodę za pierwsze ukończenie (1 raz).
234. [Samouczek i wskazówki [tutorial_mainui_28_tkt_04_title_01] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_04_title_01].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Samouczek i wskazówki [tutorial_mainui_28_tkt_04_desc_01] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [회중시계]의 획득량이 크게 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_04_desc_01].content
   limit: do 190 znaków
   EN: Having Identities and E.G.O from Timekilling Time event on your team increases the amount of [Pocket Watch] earned from Stages and Mirror Dungeons.
   PL: Umieszczenie w drużynie premiowanych Tożsamości i E.G.O wydarzenia znacznie zwiększa liczbę [Zegarków Kieszonkowych] zdobywanych na etapach i w Lustrzanych Lochach.
236. [Samouczek i wskazówki [tutorial_mainui_28_tkt_05_title_01] — tekst] 아이템 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_05_title_01].content
   limit: do 120 znaków
   EN: Item Exchange
   PL: Wymiana przedmiotów
237. [Samouczek i wskazówki [tutorial_mainui_28_tkt_05_desc_01] — tekst] 획득한 [회중시계]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_05_desc_01].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Reward Exchange] based on the number of [Pocket Watch] you have.
   PL: Wydawaj zdobyte [Zegarki Kieszonkowe] w [Wymianie nagród], aby odbierać rozmaite nagrody.
238. [Samouczek i wskazówki [tutorial_mainui_28_tkt_06_desc_01] — tekst] [보상 교환] 페이지에서 이벤트 배포 인격과 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_06_desc_01].content
   limit: do 120 znaków
   EN: You can acquire the event reward Identity and various currencies from [Reward Exchange].
   PL: Na stronie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia oraz rozmaite waluty.
239. [Samouczek i wskazówki [tutorial_mainui_28_tkt_06_desc_02] — tekst] [보상 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_06_desc_02].content
   limit: do 120 znaków
   EN: The [Reward Exchange]'s open duration is shown here.
   PL: Tutaj wyświetlany jest okres odbioru nagród w [Wymianie nagród].
240. [Samouczek i wskazówki [tutorial_mainui_28_tkt_07_title_01] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_07_title_01].content
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Samouczek i wskazówki [tutorial_mainui_28_tkt_07_desc_01] — tekst] 시간살인시간 이벤트 제일 마지막에는 거울 던전이 등장하며, 입장 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_07_desc_01].content
   limit: do 160 znaków
   EN: A Mirror Dungeon awaits at the end of the Timekilling Time event. Entering this Mirror Dungeon costs Enkephalin Modules.
   PL: Na samym końcu wydarzenia Czas Zabijania Czasu czeka loch w trybie Lustrzanych Lochów; wejście do niego zużywa Moduły Enkefaliny.
242. [Samouczek i wskazówki [tutorial_mainui_28_tkt_08_title_01] — tekst] 회중시계 묶음
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_08_title_01].content
   limit: do 120 znaków
   EN: Pocket Watch Bundle
   PL: Pęk Zegarków Kieszonkowych
243. [Samouczek i wskazówki [tutorial_mainui_28_tkt_08_desc_01] — tekst] 전투에서 승리할 경우, 낮은 확률로 [회중시계 묶음]을 획득할 수 있습니다.\n\n획득한 [회중시계 묶음]은 [회중시계] 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_08_desc_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rarely, you may obtain [Pocket Watch Bundle] from clearing Encounters.\n\n[Pocket Watch Bundle] is automatically converted to 20 [Pocket Watch] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Pęku Zegarków Kieszonkowych].\n\nZdobyty [Pęk Zegarków Kieszonkowych] jest automatycznie zamieniany na 20 [Zegarków Kieszonkowych].
244. [Samouczek i wskazówki [tutorial_mainui_28_tkt_09_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 시간살인시간 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt_09_desc_01].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Timekilling Time combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Czasu Zabijania Czasu możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
245. [Samouczek i wskazówki [tutorial_mainui_28_tkt] — tekst] 시간살인시간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_28_tkt].content
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
246. [Samouczek i wskazówki [tutorial_mainui_railway4_title_01] — tekst] 거울굴절철도 4호선
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_title_01].content
   limit: do 120 znaków
   EN: Refraction Railway Line 4
   PL: Kolej Załamania — Linia 4
247. [Samouczek i wskazówki [tutorial_mainui_railway4_page_01_title_01] — tekst] 입장 방법
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_01_title_01].content
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Samouczek i wskazówki [tutorial_mainui_railway4_page_01_desc_01] — tekst] 활성화된 노선을 선택하여 입장합니다.\n\n거울굴절철도 입장 시에는 재화를 소모하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_01_desc_01].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the activated Line to enter. Entering the Refraction Railway does not cost any currency or resources.
   PL: Wybierz aktywną linię, aby wejść.\n\nWejście do Kolei Załamania nie zużywa żadnych walut.
249. [Samouczek i wskazówki [tutorial_mainui_railway4_page_02_desc_01] — tekst] 거울굴절철도는 매우 어려운 난이도의 콘텐츠입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_02_desc_01].content
   limit: do 120 znaków
   EN: Refraction Railway presents a series of very challenging battles.
   PL: Kolej Załamania to zawartość o bardzo wysokim poziomie trudności.
250. [Samouczek i wskazówki [tutorial_mainui_railway4_page_02_desc_02] — tekst] 이번 4호선의 경우, 입장 시 권장 사양은 인격 동기화 4단계와 레벨 45, E.G.O 환상 해석 4단계입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_02_desc_02].content
   limit: do 150 znaków
   EN: We recommend that you Uptie your Identities to Tier 4, level them to Level 45, and Threadspin your E.G.Os to Tier 4.
   PL: Zalecane parametry na Linii 4 to 4. stopień Synchronizacji i 45. poziom Tożsamości oraz 4. stopień Splotu Nici E.G.O.
251. [Samouczek i wskazówki [tutorial_mainui_railway4_page_02_desc_03] — tekst] 되도록이면 육성 조건을 맞춘 이후에 입장하는 것을 추천드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_02_desc_03].content
   limit: do 120 znaków
   EN: We suggest that you enter the Railway after meeting the recommended conditions.
   PL: Zalecamy wejście dopiero po spełnieniu sugerowanych warunków rozwoju.
252. [Samouczek i wskazówki [tutorial_mainui_railway4_page_03_title_01] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_03_title_01].content
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Samouczek i wskazówki [tutorial_mainui_railway4_page_03_desc_01] — tekst] 보유한 인격과 E.G.O를 편성하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_03_desc_01].content
   limit: do 120 znaków
   EN: Choose a number of Identities and E.G.O to enter the Railway with.
   PL: Uformuj skład z posiadanych Tożsamości oraz E.G.O i rozpocznij wyprawę.
254. [Samouczek i wskazówki [tutorial_mainui_railway4_page_03_desc_02] — tekst] 인격의 레벨을 올리거나 동기화 단계 상승, E.G.O 환상 해석 단계 상승 시, 진행 중인 거울굴절철도에도 변경된 내용이 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_03_desc_02].content
   limit: do 230 znaków
   EN: If you level up, Uptie, or Threadspin your Identities or E.G.O outside the Refraction Railway, the changes will be applied to your characters in the Refraction Railway as well.
   PL: Podniesienie poziomu Tożsamości, stopnia Synchronizacji lub stopnia Splotu Nici E.G.O poza Koleją Załamania zostanie odzwierciedlone również w trwającej wyprawie.
255. [Samouczek i wskazówki [tutorial_mainui_railway4_page_04_title_01] — tekst] 4호선 역과 구간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_04_title_01].content
   limit: do 120 znaków
   EN: Line 4: Stations and Sections
   PL: Linia 4: stacje i odcinki
256. [Samouczek i wskazówki [tutorial_mainui_railway4_page_04_desc_01] — tekst] 4호선에는 총 13개의 역이 있으며, 여러 개의 역은 각 구간 별로 묶여 각각의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_04_desc_01].content
   limit: do 180 znaków
   EN: Refraction Railway Line 4 is composed of several Sections that tie several Stations into a single Stage. There are a total of 13 Stations.
   PL: Linia 4 liczy łącznie 13 stacji połączonych w poszczególne odcinki, z których każdy stanowi osobny etap.
257. [Samouczek i wskazówki [tutorial_mainui_railway4_page_04_desc_02] — tekst] 4호선은 네 개의 구간으로 구성된 전투 스테이지와 각 구간별 사이에 휴게역이 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_04_desc_02].content
   limit: do 140 znaków
   EN: There are four Combat Encounter Stages, each called a 'Section'; between each Section is a rest station.
   PL: Linia 4 obejmuje cztery odcinki bojowe oraz stacje postojowe pomiędzy nimi.
258. [Samouczek i wskazówki [tutorial_mainui_railway4_page_05_desc_01] — tekst] 구간을 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_05_desc_01].content
   limit: do 120 znaków
   EN: Select the Section to enter.
   PL: Wybierz odcinek, aby wejść.
259. [Samouczek i wskazówki [tutorial_mainui_railway4_page_05_desc_02] — tekst] 해당 구간 클리어 시, 클리어 턴이 기록됩니다.\n\n이와 함께 제 1 구간으로부터 현재 구간까지의 각 구간별 클리어 턴이 모두 합해진 누적 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_05_desc_02].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the Section will record your Clear Turn Count.\n\nBelow the Clear Turn Count is the Total Turn Count, which is the sum of all Clear Turn Counts from each Section.
   PL: Po ukończeniu odcinka zapisywana jest liczba tur ukończenia.\n\nObok niej zapisywana jest łączna liczba tur będąca sumą tur ukończenia wszystkich odcinków od Odcinka 1 do bieżącego.
260. [Samouczek i wskazówki [tutorial_mainui_railway4_page_05_desc_03] — tekst] 해당 구간을 클리어하였을 때 분실물보관소를 통해 얻을 수 있게 되는 보상이 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_05_desc_03].content
   limit: do 140 znaków
   EN: Below each Section, you can view the rewards for clearing that Section. Claim them at the Lost & Found.
   PL: Poniżej widnieją nagrody za ukończenie danego odcinka do odebrania w Biurze Rzeczy Znalezionych.
261. [Samouczek i wskazówki [tutorial_mainui_railway4_page_06_title_01] — tekst] 전투 편성 - 편성 순서 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_06_title_01].content
   limit: do 120 znaków
   EN: Combat Deployment - Deployment Order Effects
   PL: Ustawienie drużyny — efekty kolejności
262. [Samouczek i wskazówki [tutorial_mainui_railway4_page_06_desc_01] — tekst] 4호선에서는 편성 순서에 따라 특별한 버프를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_06_desc_01].content
   limit: do 140 znaków
   EN: Refraction Railway Line 4 presents special buffs to your Sinners depending on their order of Deployment.
   PL: Na Linii 4 Grzesznicy otrzymują specjalne wzmocnienia zależne od kolejności rozstawienia.
263. [Samouczek i wskazówki [tutorial_mainui_railway4_page_06_desc_02] — tekst] 일부 대기 인원에게는 시작 정신력 버프가 추가로 적용됩니다. 빼기 코인을 사용하는 인격의 경우에는 시작 정신력 버프가 음수값으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_06_desc_02].content
   limit: do 150 znaków
   EN: Certain Backup units receive additional Entry SP buffs. Minus Coin Identities will receive negative Entry SP buffs.
   PL: Niektórzy rezerwowi zyskują premię początkowych PP. W przypadku Tożsamości z Monetami Ujemnymi premia początkowych PP ma wartość ujemną.
264. [Samouczek i wskazówki [tutorial_mainui_railway4_page_07_title_01] — tekst] 전투 편성 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_07_title_01].content
   limit: do 120 znaków
   EN: Combat Deployment - Chain Battles
   PL: Ustawienie drużyny — Walka Seryjna
265. [Samouczek i wskazówki [tutorial_mainui_railway4_page_07_desc_01] — tekst] 4호선은 연속 전투 방식으로 진행됩니다.\n\n연속 전투에서는 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_07_desc_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Refraction Railway Line 4 introduces the 'Chain Battle' system.\n\nIn Chain Battles, when a Deployed unit is defeated, the Backup units will fill their spots in their own Deployment orders.
   PL: Linia 4 rozgrywana jest w trybie Walki Seryjnej.\n\nW Walce Seryjnej po śmierci uczestnika w polu jego miejsce zajmuje kolejny rezerwowy zgodnie z ustaloną kolejnością.
266. [Samouczek i wskazówki [tutorial_mainui_railway4_page_07_desc_02] — tekst] 7명의 출격 인원과 5명의 대기 인원을 전부 설정하여야 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_07_desc_02].content
   limit: do 160 znaków
   EN: You can enter the Station only when you have selected both your Deployment and Backup units: 7 and 5 units, respectively.
   PL: Aby wejść, musisz obsadzić wszystkich 7 uczestników podstawowych oraz 5 rezerwowych.
267. [Samouczek i wskazówki [tutorial_mainui_railway4_page_08_title_01] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_08_title_01].content
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Samouczek i wskazówki [tutorial_mainui_railway4_page_08_desc_01] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.\n거울굴절철도 4호선 진입시 빛의 묘목 능력을 진행 중 1회 사용할 수 있습니다.\n사용 시 해당 컨텐츠 밖에서의 사용 횟수에 영향을 주지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_08_desc_01].content
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every battle in the Refraction Railway will allow you to directly match ally skills against enemy skills, just like in Focused Encounters.\nIn Refraction Railway Line 4, the Sapling of Light ability can be activated once per every run.\nActivation inside the Refraction Railway does not count toward the activation limit outside the Refraction Railway.
   PL: Wszystkie walki odbywają się w trybie starcia skupionego, w którym bezpośrednio kierujesz umiejętności sojuszników przeciw wrogom.\nPo wejściu na Linię 4 Kolei Załamania możesz użyć zdolności Sadzonki Światła 1 raz na wyprawę.\nJej użycie nie zużywa dziennego limitu poza tym trybem.
269. [Samouczek i wskazówki [tutorial_mainui_railway4_page_09_title_01] — tekst] 전투 - 편성 순서 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_09_title_01].content
   limit: do 120 znaków
   EN: Combat - Deployment Order Effects
   PL: Walka — efekty kolejności rozstawienia
270. [Samouczek i wskazówki [tutorial_mainui_railway4_page_09_desc_01] — tekst] 편성 순서에 따라 적용된 버프를 전투 중에도 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_09_desc_01].content
   limit: do 120 znaków
   EN: You can view the Deployment Order effects in the middle of an Encounter as well.
   PL: Wzmocnienia wynikające z kolejności rozstawienia można sprawdzić również w trakcie walki.
271. [Samouczek i wskazówki [tutorial_mainui_railway4_page_09_desc_02] — tekst] 4호선에서는 아군 인격이 사망하면, 사망한 인격이 보유한 기본 공격 스킬과 동일한 속성의 E.G.O 자원을 각 스킬의 등급만큼 얻게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_09_desc_02].content
   limit: do 360 znaków
   EN: In Line 4, a defeated ally Identity will give E.G.O resources that correspond with the Sin Affinities of the Attack Skills on the defeated Ally. The amount of E.G.O resources given corresponds with the Rank of each Attack Skill. (S1 gives 1, S2 gives 2, S3 gives 3, for example)
   PL: Na Linii 4 śmierć sojuszniczej Tożsamości zapewnia zasoby E.G.O odpowiadające grzechom jej podstawowych umiejętności ataku w liczbie równej randze każdej z tych umiejętności.
272. [Samouczek i wskazówki [tutorial_mainui_railway4_page_10_title_01] — tekst] 전투 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_10_title_01].content
   limit: do 120 znaków
   EN: Combat - Chain Battles
   PL: Walka — Walka Seryjna
273. [Samouczek i wskazówki [tutorial_mainui_railway4_page_10_desc_01] — tekst] 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_10_desc_01].content
   limit: do 130 znaków
   EN: When a Deployed unit is defeated, the Backup units will fill their spot in the Deployment order.
   PL: Gdy uczestnik podstawowy zginie, rezerwowi zajmują jego miejsce zgodnie z ustaloną kolejnością.
274. [Samouczek i wskazówki [tutorial_mainui_railway4_page_10_desc_02] — tekst] 대기 인원이 출격 인원으로 전환되면, 적용 중인 서포트 패시브가 전투 패시브로 변경됩니다.\n\n출격 인원이 사망한 경우, 적용 중인 전투 패시브가 서포트 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_10_desc_02].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a Backup unit is Deployed into battle, its Combat Passive activates instead of its Support Passive.\n\nWhen a Deployed unit is defeated, its Support Passive will activate instead of its Combat Passive.
   PL: Gdy rezerwowy wchodzi do walki, jego pasywka wsparcia zamienia się w pasywkę bojową.\n\nGdy uczestnik podstawowy zginie, jego pasywka bojowa zamienia się w pasywkę wsparcia.
275. [Samouczek i wskazówki [tutorial_mainui_railway4_page_11_title_01] — tekst] 전투 - 굳은 의지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_11_title_01].content
   limit: do 120 znaków
   EN: Combat - Resilient Determination
   PL: Walka — Niezłomna Wola
276. [Samouczek i wskazówki [tutorial_mainui_railway4_page_11_desc_01] — tekst] 4호선에서는 인격이 사망 시 정신력이 감소하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_11_desc_01].content
   limit: do 120 znaków
   EN: In Line 4, ally death will not lower the other allies' SP.
   PL: Na Linii 4 śmierć Tożsamości nie obniża PP pozostałych sojuszników.
277. [Samouczek i wskazówki [tutorial_mainui_railway4_page_11_desc_02] — tekst] 4호선에 등장하는 일부 적들에게는 편성 순서가 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_11_desc_02].content
   limit: do 120 znaków
   EN: Certain enemies in Line 4 will gain certain effects based on their Deployment orders.
   PL: Niektórzy wrogowie na Linii 4 również podlegają efektom kolejności rozstawienia.
278. [Samouczek i wskazówki [tutorial_mainui_railway4_page_12_title_01] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_12_title_01].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Samouczek i wskazówki [tutorial_mainui_railway4_page_12_desc_01] — tekst] 스토리 던전 또는 거울 던전 전투를 통해 관찰 단계가 활성화된 환상체를 조우할 경우, 그 내용이 환상체 도감에 반영되어 확인할 수 있게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_12_desc_01].content
   limit: do 330 znaków
   EN: If you have already unlocked the Abnormalities' Observation Levels through the Story Dungeon or Mirror Dungeon Encounters, their Observation Levels will be reflected in the Refraction Railway, and you can view their information as you would in those Dungeons.
   PL: Jeśli w Lochach Fabularnych lub Lustrzanych Lochach odblokowano Poziomy Obserwacji napotkanych Anomalii, zostaną one uwzględnione w Kompendium Anomalii i będą widoczne podczas walki.
280. [Samouczek i wskazówki [tutorial_mainui_railway4_page_12_desc_02] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_12_desc_02].content
   limit: do 130 znaków
   EN: However, the damage bonus based on Observation Levels does not apply in the Refraction Railway.
   PL: Premia do obrażeń wynikająca z Poziomu Obserwacji nie jest jednak aktywna.
281. [Samouczek i wskazówki [tutorial_mainui_railway4_page_12_desc_03] — tekst] 4호선에서는 전투 중 재도전하거나 포기하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_12_desc_03].content
   limit: do 130 znaków
   EN: In Line 4, the updated Observation Level will be saved even if you give up or retry mid-Encounter.
   PL: Na Linii 4 zaktualizowane wpisy Kompendium zostają zapisane nawet przy ponowieniu lub poddaniu walki.
282. [Samouczek i wskazówki [tutorial_mainui_railway4_page_13_desc_01] — tekst] 전투 이후 남은 E.G.O 자원은 다음 구간에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_13_desc_01].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a Station can be carried over to the next Section.
   PL: Zasoby E.G.O pozostałe po walce można wykorzystać na następnym odcinku.
283. [Samouczek i wskazówki [tutorial_mainui_railway4_page_13_desc_02] — tekst] 편성한 인격의 체력, 정신력, 사망 상태가 화면 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_13_desc_02].content
   limit: do 120 znaków
   EN: The HP, SP, and availability of your Identities are shown at the bottom of the screen.
   PL: U dołu ekranu widnieją PŻ, PP oraz stan poległych Tożsamości w składzie.
284. [Samouczek i wskazówki [tutorial_mainui_railway4_page_14_title_01] — tekst] 휴게역
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_14_title_01].content
   limit: do 120 znaków
   EN: Rest Stations
   PL: Stacje postojowe
285. [Samouczek i wskazówki [tutorial_mainui_railway4_page_14_desc_01] — tekst] 각 구간 사이에 있는 휴게역에서는 체력이 최대가 되고 정신력이 0으로 초기화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_14_desc_01].content
   limit: do 160 znaków
   EN: Stopping by the Rest Stations, which are located between Sections, will fully heal your Identities and reset their Sp to 0.
   PL: Na stacjach postojowych pomiędzy odcinkami PŻ wracają do maksimum, a PP zostają zresetowane do 0.
286. [Samouczek i wskazówki [tutorial_mainui_railway4_page_14_desc_02] — tekst] 휴게역에서는 편성을 자유롭게 변경할 수 있습니다.\n\n전투 진행에 어려움을 느끼신다면 휴게역에서 다른 편성으로 교체하는 방법을 권장드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_14_desc_02].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can also change your Team Loadout in Rest Stations.\n\nIf you are having difficulty clearing a Stage, please note that a different Team may work better against certain enemies.
   PL: Na stacjach postojowych możesz swobodnie zmienić skład drużyny.\n\nJeśli dany etap sprawia trudności, zalecamy wymianę składu na stacji postojowej.
287. [Samouczek i wskazówki [tutorial_mainui_railway4_page_15_desc_01] — tekst] 아군이 모두 전멸하였다면 입장 화면으로 돌아가 편성 순서를 다시 설정하거나 현재 전투를 즉시 재도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_15_desc_01].content
   limit: do 210 znaków
   EN: If all of your allies are defeated, you can choose between returning to the Team Loadout menu to change your Deployment orders, and immediately retrying the battle.
   PL: W razie zagłady całej drużyny możesz wrócić do ekranu wejścia, aby zmienić kolejność rozstawienia, albo natychmiast ponowić bieżącą walkę.
288. [Samouczek i wskazówki [tutorial_mainui_railway4_page_16_title_01] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_16_title_01].content
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Samouczek i wskazówki [tutorial_mainui_railway4_page_16_desc_01] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_16_desc_01].content
   limit: do 120 znaków
   EN: During an expedition, you can choose to start over from previously cleared Stages.
   PL: W trakcie wyprawy możesz rozpocząć grę od nowa od wybranego ukończonego wcześniej etapu.
290. [Samouczek i wskazówki [tutorial_mainui_railway4_page_16_desc_02] — tekst] 특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_16_desc_02].content
   limit: do 220 znaków
   EN: When you do so, the battle will start with the Sinners’ statuses and E.G.O resources reverted to that point, and any progress you've made since that Stage will be reset.
   PL: Rozpoczęcie od wybranego etapu przywraca stan Tożsamości oraz posiadane zasoby E.G.O z momentu wejścia na ten etap, a rekordy późniejszych etapów zostają wyczyszczone.
291. [Samouczek i wskazówki [tutorial_mainui_railway4_page_17_title_01] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_17_title_01].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Samouczek i wskazówki [tutorial_mainui_railway4_page_17_desc_01] — tekst] 거울굴절철도 4호선 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_17_desc_01].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 4 banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 4.
293. [Samouczek i wskazówki [tutorial_mainui_railway4_page_17_desc_02] — tekst] 배너를 획득하면 제일 좋은 기록의 누적 턴 수가 배너에 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_17_desc_02].content
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Samouczek i wskazówki [tutorial_mainui_railway4_page_18_title_01] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_18_title_01].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Samouczek i wskazówki [tutorial_mainui_railway4_page_18_desc_01] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_18_desc_01].content
   limit: do 130 znaków
   EN: After clearing a Stage in the Line for the first time, the rewards will be sent to the Lost & Found.
   PL: Po pierwszym ukończeniu etapu nagroda trafia do Biura Rzeczy Znalezionych i zostaje aktywowana.
296. [Samouczek i wskazówki [tutorial_mainui_railway4_page_18_desc_02] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.\n\n이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_18_desc_02].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To gain access to a reward for the first time at Lost & Found, a number of Enkephalin Modules will be required.\nAfterward, you may freely access it and claim rewards you’ve earned at no additional cost.
   PL: Aby po raz pierwszy odebrać nagrody w Biurze Rzeczy Znalezionych, należy jednorazowo zapłacić określoną liczbę Modułów Enkefaliny.\n\nKolejne odblokowane nagrody odbierzesz w dowolnej chwili bez dodatkowych Modułów Enkefaliny.
297. [Samouczek i wskazówki [tutorial_mainui_railway4_page_19_title_01] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_19_title_01].content
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Samouczek i wskazówki [tutorial_mainui_railway4_page_19_desc_01] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_19_desc_01].content
   limit: do 150 znaków
   EN: Upon clearing the final Stage, your Refraction Railway play record will be saved. Up to 20 records can be viewed.
   PL: Po ukończeniu finałowego etapu zapisywany jest rekord przejścia Kolei Załamania; możesz przeglądać maksymalnie 20 rekordów.
299. [Samouczek i wskazówki [tutorial_mainui_railway4_page_19_desc_02] — tekst] 기록이 20개를 넘어갈 경우에는 누적 턴 수가 많은 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_railway4_page_19_desc_02].content
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Samouczek i wskazówki [tutorial_mainui_29_mowe_01_title] — tekst] 워프특급 살인사건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_01_title].content
   limit: do 120 znaków
   EN: Murder on the WARP Express
   PL: Morderstwo w Ekspresie WARP
301. [Samouczek i wskazówki [tutorial_mainui_29_mowe_01_title_01] — tekst] 워프특급 살인사건 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_01_title_01].content
   limit: do 120 znaków
   EN: Unlocking Murder on the WARP Express
   PL: Odblokowanie Morderstwa w Ekspresie WARP
302. [Samouczek i wskazówki [tutorial_mainui_29_mowe_01_desc_01] — tekst] [워프특급 살인사건 이벤트 페이지]는 주요 이야기의 0-4를 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_01_desc_01].content
   limit: do 220 znaków
   EN: The [Murder on the WARP Express Event Page] opens after clearing Stage 0-4 of the Main Story. You may enter the event page via the banner on the Window or the Driverside.
   PL: [Strona wydarzenia Morderstwo w Ekspresie WARP] odblokowuje się po ukończeniu etapu 0-4 Głównej Opowieści. Wejdziesz na nią przez baner wydarzenia w Oknie lub Jeździe.
303. [Samouczek i wskazówki [tutorial_mainui_29_mowe_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_02_title_01].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Samouczek i wskazówki [tutorial_mainui_29_mowe_02_desc_01] — tekst] 워프특급 살인사건 이벤트 기간이 표시됩니다. 이벤트 기간 동안 워프특급 살인사건 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [일반 승객 복구팩]을 획득할 수 있습니다. ※ 단, 채광과 거울굴절철도에서는 [일반 승객 복구팩]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_02_desc_01].content
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Murder on the WARP Express event is shown here.\n\nDuring the event, you can earn [Civilian Recov. Pack] by clearing Event Stages. You can also earn [Civilian Recov. Pack] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Civilian Recov. Pack] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Morderstwo w Ekspresie WARP. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Pakiety Rekonstrukcyjne Pasażera]. ※ [Pakietów Rekonstrukcyjnych Pasażera] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
305. [Samouczek i wskazówki [tutorial_mainui_29_mowe_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_03_title_01].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Samouczek i wskazówki [tutorial_mainui_29_mowe_03_desc_01] — tekst] 워프특급 살인사건 스테이지는 스토리 스테이지를 포함하여 총 15개의 스테이지로 구성됩니다. 워프특급 살인사건 전투에서는 클리어 보상과 별개로 초회 보상으로 [일반 승객 복구팩]을 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_03_desc_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Murder on the WARP Express consists of 15 stages, including story stages.\nSaid stages also offer batches of [Civilian Recov. Pack] as a first-time EX Clear bonus.
   PL: Morderstwo w Ekspresie WARP obejmuje łącznie 15 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Pakiety Rekonstrukcyjne Pasażera] za pierwsze ukończenie (1 raz).
307. [Samouczek i wskazówki [tutorial_mainui_29_mowe_03_desc_02] — tekst] 워프특급 살인사건 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [일반 승객 복구팩]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_03_desc_02].content
   limit: do 160 znaków
   EN: You can earn considerably more [Civilian Recov. Pack] from Murder on the WARP Express Stages compared to Main Story Stages.
   PL: Etapy Morderstwa w Ekspresie WARP zapewniają znacznie więcej [Pakietów Rekonstrukcyjnych Pasażera] niż etapy Głównej Opowieści.
308. [Samouczek i wskazówki [tutorial_mainui_29_mowe_04_title_01] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_04_title_01].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Samouczek i wskazówki [tutorial_mainui_29_mowe_04_desc_01] — tekst] 워프특급 살인사건 기간 동안 이벤트 인격, E.G.O 편성하여 스테이지를 클리어하면 [일반 승객 복구팩]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_04_desc_01].content
   limit: do 220 znaków
   EN: Having Event Identities and E.G.O from the Murder on the WARP Express event on your team increases the amount of [Civilian Recov. Pack] earned from Stages and Dungeons.
   PL: Wystawienie w drużynie Tożsamości i E.G.O wydarzenia Morderstwo w Ekspresie WARP zwiększa liczbę zdobywanych [Pakietów Rekonstrukcyjnych Pasażera].
310. [Samouczek i wskazówki [tutorial_mainui_29_mowe_05_title_01] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_05_title_01].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Samouczek i wskazówki [tutorial_mainui_29_mowe_05_desc_01] — tekst] 획득한 [일반 승객 복구팩]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_05_desc_01].content
   limit: do 150 znaków
   EN: You can redeem various rewards from the [Reward Exchange] using the [Civilian Recov. Pack] you have collected.
   PL: Wydawaj zdobyte [Pakiety Rekonstrukcyjne Pasażera] w [Wymianie nagród], aby odbierać rozmaite nagrody.
312. [Samouczek i wskazówki [tutorial_mainui_29_mowe_06_desc_01] — tekst] [보상 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_06_desc_01].content
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Samouczek i wskazówki [tutorial_mainui_29_mowe_06_desc_02] — tekst] [보상 교환] 페이지에서 각종 재화와 이벤트 배포 인격을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_06_desc_02].content
   limit: do 120 znaków
   EN: You can acquire event reward Identities and various currencies from the [Reward Exchange].
   PL: Na stronie [Wymiany nagród] zdobędziesz rozmaite waluty oraz darmową Tożsamość wydarzenia.
314. [Samouczek i wskazówki [tutorial_mainui_29_mowe_07_title_01] — tekst] 연속 전투 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_07_title_01].content
   limit: do 120 znaków
   EN: Chain Battle Encounters
   PL: Etapy Walki Seryjnej
315. [Samouczek i wskazówki [tutorial_mainui_29_mowe_07_desc_01] — tekst] 워프특급 살인사건의 일부 전투는 연속 전투 방식으로 진행됩니다. 연속 전투에서는 아군이 죽더라도 정신력이 소모되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_07_desc_01].content
   limit: do 230 znaków
   EN: Certain Encounters in the Murder on the WARP Express event are Chain Battles. In Chain Battles, the Sinners will not lose their Sanity(SP) even if their allies are defeated.
   PL: Część walk Morderstwa w Ekspresie WARP to Walki Seryjne. W Walkach Seryjnych śmierć sojusznika nie obniża Poczytalności (PP) pozostałych.
316. [Samouczek i wskazówki [tutorial_mainui_29_mowe_08_title_01] — tekst] 해결사 승객 복구팩
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_08_title_01].content
   limit: do 120 znaków
   EN: Fixer Recov. Pack
   PL: Pakiet Rekonstrukcyjny Fiksera
317. [Samouczek i wskazówki [tutorial_mainui_29_mowe_08_desc_01] — tekst] 전투에서 승리할 경우, 낮은 확률로 [해결사 승객 복구팩]을 획득할 수 있습니다. 획득한 해결사 승객 복구팩은 일반 승객 복구팩 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_08_desc_01].content
   limit: do 210 znaków
   EN: Rarely, you may obtain [Fixer Recov. Pack] from clearing Encounters. [Fixer Recov. Pack] is immediately converted to 20 [Civilian Recov. Pack] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Pakietu Rekonstrukcyjnego Fiksera], który od razu zamienia się na 20 [Pakietów Rekonstrukcyjnych Pasażera].
318. [Samouczek i wskazówki [tutorial_mainui_29_mowe_09_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관 - [그 밖의 이야기]를 통해 워프특급 살인사건 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_29_mowe_09_desc_01].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Murder on the WARP Express combat Encounters and view its story at any time at the Driverside and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Morderstwa w Ekspresie WARP możesz w każdej chwili odtworzyć w menu Jazda oraz Teatr — [Opowieści Poboczne].
319. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_11_title_01] — tekst] 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_11_title_01].content
   limit: do 120 znaków
   EN: Chain Battles
   PL: Walka Seryjna
320. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_11_desc_01] — tekst] 연속 전투에서는 전투 참가 인원 이외에도 '대기 인원'을 선택할 수 있습니다.\n\n전투 중 전투 참가 인원이 사망하면, 대기 인원이 그 자리를 대신하여 전투에 참가합니다.\n\n연속 전투는 편성에서 선택한 모든 인원(전투 참가 인원, 대기 인원)이 사망할 때까지 전투에서 패배해지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_11_desc_01].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Chain Battles, you can deploy 'Backup Units' in addition to participating units.\n\nWhen a unit is defeated mid-battle, a backup unit will substitute in to fill their place.\n\nIn Chain Battles, you cannot lose until all units selected for the Encounter(both participating units and backup units) are defeated.
   PL: W Walce Seryjnej oprócz uczestników podstawowych możesz wybrać również „jednostki rezerwowe”.\n\nGdy uczestnik podstawowy zginie w trakcie walki, jego miejsce zajmuje rezerwowy.\n\nW Walce Seryjnej nie przegrywasz, dopóki nie polegną wszystkie wybrane jednostki (zarówno podstawowe, jak i rezerwowe).
321. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_12_title_01] — tekst] 대기 인원 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_12_title_01].content
   limit: do 120 znaków
   EN: Deploying Backup Units
   PL: Ustawianie rezerwowych
322. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_12_desc_01] — tekst] 전투 참가 인원이 사망하였을 때, 대기 인원은 편성 순서에 따라 등장합니다.\n\n대기 인원이 전투에 참여할 때 편성 순서에 따른 시작 정신력 값만큼 해당 캐릭터의 정신력이 회복됩니다.\n\n일부 연속 전투에서는 대기 인원이 전투에 참가할 때 부가적인 효과를 얻을 수 있습니다.\n\n이를 활용하여 전략적으로 편성 순서를 정하세요.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_12_desc_01].content
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a participating unit is killed, Backup units will be substituted into the field in the order of their Deployment.\n\nWhen the Backup units substitute into the battle, they enter with bonus SP based on the starting SP values defined by their deployment order.\n\nCertain Chain Battles may give additional buffs for Backup units.\n\nPlease experiment with Deployment orders to strategize prior to entering Chain Battles.
   PL: Gdy uczestnik podstawowy polegnie, rezerwowi wkraczają na pole bitwy zgodnie z kolejnością rozstawienia.\n\nWchodzący do walki rezerwowy odzyskuje PP w liczbie odpowiadającej premii początkowych PP przypisanej do jego numeru rozstawienia.\n\nW niektórych Walkach Seryjnych wchodzący rezerwowi otrzymują też dodatkowe wzmocnienia.\n\nWykorzystaj to, aby strategicznie zaplanować kolejność rozstawienia.
323. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_13_title_01] — tekst] 대기 해제
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_13_title_01].content
   limit: do 120 znaków
   EN: Substitute
   PL: Wejście Rezerwy
324. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_13_desc_01] — tekst] 연속 전투에서는 아군이 사망하더라도 기본 정신력 증감 조건으로 인해 정신력이 감소하지 않습니다.\n\n전투 중 일부 인원이 사망했다면, 현재 편성 순서가 가장 빠른 대기 인원이 그 자리를 대신하여 전투에 참가합니다.\n이를 <대기 해제>라고 합니다.\n\n사망한 인격의 전투 패시브는 서포트 패시브로 전환됩니다.\n\n대기 해제된 인격의 서포트 패시브는 전투 패시브로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_13_desc_01].content
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Chain Battles, SP loss due to ally death listed in the 'Base factors increasing/decreasing Sanity' will not activate.\n\nIf an ally is defeated mid-Encounter, the Backup unit next in the Deployment order will replace them.\nThis is called <Substitution>.\n\nWhen a Deployed unit is defeated, its Support Passive will activate instead of its Combat Passive.\n\nWhen a Backup unit is substituted in, its Combat Passive will activate instead of its Support Passive.
   PL: W Walce Seryjnej śmierć sojusznika nie powoduje utraty PP z podstawowych warunków zmiany Poczytalności.\n\nGdy uczestnik polegnie w walce, zastępuje go rezerwowy o najniższym numerze w kolejności rozstawienia.\nNazywa się to „Wejściem Rezerwy”.\n\nPasywka bojowa poległej Tożsamości przełącza się na pasywkę wsparcia.\n\nPasywka wsparcia wchodzącej Tożsamości rezerwowej przełącza się na pasywkę bojową.
325. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_14_title_01] — tekst] 적 현황 표기 UI
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_14_title_01].content
   limit: do 120 znaków
   EN: Remaining Enemies Indicator
   PL: Wskaźnik stanu wrogów
326. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_14_desc_01] — tekst] 연속 전투에서는 기존의 WAVE UI에서 전투에 등장하는 적의 수와 처치한 적의 수가 표시됩니다.\n\n다만, 전투 중 특정 조건에 의해 생성되는 적은 해당 UI에 표시되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_14_desc_01].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Chain Battles, the indicator that shows the number of Waves shows total number of enemies and the number of defeated enemies instead.\n\nHowever, this indicator does not take into account the extra enemies that are summoned due to certain conditions.
   PL: W Walce Seryjnej w miejscu dotychczasowego wskaźnika fal (WAVE) wyświetlana jest łączna liczba wrogów w walce oraz liczba pokonanych wrogów.\n\nDodatkowi wrogowie przyzywani w trakcie walki po spełnieniu określonych warunków nie są jednak uwzględniani na tym wskaźniku.
327. [Samouczek i wskazówki [TutoEvent5501_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Samouczek i wskazówki [TutoEvent5501_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [20번구의 기적 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P1_D1].content
   limit: do 160 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Miracle in District 20 BokGak Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Cud w Dystrykcie 20 BokGak].
329. [Samouczek i wskazówki [TutoEvent5501_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Samouczek i wskazówki [TutoEvent5501_P2_D1] — tekst] 20번구의 기적 BokGak 이벤트 기간이 표시됩니다.\n\n이벤트 기간 동안 20번구의 기적 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [장식 꾸러미]를 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [장식 꾸러미]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P2_D1].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Miracle in District 20 BokGak Event is shown here.\n\nDuring the event, you can earn [Trinkets Sack] by clearing Event Stages. You can also earn [Trinkets Sack] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Trinkets Sack] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Cud w Dystrykcie 20 BokGak.\n\nW trakcie wydarzenia ukończenie etapów Cudu w Dystrykcie 20, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Worki Ozdób].\n\n※ [Worków Ozdób] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
331. [Samouczek i wskazówki [TutoEvent5501_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Samouczek i wskazówki [TutoEvent5501_P3_D1] — tekst] 20번구의 기적 BokGak 이벤트는 스토리 스테이지를 포함하여 총 13개의 스테이지로 구성됩니다.\n\n이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [장식 꾸러미]를 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P3_D1].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Miracle in District 20 BokGak Event consists of 13 stages, including story stages.\n\nSaid stages also offer batches of [Trinkets Sack] as a First-time Clear bonus in addition to clear rewards. (only for first-time clears of each Stage)
   PL: Wydarzenie Cud w Dystrykcie 20 BokGak obejmuje łącznie 13 etapów wraz z fabularnymi.\n\nWalki wydarzenia zapewniają oprócz zwykłych nagród także [Worki Ozdób] za pierwsze ukończenie każdego etapu (1 raz na walkę).
333. [Samouczek i wskazówki [TutoEvent5501_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Samouczek i wskazówki [TutoEvent5501_P4_D1] — tekst] 이벤트 기간 동안 이벤트 E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [장식 꾸러미]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P4_D1].content
   limit: do 170 znaków
   EN: Having Event E.G.Os from the Event on your team increases the amount of [Trinkets Sack] earned from Stages and the Mirror Dungeon.
   PL: Wystawienie E.G.O wydarzenia w drużynie zwiększa liczbę [Worków Ozdób] zdobywanych na etapach oraz w Lustrzanych Lochach.
335. [Samouczek i wskazówki [TutoEvent5501_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Samouczek i wskazówki [TutoEvent5501_P5_D1] — tekst] 획득한 [장식 꾸러미]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P5_D1].content
   limit: do 130 znaków
   EN: You can redeem various rewards from [Reward Exchange] by spending the [Trickets Sack] you collected.
   PL: Wydawaj zdobyte [Worki Ozdób] w [Wymianie nagród], aby odbierać rozmaite nagrody.
337. [Samouczek i wskazówki [TutoEvent5501_P6_D1] — tekst] [보상 교환] 창에서 이벤트 배포 E.G.O와 아나운서, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P6_D1].content
   limit: do 160 znaków
   EN: You can acquire the event reward E.G.O, Announcer, Ticket Deco, banners, and various currencies from [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmowe E.G.O wydarzenia, Komentatora, ozdoby biletu, banery oraz rozmaite waluty.
338. [Samouczek i wskazówki [TutoEvent5501_P6_D2] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P6_D2].content
   limit: do 120 znaków
   EN: The [Reward Exchange]'s open duration is shown here.
   PL: W oknie [Wymiany nagród] widnieje okres odbioru nagród.
339. [Samouczek i wskazówki [TutoEvent5501_P7_T1] — tekst] 거대한 장식 꾸러미
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P7_T1].content
   limit: do 120 znaków
   EN: Huge Trinkets Sack
   PL: Wielki Worek Ozdób
340. [Samouczek i wskazówki [TutoEvent5501_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [거대한 장식 꾸러미]를 획득할 수 있습니다.\n\n획득한 [거대한 장식 꾸러미]는 [장식 꾸러미] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P7_D1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is a small chance to obtain a [Huge Trinkets Sack] upon clearing an Encounter.\n\n[Huge Trinkets Sacks] are automatically converted to 20 [Trinkets Sack].
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Wielkiego Worka Ozdób].\n\nZdobyty [Wielki Worek Ozdób] jest automatycznie zamieniany na 20 [Worków Ozdób].
341. [Samouczek i wskazówki [TutoEvent5501_P8_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P8_T1].content
   limit: do 120 znaków
   EN: Hard Difficulty
   PL: Poziom Hard
342. [Samouczek i wskazówki [TutoEvent5501_P8_D1] — tekst] 이벤트 기간 동안 20번구의 기적 Hard 난이도를 진행할 수 있습니다. 주요 이야기 6-48 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P8_D1].content
   limit: do 200 znaków
   EN: Miracle in District 20 Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 6-48.
   PL: W trakcie wydarzenia dostępny jest poziom trudności Hard Cudu w Dystrykcie 20. Odblokowuje się on po ukończeniu etapu 6-48 Głównej Opowieści.
343. [Samouczek i wskazówki [TutoEvent5501_P8_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P8_D2].content
   limit: do 120 znaków
   EN: Hard Difficulty rewards more Event currencies than the Normal Difficulty does.
   PL: Na poziomie Hard zdobędziesz więcej waluty wydarzenia niż na poziomie Normal.
344. [Samouczek i wskazówki [TutoEvent5501_P8_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P8_D3].content
   limit: do 180 znaków
   EN: You can earn first-time clear rewards, EX Clear rewards, and Chapter Progress rewards from clearing the Hard Difficulty Stages as well.
   PL: Ukończenie etapów Hard również zapewnia nagrody za pierwsze przejście, nagrody EX oraz nagrody postępu rozdziału.
345. [Samouczek i wskazówki [TutoEvent5501_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 20번구의 기적 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5501_P9_D1].content
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Samouczek i wskazówki [TutoEvent7501_P1_T1] — tekst] LCB 정기검진
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P1_T1].content
   limit: do 120 znaków
   EN: LCB Regular Check-up
   PL: Okresowe Badania LCB
347. [Samouczek i wskazówki [TutoEvent7501_P1_D1] — tekst] LCB 정기검진 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P1_D1].content
   limit: do 120 znaków
   EN: Unlocking LCB Regular Check-up
   PL: Odblokowanie Okresowych Badań LCB
348. [Samouczek i wskazówki [TutoEvent7501_P1_D2] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P1_D2].content
   limit: do 120 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter.
   PL: Wejdziesz przez baner wydarzenia w Oknie lub Jeździe.
349. [Samouczek i wskazówki [TutoEvent7501_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Samouczek i wskazówki [TutoEvent7501_P2_D1] — tekst] LCB 정기검진 이벤트 기간이 표시됩니다. 이벤트 기간 동안 LCB 정기검진 스테이지 혹은 주요 이야기 스테이지와 거울 던전을 클리어하면 [정보서류]를 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [정보서류]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P2_D1].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of LCB Regular Check-up event is shown here. During the event, you can earn [Amassed Data] by clearing Stages and Dungeons in the event and Main Story.\n\n※ However, [Amassed Data] cannot be obtained in Luxcavations.
   PL: Tutaj widnieje czas trwania wydarzenia Okresowe Badania LCB. W trakcie wydarzenia ukończenie etapów wydarzenia, etapów Głównej Opowieści lub Lustrzanych Lochów zapewnia [Akta Informacyjne].\n\n※ [Akt Informacyjnych] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
351. [Samouczek i wskazówki [TutoEvent7501_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Samouczek i wskazówki [TutoEvent7501_P3_D1] — tekst] LCB 정기검진 전투는 스토리 스테이지를 포함하여 총 13개의 스테이지와 1개의 던전으로 구성됩니다. LCB 정기검진 전투에서는 클리어 보상과 별개로 초회 보상으로 [정보서류]를 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P3_D1].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB Regular Check-up event consists of 13 stages, including story stages, and a single dungeon.\n\nEvent Encounters also offer batches of [Amassed Data] as a first-time Clear bonus.
   PL: Okresowe Badania LCB obejmują łącznie 13 etapów (wraz z fabularnymi) oraz 1 loch.\nWalki wydarzenia zapewniają dodatkowo [Akta Informacyjne] za pierwsze ukończenie (1 raz).
353. [Samouczek i wskazówki [TutoEvent7501_P3_D2] — tekst] LCB 정기검진 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [정보서류]를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P3_D2].content
   limit: do 150 znaków
   EN: You can earn considerably more [Amassed Data] from LCB Regular Check-up Stages compared to Main Story Stages.
   PL: Etapy Okresowych Badań LCB zapewniają znacznie więcej [Akt Informacyjnych] niż etapy Głównej Opowieści.
354. [Samouczek i wskazówki [TutoEvent7501_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Samouczek i wskazówki [TutoEvent7501_P4_D1] — tekst] LCB 정기검진 기간 동안 이벤트 인격, E.G.O 편성하여 스테이지, 던전을 클리어하면 [정보서류]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P4_D1].content
   limit: do 200 znaków
   EN: Having Event Identities and E.G.O from the LCB Regular Check-up event on your team increases the amount of [Amassed Data] earned from Stages and Dungeons.
   PL: Wystawienie w drużynie Tożsamości i E.G.O wydarzenia Okresowe Badania LCB zwiększa liczbę [Akt Informacyjnych] zdobywanych na etapach i w lochach.
356. [Samouczek i wskazówki [TutoEvent7501_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Samouczek i wskazówki [TutoEvent7501_P5_D1] — tekst] 획득한 [정보서류]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P5_D1].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Reward Exchange] based on the number of [Amassed Data] you have.
   PL: Wydawaj zdobyte [Akta Informacyjne] w [Wymianie nagród], aby odbierać rozmaite nagrody.
358. [Samouczek i wskazówki [TutoEvent7501_P6_T1] — tekst] [보상 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P6_T1].content
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Samouczek i wskazówki [TutoEvent7501_P6_D1] — tekst] [보상 교환] 페이지에서 각종 재화와 이벤트 배포 인격을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P6_D1].content
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Samouczek i wskazówki [TutoEvent7501_P7_T1] — tekst] 연속 전투 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P7_T1].content
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Samouczek i wskazówki [TutoEvent7501_P7_D1] — tekst] LCB 정기검진의 일부 전투는 연속 전투 방식으로 진행됩니다. 연속 전투에서는 아군이 죽더라도 정신력이 소모되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P7_D1].content
   limit: do 220 znaków
   EN: Certain Encounters in the LCB Regular Check-up event are Chain Battles. In Chain Battles, the Sinners will not lose their Sanity(SP) even if their allies are defeated.
   PL: Część walk Okresowych Badań LCB to Walki Seryjne. W Walkach Seryjnych śmierć sojusznika nie obniża Poczytalności (PP) pozostałych.
362. [Samouczek i wskazówki [TutoEvent7501_P8_T1] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P8_T1].content
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Samouczek i wskazówki [TutoEvent7501_P8_D1] — tekst] LCB 정기검진 제일 마지막에는 거울 던전이 등장하며, 입장 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P8_D1].content
   limit: do 160 znaków
   EN: A Mirror Dungeon awaits at the end of LCB Regular Check-up event. Entering this Mirror Dungeon costs Enkephalin Modules.
   PL: Na samym końcu Okresowych Badań LCB czeka loch w trybie Lustrzanych Lochów; wejście do niego zużywa Moduły Enkefaliny.
364. [Samouczek i wskazówki [TutoEvent7501_P9_T1] — tekst] 기밀서류
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P9_T1].content
   limit: do 120 znaków
   EN: Classified Data
   PL: Tajne Akta
365. [Samouczek i wskazówki [TutoEvent7501_P9_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 기밀서류를 획득할 수 있습니다. 획득한 기밀서류는 정보서류 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P9_D1].content
   limit: do 190 znaków
   EN: There is a small chance to obtain Classified Data upon clearing an Encounter. Classified Data are automatically converted to 20 Amassed Data.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie Tajnych Akt. Zdobyte Tajne Akta są automatycznie zamieniane na 20 Akt Informacyjnych.
366. [Samouczek i wskazówki [TutoEvent7501_P10_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 LCB 정기검진 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7501_P10_D1].content
   limit: do 260 znaków
   EN: Even after the event fully ends, you will be able to experience the LCB Regular Check-up combat Encounters and view its story at any time at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Okresowych Badań LCB możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
367. [Samouczek i wskazówki [TutoEvent5502_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Samouczek i wskazówki [TutoEvent5502_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [육참골단 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P1_D1].content
   limit: do 180 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Yield My Flesh to Claim Their Bones BokGak Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Oddam Ciało, by Złamać Ich Kości BokGak].
369. [Samouczek i wskazówki [TutoEvent5502_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Samouczek i wskazówki [TutoEvent5502_P2_D1] — tekst] 육참골단 BokGak 이벤트 기간이 표시됩니다. 이벤트 기간 동안 육참골단 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [피에 절은 검집]을 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [피에 절은 검집]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P2_D1].content
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Yield My Flesh to Claim Their Bones BokGak Event is shown here.\n\nDuring the event, you can earn [Bloodied Scabbard] by clearing Event Stages. You can also earn [Bloodied Scabbard] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Bloodied Scabbard] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Oddam Ciało, by Złamać Ich Kości BokGak. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Zakrwawione Pochwy].\n\n※ [Zakrwawionych Pochew] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
371. [Samouczek i wskazówki [TutoEvent5502_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Samouczek i wskazówki [TutoEvent5502_P3_D1] — tekst] 육참골단 BokGak 이벤트는 스토리 스테이지를 포함하여 총 11개의 스테이지와 1개의 던전으로 구성됩니다. 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [피에 절은 검집]을 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P3_D1].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yield My Flesh to Claim Their Bones BokGak Event consists of 11 stages, including story stages, and a Dungeon.\n\nSaid stages also offer batches of [Bloodied Scabbard] as a First-time Clear bonus in addition to clear rewards. (only for first-time clears of each Stage)
   PL: Wydarzenie Oddam Ciało, by Złamać Ich Kości BokGak obejmuje łącznie 11 etapów (wraz z fabularnymi) oraz 1 loch.\nWalki wydarzenia zapewniają oprócz zwykłych nagród także [Zakrwawione Pochwy] za pierwsze ukończenie każdego etapu (1 raz na walkę).
373. [Samouczek i wskazówki [TutoEvent5502_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Samouczek i wskazówki [TutoEvent5502_P4_D1] — tekst] 이벤트 기간 동안 이벤트 인격을 편성하여 스테이지와 거울 던전을 클리어하면 [피에 절은 검집]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P4_D1].content
   limit: do 160 znaków
   EN: Having Event Identities from Event on your team increases the amount of [Bloodied Scabbard] earned from Stages and Dungeons.
   PL: Wystawienie Tożsamości wydarzenia w drużynie zwiększa liczbę [Zakrwawionych Pochew] zdobywanych na etapach i w Lustrzanych Lochach.
375. [Samouczek i wskazówki [TutoEvent5502_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Samouczek i wskazówki [TutoEvent5502_P5_D1] — tekst] 획득한 [피에 절은 검집]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P5_D1].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Reward Exchange] using the [Bloodied Scabbard] you have collected.
   PL: Wydawaj zdobyte [Zakrwawione Pochwy] w [Wymianie nagród], aby odbierać rozmaite nagrody.
377. [Samouczek i wskazówki [TutoEvent5502_P6_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P6_D1].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Samouczek i wskazówki [TutoEvent5502_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P6_D2].content
   limit: do 150 znaków
   EN: You can acquire the event reward Identity, Ticket Deco, banners, and various currencies from [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia, ozdoby biletu, banery oraz rozmaite waluty.
379. [Samouczek i wskazówki [TutoEvent5502_P7_T1] — tekst] 한 서린 검집
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P7_T1].content
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Samouczek i wskazówki [TutoEvent5502_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [한 서린 검집]을 획득할 수 있습니다. 획득한 [한 서린 검집]은 [피에 절은 검집] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P7_D1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rarely, you may obtain [Resentful Scabbard] from clearing Encounters.\n\n[Resentful Scabbard] is automatically converted to 20 [Bloodied Scabbard] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Przepełnionej Żalem Pochwy].\nZdobyta [Przepełniona Żalem Pochwa] zamienia się automatycznie na 20 [Zakrwawionych Pochew].
381. [Samouczek i wskazówki [TutoEvent5502_P8_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P8_T1].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Samouczek i wskazówki [TutoEvent5502_P8_D1] — tekst] 이벤트 기간 동안 육참골단 Hard 난이도를 진행할 수 있습니다. 주요 이야기 6-48 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P8_D1].content
   limit: do 220 znaków
   EN: Yield My Flesh to Claim Their Bones Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 6-48.
   PL: W trakcie wydarzenia dostępny jest poziom trudności Hard „Oddam Ciało, by Złamać Ich Kości”. Odblokowuje się on po ukończeniu etapu 6-48 Głównej Opowieści.
383. [Samouczek i wskazówki [TutoEvent5502_P8_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P8_D2].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Samouczek i wskazówki [TutoEvent5502_P8_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P8_D3].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Samouczek i wskazówki [TutoEvent5502_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 육참골단 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent5502_P9_D1].content
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Samouczek i wskazówki [TutoRailway5_P1_T1] — tekst] 거울굴절철도 5호선
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P1_T1].content
   limit: do 120 znaków
   EN: Refraction Railway Line 5
   PL: Kolej Załamania — Linia 5
387. [Samouczek i wskazówki [TutoRailway5_P1_D1] — tekst] 입장 방법
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P1_D1].content
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Samouczek i wskazówki [TutoRailway5_P1_D2] — tekst] 활성화된 노선을 선택하여 입장합니다.\n\n거울굴절철도 입장 시에는 재화를 소모하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P1_D2].content
   (powtórzenie elementu 248 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Samouczek i wskazówki [TutoRailway5_P2_T1] — tekst] 거울굴절철도는 매우 어려운 난이도의 콘텐츠입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P2_T1].content
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Samouczek i wskazówki [TutoRailway5_P2_D1] — tekst] 이번 5호선의 경우, 입장 시 권장 사양은 인격 동기화 4단계와 레벨 50, E.G.O 환상 해석 4단계입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P2_D1].content
   limit: do 150 znaków
   EN: We recommend that you Uptie your Identities to Tier 4, level them to Level 50, and Threadspin your E.G.Os to Tier 4.
   PL: Zalecane parametry na Linii 5 to 4. stopień Synchronizacji i 50. poziom Tożsamości oraz 4. stopień Splotu Nici E.G.O.
391. [Samouczek i wskazówki [TutoRailway5_P2_D2] — tekst] 되도록이면 육성 조건을 맞춘 이후에 입장하는 것을 추천드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P2_D2].content
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Samouczek i wskazówki [TutoRailway5_P3_T1] — tekst] 5호선 역과 구간
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P3_T1].content
   limit: do 120 znaków
   EN: Line 5: Stations and Sections
   PL: Linia 5: stacje i odcinki
393. [Samouczek i wskazówki [TutoRailway5_P3_D1] — tekst] 5호선에는 총 11개의 역이 있으며, 여러 개의 역은 각 구간 별로 묶여 각각의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P3_D1].content
   limit: do 180 znaków
   EN: Refraction Railway Line 5 is composed of several Sections that tie several Stations into a single Stage. There are a total of 11 Stations.
   PL: Linia 5 liczy łącznie 11 stacji połączonych w poszczególne odcinki, z których każdy stanowi osobny etap.
394. [Samouczek i wskazówki [TutoRailway5_P3_D2] — tekst] 5호선은 세 개의 구간으로 구성된 전투 스테이지가 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P3_D2].content
   limit: do 120 znaków
   EN: There are 3 Combat Encounter Stages, each called a 'Section'.
   PL: Linia 5 składa się z trzech odcinków bojowych.
395. [Samouczek i wskazówki [TutoRailway5_P4_T1] — tekst] 구간 입장
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P4_T1].content
   limit: do 120 znaków
   EN: Entering Section
   PL: Wejście na odcinek
396. [Samouczek i wskazówki [TutoRailway5_P4_D1] — tekst] 해당 구간 클리어 시, 클리어 턴이 기록됩니다.\n\n이와 함께 제 1 구간으로부터 현재 구간까지의 각 구간별 클리어 턴이 모두 합해진 누적 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P4_D1].content
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Samouczek i wskazówki [TutoRailway5_P4_D2] — tekst] 해당 구간을 클리어하였을 때 분실물 보관소를 통해 얻을 수 있게 되는 보상이 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P4_D2].content
   limit: do 140 znaków
   EN: Below each Section, you can view the rewards for clearing that Section. Claim them at the Lost & Found.
   PL: Poniżej widnieją nagrody za ukończenie danego odcinka do odebrania w Biurze Rzeczy Znalezionych.
398. [Samouczek i wskazówki [TutoRailway5_P5_T1] — tekst] 전투 편성 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P5_T1].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Samouczek i wskazówki [TutoRailway5_P5_D1] — tekst] 5호선은 연속 전투 방식으로 진행됩니다.\n\n연속 전투에서는 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P5_D1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Refraction Railway Line 5 uses the 'Chain Battle' system.\n\nIn Chain Battles, when a Deployed unit is defeated, the Backup units will fill their spots in their own Deployment orders.
   PL: Linia 5 rozgrywana jest w trybie Walki Seryjnej.\n\nW Walce Seryjnej po śmierci uczestnika podstawowego jego miejsce zajmują rezerwowi zgodnie z ustaloną kolejnością.
400. [Samouczek i wskazówki [TutoRailway5_P5_D2] — tekst] 6명의 출격 인원과 6명의 대기 인원을 전부 설정하여야 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P5_D2].content
   limit: do 160 znaków
   EN: You can enter the Section only when you have selected both your Deployment units and the Backup units, six in each category.
   PL: Aby wejść, musisz obsadzić wszystkich 6 uczestników podstawowych oraz 6 rezerwowych.
401. [Samouczek i wskazówki [TutoRailway5_P6_T1] — tekst] 인격 편성 제한
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P6_T1].content
   limit: do 120 znaków
   EN: Identity Deployment Limits
   PL: Ograniczenia składu Tożsamości
402. [Samouczek i wskazówki [TutoRailway5_P6_D1] — tekst] 5호선에서는 1구간과 2구간을 동일한 인격으로 도전할 수 없습니다.\n각 구간 별로 도전할 인격을 각각 지정해야합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P6_D1].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Line 5, you cannot use the same team to challenge both Section 1 and Section 2.\nEach Section needs a different team of Identities.
   PL: Na Linii 5 nie możesz użyć tych samych Tożsamości na Odcinku 1 oraz Odcinku 2.\nDla każdego z tych odcinków należy wyznaczyć osobną drużynę Tożsamości.
403. [Samouczek i wskazówki [TutoRailway5_P6_D2] — tekst] 3구간에서는 인격 제한이 적용되지 않으며, 자유롭게 인격을 선택하여 편성할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P6_D2].content
   limit: do 160 znaków
   EN: This Identity restriction does not apply to Section 3, however, and you can freely select any Identity to be deployed.
   PL: Na Odcinku 3 ograniczenie Tożsamości nie obowiązuje — możesz swobodnie wybrać dowolne Tożsamości do składu.
404. [Samouczek i wskazówki [TutoRailway5_P7_T1] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P7_T1].content
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Samouczek i wskazówki [TutoRailway5_P7_D1] — tekst] 보유한 인격과 E.G.O를 편성하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P7_D1].content
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Samouczek i wskazówki [TutoRailway5_P7_D2] — tekst] 인격의 레벨을 올리거나 동기화 단계 상승, E.G.O 환상 해석 단계 상승 시, 진행 중인 거울굴절철도에도 변경된 내용이 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P7_D2].content
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Samouczek i wskazówki [TutoRailway5_P7_D3] — tekst] 대기 인원에게는 시작 정신력 버프가 추가로 적용되며, 편성 순서가 늦을 수록 시작 정신력 값이 높아집니다.\n\n빼기 코인을 사용하는 인격의 경우에는 시작 정신력 버프가 음수값으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P7_D3].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Backup units receive Starting SP buffs, and Backup units further back in the Deployment order receive greater Starting SP buffs.\n\nMinus Coin Identities receive negative Starting SP buffs.
   PL: Rezerwowi otrzymują premię początkowych PP — im dalsze miejsce w kolejności rozstawienia, tym wyższa wartość początkowych PP.\n\nW przypadku Tożsamości z Monetami Ujemnymi premia początkowych PP ma wartość ujemną.
408. [Samouczek i wskazówki [TutoRailway5_P8_T1] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P8_T1].content
   limit: do 120 znaków
   EN: Combat
   PL: Walka
409. [Samouczek i wskazówki [TutoRailway5_P8_D1] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.\n하나의 구간에서 기록되는 최대 턴 수는 100턴이며, 한 스테이지 내에서 턴 수가 100을 초과할 경우에는 패배한 것으로 적용됩니다
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P8_D1].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every battle in the Refraction Railway will allow you to directly match ally skills against enemy skills.\nThe highest Turn Count that can be recorded in each Section is 100 Turns. If your Turn Count goes beyond 100 Turns in a single Stage, the Encounter will end in defeat.
   PL: Wszystkie walki odbywają się w trybie starcia skupionego, w którym bezpośrednio kierujesz umiejętności sojuszników przeciw wrogom.\nMaksymalna zapisywana liczba tur na odcinek wynosi 100 — przekroczenie 100 tur na jednym etapie oznacza porażkę.
410. [Samouczek i wskazówki [TutoRailway5_P9_T1] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P9_T1].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Samouczek i wskazówki [TutoRailway5_P9_D1] — tekst] 5호선에서는 각 구간별 마지막 웨이브 보스를 제외한 모든 적의 적 정보가 공개되어있습니다. 공략에 알맞은 인격과 E.G.O를 편성하여 전투를 진행하세요.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P9_D1].content
   limit: do 270 znaków
   EN: Save for the Boss enemy of the final waves of each Section, all enemy info will be unlocked for viewing from the start. Prepare the appropriate strategy, Identity, and E.G.O loadout based on this information.
   PL: Na Linii 5 informacje o wszystkich wrogach oprócz bossów ostatniej fali każdego odcinka są od razu jawne. Dobierz odpowiednią strategię, Tożsamości oraz E.G.O.
412. [Samouczek i wskazówki [TutoRailway5_P9_D2] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P9_D2].content
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Samouczek i wskazówki [TutoRailway5_P9_D3] — tekst] 5호선에서는 전투 중 재도전하거나 포기하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P9_D3].content
   limit: do 130 znaków
   EN: In Line 5, the updated Observation Level will be saved even if you give up or retry mid-Encounter.
   PL: Na Linii 5 zaktualizowane wpisy Kompendium zostają zapisane nawet przy ponowieniu lub poddaniu walki.
414. [Samouczek i wskazówki [TutoRailway5_P10_T1] — tekst] 전투 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P10_T1].content
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Samouczek i wskazówki [TutoRailway5_P10_D1] — tekst] 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P10_D1].content
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Samouczek i wskazówki [TutoRailway5_P10_D2] — tekst] 대기 인원이 출격 인원으로 전환되면, 적용 중인 서포트 패시브가 전투 패시브로 변경됩니다.\n\n출격 인원이 사망한 경우, 적용 중인 전투 패시브가 서포트 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P10_D2].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Samouczek i wskazówki [TutoRailway5_P11_T1] — tekst] 전투 - 이어지는 의지
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P11_T1].content
   limit: do 120 znaków
   EN: Combat - Lasting Determination
   PL: Walka — Dziedziczona Wola
418. [Samouczek i wskazówki [TutoRailway5_P11_D1] — tekst] 5호선에서는 인격 사망 시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻으며, 기존 연속 전투와 같이 다른 아군의 정신력이 감소하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P11_D1].content
   limit: do 270 znaków
   EN: In Line 5, when an Identity is killed, they release E.G.O resources based on the ranks and Affinities of their Base Attack Skills. And just like in Chain Encounters, their deaths will not reduce other allies' SP.
   PL: Na Linii 5 śmierć Tożsamości zapewnia zasoby E.G.O odpowiadające grzechom jej podstawowych umiejętności ataku w liczbie równej ich randze, a podobnie jak w Walkach Seryjnych nie obniża PP pozostałych sojuszników.
419. [Samouczek i wskazówki [TutoRailway5_P12_T1] — tekst] 5호선에 등장하는 일부 적들에게는 편성 순서가 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P12_T1].content
   limit: do 120 znaków
   EN: Certain enemies in Line 5 will gain certain effects based on their Deployment orders.
   PL: Niektórzy wrogowie na Linii 5 podlegają efektom kolejności rozstawienia.
420. [Samouczek i wskazówki [TutoRailway5_P13_T1] — tekst] 전투 - 버프와 고난
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P13_T1].content
   limit: do 120 znaków
   EN: Combat - Buffs & Trials
   PL: Walka — wzmocnienia i Próby
421. [Samouczek i wskazówki [TutoRailway5_P13_D1] — tekst] 구간 내 1개의 웨이브(역)을 클리어하면 버프와 고난을 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P13_D1].content
   limit: do 130 znaków
   EN: Clearing a wave(Station) within a Section will bring you to the Buffs & Trials selection menu.
   PL: Po ukończeniu 1 fali (stacji) w ramach odcinka przechodzisz do wyboru wzmocnień oraz Prób.
422. [Samouczek i wskazówki [TutoRailway5_P13_D2] — tekst] 아군에게 유리한 버프와, 적에게 유리한 고난을 같이 선택하게 되며, 선택한 버프/고난은 5호선을 도전하는 동안 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P13_D2].content
   limit: do 220 znaków
   EN: Here, you will be selecting a mix of Buffs and Trials with positive effects for allies and enemies both. Any Buffs and Trials selected here will persist throughout Line 5.
   PL: Wybierasz jednocześnie wzmocnienie korzystne dla sojuszników oraz Próbę korzystną dla wrogów; wybrane efekty utrzymują się przez całe wyzwanie Linii 5.
423. [Samouczek i wskazówki [TutoRailway5_P14_T1] — tekst] 클리어 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P14_T1].content
   limit: do 120 znaków
   EN: Clear Info
   PL: Informacje o ukończeniu
424. [Samouczek i wskazówki [TutoRailway5_P14_D1] — tekst] 각 구간을 클리어한 후, 클리어 정보 창에서 자신이 얻은 버프와 고난, 전투 참여 인격 등의 통계를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P14_D1].content
   limit: do 190 znaków
   EN: After clearing each Section, you can view statistics such as the obtained Buffs, Trials, and participating Identities in the Clear Info menu.
   PL: Po ukończeniu każdego odcinka w oknie informacji o ukończeniu sprawdzisz zdobyte wzmocnienia i Próby, statystyki uczestniczących Tożsamości i więcej.
425. [Samouczek i wskazówki [TutoRailway5_P15_T1] — tekst] 구간 클리어 이후 남은 E.G.O 자원은 다음 구간에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P15_T1].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a Section can be carried over to the next Section.
   PL: Zasoby E.G.O pozostałe po ukończeniu odcinka można wykorzystać na następnym odcinku.
426. [Samouczek i wskazówki [TutoRailway5_P16_T1] — tekst] 아군이 모두 전멸하였다면 입장 화면으로 돌아가 편성 순서를 다시 설정하거나 현재 전투를 즉시 재도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P16_T1].content
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Samouczek i wskazówki [TutoRailway5_P17_T1] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P17_T1].content
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Samouczek i wskazówki [TutoRailway5_P17_D1] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P17_D1].content
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Samouczek i wskazówki [TutoRailway5_P17_D2] — tekst] 특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P17_D2].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [Samouczek i wskazówki [TutoRailway5_P18_T1] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P18_T1].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Samouczek i wskazówki [TutoRailway5_P18_D1] — tekst] 거울굴절철도 5호선 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P18_D1].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 5 banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 5.
432. [Samouczek i wskazówki [TutoRailway5_P18_D2] — tekst] 배너를 획득하면 제일 좋은 기록의 누적 턴 수가 배너에 표기됩니다.\n누적 턴 수가 감소하면 배너의 누적 턴 수가 갱신됩니다. 누적 턴 수가 동일한 경우, 최신 클리어 기록의 턴 수로 갱신됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P18_D2].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once you obtain a Banner, the Turn Count of your best record for each Section and total turns will be displayed on it.\nMaking a new best record in total turn count will update the Turn Count on your banner. If there are records with the same number of total turns, it will display the more recent record.
   PL: Po zdobyciu baneru widnieje na nim łączna liczba tur z twojego najlepszego rekordu.\nZmniejszenie łącznej liczby tur zaktualizuje zapis na banerze. W razie równej łącznej liczby tur zapisywany jest najnowszy rekord.
433. [Samouczek i wskazówki [TutoRailway5_P19_T1] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P19_T1].content
   (powtórzenie elementu 202 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
434. [Samouczek i wskazówki [TutoRailway5_P19_D1] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P19_D1].content
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Samouczek i wskazówki [TutoRailway5_P19_D2] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.\n\n이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P19_D2].content
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Samouczek i wskazówki [TutoRailway5_P20_T1] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P20_T1].content
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Samouczek i wskazówki [TutoRailway5_P20_D1] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P20_D1].content
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Samouczek i wskazówki [TutoRailway5_P20_D2] — tekst] 기록이 20개를 넘어갈 경우에는 누적 턴 수가 많은 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway5_P20_D2].content
   (powtórzenie elementu 207 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Samouczek i wskazówki [TutoEvent7502_P1_T1] — tekst] 심야청소
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P1_T1].content
   limit: do 120 znaków
   EN: Nocturnal Sweeping
   PL: Nocne Sprzątanie
440. [Samouczek i wskazówki [TutoEvent7502_P1_D1] — tekst] 심야청소 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P1_D1].content
   limit: do 120 znaków
   EN: Unlocking Nocturnal Sweeping
   PL: Odblokowanie Nocnego Sprzątania
441. [Samouczek i wskazówki [TutoEvent7502_P1_D2] — tekst] [심야청소]는 주요 이야기의 7.5-14를 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P1_D2].content
   limit: do 210 znaków
   EN: The [Nocturnal Sweeping] page opens after clearing Stage 7.5-14 of the Main Story. You may enter the event page via the banner on the Window or the Drive menu.
   PL: [Nocne Sprzątanie] odblokowuje się po ukończeniu etapu 7.5-14 Głównej Opowieści. Wejdziesz do niego przez baner wydarzenia w Oknie lub Jeździe.
442. [Samouczek i wskazówki [TutoEvent7502_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Samouczek i wskazówki [TutoEvent7502_P2_D1] — tekst] 심야청소 이벤트 기간이 표시됩니다. 이벤트 기간 동안 심야청소 스테이지 혹은 주요 이야기 스테이지와 거울 던전을 클리어하면 [청소부 액체 연료통]을 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도, 거울던전 평행중첩 모드(6층 이상)에서는 [청소부 액체 연료통]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P2_D1].content
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Nocturnal Sweeping event is shown here. During the event, you can earn [Sweeper Fuel Cylinder] by clearing Stages and Dungeons in the event and Main Story, or the Mirror Dungeon\n\n※ However, [Sweeper Fuel Cylinder] cannot be obtained in Luxcavations and in Mirror Dungeon Parallel Superposition Mode (F6 or higher).
   PL: Tutaj widnieje czas trwania wydarzenia Nocne Sprzątanie. W trakcie wydarzenia ukończenie etapów Nocnego Sprzątania, etapów Głównej Opowieści lub Lustrzanych Lochów zapewnia [Kanistry Płynnego Paliwa Sprzątacza].\n\n※ [Kanistrów Płynnego Paliwa Sprzątacza] nie można zdobyć w Lochach Wydobywczych, Kolei Załamania ani w Trybie Superpozycji Równoległej Lustrzanych Lochów (piętro 6+).
444. [Samouczek i wskazówki [TutoEvent7502_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Samouczek i wskazówki [TutoEvent7502_P3_D1] — tekst] 심야청소 전투는 스토리 스테이지를 포함하여 총 12개의 스테이지로 구성됩니다. 심야청소 전투에서는 클리어 보상과 별개로 초회 보상으로 [청소부 액체 연료통]을 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P3_D1].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Nocturnal Sweeping consists of 12 Stages, including story Stages.\nSaid Stages also offer batches of [Sweeper Fuel Cylinder] as a first-time EX Clear bonus.
   PL: Nocne Sprzątanie obejmuje łącznie 12 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Kanistry Płynnego Paliwa Sprzątacza] za pierwsze ukończenie (1 raz).
446. [Samouczek i wskazówki [TutoEvent7502_P3_D2] — tekst] 심야청소 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [청소부 액체 연료통]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P3_D2].content
   limit: do 150 znaków
   EN: You can earn considerably more [Sweeper Fuel Cylinder] from Nocturnal Sweeping Stages compared to Main Story Stages.
   PL: Etapy Nocnego Sprzątania zapewniają znacznie więcej [Kanistrów Płynnego Paliwa Sprzątacza] niż etapy Głównej Opowieści.
447. [Samouczek i wskazówki [TutoEvent7502_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Samouczek i wskazówki [TutoEvent7502_P4_D1] — tekst] 심야청소 기간 동안 이벤트 인격을 편성하여 스테이지, 던전을 클리어하면 [청소부 액체 연료통]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P4_D1].content
   limit: do 200 znaków
   EN: Having Event Identities from the Nocturnal Sweeping event on your team increases the amount of [Sweeper Fuel Cylinder] earned from Stages and Dungeons.
   PL: Wystawienie w drużynie Tożsamości wydarzenia Nocne Sprzątanie zwiększa liczbę [Kanistrów Płynnego Paliwa Sprzątacza] zdobywanych na etapach i w lochach.
449. [Samouczek i wskazówki [TutoEvent7502_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Samouczek i wskazówki [TutoEvent7502_P5_D2] — tekst] 획득한 [청소부 액체 연료통]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P5_D2].content
   limit: do 140 znaków
   EN: You can redeem various rewards from [Reward Exchange] by spending the [Sweeper Fuel Cylinder] you collected.
   PL: Wydawaj zdobyte [Kanistry Płynnego Paliwa Sprzątacza] w [Wymianie nagród], aby odbierać rozmaite nagrody.
451. [Samouczek i wskazówki [TutoEvent7502_P6_D1] — tekst] [보상 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P6_D1].content
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Samouczek i wskazówki [TutoEvent7502_P6_D2] — tekst] [보상 교환] 페이지에서 각종 재화와 이벤트 배포 인격을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P6_D2].content
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Samouczek i wskazówki [TutoEvent7502_P7_T1] — tekst] 연속 전투 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P7_T1].content
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Samouczek i wskazówki [TutoEvent7502_P7_D1] — tekst] 심야청소의 전투는 연속 전투 방식으로 진행됩니다. 연속 전투에서는 아군이 죽더라도 정신력이 소모되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P7_D1].content
   limit: do 210 znaków
   EN: Encounters in the Nocturnal Sweeping event are Chain Battles. In Chain Battles, the Sinners will not lose their Sanity(SP) even if their allies are defeated.
   PL: Walki Nocnego Sprzątania to Walki Seryjne. W Walkach Seryjnych śmierć sojusznika nie obniża Poczytalności (PP) pozostałych.
455. [Samouczek i wskazówki [TutoEvent7502_P8_T1] — tekst] 특대형 액체 연료통
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P8_T1].content
   limit: do 120 znaków
   EN: [Sweeper Fuel Tank]
   PL: Wielki Zbiornik Płynnego Paliwa
456. [Samouczek i wskazówki [TutoEvent7502_P8_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 특대형 액체 연료통을 획득할 수 있습니다. 획득한 특대형 액체 연료통은 청소부 액체 연료통 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P8_D1].content
   limit: do 210 znaków
   EN: There is a small chance to obtain a [Sweeper Fuel Tank] upon clearing an Encounter. [Sweeper Fuel Tank] are automatically converted to 20 [Sweeper Fuel Cylinder].
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie Wielkiego Zbiornika Płynnego Paliwa, który automatycznie zamienia się na 20 Kanistrów Płynnego Paliwa Sprzątacza.
457. [Samouczek i wskazówki [TutoEvent7502_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 심야청소 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7502_P9_D1].content
   limit: do 240 znaków
   EN: Even after the event fully ends, you will be able to experience the Nocturnal Sweeping combat Encounters and view its story anytime at Drive - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Nocnego Sprzątania możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
458. [Samouczek i wskazówki [TutoFormation_P1_T1] — tekst] 수감자 (편성)
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P1_T1].content
   limit: do 120 znaków
   EN: Sinners (Team)
   PL: Grzesznicy (Skład)
459. [Samouczek i wskazówki [TutoFormation_P1_D1] — tekst] 림버스 컴퍼니에 소속된 수감자 12명의 인격을 조합하여 다양한 편성을 만들 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P1_D1].content
   limit: do 120 znaków
   EN: You can configure various Teams from your 12 Limbus Company Sinners and their Identities.
   PL: Łącz Tożsamości 12 Grzeszników Limbus Company, aby tworzyć różnorodne drużyny.
460. [Samouczek i wskazówki [TutoFormation_P1_T2] — tekst] 편성 편집
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P1_T2].content
   limit: do 120 znaków
   EN: Edit Team
   PL: Edycja składu
461. [Samouczek i wskazówki [TutoFormation_P1_D2] — tekst] 수감자 창에서 인격 초상화를 선택하면, 해당 수감자의 인격, E.G.O 목록이 등장합니다. 이를 통해 편성을 편집할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P1_D2].content
   limit: do 190 znaków
   EN: In 'Sinners' window, selecting a Sinner's Identity portrait will show a list of their Identities and E.G.O. You can change your Team from there.
   PL: Kliknięcie portretu Tożsamości w oknie Grzeszników otwiera listę Tożsamości oraz E.G.O danego Grzesznika, pozwalając edytować skład.
462. [Samouczek i wskazówki [TutoFormation_P1_D3] — tekst] 우측에 있는 전체 인격 또는 전체 E.G.O 버튼을 선택하면, 모든 수감자의 인격, E.G.O 목록이 등장하여 편성을 더욱 쉽게 편집할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P1_D3].content
   limit: do 220 znaków
   EN: Select the "All Identities" or "All E.G.O" button on the right to view the full list of Identities and E.G.O for all Sinners, making it easier to design your Team loadout.
   PL: Wybierz przycisk „Wszystkie Tożsamości” lub „Wszystkie E.G.O” po prawej stronie, aby wyświetlić pełną listę dla wszystkich Grzeszników i łatwiej edytować skład.
463. [Samouczek i wskazówki [TutoFormation_P2_T1] — tekst] 전투 편성 창
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_T1].content
   limit: do 120 znaków
   EN: Deployment Menu
   PL: Okno wyboru uczestników walki
464. [Samouczek i wskazówki [TutoFormation_P2_D1] — tekst] 보통의 편성 창에서는 인격의 초상화 영역 전체가 편성 편집 영역에 해당하지만, 각종 전투 콘텐츠에서 편성 창이 표시되는 경우에는 해당 영역이 다음과 같이 두 부분으로 나누어집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D1].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In normal Team loadout menus, clicking anywhere on each Identity's portrait loads into the "Edit Team" menu.\nHowever, in battle encounter Team menus, the Identity's portrait will be divided into the following two areas.
   PL: W zwykłym oknie składu cały obszar portretu Tożsamości służy do edycji drużyny,\nnatomiast w oknie przygotowania do walki portret dzieli się na dwie poniższe części.
465. [Samouczek i wskazówki [TutoFormation_P2_D2] — tekst] 초상화 상단 영역을 선택할 경우에는 앞에서 설명한 편성 편집 기능과 동일하게 동작하여, 해당 수감자의 인격, E.G.O 목록을 확인하고 교체할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D2].content
   limit: do 200 znaków
   EN: Selecting the upper part of the portrait loads into the "Edit Team" menu, where you can view and swap out the Identities and E.G.O of the selected Sinner.
   PL: Górna część portretu działa jak edycja składu — pozwala przejrzeć oraz wymienić Tożsamości i E.G.O wybranego Grzesznika.
466. [Samouczek i wskazówki [TutoFormation_P2_D3] — tekst] 초상화 하단 영역은 전투 참가 인격 선택 기능으로, 이를 선택할 경우, 해당 인격이 이번 전투에 참가하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D3].content
   limit: do 160 znaków
   EN: Selecting the lower part of the portrait Deploys the Sinner, which means that the Sinner will be taking part in the battle.
   PL: Dolna część portretu służy do wyboru uczestników walki — jej kliknięcie wystawia daną Tożsamość do bieżącego starcia.
467. [Samouczek i wskazówki [TutoFormation_P2_D4] — tekst] 우하단에는 전투에 참여할 수 있는 최대 인원 수가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D4].content
   limit: do 130 znaków
   EN: This area on the bottom right shows the total number of Deployable Identities for this battle.
   PL: W prawym dolnym rogu wyświetlana jest maksymalna liczba uczestników tej walki.
468. [Samouczek i wskazówki [TutoFormation_P2_D5] — tekst] 편성을 변경할 수 없는 특정 전투 콘텐츠에서는 인격 초상화 영역 전체가 전투 참가 인격 선택 기능으로 동작합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D5].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You will not be able to edit your Team in certain battle encounters, however.\nIn those cases, selecting anywhere on a Sinner's Identity portrait will deploy that Identity to battle.
   PL: W niektórych trybach bojowych, w których nie można zmieniać składu,\ncały obszar portretu Tożsamości służy do wyboru uczestników walki.
469. [Samouczek i wskazówki [TutoFormation_P2_T2] — tekst] 대기 인원 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_T2].content
   (powtórzenie elementu 321 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Samouczek i wskazówki [TutoFormation_P2_D6] — tekst] 일반적인 전투에서는 전투 참가 인격을 설정할 때, 우하단의 총 전투 인원보다 더 많은 인원을 선택할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D6].content
   limit: do 150 znaków
   EN: In normal battles, you cannot Deploy more Sinners than the "Participant Limit" indicated in the bottom right corner.
   PL: W standardowej walce nie możesz wybrać więcej uczestników niż limit wskazany w prawym dolnym rogu.
471. [Samouczek i wskazówki [TutoFormation_P2_D7] — tekst] 단, 해당 전투가 연속 전투일 경우에는 전투 참가 인원 이외에도 '대기 인원'을 선택할 수 있습니다.\n\n전투 중 전투 참가 인원이 사망하면, 대기 인원이 그 자리를 대신하여 전투에 참가합니다.\n\n연속 전투는 편성에서 선택한 모든 인원(전투 참가 인원, 대기 인원)이 사망할 때까지 전투에서 패배하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D7].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: However, in Chain Battles, you can deploy 'Backup Units' in addition to participating units.\n\nWhen a unit is defeated mid-battle, a Backup Unit will substitute in to fill their place.\n\nIn Chain Battles, the battle will not end in defeat until all units selected for the battle encounter(both participating units and backup units) are defeated.
   PL: Jeśli jednak jest to Walka Seryjna, oprócz uczestników podstawowych możesz wybrać także „jednostki rezerwowe”.\n\nGdy uczestnik podstawowy zginie w trakcie walki, jego miejsce zajmuje rezerwowy.\n\nW Walce Seryjnej nie przegrywasz, dopóki nie polegną wszystkie wybrane jednostki (zarówno podstawowe, jak i rezerwowe).
472. [Samouczek i wskazówki [TutoFormation_P2_D8] — tekst] 전투 참가 인원이 사망하였을 때, 대기 인원은 편성 순서에 따라 등장합니다.\n\n대기 인원이 전투에 참여할 때 편성 순서에 따른 시작 정신력 값만큼 해당 캐릭터의 정신력이 회복됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D8].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a participating unit is killed, Backup units will be substituted into the field in the order of their Deployment.\n\nWhen the Backup units substitute into the battle, they enter with bonus SP based on the starting SP values defined by their deployment order.
   PL: Gdy uczestnik podstawowy polegnie, rezerwowi wkraczają do walki zgodnie z kolejnością rozstawienia.\n\nWchodzący rezerwowy odzyskuje PP w liczbie odpowiadającej premii początkowych PP wynikającej z jego kolejności rozstawienia.
473. [Samouczek i wskazówki [TutoFormation_P2_D9] — tekst] 일부 연속 전투에서는 대기 인원이 전투에 참가할 때 부가적인 효과를 얻을 수 있습니다.\n\n이를 활용하여 전략적으로 편성 순서를 정하는 것이 전투에 유리합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D9].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Certain Chain Battles may give additional buffs for Backup units.\n\nPlease experiment with Deployment orders and strategize prior to entering Chain Battles to gain an edge.
   PL: W niektórych Walkach Seryjnych wchodzący rezerwowi zyskują dodatkowe efekty.\n\nWarto wykorzystać to i strategicznie ustalić kolejność rozstawienia.
474. [Samouczek i wskazówki [TutoFormation_P2_T3] — tekst] 대기 해제
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_T3].content
   limit: do 120 znaków
   EN: Substitution
   PL: Wejście Rezerwy
475. [Samouczek i wskazówki [TutoFormation_P2_D10] — tekst] 연속 전투에서는 아군이 사망하더라도 기본 정신력 증감 조건으로 인해 정신력이 감소하지 않습니다.\n\n전투 중 일부 인원이 사망했다면, 현재 편성 순서가 가장 빠른 대기 인원이 그 자리를 대신하여 전투에 참가합니다.\n이를 <대기 해제>라고 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D10].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Chain Battles, SP loss due to ally death listed in the 'Base factors increasing/decreasing Sanity' will not activate.\n\nIf an ally is defeated mid-Encounter, a Backup Unit with the earliest Deployment order will replace them.\nThis is called <Substitution> or <Substitute>.
   PL: W Walce Seryjnej śmierć sojusznika nie powoduje utraty PP z podstawowych warunków zmiany Poczytalności.\n\nGdy uczestnik zginie w walce, zastępuje go rezerwowy o najniższym numerze rozstawienia.\nNazywa się to „Wejściem Rezerwy”.
476. [Samouczek i wskazówki [TutoFormation_P2_D11] — tekst] 사망한 인격의 전투 패시브는 서포트 패시브로 전환됩니다.\n\n대기 해제된 인격의 서포트 패시브는 전투 패시브로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D11].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a Deployed unit is defeated, its Support Passive will activate instead of its Combat Passive.\n\nWhen a Backup unit Substitutes in, its Combat Passive will activate instead of its Support Passive.
   PL: Pasywka bojowa poległej Tożsamości zamienia się w pasywkę wsparcia.\n\nPasywka wsparcia wchodzącej Tożsamości rezerwowej zamienia się w pasywkę bojową.
477. [Samouczek i wskazówki [TutoFormation_P2_T4] — tekst] 적 현황
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_T4].content
   limit: do 120 znaków
   EN: Enemy Count
   PL: Stan wrogów
478. [Samouczek i wskazówki [TutoFormation_P2_D12] — tekst] 연속 전투에서는 기존의 WAVE UI에서 전투에 등장하는 적의 수와 처치한 적의 수가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D12].content
   limit: do 180 znaków
   EN: In Chain Battles, the indicator that shows the number of WAVEs shows total number of enemies and the number of defeated enemies instead.
   PL: W Walce Seryjnej w miejscu dotychczasowego wskaźnika fal (WAVE) widnieje łączna liczba wrogów w walce oraz liczba pokonanych wrogów.
479. [Samouczek i wskazówki [TutoFormation_P2_D13] — tekst] 다만, 전투 중 특정 조건에 의해 생성되는 적은 해당 UI에 표시되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P2_D13].content
   limit: do 150 znaków
   EN: However, this indicator does not take into account the extra enemies that are summoned due to certain conditions.
   PL: Dodatkowi wrogowie przyzywani w trakcie walki po spełnieniu określonych warunków nie są jednak uwzględniani na tym wskaźniku.
480. [Samouczek i wskazówki [TutoFormation_P3_T1] — tekst] 인격 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P3_T1].content
   limit: do 120 znaków
   EN: Identity Info
   PL: Informacje o Tożsamości
481. [Samouczek i wskazówki [TutoFormation_P3_D1] — tekst] 편성 창에서 인격 초상화를 길게 선택할 경우, 인격 정보 창이 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P3_D1].content
   limit: do 120 znaków
   EN: Select and hold an Identity portrait to view the selected Identity's detailed information.
   PL: Przytrzymanie portretu Tożsamości w oknie składu otwiera okno informacji o Tożsamości.
482. [Samouczek i wskazówki [TutoFormation_P3_D2] — tekst] 인격 정보 창에서는 해당 인격과 장착한 E.G.O에 대한 상세한 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P3_D2].content
   limit: do 160 znaków
   EN: In the detailed Identity info menu, you can view more information about the selected Identity and any of its equipped E.G.O.
   PL: Sprawdzisz w nim szczegółowe dane o wybranej Tożsamości oraz wyposażonych przez nią E.G.O.
483. [Samouczek i wskazówki [TutoFormation_P4_T1] — tekst] 아나운서 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P4_T1].content
   limit: do 120 znaków
   EN: Select Announcer
   PL: Wybór Komentatora
484. [Samouczek i wskazówki [TutoFormation_P4_D1] — tekst] 좌측의 아나운서 버튼을 선택하면 아나운서 목록이 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P4_D1].content
   limit: do 120 znaków
   EN: Select the Announcer button on the left to view the list of Announcers.
   PL: Kliknij przycisk Komentatora po lewej stronie, aby otworzyć listę Komentatorów.
485. [Samouczek i wskazówki [TutoFormation_P4_D2] — tekst] 아나운서는 전투의 상황을 보고하고 전달하는 역할을 합니다. 이곳에서 전투 중에 사용할 아나운서를 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P4_D2].content
   limit: do 140 znaków
   EN: Announcers relay information regarding the flow of battle. You can change the equipped Announcer here.
   PL: Komentatorzy relacjonują przebieg bitwy. Tutaj możesz zmienić Komentatora używanego podczas walk.
486. [Samouczek i wskazówki [TutoFormation_P4_D3] — tekst] 아나운서 하단의 돋보기 버튼을 선택하면 해당 아나운서의 상황별 대사를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P4_D3].content
   limit: do 140 znaków
   EN: Select the magnifier icon at the bottom of each Announcer to view their voicelinces for each situation.
   PL: Kliknij ikonę lupy u dołu Komentatora, aby przejrzeć jego kwestie głosowe dla poszczególnych sytuacji.
487. [Samouczek i wskazówki [TutoFormation_P5_T1] — tekst] 편성 이름
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P5_T1].content
   limit: do 120 znaków
   EN: Team Names
   PL: Nazwa drużyny
488. [Samouczek i wskazówki [TutoFormation_P5_D1] — tekst] 제시된 키워드를 조합하여 편성 이름을 정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P5_D1].content
   limit: do 120 znaków
   EN: Select from the list of keywords to choose a name for your Team loadout.
   PL: Możesz nadać nazwę drużynie, łącząc proponowane słowa kluczowe.
489. [Samouczek i wskazówki [TutoFormation_P5_D2] — tekst] 편성은 최대 20개까지 만들 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P5_D2].content
   limit: do 120 znaków
   EN: You can create up to 20 Teams.
   PL: Możesz utworzyć maksymalnie 20 drużyn.
490. [Samouczek i wskazówki [TutoFormation_P6_T1] — tekst] 편성 상세
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P6_T1].content
   limit: do 120 znaków
   EN: Team Details
   PL: Szczegóły drużyny
491. [Samouczek i wskazówki [TutoFormation_P6_D1] — tekst] 상세 버튼 선택 시, 편성에 포함된 모든 인격이 보유한 스킬의 공격 유형, 죄악 속성과 장착 중인 E.G.O 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P6_D1].content
   limit: do 190 znaków
   EN: Select the detailed info button here to view the following information: All Identities' Skill Attack Types, Sin Affinities, and equipped E.G.O.
   PL: Kliknij przycisk szczegółów, aby sprawdzić typy ataków umiejętności, grzechy oraz wyposażone E.G.O wszystkich Tożsamości w składzie.
492. [Samouczek i wskazówki [TutoFormation_P6_T2] — tekst] E.G.O 자원
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P6_T2].content
   limit: do 120 znaków
   EN: E.G.O Resources
   PL: Zasoby E.G.O
493. [Samouczek i wskazówki [TutoFormation_P6_D2] — tekst] 우측 패널에서는 현재 편성으로 전투에서 획득할 수 있는 E.G.O 자원의 종류와 대략적인 수량을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P6_D2].content
   limit: do 180 znaków
   EN: On the right panel, you can access the general overview for the types and amounts of E.G.O Resources your current Team can gain in battle.
   PL: Prawy panel pokazuje ogólny podgląd rodzajów oraz przybliżonej liczby zasobów E.G.O, jakie bieżąca drużyna może zdobyć w walce.
494. [Samouczek i wskazówki [TutoFormation_P6_D3] — tekst] 우측 패널 선택 시, 선택한 E.G.O 자원을 수급하는 인격과 사용하는 E.G.O 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P6_D3].content
   limit: do 150 znaków
   EN: Select the right panel to view the Identities that gain the selected E.G.O Resources and E.G.O that use them.
   PL: Kliknij prawy panel, aby zobaczyć listę Tożsamości generujących wybrany zasób E.G.O oraz E.G.O, które go zużywają.
495. [Samouczek i wskazówki [TutoFormation_P7_T1] — tekst] 편성 코드
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_T1].content
   limit: do 120 znaków
   EN: Team Codes
   PL: Kod drużyny
496. [Samouczek i wskazówki [TutoFormation_P7_D1] — tekst] 편성을 복사하여 공유하거나, 다른 코드를 붙여넣어 불러올 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_D1].content
   limit: do 120 znaków
   EN: You can copy and share the Team Code, or paste it here to load a Team loadout.
   PL: Możesz skopiować i udostępnić kod drużyny albo wkleić inny kod, aby wczytać gotowy skład.
497. [Samouczek i wskazówki [TutoFormation_P7_T2] — tekst] 편성 삭제
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_T2].content
   limit: do 120 znaków
   EN: Delete Team Loadout
   PL: Usuń skład
498. [Samouczek i wskazówki [TutoFormation_P7_D2] — tekst] 현재 선택한 편성을 초기화합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_D2].content
   limit: do 120 znaków
   EN: Reset the currently selected Team.
   PL: Resetuje bieżącą wybraną drużynę.
499. [Samouczek i wskazówki [TutoFormation_P7_T3] — tekst] 지원
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_T3].content
   limit: do 120 znaków
   EN: Support
   PL: Wsparcie
500. [Samouczek i wskazówki [TutoFormation_P7_D3] — tekst] 친구가 등록한 지원 인격을 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P7_D3].content
   limit: do 120 znaków
   EN: You can select the Support Identities that your Friends have registered here.
   PL: Tutaj możesz wybrać Tożsamości wsparcia zarejestrowane przez twoich znajomych.
501. [Samouczek i wskazówki [TutoFormation_P8_T1] — tekst] 코드 복사
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P8_T1].content
   limit: do 120 znaków
   EN: Copy Code
   PL: Kopiuj kod
502. [Samouczek i wskazówki [TutoFormation_P8_D1] — tekst] 현재 선택한 편성 코드를 복사합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P8_D1].content
   limit: do 120 znaków
   EN: Copy the Team Code for the currently selected Team loadout.
   PL: Kopiuje kod aktualnie wybranej drużyny.
503. [Samouczek i wskazówki [TutoFormation_P8_T2] — tekst] 코드 붙여넣기
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P8_T2].content
   limit: do 120 znaków
   EN: Paste Code
   PL: Wklej kod
504. [Samouczek i wskazówki [TutoFormation_P8_D2] — tekst] 복사한 편성 코드의 데이터를 불러와 현재 편성에 반영합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoFormation_P8_D2].content
   limit: do 120 znaków
   EN: Paste the copied Team Code here to equip the Team loadout.
   PL: Wczytuje dane skopiowanego kodu drużyny i nakłada je na bieżący skład.
505. [Samouczek i wskazówki [TutoIDList_P1_T1] — tekst] 인격 목록
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P1_T1].content
   limit: do 120 znaków
   EN: Identity List
   PL: Lista Tożsamości
506. [Samouczek i wskazówki [TutoIDList_P1_D1] — tekst] 편성에서 선택한 수감자의 인격 목록이 나열됩니다.\n\n인격의 등급과 동기화 단계, 레벨, 소속을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P1_D1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The selected Sinner’s Identities are shown here.\n\nYou can check their Rarity, Uptie Tier, Level, and Faction here.
   PL: Wyświetla listę Tożsamości wybranego w składzie Grzesznika.\n\nSprawdzisz tutaj rzadkość, stopień Synchronizacji, poziom oraz przynależność Tożsamości.
507. [Samouczek i wskazówki [TutoIDList_P2_T1] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P2_T1].content
   limit: do 120 znaków
   EN: Selecting Sinners
   PL: Wybór Grzesznika
508. [Samouczek i wskazówki [TutoIDList_P2_D1] — tekst] ALL 버튼을 선택하면, 모든 수감자의 인격 목록을 한 번에 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P2_D1].content
   limit: do 120 znaków
   EN: Select the "ALL" button to view the list of Identities for all Sinners at once.
   PL: Wybierz przycisk „ALL”, aby zobaczyć naraz listę Tożsamości wszystkich Grzeszników.
509. [Samouczek i wskazówki [TutoIDList_P2_D2] — tekst] 현재 편성에 포함된 인격을 다음과 같이 확인할 수 있습니다.\n\n수감자의 초상화를 선택 시, 해당 수감자의 인격 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P2_D2].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Identities that are in your current Team will be visible.\n\nSelect a Sinner's portrait to view their list of Identities.
   PL: Tożsamości wchodzące w skład bieżącej drużyny są tu odpowiednio oznaczone.\n\nKliknij portret Grzesznika, aby wyświetlić listę jego Tożsamości.
510. [Samouczek i wskazówki [TutoIDList_P2_D3] — tekst] 인격 목록 또는 E.G.O 목록으로 전환합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P2_D3].content
   limit: do 120 znaków
   EN: Toggle between Identities and E.G.O tabs here.
   PL: Przełącza widok pomiędzy listą Tożsamości a listą E.G.O.
511. [Samouczek i wskazówki [TutoIDList_P3_T1] — tekst] 상세 정보 표시
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P3_T1].content
   limit: do 120 znaków
   EN: Toggle Details
   PL: Przełącz szczegóły
512. [Samouczek i wskazówki [TutoIDList_P3_D1] — tekst] 인격이 보유한 스킬의 공격 유형, 죄악 속성과 인격의 스테이터스, 내성 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P3_D1].content
   limit: do 130 znaków
   EN: The Identities' Skill Attack Types, Sin Affinities, stat values, and Resistances can be viewed here.
   PL: Sprawdzisz tu typy ataków umiejętności, grzechy, statystyki oraz odporności Tożsamości.
513. [Samouczek i wskazówki [TutoIDList_P3_D2] — tekst] ※ E.G.O 목록에서는 해당 버튼이 비활성화 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P3_D2].content
   limit: do 120 znaków
   EN: ※ This button is deactivated when viewing the list of E.G.O.
   PL: ※ Na liście E.G.O ten przycisk jest nieaktywny.
514. [Samouczek i wskazówki [TutoIDList_P4_T1] — tekst] E.G.O 목록
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P4_T1].content
   limit: do 120 znaków
   EN: E.G.O List
   PL: Lista E.G.O
515. [Samouczek i wskazówki [TutoIDList_P4_D1] — tekst] 편성에서 선택한 수감자의 E.G.O 목록이 나열됩니다.\n\nE.G.O의 등급과 환상 해석 단계, 주 속성, 이름을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P4_D1].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The selected Sinner's E.G.O are shown here.\n\nYou can check their Rarity, Threadspinning Tier, their primary Affinity, and name here.
   PL: Wyświetla listę E.G.O wybranego w składzie Grzesznika.\n\nSprawdzisz tu klasę, stopień Splotu Nici, główny grzech oraz nazwę E.G.O.
516. [Samouczek i wskazówki [TutoIDList_P5_D1] — tekst] 인격 목록과 동일하게, ALL 버튼을 선택하면 모든 수감자의 E.G.O 목록을 한 번에 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P5_D1].content
   limit: do 120 znaków
   EN: Select the "ALL" button to view the list of E.G.O for all Sinners at once.
   PL: Podobnie jak na liście Tożsamości, przycisk „ALL” wyświetla naraz E.G.O wszystkich Grzeszników.
517. [Samouczek i wskazówki [TutoIDList_P5_D2] — tekst] 수감자의 초상화를 선택 시, 해당 수감자의 E.G.O 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P5_D2].content
   limit: do 120 znaków
   EN: Select a Sinner's portrait to view the full list of their E.G.O.
   PL: Kliknij portret Grzesznika, aby wyświetlić listę jego E.G.O.
518. [Samouczek i wskazówki [TutoIDList_P6_T1] — tekst] 편성 현황
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P6_T1].content
   limit: do 120 znaków
   EN: Team Loadout Configuration
   PL: Konfiguracja wyposażenia
519. [Samouczek i wskazówki [TutoIDList_P6_D1] — tekst] 현재 편성에서 선택한 수감자가 사용할 인격과 E.G.O를 한 번에 확인할 수 있습니다. E.G.O는 각 등급마다 하나씩 등록할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P6_D1].content
   limit: do 150 znaków
   EN: You can see the equipped Identity and E.G.O for the selected Sinner. Only one E.G.O can be equipped from each grade.
   PL: Sprawdzisz tu naraz Tożsamość oraz E.G.O wybranego Grzesznika. Dla każdej klasy można wyposażyć po jednym E.G.O.
520. [Samouczek i wskazówki [TutoIDList_P6_D2] — tekst] 편성 현황의 버튼 선택 시, 해당 칸에 등록할 수 있는 인격 목록 또는 E.G.O 목록으로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P6_D2].content
   limit: do 140 znaków
   EN: Selecting this button brings you to the list of Identities or E.G.O that can be equipped on the slot.
   PL: Kliknięcie gniazda przełącza widok na listę Tożsamości lub E.G.O, które można w nim umieścić.
521. [Samouczek i wskazówki [TutoIDList_P7_T1] — tekst] 정렬
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P7_T1].content
   limit: do 120 znaków
   EN: Sorting
   PL: Sortowanie
522. [Samouczek i wskazówki [TutoIDList_P7_D1] — tekst] 인격, E.G.O를 원하는 방식으로 정렬할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P7_D1].content
   limit: do 120 znaków
   EN: Sort the Identities and E.G.O by the following categories.
   PL: Posortuj Tożsamości oraz E.G.O według wybranego kryterium.
523. [Samouczek i wskazówki [TutoIDList_P7_T2] — tekst] 필터
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P7_T2].content
   limit: do 120 znaków
   EN: Filters
   PL: Filtry
524. [Samouczek i wskazówki [TutoIDList_P7_D2] — tekst] 인격, E.G.O의 특수한 키워드를 선택하여 원하는 인격과 E.G.O만 표시되도록 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P7_D2].content
   limit: do 130 znaków
   EN: Use these keyword filters to search for specific Identities and E.G.O that fit your criteria.
   PL: Wybierz słowa kluczowe Tożsamości i E.G.O, aby wyświetlić tylko pasujące pozycje.
525. [Samouczek i wskazówki [TutoIDList_P8_T1] — tekst] 표시할 목록 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P8_T1].content
   limit: do 120 znaków
   EN: Visibility Toggle
   PL: Widoczność listy
526. [Samouczek i wskazówki [TutoIDList_P8_D1] — tekst] 보유 선택 시, 보유 중인 인격과 E.G.O만 목록에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P8_D1].content
   limit: do 120 znaków
   EN: Selecting the "Obtained" option will show only the list of obtained Identities and E.G.O.
   PL: Wybranie opcji „Posiadane” wyświetla na liście wyłącznie posiadane Tożsamości i E.G.O.
527. [Samouczek i wskazówki [TutoIDList_P8_D2] — tekst] ALL 선택 시, 보유하지 않은 인격과 E.G.O를 포함하여 모든 인격, E.G.O가 목록에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P8_D2].content
   limit: do 120 znaków
   EN: Selecting "ALL" option will show the full list of Identities and E.G.O, obtained or not.
   PL: Wybranie opcji „ALL” wyświetla pełną listę Tożsamości i E.G.O, włącznie z nieposiadanymi.
528. [Samouczek i wskazówki [TutoIDList_P9_T1] — tekst] 지원 목록
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P9_T1].content
   limit: do 120 znaków
   EN: Support List
   PL: Lista wsparcia
529. [Samouczek i wskazówki [TutoIDList_P9_D1] — tekst] 친구가 설정해둔 지원 인격의 목록이 나열됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P9_D1].content
   limit: do 120 znaków
   EN: View the list of Support Identities registered by your friends here.
   PL: Wyświetla listę Tożsamości wsparcia ustawionych przez twoich znajomych.
530. [Samouczek i wskazówki [TutoIDList_P9_D2] — tekst] 선택 시, 친구가 설정한 인격과 E.G.O를 빌려 전투에서 사용할 수 있습니다. 단, 하나의 편성에 둘 이상의 친구 인격을 빌릴 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoIDList_P9_D2].content
   limit: do 220 znaków
   EN: Select them to borrow your friends' Identities and E.G.O for battles. However, please note that you cannot have more than 1 Support Identity in a single Team loadout.
   PL: Wybierz pozycję, aby wypożyczyć Tożsamość i E.G.O znajomego do walki. W jednej drużynie nie można jednak wypożyczyć więcej niż 1 Tożsamości znajomego.
531. [Samouczek i wskazówki [TutoEvent6511_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Samouczek i wskazówki [TutoEvent6511_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [시간살인시간 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P1_D1].content
   limit: do 140 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Timekilling Time Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Czas Zabijania Czasu BokGak].
533. [Samouczek i wskazówki [TutoEvent6511_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Samouczek i wskazówki [TutoEvent6511_P2_D1] — tekst] 시간살인시간 BokGak 이벤트 기간이 표시됩니다. 이벤트 기간 동안 시간살인시간 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [회중시계]를 획득할 수 있습니다.\n※ 단, 채광과 거울굴절철도에서는 [회중시계]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P2_D1].content
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Timekilling Time BokGak event is shown here.\n\nDuring the event, you can earn [Pocket Watch] by clearing Event Stages. You can also earn [Pocket Watch] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Pocket Watch] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Czas Zabijania Czasu BokGak. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Zegarki Kieszonkowe].\n※ [Zegarków Kieszonkowych] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
535. [Samouczek i wskazówki [TutoEvent6511_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Samouczek i wskazówki [TutoEvent6511_P3_D1] — tekst] 시간살인시간 BokGak 이벤트는 스토리 스테이지를 포함하여 총 14개의 스테이지와 1개의 던전으로 구성됩니다. 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [회중시계]를 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P3_D1].content
   limit: do 230 znaków
   EN: Timekilling Time BokGak consists of 14 stages, including story stages, and a single dungeon. Event Encounters also offer batches of [Pocket Watch] as a first-time Clear bonus.
   PL: Wydarzenie Czas Zabijania Czasu BokGak obejmuje łącznie 14 etapów (wraz z fabularnymi) oraz 1 loch. Walki wydarzenia zapewniają dodatkowo [Zegarki Kieszonkowe] za pierwsze ukończenie każdego etapu (1 raz na walkę).
537. [Samouczek i wskazówki [TutoEvent6511_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Samouczek i wskazówki [TutoEvent6511_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [회중시계]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P4_D1].content
   limit: do 190 znaków
   EN: Having Identities and E.G.O from Timekilling Time event on your team increases the amount of [Pocket Watch] earned from Stages and Mirror Dungeons.
   PL: Wystawienie w drużynie premiowanych Tożsamości i E.G.O wydarzenia zwiększa liczbę [Zegarków Kieszonkowych] zdobywanych na etapach i w Lustrzanych Lochach.
539. [Samouczek i wskazówki [TutoEvent6511_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Samouczek i wskazówki [TutoEvent6511_P5_D1] — tekst] 획득한 [회중시계]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P5_D1].content
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Samouczek i wskazówki [TutoEvent6511_P6_D1] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P6_D1].content
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Samouczek i wskazówki [TutoEvent6511_P6_D2] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P6_D2].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Samouczek i wskazówki [TutoEvent6511_P7_T1] — tekst] 회중시계 묶음
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P7_T1].content
   (powtórzenie elementu 242 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Samouczek i wskazówki [TutoEvent6511_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [회중시계 묶음]을 획득할 수 있습니다. 획득한 [회중시계 묶음]은 [회중시계] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P7_D1].content
   limit: do 210 znaków
   EN: Rarely, you may obtain [Pocket Watch Bundle] from clearing Encounters. [Pocket Watch Bundle] is automatically converted to 20 [Pocket Watch] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Pęku Zegarków Kieszonkowych], który automatycznie zamienia się na 20 [Zegarków Kieszonkowych].
545. [Samouczek i wskazówki [TutoEvent6511_P8_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P8_T1].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Samouczek i wskazówki [TutoEvent6511_P8_D1] — tekst] 이벤트 기간 동안 시간살인시간 Hard 난이도를 진행할 수 있습니다. 주요 이야기 7-36 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P8_D1].content
   limit: do 190 znaków
   EN: Timekilling Time Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 7-36.
   PL: W trakcie wydarzenia dostępny jest poziom trudności Hard Czasu Zabijania Czasu. Odblokowuje się on po ukończeniu etapu 7-36 Głównej Opowieści.
547. [Samouczek i wskazówki [TutoEvent6511_P8_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P8_D2].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Samouczek i wskazówki [TutoEvent6511_P8_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P8_D3].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Samouczek i wskazówki [TutoEvent6511_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 시간살인시간 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6511_P9_D1].content
   (powtórzenie elementu 244 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Samouczek i wskazówki [TutoEvent8501_Title] — tekst] 절차탁춘
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_Title].content
   limit: do 120 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
551. [Samouczek i wskazówki [TutoEvent8501_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [Samouczek i wskazówki [TutoEvent8501_P1_D1] — tekst] [절차탁춘]은 주요 이야기의 8-33을 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P1_D1].content
   limit: do 210 znaków
   EN: The [Spring Cultivation] page opens after clearing Stage 8-33 of the Main Story. You may enter the event page via the banner on the Window or the Drive menu.
   PL: [Wiosenny Szlif] odblokowuje się po ukończeniu etapu 8-33 Głównej Opowieści. Wejdziesz do niego przez baner wydarzenia w Oknie lub Jeździe.
553. [Samouczek i wskazówki [TutoEvent8501_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Samouczek i wskazówki [TutoEvent8501_P2_D1] — tekst] 절차탁춘 이벤트 기간이 표시됩니다. 이벤트 기간 동안 절차탁춘 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [지·용·인 기초 입문]을 획득할 수 있습니다.\n※ 단, 채광과 거울굴절철도에서는 [지·용·인 기초 입문]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P2_D1].content
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Spring Cultivation Event is shown here.\n\nDuring the event, you can earn [Intro to Zhi, Yong, Ren] by clearing Event Stages. You can also earn [Intro to Zhi, Yong, Ren] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Intro to Zhi, Yong, Ren] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Wiosenny Szlif. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Wprowadzenie do Zhi, Yong i Ren].\n※ [Wprowadzenia do Zhi, Yong i Ren] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
555. [Samouczek i wskazówki [TutoEvent8501_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Samouczek i wskazówki [TutoEvent8501_P3_D1] — tekst] 절차탁춘 이벤트는 스토리 스테이지를 포함하여 총 12개의 스테이지로 구성됩니다. 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [지·용·인 기초 입문]을 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P3_D1].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Spring Cultivation Event consists of 12 stages, including story stages.\nSaid stages also offer batches of [Intro to Zhi, Yong, Ren] as a first-time Clear bonus. (only for first-time clears of each Stage)
   PL: Wydarzenie Wiosenny Szlif obejmuje łącznie 12 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Wprowadzenie do Zhi, Yong i Ren] za pierwsze ukończenie każdego etapu (1 raz na walkę).
557. [Samouczek i wskazówki [TutoEvent8501_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Samouczek i wskazówki [TutoEvent8501_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격을 편성하여 스테이지와 거울 던전을 클리어하면 [지·용·인 기초 입문]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P4_D1].content
   limit: do 170 znaków
   EN: Having Bonus Identities on your team increases the amount of [Intro to Zhi, Yong, Ren] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości w drużynie zwiększa liczbę [Wprowadzenia do Zhi, Yong i Ren] zdobywanego na etapach i w Lustrzanych Lochach.
559. [Samouczek i wskazówki [TutoEvent8501_P5_T1] — tekst] 업적
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P5_T1].content
   limit: do 120 znaków
   EN: Achievements
   PL: Osiągnięcia
560. [Samouczek i wskazówki [TutoEvent8501_P5_D1] — tekst] 육성 중 수행할 수 있는 미션과 미션의 보상을 확인할 수 있는 [업적] 페이지로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P5_D1].content
   limit: do 180 znaków
   EN: You can enter the [Achievements] page, where you can view the list of Missions to be completed during the Cultivation and their rewards.
   PL: Przejdź na stronę [Osiągnięć], aby sprawdzić misje możliwe do wykonania podczas szkolenia oraz przypisane do nich nagrody.
561. [Samouczek i wskazówki [TutoEvent8501_P6_D1] — tekst] [업적] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P6_D1].content
   limit: do 120 znaków
   EN: The [Achievement] Page's open duration is shown here.
   PL: Na stronie [Osiągnięć] widnieje okres odbioru nagród.
562. [Samouczek i wskazówki [TutoEvent8501_P6_D2] — tekst] 미션을 완료하면 [업적]에서 [지·용·인 기초 입문]을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P6_D2].content
   limit: do 120 znaków
   EN: Complete these Missions and claim [Intro to Zhi, Yong, Ren] from the [Achievements] page.
   PL: Wykonuj misje, aby odbierać [Wprowadzenie do Zhi, Yong i Ren] w zakładce [Osiągnięcia].
563. [Samouczek i wskazówki [TutoEvent8501_P7_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P7_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Samouczek i wskazówki [TutoEvent8501_P7_D1] — tekst] 획득한 [지·용·인 기초 입문]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P7_D1].content
   limit: do 150 znaków
   EN: You can redeem various rewards from the [Reward Exchange] using the [Intro to Zhi, Yong, Ren] you have collected.
   PL: Wydawaj zdobyte [Wprowadzenie do Zhi, Yong i Ren] w [Wymianie nagród], aby odbierać rozmaite nagrody.
565. [Samouczek i wskazówki [TutoEvent8501_P8_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P8_D1].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Samouczek i wskazówki [TutoEvent8501_P8_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P8_D2].content
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Samouczek i wskazówki [TutoEvent8501_P9_T1] — tekst] 연속 전투 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P9_T1].content
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Samouczek i wskazówki [TutoEvent8501_P9_D1] — tekst] 절차탁춘의 마지막 전투는 연속 전투 방식으로 진행되며, 입장 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P9_D1].content
   limit: do 140 znaków
   EN: The final battle of Spring Cultivation is a Chain Battle Encounter. Entering costs Enkephalin Modules.
   PL: Ostatnia walka Wiosennego Szlifu to Walka Seryjna; wejście do niej zużywa Moduły Enkefaliny.
569. [Samouczek i wskazówki [TutoEvent8501_P10_T1] — tekst] 비급이 아닌 척하는 비전서
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P10_T1].content
   limit: do 120 znaków
   EN: Definitely Not A Secret Scroll
   PL: Zdecydowanie Nie Tajny Zwój
570. [Samouczek i wskazówki [TutoEvent8501_P10_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [비급이 아닌 척하는 비전서]를 획득할 수 있습니다. 획득한 [비급이 아닌 척하는 비전서]는 [지·용·인 기초 입문] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P10_D1].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rarely, you may obtain [Definitely Not A Secret Scroll] from clearing Encounters.\n\n[Definitely Not A Secret Scroll] is automatically converted to 20 [Intro to Zhi, Yong, Ren] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Zdecydowanie Nie Tajnego Zwoju].\nZdobyty [Zdecydowanie Nie Tajny Zwój] zamienia się automatycznie na 20 szt. [Wprowadzenia do Zhi, Yong i Ren].
571. [Samouczek i wskazówki [TutoEvent8501_P11_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 절차탁춘 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8501_P11_D1].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Spring Cultivation combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Wiosennego Szlifu możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
572. [Samouczek i wskazówki [TutoMinigame8501_P1_T1] — tekst] 날짜와 능력치
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P1_T1].content
   limit: do 120 znaków
   EN: Days & Stats
   PL: Dni i statystyki
573. [Samouczek i wskazówki [TutoMinigame8501_P1_D1] — tekst] [수업]은 30일 동안 진행되며, 그 안에 주요 능력치인 지, 용, 인을 최대한 올리는 것이 목표입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P1_D1].content
   limit: do 170 znaków
   EN: The goal in this game mode is to raise the main stats "Zhi, Yong, and Ren" as high as possible over the course of 30 [Class] days.
   PL: [Zajęcia] trwają 30 dni, a twoim celem jest jak najwyższe rozwinięcie w tym czasie trzech głównych statystyk: Zhi, Yong oraz Ren.
574. [Samouczek i wskazówki [TutoMinigame8501_P2_T1] — tekst] 수업 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P2_T1].content
   limit: do 120 znaków
   EN: Select Class
   PL: Wybór zajęć
575. [Samouczek i wskazówki [TutoMinigame8501_P2_D1] — tekst] 수업이 고정된 날짜를 제외하고 듣고 싶은 수업을 하루에 1종류씩 총 3개 선택할 수 있습니다.\n수업 종류는 날짜가 흐를 때마다 점점 늘어납니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P2_D1].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Aside from days with Fixed Classes, you can choose up to 3 Classes per day. The variety of selectable Classes grows as the days go by.
   PL: Poza dniami ze stałymi zajęciami możesz wybrać na dany dzień łącznie 3 zajęcia (po 1 wybranego rodzaju).\nPula dostępnych rodzajów zajęć rośnie wraz z kolejnymi dniami.
576. [Samouczek i wskazówki [TutoMinigame8501_P2_T2] — tekst] 수업 효과
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P2_T2].content
   limit: do 120 znaków
   EN: Class Effects
   PL: Efekty zajęć
577. [Samouczek i wskazówki [TutoMinigame8501_P2_D2] — tekst] 각 수업마다 증가하는 능력치가 다르며, 어떤 수업은 컨디션이 증가하거나 감소합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P2_D2].content
   limit: do 160 znaków
   EN: Each Class specializes in raising different Stats, and some Classes might even raise or lower the students' Morale values.
   PL: Każde zajęcia podnoszą inne statystyki, a niektóre dodatkowo zwiększają lub obniżają kondycję.
578. [Samouczek i wskazówki [TutoMinigame8501_P3_T1] — tekst] 수업 결과와 컨디션
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P3_T1].content
   limit: do 120 znaków
   EN: Class Results & Morale
   PL: Wynik zajęć a kondycja
579. [Samouczek i wskazówki [TutoMinigame8501_P3_D1] — tekst] 수업은 성공하거나 실패할 수 있습니다. 성공 시 획득하는 능력치가 크게 증가하지만, 실패 시 획득하는 능력치가 크게 감소합니다.\n컨디션이 높을수록 성공할 확률이 증가합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P3_D1].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Classes can either end in success or failure. A successful class will greatly increase the amount of Stat gained, but a failed class will greatly reduce the amount of Stat gained.\nHigher Morale results in higher chance to have a successful class.
   PL: Zajęcia mogą zakończyć się sukcesem lub porażką. Sukces znacznie zwiększa przyrost statystyk, natomiast porażka znacznie go zmniejsza.\nIm wyższa kondycja, tym większa szansa na sukces.
580. [Samouczek i wskazówki [TutoMinigame8501_P4_T1] — tekst] 콤보
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P4_T1].content
   limit: do 120 znaków
   EN: Combo
   PL: Kombinacje
581. [Samouczek i wskazówki [TutoMinigame8501_P4_D1] — tekst] 각 수업마다 특정 수업과 같은 날에 들었을 때 보너스 효과를 얻는 콤보가 존재합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P4_D1].content
   limit: do 150 znaków
   EN: Class "Combos" are Class combinations that give certain bonus effects when those classes are taken in the same day.
   PL: Niektóre zajęcia tworzą kombinacje zapewniające dodatkowe efekty premiowe, gdy odbędą się tego samego dnia co określone inne zajęcia.
582. [Samouczek i wskazówki [TutoMinigame8501_P4_T2] — tekst] 콤보 발생
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P4_T2].content
   limit: do 120 znaków
   EN: Combo Activation
   PL: Aktywacja kombinacji
583. [Samouczek i wskazówki [TutoMinigame8501_P4_D2] — tekst] 발견한 콤보는 시간표에서 콤보 발동 여부를 미리 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P4_D2].content
   limit: do 120 znaków
   EN: Once you discover a Combo, you can preview its activation in the Schedule menu.
   PL: Odkryte kombinacje możesz zawczasu podejrzeć bezpośrednio w planie zajęć.
584. [Samouczek i wskazówki [TutoMinigame8501_P5_T1] — tekst] 콤보 목록
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P5_T1].content
   limit: do 120 znaków
   EN: Combo List
   PL: Lista kombinacji
585. [Samouczek i wskazówki [TutoMinigame8501_P5_D1] — tekst] [콤보 목록] 페이지에서 발견한 콤보와 발견하지 못한 콤보를 모두 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P5_D1].content
   limit: do 120 znaków
   EN: View all discovered Combos and undiscovered combos in the [Combo List] page.
   PL: Na stronie [Listy kombinacji] sprawdzisz zarówno odkryte, jak i jeszcze nieodkryte kombinacje.
586. [Samouczek i wskazówki [TutoMinigame8501_P6_T1] — tekst] 수업 시작
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P6_T1].content
   limit: do 120 znaków
   EN: Begin Class
   PL: Rozpocznij zajęcia
587. [Samouczek i wskazówki [TutoMinigame8501_P6_D1] — tekst] 수업을 모두 선택했다면 [수업 시작] 버튼을 눌러 수업을 진행합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P6_D1].content
   limit: do 120 znaków
   EN: Once you've selected all of your classes, select [Begin Class] button to... begin class.
   PL: Po wybraniu wszystkich zajęć kliknij przycisk [Rozpocznij zajęcia], aby je przeprowadzić.
588. [Samouczek i wskazówki [TutoMinigame8501_P7_D1] — tekst] 수업 진행
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P7_D1].content
   limit: do 120 znaków
   EN: Class Progression
   PL: Przebieg zajęć
589. [Samouczek i wskazówki [TutoMinigame8501_P7_D2] — tekst] 수업은 별도의 조작 없이 자동으로 진행됩니다. 수업 진행 중에 능력치 변동을 실시간으로 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P7_D2].content
   limit: do 140 znaków
   EN: Classes progress automatically. During class, you can view the students' changing stat values in real-time.
   PL: Zajęcia przebiegają automatycznie; w ich trakcie możesz na żywo śledzić zmiany statystyk.
590. [Samouczek i wskazówki [TutoMinigame8501_P8_T1] — tekst] 수업 업그레이드
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P8_T1].content
   limit: do 120 znaków
   EN: Class Upgrade
   PL: Ulepszanie zajęć
591. [Samouczek i wskazówki [TutoMinigame8501_P8_D1] — tekst] 수업 별로 들을 때마다 경험치를 쌓을 수 있습니다. 경험치가 전부 쌓인 수업은 다음 단계로 업그레이드 됩니다.\n단계가 높을수록 수업 결과로 얻는 능력치가 증가합니다. 고급 단계에선 업그레이드할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P8_D1].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Taking a Class gives "EXP". Once a Class EXP has been maxed out, the Class will be upgraded to the next level.\nTaking higher-level Classes will yield more Stat increases. Please note that Classes cannot be upgraded beyond "Master".
   PL: Każde odbyte zajęcia zapewniają im punkty doświadczenia. Po zapełnieniu paska PD zajęcia awansują na kolejny poziom.\nWyższy poziom zajęć daje większy przyrost statystyk. Na poziomie mistrzowskim nie można ich już dalej ulepszać.
592. [Samouczek i wskazówki [TutoMinigame8501_P9_T1] — tekst] 전투 능력 강화 방법
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P9_T1].content
   limit: do 120 znaków
   EN: Combat Prowess Enhancements
   PL: Wzmacnianie zdolności bojowych
593. [Samouczek i wskazówki [TutoMinigame8501_P9_D1] — tekst] 지, 용, 인을 특정 수치 이상 올리거나 수업을 특정 단계로 업그레이드하면 전투 능력이 강화합니다. 강화된 능력은 가시춘과 싱클레어가 서로 다르게 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P9_D1].content
   limit: do 270 znaków
   EN: Raising Zhi, Yong, or Ren stats beyond a specific level, or upgrading a Class to a certain level will enhance the students' combat prowess. These enhancements are applied separately for Jia Xichun and Sinclair.
   PL: Podniesienie Zhi, Yong lub Ren powyżej określonego progu albo ulepszenie zajęć do danego poziomu wzmacnia zdolności bojowe. Wzmocnienia działają odmiennie u Jia Xichun oraz u Sinclaira.
594. [Samouczek i wskazówki [TutoMinigame8501_P10_T1] — tekst] 전투 능력 확인
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P10_T1].content
   limit: do 120 znaków
   EN: Viewing Combat Prowess
   PL: Podgląd zdolności bojowych
595. [Samouczek i wskazówki [TutoMinigame8501_P10_D1] — tekst] 가시춘의 자세한 스테이터스는 돋보기 아이콘을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P10_D1].content
   limit: do 120 znaków
   EN: Select the magnifier icon here to view Jia Xichun's detailed stats.
   PL: Szczegółowe statystyki Jia Xichun sprawdzisz pod ikoną lupy.
596. [Samouczek i wskazówki [TutoMinigame8501_P11_T1] — tekst] 가시춘 단독 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P11_T1].content
   limit: do 120 znaków
   EN: Jia Xichun Solo Battles
   PL: Samotne walki Jia Xichun
597. [Samouczek i wskazówki [TutoMinigame8501_P11_D1] — tekst] 특정 날짜에는 수업 대신 전투가 발생할 수 있습니다. 이때, 참가하는 전투 인원은 가시춘 혼자입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P11_D1].content
   limit: do 170 znaków
   EN: On certain dates, Combat Encounters may occur in place of classes. Jia Xichun will be participating in these Encounters on her own.
   PL: W niektóre dni zamiast zajęć może dojść do walki. Bierze w niej udział wyłącznie sama Jia Xichun.
598. [Samouczek i wskazówki [TutoMinigame8501_P12_T1] — tekst] 전투 진행 방법
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P12_T1].content
   limit: do 120 znaków
   EN: Combat Progression
   PL: Przebieg walki
599. [Samouczek i wskazówki [TutoMinigame8501_P12_D1] — tekst] 스킬 슬롯은 자동으로 연결되며, 징 모양 버튼을 누르면 전투가 진행됩니다.\n전투에서 승리해야 다음 날짜 또는 수업으로 넘어갈 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoMinigame8501_P12_D1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skill Slots are chained automatically. Press the "Gong-shaped button" to begin the combat phase.\nOnly by winning the combat Encounter can she progress to the next day, or the next Class.
   PL: Sloty umiejętności łączą się automatycznie — naciśnij przycisk w kształcie gongu, aby rozpocząć walkę.\nMusisz zwyciężyć, aby przejść do następnego dnia lub kolejnych zajęć.
600. [Samouczek i wskazówki [TutoEvent8502_Title] — tekst] 선의의 순례
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_Title].content
   limit: do 120 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
601. [Samouczek i wskazówki [TutoEvent8502_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Samouczek i wskazówki [TutoEvent8502_P1_D1] — tekst] [선의의 순례]는 주요 이야기의 0-4를 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P1_D1].content
   limit: do 210 znaków
   EN: The [Pilgrimage of Compassion] page opens after clearing Stage 0-4 of the Main Story. You may enter the event page via the banner on the Window or the Drive menu.
   PL: [Pielgrzymka Współczucia] odblokowuje się po ukończeniu etapu 0-4 Głównej Opowieści. Wejdziesz do niej przez baner wydarzenia w Oknie lub Jeździe.
603. [Samouczek i wskazówki [TutoEvent8502_P1_D2] — tekst] 스토리의 시간 순서 상 8.5장 절차탁춘을 플레이하지 않은 분들께는 스토리의 일부 요소 중 스포일러가 포함될 수 있으니 이 점을 참고부탁드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P1_D2].content
   limit: do 180 znaków
   EN: Please note that this story takes place after Intervallo VI - Spring Cultivation, and may contain spoilers up to that point in the story.
   PL: Uwaga: chronologicznie historia ta rozgrywa się po odcinku 8.5 (Wiosenny Szlif), więc u osób, które jeszcze go nie ukończyły, niektóre wątki mogą zawierać spojlery.
604. [Samouczek i wskazówki [TutoEvent8502_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Samouczek i wskazówki [TutoEvent8502_P2_D1] — tekst] 선의의 순례 이벤트 기간이 표시됩니다. 이벤트 기간 동안 선의의 순례 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [시테러 표본]을 획득할 수 있습니다.\n※ 단, 채광과 거울굴절철도에서는 [시테러 표본]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P2_D1].content
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Pilgrimage of Compassion event is shown here.\n\nDuring the event, you can earn [Sea Terror Sample] by clearing Event Stages. You can also earn [Sea Terror Sample] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Sea Terror Sample] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Pielgrzymka Współczucia. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Próbki Morskiego Koszmaru].\n※ [Próbek Morskiego Koszmaru] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
606. [Samouczek i wskazówki [TutoEvent8502_P2_D2] — tekst] 선의의 순례는 이벤트 기간에만 플레이할 수 있는 한정 컨텐츠이며, 이벤트 기간이 종료되면 관련된 스토리 감상 및 스테이지 진행, 전투를 플레이 하실 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P2_D2].content
   limit: do 290 znaków
   EN: Pilgrimage of Compassion is a limited content that is accessible only during the Event period. Please note that, once the Event period is over, its story, stage progression, and combat content will no longer be accessible.
   PL: Pielgrzymka Współczucia to zawartość limitowana dostępna wyłącznie podczas trwania wydarzenia — po jego zakończeniu fabuła, etapy ani walki nie będą już dostępne.
607. [Samouczek i wskazówki [TutoEvent8502_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Samouczek i wskazówki [TutoEvent8502_P3_D1] — tekst] 선의의 순례 이벤트는 스토리 스테이지를 포함하여 총 14개의 스테이지로 구성됩니다. 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [시테러 표본]을 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P3_D1].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pilgrimage of Compassion Event consists of 14 stages, including story stages.\nSaid stages also offer batches of [Sea Terror Sample] as a first-time Clear bonus. (only for first-time clears of each Stage)
   PL: Wydarzenie Pielgrzymka Współczucia obejmuje łącznie 14 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Próbki Morskiego Koszmaru] za pierwsze ukończenie każdego etapu (1 raz na walkę).
609. [Samouczek i wskazówki [TutoEvent8502_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Samouczek i wskazówki [TutoEvent8502_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [시테러 표본]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P4_D1].content
   limit: do 160 znaków
   EN: Having E.G.O from the event on your team increases the amount of [Sea Terror Sample] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych E.G.O wydarzenia zwiększa liczbę [Próbek Morskiego Koszmaru] zdobywanych na etapach i w Lustrzanych Lochach.
611. [Samouczek i wskazówki [TutoEvent8502_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Samouczek i wskazówki [TutoEvent8502_P5_D1] — tekst] 획득한 [시테러 표본]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P5_D1].content
   limit: do 150 znaków
   EN: You can redeem various rewards from the [Reward Exchange] based on the number of [Sea Terror Sample] you have.
   PL: Wydawaj zdobyte [Próbki Morskiego Koszmaru] w [Wymianie nagród], aby odbierać rozmaite nagrody.
613. [Samouczek i wskazówki [TutoEvent8502_P6_D1] — tekst] [보상 교환] 창에서 이벤트 보상 E.G.O, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P6_D1].content
   limit: do 150 znaków
   EN: You can acquire the event reward E.G.O, Ticket Deco, banners, and various currencies from [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz E.G.O wydarzenia, ozdoby biletu, banery oraz rozmaite waluty.
614. [Samouczek i wskazówki [TutoEvent8502_P6_D2] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P6_D2].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Samouczek i wskazówki [TutoEvent8502_P7_T1] — tekst] Normal 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P7_T1].content
   limit: do 120 znaków
   EN: Normal Difficulty
   PL: Poziom Normal
616. [Samouczek i wskazówki [TutoEvent8502_P7_D1] — tekst] Normal 난이도에서는 인격의 레벨과 동기화 단계, E.G.O의 환상 해석 단계가 낮은 경우 다음과 같이 보정이 들어갑니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P7_D1].content
   limit: do 190 znaków
   EN: In Normal difficulty, if your Identities' Levels and Uptie Tiers, and E.G.O's Threadspinning Tiers are too low, they will be leveled up as follows:
   PL: Na poziomie Normal zbyt niski poziom i stopień Synchronizacji Tożsamości oraz stopień Splotu Nici E.G.O zostają podniesione w następujący sposób:
617. [Samouczek i wskazówki [TutoEvent8502_P7_D2] — tekst] ※ 인격 레벨 55로 상승, 인격 동기화 단계 4단계로 상승, E.G.O 환상 해석 단계 4단계로 상승
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P7_D2].content
   limit: do 160 znaków
   EN: ※ Identity levels rise to Level 55, Identity Uptie Tiers rise to Tier 4, and E.G.O Threadspinning Tiers rise to Tier 4
   PL: ※ Poziom Tożsamości rośnie do 55, Synchronizacja Tożsamości do 4. stopnia, a Splot Nici E.G.O do 4. stopnia.
618. [Samouczek i wskazówki [TutoEvent8502_P8_D1] — tekst] 챕터 진행도, ex 클리어 진행도 보상은 이벤트 진행 기간(2025/9/25 12:00 ~ 10/23 06:00 (KST))에만 수령 가능합니다.\n이 점 참고해 주시기 바랍니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P8_D1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please take note that Chapter Progression & Extra Conditions Fulfilled Rewards can be obtained only during the Event Period(2025/9/25 12:00 ~ 10/23 06:00 (KST)).
   PL: Pamiętaj, że nagrody postępu rozdziału oraz postępu ukończeń EX można odebrać wyłącznie podczas trwania wydarzenia (2025/9/25 12:00 ~ 10/23 06:00 (KST)).\nProsimy mieć to na uwadze.
619. [Samouczek i wskazówki [TutoEvent8502_P9_T1] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P9_T1].content
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Samouczek i wskazówki [TutoEvent8502_P9_D1] — tekst] 선의의 순례 마지막 전투는 던전이 등장하며,\n입장 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P9_D1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Dungeon awaits at the end of the Pilgrimage of Compassion event. Entering this Dungeon costs Enkephalin Modules.
   PL: Ostatnia walka Pielgrzymki Współczucia to loch,\nktórego wejście zużywa Moduły Enkefaliny.
621. [Samouczek i wskazówki [TutoEvent8502_P10_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P10_T1].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Samouczek i wskazówki [TutoEvent8502_P10_D1] — tekst] 이벤트 기간 동안 선의의 순례 Hard 난이도를 진행할 수 있습니다.\n주요 이야기 0-4 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P10_D1].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pilgrimage of Compassion Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 0-4.
   PL: W trakcie wydarzenia dostępny jest poziom Hard Pielgrzymki Współczucia.\nOdblokowuje się on po ukończeniu etapu 0-4 Głównej Opowieści.
623. [Samouczek i wskazówki [TutoEvent8502_P10_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P10_D2].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Samouczek i wskazówki [TutoEvent8502_P10_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P10_D3].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Samouczek i wskazówki [TutoEvent8502_P10_D4] — tekst] Hard 난이도 클리어 시 해당 스테이지의 Normal 난이도도 클리어한 것으로 적용됩니다.\n이 경우, 해당 스테이지의 Normal 난이도에서 획득 가능한 EX 클리어 보상(광기), 이벤트 재화 초회 보상을 동시에 획득할 수 있습니다.\n※ 단, 계정 경험치, 인격 경험치, 이벤트 재화 반복 보상은 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P10_D4].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing a Hard difficulty stage automatically clears the Normal difficulty Stage as well. Clearing the Normal difficulty Stage by clearing the Hard difficulty Stage will yield Normal Difficulty Extra Conditions Fulfilled Reward(Lunacy) and first-time event currency rewards as well. \n※ However, this does not apply to Account EXP, Identity EXP, or repeat event currency rewards.
   PL: Ukończenie etapu na poziomie Hard automatycznie zalicza także poziom Normal tego etapu.\nOtrzymasz wówczas jednocześnie nagrodę EX poziomu Normal (Szaleństwo) oraz nagrodę waluty wydarzenia za pierwsze ukończenie.\n※ Nie dotyczy to jednak PD konta, PD Tożsamości ani powtarzalnych nagród waluty wydarzenia.
626. [Samouczek i wskazówki [TutoEvent8502_P11_T1] — tekst] 빛나는 시테러 표본
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P11_T1].content
   limit: do 120 znaków
   EN: Luminous Sea Terror Sample
   PL: Lśniąca Próbka Morskiego Koszmaru
627. [Samouczek i wskazówki [TutoEvent8502_P11_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [빛나는 시테러 표본]를 획득할 수 있습니다. 획득한 [빛나는 시테러 표본]는 [시테러 표본] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P11_D1].content
   limit: do 230 znaków
   EN: Rarely, you may obtain [Luminous Sea Terror Sample] from clearing Encounters. [Luminous Sea Terror Sample] is automatically converted to 20 [Sea Terror Sample] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Lśniącej Próbki Morskiego Koszmaru], która automatycznie zamienia się na 20 [Próbek Morskiego Koszmaru].
628. [Samouczek i wskazówki [TutoEvent8502_P12_D1] — tekst] 이벤트 기간동안 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 선의의 순례 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P12_D1].content
   limit: do 240 znaków
   EN: During the event period, you will be able to experience the Pilgrimage of Compassion combat Encounters and view its story anytime at the Drive - [Deviazione] and Theater - [Detour Tales].
   PL: W trakcie trwania wydarzenia walki oraz fabułę Pielgrzymki Współczucia możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
629. [Samouczek i wskazówki [TutoEvent8502_P12_D2] — tekst] ※ 이벤트 기간(2025/9/25 12:00 ~ 10/23 06:00 (KST)) 종료 후에는 선의의 순례 전투와 스토리가 운전석 및 상영관에서 제거됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent8502_P12_D2].content
   limit: do 220 znaków
   EN: ※ Once the event period(2025/9/25 12:00 ~ 10/23 06:00 (KST)) is over, Pilgrimage of Compassion combat Encounters and story will be removed from the Drive & Theater menus.
   PL: ※ Po zakończeniu okresu wydarzenia (2025/9/25 12:00 ~ 10/23 06:00 (KST)) walki oraz fabuła Pielgrzymki Współczucia zostaną usunięte z menu Jazdy i Teatru.
630. [Samouczek i wskazówki [TutoEvent6512_Title] — tekst] 워프특급 살인사건 BokGak
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_Title].content
   limit: do 120 znaków
   EN: Murder on the WARP Express BokGak
   PL: Morderstwo w Ekspresie WARP BokGak
631. [Samouczek i wskazówki [TutoEvent6512_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Samouczek i wskazówki [TutoEvent6512_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [워프특급 살인사건 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P1_D1].content
   limit: do 170 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Murder on the WARP Express BokGak Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Morderstwo w Ekspresie WARP BokGak].
633. [Samouczek i wskazówki [TutoEvent6512_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Samouczek i wskazówki [TutoEvent6512_P2_D1] — tekst] 워프특급 살인사건 BokGak 이벤트 기간이 표시됩니다. 이벤트 기간 동안 워프특급 살인사건 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [일반 승객 복구팩]를 획득할 수 있습니다.\n※ 단, 채광과 거울굴절철도에서는 [일반 승객 복구팩]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P2_D1].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Murder on the WARP Express BokGak event is shown here.\n\nDuring the event, you can earn [Civilian Recov. Pack] by clearing Event Stages. You can also earn [Civilian Recov. Pack] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Civilian Recov. Pack] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Morderstwo w Ekspresie WARP BokGak. W trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Pakiety Rekonstrukcyjne Pasażera].\n※ [Pakietów Rekonstrukcyjnych Pasażera] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
635. [Samouczek i wskazówki [TutoEvent6512_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Samouczek i wskazówki [TutoEvent6512_P3_D1] — tekst] 워프특급 살인사건 BokGak 이벤트는 스토리 스테이지를 포함하여 총 15개의 스테이지로 구성됩니다. 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [일반 승객 복구팩]를 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P3_D1].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Murder on the WARP Express BokGak Event consists of 15 stages, including story stages.\n\nSaid stages also offer batches of [Civilian Recov. Pack] as a First-time Clear bonus in addition to clear rewards. (only for first-time clears of each Stage)
   PL: Wydarzenie Morderstwo w Ekspresie WARP BokGak obejmuje łącznie 15 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Pakiety Rekonstrukcyjne Pasażera] za pierwsze ukończenie każdego etapu (1 raz na walkę).
637. [Samouczek i wskazówki [TutoEvent6512_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Samouczek i wskazówki [TutoEvent6512_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [일반 승객 복구팩]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P4_D1].content
   limit: do 220 znaków
   EN: Having Identities and E.G.O from Murder on the WARP Express BokGak event on your team increases the amount of [Civilian Recov. Pack] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości i E.G.O wydarzenia zwiększa liczbę [Pakietów Rekonstrukcyjnych Pasażera] zdobywanych na etapach i w Lustrzanych Lochach.
639. [Samouczek i wskazówki [TutoEvent6512_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Samouczek i wskazówki [TutoEvent6512_P5_D1] — tekst] 획득한 [일반 승객 복구팩]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P5_D1].content
   limit: do 150 znaków
   EN: You can redeem various rewards from the [Reward Exchange] using the [Civilian Recov. Pack] you have collected.
   PL: Wydawaj zdobyte [Pakiety Rekonstrukcyjne Pasażera] w [Wymianie nagród], aby odbierać rozmaite nagrody.
641. [Samouczek i wskazówki [TutoEvent6512_P6_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P6_D1].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Samouczek i wskazówki [TutoEvent6512_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P6_D2].content
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Samouczek i wskazówki [TutoEvent6512_P7_T1] — tekst] 해결사 승객 복구팩
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P7_T1].content
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Samouczek i wskazówki [TutoEvent6512_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [해결사 승객 복구팩]을 획득할 수 있습니다. 획득한 [해결사 승객 복구팩]은 [일반 승객 복구팩] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P7_D1].content
   limit: do 210 znaków
   EN: Rarely, you may obtain [Fixer Recov. Pack] from clearing Encounters. [Fixer Recov. Pack] is immediately converted to 20 [Civilian Recov. Pack] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Pakietu Rekonstrukcyjnego Fiksera], który od razu zamienia się na 20 [Pakietów Rekonstrukcyjnych Pasażera].
645. [Samouczek i wskazówki [TutoEvent6512_P8_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P8_T1].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Samouczek i wskazówki [TutoEvent6512_P8_D1] — tekst] 이벤트 기간 동안 워프특급 살인사건 Hard 난이도를 진행할 수 있습니다. 주요 이야기 7-36 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P8_D1].content
   limit: do 210 znaków
   EN: Murder on the WARP Express Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 7-36.
   PL: W trakcie wydarzenia dostępny jest poziom Hard Morderstwa w Ekspresie WARP. Odblokowuje się on po ukończeniu etapu 7-36 Głównej Opowieści.
647. [Samouczek i wskazówki [TutoEvent6512_P8_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P8_D2].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Samouczek i wskazówki [TutoEvent6512_P8_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P8_D3].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Samouczek i wskazówki [TutoEvent6512_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 워프특급 살인사건 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent6512_P9_D1].content
   limit: do 270 znaków
   EN: Even after the event fully ends, you will be able to experience the Murder on the WARP Express combat Encounters and view its story at any time at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Morderstwa w Ekspresie WARP możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
650. [Samouczek i wskazówki [TutoRailway1BokGak_P1_T1] — tekst] 거울굴절철도 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P1_T1].content
   limit: do 120 znaków
   EN: Refraction Railway Opening
   PL: Odblokowanie Kolei Załamania
651. [Samouczek i wskazówki [TutoRailway1BokGak_P1_D1] — tekst] 활성화된 노선을 선택하여 재화 소모 없이 자유롭게 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P1_D1].content
   limit: do 120 znaków
   EN: You can enter the available Lines at no cost.
   PL: Wybierz aktywną linię, aby wejść swobodnie bez zużywania walut.
652. [Samouczek i wskazówki [TutoRailway1BokGak_P2_T1] — tekst] 입장 권장 사양
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P2_T1].content
   limit: do 120 znaków
   EN: Recommended Levels
   PL: Zalecane parametry wejścia
653. [Samouczek i wskazówki [TutoRailway1BokGak_P2_D1] — tekst] 거울굴절철도 입장 권장 사양이 노선 측면에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P2_D1].content
   limit: do 120 znaków
   EN: Recommended levels & upgrade tiers are displayed on the side of the Line.
   PL: Zalecane parametry wejścia do Kolei Załamania widnieją z boku linii.
654. [Samouczek i wskazówki [TutoRailway1BokGak_P2_D2] — tekst] 되도록이면, 권장 사양을 맞춘 이후에 입장하는 것을 추천드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P2_D2].content
   limit: do 120 znaków
   EN: We suggest that you enter the Railway after meeting the recommended levels & upgrade tiers.
   PL: Zalecamy wejście po osiągnięciu sugerowanych parametrów rozwoju.
655. [Samouczek i wskazówki [TutoRailway1BokGak_P3_T1] — tekst] 1호선 역
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P3_T1].content
   limit: do 120 znaków
   EN: Line 1 Stations
   PL: Stacje Linii 1
656. [Samouczek i wskazówki [TutoRailway1BokGak_P3_D1] — tekst] 1호선에는 총 13개의 역이 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P3_D1].content
   limit: do 120 znaków
   EN: Line 1 has a total of 13 Stations.
   PL: Linia 1 liczy łącznie 13 stacji.
657. [Samouczek i wskazówki [TutoRailway1BokGak_P3_D2] — tekst] 해당 역 클리어 시, 클리어 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P3_D2].content
   limit: do 120 znaków
   EN: Clearing the Section will record your Clear Turn Count.
   PL: Po ukończeniu stacji zapisywana jest liczba tur ukończenia.
658. [Samouczek i wskazówki [TutoRailway1BokGak_P3_D3] — tekst] 이와 함께, 제 1역부터 현재 역까지의 각 역별 클리어 턴이 모두 합해진 누적 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P3_D3].content
   limit: do 150 znaków
   EN: Below the Clear Turn Count is the Total Turn Count, which is the sum of all Clear Turn Counts from each Station.
   PL: Obok niej zapisywana jest łączna liczba tur będąca sumą tur ukończenia wszystkich stacji od Stacji 1 do bieżącej.
659. [Samouczek i wskazówki [TutoRailway1BokGak_P3_D4] — tekst] 해당 역을 클리어하였을 때 분실물 보관소를 통해 얻을 수 있게되는 보상이 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P3_D4].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Below each Station, you can view the rewards for clearing that Station. Claim them at the Lost & Found.
   PL: Poniżej widnieją nagrody za ukończenie danej stacji\ndo odebrania w Biurze Rzeczy Znalezionych.
660. [Samouczek i wskazówki [TutoRailway1BokGak_P4_T1] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P4_T1].content
   (powtórzenie elementu 180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Samouczek i wskazówki [TutoRailway1BokGak_P4_D1] — tekst] 1호선에서는 모든 적의 정보가 공개되어있습니다. 공략에 알맞은 인격과 E.G.O를 편성하여 전투를 진행하세요.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P4_D1].content
   limit: do 210 znaków
   EN: In Line 1, all enemy info will be unlocked for viewing from the start. Prepare the appropriate strategy, Identity, and E.G.O loadout based on this information.
   PL: Na Linii 1 informacje o wszystkich wrogach są jawne od samego początku. Dobierz odpowiedni skład Tożsamości oraz E.G.O pod kątem strategii.
662. [Samouczek i wskazówki [TutoRailway1BokGak_P4_D2] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P4_D2].content
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Samouczek i wskazówki [TutoRailway1BokGak_P4_D3] — tekst] 1호선에서는 전투 중 재도전하거나 포기하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P4_D3].content
   limit: do 130 znaków
   EN: In Line 1, the updated Observation Level will be saved even if you give up or retry mid-Encounter.
   PL: Na Linii 1 zaktualizowane wpisy Kompendium zostają zapisane nawet przy ponowieniu lub poddaniu walki.
664. [Samouczek i wskazówki [TutoRailway1BokGak_P5_T1] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_T1].content
   limit: do 120 znaków
   EN: Team Loadout
   PL: Skład drużyny
665. [Samouczek i wskazówki [TutoRailway1BokGak_P5_D1] — tekst] 보유한 인격과 E.G.O를 편성하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_D1].content
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Samouczek i wskazówki [TutoRailway1BokGak_P5_D2] — tekst] 편성 인원은 매 역마다 변경할 수 있습니다. 매 역마다 수감자의 체력이 최대로 회복됩니다. 정신력은 이전 역의 상태가 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_D2].content
   limit: do 200 znaków
   EN: At every station, your Team loadout can be changed, and your Sinners' HP will be fully healed. Their SP, however, will carry over from the previous Station.
   PL: Skład drużyny można zmieniać na każdej stacji. Na każdej stacji PŻ Grzeszników wracają do maksimum, natomiast PP przechodzą z poprzedniej stacji.
667. [Samouczek i wskazówki [TutoRailway1BokGak_P5_D3] — tekst] 인격의 레벨을 올리거나, 동기화 단계 상승, E.G.O 환상 해석 단계 상승 시, 진행 중인 거울굴절철도에도 변경된 내용이 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_D3].content
   limit: do 230 znaków
   EN: If you level up, Uptie, or Threadspin your Identities or E.G.O outside the Refraction Railway, the changes will be applied to your characters in the Refraction Railway as well.
   PL: Podniesienie poziomu Tożsamości, stopnia Synchronizacji lub stopnia Splotu Nici E.G.O poza Koleją Załamania zostanie uwzględnione także w trwającej wyprawie.
668. [Samouczek i wskazówki [TutoRailway1BokGak_P5_D4] — tekst] 대기 인원에게는 시작 정신력 버프가 추가로 적용되며, 편성 순서가 늦을 수록 시작 정신력 값이 높아집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_D4].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Backup Units receive Starting SP buffs, and Backup Units further back in the Deployment order receive greater Starting SP buffs.
   PL: Rezerwowi zyskują premię początkowych PP —\nim dalsze miejsce w rozstawieniu, tym wyższe początkowe PP.
669. [Samouczek i wskazówki [TutoRailway1BokGak_P5_D5] — tekst] 빼기 코인을 사용하는 인격의 경우에는 시작 정신력 버프가 음수값으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P5_D5].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Minus Coin Identities receive negative Starting SP buffs.
   PL: U Tożsamości z Monetami Ujemnymi\npremia początkowych PP ma wartość ujemną.
670. [Samouczek i wskazówki [TutoRailway1BokGak_P6_T1] — tekst] 전투 편성 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P6_T1].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Samouczek i wskazówki [TutoRailway1BokGak_P6_D1] — tekst] 1호선은 연속 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P6_D1].content
   limit: do 120 znaków
   EN: Combat Encounters in Line 1 are "Chain Battles."
   PL: Linia 1 rozgrywana jest w trybie Walki Seryjnej.
672. [Samouczek i wskazówki [TutoRailway1BokGak_P6_D2] — tekst] 연속 전투에서는 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P6_D2].content
   limit: do 160 znaków
   EN: In Chain Battles, when a Deployed unit is defeated, the Backup Units will fill their spot according to the Deployment order.
   PL: W Walce Seryjnej po śmierci uczestnika podstawowego jego miejsce zajmują rezerwowi zgodnie z ustaloną kolejnością.
673. [Samouczek i wskazówki [TutoRailway1BokGak_P6_D3] — tekst] 5명의 출격 인원과 7명의 대기 인원을 전부 설정하여야 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P6_D3].content
   limit: do 160 znaków
   EN: You can enter the Station only when you have selected both your Deployment and Backup units: 5 and 7 units, respectively.
   PL: Aby wejść, musisz obsadzić wszystkich 5 uczestników podstawowych oraz 7 rezerwowych.
674. [Samouczek i wskazówki [TutoRailway1BokGak_P7_T1] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P7_T1].content
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Samouczek i wskazówki [TutoRailway1BokGak_P7_D1] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P7_D1].content
   (powtórzenie elementu 5 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Samouczek i wskazówki [TutoRailway1BokGak_P7_D2] — tekst] 하나의 역에서 기록되는 최대 턴 수는 100턴이며, 한 스테이지 내에서 턴 수가 100을 초과할 경우에는 패배한 것으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P7_D2].content
   limit: do 220 znaków
   EN: The highest Turn Count that can be recorded in each Station is 100 Turns. If your Turn Count goes beyond 100 Turns in a single Stage, the Encounter will end in defeat.
   PL: Maksymalna zapisywana liczba tur na stację wynosi 100 — przekroczenie 100 tur na jednym etapie skutkuje porażką.
677. [Samouczek i wskazówki [TutoRailway1BokGak_P8_T1] — tekst] 전투 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P8_T1].content
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Samouczek i wskazówki [TutoRailway1BokGak_P8_D1] — tekst] 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P8_D1].content
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Samouczek i wskazówki [TutoRailway1BokGak_P8_D2] — tekst] 대기 인원이 출격 인원으로 전환되면, 적용 중인 서포트 패시브가 전투 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P8_D2].content
   limit: do 140 znaków
   EN: When a Backup unit is Deployed into battle, its Combat Passive activates instead of its Support Passive.
   PL: Gdy rezerwowy wchodzi do walki, jego pasywka wsparcia zamienia się w pasywkę bojową.
680. [Samouczek i wskazówki [TutoRailway1BokGak_P8_D3] — tekst] 출격인원이 사망한 경우, 적용 중인 전투 패시브가 서포트 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P8_D3].content
   limit: do 140 znaków
   EN: When a unit on the field is defeated, its Support Passive will activate instead of its Combat Passive.
   PL: Gdy uczestnik podstawowy zginie, jego pasywka bojowa zamienia się w pasywkę wsparcia.
681. [Samouczek i wskazówki [TutoRailway1BokGak_P9_T1] — tekst] 전투 - 남겨진 의지
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P9_T1].content
   limit: do 120 znaków
   EN: Combat - Lingering Determination
   PL: Walka — Pozostawiona Wola
682. [Samouczek i wskazówki [TutoRailway1BokGak_P9_D1] — tekst] 1호선에서는 인격 사망 시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻으며, 기존 연속 전투와 같이 다른 아군의 정신력이 감소하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P9_D1].content
   limit: do 270 znaków
   EN: In Line 1, when an Identity is killed, they release E.G.O resources based on the ranks and Affinities of their Base Attack Skills. And just like in Chain Battles, their deaths will not reduce other allies' SP.
   PL: Na Linii 1 śmierć Tożsamości zapewnia zasoby E.G.O odpowiadające grzechom jej podstawowych umiejętności ataku w liczbie równej ich randze, a tak jak w Walkach Seryjnych nie obniża PP pozostałych sojuszników.
683. [Samouczek i wskazówki [TutoRailway1BokGak_P10_T1] — tekst] 클리어 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P10_T1].content
   (powtórzenie elementu 423 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Samouczek i wskazówki [TutoRailway1BokGak_P10_D1] — tekst] 각 역을 클리어한 후, 클리어 정보 창에서 클리어 턴, 누적 턴, 전투 참여 인격의 통계를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P10_D1].content
   limit: do 180 znaków
   EN: After clearing each Station, you can view statistics such as Clear Turns, Total Turns, and participating Identities in the Clear Info menu.
   PL: Po ukończeniu każdej stacji w oknie informacji sprawdzisz tury ukończenia, łączne tury oraz statystyki uczestniczących Tożsamości.
685. [Samouczek i wskazówki [TutoRailway1BokGak_P11_D1] — tekst] 역 클리어 이후 남은 E.G.O 자원은 다음 역에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P11_D1].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a Station can be carried over to the next Station.
   PL: Zasoby E.G.O pozostałe po ukończeniu stacji można wykorzystać na następnej stacji.
686. [Samouczek i wskazówki [TutoRailway1BokGak_P12_D1] — tekst] 아군이 모두 전멸하였다면 입장 화면으로 돌아가 편성 순서를 다시 설정하거나 현재 전투를 즉시 재도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P12_D1].content
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Samouczek i wskazówki [TutoRailway1BokGak_P13_T1] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P13_T1].content
   (powtórzenie elementu 190 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Samouczek i wskazówki [TutoRailway1BokGak_P13_D1] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P13_D1].content
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Samouczek i wskazówki [TutoRailway1BokGak_P13_D2] — tekst] 특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P13_D2].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Samouczek i wskazówki [TutoRailway1BokGak_P14_T1] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P14_T1].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Samouczek i wskazówki [TutoRailway1BokGak_P14_D1] — tekst] 거울굴절철도 1호선 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P14_D1].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 1 banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 1.
692. [Samouczek i wskazówki [TutoRailway1BokGak_P15_T1] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P15_T1].content
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Samouczek i wskazówki [TutoRailway1BokGak_P15_D1] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P15_D1].content
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Samouczek i wskazówki [TutoRailway1BokGak_P15_D2] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P15_D2].content
   limit: do 150 znaków
   EN: To gain access to a reward for the first time at Lost & Found, a number of Enkephalin Modules will be required.
   PL: Aby po raz pierwszy odebrać nagrody w Biurze Rzeczy Znalezionych, należy jednorazowo zapłacić określoną liczbę Modułów Enkefaliny.
695. [Samouczek i wskazówki [TutoRailway1BokGak_P15_D3] — tekst] 이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway1BokGak_P15_D3].content
   limit: do 120 znaków
   EN: Afterward, you may freely access it and claim rewards you’ve earned at no additional cost.
   PL: Kolejne odblokowane nagrody odbierzesz w dowolnej chwili bez dodatkowych Modułów Enkefaliny.
696. [Samouczek i wskazówki [TutoUIReplacement_P1_T1] — tekst] UI 디자인 변경
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P1_T1].content
   limit: do 120 znaków
   EN: Change UI Design
   PL: Zmiana wyglądu UI
697. [Samouczek i wskazówki [TutoUIReplacement_P1_D1] — tekst] 해당 버튼을 통해 UI 인터페이스 디자인을 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P1_D1].content
   limit: do 120 znaków
   EN: Select this button to switch between User Interface designs.
   PL: Za pomocą tego przycisku zmienisz wygląd interfejsu użytkownika.
698. [Samouczek i wskazówki [TutoUIReplacement_P2_T1] — tekst] UI 디자인 모드
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P2_T1].content
   limit: do 120 znaków
   EN: UI Modes
   PL: Tryb wyglądu UI
699. [Samouczek i wskazówki [TutoUIReplacement_P2_D1] — tekst] 모드 항목에서는 기본 모드와 다크 모드 중 하나를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P2_D1].content
   limit: do 120 znaków
   EN: You can select between "Default" and "Dark" modes here.
   PL: W sekcji trybu możesz wybrać pomiędzy trybem domyślnym a trybem ciemnym.
700. [Samouczek i wskazówki [TutoUIReplacement_P2_T2] — tekst] UI 스킨
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P2_T2].content
   limit: do 120 znaków
   EN: UI Skins
   PL: Skórki UI
701. [Samouczek i wskazówki [TutoUIReplacement_P2_D2] — tekst] UI 스킨은 향후 추가될 예정으로, 테마에 어울리는 꾸밈 요소가 UI 디자인 형태에 반영될 예정입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P2_D2].content
   limit: do 150 znaków
   EN: "UI Skins" is a feature that will be added in a future update. Various themed cosmetic UI skins will be available.
   PL: Skórki UI zostaną dodane w przyszłej aktualizacji i pozwolą nadać interfejsowi elementy ozdobne dopasowane do motywu.
702. [Samouczek i wskazówki [TutoUIReplacement_P3_T1] — tekst] 선택한 UI 변경안 미리보기
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P3_T1].content
   limit: do 120 znaków
   EN: Selected UI Preview
   PL: Podgląd wybranego wyglądu UI
703. [Samouczek i wskazówki [TutoUIReplacement_P3_D1] — tekst] 해당 버튼 선택 시, 관리자님이 고른 UI 디자인 모드와 스킨이 반영된 로비 화면을 미리 볼 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P3_D1].content
   limit: do 120 znaków
   EN: Select this button to preview the UI mode and/or UI Skin you have selected.
   PL: Kliknij ten przycisk, aby podejrzeć ekran lobby z wybranym przez Kierownika trybem oraz skórką UI.
704. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_15_title_01] — tekst] 외형 투영
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_15_title_01].content
   limit: do 120 znaków
   EN: Façade Projection
   PL: Projekcja Wyglądu
705. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_15_desc_01] — tekst] 편성에서 선택한 수감자의 외형 목록이 나열됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_15_desc_01].content
   limit: do 120 znaków
   EN: The selected Sinner's list of Façades will be shown here.
   PL: Wyświetla listę wyglądów wybranego w składzie Grzesznika.
706. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_16_title_01] — tekst] 투영 제작
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_16_title_01].content
   limit: do 120 znaków
   EN: Weave Projection
   PL: Tworzenie Projekcji
707. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_16_desc_01] — tekst] 아직 제작되지 않은 투영은 하단 버튼을 통해 제작이 가능합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_16_desc_01].content
   limit: do 120 znaków
   EN: Select this button to weave(craft) any unacquired Façades.
   PL: Jeszcze niewytworzone Projekcje możesz utkać za pomocą dolnego przycisku.
708. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_17_title_01] — tekst] 투영 제작
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_17_title_01].content
   (powtórzenie elementu 706 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_17_desc_01] — tekst] 투영은 자아 파편과 끈을 사용해 제작할 수 있습니다. 투영할 외형을 제작할 수감자의 자아 파편을 사용하면 보다 저렴한 비용으로 투영을 제작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_17_desc_01].content
   limit: do 180 znaków
   EN: Façades can be woven using the Sinners' Egoshards or Thread. Use the corresponding Sinner's Egoshards to weave Façades at a cheaper cost.
   PL: Projekcję wytworzysz za Odłamki E.G.O oraz Nici. Użycie Odłamków E.G.O Grzesznika, dla którego tworzysz wygląd, obniża koszt wytworzenia Projekcji.
710. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_18_title_01] — tekst] 외형 투영 적용
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_18_title_01].content
   limit: do 120 znaków
   EN: Project Façades
   PL: Zastosowanie Projekcji Wyglądu
711. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_18_desc_01] — tekst] 외형을 투영한 수감자에게는 외형 투영 아이콘이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_18_desc_01].content
   limit: do 120 znaków
   EN: Any Sinners who are equipped with Façades will be marked with a "Façade Projection" icon.
   PL: Grzesznicy z nałożoną Projekcją Wyglądu oznaczeni są ikoną Projekcji Wyglądu.
712. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_19_title_01] — tekst] 외형 투영 적용
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_19_title_01].content
   (powtórzenie elementu 710 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_19_desc_01] — tekst] 회사 메뉴의 지원 인격 설정에서도 외형을 투영한 인격을 배치할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_19_desc_01].content
   limit: do 120 znaków
   EN: You can also set Façade-wearing Identities as your Support Identities in the "Company" menu.
   PL: Tożsamości z nałożoną Projekcją Wyglądu możesz ustawić także jako Tożsamości wsparcia w menu Firmy.
714. [Samouczek i wskazówki [TutoEvent7512_Title] — tekst] LCB 정기검진 BokGak
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_Title].content
   limit: do 120 znaków
   EN: LCB Regular Check-up BokGak
   PL: Okresowe Badania LCB BokGak
715. [Samouczek i wskazówki [TutoEvent7512_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Samouczek i wskazówki [TutoEvent7512_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [LCB 정기검진 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P1_D1].content
   limit: do 160 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [LCB Regular Check-up BokGak Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Okresowe Badania LCB BokGak].
717. [Samouczek i wskazówki [TutoEvent7512_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Samouczek i wskazówki [TutoEvent7512_P2_D1] — tekst] LCB 정기검진 BokGak 이벤트 기간이 표시됩니다.\n\n이벤트 기간 동안 LCB 정기검진 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [정보서류]를 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [정보서류]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P2_D1].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the LCB Regular Check-up BokGak event is shown here.\n\nDuring the event, you can earn [Amassed Data] by clearing Event Stages. You can also earn [Amassed Data] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Amassed Data] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Okresowe Badania LCB BokGak.\n\nW trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Akta Informacyjne].\n\n※ [Akt Informacyjnych] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
719. [Samouczek i wskazówki [TutoEvent7512_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P3_T1].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Samouczek i wskazówki [TutoEvent7512_P3_D1] — tekst] LCB 정기검진 BokGak 이벤트는 스토리 스테이지를 포함하여 총 12개의 스테이지와 1개의 던전으로 구성됩니다.\n\n이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [정보서류]를 획득할 수 있습니다 (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P3_D1].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: LCB Regular Check-up BokGak consists of 12 stages, including story stages, and a single dungeon. Event Encounters also offer batches of [Amassed Data] as a first-time Clear bonus.
   PL: Wydarzenie Okresowe Badania LCB BokGak obejmuje łącznie 12 etapów (wraz z fabularnymi) oraz 1 loch.\n\nWalki wydarzenia zapewniają dodatkowo [Akta Informacyjne] za pierwsze ukończenie każdego etapu (1 raz na walkę).
721. [Samouczek i wskazówki [TutoEvent7512_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P4_T1].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Samouczek i wskazówki [TutoEvent7512_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [정보서류]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P4_D1].content
   limit: do 210 znaków
   EN: Having Identities and E.G.O from the LCB Regular Check-up BokGak event on your team increases the amount of [Amassed Data] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości i E.G.O wydarzenia zwiększa liczbę [Akt Informacyjnych] zdobywanych na etapach i w Lustrzanych Lochach.
723. [Samouczek i wskazówki [TutoEvent7512_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P5_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Samouczek i wskazówki [TutoEvent7512_P5_D1] — tekst] 획득한 [정보서류]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P5_D1].content
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Samouczek i wskazówki [TutoEvent7512_P6_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P6_D1].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Samouczek i wskazówki [TutoEvent7512_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 아나운서, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P6_D2].content
   limit: do 170 znaków
   EN: You can acquire the event reward Identity, Announcer, Ticket Deco, Banners, and various currencies from the [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia, Komentatora, ozdoby biletu, banery oraz rozmaite waluty.
727. [Samouczek i wskazówki [TutoEvent7512_P7_T1] — tekst] 기밀서류
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P7_T1].content
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Samouczek i wskazówki [TutoEvent7512_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [기밀서류]를 획득할 수 있습니다. 획득한 [기밀서류]는 [정보서류] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P7_D1].content
   limit: do 200 znaków
   EN: Rarely, you may obtain [Classified Data] from clearing Encounters. [Classified Data] is automatically converted to 20 [Amassed Data] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Tajnych Akt], które automatycznie zamieniają się na 20 [Akt Informacyjnych].
729. [Samouczek i wskazówki [TutoEvent7512_P8_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P8_T1].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Samouczek i wskazówki [TutoEvent7512_P8_D1] — tekst] 이벤트 기간 동안 LCB 정기검진 Hard 난이도를 진행할 수 있습니다. 주요 이야기 8-33 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P8_D1].content
   limit: do 200 znaków
   EN: LCB Regular Check-up Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 8-33.
   PL: W trakcie wydarzenia dostępny jest poziom Hard Okresowych Badań LCB. Odblokowuje się on po ukończeniu etapu 8-33 Głównej Opowieści.
731. [Samouczek i wskazówki [TutoEvent7512_P8_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P8_D2].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Samouczek i wskazówki [TutoEvent7512_P8_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P8_D3].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Samouczek i wskazówki [TutoEvent7512_P9_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 LCB 정기검진 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7512_P9_D1].content
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Samouczek i wskazówki [TutoEvent9125_Title] — tekst] 타래 엮기
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_Title].content
   limit: do 120 znaków
   EN: Twining Threads
   PL: Splatanie Pasm
735. [Samouczek i wskazówki [TutoEvent9125_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P1_T1].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Samouczek i wskazówki [TutoEvent9125_P1_D1] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [타래 엮기 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P1_D1].content
   limit: do 140 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Twining Threads Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Splatanie Pasm].
737. [Samouczek i wskazówki [TutoEvent9125_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P2_T1].content
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
