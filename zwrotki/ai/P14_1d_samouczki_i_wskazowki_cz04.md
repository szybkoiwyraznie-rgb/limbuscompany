# Paczka AI P14 (Fala 1 · 1D) — Samouczki systemowe i wskazówki ekranu ładowania (część 4/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P14_1d_samouczki_i_wskazowki_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P14_1d_samouczki_i_wskazowki_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Samouczek i wskazówki: TutorialMirrorDungeon
- plik gry: `TutorialMirrorDungeon.json`

1. [Samouczek i wskazówki [TutoMD08_P2_D5] — tekst] 시지프의 거울에서는 별의 가호, 관측, 소원 빌기 등 별빛을 사용하여 던전 진행에 도움이 될 수 있는 기능들이 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D5].content
   limit: do 230 znaków
   EN: Mirror of Sisyphe adds various options and avenues to spend Starlight to help you through the dungeon, including but not limited to Grace of Stars, Observations, and Wishmaking.
   PL: W Lustrze Sisyphe dostępne są pomocne funkcje wykorzystujące Gwiezdny Blask, takie jak Błogosławieństwo Gwiazd, Obserwacja czy Życzenie Gwiazd.
2. [Samouczek i wskazówki [TutoMD08_P2_D6] — tekst] 별빛은 도달한 층이 높을수록, Hard 난이도를 더 많이 클리어할수록 획득량이 증가합니다. 또는 거울굴절철도 테마팩을 클리어하였거나 전투 보상 카드에서 별빛을 많이 선택했다면 더욱 많은 별빛을 모을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D6].content
   limit: do 330 znaków
   EN: The amount of Starlight gained is proportional to the number of Floors reached and the number of Hard difficulty Packs cleared. You can also gain additional Starlight by clearing Refraction Railway Theme Packs or selecting Starlight Encounter Reward Cards.
   PL: Ilość zdobywanego Gwiezdnego Blasku rośnie wraz z osiągniętym piętrem oraz liczbą ukończonych pakietów Hard. Dodatkowy Gwiezdny Blask zdobędziesz też za Pakiety Tematyczne Kolei Załamania i Karty Nagród za Walkę.
3. [Samouczek i wskazówki [TutoMD08_P2_D7] — tekst] 이외에도 신규 3성, E.G.O가 추출에서 새롭게 등장하여 이를 획득하였을 때, 매우 많은 양의 별빛을 얻을 수 있습니다.\n※ 자판기를 통해 획득하였을 때는 별빛이 제공되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D7].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can also gain a large amount of Starlight by Extracting a newly released 3★ Identity or E.G.O within a certain timeframe.\n※ Please note that you cannot gain Starlight by obtaining them via the Dispenser.
   PL: Bardzo dużą ilość Gwiezdnego Blasku otrzymasz też za wylosowanie w Ekstrakcji nowej Tożsamości 3★ lub E.G.O.\n※ Zakup w Automacie nie zapewnia Gwiezdnego Blasku.
4. [Samouczek i wskazówki [TutoMD08_P2_D8] — tekst] 추출로 획득한 별빛은 현재 진행 중인 거울 던전에도 즉시 적용되어 언제든지 사용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P2_D8].content
   limit: do 140 znaków
   EN: Starlight obtained from Extraction are immediately made usable for in-progress Mirror Dungeons as well.
   PL: Gwiezdny Blask zdobyty z Ekstrakcji jest natychmiast uwzględniany także w trwającej wyprawie Lustrzanych Lochów.
5. [Samouczek i wskazówki [TutoMD08_P3_T1] — tekst] 수감자
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_T1].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
6. [Samouczek i wskazówki [TutoMD08_P3_D1] — tekst] 수감자 편성 현황을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_D1].content
   limit: do 120 znaków
   EN: You can view your currently deployed Sinners here.
   PL: Tutaj sprawdzisz bieżące ustawienie Grzeszników.
7. [Samouczek i wskazówki [TutoMD08_P3_T2] — tekst] 테마팩 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_T2].content
   limit: do 120 znaków
   EN: Theme Pack Compendium
   PL: Kompendium Pakietów Tematycznych
8. [Samouczek i wskazówki [TutoMD08_P3_D2] — tekst] 거울 던전에 등장하는 테마팩을 확인할 수 있습니다.\n거울 던전 진행 중 선택한 테마팩에 대한 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_D2].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the list of Theme Packs that appear in the Mirror Dungeon.\nSelected Theme Pack records will be collected here.
   PL: Tutaj przejrzysz Pakiety Tematyczne występujące w Lustrzanych Lochach.\nZbierane są tu wpisy o wybranych podczas wypraw pakietach.
9. [Samouczek i wskazówki [TutoMD08_P3_T3] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_T3].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
10. [Samouczek i wskazówki [TutoMD08_P3_D3] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다.\n거울 던전 진행 중에 획득한 E.G.O 기프트의 기록이 수집됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P3_D3].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the list of E.G.O Gifts that appear in the Mirror Dungeon.\nObtaining an E.G.O Gift in the Mirror Dungeon will add an entry to your E.G.O Gift Compendium.
   PL: Tutaj przejrzysz Dary E.G.O występujące w Lustrzanych Lochach.\nZdobycie Daru E.G.O podczas wyprawy dodaje jego wpis do Kompendium.
11. [Samouczek i wskazówki [TutoMD08_P4_T1] — tekst] 편성
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P4_T1].content
   limit: do 120 znaków
   EN: Team Loadout
   PL: Skład drużyny
12. [Samouczek i wskazówki [TutoMD08_P4_D1] — tekst] 전투에 참여할 인격을 선택하여 편성합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P4_D1].content
   limit: do 120 znaków
   EN: Select Identities to participate in battle.
   PL: Wybierz i ustaw Tożsamości, które wezmą udział w walce.
13. [Samouczek i wskazówki [TutoMD08_P4_D2] — tekst] Normal 난이도에서는 인격 레벨이 65로 적용되고, Hard 난이도에서는 보유한 인격의 레벨에 맞추어 최대 65까지 적용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P4_D2].content
   limit: do 210 znaków
   EN: In Mirror Dungeon Normal, all Identity Levels will be fixed to 65. In Mirror Dungeon Hard, your current Identity Levels will be reflected instead, up to Level 65.
   PL: Na poziomie Normal poziom Tożsamości wynosi 65, a na poziomie Hard obowiązuje aktualny poziom posiadanych Tożsamości (maks. 65).
14. [Samouczek i wskazówki [TutoMD08_P4_D3] — tekst] 단, 인격의 동기화 단계와 E.G.O의 환상 해석 단계는 별도로 보정되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P4_D3].content
   limit: do 130 znaków
   EN: Please note that, however, Identity Uptie Tiers and E.G.O Threadspinning Tiers will not be affected.
   PL: Stopień Synchronizacji Tożsamości oraz stopień Splotu Nici E.G.O nie podlegają jednak korekcie.
15. [Samouczek i wskazówki [TutoMD08_P5_T1] — tekst] 별빛 보너스
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_T1].content
   limit: do 120 znaków
   EN: Starlight Bonus
   PL: Premia Gwiezdnego Blasku
16. [Samouczek i wskazówki [TutoMD08_P5_D1] — tekst] 거울 던전 수감자 편성 창에서는 각 인격의 별빛 보너스 게이지를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_D1].content
   limit: do 130 znaków
   EN: In the Mirror Dungeon Sinner Team loadout menu, you can view each Identity's Starlight Bonus bars.
   PL: W oknie składu Grzeszników Lustrzanych Lochów sprawdzisz pasek Premii Gwiezdnego Blasku każdej Tożsamości.
17. [Samouczek i wskazówki [TutoMD08_P5_D2] — tekst] 현재 선택한 편성을 기준으로, 각 인격의 별빛 보너스 게이지로부터 얻을 수 있는 별빛의 총합이 우하단의 확인 버튼 위에 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_D2].content
   limit: do 220 znaków
   EN: The sum of obtainable Starlight from each Identity's Starlight Bonuses in your current Team can be viewed here, at the bottom right corner, above the Confirmation button.
   PL: Łączna suma Gwiezdnego Blasku możliwa do uzyskania z pasków Premii Gwiezdnego Blasku bieżącego składu widnieje w prawym dolnym rogu nad przyciskiem potwierdzenia.
18. [Samouczek i wskazówki [TutoMD08_P5_D3] — tekst] 별빛 보너스를 통해 획득하는 별빛은 이후에 설명할 별의 가호를 고를 때 사용됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_D3].content
   limit: do 120 znaków
   EN: Starlight, which are obtained via Starlight Bonuses, are used to activate Grace of Stars.
   PL: Gwiezdny Blask uzyskany z Premii Gwiezdnego Blasku służy do wyboru Błogosławieństw Gwiazd.
19. [Samouczek i wskazówki [TutoMD08_P5_D4] — tekst] 이후 거울 던전 클리어 시, 입장 시점에 편성한 인격의 별빛 보너스는 0으로 초기화됩니다. 대신 편성하지 않은 모든 인격의 별빛 보너스는 1씩 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_D4].content
   limit: do 210 znaków
   EN: Upon clearing Mirror Dungeon, Starlight Bonuses for Identities in your current Mirror Dungeon Team resets to 0, and every other Identity gains 1 Starlight Bonus.
   PL: Po ukończeniu Lustrzanych Lochów Premia Gwiezdnego Blasku początkowego składu resetuje się do 0, a wszystkie niewystawione Tożsamości zyskują +1 Premii Gwiezdnego Blasku.
20. [Samouczek i wskazówki [TutoMD08_P5_D5] — tekst] 거울 던전 진행 과정에서 교체하여 등장한 인격은 별빛 게이지가 소모되거나 증가하지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P5_D5].content
   limit: do 170 znaków
   EN: Identities that have been swapped in or out during the Mirror Dungeon run will, however, neither spend nor gain Starlight Bonuses.
   PL: Tożsamości wprowadzone poprzez wymianę składu w trakcie wyprawy nie zużywają ani nie zyskują paska Gwiezdnego Blasku.
21. [Samouczek i wskazówki [TutoMD08_P6_T1] — tekst] 시지프 별의 가호
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_T1].content
   limit: do 120 znaków
   EN: Grace of the Sisyphean Star
   PL: Błogosławieństwo Gwiazdy Sisyphe
22. [Samouczek i wskazówki [TutoMD08_P6_D1] — tekst] 편성을 통해 획득한 별빛 보너스를 지불하여 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_D1].content
   limit: do 120 znaków
   EN: Spend Starlight Bonuses obtained from your Team loadout to select Grace of Stars.
   PL: Wydaj Premię Gwiezdnego Blasku uzyskaną ze składu, aby wybrać Błogosławieństwa Gwiazd.
23. [Samouczek i wskazówki [TutoMD08_P6_D2] — tekst] 별빛 보너스 이외에도 따로 별빛을 보유하고 있다면, 추가로 지불하여 더 많은 별의 가호를 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_D2].content
   limit: do 160 znaków
   EN: If you have more Starlight in additional to Starlight Bonuses, you can spend them as well to select more Grace of Stars.
   PL: Jeśli oprócz Premii Gwiezdnego Blasku posiadasz dodatkowy Gwiezdny Blask, możesz go dopłacić, aby wybrać więcej Błogosławieństw Gwiazd.
24. [Samouczek i wskazówki [TutoMD08_P6_D3] — tekst] 해당 버튼으로 별의 가호를 더욱 편하게 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_D3].content
   limit: do 120 znaków
   EN: Use this button to select multiple Graces at once.
   PL: Ten przycisk pozwala wygodniej wybrać naraz wiele Błogosławieństw Gwiazd.
25. [Samouczek i wskazówki [TutoMD08_P6_D4] — tekst] 별의 가호를 선택하고 남은 별빛 보너스는 클리어 시 수령하거나 던전 진행 중 사용할 코스트로 전환할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_D4].content
   limit: do 170 znaków
   EN: Remaining Starlight Bonus after selecting Graces of Stars will be converted to 'Cost' to be used during your Mirror Dungeon run.
   PL: Premię Gwiezdnego Blasku pozostałą po wyborze Błogosławieństw Gwiazd odbierzesz przy ukończeniu lub zamienisz na Koszt dostępny podczas wyprawy.
26. [Samouczek i wskazówki [TutoMD08_P6_D5] — tekst] ※ 보유 별빛은 코스트로 전환되지 않습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P6_D5].content
   limit: do 120 znaków
   EN: ※ Owned Starlight are not converted into Costs.
   PL: ※ Posiadany Gwiezdny Blask nie zamienia się w Koszt.
27. [Samouczek i wskazówki [TutoMD08_P7_T1] — tekst] 시작 E.G.O 기프트 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P7_T1].content
   limit: do 120 znaków
   EN: Starting E.G.O Gift Choice
   PL: Wybór początkowego Daru E.G.O
28. [Samouczek i wskazówki [TutoMD08_P7_D1] — tekst] 거울 던전 입장 시, E.G.O 기프트의 키워드별 항목이 제시됩니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P7_D1].content
   limit: do 120 znaków
   EN: Upon Mirror Dungeon entry, you will be given Keyword categories to choose E.G.O Gifts from.
   PL: Przy wejściu do Lustrzanych Lochów prezentowane są kategorie Darów E.G.O według słów kluczowych.
29. [Samouczek i wskazówki [TutoMD08_P7_D2] — tekst] 각 키워드별 항목의 등장 E.G.O 기프트는 고정이며, 선택한 카테고리 내에 있는 E.G.O 기프트를 선택 가능한 수만큼 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P7_D2].content
   limit: do 180 znaków
   EN: E.G.O Gifts appearing in each category are fixed. You can choose as many E.G.O Gifts as it is available to you from the same category.
   PL: Pula Darów E.G.O w każdej kategorii słowa kluczowego jest stała; z wybranej kategorii możesz dobrać tyle Darów E.G.O, na ile pozwala twój limit.
30. [Samouczek i wskazówki [TutoMD08_P7_D3] — tekst] 이 단계에서 선택한 키워드에 해당하는 E.G.O 기프트가 던전 진행 중에 더욱 자주 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P7_D3].content
   limit: do 140 znaków
   EN: Through your Mirror Dungeon run, E.G.O Gifts in the category you selected here will appear more frequently.
   PL: Dary E.G.O odpowiadające wybranemu na tym etapie słowu kluczowemu będą pojawiać się częściej podczas wyprawy.
31. [Samouczek i wskazówki [TutoMD08_P8_T1] — tekst] E.G.O 기프트 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P8_T1].content
   limit: do 120 znaków
   EN: E.G.O Gift Search
   PL: Obserwacja Darów E.G.O
32. [Samouczek i wskazówki [TutoMD08_P8_D1] — tekst] E.G.O 기프트 관측은 별빛을 소모하여 리스트에 있는 E.G.O 기프트를 추가로 획득하는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P8_D1].content
   limit: do 120 znaków
   EN: Use E.G.O Gift Search to select and obtain an E.G.O Gift from the list.
   PL: Obserwacja Darów E.G.O pozwala wydać Gwiezdny Blask, aby dobrać dodatkowy Dar E.G.O z listy.
33. [Samouczek i wskazówki [TutoMD08_P8_D2] — tekst] E.G.O 기프트 관측 기능은 토글 방식으로 ON/OFF를 할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P8_D2].content
   limit: do 120 znaków
   EN: You can toggle ON/OFF the E.G.O Gift Search function,
   PL: Funkcję Obserwacji Darów E.G.O możesz przełączać (WŁ./WYŁ.).
34. [Samouczek i wskazówki [TutoMD08_P8_D3] — tekst] 보유 중인 E.G.O 기프트는 선택하지 못하며, 선택한 E.G.O 기프트의 수에 따라 지불해야 하는 가격이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P8_D3].content
   limit: do 180 znaków
   EN: You cannot select an E.G.O Gift you already own, and the cost of selecting E.G.O Gifts grows more expensive the more E.G.O Gifts you select.
   PL: Nie możesz wybrać posiadanego już Daru E.G.O, a wraz z liczbą wybranych Darów E.G.O rośnie koszt do zapłaty.
35. [Samouczek i wskazówki [TutoMD08_P9_T1] — tekst] 테마팩 선택
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_T1].content
   limit: do 120 znaków
   EN: Selecting Theme Packs
   PL: Wybór Pakietu Tematycznego
36. [Samouczek i wskazówki [TutoMD08_P9_D1] — tekst] 층 진입 시, 이번 층에서 헤쳐나갈 테마를 제시된 목록 중에서 선택할 수 있습니다. 선택하고자 하는 테마팩을 아래로 드래그하여 고를 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D1].content
   limit: do 270 znaków
   EN: Upon entering a new Floor, you will be presented with a collection of different 'Themes' that you can choose to face on this Floor. Select and pull down a Theme Pack you would like to challenge for this Floor.
   PL: Przy wejściu na piętro wybierasz z listy motyw, z którym zmierzysz się na tym piętrze. Przeciągnij wybrany Pakiet Tematyczny w dół, aby go zatwierdzić.
37. [Samouczek i wskazówki [TutoMD08_P9_D2] — tekst] 각각의 테마팩 우상단 버튼을 통해 해당 팩에서 등장할 수 있는 보스와 전투 보상으로 얻을 수 있는 E.G.O 기프트를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D2].content
   limit: do 220 znaków
   EN: You can view the available Bosses and E.G.O Gifts(obtainable as Encounter rewards) from the Theme Pack by pressing this button in the top right corner of each Theme Pack.
   PL: Przycisk w prawym górnym rogu każdego Pakietu Tematycznego pozwala sprawdzić możliwych bossów oraz Dary E.G.O dostępne jako nagrody za walki.
38. [Samouczek i wskazówki [TutoMD08_P9_D3] — tekst] 테마팩 하단에는 해당 테마팩의 보스 클리어 시 선택 가능한 E.G.O 기프트의 목록이 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D3].content
   limit: do 180 znaków
   EN: At the bottom of the Theme Packs, you can view the list of E.G.O Gifts that you can choose from after defeating the boss of this Theme Pack.
   PL: U dołu Pakietu Tematycznego widnieje lista Darów E.G.O możliwych do wyboru po pokonaniu bossa tego pakietu.
39. [Samouczek i wskazówki [TutoMD08_P9_T2] — tekst] 테마팩 난이도 변경
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_T2].content
   limit: do 120 znaków
   EN: Choosing the Theme Pack Difficulty
   PL: Zmiana trudności Pakietu Tematycznego
40. [Samouczek i wskazówki [TutoMD08_P9_D4] — tekst] 시지프의 거울에서는 테마팩 선택 단계에서 원하는 난이도를 선택하여 입장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D4].content
   limit: do 140 znaków
   EN: In Mirror of Sisyphe, you can select the difficulty of the upcoming floor in the Theme Pack selection phase.
   PL: W Lustrze Sisyphe poziom trudności nadchodzącego piętra wybierasz na etapie wyboru Pakietu Tematycznego.
41. [Samouczek i wskazówki [TutoMD08_P9_D5] — tekst] 단, Hard 난이도를 선택하여 입장하면 이후에는 난이도를 변경할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D5].content
   limit: do 120 znaków
   EN: However, once you enter the Hard difficulty, it cannot be changed again.
   PL: Po wybraniu i wejściu na poziom Hard nie można już jednak zmienić poziomu trudności z powrotem.
42. [Samouczek i wskazówki [TutoMD08_P9_T3] — tekst] Hard 난이도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_T3].content
   limit: do 120 znaków
   EN: Hard Difficulty
   PL: Poziom Hard
43. [Samouczek i wskazówki [TutoMD08_P9_D6] — tekst] Hard 난이도 테마팩에서는 보스 클리어 시 제시되는 E.G.O 기프트의 목록이 3개에서 4개로 증가합니다. 또한 해당 목록에 있는 E.G.O 기프트를 2개 고를 수 있는 대신, 추가되는 고난도 2개가 선택됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D6].content
   limit: do 280 znaków
   EN: In Hard Theme Packs, you will be able to choose 4 instead of 3 E.G.O Gifts upon clearing the Floor Boss. Also, while you can pick two E.G.O Gifts from the said pool, you will also be selecting two Mounting Trials.
   PL: W Pakietach Tematycznych Hard po pokonaniu bossa piętra lista proponowanych Darów E.G.O rośnie z 3 do 4. Możesz wybrać z niej 2 Dary E.G.O, lecz nałożone zostaną także 2 Próby.
44. [Samouczek i wskazówki [TutoMD08_P9_D7] — tekst] Hard 난이도에서는 특별한 상점이 등장할 수 있으며, 특정 E.G.O 기프트는 Hard 난이도에서만 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P9_D7].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Hard Difficulty, you might come across certain special Shops.\nAlso, certain E.G.O Gifts are exclusive to the Hard Difficulty.
   PL: Na poziomie Hard może pojawić się Wzmocniony Sklep,\na niektóre Dary E.G.O dostępne są wyłącznie na poziomie Hard.
45. [Samouczek i wskazówki [TutoMD08_P10_T1] — tekst] 테마팩 관측
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P10_T1].content
   limit: do 120 znaków
   EN: Theme Pack Observation
   PL: Obserwacja Pakietów Tematycznych
46. [Samouczek i wskazówki [TutoMD08_P10_D1] — tekst] 테마팩 관측은 별빛을 소모하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 찾는 신규 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P10_D1].content
   limit: do 240 znaków
   EN: By using the new addition Theme Pack Observation, or "Pack Search", you can choose specific Theme Packs from the list of available Packs in the current Floor and Difficulty combination.
   PL: Obserwacja Pakietów Tematycznych to nowa funkcja pozwalająca za Gwiezdny Blask wyszukać wybrany Pakiet Tematyczny dostępny na bieżącym piętrze i poziomie trudności.
47. [Samouczek i wskazówki [TutoMD08_P10_D2] — tekst] 테마팩 관측 버튼을 선택하여 활성화하면 테마팩의 우상단 버튼이 새로고침 모양으로 변경되며, 이를 선택하면 테마팩 관측 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P10_D2].content
   limit: do 230 znaków
   EN: Selecting the "Pack Search" button will change the top right corner buttons of each Theme Packs to Refresh icons. Select those icons to enter the Theme Pack Observation window.
   PL: Po włączeniu przycisku Obserwacji Pakietów Tematycznych ikona w prawym górnym rogu pakietów zmieni się w symbol odświeżenia — kliknij go, aby otworzyć okno Obserwacji.
48. [Samouczek i wskazówki [TutoMD08_P10_D3] — tekst] 별빛을 사용하여 현재 층과 난이도에서 등장할 수 있는 테마팩을 선택하여 등장시킬 수 있습니다. 아직 열람하지 못한 테마팩의 경우에는 별빛을 추가로 소모합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P10_D3].content
   limit: do 210 znaków
   EN: Spend Starlight to select an available Theme Pack in the current Floor & Difficulty combination. Previously unobserved Theme Packs spend more Starlight to select.
   PL: Wydaj Gwiezdny Blask, aby wywołać wybrany Pakiet Tematyczny dostępny na bieżącym piętrze i trudności. Pakiety jeszcze nieodkryte wymagają dodatkowego Gwiezdnego Blasku.
49. [Samouczek i wskazówki [TutoMD08_P10_D4] — tekst] 단, 던전 진행 과정에서 테마팩 관측 기능을 사용할수록 필요한 별빛 비용이 증가하므로 이를 유의해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P10_D4].content
   limit: do 160 znaków
   EN: However, please be warned that the more you use the Theme Pack Search function, the more Starlight it will cost to use.
   PL: Pamiętaj jednak, że każde kolejne użycie Obserwacji Pakietów Tematycznych w trakcie wyprawy zwiększa koszt w Gwiezdnym Blasku.
50. [Samouczek i wskazówki [TutoMD08_P11_T1] — tekst] 거울 던전 탐사
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P11_T1].content
   limit: do 120 znaków
   EN: Exploring Mirror Dungeons
   PL: Eksploracja Lustrzanych Lochów
51. [Samouczek i wskazówki [TutoMD08_P11_D1] — tekst] 거울 던전에 입장하게 되면 인카운터와 경로가 무작위로 생성됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P11_D1].content
   limit: do 120 znaków
   EN: The Mirror Dungeon Encounters and paths are randomly generated.
   PL: Po wejściu do Lustrzanych Lochów starcia oraz ścieżki generowane są losowo.
52. [Samouczek i wskazówki [TutoMD08_P11_D2] — tekst] 현재 인카운터에서 연결된 인카운터을 선택해 진행하며, 각 인카운터에서는 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P11_D2].content
   limit: do 170 znaków
   EN: You proceed by moving to nodes adjacent to your current node. You may find various events or combat encounters in each of the nodes.
   PL: Poruszasz się, wybierając węzły połączone z bieżącym; w każdym z nich losowo pojawiają się rozmaite walki oraz wydarzenia.
53. [Samouczek i wskazówki [TutoMD08_P11_T2] — tekst] 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P11_T2].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
54. [Samouczek i wskazówki [TutoMD08_P11_D3] — tekst] 거울 던전 진행 과정에서 코스트를 획득할 수 있습니다. 코스트를 지불하여 상점의 기능을 이용할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P11_D3].content
   limit: do 170 znaków
   EN: You will earn 'Cost' as you proceed through the Mirror Dungeon. 'Cost' you earned can be spent at Shops for their various services.
   PL: Podczas wyprawy przez Lustrzane Lochy zdobywasz Koszt, za który skorzystasz z funkcji Sklepów.
55. [Samouczek i wskazówki [TutoMD08_P12_T1] — tekst] 스테이지 유효 속성과 획득 코스트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_T1].content
   limit: do 120 znaków
   EN: Effective Attacks & Cost Rewards
   PL: Skuteczne atrybuty i Koszt
56. [Samouczek i wskazówki [TutoMD08_P12_D1] — tekst] 거울 던전의 전투 인카운터에는 해당 전투에서 유효한 속성과 해당 전투를 클리어 시 획득할 수 있는 코스트가 표시됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_D1].content
   limit: do 220 znaków
   EN: Combat Encounter nodes of Mirror Dungeons display affinity/attack type useful for that battle. It also displays the amount of Cost reward you can gain by completing it.
   PL: Na węzłach walk w Lustrzanych Lochach wyświetlane są skuteczne typy ataków i grzechy oraz liczba Kosztu za ukończenie starcia.
57. [Samouczek i wskazówki [TutoMD08_P12_T2] — tekst] 수감자 현황
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_T2].content
   limit: do 120 znaków
   EN: Sinner Status
   PL: Stan Grzeszników
58. [Samouczek i wskazówki [TutoMD08_P12_D2] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_D2].content
   limit: do 120 znaków
   EN: The HP, SP, and lost lives of your Sinners will carry over between encounters.
   PL: Przez cały czas trwania wyprawy PŻ, PP oraz stan poległych Grzeszników przechodzą między walkami.
59. [Samouczek i wskazówki [TutoMD08_P12_T3] — tekst] E.G.O 기프트
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_T3].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
60. [Samouczek i wskazówki [TutoMD08_P12_D3] — tekst] 획득한 E.G.O 기프트가 표시됩니다. E.G.O 기프트는 던전 안에서 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_D3].content
   limit: do 170 znaków
   EN: Acquired E.G.O Gifts are displayed here. E.G.O Gifts are items that offer powerful effects that last until the end of the Dungeon.
   PL: Tutaj widnieją zdobyte Dary E.G.O — przedmioty zapewniające potężne efekty działające wewnątrz lochu.
61. [Samouczek i wskazówki [TutoMD08_P12_T4] — tekst] 수감자 편성 확인
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_T4].content
   limit: do 120 znaków
   EN: Observe Team Loadout
   PL: Podgląd składu Grzeszników
62. [Samouczek i wskazówki [TutoMD08_P12_D4] — tekst] 현재 편성된 인격의 상세 정보를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_D4].content
   limit: do 120 znaków
   EN: You can view detailed information of the Identities in your loadout.
   PL: Sprawdzisz tu szczegółowe informacje o Tożsamościach w bieżącym składzie.
63. [Samouczek i wskazówki [TutoMD08_P12_T5] — tekst] 적용 효과 목록
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_T5].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
64. [Samouczek i wskazówki [TutoMD08_P12_D5] — tekst] 던전을 진행하는 동안 선택한 고난, 별의 가호, 선택지 효과를 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P12_D5].content
   limit: do 120 znaków
   EN: View your Mounting Trials, Grace of Stars, and Choice Event Effects here.
   PL: Sprawdzisz tu wybrane podczas wyprawy Próby, Błogosławieństwa Gwiazd oraz efekty z wydarzeń.
65. [Samouczek i wskazówki [TutoMD08_P13_T1] — tekst] 상점
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P13_T1].content
   limit: do 120 znaków
   EN: Shops
   PL: Sklep
66. [Samouczek i wskazówki [TutoMD08_P13_D1] — tekst] 테마팩 보스 전투 직전에는 상점이 배치되어 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P13_D1].content
   limit: do 120 znaków
   EN: Nodes before Theme Pack Boss Encounters are shops.
   PL: Tuż przed walką z bossem Pakietu Tematycznego znajduje się Sklep.
