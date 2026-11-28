# Paczka AI P09 (Fala 1 · 1C) — Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI) (część 5/6)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P09_1c_tryby_etapy_lochy_teatr_cz05.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P09_1c_tryby_etapy_lochy_teatr_cz05.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_2
- plik gry: `MirrorDungeonUI_2.json`

1. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_require_condition_ego_gacksung] — tekst] - E.G.O 환상 해석 3 단계
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_hard_require_condition_ego_gacksung].content
   limit: do 120 znaków
   EN: - E.G.O Threadspin Tier 3
   PL: - Splot Nici E.G.O poz. 3
2. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_require_condition_personality_gacksung] — tekst] - 인격 동기화 3 단계
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_hard_require_condition_personality_gacksung].content
   limit: do 120 znaków
   EN: - Identity Uptie Tier 3
   PL: - Synchronizacja Tożsamości poz. 3
3. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_require_condition_start_buf] — tekst] - 시작 버프 전체 활성화
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_hard_require_condition_start_buf].content
   limit: do 120 znaków
   EN: - All Starter Buffs Active
   PL: - Wszystkie wzmocnienia początkowe aktywne
4. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_using_hard_using_chance_desc] — tekst] 남은 <color=#a16a3b>주간 추가 보상</color>과 <color=#ff0000>어려움 난이도 보상</color>을 전부 소모하여 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_using_hard_using_chance_desc].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, <color=#ff0000>
   EN: Consume all of your remaining <color=#a16a3b>Weekly Bonuses</color> and <color=#ff0000>Hard Difficulty Reward count</color> to claim the rewards?
   PL: Zużyć wszystkie pozostałe <color=#a16a3b>Cotygodniowe Premie</color> oraz <color=#ff0000>Nagrody poz. Trudnego</color>, by odebrać nagrody?
5. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_using_hard_not_using_chance_desc] — tekst] 사용 가능한 <color=#a16a3b>주간 추가 보상</color>이 있습니다.\n\n<color=#ff0000>어려움 난이도 보상</color>만 소모하여 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_using_hard_not_using_chance_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, <color=#ff0000>, \n
   EN: You have remaining <color=#a16a3b>Weekly Bonuses</color>.\n\nConsume only the <color=#ff0000>Hard Difficulty Reward counts</color> to unlock the rewards?
   PL: Masz dostępne <color=#a16a3b>Cotygodniowe Premie</color>.\n\nZużyć wyłącznie <color=#ff0000>Nagrody poz. Trudnego</color>, by odebrać nagrody?
6. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_using_hard_no_chance_desc] — tekst] <color=#ff0000>어려움 난이도 보상</color>을 소모하여 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_using_hard_no_chance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: Spend <color=#ff0000>Hard Difficulty Rewards count</color> to unlock the rewards?
   PL: Zużyć <color=#ff0000>Nagrody poz. Trudnego</color>, aby odebrać nagrody?
7. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_not_using_hard_chance_using_chance_desc] — tekst] 사용 가능한 <color=#ff0000>어려움 난이도 보상</color>이 있습니다.\n\n<color=#a16a3b>주간 추가 보상</color>만 소모하여 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_not_using_hard_chance_using_chance_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, <color=#a16a3b>, \n
   EN: You have remaining <color=#ff0000>Hard Difficulty Reward counts</color>.\n\nConsume only the <color=#a16a3b>Weekly Bonuses</color> to unlock the rewards?
   PL: Masz dostępne <color=#ff0000>Nagrody poz. Trudnego</color>.\n\nZużyć wyłącznie <color=#a16a3b>Cotygodniową Premię</color>, by odebrać nagrody?
8. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_not_using_hard_chance_not_using_chance_desc] — tekst] 사용 가능한 <color=#a16a3b>주간 추가 보상</color>과 <color=#ff0000>어려움 난이도 보상</color>이 있습니다.\n\n이를 소모하지 않고 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_not_using_hard_chance_not_using_chance_desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, <color=#ff0000>, \n
   EN: You have remaining <color=#a16a3b>Weekly Bonuses</color> and <color=#ff0000>Hard Difficulty Reward counts</color>.\n\nUnlock the rewards without spending them?
   PL: Masz dostępne <color=#a16a3b>Cotygodniowe Premie</color> oraz <color=#ff0000>Nagrody poz. Trudnego</color>.\n\nOdebrać nagrody bez ich zużywania?
9. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_not_using_hard_chance_no_chance_desc] — tekst] 사용 가능한 <color=#ff0000>어려움 난이도 보상</color>이 있습니다.\n\n이를 소모하지 않고 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_not_using_hard_chance_no_chance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: You have remaining <color=#ff0000>Hard Difficulty Reward counts</color>.\n\nUnlock the rewards without spending them?
   PL: Masz dostępne <color=#ff0000>Nagrody poz. Trudnego</color>.\n\nOdebrać nagrody bez ich zużywania?
10. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_no_hard_chance_using_chance_desc] — tekst] <color=#a16a3b>주간 추가 보상</color>을 소모하여 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_no_hard_chance_using_chance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>
   EN: Spend <color=#a16a3b>Weekly Bonuses</color> to unlock the rewards?
   PL: Zużyć <color=#a16a3b>Cotygodniową Premię</color>, aby odebrać nagrody?
11. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_no_hard_chance_not_using_chance_desc] — tekst] 사용 가능한 <color=#a16a3b>주간 추가 보상</color>이 있습니다.\n\n이를 소모하지 않고 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_no_hard_chance_not_using_chance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, \n
   EN: You have remaining <color=#a16a3b>Weekly Bonuses</color>.\n\nUnlock the rewards without spending them?
   PL: Masz dostępne <color=#a16a3b>Cotygodniowe Premie</color>.\n\nOdebrać nagrody bez ich zużywania?
12. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_no_hard_chance_no_chance_desc] — tekst] 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_no_hard_chance_no_chance_desc].content
   limit: do 120 znaków
   EN: Claim the rewards?
   PL: Odebrać nagrody?
13. [Tryby lochów i Kolei Refrakcji [mirrordungeon_hard_no_reward_desc] — tekst] <color=#ff0000>해당 콘텐츠 보상을 이미 획득하여, 보상을 획득할 수 없습니다.</color>
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_hard_no_reward_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>The rewards for this content has already been claimed.</color>
   PL: <color=#ff0000>Nagrody za tę zawartość zostały już odebrane.</color>
14. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_1] — tekst] 여정의 시작
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_1].content
   limit: do 120 znaków
   EN: A Journey's Start
   PL: Początek Podróży
15. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_2] — tekst] 기회 잡기
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_2].content
   limit: do 120 znaków
   EN: Seize the Opportunity
   PL: Chwytanie Okazji
16. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_3] — tekst] 유비무환
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_3].content
   limit: do 120 znaków
   EN: Just in Case
   PL: Przezorny Zawsze Ubezpieczony
17. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_4] — tekst] 노력의 산물
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_4].content
   limit: do 120 znaków
   EN: Fruits of Labor
   PL: Owoce Pracy
18. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_5] — tekst] 값진 결실
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_5].content
   limit: do 120 znaków
   EN: Worthy Prize
   PL: Cenny Plon
19. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_6] — tekst] 새로운 발견
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_6].content
   limit: do 120 znaków
   EN: New Discovery
   PL: Nowe Odkrycie
20. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_7] — tekst] 전리품
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_7].content
   limit: do 120 znaków
   EN: The Spoils of War
   PL: Łupy Wojenne
21. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_8] — tekst] 다다익선
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_8].content
   limit: do 120 znaków
   EN: More the Better
   PL: Im Więcej, Tym Lepiej
22. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_9] — tekst] 다져진 신뢰
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_9].content
   limit: do 120 znaków
   EN: Established Trust
   PL: Ugruntowane Zaufanie
23. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_10] — tekst] 절차탁마
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_10].content
   limit: do 120 znaków
   EN: Perseverance
   PL: Nieustanny Szlif
24. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_11] — tekst] 이름값
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_11].content
   limit: do 120 znaków
   EN: Namesake
   PL: Waga Imienia
25. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_12] — tekst] 명성과 위업
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_12].content
   limit: do 120 znaków
   EN: Fame and Feats
   PL: Sława i Czyny
26. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_13] — tekst] 권리
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_13].content
   limit: do 120 znaków
   EN: Rights
   PL: Prawa
27. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_14] — tekst] 금의환향
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_14].content
   limit: do 120 znaków
   EN: Triumphant Return
   PL: Triumfalny Powrót
28. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_15] — tekst] 목표
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_15].content
   limit: do 120 znaków
   EN: Goals
   PL: Cel
29. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_16] — tekst] 준비성
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_16].content
   limit: do 120 znaków
   EN: Readiness
   PL: Gotowość
30. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_17] — tekst] 나아갈 투지
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_17].content
   limit: do 120 znaków
   EN: Spirit to Push Ahead
   PL: Wola Parcia Naprzód
31. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_buffs_title_18] — tekst] 체력 단련
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_3_buffs_title_18].content
   limit: do 120 znaków
   EN: Physical Training
   PL: Trening Wytrzymałościowy
32. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_101] — tekst] 3등급 기프트 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_101].content
   limit: do 120 znaków
   EN: Tier 3 Gift Appearance
   PL: Pojawianie się Darów rangi 3
33. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1011] — tekst] 화상 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1011].content
   limit: do 120 znaków
   EN: Higher Tier Burn Gifts appear
   PL: Wyższa ranga pojawiających się Darów Podpalenia
34. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1012] — tekst] 출혈 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1012].content
   limit: do 120 znaków
   EN: Higher Tier Bleed Gifts appear
   PL: Wyższa ranga pojawiających się Darów Krwawienia
35. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1013] — tekst] 진동 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1013].content
   limit: do 120 znaków
   EN: Higher Tier Tremor Gifts appear
   PL: Wyższa ranga pojawiających się Darów Wstrząsu
36. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1014] — tekst] 파열 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1014].content
   limit: do 120 znaków
   EN: Higher Tier Rupture Gifts appear
   PL: Wyższa ranga pojawiających się Darów Rozdarcia
37. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1015] — tekst] 침잠 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1015].content
   limit: do 120 znaków
   EN: Higher Tier Sinking Gifts appear
   PL: Wyższa ranga pojawiających się Darów Zatonięcia
38. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1016] — tekst] 호흡 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1016].content
   limit: do 120 znaków
   EN: Higher Tier Poise Gifts appear
   PL: Wyższa ranga pojawiających się Darów Oddechu
39. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1017] — tekst] 충전 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1017].content
   limit: do 120 znaków
   EN: Higher Tier Charge Gifts appear
   PL: Wyższa ranga pojawiających się Darów Ładunku
40. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1018] — tekst] 무작위 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1018].content
   limit: do 120 znaków
   EN: Higher Tier Random Gifts appear
   PL: Wyższa ranga pojawiających się Darów losowych
41. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_102] — tekst] 4등급 이상 기프트 등장 및 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_102].content
   limit: do 120 znaków
   EN: Tier 4+ Gifts appear & Higher Tier Gifts appear
   PL: Pojawianie się Darów rangi 4+ oraz wzrost rangi Darów
42. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1021] — tekst] 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1021].content
   limit: do 120 znaków
   EN: Higher Tier Gifts appear
   PL: Wyższa ranga pojawiających się Darów
43. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1022] — tekst] 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1022].content
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1023] — tekst] 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1023].content
   (powtórzenie elementu 42 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_103] — tekst] 등장하는 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_103].content
   limit: do 120 znaków
   EN: Selectable E.G.O Gift +1
   PL: Liczba pojawiających się Darów +1
46. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1031] — tekst] 등장하는 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1031].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_104] — tekst] 등장하는 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_104].content
   (powtórzenie elementu 45 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
48. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1041] — tekst] 등장하는 화상 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1041].content
   limit: do 120 znaków
   EN: Selectable Burn E.G.O Gift +1
   PL: Liczba pojawiających się Darów Podpalenia +1
49. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1042] — tekst] 등장하는 출혈 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1042].content
   limit: do 120 znaków
   EN: Selectable Bleed E.G.O Gift +1
   PL: Liczba pojawiających się Darów Krwawienia +1
50. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1043] — tekst] 등장하는 진동 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1043].content
   limit: do 120 znaków
   EN: Selectable Tremor E.G.O Gift +1
   PL: Liczba pojawiających się Darów Wstrząsu +1
51. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1044] — tekst] 등장하는 파열 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1044].content
   limit: do 120 znaków
   EN: Selectable Rupture E.G.O Gift +1
   PL: Liczba pojawiających się Darów Rozdarcia +1
52. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1045] — tekst] 등장하는 침잠 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1045].content
   limit: do 120 znaków
   EN: Selectable Sinking E.G.O Gift +1
   PL: Liczba pojawiających się Darów Zatonięcia +1
53. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1046] — tekst] 등장하는 호흡 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1046].content
   limit: do 120 znaków
   EN: Selectable Poise E.G.O Gift +1
   PL: Liczba pojawiających się Darów Oddechu +1
54. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1047] — tekst] 등장하는 충전 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1047].content
   limit: do 120 znaków
   EN: Selectable Charge E.G.O Gift +1
   PL: Liczba pojawiających się Darów Ładunku +1
55. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1048] — tekst] 등장하는 무작위 기프트 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1048].content
   limit: do 120 znaków
   EN: Selectable Random E.G.O Gift +1
   PL: Liczba pojawiających się Darów losowych +1
56. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_105] — tekst] 시작 코스트 50 획득
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_105].content
   limit: do 120 znaków
   EN: Gain +50 Starting Cost
   PL: Zyskaj 50 początkowego Kosztu
57. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1051] — tekst] 시작 코스트 +50
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1051].content
   limit: do 120 znaków
   EN: Starting Cost +50
   PL: Początkowy Koszt +50
58. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1052] — tekst] 시작 코스트 +50
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1052].content
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1053] — tekst] 시작 코스트 +50
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1053].content
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
60. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_106] — tekst] 기프트 3종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_106].content
   limit: do 120 znaków
   EN: Introduce 3 new Gifts
   PL: Odblokowanie 3 nowych Darów
61. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1061] — tekst] 화상 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1061].content
   limit: do 120 znaków
   EN: Introduce 2 new Burn Gifts
   PL: Odblokowanie 2 nowych Darów Podpalenia
62. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1062] — tekst] 출혈 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1062].content
   limit: do 120 znaków
   EN: Introduce 2 new Bleed Gifts
   PL: Odblokowanie 2 nowych Darów Krwawienia
63. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1063] — tekst] 진동 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1063].content
   limit: do 120 znaków
   EN: Introduce 2 new Tremor Gifts
   PL: Odblokowanie 2 nowych Darów Wstrząsu
64. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1064] — tekst] 파열 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1064].content
   limit: do 120 znaków
   EN: Introduce 2 new Rupture Gifts
   PL: Odblokowanie 2 nowych Darów Rozdarcia
65. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1065] — tekst] 침잠 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1065].content
   limit: do 120 znaków
   EN: Introduce 2 new Sinking Gifts
   PL: Odblokowanie 2 nowych Darów Zatonięcia
66. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1066] — tekst] 호흡 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1066].content
   limit: do 120 znaków
   EN: Introduce 2 new Poise Gifts
   PL: Odblokowanie 2 nowych Darów Oddechu
67. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1067] — tekst] 충전 기프트 2종 추가 등장
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1067].content
   limit: do 120 znaków
   EN: Introduce 2 new Charge Gifts
   PL: Odblokowanie 2 nowych Darów Ładunku
68. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_107] — tekst] 전투에서 획득하는 코스트 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_107].content
   limit: do 120 znaków
   EN: Gain more Cost from Combat Encounters
   PL: Więcej Kosztu zdobywanego w walkach
69. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1071] — tekst] 일반 전투에서 획득하는 코스트 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1071].content
   limit: do 120 znaków
   EN: Gain more Cost from Regular Encounters
   PL: Więcej Kosztu zdobywanego w zwykłych starciach
70. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1072] — tekst] 집중 전투에서 획득하는 코스트 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1072].content
   limit: do 120 znaków
   EN: Gain more Cost from Focused Encounters
   PL: Więcej Kosztu zdobywanego w starciach skupionych
71. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1073] — tekst] 위험 전투에서 획득하는 코스트 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1073].content
   limit: do 120 znaków
   EN: Gain more Cost from Risky Encounters
   PL: Więcej Kosztu zdobywanego w starciach ryzykownych
72. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1074] — tekst] 층 보스 전투에서 획득하는 코스트 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1074].content
   limit: do 120 znaków
   EN: Gain more Cost from Floor Boss Encounters
   PL: Więcej Kosztu zdobywanego w walkach z bossami pięter
73. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_108] — tekst] 기프트 선택 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_108].content
   limit: do 120 znaków
   EN: Gift Choice +1
   PL: Liczba wybieranych Darów +1
74. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_109] — tekst] 새로고침 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_109].content
   limit: do 120 znaków
   EN: Cheaper Refresh Cost
   PL: Niższy koszt odświeżenia
75. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1091] — tekst] 새로고침 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1091].content
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1092] — tekst] 낮은 확률로 새로 고침 비용 소모 없음
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1092].content
   limit: do 120 znaków
   EN: Small chance for a free Refresh
   PL: Niewielka szansa na darmowe odświeżenie
77. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1093] — tekst] 스킬 교체 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1093].content
   limit: do 120 znaków
   EN: [Shops] Cheaper Skill Replacement Cost
   PL: Niższy koszt wymiany umiejętności
78. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1094] — tekst] 스킬 교체 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1094].content
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_110] — tekst] 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_110].content
   limit: do 120 znaków
   EN: Cheaper Enhancement Cost
   PL: Niższy koszt ulepszenia
80. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1101] — tekst] 낮은 확률로 강화 비용 소모 없음
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1101].content
   limit: do 120 znaków
   EN: Small chance for a free Enhance
   PL: Niewielka szansa na darmowe ulepszenie
81. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1102] — tekst] 화상 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1102].content
   limit: do 120 znaków
   EN: Cheaper Burn Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Podpalenia
82. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1103] — tekst] 출혈 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1103].content
   limit: do 120 znaków
   EN: Cheaper Bleed Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Krwawienia
83. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1104] — tekst] 진동 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1104].content
   limit: do 120 znaków
   EN: Cheaper Tremor Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Wstrząsu
84. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1105] — tekst] 파열 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1105].content
   limit: do 120 znaków
   EN: Cheaper Rupture Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Rozdarcia
85. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1106] — tekst] 침잠 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1106].content
   limit: do 120 znaków
   EN: Cheaper Sinking Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Zatonięcia
86. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1107] — tekst] 호흡 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1107].content
   limit: do 120 znaków
   EN: Cheaper Poise Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Oddechu
87. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1108] — tekst] 충전 기프트 강화 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1108].content
   limit: do 120 znaków
   EN: Cheaper Charge Gift Enhancement Cost
   PL: Niższy koszt ulepszenia Darów Ładunku
88. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_111] — tekst] 기프트 판매 비용 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_111].content
   limit: do 120 znaków
   EN: Gain more Cost from selling Gifts
   PL: Wyższa cena sprzedaży Darów
89. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1111] — tekst] 기프트 판매 비용 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1111].content
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_112] — tekst] 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_112].content
   limit: do 120 znaków
   EN: Cheaper Gift Purchase Cost
   PL: Niższy koszt zakupu Darów
91. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1121] — tekst] 화상 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1121].content
   limit: do 120 znaków
   EN: Cheaper Burn Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Podpalenia
92. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1122] — tekst] 출혈 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1122].content
   limit: do 120 znaków
   EN: Cheaper Bleed Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Krwawienia
93. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1123] — tekst] 진동 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1123].content
   limit: do 120 znaków
   EN: Cheaper Tremor Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Wstrząsu
94. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1124] — tekst] 파열 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1124].content
   limit: do 120 znaków
   EN: Cheaper Rupture Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Rozdarcia
95. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1125] — tekst] 침잠 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1125].content
   limit: do 120 znaków
   EN: Cheaper Sinking Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Zatonięcia
96. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1126] — tekst] 호흡 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1126].content
   limit: do 120 znaków
   EN: Cheaper Poise Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Oddechu
97. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1127] — tekst] 충전 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1127].content
   limit: do 120 znaków
   EN: Cheaper Charge Gift Purchase Cost
   PL: Niższy koszt zakupu Darów Ładunku
98. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1128] — tekst] 범용 기프트 구매 비용 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1128].content
   limit: do 120 znaków
   EN: Cheaper Keywordless Gift Purchase Cost
   PL: Niższy koszt zakupu Darów uniwersalnych
99. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_151] — tekst] E.G.O 기프트 선택 수 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_151].content
   limit: do 120 znaków
   EN: E.G.O Gift Selection +1
   PL: Liczba wybieranych Darów E.G.O +1
100. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_152] — tekst] 시작 코스트 + 250
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_152].content
   limit: do 120 znaków
   EN: Starting Cost +250
   PL: Początkowy Koszt +250
101. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_153] — tekst] 시작 단계에서 선택한 항목의 4등급 무작위 E.G.O 기프트를 추가로 획득
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_153].content
   limit: do 120 znaków
   EN: After selecting a Starting E.G.O Gift, receive a random Tier 4 E.G.O Gift
   PL: Po wyborze początkowego Daru E.G.O otrzymujesz dodatkowo losowy Dar E.G.O rangi 4 wybranej kategorii
102. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_121] — tekst] 모든 속성 E.G.O 자원 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_121].content
   limit: do 120 znaków
   EN: +1 E.G.O resource for all Affinities
   PL: Zasoby E.G.O wszystkich Grzechów +1
103. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1211] — tekst] 모든 속성 E.G.O 자원 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1211].content
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1212] — tekst] 속도 최댓값 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1212].content
   limit: do 120 znaków
   EN: Max Speed +1
   PL: Maks. Szybkość +1
105. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1213] — tekst] 속도 최댓값 +1
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1213].content
   (powtórzenie elementu 104 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_122] — tekst] 가하는 피해량 3% 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_122].content
   limit: do 120 znaków
   EN: Deal +3% damage
   PL: Zadawane obrażenia +3%
107. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1221] — tekst] 가하는 피해량 3% 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1221].content
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1222] — tekst] 공격 레벨 1 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1222].content
   limit: do 120 znaków
   EN: Offense Level +1
   PL: Poziom Ataku +1
109. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1223] — tekst] 공격 레벨 1 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1223].content
   (powtórzenie elementu 108 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1224] — tekst] 가하는 참격 피해량 4% 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1224].content
   limit: do 120 znaków
   EN: Deal +4% Slash Damage
   PL: Zadawane obrażenia Cięte +4%
111. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1225] — tekst] 가하는 관통 피해량 4% 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1225].content
   limit: do 120 znaków
   EN: Deal +4% Pierce Damage
   PL: Zadawane obrażenia Kłute +4%
112. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1226] — tekst] 가하는 타격 피해량 4% 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1226].content
   limit: do 120 znaków
   EN: Deal +4% Blunt Damage
   PL: Zadawane obrażenia Obuchowe +4%
113. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_123] — tekst] 받는 피해량 3% 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_123].content
   limit: do 120 znaków
   EN: Take -3% damage
   PL: Otrzymywane obrażenia -3%
114. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1231] — tekst] 받는 피해량 3% 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1231].content
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1232] — tekst] 방어 레벨 1 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1232].content
   limit: do 120 znaków
   EN: Defense Level +1
   PL: Poziom Obrony +1
116. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1233] — tekst] 방어 레벨 2 증가
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1233].content
   limit: do 120 znaków
   EN: Defense Level +2
   PL: Poziom Obrony +2
117. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1234] — tekst] 참격 내성 0.1만큼 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1234].content
   limit: do 120 znaków
   EN: Slash Resistance -0.1
   PL: Odporność na Cięcie -0,1
118. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1235] — tekst] 관통 내성 0.1만큼 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1235].content
   limit: do 120 znaków
   EN: Pierce Resistance -0.1
   PL: Odporność na Kłucie -0,1
119. [Tryby lochów i Kolei Refrakcji [md3_buffs_summaryDesc_1236] — tekst] 타격 내성 0.1만큼 감소
   źródło: MirrorDungeonUI_2.json :: dataList[id=md3_buffs_summaryDesc_1236].content
   limit: do 120 znaków
   EN: Blunt Resistance -0.1
   PL: Odporność na Obuch -0,1

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_3
- plik gry: `MirrorDungeonUI_3.json`

120. [Tryby lochów i Kolei Refrakcji [dungeon_shop_ego_gift_upgrade] — tekst] 기프트 강화
   źródło: MirrorDungeonUI_3.json :: dataList[id=dungeon_shop_ego_gift_upgrade].content
   limit: do 120 znaków
   EN: Enhance Gifts
   PL: Ulepsz Dary
121. [Tryby lochów i Kolei Refrakcji [dungeon_shop_ego_gift_composite] — tekst] 기프트 합성
   źródło: MirrorDungeonUI_3.json :: dataList[id=dungeon_shop_ego_gift_composite].content
   limit: do 120 znaków
   EN: Fuse Gifts
   PL: Syntezuj Dary
122. [Tryby lochów i Kolei Refrakcji [dungeon_shop_ego_gift_sell] — tekst] 기프트 판매
   źródło: MirrorDungeonUI_3.json :: dataList[id=dungeon_shop_ego_gift_sell].content
   limit: do 120 znaków
   EN: Sell Gifts
   PL: Sprzedaj Dary
123. [Tryby lochów i Kolei Refrakcji [dungeon_shop_refresh] — tekst] 새로고침
   źródło: MirrorDungeonUI_3.json :: dataList[id=dungeon_shop_refresh].content
   limit: do 120 znaków
   EN: Refresh
   PL: Odśwież
124. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_selected_ego_gift] — tekst] 선택한 E.G.O 기프트
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_selected_ego_gift].content
   limit: do 120 znaków
   EN: Selected E.G.O Gift
   PL: Wybrany Dar E.G.O
125. [Tryby lochów i Kolei Refrakcji [ego_gift_upgrade_ui_title] — tekst] E.G.O 기프트 강화
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_upgrade_ui_title].content
   limit: do 120 znaków
   EN: Enhance E.G.O Gift
   PL: Ulepszanie Daru E.G.O
126. [Tryby lochów i Kolei Refrakcji [ego_gift_upgrade_confirm_format] — tekst] 코스트 <color=#F8C200>{0}</color>을(를) 소모하여 강화를 진행하시겠습니까?
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_upgrade_confirm_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, {0}
   EN: Spend <color=#F8C200>{0}</color> Cost to Enhance the E.G.O Gift?
   PL: Wydać <color=#F8C200>{0}</color> Kosztu, aby ulepszyć Dar E.G.O?
127. [Tryby lochów i Kolei Refrakcji [ego_gift_upgrade_not_enough_cost_format] — tekst] 강화에 필요한 코스트가 <color=#990000>{0}</color>부족합니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_upgrade_not_enough_cost_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}
   EN: You need <color=#990000>{0}</color> more Cost to Enhance this E.G.O Gift.
   PL: Brakuje <color=#990000>{0}</color> Kosztu do ulepszenia Daru E.G.O.
128. [Tryby lochów i Kolei Refrakcji [ego_gift_combine_ui_title] — tekst] E.G.O 기프트 합성
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_combine_ui_title].content
   limit: do 120 znaków
   EN: Fuse E.G.O Gift
   PL: Synteza Darów E.G.O
129. [Tryby lochów i Kolei Refrakcji [combine] — tekst] 합성
   źródło: MirrorDungeonUI_3.json :: dataList[id=combine].content
   limit: do 120 znaków
   EN: Fuse
   PL: Syntezuj
130. [Tryby lochów i Kolei Refrakcji [selected_gift] — tekst] 선택한 기프트
   źródło: MirrorDungeonUI_3.json :: dataList[id=selected_gift].content
   limit: do 120 znaków
   EN: Selected E.G.O Gifts
   PL: Wybrane Dary
131. [Tryby lochów i Kolei Refrakcji [expectation] — tekst] 예상
   źródło: MirrorDungeonUI_3.json :: dataList[id=expectation].content
   limit: do 120 znaków
   EN: Prediction
   PL: Prognoza
132. [Tryby lochów i Kolei Refrakcji [ego_gift_combine_ui_main_text] — tekst] 선택한 E.G.O 기프트를 조합하시겠습니까?
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_combine_ui_main_text].content
   limit: do 120 znaków
   EN: Fuse the selected E.G.O Gifts?
   PL: Zsyntezować wybrane Dary E.G.O?
133. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_normal_reward_info] — tekst] 일반
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_normal_reward_info].content
   limit: do 120 znaków
   EN: Normal
   PL: Normalny
134. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_hard_reward_info] — tekst] 어려움
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_hard_reward_info].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
135. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_current_explore] — tekst] 탐사 현황
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_current_explore].content
   limit: do 120 znaków
   EN: Exploring:
   PL: Stan wyprawy
136. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_entrance_button_formation] — tekst] 수감자
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_entrance_button_formation].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
137. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_entrance_button_start_buff] — tekst] 시작 버프
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_entrance_button_start_buff].content
   limit: do 120 znaków
   EN: Starter Buffs
   PL: Wzmocnienia początkowe
138. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_entrance_hard_hint_before_release] — tekst] 4장 클리어 시 개방
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_entrance_hard_hint_before_release].content
   limit: do 120 znaków
   EN: Clear Canto IV to Unlock
   PL: Odblokowanie po ukończeniu Canto IV
139. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_start_buff_summary_detail] — tekst] 요약/상세
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_start_buff_summary_detail].content
   limit: do 120 znaków
   EN: Summary/Details
   PL: Skrót / Szczegóły
140. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_start_buff_summary] — tekst] 요약
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_start_buff_summary].content
   limit: do 120 znaków
   EN: Summary
   PL: Skrót
141. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_start_buff_detail] — tekst] 상세
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_start_buff_detail].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
142. [Tryby lochów i Kolei Refrakcji [ego_gift_sell_ui_title] — tekst] E.G.O 기프트 판매
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_sell_ui_title].content
   limit: do 120 znaków
   EN: Sell E.G.O Gift
   PL: Sprzedaż Daru E.G.O
143. [Tryby lochów i Kolei Refrakcji [sell] — tekst] 판매
   źródło: MirrorDungeonUI_3.json :: dataList[id=sell].content
   limit: do 120 znaków
   EN: Sell
   PL: Sprzedaj
144. [Tryby lochów i Kolei Refrakcji [guided_sell_ego_gift] — tekst] 판매할 E.G.O 기프트를 선택해주세요.
   źródło: MirrorDungeonUI_3.json :: dataList[id=guided_sell_ego_gift].content
   limit: do 120 znaków
   EN: Select the E.G.O Gift you would like to sell.
   PL: Wybierz Dar E.G.O na sprzedaż.
145. [Tryby lochów i Kolei Refrakcji [ego_gift_sell_confirm_format] — tekst] [{0}]을(를) 코스트 {1}에 판매하시겠습니까?
   źródło: MirrorDungeonUI_3.json :: dataList[id=ego_gift_sell_confirm_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Sell [{0}] for {1} Cost?
   PL: Sprzedać [{0}] za {1} Kosztu?
146. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_start_buff_name] — tekst] 시작 버프 - 별의 이정표
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_3_start_buff_name].content
   limit: do 120 znaków
   EN: Starter Buffs - Astral Milestones
   PL: Wzmocnienia początkowe — Gwiezdne Drogowskazy
147. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_3_purchase_start_buff] — tekst] 별새김
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_3_purchase_start_buff].content
   limit: do 120 znaków
   EN: Engrave Stars
   PL: Wyryj gwiazdy
148. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_give_up_getting_ego_gift_with_enemy_buff] — tekst] E.G.O 기프트를 선택하지 않으면 무작위 층 버프가 선택됩니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_give_up_getting_ego_gift_with_enemy_buff].content
   limit: do 130 znaków
   EN: If you choose to continue without an E.G.O Gift, a random floor buff will be selected instead.
   PL: Jeśli pominiesz wybór Daru E.G.O, zostanie wylosowana próba piętra.
149. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_could_not_refresh] — tekst] 새로고침 불가
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_shop_could_not_refresh].content
   limit: do 120 znaków
   EN: Cannot Refresh
   PL: Nie można odświeżyć
150. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_change_formation_count] — tekst] 편성 인원
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_shop_change_formation_count].content
   limit: do 120 znaków
   EN: Team Participants
   PL: Uczestnicy składu
151. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_exploring] — tekst] ! 탐사 중 !
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_exploring].content
   limit: do 120 znaków
   EN: ! Exploring !
   PL: ! Wyprawa w toku !
152. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_before] — tekst] 진입 전
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_progress_text_before].content
   limit: do 120 znaków
   EN: Before Entry
   PL: Przed wejściem
153. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_3_normal] — tekst] 일반 난이도 {0} 층
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_progress_text_3_normal].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Normal Floor {0}
   PL: Normalny — piętro {0}
154. [Tryby lochów i Kolei Refrakcji [normal_difficulty_simple] — tekst] 일반
   źródło: MirrorDungeonUI_3.json :: dataList[id=normal_difficulty_simple].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Tryby lochów i Kolei Refrakcji [hard_difficulty_simple] — tekst] 어려움
   źródło: MirrorDungeonUI_3.json :: dataList[id=hard_difficulty_simple].content
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Tryby lochów i Kolei Refrakcji [starchip_ui_difficulty_ratio_format] — tekst] ※ 난이도: {0} [x{1}]
   źródło: MirrorDungeonUI_3.json :: dataList[id=starchip_ui_difficulty_ratio_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: ※ Difficulty: {0} [x{1}]
   PL: ※ Trudność: {0} [x{1}]
157. [Tryby lochów i Kolei Refrakcji [number_of_cleared_floors] — tekst] 클리어 층 수
   źródło: MirrorDungeonUI_3.json :: dataList[id=number_of_cleared_floors].content
   limit: do 120 znaków
   EN: Cleared Floors
   PL: Ukończone piętra
158. [Tryby lochów i Kolei Refrakcji [number_of_cleared_nodes] — tekst] 클리어 노드 수
   źródło: MirrorDungeonUI_3.json :: dataList[id=number_of_cleared_nodes].content
   limit: do 120 znaków
   EN: Cleared Nodes
   PL: Ukończone węzły
159. [Tryby lochów i Kolei Refrakcji [number_of_starlight_nodes] — tekst] 별빛 노드 수
   źródło: MirrorDungeonUI_3.json :: dataList[id=number_of_starlight_nodes].content
   limit: do 120 znaków
   EN: Starlight Nodes
   PL: Węzły Gwiezdnego Blasku
160. [Tryby lochów i Kolei Refrakcji [number_of_battles] — tekst] 전투 횟수
   źródło: MirrorDungeonUI_3.json :: dataList[id=number_of_battles].content
   limit: do 120 znaków
   EN: Encounters
   PL: Stoczone walki
161. [Tryby lochów i Kolei Refrakcji [number_of_acquired_ego_gift] — tekst] 획득한 E.G.O 기프트 수
   źródło: MirrorDungeonUI_3.json :: dataList[id=number_of_acquired_ego_gift].content
   limit: do 120 znaków
   EN: Acquired E.G.O Gifts
   PL: Zdobyte Dary E.G.O
162. [Tryby lochów i Kolei Refrakcji [choose_starting_ego_gift] — tekst] 시작 E.G.O 기프트 선택
   źródło: MirrorDungeonUI_3.json :: dataList[id=choose_starting_ego_gift].content
   limit: do 120 znaków
   EN: Starting E.G.O Gift Choice
   PL: Wybór początkowego Daru E.G.O
163. [Tryby lochów i Kolei Refrakcji [rest_gauge] — tekst] 휴식 보너스
   źródło: MirrorDungeonUI_3.json :: dataList[id=rest_gauge].content
   limit: do 120 znaków
   EN: Rest Bonus
   PL: Premia Odpoczynku
164. [Tryby lochów i Kolei Refrakcji [starlight_reward] — tekst] 별빛 보상
   źródło: MirrorDungeonUI_3.json :: dataList[id=starlight_reward].content
   limit: do 120 znaków
   EN: Starlight
   PL: Gwiezdny Blask
165. [Tryby lochów i Kolei Refrakcji [battlepass_progress_reward] — tekst] 패스 경험치 보상
   źródło: MirrorDungeonUI_3.json :: dataList[id=battlepass_progress_reward].content
   limit: do 120 znaków
   EN: Pass XP Reward
   PL: PD Przepustki
166. [Tryby lochów i Kolei Refrakcji [side_title_unable_ego_gift_upgrade] — tekst] 강화 불가
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_title_unable_ego_gift_upgrade].content
   limit: do 120 znaków
   EN: Cannot Enhance
   PL: Nie można ulepszyć
167. [Tryby lochów i Kolei Refrakcji [side_content_not_have_any_ego_gift] — tekst] 보유 중인 E.G.O 기프트가 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_not_have_any_ego_gift].content
   limit: do 120 znaków
   EN: No E.G.O Gifts owned.
   PL: Brak posiadanych Darów E.G.O.
