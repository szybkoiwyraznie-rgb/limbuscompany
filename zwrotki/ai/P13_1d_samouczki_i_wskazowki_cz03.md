# Paczka AI P13 (Fala 1 · 1D) — Samouczki systemowe i wskazówki ekranu ładowania (część 3/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P13_1d_samouczki_i_wskazowki_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P13_1d_samouczki_i_wskazowki_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Samouczek i wskazówki: TutorialMainUIText
- plik gry: `TutorialMainUIText.json`

1. [Samouczek i wskazówki [TutoEvent9125_P2_D1] — tekst] 타래 엮기 이벤트 기간이 표시됩니다.\n\n이벤트 기간 동안 타래 엮기 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [잘린 실]를 획득할 수 있습니다.\n\n※ 단, 채광과 거울굴절철도에서는 [잘린 실]를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P2_D1].content
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Twining Threads event is shown here.\n\nDuring the event, you can earn [Severed Thread] by clearing Event Stages. You can also earn [Severed Thread] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Severed Thread] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Splatanie Pasm.\n\nW trakcie wydarzenia ukończenie etapów Splatania Pasm, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Odcięte Nici].\n\n※ [Odciętych Nici] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
2. [Samouczek i wskazówki [TutoEvent9125_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P3_T1].content
   limit: do 120 znaków
   EN: Event Encounters
   PL: Walki wydarzenia
3. [Samouczek i wskazówki [TutoEvent9125_P3_D1] — tekst] 타래 엮기 이벤트는 스토리 스테이지를 포함하여 총 14개의 스테이지로 구성됩니다.\n이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [잘린 실]를 획득할 수 있습니다 (전투당 최초 1회 한정).\n\n타래 엮기 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [잘린 실]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P3_D1].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Twining Threads Event consists of 14 stages, including story stages. Said stages also offer batches of [Severed Thread] as a first-time Clear bonus (only for first-time clears of each Stage).\n\nYou can earn considerably more [Severed Thread] from Twining Threads Stages compared to Main Story Stages.
   PL: Wydarzenie Splatanie Pasm obejmuje łącznie 14 etapów wraz z fabularnymi.\nWalki wydarzenia zapewniają dodatkowo [Odcięte Nici] za pierwsze ukończenie każdego etapu (1 raz na walkę).\n\nEtapy Splatania Pasm zapewniają znacznie więcej [Odciętych Nici] niż etapy Głównej Opowieści.
4. [Samouczek i wskazówki [TutoEvent9125_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P4_T1].content
   limit: do 120 znaków
   EN: Event Bonus Units
   PL: Jednostki premiowane w wydarzeniu
5. [Samouczek i wskazówki [TutoEvent9125_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [잘린 실]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P4_D1].content
   limit: do 200 znaków
   EN: Having Identities and E.G.O from the Twining Threads event on your team increases the amount of [Severed Thread] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości i E.G.O wydarzenia zwiększa liczbę [Odciętych Nici] zdobywanych na etapach i w Lustrzanych Lochach.
6. [Samouczek i wskazówki [TutoEvent9125_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P5_T1].content
   limit: do 120 znaków
   EN: Reward Exchange
   PL: Wymiana nagród
7. [Samouczek i wskazówki [TutoEvent9125_P5_D1] — tekst] 획득한 [잘린 실]를 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P5_D1].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Reward Exchange] based on the number of [Severed Thread] you have.
   PL: Wydawaj zdobyte [Odcięte Nici] w [Wymianie nagród], aby odbierać rozmaite nagrody.
8. [Samouczek i wskazówki [TutoEvent9125_P6_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P6_D1].content
   limit: do 120 znaków
   EN: The [Reward Exchange]'s open duration is shown here.
   PL: W oknie [Wymiany nagród] widnieje okres odbioru nagród.
9. [Samouczek i wskazówki [TutoEvent9125_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 아나운서, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P6_D2].content
   limit: do 170 znaków
   EN: You can acquire the event reward Identity, Announcer, Ticket Deco, Banners, and various currencies from the [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia, Komentatora, ozdoby biletu, banery oraz rozmaite waluty.
10. [Samouczek i wskazówki [TutoEvent9125_P7_T1] — tekst] 잘리고 타버린 실뭉치
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P7_T1].content
   limit: do 120 znaków
   EN: Severed and Scorched Skein
   PL: Odcięty i Nadpalony Motek
11. [Samouczek i wskazówki [TutoEvent9125_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [잘리고 타버린 실뭉치]를 획득할 수 있습니다. 획득한 [잘리고 타버린 실뭉치]는 [잘린 실] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P7_D1].content
   limit: do 230 znaków
   EN: Rarely, you may obtain [Severed and Scorched Skein] from clearing Encounters. [Severed and Scorched Skein] is automatically converted to 20 [Severed Thread] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Odciętego i Nadpalonego Motka], który automatycznie zamienia się na 20 [Odciętych Nici].
12. [Samouczek i wskazówki [TutoEvent9125_P8_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 타래 엮기 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P8_D1].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Twining Threads combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Splatania Pasm możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
13. [Samouczek i wskazówki [TutoEvent9125_P9_T1] — tekst] 사영전투][투전영사
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P9_T1].content
   limit: do 120 znaków
   EN: Reflectrial][lairtcelfeR
   PL: Walka Projekcyjna][anjyckejorP aklaW
14. [Samouczek i wskazówki [TutoEvent9125_P9_D1] — tekst] 이벤트 2주차에는 사영전투][투전영사가 추가되며,\n해당 이벤트의 스테이지를 전부 클리어한 경우 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P9_D1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reflectrial][lairtcelfeR will be added to the game in the second week of the Twining Threads Event.\n\nEntry to Reflectrial][lairtcelfeR will be unlocked upon clearing all Event Stages.
   PL: W 2. tygodniu wydarzenia dodana zostanie Walka Projekcyjna][anjyckejorP aklaW,\nodblokowywana po ukończeniu wszystkich etapów wydarzenia.
15. [Samouczek i wskazówki [TutoEvent9125_P9_D2] — tekst] 이곳에서는 이벤트 보스가 한층 더 강화된 상태로 등장하며,\n다수의 파티를 활용하여 일정 턴 이내에 이벤트 보스를 클리어하는 것이 목표입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9125_P9_D2].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reflectrial][lairtcelfeR features a stronger version of the Event Boss unit.\nPlan out your teams and clear the battle against the Event Boss unit within a certain number of turns.
   PL: Boss wydarzenia pojawia się tu w znacznie wzmocnionej wersji,\na twoim celem jest pokonanie go w określonej liczbie tur przy użyciu kilku drużyn.
16. [Samouczek i wskazówki [TutoBossraid_Title] — tekst] 사영전투][투전영사
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_Title].content
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Samouczek i wskazówki [TutoBossraid_P1_T1] — tekst] 개방 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P1_T1].content
   limit: do 120 znaków
   EN: Entry Period
   PL: Okres dostępności
18. [Samouczek i wskazówki [TutoBossraid_P1_D1] — tekst] 선택한 챕터의 보스를 도전할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P1_D1].content
   limit: do 170 znaków
   EN: Reflectrial][lairtcelfeR has a limited availability period during which you may battle the Event Boss unit of the selected Chapter.
   PL: Wyświetlany jest okres, w którym możesz rzucić wyzwanie bossowi wybranego rozdziału.
19. [Samouczek i wskazówki [TutoBossraid_P1_D2] — tekst] 보스를 클리어하면, 1회에 한하여 보상을 획득할 수 있습니다. 특정 턴 이내로 클리어한 경우, 추가 보상을 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P1_D2].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the boss battle yields a first-time clear reward.\nClear the boss fight under certain turn counts to obtain extra rewards.
   PL: Pokonanie bossa zapewnia jednorazową nagrodę.\nUkończenie walki w określonej liczbie tur gwarantuje dodatkowe nagrody.
20. [Samouczek i wskazówki [TutoBossraid_P1_D3] — tekst] 이벤트 BokGak으로 추가된 보스는 별도의 개방 기간 없이 영구적으로 도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P1_D3].content
   limit: do 120 znaków
   EN: Battle against boss units added in BokGak Events are available indefinitely.
   PL: Bossowie dodani w ramach wydarzeń BokGak dostępni są bezterminowo.
21. [Samouczek i wskazówki [TutoBossraid_P2_T1] — tekst] 권장 사양
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P2_T1].content
   limit: do 120 znaków
   EN: Recommended Specs
   PL: Zalecane parametry
22. [Samouczek i wskazówki [TutoBossraid_P2_D1] — tekst] 사영전투][투전영사는 고난이도 콘텐츠이므로,\n인격과 E.G.O를 권장 사양에 맞추어 충분히 성장시킨\n다음에 도전하시길 바랍니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P2_D1].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reflectrial][lairtcelfeR is a high-difficulty challenge. Level up and Uptie/Threadspin your Identities and E.G.O to meet the recommended specs before entering the battle.
   PL: Walka Projekcyjna][anjyckejorP aklaW to zawartość o wysokim poziomie trudności —\nprzed podjęciem wyzwania odpowiednio rozwiń Tożsamości oraz E.G.O\ndo zalecanych parametrów.
23. [Samouczek i wskazówki [TutoBossraid_P2_T2] — tekst] 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P2_T2].content
   limit: do 120 znaków
   EN: Difficulty
   PL: Poziom trudności
24. [Samouczek i wskazówki [TutoBossraid_P2_D2] — tekst] 난이도는 Normal, Hard 2종으로 구분되며,\nHard 난이도는 Normal 난이도 클리어 시 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P2_D2].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reflectrial][lairtcelfeR has 2 difficulty levels: Normal and Hard.\nHard Difficulty is unlocked upon clearing the content on Normal Difficulty.
   PL: Dostępne są 2 poziomy trudności: Normal oraz Hard.\nPoziom Hard odblokowuje się po ukończeniu poziomu Normal.
25. [Samouczek i wskazówki [TutoBossraid_P3_T1] — tekst] 사영 효과
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P3_T1].content
   limit: do 120 znaków
   EN: Effect: Shade of Reflection
   PL: Efekty Odbicia
26. [Samouczek i wskazówki [TutoBossraid_P3_D1] — tekst] 사영전투][투전영사에서는 각 전투와\n페이즈에 따라 특별한 효과가 적용됩니다.\n\n이를 고려하여 편성하면 전투를 더욱\n유리하게 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P3_D1].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reflectrial][lairtcelfeR features unique effects in each Encounter and combat phase.\n\nIt is recommended to plan out your teams by taking these effects into account before entering the battle.
   PL: W Walce Projekcyjnej][ąnjyckejorP ęklaW w każdym starciu i fazie\nobowiązują specjalne efekty.\n\nUwzględnij je podczas układania drużyn,\naby zyskać przewagę w walce.
27. [Samouczek i wskazówki [TutoBossraid_P4_T1] — tekst] 진행 방식
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P4_T1].content
   limit: do 120 znaków
   EN: Progression
   PL: Zasady rozgrywki
28. [Samouczek i wskazówki [TutoBossraid_P4_D1] — tekst] 사영전투][투전영사의 전반적인\n진행 방식을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P4_D1].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the general progression method of Reflectrial][lairtcelfeR under the "Progression" menu.
   PL: Tutaj sprawdzisz ogólne zasady przebiegu\nWalki Projekcyjnej][ąnjyckejorP ęklaW.
29. [Samouczek i wskazówki [TutoBossraid_P5_T1] — tekst] 적 정보 확인
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P5_T1].content
   limit: do 120 znaków
   EN: Enemy Information
   PL: Informacje o wrogu
30. [Samouczek i wskazówki [TutoBossraid_P5_D1] — tekst] 페이즈별 적의 정보, 스킬, 패시브를\n전투 전에 미리 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P5_D1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the enemy information, such as Skills and passives, before entering the battle.
   PL: Przed walką możesz zawczasu sprawdzić informacje,\numiejętności oraz pasywki wroga w poszczególnych fazach.
31. [Samouczek i wskazówki [TutoBossraid_P6_T1] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P6_T1].content
   limit: do 120 znaków
   EN: Team Loadout
   PL: Skład drużyny
32. [Samouczek i wskazówki [TutoBossraid_P6_D1] — tekst] 전투에서는 최대 3개의 편성을 순차적으로 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P6_D1].content
   limit: do 120 znaków
   EN: Reflectrial][lairtcelfeR battles allow a maximum of 3 Team Loadouts to be used in order.
   PL: W walce możesz użyć kolejno maksymalnie 3 składów.
33. [Samouczek i wskazówki [TutoBossraid_P6_D2] — tekst] 단, 이전 전투의 편성에 포함된 인격은 이후 편성에서 다시 사용할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P6_D2].content
   limit: do 120 znaków
   EN: However, Identities assigned to a previous battle cannot be reused in subsequent Loadouts.
   PL: Tożsamości użytych we wcześniejszym składzie nie można jednak wystawić ponownie w kolejnych składach.
34. [Samouczek i wskazówki [TutoBossraid_P7_D1] — tekst] 편성 하나당 최대 12턴 동안 전투를 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P7_D1].content
   limit: do 120 znaków
   EN: A 12-turn limit is applied to each Team Loadout.
   PL: Każdy skład może walczyć przez maksymalnie 12 tur.
35. [Samouczek i wskazówki [TutoBossraid_P8_D1] — tekst] 전투 진행 중 12턴이 넘거나 전투 종료를 선택하면 보스의 페이즈와 체력, 정신력, 남은 E.G.O 자원이 저장되고 다음 편성으로 이어서 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P8_D1].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Exceeding 12 turns or opting to end the battle on your current loadout will save the state of battle progression (Boss Unit's Combat Phase, HP, and SP; as well as E.G.O Resources owned).\n\nYou may continue progressing through the battle with the next loadout.
   PL: Po przekroczeniu 12 tur lub wybraniu zakończenia walki bieżącego składu zapisywane są faza bossa, jego PŻ i PP oraz pozostałe zasoby E.G.O,\na starcie możesz kontynuować kolejnym składem.
36. [Samouczek i wskazówki [TutoBossraid_P9_D1] — tekst] Normal 난이도 클리어 시, Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P9_D1].content
   limit: do 120 znaków
   EN: Hard Difficulty is unlocked upon clearing Normal Difficulty.
   PL: Ukończenie poziomu Normal odblokowuje poziom Hard.
37. [Samouczek i wskazówki [TutoBossraid_P10_D1] — tekst] Hard 난이도에서는 사영 효과 이외에도\n고난 효과가 추가로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P10_D1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hard Difficulty features "Tribulation" effects in addition to "Shade of Reflection" effects.
   PL: Na poziomie Hard oprócz Efektów Odbicia\nnakładane są dodatkowo efekty Prób.
38. [Samouczek i wskazówki [TutoBossraid_P11_T1] — tekst] 보상
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P11_T1].content
   limit: do 120 znaków
   EN: Rewards
   PL: Nagrody
39. [Samouczek i wskazówki [TutoBossraid_P11_D1] — tekst] 각 난이도별로 보스 클리어 시, 1회에 한하여\n보상을 획득할 수 있습니다. 특정 턴 이내로\n클리어한 경우, 추가 보상을 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P11_D1].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the boss battle on each difficulty yields their respective first-time clear rewards.\nClear the boss fight under certain turn counts to obtain extra rewards.
   PL: Za pokonanie bossa na każdym poziomie trudności otrzymasz\njednorazową nagrodę. Ukończenie w określonej liczbie tur\nzapewnia dodatkowe nagrody.
40. [Samouczek i wskazówki [TutoEvent7522_P1_T1] — tekst] 심야청소 BokGak
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P1_T1].content
   limit: do 120 znaków
   EN: Nocturnal Sweeping BokGak
   PL: Nocne Sprzątanie BokGak
41. [Samouczek i wskazówki [TutoEvent7522_P1_D1] — tekst] 심야청소 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P1_D1].content
   limit: do 120 znaków
   EN: Unlocking Nocturnal Sweeping
   PL: Odblokowanie Nocnego Sprzątania
42. [Samouczek i wskazówki [TutoEvent7522_P1_D2] — tekst] 유리창이나 운전석에 있는 이벤트 배너를 통해 [심야청소 BokGak 이벤트 창]으로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P1_D2].content
   limit: do 160 znaków
   EN: Select the Event banner from either the Window or the Drive menu to enter the [Nocturnal Sweeping BokGak Event] menu.
   PL: Wybierz baner wydarzenia w Oknie lub Jeździe, aby przejść do [okna wydarzenia Nocne Sprzątanie BokGak].
43. [Samouczek i wskazówki [TutoEvent7522_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P2_T1].content
   limit: do 120 znaków
   EN: Event Period
   PL: Czas trwania wydarzenia
44. [Samouczek i wskazówki [TutoEvent7522_P2_D1] — tekst] 심야청소 BokGak 이벤트 기간이 표시됩니다. 이벤트 기간 동안 심야청소 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [청소부 연료통]을 획득할 수 있습니다. ※ 단, 채광과 거울굴절철도에서는 [청소부 연료통]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P2_D1].content
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of Nocturnal Sweeping BokGak Event is shown here.\n\nDuring the event, you can earn [Sweeper Fuel Cylinder] by clearing Event Stages. You can also earn [Sweeper Fuel Cylinder] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n\n※ However, [Sweeper Fuel Cylinder] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Nocne Sprzątanie BokGak.\nW trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Kanistry Płynnego Paliwa Sprzątacza].\n※ [Kanistrów Płynnego Paliwa Sprzątacza] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
45. [Samouczek i wskazówki [TutoEvent7522_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P3_T1].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
46. [Samouczek i wskazówki [TutoEvent7522_P3_D1] — tekst] 심야청소 BokGak 이벤트는 스토리 스테이지를 포함하여 총 12개의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P3_D1].content
   limit: do 120 znaków
   EN: Including Story Stages, Nocturnal Sweeping BokGak Event is composed of 12 Stages.
   PL: Wydarzenie Nocne Sprzątanie BokGak obejmuje łącznie 12 etapów wraz z fabularnymi.
47. [Samouczek i wskazówki [TutoEvent7522_P3_D2] — tekst] 이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [청소부 연료통]을 획득할 수 있습니다. (전투당 최초 1회 한정).
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P3_D2].content
   limit: do 170 znaków
   EN: Event Stages offer batches of [Sweeper Fuel Cylinder] as a first-time Clear bonus (only for first-time clears of each Stage).
   PL: Walki wydarzenia zapewniają dodatkowo [Kanistry Płynnego Paliwa Sprzątacza] za pierwsze ukończenie każdego etapu (1 raz na walkę).
48. [Samouczek i wskazówki [TutoEvent7522_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P4_T1].content
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Samouczek i wskazówki [TutoEvent7522_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격, E.G.O를 편성하여 스테이지와 거울 던전을 클리어하면 [청소부 연료통]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P4_D1].content
   limit: do 220 znaków
   EN: Having Identities and E.G.O from the Nocturnal Sweeping BokGak event on your team increases the amount of [Sweeper Fuel Cylinder] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości i E.G.O wydarzenia zwiększa liczbę [Kanistrów Płynnego Paliwa Sprzątacza] zdobywanych na etapach i w Lustrzanych Lochach.
50. [Samouczek i wskazówki [TutoEvent7522_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P5_T1].content
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
51. [Samouczek i wskazówki [TutoEvent7522_P5_D1] — tekst] 획득한 [청소부 연료통]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P5_D1].content
   limit: do 140 znaków
   EN: You can redeem various rewards from [Reward Exchange] by spending the [Sweeper Fuel Cylinder] you collected.
   PL: Wydawaj zdobyte [Kanistry Płynnego Paliwa Sprzątacza] w [Wymianie nagród], aby odbierać rozmaite nagrody.
52. [Samouczek i wskazówki [TutoEvent7522_P6_D1] — tekst] [보상 교환] 페이지에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P6_D1].content
   limit: do 120 znaków
   EN: The [Reward Exchange]'s open duration is shown here.
   PL: Na stronie [Wymiany nagród] widnieje okres odbioru nagród.
53. [Samouczek i wskazówki [TutoEvent7522_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 아나운서, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P6_D2].content
   limit: do 170 znaków
   EN: You can acquire the Event Reward Identity, Announcer, Ticket Deco, Banners, and various currencies from the [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia, Komentatora, ozdoby biletu, banery oraz rozmaite waluty.
54. [Samouczek i wskazówki [TutoEvent7522_P7_T1] — tekst] 연속 전투 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P7_T1].content
   limit: do 120 znaków
   EN: Chain Battle Encounters
   PL: Etapy Walki Seryjnej
55. [Samouczek i wskazówki [TutoEvent7522_P7_D1] — tekst] 심야청소의 전투는 연속 전투 방식으로 진행됩니다. 연속 전투에서는 아군이 죽더라도 정신력이 소모되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P7_D1].content
   limit: do 210 znaków
   EN: Encounters in the Nocturnal Sweeping event are Chain Battles. In Chain Battles, the Sinners will not lose their Sanity (SP) even if their allies are defeated.
   PL: Walki Nocnego Sprzątania to Walki Seryjne. W Walkach Seryjnych śmierć sojusznika nie obniża Poczytalności (PP) pozostałych.
56. [Samouczek i wskazówki [TutoEvent7522_P8_T1] — tekst] 특대형 액체 연료통
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P8_T1].content
   limit: do 120 znaków
   EN: [Sweeper Fuel Tank]
   PL: Wielki Zbiornik Płynnego Paliwa
57. [Samouczek i wskazówki [TutoEvent7522_P8_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 특대형 액체 연료통을 획득할 수 있습니다. 획득한 특대형 액체 연료통은 청소부 연료통 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P8_D1].content
   limit: do 210 znaków
   EN: There is a small chance to obtain a [Sweeper Fuel Tank] upon clearing an Encounter. [Sweeper Fuel Tank] are automatically converted to 20 [Sweeper Fuel Cylinder].
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie Wielkiego Zbiornika Płynnego Paliwa, który automatycznie zamienia się na 20 Kanistrów Płynnego Paliwa Sprzątacza.
58. [Samouczek i wskazówki [TutoEvent7522_P9_T1] — tekst] Hard 난이도
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P9_T1].content
   limit: do 120 znaków
   EN: Hard Difficulty
   PL: Poziom Hard
59. [Samouczek i wskazówki [TutoEvent7522_P9_D1] — tekst] 이벤트 기간 동안 심야청소 Hard 난이도를 진행할 수 있습니다. 주요 이야기 8-33 클리어 시 이벤트 스테이지 Hard 난이도가 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P9_D1].content
   limit: do 200 znaków
   EN: Nocturnal Sweeping Hard Difficulty will be unlocked during the Event period. The Hard Difficulty is unlocked upon clearing the Main Story Stage 8-33.
   PL: W trakcie wydarzenia dostępny jest poziom Hard Nocnego Sprzątania. Odblokowuje się on po ukończeniu etapu 8-33 Głównej Opowieści.
60. [Samouczek i wskazówki [TutoEvent7522_P9_D2] — tekst] Hard 난이도에서는 Normal 난이도보다 더 많은 이벤트 재화를 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P9_D2].content
   limit: do 120 znaków
   EN: Hard Difficulty rewards more Event currencies than the Normal Difficulty does.
   PL: Na poziomie Hard zdobędziesz więcej waluty wydarzenia niż na poziomie Normal.
61. [Samouczek i wskazówki [TutoEvent7522_P9_D3] — tekst] Hard 스테이지 클리어 시에도 초회 보상, EX 클리어 보상, 챕터 진행도 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P9_D3].content
   limit: do 180 znaków
   EN: You can earn first-time clear rewards, EX Clear rewards, and Chapter Progress rewards from clearing the Hard Difficulty Stages as well.
   PL: Ukończenie etapów Hard również zapewnia nagrody za pierwsze przejście, nagrody EX oraz nagrody postępu rozdziału.
62. [Samouczek i wskazówki [TutoEvent7522_P10_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 심야청소 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent7522_P10_D1].content
   limit: do 240 znaków
   EN: Even after the event fully ends, you will be able to experience the Nocturnal Sweeping combat Encounters and view its story anytime at Drive - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Nocnego Sprzątania możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
63. [Samouczek i wskazówki [TutoBossraid_P12_T1] — tekst] 교환 상점 - 상시 보상
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P12_T1].content
   limit: do 120 znaków
   EN: Reward Exchange - Standard Rewards
   PL: Wymiana nagród — nagrody stałe
64. [Samouczek i wskazówki [TutoBossraid_P12_D1] — tekst] 상시 보상 탭에서 익은 렌즈를 지불하여 다양한 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P12_D1].content
   limit: do 140 znaków
   EN: In the Standard Rewards tab, you can earn various currencies by using the Burnt-in Lens you have collected.
   PL: W zakładce nagród stałych wymienisz zebrane Wypalone Soczewki na rozmaite waluty.
65. [Samouczek i wskazówki [TutoRailway6_P1_T1] — tekst] 거울굴절철도 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P1_T1].content
   limit: do 120 znaków
   EN: Refraction Railway Opening
   PL: Odblokowanie Kolei Załamania
66. [Samouczek i wskazówki [TutoRailway6_P1_D1] — tekst] 활성화된 노선을 선택하여 재화 소모 없이 자유롭게 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P1_D1].content
   limit: do 120 znaków
   EN: You can enter the available Lines at no cost.
   PL: Wybierz aktywną linię, aby wejść swobodnie bez zużywania walut.
67. [Samouczek i wskazówki [TutoRailway6_P2_T1] — tekst] 입장 권장 사양
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P2_T1].content
   limit: do 120 znaków
   EN: Recommended Level & Tier
   PL: Zalecane parametry wejścia
68. [Samouczek i wskazówki [TutoRailway6_P2_D1] — tekst] 거울굴절철도 입장 권장 사양이 노선 측면에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P2_D1].content
   limit: do 120 znaków
   EN: Recommended levels & upgrade tiers are displayed on the side of the Line.
   PL: Zalecane parametry wejścia do Kolei Załamania widnieją z boku linii.
69. [Samouczek i wskazówki [TutoRailway6_P2_D2] — tekst] 거울굴절철도는 높은 난이도의 전투 컨텐츠입니다. 되도록이면, 권장 사양을 맞춘 이후에 입장하는 것을 추천드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P2_D2].content
   limit: do 220 znaków
   EN: Refraction Railways present combat Encounters with high levels of difficulty. We suggest that you enter the Railway after meeting the recommended levels & upgrade tiers.
   PL: Kolej Załamania to zawartość bojowa o wysokim poziomie trudności. Zalecamy wejście dopiero po spełnieniu sugerowanych parametrów rozwoju.
70. [Samouczek i wskazówki [TutoRailway6_P3_T1] — tekst] 6호선 역과 구간
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P3_T1].content
   limit: do 120 znaków
   EN: Line 6: Stations and Sections
   PL: Linia 6: stacje i odcinki
71. [Samouczek i wskazówki [TutoRailway6_P3_D1] — tekst] 6호선에는 총 8개의 역이 있으며, 여러 개의 역은 각 구간 별로 묶여 각각의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P3_D1].content
   limit: do 180 znaków
   EN: Refraction Railway Line 6 is composed of several Sections that tie several Stations into a single Stage. There are a total of 8 Stations.
   PL: Linia 6 liczy łącznie 8 stacji połączonych w poszczególne odcinki, z których każdy stanowi osobny etap.
72. [Samouczek i wskazówki [TutoRailway6_P3_D2] — tekst] 6호선은 5개의 구간으로 구성된 전투 스테이지가 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P3_D2].content
   limit: do 120 znaków
   EN: There are 5 Combat Encounter Stages, each called a 'Section'.
   PL: Linia 6 składa się z 5 odcinków bojowych.
73. [Samouczek i wskazówki [TutoRailway6_P3_D3] — tekst] 해당 역 클리어 시, 클리어 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P3_D3].content
   limit: do 120 znaków
   EN: Clearing the Section will record your Clear Turn Count.
   PL: Po ukończeniu stacji zapisywana jest liczba tur ukończenia.
74. [Samouczek i wskazówki [TutoRailway6_P3_D4] — tekst] 해당 역을 클리어하였을 때 분실물 보관소를 통해 얻을 수 있게되는 보상이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P3_D4].content
   limit: do 120 znaków
   EN: You can view the rewards for clearing that Station. Claim them at the Lost & Found.
   PL: Wyświetlane są nagrody za ukończenie danej stacji do odebrania w Biurze Rzeczy Znalezionych.
75. [Samouczek i wskazówki [TutoRailway6_P4_T1] — tekst] 구간 입장
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P4_T1].content
   limit: do 120 znaków
   EN: Entering Section
   PL: Wejście na odcinek
76. [Samouczek i wskazówki [TutoRailway6_P4_D1] — tekst] 해당 구간 클리어 시, 클리어 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P4_D1].content
   limit: do 120 znaków
   EN: Clearing the Section will record your Clear Turn Count.
   PL: Po ukończeniu odcinka zapisywana jest liczba tur ukończenia.
77. [Samouczek i wskazówki [TutoRailway6_P4_D2] — tekst] 이와 함께 제 1 구간으로부터 현재 구간까지의 각 구간별 클리어 턴이 모두 합해진 누적 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P4_D2].content
   limit: do 150 znaków
   EN: Below the Clear Turn Count is the Total Turn Count, which is the sum of all Clear Turn Counts from each Section.
   PL: Obok niej zapisywana jest łączna liczba tur będąca sumą tur ukończenia wszystkich odcinków od Odcinka 1 do bieżącego.
78. [Samouczek i wskazówki [TutoRailway6_P4_D3] — tekst] 해당 구간을 클리어하였을 때 분실물 보관소를 통해 얻을 수 있게 되는 보상이 하단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P4_D3].content
   limit: do 140 znaków
   EN: Below each Section, you can view the rewards for clearing that Section. Claim them at the Lost & Found.
   PL: Poniżej widnieją nagrody za ukończenie danego odcinka do odebrania w Biurze Rzeczy Znalezionych.
79. [Samouczek i wskazówki [TutoRailway6_P5_T1] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P5_T1].content
   limit: do 120 znaków
   EN: Observation Logs
   PL: Kompendium
80. [Samouczek i wskazówki [TutoRailway6_P5_D1] — tekst] 6호선에서는 특정 보스를 제외한 모든 적의 적 정보가 공개되어있습니다. 공략에 알맞은 인격과 E.G.O를 편성하여 전투를 진행하세요.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P5_D1].content
   limit: do 250 znaków
   EN: In Line 6, save for a certain boss enemy, all enemy info will be unlocked for viewing from the start. Prepare the appropriate strategy, Identity, and E.G.O loadout based on this information.
   PL: Na Linii 6 informacje o wszystkich wrogach oprócz określonego bossa są od razu jawne. Dobierz odpowiednią strategię, Tożsamości oraz E.G.O.
81. [Samouczek i wskazówki [TutoRailway6_P5_D2] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P5_D2].content
   limit: do 130 znaków
   EN: However, the damage bonus based on Observation Levels does not apply in the Refraction Railway.
   PL: Premia do obrażeń wynikająca z Poziomu Obserwacji nie jest jednak aktywna.
82. [Samouczek i wskazówki [TutoRailway6_P5_D3] — tekst] 6호선에서는 전투 중 재도전하거나 포기하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P5_D3].content
   limit: do 130 znaków
   EN: In Line 6, the updated Observation Level will be saved even if you give up or retry mid-Encounter.
   PL: Na Linii 6 zaktualizowane wpisy Kompendium zostają zapisane nawet przy ponowieniu lub poddaniu walki.
83. [Samouczek i wskazówki [TutoRailway6_P6_T1] — tekst] 전투 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P6_T1].content
   limit: do 120 znaków
   EN: Team Setup
   PL: Ustawienie drużyny
84. [Samouczek i wskazówki [TutoRailway6_P6_D1] — tekst] 보유한 인격과 E.G.O를 편성하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P6_D1].content
   limit: do 120 znaków
   EN: Choose a number of Identities and E.G.O to enter the Railway with.
   PL: Uformuj skład z posiadanych Tożsamości oraz E.G.O i rozpocznij wyprawę.
85. [Samouczek i wskazówki [TutoRailway6_P6_D2] — tekst] 인격의 레벨을 올리거나 동기화 단계 상승, E.G.O 환상 해석 단계 상승 시, 진행 중인 거울굴절철도에도 변경된 내용이 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P6_D2].content
   limit: do 230 znaków
   EN: If you level up, Uptie, or Threadspin your Identities or E.G.O outside the Refraction Railway, the changes will be applied to your characters in the Refraction Railway as well.
   PL: Podniesienie poziomu Tożsamości, stopnia Synchronizacji lub stopnia Splotu Nici E.G.O poza Koleją Załamania zostanie uwzględnione także w trwającej wyprawie.
86. [Samouczek i wskazówki [TutoRailway6_P6_D3] — tekst] 대기 인원에게는 시작 정신력 버프가 추가로 적용되며, 편성 순서가 늦을 수록 시작 정신력 값이 높아집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P6_D3].content
   limit: do 170 znaków
   EN: Backup Units receive Starting SP buffs, and Backup Units further back in the Deployment order receive greater Starting SP buffs.
   PL: Rezerwowi otrzymują premię początkowych PP — im dalsze miejsce w kolejności rozstawienia, tym wyższe początkowe PP.
87. [Samouczek i wskazówki [TutoRailway6_P6_D4] — tekst] 빼기 코인을 사용하는 인격의 경우에는 시작 정신력 버프가 음수값으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P6_D4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Minus Coin Identities receive negative Starting SP buffs.
   PL: U Tożsamości z Monetami Ujemnymi\npremia początkowych PP ma wartość ujemną.
