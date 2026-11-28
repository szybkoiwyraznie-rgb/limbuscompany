# Paczka AI P32 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 3/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P32_2b_przedmioty_sklep_wydarzenia_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P32_2b_przedmioty_sklep_wydarzenia_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Interfejs i ustawienia: UI_Mission_MirrorDungeon8Event
- plik gry: `UI_Mission_MirrorDungeon8Event.json`

1. [Interfejs i ustawienia [mission_ui_condition_tags_201003041] — tekst] 클리어 시점에 시지프 소속 인격이 5명 이상 편성된 상태로 거울 던전 5층 이상 클리어 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003041].content
   limit: do 200 znaków
   EN: Clear Mirror Dungeon at Floor 5 or higher with 5 or more Sisyphe Identities in your Loadout at the time of completion (incompletable by Rental Teams)
   PL: Ukończ Lustrzane Lochy na piętrze 5 lub wyższym, mając w składzie co najmniej 5 Tożsamości Sisyphe w momencie ukończenia (nieosiągalne przy składzie wypożyczonym)
2. [Interfejs i ustawienia [mission_ui_condition_tags_201003042] — tekst] 클리어 시점에 엄지 소속 인격이 2명 이상 편성된 상태로 거울 던전 5층 이상 클리어 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003042].content
   limit: do 200 znaków
   EN: Clear Mirror Dungeon at Floor 5 or higher with 2 or more The Thumb Identities in your Loadout at the time of completion (incompletable by Rental Teams)
   PL: Ukończ Lustrzane Lochy na piętrze 5 lub wyższym, mając w składzie co najmniej 2 Tożsamości Kciuka w momencie ukończenia (nieosiągalne przy składzie wypożyczonym)
3. [Interfejs i ustawienia [mission_ui_condition_tags_201003043] — tekst] ‘오트쿠튀르::르누아르 브랜드 매니저 돈키호테’ 인격을 포함한 르누아르 소속 인격을 3명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘탐식의 재림’ 테마팩의 보스 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003043].content
   limit: do 280 znaków
   EN: Defeat the "Readvent of Gluttony" Theme Pack boss with 3 or more Le Noir Identities, including "Haute Couture::Le Noir Brand Manager Don Quixote" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossa Pakietu Tematycznego „Powrót Obżarstwa”, mając w składzie (bez liczenia rezerwy) co najmniej 3 Tożsamości Le Noir, w tym „Haute Couture::Menedżerka Marki Le Noir Don Quixote”
4. [Interfejs i ustawienia [mission_ui_condition_tags_201003044] — tekst] ‘오트쿠튀르::르루주 붉은 신 싱클레어’ 인격을 포함한 르루주 소속 인격을 3명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘보존의 신념’ 테마팩의 보스 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003044].content
   limit: do 290 znaków
   EN: Defeat the "Creed of Preservation" Theme Pack boss with 3 or more Le Rouge Identities, including "Haute Couture::The Crimson God of Le Rouge Sinclair" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossa Pakietu Tematycznego „Wiara w Zachowanie”, mając w składzie (bez liczenia rezerwy) co najmniej 3 Tożsamości Le Rouge, w tym „Haute Couture::Szkarłatny Bóg Le Rouge Sinclair”
5. [Interfejs i ustawienia [mission_ui_condition_tags_201003045] — tekst] ‘료. 고. 파. 주방장 료슈’, ‘료. 고. 파. 조수 그레고르’ 인격을 2명 편성한 상태(대기인원은 포함하지 않음)에서 ‘헬스치킨’ 테마팩의 보스 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003045].content
   limit: do 250 znaków
   EN: Defeat the "Hell's Chicken" Theme Pack boss with "R.B. Chef de Cuisine Ryōshū" and "R.B. Sous-chef Gregor" Identities in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossa Pakietu Tematycznego „Piekielny Kurczak”, mając w składzie (bez liczenia rezerwy) 2 Tożsamości: „Szef kuchni R.P.M. Ryōshū” i „Sous-chef R.P.M. Gregor”
6. [Interfejs i ustawienia [mission_ui_condition_tags_201003046] — tekst] 어금니 사무소 소속 인격을 4명 편성한 상태(대기인원은 포함하지 않음)에서 ‘우.미.다’ 테마팩의 보스 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003046].content
   limit: do 190 znaków
   EN: Defeat the "S.E.A." Theme Pack boss with 4 Molar Office Identities in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossa Pakietu Tematycznego „M.O.R.Z.E.”, mając w składzie (bez liczenia rezerwy) 4 Tożsamości Biura Trzonowca
7. [Interfejs i ustawienia [mission_ui_condition_tags_201003047] — tekst] 클리어 시점에 사무소 및 공방 소속 해결사 인격이 6명 이상 편성된 상태로 거울 던전 5층 이상 클리어 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003047].content
   limit: do 210 znaków
   EN: Clear Mirror Dungeon at Floor 5 or higher with 6 or more Office or Workshop Identities in your Loadout at the time of completion (Incompletable by Rental Teams)
   PL: Ukończ Lustrzane Lochy na piętrze 5 lub wyższym, mając w składzie co najmniej 6 Tożsamości Fikserów z Biur lub Warsztatów w momencie ukończenia (nieosiągalne przy składzie wypożyczonym)
8. [Interfejs i ustawienia [mission_ui_condition_tags_201003048] — tekst] ‘피쿼드호 선장 이스마엘’ 인격을 포함한 피쿼드호 소속 인격을 3명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘기어오는 심연’, ‘악으로 규정되는’, ‘우.미.다 게.판’ 테마팩의 보스 3종 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003048].content
   limit: do 310 znaków
   EN: Defeat the "Crawling Abyss", "The Evil Defining", and "S.E.A. C.R" Theme Pack bosses with 3 or more of The Pequod Identities, including "The Pequod Captain Ishmael" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossów Pakietów Tematycznych „Pełznąca Otchłań”, „Naznaczające Zło” i „M.O.R.Z.E. C.R”, mając w składzie (bez liczenia rezerwy) co najmniej 3 Tożsamości Pequoda, w tym „Kapitan Pequoda Ishmael”
9. [Interfejs i ustawienia [mission_ui_condition_tags_201003049] — tekst] ‘흑운회 부조장 그레고르’ 인격을 포함한 흑운회 소속 인격을 6명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘육참골단 BokGak’ 테마팩의 보스 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003049].content
   limit: do 300 znaków
   EN: Defeat the "Yield My Flesh to Claim Their Bones BokGak" Theme Pack boss with 6 or more of Kurokumo Clan Identities, including "Kurokumo Clan Captain Gregor" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossa Pakietu Tematycznego „Oddam Ciało, by Złamać Ich Kości BokGak”, mając w składzie (bez liczenia rezerwy) co najmniej 6 Tożsamości Klanu Kurokumo, w tym „Kapitan Klanu Kurokumo Gregor”
10. [Interfejs i ustawienia [mission_ui_condition_tags_201003050] — tekst] ‘검계 우두머리 뫼르소’ 인격을 포함한 검계 소속 인격을 6명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘탄환이 찍은 마침표’, ‘육참골단 BokGak’, ‘경험기억’ 테마팩의 보스 3종 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003050].content
   limit: do 370 znaków
   EN: Defeat the "Full-Stopped by a Bullet", "Yield My Flesh to Claim Their Bones BokGak", and "Mnestic Experience" Theme Pack bosses with 6 or more of Blade Lineage Identities, including "Blade Lineage Mentor Meursault" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossów Pakietów Tematycznych „Kropka Postawiona Kulą”, „Oddam Ciało, by Złamać Ich Kości BokGak” i „Pamięć Doświadczenia”, mając w składzie (bez liczenia rezerwy) co najmniej 6 Tożsamości Rodu Ostrza, w tym „Mentor Rodu Ostrza Meursault”
11. [Interfejs i ustawienia [mission_ui_condition_tags_201003051] — tekst] ‘홍원 군주 홍루’, ‘가주 후보 이스마엘’ 인격을 포함한 H사 소속 인격을 7명 이상 편성한 상태(대기인원은 포함하지 않음)에서 ‘심야청소’, ‘사대 가문과 욕망’, ‘바라볼 수밖에 없는’, ‘절차탁춘’ 테마팩의 보스 4종 처치 (대여 편성으로 클리어 불가)
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201003051].content
   limit: do 410 znaków
   EN: Defeat the "Nocturnal Sweeping", "Four Houses and Greed", "The Surrendered Witnessing", and "Spring Cultivation" Theme Pack bosses with 7 or more of H Corp. Identities, including "The Lord of Hongyuan Hong Lu" and "Family Hierarch Candidate Ishmael" in your Loadout (not counting Backup Units; incompletable by Rental Teams)
   PL: Pokonaj bossów Pakietów Tematycznych „Nocne Sprzątanie”, „Cztery Rody i Chciwość”, „Skazany na Patrzenie” i „Wiosenny Szlif”, mając w składzie (bez liczenia rezerwy) co najmniej 7 Tożsamości H Corp., w tym „Władca Hongyuan Hong Lu” i „Kandydatka na Głowę Rodu Ishmael”
12. [Interfejs i ustawienia [mission_ui_condition_tags_201005101] — tekst] 조합 E.G.O 기프트 없이 거울 던전 {0}층 이상 클리어
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Floor {0} or higher of Mirror Dungeon without any Fusion E.G.O Gifts
   PL: Ukończ piętro {0} lub wyższy Lustrzanych Loch bez Darów E.G.O Fuzji
13. [Interfejs i ustawienia [mission_ui_condition_tags_201005014] — tekst] 한 턴에 인격 6명 이상이 모두 속도 12 이상 달성
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005014].content
   limit: do 120 znaków
   EN: Have 6 or more Identities reach 12+ Speed in the same turn
   PL: Spraw, by co najmniej 6 Tożsamości osiągnęło w jednej turze Szybkość 12 lub wyższą
14. [Interfejs i ustawienia [mission_ui_condition_tags_201005015] — tekst] 한 턴에 모든 아군이 공격 스킬로 충전 횟수를 총합 {0} 이상 소모하기
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005015].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Consume a combined total of {0} or more Charge Count with all allies' Attack Skills in a single turn
   PL: Zużyj w jednej turze Umiejętnościami ataku wszystkich sojuszników łącznie {0} lub więcej Licznika
15. [Interfejs i ustawienia [mission_ui_condition_tags_201005019] — tekst] 한 턴에 적 1명에게 진동 {0}종류 이상 진폭 변환
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005019].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Perform {0} or more different Tremor Amplitude Conversions on a single enemy in one turn
   PL: Wykonaj {0} lub więcej różnych Konwersji Amplitudy Wstrząsu na jednym wrogu w jednej turze
16. [Interfejs i ustawienia [mission_ui_condition_tags_201005016] — tekst] 한 전투에서 원호 방어 전용 스킬을 {0}회 이상 사용한 채로 전투 클리어
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005016].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Win a battle after using Assist Defense exclusive Skills {0} or more times in that battle
   PL: Wygraj walkę, używając w niej {0} lub więcej razy Umiejętność wyłącznie Obrony Wsparcia
17. [Interfejs i ustawienia [mission_ui_condition_tags_201005017] — tekst] 한 턴에 한 수감자가 보호막 {0} 이상 얻기
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005017].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Have a single Sinner gain {0} or more Shield in one turn
   PL: Spraw, by jeden Skazaniec zdobył w jednej turze {0} lub więcej Tarczy
18. [Interfejs i ustawienia [mission_ui_condition_tags_201005018] — tekst] 환상체 ‘나는 비워내느니’ 전투 중 ‘업보’를 통해 적을 {0}명 처치
   źródło: UI_Mission_MirrorDungeon8Event.json :: dataList[id=mission_ui_condition_tags_201005018].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Kill {0} enemies via the "Karma" effect during battle against the Abnormality "My Form Empties"
   PL: Pokonaj {0} wrogów przez efekt „Karma” w walce z Anomalią „Forma, Którą Wypełnia Pustka”

## Interfejs i ustawienia: UI_Mission_NewReturnUserEvent
- plik gry: `UI_Mission_NewReturnUserEvent.json`

19. [Interfejs i ustawienia [mission_ui_condition_tags_103001001] — tekst] 1장 이후의 임의의 스토리 스테이지 누적 {0}회 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103001001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Past Canto I, clear any {0} Story Stages
   PL: Ukończ łącznie {0} dowolnych etapów fabularnych po Cant I
20. [Interfejs i ustawienia [mission_ui_condition_tags_103002001] — tekst] 경험치 채광 누적 {0}회 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103002001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear EXP Luxcavation a total of {0} time(s)
   PL: Ukończ łącznie {0} razy Wydobycie PD
21. [Interfejs i ustawienia [mission_ui_condition_tags_103003001] — tekst] 끈 채광 누적 {0}회 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103003001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Thread Luxcavation a total of {0} time(s)
   PL: Ukończ łącznie {0} razy Wydobycie Nici
22. [Interfejs i ustawienia [mission_ui_condition_tags_103004001] — tekst] 거울 던전 노드(전투 스테이지 노드) {0}개 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103004001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear {0} Mirror Dungeon (combat)Nodes
   PL: Ukończ {0} Węzłów Lustrzanych Loch (węzły walki)
23. [Interfejs i ustawienia [mission_ui_condition_tags_103004002] — tekst] 거울 던전 노말 이상 난이도를 최소 {0}층까지 도달한 후 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103004002].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear a Mirror Dungeon (Normal or higher difficulty) after reaching Floor {0}
   PL: Ukończ Lustrzane Lochy (poziom Normalny lub wyższy), osiągnąwszy piętro {0}
24. [Interfejs i ustawienia [mission_ui_condition_tags_103004003] — tekst] 거울 던전 노말 이상 난이도를 최소 {0}층까지 도달한 후 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103004003].content
   (powtórzenie elementu 23 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Interfejs i ustawienia [mission_ui_condition_tags_103004004] — tekst] 거울 던전 노말 이상 난이도 {0}회 클리어\n(마지막 층 보스전까지 클리어 필요)
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103004004].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Clear a Mirror Dungeon (Normal or harder) {0} time(s)\n(Must finish the final floor boss fight as well)
   PL: Ukończ Lustrzane Lochy (poziom Normalny lub wyższy) {0} razy\n(Trzeba pokonać bossa ostatniego piętra)
26. [Interfejs i ustawienia [mission_ui_condition_tags_103005001] — tekst] 임의의 인격 {0}명 {1}레벨 달성
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103005001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Level up {0} Identity(Identities) to Level {1}
   PL: Podnieś {0} dowolnych Tożsamości do poziomu {1}
27. [Interfejs i ustawienia [mission_ui_condition_tags_103005002] — tekst] 기본 인격이 아닌 임의의 인격 {0}명 동기화 {1}단계 달성
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103005002].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} non-LCB Sinner Identity(Identities) to Uptie Tier {1}
   PL: Podnieś {0} Tożsamości (poza bazowymi Skazańcami) do Stopnia Synchronizacji {1}
28. [Interfejs i ustawienia [mission_ui_condition_tags_103005003] — tekst] 임의의 인격 {0}명 동기화 {1}단계 달성
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103005003].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie any {0} Identity(Identities) to Uptie Tier {1}
   PL: Podnieś {0} dowolnych Tożsamości do Stopnia Synchronizacji {1}
29. [Interfejs i ustawienia [mission_ui_condition_tags_103005004] — tekst] 임의의 E.G.O {0}개 환상 해석 {1}단계 달성
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103005004].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Threadspin any {0} E.G.O to Threadspin Tier {1}
   PL: Podnieś {0} dowolnych E.G.O do Stopnia Splotu Nici {1}
30. [Interfejs i ustawienia [mission_ui_condition_tags_103006001] — tekst] 일일 미션 {0}개 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103006001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear {0} Daily Missions
   PL: Ukończ {0} misji dziennych
31. [Interfejs i ustawienia [mission_ui_condition_tags_103006002] — tekst] 주간 미션 {0}개 클리어
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_ui_condition_tags_103006002].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear {0} Weekly Missions
   PL: Ukończ {0} misji tygodniowych
32. [Interfejs i ustawienia [mission_condition_ui_group_2] — tekst] 스토리 스테이지
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_2].content
   limit: do 120 znaków
   EN: Story Stages
   PL: Etapów fabularnych
33. [Interfejs i ustawienia [mission_condition_ui_group_3] — tekst] 경험치 채광
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_3].content
   limit: do 120 znaków
   EN: EXP Luxcavation
   PL: Kopalnia PD
34. [Interfejs i ustawienia [mission_condition_ui_group_4] — tekst] 끈 채광
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_4].content
   limit: do 120 znaków
   EN: Thread Luxcavation
   PL: Kopalnia Nici
35. [Interfejs i ustawienia [mission_condition_ui_group_6] — tekst] 거울 던전
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_6].content
   limit: do 120 znaków
   EN: Mirror Dungeon
   PL: Lustrzane Lochy
36. [Interfejs i ustawienia [mission_condition_ui_group_8] — tekst] 육성
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_8].content
   limit: do 120 znaków
   EN: Upgrading
   PL: Ulepszanie
37. [Interfejs i ustawienia [mission_condition_ui_group_11] — tekst] 배틀 패스
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_condition_ui_group_11].content
   limit: do 120 znaków
   EN: Battle Pass
   PL: Przepustka Bojowa
38. [Interfejs i ustawienia [return_user_remain_Luxcavation_bonus] — tekst] 잔여 일일 복귀 보너스
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=return_user_remain_Luxcavation_bonus].content
   limit: do 120 znaków
   EN: Remaining Daily Bonuses for Returnees
   PL: Pozostałe dzienne bonusy Powrotu
39. [Interfejs i ustawienia [move_to_luxcavation] — tekst] 채광으로 이동
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=move_to_luxcavation].content
   limit: do 120 znaków
   EN: Go to Luxcavations
   PL: Przejdź do Wydobycia
40. [Interfejs i ustawienia [move_to_shop] — tekst] 상점으로 이동
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=move_to_shop].content
   limit: do 120 znaków
   EN: Go to Shop
   PL: Przejdź do Sklepu
41. [Interfejs i ustawienia [information_about_luxcavation] — tekst] 채광 보너스 안내
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=information_about_luxcavation].content
   limit: do 120 znaków
   EN: About Lux. Bonus
   PL: Informacje o bonusie Wydobycia
42. [Interfejs i ustawienia [information_about_returning_user_package] — tekst] 복귀 한정 패키지 안내
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=information_about_returning_user_package].content
   limit: do 120 znaków
   EN: About the Back to Office Pack
   PL: Informacje o Pakiecie „Powrót do Biura”
43. [Interfejs i ustawienia [information_about_returning_user_package_desc] — tekst] 이벤트 기간 동안 복귀 한정 패키지를\n상점에서 구매하실 수 있습니다.
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=information_about_returning_user_package_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During the Event period, the Back to Office Pack\nwill become available from the Shop.
   PL: W okresie wydarzenia Pakiet „Powrót do Biura”\nbędzie dostępny w Sklepie.
44. [Interfejs i ustawienia [returning_user_exp_luxcavation_bonus_desc] — tekst] 경험치 채광 일일 보너스 횟수 : {0} 회
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_exp_luxcavation_bonus_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Exp Lux. Daily Bonus Count : {0}
   PL: Dzienny bonus Wydobycia PD: {0}
45. [Interfejs i ustawienia [returning_user_thread_luxcavation_bonus_desc] — tekst] 끈 채광 일일 보너스 횟수 : {0} 회
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_thread_luxcavation_bonus_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thread Lux. Daily Bonus Count : {0}
   PL: Dzienny bonus Wydobycia Nici: {0}
46. [Interfejs i ustawienia [returning_user_luxcavation_bonus_desc] — tekst] 이벤트 기간 동안 채광 클리어 시 기본 보상을 추가로 획득할 수 있습니다.
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_luxcavation_bonus_desc].content
   limit: do 120 znaków
   EN: You can obtain bonus Luxcavation rewards during the Event period.
   PL: W okresie wydarzenia ukończenie Wydobycia daje dodatkowe nagrody bazowe.
47. [Interfejs i ustawienia [returning_user_mission] — tekst] 복귀 미션
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_mission].content
   limit: do 120 znaków
   EN: Returning Manager Missions
   PL: Misje Powrotu
48. [Interfejs i ustawienia [attendance_check] — tekst] 출석 체크
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=attendance_check].content
   limit: do 120 znaków
   EN: Attendance Check
   PL: Lista obecności
49. [Interfejs i ustawienia [welcome_returning_user] — tekst] 업무 복귀를 환영합니다. 관리자님!
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=welcome_returning_user].content
   limit: do 120 znaków
   EN: Welcome back to the office, Manager!
   PL: Witamy z powrotem w biurze, Panie Menedżerze!
50. [Interfejs i ustawienia [luxcavation_bonus_and_package] — tekst] 채광 보너스&패키지
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=luxcavation_bonus_and_package].content
   limit: do 120 znaków
   EN: Luxcavation Bonus & Pack
   PL: Bonus i Pakiet Wydobycia
51. [Interfejs i ustawienia [until_event_finish_date] — tekst] 이벤트 종료까지 {0}일 남음
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=until_event_finish_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Days until the end of Event
   PL: Do końca wydarzenia: {0} dni
52. [Interfejs i ustawienia [event_for_new_user_from_date] — tekst] 대상 : <color=#990000>{2}년 {0}월 {1}일</color> 12:00(KST) 이후 신규 생성된 계정
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=event_for_new_user_from_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {2}, {0}, {1}
   EN: For : new accounts created after <color=#990000>{0}/{1}/{2}</color>, 12:00(KST)
   PL: Dotyczy: kont utworzonych po <color=#990000>{0}.{1}.{2}</color>, 12:00 (KST)
53. [Interfejs i ustawienia [mission_progress_rate] — tekst] 미션 진행도
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=mission_progress_rate].content
   limit: do 120 znaków
   EN: Mission Progress
   PL: Postęp misji
54. [Interfejs i ustawienia [welcome_returing_user_title] — tekst] 복귀 지원\n물품 지급
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=welcome_returing_user_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Work Re-adjustment\nResources
   PL: Przystosowanie do pracy\nZasoby
55. [Interfejs i ustawienia [welcome_returing_user_desc] — tekst] 관리자님의 복귀를 환영합니다.
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=welcome_returing_user_desc].content
   limit: do 120 znaków
   EN: Welcome back to the office, Manager.
   PL: Witamy z powrotem w biurze, Panie Menedżerze.
56. [Interfejs i ustawienia [returning_user_attendance_check_title] — tekst] 복귀 관리자님을 위한 출석 체크 이벤트
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_attendance_check_title].content
   limit: do 120 znaków
   EN: Roll Call for our returning Manager
   PL: Lista obecności dla powracającego Menedżera
57. [Interfejs i ustawienia [returning_user_attendance_check_desc] — tekst] ※ 이벤트 기간 동안 누적 출석 일수에 따라 보상을 획득할 수 있습니다.\n\n※ 일간 초기화를 기준으로 서버 통신이 진행되면 당일 출석한 것으로 인정됩니다.
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=returning_user_attendance_check_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Collect more attendance checks and unlock greater rewards.\n\n※ Log in after the daily reset period and receive your daily attendance checks.
   PL: ※ W okresie wydarzenia nagrody zależą od łącznej liczby dni logowania.\n\n※ Logowanie po dziennym resecie serwera uznawane jest za obecność danego dnia.
58. [Interfejs i ustawienia [complete_to_receive] — tekst] 수령 완료
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=complete_to_receive].content
   limit: do 120 znaków
   EN: Claimed
   PL: Odebrano
59. [Interfejs i ustawienia [already_owned] — tekst] 보유 중
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=already_owned].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
60. [Interfejs i ustawienia [move_shortcut] — tekst] 바로가기
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=move_shortcut].content
   limit: do 120 znaków
   EN: Go to
   PL: Przejdź do
61. [Interfejs i ustawienia [warning_about_change_season_item] — tekst] 시즌 4 동기화, 환상해석 전용 파편 아이템은 새로운 시즌이 시작될 때 절반으로 감소한 뒤 이월되는 아이템입니다.\n그래도 수령하시겠습니까?
   źródło: UI_Mission_NewReturnUserEvent.json :: dataList[id=warning_about_change_season_item].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When a new Season starts, only half of your stock of 'Season 4 Uptie & Threadspinning only Shard' will be migrated to the upcoming Season.\nClaim them anyway?
   PL: Po rozpoczęciu nowego sezonu tylko połowa zapasu „Odłamków wyłącznie na Synchronizację i Splot Nici Sezonu 4” zostanie przeniesiona do nadchodzącego sezonu.\nOdebrać mimo to?

## Interfejs i ustawienia: UI_ModuleDevice
- plik gry: `UI_ModuleDevice.json`

62. [Interfejs i ustawienia [select_personality_gacksung_up_ticket] — tekst] 상승 도약 인격 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_personality_gacksung_up_ticket].content
   limit: do 120 znaków
   EN: Select Identity to Takeoff
   PL: Wybierz Tożsamość do Skoku Rozwoju
63. [Interfejs i ustawienia [tip_long_click_to_view_personality] — tekst] ※ 길게 터치하면 인격의 상세 정보를 확인할 수 있습니다.
   źródło: UI_ModuleDevice.json :: dataList[id=tip_long_click_to_view_personality].content
   limit: do 120 znaków
   EN: ※ Long-press an Identity to view more detailed info.
   PL: ※ Przytrzymaj Tożsamość, aby zobaczyć szczegółowe informacje.
64. [Interfejs i ustawienia [leap_up_confim_main_only_gacksung] — tekst] [{0}] 인격의 동기화 단계가 다음과 같이 변경됩니다.
   źródło: UI_ModuleDevice.json :: dataList[id=leap_up_confim_main_only_gacksung].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0}] Identity's Uptie Tier will be changed as follows.
   PL: Stopień Synchronizacji Tożsamości [{0}] zmieni się następująco.
65. [Interfejs i ustawienia [select_ego_gacksung_up_ticket] — tekst] 상승 도약 E.G.O 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_ego_gacksung_up_ticket].content
   limit: do 120 znaków
   EN: Select E.G.O to Takeoff
   PL: Wybierz E.G.O do Skoku Rozwoju
66. [Interfejs i ustawienia [tip_long_click_to_view_ego] — tekst] ※ 길게 터치하면 E.G.O의 상세 정보를 확인할 수 있습니다.
   źródło: UI_ModuleDevice.json :: dataList[id=tip_long_click_to_view_ego].content
   limit: do 120 znaków
   EN: ※ Long-press an E.G.O to view more detailed info.
   PL: ※ Przytrzymaj E.G.O, aby zobaczyć szczegółowe informacje.
67. [Interfejs i ustawienia [ego_leap_up_confim_main_only_gacksung] — tekst] [{0}] E.G.O의 환상 해석 단계가 다음과 같이 변경됩니다.
   źródło: UI_ModuleDevice.json :: dataList[id=ego_leap_up_confim_main_only_gacksung].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0}] E.G.O's Threadspinning Tier will be changed as follows.
   PL: Stopień Splotu Nici E.G.O [{0}] zmieni się następująco.
68. [Interfejs i ustawienia [all_egos] — tekst] 전체 E.G.O
   źródło: UI_ModuleDevice.json :: dataList[id=all_egos].content
   limit: do 120 znaków
   EN: All E.G.Os
   PL: Wszystkie E.G.O
69. [Interfejs i ustawienia [leap_up_able_uptie_ego_tier] — tekst] 환상 해석 단계 상승 가능
   źródło: UI_ModuleDevice.json :: dataList[id=leap_up_able_uptie_ego_tier].content
   limit: do 120 znaków
   EN: Can be Threadspun
   PL: Można podnieść Stopień Splotu Nici
70. [Interfejs i ustawienia [ego_gacksung_grade] — tekst] 환상 해석 단계
   źródło: UI_ModuleDevice.json :: dataList[id=ego_gacksung_grade].content
   limit: do 120 znaków
   EN: Threadspin Tier
   PL: Stopień Splotu Nici
71. [Interfejs i ustawienia [leap_up_ego_confim_title] — tekst] E.G.O 선택
   źródło: UI_ModuleDevice.json :: dataList[id=leap_up_ego_confim_title].content
   limit: do 120 znaków
   EN: Selecting E.G.O
   PL: Wybór E.G.O
72. [Interfejs i ustawienia [check_default_personality_leap_up] — tekst] 선택한 인격은 주요 이야기 진행을 통해 동기화 단계를 최대 3단계까지 재화 소모 없이 상승시킬 수 있습니다.\n\n그럼에도 동기화를 진행하시겠습니까?
   źródło: UI_ModuleDevice.json :: dataList[id=check_default_personality_leap_up].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is an Identity that can be Uptied for free to Tier 3 by progressing through the Main Story.\n\nUptie this Identity anyway?
   PL: Tę Tożsamość można podnieść do Stopnia 3 Synchronizacji bezkosztowo, postępując w Głównej Fabule.\n\nCzy mimo to przeprowadzić Synchronizację?
73. [Interfejs i ustawienia [check_default_ego_leap_up] — tekst] 선택한 E.G.O는 주요 이야기 진행을 통해 환상 해석 단계를 최대 3단계까지 재화 소모 없이 상승시킬 수 있습니다.\n\n그럼에도 환상 해석을 진행하시겠습니까?
   źródło: UI_ModuleDevice.json :: dataList[id=check_default_ego_leap_up].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is an E.G.O that can be Threadspun for free to Tier 3 by progressing through the Main Story.\n\nUptie this Identity anyway?
   PL: To E.G.O można podnieść do Stopnia 3 Splotu Nici bezkosztowo, postępując w Głównej Fabule.\n\nCzy mimo to przeprowadzić Splot Nici?
74. [Interfejs i ustawienia [select_identity_popup_title] — tekst] 인격 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_identity_popup_title].content
   limit: do 120 znaków
   EN: Select Identity
   PL: Wybór Tożsamości
75. [Interfejs i ustawienia [select_identity_popup_title_season_1] — tekst] 시즌 1 인격 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_identity_popup_title_season_1].content
   limit: do 120 znaków
   EN: Select Season 1 Identity
   PL: Wybór Tożsamości Sezonu 1
76. [Interfejs i ustawienia [select_ego_popup_title_season_1_battlepass] — tekst] 시즌 1 배틀 패스 E.G.O 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_ego_popup_title_season_1_battlepass].content
   limit: do 120 znaków
   EN: Select Season 1 Battle Pass E.G.O
   PL: Wybór E.G.O Przepustki Bojowej Sezonu 1
77. [Interfejs i ustawienia [select_ego_popup_title] — tekst] E.G.O 선택
   źródło: UI_ModuleDevice.json :: dataList[id=select_ego_popup_title].content
   limit: do 120 znaków
   EN: Select E.G.O
   PL: Wybór E.G.O

## Interfejs i ustawienia: UI_x1p1c1
- plik gry: `UI_x1p1c1.json`

78. [Interfejs i ustawienia [fools_2026_entrance_popup_title] — tekst] 한봄 밤의 꿈 3
   źródło: UI_x1p1c1.json :: dataList[id=fools_2026_entrance_popup_title].content
   limit: do 120 znaków
   EN: A Midspring Night's Dream 3
   PL: Sen Środkowowiosennej Nocy 3
79. [Interfejs i ustawienia [fools_2026_entrance_popup_desc] — tekst] 한봄 밤의 꿈 3 스토리에 입장하시겠습니까?
   źródło: UI_x1p1c1.json :: dataList[id=fools_2026_entrance_popup_desc].content
   limit: do 120 znaków
   EN: Enter A Midspring Night's Dream 3 Story?
   PL: Wejść do fabuły „Sen Środkowowiosennej Nocy 3”?
