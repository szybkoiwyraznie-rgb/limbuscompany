# Paczka AI P11 (Fala 1 · 1D) — Samouczki systemowe i wskazówki ekranu ładowania (część 1/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P11_1d_samouczki_i_wskazowki_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P11_1d_samouczki_i_wskazowki_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Samouczek i wskazówki: BattleHint
- plik gry: `BattleHint.json`

1. [Samouczek i wskazówki [1] — tekst] 거울던전 보상 수령 시에는 엔케팔린 모듈이 필요합니다.
   źródło: BattleHint.json :: dataList[id=1].content
   limit: do 120 znaków
   EN: It costs Enkephalin Modules to claim rewards after completing a Mirror Dungeon expedition.
   PL: Odebranie nagród po ukończeniu Lustrzanego Lochu wymaga zużycia Modułów Enkefaliny.
2. [Samouczek i wskazówki [2] — tekst] 모든 스킬은 1개 이상의 코인을 가지고 있습니다.
   źródło: BattleHint.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Every skill consists of at least 1 Coin.
   PL: Każda umiejętność posiada co najmniej 1 monetę.
3. [Samouczek i wskazówki [3] — tekst] 코인은 앞면과 뒷면에 따라 위력이 감소하거나 증가합니다.
   źródło: BattleHint.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: A Coin’s Power may increase or decrease depending on the face it lands on.
   PL: W zależności od tego, czy wypadnie awers, czy rewers, Moc monety wzrasta lub maleje.
4. [Samouczek i wskazówki [4] — tekst] 코인의 앞면과 뒷면은 스킬 효과의 활성화에도 영향을 줍니다.
   źródło: BattleHint.json :: dataList[id=4].content
   limit: do 120 znaków
   EN: Coin faces also affect the activation of certain skill effects.
   PL: Awers i rewers monety wpływają również na aktywację efektów umiejętności.
5. [Samouczek i wskazówki [5] — tekst] 정신력이 일정 이하로 떨어지면, 패닉 상태에 빠지게 됩니다.
   źródło: BattleHint.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: Units can fall into a state of Panic when their Sanity falls below a certain threshold.
   PL: Gdy Poczytalność spadnie poniżej określonego progu, postać popada w Panikę.
6. [Samouczek i wskazówki [6] — tekst] 정신력이 최저 수치가 된 수감자는 E.G.O에 침식됩니다.
   źródło: BattleHint.json :: dataList[id=6].content
   limit: do 120 znaków
   EN: Sinners with low Sanity will be corroded by E.G.O.
   PL: Grzesznik, którego Poczytalność spadnie do minimum, ulega Korozji E.G.O.
7. [Samouczek i wskazówki [7] — tekst] E.G.O에 침식된 수감자는 아군과 적군을 구별 없이 공격하니 주의하세요.
   źródło: BattleHint.json :: dataList[id=7].content
   limit: do 120 znaków
   EN: Corroded Sinners will lash out indiscriminately, so be careful.
   PL: Uważaj — Grzesznik objęty Korozją E.G.O atakuje na oślep zarówno wrogów, jak i sojuszników.
8. [Samouczek i wskazówki [8] — tekst] 상태 이상의 위력은 상태 이상이 주는 피해량을 표시합니다.
   źródło: BattleHint.json :: dataList[id=8].content
   limit: do 120 znaków
   EN: A status effect’s Potency indicates how much damage it will deal.
   PL: Nasilenie efektu statusu określa wielkość zadawanych przez niego obrażeń.
9. [Samouczek i wskazówki [9] — tekst] 사용한 스킬 아이콘(죄)은 E.G.O 자원으로 모여 E.G.O를 사용하는데 매개체가 됩니다.
   źródło: BattleHint.json :: dataList[id=9].content
   limit: do 120 znaków
   EN: After use, skills are converted into E.G.O resources corresponding to their Sin Affinity.
   PL: Użyte ikony umiejętności (Grzechów) gromadzą się jako zasoby E.G.O potrzebne do wyzwalania E.G.O.
10. [Samouczek i wskazówki [10] — tekst] 같은 환상체를 여러 번 잡으면 관찰 레벨이 올라 환상체에게 주는 피해량이 증가합니다.
   źródło: BattleHint.json :: dataList[id=10].content
   limit: do 160 znaków
   EN: Defeating an Abnormality multiple times raises its Observation Level, allowing you to better damage it in future encounters.
   PL: Wielokrotne pokonanie tej samej Anomalii podnosi jej Poziom Obserwacji, zwiększając zadawane jej obrażenia.
11. [Samouczek i wskazówki [11] — tekst] 자원이 필요한 스킬은 자원이 없을 때 스킬이 취소되니 주의가 필요합니다.
   źródło: BattleHint.json :: dataList[id=11].content
   limit: do 130 znaków
   EN: Skills that require resources will be canceled if the character is missing the required amount.
   PL: Umiejętność wymagająca zasobów zostanie anulowana, jeśli zabraknie wymaganej ich liczby.
12. [Samouczek i wskazówki [12] — tekst] 속도는 매 턴마다 최솟값, 최댓값 사이의 랜덤한 값으로 정해집니다.
   źródło: BattleHint.json :: dataList[id=12].content
   limit: do 120 znaków
   EN: Speed is randomly determined within a given range each turn.
   PL: Co turę Szybkość jest losowana z przedziału od wartości minimalnej do maksymalnej.
13. [Samouczek i wskazówki [13] — tekst] 속도에 따라 아군과 적의 진형 배치가 변경됩니다.
   źródło: BattleHint.json :: dataList[id=13].content
   limit: do 120 znaków
   EN: Speed determines the formation of units in combat.
   PL: Ustawienie sojuszników i wrogów w szyku bojowym zależy od ich Szybkości.
14. [Samouczek i wskazówki [14] — tekst] 전투 시 인격은 착용한 가장 낮은 등급 E.G.O의 속성 내성을 가지고 시작합니다.
   źródło: BattleHint.json :: dataList[id=14].content
   limit: do 150 znaków
   EN: At the start of battle, your characters assume the Sin Resistances of the lowest grade E.G.O they have equipped.
   PL: Na początku walki Tożsamość przyjmuje odporności na Grzechy z najniższej rangi wyposażonego E.G.O.
15. [Samouczek i wskazówki [15] — tekst] E.G.O를 사용하면 E.G.O가 가지고 있는 가장 높은 속성 내성으로 변경 및 유지됩니다.
   źródło: BattleHint.json :: dataList[id=15].content
   limit: do 180 znaków
   EN: After a Sinner uses E.G.O, their Sin Resistances are updated; however, any values that would be lowered will instead remain as they were.
   PL: Po użyciu E.G.O odporności na Grzechy zostają zaktualizowane do najwyższych wartości spośród użytego i bieżącego E.G.O.
16. [Samouczek i wskazówki [16] — tekst] 방어 스킬 사용 시 인격 슬롯의 최하단에 있는 스킬 혹은 E.G.O가 방어 스킬로 변경됩니다.
   źródło: BattleHint.json :: dataList[id=16].content
   limit: do 140 znaków
   EN: A generated Defense skill will fill in the Sinner’s bottom skill slot, replacing the current skill or E.G.O.
   PL: Wygenerowana umiejętność obrony zastępuje umiejętność lub E.G.O na samym dole kolumny Grzesznika.
17. [Samouczek i wskazówki [17] — tekst] E.G.O 사용을 취소하면 사용한 자원은 반환됩니다.
   źródło: BattleHint.json :: dataList[id=17].content
   limit: do 120 znaków
   EN: Cancelling E.G.O before using it will return its resources.
   PL: Anulowanie użycia E.G.O przed rozpoczęciem walki zwraca zużyte zasoby.
18. [Samouczek i wskazówki [18] — tekst] 같은 속성 스킬이 2개 이상 연결되었다면, 죄악 공명이 발동해 강한 피해를 줍니다.
   źródło: BattleHint.json :: dataList[id=18].content
   limit: do 130 znaków
   EN: If 2+ skills of the same Sin are in a chain, Sin Resonance activates, strengthening your attacks.
   PL: Połączenie co najmniej 2 umiejętności tego samego Grzechu wyzwala Rezonans Grzechu, wzmacniając ataki.
19. [Samouczek i wskazówki [19] — tekst] 같은 속성이 연속으로 3개 이상 연결되었다면, 완전 공명이 발동해 더 강한 피해를 줍니다.
   źródło: BattleHint.json :: dataList[id=19].content
   limit: do 150 znaków
   EN: If 3+ skills of the same Sin are in direct succession, Absolute Resonance activates, strengthening your attacks.
   PL: Połączenie pod rząd co najmniej 3 umiejętności tego samego Grzechu wyzwala Pełny Rezonans, jeszcze mocniej wzmacniając ataki.
20. [Samouczek i wskazówki [20] — tekst] 합이 높아질수록 최종적으로 받거나 주는 피해가 증가합니다.
   źródło: BattleHint.json :: dataList[id=20].content
   limit: do 120 znaków
   EN: The longer a Clash goes on, the higher the victor’s final damage will be.
   PL: Im więcej wymian w Starciu, tym większe obrażenia końcowe zada zwycięzca.
21. [Samouczek i wskazówki [21] — tekst] 흐트러짐 구간까지 체력이 소모되면, 공격 유형 내성이 취약으로 변경되고 다음 턴까지 행동하지 않습니다.
   źródło: BattleHint.json :: dataList[id=21].content
   limit: do 200 znaków
   EN: When a character’s health falls below the Stagger Threshold, they become vulnerable to all attacks and can’t act until the end of the following turn.
   PL: Gdy PŻ spadną poniżej progu Oszołomienia, odporności fizyczne stają się Podatne, a postać traci możliwość działania do końca kolejnej tury.
22. [Samouczek i wskazówki [22] — tekst] 던전 진행 시 세이브 룸에서 피해를 회복하고 던전 탐사 진행을 저장할 수 있습니다.
   źródło: BattleHint.json :: dataList[id=22].content
   limit: do 120 znaków
   EN: In Dungeons, you can heal up and save your progress at Checkpoints.
   PL: W trakcie eksploracji lochu w punktach zapisu możesz uleczyć drużynę i zapisać postęp wyprawy.
23. [Samouczek i wskazówki [23] — tekst] 모든 인격은 전투 패시브와 서포트 패시브를 가지고 있습니다.
   źródło: BattleHint.json :: dataList[id=23].content
   limit: do 120 znaków
   EN: Every Identity has a Combat Passive and a Support Passive.
   PL: Każda Tożsamość posiada pasywkę bojową oraz pasywkę wsparcia.
24. [Samouczek i wskazówki [24] — tekst] 전투에 참여한 인격은 전투 패시브를 사용합니다.
   źródło: BattleHint.json :: dataList[id=24].content
   limit: do 120 znaków
   EN: Identities participating in combat use Combat Passives.
   PL: Tożsamości biorące bezpośredni udział w walce korzystają ze swoich pasywek bojowych.
25. [Samouczek i wskazówki [25] — tekst] 전투에 참여하지 않은 인격의 패시브는 서포트 패시브로 적용됩니다.
   źródło: BattleHint.json :: dataList[id=25].content
   limit: do 130 znaków
   EN: Sinners who are not directly participating in battle will provide aid with their Support Passives.
   PL: Pasywki Tożsamości niewystawionych do walki działają jako pasywki wsparcia.
26. [Samouczek i wskazówki [26] — tekst] 환상체는 부위마다 내성과 사용하는 스킬이 다릅니다.
   źródło: BattleHint.json :: dataList[id=26].content
   limit: do 120 znaków
   EN: An Abnormality’s Parts may have differing Resistances and behavior.
   PL: Poszczególne części Anomalii różnią się odpornościami oraz używanymi umiejętnościami.
27. [Samouczek i wskazówki [27] — tekst] 집중 전투 중에는 선택지가 발생하고 결과에 따라 다양한 효과나 E.G.O 기프트를 얻을 수 있습니다.
   źródło: BattleHint.json :: dataList[id=27].content
   limit: do 260 znaków
   EN: When confronting Abnormalities in Focused Encounters, you may come across situations requiring you to make a choice; depending on the outcome, you might receive various effects or even E.G.O Gifts.
   PL: Podczas starć skupionych mogą pojawić się wydarzenia wymagające wyboru — w zależności od wyniku można uzyskać rozmaite efekty lub Dary E.G.O.
28. [Samouczek i wskazówki [28] — tekst] 선택지가 요구하는 죄를 가지고 있지 않더라도 성공할 수 있습니다.
   źródło: BattleHint.json :: dataList[id=28].content
   limit: do 120 znaków
   EN: It’s still possible to pass a check even without the requisite Sin.
   PL: Test w wydarzeniu może zakończyć się powodzeniem nawet bez wymaganego Grzechu.
29. [Samouczek i wskazówki [29] — tekst] 던전을 진행하면서 선택지와 전투로 E.G.O 기프트를 얻을 수 있습니다.
   źródło: BattleHint.json :: dataList[id=29].content
   limit: do 120 znaków
   EN: You can obtain E.G.O Gifts from both checks and battles as you progress through a Dungeon.
   PL: Podczas eksploracji lochu Dary E.G.O można zdobywać zarówno z wydarzeń, jak i z walk.
30. [Samouczek i wskazówki [30] — tekst] 적은 정신력이 소모되어 패닉 상태가 되면, 부정적인 효과를 가지게 됩니다.
   źródło: BattleHint.json :: dataList[id=30].content
   limit: do 120 znaków
   EN: When an enemy runs out of Sanity and falls into Panic, they suffer negative effects.
   PL: Gdy wróg wyczerpie Poczytalność i popadnie w Panikę, otrzymuje negatywne efekty.
31. [Samouczek i wskazówki [31] — tekst] 흐트러짐 상태에서 다음 흐트러짐 구간까지 피해를 준다면 추가 피해를 줍니다.
   źródło: BattleHint.json :: dataList[id=31].content
   limit: do 130 znaków
   EN: If a Staggered character’s HP falls below the next Stagger Threshold, they’ll take extra damage.
   PL: Jeśli PŻ Oszołomionej postaci spadną poniżej kolejnego progu Oszołomienia, otrzyma ona dodatkowe obrażenia.
32. [Samouczek i wskazówki [32] — tekst] 상태 이상의 횟수는 상태 이상이 유지되는 턴 수를 표시합니다.
   źródło: BattleHint.json :: dataList[id=32].content
   limit: do 140 znaków
   EN: A status effect’s Count indicates how long it will last or how many times it will activate during combat.
   PL: Licznik efektu statusu wskazuje liczbę tur jego trwania lub liczbę pozostałych aktywacji.
33. [Samouczek i wskazówki [33] — tekst] E.G.O 스킬은 조작 패널의 최하단에서부터 생성됩니다.
   źródło: BattleHint.json :: dataList[id=33].content
   limit: do 120 znaków
   EN: E.G.O skills are placed at the bottom of a Sinner’s column.
   PL: Umiejętności E.G.O są generowane od samego dołu kolumny Grzesznika na panelu dowodzenia.
34. [Samouczek i wskazówki [34] — tekst] 서로 공격 스킬로 공격할 때 합이 발생합니다.
   źródło: BattleHint.json :: dataList[id=34].content
   limit: do 120 znaków
   EN: Clashes occur when two Attack Skills target each other.
   PL: Gdy dwie postacie zaatakują się nawzajem umiejętnościami ataku, dochodzi do Starcia.
35. [Samouczek i wskazówki [35] — tekst] 전투 패시브와 서포트 패시브는 활성화되기 위해서는 특정 죄를 연결하거나 소유해야 합니다.
   źródło: BattleHint.json :: dataList[id=35].content
   limit: do 160 znaków
   EN: Combat Passives and Support Passives require certain Sin Affinities to be chained or their resources owned to activate.
   PL: Aktywacja pasywek bojowych i pasywek wsparcia wymaga połączenia lub posiadania zasobów określonych Grzechów.

## Samouczek i wskazówki: BattleHint_AbnorBattle
- plik gry: `BattleHint_AbnorBattle.json`

36. [Samouczek i wskazówki [1] — tekst] 집중 전투는 진행하면서 내성을 알아내고 약한 속성으로 공격해 부위파괴를 노려봅시다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=1].content
   limit: do 170 znaków
   EN: In Focused Encounters, prioritize discovering its weaknesses and destroying its parts by attacking with effective Affinities.
   PL: W starciach skupionych odkrywaj odporności Anomalii i uderzaj w jej słabe punkty, aby niszczyć poszczególne części ciała.
37. [Samouczek i wskazówki [2] — tekst] 선택지가 요구하는 죄를 가진 인격이 있다면 더 쉽게 해결할 수 있습니다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Identities with certain Sins will have better odds at passing checks.
   PL: Tożsamości dysponujące Grzechem wymaganym przez wydarzenie mają większą szansę powodzenia.
38. [Samouczek i wskazówki [3] — tekst] 환상체의 스킬은 부위파괴 시 취소할 수 있기 때문에 강력한 스킬을 막고 싶다면 부위파괴를 노려봅시다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=3].content
   limit: do 160 znaków
   EN: Some Abnormality skills can be canceled by breaking their parts. Breaking one at the right time can stop a powerful skill.
   PL: Zniszczenie części ciała Anomalii anuluje przypisane do niej umiejętności — wykorzystaj to, by powstrzymać jej najgroźniejsze ataki.
39. [Samouczek i wskazówki [4] — tekst] 착용한 E.G.O를 확인해 필요한 자원을 얻을 수 있는 인격으로 구성하여 전투를 진행해 봅시다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=4].content
   limit: do 150 znaków
   EN: Take into account what E.G.O you bring into your team so that you can gather the necessary resources more easily.
   PL: Sprawdź wymagane zasoby wyposażonych E.G.O i dobierz Tożsamości, które sprawnie zgromadzą je w walce.
40. [Samouczek i wskazówki [5] — tekst] E.G.O는 정신력이 높은 상태에서 사용 시 전투의 승기를 가져오기 쉬워집니다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: E.G.O can shift the battle in your favor if used when your Sinner has high enough sanity.
   PL: Użycie E.G.O przy wysokiej Poczytalności pozwala łatwo przechylić szalę zwycięstwa na swoją stronę.
41. [Samouczek i wskazówki [6] — tekst] 흐트러짐 상태에서 다음 흐트러짐 구간까지 피해를 준다면, 더 강한 추가 피해를 줄 수 있습니다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=6].content
   limit: do 130 znaków
   EN: If a Staggered character’s health falls below the next Stagger Threshold, they’ll take extra damage.
   PL: Przebicie kolejnego progu Oszołomienia na już Oszołomionym celu zadaje jeszcze dotkliwsze obrażenia dodatkowe.
42. [Samouczek i wskazówki [7] — tekst] 스토리 던전이 어렵다면 인격을 성장시켜 진행합시다. 스토리 던전에서는 인격의 성장이 큰 도움이 됩니다.
   źródło: BattleHint_AbnorBattle.json :: dataList[id=7].content
   limit: do 140 znaków
   EN: If you’re struggling to conquer a Story Dungeon, make sure to power up your Identities as best you can.
   PL: Jeśli Loch Fabularny sprawia trudności, rozwiń swoje Tożsamości — ich poziom ma w nim kluczowe znaczenie.

## Samouczek i wskazówki: BattleHint_NormalBattle
- plik gry: `BattleHint_NormalBattle.json`

43. [Samouczek i wskazówki [1] — tekst] 착용한 E.G.O를 확인해 필요한 자원을 얻을 수 있는 인격으로 구성하여 전투를 진행해 봅시다.
   źródło: BattleHint_NormalBattle.json :: dataList[id=1].content
   limit: do 190 znaków
   EN: Check the E.G.O your Sinners have equipped and their required resources to form a team of Identities that can efficiently gather them in battle.
   PL: Sprawdź wyposażone E.G.O i dobierz do składu Tożsamości pozwalające sprawnie gromadzić potrzebne im zasoby w walce.
44. [Samouczek i wskazówki [2] — tekst] E.G.O는 정신력이 높은 상태에서 사용 시 전투의 승기를 가져오기 쉬워집니다.
   źródło: BattleHint_NormalBattle.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: E.G.O can shift the battle in your favor if used when your Sinners have enough Sanity.
   PL: Użycie E.G.O przy wysokiej Poczytalności ułatwia przejęcie inicjatywy w walce.
45. [Samouczek i wskazówki [3] — tekst] 정신력이 소모된 적이 패닉 상태가 된다면 부정적인 효과를 가지게 되어 전투의 승기를 가질 수 있습니다.
   źródło: BattleHint_NormalBattle.json :: dataList[id=3].content
   limit: do 150 znaków
   EN: When an enemy runs out of Sanity and falls into Panic, they’ll suffer negative effects, giving you an advantage.
   PL: Doprowadzenie wroga do utraty Poczytalności i Paniki nakłada na niego kary, które otwierają drogę do zwycięstwa.
46. [Samouczek i wskazówki [4] — tekst] 흐트러짐 상태에서 다음 흐트러짐 구간까지 피해를 준다면, 더 강한 추가 피해를 줄 수 있습니다.
   źródło: BattleHint_NormalBattle.json :: dataList[id=4].content
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Samouczek i wskazówki: TutorialDesc
- plik gry: `TutorialDesc.json`

47. [Samouczek i wskazówki [tutorial_101_01] — tekst] 전투를 진행하기 위한 기본적인 명령 방법을 알려드리겠습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_101_01].content
   limit: do 120 znaków
   EN: Allow me to show you the basics of management and command.
   PL: Przedstawię podstawy wydawania rozkazów niezbędne do prowadzenia walki.
48. [Samouczek i wskazówki [tutorial_101_02] — tekst] 조작 패널을 통해 스킬을 연결하여 수감자들에게 명령을 내릴 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_101_02].content
   limit: do 150 znaków
   EN: You can give orders to the Sinners by connecting (chaining) skills on the Dashboard at the bottom of the screen.
   PL: Łącząc umiejętności na panelu dowodzenia u dołu ekranu, wydajesz rozkazy Grzesznikom.
49. [Samouczek i wskazówki [tutorial_101_03] — tekst] 왼쪽 기어를 눌러보세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_101_03].content
   limit: do 120 znaków
   EN: Press and hold this gear on the left.
   PL: Naciśnij lewe koło zębate.
50. [Samouczek i wskazówki [tutorial_101_04] — tekst] 왼쪽 기어부터 오른쪽 기어까지 스킬 아이콘을 연결해 보세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_101_04].content
   limit: do 120 znaków
   EN: From here, form a chain of skills all the way to the gear on the right.
   PL: Przeciągnij łańcuch przez ikony umiejętności od lewego koła zębatego aż do prawego.
51. [Samouczek i wskazówki [tutorial_101_05] — tekst] 스킬 아이콘을 모두 연결한 뒤, 오른쪽 기어를 눌러 전투를 시작해보죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_101_05].content
   limit: do 120 znaków
   EN: After you have formed a chain of skills, press the right gear to begin combat.
   PL: Po połączeniu wszystkich ikon umiejętności naciśnij prawe koło zębate, aby rozpocząć walkę.
52. [Samouczek i wskazówki [tutorial_102_01] — tekst] 강한 공격이 필요하겠어요. 강한 공격을 하도록 연결해보죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_102_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It appears we need a powerful attack.\nLet’s form the proper chain for it.
   PL: Przyda się silniejsze uderzenie. Połączmy umiejętności tak, by wzmocnić atak.
53. [Samouczek i wskazówki [tutorial_102_02] — tekst] 이번 턴에 2개 이상 같은 속성을 연결하면 <공명>이 발생합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_102_02].content
   limit: do 120 znaków
   EN: By chaining 2 or more skills of the same Affinity this turn, you will cause <Resonance>.
   PL: Połączenie w tej turze co najmniej 2 umiejętności tego samego Grzechu wywoła „Rezonans”.
54. [Samouczek i wskazówki [tutorial_102_03_popup_title] — tekst] 공명 입력
   źródło: TutorialDesc.json :: dataList[id=tutorial_102_03_popup_title].content
   limit: do 120 znaków
   EN: Resonance Input
   PL: Wprowadzanie Rezonansu
55. [Samouczek i wskazówki [tutorial_102_03] — tekst] 공명은 연결된 “같은 속성 스킬 수”에 따라 피해량이 증가합니다.\n같은 속성 스킬 중 나중에 입력된 스킬일수록 스킬 위력이 증가합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_102_03].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Resonance boosts the damage of skills with the same\nSin Affinity. (Their color, in other words.)\nThe Power of each skill is boosted by the number of skills that come before it.
   PL: Rezonans zwiększa obrażenia proporcjonalnie do liczby połączonych umiejętności tego samego Grzechu.\nIm dalej w łańcuchu znajduje się dana umiejętność, tym większą premię do Mocy otrzymuje.
56. [Samouczek i wskazówki [tutorial_103_01] — tekst] 부족하네요. 더 강한 공격이 필요하겠어요.\n스킬을 연결해보세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_103_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That wasn’t enough. We must strike them even harder.\nTry chaining our skills again.
   PL: To wciąż za mało — potrzebujemy jeszcze silniejszego natarcia.\nSpróbuj ponownie połączyć umiejętności.
57. [Samouczek i wskazówki [tutorial_103_02] — tekst] 같은 속성을 “3개 이상 연속으로” 연결하면 <완전 공명>이 발생합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_103_02].content
   limit: do 140 znaków
   EN: By chaining 3 or more skills of the same Affinity in direct succession, you will cause <Absolute Resonance>.
   PL: Połączenie „co najmniej 3 pod rząd” umiejętności tego samego Grzechu wywołuje „Pełny Rezonans”.
58. [Samouczek i wskazówki [tutorial_103_03_popup_title] — tekst] 완전 공명 입력
   źródło: TutorialDesc.json :: dataList[id=tutorial_103_03_popup_title].content
   limit: do 120 znaków
   EN: What is Absolute Resonance?
   PL: Pełny Rezonans
59. [Samouczek i wskazówki [tutorial_103_03] — tekst] 같은 속성의 죄악이 3개 이상 연속 연결되면 <완전 공명>이 됩니다.\n<완전 공명>은 연속된 같은 속성 스킬에 동일하게 가장 높은 스킬 위력 증가가 적용됩니다.\n스킬 위력은 완전 공명된 수에 따라 높아집니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_103_03].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As we just covered, chaining 3 or more skills of the same Affinity in succession causes <Absolute Resonance>.\nEvery skill under <Absolute Resonance> receives a Power boost based on their total number.\nLikewise, this boost especially shines with more resonating skills.
   PL: Połączenie pod rząd co najmniej 3 umiejętności tego samego Grzechu aktywuje „Pełny Rezonans”.\nW ramach „Pełnego Rezonansu” wszystkie połączone umiejętności tego Grzechu otrzymują jednakowo najwyższą premię do Mocy.\nPremia rośnie wraz z liczbą umiejętności objętych Pełnym Rezonansem.
60. [Samouczek i wskazówki [tutorial_104_01] — tekst] 모든 캐릭터의 체력에는 노란색으로 표시된 흐트러짐 구간이 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_104_01].content
   limit: do 120 znaków
   EN: You will find yellow Stagger Thresholds on the health bars of both your Sinners and enemies.
   PL: Na pasku PŻ każdej postaci widnieją żółte linie oznaczające progi Oszołomienia.
61. [Samouczek i wskazówki [tutorial_104_02_popup_title] — tekst] 흐트러짐 설명
   źródło: TutorialDesc.json :: dataList[id=tutorial_104_02_popup_title].content
   limit: do 120 znaków
   EN: What is Stagger?
   PL: Oszołomienie
62. [Samouczek i wskazówki [tutorial_104_02] — tekst] 체력이 흐트러짐 구간까지 감소하면 <흐트러짐 상태>가 됩니다.\n<흐트러짐 상태>는 모든 물리 내성을 취약으로 만듭니다.\n한 턴 동안 흐트러짐 구간을 추가로 넘어갈 때마다 <흐트러짐 상태> 단계가 증가합니다.\n<흐트러짐 단계>는 3단계가 있으며, 단계가 올라갈수록 추가로 받는 피해가 높아집니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_104_02].content
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When an attack puts a unit’s HP below one of the yellow-lined thresholds, they will become <Staggered>.\nWhile <Staggered>, all physical resistances change to Fatal.\nIf a unit’s HP drops past multiple Stagger Thresholds in a single turn, their <Stagger Level> will increase.\nThis <Stagger Level> can go up to 3, and as it increases, the damage the unit takes is amplified.
   PL: Gdy PŻ spadną poniżej progu Oszołomienia, postać przechodzi w stan „Oszołomienia”.\n„Oszołomienie” zmienia wszystkie odporności fizyczne na Podatne.\nKażdy kolejny próg Oszołomienia przekroczony w tej samej turze podnosi stopień „Oszołomienia”.\nIstnieją 3 stopnie „Oszołomienia” — im wyższy stopień, tym większe obrażenia przyjmuje cel.
63. [Samouczek i wskazówki [tutorial_104_03] — tekst] 좋아요. 적이 <흐트러짐 상태>가 되었어요. 지금까지 알려드렸던 방법으로 명령을 내려 전투를 진행해주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_104_03].content
   limit: do 130 znaków
   EN: Well done. We’ve <Staggered> an enemy. Now, keep up the fight with what I’ve taught you so far.
   PL: Doskonale. Wróg został „Oszołomiony”. Kontynuuj walkę, wydając rozkazy zgodnie z dotychczasowymi wskazówkami.
64. [Samouczek i wskazówki [tutorial_201_01] — tekst] 모든 캐릭터 행동에는 <속도>가 정해져있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_01].content
   limit: do 120 znaków
   EN: All actions are dictated by a <Speed> value.
   PL: Każde działanie postaci podlega wartości „Szybkości”.