67. [Samouczek i wskazówki [TutoMD08_P13_D2] — tekst] 코스트를 소모하여 E.G.O 기프트를 구입하거나 수감자 회복과 부활, 편성 교체, 인격 스킬 교체를 진행할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P13_D2].content
   limit: do 200 znaków
   EN: At Shops, you can spend your 'Cost' to purchase E.G.O Gifts, heal or revive Sinners, deploy/swap out additional Identities, or replace Identity Skills.
   PL: W Sklepie wydasz Koszt na zakup Darów E.G.O, leczenie i wskrzeszanie Grzeszników, zmianę składu lub wymianę umiejętności Tożsamości.
68. [Samouczek i wskazówki [TutoMD08_P13_D3] — tekst] 또한 E.G.O 기프트를 상점에서 판매하여 코스트를 획득하거나, E.G.O 기프트를 합성하여 더욱 유용한 E.G.O 기프트를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P13_D3].content
   limit: do 170 znaków
   EN: Also, you can sell your E.G.O Gifts at Shops to gain more Cost or Fuse your E.G.O Gifts to gain even more useful E.G.O Gifts.
   PL: Możesz też sprzedawać Dary E.G.O za Koszt albo syntezować je, aby zdobyć jeszcze bardziej przydatne Dary E.G.O.
69. [Samouczek i wskazówki [TutoMD08_P13_D4] — tekst] Hard 난이도로 진행 시, 특별한 상점이 등장할 수 있습니다. 거울 던전 진행 중에 누적 소모한 코스트가 많을수록 특별한 상점이 등장할 확률이 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P13_D4].content
   limit: do 210 znaków
   EN: In Hard difficulty, there is a chance for a Super Shop to appear. The more Cost you spend in a Mirror Dungeon run, the greater the chance becomes for it to appear.
   PL: Na poziomie Hard może pojawić się Wzmocniony Sklep — szansa na jego wystąpienie rośnie wraz z łączną ilością wydanego w wyprawie Kosztu.
70. [Samouczek i wskazówki [TutoMD08_P14_T1] — tekst] 조합식
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P14_T1].content
   limit: do 120 znaków
   EN: Fusion Recipes
   PL: Receptury Syntezy
71. [Samouczek i wskazówki [TutoMD08_P14_D1] — tekst] 특정 조합식이 필요한 기프트의 조합식을 확인할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P14_D1].content
   limit: do 120 znaków
   EN: Some E.G.O Gifts require specific recipes to fuse. View them here.
   PL: Sprawdzisz tu receptury Darów E.G.O wymagających określonych składników.
72. [Samouczek i wskazówki [TutoMD08_P14_D2] — tekst] 특정 테마팩에서만 획득할 수 있는 기프트를 재료로 필요하는 기프트도 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P14_D2].content
   limit: do 140 znaków
   EN: There are also E.G.O Gifts whose recipes require certain Theme Pack exclusive E.G.O Gifts as ingredients.
   PL: Niektóre Dary wymagają jako składników Darów dostępnych wyłącznie w określonych Pakietach Tematycznych.
73. [Samouczek i wskazówki [TutoMD08_P34_T1] — tekst] 합성 - 자동 조합
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P34_T1].content
   limit: do 120 znaków
   EN: Fusion - Autoselect
   PL: Synteza — autowybór receptury
74. [Samouczek i wskazówki [TutoMD08_P34_D1] — tekst] 특정 조합식이 필요한 기프트의 재료 기프트를 다 모았을 경우, 클릭하여 자동으로 재료 기프트를 합성 칸에 등록할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P34_D1].content
   limit: do 210 znaków
   EN: Once you have gathered all the E.G.O Gifts necessary for a Fusion, you can automatically place them into the Fusion slot by clicking the fusible E.G.O Gift result.
   PL: Gdy zbierzesz wszystkie Dary wymagane w danej recepturze, kliknięcie docelowego Daru automatycznie umieści składniki w polach Syntezy.
75. [Samouczek i wskazówki [TutoMD08_P34_D2] — tekst] ※ 조합을 위해 합성 칸이 3개 초과로 필요한 경우, 재료 기프트를 전부 모았어도 일반 상점에서는 합성이 불가능할 수 있습니다.\n하위 재료 기프트를 조합 하거나 특별한 상점에서 시도해주시길 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P34_D2].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Even if you have gathered all the required Gifts, regular shops will not allow Fusions if a Fusion requires more than 3 slots.\nTry fusing lower-tier Gifts or use a Super Shop instead.
   PL: ※ Jeśli receptura wymaga więcej niż 3 pól Syntezy, w zwykłym Sklepie nie uda się jej przeprowadzić nawet po zebraniu wszystkich składników.\nZsyntezuj najpierw składniki niższego rzędu albo skorzystaj ze Wzmocnionego Sklepu.
76. [Samouczek i wskazówki [TutoMD08_P15_T1] — tekst] 합성 - 소원 빌기
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P15_T1].content
   limit: do 120 znaków
   EN: Fusion - Wishmaking
   PL: Synteza — Życzenie Gwiazd
77. [Samouczek i wskazówki [TutoMD08_P15_D1] — tekst] 소원 빌기는 별빛을 추가로 소모하여 E.G.O 기프트 합성 확률을 증가시킬 수 있는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P15_D1].content
   limit: do 150 znaków
   EN: By using the Wishmaking function, you can spend additional Starlight to improve the E.G.O Gift Fusion success rate.
   PL: Życzenie Gwiazd pozwala wydać dodatkowy Gwiezdny Blask, aby zwiększyć szansę powodzenia Syntezy Darów E.G.O.
78. [Samouczek i wskazówki [TutoMD08_P15_D2] — tekst] 소원 빌기는 사용 횟수와 관계 없이 비용이 고정됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P15_D2].content
   limit: do 120 znaków
   EN: The cost of Wishmaking remains the same no matter how many times it is used.
   PL: Koszt Życzenia Gwiazd jest stały niezależnie od liczby użyć.
79. [Samouczek i wskazówki [TutoMD08_P16_T1] — tekst] 전투 보상 카드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P16_T1].content
   limit: do 120 znaków
   EN: Encounter Reward Cards
   PL: Karty Nagród za Walkę
80. [Samouczek i wskazówki [TutoMD08_P16_D1] — tekst] 전투에서 승리하면 전투 난이도에 따라 일정 확률로 전투 보상 카드가 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P16_D1].content
   limit: do 240 znaków
   EN: There is a chance for 'Encounter Reward Cards' to appear after winning an Encounter. The harder the Encounter difficulty, the higher the chance of obtaining an Encounter Reward Card.
   PL: Po zwycięstwie w starciu masz zależną od trudności walki szansę na pojawienie się Kart Nagród za Walkę.
81. [Samouczek i wskazówki [TutoMD08_P16_D2] — tekst] 전투 보상 카드를 통해 코스트, 별빛, E.G.O 기프트, E.G.O 자원을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P16_D2].content
   limit: do 160 znaków
   EN: You can obtain various resources such as Cost, Starlight, E.G.O Gifts, or E.G.O Resources from the Encounter Reward Cards.
   PL: Z Kart Nagród za Walkę zdobędziesz Koszt, Gwiezdny Blask, Dary E.G.O lub zasoby E.G.O.
82. [Samouczek i wskazówki [TutoMD08_P17_T1] — tekst] E.G.O 기프트와 추가되는 고난
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P17_T1].content
   limit: do 120 znaków
   EN: E.G.O Gifts & Mounting Trials
   PL: Dary E.G.O i dodawane Próby
83. [Samouczek i wskazówki [TutoMD08_P17_D1] — tekst] 층을 클리어할 경우, E.G.O 기프트와 함께 연결된 고난 효과를 선택하여 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P17_D1].content
   limit: do 120 znaków
   EN: Upon clearing a floor, you will obtain random enemy buffs linked to each E.G.O Gift.
   PL: Po ukończeniu piętra wybierasz Dar E.G.O wraz z powiązanym z nim efektem Próby.
84. [Samouczek i wskazówki [TutoMD08_P17_D2] — tekst] 층을 클리어할 때마다 고난 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P17_D2].content
   limit: do 120 znaków
   EN: Mounting Trials will continue to stack with every floor cleared.
   PL: Efekty Prób kumulują się z każdym ukończonym piętrem.
85. [Samouczek i wskazówki [TutoMD08_P17_D3] — tekst] Hard 난이도로 진행 시, E.G.O 기프트를 2개 선택할 수 있습니다. 대신 고난 효과도 2개를 선택하게 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P17_D3].content
   limit: do 180 znaków
   EN: In Hard difficulty, you can select 2 E.G.O Gifts. However, this means that you will be selecting 2 Mounting Trials in the process as well.
   PL: Na poziomie Hard możesz wybrać 2 Dary E.G.O, lecz wiąże się to również z wyborem 2 efektów Prób.
86. [Samouczek i wskazówki [TutoMD08_P18_T1] — tekst] 거울 던전 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P18_T1].content
   limit: do 120 znaków
   EN: Mirror Dungeon Rewards
   PL: Nagrody Lustrzanych Lochów
87. [Samouczek i wskazówki [TutoMD08_P18_D1] — tekst] 거울 던전 클리어 시, 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P18_D1].content
   limit: do 120 znaków
   EN: Upon clearing a Mirror Dungeon run, spend Enkephalin Modules to claim your rewards.
   PL: Po ukończeniu Lustrzanych Lochów wydaj Moduły Enkefaliny, aby odebrać nagrody.
88. [Samouczek i wskazówki [TutoMD08_P18_D2] — tekst] 보상은 클리어한 층 수에 따라 지급되며, 주간 보너스 기회를 사용하여 더 많은 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P18_D2].content
   limit: do 160 znaków
   EN: The amount of rewards depends on the number of cleared Floors. You can use Weekly Bonus chances to claim even more rewards.
   PL: Liczba nagród zależy od ukończonych pięter; użyj szans Cotygodniowej Premii, aby zdobyć ich jeszcze więcej.
89. [Samouczek i wskazówki [TutoMD08_P18_D3] — tekst] 모든 테마팩을 Hard 난이도로 클리어 시, 주간 추가 보상 기회를 한 번에 2개 이상 소모할 수 있으며, 그에 비례한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P18_D3].content
   limit: do 240 znaków
   EN: If you chose Hard difficulty Theme Packs for every Floor, you can consume 2 or more Weekly Bonuses at once, and will receive rewards proportional to the number of Weekly Bonuses used.
   PL: Ukończenie wszystkich Pakietów Tematycznych na poziomie Hard pozwala zużyć naraz 2 lub więcej szans Cotygodniowej Premii i zyskać proporcjonalne nagrody.
90. [Samouczek i wskazówki [TutoMD08_P18_D4] — tekst] 단, 주간 추가 보상 기회를 한 번에 사용하는 것보다는 한 번에 1회씩 사용하는 것이 소모한 엔케팔린 대비 보상 효율이 제일 높습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P18_D4].content
   limit: do 150 znaków
   EN: However, it is more enkephalin-efficient to use 1 Weekly Bonus at a time rather than to use them all at once.
   PL: Najwyższą wydajność nagród względem zużytej Enkefaliny daje jednak wykorzystywanie Cotygodniowej Premii pojedynczo (po 1 razie).
91. [Samouczek i wskazówki [TutoMD08_P19_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P19_T1].content
   limit: do 120 znaków
   EN: Achievements
   PL: Osiągnięcia
92. [Samouczek i wskazówki [TutoMD08_P19_D1] — tekst] 업적은 특별한 도전 달성 시 투영도가 쌓이며, 이를 통해 다양한 보상을 획득할 수 있는 콘텐츠입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P19_D1].content
   limit: do 140 znaków
   EN: Achievements is a game content in which you beat challenges to gain Projection rate to earn various rewards.
   PL: Osiągnięcia to zawartość, w której realizujesz specjalne wyzwania, gromadzisz Stopień Projekcji i odbierasz rozmaite nagrody.
93. [Samouczek i wskazówki [TutoMD08_P25_T1] — tekst] 평행중첩 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P25_T1].content
   limit: do 120 znaków
   EN: Parallel Superposition Mode
   PL: Tryb Superpozycji Równoległej
94. [Samouczek i wskazówki [TutoMD08_P25_D1] — tekst] 평행중첩 모드 적용 시, 거울 던전을 최대 10층까지 도전할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P25_D1].content
   limit: do 120 znaków
   EN: Engage the Parallel Superposition Mode to extend the Mirror Dungeon up to 10 Floors.
   PL: Włączenie Trybu Superpozycji Równoległej pozwala kontynuować wyzwanie Lustrzanych Lochów aż do 10. piętra.
95. [Samouczek i wskazówki [TutoMD08_P25_D2] — tekst] 평행중첩 모드는 도전 또는 업적 달성을 위한 모드이며, 5층 클리어 기준으로 별도로 보상이 증가하지는 않으니 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P25_D2].content
   limit: do 180 znaków
   EN: Please note that Parallel Superposition Mode is solely for Achievements, and does not yield additional rewards on its own past Floor 5.
   PL: Tryb Superpozycji Równoległej przeznaczony jest do wyzwań oraz Osiągnięć i sam w sobie nie zwiększa nagród powyżej poziomu 5. piętra.
96. [Samouczek i wskazówki [TutoMD08_P26_D1] — tekst] 거울 던전 입장화면 또는 던전 진행도 창에서 평행중첩 모드 활성화 여부를 언제든지 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P26_D1].content
   limit: do 170 znaków
   EN: You can choose at any time to engage the Parallel Superposition Mode at the Mirror Dungeon entrance and the Dungeon Progress window.
   PL: Tryb Superpozycji Równoległej możesz w dowolnej chwili włączyć lub wyłączyć na ekranie wejścia lub w oknie postępu lochu.
97. [Samouczek i wskazówki [TutoMD08_P26_D2] — tekst] 단, 평행중첩 모드를 적용하기 위해서는 5층까지의 모든 테마팩을 하드 난이도로 클리어해야 합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P26_D2].content
   limit: do 200 znaków
   EN: However, in order to enter the Parallel Superposition Mode, you had to have finished every Floor Theme Pack up to Floor 5 of that run in Hard difficulty.
   PL: Aby wejść w Tryb Superpozycji Równoległej, musisz jednak ukończyć wszystkie Pakiety Tematyczne do 5. piętra włącznie na poziomie Hard.
98. [Samouczek i wskazówki [TutoMD08_P27_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 5층 클리어 시, 평행중첩 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P27_D1].content
   limit: do 200 znaków
   EN: Clear Floor 5 while the Parallel Superposition Mode is engaged, and a prompt will appear asking if you would like to enter the Parallel Superposition Mode.
   PL: Po ukończeniu 5. piętra przy aktywnym Trybie Superpozycji Równoległej pojawi się okno z pytaniem o przejście w ten tryb.
99. [Samouczek i wskazówki [TutoMD08_P27_D2] — tekst] 확인 선택 시, 평행중첩 모드가 적용되어 6층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P27_D2].content
   limit: do 120 znaków
   EN: Confirm to enter Parallel Superposition Mode and move up to Floor 6.
   PL: Potwierdź, aby aktywować Tryb Superpozycji Równoległej i wejść na 6. piętro.
100. [Samouczek i wskazówki [TutoMD08_P27_D3] — tekst] 5층 클리어 이후에는 실패 혹은 중도 포기하더라도 5층 클리어 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P27_D3].content
   limit: do 170 znaków
   EN: Please note that failing or exiting the Mirror Dungeon at any point past Floor 5 will still yield full Floor 5 Clear Rewards.
   PL: Pamiętaj, że po ukończeniu 5. piętra nawet porażka lub rezygnacja na dalszym etapie nadal zapewni pełne nagrody za 5. piętro.
101. [Samouczek i wskazówki [TutoMD08_P32_T1] — tekst] 평행중첩 EXTREME 모드
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P32_T1].content
   limit: do 120 znaków
   EN: Parallel Superposition EXTREME
   PL: Tryb Superpozycji Równoległej EXTREME
102. [Samouczek i wskazówki [TutoMD08_P32_D1] — tekst] 평행중첩 모드를 활성화한 상태에서 10층 클리어시, 평행중첩 EXTREME 모드 적용 여부를 묻는 창이 등장합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P32_D1].content
   limit: do 210 znaków
   EN: Clear Floor 10 while the Parallel Superposition Mode is engaged, and a prompt will appear asking if you would like to enter the Parallel Superposition EXTREME Mode.
   PL: Po ukończeniu 10. piętra w aktywnym Trybie Superpozycji Równoległej pojawi się okno z pytaniem o włączenie Trybu Superpozycji Równoległej EXTREME.
103. [Samouczek i wskazówki [TutoMD08_P32_D2] — tekst] 확인 선택 시, 평행중첩 EXTREME 모드가 적용되어 11층으로 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P32_D2].content
   limit: do 120 znaków
   EN: Confirm to enter Parallel Superposition EXTREME Mode and move up to Floor 11.
   PL: Potwierdź, aby aktywować tryb EXTREME i wejść na 11. piętro.
104. [Samouczek i wskazówki [TutoMD08_P32_D3] — tekst] 실패 혹은 중도 포기하게 될 시 탐사 완료된 이전 층을 기준으로 보상을 획득할 수 있으니 참고하시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P32_D3].content
   limit: do 180 znaków
   EN: Please note that failing or exiting the Mirror Dungeon at any point will still yield Clear Rewards based on the Floor you cleared last.
   PL: W razie porażki lub rezygnacji po drodze otrzymasz nagrody odpowiadające ostatniemu ukończonemu piętru.
105. [Samouczek i wskazówki [TutoMD08_P33_T1] — tekst] 제약 설정
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P33_T1].content
   limit: do 120 znaków
   EN: Set Adversities
   PL: Ustawienia Utrudnień
106. [Samouczek i wskazówki [TutoMD08_P33_D1] — tekst] 11층부터는 제약을 선택할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P33_D1].content
   limit: do 120 znaków
   EN: Starting from Floor 11, you can select "Adversities".
   PL: Od 11. piętra możesz wybierać Utrudnienia.
107. [Samouczek i wskazówki [TutoMD08_P33_D2] — tekst] 제약은 각층마다 최대 5개까지 설정할 수 있으며,\n층을 클리어할 때마다 제약 점수와 제약 효과는 누적됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P33_D2].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can select up to 5 Adversities per Floor; your Adversity Score & Adversity effects stack with every Floor clear.
   PL: Na każdym piętrze możesz ustawić do 5 Utrudnień;\nz każdym ukończonym piętrem punkty i efekty Utrudnień kumulują się.
108. [Samouczek i wskazówki [TutoMD08_P33_D3] — tekst] 제약을 선택하면 제약 점수에 따라 추가 별빛과 시지프의 거울 패스 투영도를 획득할 수 있습니다. 단, 추가 보상의 경우 제약 설정을 진행했던 층을 클리어 해야만 결과에 합산됩니다. 또한 그 외 보상은 5층 클리어 기준으로 지급됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P33_D3].content
   limit: do 420 znaków
   EN: Select Adversities to gain bonus Starlight and Mirror of Sisyphe Pass Projection rate based on your Adversity Score. However, please note that Adversity bonus rewards for each floor can be obtained only by clearing the Floor on which the Adversities were selected. Also, any other reward will be based on Floor 5 Clear rewards.
   PL: Wybranie Utrudnień zapewnia dodatkowy Gwiezdny Blask oraz Stopień Projekcji Przepustki Lustra Sisyphe zależnie od punktów Utrudnień. Premia za dane piętro naliczana jest jednak dopiero po jego ukończeniu, a pozostałe nagrody wypłacane są według 5. piętra.
109. [Samouczek i wskazówki [TutoMD08_P33_D4] — tekst] 선택한 제약이 많을수록 난이도는 높아지지만, 더욱 많은 양의 별빛과 시지프의 거울 패스 투영도를 얻을 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P33_D4].content
   limit: do 180 znaków
   EN: Selecting more Adversities will increase the difficulty. However, it will reward more Starlight and Mirror of Sisyphe Pass Projection rate.
   PL: Im więcej Utrudnień wybierzesz, tym wyższa trudność, ale też więcej Gwiezdnego Blasku i Stopnia Projekcji Przepustki Lustra Sisyphe.
110. [Samouczek i wskazówki [TutoMD08_P20_T1] — tekst] 편성 대여
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P20_T1].content
   limit: do 120 znaków
   EN: Team Rental
   PL: Wypożyczenie składu
111. [Samouczek i wskazówki [TutoMD08_P20_D1] — tekst] 편성 대여는 성장 시킬 필요 없는 지정된 덱으로 거울 던전과 신규 인격을 체험해볼 수 있는 기능입니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P20_D1].content
   limit: do 140 znaków
   EN: Through the Team Rental system, you can experience the Mirror Dungeon with new Identities in a preset Team.
   PL: Wypożyczenie składu pozwala wypróbować Lustrzane Lochy oraz nowe Tożsamości gotową talią niewymagającą rozwoju.
112. [Samouczek i wskazówki [TutoMD08_P20_D2] — tekst] 편성 대여는 대여 버튼을 선택하여 진입할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P20_D2].content
   limit: do 120 znaków
   EN: Select the rental button to enter the Team Rental menu.
   PL: Wejdziesz tam za pomocą przycisku wypożyczenia.
113. [Samouczek i wskazówki [TutoMD08_P21_T1] — tekst] 편성 대여
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P21_T1].content
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Samouczek i wskazówki [TutoMD08_P21_D1] — tekst] 대여 기간 중 1회 한정으로 편성을 대여하여 거울 던전을 플레이할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P21_D1].content
   limit: do 140 znaków
   EN: Each Rental Team can be rented to play through the Mirror Dungeon once over their respective rental periods.
   PL: W okresie wypożyczenia możesz jednorazowo wypożyczyć skład, aby rozegrać Lustrzane Lochy.
115. [Samouczek i wskazówki [TutoMD08_P21_D2] — tekst] 거울 던전 클리어 보상 수령 시 대여 횟수가 차감됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P21_D2].content
   limit: do 120 znaków
   EN: Claiming the Mirror Dungeon Clear Reward will consume your Rental chance.
   PL: Limit wypożyczenia zostaje zużyty w momencie odbioru nagród za ukończenie Lustrzanych Lochów.
116. [Samouczek i wskazówki [TutoMD08_P21_D3] — tekst] 편성 대여로 평행 중첩 모드에 진입할 수 없습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P21_D3].content
   limit: do 120 znaków
   EN: You cannot enter the Parallel Superposition mode with a Rental Team.
   PL: Wypożyczonym składem nie można wejść w Tryb Superpozycji Równoległej.
117. [Samouczek i wskazówki [TutoMD08_P22_D1] — tekst] 편성 대여는 정해진 인격과 E.G.O 스킬을 사용하며, 변경이 불가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P22_D1].content
   limit: do 120 znaków
   EN: Rental Teams use preset Identities and E.G.O, none of which can be changed.
   PL: Wypożyczony skład korzysta ze z góry ustalonych Tożsamości i E.G.O, których nie można zmienić.
118. [Samouczek i wskazówki [TutoMD08_P22_D2] — tekst] 편성 대여에 있는 인격은 최대 별빛 보너스를 획득합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P22_D2].content
   limit: do 120 znaków
   EN: All Identities in the Rental Team receive maximum Starlight Bonuses.
   PL: Wszystkie Tożsamości w wypożyczonym składzie otrzymują maksymalną Premię Gwiezdnego Blasku.
119. [Samouczek i wskazówki [TutoMD08_P23_D1] — tekst] 편성 대여로는 편성 변경이 불가 합니다
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P23_D1].content
   limit: do 120 znaków
   EN: Rental Teams' loadouts cannot be edited or altered.
   PL: Wypożyczonego składu nie można modyfikować.
120. [Samouczek i wskazówki [TutoMD08_P24_T1] — tekst] 편성 대여 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P24_T1].content
   limit: do 120 znaków
   EN: Team Rental Rewards
   PL: Nagrody wypożyczonego składu
121. [Samouczek i wskazówki [TutoMD08_P24_D1] — tekst] 편성 대여로 별빛과 이벤트 재화를 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P24_D1].content
   limit: do 120 znaków
   EN: You can gain Starlight and Event currencies by using Rental Teams.
   PL: Grając wypożyczonym składem, zdobędziesz Gwiezdny Blask oraz waluty wydarzeń.
122. [Samouczek i wskazówki [TutoMD08_P24_D2] — tekst] 편성 대여로는 주간 보너스를 1회만 소모 가능합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P24_D2].content
   limit: do 120 znaków
   EN: Only one Weekly Bonus can be consumed when clearing a Mirror Dungeon with a Rental Team.
   PL: Wypożyczony skład pozwala zużyć tylko 1 Cotygodniową Premię.
123. [Samouczek i wskazówki [TutoMD08_P28_T1] — tekst] 거울 투영 / 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P28_T1].content
   limit: do 120 znaków
   EN: Mirror Projection / Achievements
   PL: Projekcja Lustra / Osiągnięcia
124. [Samouczek i wskazówki [TutoMD08_P28_D1] — tekst] 업적 달성 및 거울 던전 클리어 시, 투영도가 증가합니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P28_D1].content
   limit: do 120 znaków
   EN: Completing an Achievement or clearing a Mirror Dungeon raises your Projection Rate.
   PL: Zdobycie Osiągnięcia lub ukończenie Lustrzanych Lochów zwiększa Stopień Projekcji.
125. [Samouczek i wskazówki [TutoMD08_P28_D2] — tekst] 투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P28_D2].content
   limit: do 120 znaków
   EN: You can obtain various rewards by meeting Projection rate milestones.
   PL: Po osiągnięciu kolejnych progów Stopnia Projekcji odbierzesz rozmaite nagrody.
126. [Samouczek i wskazówki [TutoMD08_P29_T1] — tekst] 업적
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P29_T1].content
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Samouczek i wskazówki [TutoMD08_P29_D1] — tekst] 다양한 업적을 통해 투영도을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P29_D1].content
   limit: do 120 znaków
   EN: Raise your Projection rate by completing various Achievements.
   PL: Zdobywaj Stopień Projekcji, wykonując różnorodne Osiągnięcia.
128. [Samouczek i wskazówki [TutoMD08_P29_D2] — tekst] ※ 클리어 관련 업적은 보상 수령 창에서 엔케팔린 모듈을 소모하여 클리어할 때 적용되므로, 이를 도전하시는 관리자님께서는 참고해주시기 바랍니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P29_D2].content
   limit: do 280 znaków
   EN: ※ Achievements that require the player to 'clear' the Mirror Dungeon count only when the Enkephalin Modules have been consumed at the reward claim window. Please note this information before attempting to complete them.
   PL: ※ Osiągnięcia powiązane z ukończeniem zaliczane są dopiero po zużyciu Modułów Enkefaliny w oknie odbioru nagród — prosimy Kierowników o uwzględnienie tego podczas wyzwań.
129. [Samouczek i wskazówki [TutoMD08_P30_T1] — tekst] 투영도 보상
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P30_T1].content
   limit: do 120 znaków
   EN: Projection Rewards
   PL: Nagrody Projekcji
130. [Samouczek i wskazówki [TutoMD08_P30_D1] — tekst] 투영도가 일정 수치가 될 때마다 다양한 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P30_D1].content
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Samouczek i wskazówki [TutoMD08_P31_T1] — tekst] 주간 투영도
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P31_T1].content
   limit: do 120 znaków
   EN: Weekly Projection
   PL: Tygodniowy Stopień Projekcji
132. [Samouczek i wskazówki [TutoMD08_P31_D1] — tekst] 거울 던전 클리어후 보상 수령 시 투영도를 획득 하실 수 있습니다. 획득 가능한 투영도는 거울 던전 진행 방식에 따라 달라집니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P31_D1].content
   limit: do 250 znaków
   EN: You can earn "Projection" rate by clearing the Mirror Dungeon and claiming its rewards. Obtainable Projection rate changes based on your progress and choices made during your Mirror Dungeon runs.
   PL: Po ukończeniu Lustrzanych Lochów i odbiorze nagród zdobywasz Stopień Projekcji. Jego ilość zależy od przebiegu wyprawy.
133. [Samouczek i wskazówki [TutoMD08_P31_D2] — tekst] 획득한 투영도로 시지프의 거울 패스 레벨을 올릴 수 있으며, 레벨에 따라 각종 보상을 획득할 수 있습니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P31_D2].content
   limit: do 170 znaków
   EN: Increasing your Projection rate raises your Mirror of Sisyphe Pass Projection Level. Various rewards await at each level milestone.
   PL: Zdobyty Stopień Projekcji podnosi poziom Przepustki Lustra Sisyphe, zapewniając rozmaite nagrody na kolejnych progach.