80. [Interfejs i ustawienia [fools_2026_entrance_popup_desc_not_cleared_target_chapter] — tekst] 한봄 밤의 꿈 3 스토리에 입장하시겠습니까?\n\n<size=35>※ 진행 기간 : 2026.04.01 00:00 ~ 04.09 00:00 (KST) \n\n<color=#b01c37>※주의 : 해당 스토리는 9장 끊어지지 않는 챕터의 스포일러가 포함되어있습니다.</color></size>
   źródło: UI_x1p1c1.json :: dataList[id=fools_2026_entrance_popup_desc_not_cleared_target_chapter].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <size=35>, <color=#b01c37>, </color>, </size>, \n
   EN: Enter A Midspring Night's Dream 3 Story?\n\n<size=35>※ Event Period: 2026.04.01 00:00 ~ 04.09 00:00 (KST)\n\n\n<color=#b01c37>※ WARNING: The following story contains spoilers for Canto IX: The Unsevering.</color></size>
   PL: Wejść do fabuły „Sen Środkowowiosennej Nocy 3”?\n\n<size=35>※ Czas trwania: 2026.04.01 00:00 ~ 04.09 00:00 (KST) \n\n<color=#b01c37>※Uwaga: ta fabuła zawiera spoilery Cant IX: The Unsevering.</color></size>

## Interfejs i ustawienia: UserAgreements
- plik gry: `UserAgreements.json`

81. [Interfejs i ustawienia [UserAgreement_popup_title] — tekst] 서비스 이용약관
   źródło: UserAgreements.json :: dataList[id=UserAgreement_popup_title].content
   limit: do 120 znaków
   EN: Terms of Service
   PL: Regulamin Usługi
82. [Interfejs i ustawienia [UserAgreement_title] — tekst] 이용 약관
   źródło: UserAgreements.json :: dataList[id=UserAgreement_title].content
   limit: do 120 znaków
   EN: User Agreement
   PL: Warunki korzystania
83. [Interfejs i ustawienia [UserAgreement_personality_title] — tekst] 개인 정보 수집 및 이용에 대한 안내
   źródło: UserAgreements.json :: dataList[id=UserAgreement_personality_title].content
   limit: do 120 znaków
   EN: Information and Privacy Policy
   PL: Informacje o gromadzeniu i wykorzystaniu danych osobowych
84. [Interfejs i ustawienia [UserAgreement_agreed] — tekst] 동의합니다.
   źródło: UserAgreements.json :: dataList[id=UserAgreement_agreed].content
   limit: do 120 znaków
   EN: I agree.
   PL: Zgadzam się.

## Samouczek i wskazówki: BattleResultHint-a1c10p1
- plik gry: `BattleResultHint-a1c10p1.json`

85. [Samouczek i wskazówki [battleTip_11006_1] — tekst] 리나모비블은 일정 주기로 탈의실에 들어갔다 나오기를 반복합니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11006_1].content
   limit: do 120 znaków
   EN: L'Inamovible will enter and leave the Changing Room in intervals.
   PL: L'Inamovible wchodzi do Przymierzalni i wychodzi z niej w stałych odstępach czasu.
86. [Samouczek i wskazówki [battleTip_11006_2] — tekst] 리나모비블이 탈의실에 들어갔을 때 공격하면 공격성이 증가합니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11006_2].content
   limit: do 120 znaków
   EN: Attacking L'Inamovible while she is in the Changing Room will increase her aggressiveness.
   PL: Atakowanie L'Inamovible, gdy przebywa w Przymierzalni, zwiększa jej agresywność.
87. [Samouczek i wskazówki [battleTip_11008_1] — tekst] 수셰프는 처치한 대상으로 '토막난 요리재료'를 얻고, 턴이 끝날 때 이를 먹어 '맛있는거 먹고 힘난다는거예요'를 쌓습니다.\n수치가 쌓일수록 강력한 스킬 '제 시그니쳐인 거예요'가 빨라지고 강해집니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11008_1].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sous Chef gains "Chopped Ingredients" from units she kills. These are consumed at the end of the turn, granting her stacks of "Eat yummies and perk up, you hear?".\n\nThe more she gets the stacks, the stronger and more frequent will her powerful move, "My signature knife work, you hear?", become.
   PL: Sous-chef zdobywa „Pokrojone Składniki” od pokonanych celów. Na koniec tury zjada je, kumulując „Zjadam przysmaki i nabieram sił, słyszysz?”.\nIm więcej stosów, tym silniejsza i częstsza jest jej potężna Umiejętność „Moje sygnaturowe cięcie, słyszysz?”
88. [Samouczek i wskazówki [battleTip_11008_2] — tekst] 수셰프는 자신의 가죽 지갑도 재료로 삼기 때문에, 수감자만 지켜서는 요리를 막을 수 없습니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11008_2].content
   limit: do 200 znaków
   EN: Leather Wallets are not an exception when it comes to Sous Chef's ingredient-gathering. You cannot stop her culinary activity by playing defensively.
   PL: Sous-chef traktuje jako składniki również Skórzane Portfele — sama defensywa Skazańców nie zatrzyma jej gotowania.
89. [Samouczek i wskazówki [battleTip_11008_3] — tekst] 수셰프가 아무도 처치하지 못한 턴에는 '배고픈 거예요'가 쌓입니다.\n수치가 3에 도달하면 또 다른 강력한 스킬을 사용하니, 한 번씩은 요리하도록 내버려 두는 것도 방법입니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11008_3].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When Sous Chef fails to kill any targets, she will get stacks of "Got an appetite, you hear?". \nAt 3 stacks, she will use <i>another</i> powerful Skill. It may be a good idea to let her continue cooking every once in a while.
   PL: W turze, gdy Sous-chef nie pokona nikogo, kumuluje „Mam apetyt, słyszysz?”.\nPrzy 3 stosach użyje kolejnej potężnej Umiejętności — czasem warto pozwolić jej ugotować
90. [Samouczek i wskazówki [battleTip_11010_1] — tekst] 플로어 매니저의 특정 스킬에는 공격 스킬을 사용하지 않는 것이 좋습니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11010_1].content
   limit: do 140 znaków
   EN: Sometimes, Clashing against the Floor Manager's certain skill with your Attack Skills could be a bad idea.
   PL: Czasem prowadzenie Starć z określonymi Umiejętnościami Menedżera Piętra przy użyciu Umiejętności ataku może być złym pomysłem.
91. [Samouczek i wskazówki [battleTip_11010_2] — tekst] '경계심'이 10에 도달할 경우 플로어 매니저가 강력한 스킬을 사용합니다.\n경계심이 쌓이지 않도록 주의하거나 특정 스킬에 합을 패배하면 경계심을 제거할 수 있습니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11010_2].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Be too wary and let yourself accumulate 10 stacks of "Guarded Caution", and you will risk inviting the Floor Manager's powerful Skill.\nPay attention so that "Guarded Caution" does not reach 10 stacks. You may also choose to lose a Clash against a certain Skill to remove the stacks.
   PL: Gdy „Czujność” osiągnie 10, Menedżer Piętra użyje potężnej Umiejętności.\nUważaj, by „Czujność” nie osiągnęła 10 stosów — albo przegraj Starcie z określoną Umiejętnością, by ją usunąć
92. [Samouczek i wskazówki [battleTip_11010_3] — tekst] '경청에 대한 감사'를 보유했다면 잠깐 동안 공격을 하지 않는 것도 방법입니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11010_3].content
   limit: do 130 znaków
   EN: If you have "Gratitude for Listening", perhaps you will want to stay your attacks for a short while.
   PL: Jeśli posiadasz „Wdzięczność za Wysłuchanie”, jednym ze sposobów jest też chwilowe wstrzymanie ataków.
93. [Samouczek i wskazówki [battleTip_11011_1] — tekst] 붉은 신[미생]의 생명줄은 매우 강력하기 때문에 먼저 파괴하는 것을 추천합니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11011_1].content
   limit: do 170 znaków
   EN: The Crimson God [Inchoate Life]'s Lifecord houses immense power. It may be a good idea to prioritize destroying it before all else.
   PL: Linka Życia Czerwonego Boga [Życie Zarodkowe] ma ogromną moc — zalecamy zniszczyć ją w pierwszej kolejności.
94. [Samouczek i wskazówki [battleTip_11011_2] — tekst] 붉은 신[미생]의 강력한 스킬에는 체력이 높은 아군으로 대응해야 합니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11011_2].content
   limit: do 120 znaków
   EN: Let a Sinner with high HP deal with the Crimson God [Inchoate Life]'s powerful Skill.
   PL: Potężne Umiejętności Czerwonego Boga [Życie Zarodkowe] powinien przejąć sojusznik o wysokim HP.
95. [Samouczek i wskazówki [battleTip_11011_3] — tekst] '세례[적]'이 쌓일 경우 수비 스킬을 사용하여 제거하는 것을 추천합니다. 최대로 쌓이면 큰 출혈 피해를 입게 되고 사망할 시 '붉은 신[미생]의 뜯긴 살점'이 적으로 생성됩니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11011_3].content
   limit: do 320 znaków
   EN: If your units are gaining too many "Baptism [Crimson]" Stacks, use Defense Skills to remove them. At max Stack, it causes a great deal of Bleed Damage, and the defeated unit will become an enemy—"Ripped Flesh of the Crimson God [Inchoate Life]."
   PL: Gdy stosy „Chrzest [Czerwień]” się nagromadzą, zalecamy usuwać je Umiejętnościami obrony. Przy maksimum czeka ogromne obrażenie od Krwawienia, a po śmierci na pole wchodzi „Rozdarte Ciało Czerwonego Boga [Życie Zarodkowe]”
96. [Samouczek i wskazówki [battleTip_11016_1] — tekst] 바늘못 수치가 높은 상태로 ‘피크스티치 일부러 눈에 띄게 박았냐고?! 그렇게 쳐박아주마!’ 스킬에 피격당하면 박제 상태가 되며 큰 피해를 받습니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11016_1].content
   limit: do 280 znaków
   EN: If you are hit by the "Pick stitch too obvious, you say?! I'll pick-stitch your ass!" Skill while you have accumulated many stacks of Naildle, you will enter the "Taxidermized" state and receive devastating damage.
   PL: Trafienie Umiejętnością „Ścieg tak rażąco widoczny, mówisz?! Wbiję ci go w tyłek!” przy wysokich stosach Igłogwoźdź zamieni cię w wypchanie i zada potworne obrażenia.
97. [Samouczek i wskazówki [battleTip_11016_2] — tekst] 바느질의 왕이 강력한 스킬을 사용하는 턴에 바늘이들이 생존해있다면 큰 피해를 받을 수 있습니다.
   źródło: BattleResultHint-a1c10p1.json :: dataList[id=battleTip_11016_2].content
   limit: do 190 znaków
   EN: If there are surviving Needlekins in the same turn as when the King of Needleworks uses a powerful Skill, they will enhance that Skill's damage.
   PL: W turze, w której Król Szycia używa potężnej Umiejętności, przeżyłe Igiełki mogą znacznie ją wzmocnić.

## Samouczek i wskazówki: BattleResultHint-a1c10p2
- plik gry: `BattleResultHint-a1c10p2.json`

98. [Samouczek i wskazówki [battleTip_11027_1] — tekst] 수선사 아네트가 지속적으로 얻는 보호막은 흐트러짐 상태가 되면 파괴됩니다. 진동 키워드를 사용하거나 공격 횟수가 많은 인격을 편성해보세요.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11027_1].content
   limit: do 240 znaków
   EN: Annette the Alterationist's Shield breaks when she becomes Staggered. Try using Tremor Identities or Identities that hit multiple times to break through Annette's Shield more efficiently.
   PL: Tarcza Annette the Alterationist pęka, gdy wpada w Oszołomienie. Spróbuj Tożsamości ze Wstrząsem albo wieloma atakami.
99. [Samouczek i wskazówki [battleTip_11027_2] — tekst] 수선사 아네트가 수선 대상에게 특수한 스킬을 사용할 때, 공격보다는 수비를 하는 것이 좋은 선택일 수 있습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11027_2].content
   limit: do 140 znaków
   EN: Defending may be safer than attacking when Annette uses her special Skill against an Alteration Target.
   PL: Gdy Annette the Alterationist używa specjalnej Umiejętności na obiekcie reperacji, obrona może być lepszym wyborem niż atak.
100. [Samouczek i wskazówki [battleTip_11028_1] — tekst] 패닉 상태가 되지 않도록 정신력 관리에 유의하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11028_1].content
   limit: do 120 znaków
   EN: Keep SP under control to avoid entering Panic.
   PL: Kontroluj Poczytalność, by nie wpaść w Panikę.
101. [Samouczek i wskazówki [battleTip_11028_2] — tekst] 속죄의 월계관 효과를 보유한 아군을 활용하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11028_2].content
   limit: do 120 znaków
   EN: Make good use of allies that have Laurel Wreath of Atonement.
   PL: Ważne jest wykorzystanie sojuszników z efektom Wieńca Laurowego Zadośćuczynienia.
102. [Samouczek i wskazówki [battleTip_11030_1] — tekst] 통제자가 무두질된 죄수를 소환할 때는 자신의 체력을 소모합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11030_1].content
   limit: do 120 znaków
   EN: The Overseer consumes its own HP whenever it summons a Tanned Prisoner.
   PL: Nadzorca zużywa własne HP za każdym razem, gdy przywołuje Wygarbowanego Więźnia.
103. [Samouczek i wskazówki [battleTip_11030_2] — tekst] 통제자의 통제를 따르지 않으면 통제자가 강력한 공격을 사용합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11030_2].content
   limit: do 120 znaków
   EN: Disobeying the Overseer's prohibitions causes it to retaliate with a powerful attack.
   PL: Nieposłuszeństwo wobec Nakazów Nadzorcy kończy się potężnym atakiem odwetowym.
104. [Samouczek i wskazówki [battleTip_11031_1] — tekst] 아군이 얻을 수 있는 '묵시적 형벌' 수치를 적당하게 분배하고 조절하세요. 특정 스킬에 받는 피해량을 대폭 낮출 수 있습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11031_1].content
   limit: do 220 znaków
   EN: Distribute "Apocalyptic Vengeance" Stacks across your allies instead of letting them pile up on one unit. Used well, they can greatly reduce damage from certain Skills.
   PL: Rozdzielaj i kontroluj stosy „Apokaliptycznej Zemsty” zdobywane przez sojuszników. Mogą one drastycznie obniżyć obrażenia od określonych Umiejętności.
105. [Samouczek i wskazówki [battleTip_11031_2] — tekst] 르누아르 브랜드 매니저가 사용하는 '언약' 스킬에 합을 승리하면, '계시' 스킬로 얻은 보호막을 크게 감소시킬 수 있습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11031_2].content
   limit: do 170 znaków
   EN: Winning a Clash against the Le Noir Brand Manager's "Covenant" Skill can greatly reduce the Shield it gains from "Revelation".
   PL: Wygranie Starcia z Umiejętnością „Przymierze” Menedżerki Marki Le Noir może znacznie obniżyć Tarczę zyskaną Umiejętnością „Objawienie”
106. [Samouczek i wskazówki [battleTip_11032_1] — tekst] 바늘못 수치가 높은 상태로 ‘피크스티치 일부러 눈에 띄게 박았냐고?! 그렇게 쳐박아주마!’ 스킬에 피격당하면 박제 상태가 되며 큰 피해를 받습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11032_1].content
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [Samouczek i wskazówki [battleTip_11032_2] — tekst] 바느질의 왕이 강력한 스킬을 사용하는 턴에 바늘이들이 생존해있다면 큰 피해를 받을 수 있습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11032_2].content
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Samouczek i wskazówki [battleTip_11033_1] — tekst] 수셰프는 처치한 대상으로 '토막난 요리재료'를 얻고, 턴이 끝날 때 이를 먹어 '맛있는거 먹고 힘난다는거예요'를 쌓습니다.\n수치가 쌓일수록 강력한 스킬 '제 시그니쳐인 거예요'가 빨라지고 강해집니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11033_1].content
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Samouczek i wskazówki [battleTip_11033_2] — tekst] 수셰프는 자신의 가죽 지갑도 재료로 삼기 때문에, 수감자만 지켜서는 요리를 막을 수 없습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11033_2].content
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Samouczek i wskazówki [battleTip_11033_3] — tekst] 수셰프가 아무도 처치하지 못한 턴에는 '배고픈 거예요'가 쌓입니다.\n수치가 3에 도달하면 또 다른 강력한 스킬을 사용하니, 한 번씩은 요리하도록 내버려 두는 것도 방법입니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11033_3].content
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Samouczek i wskazówki [battleTip_11034_1] — tekst] 플로어 매니저의 특정 스킬에는 공격 스킬을 사용하지 않는 것이 좋습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11034_1].content
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
112. [Samouczek i wskazówki [battleTip_11034_2] — tekst] '경계심'이 10에 도달할 경우 플로어 매니저가 강력한 스킬을 사용합니다.\n경계심이 쌓이지 않도록 주의하거나 특정 스킬에 합을 패배하면 경계심을 제거할 수 있습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11034_2].content
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Samouczek i wskazówki [battleTip_11034_3] — tekst] '경청에 대한 감사'를 보유했다면 잠깐 동안 공격을 하지 않는 것도 방법입니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11034_3].content
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Samouczek i wskazówki [battleTip_11038_1] — tekst] 뒤엉킴은 수치가 높을수록 받는 피해가 늘고 위력이 떨어지며, 15 이상일 때 특정 스킬에 피격되면 강제로 흐트러집니다.\n수비 스킬을 사용하거나 '씻어내기'와 합을 하여 뒤엉킴 수치를 조절하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11038_1].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Higher Stacks of "Tangling" increase damage taken and lowers Power. At 15+ Stacks, certain Skills can force Stagger on hit. Use Defense Skills or Clash against "Cleansing" to keep "Tangling" under control.
   PL: Im wyższe stosy „Splątania”, tym większe otrzymywane obrażenia i tym niższa Moc; przy 15 lub więcej określone Umiejętności wymuszają Oszołomienie.\nUżywaj Umiejętności obrony albo prowadź Starcia z „Zmywaniem”, by kontrolować „Splątanie”
115. [Samouczek i wskazówki [battleTip_11038_2] — tekst] '검은 물 웅덩이'는 피격 시 스킬당 1회만 감소하기 때문에, 가중치 스킬을 통해 한 번에 제거하는 것이 좋습니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11038_2].content
   limit: do 180 znaków
   EN: "Pool of Black Water" is lost only once per Skill when hit. Skills with high Atk Weight are the most efficient way to remove it in one go.
   PL: „Kałuża Czarnej Wody” maleje tylko raz na Umiejętność przy trafieniu — najlepiej usuń ją za jednym razem Umiejętnościami o dużej Wadze Ataku.
116. [Samouczek i wskazówki [battleTip_11038_3] — tekst] 옛 바다의 검은 실의 스킬 '무저갱의 아가리'는 대상이 흐트러진 상태이거나 뒤엉킴이 20 이상이면 대상에게 즉사급 피해를 입힙니다.\n속도와 관계없이 합을 걸 수 있는 스킬이니 수감자들의 뒤엉킴을 20 아래로 관리하고, 위험할 때는 반드시 합으로 막아내세요.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11038_3].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "Abyssal Maw," Blackthread of the Elden Sea's Skill, deals near-lethal damage if the target is Staggered or has 20+ "Tangling". It can be Clashed against regardless of Speed, so keep "Tangling" Stacks below 20 and always intercept it when a Sinner is at risk.
   PL: „Paszcza Otchłani”, Umiejętność Czarnej Nici Dawnego Morza, zadaje niemal śmiertelne obrażenia, gdy cel jest oszołomiony albo ma 20 lub więcej „Splątania”.\nBez względu na Szybkość można ją przejąć Starciem — trzymaj „Splątanie” Skazańców poniżej 20 i zawsze blokuj ją Starciem, gdy Skazaniec jest zagrożony
117. [Samouczek i wskazówki [battleTip_11040_1] — tekst] 퍼티의 속도를 조절하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11040_1].content
   limit: do 120 znaków
   EN: Keeping Putty's Speed under control is key to this fight.
   PL: Kluczem do tej walki jest kontrola Szybkości Putty.
118. [Samouczek i wskazówki [battleTip_11040_2] — tekst] 스킬이 파괴 불가 코인이 되지 않도록 유의하여 충전 횟수를 조절하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p2.json :: dataList[id=battleTip_11040_2].content
   limit: do 120 znaków
   EN: Manage Charge Count carefully so that Coins do not become Unbreakable.
   PL: Ostrożnie zarządzaj Licznikiem, by monety nie stały się Niezniszczalne.

## Samouczek i wskazówki: BattleResultHint-a1c10p3
- plik gry: `BattleResultHint-a1c10p3.json`

119. [Samouczek i wskazówki [battleTip_11039_phase1_1] — tekst] 시지프 백화점 설계도를 잔느의 포착 스킬로 처치 못하도록 먼저 처치 하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase1_1].content
   limit: do 160 znaków
   EN: Prioritize taking out the Grand Magasin Sisyphe Blueprints before Jeanne can finish them off with her "Focusing" Skill.
   PL: Ważne jest zniszczenie Schematów Grand Magasin Sisyphe, zanim Jeanne zdąży ich użyć Umiejętnością „Pojmania”
120. [Samouczek i wskazówki [battleTip_11039_phase1_2] — tekst] 잔느의 앙가즈망(engagement)이 활성화 되었을 때, 기본 위력이 높은 E.G.O 스킬로 합을 하는 것이 좋습니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase1_2].content
   limit: do 140 znaków
   EN: When Jeanne's "Engagement" effect is active, use an E.G.O Skill with high Base Power to Clash against her.
   PL: Gdy aktywny jest efekt „Engagement” (engagement) Jeanne, lepiej prowadzić Starcia Umiejętnością E.G.O o wysokiej Mocy bazowej.
121. [Samouczek i wskazówki [battleTip_11039_phase2_1] — tekst] 뫼르소의 체력을 관리하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase2_1].content
   limit: do 120 znaków
   EN: Keep a close eye on Meursault's HP.
   PL: Ważne jest pilnowanie HP Meursaulta.
122. [Samouczek i wskazówki [battleTip_11039_phase2_2] — tekst] 잔느의 의도에 맞게 스킬의 타겟을 지정할 필요가 있습니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase2_2].content
   limit: do 120 znaków
   EN: Pay attention to Jeanne's intended pattern when assigning Skill targets.
   PL: Przy wyborze celów Umiejętności trzeba stosować się do zamierzeń Jeanne.
123. [Samouczek i wskazówki [battleTip_11039_phase3_1] — tekst] 잔느의 스킬에 피격 시 수감자가 코인 앞면을 띄울 수 없으니 유의해야 합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase3_1].content
   limit: do 120 znaków
   EN: Be careful: Sinners hit by Jeanne's Skills cannot roll Heads.
   PL: Uwaga: Skazańcy trafieni Umiejętnościami Jeanne nie mogą wyrzucać Orłów.
124. [Samouczek i wskazówki [battleTip_11039_phase3_2] — tekst] 설계도를 처치하면 잔느의 체력이 감소하므로, 공격 가중치가 높은 E.G.O를 사용하여 빠르게 처치하는 것이 중요합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11039_phase3_2].content
   limit: do 150 znaków
   EN: Taking out the Blueprints reduces Jeanne's HP. Use E.G.O Skills with high Attack Weight to defeat them quickly.
   PL: Zniszczenie Schematów obniża HP Jeanne — ważne jest szybkie ich niszczenie Umiejętnościami E.G.O o dużej Wadze Ataku.
125. [Samouczek i wskazówki [battleTip_11041_1] — tekst] '라 주이상스'와의 합에서 승리할 때마다 붉은 신[완숙]은 '뿌이의 기억'을 얻고 약해집니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11041_1].content
   limit: do 160 znaków
   EN: Each time you win a Clash against "La Jouissance", The Crimson God [Adulthood] gains "Pwie's Memories" and becomes weaker.
   PL: Za każde wygrane Starcie z „La Jouissance” Czerwony Bóg [Dojrzałość] zyskuje „Wspomnienia Pwie” i słabnie.
126. [Samouczek i wskazówki [battleTip_11041_2] — tekst] '뿌이와의 경험'을 보유한 수감자는 붉은 신[완숙]에게 받는 피해가 줄고, 붉은 신[완숙]은 그 수감자에게 스킬을 사용할 때마다 정신력을 잃습니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11041_2].content
   limit: do 230 znaków
   EN: Sinners who have "Shared with Pwie" take less damage from The Crimson God [Adulthood], and The Crimson God [Adulthood] loses SP each time they use a Skill against the said Sinners.
   PL: Skazańcy z „Doświadczeniem z Pwie” otrzymują mniej obrażeń od Czerwonego Boga [Dojrzałość], a Bóg traci Poczytalność za każde trafienie Umiejętnością tego Skazańca.
127. [Samouczek i wskazówki [battleTip_11041_3] — tekst] '라브젝트(l'abject)'가 쌓이면 속도가 느려지고 출혈로 받는 피해가 커집니다.\n5 이상 쌓인 수감자는 붉은 신[완숙]의 강력한 추가 공격 대상이 되니 주의하세요.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11041_3].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: As L'Abject stacks, Speed decreases and damage taken from Bleed increases. Sinners with 5 or more Stacks become targets for The Crimson God [Adulthood]'s powerful additional attack. Exercise caution.
   PL: Kumulujące się stosy „L'Abject (l'abject)” obniżają Szybkość i zwiększają otrzymywane obrażenia od Krwawienia.\nSkazańcy z 5 lub więcej stosami to potencjalne cele potężnych dodatkowych ataków Czerwonego Boga [Dojrzałość] — zachowaj czujność
128. [Samouczek i wskazówki [battleTip_11036_phase1_1] — tekst] 속도가 1인 수감자가 간수의 스킬과 합을 진행하면, 위력과 피해량이 크게 증가하여 합을 이겨도 아프게 되니 유의해야 합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase1_1].content
   limit: do 180 znaków
   EN: If a Sinner with 1 Speed Clashes with the Warden's Skill, its Power and Damage increase greatly. Even winning the Clash will still hurt.
   PL: Uwaga: gdy Skazaniec o Szybkości 1 prowadzi Starcie z Umiejętnością Strażnika, Moc i obrażenia Strażnika mocno rosną — nawet wygrane Starcie boli.
129. [Samouczek i wskazówki [battleTip_11036_phase1_2] — tekst] 형벌 촛대가 생존하면, 턴 종료 시 다음 턴에 모든 수감자에게 속박을 부여하므로 1순위로 해치워야 합니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase1_2].content
   limit: do 150 znaków
   EN: If a Candle of Retribution survives, it inflicts Bind on all Sinners next turn at Turn End. Prioritize defeating it.
   PL: Przeżyła Świeca Odwety na koniec tury nakłada Spętanie na wszystkich Skazańców w następnej turze — likwiduj ją priorytetowo.
130. [Samouczek i wskazówki [battleTip_11036_phase2_1] — tekst] 간수의 특정 스킬은 박동 또는 정지 효과를 보유한 수감자로 합을 진행해야 크게 무력화됩니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase2_1].content
   limit: do 160 znaków
   EN: Certain Skills of the Warden can be greatly weakened by Clashing with Sinners who have "Thumping Pulse" or "Stillness".
   PL: Określone Umiejętności Strażnika można znacznie unieszkodliwić, prowadząc Starcia Skazańcami z efektom Tętnienia lub Zastoju.
131. [Samouczek i wskazówki [battleTip_11036_phase2_2] — tekst] 간수는 수감자를 공격할 때, 해당 수감자가 보유한 각종 못(고해의 증거)에 비례하여 강해집니다. 이를 신경쓰며 스킬을 대응해봅시다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase2_2].content
   limit: do 220 znaków
   EN: When attacking a Sinner, the Warden becomes stronger based on the various Nails (Proof of Confession) that Sinner has. Keep this in mind when responding to his Skills.
   PL: Atakując Skazańca, Strażnik staje się silniejszy proporcjonalnie do posiadanych przez niego Gwoździ (Dowodów Spowiedzi). Uwzględnij to, planując odpowiedź Umiejętnościami.
132. [Samouczek i wskazówki [battleTip_11036_phase3_1] — tekst] 신부의 특정 스킬은 박동 또는 정지 효과를 보유한 수감자로 합을 진행해야 크게 무력화됩니다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase3_1].content
   limit: do 160 znaków
   EN: Certain Skills of the Chaplain can be greatly weakened by Clashing with Sinners who have "Thumping Pulse" or "Stillness".
   PL: Określone Umiejętności Kapelana można znacznie unieszkodliwić, prowadząc Starcia Skazańcami z efektom Tętnienia lub Zastoju.
133. [Samouczek i wskazówki [battleTip_11036_phase3_2] — tekst] 신부는 수감자를 공격할 때, 해당 수감자가 보유한 각종 못(〜)에 비례하여 강해집니다. 이를 신경쓰며 스킬을 대응해봅시다.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase3_2].content
   limit: do 200 znaków
   EN: When attacking a Sinner, the Chaplain becomes stronger based on the various Nails (〜) that Sinner has. Keep this in mind when responding to his Skills.
   PL: Atakując Skazańca, Kapelan staje się silniejszy proporcjonalnie do posiadanych przez niego Gwoździ (〜). Uwzględnij to, planując odpowiedź Umiejętnościami.
134. [Samouczek i wskazówki [battleTip_11036_phase3_3] — tekst] 신부와의 전투 중에는 특정 동작을 할 경우, 수감자에게 못[Console]이 크게 쌓이고 약간의 체력 피해를 받게 됩니다. 이를 항상 주의하세요.
   źródło: BattleResultHint-a1c10p3.json :: dataList[id=battleTip_11036_phase3_3].content
   limit: do 230 znaków
   EN: During the fight against the Chaplain, certain actions cause Sinners to gain a large amount of Nail [Console] and take a small amount of HP damage. Keep this in mind at all times.
   PL: W walce z Kapelanem określone działania sprawiają, że Skazańcy gromadzą dużo Gwoździ [Console] i odnoszą niewielkie obrażenia HP. Zawsze na to uważaj.

## Samouczek i wskazówki: BattleResultHint-a1c9p1
- plik gry: `BattleResultHint-a1c9p1.json`

135. [Samouczek i wskazówki [battleTip_10903_1] — tekst] 아비의 명령으로 엄지 제자는 료슈에게 강한 일격을 날릴 수 없습니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10903_1].content
   limit: do 140 znaków
   EN: By the command of the Nursefather, the Thumb Apprentice is forbidden from using powerful attacks on Ryōshū.
   PL: Rozkazem Ojca Kciuka Uczeń Kciuka nie może wymierzyć silnego ciosu w Ryōshū.
136. [Samouczek i wskazówki [battleTip_10903_2] — tekst] 엄지 제자에게 동일한 수감자로 계속해서 합을 하는 것은 좋지 않습니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10903_2].content
   limit: do 120 znaków
   EN: Using the same Sinner to repeatedly Clash against the Thumb Apprentice is not recommended.
   PL: Nie zaleca się wielokrotnego prowadzenia Starć z Uczniem Kciuka tym samym Skazańcem.
