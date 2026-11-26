# Paczka AI P34 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 5/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P34_2b_przedmioty_sklep_wydarzenia_cz05.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P34_2b_przedmioty_sklep_wydarzenia_cz05.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Wydarzenia i Przepustka: LimtochessUI
- plik gry: `LimtochessUI.json`

1. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_reroll_segment] — tekst] 새로고침 기회
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_reroll_segment].content
   limit: do 120 znaków
   EN: Reshuffles
   PL: Szanse na odnowienie
2. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_sync_pick] — tekst] 동기화 상승 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_sync_pick].content
   limit: do 120 znaków
   EN: Choose Identity to Uptie
   PL: Wybierz Tożsamość do synchronizacji
3. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_sync_random] — tekst] 무작위 동기화 상승
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_sync_random].content
   limit: do 120 znaków
   EN: Uptie Random Identity
   PL: Synchronizacja losowej Tożsamości
4. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_recruit_pick] — tekst] 인격 영입
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_recruit_pick].content
   limit: do 120 znaków
   EN: Recruit Identity
   PL: Werbunek Tożsamości
5. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_pack_random] — tekst] 무작위 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_pack_random].content
   limit: do 120 znaków
   EN: Obtain a random Pack
   PL: Zdobądź losowy Pakiet
6. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_pack_keyword] — tekst] 키워드 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_pack_keyword].content
   limit: do 120 znaków
   EN: Obtain Keyword Pack
   PL: Zdobądź Pakiet Słowa Kluczowego
7. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_ego_pick] — tekst] E.G.O 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_ego_pick].content
   limit: do 120 znaków
   EN: Equip E.G.O
   PL: Wyposaż E.G.O
8. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_ego_keyword] — tekst] 키워드 E.G.O 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_ego_keyword].content
   limit: do 120 znaków
   EN: Equip Keyword E.G.O
   PL: Wyposaż E.G.O Słowa Kluczowego
9. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_reroll_to_generic] — tekst] 범용 조각 환산
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_reroll_to_generic].content
   limit: do 120 znaków
   EN: Convert to Universal Slivers
   PL: Zamień na Okruchy Uniwersalne
10. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_affiliation_random] — tekst] 같은 소속 무작위 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_affiliation_random].content
   limit: do 120 znaków
   EN: Random Same-faction Swap
   PL: Losowa wymiana w tej samej Przynależności
11. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_affiliation_pick] — tekst] 같은 소속 선택 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_affiliation_pick].content
   limit: do 120 znaków
   EN: Choose Same-faction Swap
   PL: Wybrana wymiana w tej samej Przynależności
12. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_pick] — tekst] 인격 교체 영입
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_pick].content
   limit: do 120 znaków
   EN: Recruit and Replace Identity
   PL: Werbunek i wymiana Tożsamości
13. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_all] — tekst] 편성 전원 변경
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_all].content
   limit: do 120 znaków
   EN: Change Entire Team
   PL: Zmień cały skład
14. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_one] — tekst] 인격 1명 변경
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_one].content
   limit: do 120 znaków
   EN: Change 1 Identity
   PL: Zmień 1 Tożsamość
15. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_pack_grade_open] — tekst] 등급 팩 개봉
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_pack_grade_open].content
   limit: do 120 znaków
   EN: Open Grade Pack
   PL: Otwórz Pakiet rangi
16. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_cost_up_pick] — tekst] 코스트 +1 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_cost_up_pick].content
   limit: do 120 znaków
   EN: Cost +1 Swap
   PL: Wymiana Koszt +1
17. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_swap_one_pick] — tekst] 고른 인격 1명 변경
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_swap_one_pick].content
   limit: do 120 znaków
   EN: Change 1 Selected Identity
   PL: Zmień 1 wybraną Tożsamość
18. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_final_boss] — tekst] 최종 보스 변경
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_final_boss].content
   limit: do 120 znaków
   EN: Change Final Boss
   PL: Zmień Bossa Finałowego
19. [Wydarzenia i Przepustka [limtochess_roominfo_effect_name_stage_unlock] — tekst] 보스 선택지 해금
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_name_stage_unlock].content
   limit: do 120 znaków
   EN: Unlock Boss Option
   PL: Odblokuj Opcję Bossa
20. [Wydarzenia i Przepustka [limtochess_packtip_deck_match] — tekst] 현재 편성 중인 {1} 인격 {0}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_deck_match].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: {0} {1} Identities in Team
   PL: {1} — {0} Tożsamości w składzie
21. [Wydarzenia i Przepustka [limtochess_packtip_guarantee_head] — tekst] {1} 카드 최소 {0}장 확정
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_guarantee_head].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: {0} Guaranteed {1} Card(s)
   PL: {0} gwarantowanych kart {1}
22. [Wydarzenia i Przepustka [limtochess_packtip_chance_head] — tekst] 확률
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_chance_head].content
   limit: do 120 znaków
   EN: Odds
   PL: Szansa
23. [Wydarzenia i Przepustka [limtochess_packtip_identity] — tekst] 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_identity].content
   limit: do 120 znaków
   EN: Identity
   PL: Tożsamości
24. [Wydarzenia i Przepustka [limtochess_packtip_ego] — tekst] E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_ego].content
   limit: do 120 znaków
   EN: E.G.O
   PL: E.G.O
25. [Wydarzenia i Przepustka [limtochess_packtip_keep] — tekst] 선택\n가능
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_keep].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Avail.
   PL: Wybór\nmożliwy
26. [Wydarzenia i Przepustka [limtochess_gauge_cycle_state_extended] — tekst] 공통주기 연장중
   źródło: LimtochessUI.json :: dataList[id=limtochess_gauge_cycle_state_extended].content
   limit: do 120 znaków
   EN: Shared Cycle Extended
   PL: Tury wspólne wydłużone
27. [Wydarzenia i Przepustka [limtochess_option_retry_left] — tekst] 남은 횟수 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_option_retry_left].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Retries Remaining: {0}
   PL: Pozostałe ponowienia: {0}
28. [Wydarzenia i Przepustka [limtochess_roominfo_list_merit] — tekst] 승리 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_merit].content
   limit: do 120 znaków
   EN: Victory Rewards
   PL: Nagrody za zwycięstwo
29. [Wydarzenia i Przepustka [limtochess_roominfo_merit_pack] — tekst] 팩 {0}개 중 1개 개봉
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_merit_pack].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Open 1 of {0} Packs
   PL: Otwórz 1 z {0} Pakietów
30. [Wydarzenia i Przepustka [limtochess_roominfo_merit_reroll] — tekst] 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_merit_reroll].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reshuffles +{0}
   PL: Odświeżenia +{0}
31. [Wydarzenia i Przepustka [limtochess_roominfo_merit_elite] — tekst] 정예 보상 1개 선택 (인격 및 E.G.O 교체·편성·동기화)
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_merit_elite].content
   limit: do 120 znaków
   EN: Choose 1 Elite Reward (Identity/E.G.O Swap, Formation, or Uptie)
   PL: Wybierz 1 nagrodę elit (Wymiana Tożsamości/E.G.O, Skład albo Synchronizacja)
32. [Wydarzenia i Przepustka [limtochess_roominfo_merit_level] — tekst] 인격 레벨 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_merit_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Identity Level +{0}
   PL: Poziom Tożsamości +{0}
33. [Wydarzenia i Przepustka [limtochess_ego_choice_title] — tekst] {0} {1} E.G.O 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Select {1} {0} E.G.O
   PL: {0} {1} E.G.O — wybór
34. [Wydarzenia i Przepustka [limtochess_ego_choice_desc] — tekst] {0}의 {1} 칸에는 E.G.O를 1개만 장착할 수 있습니다. 장착할 E.G.O를 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Only 1 E.G.O can be equipped in {0}'s {1} slot. Select the E.G.O to equip.
   PL: W gnieździe {1} jednostki {0} można wyposażyć tylko 1 E.G.O. Wybierz E.G.O do wyposażenia.
35. [Wydarzenia i Przepustka [limtochess_ego_choice_warning] — tekst] 고르지 않은 E.G.O는 사라집니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_warning].content
   limit: do 120 znaków
   EN: Unselected E.G.O will be lost.
   PL: Niewybrane E.G.O przepadnie.
36. [Wydarzenia i Przepustka [limtochess_ego_choice_current] — tekst] 기존 E.G.O · {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_current].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Current E.G.O · Tier {0}
   PL: Obecne E.G.O · Stopień {0}
37. [Wydarzenia i Przepustka [limtochess_ego_choice_new] — tekst] 신규 E.G.O · {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_new].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New E.G.O · Tier {0}
   PL: Nowe E.G.O · Stopień {0}
38. [Wydarzenia i Przepustka [limtochess_ego_choice_confirm] — tekst] 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_confirm].content
   limit: do 120 znaków
   EN: Equip
   PL: Wyposaż
39. [Wydarzenia i Przepustka [limtochess_ego_choice_back] — tekst] 뒤로
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_choice_back].content
   limit: do 120 znaków
   EN: Back
   PL: Wstecz
40. [Wydarzenia i Przepustka [limtochess_packselect_summary_ego_keep] — tekst] {0} E.G.O 보관
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_ego_keep].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Store {0} E.G.O
   PL: Schowaj {0} E.G.O
41. [Wydarzenia i Przepustka [limtochess_packselect_ego_same_grade] — tekst] {0}의 {1} E.G.O를 {2}장 골랐습니다. 확정 시 1장만 장착합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_ego_same_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: You have selected {2} {1} E.G.O for {0}. Only one copy will be equipped upon confirmation.
   PL: Wybrano {2} E.G.O ({1}) dla {0}. Po potwierdzeniu wyposażysz tylko 1.
42. [Wydarzenia i Przepustka [limtochess_band_ready_buff_turn] — tekst] TURN {0}부터
   źródło: LimtochessUI.json :: dataList[id=limtochess_band_ready_buff_turn].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: From TURN {0}
   PL: Od TURN {0}
43. [Wydarzenia i Przepustka [limtochess_roominfo_choice_1] — tekst] 선택지 1
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_1].content
   limit: do 120 znaków
   EN: Option 1
   PL: Opcja 1
44. [Wydarzenia i Przepustka [limtochess_roominfo_choice_2] — tekst] 선택지 2
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_2].content
   limit: do 120 znaków
   EN: Option 2
   PL: Opcja 2
45. [Wydarzenia i Przepustka [limtochess_roominfo_choice_3] — tekst] 선택지 3
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_3].content
   limit: do 120 znaków
   EN: Option 3
   PL: Opcja 3
46. [Wydarzenia i Przepustka [limtochess_roominfo_choice_4] — tekst] 선택지 4
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_4].content
   limit: do 120 znaków
   EN: Option 4
   PL: Opcja 4
47. [Wydarzenia i Przepustka [limtochess_roominfo_choice_5] — tekst] 선택지 5
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_5].content
   limit: do 120 znaków
   EN: Option 5
   PL: Opcja 5
48. [Wydarzenia i Przepustka [limtochess_roominfo_choice_6] — tekst] 선택지 6
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_6].content
   limit: do 120 znaków
   EN: Option 6
   PL: Opcja 6
49. [Wydarzenia i Przepustka [limtochess_roominfo_choice_7] — tekst] 선택지 7
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_7].content
   limit: do 120 znaków
   EN: Option 7
   PL: Opcja 7
50. [Wydarzenia i Przepustka [limtochess_roominfo_choice_8] — tekst] 선택지 8
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_8].content
   limit: do 120 znaków
   EN: Option 8
   PL: Opcja 8
51. [Wydarzenia i Przepustka [limtochess_roominfo_choice_option] — tekst] {0} · {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_choice_option].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} · {1}
   PL: {0} · {1}
52. [Wydarzenia i Przepustka [limtochess_briefing_skill] — tekst] 스킬
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_skill].content
   limit: do 120 znaków
   EN: Skills
   PL: Umiejętności
53. [Wydarzenia i Przepustka [limtochess_ink_lobby_run_title] — tekst] 진행 중인 도상구축
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_lobby_run_title].content
   limit: do 120 znaków
   EN: Schemacrafting in Progress
   PL: Konstrukcja Schematów w toku
54. [Wydarzenia i Przepustka [limtochess_ink_lobby_ticker] — tekst] ※ BETA — 베타 기간 중에는 도상구축의 진행 방식과 화면이 달라질 수 있습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_lobby_ticker].content
   limit: do 140 znaków
   EN: ※ In BETA—Gameplay systems and visuals of the Schemacraft mode are subject to change over the Beta period.
   PL: ※ BETA — w okresie beta sposób rozgrywania Konstrukcji Schematów i jej wygląd mogą się zmieniać
55. [Wydarzenia i Przepustka [limtochess_ink_start_ego_resource] — tekst] 시작 E.G.O 자원
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_ego_resource].content
   limit: do 120 znaków
   EN: Starting E.G.O Resource
   PL: Początkowe zasoby E.G.O
56. [Wydarzenia i Przepustka [limtochess_ink_start_primary] — tekst] 구축 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_primary].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Commence\nCraft
   PL: Rozpocznij Konstrukcję
57. [Wydarzenia i Przepustka [limtochess_ink_start_reroll_info] — tekst] · 자동 편성 새로고침 기회는 최대 {1}회까지 보유할 수 있습니다.\n· 자동 편성 새로고침 기회는 매일 {0}회씩 충전됩니다.\n· 도상구축을 마치면 진행도에 따라 자동 편성 새로고침 기회를 {1}회까지 획득할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_reroll_info].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: · You can hold up to {1} Randomized Team Reshuffles.\n· You recover {0} Randomized Team Reshuffles each day.\n· When a Schemacraft run ends, you can earn up to {1} Randomized Team Reshuffles based on your progress.
   PL: · Maksymalnie można mieć {1} odświeżeń Składu Losowego.\n· Każdego dnia odzyskujesz {0} odświeżeń Składu Losowego.\n· Po zakończeniu Konstrukcji Schematów możesz zyskać do {1} odświeżeń stosownie do postępu.
58. [Wydarzenia i Przepustka [limtochess_ink_map_formation] — tekst] 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_map_formation].content
   limit: do 120 znaków
   EN: Team
   PL: Skład drużyny
59. [Wydarzenia i Przepustka [limtochess_ink_start_deck_empty] — tekst] · 자동 편성 새로고침으로 등장한 편성은 화면 하단에 저장되며, 원하는 편성을 선택하여 입장할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_deck_empty].content
   limit: do 170 znaków
   EN: · Teams generated by Randomized Team Reshuffles are saved at the bottom of the screen. Select the team you want to enter with.
   PL: · Składy wylosowane odświeżeniem zapisują się na dole ekranu — wybierz ten, z którym chcesz wejść.
60. [Wydarzenia i Przepustka [limtochess_ink_event_pick_skip] — tekst] 받지 않기
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_event_pick_skip].content
   limit: do 120 znaków
   EN: Decline
   PL: Odrzuć
61. [Wydarzenia i Przepustka [limtochess_ink_pass_tab_reward] — tekst] 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_tab_reward].content
   limit: do 120 znaków
   EN: Reward
   PL: Nagrody
62. [Wydarzenia i Przepustka [limtochess_ink_pass_tab_mission_progress] — tekst] 업적 {0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_tab_mission_progress].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Achievement {0}%
   PL: Osiągnięcia {0}%
63. [Wydarzenia i Przepustka [limtochess_ink_pass_max] — tekst] 최고 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_max].content
   limit: do 120 znaków
   EN: Max Level
   PL: Maks. Poziom
64. [Wydarzenia i Przepustka [limtochess_ink_pass_featured] — tekst] Lv {0} 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_featured].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lv {0} Reward
   PL: Nagroda za Lv {0}
65. [Wydarzenia i Przepustka [limtochess_ink_pass_featured_receivable] — tekst] 지금 받을 수 있습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_featured_receivable].content
   limit: do 120 znaków
   EN: Available to claim
   PL: Można odebrać teraz
66. [Wydarzenia i Przepustka [limtochess_ink_pass_featured_need] — tekst] 패스 경험치 {0} 더 필요합니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_featured_need].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Requires {0} more Pass EXP
   PL: Potrzeba jeszcze {0} PD Przepustki
67. [Wydarzenia i Przepustka [limtochess_ink_pass_featured_received] — tekst] 받은 보상입니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_featured_received].content
   limit: do 120 znaków
   EN: Reward already claimed
   PL: Nagroda już odebrana
68. [Wydarzenia i Przepustka [limtochess_ink_pass_count] — tekst] x{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: x{0}
   PL: x{0}
69. [Wydarzenia i Przepustka [limtochess_ink_pass_coming] — tekst] 준비 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_coming].content
   limit: do 120 znaków
   EN: Coming Soon
   PL: Wkrótce
70. [Wydarzenia i Przepustka [limtochess_ink_result_mvp_tag] — tekst] MVP
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_result_mvp_tag].content
   limit: do 120 znaków
   EN: MVP
   PL: MVP
71. [Wydarzenia i Przepustka [limtochess_ink_prep_ego_owned_demand] — tekst] 보유 / 요구
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_prep_ego_owned_demand].content
   limit: do 120 znaków
   EN: Owned / Required
   PL: Posiadane / wymagane
72. [Wydarzenia i Przepustka [limtochess_ink_pass_featured_item] — tekst] {0} x{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_featured_item].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} x {1}
   PL: {0} x{1}
73. [Wydarzenia i Przepustka [limtochess_ink_pass_mission_empty] — tekst] 등록된 업적이 없습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_mission_empty].content
   limit: do 120 znaków
   EN: No Achievements available
   PL: Brak zarejestrowanych Osiągnięć
74. [Wydarzenia i Przepustka [limtochess_ink_pass_mission_progress] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_mission_progress].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}/{1}
   PL: {0}/{1}
75. [Wydarzenia i Przepustka [limtochess_ink_pass_mission_receivable] — tekst] 받기
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_mission_receivable].content
   limit: do 120 znaków
   EN: Claim
   PL: Odbierz
76. [Wydarzenia i Przepustka [limtochess_ink_pass_mission_received] — tekst] 받음
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_mission_received].content
   limit: do 120 znaków
   EN: Claimed
   PL: Odebrano
77. [Wydarzenia i Przepustka [limtochess_battleprep_sortie_label] — tekst] 전투 가능 인원
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_sortie_label].content
   limit: do 120 znaków
   EN: Deployable Units
   PL: Jednostki zdolne do walki
78. [Wydarzenia i Przepustka [limtochess_ink_pass_exp] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_exp].content
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Wydarzenia i Przepustka [limtochess_ink_pass_beta_notice] — tekst] · 도상구축 플레이로 얻는 패스 경험치는 주마다 최대 1,000까지 획득할 수 있습니다.\n· 현재 개방된 최대 레벨에 도달하면, 도상구축 플레이로 얻는 경험치는 추가로 쌓이지 않습니다.\n· 단, 향후 추가될 업적으로 얻는 경험치의 초과분은 패스 레벨이 확장될 때 자동으로 반영됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_pass_beta_notice].content
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: · You can earn up to 1,000 Pass EXP each week by playing Schemacraft.\n· Once you reach the currently-unlocked level cap, you cannot earn any more EXP from playing Schemacraft.\n· Any excess EXP earned from Achievements added in the future will be applied automatically when the Pass level cap increases.
   PL: · Tygodniowo można zdobyć maks. 1,000 PD Przepustki grając w Konstrukcję Schematów.\n· Po osiągnięciu aktualnie otwartego maks. poziomu PD z Konstrukcji Schematów nie przyrastają dalej.\n· Nadwyżka PD z przyszłych Osiągnięć zostanie naliczona automatycznie, gdy limit poziomu Passu wzrośnie.
80. [Wydarzenia i Przepustka [limtochess_ink_start_drawer_open] — tekst] 출전 인격 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_drawer_open].content
   limit: do 120 znaków
   EN: Select Identity to Deploy
   PL: Wybierz Tożsamość do wysłania
81. [Wydarzenia i Przepustka [limtochess_ink_gauge_cycle] — tekst] TURN {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_gauge_cycle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: TURN {0}
   PL: TURN {0}
82. [Wydarzenia i Przepustka [limtochess_ink_band_ready_buff_turn] — tekst] TURN {0}부터\n효과 적용
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_band_ready_buff_turn].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Effect applied\nfrom TURN {0}
   PL: Efekt działa\nod TURN {0}
83. [Wydarzenia i Przepustka [limtochess_ego_guide_aim_click] — tekst] 대상 적을 선택하세요
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_guide_aim_click].content
   limit: do 120 znaków
   EN: Select target enemy
   PL: Wybierz wrogiego cel
84. [Wydarzenia i Przepustka [limtochess_ego_guide_aim_cancel] — tekst] (우클릭 = 취소)
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_guide_aim_cancel].content
   limit: do 120 znaków
   EN: (Right-click to cancel)
   PL: (PPM = anuluj)
85. [Wydarzenia i Przepustka [limtochess_ego_guide_drop_fire] — tekst] 적 위에 놓으면 발동
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_guide_drop_fire].content
   limit: do 120 znaków
   EN: Drop on an enemy to activate
   PL: Puść nad wrogiem, aby aktywować
86. [Wydarzenia i Przepustka [limtochess_ego_guide_drop_reserve] — tekst] 적 위에 놓으면 사용 예약
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_guide_drop_reserve].content
   limit: do 120 znaków
   EN: Drop on an enemy to queue
   PL: Puść nad wrogiem, aby zakolejkować
87. [Wydarzenia i Przepustka [limtochess_ego_guide_drop_cancel] — tekst] (빈 곳에 놓으면 취소)
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_guide_drop_cancel].content
   limit: do 120 znaków
   EN: (Drop on an empty space to cancel)
   PL: (Puść na pustym miejscu, aby anulować)
88. [Wydarzenia i Przepustka [limtochess_ego_badge_duel] — tekst] 합
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_duel].content
   limit: do 120 znaków
   EN: Clash
   PL: Starcie
89. [Wydarzenia i Przepustka [limtochess_ego_badge_oneside] — tekst] 일방
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_oneside].content
   limit: do 120 znaków
   EN: Unopposed
   PL: Bez oporu
90. [Wydarzenia i Przepustka [limtochess_ego_badge_impossible] — tekst] 불가
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_impossible].content
   limit: do 120 znaków
   EN: Unavailable
   PL: Niedostępne
91. [Wydarzenia i Przepustka [limtochess_ego_badge_target] — tekst] E.G.O 대상
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_target].content
   limit: do 120 znaków
   EN: E.G.O Target
   PL: Cel E.G.O
92. [Wydarzenia i Przepustka [limtochess_ego_badge_resonance] — tekst] {0} {1}공명
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_resonance].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} {1} Reson.
   PL: {0} {1} Rezonans
93. [Wydarzenia i Przepustka [limtochess_ego_badge_absolute] — tekst] 절대 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_ego_badge_absolute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Absolute {0}
   PL: Absolutny {0}
94. [Wydarzenia i Przepustka [limtochess_egoaim_guide] — tekst] 적 위로 드래그
   źródło: LimtochessUI.json :: dataList[id=limtochess_egoaim_guide].content
   limit: do 120 znaków
   EN: Drag onto an enemy
   PL: Przeciągnij na wroga
95. [Wydarzenia i Przepustka [limtochess_egoaim_resonance] — tekst] {0}공명
   źródło: LimtochessUI.json :: dataList[id=limtochess_egoaim_resonance].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Reson.
   PL: {0} Rezonans
96. [Wydarzenia i Przepustka [limtochess_egoaim_absolute] — tekst] {0}완전공명
   źródło: LimtochessUI.json :: dataList[id=limtochess_egoaim_absolute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} A-Reson.
   PL: {0} Rez. Abs.
97. [Wydarzenia i Przepustka [limtochess_egoaim_target] — tekst] {0} ({1})
   źródło: LimtochessUI.json :: dataList[id=limtochess_egoaim_target].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} ({1})
   PL: {0} ({1})
98. [Wydarzenia i Przepustka [limtochess_packpreview_detail] — tekst] 상세 보기
   źródło: LimtochessUI.json :: dataList[id=limtochess_packpreview_detail].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
99. [Wydarzenia i Przepustka [limtochess_ink_start_exp_up] — tekst] 도상구축 패스 경험치 +40%
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_exp_up].content
   limit: do 120 znaków
   EN: Schemacraft Pass EXP +40%
   PL: PD Przepustki Konstrukcji Schematów +40%
100. [Wydarzenia i Przepustka [limtochess_cost_tag] — tekst] COST
   źródło: LimtochessUI.json :: dataList[id=limtochess_cost_tag].content
   limit: do 120 znaków
   EN: COST
   PL: COST
101. [Wydarzenia i Przepustka [limtochess_elite_replace_target_label] — tekst] 교체할 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_replace_target_label].content
   limit: do 120 znaków
   EN: Incoming Identity
   PL: Wchodząca Tożsamość
102. [Wydarzenia i Przepustka [limtochess_result_dmg_label] — tekst] DMG
   źródło: LimtochessUI.json :: dataList[id=limtochess_result_dmg_label].content
   limit: do 120 znaków
   EN: DMG
   PL: DMG