134. [Samouczek i wskazówki [TutoMD08_P31_D3] — tekst] 획득 가능한 경험치는 매주 한정되어 있으며, 매주 목요일 오전 6시(KST)를 기준으로 초기화 됩니다.
   źródło: TutorialMirrorDungeon.json :: dataList[id=TutoMD08_P31_D3].content
   limit: do 150 znaków
   EN: There is a weekly cap to how much experience points can be earned. The weekly cap resets every Thursday 6AM (KST).
   PL: Tygodniowa ilość możliwych do zdobycia punktów jest ograniczona i resetuje się w każdy czwartek o 06:00 (KST).

## Samouczek i wskazówki: TutorialNewUpperSkillInfoUI
- plik gry: `TutorialNewUpperSkillInfoUI.json`

135. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_title_01] — tekst] 전투 화면 내 정보량 조절 설정
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_title_01].content
   limit: do 120 znaków
   EN: Adjusting Density of Information on Screen During Combat
   PL: Gęstość informacji na ekranie walki
136. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_01] — tekst] 전투 화면 오른쪽 상단에는 전투와 관련된 정보를 제어하는 버튼이 있습니다.\n\n버튼은 각각 최소 / 중간 / 최대 양의 정보를 표시합니다.
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_01].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On the top right of the in-battle screen, there is a button to adjust the amount of information displayed.\n\nThe three buttons will adjust the density to minimum, medium, and maximum, respectively.
   PL: W prawym górnym rogu ekranu walki znajduje się przycisk regulujący ilość wyświetlanych informacji.\n\nTrzy opcje ustawiają odpowiednio minimalną, średnią lub maksymalną ilość informacji.
137. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_title_02] — tekst] MAX
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_title_02].content
   limit: do 120 znaków
   EN: MAX
   PL: MAX
138. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_02] — tekst] 최대 정보 표시 설정입니다.\n\n게임 시작 시 최초 적용된 정보 표시 설정입니다.\n\n중간 정보 표시, 최소 정보 표시보다 더 많은 정보를 제공합니다.\n\n스킬에서 사용되는 키워드에 대한 정보를 표시해줍니다.
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_02].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The maximum information display configuration.\n\nThis is the default setting applied when first starting the game.\n\nMore information is shown compared to the other two settings.\n\nDetails on keywords used in skills are shown as well.
   PL: Konfiguracja maksymalnej ilości informacji.\n\nJest to ustawienie domyślne przy pierwszym uruchomieniu gry.\n\nPokazuje więcej szczegółów niż ustawienia średnie i minimalne.\n\nWyświetla także opisy słów kluczowych używanych w umiejętnościach.
139. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_title_03] — tekst] MID
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_title_03].content
   limit: do 120 znaków
   EN: MID
   PL: MID
140. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_03] — tekst] 중간 정보 표시 설정입니다.\n\n최대 정보 표시와 차이점은 스킬에서 사용되는 키워드에 대한 정보가 표시되지 않습니다.\n\n그 외에는 최대 정보 표시와 같은 정보를 표시합니다.
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_03].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The medium information display configuration.\n\nIn this setting, details on keywords used in skills will not be shown.\n\nOtherwise, it functions the same as the maximum setting.
   PL: Konfiguracja średniej ilości informacji.\n\nW odróżnieniu od ustawienia maksymalnego ukrywa opisy słów kluczowych w umiejętnościach.\n\nPoza tym wyświetla te same informacje co ustawienie maksymalne.
141. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_title_04] — tekst] MIN
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_title_04].content
   limit: do 120 znaków
   EN: MIN
   PL: MIN
142. [Samouczek i wskazówki [tutorial_upperSkillInfo_System_popup_04] — tekst] 최소 정보 표시 설정입니다.\n\n최대 정보 표시, 중간 정보 표시와 다르게 스킬의 효과와 키워드에 대한 정보를 표시하지 않습니다.
   źródło: TutorialNewUpperSkillInfoUI.json :: dataList[id=tutorial_upperSkillInfo_System_popup_04].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The minimum information display configuration.\n\nIn this setting, information on effects and keywords of skills will not be displayed.
   PL: Konfiguracja minimalnej ilości informacji.\n\nW odróżnieniu od ustawień MAX i MID nie wyświetla opisów efektów ani słów kluczowych umiejętności.

## Samouczek i wskazówki: TutorialPopUpDesc
- plik gry: `TutorialPopUpDesc.json`

143. [Samouczek i wskazówki [tutorial_main_low_0] — tekst] 메인메뉴 튜토리얼 1번째 설명
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_main_low_0].content
   limit: do 120 znaków
   EN: Main Menu Tutorial #1
   PL: Samouczek menu głównego #1
144. [Samouczek i wskazówki [tutorial_main_low_1] — tekst] 메인메뉴 튜토리얼 2번째 설명
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_main_low_1].content
   limit: do 120 znaków
   EN: Main Menu Tutorial #2
   PL: Samouczek menu głównego #2
145. [Samouczek i wskazówki [tutorial_main_low_2] — tekst] 메인메뉴 튜토리얼 3번째 설명
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_main_low_2].content
   limit: do 120 znaków
   EN: Main Menu Tutorial #3
   PL: Samouczek menu głównego #3
146. [Samouczek i wskazówki [tutorial_main_low_3] — tekst] 메인메뉴 튜토리얼 4번째 설명
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_main_low_3].content
   limit: do 120 znaków
   EN: Main Menu Tutorial #4
   PL: Samouczek menu głównego #4
147. [Samouczek i wskazówki [tutorial_main_low_4] — tekst] 메인메뉴 튜토리얼 5번째 설명
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_main_low_4].content
   limit: do 120 znaków
   EN: Main Menu Tutorial #5
   PL: Samouczek menu głównego #5
148. [Samouczek i wskazówki [tutorial_dungeon_formation_1] — tekst] 각 장의 마지막에는 저희가 조사해야하는 옛 L사의 지부, <던전>이 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_formation_1].content
   limit: do 150 znaków
   EN: During the final stretch of each chapter, you’ll be exploring a <Dungeon>, a branch facility of the former L Corp.
   PL: Na końcu każdego rozdziału czeka dawna placówka oddziału L Corp., którą musimy zbadać — „Loch”.
149. [Samouczek i wskazówki [tutorial_dungeon_formation_2] — tekst] 던전을 탐험할 수감자들의 인격을 설정해주세요.\n던전에 들어가면 편성을 변경할 수 없으니 신중히 선택하시기 바랍니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_formation_2].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Designate the Identities who will enter the Dungeon with you. You can’t adjust your team once inside, so choose wisely.
   PL: Wybierz Tożsamości Grzeszników, które wyruszą do Lochu.\nPo wejściu nie będzie można zmienić składu, więc dokonaj wyboru rozważnie.
150. [Samouczek i wskazówki [tutorial_dungeon_formation_start_button] — tekst] 편성을 끝내고, 이 곳의 입장 버튼을 눌러주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_formation_start_button].content
   limit: do 120 znaków
   EN: When you’re fully prepared, press the [Enter] button.
   PL: Po zakończeniu układania składu naciśnij tutaj przycisk [Wejdź].
151. [Samouczek i wskazówki [tutorial_dungeon_entry_0_title] — tekst] 던전의 구성
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_0_title].content
   limit: do 120 znaków
   EN: Dungeon Structure
   PL: Struktura Lochu
152. [Samouczek i wskazówki [tutorial_dungeon_entry_0] — tekst] 던전의 마지막 층의 마지막 방까지 도달하여 황금가지를 회수해야합니다.\n던전은 여러 개의 층으로 구성되어 있으며, 각 층마다 다양한 이벤트와 전투가 존재합니다.\n각 층의 마지막 방을 클리어하면 다음 층으로 넘어갈 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_0].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Your goal is to reach the last section of the bottom floor and retrieve the Golden Bough.\nThe Dungeon consists of multiple floors, each rife with events and encounters.\nClear the sector at the end of the floor to proceed to the next.
   PL: Twoim celem jest dotarcie do ostatniej komnaty najniższego piętra i odzyskanie Złotej Gałęzi.\nLoch składa się z wielu pięter pełnych wydarzeń oraz starć.\nUkończenie ostatniej komnaty piętra przenosi na kolejne piętro.
153. [Samouczek i wskazówki [tutorial_dungeon_entry_1_title] — tekst] 던전의 이동
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_1_title].content
   limit: do 120 znaków
   EN: Dungeon Navigation
   PL: Poruszanie się po Lochu
154. [Samouczek i wskazówki [tutorial_dungeon_entry_1] — tekst] 던전의 각 방에는 여러 갈래의 길이 연결되어있습니다.\n현재 위치한 방과 연결된 방 중 원하는 곳을 눌러 이동할 수 있습니다.\n한번 이동한 길도 다시 되돌아갈 수 있으니, 부담 없이 탐색할 방을 선택해주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Each sector is connected to one or more paths.\nYou can travel to adjacent sectors by selecting them.\nIt’s possible to retrace your steps, so feel free to explore where you want first.
   PL: Od każdej komnaty Lochu odchodzi jedna lub więcej ścieżek.\nKliknij dowolną komnatę połączoną z bieżącą, aby się do niej przemieścić.\nMożesz swobodnie wracać po własnych śladach, więc bez obaw wybieraj kierunek eksploracji.
155. [Samouczek i wskazówki [tutorial_dungeon_entry_2_title] — tekst] 피로도 누적
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_2_title].content
   limit: do 120 znaków
   EN: Sustained Damage
   PL: Kumulacja zmęczenia
156. [Samouczek i wskazówki [tutorial_dungeon_entry_2] — tekst] 던전 전투 후에는 수감자들의 체력, 정신력이 회복되지 않습니다.\n체력이 0이 된 수감자는 출전할 수 없으니 주의해주세요.\n체력과 정신력은 층의 세이브 포인트에서 회복할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_2].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sinners don’t heal after battle while in Dungeons.\nSinners with 0 HP are unable to participate, so keep track of their status.\nReaching a checkpoint will allow you to fully restore your Sinners.
   PL: Po walkach w Lochu PŻ ani PP Grzeszników nie odnawiają się samoczynnie.\nGrzesznik z 0 PŻ nie może walczyć, więc uważnie śledź stan drużyny.\nPŻ oraz PP odnowisz w punktach zapisu na piętrze.
157. [Samouczek i wskazówki [tutorial_dungeon_entry_3_title] — tekst] 패배와 재도전
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_3_title].content
   limit: do 120 znaków
   EN: Defeats and Retries
   PL: Porażka i ponowienie
158. [Samouczek i wskazówki [tutorial_dungeon_entry_3] — tekst] 전투에서 패배할 경우, 전투는 종료되고 남아있는 수감자가 있다면 다시 도전할 수 있습니다. 이때, 이전의 전투 내용은 초기화됩니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_entry_3].content
   limit: do 150 znaków
   EN: After losing a battle, you can reattempt it from the start with whatever living Sinners remain on your full team.
   PL: W razie porażki walka dobiega końca, a jeśli pozostali przy życiu inni Grzesznicy, możesz spróbować ponownie od początku starcia.
159. [Samouczek i wskazówki [tutorial_dungeon_saveroom] — tekst] 던전의 곳곳에는 세이브 포인트가 있습니다.\n세이브 포인트로 이동하면 수감자들의 체력과 정신력이 전부 회복됩니다.\n던전 진행 중 모든 수감자가 사망하면 세이브 포인트에서 부활합니다.\n단, 이 경우 세이브 포인트 이후에 진행한 방의 진행 상태가 초기화되니 주의하세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_saveroom].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can find checkpoints as you explore the Dungeon.\nYour Sinners will fully heal their HP and reset their SP upon reaching one.\nWhen all of your Sinners die, you’ll be brought back to your last checkpoint.\nDo note that progress made beyond said checkpoint will be reset as well.
   PL: W różnych miejscach Lochu znajdują się punkty zapisu.\nWejście do punktu zapisu w pełni odnawia PŻ i resetuje PP Grzeszników.\nGdy zginą wszyscy Grzesznicy, drużyna odrodzi się w ostatnim punkcie zapisu.\nPamiętaj jednak, że postępy poczynione za tym punktem zapisu zostaną zresetowane.
160. [Samouczek i wskazówki [tutorial_dungeon_ab_part_title] — tekst] 환상체 부위
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_part_title].content
   limit: do 120 znaków
   EN: Abnormality Parts
   PL: Części Anomalii
161. [Samouczek i wskazówki [tutorial_dungeon_ab_part_1] — tekst] 모든 환상체는 부위를 1개 이상 가지고 있습니다.\n환상체는 부위마다 체력, 내성, 사용하는 스킬이 달라집니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_part_1].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abnormalities consist of at least one body part.\nEach part has its own slots, as well as individual skills.
   PL: Każda Anomalia posiada co najmniej 1 część.\nPoszczególne części różnią się PŻ, odpornościami oraz używanymi umiejętnościami.
162. [Samouczek i wskazówki [tutorial_dungeon_ab_speed_title] — tekst] 환상체 속도
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_speed_title].content
   limit: do 120 znaków
   EN: Abnormality Speed
   PL: Szybkość Anomalii
163. [Samouczek i wskazówki [tutorial_dungeon_ab_speed_1] — tekst] 환상체에게는 부위마다 슬롯이 존재하며 속도가 있습니다.\n환상체의 속도는 행동 순서를 결정하고, 환상체의 공격 타겟을 바꿀 수 있는 조건이 됩니다.\n환상체보다 <속도가 빠른> 아군의 스킬을 환상체의 스킬 슬롯에 드래그하면, <합>이 발생하여 환상체의 공격 타겟을 변경할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_speed_1].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Each Abnormality part has slots with the skills it intends to use.\nThe parts also have Speed values that determine their order of action.\nIf you target a skill slot with a Sinner whose Speed is higher, they can redirect that attack and Clash with it.
   PL: Każda część Anomalii posiada własne sloty oraz Szybkość.\nSzybkość części decyduje o kolejności działań i o możliwości przekierowania ataku.\nPrzeciągnięcie umiejętności sojusznika o „wyższej Szybkości” na slot umiejętności Anomalii wywołuje „Starcie” i zmienia cel jej ataku.
164. [Samouczek i wskazówki [tutorial_dungeon_ab_destroypart_title] — tekst] 부위 파괴
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_destroypart_title].content
   limit: do 120 znaków
   EN: Breaking Parts
   PL: Zniszczenie części
165. [Samouczek i wskazówki [tutorial_dungeon_ab_destroypart_1] — tekst] 환상체 부위는 체력이 0이 되면  <부위파괴>가 됩니다.\n부위 파괴가 되면 해당 부위가 가지고 있는 모든 물리 내성이 취약 상태가 됩니다.\n부위에 따라 파괴 시 스킬을 사용하지 못하거나, 패시브가 사라지는 경우도 있습니다.\n부위 파괴 시 환상체에 따라 흉폭해지거나 파괴된 부위가 재생할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_destroypart_1].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the HP of a body part is reduced to 0, it is <Broken>.\nA broken part becomes vulnerable to all physical attack types.\nSome parts may lose certain skills or passives after breaking.\nDo note that some Abnormalities have regenerative parts, as well as that breaking certain ones may instead enrage an Abnormality.
   PL: Gdy PŻ części Anomalii spadną do 0, następuje „Zniszczenie części”.\nWszystkie odporności fizyczne zniszczonej części zmieniają się na Podatność (Fatal).\nZależnie od części jej zniszczenie może zablokować niektóre umiejętności lub usunąć pasywki.\nNiektóre Anomalie po utracie części wpadają w szał albo regenerują zniszczoną część.
166. [Samouczek i wskazówki [tutorial_dungeon_ab_guide_title] — tekst] 환상체 도감
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_guide_title].content
   limit: do 120 znaków
   EN: The Abnormality Encyclopedia
   PL: Kompendium Anomalii
167. [Samouczek i wskazówki [tutorial_dungeon_ab_guide_1] — tekst] 환상체 도감에는 부위마다 정보가 기록되어있습니다.\n처음 만난 환상체의 도감은 미완성 상태입니다.\n미완성 상태의 도감은 환상체를 상대하면서 점차 완성됩니다.\n환상체는 여러 번 조우하고 전투할수록 관찰 단계가 증가합니다.\n관찰 단계가 높아질수록 환상체에게 입히는 피해량이 증가합니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_guide_1].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Encyclopedia records information on Abnormalities and their parts.\nBy nature, the Encyclopedia starts out incomplete.\nThe more you fight an Abnormality, the more its entry will be penned.\nAfter enough encounters, its Observation Level will go up.\nHigher Observation Levels can increase the damage you deal.
   PL: W Kompendium Anomalii zapisywane są informacje o jej poszczególnych częściach.\nPrzy pierwszym spotkaniu wpis w Kompendium jest niepełny\ni uzupełnia się stopniowo w miarę kolejnych walk z Anomalią.\nWielokrotne spotkania i walki z Anomalią podnoszą jej Poziom Obserwacji,\na wyższy Poziom Obserwacji zwiększa zadawane jej obrażenia.
168. [Samouczek i wskazówki [tutorial_dungeon_ab_selection_title] — tekst] 선택지
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_selection_title].content
   limit: do 120 znaków
   EN: Checks
   PL: Wydarzenia wyboru
169. [Samouczek i wskazówki [tutorial_dungeon_ab_selection_1] — tekst] 환상체 선택지는 선택지마다 요구하는 죄악 속성과 수치가 존재합니다.\n선택지에 맞는 속성을 가진 수감자를 골라야 성공 확률이 높아집니다.\n선택지에서 선택된 내용과 결과에 따라 환상체의 반응이 달라집니다.\n판정에 성공하면 긍정적인 효과를 그렇지 못하면 부정적인 효과를 얻습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_ab_selection_1].content
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Checks presented by Abnormalities have a required Sin Affinity and a threshold to pass.\nChoose a Sinner with the right affinity for a higher likelihood of success.\nThe Abnormality will react differently depending on your choice and its results.\nPassing the check usually gives you benefits, and failing it burdens you with disadvantages.
   PL: Każda opcja wyboru w starciu z Anomalią wymaga określonego grzechu oraz progu wartości.\nWskazanie Grzesznika z pasującym grzechem zwiększa szansę powodzenia.\nReakcja Anomalii zależy od wybranej opcji oraz wyniku testu:\nsukces zapewnia zazwyczaj korzyści, a porażka nakłada negatywne efekty.
170. [Samouczek i wskazówki [tutorial_dungeon_saveroom_title] — tekst] 세이브 포인트
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_saveroom_title].content
   limit: do 120 znaków
   EN: Checkpoints
   PL: Punkty zapisu
171. [Samouczek i wskazówki [tutorial_dungeon_saveroom_1] — tekst] 던전 곳곳에는 세이브 포인트가 존재합니다.\n세이브 포인트는 도착한 수감자들의 체력과 정신력이 전부 회복되며, 진행 상황이 저장됩니다.\n던전 진행 중 모든 수감자가 사망하면 가장 최근에 지나온 세이브 포인트에서 부활하게 됩니다.\n단, 부활하게 된다면 해당 세이브 포인트 이후의 진행 상태는 초기화됩니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_dungeon_saveroom_1].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can find checkpoints as you explore the Dungeon.\nYour Sinners will fully heal their HP and reset their SP upon reaching one.\nWhen all of your Sinners die, you’ll be brought back to your last checkpoint.\nDo note that progress made beyond said checkpoint will be reset as well.
   PL: W różnych miejscach Lochu znajdują się punkty zapisu.\nDotarcie do punktu zapisu w pełni odnawia PŻ i PP Grzeszników oraz zapisuje postęp.\nJeśli wszyscy Grzesznicy zginą, odrodzą się w ostatnio odwiedzonym punkcie zapisu,\njednak cały postęp za tym punktem zapisu zostanie wówczas zresetowany.
172. [Samouczek i wskazówki [tutorial_skill_command_title] — tekst] 공격 스킬 입력
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_skill_command_title].content
   limit: do 120 znaków
   EN: Ordering Attacks
   PL: Wydawanie rozkazów ataku
173. [Samouczek i wskazówki [tutorial_skill_command_1] — tekst] 전투가 시작되기 위해서는 “모든 인격의 행동”이 결정되어야 합니다.\n일반 전투에서는 왼쪽 기어부터 오른쪽 기어까지 드래그하며 행동을 결정해 전투를 진행 할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_skill_command_1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For the combat phase to begin, every Sinner must be given an order.\nIn regular encounters, you select skills by chaining them across the Dashboard, from the left gear to the right one.
   PL: Aby walka mogła się rozpocząć, trzeba wyznaczyć działanie „każdej Tożsamości”.\nW zwykłych starciach przeciągnij łańcuch od lewej zębatki do prawej na panelu dowodzenia, aby wydać rozkazy.
174. [Samouczek i wskazówki [tutorial_skill_coin_title] — tekst] 스킬 코인
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_skill_coin_title].content
   limit: do 120 znaków
   EN: Skill Coins
   PL: Monety umiejętności
175. [Samouczek i wskazówki [tutorial_skill_coin_1] — tekst] 스킬에는 코인이 1개 이상 존재하며, 코인 수는 공격 횟수를 의미합니다.\n코인은 앞면과 뒷면이 있으며, 면에 따라 스킬 위력을 감소하거나 증가시킵니다.\n다음 코인이 있다면 감소하거나 증가한 위력은 유지됩니다.\n코인 종류에는 더하기 코인, 빼기 코인이 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_skill_coin_1].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Each skill consists of at least 1 Coin, which represents the number of attacks it can perform.\nThe Coin is tossed when the attack is initiated, and its outcome may boost or reduce the Power of the skill.\nThis modifier carries over to the next Coin if there is one.\nThe two types of Coins are plus (+) and minus (-).
   PL: Każda umiejętność ma co najmniej 1 Monetę, a liczba Monet oznacza liczbę ciosów.\nMoneta ma awers i rewers — wynik rzutu zwiększa lub zmniejsza Moc umiejętności.\nPrzy kolejnych Monetach zmodyfikowana Moc przechodzi na następny rzut.\nWyróżniamy Monety Dodatnie (+) oraz Monety Ujemne (-).
176. [Samouczek i wskazówki [tutorial_adding_slot_title] — tekst] 슬롯 추가
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_adding_slot_title].content
   limit: do 120 znaków
   EN: Added Slots
   PL: Dodatkowe sloty
177. [Samouczek i wskazówki [tutorial_adding_slot_1] — tekst] 행동 슬롯은 최대 12개로 매 턴마다 전투에 참여한 인격의 <흐트러짐>, <패닉>, <에고 침식>상태에 관계 없이 전투 편성 순서에 따라 스킬 슬롯이 추가됩니다.\n이전 턴에 증가한 인원이 있다면, 제외하고 다른 인격의 슬롯이 무작위로 증가합니다.\n모든 인격이 한 번씩 증가했다면, 처음과 같이 무작위로 슬롯이 증가합니다.\n전투가 진행됨에 따라 적 슬롯도 증가합니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_adding_slot_1].content
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On the Dashboard, a new column is added for one Sinner at a time each turn in the order they were deployed, up to a total of 12.\nSinners that have gained one will not receive another until all of their allies gain one of their own.\nOnce every Sinner has an additional column, they are all once again eligible.\nEnemies also gain additional slots as the battle goes on.
   PL: Liczba slotów akcji wynosi maksymalnie 12; w każdej turze uczestnicy otrzymują dodatkowy slot zgodnie z kolejnością rozstawienia — niezależnie od „Oszołomienia”, „Paniki” czy „Korozji E.G.O”.\nPomijani są ci, którzy zyskali już slot w poprzednich turach, dopóki każdy uczestnik nie otrzyma po jednym.\nGdy wszyscy zyskają po slocie, cykl naliczania zaczyna się od nowa.\nW miarę trwania walki rośnie również liczba slotów wrogów.
178. [Samouczek i wskazówki [tutorial_passive_title] — tekst] 패시브
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_passive_title].content
   limit: do 120 znaków
   EN: Passives
   PL: Pasywki
179. [Samouczek i wskazówki [tutorial_passive_1] — tekst] 전투 패시브와 서포트 패시브는 “발동에 필요한 속성 스킬”이 연결되어야 발동됩니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_passive_1].content
   limit: do 120 znaków
   EN: Passive abilities activate when skills of certain Affinities are chained.
   PL: Pasywki bojowe oraz pasywki wsparcia aktywują się po połączeniu „umiejętności wymaganych grzechów”.
180. [Samouczek i wskazówki [tutorial_ab_assign_skill_title] — tekst] 환상체전 스킬 입력
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_ab_assign_skill_title].content
   limit: do 120 znaków
   EN: Attacking Abnormalities
   PL: Wybór celów w walce z Anomalią
181. [Samouczek i wskazówki [tutorial_ab_assign_skill_1] — tekst] 아군 스킬을 클릭하여 환상체 머리 위에 위치한 스킬 슬롯에 넣으면 타겟 설정이 가능해집니다.\n스킬 슬롯마다 타겟되는 부위는 다릅니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=tutorial_ab_assign_skill_1].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select a Sinner’s skill, then drag it to one of the Abnormality’s slots to designate the target.\nNote that each skill slot represents a different body part.
   PL: Kliknij umiejętność sojusznika i przeciągnij ją na slot umiejętności nad głową Anomalii, aby wyznaczyć cel.\nKażdy slot umiejętności odpowiada określonej części ciała.
182. [Samouczek i wskazówki [ui_tutorial_2_1] — tekst] 모든 수감자가 전투에 참여하는 방법도 있겠지만, 이 많은 인원들을 동시에 통솔하고 명령을 내리는 일이 결코 쉬운 일은 아닐 거예요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_1].content
   limit: do 160 znaków
   EN: You could send every Sinner into battle at once, yes. But commanding so many personnel at once will not be an easy task.
   PL: Można by wysłać do boju wszystkich Grzeszników naraz, lecz jednoczesne dowodzenie tak licznym oddziałem nie byłoby łatwym zadaniem.
183. [Samouczek i wskazówki [ui_tutorial_2_2] — tekst] 그렇기 때문에 각 전장의 상황에 따라 통솔하기에 적합한 인원 수를 안내해 드린답니다.\n이 전장에서는 5명의 인원이 효과적이겠네요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_2].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Therefore, I will inform you of the appropriate number of participants depending on the particularities of each battle.\nFor this occasion, 5 Sinners will make an appropriate force.
   PL: Dlatego zależnie od sytuacji na polu bitwy wskażę ci optymalną liczbę uczestników.\nW tym starciu najlepiej sprawdzi się 5 Grzeszników.
184. [Samouczek i wskazówki [ui_tutorial_2_3] — tekst] 전투에 참여할 5명의 수감자를 선택해주세요.\n수감자 패널의 하단을 눌러 이번 전투에 참여할 수감자를 선택할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_3].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select 5 Sinners you would like to Deploy for this battle.\nSelect the lower half of each Sinner's cards to Deploy them.
   PL: Wybierz 5 Grzeszników do tej walki.\nKliknij dolną część karty Grzesznika, aby wystawić go do starcia.
185. [Samouczek i wskazówki [ui_tutorial_2_4] — tekst] 먼저 이상 수감자를 선택해주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_4].content
   limit: do 120 znaków
   EN: First, select Sinner Yi Sang.
   PL: Najpierw wybierz Grzesznika Yi Sanga.
186. [Samouczek i wskazówki [ui_tutorial_2_5] — tekst] 정확합니다.\n이어서 전투에 참가할 수감자를 차례대로 선택해주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_5].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Well done.\nSelect the rest of the Sinners you would like to Deploy for this encounter.
   PL: Doskonale.\nTeraz wybierz po kolei pozostałych Grzeszników do walki.
187. [Samouczek i wskazówki [ui_tutorial_2_6] — tekst] 전투 시작 버튼을 누르면 선택한 수감자들과 함께 전투를 진행합니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_2_6].content
   limit: do 120 znaków
   EN: Select 'To Battle' to begin the Encounter with the currently Deployed Sinners.
   PL: Naciśnij przycisk rozpoczęcia walki, aby wyruszyć do boju z wybranymi Grzesznikami.
188. [Samouczek i wskazówki [ui_tutorial_3_1] — tekst] 이전 전투에 참여한 수감자의 기록이 남아있기 때문에, 번거롭게 매번 수감자들을 선택하지는 않으셔도 됩니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_3_1].content
   limit: do 270 znaków
   EN: The Sinners you have deployed in the last encounter will automatically be selected for the next, saving you the trouble of selecting them again. Feel free to change them before entering the battle, however.
   PL: Skład z poprzedniego starcia zostaje zapamiętany, więc nie musisz za każdym razem wybierać Grzeszników od nowa.
189. [Samouczek i wskazówki [ui_tutorial_3_2] — tekst] 전투 시작 버튼을 눌러주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_3_2].content
   limit: do 120 znaków
   EN: Select the 'To Battle' button.
   PL: Naciśnij przycisk rozpoczęcia walki.