137. [Samouczek i wskazówki [battleTip_10903_3] — tekst] 엄지 제자의 강력한 공격이 들어가기 전에 다른 공격 스킬 먼저 합으로 승리해야 합니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10903_3].content
   limit: do 150 znaków
   EN: Make sure to win Clashes against the Thumb Apprentice's other Attack Skills before he unleashes a deadlier Skill.
   PL: Zanim Uczeń Kciuka wyprowadzi potężniejszy atak, trzeba najpierw wygrać Starcia z jego pozostałymi Umiejętnościami ataku.
138. [Samouczek i wskazówki [battleTip_10910_1] — tekst] 열매 부위 파괴를 방해하는 부위를 우선적으로 파괴하는 것이 더 유리할 수도 있습니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10910_1].content
   limit: do 140 znaków
   EN: Prioritizing the Parts that interfere with destroying the Fruit can sometimes be the better strategy.
   PL: Priorytetowe niszczenie części przeszkadzających w zniszczeniu Owocu może być korzystniejszą strategią.
139. [Samouczek i wskazówki [battleTip_10910_2] — tekst] 수감자가 어느 부위를 타겟팅하고 있는지 파악하는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10910_2].content
   limit: do 120 znaków
   EN: It is important to keep track of which Part each Sinner is targeting.
   PL: Ważne jest śledzenie, którą część celuje każdy Skazaniec.
140. [Samouczek i wskazówki [battleTip_10910_3] — tekst] 착용한 E.G.O를 확인해 필요한 자원을 얻을 수 있는 인격으로 구성하여 전투를 진행해 봅시다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10910_3].content
   limit: do 150 znaków
   EN: Take into account what E.G.O you bring into your team so that you can gather the necessary resources more easily.
   PL: Sprawdź wyposażone E.G.O i dobierz do składu Tożsamości pozwalające sprawnie gromadzić potrzebne im zasoby w walce.
141. [Samouczek i wskazówki [battleTip_10918_phase1_1] — tekst] 소지 제자의 강력한 스킬에는 반드시 합을 이길 수 있도록 전략을 준비하세요.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10918_phase1_1].content
   limit: do 120 znaków
   EN: Prepare a strategy that can win Clashes against the Pinky Apprentice's deadlier Skills.
   PL: Przygotuj strategię, która wygra Starcia z zabójczymi Umiejętnościami Ucznia Małego Palca.
142. [Samouczek i wskazówki [battleTip_10918_phase1_2] — tekst] 가장 위험한 공격에 올바르게 대응하는 것이 모든 스킬에 합을 지정하는 것보다 중요합니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10918_phase1_2].content
   limit: do 150 znaków
   EN: Choosing the right way to handle the enemy's deadliest attacks matters more than assigning Clashes to every slot.
   PL: Właściwa reakcja na najgroźniejsze ataki jest ważniejsza niż przypisywanie Starć do każdego slotu.
143. [Samouczek i wskazówki [battleTip_10918_phase2_1] — tekst] 약지 제자의 강력한 공격은 합 대신 다른 방법으로 약화시킬 수 있습니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10918_phase2_1].content
   limit: do 120 znaków
   EN: Clashing is not the only way to weaken the Ring Apprentice's most dangerous Skill.
   PL: Najgroźniejszą Umiejętność Uczennicy Serdecznego można osłabić także inaczej niż Starciem.
144. [Samouczek i wskazówki [battleTip_10918_phase2_2] — tekst] 약지 제자의 수비는 출혈을 부여하니 신중하게 공격할 필요가 있습니다.
   źródło: BattleResultHint-a1c9p1.json :: dataList[id=battleTip_10918_phase2_2].content
   limit: do 120 znaków
   EN: The Ring Apprentice's Defense Skill inflicts Bleed—exercise caution when Clashing with it.
   PL: Obrona Uczennicy Serdecznego nakłada Krwawienie — prowadź z nią Starcia ostrożnie.

## Samouczek i wskazówki: BattleResultHint-a1c9p2
- plik gry: `BattleResultHint-a1c9p2.json`

145. [Samouczek i wskazówki [battleTip_10925_1] — tekst] 대응하지 못할 땐 수비적으로 행동하는 것이 더 유리할 수도 있습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10925_1].content
   limit: do 130 znaków
   EN: If the enemy's attacks cannot be met head-on, going on the defensive might be the better strategy.
   PL: Gdy ataków wroga nie da się przyjąć frontalnie, gra defensywna może być lepszą strategią.
146. [Samouczek i wskazówki [battleTip_10925_2] — tekst] 보호하고 있는 부위를 파괴해 약점을 노리는 전략이 유리할 수도 있습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10925_2].content
   limit: do 140 znaków
   EN: Sometimes, destroying a protected Part to capitalize on the enemy's weaknesses can be a sound strategy.
   PL: Niszczenie chronionej części, by trafić w słabość, może być skuteczną taktyką.
147. [Samouczek i wskazówki [battleTip_10925_3] — tekst] 착용한 E.G.O를 확인해 필요한 자원을 얻을 수 있는 인격으로 구성하여 전투를 진행해 봅시다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10925_3].content
   limit: do 190 znaków
   EN: Check the E.G.O your Sinners have equipped and their required resources to form a team of Identities that can efficiently gather them in battle.
   PL: Sprawdź wyposażone E.G.O i dobierz do składu Tożsamości pozwalające sprawnie gromadzić potrzebne im zasoby w walce.
148. [Samouczek i wskazówki [battleTip_10928_1] — tekst] 약점 부위의 내성을 파악하고 공략하는 것이 더 유리할 수도 있습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10928_1].content
   limit: do 120 znaków
   EN: Identifying the Resistance values on the enemy's weak Part might be the better strategy.
   PL: Rozpoznanie odporności słabej części wroga może być lepszą strategią.
149. [Samouczek i wskazówki [battleTip_10928_2] — tekst] E.G.O를 적절한 타이밍에 사용하는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10928_2].content
   limit: do 120 znaków
   EN: It is important to identify the situations in which E.G.O Skills are most effective.
   PL: Ważne jest używanie E.G.O we właściwych momentach.
150. [Samouczek i wskazówki [battleTip_10928_3] — tekst] 착용한 E.G.O를 확인해 필요한 자원을 얻을 수 있는 인격으로 구성하여 전투를 진행해 봅시다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10928_3].content
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Samouczek i wskazówki [battleTip_10930_1] — tekst] 검지 제자 소라는 지령을 달성하지 못하면 카르마가 증가합니다. 지령의 내용을 확인하고 지령을 수행하지 못하도록 방해해봅시다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10930_1].content
   limit: do 230 znaków
   EN: The Index Apprentice Sora gains Karmic Consequence if she fails to fulfill the Prescript. Make sure to check which Prescript she has received and prevent her from executing it.
   PL: Gdy Uczennica Wskazującego Sora nie zrealizuje Nakazu, zyskuje Karma. Sprawdź treść Nakazu i przeszkadzaj w jego wykonaniu.
152. [Samouczek i wskazówki [battleTip_10930_2] — tekst] 초반 단계 지령을 방해하기 위해, 지령 대상이 있는 수감자는 되도록 소라의 첫 번째 슬롯 스킬과 합을 하지 않는 것이 좋습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10930_2].content
   limit: do 250 znaków
   EN: To prevent the execution of The Index Apprentice Sora's early-phase Prescript, it is best for Sinners inflicted with "The Prescript's Target" to avoid Clashing with Sora's first Skill Slot.
   PL: Aby zablokować wczesne Nakazy, Skazańcy z „Celem Nakazu” powinni unikać Starć z Umiejętnością pierwszego slotu Sory.
153. [Samouczek i wskazówki [battleTip_10930_3] — tekst] 료슈가 보유한 버프에는 숨겨진 특수한 효과가 있습니다. 검지 제자의 특정 공격이 지나치게 까다로울 때, 료슈로 대응해봅시다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10930_3].content
   limit: do 220 znaków
   EN: Ryōshū's has a hidden, unique effect in this Encounter. If a certain attack used by the Index Apprentice is difficult to overcome, try commanding Ryōshū against her.
   PL: Buff Ryōshū kryje ukryty efekt specjalny. Gdy określony atak Uczennicy Wskazującej okaże się zbyt trudny, odpowiedz Ryōshū.
154. [Samouczek i wskazówki [battleTip_10933_1] — tekst] ‘관망’ 스킬에 대응하여 이번 턴의 위력을 낮춰 불리한 상황을 타개할 수 있습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10933_1].content
   limit: do 130 znaków
   EN: Examine the "Silent Regard" Skill—it provides a way to lower the enemy's Power for this turn.
   PL: Przyjrzyj się Umiejętności „Wyczekiwanie” — pozwala obniżyć Moc wroga w tej turze.
155. [Samouczek i wskazówki [battleTip_10933_2] — tekst] 고유 디버프인 ‘검흔[잔상]’은 ‘잔상보[殘像步]’스킬에 대응하여 수치를 대폭 감소시킬 수 있습니다.
   źródło: BattleResultHint-a1c9p2.json :: dataList[id=battleTip_10933_2].content
   limit: do 160 znaków
   EN: Examine the "Phantom Step [殘像步]" Skill—it may have a way to mitigate the enemy's unique debuff, "Bladetrail [Afterimage]."
   PL: Przyjrzyj się Umiejętności „Krok Powidła [殘像步]” — może złagodzić unikalny debuff wroga „Ślad Ostrza [Powidło]”.

## Samouczek i wskazówki: BattleResultHint-a1c9p3
- plik gry: `BattleResultHint-a1c9p3.json`

156. [Samouczek i wskazówki [battleTip_10937_1] — tekst] 호엔하임과 알리사가 수감자보다 먼저 쓰러지지 않도록 주의해야 합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10937_1].content
   limit: do 120 znaków
   EN: Make sure that Hohenheim and Alyssa are not defeated before the Sinners.
   PL: Uważaj, by Hohenheim i Alyssa nie zginęli przed Skazańcami.
157. [Samouczek i wskazówki [battleTip_10937_2] — tekst] 약지 아비의 스킬 중 반드시 합을 이겨야 하는 스킬에 집중하는 것이 좋습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10937_2].content
   limit: do 120 znaków
   EN: It is recommended to focus on the Ring Nursefather's Skills whose Clashes must be won.
   PL: Zaleca się skupienie na Umiejętnościach Ojca Serdecznego, których Starć trzeba wygrać za wszelką cenę.
158. [Samouczek i wskazówki [battleTip_10937_3] — tekst] 약지 아비와 제자의 강력한 공격은 합을 진행하기 전에 다른 방법으로 약화시킬 수 있습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10937_3].content
   limit: do 120 znaków
   EN: The Ring Nursefather and his Apprentice's powerful Skills can be weakened before Clashing.
   PL: Potężne ataki Ojca Serdecznego i jego Ucznia można osłabić jeszcze przed Starciem.
159. [Samouczek i wskazówki [battleTip_10943_1] — tekst] 상대적으로 합을 이기기 쉬운 스킬을 선택해 합을 시도하는 것이 좋습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10943_1].content
   limit: do 120 znaków
   EN: It is recommended to attempt Clashes with Skills that are relatively easier to win.
   PL: Zaleca się próby Starć Umiejętnościami, które stosunkowo łatwo wygrać.
160. [Samouczek i wskazówki [battleTip_10943_2] — tekst] 체력이 낮은 적부터 우선적으로 처치하는 것이 좋습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10943_2].content
   limit: do 120 znaków
   EN: Try prioritizing enemies with low HP first.
   PL: Zaleca się priorytetowe eliminowanie wrogów o niskim HP.
161. [Samouczek i wskazówki [battleTip_10938_1] — tekst] 아비는 수감자가 상대하기 어려운 적입니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10938_1].content
   limit: do 120 znaków
   EN: Nursefathers are difficult enemies for the Sinners.
   PL: Ojcowie są trudnymi przeciwnikami dla Skazańców.
162. [Samouczek i wskazówki [battleTip_10938_2] — tekst] 베스파와 에즈라의 원호 방어를 적극적으로 활용하는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10938_2].content
   limit: do 120 znaków
   EN: It is important to make use of Vespa and Ezra's Assist Defense.
   PL: Ważne jest aktywne wykorzystywanie Obrony Wsparcia Vespy i Ezry.
163. [Samouczek i wskazówki [battleTip_10942_phase1_1] — tekst] 엄지 제자가 강력한 스킬을 사용하기 전에 다른 수감자들로 먼저 합을 진행하여 스킬을 약화시키세요.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10942_phase1_1].content
   limit: do 120 znaków
   EN: Use the Sinners to Clash with The Thumb Apprentice's Skills to weaken his powerful Skill.
   PL: Zanim Uczeń Kciuka użyje potężnej Umiejętności, osłabij ją, prowadząc Starcia innymi Skazańcami.
164. [Samouczek i wskazówki [battleTip_10942_phase1_2] — tekst] 엄지 제자의 체력을 절반 이하로 감소시켜야 합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10942_phase1_2].content
   limit: do 120 znaków
   EN: Reduce The Thumb Apprentice's HP to below half.
   PL: Trzeba obniżyć HP Ucznia Kciuka poniżej połowy.
165. [Samouczek i wskazówki [battleTip_10942_phase2_1] — tekst] 엄지 제자가 조력자의 공격을 방해하고 있습니다.\n수감자들로 엄지 제자를 먼저 공략하는 것이 좋습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10942_phase2_1].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Thumb Apprentice is interfering with the Assist Units' attacks.\nIt is recommended to focus the Sinners' attacks on The Thumb Apprentice first.
   PL: Uczeń Kciuka przeszkadza atakom jednostek wspierających.\nZaleca się najpierw skupić ataki Skazańców na Uczniu Kciuka.
166. [Samouczek i wskazówki [battleTip_10942_phase2_2] — tekst] 엄지 아비는 공격을 받을 때 예지안을 소모하여 회피 스킬을 사용합니다.\n조력자를 활용해 예지안을 지속적으로 소모시키는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10942_phase2_2].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When attacked, The Thumb Nursefather consumes her "Eye of Precognition" Stack to evade.\nIt is important to have the non-Sinner ally constantly drain her Eye of Precognition Stack.
   PL: Przy ataku Ojciec Kciuka zużywa stos Oko Prekognicji, by użyć Umiejętności uniku.\nWażne jest nieustanne wyczerpywanie Oko Prekognicji przez jednostki wspierające.
167. [Samouczek i wskazówki [battleTip_10942_phase2_3] — tekst] 엄지 아비의 강력한 스킬은 대상을 변경할 수 없습니다.\n해당 스킬은 예지안을 소모할수록 약화되므로, 스킬 발동 전에 예지안을 최대한 소모시키는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10942_phase2_3].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You cannot redirect The Thumb Nursefather's powerful Skill.\nMake sure to drain her Eye of Precognition as much as possible before the Skill is activated; the fewer Eye of Precognition Stacks she has, the weaker the Skill becomes.
   PL: Potężnej Umiejętności Ojca Kciuka nie można przekierować.\nOsłabia się wraz ze zużywaniem Oko Prekognicji — wyczerpij je maksymalnie przed aktywacją Umiejętności
168. [Samouczek i wskazówki [battleTip_10944_1] — tekst] 베스파와 에즈라의 원호 방어를 활용하는 것이 중요합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10944_1].content
   limit: do 120 znaków
   EN: It is important to make use of Vespa and Ezra's Assist Defense.
   PL: Ważne jest wykorzystywanie Obrony Wsparcia Vespy i Ezry.
169. [Samouczek i wskazówki [battleTip_10944_2] — tekst] 일방 공격으로 적을 흐트러뜨릴 수 있는 타이밍을 전략적으로 활용하세요.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10944_2].content
   limit: do 130 znaków
   EN: Strategize appropriately and make use of the opportunity to Stagger enemies with Unopposed Attacks.
   PL: Taktycznie wykorzystaj momenty, w których atak jednostronny pozwala oszołomić wrogów.
170. [Samouczek i wskazówki [battleTip_10944_3] — tekst] 적이 궁지에 몰려 강해지면, 무리하게 합을 진행하기보다는 버티는 데 집중하여 조력자의 비장의 한 수를 기다리세요.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10944_3].content
   limit: do 200 znaków
   EN: When enemies are cornered and become stronger, focus on buying time rather than winning Clashes, and wait for the Assist Units to play their trump card.
   PL: Gdy wrogowie w kącie stają się silniejsi, skup się na przetrwaniu, a nie na Starciach — czekaj na asy jednostek wspierających.
171. [Samouczek i wskazówki [battleTip_10945_1] — tekst] 바퀴 황제는 수감자와의 합에서 이길수록 약해집니다.\n단, 모든 공격을 수감자가 받아내는 것은 위험합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10945_1].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The more The Roach Emperor wins his Clashes against the Sinners, the weaker he gets.\nHowever, it is a very risky decision to have the Sinners deal with all of his Skills on their own.
   PL: Im więcej Starych wygrywa Cesarz Karaluchów ze Skazańcami, tym słabszy się staje.\nJednak przyjmowanie wszystkich ataków przez Skazańców jest ryzykowne.
172. [Samouczek i wskazówki [battleTip_10945_2] — tekst] 공격 해충[바퀴]가 많이 누적되었다면 바퀴 황제의 `황제의 포식` 스킬에 피격되어 수치를 낮출 수도 있습니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10945_2].content
   limit: do 150 znaków
   EN: "Hurting Pest [Roaches]" Stacks can be lowered by letting The Roach Emperor's "Emperor's Devouring" Skill hit you.
   PL: Stosy „Raniącego Szkodnika [Karaluchy]” można obniżyć, przyjmując trafienie Umiejętnością Cesarza Karaluchów „Pożeranie Cesarza”
173. [Samouczek i wskazówki [battleTip_10945_3] — tekst] 바퀴 황제의 적출 코인을 가진 스킬은 파괴 불가 코인을 보유한 스킬을 대상으로 아주 강력해집니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10945_3].content
   limit: do 130 znaków
   EN: The Roach Emperor's Excision Coin Skills become much stronger against Skills with Unbreakable Coins.
   PL: Umiejętności Cesarza Karaluchów z Monetą Odcięcia stają się bardzo silne przeciwko Umiejętnościom z Niezniszczalnymi Monetami.
174. [Samouczek i wskazówki [battleTip_10941_1] — tekst] `확정된 상대` 스킬에 합이 가능한 수감자를 확인해 적절한 공격을 명령하고, 소지 아비에게 피해를 누적시키세요.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10941_1].content
   limit: do 190 znaków
   EN: Check for Sinners that can Clash against 'Destinated Opponent' Skill with suitable Attack Skills, and build up damage on The Pinky Nursefather.
   PL: Sprawdź, którzy Skazańcy mogą prowadzić Starcia z Umiejętnością „Gwarantowany Przeciwnik”, wydaj odpowiednie rozkazy ataku i kumuluj obrażenia na Ojcu Małego Palca.
175. [Samouczek i wskazówki [battleTip_10941_2] — tekst] 상황에 따라 소지 아비의 어떤 스킬에 먼저 합을 진행할지에 대한 임기응변이 중요합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10941_2].content
   limit: do 180 znaków
   EN: Depending on the situation, it is important to plan impromptu and decide on which of The Pinky Nursefather's Skills should be Clashed first.
   PL: W zależności od sytuacji ważna jest improwizacja: z którą Umiejętnością Ojca Małego Palca prowadzić Starcie najpierw.
176. [Samouczek i wskazówki [battleTip_10948_1] — tekst] 전투 상황에서 아군이 유리하면 소지 아비는 공격적으로,\n아군이 불리하면 방어적으로 행동합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10948_1].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Pinky Nursefather will go on the offensive if you have the advantage, and will go on the defensive if she has the advantage.
   PL: Gdy sojusznicy mają przewagę, Ojciec Małego Palca działa ofensywnie,\na gdy jest im trudno — defensywnie.
177. [Samouczek i wskazówki [battleTip_10948_2] — tekst] 소지 아비의 공격을 견딜 수 있는 전략을 세우고, 꾸준히 피해를 누적시키세요.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10948_2].content
   limit: do 130 znaków
   EN: Strategize around surviving The Pinky Nursefather's attacks and slowly chip away at her health.
   PL: Zbuduj strategię przetrwania ataków Ojca Małego Palca i cierpliwie kumuluj obrażenia.
178. [Samouczek i wskazówki [battleTip_10949_1] — tekst] 검지 제자와 소지 제자를 쓰러뜨리기 전에 뫼르소와 오티스가 먼저 사망하지 않도록 주의해야 합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10949_1].content
   limit: do 160 znaków
   EN: Focus on ensuring that Meursault and Outis survive the fight, rather than defeating Sora and Ren, the two Apprentices.
   PL: Uważaj, by Meursault i Outis nie zginęli pierwsi, zanim upadną Uczennica Wskazującego i Uczeń Małego Palca.
179. [Samouczek i wskazówki [battleTip_10949_2] — tekst] 료슈는 매 턴마다 검지 제자 또는 소지 제자 중 한 명을 공격합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10949_2].content
   limit: do 130 znaków
   EN: Every turn, Ryōshū will attack one of the two enemies—The Index Apprentice or The Pinky Apprentice.
   PL: W każdej turze Ryōshū atakuje jednego z dwóch wrogów: Uczennicę Wskazującego albo Ucznia Małego Palca.
180. [Samouczek i wskazówki [battleTip_10949_3] — tekst] 매 턴마다 료슈가 제자 중 한 명을 온전히 상대하도록 유도하고,\n수감자로는 다른 제자를 공략하는 것이 유리합니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10949_3].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It may be wise to let Ryōshū deal with one of the Apprentices while the Sinners focus on the other.
   PL: Warto pozwolić, by Ryōshū w każdej turze w pełni zajęła się jednym z Uczniów, a Skazańcy skupili się na drugim.
181. [Samouczek i wskazówki [battleTip_10950_1] — tekst] 검지 아비는 지령 실패 시, 카르마를 얻습니다. 카르마가 증가할수록 검지 아비의 합 위력을 포함한 전반적인 능력이 약화됩니다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10950_1].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Index Nursefather gains Karmic Consequence when he fails to carry out his Prescripts.\nRaising his Karmic Consequence Stack weakens his various stats, including his Clash Power.
   PL: Gdy Ojciec Wskazującego zawiedzie w wykonywaniu Nakazów, zyskuje Karma. Im więcej Karmy, tym słabsze jego ogólne zdolności, w tym Moc Starcia.
182. [Samouczek i wskazówki [battleTip_10950_2] — tekst] 특수 패턴에서 합 위력이 높은 참격, 관통, 타격 스킬이 필요합니다. 합 위력이 높은 참격, 관통, 타격 E.G.O 스킬을 준비해봅시다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10950_2].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During a unique pattern, you will need high-Clashing Skills in all three Attack Types: Slash, Pierce, and Blunt.\nPreparing high-Clashing E.G.O Skills in each Attack Type is recommended.
   PL: W unikalnym wzorcu potrzebne są Umiejętności Cięcia, Przebicia i Uderzenia o wysokiej Mocy Starcia. Przygotuj E.G.O tych trzech typów o dużej Mocy Starcia.
183. [Samouczek i wskazówki [battleTip_10950_3] — tekst] 검지 아비가 체력이 낮을 때 사용하는 강력한 스킬은 위력이 매우 높습니다. 이때 료슈의 기본 E.G.O인 '삼라염상'으로 맞서봅시다.
   źródło: BattleResultHint-a1c9p3.json :: dataList[id=battleTip_10950_3].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At low HP, The Index Nursefather uses a powerful Skill with a very high Power.\nRyōshū's Base E.G.O., "Forest for the Flames" may be effective against this attack.
   PL: Potężna Umiejętność używana przez Ojca Wskazującego przy niskim HP ma bardzo wysoką Moc. Spróbuj przeciwstawić jej bazowe E.G.O Ryōshū — „Las dla Płomieni”

## Samouczek i wskazówki: BattleResultHint-exme
- plik gry: `BattleResultHint-exme.json`

184. [Samouczek i wskazówki [battleTip_912710_1] — tekst] 임경업의 본국검술[살] 수치를 수감자에게 유리하게 조정해야 합니다.
   źródło: BattleResultHint-exme.json :: dataList[id=battleTip_912710_1].content
   limit: do 160 znaków
   EN: Make sure that Im Gyeong-eop's Swordplay of the Homeland [Sal] Stack remains in a range that is advantageous to the Sinners.
   PL: Dopilnuj, by stos „Rodzimej Szermierki [Sal]” Im Gyeong-eopa pozostawał na poziomie korzystnym dla Skazańców.
185. [Samouczek i wskazówki [battleTip_912710_2] — tekst] 섬광 현상 - 영사기를 우선 공격하면 S사로 빠르게 넘어갈 수 있습니다.
   źródło: BattleResultHint-exme.json :: dataList[id=battleTip_912710_2].content
   limit: do 120 znaków
   EN: Prioritize attacking Flash Phenomenon - Projector to transition quicker to S Corp.
   PL: Priorytetowo atakuj Zjawisko Rozbłysku — Projektor, by szybciej przejść do S Corp.
186. [Samouczek i wskazówki [battleTip_912710_3] — tekst] 후속 직원 보충은 N사에서만 일어납니다.
   źródło: BattleResultHint-exme.json :: dataList[id=battleTip_912710_3].content
   limit: do 120 znaków
   EN: N Corp. Staff reinforcements occur only in N Corp.
   PL: Uzupełnienia personelu następują wyłącznie w N Corp.

## Samouczek i wskazówki: BattleResultHint-twth
- plik gry: `BattleResultHint-twth.json`

187. [Samouczek i wskazówki [battleTip_912512_1] — tekst] 도슨트 루포는 초반에 자신의 아군 스튜던트 수만큼 보호를 얻습니다. 초반에는 스튜던트를 노려보세요.
   źródło: BattleResultHint-twth.json :: dataList[id=battleTip_912512_1].content
   limit: do 180 znaków
   EN: In the earlier part of the battle, Docent Rufo gains Protection equal to the number of allied Students. Try taking out the Students first.
   PL: We wczesnej fazie walki Docent Rufo zyskuje Ochronę równą liczbie podległych jej Studentów. Na początku celuj w Studentów.
188. [Samouczek i wskazówki [battleTip_912512_2] — tekst] 강렬한 색채를 보유한 인격은 루포에게 합을 이기기 어려울 수 있습니다. 이 때는 수비 스킬을 써보세요.
   źródło: BattleResultHint-twth.json :: dataList[id=battleTip_912512_2].content
   limit: do 190 znaków
   EN: Identities inflicted with Palette Vibrante may find it difficult to win Clashes against Rufo. Try having those Identities use a Defensive Skill.
   PL: Tożsamości z Palette Vibrante mogą mieć trudność z wygraniem Starych z Rufo. Wtedy sięgnij po Umiejętności obrony.
189. [Samouczek i wskazówki [battleTip_912512_3] — tekst] 도슨트 루포는 후반에 높은 보호를 얻습니다. 부정적인 효과를 얻을수록 보호 수치가 감소하니 이를 고려해보세요.
   źródło: BattleResultHint-twth.json :: dataList[id=battleTip_912512_3].content
   limit: do 240 znaków
   EN: In the later part of the battle, Docent Rufo gains a high Protection Stack. Consider that her Protection Stack can be lowered by inflicting her with a variety of negative effect types.
   PL: W późnej fazie walki Docent Rufo zyskuje wysoką Ochronę. Im więcej efektów negatywnych, tym niższy jej stos — uwzględnij to.

## Wydarzenia i Przepustka: AttendanceCheckS7
- plik gry: `AttendanceCheckS7.json`