88. [Samouczek i wskazówki [TutoRailway6_P7_T1] — tekst] 전투 편성 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P7_T1].content
   limit: do 120 znaków
   EN: Combat Deployment - Chain Battles
   PL: Ustawienie drużyny — Walka Seryjna
89. [Samouczek i wskazówki [TutoRailway6_P7_D1] — tekst] 6호선은 연속 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P7_D1].content
   limit: do 120 znaków
   EN: Combat Encounters in Line 6 are "Chain Battles."
   PL: Linia 6 rozgrywana jest w trybie Walki Seryjnej.
90. [Samouczek i wskazówki [TutoRailway6_P7_D2] — tekst] 연속 전투에서는 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P7_D2].content
   limit: do 160 znaków
   EN: In Chain Battles, when a Deployed unit is defeated, the Backup Units will fill their spot according to the Deployment order.
   PL: W Walce Seryjnej po śmierci uczestnika podstawowego jego miejsce zajmują rezerwowi zgodnie z ustaloną kolejnością.
91. [Samouczek i wskazówki [TutoRailway6_P7_D3] — tekst] 7명의 출격 인원과 5명의 대기 인원을 전부 설정하여야 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P7_D3].content
   limit: do 160 znaków
   EN: You can enter the Station only when you have selected both your Deployment and Backup units: 7 and 5 units, respectively.
   PL: Aby wejść, musisz obsadzić wszystkich 7 uczestników podstawowych oraz 5 rezerwowych.
92. [Samouczek i wskazówki [TutoRailway6_P8_T1] — tekst] 인격 편성 제한
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P8_T1].content
   limit: do 120 znaków
   EN: Identity Deployment Limits
   PL: Ograniczenia składu Tożsamości
93. [Samouczek i wskazówki [TutoRailway6_P8_D1] — tekst] 6호선에서는 5구간 진입 시 1구간 클리어 시점의 체력 비율과 정신력이 유지됩니다.\n또한 3,4 구간에서는 직전 구간에서 편성하여 전투를 진행한 인격을 사용할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P8_D1].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Line 6, your Team's HP percentage and SP at the point of clearing Section 1 will carry over to Section 5.\nIn Sections 3 and 4, you will be unable to use the Identities assigned in the Team Loadout used in the immediately preceding Sections.
   PL: Na Linii 6 przy wejściu na Odcinek 5 zachowywane są procent PŻ oraz PP z momentu ukończenia Odcinka 1.\nPonadto na Odcinkach 3 i 4 nie można użyć Tożsamości wystawionych w bezpośrednio poprzedzającym odcinku.
94. [Samouczek i wskazówki [TutoRailway6_P9_T1] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P9_T1].content
   limit: do 120 znaków
   EN: Combat
   PL: Walka
95. [Samouczek i wskazówki [TutoRailway6_P9_D1] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P9_D1].content
   limit: do 180 znaków
   EN: Every battle in the Refraction Railway will allow you to directly match ally skills against enemy skills, just like in Focused Encounters.
   PL: Wszystkie walki odbywają się w trybie starcia skupionego, w którym bezpośrednio kierujesz umiejętności sojuszników przeciwko umiejętnościom wrogów.
96. [Samouczek i wskazówki [TutoRailway6_P9_D2] — tekst] 하나의 역에서 기록되는 최대 턴 수는 100턴이며, 한 스테이지 내에서 턴 수가 100을 초과할 경우에는 패배한 것으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P9_D2].content
   limit: do 220 znaków
   EN: The highest Turn Count that can be recorded in each Station is 100 Turns. If your Turn Count goes beyond 100 Turns in a single Stage, the Encounter will end in defeat.
   PL: Maksymalna zapisywana liczba tur na stację wynosi 100 — przekroczenie 100 tur na jednym etapie skutkuje porażką.
97. [Samouczek i wskazówki [TutoRailway6_P10_T1] — tekst] 전투 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P10_T1].content
   limit: do 120 znaków
   EN: Combat - Chain Battles
   PL: Walka — Walka Seryjna
98. [Samouczek i wskazówki [TutoRailway6_P10_D1] — tekst] 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P10_D1].content
   limit: do 130 znaków
   EN: When a Deployed unit is defeated, the Backup units will fill their spot in the Deployment order.
   PL: Gdy uczestnik podstawowy zginie, rezerwowi zajmują jego miejsce zgodnie z ustaloną kolejnością.
99. [Samouczek i wskazówki [TutoRailway6_P10_D2] — tekst] 대기 인원이 출격 인원으로 전환되면, 적용 중인 서포트 패시브가 전투 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P10_D2].content
   limit: do 140 znaków
   EN: When a Backup unit is Deployed into battle, its Combat Passive activates instead of its Support Passive.
   PL: Gdy rezerwowy wchodzi do walki, jego pasywka wsparcia zamienia się w pasywkę bojową.
100. [Samouczek i wskazówki [TutoRailway6_P10_D3] — tekst] 출격인원이 사망한 경우, 적용 중인 전투 패시브가 서포트 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P10_D3].content
   limit: do 140 znaków
   EN: When a unit on the field is defeated, its Support Passive will activate instead of its Combat Passive.
   PL: Gdy uczestnik podstawowy zginie, jego pasywka bojowa zamienia się w pasywkę wsparcia.
101. [Samouczek i wskazówki [TutoRailway6_P11_T1] — tekst] 전투 - 남겨진 의지
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P11_T1].content
   limit: do 120 znaków
   EN: Combat - Lingering Determination
   PL: Walka — Pozostawiona Wola
102. [Samouczek i wskazówki [TutoRailway6_P11_D1] — tekst] 6호선에서는 인격 사망 시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻으며, 기존 연속 전투와 같이 다른 아군의 정신력이 감소하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P11_D1].content
   limit: do 270 znaków
   EN: In Line 6, when an Identity is killed, they release E.G.O resources based on the ranks and Affinities of their Base Attack Skills. And just like in Chain Battles, their deaths will not reduce other allies' SP.
   PL: Na Linii 6 śmierć Tożsamości zapewnia zasoby E.G.O odpowiadające grzechom jej podstawowych umiejętności ataku w liczbie równej ich randze, a tak jak w Walkach Seryjnych nie obniża PP pozostałych sojuszników.
103. [Samouczek i wskazówki [TutoRailway6_P12_T1] — tekst] 6호선에 등장하는 일부 적들에게는 편성 순서가 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P12_T1].content
   limit: do 120 znaków
   EN: Certain enemies in Line 6 will gain certain effects based on their Deployment orders.
   PL: Niektórzy wrogowie na Linii 6 podlegają efektom kolejności rozstawienia.
104. [Samouczek i wskazówki [TutoRailway6_P13_T1] — tekst] 클리어 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P13_T1].content
   limit: do 120 znaków
   EN: Clear Info
   PL: Informacje o ukończeniu
105. [Samouczek i wskazówki [TutoRailway6_P13_D1] — tekst] 각 역을 클리어한 후, 클리어 정보 창에서 클리어 턴, 누적 턴, 각 전투에서 획득한 효과, 전투 참여 인격 등의 통계를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P13_D1].content
   limit: do 230 znaków
   EN: After clearing each Station, you can view statistics such as Clear Turns, Total Turns, effects obtained in each Encounter, and participating Identities in the Clear Info menu.
   PL: Po ukończeniu każdej stacji w oknie informacji sprawdzisz tury ukończenia, łączne tury, efekty zdobyte w poszczególnych starciach oraz statystyki uczestniczących Tożsamości.
106. [Samouczek i wskazówki [TutoRailway6_P14_D1] — tekst] 역 클리어 이후 남은 E.G.O 자원은 다음 역에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P14_D1].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a Station can be carried over to the next Station.
   PL: Zasoby E.G.O pozostałe po ukończeniu stacji można wykorzystać na następnej stacji.
107. [Samouczek i wskazówki [TutoRailway6_P15_D1] — tekst] 아군이 모두 전멸하였다면 입장 화면으로 돌아가 편성 순서를 다시 설정하거나 현재 전투를 즉시 재도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P15_D1].content
   limit: do 210 znaków
   EN: If all of your allies are defeated, you can choose between returning to the Team Loadout menu to change your Deployment orders, and immediately retrying the battle.
   PL: W razie zagłady całej drużyny możesz wrócić do ekranu wejścia, aby zmienić kolejność rozstawienia, albo natychmiast ponowić bieżącą walkę.
108. [Samouczek i wskazówki [TutoRailway6_P16_T1] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P16_T1].content
   limit: do 120 znaków
   EN: Breaking Records
   PL: Bicie rekordów
109. [Samouczek i wskazówki [TutoRailway6_P16_D1] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P16_D1].content
   limit: do 120 znaków
   EN: During an expedition, you can choose to start over from previously cleared Stages.
   PL: W trakcie wyprawy możesz rozpocząć grę od nowa od wybranego ukończonego wcześniej etapu.
110. [Samouczek i wskazówki [TutoRailway6_P16_D2] — tekst] 특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P16_D2].content
   limit: do 220 znaków
   EN: When you do so, the battle will start with the Sinners’ statuses and E.G.O resources reverted to that point, and any progress you've made since that Stage will be reset.
   PL: Rozpoczęcie od wybranego etapu przywraca stan Tożsamości oraz posiadane zasoby E.G.O z momentu wejścia na ten etap, a rekordy późniejszych etapów zostają wyczyszczone.
111. [Samouczek i wskazówki [TutoRailway6_P17_T1] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P17_T1].content
   limit: do 120 znaków
   EN: Banner Requisites
   PL: Warunki zdobycia banerów
112. [Samouczek i wskazówki [TutoRailway6_P17_D1] — tekst] 거울굴절철도 6호선 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P17_D1].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 6 banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 6.
113. [Samouczek i wskazówki [TutoRailway6_P18_T1] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P18_T1].content
   limit: do 120 znaków
   EN: The Lost & Found
   PL: Biuro Rzeczy Znalezionych
114. [Samouczek i wskazówki [TutoRailway6_P18_D1] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P18_D1].content
   limit: do 130 znaków
   EN: After clearing a Stage in the Line for the first time, the rewards will be sent to the Lost & Found.
   PL: Po pierwszym ukończeniu etapu nagroda trafia do Biura Rzeczy Znalezionych i zostaje aktywowana.
115. [Samouczek i wskazówki [TutoRailway6_P18_D2] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P18_D2].content
   limit: do 150 znaków
   EN: To gain access to a reward for the first time at Lost & Found, a number of Enkephalin Modules will be required.
   PL: Aby po raz pierwszy odebrać nagrody w Biurze Rzeczy Znalezionych, należy jednorazowo zapłacić określoną liczbę Modułów Enkefaliny.
116. [Samouczek i wskazówki [TutoRailway6_P18_D3] — tekst] 이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P18_D3].content
   limit: do 120 znaków
   EN: Afterward, you may freely access it and claim rewards you’ve earned at no additional cost.
   PL: Kolejne odblokowane nagrody odbierzesz w dowolnej chwili bez dodatkowych Modułów Enkefaliny.
117. [Samouczek i wskazówki [TutoRailway6_P19_T1] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P19_T1].content
   limit: do 120 znaków
   EN: Total Record
   PL: Historia rekordów
118. [Samouczek i wskazówki [TutoRailway6_P19_D1] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P19_D1].content
   limit: do 150 znaków
   EN: Upon clearing the final Stage, your Refraction Railway play record will be saved. Up to 20 records can be viewed.
   PL: Po ukończeniu finałowego etapu zapisywany jest rekord przejścia Kolei Załamania; możesz przeglądać maksymalnie 20 rekordów.
119. [Samouczek i wskazówki [TutoRailway6_P19_D2] — tekst] 기록이 20개를 넘어갈 경우에는 누적 턴 수가 많은 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway6_P19_D2].content
   limit: do 130 znaków
   EN: If you have more than 20 records, records with the highest Total Turns will be deleted first.
   PL: Po przekroczeniu 20 rekordów w pierwszej kolejności usuwane są zapisy z największą łączną liczbą tur.
120. [Samouczek i wskazówki [TutoEvent9127_Title] — tekst] 경험기억
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_Title].content
   limit: do 120 znaków
   EN: Mnestic Experience
   PL: Pamięć Doświadczenia
121. [Samouczek i wskazówki [TutoEvent9127_P1_T1] — tekst] 이벤트 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P1_T1].content
   limit: do 120 znaków
   EN: Accessing the Event
   PL: Odblokowanie wydarzenia
122. [Samouczek i wskazówki [TutoEvent9127_P1_D1] — tekst] [경험기억 이벤트 페이지]는 주요 이야기의 0-4를 클리어한 경우 개방됩니다. 유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P1_D1].content
   limit: do 210 znaków
   EN: The [Mnestic Experience Event Page] opens after clearing Stage 0-4 of the Main Story. You may enter the event page via the banner on the Window or the Driverside.
   PL: [Strona wydarzenia Pamięć Doświadczenia] odblokowuje się po ukończeniu etapu 0-4 Głównej Opowieści. Wejdziesz na nią przez baner wydarzenia w Oknie lub Jeździe.
123. [Samouczek i wskazówki [TutoEvent9127_P2_T1] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P2_T1].content
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Samouczek i wskazówki [TutoEvent9127_P2_D1] — tekst] 경험기억 이벤트 기간이 표시됩니다.\n이벤트 기간 동안 경험기억 스테이지, 거울 던전을 클리어하거나 주요 이야기 스테이지를 이벤트 시작 후 처음으로 클리어할 경우, [사진들]을 획득할 수 있습니다.\n※ 단, 채광과 거울굴절철도에서는 [사진들]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P2_D1].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The duration of the Mnestic Experience event is shown here.\nDuring the event, you can earn [Photos] by clearing Event Stages. You can also earn [Photos] by clearing the Mirror Dungeons or clearing Main Story Stages for the first time.\n※ However, [Photos] cannot be obtained in Luxcavations and Refraction Railways.
   PL: Tutaj widnieje czas trwania wydarzenia Pamięć Doświadczenia.\nW trakcie wydarzenia ukończenie etapów wydarzenia, Lustrzanych Lochów lub pierwsze od startu wydarzenia ukończenie etapów Głównej Opowieści zapewnia [Zdjęcia].\n※ [Zdjęć] nie można zdobyć w Lochach Wydobywczych ani w Kolei Załamania.
125. [Samouczek i wskazówki [TutoEvent9127_P3_T1] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P3_T1].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Samouczek i wskazówki [TutoEvent9127_P3_D1] — tekst] 경험기억 이벤트는 스토리 스테이지를 포함하여 총 11개의 스테이지와 1개의 던전으로 구성됩니다.\n이벤트 전투에서는 클리어 보상과 별개로 초회 보상으로 [사진들]을 획득할 수 있습니다 (전투당 최초 1회 한정).\n\n경험기억 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [사진들]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P3_D1].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Mnestic Experience Event consists of 11 stages, including story stages, and a single dungeon. Said stages also offer batches of [Photos] as a first-time Clear bonus (only for first-time clears of each Stage).\n\nYou can earn considerably more [Photos] from Mnestic Experience Stages compared to Main Story Stages.
   PL: Wydarzenie Pamięć Doświadczenia obejmuje łącznie 11 etapów (wraz z fabularnymi) oraz 1 loch.\nWalki wydarzenia zapewniają dodatkowo [Zdjęcia] za pierwsze ukończenie każdego etapu (1 raz na walkę).\n\nEtapy Pamięci Doświadczenia zapewniają znacznie więcej [Zdjęć] niż etapy Głównej Opowieści.
127. [Samouczek i wskazówki [TutoEvent9127_P4_T1] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P4_T1].content
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Samouczek i wskazówki [TutoEvent9127_P4_D1] — tekst] 이벤트 기간 동안 이벤트 특화 대상 인격을 편성하여 스테이지와 거울 던전을 클리어하면 [사진들]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P4_D1].content
   limit: do 150 znaków
   EN: Having Bonus Identities on your team increases the amount of [Photos] earned from Stages and Mirror Dungeons.
   PL: Wystawienie premiowanych Tożsamości w drużynie zwiększa liczbę [Zdjęć] zdobywanych na etapach i w Lustrzanych Lochach.
129. [Samouczek i wskazówki [TutoEvent9127_P5_T1] — tekst] 보상 교환
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P5_T1].content
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
130. [Samouczek i wskazówki [TutoEvent9127_P5_D1] — tekst] 획득한 [사진들]을 소모하여 [보상 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P5_D1].content
   limit: do 130 znaków
   EN: You can redeem various rewards from the [Reward Exchange] based on the number of [Photos] you have.
   PL: Wydawaj zdobyte [Zdjęcia] w [Wymianie nagród], aby odbierać rozmaite nagrody.
131. [Samouczek i wskazówki [TutoEvent9127_P6_D1] — tekst] [보상 교환] 창에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P6_D1].content
   (powtórzenie elementu 8 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
132. [Samouczek i wskazówki [TutoEvent9127_P6_D2] — tekst] [보상 교환] 창에서 이벤트 배포 인격, 티켓 꾸미기와 장식 배너, 각종 재화를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P6_D2].content
   limit: do 150 znaków
   EN: You can acquire the event reward Identity, Ticket Deco, banners, and various currencies from [Reward Exchange] menu.
   PL: W oknie [Wymiany nagród] zdobędziesz darmową Tożsamość wydarzenia, ozdoby biletu, banery oraz rozmaite waluty.
133. [Samouczek i wskazówki [TutoEvent9127_P7_T1] — tekst] 사진더미들
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P7_T1].content
   limit: do 120 znaków
   EN: Photo Bundles
   PL: Stosy Zdjęć
134. [Samouczek i wskazówki [TutoEvent9127_P7_D1] — tekst] 전투에서 승리할 경우, 낮은 확률로 [사진더미들]을 획득할 수 있습니다. 획득한 [사진더미들]은 [사진들] 20개로 자동 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P7_D1].content
   limit: do 180 znaków
   EN: Rarely, you may obtain [Photo Bundles] from clearing Encounters. [Photo Bundles] is automatically converted to 20 [Photos] upon acquisition.
   PL: Po zwycięstwie w walce masz niewielką szansę na zdobycie [Stosów Zdjęć], które automatycznie zamieniają się na 20 [Zdjęć].
135. [Samouczek i wskazówki [TutoEvent9127_P8_D1] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 경험기억 전투를 다시 즐기거나 스토리를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoEvent9127_P8_D1].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Mnestic Experience combat Encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Pamięci Doświadczenia możesz w każdej chwili odtworzyć w menu Jazda — [Deviazione] oraz Teatr — [Opowieści Poboczne].
136. [Samouczek i wskazówki [TutoBossraid_P13_T1] — tekst] 교환 상점 - 한정 보상
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P13_T1].content
   limit: do 120 znaków
   EN: Reward Exchange - Limited Rewards
   PL: Wymiana nagród — nagrody limitowane
137. [Samouczek i wskazówki [TutoBossraid_P13_D1] — tekst] 한정 보상 탭에서 풀린 필름을 지불하여 이벤트 한정 보상을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P13_D1].content
   limit: do 150 znaków
   EN: In the Limited Rewards tab, you can earn event Limited Rewards by using the Unrolled Film you have collected.
   PL: W zakładce nagród limitowanych wymienisz zebrane Rozwinięte Klisze na limitowane nagrody wydarzenia.
138. [Samouczek i wskazówki [TutoBossraid_P13_D2] — tekst] 한정 보상 교환은 이벤트 보상 교환 기간까지만 진행할 수 있습니다.\n이벤트 보상 교환 기간이 종료되면, 한정 보상 탭이 사라지며, 풀린 필름은 상시 보상 교환에 사용되는 익은 렌즈로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoBossraid_P13_D2].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Limited Reward exchange is only available during the Event Reward Exchange Period. Once the Event Reward Exchange Period is over, the Limited Rewards tab will become inaccessible, and any Unrolled Film you have obtained will be converted into Burnt-in Lens.
   PL: Wymiana nagród limitowanych dostępna jest wyłącznie w okresie wymiany wydarzenia.\nPo jego zakończeniu zakładka nagród limitowanych znika, a wszystkie Rozwinięte Klisze zamieniają się w Wypalone Soczewki służące do wymiany nagród stałych.
139. [Samouczek i wskazówki [TutoUIReplacement_P4_T1] — tekst] 로비 BGM 변경
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P4_T1].content
   limit: do 120 znaków
   EN: Setting Lobby BGM
   PL: Zmiana muzyki lobby
140. [Samouczek i wskazówki [TutoUIReplacement_P4_D1] — tekst] 해당 버튼을 통해 로비 BGM을 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P4_D1].content
   limit: do 120 znaków
   EN: Click this button to set the Lobby BGM.
   PL: Kliknij ten przycisk, aby ustawić muzykę w tle (BGM) ekranu lobby.
141. [Samouczek i wskazówki [TutoUIReplacement_P5_T1] — tekst] BGM 변경 모드
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P5_T1].content
   limit: do 120 znaków
   EN: Changing BGM
   PL: Tryb zmiany BGM
142. [Samouczek i wskazówki [TutoUIReplacement_P5_D1] — tekst] BGM 변경은 유리창 BGM 혹은 수감자 별 BGM로 각각 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P5_D1].content
   limit: do 120 znaków
   EN: Either set a general Window BGM or select a specific soundtrack as BGM for each Sinner.
   PL: Możesz ustawić wspólną muzykę Okna albo osobny utwór dla każdego Grzesznika.
143. [Samouczek i wskazówki [TutoUIReplacement_P6_T1] — tekst] 유리창 BGM 설정
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P6_T1].content
   limit: do 120 znaków
   EN: Setting Window BGM
   PL: Ustawienia BGM Okna
144. [Samouczek i wskazówki [TutoUIReplacement_P6_D1] — tekst] 유리창 BGM 설정은 전체 음원에서 원하는 BGM을 선택하여 플레이 리스트에 등록합니다. BGM를 출력할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P6_D1].content
   limit: do 210 znaków
   EN: Click the "Set Window BGM" button to select the desired track from the available BGM list and add it to the playlist. The selected BGM can be played in full here.
   PL: W ustawieniach BGM Okna wybierasz dowolne utwory z pełnej biblioteki i dodajesz je do listy odtwarzania, aby słuchać ich w tle.
145. [Samouczek i wskazówki [TutoUIReplacement_P6_D2] — tekst] 등록된 플레이 리스트를 통해 유리창 BGM를 감상 할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P6_D2].content
   limit: do 120 znaków
   EN: Use your playlist to play the BGM in the Window.
   PL: Zarejestrowana lista odtwarzania będzie odtwarzana w Oknie.
146. [Samouczek i wskazówki [TutoUIReplacement_P7_T1] — tekst] 수감자 별 BGM 설정
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P7_T1].content
   limit: do 120 znaków
   EN: Setting Sinner BGM
   PL: Ustawienia BGM Grzeszników
147. [Samouczek i wskazówki [TutoUIReplacement_P7_D1] — tekst] 수감자 별 BGM 설정은 로비 화면에서 수감자 별로 각각 재생할 BGM들을 설정 할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P7_D1].content
   limit: do 160 znaków
   EN: Click the "Set Sinner BGM" button to customize the per-Sinner soundtrack. The selected BGM can be played in the Lobby.
   PL: Pozwala przypisać osobny utwór BGM każdemu Grzesznikowi na ekranie lobby.
148. [Samouczek i wskazówki [TutoUIReplacement_P8_T1] — tekst] 수감자 별 BGM 설정
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P8_T1].content
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Samouczek i wskazówki [TutoUIReplacement_P8_D1] — tekst] 수감자를 골라, 원하는 BGM 설정하면 해당 수감자 로비 화면에서 설정한 BGM이 재생됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoUIReplacement_P8_D1].content
   limit: do 130 znaków
   EN: Select a Sinner and set the desired BGM. The selected BGM will play on that Sinner's Lobby screen.
   PL: Wybierz Grzesznika i przypisz mu wybrany utwór — będzie on odtwarzany na ekranie lobby tego Grzesznika.
150. [Samouczek i wskazówki [Jukebox_P1_T1] — tekst] 주크박스
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P1_T1].content
   limit: do 120 znaków
   EN: Jukebox
   PL: Szafa grająca
151. [Samouczek i wskazówki [Jukebox_P1_D1] — tekst] 주크박스에서는 보유한 BGM들을 감상할 수 있는 공간입니다
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P1_D1].content
   limit: do 120 znaków
   EN: Enjoy your unlocked soundtracks from the Jukebox.
   PL: W Szafie grającej posłuchasz posiadanych utworów BGM.
152. [Samouczek i wskazówki [Jukebox_P1_D2] — tekst] BGM은 스토리 스테이지 클리어, 이벤트 보상, 자판기 등 다양한 방식으로 획득 할 수 있습니다
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P1_D2].content
   limit: do 190 znaków
   EN: Soundtracks can be obtained from various sources: Clearing story stages, claiming from event rewards, or purchasing from the Dispenser and more.
   PL: Utwory BGM zdobędziesz na różne sposoby: za kończenie etapów fabularnych, z nagród wydarzeń, w Automacie i nie tylko.
153. [Samouczek i wskazówki [Jukebox_P2_T1] — tekst] 버튼 기능
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P2_T1].content
   limit: do 120 znaków
   EN: Button Functions
   PL: Funkcje przycisków
154. [Samouczek i wskazówki [Jukebox_P2_D1] — tekst] 순환 버튼을 통해 순서대로 반복해서 듣거나, 셔플 버튼을 통해 무작위 순서대로 감상하실 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P2_D1].content
   limit: do 180 znaków
   EN: Press the "Repeat" button to listen to the playlist as ordered on repeat, or press the "Shuffle" button to play them in random order.
   PL: Przycisk powtarzania odtwarza utwory po kolei w pętli, a przycisk losowania odtwarza je w losowej kolejności.
155. [Samouczek i wskazówki [Jukebox_P3_T1] — tekst] 카테고리
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P3_T1].content
   limit: do 120 znaków
   EN: Categories
   PL: Kategorie
156. [Samouczek i wskazówki [Jukebox_P3_D1] — tekst] 원하는 카테고리를 누르고, 음악을 재생하면 해당 카테고리의 음악들만 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P3_D1].content
   limit: do 130 znaków
   EN: Select the Category you want and hit "Play" to listen to the soundtracks in the selected Category.
   PL: Wybierz interesującą cię kategorię i włącz odtwarzanie, aby słuchać wyłącznie utworów z tej kategorii.
157. [Samouczek i wskazówki [Jukebox_P4_T1] — tekst] 플레이 리스트
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P4_T1].content
   limit: do 120 znaków
   EN: Playlist
   PL: Lista odtwarzania
158. [Samouczek i wskazówki [Jukebox_P4_D1] — tekst] 원하는 BGM들을 모아서 듣고 싶은 경우 BGM의 + 버튼을 선택하여 플레이 리스트에 등록할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=Jukebox_P4_D1].content
   limit: do 120 znaków
   EN: Select the "+" button next to each soundtrack to add them to your own personalized playlist.
   PL: Kliknij przycisk „+” obok wybranego utworu BGM, aby dodać go do własnej listy odtwarzania.
159. [Samouczek i wskazówki [TutoRailway2BokGak_P1_T1] — tekst] 거울굴절철도 개방
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P1_T1].content
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [Samouczek i wskazówki [TutoRailway2BokGak_P1_D1] — tekst] 활성화된 노선을 선택하여 재화 소모 없이 자유롭게 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P1_D1].content
   (powtórzenie elementu 66 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Samouczek i wskazówki [TutoRailway2BokGak_P2_T1] — tekst] 입장 권장 사양
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P2_T1].content
   limit: do 120 znaków
   EN: Recommended Specs
   PL: Zalecane parametry wejścia
162. [Samouczek i wskazówki [TutoRailway2BokGak_P2_D1] — tekst] 거울굴절철도 입장 권장 사양이 노선 상단에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P2_D1].content
   limit: do 120 znaków
   EN: Recommended levels & upgrade tiers are displayed on each Line.
   PL: Zalecane parametry wejścia do Kolei Załamania widnieją u góry linii.
163. [Samouczek i wskazówki [TutoRailway2BokGak_P2_D2] — tekst] 되도록이면, 권장 사양을 맞춘 이후에 입장하는 것을 추천드립니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P2_D2].content
   limit: do 120 znaków
   EN: We suggest that you enter the Railway after meeting the recommended levels & upgrade tiers.
   PL: Zalecamy wejście po osiągnięciu sugerowanych parametrów rozwoju.
164. [Samouczek i wskazówki [TutoRailway2BokGak_P3_T1] — tekst] 2호선 역
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P3_T1].content
   limit: do 120 znaków
   EN: Line 2 Stations
   PL: Stacje Linii 2
165. [Samouczek i wskazówki [TutoRailway2BokGak_P3_D1] — tekst] 2호선에는 총 9개의 역으로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P3_D1].content
   limit: do 120 znaków
   EN: Line 2 has a total of 9 Stations.
   PL: Linia 2 liczy łącznie 9 stacji.
166. [Samouczek i wskazówki [TutoRailway2BokGak_P3_D2] — tekst] 각 순환 횟수에 따라 해당 스테이지에서 등장하는 보스의 역만 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P3_D2].content
   limit: do 120 znaków
   EN: Only the boss Stations present in each respective Cycle Count will be visible.
   PL: Zależnie od liczby cykli widoczne są wyłącznie stacje bossów występujących na danym etapie.
167. [Samouczek i wskazówki [TutoRailway2BokGak_P3_D3] — tekst] 해당 순환에 표시된 모든 역은 하나의 연속 전투 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P3_D3].content
   limit: do 140 znaków
   EN: Each Cycle consists of a single Chain Battle against every available Station for each respective Cycle.
   PL: Wszystkie stacje widoczne w danym cyklu tworzą razem jeden etap Walki Seryjnej.
168. [Samouczek i wskazówki [TutoRailway2BokGak_P4_T1] — tekst] 순환
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P4_T1].content
   limit: do 120 znaków
   EN: Cycle
   PL: Cykl
169. [Samouczek i wskazówki [TutoRailway2BokGak_P4_D1] — tekst] 노선 위에 있는 개방된 역을 모두 클리어하였다면 다음 순환으로 자동으로 넘어갑니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P4_D1].content
   limit: do 130 znaków
   EN: Upon clearing all open Stations on the Line, you will automatically continue to the next Cycle.
   PL: Po ukończeniu wszystkich otwartych stacji na linii automatycznie przechodzisz do następnego cyklu.
170. [Samouczek i wskazówki [TutoRailway2BokGak_P4_D2] — tekst] 순환을 진행할 경우, 순환 횟수가 1 증가합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P4_D2].content
   limit: do 120 znaków
   EN: Should you choose to continue the Cycle, you will gain 1 Cycle Count.
   PL: Przejście do kolejnego cyklu zwiększa liczbę cykli o 1.
171. [Samouczek i wskazówki [TutoRailway2BokGak_P4_D3] — tekst] 일부 역은 순환 횟수에 따라 추가로 개방됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P4_D3].content
   limit: do 120 znaków
   EN: Access to certain Stations are unlocked at higher Cycle Counts.
   PL: Niektóre stacje odblokowują się wraz ze wzrostem liczby cykli.
172. [Samouczek i wskazówki [TutoRailway2BokGak_P4_D4] — tekst] 직전 순환을 다시 도전할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P4_D4].content
   limit: do 120 znaków
   EN: You cannot return to the immediately preceding Cycle.
   PL: Nie można ponownie rozegrać bezpośrednio poprzedzającego cyklu.
173. [Samouczek i wskazówki [TutoRailway2BokGak_P5_T1] — tekst] 도감
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P5_T1].content
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Samouczek i wskazówki [TutoRailway2BokGak_P5_D1] — tekst] 2호선에서는 모든 적의 정보가 공개되어있습니다. 공략에 알맞은 인격과 E.G.O를 편성하여 전투를 진행하세요.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P5_D1].content
   limit: do 210 znaków
   EN: In Line 2, all enemy info will be unlocked for viewing from the start. Prepare the appropriate strategy, Identity, and E.G.O loadout based on this information.
   PL: Na Linii 2 informacje o wszystkich wrogach są jawne od samego początku. Dobierz odpowiedni skład Tożsamości oraz E.G.O pod kątem strategii.
175. [Samouczek i wskazówki [TutoRailway2BokGak_P5_D2] — tekst] 단, 관찰 단계에 따른 피해량 증가 효과는 적용되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P5_D2].content
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Samouczek i wskazówki [TutoRailway2BokGak_P5_D3] — tekst] 2호선에서는 전투 중 재도전하거나 포기하여도 전투 중 갱신된 도감 내용이 그대로 저장됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P5_D3].content
   limit: do 130 znaków
   EN: In Line 2, the updated Observation Level will be saved even if you give up or retry mid-Encounter.
   PL: Na Linii 2 zaktualizowane wpisy Kompendium zostają zapisane nawet przy ponowieniu lub poddaniu walki.
177. [Samouczek i wskazówki [TutoRailway2BokGak_P6_T1] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_T1].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Samouczek i wskazówki [TutoRailway2BokGak_P6_D1] — tekst] 보유한 인격과 E.G.O를 편성하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_D1].content
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Samouczek i wskazówki [TutoRailway2BokGak_P6_D2] — tekst] 편성 인원은 매 순환마다 변경할 수 있습니다. 매 순환마다 수감자의 체력이 최대로 회복됩니다. 정신력은 이전 순환의 상태가 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_D2].content
   limit: do 220 znaków
   EN: Every new Cycle fully heals every Sinner's HP and presents an opportunity to change your Team loadout. However, the Sinners' SP will carry over from the previous Cycle's.
   PL: Skład drużyny można zmieniać w każdym cyklu. Z każdym nowym cyklem PŻ Grzeszników wracają do maksimum, natomiast PP przechodzą z poprzedniego cyklu.