103. [Wydarzenia i Przepustka [limtochess_buildpower_help] — tekst] 구축력은 현재 편성이 얼마나 갖춰졌는지를 보여 주는 수치입니다.\n\n인격의 코스트 · 동기화 단계 · 레벨이 높을수록 구축력이 증가합니다. 또한 같은 키워드 · 소속의 인격을 모으거나, 등급이 높은 E.G.O를 장착하는 경우에도 구축력이 증가합니다. 출격 인격은 대기 인격보다 구축력에 더 크게 반영됩니다.\n\n※ 단, 구축력은 편성의 강함을 가늠하는 참고 지표일 뿐이며, 전투에 직접적인 영향은 주지 않습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_help].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Craftpower shows how well-developed your current team is.\n\nHigher Identity Costs, Uptie Tiers, and levels increase Craftpower. Bringing Identities with the same keyword or faction and equipping higher-grade E.G.O also increase it. Fielded Identities contribute more than Backup Identities.\n\n※ Craftpower is only a guide to your team's strength and has no direct effect on combat.
   PL: Siła Konstrukcji pokazuje, jak rozwinięty jest obecny skład.\n\nWyższy Koszt Tożsamości, Stopień Synchronizacji i poziom zwiększają Siłę Konstrukcji. Również zbieranie Tożsamości tego samego Słowa Kluczowego czy Przynależności oraz wyposażanie E.G.O wyższych rang ją podnosi. Wysłane Tożsamości liczą się bardziej niż Rezerwa.\n\n※ Siła Konstrukcji to jedynie punkt odniesienia siły składu — nie wpływa bezpośrednio na walkę.
104. [Wydarzenia i Przepustka [limtochess_event_block_no_boss_set] — tekst] 보스 적 세트 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_no_boss_set].content
   limit: do 120 znaków
   EN: No Boss Enemy Set
   PL: Brak zestawu wrogów bossa
105. [Wydarzenia i Przepustka [limtochess_event_block_same_boss] — tekst] 지금 최종 보스와 같음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_same_boss].content
   limit: do 120 znaków
   EN: Same as Current Final Boss
   PL: Tak jak obecny Boss Finałowy
106. [Wydarzenia i Przepustka [limtochess_event_block_cleared_boss] — tekst] 이미 깬 보스
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_cleared_boss].content
   limit: do 120 znaków
   EN: Boss Already Defeated
   PL: Boss już pokonany
107. [Wydarzenia i Przepustka [limtochess_event_block_no_target] — tekst] 대상 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_no_target].content
   limit: do 120 znaków
   EN: No Target
   PL: Brak celu
108. [Wydarzenia i Przepustka [limtochess_event_block_not_enough_reroll] — tekst] 새로고침 기회 부족
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_not_enough_reroll].content
   limit: do 120 znaków
   EN: Insufficient Reshuffles
   PL: Za mało odświeżeń
109. [Wydarzenia i Przepustka [limtochess_event_block_skip_off] — tekst] 안 고른다 꺼짐
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_block_skip_off].content
   limit: do 120 znaków
   EN: Skipping Disabled
   PL: Pomijanie niedostępne
110. [Wydarzenia i Przepustka [limtochess_packselect_roster_cap_short] — tekst] 편성 상한 {0}명 — 대체할 수 있는 수감자가 모자랍니다. 고른 카드를 줄이세요
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_roster_cap_short].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Team limit: {0}. There aren't enough Sinners to replace. Select fewer cards.
   PL: Limit składu: {0} — brakuje Grzeszników do wymiany. Zmniejsz wybór kart
111. [Wydarzenia i Przepustka [limtochess_ink_start_auto_cost_info] — tekst] · 자동 편성 선택 시, {0}코스트 안에서 무작위로 인격이 선택됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_auto_cost_info].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: · Selecting Randomized Team picks Identities at random within a Cost limit of {0}.
   PL: · Skład Losowy wybiera Tożsamości losowo w limicie {0} Kosztu.
112. [Wydarzenia i Przepustka [limtochess_notice_roster_cap_up] — tekst] 편성 가능한 인격 수가 {0}명에서 {1}명으로 증가했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_roster_cap_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Maximum Team size increased from {0} to {1}.
   PL: Maksymalny rozmiar składu wzrósł z {0} do {1}.
113. [Wydarzenia i Przepustka [limtochess_level_bonus] — tekst] Lv {0}+{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_level_bonus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Lv {0}+{1}
   PL: Lv {0}+{1}
114. [Wydarzenia i Przepustka [limtochess_ink_gauge_cycle_extended] — tekst] TURN {0} - 연장 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_gauge_cycle_extended].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: TURN {0} - Extended
   PL: TURN {0} - Wydłużony
115. [Wydarzenia i Przepustka [limtochess_battle_effect_level] — tekst] 적 레벨 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_effect_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy Level {0}
   PL: Poziom Wroga {0}
116. [Wydarzenia i Przepustka [limtochess_roster_replace_power_now] — tekst] 현재 구축력
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_power_now].content
   limit: do 120 znaków
   EN: Craftpower
   PL: Obecna Siła Konstrukcji
117. [Wydarzenia i Przepustka [limtochess_buildpower_recommended_label] — tekst] 권장 구축력
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_recommended_label].content
   limit: do 120 znaków
   EN: Rec. Craftpower
   PL: Zalecana Siła Konstrukcji
118. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10910] — tekst] 딜리버리 캐리어 - 로쟈가 15 이상이고 퇴각이 가능할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10910].content
   limit: do 120 znaków
   EN: Use a Defense Skill at 15+ Courier Trunk - Rodion if Retreat is available
   PL: Kufer Kuriera - Rodion 15+: użyj Umiejętności obrony, gdy dostępny jest Odwrót
119. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11011] — tekst] 딜리버리 캐리어 - 싱클레어가 15 이상이고 퇴각이 가능할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11011].content
   limit: do 120 znaków
   EN: Use a Defense Skill at 15+ Courier Trunk - Sinclair if Retreat is available
   PL: Kufer Kuriera - Sinclair 15+: użyj Umiejętności obrony, gdy dostępny jest Odwrót
120. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10812] — tekst] 시[始]가 3 이상이고 퇴각이 가능할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10812].content
   limit: do 120 znaków
   EN: Use a Defense Skill at 3+ Launcher [始] if Retreat is available
   PL: Inicjator [始] 3+: użyj Umiejętności obrony, gdy dostępny jest Odwrót
121. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10613] — tekst] 대기·복귀 인원이 있고 퇴각시킬 흑수가 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10613].content
   limit: do 120 znaków
   EN: Use a Defense Skill if a Backup or returning unit is available and a Heishou can Retreat
   PL: Użyj Umiejętności obrony, gdy dostępna jest Rezerwa albo jednostka wraca do walki, a któryś Heishou może zejść w Odwrót
122. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10710] — tekst] 듀라한을 준비할 때, 또는 공격받을 때 듀라한이 있고 정신력이 15 이상이어서 강화 반격이 가능하면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10710].content
   limit: do 200 znaków
   EN: Use a Defense Skill when readying Dullahan, or when targeted by an attack if Dullahan is active and this unit is at 15+ SP, allowing an empowered Counter
   PL: Użyj Umiejętności obrony przy przygotowaniu Dullahana albo gdy jesteś celem ataku, masz Dullahana i Poczytalność 15+, co pozwala na Wzmocnioną Kontrę
123. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10415] — tekst] 천살을 준비할 거미집 아군이 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10415].content
   limit: do 150 znaków
   EN: Use a Defense Skill when Slay the Heavens - Tiansha can be readied against "The House of Spiders" ally on the field
   PL: Użyj Umiejętności obrony, gdy można przygotować Cięcie Ostrzem Gwiazdy Tiansha przeciw sojusznikowi Domu Pajęczyn na polu
124. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10416] — tekst] 르누아르 개버딘 원단 코트와 아르뮈르 에비이예를 전환할 때, 또는 공격받을 때 강화 공격이 가능하면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10416].content
   limit: do 210 znaków
   EN: Use a Defense Skill when switching between Le Noir: Gabardine Overcoat and Armure Éveillée, or if an empowered attack is available when targeted by an attack
   PL: Użyj Umiejętności obrony przy przełączaniu Le Noir: Płaszcz z Gabardyny i Armure Éveillée albo gdy jesteś celem ataku i dostępny jest Wzmocniony Atak
125. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10216] — tekst] 공격받을 때, 불꽃나비의 관이 30 이상이고 과열된 관이 없으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10216].content
   limit: do 130 znaków
   EN: Use a Defense Skill when targeted by an attack at 30+ Fire Butterfly Coffin and no Overheated Coffin
   PL: Użyj Umiejętności obrony, gdy jesteś celem ataku, masz Trumnę Ognistych Motyli 30+ i nie ma Przegrzanej Trumny
126. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11216] — tekst] 공격받을 때, 새벽불이 30 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11216].content
   limit: do 120 znaków
   EN: Use a Defense Skill when targeted by an attack at 30+ Light of Daybreak
   PL: Użyj Umiejętności obrony, gdy jesteś celem ataku, a Płomień Świtu wynosi 30+
127. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10110] — tekst] 산나비와 죽은나비의 합이 최대치의 25% 이하이고 재장전 뒤 정신력이 -40 초과일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10110].content
   limit: do 210 znaków
   EN: Use a Defense Skill when the sum of The Living(Ammo) and The Departed(Ammo) totals at 25% or less of their max Stacks and SP is more than -40 after reloading
   PL: Użyj Umiejętności obrony, gdy suma Żywych i Zmarłych wynosi 25% maksimum lub mniej, a Poczytalność po przeładowaniu jest powyżej -40
128. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10115] — tekst] 해금 - II를 준비할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10115].content
   limit: do 120 znaków
   EN: Use a Defense Skill when Unlock - II can be readied
   PL: Użyj Umiejętności obrony, gdy można przygotować Odblokowanie - II
129. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10213] — tekst] 저격 자세를 준비하거나 섬궁으로 전환할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10213].content
   limit: do 140 znaków
   EN: Use a Defense Skill when Ready to Loose can be readied or this unit's Skill can be switched to Bow's Glimmer
   PL: Użyj Umiejętności obrony, gdy można przygotować Postawę Snajperską albo przełączyć Umiejętność na Błysk Łuku
130. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10309] — tekst] 시간 대여를 시작할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10309].content
   limit: do 120 znaków
   EN: Use a Defense Skill when Borrowed Time can be activated
   PL: Użyj Umiejętności obrony, gdy można rozpocząć Pożyczony Czas
131. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10314] — tekst] 해금 단계를 높일 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10314].content
   limit: do 120 znaków
   EN: Use a Defense Skill when Unlock can advance to the next stage
   PL: Użyj Umiejętności obrony, gdy można podnieść stopień Odblokowania
132. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10315] — tekst] 검은 신의 가호가 100 이상이어서 강화 공격을 사용할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10315].content
   limit: do 120 znaków
   EN: Use a Defense Skill at 100+ Blessing of the Obsidian God if an enhanced attack is available
   PL: Użyj Umiejętności obrony przy Łasce Czarnego Boga 100+, gdy dostępny jest Wzmocniony Atak
133. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10412] — tekst] 시선의 경멸 상태로 진입할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10412].content
   limit: do 120 znaków
   EN: Use a Defense Skill when Contempt of the Gaze can be activated
   PL: Użyj Umiejętności obrony, gdy można wejść w stan Pogardy Spojrzenia
134. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10514] — tekst] 포자탄[기본]과 포자탄[산탄]의 합이 최대치의 25% 이하이고 재장전 뒤 정신력이 -40 초과일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10514].content
   limit: do 210 znaków
   EN: Use a Defense Skill when the sum of Spore Round [Base] and Spore Round [Buckshot] totals at 25% or less of their max Stacks and SP is more than -40 after reloading
   PL: Użyj Umiejętności obrony, gdy suma Pocisków Zarodnikowych [Podstawowy] i [Śrut] wynosi 25% maksimum lub mniej, a Poczytalność po przeładowaniu jest powyżej -40
135. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10611] — tekst] 탄환이 없고 재장전할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10611].content
   limit: do 120 znaków
   EN: Use a Defense Skill when out of Ammo if reloading is available
   PL: Użyj Umiejętności obrony, gdy nie ma amunicji, a przeładowanie jest dostępne
136. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10713] — tekst] 충전 횟수가 15 미만이고 과충전을 준비할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10713].content
   limit: do 120 znaków
   EN: Use a Defense Skill at fewer than 15 Charge Count if Overcharge can be readied
   PL: Użyj Umiejętności obrony przy Liczniku Ładowania poniżej 15, gdy można przygotować Nadładowanie
137. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10813] — tekst] 다음 스킬로 스킬 1이 2개 이상 쌓여 짝패를 바꿀 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10813].content
   limit: do 120 znaków
   EN: Use a Defense Skill to change Suits when at least 2 copies of Skill 1 are queued
   PL: Użyj Umiejętności obrony, by zmienić Rękę, gdy w kolejce zebrały się co najmniej 2 kopie Umiejętności 1
138. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10816] — tekst] 체력이 10% 이하여서 탈의실에 들어가거나 탈의실에서 체력이 최대 체력 미만이어서 회복할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10816].content
   limit: do 150 znaków
   EN: Use a Defense Skill to enter Changing Room at 10% HP or less, or to heal while in Changing Room if below max HP
   PL: Użyj Umiejętności obrony, by wejść do Przymierzalni przy 10% HP lub mniej, albo by się leczyć w Przymierzalni, gdy HP poniżej maksimum
139. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10902] — tekst] 공격받을 때, 호흡이 5 이상이어서 흑운도 패시브로 강화 반격을 사용할 수 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10902].content
   limit: do 160 znaków
   EN: Use a Defense Skill when targeted by an attack if 5+ Poise enables the enhanced Counter from the Dark Cloud Blade Passive
   PL: Użyj Umiejętności obrony, gdy jesteś celem ataku, a Oddech 5+ pozwala na Wzmocnioną Kontrę z pasywu Ostrza Czarnej Chmury
140. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10909] — tekst] 시간 대여를 시작할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10909].content
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10913] — tekst] 눈물 벼리기가 3 미만이고 정신력 소모 뒤 정신력이 -40 초과일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10913].content
   limit: do 130 znaków
   EN: Use a Defense Skill at fewer than 3 Tear-sharpened if SP is more than -40 after paying the SP cost
   PL: Użyj Umiejętności obrony przy Ostrzonych Łzami poniżej 3, gdy Poczytalność po zapłacie kosztu jest powyżej -40
142. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10915] — tekst] 자신에게 레플렉시옹이 없고 공격해 오는 적의 부정적인 효과가 3개 이상이어서 크리틱을 사용할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10915].content
   limit: do 190 znaków
   EN: Use a Defense Skill if this unit does not have Réflexion and the attacking enemy has 3+ types of negative effect, allowing Critique to activate
   PL: Użyj Umiejętności obrony, gdy nie masz Réflexion, a atakujący wróg ma 3+ negatywnych efektów, co pozwala użyć Krytyki
143. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10916] — tekst] 가속탄이 5 미만이어서 보충할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10916].content
   limit: do 120 znaków
   EN: Use a Defense Skill at fewer than 5 Acceleration Rounds if they can be gained
   PL: Użyj Umiejętności obrony przy Pociskach Przyspieszenia poniżej 5, gdy można je uzupełnić
144. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11113] — tekst] 시간 대여를 시작할 수 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11113].content
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11213] — tekst] 체력 40% 이하인 적이 있고 메르체 추가 공격을 준비할 수 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11213].content
   limit: do 130 znaków
   EN: Use a Defense Skill if an enemy is at 40% HP or less and the additional Mercé attack can be readied
   PL: Użyj Umiejętności obrony, gdy wróg ma 40% HP lub mniej, a dodatkowy atak Mercé można przygotować
146. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10111] — tekst] 미끼 요정이 3 미만일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10111].content
   limit: do 120 znaków
   EN: Use a Defense Skill instead of Skill 1 at fewer than 3 Fairy Lure
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Wabiku Wróżek poniżej 3
147. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10113] — tekst] 반격할 상대가 있고 찢어진 추억이 2 미만일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10113].content
   limit: do 130 znaków
   EN: Use a Defense Skill when there is an enemy to Counter and this unit has fewer than 2 Torn Memory
   PL: Użyj Umiejętności obrony, gdy jest kto Kontrować, a Naderwanych Wspomnień masz mniej niż 2
148. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10114] — tekst] 각력【오】가 없고 다음 턴에 얻을 예정도 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10114].content
   limit: do 150 znaków
   EN: Use a Defense Skill in place of Skill 1 if this unit does not have Strider [Wu] and is not set to gain it next turn
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie masz Kroczącego【Wu】 i nie zdobędziesz go w następnej turze
149. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10207] — tekst] 공격받을 때 진동 횟수가 6 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10207].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if Tremor Count is fewer than 6
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Wstrząsu poniżej 6
150. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10210] — tekst] 공격받을 때 충전 횟수가 5 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10210].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if Charge Count is fewer than 5
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Ładowania poniżej 5
151. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10211] — tekst] 공격받을 때 자기 화상이 10 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10211].content
   limit: do 120 znaków
   EN: Use a Defense Skill when targeted by an attack and this unit has 10+ Burn on self
   PL: Użyj Umiejętności obrony, gdy jesteś celem ataku i masz 10+ Podpalenia na sobie
152. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10212] — tekst] 반격할 상대가 있고 각력【묘】가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10212].content
   limit: do 130 znaków
   EN: Use a Defense Skill when there is a target to counter and this unit does not have Strider [Mao]
   PL: Użyj Umiejętności obrony, gdy jest kto Kontrować, a nie masz Biegacza【Mao】
153. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10312] — tekst] 공격받을 때 사랑/증오 횟수가 4 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10312].content
   limit: do 120 znaków
   EN: Use a Defense Skill when targeted by an attack at fewer than 4 Love/Hate Count
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Miłości/Nienawiści poniżej 4
154. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10313] — tekst] 반격할 상대가 있고 발각[發角]이 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10313].content
   limit: do 140 znaków
   EN: Use a Defense Skill when there is a target to counter and this unit does not have Burgeoning of Horns [發角]
   PL: Użyj Umiejętności obrony, gdy jest kto Kontrować, a nie masz Wyrastania Rogów [發角]
155. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10411] — tekst] 반격할 상대가 있고 각력【묘】가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10411].content
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10413] — tekst] 호위태세가 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10413].content
   limit: do 120 znaków
   EN: Use a Defense Skill in place of Skill 1 if this unit does not have Protector's Stance
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie masz Postawy Strażniczej
157. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10503] — tekst] 충전 횟수가 5 미만일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10503].content
   limit: do 120 znaków
   EN: Use a Defense Skill instead of Skill 1 if Charge Count is fewer than 5
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Liczniku Ładowania poniżej 5
158. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10506] — tekst] 공격받을 때 충전 횟수가 5 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10506].content
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10612] — tekst] 공격받을 때 충전 횟수가 10 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10612].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if Charge Count is fewer than 10
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Ładowania poniżej 10
160. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10709] — tekst] 공격받을 때 충전 횟수가 5 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10709].content
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10714] — tekst] 반격할 상대가 있고 혈염[血炎]이 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10714].content
   limit: do 130 znaków
   EN: Use a Defense Skill when there is a target to counter and this unit does not have Bloodflame [血炎]
   PL: Użyj Umiejętności obrony, gdy jest kto Kontrować, a nie masz Bloodflame [血炎]
162. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10810] — tekst] 방어 태세가 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10810].content
   limit: do 120 znaków
   EN: Use a Defense Skill instead of Skill 1 if this unit does not have Defensive Stance
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie masz Postawy Obronnej
163. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10905] — tekst] 충전 횟수가 5 미만일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10905].content
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10912] — tekst] 사완이 없고 다음 턴에 얻을 예정도 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10912].content
   limit: do 150 znaków
   EN: Use a Defense Skill in place of Skill 1 if this unit does not have Serpent Arm and is not set to gain it next turn
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie masz Wężowego Ramienia i nie zdobędziesz go w następnej turze
165. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10914] — tekst] 공격받을 때 충전 횟수가 5 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10914].content
   (powtórzenie elementu 150 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11010] — tekst] 공격받을 때 진동 횟수가 3 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11010].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if Tremor Count is fewer than 3
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Wstrząsu poniżej 3
167. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11014] — tekst] 반격할 상대가 있고 혈염[血炎]이 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11014].content
   (powtórzenie elementu 161 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11015] — tekst] 호흡 25 미만이면 스킬 1을 사용할 차례에 수비 사용. 호흡 25 이상이고 공격받을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11015].content
   limit: do 170 znaków
   EN: Use a Defense Skill instead of Skill 1 if Poise is fewer than 25. At 25+ Poise, use a Defense Skill when targeted by an attack
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Oddechu poniżej 25. Przy Oddechu 25+ używaj Umiejętności obrony, gdy jesteś celem ataku
169. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11110] — tekst] 공격받을 때 충전 횟수가 15 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11110].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if Charge Count is fewer than 15
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Liczniku Ładowania poniżej 15
170. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11112] — tekst] 반격할 상대가 있고 각력【묘】가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11112].content
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11211] — tekst] 12구산 연료가 50 미만일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11211].content
   limit: do 120 znaków
   EN: Use a Defense Skill instead of Skill 1 if District 12 Fuel is fewer than 50
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Paliwie Dystryktu 12 poniżej 50
172. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11212] — tekst] 사완이 없고 다음 턴에 얻을 예정도 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11212].content
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11215] — tekst] 고전압 외피가 없을 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11215].content
   limit: do 120 znaków
   EN: Use a Defense Skill instead of Skill 1 if this unit does not have High-voltage Exoskeleton
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie masz Pancerza Wysokiego Napięcia
174. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10105] — tekst] 공격받을 때, 대기 스킬에 스킬 1만 2개 이상 남았으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10105].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if only 2 or more Skill 1s remain in queue
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, jeśli w kolejce zostały tylko co najmniej 2 Umiejętności 1
175. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11105] — tekst] 공격받을 때, 대기 스킬에 스킬 1만 2개 이상 남았으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11105].content
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10108] — tekst] 공격받을 때, 대기 스킬에 스킬 3 없이 탐구한 지식을 유지하거나 올릴 수 있는 버리기가 가능할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10108].content
   limit: do 170 znaków
   EN: When targeted by an attack, use a Defense Skill if there is no Queued Skill 3 and this unit can Discard to maintain or gain Insight
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy w kolejce nie ma Umiejętności 3, a Odrzucenie pozwala zachować albo podnieść Zgłębioną Wiedzę
177. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10608] — tekst] 공격받을 때, 대기 스킬에 스킬 3 없이 탐구한 지식을 유지하거나 올릴 수 있는 버리기가 가능할 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10608].content
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10510] — tekst] 공격받을 때, 대기 스킬에서 스킬 3을 보존하면서 탐구한 지식을 유지하거나 올릴 수 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10510].content
   limit: do 160 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit can maintain or gain Insight without using up Queued Skill 3
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy możesz zachować albo podnieść Zgłębioną Wiedzę, nie zużywając Umiejętności 3 z kolejki
179. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10907] — tekst] 공격받을 때, 대기 스킬에서 스킬 3을 보존하면서 탐구한 지식을 유지하거나 올릴 수 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10907].content
   (powtórzenie elementu 178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10116] — tekst] 충전 횟수가 7 미만이고 체력 비용을 낸 뒤 체력이 60% 이상이면 스킬 1을 사용할 차례에 수비 사용. 충전 횟수 15 초과·체력 85% 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10116].content
   limit: do 240 znaków
   EN: Use a Defense Skill instead of Skill 1 if Charge Count is fewer than 7 and HP is at 60%+ after paying the HP cost. Also use a Defense Skill if Charge Count is at 15+ and HP is below 85%
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Liczniku Ładowania poniżej 7 i HP 60%+ po zapłacie kosztu HP. Używaj też Umiejętności obrony przy Liczniku Ładowania 15+ i HP poniżej 85%
181. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10310] — tekst] 혈찬이 10 이상이고 경혈이 10 미만이며 체력이 60% 이상일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10310].content
   limit: do 140 znaków
   EN: Use a Defense Skill instead of Skill 1 if this unit has 10+ Bloodfeast, fewer than 10 Hardblood, and 60%+ HP
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy masz 10+ Krwawej Uczty, mniej niż 10 Twardej Krwi i 60%+ HP
182. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10414] — tekst] 공격받을 때, 체력이 80% 이상이고 꽃잎이 10 미만이며 취약이 없으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10414].content
   limit: do 150 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit has 80%+ HP, fewer than 10 Petals, and no Fragile
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy masz 80%+ HP, mniej niż 10 Płatków Kwiatów i brak Wrażliwości
183. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10513] — tekst] 공격받을 때, 경혈 갑주가 3 미만이고 대상 아군이 출혈 비용을 낸 뒤 체력이 60% 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10513].content
   limit: do 200 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit has fewer than 3 Hardblood Armor and the target ally is at 60%+ HP after paying the Bleed cost
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy masz mniej niż 3 Pancerza Twardej Krwi, a cel-sojusznik ma 60%+ HP po zapłacie kosztu Krwawienia
184. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10605] — tekst] 공격받을 때, 체력이 50% 이하이고 K사 앰플이 2 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10605].content
   limit: do 150 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit has 50% or less HP and fewer than 2 K Corp Ampules
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy masz 50% HP lub mniej i mniej niż 2 Ampułki Korp. K
185. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10702] — tekst] 공격받을 때, 호흡 횟수가 3 이상이고 체력 5를 소모한 뒤 체력이 60% 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10702].content
   limit: do 150 znaków
   EN: When targeted by an attack, use a Defense Skill if Poise Count is 3+ and this unit has 60%+ HP after consuming 5 HP
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy masz 3+ Liczniki Oddechu i 60%+ HP po zużyciu 5 HP
186. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10705] — tekst] 공격받을 때, 체력이 60% 이상이고 정신력이 -20 이상 0 이하이며 자기 침잠이 5 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10705].content
   limit: do 190 znaków
   EN: When targeted by an attack, use a Defense Skill if HP is at 60% or less, SP is between -20 and 0 inclusive, and Sinking on self is fewer than 5
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy HP wynosi 60% lub mniej, Poczytalność mieści się w przedziale od -20 do 0, a Zatonięcia na sobie masz mniej niż 5
187. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11005] — tekst] 정신력 -30 이하일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11005].content
   limit: do 120 znaków
   EN: Use a Defense Skill if SP is -30 or lower
   PL: Użyj Umiejętności obrony, gdy Poczytalność wynosi -30 lub mniej
188. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11006] — tekst] 공격받을 때, 부적이 4이고 뒤에 전달할 3스킬이 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11006].content
   limit: do 170 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit has 4 Talisman and a Skill 3 available afterward to transfer them
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy masz 4 Talizmany i Umiejętność 3 do przekazania ich dalej
189. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11016] — tekst] 폭주 상태가 아니고 맥동 횟수가 15 미만이며 체력 비용을 낸 뒤 체력이 60% 이상일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11016].content
   limit: do 230 znaków
   EN: Use a Defense Skill instead of Skill 1 if this unit is not in Uncontrollable Rampage state, Pulsation Count is fewer than 15, and this unit has 60%+ HP after paying the HP cost
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1, gdy nie trwasz w stanie Paroksyzmu, Licznik Pulsacji jest poniżej 15, a HP wynosi 60%+ po zapłacie kosztu HP
190. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11107] — tekst] 공격받을 때, 마탄이 6 미만이고 정신력 비용을 낸 뒤 정신력이 -20 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11107].content
   limit: do 170 znaków
   EN: When targeted by an attack, use a Defense Skill if Magic Bullet is fewer than 6 and this unit has -20+ SP after paying the SP cost
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy Magicznych Pocisków masz mniej niż 6, a Poczytalność po zapłacie kosztu wynosi -20 lub więcej
191. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11210] — tekst] 체력 40% 미만이고 혈찬이 있으면 수비 사용. 그 외에는 닳아버린 마음이 3 미만이고 출혈 비용을 낸 뒤 체력이 60% 이상이면 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11210].content
   limit: do 270 znaków
   EN: Use a Defense Skill if HP is at 40% or less and Bloodfeast is available. Otherwise, use a Defense Skill instead of Skill 1 if Ailing Heart is fewer than 3 and this unit has 60%+ HP after paying the Bleed cost
   PL: Użyj Umiejętności obrony przy HP 40% lub mniej, jeśli masz Krwawą Ucztę. W przeciwnym razie użyj Umiejętności obrony zamiast Umiejętności 1 przy Zmęczonym Sercu poniżej 3 i HP 60%+ po zapłacie kosztu Krwawienia
192. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11214] — tekst] 램프가 8 미만이고 체력 비용을 낸 뒤 체력이 60% 이상일 때, 스킬 1을 사용할 차례에 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11214].content
   limit: do 150 znaków
   EN: Use a Defense Skill instead of Skill 1 if Lamp is fewer than 8 and this unit has 60%+ HP after paying the HP cost
   PL: Użyj Umiejętności obrony zamiast Umiejętności 1 przy Lampie poniżej 8 i HP 60%+ po zapłacie kosztu HP
193. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10215] — tekst] 구속 해제 - 창작 몰입 상태에서 체력 70% 이하인 아군이 있고 원호 방어가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10215].content
   limit: do 160 znaków
   EN: Use a Defense Skill while in The Self Unbound - Flow State if an ally has 70% HP or less and there is no Assist Defense
   PL: Użyj Umiejętności obrony w Stanie Przepływu Uwolnienia Jaźni, gdy sojusznik ma 70% HP lub mniej, a nie ma Obrony Wsparcia
194. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10614] — tekst] 체력 70% 이하인 아군이 있고 원호 방어가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10614].content
   limit: do 120 znaków
   EN: Use a Defense Skill if an ally has 70% HP or less and there is no Assist Defense
   PL: Użyj Umiejętności obrony, gdy sojusznik ma 70% HP lub mniej, a nie ma Obrony Wsparcia
195. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10615] — tekst] 공격받을 때, 호흡이 5 미만이고 포박 [홍루]가 부여된 적이 없으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10615].content
   limit: do 140 znaków
   EN: When targeted by an attack, use a Defense Skill at fewer than 5 Poise and no enemies have Trussed [Hong Lu]
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony przy Oddechu poniżej 5, gdy żaden wróg nie ma Skutego [Hong Lu]
196. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10711] — tekst] 공격받을 때, 원호 가능한 마침표 홍루가 있고 집중【저격】이 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10711].content
   limit: do 190 znaków
   EN: When targeted by an attack, use a Defense Skill if Full-Stop Office Hong Lu is available for Assist and this unit has no Concentration【Sniper】
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy do Wsparcia dostępny jest Hong Lu z Biura Kropki, a nie masz Skupienia【Snajper】
197. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10808] — tekst] 공격받을 때, 양옆 아군 중 정신력이 35 이하인 아군이 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10808].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if either adjacent ally has 35 or less SP
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, gdy któryś z sąsiednich sojuszników ma 35 Poczytalności lub mniej
198. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10811] — tekst] 속도가 가장 빠른 흑운회 아군 2명 중 체력 70% 이하이고 수비 위력 증가가 없는 아군이 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10811].content
   limit: do 180 znaków
   EN: Use a Defense Skill if either of the 2 Kurokumo Clan allies with the fastest Speed has 70% or less HP and no allies have Defense Power Up
   PL: Użyj Umiejętności obrony, gdy któryś z 2 najszybszych sojuszników Klanu Kurokumo ma 70% HP lub mniej i nie ma Wzrostu Mocy Obrony
199. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10815] — tekst] 체력 70% 이하인 아군이 있고 원호 방어가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10815].content
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10911] — tekst] 공격받을 때, 출혈이 3 이상인 다른 아군이 있으면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10911].content
   limit: do 120 znaków
   EN: When attacked, use a Defense Skill if another ally has 3+ Bleed
   PL: Gdy jesteś atakowany, użyj Umiejętności obrony, gdy inny sojusznik ma 3+ Krwawienia
201. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10917] — tekst] 본인이나 체력 비율이 가장 낮은 아군 2명 중 체력 70% 이하이고 보호막이 없는 대상이 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10917].content
   limit: do 160 znaków
   EN: Use a Defense Skill if this unit or either of the 2 allies with the lowest HP percentages has 70% or less HP and no Shield
   PL: Użyj Umiejętności obrony, gdy ty albo jeden z 2 sojuszników o najniższym HP ma 70% HP lub mniej i nie ma Tarczy
202. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10410] — tekst] 공격받을 때, 반격으로 얻을 적안 또는 참회가 7 미만이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10410].content
   limit: do 180 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit will gain fewer than 7 Red Eyes or Penitence this unit's Counter will grant
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, jeśli Kontra da ci mniej niż 7 Czerwonych Ok lub Pokuty
203. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11116] — tekst] 체력 70% 이하인 아군이 있고 원호 방어가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11116].content
   (powtórzenie elementu 194 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10316] — tekst] 공격해 오는 적의 쐐기 - 싱클레어가 4 이상일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10316].content
   limit: do 120 znaków
   EN: Use a Defense Skill if the attacking enemy has 4+ Wedge - Sinclair
   PL: Użyj Umiejętności obrony, gdy atakujący wróg ma 4+ Klin - Sinclair
205. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11017] — tekst] 공격해 오는 적의 쐐기 - 돈키호테가 4 이상일 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11017].content
   limit: do 120 znaków
   EN: Use a Defense Skill if the attacking enemy has 4+ Wedge - Don Quixote
   PL: Użyj Umiejętności obrony, gdy atakujący wróg ma 4+ Klin - Don Quixote
206. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10617] — tekst] 경청의 시간이 있으면 공격받을 때 수비 사용. 그 외에는 체력 70% 이하인 아군이 있고 원호 방어가 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10617].content
   limit: do 220 znaków
   EN: If this unit has Time to Listen, use a Defense Skill when targeted by an attack. Otherwise, use a Defense Skill if an ally has 70% HP or less and there is no Assist Defense
   PL: Jeśli masz Czas Uważnego Słuchu, użyj Umiejętności obrony, gdy jesteś celem ataku. W przeciwnym razie użyj Umiejętności obrony, gdy sojusznik ma 70% HP lub mniej, a nie ma Obrony Wsparcia
207. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10717] — tekst] 공격 받을 때, 자신의 체력이 50% 이상이면 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10717].content
   limit: do 120 znaków
   EN: When targeted by an attack, use a Defense Skill if this unit's HP is at 50%+
   PL: Gdy jesteś celem ataku, użyj Umiejętności obrony, jeśli twoje HP wynosi 50% lub więcej
208. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_10117] — tekst] 공격해 오는 적에게 '규칙: 수비 스킬 지정 금지'가 있을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_10117].content
   limit: do 120 znaków
   EN: Use a Defense Skill if the attacking enemy has "Rule: Targeting Defense Skills Prohibited"
   PL: Użyj Umiejętności obrony, gdy atakujący wróg ma „Zasadę: Zakaz Namierzania Umiejętności Obrony”
209. [Wydarzenia i Przepustka [limtochess_defense_identity_condition_11217] — tekst] 이어진 실을 보유한 아군이 없을 때 수비 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_condition_11217].content
   limit: do 120 znaków
   EN: Use a Defense Skill if no ally has Thread Tether
   PL: Użyj Umiejętności obrony, gdy żaden sojusznik nie ma Połączonej Nici
210. [Wydarzenia i Przepustka [limtochess_defense_identity_retreat_support] — tekst] 이스마엘의 지원 효과로 퇴각이 가능할 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_retreat_support].content
   limit: do 120 znaków
   EN: When Retreat is available through Ishmael's Support effect
   PL: Gdy Odwrót jest dostępny dzięki efektowi wsparcia Ishmael
211. [Wydarzenia i Przepustka [limtochess_defense_identity_fallback] — tekst] 이 인격의 고유 조건이 충족될 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_defense_identity_fallback].content
   limit: do 120 znaków
   EN: When Identity-specific conditions are filled
   PL: Gdy spełniony jest warunek własny tej Tożsamości
212. [Wydarzenia i Przepustka [limtochess_event_choice_tag_gain] — tekst] 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_choice_tag_gain].content
   limit: do 120 znaków
   EN: Acquire
   PL: Zdobyte
213. [Wydarzenia i Przepustka [limtochess_event_choice_tag_cost] — tekst] 대가
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_choice_tag_cost].content
   limit: do 120 znaków
   EN: Consequence
   PL: Konsekwencja
214. [Wydarzenia i Przepustka [limtochess_buildpower_band_low] — tekst] 주의
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_band_low].content
   limit: do 120 znaków
   EN: Risky
   PL: UWAGA
215. [Wydarzenia i Przepustka [limtochess_buildpower_band_fit] — tekst] 적정
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_band_fit].content
   limit: do 120 znaków
   EN: Fair
   PL: Umiarkowane
216. [Wydarzenia i Przepustka [limtochess_buildpower_band_high] — tekst] 여유
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_band_high].content
   limit: do 120 znaków
   EN: Easy
   PL: Niskie
217. [Wydarzenia i Przepustka [limtochess_buildpower_penalty_hint] — tekst] 패널티 상세 확인
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_penalty_hint].content
   limit: do 120 znaków
   EN: View Penalty Details
   PL: Szczegóły Kar
218. [Wydarzenia i Przepustka [limtochess_buildpower_range] — tekst] {0}~{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_range].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}~{1}
   PL: {0}~{1}
219. [Wydarzenia i Przepustka [limtochess_packselect_cap_title] — tekst] 편성 인원 가득 참
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_cap_title].content
   limit: do 120 znaków
   EN: Team Full
   PL: Skład pełny
220. [Wydarzenia i Przepustka [limtochess_packselect_cap_desc] — tekst] 선택 시 기존 인격 1명을 제외합니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_cap_desc].content
   limit: do 120 znaków
   EN: Must remove 1 ID from Team to recruit
   PL: Wybór usunie 1 dotychczasową Tożsamość
221. [Wydarzenia i Przepustka [limtochess_egoreplace_sync_label] — tekst] 환상 해석
   źródło: LimtochessUI.json :: dataList[id=limtochess_egoreplace_sync_label].content
   limit: do 120 znaków
   EN: Threadspinning
   PL: Analiza Anomalii
222. [Wydarzenia i Przepustka [limtochess_report_to_formation_retry] — tekst] 편성을 변경하여 재도전
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_to_formation_retry].content
   limit: do 120 znaków
   EN: Change Team and Retry
   PL: Zmień skład i ponów
223. [Wydarzenia i Przepustka [limtochess_rest_generic_short] — tekst] 범용 조각이 부족합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_short].content
   limit: do 120 znaków
   EN: Not enough Universal Slivers.
   PL: Za mało Okruchów Uniwersalnych.
224. [Wydarzenia i Przepustka [limtochess_lobby_run_level] — tekst] 인격 레벨 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_lobby_run_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Identity Level {0}
   PL: Poziom Tożsamości {0}
225. [Wydarzenia i Przepustka [limtochess_packselect_boss_reward] — tekst] 보스 클리어 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_boss_reward].content
   limit: do 120 znaków
   EN: Boss Clear Reward
   PL: Nagroda za pokonanie bossa
226. [Wydarzenia i Przepustka [limtochess_packselect_slot_reroll_identity] — tekst] 새로고침
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_slot_reroll_identity].content
   limit: do 120 znaków
   EN: Reshuffle
   PL: Odśwież
227. [Wydarzenia i Przepustka [limtochess_packselect_slot_reroll_ego] — tekst] 새로고침
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_slot_reroll_ego].content
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Wydarzenia i Przepustka [limtochess_packselect_slot_reroll_used] — tekst] 새로고침 완료
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_slot_reroll_used].content
   limit: do 120 znaków
   EN: Reshuffled
   PL: Odświeżono
229. [Wydarzenia i Przepustka [limtochess_packselect_sync_keep] — tekst] 동기화 {0}단계 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_sync_keep].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Keep Uptie Tier {0}
   PL: Synchronizacja {0} bez zmian
230. [Wydarzenia i Przepustka [limtochess_roominfo_list_event_skip_head] — tekst] 선택하지 않을 때
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_list_event_skip_head].content
   limit: do 120 znaków
   EN: If no choice is made
   PL: Jeśli nic nie wybierzesz
231. [Wydarzenia i Przepustka [limtochess_packselect_title_event_reward] — tekst] 이벤트 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_title_event_reward].content
   limit: do 120 znaków
   EN: Event Reward
   PL: Nagroda wydarzenia
232. [Wydarzenia i Przepustka [limtochess_ink_start_reroll_caption] — tekst] 남은 횟수
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_reroll_caption].content
   limit: do 120 znaków
   EN: Reshuffles Left
   PL: Pozostałe użycia
233. [Wydarzenia i Przepustka [limtochess_packselect_title_normal_reward] — tekst] 일반 전투 클리어 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_title_normal_reward].content
   limit: do 120 znaków
   EN: Regular Encounter Clear Reward
   PL: Nagroda za ukończenie Zwykłego Starcia
234. [Wydarzenia i Przepustka [limtochess_packselect_title_elite_reward] — tekst] 정예 전투 클리어 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_title_elite_reward].content
   limit: do 120 znaków
   EN: Elite Encounter Clear Reward
   PL: Nagroda za ukończenie Walki Elitarnej
235. [Wydarzenia i Przepustka [limtochess_part_focus_6011_pole_broken] — tekst] 전봇대 파괴
   źródło: LimtochessUI.json :: dataList[id=limtochess_part_focus_6011_pole_broken].content
   limit: do 120 znaków
   EN: Telepole Destroyed
   PL: Zniszczono Telepole
236. [Wydarzenia i Przepustka [limtochess_part_focus_6011_pole_failed] — tekst] 전봇대 파괴 실패
   źródło: LimtochessUI.json :: dataList[id=limtochess_part_focus_6011_pole_failed].content
   limit: do 120 znaków
   EN: Failed to Destroy Telepole
   PL: Nie zniszczono Telepole
237. [Wydarzenia i Przepustka [limtochess_part_focus_6011_pole_imminent] — tekst] 적뢰 발동 임박
   źródło: LimtochessUI.json :: dataList[id=limtochess_part_focus_6011_pole_imminent].content
   limit: do 120 znaków
   EN: Red Bolts Imminent
   PL: Czerwone Wyładowania wkrótce
238. [Wydarzenia i Przepustka [limtochess_report_axis_round] — tekst] T{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_axis_round].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: T{0}
   PL: T{0}
239. [Wydarzenia i Przepustka [limtochess_packselect_toggle_replace_identity] — tekst] 인격 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_replace_identity].content
   limit: do 120 znaków
   EN: Replace ID
   PL: Wymiana Tożsamości
240. [Wydarzenia i Przepustka [limtochess_packselect_toggle_replace_ego] — tekst] E.G.O 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_toggle_replace_ego].content
   limit: do 120 znaków
   EN: Replace E.G.O
   PL: Wymiana E.G.O
241. [Wydarzenia i Przepustka [limtochess_ink_start_ego_resource_help] — tekst] E.G.O 자원은 다음 전투로 이월되지 않으며, 전투를 시작할 때마다 현재 편성에 따라 E.G.O 자원을 얻고 전투를 진행합니다.\n\nE.G.O 자원의 획득량은 편성한 인격 전원(대기 포함)의 스킬을 속성별로 센 수의 절반(소수점 버림)입니다.\n· 스킬 1·2·3은 각각 3·2·1개로 셉니다.\n· 수비 스킬은 세지 않습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_ink_start_ego_resource_help].content
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O resources do not carry over between battles. At the start of each battle, you gain E.G.O resources based on your current team.\n\nFor each Affinity, you gain half the total Skill count of that Affinity across all Identities in your formation, including Backup Identities (rounded down).\n · Skill 1, Skill 2, and Skill 3 count as 3, 2, and 1, respectively.\n · Defense Skills do not count.
   PL: Zasoby E.G.O nie przechodzą na następną walkę — przed każdą walką zyskujesz zasoby E.G.O stosownie do obecnego składu.\n\nZyskujesz połowę łącznej liczby Umiejętności danego Grzechu wszystkich Tożsamości w składzie, włącznie z Rezerwą (w dół).\n· Umiejętności 1, 2 i 3 liczą się odpowiednio jako 3, 2 i 1.\n· Umiejętności obrony się nie liczą.
242. [Wydarzenia i Przepustka [limtochess_pass_weekly_max_limit] — tekst] 주간 획득 한도
   źródło: LimtochessUI.json :: dataList[id=limtochess_pass_weekly_max_limit].content
   limit: do 120 znaków
   EN: Weekly Pass EXP Limit
   PL: Tygodniowy limit PD Przepustki
243. [Wydarzenia i Przepustka [limtochess_beta_desc_at_all] — tekst] ※ BETA — 베타 기간 중에는 도상구축의 진행 방식과 화면이 달라질 수 있습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_beta_desc_at_all].content
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
244. [Wydarzenia i Przepustka [limtochess_buildpower_line_change] — tekst] 구축력 {0} → {1} ({2})
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_line_change].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Craftpower {0} → {1} ({2})
   PL: Siła Konstrukcji {0} → {1} ({2})
245. [Wydarzenia i Przepustka [limtochess_buildpower_line_range] — tekst] 구축력 {0} → {1} ~ {2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_line_range].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Craftpower {0} → {1} ~ {2}
   PL: Siła Konstrukcji {0} → {1} ~ {2}
246. [Wydarzenia i Przepustka [limtochess_buildpower_roster_drop] — tekst] 제외 시 구축력 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_roster_drop].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Craftpower if removed: {0}
   PL: Siła Konstrukcji po usunięciu: {0}
247. [Wydarzenia i Przepustka [limtochess_buildpower_roster_result_pending] — tekst] 구축력 영입 후 {0} → 제외 후 ?
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_roster_result_pending].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Craftpower: {0} after recruitment → ? after removal
   PL: Siła Konstrukcji: {0} po werbunku → ? po usunięciu
248. [Wydarzenia i Przepustka [limtochess_buildpower_roster_result] — tekst] 구축력 영입 후 {0} → 제외 후 {1} ({2})
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_roster_result].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Craftpower: {0} after recruitment → {1} after removal ({2})
   PL: Siła Konstrukcji: {0} po werbunku → {1} po usunięciu ({2})
249. [Wydarzenia i Przepustka [limtochess_buildpower_roster_now] — tekst] 지금 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_buildpower_roster_now].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Current: {0}
   PL: Obecnie: {0}
250. [Wydarzenia i Przepustka [limtochess_event_effect_final_boss_weakness] — tekst] 최종 보스 → {0} {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_final_boss_weakness].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Final Boss → {0} {1}
   PL: Boss Finałowy → {0} {1}
251. [Wydarzenia i Przepustka [limtochess_event_boss_hidden_name] — tekst] ???
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_hidden_name].content
   limit: do 120 znaków
   EN: ???
   PL: ???
252. [Wydarzenia i Przepustka [limtochess_event_boss_weakness_jun] — tekst] [권장 속성 : 참격·탐식·오만]
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_weakness_jun].content
   limit: do 120 znaków
   EN: [Recommended: Slash · Gluttony · Pride]
   PL: [Zalecane Grzechy: Cięcie · Obżarstwo · Pycha]
253. [Wydarzenia i Przepustka [limtochess_event_boss_weakness_ricardo] — tekst] [권장 속성 : 타격·나태·질투]
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_weakness_ricardo].content
   limit: do 120 znaków
   EN: [Recommended: Blunt · Sloth · Envy]
   PL: [Zalecane Grzechy: Obuch · Lenistwo · Zawiść]
254. [Wydarzenia i Przepustka [limtochess_event_boss_weakness_cleaners] — tekst] [권장 속성 : 관통·색욕·오만]
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_weakness_cleaners].content
   limit: do 120 znaków
   EN: [Recommended: Pierce · Lust · Pride]
   PL: [Zalecane Grzechy: Kłucie · Żądza · Pycha]
255. [Wydarzenia i Przepustka [limtochess_event_boss_weakness_alley] — tekst] [권장 속성 : 타격·나태·오만]
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_weakness_alley].content
   limit: do 120 znaków
   EN: [Recommended: Blunt · Sloth · Pride]
   PL: [Zalecane Grzechy: Obuch · Lenistwo · Pycha]
256. [Wydarzenia i Przepustka [limtochess_event_boss_weakness_blackcloud] — tekst] [권장 속성 : 참격·오만]
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_weakness_blackcloud].content
   limit: do 120 znaków
   EN: [Recommended: Slash · Pride]
   PL: [Zalecane Grzechy: Cięcie · Pycha]
257. [Wydarzenia i Przepustka [limtochess_pass_level_up_popup_title] — tekst] 패스 레벨 상승
   źródło: LimtochessUI.json :: dataList[id=limtochess_pass_level_up_popup_title].content
   limit: do 120 znaków
   EN: Pass Level Up
   PL: Poziom Passu podniesiony
258. [Wydarzenia i Przepustka [limtochess_pass_level_up_popup_name] — tekst] 도상구축 패스
   źródło: LimtochessUI.json :: dataList[id=limtochess_pass_level_up_popup_name].content
   limit: do 120 znaków
   EN: Schemacraft Pass
   PL: Przepustka Konstrukcji Schematów

## Wydarzenia i Przepustka: NightCleanUpEvent
- plik gry: `NightCleanUpEvent.json`

259. [Wydarzenia i Przepustka [night_clean_up_stage_button_default] — tekst] 스테이지
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_stage_button_default].content
   limit: do 120 znaków
   EN: Stages
   PL: Etap
260. [Wydarzenia i Przepustka [night_clean_up_stage_button_locked] — tekst] 7.5-14 클리어 시 개방
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_stage_button_locked].content
   limit: do 120 znaków
   EN: Clear 7.5-14 to Unlock
   PL: Odblokowanie po ukończeniu 7.5-14
261. [Wydarzenia i Przepustka [night_clean_up_storybutton_default] — tekst] 상영관 이동
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_storybutton_default].content
   limit: do 120 znaków
   EN: To Theater
   PL: Do Teatru
262. [Wydarzenia i Przepustka [night_clean_up_storybutton_start] — tekst] <size=75%>이벤트 첫 번째 이야기\n감상 시 개방</size>
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_storybutton_start].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=75%>, </size>, \n
   EN: <size=75%>View the 1st event Story Stage \nto Unlock</size>
   PL: <size=75%>Odblokowanie po obejrzeniu pierwszej\nfabuły wydarzenia</size>