190. [Wydarzenia i Przepustka [attendance_check_s7_special_reward_condition] — tekst] 이벤트 기간 동안\n사영전투-삽시호 (Normal)\n클리어 시 획득
   źródło: AttendanceCheckS7.json :: dataList[id=attendance_check_s7_special_reward_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtained by clearing\nReflectrial - Chachihu (Normal)\nbefore the event ends
   PL: Zdobyte za ukończenie\nWalki Projekcyjnej — Chachihu (Normal)\nw okresie wydarzenia
191. [Wydarzenia i Przepustka [attendance_event_s7_desc] — tekst] ※ 이벤트 기간 동안 누적 출석일에 따라 보상을 획득할 수 있습니다.
   źródło: AttendanceCheckS7.json :: dataList[id=attendance_event_s7_desc].content
   limit: do 120 znaków
   EN: ※ Receive more rewards the more attendance checks you accumulate over the event period.
   PL: ※ W okresie wydarzenia nagrody zależą od łącznej liczby dni logowania.

## Wydarzenia i Przepustka: AttendanceRewardsText
- plik gry: `AttendanceRewardsText.json`

192. [Wydarzenia i Przepustka [total_consumed_enkephalin] — tekst] 전체 소모한 엔케팔린
   źródło: AttendanceRewardsText.json :: dataList[id=total_consumed_enkephalin].content
   limit: do 120 znaków
   EN: Total Enkephalin Used
   PL: Łącznie zużyte Enkefaliny
193. [Wydarzenia i Przepustka [enkephalin_consumption_encourage] — tekst] 와! 일하세요 관리자님! 먹여 살려야 할 수감자가 이렇게나 많이!
   źródło: AttendanceRewardsText.json :: dataList[id=enkephalin_consumption_encourage].content
   limit: do 120 znaków
   EN: Yay! Get to work, Manager! You’ve got a whole lot of Sinners to feed!
   PL: Jej! Do pracy, Panie Menedżerze! Tyle Skazańców trzeba wyżywić!
194. [Wydarzenia i Przepustka [attendance_rewards_description_0] — tekst] 이벤트 기간 동안 실제 소모한 엔케팔린 수치가 반영됩니다
   źródło: AttendanceRewardsText.json :: dataList[id=attendance_rewards_description_0].content
   limit: do 120 znaków
   EN: Enkephalin spent during the event period will be tallied.
   PL: W okresie wydarzenia zliczane jest rzeczywiście zużyte Enkefaliny
195. [Wydarzenia i Przepustka [attendance_rewards_description_1] — tekst] 엔케팔린 모듈을 소모할 경우, 개당 20만큼의 엔케팔린 수치가 반영됩니다.
   źródło: AttendanceRewardsText.json :: dataList[id=attendance_rewards_description_1].content
   limit: do 120 znaków
   EN: Using an Enkephalin Module counts as spending 20 Enkephalin.
   PL: Użycie Modułu Enkefalinu liczy się jako zużycie 20 Enkefalin
196. [Wydarzenia i Przepustka [attendance_rewards_description_2] — tekst] 거울 던전 일일 무료 입장은 반영되지 않습니다
   źródło: AttendanceRewardsText.json :: dataList[id=attendance_rewards_description_2].content
   limit: do 120 znaków
   EN: Daily free entry for Mirror Dungeons does not count toward the tally.
   PL: Darmowe codzienne wejścia do Lustrzanych Loch nie wliczają się do zliczania
197. [Wydarzenia i Przepustka [april_event_story_popup_title] — tekst] 이야기 다시보기
   źródło: AttendanceRewardsText.json :: dataList[id=april_event_story_popup_title].content
   limit: do 120 znaków
   EN: Rewatch Story
   PL: Obejrzyj fabułę ponownie
198. [Wydarzenia i Przepustka [april_event_story_popup_content] — tekst] '한봄 밤의 꿈' 을 다시 보시겠습니까?
   źródło: AttendanceRewardsText.json :: dataList[id=april_event_story_popup_content].content
   limit: do 120 znaków
   EN: Rewatch “A Midspring Night’s Dream”?
   PL: Obejrzeć ponownie „Sen Środkowowiosennej Nocy”?

## Wydarzenia i Przepustka: BattlePass-a1c10
- plik gry: `BattlePass-a1c10.json`

199. [Wydarzenia i Przepustka [battlepass_season_8] — tekst] 푼크툼
   źródło: BattlePass-a1c10.json :: dataList[id=battlepass_season_8].content
   limit: do 120 znaków
   EN: PUNCTUM
   PL: PUNCTUM
200. [Wydarzenia i Przepustka [battle_pass_season_8_product_package_with_limbus_desc_summary] — tekst] ◆ 시즌 8 림버스 패스\n◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 VI\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c10.json :: dataList[id=battle_pass_season_8_product_package_with_limbus_desc_summary].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Season 8 Limbus Pass\n◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket VI\n◆ Limbus Package Special Banner
   PL: ◆ Limbus Pass Sezonu 8\n◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości VI\n◆ Specjalny banner Pakietu Limbus
201. [Wydarzenia i Przepustka [battle_pass_season_8_product_package_without_limbus_desc_summary] — tekst] ◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 VI\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c10.json :: dataList[id=battle_pass_season_8_product_package_without_limbus_desc_summary].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket VI\n◆ Limbus Package Special Banner
   PL: ◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości VI\n◆ Specjalny banner Pakietu Limbus
202. [Wydarzenia i Przepustka [until_season_8_start] — tekst] - 시즌 9 업데이트 전까지
   źródło: BattlePass-a1c10.json :: dataList[id=until_season_8_start].content
   limit: do 120 znaków
   EN: - Until Season 9 Update
   PL: - Do aktualizacji Sezonu 9
203. [Wydarzenia i Przepustka [until_season_8_end_on_shop] — tekst] 시즌 9 업데이트 전\n까지
   źródło: BattlePass-a1c10.json :: dataList[id=until_season_8_end_on_shop].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Until Season 9 Update
   PL: Do aktualizacji\nSezonu 9

## Wydarzenia i Przepustka: BattlePass-a1c7
- plik gry: `BattlePass-a1c7.json`

204. [Wydarzenia i Przepustka [battle_pass_season_5_product_package_with_limbus_desc_summary] — tekst] ◆ 시즌 5 림버스 패스\n◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너 2종
   źródło: BattlePass-a1c7.json :: dataList[id=battle_pass_season_5_product_package_with_limbus_desc_summary].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Season 5 Limbus Pass\n◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket V\n◆ Limbus Package Special Banner x2
   PL: ◆ Limbus Pass Sezonu 5\n◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości V\n◆ 2 Specjalne bannery Pakietu Limbus
205. [Wydarzenia i Przepustka [battle_pass_season_5_product_package_without_limbus_desc_summary] — tekst] ◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너 2종
   źródło: BattlePass-a1c7.json :: dataList[id=battle_pass_season_5_product_package_without_limbus_desc_summary].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket V\n◆ Limbus Package Special Banner x2
   PL: ◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości V\n◆ 2 Specjalne bannery Pakietu Limbus

## Wydarzenia i Przepustka: BattlePass-a1c8
- plik gry: `BattlePass-a1c8.json`

206. [Wydarzenia i Przepustka [battle_pass_season_6_product_package_with_limbus_desc_summary] — tekst] ◆ 시즌 6 림버스 패스\n◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c8.json :: dataList[id=battle_pass_season_6_product_package_with_limbus_desc_summary].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Season 6 Limbus Pass\n◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket V\n◆ Limbus Package Special Banner
   PL: ◆ Limbus Pass Sezonu 6\n◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości V\n◆ Specjalny banner Pakietu Limbus
207. [Wydarzenia i Przepustka [battle_pass_season_6_product_package_without_limbus_desc_summary] — tekst] ◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c8.json :: dataList[id=battle_pass_season_6_product_package_without_limbus_desc_summary].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket V\n◆ Limbus Package Special Banner
   PL: ◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości V\n◆ Specjalny banner Pakietu Limbus

## Wydarzenia i Przepustka: BattlePass-a1c9
- plik gry: `BattlePass-a1c9.json`

208. [Wydarzenia i Przepustka [battlepass_season_7] — tekst] 쿠모노 이토 · 아카노 이토
   źródło: BattlePass-a1c9.json :: dataList[id=battlepass_season_7].content
   limit: do 120 znaków
   EN: Kumo no Ito · otI on akA
   PL: Kumo no Ito · otI on akA
209. [Wydarzenia i Przepustka [battle_pass_season_7_product_package_with_limbus_desc_summary] — tekst] ◆ 시즌 7 림버스 패스\n◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 VI\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c9.json :: dataList[id=battle_pass_season_7_product_package_with_limbus_desc_summary].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Season 7 Limbus Pass\n◆ Immediately gain 10 Pass LV upon purchase\n◆ Level Boost Ticket VI\n◆ Limbus Package Special Banner
   PL: ◆ Limbus Pass Sezonu 7\n◆ Natychmiastowy zysk 10 poziomów Passu po zakupie\n◆ Bilet Specjalnego Wzmocnienia Tożsamości VI\n◆ Specjalny banner Pakietu Limbus
210. [Wydarzenia i Przepustka [battle_pass_season_7_product_package_without_limbus_desc_summary] — tekst] ◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 VI\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass-a1c9.json :: dataList[id=battle_pass_season_7_product_package_without_limbus_desc_summary].content
   (powtórzenie elementu 201 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Wydarzenia i Przepustka [until_season_7_start] — tekst] - 시즌 8 업데이트 전까지
   źródło: BattlePass-a1c9.json :: dataList[id=until_season_7_start].content
   limit: do 120 znaków
   EN: - Until Season 8 Update
   PL: - Do aktualizacji Sezonu 8
212. [Wydarzenia i Przepustka [until_season_7_end_on_shop] — tekst] 시즌 8 업데이트 전\n까지
   źródło: BattlePass-a1c9.json :: dataList[id=until_season_7_end_on_shop].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Until Season 8
   PL: Do aktualizacji\nSezonu 8

## Wydarzenia i Przepustka: BattlePass
- plik gry: `BattlePass.json`

213. [Wydarzenia i Przepustka [battlepass_battlepass] — tekst] 배틀 패스
   źródło: BattlePass.json :: dataList[id=battlepass_battlepass].content
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Wydarzenia i Przepustka [battlepass_passmission] — tekst] 패스 미션
   źródło: BattlePass.json :: dataList[id=battlepass_passmission].content
   limit: do 120 znaków
   EN: Pass Missions
   PL: Misje Przepustki
215. [Wydarzenia i Przepustka [battlepass_dailymission] — tekst] 일일미션
   źródło: BattlePass.json :: dataList[id=battlepass_dailymission].content
   limit: do 120 znaków
   EN: Daily
   PL: Dzienne
216. [Wydarzenia i Przepustka [battlepass_weeklymission] — tekst] 주간미션
   źródło: BattlePass.json :: dataList[id=battlepass_weeklymission].content
   limit: do 120 znaków
   EN: Weekly
   PL: Tygodniowe
217. [Wydarzenia i Przepustka [battlepass_seasonmission] — tekst] 시즌미션
   źródło: BattlePass.json :: dataList[id=battlepass_seasonmission].content
   limit: do 120 znaków
   EN: Seasonal
   PL: Sezonowe
218. [Wydarzenia i Przepustka [battlepass_freeandpaid] — tekst] 유료 {0} 무료 {1}
   źródło: BattlePass.json :: dataList[id=battlepass_freeandpaid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Paid {0} Free {1}
   PL: Płatne {0} Darmowe {1}
219. [Wydarzenia i Przepustka [battlepass_mission_tag_normal] — tekst] 일반
   źródło: BattlePass.json :: dataList[id=battlepass_mission_tag_normal].content
   limit: do 120 znaków
   EN: Regular
   PL: Ogólne
220. [Wydarzenia i Przepustka [battlepass_mission_tag_battle] — tekst] 전투
   źródło: BattlePass.json :: dataList[id=battlepass_mission_tag_battle].content
   limit: do 120 znaków
   EN: Combat
   PL: Walka
221. [Wydarzenia i Przepustka [battlepass_remain_time] — tekst] {0}일 {1}시간 남음
   źródło: BattlePass.json :: dataList[id=battlepass_remain_time].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} days {1} hours left
   PL: Pozostało: {0} dni {1} godz.
222. [Wydarzenia i Przepustka [battlepass_ask_purchase_limbus_pass] — tekst] 림버스 패스 구매 시,\n{0} 기간 동안 다음과 같은 혜택이 제공됩니다.
   źródło: BattlePass.json :: dataList[id=battlepass_ask_purchase_limbus_pass].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Purchasing the Limbus Pass will give you the following benefits during {0}:
   PL: Zakup Limbus Pass zapewni następujące korzyści w okresie {0}:
223. [Wydarzenia i Przepustka [battlepass_limbus_pass_benefit_reward] — tekst] 림버스 패스 보상 획득 가능
   źródło: BattlePass.json :: dataList[id=battlepass_limbus_pass_benefit_reward].content
   limit: do 120 znaków
   EN: Limbus Pass Rewards Available
   PL: Nagrody Limbus Pass dostępne
224. [Wydarzenia i Przepustka [battlepass_limbus_pass_benefit_ex_reward] — tekst] 패스 레벨 초과 보상 강화
   źródło: BattlePass.json :: dataList[id=battlepass_limbus_pass_benefit_ex_reward].content
   limit: do 120 znaków
   EN: Max Pass Level Reward Upgraded
   PL: Ulepszone nagrody ponad maksymalny poziom Passu
225. [Wydarzenia i Przepustka [battlepass_level_up] — tekst] 패스 레벨 업
   źródło: BattlePass.json :: dataList[id=battlepass_level_up].content
   limit: do 120 znaków
   EN: Pass Level-up
   PL: Podnieś poziom Passu
226. [Wydarzenia i Przepustka [battlepass_level_up_ask] — tekst] [유료 광기]를 소모하여 패스 레벨 업 하시겠습니까?
   źródło: BattlePass.json :: dataList[id=battlepass_level_up_ask].content
   limit: do 120 znaków
   EN: Level up the Pass using [Paid Lunacy]?
   PL: Podnieść poziom Passu za [Płatne Szaleństwo]?
227. [Wydarzenia i Przepustka [battlepass_level_upgrade] — tekst] 패스 레벨 상승
   źródło: BattlePass.json :: dataList[id=battlepass_level_upgrade].content
   limit: do 120 znaków
   EN: Pass Level Up
   PL: Poziom Passu podniesiony
228. [Wydarzenia i Przepustka [battlepass_level_max] — tekst] 패스 <color=#f8c200>최대 레벨</color> 달성
   źródło: BattlePass.json :: dataList[id=battlepass_level_max].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: <color=#f8c200>Max Pass Level</color> reached.
   PL: Osiągnięto <color=#f8c200>maksymalny poziom Passu</color>
229. [Wydarzenia i Przepustka [battlepass_purchase_level_up_failed] — tekst] 패스 레벨 구매 불가
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_level_up_failed].content
   limit: do 120 znaków
   EN: Cannot Purchase Pass Level
   PL: Nie można kupić poziomu Passu
230. [Wydarzenia i Przepustka [lack_if_paid_lunacy] — tekst] 유료 광기 부족
   źródło: BattlePass.json :: dataList[id=lack_if_paid_lunacy].content
   limit: do 120 znaków
   EN: Insufficient Paid Lunacy
   PL: Za mało Płatnego Szaleństwa
231. [Wydarzenia i Przepustka [remain_days_with_label] — tekst] {0}일 남음
   źródło: BattlePass.json :: dataList[id=remain_days_with_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}d left
   PL: Pozostało dni: {0}
232. [Wydarzenia i Przepustka [remain_hours_with_label] — tekst] {0}시간 남음
   źródło: BattlePass.json :: dataList[id=remain_hours_with_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}h left
   PL: Pozostało {0} godz.
233. [Wydarzenia i Przepustka [remain_minutes_with_label] — tekst] {0}분 남음
   źródło: BattlePass.json :: dataList[id=remain_minutes_with_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}m left
   PL: Pozostało {0} min
234. [Wydarzenia i Przepustka [update_progress] — tekst] 진행도 갱신
   źródło: BattlePass.json :: dataList[id=update_progress].content
   limit: do 120 znaków
   EN: Progress Updated
   PL: Postęp zaktualizowany
235. [Wydarzenia i Przepustka [able_to_acquire_ex_pass_level_reward] — tekst] 패스 레벨 초과 보상 수령 가능
   źródło: BattlePass.json :: dataList[id=able_to_acquire_ex_pass_level_reward].content
   limit: do 120 znaków
   EN: Eligible for Max Pass Level rewards
   PL: Nagrody ponad maksymalny poziom Passu dostępne
236. [Wydarzenia i Przepustka [ask_to_use_paid_lunacy_to_level_up_pass] — tekst] 유료 광기 {0}개를 소모하여 패스 레벨을 구매하시겠습니까?
   źródło: BattlePass.json :: dataList[id=ask_to_use_paid_lunacy_to_level_up_pass].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Spend {0} Paid Lunacy to purchase Pass Levels?
   PL: Wydać {0} Płatnego Szaleństwa na zakup poziomów Passu?
237. [Wydarzenia i Przepustka [battlepass_purchase_level_up] — tekst] 패스 레벨 구매
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_level_up].content
   limit: do 120 znaków
   EN: Buy Pass Levels
   PL: Kup poziomy Passu
238. [Wydarzenia i Przepustka [lack_of_paid_lunacy] — tekst] 유료 광기가 부족합니다.
   źródło: BattlePass.json :: dataList[id=lack_of_paid_lunacy].content
   limit: do 120 znaków
   EN: You don’t have enough paid Lunacy.
   PL: Za mało Płatnego Szaleństwa.
239. [Wydarzenia i Przepustka [only_paid_lunacy_for_battlepass_levelup] — tekst] ※배틀 패스 레벨 구매 시, 유료 광기 300을 소모합니다.
   źródło: BattlePass.json :: dataList[id=only_paid_lunacy_for_battlepass_levelup].content
   limit: do 120 znaków
   EN: ※ Purchasing Battle Pass Levels costs 300 Paid Lunacy.
   PL: ※ Zakup poziomów Przepustki Bojowej kosztuje 300 Płatnego Szaleństwa.
240. [Wydarzenia i Przepustka [buy_battlepass_word] — tekst] 구매
   źródło: BattlePass.json :: dataList[id=buy_battlepass_word].content
   limit: do 120 znaków
   EN: Buy
   PL: Kup
241. [Wydarzenia i Przepustka [battlepass_level_ex_reward] — tekst] 패스 레벨 초과 보상
   źródło: BattlePass.json :: dataList[id=battlepass_level_ex_reward].content
   limit: do 120 znaków
   EN: Max Pass Level Reward
   PL: Nagroda ponad maksymalny poziom Passu
242. [Wydarzenia i Przepustka [battlepass_progress] — tekst] 패스 경험치
   źródło: BattlePass.json :: dataList[id=battlepass_progress].content
   limit: do 120 znaków
   EN: Battle Pass XP
   PL: PD Przepustki Bojowej
243. [Wydarzenia i Przepustka [battlepass_free] — tekst] 무료
   źródło: BattlePass.json :: dataList[id=battlepass_free].content
   limit: do 120 znaków
   EN: Free
   PL: Darmowe
244. [Wydarzenia i Przepustka [battlepass_limbuspass] — tekst] 림버스패스
   źródło: BattlePass.json :: dataList[id=battlepass_limbuspass].content
   limit: do 120 znaków
   EN: Limbus Pass
   PL: Limbus Pass
245. [Wydarzenia i Przepustka [battlepass_unable_levelup_by_level] — tekst] 최대 레벨 도달
   źródło: BattlePass.json :: dataList[id=battlepass_unable_levelup_by_level].content
   limit: do 120 znaków
   EN: Max Level Reached
   PL: Osiągnięto maksymalny poziom
246. [Wydarzenia i Przepustka [battlepass_reward_opened_at] — tekst] {0} 업데이트
   źródło: BattlePass.json :: dataList[id=battlepass_reward_opened_at].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Update
   PL: Aktualizacja {0}
247. [Wydarzenia i Przepustka [battlepass_package_purchase] — tekst] <font="BebasKai SDF">LIMBUS PASS</font> 패키지
   źródło: BattlePass.json :: dataList[id=battlepass_package_purchase].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="BebasKai SDF">, </font>
   EN: <font="BebasKai SDF">LIMBUS PASS</font> Package
   PL: <font="BebasKai SDF">LIMBUS PASS</font> Pakiet
248. [Wydarzenia i Przepustka [battlepass_package_desc_level] — tekst] 「림버스 패키지 특별 배너」 포함 각종 보상
   źródło: BattlePass.json :: dataList[id=battlepass_package_desc_level].content
   limit: do 120 znaków
   EN: Contains various rewards including the 「Limbus Pass Package Special Banner」
   PL: Różne nagrody, w tym „Specjalny banner Pakietu Limbus”
249. [Wydarzenia i Przepustka [battlepass_package_desc_banner] — tekst] + [LIMBUS PASS] 증정
   źródło: BattlePass.json :: dataList[id=battlepass_package_desc_banner].content
   limit: do 120 znaków
   EN: + [LIMBUS PASS] Activation
   PL: + Aktywacja [LIMBUS PASS]
250. [Wydarzenia i Przepustka [battlepass_package_ask_purchase] — tekst] 유료 광기 {0}를 소모하여 패키지를 구매하시겠습니까?
   źródło: BattlePass.json :: dataList[id=battlepass_package_ask_purchase].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Spend {0} Paid Lunacy to purchase this Package?
   PL: Wydać {0} Płatnego Szaleństwa na zakup tego Pakietu?
251. [Wydarzenia i Przepustka [battlepass_package_warning] — tekst] ※ 구매 즉시 사용되는 상품으로, 청약 철회가 제한되는 상품입니다.
   źródło: BattlePass.json :: dataList[id=battlepass_package_warning].content
   limit: do 120 znaków
   EN: ※ This item will be immediately used upon purchase; refund may be restricted.
   PL: ※ Przedmiot używany natychmiast po zakupie; zwrot może być ograniczony.
252. [Wydarzenia i Przepustka [battlepass_limbus_pass_benefit_ex_box_reward] — tekst] 구매 시, 다음 패스 레벨 초과 보상 획득
   źródło: BattlePass.json :: dataList[id=battlepass_limbus_pass_benefit_ex_box_reward].content
   limit: do 120 znaków
   EN: Receive the following Max Pass Level EX Rewards upon purchase
   PL: Po zakupie otrzymasz następujące nagrody ponad maksymalny poziom Passu