65. [Samouczek i wskazówki [tutorial_201_02_popup_title] — tekst] 속도 설명
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_02_popup_title].content
   limit: do 120 znaków
   EN: What is Speed?
   PL: Szybkość
66. [Samouczek i wskazówki [tutorial_201_02] — tekst] 모든 캐릭터 속도는 매 턴마다 최소 속도 ~ 최대 속도 사이에서 결정됩니다.\n매 턴마다 속도에 따라 캐릭터의 위치가 정해집니다.\n속도가 낮은 캐릭터일 수록 상대와 가까이 배치되어 표적이 되기 쉬워집니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_02].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Speed is a random number chosen from within a given range each turn.\nThe positions of units are rearranged every turn according to their Speeds.\nThose with lower Speeds are placed at the front, making them easier targets.
   PL: Co turę Szybkość każdej postaci jest losowana z przedziału od jej wartości minimalnej do maksymalnej.\nNa podstawie wylosowanej Szybkości ustalane jest ustawienie na polu bitwy.\nWolniejsze postacie stają bliżej przeciwnika, przez co łatwiej stają się celem ataków.
67. [Samouczek i wskazówki [tutorial_201_05] — tekst] 스킬로 공격하기 전 캐릭터는 코인을 굴려 최종 위력을 결정합니다. 최종 위력이 높을수록 스킬 대미지가 증가합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_05].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Before using a skill, characters will flip Coins to determine its final Power value.\nHigher Power means higher damage.
   PL: Przed wyprowadzeniem ataku postać rzuca monetami, aby ustalić końcową Moc umiejętności. Im wyższa Moc końcowa, tym większe obrażenia.
68. [Samouczek i wskazówki [tutorial_201_06] — tekst] 코인 수는 스킬의 공격 횟수를 의미합니다. 코인이 2개라는 것은 2번 공격한다는 것이죠
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_06].content
   limit: do 120 znaków
   EN: The number of Coins indicates how many attacks are made. Two Coins means two hits.
   PL: Liczba monet oznacza liczbę uderzeń umiejętności. Dwie monety to dwa ciosy.
69. [Samouczek i wskazówki [tutorial_201_07] — tekst] 스킬로 공격하기 전 캐릭터는 코인을 굴려 최종 위력을 결정합니다. 최종 위력이 높을수록 스킬 대미지가 증가합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_07].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Samouczek i wskazówki [tutorial_201_08] — tekst] 코인에서 앞면이 나오면 스킬 위력에 코인 위력이 더해집니다. 최종 위력이 변하게되죠. 이번에는 증가하겠네요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_08].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Usually, if a Coin lands on heads, its Power will be added to the skill’s Power.\nLooks like the skill will be strengthened this time.
   PL: Gdy wypadnie awers, Moc monety zostaje doliczona do Mocy umiejętności, zmieniając Moc końcową. Tym razem wartość wzrośnie.
71. [Samouczek i wskazówki [tutorial_201_09] — tekst] 이렇게 증가한 위력은 다음 코인을 던질 때에도 유지됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_201_09].content
   limit: do 120 znaków
   EN: The added Power persists over to the next coin toss.
   PL: Zwiększona w ten sposób Moc utrzymuje się również przy rzucie kolejną monetą.
72. [Samouczek i wskazówki [tutorial_202_01] — tekst] 턴이 시작될 때마다 <흐트러짐>, <패닉>, <E.G.O 침식> 상태에 관계 없이 전투 편성 순서에 따라 스킬 슬롯이 추가됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_01].content
   limit: do 250 znaków
   EN: At the start of each turn, a skill slot will be added for a Sinner in the order they were deployed during team setup, regardless of if the Sinner is <Staggered>, <in Panic>, or <E.G.O corrosion>.
   PL: Na początku każdej tury — niezależnie od „Oszołomienia”, „Paniki” czy „Korozji E.G.O” — dodawane są kolejne pola umiejętności zgodnie z kolejnością wystawienia w składzie.
73. [Samouczek i wskazówki [tutorial_202_02] — tekst] 수감자와 대치하는 적이 서로 공격 스킬을 사용하면 <합>이 발생합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_02].content
   limit: do 120 znaków
   EN: When a Sinner and their target both use attack skills, a <Clash> occurs.
   PL: Gdy Grzesznik i stojący naprzeciw wróg użyją przeciw sobie umiejętności ataku, dochodzi do „Starcia”.
74. [Samouczek i wskazówki [tutorial_202_03_popup_title] — tekst] 합 설명
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_03_popup_title].content
   limit: do 120 znaków
   EN: What are Clashes?
   PL: Starcie
75. [Samouczek i wskazówki [tutorial_202_03] — tekst] <합>은 수감자와 적이 서로 공격 스킬을 사용할 때 발생합니다.\n<합>은 두 스킬 중 합 위력이 큰 쪽이 승리하며,  패배한 쪽의 스킬 코인 한 개가 파괴됩니다.\n스킬 코인이 남아있다면, 모두 파괴되기 전까지 코인을 새로 굴리며 <합>을 진행합니다.\n<합>진행 중 스킬 코인이 모두 파괴되면, 해당 캐릭터 스킬이 취소되고 합에서 패배합니다.\n<합>에서 이긴 해당 캐릭터는 합 수에 따라 더 강한 피해를 줄 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_03].content
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A <Clash> occurs when two characters attack each other.\nThe side with the higher Power wins, removing 1 Coin from the loser.\nIf both sides still have Coins, more Clashes will occur until one side has lost all of its Coins.\nThe side that loses all their Coins will have their attack skill canceled.\nThe winner will then attack with their remaining Coins, gaining a damage bonus based on the total number of Clashes.
   PL: „Starcie” następuje, gdy Grzesznik i wróg zaatakują się nawzajem umiejętnościami ataku.\nWygrywa strona o wyższej Mocy Starcia, niszcząc jedną monetę umiejętności przegranego.\nDopóki po obu stronach pozostają monety, rzuty są ponawiane w kolejnych wymianach „Starcia”.\nGdy wszystkie monety jednej ze stron ulegną zniszczeniu, jej umiejętność zostaje anulowana, a Starcie kończy się jej porażką.\nZwycięzca „Starcia” wyprowadza atak pozostałymi monetami, zadając obrażenia zwiększone o premię za liczbę wymian.
76. [Samouczek i wskazówki [tutorial_202_04] — tekst] <합>은 두 스킬의 합 위력을 비교하여, 합 위력이 큰 쪽이 승리하는 이벤트입니다.\n상단의 게이지와 텍스트를 참고하여 합의 예상 승률을 알 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In a <Clash>, the Clash Power of two opposing skills is compared, and the side with greater Power wins.\nThe gauge and text shown at the top of the screen predict your odds of winning.
   PL: W „Starciu” porównywana jest Moc Starcia obu umiejętności, a zwycięża strona z wyższym wynikiem.\nPasek oraz komunikat u góry ekranu wskazują przewidywane szanse zwycięstwa.
77. [Samouczek i wskazówki [tutorial_202_05] — tekst] 합을 시작하면 두 캐릭터가 코인을 굴려 합 위력을 정합니다. 둘 중 합 위력이 높은 캐릭터가 합에서 승리하여, 공격과 함께 적의 코인을 한 개 파괴합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_05].content
   limit: do 230 znaków
   EN: When a Clash begins, the two characters will each toss a Coin to determine their skills’ power in the Clash. Then, the side with more Power wins and destroys the opponent’s Coin.
   PL: Na początku Starcia obie postacie rzucają monetami, ustalając swoją Moc Starcia. Postać z wyższą Mocą wygrywa wymianę i niszczy jedną monetę przeciwnika.
78. [Samouczek i wskazówki [tutorial_202_06] — tekst] 이후 1명의 코인이 모두 사라질 때까지 합을 지속합니다.\n1명의 코인이 모두 파괴되면, 해당 캐릭터의 스킬이 취소되고, 합에서 완전히 패배합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_202_06].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Clash will continue until one side has run out of Coins.\nWhen a character’s final Coin is destroyed, their skill is canceled, and the Clash will end in complete defeat.
   PL: Wymiany trwają aż do utraty wszystkich monet przez jedną ze stron.\nGdy ostatnia moneta postaci ulegnie zniszczeniu, jej umiejętność zostaje anulowana, a Starcie kończy się całkowitą porażką.
79. [Samouczek i wskazówki [tutorial_203_01] — tekst] 체력 옆에 있는 구체는 캐릭터 <정신력>을 나타냅니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_01].content
   limit: do 120 znaków
   EN: The blue orb next to a character’s health bar is an indicator of their <Sanity>, or SP.
   PL: Kula obok paska PŻ wskazuje „Poczytalność” (SP) postaci.
80. [Samouczek i wskazówki [tutorial_203_02_popup_title] — tekst] 정신력 설명
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_02_popup_title].content
   limit: do 120 znaków
   EN: What is Sanity?
   PL: Poczytalność
81. [Samouczek i wskazówki [tutorial_203_02] — tekst] 체력 옆에 있는 구체는 <정신력>을 나타내며, -45부터 +45까지\n정신력이 높을수록 스킬에서 사용하는 코인의 앞면 확률이 증가합니다.\n적을 처치하거나 아군이 사망할 때 정신력이 증가하거나 감소합니다.\n정신력이 일정 수치 이하로 낮아진 적은 “사기 저하” 또는 “패닉”상태가 됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_02].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The sphere on a unit’s right indicates their <Sanity>, or SP. It has a range of -45 to +45.\nUnits with higher Sanity have a higher chance of their Coin flips landing heads.\nDefeating enemies boosts Sanity, while ally deaths will harm Sanity.\nEnemy units at low Sanity may fall into states of “Low Morale” or “Panic”.
   PL: Kula obok paska PŻ oznacza „Poczytalność” (od -45 do +45).\nIm wyższa Poczytalność, tym większa szansa na wyrzucenie awersu monet umiejętności.\nPokonywanie wrogów podnosi Poczytalność, natomiast śmierć sojuszników ją obniża.\nWrogowie, których Poczytalność spadnie poniżej określonego progu, popadają w „Niskie Morale” lub „Panikę”.
82. [Samouczek i wskazówki [tutorial_203_06] — tekst] 이 영역을 통해 현재 캐릭터에게 적용 중인 효과를 확인할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_06].content
   limit: do 120 znaków
   EN: You can view the effects and ailments on a unit in the indicated area.
   PL: W tym miejscu możesz sprawdzić efekty działające aktualnie na postać.
83. [Samouczek i wskazówki [tutorial_203_07] — tekst] 영역 내의 아이콘을 누르면 해당 효과의 세부 정보를 확인할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_07].content
   limit: do 120 znaków
   EN: Press or hover over one of the effect icons to examine it in detail.
   PL: Dotknięcie ikony w tym obszarze wyświetli szczegółowy opis danego efektu.
84. [Samouczek i wskazówki [tutorial_203_08] — tekst] 모든 적들이 패닉 상태가 되었군요. 지금이 기회에요. 자유롭게 명령을 내려보세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_203_08].content
   limit: do 120 znaków
   EN: All of our foes have fallen into panic. Now’s our chance. Give us orders at your discretion.
   PL: Wszyscy wrogowie wpadli w Panikę. To nasza szansa — wydaj rozkazy według własnego uznania.
85. [Samouczek i wskazówki [tutorial_301_01] — tekst] 스킬을 연결해주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_301_01].content
   limit: do 120 znaków
   EN: Please form a chain of skills. I have more to teach you.
   PL: Połącz umiejętności.
86. [Samouczek i wskazówki [tutorial_301_02_popup_tItle] — tekst] 공격 유형과 속성
   źródło: TutorialDesc.json :: dataList[id=tutorial_301_02_popup_tItle].content
   limit: do 120 znaków
   EN: Attack Types and Affinities
   PL: Typy ataku i Grzechy
87. [Samouczek i wskazówki [tutorial_301_02] — tekst] 스킬에는 공격 유형으로 <참격>, <관통>, <타격>과\n죄악 속성으로 <분노>, <색욕>, <나태>, <탐식>, <우울>, <오만>, <질투>이 있습니다.\n대상의 공격 유형과 죄악 속성 내성에 따라 대미지가 결정되죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_301_02].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Skills have two major properties:\nTheir <Attack Type> and <Sin Affinity>.\nThe Attack Types are Slash, Pierce, and Blunt.\nThe Sin Affinities are Wrath, Lust, Sloth, Gluttony, Gloom, Pride, and Envy.\nCombined with Resistances, Attack Types and Affinities determine the damage of skills.
   PL: Umiejętności dzielą się pod względem typu ataku na „Cięcie”, „Kłucie” i „Obuch”\noraz pod względem Grzechu na „Gniew”, „Żądzę”, „Lenistwo”, „Obżarstwo”, „Posępność”, „Pychę” i „Zawiść”.\nOstateczne obrażenia zależą od odporności celu na dany typ ataku oraz Grzech.
88. [Samouczek i wskazówki [tutorial_301_03] — tekst] 이 곳에서 아군이 사용할 스킬의 공격 유형과 죄악 속성을 확인할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_301_03].content
   limit: do 120 znaków
   EN: Here, you can check the Attack Type and Sin Affinity of your Sinners' Skills.
   PL: Tutaj sprawdzisz typ ataku oraz Grzech umiejętności, której zamierza użyć sojusznik.
89. [Samouczek i wskazówki [tutorial_301_04] — tekst] 이 곳에서는 각 캐릭터의 약점 내성을 확인할 수 있습니다.\n저 적은 참격에 취약하군요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_301_04].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can see the resistances and weaknesses of each unit up here. This hooligan is vulnerable to Slash attacks.
   PL: W tym miejscu widoczne są odporności i słabości poszczególnych postaci.\nTen przeciwnik jest podatny na Cięcie.
90. [Samouczek i wskazówki [tutorial_302_01] — tekst] 적의 공격을 막기 위해 수비 스킬을 사용할 수도 있습니다.\n상대와 합이 지정된 수비 스킬은 해당 적에게 공격당할 때 사용되며, 합이 지정되지 않은 수비 스킬은 일방 공격당할 때 사용됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_01].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can also use defense skills to deal with an enemy offense.\nDefense skills activate against the enemy attack paired with it.\nIf a defense skill isn't paired, it will activate when the unit is subject to an unopposed attack.
   PL: Aby odeprzeć natarcie wroga, możesz również użyć umiejętności obrony.\nSparowana z wrogiem umiejętność obrony zadziała przeciwko jego atakowi, natomiast niesparowana aktywuje się w chwili otrzymania ataku jednostronnego.
91. [Samouczek i wskazówki [tutorial_302_02] — tekst] 수비 스킬은 공격 스킬과 달리 스킬을 별도로 생성해야 합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_02].content
   limit: do 120 znaków
   EN: Unlike attack skills, defense skills need to be generated.
   PL: W przeciwieństwie do umiejętności ataku umiejętności obrony należy wygenerować osobno.
92. [Samouczek i wskazówki [tutorial_302_03] — tekst] 먼저 가드 스킬을 생성해 보죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_03].content
   limit: do 120 znaków
   EN: Let’s generate a Guard skill first.
   PL: Najpierw wygenerujmy umiejętność Gardy.
93. [Samouczek i wskazówki [tutorial_302_04] — tekst] 그레고르의 초상화를 눌러주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_04].content
   limit: do 120 znaków
   EN: If you’d be so kind as to press Gregor’s portrait.
   PL: Naciśnij portret Gregora.
94. [Samouczek i wskazówki [tutorial_302_05_popup_title] — tekst] 수비 스킬 - 가드
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_05_popup_title].content
   limit: do 120 znaków
   EN: Defense Skills: Guard
   PL: Umiejętność obrony — Garda
95. [Samouczek i wskazówki [tutorial_302_05] — tekst] 가드는 위력만큼 보호막을 얻습니다.\n피격 시 체력 대신 보호막이 감소합니다.\n한 턴에 가드를 여러 번 사용하면, 사용수만큼 가드가 발동합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_05].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Guard creates a shield with health equal to its Power value.\nThis shield will absorb incoming damage first.\nUsing Guard multiple times in a single turn will have it activate that many times.
   PL: Garda zapewnia Tarczę równą swojej Mocy.\nPrzy otrzymaniu ciosu w pierwszej kolejności pomniejszana jest Tarcza zamiast PŻ.\nKilkukrotne użycie Gardy w jednej turze aktywuje ją odpowiednią liczbę razy.
96. [Samouczek i wskazówki [tutorial_302_06] — tekst] 좋아요. 가드 스킬이 생성되었네요. 이제 반격 스킬을 생성해보죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_06].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Good. A Guard skill has been generated.\nLet’s do the same for a Counter skill.
   PL: Dobrze — umiejętność Gardy została wygenerowana. Teraz wygenerujmy umiejętność Kontry.
97. [Samouczek i wskazówki [tutorial_302_07] — tekst] 로쟈의 초상화를 눌러주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_07].content
   limit: do 120 znaków
   EN: If you’d be so kind as to press Rodya’s portrait.
   PL: Naciśnij portret Rodii.
98. [Samouczek i wskazówki [tutorial_302_08_popup_title] — tekst] 수비 스킬 - 반격
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_08_popup_title].content
   limit: do 120 znaków
   EN: Defense Skills: Counter
   PL: Umiejętność obrony — Kontra
99. [Samouczek i wskazówki [tutorial_302_08] — tekst] 반격은 다른 수비 스킬과 다르게 속성이 있으며 사용 시 E.G.O 자원이 생성됩니다.\n반격은 피격 후 대상에게 일방 공격을 가합니다.\n다만, 피격 후 흐트러진다면 반격할 수 없게됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_08].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unlike other defense skills, Counter has an Affinity and will generate its corresponding E.G.O resource.\nWhen using Counter, the unit will launch an unopposed attack after being hit.\nHowever, the unit cannot launch a Counter while Staggered.
   PL: W odróżnieniu od pozostałych umiejętności obrony Kontra posiada własny Grzech i po użyciu generuje zasób E.G.O.\nPo przyjęciu trafienia postać wyprowadza atak jednostronny przeciwko agresorowi.\nJeśli jednak cios doprowadzi do Oszołomienia, Kontra nie zostanie wykonana.
100. [Samouczek i wskazówki [tutorial_302_09] — tekst] 잘하셨어요.\n마지막으로 회피 스킬을 생성해보죠
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_09].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gut gemacht.\nLastly, we’ll generate an Evade skill.
   PL: Znakomicie.\nNa koniec wygenerujmy umiejętność Uniku.
101. [Samouczek i wskazówki [tutorial_302_10] — tekst] 파우스트의 초상화를 눌러주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_10].content
   limit: do 120 znaków
   EN: If you’d be so kind as to press Faust’s portrait.
   PL: Naciśnij portret Faust.
102. [Samouczek i wskazówki [tutorial_302_11_popup_title] — tekst] 수비 스킬 - 회피
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_11_popup_title].content
   limit: do 120 znaków
   EN: Defense Skills: Evade
   PL: Umiejętność obrony — Unik
103. [Samouczek i wskazówki [tutorial_302_11] — tekst] 회피는 상대 스킬보다 최종 위력이 높거나 같으면, 공격을 완전히 회피합니다.\n최종 위력이 낮을 경우 공격을 그대로 받으니 주의하세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_11].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When using Evade, the character will dodge if the Evade’s final Power value is greater than or equal to the incoming attack’s.\nThe attack will hit with full force if the Evade’s Power is lower, so be careful.
   PL: Jeśli Moc końcowa Uniku jest równa lub wyższa od Mocy umiejętności przeciwnika, postać całkowicie unika ataku.\nUważaj — jeśli Moc końcowa okaże się niższa, cios trafi z pełną siłą.
104. [Samouczek i wskazówki [tutorial_302_12] — tekst] 회피 스킬도 정확히 생성되었습니다.\n이제 생성한 수비 스킬을 연결하여 전투 명령을 내려주세요.\n목표는 모든 적의 섬멸입니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_302_12].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: These skills have been generated without a problem.\nNow, utilize them and continue the battle.\nYour goal is to eliminate all of our enemies.
   PL: Umiejętność Uniku również została prawidłowo wygenerowana.\nTeraz połącz wygenerowane umiejętności obrony i wydaj rozkaz do walki.\nCelem jest eliminacja wszystkich wrogów.
105. [Samouczek i wskazówki [tutorial_1001_01] — tekst] 던전에는 <환상체>라는 생명체들이 존재합니다.\n던전에서는 이들과의 전투를 반드시 진행해야하죠.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_01].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In dungeons, creatures we call <Abnormalities> exist.\nEncounters with them will be unavoidable.
   PL: W lochach bytują istoty zwane „Anomaliami”.\nStarcia z nimi są tu nieuniknione.
106. [Samouczek i wskazówki [tutorial_1001_02_popup_title] — tekst] 환상체 / 부위 설명
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_02_popup_title].content
   limit: do 120 znaków
   EN: Abnormalities and their Parts
   PL: Anomalie i ich części
107. [Samouczek i wskazówki [tutorial_1001_02] — tekst] 모든 환상체는 부위를 1개 이상 가지고 있습니다.\n부위마다 슬롯이 존재하며, 스킬을 사용합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_02].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abnormalities consist of at least one body part.\nEach part has its own slots, as well as individual skills.
   PL: Każda Anomalia składa się z co najmniej jednej części ciała.\nKażda część posiada własne pola umiejętności i wyprowadza osobne ataki.
108. [Samouczek i wskazówki [tutorial_1001_03] — tekst] 아군의 스킬을 선택하여 환상체의 스킬 슬롯에 끌어넣어주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_03].content
   limit: do 120 znaków
   EN: Choose one of your Sinner’s skills and drag it to the Abnormality’s skill slot.
   PL: Wybierz umiejętność sojusznika i przeciągnij ją na pole umiejętności Anomalii.
109. [Samouczek i wskazówki [tutorial_1001_04] — tekst] 환상체의 스킬에도 <속도>가 정해집니다.\n환상체의 속도는 행동 순서를 결정하고, 환상체의 공격 타겟을 바꿀 수 있는 조건이 됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abnormality skills also have <Speed> values.\nAlongside determining the order of actions, an Abnormality’s Speeds are something to pay attention to when you wish to redirect its attacks.
   PL: Umiejętnościom Anomalii również przypisana jest „Szybkość”.\nDecyduje ona o kolejności działań i stanowi warunek przejęcia celu ataku Anomalii.
110. [Samouczek i wskazówki [tutorial_1001_05] — tekst] 환상체보다 <속도가 빠른> 아군의 스킬을\n환상체의 스킬 슬롯에 드래그하면,\n<합>이 발생하여 환상체의 공격 타겟을 변경할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_05].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When you order a Sinner with *higher* Speed to target one of the Abnormality’s skill slots, it will be forced to engage in a <Clash> with its new target.
   PL: Przeciągnięcie umiejętności sojusznika o „wyższej Szybkości”\nna pole umiejętności Anomalii\nwywołuje „Starcie” i przekierowuje cel jej ataku.
111. [Samouczek i wskazówki [tutorial_1001_06] — tekst] 속도가 빠른 아군의 스킬을 드래그하여 환상체의 타겟을 변경해주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_06].content
   limit: do 120 znaków
   EN: Drag a skill belonging to a character with higher Speed to change the Abnormality’s target.
   PL: Przeciągnij umiejętność szybszego sojusznika, aby zmienić cel Anomalii.
112. [Samouczek i wskazówki [tutorial_1001_07] — tekst] 환상체의 타겟을 변경했습니다. 이제 저 두 캐릭터는 이번 턴에 합을 진행할 거에요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_07].content
   limit: do 120 znaków
   EN: You’ve redirected the Abnormality’s target. These two will now get into a Clash this turn.
   PL: Cel Anomalii został zmieniony. W tej turze obie postacie zewrą się w Starciu.
113. [Samouczek i wskazówki [tutorial_1001_08] — tekst] 이렇게 속도 차이를 활용하여\n환상체의 타겟을 자유롭게 변경할 수 있습니다.\n집중 전투에서는 <타겟 변경>으로\n유리한 대상과 <합>이 발생하도록 응용하는 것이 중요해요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_08].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: By using Speed this way,\nyou can freely manipulate who an Abnormality attacks.\nIn Focused Encounters, it is vital to *switch targets*\nso that they are forced into Clashes that will play out in your favor.
   PL: Wykorzystując różnicę Szybkości,\nmożesz swobodnie przejmować cele ataków Anomalii.\nW starciach skupionych kluczowe jest takie „przekierowywanie celów”,\nby wymuszać „Starcia” korzystne dla naszej drużyny.
114. [Samouczek i wskazówki [tutorial_1001_09] — tekst] 이제 남은 수감자들에게도 명령을 내려주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_09].content
   limit: do 120 znaków
   EN: Now, give your orders to the rest of the Sinners.
   PL: Wydaj teraz rozkazy pozostałym Grzesznikom.
115. [Samouczek i wskazówki [tutorial_1001_10] — tekst] 수감자들의 스킬을 모두 선택한 뒤 이 쪽을 누르면 전투를 시작할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_10].content
   limit: do 120 znaków
   EN: After you’ve planned out your Sinners’ moves, press here to begin combat.
   PL: Po wybraniu umiejętności dla wszystkich Grzeszników naciśnij tutaj, aby rozpocząć walkę.
116. [Samouczek i wskazówki [tutorial_1001_99_popup_title] — tekst] 부위 파괴
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_99_popup_title].content
   limit: do 120 znaków
   EN: Breaking Parts
   PL: Zniszczenie części
117. [Samouczek i wskazówki [tutorial_1001_99] — tekst] 환상체 부위는 체력이 0이 되면 <부위파괴>가 됩니다.\n부위 파괴가 되면 해당 부위가 가지고 있는 모든 물리 내성이 취약 상태가 됩니다.\n부위에 따라 파괴 시 스킬을 사용하지 못하거나, 패시브가 사라지는 경우도 있습니다.\n부위 파괴 시 환상체에 따라 흉폭해지거나 파괴된 부위가 재생할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1001_99].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When the HP of a body part is reduced to 0, it is <Broken>.\nA broken part becomes vulnerable to all physical attack types.\nSome parts may lose certain skills or passives after breaking.\nDo note that some Abnormalities have regenerative parts, as well as that breaking certain ones may instead enrage an Abnormality.
   PL: Gdy PŻ danej części ciała Anomalii spadną do 0, ulega ona „Zniszczeniu części”.\nWszystkie odporności fizyczne zniszczonej części zmieniają się wówczas na Podatne.\nW zależności od części jej zniszczenie może zablokować niektóre umiejętności lub wyłączyć pasywki.\nNiektóre Anomalie po utracie części wpadają jednak w szał lub potrafią ją zregenerować.
118. [Samouczek i wskazówki [tutorial_1101_01] — tekst] 던전에는 여러 개의 부위를 가진 환상체도 존재합니다.\n부위가 여러 개인 경우,\n각 부위마다 내성과 사용하는 스킬, 패시브가 달라집니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1101_01].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You may find Abnormalities with multiple parts in the dungeons you explore.\nIn such cases, each part will have different Resistances and Passives, and use different skills.
   PL: W lochach napotkasz także Anomalie złożone z wielu części ciała.\nW takim przypadku\nkażda część ma odrębne odporności, umiejętności oraz pasywki.
119. [Samouczek i wskazówki [tutorial_1101_02] — tekst] 이럴 때를 대비해 <환상체 도감>을 준비해두었습니다.\n도감에는 환상체의 부위별 내성, 스킬, 패시브 등의 자료가 적혀있죠.\n환상체를 클릭하여 도감을 확인할 수 있습니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1101_02].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We’ve prepared an <Abnormality Encyclopedia> for occasions like this.\nIt lists the Resistances, Skills, and Passives for each part.\nSelect an Abnormality to view its entry.
   PL: Na taką okoliczność przygotowaliśmy „Kompendium Anomalii”.\nZawiera ono dane o odpornościach, umiejętnościach i pasywkach poszczególnych części.\nKliknij Anomalię, aby otworzyć jej wpis w kompendium.
120. [Samouczek i wskazówki [tutorial_1101_03_popup_title] — tekst] 하지만 도감은 아직 미완성 상태입니다.\n표면적인 조사만으로 환상체를 완전히 파악할 수는 없었죠.\n당신이 환상체를 상대할 때마다 도감이 보완될 거에요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1101_03_popup_title].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: However, the encyclopedia is incomplete at the moment.\nSurface-level analysis can only yield so much information.\nOur entries will be supplemented with more info as you encounter Abnormalities in the field.
   PL: Kompendium jest jednak na razie niekompletne.\nPowierzchowne oględziny nie wystarczyły, by w pełni rozpracować Anomalie.\nWpisy będą uzupełniane w miarę kolejnych starć pod twoim dowództwem.
121. [Samouczek i wskazówki [tutorial_1101_03] — tekst] 환상체 도감에는 부위마다 정보가 기록되어있습니다.\n처음 만난 환상체의 도감은 미완성 상태입니다.\n미완성 상태의 도감은 환상체를 상대하면서 점차 완성됩니다.\n환상체는 여러 번 조우하고 전투할수록 관찰 단계가 증가합니다.\n관찰 단계가 높아질수록 환상체에게 입히는 피해량이 증가합니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1101_03].content
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Abnormality Encyclopedia records information on Abnormalities and their parts.\nBy nature, the Encyclopedia starts out incomplete.\nThe more you fight an Abnormality, the more its entry will be penned in the Encyclopedia.\nAfter enough encounters, the Observation Level for the Abnormality will go up.\nHigher Observation Levels increase the damage you deal against an Abnormality.
   PL: Kompendium Anomalii gromadzi informacje o każdej części ciała.\nPrzy pierwszym spotkaniu wpis Anomalii pozostaje niepełny.\nDane uzupełniają się stopniowo wraz z kolejnymi walkami przeciwko niej.\nWielokrotne starcia z Anomalią podnoszą jej Poziom Obserwacji.\nIm wyższy Poziom Obserwacji, tym większe obrażenia zadajesz danej Anomalii.