263. [Wydarzenia i Przepustka [night_clean_up_stage_button_end_event] — tekst] 이벤트 기간 종료
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_stage_button_end_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Zakończenie okresu wydarzenia
264. [Wydarzenia i Przepustka [night_clean_up_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_bonus_popup_title].content
   limit: do 120 znaków
   EN: Event Bonus Units
   PL: Jednostki premiowane w wydarzeniu
265. [Wydarzenia i Przepustka [night_clean_up_bonusUIDesc] — tekst] 이벤트 기간 동안 해당 인격 편성 시, <color=#625aff>[청소부 액체 연료통]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#625aff>120%</color>까지 적용됩니다.
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_bonusUIDesc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#625aff>, </color>, \n
   EN: During the event period, deploying the following Identities on your team will\nboost the amount of <color=#625aff>[Sweeper Fuel Cylinder]</color> earned.\nYou can earn a maximum of <color=#625aff>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości, zwiększasz zdobywanie <color=#625aff>[Kanistrów Płynnego Paliwa Sprzątacza]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#625aff>120%</color>.
266. [Wydarzenia i Przepustka [night_clean_up_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_scrap_guide_title].content
   limit: do 120 znaków
   EN: Event Currency Guide
   PL: Informacje o walucie wydarzenia
267. [Wydarzenia i Przepustka [night_clean_up_scrap_guide_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어,\n거울 던전 클리어를 통해 <color=#625aff>[청소부 액체 연료통]</color>을 획득할 수 있으며,\n낮은 확률로 <color=#625aff>[특대형 액체 연료통]</color>을 추가로 획득할 수 있습니다.\n\n<color=#625aff>[특대형 액체 연료통]</color>은 획득 즉시, <color=#625aff>[청소부 액체 연료통]</color> 20개로 전환됩니다.
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_scrap_guide_desc].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#625aff>, </color>, \n
   EN: You can obtain <color=#625aff>[Sweeper Fuel Cylinder]</color> from first-time Event/Main Story Stages completions, or by clearing the Mirror Dungeon.\nYou also have a small chance to obtain <color=#625aff>[Sweeper Fuel Tank]</color> in the process.\n\n<color=#625aff>[Sweeper Fuel Tank]</color> is immediately converted to 20 <color=#625aff>[Sweeper Fuel Cylinder]</color> upon acquisition.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#625aff>[Kanister Płynnego Paliwa Sprzątacza]</color>, a z pewnym prawdopodobieństwem dodatkowo <color=#625aff>[Wielki Zbiornik Płynnego Paliwa]</color>.\n\n<color=#625aff>[Wielki Zbiornik Płynnego Paliwa]</color> od razu zamienia się na 20 <color=#625aff>[Kanistrów Płynnego Paliwa Sprzątacza]</color>.
268. [Wydarzenia i Przepustka [nightcleanup_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#e50000>[청소부 액체 연료통]</color>을 획득할 수 있습니다.\n\n<color=#e50000>[보상 교환]</color>창에서 <color=#e50000>[청소부 액체 연료통]</color>을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: NightCleanUpEvent.json :: dataList[id=nightcleanup_reward_popup_desc].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#e50000>, </color>, \n
   EN: Earn <color=#e50000>[Sweeper Fuel Cylinder]</color> via the following methods:\nEvent Stage clears, Mirror Dungeon clears,\nand Main Story Stage first-time clears.\n\nIn the <color=#e50000>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#e50000>[Sweeper Fuel Cylinder]</color> you have collected.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#e50000>[Kanister Płynnego Paliwa Sprzątacza]</color>.\n\nW oknie <color=#e50000>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#e50000>[Kanistry Płynnego Paliwa Sprzątacza]</color>.
269. [Wydarzenia i Przepustka [nightCleanUp_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: NightCleanUpEvent.json :: dataList[id=nightCleanUp_reward_popup_num_of_owned_items].content
   limit: do 120 znaków
   EN: Items Owned
   PL: Liczba posiadanych przedmiotów
270. [Wydarzenia i Przepustka [night_clean_up_rewardShopButton] — tekst] 보상 교환
   źródło: NightCleanUpEvent.json :: dataList[id=night_clean_up_rewardShopButton].content
   limit: do 120 znaków
   EN: Reward Exchange
   PL: Wymiana nagród

## Wydarzenia i Przepustka: PilgrimageUIText
- plik gry: `PilgrimageUIText.json`

271. [Wydarzenia i Przepustka [pilgrimage_bonus_preview] — tekst] 이벤트 특화 대상
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_bonus_preview].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Wydarzenia i Przepustka [pilgrimage_stage_button] — tekst] 스테이지
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_stage_button].content
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Wydarzenia i Przepustka [pilgrimage_theater_button] — tekst] 상영관
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_theater_button].content
   limit: do 120 znaków
   EN: Theater
   PL: Teatr
274. [Wydarzenia i Przepustka [pilgrimage_reward_button] — tekst] 보상 교환
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_reward_button].content
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Wydarzenia i Przepustka [pilgrimage_reward_popup_desc] — tekst] 이벤트 스테이지와 던전, 주요 이야기\n최초 클리어, 거울 던전 클리어를 통해\n<color=#acb2ff>[시테러 표본]</color>을 획득할 수 있습니다.\n\n<color=#acb2ff>[보상 교환]</color> 창에서 <color=#acb2ff>[시테러 표본]</color>을\n지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_reward_popup_desc].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#acb2ff>, </color>, \n
   EN: Earn <color=#acb2ff>[Sea Terror Sample]</color> via the following methods:\nEvent Stage & Dungeon clears, Mirror Dungeon clears,\nand Main Story Stage & Dungeon first-time clears.\n\nIn the <color=#acb2ff>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#acb2ff>[Sea Terror Sample]</color> you have collected.
   PL: Zdobądź <color=#acb2ff>[Próbkę Morskiego Koszmaru]</color> przez:\npierwsze ukończenia etapów i lochów wydarzenia,\netapów Głównej Opowieści oraz Lustrzane Lochy.\n\nW oknie <color=#acb2ff>[Wymiany nagród]</color> możesz kupić różne nagrody\nza zebrane <color=#acb2ff>[Próbki Morskiego Koszmaru]</color>.
276. [Wydarzenia i Przepustka [pilgrimage_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_scrap_guide_title].content
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Wydarzenia i Przepustka [pilgrimage_rewardpage_desc] — tekst] 이벤트 스테이지를 클리어할 때마다 <color=#acb2ff>[시테러 표본]</color>을 획득할 수 있습니다. 이외에도 주요 이야기\n스테이지를 최초로 클리어하거나 거울 던전 클리어 시, <color=#acb2ff>[시테러 표본]</color>을 획득할 수 있습니다.\n\n이벤트와 주요 이야기의 스테이지 또는 거울 던전을 클리어하면 낮은 확률로 <color=#acb2ff>[빛나는 시테러 표본]</color>을 획득할 수 있으며, <color=#acb2ff>[빛나는 시테러 표본]</color>은 획득 즉시 <color=#acb2ff>[시테러 표본]</color> 20개로 전환됩니다.\n\n<color=#acb2ff>[보상 교환]</color> 창에서 <color=#acb2ff>[시테러 표본]</color>을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_rewardpage_desc].content
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#acb2ff>, </color>, \n
   EN: During the event, you can earn <color=#acb2ff>[Sea Terror Sample]</color> by clearing event Stages. You can also obtain <color=#acb2ff>[Sea Terror Sample]</color> by clearing Main Story Stages for the first time, or by clearing the Mirror Dungeon.\n\nRarely, you may obtain <color=#acb2ff>[Luminous Sea Terror Sample]</color> from clearing Event Stages, Main Story Stages, or Mirror Dungeons,\nand <color=#acb2ff>[Luminous Sea Terror Sample]</color> is automatically converted to 20 <color=#acb2ff>[Sea Terror Sample]</color> upon acquisition.\n\nIn the <color=#acb2ff>[Reward Exchange]</color> window, you can purchase various rewards by spending <color=#acb2ff>[Sea Terror Sample]</color> you have collected.
   PL: Ukończoną każdą etap wydarzenia, zdobywasz <color=#acb2ff>[Próbkę Morskiego Koszmaru]</color>. Zdobędziesz ją także za pierwsze ukończenia etapów Głównej Opowieści albo Lustrzane Lochy.\n\nUkończywszy etapy wydarzenia lub Głównej Opowieści albo Lustrzane Lochy, z pewnym prawdopodobieństwem zdobędziesz <color=#acb2ff>[Lśniącą Próbkę Morskiego Koszmaru]</color>, która od razu zamienia się na 20 <color=#acb2ff>[Próbek Morskiego Koszmaru]</color>.\n\nW oknie <color=#acb2ff>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#acb2ff>[Próbki Morskiego Koszmaru]</color>.
278. [Wydarzenia i Przepustka [pilgrimage_bonusUI_Desc] — tekst] 이벤트 기간 동안 해당 E.G.O 편성 시, <color=#acb2ff>[시테러 표본]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#acb2ff>120%</color>까지 적용됩니다.
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_bonusUI_Desc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#acb2ff>, </color>, \n
   EN: During the event period, deploying the following E.G.O on your team will\nboost the amount of <color=#acb2ff>[Sea Terror Sample]</color> earned.\nYou can earn a maximum of <color=#acb2ff>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane E.G.O, zwiększasz zdobywanie <color=#acb2ff>[Próbek Morskiego Koszmaru]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#acb2ff>120%</color>.
279. [Wydarzenia i Przepustka [pilgrimage_warning_spoiler] — tekst] 주요 이야기 8.5장 절차탁춘 이후의 내용을 담고 있습니다. 스토리를 감상하시겠습니까?
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_warning_spoiler].content
   limit: do 140 znaków
   EN: This story takes place after Intervallo VI - Spring Cultivation. Would you like to view the story anyway?
   PL: Ta opowieść rozgrywa się po Intervallo VI - Wiosenny Szlif (rozdz. 8.5). Obejrzeć mimo wszystko?
280. [Wydarzenia i Przepustka [pilgrimage_hard_stage_clear_desc] — tekst] ※ 스테이지 하드 난이도로 클리어 시, 해당 스테이지의\n노말 난이도도 클리어한 것으로 적용됩니다.
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_hard_stage_clear_desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Clearing via Hard difficulty Stages will automatically\nclear the corresponding Normal difficulty Stages as well.
   PL: ※ Ukończenie etapu na Poziomie Trudnym liczy się także jako ukończenie\nodpowiedniego etapu na Poziomie Normalnym.
281. [Wydarzenia i Przepustka [pilgrimage_chapter_progress_reward_desc] — tekst] ※ 이벤트 종료 이후에는 진행도 보상을 획득할 수 없으므로 미리 수령하시기 바랍니다.
   źródło: PilgrimageUIText.json :: dataList[id=pilgrimage_chapter_progress_reward_desc].content
   limit: do 140 znaków
   EN: ※ Please claim your Progress rewards ahead of time as they will become unavailable after the Event is over.
   PL: ※ Po zakończeniu wydarzenia nagrody za postęp przepadną — odbierz je z wyprzedzeniem.

## Wydarzenia i Przepustka: ProjectGS
- plik gry: `ProjectGS.json`

282. [Wydarzenia i Przepustka [project_gs_button_label_open_lesson_ui] — tekst] 수업 선택
   źródło: ProjectGS.json :: dataList[id=project_gs_button_label_open_lesson_ui].content
   limit: do 120 znaków
   EN: Select Class
   PL: Wybór zajęć
283. [Wydarzenia i Przepustka [project_gs_button_label_progress_lesson] — tekst] 수업 시작
   źródło: ProjectGS.json :: dataList[id=project_gs_button_label_progress_lesson].content
   limit: do 120 znaków
   EN: Begin Class
   PL: Rozpocznij zajęcia
284. [Wydarzenia i Przepustka [project_gs_button_label_open_battle] — tekst] 중간 심사
   źródło: ProjectGS.json :: dataList[id=project_gs_button_label_open_battle].content
   limit: do 120 znaków
   EN: Midterm
   PL: Egzamin Środkowy
285. [Wydarzenia i Przepustka [project_gs_stats_wisdom] — tekst] 지
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_wisdom].content
   limit: do 120 znaków
   EN: Zhi
   PL: Zhi
286. [Wydarzenia i Przepustka [project_gs_stats_courage] — tekst] 용
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_courage].content
   limit: do 120 znaków
   EN: Yong
   PL: Yong
287. [Wydarzenia i Przepustka [project_gs_stats_benevolence] — tekst] 인
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_benevolence].content
   limit: do 120 znaków
   EN: Ren
   PL: Ren
288. [Wydarzenia i Przepustka [project_gs_stats_wisdom_with_char] — tekst] 지(智)
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_wisdom_with_char].content
   limit: do 120 znaków
   EN: Zhi (智)
   PL: Zhi (智)
289. [Wydarzenia i Przepustka [project_gs_stats_courage_with_char] — tekst] 용(勇)
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_courage_with_char].content
   limit: do 120 znaków
   EN: Yong (勇)
   PL: Yong (勇)
290. [Wydarzenia i Przepustka [project_gs_stats_benevolence_with_char] — tekst] 인(仁)
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_benevolence_with_char].content
   limit: do 120 znaków
   EN: Ren (仁)
   PL: Ren (仁)
291. [Wydarzenia i Przepustka [project_gs_condition] — tekst] 컨디션
   źródło: ProjectGS.json :: dataList[id=project_gs_condition].content
   limit: do 120 znaków
   EN: Morale
   PL: Kondycja
292. [Wydarzenia i Przepustka [project_gs_day] — tekst] {0}일 차
   źródło: ProjectGS.json :: dataList[id=project_gs_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Day {0}
   PL: Dzień {0}
293. [Wydarzenia i Przepustka [project_gs_schedule_label] — tekst] 일정표
   źródło: ProjectGS.json :: dataList[id=project_gs_schedule_label].content
   limit: do 120 znaków
   EN: Class Schedule
   PL: Plan Zajęć
294. [Wydarzenia i Przepustka [project_gs_desc_select_lesson] — tekst] 수업을 선택해주세요
   źródło: ProjectGS.json :: dataList[id=project_gs_desc_select_lesson].content
   limit: do 120 znaków
   EN: Select a Class for this timeslot
   PL: Wybierz zajęcia dla tego bloku
295. [Wydarzenia i Przepustka [project_gs_condition_highest] — tekst] 최상
   źródło: ProjectGS.json :: dataList[id=project_gs_condition_highest].content
   limit: do 120 znaków
   EN: Tip-top
   PL: Znakomita
296. [Wydarzenia i Przepustka [project_gs_condition_high] — tekst] 상
   źródło: ProjectGS.json :: dataList[id=project_gs_condition_high].content
   limit: do 120 znaków
   EN: Good
   PL: Dobra
297. [Wydarzenia i Przepustka [project_gs_condition_medium] — tekst] 양호
   źródło: ProjectGS.json :: dataList[id=project_gs_condition_medium].content
   limit: do 120 znaków
   EN: Okay
   PL: Przyzwoita
298. [Wydarzenia i Przepustka [project_gs_condition_low] — tekst] 낮음
   źródło: ProjectGS.json :: dataList[id=project_gs_condition_low].content
   limit: do 120 znaków
   EN: Bad
   PL: Niska
299. [Wydarzenia i Przepustka [project_gs_condition_lowest] — tekst] 최하
   źródło: ProjectGS.json :: dataList[id=project_gs_condition_lowest].content
   limit: do 120 znaków
   EN: Awful
   PL: Krytyczna
300. [Wydarzenia i Przepustka [project_gs_title_grow_up] — tekst] 육성
   źródło: ProjectGS.json :: dataList[id=project_gs_title_grow_up].content
   limit: do 120 znaków
   EN: Cultivation
   PL: Uprawiaj
301. [Wydarzenia i Przepustka [project_gs_title_schedule] — tekst] 시간표 선택
   źródło: ProjectGS.json :: dataList[id=project_gs_title_schedule].content
   limit: do 120 znaków
   EN: Select Schedule
   PL: Wybierz Plan Zajęć
302. [Wydarzenia i Przepustka [project_gs_lesson_level_1] — tekst] 초급
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_level_1].content
   limit: do 120 znaków
   EN: Novice
   PL: Podstawowy
303. [Wydarzenia i Przepustka [project_gs_lesson_level_2] — tekst] 중급
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_level_2].content
   limit: do 120 znaków
   EN: Expert
   PL: Średniozaawansowany
304. [Wydarzenia i Przepustka [project_gs_lesson_level_3] — tekst] 고급
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_level_3].content
   limit: do 120 znaków
   EN: Master
   PL: Zaawansowany
305. [Wydarzenia i Przepustka [project_gs_jia_xichun_name] — tekst] 가시춘
   źródło: ProjectGS.json :: dataList[id=project_gs_jia_xichun_name].content
   limit: do 120 znaków
   EN: Jia Xichun
   PL: Jia Xichun
306. [Wydarzenia i Przepustka [project_gs_sinclair_name] — tekst] 싱클레어
   źródło: ProjectGS.json :: dataList[id=project_gs_sinclair_name].content
   limit: do 120 znaków
   EN: Sinclair
   PL: Sinclair
307. [Wydarzenia i Przepustka [project_gs_exp] — tekst] 경험치
   źródło: ProjectGS.json :: dataList[id=project_gs_exp].content
   limit: do 120 znaków
   EN: EXP
   PL: PD
308. [Wydarzenia i Przepustka [project_gs_combo] — tekst] 콤보
   źródło: ProjectGS.json :: dataList[id=project_gs_combo].content
   limit: do 120 znaków
   EN: Combo
   PL: Kombinacje
309. [Wydarzenia i Przepustka [project_gs_fixed_lesson] — tekst] 고정 수업
   źródło: ProjectGS.json :: dataList[id=project_gs_fixed_lesson].content
   limit: do 120 znaków
   EN: Mandatory Class
   PL: Zajęcia Obowiązkowe
310. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_1_critical_success] — tekst] 내면의 나와 대화할 수 있는 소중한 시간이었다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_1_critical_success].content
   limit: do 120 znaków
   EN: I had a very precious time learning to converse with my inner self!!
   PL: To był bezcenny czas na rozmowę z sobą samego!!
311. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_1_success] — tekst] 거울을 들여다보면서 조금 더 나답게 말하는 법을 깨달았다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_1_success].content
   limit: do 120 znaków
   EN: I learned how to be more true to myself by looking into the mirror!
   PL: Wpatrując się w lustro, odkryłem, jak mówić bardziej po swojemu!
312. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_1_normal] — tekst] 그럭저럭 스스로를 돌아볼 수 있었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_1_normal].content
   limit: do 120 znaków
   EN: Had a so-so time reflecting upon myself.
   PL: Najdążyłem na siebie jako tak — bez fajerwerków.
313. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_1_failure] — tekst] 계속해서 거울을 들여다보니 순간 내 모습이 어색하게 느껴졌다… 무서워져서 수업에 집중할 수 없었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_1_failure].content
   limit: do 200 znaków
   EN: After staring into the mirror for a while, my reflection suddenly felt so... unfamiliar. Fear gripped me, and I couldn't focus on the rest of the class.
   PL: Po dłuższym wpatrywaniu się w lustro moje odbicie nagle wydało mi się obce… Strach odebrał mi koncentrację na reszcie zajęć.
314. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_1_critical_failure] — tekst] 거울 속의 나는 나인가 아니면 또 다른 누구인가… 거울만 하염없이 바라보다 수업이 끝났다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_1_critical_failure].content
   limit: do 180 znaków
   EN: Is the self in the mirror my reflection, or another being entirely...? The class ended after a prolonged blank stare into the mirror.
   PL: Czy to ja w lustrze, czy ktoś zupełnie inny… Zajęcia minęły na bezszelestnym wpatrywaniu się w lustro.
315. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_2_critical_success] — tekst] 배운 기술을 바탕으로 파우스트가 가져온 설계도 속 기계의 모조품을 만들어냈다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_2_critical_success].content
   limit: do 130 znaków
   EN: Based on the skills I learned, I managed to recreate the model of a machine from Faust's blueprint!
   PL: Na podstawie zdobytej wiedzy odtworzyłem model maszyny z projektu, który przyniosła Faust!!
316. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_2_success] — tekst] 구 H사에 대한 기술의 세세한 작동 원리까지 깨칠 수 있었다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_2_success].content
   limit: do 120 znaków
   EN: Managed to learn various, detailed mechanical fundamentals about old H Corp. technology!
   PL: Pochłonąłem nawet drobiazgowe zasady działania technologii starej Korp. H!
317. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_2_normal] — tekst] 그럭저럭 여러 기술과 공학에 대한 지식이 늘었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_2_normal].content
   limit: do 120 znaków
   EN: I had a so-so time learning various technological and engineering knowledge.
   PL: Kilka technicznych i inżynierskich wiadomości przybyło — jako tak.
318. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_2_failure] — tekst] 공학에 관련된 유익한 지식을 여럿 배웠지만, 복습하지 않으면 곧 잊어버릴 것 같다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_2_failure].content
   limit: do 200 znaków
   EN: I learned various things about engineering, but they're all kind of hazy... I'm going to have to review this material later, or I'm gonna forget all of it.
   PL: Nauczyłem się wielu pożytecznych rzeczy o inżynierii, ale bez powtórki szybko wszystko wyparuje.
319. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_2_critical_failure] — tekst] 진도가 너무 빠르다… 파우스트의 강의 대부분을 이해하지 못했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_2_critical_failure].content
   limit: do 120 znaków
   EN: The class is moving way too fast... Most of Faust's class went completely over my head.
   PL: Tempo aż za szybkie… Większości wykładu Faust nie zrozumiałem.
320. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_3_critical_success] — tekst] 해결사들의 가슴 벅찬 모험담에 숨 쉬는 것조차 잊고 빠져들었다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_3_critical_success].content
   limit: do 140 znaków
   EN: I was completely absorbed in the exhilarating tales of Fixers! I even forgot to breathe at one point!
   PL: Zachwycające opowieści Fikserów wchłonęły mnie całkowicie — zapomniałem nawet oddychać!!
321. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_3_success] — tekst] 흥미진진한 모험담을 듣다 보니, 시간 가는 줄 몰랐다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_3_success].content
   limit: do 120 znaków
   EN: Time certainly flies when hearing the tales of exciting adventures!
   PL: Słuchając porywających opowieści o przygodach, nie zauważyłem, jak upłynął czas!
322. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_3_normal] — tekst] 그럭저럭 해결사에 대한 지식이 알차게 쌓여 간다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_3_normal].content
   limit: do 120 znaków
   EN: I had a so-so time learning about the Fixers and their deeds.
   PL: Wiedza o Fikserach i ich wyczynach rosła — jako tak, ale konkretnie.
323. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_3_failure] — tekst] 오늘 모험담은 조금 지루했지만, 끝까지 귀 기울여 들었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_3_failure].content
   limit: do 130 znaków
   EN: Today's tale of adventures was a bit boring, but I managed to pay attention through the whole thing.
   PL: Dzisiejsza opowieść była trochę nudna, ale wysłuchałem jej do końca.
324. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_3_critical_failure] — tekst] 이미 몇 번이나 들었던 익숙한 모험담을 수업 시간 내내 다시 들었다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_3_critical_failure].content
   limit: do 130 znaków
   EN: The class consisted of listening to the same adventure I'd already heard many times in the past...
   PL: Całe zajęcia słuchałem tej samej, nie raz już opowiadanej przygody…
325. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_4_critical_success] — tekst] 멋진 모험에 성공했다. 다음 플레이… 수업이 기다려진다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_4_critical_success].content
   limit: do 120 znaków
   EN: What a wonderful adventure that was. I'm so excited for our next session—I mean, class!!
   PL: Świetna przygoda! Nie mogę się doczekać kolejnej sesji — to znaczy, zajęć!!
326. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_4_success] — tekst] 모험 속 고난을 싱클레어와 힘을 합쳐 재치 있게 해결했다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_4_success].content
   limit: do 140 znaków
   EN: Worked with Sinclair to come up with creative solutions to all kinds of trials we faced in the adventure!
   PL: Siłami Sinclaira sprytnie rozwiązaliśmy wszystkie próby stojące na drodze przygody!
327. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_4_normal] — tekst] 그럭저럭 괜찮은 모험을 즐겼다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_4_normal].content
   limit: do 120 znaków
   EN: I had a so-so time with today's adventure.
   PL: Dzisiejsza przygoda była jako tak — dobra zabawa.
328. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_4_failure] — tekst] 즐거운 모험이었지만, 진행이 지지부진했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_4_failure].content
   limit: do 120 znaków
   EN: Today's adventure was fun, but we barely made any main quest progress.
   PL: Przygoda fajna, ale ciągnęła się w miejscu.
329. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_4_critical_failure] — tekst] 강호유람기 속 세가들이 전멸했다… 진상은 어둠에 묻혔다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_4_critical_failure].content
   limit: do 120 znaków
   EN: Total clan kill... Thus the truth of the realm is now lost to darkness...
   PL: Klany z Podróży po Jianghu wyginęły w całości… Prawda spowija ją ciemność…
330. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_5_critical_success] — tekst] 사병들의 고충을 이해하고, 전장의 흐름을 전부 꿰뚫을 수 있게 되었다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_5_critical_success].content
   limit: do 170 znaków
   EN: Managed to understand the troubles most foot-soldiers go through, and learned to get a better idea of the flow of a battlefield!
   PL: Zrozumiałem dylematy zwykłych żołnierzy i nauczyłem się wyczuwać tok całego pola bitwy!!
331. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_5_success] — tekst] 시가전과 참호전을 구분해서 설명할 수 있을 것 같다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_5_success].content
   limit: do 120 znaków
   EN: Now I know enough about urban and trench warfare to give an explanation of my own!
   PL: Teraz umiem samodzielnie wyjaśnić różnice między walką miejską a wojną okopową!
332. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_5_normal] — tekst] 그럭저럭 날개 전쟁을 이해했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_5_normal].content
   limit: do 120 znaków
   EN: I've gained a so-so understanding of War of the Wings.
   PL: Wojnę Skrzydeł rozumiem — jako tak.
333. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_5_failure] — tekst] 날개 전쟁의 설명보다 그레고르의 과거 이야기에 심취해 버렸다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_5_failure].content
   limit: do 170 znaków
   EN: I ended up becoming completely absorbed in hearing about Gregor's past, instead of focusing on his lectures on the War of the Wings.
   PL: Zamiast słuchać wykładu o Wojnie Skrzydeł, wchłonęło mnie słuchanie o przeszłości Gregora.
334. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_5_critical_failure] — tekst] 그레고르의 침울함에 너무 공감한 나머지, 슬퍼져서 수업을 거의 듣지 못했다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_5_critical_failure].content
   limit: do 140 znaków
   EN: I ended up sympathizing too hard with Gregor's sadness to the point I couldn't focus in class anymore...
   PL: Zbyt mocno utożsamiłem się z smutkiem Gregora — prawie niczego się nie nauczyłem…
335. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_6_critical_success] — tekst] 홍루가 준비한 암살 수법을 모두 간파했다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_6_critical_success].content
   limit: do 120 znaków
   EN: I saw right through every assassination method Hong Lu prepared!!
   PL: Prześwietliłem wszystkie metody skrytobójcze, jakie przygotował Hong Lu!!
336. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_6_success] — tekst] 홍루와 대옥이 풍기는 분위기로, 사발의 미세한 차이를 알아차렸다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_6_success].content
   limit: do 130 znaków
   EN: I managed to tell the difference between the bowls by reading Hong Lu and Daiyu's subtle tells!
   PL: Czytając subtelne gesty Hong Lu i Daiyu, rozpoznałem różnice między czarami!
337. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_6_normal] — tekst] 그럭저럭 분위기와 전조 현상을 읽는 훈련을 반복했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_6_normal].content
   limit: do 120 znaków
   EN: I had a so-so time with the repetitive practices on looking for tells.
   PL: Powtarzałem trening odczytywania zapowiedzi i nastroju — jako tak.
338. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_6_failure] — tekst] 감이 잡히는 것 같으면서도, 아리송한 느낌이다. 절반 정도의 독 사발을 구분해 냈다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_6_failure].content
   limit: do 150 znaków
   EN: I still don't quite understand how this "hunch" thing works... Still, I managed to get about half of them right.
   PL: Niby coś czuję, a niby nie. Zgadłem około połowy zatrutych czar.
339. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_6_critical_failure] — tekst] 고르는 족족 독이 든 사발이었다. 오늘은 감이 좋지 않을지도…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_6_critical_failure].content
   limit: do 120 znaków
   EN: Literally every bowl I picked contained poison. Today just might not be my day...
   PL: Każydz czara, którą wybrałem, była zatruta. Może dziś po prostu nie mój dzień…
340. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_7_critical_success] — tekst] 수업 끝.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_7_critical_success].content
   limit: do 120 znaków
   EN: Class over.
   PL: Koniec zajęć.
341. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_7_success] — tekst] 수업 완료.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_7_success].content
   limit: do 120 znaków
   EN: Took the class.
   PL: Zajęcia odbyte.
342. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_7_normal] — tekst] 그럭저럭 수업을 잘 마쳤다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_7_normal].content
   limit: do 120 znaków
   EN: I had a so-so time with the class.
   PL: Zajęcia zakończyłem jako tak.
343. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_7_failure] — tekst] 불필요한 말을 줄인다는 건 너무 어려운 일이다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_7_failure].content
   limit: do 120 znaków
   EN: Why is it so hard to keep things concise...?
   PL: Dlaczego zwięzłość jest tak trudna…
344. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_7_critical_failure] — tekst] 말을 아끼긴 커녕, 굳이 말하지 않아도 될 불만까지 모두 말하고 나서야 수업이 끝났다. 다음에는 꼭 필요한 말만 하기로 다짐했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_7_critical_failure].content
   limit: do 280 znaków
   EN: So much for saving unnecessary words! I ended up telling every little gripe I had with everything until the class ended. Next time, I'm going to say only what needs saying. I made a promise to myself to do just that.
   PL: Zamiast oszczędzać słowa, wylałem wszystkie zaległe narzekania — zajęcia zakończyły się dopiero wtedy. Następnym razem powiem tylko to, co konieczne. Przyrzekłem sobie to.
345. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_8_critical_success] — tekst] 몇 마디의 말만으로 상대방이 새파랗게 얼굴이 질리더니 모든 것을 털어놓았다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_8_critical_success].content
   limit: do 120 znaków
   EN: With only a few words, I managed to "convince" the target to spill all the beans!
   PL: Kilka słów wystarczyło, żeby „przekonać” cel, że wylał wszystko!!
346. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_8_success] — tekst] 상대방의 간담을 서늘하게 만들 만한 협박 몇 가지를 기억했다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_8_success].content
   limit: do 120 znaków
   EN: Learned some threats and intimidating expressions I could use to frighten the target!
   PL: Zapamiętałem kilka gróźb i groźnych sformułowań, żeby przerazić cel!
347. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_8_normal] — tekst] 그럭저럭 필요한 정보를 끄집어낼 수 있었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_8_normal].content
   limit: do 120 znaków
   EN: Had a so-so result on learning more intel from the target.
   PL: Wyciągnąłem od celu potrzebne informacje — jako tak.
348. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_8_failure] — tekst] 방법은 터득했지만, 상대방에게 모진 말을 해야 할 때마다 망설여버렸다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_8_failure].content
   limit: do 140 znaków
   EN: I now know how to interrogate, but every time I had to say something awful to the target, I hesitated.
   PL: Metodę mam, ale za każdym razem, gdy trzeba było powiedzieć coś ciężkiego, wahałem się.
349. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_8_critical_failure] — tekst] 오히려 상대방에게 말려들어, 나의 정보만 상대방에게 줄줄 읊었다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_8_critical_failure].content
   limit: do 120 znaków
   EN: I don't know how it happened, but the target somehow convinced <i>me</i> to spill all my beans...
   PL: Wręcz przeciwnie — to cel mnie wciągnął i ja wyleciałem z informacjami…
350. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_9_critical_success] — tekst] 완. 수. (완벽한 수업)!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_9_critical_success].content
   limit: do 120 znaków
   EN: F.C. (Flawless Class)!!
   PL: W. Z. (Wzorowe Zajęcia)!!
351. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_9_success] — tekst] 동심으로 돌아가 아이들과 한껏 웃고 떠들었다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_9_success].content
   limit: do 120 znaków
   EN: Laughing and playing with children brought back fond memories of my own childhood!
   PL: Wróciłem myślami do dzieciństwa — z dziećmi śmiałem się i szalełem na zdrowie!
352. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_9_normal] — tekst] 그럭저럭 아이의 눈높이에 맞춘 대화법을 터득했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_9_normal].content
   limit: do 120 znaków
   EN: I gained a so-so level of knowledge on how to talk to children.
   PL: Zrozumiałem, jako tak, jak rozmawiać na poziomie dziecka.
353. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_9_failure] — tekst] 아이와 놀아주는 것도 좋지만… 그만 지쳐버렸다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_9_failure].content
   limit: do 120 znaków
   EN: Playing with children is all fine and good, but... it's also very draining.
   PL: Zabawa z dziećmi to fajna sprawa… ale mocno męczy.
354. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_9_critical_failure] — tekst] 아이를 울려버렸다… 눈앞이 깜깜해졌다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_9_critical_failure].content
   limit: do 120 znaków
   EN: I made the kid cry... oh no.
   PL: Doprowadziłem dziecko do płaczu… Robi mi się ciemno przed oczami.
355. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_10_critical_success] — tekst] 감추는 것을 넘어 필요한 표정을 짓는 법을 터득했다. 드디어 로쟈에게 일국을 따냈다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_10_critical_success].content
   limit: do 170 znaków
   EN: I didn't just learn how to hide my feelings... I learned how to make whatever expressions I want. Finally won a round against Rodya!
   PL: Nauczyłem się nie tylko ukrywać uczucia — potrafię już rysować sobie twarz, jaką chcę. W końcu wygrałem rundę z Rodion!!
356. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_10_success] — tekst] 표정 뿐 아니라, 다양한 제스처를 감출 수 있도록 로쟈와 여러 게임을 즐겼다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_10_success].content
   limit: do 170 znaków
   EN: By playing various games with Rodya, I didn't just learn how to hide my expressions... I learned how to hide my gesture tells, too!
   PL: Grając z Rodion w różne gry, nauczyłem się ukrywać nie tylko miny, ale i gesty!
357. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_10_normal] — tekst] 그럭저럭 감정이 표정에 드러나지 않게 숨기는 법을 배웠다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_10_normal].content
   limit: do 120 znaków
   EN: I had a so-so time learning to prevent my emotions from becoming too obvious.
   PL: Nauczyłem się — jako tak — nie obnażać emocji na twarzy.
358. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_10_failure] — tekst] 표정을 숨기려 노력해봤지만, 좋은 패가 들어왔을 때 올라간 입꼬리를 감추지 못했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_10_failure].content
   limit: do 170 znaków
   EN: I tried my best to keep a poker face, but I couldn't stop my lips from involuntarily smiling whenever I got the tiles I needed.
   PL: Starałem się zachować pokerową twarz, ale gdy przyszły dobre kafle, kąciki ust same się unosiły.
359. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_10_critical_failure] — tekst] 생각한 것이 표정에 모두 드러나 버렸다. 로쟈에게 탈탈 털리고 말았다…
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_10_critical_failure].content
   limit: do 120 znaków
   EN: Apparently, my expressions were extremely obvious. Rodya fleeced me...
   PL: Wszystko, co myślałem, pisało się po mojej twarzy. Rodion mnie wyprana z kasy…
360. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_11_critical_success] — tekst] 잡아먹을 것 같은 눈빛, 망설이지 않는 행동을 전부 체득했다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_11_critical_success].content
   limit: do 120 znaków
   EN: I learned the art of "mad dogging" and decisive action!
   PL: Przyswoiłem sztukę szczerzenia kłów i zdecydowanego działania!!
361. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_11_success] — tekst] 적을 어떻게 기선제압해야 할지 깨달을 수 있었다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_11_success].content
   limit: do 120 znaków
   EN: Gained an understanding of how I could break the enemy's morale!
   PL: Zrozumiałem, jak przeciągnąć na siebie morale wroga!
362. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_11_normal] — tekst] 그럭저럭 기분 좋게 땀을 흘렸다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_11_normal].content
   limit: do 120 znaków
   EN: Had a so-so time sweating things out.
   PL: Wygadzałem się — jako tak — z przyjemnością.
363. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_11_failure] — tekst] 몸의 움직임이 둔해져서 수업 내용의 절반 정도만 따라갈 수 있었다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_11_failure].content
   limit: do 120 znaków
   EN: I was too exhausted to fully keep up with the class.
   PL: Ciało zrobiło się powolne — nadążyłem za połową zajęć.
364. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_11_critical_failure] — tekst] 무기가 손에서 미끄러져서 히스클리프의 머리에 부딪혔다… 사과하는 데에 모든 수업 시간을 써버렸다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_11_critical_failure].content
   limit: do 160 znaków
   EN: The weapon slipped out of my hand and struck Heathcliff square in his head... I wasted the entire class time apologizing.
   PL: Broń mi wyślizgnęła się z ręki i trafiła Heathcliffa prosto w głowę… Całe zajęcia poszły na przepraszan-ie.
365. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_12_critical_success] — tekst] 상념을 떨쳐내고 투로에 모든 것을 담아 휘둘렀다. 보이지 않는 무언가를 가른 것만 같다!!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_12_critical_success].content
   limit: do 180 znaków
   EN: I emptied all distracting thoughts and let the flow of battle swing my weapon. I think I managed to cut through something invisible!!
   PL: Strąciłem wszystkie dystrakcje i wymierzyłem cios całym torem walki. Jakbym przeciął coś niewidzialnego!!
366. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_12_success] — tekst] 나를 제외한 모든 것을 무로 만들기 위해 명상했다. 어설프게나마 실마리가 잡혔다!
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_12_success].content
   limit: do 140 znaków
   EN: I meditated to empty everything except for the self. I'm still getting there, but I think I've got an idea!
   PL: Medytowałem, by sprowadzić do zera wszystko poza sobą. Ledwo się czuję, ale coś mi świta!
367. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_12_normal] — tekst] 그럭저럭 취수야객의 말들을 이해했다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_12_normal].content
   limit: do 120 znaków
   EN: I think I've gained a so-so understanding of the Night Drifter's teachings.
   PL: Nauki Pijanicy Nocnego Wędrowca zrozumiałem — jako tak.
368. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_12_failure] — tekst] 취수야객의 동작을 이해하는 것은 너무 어렵다… 그리고 진동하는 술 냄새에 머리가 어지럽다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_12_failure].content
   limit: do 150 znaków
   EN: The Night Drifter's moves are so confusing to follow... not to mention the pungent smell of alcohol making me dizzy.
   PL: Ruchy Pijanicy Nocnego Wędrowca są strasznie trudne do wychwycenia… a od woni alkoholu kręci mi się w głowie.
369. [Wydarzenia i Przepustka [project_gs_lesson_result_desc_12_critical_failure] — tekst] 취수야객과 술을 나누어 마셨다… 기분이 좋았다.
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_result_desc_12_critical_failure].content
   limit: do 120 znaków
   EN: Shared some drinks with the Night Drifter... dang, that felt good.
   PL: Wypiliśmy z Pijanicą Nocnym Wędrowcem… Dobre to było.
370. [Wydarzenia i Przepustka [project_gs_combo_desc_wisdom_up] — tekst] 지 스탯 {0} 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_wisdom_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat gain: Zhi +{0}]
   PL: [Wzrost statystyki Zhi: {0}]
371. [Wydarzenia i Przepustka [project_gs_combo_desc_wisdom_down] — tekst] 지 스탯 {0} 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_wisdom_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat loss: Zhi -{0}]
   PL: [Spadek statystyki Zhi: {0}]
372. [Wydarzenia i Przepustka [project_gs_combo_desc_courage_up] — tekst] 용 스탯 {0} 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_courage_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat gain: Yong +{0}]
   PL: [Wzrost statystyki Yong: {0}]
373. [Wydarzenia i Przepustka [project_gs_combo_desc_courage_down] — tekst] 용 스탯 {0} 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_courage_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat loss: Yong -{0}]
   PL: [Spadek statystyki Yong: {0}]
374. [Wydarzenia i Przepustka [project_gs_combo_desc_benevolence_up] — tekst] 인 스탯 {0} 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_benevolence_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat gain: Ren +{0}]
   PL: [Wzrost statystyki Ren: {0}]
375. [Wydarzenia i Przepustka [project_gs_combo_desc_benevolence_down] — tekst] 인 스탯 {0} 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_benevolence_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Stat loss: Ren -{0}]
   PL: [Spadek statystyki Ren: {0}]
376. [Wydarzenia i Przepustka [project_gs_combo_desc_all_stats_up] — tekst] 모든 스탯 {0} 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_all_stats_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [All Stats +{0}]
   PL: [Wzrost wszystkich statystyk: {0}]
377. [Wydarzenia i Przepustka [project_gs_combo_desc_all_stats_down] — tekst] 모든 스탯 {0} 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_all_stats_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [All Stats -{0}]
   PL: [Spadek wszystkich statystyk: {0}]
378. [Wydarzenia i Przepustka [project_gs_combo_desc_condition_up] — tekst] 컨디션 {0} 회복
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_condition_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0} Morale restored]
   PL: [Odzyskano {0} Kondycji]
379. [Wydarzenia i Przepustka [project_gs_combo_desc_condition_down] — tekst] 컨디션 {0} 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_condition_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0} Morale lost]
   PL: [Utracono {0} Kondycji]
380. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_critical_success] — tekst] 수업 대성공
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_critical_success].content
   limit: do 120 znaków
   EN: [Huge Success in Class]
   PL: [Wielki Sukces Zajęć]
381. [Wydarzenia i Przepustka [project_gs_combo_desc_next_lesson_critical_success] — tekst] 다음 수업 대성공
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_next_lesson_critical_success].content
   limit: do 120 znaków
   EN: [Huge Success in next Class]
   PL: [Wielki Sukces na następnych Zajęciach]
382. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_wisdom_up] — tekst] 수업 결과로 얻은 지 스탯 {0}% 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_wisdom_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [+{0}% to Zhi Stat gained from Class]
   PL: [Statystyka Zhi ze Zajęć +{0}%]
383. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_wisdom_down] — tekst] 수업 결과로 얻은 지 스탯 {0}% 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_wisdom_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [-{0}% to Zhi Stat gained from Class]
   PL: [Statystyka Zhi ze Zajęć -{0}%]
384. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_courage_up] — tekst] 수업 결과로 얻은 용 스탯 {0}% 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_courage_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [+{0}% to Yong Stat gained from Class]
   PL: [Statystyka Yong ze Zajęć +{0}%]
385. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_courage_down] — tekst] 수업 결과로 얻은 용 스탯 {0}% 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_courage_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [-{0}% to Yong Stat gained from Class]
   PL: [Statystyka Yong ze Zajęć -{0}%]
386. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_benevolence_up] — tekst] 수업 결과로 얻은 인 스탯 {0}% 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_benevolence_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [+{0}% to Ren Stat gained from Class]
   PL: [Statystyka Ren ze Zajęć +{0}%]
387. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_benevolence_down] — tekst] 수업 결과로 얻은 인 스탯 {0}% 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_benevolence_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [-{0}% to Ren Stat gained from Class]
   PL: [Statystyka Ren ze Zajęć -{0}%]
388. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_all_up] — tekst] 수업 결과로 얻은 모든 스탯 {0}% 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_all_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [+{0}% to all Stats gained from Class]
   PL: [Wszystkie statystyki ze Zajęć +{0}%]
389. [Wydarzenia i Przepustka [project_gs_combo_desc_stats_result_ratio_all_down] — tekst] 수업 결과로 얻은 모든 스탯 {0}% 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_stats_result_ratio_all_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [-{0}% to all Stats gained from Class]
   PL: [Wszystkie statystyki ze Zajęć -{0}%]
390. [Wydarzenia i Przepustka [project_gs_combo_desc_title] — tekst] 콤보 발생 조합
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_title].content
   limit: do 120 znaków
   EN: Combo Combinations
   PL: Wyzwalacze Kombinacji
391. [Wydarzenia i Przepustka [project_gs_restart] — tekst] 재시작
   źródło: ProjectGS.json :: dataList[id=project_gs_restart].content
   limit: do 120 znaków
   EN: Restart
   PL: Zacznij od nowa
392. [Wydarzenia i Przepustka [project_gs_ask_to_restart] — tekst] 1일 부터 재시작하시겠습니까?
   źródło: ProjectGS.json :: dataList[id=project_gs_ask_to_restart].content
   limit: do 120 znaków
   EN: Restart from Day 1?
   PL: Zrestartować od Dnia 1?
393. [Wydarzenia i Przepustka [project_gs_finish_to_grow_up] — tekst] 수업 완료
   źródło: ProjectGS.json :: dataList[id=project_gs_finish_to_grow_up].content
   limit: do 120 znaków
   EN: Class Complete
   PL: Zajęcia ukończone
394. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_success_rate_up] — tekst] 수업 성공 확률 {0}% 증가
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_success_rate_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Class Success Rate +{0}%]
   PL: [Szansa sukcesu Zajęć +{0}%]
395. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_success_rate_down] — tekst] 수업 성공 확률 {0}% 감소
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_success_rate_down].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [Class Success Rate -{0}%]
   PL: [Szansa sukcesu Zajęć -{0}%]
396. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_success_rate_changed] — tekst] 수업 성공 확률 변경
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_success_rate_changed].content
   limit: do 120 znaków
   EN: [Class Success Rate Changed]
   PL: [Szansa sukcesu Zajęć zmieniona]
397. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_critical_success_changed] — tekst] - 대성공 : {0}%
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_critical_success_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: - Huge Success : {0}%
   PL: - Wielki Sukces : {0}%
398. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_success_changed] — tekst] - 성공 : {0}%
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_success_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: - Success : {0}%
   PL: - Sukces : {0}%
399. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_normal_changed] — tekst] - 보통 : {0}%
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_normal_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: - Average : {0}%
   PL: - Przeciętnie : {0}%
400. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_failure_changed] — tekst] - 실패 : {0}%
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_failure_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: - Failure : {0}%
   PL: - Porażka : {0}%
401. [Wydarzenia i Przepustka [project_gs_combo_desc_lesson_critical_failure_changed] — tekst] - 대실패 : {0}%
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_desc_lesson_critical_failure_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: - Huge Failure : {0}%
   PL: - Wielka Porażka : {0}%
402. [Wydarzenia i Przepustka [project_gs_lesson_level_up_title] — tekst] 알림
   źródło: ProjectGS.json :: dataList[id=project_gs_lesson_level_up_title].content
   limit: do 120 znaków
   EN: Notice
   PL: Powiadomienia
403. [Wydarzenia i Przepustka [project_gs_notice_unable_to_release_fixed_lesson] — tekst] 필수로 수강해야 하는\n수업입니다.
   źródło: ProjectGS.json :: dataList[id=project_gs_notice_unable_to_release_fixed_lesson].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is a mandatory class.
   PL: Musisz obowiązkowo\nodbyć te zajęcia.
404. [Wydarzenia i Przepustka [project_gs_combo_text_only_jia_xichun] — tekst] (가시춘)
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_text_only_jia_xichun].content
   limit: do 120 znaków
   EN: (Jia Xichun)
   PL: (Jia Xichun)
405. [Wydarzenia i Przepustka [project_gs_combo_text_only_sinclair] — tekst] (싱클레어)
   źródło: ProjectGS.json :: dataList[id=project_gs_combo_text_only_sinclair].content
   limit: do 120 znaków
   EN: (Sinclair)
   PL: (Sinclair)
406. [Wydarzenia i Przepustka [project_gs_ask_to_start_lesson] — tekst] 수업을 시작하시겠습니까?
   źródło: ProjectGS.json :: dataList[id=project_gs_ask_to_start_lesson].content
   limit: do 120 znaków
   EN: Resume Classes?
   PL: Wznowić zajęcia?
407. [Wydarzenia i Przepustka [project_gs_do_not_see_ask_to_start_lesson_popup] — tekst] 이 팝업을 다시 보지 않기
   źródło: ProjectGS.json :: dataList[id=project_gs_do_not_see_ask_to_start_lesson_popup].content
   limit: do 120 znaków
   EN: Don't show this message again
   PL: Nie pokazuj więcej tego komunikatu
408. [Wydarzenia i Przepustka [project_gs_stats_saved] — tekst] 성장 기록
   źródło: ProjectGS.json :: dataList[id=project_gs_stats_saved].content
   limit: do 120 znaków
   EN: Growth History
   PL: Historia Rozwoju
409. [Wydarzenia i Przepustka [project_gs_progress_label] — tekst] 수업 진행도
   źródło: ProjectGS.json :: dataList[id=project_gs_progress_label].content
   limit: do 120 znaków
   EN: Class Progress
   PL: Postęp Zajęć