253. [Wydarzenia i Przepustka [battlepass_limbus_pass_benefit_ex_box_reward_count] — tekst] <size=75%>(구매 시, 현재 패스 레벨 기준으로\n시즌 {0} 자아 파편 선택 상자 <style="highlightConverted">{1}</style>개 획득 가능)</size>
   źródło: BattlePass.json :: dataList[id=battlepass_limbus_pass_benefit_ex_box_reward_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=75%>, <style="highlightConverted">, </style>, </size>, {0}, {1}, \n
   EN: <size=75%>(At your Pass Level, you can obtain <style="highlightConverted">{1}</style> Season {0} Nominable Egoshard Crates upon purchase)</size>
   PL: <size=75%>(Przy obecnym poziomie Passu otrzymasz przy zakupie <style="highlightConverted">{1}</style> Imiennych Skrzynek Odłamków E.G.O Sezonu {0})</size>
254. [Wydarzenia i Przepustka [battlepass_select_product_popup_title] — tekst] 패스/패키지 선택
   źródło: BattlePass.json :: dataList[id=battlepass_select_product_popup_title].content
   limit: do 120 znaków
   EN: Select Pass/Package
   PL: Wybór Passu/Pakietu
255. [Wydarzenia i Przepustka [only_paid_lunacy_for_battlepass_levelup_with_number] — tekst] ※ 패스 레벨 1 구매 시, 유료 광기 {0} 소모
   źródło: BattlePass.json :: dataList[id=only_paid_lunacy_for_battlepass_levelup_with_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ Purchasing a Pass Level costs {0} Paid Lunacy.
   PL: ※ Zakup 1 poziomu Passu kosztuje {0} Płatnego Szaleństwa.
256. [Wydarzenia i Przepustka [battle_pass_package_button_desc] — tekst] 특별 배너 포함\n각종 보상 획득
   źródło: BattlePass.json :: dataList[id=battle_pass_package_button_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Various Rewards\nIncluding the Special Banner
   PL: Różne nagrody\nze Specjalnym bannerem
257. [Wydarzenia i Przepustka [battle_pass_select_popup_package_desc] — tekst] 특별 배너 포함\n각종 보상 획득
   źródło: BattlePass.json :: dataList[id=battle_pass_select_popup_package_desc].content
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Wydarzenia i Przepustka [battle_pass_select_popup_limbus_desc] — tekst] ◆ 림버스 패스 보상 획득 가능\n◆ 패스 레벨 초과 보상 강화
   źródło: BattlePass.json :: dataList[id=battle_pass_select_popup_limbus_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Unlocks Limbus Pass Rewards\n◆ Upgrades Max Pass Level EX Rewards
   PL: ◆ Odblokowuje nagrody Limbus Pass\n◆ Ulepsza nagrody ponad maksymalny poziom Passu
259. [Wydarzenia i Przepustka [battle_pass_package_purchase_popup_desc] — tekst] ◆ 구매 즉시 패스 레벨이 10만큼 증가합니다.\n◆ 다음 구성품이 포함되어 있습니다.
   źródło: BattlePass.json :: dataList[id=battle_pass_package_purchase_popup_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Gain 10 Pass Levels immediately upon purchase.\n◆ Includes the following contents.
   PL: ◆ Po zakupie natychmiast zyskujesz 10 poziomów Passu.\n◆ Zawiera następujące składniki.
260. [Wydarzenia i Przepustka [battle_pass_limbus_purchase_popup_desc] — tekst] ◆ 림버스 패스에 포함된 각종 보상을 획득할 수 있습니다.\n◆ 패스 레벨 초과 보상으로 획득할 수 있는 시즌 3 자아 파편 선택 상자의 수량이 1개에서 3개로 증가합니다.
   źródło: BattlePass.json :: dataList[id=battle_pass_limbus_purchase_popup_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Receive various rewards from the Limbus Pass.\n◆ Receive 3 [Season 3] Nominable Egoshard Crates instead of 1 from the Max Pass Level EX Rewards.
   PL: ◆ Otrzymasz różne nagrody z Limbus Pass.\n◆ Liczba Imiennych Skrzynek Odłamków E.G.O Sezonu 3 dostępnych jako nagrody ponad maksymalny poziom Passu wzrasta z 1 do 3 sztuk
261. [Wydarzenia i Przepustka [battle_pass_package_button_desc_with_limbus] — tekst] 특별 배너 포함\n각종 보상 획득\n+[LIMBUS PASS] 증정
   źródło: BattlePass.json :: dataList[id=battle_pass_package_button_desc_with_limbus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Various Rewards\nIncluding the Special Banner\n+ [LIMBUS PASS]
   PL: Różne nagrody\nze Specjalnym bannerem\n+ [LIMBUS PASS]
262. [Wydarzenia i Przepustka [battle_pass_package_purchase_popup_desc_in_box] — tekst] - 림버스 패키지 특별 배너\n- 인격 특수 강화 티켓 IV
   źródło: BattlePass.json :: dataList[id=battle_pass_package_purchase_popup_desc_in_box].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Limbus Pass Package Special Banner\n- Level Boost Ticket IV
   PL: - Specjalny banner Pakietu Limbus\n- Bilet Specjalnego Wzmocnienia Tożsamości IV
263. [Wydarzenia i Przepustka [until_season_4_start] — tekst] ~ 시즌 4 업데이트 전까지
   źródło: BattlePass.json :: dataList[id=until_season_4_start].content
   limit: do 120 znaków
   EN: ~ Until Season 4 Update
   PL: ~ Do aktualizacji Sezonu 4
264. [Wydarzenia i Przepustka [until_season_5_start] — tekst] 시즌 6 업데이트 전까지
   źródło: BattlePass.json :: dataList[id=until_season_5_start].content
   limit: do 120 znaków
   EN: Until Season 6 Update
   PL: Do aktualizacji Sezonu 6
265. [Wydarzenia i Przepustka [battlepass_ask_purchase_limbus_pass_package] — tekst] 림버스 패스 패키지 구매 시,\n{0} 기간 동안 다음과 같은 혜택이 제공됩니다.
   źródło: BattlePass.json :: dataList[id=battlepass_ask_purchase_limbus_pass_package].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Purchasing the Limbus Pass Package will\ngive you the following benefits during {0}:
   PL: Zakup Pakietu Limbus Pass zapewni następujące korzyści w okresie {0}:
266. [Wydarzenia i Przepustka [battlepass_purchase_desc_pass] — tekst] 림버스 패스에 포함된 각종 보상 획득 가능
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_pass].content
   limit: do 120 znaków
   EN: Various rewards included in the Limbus Pass
   PL: Różne nagrody zawarte w Limbus Pass
267. [Wydarzenia i Przepustka [battlepass_purchase_desc_ex] — tekst] 패스 레벨 초과 보상으로 획득할 수 있는 시즌 8 자아 파편 선택 상자의 수량이 <style="highlightConverted">{0}</style>개에서 <style="highlightConverted">{1}</style>개로 증가
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_ex].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="highlightConverted">, </style>, {0}, {1}
   EN: Receive <style="highlightConverted">{1}</style> Season 8 Nominable Egoshard Crates from Max Pass Level+ Rewards instead of <style="highlightConverted">{0}</style>
   PL: Liczba Imiennych Skrzynek Odłamków E.G.O Sezonu 8 jako nagrody ponad maks. poziom Passu rośnie z <style="highlightConverted">{0}</style> do <style="highlightConverted">{1}</style> szt.
268. [Wydarzenia i Przepustka [battlepass_purchase_desc_pass_level] — tekst] 구매 즉시 패스 레벨 10 증가
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_pass_level].content
   limit: do 120 znaków
   EN: Immediately gain 10 Pass Levels upon purchase
   PL: Po zakupie natychmiast zyskujesz 10 poziomów Passu
269. [Wydarzenia i Przepustka [battlepass_purchase_desc_level_ticket] — tekst] 인격 특수 강화 티켓 VI
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_level_ticket].content
   limit: do 120 znaków
   EN: Level Boost Ticket VI
   PL: Bilet Specjalnego Wzmocnienia Tożsamości VI
270. [Wydarzenia i Przepustka [battlepass_purchase_desc_special_banner] — tekst] 림버스 패키지 특별 배너
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_special_banner].content
   limit: do 120 znaków
   EN: Limbus Pass Package Special Banner
   PL: Specjalny banner Pakietu Limbus
271. [Wydarzenia i Przepustka [battlepass_purchase_desc_policy] — tekst] ※ 구매 즉시 사용되는 상품으로, 청약 철회가 제한되는 상품입니다.\n\n※ 배틀 패스는 [시즌 시작일로부터 최소 90일 이상의 기간]이 보장됩니다.\n배틀 패스 이용 종료일의 정확한 날짜는 [다음 시즌을 안내하는 공지 사항이 공개되는 시점]에 공지 사항을 통해 안내해 드립니다.\n배틀 패스 구매 일자는 이용할 수 있는 일수에 영향을 주지 않으니, 이 점을 유의하여 구매 과정에서 반드시 참고해 주시길 바랍니다.
   źródło: BattlePass.json :: dataList[id=battlepass_purchase_desc_policy].content
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ This item will be used immediately upon purchase; refund will be restricted.\n\n※ The Battle Pass is guaranteed to last [at least 90 days from the start of the Season].\nThe exact end date of the Battle Pass will be notified when the next [Guide for the upcoming Season] is posted.\nPlease note that your Battle Pass purchase date has no effect on the active duration of the Battle Pass.
   PL: ※ Przedmiot używany natychmiast po zakupie; zwrot będzie ograniczony.\n\n※ Przepustka Bojowa gwarantuje [co najmniej 90 dni od początku sezonu].\nDokładna data zakończenia Przepustki Bojowej zostanie ogłoszona w momencie publikacji [informacji o nadchodzącym sezonie].\nData zakupu Przepustki Bojowej nie wpływa na czas jej trwania — uwzględnij to przy zakupie.
272. [Wydarzenia i Przepustka [owned_count] — tekst] 소지 {0}
   źródło: BattlePass.json :: dataList[id=owned_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Owned
   PL: Posiadane: {0}
273. [Wydarzenia i Przepustka [battle_pass_package_button_desc_with_limbus_2] — tekst] ◆ 구매 즉시 패스 LV 10 상승\n◆ 추가 특별 배너 증정\n◆ 인격 특수 강화 티켓 VI
   źródło: BattlePass.json :: dataList[id=battle_pass_package_button_desc_with_limbus_2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ◆ Immediately gain 10 Pass LV upon purchase\n◆ Receive a Special Banner\n◆ Level Boost Ticket VI
   PL: ◆ Po zakupie natychmiast zyskujesz 10 poziomów Passu\n◆ Dodatkowy Specjalny banner\n◆ Bilet Specjalnego Wzmocnienia Tożsamości VI
274. [Wydarzenia i Przepustka [battle_pass_product_limbus_desc_summary] — tekst] ◆ 림버스 패스 보상 획득 가능\n◆ 패스 레벨 초과 보상 강화
   źródło: BattlePass.json :: dataList[id=battle_pass_product_limbus_desc_summary].content
   (powtórzenie elementu 258 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Wydarzenia i Przepustka [battle_pass_product_package_with_limbus_desc_summary] — tekst] ◆ 시즌 6 림버스 패스\n◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너
   źródło: BattlePass.json :: dataList[id=battle_pass_product_package_with_limbus_desc_summary].content
   (powtórzenie elementu 206 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Wydarzenia i Przepustka [battle_pass_product_package_without_limbus_desc_summary] — tekst] ◆ 구매 즉시 패스 레벨 10 상승\n◆ 인격 특수 강화 티켓 V\n◆ 림버스 패키지 특별 배너 2종
   źródło: BattlePass.json :: dataList[id=battle_pass_product_package_without_limbus_desc_summary].content
   (powtórzenie elementu 205 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Wydarzenia i Przepustka [battle_pass_sale_10] — tekst] 기존 대비 10% 할인
   źródło: BattlePass.json :: dataList[id=battle_pass_sale_10].content
   limit: do 120 znaków
   EN: 10% Discount
   PL: 10% taniej niż dotąd
278. [Wydarzenia i Przepustka [until_season_6_start] — tekst] - 시즌 7 업데이트 전까지
   źródło: BattlePass.json :: dataList[id=until_season_6_start].content
   limit: do 120 znaków
   EN: - Until Season 7 Update
   PL: - Do aktualizacji Sezonu 7

## Wydarzenia i Przepustka: BattlePass_Banner-a1c6
- plik gry: `BattlePass_Banner-a1c6.json`

279. [Wydarzenia i Przepustka [battlepass_season_4] — tekst] 시즌 4 클리어 올 캐시
   źródło: BattlePass_Banner-a1c6.json :: dataList[id=battlepass_season_4].content
   limit: do 120 znaków
   EN: Season 4: Clear All Cathy
   PL: Sezon 4: Clear All Cathy

## Wydarzenia i Przepustka: BattlePass_Banner-a1c7
- plik gry: `BattlePass_Banner-a1c7.json`

280. [Wydarzenia i Przepustka [battlepass_season_5] — tekst] 시즌 5 오블리비언
   źródło: BattlePass_Banner-a1c7.json :: dataList[id=battlepass_season_5].content
   limit: do 120 znaków
   EN: Season 5: Oblivion
   PL: Sezon 5: Oblivion

## Wydarzenia i Przepustka: BattlePass_Banner-a1c8
- plik gry: `BattlePass_Banner-a1c8.json`

281. [Wydarzenia i Przepustka [battlepass_season_6] — tekst] 시즌 6 장화인
   źródło: BattlePass_Banner-a1c8.json :: dataList[id=battlepass_season_6].content
   limit: do 120 znaków
   EN: Season 6: Zàng Huā Yín
   PL: Sezon 6: Zàng Huā Yín

## Wydarzenia i Przepustka: BattlePass_Banner
- plik gry: `BattlePass_Banner.json`

282. [Wydarzenia i Przepustka [battlepass_season_1] — tekst] 시즌 1 오리엔테이션
   źródło: BattlePass_Banner.json :: dataList[id=battlepass_season_1].content
   limit: do 120 znaków
   EN: Season 1: Orientation
   PL: Sezon 1: Orientation
283. [Wydarzenia i Przepustka [battlepass_season_2] — tekst] 시즌 2 레미니센스
   źródło: BattlePass_Banner.json :: dataList[id=battlepass_season_2].content
   limit: do 120 znaków
   EN: Season 2: Reminiscence
   PL: Sezon 2: Reminiscence

## Wydarzenia i Przepustka: BattlePass_Banner_2
- plik gry: `BattlePass_Banner_2.json`

284. [Wydarzenia i Przepustka [battlepass_season_3] — tekst] 시즌 3 본 보야지
   źródło: BattlePass_Banner_2.json :: dataList[id=battlepass_season_3].content
   limit: do 120 znaków
   EN: Season 3: Bon Voyage
   PL: Sezon 3: Bon Voyage

## Wydarzenia i Przepustka: BattlePass_Mission
- plik gry: `BattlePass_Mission.json`

285. [Wydarzenia i Przepustka [CLEAR_STAGE] — tekst] 임의의 스테이지 {0}회 클리어
   źródło: BattlePass_Mission.json :: dataList[id=CLEAR_STAGE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear any stage {0} time(s)
   PL: Ukończ dowolny etap {0} razy
286. [Wydarzenia i Przepustka [KILL_ENEMY_ANY] — tekst] 전투 중 적 누적 {0}명 섬멸
   źródło: BattlePass_Mission.json :: dataList[id=KILL_ENEMY_ANY].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defeat {0} enemies
   PL: Pokonaj łącznie {0} wrogów w walkach
287. [Wydarzenia i Przepustka [KILL_ENEMY_ABNORMALITY] — tekst] 전투 중 환상체 {0}체 제압
   źródło: BattlePass_Mission.json :: dataList[id=KILL_ENEMY_ABNORMALITY].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Suppress {0} Abnormalities
   PL: Stłum {0} Anomalii w walkach
288. [Wydarzenia i Przepustka [SOMEONE_PARTICIPATED_IN_BATTLE] — tekst] {1} 전투 참여 {0}회
   źródło: BattlePass_Mission.json :: dataList[id=SOMEONE_PARTICIPATED_IN_BATTLE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Have {1} in battle {0} time(s)
   PL: Weź udział w {0} walkach jako {1}
289. [Wydarzenia i Przepustka [MIRROR_DUNGEON_TRY] — tekst] 거울 던전 {0}회 도전
   źródło: BattlePass_Mission.json :: dataList[id=MIRROR_DUNGEON_TRY].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enter the Mirror Dungeon {0} time(s)
   PL: Wejdź do Lustrzanych Loch {0} razy
290. [Wydarzenia i Przepustka [MIRROR_DUNGEON_CLEAR] — tekst] 거울 던전 {0}회 클리어
   źródło: BattlePass_Mission.json :: dataList[id=MIRROR_DUNGEON_CLEAR].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Mirror Dungeons {0} time(s)
   PL: Ukończ Lustrzane Lochy {0} razy
291. [Wydarzenia i Przepustka [BATTLEPASS_LEVELUP] — tekst] 배틀패스 레벨 {0} 달성
   źródło: BattlePass_Mission.json :: dataList[id=BATTLEPASS_LEVELUP].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reach Battle Pass Level {0}
   PL: Osiągnij poziom {0} Przepustki Bojowej
292. [Wydarzenia i Przepustka [USE_EGO_20402] — tekst] 4번째 성냥불 료슈를 {0}회 사용
   źródło: BattlePass_Mission.json :: dataList[id=USE_EGO_20402].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Use Ryōshū’s 4th Match Flame {0} time(s)
   PL: Użyj 4. Zapałki Ryōshū {0} razy
293. [Wydarzenia i Przepustka [USE_ANNOUNCER_2] — tekst] 그레고르 아나운서를 {0}회 사용
   źródło: BattlePass_Mission.json :: dataList[id=USE_ANNOUNCER_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Have Gregor as the Announcer {0} time(s)
   PL: Ustaw Gregora jako Komentatora {0} razy
294. [Wydarzenia i Przepustka [LOGIN_ONCE] — tekst] 일일 로그인 {0}회
   źródło: BattlePass_Mission.json :: dataList[id=LOGIN_ONCE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} daily log-ins
   PL: {0} dziennych logowań
295. [Wydarzenia i Przepustka [LOGIN_MULTIPLE] — tekst] 누적 일일 로그인 {0}회
   źródło: BattlePass_Mission.json :: dataList[id=LOGIN_MULTIPLE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} total daily log-ins
   PL: Łącznie {0} dni logowania
296. [Wydarzenia i Przepustka [EXPDUNGEON_CLEAR] — tekst] 경험치 채광 {0}회 클리어
   źródło: BattlePass_Mission.json :: dataList[id=EXPDUNGEON_CLEAR].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear EXP Luxcavation {0} time(s)
   PL: Ukończ Wydobycie PD {0} razy
297. [Wydarzenia i Przepustka [THREADDENGEON_CLEAR] — tekst] 끈 채광 {0}회 클리어
   źródło: BattlePass_Mission.json :: dataList[id=THREADDENGEON_CLEAR].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Thread Luxcavation {0} time(s)
   PL: Ukończ Wydobycie Nici {0} razy
298. [Wydarzenia i Przepustka [PURCHASE_ENKEPHALIN_MODULE] — tekst] 엔케팔린 모듈 제작 {0}회
   źródło: BattlePass_Mission.json :: dataList[id=PURCHASE_ENKEPHALIN_MODULE].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Assemble {0} Enkephalin Module(s)
   PL: Wytwórz {0} Modułów Enkefalinu

## Wydarzenia i Przepustka: CultivationEvent
- plik gry: `CultivationEvent.json`

299. [Wydarzenia i Przepustka [cultivation_rewardShopButton] — tekst] 보상 교환
   źródło: CultivationEvent.json :: dataList[id=cultivation_rewardShopButton].content
   limit: do 120 znaków
   EN: Reward Exchange
   PL: Wymiana nagród
300. [Wydarzenia i Przepustka [cultivation_missionbutton_normal] — tekst] 업적
   źródło: CultivationEvent.json :: dataList[id=cultivation_missionbutton_normal].content
   limit: do 120 znaków
   EN: Achievements
   PL: Osiągnięcia
301. [Wydarzenia i Przepustka [cultivation_missionbutton_not_clear] — tekst] 8.5-3 클리어
   źródło: CultivationEvent.json :: dataList[id=cultivation_missionbutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 8.5-3
   PL: Ukończ 8.5-3
302. [Wydarzenia i Przepustka [cultivation_classbutton_normal] — tekst] 육성
   źródło: CultivationEvent.json :: dataList[id=cultivation_classbutton_normal].content
   limit: do 120 znaków
   EN: Cultivate
   PL: Uprawiaj
303. [Wydarzenia i Przepustka [cultivation_classbutton_not_clear] — tekst] 8.5-4 입장
   źródło: CultivationEvent.json :: dataList[id=cultivation_classbutton_not_clear].content
   limit: do 120 znaków
   EN: Enter 8.5-4
   PL: Wejdź do 8.5-4
304. [Wydarzenia i Przepustka [cultivation_stagebutton_normal] — tekst] 스테이지
   źródło: CultivationEvent.json :: dataList[id=cultivation_stagebutton_normal].content
   limit: do 120 znaków
   EN: Stages
   PL: Etap
305. [Wydarzenia i Przepustka [cultivation_stagebutton_not_clear] — tekst] 8-33 클리어
   źródło: CultivationEvent.json :: dataList[id=cultivation_stagebutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 8-33
   PL: Ukończ 8-33
306. [Wydarzenia i Przepustka [cultivation_stagebutton_end_event] — tekst] 이벤트 기간 종료
   źródło: CultivationEvent.json :: dataList[id=cultivation_stagebutton_end_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Zakończenie okresu wydarzenia
307. [Wydarzenia i Przepustka [cultivation_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: CultivationEvent.json :: dataList[id=cultivation_bonus_preview].content
   limit: do 120 znaków
   EN: Event Bonus Units
   PL: Jednostki premiowane w wydarzeniu
308. [Wydarzenia i Przepustka [cultivation_storybutton_before_start] — tekst] 8.5-1 클리어
   źródło: CultivationEvent.json :: dataList[id=cultivation_storybutton_before_start].content
   limit: do 120 znaków
   EN: Clear 8.5-1
   PL: Ukończ 8.5-1
309. [Wydarzenia i Przepustka [cultivation_storybutton_normal] — tekst] 상영관 이동
   źródło: CultivationEvent.json :: dataList[id=cultivation_storybutton_normal].content
   limit: do 120 znaków
   EN: To Theater
   PL: Do Teatru
310. [Wydarzenia i Przepustka [cultivation_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: CultivationEvent.json :: dataList[id=cultivation_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Wydarzenia i Przepustka [cultivation_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 인격 편성 시, <color=#ffa7a7>[지·용·인 기초 입문서]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#ffa7a7>120%</color>까지 적용됩니다.
   źródło: CultivationEvent.json :: dataList[id=cultivation_bonusUI_Desc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ffa7a7>, </color>, \n
   EN: During the event period, deploying the following Identities on your team will\nboost the amount of <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> earned.\nYou can earn a maximum of <color=#ffa7a7>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości, zwiększasz zdobywanie <color=#ffa7a7>[Wprowadzenia do Zhi, Yong i Ren]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#ffa7a7>120%</color>.
312. [Wydarzenia i Przepustka [cultivation_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: CultivationEvent.json :: dataList[id=cultivation_scrap_guide_title].content
   limit: do 120 znaków
   EN: Event Currency Guide
   PL: Informacje o walucie wydarzenia
313. [Wydarzenia i Przepustka [cultivation_rewardpage_desc] — tekst] 이벤트 스테이지를 클리어할 때마다 <color=#ffa7a7>[지·용·인 기초 입문서]</color>를 획득할 수 있습니다. 이외에도 주요 이야기\n스테이지를 최초로 클리어하거나 거울 던전 클리어 또는 업적 클리어 시, <color=#ffa7a7>[지·용·인 기초 입문서]</color>를 획득할 수 있습니다.\n\n이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 낮은 확률로 <color=#ffa7a7>[비급이 아닌 척하는 비전서]</color>를 획득할 수 있으며, <color=#ffa7a7>[비급이 아닌 척하는 비전서]</color>는 획득 즉시 <color=#ffa7a7>[지·용·인 기초 입문서]</color> 20개로 전환됩니다.\n\n<color=#ffa7a7>[보상 교환]</color> 창에서 <color=#ffa7a7>[지·용·인 기초 입문서]</color>를 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: CultivationEvent.json :: dataList[id=cultivation_rewardpage_desc].content
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: <color=#ffa7a7>, </color>, \n
   EN: During the event, you can earn <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> by clearing event Stages. You can also obtain <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> by clearing Main Story Stages for the first time, by clearing the Mirror Dungeon, or by clearing Achievements.\n\nRarely, you may obtain <color=#ffa7a7>[Definitely Not A Secret Scroll]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons,\nand <color=#ffa7a7>[Definitely Not A Secret Scroll]</color> is automatically converted to 20 <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> upon acquisition.\n\nIn the <color=#ffa7a7>[Reward Exchange]</color> window, you can purchase various rewards by spending <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> you have collected.
   PL: Ukończoną każdą etap wydarzenia, zdobywasz <color=#ffa7a7>[Wprowadzenie do Zhi, Yong i Ren]</color>. Możesz je także zdobyć za pierwsze ukończenia etapów Głównej Fabuły, Lustrzane Lochy lub Osiągnięcia.\n\nUkończywszy etapy wydarzenia, Głównej Fabuły lub Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#ffa7a7>[Zdecydowanie Nie Tajny Zwój]</color>, który od razu zamienia się na 20 szt. <color=#ffa7a7>[Wprowadzenia do Zhi, Yong i Ren]</color>.\n\nW oknie <color=#ffa7a7>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#ffa7a7>[Wprowadzenie do Zhi, Yong i Ren]</color>.
314. [Wydarzenia i Przepustka [cultivation_reward_popup_desc] — tekst] 이벤트 스테이지와 던전, 주요 이야기\n최초 클리어, 거울 던전 클리어, 업적 클리어를 통해\n<color=#ffa7a7>[지·용·인 기초 입문서]</color>를 획득할 수 있습니다.\n\n<color=#ffa7a7>[보상 교환]</color> 창에서 <color=#ffa7a7>[지·용·인 기초 입문서]</color>를\n지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: CultivationEvent.json :: dataList[id=cultivation_reward_popup_desc].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#ffa7a7>, </color>, \n
   EN: Earn <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> via the following methods:\nEvent Stage & Dungeon clears, Mirror Dungeon clears,\nAchievement clears, and Main Story Stage & Dungeon first-time clears.\n\nIn the <color=#ffa7a7>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color> you have collected.
   PL: Zdobywaj <color=#ffa7a7>[Wprowadzenie do Zhi, Yong i Ren]</color> przez:\nukończenia etapów wydarzenia i lochów, Lustrzane Lochy,\nOsiągnięcia oraz pierwsze ukończenia etapów i lochów Głównej Fabuły.\n\nW oknie <color=#ffa7a7>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#ffa7a7>[Wprowadzenie do Zhi, Yong i Ren]</color>.
315. [Wydarzenia i Przepustka [cultivation_mission_reward_popup_desc] — tekst] 수업을 통해 다양한 업적을\n달성하면 <color=#ffa7a7>[지·용·인 기초 입문서]</color>를\n획득할 수 있습니다.\n\n 이벤트 진행 기간이 종료되면 업적을 진행할 수 없으며, 보상 수령만 가능합니다.
   źródło: CultivationEvent.json :: dataList[id=cultivation_mission_reward_popup_desc].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#ffa7a7>, </color>, \n
   EN: Complete various Achievements via classes to obtain <color=#ffa7a7>[Intro to Zhi, Yong, Ren]</color>.\n\nOnce the event period is over, you will no longer be able to complete the Achievements. However, the rewards will still remain claimable.
   PL: Realizując różne Osiągnięcia w trakcie zajęć, zdobywasz\n<color=#ffa7a7>[Wprowadzenie do Zhi, Yong i Ren]</color>.\n\nPo zakończeniu okresu wydarzenia Osiągnięć nie da się ukończyć — nagrody pozostają do odebrania.
316. [Wydarzenia i Przepustka [ask_xichun_class_node_enter] — tekst] 수업을 위해\n교실로 입장하시겠습니까?
   źródło: CultivationEvent.json :: dataList[id=ask_xichun_class_node_enter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Head back to the classroom\nto resume the studies?
   PL: Czy wejść do klasy, aby wznowić zajęcia?
317. [Wydarzenia i Przepustka [not_playing_xichun_class_node] — tekst] 아직 수업 전입니다.
   źródło: CultivationEvent.json :: dataList[id=not_playing_xichun_class_node].content
   limit: do 120 znaków
   EN: Classes aren't in session yet.
   PL: Zajęcia jeszcze się nie rozpoczęły.
318. [Wydarzenia i Przepustka [not_playing_xichun_class_node_retry] — tekst] 수업이 종료되었습니다.\n다시 수업을 듣고 싶다면 스테이지 8.5-4로 입장해주시기 바랍니다.
   źródło: CultivationEvent.json :: dataList[id=not_playing_xichun_class_node_retry].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Classes are over.\nPlease enter Stage 8.5-4 if you would like to take those Classes again.
   PL: Zajęcia dobiegły końca.\nAby powtórzyć zajęcia, wejdź do etapu 8.5-4.

## Wydarzenia i Przepustka: DailyLoginEvent
- plik gry: `DailyLoginEvent.json`

319. [Wydarzenia i Przepustka [daily_login_event_title] — tekst] 출석 체크 이벤트
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_event_title].content
   limit: do 120 znaków
   EN: Roll Call Event
   PL: Wydarzenie listy obecności
320. [Wydarzenia i Przepustka [daily_login_event_description] — tekst] ※ 게임 내 일간 초기화를 기준(D-0 06:00 ~ D+1 05:59 (KST))으로, 출석 당일의 보상을 획득할 수 있습니다.\n※ 수령하지 않은 보상의 경우에는 다음 날에 기한 만료로 처리되오니 반드시 보상을 수령해주시길 바랍니다.
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_event_description].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ You can receive log-in rewards each day when entering the game based on the game’s daily resets (D-0 06:00 ~ D+1 05:59 <KST>).\n※ Unclaimed rewards are lost the next day, so please make sure to redeem them in time.
   PL: ※ Na podstawie dziennego resetu w grze (D-0 06:00 ~ D+1 05:59 (KST)) możesz odbierać nagrody za obecność danego dnia.\n※ Nieodebrane nagrody przepadają następnego dnia — odbieraj je na bieżąco.
321. [Wydarzenia i Przepustka [daily_login_event_weekly_format] — tekst] {0}주차
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_event_weekly_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Week {0}
   PL: Tydzień {0}
322. [Wydarzenia i Przepustka [daily_login_halloween_title] — tekst] 할로윈 출석 체크 이벤트
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_halloween_title].content
   limit: do 120 znaków
   EN: Halloween Attendance Check Event
   PL: Wydarzenie listy obecności Halloween
323. [Wydarzenia i Przepustka [daily_login_halloween_desc] — tekst] ▶누적 7일 접속 시, 「추출 10회 티켓 보상」을 얻을 수 있습니다
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_halloween_desc].content
   limit: do 120 znaków
   EN: ▶ Receive a 「Decaextraction Ticket」 by collecting 7 Attendance Checks
   PL: ▶ Za 7 dni obecności otrzymasz nagrodę „Bilet Dekaekstrakcji”
324. [Wydarzenia i Przepustka [daily_login_seventh_anniversary_desc] — tekst] 이벤트 기간 내 접속 시, 추출 10회 티켓 획득
   źródło: DailyLoginEvent.json :: dataList[id=daily_login_seventh_anniversary_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Log in during the event period\nand receive a Decaextraction Ticket
   PL: Zaloguj się w okresie wydarzenia\ni odbierz Bilet Dekaekstrakcji

## Wydarzenia i Przepustka: DailyLoginEvent_2
- plik gry: `DailyLoginEvent_2.json`

325. [Wydarzenia i Przepustka [daily_login_event_2_event_Title] — tekst] 특별 출석 체크 이벤트
   źródło: DailyLoginEvent_2.json :: dataList[id=daily_login_event_2_event_Title].content
   limit: do 120 znaków
   EN: Special Attendance Check Event
   PL: Specjalne wydarzenie listy obecności
326. [Wydarzenia i Przepustka [daily_login_event_2_event_description] — tekst] ※ 이벤트 기간 동안 누적한 출석 일수에\n따라 보상을 획득할 수 있습니다.\n\n※ 일간 초기화를 기준으로 서버 통신이\n진행되면 당일 출석한 것으로 인정됩니다.\n\n※ 수령하지 않은 보상은 이벤트 종료 이후\n받을 수 없게 되오니 반드시 이벤트 종료\n전에 보상을 수령해주시길 바랍니다.
   źródło: DailyLoginEvent_2.json :: dataList[id=daily_login_event_2_event_description].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Collect more attendance checks\nand unlock greater rewards.\n\n※ Log in after the daily reset period \nand receive your daily attendance checks.\n\n※ Once the event is over,\nthe rewards cannot be claimed.\nClaim them before the event ends.
   PL: ※ W okresie wydarzenia nagrody zależą\nod łącznej liczby dni logowania.\n\n※ Logowanie po dziennym resecie serwera\nuznawane jest za obecność danego dnia.\n\n※ Po zakończeniu wydarzenia nagrody\nnie będą już dostępne — odbierz je\nprzed końcem wydarzenia.
327. [Wydarzenia i Przepustka [new_user_daily_login_day] — tekst] {0}일차
   źródło: DailyLoginEvent_2.json :: dataList[id=new_user_daily_login_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Day {0}
   PL: Dzień {0}

## Wydarzenia i Przepustka: DawnOfGreenEventText
- plik gry: `DawnOfGreenEventText.json`

328. [Wydarzenia i Przepustka [dawn_of_green_reward_button] — tekst] 미션 목록
   źródło: DawnOfGreenEventText.json :: dataList[id=dawn_of_green_reward_button].content
   limit: do 120 znaków
   EN: Missions
   PL: Lista misji
329. [Wydarzenia i Przepustka [dawn_of_green_story_theater_button] — tekst] 상영관 이동
   źródło: DawnOfGreenEventText.json :: dataList[id=dawn_of_green_story_theater_button].content
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Wydarzenia i Przepustka [dawn_of_green_normal_stage] — tekst] 일반 난이도
   źródło: DawnOfGreenEventText.json :: dataList[id=dawn_of_green_normal_stage].content
   limit: do 120 znaków
   EN: Normal
   PL: Normalny
331. [Wydarzenia i Przepustka [dawn_of_green_hard_stage] — tekst] 어려움 난이도
   źródło: DawnOfGreenEventText.json :: dataList[id=dawn_of_green_hard_stage].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
332. [Wydarzenia i Przepustka [dawn_of_green_hard_stage_unlock_condition] — tekst] 일반 난이도 클리어 시 개방
   źródło: DawnOfGreenEventText.json :: dataList[id=dawn_of_green_hard_stage_unlock_condition].content
   limit: do 120 znaków
   EN: Clear Normal Difficulty to Unlock
   PL: Odblokowanie po ukończeniu poziomu Normalnego
333. [Wydarzenia i Przepustka [reward_Noraml] — tekst] 일반
   źródło: DawnOfGreenEventText.json :: dataList[id=reward_Noraml].content
   limit: do 120 znaków
   EN: Normal
   PL: Normalny
334. [Wydarzenia i Przepustka [reward_Hard] — tekst] 어려움
   źródło: DawnOfGreenEventText.json :: dataList[id=reward_Hard].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
335. [Wydarzenia i Przepustka [EVENT_NEWYEAR_2024_NORMAL] — tekst] 일반
   źródło: DawnOfGreenEventText.json :: dataList[id=EVENT_NEWYEAR_2024_NORMAL].content
   (powtórzenie elementu 333 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Wydarzenia i Przepustka [EVENT_NEWYEAR_2024_HARD] — tekst] 어려움
   źródło: DawnOfGreenEventText.json :: dataList[id=EVENT_NEWYEAR_2024_HARD].content
   (powtórzenie elementu 334 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Wydarzenia i Przepustka [missionConditionTitle_10001] — tekst] 1회 전투에서 녹빛 여명 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10001].content
   limit: do 120 znaków
   EN: Dawn of Green entities defeated in a single Encounter
   PL: Pokonaj istoty Zielonego Świtu w jednej walce
338. [Wydarzenia i Przepustka [missionConditionTitle_10002] — tekst] 1회 전투에서 녹빛 여명 - 의문 - γ 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10002].content
   limit: do 120 znaków
   EN: Dawn of Green - Doubt - γ entities defeated in a single Encounter
   PL: Pokonaj w jednej walce istoty Zielonego Świtu — Wątpliwość — γ
339. [Wydarzenia i Przepustka [missionConditionTitle_10003] — tekst] 1회 전투에서 녹빛 여명 - 의문 - δ 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10003].content
   limit: do 120 znaków
   EN: Dawn of Green - Doubt - δ entities defeated in a single Encounter
   PL: Pokonaj w jednej walce istoty Zielonego Świtu — Wątpliwość — δ
340. [Wydarzenia i Przepustka [missionConditionTitle_10004] — tekst] 모든 아군이 생존한 상태로 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10004].content
   limit: do 120 znaków
   EN: Complete Suppression without any ally deaths
   PL: Zakończ Tłumienie bez strat wśród sojuszników
341. [Wydarzenia i Przepustka [missionConditionTitle_10005] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10005].content
   limit: do 120 znaków
   EN: Complete Suppression without any of the allies' SP dropping to -45 SP
   PL: Zakończ Tłumienie, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
342. [Wydarzenia i Przepustka [missionConditionTitle_10006] — tekst] 공격 스킬 1회 사용으로 동시에 녹빛 여명 3 개체 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10006].content
   limit: do 120 znaków
   EN: Defeat 3 Dawn of Green entities with a single Attack Skill
   PL: Pokonaj 3 istoty Zielonego Świtu jednym użyciem Umiejętności ataku
343. [Wydarzenia i Przepustka [missionConditionTitle_10007] — tekst] 1회 전투에서 지휘팀 팀장이 공격 스킬로 녹빛 여명 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10007].content
   limit: do 130 znaków
   EN: Dawn of Green entities defeated by the Control Team Captain's Attack Skill in a single Encounter
   PL: Pokonaj w jednej walce istoty Zielonego Świtu Umiejętnością ataku Kapitana Zespołu Dowodzenia
344. [Wydarzenia i Przepustka [missionConditionTitle_10008] — tekst] 지휘팀 팀장이 적의 공격 스킬에 피해를 10회 미만으로 받고 생존한 상태로 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_10008].content
   limit: do 150 znaków
   EN: Complete Suppression with Control Team Captain surviving and taking less than 10 hits from enemy Attack Skills
   PL: Zakończ Tłumienie, w którym Kapitan Zespołu Dowodzenia przeżyje, otrzymawszy mniej niż 10 trafień Umiejętnościami ataku wroga
345. [Wydarzenia i Przepustka [missionConditionTitle_20001] — tekst] 1회 전투에서 녹빛 여명 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20001].content
   (powtórzenie elementu 337 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Wydarzenia i Przepustka [missionConditionTitle_20002] — tekst] 1회 전투에서 녹빛 여명 - 의문 - γ 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20002].content
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Wydarzenia i Przepustka [missionConditionTitle_20003] — tekst] 1회 전투에서 녹빛 여명 - 의문 - δ 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20003].content
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
348. [Wydarzenia i Przepustka [missionConditionTitle_20004] — tekst] 모든 아군이 생존한 상태로 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20004].content
   (powtórzenie elementu 340 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Wydarzenia i Przepustka [missionConditionTitle_20005] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20005].content
   (powtórzenie elementu 341 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Wydarzenia i Przepustka [missionConditionTitle_20006] — tekst] 공격 스킬 1회 사용으로 동시에 녹빛 여명 7 개체 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20006].content
   limit: do 120 znaków
   EN: Defeat 7 Dawn of Green entities with a single Attack Skill
   PL: Pokonaj 7 istot Zielonego Świtu jednym użyciem Umiejętności ataku
351. [Wydarzenia i Przepustka [missionConditionTitle_20007] — tekst] 1회 전투에서 지휘팀 팀장이 공격 스킬로 녹빛 여명 처치
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20007].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Wydarzenia i Przepustka [missionConditionTitle_20008] — tekst] 지휘팀 팀장이 적의 공격 스킬에 피해를 5회 미만으로 받고 생존한 상태로 제압 종료
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_20008].content
   limit: do 150 znaków
   EN: Complete Suppression with Control Team Captain surviving and taking less than 5 hits from enemy Attack Skills
   PL: Zakończ Tłumienie, w którym Kapitan Zespołu Dowodzenia przeżyje, otrzymawszy mniej niż 5 trafień Umiejętnościami ataku wroga
353. [Wydarzenia i Przepustka [missionConditionTitle_30001] — tekst] 일반, 어려움 난이도의 모든 미션 클리어
   źródło: DawnOfGreenEventText.json :: dataList[id=missionConditionTitle_30001].content
   limit: do 120 znaków
   EN: Complete all Missions in both Normal and Hard difficulties
   PL: Ukończ wszystkie misje na poziomach Normalnym i Trudnym
354. [Wydarzenia i Przepustka [dawnofgreen_rewardpage_desc] — tekst] 녹빛 여명의 시련 - 일반, 어려움 난이도 전투에서 녹빛 여명을 제압하며 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: DawnOfGreenEventText.json :: dataList[id=dawnofgreen_rewardpage_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Suppress Dawn of Green entities in 'Normal' and 'Hard' difficulties from the Dawn of Green Ordeal.\n\nEarn various rewards by clearing these missions.
   PL: Próba Zielonego Świtu — stłum istoty Zielonego Świtu na poziomach Normalnym i Trudnym i ukończ misje.\n\nZa ukończone misje otrzymasz różne nagrody.
355. [Wydarzenia i Przepustka [mainui_battleresult_wa] — tekst] 제압한 시련
   źródło: DawnOfGreenEventText.json :: dataList[id=mainui_battleresult_wa].content
   limit: do 120 znaków
   EN: Ordeals Suppressed
   PL: Stłumione próby

## Wydarzenia i Przepustka: EventCommonText
- plik gry: `EventCommonText.json`

356. [Wydarzenia i Przepustka [event_bonus_description] — tekst] 이벤트 기간 동안 해당 인격 및 E.G.O 편성 시,\n<color=#f8c200>[{0}]의 획득량이 상승</color>합니다.
   źródło: EventCommonText.json :: dataList[id=event_bonus_description].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, \n
   EN: During the event, having the listed Identities and E.G.O on your team\n<color=#f8c200>increases the amount of [{0}] earned</color>.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości i E.G.O,\n<color=#f8c200>zwiększasz zdobywanie [{0}]</color>.
357. [Wydarzenia i Przepustka [event_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: EventCommonText.json :: dataList[id=event_bonus_preview].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: EventLCBCheckupText
- plik gry: `EventLCBCheckupText.json`

358. [Wydarzenia i Przepustka [lcb_checkup_stagebutton_not_clear] — tekst] 7-36 클리어 시 개방
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_stagebutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 7-36 to Unlock
   PL: Odblokowanie po ukończeniu 7-36
359. [Wydarzenia i Przepustka [lcb_checkup_stagebutton_normal] — tekst] 스테이지
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_stagebutton_normal].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Wydarzenia i Przepustka [lcb_checkup_stagebutton_end_event] — tekst] 이벤트 기간 종료
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_stagebutton_end_event].content
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Wydarzenia i Przepustka [lcb_checkup_storybutton_before_start] — tekst] <size=75%>이벤트 첫 번째 이야기\n감상 시 개방</size>
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_storybutton_before_start].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=75%>, </size>, \n
   EN: <size=75%>View the 1st event Story Stage \nto Unlock</size>
   PL: <size=75%>Odblokowanie po obejrzeniu pierwszej\nfabuły wydarzenia</size>