190. [Samouczek i wskazówki [ui_tutorial_4_1] — tekst] 메피스토펠레스에는 추출이라는 기능이 있습니다.\n추출을 통해 다양한 인격과 E.G.O를 수집할 수 있죠.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of Mephistopheles' various functions is 'Extraction'.\nYou can collect various Identities and E.G.O from here.
   PL: Mefistofeles dysponuje funkcją zwaną Ekstrakcją.\nDzięki Ekstrakcji możesz zdobywać rozmaite Tożsamości oraz E.G.O.
191. [Samouczek i wskazówki [ui_tutorial_4_2] — tekst] 추출 버튼을 눌러주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_2].content
   limit: do 120 znaków
   EN: Select the Extract button.
   PL: Naciśnij przycisk Ekstrakcji.
192. [Samouczek i wskazówki [ui_tutorial_4_3] — tekst] 새로운 인격을 얻으셨군요.\n추출을 이용해 새로운 인격과 E.G.O를 모은다면, 전력 향상에 큰 도움이 될 것입니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_3].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You have acquired a new Identity.\nCollecting new Identities and E.G.O will be contributive to improving our combat performance.
   PL: Zdobyto nową Tożsamość.\nPozyskiwanie nowych Tożsamości i E.G.O przez Ekstrakcję wydatnie wzmocni naszą siłę bojową.
193. [Samouczek i wskazówki [ui_tutorial_4_4] — tekst] 이제 다시 전투로 이동해주세요.\n전투는 운전석 버튼을 통해 입장할 수 있습니다.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now, let us return to battle.\nBattles can be accessed via the 'Drive' window.
   PL: Wróćmy teraz do walki.\nDo starć przejdziesz za pomocą przycisku Jazdy.
194. [Samouczek i wskazówki [ui_tutorial_4_5] — tekst] 수감자 패널의 상단을 눌러, 수감자의 인격을 교체할 수 있어요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_5].content
   limit: do 120 znaków
   EN: Select the top part of the Sinner cards to swap them out for a different Identity.
   PL: Kliknij górną część karty Grzesznika, aby zmienić jego Tożsamość.
195. [Samouczek i wskazówki [ui_tutorial_4_6] — tekst] 이스마엘 수감자를 선택해주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_6].content
   limit: do 120 znaków
   EN: Select Sinner Ishmael, if you will.
   PL: Wybierz Grzeszniczkę Ishmael.
196. [Samouczek i wskazówki [ui_tutorial_4_7] — tekst] 이곳에서 추출로 획득한 다른 인격들 중 하나를 선택해, 전투에 활용할 수 있습니다.\n새롭게 얻은 이스마엘의 인격을 선택해주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_7].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: From this menu, you may select one of the Identities you have Extracted to deploy them into battle.\nPlease select the newly acquired Identity for Ishmael.
   PL: Tutaj możesz wybrać jedną ze zdobytych w Ekstrakcji Tożsamości, aby wystawić ją do boju.\nWybierz nowo zdobytą Tożsamość Ishmael.
197. [Samouczek i wskazówki [ui_tutorial_4_8] — tekst] 잘 하셨어요. 각 전투 상황에 유리한 인격을 편성하는 것이 승리의 지름길이랍니다.\n이제 전투 시작 버튼을 눌러주세요.
   źródło: TutorialPopUpDesc.json :: dataList[id=ui_tutorial_4_8].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Good work. Selecting Identities appropriate for the particularities of each battle is the path to victory.\nNow, select the 'To Battle' button.
   PL: Świetna robota. Dobieranie Tożsamości dopasowanych do specyfiki starcia to najkrótsza droga do zwycięstwa.\nNaciśnij teraz przycisk rozpoczęcia walki.

## Samouczek i wskazówki: TutorialRenewalDesc
- plik gry: `TutorialRenewalDesc.json`

198. [Samouczek i wskazówki [tuto_00_01_01_01] — tekst] 지금부터 전투 진행 방법을 알려드리겠습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_01].content
   limit: do 120 znaków
   EN: Let us begin by learning the basics of combat.
   PL: Wyjaśnię teraz, jak przebiega walka.
199. [Samouczek i wskazówki [tuto_00_01_01_02] — tekst] 먼저 <color=#f8c200>조작 패널<color=#ebcaa2>을 확인해주세요.\n\n<color=#f8c200>조작 패널<color=#ebcaa2>을 통해 수감자들에게 명령을 내릴 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_02].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Please direct your attention to the <color=#f8c200>Dashboard<color=#ebcaa2> here.\n\nYou will be using the <color=#f8c200>Dashboard<color=#ebcaa2> to relay your commands to the Sinners.
   PL: Spójrz najpierw na <color=#f8c200>panel dowodzenia<color=#ebcaa2>.\n\nZa pomocą <color=#f8c200>panelu dowodzenia<color=#ebcaa2> wydajesz rozkazy Grzesznikom.
200. [Samouczek i wskazówki [tuto_00_01_01_03] — tekst] <color=#f8c200>조작 패널<color=#ebcaa2> 위에는 수감자가 사용하는 <color=#f8c200>스킬<color=#ebcaa2>이 배치됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: You will find each Sinner's <color=#f8c200>Skills<color=#ebcaa2> on the <color=#f8c200>Dashboard<color=#ebcaa2>.
   PL: Na <color=#f8c200>panelu dowodzenia<color=#ebcaa2> rozmieszczone są <color=#f8c200>umiejętności<color=#ebcaa2> Grzeszników.
201. [Samouczek i wskazówki [tuto_00_01_01_04] — tekst] 조작 방법은 간단합니다. <color=#f8c200>왼쪽부터 오른쪽까지 스킬을 차례대로 연결<color=#ebcaa2>하면 전투가 진행됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_04].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: The control scheme is simple. <color=#f8c200>Simply drag from the left end of the Dashboard to the right end to chain the Skills<color=#ebcaa2>, and you are ready to enter the combat phase.
   PL: Sterowanie jest proste: <color=#f8c200>połącz umiejętności po kolei od lewej do prawej<color=#ebcaa2>, aby rozpocząć walkę.
202. [Samouczek i wskazówki [tuto_00_01_01_05] — tekst] 그럼 직접 명령을 내려보도록 하죠.\n\n조작 패널의 <color=#f8c200>왼쪽 기어<color=#ebcaa2>를 눌러보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_05].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Allow me to guide your hand.\n\nPress and hold the <color=#f8c200>gear on the left<color=#ebcaa2> on the Dashboard to grab the chain.
   PL: Wydajmy więc pierwszy rozkaz.\n\nNaciśnij i przytrzymaj <color=#f8c200>lewą zębatkę<color=#ebcaa2> panelu dowodzenia.
203. [Samouczek i wskazówki [tuto_00_01_01_06] — tekst] 왼쪽 기어를 누른 상태에서 <color=#f8c200>연결선을 따라 스킬을 차례대로 연결<color=#ebcaa2>해보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_06].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Then, while you're holding the chain from the left gear, <color=#f8c200>connect the Skills from left to right, along the guiding line.<color=#ebcaa2>
   PL: Trzymając lewą zębatkę, <color=#f8c200>połącz po kolei umiejętności wzdłuż linii pomocniczej<color=#ebcaa2>.
204. [Samouczek i wskazówki [tuto_00_01_01_07] — tekst] 잘 하셨어요. 스킬을 모두 연결했으면 <color=#f8c200>오른쪽 기어<color=#ebcaa2>를 눌러 전투를 시작해보죠.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_01_07].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Well done. Now that Skills for all Sinners have been chained, you may press the <color=#f8c200>gear on the right<color=#ebcaa2> to start the combat phase.
   PL: Doskonale. Gdy wszystkie umiejętności są połączone, naciśnij <color=#f8c200>prawą zębatkę<color=#ebcaa2>, aby rozpocząć walkę.
205. [Samouczek i wskazówki [tuto_00_01_02_01] — tekst] 이렇게 관리자님의 지시에 따라 전투가 진행됩니다.\n\n다시 한 번 해보시겠어요?
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_02_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: And that is how you, the manager, issue your orders.\n\nLet us try that again.
   PL: Właśnie w ten sposób walka toczy się pod dyktando rozkazów Kierownika.\n\nSpróbujemy jeszcze raz?
206. [Samouczek i wskazówki [tuto_00_01_02_02] — tekst] 조작 패널에서 왼쪽부터 오른쪽까지 스킬을 차례대로 연결해서 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_02_02].content
   limit: do 170 znaków
   EN: Look at the Dashboard, grab the chain from the left gear, and connect the Skills along the guiding line to command us to use them.
   PL: Połącz umiejętności na panelu dowodzenia po kolei od lewej do prawej, aby wydać rozkaz.
207. [Samouczek i wskazówki [tuto_00_01_02_03_title] — tekst] 조작 패널
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_02_03_title].content
   limit: do 120 znaków
   EN: The Dashboard
   PL: Panel dowodzenia
208. [Samouczek i wskazówki [tuto_00_01_02_04] — tekst] 조작 패널을 통해 전투를 진행할 수 있습니다.\n\n왼쪽 기어를 눌러 스킬을 차례대로 이어 오른쪽 기어까지 연결하면 전투가 진행됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_01_02_04].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use the Dashboard to issue commands to your Sinners in combat.\nStart the combat phase by following these steps:\n\n1) Grab and drag the chain from the left gear.\n2) Thread it through the Skills you want to use.\n3) Connect the chain to, or select, the right gear.
   PL: Panel dowodzenia służy do kierowania walką.\n\nChwyć lewą zębatkę, przeprowadź łańcuch przez kolejne umiejętności aż do prawej zębatki, aby rozpocząć starcie.
209. [Samouczek i wskazówki [tuto_00_02_01_01] — tekst] 아군과 적군의 머리 위에 있는 칠각형 아이콘을\n<color=#f8c200>스킬 슬롯<color=#ebcaa2>이라고 합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_01].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: These seven-sided icons floating above both the allies and enemies' heads are called <color=#f8c200>Skill Slots<color=#ebcaa2>.
   PL: Siedmiokątne ikony nad głowami sojuszników i wrogów\nnazywamy <color=#f8c200>slotami umiejętności<color=#ebcaa2>.
210. [Samouczek i wskazówki [tuto_00_02_01_02] — tekst] 지금은 관리자님이 명령을 내려주시기 전이라\n아군의 스킬 슬롯이 비워져있는 상태입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_02].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Because you haven’t issued a command by chaining Skills yet, the allied Skill Slots are currently empty.
   PL: Ponieważ nie wydano jeszcze rozkazu,\nsloty umiejętności sojuszników są na razie puste.
211. [Samouczek i wskazówki [tuto_00_02_01_03] — tekst] 조작 패널의 첫 번째에 있는\n스킬 중 하나를 골라 연결해보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_03].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Grab the chain from the left gear and chain it to one of these two leftmost Skills on the Dashboard.
   PL: Wybierz i połącz jedną z umiejętności\nw pierwszej kolumnie panelu dowodzenia.
212. [Samouczek i wskazówki [tuto_00_02_01_04] — tekst] 관리자님이 선택한 스킬이 스킬 슬롯에 장착됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_04].content
   limit: do 120 znaków
   EN: As you can see, the Skill you just chained has been equipped to the Skill Slot.
   PL: Wybrana przez Kierownika umiejętność zostaje umieszczona w slocie umiejętności.
213. [Samouczek i wskazówki [tuto_00_02_01_05_title] — tekst] 스킬 슬롯
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_05_title].content
   limit: do 120 znaków
   EN: Skill Slots
   PL: Sloty umiejętności
214. [Samouczek i wskazówki [tuto_00_02_01_06] — tekst] 장착된 스킬은 수감자 상단의 스킬 슬롯에 표시됩니다.\n\n전투가 시작되면 수감자들은 자신의 스킬 슬롯에 장착된 스킬을 사용하여 전투를 진행합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_06].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Equipped Skills are displayed on the Skill Slots floating above each Sinner’s head.\n\nWhen the combat phase begins, each Sinner will engage in battle using the Skills equipped in their Skill Slots.
   PL: Wybrane umiejętności pojawiają się w slotach umiejętności nad głowami Grzeszników.\n\nPo rozpoczęciu fazy walki Grzesznicy ruszają do boju, używając umiejętności ze swoich slotów.
215. [Samouczek i wskazówki [tuto_00_02_01_07] — tekst] 조작 패널에 있는 스킬을 끝까지 연결해서 아군의 모든 슬롯에 장착해보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_07].content
   limit: do 150 znaków
   EN: Drag from left to right on the Dashboard to equip every Sinner with one of the Skills on their respective columns.
   PL: Połącz umiejętności na panelu dowodzenia aż do końca, aby obsadzić wszystkie sloty sojuszników.
216. [Samouczek i wskazówki [tuto_00_02_01_08] — tekst] 잘 하셨어요. 이 상태에서 명령을 내려주시면 자신의 스킬 슬롯에 장착된 스킬을 사용해 전투를 시작합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_01_08].content
   limit: do 200 znaków
   EN: Well done. Now, select the gear on the right to issue your command, and the Sinners will enter the combat phase, using the Skills you’ve equipped for them.
   PL: Świetnie. Wydanie rozkazu w tym stanie sprawi, że Grzesznicy rozpoczną walkę przy użyciu umiejętności ze swoich slotów.
217. [Samouczek i wskazówki [tuto_00_02_02_01] — tekst] 수감자와 적이 서로 공격 스킬을 사용하면 <color=#f8c200><합><color=#ebcaa2>이 발생합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: A <color=#f8c200><Clash><color=#ebcaa2> occurs when the Sinner and their target both use Attack Skills against each other.
   PL: Gdy Grzesznik i wróg użyją przeciw sobie umiejętności ataku, dochodzi do <color=#f8c200>„Starcia”<color=#ebcaa2>.
218. [Samouczek i wskazówki [tuto_00_02_02_02] — tekst] <color=#f8c200><합><color=#ebcaa2>을 진행하면 각 캐릭터가 사용한 스킬에 따라 <color=#f8c200>위력<color=#ebcaa2>이 결정됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: In a <color=#f8c200><Clash><color=#ebcaa2>, their <color=#f8c200>Power<color=#ebcaa2> is determined primarily by the Skill they are using to Clash.
   PL: Podczas <color=#f8c200>„Starcia”<color=#ebcaa2> na podstawie użytych umiejętności wyznaczana jest <color=#f8c200>Moc<color=#ebcaa2> obu stron.
219. [Samouczek i wskazówki [tuto_00_02_02_03] — tekst] <color=#f8c200><합><color=#ebcaa2>은 두 스킬 중 <color=#f8c200>위력<color=#ebcaa2>이 큰 쪽이 승리합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: And in this <color=#f8c200><Clash><color=#ebcaa2> between two Skills, the Skill with the higher <color=#f8c200>Power<color=#ebcaa2> wins.
   PL: <color=#f8c200>„Starcie”<color=#ebcaa2> wygrywa ta z dwóch umiejętności, która ma wyższą <color=#f8c200>Moc<color=#ebcaa2>.
220. [Samouczek i wskazówki [tuto_00_02_02_04] — tekst] <color=#f8c200>패배<color=#ebcaa2>한 쪽은 스킬 <color=#f8c200>코인 한 개가 파괴<color=#ebcaa2>됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Pay attention to the enemy's Coins. When a Skill <color=#f8c200>loses<color=#ebcaa2> a Clash, <color=#f8c200>it will lose a Coin<color=#ebcaa2>.
   PL: Po stronie <color=#f8c200>przegranej<color=#ebcaa2> niszczona jest <color=#f8c200>jedna Moneta umiejętności<color=#ebcaa2>.
221. [Samouczek i wskazówki [tuto_00_02_02_05] — tekst] <color=#f8c200>스킬 코인<color=#ebcaa2>이 남아있다면, <color=#f8c200>모두 파괴<color=#ebcaa2>되기 전까지 코인을 다시 굴리며 <color=#f8c200><합><color=#ebcaa2>을 진행합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_05].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Even if a Skill loses a Clash, as long as it has remaining <color=#f8c200>Skill Coins<color=#ebcaa2>, the two Skills will continue to flip their Coins and <color=#f8c200><Clash><color=#ebcaa2> until <color=#f8c200>one of them loses all Coins<color=#ebcaa2>.
   PL: Dopóki obu stronom pozostają <color=#f8c200>Monety umiejętności<color=#ebcaa2>, rzucają nimi ponownie i toczą <color=#f8c200>„Starcie”<color=#ebcaa2> aż do <color=#f8c200>zniszczenia wszystkich Monet<color=#ebcaa2> jednej ze stron.
222. [Samouczek i wskazówki [tuto_00_02_02_06] — tekst] <color=#f8c200><합><color=#ebcaa2> 진행 중 모든 코인이 파괴된 쪽은 <color=#f8c200><합><color=#ebcaa2>에서 패배하며, <color=#f8c200><합><color=#ebcaa2>에서 <color=#f8c200>승리한 캐릭터가 공격권<color=#ebcaa2>을 가집니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_02_06].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The Skill that lost all of its Coins in this <color=#f8c200><Clash><color=#ebcaa2> will conclusively lose the <color=#f8c200><Clash><color=#ebcaa2>.\nThis means that the <color=#f8c200>unit that won<color=#ebcaa2> the <color=#f8c200><Clash><color=#ebcaa2> gets to attack, while the unit that lost does not.
   PL: Strona, która w trakcie <color=#f8c200>„Starcia”<color=#ebcaa2> straci wszystkie Monety, przegrywa <color=#f8c200>„Starcie”<color=#ebcaa2>,\nnatomiast <color=#f8c200>zwycięzca<color=#ebcaa2> <color=#f8c200>„Starcia”<color=#ebcaa2> wyprowadza atak.
223. [Samouczek i wskazówki [tuto_00_02_03_01] — tekst] 이번에는 <color=#f8c200><합><color=#ebcaa2>의 승패를 결정하는 <color=#f8c200>위력<color=#ebcaa2>이 정확히 어떻게 결정되는지 알려드리겠습니다.\n\n다시 한 번 전투 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_01].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Let's see how <color=#f8c200>Power<color=#ebcaa2>, which determines the outcome of a <color=#f8c200><Clash><color=#ebcaa2>, is calculated.\n\nPlease issue a command.
   PL: Sprawdźmy teraz dokładnie, jak wyliczana jest <color=#f8c200>Moc<color=#ebcaa2> decydująca o wyniku <color=#f8c200>„Starcia”<color=#ebcaa2>.\n\nWydaj ponownie rozkaz do walki.
224. [Samouczek i wskazówki [tuto_00_02_03_02] — tekst] 이곳에 스킬의 코인을 굴리기 전 <color=#f8c200>기본 위력<color=#ebcaa2>이 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: This number is the Skill's <color=#f8c200>Base Power<color=#ebcaa2> before it flips any Coins.
   PL: Tutaj widnieje <color=#f8c200>Moc Bazowa<color=#ebcaa2> umiejętności przed rzutem Monetami.
225. [Samouczek i wskazówki [tuto_00_02_03_03] — tekst] 이곳에 스킬의 <color=#f8c200>코인 위력<color=#ebcaa2>이 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: This number is the Skill's <color=#f8c200>Coin Power<color=#ebcaa2>.
   PL: Tutaj widnieje <color=#f8c200>Moc Monety<color=#ebcaa2> umiejętności.
226. [Samouczek i wskazówki [tuto_00_02_03_04] — tekst] 이곳에 스킬의 <color=#f8c200>코인 개수<color=#ebcaa2>가 표시됩니다.\n\n<color=#f8c200><합>을 할 수 있는 기회이자 공격 횟수<color=#ebcaa2>입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_04].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Here, you can see <color=#f8c200>how many Coins<color=#ebcaa2> these Skills have.\n\nThe number of Coins determines two things:\n<color=#f8c200>1) How many times the Skill can lose a <Clash> before losing all of its Coins\n2) How many times the Skill hits when it attacks<color=#ebcaa2>.
   PL: Tutaj wyświetlana jest <color=#f8c200>liczba Monet<color=#ebcaa2> umiejętności.\n\nOznacza ona <color=#f8c200>liczbę szans w „Starciu” oraz liczbę zadawanych ciosów<color=#ebcaa2>.
227. [Samouczek i wskazówki [tuto_00_02_03_05] — tekst] 두 캐릭터가 각자 코인을 굴려 <color=#f8c200>앞면이 나온 코인의 개수<color=#ebcaa2>만큼 <color=#f8c200>기본 위력<color=#ebcaa2>에 <color=#f8c200>코인 위력<color=#ebcaa2>을 더합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_05].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Each Coin that flipped Heads<color=#ebcaa2> will add the <color=#f8c200>Coin Power<color=#ebcaa2> of that Skill to the <color=#f8c200>Base Power<color=#ebcaa2> of that same Skill.
   PL: Obie postacie rzucają Monetami i za <color=#f8c200>każdy wyrzucony awers<color=#ebcaa2> dodają do <color=#f8c200>Mocy Bazowej<color=#ebcaa2> wartość <color=#f8c200>Mocy Monety<color=#ebcaa2>.
228. [Samouczek i wskazówki [tuto_00_02_03_05_popup_title] — tekst] 최종 위력 계산
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_05_popup_title].content
   limit: do 120 znaków
   EN: Final Power Calculation
   PL: Obliczanie Mocy Końcowej
229. [Samouczek i wskazówki [tuto_00_02_03_05_popup_content] — tekst] <color=#f8c200>기본 위력<color=#ebcaa2>에 <color=#f8c200>앞면인 코인 한 개<color=#ebcaa2>당 <color=#f8c200>코인 위력 한 번<color=#ebcaa2>을 더해 <color=#f8c200>최종 위력<color=#ebcaa2>이 결정됩니다.\n\n앞면인 코인은 밝게, 뒷면인 코인은 어둡게 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_05_popup_content].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The formula for a Skill's Final Power is as follows: \n\n<color=#f8c200>Base Power + (Number of Coins that flipped Heads x Coin Power)<color=#ebcaa2>.\n\nCoins that flipped Heads will glow, while the Coins that flipped Tails will appear dimmed.
   PL: Dodanie do <color=#f8c200>Mocy Bazowej<color=#ebcaa2> wartości <color=#f8c200>Mocy Monety<color=#ebcaa2> za <color=#f8c200>każdą Monetę z awersem<color=#ebcaa2> wyznacza <color=#f8c200>Moc Końcową<color=#ebcaa2>.\n\nMonety z awersem świecą jasno, a Monety z rewersem są przyciemnione.
230. [Samouczek i wskazówki [tuto_00_02_03_06] — tekst] 코인을 굴려 <color=#f8c200>최종<color=#ebcaa2>적으로 결정된 <color=#f8c200>스킬 위력<color=#ebcaa2>이 이곳에 표시됩니다.\n\n<color=#f8c200>'강타' 스킬의 위력이 더 높으므로 적의 코인 1개를 파괴<color=#ebcaa2>합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_06].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The <color=#f8c200>resultant<color=#ebcaa2> <color=#f8c200>Skill Power<color=#ebcaa2> is displayed here.\n\n<color=#f8c200>Ishmael's 'Loggerhead' Skill has the higher Skill Power, so the enemy Skill loses a Coin.<color=#ebcaa2>
   PL: Tutaj widnieje <color=#f8c200>końcowa<color=#ebcaa2> wyliczona <color=#f8c200>Moc umiejętności<color=#ebcaa2>.\n\n<color=#f8c200>Umiejętność „Mocny Cios” ma wyższą Moc, więc niszczy 1 Monetę wroga.<color=#ebcaa2>
231. [Samouczek i wskazówki [tuto_00_02_03_07] — tekst] 이렇게 한 쪽의 모든 코인이 파괴될 때까지 <color=#f8c200><합><color=#ebcaa2>이 진행되며, <color=#f8c200>코인이 남은 쪽이 <합>에서 승리<color=#ebcaa2>합니다.\n\n<color=#f8c200><합><color=#ebcaa2>에서 승리할 수 있는 전략을 세우는 것이 가장 중요하다는 것을 꼭 기억해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_02_03_07].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: As seen in this example, they will continue to <color=#f8c200><Clash><color=#ebcaa2> until one of them has no more Coins left to flip. <color=#f8c200>The unit with remaining Coins ultimately wins that <Clash><color=#ebcaa2>.\n\nRemember: winning <color=#f8c200><Clashes><color=#ebcaa2> is one of the most fundamental aspects of winning the battle.
   PL: <color=#f8c200>„Starcie”<color=#ebcaa2> trwa, dopóki jedna ze stron nie straci wszystkich Monet, a <color=#f8c200>strona z ocalałymi Monetami wygrywa „Starcie”<color=#ebcaa2>.\n\nPamiętaj, że kluczem do zwycięstwa jest strategia pozwalająca wygrywać <color=#f8c200>„Starcia”<color=#ebcaa2>.
232. [Samouczek i wskazówki [tuto_00_03_01_01] — tekst] 이번에는 <color=#f8c200><정신력><color=#ebcaa2>에 대해 알아보죠.\n\n<color=#f8c200><정신력><color=#ebcaa2>은 최대 45, 최소 -45까지 증가하거나 감소합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_01_01].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: This time, let us learn about <color=#f8c200><SP><color=#ebcaa2>, or Sanity Points.\n\n<color=#f8c200><SP><color=#ebcaa2> has a maximum value of 45, and a minimum value of -45.
   PL: Poznajmy teraz <color=#f8c200>„Poczytalność” (PP)<color=#ebcaa2>.\n\n<color=#f8c200>„Poczytalność”<color=#ebcaa2> rośnie maksymalnie do 45 i spada minimalnie do -45.
233. [Samouczek i wskazówki [tuto_00_03_01_02] — tekst] 하단의 수감자 아이콘 옆 구체에서도 수감자들의 <color=#f8c200><정신력><color=#ebcaa2>을 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_01_02].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Please note that the Sinners' <color=#f8c200><SP><color=#ebcaa2> values can also be viewed here, next to these orbs adjacent to the portrait icons on the Dashboard.
   PL: <color=#f8c200>„Poczytalność”<color=#ebcaa2> Grzeszników sprawdzisz także na kulach obok ich portretów u dołu ekranu.
234. [Samouczek i wskazówki [tuto_00_03_01_03] — tekst] 전투 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_01_03].content
   limit: do 120 znaków
   EN: Now, please issue a command.
   PL: Wydaj rozkaz do walki.
235. [Samouczek i wskazówki [tuto_00_03_01_04] — tekst] <color=#f8c200><정신력><color=#ebcaa2>은 합에서 승리하거나 적을 처치하는 등\n전투에서 <color=#f8c200>유리한 상황일 때 증가<color=#ebcaa2>하고,\n전투에서 <color=#f8c200>불리한 상황일 때 감소<color=#ebcaa2>합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_01_04].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Each unit's <color=#f8c200><SP><color=#ebcaa2> values change based on certain triggers.\nThey tend to heal SP with <color=#f8c200>favorable triggers(winning Clashes or killing enemies),<color=#ebcaa2>\nand lose SP with <color=#f8c200>unfavorable triggers.<color=#ebcaa2>
   PL: <color=#f8c200>„Poczytalność”<color=#ebcaa2> <color=#f8c200>rośnie w korzystnych sytuacjach<color=#ebcaa2> (np. po wygraniu Starcia lub pokonaniu wroga)\ni <color=#f8c200>maleje w sytuacjach niekorzystnych<color=#ebcaa2>.
236. [Samouczek i wskazówki [tuto_00_03_01_05] — tekst] <color=#f8c200><정신력>이 높을수록<color=#ebcaa2> 스킬의 코인을 굴릴 때 <color=#f8c200>앞면이 나올 확률이 증가<color=#ebcaa2>합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_01_05].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>The higher the unit's <SP> value,<color=#ebcaa2> the <color=#f8c200>higher the chance to flip Heads<color=#ebcaa2> when flipping Skill Coins.
   PL: <color=#f8c200>Im wyższa „Poczytalność”<color=#ebcaa2>, tym <color=#f8c200>większa szansa na awers<color=#ebcaa2> przy rzucie Monetami.
237. [Samouczek i wskazówki [tuto_00_03_02_01] — tekst] 전 턴에 모든 아군이 합에서 승리하여 우리가 유리한 상황이네요. 전투 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_02_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The allied units all won their respective Clashes in the previous turn, which healed their SP.\nThis put us in a favorable position. Please issue your next command.
   PL: W poprzedniej turze wszyscy sojusznicy wygrali Starcia, więc mamy przewagę.\nWydaj kolejny rozkaz do walki.
238. [Samouczek i wskazówki [tuto_00_03_02_02] — tekst] 모든 캐릭터의 체력에는 <color=#f8c200><흐트러짐><color=#ebcaa2> 구간이 선으로 표시되어 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_02_02].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Please direct your attention to this unit's HP(Health Point) bar. This thin line here is called the <color=#f8c200><Stagger Threshold><color=#ebcaa2>.
   PL: Na pasku PŻ każdej postaci linia oznacza próg <color=#f8c200>„Oszołomienia”<color=#ebcaa2>.