168. [Tryby lochów i Kolei Refrakcji [side_content_ego_gift_is_not_upgradeable] — tekst] 강화할 수 없는 E.G.O 기프트입니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_ego_gift_is_not_upgradeable].content
   limit: do 120 znaków
   EN: This E.G.O Gift cannot be Enhanced.
   PL: Tego Daru E.G.O nie można ulepszyć.
169. [Tryby lochów i Kolei Refrakcji [side_content_ego_gift_is_maximum_upgraded] — tekst] 최대로 강화된 E.G.O 기프트입니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_ego_gift_is_maximum_upgraded].content
   limit: do 120 znaków
   EN: This E.G.O Gift is already fully Enhanced.
   PL: Ten Dar E.G.O jest już maksymalnie ulepszony.
170. [Tryby lochów i Kolei Refrakcji [side_title_unable_ego_gift_combine] — tekst] 합성 불가
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_title_unable_ego_gift_combine].content
   limit: do 120 znaków
   EN: Cannot Fuse
   PL: Synteza niemożliwa
171. [Tryby lochów i Kolei Refrakcji [side_content_need_more_ego_gift] — tekst] 최소 2개 이상의 E.G.O 기프트가 필요합니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_need_more_ego_gift].content
   limit: do 120 znaków
   EN: You need to own at least 2 E.G.O Gifts.
   PL: Wymagane są co najmniej 2 Dary E.G.O.
172. [Tryby lochów i Kolei Refrakcji [side_content_need_lower_tier_ego_gift] — tekst] 3등급 이하의 E.G.O 기프트만 선택할 수 있습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_need_lower_tier_ego_gift].content
   limit: do 120 znaków
   EN: You can select only Tier 3 or lower E.G.O Gifts.
   PL: Można wybrać wyłącznie Dary E.G.O rangi 3 lub niższej.
173. [Tryby lochów i Kolei Refrakcji [side_title_unable_ego_gift_sell] — tekst] 판매 불가
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_title_unable_ego_gift_sell].content
   limit: do 120 znaków
   EN: Cannot Sell
   PL: Sprzedaż niemożliwa
174. [Tryby lochów i Kolei Refrakcji [side_content_ego_gift_is_not_for_sale] — tekst] 판매할 수 없는 E.G.O 기프트입니다
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_ego_gift_is_not_for_sale].content
   limit: do 120 znaków
   EN: You cannot sell this E.G.O Gift.
   PL: Tego Daru E.G.O nie można sprzedać.
175. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_already_participated] — tekst] 참여 중
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_already_participated].content
   limit: do 120 znaków
   EN: Participating
   PL: W drużynie
176. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_acquire_ego_gift_desc] — tekst] 획득 E.G.O 기프트
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_acquire_ego_gift_desc].content
   limit: do 120 znaków
   EN: Acquire E.G.O Gift
   PL: Zdobywany Dar E.G.O
177. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_acquire_enemy_buff] — tekst] 추가되는 고난
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_acquire_enemy_buff].content
   limit: do 120 znaków
   EN: Mounting Trials
   PL: Dodawana Próba
178. [Tryby lochów i Kolei Refrakcji [mirror_dungeon3_entrance_hard_hint_after_release] — tekst] <개방 조건>\n4-54 클리어\n호수의 거울 일반 난이도 클리어
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon3_entrance_hard_hint_after_release].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <Unlock Conditions>\nClear 4-54\nClear Mirror of the Lake Normal Difficulty
   PL: [Warunki odblokowania]\nUkończ 4-54\nUkończ Lustro Jeziora (Normalny)
179. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_reload_select_ego_gift_category] — tekst] 새로고침 (1회)
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_reload_select_ego_gift_category].content
   limit: do 120 znaków
   EN: Refresh (Once)
   PL: Odśwież (1 raz)
180. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_select_chip_effect] — tekst] 별의 소원
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_select_chip_effect].content
   limit: do 120 znaków
   EN: Wish of Stars
   PL: Życzenie Gwiazd
181. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_select_chip_effect_desc_selected] — tekst] 별빛 {0}을 소모하여 이번 거울 던전 탐사 과정에서 선택한 효과를 적용합니다.\n선택을 해제하거나 별빛을 모두 소모하기 전까지는 선택한 효과가 시작 시 자동으로 적용됩니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_select_chip_effect_desc_selected].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Spend {0} Starlight to activate the selected effect for this Mirror Dungeon run.\nUnless you deactivate the effect, or unless you deplete your Starlight, the selected effect will be automatically applied upon starting a new Mirror Dungeon run.
   PL: Zużyj {0} Gwiezdnego Blasku, aby aktywować wybrany efekt w tej wyprawie do Lustrzanego Lochu.\nDopóki nie wyłączysz efektu lub nie wyczerpiesz Gwiezdnego Blasku, pozostanie on automatycznie zaznaczony przy kolejnych wejściach.
182. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_select_chip_effect_desc_not_selected] — tekst] 보유한 별빛을 소모하여 이번 거울 던전 탐사 과정에서 특별한 효과를 적용할 수 있습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_select_chip_effect_desc_not_selected].content
   limit: do 120 znaków
   EN: Spend Starlight to activate special effects for this Mirror Dungeon run.
   PL: Zużyj posiadany Gwiezdny Blask, aby aktywować specjalne efekty w tej wyprawie do Lustrzanego Lochu.
183. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_atart_buff_activation] — tekst] 활성화
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_atart_buff_activation].content
   limit: do 120 znaków
   EN: Activate
   PL: Aktywuj
184. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_atart_buff_diactivation] — tekst] 비활성화
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_atart_buff_diactivation].content
   limit: do 120 znaków
   EN: Deactivate
   PL: Dezaktywuj
185. [Tryby lochów i Kolei Refrakcji [mirrordungeon_unable_to_change_activation_buffs_when_running_dungeon] — tekst] 거울 던전 진행 중에는 시작 버프 활성화 여부를 변경할 수 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirrordungeon_unable_to_change_activation_buffs_when_running_dungeon].content
   limit: do 130 znaków
   EN: You cannot activate or deactivate your Starter Buffs while a Mirror Dungeon run is in progress.
   PL: Nie można zmieniać aktywacji wzmocnień początkowych podczas trwającej wyprawy do Lustrzanego Lochu.
186. [Tryby lochów i Kolei Refrakcji [mirrordungeon_edit_start_buff_activation] — tekst] 빠른 편집
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirrordungeon_edit_start_buff_activation].content
   limit: do 120 znaków
   EN: Quick Edit
   PL: Szybka edycja
187. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_3_hard] — tekst] 어려움 난이도 {0} 층
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_progress_text_3_hard].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Hard Floor {0}
   PL: Trudny — piętro {0}
188. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_unable_to_modify_activation_of_start_buff_during_running] — tekst] 거울 던전 진행 중에는 시작 버프 활성화 여부를 변경할 수 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungeon_unable_to_modify_activation_of_start_buff_during_running].content
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Tryby lochów i Kolei Refrakcji [add_enemy_level] — tekst] 적 레벨 증가
   źródło: MirrorDungeonUI_3.json :: dataList[id=add_enemy_level].content
   limit: do 120 znaków
   EN: Enemy Level Up
   PL: Wzrost poziomu wrogów
190. [Tryby lochów i Kolei Refrakcji [mirrordungeon_unable_to_change_activation_buffs_when_parent_buff_off] — tekst] 주요 버프가 비활성화된 상태에서는 보조 버프를 활성화할 수 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirrordungeon_unable_to_change_activation_buffs_when_parent_buff_off].content
   limit: do 120 znaków
   EN: You cannot activate the Secondary Buffs while the Primary Buffs are deactivated.
   PL: Nie można aktywować wzmocnień pobocznych, gdy wzmocnienie główne jest wyłączone.
191. [Tryby lochów i Kolei Refrakcji [mirrordungeon_purchase_buffs_when_parent_buff_off] — tekst] 주요 버프가 비활성화된 상태에서는 보조 버프를 별새김할 수 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirrordungeon_purchase_buffs_when_parent_buff_off].content
   limit: do 120 znaków
   EN: You cannot Engrave Stars on Secondary Buffs while the Primary Buffs are deactivated.
   PL: Nie można wyryć gwiazd na wzmocnieniu pobocznym, gdy wzmocnienie główne jest wyłączone.
192. [Tryby lochów i Kolei Refrakcji [side_content_already_owned_tier_ego_gift] — tekst] 현재 쉼터에서 더이상 해당 등급의 E.G.O 기프트를 합성으로 얻을 수 없습니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_already_owned_tier_ego_gift].content
   limit: do 120 znaków
   EN: You can no longer obtain that Tier of E.G.O Gifts via 'Fuse Gift' from the Rest Stops.
   PL: W tym Przystanku Odpoczynku nie można już uzyskać Daru E.G.O tej rangi poprzez Syntezę.
193. [Tryby lochów i Kolei Refrakcji [mirror_dungoen_ego_gift_history_view_desc] — tekst] 설명 보기
   źródło: MirrorDungeonUI_3.json :: dataList[id=mirror_dungoen_ego_gift_history_view_desc].content
   limit: do 120 znaków
   EN: View Desc.
   PL: Pokaż opis
194. [Tryby lochów i Kolei Refrakcji [side_content_ego_gift_is_unable_combine] — tekst] 합성할 수 없는 E.G.O 기프트입니다.
   źródło: MirrorDungeonUI_3.json :: dataList[id=side_content_ego_gift_is_unable_combine].content
   limit: do 120 znaków
   EN: This E.G.O Gift cannot be Fused.
   PL: Tego Daru E.G.O nie można użyć do Syntezy.

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_4
- plik gry: `MirrorDungeonUI_4.json`

195. [Tryby lochów i Kolei Refrakcji [dungeon_selectable] — tekst] 선택 가능
   źródło: MirrorDungeonUI_4.json :: dataList[id=dungeon_selectable].content
   limit: do 120 znaków
   EN: Selectable
   PL: Dostępne
196. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reawrd_card_selection] — tekst] 전투 보상 카드 선택
   źródło: MirrorDungeonUI_4.json :: dataList[id=dungeon_battle_reawrd_card_selection].content
   limit: do 120 znaków
   EN: Select Encounter Reward Card
   PL: Wybierz kartę nagrody za walkę
197. [Tryby lochów i Kolei Refrakcji [dungeon_opportunity_to_select_rewards_remaining] — tekst] 보상 선택 기회가 남아있습니다.\n보상을 선택하지 않고 진행하시겠습니까?
   źródło: MirrorDungeonUI_4.json :: dataList[id=dungeon_opportunity_to_select_rewards_remaining].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You have not selected a reward yet.\nContinue without choosing a reward?
   PL: Pozostała niewykorzystana szansa wyboru nagrody.\nKontynuować bez jej odebrania?
198. [Tryby lochów i Kolei Refrakcji [mirrordungeon_appear_able_theme_pack_title] — tekst] {0} - 등장 테마팩
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_appear_able_theme_pack_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} - Featured Theme Packs
   PL: {0} — Dostępne Pakiety Tematyczne
199. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_pack_boss] — tekst] 등장 보스
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_theme_pack_boss].content
   limit: do 120 znaków
   EN: Featured Boss
   PL: Pojawiający się boss
200. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_pack_ego_gift] — tekst] 등장 E.G.O 기프트
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_theme_pack_ego_gift].content
   limit: do 120 znaków
   EN: Featured E.G.O Gifts
   PL: Pojawiające się Dary E.G.O
201. [Tryby lochów i Kolei Refrakcji [mirrordunge_theme_pack_history_button_label] — tekst] 테마팩 기록집
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordunge_theme_pack_history_button_label].content
   limit: do 120 znaków
   EN: Theme Pack Compendium
   PL: Kompendium Pakietów Tematycznych
202. [Tryby lochów i Kolei Refrakcji [simulation_difficulty] — tekst] 시뮬레이션 난이도
   źródło: MirrorDungeonUI_4.json :: dataList[id=simulation_difficulty].content
   limit: do 120 znaków
   EN: Simulation
   PL: Symulacja
203. [Tryby lochów i Kolei Refrakcji [ritournelle_difficulty] — tekst] 리토르넬로 난이도
   źródło: MirrorDungeonUI_4.json :: dataList[id=ritournelle_difficulty].content
   limit: do 120 znaków
   EN: Ritornello
   PL: Ritornello
204. [Tryby lochów i Kolei Refrakcji [enter_simulation_difficulty] — tekst] 시뮬레이션 난이도 입장
   źródło: MirrorDungeonUI_4.json :: dataList[id=enter_simulation_difficulty].content
   limit: do 120 znaków
   EN: Enter Simulation
   PL: Wejdź (Symulacja)
205. [Tryby lochów i Kolei Refrakcji [enter_ritournelle_difficulty] — tekst] 리토르넬로 난이도 입장
   źródło: MirrorDungeonUI_4.json :: dataList[id=enter_ritournelle_difficulty].content
   limit: do 120 znaków
   EN: Enter Ritornello
   PL: Wejdź (Ritornello)
206. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_4_normal] — tekst] 시뮬레이션 {0}층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_progress_text_4_normal].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Simulation Floor {0}
   PL: Symulacja — piętro {0}
207. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_4_hard] — tekst] 리토르넬로 {0}층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_progress_text_4_hard].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Ritornello Floor {0}
   PL: Ritornello — piętro {0}
208. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_before_exploration] — tekst] 탐사 전
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_progress_text_before_exploration].content
   limit: do 120 znaków
   EN: Before Entry
   PL: Przed wejściem
209. [Tryby lochów i Kolei Refrakcji [mirror_dungeon4_entrance_hard_hint_after_release] — tekst] <개방 조건>\n주요 이야기 5-36 클리어\n폭풍의 거울 시뮬레이션 난이도 클리어
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon4_entrance_hard_hint_after_release].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <Unlock Conditions>\nClear 5-36\nClear Mirror of the Wuthering\nSimulation Difficulty
   PL: [Warunki odblokowania]\nUkończ etap 5-36\nUkończ Lustro Wichury (Symulacja)
210. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_elite_battle] — tekst] 정예 전투
   źródło: MirrorDungeonUI_4.json :: dataList[id=dungeon_encounter_guide_elite_battle].content
   limit: do 120 znaków
   EN: Elite Encounter
   PL: Starcie elitarne
211. [Tryby lochów i Kolei Refrakcji [purchase_ego_gift] — tekst] E.G.O 기프트 구매
   źródło: MirrorDungeonUI_4.json :: dataList[id=purchase_ego_gift].content
   limit: do 120 znaków
   EN: Purchase E.G.O Gifts
   PL: Zakup Darów E.G.O
212. [Tryby lochów i Kolei Refrakcji [purchase_personality_skill_desc] — tekst] 코스트 <color=#f8c200>{0}</color>을 소모하여 교체하시겠습니까?
   źródło: MirrorDungeonUI_4.json :: dataList[id=purchase_personality_skill_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: Spend <color=#f8c200>{0}</color> Cost to replace this Skill?
   PL: Wydać <color=#f8c200>{0}</color> Kosztu, aby wymienić umiejętność?
213. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_start_buff_name] — tekst] 별의 귀로
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_start_buff_name].content
   limit: do 120 znaków
   EN: Path of Stars
   PL: Ścieżka Gwiazd
214. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_1] — tekst] 폭풍의 눈
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_1].content
   limit: do 120 znaków
   EN: Eye of the Storm
   PL: Oko Cyklonu
215. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_2] — tekst] 벽력성
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_2].content
   limit: do 120 znaków
   EN: Thunder
   PL: Grom
216. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_3] — tekst] 칼바람
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_3].content
   limit: do 120 znaków
   EN: Biting Wind
   PL: Przejmujący Wicher
217. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_4] — tekst] 순풍
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_4].content
   limit: do 120 znaków
   EN: Fair Winds
   PL: Pomyślny Wiatr
218. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_5] — tekst] 무리 지은 번개
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_5].content
   limit: do 120 znaków
   EN: Cascade of Levin
   PL: Kaskada Błyskawic
219. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_6] — tekst] 모여드는 폭풍
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_6].content
   limit: do 120 znaków
   EN: Gathering Storm
   PL: Zbierająca się Burza
220. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_7] — tekst] 용오름
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_7].content
   limit: do 120 znaków
   EN: Tornado
   PL: Trąba Powietrzna
221. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_8] — tekst] 제야의 울림
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_8].content
   limit: do 120 znaków
   EN: Ringing of the New Year's Eve
   PL: Dzwon Ostatniej Nocy Roku
222. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_9] — tekst] 희미한 땅거미
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_9].content
   limit: do 120 znaków
   EN: Faint Evenfall
   PL: Nikły Zmierzch
223. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_10] — tekst] 검은 극야
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_10].content
   limit: do 120 znaków
   EN: Black Polar Night
   PL: Czarna Noc Polarna
224. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_11] — tekst] 고요한 새벽
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_11].content
   limit: do 120 znaków
   EN: Still Dawn
   PL: Cichy Świt
225. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_12] — tekst] 차가운 여명
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_12].content
   limit: do 120 znaków
   EN: Wintry Daybreak
   PL: Mroźny Brzask
226. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_13] — tekst] 불야성
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_13].content
   limit: do 120 znaków
   EN: Nightless City
   PL: Bezsenne Miasto
227. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_14] — tekst] 양떼구름
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_14].content
   limit: do 120 znaków
   EN: Sheepback Clouds
   PL: Obłoki Barankowe
228. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_15] — tekst] 드높은 운해
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_15].content
   limit: do 120 znaków
   EN: Grand Sea of Clouds
   PL: Bezkresne Morze Chmur
229. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_16] — tekst] 재넘이
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_16].content
   limit: do 120 znaków
   EN: Katabatic Wind
   PL: Wiatr znad Przełęczy
230. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_17] — tekst] 거센 돌풍
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_17].content
   limit: do 120 znaków
   EN: Fierce Gust
   PL: Porywisty Szkwał
231. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_18] — tekst] 서풍의 귀로
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_18].content
   limit: do 120 znaków
   EN: Path of the West Wind
   PL: Szlak Zachodniego Wiatru
232. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_19] — tekst] 상승기류
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_19].content
   limit: do 120 znaków
   EN: Updraft
   PL: Prąd Wznoszący
233. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_19_1] — tekst] 밤 소나기
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_19_1].content
   limit: do 120 znaków
   EN: Night Rain
   PL: Nocna Ulewa
234. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_20] — tekst] 낙뢰향연
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_20].content
   limit: do 120 znaków
   EN: Feast of Lightning
   PL: Uczta Piorunów
235. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_21] — tekst] 뒤따르는 뇌명
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_21].content
   limit: do 120 znaków
   EN: Impending Thunder
   PL: Nadciągający Grzmot
236. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_22] — tekst] 두터운 안개
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_22].content
   limit: do 120 znaków
   EN: Hazy Mist
   PL: Gęsta Mgła
237. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_23] — tekst] 산돌림
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_23].content
   limit: do 120 znaków
   EN: Itinerant Rain
   PL: Wędrowny Deszcz
238. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_24] — tekst] 끝없는 대류
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_24].content
   limit: do 120 znaków
   EN: Endless Current
   PL: Nieustanna Konwekcja
239. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_25] — tekst] 사건의 지평선
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_25].content
   limit: do 120 znaków
   EN: Event Horizon
   PL: Horyzont Zdarzeń
240. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_26] — tekst] 은하수
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_26].content
   limit: do 120 znaków
   EN: Milky Way
   PL: Droga Mleczna
241. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_4_buffs_title_27] — tekst] 다가오는 혜성
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_4_buffs_title_27].content
   limit: do 120 znaków
   EN: Impending Comet
   PL: Nadciągająca Kometa
242. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_100] — tekst] [한정]\n별새김 진행 시, 별빛 200 획득 (최초 1회 한정, 활성화 영향을 받지 않음)
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_100].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Limited]\nGain 200 Starlight upon engraving this Star (1-time only, unaffected by activation status)
   PL: [Jednorazowe]\nPo wyryciu gwiazdy zyskaj 200 Gwiezdnego Blasku (tylko za 1. razem, niezależnie od aktywacji)
243. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_101] — tekst] [시작 E.G.O 기프트]\n신규 E.G.O 기프트 7종 시작 E.G.O 기프트 목록에 추가
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nIntroduce 7 new E.G.O Gifts to the Starting E.G.O Gift pool
   PL: [Początkowy Dar E.G.O]\nDodaje 7 nowych Darów E.G.O do puli początkowych Darów E.G.O
244. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1011] — tekst] [시작 E.G.O 기프트]\n화상 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1011].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Burn E.G.O Gifts Category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Podpalenie
245. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1012] — tekst] [시작 E.G.O 기프트]\n출혈 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1012].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Bleed E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Krwawienie
246. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1013] — tekst] [시작 E.G.O 기프트]\n진동 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1013].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Tremor E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Wstrząs
247. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1014] — tekst] [시작 E.G.O 기프트]\n파열 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1014].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Rupture E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Rozdarcie
248. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1015] — tekst] [시작 E.G.O 기프트]\n침잠 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1015].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Sinking E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Zatonięcie
249. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1016] — tekst] [시작 E.G.O 기프트]\n호흡 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1016].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Poise E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Oddech
250. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1017] — tekst] [시작 E.G.O 기프트]\n충전 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1017].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Charge E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Ładunek
251. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_102] — tekst] [시작 E.G.O 기프트]\n신규 E.G.O 기프트 6종 시작 E.G.O 기프트 목록에 추가
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_102].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nIntroduce 6 new E.G.O Gifts to the Starting E.G.O Gift pool
   PL: [Początkowy Dar E.G.O]\nDodaje 6 nowych Darów E.G.O do puli początkowych Darów E.G.O
252. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1021] — tekst] [시작 E.G.O 기프트]\n참격 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1021].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Slash E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Cięcie
253. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1022] — tekst] [시작 E.G.O 기프트]\n관통 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1022].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Pierce E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Kłucie
254. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1023] — tekst] [시작 E.G.O 기프트]\n타격 E.G.O 기프트 항목 개방
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1023].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nUnlocks Blunt E.G.O Gifts category
   PL: [Początkowy Dar E.G.O]\nOdblokowuje kategorię Darów E.G.O: Obuch
255. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1024] — tekst] (사용 안 함)
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1024].content
   limit: do 120 znaków
   EN: (NOT USED)
   PL: (NIEUŻYWANE)
256. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_103] — tekst] [공용]\n시작 코스트 50 획득
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_103].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +50 Starting Cost
   PL: [Ogólne]\nPoczątkowy Koszt +50
257. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1031] — tekst] [공용]\n시작 코스트 +50
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1031].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +50 Starting Cost
   PL: [Ogólne]\nPoczątkowy Koszt +50
258. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1032] — tekst] [공용]\n시작 코스트 +50
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1032].content
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
259. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1033] — tekst] [공용]\n시작 코스트 +50
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1033].content
   (powtórzenie elementu 257 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_104] — tekst] [공용]\n2등급 신규 E.G.O 기프트 16종 상점, 합성 결과, 전투 보상에 추가
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_104].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nIntroduce 16 new Tier 2 E.G.O Gifts to the Shops, Gift Fusion results, and Encounter Rewards pool
   PL: [Ogólne]\nDodaje 16 nowych Darów E.G.O rangi 2 do Sklepu, wyników Syntezy i nagród za walkę
261. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1041] — tekst] [시작 E.G.O 기프트]\n화상 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1041].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Burn Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Podpalenia +1
262. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1042] — tekst] [시작 E.G.O 기프트]\n출혈 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1042].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Bleed Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Krwawienia +1
263. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1043] — tekst] [시작 E.G.O 기프트]\n진동 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1043].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Tremor Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Wstrząsu +1
264. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1044] — tekst] [시작 E.G.O 기프트]\n파열 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1044].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Rupture Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Rozdarcia +1
265. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1045] — tekst] [시작 E.G.O 기프트]\n침잠 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1045].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Sinking Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Zatonięcia +1
266. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1046] — tekst] [시작 E.G.O 기프트]\n호흡 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1046].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Poise Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Oddechu +1
267. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1047] — tekst] [시작 E.G.O 기프트]\n충전 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1047].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Charge Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Ładunku +1
268. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_105] — tekst] [공용]\n3~4등급 신규 E.G.O 기프트 28종 상점, 합성 결과, 전투 보상에 추가
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_105].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nIntroduce 28 new Tier 3~4 E.G.O Gifts to the Shops, Gift Fusion results, and Encounter Rewards pool
   PL: [Ogólne]\nDodaje 28 nowych Darów E.G.O rangi 3~4 do Sklepu, wyników Syntezy i nagród za walkę
269. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1051] — tekst] [시작 E.G.O 기프트]\n참격 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1051].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Slash Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Cięcia +1
270. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1052] — tekst] [시작 E.G.O 기프트]\n관통 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1052].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Pierce Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Kłucia +1
271. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1053] — tekst] [시작 E.G.O 기프트]\n타격 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1053].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Blunt Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się Darów E.G.O Obuchu +1
272. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1054] — tekst] [시작 E.G.O 기프트]\n무작위 E.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1054].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Starting E.G.O Gift]\nNumber of E.G.O Gifts appearing in the Random Category +1
   PL: [Początkowy Dar E.G.O]\nLiczba pojawiających się losowych Darów E.G.O +1
273. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_106] — tekst] [상점]\n선택 가능한 E.G.O 기프트 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_106].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nNumber of E.G.O Gifts sold at Shops +1
   PL: [Sklep]\nLiczba Darów E.G.O do wyboru w Sklepie +1
274. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_111] — tekst] [상점]\nE.G.O 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_111].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nSells higher Tier E.G.O Gifts
   PL: [Sklep]\nWyższa ranga pojawiających się Darów E.G.O
275. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1111] — tekst] [상점]\nE.G.O 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1111].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
276. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1112] — tekst] [상점]\nE.G.O 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1112].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1113] — tekst] [상점]\nE.G.O 기프트 출현 등급 상승
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1113].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_112] — tekst] [상점]\n등장 E.G.O 기프트 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_112].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nNumber of E.G.O Gifts sold at Shops +1
   PL: [Sklep]\nLiczba pojawiających się Darów E.G.O +1
279. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1121] — tekst] [상점]\n새로고침 비용 -20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1121].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nRefresh Cost -20%
   PL: [Sklep]\nKoszt odświeżenia -20%
280. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1122] — tekst] [상점]\n새로고침 비용 -20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1122].content
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_113] — tekst] [상점]\nE.G.O 기프트 구매 비용 -5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_113].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nE.G.O Gift purchase Cost -5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O -5%
282. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1131] — tekst] [상점]\n1등급 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1131].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 1 E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O rangi 1 -7,5%
283. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1132] — tekst] [상점]\n2등급 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1132].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 2E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O rangi 2 -7,5%
284. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1133] — tekst] [상점]\n3등급 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1133].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 3 E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O rangi 3 -7,5%
285. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1134] — tekst] [상점]\n4등급 이상 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1134].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 4+ E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O rangi 4+ -7,5%
286. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_114] — tekst] [상점]\nE.G.O 기프트 구매 비용 -5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_114].content
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1141] — tekst] [상점]\n화상 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1141].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nBurn E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Podpalenia -7,5%
288. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1142] — tekst] [상점]\n출혈 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1142].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nBleed E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Krwawienia -7,5%
289. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1143] — tekst] [상점]\n진동 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1143].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTremor E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Wstrząsu -7,5%
290. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1144] — tekst] [상점]\n파열 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1144].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nRupture E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Rozdarcia -7,5%
291. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1145] — tekst] [상점]\n침잠 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1145].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nSinking E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Zatonięcia -7,5%
292. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1146] — tekst] [상점]\n호흡 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1146].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nPoise E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Oddechu -7,5%
293. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1147] — tekst] [상점]\n충전 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1147].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nCharge E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Ładunku -7,5%
294. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_115] — tekst] [상점]\nE.G.O 기프트 구매 비용 -5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_115].content
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1151] — tekst] [상점]\n참격 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1151].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nSlash E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Cięcia -7,5%
296. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1152] — tekst] [상점]\n관통 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1152].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nPierce E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Kłucia -7,5%
297. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1153] — tekst] [상점]\n타격 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1153].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nBlunt E.G.O Gift purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O Obuchu -7,5%
298. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1154] — tekst] [상점]\n키워드가 없는 E.G.O 기프트 구매 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1154].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nKeywordless E.G.O Gift Purchase Cost -7.5%
   PL: [Sklep]\nKoszt zakupu Darów E.G.O bez słowa kluczowego -7,5%
299. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_116] — tekst] [상점]\nE.G.O 기프트 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_116].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nNumber of E.G.O Gifts sold at Shops +1
   PL: [Sklep]\nLiczba pojawiających się Darów E.G.O +1
300. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1161] — tekst] [상점]\n1등급 E.G.O 기프트 판매 비용 +20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1161].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 1 E.G.O Gift sale Cost +20%
   PL: [Sklep]\nCena sprzedaży Darów E.G.O rangi 1 +20%
301. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1162] — tekst] [상점]\n2등급 E.G.O 기프트 판매 비용 +20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1162].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 2 E.G.O Gift sale Cost +20%
   PL: [Sklep]\nCena sprzedaży Darów E.G.O rangi 2 +20%
302. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1163] — tekst] [상점]\n3등급 E.G.O 기프트 판매 비용 +20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1163].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 3 E.G.O Gift sale Cost +20%
   PL: [Sklep]\nCena sprzedaży Darów E.G.O rangi 3 +20%
303. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1164] — tekst] [상점]\n4등급 이상 E.G.O 기프트 판매 비용 +20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1164].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nTier 4+ E.G.O Gift sale Cost +20%
   PL: [Sklep]\nCena sprzedaży Darów E.G.O rangi 4+ +20%
304. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1165] — tekst] [상점]\n스킬 교체 비용 -20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1165].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\nSkill Replacement Cost -20%
   PL: [Sklep]\nKoszt wymiany umiejętności -20%
305. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1166] — tekst] [상점]\n스킬 교체 비용 -20%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1166].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_121] — tekst] [쉼터]\nE.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_121].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nE.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O -7,5%
307. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1211] — tekst] [쉼터]\n1등급 E.G.O 기프트의 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1211].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nTier 1 E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O rangi 1 -7,5%
308. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1212] — tekst] [쉼터]\n2등급 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1212].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nTier 2 E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O rangi 2 -7,5%
309. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1213] — tekst] [쉼터]\n3등급 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1213].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nTier 3 E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O rangi 3 -7,5%
310. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1214] — tekst] [쉼터]\n4등급 이상 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1214].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nTier 4+ E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O rangi 4+ -7,5%
311. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_122] — tekst] [상점]\n20% 확률로 새로고침 시 무료
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_122].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Shops]\n20% chance for a Cost-free Refresh
   PL: [Sklep]\n20% szansy na darmowe odświeżenie
312. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_123] — tekst] [쉼터]\nE.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_123].content
   (powtórzenie elementu 306 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1231] — tekst] [쉼터]\n화상 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1231].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nBurn E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Podpalenia -7,5%
314. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1232] — tekst] [쉼터]\n출혈 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1232].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nBleed E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Krwawienia -7,5%
315. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1233] — tekst] [쉼터]\n진동 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1233].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nTremor E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Wstrząsu -7,5%
316. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1234] — tekst] [쉼터]\n파열 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1234].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nRupture E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Rozdarcia -7,5%
317. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1235] — tekst] [쉼터]\n침잠 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1235].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nSinking E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Zatonięcia -7,5%
318. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1236] — tekst] [쉼터]\n호흡 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1236].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nPoise E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Oddechu -7,5%
319. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1237] — tekst] [쉼터]\n충전 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1237].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nCharge E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Ładunku -7,5%
320. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_124] — tekst] [쉼터]\n20% 확률로 강화 시 비용 반환
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_124].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\n20% chance to refund Enhancement Cost
   PL: [Przystanek]\n20% szansy na zwrot Kosztu przy ulepszeniu
321. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_125] — tekst] [쉼터]\nE.G.O 기프트 강화 비용 -10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_125].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nE.G.O Gift Enhance Cost -10%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O -10%
322. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1251] — tekst] [쉼터]\n참격 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1251].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nSlash E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Cięcia -7,5%
323. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1252] — tekst] [쉼터]\n관통 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1252].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nPierce E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Kłucia -7,5%
324. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1253] — tekst] [쉼터]\n타격 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1253].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nBlunt E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O Obuchu -7,5%
325. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1254] — tekst] [쉼터]\n키워드가 없는 E.G.O 기프트 강화 비용 -7.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1254].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rest Stops]\nKeywordless E.G.O Gift Enhance Cost -7.5%
   PL: [Przystanek]\nKoszt ulepszenia Darów E.G.O bez słowa kluczowego -7,5%
326. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_126] — tekst] [공용]\n전투 승리 시 획득 코스트 +10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_126].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +10% more Cost after winning a Combat Encounter
   PL: [Ogólne]\nZdobywany Koszt za wygraną walkę +10%
327. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1261] — tekst] [공용]\n일반 전투 승리 시 획득 코스트 +10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1261].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +10% more Cost after winning a Regular Encounter
   PL: [Ogólne]\nZdobywany Koszt za wygrane zwykłe starcie +10%
328. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1262] — tekst] [공용]\n집중 전투 승리 시, 획득하는 코스트 +10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1262].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +10% more Cost after winning a Focused Encounter
   PL: [Ogólne]\nZdobywany Koszt za wygrane starcie skupione +10%
329. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1263] — tekst] [공용]\n정예 전투 승리 시, 획득 코스트 +10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1263].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +10% more Cost after winning an Elite Encounter
   PL: [Ogólne]\nZdobywany Koszt za wygrane starcie elitarne +10%
330. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1264] — tekst] [공용]\n보스 전투 승리 시, 획득 코스트 +10%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1264].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Universal]\nGain +10% more Cost after winning a Boss Encounter
   PL: [Ogólne]\nZdobywany Koszt za wygraną walkę z bossem +10%
331. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_131] — tekst] [층 테마]\n층 테마 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_131].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Floor Theme]\nNumber of Floor Theme Choices +1
   PL: [Motyw piętra]\nLiczba pojawiających się motywów piętra +1
332. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_132] — tekst] [전투]\n가하는 피해량 +2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_132].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\nDeal +2.5% damage
   PL: [Walka]\nZadawane obrażenia +2,5%
333. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1321] — tekst] [전투]\n가하는 피해량 +2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1321].content
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1322] — tekst] [전투]\n가하는 피해량 +2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1322].content
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1323] — tekst] [전투]\n가하는 피해량 +2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1323].content
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
336. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1324] — tekst] [전투]\n공격 레벨 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1324].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\nOffense Level +1
   PL: [Walka]\nPoziom Ataku +1
337. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1325] — tekst] [전투]\n공격 레벨 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1325].content
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_133] — tekst] [전투 보상 카드]\n전투 보상 카드 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_133].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounter Reward Cards]\nNumber of Encounter Reward Card Choices +1
   PL: [Karty nagród]\nLiczba kart nagród po walce do wyboru +1
339. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_134] — tekst] [전투]\n받는 피해량 -2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_134].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\nTake -2.5% damage
   PL: [Walka]\nOtrzymywane obrażenia -2,5%
340. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1341] — tekst] [전투]\n받는 피해량 -2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1341].content
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1342] — tekst] [전투]\n받는 피해량 -2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1342].content
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1343] — tekst] [전투]\n받는 피해량 -2.5%
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1343].content
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1344] — tekst] [전투]\n방어 레벨 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1344].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\nDefense Level +1
   PL: [Walka]\nPoziom Obrony +1
344. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1345] — tekst] [전투]\n방어 레벨 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1345].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1346] — tekst] [전투]\n방어 레벨 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1346].content
   (powtórzenie elementu 343 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_135] — tekst] [층 테마]\n층 테마 등장 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_135].content
   (powtórzenie elementu 331 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_136] — tekst] [전투]\n모든 속성 E.G.O 자원 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_136].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\n+1 to all E.G.O resources at the start of the Mirror Dungeon run
   PL: [Walka]\nZasoby E.G.O wszystkich Grzechów +1
348. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1361] — tekst] [전투]\n모든 속성 E.G.O 자원 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1361].content
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1362] — tekst] [전투]\n속도 최댓값 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1362].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Encounters]\nMax Speed +1
   PL: [Walka]\nMaks. Szybkość +1
350. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_1363] — tekst] [전투]\n속도 최댓값 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_1363].content
   (powtórzenie elementu 349 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_141] — tekst] E.G.O 기프트 선택 수 +1
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_141].content
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
352. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_142] — tekst] 시작 코스트 + 250
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_142].content
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Tryby lochów i Kolei Refrakcji [md4_buffs_summaryDesc_14] — tekst] 시작 단계에서 선택한 항목의 4등급 무작위 E.G.O 기프트를 추가로 획득
   źródło: MirrorDungeonUI_4.json :: dataList[id=md4_buffs_summaryDesc_14].content
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_1] — tekst] 합성에서는 <color=#f8c200>E.G.O 기프트의 키워드를 동일하게 맞추어 조합</color>하였을 때, 해당 키워드의 E.G.O 기프트를 획득할 확률이 증가합니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_1].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: In E.G.O Gift Fusion, <color=#f8c200>fusing E.G.O Gifts with the same Keyword</color> raises the chance of obtaining an E.G.O Gift of the corresponding Keyword.
   PL: W Syntezowaniu <color=#f8c200>połączenie Darów E.G.O o tym samym słowie kluczowym</color> zwiększa szansę na uzyskanie Daru E.G.O z tym słowem kluczowym.
355. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_2] — tekst] 두 개의 E.G.O 기프트를 조합하는 경우, 예상되는 E.G.O 기프트 단계는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_2].content
   limit: do 120 znaków
   EN: The following are the E.G.O Gift Tier forecasts when fusing 2 E.G.O Gifts together.
   PL: Przy łączeniu 2 Darów E.G.O prognozowana ranga wyniku przedstawia się następująco:
356. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_diffrent_keyword] — tekst] 서로 키워드가 다른 경우
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_diffrent_keyword].content
   limit: do 120 znaków
   EN: Combining Gifts with different Keywords
   PL: Różne słowa kluczowe
357. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_identical_keyword] — tekst] 키워드가 전부 동일한 경우
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_identical_keyword].content
   limit: do 120 znaków
   EN: Combining Gifts with the same Keyword
   PL: Wszystkie słowa kluczowe identyczne
358. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_two_same_keywords] — tekst] 두 개의 키워드가 같고 하나가 다른 경우
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_two_same_keywords].content
   limit: do 120 znaków
   EN: Combining Gifts when only 2/3 Gifts share the Keyword
   PL: Dwa takie same słowa kluczowe i jedno inne
359. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_1_0] — tekst] 1등급 + 1등급 => 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_1_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 => Tier 1
   PL: Ranga 1 + Ranga 1 => Ranga 1
360. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_1_1] — tekst] 1등급 + 1등급 => <color=#f8c200>2등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_1_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 1 + Tier 1 => <color=#f8c200>Tier 2</color>
   PL: Ranga 1 + Ranga 1 => <color=#f8c200>Ranga 2</color>
361. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_2_0] — tekst] 1등급 + 2등급 => 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_2_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2 => Tier 1
   PL: Ranga 1 + Ranga 2 => Ranga 1
362. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_2_1] — tekst] 1등급 + 2등급 => <color=#f8c200>2등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_2_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 1 + Tier 2 => <color=#f8c200>Tier 2</color>
   PL: Ranga 1 + Ranga 2 => <color=#f8c200>Ranga 2</color>
363. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_3_0] — tekst] 1등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_3_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 3 => Tier 2
   PL: Ranga 1 + Ranga 3 => Ranga 2
364. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_3_1] — tekst] 1등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_3_1].content
   (powtórzenie elementu 363 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_4_0] — tekst] 2등급 + 2등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_4_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 => Tier 2
   PL: Ranga 2 + Ranga 2 => Ranga 2
366. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_4_1] — tekst] 2등급 + 2등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_4_1].content
   (powtórzenie elementu 365 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_5_0] — tekst] 2등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_5_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 3 => Tier 2
   PL: Ranga 2 + Ranga 3 => Ranga 2
368. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_5_1] — tekst] 2등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_5_1].content
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_6_0] — tekst] 3등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_6_0].content
   limit: do 120 znaków
   EN: Tier 3 + Tier 3 => Tier 3
   PL: Ranga 3 + Ranga 3 => Ranga 3
370. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_1_desc_6_1] — tekst] 3등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_1_desc_6_1].content
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_3] — tekst] 두 개의 E.G.O 기프트를 조합하는 경우, 예상되는 E.G.O 기프트의 키워드는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_3].content
   limit: do 120 znaków
   EN: The following are the E.G.O Gift Keyword forecasts when fusing 2 E.G.O Gifts together.
   PL: Przy łączeniu 2 Darów E.G.O prognozowane słowo kluczowe wyniku przedstawia się następująco:
372. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_2_desc_1_0] — tekst] 재료로 사용되는 E.G.O 기프트 키워드 등장 확률이 각각 37.5%\n나머지 키워드 등장 확률 합계가 25%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_2_desc_1_0].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rates for Keywords on the Ingredient E.G.O Gifts: 37.5% each\nCombined Rate for every other Keyword: 25%
   PL: Szansa na słowo kluczowe każdego ze składników: po 37,5%\nŁączna szansa na pozostałe słowa kluczowe: 25%
373. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_2_desc_1_1] — tekst] 재료로 사용되는 E.G.O 기프트 키워드 등장 확률이 75%\n나머지 키워드 등장 확률 합계가 25%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_2_desc_1_1].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rate for Keyword on the Ingredient E.G.O Gifts: 75%\nCombined Rate for every other Keyword: 25%
   PL: Szansa na wspólne słowo kluczowe składników: 75%\nŁączna szansa na pozostałe słowa kluczowe: 25%
374. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_4] — tekst] 세 개의 E.G.O 기프트를 조합하는 경우, 예상되는 E.G.O 기프트 단계는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_4].content
   limit: do 120 znaków
   EN: The following are the E.G.O Gift Tier forecasts when fusing 3 E.G.O Gifts together.
   PL: Przy łączeniu 3 Darów E.G.O prognozowana ranga wyniku przedstawia się następująco:
375. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_1_0] — tekst] 1등급 + 1등급 + 1등급 => 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_1_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 1 => Tier 1
   PL: Ranga 1 + Ranga 1 + Ranga 1 => Ranga 1
376. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_1_1] — tekst] 1등급 + 1등급 + 1등급 => <color=#f8c200>2등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_1_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 1 + Tier 1 + Tier 1 => <color=#f8c200>Tier 2</color>
   PL: Ranga 1 + Ranga 1 + Ranga 1 => <color=#f8c200>Ranga 2</color>
377. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_2_0] — tekst] 1등급 + 1등급 + 2등급 => 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_2_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 2 => Tier 1
   PL: Ranga 1 + Ranga 1 + Ranga 2 => Ranga 1
378. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_2_1] — tekst] 1등급 + 1등급 + 2등급 => <color=#f8c200>2등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_2_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 1 + Tier 1 + Tier 2 => <color=#f8c200>Tier 2</color>
   PL: Ranga 1 + Ranga 1 + Ranga 2 => <color=#f8c200>Ranga 2</color>
379. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_3_0] — tekst] 1등급 + 1등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_3_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 3 => Tier 2
   PL: Ranga 1 + Ranga 1 + Ranga 3 => Ranga 2
380. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_3_1] — tekst] 1등급 + 1등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_3_1].content
   (powtórzenie elementu 379 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
381. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_4_0] — tekst] 1등급 + 2등급 + 2등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_4_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2 + Tier 2 => Tier 2
   PL: Ranga 1 + Ranga 2 + Ranga 2 => Ranga 2
382. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_4_1] — tekst] 1등급 + 2등급 + 2등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_4_1].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_5_0] — tekst] 1등급 + 2등급 + 3등급 => 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_5_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2 + Tier 3 => Tier 2
   PL: Ranga 1 + Ranga 2 + Ranga 3 => Ranga 2
384. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_5_1] — tekst] 1등급 + 2등급 + 3등급 => <color=#f8c200>3등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_5_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 1 + Tier 2 + Tier 3 => <color=#f8c200>Tier 3</color>
   PL: Ranga 1 + Ranga 2 + Ranga 3 => <color=#f8c200>Ranga 3</color>
385. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_6_0] — tekst] 1등급 + 3등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_6_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 3 + Tier 3 => Tier 3
   PL: Ranga 1 + Ranga 3 + Ranga 3 => Ranga 3
386. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_6_1] — tekst] 1등급 + 3등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_6_1].content
   (powtórzenie elementu 385 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_7_0] — tekst] 2등급 + 2등급 + 2등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_7_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 + Tier 2 => Tier 3
   PL: Ranga 2 + Ranga 2 + Ranga 2 => Ranga 3
388. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_7_1] — tekst] 2등급 + 2등급 + 2등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_7_1].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_8_0] — tekst] 2등급 + 2등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_8_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 + Tier 3 => Tier 3
   PL: Ranga 2 + Ranga 2 + Ranga 3 => Ranga 3
390. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_8_1] — tekst] 2등급 + 2등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_8_1].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 + Tier 2 => Tier 3
   PL: Ranga 2 + Ranga 2 + Ranga 3 => Ranga 3
391. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_9_0] — tekst] 2등급 + 3등급 + 3등급 => 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_9_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 3 + Tier 3 => Tier 3
   PL: Ranga 2 + Ranga 3 + Ranga 3 => Ranga 3
392. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_9_1] — tekst] 2등급 + 3등급 + 3등급 => <color=#f8c200>4등급</color>
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_9_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: Tier 2 + Tier 3 + Tier 3 => <color=#f8c200>Tier 4</color>
   PL: Ranga 2 + Ranga 3 + Ranga 3 => <color=#f8c200>Ranga 4</color>
393. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_10_0] — tekst] 3등급 + 3등급 + 3등급 => 4등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_10_0].content
   limit: do 120 znaków
   EN: Tier 3 + Tier 3 + Tier 3 => Tier 4
   PL: Ranga 3 + Ranga 3 + Ranga 3 => Ranga 4
394. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_3_desc_10_1] — tekst] 3등급 + 3등급 + 3등급 => 4등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_3_desc_10_1].content
   (powtórzenie elementu 393 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_5] — tekst] 세 개의 E.G.O 기프트를 조합하는 경우, 예상되는 E.G.O 기프트의 키워드는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_5].content
   limit: do 120 znaków
   EN: The following are the E.G.O Gift Keyword forecasts when fusing 3 E.G.O Gifts together.
   PL: Przy łączeniu 3 Darów E.G.O prognozowane słowo kluczowe wyniku przedstawia się następująco:
396. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_4_desc_1_0] — tekst] 재료로 사용되는 E.G.O 기프트 키워드 등장 확률이 각각 25%\n\n나머지 키워드 등장 확률 합계가 25%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_4_desc_1_0].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rates for Keywords on the Ingredient E.G.O Gifts: 25% each\nCombined Rate for every other Keyword: 25%
   PL: Szansa na słowo kluczowe każdego ze składników: po 25%\n\nŁączna szansa na pozostałe słowa kluczowe: 25%
397. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_4_desc_1_1] — tekst] 재료로 사용되는 E.G.O 기프트(셋 중 키워드가 겹치는 두 개의 기프트) 키워드 등장 확률이 50%\n\n재료로 사용되는 E.G.O 기프트(셋 중 키워드가 겹치지 않는 기프트) 키워드 등장 확률이 25%\n\n나머지 키워드 등장 확률 합계가 25%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_4_desc_1_1].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rate for the Keyword on the Ingredient E.G.O Gifts that share the Keyword: 50%\n\nRate for the Keyword on the Ingredient E.G.O Gift that doesn't share the Keyword: 25%\n\nCombined Rate for every other Keyword: 25%
   PL: Szansa na wspólne słowo kluczowe 2 składników: 50%\n\nSzansa na słowo kluczowe trzeciego składnika: 25%\n\nŁączna szansa na pozostałe słowa kluczowe: 25%
398. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_table_4_desc_1_2] — tekst] 재료로 사용되는 E.G.O 기프트 키워드 등장 확률이 75%\n\n나머지 키워드 등장 확률 합계가 25%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_table_4_desc_1_2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rate for Keyword on the Ingredient E.G.O Gifts: 75%\n\nCombined Rate for every other Keyword: 25%
   PL: Szansa na wspólne słowo kluczowe składników: 75%\n\nŁączna szansa na pozostałe słowa kluczowe: 25%
399. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_desc_6] — tekst] ※ 단, 위 조건에 해당하는 E.G.O 기프트를 해당 합성 시점에서 더 이상 획득할 수 없는 경우에는 다른 등급 또는 키워드의 E.G.O 기프트를 획득할 수 있습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_desc_6].content
   limit: do 200 znaków
   EN: ※ However, if there are no more obtainable E.G.O Gifts fitting the above conditions, Gift Fusion may result in E.G.O Gifts of different Tiers or Keywords.
   PL: ※ Jeśli w chwili Syntezy nie ma już dostępnych Darów E.G.O spełniających powyższe warunki, wynikiem może być Dar E.G.O innej rangi lub słowa kluczowego.
400. [Tryby lochów i Kolei Refrakcji [mirror_ego_gift_combine_guide_popup_title] — tekst] 합성 안내
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_ego_gift_combine_guide_popup_title].content
   limit: do 120 znaków
   EN: Fusion Guide
   PL: Zasady Syntezy
401. [Tryby lochów i Kolei Refrakcji [mirrordungeon_select_theme_pack_at_floor] — tekst] {0}층 테마팩 선택
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_select_theme_pack_at_floor].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select Floor {0} Theme Pack
   PL: Wybór Pakietu Tematycznego — piętro {0}
402. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ego_gift_appear_rate_up] — tekst] 등장 확률 업
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_ego_gift_appear_rate_up].content
   limit: do 120 znaków
   EN: Rate Up
   PL: Większa szansa
403. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ego_gift_appearable] — tekst] 등장 가능
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_ego_gift_appearable].content
   limit: do 120 znaków
   EN: Featured
   PL: Dostępne
404. [Tryby lochów i Kolei Refrakcji [mirrordungeon_selected_floor_theme_label] — tekst] 선택 층 테마
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_selected_floor_theme_label].content
   limit: do 120 znaków
   EN: Selected Floor Theme
   PL: Wybrany motyw piętra
405. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ego_gift_sort_by_tier] — tekst] 등급 순
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_ego_gift_sort_by_tier].content
   limit: do 120 znaków
   EN: By Tier
   PL: Wg rangi
406. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ego_gift_sort_by_keyword] — tekst] 키워드 순
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirrordungeon_ego_gift_sort_by_keyword].content
   limit: do 120 znaków
   EN: By Keyword
   PL: Wg słowa kluczowego
407. [Tryby lochów i Kolei Refrakcji [side_content_cannot_acquire_specific_ego_gift] — tekst] 현재 층 테마에서 획득할 수 있는 {0}등급 E.G.O 기프트가 없습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=side_content_cannot_acquire_specific_ego_gift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: There are no Tier {0} E.G.O Gifts obtainable from your current Floor Theme.
   PL: W bieżącym motywie piętra nie ma dostępnych Darów E.G.O rangi {0}.
408. [Tryby lochów i Kolei Refrakcji [side_content_free_refresh] — tekst] [신상품 팜플렛] 효과 발동\n새로 고침 비용 반환
   źródło: MirrorDungeonUI_4.json :: dataList[id=side_content_free_refresh].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [New Release Pamphlet] Buff Activated\nRefresh Cost Refunded
   PL: Aktywowano [Ulotkę Nowości]\nZwrócono Koszt odświeżenia
409. [Tryby lochów i Kolei Refrakcji [side_content_egogift_free_upgrade] — tekst] [리베이트 토큰] 효과 발동\n강화 비용 반환
   źródło: MirrorDungeonUI_4.json :: dataList[id=side_content_egogift_free_upgrade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Rebate Token] Buff Activated\nEnhancement Cost Refunded
   PL: Aktywowano [Żeton Rabatowy]\nZwrócono Koszt ulepszenia
410. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_floor_theme] — tekst] 층 테마
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_finished_panel_floor_theme].content
   limit: do 120 znaków
   EN: Floor Theme
   PL: Motyw piętra
411. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_battle_reward] — tekst] 전투 보상카드
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_finished_panel_battle_reward].content
   limit: do 120 znaków
   EN: Encounter Reward Cards
   PL: Karty nagród za walkę
412. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_used] — tekst] 소모 별빛
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_finished_panel_used].content
   limit: do 120 znaków
   EN: Starlight Cost
   PL: Zużyty Gwiezdny Blask
413. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_appeared_ego_gift] — tekst] 등장 E.G.O 기프트 목록
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_appeared_ego_gift].content
   limit: do 120 znaków
   EN: Featured E.G.O Gifts
   PL: Dostępne Dary E.G.O
414. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_select_theme_drag] — tekst] 드래그
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_select_theme_drag].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select a Pack\nAnd Pull
   PL: Przeciągnij
415. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_cannot_acquired_ego_gift] — tekst] E.G.O 기프트 획득 실패
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_cannot_acquired_ego_gift].content
   limit: do 120 znaków
   EN: Did Not Gain an E.G.O Gift
   PL: Nie zdobyto Daru E.G.O
416. [Tryby lochów i Kolei Refrakcji [simulation_difficulty_short] — tekst] 시뮬레이션
   źródło: MirrorDungeonUI_4.json :: dataList[id=simulation_difficulty_short].content
   limit: do 120 znaków
   EN: Simulation
   PL: Symulacja
417. [Tryby lochów i Kolei Refrakcji [ritournelle_difficulty_short] — tekst] 리토르넬로
   źródło: MirrorDungeonUI_4.json :: dataList[id=ritournelle_difficulty_short].content
   limit: do 120 znaków
   EN: Ritornello
   PL: Ritornello
418. [Tryby lochów i Kolei Refrakcji [easy_difficulty_simple] — tekst] 쉬움
   źródło: MirrorDungeonUI_4.json :: dataList[id=easy_difficulty_simple].content
   limit: do 120 znaków
   EN: Easy
   PL: Łatwy
419. [Tryby lochów i Kolei Refrakcji [refresh_shop_item_by_chip_warning] — tekst] 별빛을 소모하여 새로 고침을 진행하시겠습니까?\n\n<size=70%>※「별빛 새로 고침」은 <color=#990000>입장 시 보유한 별빛</color>과 <color=#990000>\n던전 진행 중에 획득한 별빛</color>을 소모하여 진행할 수\n있습니다. 단, 이를 초과하여 별빛을 소모할 수 없습니다.</size>\n\n<size=85%>입장 시 보유한 별빛 : {0}</size>
   źródło: MirrorDungeonUI_4.json :: dataList[id=refresh_shop_item_by_chip_warning].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <size=70%>, <color=#990000>, </color>, </size>, <size=85%>, {0}, \n
   EN: Consume Starlight to Refresh?\n\n<size=70%>※「Starlight Refresh」 uses <color=#990000>Starlight owned at the start of the Dungeon</color> and <color=#990000>any Starlight obtained during the Dungeon run</color>.\nHowever, you cannot spend more Starlight than what you have.</size>\n\n<size=85%>Starlight owned at the start of the Dungeon: {0}</size>
   PL: Zużyć Gwiezdny Blask, aby odświeżyć?\n\n<size=70%>※ „Gwiezdne odświeżenie” zużywa <color=#990000>Gwiezdny Blask posiadany przy wejściu</color> oraz <color=#990000>\nGwiezdny Blask zdobyty w trakcie wyprawy</color>.\nNie można wydać więcej niż posiadana pula.</size>\n\n<size=85%>Gwiezdny Blask przy wejściu: {0}</size>
420. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_theme_ego_gift_popup_valid_atk] — tekst] 유효 속성
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_theme_ego_gift_popup_valid_atk].content
   limit: do 120 znaków
   EN: Effective Affinities
   PL: Skuteczne Grzechy
421. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_keyword_refresh] — tekst] 키워드 새로고침
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_shop_keyword_refresh].content
   limit: do 120 znaków
   EN: Keyword Refresh
   PL: Odświeżenie wg słowa kluczowego
422. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_refresh_by_chip] — tekst] 별빛 새로고침
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_shop_refresh_by_chip].content
   limit: do 120 znaków
   EN: Starlight Refresh
   PL: Gwiezdne odświeżenie
423. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_keyword_refresh_popup_title] — tekst] 상점-키워드 새로고침
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_shop_keyword_refresh_popup_title].content
   limit: do 120 znaków
   EN: Shop - Keyword Refresh
   PL: Sklep — odświeżenie wg słowa kluczowego
424. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_keyword_refresh_popup_desc] — tekst] 선택한 키워드의 E.G.O 기프트가 등장할 확률이 크게 증가합니다.\n{0} 코스트를 사용하여 키워드 새로고침을 진행하시겠습니까?
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_dungeon_shop_keyword_refresh_popup_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: 'Keyword Refresh' to raise the chances of getting E.G.O Gifts of the selected Keyword category in the Shop.\nSpend {0} Cost to Keyword Refresh?
   PL: Znacząco zwiększa szansę pojawienia się Darów E.G.O wybranego słowa kluczowego.\nWydać {0} Kosztu na odświeżenie wg słowa kluczowego?
425. [Tryby lochów i Kolei Refrakcji [ego_gift_combine_ui_plz_select_keyword] — tekst] 키워드를 선택해주세요.
   źródło: MirrorDungeonUI_4.json :: dataList[id=ego_gift_combine_ui_plz_select_keyword].content
   limit: do 120 znaków
   EN: Select a Keyword.
   PL: Wybierz słowo kluczowe.
426. [Tryby lochów i Kolei Refrakcji [ego_gift_select_keyword_ui_title] — tekst] 합성 - 키워드 선택
   źródło: MirrorDungeonUI_4.json :: dataList[id=ego_gift_select_keyword_ui_title].content
   limit: do 120 znaków
   EN: Fusion - Keyword Selection
   PL: Synteza — wybór słowa kluczowego
427. [Tryby lochów i Kolei Refrakcji [ego_gift_select_keyword_ui_desc] — tekst] 원하는 키워드를 선택해주세요.
   źródło: MirrorDungeonUI_4.json :: dataList[id=ego_gift_select_keyword_ui_desc].content
   limit: do 120 znaków
   EN: Please choose a Keyword you want to Fuse into.
   PL: Wybierz docelowe słowo kluczowe Syntezy.
428. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_desc_1] — tekst] <합성 - 키워드 선택> 창에서 키워드를 설정하였다면, 예상되는 E.G.O 기프트의 키워드는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_desc_1].content
   limit: do 190 znaków
   EN: The following is the E.G.O Gift Keyword forecast once you've selected the Keyword you want to Fuse into in the <Fusion - Keyword Selection> screen.
   PL: Po ustawieniu słowa kluczowego w oknie „Synteza — wybór słowa kluczowego” szanse na słowo kluczowe wyniku przedstawiają się następująco:
429. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_col_1_title] — tekst] 합성 재료로 사용하는 E.G.O 기프트의 수량
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_col_1_title].content
   limit: do 120 znaków
   EN: Number of ingredient E.G.O Gifts used for Fusion
   PL: Liczba Darów E.G.O użytych jako składniki
430. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_col_2_title] — tekst] 설정한 키워드 등장 확률
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_col_2_title].content
   limit: do 120 znaków
   EN: Rates for an E.G.O Gift with your selected Keyword
   PL: Szansa na wybrane słowo kluczowe
431. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_1_0] — tekst] 2개
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_1_0].content
   limit: do 120 znaków
   EN: 2 Gifts
   PL: 2 szt.
432. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_1_1] — tekst] 60%
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_1_1].content
   limit: do 120 znaków
   EN: 60%
   PL: 60%
433. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_2_0] — tekst] 3개
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_2_0].content
   limit: do 120 znaków
   EN: 3 Gifts
   PL: 3 szt.
434. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_2_1] — tekst] 90%
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_2_1].content
   limit: do 120 znaków
   EN: 90%
   PL: 90%
435. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_diffrent_keyword_notice] — tekst] ※ 재료로 사용되는 E.G.O 기프트의 키워드는 결과물의 키워드에 별도의 영향을 주지 않습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_diffrent_keyword_notice].content
   limit: do 120 znaków
   EN: ※ Keywords on the ingredient E.G.O Gifts do not affect the outcome of the Fusion.
   PL: ※ Słowa kluczowe Darów E.G.O użytych jako składniki nie wpływają na słowo kluczowe wyniku.
436. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_desc_2] — tekst] 두 개의 E.G.O 기프트를 조합하는 경우, E.G.O 기프트의 단계는 최대 3등급까지 획득할 수 있으며, 예상되는 E.G.O 기프트 단계는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_desc_2].content
   limit: do 220 znaków
   EN: The following are the E.G.O Gift Tier forecasts when fusing 2 E.G.O Gifts. Please note that you can receive up to Tier 3 E.G.O Gifts when fusing 2 E.G.O Gifts together.
   PL: Przy łączeniu 2 Darów E.G.O można uzyskać maksymalnie rangę 3, a prognozowana ranga wyniku przedstawia się następująco:
437. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_col_1_title] — tekst] 재료로 사용한 E.G.O 기프트의 등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_col_1_title].content
   limit: do 120 znaków
   EN: Ingredient E.G.O Gift Tiers
   PL: Rangi składników Darów E.G.O
438. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_col_2_title] — tekst] 예상되는 E.G.O 기프트 단계
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_col_2_title].content
   limit: do 120 znaków
   EN: E.G.O Gift Tier Forecast
   PL: Prognozowana ranga Daru E.G.O
439. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_1_0] — tekst] 1등급 + 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_1_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1
   PL: Ranga 1 + Ranga 1
440. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_2_0] — tekst] 1등급 + 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_2_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2
   PL: Ranga 1 + Ranga 2
441. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_3_0] — tekst] 1등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_3_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 3
   PL: Ranga 1 + Ranga 3
442. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_4_0] — tekst] 2등급 + 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_4_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2
   PL: Ranga 2 + Ranga 2
443. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_5_0] — tekst] 2등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_5_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 3
   PL: Ranga 2 + Ranga 3
444. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_2_desc_6_0] — tekst] 3등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_2_desc_6_0].content
   limit: do 120 znaków
   EN: Tier 3 + Tier 3
   PL: Ranga 3 + Ranga 3
445. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_desc_3] — tekst] 세 개의 E.G.O 기프트를 조합하는 경우, E.G.O 기프트의 단계는 최대 4등급까지 획득할 수 있으며, 예상되는 E.G.O 기프트 단계는 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_desc_3].content
   limit: do 220 znaków
   EN: The following are the E.G.O Gift Tier forecasts when fusing 3 E.G.O Gifts. Please note that you can receive up to Tier 4 E.G.O Gifts when fusing 3 E.G.O Gifts together.
   PL: Przy łączeniu 3 Darów E.G.O można uzyskać maksymalnie rangę 4, a prognozowana ranga wyniku przedstawia się następująco:
446. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_col_1_title] — tekst] 서로 키워드가 다른 경우
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_col_1_title].content
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_col_2_title] — tekst] 예상되는 E.G.O 기프트 단계
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_col_2_title].content
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_1_0] — tekst] 1등급 + 1등급 + 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_1_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 1
   PL: Ranga 1 + Ranga 1 + Ranga 1
449. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_2_0] — tekst] 1등급 + 1등급 + 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_2_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 2
   PL: Ranga 1 + Ranga 1 + Ranga 2
450. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_3_0] — tekst] 1등급 + 1등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_3_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 1 + Tier 3
   PL: Ranga 1 + Ranga 1 + Ranga 3
451. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_4_0] — tekst] 1등급 + 2등급 + 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_4_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2 + Tier 2
   PL: Ranga 1 + Ranga 2 + Ranga 2
452. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_5_0] — tekst] 1등급 + 2등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_5_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 2 + Tier 3
   PL: Ranga 1 + Ranga 2 + Ranga 3
453. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_6_0] — tekst] 1등급 + 3등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_6_0].content
   limit: do 120 znaków
   EN: Tier 1 + Tier 3 + Tier 3
   PL: Ranga 1 + Ranga 3 + Ranga 3
454. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_7_0] — tekst] 2등급 + 2등급 + 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_7_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 + Tier 2
   PL: Ranga 2 + Ranga 2 + Ranga 2
455. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_8_0] — tekst] 2등급 + 2등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_8_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 2 + Tier 3
   PL: Ranga 2 + Ranga 2 + Ranga 3
456. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_9_0] — tekst] 2등급 + 3등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_9_0].content
   limit: do 120 znaków
   EN: Tier 2 + Tier 3 + Tier 3
   PL: Ranga 2 + Ranga 3 + Ranga 3
457. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_3_desc_10_0] — tekst] 3등급 + 3등급 + 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_table_3_desc_10_0].content
   limit: do 120 znaków
   EN: Tier 3 + Tier 3 + Tier 3
   PL: Ranga 3 + Ranga 3 + Ranga 3
458. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_tier_1] — tekst] 1등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_tier_1].content
   limit: do 120 znaków
   EN: Tier 1
   PL: Ranga 1
459. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_tier_2] — tekst] 2등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_tier_2].content
   limit: do 120 znaków
   EN: Tier 2
   PL: Ranga 2
460. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_tier_3] — tekst] 3등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_tier_3].content
   limit: do 120 znaków
   EN: Tier 3
   PL: Ranga 3
461. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_tier_4] — tekst] 4등급
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_tier_4].content
   limit: do 120 znaków
   EN: Tier 4
   PL: Ranga 4
462. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_desc_4] — tekst] 단, 해당 등급의 선택한 키워드 E.G.O 기프트를 전부 획득하였거나 현재 층의 선택지, 보스 클리어 시 등장하는 E.G.O 기프트에 이미 배정되어 획득할 수 없는 경우에는 <u><b>해당 등급 기프트 중 선택하지 않은 키워드의 E.G.O 기프트를 획득</u></b>할 수 있습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_desc_4].content
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <u>, <b>, </u>, </b>
   EN: However, if you have already acquired every single E.G.O Gift in the above Keyword & Tier combination, or if those E.G.O Gifts have already been assigned to Mirror Dungeon Events or the Boss Rewards of this Floor, then <u><b>you might acquire an E.G.O Gift of a different Tier or a Keyword category</u></b> from the chart listed above.
   PL: Jeśli jednak zdobyto już wszystkie Dary E.G.O danej rangi i wybranego słowa kluczowego albo zostały one już przypisane do wydarzeń lub nagród za bossa na bieżącym piętrze, <u><b>możesz otrzymać Dar E.G.O tej samej rangi z innym słowem kluczowym</b></u>.
463. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_desc_5] — tekst] 만약 키워드 관계 없이 해당 등급의 E.G.O 기프트를 전부 획득하였거나 앞서 설명한 내용으로 인해 추가로 획득할 수 없는 경우에는 <u><b>합성을 진행할 수 없습니다.</u></b>
   źródło: MirrorDungeonUI_4.json :: dataList[id=new_ego_gift_combine_guide_desc_5].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <u>, <b>, </u>, </b>
   EN: If you have already acquired all E.G.O Gifts in the corresponding Tier or are unable to obtain them due to the aforementioned reasons, then <u><b>you cannot proceed with the Fusion</u></b>.
   PL: Jeśli zdobyto już wszystkie Dary E.G.O danej rangi bez względu na słowo kluczowe lub nie można ich uzyskać z powyższych przyczyn, <u><b>przeprowadzenie Syntezy jest niemożliwe</b></u>.
464. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_popup_title] — tekst] 전투 보상 카드 안내
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_popup_title].content
   limit: do 120 znaków
   EN: Encounter Reward Cards Guide
   PL: Przewodnik po kartach nagród za walkę
465. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_text_1] — tekst] 전투 클리어 시, 거울 던전 난이도와 진행 중인 층에 따라 전투 보상 카드를 획득할 수 있습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_text_1].content
   limit: do 260 znaków
   EN: You may have a chance to obtain an Encounter Reward Card upon clearing an Encounter. Variables such as Mirror Dungeon Difficulty and your Current floor affect which Encounter Reward Cards you can get.
   PL: Po ukończeniu walki możesz otrzymać kartę nagrody za walkę w zależności od trudności Lustrzanego Lochu oraz bieżącego piętra.
466. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_text_2] — tekst] 전투 보상 카드의 등장 확률은 다음과 같습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_text_2].content
   limit: do 120 znaków
   EN: The following are the appearance rates for the Encounter Reward Cards.
   PL: Szanse pojawienia się kart nagród za walkę przedstawiają się następująco:
467. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_0_1] — tekst] 거울 던전 시뮬레이션
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_0_1].content
   limit: do 120 znaków
   EN: Mirror Dungeon Simulation
   PL: Lustrzany Loch — Symulacja
468. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_0_2] — tekst] 거울 던전 리토르넬로
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_0_2].content
   limit: do 120 znaków
   EN: Mirror Dungeon Ritornello
   PL: Lustrzany Loch — Ritornello
469. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_1_0] — tekst] 1층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_1_0].content
   limit: do 120 znaków
   EN: Floor 1
   PL: 1. piętro
470. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_1_1] — tekst] 일반 전투 : 7.5%\n집중 전투 : -\n정예 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_1_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 7.5%\nFocused Encounter : -\nElite Encounter : -\nBoss Encounter : 100%
   PL: Zwykłe starcie: 7,5%\nStarcie skupione: -\nStarcie elitarne: -\nWalka z bossem: 100%
471. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_1_2] — tekst] 일반 전투 : 7.5%\n집중 전투 : -\n정예 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_1_2].content
   (powtórzenie elementu 470 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_2_0] — tekst] 2층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_2_0].content
   limit: do 120 znaków
   EN: Floor 2
   PL: 2. piętro
473. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_2_1] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_2_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 10%\nFocused Encounter : 20%\nElite Encounter : 33%\nBoss Encounter : 100%
   PL: Zwykłe starcie: 10%\nStarcie skupione: 20%\nStarcie elitarne: 33%\nWalka z bossem: 100%
474. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_2_2] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_2_2].content
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_3_0] — tekst] 3층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_3_0].content
   limit: do 120 znaków
   EN: Floor 3
   PL: 3. piętro
476. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_3_1] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_3_1].content
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_3_2] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_3_2].content
   (powtórzenie elementu 473 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_4_0] — tekst] 4층
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_4_0].content
   limit: do 120 znaków
   EN: Floor 4
   PL: 4. piętro
479. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_4_1] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n보스 전투 : -
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_4_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 12.5%\nFocused Encounter : 25%\nElite Encounter : 50%\nBoss Encounter : -
   PL: Zwykłe starcie: 12,5%\nStarcie skupione: 25%\nStarcie elitarne: 50%\nWalka z bossem: -
480. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_4_2] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_4_2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 12.5%\nFocused Encounter : 25%\nElite Encounter : 50%\nBoss Encounter : 100%
   PL: Zwykłe starcie: 12,5%\nStarcie skupione: 25%\nStarcie elitarne: 50%\nWalka z bossem: 100%
481. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_5_0] — tekst] 5층 이후
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_5_0].content
   limit: do 120 znaków
   EN: Floor 5+
   PL: 5. piętro i dalej
482. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_5_1] — tekst] -
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_5_1].content
   limit: do 120 znaków
   EN: -
   PL: -
483. [Tryby lochów i Kolei Refrakcji [mirror_battle_reward_card_guide_table_1_desc_5_2] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n보스 전투 : -
   źródło: MirrorDungeonUI_4.json :: dataList[id=mirror_battle_reward_card_guide_table_1_desc_5_2].content
   (powtórzenie elementu 479 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Tryby lochów i Kolei Refrakcji [expected_result] — tekst] 예상 결과
   źródło: MirrorDungeonUI_4.json :: dataList[id=expected_result].content
   limit: do 120 znaków
   EN: Forecasts
   PL: Prognoza wyniku
485. [Tryby lochów i Kolei Refrakcji [confirmed] — tekst] 확정
   źródło: MirrorDungeonUI_4.json :: dataList[id=confirmed].content
   limit: do 120 znaków
   EN: Guaranteed
   PL: Gwarantowane
486. [Tryby lochów i Kolei Refrakcji [combine_tooltip_title] — tekst] 다음 상황일 때, 합성 결과로 나오는 E.G.O 기프트가 기존 합성 공식을 따르지 않을 수 있습니다. 이러한 경우에는 예상 키워드가 ?(무작위)로 표시됩니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=combine_tooltip_title].content
   limit: do 240 znaków
   EN: The following are the circumstances in which the resulting E.G.O Gift from the Fusion won't match the Fusion Forecasts. In such cases, Keyword Forecast will be marked as "?(Random)".
   PL: W poniższych sytuacjach wynik Syntezy Darów E.G.O może odbiegać od standardowej formuły — prognozowane słowo kluczowe jest wówczas oznaczone jako „? (Losowe)”:
487. [Tryby lochów i Kolei Refrakcji [combine_tooltip_desc1] — tekst] 선택한 키워드의 해당 등급 E.G.O 기프트를 전부 획득하였을 경우
   źródło: MirrorDungeonUI_4.json :: dataList[id=combine_tooltip_desc1].content
   limit: do 140 znaków
   EN: When every available E.G.O Gift in the selected Keyword category & forecasted Tier has already been obtained
   PL: Gdy zdobyto już wszystkie dostępne Dary E.G.O wybranego słowa kluczowego w prognozowanej randze
488. [Tryby lochów i Kolei Refrakcji [combine_tooltip_desc2] — tekst] 선택한 키워드의 해당 등급 E.G.O 기프트가 현재 층의 선택지, 보스 클리어 시 등장하는 E.G.O 기프트에 이미 배정된 경우 (다음 층에서 획득 가능)
   źródło: MirrorDungeonUI_4.json :: dataList[id=combine_tooltip_desc2].content
   limit: do 260 znaków
   EN: When E.G.O Gifts of the selected Keyword category & the forecasted Tier have all been assigned to that Floor's Mirror Dungeon Events or Boss Encounter Reward pool (Can be obtained in the next Floor)
   PL: Gdy wszystkie Dary E.G.O wybranego słowa kluczowego w prognozowanej randze zostały już przypisane do wydarzeń lub nagród za bossa na bieżącym piętrze (dostępne od kolejnego piętra)