362. [Wydarzenia i Przepustka [lcb_checkup_storybutton_normal] — tekst] 상영관 이동
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_storybutton_normal].content
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Wydarzenia i Przepustka [lcb_checkup_rewardShopButton] — tekst] 보상 교환
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_rewardShopButton].content
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Wydarzenia i Przepustka [lcb_checkup_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_scrap_guide_title].content
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Wydarzenia i Przepustka [lcb_checkup_scrap_guide_desc] — tekst] !!! 이거 사용하는 곳 없는지 확인하고 없으면 제거 !!! 이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 낮은 확률로<color=#ff99e6>[기밀서류]</color>를 획득할 수 있습니다.\n\n<color=#ff99e6>[기밀서류]</color>는 획득 즉시, <color=#ff99e6>[정보서류]</color> 20개로 전환됩니다.
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_scrap_guide_desc].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff99e6>, </color>, \n
   EN: !!! 이거 사용하는 곳 없는지 확인하고 없으면 제거 !!! Rarely, you may obtain <color=#ff99e6>[Classified Data]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons.\n\n<color=#ff99e6>[Classified Data]</color> is converted to 20 <color=#ff99e6>[Amassed Data] immediately upon acquisition</color>.
   PL: !!! Sprawdź, czy to jest gdziekolwiek używane — jeśli nie, usuń !!! Ukończywszy etapy wydarzenia lub Głównej Fabuły albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#ff99e6>[Poufne Dane]</color>.\n\n<color=#ff99e6>[Poufne Dane]</color> od razu zamieniają się na 20 <color=#ff99e6>[Zgromadzonych Danych]</color>.