239. [Samouczek i wskazówki [tuto_00_03_02_03] — tekst] 피격으로 인해 체력이 <color=#f8c200><흐트러짐><color=#ebcaa2> 구간 이하로 감소하면 <color=#f8c200><흐트러짐 상태><color=#ebcaa2>가 됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_02_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: When a unit's HP drops below the <color=#f8c200><Stagger Threshold><color=#ebcaa2> line, they become <color=#f8c200><Staggered><color=#ebcaa2>.
   PL: Gdy wskutek obrażeń PŻ spadną poniżej progu <color=#f8c200>„Oszołomienia”<color=#ebcaa2>, postać wpada w <color=#f8c200>„stan Oszołomienia”<color=#ebcaa2>.
240. [Samouczek i wskazówki [tuto_00_03_03_01] — tekst] <color=#f8c200><흐트러짐 상태><color=#ebcaa2>인 대상은 행동을 할 수 없고 받는 피해가 크게 증가하기 때문에 전투에서 상당히 불리해집니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_03_01].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200><Staggered><color=#ebcaa2> units cannot take any action and take double the damage, which puts them at a significant disadvantage in battle.
   PL: Cel w <color=#f8c200>„stanie Oszołomienia”<color=#ebcaa2> nie może wykonywać akcji i otrzymuje znacznie większe obrażenia, co stawia go w fatalnym położeniu.
241. [Samouczek i wskazówki [tuto_00_03_04_01] — tekst] 이전 턴에 적을 처치하여 남은 적들이 전의를 잃고\n<color=#f8c200><패닉><color=#ebcaa2> 상태가 되었습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_04_01].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: You have put the remaining enemies in <color=#f8c200><Panic><color=#ebcaa2> states by defeating their allies in the previous turn, which dropped their SP.
   PL: Pokonanie wroga w poprzedniej turze złamało morale pozostałych,\nprzez co wpadli w stan <color=#f8c200>„Paniki”<color=#ebcaa2>.
242. [Samouczek i wskazówki [tuto_00_03_04_02] — tekst] 정신력이 일정 수치 이하로 낮아진 적은 <color=#f8c200><사기 저하><color=#ebcaa2> 또는 <color=#f8c200><패닉><color=#ebcaa2> 상태가 되며, 부정적인 효과를 얻습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_04_02].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: When an enemy's SP drops below a certain threshold, they may enter <color=#f8c200><Low Morale><color=#ebcaa2> or <color=#f8c200><Panic><color=#ebcaa2> states, which inflict them with negative effects.
   PL: Wróg, którego PP spadną poniżej określonego progu, wpada w <color=#f8c200>„Niskie Morale”<color=#ebcaa2> lub <color=#f8c200>„Panikę”<color=#ebcaa2> i otrzymuje negatywne efekty.
243. [Samouczek i wskazówki [tuto_00_03_04_03] — tekst] <color=#f8c200><사기 저하><color=#ebcaa2>, <color=#f8c200><패닉><color=#ebcaa2> 효과를 받고 있다면 여기에 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_04_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Units in <color=#f8c200><Low Morale><color=#ebcaa2> or <color=#f8c200><Panic><color=#ebcaa2> states are marked by these labels.
   PL: Aktywne efekty <color=#f8c200>„Niskiego Morale”<color=#ebcaa2> lub <color=#f8c200>„Paniki”<color=#ebcaa2> wyświetlane są w tym miejscu.
244. [Samouczek i wskazówki [tuto_00_03_04_04] — tekst] <color=#f8c200><사기 저하><color=#ebcaa2>, <color=#f8c200><패닉><color=#ebcaa2> 효과는 개체마다 다릅니다.\n하단의 아이콘을 눌러 정확히 어떤 효과를 받고 있는지 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_03_04_04].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Each unit gains different effects from entering <color=#f8c200><Low Morale><color=#ebcaa2> and <color=#f8c200><Panic><color=#ebcaa2> states.\nSelect this icon to learn what effects this unit is suffering from.
   PL: Efekty <color=#f8c200>„Niskiego Morale”<color=#ebcaa2> i <color=#f8c200>„Paniki”<color=#ebcaa2> różnią się zależnie od jednostki.\nKliknij dolną ikonę, aby sprawdzić dokładne działanie efektu.
245. [Samouczek i wskazówki [tuto_00_04_01_01] — tekst] 캐릭터를 누르면 그 캐릭터의 <color=#f8c200>정보<color=#ebcaa2>를 알 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Select a unit to view their <color=#f8c200>detailed information<color=#ebcaa2> window.
   PL: Kliknij postać, aby wyświetlić jej <color=#f8c200>informacje<color=#ebcaa2>.
246. [Samouczek i wskazówki [tuto_00_04_01_02] — tekst] 이곳에서는 캐릭터의 기본적인 <color=#f8c200>스테이터스<color=#ebcaa2>를 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: This is where you view each character's <color=#f8c200>basic stats<color=#ebcaa2>.
   PL: Tutaj sprawdzisz podstawowe <color=#f8c200>statystyki<color=#ebcaa2> postaci.
247. [Samouczek i wskazówki [tuto_00_04_01_03] — tekst] 이곳에서는 캐릭터의 <color=#f8c200>육성 상태<color=#ebcaa2>와 <color=#f8c200>보유한 스킬<color=#ebcaa2>을 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: This is where you view this unit's <color=#f8c200>list of Skills<color=#ebcaa2> and <color=#f8c200>upgrade progress<color=#ebcaa2>.
   PL: Tutaj sprawdzisz <color=#f8c200>stan rozwoju<color=#ebcaa2> oraz <color=#f8c200>posiadane umiejętności<color=#ebcaa2> postaci.
248. [Samouczek i wskazówki [tuto_00_04_01_04] — tekst] 같은 방법으로 적의 정보도 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_04].content
   limit: do 120 znaków
   EN: You may also select an enemy to view their detailed information.
   PL: W ten sam sposób możesz sprawdzić także informacje o wrogach.
249. [Samouczek i wskazówki [tuto_00_04_01_05] — tekst] 모든 캐릭터는 <color=#f8c200>내성<color=#ebcaa2>이 정해져 있습니다.\n이곳에서 <color=#f8c200>어떤 속성에 취약<color=#ebcaa2>한지 파악할 수 있죠.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_05].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Each unit has <color=#f8c200>Resistance<color=#ebcaa2> values.\nUse these values to determine what <color=#f8c200>Attack Type or Affinity<color=#ebcaa2> they are weak against.
   PL: Każda postać ma określone <color=#f8c200>odporności<color=#ebcaa2>.\nTutaj sprawdzisz, <color=#f8c200>na jakie ataki jest podatna<color=#ebcaa2>.
250. [Samouczek i wskazówki [tuto_00_04_01_06_title] — tekst] 공격 유형과 속성
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_06_title].content
   limit: do 120 znaków
   EN: Attack Types and Affinities
   PL: Typy ataków i grzechy
251. [Samouczek i wskazówki [tuto_00_04_01_07] — tekst] 스킬은 <color=#f8c200>3가지의 공격 유형과<color=#ebcaa2>, <color=#f8c200>7가지의 죄악 속성<color=#ebcaa2>으로 분류됩니다.\n대상의 내성에 따라 대미지가 결정됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_07].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Each Skill's damage is classified by two categories: <color=#f8c200>3 Attack Types<color=#ebcaa2> and <color=#f8c200>7 Sin Affinities<color=#ebcaa2>.\nThe target’s Resistance to these categories can either increase or reduce the damage dealt.\n<color=#f8c200>A higher Resistance value on a unit means they will take more damage from that damage type.<color=#ebcaa2>
   PL: Umiejętności dzielą się na <color=#f8c200>3 typy ataków<color=#ebcaa2> oraz <color=#f8c200>7 grzechów<color=#ebcaa2>.\nZadawane obrażenia zależą od odporności celu na te kategorie.
252. [Samouczek i wskazówki [tuto_00_04_01_08] — tekst] 적의 약점 속성을 파악하여 적합한 속성으로 공격하면 전투를 더 유리하게 이끌어 나갈 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_01_08].content
   limit: do 130 znaków
   EN: Check your enemy's weaknesses and select the Skills that can exploit them to deal more damage.
   PL: Rozpoznawanie słabości wroga i atakowanie odpowiednimi atrybutami zapewni ci przewagę w walce.
253. [Samouczek i wskazówki [tuto_00_04_02_01] — tekst] 일반적으로 하단의 스킬창에서 왼쪽에 위치한 스킬의 행동 순서가 가장 빠릅니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_02_01].content
   limit: do 140 znaków
   EN: In most cases, the unit with the leftmost Skill on the Dashboard will be the first to act among allies.
   PL: Zazwyczaj najszybciej działa sojusznik zajmujący skrajną lewą kolumnę na dolnym panelu umiejętności.
254. [Samouczek i wskazówki [tuto_00_04_02_02] — tekst] 턴이 지날 때마다 <color=#f8c200>편성 순서가 빠른 아군<color=#ebcaa2>부터 슬롯이 1개씩 증가하여 추가적인 공격 기회를 얻습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_02_02].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Starting from the <color=#f8c200>allied unit highest on the Deployment order<color=#ebcaa2>, an ally gains 1 additional Slot with every passing turn. This means that they gain an extra opportunity to attack.
   PL: Z każdą kolejną turą <color=#f8c200>począwszy od sojuszników z najniższym numerem rozstawienia<color=#ebcaa2> dodawany jest 1 slot, dając dodatkową okazję do ataku.
255. [Samouczek i wskazówki [tuto_00_04_03_01] — tekst] 이것은 수감자들에게 <color=#f8c200>자율적인 스킬 장착<color=#ebcaa2>을 맡기는 기능입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_03_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Use one of these buttons to let the Sinners choose what Skills they want to use.
   PL: Te przyciski powierzają Grzesznikom <color=#f8c200>automatyczny dobór umiejętności<color=#ebcaa2>.
256. [Samouczek i wskazówki [tuto_00_04_03_02] — tekst] 관리자님의 명령 없이 수감자들의 판단에 맡기는 건 비효율적인 전투로 이어질 가능성이 있으니 선택은 관리자님의 몫입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_03_02].content
   limit: do 180 znaków
   EN: However, it must be emphasized that leaving the Sinners to make their own strategic choices could lead to suboptimal combat performances.
   PL: Pozostawienie decyzji osądowi Grzeszników bez rozkazów Kierownika może jednak skutkować nieoptymalną walką — wybór należy do ciebie.
257. [Samouczek i wskazówki [tuto_00_04_03_03_title] — tekst] 승률 계산
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_03_03_title].content
   limit: do 120 znaków
   EN: Clash Outcome Forecast
   PL: Prognoza Starcia
258. [Samouczek i wskazówki [tuto_00_04_03_04] — tekst] 현재 상황에 따른 해당 스킬의 합 승률이 자동으로 계산되어 이 두 곳에 표시됩니다.\n\n완벽한 계산은 아니지만, 빠른 판단이 필요할 때 참고하세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_00_04_03_04].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Clash outcome forecast appears at the top of the screen and beside each selected Skill. \n\nPlease note that the forecast is not always perfect, but it is serviceable when quick decisions are necessary.
   PL: Szansa wygrania Starcia daną umiejętnością w bieżącej sytuacji obliczana jest automatycznie i wyświetlana w tych dwóch miejscach.\n\nPrognoza nie jest nieomylna, lecz pomaga przy podejmowaniu szybkich decyzji.
259. [Samouczek i wskazówki [tuto_01_02_01_01] — tekst] 한 턴에 같은 <color=#f8c200>속성(색깔)<color=#ebcaa2>의 스킬을 여러 개 사용하면 <color=#f8c200><공명><color=#ebcaa2>이 발생합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_01].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Chaining multiple Skills with the same <color=#f8c200>Affinity(Color)<color=#ebcaa2> in the same turn will activate what is known as <color=#f8c200><Resonance><color=#ebcaa2>.
   PL: Użycie w jednej turze kilku umiejętności tego samego <color=#f8c200>grzechu (koloru)<color=#ebcaa2> wywołuje <color=#f8c200>„Rezonans”<color=#ebcaa2>.
260. [Samouczek i wskazówki [tuto_01_02_01_02] — tekst] 같은 속성의 스킬을 연결하여 <color=#f8c200><공명><color=#ebcaa2>을 만들어주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Connect these Skills with the same Affinities and activate <color=#f8c200><Resonance><color=#ebcaa2>.
   PL: Połącz umiejętności tego samego grzechu, aby wywołać <color=#f8c200>„Rezonans”<color=#ebcaa2>.
261. [Samouczek i wskazówki [tuto_01_02_01_03] — tekst] <color=#f8c200>같은 속성 3개 이상을 이어지게 연결<color=#ebcaa2>하면 <color=#f8c200><완전 공명><color=#ebcaa2>이 발생합니다.\n\n<color=#f8c200><완전 공명><color=#ebcaa2>을 만들어주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_03].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: <color=#f8c200>Chaining 3 or more adjacent Skills<color=#ebcaa2> with the same Affinity activates <color=#f8c200><Absolute Resonance><color=#ebcaa2>.\n\nTry activating <color=#f8c200><Absolute Resonance><color=#ebcaa2> using these Skills.
   PL: <color=#f8c200>Połączenie obok siebie co najmniej 3 umiejętności tego samego grzechu<color=#ebcaa2> wywołuje <color=#f8c200>„Rezonans Absolutny”<color=#ebcaa2>.\n\nUtwórz <color=#f8c200>„Rezonans Absolutny”<color=#ebcaa2>.
262. [Samouczek i wskazówki [tuto_01_02_01_04] — tekst] 이렇게 <color=#f8c200><공명><color=#ebcaa2>과 <color=#f8c200><완전 공명><color=#ebcaa2>을 하면 해당 스킬의 위력이 소폭 증가하는 등의 유리한 효과를 얻을 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_04].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Activating <color=#f8c200><Resonance><color=#ebcaa2> or <color=#f8c200><Absolute Resonance><color=#ebcaa2> grants minor boosts to the Skills chained for the Resonance, such as a slight increase in Skill Power.
   PL: Aktywacja <color=#f8c200>„Rezonansu”<color=#ebcaa2> oraz <color=#f8c200>„Rezonansu Absolutnego”<color=#ebcaa2> zapewnia korzystne efekty, takie jak niewielki wzrost Mocy objętych nim umiejętności.
263. [Samouczek i wskazówki [tuto_01_02_01_05_title] — tekst] 공명
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_05_title].content
   limit: do 120 znaków
   EN: Resonance
   PL: Rezonans
264. [Samouczek i wskazówki [tuto_01_02_01_06] — tekst] 한 턴에 같은 속성 스킬을 2개 이상 사용하면 <color=#f8c200><공명><color=#ebcaa2>이 발생합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_01_06].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Chaining 2 or more Skills with the same Affinity in the same turn will activate what is known as <color=#f8c200><Resonance><color=#ebcaa2>.
   PL: Użycie w jednej turze co najmniej 2 umiejętności tego samego grzechu wywołuje <color=#f8c200>„Rezonans”<color=#ebcaa2>.
265. [Samouczek i wskazówki [tuto_01_02_02_01_title] — tekst] 완전 공명
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_02_01_title].content
   limit: do 120 znaków
   EN: Absolute Resonance
   PL: Rezonans Absolutny
266. [Samouczek i wskazówki [tuto_01_02_02_02] — tekst] 한 턴에 같은 속성 스킬을 3개 이상 연속으로 연결하면\n<color=#f8c200><완전 공명><color=#ebcaa2>이 발생합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_02_02].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Chaining 3 or more adjacent Skills with the same Affinity in the same turn will activate what is known as <color=#f8c200><Absolute Resonance><color=#ebcaa2>.
   PL: Połączenie w jednej turze co najmniej 3 sąsiadujących umiejętności tego samego grzechu\nwywołuje <color=#f8c200>„Rezonans Absolutny”<color=#ebcaa2>.
267. [Samouczek i wskazówki [tuto_01_02_02_03_title] — tekst] 공명 효과
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_02_03_title].content
   limit: do 120 znaków
   EN: Resonance Effects
   PL: Efekty Rezonansu
268. [Samouczek i wskazówki [tuto_01_02_02_04] — tekst] <color=#f8c200><공명><color=#ebcaa2>이 발생한 스킬은 <color=#f8c200>공명된 스킬 수<color=#ebcaa2>에 비례하여 스킬이 소폭 강화되며, <color=#f8c200>나중에 입력된 스킬<color=#ebcaa2>일수록 성능이 더욱 강화됩니다.\n\n<color=#f8c200><완전 공명><color=#ebcaa2>시 완전 공명된 <color=#f8c200>모든 스킬에 강화 효과<color=#ebcaa2>가 적용됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_02_04].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Activating <color=#f8c200><Resonance><color=#ebcaa2> slightly enhances affected Skills based on <color=#f8c200>the number of Skills linked in the Resonance chain<color=#ebcaa2>. Skills closer to the right end of the Dashboard receive greater boosts.\n\nActivating <color=#f8c200><Absolute Resonance><color=#ebcaa2> guarantees that every Skill in the Resonance chain receives the boost.
   PL: Umiejętności objęte <color=#f8c200>„Rezonansem”<color=#ebcaa2> zostają wzmocnione proporcjonalnie do <color=#f8c200>liczby umiejętności w Rezonansie<color=#ebcaa2>, przy czym <color=#f8c200>umiejętności dalej po prawej<color=#ebcaa2> zyskują silniejszą premię.\n\nPrzy <color=#f8c200>„Rezonansie Absolutnym”<color=#ebcaa2> wzmocnienie otrzymują <color=#f8c200>wszystkie umiejętności w łańcuchu<color=#ebcaa2>.
269. [Samouczek i wskazówki [tuto_01_02_03_01] — tekst] 모든 캐릭터는 고유의 <color=#f8c200>패시브<color=#ebcaa2>를 보유하고 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Each unit has a unique <color=#f8c200>Passive<color=#ebcaa2>.
   PL: Każda postać posiada unikalną <color=#f8c200>pasywkę<color=#ebcaa2>.
270. [Samouczek i wskazówki [tuto_01_02_03_02] — tekst] <color=#f8c200>패시브<color=#ebcaa2>를 확인하기 위해 파우스트를 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Select Faust to view her <color=#f8c200>Passive<color=#ebcaa2>.
   PL: Kliknij Faust, aby sprawdzić jej <color=#f8c200>pasywkę<color=#ebcaa2>.
271. [Samouczek i wskazówki [tuto_01_02_03_03] — tekst] 수감자의 스킬 정보를 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_03].content
   limit: do 120 znaków
   EN: Select the Sinner's Skills tab.
   PL: Kliknij zakładkę umiejętności Grzeszniczki.
272. [Samouczek i wskazówki [tuto_01_02_03_04] — tekst] 이곳의 <color=#f8c200>패시브<color=#ebcaa2> 버튼을 눌러 발동 조건과 효과를 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Select the <color=#f8c200>Passive<color=#ebcaa2> button here to view its activation conditionals and effects.
   PL: Kliknij tutaj przycisk <color=#f8c200>pasywki<color=#ebcaa2>, aby sprawdzić warunek aktywacji oraz efekt.
273. [Samouczek i wskazówki [tuto_01_02_03_05] — tekst] 파우스트의 패시브는 <color=#f8c200><공명><color=#ebcaa2> 효과입니다.\n앞서 설명드린 <color=#f8c200><공명><color=#ebcaa2>을 통해 발동시킬 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_05].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Faust's Passive is a <color=#f8c200><Resonance><color=#ebcaa2> Passive.\nThe conditionals for these Passives can be met by activating <color=#f8c200><Resonance><color=#ebcaa2> that was explained earlier.
   PL: Pasywka Faust działa w oparciu o <color=#f8c200>„Rezonans”<color=#ebcaa2>.\nAktywujesz ją poprzez wyjaśniony wcześniej <color=#f8c200>„Rezonans”<color=#ebcaa2>.
274. [Samouczek i wskazówki [tuto_01_02_03_06] — tekst] 필요한 속성의 <color=#f8c200><공명><color=#ebcaa2>을 발생시켜 <color=#f8c200><공명 패시브><color=#ebcaa2>를 활성화시켜주세요.\n\n파우스트의 패시브는 <color=#004bd5>오만(남색)<color=#ebcaa2> 속성으로 2공명 이상이 필요합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_03_06].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, <color=#004bd5>, \n
   EN: Please activate the <color=#f8c200><Resonance Passive><color=#ebcaa2> by activating <color=#f8c200><Resonance><color=#ebcaa2> for the necessary Affinity.\n\nFaust's Passive requires 2 or more <color=#004bd5>Pride(Indigo)<color=#ebcaa2> Resonance.
   PL: Wywołaj <color=#f8c200>„Rezonans”<color=#ebcaa2> wymaganego grzechu, aby aktywować <color=#f8c200>„pasywkę Rezonansu”<color=#ebcaa2>.\n\nPasywka Faust wymaga Rezonansu co najmniej 2 umiejętności <color=#004bd5>Pychy (granatowych)<color=#ebcaa2>.
275. [Samouczek i wskazówki [tuto_01_02_04_01] — tekst] 이번에는 다른 종류의 패시브를 확인해보죠.\n\n<color=#f8c200>좌측 상단<color=#ebcaa2>의 아이콘을 눌러도 패시브를 확인할 수 있습니다.\n표시된 뫼르소 수감자의 아이콘을 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Let us take a look at a different type of Passive.\n\nThese icons <color=#f8c200>in the top left corner<color=#ebcaa2> of the screen also show the list of available Passives. Select Meursault's icon, highlighted here.
   PL: Sprawdźmy teraz inny rodzaj pasywki.\n\nPasywki przejrzysz również pod ikonami w <color=#f8c200>lewym górnym rogu<color=#ebcaa2>.\nKliknij podświetloną ikonę Grzesznika Meursaulta.
276. [Samouczek i wskazówki [tuto_01_02_04_02] — tekst] 뫼르소 수감자의 패시브는 <color=#f8c200><보유><color=#ebcaa2> 효과입니다.\n\n<color=#f8c200><보유 패시브><color=#ebcaa2>는 <color=#f8c200>E.G.O 자원<color=#ebcaa2>을 요구치만큼 보유하고 있으면 턴마다 자동으로 활성화됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_02].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Sinner Meursault's Passive is an <color=#f8c200><Owned><color=#ebcaa2> Passive.\n\n<color=#f8c200><Owned Passives><color=#ebcaa2> activate automatically each turn, provided you have enough <color=#f8c200>E.G.O resources<color=#ebcaa2> to meet the requirement.
   PL: Pasywka Meursaulta działa w oparciu o <color=#f8c200>„Posiadanie”<color=#ebcaa2>.\n\n<color=#f8c200>„Pasywka Posiadania”<color=#ebcaa2> aktywuje się automatycznie co turę, jeśli posiadasz wymaganą liczbę <color=#f8c200>zasobów E.G.O<color=#ebcaa2>.
277. [Samouczek i wskazówki [tuto_01_02_04_03] — tekst] 이 패시브는 <color=#fbc82b>나태(노란색)<color=#ebcaa2> 자원을 2개 요구하네요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fbc82b>, <color=#ebcaa2>
   EN: This Passive requires that you own 2 <color=#fbc82b>Sloth(Yellow)<color=#ebcaa2> Resources.
   PL: Ta pasywka wymaga posiadania 2 zasobów <color=#fbc82b>Lenistwa (żółtych)<color=#ebcaa2>.
278. [Samouczek i wskazówki [tuto_01_02_04_04] — tekst] <color=#f8c200>스킬을 사용<color=#ebcaa2>하면 <color=#f8c200>해당 스킬 속성의 자원<color=#ebcaa2>을 얻습니다.\n\n이전 턴에 충분한 <color=#fbc82b>나태(노란색)<color=#ebcaa2> 자원을 모아둔 상태라 이 <color=#f8c200><보유 패시브><color=#ebcaa2>는 활성화된 상태입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_04].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, <color=#fbc82b>, \n
   EN: <color=#f8c200>Use a Skill<color=#ebcaa2> to <color=#f8c200>gain an E.G.O resource corresponding to that Skill's Affinity<color=#ebcaa2>, viewable here.\n\nSince we gathered enough <color=#fbc82b>Sloth (Yellow)<color=#ebcaa2> E.G.O resources in the previous turn, this <color=#f8c200><Owned Passive><color=#ebcaa2> is already activated.
   PL: <color=#f8c200>Użycie umiejętności<color=#ebcaa2> zapewnia <color=#f8c200>zasób odpowiadającego jej grzechu<color=#ebcaa2>.\n\nPonieważ w poprzedniej turze zebraliśmy dość zasobów <color=#fbc82b>Lenistwa (żółtych)<color=#ebcaa2>, ta <color=#f8c200>„pasywka Posiadania”<color=#ebcaa2> jest już aktywna.
279. [Samouczek i wskazówki [tuto_01_02_04_05] — tekst] 현재 활성화된 패시브는 밝게 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_05].content
   limit: do 120 znaków
   EN: Currently active Passives will be highlighted.
   PL: Aktualnie aktywne pasywki są podświetlone.
280. [Samouczek i wskazówki [tuto_01_02_04_06] — tekst] 전투에 참여하지 않는 수감자들은 <서포트 패시브>로 전투중인 수감자들을 지원합니다.\n\n<color=#f8c200><서포트 패시브><color=#ebcaa2>는 이곳에서 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_06].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Sinners not participating in this Encounter will provide <Support Passives> to aid the Sinners in battle.\n\nView the <color=#f8c200><Support Passives><color=#ebcaa2> here.
   PL: Grzesznicy nieuczestniczący bezpośrednio w walce wspierają walczących poprzez „pasywki wsparcia”.\n\n<color=#f8c200>„Pasywki wsparcia”<color=#ebcaa2> sprawdzisz w tym miejscu.
281. [Samouczek i wskazówki [tuto_01_02_04_07_title] — tekst] 서포트 패시브
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_07_title].content
   limit: do 120 znaków
   EN: Support Passives
   PL: Pasywki wsparcia
282. [Samouczek i wskazówki [tuto_01_02_04_08] — tekst] 수감자들이 충분히 성장한 이후에는 전투에 참여하지 않은 수감자도 <서포트 패시브>를 통해 아군을 지원할 수 있습니다.\n<서포트 패시브>도 일반 패시브와 동일하게 <color=#f8c200><공명><color=#ebcaa2> 또는 <color=#f8c200><보유><color=#ebcaa2> 효과를 통해 활성화할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_02_04_08].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Sinners that have been sufficiently upgraded can assist the Deployed Sinners through their <Support Passives>.\n<Support Passives>, like regular Passives, have <color=#f8c200><Resonance><color=#ebcaa2> and <color=#f8c200><Owned><color=#ebcaa2> conditionals.
   PL: Odpowiednio rozwinięci Grzesznicy niebiorący udziału w starciu wspierają sojuszników swoimi „pasywkami wsparcia”.\nPodobnie jak zwykłe pasywki, aktywuje się je poprzez <color=#f8c200>„Rezonans”<color=#ebcaa2> lub <color=#f8c200>„Posiadanie”<color=#ebcaa2>.
283. [Samouczek i wskazówki [tuto_01_03_01_01] — tekst] 캐릭터는 공격 스킬 외에도 <color=#f8c200><수비 스킬><color=#ebcaa2>을 보유하고 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: In addition to Attack Skills, each unit also has <color=#f8c200><Defense Skills><color=#ebcaa2>.
   PL: Oprócz umiejętności ataku postacie posiadają również <color=#f8c200>„umiejętności obrony”<color=#ebcaa2>.
284. [Samouczek i wskazówki [tuto_01_03_01_02] — tekst] 하단의 수감자 아이콘을 짧게 누르면 해당 슬롯을\n<color=#f8c200><수비 스킬><color=#ebcaa2>로 변경할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_02].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Lightly tap a Sinner's portrait at the bottom of the Dashboard to swap their bottom Skill with a <color=#f8c200><Defense Skill><color=#ebcaa2>.
   PL: Krótkie dotknięcie portretu Grzesznika u dołu ekranu zamienia jego dolny slot na\n<color=#f8c200>„umiejętność obrony”<color=#ebcaa2>.
285. [Samouczek i wskazówki [tuto_01_03_01_03] — tekst] 먼저 뫼르소 수감자의 아이콘을 눌러 <color=#f8c200><가드><color=#ebcaa2> 스킬을 생성해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: First, let's try selecting Sinner Meursault's portrait to generate a <color=#f8c200><Guard><color=#ebcaa2> Skill.
   PL: Najpierw dotknij portretu Meursaulta, aby wygenerować umiejętność <color=#f8c200>„Gardy”<color=#ebcaa2>.
286. [Samouczek i wskazówki [tuto_01_03_01_04] — tekst] 이번엔 파우스트의 아이콘을 눌러 <color=#f8c200><회피><color=#ebcaa2> 스킬을 생성해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Now, select Faust's portrait to generate an <color=#f8c200><Evade><color=#ebcaa2> Skill.
   PL: Teraz dotknij portretu Faust, aby wygenerować umiejętność <color=#f8c200>„Uniku”<color=#ebcaa2>.