180. [Samouczek i wskazówki [TutoRailway2BokGak_P6_D3] — tekst] 인격의 레벨을 올리거나, 동기화 단계 상승, E.G.O 환상 해석 단계 상승 시, 진행 중인 거울굴절철도에도 변경된 내용이 반영됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_D3].content
   limit: do 230 znaków
   EN: If you level up, Uptie, or Threadspin your Identities or E.G.O outside the Refraction Railway, the changes will be applied to your characters in the Refraction Railway as well.
   PL: Podniesienie poziomu Tożsamości, stopnia Synchronizacji lub stopnia Splotu Nici E.G.O poza Koleją Załamania zostanie uwzględnione także w trwającej wyprawie.
181. [Samouczek i wskazówki [TutoRailway2BokGak_P6_D4] — tekst] 대기 인원에게는 시작 정신력 버프가 추가로 적용되며, 편성 순서가 늦을 수록 시작 정신력 값이 높아집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_D4].content
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Samouczek i wskazówki [TutoRailway2BokGak_P6_D5] — tekst] 빼기 코인을 사용하는 인격의 경우에는 시작 정신력 버프가 음수값으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P6_D5].content
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Samouczek i wskazówki [TutoRailway2BokGak_P7_T1] — tekst] 전투 편성 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P7_T1].content
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
184. [Samouczek i wskazówki [TutoRailway2BokGak_P7_D1] — tekst] 2호선은 연속 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P7_D1].content
   limit: do 120 znaków
   EN: Combat Encounters in Line 2 are "Chain Battles."
   PL: Linia 2 rozgrywana jest w trybie Walki Seryjnej.
185. [Samouczek i wskazówki [TutoRailway2BokGak_P7_D2] — tekst] 연속 전투에서는 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P7_D2].content
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Samouczek i wskazówki [TutoRailway2BokGak_P7_D3] — tekst] 7명의 출격 인원과 5명의 대기 인원을 전부 설정하여야 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P7_D3].content
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Samouczek i wskazówki [TutoRailway2BokGak_P8_T1] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P8_T1].content
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Samouczek i wskazówki [TutoRailway2BokGak_P8_D1] — tekst] 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는 집중 전투 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P8_D1].content
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Samouczek i wskazówki [TutoRailway2BokGak_P8_D2] — tekst] 한 스테이지에서 기록되는 최대 턴 수는 100턴이며, 턴 수가 100을 초과할 경우에는 패배한 것으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P8_D2].content
   limit: do 220 znaków
   EN: The highest Turn Count that can be recorded in each Stage is 100 Turns. If your Turn Count goes beyond 100 Turns in a single Stage, the Encounter will end in defeat.
   PL: Maksymalna zapisywana liczba tur na etap wynosi 100 — przekroczenie 100 tur skutkuje porażką.
190. [Samouczek i wskazówki [TutoRailway2BokGak_P9_T1] — tekst] 전투 - 연속 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P9_T1].content
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Samouczek i wskazówki [TutoRailway2BokGak_P9_D1] — tekst] 출격 인원이 사망하였을 때, 대기 인원이 설정한 순서에 따라 그 자리를 채우게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P9_D1].content
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Samouczek i wskazówki [TutoRailway2BokGak_P9_D2] — tekst] 대기 인원이 출격 인원으로 전환되면, 적용 중인 서포트 패시브가 전투 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P9_D2].content
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Samouczek i wskazówki [TutoRailway2BokGak_P9_D3] — tekst] 출격인원이 사망한 경우, 적용 중인 전투 패시브가 서포트 패시브로 변경됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P9_D3].content
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Samouczek i wskazówki [TutoRailway2BokGak_P10_T1] — tekst] 전투 - 남겨진 의지
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P10_T1].content
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Samouczek i wskazówki [TutoRailway2BokGak_P10_D1] — tekst] 2호선에서는 인격 사망 시 보유한 기본 공격 스킬의 속성과 동일한 E.G.O 자원을 등급만큼 얻으며, 기존 연속 전투와 같이 다른 아군의 정신력이 감소하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P10_D1].content
   limit: do 270 znaków
   EN: In Line 2, when an Identity is killed, they release E.G.O resources based on the ranks and Affinities of their Base Attack Skills. And just like in Chain Battles, their deaths will not reduce other allies' SP.
   PL: Na Linii 2 śmierć Tożsamości zapewnia zasoby E.G.O odpowiadające grzechom jej podstawowych umiejętności ataku w liczbie równej ich randze, a tak jak w Walkach Seryjnych nie obniża PP pozostałych sojuszników.
196. [Samouczek i wskazówki [TutoRailway2BokGak_P11_T1] — tekst] 버프 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_T1].content
   limit: do 120 znaków
   EN: Select Buffs
   PL: Wybór wzmocnień
197. [Samouczek i wskazówki [TutoRailway2BokGak_P11_D1] — tekst] 순환을 진행할 때마다 아군 버프, 적 버프를 각각 1개씩 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_D1].content
   limit: do 120 znaków
   EN: At the end of every Cycle, you can choose 1 Ally Buff and 1 Enemy Buff.
   PL: Przy każdym kolejnym cyklu wybierasz po 1 wzmocnieniu sojuszników oraz 1 wzmocnieniu wrogów.
198. [Samouczek i wskazówki [TutoRailway2BokGak_P11_D2] — tekst] 선택한 모든 효과들은 이후의 전투에서 누적되어 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_D2].content
   limit: do 120 znaków
   EN: All selected Buffs will carry over to the coming encounters.
   PL: Wszystkie wybrane efekty kumulują się i obowiązują w kolejnych walkach.
199. [Samouczek i wskazówki [TutoRailway2BokGak_P11_D3] — tekst] 아군 버프 1종을 선택합니다. 직전 순환에서 선택한 효과는 고를 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_D3].content
   limit: do 120 znaków
   EN: Select 1 Ally Buff. You cannot select the same Buff you selected in the last Cycle.
   PL: Wybierz 1 wzmocnienie sojuszników. Nie możesz wybrać efektu wybranego w bezpośrednio poprzedzającym cyklu.
200. [Samouczek i wskazówki [TutoRailway2BokGak_P11_D4] — tekst] 적 버프를 1종 선택합니다. 이전에 선택한 효과를 고를 수 없습니다.\n단, 모든 효과를 한 번씩 선택하였다면 선택 기회가 초기화되어 다시 원하는 효과를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_D4].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select 1 Enemy Buff. You cannot select the same Buff you selected in the last Cycle.\nHowever, if all Buffs had been selected at least once, selection limits will reset and you can select any Buff you want again.
   PL: Wybierz 1 wzmocnienie wrogów. Nie możesz wybrać efektu wybranego wcześniej.\nJeśli jednak wszystkie efekty zostały już wybrane po razie, pula wyboru się resetuje i znów możesz wybrać dowolny efekt.
201. [Samouczek i wskazówki [TutoRailway2BokGak_P11_D5] — tekst] 직접 선택할 수 있는 버프 이외에 매 순환 시마다 1개의 고정 버프가 추가로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P11_D5].content
   limit: do 120 znaków
   EN: Aside from the Buffs you select, every Cycle also gives 1 fixed Buff.
   PL: Oprócz wybieranych wzmocnień każdy cykl nakłada dodatkowo 1 stałe wzmocnienie.
202. [Samouczek i wskazówki [TutoRailway2BokGak_P15_T1] — tekst] 종착역
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P15_T1].content
   limit: do 120 znaków
   EN: The Terminus
   PL: Stacja końcowa
203. [Samouczek i wskazówki [TutoRailway2BokGak_P15_D1] — tekst] 순환 횟수가 1 이상이면, 노선 중앙에 있는 종착역이 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P15_D1].content
   limit: do 130 znaków
   EN: If you are at 1 or higher Cycle Count, the Terminus in the middle of this Line will be activated.
   PL: Gdy liczba cykli wynosi co najmniej 1, aktywuje się Stacja końcowa pośrodku linii.
204. [Samouczek i wskazówki [TutoRailway2BokGak_P15_D2] — tekst] 종착역이 활성화되면, 어느 순환에서든 자유롭게 종착역에 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P15_D2].content
   limit: do 120 znaków
   EN: Once the Terminus is activated, you can access it from any Cycle.
   PL: Po aktywacji Stacji końcowej możesz swobodnie wejść na nią z dowolnego cyklu.
205. [Samouczek i wskazówki [TutoRailway2BokGak_P15_D3] — tekst] 종착역에 입장하면 더이상 이전 역으로 되돌아갈 수 없기 때문에 신중한 선택이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P15_D3].content
   limit: do 120 znaków
   EN: You cannot go back to the previous Station once you enter the Terminus. Choose carefully.
   PL: Po wejściu na Stację końcową nie można już wrócić na poprzednią stację — podejmij decyzję rozważnie.
206. [Samouczek i wskazówki [TutoRailway2BokGak_P15_D4] — tekst] 종착역을 클리어하는 것이 거울굴절철도 2호선의 최종 목표이며, 클리어하게 되면 순환 횟수와 누적 턴 수, 참여한 인격과 E.G.O, 버프 목록이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P15_D4].content
   limit: do 250 znaków
   EN: The ultimate goal of Refraction Railway Line 2 is to complete the Terminus. Upon completion, your Cycle Count, Total Turns, participating Identities & E.G.O, and selected Buffs will be recorded.
   PL: Ukończenie Stacji końcowej to ostateczny cel Kolei Załamania — Linii 2. Po jej przejściu zapisywane są liczba cykli, łączna liczba tur, uczestniczące Tożsamości i E.G.O oraz lista wzmocnień.
207. [Samouczek i wskazówki [TutoRailway2BokGak_P16_T1] — tekst] 클리어 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P16_T1].content
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Samouczek i wskazówki [TutoRailway2BokGak_P16_D1] — tekst] 각 역을 클리어한 후, 클리어 정보 창에서 클리어 턴, 누적 턴, 전투 참여 인격의 통계를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P16_D1].content
   limit: do 180 znaków
   EN: After clearing each Station, you can view statistics such as Clear Turns, Total Turns, and participating Identities in the Clear Info menu.
   PL: Po ukończeniu każdej stacji w oknie informacji sprawdzisz tury ukończenia, łączne tury oraz statystyki uczestniczących Tożsamości.
209. [Samouczek i wskazówki [TutoRailway2BokGak_P17_D1] — tekst] 역 클리어 이후 남은 E.G.O 자원은 다음 역에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P17_D1].content
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Samouczek i wskazówki [TutoRailway2BokGak_P18_D1] — tekst] 현재 완료한 순환 횟수와 누적 턴 수를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P18_D1].content
   limit: do 120 znaków
   EN: View your completed Cycle Counts and Total Turn Count here.
   PL: Tutaj sprawdzisz aktualną liczbę ukończonych cykli oraz łączną liczbę tur.
211. [Samouczek i wskazówki [TutoRailway2BokGak_P19_D1] — tekst] 아군이 모두 전멸하였다면 입장 화면으로 돌아가 편성 순서를 다시 설정하거나 현재 전투를 즉시 재도전할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P19_D1].content
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Samouczek i wskazówki [TutoRailway2BokGak_P20_T1] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P20_T1].content
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Samouczek i wskazówki [TutoRailway2BokGak_P20_D1] — tekst] 거울굴절철도 2호선 BokGak 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P20_D1].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring Refraction Railway Line 2 BokGak banners here.
   PL: Tutaj sprawdzisz warunki zdobycia banerów Kolei Załamania — Linii 2 BokGak.
214. [Samouczek i wskazówki [TutoRailway2BokGak_P21_T1] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P21_T1].content
   limit: do 120 znaków
   EN: Lost & Found
   PL: Biuro Rzeczy Znalezionych
215. [Samouczek i wskazówki [TutoRailway2BokGak_P21_D1] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 보상이 분실물 보관소에 등록되어 활성화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P21_D1].content
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Samouczek i wskazówki [TutoRailway2BokGak_P21_D2] — tekst] 분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P21_D2].content
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Samouczek i wskazówki [TutoRailway2BokGak_P21_D3] — tekst] 이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoRailway2BokGak_P21_D3].content
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Samouczek i wskazówki [TutoSchemacraft_Title] — tekst] 도상구축
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_Title].content
   limit: do 120 znaków
   EN: Schemacraft
   PL: Konstrukcja Schematów
219. [Samouczek i wskazówki [TutoSchemacraft_P1_T1] — tekst] 도상구축
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_T1].content
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Samouczek i wskazówki [TutoSchemacraft_P1_D1] — tekst] 도상구축은 주사위를 굴려 도상을 탐사하고, 전투 보상으로 얻은 인격과 E.G.O로 편성을 갖추어 나가는 콘텐츠입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_D1].content
   limit: do 160 znaków
   EN: In Schemacraft, you roll dice to explore Schemas and build your team with Identities and E.G.O earned from battle rewards.
   PL: Konstrukcja Schematów to tryb, w którym rzucasz kością, eksplorujesz Schematy i budujesz drużynę z Tożsamości oraz E.G.O zdobywanych za walki.
221. [Samouczek i wskazówki [TutoSchemacraft_P1_D2] — tekst] 전투는 자동으로 진행되며, 어느 표상으로 나아갈지와 어떤 보상을 고를지, 언제 E.G.O를 사용할지를 선택하여 최종 보스 처치를 목표로 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_D2].content
   limit: do 200 znaków
   EN: Battles play out automatically. Choose which Representations to visit, which rewards to claim, and when to use E.G.O as you make your way to the Final Boss.
   PL: Walki toczą się automatycznie — wybieraj, do których Reprezentacji wyruszyć, jakie nagrody odebrać oraz kiedy użyć E.G.O, aby pokonać finałowego bossa.
222. [Samouczek i wskazówki [TutoSchemacraft_P1_T2] — tekst] 입장하기
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_T2].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
223. [Samouczek i wskazówki [TutoSchemacraft_P1_D3] — tekst] 입장하기를 선택하면 시작 편성 화면으로 이동합니다. 진행 중인 도상구축이 있으면 이어하기로 계속하거나 새로하기로 다시 시작할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_D3].content
   limit: do 200 znaków
   EN: Select "Enter" to open the Starting Team screen. If a run is already in progress, select "Continue" to resume it or "Fresh Start" to begin a new one.
   PL: Wybierz „Wejdź”, aby przejść do ekranu drużyny startowej. Jeśli wyprawa już trwa, możesz ją wznowić przyciskiem „Kontynuuj” lub zacząć od zera opcją „Od nowa”.
224. [Samouczek i wskazówki [TutoSchemacraft_P1_T3] — tekst] 도상구축 패스
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_T3].content
   limit: do 120 znaków
   EN: Schemacraft Pass
   PL: Przepustka Konstrukcji Schematów
225. [Samouczek i wskazówki [TutoSchemacraft_P1_D4] — tekst] 도상구축을 진행하여 패스 경험치를 획득하고, 레벨에 따라 보상을 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P1_D4].content
   limit: do 120 znaków
   EN: Earn Schemacraft Pass EXP by playing Schemacraft, and claim rewards as your Pass levels up.
   PL: Rozgrywaj Konstrukcję Schematów, zdobywaj PD Przepustki i odbieraj nagrody za kolejne poziomy.
226. [Samouczek i wskazówki [TutoSchemacraft_P2_T1] — tekst] 시작 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_T1].content
   limit: do 120 znaków
   EN: Starting Team
   PL: Drużyna startowa
227. [Samouczek i wskazówki [TutoSchemacraft_P2_D1] — tekst] 도상구축을 함께 시작할 인격을 최대 4명까지 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D1].content
   limit: do 120 znaków
   EN: Select up to 4 Identities to start your Schemacraft run with.
   PL: Wybierz maksymalnie 4 Tożsamości, z którymi rozpoczniesz Konstrukcję Schematów.
228. [Samouczek i wskazówki [TutoSchemacraft_P2_T2] — tekst] 수동 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_T2].content
   limit: do 120 znaków
   EN: Manual Team
   PL: Skład ręczny
229. [Samouczek i wskazówki [TutoSchemacraft_P2_D2] — tekst] 주어진 코스트 안에서 원하는 인격을 직접 선택합니다. 코스트가 높은 인격은 편성할 수 있는 수가 제한됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D2].content
   limit: do 170 znaków
   EN: Manually recruit Identities within the available Cost limit. There is a limit to how many high-Cost Identities you can select.
   PL: Samodzielnie wybierz Tożsamości w ramach dostępnego Kosztu. Liczba Tożsamości o wysokim Koszcie jest ograniczona.
230. [Samouczek i wskazówki [TutoSchemacraft_P2_T3] — tekst] 자동 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_T3].content
   limit: do 120 znaków
   EN: Randomized Team
   PL: Skład losowy
231. [Samouczek i wskazówki [TutoSchemacraft_P2_D3] — tekst] 수동 편성보다 많은 코스트로 구성된 무작위 편성을 받습니다. 받은 편성은 자동 편성 목록에 보관되어 그중 하나를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D3].content
   limit: do 200 znaków
   EN: Receive a randomized team with a higher Cost allowance than Manual Team. Generated teams are saved to the list so you can choose which one to start with.
   PL: Otrzymujesz losową drużynę o wyższym limicie Kosztu niż w składzie ręcznym. Wygenerowane składy trafiają na listę, z której możesz wybrać jeden.
232. [Samouczek i wskazówki [TutoSchemacraft_P2_D4] — tekst] 자동 편성 새로고침으로 새로운 편성을 받을 수 있으며, 남은 횟수는 매일 초기화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D4].content
   limit: do 120 znaków
   EN: Use Randomized Team Reshuffles to generate new teams. Your remaining Reshuffles reset daily.
   PL: Użyj odświeżenia składu losowego, aby wylosować nową drużynę; pozostałe próby odnawiają się codziennie.
233. [Samouczek i wskazówki [TutoSchemacraft_P2_D5] — tekst] 도상구축을 일정 도상 이상 진행한 뒤 종료하면, 자동 편성 새로고침 기회를 추가로 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D5].content
   limit: do 140 znaków
   EN: If you reach a certain Schema before ending a run, you'll earn additional Randomized Team Reshuffles.
   PL: Zakończenie wyprawy po dotarciu do określonego Schematu zapewnia dodatkowe szanse odświeżenia składu losowego.
234. [Samouczek i wskazówki [TutoSchemacraft_P2_D6] — tekst] 자동 편성으로 시작하면 도상구축 패스 경험치를 추가로 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P2_D6].content
   limit: do 120 znaków
   EN: Starting with a Randomized Team grants extra Schemacraft Pass EXP.
   PL: Rozpoczęcie gry składem losowym zapewnia dodatkowe PD Przepustki Konstrukcji Schematów.
235. [Samouczek i wskazówki [TutoSchemacraft_P3_T1] — tekst] 도상 탐사
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_T1].content
   limit: do 120 znaków
   EN: Exploring Schemas
   PL: Eksploracja Schematów
236. [Samouczek i wskazówki [TutoSchemacraft_P3_D1] — tekst] 도상구축은 여러 개의 도상으로 구성되며, 각 도상의 보스를 처치하면 다음 도상으로 넘어갑니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D1].content
   limit: do 120 znaków
   EN: A Schemacraft run spans 5 Schemas. Defeat each Schema's boss to advance to the next.
   PL: Konstrukcja Schematów składa się z kolejnych Schematów; pokonanie bossa danego Schematu przenosi do następnego.
237. [Samouczek i wskazówki [TutoSchemacraft_P3_D2] — tekst] 표상은 도상 위에서 이동할 수 있는 지점입니다. 일반 전투, 정예 전투, 보스 전투, 휴식, 유혹, 이벤트로 구분됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D2].content
   limit: do 220 znaków
   EN: Representations are spaces you can move to within a Schema. They include Regular, Elite, and Boss Encounters, as well as Respite, Temptation, and Event Representations.
   PL: Reprezentacje to punkty na Schemacie, na które możesz się przemieścić. Dzielą się na Zwykłą Walkę, Walkę Elitarną, Walkę z Bossem, Wytchnienie, Pokusę oraz Wydarzenie.
238. [Samouczek i wskazówki [TutoSchemacraft_P3_T2] — tekst] 주사위
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_T2].content
   limit: do 120 znaków
   EN: Dice
   PL: Kość
239. [Samouczek i wskazówki [TutoSchemacraft_P3_D3] — tekst] 주사위를 굴리면 나온 눈만큼의 거리 안에 있는 표상이 밝혀지며, 그중 하나를 선택하여 이동할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D3].content
   limit: do 150 znaków
   EN: When you roll the dice, Representations within the rolled distance are revealed. Choose one of them to move to.
   PL: Po rzucie kością ujawniane są Reprezentacje w zasięgu wyrzuconej liczby oczek — wybierz jedną z nich, aby tam przejść.
240. [Samouczek i wskazówki [TutoSchemacraft_P3_T3] — tekst] 도상 왜곡
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_T3].content
   limit: do 120 znaków
   EN: Schema Deformation
   PL: Wypaczenie Schematu
241. [Samouczek i wskazówki [TutoSchemacraft_P3_D4] — tekst] 남은 횟수와 추가 굴림을 모두 사용한 뒤에도 주사위를 굴릴 수 있지만, 굴릴 때마다 도상 왜곡이 쌓이게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D4].content
   limit: do 180 znaków
   EN: You can keep rolling the dice after using all your remaining rolls and Bonus Rolls, but each additional roll adds Schema Deformation.
   PL: Możesz nadal rzucać kością po wyczerpaniu pozostałych i dodatkowych rzutów, lecz każdy kolejny rzut nakłada Wypaczenie Schematu.
242. [Samouczek i wskazówki [TutoSchemacraft_P3_D5] — tekst] 도상 왜곡은 현재 도상의 적을 강화합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D5].content
   limit: do 120 znaków
   EN: Schema Deformation strengthens enemies in the current Schema.
   PL: Wypaczenie Schematu wzmacnia wrogów w bieżącym Schemacie.
243. [Samouczek i wskazówki [TutoSchemacraft_P3_T4] — tekst] 편성과 구축력
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_T4].content
   limit: do 120 znaków
   EN: Teams and Craftpower
   PL: Skład i Siła Konstrukcji
244. [Samouczek i wskazówki [TutoSchemacraft_P3_D6] — tekst] 인격 레벨은 편성한 모든 인격에게 공통으로 적용되며, 전투에서 승리할수록 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D6].content
   limit: do 130 znaków
   EN: Every Identity on your team shares the same Identity Level. This level increases as you win battles.
   PL: Poziom Tożsamości jest wspólny dla całej drużyny i rośnie wraz z kolejnymi wygranymi walkami.
245. [Samouczek i wskazówki [TutoSchemacraft_P3_D7] — tekst] 구축력은 현재 편성의 강함을 나타내는 수치입니다. 표상 정보에서 권장 구축력과 비교할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P3_D7].content
   limit: do 170 znaków
   EN: Craftpower measures the strength of your current team. You can compare it with the Recommended Craftpower in Representation Info.
   PL: Siła Konstrukcji określa potęgę bieżącego składu. Możesz porównać ją z Zalecaną Siłą Konstrukcji w informacjach o Reprezentacji.
246. [Samouczek i wskazówki [TutoSchemacraft_P4_T1] — tekst] 표상 정보
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P4_T1].content
   limit: do 120 znaków
   EN: Representation Info
   PL: Informacje o Reprezentacji
247. [Samouczek i wskazówki [TutoSchemacraft_P4_D1] — tekst] 해당 표상의 종류와 적의 평균 레벨 등을 확인할 수 있습니다. 표상 진입을 선택하면 해당 표상으로 이동합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P4_D1].content
   limit: do 180 znaków
   EN: Check the Representation type, the enemies' average level, and other details. Select "Enter" to move to that specific Representation.
   PL: Sprawdzisz tu rodzaj Reprezentacji, średni poziom wrogów i inne dane. Wybierz wejście, aby przemieścić się do tej Reprezentacji.
248. [Samouczek i wskazówki [TutoSchemacraft_P4_T2] — tekst] 등장 팩 목록
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P4_T2].content
   limit: do 120 znaków
   EN: Available Packs
   PL: Dostępne Pakiety
249. [Samouczek i wskazówki [TutoSchemacraft_P4_D2] — tekst] 전투에서 승리하였을 때 등장할 수 있는 팩의 목록입니다. 각 팩을 선택하여 팩의 자세한 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P4_D2].content
   limit: do 130 znaków
   EN: See which Packs may appear as rewards for winning the battle. Select a Pack to view its details.
   PL: Lista Pakietów mogących pojawić się po wygranej walce. Kliknij Pakiet, aby sprawdzić jego szczegóły.
250. [Samouczek i wskazówki [TutoSchemacraft_P5_T1] — tekst] 전투 편성
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_T1].content
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
251. [Samouczek i wskazówki [TutoSchemacraft_P5_D1] — tekst] 전투에 참여할 인격과 순서를 정합니다. 전투 가능 인원은 도상이 진행될수록 늘어납니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_D1].content
   limit: do 170 znaków
   EN: Choose which Identities to deploy and in what order. More deployment slots become available as you progress through the Schemas.
   PL: Wybierz uczestniczące w walce Tożsamości i ich kolejność. Limit uczestników w polu rośnie w miarę postępów przez Schematy.
252. [Samouczek i wskazówki [TutoSchemacraft_P5_D2] — tekst] 전투 가능 인원을 넘는 인격은 대기 인원으로 편성되며, 아군이 사망하면 편성 순서에 따라 대신 전투에 참여합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_D2].content
   limit: do 200 znaków
   EN: Identities beyond the field deployment limit become Backup Identities. When a fielded ally dies, Backup Identities enter the battle in Deployment Order.
   PL: Tożsamości powyżej limitu uczestników w polu trafiają do rezerwy i wchodzą do walki zgodnie z kolejnością po śmierci sojusznika.
253. [Samouczek i wskazówki [TutoSchemacraft_P5_T2] — tekst] 전투 준비
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_T2].content
   limit: do 120 znaków
   EN: Battle Preparation
   PL: Przygotowanie do walki
254. [Samouczek i wskazówki [TutoSchemacraft_P5_D3] — tekst] 하단의 버튼을 선택하여 방어 정책과 브리핑을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_D3].content
   limit: do 120 znaków
   EN: Use the buttons at the bottom of the screen to open Defense Strat. and Briefing.
   PL: Użyj dolnych przycisków, aby sprawdzić Politykę obrony oraz Odprawę.
255. [Samouczek i wskazówki [TutoSchemacraft_P5_D4] — tekst] 준비를 마친 뒤 전투 시작을 선택하면 전투가 시작됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P5_D4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When you're ready, select "To Battle!" to begin.
   PL: Gdy wszystko gotowe, wybierz rozpoczęcie walki,\naby przystąpić do starcia.
256. [Samouczek i wskazówki [TutoSchemacraft_P6_T1] — tekst] 방어 정책
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_T1].content
   limit: do 120 znaków
   EN: Defense Strat.
   PL: Polityka obrony
257. [Samouczek i wskazówki [TutoSchemacraft_P6_D1] — tekst] 방어 정책에서는 각 인격이 수비 스킬을 사용할 조건을 정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_D1].content
   limit: do 120 znaków
   EN: Set the conditions under which each Identity uses their Defense Skill.
   PL: W Polityce obrony ustalisz warunki, w których poszczególne Tożsamości użyją umiejętności obrony.
258. [Samouczek i wskazówki [TutoSchemacraft_P6_T2] — tekst] 수비 조건
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_T2].content
   limit: do 120 znaków
   EN: Defense Conditions
   PL: Warunki obrony
259. [Samouczek i wskazówki [TutoSchemacraft_P6_D2] — tekst] 인격을 선택한 뒤, 목록에서 수비 스킬을 사용할 조건을 선택합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_D2].content
   limit: do 120 znaków
   EN: Select an Identity, then choose a condition from the list.
   PL: Wybierz Tożsamość, a następnie wskaż na liście warunek użycia umiejętności obrony.
260. [Samouczek i wskazówki [TutoSchemacraft_P6_T3] — tekst] 일괄 설정
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_T3].content
   limit: do 120 znaków
   EN: Set All Conditions
   PL: Ustaw zbiorczo
261. [Samouczek i wskazówki [TutoSchemacraft_P6_D3] — tekst] 편성한 인격의 수비 조건을 한 번에 기본값으로 되돌리거나, 같은 조건으로 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P6_D3].content
   limit: do 150 znaków
   EN: Reset all Identities on your team to their default conditions, or assign the same condition to all of them at once.
   PL: Przywróć domyślne warunki obrony wszystkim Tożsamościom w składzie naraz albo przypisz im ten sam warunek.
262. [Samouczek i wskazówki [TutoSchemacraft_P7_T1] — tekst] 브리핑
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P7_T1].content
   limit: do 120 znaków
   EN: Briefing
   PL: Odprawa
263. [Samouczek i wskazówki [TutoSchemacraft_P7_D1] — tekst] 전투를 시작하기 전에 아군과 적의 평균 레벨, 출현하는 적의 수와 약점을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P7_D1].content
   limit: do 160 znaków
   EN: Before starting the battle, check the average level of each side, how many enemies will appear, and what they're weak to.
   PL: Przed rozpoczęciem walki sprawdzisz tu średni poziom sojuszników i wrogów, liczbę przeciwników oraz ich słabości.
264. [Samouczek i wskazówki [TutoSchemacraft_P7_T2] — tekst] E.G.O 자원
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P7_T2].content
   limit: do 120 znaków
   EN: E.G.O Resources
   PL: Zasoby E.G.O
265. [Samouczek i wskazówki [TutoSchemacraft_P7_D2] — tekst] 먼저 출전하는 인격의 스킬로 얻을 수 있는 E.G.O 자원과, 장착한 E.G.O에 필요한 자원을 비교할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P7_D2].content
   limit: do 180 znaków
   EN: Compare the E.G.O resources provided by the Skills of the Identities deployed first with the resources required by your equipped E.G.O.
   PL: Porównaj zasoby E.G.O generowane przez umiejętności wystawionych jako pierwsze Tożsamości z zasobami wymaganymi przez wyposażone E.G.O.
266. [Samouczek i wskazówki [TutoSchemacraft_P8_T1] — tekst] 자동 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_T1].content
   limit: do 120 znaków
   EN: Auto Battle
   PL: Walka automatyczna
267. [Samouczek i wskazówki [TutoSchemacraft_P8_D1] — tekst] 아군과 적은 각자의 속도에 따라 자동으로 행동하며, 서로의 스킬이 마주치면 합을 진행합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_D1].content
   limit: do 150 znaków
   EN: Allies and enemies act automatically according to their Speed. When their Skills oppose each other, they Clash.
   PL: Sojusznicy i wrogowie działają automatycznie zależnie od Szybkości, a gdy ich umiejętności się zetkną, dochodzi do Starcia.
268. [Samouczek i wskazówki [TutoSchemacraft_P8_T2] — tekst] TURN
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_T2].content
   limit: do 120 znaków
   EN: TURN
   PL: TURN
269. [Samouczek i wskazówki [TutoSchemacraft_P8_D2] — tekst] 화면 중앙의 게이지는 턴 진행 상황을 나타내며, 턴 종료 시 효과는 턴이 끝날 때마다 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_D2].content
   limit: do 150 znaków
   EN: The gauge at the center of the screen tracks the turn's progress. Turn End effects activate at the end of each turn.
   PL: Pasek na środku ekranu pokazuje postęp tury; efekty końca tury aktywują się po zakończeniu każdej tury.
270. [Samouczek i wskazówki [TutoSchemacraft_P8_T3] — tekst] 전투 인원
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_T3].content
   limit: do 120 znaków
   EN: Participants
   PL: Uczestnicy walki
271. [Samouczek i wskazówki [TutoSchemacraft_P8_D3] — tekst] 출전한 아군이 사망하면 대기 인원이 투입되며, 편성한 인격이 모두 사망하면 전투에서 패배합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_D3].content
   limit: do 160 znaków
   EN: When a deployed ally dies, a Backup Identity takes their place. If all Identities on your team die, you lose the battle.
   PL: Gdy walczący sojusznik zginie, wkracza rezerwowy; śmierć wszystkich Tożsamości w składzie oznacza porażkę.
272. [Samouczek i wskazówki [TutoSchemacraft_P8_T4] — tekst] 적용 효과
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_T4].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
273. [Samouczek i wskazówki [TutoSchemacraft_P8_D4] — tekst] 고난과 도상 왜곡으로 적에게 적용 중인 효과를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_D4].content
   limit: do 120 znaków
   EN: Check which effects from Obstacles and Schema Deformation are currently applied to enemies.
   PL: Sprawdzisz tu efekty nałożone na wrogów przez Próby oraz Wypaczenie Schematu.
274. [Samouczek i wskazówki [TutoSchemacraft_P8_T5] — tekst] E.G.O 자원
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_T5].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Samouczek i wskazówki [TutoSchemacraft_P8_D5] — tekst] 전투 시작 시 대기 인격을 포함해 죄악 속성별로 스킬 2장당 자원 1개를 얻습니다. 전투 중에도 스킬 속성에 따라 자원을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P8_D5].content
   limit: do 260 znaków
   EN: At the start of battle, you gain 1 resource per 2 Skills of each Sin Affinity, counting Backup Identities as well. You can also gain resources during battle based on the Affinity of the Skills used.
   PL: Na początku walki otrzymujesz 1 zasób za każde 2 umiejętności danego grzechu (wliczając rezerwowych). Zasoby zdobywasz też w trakcie walki zależnie od grzechów używanych umiejętności.