366. [Wydarzenia i Przepustka [lcb_checkup_rewardpage_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어,\n거울 던전 클리어를 통해 <color=#ac1605>[정보서류]</color>를 획득할 수 있으며,\n낮은 확률로 <color=#ac1605>[기밀서류]</color>를 추가로 획득할 수 있습니다.\n\n<color=#ac1605>[기밀서류]</color>는 획득 즉시, <color=#ac1605>[정보서류]</color> 20개로 전환됩니다.
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_rewardpage_desc].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#ac1605>, </color>, \n
   EN: You can obtain <color=#ac1605>[Amassed Data]</color> from first-time Event/Main Story Stages completions, or by clearing the Mirror Dungeon.\nYou also have a small chance to obtain <color=#ac1605>[Classified Data]</color> in the process.\n\n<color=#ac1605>[Classified Data]</color> is immediately converted to 20 <color=#ac1605>[Amassed Data]</color> upon acquisition.
   PL: Zdobywaj <color=#ac1605>[Zgromadzone Dane]</color> za pierwsze ukończenia etapów wydarzenia i Głównej Fabuły oraz Lustrzane Lochy.\nDodatkowo z pewnym prawdopodobieństwem zdobędziesz <color=#ac1605>[Poufne Dane]</color>.\n\n<color=#ac1605>[Poufne Dane]</color> od razu zamieniają się na 20 <color=#ac1605>[Zgromadzonych Danych]</color>.
367. [Wydarzenia i Przepustka [lcb_checkup_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#ac1605>[정보서류]</color>를 획득할 수 있습니다.\n\n<color=#ac1605>[보상 교환]</color>창에서 <color=#ac1605>[정보서류]</color>를 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_reward_popup_desc].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ac1605>, </color>, \n
   EN: Earn <color=#ac1605>[Amassed Data]</color> via the following methods:\nFirst-time Event Stage & Dungeon clears and Mirror Dungeon clears.\n\nIn the <color=#ac1605>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#ac1605>[Amassed Data]</color> you have collected.
   PL: Zdobywaj <color=#ac1605>[Zgromadzone Dane]</color> przez:\npierwsze ukończenia etapów i lochów wydarzenia oraz Lustrzane Lochy.\n\nW oknie <color=#ac1605>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#ac1605>[Zgromadzone Dane]</color>.
368. [Wydarzenia i Przepustka [lcb_checkup_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_reward_popup_num_of_owned_items].content
   limit: do 120 znaków
   EN: Items Owned
   PL: Liczba posiadanych przedmiotów
369. [Wydarzenia i Przepustka [lcb_checkup_bonusUI_Title] — tekst] 증가
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_bonusUI_Title].content
   limit: do 120 znaków
   EN: Gain
   PL: Zysk
370. [Wydarzenia i Przepustka [lcb_checkup_bonusUI_Title_contain_false] — tekst] 미보유
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_bonusUI_Title_contain_false].content
   limit: do 120 znaków
   EN: Not Owned
   PL: Nieposiadane
371. [Wydarzenia i Przepustka [lcb_checkup_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 인격 및 E.G.O 편성 시, <color=#ac1605>[정보서류]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#ac1605>120%</color>까지 적용됩니다.
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_bonusUI_Desc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#ac1605>, </color>, \n
   EN: During the event period, deploying the following Identities or E.G.O on your team will\nboost the amount of <color=#ac1605>[Amassed Data]</color> earned.\nYou can earn a maximum of <color=#ac1605>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości i E.G.O, zwiększasz zdobywanie <color=#ac1605>[Zgromadzonych Danych]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#ac1605>120%</color>.
372. [Wydarzenia i Przepustka [lcb_checkup_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Wydarzenia i Przepustka [lcb_checkup_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: EventLCBCheckupText.json :: dataList[id=lcb_checkup_bonus_preview].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: EventLimbus1stAnnivText
- plik gry: `EventLimbus1stAnnivText.json`

374. [Wydarzenia i Przepustka [limbus_1st_anniversary_attendance_desc] — tekst] 이벤트 기간 동안 매일 접속 시, 추출 티켓을 획득할 수 있습니다.\n누적 7일, 14일 접속 시, 특별한 보상을 획득할 수 있습니다.
   źródło: EventLimbus1stAnnivText.json :: dataList[id=limbus_1st_anniversary_attendance_desc].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Get Extraction Tickets each day you log in during the event period.\nReceive special rewards by collecting 7 Attendance Checks.
   PL: Za każde zalogowanie w okresie wydarzenia otrzymujesz Bilety Ekstrakcji.\nZa 7 dni obecności otrzymasz specjalne nagrody.
375. [Wydarzenia i Przepustka [limbus_1st_anniversary_attendance_last_reward_desc] — tekst] 해당 아나운서를 이미 가지고 있다면 끈 상자 50개로 전환되어 획득하게 됩니다.
   źródło: EventLimbus1stAnnivText.json :: dataList[id=limbus_1st_anniversary_attendance_last_reward_desc].content
   limit: do 120 znaków
   EN: If you have already acquired the Announcer, you will receive 50 Thread Crates instead.
   PL: Jeśli masz już tego Komentatora, otrzymasz 50 Skrzynek Nici.
376. [Wydarzenia i Przepustka [limbus_1st_anniversary_welcome_title] — tekst] 림버스 컴퍼니 1주년
   źródło: EventLimbus1stAnnivText.json :: dataList[id=limbus_1st_anniversary_welcome_title].content
   limit: do 120 znaków
   EN: Limbus Company 1st Anniversary
   PL: 1. rocznica Limbus Company
377. [Wydarzenia i Przepustka [limbus_1st_anniversary_welcome_desc] — tekst] 기간 내 접속 시 3성 인격 출현 추출 티켓 증정!
   źródło: EventLimbus1stAnnivText.json :: dataList[id=limbus_1st_anniversary_welcome_desc].content
   limit: do 120 znaków
   EN: Log in during the event and pick up a [3★ Guarantee Decaextraction Ticket]!
   PL: Zaloguj się w okresie wydarzenia i odbierz Bilet Dekstrakcji Gwarantowanej 3★!

## Wydarzenia i Przepustka: EventLimbus2ndAnnivText
- plik gry: `EventLimbus2ndAnnivText.json`

378. [Wydarzenia i Przepustka [limbus_2nd_anniversary_first_reward_slot_tag] — tekst] 첫 접속
   źródło: EventLimbus2ndAnnivText.json :: dataList[id=limbus_2nd_anniversary_first_reward_slot_tag].content
   limit: do 120 znaków
   EN: First Login
   PL: Pierwsze logowanie
379. [Wydarzenia i Przepustka [limbus_2nd_anniversary_attendance_last_reward_slot_desc] — tekst] 해당 아나운서를 이미 가지고 있다면 끈 상자 50개로 전환되어 획득하게 됩니다.
   źródło: EventLimbus2ndAnnivText.json :: dataList[id=limbus_2nd_anniversary_attendance_last_reward_slot_desc].content
   (powtórzenie elementu 375 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: EventMOWEText
- plik gry: `EventMOWEText.json`

380. [Wydarzenia i Przepustka [mowe_stagebutton_not_clear] — tekst] 6.5-15 클리어 시 개방
   źródło: EventMOWEText.json :: dataList[id=mowe_stagebutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 6.5-15 to Unlock
   PL: Odblokowanie po ukończeniu 6.5-15
381. [Wydarzenia i Przepustka [mowe_stagebutton_normal] — tekst] 스테이지
   źródło: EventMOWEText.json :: dataList[id=mowe_stagebutton_normal].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Wydarzenia i Przepustka [mowe_stagebutton_end_event] — tekst] 이벤트 기간 종료
   źródło: EventMOWEText.json :: dataList[id=mowe_stagebutton_end_event].content
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Wydarzenia i Przepustka [mowe_storybutton_before_start] — tekst] <size=75%>이벤트 첫 번째 이야기\n감상 시 개방</size>
   źródło: EventMOWEText.json :: dataList[id=mowe_storybutton_before_start].content
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Wydarzenia i Przepustka [mowe_storybutton_normal] — tekst] 상영관 이동
   źródło: EventMOWEText.json :: dataList[id=mowe_storybutton_normal].content
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Wydarzenia i Przepustka [mowe_rewardShopButton] — tekst] 보상 교환
   źródło: EventMOWEText.json :: dataList[id=mowe_rewardShopButton].content
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Wydarzenia i Przepustka [mowe_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: EventMOWEText.json :: dataList[id=mowe_scrap_guide_title].content
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Wydarzenia i Przepustka [mowe_scrap_guide_desc] — tekst] 이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 낮은 확률로<color=#ff99e6>[해결사 승객 복구팩]</color>을 획득할 수 있습니다.\n\n<color=#ff99e6>[해결사 승객 복구팩]</color>은 획득 즉시, <color=#ff99e6>[일반 승객 복구팩]</color> 20개로 전환됩니다.
   źródło: EventMOWEText.json :: dataList[id=mowe_scrap_guide_desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#ff99e6>, </color>, \n
   EN: Rarely, you may obtain <color=#ff99e6>[Fixer Recov. Pack]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons.\n\n<color=#ff99e6>[Fixer Recov. Pack]</color> is immediately converted to 20 <color=#ff99e6>[Civilian Recov. Pack]</color> upon acquisition.
   PL: Ukończywszy etapy wydarzenia lub Głównej Fabuły albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#ff99e6>[Pakiet Rekonstrukcyjny Fiksera]</color>.\n\n<color=#ff99e6>[Pakiet Rekonstrukcyjny Fiksera]</color> od razu zamienia się na 20 <color=#ff99e6>[Pakietów Rekonstrukcyjnych Pasażera]</color>.
388. [Wydarzenia i Przepustka [mowe_rewardpage_desc] — tekst] 이벤트 스테이지를 클리어할 때마다 <color=#ff99e6>[일반 승객 복구팩]</color>을 획득할 수 있습니다. 이외에도 주요 이야기\n스테이지를 최초로 클리어하거나 거울 던전 클리어 시, <color=#ff99e6>[일반 승객 복구팩]</color>을 획득할 수 있습니다.\n\n이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 낮은 확률로 <color=#ff99e6>[해결사 승객 복구팩]</color>을 획득할 수 있으며, <color=#ff99e6>[해결사 승객 복구팩]</color>은 획득 즉시 <color=#ff99e6>[일반 승객 복구팩]</color> 20개로 전환됩니다.\n\n<color=#ff99e6>[보상 교환]</color> 창에서 <color=#ff99e6>[일반 승객 복구팩]</color>을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventMOWEText.json :: dataList[id=mowe_rewardpage_desc].content
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: <color=#ff99e6>, </color>, \n
   EN: During the event, you can earn <color=#ff99e6>[Civilian Recov. Pack]</color> by clearing event Stages. You can also obtain <color=#ff99e6>[Civilian Recov. Pack]</color> by clearing Main Story Stages for the first time, or by clearing the Mirror Dungeon.\n\nRarely, you may obtain <color=#ff99e6>[Fixer Recov. Pack]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons,\nand <color=#ff99e6>[Fixer Recov. Pack]</color> is automatically converted to 20 <color=#ff99e6>[Civilian Recov. Pack]</color> upon acquisition.\n\nIn the <color=#ff99e6>[Reward Exchange]</color> window, you can purchase various rewards by spending <color=#ff99e6>[Civilian Recov. Pack]</color> you have collected.
   PL: Ukończoną każdą etap wydarzenia, zdobywasz <color=#ff99e6>[Pakiet Rekonstrukcyjny Pasażera]</color>. Możesz go także zdobyć za pierwsze ukończenia etapów Głównej Fabuły lub Lustrzane Lochy.\n\nUkończywszy etapy wydarzenia lub Głównej Fabuły albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#ff99e6>[Pakiet Rekonstrukcyjny Fiksera]</color>, który od razu zamienia się na 20 <color=#ff99e6>[Pakietów Rekonstrukcyjnych Pasażera]</color>.\n\nW oknie <color=#ff99e6>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#ff99e6>[Pakiety Rekonstrukcyjne Pasażera]</color>.
389. [Wydarzenia i Przepustka [mowe_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기\n최초 클리어, 거울 던전 클리어를 통해\n<color=#ff99e6>[일반 승객 복구팩]</color>을 획득할 수 있습니다.\n\n<color=#ff99e6>[보상 교환]</color> 창에서 <color=#ff99e6>[일반 승객 복구팩]</color>을\n지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventMOWEText.json :: dataList[id=mowe_reward_popup_desc].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#ff99e6>, </color>, \n
   EN: Earn <color=#ff99e6>[Civilian Recov. Pack]</color> via the following methods:\nEvent Stage & Dungeon clears, Mirror Dungeon clears,\nand Main Story Stage & Dungeon first-time clears.\n\nIn the <color=#ff99e6>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#ff99e6>[Civilian Recov. Pack]</color> you have collected.
   PL: Zdobywaj <color=#ff99e6>[Pakiet Rekonstrukcyjny Pasażera]</color> przez:\nukończenia etapów wydarzenia i lochów oraz pierwsze ukończenia etapów i lochów Głównej Fabuły, a także Lustrzane Lochy.\n\nW oknie <color=#ff99e6>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#ff99e6>[Pakiety Rekonstrukcyjne Pasażera]</color>.
390. [Wydarzenia i Przepustka [mowe_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: EventMOWEText.json :: dataList[id=mowe_reward_popup_num_of_owned_items].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Wydarzenia i Przepustka [mowe_bonusUI_Title] — tekst] 증가
   źródło: EventMOWEText.json :: dataList[id=mowe_bonusUI_Title].content
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Wydarzenia i Przepustka [mowe_bonusUI_Title_contain_false] — tekst] 미보유
   źródło: EventMOWEText.json :: dataList[id=mowe_bonusUI_Title_contain_false].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Wydarzenia i Przepustka [mowe_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 인격, E.G.O 편성 시, <color=#ff99e6>[일반 승객 복구팩]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#ff99e6>120%</color>까지 적용됩니다.
   źródło: EventMOWEText.json :: dataList[id=mowe_bonusUI_Desc].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#ff99e6>, </color>, \n
   EN: During the event period, deploying the following Identities or E.G.O on your team will\nboost the amount of <color=#ff99e6>[Civilian Recov. Pack]</color> earned.\nYou can earn a maximum of <color=#ff99e6>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości i E.G.O, zwiększasz zdobywanie <color=#ff99e6>[Pakietów Rekonstrukcyjnych Pasażera]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#ff99e6>120%</color>.
394. [Wydarzenia i Przepustka [mowe_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: EventMOWEText.json :: dataList[id=mowe_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Wydarzenia i Przepustka [mowe_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: EventMOWEText.json :: dataList[id=mowe_bonus_preview].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Wydarzenia i Przepustka [mowe_chapter_map_difficulty_ui_unlock_condition] — tekst] {0}-{1} 이후 어려움 난이도 개방
   źródło: EventMOWEText.json :: dataList[id=mowe_chapter_map_difficulty_ui_unlock_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Clear {0}-{1} to Unlock the Hard Difficulty
   PL: Po ukończeniu {0}-{1} odblokujesz Poziom Trudności

## Wydarzenia i Przepustka: EventMiracleText
- plik gry: `EventMiracleText.json`

397. [Wydarzenia i Przepustka [miracle_stagebutton_not_clear_cp4] — tekst] {0}장은 클리어하고 와!
   źródło: EventMiracleText.json :: dataList[id=miracle_stagebutton_not_clear_cp4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Go clear Canto {0} first!
   PL: Najpierw ukończ Cant {0}!
398. [Wydarzenia i Przepustka [miracle_stagebutton_normal] — tekst] 시계 대가리! 빨리 튀어와!
   źródło: EventMiracleText.json :: dataList[id=miracle_stagebutton_normal].content
   limit: do 120 znaków
   EN: Oi, Clockhead! Get crackin'!
   PL: O, zegarowa głowo! Pokazuj się prędzej!
399. [Wydarzenia i Przepustka [miracle_stagebutton_end_event] — tekst] 늦었잖아! 이벤트 끝났어!
   źródło: EventMiracleText.json :: dataList[id=miracle_stagebutton_end_event].content
   limit: do 120 znaków
   EN: You're late! Event's shut!
   PL: Za późno! Wydarzenie się skończyło!
400. [Wydarzenia i Przepustka [miracle_storybutton_before_start] — tekst] 5.5-1 클리어 시 개방
   źródło: EventMiracleText.json :: dataList[id=miracle_storybutton_before_start].content
   limit: do 120 znaków
   EN: Clear 5.5-1 to Unlock
   PL: Odblokowanie po ukończeniu 5.5-1
401. [Wydarzenia i Przepustka [miracle_storybutton_normal] — tekst] 이것은 모험의 기록이네!
   źródło: EventMiracleText.json :: dataList[id=miracle_storybutton_normal].content
   limit: do 120 znaków
   EN: Revisit thine adventures!
   PL: To zapis twej przygody!
402. [Wydarzenia i Przepustka [miracle_exchange_scrap] — tekst] 보상 교환
   źródło: EventMiracleText.json :: dataList[id=miracle_exchange_scrap].content
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Wydarzenia i Przepustka [miracle_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: EventMiracleText.json :: dataList[id=miracle_scrap_guide_title].content
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Wydarzenia i Przepustka [miracle_scrap_guide_desc] — tekst] 이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 <color=#008d0d>[장식 꾸러미]</color>를\n획득할 수 있으며, 낮은 확률로 <color=#008d0d>[거대한 장식 꾸러미]</color>를 추가로 획득할 수 있습니다.\n\n<color=#008d0d>[거대한 장식 꾸러미]</color>는 획득 즉시, <color=#008d0d>[장식 꾸러미]</color> 20개로 전환됩니다.
   źródło: EventMiracleText.json :: dataList[id=miracle_scrap_guide_desc].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#008d0d>, </color>, \n
   EN: You can obtain <color=#008d0d>[Trinkets Sack]</color> by completing Event/Main Story Stages or the Mirror Dungeon.\nYou also have a small chance to obtain <color=#008d0d>[Huge Trinkets Sack]</color> in the process.\n\n<color=#008d0d>[Huge Trinkets Sack]</color> is immediately converted to 20 <color=#008d0d>[Trinkets Sack]</color> upon acquisition.
   PL: Ukończywszy etapy wydarzenia lub Głównej Fabuły albo Lustrzane Lochy, zdobędziesz <color=#008d0d>[Worek Ozdób]</color>, a z pewnym prawdopodobieństwem dodatkowo <color=#008d0d>[Wielki Worek Ozdób]</color>.\n\n<color=#008d0d>[Wielki Worek Ozdób]</color> od razu zamienia się na 20 <color=#008d0d>[Worków Ozdób]</color>.
405. [Wydarzenia i Przepustka [miracle_rewardpage_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#008d0d>[장식 꾸러미]</color>를 획득할 수 있습니다.\n\n<color=#008d0d>[보상 교환]</color>창에서 <color=#008d0d>[장식 꾸러미]</color>를 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventMiracleText.json :: dataList[id=miracle_rewardpage_desc].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#008d0d>, </color>, \n
   EN: Earn <color=#008d0d>[Trinkets Sack]</color> via the following methods:\nFirst-time Event Stage & Dungeon clears and Mirror Dungeon clears.\n\nIn the <color=#008d0d>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#008d0d>[Trinkets Sack]</color> you have collected.
   PL: Zdobywaj <color=#008d0d>[Worek Ozdób]</color> przez:\npierwsze ukończenia etapów wydarzenia i Głównej Fabuły oraz Lustrzane Lochy.\n\nW oknie <color=#008d0d>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#008d0d>[Worki Ozdób]</color>.
406. [Wydarzenia i Przepustka [miracle_scrap_counter_label] — tekst] 수집한 장식 꾸러미
   źródło: EventMiracleText.json :: dataList[id=miracle_scrap_counter_label].content
   limit: do 120 znaków
   EN: Trinkets Sacks Collected
   PL: Zdobyte Worki Ozdób
407. [Wydarzenia i Przepustka [miracle_chapter_map_difficulty_ui_9105] — tekst] NORMAL
   źródło: EventMiracleText.json :: dataList[id=miracle_chapter_map_difficulty_ui_9105].content
   limit: do 120 znaków
   EN: NORMAL
   PL: NORMAL
408. [Wydarzenia i Przepustka [miracle_chapter_map_difficulty_ui_9112] — tekst] HARD
   źródło: EventMiracleText.json :: dataList[id=miracle_chapter_map_difficulty_ui_9112].content
   limit: do 120 znaków
   EN: HARD
   PL: HARD
409. [Wydarzenia i Przepustka [miracle_chapter_map_difficulty_ui_hard_chapter_unlock_condition] — tekst] {0}-{1} 이후 하드 모드 개방
   źródło: EventMiracleText.json :: dataList[id=miracle_chapter_map_difficulty_ui_hard_chapter_unlock_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Clear {0}-{1} to Unlock the Hard Mode
   PL: Po ukończeniu {0}-{1} odblokujesz Poziom Trudny
410. [Wydarzenia i Przepustka [miracle_chapter_map_difficulty_ui_event_date_format] — tekst] {0}월 {1}일까지
   źródło: EventMiracleText.json :: dataList[id=miracle_chapter_map_difficulty_ui_event_date_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Until {0}/{1}
   PL: Do {0}/{1}
411. [Wydarzenia i Przepustka [miracle_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 E.G.O 편성 시, <color=#008d0d>[장식 꾸러미]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#008d0d>120%</color>까지 적용됩니다.
   źródło: EventMiracleText.json :: dataList[id=miracle_bonusUI_Desc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#008d0d>, </color>, \n
   EN: During the event period, deploying the following E.G.O on your team will\nboost the amount of <color=#008d0d>[Trinkets Sack]</color> earned.\nYou can earn a maximum of <color=#008d0d>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane E.G.O, zwiększasz zdobywanie <color=#008d0d>[Worków Ozdób]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#008d0d>120%</color>.
412. [Wydarzenia i Przepustka [miracle_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: EventMiracleText.json :: dataList[id=miracle_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: EventTKTText
- plik gry: `EventTKTText.json`

413. [Wydarzenia i Przepustka [tkt_stagebutton_not_clear] — tekst] 6-48 클리어 시 개방
   źródło: EventTKTText.json :: dataList[id=tkt_stagebutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 6-48 to Unlock
   PL: Odblokowanie po ukończeniu 6-48
414. [Wydarzenia i Przepustka [tkt_stagebutton_normal] — tekst] 스테이지
   źródło: EventTKTText.json :: dataList[id=tkt_stagebutton_normal].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Wydarzenia i Przepustka [tkt_stagebutton_end_event] — tekst] 이벤트 기간 종료
   źródło: EventTKTText.json :: dataList[id=tkt_stagebutton_end_event].content
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
416. [Wydarzenia i Przepustka [tkt_storybutton_before_start] — tekst] <size=75%>이벤트 첫 번째 이야기 감상 시 개방</size>
   źródło: EventTKTText.json :: dataList[id=tkt_storybutton_before_start].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=75%>, </size>
   EN: <size=75%>View the 1st event Story Stage to Unlock</size>
   PL: <size=75%>Odblokowanie po obejrzeniu pierwszej fabuły wydarzenia</size>
417. [Wydarzenia i Przepustka [tkt_storybutton_normal] — tekst] 상영관 이동
   źródło: EventTKTText.json :: dataList[id=tkt_storybutton_normal].content
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Wydarzenia i Przepustka [tkt_rewardShopButton] — tekst] 보상 교환
   źródło: EventTKTText.json :: dataList[id=tkt_rewardShopButton].content
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Wydarzenia i Przepustka [tkt_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: EventTKTText.json :: dataList[id=tkt_scrap_guide_title].content
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Wydarzenia i Przepustka [tkt_scrap_guide_desc] — tekst] 이벤트와 주요 이야기의 스테이지 및 던전 또는 거울 던전을 클리어하면 낮은 확률로</color> <color=#c69136>[회중시계 묶음]</color>을 획득할 수 있습니다.\n\n<color=#c69136>[회중시계 묶음]</color>은 획득 즉시, <color=#c69136>[회중시계]</color> 20개로 전환됩니다.
   źródło: EventTKTText.json :: dataList[id=tkt_scrap_guide_desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: </color>, <color=#c69136>, \n
   EN: Rarely, you may obtain </color>[Pocket Watch Bundle]<color=#c69136> from clearing Event Stages, Main Story Stages, or Mirror Dungeons.\n\n</color>[Pocket Watch Bundle]<color=#c69136> is immediately converted to 20 </color>[Pocket Watch]<color=#c69136> upon acquisition.
   PL: Ukończywszy etapy wydarzenia, Głównej Fabuły oraz lochy albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz </color> <color=#c69136>[Pęk Zegarków Kieszonkowych]</color>.\n\n<color=#c69136>[Pęk Zegarków Kieszonkowych]</color> od razu zamienia się na 20 <color=#c69136>[Zegarków Kieszonkowych]</color>.
421. [Wydarzenia i Przepustka [tkt_rewardpage_desc] — tekst] 이벤트 스테이지와 던전을 클리어할 때마다 <color=#c69136>[회중시계]</color>를 획득할 수 있습니다. 이외에도 주요 이야기\n스테이지와 던전을 최초로 클리어하거나 거울 던전 클리어 시, <color=#c69136>[회중시계]</color>를 획득할 수 있습니다.\n\n이벤트와 주요 이야기의 스테이지 및 던전 또는 거울 던전을 클리어하면 낮은 확률로 <color=#c69136>[회중시계 묶음]</color>을 획득할 수 있으며, <color=#c69136>[회중시계 묶음]</color>은 획득 즉시 <color=#c69136>[회중시계]</color> 20개로 전환됩니다.\n\n<color=#c69136>[보상 교환]</color> 창에서 <color=#c69136>[회중시계]</color>를 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventTKTText.json :: dataList[id=tkt_rewardpage_desc].content
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: <color=#c69136>, </color>, \n
   EN: During the event, you can earn <color=#c69136>[Pocket Watch]</color> by clearing event Stages and Dungeons. You can also obtain <color=#c69136>[Pocket Watch]</color> by clearing Main Story Stages or Dungeons for the first time, or clearing the Mirror Dungeon.\n\nRarely, you may obtain <color=#c69136>[Pocket Watch Bundle]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons,\nand <color=#c69136>[Pocket Watch Bundle]</color> is automatically converted to 20 <color=#c69136>[Pocket Watch]</color> upon acquisition.\n\nIn the <color=#c69136>[Reward Exchange]</color> window, you can purchase various rewards by spending <color=#c69136>[Pocket Watch]</color> you have collected.
   PL: Ukończoną każdą etap wydarzenia i loch, zdobywasz\n<color=#c69136>[Zegarek Kieszonkowy]</color>. Możesz go także zdobyć za pierwsze ukończenia etapów i lochów Głównej Fabuły lub Lustrzane Lochy.\n\nUkończywszy etapy wydarzenia, Głównej Fabuły i lochy albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#c69136>[Pęk Zegarków Kieszonkowych]</color>, który od razu zamienia się na 20 <color=#c69136>[Zegarków Kieszonkowych]</color>.\n\nW oknie <color=#c69136>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#c69136>[Zegarki Kieszonkowe]</color>.
422. [Wydarzenia i Przepustka [tkt_reward_popup_desc] — tekst] 이벤트 스테이지와 던전, 주요 이야기\n최초 클리어, 거울 던전 클리어를 통해\n<color=#c69136>[회중시계]</color>를 획득할 수 있습니다.\n\n<color=#c69136>[보상 교환]</color> 창에서 <color=#c69136>[회중시계]</color>를\n지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventTKTText.json :: dataList[id=tkt_reward_popup_desc].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#c69136>, </color>, \n
   EN: Earn <color=#c69136>[Pocket Watch]</color> via the following methods:\nEvent Stage & Dungeon clears, Mirror Dungeon clears,\nand Main Story Stage & Dungeon first-time clears.\n\nIn the <color=#c69136>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#c69136>[Pocket Watch]</color> you have collected.
   PL: Zdobywaj <color=#c69136>[Zegarek Kieszonkowy]</color> przez:\nukończenia etapów wydarzenia i lochów, pierwsze ukończenia\netapów i lochów Głównej Fabuły oraz Lustrzane Lochy.\n\nW oknie <color=#c69136>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#c69136>[Zegarki Kieszonkowe]</color>.
423. [Wydarzenia i Przepustka [tkt_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: EventTKTText.json :: dataList[id=tkt_reward_popup_num_of_owned_items].content
   (powtórzenie elementu 368 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Wydarzenia i Przepustka [tkt_bonusUI_Title] — tekst] 증가
   źródło: EventTKTText.json :: dataList[id=tkt_bonusUI_Title].content
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Wydarzenia i Przepustka [tkt_bonusUI_Title_contain_false] — tekst] 미보유
   źródło: EventTKTText.json :: dataList[id=tkt_bonusUI_Title_contain_false].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [Wydarzenia i Przepustka [tkt_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 인격, E.G.O 편성 시, <color=#c69136>[회중시계]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#c69136>120%</color>까지 적용됩니다.
   źródło: EventTKTText.json :: dataList[id=tkt_bonusUI_Desc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#c69136>, </color>, \n
   EN: During the event period, deploying the following Identities or E.G.O on your team will\nboost the amount of <color=#c69136>[Pocket Watch]</color> earned.\nYou can earn a maximum of <color=#c69136>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości i E.G.O, zwiększasz zdobywanie <color=#c69136>[Zegarków Kieszonkowych]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#c69136>120%</color>.
427. [Wydarzenia i Przepustka [tkt_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: EventTKTText.json :: dataList[id=tkt_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Wydarzenia i Przepustka [tkt_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: EventTKTText.json :: dataList[id=tkt_bonus_preview].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Wydarzenia i Przepustka [tkt_chapter_map_difficulty_ui_unlock_condition] — tekst] {0}-{1} 이후 어려움 난이도 개방
   źródło: EventTKTText.json :: dataList[id=tkt_chapter_map_difficulty_ui_unlock_condition].content
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: EventUmidaText
- plik gry: `EventUmidaText.json`

430. [Wydarzenia i Przepustka [umida_stagebutton_not_clear_cp4] — tekst] 4-54 클리어 시 개방
   źródło: EventUmidaText.json :: dataList[id=umida_stagebutton_not_clear_cp4].content
   limit: do 120 znaków
   EN: Clear 4-54 to Unlock
   PL: Odblokowanie po ukończeniu 4-54
431. [Wydarzenia i Przepustka [umida_stagebutton_normal] — tekst] 폐품 수집
   źródło: EventUmidaText.json :: dataList[id=umida_stagebutton_normal].content
   limit: do 120 znaków
   EN: Gather Scrap
   PL: Zbieraj Złom
432. [Wydarzenia i Przepustka [umida_stagebutton_end_event] — tekst] 이벤트 종료
   źródło: EventUmidaText.json :: dataList[id=umida_stagebutton_end_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Wydarzenie zakończone
433. [Wydarzenia i Przepustka [umida_storybutton_before_start] — tekst] 4.5-1 클리어 시 개방
   źródło: EventUmidaText.json :: dataList[id=umida_storybutton_before_start].content
   limit: do 120 znaków
   EN: Clear 4.5-1 to Unlock
   PL: Odblokowanie po ukończeniu 4.5-1
434. [Wydarzenia i Przepustka [umida_storybutton_normal] — tekst] 회상하기
   źródło: EventUmidaText.json :: dataList[id=umida_storybutton_normal].content
   limit: do 120 znaków
   EN: Recollect
   PL: Wspomnij wspomnienia
435. [Wydarzenia i Przepustka [umida_exchange_scrap] — tekst] 폐품 수집함
   źródło: EventUmidaText.json :: dataList[id=umida_exchange_scrap].content
   limit: do 120 znaków
   EN: Scrap Box
   PL: Pojemnik na Złom
436. [Wydarzenia i Przepustka [umida_scrap_guide_title] — tekst] 특별한 폐품
   źródło: EventUmidaText.json :: dataList[id=umida_scrap_guide_title].content
   limit: do 120 znaków
   EN: Extraordinary Scrap
   PL: Niezwykły Złom
437. [Wydarzenia i Przepustka [umida_scrap_guide_desc] — tekst] 이벤트 혹은 주요 이야기의 스테이지와 던전을 클리어하면\n낮은 확률로 <color=#f8c200>[희귀한 말굽이 포함된 버스 개조용 폐품]</color>을 획득할 수 있습니다.\n\n<color=#f8c200>[희귀한 말굽이 포함된 버스 개조용 폐품]</color>은 <color=#f8c200>[버스 개조용 폐품]</color> 20개로 전환됩니다.
   źródło: EventUmidaText.json :: dataList[id=umida_scrap_guide_desc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: Rarely, you may obtain <color=#f8c200>[Rare Horseshoe with Bus-modifying Scrap]</color> from clearing Event Stages, Main Story Stages, or Dungeons.\n\n<color=#f8c200>[Rare Horseshoe with Bus-modifying Scrap]</color> is converted to 20 <color=#f8c200>[Bus-modifying Scrap]</color>.
   PL: Ukończywszy etapy wydarzenia lub Głównej Fabuły, z pewnym prawdopodobieństwem zdobędziesz <color=#f8c200>[Złom do Modernizacji Autobusu z Rzadką Podkową]</color>.\n\n<color=#f8c200>[Złom do Modernizacji Autobusu z Rzadką Podkową]</color> zamienia się na 20 <color=#f8c200>[Złomu do Modernizacji Autobusu]</color>.
438. [Wydarzenia i Przepustka [umida_rewardpage_desc] — tekst] 이벤트 혹은 주요 이야기의 스테이지와 던전을 클리어하여 <color=#f8c200>[버스 개조용 폐품]</color>을 획득할 수 있습니다.\n\n획득한 <color=#f8c200>[버스 개조용 폐품]</color> 수량에 비례하여 <color=#f8c200>[폐품 수집함]</color>에서 다양한 보상을 얻을 수 있습니다.
   źródło: EventUmidaText.json :: dataList[id=umida_rewardpage_desc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: Clear Event Stages, Main Story Stages, or Dungeons to earn <color=#f8c200>[Bus-modifying Scrap]</color>.\n\nYou can redeem various rewards from the <color=#f8c200>[Scrap Box]</color> based on the number of <color=#f8c200>[Bus-modifying Scrap]</color> you have.
   PL: Ukończywszy etapy wydarzenia lub Głównej Fabuły, zdobędziesz <color=#f8c200>[Złom do Modernizacji Autobusu]</color>.\n\nProporcjonalnie do ilości <color=#f8c200>[Złomu do Modernizacji Autobusu]</color> możesz odbierać różne nagrody w <color=#f8c200>[Pojemniku na Złom]</color>.
439. [Wydarzenia i Przepustka [umida_scrap_counter_label] — tekst] 수집한 폐품 수량
   źródło: EventUmidaText.json :: dataList[id=umida_scrap_counter_label].content
   limit: do 120 znaków
   EN: Scrap Collected
   PL: Zebrany Złom

## Wydarzenia i Przepustka: EventVerificationUIText
- plik gry: `EventVerificationUIText.json`

440. [Wydarzenia i Przepustka [event_verification_btn] — tekst] 프로젝트문 10주년 패스 인증
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_btn].content
   limit: do 120 znaków
   EN: Project Moon 10th Anniv. Pass Verification
   PL: Weryfikacja Przepustki 10-lecia Project Moon
441. [Wydarzenia i Przepustka [event_verification_popup_title] — tekst] 프로젝트문 10주년 패스 인증
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_popup_title].content
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Wydarzenia i Przepustka [event_verification_popup_desc] — tekst] 현장 스태프분에게 이 화면을 보여 주세요.\n인증 코드는 스태프분이 직접 입력합니다.\n\n<b><color=#990000>관리자께서 임의로 인증한 계정은 재인증할 수 없어\n현장에서 입장 팔찌 교환 및 공연장 입장이 불가합니다.</color></b>
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_popup_desc].content
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <b>, <color=#990000>, </color>, </b>, \n
   EN: Please show this screen to a staff member at the venue.\nA staff member will input the verification code.\n\n<b><color=#990000>Please note that, should you verify this account on your own, it cannot be re-verified at the venue. This means that you will not be able to receive the entrance bracelet at the venue or enter the concert hall itself.</color></b>
   PL: Pokaż ten ekran personelowi na miejscu.\nKod weryfikacji wprowadzi personel.\n\n<b><color=#990000>Jeśli zweryfikujesz konto samodzielnie, nie będzie można zweryfikować go ponownie na miejscu — oznacza to, że nie otrzymasz na miejscu opaski wstępu ani nie wejdziesz na koncert.</color></b>
443. [Wydarzenia i Przepustka [event_verification_authenticate_btn] — tekst] 인증하기
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_authenticate_btn].content
   limit: do 120 znaków
   EN: Verify
   PL: Zweryfikuj
444. [Wydarzenia i Przepustka [event_verification_confirm_desc] — tekst] 현장 스태프가 인증하지 않은 경우에는 콘서트 팔찌 착용 및 입장이 제한됩니다. 정말 진행하시겠습니까?
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_confirm_desc].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unless this verification process is handled by an on-site staff member, you will not be able to receive the entrance bracelet or enter the concert hall.\nAre you sure you want to proceed?
   PL: Jeśli personel na miejscu nie przeprowadzi weryfikacji, opaska koncertowa i wstęp nie będą dostępne. Czy na pewno chcesz kontynuować?
445. [Wydarzenia i Przepustka [event_verification_retry_btn] — tekst] 다시 확인
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_retry_btn].content
   limit: do 120 znaków
   EN: Retry
   PL: Spróbuj ponownie
446. [Wydarzenia i Przepustka [event_verification_staff_code_placeholder] — tekst] 스태프 전용 인증 코드
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_staff_code_placeholder].content
   limit: do 120 znaków
   EN: Staff Verification Code
   PL: Kod weryfikacji wyłącznie dla personelu
447. [Wydarzenia i Przepustka [event_verification_input_verified] — tekst] 인증 완료 계정 (재인증 불가)
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_input_verified].content
   limit: do 120 znaków
   EN: Verified Account (Cannot re-verify)
   PL: Zweryfikowane konto (Nie można zweryfikować ponownie)
448. [Wydarzenia i Przepustka [event_verification_verified] — tekst] 인증이 완료되었습니다.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_verified].content
   limit: do 120 znaków
   EN: Account verification completed.
   PL: Weryfikacja zakończona.
449. [Wydarzenia i Przepustka [event_verification_already_verified] — tekst] 이미 인증이 완료된 계정입니다. (재인증 불가)
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_already_verified].content
   limit: do 120 znaków
   EN: This account has already been verified. (Cannot re-verify)
   PL: To konto zostało już zweryfikowane. (Nie można zweryfikować ponownie)
450. [Wydarzenia i Przepustka [event_verification_verified_at] — tekst] 인증 일시: {0} (KST)
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_verified_at].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Verification Date: {0} (KST)
   PL: Data weryfikacji: {0} (KST)
451. [Wydarzenia i Przepustka [event_verification_level_required] — tekst] 관리자 레벨 {0} 이상 달성한 계정만 인증할 수 있습니다.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_level_required].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Only accounts with Manager Level {0} or higher may proceed with the verification.
   PL: Weryfikacja dostępna tylko dla kont z poziomem Menedżera {0} lub wyższym.
452. [Wydarzenia i Przepustka [event_verification_not_started] — tekst] 아직 인증 기간이 아닙니다.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_not_started].content
   limit: do 120 znaków
   EN: Now is not the verification period.
   PL: Okres weryfikacji jeszcze się nie rozpoczął.
453. [Wydarzenia i Przepustka [event_verification_ended] — tekst] 인증 기간이 종료되었습니다.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_ended].content
   limit: do 120 znaków
   EN: Verification period has passed.
   PL: Okres weryfikacji dobiegł końca.
454. [Wydarzenia i Przepustka [event_verification_locked] — tekst] <b><color=#990000>인증 코드를 3회 잘못 입력했습니다.</color></b>\n{0}초 후 다시 시도해 주세요.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_locked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <b>, <color=#990000>, </color>, </b>, {0}, \n
   EN: <b><color=#990000>3 incorrect verification code attempts.</color></b>\nPlease try again after {0} seconds.
   PL: <b><color=#990000>Kod weryfikacji błędnie wprowadzono 3 razy.</color></b>\nSpróbuj ponownie za {0} sekund.
455. [Wydarzenia i Przepustka [event_verification_invalid_code] — tekst] <b><color=#990000>인증 코드가 올바르지 않습니다.</color></b>\n코드를 다시 입력해 주세요.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_invalid_code].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <b>, <color=#990000>, </color>, </b>, \n
   EN: <b><color=#990000>Incorrect verification code.</color></b>\nPlease try inputting the code again.
   PL: <b><color=#990000>Kod weryfikacji jest nieprawidłowy.</color></b>\nWprowadź kod ponownie.
456. [Wydarzenia i Przepustka [event_verification_failed_title] — tekst] 인증 실패
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_failed_title].content
   limit: do 120 znaków
   EN: Verification Failed
   PL: Weryfikacja nieudana
457. [Wydarzenia i Przepustka [event_verification_unavailable] — tekst] 현재 진행 중인 인증이 없습니다.
   źródło: EventVerificationUIText.json :: dataList[id=event_verification_unavailable].content
   limit: do 120 znaków
   EN: No verifications available.
   PL: Aktualnie nie ma weryfikacji.

## Wydarzenia i Przepustka: EventYCGDText
- plik gry: `EventYCGDText.json`

458. [Wydarzenia i Przepustka [ycgd_stagebutton_not_clear] — tekst] 5.5-12 클리어 시 개방
   źródło: EventYCGDText.json :: dataList[id=ycgd_stagebutton_not_clear].content
   limit: do 120 znaków
   EN: Clear 5.5-12 to Unlock
   PL: Odblokowanie po ukończeniu 5.5-12
459. [Wydarzenia i Przepustka [ycgd_stagebutton_normal] — tekst] 스테이지
   źródło: EventYCGDText.json :: dataList[id=ycgd_stagebutton_normal].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Wydarzenia i Przepustka [ycgd_stagebutton_end_event] — tekst] 이벤트 기간 종료
   źródło: EventYCGDText.json :: dataList[id=ycgd_stagebutton_end_event].content
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Wydarzenia i Przepustka [ycgd_storybutton_before_start] — tekst] <size=75%>이벤트 첫 번째 이야기 감상 시 개방</size>
   źródło: EventYCGDText.json :: dataList[id=ycgd_storybutton_before_start].content
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Wydarzenia i Przepustka [ycgd_storybutton_normal] — tekst] 상영관 이동
   źródło: EventYCGDText.json :: dataList[id=ycgd_storybutton_normal].content
   (powtórzenie elementu 309 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Wydarzenia i Przepustka [ycgd_rewardShopButton] — tekst] 보상 교환
   źródło: EventYCGDText.json :: dataList[id=ycgd_rewardShopButton].content
   (powtórzenie elementu 299 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Wydarzenia i Przepustka [ycgd_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: EventYCGDText.json :: dataList[id=ycgd_scrap_guide_title].content
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Wydarzenia i Przepustka [ycgd_scrap_guide_desc] — tekst] 이벤트와 주요 이야기의 스테이지와 던전 또는 거울 던전을 클리어하면 낮은 확률로 <color=#1998fe>[한 서린 검집]</color>를 획득할 수 있습니다.\n\n<color=#1998fe>[한 서린 검집]</color>은 획득 즉시, <color=#008d0d>[피에 절은 검집]</color> 20개로 전환됩니다.
   źródło: EventYCGDText.json :: dataList[id=ycgd_scrap_guide_desc].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#1998fe>, </color>, <color=#008d0d>, \n
   EN: Rarely, you may obtain <color=#1998fe>[Resentful Scabbard]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons.\n\n<color=#1998fe>[Resentful Scabbard]</color> is converted to 20 <color=#008d0d>[Bloodied Scabbard]</color>.
   PL: Ukończywszy etapy wydarzenia lub Głównej Fabuły albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#1998fe>[Przepełnioną Żalem Pochwę]</color>.\n\n<color=#1998fe>[Przepełniona Żalem Pochwa]</color> od razu zamienia się na 20 <color=#008d0d>[Zakrwawionych Pochew]</color>.
466. [Wydarzenia i Przepustka [ycgd_rewardpage_desc] — tekst] 이벤트 스테이지와 던전을 클리어할 때마다\n<color=#1998fe>[피에 절은 검집]</color>을 획득할 수 있으며, 낮은 확률로\n<color=#7fc6ff>[한 서린 검집]</color>을 추가로 획득할 수 있습니다.\n\n<color=#7fc6ff>[한 서린 검집]</color>은 획득 즉시 <color=#1998fe>[피에 절은 검집]</color> 20개로 전환됩니다.
   źródło: EventYCGDText.json :: dataList[id=ycgd_rewardpage_desc].content
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#1998fe>, </color>, <color=#7fc6ff>, \n
   EN: You can obtain <color=#1998fe>[Bloodied Scabbard]</color> from Event Stages & Dungeon.\nYou also have a small chance to obtain <color=#7fc6ff>[Resentful Scabbard]</color> in the process.\n\n<color=#7fc6ff>[Resentful Scabbard]</color> is immediately converted to 20 <color=#1998fe>[Bloodied Scabbard]</color> upon acquisition.
   PL: Ukończoną każdą etap wydarzenia i loch, zdobywasz\n<color=#1998fe>[Zakrwawione Pochwy]</color>, a z pewnym prawdopodobieństwem\ndodatkowo <color=#7fc6ff>[Przepełnioną Żalem Pochwę]</color>.\n\n<color=#7fc6ff>[Przepełniona Żalem Pochwa]</color> od razu zamienia się na 20 <color=#1998fe>[Zakrwawionych Pochew]</color>.
467. [Wydarzenia i Przepustka [ycgd_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#1998fe>[피에 절은 검집]</color>을 획득할 수 있습니다.\n\n<color=#1998fe>[보상 교환]</color> 창에서 <color=#1998fe>[피에 절은 검집]</color>을\n지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: EventYCGDText.json :: dataList[id=ycgd_reward_popup_desc].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#1998fe>, </color>, \n
   EN: Earn <color=#1998fe>[Bloodied Scabbard]</color> via the following methods:\nEvent Stage clears, Mirror Dungeon clears,\nand Main Story Stage first-time clears.\n\nIn the <color=#1998fe>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#1998fe>[Bloodied Scabbard]</color> you have collected.
   PL: Zdobywaj <color=#1998fe>[Zakrwawione Pochwy]</color> przez:\nukończenia etapów wydarzenia, pierwsze ukończenia etapów\nGłównej Fabuły oraz Lustrzane Lochy.\n\nW oknie <color=#1998fe>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#1998fe>[Zakrwawione Pochwy]</color>.
468. [Wydarzenia i Przepustka [ycgd_reward_popup_num_of_owned_items] — tekst] 보유 검집 수
   źródło: EventYCGDText.json :: dataList[id=ycgd_reward_popup_num_of_owned_items].content
   limit: do 120 znaków
   EN: Scabbards Collected
   PL: Posiadane Pochwy
469. [Wydarzenia i Przepustka [ycgd_bonusUI_Title] — tekst] 증가
   źródło: EventYCGDText.json :: dataList[id=ycgd_bonusUI_Title].content
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Wydarzenia i Przepustka [ycgd_bonusUI_Title_contain_false] — tekst] 미보유
   źródło: EventYCGDText.json :: dataList[id=ycgd_bonusUI_Title_contain_false].content
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Wydarzenia i Przepustka [ycgd_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 인격 편성 시, <color=#1998fe>[피에 절은 검집]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#1998fe>120%</color>까지 적용됩니다.
   źródło: EventYCGDText.json :: dataList[id=ycgd_bonusUI_Desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#1998fe>, </color>, \n
   EN: During the event period, deploying the following Identities on your team will\nboost the amount of <color=#1998fe>[Bloodied Scabbard]</color> earned.\nYou can earn a maximum of <color=#1998fe>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości, zwiększasz zdobywanie <color=#1998fe>[Zakrwawionych Pochew]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#1998fe>120%</color>.
472. [Wydarzenia i Przepustka [ycgd_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: EventYCGDText.json :: dataList[id=ycgd_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Wydarzenia i Przepustka [ycgd_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: EventYCGDText.json :: dataList[id=ycgd_bonus_preview].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Wydarzenia i Przepustka [ycgd_chapter_map_difficulty_ui_9107] — tekst] NORMAL
   źródło: EventYCGDText.json :: dataList[id=ycgd_chapter_map_difficulty_ui_9107].content
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Wydarzenia i Przepustka [ycgd_chapter_map_difficulty_ui_9115] — tekst] HARD
   źródło: EventYCGDText.json :: dataList[id=ycgd_chapter_map_difficulty_ui_9115].content
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Wydarzenia i Przepustka [ycgd_chapter_map_difficulty_ui_unlock_condition] — tekst] {0}-{1} 이후 어려움 난이도 개방
   źródło: EventYCGDText.json :: dataList[id=ycgd_chapter_map_difficulty_ui_unlock_condition].content
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: Fools2025
- plik gry: `Fools2025.json`

477. [Wydarzenia i Przepustka [fools_2025_entrance_popup_title] — tekst] 한봄 밤의 꿈 2
   źródło: Fools2025.json :: dataList[id=fools_2025_entrance_popup_title].content
   limit: do 120 znaków
   EN: A Midspring Night's Dream 2
   PL: Sen Środkowowiosennej Nocy 2
478. [Wydarzenia i Przepustka [fools_2025_entrance_popup_desc] — tekst] 한봄 밤의 꿈 2 스토리에 입장하시겠습니까?
   źródło: Fools2025.json :: dataList[id=fools_2025_entrance_popup_desc].content
   limit: do 120 znaków
   EN: Enter A Midspring Night's Dream 2 Story?
   PL: Wejść do fabuły „Sen Środkowowiosennej Nocy 2”?
479. [Wydarzenia i Przepustka [fools_2025_entrance_popup_desc_not_cleared_target_chapter] — tekst] 한봄 밤의 꿈 2 스토리에 입장하시겠습니까?\n\n<size=35>※ 진행 기간 : 2025.04.01 00:00 ~ 04.07 00:00 (KST) \n\n<color=#b01c37>※주의 : 해당 스토리는 7.5장 심야청소 챕터의 스포일러가 포함되어있습니다.</color></size>
   źródło: Fools2025.json :: dataList[id=fools_2025_entrance_popup_desc_not_cleared_target_chapter].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <size=35>, <color=#b01c37>, </color>, </size>, \n
   EN: Enter A Midspring Night's Dream 2 Story?\n\n<size=35>※ Event Period: 2025.04.01 00:00 ~ 04.07 00:00 (KST)\n\n\n<color=#b01c37>※ WARNING: The following story contains spoilers for Intervallo V-2 Nocturnal Sweeping.</color></size>
   PL: Wejść do fabuły „Sen Środkowowiosennej Nocy 2”?\n\n<size=35>※ Czas trwania: 2025.04.01 00:00 ~ 04.07 00:00 (KST) \n\n<color=#b01c37>※Uwaga: ta fabuła zawiera spoilery Intervallo V-2 Nocne Sprzątanie.</color></size>

## Wydarzenia i Przepustka: HellsChicken
- plik gry: `HellsChicken.json`

480. [Wydarzenia i Przepustka [hells_chicken_bonus_description] — tekst] 이벤트 기간 동안 해당 인격, E.G.O 편성 시 <color=#f8c200>[봉이 인형]의 획득량이 상승</color>합니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_bonus_description].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: During the event, having the listed Identities and E.G.O on your team <color=#f8c200>increases the amount of [Bongy Plushies] earned</color>.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości i E.G.O, <color=#f8c200>zwiększasz zdobywanie [Pluszaków Bongy]</color>.
481. [Wydarzenia i Przepustka [hells_chicken_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: HellsChicken.json :: dataList[id=hells_chicken_bonus_popup_title].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Wydarzenia i Przepustka [hells_chicken_event_panel_stage] — tekst] 스테이지 가보자고!
   źródło: HellsChicken.json :: dataList[id=hells_chicken_event_panel_stage].content
   limit: do 120 znaków
   EN: Hit up the Stages!
   PL: Ruszaj na etapy!
483. [Wydarzenia i Przepustka [hells_chicken_event_panel_story_title] — tekst] 스.다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_event_panel_story_title].content
   limit: do 120 znaków
   EN: R.S.
   PL: R.S.
484. [Wydarzenia i Przepustka [hells_chicken_event_panel_story_desc] — tekst] (스토리 다시보기)
   źródło: HellsChicken.json :: dataList[id=hells_chicken_event_panel_story_desc].content
   limit: do 120 znaków
   EN: (Rewatch Story)
   PL: (Ponowne obejrzenie fabuły)
485. [Wydarzenia i Przepustka [hells_chicken_doll_name] — tekst] 봉이 인형
   źródło: HellsChicken.json :: dataList[id=hells_chicken_doll_name].content
   limit: do 120 znaków
   EN: Bongy Plush
   PL: Pluszak Bongy
486. [Wydarzenia i Przepustka [hells_chicken_reward_exchange_counter] — tekst] 쿠폰 교환
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_exchange_counter].content
   limit: do 120 znaków
   EN: Coupon Trade-in
   PL: Wymiana Kuponów
487. [Wydarzenia i Przepustka [hells_chicken_additional_effect_desc] — tekst] 이벤트 인격 및 E.G.O 편성 시,\n[봉이 인형] 획득량 상승
   źródło: HellsChicken.json :: dataList[id=hells_chicken_additional_effect_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Event Identities and E.G.O on the team\nboost the amnt. of [Bongy Plushies] earned.
   PL: Mając w składzie Tożsamości i E.G.O wydarzenia,\nzwiększasz zdobywanie [Pluszaków Bongy]
488. [Wydarzenia i Przepustka [hells_chicken_reward_event_main_phrase] — tekst] 은봉이네 <color=#205925>호프치킨<color=#ebcaa2>이 쏩니다!
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_event_main_phrase].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#205925>, <color=#ebcaa2>
   EN: Eunbong’s <color=#205925>Bar & Fryers</color> <color=#ebcaa2>Chickapalooza!</color>
   PL: U Eunbonga <color=#205925>Bar i Smażalnia<color=#ebcaa2> ogłasza Kurczakomanię!
489. [Wydarzenia i Przepustka [hells_chicken_reward_event_phrase_0] — tekst] ※은봉이네에서 사용하는 모든 원료육은 K사 특이점이 사용되지 않았으므로 안심하고 드셔도 됩니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_event_phrase_0].content
   limit: do 130 znaków
   EN: ※ Please rest assured that all meat used at Eunbong’s is not derived from K Corp’s Singularity.
   PL: ※ Całe mięso używane u Eunbonga nie pochodzi z Osobliwości K Corp. — możesz jeść bez obaw.
490. [Wydarzenia i Przepustka [hells_chicken_reward_event_phrase_1] — tekst] 선물이 이만큼씩이나?! 싸장님이 미쳤어요!!!
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_event_phrase_1].content
   limit: do 120 znaków
   EN: All this stuff up for grabs?! The owner’s gone cuckoo!!!
   PL: Tyle nagród w zasięgu ręki?! Właścicielka oszalała!!!
491. [Wydarzenia i Przepustka [hells_chicken_reward_event_phrase_2] — tekst] 스페-샬\n치킨 쿠폰
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_event_phrase_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: SPECIAL\nCHICKEN COUPON
   PL: SPECJALNY\nKURCZAKOWY KUPON
492. [Wydarzenia i Przepustka [hells_chicken_reward_event_description] — tekst] 헬스 치킨 혹은 주요 이야기의 스테이지, 던전을 클리어하여 <color=#990000>[봉이 인형]</color>을 획득할 수 있습니다.\n\n관리자 님은 획득한 <color=#990000>[봉이 인형]</color>의 수에 비례하여 <color=#990000>[쿠폰 교환]</color>에서 다양한 보상을 얻을 수 있습니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_reward_event_description].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: Clear Hell’s Chicken Event Stages, Main Story Stages, or Dungeons to earn <color=#990000>[Bongy Plushies]</color>.\n\nYou can redeem various rewards from the <color=#990000>[Coupon Trade-in]</color> based on the number of <color=#990000>[Bongy Plushies]</color> you have.
   PL: Ukończywszy etapy i lochy Piekielnego Kurczaka lub Głównej Fabuły, zdobędziesz <color=#990000>[Pluszaki Bongy]</color>.\n\nProporcjonalnie do liczby zdobytych <color=#990000>[Pluszaków Bongy]</color> możesz odbierać różne nagrody w <color=#990000>[Wymianie Kuponów]</color>.
493. [Wydarzenia i Przepustka [hells_chicken_main_event_banner_unlock_condition] — tekst] 3-22 클리어 후 개방
   źródło: HellsChicken.json :: dataList[id=hells_chicken_main_event_banner_unlock_condition].content
   limit: do 120 znaków
   EN: Clear 3-22 to Unlock
   PL: Odblokowanie po ukończeniu 3-22
494. [Wydarzenia i Przepustka [check_rewards] — tekst] 보상 확인
   źródło: HellsChicken.json :: dataList[id=check_rewards].content
   limit: do 120 znaków
   EN: Check Rewards
   PL: Sprawdź nagrody
495. [Wydarzenia i Przepustka [earned_doll_count] — tekst] 획득한 봉이 수
   źródło: HellsChicken.json :: dataList[id=earned_doll_count].content
   limit: do 120 znaków
   EN: Bongy Plushies
   PL: Zdobyte Pluszaki Bongy
496. [Wydarzenia i Przepustka [hells_chicken_event_end_stage_text] — tekst] 이벤트는\n끝이라고.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_event_end_stage_text].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I’m off\nfor R&R.
   PL: Zbieram się\nna urlop.
497. [Wydarzenia i Przepustka [hells_chicken_dungeon_select_recent] — tekst] 프리셋
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_select_recent].content
   limit: do 120 znaków
   EN: Preset
   PL: Szablon składu
498. [Wydarzenia i Przepustka [hells_chicken_dungeon_ask_recent_personality] — tekst] 프리셋에 저장된 인격과 E.G.O 목록을 불러오시겠습니까?
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_ask_recent_personality].content
   limit: do 120 znaków
   EN: Load the saved Identities and E.G.O from the preset?
   PL: Wczytać listę Tożsamości i E.G.O zapisaną w szablonie?
499. [Wydarzenia i Przepustka [hells_chicken_dungeon_no_recent_personality] — tekst] 저장된 프리셋이 없습니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_no_recent_personality].content
   limit: do 120 znaków
   EN: No saved presets available.
   PL: Brak zapisanych szablonów.
500. [Wydarzenia i Przepustka [hells_chicken_dungeon_desc_recent_personality] — tekst] ※ 이전에 선택한 인격과 E.G.O의 목록이 프리셋에 자동으로 저장되며, 다시 입장할 경우 이를 불러올 수 있습니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_desc_recent_personality].content
   limit: do 150 znaków
   EN: ※ The list of Identities and E.G.O you used is automatically saved in the preset, which can be loaded upon reentry.
   PL: ※ Lista użytych Tożsamości i E.G.O zapisuje się automatycznie w szablonie; przy ponownym wejściu można ją wczytać.
501. [Wydarzenia i Przepustka [giving_up_hells_chicken_dungeon_title] — tekst] 이벤트 거울 던전 포기
   źródło: HellsChicken.json :: dataList[id=giving_up_hells_chicken_dungeon_title].content
   limit: do 120 znaków
   EN: Forfeit Event Dungeon
   PL: Porzucić Loch Wydarzenia
502. [Wydarzenia i Przepustka [giving_up_hells_chicken_dungeon_content] — tekst] {0}을 진행 중입니다.\n진행을 포기하고 새로운 던전에 도전하시겠습니까?
   źródło: HellsChicken.json :: dataList[id=giving_up_hells_chicken_dungeon_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: You’re currently exploring {0}.\nForfeit your progress and enter a new dungeon?
   PL: Obecnie eksplorujesz {0}.\nPorzucić postęp i spróbować nowego lochu?
503. [Wydarzenia i Przepustka [hells_chicken_dungeon_error_desc] — tekst] 서버 오류로 인하여 데이터가 손실되었습니다.\n포기 선택 시, 입장할 때 사용한 엔케팔린 모듈은 반환됩니다.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_error_desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Data was lost due to a server error.\nIf you forfeit, the Enkephalin Modules spent for entry will be refunded.
   PL: Dane utracono z powodu błędu serwera.\nPo porzuceniu Moduły Enkefalinu użyte do wejścia zostaną zwrócone.
504. [Wydarzenia i Przepustka [only_giving_up_hells_chicken_dungeon_content] — tekst] {0}을 진행 중입니다.\n진행을 포기하시겠습니까?
   źródło: HellsChicken.json :: dataList[id=only_giving_up_hells_chicken_dungeon_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: {0} is in progress.\nAre you sure you want to forfeit?
   PL: {0} w toku.\nNa pewno porzucić?
505. [Wydarzenia i Przepustka [hells_chicken_dungeon_stage_button_locked] — tekst] 3장 클리어 하고 와.
   źródło: HellsChicken.json :: dataList[id=hells_chicken_dungeon_stage_button_locked].content
   limit: do 120 znaków
   EN: Go clear Canto III first.
   PL: Najpierw ukończ Cant III.

## Wydarzenia i Przepustka: LimtochessUI
- plik gry: `LimtochessUI.json`

506. [Wydarzenia i Przepustka [limtochess_entrance_continue] — tekst] 이어하기
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_continue].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuuj
507. [Wydarzenia i Przepustka [limtochess_entrance_new_game] — tekst] 새로하기
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_new_game].content
   limit: do 120 znaków
   EN: Fresh Start
   PL: Nowa gra
508. [Wydarzenia i Przepustka [limtochess_entrance_pass] — tekst] 도상구축 패스
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_pass].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Schemacraft\nPass
   PL: Przepustka Konstrukcji Schematów
509. [Wydarzenia i Przepustka [limtochess_entrance_overwrite_title] — tekst] 새로하기
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_overwrite_title].content
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Wydarzenia i Przepustka [limtochess_entrance_overwrite_desc] — tekst] 진행 중인 도상구축을 종료하고 새로 시작하시겠습니까?\n확인 선택 시, 지금까지의 진행도에 따라 보상을 받은 다음 새롭게 시작합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_overwrite_desc].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Forfeit the Schemacraft run in progress and start a new run?\nSelecting "Confirm" will yield rewards based on your current Schemacraft progress first before the new run starts.
   PL: Porzucić trwającą Konstrukcję Schematów i rozpocząć nową?\nWybierając „Potwierdź”, najpierw otrzymasz nagrody stosownie do dotychczasowego postępu, a potem zaczniesz od nowa.
511. [Wydarzenia i Przepustka [limtochess_mode_name] — tekst] 도상구축
   źródło: LimtochessUI.json :: dataList[id=limtochess_mode_name].content
   limit: do 120 znaków
   EN: Schemacraft
   PL: Konstrukcja Schematów
512. [Wydarzenia i Przepustka [limtochess_mode_title] — tekst] 도상구축 (베타)
   źródło: LimtochessUI.json :: dataList[id=limtochess_mode_title].content
   limit: do 120 znaków
   EN: Schemacraft (Beta)
   PL: Konstrukcja Schematów (Beta)
513. [Wydarzenia i Przepustka [limtochess_entrance_enter] — tekst] 입장하기
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_enter].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
514. [Wydarzenia i Przepustka [limtochess_entrance_auto_select_bonus] — tekst] 이번 플레이 시 자동 편성 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_auto_select_bonus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reshuffle Random Team +{0} more times for this run
   PL: W tej rozgrywce szans na odnowienie losowego składu: +{0}
515. [Wydarzenia i Przepustka [limtochess_entrance_locked] — tekst] {0} 후 입장할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_locked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: May enter after {0}.
   PL: Wejście możliwe po {0}.
516. [Wydarzenia i Przepustka [limtochess_room_type_start] — tekst] 시작 방
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_start].content
   limit: do 120 znaków
   EN: Starting Room
   PL: Pokój Startowy
517. [Wydarzenia i Przepustka [limtochess_room_type_empty] — tekst] 빈 방
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_empty].content
   limit: do 120 znaków
   EN: Empty Room
   PL: Pusty Pokój
518. [Wydarzenia i Przepustka [limtochess_room_type_normal] — tekst] 일반
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_normal].content
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Wydarzenia i Przepustka [limtochess_room_type_elite] — tekst] 정예
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_elite].content
   limit: do 120 znaków
   EN: Elite
   PL: Elita
520. [Wydarzenia i Przepustka [limtochess_room_type_rest] — tekst] 휴식
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_rest].content
   limit: do 120 znaków
   EN: Respite
   PL: Wytchnienie
521. [Wydarzenia i Przepustka [limtochess_room_type_temptation] — tekst] 유혹
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_temptation].content
   limit: do 120 znaków
   EN: Temptation
   PL: Pokusa