122. [Samouczek i wskazówki [tutorial_1201_01] — tekst] 집중 전투 중에는 종종 당신의 결정을 요구하는 <선택지>가 등장합니다.\n당신은 현재의 상황을 고려하여 수감자나 행동을 선택해야하죠.\n선택지의 결과에 따라 환상체의 반응이 달라지니 신중히 선택해주세요.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1201_01].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During Focused Encounters, you may occasionally be tasked to make key <Decisions>.\nThese require you to choose a Sinner or an action based on your current situation.\nAn Abnormality’s response may vastly differ by the choices you make, so choose wisely.
   PL: Podczas starć skupionych niekiedy pojawiają się „wydarzenia” wymagające twojej decyzji.\nMusisz wówczas ocenić sytuację i wskazać odpowiedniego Grzesznika lub działanie.\nReakcja Anomalii zależy od wyniku wyboru, dlatego decyduj rozważnie.
123. [Samouczek i wskazówki [tutorial_1301_01_popup_title] — tekst] 광역 스킬
   źródło: TutorialDesc.json :: dataList[id=tutorial_1301_01_popup_title].content
   limit: do 120 znaków
   EN: Area-of-Effect Skills
   PL: Umiejętności obszarowe
124. [Samouczek i wskazówki [tutorial_1301_01] — tekst] 광역 스킬은 공격 가중치를 가지고 있습니다.\n공격 대상은 광역 스킬의 타겟팅 유형(전열, 중열, 후열, 특수 등)에 따라 달라집니다.\n광역 스킬의 합은 스킬을 직접 지정한\n메인 타겟에게만 발생합니다.\n광역 스킬이 합에서 패배하면,\n해당 스킬의 모든 대상에 대한 공격이 취소됩니다.\n광역 스킬에 피격당할 때에도 수비 스킬이 발동됩니다.
   źródło: TutorialDesc.json :: dataList[id=tutorial_1301_01].content
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Area-of-Effect skills, or AoE skills for short, have an attack weight (Atk Weight) assigned to them.\nThe targets of an AoE skill depend on its targeting range. (Front, Middle, Back, Special, etc.)\nWith AoE skills, Clashes can only occur against the manually targeted unit.\nIf an AoE skill loses in a Clash, the attack will be canceled against all its targets.\nDefense skills will still activate against AoE skills.
   PL: Umiejętności obszarowe posiadają Wagę Ataku.\nCele ataku zależą od zakresu celowania danej umiejętności (przód, środek, tył, specjalny itp.).\nStarcie umiejętności obszarowej zachodzi wyłącznie\nprzeciwko bezpośrednio wskazanemu celowi głównemu.\nJeśli umiejętność obszarowa przegra Starcie,\natak zostaje anulowany wobec wszystkich jej celów.\nPrzeciwko umiejętnościom obszarowym również aktywują się umiejętności obrony.

## Samouczek i wskazówki: TutorialDesc0-4
- plik gry: `TutorialDesc0-4.json`

125. [Samouczek i wskazówki [tutorial_401_01] — tekst] 각 캐릭터는 정해진 <스킬 구성>을 가지고 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_01].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Each character has a <Skillset>.\nThis is the list of skills from which they draw.
   PL: Każda postać dysponuje określonym „zestawem umiejętności”.
126. [Samouczek i wskazówki [tutorial_401_02] — tekst] 캐릭터를 눌러 정보창을 확인할 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_02].content
   limit: do 120 znaków
   EN: Press a character to open their info tab.
   PL: Naciśnij postać, aby otworzyć okno jej informacji.
127. [Samouczek i wskazówki [tutorial_401_03] — tekst] 정보창을 통해 해당 캐릭터의 스킬을 비롯한 다양한 정보를 확인할 수 있죠.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_03].content
   limit: do 120 znaków
   EN: With this, you can check various details including their skills.
   PL: W oknie informacji sprawdzisz szczegóły dotyczące postaci, w tym jej umiejętności.
128. [Samouczek i wskazówki [tutorial_401_04] — tekst] 수감자의 스킬에는 정해진 구성이 있습니다.\n조작 패널에는 아군의 스킬 구성에 있는 스킬이 랜덤하게 배치됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_04].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Each Sinner you control has their own group of skills.\nA number of them from those Skillsets will be randomly selected and deployed on the Dashboard.
   PL: Zestaw umiejętności każdego Grzesznika ma ściśle określony skład.\nNa panelu dowodzenia losowo pojawiają się umiejętności pochodzące z tego zestawu.
129. [Samouczek i wskazówki [tutorial_401_05] — tekst] 한번 사용한 스킬은 스킬 구성에서 제외되며,\n구성 내의 스킬을 <전부 사용>해야 다시 사용할 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_05].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Used skills are treated as “discarded” from the set.\nThey will not reappear until every other skill in the Skillset has been used, thus refilling it.
   PL: Raz użyta umiejętność zostaje odłożona z bieżącej puli\ni powróci dopiero po „wykorzystaniu wszystkich” pozostałych umiejętności z zestawu.
130. [Samouczek i wskazówki [tutorial_401_06] — tekst] 또한 사용하는 공격 스킬에는 공격 레벨이 있습니다.\n공격 레벨의 차이에 따라 합 진행 시 유리하거나 불리해질 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_06].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Additionally, attack skills have an “offense level”.\nIn clashes, the differences in offense levels may affect the outcome.
   PL: Każda umiejętność ataku posiada ponadto Poziom Ataku.\nRóżnica Poziomów Ataku może zapewnić przewagę lub utrudnienie podczas Starcia.
131. [Samouczek i wskazówki [tutorial_401_07] — tekst] 아군의 스킬에 대한 정보는 이해가 되셨나요?\n이제 명령을 내려주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_401_07].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That should cover the basics of your Sinners’ skills.\nNow, give them your orders.
   PL: Czy zasady działania umiejętności sojuszników są już jasne?\nWydaj teraz rozkazy.
132. [Samouczek i wskazówki [tutorial_402_01] — tekst] 인격은 공격 스킬 이외에 <패시브>도 보유하고 있습니다.\n전투에 참여한 인격은 전투 패시브가 활성화 됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_402_01].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Besides skills, your Sinners have <Passive Abilities>.\nSinners in battle have their Combat Passives active.
   PL: Oprócz umiejętności ataku Tożsamości posiadają również „Pasywki”.\nU Tożsamości biorących udział w walce aktywne są ich pasywki bojowe.
133. [Samouczek i wskazówki [tutorial_402_02] — tekst] 전투에 참여하지 않은 인격의 패시브는 서포트 패시브로 적용됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_402_02].content
   (powtórzenie elementu 25 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Samouczek i wskazówki [tutorial_402_03] — tekst] 패시브 발동을 위해 오만 속성의 스킬을 2개 연결해주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_402_03].content
   limit: do 120 znaków
   EN: To put theory into practice, activate the Passive by chaining two Pride skills.
   PL: Aby aktywować pasywkę, połącz 2 umiejętności Grzechu Pychy.
135. [Samouczek i wskazówki [tutorial_402_04] — tekst] 발동된 패시브는 이쪽에서 확인할 수 있습니다.\n패시브는 보유하고 있는 자원 혹은 조작 패널에서 공명을 통해 활성화 됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_402_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This portion will indicate what Passives are active.\nPassives activate when you possess a certain number of E.G.O resources or chain skills of certain Affinities to cause Resonance.
   PL: Aktywne pasywki sprawdzisz w tym miejscu.\nPasywki uruchamiają się dzięki posiadanym zasobom lub wywołaniu Rezonansu na panelu dowodzenia.
136. [Samouczek i wskazówki [tutorial_403_00] — tekst] 앞으로의 전투는 여러 개의 웨이브로 구성되어 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_00].content
   limit: do 120 znaków
   EN: Our current encounter comes in multiple waves.
   PL: Nadchodzące starcie składa się z kilku fal wrogów.
137. [Samouczek i wskazówki [tutorial_403_01] — tekst] 수감자에게는 감정에 공명하여 발현되는 <E.G.O>라는 강력한 스킬이 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_01].content
   limit: do 160 znaków
   EN: To help with this, your Sinners possess powerful skills called <E.G.O>, manifested by resonating with their emotions.
   PL: Grzesznicy dysponują potężnymi umiejętnościami zwanymi „E.G.O”, manifestowanymi poprzez rezonans z emocjami.
138. [Samouczek i wskazówki [tutorial_403_02] — tekst] <E.G.O>를 사용하기 위해서는 E.G.O 자원이 필요합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_02].content
   limit: do 120 znaków
   EN: To use <E.G.O>, you need E.G.O resources.
   PL: Użycie „E.G.O” wymaga zasobów E.G.O.
139. [Samouczek i wskazówki [tutorial_403_03] — tekst] 이 곳에서 현재 보유하고 있는 E.G.O 자원을 확인할 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_03].content
   limit: do 120 znaków
   EN: You can view the E.G.O resources you currently have stockpiled here on the right.
   PL: Tutaj sprawdzisz aktualnie zgromadzone zasoby E.G.O.
140. [Samouczek i wskazówki [tutorial_403_04] — tekst] <E.G.O>를 처음 사용하는 관리자님을 위해 E.G.O 자원을 채워드렸습니다. 특별한 힘이 필요하기 때문에 앞으로는 직접 자원을 모아주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_04].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As this is your first time trying your hand at <E.G.O>, I’ve collected the necessary resources for you.\nThis is a special power, so you’ll need to gather them on your own from now on.
   PL: Ponieważ po raz pierwszy sięgasz po „E.G.O”, Kierowniku, zawczasu uzupełniłam zasoby E.G.O. To wyjątkowa moc, więc od tej pory gromadź je już samodzielnie.
141. [Samouczek i wskazówki [tutorial_403_05] — tekst] <E.G.O>를 사용할 수 있는 수감자는 이러한 표시가 나타납니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_05].content
   limit: do 120 znaków
   EN: Sinners who can currently use <E.G.O> will be highlighted.
   PL: Grzesznicy mogący użyć „E.G.O” są wyróżnieni w ten sposób.
142. [Samouczek i wskazówki [tutorial_403_06] — tekst] <E.G.O 스킬>은 수비 스킬과 마찬가지로 별도의 방법으로 생성이 필요합니다. 이 곳을 길게 눌러주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_06].content
   limit: do 140 znaków
   EN: <E.G.O Skills> must be generated on the Dashboard, much like defense skills. Please press and hold here.
   PL: „Umiejętności E.G.O” — podobnie jak umiejętności obrony — wymagają osobnego wygenerowania. Naciśnij i przytrzymaj to miejsce.
143. [Samouczek i wskazówki [tutorial_403_07] — tekst] 사용할 <E.G.O> 아이콘을 눌러주세요. 생성한 <E.G.O 스킬>은 이와 동일한 조작으로 취소할 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_07].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Press the icon of the <E.G.O> you will use.\nThis can also be used to cancel the ones you’ve generated.
   PL: Naciśnij ikonę „E.G.O”, którego chcesz użyć. Wygenerowaną „umiejętność E.G.O” możesz anulować w ten sam sposób.
144. [Samouczek i wskazówki [tutorial_403_08_title] — tekst] E.G.O
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_08_title].content
   limit: do 120 znaków
   EN: E.G.O
   PL: E.G.O
145. [Samouczek i wskazówki [tutorial_403_08] — tekst] E.G.O는 수감자의 감정에 공명하여 발현되는 강력한 장비입니다.\nE.G.O 스킬을 사용하기 위해서는 E.G.O 자원이 필요합니다.\nE.G.O 자원은 전투에서 스킬을 사용할 때마다, 스킬의 속성과 동일한 자원이 누적됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_08].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O is powerful equipment that manifests by resonating with your Sinners’ emotions.\nTo use an E.G.O skill, you need Sin Affinity-based E.G.O resources.\nWhenever you use an attack skill, you’ll gain an E.G.O resource matching its Affinity.
   PL: E.G.O to potężny ekwipunek manifestowany poprzez rezonans z emocjami Grzeszników.\nUżycie umiejętności E.G.O wymaga zasobów E.G.O.\nZa każdym razem, gdy w walce używasz umiejętności, gromadzisz zasób E.G.O odpowiadający jej Grzechowi.
146. [Samouczek i wskazówki [tutorial_403_09_title] — tekst] E.G.O 침식
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_09_title].content
   limit: do 120 znaków
   EN: E.G.O Corrosion
   PL: Korozja E.G.O
147. [Samouczek i wskazówki [tutorial_403_09] — tekst] E.G.O 스킬을 사용할 때에는 E.G.O 자원과 함께 수감자의 정신력도 소모됩니다.\n정신력이 낮은 상태에서 E.G.O를 사용할 경우\n<E.G.O 침식>이 일어날 수 있습니다.\nE.G.O에 침식된 수감자는 관리자님의 명령을 듣지 않으니 수감자들의 정신력을 항상 신경써야합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_09].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On top of requiring E.G.O resources, E.G.O takes a toll on a Sinner’s Sanity.\nAt low Sanity, the Sinner might suffer from <E.G.O Corrosion>.\nSinners corroded by E.G.O will ignore your commands, so ensure that your Sinners are in good mental health.
   PL: Użycie umiejętności E.G.O pochłania nie tylko zasoby E.G.O, ale także Poczytalność Grzesznika.\nWyzwolenie E.G.O przy niskiej Poczytalności\nmoże doprowadzić do „Korozji E.G.O”.\nGrzesznik objęty Korozją E.G.O nie słucha rozkazów Kierownika, dlatego stale kontroluj stan ich Poczytalności.
148. [Samouczek i wskazówki [tutorial_403_10_title] — tekst] E.G.O 패시브
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_10_title].content
   limit: do 120 znaków
   EN: E.G.O Passives
   PL: Pasywki E.G.O
149. [Samouczek i wskazówki [tutorial_403_10] — tekst] E.G.O 스킬을 사용한 다음 턴부터 해당 전투동안 E.G.O 패시브가 적용됩니다.\nE.G.O마다 다양한 패시브를 보유하고 있으니 잘 활용해주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_10].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After using an E.G.O Skill, its Passive ability will activate on the next turn and further empower the Sinner for the rest of the battle.\nMake good use of the variety of Passives that E.G.O has to offer.
   PL: Od tury następującej po użyciu umiejętności E.G.O aż do końca danej walki działa pasywka tego E.G.O.\nKażde E.G.O oferuje odmienną pasywkę — rób z nich właściwy użytek.
150. [Samouczek i wskazówki [tutorial_403_11] — tekst] 공격 스킬에는 단일 스킬과 광역 스킬이 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_11].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack skills can be single-target or multi-target;\nthe latter are called “AoE Skills”.
   PL: Umiejętności ataku dzielą się na pojedyncze oraz obszarowe.
151. [Samouczek i wskazówki [tutorial_403_12] — tekst] 이번에 사용하는 <E.G.O 스킬>은 광역 스킬이네요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_12].content
   limit: do 120 znaków
   EN: It seems the E.G.O that’s about to be in play has an AoE Skill.
   PL: Używana teraz „umiejętność E.G.O” jest umiejętnością obszarową.
152. [Samouczek i wskazówki [tutorial_403_13_title] — tekst] 광역 스킬
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_13_title].content
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [Samouczek i wskazówki [tutorial_403_13] — tekst] 광역 스킬은 메인 타겟과 서브 타겟으로 대상이 나뉩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_13].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Targets of AoE skills are divided into two categories:\nthe main target, and sub-targets.
   PL: Cele umiejętności obszarowej dzielą się na cel główny oraz cele poboczne.
154. [Samouczek i wskazówki [tutorial_403_14] — tekst] 광역 스킬과 합은 직접 지정한 메인 타겟에게만 발생합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_14].content
   limit: do 120 znaków
   EN: Clashes with AoE skills can only occur from the chosen main target.
   PL: Starcie umiejętności obszarowej zachodzi wyłącznie przeciwko bezpośrednio wskazanemu celowi głównemu.
155. [Samouczek i wskazówki [tutorial_403_15] — tekst] 합에서 패배한다면 해당 스킬의 모든 대상에 대한 공격은 취소됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_15].content
   limit: do 120 znaków
   EN: If an AoE skill loses its Clash, the attack will be canceled for every target.
   PL: W razie przegrania Starcia atak tej umiejętności zostaje anulowany wobec wszystkich celów.
156. [Samouczek i wskazówki [tutorial_403_16] — tekst] 서브 타겟은 광역 스킬의 타겟팅 유형에 따라서 달라집니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_16].content
   limit: do 120 znaków
   EN: Sub-targets are determined by the targeting range of the skill.
   PL: Cele poboczne zależą od zakresu celowania danej umiejętności obszarowej.
157. [Samouczek i wskazówki [tutorial_403_17_title] — tekst] 광역 스킬은 메인 타겟과 서브 타겟으로 대상이 나뉩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_17_title].content
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [Samouczek i wskazówki [tutorial_403_17] — tekst] 광역 스킬은 적의 슬롯을 타겟합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_17].content
   limit: do 120 znaków
   EN: AoE skills target enemy skill slots.
   PL: Umiejętności obszarowe celują w pola umiejętności wrogów.
159. [Samouczek i wskazówki [tutorial_403_18] — tekst] 광역 스킬마다 공격 가중치가 정해져 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_18].content
   limit: do 120 znaków
   EN: Each AoE skill has an attack weight (Atk Weight).
   PL: Każda umiejętność obszarowa ma określoną Wagę Ataku.
160. [Samouczek i wskazówki [tutorial_403_19] — tekst] 슬롯에는 가중치가 있으며, 슬롯은 그 수만큼 광역 스킬의 공격 가중치를 소모시킬 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_19].content
   limit: do 120 znaków
   EN: Each slot has a “weight” which can take up a portion of an AoE skill's Atk Weight.
   PL: Każde pole ma własną wagę i pochłania odpowiadającą jej część Wagi Ataku umiejętności obszarowej.
161. [Samouczek i wskazówki [tutorial_403_20] — tekst] 일반 전투에서 적 하나는 광역 스킬에 여러 번 타겟이 되더라도 한 번만 공격 당합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_20].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In regular encounters, an enemy is only attacked once by an AoE skill, even if the unit is taking up multiple targets.
   PL: W zwykłym starciu pojedynczy wróg otrzymuje trafienie umiejętnością obszarową tylko raz, nawet jeśli zajęto kilka jego pól.
162. [Samouczek i wskazówki [tutorial_403_21] — tekst] 집중 전투에서는 부위 슬롯에 여러 번 타겟이 되어도 부위당 한 번만 공격 당합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_21].content
   limit: do 170 znaków
   EN: In Focused Encounters, the slots on their body parts are only attacked once, even if said slots are taking up multiple targets.
   PL: W starciu skupionym dana część ciała otrzymuje trafienie tylko raz, nawet jeśli wycelowano w kilka jej pól.
163. [Samouczek i wskazówki [tutorial_404_00] — tekst] 이렇게 E.G.O를 잘 활용하는 것도 중요한 전략 중 하나입니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_00].content
   limit: do 120 znaków
   EN: Utilizing E.G.O will be an important part of your strategy.
   PL: Umiejętne wykorzystanie E.G.O stanowi jeden z filarów skutecznej strategii.
164. [Samouczek i wskazówki [tutorial_404_01] — tekst] 앞으로의 전투는 여러 개의 웨이브로 구성되어 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_01].content
   (powtórzenie elementu 136 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [Samouczek i wskazówki [tutorial_404_02] — tekst] 남은 전투에 앞서 유용한 기능을 설명드리죠.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_02].content
   limit: do 120 znaków
   EN: Before we proceed, allow me to introduce you to a useful feature.
   PL: Przed dalszą walką wyjaśnię jeszcze jedną przydatną funkcję.
166. [Samouczek i wskazówki [tutorial_404_03] — tekst] 이제부터 스킬의 자동 선택이 가능합니다.\n관리자님이 누르는 버튼에 따라 자동으로 스킬이 선택되죠.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_03].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can now let the game chain skills for you.\nChains will be automatically chosen depending on what button you press.
   PL: Od teraz dostępny jest automatyczny dobór umiejętności.\nW zależności od wybranego przycisku łańcuch umiejętności zostanie ułożony automatycznie.
167. [Samouczek i wskazówki [tutorial_404_04] — tekst] <승률> 버튼은 합 승리 확률이 높은 스킬 위주로 스킬을 선택합니다.\n<피해량> 버튼은 적에게 피해를 높게 줄 수 있는 스킬 위주로 스킬을 선택합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_04].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ‘Win Rate’ picks skills that are the most likely to win Clashes.\n‘Damage’, as the name implies, picks skills that can hurt your enemies the most.
   PL: Przycisk „Szansa” dobiera umiejętności o najwyższej szansie zwycięstwa w Starciach.\nPrzycisk „Obrażenia” wybiera umiejętności zadające wrogom jak największe obrażenia.
168. [Samouczek i wskazówki [tutorial_404_05] — tekst] 하지만 자동 선택은 관리자님만큼 여러가지 전투 상황들을 고려하지 못하니 주의가 필요합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_05].content
   limit: do 160 znaków
   EN: However, do keep in mind that auto-chaining does not take the full extent of every complex factor into consideration.
   PL: Pamiętaj jednak, że automatyczny dobór nie uwzględnia złożonych niuansów pola bitwy tak dokładnie jak Kierownik.
169. [Samouczek i wskazówki [tutorial_404_06] — tekst] 또한 우상단에서 타겟팅 화살표 표시와 환경 설정을 통해 전투의 스킬 툴 표시와 코인 토스를 조정할 수 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_06].content
   limit: do 210 znaków
   EN: Also, you can toggle target arrow displays using the panel on the upper right, and configure the skill tooltip display and Coin flip controls from the settings.
   PL: W prawym górnym rogu możesz ponadto przełączać strzałki celowania oraz dostosować w ustawieniach opisy umiejętności i rzuty monetami.
170. [Samouczek i wskazówki [tutorial_404_07] — tekst] 이제 더 이상 드릴 도움이 없습니다.\n직접 명령을 내려주세요.\n앞으로 훌륭한 명령을 기대하죠. 단테.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_07].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: That’s the last of my advice.\nNow, manage the Sinners without my help.\nI expect to receive superb commands from you, Dante.
   PL: To już wszystko, w czym mogłam pomóc.\nWydaj rozkazy osobiście.\nLiczę na znakomite dowodzenie, Dante.
171. [Samouczek i wskazówki [tutorial_404_08_title] — tekst] 피해량 승률 자동전투
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_08_title].content
   limit: do 120 znaków
   EN: Damage & Win Rate Auto-chaining
   PL: Automatyczny dobór: Obrażenia i Szansa
172. [Samouczek i wskazówki [tutorial_404_08] — tekst] “승률” 버튼은 합 승리 확률이 높은 스킬 위주로 선택됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_08].content
   limit: do 120 znaków
   EN: ‘Win Rate’ picks skills that are the most likely to win Clashes.
   PL: Przycisk „Szansa” wybiera umiejętności o najwyższym prawdopodobieństwie wygrania Starć.
173. [Samouczek i wskazówki [tutorial_404_09] — tekst] “피해량” 버튼은 적에게 피해를 높게 줄 수 있는 스킬 위주로 선택됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_09].content
   limit: do 120 znaków
   EN: ‘Damage’, as the name implies, picks skills that can hurt your enemies the most.
   PL: Przycisk „Obrażenia” wybiera umiejętności zadające wrogom najwyższe obrażenia.
174. [Samouczek i wskazówki [tutorial_404_10] — tekst] 자동 선택 버튼은 일반 전투에서는 EX클리어한 스테이지, 집중 전투는 처음부터 사용할 수 있습니다.\n자동 선택은 여러 전투 상황들을 고려하지는 못하니 사용에 주의가 필요합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_404_10].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For regular encounters, auto-chaining is only available on stages where you’ve cleared the EX Conditions.\nAuto-chaining can always be used for Focused Encounters.\nNote that auto-chains are not necessarily the guaranteed optimal solution.
   PL: W zwykłych starciach przyciski automatycznego doboru są dostępne po ukończeniu etapu z warunkiem EX, natomiast w starciach skupionych — od samego początku.\nAutomatyczny dobór nie bierze pod uwagę wszystkich okoliczności walki, dlatego korzystaj z niego z rozwagą.
175. [Samouczek i wskazówki [tutorial_ego_overclock_title] — tekst] E.G.O 오버클록
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_title].content
   limit: do 120 znaków
   EN: E.G.O Overclock
   PL: Przeciążenie E.G.O
176. [Samouczek i wskazówki [tutorial_ego_overclock_1] — tekst] 오버클록은 안정 오버클록과 불안정 오버클록이 있습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_1].content
   limit: do 120 znaków
   EN: E.G.O Overclock can be Stable or Unstable depending on resources available.
   PL: Przeciążenie dzieli się na Stabilne Przeciążenie oraz Niestabilne Przeciążenie.
177. [Samouczek i wskazówki [tutorial_ego_overclock_2] — tekst] 오버클록 시 에고 스킬이 사용하는 자원과 소모 정신력의 1.5배만큼 사용됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_2].content
   limit: do 130 znaków
   EN: Overclocking spends 1.5 times as many E.G.O resources and SP as the E.G.O skill’s usual cost.
   PL: Podczas Przeciążenia zużywana jest 1,5-krotność standardowego kosztu zasobów oraz Poczytalności umiejętności E.G.O.
178. [Samouczek i wskazówki [tutorial_ego_overclock_3] — tekst] 오버클록을 위해서는 에고를 사용할 수 있는 기본 자원이 필요하며, 자원이 부족한 경우 음수 처리됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_3].content
   limit: do 270 znaków
   EN: To overclock an E.G.O skill, you need to possess at least the base E.G.O resource cost; if you have the base cost but not enough for overclock, the overclock cost will be subtracted from your possession beyond 0.
   PL: Do Przeciążenia wymagane jest posiadanie co najmniej podstawowego kosztu zasobów E.G.O — brakująca nadwyżka zostanie odjęta poniżej zera.
179. [Samouczek i wskazówki [tutorial_ego_overclock_4] — tekst] 오버클록을 사용해도 침식 당할 수 있으며, 침식 시에는 기본 자원만큼만 사용됩니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_4].content
   limit: do 150 znaków
   EN: The unit can still be corroded upon overclocking; in this case, only the base E.G.O resource cost will be consumed.
   PL: Nawet przy Przeciążeniu może dojść do samoistnej Korozji; zużyty zostaje wówczas wyłącznie podstawowy koszt zasobów.
180. [Samouczek i wskazówki [tutorial_ego_overclock_5] — tekst] 안정 오버클록은 피아식별이 가능한 상태이며, 침식 에고의 스킬 효과 및 수치는 같습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_5].content
   limit: do 190 znaków
   EN: Stable overclocked E.G.O skills have the same effects and damage values as the corrosion skill while being able to distinguish allies from foes.
   PL: Stabilne Przeciążenie zachowuje efekty i wartości Korozyjnego E.G.O, pozwalając jednocześnie odróżniać sojuszników od wrogów.
181. [Samouczek i wskazówki [tutorial_ego_overclock_6] — tekst] 불안정 오버클록은 피아식별이 불가능하며, 침식 에고의 스킬 효과 및 수치는 같습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_ego_overclock_6].content
   limit: do 180 znaków
   EN: Unstable overclocked skills carry the risk of targeting indiscriminately and have the same effects and values as the corrosion skill.
   PL: Niestabilne Przeciążenie ma takie same efekty i wartości jak Korozyjne E.G.O, lecz uniemożliwia odróżnianie sojuszników od wrogów.
182. [Samouczek i wskazówki [tutorial_403_06_New] — tekst] <E.G.O 스킬>은 수비 스킬과 마찬가지로 별도의 방법으로 생성이 필요합니다. 테두리 색이 활성화된 초상화를 길게 눌러주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_06_New].content
   limit: do 160 znaków
   EN: <E.G.O Skills> must be generated on the Dashboard, much like defensive skills. Press and hold the highlighted portrait.
   PL: „Umiejętności E.G.O” — podobnie jak umiejętności obrony — wymagają osobnego wygenerowania. Naciśnij i przytrzymaj podświetlony portret.
183. [Samouczek i wskazówki [tutorial_403_07_New] — tekst] 사용할 <E.G.O> 아이콘을 눌러주세요.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_07_New].content
   limit: do 120 znaków
   EN: Press the icon of the <E.G.O> you want to use.
   PL: Naciśnij ikonę „E.G.O”, którego chcesz użyć.
184. [Samouczek i wskazówki [tutorial_403_07_1] — tekst] E.G.O 자원을 소모하여 다음과 같이 E.G.O 스킬 아이콘을 조작 패널에 생성합니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_07_1].content
   limit: do 120 znaków
   EN: Consume E.G.O Resources to generate an E.G.O. Skill icon on the Dashboard.
   PL: Zużyj zasoby E.G.O, aby wygenerować ikonę umiejętności E.G.O na panelu dowodzenia.
185. [Samouczek i wskazówki [tutorial_403_07_2] — tekst] E.G.O 스킬이 생성된 상태에서 초상화를 두 번 연속으로 누르면, 생성한 E.G.O 아이콘이 사라지고 E.G.O 자원을 돌려받습니다.
   źródło: TutorialDesc0-4.json :: dataList[id=tutorial_403_07_2].content
   limit: do 220 znaków
   EN: E.G.O. Skills can be canceled by tapping on the portrait twice once they are added to the Dashboard. The E.G.O. skill will be canceled and your resources will be refunded.
   PL: Dwukrotne dotknięcie portretu przy wygenerowanej umiejętności E.G.O usuwa jej ikonę i zwraca zużyte zasoby E.G.O.