276. [Samouczek i wskazówki [TutoSchemacraft_P9_T1] — tekst] 인격 패널
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_T1].content
   limit: do 120 znaków
   EN: Identity Panels
   PL: Panele Tożsamości
277. [Samouczek i wskazówki [TutoSchemacraft_P9_D1] — tekst] 화면 하단의 인격 패널에는 출전 중인 인격마다 발동 중인 스킬, 대기 중인 스킬, 수비 스킬이 차례로 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_D1].content
   limit: do 180 znaków
   EN: At the bottom of the screen, each deployed Identity's panel shows their active Skill, queued Skills, and Defense Skill, in that order.
   PL: Na panelach Tożsamości u dołu ekranu widnieją kolejno: używana umiejętność, oczekujące umiejętności oraz umiejętność obrony każdego uczestnika.
278. [Samouczek i wskazówki [TutoSchemacraft_P9_T2] — tekst] E.G.O 사용
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_T2].content
   limit: do 120 znaków
   EN: Using E.G.O
   PL: Użycie E.G.O
279. [Samouczek i wskazówki [TutoSchemacraft_P9_D2] — tekst] E.G.O 자원이 충분하면 인격 패널의 E.G.O를 선택하여 사용할 수 있으며, 대상은 자동으로 정해집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_D2].content
   limit: do 160 znaków
   EN: If you have enough E.G.O resources, select an E.G.O on the Identity's panel to use it. The target is selected automatically.
   PL: Gdy masz dość zasobów E.G.O, kliknij E.G.O na panelu Tożsamości, aby go użyć — cel wybierany jest automatycznie.
280. [Samouczek i wskazówki [TutoSchemacraft_P9_D3] — tekst] E.G.O를 위로 끌어 적에게 놓으면 대상을 직접 지정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_D3].content
   limit: do 120 znaków
   EN: To choose a target yourself, drag the E.G.O upward and drop it onto an enemy.
   PL: Przeciągnij E.G.O w górę i upuść na wroga, aby samodzielnie wskazać cel.
281. [Samouczek i wskazówki [TutoSchemacraft_P9_D4] — tekst] E.G.O를 아래로 끌면 오버클록으로 전환되며, 그대로 손을 떼거나 적에게 놓아 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_D4].content
   limit: do 140 znaków
   EN: Drag the E.G.O downward to Overclock it. Release to use it, or drop it onto an enemy to choose the target.
   PL: Przeciągnij E.G.O w dół, aby włączyć Przeciążenie — puść palec lub upuść na wybranego wroga, by go użyć.
282. [Samouczek i wskazówki [TutoSchemacraft_P9_D5] — tekst] E.G.O를 길게 누른 뒤 손을 떼면 해당 E.G.O의 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P9_D5].content
   limit: do 120 znaków
   EN: Press and hold the E.G.O, then release to view its details.
   PL: Przytrzymaj E.G.O i puść, aby wyświetlić jego szczegóły.
283. [Samouczek i wskazówki [TutoSchemacraft_P10_T1] — tekst] 전투 리포트
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_T1].content
   limit: do 120 znaków
   EN: Battle Report
   PL: Raport z walki
284. [Samouczek i wskazówki [TutoSchemacraft_P10_D1] — tekst] 전투 리포트에서는 진영별 체력의 변화와 아군의 평균 정신력, 수감자별 기록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_D1].content
   limit: do 140 znaków
   EN: The Battle Report shows how each side's HP changed, your team's average SP, and each Sinner's battle stats.
   PL: W raporcie z walki sprawdzisz zmiany PŻ obu stron, średnie PP sojuszników oraz statystyki poszczególnych Grzeszników.
285. [Samouczek i wskazówki [TutoSchemacraft_P10_T2] — tekst] 전투 후 상태
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_T2].content
   limit: do 120 znaków
   EN: After Battle
   PL: Stan po walce
286. [Samouczek i wskazówki [TutoSchemacraft_P10_D2] — tekst] 전투가 종료되면 사망한 인격도 복귀하고 체력이 모두 회복됩니다. 정신력은 다음 전투까지 이어지며, 0보다 낮다면 0으로 회복됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_D2].content
   limit: do 210 znaków
   EN: When a battle ends, Identities that died return and all Identities recover to full HP. SP carries over to the next battle, but any SP below 0 is restored to 0.
   PL: Po zakończeniu walki poległe Tożsamości wracają, a PŻ odnawiają się w pełni. PP przechodzą do kolejnej walki, przy czym wartości poniżej 0 wracają do 0.
287. [Samouczek i wskazówki [TutoSchemacraft_P10_T3] — tekst] 재도전
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_T3].content
   limit: do 120 znaków
   EN: Retry
   PL: Ponowienie
288. [Samouczek i wskazówki [TutoSchemacraft_P10_D3] — tekst] 전투마다 정해진 횟수만큼 재도전할 수 있으며, 횟수를 모두 사용한 상태에서 패배하면 도상구축이 종료됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P10_D3].content
   limit: do 150 znaków
   EN: Each battle has a limited number of retries. If you lose with no retries remaining, your Schemacraft run ends.
   PL: Każdą walkę można ponowić określoną liczbę razy; porażka po wyczerpaniu wszystkich prób kończy Konstrukcję Schematów.
289. [Samouczek i wskazówki [TutoSchemacraft_P11_T1] — tekst] 전투 보상 - 팩 고르기
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_T1].content
   limit: do 120 znaków
   EN: Battle Reward: Choose a Pack
   PL: Nagroda za walkę — wybór Pakietu
290. [Samouczek i wskazówki [TutoSchemacraft_P11_D1] — tekst] 전투에서 승리하면 3개의 팩이 제시되며, 그중 하나를 골라 인격과 E.G.O를 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_D1].content
   limit: do 140 znaków
   EN: After winning a battle, choose 1 of the 3 Packs offered, then select Identities and E.G.O from that Pack.
   PL: Po zwycięstwie proponowane są 3 Pakiety — wybierz jeden z nich, aby dobrać z niego Tożsamości i E.G.O.
291. [Samouczek i wskazówki [TutoSchemacraft_P11_D2] — tekst] 각 팩에는 확정으로 등장하는 소속 또는 키워드와 인격의 코스트별 확률이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_D2].content
   limit: do 130 znaków
   EN: Each Pack shows the guaranteed faction or keyword and the odds of drawing an Identity at each Cost.
   PL: Na każdym Pakiecie widnieje gwarantowana przynależność lub słowo kluczowe oraz szanse wylosowania Tożsamości według Kosztu.
292. [Samouczek i wskazówki [TutoSchemacraft_P11_T2] — tekst] 팩 교체
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_T2].content
   limit: do 120 znaków
   EN: Reshuffling Pack
   PL: Wymiana Pakietu
293. [Samouczek i wskazówki [TutoSchemacraft_P11_D3] — tekst] 새로고침 기회를 소모하여 제시된 팩을 등장 팩 목록의 다른 팩으로 교체할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_D3].content
   limit: do 130 znaków
   EN: Spend Reshuffles to replace an offered Pack. Each successive replacement costs more Reshuffles.
   PL: Wydaj szansę odświeżenia, aby zamienić proponowany Pakiet na inny z listy Dostępnych Pakietów.
294. [Samouczek i wskazówki [TutoSchemacraft_P11_D4] — tekst] 새로고침 기회는 전투에서 승리할 때마다 획득하며, 휴식 표상 등에서도 추가로 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P11_D4].content
   limit: do 160 znaków
   EN: You earn Reshuffles each time you win a battle. You can also get more from Respite Representations and other sources.
   PL: Szanse odświeżenia zdobywasz za każdą wygraną walkę, a dodatkowe możesz uzyskać m.in. w Reprezentacjach Wytchnienia.
295. [Samouczek i wskazówki [TutoSchemacraft_P12_T1] — tekst] 인격과 E.G.O 선택
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_T1].content
   limit: do 120 znaków
   EN: Select Identities and E.G.O
   PL: Wybór Tożsamości i E.G.O
296. [Samouczek i wskazówki [TutoSchemacraft_P12_D1] — tekst] 팩을 열면 제시된 인격과 E.G.O 중 정해진 수만큼 골라 획득합니다. 새로고침 기회를 소모하여 카드마다 한 번씩 다시 뽑을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D1].content
   limit: do 210 znaków
   EN: When you open a Pack, choose the specified number of Identities and E.G.O from the cards offered. You can spend Reshuffles to draw a replacement for each card once.
   PL: Po otwarciu Pakietu wybierz określoną liczbę Tożsamości i E.G.O spośród wylosowanych kart. Za szansę odświeżenia możesz raz wymienić każdą kartę.
297. [Samouczek i wskazówki [TutoSchemacraft_P12_T2] — tekst] 편성 / 교체 / 조각
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_T2].content
   limit: do 120 znaków
   EN: Team / Replace / Slivers
   PL: Skład / Wymiana / Okruchy
298. [Samouczek i wskazówki [TutoSchemacraft_P12_D2] — tekst] 편성 : 아직 편성되지 않은 수감자의 인격을 편성에 추가합니다. 편성 상한에 도달했다면 제외할 인격을 선택해야 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D2].content
   limit: do 150 znaków
   EN: Team: Add an Identity for a Sinner who isn't already on the team. If the team is full, select an Identity to remove.
   PL: Skład: dodaje Tożsamość Grzesznika nieobecnego jeszcze w drużynie. Przy pełnym składzie należy wskazać Tożsamość do usunięcia.
299. [Samouczek i wskazówki [TutoSchemacraft_P12_D3] — tekst] 교체 : 이미 편성된 수감자의 인격을 선택한 인격으로 바꿉니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D3].content
   limit: do 120 znaków
   EN: Replace: Swap a Sinner's current Identity for the selected Identity.
   PL: Wymiana: zastępuje bieżącą Tożsamość Grzesznika wybraną nową Tożsamością.
300. [Samouczek i wskazówki [TutoSchemacraft_P12_D4] — tekst] 조각 : 인격을 편성하는 대신 해당 수감자의 조각을 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D4].content
   limit: do 120 znaków
   EN: Slivers: Receive that Sinner's Slivers instead of adding the Identity to the team.
   PL: Okruchy: zamiast dodawać Tożsamość do składu, otrzymujesz Okruchy danego Grzesznika.
301. [Samouczek i wskazówki [TutoSchemacraft_P12_T3] — tekst] 동기화와 조각
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_T3].content
   limit: do 120 znaków
   EN: Uptie and Slivers
   PL: Synchronizacja i Okruchy
302. [Samouczek i wskazówki [TutoSchemacraft_P12_D5] — tekst] 편성 중인 인격과 같은 인격을 선택하면 동기화 단계가 상승합니다. 계정에서 보유하지 않은 인격은 동기화 3단계까지만 올릴 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D5].content
   limit: do 200 znaków
   EN: Selecting the same Identity you already have on your team raises its Uptie Tier. Identities you don't own on your account can only reach Uptie Tier 3.
   PL: Wybranie tej samej Tożsamości, którą masz już w składzie, podnosi jej stopień Synchronizacji. Tożsamości nieposiadane na koncie mogą osiągnąć maks. 3. stopień.
303. [Samouczek i wskazówki [TutoSchemacraft_P12_D6] — tekst] 수감자의 조각이 필요한 수만큼 모이면, 해당 수감자의 인격이 다음 동기화 단계로 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D6].content
   limit: do 140 znaków
   EN: Once you collect enough Slivers for a Sinner, their current Identity advances to the next Uptie Tier.
   PL: Po zebraniu wymaganej liczby Okruchów Grzesznika jego Tożsamość awansuje na kolejny stopień Synchronizacji.
304. [Samouczek i wskazówki [TutoSchemacraft_P12_T4] — tekst] 범용 조각
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_T4].content
   limit: do 120 znaków
   EN: Universal Sliver
   PL: Okruch Uniwersalny
305. [Samouczek i wskazówki [TutoSchemacraft_P12_D7] — tekst] 동기화 단계가 상한에 도달한 수감자의 조각은 범용 조각으로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D7].content
   limit: do 130 znaków
   EN: Slivers for a Sinner whose Identity is already at its Uptie cap are converted to Universal Slivers.
   PL: Okruchy Grzesznika, którego Tożsamość osiągnęła limit Synchronizacji, zamieniają się w Okruchy Uniwersalne.
306. [Samouczek i wskazówki [TutoSchemacraft_P12_T5] — tekst] E.G.O 환상 해석
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_T5].content
   limit: do 120 znaków
   EN: E.G.O Threadspin
   PL: Splot Nici E.G.O
307. [Samouczek i wskazówki [TutoSchemacraft_P12_D8] — tekst] E.G.O의 환상 해석 단계는 계정의 보유 단계를 따르며, 보유하지 않은 E.G.O는 환상 해석 1단계로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P12_D8].content
   limit: do 130 znaków
   EN: E.G.O use the Threadspin Tier on your account. E.G.O you don't own are set to Threadspin Tier 1.
   PL: Stopień Splotu Nici E.G.O odpowiada stanowi na koncie, natomiast nieposiadane E.G.O mają 1. stopień Splotu Nici.
308. [Samouczek i wskazówki [TutoSchemacraft_P13_T1] — tekst] 정예 전투
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_T1].content
   limit: do 120 znaków
   EN: Elite Encounter
   PL: Walka Elitarna
309. [Samouczek i wskazówki [TutoSchemacraft_P13_D1] — tekst] 정예 전투에서 승리하면 팩 보상과 함께 정예 보상 중 하나를 선택하여 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_D1].content
   limit: do 120 znaków
   EN: Winning an Elite Encounter lets you choose an Elite Reward in addition to your Pack reward.
   PL: Zwycięstwo w Walce Elitarnej pozwala oprócz Pakietu wybrać dodatkowo jedną z nagród elitarnych.
310. [Samouczek i wskazówki [TutoSchemacraft_P13_D2] — tekst] 인격 교체 : 편성 중인 수감자의 인격을 제시된 다른 인격으로 바꿉니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_D2].content
   limit: do 120 znaków
   EN: Replace Identity: Swap a Sinner's current Identity for the one offered.
   PL: Wymiana Tożsamości: zastępuje Tożsamość Grzesznika w składzie proponowaną inną Tożsamością.
311. [Samouczek i wskazówki [TutoSchemacraft_P13_D3] — tekst] 인격 편성 : 제시된 인격을 편성에 추가합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_D3].content
   limit: do 120 znaków
   EN: Recruit Identity: Add the offered Identity to your team.
   PL: Włączenie do składu: dodaje proponowaną Tożsamość do drużyny.
312. [Samouczek i wskazówki [TutoSchemacraft_P13_D4] — tekst] 성장 : 편성 중인 수감자 1명을 골라 조각을 부여합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_D4].content
   limit: do 120 znaków
   EN: Upgrade: Choose 1 Sinner on your current team and give them Slivers.
   PL: Rozwój: przyznaje Okruchy 1 wybranemu Grzesznikowi z bieżącego składu.
313. [Samouczek i wskazówki [TutoSchemacraft_P13_D5] — tekst] 받지 않기 : 정예 보상을 받지 않고 진행합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P13_D5].content
   limit: do 120 znaków
   EN: Decline: Continue without claiming an Elite Reward.
   PL: Pomiń: kontynuuj bez odbierania nagrody elitarnej.
314. [Samouczek i wskazówki [TutoSchemacraft_P14_T1] — tekst] 유혹
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P14_T1].content
   limit: do 120 znaków
   EN: Temptation
   PL: Pokusa
315. [Samouczek i wskazówki [TutoSchemacraft_P14_D1] — tekst] 유혹 표상에서는 인격과 E.G.O를 제안받으며, 선택한 인격은 편성에 추가되거나 기존 인격과 교체됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P14_D1].content
   limit: do 200 znaków
   EN: At Temptation Representations, you're offered Identities and E.G.O. An Identity you choose is either added to your team or replaces an existing Identity.
   PL: W Reprezentacji Pokusy otrzymujesz propozycję Tożsamości oraz E.G.O; wybrana Tożsamość dołącza do składu lub zastępuje dotychczasową.
316. [Samouczek i wskazówki [TutoSchemacraft_P14_D2] — tekst] 받지 않기를 선택하여 현재 전투 편성을 유지할 수도 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P14_D2].content
   limit: do 120 znaków
   EN: You can also select "Decline" to keep your team as it is.
   PL: Możesz też wybrać pominięcie, aby zachować obecny skład drużyny.
317. [Samouczek i wskazówki [TutoSchemacraft_P14_D3] — tekst] 제안에 따라 주사위 굴림 횟수가 차감될 수 있습니다. 남은 횟수가 부족하더라도 선택할 수 있지만, 부족한 만큼 도상 왜곡이 쌓이게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P14_D3].content
   limit: do 180 znaków
   EN: Some offers cost dice rolls. You can accept even if you don't have enough rolls left, but any shortfall adds that much Schema Deformation.
   PL: Niektóre propozycje odejmują rzuty kością. Możesz je przyjąć nawet przy braku rzutów, lecz niedobór nałoży odpowiednią ilość Wypaczenia Schematu.
318. [Samouczek i wskazówki [TutoSchemacraft_P15_T1] — tekst] 이벤트
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P15_T1].content
   limit: do 120 znaków
   EN: Events
   PL: Wydarzenie
319. [Samouczek i wskazówki [TutoSchemacraft_P15_D1] — tekst] 이벤트 표상에서는 상황에 따른 선택지가 제시되며, 하나를 선택하여 해당 효과를 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P15_D1].content
   limit: do 120 znaków
   EN: At Event Representations, choose one of the options presented to receive its effect.
   PL: W Reprezentacji Wydarzenia prezentowane są opcje wyboru zależne od sytuacji — wskaż jedną, aby uzyskać jej efekt.
320. [Samouczek i wskazówki [TutoSchemacraft_P15_D2] — tekst] 선택지를 고르지 않고 나갈 수도 있으며, 이 경우 효과와 고난을 모두 받지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P15_D2].content
   limit: do 120 znaków
   EN: You can also leave without choosing. You won't receive any effects or incur any Obstacles.
   PL: Możesz też wyjść bez dokonywania wyboru — nie otrzymasz wówczas ani efektów, ani Prób.
321. [Samouczek i wskazówki [TutoSchemacraft_P15_T2] — tekst] 고난
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P15_T2].content
   limit: do 120 znaków
   EN: Obstacle
   PL: Próba
322. [Samouczek i wskazówki [TutoSchemacraft_P15_D3] — tekst] 선택지의 고난은 적의 체력 또는 적이 가하는 피해량을 증가시키며, 도상구축이 끝날 때까지 누적됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P15_D3].content
   limit: do 150 znaków
   EN: Obstacles increase enemy HP or the damage enemies deal. They stack and last until the end of the Schemacraft run.
   PL: Próba z wybranej opcji zwiększa PŻ wrogów lub zadawane przez nich obrażenia i kumuluje się aż do końca Konstrukcji Schematów.
323. [Samouczek i wskazówki [TutoSchemacraft_P16_T1] — tekst] 휴식
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P16_T1].content
   limit: do 120 znaków
   EN: Respite
   PL: Wytchnienie
324. [Samouczek i wskazówki [TutoSchemacraft_P16_D1] — tekst] 휴식 표상에서는 새로고침 기회, 동기화 단계 상승, 주사위 굴림 횟수 증가 등의 효과 중 하나를 선택하여 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P16_D1].content
   limit: do 160 znaków
   EN: At Respite Representations, you can choose one benefit, such as Reshuffles, a higher Uptie Tier, or additional dice rolls.
   PL: W Reprezentacji Wytchnienia wybierasz jedną korzyść, np. szanse odświeżenia, wyższy stopień Synchronizacji lub dodatkowe rzuty kością.
325. [Samouczek i wskazówki [TutoSchemacraft_P16_T2] — tekst] 범용 조각 사용
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P16_T2].content
   limit: do 120 znaków
   EN: Using Universal Slivers
   PL: Użycie Okruchów Uniwersalnych
326. [Samouczek i wskazówki [TutoSchemacraft_P16_D2] — tekst] 범용 조각을 사용하여 원하는 인격의 동기화 단계를 올릴 수 있습니다. 올릴 수 있는 단계는 도상이 진행될수록 높아집니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P16_D2].content
   limit: do 220 znaków
   EN: Spend Universal Slivers to raise the Uptie Tier of an Identity of your choice. The highest Tier you can reach this way increases as you progress through the Schemas.
   PL: Wydaj Okruchy Uniwersalne, aby podnieść stopień Synchronizacji dowolnej wybranej Tożsamości. Maksymalny dostępny stopień rośnie w miarę postępów przez Schematy.
327. [Samouczek i wskazówki [TutoSchemacraft_P17_T1] — tekst] 최종 전투 결과
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P17_T1].content
   limit: do 120 znaków
   EN: Final Battle Results
   PL: Podsumowanie wyprawy
328. [Samouczek i wskazówki [TutoSchemacraft_P17_D1] — tekst] 도상구축이 종료되면 도상 진행도와 전투 진행 횟수, 참여 인격의 피해 기록과 보상 기록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P17_D1].content
   limit: do 240 znaków
   EN: When your Schemacraft run ends, you can review your progress through the Schemas, how many battles you fought, the damage stats of participating Identities, and the rewards you earned.
   PL: Po zakończeniu Konstrukcji Schematów sprawdzisz postęp Schematów, liczbę stoczonych walk, statystyki obrażeń Tożsamości oraz zdobyte nagrody.
329. [Samouczek i wskazówki [TutoSchemacraft_P18_T1] — tekst] 도상구축 패스
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_T1].content
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Samouczek i wskazówki [TutoSchemacraft_P18_D1] — tekst] 더 깊은 도상까지 나아갈수록 더 많은 패스 경험치를 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D1].content
   limit: do 120 znaków
   EN: The farther you progress through the Schemas, the more Pass EXP you earn.
   PL: Im głębszy Schemat osiągniesz, tym więcej PD Przepustki zdobędziesz.
331. [Samouczek i wskazówki [TutoSchemacraft_P18_D2] — tekst] 패스 보상은 정해진 기간까지만 수령할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D2].content
   limit: do 120 znaków
   EN: Pass rewards can only be claimed during the stated claim period.
   PL: Nagrody Przepustki można odebrać wyłącznie we wskazanym okresie.
332. [Samouczek i wskazówki [TutoSchemacraft_P18_D3] — tekst] 획득 가능한 패스 경험치는 매주 한정되어 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D3].content
   limit: do 120 znaków
   EN: There is a weekly limit on the Pass EXP you can earn.
   PL: Liczba PD Przepustki możliwych do zdobycia w tygodniu jest ograniczona.
333. [Samouczek i wskazówki [TutoSchemacraft_P18_D4] — tekst] 주간 초기화 시점에 진행 중인 도상구축은 종료되므로, 이를 유의해주시기 바랍니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D4].content
   limit: do 120 znaków
   EN: Any Schemacraft run in progress ends at the weekly reset. Plan your runs accordingly.
   PL: Trwająca Konstrukcja Schematów kończy się w momencie cotygodniowego resetu — prosimy mieć to na uwadze.
334. [Samouczek i wskazówki [TutoSchemacraft_P18_D6] — tekst] 현재 개방된 최고 레벨에 도달하면, 다음 구간이 개방될 때까지 플레이로 패스 경험치를 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D6].content
   limit: do 160 znaków
   EN: When you reach the highest level currently available, you can no longer earn Pass EXP from playing until more levels unlock.
   PL: Po osiągnięciu najwyższego otwartego obecnie poziomu nie zdobędziesz kolejnych PD Przepustki za grę aż do odblokowania następnego progu.
335. [Samouczek i wskazówki [TutoSchemacraft_P18_T2] — tekst] 업적
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_T2].content
   limit: do 120 znaków
   EN: Achievements
   PL: Osiągnięcia
336. [Samouczek i wskazówki [TutoSchemacraft_P18_D5] — tekst] 업적은 향후 업데이트를 통해 추가될 예정입니다.
   źródło: TutorialMainUIText.json :: dataList[id=TutoSchemacraft_P18_D5].content
   limit: do 120 znaków
   EN: Achievements will be added in a future update.
   PL: Osiągnięcia zostaną dodane w przyszłej aktualizacji.

## Samouczek i wskazówki: TutorialMainUIText_pilgrimage
- plik gry: `TutorialMainUIText_pilgrimage.json`

337. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P1_T1] — tekst] 발푸르기스의 밤
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P1_T1].content
   limit: do 120 znaków
   EN: Walpurgis Night
   PL: Noc Walpurgii
338. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P1_D1] — tekst] 이벤트 기간동안 발푸르기스의 밤 특정 추출이 진행됩니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P1_D1].content
   limit: do 120 znaków
   EN: Walpurgis Night Target Extractions will be available during the event period.
   PL: W trakcie wydarzenia dostępna jest Ekstrakcja Celowana Nocy Walpurgii.
339. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P1_D2] — tekst] 발푸르기스의 밤 특정 추출에서는 이번 회차의 발푸르기스의 밤 인격 및 E.G.O의 등장 확률이 상승합니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P1_D2].content
   limit: do 190 znaków
   EN: Walpurgis Night Target Extractions will have higher Extraction rates for Identities and E.G.O from the currently active Walpurgis Night event.
   PL: W Ekstrakcji Celowanej Nocy Walpurgii zwiększona jest szansa wylosowania Tożsamości oraz E.G.O z bieżącej edycji Nocy Walpurgii.
340. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P1_D3] — tekst] 파도의 만가 이스마엘은 [선의의 순례 이벤트 보상]에서만 획득할 수 있으며, 추출, 자판기, 이상 교환을 통해서는 획득할 수 없습니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P1_D3].content
   limit: do 200 znaków
   EN: Tidal Elegy Ishmael can only be obtained as a [Pilgrimage of Compassion Event Reward]; it cannot be obtained via Extraction, Dispenser, or Yisang Exchange.
   PL: Elegię Fal Ishmael można zdobyć wyłącznie jako [nagrodę wydarzenia Pielgrzymka Współczucia] — nie jest dostępna w Ekstrakcji, Automacie ani Wymianie Yisanga.
341. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P1_D4] — tekst] ※ E.G.O는 비복원 추출로 진행됩니다. 이에 따라, 이미 획득한 E.G.O는 추출에서 등장하지 않으니 참고해주시기 바랍니다.\n(이미 획득한 E.G.O는 이상 교환 목록에서도 보유 중으로 표시되어 교환할 수 없습니다.)
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P1_D4].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ E.G.O, once Extracted, are removed from the Extraction pool. This means that once an E.G.O is obtained, it cannot be Extracted again.\n(In Yisang Exchange, already-obtained E.G.O will be labeled “Owned”, and cannot be exchanged for.)
   PL: ※ E.G.O losowane są bez powtórzeń — raz zdobyte E.G.O nie pojawi się ponownie w Ekstrakcji.\n(Na liście Wymiany Yisanga posiadane E.G.O oznaczone jest jako posiadane i nie podlega wymianie).
342. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P2_D1] — tekst] 이벤트 기간동안 다른 추출(시즌 관련 추출 제외)에서도 이번 회차의 발푸르기스의 밤 인격 및 E.G.O가 등장합니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P2_D1].content
   limit: do 240 znaków
   EN: During the event period, Identities & E.G.O from the current Walpurgis Night event will be Extractable from other Extraction banners(save for Season relevant Extraction banners) as well.
   PL: W trakcie wydarzenia Tożsamości oraz E.G.O z bieżącej Nocy Walpurgii mogą pojawić się także w innych Ekstrakcjach (z wyjątkiem powiązanych z sezonem).
343. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P2_D2] — tekst] 단, 이러한 경우에는 등장 확률이 별도로 상승하지 않습니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P2_D2].content
   limit: do 120 znaków
   EN: However, their extraction rates will be identical to those of other Identities & E.G.O.
   PL: W takich Ekstrakcjach szansa ich pojawienia się nie jest jednak dodatkowo zwiększona.
344. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P3_D1] — tekst] 이벤트 기간이 종료되면 발푸르기스의 밤 인격과 E.G.O가 모든 추출 목록에서 사라집니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P3_D1].content
   limit: do 130 znaków
   EN: Once the event period is over, Walpurgis Night Identities and E.G.O will no longer be Extractable.
   PL: Po zakończeniu wydarzenia Tożsamości i E.G.O Nocy Walpurgii znikają ze wszystkich list Ekstrakcji.
345. [Samouczek i wskazówki [TutoSpecialEvent_Pilgrimage_P3_D2] — tekst] 이벤트 기간 동안 모든 추출(시즌 관련 추출 제외)에서 다른 회차의 발푸르기스의 밤 인격 및 E.G.O가 등장합니다. 단, 이러한 경우에는 다른 인격 및 E.G.O와 등장 확률이 동일합니다.
   źródło: TutorialMainUIText_pilgrimage.json :: dataList[id=TutoSpecialEvent_Pilgrimage_P3_D2].content
   limit: do 300 znaków
   EN: During the event period, previous Walpurgis Night Identities & E.G.O will be Extractable from all Extraction banners(save for Season relevant Extraction banners). However, they will not receive increased rates for those Extractions.
   PL: W trakcie wydarzenia we wszystkich Ekstrakcjach (z wyjątkiem powiązanych z sezonem) mogą pojawić się Tożsamości i E.G.O z poprzednich edycji Nocy Walpurgii, lecz bez zwiększonej szansy wylosowania.

## Samouczek i wskazówki: TutorialMirrorDungeon
- plik gry: `TutorialMirrorDungeon.json`

346. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_01_title_01] — tekst] 폭풍의 거울
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_01_title_01].content
   limit: do 120 znaków
   EN: Mirror of the Wuthering
   PL: Lustro Wichury
347. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_01_desc_01] — tekst] 시즌 4 거울 던전의 명칭은 폭풍의 거울로 불립니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_01_desc_01].content
   limit: do 120 znaków
   EN: Season 4's Mirror Dungeon is called 'Mirror of the Wuthering'.
   PL: Lustrzane Lochy Sezonu 4 noszą nazwę „Lustro Wichury”.
348. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_01_desc_02] — tekst] 시뮬레이션 난이도와 리토르넬로 난이도 중 하나를 선택하여 입장할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_01_desc_02].content
   limit: do 120 znaków
   EN: Choose between 'Simulation' and 'Ritornello' difficulties to enter.
   PL: Przed wejściem wybierz poziom trudności: Symulacja lub Ritornello.
349. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_02_title_01] — tekst] 주간 추가 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_02_title_01].content
   limit: do 120 znaków
   EN: Weekly Bonuses
   PL: Cotygodniowa Premia
350. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_02_desc_01] — tekst] 거울 던전에서는 주간 추가 보상 기회가 제공됩니다. 보상 수령 시점에 추가 보상 기회를 사용하면 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_02_desc_01].content
   limit: do 200 znaków
   EN: Every week, Mirror Dungeons offer Weekly Bonuses. Use Weekly Bonuses when you're claiming the rewards for the run—and receive greatly increased rewards.
   PL: W Lustrzanych Lochach dostępna jest Cotygodniowa Premia. Wykorzystanie jej szansy przy odbiorze nagród znacznie zwiększa zdobywane łupy.
351. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_02_desc_02] — tekst] 주간 추가 보상은 난이도 관계없이 매주 최대 3회까지 제공됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_02_desc_02].content
   limit: do 120 znaków
   EN: Every week, you can receive 3 Weekly Bonuses regardless of difficulty.
   PL: Niezależnie od poziomu trudności co tydzień dostępne są maksymalnie 3 Cotygodniowe Premie.
352. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_02_desc_03] — tekst] 리토르넬로 난이도 클리어 시에는 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_02_desc_03].content
   limit: do 190 znaków
   EN: In Ritornello difficulty, you can use 2 or more Weekly Bonuses at once, and will receive rewards proportional to the number of Weekly Bonuses used.
   PL: Po ukończeniu poziomu Ritornello możesz zużyć naraz 2 lub więcej szans Cotygodniowej Premii i otrzymać proporcjonalne do tego nagrody.
353. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_02_desc_04] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_02_desc_04].content
   limit: do 150 znaków
   EN: However, it is more enkephalin-efficient to use all 3 Weekly Bonuses at once rather than to use them one at a time.
   PL: Najwyższą wydajność nagród w przeliczeniu na zużytą Enkefalinę daje jednak wykorzystywanie Cotygodniowej Premii pojedynczo (po 1 razie).
354. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_title_01] — tekst] 수감자
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_title_01].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
355. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_desc_01] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can view your currently deployed Sinners here.
   PL: Tutaj sprawdzisz bieżące ustawienie Grzeszników.
356. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_title_02] — tekst] 시작 버프
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_title_02].content
   limit: do 120 znaków
   EN: Starter Buffs
   PL: Wzmocnienia startowe
357. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_desc_02] — tekst] 거울 던전 클리어 시 획득하는 별빛을 사용하여 거울 던전 진행에 도움이 되는 다양한 버프를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_desc_02].content
   limit: do 180 znaków
   EN: Collect Starlight from completing Mirror Dungeons and use them to obtain several Starter Buffs that will help you in the Mirror Dungeon.
   PL: Wykorzystaj Gwiezdny Blask zdobywany za kończenie Lustrzanych Lochów, aby odblokować rozmaite wzmocnienia ułatwiające wyprawy.
358. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_title_03] — tekst] 테마팩 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_title_03].content
   limit: do 120 znaków
   EN: Theme Pack Compendium
   PL: Kompendium Pakietów Tematycznych
359. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_desc_03] — tekst] 거울 던전에 등장하는 층 테마팩을 확인할 수 있습니다. 거울 던전 진행 중에 선택한 층 테마에 대한 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_desc_03].content
   limit: do 180 znaków
   EN: You can view the list of Floor Theme Packs that appear in the Mirror Dungeon. Selected Floor Theme Pack records will be collected here.
   PL: Tutaj przejrzysz Pakiety Tematyczne pięter występujące w Lustrzanych Lochach. Zbierane są tu wpisy o wybranych podczas wypraw motywach.
360. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_title_04] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_title_04].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
361. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_03_desc_04] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다. 거울 던전 진행 중에 획득한 E.G.O 기프트의 기록이 추가됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_03_desc_04].content
   limit: do 220 znaków
   EN: You can view the list of E.G.O Gifts that appear in the Mirror Dungeon. Obtaining an E.G.O Gift in the Mirror Dungeon will add an entry to your E.G.O Gift Compendium.
   PL: Tutaj przejrzysz Dary E.G.O występujące w Lustrzanych Lochach. Zdobycie Daru E.G.O podczas wyprawy dodaje jego wpis do Kompendium.
362. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_title_01] — tekst] 시작 버프
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_title_01].content
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_desc_01] — tekst] 시작 버프를 많이 활성화할수록 진행 과정에서 도움이 되는 E.G.O 기프트를 획득할 기회가 많아집니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_desc_01].content
   limit: do 170 znaków
   EN: You can increase your chances of obtaining helpful E.G.O Gifts during your Mirror Dungeon run by activating more Starter Buffs.
   PL: Im więcej wzmocnień startowych aktywujesz, tym większa szansa na zdobycie pomocnych Darów E.G.O w trakcie wyprawy.
364. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_desc_02] — tekst] 시작 버프는 던전의 난이도 상관없이 적용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_desc_02].content
   limit: do 120 znaków
   EN: Starter Buffs do not change with the Mirror Dungeon difficulties.
   PL: Wzmocnienia startowe obowiązują niezależnie od wybranego poziomu trudności lochu.
365. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_title_02] — tekst] 별빛
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_title_02].content
   limit: do 120 znaków
   EN: Starlight
   PL: Gwiezdny Blask
366. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_desc_03] — tekst] 별빛은 거울 던전 클리어 시 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_desc_03].content
   limit: do 120 znaków
   EN: You can obtain Starlight from completing Mirror Dungeon runs.
   PL: Gwiezdny Blask zdobywasz za ukończenie Lustrzanych Lochów.
367. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_04_desc_04] — tekst] 높은 층에 오를수록 더 많은 별빛을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_04_desc_04].content
   limit: do 120 znaków
   EN: The higher you rise through the Mirror Dungeon floors, the more Starlight you will obtain.
   PL: Im wyższe piętro osiągniesz, tym więcej Gwiezdnego Blasku otrzymasz.
368. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_05_title_01] — tekst] 시작 E.G.O 기프트 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_05_title_01].content
   limit: do 120 znaków
   EN: Starting E.G.O Gift Choice
   PL: Wybór początkowego Daru E.G.O
369. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_05_desc_01] — tekst] 거울 던전 입장 시, E.G.O 기프트의 키워드별 항목이 제시됩니다. 처음에는 무작위만 표시되지만 시작 버프를 통해 키워드별 항목을 추가로 개방할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_05_desc_01].content
   limit: do 320 znaków
   EN: When you enter a Mirror Dungeon, you’ll be offered a selection of Keyword-based categories of E.G.O Gifts. At first, you will only have access to the Random category. However, you can unlock more Keyword categories as you activate more Starter Buffs.
   PL: Przy wejściu do Lustrzanych Lochów prezentowane są kategorie Darów E.G.O według słów kluczowych. Początkowo dostępna jest tylko kategoria losowa, lecz kolejne odblokujesz poprzez wzmocnienia startowe.
370. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_05_desc_02] — tekst] 각 키워드별 항목의 등장 E.G.O 기프트는 고정이며, 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_05_desc_02].content
   limit: do 180 znaków
   EN: E.G.O Gifts appearing in each category are fixed. You can choose as many E.G.O Gifts as it is available to you from the same category.
   PL: Pula Darów E.G.O w każdej kategorii słowa kluczowego jest stała; z wybranej kategorii możesz dobrać tyle Darów E.G.O, na ile pozwala twój limit.
371. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_05_desc_03] — tekst] 직전 클리어 시 선택하지 않은 E.G.O 기프트 항목을 선택하여 거울 던전을 클리어한다면 별빛을 추가로 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_05_desc_03].content
   limit: do 160 znaków
   EN: You can obtain extra Starlight by choosing an E.G.O Gift category that you did not use in your immediately preceding run.
   PL: Ukończenie Lustrzanych Lochów z kategorią Darów E.G.O niewybraną w bezpośrednio poprzedzającej wyprawie zapewnia dodatkowy Gwiezdny Blask.
372. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_06_title_01] — tekst] 수감자 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_06_title_01].content
   limit: do 120 znaków
   EN: Forming the Team
   PL: Wybór Grzeszników
373. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_06_desc_01] — tekst] 거울 던전에 참여할 수감자를 선택하여 편성합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_06_desc_01].content
   limit: do 120 znaków
   EN: Select Sinners who will participate in the Mirror Dungeon run.
   PL: Wybierz i ustaw Grzeszników, którzy wezmą udział w wyprawie do Lustrzanych Lochów.
374. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_06_desc_02] — tekst] 거울 던전 편성 단계에서는 인격의 레벨에 보정치를 반영하여 45로 적용됩니다. 리토르넬로 난이도에서는 보유한 인격의 레벨이 적용됩니다. (최대 레벨 45)
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_06_desc_02].content
   limit: do 230 znaków
   EN: In the Mirror Dungeon deployment stage, all Identity Levels will be fixed to 45. In the Ritornello difficulty, your current Identity levels will be reflected instead. (Max Lv. 45)
   PL: Na etapie ustawiania składu poziom Tożsamości jest korygowany do 45. Na poziomie Ritornello obowiązuje aktualny poziom posiadanych Tożsamości (maks. 45).
375. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_06_desc_03] — tekst] 1성, 2성 인격을 편성할 경우, 입장 시 코스트를 추가로 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_06_desc_03].content
   limit: do 120 znaków
   EN: Deploy 1★ or 2★ Identities to gain additional Cost upon entry.
   PL: Wystawienie Tożsamości 1★ lub 2★ zapewnia dodatkowy Koszt na starcie.
376. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_06_desc_04] — tekst] 만약 이전 클리어 과정에서 교체를 포함해 한 번도 선택하지 않은 인격을 편성할 경우, 입장 시 코스트를 추가로 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_06_desc_04].content
   limit: do 150 znaków
   EN: Deploy Identities that have not been used in your immediately preceding Run to gain additional Cost upon entry.
   PL: Wystawienie Tożsamości nieużywanych w poprzedniej ukończonej wyprawie (wliczając wymiany) zapewnia dodatkowy Koszt na starcie.
377. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_07_title_01] — tekst] 휴식 게이지
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_07_title_01].content
   limit: do 120 znaków
   EN: Rest Bonus
   PL: Pasek Odpoczynku
378. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_07_desc_01] — tekst] 거울 던전 클리어 시, 편성한 인격의 휴식 게이지가 전부 소모되고 그 수치의 총합만큼 별빛을 추가로 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_07_desc_01].content
   limit: do 210 znaków
   EN: The deployed Identity's Rest Bonus will be completely exhausted upon clearing the Mirror Dungeon. The more Rest Bonus you exhaust, the more Starlight you will earn.
   PL: Po ukończeniu Lustrzanych Lochów cały Pasek Odpoczynku wystawionych Tożsamości zostaje zużyty, a jego suma zapewnia dodatkowy Gwiezdny Blask.
379. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_07_desc_02] — tekst] 단, 게임 진행 과정에서 한 번이라도 교체된 인격은 휴식 게이지가 소모되지 않아 별빛을 획득할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_07_desc_02].content
   limit: do 210 znaków
   EN: However, Identities that have been swapped in or out during the Mirror Dungeon run will not spend their Rest Bonuses, and will not provide additional Starlight.
   PL: Tożsamości wymienione choć raz w trakcie wyprawy nie zużywają jednak Paska Odpoczynku i nie dają dodatkowego Gwiezdnego Blasku.
380. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_07_desc_03] — tekst] 휴식 게이지를 소모하였거나 한 번이라도 교체된 인격을 제외한 나머지 모든 인격은 휴식 게이지가 한 칸 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_07_desc_03].content
   limit: do 170 znaków
   EN: Identities that did not spend their Rest Bonuses, and Identities that were not swapped in or out will gain 1 Bar of Rest Bonus.
   PL: Wszystkie pozostałe Tożsamości, które nie zużyły Paska Odpoczynku ani nie były wymieniane, zyskują 1 segment Paska Odpoczynku.
381. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_08_title_01] — tekst] 거울 던전 입장
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_08_title_01].content
   limit: do 120 znaków
   EN: Entering the Mirror Dungeon
   PL: Wejście do Lustrzanych Lochów
382. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_08_desc_01] — tekst] 인격과 E.G.O 편성을 완료하였다면 확인 버튼을 통해 거울 던전 스테이지로 입장할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_08_desc_01].content
   limit: do 120 znaków
   EN: After finishing up the initial Team setup, press 'Confirm' to enter the Mirror Dungeon.
   PL: Po zakończeniu ustawiania Tożsamości i E.G.O naciśnij przycisk potwierdzenia, aby wejść do Lustrzanych Lochów.
383. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_08_desc_02] — tekst] 편성 과정에서 획득하게 된 추가 코스트 수량 합계가 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_08_desc_02].content
   limit: do 120 znaków
   EN: This area displays the additional Cost you have gained over the deployment process.
   PL: Tutaj widnieje łączna suma dodatkowego Kosztu uzyskanego podczas ustawiania składu.
384. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_09_title_01] — tekst] 층 테마팩 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_09_title_01].content
   limit: do 120 znaków
   EN: Selecting Floor Theme Packs
   PL: Wybór Pakietu Tematycznego piętra
385. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_09_desc_01] — tekst] 층 진입 시, 이번 층에서 마주할 테마를 제시된 목록 중에서 선택할 수 있습니다. 선택하고자 하는 테마팩을 아래로 드래그하여 고를 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_09_desc_01].content
   limit: do 270 znaków
   EN: Upon entering a new Floor, you will be presented with a collection of different 'Themes' that you can choose to face on this Floor. Select and pull down a Theme Pack you would like to challenge for this Floor.
   PL: Przy wejściu na piętro wybierasz z listy motyw, z którym zmierzysz się na tym piętrze. Przeciągnij wybrany Pakiet Tematyczny w dół, aby go zatwierdzić.
386. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_09_desc_02] — tekst] 각각의 층 테마팩 우상단 버튼을 통해 해당 팩에서 등장할 수 있는 보스와 E.G.O 기프트를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_09_desc_02].content
   limit: do 180 znaków
   EN: You can view the available Bosses and E.G.O Gifts from the Theme Pack by pressing this button in the top right corner of each Theme Pack.
   PL: Przycisk w prawym górnym rogu każdego Pakietu Tematycznego pozwala sprawdzić możliwych bossów oraz Dary E.G.O z tego pakietu.
387. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_09_desc_03] — tekst] 층 테마팩 하단에는 해당 층 테마의 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_09_desc_03].content
   limit: do 180 znaków
   EN: At the bottom of the Floor Theme Packs, you can view the E.G.O Gifts that you can choose from after defeating the boss of the Floor Theme.
   PL: U dołu Pakietu Tematycznego widnieje lista Darów E.G.O do wyboru po pokonaniu bossa danego piętra.
388. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_09_desc_04] — tekst] 층 테마마다 각각 적, E.G.O 기프트, 선택지의 등장 범위가 정해져 있기 때문에, 현재 편성으로 상대하기 유리한 적들이나 편성에 도움이 되는 E.G.O 기프트가 존재하는 층 테마팩을 선택하는 것이 효율적입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_09_desc_04].content
   limit: do 310 znaków
   EN: Because each Floor Theme has a set range of E.G.O Gifts and Choices, it would be most effective to choose the Floor Theme Pack that has enemies that are weak to your current Team composition, or Floor Theme Packs with E.G.O Gifts that you need.
   PL: Każdy motyw piętra ma określoną pulę wrogów, Darów E.G.O oraz wydarzeń — najkorzystniej wybierać Pakiety Tematyczne z przeciwnikami podatnymi na twój obecny skład lub zawierające potrzebne drużynie Dary E.G.O.
389. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_10_title_01] — tekst] 거울 던전 탐사
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_10_title_01].content
   limit: do 120 znaków
   EN: Exploring Mirror Dungeons
   PL: Eksploracja Lustrzanych Lochów
390. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_10_desc_01] — tekst] 거울 던전에 입장하게 되면 방과 경로가 무작위로 생성됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_10_desc_01].content
   limit: do 120 znaków
   EN: The Mirror Dungeon rooms and paths are randomly generated.
   PL: Po wejściu do Lustrzanych Lochów komnaty oraz ścieżki generowane są losowo.
391. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_10_desc_02] — tekst] 현재 방에서 연결된 방을 선택해 진행하며, 각 방에선 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_10_desc_02].content
   limit: do 170 znaków
   EN: You proceed by moving to nodes adjacent to your current node. You may find various events or combat encounters in each of the nodes.
   PL: Poruszasz się, wybierając komnaty połączone z bieżącą; w każdej z nich losowo pojawiają się rozmaite walki oraz wydarzenia.
392. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_10_title_02] — tekst] 별빛과 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_10_title_02].content
   limit: do 120 znaków
   EN: Starlight & Starting Cost
   PL: Gwiezdny Blask i Koszt
393. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_10_desc_03] — tekst] 거울 던전 진행 과정에서 별빛과 코스트를 획득할 수 있습니다. 별빛으로는 시작 버프 별새김을, 코스트로는 진행 중 상점이나 쉼터의 기능을 이용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_10_desc_03].content
   limit: do 290 znaków
   EN: You will earn 'Starlight' and 'Cost' as you proceed through the Mirror Dungeon. Starlight can be spent to engrave stars(activate) Starter Buffs, and 'Cost' can be spent at Shops and Rest Stops found in the Mirror Dungeon.
   PL: W trakcie wyprawy zdobywasz Gwiezdny Blask oraz Koszt. Gwiezdny Blask pozwala wyryć gwiazdy wzmocnień startowych, a Koszt służy do korzystania ze Sklepów i Przystanków Odpoczynku.
394. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_title_01] — tekst] E.G.O 기프트
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_title_01].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
395. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_desc_01] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_desc_01].content
   limit: do 170 znaków
   EN: Acquired E.G.O Gifts are displayed here. E.G.O Gifts are items that offer powerful effects that last until the end of the Dungeon.
   PL: Tutaj widnieją zdobyte Dary E.G.O — przedmioty zapewniające potężne efekty działające wewnątrz lochu.
396. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_title_02] — tekst] 스테이지 유효 속성
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_title_02].content
   limit: do 120 znaków
   EN: Effective Attacks
   PL: Skuteczne atrybuty etapu
397. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_desc_02] — tekst] 거울 던전의 전투 방 하단에는 해당 스테이지에서 유효한 속성이 표기됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_desc_02].content
   limit: do 160 znaków
   EN: Below the combat Encounter nodes in Mirror Dungeons are types and affinities effective against the enemies in each node.
   PL: Pod węzłami walk w Lustrzanych Lochach wyświetlane są typy ataków i grzechy skuteczne na danym etapie.
398. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_title_03] — tekst] 수감자 현황
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_title_03].content
   limit: do 120 znaków
   EN: Sinner Status
   PL: Stan Grzeszników
399. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_11_desc_03] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_11_desc_03].content
   limit: do 120 znaków
   EN: The HP, SP, and lost lives of your Sinners will carry over between encounters.
   PL: Przez cały czas trwania wyprawy PŻ, PP oraz stan poległych Grzeszników przechodzą między walkami.
400. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_12_title_01] — tekst] 상점
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_12_title_01].content
   limit: do 120 znaków
   EN: Shops
   PL: Sklep
401. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_12_desc_01] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 아군 회복, 추가 편성, 제시된 인격 강화를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_12_desc_01].content
   limit: do 190 znaków
   EN: At Shops, you can spend your 'Cost' to purchase E.G.O Gifts, heal allies, deploy/swap out additional Identities or power up selected Identities.
   PL: W Sklepie możesz wydawać Koszt, aby kupować Dary E.G.O, leczyć sojuszników, dobierać skład lub wzmacniać wskazane Tożsamości.
402. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_12_desc_02] — tekst] 사용하지 않는 E.G.O 기프트를 상점에서 판매하여 코스트를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_12_desc_02].content
   limit: do 120 znaków
   EN: At Shops, you can sell E.G.O Gifts you don't use to obtain 'Cost'.
   PL: W Sklepie możesz sprzedawać nieużywane Dary E.G.O, aby zyskać Koszt.
403. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_13_title_01] — tekst] 쉼터
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_13_title_01].content
   limit: do 120 znaków
   EN: Rest Stops
   PL: Przystanek Odpoczynku
404. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_13_desc_01] — tekst] 코스트를 소모하여 아군 회복, 추가 편성, E.G.O 기프트 강화를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_13_desc_01].content
   limit: do 160 znaków
   EN: At Rest Stops, you can spend your 'Cost' to heal allies, deploy/swap out additional Identities or enhance E.G.O Gifts.
   PL: Na Przystanku Odpoczynku możesz wydać Koszt na leczenie sojuszników, dobór składu oraz ulepszanie Darów E.G.O.
405. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_13_desc_02] — tekst] E.G.O 기프트를 합성하여 다른 E.G.O 기프트를 노려볼 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_13_desc_02].content
   limit: do 120 znaków
   EN: You can Fuse E.G.O Gifts to obtain different E.G.O Gifts.
   PL: Możesz też syntezować Dary E.G.O, aby spróbować zdobyć inny Dar E.G.O.
406. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_14_title_01] — tekst] 전투 보상 카드
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_14_title_01].content
   limit: do 120 znaków
   EN: Encounter Reward Cards
   PL: Karty Nagród za Walkę
407. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_14_desc_01] — tekst] 전투에서 승리하면 전투 난이도에 따라 일정 확률로 전투 보상 카드가 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_14_desc_01].content
   limit: do 240 znaków
   EN: There is a chance for 'Encounter Reward Cards' to appear after winning an Encounter. The harder the Encounter difficulty, the higher the chance of obtaining an Encounter Reward Card.
   PL: Po zwycięstwie w starciu masz zależną od trudności walki szansę na pojawienie się Kart Nagród za Walkę.
408. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_14_desc_02] — tekst] 전투 보상 카드를 통해 코스트, 별빛, E.G.O 기프트 또는 E.G.O 자원을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_14_desc_02].content
   limit: do 160 znaków
   EN: You can obtain various resources such as Cost, Starlight, E.G.O Gifts, or E.G.O Resources from the Encounter Reward Cards.
   PL: Z Kart Nagród za Walkę zdobędziesz Koszt, Gwiezdny Blask, Dary E.G.O lub zasoby E.G.O.
409. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_15_title_01] — tekst] 층 버프
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_15_title_01].content
   limit: do 120 znaków
   EN: Floor Buffs
   PL: Wzmocnienia piętra
410. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_15_desc_01] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 무작위 적 버프를 획득하게 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_15_desc_01].content
   limit: do 120 znaków
   EN: Upon clearing a floor, you will obtain random enemy buffs tied to each E.G.O Gifts.
   PL: Po ukończeniu piętra wraz z Darem E.G.O nakładane jest powiązane z nim losowe wzmocnienie wrogów.
411. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_15_desc_02] — tekst] 층을 클리어할 때마다 적 버프는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_15_desc_02].content
   limit: do 120 znaków
   EN: Enemy Buffs will continue to stack with every floor cleared.
   PL: Wzmocnienia wrogów kumulują się z każdym ukończonym piętrem.
412. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_16_title_01] — tekst] 거울 던전 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_16_title_01].content
   limit: do 120 znaków
   EN: Mirror Dungeon Rewards
   PL: Nagrody Lustrzanych Lochów
413. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_16_desc_01] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_16_desc_01].content
   limit: do 120 znaków
   EN: Upon clearing a Mirror Dungeon run, spend Enkephalin Modules to claim your rewards.
   PL: Po ukończeniu Lustrzanych Lochów wydaj Moduły Enkefaliny, aby odebrać nagrody.
414. [Samouczek i wskazówki [tutorial_mirrordungeon04_page_16_desc_02] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=tutorial_mirrordungeon04_page_16_desc_02].content
   limit: do 160 znaków
   EN: The amount of rewards depends on the number of cleared Floors. You can use Weekly Bonus chances to claim even more rewards.
   PL: Liczba nagród zależy od ukończonych pięter; użyj szans Cotygodniowej Premii, aby zdobyć ich jeszcze więcej.
415. [Samouczek i wskazówki [TutoMD05_P1_T1] — tekst] 꿈결의 거울
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P1_T1].content
   limit: do 120 znaków
   EN: Mirror of the Dreaming
   PL: Lustro Snu
416. [Samouczek i wskazówki [TutoMD05_P1_D1] — tekst] 시즌 5 거울 던전의 명칭은 꿈결의 거울로 불립니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P1_D1].content
   limit: do 120 znaków
   EN: Season 5's Mirror Dungeon is called 'Mirror of the Dreaming'.
   PL: Lustrzane Lochy Sezonu 5 noszą nazwę „Lustro Snu”.
417. [Samouczek i wskazówki [TutoMD05_P1_D2] — tekst] 문 또는 입장 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P1_D2].content
   limit: do 120 znaków
   EN: Select the door or the "Enter" button to begin your Mirror Dungeon run.
   PL: Kliknij drzwi lub przycisk wejścia, aby rozpocząć wyprawę.
418. [Samouczek i wskazówki [TutoMD05_P2_T1] — tekst] 주간 추가 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P2_T1].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Samouczek i wskazówki [TutoMD05_P2_D1] — tekst] 거울 던전에서는 매주 3회의 주간 추가 보상 기회가 제공됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P2_D1].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every week, you're given 3 Weekly Bonus eligibilities\nto gain additional Mirror Dungeon rewards.
   PL: Co tydzień w Lustrzanych Lochach otrzymujesz\n3 szanse na Cotygodniową Premię.
420. [Samouczek i wskazówki [TutoMD05_P2_D2] — tekst] 보상 수령 시 주간 추가 보상 기회를 사용하면, 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P2_D2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Using a Weekly Bonus eligibility when claiming your reward,\nand receive greatly increased rewards.
   PL: Wykorzystanie szansy Cotygodniowej Premii przy odbiorze\nznacznie zwiększa zdobywane nagrody.
421. [Samouczek i wskazówki [TutoMD05_P2_D3] — tekst] 모든 테마팩을 Hard 난이도로 클리어 시, 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P2_D3].content
   limit: do 240 znaków
   EN: If you chose Hard difficulty Theme Packs for every Floor, you can consume 2 or more Weekly Bonuses at once, and will receive rewards proportional to the number of Weekly Bonuses used.
   PL: Ukończenie wszystkich Pakietów Tematycznych na poziomie Hard pozwala zużyć naraz 2 lub więcej szans Cotygodniowej Premii i zyskać proporcjonalne nagrody.
422. [Samouczek i wskazówki [TutoMD05_P2_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P2_D4].content
   limit: do 150 znaków
   EN: However, it is more enkephalin-efficient to use 1 Weekly Bonus at a time rather than to use them all at once.
   PL: Najwyższą wydajność nagród względem zużytej Enkefaliny daje jednak wykorzystywanie Cotygodniowej Premii pojedynczo (po 1 razie).
423. [Samouczek i wskazówki [TutoMD05_P3_T1] — tekst] 수감자
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_T1].content
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Samouczek i wskazówki [TutoMD05_P3_D1] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_D1].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Samouczek i wskazówki [TutoMD05_P3_T2] — tekst] 테마팩 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_T2].content
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Samouczek i wskazówki [TutoMD05_P3_D2] — tekst] 거울 던전에 등장하는 테마팩을 확인할 수 있습니다. 거울 던전 진행 중 선택한 테마팩에 대한 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_D2].content
   limit: do 160 znaków
   EN: You can view the list of Theme Packs that appear in the Mirror Dungeon. Selected Theme Pack records will be collected here.
   PL: Tutaj przejrzysz Pakiety Tematyczne występujące w Lustrzanych Lochach. Zbierane są tu wpisy o wybranych podczas wypraw pakietach.
427. [Samouczek i wskazówki [TutoMD05_P3_T3] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_T3].content
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Samouczek i wskazówki [TutoMD05_P3_D3] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다. 거울 던전 진행 중에 획득한 E.G.O 기프트의 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P3_D3].content
   limit: do 220 znaków
   EN: You can view the list of E.G.O Gifts that appear in the Mirror Dungeon. Obtaining an E.G.O Gift in the Mirror Dungeon will add an entry to your E.G.O Gift Compendium.
   PL: Tutaj przejrzysz Dary E.G.O występujące w Lustrzanych Lochach. Zdobycie Daru E.G.O podczas wyprawy dodaje jego wpis do Kompendium.
429. [Samouczek i wskazówki [TutoMD05_P4_T1] — tekst] 편성 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P4_T1].content
   limit: do 120 znaków
   EN: Creating your TEAM
   PL: Wybór składu
430. [Samouczek i wskazówki [TutoMD05_P4_D1] — tekst] 참여할 인격을 선택하여 편성합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P4_D1].content
   limit: do 120 znaków
   EN: Select Identities to run this Dungeon with.
   PL: Wybierz i ustaw Tożsamości, które wezmą udział w wyprawie.
431. [Samouczek i wskazówki [TutoMD05_P4_D2] — tekst] 거울 던전 Normal 난이도에서는 인격 레벨이 50으로 적용됩니다. Hard 난이도에서는 보유한 인격의 레벨이 적용됩니다. (최대 Lv.50)
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P4_D2].content
   limit: do 210 znaków
   EN: In Mirror Dungeon Normal, all Identity Levels will be fixed to 50. In Mirror Dungeon Hard, your current Identity levels will be reflected instead. (max Lv. 50)
   PL: Na poziomie Normal poziom Tożsamości wynosi 50. Na poziomie Hard obowiązuje aktualny poziom posiadanych Tożsamości (maks. 50).
432. [Samouczek i wskazówki [TutoMD05_P5_T1] — tekst] 휴식 보너스
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_T1].content
   limit: do 120 znaków
   EN: Rest Bonus
   PL: Premia Odpoczynku
433. [Samouczek i wskazówki [TutoMD05_P5_D1] — tekst] 거울 던전 입장 시, 편성한 인격의 휴식 보너스를 이용하여 꿈결 별의 가호에서 특별한 효과를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_D1].content
   limit: do 190 znaków
   EN: Upon entering Mirror Dungeon, you can spend the Rest Bonus of the Identities in your Team to select special effects from Grace of the Dreaming Star.
   PL: Przy wejściu do Lustrzanych Lochów możesz wykorzystać Premię Odpoczynku wystawionych Tożsamości, aby wybrać specjalne efekty Błogosławieństwa Śniącej Gwiazdy.
434. [Samouczek i wskazówki [TutoMD05_P5_D2] — tekst] 거울 던전을 클리어하면 입장 시 편성한 인격의 휴식 보너스는 0으로 초기화되고 편성하지 않은 모든 인격의 휴식 보너스가 1 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_D2].content
   limit: do 200 znaków
   EN: Upon clearing Mirror Dungeon, Rest Bonus for Identities in your current Mirror Dungeon Team resets to 0, and every other Identity gains 1 Rest Bonus.
   PL: Po ukończeniu Lustrzanych Lochów Premia Odpoczynku początkowego składu resetuje się do 0, a wszystkie niewystawione Tożsamości zyskują +1 Premii Odpoczynku.
435. [Samouczek i wskazówki [TutoMD05_P5_D3] — tekst] 게임 진행 과정에서 편성을 교체하여 등장한 인격은 휴식 게이지가 소모되거나 증가하지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_D3].content
   limit: do 170 znaków
   EN: Identities that have been swapped in or out during the Mirror Dungeon run will, however, neither spend nor gain Rest Bonuses.
   PL: Tożsamości wprowadzone poprzez wymianę składu w trakcie wyprawy nie zużywają ani nie zyskują Paska Odpoczynku.
436. [Samouczek i wskazówki [TutoMD05_P5_D4] — tekst] 인격과 E.G.O 편성을 완료하였다면 확인 버튼을 통해 거울 던전에 입장할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_D4].content
   limit: do 130 znaków
   EN: Once you're finished with the Team ID & E.G.O setup, press 'Confirm' to enter the Mirror Dungeon.
   PL: Po zakończeniu ustawiania Tożsamości i E.G.O naciśnij przycisk potwierdzenia, aby wejść do Lustrzanych Lochów.
437. [Samouczek i wskazówki [TutoMD05_P5_D5] — tekst] 현재 편성의 휴식 보너스 합계를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P5_D5].content
   limit: do 120 znaków
   EN: You can view your team's sum of Rest Bonuses here.
   PL: Tutaj sprawdzisz sumę Premii Odpoczynku bieżącego składu.
438. [Samouczek i wskazówki [TutoMD05_P6_T1] — tekst] 꿈결 별의 가호
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_T1].content
   limit: do 120 znaków
   EN: Grace of the Dreaming Star
   PL: Błogosławieństwo Śniącej Gwiazdy
439. [Samouczek i wskazówki [TutoMD05_P6_D1] — tekst] 보유한 휴식 보너스를 지불하여 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_D1].content
   limit: do 120 znaków
   EN: Spend your Team's Rest Bonuses to select Graces of Stars.
   PL: Wydaj posiadaną Premię Odpoczynku, aby wybrać Błogosławieństwa Gwiazd.
440. [Samouczek i wskazówki [TutoMD05_P6_T2] — tekst] 잔여 휴식 보너스
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_T2].content
   limit: do 120 znaków
   EN: Remaining Rest Bonus
   PL: Pozostała Premia Odpoczynku
441. [Samouczek i wskazówki [TutoMD05_P6_D2] — tekst] 별의 가호를 선택하고 남은 휴식 보너스는 던전 진행 중 사용할 코스트로 전환됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_D2].content
   limit: do 160 znaków
   EN: Remaining Rest Bonus after selecting Graces of Stars will be converted to 'Cost' to be used during your Mirror Dungeon run.
   PL: Premia Odpoczynku pozostała po wyborze Błogosławieństw Gwiazd zamienia się w Koszt do wykorzystania w trakcie wyprawy.
442. [Samouczek i wskazówki [TutoMD05_P6_D3] — tekst] 별의 가호 패시브는 휴식 보너스를 일정 수치 보유한 상태면 자동으로 적용되며, 휴식 보너스를 별도로 소모하지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_D3].content
   limit: do 160 znaków
   EN: Grace of Stars Passives do not consume your Rest Bonuses; they activate automatically if you have enough Rest Bonuses.
   PL: Pasywki Błogosławieństwa Gwiazd aktywują się automatycznie po osiągnięciu wymaganego progu Premii Odpoczynku i nie zużywają jej.
443. [Samouczek i wskazówki [TutoMD05_P6_D4] — tekst] 남은 휴식 보너스는 거울 던전 진행 중 사용할 수 있는 코스트로 전환됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P6_D4].content
   limit: do 120 znaków
   EN: Remaining Rest Bonus will be converted to 'Cost' to be used during your Mirror Dungeon run.
   PL: Pozostała Premia Odpoczynku zamienia się w Koszt dostępny podczas wyprawy w Lustrzanych Lochach.
444. [Samouczek i wskazówki [TutoMD05_P7_T1] — tekst] 시작 E.G.O 기프트 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P7_T1].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Samouczek i wskazówki [TutoMD05_P7_D1] — tekst] 거울 던전 입장 시, E.G.O 기프트의 키워드별 항목이 제시됩니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P7_D1].content
   limit: do 120 znaków
   EN: Upon Mirror Dungeon entry, you will be given Keyword categories to choose E.G.O Gifts from.
   PL: Przy wejściu do Lustrzanych Lochów prezentowane są kategorie Darów E.G.O według słów kluczowych.
446. [Samouczek i wskazówki [TutoMD05_P7_D2] — tekst] 각 키워드별 항목의 등장 E.G.O 기프트는 고정이며, 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P7_D2].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Samouczek i wskazówki [TutoMD05_P7_D3] — tekst] 이 단계에서 선택한 키워드에 해당하는 E.G.O 기프트가 던전 진행 중에 더욱 자주 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P7_D3].content
   limit: do 140 znaków
   EN: Through your Mirror Dungeon run, E.G.O Gifts in the category you selected here will appear more frequently.
   PL: Dary E.G.O odpowiadające wybranemu na tym etapie słowu kluczowemu będą pojawiać się częściej podczas wyprawy.
448. [Samouczek i wskazówki [TutoMD05_P8_T1] — tekst] 테마팩 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_T1].content
   limit: do 120 znaków
   EN: Selecting Theme Packs
   PL: Wybór Pakietu Tematycznego
449. [Samouczek i wskazówki [TutoMD05_P8_D1] — tekst] 층 진입 시, 이번 층에서 헤쳐나갈 테마를 제시된 목록 중에서 선택할 수 있습니다. 선택하고자 하는 테마팩을 아래로 드래그하여 고를 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D1].content
   limit: do 270 znaków
   EN: Upon entering a new Floor, you will be presented with a collection of different 'Themes' that you can choose to face on this Floor. Select and pull down a Theme Pack you would like to challenge for this Floor.
   PL: Przy wejściu na piętro wybierasz z listy motyw, z którym zmierzysz się na tym piętrze. Przeciągnij wybrany Pakiet Tematyczny w dół, aby go zatwierdzić.