287. [Samouczek i wskazówki [tuto_01_03_01_05] — tekst] 이번엔 히스클리프 수감자의 아이콘을 눌러 <color=#f8c200><반격><color=#ebcaa2> 스킬을 생성해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_05].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Finally, select Sinner Heathcliff's portrait to generate a <color=#f8c200><Counter><color=#ebcaa2> Skill.
   PL: Na koniec dotknij portretu Heathcliffa, aby wygenerować umiejętność <color=#f8c200>„Kontry”<color=#ebcaa2>.
288. [Samouczek i wskazówki [tuto_01_03_01_06_title] — tekst] 수비 스킬 - 가드
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_06_title].content
   limit: do 120 znaków
   EN: Defense Skills: Guard
   PL: Umiejętności obrony — Garda
289. [Samouczek i wskazówki [tuto_01_03_01_07] — tekst] <color=#f8c200><가드><color=#ebcaa2>는 위력만큼 <color=#f8c200>보호막<color=#ebcaa2>을 얻습니다.\n피해를 입을 때, 체력보다 보호막에 먼저 피해를 입습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_07].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Use the <color=#f8c200><Guard><color=#ebcaa2> Skill to gain <color=#f8c200>Shield<color=#ebcaa2> equal to its Power.\nDamage will be absorbed by the Shield first before affecting the unit's HP.
   PL: <color=#f8c200>„Garda”<color=#ebcaa2> zapewnia <color=#f8c200>Tarczę<color=#ebcaa2> równą jej Mocy.\nPrzy otrzymywaniu obrażeń w pierwszej kolejności pochłania je Tarcza zamiast PŻ.
290. [Samouczek i wskazówki [tuto_01_03_01_08_title] — tekst] 수비 스킬 - 회피
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_08_title].content
   limit: do 120 znaków
   EN: Defense Skills: Evade
   PL: Umiejętności obrony — Unik
291. [Samouczek i wskazówki [tuto_01_03_01_09] — tekst] <color=#f8c200><회피><color=#ebcaa2>는 상대 스킬보다 최종 위력이 높거나 같으면, 공격을 완전히 <color=#f8c200>무효화<color=#ebcaa2>합니다.\n상대 공격 스킬의 코인마다 판정하며, 상대보다 최종 위력이 낮을 경우 아무런 효과가 없으니 주의하세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_09].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: When using a <color=#f8c200><Evade><color=#ebcaa2> Skill, if its Final Power is greater than or equal to that of the enemy's Skill, the unit will <color=#f8c200>completely ignore<color=#ebcaa2> the enemy's attack, taking no damage from it.\nEvade Skills flip their Coin once for every enemy Coinflip.\nWarning: If an Evade-type Defense Skill's Final Power is lower than the enemy's attack, it will fail, and the enemy's attack will strike with full force.
   PL: Jeśli Moc Końcowa <color=#f8c200>„Uniku”<color=#ebcaa2> jest równa lub wyższa od Mocy umiejętności wroga, całkowicie <color=#f8c200>unika<color=#ebcaa2> on ataku.\nTest powtarzany jest dla każdej Monety ataku wroga; jeśli Moc Końcowa okaże się niższa od wroga, Unik nie zadziała.
292. [Samouczek i wskazówki [tuto_01_03_01_10_title] — tekst] 수비 스킬 - 반격
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_10_title].content
   limit: do 120 znaków
   EN: Defense Skills: Counter
   PL: Umiejętności obrony — Kontra
293. [Samouczek i wskazówki [tuto_01_03_01_11] — tekst] <color=#f8c200><반격><color=#ebcaa2>은 <color=#f8c200>피격 후 대상에게 일방 공격<color=#ebcaa2>을 가합니다.\n피격당해 흐트러진다면 반격할 수 없게 되니 주의하세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_11].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: <color=#f8c200><Counter><color=#ebcaa2> Skills allow the enemy to strike first, <color=#f8c200>then perform an Unopposed Attack against the attacker<color=#ebcaa2>.\nWarning: If the unit is Staggered by the enemy's attack, the Counter will not activate.
   PL: <color=#f8c200>„Kontra”<color=#ebcaa2> <color=#f8c200>po otrzymaniu trafienia wyprowadza atak jednostronny<color=#ebcaa2> w agresora.\nUwaga: jeśli postać ulegnie Oszołomieniu od ciosu wroga, nie wykona Kontry.
294. [Samouczek i wskazówki [tuto_01_03_01_12] — tekst] 수감자 아이콘을 다시 한번 누르면 생성된\n<color=#f8c200><수비 스킬>을 취소<color=#ebcaa2>할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_12].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Lightly tap the Sinner's portrait again to <color=#f8c200>cancel the generated <Defense Skill><color=#ebcaa2>.
   PL: Ponowne dotknięcie portretu Grzesznika\n<color=#f8c200>anuluje wygenerowaną „umiejętność obrony”<color=#ebcaa2>.
295. [Samouczek i wskazówki [tuto_01_03_01_13] — tekst] 이제 전투에서 직접 효과를 알아보도록 하겠습니다.\n\n<color=#f8c200><수비 스킬><color=#ebcaa2>을 연결하여 전투 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_01_13].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Let us demonstrate the effects of each Defense Skill in this battle.\n\nChain the <color=#f8c200><Defense Skills><color=#ebcaa2>, then start the combat phase.
   PL: Sprawdźmy teraz ich działanie bezpośrednio w walce.\n\nPołącz <color=#f8c200>„umiejętności obrony”<color=#ebcaa2> i wydaj rozkaz do starcia.
296. [Samouczek i wskazówki [tuto_01_03_02_01] — tekst] <color=#f8c200><수비 스킬><color=#ebcaa2>은 적절한 상황에 활용했을 때 공격하는 것보다 큰 이득을 볼 수 있지만, 상황에 따라 오히려 더 위험할 수도 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_02_01].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: When used under the right circumstances, <color=#f8c200><Defense Skills><color=#ebcaa2> can be even more effective than Clashing or attacking enemies. However, poorly timed use of these Skills can put the Sinners at great risk.
   PL: Użyte we właściwym momencie <color=#f8c200>„umiejętności obrony”<color=#ebcaa2> potrafią przynieść większą korzyść niż atak, lecz w nieodpowiedniej sytuacji mogą okazać się ryzykowne.
297. [Samouczek i wskazówki [tuto_01_03_02_02] — tekst] 또한 수감자들은 관리자님이 <color=#f8c200>직접 명령<color=#ebcaa2>을 내리지 않으면 <color=#f8c200><수비 스킬><color=#ebcaa2>을 사용하지 않으니 <color=#f8c200>자동 스킬 장착<color=#ebcaa2>기능을 사용하실 때 유의해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_03_02_02].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Also, please note that Sinners will not select their <color=#f8c200><Defense Skills><color=#ebcaa2> unless you <color=#f8c200>personally issue a direct command<color=#ebcaa2>. Keep this in mind when using the <color=#f8c200>auto-Skill chaining<color=#ebcaa2> functions.
   PL: Pamiętaj też, że Grzesznicy nie użyją <color=#f8c200>„umiejętności obrony”<color=#ebcaa2> bez <color=#f8c200>bezpośredniego rozkazu<color=#ebcaa2> Kierownika — miej to na uwadze podczas korzystania z <color=#f8c200>automatycznego doboru umiejętności<color=#ebcaa2>.
298. [Samouczek i wskazówki [tuto_01_04_01_01_title] — tekst] 전투 화면 내 정보량 조절 설정
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_01_title].content
   (powtórzenie elementu 135 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Samouczek i wskazówki [tuto_01_04_01_02] — tekst] 전투 화면 오른쪽 상단에는 전투와 관련된 정보를 제어하는 버튼이 있습니다.\n\n버튼은 각각 <color=#f8c200>최소 / 중간 / 최대<color=#ebcaa2> 양의 정보를 표시합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_02].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: At the top right of the in-battle screen, there is a button that adjusts the amount of information displayed.\n\nThe three options set the display density to <color=#f8c200>minimum, medium, or maximum<color=#ebcaa2>, respectively.
   PL: W prawym górnym rogu ekranu walki znajduje się przycisk regulujący ilość wyświetlanych informacji.\n\nPrzyciski ustawiają odpowiednio <color=#f8c200>minimalną / średnią / maksymalną<color=#ebcaa2> ilość informacji.
300. [Samouczek i wskazówki [tuto_01_04_01_03_title] — tekst] MAX
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_03_title].content
   (powtórzenie elementu 137 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Samouczek i wskazówki [tuto_01_04_01_04] — tekst] 최대 정보 표시 설정입니다.\n\n게임 시작 시 최초 적용된 정보 표시 설정입니다.\n\n중간 정보 표시, 최소 정보 표시보다 더 많은 정보를 제공합니다.\n\n스킬에서 사용되는 키워드에 대한 정보를 표시해줍니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_04].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The maximum information display configuration.\n\nThis is the default setting applied when first starting the game.\n\nMore information is shown compared to the other two settings.\n\nDetails on Keywords used in Skills are shown as well.
   PL: Konfiguracja maksymalnej ilości informacji.\n\nJest to ustawienie domyślne przy pierwszym uruchomieniu gry.\n\nPokazuje więcej szczegółów niż ustawienia średnie i minimalne.\n\nWyświetla także opisy słów kluczowych używanych w umiejętnościach.
302. [Samouczek i wskazówki [tuto_01_04_01_05_title] — tekst] MID
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_05_title].content
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Samouczek i wskazówki [tuto_01_04_01_06] — tekst] 중간 정보 표시 설정입니다.\n\n최대 정보 표시와 차이점은 스킬에서 사용되는 키워드에 대한 정보가 표시되지 않습니다.\n\n그 외에는 최대 정보 표시와 같은 정보를 표시합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_06].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The medium information display configuration.\n\nIn this setting, details on Keywords used in Skills will not be shown.\n\nOtherwise, it functions the same as the maximum setting.
   PL: Konfiguracja średniej ilości informacji.\n\nW odróżnieniu od ustawienia maksymalnego ukrywa opisy słów kluczowych w umiejętnościach.\n\nPoza tym wyświetla te same informacje co ustawienie maksymalne.
304. [Samouczek i wskazówki [tuto_01_04_01_07_title] — tekst] MIN
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_07_title].content
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Samouczek i wskazówki [tuto_01_04_01_08] — tekst] 최소 정보 표시 설정입니다.\n\n최대 정보 표시, 중간 정보 표시와 다르게 스킬의 효과와 키워드에 대한 정보를 표시하지 않습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_04_01_08].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The minimum information display configuration.\n\nIn this setting, information on effects and Keywords of Skills will not be displayed.
   PL: Konfiguracja minimalnej ilości informacji.\n\nW odróżnieniu od ustawień MAX i MID nie wyświetla opisów efektów ani słów kluczowych umiejętności.
306. [Samouczek i wskazówki [tuto_01_08_01_01] — tekst] 이번에는 <color=#f8c200><E.G.O><color=#ebcaa2>에 대해 알려드리겠습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Let's learn how to use <color=#f8c200><E.G.O><color=#ebcaa2>.
   PL: Poznajmy teraz <color=#f8c200>„E.G.O”<color=#ebcaa2>.
307. [Samouczek i wskazówki [tuto_01_08_01_02] — tekst] <color=#f8c200><E.G.O><color=#ebcaa2>는 장착하기만 하면 <color=#f8c200>인격에 관계 없이<color=#ebcaa2> 사용할 수 있는 각 <color=#f8c200>수감자 고유의 스킬<color=#ebcaa2>입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_02].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200><E.G.O><color=#ebcaa2> are each Sinner's <color=#f8c200>unique Skills<color=#ebcaa2> that can be used <color=#f8c200>regardless of the Identity<color=#ebcaa2> they are wearing.
   PL: <color=#f8c200>„E.G.O”<color=#ebcaa2> to <color=#f8c200>unikalne umiejętności Grzeszników<color=#ebcaa2>, których po wyposażeniu można używać <color=#f8c200>niezależnie od Tożsamości<color=#ebcaa2>.
308. [Samouczek i wskazówki [tuto_01_08_01_03] — tekst] 히스클리프 수감자의 <color=#f8c200><E.G.O><color=#ebcaa2>를 확인해보죠.\n\n하단의 히스클리프 수감자 아이콘을 길게 꾹 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_03].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Let's inspect Sinner Heathcliff's <color=#f8c200>E.G.O<color=#ebcaa2>.\n\nPress and hold Sinner Heathcliff's portrait at the bottom of the Dashboard.
   PL: Sprawdźmy <color=#f8c200>„E.G.O”<color=#ebcaa2> Grzesznika Heathcliffa.\n\nNaciśnij i przytrzymaj portret Heathcliffa u dołu ekranu.
309. [Samouczek i wskazówki [tuto_01_08_01_04] — tekst] 현재 히스클리프 수감자가 장착한 <color=#f8c200><E.G.O><color=#ebcaa2>가 이곳에 모두 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Every <color=#f8c200><E.G.O><color=#ebcaa2> currently equipped by Sinner Heathcliff are visible here.
   PL: Tutaj widnieją wszystkie <color=#f8c200>„E.G.O”<color=#ebcaa2> wyposażone obecnie przez Heathcliffa.
310. [Samouczek i wskazówki [tuto_01_08_01_05] — tekst] <color=#f8c200><E.G.O><color=#ebcaa2> 스킬을 사용할 때\n<color=#f8c200>E.G.O 자원<color=#ebcaa2>과 <color=#f8c200>정신력<color=#ebcaa2>을 소모합니다.\n\n소모되는 정신력의 양은 <color=#f8c200><E.G.O><color=#ebcaa2> 정보의 좌측 상단에 표시됩니다.\n\n이제 <color=#f8c200>시체자루 <E.G.O><color=#ebcaa2>를 눌러보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_05].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Using <color=#f8c200><E.G.O><color=#ebcaa2> Skills consumes <color=#f8c200>E.G.O resources<color=#ebcaa2> and <color=#f8c200>SP<color=#ebcaa2>.\n\nThe amount of SP consumed by each <color=#f8c200><E.G.O><color=#ebcaa2> is listed at the top left corner of its information card.\n\nNow, select this <color=#f8c200><E.G.O><color=#ebcaa2>—'Bodysack'.
   PL: Użycie umiejętności <color=#f8c200>„E.G.O”<color=#ebcaa2> zużywa\n<color=#f8c200>zasoby E.G.O<color=#ebcaa2> oraz <color=#f8c200>PP<color=#ebcaa2>.\n\nKoszt PP widnieje w lewym górnym rogu karty informacji o <color=#f8c200>„E.G.O”<color=#ebcaa2>.\n\nKliknij teraz <color=#f8c200>„E.G.O” Worek na Zwłoki<color=#ebcaa2>.
311. [Samouczek i wskazówki [tuto_01_08_01_06] — tekst] 지금은 자원이 부족하여 <color=#f8c200>\n<E.G.O><color=#ebcaa2> 스킬을 사용할 수 없네요.\n\n모든 <color=#f8c200><E.G.O><color=#ebcaa2> 스킬에는 <color=#f8c200>E.G.O 자원<color=#ebcaa2>이 필요합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_06].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: It seems we don't have enough E.G.O resources to use the <color=#f8c200><E.G.O><color=#ebcaa2> Skill.\n\nEach <color=#f8c200><E.G.O><color=#ebcaa2> Skill requires a certain amount of <color=#f8c200>E.G.O resources<color=#ebcaa2> to activate.
   PL: Na razie brakuje zasobów, więc nie możemy użyć umiejętności <color=#f8c200>\n„E.G.O”<color=#ebcaa2>.\n\nKażda umiejętność <color=#f8c200>„E.G.O”<color=#ebcaa2> wymaga <color=#f8c200>zasobów E.G.O<color=#ebcaa2>.
312. [Samouczek i wskazówki [tuto_01_08_01_07] — tekst] 이곳에 <color=#f8c200><E.G.O><color=#ebcaa2>스킬을 사용하는 데 필요한 <color=#f8c200><E.G.O 자원><color=#ebcaa2>의 종류와 수가 표시됩니다.\n\n주황색 <color=#ff6600><색욕><color=#ebcaa2> 자원과 보라색 <color=#9500de><질투><color=#ebcaa2> 자원이 필요하네요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_07].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, <color=#ff6600>, <color=#9500de>, \n
   EN: Here, you can view the number of <E.G.O resources> and their Affinities required to use this <color=#f8c200><E.G.O><color=#ebcaa2> Skill.\n\nIt seems that we do not have enough Orange <color=#ff6600><Lust><color=#ebcaa2> and Purple <color=#9500de><Envy><color=#ebcaa2> E.G.O resources.
   PL: Tutaj pokazane są rodzaje i liczba <color=#f8c200>„zasobów E.G.O”<color=#ebcaa2> wymaganych do użycia tej umiejętności <color=#f8c200>„E.G.O”<color=#ebcaa2>.\n\nPotrzebujemy pomarańczowych zasobów <color=#ff6600>„Żądzy”<color=#ebcaa2> oraz fioletowych zasobów <color=#9500de>„Zawiści”<color=#ebcaa2>.
313. [Samouczek i wskazówki [tuto_01_08_01_08] — tekst] 보유한 <color=#f8c200><E.G.O 자원><color=#ebcaa2>은 이곳에서 확인할 수 있습니다.\n\n<color=#f8c200><E.G.O 자원><color=#ebcaa2>이라는 개념이 아직 생소하시겠지만, 스테이터스 창에서 속성 아이콘을 눌러 명칭을 확인할 수 있으니 참고해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_08].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: View your current <color=#f8c200><E.G.O resource><color=#ebcaa2> reserves here.\n\nThe names of each Sin Affinity for <color=#f8c200><E.G.O resources><color=#ebcaa2> may still be unfamiliar to you, but you can check which is which by selecting each E.G.O's Sin Affinity resistances in the detailed info window.
   PL: Posiadane <color=#f8c200>„zasoby E.G.O”<color=#ebcaa2> sprawdzisz w tym miejscu.\n\nJeśli nazwy grzechów <color=#f8c200>„zasobów E.G.O”<color=#ebcaa2> są ci jeszcze obce, możesz kliknąć ikony grzechów w oknie statusu, aby podejrzeć ich nazwy.
314. [Samouczek i wskazówki [tuto_01_08_01_09] — tekst] <color=#f8c200><E.G.O 자원><color=#ebcaa2>은 스킬을 사용하여 모을 수 있습니다.\n\n마침 현재 전투 중인 인원들이 필요한 속성의 스킬을 보유하고 있으니 사용해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_01_09].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Required <color=#f8c200><E.G.O resources><color=#ebcaa2> can be obtained by using Skills during battle. For example, an Envy-colored Skill will grant an Envy resource.\n\nAs luck would have it, the units currently on the field possess Skills with the Affinities we need. Put them to use.
   PL: <color=#f8c200>„Zasoby E.G.O”<color=#ebcaa2> gromadzisz, używając umiejętności w walce.\n\nNa szczęście obecni na polu bitwy Grzesznicy dysponują umiejętnościami potrzebnych grzechów — użyj ich.
315. [Samouczek i wskazówki [tuto_01_08_02_01] — tekst] <color=#f8c200>승률<color=#ebcaa2> 버튼을 눌러 전투를 명령해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_01].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Press the <color=#f8c200>Win Rate<color=#ebcaa2> button to order the Sinners to choose their own Skills based on Clash Win rate.
   PL: Naciśnij przycisk <color=#f8c200>Szansy<color=#ebcaa2>, aby wydać rozkaz do walki.
316. [Samouczek i wskazówki [tuto_01_08_02_02] — tekst] 현재 적 하나가 히스클리프 수감자에게 쉽게 받아내기 어려운 <color=#f8c200>강한 공격<color=#ebcaa2>을 사용하려고 합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_02].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: As you can see here, an enemy is about to launch a <color=#f8c200>powerful attack<color=#ebcaa2> against Sinner Heathcliff—and it's unlikely he will win this Clash.
   PL: Jeden z wrogów zamierza wyprowadzić przeciwko Heathcliffowi <color=#f8c200>potężny atak<color=#ebcaa2>, który trudno będzie odeprzeć.
317. [Samouczek i wskazówki [tuto_01_08_02_03] — tekst] 지금과 같이 <color=#f8c200><합><color=#ebcaa2> 승리가 어려울 때, <color=#f8c200><E.G.O><color=#ebcaa2> 스킬로 상황을 풀어나갈 수도 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_03].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: When a unit is about to <color=#f8c200><Clash><color=#ebcaa2> with a difficult enemy Skill, you can use an <color=#f8c200><E.G.O><color=#ebcaa2> Skill to turn the situation around.\nTheir high Power makes them especially effective against strong enemy Skills.
   PL: Gdy trudno wygrać <color=#f8c200>„Starcie”<color=#ebcaa2>, sytuację może uratować umiejętność <color=#f8c200>„E.G.O”<color=#ebcaa2>.\nJej wysoka Moc świetnie radzi sobie z groźnymi atakami.
318. [Samouczek i wskazówki [tuto_01_08_02_04] — tekst] 현재 보유한 자원으로 사용할 수 있는 <color=#f8c200><E.G.O><color=#ebcaa2> 스킬이 있으면 수감자 아이콘 주위에 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_04].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: If there are any usable <color=#f8c200><E.G.O><color=#ebcaa2> Skills for which you have enough resources, it will be indicated in the shape surrounding the Sinner, as shown here.
   PL: Jeśli posiadasz dość zasobów, aby użyć wyposażonego <color=#f8c200>„E.G.O”<color=#ebcaa2>, zostanie to zasygnalizowane wokół portretu Grzesznika.
319. [Samouczek i wskazówki [tuto_01_08_02_05] — tekst] 히스클리프 수감자 아이콘을 다시 꾹 눌러 <color=#f8c200><E.G.O><color=#ebcaa2> 선택 창으로 진입해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_05].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Press and hold Sinner Heathcliff's portrait again to enter the <color=#f8c200><E.G.O><color=#ebcaa2> selection menu.
   PL: Ponownie przytrzymaj portret Heathcliffa, aby otworzyć wybór <color=#f8c200>„E.G.O”<color=#ebcaa2>.
320. [Samouczek i wskazówki [tuto_01_08_02_06] — tekst] 이제 충분한 자원을 모아 <color=#f8c200><E.G.O><color=#ebcaa2> 스킬이 사용 가능해졌습니다.\n\n<color=#f8c200>시체자루<color=#ebcaa2>를 다시 선택하여 스킬 슬롯에 장착해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_06].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: You now have enough resources to use this <color=#f8c200><E.G.O><color=#ebcaa2> Skill.\n\nDouble-tap to select his <color=#f8c200>Bodysack<color=#ebcaa2> E.G.O Skill again and equip it in Heathcliff's Skill Slot.
   PL: Zebraliśmy dość zasobów, więc umiejętność <color=#f8c200>„E.G.O”<color=#ebcaa2> jest już dostępna.\n\nWybierz ponownie <color=#f8c200>Worek na Zwłoki<color=#ebcaa2>, aby umieścić go w slocie.
321. [Samouczek i wskazówki [tuto_01_08_02_07] — tekst] 선택한 <color=#f8c200><E.G.O><color=#ebcaa2>스킬은 하단 슬롯에 자동으로 장착됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_07].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Once selected, the <color=#f8c200><E.G.O><color=#ebcaa2> Skill will automatically be equipped in the bottom Skill Slot of the respective Sinner.
   PL: Wybrana umiejętność <color=#f8c200>„E.G.O”<color=#ebcaa2> zostaje automatycznie umieszczona w dolnym slocie danego Grzesznika.
322. [Samouczek i wskazówki [tuto_01_08_02_08] — tekst] <E.G.O> 스킬이 장착된 슬롯에 <color=#f8c200>다른 <E.G.O> 스킬을 장착<color=#ebcaa2>하거나, 해당 슬롯을 <color=#f8c200>수비 스킬로 변경<color=#ebcaa2>하면 장착했던 <E.G.O> 스킬은 해제되며, E.G.O 자원도 반환됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_08].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Equipping a different <E.G.O> Skill<color=#ebcaa2> in the same Slot, or swapping it for a <color=#f8c200>Defense Skill<color=#ebcaa2>, will unequip the current <E.G.O> Skill and refund the E.G.O resources spent to equip it.
   PL: Jeśli w slocie z „E.G.O” <color=#f8c200>umieścisz inne „E.G.O”<color=#ebcaa2> lub zamienisz go na <color=#f8c200>umiejętność obrony<color=#ebcaa2>, poprzednie „E.G.O” zostanie zdjęte, a zasoby E.G.O zwrócone.
323. [Samouczek i wskazówki [tuto_01_08_02_09] — tekst] 이제 다시 전투를 진행해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_09].content
   limit: do 120 znaków
   EN: Now, let's return to the battle at hand.
   PL: Wznów teraz walkę.
324. [Samouczek i wskazówki [tuto_01_08_02_10] — tekst] <color=#f8c200><E.G.O><color=#ebcaa2> 스킬로 공격을 시작할 때\n필요한 <color=#f8c200>정신력이 소모<color=#ebcaa2>됩니다.\n\n정신력이 지나치게 낮아지면 수감자가 <color=#f8c200>패닉<color=#ebcaa2> 상태에 빠지거나 <color=#f8c200><E.G.O><color=#ebcaa2>에 <color=#f8c200>침식<color=#ebcaa2>될 수 있으니 주의하세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_02_10].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The <color=#f8c200>SP cost is consumed<color=#ebcaa2> the moment the <color=#f8c200><E.G.O><color=#ebcaa2> Skill begins its attack.\n\nBe warned: letting a Sinner's SP drop too low may cause them to <color=#f8c200>Panic<color=#ebcaa2> or become <color=#f8c200>Corroded<color=#ebcaa2> by their <color=#f8c200><E.G.O><color=#ebcaa2>.
   PL: W momencie rozpoczęcia ataku umiejętnością <color=#f8c200>„E.G.O”<color=#ebcaa2>\nzużywane są wymagane <color=#f8c200>PP<color=#ebcaa2>.\n\nUważaj: przy zbyt niskich PP Grzesznik może wpaść w <color=#f8c200>Panikę<color=#ebcaa2> lub ulec <color=#f8c200>Korozji<color=#ebcaa2> swojego <color=#f8c200>„E.G.O”<color=#ebcaa2>.
325. [Samouczek i wskazówki [tuto_01_08_03_01] — tekst] <E.G.O> 스킬의 해석 단계를 올리면, <color=#f8c200><E.G.O> 패시브<color=#ebcaa2>가 <E.G.O> 스킬을 사용한 <color=#f8c200>다음 턴<color=#ebcaa2>부터 <color=#f8c200>활성화<color=#ebcaa2>됩니다.\n\n<E.G.O> 패시브의 효과는 수감자의 정보창에서 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_08_03_01].content
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Raising an <E.G.O> Skill's Threadspinning Tier unlocks its <color=#f8c200><E.G.O> Passive<color=#ebcaa2>.\nOnce the turn in which this unit used the <E.G.O> Skill ends and the battle moves to the <color=#f8c200>next turn<color=#ebcaa2>, the Skill's unique <color=#f8c200><E.G.O> Passive<color=#ebcaa2> will activate.\n\nYou can view detailed information about <E.G.O> Passives in each Sinner's detailed info menu.
   PL: Podniesienie stopnia Splotu Nici „E.G.O” sprawia, że od <color=#f8c200>następnej tury<color=#ebcaa2> po użyciu tej umiejętności <color=#f8c200>aktywuje się<color=#ebcaa2> <color=#f8c200>pasywka „E.G.O”<color=#ebcaa2>.\n\nDziałanie pasywki „E.G.O” sprawdzisz w oknie informacji o Grzeszniku.
326. [Samouczek i wskazówki [tuto_01_09_01_01] — tekst] 이번 전투에서는 <E.G.O>에 대해 더 자세히 알아보겠습니다.\n료슈 수감자의 정신력이 높은 상태로 시작합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_01].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In this Encounter, we will learn about more advanced usage of <E.G.O>.\nSinner Ryōshū will begin with a higher SP value for demonstration purposes.
   PL: W tym starciu przyjrzymy się bliżej działaniu „E.G.O”.\nGrzeszniczka Ryōshū zaczyna walkę z wysoką wartością PP.
327. [Samouczek i wskazówki [tuto_01_09_01_02] — tekst] 기본 E.G.O 스킬을 제외한 다른 E.G.O 스킬은 <color=#f8c200><E.G.O 오버클록><color=#ebcaa2>이 가능합니다.\n료슈 수감자의 아이콘을 길게 눌러 E.G.O를 확인해보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_02].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Every E.G.O Skill, except for Base E.G.O Skills, can be <color=#f8c200><Overclocked><color=#ebcaa2>.\nPress and hold Sinner Ryōshū's portrait to bring up the list of her E.G.O.
   PL: Wszystkie umiejętności E.G.O oprócz podstawowych pozwalają użyć <color=#f8c200>„Przeciążenia E.G.O”<color=#ebcaa2>.\nPrzytrzymaj portret Ryōshū, aby sprawdzić jej E.G.O.