489. [Tryby lochów i Kolei Refrakcji [combine_tooltip_notice] — tekst] 예상 결과로 나올 수 있는 등급의 E.G.O 기프트를 전부 획득한 경우에는 합성을 진행할 수 없습니다.
   źródło: MirrorDungeonUI_4.json :: dataList[id=combine_tooltip_notice].content
   limit: do 130 znaków
   EN: You cannot continue with the Fusion if you have collected every E.G.O Gift in the forecasted Tier.
   PL: Gdy zdobyto już wszystkie Dary E.G.O prognozowanej rangi, przeprowadzenie Syntezy jest niemożliwe.

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_5
- plik gry: `MirrorDungeonUI_5.json`

490. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_get_ego_gift_with_enemy_buff_less_count] — tekst] E.G.O 기프트 선택 가능 횟수가 남았습니다.\n\nE.G.O 기프트를 선택하지 않고 이대로 진행하시겠습니까?\n\n(※ E.G.O 기프트를 선택하지 않을 경우, 남은 횟수만큼 무작위 고난을 획득합니다)
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_get_ego_gift_with_enemy_buff_less_count].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You have remaining E.G.O Gift choices.\n\nWill you proceed without selecting an E.G.O Gift?\n\n(※ You will gain random Trials equal to the number of your remaining choices)
   PL: Pozostały niewykorzystane wybory Darów E.G.O.\n\nKontynuować bez wyboru Daru E.G.O?\n\n(※ Pominięcie wyboru nałoży losowe Próby w liczbie równej pozostałym wyborom.)
491. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_easy_difficulty] — tekst] Normal
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_easy_difficulty].content
   limit: do 120 znaków
   EN: Normal
   PL: Normal
492. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_difficulty] — tekst] Hard
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_hard_difficulty].content
   limit: do 120 znaków
   EN: Hard
   PL: Hard
493. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_bonus_formation_rest_point] — tekst] 별빛 보너스
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_start_bonus_formation_rest_point].content
   limit: do 120 znaków
   EN: Starlight Bonus
   PL: Premia Gwiezdnego Blasku
494. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_bonus_formation_total] — tekst] 별빛\n보너스
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_start_bonus_formation_total].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starlight\nBonus
   PL: Premia\nBlasku
495. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_reset_selection] — tekst] 선택 효과 초기화
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_start_buff_Panel_reset_selection].content
   limit: do 120 znaków
   EN: Clear Effect Selection
   PL: Resetuj wybór efektów
496. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_applied_effect] — tekst] 적용한 효과
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_start_buff_Panel_applied_effect].content
   limit: do 120 znaków
   EN: Activated Effects
   PL: Wybrane efekty
497. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_reward_popup_rest_bonus_guide] — tekst] 편성하지 않은 인격의 별빛 보너스 1 증가
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_reward_popup_rest_bonus_guide].content
   limit: do 120 znaków
   EN: All Identities outside the current Team gain 1 Starlight Bonus
   PL: Premia Gwiezdnego Blasku niewystawionych Tożsamości wzrasta o 1
498. [Tryby lochów i Kolei Refrakcji [mirror_user_start_buff] — tekst] 별빛 보너스
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_user_start_buff].content
   (powtórzenie elementu 493 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Tryby lochów i Kolei Refrakcji [mirror_enemy_buff] — tekst] 고난
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_enemy_buff].content
   limit: do 120 znaków
   EN: Trials
   PL: Próby
500. [Tryby lochów i Kolei Refrakcji [mirror_enemy_addenemylevel_desc] — tekst] 적 레벨 증가 +{0}
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_enemy_addenemylevel_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy Level Up +{0}
   PL: Poziom wrogów +{0}
501. [Tryby lochów i Kolei Refrakcji [mirror_card_pack] — tekst] 테마팩
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_card_pack].content
   limit: do 120 znaków
   EN: Theme Pack
   PL: Pakiet Tematyczny
502. [Tryby lochów i Kolei Refrakcji [mirror_acquired_random_enemy_buff_popup_title] — tekst] 고난 추가
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_acquired_random_enemy_buff_popup_title].content
   limit: do 120 znaków
   EN: Trial Gained
   PL: Dodano Próbę
503. [Tryby lochów i Kolei Refrakcji [mirror_acquired_enemy_buff_popup_desc] — tekst] 고난이 추가되었습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_acquired_enemy_buff_popup_desc].content
   limit: do 120 znaków
   EN: A Trial has been added.
   PL: Dodano nową Próbę.
504. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_complete_modal_title] — tekst] 별의 가호 선택 완료
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_complete_modal_title].content
   limit: do 120 znaków
   EN: Grace of Stars Selected
   PL: Wybrano Błogosławieństwo Gwiazd
505. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_complete_modal_desc] — tekst] 별의 가호 선택을 완료하였습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_complete_modal_desc].content
   limit: do 120 znaków
   EN: Grace of Stars has been selected.
   PL: Zatwierdzono wybór Błogosławieństwa Gwiazd.
506. [Tryby lochów i Kolei Refrakcji [mirror_recovered_unit_status] — tekst] 사망한 아군이 부활하고 모든 아군이 회복되었습니다\n(부활불가 아군 제외)
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_recovered_unit_status].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All allies have been fully healed, and defeated allies have been revived\n(excluding unrevivable allies)
   PL: Wskrzeszono poległych sojuszników i uleczono całą drużynę\n(z wyjątkiem jednostek niepodlegających wskrzeszeniu)
507. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_cannot_purchase_side_popup_title] — tekst] 진행 불가
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_cannot_purchase_side_popup_title].content
   limit: do 120 znaków
   EN: Cannot Progress
   PL: Nie można kontynuować
508. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_cannot_purchase_side_popup_desc] — tekst] 별빛 보너스 부족
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_cannot_purchase_side_popup_desc].content
   limit: do 120 znaków
   EN: Not Enough Starlight Bonus
   PL: Za mało Premii Gwiezdnego Blasku
509. [Tryby lochów i Kolei Refrakcji [user_enemy_buff_empty_list] — tekst] 보유 중인 효과 없음
   źródło: MirrorDungeonUI_5.json :: dataList[id=user_enemy_buff_empty_list].content
   limit: do 120 znaków
   EN: No Active Effects
   PL: Brak aktywnych efektów
510. [Tryby lochów i Kolei Refrakcji [mirror_start_set_buff_type] — tekst] 별의 가호
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_set_buff_type].content
   limit: do 120 znaków
   EN: Grace of Stars
   PL: Błogosławieństwo Gwiazd
511. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_type] — tekst] 별무리의 은총
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_type].content
   limit: do 120 znaków
   EN: Grace of Star Clusters
   PL: Łaska Gromady Gwiazd
512. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_button] — tekst] 입장
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_button].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
513. [Tryby lochów i Kolei Refrakcji [user_enemy_buff_select_event_buff] — tekst] 선택지 효과
   źródło: MirrorDungeonUI_5.json :: dataList[id=user_enemy_buff_select_event_buff].content
   limit: do 120 znaków
   EN: Choice Effects
   PL: Efekty wydarzeń
514. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_desc_one_revive] — tekst] 선택한 수감자 부활
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_desc_one_revive].content
   limit: do 120 znaków
   EN: Revive Selected Sinner
   PL: Wskrześ wybranego Grzesznika
515. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_desc_all_revive] — tekst] 모든 수감자 부활
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_desc_all_revive].content
   limit: do 120 znaków
   EN: Revive All Sinners
   PL: Wskrześ wszystkich Grzeszników
516. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_mirror_hard_ab_battle] — tekst] 환상체 전투
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_encounter_guide_mirror_hard_ab_battle].content
   limit: do 120 znaków
   EN: Abnormality Encounter
   PL: Walka z Anomalią
517. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_enter] — tekst] 수감자를 회복시키거나 부활시킬 수 있다.\n어떻게 할까?
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_enter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We can heal or revive a Sinner here.\nWhat should we do?
   PL: Można tu uleczyć lub wskrzesić Grzeszników.\nCo robimy?
518. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_select_one] — tekst] {0} 수감자의 체력과 정신력이 회복되었다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_select_one].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: HP and SP healed for {0}.
   PL: Odnowiono PŻ i SP Grzesznika: {0}.
519. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_all] — tekst] 모든 수감자의 체력과 정신력이 회복되었다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_all].content
   limit: do 120 znaków
   EN: All Sinners' HP and SP have been healed.
   PL: Odnowiono PŻ i SP wszystkich Grzeszników.
520. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_revive_select_one] — tekst] {0} 수감자가 부활하여 전투에 복귀하였다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_revive_select_one].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}, revived, returns to battle.
   PL: {0} powstaje z martwych i wraca do walki.
521. [Tryby lochów i Kolei Refrakcji [mirrordungeon_revive_log] — tekst] 별의 가호 효과 발동\n[{0}] 수감자 부활
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_revive_log].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Grace of Stars Activated\n[{0}] Revived
   PL: Aktywowano Błogosławieństwo Gwiazd\nWskrzeszono Grzesznika [{0}]
522. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_unlock_condition_needs_held_buff_points] — tekst] 별빛 보너스 {0}이상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_unlock_condition_needs_held_buff_points].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: At {0}+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. {0}
523. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_after_selected_bonus] — tekst] 잔여 별빛 보너스
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_after_selected_bonus].content
   limit: do 120 znaków
   EN: Remaining Starlight Bonus
   PL: Pozostała Premia Gwiezdnego Blasku
524. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_exchanged_cost] — tekst] 코스트
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_exchanged_cost].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
525. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_title] — tekst] 별의 가호 선택
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_title].content
   limit: do 120 znaków
   EN: Select Grace of Stars
   PL: Wybór Błogosławieństwa Gwiazd
526. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_description] — tekst] 이 효과를 선택하시겠습니까?
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_description].content
   limit: do 120 znaków
   EN: Continue with selected effects?
   PL: Kontynuować z wybranymi efektami?
527. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_purchase_description] — tekst] 남은 별빛 보너스는 코스트로 전환됩니다
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_purchase_description].content
   limit: do 120 znaków
   EN: Remaining Starlight Bonus will be converted to Cost
   PL: Pozostała Premia Gwiezdnego Blasku zostanie zamieniona na Koszt
528. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_applied_passive] — tekst] 별의 가호 패시브
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_applied_passive].content
   limit: do 120 znaków
   EN: Grace of Stars Passive
   PL: Pasywka Błogosławieństwa Gwiazd
529. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_title] — tekst] 꿈결 별의 가호
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_start_buff_Panel_title].content
   limit: do 120 znaków
   EN: Grace of the Dreaming Star
   PL: Błogosławieństwo Śniącej Gwiazdy
530. [Tryby lochów i Kolei Refrakcji [mirror_shop_purchase_complete] — tekst] 구매 완료
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_shop_purchase_complete].content
   limit: do 120 znaków
   EN: Purchased
   PL: Zakupiono
531. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_not_selected_any_buff] — tekst] 선택하지 않음
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_purchase_modal_not_selected_any_buff].content
   limit: do 120 znaków
   EN: None Selected
   PL: Brak wyboru
532. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_title_all_season5] — tekst] 모든 수감자를 조금씩 회복시킨다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_title_all_season5].content
   limit: do 120 znaków
   EN: Moderately heal every Sinner.
   PL: Ulecz po trochu wszystkich Grzeszników.
533. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_title_one_season5] — tekst] 수감자 한 명을 크게 회복시킨다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_heal_title_one_season5].content
   limit: do 120 znaków
   EN: Greatly heal a single Sinner.
   PL: Znacząco ulecz jednego Grzesznika.
534. [Tryby lochów i Kolei Refrakcji [dungeon_shop_revive_title_one_season5] — tekst] 수감자 한 명을 부활시킨다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_revive_title_one_season5].content
   limit: do 120 znaków
   EN: Revive a single Sinner.
   PL: Wskrześ jednego Grzesznika.
535. [Tryby lochów i Kolei Refrakcji [dungeon_shop_revive_one_select_ask] — tekst] 부활시킬 수감자를 선택하세요
   źródło: MirrorDungeonUI_5.json :: dataList[id=dungeon_shop_revive_one_select_ask].content
   limit: do 120 znaków
   EN: Select the Sinner to revive.
   PL: Wybierz Grzesznika do wskrzeszenia.
536. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_block_to_click_hard_theme_list] — tekst] 주요 이야기 8장\n클리어 시 개방됩니다
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_block_to_click_hard_theme_list].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clear Canto 8\nto Unlock
   PL: Odblokowanie po ukończeniu\nCanto VIII
537. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_blocked] — tekst] 주요 이야기 8장\n클리어 시 개방됩니다
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_theme_hard_blocked].content
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_title] — tekst] 수감자 회복
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_shop_heal_title].content
   limit: do 120 znaków
   EN: Heal Sinners
   PL: Leczenie Grzeszników
539. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_title] — tekst] 상점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_shop_title].content
   limit: do 120 znaków
   EN: Shop
   PL: Sklep
540. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_5] — tekst] 꿈결의 거울 {0}층
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_progress_text_5].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mirror of the Dreaming - F{0}
   PL: Lustro Snu — {0}. piętro
541. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_awaiting_reward_claim] — tekst] 보상 수령 대기 중
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_progress_awaiting_reward_claim].content
   limit: do 120 znaków
   EN: Unclaimed Rewards
   PL: Oczekiwanie na odbiór nagród
542. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_bonus_gift] — tekst] 별의 가호 효과 발동\n합성·판매용 기프트 획득
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_bonus_gift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Grace of Stars Activated\nFor Fusion & Sale Gifts obtained
   PL: Aktywowano Błogosławieństwo Gwiazd\nZdobyto Dar do Syntezy/Sprzedaży
543. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_0_1] — tekst] NORMAL 난이도
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_0_1].content
   limit: do 120 znaków
   EN: NORMAL
   PL: NORMAL
544. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_0_2] — tekst] HARD 난이도
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_0_2].content
   limit: do 120 znaków
   EN: HARD
   PL: HARD
545. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_1_1] — tekst] 일반 전투 : 7.5%\n집중 전투 : -\n정예 전투 : -\n환상체 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_1_1].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 7.5%\nFocused Encounter : -\nElite Encounter : -\nAbno. Encounter: -\nBoss Encounter : 100%
   PL: Zwykłe starcie: 7,5%\nStarcie skupione: -\nStarcie elitarne: -\nWalka z Anomalią: -\nWalka z bossem: 100%
546. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_1_2] — tekst] 일반 전투 : 7.5%\n집중 전투 : -\n정예 전투 : -\n환상체 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_1_2].content
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
547. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_2_1] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n환상체 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_2_1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 10%\nFocused Encounter : 20%\nElite Encounter : 33%\nAbno. Encounter: -\nBoss Encounter : 100%
   PL: Zwykłe starcie: 10%\nStarcie skupione: 20%\nStarcie elitarne: 33%\nWalka z Anomalią: -\nWalka z bossem: 100%
548. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_2_2] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n환상체 전투 : -\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_2_2].content
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
549. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_3_1] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n환상체 전투 : 100%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_3_1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 10%\nFocused Encounter : 20%\nElite Encounter : 33%\nAbno. Encounter: 100%\nBoss Encounter : 100%
   PL: Zwykłe starcie: 10%\nStarcie skupione: 20%\nStarcie elitarne: 33%\nWalka z Anomalią: 100%\nWalka z bossem: 100%
550. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_3_2] — tekst] 일반 전투 : 10%\n집중 전투 : 20%\n정예 전투 : 33%\n환상체 전투 : 100%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_3_2].content
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_4_1] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n환상체 전투 : 100%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_4_1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 12.5%\nFocused Encounter : 25%\nElite Encounter : 50%\nAbno. Encounter: 100%\nBoss Encounter : 100%
   PL: Zwykłe starcie: 12,5%\nStarcie skupione: 25%\nStarcie elitarne: 50%\nWalka z Anomalią: 100%\nWalka z bossem: 100%
552. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_4_2] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n환상체 전투 : 100%\n보스 전투 : 100%
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_4_2].content
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_5_1] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n환상체 전투 : 100%\n보스 전투 : -
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_5_1].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Regular Encounter : 12.5%\nFocused Encounter : 25%\nElite Encounter : 50%\nAbno. Encounter: 100%\nBoss Encounter : -
   PL: Zwykłe starcie: 12,5%\nStarcie skupione: 25%\nStarcie elitarne: 50%\nWalka z Anomalią: 100%\nWalka z bossem: -
554. [Tryby lochów i Kolei Refrakcji [mirror_5_battle_reward_card_guide_table_1_desc_5_2] — tekst] 일반 전투 : 12.5%\n집중 전투 : 25%\n정예 전투 : 50%\n환상체 전투 : 100%\n보스 전투 : -
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_5_battle_reward_card_guide_table_1_desc_5_2].content
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Tryby lochów i Kolei Refrakcji [mirrordungeon_additional_cost_by_start_bonus] — tekst] 별의 가호 효과 발동\n코스트 획득
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_additional_cost_by_start_bonus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Grace of Stars Activated\nCost gained
   PL: Aktywowano Błogosławieństwo Gwiazd\nZdobyto Koszt
556. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_desc] — tekst] E.G.O 기프트의 등급에 따라, 합성 재료로 사용될 때의 점수는 다음과 같습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_desc].content
   limit: do 120 znaków
   EN: Each E.G.O Gift has varying 'Points' for Fusion depending on their Tier.
   PL: W zależności od rangi Daru E.G.O jego wartość punktowa jako składnika Syntezy wynosi:
557. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_header] — tekst] E.G.O 기프트 등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_header].content
   limit: do 120 znaków
   EN: E.G.O Gift Tiers
   PL: Ranga Daru E.G.O
558. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_score_header] — tekst] 점수
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_score_header].content
   limit: do 120 znaków
   EN: Points
   PL: Punkty
559. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_1] — tekst] 1등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_1].content
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_1_score] — tekst] 3
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_1_score].content
   limit: do 120 znaków
   EN: 3
   PL: 3
561. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_2] — tekst] 2등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_2].content
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_2_score] — tekst] 6
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_2_score].content
   limit: do 120 znaków
   EN: 6
   PL: 6
563. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_3] — tekst] 3등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_3].content
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_3_score] — tekst] 10
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_3_score].content
   limit: do 120 znaków
   EN: 10
   PL: 10
565. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_4] — tekst] 4등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_4].content
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_4_score] — tekst] 15
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_4_score].content
   limit: do 120 znaków
   EN: 15
   PL: 15
567. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_5] — tekst] 5등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_5].content
   limit: do 120 znaków
   EN: Tier 5
   PL: Ranga 5
568. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_score_tier_5_score] — tekst] 30
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_score_tier_5_score].content
   limit: do 120 znaków
   EN: 30
   PL: 30
569. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_label] — tekst] 합성 시, 합성 재료 점수의 총합에 따라 만들어지는 E.G.O 기프트의 등급이 다음과 같이 결정됩니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_label].content
   limit: do 120 znaków
   EN: The Fusion E.G.O Gift Tier is determined by the tally of Points from each ingredient.
   PL: Podczas Syntezy ranga powstającego Daru E.G.O zależy od sumy punktów składników:
570. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_header] — tekst] 점수 총합
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_header].content
   limit: do 120 znaków
   EN: Point Tally
   PL: Suma punktów
571. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_tier_header] — tekst] 합성 E.G.O 기프트 등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_tier_header].content
   limit: do 120 znaków
   EN: Fusion E.G.O Gift Tier
   PL: Ranga Daru z Syntezy
572. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_1] — tekst] 10점 이하
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_1].content
   limit: do 120 znaków
   EN: 10- Points
   PL: Maks. 10 pkt
573. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_tier_1] — tekst] 1등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_tier_1].content
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_2] — tekst] 11 ~ 16점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_2].content
   limit: do 120 znaków
   EN: 11~16 Points
   PL: 11 ~ 16 pkt
575. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_tier_2] — tekst] 2등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_tier_2].content
   (powtórzenie elementu 459 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_3] — tekst] 17 ~ 24점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_3].content
   limit: do 120 znaków
   EN: 17 ~ 24 Points
   PL: 17 ~ 24 pkt
577. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_tier_3] — tekst] 3등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_tier_3].content
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_4] — tekst] 25점 이상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_4].content
   limit: do 120 znaków
   EN: 25+ Points
   PL: Min. 25 pkt
579. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_tier_4] — tekst] 4등급
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_tier_4].content
   (powtórzenie elementu 461 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_season_5_etc_1] — tekst] ※ 현재 보유 중인 E.G.O 기프트는 합성을 통해 얻을 수 있는 E.G.O 기프트에서 제외됩니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_season_5_etc_1].content
   limit: do 120 znaków
   EN: ※ Any E.G.O Gifts currently in your possession cannot be obtained as a Fusion result.
   PL: ※ Aktualnie posiadane Dary E.G.O są wykluczone z puli wyników Syntezy.
581. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_season_5_etc_2] — tekst] ※ 합성의 재료로 사용된 E.G.O 기프트는 해당 합성의 결과물로 등장하지 않습니다. 단, 이전에 재료로 사용한 E.G.O 기프트는 합성의 결과물로 등장할 수 있습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_season_5_etc_2].content
   limit: do 270 znaków
   EN: ※ E.G.O Gifts consumed as ingredients for a Fusion cannot be obtained from that Fusion. However, E.G.O Gifts that have already been consumed as ingredients in previous Fusions can be obtained as a Fusion result.
   PL: ※ Dary E.G.O użyte jako składniki danej Syntezy nie mogą pojawić się jako jej bezpośredni wynik (mogą jednak pojawić się ponownie w kolejnych Syntezach).
582. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_season_5_etc_3] — tekst] ※ 특정 등급의 특정 키워드에 해당하는 E.G.O 기프트를 추가로 얻을 수 없는 경우에는 동일한 등급의 다른 키워드 E.G.O 기프트를 획득합니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_season_5_etc_3].content
   limit: do 230 znaków
   EN: ※ If you have obtained every possible E.G.O Gift obtainable in that specific Tier + Keyword combination, you will receive an E.G.O Gift of a different Keyword in the same Tier.
   PL: ※ Jeśli nie można już zdobyć kolejnych Darów E.G.O danej rangi i słowa kluczowego, otrzymasz Dar E.G.O tej samej rangi z innym słowem kluczowym.
583. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_season_5_etc_4] — tekst] ※ 특정 등급에 해당하는 E.G.O 기프트를 추가로 얻을 수 없는 경우에는 동일한 등급의 합성 · 판매용 E.G.O 기프트를 획득합니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_season_5_etc_4].content
   limit: do 180 znaków
   EN: ※ If you have obtained every possible E.G.O Gift obtainable from the resultant Tier, you will receive a Fusion & Sale Only E.G.O Gift.
   PL: ※ Jeśli nie można już zdobyć żadnych zwykłych Darów E.G.O danej rangi, otrzymasz Dar E.G.O do Syntezy/Sprzedaży tej samej rangi.
584. [Tryby lochów i Kolei Refrakcji [mirrordungeon_upgrade_shop_title] — tekst] <color=#990000>특별한 상점</color>
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_upgrade_shop_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>
   EN: <color=#990000>Super Shop</color>
   PL: <color=#990000>Wzmocniony Sklep</color>
585. [Tryby lochów i Kolei Refrakcji [mirrordungeon_upgrade_shop_rate_in_next_floor] — tekst] 다음 층에서\n특별한 상점 등장 확률
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_upgrade_shop_rate_in_next_floor].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Super Shop\nOn Next Floor?
   PL: Szansa na Wzmocniony Sklep\nna następnym piętrze
586. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_unlock_condition_lack_of_current_point] — tekst] 별빛 보너스 부족
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_start_buff_unlock_condition_lack_of_current_point].content
   (powtórzenie elementu 508 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Tryby lochów i Kolei Refrakcji [mirror_theme_pack_baton] — tekst] 장기 전투
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_theme_pack_baton].content
   limit: do 120 znaków
   EN: Long Battle
   PL: Długa walka
588. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_no_pool] — tekst] Hard 난이도 개방 조건을 달성하였습니다. 다음 층 테마팩 선택 창부터 난이도를 전환할 수 있습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_theme_hard_no_pool].content
   limit: do 170 znaków
   EN: You now meet the conditions to unlock the Hard difficulty. You can switch difficulties starting from next Floor Theme Pack menu.
   PL: Spełniono warunki odblokowania poziomu Hard. Możesz przełączyć trudność od następnego ekranu wyboru Pakietu Tematycznego.
589. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_3_0] — tekst] 4개 이상
   źródło: MirrorDungeonUI_5.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_3_0].content
   limit: do 120 znaków
   EN: 4+ Gifts
   PL: Min. 4 szt.
590. [Tryby lochów i Kolei Refrakcji [new_ego_gift_combine_guide_table_1_desc_3_1] — tekst] 99%
   źródło: MirrorDungeonUI_5.json :: dataList[id=new_ego_gift_combine_guide_table_1_desc_3_1].content
   limit: do 120 znaków
   EN: 99%
   PL: 99%
591. [Tryby lochów i Kolei Refrakcji [mirrordungeon_level_up_by_long_battle_theme] — tekst] 장기 전투 보상 획득\n인격 레벨 +3
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_level_up_by_long_battle_theme].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Long Battle Reward Gained\nIdentity Levels +3
   PL: Nagroda za długą walkę\nPoziom Tożsamości +3
592. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_100] — tekst] 시작의 별
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_100].content
   limit: do 120 znaków
   EN: Star of the Beginning
   PL: Gwiazda Początku
593. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_101] — tekst] 쌓여가는 별무리
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_101].content
   limit: do 120 znaków
   EN: Cumulating Starcloud
   PL: Gęstniejąca Gromada Gwiazd
594. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_102] — tekst] 성간여행
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_102].content
   limit: do 120 znaków
   EN: Interstellar Travel
   PL: Podróż Międzygwiezdna
595. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_103] — tekst] 쏟아지는 유성우
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_103].content
   limit: do 120 znaków
   EN: Star-shower
   PL: Deszcz Meteorów
596. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_104] — tekst] 쌍성계 상점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_104].content
   limit: do 120 znaków
   EN: Binary Star-shop
   PL: Sklep Układu Podwójnego
597. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_105] — tekst] 위성계 상점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_105].content
   limit: do 120 znaków
   EN: Moon Star-shop
   PL: Sklep Układu Księżycowego
598. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_106] — tekst] 성운의 총애
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_106].content
   limit: do 120 znaków
   EN: Favor of the Nebulae
   PL: Łaska Mgławicy
599. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_107] — tekst] 별빛의 인도
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_107].content
   limit: do 120 znaków
   EN: Starlight Guidance
   PL: Przewodnictwo Gwiezdnego Blasku
600. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_108] — tekst] 우연한 혜성
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_108].content
   limit: do 120 znaków
   EN: Chance Comet
   PL: Przypadkowa Kometa
601. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_title_109] — tekst] 완전한 가능성
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_title_109].content
   limit: do 120 znaków
   EN: Perfected Possibility
   PL: Doskonała Możliwość
602. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_over10] — tekst] 별빛 보너스 [10] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_over10].content
   limit: do 120 znaków
   EN: At [10]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [10]
603. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_over20] — tekst] 별빛 보너스 [20] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_over20].content
   limit: do 120 znaków
   EN: At [20]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [20]
604. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_over30] — tekst] 별빛 보너스 [30] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_over30].content
   limit: do 120 znaków
   EN: At [30]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [30]
605. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs_over40] — tekst] 별빛 보너스 [40] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs_over40].content
   limit: do 120 znaków
   EN: At [40]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [40]
606. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs__over50] — tekst] 별빛 보너스 [50] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs__over50].content
   limit: do 120 znaków
   EN: At [50]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [50]
607. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_5_buffs__over60] — tekst] 별빛 보너스 [60] 이상 보유
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_5_buffs__over60].content
   limit: do 120 znaków
   EN: At [60]+ Starlight Bonus
   PL: Premia Gwiezdnego Blasku min. [60]
608. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_label_upgrade] — tekst] 특별한 상점에서 합성을 진행하는 경우에는 점수 총합에 보정치가 적용됩니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_label_upgrade].content
   limit: do 140 znaków
   EN: Fusing in a Super Shop adds a special modifier to the required tally of the Points from each ingredient.
   PL: Podczas Syntezy we Wzmocnionym Sklepie wymagane progi punktowe ulegają obniżeniu:
609. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_1_upgrade] — tekst] 9점 이하
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_1_upgrade].content
   limit: do 120 znaków
   EN: 9- Points
   PL: Maks. 9 pkt
610. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_2_upgrade] — tekst] 10 ~ 14점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_2_upgrade].content
   limit: do 120 znaków
   EN: 10 ~ 14 Points
   PL: 10 ~ 14 pkt
611. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_3_upgrade] — tekst] 15 ~ 21점
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_3_upgrade].content
   limit: do 120 znaków
   EN: 15 ~ 21 Points
   PL: 15 ~ 21 pkt
612. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_combine_guide_result_total_4_upgrade] — tekst] 22점 이상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_egogift_combine_guide_result_total_4_upgrade].content
   limit: do 120 znaków
   EN: 22+ Points
   PL: Min. 22 pkt
613. [Tryby lochów i Kolei Refrakcji [mirrordungeon_start_bonus_personality_title] — tekst] 별빛 보너스 보존 대상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_start_bonus_personality_title].content
   limit: do 120 znaków
   EN: Starlight Bonus Retention Units
   PL: Jednostki zachowujące Premię Blasku
614. [Tryby lochów i Kolei Refrakcji [mirrordungeon_start_bonus_personality_desc] — tekst] 별빛 보너스 보존 기간 동안 해당 인격으로 거울 던전 클리어 시 별빛 보너스가 소모되지 않습니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_start_bonus_personality_desc].content
   limit: do 150 znaków
   EN: For the retention duration, these units' Starlight Bonuses will not be spent upon clearing a Mirror Dungeon run.
   PL: W okresie zachowania Premii ukończenie Lustrzanego Lochu tymi Tożsamościami nie zużywa ich Premii Gwiezdnego Blasku.
615. [Tryby lochów i Kolei Refrakcji [mirrordungeon_start_bonus_personality_label] — tekst] 적용 대상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_start_bonus_personality_label].content
   limit: do 120 znaków
   EN: Affected Units
   PL: Objęte Tożsamości
616. [Tryby lochów i Kolei Refrakcji [mirrordungeon_start_bonus_personality_button_label] — tekst] 별빛 보너스 보존 대상
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_start_bonus_personality_button_label].content
   (powtórzenie elementu 613 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Tryby lochów i Kolei Refrakcji [mirrordungeon_start_bonus_personality_period] — tekst] {0}까지
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_start_bonus_personality_period].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Until {0}
   PL: Do {0}
618. [Tryby lochów i Kolei Refrakcji [mirrordungeon_purchase_achievement_level_using_lunacy_desc] — tekst] ※ 투영도 {0} 구매 시, 유료 광기 {1} 소모
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_purchase_achievement_level_using_lunacy_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: ※ Purchasing {0} Projection Rate costs {1} Paid Lunacy.
   PL: ※ Zakup {0} pkt Stopnia Projekcji kosztuje {1} Płatnego Szaleństwa
619. [Tryby lochów i Kolei Refrakcji [mirrordungeon_purchase_achievement_level_ask_using_lunacy] — tekst] 유료 광기 {0}개를 소모하여 투영도를 구매하시겠습니까?
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_purchase_achievement_level_ask_using_lunacy].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Spend {0} Paid Lunacy to purchase Projection Rate?
   PL: Wydać {0} Płatnego Szaleństwa, aby kupić Stopień Projekcji?
620. [Tryby lochów i Kolei Refrakcji [mirrordungeon_purchase_achievement_title] — tekst] 투영도 구매
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_purchase_achievement_title].content
   limit: do 120 znaków
   EN: Purchase Projection Rate
   PL: Zakup Stopnia Projekcji
621. [Tryby lochów i Kolei Refrakcji [mirrordungeon_achievement_progress] — tekst] 업적 진행도
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_achievement_progress].content
   limit: do 120 znaków
   EN: Progress
   PL: Postęp osiągnięć
622. [Tryby lochów i Kolei Refrakcji [mirrordungeon_purchase_achievement_block_by_max_level] — tekst] 구매 가능한 패스 레벨 초과
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_purchase_achievement_block_by_max_level].content
   limit: do 120 znaków
   EN: Exceeded purchasable Pass Level
   PL: Przekroczono maksymalny poziom do zakupu
623. [Tryby lochów i Kolei Refrakcji [mirrordungeon_achievement_max_level] — tekst] 패스 레벨 최대 달성
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirrordungeon_achievement_max_level].content
   limit: do 120 znaków
   EN: Pass Level maxed out
   PL: Osiągnięto maksymalny poziom
624. [Tryby lochów i Kolei Refrakcji [lack_of_point_for_shop_without_new_line] — tekst] 코스트 부족
   źródło: MirrorDungeonUI_5.json :: dataList[id=lack_of_point_for_shop_without_new_line].content
   limit: do 120 znaków
   EN: Not Enough Cost
   PL: Za mało Kosztu
625. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_give_up_ego_gift_ask_with_random_category] — tekst] E.G.O 기프트를 선택하지 않고 진행하시겠습니까?\n\n진행할 경우 시작 E.G.O 기프트의 키워드는\n무작위로 선택됩니다.
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_give_up_ego_gift_ask_with_random_category].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Continue without selecting an E.G.O Gift?\n\nIf you continue without selecting an E.G.O Gift,\nthe Keywords of your Starting E.G.O Gift will be\nselected at random.
   PL: Kontynuować bez wyboru Daru E.G.O?\n\nW takim przypadku słowo kluczowe początkowego Daru E.G.O\nzostanie wybrane losowo.
626. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_block_to_click_extream_theme_list] — tekst] 주요 이야기 8장\n클리어 시 개방됩니다
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_block_to_click_extream_theme_list].content
   (powtórzenie elementu 536 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_extream_difficulty] — tekst] EXTREME
   źródło: MirrorDungeonUI_5.json :: dataList[id=mirror_dungeon_extream_difficulty].content
   limit: do 120 znaków
   EN: EXTREME
   PL: EXTREME

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_5_InfinityFloor
- plik gry: `MirrorDungeonUI_5_InfinityFloor.json`

628. [Tryby lochów i Kolei Refrakcji [InfinityFloor_CheckEnter_Modal_Title] — tekst] 평행중첩 모드
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=InfinityFloor_CheckEnter_Modal_Title].content
   limit: do 120 znaków
   EN: Parallel Superposition Mode
   PL: Tryb Superpozycji Równoległej
629. [Tryby lochów i Kolei Refrakcji [InfinityFloor_CheckEnter_Modal_Desc] — tekst] 평행중첩 모드를 적용할 수 있습니다.\n\n평행중첩 모드를 적용하여 다음 층으로 이동하시겠습니까?
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=InfinityFloor_CheckEnter_Modal_Desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can enter the Parallel Superposition Mode.\n\nEnter the Parallel Superposition Mode and proceed to the next floor?
   PL: Możesz aktywować Tryb Superpozycji Równoległej.\n\nWłączyć go i przejść na następne piętro?
630. [Tryby lochów i Kolei Refrakcji [InfinityFloor_Mode_Button_Title] — tekst] 평행중첩 모드 :
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=InfinityFloor_Mode_Button_Title].content
   limit: do 120 znaków
   EN: Parallel Superposition Mode :
   PL: Tryb Superpozycji Równoległej:
631. [Tryby lochów i Kolei Refrakcji [InfinityFloor_Mode_Button_Title_forProgressPopup] — tekst] 평행중첩
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=InfinityFloor_Mode_Button_Title_forProgressPopup].content
   limit: do 120 znaków
   EN: Parallel S.
   PL: Superpozycja
632. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_infinity_difficulty] — tekst] infinity
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirror_dungeon_infinity_difficulty].content
   limit: do 120 znaków
   EN: infinity
   PL: infinity
633. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_achievement_panel_title] — tekst] 거울 투영 / 업적
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirror_dungeon_achievement_panel_title].content
   limit: do 120 znaków
   EN: Mirror Projection / Achievements
   PL: Projekcja Lustra / Osiągnięcia
634. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_achievement_reward_title] — tekst] 투영도 보상
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirror_dungeon_achievement_reward_title].content
   limit: do 120 znaków
   EN: Projection Rewards
   PL: Nagrody Projekcji
635. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_achievement_list_title] — tekst] 업적
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirror_dungeon_achievement_list_title].content
   limit: do 120 znaków
   EN: Achievements
   PL: Osiągnięcia
636. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_COLLECTION] — tekst] 수집
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_COLLECTION].content
   limit: do 120 znaków
   EN: Collection
   PL: Kolekcja