450. [Samouczek i wskazówki [TutoMD05_P8_D2] — tekst] 각각의 테마팩 우상단 버튼을 통해 해당 팩에서 등장할 수 있는 보스와 전투 보상으로 얻을 수 있는 E.G.O 기프트를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D2].content
   limit: do 220 znaków
   EN: You can view the available Bosses and E.G.O Gifts(obtainable as Encounter rewards) from the Theme Pack by pressing this button in the top right corner of each Theme Pack.
   PL: Przycisk w prawym górnym rogu każdego Pakietu Tematycznego pozwala sprawdzić możliwych bossów oraz Dary E.G.O dostępne jako nagrody za walki.
451. [Samouczek i wskazówki [TutoMD05_P8_D3] — tekst] 테마팩 하단에는 해당 테마팩의 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D3].content
   limit: do 180 znaków
   EN: At the bottom of the Theme Packs, you can view the list of E.G.O Gifts that you can choose from after defeating the boss of this Theme Pack.
   PL: U dołu Pakietu Tematycznego widnieje lista Darów E.G.O proponowanych po pokonaniu bossa tego pakietu.
452. [Samouczek i wskazówki [TutoMD05_P8_T2] — tekst] 테마팩 난이도 변경
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_T2].content
   limit: do 120 znaków
   EN: Choosing the Theme Pack Difficulty
   PL: Zmiana trudności Pakietu Tematycznego
453. [Samouczek i wskazówki [TutoMD05_P8_D4] — tekst] 꿈결의 거울에서는 테마팩 선택 단계에서 원하는 난이도를 선택하여 입장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D4].content
   limit: do 150 znaków
   EN: In Mirror of the Dreaming, you can select the difficulty of the upcoming floor in the Theme Pack selection phase.
   PL: W Lustrze Snu na etapie wyboru Pakietu Tematycznego wybierasz również poziom trudności nadchodzącego piętra.
454. [Samouczek i wskazówki [TutoMD05_P8_D5] — tekst] 단, Hard 난이도를 선택하여 입장하면 이후에는 난이도를 변경할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D5].content
   limit: do 120 znaków
   EN: However, once you enter the Hard difficulty, it cannot be changed again.
   PL: Po wybraniu i wejściu na poziom Hard nie można już jednak zmienić poziomu trudności z powrotem.
455. [Samouczek i wskazówki [TutoMD05_P8_T3] — tekst] Hard 난이도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_T3].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Samouczek i wskazówki [TutoMD05_P8_D6] — tekst] Hard 난이도 테마팩에서는 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 3개에서 4개로 증가하며, 어떤 E.G.O 기프트는 Hard 난이도에서만 얻을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D6].content
   limit: do 210 znaków
   EN: In Hard Theme Packs, you will be able to choose 4 instead of 3 E.G.O Gifts upon clearing the Floor Boss. Also, some E.G.O Gifts are exclusive to Hard difficulty.
   PL: W Pakietach Tematycznych Hard po pokonaniu bossa piętra pula proponowanych Darów E.G.O rośnie z 3 do 4, a niektóre Dary E.G.O dostępne są wyłącznie na poziomie Hard.
457. [Samouczek i wskazówki [TutoMD05_P8_D7] — tekst] 또한 Hard 난이도에서는 E.G.O 기프트와 고난을 2개씩 선택해야 하며, 특별한 상점이 등장할 수도 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P8_D7].content
   limit: do 170 znaków
   EN: Also, you must select 2 E.G.O Gifts and 2 Mounting Trials in Hard difficulty, and there's a chance for a Super Shop to spawn.
   PL: Ponadto na poziomie Hard musisz wybrać po 2 Dary E.G.O i 2 Próby, a po drodze może pojawić się Wzmocniony Sklep.
458. [Samouczek i wskazówki [TutoMD05_P9_T1] — tekst] 거울 던전 탐사
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P9_T1].content
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Samouczek i wskazówki [TutoMD05_P9_D1] — tekst] 거울 던전에 입장하게 되면 인카운터와 경로가 무작위로 생성됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P9_D1].content
   limit: do 120 znaków
   EN: The Mirror Dungeon Encounters and paths are randomly generated.
   PL: Po wejściu do Lustrzanych Lochów starcia oraz ścieżki generowane są losowo.
460. [Samouczek i wskazówki [TutoMD05_P9_D2] — tekst] 현재 인카운터에서 연결된 인카운터을 선택해 진행하며, 각 인카운터에서는 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P9_D2].content
   limit: do 170 znaków
   EN: You proceed by moving to nodes adjacent to your current node. You may find various events or combat encounters in each of the nodes.
   PL: Poruszasz się, wybierając węzły połączone z bieżącym; w każdym z nich losowo pojawiają się rozmaite walki oraz wydarzenia.
461. [Samouczek i wskazówki [TutoMD05_P9_T2] — tekst] 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P9_T2].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
462. [Samouczek i wskazówki [TutoMD05_P9_D3] — tekst] 거울 던전 진행 과정에서 코스트를 획득할 수 있습니다. 코스트를 지불하여 상점의 기능을 이용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P9_D3].content
   limit: do 170 znaków
   EN: You will earn 'Cost' as you proceed through the Mirror Dungeon. 'Cost' you earned can be spent at Shops for their various services.
   PL: Podczas wyprawy przez Lustrzane Lochy zdobywasz Koszt, za który skorzystasz z funkcji Sklepów.
463. [Samouczek i wskazówki [TutoMD05_P10_T1] — tekst] E.G.O 기프트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_T1].content
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Samouczek i wskazówki [TutoMD05_P10_D1] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_D1].content
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Samouczek i wskazówki [TutoMD05_P10_T2] — tekst] 스테이지 유효 속성과 획득 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_T2].content
   limit: do 120 znaków
   EN: Effective Attacks & Cost Rewards
   PL: Skuteczne atrybuty i Koszt
466. [Samouczek i wskazówki [TutoMD05_P10_D2] — tekst] 거울 던전의 전투 인카운터에는 해당 전투에서 유효한 속성과 해당 전투를 클리어 시 획득할 수 있는 코스트가 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_D2].content
   limit: do 220 znaków
   EN: Combat Encounter nodes of Mirror Dungeons display affinity/attack type useful for that battle. It also displays the amount of Cost reward you can gain by completing it.
   PL: Na węzłach walk w Lustrzanych Lochach wyświetlane są skuteczne typy ataków i grzechy oraz liczba Kosztu za ukończenie starcia.
467. [Samouczek i wskazówki [TutoMD05_P10_T3] — tekst] 수감자 현황
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_T3].content
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Samouczek i wskazówki [TutoMD05_P10_D3] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_D3].content
   limit: do 120 znaków
   EN: The HP, SP, and lives of Sinners lost will carry over between encounters.
   PL: Przez cały czas trwania wyprawy PŻ, PP oraz stan poległych Grzeszników przechodzą między walkami.
469. [Samouczek i wskazówki [TutoMD05_P10_T4] — tekst] 적용 효과 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_T4].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
470. [Samouczek i wskazówki [TutoMD05_P10_D4] — tekst] 던전을 진행하는 동안 선택한 고난, 휴식 보너스, 선택지 효과를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P10_D4].content
   limit: do 120 znaków
   EN: View your Mounting Trials, Rest Bonus, and Choice Event Effects here.
   PL: Sprawdzisz tu wybrane w trakcie wyprawy Próby, Premię Odpoczynku oraz efekty z wydarzeń.
471. [Samouczek i wskazówki [TutoMD05_P11_T1] — tekst] 상점
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P11_T1].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Samouczek i wskazówki [TutoMD05_P11_D1] — tekst] 테마팩 보스 전투 직전에는 상점이 배치되어 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P11_D1].content
   limit: do 120 znaków
   EN: Nodes before Theme Pack Boss Encounters are shops.
   PL: Tuż przed walką z bossem Pakietu Tematycznego znajduje się Sklep.
473. [Samouczek i wskazówki [TutoMD05_P11_D2] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 회복과 부활, 편성 교체, 인격 스킬 교체를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P11_D2].content
   limit: do 200 znaków
   EN: At Shops, you can spend your 'Cost' to purchase E.G.O Gifts, heal or revive allies, deploy/swap out additional Identities, or replace Identity Skills.
   PL: W Sklepie wydasz Koszt na zakup Darów E.G.O, leczenie i wskrzeszanie, zmianę składu lub wymianę umiejętności Tożsamości.
474. [Samouczek i wskazówki [TutoMD05_P11_D3] — tekst] 또한 E.G.O 기프트를 상점에서 판매하여 코스트를 획득하거나, E.G.O 기프트를 합성하여 더욱 유용한 E.G.O 기프트를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P11_D3].content
   limit: do 170 znaków
   EN: Also, you can sell your E.G.O Gifts at Shops to gain more Cost or Fuse your E.G.O Gifts to gain even more useful E.G.O Gifts.
   PL: Możesz też sprzedawać Dary E.G.O za Koszt albo syntezować je, aby zdobyć jeszcze bardziej przydatne Dary E.G.O.
475. [Samouczek i wskazówki [TutoMD05_P11_D4] — tekst] Hard 난이도로 진행 시, 특별한 상점이 등장할 수 있습니다. 거울 던전 진행 중에 누적 소모한 코스트가 많을수록 특별한 상점이 등장할 확률이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P11_D4].content
   limit: do 210 znaków
   EN: In Hard difficulty, there is a chance for a Super Shop to appear. The more Cost you spend in a Mirror Dungeon run, the greater the chance becomes for it to appear.
   PL: Na poziomie Hard może pojawić się Wzmocniony Sklep — szansa na jego wystąpienie rośnie wraz z łączną ilością wydanego w wyprawie Kosztu.
476. [Samouczek i wskazówki [TutoMD05_P12_T1] — tekst] 전투 보상 카드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P12_T1].content
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Samouczek i wskazówki [TutoMD05_P12_D1] — tekst] 전투에서 승리하면 전투 난이도에 따라 일정 확률로 전투 보상 카드가 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P12_D1].content
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Samouczek i wskazówki [TutoMD05_P12_D2] — tekst] 전투 보상 카드를 통해 코스트,E.G.O 기프트 또는 E.G.O 자원을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P12_D2].content
   limit: do 150 znaków
   EN: You can obtain various resources such as Cost, E.G.O Gifts, or E.G.O Resources from the Encounter Reward Cards.
   PL: Z Kart Nagród za Walkę zdobędziesz Koszt, Dary E.G.O lub zasoby E.G.O.
479. [Samouczek i wskazówki [TutoMD05_P13_T1] — tekst] E.G.O 기프트와 추가되는 고난
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P13_T1].content
   limit: do 120 znaków
   EN: E.G.O Gifts & Mounting Trials
   PL: Dary E.G.O i dodawane Próby
480. [Samouczek i wskazówki [TutoMD05_P13_D1] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 고난 효과를 선택하여 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P13_D1].content
   limit: do 120 znaków
   EN: Upon clearing a floor, you will obtain random enemy buffs linked to each E.G.O Gift.
   PL: Po ukończeniu piętra wybierasz Dar E.G.O wraz z powiązanym z nim efektem Próby.
481. [Samouczek i wskazówki [TutoMD05_P13_D2] — tekst] 층을 클리어할 때마다 고난 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P13_D2].content
   limit: do 120 znaków
   EN: Mounting Trials will continue to stack with every floor cleared.
   PL: Efekty Prób kumulują się z każdym ukończonym piętrem.
482. [Samouczek i wskazówki [TutoMD05_P13_D3] — tekst] Hard 난이도로 진행 시, E.G.O 기프트를 2개 선택할 수 있습니다. 대신 고난 효과도 2개를 선택하게 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P13_D3].content
   limit: do 180 znaków
   EN: In Hard difficulty, you can select 2 E.G.O Gifts. However, this means that you will be selecting 2 Mounting Trials in the process as well.
   PL: Na poziomie Hard możesz wybrać 2 Dary E.G.O, lecz wiąże się to również z wyborem 2 efektów Prób.
483. [Samouczek i wskazówki [TutoMD05_P14_T1] — tekst] 거울 던전 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P14_T1].content
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Samouczek i wskazówki [TutoMD05_P14_D1] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P14_D1].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Samouczek i wskazówki [TutoMD05_P14_D2] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P14_D2].content
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Samouczek i wskazówki [TutoMD05_P14_D3] — tekst] 모든 테마팩을 Hard 난이도로 클리어 시, 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P14_D3].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Samouczek i wskazówki [TutoMD05_P14_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P14_D4].content
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Samouczek i wskazówki [TutoMD05_P15_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P15_T1].content
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Samouczek i wskazówki [TutoMD05_P15_D1] — tekst] 꿈결의 거울 업적을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P15_D1].content
   limit: do 120 znaków
   EN: You can view the Achievements for The Mirror of the Dreaming here.
   PL: Tutaj sprawdzisz Osiągnięcia Lustra Snu.
490. [Samouczek i wskazówki [TutoMD05_P16_T1] — tekst] 업적 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P16_T1].content
   limit: do 120 znaków
   EN: Achievements List
   PL: Lista Osiągnięć
491. [Samouczek i wskazówki [TutoMD05_P16_D1] — tekst] 달성 시 업적 진행도를 얻을 수 있는 업적 목록입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P16_D1].content
   limit: do 120 znaków
   EN: Complete these Achievements to raise your Achievements progress.
   PL: Lista Osiągnięć zapewniających postęp Osiągnięć po ich spełnieniu.
492. [Samouczek i wskazówki [TutoMD05_P16_D2] — tekst] 보상 수령 창에서 엔케팔린 모듈을 소모한 경우에만 클리어한 것으로 적용됩니다.\n\n클리어를 조건으로 하는 업적을 도전하실 때 이를 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P16_D2].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Achievements that require the player to 'clear' the Mirror Dungeon count only when the Enkephalin Modules have been consumed at the reward claim window.\n\nPlease note this information before attempting to complete an Achievement tied to clearing the Mirror Dungeon.
   PL: Ukończenie lochu zaliczane jest wyłącznie wtedy, gdy w oknie odbioru nagród zużyjesz Moduły Enkefaliny.\n\nPamiętaj o tym podczas wykonywania Osiągnięć wymagających ukończenia Lustrzanych Lochów.
493. [Samouczek i wskazówki [TutoMD05_P17_T1] — tekst] 보상 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P17_T1].content
   limit: do 120 znaków
   EN: Rewards List
   PL: Lista nagród
494. [Samouczek i wskazówki [TutoMD05_P17_D1] — tekst] 업적 진행도에 따라 각종 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P17_D1].content
   limit: do 120 znaków
   EN: Receive various rewards by raising your Achievements progress bar.
   PL: Odbieraj rozmaite nagrody wraz ze wzrostem paska postępu Osiągnięć.
495. [Samouczek i wskazówki [TutoMD05_P18_T1] — tekst] 평행중첩 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P18_T1].content
   limit: do 120 znaków
   EN: Parallel Superposition Mode
   PL: Tryb Superpozycji Równoległej
496. [Samouczek i wskazówki [TutoMD05_P18_D1] — tekst] 평행중첩 모드 적용 시, 거울 던전을 최대 10층까지 도전할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P18_D1].content
   limit: do 120 znaków
   EN: Engage the Parallel Superposition Mode to extend the Mirror Dungeon up to 10 Floors.
   PL: Włączenie Trybu Superpozycji Równoległej pozwala kontynuować wyzwanie Lustrzanych Lochów aż do 10. piętra.
497. [Samouczek i wskazówki [TutoMD05_P18_D2] — tekst] 평행중첩 모드는 도전 또는 업적 달성을 위한 모드이며, 5층 클리어 기준으로 별도로 보상이 증가하지는 않으니 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P18_D2].content
   limit: do 180 znaków
   EN: Please note that Parallel Superposition Mode is solely for Achievements, and does not yield additional rewards on its own past Floor 5.
   PL: Tryb Superpozycji Równoległej przeznaczony jest do wyzwań oraz Osiągnięć i sam w sobie nie zwiększa nagród powyżej poziomu 5. piętra.
498. [Samouczek i wskazówki [TutoMD05_P19_D1] — tekst] 거울 던전 입장화면 또는 던전 진행도 창에서 평행중첩 모드 활성화 여부를 언제든지 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P19_D1].content
   limit: do 170 znaków
   EN: You can choose at any time to engage the Parallel Superposition Mode at the Mirror Dungeon entrance and the Dungeon Progress window.
   PL: Tryb Superpozycji Równoległej możesz w dowolnej chwili włączyć lub wyłączyć na ekranie wejścia lub w oknie postępu lochu.
499. [Samouczek i wskazówki [TutoMD05_P19_D2] — tekst] 단, 평행중첩 모드를 적용하기 위해서는 5층까지의 모든 테마팩을 하드 난이도로 클리어해야 합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P19_D2].content
   limit: do 200 znaków
   EN: However, in order to enter the Parallel Superposition Mode, you had to have finished every Floor Theme Pack up to Floor 5 of that run in Hard difficulty.
   PL: Aby wejść w Tryb Superpozycji Równoległej, musisz jednak ukończyć wszystkie Pakiety Tematyczne do 5. piętra włącznie na poziomie Hard.
500. [Samouczek i wskazówki [TutoMD05_P20_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 5층 클리어 시, 평행중첩 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P20_D1].content
   limit: do 200 znaków
   EN: Clear Floor 5 while the Parallel Superposition Mode is engaged, and a prompt will appear asking if you would like to enter the Parallel Superposition Mode.
   PL: Po ukończeniu 5. piętra przy aktywnym Trybie Superpozycji Równoległej pojawi się okno z pytaniem o przejście w ten tryb.
501. [Samouczek i wskazówki [TutoMD05_P20_D2] — tekst] 확인 선택 시, 평행중첩 모드가 적용되어 6층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P20_D2].content
   limit: do 120 znaków
   EN: Confirm to enter Parallel Superposition Mode and move up to Floor 6.
   PL: Potwierdź, aby aktywować Tryb Superpozycji Równoległej i wejść na 6. piętro.
502. [Samouczek i wskazówki [TutoMD05_P20_D3] — tekst] 5층 클리어 이후에는 실패 혹은 중도 포기하더라도 5층 클리어 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P20_D3].content
   limit: do 170 znaków
   EN: Please note that failing or exiting the Mirror Dungeon at any point past Floor 5 will still yield full Floor 5 Clear Rewards.
   PL: Pamiętaj, że po ukończeniu 5. piętra nawet porażka lub rezygnacja na dalszym etapie nadal zapewni pełne nagrody za 5. piętro.
503. [Samouczek i wskazówki [TutoMD05_P20_P1] — tekst] 25. 02. 27 (KST) 업데이트 추가
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD05_P20_P1].content
   limit: do 120 znaków
   EN: Added with the Feb 27th, 2025 (KST) Scheduled Update
   PL: Dodane w aktualizacji 27.02.2025 (KST)
504. [Samouczek i wskazówki [TutoMD06_P1_T1] — tekst] 영생의 거울
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P1_T1].content
   limit: do 120 znaków
   EN: Mirror of Immortality
   PL: Lustro Nieśmiertelności
505. [Samouczek i wskazówki [TutoMD06_P1_D1] — tekst] 시즌 6 거울 던전의 명칭은 영생의 거울입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P1_D1].content
   limit: do 120 znaków
   EN: Season 6's Mirror Dungeon is called 'Mirror of Immortality'.
   PL: Lustrzane Lochy Sezonu 6 noszą nazwę „Lustro Nieśmiertelności”.
506. [Samouczek i wskazówki [TutoMD06_P1_D2] — tekst] 문 또는 입장 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P1_D2].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Samouczek i wskazówki [TutoMD06_P2_T1] — tekst] 주간 추가 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_T1].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Samouczek i wskazówki [TutoMD06_P2_D1] — tekst] 거울 던전에서는 매주 3회의 주간 추가 보상 기회가 제공됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D1].content
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Samouczek i wskazówki [TutoMD06_P2_D2] — tekst] 보상 수령 시 주간 추가 보상 기회를 사용하면, 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D2].content
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Samouczek i wskazówki [TutoMD06_P2_D3] — tekst] 거울 던전 클리어 시 모든 테마팩을 Hard 난이도로 클리어하였다면 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있습니다. 획득 보상은 소모한 주간 추가 보상 기회에 비례합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D3].content
   limit: do 290 znaków
   EN: If you chose Hard Difficulty Theme Packs for every Floor before clearing the Mirror Dungeon run, you can consume 2 or more Weekly Bonuses at once, and will receive rewards proportional to the number of Weekly Bonuses used.
   PL: Jeśli przed ukończeniem Lustrzanych Lochów wszystkie Pakiety Tematyczne zaliczono na poziomie Hard, możesz zużyć naraz 2 lub więcej szans Cotygodniowej Premii i odebrać proporcjonalne nagrody.
511. [Samouczek i wskazówki [TutoMD06_P2_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 하나씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D4].content
   limit: do 150 znaków
   EN: However, it is more enkephalin-efficient to use 1 Weekly Bonus at a time rather than to use them all at once.
   PL: Najwyższą wydajność nagród względem zużytej Enkefaliny daje jednak wykorzystywanie Cotygodniowej Premii pojedynczo.
512. [Samouczek i wskazówki [TutoMD06_P2_T2] — tekst] 별빛
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_T2].content
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
513. [Samouczek i wskazówki [TutoMD06_P2_D5] — tekst] 이번 영생의 거울에서는 별의 가호, 관측, 소원 빌기 등 별빛을 사용하여 던전 진행에 도움이 될 수 있는 기능들이 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D5].content
   limit: do 240 znaków
   EN: Mirror of Immortality adds various options and avenues to spend Starlight to help you through the dungeon, including but not limited to Grace of Stars, Observations, and Wishmaking.
   PL: W Lustrze Nieśmiertelności dostępne są pomocne funkcje wykorzystujące Gwiezdny Blask, takie jak Błogosławieństwo Gwiazd, Obserwacja czy Życzenie Gwiazd.
514. [Samouczek i wskazówki [TutoMD06_P2_D6] — tekst] 별빛은 도달한 층이 높을수록, Hard 난이도를 더 많이 클리어할수록 획득량이 증가합니다. 또는 거울굴절철도 테마팩을 클리어하였거나 전투 보상 카드에서 별빛을 많이 선택했다면 더욱 많은 별빛을 모을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D6].content
   limit: do 330 znaków
   EN: The amount of Starlight gained is proportional to the number of Floors reached and the number of Hard difficulty Packs cleared. You can also gain additional Starlight by clearing Refraction Railway Theme Packs or selecting Starlight Encounter Reward Cards.
   PL: Ilość zdobywanego Gwiezdnego Blasku rośnie wraz z osiągniętym piętrem oraz liczbą ukończonych pakietów Hard. Dodatkowy Gwiezdny Blask zdobędziesz też za Pakiety Tematyczne Kolei Załamania i Karty Nagród za Walkę.
515. [Samouczek i wskazówki [TutoMD06_P2_D7] — tekst] 이외에도 새롭게 출시된 3성, E.G.O를 특정 기간 동안 추출에서 획득하였을 때, 매우 많은 양의 별빛을 얻을 수 있습니다.\n※ 자판기를 통해 획득하였을 때는 별빛이 제공되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D7].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can also gain a large amount of Starlight by Extracting a newly released 3★ Identity or E.G.O within a certain timeframe.\n※ Please note that you cannot gain Starlight by obtaining them via the Dispenser.
   PL: Bardzo dużą ilość Gwiezdnego Blasku otrzymasz również za wylosowanie w Ekstrakcji nowo wydanej Tożsamości 3★ lub E.G.O w określonym przedziale czasu.\n※ Zakup w Automacie nie zapewnia Gwiezdnego Blasku.
516. [Samouczek i wskazówki [TutoMD06_P2_D8] — tekst] 추출로 획득한 별빛은 현재 진행 중인 거울 던전에도 즉시 적용되어 언제든지 사용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P2_D8].content
   limit: do 140 znaków
   EN: Starlight obtained from Extraction are immediately made usable for in-progress Mirror Dungeons as well.
   PL: Gwiezdny Blask zdobyty z Ekstrakcji jest natychmiast uwzględniany także w trwającej wyprawie Lustrzanych Lochów.
517. [Samouczek i wskazówki [TutoMD06_P3_T1] — tekst] 수감자
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_T1].content
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Samouczek i wskazówki [TutoMD06_P3_D1] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_D1].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Samouczek i wskazówki [TutoMD06_P3_T2] — tekst] 테마팩 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_T2].content
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Samouczek i wskazówki [TutoMD06_P3_D2] — tekst] 거울 던전에 등장하는 테마팩을 확인할 수 있습니다.\n거울 던전 진행 중 선택한 테마팩에 대한 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_D2].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the list of Theme Packs that appear in the Mirror Dungeon.\nSelected Theme Pack records will be collected here.
   PL: Tutaj przejrzysz Pakiety Tematyczne występujące w Lustrzanych Lochach.\nZbierane są tu wpisy o wybranych podczas wypraw pakietach.
521. [Samouczek i wskazówki [TutoMD06_P3_T3] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_T3].content
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [Samouczek i wskazówki [TutoMD06_P3_D3] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다.\n거울 던전 진행 중에 획득한 E.G.O 기프트의 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P3_D3].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the list of E.G.O Gifts that appear in the Mirror Dungeon.\nObtaining an E.G.O Gift in the Mirror Dungeon will add an entry to your E.G.O Gift Compendium.
   PL: Tutaj przejrzysz Dary E.G.O występujące w Lustrzanych Lochach.\nZdobycie Daru E.G.O podczas wyprawy dodaje jego wpis do Kompendium.
523. [Samouczek i wskazówki [TutoMD06_P4_T1] — tekst] 편성
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P4_T1].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Samouczek i wskazówki [TutoMD06_P4_D1] — tekst] 전투에 참여할 인격을 선택하여 편성합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P4_D1].content
   limit: do 120 znaków
   EN: Select Identities to participate in battle.
   PL: Wybierz i ustaw Tożsamości, które wezmą udział w walce.
525. [Samouczek i wskazówki [TutoMD06_P4_D2] — tekst] Easy 난이도에서는 인격 레벨이 55로 적용되고, Hard 난이도에서는 보유한 인격의 레벨에 맞추어 최대 55까지 적용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P4_D2].content
   limit: do 210 znaków
   EN: In Mirror Dungeon Easy, all Identity Levels will be fixed to 55. In Mirror Dungeon Hard, your current Identity Levels will be reflected instead, up to Level 55.
   PL: Na poziomie Easy poziom Tożsamości wynosi 55, natomiast na poziomie Hard obowiązuje aktualny poziom posiadanych Tożsamości (maks. 55).
526. [Samouczek i wskazówki [TutoMD06_P4_D3] — tekst] 단, 인격의 동기화 단계와 E.G.O의 환상 해석 단계는 별도로 보정되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P4_D3].content
   limit: do 130 znaków
   EN: Please note that, however, Identity Uptie Tiers and E.G.O Threadspinning Tiers will not be affected.
   PL: Stopień Synchronizacji Tożsamości oraz stopień Splotu Nici E.G.O nie podlegają jednak korekcie.
527. [Samouczek i wskazówki [TutoMD06_P5_T1] — tekst] 별빛 보너스
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_T1].content
   limit: do 120 znaków
   EN: Starlight Bonus
   PL: Premia Gwiezdnego Blasku
528. [Samouczek i wskazówki [TutoMD06_P5_D1] — tekst] 거울 던전 수감자 편성 창에서는 각 인격의 별빛 보너스 게이지를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_D1].content
   limit: do 130 znaków
   EN: In the Mirror Dungeon Sinner Team loadout menu, you can view each Identity's Starlight Bonus bars.
   PL: W oknie składu Grzeszników Lustrzanych Lochów sprawdzisz pasek Premii Gwiezdnego Blasku każdej Tożsamości.
529. [Samouczek i wskazówki [TutoMD06_P5_D2] — tekst] 현재 선택한 편성을 기준으로, 각 인격의 별빛 보너스 게이지로부터 얻을 수 있는 별빛의 총합이 우하단의 확인 버튼 위에 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_D2].content
   limit: do 220 znaków
   EN: The sum of obtainable Starlight from each Identity's Starlight Bonuses in your current Team can be viewed here, at the bottom right corner, above the Confirmation button.
   PL: Łączna suma Gwiezdnego Blasku możliwa do uzyskania z pasków Premii Gwiezdnego Blasku bieżącego składu widnieje w prawym dolnym rogu nad przyciskiem potwierdzenia.
530. [Samouczek i wskazówki [TutoMD06_P5_D3] — tekst] 별빛 보너스를 통해 획득하는 별빛은 이후에 설명할 별의 가호를 고를 때 사용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_D3].content
   limit: do 120 znaków
   EN: Starlight, which are obtained via Starlight Bonuses, are used to activate Grace of Stars.
   PL: Gwiezdny Blask uzyskany z Premii Gwiezdnego Blasku służy do wyboru Błogosławieństw Gwiazd.
531. [Samouczek i wskazówki [TutoMD06_P5_D4] — tekst] 이후 거울 던전 클리어 시, 입장 시점에 편성한 인격의 별빛 보너스는 0으로 초기화됩니다. 대신 편성하지 않은 모든 인격의 별빛 보너스는 1씩 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_D4].content
   limit: do 210 znaków
   EN: Upon clearing Mirror Dungeon, Starlight Bonuses for Identities in your current Mirror Dungeon Team resets to 0, and every other Identity gains 1 Starlight Bonus.
   PL: Po ukończeniu Lustrzanych Lochów Premia Gwiezdnego Blasku początkowego składu resetuje się do 0, a wszystkie niewystawione Tożsamości zyskują +1 Premii Gwiezdnego Blasku.
532. [Samouczek i wskazówki [TutoMD06_P5_D5] — tekst] 거울 던전 진행 과정에서 교체하여 등장한 인격은 별빛 게이지가 소모되거나 증가하지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P5_D5].content
   limit: do 170 znaków
   EN: Identities that have been swapped in or out during the Mirror Dungeon run will, however, neither spend nor gain Starlight Bonuses.
   PL: Tożsamości wprowadzone poprzez wymianę składu w trakcie wyprawy nie zużywają ani nie zyskują paska Gwiezdnego Blasku.
533. [Samouczek i wskazówki [TutoMD06_P6_T1] — tekst] 영생 별의 가호
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P6_T1].content
   limit: do 120 znaków
   EN: Grace of the Immortal Star
   PL: Błogosławieństwo Nieśmiertelnej Gwiazdy
534. [Samouczek i wskazówki [TutoMD06_P6_D1] — tekst] 편성을 통해 획득한 별빛 보너스를 지불하여 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P6_D1].content
   limit: do 120 znaków
   EN: Spend Starlight Bonuses obtained from your Team loadout to select Grace of Stars.
   PL: Wydaj Premię Gwiezdnego Blasku uzyskaną ze składu, aby wybrać Błogosławieństwa Gwiazd.
535. [Samouczek i wskazówki [TutoMD06_P6_D2] — tekst] 별빛 보너스 이외에도 따로 별빛을 보유하고 있다면, 추가로 지불하여 더 많은 별의 가호를 고르거나 선택한 별의 가호를 강화할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P6_D2].content
   limit: do 210 znaków
   EN: If you have more Starlight in additional to Starlight Bonuses, you can spend them as well to select more Grace of Stars or enhance your selected Grace of Stars.
   PL: Jeśli oprócz Premii Gwiezdnego Blasku posiadasz zgromadzony Gwiezdny Blask, możesz go dopłacić, aby wybrać więcej Błogosławieństw Gwiazd lub ulepszyć wybrane.
536. [Samouczek i wskazówki [TutoMD06_P6_D3] — tekst] 별의 가호를 선택하고 남은 별빛 보너스는 클리어 시 수령하거나 던전 진행 중 사용할 코스트로 전환할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P6_D3].content
   limit: do 170 znaków
   EN: Remaining Starlight Bonus after selecting Graces of Stars will be converted to 'Cost' to be used during your Mirror Dungeon run.
   PL: Premię Gwiezdnego Blasku pozostałą po wyborze Błogosławieństw Gwiazd odbierzesz przy ukończeniu lub zamienisz na Koszt dostępny podczas wyprawy.
537. [Samouczek i wskazówki [TutoMD06_P6_D4] — tekst] ※ 보유 별빛은 코스트로 전환되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P6_D4].content
   limit: do 120 znaków
   EN: ※ Owned Starlight are not converted into Costs.
   PL: ※ Posiadany Gwiezdny Blask nie zamienia się w Koszt.