328. [Samouczek i wskazówki [tuto_01_09_01_03] — tekst] 가장 먼저 료슈의 새로운 E.G.O 각성 스킬을 사용해보겠습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_03].content
   limit: do 120 znaków
   EN: Let's first try using Ryōshū's newly acquired E.G.O Awakening Skill.
   PL: Użyjmy najpierw nowej umiejętności Przebudzenia E.G.O Ryōshū.
329. [Samouczek i wskazówki [tuto_01_09_01_04] — tekst] <color=#f8c200>E.G.O를 사용<color=#ebcaa2>하면, 해당 수감자의 <color=#f8c200>죄악 내성이 변경<color=#ebcaa2>됩니다.\n적에 따라 내성을 바꾸면 전투를 보다 유리하게 끌어갈 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: You can <color=#f8c200>change the Sinner's Sin Resistances<color=#ebcaa2> by <color=#f8c200>using their E.G.O<color=#ebcaa2>.\nCheck the Sin Affinities of enemy Skills, and use an appropriate E.G.O to adjust your Resistances and gain an advantage.
   PL: <color=#f8c200>Użycie E.G.O<color=#ebcaa2> <color=#f8c200>zmienia odporności na grzechy<color=#ebcaa2> danego Grzesznika.\nDopasowując odporności do ataków wroga, zyskasz przewagę w walce.
330. [Samouczek i wskazówki [tuto_01_09_01_05] — tekst] 다시 한 번 E.G.O 스킬을 사용해보겠습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_05].content
   limit: do 120 znaków
   EN: Let's use that E.G.O Skill again.
   PL: Użyjmy umiejętności E.G.O jeszcze raz.
331. [Samouczek i wskazówki [tuto_01_09_01_06] — tekst] E.G.O 스킬은 <color=#f8c200>정신력<color=#ebcaa2>이 낮을수록 <color=#f8c200>침식<color=#ebcaa2>될 확률이 높아집니다. 침식 시 피아식별이 불가능한 침식 스킬을 사용하니 주의하세요.\n침식 확률은 이 곳에서 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_06].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: E.G.O Skills have a chance to <color=#f8c200>Corrode<color=#ebcaa2> at lower <color=#f8c200>SP<color=#ebcaa2> values.\nBe warned: Corrosion causes the Sinner to use a Corrosion Skill, which attacks allies and enemies indiscriminately.\nYou can view the Corrosion chance here.
   PL: Im niższe <color=#f8c200>PP<color=#ebcaa2>, tym większa szansa, że umiejętność E.G.O wywoła <color=#f8c200>Korozję<color=#ebcaa2>. Uwaga: przy Korozji używana jest umiejętność Korozji atakująca bez rozróżnienia sojuszników i wrogów.\nSzansę Korozji sprawdzisz tutaj.
332. [Samouczek i wskazówki [tuto_01_09_01_07] — tekst] 정신력이 <color=#f8c200>-45<color=#ebcaa2>가 되면, 확정적으로 <color=#f8c200><E.G.O 침식 상태><color=#ebcaa2>가 됩니다.\n<color=#f8c200><E.G.O 침식 상태><color=#ebcaa2>에서는 아군과 적군을 가리지 않고 공격하게 됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_07].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Reaching <color=#f8c200>-45 SP<color=#ebcaa2> will guarantee that the Sinner enters <color=#f8c200><E.G.O Corrosion><color=#ebcaa2> state.\nIn an <color=#f8c200><E.G.O Corrosion><color=#ebcaa2> state, the Sinner will indiscriminately attack both allies and enemies.
   PL: Gdy PP spadną do <color=#f8c200>-45<color=#ebcaa2>, Grzesznik niezawodnie wpada w <color=#f8c200>„stan Korozji E.G.O”<color=#ebcaa2>.\nW <color=#f8c200>„stanie Korozji E.G.O”<color=#ebcaa2> atakuje na oślep zarówno sojuszników, jak i wrogów.
333. [Samouczek i wskazówki [tuto_01_09_01_08] — tekst] 다음 턴이 되면 <color=#f8c200><E.G.O 침식 상태><color=#ebcaa2>가 종료되고\n정신력은 0으로 돌아옵니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_08].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The Sinner will recover from the <color=#f8c200><E.G.O Corrosion><color=#ebcaa2> state next turn, and their SP will reset to 0.
   PL: W następnej turze <color=#f8c200>„stan Korozji E.G.O”<color=#ebcaa2> dobiega końca,\na PP wracają do 0.
334. [Samouczek i wskazówki [tuto_01_09_01_09] — tekst] 이번에는 <color=#f8c200><E.G.O 오버클록><color=#ebcaa2>을 사용해보겠습니다. 료슈 수감자의 아이콘를 길게 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_09].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Let's try the <color=#f8c200><E.G.O Overclock><color=#ebcaa2> this time. Press and hold Ryōshū's portrait.
   PL: Wypróbujmy teraz <color=#f8c200>„Przeciążenie E.G.O”<color=#ebcaa2>. Przytrzymaj portret Ryōshū.
335. [Samouczek i wskazówki [tuto_01_09_01_10] — tekst] E.G.O 스킬을 길게 눌러, <color=#f8c200><E.G.O 오버클록><color=#ebcaa2> 상태로 변경해주세요.\n<E.G.O 오버클록>은 <color=#f8c200><E.G.O>를 강제로 침식 스킬로 발동<color=#ebcaa2>시키는 기능입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_10].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Press and hold the E.G.O Skill card to <color=#f8c200><E.G.O Overclock><color=#ebcaa2> it.\nUsing <E.G.O Overclock> <color=#f8c200>forces the Sinner to use the Corrosion Skill<color=#ebcaa2> of the <E.G.O>.
   PL: Przytrzymaj kartę E.G.O, aby przełączyć ją w stan <color=#f8c200>„Przeciążenia E.G.O”<color=#ebcaa2>.\n„Przeciążenie E.G.O” <color=#f8c200>wymusza aktywację E.G.O jako umiejętności Korozji<color=#ebcaa2>.
336. [Samouczek i wskazówki [tuto_01_09_01_11] — tekst] 오버클록시 자원이 충분하면 <color=#f8c200>안정 오버클록<color=#ebcaa2>, 그렇지 않다면 <color=#f8c200>불안정 오버클록<color=#ebcaa2>으로 시전됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_11].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: If you have enough resources to use the Overclocked E.G.O Skill, it will activate as <color=#f8c200>Stable Overclock<color=#ebcaa2>. If not, it will activate as <color=#f8c200>Unstable Overclock<color=#ebcaa2>.
   PL: Jeśli masz dość zasobów na Przeciążenie, nastąpi <color=#f8c200>Stabilne Przeciążenie<color=#ebcaa2>, a w przeciwnym razie — <color=#f8c200>Niestabilne Przeciążenie<color=#ebcaa2>.
337. [Samouczek i wskazówki [tuto_01_09_01_12_title] — tekst] 안정 오버클록
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_12_title].content
   limit: do 120 znaków
   EN: Stable Overclock
   PL: Stabilne Przeciążenie
338. [Samouczek i wskazówki [tuto_01_09_01_12] — tekst] <color=#f8c200><안정 오버클록><color=#ebcaa2> 상태에선 정신력을 포함하여 기존에 소모되는 <color=#f8c200>자원을 1.5배만큼 소모<color=#ebcaa2>하며, <color=#f8c200>아군을 공격하지 않습니다.<color=#ebcaa2>\n다만, <color=#f8c200>정신력이 낮으면<color=#ebcaa2> 오버클록으로도 <color=#f8c200>침식 상태<color=#ebcaa2>가 될 수 있으니 주의하세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_12].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Activating <color=#f8c200><Stable Overclock><color=#ebcaa2> consumes <color=#f8c200>1.5 times the resources (including SP)<color=#ebcaa2> compared to a non-Overclocked E.G.O, but it does <color=#f8c200>not target allies<color=#ebcaa2>.\nWarning: Even a Stable Overclock can <color=#f8c200>Corrode<color=#ebcaa2> your Sinners if their <color=#f8c200>SP value is low<color=#ebcaa2>.
   PL: <color=#f8c200>„Stabilne Przeciążenie”<color=#ebcaa2> <color=#f8c200>zużywa 1,5 raza więcej zasobów<color=#ebcaa2> (w tym PP), lecz <color=#f8c200>nie atakuje sojuszników<color=#ebcaa2>.\nUważaj jednak: przy <color=#f8c200>niskich PP<color=#ebcaa2> nawet Przeciążenie może wpędzić w <color=#f8c200>stan Korozji<color=#ebcaa2>.
339. [Samouczek i wskazówki [tuto_01_09_01_13_title] — tekst] 불안정 오버클록
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_13_title].content
   limit: do 120 znaków
   EN: Unstable Overclock
   PL: Niestabilne Przeciążenie
340. [Samouczek i wskazówki [tuto_01_09_01_13] — tekst] <color=#f8c200><E.G.O 오버클록><color=#ebcaa2> 시 자원이 부족한 경우\n<color=#f8c200><불안정 오버클록><color=#ebcaa2>으로 발동됩니다.\n이 상태에선 침식 스킬과 동일하게 <color=#f8c200>피아식별이 불가능<color=#ebcaa2>하며, <color=#f8c200>부족한 E.G.O자원이 마이너스로 저장<color=#ebcaa2>됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_09_01_13].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Activating <color=#f8c200><E.G.O Overclock><color=#ebcaa2> without enough resources will trigger <color=#f8c200><Unstable Overclock><color=#ebcaa2> instead.\nUnstable Overclock targets both allies and enemies <color=#f8c200>indiscriminately<color=#ebcaa2>, like E.G.O Corrosion, and any <color=#f8c200>insufficient E.G.O resources will go into the negatives<color=#ebcaa2>.
   PL: Gdy przy <color=#f8c200>„Przeciążeniu E.G.O”<color=#ebcaa2> brakuje zasobów,\nuruchamiane jest <color=#f8c200>„Niestabilne Przeciążenie”<color=#ebcaa2>.\nTak jak przy Korozji <color=#f8c200>nie odróżnia ono swoich od wrogów<color=#ebcaa2>, a <color=#f8c200>brakujące zasoby E.G.O spadają poniżej zera<color=#ebcaa2>.
341. [Samouczek i wskazówki [tuto_01_11_abbattle_01_01] — tekst] 던전에는 <color=#f8c200>환상체<color=#ebcaa2>라는 것이 존재합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Entities known as <color=#f8c200>Abnormalities<color=#ebcaa2> may be found in Dungeons.
   PL: W Lochach napotkasz istoty zwane <color=#f8c200>Anomaliami<color=#ebcaa2>.
342. [Samouczek i wskazówki [tuto_01_11_abbattle_01_02] — tekst] 환상체와의 전투는 여태까지의 전투와 다른 전투 방식으로 진행됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_02].content
   limit: do 120 znaków
   EN: A different kind of approach is needed in Encounters against Abnormalities.
   PL: Walki z Anomaliami przebiegają w innym trybie niż dotychczasowe starcia.
343. [Samouczek i wskazówki [tuto_01_11_abbattle_01_03] — tekst] 이러한 전투 방식을 <color=#f8c200>집중 전투<color=#ebcaa2>라고 하며, 이제부터 설명드리겠습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_03].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Battles that employ this different approach are called <color=#f8c200>Focused Encounters<color=#ebcaa2>. Let's explore its mechanics.
   PL: Ten tryb walki nazywa się <color=#f8c200>starciem skupionym<color=#ebcaa2> — wyjaśnię teraz jego zasady.
344. [Samouczek i wskazówki [tuto_01_11_abbattle_01_04] — tekst] 환상체는 하나 이상의 <color=#f8c200>부위<color=#ebcaa2>가 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: All abnormalities have one or more <color=#f8c200>Parts<color=#ebcaa2>.
   PL: Każda Anomalia posiada jedną lub więcej <color=#f8c200>części<color=#ebcaa2>.
345. [Samouczek i wskazówki [tuto_01_11_abbattle_01_05] — tekst] 각 부위별로 스킬 슬롯이 배정되며, 속도가 결정됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_05].content
   limit: do 120 znaków
   EN: Each Part has their own set of Skill Slots and Speed values.
   PL: Każdej części przypisywane są osobne sloty umiejętności oraz Szybkość.
346. [Samouczek i wskazówki [tuto_01_11_abbattle_01_06_title] — tekst] 환상체의 부위
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_06_title].content
   limit: do 120 znaków
   EN: Abnormality Parts
   PL: Części Anomalii
347. [Samouczek i wskazówki [tuto_01_11_abbattle_01_06] — tekst] 모든 환상체는 1개 이상의 부위가 있습니다.\n\n각 부위별로 스킬 슬롯이 존재하며, 턴마다 부위별로 속도가 결정됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_06].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abnormalities often have multiple Parts that can be targeted.\n\nEach Part uses Skills from its assigned Skill Slots, and its Speed values can change from turn to turn.
   PL: Każda Anomalia składa się z co najmniej 1 części.\n\nKażda część ma własne sloty umiejętności, a jej Szybkość losowana jest co turę.
348. [Samouczek i wskazówki [tuto_01_11_abbattle_01_07] — tekst] 집중 전투에서는 아군의 스킬을 선택한 후, <color=#f8c200>직접<color=#ebcaa2> 환상체의 스킬 슬롯에 연결해야 합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_07].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: In Focused Encounters, you must select the Sinners' Skill icons and chain them <color=#f8c200>directly<color=#ebcaa2> to the Abnormalities' Skill Slots.
   PL: W starciu skupionym musisz wybrać umiejętność sojusznika i <color=#f8c200>bezpośrednio<color=#ebcaa2> połączyć ją ze slotem umiejętności Anomalii.
349. [Samouczek i wskazówki [tuto_01_11_abbattle_01_08] — tekst] 조작 패널 첫 번째 열에 배치된 수감자의 스킬을 선택해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_08].content
   limit: do 120 znaków
   EN: Select a Skill from the leftmost column of the Dashboard.
   PL: Wybierz umiejętność Grzesznika z pierwszej kolumny panelu dowodzenia.
350. [Samouczek i wskazówki [tuto_01_11_abbattle_01_09] — tekst] 선택한 아군의 스킬을 표시된 <color=#f8c200>적 스킬 슬롯과 연결<color=#ebcaa2>해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_09].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Now, drag from the selected Skill to <color=#f8c200>this enemy Skill Slot to chain them<color=#ebcaa2>.
   PL: Połącz wybraną umiejętność sojusznika ze wskazanym <color=#f8c200>slotem umiejętności wroga<color=#ebcaa2>.
351. [Samouczek i wskazówki [tuto_01_11_abbattle_01_10] — tekst] 방금과 같이 아군의 스킬을 적 스킬 슬롯에 직접 연결하는 것이 집중 전투의 기본입니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_10].content
   limit: do 140 znaków
   EN: Remember: in Focused Encounters, you connect the Sinners' Skills directly to the enemies' Skill Slots.
   PL: Bezpośrednie łączenie umiejętności sojuszników ze slotami umiejętności wrogów to podstawa starcia skupionego.
352. [Samouczek i wskazówki [tuto_01_11_abbattle_01_11] — tekst] 만약 전투의 전반적인 상황을 확인하기 위해 시야를 원래대로 되돌리고 싶으시다면, 왼쪽 기어를 눌러주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_11].content
   limit: do 130 znaków
   EN: Please press the gear on the left if you would like to zoom out and view the entire battlefield.
   PL: Jeśli chcesz oddalić kamerę, aby ogarnąć wzrokiem całe pole bitwy, naciśnij lewą zębatkę.
353. [Samouczek i wskazówki [tuto_01_11_abbattle_01_12] — tekst] 시야가 확대된 상태에서 왼쪽 기어를 누르면\n전투 시작 시점의 시야로 초기화 됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_12].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pressing the gear on the left while zoomed in\nwill reset your field of view.
   PL: Naciśnięcie lewej zębatki przy przybliżonym widoku\nprzywraca domyślną kamerę z początku walki.
354. [Samouczek i wskazówki [tuto_01_11_abbattle_01_13] — tekst] 조작 패널에 배치된 아군의 스킬을 <color=#f8c200>전부 연결<color=#ebcaa2>해야 전투를 진행할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_13].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Once you have <color=#f8c200>connected every available Skill to the enemies' Skill Slots<color=#ebcaa2>, the gear icon on the right—the button to enter the combat phase—will activate. Only then can you proceed to the Combat Phase.
   PL: Aby rozpocząć fazę walki, musisz <color=#f8c200>połączyć wszystkie umiejętności<color=#ebcaa2> sojuszników z panelu dowodzenia.
355. [Samouczek i wskazówki [tuto_01_11_abbattle_01_14] — tekst] <color=#f8c200>모든 수감자의 스킬을 적 슬롯에 연결<color=#ebcaa2>한 뒤 전투 명령을 내려주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_01_14].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Now, <color=#f8c200>chain every Sinner's Skills to the enemy Slots<color=#ebcaa2>, then start the combat phase using the gear icon on the right.
   PL: <color=#f8c200>Połącz umiejętności wszystkich Grzeszników ze slotami wroga<color=#ebcaa2> i wydaj rozkaz do walki.
356. [Samouczek i wskazówki [tuto_01_11_abbattle_02_01] — tekst] 집중 전투는 <color=#f8c200>속도<color=#ebcaa2> 순으로 진행됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Speed<color=#ebcaa2> determines the order of actions taken in Focused Encounters.
   PL: Starcie skupione przebiega w kolejności <color=#f8c200>Szybkości<color=#ebcaa2>.
357. [Samouczek i wskazówki [tuto_01_11_abbattle_02_02] — tekst] 현재 턴의 각 캐릭터 속도는 <color=#f8c200>전투 슬롯 근처<color=#ebcaa2>에서 확인할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: The Speed assigned to each unit for this turn can be viewed here, <color=#f8c200>next to their Skill Slots<color=#ebcaa2>.
   PL: Szybkość każdej jednostki w bieżącej turze widnieje <color=#f8c200>obok jej slotów umiejętności<color=#ebcaa2>.
358. [Samouczek i wskazówki [tuto_01_11_abbattle_02_03] — tekst] 아군의 속도는 <color=#f8c200>조작 패널<color=#ebcaa2>에서도 확인 가능합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Speed of allied units can be viewed here <color=#f8c200>on the Dashboard<color=#ebcaa2> as well.
   PL: Szybkość sojuszników sprawdzisz również na <color=#f8c200>panelu dowodzenia<color=#ebcaa2>.
359. [Samouczek i wskazówki [tuto_01_11_abbattle_02_04] — tekst] 집중 전투에서는 방금과 같이 공격 대상을\n<color=#f8c200>직접 지정<color=#ebcaa2>해야 합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_04].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: As you have just seen, Focused Encounters are conducted by chaining your units' Skills <color=#f8c200>directly<color=#ebcaa2> to enemy Skill Slots.
   PL: W starciu skupionym musisz w ten właśnie sposób\n<color=#f8c200>samodzielnie wskazywać<color=#ebcaa2> cele ataków.
360. [Samouczek i wskazówki [tuto_01_11_abbattle_02_05] — tekst] 다음은 적에게 집중적으로 공격당하는 상황의 대응 방법입니다.\n공격 슬롯을 확인해 보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_05].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Now, let's learn how to handle situations where several enemies are focusing on a single allied unit.\nHover over then select this unit's Slot here.
   PL: Zobaczmy teraz, jak radzić sobie, gdy wrogowie skupiają ataki na jednym sojuszniku.\nSprawdź ten slot ataku.
361. [Samouczek i wskazówki [tuto_01_11_abbattle_02_06] — tekst] <color=#f8c200>아군의 속도가 적보다 빠르면<color=#ebcaa2>, 해당 아군으로 적의 <color=#f8c200>공격 대상을 변경하여 <합><color=#ebcaa2>을 진행할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_06].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Allies with faster Speeds<color=#ebcaa2> can force enemies with slower Speeds to <color=#f8c200>redirect their attacks and <Clash> with them<color=#ebcaa2> instead by chaining their own Skill against the enemy's.
   PL: <color=#f8c200>Jeśli sojusznik jest szybszy od wroga<color=#ebcaa2>, może <color=#f8c200>przekierować jego cel ataku na siebie i wywołać „Starcie”<color=#ebcaa2>.
362. [Samouczek i wskazówki [tuto_01_11_abbattle_02_07] — tekst] 속도가 높은 수감자로 스킬을 지정해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_07].content
   limit: do 120 znaków
   EN: Select a faster Sinner and chain their Skill against the enemy's.
   PL: Wskaż umiejętność szybszego Grzesznika przeciw temu wrogowi.
363. [Samouczek i wskazówki [tuto_01_11_abbattle_02_08] — tekst] 속도가 높은 수감자로 스킬을 지정해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_08].content
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Samouczek i wskazówki [tuto_01_11_abbattle_02_09] — tekst] 이렇게 적보다 속도가 빠르면, 적의 공격 대상을 전투에 <color=#f8c200>유리한 방향으로 변경<color=#ebcaa2>할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_09].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: As demonstrated here, allies with faster Speeds than the enemy can <color=#f8c200>strategically draw attacks targeting other allies to themselves<color=#ebcaa2> depending on the flow of battle.
   PL: Gdy sojusznik ma wyższą Szybkość od wroga, możesz w ten sposób <color=#f8c200>korzystnie przekierowywać ataki<color=#ebcaa2>.
365. [Samouczek i wskazówki [tuto_01_11_abbattle_02_10_title] — tekst] 속도가 빠른 경우
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_10_title].content
   limit: do 120 znaków
   EN: When Ally's Speed > Enemy's Speed
   PL: Gdy Szybkość jest wyższa
366. [Samouczek i wskazówki [tuto_01_11_abbattle_02_10] — tekst] <color=#f8c200>아군의 속도가 적보다 빠르면<color=#ebcaa2>, 적의 <color=#f8c200>공격 대상<color=#ebcaa2>을 해당 아군으로 <color=#f8c200>변경<color=#ebcaa2>할 수 있습니다.\n\n이 과정에서 <color=#f8c200>합<color=#ebcaa2>이 발생합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_10].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: <color=#f8c200>If an allied unit's Speed is faster than the enemy unit's<color=#ebcaa2>, the allied unit can <color=#f8c200>redirect<color=#ebcaa2> the <color=#f8c200>targeting<color=#ebcaa2> of the enemy's Skill to themselves.\n\nOnce redirected, the allied unit and the enemy unit will <color=#f8c200>Clash<color=#ebcaa2>.
   PL: <color=#f8c200>Gdy sojusznik jest szybszy od wroga<color=#ebcaa2>, może <color=#f8c200>zmienić<color=#ebcaa2> <color=#f8c200>cel ataku<color=#ebcaa2> wroga na siebie.\n\nDochodzi wówczas do <color=#f8c200>Starcia<color=#ebcaa2>.
367. [Samouczek i wskazówki [tuto_01_11_abbattle_02_11] — tekst] <color=#f8c200>원래 타겟<color=#ebcaa2>이었던 수감자는 <color=#f8c200>속도에 상관없이<color=#ebcaa2> 대상 적과 <color=#f8c200>합<color=#ebcaa2>을 진행할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_11].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Another thing to note regarding targeting and redirecting: an <color=#f8c200>allied unit targeted by an enemy Skill<color=#ebcaa2> can still <color=#f8c200>Clash<color=#ebcaa2> against that Skill, <color=#f8c200>regardless of their own Speed<color=#ebcaa2>.
   PL: Grzesznik będący <color=#f8c200>pierwotnym celem<color=#ebcaa2> może stoczyć z tym wrogiem <color=#f8c200>Starcie<color=#ebcaa2> <color=#f8c200>niezależnie od Szybkości<color=#ebcaa2>.
368. [Samouczek i wskazówki [tuto_01_11_abbattle_02_12] — tekst] 스킬을 다시 지정해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_12].content
   limit: do 120 znaków
   EN: Chain your Skills against the enemy's.
   PL: Wyznacz umiejętności jeszcze raz.
369. [Samouczek i wskazówki [tuto_01_11_abbattle_02_13] — tekst] 스킬을 다시 지정해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_13].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Samouczek i wskazówki [tuto_01_11_abbattle_02_14_title] — tekst] 스킬의 타겟인 경우
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_14_title].content
   limit: do 120 znaków
   EN: When targeted by enemy Skills
   PL: Gdy sojusznik jest celem umiejętności
371. [Samouczek i wskazówki [tuto_01_11_abbattle_02_14] — tekst] 적의 공격 대상인 아군은 <color=#f8c200>속도와 상관없이 합<color=#ebcaa2>이 가능합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_14].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Allies targeted by enemy Skills can Clash against Skills targeting themselves <color=#f8c200>regardless of Speed<color=#ebcaa2>.
   PL: Sojusznik będący celem ataku wroga może wejść w <color=#f8c200>Starcie niezależnie od Szybkości<color=#ebcaa2>.
372. [Samouczek i wskazówki [tuto_01_11_abbattle_02_15] — tekst] 속도가 같거나 느려 합을 이끌어오지 못하는 경우에는\n<color=#05DBF2>일방 공격<color=#ebcaa2>이 발생할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_15].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#05DBF2>, <color=#ebcaa2>, \n
   EN: If an allied unit's Speed is equal to or slower than the enemy's, they cannot redirect the enemy Skill and may instead perform an <color=#05DBF2>Unopposed Attack<color=#ebcaa2>.
   PL: Gdy Szybkość jest równa lub niższa i nie można przejąć Starcia,\nmoże dojść do <color=#05DBF2>ataku jednostronnego<color=#ebcaa2>.
373. [Samouczek i wskazówki [tuto_01_11_abbattle_02_16_title] — tekst] 속도가 같거나 느린 경우
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_16_title].content
   limit: do 120 znaków
   EN: When Ally's Speed ≤ Enemy's Speed
   PL: Gdy Szybkość jest równa lub niższa
374. [Samouczek i wskazówki [tuto_01_11_abbattle_02_16] — tekst] 아군의 속도가 적과 같거나 느리면 적의 공격 대상을 변경할 수 없습니다.\n이 경우 합이 아닌 <color=#05DBF2>일방 공격(파란색 화살표)<color=#ebcaa2>이 이루어집니다.\n\n<color=#05DBF2>일방 공격<color=#ebcaa2>은 합이 발생하지 않으며, 공격만 진행됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_16].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#05DBF2>, <color=#ebcaa2>, \n
   EN: Allies with lower or equal Speed values cannot force enemies with faster Speed to target them.\nIn such cases, both units will perform an <color=#05DBF2>Unopposed Attack (marked by blue arrows)<color=#ebcaa2> instead of engaging in a Clash first. Faster unit will attack first.\n\n<color=#05DBF2>Unopposed Attacks<color=#ebcaa2> skip Clashes and strike directly.
   PL: Gdy sojusznik ma Szybkość równą lub niższą od wroga, nie może zmienić celu jego ataku.\nZamiast Starcia następuje wówczas <color=#05DBF2>atak jednostronny (niebieska strzałka)<color=#ebcaa2>.\n\n<color=#05DBF2>Atak jednostronny<color=#ebcaa2> pomija Starcie i od razu wyprowadza uderzenie.
375. [Samouczek i wskazówki [tuto_01_11_abbattle_02_17] — tekst] 같은 슬롯을 여러 스킬로 공격해도 합으로 지정된 스킬 외에는 <color=#05DBF2>일방 공격<color=#ebcaa2>이 발생합니다.\n피해를 감수하고 <color=#f8c200>합<color=#ebcaa2>대신 <color=#05DBF2>일방 공격<color=#ebcaa2>으로\n집중적인 공격을 명령할 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_abbattle_02_17].content
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: <color=#05DBF2>, <color=#ebcaa2>, <color=#f8c200>, \n
   EN: While multiple Skills may target a single Slot, only the last Skill chained to it will Clash; the others will activate as <color=#05DBF2>Unopposed Attacks<color=#ebcaa2>.\nSometimes, it can be an effective strategy to forgo <color=#f8c200>Clashes<color=#ebcaa2> and have multiple units use <color=#05DBF2>Unopposed Attacks<color=#ebcaa2> against a single dangerous enemy, even if it leaves them exposed to attacks from others.
   PL: Gdy kilka umiejętności celuje w ten sam slot, poza umiejętnością w Starciu pozostałe wykonują <color=#05DBF2>atak jednostronny<color=#ebcaa2>.\nCzasem warto przyjąć obrażenia i zamiast <color=#f8c200>Starcia<color=#ebcaa2> rozkazać zmasowany <color=#05DBF2>atak jednostronny<color=#ebcaa2>\nw jednego groźnego przeciwnika.