## Samouczek i wskazówki: TutorialDesc_Ab
- plik gry: `TutorialDesc_Ab.json`

186. [Samouczek i wskazówki [tutorial_1001_renewal_01] — tekst] 던전에는 환상체라는 것이 존재합니다. 가장 신중하게 대처해야하는 적이죠.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_01].content
   limit: do 140 znaków
   EN: In dungeons, you may encounter entities known as 'Abnormalities'. These enemies require a careful strategy.
   PL: W lochach bytują istoty zwane Anomaliami. To przeciwnicy wymagający najwyższej ostrożności.
187. [Samouczek i wskazówki [tutorial_1001_renewal_02] — tekst] 이들을 상대하기 위해서는 일반적인 전투보다 세밀한 방향으로 전투를 진행해야합니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_02].content
   limit: do 130 znaków
   EN: Therefore, you must employ a different, more hands-on approach to combat when facing these enemies.
   PL: Walka z nimi wymaga bardziej precyzyjnego dowodzenia niż zwykłe potyczki.
188. [Samouczek i wskazówki [tutorial_1001_renewal_03] — tekst] 이러한 전투 방식을 집중 전투라고 합니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_03].content
   limit: do 120 znaków
   EN: Encounters where you must use this hands-on approach are called 'Focused Encounters'.
   PL: Ten tryb walki nazywamy starciem skupionym.
189. [Samouczek i wskazówki [tutorial_1001_renewal_04] — tekst] 일반 전투에서는, 조작 패널의 왼쪽 기어에서 오른쪽 기어까지 스킬 아이콘을 차례대로 연결했어요.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_04].content
   limit: do 160 znaków
   EN: In Regular Encounters, you gave command to your sinners by chaining Skills from the left end of the Dashboard to the right.
   PL: W zwykłych starciach łączyliśmy po kolei ikony umiejętności od lewego do prawego koła zębatego na panelu dowodzenia.
190. [Samouczek i wskazówki [tutorial_1001_renewal_05] — tekst] 집중 전투에서는 아군의 스킬 아이콘을 선택한 후, 직접 환상체의 스킬 슬롯에 연결해 주어야 합니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_05].content
   limit: do 180 znaków
   EN: In Focused Encounters, however, you must select the Sinners' Skill icons and chain them directly against the Abnormalities' Skill Slots.
   PL: W starciach skupionych należy natomiast wybrać ikonę umiejętności sojusznika i połączyć ją bezpośrednio z polem umiejętności Anomalii.
191. [Samouczek i wskazówki [tutorial_1001_renewal_06] — tekst] 그럼 전투를 직접 진행해보기로 하죠. 조작 패널 첫 번째 열에 배치된 수감자의 스킬을 선택해주세요.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_06].content
   limit: do 130 znaków
   EN: Let us perform a hands-on field exercise. Select a Skill from the leftmost column of the Dashboard.
   PL: Przejdźmy do praktyki. Wybierz umiejętność Grzesznika w pierwszej kolumnie panelu dowodzenia.
192. [Samouczek i wskazówki [tutorial_1001_renewal_07] — tekst] 선택한 아군의 스킬 아이콘을 적 스킬 슬롯과 연결해주세요.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_07].content
   limit: do 120 znaków
   EN: Chain the selected Skill icon to the entity's Skill Slot.
   PL: Połącz wybraną ikonę umiejętności sojusznika z polem umiejętności wroga.
193. [Samouczek i wskazówki [tutorial_1001_renewal_08] — tekst] 정확합니다. 방금과 같이 아군의 스킬을 적 스킬 슬롯에 직접 연결하는 것이 집중 전투의 기본입니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_08].content
   limit: do 150 znaków
   EN: Precisely. Remember: in Focused Encounters, connect the Sinners' Skills directly to the enemies' Skill Slots.
   PL: Dokładnie tak. Bezpośrednie łączenie umiejętności sojuszników z polami umiejętności wrogów to podstawa starć skupionych.
194. [Samouczek i wskazówki [tutorial_1001_renewal_09] — tekst] 만약 전투의 전반적인 상황을 확인하기 위해 시야를 원래대로 되돌리고 싶으시다면, 왼쪽 기어를 눌러주세요.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_09].content
   limit: do 130 znaków
   EN: Please press the gear on the left if you would like to zoom out and view the entire battlefield.
   PL: Jeśli chcesz oddalić widok, by ocenić sytuację na całym polu bitwy, naciśnij lewe koło zębate.
195. [Samouczek i wskazówki [tutorial_1001_renewal_10] — tekst] 잘하셨어요. 시야가 확대된 상태에서 왼쪽 기어를 누르면 전투 시작 시점의 시야로 초기화 됩니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_10].content
   limit: do 120 znaków
   EN: Good. Pressing the gear on the left while zoomed in will reset your field of view.
   PL: Doskonale. Naciśnięcie lewego koła zębatego przy przybliżonej kamerze przywraca początkowy widok pola walki.
196. [Samouczek i wskazówki [tutorial_1001_renewal_11] — tekst] 조작 패널에 배치된 아군의 스킬을 전부 연결하면, 오른쪽 기어가 활성화되어 전투를 진행할 수 있습니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_11].content
   limit: do 220 znaków
   EN: Once you have selected and connected every available Skill to the enemies' Skill Slots, the gear on the right will activate. Then, you can proceed to the Combat Phase.
   PL: Po przypisaniu wszystkich umiejętności sojuszników na panelu dowodzenia uaktywni się prawe koło zębate, pozwalając rozpocząć fazę walki.
197. [Samouczek i wskazówki [tutorial_1001_renewal_12] — tekst] 그럼, 관리자 님. 모든 수감자에게 전투 명령을 내려주시길 바랍니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_12].content
   limit: do 120 znaków
   EN: Then, dear Manager. Please command your Sinners so that we may continue the battle.
   PL: Proszę więc, Kierowniku — wydaj rozkazy bojowe wszystkim Grzesznikom.
198. [Samouczek i wskazówki [tutorial_1001_renewal_13] — tekst] 집중 전투의 기본에 대한 설명을 여기서 마치고, 본격적인 전투에 들어가기 앞서 속도에 대해 설명드리겠습니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_13].content
   limit: do 150 znaków
   EN: Thus ends the basics of introduction to Focused Encounters. "Speed" before we continue further into the battle.
   PL: Na tym kończymy podstawy starć skupionych. Zanim przejdziemy do właściwej bitwy, omówię jeszcze rolę Szybkości.
199. [Samouczek i wskazówki [tutorial_1001_renewal_14] — tekst] 환상체는 하나 이상의 부위를 가지고 있습니다. 스킬 슬롯 상단에 표시된 속도는 해당 부위의 속도와 동일합니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_14].content
   limit: do 200 znaków
   EN: Abnormalities often have multiple parts that can be targeted. The "Speed" displayed above their Skill Slots reflect the Speed of the corresponding Parts.
   PL: Anomalie składają się z co najmniej jednej części ciała. Szybkość widoczna nad polem umiejętności jest równa Szybkości odpowiadającej mu części.
200. [Samouczek i wskazówki [tutorial_1001_renewal_01_popup_title] — tekst] 환상체의 부위
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_01_popup_title].content
   limit: do 120 znaków
   EN: Abnormality Parts
   PL: Części ciała Anomalii
201. [Samouczek i wskazówki [tutorial_1001_renewal_01_popup_desc] — tekst] 모든 환상체는 1개 이상의 부위가 있습니다.\n부위마다 스킬 슬롯이 존재하여 스킬을 사용합니다.\n스킬 슬롯의 속도는 해당 부위의 속도와 동일합니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_01_popup_desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Abnormalities often have multiple Parts that can be targeted.\nEach Part will use Skills from the Skill Slots assigned to them.\nThe Skill Slots' Speed is the same as the Speed of the Part using them.
   PL: Każda Anomalia posiada co najmniej 1 część ciała.\nKażda część dysponuje własnymi polami umiejętności, z których wyprowadza ataki.\nSzybkość pola umiejętności jest równa Szybkości danej części.
202. [Samouczek i wskazówki [tutorial_1001_renewal_15] — tekst] 전투는 기본적으로 속도 순으로 진행됩니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_15].content
   limit: do 120 znaków
   EN: Speed determines the order of actions in encounters.
   PL: Walka toczy się zasadniczo w kolejności wynikającej z Szybkości.
203. [Samouczek i wskazówki [tutorial_1001_renewal_16] — tekst] 일반 전투와 달리 집중 전투에서는 목표를 직접 지정하기 때문에, 속도를 이용하여 공격 대상을 이끌어올 수 있습니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_16].content
   limit: do 260 znaków
   EN: Unlike in Regular Encounters, you can select which enemies to target in Focused Encounters. You can use Sinners with higher Speed values to force enemies with lower Speed values to target them instead.
   PL: Ponieważ w starciach skupionych wskazujesz cele ręcznie, możesz wykorzystać wyższą Szybkość, aby przejąć atak przeciwnika.
204. [Samouczek i wskazówki [tutorial_1001_renewal_17] — tekst] 만약 아군의 속도가 환상체보다 빠르다면, 해당 환상체의 공격이 대상 아군을 향하도록 이끌어올 수 있습니다. 이 과정에서 합이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_17].content
   limit: do 170 znaków
   EN: Sinners with higher Speed values can force Abnormalities with lower Speed values to target them instead, resulting in a Clash.
   PL: Jeśli sojusznik jest szybszy od części Anomalii, może ściągnąć jej atak na siebie, doprowadzając do Starcia.
205. [Samouczek i wskazówki [tutorial_1001_renewal_18] — tekst] 만약 아군의 속도가 환상체와 같거나 느리다면, 해당 환상체의 공격이 대상 아군을 향하도록 이끌어올 수 없습니다. 이 과정에서는 합이 아닌 일방 공격이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_18].content
   limit: do 330 znaków
   EN: Sinners with lower or equal Speed values can not force Abnormalities with higher Speed values to target them. Chaining the Skill of a slower Sinner to a faster Abnormality will cause them to conduct an Unopposed attack instead of Clashing with the Abnormality.
   PL: Jeśli Szybkość sojusznika jest równa lub niższa od Szybkości Anomalii, nie zdoła on przejąć celu jej ataku — zamiast Starcia wykona wówczas atak jednostronny.
206. [Samouczek i wskazówki [tutorial_1001_renewal_19] — tekst] 속도와 관계없이 수감자가 환상체 스킬의 목표 대상이 되었을 때, 스킬을 사용하여 해당 환상체 스킬에 맞대응을 하게 되면 합이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_19].content
   limit: do 250 znaków
   EN: Sinners that are targeted by an Abnormality's Skill, however, can use their Skill to Clash with the Abnormality's Skill that's targeting them. In such a case, Speed is not a relevant factor.
   PL: Niezależnie od Szybkości Grzesznik będący już celem umiejętności Anomalii może odpowiedzieć własną umiejętnością na to pole, doprowadzając do Starcia.
207. [Samouczek i wskazówki [tutorial_1001_renewal_20] — tekst] 아무래도 설명으로만 들으면 복잡하게 느껴질 수 밖에 없겠죠. 지금은 아군의 속도가 적보다 높을 때, 적 공격에 일방적으로 당하지 않고 대응하기 용이하다는 것만 알아주세요.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_20].content
   limit: do 270 znaków
   EN: I understand that hands-on experience may be the best way to learn. For now, simply keep in mind that Sinners with higher Speed values can redirect attacks from enemies with lower Speed values to themselves.
   PL: Sama teoria może brzmieć zawile — na razie zapamiętaj po prostu, że wyższa Szybkość sojuszników ułatwia przejmowanie ataków wroga zamiast przyjmowania ciosów bez obrony.
208. [Samouczek i wskazówki [tutorial_1001_renewal_02_popup_title] — tekst] 속도가 빠른 경우
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_02_popup_title].content
   limit: do 120 znaków
   EN: Sinner's Speed > Enemy's Speed
   PL: Gdy sojusznik jest szybszy
209. [Samouczek i wskazówki [tutorial_1001_renewal_02_popup_desc] — tekst] 만약 아군의 속도가 환상체보다 빠르다면, 해당 환상체의 공격이 대상 아군을 향하도록 이끌어올 수 있습니다.\n이 과정에서 합(노란색 화살표)이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_02_popup_desc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sinners with higher Speed values can force Abnormalities with lower Speed values to target them instead.\nThis will lead to a Clash(marked by yellow arrows) between the Sinner and the Abnormality.
   PL: Jeśli Szybkość sojusznika przewyższa Szybkość Anomalii, może on ściągnąć jej atak na siebie.\nDochodzi wówczas do Starcia (żółta strzałka).
210. [Samouczek i wskazówki [tutorial_1001_renewal_03_popup_title] — tekst] 속도가 같거나 느린 경우
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_03_popup_title].content
   limit: do 120 znaków
   EN: Sinner's Speed ≤ Enemy's Speed
   PL: Gdy Szybkość jest równa lub niższa
211. [Samouczek i wskazówki [tutorial_1001_renewal_03_popup_desc] — tekst] 만약 아군의 속도가 환상체와 같거나 느리다면, 해당 환상체의 공격이 대상 아군을 향하도록 이끌어올 수 없습니다.\n이 과정에서는 합이 아닌 일방 공격 (파란색 화살표)이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_03_popup_desc].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sinners with lower or equal Speed values can not force Abnormalities with higher Speed values to target them.\nIn such a case, the Sinner will conduct an Unopposed attack(marked by blue arrows) instead of Clashing with the Abnormality.
   PL: Jeśli Szybkość sojusznika jest równa lub niższa od Szybkości Anomalii, nie może on przejąć celu jej ataku.\nZamiast Starcia następuje wówczas atak jednostronny (niebieska strzałka).
212. [Samouczek i wskazówki [tutorial_1001_renewal_04_popup_title] — tekst] 맞대응하는 경우
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_04_popup_title].content
   limit: do 120 znaków
   EN: When targeted by an enemy Skill
   PL: Bezpośrednia odpowiedź celu
213. [Samouczek i wskazówki [tutorial_1001_renewal_04_popup_desc] — tekst] 속도와 관계없이 수감자가 환상체 스킬의 목표 대상이 되었을 때, 스킬을 사용하여 해당 환상체 스킬에 맞대응을 하게 되면 합(노란색 화살표)이 이루어집니다.
   źródło: TutorialDesc_Ab.json :: dataList[id=tutorial_1001_renewal_04_popup_desc].content
   limit: do 270 znaków
   EN: Sinners that are targeted by an Abnormality's Skill can use their Skill to Clash(marked by yellow arrows) with the Abnormality's Skill that's targeting them. In such a case, Speed is not a relevant factor.
   PL: Niezależnie od Szybkości Grzesznik obrany na cel umiejętności Anomalii może odpowiedzieć na nią własną umiejętnością, doprowadzając do Starcia (żółta strzałka).

## Samouczek i wskazówki: TutorialMainUIText
- plik gry: `TutorialMainUIText.json`

214. [Samouczek i wskazówki [tutorial_mainui_01_selection] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection].content
   limit: do 120 znaków
   EN: Creating your Team
   PL: Skład
215. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_01_desc_01] — tekst] 림버스 수감자 12명의 인격을 조합하여 하나의 편성을 만들 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can configure a Team from your 12 Sinners and their Identities.
   PL: Z Tożsamości 12 Grzeszników Limbus Company możesz utworzyć wspólny skład.
216. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_02_title_01] — tekst] 편성 (수감자 창)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_02_title_01].content
   limit: do 120 znaków
   EN: Team (Sinners Window)
   PL: Skład (okno Grzeszników)
217. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_02_desc_01] — tekst] 수감자 창에서 인격 초상화를 터치하면 인격 목록이 등장하여 편성을 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_02_desc_01].content
   limit: do 190 znaków
   EN: In 'Sinners' window, selecting a Sinner's Identity portrait will show a list of their Identities. From there, you can choose an Identity to deploy.
   PL: Dotknięcie portretu Tożsamości w oknie Grzeszników otwiera listę Tożsamości i pozwala zmienić skład.
218. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_03_title_01] — tekst] 편성 (전투 콘텐츠)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_03_title_01].content
   limit: do 120 znaków
   EN: Team (Before Battles)
   PL: Skład (przed walką)
219. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_03_desc_01] — tekst] 각종 전투 콘텐츠의 편성 창에서 인격 초상화 상단을 터치하면 인격 목록이 등장하여 편성을 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_03_desc_01].content
   limit: do 190 znaków
   EN: Selecting the top part of a Sinner's Identity portrait will show a list of their Identities. From there, you can select an Identity to deploy.
   PL: Dotknięcie górnej części portretu w oknie składu przed walką otwiera listę Tożsamości i pozwala zmienić wyposażoną Tożsamość.
220. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_04_desc_01] — tekst] 각종 전투 콘텐츠의 편성 창에서 인격 초상화 하단을 터치하면 해당 인격이 전투에 참가하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_04_desc_01].content
   limit: do 130 znaków
   EN: Selecting the bottom part of a Sinner's Identity portrait will deploy that Identity to this battle.
   PL: Dotknięcie dolnej części portretu w oknie składu przed walką wybiera daną Tożsamość do udziału w bitwie.
221. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_04_desc_02] — tekst] 전투에 참가할 수 있는 최대 인격 수가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_04_desc_02].content
   limit: do 120 znaków
   EN: This shows the total number of deployable Identities for this battle.
   PL: Pokazuje maksymalną liczbę Tożsamości mogących wziąć udział w tej walce.
222. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_05_desc_01] — tekst] 편성을 변경할 수 없는 특정 전투 콘텐츠에서는 인격 초상화를 터치하면 해당 인격이 전투에 참가하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_05_desc_01].content
   limit: do 210 znaków
   EN: You will not be able to edit your Team in certain battle encounters. In those cases, selecting a Sinner's Identity portrait will deploy that Identity to battle.
   PL: W trybach, w których zmiana Tożsamości jest zablokowana, dotknięcie portretu wyznacza daną Tożsamość bezpośrednio do udziału w walce.
223. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_06_title_01] — tekst] 편성 - 인격 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_06_title_01].content
   limit: do 120 znaków
   EN: Team - Identity Details
   PL: Skład — informacje o Tożsamości
224. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_06_desc_01] — tekst] 모든 편성 창에서는 인격 초상화를 길게 터치하면 인격 정보가 등장하여 인격과 E.G.O에 대한 상세 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_06_desc_01].content
   limit: do 190 znaków
   EN: In all Team menus, you can press and hold on an Identity portrait to view detailed information on that Sinner's currently equipped Identity & E.G.O.
   PL: W każdym oknie składu przytrzymanie portretu otwiera szczegółowe informacje o wyposażonej Tożsamości oraz E.G.O.
225. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_07_title_01] — tekst] 아나운서 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_07_title_01].content
   limit: do 120 znaków
   EN: Select Battle Announcer
   PL: Wybór komentatora
226. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_07_desc_01] — tekst] 선택 시, 아나운서 목록이 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_07_desc_01].content
   limit: do 120 znaków
   EN: Select this button to view your Battle Announcers list.
   PL: Po wybraniu otwiera listę komentatorów bojowych.
227. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_07_desc_02] — tekst] 전투 중에 사용할 아나운서를 변경할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_07_desc_02].content
   limit: do 120 znaków
   EN: You can choose which Battle Announcers to accompany you in battle.
   PL: Możesz zmienić komentatora towarzyszącego drużynie podczas walki.
228. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_08_title_01] — tekst] 편성 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_08_title_01].content
   limit: do 120 znaków
   EN: TEAMS
   PL: Lista składów
229. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_08_desc_01] — tekst] 제시된 키워드를 조합하여 편성 이름을 정합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_08_desc_01].content
   limit: do 120 znaków
   EN: Select from the list of keywords to choose a name for your Team.
   PL: Ustaw nazwę składu, łącząc dostępne słowa kluczowe.
230. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_08_desc_02] — tekst] 총 20개의 팀을 편성할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_08_desc_02].content
   limit: do 120 znaków
   EN: Preconfigure up to 20 Teams here.
   PL: Możesz zapisać łącznie do 20 składów.
231. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_09_title_01] — tekst] 편성 상세
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_09_title_01].content
   limit: do 120 znaków
   EN: Team Details
   PL: Szczegóły składu
232. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_09_desc_01] — tekst] 편성에 포함된 모든 인격이 보유한 스킬의 공격 유형, 죄악 속성과 장착 중인 E.G.O 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_09_desc_01].content
   limit: do 150 znaków
   EN: You can view the following information here: All Identities' Skill Attack Types, Sin Affinities, and equipped E.G.O.
   PL: Sprawdzisz tu typy ataków i Grzechy umiejętności wszystkich Tożsamości w składzie oraz listę wyposażonych E.G.O.
233. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_10_title_01] — tekst] E.G.O 자원
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_10_title_01].content
   limit: do 120 znaków
   EN: E.G.O Resources
   PL: Zasoby E.G.O
234. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_10_desc_01] — tekst] 팀이 전투에서 획득할 수 있는 E.G.O 자원의 종류와 수량을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_10_desc_01].content
   limit: do 120 znaków
   EN: Here, you can view the types and amounts of E.G.O Costs your team can gain in battle.
   PL: Pokazuje rodzaje oraz liczby zasobów E.G.O, które drużyna może zdobywać w walce.
235. [Samouczek i wskazówki [tutorial_mainui_01_selection_page_10_desc_02] — tekst] 터치 시, 선택한 E.G.O 자원을 수급하는 인격과 사용하는 E.G.O 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_01_selection_page_10_desc_02].content
   limit: do 120 znaków
   EN: Select it, and you can view Identities that gain the E.G.O Costs and E.G.O that use them.
   PL: Po dotknięciu wyświetla Tożsamości generujące wybrany zasób E.G.O oraz korzystające z niego E.G.O.
236. [Samouczek i wskazówki [tutorial_mainui_02_identityandegolist] — tekst] 인격 및 E.G.O 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identityandegolist].content
   limit: do 120 znaków
   EN: Identity and E.G.O Lists
   PL: Lista Tożsamości i E.G.O
237. [Samouczek i wskazówki [tutorial_mainui_02_identitylist] — tekst] 인격 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist].content
   limit: do 120 znaków
   EN: Identity List
   PL: Lista Tożsamości
238. [Samouczek i wskazówki [tutorial_mainui_02_egolist] — tekst] E.G.O 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_egolist].content
   limit: do 120 znaków
   EN: E.G.O List
   PL: Lista E.G.O
239. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_01_desc_01] — tekst] 편성에서 선택한 수감자의 인격 목록이 나열됩니다. 인격의 등급과 동기화 단계, 레벨, 소속을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_01_desc_01].content
   limit: do 140 znaków
   EN: Your Sinner’s Identities are shown here. You can check their Grades, Uptie Tiers, Levels, and Factions.
   PL: Wyświetla Tożsamości wybranego Grzesznika wraz z ich rzadkością, stopniem Synchronizacji, poziomem oraz przynależnością.
240. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_02_title_01] — tekst] 편성 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_02_title_01].content
   limit: do 120 znaków
   EN: Team Configuration
   PL: Aktualny ekwipunek
241. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_02_desc_01] — tekst] 편성 중인 인격과 E.G.O를 동시에 확인할 수 있습니다. E.G.O는 각 등급마다 하나씩 등록할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_02_desc_01].content
   limit: do 140 znaków
   EN: You can see both the Identities and E.G.O set for the team here. One E.G.O can be registered for each grade.
   PL: Pozwala jednocześnie przejrzeć wybraną Tożsamość oraz wyposażone E.G.O. Dla każdej rangi można przypisać jedno E.G.O.
242. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_03_title_01] — tekst] 편성 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_03_title_01].content
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_03_desc_01] — tekst] 편성 현황의 버튼 터치 시, 해당 칸에 등록할 수 있는 E.G.O 목록으로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_03_desc_01].content
   limit: do 120 znaków
   EN: Tapping this button brings you to the list of E.G.O that can be equipped on the slot.
   PL: Dotknięcie przycisku przełącza widok na listę E.G.O dostępnych dla danego gniazda.
244. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_04_desc_01] — tekst] E.G.O의 등급과 해석 단계, 주 속성, 이름을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_04_desc_01].content
   limit: do 120 znaków
   EN: You can view the E.G.O’s grade, Threadspin Tier, main attribute, and name.
   PL: Sprawdzisz tu rangę E.G.O, stopień Splotu Nici, główny Grzech oraz nazwę.
245. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_05_title_01] — tekst] 지원 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_05_title_01].content
   limit: do 120 znaków
   EN: Support List
   PL: Lista wsparcia
246. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_05_title_02] — tekst] 지원 목록 버튼
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_05_title_02].content
   limit: do 120 znaków
   EN: Support Button
   PL: Przycisk wsparcia
247. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_05_desc_01] — tekst] 선택 시, 친구의 지원 인격 목록을 표시합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_05_desc_01].content
   limit: do 120 znaków
   EN: Upon selection, a list of your friends’ support Identities is shown.
   PL: Po wybraniu wyświetla listę Tożsamości wsparcia udostępnionych przez znajomych.
248. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_05_desc_02] — tekst] 친구가 등록한 지원 인격의 목록과 E.G.O 등록 현황이 나열됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_05_desc_02].content
   limit: do 120 znaków
   EN: Support Identities and E.G.O registered by friends are shown here.
   PL: Pokazuje zarejestrowane przez znajomych Tożsamości wsparcia wraz z ich wyposażonym E.G.O.
249. [Samouczek i wskazówki [tutorial_mainui_02_identitylist_page_06_desc_01] — tekst] 친구의 인격과 E.G.O를 빌릴 수 있습니다. 단, 하나의 편성에 둘 이상의 친구 인격을 빌릴 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_02_identitylist_page_06_desc_01].content
   limit: do 170 znaków
   EN: You can borrow a friend’s Identity and E.G.O to assist you. Note that you may only have one support Identity on your team at a time.
   PL: Możesz wypożyczyć Tożsamość i E.G.O znajomego. W jednym składzie można korzystać maksymalnie z jednej Tożsamości wsparcia.
250. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo] — tekst] 인격 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo].content
   limit: do 120 znaków
   EN: Identity Info
   PL: Informacje o Tożsamości
251. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_01_title_01] — tekst] 레벨
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_01_title_01].content
   limit: do 120 znaków
   EN: Level
   PL: Poziom
252. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_01_desc_01] — tekst] 레벨이 높아질수록 인격이 스테이터스가 강화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_01_desc_01].content
   limit: do 120 znaków
   EN: Levelling up an Identity increases its stats.
   PL: Wraz ze wzrostem poziomu rosną statystyki Tożsamości.
253. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_01_title_02] — tekst] 동기화 단계
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_01_title_02].content
   limit: do 120 znaków
   EN: Uptie Tier
   PL: Stopień Synchronizacji
254. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_01_desc_02] — tekst] 동기화 단계가 높아질수록 스킬 효과가 강화되거나 새로운 스킬을 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_01_desc_02].content
   limit: do 120 znaków
   EN: Higher Uptie tiers will enhance existing Skills or unlock new Skills.
   PL: Wyższy stopień Synchronizacji wzmacnia efekty umiejętności lub odblokowuje nowe umiejętności.
255. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_02_title_01] — tekst] 스테이터스
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_02_title_01].content
   limit: do 120 znaków
   EN: Status
   PL: Statystyki
256. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_02_desc_01] — tekst] 인격의 체력, 속도 범위값, 방어 레벨과 보정치가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_02_desc_01].content
   limit: do 120 znaków
   EN: The Identity's Max HP, Speed Range, Defense Level and its modifier are displayed here.
   PL: Wyświetla maks. PŻ, przedział Szybkości oraz Poziom Obrony Tożsamości wraz z modyfikatorem.
257. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_02_title_02] — tekst] 내성 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_02_title_02].content
   limit: do 120 znaków
   EN: Resistances
   PL: Odporności
258. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_02_desc_02] — tekst] 인격의 내성 정보가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_02_desc_02].content
   limit: do 120 znaków
   EN: The Identity's Resistances are displayed here.
   PL: Wyświetla odporności Tożsamości.
259. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_03_title_01] — tekst] 인격 정보 요약
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_03_title_01].content
   limit: do 120 znaków
   EN: Identity Summary
   PL: Podsumowanie Tożsamości
260. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_03_desc_01] — tekst] 인격의 E.G.O 장착 현황과 보유 스킬을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_03_desc_01].content
   limit: do 120 znaków
   EN: The Identity's equipped E.G.O and unlocked Skills are displayed here.
   PL: Sprawdzisz tu wyposażone E.G.O oraz posiadane umiejętności Tożsamości.
261. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_04_title_01] — tekst] 스킬
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_04_title_01].content
   limit: do 120 znaków
   EN: Skills
   PL: Umiejętności
262. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_04_desc_01] — tekst] 인격은 저마다 다양한 스킬을 가지고 있습니다. 스킬에 대한 자세한 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_04_desc_01].content
   limit: do 120 znaków
   EN: Each Identity has Skills of various functions. You can view the details about them here.
   PL: Każda Tożsamość dysponuje odmiennym zestawem umiejętności — tutaj sprawdzisz ich szczegółowe opisy.
263. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_05_desc_01] — tekst] 전투에 참여한 인격은 패시브 스킬을 발동시킬 수 있습니다. 매 턴 시작 시 조건을 만족할 경우, 패시브 스킬이 발동합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_05_desc_01].content
   limit: do 180 znaków
   EN: Identities deployed in battle can activate their Passives. At the start of every turn, Passives will activate when their conditions are met.
   PL: Tożsamości biorące udział w walce mogą aktywować swoją pasywkę bojową na początku każdej tury po spełnieniu jej warunku.
264. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_06_desc_01] — tekst] 전투에 참여하지 않은 인격은 서포트 패시브 스킬을 발동시킬 수 있습니다. 매 턴 시작 시 조건을 만족할 경우, 서포트 패시브 스킬이 발동합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_06_desc_01].content
   limit: do 210 znaków
   EN: Identities not deployed in battle can activate their Support Passives. At the start of every turn, Support Passives will activate when their conditions are met.
   PL: Tożsamości niebiorące udziału w walce mogą aktywować swoją pasywkę wsparcia na początku każdej tury po spełnieniu jej warunku.
265. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_07_title_01] — tekst] 스킬 아이콘
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_07_title_01].content
   limit: do 120 znaków
   EN: Skill Icons
   PL: Ikona umiejętności
266. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_07_desc_01] — tekst] 스킬 아이콘 색상을 통해 죄악 속성을 알 수 있습니다. 죄악 속성은 각 색상에 따라 분노, 색욕, 나태, 탐식, 우울, 오만, 질투로 구분됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_07_desc_01].content
   limit: do 220 znaków
   EN: The color of each Skill Icon corresponds to a Sin Affinity of the same color. These are the following Sin Affinities: Wrath, Lust, Sloth, Gluttony, Gloom, Pride, and Envy.
   PL: Kolor ikony umiejętności określa jej Grzech: Gniew, Żądzę, Lenistwo, Obżarstwo, Posępność, Pychę lub Zawiść.
267. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_08_desc_01] — tekst] 스킬 아이콘 하단에는 공격 유형이 표시됩니다. 공격 유형은 각각 참격, 관통, 타격으로 구분합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_08_desc_01].content
   limit: do 150 znaków
   EN: On the bottom of a Skill Icon is its Attack Type. These are the following Attack Types: Slash, Pierce, and Blunt.
   PL: U dołu ikony umiejętności widnieje jej typ ataku: Cięcie, Kłucie lub Obuch.
268. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_08_desc_02] — tekst] 스킬 아이콘 좌측에는 스킬의 기본 위력이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_08_desc_02].content
   limit: do 120 znaków
   EN: On the left of a Skill Icon is its Base Power.
   PL: Po lewej stronie ikony umiejętności wyświetlana jest jej Moc Bazowa.
269. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_08_desc_03] — tekst] 스킬 아이콘 상단에는 코인 위력이 표시됩니다. 코인 위력의 연산 방식은 각각 더하기, 빼기, 곱하기로 구분합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_08_desc_03].content
   limit: do 160 znaków
   EN: On the top of a Skill Icon is its Coin Power. These are the following Coin Power calculations: Plus, Minus, and Multiply.
   PL: Nad ikoną umiejętności wyświetlana jest Moc Monety wraz ze sposobem działania: dodawaniem, odejmowaniem lub mnożeniem.
270. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_09_desc_01] — tekst] 스킬의 코인 수량이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_09_desc_01].content
   limit: do 120 znaków
   EN: The number of Coins for this Skill is displayed here.
   PL: Wskazuje liczbę monet danej umiejętności.
271. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_09_desc_02] — tekst] 스킬명과 인격이 보유한 해당 스킬의 수량이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_09_desc_02].content
   limit: do 120 znaków
   EN: This indicates how many copies of the Skill are in the Identity's Skillset.
   PL: Wskazuje nazwę umiejętności oraz liczbę jej kopii w zestawie Tożsamości.
272. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_09_desc_03] — tekst] 스킬의 공격 레벨과 보정치가 표시됩니다. 스킬의 공격 레벨과 피격자의 방어 레벨 간의 격차가 클수록 피해량이 크게 증가하거나 혹은 감소합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_09_desc_03].content
   limit: do 250 znaków
   EN: The Skill's Offense Level and its modifier are displayed here. The difference in the Attack Skill's Offense Level and the target's Defense Level can greatly affect the amount of damage dealt.
   PL: Wyświetla Poziom Ataku umiejętności wraz z modyfikatorem. Im większa różnica między Poziomem Ataku a Poziomem Obrony celu, tym mocniej rosną lub maleją zadawane obrażenia.
273. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_10_desc_01] — tekst] 스킬의 공격 가중치가 표시됩니다. 스킬의 공격 가중치만큼 적 슬롯 가중치에 대응하여 공격합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_10_desc_01].content
   limit: do 210 znaków
   EN: The Skill's Atk Weight is displayed here. Higher Atk Weight will target more enemies. (e.g. 1 Atk Weight will target 1 enemy, 3 Atk Weight will target 3 enemies)
   PL: Wyświetla Wagę Ataku umiejętności — atak obejmuje pola wrogów o łącznej wadze równej tej wartości.
274. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_11_title_01] — tekst] 스킬 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_11_title_01].content
   limit: do 120 znaków
   EN: Skill Effects
   PL: Efekty umiejętności
275. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_11_desc_01] — tekst] 조건을 만족할 경우 발동하는 스킬의 효과입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_11_desc_01].content
   limit: do 120 znaków
   EN: Skills may have effects that activate when the stated conditions are met.
   PL: Efekty umiejętności uruchamiane po spełnieniu określonych warunków.
276. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_11_title_02] — tekst] 코인별 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_11_title_02].content
   limit: do 120 znaków
   EN: Coin Effects
   PL: Efekty monet
277. [Samouczek i wskazówki [tutorial_mainui_03_identityinfo_page_11_desc_02] — tekst] 코인에 따른 조건을 만족할 경우 발동하는 스킬의 효과입니다. 판정에 실패한 코인의 효과는 발동되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_03_identityinfo_page_11_desc_02].content
   limit: do 220 znaków
   EN: Skills may have effects that activate when the stated Coin conditions(e.g. Heads Hit, Tails Hit) are met. Coin effects will not activate when the conditions aren't met.
   PL: Efekty przypisane do poszczególnych monet uruchamiane po spełnieniu ich warunków — nieudany rzut nie aktywuje danego efektu.
278. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo] — tekst] E.G.O 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo].content
   limit: do 120 znaków
   EN: E.G.O Info
   PL: Informacje o E.G.O
279. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_01_title_01] — tekst] 환상 해석 단계
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_01_title_01].content
   limit: do 120 znaków
   EN: Threadspin Tier
   PL: Stopień Splotu Nici
280. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_01_desc_01] — tekst] 환상 해석 단계가 높아질수록 스킬 효과가 강화됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_01_desc_01].content
   limit: do 120 znaków
   EN: Higher Threadspinning Tiers will enhance the E.G.O's Skills and abilities.
   PL: Wyższy stopień Splotu Nici wzmacnia efekty umiejętności E.G.O.
281. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_title_01] — tekst] 내성 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_title_01].content
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_desc_01] — tekst] E.G.O의 내성 정보가 표시됩니다. 인격이 E.G.O 스킬을 사용하였다면, 인격의 속성 내성은 해당 E.G.O의 속성 내성으로 교체됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_desc_01].content
   limit: do 200 znaków
   EN: The E.G.O's Resistances are displayed here. If an Identity has used an E.G.O Skill, its Resistances will be overwritten by the used E.G.O's Resistances.
   PL: Wyświetla odporności E.G.O. Gdy Tożsamość użyje umiejętności E.G.O, jej odporności na Grzechy zostają zastąpione odpornościami tego E.G.O.
283. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_title_02] — tekst] 정신 소모량
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_title_02].content
   limit: do 120 znaków
   EN: Sanity Cost
   PL: Koszt Poczytalności
284. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_desc_02] — tekst] E.G.O 스킬 사용 시 해당 수치만큼 정신력이 소모됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_desc_02].content
   limit: do 120 znaków
   EN: The amount of SP spent when using this E.G.O Skill is displayed here.
   PL: Wskazuje ilość Poczytalności zużywaną przy wyzwalaniu tej umiejętności E.G.O.
285. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_title_03] — tekst] E.G.O 자원 소모량
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_title_03].content
   limit: do 120 znaków
   EN: E.G.O Resource Cost
   PL: Koszt zasobów E.G.O
286. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_02_desc_03] — tekst] E.G.O 스킬 사용 시 표시된 수치만큼 E.G.O 자원이 소모됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_02_desc_03].content
   limit: do 120 znaków
   EN: E.G.O resources required to use this E.G.O Skill are displayed here.
   PL: Wskazuje liczbę zasobów E.G.O zużywanych przy wyzwalaniu tej umiejętności E.G.O.
287. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_03_title_01] — tekst] E.G.O 스킬
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_03_title_01].content
   limit: do 120 znaków
   EN: E.G.O Skills
   PL: Umiejętność E.G.O
288. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_03_desc_01] — tekst] E.G.O 스킬은 높은 위력과 강력한 스킬 효과를 가지고 있습니다. E.G.O 스킬에 대한 자세한 정보를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_03_desc_01].content
   limit: do 160 znaków
   EN: E.G.O Skills have high Base/Coin Power values and potent Skill effects. Details about the E.G.O Skill are displayed here.
   PL: Umiejętności E.G.O cechują się wysoką Mocą oraz potężnymi efektami. Tutaj sprawdzisz ich szczegółowe informacje.
289. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_04_desc_01] — tekst] 인격이 정신력이 낮은 상태에서 E.G.O 스킬을 사용하였을 때, 확률에 따라 E.G.O 침식 스킬이 되어 위력과 스킬 효과가 훨씬 강력해집니다.\n다만 피아식별을 할 수 없는 상태가 되어 아군을 공격할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_04_desc_01].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If an Identity with a low SP value uses an E.G.O Skill, there is a chance that a much more powerful E.G.O Corrosion Skill will be activated instead. Using E.G.O Corrosion Skills carries a risk, however, as it attacks indiscriminately and may target allies as well.
   PL: Gdy Tożsamość o niskiej Poczytalności użyje umiejętności E.G.O, istnieje szansa na wyzwolenie znacznie potężniejszej umiejętności Korozyjnej E.G.O.\nPostać traci wówczas zdolność odróżniania swoich od wrogów i może zaatakować sojuszników.
290. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_05_desc_01] — tekst] E.G.O 스킬을 생성할 때 E.G.O 자원과 정신력을 1.5배로 소모하여 E.G.O 침식 스킬을 강제로 사용할 수 있습니다. 이를 E.G.O 오버클록이라고 합니다.\n전투 중 E.G.O 선택 단계에서, E.G.O를 길게 터치하여 E.G.O 오버클록 기능을 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_05_desc_01].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can force activate an E.G.O Corrosion Skill by Overclocking, which consumes 1.5 times as many E.G.O Resources and SP as the E.G.O Skill's usual cost. This is called E.G.O Overclock.\nE.G.O Overclock can be activated by pressing and holding the E.G.O Card in the E.G.O Skill selection menu in combat.
   PL: Podczas generowania umiejętności E.G.O możesz zużyć 1,5-krotność zasobów E.G.O oraz Poczytalności, aby celowo wyzwolić umiejętność Korozyjną — nazywamy to Przeciążeniem E.G.O.\nW trakcie walki przytrzymaj kartę E.G.O w menu wyboru E.G.O, aby użyć Przeciążenia E.G.O.
291. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_05_desc_02] — tekst] 오버클록 기능을 사용하였을 때 E.G.O 자원이 충분한 상태라면, 안정 상태가 되어 피아식별이 가능한 안정화된 오버클록 E.G.O 스킬을 사용합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_05_desc_02].content
   limit: do 240 znaków
   EN: Stable E.G.O Overclock Skill will be activated if there are enough E.G.O Costs(1.5 times the usual cost) at hand. Stable E.G.O Overclock Skill is able to distinguish allies from foes.
   PL: Jeśli podczas Przeciążenia posiadasz wystarczającą ilość zasobów E.G.O, wyzwolisz Stabilne Przeciążenie E.G.O, które odróżnia sojuszników od wrogów.
292. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_05_desc_03] — tekst] 만약 E.G.O 자원이 부족한 상태라면, 불안정 상태가 되어 피아식별이 불가능한 불안정한 오버클록 E.G.O 스킬을 사용합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_05_desc_03].content
   limit: do 220 znaków
   EN: If there aren't enough E.G.O Costs at hand, Unstable E.G.O Overclock Skill will be activated instead. Unstable E.G.O Overclock Skill does not distinguish allies from foes.
   PL: Jeśli brakuje wymaganych zasobów E.G.O, wyzwolone zostanie Niestabilne Przeciążenie E.G.O, które nie odróżnia sojuszników od wrogów.
293. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_06_desc_01] — tekst] E.G.O 스킬 사용 시, E.G.O 패시브 효과가 발동합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_06_desc_01].content
   limit: do 120 znaków
   EN: Using an E.G.O Skill will activate the E.G.O's Passive.
   PL: Użycie umiejętności E.G.O aktywuje pasywkę danego E.G.O.
294. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_07_title_01] — tekst] 스킬 아이콘
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_07_title_01].content
   (powtórzenie elementu 265 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_07_desc_01] — tekst] 스킬 아이콘 색상을 통해 죄악 속성을 알 수 있습니다. 죄악 속성은 각 색상에 따라 분노, 색욕, 나태, 탐식, 우울, 오만, 질투로 구분됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_07_desc_01].content
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_08_desc_01] — tekst] 스킬 아이콘 하단에는 공격 유형이 표시됩니다. 공격 유형은 각각 참격, 관통, 타격으로 구분합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_08_desc_01].content
   (powtórzenie elementu 267 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_08_desc_02] — tekst] 스킬 아이콘 좌측에는 스킬의 기본 위력이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_08_desc_02].content
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_08_desc_03] — tekst] 스킬 아이콘 상단에는 코인 위력이 표시됩니다. 코인 위력의 연산 방식은 각각 더하기, 빼기, 곱하기로 구분합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_08_desc_03].content
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_09_desc_01] — tekst] 스킬의 코인 수량이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_09_desc_01].content
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_09_desc_02] — tekst] 스킬의 공격 레벨과 보정치가 표시됩니다. 스킬의 공격 레벨과 피격자의 방어 레벨 간의 격차가 클수록 피해량이 크게 증가하거나 혹은 감소합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_09_desc_02].content
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_09_desc_03] — tekst] 스킬의 공격 가중치가 표시됩니다. 스킬의 공격 가중치만큼 적 슬롯 가중치에 대응하여 공격합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_09_desc_03].content
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_10_title_01] — tekst] 스킬 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_10_title_01].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_10_desc_01] — tekst] 조건을 만족할 경우 발동하는 스킬의 효과입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_10_desc_01].content
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_10_title_02] — tekst] 코인별 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_10_title_02].content
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Samouczek i wskazówki [tutorial_mainui_04_egoinfo_page_10_desc_02] — tekst] 코인에 따른 조건을 만족할 경우 발동하는 스킬의 효과입니다. 판정에 실패한 코인의 효과는 발동되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_04_egoinfo_page_10_desc_02].content
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Samouczek i wskazówki [tutorial_mainui_05_storymain] — tekst] 주요 이야기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain].content
   limit: do 120 znaków
   EN: The Main Story
   PL: Główna Opowieść
307. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_01_title_01] — tekst] 장 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_01_title_01].content
   limit: do 120 znaków
   EN: Canto Select
   PL: Wybór Canto
308. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_01_desc_01] — tekst] 전투를 진행하며 감상한 주요 이야기를 다시 볼 수 있습니다. 이야기의 장을 선택합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can view past parts of the story here. Select a Canto.
   PL: Możesz tu ponownie obejrzeć poznane rozdziały Głównej Opowieści. Wybierz Canto.
309. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_02_title_01] — tekst] 주요 이야기 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_02_title_01].content
   limit: do 120 znaków
   EN: Story Timeline
   PL: Lista odcinków
310. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_02_desc_01] — tekst] 이야기를 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_02_desc_01].content
   limit: do 120 znaków
   EN: Choose the scene you’d like to view.
   PL: Wybierz epizod, aby go odtworzyć.
311. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_03_title_01] — tekst] 주요 이야기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_03_title_01].content
   limit: do 120 znaków
   EN: Place in the Story
   PL: Miejsce w fabule
312. [Samouczek i wskazówki [tutorial_mainui_05_storymain_page_03_desc_01] — tekst] 선택한 스토리가 등장한 스테이지를 알 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_05_storymain_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can also check what stage the scene originally played in.
   PL: Sprawdzisz tu etap, na którym pierwotnie rozegrała się wybrana scena.
313. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity] — tekst] 인격 이야기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity].content
   limit: do 120 znaków
   EN: Identity Stories
   PL: Historie Tożsamości
314. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_01_title_01] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_01_title_01].content
   limit: do 120 znaków
   EN: Selecting a Sinner
   PL: Wybór Grzesznika
315. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_01_desc_01] — tekst] 림버스 수감자의 이야기나 정보를 볼 수 있습니다. 수감자를 선택합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can read up on the profiles and stories of your Sinners. Select a Sinner.
   PL: Możesz tu zapoznać się z historiami oraz profilami Grzeszników Limbus Company. Wybierz Grzesznika.
316. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_02_title_01] — tekst] 인격 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_02_title_01].content
   limit: do 120 znaków
   EN: Selecting Identities
   PL: Wybór Tożsamości
317. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_02_desc_01] — tekst] 선택한 수감자의 인격이 나열됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_02_desc_01].content
   limit: do 120 znaków
   EN: You can select from the Sinner’s listed Identities.
   PL: Wyświetla listę Tożsamości wybranego Grzesznika.
318. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_03_title_01] — tekst] 인격 이야기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_03_title_01].content
   limit: do 120 znaków
   EN: Identity Story
   PL: Historia Tożsamości
319. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_03_desc_01] — tekst] 인격의 이야기를 감상합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can read the Identity’s story here.
   PL: Odtwarza historię wybranej Tożsamości.
320. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_04_title_01] — tekst] 대사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_04_title_01].content
   limit: do 120 znaków
   EN: Voice Lines
   PL: Kwestie głosowe
321. [Samouczek i wskazówki [tutorial_mainui_06_storyidentity_page_04_desc_01] — tekst] 인격의 대사를 보거나 이야기를 들을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_06_storyidentity_page_04_desc_01].content
   limit: do 120 znaków
   EN: You can view the Identity’s lines or their story.
   PL: Możesz tu przejrzeć kwestie Tożsamości oraz odsłuchać jej historię.
322. [Samouczek i wskazówki [tutorial_mainui_07_storymirror] — tekst] 거울 세계들
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror].content
   limit: do 120 znaków
   EN: Mirror Worlds
   PL: Światy Lustrzane
323. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_01_title_01] — tekst] 거울 세계들
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_01_title_01].content
   (powtórzenie elementu 322 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_01_desc_01] — tekst] 선택 시, 거울 세계들이 나열된 목록으로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_01_desc_01].content
   limit: do 120 znaków
   EN: Upon selection, you’ll be taken to the list of Mirror Worlds.
   PL: Po wybraniu przełącza widok na listę Światów Lustrzanych.
325. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_01_title_02] — tekst] 거울 세계들 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_01_title_02].content
   limit: do 120 znaków
   EN: Organization
   PL: Lista Światów Lustrzanych
326. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_01_desc_02] — tekst] 거울 세계들에서는 다양한 인격 이야기를 각각의 거울 세계에 따라 분류합니다. 다양한 거울 세계와 각 거울 세계에서 등장하는 소속 단체를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_01_desc_02].content
   limit: do 240 znaków
   EN: In the Mirror Worlds, the various Identity stories are categorized in accordance with the reflection they come from. You can check each Mirror World and the factions that appear in it.
   PL: W zakładce Światów Lustrzanych historie poszczególnych Tożsamości są pogrupowane według światów, z których pochodzą. Sprawdzisz tu poszczególne Światy Lustrzane oraz występujące w nich frakcje.
327. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_02_title_01] — tekst] 인격 이야기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_02_title_01].content
   limit: do 120 znaków
   EN: Tales from the Mirror
   PL: Historie Tożsamości
328. [Samouczek i wskazówki [tutorial_mainui_07_storymirror_page_02_desc_01] — tekst] 거울 세계를 기준으로 한 인격 이야기를 감상합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_07_storymirror_page_02_desc_01].content
   limit: do 120 znaków
   EN: Read each Identity’s story based on the Mirror World.
   PL: Pozwala przeglądać historie Tożsamości przypisane do danego Świata Lustrzanego.
329. [Samouczek i wskazówki [tutorial_mainui_08_stagemain] — tekst] 메인 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain].content
   limit: do 120 znaków
   EN: Main Stages
   PL: Etapy główne
330. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_01_title_01] — tekst] 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_01_title_01].content
   limit: do 120 znaków
   EN: Stage
   PL: Etap
331. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_01_desc_01] — tekst] 스테이지를 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_01_desc_01].content
   limit: do 120 znaków
   EN: You choose a stage to enter.
   PL: Wybierz etap, aby na niego wejść.
332. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_02_desc_01] — tekst] 전투에서 승리하면 클리어 표시가 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_02_desc_01].content
   limit: do 120 znaków
   EN: After you’ve won the battle, the stage will be marked as cleared.
   PL: Po wygranej walce etap zostaje oznaczony jako ukończony.
333. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_02_desc_02] — tekst] EX 클리어 조건을 달성하여 승리하면 EX 클리어 표시가 되고 추가 보상을 획득합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_02_desc_02].content
   limit: do 130 znaków
   EN: If you clear the EX Objectives, you’ll earn bonus rewards, and the stage will be marked accordingly.
   PL: Zwycięstwo przy spełnieniu warunku EX oznacza etap jako ukończony na EX i zapewnia dodatkową nagrodę.
334. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_title_01] — tekst] 스테이지 스토리
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_title_01].content
   limit: do 120 znaków
   EN: Stage Story
   PL: Fabuła etapu
335. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_desc_01] — tekst] 선택한 스테이지에 등장하는 이야기를 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can rewatch the story scenes featured in the stage as well.
   PL: Pozwala obejrzeć sceny fabularne występujące na wybranym etapie.
336. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_title_02] — tekst] 스테이지 설명
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_title_02].content
   limit: do 120 znaków
   EN: Stage Description
   PL: Opis etapu
337. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_desc_02] — tekst] 등장하는 이야기와 스테이지에 대한 설명을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_desc_02].content
   limit: do 120 znaków
   EN: You can view the blurb and description for the stage here.
   PL: Sprawdzisz tu streszczenie i opis wybranego etapu.
338. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_title_03] — tekst] 적 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_title_03].content
   limit: do 120 znaków
   EN: Enemy Info
   PL: Informacje o wrogach
339. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_03_desc_03] — tekst] 적에 대한 다양한 정보를 파악할 수 있습니다. 일부 강력한 적들은 직접 조우한 이후부터 그 정보를 확인할 수 있게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_03_desc_03].content
   limit: do 170 znaków
   EN: You can read up on the enemies that appear. Information on certain powerful enemies will only be available after encountering them.
   PL: Pozwala przejrzeć dane o przeciwnikach. Informacje o niektórych potężnych wrogach stają się widoczne dopiero po bezpośrednim starciu z nimi.
340. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_04_title_01] — tekst] EX 클리어 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_04_title_01].content
   limit: do 120 znaków
   EN: EX Objectives
   PL: Warunek EX
341. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_04_desc_01] — tekst] EX 클리어를 달성하기 위한 조건이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_04_desc_01].content
   limit: do 120 znaków
   EN: EX Objectives are displayed here.
   PL: Wyświetla warunek wymagany do ukończenia etapu z oceną EX.
342. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_04_title_02] — tekst] 입장
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_04_title_02].content
   limit: do 120 znaków
   EN: Stage Entry
   PL: Wejście
343. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_04_desc_02] — tekst] 전투 스테이지에 입장할 때 엔케팔린을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_04_desc_02].content
   limit: do 120 znaków
   EN: Entering battle stages costs Enkephalin.
   PL: Wejście na etap bojowy zużywa Enkefalinę.
344. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_05_title_01] — tekst] 전투 참가 가능 수
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_05_title_01].content
   limit: do 120 znaków
   EN: Participant Limit
   PL: Limit uczestników
345. [Samouczek i wskazówki [tutorial_mainui_08_stagemain_page_05_desc_01] — tekst] 각 스테이지는 최대로 참여할 수 있는 인원 수 제한이 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_08_stagemain_page_05_desc_01].content
   limit: do 120 znaków
   EN: Each stage has a limit to the number of participants.
   PL: Każdy etap ma określoną maksymalną liczbę uczestników walki.
346. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon] — tekst] 스토리 던전
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon].content
   limit: do 120 znaków
   EN: Story Dungeons
   PL: Lochy Fabularne
347. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_01_title_01] — tekst] 스토리 던전 정보 창
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_01_title_01].content
   limit: do 120 znaków
   EN: Dungeon Info Tab
   PL: Informacje o Lochu Fabularnym
348. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_01_desc_01] — tekst] 각 장의 마지막에는 던전이 등장할 수 있습니다. 던전은 입장 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_01_desc_01].content
   limit: do 130 znaków
   EN: A dungeon may await at the tail end of each Episode. Entering dungeons costs Enkephalin Modules.
   PL: W finale rozdziału może pojawić się loch. Wejście do lochu zużywa Moduły Enkefaliny.
349. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_02_title_01] — tekst] 던전 탐사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_02_title_01].content
   limit: do 120 znaków
   EN: Dungeon Exploration
   PL: Eksploracja lochu
350. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_02_desc_01] — tekst] 현재 방에서 연결된 방을 선택하며 진행할 수 있습니다. 각 방에서는 다양한 종류의 전투와 이벤트가 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_02_desc_01].content
   limit: do 180 znaków
   EN: You proceed by moving to spaces adjacent to your location. You may find encounters with various foes and also events with consequences.
   PL: Poruszasz się naprzód, wybierając sąsiednie węzły połączone z bieżącym pomieszczeniem. W kolejnych komnatach czekają rozmaite walki oraz wydarzenia.
351. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_03_title_01] — tekst] 수감자 체력 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_03_title_01].content
   limit: do 120 znaków
   EN: Sinner Health
   PL: Stan PŻ Grzeszników
352. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_03_desc_01] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_03_desc_01].content
   limit: do 120 znaków
   EN: The HP, SP, and lost lives of your Sinners will carry over between encounters.
   PL: Podczas eksploracji lochu PŻ, Poczytalność oraz zgony Grzeszników przechodzą między kolejnymi walkami.
353. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_03_title_02] — tekst] 세이브 포인트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_03_title_02].content
   limit: do 120 znaków
   EN: Checkpoints
   PL: Punkty zapisu
354. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_03_desc_02] — tekst] 세이브 포인트에 도달하면 모든 수감자들의 체력과 정신력이 회복됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_03_desc_02].content
   limit: do 120 znaków
   EN: When you reach a checkpoint, your Sinners will be fully healed.
   PL: Dotarcie do punktu zapisu odnawia PŻ i Poczytalność wszystkich Grzeszników.
355. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_04_title_01] — tekst] E.G.O 기프트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_04_title_01].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
356. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_04_desc_01] — tekst] 던전을 진행하며 E.G.O 기프트를 획득합니다. E.G.O 기프트는 획득한 던전 안에서만 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_04_desc_01].content
   limit: do 180 znaków
   EN: As you explore the dungeon, you may acquire E.G.O Gifts; these items offer powerful effects that last until the end of the exploration.
   PL: W trakcie eksploracji lochu zdobywasz Dary E.G.O — przedmioty zapewniające potężne efekty obowiązujące wyłącznie wewnątrz danego lochu.
357. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_04_title_02] — tekst] 다음 층
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_04_title_02].content
   limit: do 120 znaków
   EN: Descending Floors
   PL: Następne piętro
358. [Samouczek i wskazówki [tutorial_mainui_09_stagedungeon_page_04_desc_02] — tekst] 던전은 여러 층으로 구성되어 있으며, 현재 층의 마지막 방을 클리어하면 다음 층으로 넘어갈 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_09_stagedungeon_page_04_desc_02].content
   limit: do 140 znaków
   EN: A dungeon consists of multiple floors. You may proceed down after securing the space containing stairs.
   PL: Loch składa się z wielu pięter; ukończenie ostatniej komnaty bieżącego piętra pozwala zejść na kolejne.
359. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon] — tekst] 거울 던전
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon].content
   limit: do 120 znaków
   EN: Mirror Dungeons
   PL: Lustrzane Lochy
360. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_01_title_01] — tekst] 거울 던전 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_01_title_01].content
   limit: do 120 znaków
   EN: Mirror Dungeons List
   PL: Lista Lustrzanych Lochów
361. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_01_desc_01] — tekst] 다양한 거울 던전 중 하나를 선택하여 입장합니다. 거울던전에서는 보상 수령 시 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_01_desc_01].content
   limit: do 160 znaków
   EN: You can choose one of the various Mirror Dungeons to enter. Claiming Mirror Dungeon Rewards costs Enkephalin Modules.
   PL: Wybierz jeden z dostępnych Lustrzanych Lochów, aby rozpocząć wyprawę. Odebranie nagród wymaga zużycia Modułów Enkefaliny.
362. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_02_title_01] — tekst] E.G.O 기프트 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_02_title_01].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
363. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_02_desc_01] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다. 일부 E.G.O 기프트는 특별한 해금 조건이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_02_desc_01].content
   limit: do 190 znaków
   EN: You can check the list of E.G.O Gifts that appear in the Mirror Dungeon. Certain E.G.O Gifts need to be unlocked by fulfilling specific conditions.
   PL: Sprawdzisz tu Dary E.G.O pojawiające się w Lustrzanych Lochach. Niektóre z nich wymagają spełnienia specjalnych warunków odblokowania.
364. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_03_title_01] — tekst] 최초 E.G.O 기프트 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_03_title_01].content
   limit: do 120 znaków
   EN: Starting E.G.O Gift
   PL: Wybór początkowego Daru E.G.O
365. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_03_desc_01] — tekst] 거울 던전 입장 시, E.G.O 기프트가 무작위로 제시됩니다. 이 중 하나를 선택하여 거울 던전을 진행하는 동안 특별한 효과를 누릴 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_03_desc_01].content
   limit: do 180 znaków
   EN: When you enter a Mirror Dungeon, you’ll be offered a random selection of E.G.O Gifts to help the exploration. Choose one to take with you.
   PL: Przy wejściu do Lustrzanego Lochu losowane są początkowe Dary E.G.O — wybierz jeden, by korzystać z jego efektu przez całą wyprawę.
366. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_04_title_01] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_04_title_01].content
   limit: do 120 znaków
   EN: Selecting Sinners
   PL: Wybór Grzeszników
367. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_04_desc_01] — tekst] 모든 수감자 중에서 셋을 선택하여 팀을 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_04_desc_01].content
   limit: do 120 znaków
   EN: Make a team of three Sinners to carry out the exploration.
   PL: Wybierz troje Grzeszników spośród całej dwunastki, aby utworzyć początkowy skład.
368. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_05_title_01] — tekst] 인격 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_05_title_01].content
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_05_desc_01] — tekst] 선택한 수감자의 인격을 편성합니다. 거울 던전에서는 별도의 강화 단계가 적용되며, 모든 인격은 첫 편성 단계에서 레벨이 10으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_05_desc_01].content
   limit: do 170 znaków
   EN: Select Identities for the Sinners. In Mirror Dungeons, all Identities start at Level 10, and can be powered up as you progress.
   PL: Wybierz Tożsamości dla wskazanych Grzeszników. W tym Lustrzanym Lochu obowiązuje odrębny rozwój, a wszystkie Tożsamości zaczynają na 10. poziomie.
370. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_06_title_01] — tekst] E.G.O 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_06_title_01].content
   limit: do 120 znaków
   EN: Selecting E.G.O
   PL: Wybór E.G.O
371. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_06_desc_01] — tekst] 선택한 수감자의 E.G.O를 편성합니다. 첫 편성 단계에선 ZAYIN급 E.G.O만 선택할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_06_desc_01].content
   limit: do 130 znaków
   EN: Choose E.G.O for your Sinners to equip. You can only select ZAYIN-grade E.G.O during deployment.
   PL: Przypisz E.G.O wybranym Grzesznikom. Na etapie początkowego składu dostępne są wyłącznie E.G.O rangi ZAYIN.
372. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_07_title_01] — tekst] 거울 던전 탐사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_07_title_01].content
   limit: do 120 znaków
   EN: Exploring Mirror Dungeons
   PL: Eksploracja Lustrzanego Lochu
373. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_07_desc_01] — tekst] 거울 던전에 입장할 때마다 방과 경로가 무작위로 생성됩니다. 현재 방에서 연결된 방을 선택해 진행하며, 각 방에선 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_07_desc_01].content
   limit: do 270 znaków
   EN: The layouts and paths in Mirror Dungeons are randomly generated each time you enter. Proceed by moving to one of the adjacent spaces in the next sector, and deal with the encounters and events waiting for you.
   PL: Przy każdym wejściu do Lustrzanego Lochu układ komnat i ścieżek jest generowany losowo. Przemieszczaj się do połączonych węzłów, stawiając czoła losowym walkom i wydarzeniom.
374. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_08_title_01] — tekst] E.G.O 기프트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_08_title_01].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_08_desc_01] — tekst] 던전을 진행하며 E.G.O 기프트를 획득합니다. E.G.O 기프트는 획득한 던전 안에서만 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_08_desc_01].content
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_08_title_02] — tekst] 수감자 체력 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_08_title_02].content
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_08_desc_02] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_08_desc_02].content
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_09_title_01] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_09_title_01].content
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_09_desc_01] — tekst] 일부 이벤트를 통해 수감자를 팀에 추가로 편성하여 늘려나갈 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_09_desc_01].content
   limit: do 120 znaków
   EN: Certain events allow you to add more Sinners to your team.
   PL: Niektóre wydarzenia pozwalają zwerbować kolejnych Grzeszników do drużyny.
380. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_09_title_02] — tekst] 성장
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_09_title_02].content
   limit: do 120 znaków
   EN: Powering Up
   PL: Rozwój
381. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_09_desc_02] — tekst] 거울 던전에서는 별도의 강화 단계가 적용됩니다. 전투나 이벤트를 통해 레벨을 올리고 E.G.O를 추가로 장착할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_09_desc_02].content
   limit: do 180 znaków
   EN: In Mirror Dungeons, Identities power up in steps as you progress. Level up and equip more E.G.O through combat encounters and events.
   PL: W tym Lustrzanym Lochu obowiązuje odrębny system wzmocnień — poprzez walki i wydarzenia podnosisz poziomy oraz odblokowujesz kolejne gniazda E.G.O.
382. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_10_title_01] — tekst] 거울 던전 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_10_title_01].content
   limit: do 120 znaków
   EN: Mirror Dungeon Rewards
   PL: Nagrody Lustrzanego Lochu
383. [Samouczek i wskazówki [tutorial_mainui_10_mirrordungeon_page_10_desc_01] — tekst] 던전 클리어 시 보상을 획득할 수 있으며, 매주 일정 횟수만큼 추가 보상을 얻을 수 있습니다. 보상 수량은 클리어한 방의 수에 비례하여 지급됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_10_mirrordungeon_page_10_desc_01].content
   limit: do 230 znaków
   EN: You’ll be rewarded upon clearing the dungeon, and a bonus will be given for a set number of times each week. The amount of rewards is proportional to the number of spaces cleared.
   PL: Za ukończenie lochu otrzymujesz nagrody oraz cotygodniową pulę premii dodatkowych. Wielkość nagród zależy od liczby ukończonych węzłów.
384. [Samouczek i wskazówki [tutorial_mainui_11_extraction] — tekst] 추출
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction].content
   limit: do 120 znaków
   EN: Extractions
   PL: Ekstrakcja
385. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_01_title_01] — tekst] 추출 종류
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_01_title_01].content
   limit: do 120 znaków
   EN: Category
   PL: Rodzaj Ekstrakcji
386. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_01_desc_01] — tekst] 상시 또는 픽업 중 원하는 추출을 선택하여 진행할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_01_desc_01].content
   limit: do 120 znaków
   EN: You may choose between Standard and Target Extractions.
   PL: Możesz wybierać pomiędzy Ekstrakcją standardową a celowaną.
387. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_01_title_02] — tekst] 추출
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_01_title_02].content
   limit: do 120 znaków
   EN: Extraction
   PL: Ekstrakcja
388. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_01_desc_02] — tekst] 광기를 통해 인격 또는 E.G.O를 추출할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_01_desc_02].content
   limit: do 120 znaków
   EN: You can spend Lunacy to extract Identities or E.G.O.
   PL: Wydając Szaleństwo, możesz ekstrahować Tożsamości oraz E.G.O.
389. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_02_title_01] — tekst] 픽업 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_02_title_01].content
   limit: do 120 znaków
   EN: Target Period
   PL: Czas trwania
390. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_02_desc_01] — tekst] 픽업 기간을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_02_desc_01].content
   limit: do 120 znaków
   EN: You can see how long the limited Extraction banner will last.
   PL: Sprawdzisz tu czas trwania danej Ekstrakcji celowanej.
391. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_02_title_02] — tekst] 픽업 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_02_title_02].content
   limit: do 120 znaków
   EN: Featured Target
   PL: Wyróżnione cele
392. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_02_desc_02] — tekst] 픽업 인격 또는 E.G.O의 상세 정보를 확인합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_02_desc_02].content
   limit: do 120 znaków
   EN: View details on the featured Identity or E.G.O here.
   PL: Pozwala sprawdzić szczegóły wyróżnionej Tożsamości lub E.G.O.
393. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_03_title_01] — tekst] 추출 이력
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_03_title_01].content
   limit: do 120 znaków
   EN: Extraction History
   PL: Historia Ekstrakcji
394. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_03_desc_01] — tekst] 추출을 진행한 이력을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can view records of your previous Extractions here.
   PL: Sprawdzisz tu zapis dotychczas przeprowadzonych Ekstrakcji.
395. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_03_title_02] — tekst] 확률 상세 보기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_03_title_02].content
   limit: do 120 znaków
   EN: Rate Info
   PL: Szczegóły szans
396. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_03_desc_02] — tekst] 픽업 인격 또는 E.G.O의 획득 확률을 알 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_03_desc_02].content
   limit: do 120 znaków
   EN: You can view the likelihood of the featured Identity or E.G.O being extracted.
   PL: Pokazuje prawdopodobieństwo uzyskania wyróżnionej Tożsamości lub E.G.O.
397. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_04_title_01] — tekst] 자아 파편
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_04_title_01].content
   limit: do 120 znaków
   EN: Egoshards
   PL: Odłamki E.G.O
398. [Samouczek i wskazówki [tutorial_mainui_11_extraction_page_04_desc_01] — tekst] 이미 보유한 인격을 획득하게 되면 등급에 비례하여 자아 파편을 얻게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_11_extraction_page_04_desc_01].content
   limit: do 120 znaków
   EN: When you get an Identity you already own, you’ll receive Egoshards based on its rarity.
   PL: Wylosowanie posiadanej już Tożsamości zapewnia Odłamki E.G.O w liczbie zależnej od jej rzadkości.
399. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine] — tekst] 자판기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine].content
   limit: do 120 znaków
   EN: Dispenser
   PL: Automat
400. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_01_title_01] — tekst] 자판기 상품 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_01_title_01].content
   limit: do 120 znaków
   EN: Dispenser Catalogue
   PL: Oferta Automatu
401. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_01_desc_01] — tekst] 자아 파편을 사용하여 보유하지 않은 인격이나 E.G.O를 구입합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can exchange Egoshards for Identities or E.G.O you don’t yet own.
   PL: Wymieniaj Odłamki E.G.O na nieposiadane jeszcze Tożsamości oraz E.G.O.
402. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_02_title_01] — tekst] 자판기 종류
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_02_title_01].content
   limit: do 120 znaków
   EN: Dispenser Types
   PL: Kategorie Automatu
403. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_02_desc_01] — tekst] 상시 또는 원하는 시즌의 인격이나 E.G.O를 구입할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_02_desc_01].content
   limit: do 130 znaków
   EN: You can purchase permanently available Identities and E.G.O, as well as those from past seasons.
   PL: Możesz nabywać pozycje dostępne stale lub należące do wybranego sezonu.
404. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_03_title_01] — tekst] 자판기 상품 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_03_title_01].content
   limit: do 120 znaków
   EN: Choosing Items to Buy
   PL: Wybór pozycji w Automacie
405. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_03_desc_01] — tekst] 인격 또는 E.G.O를 구입하기 위해서는 해당 수감자의 자아 파편이 필요합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_03_desc_01].content
   limit: do 120 znaków
   EN: To buy Identities or E.G.O from here, you will need Egoshards of the Sinner.
   PL: Aby nabyć Tożsamość lub E.G.O, potrzebujesz Odłamków E.G.O odpowiadającego im Grzesznika.
406. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_04_title_01] — tekst] 끈 구매
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_04_title_01].content
   limit: do 120 znaków
   EN: Thread Exchange
   PL: Wymiana na Nić
407. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_04_desc_01] — tekst] 수감자의 자아 파편으로 끈을 구매할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_04_desc_01].content
   limit: do 120 znaków
   EN: Egoshards can also be exchanged for Thread.
   PL: Odłamki E.G.O Grzeszników można również wymieniać na Nić.
408. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_04_title_02] — tekst] 끈
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_04_title_02].content
   limit: do 120 znaków
   EN: Thread
   PL: Nić
409. [Samouczek i wskazówki [tutorial_mainui_12_vendingmachine_page_04_desc_02] — tekst] 끈은 인격의 동기화나 E.G.O의 환상 해석에 사용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_12_vendingmachine_page_04_desc_02].content
   limit: do 120 znaków
   EN: Thread is used for the Uptying of Identities and Threadspinning of E.G.O.
   PL: Nić służy do Synchronizacji Tożsamości oraz Splotu Nici E.G.O.
410. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_manager] — tekst] 관리자
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_manager].content
   limit: do 120 znaków
   EN: Manager Info
   PL: Kierownik
411. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_01_title_01] — tekst] 유저 정보 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_01_title_01].content
   limit: do 120 znaków
   EN: User Info
   PL: Zakładki profilu
412. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_01_desc_01] — tekst] 유저 정보와 지원 캐릭터, 친구 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can check your user info, list of support characters, and the friend list here.
   PL: Sprawdzisz tu profil użytkownika, postacie wsparcia oraz listę znajomych.
413. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_02_title_01] — tekst] 유저 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_02_title_01].content
   limit: do 120 znaków
   EN: User Info
   PL: Profil użytkownika
414. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_02_desc_01] — tekst] 유저 ID와 계정 레벨을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_02_desc_01].content
   limit: do 120 znaków
   EN: The User ID (UID) and account level are shown here.
   PL: Wyświetla identyfikator użytkownika (UID) oraz poziom konta.
415. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_02_title_02] — tekst] 장식 배너
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_02_title_02].content
   limit: do 120 znaków
   EN: Banner
   PL: Sztandar ozdobny
416. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_02_desc_02] — tekst] 장식 배너를 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_02_desc_02].content
   limit: do 120 znaków
   EN: You can configure your decorative banners.
   PL: Pozwala ustawić sztandar ozdobny profilu.
417. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_03_title_01] — tekst] 대표 수감자 설정
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_03_title_01].content
   limit: do 120 znaków
   EN: Face of the Company
   PL: Wyróżniony Grzesznik
418. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_03_desc_01] — tekst] 보유하고 있는 수감자 중에서 대표 수감자 일러스트를 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_03_desc_01].content
   limit: do 120 znaków
   EN: You can choose artwork to display from the Sinners in your possession.
   PL: Pozwala wybrać ilustrację wyróżnionego Grzesznika spośród posiadanych kart.
419. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_04_title_01] — tekst] 일러스트 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_04_title_01].content
   limit: do 120 znaków
   EN: Art List
   PL: Lista ilustracji
420. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_04_desc_01] — tekst] 보유한 인격, EGO 일러스트를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_04_desc_01].content
   limit: do 120 znaków
   EN: You can check the artwork of the Identities and E.G.O you own.
   PL: Przejrzysz tu ilustracje posiadanych Tożsamości oraz E.G.O.
421. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_05_title_01] — tekst] 인사말
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_05_title_01].content
   limit: do 120 znaków
   EN: Introduction
   PL: Wizytówka
422. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_05_desc_01] — tekst] 정해져 있는 단어를 조합해 자신만의 인사말을 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_05_desc_01].content
   limit: do 120 znaków
   EN: Use a combination of given words and phrases to make your introduction.
   PL: Ułóż własne hasło powitalne z dostępnych słów i zwrotów.
423. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_06_title_01] — tekst] 인사말 설정
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_06_title_01].content
   limit: do 120 znaków
   EN: Making an Intro
   PL: Edycja wizytówki
424. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_06_desc_01] — tekst] 문장과 단어를 정해 인사말을 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_06_desc_01].content
   limit: do 120 znaków
   EN: Choose from a given list of phrases and words to make your introduction.
   PL: Wybierz szablon zdania oraz słowa, aby skonfigurować wizytówkę.
425. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_company] — tekst] 회사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_company].content
   limit: do 120 znaków
   EN: Company
   PL: Firma
426. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_07_title_01] — tekst] 지원 인격 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_07_title_01].content
   limit: do 120 znaków
   EN: Support Identities
   PL: Tożsamości wsparcia
427. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_07_desc_01] — tekst] 지원 보내는 인격과 에고를 설정할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_07_desc_01].content
   limit: do 120 znaków
   EN: You can assign support Identities and E.G.O to assist others.
   PL: Pozwala przypisać Tożsamości oraz E.G.O udostępniane znajomym jako wsparcie.
428. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_friend] — tekst] 친구
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_friend].content
   limit: do 120 znaków
   EN: Friends
   PL: Znajomi
429. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_08_title_01] — tekst] 친구 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_08_title_01].content
   limit: do 120 znaków
   EN: Friends List
   PL: Lista znajomych
430. [Samouczek i wskazówki [tutorial_mainui_13_userinfo_page_08_desc_01] — tekst] 친구의 ID, 배너, 인사말, 접속일 확인 및 친구 추가를 할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_13_userinfo_page_08_desc_01].content
   limit: do 140 znaków
   EN: You can check your friends’ IDs, banners, introductions, and log-in times; plus, add users as friends!
   PL: Sprawdzisz tu UID, sztandary, wizytówki i czas ostatniego logowania znajomych oraz dodasz nowych graczy.
431. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_title] — tekst] 배틀 패스
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_title].content
   limit: do 120 znaków
   EN: Battle Pass
   PL: Przepustka Bitewna
432. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_01_title_01] — tekst] 배틀 패스 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_01_title_01].content
   limit: do 120 znaków
   EN: Battle Pass Rewards
   PL: Nagrody Przepustki Bitewnej
433. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_01_desc_01] — tekst] 배틀 패스 레벨별 무료 혹은 림버스 패스에 해당하는 보상을 확인하고 받을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_01_desc_01].content
   limit: do 120 znaków
   EN: You can check and redeem level rewards for the free battle pass and the Limbus Pass.
   PL: Pozwala przeglądać i odbierać nagrody darmowej ścieżki oraz Przepustki Limbus za kolejne poziomy.
434. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_02_title_01] — tekst] 배틀 패스 기간 및 이름
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_02_title_01].content
   limit: do 120 znaków
   EN: Pass Period and Name
   PL: Okres i nazwa Przepustki
435. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_02_desc_01] — tekst] 배틀 패스 기간과 시즌 이름을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_02_desc_01].content
   limit: do 120 znaków
   EN: You can check the title of the battle pass and its period.
   PL: Sprawdzisz tu czas trwania Przepustki Bitewnej oraz nazwę bieżącego sezonu.
436. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_02_title_02] — tekst] 배틀 패스 레벨 및 진행도
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_02_title_02].content
   limit: do 120 znaków
   EN: Pass Level and Progress
   PL: Poziom i postęp Przepustki
437. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_02_desc_02] — tekst] 배틀 패스 레벨과 진행도를 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_02_desc_02].content
   limit: do 120 znaków
   EN: You can check your battle pass level and progress here.
   PL: Wyświetla aktualny poziom oraz postęp Przepustki Bitewnej.
438. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_03_title_01] — tekst] 패스 미션 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_03_title_01].content
   limit: do 120 znaków
   EN: Battle Pass Missions
   PL: Misje Przepustki
439. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_03_desc_01] — tekst] 달성 시 배틀 패스 진행도를 얻을 수 있는 미션 목록입니다. 일일, 주간, 시즌 미션으로 분류됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_03_desc_01].content
   limit: do 190 znaków
   EN: This shows the list of missions that reward you with battle pass progression upon completion. There are daily, weekly, and seasonal missions.
   PL: Lista misji zapewniających punkty postępu Przepustki Bitewnej, podzielona na misje dzienne, tygodniowe i sezonowe.
440. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_04_title_01] — tekst] 배틀 패스 초과 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_04_title_01].content
   limit: do 120 znaków
   EN: Max Level Rewards
   PL: Nagrody ponad limit poziomu
441. [Samouczek i wskazówki [tutorial_mainui_14_battlepass_page_04_desc_01] — tekst] 배틀 패스에서 보상 수령이 가능한 레벨을 초과한 뒤 레벨이 오를 시 초과 보상이 주어집니다. 림버스 패스를 사용한다면 더 많은 초과 보상이 주어집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_14_battlepass_page_04_desc_01].content
   limit: do 230 znaków
   EN: Once you’ve reached the maximum level for determined rewards on the battle pass, you will be given bonus rewards with each level up. Limbus Pass owners gain additional rewards.
   PL: Po przekroczeniu maksymalnego poziomu Przepustki każdy kolejny awans zapewnia nagrody dodatkowe — posiadacze Przepustki Limbus otrzymują ich więcej.
442. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_title] — tekst] 경험치 채광
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation
   PL: Lochy Wydobywcze PD
443. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_01_title_01] — tekst] 경험치 채광 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_01_title_01].content
   limit: do 120 znaków
   EN: List of Luxcavation Sites
   PL: Lista Wydobycia PD
444. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_01_desc_01] — tekst] 추천 레벨에 맞는 경험치 채광 중 하나를 선택하여 입장합니다. 입장할 때 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_01_desc_01].content
   limit: do 150 znaków
   EN: Choose a stage to enter based on the strength of your Sinners. Entering Luxcavation stages costs Enkephalin Modules.
   PL: Wybierz etap Wydobycia PD dopasowany do zalecanego poziomu drużyny. Wejście zużywa Moduły Enkefaliny.
445. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_02_title_01] — tekst] 유효 속성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_02_title_01].content
   limit: do 120 znaków
   EN: Useful Affinities
   PL: Skuteczne typy
446. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_02_desc_01] — tekst] 경험치 채광에 등장하는 적들은 독특한 물리 내성과 속성 내성을 가지고 있습니다. 해당 스테이지에서 큰 효과를 볼 수 있는 공격 유형이 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_02_desc_01].content
   limit: do 200 znaków
   EN: Enemies in EXP Luxcavation have specific resistances. You can check the type and Affinity that will be the most effective for each stage before entering.
   PL: Przeciwnicy w Wydobyciu PD cechują się wyrazistymi odpornościami — przed wejściem sprawdzisz typ ataku najskuteczniejszy na danym etapie.
447. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_03_title_01] — tekst] 경험치 채광 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_03_title_01].content
   limit: do 120 znaków
   EN: EXP Luxcavation Rewards
   PL: Nagrody Wydobycia PD
448. [Samouczek i wskazówki [tutorial_mainui_15_exp_dungeon_page_03_desc_01] — tekst] 경험치 채광 클리어 시 전투 경험치와 인격 학습 티켓을 획득할 수 있으며, 매일 일정 횟수만큼 추가 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_15_exp_dungeon_page_03_desc_01].content
   limit: do 210 znaków
   EN: In EXP Luxcavation, you can acquire experience from combat and Identity Training Tickets, and you can earn bonus rewards for a set number of clears each day.
   PL: Ukończenie Wydobycia PD zapewnia doświadczenie bojowe oraz Bilety Treningu Tożsamości, a określona liczba dziennych ukończeń daje dodatkowe premie.
449. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_title] — tekst] 끈 채광
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_title].content
   limit: do 120 znaków
   EN: Thread Luxcavation
   PL: Lochy Wydobywcze Nici
450. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_01_title_01] — tekst] 끈 채광 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_01_title_01].content
   limit: do 120 znaków
   EN: List of Luxcavation Sites
   PL: Lista Wydobycia Nici
451. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_01_desc_01] — tekst] 요일에 따라 등장하는 환상체가 변경됩니다. 입장할 때 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_01_desc_01].content
   limit: do 170 znaków
   EN: Features different Abnormality battle stages depending on the day of the week. Entering Luxcavation stages costs Enkephalin Modules.
   PL: Pojawiająca się Anomalia zależy od dnia tygodnia. Wejście zużywa Moduły Enkefaliny.
452. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_02_title_01] — tekst] 유효 속성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_02_title_01].content
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_02_desc_01] — tekst] 끈 채광에 등장하는 적들은 독특한 물리 내성과 속성 내성을 가지고 있습니다. 해당 스테이지에서 큰 효과를 볼 수 있는 죄악 속성이 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_02_desc_01].content
   limit: do 200 znaków
   EN: Enemies in Thread Luxcavation have specific resistances. You can check the type and Affinity that will be the most effective for each stage before entering.
   PL: Przeciwnicy w Wydobyciu Nici cechują się wyrazistymi odpornościami — przed wejściem sprawdzisz Grzechy najskuteczniejsze na danym etapie.
454. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_03_title_01] — tekst] 레벨 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_03_title_01].content
   limit: do 120 znaków
   EN: Level Select
   PL: Wybór poziomu
455. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_03_desc_01] — tekst] 추천 레벨에 맞는 끈 채광 중 하나를 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_03_desc_01].content
   limit: do 120 znaków
   EN: Choose a stage to enter based on the strength of your Sinners.
   PL: Wybierz poziom trudności Wydobycia Nici dopasowany do siły swojej drużyny.
456. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_04_title_01] — tekst] 끈 채광 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_04_title_01].content
   limit: do 120 znaków
   EN: Thread Luxcavation Rewards
   PL: Nagrody Wydobycia Nici
457. [Samouczek i wskazówki [tutorial_mainui_16_thread_dungeon_page_04_desc_01] — tekst] 끈 채광 클리어 시 끈을 획득할 수 있으며, 매일 일정 횟수만큼 추가 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_16_thread_dungeon_page_04_desc_01].content
   limit: do 150 znaków
   EN: In Thread Luxcavation, you can acquire Thread, and you can earn bonus rewards for a set number of clears each day.
   PL: Ukończenie Wydobycia Nici zapewnia Nić, a określona liczba dziennych ukończeń gwarantuje dodatkowe premie.
458. [Samouczek i wskazówki [tutorial_mainui_17_railway_title] — tekst] 거울굴절철도
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_title].content
   limit: do 120 znaków
   EN: Refraction Railways
   PL: Kolej Załamania
459. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_01_title_01] — tekst] 거울굴절철도 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_01_title_01].content
   limit: do 120 znaków
   EN: Refraction Railway Opening
   PL: Otwarcie Kolei Załamania
460. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_01_desc_01] — tekst] 거울굴절철도 운행 기간 동안 입장할 수 있는 호선이 등장합니다.\n활성화된 노선을 선택하여 재화 소모 없이 자유롭게 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_01_desc_01].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Lines of the Refraction Railway run for a certain period of time.\nYou can enter the available Lines at no cost.
   PL: W okresie kursowania Kolei Załamania pojawiają się dostępne linie.\nAktywną linię możesz wybrać i rozgrywać bez zużywania jakichkolwiek zasobów.
461. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_02_title_01] — tekst] 운행 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_02_title_01].content
   limit: do 120 znaków
   EN: Running Period
   PL: Okres kursowania
462. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_02_desc_01] — tekst] 거울굴절철도 운행 기간이 노선 측면에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_02_desc_01].content
   limit: do 120 znaków
   EN: The Railway’s running time is displayed on the side of the Line.
   PL: Czas kursowania Kolei Załamania widnieje z boku danej linii.
463. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_03_desc_01] — tekst] 입장 시, 보유한 인격과 E.G.O를 선택하여 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_03_desc_01].content
   limit: do 120 znaków
   EN: You will choose a number of Identities and E.G.O to begin the expedition with.
   PL: Przy wejściu wybierasz skład spośród posiadanych Tożsamości oraz E.G.O.
464. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_04_desc_01] — tekst] 다른 전투 콘텐츠와 달리 편성을 완료하여 입장하게 되면, 이후에 진행된 레벨업이나 동기화, 환상 해석은 해당 편성에 반영되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_04_desc_01].content
   limit: do 240 znaków
   EN: Unlike other combat-based content, the level-ups and tier-ups done to your Identities and E.G.O while an expedition is in progress will not be immediately reflected on your team’s status.
   PL: W odróżnieniu od pozostałych trybów bojowych po zatwierdzeniu składu późniejsze podnoszenie poziomów, Synchronizacja ani Splot Nici nie zostaną odzwierciedlone w trwającym przejeździe.
465. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_05_desc_01] — tekst] 편성은 스테이지 진행 도중에 교체할 수 없습니다.\n편성된 인격과 E.G.O의 레벨업, 동기화, 환상 해석을 반영하거나 다른 인격, E.G.O로 교체하기 위해서는 다시 입장하여 첫 스테이지부터 진행해야 합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_05_desc_01].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You may not change your team in the middle of an expedition. \nIf you wish to modify your setup or reflect upgrades on your Identities and E.G.O, you must start a new expedition.
   PL: Składu nie można zmieniać w trakcie trwania przejazdu.\nAby uwzględnić ulepszenia Tożsamości i E.G.O lub wymienić skład, należy rozpocząć przejazd od nowa od pierwszej stacji.
466. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_06_title_01] — tekst] 거울굴절철도 메인 화면
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_06_title_01].content
   limit: do 120 znaków
   EN: Refraction Railway Main Screen
   PL: Ekran główny Kolei Załamania
467. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_06_desc_01] — tekst] 거울굴절철도에 등장하는 전투는 총 13개의 스테이지로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_06_desc_01].content
   limit: do 120 znaków
   EN: The Refraction Railway consists of 13 stages.
   PL: Ta linia Kolei Załamania składa się łącznie z 13 stacji bojowych.
468. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_07_title_01] — tekst] 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_07_title_01].content
   limit: do 120 znaków
   EN: Encounter
   PL: Walka
469. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_07_desc_01] — tekst] 거울굴절철도에 등장하는 모든 전투는 아군의 스킬을 직접 적 스킬과 대응하는, 집중 전투와 동일한 방식으로 진행됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_07_desc_01].content
   limit: do 180 znaków
   EN: Every battle in the Refraction Railway will allow you to directly match ally skills against enemy skills, similar to Focused Encounters.
   PL: Wszystkie walki na Kolei Załamania rozgrywane są tak jak starcia skupione — poprzez bezpośrednie parowanie umiejętności sojuszników z polami wrogów.
470. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_08_title_01] — tekst] E.G.O 자원 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_08_title_01].content
   limit: do 120 znaków
   EN: Current E.G.O Resources
   PL: Stan zasobów E.G.O
471. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_08_desc_01] — tekst] 스테이지 클리어 후 남은 E.G.O 자원은 다음 스테이지에서 사용할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_08_desc_01].content
   limit: do 120 znaków
   EN: The E.G.O resources held after clearing a stage can be carried over to the next stage.
   PL: Zasoby E.G.O pozostałe po ukończeniu stacji przechodzą na kolejną stację.
472. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_08_title_02] — tekst] 인격 상태
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_08_title_02].content
   limit: do 120 znaków
   EN: Sinner Status
   PL: Stan Tożsamości
473. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_08_desc_02] — tekst] 편성한 인격의 체력, 정신력, 사망 상태가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_08_desc_02].content
   limit: do 120 znaków
   EN: The HP, SP, and availability of your Identities are shown here.
   PL: Wyświetla PŻ, Poczytalność oraz ewentualny zgon Tożsamości ze składu.
474. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_09_title_01] — tekst] 클리어 턴 및 누적 턴
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_09_title_01].content
   limit: do 120 znaków
   EN: Clear Turns & Total Turns
   PL: Tury ukończenia i łączne tury
475. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_09_desc_01] — tekst] 스테이지 클리어 시, 해당 스테이지를 클리어하는 데 걸린 클리어 턴, 시작부터 해당 스테이지를 클리어하기까지 걸린 누적 턴이 기록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_09_desc_01].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When you clear a stage, the Station will record the number of turns taken to beat it: Clear Turns.\nAs well as the cumulative number of turns taken throughout the current expedition: Total Turns.
   PL: Po ukończeniu stacji zapisywana jest liczba tur zużytych na danej stacji (Tury ukończenia) oraz suma tur od początku przejazdu (Łączne tury).
476. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_10_title_01] — tekst] 인격 상태
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_10_title_01].content
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_10_desc_01] — tekst] 편성한 인격의 체력, 정신력, 사망 상태가 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_10_desc_01].content
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_11_title_01] — tekst] 배너 획득 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_11_title_01].content
   limit: do 120 znaków
   EN: Banner Requisites
   PL: Warunki zdobycia sztandaru
479. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_11_desc_01] — tekst] 이벤트 배너 획득 조건을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_11_desc_01].content
   limit: do 120 znaków
   EN: You can check the requirements for acquiring banners here.
   PL: Sprawdzisz tu warunki zdobycia sztandarów wydarzenia.
480. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_11_desc_02] — tekst] 획득 조건이 어려울수록 더욱 특별한 배너를 얻게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_11_desc_02].content
   limit: do 120 znaków
   EN: You can acquire more lavishly ornamented banners as you meet more difficult conditions.
   PL: Im trudniejszy warunek spełnisz, tym bardziej wyjątkowy sztandar otrzymasz.
481. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_12_title_01] — tekst] 분실물 보관소
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_12_title_01].content
   limit: do 120 znaków
   EN: The Lost & Found
   PL: Biuro Rzeczy Znalezionych
482. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_12_desc_01] — tekst] 스테이지를 처음으로 클리어할 경우, 해당 스테이지의 보상이 분실물 보관소에 등록됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_12_desc_01].content
   limit: do 160 znaków
   EN: After clearing a stage in the Line for the first time during the event period, the rewards will be sent to the Lost & Found.
   PL: Przy pierwszym ukończeniu stacji jej nagrody trafiają do Biura Rzeczy Znalezionych.
483. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_12_desc_02] — tekst] 이벤트 기간 중 스테이지를 최초로 클리어하면 그 보상이 분실물 보관소에 쌓입니다.\n분실물 보관소에서 보상을 수령하기 위해서는 최초 1회에 한하여 일정량의 엔케팔린 모듈을 지불해야 합니다.\n이후에 얻게 되는 보상은 별도의 추가 엔케팔린 모듈 소모 없이 언제든지 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_12_desc_02].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After clearing a stage in the Line for the first time during the event period, the rewards will be sent to the Lost & Found.\nTo gain access to the Lost & Found, a number of Enkephalin Modules will be required.\nAfterward, you may freely access it and claim the rewards you’ve earned at no additional cost.
   PL: Nagrody za pierwsze ukończenie poszczególnych stacji w okresie wydarzenia gromadzą się w Biurze Rzeczy Znalezionych.\nAby odblokować odbiór nagród z Biura Rzeczy Znalezionych, wystarczy jednorazowo opłacić określoną liczbę Modułów Enkefaliny.\nWszystkie kolejne nagrody odbierzesz już w dowolnej chwili bez dodatkowych kosztów.
484. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_13_title_01] — tekst] 누적 기록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_13_title_01].content
   limit: do 120 znaków
   EN: Total Record
   PL: Archiwum przejazdów
485. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_13_desc_01] — tekst] 최종 스테이지를 클리어할 경우 거울굴절철도 플레이 기록이 저장되며, 그 기록들을 최대 20개까지 확인할 수 있습니다.\n기록이 20개를 넘어갈 경우에는 누적 턴 수가 많은 기록이 먼저 사라지게 되며, 턴 수도 동일할 경우에는 인격 사망 수가 많은 기록이 삭제됩니다.\n이 역시 동일하다면 더 오래된 기록이 삭제됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_13_desc_01].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon clearing the final stage, the records for the expedition will be saved.\nRecords of up to 20 expeditions are kept in the logs.\nIf more than 20 records are in the log, the ones with the highest Total Turns will be removed first; if the Total Turns are the same, then the death count acts as the next criterion.\nIf the death counts are identical as well, the older record will be removed.
   PL: Ukończenie ostatniej stacji zapisuje wynik przejazdu Kolei Załamania — archiwum przechowuje maksymalnie 20 zapisów.\nPo przekroczeniu 20 wpisów w pierwszej kolejności usuwane są przejazdy z największą łączną liczbą tur, a przy remisie — z większą liczbą zgonów Tożsamości.\nJeśli również ta wartość jest identyczna, usunięty zostaje starszy zapis.
486. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_14_title_01] — tekst] 휴식
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_14_title_01].content
   limit: do 120 znaków
   EN: Resting
   PL: Odpoczynek
487. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_14_desc_01] — tekst] 전투에 참여한 인격의 체력과 정신력은 다음 스테이지 전투에 참가할 경우 그대로 유지됩니다.\n대신 해당 인격이 다음 스테이지 전투에 참가하지 않고 쉴 경우 그 다음 스테이지 진입 시, 체력이 완전히 회복되고 정신력이 0으로 초기화됩니다.\n단, 정신력이 0 이상일 경우에는 0으로 초기화되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_14_desc_01].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Health and Sanity of your Sinners will carry over between stages.\nHowever, after clearing a stage, those who did not participate in the battle will fully recover their HP and SP when entering the next stage.\nAny Sanities above 0 will be maintained in either case.
   PL: PŻ i Poczytalność Tożsamości biorących udział w walce przechodzą bez zmian na kolejną stację.\nJeśli natomiast dana Tożsamość odpocznie i nie weźmie udziału w kolejnej stacji, przy wejściu na następną jej PŻ zostaną w pełni odnowione, a ujemna Poczytalność zresetowana do 0.\nDodatnia Poczytalność (powyżej 0) zostaje zachowana.
488. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_15_title_01] — tekst] 기록 경신
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_15_title_01].content
   limit: do 120 znaków
   EN: Breaking Records
   PL: Poprawianie rekordu
489. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_15_desc_01] — tekst] 스테이지 진행 중 이전에 클리어한 특정 스테이지부터 다시 시작할 수 있습니다.\n특정 스테이지부터 다시 시작할 경우 해당 스테이지 입장 시점의 인격 상태와 E.G.O 자원 보유량이 반영된 상태로 전투를 시작하며, 그 이후 스테이지의 클리어 기록이 초기화되어 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_15_desc_01].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During an expedition, you can choose to start over from previously cleared Stations.\nWhen you do so, the battle will start with the Sinners’ statuses and E.G.O resources reverted to that point, and any progress you've made since that Station will be reset.
   PL: W trakcie przejazdu możesz wznowić trasę od dowolnej wcześniej ukończonej stacji.\nWalka rozpocznie się wówczas ze stanem Tożsamości oraz zasobami E.G.O z chwili pierwszego wejścia na tę stację, natomiast zapisy ukończenia wszystkich dalszych stacji zostaną zresetowane.
490. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_16_title_01] — tekst] 거울굴절철도 특별 장식 배너
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_16_title_01].content
   limit: do 120 znaków
   EN: The Railway’s Special Decorative Banners
   PL: Specjalny sztandar Kolei Załamania
491. [Samouczek i wskazówki [tutorial_mainui_17_railway_page_16_desc_01] — tekst] 거울굴절철도 운행 기간이 종료되면 자신이 획득한 배너에 가장 높은 기록의 누적 턴 수가 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_17_railway_page_16_desc_01].content
   limit: do 170 znaków
   EN: When a Line of the Refraction Railway closes, the best total turn record will be etched on the lower side of that Line’s banner.
   PL: Po zakończeniu okresu kursowania danej linii Kolei Załamania na zdobytym sztandarze zostanie uwieczniony twój najlepszy rekord łącznej liczby tur.
492. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_title] — tekst] 헬스 치킨
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_title].content
   limit: do 120 znaków
   EN: Hell’s Chicken
   PL: Piekielny Kurczak
493. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_01_title_01] — tekst] 헬스 치킨 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_01_title_01].content
   limit: do 120 znaków
   EN: Unlocking Hell’s Chicken
   PL: Odblokowanie Piekielnego Kurczaka
494. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_01_desc_01] — tekst] [헬스 치킨 이벤트 페이지]는 주요 이야기의 3-22를 클리어할 경우 개방됩니다.\n유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_01_desc_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The [Hell’s Chicken Event Page] opens after clearing Stage 3-22 of the Main Story.\nYou may enter the event page via the banner on the Window or the Driverside.
   PL: [Strona wydarzenia Piekielny Kurczak] odblokowuje się po ukończeniu etapu 3-22 Głównej Opowieści.\nWejdziesz na nią przez baner wydarzenia w Oknie lub zakładce Jazda.
495. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_02_title_01].content
   limit: do 120 znaków
   EN: Event Period
   PL: Czas trwania wydarzenia
496. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_02_desc_01] — tekst] 헬스 치킨 이벤트 기간이 표시됩니다. 이벤트 기간 동안 헬스 치킨 혹은 주요 이야기의 스테이지와 던전을 클리어하여 [봉이 인형]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_02_desc_01].content
   limit: do 210 znaków
   EN: The duration of the Hell’s Chicken event is shown here. During the event, you can earn [Bongy Plushies] by clearing Stages and Dungeons in the event and Main Story.
   PL: Wyświetla czas trwania wydarzenia Piekielny Kurczak. W tym okresie za ukończenie etapów i lochów wydarzenia oraz Głównej Opowieści zdobywasz [Maskotki Bongiego].
497. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_02_desc_02] — tekst] ※ 단, 거울 던전, 채광, 거울 굴절 철도에서는 [봉이 인형]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_02_desc_02].content
   limit: do 120 znaków
   EN: ※ Mirror Dungeons, Luxcavation, and the Refraction Railway do not give [Bongy Plushies].
   PL: ※ [Maskotek Bongiego] nie można zdobyć w Lustrzanych Lochach, Wydobyciu ani na Kolei Załamania.
498. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_03_title_01].content
   limit: do 120 znaków
   EN: Event Stages
   PL: Etapy wydarzenia
499. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_03_desc_01] — tekst] 헬스 치킨 전투는 총 8개의 스테이지와 2개의 던전으로 구성됩니다.\n헬스 치킨 전투에서는 클리어 보상과 별개로 EX 클리어 보상으로 [봉이 인형]을 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_03_desc_01].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hell’s Chicken consists of 8 stages and 2 dungeons.\nSaid stages and dungeons also offer batches of [Bongy Plushies] as a first-time EX Clear bonus.
   PL: Walki Piekielnego Kurczaka obejmują 8 etapów oraz 2 lochy.\nOprócz zwykłych nagród pierwsze ukończenie z warunkiem EX zapewnia dodatkowe [Maskotki Bongiego] (jednorazowo).
500. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_03_desc_02] — tekst] 헬스 치킨 던전에서는 일반 스테이지보다 훨씬 많은 [봉이 인형]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_03_desc_02].content
   limit: do 140 znaków
   EN: You can earn considerably more [Bongy Plushies] from Hell’s Chicken Dungeons compared to regular stages.
   PL: Lochy Piekielnego Kurczaka zapewniają znacznie więcej [Maskotek Bongiego] niż zwykłe etapy.
501. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_04_title_01] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_04_title_01].content
   limit: do 120 znaków
   EN: Event Bonus Units
   PL: Jednostki premiowane
502. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_04_desc_01] — tekst] 헬스 치킨 이벤트 인격 또는 E.G.O를 편성하여 스테이지, 던전을 클리어하면 [봉이 인형]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_04_desc_01].content
   limit: do 190 znaków
   EN: Having Identities and E.G.O from the Hell’s Chicken event on your team increases the amount of [Bongy Plushies] earned from stages and dungeons.
   PL: Wystawienie w składzie Tożsamości lub E.G.O z wydarzenia Piekielny Kurczak zwiększa liczbę [Maskotek Bongiego] zdobywanych za etapy i lochy.
503. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_05_title_01] — tekst] 쿠폰 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_05_title_01].content
   limit: do 120 znaków
   EN: Coupon Trade-in
   PL: Wymiana Kuponów
504. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_05_desc_01] — tekst] 획득한 [봉이 인형]의 수에 비례하여 [쿠폰 교환]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_05_desc_01].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Coupon Trade-in] based on the number of [Bongy Plushies] you have.
   PL: W zakładce [Wymiana Kuponów] odbierzesz rozmaite nagrody w zależności od liczby zebranych [Maskotek Bongiego].
505. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_06_title_01] — tekst] 쿠폰 교환
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_06_title_01].content
   (powtórzenie elementu 503 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_06_desc_01] — tekst] [쿠폰 교환] 페이지에서 각종 재화와 이벤트 배포 인격, E.G.O를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_06_desc_01].content
   limit: do 140 znaków
   EN: You can acquire event reward Identities and E.G.O, as well as various currencies from the [Coupon Trade-in].
   PL: Na stronie [Wymiany Kuponów] zdobędziesz różnorodne zasoby oraz darmową Tożsamość i E.G.O wydarzenia.
507. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_06_desc_02] — tekst] [쿠폰 교환] 에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_06_desc_02].content
   limit: do 120 znaków
   EN: The [Coupon Trade-in]’s open duration is shown here.
   PL: Wskazuje okres, w którym można odbierać nagrody w [Wymianie Kuponów].
508. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_07_title_01] — tekst] 이벤트 던전
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_07_title_01].content
   limit: do 120 znaków
   EN: Event Dungeons
   PL: Lochy wydarzenia
509. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_07_desc_01] — tekst] 헬스 치킨 던전은 거울 던전 플레이 방식으로 진행됩니다.\n헬스 치킨 던전의 난이도는 두 가지로, 큰 특징으로는 다음과 같이 구분할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_07_desc_01].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hell’s Chicken Dungeons play similarly to Mirror Dungeons.\nThe dungeons come in two difficulties; their major traits are as follows.
   PL: Lochy Piekielnego Kurczaka opierają się na zasadach Lustrzanych Lochów.\nDostępne są dwa poziomy trudności różniące się następującymi cechami:
510. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_08_title_01] — tekst] E.G.O 기프트 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_08_title_01].content
   limit: do 120 znaków
   EN: Selecting E.G.O Gifts
   PL: Wybór Darów E.G.O
511. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_08_desc_01] — tekst] 거울 던전 E.G.O 기프트 중 일부가 헬스 치킨 던전에서 등장합니다.\n이 E.G.O 기프트들은 이벤트 인격과 E.G.O를 효과적으로 활용할 수 있도록 돕습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_08_desc_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Several E.G.O Gifts from the Mirror Dungeon will appear in the Hell’s Chicken Dungeon.\nThese E.G.O Gifts will assist event Identities and E.G.O to shine in their respective specialties.
   PL: W lochach Piekielnego Kurczaka pojawia się wybrana pula Darów E.G.O z Lustrzanych Lochów.\nWspierają one mocne strony Tożsamości i E.G.O powiązanych z wydarzeniem.
512. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_09_title_01] — tekst] 이벤트 던전 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_09_title_01].content
   limit: do 120 znaków
   EN: Event Team Setup
   PL: Skład w lochu wydarzenia
513. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_09_desc_01] — tekst] 헬스 치킨 던전에서는 총 5명의 인격을 선택하여 데려갑니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_09_desc_01].content
   limit: do 120 znaków
   EN: In the Hell’s Chicken dungeons, you begin expeditions with 5 Identities.
   PL: Do lochu Piekielnego Kurczaka zabierasz skład złożony z 5 Tożsamości.
514. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_09_title_02] — tekst] 프리셋
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_09_title_02].content
   limit: do 120 znaków
   EN: Presets
   PL: Szablon składu
515. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_09_desc_02] — tekst] 헬스 치킨 던전에서 편의성을 위한 프리셋 기능이 추가됩니다.\n프리셋 버튼을 통해 직전에 선택한 인격과 E.G.O의 목록을 불러와 빠르게 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_09_desc_02].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For player convenience, a preset function is being added for the Hell’s Chicken dungeons.\nUsing the preset button, you can quickly load the team setup you last used and make a swift entry.
   PL: Dla wygody w lochach Piekielnego Kurczaka dodano funkcję szablonu.\nPrzycisk szablonu pozwala błyskawicznie wczytać ostatnio użyte Tożsamości i E.G.O.
516. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_10_title_01] — tekst] 이벤트 던전 구성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_10_title_01].content
   limit: do 120 znaków
   EN: Dungeon Structure
   PL: Budowa lochu wydarzenia
517. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_10_desc_01] — tekst] 헬스 치킨 던전에 입장할 때마다 거울 던전과 같이 방과 경로가 무작위로 생성됩니다.\n헬스 치킨 던전은 하나의 층으로 구성되어 있으며, 마지막 방에서는 헬스 치킨 최종 보스가 고정으로 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_10_desc_01].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The layouts and paths in the Hell’s Chicken dungeons are randomly generated each time you enter.\nThese dungeons consist of a single floor, and the final node always features the Hell’s Chicken boss.
   PL: Przy każdym wejściu do lochu Piekielnego Kurczaka układ komnat i ścieżek jest losowany tak jak w Lustrzanych Lochach.\nLoch składa się z jednego piętra, a w ostatniej komnacie zawsze czeka finałowy boss Piekielnego Kurczaka.
518. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_11_title_01] — tekst] 헬스 치킨 전용 이벤트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_11_title_01].content
   limit: do 120 znaków
   EN: Exclusive Encounters
   PL: Wydarzenia specjalne Piekielnego Kurczaka
519. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_11_desc_01] — tekst] 헬스 치킨 던전에서만 만날 수 있는 특별한 이벤트와 E.G.O 기프트가 있습니다.\n헬스 치킨 던전 전용 이벤트는 방 아래에 별도의 아이콘이 표시되므로 쉽게 구분할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_11_desc_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are special encounters and E.G.O Gifts unique to the Hell’s Chicken dungeons.\nThese specialties are marked with a unique icon below the node in the dungeon for easier identification.
   PL: W lochach Piekielnego Kurczaka występują unikalne wydarzenia oraz Dary E.G.O.\nWęzły z wydarzeniami specjalnymi mają osobną ikonę pod komnatą, dzięki czemu łatwo je rozpoznać.
520. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_12_title_01] — tekst] 이벤트 이후
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_12_title_01].content
   limit: do 120 znaków
   EN: Event Closure
   PL: Po zakończeniu wydarzenia
521. [Samouczek i wskazówki [tutorial_mainui_18_hells_chicken_12_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석 - [외전]과 상영관 - [그 밖의 이야기]를 통해 언제든지 헬스 치킨 전투를 다시 즐기거나 스토리를 다시 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_18_hells_chicken_12_desc_01].content
   limit: do 250 znaków
   EN: Even after the event fully ends, you will be able to experience the Hell’s Chicken combat encounters and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę Piekielnego Kurczaka możesz w każdej chwili odtworzyć poprzez Jazda — [Intervallo] oraz Teatr — [Opowieści Poboczne].
522. [Samouczek i wskazówki [tutorial_manual_1_season_information_title] — tekst] 시즌 안내
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_title].content
   limit: do 120 znaków
   EN: Seasons Guide
   PL: Przewodnik po sezonach
523. [Samouczek i wskazówki [tutorial_manual_1_season_information_01_title_01] — tekst] 시즌 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_01_title_01].content
   limit: do 120 znaków
   EN: Season Duration
   PL: Czas trwania sezonu
524. [Samouczek i wskazówki [tutorial_manual_1_season_information_01_desc_01] — tekst] 시즌이 새롭게 시작될 때마다 새로운 배틀 패스가 등장합니다.\n배틀 패스에서 현재 시즌의 기간을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_01_desc_01].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a new season begins, a new Battle Pass is introduced with it.\nYou can check the duration of the current season on the Battle Pass page.
   PL: Wraz z rozpoczęciem nowego sezonu pojawia się nowa Przepustka Bitewna.\nCzas trwania bieżącego sezonu sprawdzisz na ekranie Przepustki Bitewnej.
525. [Samouczek i wskazówki [tutorial_manual_1_season_information_02_title_01] — tekst] 배틀 패스 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_02_title_01].content
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
526. [Samouczek i wskazówki [tutorial_manual_1_season_information_02_desc_01] — tekst] 배틀 패스에서 현재 시즌의 재화와 E.G.O를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_02_desc_01].content
   limit: do 120 znaków
   EN: You can obtain currencies for the current season as well as E.G.O from the Battle Pass.
   PL: W Przepustce Bitewnej zdobędziesz waluty bieżącego sezonu oraz E.G.O.
527. [Samouczek i wskazówki [tutorial_manual_1_season_information_03_title_01] — tekst] 인격 · E.G.O의 시즌 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_03_title_01].content
   limit: do 120 znaków
   EN: Season Info for Identities & E.G.O
   PL: Oznaczenie sezonu Tożsamości i E.G.O
528. [Samouczek i wskazówki [tutorial_manual_1_season_information_03_desc_01] — tekst] 인격 정보 또는 E.G.O 정보의 이름 하단에 시즌 정보가 표기되어 있습니다.\n시즌 정보가 표기되어 있지 않은 경우는 [통상]으로 분류됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_03_desc_01].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can check the season an Identity or E.G.O belongs to below its name in the info tab.\nThose without a season shown are categorized into the [Regular] tag.
   PL: Pod nazwą w oknie informacji o Tożsamości lub E.G.O widnieje przypisany sezon.\nPozycje bez oznaczenia sezonu należą do puli [Standardowej].
529. [Samouczek i wskazówki [tutorial_manual_1_season_information_04_title_01] — tekst] 이벤트 인격 · E.G.O의 시즌 정보
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_04_title_01].content
   limit: do 120 znaków
   EN: Season Info for Event Identities & E.G.O
   PL: Oznaczenie sezonowe pozycji wydarzeń
530. [Samouczek i wskazówki [tutorial_manual_1_season_information_04_desc_01] — tekst] 이벤트 인격과 E.G.O의 경우에는 시즌 정보 옆에 [EVENT] 표기가 추가로 붙습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_04_desc_01].content
   limit: do 120 znaków
   EN: Event Identities and E.G.O have [EVENT] marked next to their season tag.
   PL: Tożsamości oraz E.G.O pochodzące z wydarzeń mają obok oznaczenia sezonu dodatkowy znacznik [EVENT].
531. [Samouczek i wskazówki [tutorial_manual_1_season_information_05_title_01] — tekst] 자아 파편
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_05_title_01].content
   (powtórzenie elementu 397 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Samouczek i wskazówki [tutorial_manual_1_season_information_05_desc_01] — tekst] 자아 파편은 명시된 시즌 기간 동안 사용할 수 있습니다.\n\n새로운 시즌이 시작되면 이전 시즌의 자아 파편은 그 수의 절반만큼 다음 시즌으로 이월됩니다. (올림하여 처리)\n\n만약 두 번 이상의 시즌이 지나게 된다면, 지나간 시즌 횟수만큼 거듭하여 반감된 수치가 이월됩니다.\n\n이월되지 않은 자아 파편은 끈으로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_05_desc_01].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Egoshards can be used for the notated period, matching the Season’s duration.\n\nWhen a new Season begins, half of the previous Season’s Egoshards will be carried over, converted and rounded up for the new Season.\n\nThe carryover rates for unconverted Egoshards from multiple seasons past will be halved for each following Season.\n\nThe remaining Egoshards are converted into Thread.
   PL: Odłamków E.G.O można używać przez cały wskazany czas trwania sezonu.\n\nW chwili rozpoczęcia nowego sezonu połowa Odłamków E.G.O z poprzedniego sezonu przechodzi na nowy sezon (z zaokrągleniem w górę).\n\nJeśli miną dwa lub więcej sezonów, przenoszona liczba ulega połowicznemu zmniejszeniu za każdy kolejny sezon.\n\nNieprzeniesione Odłamki E.G.O zostają zamienione na Nić.
533. [Samouczek i wskazówki [tutorial_manual_1_season_information_06_title_01] — tekst] 자아 파편 상자 · 자아 파편 선택 상자
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_06_title_01].content
   limit: do 120 znaków
   EN: Egoshard Crates
   PL: Skrzynie Odłamków E.G.O i Imienne Skrzynie Odłamków
534. [Samouczek i wskazówki [tutorial_manual_1_season_information_06_desc_01] — tekst] 자아 파편 상자, 자아 파편 선택 선택 상자도 마찬가지로 명시된 시즌 기간 동안 사용할 수 있습니다.\n\n새로운 시즌이 시작되면 이전 시즌의 자아 파편 상자, 자아 파편 선택 상자는 그 수의 절반만큼 다음 시즌으로 이월됩니다. (올림하여 처리)\n\n만약 두 번 이상의 시즌이 지나게 된다면, 지나간 시즌 횟수만큼 거듭하여 반감된 수치가 이월됩니다.\n\n이월되지 않은 자아 파편 상자, 자아 파편 선택 상자는 끈 상자로 전환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_06_desc_01].content
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Similarly to Egoshards, Egoshard Crates can be used for the notated period, matching the Season’s duration.\n\nWhen a new Season begins, half of the Egoshard Crates (both random & nominable) will be carried over, converted and rounded up for the new Season.\n\nThe carryover rates for unconverted Egoshard Crates from multiple Seasons past will be halved for each following Season.\n\nThe remaining Crates are converted into Thread Crates.
   PL: Skrzynie Odłamków E.G.O oraz Imienne Skrzynie Odłamków E.G.O również zachowują ważność przez wskazany czas trwania sezonu.\n\nW chwili rozpoczęcia nowego sezonu połowa niewykorzystanych skrzyń obu rodzajów przechodzi na nowy sezon (z zaokrągleniem w górę).\n\nJeśli miną dwa lub więcej sezonów, przenoszona liczba ulega połowicznemu zmniejszeniu za każdy kolejny sezon.\n\nNieprzeniesione skrzynie zostają zamienione na Skrzynie Nici.
535. [Samouczek i wskazówki [tutorial_manual_1_season_information_07_title_01] — tekst] 추출
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_07_title_01].content
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Samouczek i wskazówki [tutorial_manual_1_season_information_07_desc_01] — tekst] 새로운 시즌이 시작되면 추출 목록에 새로운 시즌의 인격과 E.G.O가 추가로 등장합니다.\n시즌이 변경된다 하더라도 이전 시즌의 인격들은 추출 목록에서 유지되므로 추출을 통해 획득할 수 있습니다.\n※ 특정 수감자 추출에서는 이전 시즌의 이벤트 인격 · E.G.O가 등장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_07_desc_01].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new Season’s Identities and E.G.O will be added to the list of Extractable items.\nIdentities from previous Seasons remain in the pool, so you can still acquire them from Extraction.\n※ Event Identities & E.G.O from previous Seasons may appear from Sinner Target Extractions.
   PL: Wraz z nowym sezonem do puli Ekstrakcji trafiają nowe sezonowe Tożsamości oraz E.G.O.\nTożsamości z poprzednich sezonów pozostają w puli Ekstrakcji i nadal można je wylosować.\n※ W Ekstrakcjach celowanych konkretnego Grzesznika mogą pojawiać się Tożsamości i E.G.O z wydarzeń poprzednich sezonów.
537. [Samouczek i wskazówki [tutorial_manual_1_season_information_08_title_01] — tekst] 자판기
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_08_title_01].content
   (powtórzenie elementu 399 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Samouczek i wskazówki [tutorial_manual_1_season_information_08_desc_01] — tekst] 새로운 시즌이 시작되면 추출과 마찬가지로 자판기 목록에 새로운 시즌의 인격과 E.G.O가 추가로 등장합니다.\n또한 이전 시즌의 배틀 패스에서 획득할 수 있었던 인격과 E.G.O도 제작할 수 있게 됩니다.\n\n단, 직전 시즌에 등장한 추출 인격과 E.G.O는 자판기 목록에서 사라집니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_manual_1_season_information_08_desc_01].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Identities and E.G.O from the new Season will become available at the Dispenser.\nIn addition, you will be able to exchange for Identities and E.G.O from the Battle Passes of past Seasons.\nPlease note that Extraction IDs belonging to the Season immediately before will be inaccessible until 2 Seasons have passed.
   PL: Wraz z nowym sezonem do oferty Automatu trafiają pozycje z nowego sezonu.\nMożliwa staje się także wymiana na Tożsamości oraz E.G.O z Przepustki Bitewnej poprzedniego sezonu.\n\nZ oferty Automatu tymczasowo znikają natomiast Tożsamości i E.G.O z Ekstrakcji bezpośrednio poprzedzającego sezonu.
539. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon] — tekst] 거울 던전
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon].content
   (powtórzenie elementu 359 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_01] — tekst] 거울 던전 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_01].content
   (powtórzenie elementu 360 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_01] — tekst] 목록에 있는 거울 던전 중 하나를 선택하여 입장할 수 있습니다.\n한 번에 하나의 거울 던전만 진행할 수 있으며, 다른 거울 던전에 입장하기 위해서는 진행 중인 거울 던전을 클리어하거나 포기해야 합니다.\n각각의 거울 던전은 보통 난이도와 어려움 난이도로 구분됩니다. 단, 시작의 거울에는 어려움 난이도가 존재하지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_01].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can choose a Mirror Dungeon from the list to enter.\nOnly one expedition can be carried out at a time; if you want to enter a different Mirror Dungeon while an expedition is in progress, you need to clear or forfeit the ongoing expedition first.\nEach Mirror Dungeon (excluding Mirror of the Beginning) has two difficulty modes: Normal and Hard.
   PL: Wybierz jeden z Lustrzanych Lochów na liście, aby rozpocząć wyprawę.\nNaraz możesz prowadzić tylko jedną wyprawę — wejście do innego Lustrzanego Lochu wymaga ukończenia lub porzucenia bieżącego.\nKażdy Lustrzany Loch (z wyjątkiem Lustra Początku) dzieli się na poziom Normalny oraz Trudny.
542. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_02] — tekst] 주간 추가 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_02].content
   limit: do 120 znaków
   EN: Weekly Bonuses
   PL: Cotygodniowa Premia
543. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_02] — tekst] 거울 던전에서는 보상을 추가로 받을 수 있는 주간 보너스 기회가 매주 3회씩 제공됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_02].content
   limit: do 170 znaków
   EN: Every week, you're given 3 Weekly Bonus eligibilities that grant you additional rewards for Mirror Dungeon expeditions when used.
   PL: W Lustrzanych Lochach co tydzień otrzymujesz 3 szanse Cotygodniowej Premii zapewniające dodatkowe nagrody za ukończenie.
544. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_03] — tekst] 개방 조건
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_03].content
   limit: do 120 znaków
   EN: Unlock Requirements
   PL: Warunki odblokowania
545. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_03] — tekst] 각각의 거울 던전마다 개방 조건이 존재합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_03].content
   limit: do 120 znaków
   EN: Each Mirror Dungeon has requirements you need to meet to unlock.
   PL: Każdy Lustrzany Loch posiada własne warunki odblokowania.
546. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_04] — tekst] E.G.O 기프트 기록집
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_04].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
547. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_04] — tekst] 거울 던전에 등장하는 E.G.O 기프트를 확인할 수 있습니다.\n기록집에서 「획득 정보 없음」으로 표시되는 E.G.O 기프트는 거울 던전을 진행하며 획득하였을 때, 기록집에 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_04].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can check the list of E.G.O Gifts that appear in Mirror Dungeons.\nThe ones you haven't obtained yet in Mirror Dungeon expeditions will be marked with "No Data".
   PL: Sprawdzisz tu Dary E.G.O pojawiające się w Lustrzanych Lochach.\nPozycje oznaczone jako „Brak danych” zostaną odsłonięte po pierwszym zdobyciu ich podczas wyprawy.
548. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_05] — tekst] 최초 E.G.O 기프트 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_05].content
   (powtórzenie elementu 364 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_05] — tekst] 거울 던전 입장 시, E.G.O 기프트가 무작위로 제시됩니다. 이 중 하나를 선택하여 거울 던전을 진행하는 동안 특별한 효과를 누릴 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_05].content
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_06] — tekst] 수감자 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_06].content
   (powtórzenie elementu 366 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_06] — tekst] 거울 던전에 참여할 수감자를 선택합니다.\n각각의 거울 던전마다 처음에 편성할 수 있는 최대 수감자 수가 정해져 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_06].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You will select a team of Sinners to enter the Mirror Dungeon with.\nEach Mirror Dungeon has its own size limit for the starting team.
   PL: Wybierz Grzeszników biorących udział w wyprawie.\nKażdy Lustrzany Loch określa maksymalną liczbę Grzeszników w początkowym składzie.
552. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_07] — tekst] 보유 E.G.O 기프트 목록
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_07].content
   limit: do 120 znaków
   EN: E.G.O Gifts Owned
   PL: Posiadane Dary E.G.O
553. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_07] — tekst] 현재 보유하고 있는 E.G.O 기프트의 목록을 확인할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_07].content
   limit: do 120 znaków
   EN: You can view the E.G.O Gifts you currently have.
   PL: Wyświetla listę aktualnie posiadanych Darów E.G.O.
554. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_08] — tekst] 프리셋
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_08].content
   (powtórzenie elementu 514 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_08] — tekst] 프리셋 사용 시, 수감자 창에서 설정한 인격과 E.G.O 편성을 불러올 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_08].content
   limit: do 130 znaków
   EN: By using presets, you can load up Identity and E.G.O Teams you have set up in the 'Sinners' window.
   PL: Użycie szablonu pozwala wczytać skład Tożsamości oraz E.G.O skonfigurowany w oknie Grzeszników.
556. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_09] — tekst] 코스트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_09].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
557. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_09] — tekst] 현재 보유하고 있는 코스트 수량을 확인할 수 있습니다.\n코스트는 상점에서 E.G.O 기프트를 구입하거나 상점, 쉼터에서 인격 또는 E.G.O를 새롭게 편성할 때 사용됩니다.\n일반 난이도에서는 시작 시 코스트를 제공하지 않으나, 최초 편성하는 과정에서 코스트를 소모하지 않습니다.\n어려움 난이도에서는 시작 시 코스트를 일정량만큼 제공하지만 최초 편성하는 과정에서도 코스트를 소모하게 됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_09].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can view the Cost in your possession here.\nCost is used when purchasing E.G.O Gifts from the shop, or when acquiring new Identities or E.G.O to have on your team at the shop or the rest stop.\nOn Normal difficulty, you are not given any starting Cost, but the initial team setup doesn't require any Cost.\nOn Hard difficulty, you're given a set amount of Cost to build your initial team with.
   PL: Pokazuje aktualnie posiadany Koszt.\nKoszt służy do kupowania Darów E.G.O w Sklepie oraz dobierania nowych Tożsamości i E.G.O w Sklepach i Przystankach Odpoczynku.\nNa poziomie Normalnym zaczynasz bez Kosztu, lecz wybór początkowego składu jest bezpłatny.\nNa poziomie Trudnym otrzymujesz określoną pulę początkowego Kosztu, z której opłacasz również początkowy skład.
558. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_10] — tekst] 인격 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_10].content
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
559. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_10] — tekst] 선택한 수감자의 인격을 편성합니다.\n거울 던전에서는 각 거울 던전에 맞는 인격 레벨이 자동으로 적용됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_10].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select Identities for the Sinners.\nIn Mirror Dungeons, all Identities are set at the level appropriate for the Dungeon.
   PL: Wybierz Tożsamości wskazanych Grzeszników.\nW Lustrzanych Lochach automatycznie stosowany jest poziom Tożsamości przewidziany dla danego lochu.
560. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_11] — tekst] E.G.O 선택
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_11].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
561. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_11] — tekst] 선택한 수감자의 E.G.O를 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_11].content
   limit: do 120 znaków
   EN: Choose E.G.O to use for the selected Sinner.
   PL: Przypisz E.G.O wybranemu Grzesznikowi.
562. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_12] — tekst] 거울 던전 스테이지 입장
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_12].content
   limit: do 120 znaków
   EN: Entering the Mirror Dungeon
   PL: Wejście do Lustrzanego Lochu
563. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_12] — tekst] 인격과 E.G.O 편성을 완료하였다면 확인 버튼을 통해 거울 던전 스테이지로 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_12].content
   limit: do 120 znaków
   EN: After finishing up the initial team setup, press 'Confirm' to enter the Mirror Dungeon.
   PL: Po skonfigurowaniu Tożsamości oraz E.G.O naciśnij „Potwierdź”, aby wejść do Lustrzanego Lochu.
564. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_13] — tekst] 거울 던전 탐사
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_13].content
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_13] — tekst] 거울 던전에 입장하게 되면 방과 경로가 무작위로 생성됩니다.\n현재 방에서 연결된 방을 선택해 진행하며, 각 방에선 다양한 종류의 전투와 이벤트가 무작위로 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_13].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The layouts and paths in Mirror Dungeons are randomly generated each time you enter.\nProceed by moving to one of the adjacent spaces in the next sector, and deal with the encounters and events waiting for you.
   PL: Po wejściu do Lustrzanego Lochu komnaty i ścieżki są generowane losowo.\nWybieraj połączone węzły, aby posuwać się naprzód przez losowe walki i wydarzenia.
566. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_14] — tekst] E.G.O 기프트
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_14].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_14] — tekst] 던전을 진행하며 E.G.O 기프트를 획득합니다.\nE.G.O 기프트는 획득한 던전 안에서만 적용되는 강력한 효과를 주는 아이템입니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_14].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As you explore the dungeon, you may acquire E.G.O Gifts.\nThese items offer powerful effects that last until the end of the exploration.
   PL: Podczas wyprawy zdobywasz Dary E.G.O.\nTo przedmioty zapewniające potężne efekty obowiązujące wyłącznie do końca bieżącego lochu.
568. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_15] — tekst] 수감자 체력 현황
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_15].content
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_15] — tekst] 던전을 진행하는 동안 수감자들의 체력과 정신력, 사망 상태는 유지됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_15].content
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_16] — tekst] 스테이지 유효 속성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_16].content
   limit: do 120 znaków
   EN: Effective Attacks
   PL: Skuteczne typy na węźle
571. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_16] — tekst] 거울 던전의 전투 노드 하단에는 다음과 같이 해당 스테이지에서 유효한 속성이 표기됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_16].content
   limit: do 160 znaków
   EN: Below the combat encounter nodes in Mirror Dungeons, types and affinities effective against the enemies will be shown.
   PL: Pod węzłami bojowymi w Lustrzanych Lochach wyświetlane są typy ataków najskuteczniejsze na danym etapie.
572. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_17] — tekst] 쉼터
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_17].content
   limit: do 120 znaków
   EN: Rest Stops
   PL: Przystanek Odpoczynku
573. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_17] — tekst] 거울 던전 내 쉼터에서는 코스트를 소모하지 않고 아군을 회복하거나 코스트를 소모하여 인격과 E.G.O를 추가로 편성할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_17].content
   limit: do 180 znaków
   EN: In Mirror Dungeons, there are Rest Stops where you may heal up for free, or spend Cost to gain an Identity or E.G.O to deploy on the team.
   PL: W Przystankach Odpoczynku możesz bezpłatnie uleczyć drużynę albo wydać Koszt, aby dobrać do składu kolejne Tożsamości i E.G.O.
574. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_18] — tekst] 상점
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_18].content
   limit: do 120 znaków
   EN: Shops
   PL: Sklep
575. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_18] — tekst] 거울 던전 내 상점에서는 전투를 진행하며 획득한 코스트를 소모하여 E.G.O 기프트를 구입하거나 아군 회복, 인격과 E.G.O 추가 편성, 제시된 인격을 강화시킬 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_18].content
   limit: do 210 znaków
   EN: At Shops, you can purchase E.G.O Gifts, heal allies, recruit Identities or E.G.O, or power up selected allies using the Cost you earned from combat encounters.
   PL: W Sklepie wydasz Koszt zdobyty w walkach na zakup Darów E.G.O, leczenie sojuszników, dobranie Tożsamości i E.G.O lub wzmocnienie wskazanych Tożsamości.
576. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_19] — tekst] 거울 던전 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_19].content
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_19] — tekst] 던전 클리어 시 엔케팔린 모듈을 소모하여 보상을 수령할 수 있습니다.\n매주 3회씩 제공되는 주간 보너스 기회를 사용하여 보상을 수령할 경우, 일정량의 광기와 많은 양의 배틀 패스 경험치를 획득할 수 있습니다.\n보상 수량은 클리어한 방의 수에 따라 지급됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_19].content
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After clearing an expedition, you can spend Enkephalin Modules to claim rewards.\nIf you use the Weekly Bonus Eligibility count, you can earn large amounts of Battle Pass XP and some Lunacy.\nThe amount of rewards depends on the number of nodes cleared.
   PL: Po ukończeniu lochu możesz zużyć Moduły Enkefaliny, aby odebrać nagrody.\nSkorzystanie z jednej z 3 cotygodniowych szans premii zapewni pewną ilość Szaleństwa oraz dużą pulę PD Przepustki Bitewnej.\nWielkość nagród zależy od liczby ukończonych komnat.
578. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_20] — tekst] 어려움 난이도 보상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_20].content
   limit: do 120 znaków
   EN: Hard Difficulty Rewards
   PL: Nagrody poziomu Trudnego
579. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_20] — tekst] 거울의 거울에서부터 등장할 어려움 난이도가 개방되면, 어려움 난이도 보상 획득 기회 횟수가 상단에 추가됩니다.\n어려움 난이도에서는 더 많은 양의 배틀 패스 경험치를 획득할 수 있으나 매주 3회까지만 수령할 수 있습니다.\n어려움 난이도 보상과 주간 추가 보상은 서로 독립적으로 적용됩니다. 어려움 난이도 보상에 주간 추가 보상을 적용할 경우, 보상의 효율을 극대화할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_20].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Once the Hard difficulty of a Mirror Dungeon is unlocked, the Hard difficulty rewards count will be displayed above.\nOn Hard difficulty, you can earn more Battle Pass XP, but you may only claim the rewards 3 times per week.\nThe Hard difficulty rewards bonus and the weekly bonus apply independently; you can maximize your rewards by applying the weekly bonus to the Hard difficulty rewards.
   PL: Po odblokowaniu poziomu Trudnego (począwszy od Lustra Luster) u góry ekranu pojawi się licznik nagród poziomu Trudnego.\nPoziom Trudny zapewnia znacznie więcej PD Przepustki Bitewnej, lecz nagrody te można odebrać maksymalnie 3 razy w tygodniu.\nNagrody poziomu Trudnego oraz Cotygodniowa Premia naliczają się niezależnie — ich połączenie maksymalizuje zysk z jednej wyprawy.
580. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_21] — tekst] 시작 버프
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_21].content
   limit: do 120 znaków
   EN: Starter Buffs
   PL: Wzmocnienia początkowe
581. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_21] — tekst] 거울의 거울부터는 시작 버프를 활성화할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_21].content
   limit: do 120 znaków
   EN: Mirror of Mirrors and the Mirror Dungeons after it have starter buffs you can activate.
   PL: Począwszy od Lustra Luster możesz aktywować wzmocnienia początkowe.
582. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_title_22] — tekst] 시작 버프 효과
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_title_22].content
   limit: do 120 znaków
   EN: Starter Buff Effects
   PL: Efekty wzmocnień początkowych
583. [Samouczek i wskazówki [tutorial_mainui_19_mirrordungeon_desc_22] — tekst] 시작 버프는 별빛이라는 재화를 통해 활성화할 수 있으며, 거울 던전을 진행할 때 도움을 줄 다양한 효과들을 활성화할 수 있습니다.\n별빛은 거울 던전을 플레이할 때 획득할 수 있습니다. 높은 층에 오를 수록 훨씬 많은 별빛을 획득할 수 있습니다.\n특정 거울 던전의 시작 버프는 보통 난이도와 어려움 난이도에 둘 다 적용되나, 다른 거울 던전에는 영향을 끼치지 않습니다.\n특정 거울 던전에서 획득하는 별빛은 다른 거울 던전의 시작 버프 활성화에는 사용할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_19_mirrordungeon_desc_22].content
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starter buffs can be activated using 'Starlight', providing various effects to aid your Mirror Dungeon expedition.\nStarlight can be earned by playing Mirror Dungeons. Reaching further floors rewards more.\nStarter buffs apply to both the Normal and Hard difficulties, but it does not affect other Mirror Dungeons.\nYou cannot use the Starlight from a Mirror Dungeon to activate starter buffs for other Mirror Dungeons.
   PL: Wzmocnienia początkowe odblokowujesz za walutę zwaną Gwiezdnym Blaskiem, zyskując rozmaite ułatwienia podczas wypraw do Lustrzanych Lochów.\nGwiezdny Blask zdobywasz za grę w Lustrzanych Lochach — im wyższe piętro osiągniesz, tym więcej go otrzymasz.\nWzmocnienia początkowe danego Lustrzanego Lochu działają zarówno na poziomie Normalnym, jak i Trudnym, lecz nie przechodzą na inne Lustrzane Lochy.\nGwiezdnego Blasku zdobytego w jednym Lustrzanym Lochu nie można użyć w innym.
584. [Samouczek i wskazówki [tutorial_mainui_20_umida_title] — tekst] 우.미.다
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_title].content
   limit: do 120 znaków
   EN: S.E.A.
   PL: M.O.R.Z.E.
585. [Samouczek i wskazówki [tutorial_mainui_20_umida_01_title_01] — tekst] 우.미.다 개방
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_01_title_01].content
   limit: do 120 znaków
   EN: Unlocking S.E.A
   PL: Odblokowanie M.O.R.Z.E.
586. [Samouczek i wskazówki [tutorial_mainui_20_umida_01_desc_01] — tekst] [우.미.다 이벤트 페이지]는 주요 이야기의 4-54를 클리어할 경우 개방됩니다.\n유리창이나 운전석에 있는 이벤트 배너를 통해 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_01_desc_01].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [S.E.A Event Page] opens after clearing Stage 4-54 of the Main Story.\nYou may enter the event page via the banner on the Window or the Driverside.
   PL: [Strona wydarzenia M.O.R.Z.E.] odblokowuje się po ukończeniu etapu 4-54 Głównej Opowieści.\nWejdziesz na nią przez baner wydarzenia w Oknie lub zakładce Jazda.
587. [Samouczek i wskazówki [tutorial_mainui_20_umida_02_title_01] — tekst] 이벤트 기간
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_02_title_01].content
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Samouczek i wskazówki [tutorial_mainui_20_umida_02_desc_01] — tekst] 우.미.다 이벤트 기간이 표시됩니다. 이벤트 기간 동안 우.미.다 혹은 주요 이야기의 스테이지와 던전을 클리어하여 [버스 개조용 폐품]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_02_desc_01].content
   limit: do 210 znaków
   EN: The duration of the S.E.A event is shown here. During the event, you can earn [Bus-modifying Scrap] by clearing Stages and Dungeons in the event and Main Story.
   PL: Wyświetla czas trwania wydarzenia M.O.R.Z.E. W tym okresie za ukończenie etapów i lochów wydarzenia oraz Głównej Opowieści zdobywasz [Złom do Przebudowy Autobusu].
589. [Samouczek i wskazówki [tutorial_mainui_20_umida_02_desc_02] — tekst] ※ 단, 거울 던전, 채광에서는 [버스 개조용 폐품]을 획득할 수 없습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_02_desc_02].content
   limit: do 120 znaków
   EN: ※ Mirror Dungeons and Luxcavation do not give [Bus-modifying Scrap].
   PL: ※ [Złomu do Przebudowy Autobusu] nie można zdobyć w Lustrzanych Lochach ani w Wydobyciu.
590. [Samouczek i wskazówki [tutorial_mainui_20_umida_03_title_01] — tekst] 이벤트 전투
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_03_title_01].content
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Samouczek i wskazówki [tutorial_mainui_20_umida_03_desc_01] — tekst] 우.미.다 전투는 스토리 스테이지를 포함하여 총 12개의 스테이지로 구성됩니다.\n우.미.다 전투에서는 클리어 보상과 별개로 EX 클리어 보상으로 [버스 개조용 폐품]을 획득할 수 있습니다. (1회 한정)
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_03_desc_01].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: S.E.A consists of 12 stages, including story stages.\nSaid stages also offer batches of [Bus-modifying Scrap] as a first-time EX Clear bonus.
   PL: M.O.R.Z.E. obejmuje łącznie 12 etapów wraz z odcinkami fabularnymi.
Pierwsze ukończenie z warunkiem EX zapewnia dodatkowy [Złom do Przebudowy Autobusu] (1 raz).
592. [Samouczek i wskazówki [tutorial_mainui_20_umida_03_desc_02] — tekst] 우.미.다 스테이지에서는 주요 이야기의 스테이지보다 훨씬 많은 [버스 개조용 폐품]을 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_03_desc_02].content
   limit: do 140 znaków
   EN: You can earn considerably more [Bus-modifying Scrap] from S.E.A stages compared to Main Story stages.
   PL: Etapy M.O.R.Z.E. zapewniają znacznie więcej [Złomu do Przebudowy Autobusu] niż etapy Głównej Opowieści.
593. [Samouczek i wskazówki [tutorial_mainui_20_umida_04_title_01] — tekst] 이벤트 특화 대상
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_04_title_01].content
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Samouczek i wskazówki [tutorial_mainui_20_umida_04_desc_01] — tekst] 우.미.다 이벤트 인격 또는 E.G.O를 편성하여 스테이지, 던전을 클리어하면 [버스 개조용 폐품]의 획득량이 상승합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_04_desc_01].content
   limit: do 180 znaków
   EN: Having Identities and E.G.O from S.E.A event on your team increases the amount of [Bus-modifying Scrap] earned from stages and dungeons.
   PL: Wystawienie w składzie Tożsamości lub E.G.O z wydarzenia M.O.R.Z.E. zwiększa ilość [Złomu do Przebudowy Autobusu] zdobywanego za etapy i lochy.
595. [Samouczek i wskazówki [tutorial_mainui_20_umida_05_title_01] — tekst] 폐품 수집함
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_05_title_01].content
   limit: do 120 znaków
   EN: Scrap Box
   PL: Pojemnik na Złom
596. [Samouczek i wskazówki [tutorial_mainui_20_umida_05_desc_01] — tekst] 획득한 [버스 개조용 폐품]의 수에 비례하여 [폐품 수집함]에서 다양한 보상을 얻을 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_05_desc_01].content
   limit: do 140 znaków
   EN: You can redeem various rewards from the [Scrap Box] based on the number of [Bus-modifying Scrap] you have.
   PL: W [Pojemniku na Złom] odbierzesz rozmaite nagrody w zależności od ilości zebranego [Złomu do Przebudowy Autobusu].
597. [Samouczek i wskazówki [tutorial_mainui_20_umida_06_title_01] — tekst] 폐품 수집함
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_06_title_01].content
   (powtórzenie elementu 595 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Samouczek i wskazówki [tutorial_mainui_20_umida_06_desc_01] — tekst] [폐품 수집함] 페이지에서 각종 재화와 이벤트 배포 인격, E.G.O를 획득할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_06_desc_01].content
   limit: do 140 znaków
   EN: You can acquire event reward Identities and E.G.O, as well as various currencies from the [Scrap Box].
   PL: Na stronie [Pojemnika na Złom] zdobędziesz różnorodne zasoby oraz darmową Tożsamość i E.G.O wydarzenia.
599. [Samouczek i wskazówki [tutorial_mainui_20_umida_06_desc_02] — tekst] [폐품 수집함] 에서 보상을 수령할 수 있는 기간이 표시됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_06_desc_02].content
   limit: do 120 znaków
   EN: The [Scrap Box]’s open duration is shown here.
   PL: Wskazuje okres, w którym można odbierać nagrody z [Pojemnika na Złom].
600. [Samouczek i wskazówki [tutorial_mainui_20_umida_07_title_01] — tekst] 이벤트 스테이지
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_07_title_01].content
   limit: do 120 znaków
   EN: Event Stages
   PL: Etap specjalny wydarzenia
601. [Samouczek i wskazówki [tutorial_mainui_20_umida_07_desc_01] — tekst] 우.미.다에서는 던전이 등장하지 않으며, 대신 다른 스테이지보다 더 많은 [버스 개조용 폐품]을 얻을 수 있는 특수 스테이지가 등장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_07_desc_01].content
   limit: do 170 znaków
   EN: S.E.A does not feature a dungeon; instead, there's a special stage where you can earn larger amounts of [Bus-modifying Scrap].
   PL: W M.O.R.Z.E. nie ma lochu — zamiast niego pojawia się etap specjalny zapewniający znacznie więcej [Złomu do Przebudowy Autobusu] niż pozostałe etapy.
602. [Samouczek i wskazówki [tutorial_mainui_20_umida_07_desc_02] — tekst] 특수 스테이지는 엔케팔린 모듈을 소모합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_07_desc_02].content
   limit: do 120 znaków
   EN: The special stage costs Enkephalin Modules to enter.
   PL: Wejście na etap specjalny zużywa Moduły Enkefaliny.
603. [Samouczek i wskazówki [tutorial_mainui_20_umida_08_title_01] — tekst] 희귀한 말굽이 포함된 버스 개조용 폐품
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_08_title_01].content
   limit: do 120 znaków
   EN: Rare Horseshoe with Bus-modifying Scrap
   PL: Złom do Przebudowy Autobusu z Rzadką Podkową
604. [Samouczek i wskazówki [tutorial_mainui_20_umida_08_desc_01] — tekst] 전투에서 승리할 경우, 낮은 확률로 [희귀한 말굽이 포함된 버스 개조용 폐품]을 획득할 수 있습니다.\n획득한 [희귀한 말굽이 포함된 버스 개조용 폐품]은 [버스 개조용 폐품] 20개로 자동 변환됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_08_desc_01].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After winning a battle, you have a small chance to find [Rare Horseshoe with Bus-modifying Scrap].\nThe [Rare Horseshoe with Bus-modifying Scrap] is automatically converted to 20 [Bus-modifying Scrap].
   PL: Po wygranej walce masz niewielką szansę na zdobycie [Złomu do Przebudowy Autobusu z Rzadką Podkową].\nZdobyty przedmiot jest automatycznie zamieniany na 20 szt. [Złomu do Przebudowy Autobusu].
605. [Samouczek i wskazówki [tutorial_mainui_20_umida_09_title_01] — tekst] 이벤트 이후
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_09_title_01].content
   (powtórzenie elementu 520 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Samouczek i wskazówki [tutorial_mainui_20_umida_09_desc_01] — tekst] 이벤트가 종료된 이후에도 운전석과 상영관을 통해 언제든지 우.미.다 전투를 다시 즐기거나 스토리를 다시 감상할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_20_umida_09_desc_01].content
   limit: do 230 znaków
   EN: Even after the event fully ends, you will be able to experience combat encounters in S.E.A and view its story anytime at the Driverside - [Deviazione] and Theater - [Detour Tales].
   PL: Nawet po zakończeniu wydarzenia walki oraz fabułę M.O.R.Z.E. możesz w każdej chwili odtworzyć w zakładkach Jazda oraz Teatr.
607. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_01_title_01] — tekst] 입장 방법
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_01_title_01].content
   limit: do 120 znaków
   EN: How to Enter
   PL: Sposób wejścia
608. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_01_desc_01] — tekst] 거울굴절철도 2호선은 입장 시 재화를 소모하지 않습니다. 노선을 선택하여 입장할 수 있습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_01_desc_01].content
   limit: do 120 znaków
   EN: Refraction Railway 2 does not consume resources to play. Select a Line to enter.
   PL: Wejście na Linię 2 Kolei Załamania nie zużywa zasobów. Wybierz linię, aby rozpocząć przejazd.
609. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_02_title_01] — tekst] 편성
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_02_title_01].content
   limit: do 120 znaków
   EN: Team
   PL: Skład
610. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_02_desc_01] — tekst] 입장 시, 보유한 인격과 E.G.O를 선택하여 편성합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_02_desc_01].content
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_03_desc_01] — tekst] 편성은 스테이지 진행 도중에 교체할 수 없으며, 다른 전투 콘텐츠와 달리 편성 이후에 진행된 레벨업이나 동기화, 환상 해석은 해당 편성에 반영되지 않습니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_03_desc_01].content
   limit: do 330 znaków
   EN: You cannot change your loadout while the expedition is in progress. Unlike other combat-based content, the level-ups and tier-ups done to your Identities and E.G.O while an expedition is in progress will not be immediately reflected on your team’s status.
   PL: Składu nie można zmieniać w trakcie przejazdu, a w odróżnieniu od pozostałych trybów bojowych późniejsze podnoszenie poziomów, Synchronizacja ani Splot Nici nie wpływają na zatwierdzony już skład.
612. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_04_title_01] — tekst] 2호선 역
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_04_title_01].content
   limit: do 120 znaków
   EN: Line 2 Stations
   PL: Stacje Linii 2
613. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_04_desc_01] — tekst] 거울굴절철도 2호선은 총 9개의 역으로 구성됩니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_04_desc_01].content
   limit: do 120 znaków
   EN: Refraction Railway Line 2 consists of 9 Stations.
   PL: Linia 2 Kolei Załamania składa się łącznie z 9 stacji.
614. [Samouczek i wskazówki [tutorial_mainui_21_railway2_page_05_desc_01] — tekst] 역을 선택하여 입장합니다.
   źródło: TutorialMainUIText.json :: dataList[id=tutorial_mainui_21_railway2_page_05_desc_01].content
   limit: do 120 znaków
   EN: Select the Station to enter.
   PL: Wybierz stację, aby rozpocząć walkę.