538. [Samouczek i wskazówki [TutoMD06_P7_T1] — tekst] 시작 E.G.O 기프트 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P7_T1].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Samouczek i wskazówki [TutoMD06_P7_D1] — tekst] 거울 던전 입장 시, E.G.O 기프트의 키워드별 항목이 제시됩니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P7_D1].content
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Samouczek i wskazówki [TutoMD06_P7_D2] — tekst] 각 키워드별 항목의 등장 E.G.O 기프트는 고정이며, 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P7_D2].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Samouczek i wskazówki [TutoMD06_P7_D3] — tekst] 이 단계에서 선택한 키워드에 해당하는 E.G.O 기프트가 던전 진행 중에 더욱 자주 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P7_D3].content
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Samouczek i wskazówki [TutoMD06_P8_T1] — tekst] 테마팩 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_T1].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Samouczek i wskazówki [TutoMD06_P8_D1] — tekst] 층 진입 시, 이번 층에서 헤쳐나갈 테마를 제시된 목록 중에서 선택할 수 있습니다. 선택하고자 하는 테마팩을 아래로 드래그하여 고를 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D1].content
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Samouczek i wskazówki [TutoMD06_P8_D2] — tekst] 각각의 테마팩 우상단 버튼을 통해 해당 팩에서 등장할 수 있는 보스와 전투 보상으로 얻을 수 있는 E.G.O 기프트를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D2].content
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Samouczek i wskazówki [TutoMD06_P8_D3] — tekst] 테마팩 하단에는 해당 테마팩의 보스 클리어 시 선택 가능한 E.G.O 기프트의 목록이 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D3].content
   limit: do 180 znaków
   EN: At the bottom of the Theme Packs, you can view the list of E.G.O Gifts that you can choose from after defeating the boss of this Theme Pack.
   PL: U dołu Pakietu Tematycznego widnieje lista Darów E.G.O możliwych do wyboru po pokonaniu bossa tego pakietu.
546. [Samouczek i wskazówki [TutoMD06_P8_T2] — tekst] 테마팩 난이도 변경
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_T2].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Samouczek i wskazówki [TutoMD06_P8_D4] — tekst] 영생의 거울에서는 테마팩 선택 단계에서 원하는 난이도를 선택하여 입장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D4].content
   limit: do 150 znaków
   EN: In Mirror of Immortality, you can select the difficulty of the upcoming floor in the Theme Pack selection phase.
   PL: W Lustrze Nieśmiertelności na etapie wyboru Pakietu Tematycznego wybierasz poziom trudności nadchodzącego piętra.
548. [Samouczek i wskazówki [TutoMD06_P8_D5] — tekst] 단, Hard 난이도를 선택하여 입장하면 이후에는 난이도를 변경할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D5].content
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Samouczek i wskazówki [TutoMD06_P8_T3] — tekst] Hard 난이도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_T3].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Samouczek i wskazówki [TutoMD06_P8_D6] — tekst] Hard 난이도 테마팩에서는 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 3개에서 4개로 증가합니다. 또한 해당 목록에 있는 E.G.O 기프트를 2개 고를 수 있는 대신, 추가되는 고난도 2개가 선택됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D6].content
   limit: do 280 znaków
   EN: In Hard Theme Packs, you will be able to choose 4 instead of 3 E.G.O Gifts upon clearing the Floor Boss. Also, while you can pick two E.G.O Gifts from the said pool, you will also be selecting two Mounting Trials.
   PL: W Pakietach Tematycznych Hard po pokonaniu bossa piętra lista proponowanych Darów E.G.O rośnie z 3 do 4. Możesz wybrać z niej 2 Dary E.G.O, lecz nałożone zostaną także 2 Próby.
551. [Samouczek i wskazówki [TutoMD06_P8_D7] — tekst] Hard 난이도에서는 특별한 상점이 등장할 수 있으며, 특정 E.G.O 기프트는 Hard 난이도에서만 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P8_D7].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Hard Difficulty, you might come across certain special Shops.\nAlso, certain E.G.O Gifts are exclusive to the Hard Difficulty.
   PL: Na poziomie Hard może pojawić się Wzmocniony Sklep,\na niektóre Dary E.G.O dostępne są wyłącznie na poziomie Hard.
552. [Samouczek i wskazówki [TutoMD06_P9_T1] — tekst] 테마팩 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P9_T1].content
   limit: do 120 znaków
   EN: Theme Pack Observation(Search)
   PL: Obserwacja Pakietów Tematycznych
553. [Samouczek i wskazówki [TutoMD06_P9_D1] — tekst] 테마팩 관측은 별빛을 소모하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 찾는 신규 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P9_D1].content
   limit: do 240 znaków
   EN: By using the new addition Theme Pack Observation, or "Pack Search", you can choose specific Theme Packs from the list of available Packs in the current Floor and Difficulty combination.
   PL: Obserwacja Pakietów Tematycznych to nowa funkcja pozwalająca za Gwiezdny Blask wyszukać wybrany Pakiet Tematyczny dostępny na bieżącym piętrze i poziomie trudności.
554. [Samouczek i wskazówki [TutoMD06_P9_D2] — tekst] 테마팩 관측 버튼을 선택하여 활성화하면 테마팩의 우상단 버튼이 새로고침 모양으로 변경되며, 이를 선택하면 테마팩 관측 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P9_D2].content
   limit: do 230 znaków
   EN: Selecting the "Pack Search" button will change the top right corner buttons of each Theme Packs to Refresh icons. Select those icons to enter the Theme Pack Observation window.
   PL: Po włączeniu przycisku Obserwacji Pakietów Tematycznych ikona w prawym górnym rogu pakietów zmieni się w symbol odświeżenia — kliknij go, aby otworzyć okno Obserwacji.
555. [Samouczek i wskazówki [TutoMD06_P9_D3] — tekst] 별빛을 사용하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 선택하여 등장시킬 수 있습니다. 아직 열람하지 못한 테마팩의 경우에는 별빛을 추가로 소모합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P9_D3].content
   limit: do 210 znaków
   EN: Spend Starlight to select an available Theme Pack in the current Floor & Difficulty combination. Previously unobserved Theme Packs spend more Starlight to select.
   PL: Wydaj Gwiezdny Blask, aby wywołać wybrany Pakiet Tematyczny dostępny na bieżącym piętrze i trudności. Pakiety jeszcze nieodkryte wymagają dodatkowego Gwiezdnego Blasku.
556. [Samouczek i wskazówki [TutoMD06_P9_D4] — tekst] 단, 던전 진행 과정에서 테마팩 관측 기능을 사용할수록 필요한 별빛 비용이 증가하므로 이를 유의해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P9_D4].content
   limit: do 160 znaków
   EN: However, please be warned that the more you use the Theme Pack Observation function, the more Starlight it will cost to use.
   PL: Pamiętaj jednak, że każde kolejne użycie Obserwacji Pakietów Tematycznych w trakcie wyprawy zwiększa koszt w Gwiezdnym Blasku.
557. [Samouczek i wskazówki [TutoMD06_P10_T1] — tekst] 거울 던전 탐사
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P10_T1].content
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Samouczek i wskazówki [TutoMD06_P10_D1] — tekst] 거울 던전에 입장하게 되면 인카운터와 경로가 무작위로 생성됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P10_D1].content
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Samouczek i wskazówki [TutoMD06_P10_D2] — tekst] 현재 인카운터에서 연결된 인카운터을 선택해 진행하며, 각 인카운터에서는 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P10_D2].content
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Samouczek i wskazówki [TutoMD06_P10_T2] — tekst] 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P10_T2].content
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Samouczek i wskazówki [TutoMD06_P10_D3] — tekst] 거울 던전 진행 과정에서 코스트를 획득할 수 있습니다. 코스트를 지불하여 상점의 기능을 이용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P10_D3].content
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Samouczek i wskazówki [TutoMD06_P11_T1] — tekst] E.G.O 기프트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_T1].content
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Samouczek i wskazówki [TutoMD06_P11_D1] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_D1].content
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Samouczek i wskazówki [TutoMD06_P11_T2] — tekst] 스테이지 유효 속성과 획득 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_T2].content
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Samouczek i wskazówki [TutoMD06_P11_D2] — tekst] 거울 던전의 전투 인카운터에는 해당 전투에서 유효한 속성과 해당 전투를 클리어 시 획득할 수 있는 코스트가 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_D2].content
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Samouczek i wskazówki [TutoMD06_P11_T3] — tekst] 수감자 현황
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_T3].content
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Samouczek i wskazówki [TutoMD06_P11_D3] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_D3].content
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Samouczek i wskazówki [TutoMD06_P11_T4] — tekst] 적용 효과 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_T4].content
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Samouczek i wskazówki [TutoMD06_P11_D4] — tekst] 던전을 진행하는 동안 선택한 고난, 별빛 보너스, 선택지 효과를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P11_D4].content
   limit: do 120 znaków
   EN: View your Mounting Trials, Starlight Bonus, and Choice Event Effects here.
   PL: Sprawdzisz tu wybrane podczas wyprawy Próby, Premię Gwiezdnego Blasku oraz efekty z wydarzeń.
570. [Samouczek i wskazówki [TutoMD06_P12_T1] — tekst] 상점
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P12_T1].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Samouczek i wskazówki [TutoMD06_P12_D1] — tekst] 테마팩 보스 전투 직전에는 상점이 배치되어 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P12_D1].content
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Samouczek i wskazówki [TutoMD06_P12_D2] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 수감자 회복과 부활, 편성 교체, 인격 스킬 교체를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P12_D2].content
   limit: do 200 znaków
   EN: At Shops, you can spend your 'Cost' to purchase E.G.O Gifts, heal or revive Sinners, deploy/swap out additional Identities, or replace Identity Skills.
   PL: W Sklepie wydasz Koszt na zakup Darów E.G.O, leczenie i wskrzeszanie Grzeszników, zmianę składu lub wymianę umiejętności Tożsamości.
573. [Samouczek i wskazówki [TutoMD06_P12_D3] — tekst] 또한 E.G.O 기프트를 상점에서 판매하여 코스트를 획득하거나, E.G.O 기프트를 합성하여 더욱 유용한 E.G.O 기프트를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P12_D3].content
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Samouczek i wskazówki [TutoMD06_P12_D4] — tekst] Hard 난이도로 진행 시, 특별한 상점이 등장할 수 있습니다. 거울 던전 진행 중에 누적 소모한 코스트가 많을수록 특별한 상점이 등장할 확률이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P12_D4].content
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Samouczek i wskazówki [TutoMD06_P13_T1] — tekst] 합성 - 소원 빌기
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P13_T1].content
   limit: do 120 znaków
   EN: Fusion - Wishmaking
   PL: Synteza — Życzenie Gwiazd
576. [Samouczek i wskazówki [TutoMD06_P13_D1] — tekst] 소원 빌기는 새롭게 등장한 기능으로, 이를 사용하면 별빛을 추가로 소모하여 E.G.O 기프트 합성 확률을 증가시킬 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P13_D1].content
   limit: do 140 znaków
   EN: Wishmaking is a new option; spend additional Starlight to improve the E.G.O Gift Fusion success rate.
   PL: Życzenie Gwiazd to nowa funkcja pozwalająca wydać dodatkowy Gwiezdny Blask, aby zwiększyć szansę powodzenia Syntezy Darów E.G.O.
577. [Samouczek i wskazówki [TutoMD06_P13_D2] — tekst] 소원 빌기는 사용 횟수와 관계 없이 비용이 고정됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P13_D2].content
   limit: do 120 znaków
   EN: The cost of Wishmaking remains the same no matter how many times it is used.
   PL: Koszt Życzenia Gwiazd jest stały niezależnie od liczby użyć.
578. [Samouczek i wskazówki [TutoMD06_P14_T1] — tekst] 전투 보상 카드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P14_T1].content
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Samouczek i wskazówki [TutoMD06_P14_D1] — tekst] 전투에서 승리하면 전투 난이도에 따라 일정 확률로 전투 보상 카드가 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P14_D1].content
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Samouczek i wskazówki [TutoMD06_P14_D2] — tekst] 전투 보상 카드를 통해 코스트, 별빛, E.G.O 기프트, E.G.O 자원을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P14_D2].content
   limit: do 160 znaków
   EN: You can obtain various resources such as Cost, Starlight, E.G.O Gifts, or E.G.O Resources from the Encounter Reward Cards.
   PL: Z Kart Nagród za Walkę zdobędziesz Koszt, Gwiezdny Blask, Dary E.G.O lub zasoby E.G.O.
581. [Samouczek i wskazówki [TutoMD06_P15_T1] — tekst] E.G.O 기프트와 추가되는 고난
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P15_T1].content
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Samouczek i wskazówki [TutoMD06_P15_D1] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 고난 효과를 선택하여 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P15_D1].content
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Samouczek i wskazówki [TutoMD06_P15_D2] — tekst] 층을 클리어할 때마다 고난 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P15_D2].content
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Samouczek i wskazówki [TutoMD06_P15_D3] — tekst] Hard 난이도로 진행 시, E.G.O 기프트를 2개 선택할 수 있습니다. 대신 고난 효과도 2개를 선택하게 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P15_D3].content
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Samouczek i wskazówki [TutoMD06_P16_T1] — tekst] 거울 던전 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P16_T1].content
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Samouczek i wskazówki [TutoMD06_P16_D1] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P16_D1].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Samouczek i wskazówki [TutoMD06_P16_D2] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P16_D2].content
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Samouczek i wskazówki [TutoMD06_P16_D3] — tekst] 모든 테마팩을 Hard 난이도로 클리어 시, 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P16_D3].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Samouczek i wskazówki [TutoMD06_P16_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P16_D4].content
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
590. [Samouczek i wskazówki [TutoMD06_P17_T1] — tekst] 거울 투영 / 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P17_T1].content
   limit: do 120 znaków
   EN: Mirror Projection / Achievements
   PL: Projekcja Lustra / Osiągnięcia
591. [Samouczek i wskazówki [TutoMD06_P17_D1] — tekst] 거울 던전 클리어하거나 업적 달성 시, 투영도가 증가합니다.\n\n투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P17_D1].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing a Mirror Dungeon run or completing an Achievement raises your Projection rate.\n\nYou can obtain various rewards by meeting Projection milestones.
   PL: Ukończenie Lustrzanych Lochów lub zdobycie Osiągnięcia zwiększa Stopień Projekcji.\n\nPo osiągnięciu kolejnych progów Stopnia Projekcji odbierzesz rozmaite nagrody.
592. [Samouczek i wskazówki [TutoMD06_P18_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P18_T1].content
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Samouczek i wskazówki [TutoMD06_P18_D1] — tekst] 다양한 업적을 통해 투영도을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P18_D1].content
   limit: do 120 znaków
   EN: Raise your Projection rate by completing various Achievements.
   PL: Zdobywaj Stopień Projekcji, wykonując różnorodne Osiągnięcia.
594. [Samouczek i wskazówki [TutoMD06_P18_D2] — tekst] ※ 클리어 관련 업적은 보상 수령 창에서 엔케팔린 모듈을 소모하여 클리어할 때 적용되므로, 이를 도전하시는 관리자님께서는 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P18_D2].content
   limit: do 280 znaków
   EN: ※ Achievements that require the player to 'clear' the Mirror Dungeon count only when the Enkephalin Modules have been consumed at the reward claim window. Please note this information before attempting to complete them.
   PL: ※ Osiągnięcia powiązane z ukończeniem zaliczane są dopiero po zużyciu Modułów Enkefaliny w oknie odbioru nagród — prosimy Kierowników o uwzględnienie tego podczas wyzwań.
595. [Samouczek i wskazówki [TutoMD06_P19_T1] — tekst] 투영도 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P19_T1].content
   limit: do 120 znaków
   EN: Projection Rewards
   PL: Nagrody Projekcji
596. [Samouczek i wskazówki [TutoMD06_P19_D1] — tekst] 투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P19_D1].content
   limit: do 120 znaków
   EN: You can obtain various rewards by meeting Projection rate milestones.
   PL: Po osiągnięciu określonych progów Stopnia Projekcji odbierzesz rozmaite nagrody.
597. [Samouczek i wskazówki [TutoMD06_P21_T1] — tekst] E.G.O 기프트 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P21_T1].content
   limit: do 120 znaków
   EN: E.G.O Gift Search
   PL: Obserwacja Darów E.G.O
598. [Samouczek i wskazówki [TutoMD06_P21_D1] — tekst] E.G.O 기프트 관측은 별빛을 소모하여 리스트에 있는 E.G.O 기프트를 추가로 획득하는 신규 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P21_D1].content
   limit: do 120 znaków
   EN: Use E.G.O Gift Search to select and obtain an E.G.O Gift from the list.
   PL: Obserwacja Darów E.G.O to nowa funkcja pozwalająca za Gwiezdny Blask dobrać dodatkowy Dar E.G.O z listy.
599. [Samouczek i wskazówki [TutoMD06_P21_D2] — tekst] E.G.O 기프트 관측 기능은 토글 방식으로 ON/OFF를 할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P21_D2].content
   limit: do 120 znaków
   EN: You can toggle ON/OFF the E.G.O Gift Search function
   PL: Funkcję Obserwacji Darów E.G.O możesz przełączać (WŁ./WYŁ.).
600. [Samouczek i wskazówki [TutoMD06_P21_D3] — tekst] 보유 중인 E.G.O 기프트는 선택하지 못하며, 선택한 E.G.O 기프트의 수에 따라 지불해야 하는 가격이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P21_D3].content
   limit: do 180 znaków
   EN: You cannot select an E.G.O Gift you already own, and the cost of selecting E.G.O Gifts grows more expensive the more E.G.O Gifts you select.
   PL: Nie możesz wybrać posiadanego już Daru E.G.O, a wraz z liczbą wybranych Darów E.G.O rośnie koszt do zapłaty.
601. [Samouczek i wskazówki [TutoMD06_P22_T1] — tekst] 인격 대여
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P22_T1].content
   limit: do 120 znaków
   EN: Identity Rental
   PL: Wypożyczenie Tożsamości
602. [Samouczek i wskazówki [TutoMD06_P22_D1] — tekst] 인격 대여는 성장 시킬 필요 없는 지정된 덱으로 거울 던전과 신규 인격을 체험해볼 수 있는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P22_D1].content
   limit: do 150 znaków
   EN: Through the Identity Rental system, you can experience the Mirror Dungeon with new Identities in a preset Team.
   PL: Wypożyczenie Tożsamości pozwala wypróbować Lustrzane Lochy oraz nowe Tożsamości przy użyciu gotowej talii niewymagającej rozwoju.
603. [Samouczek i wskazówki [TutoMD06_P22_D2] — tekst] 인격 대여는 대여 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P22_D2].content
   limit: do 120 znaków
   EN: Select the rental button to enter the Identity Rental menu.
   PL: Wejdziesz tam za pomocą przycisku wypożyczenia.
604. [Samouczek i wskazówki [TutoMD06_P23_T1] — tekst] 대여 편성
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P23_T1].content
   limit: do 120 znaków
   EN: Rental Team
   PL: Wypożyczony skład
605. [Samouczek i wskazówki [TutoMD06_P23_D1] — tekst] 대여 기간 중 1회 한정으로 편성을 대여하여 거울 던전을 플레이할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P23_D1].content
   limit: do 140 znaków
   EN: Each Rental Team can be rented to play through the Mirror Dungeon once over their respective rental periods.
   PL: W okresie wypożyczenia możesz jednorazowo wypożyczyć skład, aby rozegrać Lustrzane Lochy.
606. [Samouczek i wskazówki [TutoMD06_P23_D2] — tekst] 거울 던전 클리어 보상 수령 시 대여 횟수가 차감됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P23_D2].content
   limit: do 120 znaków
   EN: Claiming the Mirror Dungeon Clear Reward will consume your Rental chance.
   PL: Limit wypożyczenia zostaje zużyty w momencie odbioru nagród za ukończenie Lustrzanych Lochów.
607. [Samouczek i wskazówki [TutoMD06_P23_D3] — tekst] 대여 편성으로 평행 중첩 모드에 진입할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P23_D3].content
   limit: do 120 znaków
   EN: You cannot enter the Parallel Superposition mode with a Rental Team.
   PL: Wypożyczonym składem nie można wejść w Tryb Superpozycji Równoległej.
608. [Samouczek i wskazówki [TutoMD06_P24_D1] — tekst] 대여 편성은 정해진 인격과 E.G.O 스킬을 사용하며, 변경이 불가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P24_D1].content
   limit: do 120 znaków
   EN: Rental Teams use preset Identities and E.G.O, none of which can be changed.
   PL: Wypożyczony skład korzysta ze z góry ustalonych Tożsamości i E.G.O, których nie można zmienić.
609. [Samouczek i wskazówki [TutoMD06_P24_D2] — tekst] 대여 편성에 있는 인격은 최대 별빛 보너스를 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P24_D2].content
   limit: do 120 znaków
   EN: All Identities in the Rental Team receive maximum Starlight Bonuses.
   PL: Wszystkie Tożsamości w wypożyczonym składzie otrzymują maksymalną Premię Gwiezdnego Blasku.
610. [Samouczek i wskazówki [TutoMD06_P25_D1] — tekst] 대여 편성으로는 편성 변경이 불가 합니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P25_D1].content
   limit: do 120 znaków
   EN: Rental Teams' loadouts cannot be edited or altered.
   PL: Wypożyczonego składu nie można modyfikować.
611. [Samouczek i wskazówki [TutoMD06_P26_T1] — tekst] 대여 편성 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P26_T1].content
   limit: do 120 znaków
   EN: Rental Team Rewards
   PL: Nagrody wypożyczonego składu
612. [Samouczek i wskazówki [TutoMD06_P26_D1] — tekst] 대여 편성으로 별빛과 이벤트 재화를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P26_D1].content
   limit: do 120 znaków
   EN: You can gain Starlight and Event currencies by using Rental Teams.
   PL: Grając wypożyczonym składem, zdobędziesz Gwiezdny Blask oraz waluty wydarzeń.
613. [Samouczek i wskazówki [TutoMD06_P26_D2] — tekst] 대여 편성으로는 주간 추가 보상 기회를 3회 중 1회만 소모 가능합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P26_D2].content
   limit: do 140 znaków
   EN: Only one out of three Weekly Bonuses can be consumed when clearing a Mirror Dungeon with a Rental Team.
   PL: Wypożyczony skład pozwala zużyć tylko 1 z 3 szans Cotygodniowej Premii.
614. [Samouczek i wskazówki [TutoMD06_P27_T1] — tekst] 평행중첩 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P27_T1].content
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Samouczek i wskazówki [TutoMD06_P27_D1] — tekst] 평행중첩 모드 적용 시, 거울 던전을 최대 10층까지 도전할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P27_D1].content
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Samouczek i wskazówki [TutoMD06_P27_D2] — tekst] 평행중첩 모드는 도전 또는 업적 달성을 위한 모드이며, 5층 클리어 기준으로 별도로 보상이 증가하지는 않으니 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P27_D2].content
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Samouczek i wskazówki [TutoMD06_P28_D1] — tekst] 거울 던전 입장화면 또는 던전 진행도 창에서 평행중첩 모드 활성화 여부를 언제든지 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P28_D1].content
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Samouczek i wskazówki [TutoMD06_P28_D2] — tekst] 단, 평행중첩 모드를 적용하기 위해서는 5층까지의 모든 테마팩을 하드 난이도로 클리어해야 합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P28_D2].content
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Samouczek i wskazówki [TutoMD06_P29_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 5층 클리어 시, 평행중첩 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P29_D1].content
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Samouczek i wskazówki [TutoMD06_P29_D2] — tekst] 확인 선택 시, 평행중첩 모드가 적용되어 6층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P29_D2].content
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Samouczek i wskazówki [TutoMD06_P29_D3] — tekst] 5층 클리어 이후에는 실패 혹은 중도 포기하더라도 5층 클리어 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P29_D3].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Samouczek i wskazówki [TutoMD06_P30_T1] — tekst] 주간 획득 가능 투영도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P30_T1].content
   limit: do 120 znaków
   EN: Weekly Projection Cap
   PL: Tygodniowy limit Stopnia Projekcji
623. [Samouczek i wskazówki [TutoMD06_P30_D1] — tekst] 거울 던전 클리어후 보상 수령 시 투영도를 획득 하실 수 있습니다. 획득 가능한 투영도는 거울 던전 진행 방식에 따라 달라집니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P30_D1].content
   limit: do 250 znaków
   EN: You can earn "Projection" rate by clearing the Mirror Dungeon and claiming its rewards. Obtainable Projection rate changes based on your progress and choices made during your Mirror Dungeon runs.
   PL: Po ukończeniu Lustrzanych Lochów i odbiorze nagród zdobywasz Stopień Projekcji. Jego ilość zależy od przebiegu wyprawy.
624. [Samouczek i wskazówki [TutoMD06_P30_D2] — tekst] 획득한 투영도로 거울 투영 레벨을 올릴 수 있으며, 레벨에 따라 각종 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P30_D2].content
   limit: do 150 znaków
   EN: Increasing your Projection rate raises your Mirror Projection Level. Various rewards await at each level milestone.
   PL: Zdobyty Stopień Projekcji podnosi poziom Projekcji Lustra, zapewniając rozmaite nagrody na kolejnych progach.
625. [Samouczek i wskazówki [TutoMD06_P30_D3] — tekst] 획득 가능한 투영도는 매주 한정되어 있으며, 매주 목요일 오전 6시(KST)를 기준으로 초기화 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P30_D3].content
   limit: do 150 znaków
   EN: There is a weekly cap to how much Projection rate can be earned. The weekly cap resets every Thursday 6AM (KST).
   PL: Tygodniowy limit Stopnia Projekcji jest ograniczony i resetuje się w każdy czwartek o 06:00 (KST).
626. [Samouczek i wskazówki [TutoMD06_P31_T1] — tekst] 평행중첩 EXTREME 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P31_T1].content
   limit: do 120 znaków
   EN: Parallel Superposition EXTREME
   PL: Tryb Superpozycji Równoległej EXTREME
627. [Samouczek i wskazówki [TutoMD06_P31_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 10층 클리어시, 평행중첩 EXTREME 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P31_D1].content
   limit: do 210 znaków
   EN: Clear Floor 10 while the Parallel Superposition Mode is engaged, and a prompt will appear asking if you would like to enter the Parallel Superposition EXTREME Mode.
   PL: Po ukończeniu 10. piętra w aktywnym Trybie Superpozycji Równoległej pojawi się okno z pytaniem o włączenie Trybu Superpozycji Równoległej EXTREME.
628. [Samouczek i wskazówki [TutoMD06_P31_D2] — tekst] 확인 선택 시, 평행중첩 EXTREME 모드가 적용되어 11층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P31_D2].content
   limit: do 120 znaków
   EN: Confirm to enter Parallel Superposition EXTREME Mode and move up to Floor 11.
   PL: Potwierdź, aby aktywować tryb EXTREME i wejść na 11. piętro.
629. [Samouczek i wskazówki [TutoMD06_P31_D3] — tekst] 실패 혹은 중도 포기하게 될 시 탐사 완료된 이전 층을 기준으로 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P31_D3].content
   limit: do 180 znaków
   EN: Please note that failing or exiting the Mirror Dungeon at any point will still yield Clear Rewards based on the Floor you cleared last.
   PL: W razie porażki lub rezygnacji po drodze otrzymasz nagrody odpowiadające ostatniemu ukończonemu piętru.
630. [Samouczek i wskazówki [TutoMD06_P32_T1] — tekst] 제약 설정
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P32_T1].content
   limit: do 120 znaków
   EN: Set Adversities
   PL: Ustawienia Utrudnień
631. [Samouczek i wskazówki [TutoMD06_P32_D1] — tekst] 11층부터는 제약을 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P32_D1].content
   limit: do 120 znaków
   EN: Starting from Floor 11, you can select "Adversities".
   PL: Od 11. piętra możesz wybierać Utrudnienia.
632. [Samouczek i wskazówki [TutoMD06_P32_D2] — tekst] 제약은 각층마다 최대 5개까지 설정할 수 있으며, 층을 클리어할 때마다 제약 점수와 제약 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P32_D2].content
   limit: do 150 znaków
   EN: You can select up to 5 Adversities per Floor; your Adversity Score & Adversity effects stack with every Floor clear.
   PL: Na każdym piętrze możesz ustawić do 5 Utrudnień; z każdym ukończonym piętrem punkty oraz efekty Utrudnień kumulują się.
633. [Samouczek i wskazówki [TutoMD06_P32_D3] — tekst] 제약을 선택하면 제약 점수에 따라 추가 별빛과 투영도를 획득할 수 있습니다. 단, 추가 보상의 경우 제약 설정을 진행했던 층을 클리어 해야만 결과에 합산됩니다. 또한 그 외 보상은 5층 클리어 기준으로 지급됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P32_D3].content
   limit: do 390 znaków
   EN: Select Adversities to gain bonus Starlight and Projection rate based on your Adversity Score. However, please note that Adversity bonus rewards for each floor can be obtained only by clearing the Floor on which the Adversities were selected. Also, any other reward will be based on Floor 5 Clear rewards.
   PL: Wybranie Utrudnień zapewnia dodatkowy Gwiezdny Blask i Stopień Projekcji zależnie od punktów Utrudnień. Premia za dane piętro naliczana jest jednak dopiero po ukończeniu piętra, na którym wybrano Utrudnienia, a pozostałe nagrody wypłacane są według 5. piętra.
634. [Samouczek i wskazówki [TutoMD06_P32_D4] — tekst] 선택한 제약이 많을수록 난이도는 높아지지만, 더욱 많은 양의 별빛과 투영도를 얻을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD06_P32_D4].content
   limit: do 150 znaków
   EN: Selecting more Adversities will increase the difficulty. However, it will reward more Starlight and Projection rate.
   PL: Im więcej Utrudnień wybierzesz, tym wyższy poziom trudności, ale też więcej zdobywanego Gwiezdnego Blasku i Stopnia Projekcji.
635. [Samouczek i wskazówki [TutoMD07_P1_T1] — tekst] 이름과 거미의 거울
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P1_T1].content
   limit: do 120 znaków
   EN: Mirror of Names and Spiders
   PL: Lustro Imion i Pająków
636. [Samouczek i wskazówki [TutoMD07_P1_D1] — tekst] 시즌 7 거울 던전의 명칭은 이름과 거미의 거울입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P1_D1].content
   limit: do 120 znaków
   EN: Season 7's Mirror Dungeon is called 'Mirror of Names and Spiders'.
   PL: Lustrzane Lochy Sezonu 7 noszą nazwę „Lustro Imion i Pająków”.
637. [Samouczek i wskazówki [TutoMD07_P1_D2] — tekst] 문 또는 입장 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P1_D2].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [Samouczek i wskazówki [TutoMD07_P2_T1] — tekst] 주간 추가 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_T1].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Samouczek i wskazówki [TutoMD07_P2_D1] — tekst] 거울 던전에서는 매주 3회의 주간 추가 보상 기회가 제공됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D1].content
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Samouczek i wskazówki [TutoMD07_P2_D2] — tekst] 보상 수령 시 주간 추가 보상 기회를 사용하면, 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D2].content
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Samouczek i wskazówki [TutoMD07_P2_D3] — tekst] 거울 던전 클리어 시 모든 테마팩을 Hard 난이도로 클리어하였다면 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있습니다. 획득 보상은 소모한 주간 추가 보상 기회에 비례합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D3].content
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Samouczek i wskazówki [TutoMD07_P2_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 하나씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D4].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
643. [Samouczek i wskazówki [TutoMD07_P2_T2] — tekst] 별빛
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_T2].content
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Samouczek i wskazówki [TutoMD07_P2_D5] — tekst] 이름과 거미의 거울에서는 별의 가호, 관측, 소원 빌기 등 별빛을 사용하여 던전 진행에 도움이 될 수 있는 기능들이 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D5].content
   limit: do 240 znaków
   EN: Mirror of Names and Spiders has various options and avenues to spend Starlight to help you through the dungeon, including but not limited to Grace of Stars, Observations, and Wishmaking.
   PL: W Lustrze Imion i Pająków dostępne są pomocne funkcje wykorzystujące Gwiezdny Blask, takie jak Błogosławieństwo Gwiazd, Obserwacja czy Życzenie Gwiazd.
645. [Samouczek i wskazówki [TutoMD07_P2_D6] — tekst] 별빛은 도달한 층이 높을수록, Hard 난이도를 더 많이 클리어할수록 획득량이 증가합니다. 또는 거울굴절철도 테마팩을 클리어하였거나 전투 보상 카드에서 별빛을 많이 선택했다면 더욱 많은 별빛을 모을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D6].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Samouczek i wskazówki [TutoMD07_P2_D7] — tekst] 이외에도 신규 3성, E.G.O가 추출에서 새롭게 등장하여 이를 획득하였을 때, 매우 많은 양의 별빛을 얻을 수 있습니다.\n※ 자판기를 통해 획득하였을 때는 별빛이 제공되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D7].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can also gain a large amount of Starlight by Extracting a newly released 3★ Identity or E.G.O within a certain timeframe.\n※ Please note that you cannot gain Starlight by obtaining them via the Dispenser.
   PL: Bardzo dużą ilość Gwiezdnego Blasku otrzymasz też za wylosowanie w Ekstrakcji nowej Tożsamości 3★ lub E.G.O.\n※ Zakup w Automacie nie zapewnia Gwiezdnego Blasku.
647. [Samouczek i wskazówki [TutoMD07_P2_D8] — tekst] 추출로 획득한 별빛은 현재 진행 중인 거울 던전에도 즉시 적용되어 언제든지 사용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P2_D8].content
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Samouczek i wskazówki [TutoMD07_P3_T1] — tekst] 수감자
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_T1].content
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Samouczek i wskazówki [TutoMD07_P3_D1] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_D1].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Samouczek i wskazówki [TutoMD07_P3_T2] — tekst] 테마팩 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_T2].content
   (powtórzenie elementu 358 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Samouczek i wskazówki [TutoMD07_P3_D2] — tekst] 거울 던전에 등장하는 테마팩을 확인할 수 있습니다.\n거울 던전 진행 중 선택한 테마팩에 대한 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_D2].content
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
652. [Samouczek i wskazówki [TutoMD07_P3_T3] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_T3].content
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Samouczek i wskazówki [TutoMD07_P3_D3] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다.\n거울 던전 진행 중에 획득한 E.G.O 기프트의 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P3_D3].content
   (powtórzenie elementu 522 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Samouczek i wskazówki [TutoMD07_P4_T1] — tekst] 편성
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P4_T1].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Samouczek i wskazówki [TutoMD07_P4_D1] — tekst] 전투에 참여할 인격을 선택하여 편성합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P4_D1].content
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
656. [Samouczek i wskazówki [TutoMD07_P4_D2] — tekst] Normal 난이도에서는 인격 레벨이 60으로 적용되고, Hard 난이도에서는 보유한 인격의 레벨에 맞추어 최대 60까지 적용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P4_D2].content
   limit: do 210 znaków
   EN: In Mirror Dungeon Normal, all Identity Levels will be fixed to 60. In Mirror Dungeon Hard, your current Identity Levels will be reflected instead, up to Level 60.
   PL: Na poziomie Normal poziom Tożsamości wynosi 60, a na poziomie Hard obowiązuje aktualny poziom posiadanych Tożsamości (maks. 60).