376. [Samouczek i wskazówki [tuto_01_11_snow_white_01_01] — tekst] 새로운 환상체가 등장했어요. 환상체의 도감을 확인해보죠.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_01_01].content
   limit: do 120 znaków
   EN: You have encountered a new Abnormality. Please view its Abnormality Guide.
   PL: Pojawiła się nowa Anomalia. Sprawdźmy jej wpis w Kompendium Anomalii.
377. [Samouczek i wskazówki [tuto_01_11_snow_white_01_02_title] — tekst] 환상체 도감
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_01_02_title].content
   limit: do 120 znaków
   EN: The Abnormality Guide
   PL: Kompendium Anomalii
378. [Samouczek i wskazówki [tuto_01_11_snow_white_01_02] — tekst] 환상체 도감에는 환상체의 정보가 기록되어있습니다.\n<color=#f8c200>도감은 환상체를 상대하면서 점차 완성<color=#ebcaa2>됩니다.\n\n환상체는 여러 번 조우하고 전투할수록 <color=#f8c200>관찰 단계<color=#ebcaa2>가 증가하며, 환상체에게 입히는 피해량이 소폭 증가합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_01_02].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: The Abnormality Guide lists information about the Abnormality.\n<color=#f8c200>The guide will gradually fill up as you battle the Abnormality.<color=#ebcaa2>\n\nRaise the <color=#f8c200>Observation Level<color=#ebcaa2> by repeatedly encountering and battling the Abnormality.\nHigher Observation Levels slightly increases the damage you deal against the Abnormality.
   PL: W Kompendium Anomalii zapisywane są informacje o Anomaliach.\n<color=#f8c200>Kompendium uzupełnia się stopniowo podczas walk z Anomalią.<color=#ebcaa2>\n\nWielokrotne spotkania i walki podnoszą <color=#f8c200>Poziom Obserwacji<color=#ebcaa2>, co nieznacznie zwiększa obrażenia zadawane danej Anomalii.
379. [Samouczek i wskazówki [tuto_01_11_snow_white_01_03] — tekst] 던전에는 <color=#f8c200>여러 개의 부위<color=#ebcaa2>를 가진 환상체도 존재합니다.\n각 부위마다 내성과 사용하는 스킬, 패시브가 다를 수 있습니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_01_03].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: You may encounter Abnormalities with <color=#f8c200>multiple Parts<color=#ebcaa2> in the dungeons you explore.\nIn such cases, each Part may have different Resistances, Passives, and Skills.
   PL: W Lochach spotkasz też Anomalie posiadające <color=#f8c200>wiele części<color=#ebcaa2>.\nKażda część może mieć inne odporności, umiejętności oraz pasywki.
380. [Samouczek i wskazówki [tuto_01_11_snow_white_01_04] — tekst] 이 환상체는 <color=#f8c200>열매 부위<color=#ebcaa2>가 약점인 것으로 파악되었습니다.\n열매 부위를 공격해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_01_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: This Abnormality's weak point is its <color=#f8c200>Fruit<color=#ebcaa2> Part.\nTarget the Fruit.
   PL: Ustalono, że słabym punktem tej Anomalii jest <color=#f8c200>część Owocu<color=#ebcaa2>.\nZaatakuj część Owocu.
381. [Samouczek i wskazówki [tuto_01_11_snow_white_02_01] — tekst] 환상체의 부위가 파괴되었어요. 다시 한번 정보를 확인해보죠.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_02_01].content
   limit: do 150 znaków
   EN: You destroyed a Part of the Abnormality. Let us consult the Abnormality Guide to see if anything has been updated.
   PL: Część Anomalii została zniszczona. Sprawdźmy ponownie informacje w Kompendium.
382. [Samouczek i wskazówki [tuto_01_11_snow_white_02_02] — tekst] 열매 부위가 파괴되었네요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_02_02].content
   limit: do 120 znaków
   EN: You destroyed the Fruit Part.
   PL: Część Owocu została zniszczona.
383. [Samouczek i wskazówki [tuto_01_11_snow_white_02_03] — tekst] <color=#f8c200>파괴된 부위<color=#ebcaa2>는 물리 내성이 <color=#f8c200>취약<color=#ebcaa2>으로 변경됩니다. 파괴시 <color=#f8c200>적출<color=#ebcaa2>되는 부위는 재생되기 전까지 공격할 수 없으니 참고해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_02_03].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Physical Resistance values for <color=#f8c200>Destroyed<color=#ebcaa2> Parts become <color=#f8c200>Fatal<color=#ebcaa2>.\nPlease note that Parts marked as <color=#f8c200>Severable<color=#ebcaa2> cannot be attacked again once Destroyed, unless they regenerate.
   PL: Odporności fizyczne <color=#f8c200>zniszczonej części<color=#ebcaa2> zmieniają się na <color=#f8c200>Podatność<color=#ebcaa2>.\nUwaga: części oznaczonych jako <color=#f8c200>Odcinane<color=#ebcaa2> nie można atakować po zniszczeniu, dopóki się nie zregenerują.
384. [Samouczek i wskazówki [tuto_01_11_snow_white_02_04] — tekst] 전투 진행에 따라 적의 패시브 정보가 해금됩니다.\n효율적인 전투를 위해서 파악된 <color=#f8c200>적의 정보를 확인<color=#ebcaa2>하는 습관을 들여주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_02_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: Progressing through the Encounter will unlock the enemy's Passive information.\n<color=#f8c200>Reading the details and clues in the enemy's information window<color=#ebcaa2> is crucial to winning certain battles.
   PL: W miarę postępów walki odblokowują się informacje o pasywkach wroga.\nDla skutecznej walki wyrób sobie nawyk <color=#f8c200>sprawdzania odkrytych informacji o wrogu<color=#ebcaa2>.
385. [Samouczek i wskazówki [tuto_01_11_snow_white_02_05] — tekst] 환상체를 계속 제압해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_02_05].content
   limit: do 120 znaków
   EN: Continue suppressing this Abnormality.
   PL: Kontynuuj tłumienie tej Anomalii.
386. [Samouczek i wskazówki [tuto_01_11_snow_white_03_01] — tekst] 관리자님의 결정을 요구하는 <color=#f8c200><선택지><color=#ebcaa2> 이벤트가 발생하는 경우가 있습니다.\n<color=#f8c200>선택에 따라 상황이 달라질 수 있으니<color=#ebcaa2> 신중히 선택해주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_03_01].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: During Focused Encounters, you, the manager, may occasionally be tasked with making key decisions in <color=#f8c200><Choice Events><color=#ebcaa2>.\n<color=#f8c200>The tide of battle may drastically shift<color=#ebcaa2> depending on your choices, so choose wisely.
   PL: Czasem dochodzi do wydarzenia <color=#f8c200>„Wyboru”<color=#ebcaa2> wymagającego decyzji Kierownika.\n<color=#f8c200>Przebieg bitwy może się diametralnie zmienić<color=#ebcaa2> zależnie od decyzji, więc wybieraj rozważnie.
387. [Samouczek i wskazówki [tuto_01_11_snow_white_03_02_title] — tekst] 선택지
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_03_02_title].content
   limit: do 120 znaków
   EN: Choice Events
   PL: Wydarzenia wyboru
388. [Samouczek i wskazówki [tuto_01_11_snow_white_03_02] — tekst] 선택지마다 요구하는 <color=#f8c200>죄악 속성과 수치<color=#ebcaa2>가 존재합니다.\n선택지에 <color=#f8c200>유리한 속성의 스킬<color=#ebcaa2>을 가진 수감자의 성공률이 높습니다.\n판정의 성공 여부에 따라 결과가 달라집니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_01_11_snow_white_03_02].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: These Choice Events function like Skill checks—they have a required Sin Affinity and a threshold to pass.\nEach Choice Event presents an Affinity advantage—select a Sinner with a matching Skill Affinity to increase your chances of success.\nPassing or failing the check will determine the outcome.
   PL: Każda opcja wyboru wymaga określonego <color=#f8c200>grzechu oraz progu wartości<color=#ebcaa2>.\nGrzesznik posiadający <color=#f8c200>umiejętności premiowanego grzechu<color=#ebcaa2> ma większą szansę powodzenia.\nWynik zależy od tego, czy test zakończy się sukcesem.
389. [Samouczek i wskazówki [tuto_02_12_01_01_start] — tekst] 이번에는 인격의 <color=#f8c200>레벨<color=#ebcaa2>이 전투와 스킬에 어떤 영향을 주는지 알려드리겠습니다. 스킬을 하나 연결해보세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_01_start].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Now, we will explore how an Identity's <color=#f8c200>Level<color=#ebcaa2> affects combat and Skills. Try chaining a Skill.
   PL: Zobaczmy teraz, jak <color=#f8c200>poziom<color=#ebcaa2> Tożsamości wpływa na walkę i umiejętności. Połącz jedną umiejętność.
390. [Samouczek i wskazówki [tuto_02_12_01_01] — tekst] 모든 스킬은 <color=#f8c200>공격 레벨<color=#ebcaa2>과 <color=#f8c200>방어 레벨<color=#ebcaa2>이 존재합니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Every Skill has these two values: <color=#f8c200>Offense Level<color=#ebcaa2> and <color=#f8c200>Defense Level<color=#ebcaa2>.
   PL: Każda umiejętność posiada <color=#f8c200>Poziom Ataku<color=#ebcaa2> oraz <color=#f8c200>Poziom Obrony<color=#ebcaa2>.
391. [Samouczek i wskazówki [tuto_02_12_01_02] — tekst] <color=#f8c200>공격 레벨<color=#ebcaa2>은 <color=#f8c200>공격 스킬<color=#ebcaa2>, <color=#f8c200>반격 스킬<color=#ebcaa2>에 영향을 끼칩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Offense Level<color=#ebcaa2> affects the following Skills: <color=#f8c200>Attack Skills<color=#ebcaa2> and <color=#f8c200>Counter Skills<color=#ebcaa2>.
   PL: <color=#f8c200>Poziom Ataku<color=#ebcaa2> wpływa na <color=#f8c200>umiejętności ataku<color=#ebcaa2> oraz <color=#f8c200>umiejętności Kontry<color=#ebcaa2>.
392. [Samouczek i wskazówki [tuto_02_12_01_03] — tekst] 공격자의 공격 레벨이 피격자의 방어 레벨보다 높을수록 <color=#f8c200>가하는 피해량<color=#ebcaa2>이 추가로 증가하며, 상단에 표시됩니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_03].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: <color=#f8c200>Damage dealt<color=#ebcaa2> increases in proportion to how much the attacker's Offense Level exceeds the target's Defense Level. This increased damage is shown here.
   PL: Im bardziej Poziom Ataku atakującego przewyższa Poziom Obrony celu, tym bardziej rosną <color=#f8c200>zadawane obrażenia<color=#ebcaa2> widoczne u góry.
393. [Samouczek i wskazówki [tuto_02_12_01_04] — tekst] 또한 공격 레벨이 대상과 3 차이 날 때마다 <color=#f8c200>합 위력<color=#ebcaa2>이 1씩 증가하여 합에 유리해집니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_04].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: Also, in a Clash, every 3 points of Offense Level advantage over the target's Offense Level translates to 1 point of Clash Power advantage.
   PL: Ponadto każde 3 punkty przewagi Poziomu Ataku nad celem dają +1 do <color=#f8c200>Mocy Starcia<color=#ebcaa2>, zapewniając przewagę w Starciu.
394. [Samouczek i wskazówki [tuto_02_12_01_05] — tekst] 방어 레벨은 인격이 기본으로 가지고 있으며, <color=#f8c200>받는 피해량<color=#ebcaa2>에 영향을 줍니다.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_05].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: All Identities have their Defense Levels, affecting the <color=#f8c200>amount of damage they take<color=#ebcaa2>.
   PL: Poziom Obrony posiada każda Tożsamość i wpływa on na <color=#f8c200>otrzymywane obrażenia<color=#ebcaa2>.
395. [Samouczek i wskazówki [tuto_02_12_01_06] — tekst] <color=#f8c200>공격 레벨<color=#ebcaa2>, <color=#f8c200>방어 레벨<color=#ebcaa2>은 인격의 <color=#f8c200>레벨에 비례하여 증가<color=#ebcaa2>합니다.\n적과의 레벨 차이에 따라 전투의 난이도가 달라질 수 있으니 전투 시 <color=#f8c200>인격의 레벨<color=#ebcaa2>을 신경써주세요.
   źródło: TutorialRenewalDesc.json :: dataList[id=tuto_02_12_01_06].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>, \n
   EN: <color=#f8c200>Offense Level<color=#ebcaa2> and <color=#f8c200>Defense Level<color=#ebcaa2> are stats that <color=#f8c200>grow in proportion to an Identity’s Level<color=#ebcaa2>.\nThe Level difference between allies and enemies can greatly affect combat difficulty—make sure your <color=#f8c200>Identities are leveled up<color=#ebcaa2> enough if an encounter feels too challenging.
   PL: <color=#f8c200>Poziom Ataku<color=#ebcaa2> i <color=#f8c200>Poziom Obrony<color=#ebcaa2> <color=#f8c200>rosną proporcjonalnie do poziomu<color=#ebcaa2> Tożsamości.\nRóżnica poziomów względem wrogów mocno wpływa na trudność starcia, więc dbaj o <color=#f8c200>poziom swoich Tożsamości<color=#ebcaa2>.

## Samouczek i wskazówki: TutorialRenewalMainUIDesc
- plik gry: `TutorialRenewalMainUIDesc.json`

396. [Samouczek i wskazówki [tuto_10108_01] — tekst] 이번 전투에서는 E.G.O 오버클록에 대해 알아보겠습니다.\n먼저 설명을 위해 료슈 수감자의 E.G.O를 하나 대여하겠습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_01].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We will learn about 'E.G.O Overclocking' in this Encounter.\nFor this purpose, you will be granted temporary access to one of Sinner Ryōshū's E.G.O.
   PL: W tej walce poznamy „Przeciążenie E.G.O”.\nNa potrzeby demonstracji wypożyczymy jedno E.G.O Grzeszniczki Ryōshū.
397. [Samouczek i wskazówki [tuto_10108_02] — tekst] 료슈에게 E.G.O를 장착시켜보겠습니다.\n프로필 상단 부분을 눌러보세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_02].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Let's try equipping Ryōshū with this E.G.O.\nSelect the top part of the portrait card.
   PL: Wyposażmy Ryōshū w to E.G.O.\nKliknij górną część jej karty.
398. [Samouczek i wskazówki [tuto_10108_03] — tekst] E.G.O란을 눌러주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_03].content
   limit: do 120 znaków
   EN: Select the E.G.O tab.
   PL: Kliknij zakładkę E.G.O.
399. [Samouczek i wskazówki [tuto_10108_04] — tekst] E.G.O를 선택해주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_04].content
   limit: do 120 znaków
   EN: Select the E.G.O.
   PL: Wybierz E.G.O.
400. [Samouczek i wskazówki [tuto_10108_05] — tekst] 장착된 E.G.O는 이곳에서 한 눈에 확인할 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_05].content
   limit: do 120 znaków
   EN: View all equipped E.G.O here.
   PL: Tutaj jednym rzutem oka sprawdzisz wyposażone E.G.O.
401. [Samouczek i wskazówki [tuto_10108_06] — tekst] 기본 편성창으로 돌아가주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_06].content
   limit: do 120 znaków
   EN: Let's return to the Team Loadout menu.
   PL: Wróć do podstawowego okna składu.
402. [Samouczek i wskazówki [tuto_10108_07] — tekst] 이곳에서 선택한 수감자가 <color=#f8c200>장착한 E.G.O를 사용하기 위해 필요한 자원<color=#ebcaa2>과 <color=#f8c200>스킬로 생성할 수 있는 자원<color=#ebcaa2>을 확인할 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_07].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#ebcaa2>
   EN: View the <color=#f8c200>E.G.O resource required to use the Deployed Sinners' equipped E.G.O<color=#ebcaa2> & <color=#f8c200>the amount of E.G.O resource your Deployed Sinners' Skills can generate<color=#ebcaa2> here.
   PL: Sprawdzisz tu <color=#f8c200>zasoby potrzebne do użycia wyposażonych E.G.O<color=#ebcaa2> oraz <color=#f8c200>zasoby generowane przez umiejętności wybranych Grzeszników<color=#ebcaa2>.
403. [Samouczek i wskazówki [tuto_10108_08] — tekst] 이제 전투에 참가할 수감자를 편성해주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_08].content
   limit: do 120 znaków
   EN: Now select the Sinners you want to Deploy.
   PL: Wybierz teraz Grzeszników, którzy wezmą udział w walce.
404. [Samouczek i wskazówki [tuto_10108_09] — tekst] 이제 선택한 수감자와 E.G.O를 가지고 전투를 시작해보겠습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_10108_09].content
   limit: do 120 znaków
   EN: Let's begin the Encounter using your choice of Deployed Sinners and E.G.O.
   PL: Rozpocznijmy walkę wybranymi Grzesznikami oraz E.G.O.
405. [Samouczek i wskazówki [tuto_lobby_at_start_01] — tekst] 이후의 이야기를 진행하는 법을 알려드리겠습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_lobby_at_start_01].content
   limit: do 120 znaków
   EN: Let's see how we can continue playing through the story.
   PL: Pokażę teraz, jak kontynuować dalszą część opowieści.
406. [Samouczek i wskazówki [tuto_lobby_at_start_02] — tekst] 입장 버튼을 눌러 다음 이야기를 진행할 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_lobby_at_start_02].content
   limit: do 120 znaków
   EN: Select this button to continue playing through the story.
   PL: Naciśnij przycisk wejścia, aby przejść do kolejnego etapu historii.
407. [Samouczek i wskazówki [tuto_personality_ego_info_01] — tekst] 이번에는 장착한 인격과 E.G.O의 정보를 확인하는 법을 알려드리겠습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_01].content
   limit: do 120 znaków
   EN: Let's learn how to view the detailed information on your equipped Identities & E.G.O.
   PL: Sprawdźmy teraz, jak przeglądać informacje o wyposażonych Tożsamościach i E.G.O.
408. [Samouczek i wskazówki [tuto_personality_ego_info_02] — tekst] 이상 수감자의 초상화를 꾹 눌러주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_02].content
   limit: do 120 znaków
   EN: Press and hold Sinner Yi Sang's portrait.
   PL: Naciśnij i przytrzymaj portret Grzesznika Yi Sanga.
409. [Samouczek i wskazówki [tuto_personality_ego_info_03] — tekst] 이 곳에서는 수감자의 정보를\n확인하고, 성장시킬 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_03].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Here, you can view the selected Sinner's detailed information and upgrade them.
   PL: Tutaj możesz sprawdzić informacje\no Grzeszniku oraz go rozwijać.
410. [Samouczek i wskazówki [tuto_personality_ego_info_04] — tekst] 탭을 눌러 장착한 인격과 E.G.O의\n정보를 확인할 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_04].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the tab here to view the selected Identity & E.G.O's detailed information.
   PL: Kliknij zakładkę, aby przejrzeć dane\nwyposażonej Tożsamości i E.G.O.
411. [Samouczek i wskazówki [tuto_personality_ego_info_05] — tekst] 인격의 레벨업을 진행할 수 있는\n버튼입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_05].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use this button to level up the selected Identity.
   PL: Ten przycisk służy do podnoszenia\npoziomu Tożsamości.
412. [Samouczek i wskazówki [tuto_personality_ego_info_06] — tekst] 인격의 동기화를 진행할 수 있는\n버튼입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_06].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use this button to Uptie the selected Identity.
   PL: Ten przycisk służy do przeprowadzania\nSynchronizacji Tożsamości.
413. [Samouczek i wskazówki [tuto_personality_ego_info_07] — tekst] 레벨과 동기화 단계가 높을수록\n인격이 강해지니 전투 전 레벨과\n동기화 단계를 신경써주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_07].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Identities get stronger with each level up and Uptie tier.\nPlease verify your Identities' Levels and Uptie tiers prior to starting an Encounter.
   PL: Im wyższy poziom i stopień Synchronizacji,\ntym silniejsza staje się Tożsamość —\ndbaj o nie przed walką.
414. [Samouczek i wskazówki [tuto_personality_ego_info_08] — tekst] E.G.O 탭을 눌러 E.G.O의 정보도 확인해보죠.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_08].content
   limit: do 120 znaków
   EN: Now, let's check the detailed info for this E.G.O as well.
   PL: Kliknij zakładkę E.G.O, aby sprawdzić również dane E.G.O.
415. [Samouczek i wskazówki [tuto_personality_ego_info_09] — tekst] 이 곳에서는 E.G.O의 정보를 확인할\n수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_09].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view this E.G.O's detailed information here.
   PL: Tutaj sprawdzisz szczegółowe\ninformacje o E.G.O.
416. [Samouczek i wskazówki [tuto_personality_ego_info_10] — tekst] 탭을 눌러 E.G.O의 정보를 확인할 수\n있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_10].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select the tab here to view the detailed information for E.G.O.
   PL: Kliknij zakładkę, aby wyświetlić\ninformacje o E.G.O.
417. [Samouczek i wskazówki [tuto_personality_ego_info_11] — tekst] E.G.O 스킬을 사용하기 위해 필요한 자원입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_11].content
   limit: do 120 znaków
   EN: These are the resources required to use the E.G.O Skill.
   PL: To zasoby wymagane do użycia umiejętności E.G.O.
418. [Samouczek i wskazówki [tuto_personality_ego_info_12] — tekst] E.G.O 스킬 사용시 소모되는 정신력입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_12].content
   limit: do 120 znaków
   EN: The amount of SP spent when using this E.G.O Skill is displayed here.
   PL: To liczba PP zużywanych przy użyciu umiejętności E.G.O.
419. [Samouczek i wskazówki [tuto_personality_ego_info_13] — tekst] E.G.O 스킬 사용 시 변경되는 수감자의 속성 내성입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_13].content
   limit: do 140 znaków
   EN: When using an E.G.O, the Sinner's Affinity Resistances will be changed as follows(varies for each E.G.O).
   PL: To odporności na grzechy Grzesznika zmieniane po użyciu umiejętności E.G.O.
420. [Samouczek i wskazówki [tuto_personality_ego_info_14] — tekst] E.G.O의 환상 해석을 진행할 수 있는 버튼입니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_14].content
   limit: do 120 znaków
   EN: Use this button to Threadspin(upgrade) the selected E.G.O.
   PL: Ten przycisk służy do przeprowadzania Splotu Nici E.G.O.
421. [Samouczek i wskazówki [tuto_personality_ego_info_15] — tekst] E.G.O는 환상해석을 할 수록 강해지니\n환상해석 단계를 올리는 것을 권장드립니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_15].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upgrade E.G.O Skills by Threadspinning the E.G.O.\nIt is recommended that you Threadspin them.
   PL: Splot Nici wzmacnia E.G.O,\nwięc zalecamy podnoszenie jego stopnia.
422. [Samouczek i wskazówki [tuto_personality_ego_info_16] — tekst] 기본 E.G.O의 경우 스토리 진행에 따라\n환상해석 단계가 상승하니 참고해주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_16].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please note that Base E.G.O Threadspinning Tiers will be raised automatically as you progress through the story.
   PL: W przypadku podstawowych E.G.O stopień Splotu Nici\nrośnie automatycznie wraz z postępami w fabule.
423. [Samouczek i wskazówki [tuto_personality_ego_info_17] — tekst] 자세한 내용은 이쪽의 매뉴얼에도 적혀있으니, 이 곳을 참고해주세요
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_personality_ego_info_17].content
   limit: do 120 znaków
   EN: Please review the manual accessible here for more information.
   PL: Więcej szczegółów znajdziesz również w podręczniku dostępnym w tym miejscu.
424. [Samouczek i wskazówki [tuto_exp_mining_01] — tekst] 단테, 메피스토펠레스의 새로운 기능이 준비되었다고 합니다.\n이쪽에서 확인할 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_01].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Dante, a new function of Mephistopheles has been unlocked.\nPlease direct your attention here.
   PL: Dante, przygotowano nową funkcję Mefistofelesa.\nMożesz sprawdzić ją tutaj.
425. [Samouczek i wskazówki [tuto_exp_mining_02] — tekst] 전투를 통해 경험을 쌓아 강해질 수도 있겠지만 시간이 오래 걸리죠.\n이를 도울 방법으로 채광을 준비했습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_02].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It is possible to grow stronger by gaining experience through battle, but it is not the most optimal method.\nLuxcavations are here to help speed up your Identities' training.
   PL: Można wzmacniać drużynę, zdobywając doświadczenie w walkach, lecz zajmuje to sporo czasu.\nAby to przyspieszyć, przygotowaliśmy Lochy Wydobywcze.
426. [Samouczek i wskazówki [tuto_exp_mining_03] — tekst] 경험치 채광에서 얻을 수 있는 학습 티켓을 사용하면\n인격을 훨씬 빠르게 성장시킬 수 있어요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_03].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Complete Luxcavation battles to earn 'Training Tickets'.\nUsing Training Tickets is a much faster method of leveling your Identities.
   PL: Bilety Treningowe zdobywane w Lochach Wydobywczych PD\npozwalają znacznie szybciej rozwijać poziomy Tożsamości.
427. [Samouczek i wskazówki [tuto_exp_mining_04] — tekst] 향후에 개방될 끈 채광에서는 인격의 동기화, E.G.O의\n환상 해석에 사용될 끈을 얻을 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_04].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Thread Luxcavations, which will be unlocked later, you can earn 'Threads',\nresources used to Uptie Identities and Threadspin E.G.O.
   PL: W odblokowywanych później Lochach Wydobywczych Nici zdobędziesz Nici\nsłużące do Synchronizacji Tożsamości oraz Splotu Nici E.G.O.
428. [Samouczek i wskazówki [tuto_exp_mining_05] — tekst] 채광을 입장하기 위해서는 엔케팔린 모듈이 필요하니 부디 참고해주세요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_05].content
   limit: do 120 znaków
   EN: Please note that Enkephalin Modules are needed to enter Luxcavations.
   PL: Pamiętaj, że wejście do Lochów Wydobywczych wymaga Modułów Enkefaliny.
429. [Samouczek i wskazówki [tuto_exp_mining_06] — tekst] 클리어한 채광 전투는 전투 스킵 기능이 활성화됩니다.\n소모하는 모듈이 2배로 적용되는 단점은 있지만, 시간을 아낄 수 있고 기본 보상의 1.5배만큼을 얻을 수 있어요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_06].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once cleared, Luxcavation battles can be skipped.\nSkipping costs double the Enkephalin Modules, but it saves time and grants 1.5 times the rewards.
   PL: Ukończone walki w Lochach Wydobywczych można pomijać.\nZużywa to wprawdzie 2 razy więcej Modułów, lecz oszczędza czas i daje 1,5 raza więcej nagród podstawowych.
430. [Samouczek i wskazówki [tuto_exp_mining_07] — tekst] 앞으로의 여정을 통해 채광 단계가 차례대로 개방될 거예요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_07].content
   limit: do 120 znaków
   EN: Higher Luxcavation Stages will be unlocked as you continue this journey.
   PL: Kolejne poziomy Lochów Wydobywczych będą odblokowywać się w miarę dalszej podróży.
431. [Samouczek i wskazówki [tuto_exp_mining_08] — tekst] 단계가 높을수록 얻을 수 있는 재화의 가치가 높아지니 주기적으로 확인하시는 걸 추천드려요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_exp_mining_08].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Higher-Level Luxcavation Stages yield better and more efficient resources.\nIt's highly recommended to check this menu from time to time to see if you’ve unlocked a new Stage.
   PL: Wyższe poziomy Lochów Wydobywczych zapewniają cenniejsze zasoby,\nwięc warto regularnie tu zaglądać.
432. [Samouczek i wskazówki [tuto_mirror_dungeon_01] — tekst] 지휘가 많이 능숙해지셨군요, 단테.\n지금이라면 메피스토펠레스의 핵심 기능을 사용할 수 있겠어요.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_mirror_dungeon_01].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It appears you've grown more familiar with your field command, Dante.\nYour abilities should now be sufficient to access a core function of Mephistopheles.
   PL: Nabierasz wprawy w dowodzeniu, Dante.\nTeraz możesz już skorzystać z kluczowej funkcji Mefistofelesa.
433. [Samouczek i wskazówki [tuto_mirror_dungeon_02] — tekst] 이 곳을 눌러 거울 던전으로 입장해보세요.\n거울 던전은 다양한 가능성을 시험하는 곳으로, 클리어 시 배틀 패스 경험치와 일정량의 광기를 얻을 수 있습니다.
   źródło: TutorialRenewalMainUIDesc.json :: dataList[id=tuto_mirror_dungeon_02].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Press this button to enter the Mirror Dungeon.\nIn the Mirror Dungeon, you can experiment and test various possibilities. Completing a run grants Battle Pass EXP and a certain amount of Lunacy.
   PL: Kliknij tutaj, aby wejść do Lustrzanych Lochów.\nTo miejsce badania rozmaitych możliwości, a jego ukończenie zapewnia PD Przepustki Bojowej oraz pewną ilość Szaleństwa.