410. [Wydarzenia i Przepustka [project_gs_ask_move_to_main] — tekst] 수업 진도를 저장하고\n메인 화면으로 돌아가시겠습니까?
   źródło: ProjectGS.json :: dataList[id=project_gs_ask_move_to_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Save your Class progress and\nreturn to the Main Menu?
   PL: Zapisać postęp zajęć\ni wrócić do menu głównego?
411. [Wydarzenia i Przepustka [project_gs_exit_title] — tekst] 수업 종료
   źródło: ProjectGS.json :: dataList[id=project_gs_exit_title].content
   limit: do 120 znaków
   EN: Classes Completed
   PL: Zajęcia zakończone
412. [Wydarzenia i Przepustka [project_gs_re_enter_warning] — tekst] 모든 수업이 종료되었습니다.\n다시 진입할 경우, 수업 진행 상황이 초기화되고, 마지막 수업 진행 시 이전 회차의 성장 기록이 덮어써집니다.\n그래도 진입하시겠습니까?
   źródło: ProjectGS.json :: dataList[id=project_gs_re_enter_warning].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The thirty days of Classes are over.\nRe-entering this node will reset your Class progresses, and starting the final Class will overwrite your previous run's Cultivation history.\nEnter anyway?
   PL: Wszystkie zajęcia dobiegły końca.\nPonowne wejście zresetuje postęp zajęć, a rozpoczęcie ostatnich zajęć nadpisze historię Rozwoju z poprzedniej rundy.\nWejść mimo wszystko?
413. [Wydarzenia i Przepustka [project_gs_check_growth] — tekst] 성장 확인
   źródło: ProjectGS.json :: dataList[id=project_gs_check_growth].content
   limit: do 120 znaków
   EN: View Growth
   PL: Podgląd Rozwoju
414. [Wydarzenia i Przepustka [project_gs_growth_desc] — tekst] 가시춘이 (지 : {0}, 용 : {1}, 인 : {2}) 만큼 성장했다!\n\n싱클레어가 (지 : {4}, 용 : {5}, 인 : {6}) 만큼 성장했다!
   źródło: ProjectGS.json :: dataList[id=project_gs_growth_desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {4}, {5}, {6}, \n
   EN: Jia Xichun has grown!\n(Zhi : {0}, Yong : {1}, Ren : {2})\nSinclair has grown!\n(Zhi : {4}, Yong : {5}, Ren : {6})
   PL: Jia Xichun rozwinęła się o (Zhi: {0}, Yong: {1}, Ren: {2})!\n\nSinclair rozwinął się o (Zhi: {4}, Yong: {5}, Ren: {6})!
415. [Wydarzenia i Przepustka [project_gs_growth_result_popup_lessons] — tekst] 이수한 수업
   źródło: ProjectGS.json :: dataList[id=project_gs_growth_result_popup_lessons].content
   limit: do 120 znaków
   EN: Classes Taken
   PL: Odbyte Zajęcia
416. [Wydarzenia i Przepustka [project_gs_growth_result_popup_check_stats] — tekst] 가시춘 정보 확인
   źródło: ProjectGS.json :: dataList[id=project_gs_growth_result_popup_check_stats].content
   limit: do 120 znaków
   EN: View Jia Xichun's Info
   PL: Informacje o Jia Xichun
417. [Wydarzenia i Przepustka [project_gs_ask_to_start_lesson_with_warning] — tekst] 마지막 수업을 진행할 경우, 이전 회차의 성장 기록이 덮어써집니다.\n그래도 수업을 시작하시겠습니까?
   źródło: ProjectGS.json :: dataList[id=project_gs_ask_to_start_lesson_with_warning].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Starting the final Class will overwrite the cultivation history of your last run.\nStart the Class anyway?
   PL: Rozpoczęcie ostatnich zajęć nadpisze historię Rozwoju z poprzedniej rundy.\nRozpocząć zajęcia mimo wszystko?
418. [Wydarzenia i Przepustka [project_gs_alarm_lesson_level_up] — tekst] [{0}] 수업의 등급이 {1}으로 올랐습니다.
   źródło: ProjectGS.json :: dataList[id=project_gs_alarm_lesson_level_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Class [{0}] leveled up to "{1}".
   PL: Poziom zajęć [{0}] wzrósł do {1}.

## Wydarzenia i Przepustka: ProjectGSComboName
- plik gry: `ProjectGSComboName.json`

419. [Wydarzenia i Przepustka [1] — tekst] 박제가 되어버린 천재
   źródło: ProjectGSComboName.json :: dataList[id=1].content
   limit: do 120 znaków
   EN: Taxidermied Geniuses
   PL: Zataksydermizowane Geniusze
420. [Wydarzenia i Przepustka [2] — tekst] 알쓸신협(알아두면 쓸 데 있는 신비한 해결사 협회)
   źródło: ProjectGSComboName.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Fixer Association Encyclopedia... For Dummies!
   PL: Sekrety Stowarzyszeń Fikserów... dla opornych!
421. [Wydarzenia i Przepustka [3] — tekst] 조간신문 본 뒤
   źródło: ProjectGSComboName.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: The Morning Papers
   PL: Po Porannej Prasie
422. [Wydarzenia i Przepustka [4] — tekst] 슬기로운 회사 생활
   źródło: ProjectGSComboName.json :: dataList[id=4].content
   limit: do 120 znaków
   EN: 9-to-5
   PL: Życie w Korpo
423. [Wydarzenia i Przepustka [5] — tekst] 동병상련
   źródło: ProjectGSComboName.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: Shared Pain
   PL: Wspólna Bieda
424. [Wydarzenia i Przepustka [6] — tekst] 법. 멀. 주. 가(법은 멀고 주먹은 가깝다)
   źródło: ProjectGSComboName.json :: dataList[id=6].content
   limit: do 120 znaków
   EN: F.A.F.O
   PL: Prawo Daleko, Pięści Poblisko
425. [Wydarzenia i Przepustka [7] — tekst] 전지적 예술 시점
   źródło: ProjectGSComboName.json :: dataList[id=7].content
   limit: do 120 znaków
   EN: Omniscient Artist's Viewpoint
   PL: Wszechwiedzący Punkt Widzenia Artysty
426. [Wydarzenia i Przepustka [8] — tekst] 필요한 것은 상냥함
   źródło: ProjectGSComboName.json :: dataList[id=8].content
   limit: do 120 znaków
   EN: What it Needs... is Kindness
   PL: Potrzebna Jest Łagodność
427. [Wydarzenia i Przepustka [9] — tekst] 분위기 메이커
   źródło: ProjectGSComboName.json :: dataList[id=9].content
   limit: do 120 znaków
   EN: The Comedy Duo
   PL: Duet Rozrywkowy
428. [Wydarzenia i Przepustka [10] — tekst] 좋은 상관, 나쁜 상관
   źródło: ProjectGSComboName.json :: dataList[id=10].content
   limit: do 120 znaków
   EN: The Good Drill Sergeant & Bad Drill Sergeant Routine
   PL: Dobry Sierżant, Zły Sierżant
429. [Wydarzenia i Przepustka [11] — tekst] 파괴될지언정 패배하지 않는
   źródło: ProjectGSComboName.json :: dataList[id=11].content
   limit: do 120 znaków
   EN: Can be Destroyed but not Defeated
   PL: Zniszczony, ale Nie Pokonany
430. [Wydarzenia i Przepustka [12] — tekst] 준비 만전
   źródło: ProjectGSComboName.json :: dataList[id=12].content
   limit: do 120 znaków
   EN: Prep Time
   PL: W Pełni Przygotowany
431. [Wydarzenia i Przepustka [13] — tekst] 천재와 바보는 종이 한 장 차이
   źródło: ProjectGSComboName.json :: dataList[id=13].content
   limit: do 120 znaków
   EN: Actually Pretty Similar
   PL: Geniusz i Głupek Różnią się O Włos
432. [Wydarzenia i Przepustka [14] — tekst] 소중한 식구
   źródło: ProjectGSComboName.json :: dataList[id=14].content
   limit: do 120 znaków
   EN: Family Matters
   PL: Rodzina jest Ważna
433. [Wydarzenia i Przepustka [15] — tekst] 마주하는 용기
   źródło: ProjectGSComboName.json :: dataList[id=15].content
   limit: do 120 znaków
   EN: Courage to Confront
   PL: Odwaga, by Stawić Czoła
434. [Wydarzenia i Przepustka [16] — tekst] 말보다 행동
   źródło: ProjectGSComboName.json :: dataList[id=16].content
   limit: do 120 znaków
   EN: Take A.C.T.S.
   PL: Czyny Mówią Same
435. [Wydarzenia i Przepustka [17] — tekst] 너구리굴
   źródło: ProjectGSComboName.json :: dataList[id=17].content
   limit: do 120 znaków
   EN: Hotboxed
   PL: Zadymiony Kącik
436. [Wydarzenia i Przepustka [18] — tekst] 이달의 우수사원
   źródło: ProjectGSComboName.json :: dataList[id=18].content
   limit: do 120 znaków
   EN: Wing Employees of the Month
   PL: Pracownicy Miesiąca w Skrzydle
437. [Wydarzenia i Przepustka [19] — tekst] 상명, 하복.
   źródło: ProjectGSComboName.json :: dataList[id=19].content
   limit: do 120 znaków
   EN: Chains of Command
   PL: Rozkaz W Górę, Wykonanie W Dół.
438. [Wydarzenia i Przepustka [20] — tekst] 식도락의 미학
   źródło: ProjectGSComboName.json :: dataList[id=20].content
   limit: do 120 znaków
   EN: Not-So-Solitary Gourmets
   PL: Estetyka Łasuchów
439. [Wydarzenia i Przepustka [21] — tekst] 어제의 적은 오늘의 동료
   źródło: ProjectGSComboName.json :: dataList[id=21].content
   limit: do 120 znaków
   EN: Enemy of Yesterday, Friend of Today
   PL: Wczorajszy Wróg, Dzisiejszy Towarzysz
440. [Wydarzenia i Przepustka [22] — tekst] 검으로 하는 이야기
   źródło: ProjectGSComboName.json :: dataList[id=22].content
   limit: do 120 znaków
   EN: Talking With Swords
   PL: Opowieści Na Ostrzach

## Wydarzenia i Przepustka: ProjectGSLessonName
- plik gry: `ProjectGSLessonName.json`

441. [Wydarzenia i Przepustka [1] — tekst] 거울을 통해 본 자아와 세계의 형이상학적 탐구
   źródło: ProjectGSLessonName.json :: dataList[id=1].content
   limit: do 120 znaków
   EN: Metaphysical Approach to Ego and the Reflected World
   PL: Metafizyczne Studium Jaźni i Odbitego Świata
442. [Wydarzenia i Przepustka [1] — prowadzący] 이상
   źródło: ProjectGSLessonName.json :: dataList[id=1].teacher
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
443. [Wydarzenia i Przepustka [2] — tekst] 도시 공학의 이해와 실제
   źródło: ProjectGSLessonName.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Understanding of City Engineering and its Practices
   PL: Inżynieria Miasta: Teoria i Praktyka
444. [Wydarzenia i Przepustka [2] — prowadzący] 파우스트
   źródło: ProjectGSLessonName.json :: dataList[id=2].teacher
   limit: do 40 znaków
   EN: Faust
   PL: Faust
445. [Wydarzenia i Przepustka [3] — tekst] 열정과 꿈! – 해결사 무용담
   źródło: ProjectGSLessonName.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: Be Passionate & Dream On! - Fixer Tales
   PL: Zapal się i Marz! — Opowieści Fikserów
446. [Wydarzenia i Przepustka [3] — prowadzący] 돈키호테
   źródło: ProjectGSLessonName.json :: dataList[id=3].teacher
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
447. [Wydarzenia i Przepustka [4] — tekst] 미지의 탐험, 그리고 극복-강호유람기
   źródło: ProjectGSLessonName.json :: dataList[id=4].content
   limit: do 120 znaków
   EN: Exploring and Overcoming the Unknown: Jianghu Journeys
   PL: Eksploracja Nieznanego i jego Przezwyciężanie — Podróże po Jianghu
448. [Wydarzenia i Przepustka [4] — prowadzący] 이스마엘
   źródło: ProjectGSLessonName.json :: dataList[id=4].teacher
   limit: do 40 znaków
   EN: Ishmael
   PL: Ishmael
449. [Wydarzenia i Przepustka [5] — tekst] 나의 전쟁 이야기
   źródło: ProjectGSLessonName.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: My War Tales
   PL: Moje Opowieści Wojenne
450. [Wydarzenia i Przepustka [5] — prowadzący] 그레고르
   źródło: ProjectGSLessonName.json :: dataList[id=5].teacher
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
451. [Wydarzenia i Przepustka [6] — tekst] 홍원에서 살아남는 법
   źródło: ProjectGSLessonName.json :: dataList[id=6].content
   limit: do 120 znaków
   EN: Surviving Hongyuan
   PL: Jak Przeżyć w Hongyuanie
452. [Wydarzenia i Przepustka [6] — prowadzący] 홍루
   źródło: ProjectGSLessonName.json :: dataList[id=6].teacher
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
453. [Wydarzenia i Przepustka [7] — tekst] 판단 가두기
   źródło: ProjectGSLessonName.json :: dataList[id=7].content
   limit: do 120 znaków
   EN: Judgment Containment
   PL: Dzierżenie Wyroku
454. [Wydarzenia i Przepustka [7] — prowadzący] 뫼르소
   źródło: ProjectGSLessonName.json :: dataList[id=7].teacher
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
455. [Wydarzenia i Przepustka [8] — tekst] 정보취득법 - 적은 어떻게 압박하는가
   źródło: ProjectGSLessonName.json :: dataList[id=8].content
   limit: do 120 znaków
   EN: Intelligence Acquisition - Corner Your Enemy
   PL: Zbieranie Informacji — Jak Wywierać Presję na Wrogu
456. [Wydarzenia i Przepustka [8] — prowadzący] 오티스
   źródło: ProjectGSLessonName.json :: dataList[id=8].teacher
   limit: do 40 znaków
   EN: Outis
   PL: Outis
457. [Wydarzenia i Przepustka [9] — tekst] 애. 다. 법. : 애를 다루는 법
   źródło: ProjectGSLessonName.json :: dataList[id=9].content
   limit: do 120 znaków
   EN: T.C.O.C. : Taking Care Of Children
   PL: Instrukcja Obsługi Dzieci
458. [Wydarzenia i Przepustka [9] — prowadzący] 료슈
   źródło: ProjectGSLessonName.json :: dataList[id=9].teacher
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
459. [Wydarzenia i Przepustka [10] — tekst] 포커페이스의 모든 것
   źródło: ProjectGSLessonName.json :: dataList[id=10].content
   limit: do 120 znaków
   EN: All About the Poker Face
   PL: Wszystko o Poker Face
460. [Wydarzenia i Przepustka [10] — prowadzący] 로쟈
   źródło: ProjectGSLessonName.json :: dataList[id=10].teacher
   limit: do 40 znaków
   EN: Rodion
   PL: Rodion
461. [Wydarzenia i Przepustka [11] — tekst] 싸움은 뭐다? 기세다
   źródło: ProjectGSLessonName.json :: dataList[id=11].content
   limit: do 120 znaków
   EN: Fightin's All About Morale
   PL: W Bójce Liczy się Hawiera
462. [Wydarzenia i Przepustka [11] — prowadzący] 히스클리프
   źródło: ProjectGSLessonName.json :: dataList[id=11].teacher
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
463. [Wydarzenia i Przepustka [12] — tekst] 『취수야화(酔手野話)』
   źródło: ProjectGSLessonName.json :: dataList[id=12].content
   limit: do 120 znaków
   EN: 『Rambling Tales from the Drunken Palm (酔手野話)』
   PL: 『Kołaczne Opowieści Pijanej Dłoni (酔手野話)』
464. [Wydarzenia i Przepustka [12] — prowadzący] 취수야객
   źródło: ProjectGSLessonName.json :: dataList[id=12].teacher
   limit: do 40 znaków
   EN: The Night Drifter
   PL: Pijanica Nocny Wędrowiec
465. [Wydarzenia i Przepustka [13] — tekst] ???
   źródło: ProjectGSLessonName.json :: dataList[id=13].content
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: RecordMemoryEvent
- plik gry: `RecordMemoryEvent.json`

466. [Wydarzenia i Przepustka [record_memory_stage_button_default] — tekst] 스테이지
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_stage_button_default].content
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Wydarzenia i Przepustka [record_memory_stage_button_locked] — tekst] 9.5-14 클리어 시 개방
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_stage_button_locked].content
   limit: do 120 znaków
   EN: Clear 9.5-14 to Unlock
   PL: Odblokowanie po ukończeniu 9.5-14
468. [Wydarzenia i Przepustka [record_memory_storybutton_default] — tekst] 상영관 이동
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_storybutton_default].content
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Wydarzenia i Przepustka [record_memory_storybutton_start] — tekst] <size=75%>이벤트 첫 번째 이야기\n감상 시 개방</size>
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_storybutton_start].content
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Wydarzenia i Przepustka [record_memory_stage_button_end_event] — tekst] 이벤트 기간 종료
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_stage_button_end_event].content
   (powtórzenie elementu 263 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Wydarzenia i Przepustka [record_memory_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_bonus_popup_title].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Wydarzenia i Przepustka [record_memory_bonusUIDesc] — tekst] 이벤트 기간 동안 해당 인격 편성 시, <color=#96beee>[사진들]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#96beee>120%</color>까지 적용됩니다.
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_bonusUIDesc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#96beee>, </color>, \n
   EN: During the event period, deploying the following Identities on your team will\nboost the amount of <color=#96beee>[Photos]</color> earned.\nYou can earn a maximum of <color=#96beee>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości, zwiększasz zdobywanie <color=#96beee>[Zdjęć]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#96beee>120%</color>.
473. [Wydarzenia i Przepustka [record_memory_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_scrap_guide_title].content
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Wydarzenia i Przepustka [record_memory_scrap_guide_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어,\n거울 던전 클리어를 통해 <color=#96beee>[사진들]</color>을 획득할 수 있으며,\n낮은 확률로 <color=#96beee>[사진더미들]</color>을 추가로 획득할 수 있습니다.\n\n<color=#96beee>[사진더미들]</color>은 획득 즉시, <color=#96beee>[사진들]</color> 20개로 전환됩니다.
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_scrap_guide_desc].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#96beee>, </color>, \n
   EN: You can obtain <color=#96beee>[Photos]</color> from first-time Event/Main Story Stages completions, or by clearing the Mirror Dungeon.\nYou also have a small chance to obtain <color=#96beee>[Photo Bundles]</color> in the process.\n\n<color=#96beee>[Photo Bundles]</color> are immediately converted to 20 <color=#96beee>[Photos]</color> upon acquisition.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#96beee>[Zdjęcia]</color>, a z pewnym prawdopodobieństwem dodatkowo <color=#96beee>[Stosy Zdjęć]</color>.\n\n<color=#96beee>[Stosy Zdjęć]</color> od razu zamieniają się na 20 <color=#96beee>[Zdjęć]</color>.
475. [Wydarzenia i Przepustka [record_memory_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#96beee>[사진들]</color>을 획득할 수 있습니다.\n\n<color=#96beee>[보상 교환]</color>창에서 <color=#96beee>[사진들]</color>을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_reward_popup_desc].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#96beee>, </color>, \n
   EN: Earn <color=#96beee>[Photos]</color> via the following methods:\nFirst-time Event Stage & Main Story Stage clears and Mirror Dungeon clears.\n\nIn the <color=#96beee>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#96beee>[Photos]</color> you have collected.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#96beee>[Zdjęcia]</color>.\n\nW oknie <color=#96beee>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#96beee>[Zdjęcia]</color>.
476. [Wydarzenia i Przepustka [record_memory_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_reward_popup_num_of_owned_items].content
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Wydarzenia i Przepustka [record_memory_rewardShopButton] — tekst] 보상 교환
   źródło: RecordMemoryEvent.json :: dataList[id=record_memory_rewardShopButton].content
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: SchemaCraftChoice
- plik gry: `SchemaCraftChoice.json`

478. [Wydarzenia i Przepustka [schemacraft_choice_1_title] — tekst] 전당포
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_1_title].content
   limit: do 120 znaków
   EN: A Pawnshop
   PL: Lombard
479. [Wydarzenia i Przepustka [schemacraft_choice_1_text] — tekst] 어중간한 비극과 빈곤으로는 아무도 전당포를 찾지 않지. 너저분하고 구차한 삶의 소음을 묵묵히 견뎌냈음에도, 미래에 걸었던 불투명한 기대마저 사라졌을 때. 사람들은 비로소, 가장 값진 과거를 내려놓으러 이곳으로 모여드는 거야. 양각으로 장식된 오른팔 의수, 어떤 곳으로 향할지 알 수 없는 기차표, 녹슬었지만 그 나름대로의 가치를 할 수 있을 것 같은 만년필 등이 진열되어 있어. 당신은 어색하게 주춤거리지만 주인은 그런 사람들 따위 수도 없이 보았다는 듯 고개도 들지 않고 물었지. '맡길 것?' 주머니를 뒤져 보던 당신은…
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_1_text].content
   limit: do 970 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You see, it takes more than a run of bad luck and an empty wallet for someone to step into a pawnshop willingly. People are more inclined to endure the shabby, wretched racket of "getting by" than one might think. ... Until even their faint hopes for tomorrow desert them.\nThat's when they start crowding this dingy place, ready to part with the most precious pieces of their past.\n\nOn the display, you see a prosthetic right arm adorned with raised patterns, a train ticket to who-knows-where, and a rusted fountain pen that still looks as though it might fetch something.\n\nYou linger awkwardly, but the owner has clearly seen your sort a thousand times before. Without so much as looking up, they ask, "So, what do you have?"\n\nYou rummage through your pockets and...
   PL: Sam trafiony los i pusty portfel nie każdemu sprawiają, że dobrowolnie wchodzi do lombardu. Ludzie mają się nagle za tyle tolerancji, że potrafią latami znosić szorstki, nędzny hałas „jakoś to będzie”. … Dopóki nawet blade nadzieje na jutro ich nie opuszczą.\nWtedy zaczynają schodzić do tego oblepalnego miejsca, gotowi pożegnać się z najcenniejszymi kawałkami przeszłości.\n\nNa wystawie widzisz protezę prawej ręki zdobioną wypukłymi wzorami, bilet kolejowy w nieznane i zardzewiałe pióro wieczne, które niby jeszcze coś jest warte.\n\nWaha się, ale właściciel widział takich jak ty tysiąc razy. Nie podnosząc wzroku, pyta: „No, co masz?”\nGrzebiesz w kieszeniach i…
480. [Wydarzenia i Przepustka [schemacraft_choice_1_option_a] — tekst] 가진 것들을 전부 올려놓았다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_1_option_a].content
   limit: do 120 znaków
   EN: Lay everything I have on the counter.
   PL: Kładę wszystko, co mam.
481. [Wydarzenia i Przepustka [schemacraft_choice_1_option_b] — tekst] 제일 하찮은 것 하나만 내민다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_1_option_b].content
   limit: do 120 znaków
   EN: Offer only the least valuable thing I own.
   PL: Wyciągam tylko najmniej wartą rzecz.
482. [Wydarzenia i Przepustka [schemacraft_choice_1_skip] — tekst] 훑어오는 시선을 피해 달아난다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_1_skip].content
   limit: do 120 znaków
   EN: Turn away from that appraising gaze and make a run for it.
   PL: Uciekam od oceniającego spojrzenia.
483. [Wydarzenia i Przepustka [schemacraft_choice_2_title] — tekst] 대리시험
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_2_title].content
   limit: do 120 znaków
   EN: Stand-in Exam
   PL: Egzamin za Kogoś
484. [Wydarzenia i Przepustka [schemacraft_choice_2_text] — tekst] 골목에 모여 있던 사람들이 다가왔어. '알다시피 내일 있는 실기 시험은… 얼굴을 꼼꼼하게 확인하지 않아요' 당신들은 이들이 왜 이런 말을 늘어놓는지 이내 깨달았지. '그리고 우리 아이들은 아직 너무 어려요. 경험도 부족하죠' 곧이어 옆의 사람이 이어 말했어. '하지만 이번 달까지 자격증을 전부 따야 다음 달에 있는 입사 면접에서 가산점을 딸 수 있다던데…' 어떤 시험인지는 말해주지 않아. 하지만 당신들이라면 이들이 둥지 이주에 대한 발판을 마련하는 데 조금의 도움을 줄 수 있을지도 모르지.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_2_text].content
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You are approached by a group gathered in an alley.\n\n"You know, for tomorrow's practical exam... well, let's say they're not too particular about checking faces. \n\nIt doesn't take long for you to work out what they're getting at.\n\n"And my children are still so young. They just don't have much experience."\n\nSomeone beside them picks up the thread.\n\n"But we've heard that if they earn all their certifications by the end of this month, they'll get extra points at next month's job interviews..."\n\nNobody mentions what the exam is actually for. Still, perhaps people like you might be able to give these people a small leg up on their way to achieving that dream of Nest life?
   PL: Podchodzą do ciebie ludzie zgromadzeni w zaułku.\n\n„Wiesz, jutrzejszy egzamin praktyczny… powiedzmy, że twarzy specjalnie nie sprawdzają.\n\nNie trzeba długo głowić się, do czego zmierzają.\n\n„A moje dzieci są jeszcze takie małe. Doświadczenia brakuje.”\n\nKtoś obok podbija wątek.\n\n„Ale słyszeliśmy, że jeśli do końca miesiąca zbiorą wszystkie zaświadczenia, dostaną dodatkowe punkty na przyszłomiesięcznych rozmowach o pracę…”\n\nNikt nie mówi, na co ten egzamin. Może jednak ludzie tacy jak wy mogą dać tym ludziom małego kopa w stronę życia w Gnieździe?
485. [Wydarzenia i Przepustka [schemacraft_choice_2_option_a] — tekst] 수감자 하나만 보낸다. 내키지 않아 하는 기색이지만 어쩔 수 없지.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_2_option_a].content
   limit: do 120 znaków
   EN: Send one Sinner. They don't look happy about it, but someone has to do it.
   PL: Wysyłam jednego Grzesznika. Choć nie bardzo mu się to podoba — trudno.
486. [Wydarzenia i Przepustka [schemacraft_choice_2_option_b] — tekst] 제비뽑기를 통해 뽑힌 둘을 보낸다. 이로써 최대한 많은 합격자가 나올 수 있도록.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_2_option_b].content
   limit: do 130 znaków
   EN: Draw lots and send two Sinners. That should give as many applicants as possible a chance to pass.
   PL: Losuję i wysyłam dwóch. Tak, by zdało ich jak najwięcej.
487. [Wydarzenia i Przepustka [schemacraft_choice_2_skip] — tekst] 관여하지 않는다. 둥지로의 이주는 이렇게 쉽게 이뤄지는 게 아니다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_2_skip].content
   limit: do 120 znaków
   EN: Stay out of it. Moving into a Nest is never going to be that easy.
   PL: Nie mieszam się. Przeprowadzka do Gniazda nie przychodzi tak łatwo.