657. [Samouczek i wskazówki [TutoMD07_P4_D3] — tekst] 단, 인격의 동기화 단계와 E.G.O의 환상 해석 단계는 별도로 보정되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P4_D3].content
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Samouczek i wskazówki [TutoMD07_P5_T1] — tekst] 별빛 보너스
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_T1].content
   (powtórzenie elementu 527 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Samouczek i wskazówki [TutoMD07_P5_D1] — tekst] 거울 던전 수감자 편성 창에서는 각 인격의 별빛 보너스 게이지를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_D1].content
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
660. [Samouczek i wskazówki [TutoMD07_P5_D2] — tekst] 현재 선택한 편성을 기준으로, 각 인격의 별빛 보너스 게이지로부터 얻을 수 있는 별빛의 총합이 우하단의 확인 버튼 위에 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_D2].content
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Samouczek i wskazówki [TutoMD07_P5_D3] — tekst] 별빛 보너스를 통해 획득하는 별빛은 이후에 설명할 별의 가호를 고를 때 사용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_D3].content
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Samouczek i wskazówki [TutoMD07_P5_D4] — tekst] 이후 거울 던전 클리어 시, 입장 시점에 편성한 인격의 별빛 보너스는 0으로 초기화됩니다. 대신 편성하지 않은 모든 인격의 별빛 보너스는 1씩 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_D4].content
   (powtórzenie elementu 531 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Samouczek i wskazówki [TutoMD07_P5_D5] — tekst] 거울 던전 진행 과정에서 교체하여 등장한 인격은 별빛 게이지가 소모되거나 증가하지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P5_D5].content
   (powtórzenie elementu 532 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [Samouczek i wskazówki [TutoMD07_P6_T1] — tekst] 이름과 거미 별의 가호
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_T1].content
   limit: do 120 znaków
   EN: Grace of the Star of Names and Spiders
   PL: Błogosławieństwo Gwiazdy Imion i Pająków
665. [Samouczek i wskazówki [TutoMD07_P6_D1] — tekst] 편성을 통해 획득한 별빛 보너스를 지불하여 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_D1].content
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Samouczek i wskazówki [TutoMD07_P6_D2] — tekst] 별빛 보너스 이외에도 따로 별빛을 보유하고 있다면, 추가로 지불하여 더 많은 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_D2].content
   limit: do 160 znaków
   EN: If you have more Starlight in additional to Starlight Bonuses, you can spend them as well to select more Grace of Stars.
   PL: Jeśli oprócz Premii Gwiezdnego Blasku posiadasz dodatkowy Gwiezdny Blask, możesz go dopłacić, aby wybrać więcej Błogosławieństw Gwiazd.
667. [Samouczek i wskazówki [TutoMD07_P6_D3] — tekst] 해당 버튼으로 별의 가호를 더욱 편하게 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_D3].content
   limit: do 120 znaków
   EN: Use this button to select multiple Graces at once.
   PL: Ten przycisk pozwala wygodniej wybrać naraz wiele Błogosławieństw Gwiazd.
668. [Samouczek i wskazówki [TutoMD07_P6_D4] — tekst] 별의 가호를 선택하고 남은 별빛 보너스는 클리어 시 수령하거나 던전 진행 중 사용할 코스트로 전환할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_D4].content
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Samouczek i wskazówki [TutoMD07_P6_D5] — tekst] ※ 보유 별빛은 코스트로 전환되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P6_D5].content
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Samouczek i wskazówki [TutoMD07_P7_T1] — tekst] 시작 E.G.O 기프트 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P7_T1].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Samouczek i wskazówki [TutoMD07_P7_D1] — tekst] 거울 던전 입장 시, E.G.O 기프트의 키워드별 항목이 제시됩니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P7_D1].content
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Samouczek i wskazówki [TutoMD07_P7_D2] — tekst] 각 키워드별 항목의 등장 E.G.O 기프트는 고정이며, 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P7_D2].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Samouczek i wskazówki [TutoMD07_P7_D3] — tekst] 이 단계에서 선택한 키워드에 해당하는 E.G.O 기프트가 던전 진행 중에 더욱 자주 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P7_D3].content
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Samouczek i wskazówki [TutoMD07_P8_T1] — tekst] E.G.O 기프트 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P8_T1].content
   (powtórzenie elementu 597 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Samouczek i wskazówki [TutoMD07_P8_D1] — tekst] E.G.O 기프트 관측은 별빛을 소모하여 리스트에 있는 E.G.O 기프트를 추가로 획득하는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P8_D1].content
   limit: do 120 znaków
   EN: Use E.G.O Gift Search to select and obtain an E.G.O Gift from the list.
   PL: Obserwacja Darów E.G.O pozwala wydać Gwiezdny Blask, aby dobrać dodatkowy Dar E.G.O z listy.
676. [Samouczek i wskazówki [TutoMD07_P8_D2] — tekst] E.G.O 기프트 관측 기능은 토글 방식으로 ON/OFF를 할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P8_D2].content
   (powtórzenie elementu 599 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Samouczek i wskazówki [TutoMD07_P8_D3] — tekst] 보유 중인 E.G.O 기프트는 선택하지 못하며, 선택한 E.G.O 기프트의 수에 따라 지불해야 하는 가격이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P8_D3].content
   (powtórzenie elementu 600 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Samouczek i wskazówki [TutoMD07_P9_T1] — tekst] 테마팩 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_T1].content
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Samouczek i wskazówki [TutoMD07_P9_D1] — tekst] 층 진입 시, 이번 층에서 헤쳐나갈 테마를 제시된 목록 중에서 선택할 수 있습니다. 선택하고자 하는 테마팩을 아래로 드래그하여 고를 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D1].content
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Samouczek i wskazówki [TutoMD07_P9_D2] — tekst] 각각의 테마팩 우상단 버튼을 통해 해당 팩에서 등장할 수 있는 보스와 전투 보상으로 얻을 수 있는 E.G.O 기프트를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D2].content
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
681. [Samouczek i wskazówki [TutoMD07_P9_D3] — tekst] 테마팩 하단에는 해당 테마팩의 보스 클리어 시 선택 가능한 E.G.O 기프트의 목록이 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D3].content
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Samouczek i wskazówki [TutoMD07_P9_T2] — tekst] 테마팩 난이도 변경
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_T2].content
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Samouczek i wskazówki [TutoMD07_P9_D4] — tekst] 이름과 거미의 거울에서는 테마팩 선택 단계에서 원하는 난이도를 선택하여 입장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D4].content
   limit: do 160 znaków
   EN: In Mirror of Names and Spiders, you can select the difficulty of the upcoming floor in the Theme Pack selection phase.
   PL: W Lustrze Imion i Pająków poziom trudności nadchodzącego piętra wybierasz na etapie wyboru Pakietu Tematycznego.
684. [Samouczek i wskazówki [TutoMD07_P9_D5] — tekst] 단, Hard 난이도를 선택하여 입장하면 이후에는 난이도를 변경할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D5].content
   (powtórzenie elementu 454 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Samouczek i wskazówki [TutoMD07_P9_T3] — tekst] Hard 난이도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_T3].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Samouczek i wskazówki [TutoMD07_P9_D6] — tekst] Hard 난이도 테마팩에서는 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 3개에서 4개로 증가합니다. 또한 해당 목록에 있는 E.G.O 기프트를 2개 고를 수 있는 대신, 추가되는 고난도 2개가 선택됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D6].content
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Samouczek i wskazówki [TutoMD07_P9_D7] — tekst] Hard 난이도에서는 특별한 상점이 등장할 수 있으며, 특정 E.G.O 기프트는 Hard 난이도에서만 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P9_D7].content
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Samouczek i wskazówki [TutoMD07_P10_T1] — tekst] 테마팩 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P10_T1].content
   limit: do 120 znaków
   EN: Pack Search
   PL: Obserwacja Pakietów
689. [Samouczek i wskazówki [TutoMD07_P10_D1] — tekst] 테마팩 관측은 별빛을 소모하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 찾는 신규 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P10_D1].content
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Samouczek i wskazówki [TutoMD07_P10_D2] — tekst] 테마팩 관측 버튼을 선택하여 활성화하면 테마팩의 우상단 버튼이 새로고침 모양으로 변경되며, 이를 선택하면 테마팩 관측 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P10_D2].content
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Samouczek i wskazówki [TutoMD07_P10_D3] — tekst] 별빛을 사용하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 선택하여 등장시킬 수 있습니다. 아직 열람하지 못한 테마팩의 경우에는 별빛을 추가로 소모합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P10_D3].content
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Samouczek i wskazówki [TutoMD07_P10_D4] — tekst] 단, 던전 진행 과정에서 테마팩 관측 기능을 사용할수록 필요한 별빛 비용이 증가하므로 이를 유의해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P10_D4].content
   limit: do 160 znaków
   EN: However, please be warned that the more you use the Theme Pack Search function, the more Starlight it will cost to use.
   PL: Pamiętaj jednak, że każde kolejne użycie Obserwacji Pakietów Tematycznych w trakcie wyprawy zwiększa koszt w Gwiezdnym Blasku.
693. [Samouczek i wskazówki [TutoMD07_P11_T1] — tekst] 거울 던전 탐사
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P11_T1].content
   (powtórzenie elementu 389 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Samouczek i wskazówki [TutoMD07_P11_D1] — tekst] 거울 던전에 입장하게 되면 인카운터와 경로가 무작위로 생성됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P11_D1].content
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Samouczek i wskazówki [TutoMD07_P11_D2] — tekst] 현재 인카운터에서 연결된 인카운터을 선택해 진행하며, 각 인카운터에서는 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P11_D2].content
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Samouczek i wskazówki [TutoMD07_P11_T2] — tekst] 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P11_T2].content
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Samouczek i wskazówki [TutoMD07_P11_D3] — tekst] 거울 던전 진행 과정에서 코스트를 획득할 수 있습니다. 코스트를 지불하여 상점의 기능을 이용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P11_D3].content
   (powtórzenie elementu 462 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Samouczek i wskazówki [TutoMD07_P12_T1] — tekst] 스테이지 유효 속성과 획득 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_T1].content
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Samouczek i wskazówki [TutoMD07_P12_D1] — tekst] 거울 던전의 전투 인카운터에는 해당 전투에서 유효한 속성과 해당 전투를 클리어 시 획득할 수 있는 코스트가 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_D1].content
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Samouczek i wskazówki [TutoMD07_P12_T2] — tekst] 수감자 현황
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_T2].content
   (powtórzenie elementu 398 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Samouczek i wskazówki [TutoMD07_P12_D2] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_D2].content
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Samouczek i wskazówki [TutoMD07_P12_T3] — tekst] E.G.O 기프트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_T3].content
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Samouczek i wskazówki [TutoMD07_P12_D3] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_D3].content
   (powtórzenie elementu 395 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Samouczek i wskazówki [TutoMD07_P12_T4] — tekst] 수감자 편성 확인
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_T4].content
   limit: do 120 znaków
   EN: Observe Team Loadout
   PL: Podgląd składu Grzeszników
705. [Samouczek i wskazówki [TutoMD07_P12_D4] — tekst] 현재 편성된 인격의 상세 정보를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_D4].content
   limit: do 120 znaków
   EN: You can view detailed information of the Identities in your loadout.
   PL: Sprawdzisz tu szczegółowe informacje o Tożsamościach w bieżącym składzie.
706. [Samouczek i wskazówki [TutoMD07_P12_T5] — tekst] 적용 효과 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_T5].content
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Samouczek i wskazówki [TutoMD07_P12_D5] — tekst] 던전을 진행하는 동안 선택한 고난, 별의 가호, 선택지 효과를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P12_D5].content
   limit: do 120 znaków
   EN: View your Mounting Trials, Grace of Stars, and Choice Event Effects here.
   PL: Sprawdzisz tu wybrane podczas wyprawy Próby, Błogosławieństwa Gwiazd oraz efekty z wydarzeń.
708. [Samouczek i wskazówki [TutoMD07_P13_T1] — tekst] 상점
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P13_T1].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Samouczek i wskazówki [TutoMD07_P13_D1] — tekst] 테마팩 보스 전투 직전에는 상점이 배치되어 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P13_D1].content
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Samouczek i wskazówki [TutoMD07_P13_D2] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 수감자 회복과 부활, 편성 교체, 인격 스킬 교체를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P13_D2].content
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Samouczek i wskazówki [TutoMD07_P13_D3] — tekst] 또한 E.G.O 기프트를 상점에서 판매하여 코스트를 획득하거나, E.G.O 기프트를 합성하여 더욱 유용한 E.G.O 기프트를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P13_D3].content
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Samouczek i wskazówki [TutoMD07_P13_D4] — tekst] Hard 난이도로 진행 시, 특별한 상점이 등장할 수 있습니다. 거울 던전 진행 중에 누적 소모한 코스트가 많을수록 특별한 상점이 등장할 확률이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P13_D4].content
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Samouczek i wskazówki [TutoMD07_P14_T1] — tekst] 조합식
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P14_T1].content
   limit: do 120 znaków
   EN: Fusion Recipes
   PL: Receptury Syntezy
714. [Samouczek i wskazówki [TutoMD07_P14_D1] — tekst] 특정 조합식이 필요한 기프트의 조합식을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P14_D1].content
   limit: do 120 znaków
   EN: Some E.G.O Gifts require specific recipes to fuse. View them here.
   PL: Sprawdzisz tu receptury Darów E.G.O wymagających określonych składników.
715. [Samouczek i wskazówki [TutoMD07_P14_D2] — tekst] 특정 테마팩에서만 획득할 수 있는 기프트를 재료로 필요하는 기프트도 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P14_D2].content
   limit: do 140 znaków
   EN: There are also E.G.O Gifts whose recipes require certain Theme Pack exclusive E.G.O Gifts as ingredients.
   PL: Niektóre Dary wymagają jako składników Darów dostępnych wyłącznie w określonych Pakietach Tematycznych.
716. [Samouczek i wskazówki [TutoMD07_P15_T1] — tekst] 합성 - 소원 빌기
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P15_T1].content
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Samouczek i wskazówki [TutoMD07_P15_D1] — tekst] 소원 빌기는 별빛을 추가로 소모하여 E.G.O 기프트 합성 확률을 증가시킬 수 있는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P15_D1].content
   limit: do 150 znaków
   EN: By using the Wishmaking function, you can spend additional Starlight to improve the E.G.O Gift Fusion success rate.
   PL: Życzenie Gwiazd pozwala wydać dodatkowy Gwiezdny Blask, aby zwiększyć szansę powodzenia Syntezy Darów E.G.O.
718. [Samouczek i wskazówki [TutoMD07_P15_D2] — tekst] 소원 빌기는 사용 횟수와 관계 없이 비용이 고정됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P15_D2].content
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Samouczek i wskazówki [TutoMD07_P16_T1] — tekst] 전투 보상 카드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P16_T1].content
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Samouczek i wskazówki [TutoMD07_P16_D1] — tekst] 전투에서 승리하면 전투 난이도에 따라 일정 확률로 전투 보상 카드가 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P16_D1].content
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Samouczek i wskazówki [TutoMD07_P16_D2] — tekst] 전투 보상 카드를 통해 코스트, 별빛, E.G.O 기프트, E.G.O 자원을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P16_D2].content
   (powtórzenie elementu 580 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Samouczek i wskazówki [TutoMD07_P17_T1] — tekst] E.G.O 기프트와 추가되는 고난
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P17_T1].content
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Samouczek i wskazówki [TutoMD07_P17_D1] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 고난 효과를 선택하여 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P17_D1].content
   (powtórzenie elementu 480 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Samouczek i wskazówki [TutoMD07_P17_D2] — tekst] 층을 클리어할 때마다 고난 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P17_D2].content
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [Samouczek i wskazówki [TutoMD07_P17_D3] — tekst] Hard 난이도로 진행 시, E.G.O 기프트를 2개 선택할 수 있습니다. 대신 고난 효과도 2개를 선택하게 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P17_D3].content
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
726. [Samouczek i wskazówki [TutoMD07_P18_T1] — tekst] 거울 던전 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P18_T1].content
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Samouczek i wskazówki [TutoMD07_P18_D1] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P18_D1].content
   (powtórzenie elementu 413 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Samouczek i wskazówki [TutoMD07_P18_D2] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P18_D2].content
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Samouczek i wskazówki [TutoMD07_P18_D3] — tekst] 모든 테마팩을 Hard 난이도로 클리어 시, 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P18_D3].content
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Samouczek i wskazówki [TutoMD07_P18_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P18_D4].content
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Samouczek i wskazówki [TutoMD07_P19_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P19_T1].content
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Samouczek i wskazówki [TutoMD07_P19_D1] — tekst] 업적은 특별한 도전 달성 시 투영도가 쌓이며, 이를 통해 다양한 보상을 획득할 수 있는 콘텐츠입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P19_D1].content
   limit: do 140 znaków
   EN: Achievements is a game content in which you beat challenges to gain Projection rate to earn various rewards.
   PL: Osiągnięcia to zawartość, w której realizujesz specjalne wyzwania, gromadzisz Stopień Projekcji i odbierasz rozmaite nagrody.
733. [Samouczek i wskazówki [TutoMD07_P20_T1] — tekst] 편성 대여
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P20_T1].content
   limit: do 120 znaków
   EN: Team Rental
   PL: Wypożyczenie składu
734. [Samouczek i wskazówki [TutoMD07_P20_D1] — tekst] 편성 대여는 성장 시킬 필요 없는 지정된 덱으로 거울 던전과 신규 인격을 체험해볼 수 있는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P20_D1].content
   limit: do 140 znaków
   EN: Through the Team Rental system, you can experience the Mirror Dungeon with new Identities in a preset Team.
   PL: Wypożyczenie składu pozwala wypróbować Lustrzane Lochy oraz nowe Tożsamości gotową talią niewymagającą rozwoju.
735. [Samouczek i wskazówki [TutoMD07_P20_D2] — tekst] 편성 대여는 대여 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P20_D2].content
   limit: do 120 znaków
   EN: Select the rental button to enter the Team Rental menu.
   PL: Wejdziesz tam za pomocą przycisku wypożyczenia.
736. [Samouczek i wskazówki [TutoMD07_P21_T1] — tekst] 편성 대여
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P21_T1].content
   (powtórzenie elementu 733 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Samouczek i wskazówki [TutoMD07_P21_D1] — tekst] 대여 기간 중 1회 한정으로 편성을 대여하여 거울 던전을 플레이할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P21_D1].content
   (powtórzenie elementu 605 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Samouczek i wskazówki [TutoMD07_P21_D2] — tekst] 거울 던전 클리어 보상 수령 시 대여 횟수가 차감됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P21_D2].content
   (powtórzenie elementu 606 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Samouczek i wskazówki [TutoMD07_P21_D3] — tekst] 편성 대여로 평행 중첩 모드에 진입할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P21_D3].content
   limit: do 120 znaków
   EN: You cannot enter the Parallel Superposition mode with a Rental Team.
   PL: Wypożyczonym składem nie można wejść w Tryb Superpozycji Równoległej.
740. [Samouczek i wskazówki [TutoMD07_P22_D1] — tekst] 편성 대여는 정해진 인격과 E.G.O 스킬을 사용하며, 변경이 불가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P22_D1].content
   limit: do 120 znaków
   EN: Rental Teams use preset Identities and E.G.O, none of which can be changed.
   PL: Wypożyczony skład korzysta ze z góry ustalonych Tożsamości i E.G.O, których nie można zmienić.
741. [Samouczek i wskazówki [TutoMD07_P22_D2] — tekst] 편성 대여에 있는 인격은 최대 별빛 보너스를 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P22_D2].content
   limit: do 120 znaków
   EN: All Identities in the Rental Team receive maximum Starlight Bonuses.
   PL: Wszystkie Tożsamości w wypożyczonym składzie otrzymują maksymalną Premię Gwiezdnego Blasku.
742. [Samouczek i wskazówki [TutoMD07_P23_D1] — tekst] 편성 대여로 입장했을 경우, 편성 변경이 불가 합니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P23_D1].content
   limit: do 120 znaków
   EN: You cannot change your loadout once you have entered with a Rental Team.
   PL: Po wejściu wypożyczonym składem nie można zmieniać drużyny.
743. [Samouczek i wskazówki [TutoMD07_P24_T1] — tekst] 편성 대여 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P24_T1].content
   limit: do 120 znaków
   EN: Team Rental Rewards
   PL: Nagrody wypożyczonego składu
744. [Samouczek i wskazówki [TutoMD07_P24_D1] — tekst] 편성 대여로 별빛과 이벤트 재화를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P24_D1].content
   limit: do 120 znaków
   EN: You can gain Starlight and Event currencies by using Rental Teams.
   PL: Grając wypożyczonym składem, zdobędziesz Gwiezdny Blask oraz waluty wydarzeń.
745. [Samouczek i wskazówki [TutoMD07_P24_D2] — tekst] 편성 대여로는 주간 보너스를 1회만 소모 가능합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P24_D2].content
   limit: do 120 znaków
   EN: Only one Weekly Bonus can be consumed when clearing a Mirror Dungeon with a Rental Team.
   PL: Wypożyczony skład pozwala zużyć tylko 1 Cotygodniową Premię.
746. [Samouczek i wskazówki [TutoMD07_P25_T1] — tekst] 평행중첩 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P25_T1].content
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Samouczek i wskazówki [TutoMD07_P25_D1] — tekst] 평행중첩 모드 적용 시, 거울 던전을 최대 10층까지 도전할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P25_D1].content
   (powtórzenie elementu 496 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Samouczek i wskazówki [TutoMD07_P25_D2] — tekst] 평행중첩 모드는 도전 또는 향후에 등장할 업적 달성을 위한 모드이며, 5층 클리어 기준으로 별도로 보상이 증가하지는 않으니 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P25_D2].content
   limit: do 210 znaków
   EN: Please note that Parallel Superposition Mode is solely for challenges and upcoming Achievements, and does not yield additional rewards on its own past Floor 5.
   PL: Tryb Superpozycji Równoległej służy do wyzwań oraz przyszłych Osiągnięć i sam w sobie nie zwiększa nagród powyżej poziomu 5. piętra.
749. [Samouczek i wskazówki [TutoMD07_P26_D1] — tekst] 거울 던전 입장화면 또는 던전 진행도 창에서 평행중첩 모드 활성화 여부를 언제든지 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P26_D1].content
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [Samouczek i wskazówki [TutoMD07_P26_D2] — tekst] 단, 평행중첩 모드를 적용하기 위해서는 5층까지의 모든 테마팩을 하드 난이도로 클리어해야 합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P26_D2].content
   (powtórzenie elementu 499 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Samouczek i wskazówki [TutoMD07_P27_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 5층 클리어 시, 평행중첩 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P27_D1].content
   (powtórzenie elementu 500 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Samouczek i wskazówki [TutoMD07_P27_D2] — tekst] 확인 선택 시, 평행중첩 모드가 적용되어 6층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P27_D2].content
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Samouczek i wskazówki [TutoMD07_P27_D3] — tekst] 5층 클리어 이후에는 실패 혹은 중도 포기하더라도 5층 클리어 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P27_D3].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Samouczek i wskazówki [TutoMD07_P28_T1] — tekst] 거울 투영 / 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P28_T1].content
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Samouczek i wskazówki [TutoMD07_P28_D1] — tekst] 업적 달성 및 거울 던전 클리어 시, 투영도가 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P28_D1].content
   limit: do 120 znaków
   EN: Completing an Achievement or clearing a Mirror Dungeon raises your Projection Rate.
   PL: Zdobycie Osiągnięcia lub ukończenie Lustrzanych Lochów zwiększa Stopień Projekcji.
756. [Samouczek i wskazówki [TutoMD07_P28_D2] — tekst] 투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P28_D2].content
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Samouczek i wskazówki [TutoMD07_P29_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P29_T1].content
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Samouczek i wskazówki [TutoMD07_P29_D1] — tekst] 다양한 업적을 통해 투영도을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P29_D1].content
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Samouczek i wskazówki [TutoMD07_P29_D2] — tekst] ※ 클리어 관련 업적은 보상 수령 창에서 엔케팔린 모듈을 소모하여 클리어할 때 적용되므로, 이를 도전하시는 관리자님께서는 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P29_D2].content
   (powtórzenie elementu 594 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Samouczek i wskazówki [TutoMD07_P30_T1] — tekst] 투영도 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P30_T1].content
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Samouczek i wskazówki [TutoMD07_P30_D1] — tekst] 투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P30_D1].content
   (powtórzenie elementu 596 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Samouczek i wskazówki [TutoMD07_P31_T1] — tekst] 주간 투영도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P31_T1].content
   limit: do 120 znaków
   EN: Weekly Projection
   PL: Tygodniowy Stopień Projekcji
763. [Samouczek i wskazówki [TutoMD07_P31_D1] — tekst] 거울 던전 클리어후 보상 수령 시 투영도를 획득 하실 수 있습니다. 획득 가능한 투영도는 거울 던전 진행 방식에 따라 달라집니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P31_D1].content
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Samouczek i wskazówki [TutoMD07_P31_D2] — tekst] 획득한 투영도로 이름과 거미의 거울 패스 레벨을 올릴 수 있으며, 레벨에 따라 각종 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P31_D2].content
   limit: do 190 znaków
   EN: Increasing your Projection rate raises your Mirror of Names and Spiders Pass Projection Level. Various rewards await at each level milestone.
   PL: Zdobyty Stopień Projekcji podnosi poziom Przepustki Lustra Imion i Pająków, zapewniając nagrody na kolejnych progach.
765. [Samouczek i wskazówki [TutoMD07_P31_D3] — tekst] 획득 가능한 경험치는 매주 한정되어 있으며, 매주 목요일 오전 6시(KST)를 기준으로 초기화 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P31_D3].content
   limit: do 150 znaków
   EN: There is a weekly cap to how much experience points can be earned. The weekly cap resets every Thursday 6AM (KST).
   PL: Tygodniowa ilość możliwych do zdobycia punktów jest ograniczona i resetuje się w każdy czwartek o 06:00 (KST).
766. [Samouczek i wskazówki [TutoMD07_P32_T1] — tekst] 평행중첩 EXTREME 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P32_T1].content
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Samouczek i wskazówki [TutoMD07_P32_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 10층 클리어시, 평행중첩 EXTREME 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P32_D1].content
   (powtórzenie elementu 627 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Samouczek i wskazówki [TutoMD07_P32_D2] — tekst] 확인 선택 시, 평행중첩 EXTREME 모드가 적용되어 11층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P32_D2].content
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Samouczek i wskazówki [TutoMD07_P32_D3] — tekst] 실패 혹은 중도 포기하게 될 시 탐사 완료된 이전 층을 기준으로 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P32_D3].content
   (powtórzenie elementu 629 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Samouczek i wskazówki [TutoMD07_P33_T1] — tekst] 제약 설정
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P33_T1].content
   (powtórzenie elementu 630 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Samouczek i wskazówki [TutoMD07_P33_D1] — tekst] 11층부터는 제약을 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P33_D1].content
   (powtórzenie elementu 631 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Samouczek i wskazówki [TutoMD07_P33_D2] — tekst] 제약은 각층마다 최대 5개까지 설정할 수 있으며,\n층을 클리어할 때마다 제약 점수와 제약 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P33_D2].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can select up to 5 Adversities per Floor; your Adversity Score & Adversity effects stack with every Floor clear.
   PL: Na każdym piętrze możesz ustawić do 5 Utrudnień;\nz każdym ukończonym piętrem punkty i efekty Utrudnień kumulują się.
773. [Samouczek i wskazówki [TutoMD07_P33_D3] — tekst] 제약을 선택하면 제약 점수에 따라 추가 별빛과 이름과 거미의 거울 패스 투영도를 획득할 수 있습니다. 단, 추가 보상의 경우 제약 설정을 진행했던 층을 클리어 해야만 결과에 합산됩니다. 또한 그 외 보상은 5층 클리어 기준으로 지급됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P33_D3].content
   limit: do 430 znaków
   EN: Select Adversities to gain bonus Starlight and Mirror of Names and Spiders Pass Projection rate based on your Adversity Score. However, please note that Adversity bonus rewards for each floor can be obtained only by clearing the Floor on which the Adversities were selected. Also, any other reward will be based on Floor 5 Clear rewards.
   PL: Wybranie Utrudnień zapewnia dodatkowy Gwiezdny Blask oraz Stopień Projekcji Przepustki Lustra Imion i Pająków zależnie od punktów Utrudnień. Premia za dane piętro naliczana jest jednak dopiero po jego ukończeniu, a pozostałe nagrody wypłacane są według 5. piętra.
774. [Samouczek i wskazówki [TutoMD07_P33_D4] — tekst] 선택한 제약이 많을수록 난이도는 높아지지만, 더욱 많은 양의 별빛과 이름과 거미의 거울 패스 투영도를 얻을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P33_D4].content
   limit: do 200 znaków
   EN: Selecting more Adversities will increase the difficulty. However, it will reward more Starlight and Mirror of Names and Spiders Pass Projection rate.
   PL: Im więcej Utrudnień wybierzesz, tym wyższa trudność, ale też więcej zdobywanego Gwiezdnego Blasku i Stopnia Projekcji Przepustki Lustra Imion i Pająków.
775. [Samouczek i wskazówki [TutoMD07_P34_T1] — tekst] 합성 - 자동 조합
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P34_T1].content
   limit: do 120 znaków
   EN: Fusion - Autoselect
   PL: Synteza — autowybór receptury
776. [Samouczek i wskazówki [TutoMD07_P34_D1] — tekst] 특정 조합식이 필요한 기프트의 재료 기프트를 다 모았을 경우, 클릭하여 자동으로 재료 기프트를 합성 칸에 등록할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P34_D1].content
   limit: do 210 znaków
   EN: Once you have gathered all the E.G.O Gifts necessary for a Fusion, you can automatically place them into the Fusion slot by clicking the fusible E.G.O Gift result.
   PL: Gdy zbierzesz wszystkie Dary wymagane w danej recepturze, kliknięcie docelowego Daru automatycznie umieści składniki w polach Syntezy.
777. [Samouczek i wskazówki [TutoMD07_P34_D2] — tekst] ※ 조합을 위해 합성 칸이 3개 초과로 필요한 경우, 재료 기프트를 전부 모았어도 일반 상점에서는 합성이 불가능할 수 있습니다.\n하위 재료 기프트를 조합 하거나 특별한 상점에서 시도해주시길 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD07_P34_D2].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Even if you have gathered all the required Gifts, regular shops will not allow Fusions if a Fusion requires more than 3 slots.\nTry fusing lower-tier Gifts or use a Super Shop instead.
   PL: ※ Jeśli receptura wymaga więcej niż 3 pól Syntezy, w zwykłym Sklepie nie uda się jej przeprowadzić nawet po zebraniu wszystkich składników.\nZsyntezuj najpierw składniki niższego rzędu albo skorzystaj ze Wzmocnionego Sklepu.
778. [Samouczek i wskazówki [TutoMD08_P1_T1] — tekst] 시지프의 거울
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P1_T1].content
   limit: do 120 znaków
   EN: Mirror of Sisyphe
   PL: Lustro Sisyphe
779. [Samouczek i wskazówki [TutoMD08_P1_D1] — tekst] 시즌 8 거울 던전의 명칭은 시지프의 거울입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P1_D1].content
   limit: do 120 znaków
   EN: Season 8's Mirror Dungeon is called "Mirror of Sisyphe".
   PL: Lustrzane Lochy Sezonu 8 noszą nazwę „Lustro Sisyphe”.
780. [Samouczek i wskazówki [TutoMD08_P1_D2] — tekst] 문 또는 입장 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P1_D2].content
   (powtórzenie elementu 417 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Samouczek i wskazówki [TutoMD08_P2_T1] — tekst] 주간 추가 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_T1].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Samouczek i wskazówki [TutoMD08_P2_D1] — tekst] 거울 던전에서는 매주 3회의 주간 추가 보상 기회가 제공됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D1].content
   (powtórzenie elementu 419 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Samouczek i wskazówki [TutoMD08_P2_D2] — tekst] 보상 수령 시 주간 추가 보상 기회를 사용하면, 획득하는 보상의 수치가 크게 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D2].content
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Samouczek i wskazówki [TutoMD08_P2_D3] — tekst] 거울 던전 클리어 시 모든 테마팩을 Hard 난이도로 클리어하였다면 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있습니다. 획득 보상은 소모한 주간 추가 보상 기회에 비례합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D3].content
   (powtórzenie elementu 510 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Samouczek i wskazówki [TutoMD08_P2_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 하나씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D4].content
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Samouczek i wskazówki [TutoMD08_P2_T2] — tekst] 별빛
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_T2].content
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