522. [Wydarzenia i Przepustka [limtochess_room_type_event] — tekst] 이벤트
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_event].content
   limit: do 120 znaków
   EN: Event
   PL: Wydarzenie
523. [Wydarzenia i Przepustka [limtochess_room_type_segment_boss] — tekst] 보스
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_segment_boss].content
   limit: do 120 znaków
   EN: Boss
   PL: Boss
524. [Wydarzenia i Przepustka [limtochess_room_type_final_boss] — tekst] 최종 보스
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_type_final_boss].content
   limit: do 120 znaków
   EN: Final Boss
   PL: Boss Finałowy
525. [Wydarzenia i Przepustka [limtochess_roominfo_title_room] — tekst] 제 {0}도상 {1} #{2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_title_room].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Schema {0} {1} #{2}
   PL: Schemat {0} {1} #{2}
526. [Wydarzenia i Przepustka [limtochess_roominfo_bonus_none] — tekst] -
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_bonus_none].content
   limit: do 120 znaków
   EN: -
   PL: -
527. [Wydarzenia i Przepustka [limtochess_roominfo_bonus_mp_recover] — tekst] 정신력 회복 +{0} (방에 들어올 때 적용됨)
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_bonus_mp_recover].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: SP Healed +{0} (activates upon entering the room)
   PL: Odzyskanie Poczytalności +{0} (działa przy wejściu do pokoju)
528. [Wydarzenia i Przepustka [limtochess_roominfo_bonus_mp_risk] — tekst] 정신력 손실 위험 -{0} (방에 들어올 때 적용됨)
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_bonus_mp_risk].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: SP Loss ={0} (activates upon entering the room)
   PL: Ryzyko utraty Poczytalności -{0} (działa przy wejściu do pokoju)
529. [Wydarzenia i Przepustka [limtochess_roominfo_list_effect] — tekst] 효과
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_effect].content
   limit: do 120 znaków
   EN: Effects
   PL: Efekty
530. [Wydarzenia i Przepustka [limtochess_roominfo_list_penalty] — tekst] 패널티
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_penalty].content
   limit: do 120 znaków
   EN: Penalties
   PL: Kary
531. [Wydarzenia i Przepustka [limtochess_roominfo_list_event_boss] — tekst] 이번 도상구축의 끝에서 마주할 것을 그립니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_event_boss].content
   limit: do 120 znaków
   EN: Schematize what is to be encountered at the end of this Schemacraft.
   PL: Naszkicuj to, co czeka na końcu tej Konstrukcji Schematów
532. [Wydarzenia i Przepustka [limtochess_roominfo_list_event_skip] — tekst] 고르지 않고 나가면 효과와 고난을 모두 받지 않습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_event_skip].content
   limit: do 120 znaków
   EN: Leave without choosing to receive neither effects nor penalties
   PL: Wyjście bez wyboru oznacza brak efektów i brak prób
533. [Wydarzenia i Przepustka [limtochess_roominfo_list_tempt_offer] — tekst] 입장 시, 인격 또는 E.G.O를 선택하여 받을 수 있습니다. (단, 선택하지 않아도 됩니다.)
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_tempt_offer].content
   limit: do 120 znaków
   EN: Upon entry, you may select an Identity or E.G.O to receive (you may also choose neither).
   PL: Po wejściu możesz wybrać Tożsamość lub E.G.O do otrzymania (możesz też niczego nie wybierać).
534. [Wydarzenia i Przepustka [limtochess_roominfo_list_tempt_mp] — tekst] 제안에 따라 편성 인격 전원 정신력 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_tempt_mp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Depending on the offer, SP {0} for all Identities in the team
   PL: W zależności od oferty {0} Poczytalności dla wszystkich Tożsamości w składzie
535. [Wydarzenia i Przepustka [limtochess_roominfo_list_rest_pick] — tekst] 들어가면 아래 휴식 효과 중 하나를 고릅니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_rest_pick].content
   limit: do 120 znaków
   EN: Upon entry, choose one of the Respite effects below
   PL: Po wejściu wybierz jeden z poniższych efektów Wytchnienia
536. [Wydarzenia i Przepustka [limtochess_roominfo_list_rest_mp] — tekst] 정신력 회복
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_rest_mp].content
   limit: do 120 znaków
   EN: Heal SP
   PL: Odzyskiwanie Poczytalności
537. [Wydarzenia i Przepustka [limtochess_roominfo_list_rest_reroll] — tekst] 새로고침 기회
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_rest_reroll].content
   limit: do 120 znaków
   EN: Reshuffles
   PL: Szanse na odnowienie
538. [Wydarzenia i Przepustka [limtochess_roominfo_list_rest_syncup] — tekst] 편성 인격 1명 동기화 +1단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_rest_syncup].content
   limit: do 120 znaków
   EN: Uptie +1 for 1 Identity in the team
   PL: Synchronizacja +1 dla 1 Tożsamości w składzie
539. [Wydarzenia i Przepustka [limtochess_roominfo_list_rest_freeroll_carry] — tekst] 추가 굴림 (쓰지 않은 추가 굴림은 다음 도상으로 이어집니다)
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_rest_freeroll_carry].content
   limit: do 120 znaków
   EN: Bonus Rolls (unused Bonus Rolls carry over to the next Schema)
   PL: Rzuty dodatkowe (niewykorzystane Rzuty dodatkowe przechodzą do następnego Schematu)
540. [Wydarzenia i Przepustka [limtochess_roominfo_list_event_pool] — tekst] 들어가면 아래 이벤트 중 하나가 나오며, 선택지 하나를 골라 효과를 받습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_event_pool].content
   limit: do 120 znaków
   EN: Upon entry, one of the events below appears. Choose one of its options to receive its effect
   PL: Po wejściu pojawia się jedno z poniższych wydarzeń; wybierz jedną opcję, aby otrzymać jej efekt
541. [Wydarzenia i Przepustka [limtochess_roominfo_to_formation] — tekst] 편성 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_to_formation].content
   limit: do 120 znaków
   EN: Deploy Team
   PL: Ułóż skład
542. [Wydarzenia i Przepustka [limtochess_roominfo_move] — tekst] 표상 진입
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_move].content
   limit: do 120 znaków
   EN: Enter Representation
   PL: Wejdź do Reprezentacji
543. [Wydarzenia i Przepustka [limtochess_roominfo_cannot_move] — tekst] 갈 수 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_cannot_move].content
   limit: do 120 znaków
   EN: Unreachable
   PL: Nieosiągalne
544. [Wydarzenia i Przepustka [limtochess_battleprep_step_formation] — tekst] 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_step_formation].content
   limit: do 120 znaków
   EN: Team
   PL: Skład drużyny
545. [Wydarzenia i Przepustka [limtochess_battleprep_step_defense] — tekst] 방어 정책
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_step_defense].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Defense\nStrat.
   PL: Polityka obrony
546. [Wydarzenia i Przepustka [limtochess_battleprep_step_briefing] — tekst] 브리핑
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_step_briefing].content
   limit: do 120 znaków
   EN: Briefing
   PL: Odprawa
547. [Wydarzenia i Przepustka [limtochess_battleprep_back] — tekst] 뒤로
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_back].content
   limit: do 120 znaków
   EN: Back
   PL: Wstecz
548. [Wydarzenia i Przepustka [limtochess_packpreview_grade] — tekst] {0}등급
   źródło: LimtochessUI.json :: dataList[id=limtochess_packpreview_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Tier {0}
   PL: Ranga {0}
549. [Wydarzenia i Przepustka [limtochess_packpreview_label_random] — tekst] 무작위
   źródło: LimtochessUI.json :: dataList[id=limtochess_packpreview_label_random].content
   limit: do 120 znaków
   EN: Random
   PL: Losowo
550. [Wydarzenia i Przepustka [limtochess_pack_mix_identity] — tekst] 인격 {0}개 중 {1}개 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_mix_identity].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Obtain {1} of {0} Identities
   PL: Zdobądź {1} z {0} Tożsamości
551. [Wydarzenia i Przepustka [limtochess_pack_mix_ego] — tekst] E.G.O {0}개 중 {1}개 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_mix_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Obtain {1} of {0} E.G.O
   PL: Zdobądź {1} z {0} E.G.O
552. [Wydarzenia i Przepustka [limtochess_pack_keep_identity] — tekst] 인격 {0}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_keep_identity].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Identities
   PL: {0} Tożsamości
553. [Wydarzenia i Przepustka [limtochess_pack_keep_ego] — tekst] E.G.O {0}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_keep_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O: {0}
   PL: E.G.O: {0}
554. [Wydarzenia i Przepustka [limtochess_pack_keep_suffix] — tekst] 획득 가능
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_keep_suffix].content
   limit: do 120 znaków
   EN: Available
   PL: Dostępne
555. [Wydarzenia i Przepustka [limtochess_pack_mix_identity_none] — tekst] 인격 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_mix_identity_none].content
   limit: do 120 znaków
   EN: No Identities
   PL: Brak Tożsamości
556. [Wydarzenia i Przepustka [limtochess_pack_mix_ego_none] — tekst] E.G.O 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_mix_ego_none].content
   limit: do 120 znaków
   EN: No E.G.O
   PL: Brak E.G.O
557. [Wydarzenia i Przepustka [limtochess_pack_cost] — tekst] COST {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: COST {0}
   PL: COST {0}
558. [Wydarzenia i Przepustka [limtochess_packpreview_tier_line] — tekst] {0} / {1}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_packpreview_tier_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} / {1} Identities
   PL: {0} / {1}
559. [Wydarzenia i Przepustka [limtochess_personality_name] — tekst] {0} {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_personality_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} {1}
   PL: {0} {1}
560. [Wydarzenia i Przepustka [limtochess_level] — tekst] Lv {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lv {0}
   PL: Poz. {0}
561. [Wydarzenia i Przepustka [limtochess_battleprep_start] — tekst] 전투 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_start].content
   limit: do 120 znaków
   EN: To Battle!
   PL: Do Boju!
562. [Wydarzenia i Przepustka [limtochess_defense_option_placeholder] — tekst] N
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_option_placeholder].content
   limit: do 120 znaków
   EN: N
   PL: N
563. [Wydarzenia i Przepustka [limtochess_defense_option_queue] — tekst] {0}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_option_queue].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: x{0}
   PL: ×{0}
564. [Wydarzenia i Przepustka [limtochess_defense_type_guard] — tekst] 방어
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_type_guard].content
   limit: do 120 znaków
   EN: Guard
   PL: Garda
565. [Wydarzenia i Przepustka [limtochess_defense_type_evade] — tekst] 회피
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_type_evade].content
   limit: do 120 znaków
   EN: Evade
   PL: Unik
566. [Wydarzenia i Przepustka [limtochess_defense_type_counter] — tekst] 반격
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_type_counter].content
   limit: do 120 znaków
   EN: Counter
   PL: Kontra
567. [Wydarzenia i Przepustka [limtochess_defense_preset_name_0] — tekst] 쓰지 않음
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_0].content
   limit: do 120 znaków
   EN: Don't defend
   PL: Nie broni się
568. [Wydarzenia i Przepustka [limtochess_defense_preset_name_4] — tekst] 공격받을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_4].content
   limit: do 120 znaków
   EN: When under attack
   PL: Podczas ataku
569. [Wydarzenia i Przepustka [limtochess_defense_preset_name_6] — tekst] 사망 위험
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_6].content
   limit: do 120 znaków
   EN: Deadly premonition
   PL: Przy śmiertelnym ryzyku
570. [Wydarzenia i Przepustka [limtochess_defense_preset_name_7] — tekst] 강한 공격을 받을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_7].content
   limit: do 120 znaków
   EN: When under powerful attack
   PL: Gdy otrzyma potężny atak
571. [Wydarzenia i Przepustka [limtochess_defense_preset_name_11] — tekst] 대기 스킬 중 같은 속성 {0}개 이상
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_11].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}+ Reson. with Def. Skill Affinity
   PL: {0}+ Rezonansu tym samym Grzechem w kolejce
572. [Wydarzenia i Przepustka [limtochess_defense_preset_name_12] — tekst] 고유 조건
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_name_12].content
   limit: do 120 znaków
   EN: Unique conditions
   PL: Warunek własny
573. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_0] — tekst] 수비 스킬을 쓰지 않습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_0].content
   limit: do 120 znaków
   EN: Does not use Defense Skills
   PL: Nie używa Umiejętności obrony
574. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_4] — tekst] 자신에게 공격 스킬을 사용하려는 적이 있을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_4].content
   limit: do 120 znaków
   EN: When an enemy is about to use an Attack Skill on this unit
   PL: Gdy wróg zamierza użyć Umiejętności ataku na tej jednostce
575. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_6] — tekst] 사망할 정도의 피해를 받을 것 같을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_6].content
   limit: do 120 znaków
   EN: When this unit is about to take mortal damage
   PL: Gdy jednostka ma otrzymać obrażenia zagrażające życiu
576. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_7] — tekst] 자신에게 스킬 3 또는 강화 스킬 3을 사용하려는 적이 있을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_7].content
   limit: do 120 znaków
   EN: When an enemy is about to use its Skill 3 or Empowered Skill 3 on this unit
   PL: Gdy wróg zamierza użyć na tej jednostce Umiejętności 3 lub Wzmocnionej Umiejętności 3
577. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_11] — tekst] 대기 중인 스킬에 같은 속성이 {0}개 이상일 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_11].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When there are {0} or more Skills of the same Affinity in the queue
   PL: Gdy w kolejce jest co najmniej {0} Umiejętności tego samego Grzechu
578. [Wydarzenia i Przepustka [limtochess_defense_preset_desc_12] — tekst] 이 인격의 고유 조건이 충족될 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_preset_desc_12].content
   limit: do 120 znaków
   EN: When Identity-specific conditions are filled
   PL: Gdy spełniony jest warunek własny tej Tożsamości
579. [Wydarzenia i Przepustka [limtochess_defense_default] — tekst] 기본 설정
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_default].content
   limit: do 120 znaków
   EN: Default
   PL: Ogólne
580. [Wydarzenia i Przepustka [limtochess_defense_all_default] — tekst] 전원 기본값으로
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_all_default].content
   limit: do 120 znaków
   EN: Set All to Default
   PL: Ustaw wszystkim domyślne
581. [Wydarzenia i Przepustka [limtochess_defense_all_selected] — tekst] 선택한 인격 설정을 전원에 적용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_all_selected].content
   limit: do 120 znaków
   EN: Apply Selected Identity's Settings to All
   PL: Zastosuj ustawienia wybranej Tożsamości do wszystkich
582. [Wydarzenia i Przepustka [limtochess_defense_all_none] — tekst] 전원 쓰지 않음
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_all_none].content
   limit: do 120 znaków
   EN: No One Defends
   PL: Nikt się nie broni
583. [Wydarzenia i Przepustka [limtochess_briefing_average_level] — tekst] 평균 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_average_level].content
   limit: do 120 znaków
   EN: Avg. Lvl
   PL: Śr. poz.
584. [Wydarzenia i Przepustka [limtochess_briefing_enemy_status] — tekst] 적 스테이터스
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_enemy_status].content
   limit: do 120 znaków
   EN: Enemy Status
   PL: Statystyki wroga
585. [Wydarzenia i Przepustka [limtochess_briefing_speed] — tekst] 속도
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_speed].content
   limit: do 120 znaków
   EN: Speed
   PL: Szybkość
586. [Wydarzenia i Przepustka [limtochess_briefing_ally] — tekst] 아군
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_ally].content
   limit: do 120 znaków
   EN: Allies
   PL: Sojusznicy
587. [Wydarzenia i Przepustka [limtochess_briefing_enemy] — tekst] 적
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_enemy].content
   limit: do 120 znaków
   EN: Enemies
   PL: Wrogowie
588. [Wydarzenia i Przepustka [limtochess_briefing_headcount] — tekst] 인원
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_headcount].content
   limit: do 120 znaków
   EN: Unit Count
   PL: Liczba jednostek
589. [Wydarzenia i Przepustka [limtochess_briefing_threat_0] — tekst] 여유
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_0].content
   limit: do 120 znaków
   EN: Low
   PL: Niskie
590. [Wydarzenia i Przepustka [limtochess_briefing_threat_1] — tekst] 보통
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_1].content
   limit: do 120 znaków
   EN: Moderate
   PL: Średnia
591. [Wydarzenia i Przepustka [limtochess_briefing_threat_2] — tekst] 위험
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_2].content
   limit: do 120 znaków
   EN: High
   PL: Wysokie
592. [Wydarzenia i Przepustka [limtochess_briefing_threat_3] — tekst] 절망
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_3].content
   limit: do 120 znaków
   EN: Dire
   PL: Krytyczne
593. [Wydarzenia i Przepustka [limtochess_briefing_script_0] — tekst] 일반
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_script_0].content
   (powtórzenie elementu 219 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Wydarzenia i Przepustka [limtochess_briefing_script_1] — tekst] 정예
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_script_1].content
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Wydarzenia i Przepustka [limtochess_briefing_script_2] — tekst] 보스
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_script_2].content
   (powtórzenie elementu 523 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Wydarzenia i Przepustka [limtochess_briefing_wave_tag] — tekst] 웨이브 x{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_wave_tag].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Wave x{0}
   PL: Fala x{0}
597. [Wydarzenia i Przepustka [limtochess_briefing_enemy_count] — tekst] x{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_enemy_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: x{0}
   PL: x{0}
598. [Wydarzenia i Przepustka [limtochess_briefing_refill] — tekst] 전투 중 적 {0}명이 추가로 등장합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_refill].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} enemy reinforcement units will appear.
   PL: W walce pojawi się dodatkowo {0} wrogów.
599. [Wydarzenia i Przepustka [limtochess_briefing_no_refill] — tekst] 추가로 등장하는 적이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_no_refill].content
   limit: do 120 znaków
   EN: No additional enemies will appear.
   PL: Dodatkowi wrogowie nie pojawią się.
600. [Wydarzenia i Przepustka [limtochess_briefing_speed_faster] — tekst] 아군이 대체로 먼저 움직입니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_speed_faster].content
   limit: do 120 znaków
   EN: Allies generally act first.
   PL: Sojusznicy zwykle działają pierwsi.
601. [Wydarzenia i Przepustka [limtochess_briefing_speed_slower] — tekst] 적이 대체로 먼저 움직입니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_speed_slower].content
   limit: do 120 znaków
   EN: Enemies generally act first.
   PL: Wrogowie zwykle działają pierwsi.
602. [Wydarzenia i Przepustka [limtochess_briefing_speed_similar] — tekst] 아군과 적의 속도가 비슷합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_speed_similar].content
   limit: do 120 znaków
   EN: Allies and enemies have similar Speed.
   PL: Sojusznicy i wrogowie mają podobną Szybkość.
603. [Wydarzenia i Przepustka [limtochess_briefing_multi_action_tag] — tekst] 연속 행동 x{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_multi_action_tag].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Consecutive Actions x{0}
   PL: Akcje pod rząd x{0}
604. [Wydarzenia i Przepustka [limtochess_briefing_multi_action_grow_tag] — tekst] 연속 행동 x{0}→x{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_multi_action_grow_tag].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Consecutive Actions x{0}→x{1}
   PL: Akcje pod rząd x{0}→x{1}
605. [Wydarzenia i Przepustka [limtochess_packselect_my_deck] — tekst] 편성 확인
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_my_deck].content
   limit: do 120 znaków
   EN: View Team
   PL: Zobacz skład
606. [Wydarzenia i Przepustka [limtochess_packselect_deck_tag] — tekst] {0} {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_deck_tag].content
   (powtórzenie elementu 559 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Wydarzenia i Przepustka [limtochess_packselect_reroll] — tekst] 새로고침 기회
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_reroll].content
   (powtórzenie elementu 537 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Wydarzenia i Przepustka [limtochess_packselect_deck_count] — tekst] 전투 편성에 {0}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_deck_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} in Team
   PL: {0} w składzie bojowym
609. [Wydarzenia i Przepustka [limtochess_packselect_swap] — tekst] 팩 새로고침
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_swap].content
   limit: do 120 znaków
   EN: Reshuffle Pack
   PL: Odśwież Pakiet
610. [Wydarzenia i Przepustka [limtochess_packselect_swap_cost] — tekst] 팩 교체 · 기회 소모량 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_swap_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reroll Pack · Uses {0} Rerolls
   PL: Wymiana Pakietu · zużywa {0} odnowień
611. [Wydarzenia i Przepustka [limtochess_packselect_swap_done] — tekst] 새로고침 완료
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_swap_done].content
   limit: do 120 znaków
   EN: Reshuffled
   PL: Odświeżono
612. [Wydarzenia i Przepustka [limtochess_packselect_card_reroll] — tekst] 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_card_reroll].content
   limit: do 120 znaków
   EN: Replace
   PL: Wymiana
613. [Wydarzenia i Przepustka [limtochess_packselect_rest_title] — tekst] 이 방의 팩 목록
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_rest_title].content
   limit: do 120 znaków
   EN: Packs in This Room
   PL: Pakiety w tym pokoju
614. [Wydarzenia i Przepustka [limtochess_packselect_rest_desc] — tekst] 팩 교체 시 아래 팩 중 하나로 바뀝니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_rest_desc].content
   limit: do 120 znaków
   EN: Reshuffle to replace the current pack with one of the packs below
   PL: Po wymianie pakiet zamieni się na jeden z poniższych
615. [Wydarzenia i Przepustka [limtochess_packselect_open_pack] — tekst] 팩 열기
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_open_pack].content
   limit: do 120 znaków
   EN: Open Pack
   PL: Otwórz Pakiet
616. [Wydarzenia i Przepustka [limtochess_packselect_open_pack_mix] — tekst] 팩 열기 · 인격 {0} · E.G.O {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_open_pack_mix].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Open Pack · {0} Identities · {1} E.G.O
   PL: Otwórz Pakiet · Tożsamości {0} · E.G.O {1}
617. [Wydarzenia i Przepustka [limtochess_packselect_open_pack_step] — tekst] {0} ({1}/{2})
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_open_pack_step].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} ({1}/{2})
   PL: {0} ({1}/{2})
618. [Wydarzenia i Przepustka [limtochess_packselect_odds_cost] — tekst] 인격 코스트
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_cost].content
   limit: do 120 znaków
   EN: Identity Cost
   PL: Koszt Tożsamości
619. [Wydarzenia i Przepustka [limtochess_packselect_odds_ego] — tekst] E.G.O 등급
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_ego].content
   limit: do 120 znaków
   EN: E.G.O Tier
   PL: Ranga E.G.O
620. [Wydarzenia i Przepustka [limtochess_packselect_odds_sync] — tekst] 카드 동기화
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_sync].content
   limit: do 120 znaków
   EN: Uptie Card
   PL: Synchronizuj Kartę
621. [Wydarzenia i Przepustka [limtochess_packselect_odds_item_cost] — tekst] COST {0} {1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_item_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: COST {0} {1}%
   PL: COST {0} {1}%
622. [Wydarzenia i Przepustka [limtochess_packselect_odds_item_sync] — tekst] 동기화 {0}단계 {1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_item_sync].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} {1}%
   PL: Synchronizacja {0} {1}%
623. [Wydarzenia i Przepustka [limtochess_packselect_odds_item] — tekst] {0} {1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_odds_item].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} {1}%
   PL: {0} {1}%
624. [Wydarzenia i Przepustka [limtochess_packselect_pack_title] — tekst] [ {0} ] 팩
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_pack_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [ {0} ] Pack
   PL: [ {0} ] Pakiet
625. [Wydarzenia i Przepustka [limtochess_packselect_confirm] — tekst] 확정
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_confirm].content
   limit: do 120 znaków
   EN: Confirm
   PL: Gwarantowane
626. [Wydarzenia i Przepustka [limtochess_packselect_confirm_count] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_confirm_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}/{1}%
   PL: {0}/{1}
627. [Wydarzenia i Przepustka [limtochess_packselect_confirm_preview] — tekst] 선택 항목
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_confirm_preview].content
   limit: do 120 znaków
   EN: Selected:
   PL: Wybrane:
628. [Wydarzenia i Przepustka [limtochess_packselect_toggle_recruit] — tekst] 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_recruit].content
   (powtórzenie elementu 544 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Wydarzenia i Przepustka [limtochess_packselect_toggle_replace] — tekst] 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_replace].content
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Wydarzenia i Przepustka [limtochess_packselect_toggle_fragment] — tekst] 조각
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_fragment].content
   limit: do 120 znaków
   EN: Sliver
   PL: Okruch
631. [Wydarzenia i Przepustka [limtochess_packselect_toggle_syncup] — tekst] 동기화
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_syncup].content
   limit: do 120 znaków
   EN: Uptie
   PL: Synchronizacja
632. [Wydarzenia i Przepustka [limtochess_packselect_desc_recruit] — tekst] 편성에 추가됩니다.\n동기화 {0}단계로 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_desc_recruit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Add to the team.\nStarts at Uptie {0}.
   PL: Dodaje do składu.\nZaczyna na Synchronizacji {0}.
633. [Wydarzenia i Przepustka [limtochess_packselect_desc_replace] — tekst] 선택 시 현재 인격\n[{0}](과/와) 교체됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_desc_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Replaces the current Identity, [{0}].
   PL: Po wybraniu zastąpi obecną Tożsamość,\n[{0}].
634. [Wydarzenia i Przepustka [limtochess_packselect_desc_ego_equip] — tekst] 선택 시 빈 {0} 칸에 장착합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_desc_ego_equip].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Equip in the empty {0} slot.
   PL: Po wybraniu zostanie wyposażony w puste gniazdo {0}.
635. [Wydarzenia i Przepustka [limtochess_packselect_ego_tier] — tekst] 환상 해석 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_ego_tier].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Threadspin Tier {0}
   PL: Stopień Splotu Nici {0}
636. [Wydarzenia i Przepustka [limtochess_packselect_sync_change] — tekst] 동기화 {0}단계 → 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_sync_change].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} → Uptie {1}
   PL: Synchronizacja {0} → Synchronizacja {1}
637. [Wydarzenia i Przepustka [limtochess_packselect_summary_recruit] — tekst] {0} 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_recruit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Recruit {0}
   PL: {0} do składu
638. [Wydarzenia i Przepustka [limtochess_packselect_summary_replace] — tekst] {0} 인격 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace {0} Identity
   PL: Zamień Tożsamość {0}
639. [Wydarzenia i Przepustka [limtochess_packselect_summary_syncup] — tekst] {0} 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_syncup].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Uptie {1}
   PL: {0} Synchronizacja {1}
640. [Wydarzenia i Przepustka [limtochess_packselect_summary_fragment] — tekst] {0} 조각 획득 (동기화에 필요한 조각 {2}개 중 {1}개)
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_fragment].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {2}, {1}
   EN: {0}'s Slivers obtained ({1} out of {2} Slivers required for Uptying)
   PL: Okruchy {0} zdobyte ({1} z {2} Okruchów wymaganych do Synchronizacji)
641. [Wydarzenia i Przepustka [limtochess_packselect_summary_fragment_keep] — tekst] {0} 조각 보관 {1}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_fragment_keep].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Obtain {1} {0} Sliver(s)
   PL: Zdobądź {1} Okruch(y) {0}
642. [Wydarzenia i Przepustka [limtochess_packselect_summary_fragment_generic] — tekst] {0} 범용 조각 +{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_fragment_generic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Universal Sliver +{1} obtained by {0}
   PL: Okruch Uniwersalny +{1} dzięki {0}
643. [Wydarzenia i Przepustka [limtochess_packselect_summary_none] — tekst] 선택한 인격 · E.G.O가 없습니다.\n※ 인격 동기화 필요 조각 (동기화 1/2/3단계) : 2/3/3개
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_none].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: No Identity / E.G.O Selected.\n※ Need 2/3/3 Slivers for ID Uptie 1/2/3, respectively
   PL: Nie wybrano Tożsamości ani E.G.O.\n※ Okruchy wymagane do Synchronizacji Tożsamości (Sinc. 1/2/3): 2/3/3
644. [Wydarzenia i Przepustka [limtochess_packselect_summary_ego_equip] — tekst] {0} E.G.O 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_ego_equip].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Equip {0} E.G.O
   PL: Wyposaż {0} E.G.O