488. [Wydarzenia i Przepustka [schemacraft_choice_3_title] — tekst] 자리 없는 놀이터
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_3_title].content
   limit: do 120 znaków
   EN: An Overcrowded Playground
   PL: Przepchany Plac Zabaw
489. [Wydarzenia i Przepustka [schemacraft_choice_3_text] — tekst] 이삿짐이 놓인 트럭이 좁은 골목을 비집고 들어오고 있어. 놀이터의 아이들은 일제히 고개를 돌리지만 반기는 얼굴은 하나도 없네. ‘하지만 이 놀이터는 이미 꽉 찼어. 빨간 그네에 여덟, 초록 그네에 다섯, 미끄럼틀에 열, 계단에 넷 하고 반, 시소에 열.’ 대장처럼 보이는 아이가 또박또박 말을 해. ‘그렇다면, 새로 오는 아이는 어디에 두지?’
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_3_text].content
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A moving truck loaded with someone's belongings squeezes into the narrow alley. Every child in the playground turns to look, but what a shame—not a single face lights up in welcome.\n\n"But the playground's already full. 8 on the red swings, 5 on the green ones, 10 on the slide, 4.5 on the steps, and 10 on the seesaw."\n\nThe child who seems to be in charge counts the kids off, each syllable crisp and clear.\n\n"Where are we even supposed to put the new kid?"
   PL: Ciężarówka z przeprowadzką wciska się w wąski zaułek. Wszystkie dzieci z placu zawracają głowy, ale ani jedna twarz nie promieniuje powitaniem. „Ale ten plac jest już pełny. Na czerwonych huśtawkach osiem, na zielonych pięć, na zjeżdżalni dziesięć, na schodach cztery i pół, na huśtawce dziesięć.” Dziecko wyglądające na paczkę przelicza rzędziście: „To gdzie mamy postawić nowego?”
490. [Wydarzenia i Przepustka [schemacraft_choice_3_option_a] — tekst] 모랫바닥. 늦게 온 아이가 있을 곳은 그곳밖에 없다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_3_option_a].content
   limit: do 120 znaków
   EN: On the sand. It's the only place left for a latecomer.
   PL: Na piasku. To jedyne miejsce dla spóźnialskiego.
491. [Wydarzenia i Przepustka [schemacraft_choice_3_option_b] — tekst] 빨간 그네. 조금 더 비집고 끼워 넣는다면 가능할지도?
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_3_option_b].content
   limit: do 120 znaków
   EN: On the red swings. Maybe there's room to squeeze in just one more?
   PL: Na czerwone huśtawki. Może da się jeszcze wcisnąć?
492. [Wydarzenia i Przepustka [schemacraft_choice_3_skip] — tekst] 셈에 끼지 않기로 했다. 아이들을 등지고 걸어간다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_3_skip].content
   limit: do 120 znaków
   EN: Stay out of the headcount. Turn my back on the children and walk away.
   PL: Nie mieszam się do rachub. Odwracam się od dzieci i odchodzę.
493. [Wydarzenia i Przepustka [schemacraft_choice_4_title] — tekst] 위조 명함
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_4_title].content
   limit: do 120 znaków
   EN: Counterfeit Business Card
   PL: Podróbka Wizytówki
494. [Wydarzenia i Przepustka [schemacraft_choice_4_text] — tekst] ‘무엇이든 될 수 있지. 꿈도 못 꿔본 것들 전부’ 사연 있는 사람들을 수차례 상대해 보았는지 주인은 익숙하게 영업을 해. 거창한 말과는 달리 그자의 손에 들린 것은 몇 장의 명함들 뿐. ‘이 종이에서만큼은, 당신은 K사의 팀장이지. 5급 해결사 사무소의 대표도 될 수 있고. 단 단속반이 온다면, 이곳은 과일 가게가 되는 거고 지금의 당신이 사간 건 잘 익은 사과뿐이 될 테지만.’ 이 자가 교묘하게 만들어준 명함 한 장이면 당신은 누구든 될 수 있어.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_4_text].content
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "You could be anyone. Even someone you never dared to dream of being."\n\nThe owner runs through the pitch with the ease of someone who's heard more than a few hard-luck stories.\nFor all the grand promises, though, they're holding nothing more than a few business cards.\n\n"On this little piece of paper, at least, you're a team leader at K Corp. Or the director of a Grade 5 Fixer Office, if you prefer. Mind you, if the inspectors come knocking, this is a fruit shop, and all you've bought today is a nice, ripe apple."\n\nWith one of those artfully forged cards in hand... you could be anyone.
   PL: „Możesz być kimkolwiek. Nawet kimś, o kim nie śniłeś.” Właściciel kręci sprzedaż z lekkością człowieka, który słyszał już tyle złych historii.\nMimo wszystkich wielkich obietnic trzyma w dłoni ledwie kilka wizytówek.\n\n„Na tym papierku, przynajmniej, jesteś szefem zespołu w Korp. K. Albo dyrektorem Fikserów 5. Klasy, jeśli wolisz. Ale gdy przyjadą kontrole, to tu jest sklep owocowy, a dziś kupiłeś tylko jedno ładne, dojrzałe jabłko.”\nZ taką artystycznie podrobioną wizytówką w ręku… możesz być kimkolwiek.
495. [Wydarzenia i Przepustka [schemacraft_choice_4_option_a] — tekst] 아무나 되어 본다. 지금의 나만 아니라면 누구든 상관없다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_4_option_a].content
   limit: do 120 znaków
   EN: Try being someone else. Anyone will do, so long as it isn't who I am now.
   PL: Będę kimś innym. Kogokolwiek — byle nie tym, kim jestem teraz.
496. [Wydarzenia i Przepustka [schemacraft_choice_4_option_b] — tekst] 날개의 입사자가 되어 본다. 많은 이들의 부러움을 받게 될 테니.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_4_option_b].content
   limit: do 120 znaków
   EN: Become a new hire at a Wing. That should leave plenty of people green with envy.
   PL: Zostanę nowym pracownikiem Skrzydła. Niech inni zawiędną.
497. [Wydarzenia i Przepustka [schemacraft_choice_4_skip] — tekst] 지금의 나에게 만족한다. 지금 이대로도 나쁘지 않은 인생이다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_4_skip].content
   limit: do 120 znaków
   EN: Stick with who I am. This life isn't so bad, all things considered.
   PL: Zostaję sobą. To życie, rozpatrując wszystko, nie jest takie złe.
498. [Wydarzenia i Przepustka [schemacraft_choice_5_title] — tekst] 넝마 언덕
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_5_title].content
   limit: do 120 znaków
   EN: A Hill of Rags
   PL: Wzgórze Łachmanów
499. [Wydarzenia i Przepustka [schemacraft_choice_5_text] — tekst] 혼잡스러운 시장 가판대 사이로 언덕 하나가 보여. 살펴보니 그것은 수많은 옷으로 쌓인 층들이야. 이곳의 모든 이들의 세탁물일지도 모르지. 구겨지고 주름지고 더럽고 냄새나는 경험들. 어쩌면 후일을 위해 한 벌 정도는 가져가 봐도 될지 몰라. 언젠가 우리들의 옷도 흐르고 흘러 이 언덕 아래에 쌓일 테니…
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_5_text].content
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Between the crowded market stalls, a hill rises into your view. You take a closer look, soon realizing that it contains layers upon layers of clothing; perhaps the whole town's laundry has found its way into the pile? It's their lives and experiences worn thin, creased, crumpled, filthy, reeking.\n\nMaybe it wouldn't hurt to take an outfit along, something to set aside for later. Our own clothes will find their way down to the foot of this hill one day...
   PL: Między ciasnymi straganami rynku nadciąga wzgórze. Patrzysz uważnie — to warstwy ubrań na warstwach; może całe pranie miasta skończyło się tu? To ich życie i doświadczenia, wycierane cienko, pomięte, pogniecione, brudne i śmierdzące.\n\nMoże nie szkodzi zabrać jedną sukienkę na później. Nasze własne ubrania kiedyś z rolą spłyną na dno tego wzgórza…
500. [Wydarzenia i Przepustka [schemacraft_choice_5_option_a] — tekst] 정장 한 벌을 가져간다. 좀 더 헹구고 다림질을 한다면 꽤나 그럴듯해 보일지도 모른다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_5_option_a].content
   limit: do 120 znaków
   EN: Take a suit. Another rinse and a good ironing might make it look presentable enough.
   PL: Zabieram garnitur. Jeszcze płukanie i prasowanie — i może wyglądać przyzwoicie.
501. [Wydarzenia i Przepustka [schemacraft_choice_5_option_b] — tekst] 무언가의 가죽 하나를 가져간다. 이곳을 돌아다니다 보면 가끔은 인간처럼 보이지 않아야 할 때가 찾아올 수 있기에.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_5_option_b].content
   limit: do 160 znaków
   EN: Take the hide of... something. Wandering these streets, there may come a time when looking human isn't such a good idea.
   PL: Zabieram skórę… czegoś. Krążąc po tych ulicach, czasem lepiej nie wyglądać jak człowiek.
502. [Wydarzenia i Przepustka [schemacraft_choice_5_skip] — tekst] 어떤 것도 가져가지 않는다. 지금 입은 것으로도 충분하다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_5_skip].content
   limit: do 120 znaków
   EN: Take nothing. What I'm wearing will do.
   PL: Nie zabieram nic. To, co noszę, wystarczy.
503. [Wydarzenia i Przepustka [schemacraft_choice_6_title] — tekst] 아무도 없는 정류장
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_6_title].content
   limit: do 120 znaków
   EN: An Empty Bus Stop
   PL: Pusty Przystanek
504. [Wydarzenia i Przepustka [schemacraft_choice_6_text] — tekst] 인적이 끊긴 정류장. 어디로 가는지도 어디서 왔는지도 모를 버스가 당신 앞에 멈춰섰어. 기다려온 시간에 보답하듯, 버스는 경적 한 번 울리지 않고 당신을 기다리지. 그러나 기다림은 오래지 않을 거야. 밤이 온 뒤에도, 뒷골목에는 한 번 더 밤이 찾아오기에… 서둘러 귀로를 정해야만 하겠지.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_6_text].content
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You find yourself at a bus stop, not a soul to be seen.\nA bus from nowhere pulls up in front of you; you have no idea where it's going.\nAs though returning the favor for all the time you've spent waiting, it waits patiently without so much as a honk.\nBut it won't wait for you forever.\nEven after night has fallen, the Backstreets have another night in store, after all...\nYou'd better decide how you're getting home, and quickly.
   PL: Przystanek bez duszy. Autobus znikąd staje przed tobą; nie wiesz, dokąd zmierza.\nJakby w podzięce za cały ten czas oczekiwania, czeka cierpliwie, ani razu nie zasygnalizując.\nAle czekać będzie krótko.\nPo zapadnięciu nocy zaułki czekają jeszcze jedna noc…\nMusisz szybko zdecydować, jak wrócisz do domu.
505. [Wydarzenia i Przepustka [schemacraft_choice_6_option_a] — tekst] 버스에 탑승한다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_6_option_a].content
   limit: do 120 znaków
   EN: Get on the bus.
   PL: Wsiadam do autobusu.
506. [Wydarzenia i Przepustka [schemacraft_choice_6_option_b] — tekst] 기억하는 방향으로 걸어간다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_6_option_b].content
   limit: do 120 znaków
   EN: Head off on foot, following the way I remember.
   PL: Idę piechotą w stronę, którą pamiętam.
507. [Wydarzenia i Przepustka [schemacraft_choice_6_skip] — tekst] 버스를 보내고 정류장에 남는다. 다음 차가 오기는 할까.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_6_skip].content
   limit: do 120 znaków
   EN: Let the bus go and stay at the stop. But will there even be another one?
   PL: Puszczam autobus i zostaję na przystanku. Ale czy przyjedzie następny?
508. [Wydarzenia i Przepustka [schemacraft_choice_7_title] — tekst] 백야
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_7_title].content
   limit: do 120 znaków
   EN: White Nights
   PL: Biała Noc
509. [Wydarzenia i Przepustka [schemacraft_choice_7_text] — tekst] 빽빽한 건물들의 틈 사이로, 환한 빛이 솟구쳐 오르고 있어. 밤이라는 것이 세상에서 사라진 것처럼, 온 세상이 밝아지지. 뒷골목의 사람들이 하나둘 고개를 들어 하늘을 바라봐. 그 따사로운 빛 아래서, 당신은…
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_7_text].content
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You see a brilliant pillar of light shooting up to the sky, its rays cutting through the gaps between the tightly packed buildings. Your whole world lights up, as though night itself has ceased to exist.\nOne by one, the people of the Backstreets lift their heads toward the sky.\nBeneath that gentle, warm light, you...
   PL: Widzisz jasną kolumnę światła wzbijającą się ku niebu, przecinającą szczeliny między ciasno ściśniętymi budynkami. Cały świat robi się jasny, jakby noc przestała istnieć.\nJeden po drugim ludzie Zaułków unoszą głowy ku niebu.\nPod tym łagodnym, ciepłym światłem ty…
510. [Wydarzenia i Przepustka [schemacraft_choice_7_option_a] — tekst] 사람들과 함께 하늘을 올려다본다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_7_option_a].content
   limit: do 120 znaków
   EN: Look up at the sky with everyone else.
   PL: Wzrokiem idę za niebem razem z ludźmi.
511. [Wydarzenia i Przepustka [schemacraft_choice_7_option_b] — tekst] 도로 위 난반사된 빛을 내려다본다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_7_option_b].content
   limit: do 120 znaków
   EN: Look down at the light scattering across the uneven pavement.
   PL: Patrzę w dół, na światło rozsypujące się po nierównym bruku.
512. [Wydarzenia i Przepustka [schemacraft_choice_7_skip] — tekst] 그냥 눈을 질끈 감는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_7_skip].content
   limit: do 120 znaków
   EN: Just squeeze my eyes shut.
   PL: Po prostu zaciskam oczy.
513. [Wydarzenia i Przepustka [schemacraft_choice_8_title] — tekst] 소문으로 가득찬 벽
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_title].content
   limit: do 120 znaków
   EN: A Wall Full of Rumors
   PL: Ściana Pełna Plotek
514. [Wydarzenia i Przepustka [schemacraft_choice_8_text] — tekst] 자질구레한 심부름부터 탐사와 청부살인까지. 해결사를 찾는 의뢰는 언제나 끊이질 않나봐. 의뢰의 대가는 표면적으로나마 모두 합당해 보여. 무엇을 맡고, 무엇을 외면할지는 스스로의 선택에 달려있을 거야
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_text].content
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: From petty errands to expeditions and contract killings, there's never a shortage of work for a Fixer, is there?\nThe pay for each job looks fair enough. On paper, at least.\nBut which will you take, and which will you turn a blind eye to? The choice is yours.
   PL: Od drobnych zleceń po ekspedycje i zlecenia na śmierć — dla Fiksera pracy nigdy nie brak.\nPłaca za każde zlecenie wygląda uczciwie. Przynajmniej na papierze.\nAle które podejmiesz, a które wolisz ominąć wzrokiem? Wybór należy do ciebie.
515. [Wydarzenia i Przepustka [schemacraft_choice_8_option_a] — tekst] 도시 괴담. 항상 해오던 의뢰를 맡는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_option_a].content
   limit: do 120 znaków
   EN: Urban Myth. Take on the sort of job that's familiar enough.
   PL: Miejski mit. Podejmuję zlecenie, jakie znam dobrze.
516. [Wydarzenia i Przepustka [schemacraft_choice_8_option_b] — tekst] 돈이 될만한 뜬소문을 쫓는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_option_b].content
   limit: do 120 znaków
   EN: Follow a Canard that might turn a profit.
   PL: Idę za kanardem, który może się zwrócić.
517. [Wydarzenia i Przepustka [schemacraft_choice_8_option_c] — tekst] 도시 전설. 막대한 보수가 걸린 의뢰를 맡는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_option_c].content
   limit: do 120 znaków
   EN: Urban Legend. Take on a job that offers a hefty payout.
   PL: Miejska legenda. Podejmuję zlecenie z pokaźną wypłatą.
518. [Wydarzenia i Przepustka [schemacraft_choice_8_skip] — tekst] 의뢰를 받지 않는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_8_skip].content
   limit: do 120 znaków
   EN: Take none of the contracts.
   PL: Nie przyjmuję żadnego zlecenia.
519. [Wydarzenia i Przepustka [schemacraft_choice_201_title] — tekst] 익숙하면서 낯선 골목
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_title].content
   limit: do 120 znaków
   EN: Familiar Yet Unknown Alleyways
   PL: Zaułki Znajome i Nieznane
520. [Wydarzenia i Przepustka [schemacraft_choice_201_text] — tekst] 미로 같은 골목이 이어지고 있어. 이 뒷골목은 기억하고 있는 그 어떤 곳의 골목과도 닮아있으며 동시에 낯설지. 걷고 또 걸어도 끝을 알 수 없는 골목을 걷다 문득 당신의 관심을 끌고 있는 것이 무엇인지를 알아챘어. 그것은…
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_text].content
   limit: do 440 znaków
   EN: The labyrinthine network of alleyways winds on, one turn after another. These Backstreets resemble every alley you can remember, yet somehow none of them feel familiar. You keep walking, turn after turn, but there's no end in sight. Then, all at once, a sudden realization comes to you: this odd feeling that's been tugging at your attention is...
   PL: Labirynt zaułków wije się zakrętem za zakrętem. Te Zaułki przypominają każdą aleję, jaką pamiętasz, a zarazem żadna nie jest znajoma. Idziesz i idziesz, zakręt za zakrętem, a końca brak. Wtem jednak rozumiesz, co to uczucie, które ciągnie twoją uwagę, jest…
521. [Wydarzenia i Przepustka [schemacraft_choice_201_option_a] — tekst] 어두워진 주변이다. 단말기를 꺼내 시간을 살펴보자.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_a].content
   limit: do 120 znaków
   EN: The darkness closing in around me. Better take out my PDA and check the time.
   PL: Ciemność, która się zbliża. Lepiej wyciągnąć terminal PDA i sprawdzić godzinę.
522. [Wydarzenia i Przepustka [schemacraft_choice_201_option_a_desc] — tekst] 3시 13분. 뒷골목에 밤이 내리면 그들이 찾아온다. 해가 오르면 그 어떠한 흔적도 남지 않도록.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_a_desc].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 3:13 AM.\nWhen the "Night" falls on the Backstreets, they come.\nCome sunrise, there won't be a trace of anything left behind.
   PL: 3:13 w nocy.\nGdy „Noc” zapada na Zaułkach, oni przybywają.\nO wschodzie słońca nie zostanie po nich ani ślad.
523. [Wydarzenia i Przepustka [schemacraft_choice_201_option_b] — tekst] 어딘가에서 나는 음악소리였다. 흥겨운 박자다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_b].content
   limit: do 120 znaków
   EN: Music drifting from somewhere. It's got a catchy beat.
   PL: Z zewnątrz płynęła muzyka. Ma w sobie taneczny rytm.
524. [Wydarzenia i Przepustka [schemacraft_choice_201_option_b_desc] — tekst] 잘그락거리는 사슬 소리. 과시하는 듯한 웃음 소리. 그래. 중지는 잊는 법이 없다. 그들에게 원한을 산 이상, 언제까지나 도망자 신세일 수밖에 없다. 결국은 어느 골목 어귀에서 그들과 마주치고 말 테니까.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_b_desc].content
   limit: do 280 znaków
   EN: Clinking chains. Boisterous guffaw. Right, the Middle never forgets. Once you're in their bad books, you'll be on the run for the rest of your life... only to inevitably find them waiting at the mouth of some alleyway.
   PL: Szczękanie łańcuchów. Gromki śmiech. No tak — Środkowy nie zapomina. Raz zyskawszy jego niechęć, jesteś uciekinierem do końca życia… i w końcu spotkasz go przy uchu jakiegoś zaułku.
525. [Wydarzenia i Przepustka [schemacraft_choice_201_option_c] — tekst] 무언가가 짖고 있는 소리였다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_c].content
   limit: do 120 znaków
   EN: The sound of something barking...
   PL: Z zewnątrz dobiegło szczekanie…
526. [Wydarzenia i Przepustka [schemacraft_choice_201_option_c_desc] — tekst] 한 마리가 짖기 시작하자 이내 모든 골목 전체가 따라짖는 소리로 가득찼다. 발이 네개 있는 것들이 골목을 기어다니며 무엇을 지키는지도 모른 채 울부짖는다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_c_desc].content
   limit: do 240 znaków
   EN: One starts barking, and soon every alley is barking in tandem. The four-legged things crawl on these streets, howling into the air without even figuring out what they are meant to guard.
   PL: Jedno zaczyna szczekać, a po chwili każdy zaułek szczeka w rytm. Czteronogie istoty pełzają po ulicach, wyjąc w niebo, choć same nie wiedzą, co mają strzec.
527. [Wydarzenia i Przepustka [schemacraft_choice_201_option_d] — tekst] 관심이 별로 생기지 않는다. 앞으로 계속 걸어간다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_d].content
   limit: do 120 znaków
   EN: Nothing worth stopping for. Keep walking.
   PL: Nie ma czego słuchać. Idę dalej.
528. [Wydarzenia i Przepustka [schemacraft_choice_201_option_d_desc] — tekst] 앞으로 계속 걸어가기로 했다. 내가 기다리고 있는 것은 이 골목에선 없을지도 모른다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_d_desc].content
   limit: do 120 znaków
   EN: I decide to keep moving. What I'm waiting for might not be in this alley at all.
   PL: Idę dalej. Tego, na co czekam, może nie być w tym zaułku.
529. [Wydarzenia i Przepustka [schemacraft_choice_201_option_e] — tekst] 의미없는 것이다. 더 이상 아무것도 신경쓰고 싶지 않았다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_e].content
   limit: do 120 znaków
   EN: Nothing that matters. I don't want to care about anything anymore.
   PL: Nic takiego. Już niczym nie chcę się przejmować.
530. [Wydarzenia i Przepustka [schemacraft_choice_201_option_e_desc] — tekst] 어떤 것이든 별로 궁금하지 않았다. 기척은 이내 잦아들 것이다. 그리고 또 다시 새로운 기척으로 채워지겠지.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_201_option_e_desc].content
   limit: do 180 znaków
   EN: Whatever it is, I have no desire to find out. Soon, those stirrings will die away. Then something else will come along to fill the silence.
   PL: Cokolwiek to jest, nie chcę wiedzieć. Wkrótce ten ruch umilknie. A potem ciszę zapełni coś innego.
531. [Wydarzenia i Przepustka [schemacraft_choice_202_title] — tekst] 검은 구름
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_title].content
   limit: do 120 znaków
   EN: Dark Cloud
   PL: Czarna Chmura
532. [Wydarzenia i Przepustka [schemacraft_choice_202_text] — tekst] 미로 같은 골목의 끝에서, 텅빈 공터에 발을 들였어. 이 뒷골목은 기억하고 있는 그 어떤 곳의 골목과도 달라 낯설고, 동시에 무관심하지. 그렇기에 기억을 종이 삼아, 그 위로 뒷골목의 삶을 마음대로 그려 봐도 될 거야. 진위도 가리지 않고, 허실도 구분하지 않고… 그렇게 거리의 무관심이 달갑지 않은 관심으로 변하는 순간. 생각에서 피어난 검은 구름이 골목을 따라 길게 드리웠어
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_text].content
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You wander into the cul-de-sac of some labyrinthine network of alleyways.\nThis Backstreets you've stepped into is unlike any street you've walked before; it is at once unfamiliar and disinterested.\nWith nothing but your memories as drawing paper, you begin sketching the life in this Backstreets, caring little for what is true or false, what is weak or powerful...\nAs the disinterest of the streets turns into a specific, unwelcome interest, black clouds stretching from your thoughts cast shadows just as long and dark over the alleyway.
   PL: Wchodzisz na ślepe załamanie jakiegoś labiryntu zaułków.\nTe Zaułki, do których stanąłeś, nie są podobne do żadnej ulicy, po której chodziłeś; są zarazem obce i obojętne.\nZ pamięcią jako papierem rysunkowym zaczynasz szkicować życie tych Zaułków, nie dbając o to, co prawdziwe, a co zmyślone, co słabe, a co potężne…\nGdy obojętność ulic zmienia się w konkretne, nieproszone zainteresowanie, czarne chmury, które wyrastają z twoich myśli, rzucają na zaułek równie długie i czarne cienie.
533. [Wydarzenia i Przepustka [schemacraft_choice_202_option_a] — tekst] 구름을 벤다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_option_a].content
   limit: do 120 znaków
   EN: Cut through the cumulus.
   PL: Rozcinam chmurę.
534. [Wydarzenia i Przepustka [schemacraft_choice_202_option_a_desc] — tekst] 동부십검. 검귀. 수라. 지옥의 문을 열어 처절히 경험했기에, 나는 그 이름을 가졌던 자들을 기억한다. 이곳에는…
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_option_a_desc].content
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ten Blades of the East. Blade Fiend. Ashura.\nEach warrior who held one of those titles has brought me again and again before the gates of hell, searing themselves deep into my memories with agony as their brand.\n\nHere awaits...
   PL: Dziesięć Ostrzy Wschodu. Ostrze Demon. Aszura.\nKażdy wojownik, który nosił jeden z tych tytułów, przeprowadzał mnie znów i znów przez bramy piekła, wypalając się w mojej pamięci bólem jak piętnem.\n\nTu czeka…
535. [Wydarzenia i Przepustka [schemacraft_choice_202_option_c] — tekst] 구름을 피해 도망친다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_option_c].content
   limit: do 120 znaków
   EN: Flee from the cumulus.
   PL: Uciekam przed chmurą.
536. [Wydarzenia i Przepustka [schemacraft_choice_202_option_c_desc] — tekst] 구축한 세계에 반드시 발을 들이밀 필요는 없다.
   źródło: SchemaCraftChoice.json :: dataList[id=schemacraft_choice_202_option_c_desc].content
   limit: do 120 znaków
   EN: There is no need to step into the crafted world.
   PL: Nie ma potrzeby wchodzić do zbudowanego świata.

## Wydarzenia i Przepustka: SeasonTitle-a1c7
- plik gry: `SeasonTitle-a1c7.json`

537. [Wydarzenia i Przepustka [unable_to_edit] — tekst] 편집 불가
   źródło: SeasonTitle-a1c7.json :: dataList[id=unable_to_edit].content
   limit: do 120 znaków
   EN: Cannot be Edited
   PL: Nie można edytować
538. [Wydarzenia i Przepustka [start_mp_changed] — tekst] 시작 정신력 {1} {0}
   źródło: SeasonTitle-a1c7.json :: dataList[id=start_mp_changed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Entry SP {1} {0}
   PL: PP na wejściu {1} {0}
539. [Wydarzenia i Przepustka [new_season_former_global_growth_piece_to_current_piece_desc] — tekst] 기존에 보유하였던 동기화 · 환상해석 전용 파편 (공용)의 일정량이 현재 시즌으로 이월됩니다.
   źródło: SeasonTitle-a1c7.json :: dataList[id=new_season_former_global_growth_piece_to_current_piece_desc].content
   limit: do 150 znaków
   EN: A portion of the Uptie & Threadspinning only Shard (Universal) you own will be carried over to the current season.
   PL: Część posiadanych Odłamków przeznaczonych wyłącznie do Synchronizacji · Analizy Anomalii (wspólnych) przechodzi na bieżący sezon.
540. [Wydarzenia i Przepustka [new_season_former_global_growth_piece_to_thread_desc] — tekst] 이월되지 않은 동기화 · 환상해석 전용 파편 (공용)은 끈으로 변경됩니다.
   źródło: SeasonTitle-a1c7.json :: dataList[id=new_season_former_global_growth_piece_to_thread_desc].content
   limit: do 130 znaków
   EN: The Uptie & Threadspinning only Shards that have not been carried over are converted into Thread.
   PL: Nieprzeniesione Odłamki przeznaczone wyłącznie do Synchronizacji · Analizy Anomalii (wspólne) zostają zamienione na Nić.

## Wydarzenia i Przepustka: SeasonTitle
- plik gry: `SeasonTitle.json`

541. [Wydarzenia i Przepustka [season_title_1] — tekst] ORIENTATION
   źródło: SeasonTitle.json :: dataList[id=season_title_1].content
   limit: do 120 znaków
   EN: ORIENTATION
   PL: ORIENTATION
542. [Wydarzenia i Przepustka [season_title_1_EVENT] — tekst] ORIENTATION [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_1_EVENT].content
   limit: do 120 znaków
   EN: ORIENTATION [EVENT]
   PL: ORIENTATION [EVENT]
543. [Wydarzenia i Przepustka [season_title_2] — tekst] REMINISCENCE
   źródło: SeasonTitle.json :: dataList[id=season_title_2].content
   limit: do 120 znaków
   EN: REMINISCENCE
   PL: REMINISCENCE
544. [Wydarzenia i Przepustka [season_title_2_EVENT] — tekst] REMINISCENCE [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_2_EVENT].content
   limit: do 120 znaków
   EN: REMINISCENCE [EVENT]
   PL: REMINISCENCE [EVENT]
545. [Wydarzenia i Przepustka [season_9101_walpurgisnacht] — tekst] 발푸르기스의 밤
   źródło: SeasonTitle.json :: dataList[id=season_9101_walpurgisnacht].content
   limit: do 120 znaków
   EN: Walpurgis Night
   PL: Noc Walpurgii
546. [Wydarzenia i Przepustka [season_title_3] — tekst] BON VOYAGE
   źródło: SeasonTitle.json :: dataList[id=season_title_3].content
   limit: do 120 znaków
   EN: BON VOYAGE
   PL: BON VOYAGE
547. [Wydarzenia i Przepustka [season_title_3_EVENT] — tekst] BON VOYAGE [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_3_EVENT].content
   limit: do 120 znaków
   EN: BON VOYAGE [EVENT]
   PL: BON VOYAGE [EVENT]
548. [Wydarzenia i Przepustka [season_filter_3] — tekst] 시즌 3
   źródło: SeasonTitle.json :: dataList[id=season_filter_3].content
   limit: do 120 znaków
   EN: Season 3
   PL: Sezon 3
549. [Wydarzenia i Przepustka [season_title_4] — tekst] CLEAR ALL CATHY
   źródło: SeasonTitle.json :: dataList[id=season_title_4].content
   limit: do 120 znaków
   EN: CLEAR ALL CATHY
   PL: CLEAR ALL CATHY
550. [Wydarzenia i Przepustka [season_title_4_EVENT] — tekst] CLEAR ALL CATHY [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_4_EVENT].content
   limit: do 120 znaków
   EN: CLEAR ALL CATHY [EVENT]
   PL: CLEAR ALL CATHY [EVENT]
551. [Wydarzenia i Przepustka [season_filter_4] — tekst] 시즌 4
   źródło: SeasonTitle.json :: dataList[id=season_filter_4].content
   limit: do 120 znaków
   EN: Season 4
   PL: Sezon 4
552. [Wydarzenia i Przepustka [season_title_5] — tekst] OBLIVION
   źródło: SeasonTitle.json :: dataList[id=season_title_5].content
   limit: do 120 znaków
   EN: OBLIVION
   PL: OBLIVION
553. [Wydarzenia i Przepustka [season_title_5_EVENT] — tekst] OBLIVION [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_5_EVENT].content
   limit: do 120 znaków
   EN: OBLIVION [EVENT]
   PL: OBLIVION [EVENT]
554. [Wydarzenia i Przepustka [season_filter_5] — tekst] 시즌 5
   źródło: SeasonTitle.json :: dataList[id=season_filter_5].content
   limit: do 120 znaków
   EN: Season 5
   PL: Sezon 5
555. [Wydarzenia i Przepustka [season_filter_6] — tekst] 시즌 6
   źródło: SeasonTitle.json :: dataList[id=season_filter_6].content
   limit: do 120 znaków
   EN: Season 6
   PL: Sezon 6
556. [Wydarzenia i Przepustka [season_title_6] — tekst] Zàng Huā Yín
   źródło: SeasonTitle.json :: dataList[id=season_title_6].content
   limit: do 120 znaków
   EN: Zàng Huā Yín
   PL: Zàng Huā Yín
557. [Wydarzenia i Przepustka [season_title_6_EVENT] — tekst] Zàng Huā Yín [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_6_EVENT].content
   limit: do 120 znaków
   EN: Zàng Huā Yín [EVENT]
   PL: Zàng Huā Yín [EVENT]
558. [Wydarzenia i Przepustka [season_8000_collaboration] — tekst] 콜라보레이션 한정
   źródło: SeasonTitle.json :: dataList[id=season_8000_collaboration].content
   limit: do 120 znaków
   EN: COLLABORATION - LIMITED
   PL: Kolaboracja Limitowana
559. [Wydarzenia i Przepustka [season_8000_collaboration_filter_title] — tekst] 콜라보레이션 한정
   źródło: SeasonTitle.json :: dataList[id=season_8000_collaboration_filter_title].content
   limit: do 120 znaków
   EN: COLLAB ONLY
   PL: Kolaboracja Limitowana
560. [Wydarzenia i Przepustka [season_filter_7] — tekst] 시즌 7
   źródło: SeasonTitle.json :: dataList[id=season_filter_7].content
   limit: do 120 znaków
   EN: Season 7
   PL: Sezon 7
561. [Wydarzenia i Przepustka [season_title_7] — tekst] Kumo no ito · oti on akA
   źródło: SeasonTitle.json :: dataList[id=season_title_7].content
   limit: do 120 znaków
   EN: Kumo no ito · oti on akA
   PL: Kumo no ito · oti on akA
562. [Wydarzenia i Przepustka [season_title_7_EVENT] — tekst] Kumo no ito · oti on akA [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_7_EVENT].content
   limit: do 120 znaków
   EN: Kumo no ito · oti on akA [EVENT]
   PL: Kumo no ito · oti on akA [EVENT]
563. [Wydarzenia i Przepustka [season_filter_8] — tekst] 시즌 8
   źródło: SeasonTitle.json :: dataList[id=season_filter_8].content
   limit: do 120 znaków
   EN: Season 8
   PL: Sezon 8
564. [Wydarzenia i Przepustka [season_title_8] — tekst] PUNCTUM
   źródło: SeasonTitle.json :: dataList[id=season_title_8].content
   limit: do 120 znaków
   EN: PUNCTUM
   PL: PUNCTUM
565. [Wydarzenia i Przepustka [season_title_8_EVENT] — tekst] PUNCTUM [EVENT]
   źródło: SeasonTitle.json :: dataList[id=season_title_8_EVENT].content
   limit: do 120 znaków
   EN: PUNCTUM [EVENT]
   PL: PUNCTUM [EVENT]

## Wydarzenia i Przepustka: TwiningThreadsEvent
- plik gry: `TwiningThreadsEvent.json`

566. [Wydarzenia i Przepustka [twining_threads_stage_button_default] — tekst] 스테이지
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_stage_button_default].content
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
567. [Wydarzenia i Przepustka [twining_threads_stage_button_locked] — tekst] 9장 클리어 시 개방
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_stage_button_locked].content
   limit: do 120 znaków
   EN: Clear Canto IX to Unlock
   PL: Odblokowanie po ukończeniu 9. rozdziału
568. [Wydarzenia i Przepustka [twining_threads_storybutton_default] — tekst] 상영관 이동
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_storybutton_default].content
   (powtórzenie elementu 261 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Wydarzenia i Przepustka [twining_threads_storybutton_start] — tekst] <size=75%>이벤트 첫 번째 이야기\n감상 시 개방</size>
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_storybutton_start].content
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Wydarzenia i Przepustka [twining_threads_stage_button_end_event] — tekst] 이벤트 기간 종료
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_stage_button_end_event].content
   (powtórzenie elementu 263 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Wydarzenia i Przepustka [twining_threads_bonus_popup_title] — tekst] 이벤트 특화 대상
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_bonus_popup_title].content
   (powtórzenie elementu 264 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Wydarzenia i Przepustka [twining_threads_bonusUIDesc] — tekst] 이벤트 기간 동안 해당 인격 편성 시, <color=#5c53e7>[잘린 실]</color>의 획득량이 상승합니다.\n획득량 상승치 합계는 최대 <color=#5c53e7>120%</color>까지 적용됩니다.
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_bonusUIDesc].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: <color=#5c53e7>, </color>, \n
   EN: During the event period, deploying the following Identities on your team will\nboost the amount of <color=#5c53e7>[Severed Thread]</color> earned.\nYou can earn a maximum of <color=#5c53e7>120%</color> boost to the amount of event currency earned.
   PL: W okresie wydarzenia, mając w składzie wskazane Tożsamości, zwiększasz zdobywanie <color=#5c53e7>[Odciętych Nici]</color>.\nSuma wzrostu zdobyczy może osiągnąć maksymalnie <color=#5c53e7>120%</color>.
573. [Wydarzenia i Przepustka [twining_threads_scrap_guide_title] — tekst] 이벤트 재화 안내
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_scrap_guide_title].content
   (powtórzenie elementu 266 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Wydarzenia i Przepustka [twining_threads_scrap_guide_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어,\n거울 던전 클리어를 통해 <color=#5c53e7>[잘린 실]</color>을 획득할 수 있으며,\n낮은 확률로 <color=#5c53e7>[잘리고 타버린 실뭉치]</color>를 추가로 획득할 수 있습니다.\n\n<color=#5c53e7>[잘리고 타버린 실뭉치]</color>는 획득 즉시, <color=#5c53e7>[잘린 실]</color> 20개로 전환됩니다.
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_scrap_guide_desc].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#5c53e7>, </color>, \n
   EN: You can obtain <color=#5c53e7>[Severed Thread]</color> from first-time Event/Main Story Stages completions, or by clearing the Mirror Dungeon.\nYou also have a small chance to obtain <color=#5c53e7>[Severed and Scorched Skein]</color> in the process.\n\n<color=#5c53e7>[Severed and Scorched Skein]</color> is immediately converted to 20 <color=#5c53e7>[Severed Thread]</color> upon acquisition.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#5c53e7>[Odcięte Nici]</color>, a z pewnym prawdopodobieństwem dodatkowo <color=#5c53e7>[Odcięty i Nadpalony Motek]</color>.\n\n<color=#5c53e7>[Odcięty i Nadpalony Motek]</color> od razu zamienia się na 20 <color=#5c53e7>[Odciętych Nici]</color>.
575. [Wydarzenia i Przepustka [twining_threads_reward_popup_desc] — tekst] 이벤트 스테이지와 주요 이야기 최초 클리어, 거울 던전 클리어를 통해 <color=#eeeeee>[잘린 실]</color>을 획득할 수 있습니다.\n\n<color=#eeeeee>[보상 교환]</color>창에서 <color=#eeeeee>[잘린 실]</color>을 지불하여 다양한 보상을 얻을 수 있습니다.
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_reward_popup_desc].content
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#eeeeee>, </color>, \n
   EN: Earn <color=#eeeeee>[Severed Thread]</color> via the following methods:\nFirst-time Event Stage & Main Story Stage clears and Mirror Dungeon clears.\n\nIn the <color=#eeeeee>[Reward Exchange]</color> window, you can purchase various rewards\nby spending <color=#eeeeee>[Severed Thread]</color> you have collected.
   PL: Ukończoną pierwsze etapy wydarzenia i Głównej Opowieści albo Lustrzane Lochy, zdobywasz <color=#eeeeee>[Odcięte Nici]</color>.\n\nW oknie <color=#eeeeee>[Wymiany nagród]</color> możesz kupić różne nagrody za zebrane <color=#eeeeee>[Odcięte Nici]</color>.
576. [Wydarzenia i Przepustka [twining_threads_reward_popup_num_of_owned_items] — tekst] 보유 아이템 수
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_reward_popup_num_of_owned_items].content
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Wydarzenia i Przepustka [twining_threads_rewardShopButton] — tekst] 보상 교환
   źródło: TwiningThreadsEvent.json :: dataList[id=twining_threads_rewardShopButton].content
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Wydarzenia i Przepustka: Walpu10EventText
- plik gry: `Walpu10EventText.json`

578. [Wydarzenia i Przepustka [Walpu10_reward_event_desc] — tekst] 제10회 발푸르기스의 밤 쉬움, 어려움 난이도 전투에서 미션을 클리어하세요.\n\n미션을 클리어하면 다양한 보상을 얻을 수 있습니다.
   źródło: Walpu10EventText.json :: dataList[id=Walpu10_reward_event_desc].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Complete missions in the Easy and Hard Difficulty battles of the 10th Walpurgis Night.\n\nClear missions to earn various rewards.
   PL: Ukończ misje w walkach na Poziomach Łatwym i Trudnym 10. Nocy Walpurgii.\n\nZa ukończone misje otrzymasz różne nagrody.
579. [Wydarzenia i Przepustka [Walpu10_reward_normal_tab] — tekst] 쉬움 난이도
   źródło: Walpu10EventText.json :: dataList[id=Walpu10_reward_normal_tab].content
   limit: do 120 znaków
   EN: Easy
   PL: Poziom Łatwy
580. [Wydarzenia i Przepustka [Walpu10_reward_hard_tab] — tekst] 어려움 난이도
   źródło: Walpu10EventText.json :: dataList[id=Walpu10_reward_hard_tab].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
581. [Wydarzenia i Przepustka [missionConditionTitle_10159] — tekst] 1회 전투에서 새벽 사무소 해결사를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10159].content
   limit: do 120 znaków
   EN: Complete the Reception after defeating all Dawn Office Fixers in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy wszystkich Fikserów Biura Świtu w jednej walce
582. [Wydarzenia i Przepustka [missionConditionTitle_hidden_10159] — tekst] 1회 전투에서 ???를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_10159].content
   limit: do 120 znaków
   EN: Complete the Reception after defeating all ??? in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy wszystkich ??? w jednej walce
583. [Wydarzenia i Przepustka [missionConditionTitle_10160] — tekst] 1회 전투에서 쐐기 사무소 해결사를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10160].content
   limit: do 120 znaków
   EN: Complete the Reception after defeating all Wedge Office Fixers in a single Encounter
   PL: Ukończ Przyjęcie, pokonawszy wszystkich Fikserów Biura Klina w jednej walce
584. [Wydarzenia i Przepustka [missionConditionTitle_hidden_10160] — tekst] 1회 전투에서 ???를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_10160].content
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Wydarzenia i Przepustka [missionConditionTitle_10161] — tekst] 새벽 사무소 / 쐐기 사무소 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10161].content
   limit: do 120 znaków
   EN: Complete the Dawn Office / Wedge Office Reception
   PL: Ukończ Przyjęcie Biura Świtu / Biura Klina
586. [Wydarzenia i Przepustka [missionConditionTitle_hidden_10161] — tekst] ??? 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_10161].content
   limit: do 120 znaków
   EN: Complete ??? Reception
   PL: Ukończ Przyjęcie ???
587. [Wydarzenia i Przepustka [missionConditionTitle_10162] — tekst] 1회 전투에서 불확실한 슬픔의 감정을 최대 5까지 획득하지 않은 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10162].content
   limit: do 130 znaków
   EN: Complete the Reception without ever reaching 5 Emotion of Uncertain Sorrow in a single Encounter
   PL: Ukończ Przyjęcie, nigdy nie osiągając 5 Emocji Niepewnego Smutku w jednej walce
588. [Wydarzenia i Przepustka [missionConditionTitle_hidden_10162] — tekst] 1회 전투에서 ???을 최대 5까지 획득하지 않은 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_10162].content
   limit: do 120 znaków
   EN: Complete the Reception without ever reaching 5 ??? in a single Encounter
   PL: Ukończ Przyjęcie, nigdy nie osiągając 5 ??? w jednej walce
589. [Wydarzenia i Przepustka [missionConditionTitle_10163] — tekst] 지정 사서 버프가 있는 아군이 1회 전투에서 합을 10회 이상 승리하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10163].content
   limit: do 150 znaków
   EN: Complete the Reception with the ally that has the Patron Librarian buff winning 10+ Clashes in a single Encounter
   PL: Ukończ Przyjęcie, gdy sojusznik z Wyznaczonym Bibliotekarzem wygra 10+ Starć w jednej walce
590. [Wydarzenia i Przepustka [missionConditionTitle_10164] — tekst] 지정 사서 버프가 있는 아군이 1회 전투에서 적을 2명 이상 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10164].content
   limit: do 160 znaków
   EN: Complete the Reception with the ally that has the Patron Librarian buff defeating 2 or more enemies in a single Encounter
   PL: Ukończ Przyjęcie, gdy sojusznik z Wyznaczonym Bibliotekarzem pokona 2 lub więcej wrogów w jednej walce
591. [Wydarzenia i Przepustka [missionConditionTitle_10165] — tekst] 감정 단계 2단계 달성한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10165].content
   limit: do 120 znaków
   EN: Complete the Reception after reaching Emotion Level 2
   PL: Ukończ Przyjęcie po osiągnięciu Poziomu Emocji 2
592. [Wydarzenia i Przepustka [missionConditionTitle_10166] — tekst] 쐐기 사무소 해결사들의 연계 스킬을 5회 이상 발동시키지 않고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10166].content
   limit: do 130 znaków
   EN: Complete the Reception with fewer than 5 activations of the Wedge Office Fixers' combo Skills
   PL: Ukończ Przyjęcie z mniej niż 5 aktywacjami Umiejętności łączonych Fikserów Biura Klina
593. [Wydarzenia i Przepustka [missionConditionTitle_10167] — tekst] 1회 전투에서 공격 스킬 1개(ego 스킬, 반격 스킬 포함)로 적 1개체에게 가한 피해량 300 이상 달성하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10167].content
   limit: do 200 znaków
   EN: Complete the Reception after dealing at least 300 Damage to a single enemy using 1 Attack Skill (including E.G.O and Counter Skills) in a single Encounter
   PL: Ukończ Przyjęcie, zadając co najmniej 300 obrażeń pojedynczemu wrogowi 1 Umiejętnością ataku (w tym Umiejętnością ego i Kontry) w jednej walce
594. [Wydarzenia i Przepustka [missionConditionTitle_10168] — tekst] 모든 아군이 생존한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10168].content
   limit: do 120 znaków
   EN: Complete the Reception with all allies surviving
   PL: Ukończ Przyjęcie z wszystkimi sojusznikami przy życiu
595. [Wydarzenia i Przepustka [missionConditionTitle_10169] — tekst] 모든 아군이 정신력 -45에 도달하지 않고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10169].content
   limit: do 120 znaków
   EN: Complete the Reception without any ally reaching -45 SP
   PL: Ukończ Przyjęcie, nie dopuszczając, by jakikolwiek sojusznik osiągnął -45 Poczytalności
596. [Wydarzenia i Przepustka [missionConditionTitle_10170] — tekst] 아군이 5회 이상 흐트러지지 않고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_10170].content
   limit: do 120 znaków
   EN: Complete the Reception with allies becoming Staggered fewer than 5 times
   PL: Ukończ Przyjęcie, nie dopuszczając do Oszołomienia sojuszników 5 razy lub więcej
597. [Wydarzenia i Przepustka [missionConditionTitle_20080] — tekst] 1회 전투에서 새벽 사무소 해결사를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20080].content
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20080] — tekst] 1회 전투에서 ???를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20080].content
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Wydarzenia i Przepustka [missionConditionTitle_20081] — tekst] 1회 전투에서 쐐기 사무소 해결사를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20081].content
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20081] — tekst] 1회 전투에서 ???를 모두 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20081].content
   (powtórzenie elementu 582 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Wydarzenia i Przepustka [missionConditionTitle_20082] — tekst] 새벽 사무소 / 쐐기 사무소 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20082].content
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
602. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20082] — tekst] ??? 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20082].content
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Wydarzenia i Przepustka [missionConditionTitle_20083] — tekst] 1회 전투에서 불확실한 슬픔의 감정을 최대 5까지 획득하지 않은 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20083].content
   (powtórzenie elementu 587 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20083] — tekst] 1회 전투에서 ???을 최대 5까지 획득하지 않은 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20083].content
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Wydarzenia i Przepustka [missionConditionTitle_20084] — tekst] 지정 사서 버프가 있는 아군이 1회 전투에서 합을 10회 이상 승리하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20084].content
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Wydarzenia i Przepustka [missionConditionTitle_20085] — tekst] 지정 사서 버프가 있는 아군이 1회 전투에서 적을 3명 이상 처치한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20085].content
   limit: do 160 znaków
   EN: Complete the Reception with the ally that has the Patron Librarian buff defeating 3 or more enemies in a single Encounter
   PL: Ukończ Przyjęcie, gdy sojusznik z Wyznaczonym Bibliotekarzem pokona 3 lub więcej wrogów w jednej walce
607. [Wydarzenia i Przepustka [missionConditionTitle_20086] — tekst] 아군이 1회 전투에서 필립의 타오르는 일격 스킬과의 합을 1회 이상 승리하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20086].content
   limit: do 160 znaków
   EN: Complete the Reception after an ally wins at least 1 Clash against Philip's "Blazing Strike" Skill in a single Encounter
   PL: Ukończ Przyjęcie, gdy sojusznik wygra co najmniej 1 Starcie z Umiejętnością „Płonący Cios” Philipa w jednej walce
608. [Wydarzenia i Przepustka [missionConditionTitle_hidden_20086] — tekst] 아군이 1회 전투에서 ???의 ??? 스킬과의 합을 1회 이상 승리하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_hidden_20086].content
   limit: do 140 znaków
   EN: Complete the Reception after an ally wins at least 1 Clash against ???'s ??? Skill in a single Encounter
   PL: Ukończ Przyjęcie, gdy sojusznik wygra co najmniej 1 Starcie z Umiejętnością ??? jednostki ??? w jednej walce
609. [Wydarzenia i Przepustka [missionConditionTitle_20087] — tekst] 감정 단계 3단계 달성한 상태로 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20087].content
   limit: do 120 znaków
   EN: Complete the Reception after reaching Emotion Level 3
   PL: Ukończ Przyjęcie po osiągnięciu Poziomu Emocji 3
610. [Wydarzenia i Przepustka [missionConditionTitle_20088] — tekst] 1회 전투에서 공격 스킬 1개(ego 스킬, 반격 스킬 포함)로 적 1개체에게 가한 피해량 300 이상 달성하고 접대 성공
   źródło: Walpu10EventText.json :: dataList[id=missionConditionTitle_20088].content
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
