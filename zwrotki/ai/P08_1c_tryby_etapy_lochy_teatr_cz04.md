# Paczka AI P08 (Fala 1 · 1C) — Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI) (część 4/6)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P08_1c_tryby_etapy_lochy_teatr_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P08_1c_tryby_etapy_lochy_teatr_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryby lochów i Kolei Refrakcji: BossRaidUI
- plik gry: `BossRaidUI.json`

1. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_result] — tekst] 전투 결과
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_result].content
   limit: do 120 znaków
   EN: Battle Outcome
   PL: Wynik walki
2. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_total_turn] — tekst] 누적 턴수
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_total_turn].content
   limit: do 120 znaków
   EN: Total Turns
   PL: Łączna liczba tur
3. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_statistics_button_label] — tekst] 상세 정보
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_statistics_button_label].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
4. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_party_formation] — tekst] 참여 편성
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_party_formation].content
   limit: do 120 znaków
   EN: Teams Played
   PL: Użyte składy
5. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_party_turn] — tekst] 턴수
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_party_turn].content
   limit: do 120 znaków
   EN: Turn Count
   PL: Liczba tur
6. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_party_give_damage] — tekst] 가한 피해량
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_party_give_damage].content
   limit: do 120 znaków
   EN: Damage Dealt
   PL: Zadane obrażenia
7. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_party_receive_damage] — tekst] 받은 피해량
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_party_receive_damage].content
   limit: do 120 znaków
   EN: Damage Taken
   PL: Otrzymane obrażenia
8. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_total_turn] — tekst] 전체 누적 턴수
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_total_turn].content
   limit: do 120 znaków
   EN: Total Turns
   PL: Łączna liczba tur
9. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_settings_title] — tekst] 환경 설정
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_settings_title].content
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
10. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_settings_desc] — tekst] 게임 내 시스템 및 주요 환경을 조정합니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_settings_desc].content
   limit: do 120 znaków
   EN: Adjust various in-game settings.
   PL: Dostosuj ustawienia systemowe i opcje gry.
11. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_retry_title] — tekst] 스테이지 재도전
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_retry_title].content
   limit: do 120 znaków
   EN: Retry Stage
   PL: Ponów etap
12. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_retry_desc] — tekst] 현재 설정한 편성 상태를 유지한 채로 스테이지를 재도전합니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_retry_desc].content
   limit: do 120 znaków
   EN: Retry the Stage with your current Team loadout.
   PL: Ponów etap z zachowaniem bieżącego składu drużyny.
13. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_exit_title] — tekst] 스테이지 포기
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_exit_title].content
   limit: do 120 znaków
   EN: Forfeit Stage
   PL: Poddaj etap
14. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_exit_desc] — tekst] 진행 중인 스테이지를 포기하고 전투 진입 전으로 돌아갑니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_exit_desc].content
   limit: do 120 znaków
   EN: Forfeit the current Stage progress and return to the pre-battle state.
   PL: Poddaj bieżący etap i wróć do stanu sprzed wejścia do walki.
15. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_end_title] — tekst] 스테이지 종료 후 진행도 저장
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_end_title].content
   limit: do 120 znaków
   EN: Quit Battle and Save Progress
   PL: Zakończ walkę i zapisz postęp
16. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_end_desc] — tekst] 진행 중인 스테이지를 종료하고 진행도를 저장합니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_end_desc].content
   limit: do 120 znaków
   EN: Quit the current Stage and save your progress.
   PL: Zakończ bieżący etap i zapisz dotychczasowy postęp.
17. [Tryby lochów i Kolei Refrakcji [boss_raid_10001_boss_title] — tekst] 약지 야수파 도슨트 루포
   źródło: BossRaidUI.json :: dataList[id=boss_raid_10001_boss_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rufo, Docent of \nThe Ring's School of Fauvism
   PL: Rufo, Docent Fowizmu\nSerdecznego Palca
18. [Tryby lochów i Kolei Refrakcji [boss_raid_10001_banner_title] — tekst] 타래 엮기
   źródło: BossRaidUI.json :: dataList[id=boss_raid_10001_banner_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Twining<size=46%>\n\n</size>Threads
   PL: Splatanie Pasm
19. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_current_formation] — tekst] 현재 도전 중 :: 편성 {0}
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_current_formation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Trial in Progress :: TEAM {0}
   PL: Próba w toku :: Skład {0}
20. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_phase_before] — tekst] PHASE {0}\n진행 전
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_phase_before].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: PHASE {0}\nUnreached
   PL: FAZA {0}\nPrzed wejściem
21. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_phase_current] — tekst] PHASE {0}\n진행 중
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_phase_current].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: PHASE {0}\nIn Progress
   PL: FAZA {0}\nW toku
22. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_phase_cleared] — tekst] PHASE {0}\n완료
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_phase_cleared].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: PHASE {0}\nComplete
   PL: FAZA {0}\nUkończono
23. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_enter_from_event_ui] — tekst] 사영전투][투전영사
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_enter_from_event_ui].content
   limit: do 120 znaków
   EN: Reflectrial][lairtcelfeR
   PL: Walka Projekcyjna][anjyckejorP aklaW
24. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_failed] — tekst] 전투 결과
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_failed].content
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_progressing] — tekst] 진행 중인 전투
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_progressing].content
   limit: do 120 znaków
   EN: Battle in Progress
   PL: Walka w toku
26. [Tryby lochów i Kolei Refrakcji [boss_raid_reward_ui_turn_condition] — tekst] {0}턴 이하
   źródło: BossRaidUI.json :: dataList[id=boss_raid_reward_ui_turn_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Turns or less
   PL: Maks. {0} tur
27. [Tryby lochów i Kolei Refrakcji [boss_raid_reward_ui_warning_10001] — tekst] <size=80%>※ 2026. 04. 23 12:00 ~ 2026. 05. 21 10:00 (KST) 총 4주 동안 보상을 수령할 수 있습니다.\n수령 기한이 지나면 보상을 획득할 수 없으니 주의하시길 바랍니다.</size>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_reward_ui_warning_10001].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <size=80%>, </size>, \n
   EN: <size=80%>※ Reward claim period is open for a total of 4 weeks, from 2026. 04. 23 12:00 to 2026. 05. 21 10:00 (KST)\nPlease note that rewards cannot be claimed past the Reward claim period.</size>
   PL: <size=80%>※ Nagrody można odebrać przez 4 tygodnie: od 23.04.2026 12:00 do 21.05.2026 10:00 (KST).\nPamiętaj, że po upływie tego terminu odbiór nagród będzie niemożliwy.</size>
28. [Tryby lochów i Kolei Refrakcji [boss_raid_reward_tab_text_NORMAL] — tekst] 노말 보상
   źródło: BossRaidUI.json :: dataList[id=boss_raid_reward_tab_text_NORMAL].content
   limit: do 120 znaków
   EN: Normal
   PL: Normalny
29. [Tryby lochów i Kolei Refrakcji [boss_raid_reward_tab_text_HARD] — tekst] 하드 보상
   źródło: BossRaidUI.json :: dataList[id=boss_raid_reward_tab_text_HARD].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
30. [Tryby lochów i Kolei Refrakcji [boss_raid_result_ui_formation_number] — tekst] 편성 {0}
   źródło: BossRaidUI.json :: dataList[id=boss_raid_result_ui_formation_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Team {0}
   PL: Skład {0}
31. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_title] — tekst] 스테이지 종료 후 진행도 저장
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_title].content
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
32. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_desc] — tekst] 진행 중인 전투를 종료하고\n다음 편성으로 이어서 전투를 진행하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Quit the battle in progress\nand resume with your next Team?
   PL: Zakończyć trwającą walkę\ni kontynuować następnym składem?
33. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_desc_detail] — tekst] <size=80%>확인 버튼 선택 시, <color=#f8c200>보스의 페이즈와\n체력, 정신력, 남은 E.G.O 자원이 저장</color>되고\n다음 편성으로 이어서 전투를 진행할 수 있습니다.</size>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_desc_detail].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <size=80%>, <color=#f8c200>, </color>, </size>, \n
   EN: <size=80%>Selecting "Confirm" below will <color=#f8c200>save the boss enemy's current phase, HP, SP, and your remaining E.G.O resources</color>.\nThen, you can choose to continue with your next Team of choice.</size>
   PL: <size=80%>Po potwierdzeniu <color=#f8c200>faza bossa,\njego PŻ, SP oraz pozostałe zasoby E.G.O zostaną zapisane</color>,\na walkę będzie można kontynuować kolejnym składem.</size>
34. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_exit_popup_title] — tekst] 스테이지 포기
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_exit_popup_title].content
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
35. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_exit_popup_desc] — tekst] 진행 중인 전투를 포기하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_exit_popup_desc].content
   limit: do 120 znaków
   EN: Forfeit the battle in progress?
   PL: Czy poddać trwającą walkę?
36. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_exit_popup_desc_detail] — tekst] <size=80%>확인 버튼 선택 시, 현재 편성이\n<color=#f8c200>전투에 참여하기 직전</color>의 상태로 돌아갑니다.</size>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_exit_popup_desc_detail].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <size=80%>, <color=#f8c200>, </color>, </size>, \n
   EN: <size=80%>Selecting "Confirm" below will revert you to the state <color=#f8c200>immediately before entering the battle</color> with your current Team.</size>
   PL: <size=80%>Po potwierdzeniu bieżący skład powróci do stanu\n<color=#f8c200>tuż sprzed przystąpienia do walki</color>.</size>
37. [Tryby lochów i Kolei Refrakcji [boss_raid_phase_buff_view_ui_title] — tekst] 적용 효과
   źródło: BossRaidUI.json :: dataList[id=boss_raid_phase_buff_view_ui_title].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
38. [Tryby lochów i Kolei Refrakcji [boss_raid_rule_popup_title] — tekst] 진행 방식
   źródło: BossRaidUI.json :: dataList[id=boss_raid_rule_popup_title].content
   limit: do 120 znaków
   EN: Progression
   PL: Zasady trybu
39. [Tryby lochów i Kolei Refrakcji [boss_raid_rule_popup_desc_10001] — tekst] - ‘사영전투][투전영사’는 <color=#ff0000>고난이도 콘텐츠</color>로,\n인격과 E.G.O를 권장 사양에 맞추어 <color=#ff0000>충분히 성장시킨 후 도전</color>하는 것을 권장드립니다.\n(※ 지원 인격은 사용할 수 없습니다.)\n\n- 보스 전투마다 특별한 효과가 반영됩니다.\n사영 효과는 모든 난이도, <color=#f8c200>고난은 Hard 난이도</color>에서만 적용됩니다.\n\n- 전투에서는 최대 <color=#f8c200>3개의 편성</color>을 순차적으로 사용할 수 있습니다.\n단, 이전 편성에 포함된 인격은 이후 편성에서 다시 사용할 수 없습니다.\n\n- 편성 하나당 최대 <color=#f8c200>12턴</color> 동안 전투를 진행할 수 있습니다.\n전투 진행 중 12턴이 넘거나 전투 종료를 선택하면\n보스의 페이즈와 체력, 정신력, 남은 E.G.O 자원이 저장되고\n다음 편성으로 이어서 진행할 수 있습니다.\n(※ 보스의 패턴, 보스 이외 적들의 체력과 정신력, 적들이 보유한 효과는 저장되지 않습니다.)\n\n- 두 번째 편성부터는 입장할 때 누적 턴수에 비례하여\n<color=#f8c200>시작 정신력이 증가</color>합니다 (※ 턴당 5).\n\n빼기 코인을 사용하는 인격의 경우에는 시작 정신력이 음수 값으로 적용됩니다 (※ 턴당 -5, 최소 -25).
   źródło: BossRaidUI.json :: dataList[id=boss_raid_rule_popup_desc_10001].content
   limit: do 1520 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, <color=#f8c200>, \n
   EN: - "Reflectrial][lairtcelfeR" is a <color=#ff0000>high-difficulty challenge</color>.\nLevel up and Uptie/Threadspin your Identities and E.G.O to <color=#ff0000>meet the recommended specs</color> before entering the battle.\n(※ Support Identities cannot be used.)\n\n- Each boss battle features unique effects.\n"Shade of Reflection" effects apply on all difficulties.\n<color=#f8c200>"Tribulation" effects apply on Hard Difficulty only.</color>\n\n- Reflectrial][lairtcelfeR battles <color=#f8c200>allow a maximum of 3 Team Loadouts</color> to be used in order.\nHowever, Identities assigned to a previous loadout cannot be reused in subsequent Loadouts.\n\n- <color=#f8c200>A 12-turn limit</color> is applied to each Team Loadout.\nExceeding 12 turns or opting to end the battle on your current loadout will save the state of battle progression (Boss Unit's Combat Phase, HP, and SP; as well as E.G.O Resources owned). You may continue progressing through the battle with the next loadout.'\n(※ The Boss unit's pattern, the non-Boss enemies' HP and SP, and status effects on enemies are not saved)\n\n- Starting from the second Loadout, <color=#f8c200>the starting SP of your team increases</color> upon entering the battle, based on the cumulative Turn count (※ 5 per turn).\n\nMinus Coin Identities start with negative SP numbers instead (※ -5 per turn, min -25).
   PL: - „Walka Projekcyjna][anjyckejorP aklaW” to <color=#ff0000>wyzwanie o wysokim poziomie trudności</color>.\nZalecamy przystąpienie do walki dopiero po <color=#ff0000>odpowiednim rozwinięciu Tożsamości i E.G.O</color> zgodnie z zalecanymi parametrami.\n(※ Nie można korzystać z Tożsamości Wsparcia.)\n\n- Każda walka z bossem posiada unikalne efekty.\nEfekty Odbicia działają na wszystkich poziomach trudności, natomiast <color=#f8c200>Próby wyłącznie na poziomie Trudnym</color>.\n\n- W walce można użyć kolejno maksymalnie <color=#f8c200>3 składów drużyny</color>.\nTożsamości użyte we wcześniejszym składzie nie mogą jednak zostać wybrane ponownie w kolejnych składach.\n\n- Każdy skład drużyny może walczyć przez maksymalnie <color=#f8c200>12 tur</color>.\nPo przekroczeniu 12 tur lub ręcznym zakończeniu walki dla bieżącego składu\nfaza bossa, jego PŻ i SP oraz pozostałe zasoby E.G.O zostaną zapisane,\nco pozwoli kontynuować starcie kolejnym składem.\n(※ Schemat ataków bossa, PŻ i SP pozostałych wrogów oraz nałożone na wrogów efekty nie są zapisywane.)\n\n- Począwszy od drugiego składu, przy wejściu do walki proporcjonalnie do łącznej liczby tur\n<color=#f8c200>wzrasta początkowe SP</color> sojuszników (※ +5 za turę).\n\nW przypadku Tożsamości z Monetami Ujemnymi początkowe SP przyjmuje wartości ujemne (※ -5 za turę, min. -25).
40. [Tryby lochów i Kolei Refrakcji [boss_raid_reward_ui_only_clear] — tekst] 전투 클리어
   źródło: BossRaidUI.json :: dataList[id=boss_raid_reward_ui_only_clear].content
   limit: do 120 znaków
   EN: Clear Battle
   PL: Ukończ walkę
41. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_view_current_progress_state] — tekst] 전투 현황
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_view_current_progress_state].content
   limit: do 120 znaków
   EN: Battle Progress
   PL: Stan walki
42. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_special_buff] — tekst] 사영 효과
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_special_buff].content
   limit: do 120 znaków
   EN: Effects: Shade of Reflection
   PL: Efekty Odbicia
43. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_special_buff_hardship] — tekst] 고난
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_special_buff_hardship].content
   limit: do 120 znaków
   EN: Tribulation
   PL: Próby
44. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_statistics_popup_title] — tekst] 상세 정보
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_statistics_popup_title].content
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Tryby lochów i Kolei Refrakcji [boss_raid_hard_ship_buff_apply_only_for_hard_alarm] — tekst] 고난 효과는 HARD 난이도에서만 적용됩니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_hard_ship_buff_apply_only_for_hard_alarm].content
   limit: do 120 znaków
   EN: Tribulation effects are activated only for the HARD Difficulty.
   PL: Efekty Prób działają wyłącznie na poziomie TRUDNYM.
46. [Tryby lochów i Kolei Refrakcji [boss_raid_warning_lack_of_personality_before_start] — tekst] 해당 콘텐츠에서는 최대 {0}개의 편성을 사용할 수 있으나, 현재 인격 수가 {0}개 미만인 수감자가 있습니다.\n전투에 참여한 인격은 이후 전투에서 사용할 수 없게 되므로, 진행 과정에서 편성을 만들 수 없어 <color=#ff0000>진행이 불가능한 상황</color>이 발생할 수 있습니다.\n그럼에도 불구하고 입장하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_warning_lack_of_personality_before_start].content
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, {0}, \n
   EN: Up to {0} Teams can be used for this content. However, there is a Sinner with fewer than {0} Identities.\nPlease note that this may cause your attempt to be incompletable, as once an Identity has participated in the battle, they become inaccessible for the rest of the attempt.\nWill you still enter?
   PL: W tym trybie można użyć maksymalnie {0} składów, jednak co najmniej jeden Grzesznik posiada mniej niż {0} Tożsamości.\nPonieważ Tożsamości użytych we wcześniejszej walce nie można wybrać ponownie, w dalszej części może zabraknąć jednostek do utworzenia składu i <color=#ff0000>dalsza gra stanie się niemożliwa</color>.\nCzy mimo to chcesz wejść?
47. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_ask_to_quit] — tekst] 확인 버튼 선택 시, 해당 보스의\n<color=#ff0000>현재 진행 중인 전투 기록이 완전히 초기화</color>됩니다.\n\n진행 상황을 초기화하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_ask_to_quit].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: Select "Confirm" below to <color=#ff0000>completely reset and erase the current battle progress.</color>\n\nReset battle progression?
   PL: Po potwierdzeniu <color=#ff0000>bieżący zapis postępu walki z tym bossem zostanie całkowicie zresetowany</color>.\n\nZresetować postęp?
48. [Tryby lochów i Kolei Refrakcji [boss_raid_preview_boss_info_button_label] — tekst] 적 정보\n확인
   źródło: BossRaidUI.json :: dataList[id=boss_raid_preview_boss_info_button_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: View\nEnemy Info
   PL: Informacje\no wrogach
49. [Tryby lochów i Kolei Refrakcji [boss_raid_difficulty_blocked] — tekst] 개방 조건 : {0}
   źródło: BossRaidUI.json :: dataList[id=boss_raid_difficulty_blocked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: To Unlock: {0}
   PL: Warunek odblokowania: {0}
50. [Tryby lochów i Kolei Refrakcji [boss_raid_next_difficulty_opened_side_popup] — tekst] {0} 난이도가 개방되었습니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_next_difficulty_opened_side_popup].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Difficulty unlocked.
   PL: Odblokowano poziom trudności: {0}.
51. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_recommend_state_title] — tekst] 권장 사양
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_recommend_state_title].content
   limit: do 120 znaków
   EN: Recommended Specs
   PL: Zalecane parametry
52. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_recommend_state_desc] — tekst] - 인격 : 동기화 <color=#ff0000>{1}단계</color>·레벨 <color=#ff0000>{0}</color>\n- E.G.O : 환상 해석 <color=#ff0000>{1}단계</color>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_recommend_state_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, {1}, {0}, \n
   EN: - Identities : Uptie <color=#ff0000>Tier {1}</color>, Level <color=#ff0000>{0}</color>\n- E.G.O : Threadspinning <color=#ff0000>Tier {1}</color>
   PL: - Tożsamości: Synchronizacja <color=#ff0000>poz. {1}</color> · Poziom <color=#ff0000>{0}</color>\n- E.G.O: Splot Nici <color=#ff0000>poz. {1}</color>
53. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_progressing] — tekst] 진행 중
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_progressing].content
   limit: do 120 znaków
   EN: In Progress
   PL: W toku
54. [Tryby lochów i Kolei Refrakcji [boss_raid_banned_personality_exist] — tekst] 사용할 수 없는 인격이 편성되어있습니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_banned_personality_exist].content
   limit: do 120 znaków
   EN: An Undeployable Identity is Deployed.
   PL: W składzie znajduje się niedozwolona Tożsamość.
55. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_title_last_formation] — tekst] 스테이지 종료
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_title_last_formation].content
   limit: do 120 znaków
   EN: Quit Battle
   PL: Zakończ etap
56. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_desc_last_formation] — tekst] 진행 중인 전투를 종료하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_desc_last_formation].content
   limit: do 120 znaków
   EN: Quit the battle in progress?
   PL: Czy zakończyć trwającą walkę?
57. [Tryby lochów i Kolei Refrakcji [boss_raid_ask_give_up_popup_desc_detail_last_formation] — tekst] <size=80%>확인 버튼 선택 시, <color=#f8c200>전투를 종료</color>합니다.\n\n(※ 마지막으로 사용 가능한 편성이므로, <color=#ff0000>패배 상태</color>로 종료됩니다.)</size>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ask_give_up_popup_desc_detail_last_formation].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <size=80%>, <color=#f8c200>, </color>, <color=#ff0000>, </size>, \n
   EN: <size=80%>Selecting "Confirm" below will <color=#f8c200>immediately forfeit the battle.</color>\n\n(※ This is your last available Team. Progress will not be saved, and this attempt will <color=#ff0000>end in defeat.</color>)</size>
   PL: <size=80%>Po potwierdzeniu <color=#f8c200>walka zostanie zakończona</color>.\n\n(※ To ostatni dostępny skład — walka zakończy się <color=#ff0000>porażką</color> bez zapisu postępu.)</size>
58. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_end_title_last_formation] — tekst] 스테이지 종료
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_end_title_last_formation].content
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Tryby lochów i Kolei Refrakcji [boss_raid_battle_pause_ui_end_desc_last_formation] — tekst] 진행 중인 스테이지를 종료합니다.\n(※ 마지막 편성은 진행도가 저장되지 않고 즉시 종료됩니다.)
   źródło: BossRaidUI.json :: dataList[id=boss_raid_battle_pause_ui_end_desc_last_formation].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Quit the battle in progress.\n(※ This is your last available Team. Progress will not be saved, and this attempt will end in defeat.)
   PL: Zakończ trwający etap.\n(※ Dla ostatniego składu postęp nie jest zapisywany, a walka kończy się natychmiast.)
60. [Tryby lochów i Kolei Refrakcji [boss_raid_shop_infinite_item_warning_text] — tekst] ※ 선택한 재화는 다른 재화보다 교환 효율이 낮습니다.\n※ 현재 교환 가능한 다른 재화가 남아 있습니다.\n\n위 사항에도 불구하고 해당 재화로 교환하시겠습니까?
   źródło: BossRaidUI.json :: dataList[id=boss_raid_shop_infinite_item_warning_text].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ The currency has a worse exchange rate than other currencies.\n※ There are other remaining currencies available for exchange.\n\nExchange with this currency anyway?
   PL: ※ Wybrana waluta ma mniej korzystny przelicznik wymiany niż pozostałe.\n※ Dostępne są jeszcze inne nagrody do wymiany.\n\nCzy mimo to chcesz dokonać wymiany?
61. [Tryby lochów i Kolei Refrakcji [boss_raid_limited_coin_converted] — tekst] 이벤트 기간이 종료되어, 사용하지 않은 {0} {1}개가 {2} {3}개로 변환되었습니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_limited_coin_converted].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: With the end of the event period, {1} unused {0} has been converted to {3} {2}.
   PL: Okres wydarzenia dobiegł końca — niewykorzystane {0} ({1} szt.) zamieniono na {2} ({3} szt.).
62. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_max_level_adjusted] — tekst] 초과 레벨이 {0}으로 조정되었습니다.
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_max_level_adjusted].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Excess level has been adjusted to {0}.
   PL: Nadmiarowy poziom został dostosowany do {0}.
63. [Tryby lochów i Kolei Refrakcji [boss_raid_ui_recommend_state_desc_with_max_level_adjust] — tekst] - 인격 : 동기화 <color=#ff0000>{1}단계</color>·레벨 <color=#ff0000>{0}</color>\n(최대 레벨 <color=#ff0000>{2}</color>)\n- E.G.O : 환상 해석 <color=#ff0000>{1}단계</color>
   źródło: BossRaidUI.json :: dataList[id=boss_raid_ui_recommend_state_desc_with_max_level_adjust].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, {1}, {0}, {2}, \n
   EN: - Identities : Uptie <color=#ff0000>Tier {1}</color>, Level <color=#ff0000>{0}</color>\n(Max level <color=#ff0000>{2}</color>)\n- E.G.O : Threadspinning <color=#ff0000>Tier {1}</color>
   PL: - Tożsamości: Synchronizacja <color=#ff0000>poz. {1}</color> · Poziom <color=#ff0000>{0}</color>\n(Maks. poziom <color=#ff0000>{2}</color>)\n- E.G.O: Splot Nici <color=#ff0000>poz. {1}</color>

## Tryby lochów i Kolei Refrakcji: DungeonStartBuffs
- plik gry: `DungeonStartBuffs.json`

64. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR] — opis] 층 이동 시, <color=#5bffde>보유 코스트</color> {0}% 증가 (최대 100)
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: When moving to the next Floor, increase current <color=#5bffde>Cost balance</color> by {0}% (max 100)
   PL: Przy przejściu na kolejne piętro <color=#5bffde>posiadany Koszt</color> wzrasta o {0}% (maks. 100)
65. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE] — opis] <color=#5bffde>기프트 판매 비용</color> {0}% 증가 (상점별 1회)
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Increase <color=#5bffde>E.G.O Gift sale price</color> by {0}% (once per Shop)
   PL: <color=#5bffde>Cena sprzedaży Darów E.G.O</color> +{0}% (1 raz na Sklep)
66. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_SLOT] — opis] <color=#5bffde>테마팩 목록</color> +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_FLOOR_THEME_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Theme Pack Selection</color> +{0}
   PL: <color=#5bffde>Wybór Pakietów Tematycznych</color> +{0}
67. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_REFRESH] — opis] <color=#5bffde>테마팩 새로고침 횟수</color> +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_FLOOR_THEME_REFRESH].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Theme Pack Refresh Chance</color> +{0}
   PL: <color=#5bffde>Odświeżenia Pakietów Tematycznych</color> +{0}
68. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME] — opis] 기록 없는 테마팩 선택 시, 모든 <color=#5bffde>인격 레벨</color> +{0} (최대 9)
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: When choosing a new Theme Pack for the first time, all Identities gain +{0} <color=#5bffde>Level(s)</color> (max 9)
   PL: Przy wyborze nieodkrytego Pakietu Tematycznego <color=#5bffde>poziom wszystkich Tożsamości</color> +{0} (maks. 9)
69. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_EGO_GIFT_SLOT] — opis] <color=#5bffde>상점 기프트 목록</color> +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_SHOP_EGO_GIFT_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Shop E.G.O Gift Selection</color> +{0}
   PL: <color=#5bffde>Oferta Darów E.G.O w Sklepie</color> +{0}
70. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR] — opis] 입장 시, <color=#5bffde>인격 레벨</color> +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entry, all Identities gain {0} <color=#5bffde>Level(s)</color>
   PL: Przy wejściu <color=#5bffde>poziom Tożsamości</color> +{0}
71. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR] — opis] 층 클리어 시, <color=#5bffde>인격 레벨</color> +{0} (최대 5)
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon Floor clear, all Identities gain {0} <color=#5bffde>Level(s)</color> (max 5)
   PL: Po ukończeniu piętra <color=#5bffde>poziom Tożsamości</color> +{0} (maks. 5)
72. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP] — opis] 상점 입장 시, 3등급 이하 무작위 <color=#5bffde>합성·판매용 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering a Shop, gain {0} random Tier 3 or less <color=#5bffde>For Fuse or Sale only E.G.O Gift(s)</color>
   PL: Przy wejściu do Sklepu otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O do Syntezy/Sprzedaży</color> rangi 3 lub niższej
73. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR] — opis] 3층 입장 시, 무작위 <color=#5bffde>3등급 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 3, gain {0} random <color=#5bffde>Tier 3 E.G.O Gift(s)</color>
   PL: Przy wejściu na 3. piętro otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O rangi 3</color>
74. [Tryby lochów i Kolei Refrakcji [ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE] — opis] 합성 시, 합성 결과(3등급 이상)보다 두 단계 낮은 무작위 <color=#5bffde>기프트</color> 획득 (상점별 1회)
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>
   EN: When Fusing, gain a <color=#5bffde>random additional E.G.O Gift</color> 2 Tiers below the Fusion result(must be Tier 3 or higher) (once per Shop)
   PL: Przy Syntezowaniu otrzymujesz losowy <color=#5bffde>Dar E.G.O</color> o 2 rangi niższy od wyniku Syntezy (min. ranga 3; 1 raz na Sklep)
75. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_EGO_GIFT_SELECT] — opis] <color=#5bffde>시작 기프트</color> 수 +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_START_EGO_GIFT_SELECT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Starting E.G.O Gift</color> Choice +{0}
   PL: Liczba <color=#5bffde>początkowych Darów E.G.O</color> +{0}
76. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, 선택한 키워드의 무작위 <color=#5bffde>3등급 기프트 중 {0}개 선택</color>하여 획득
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entry, gain {0} <color=#5bffde>Tier 3 E.G.O Gift(s) of your choice</color> for your selected Keyword category
   PL: Przy wejściu <color=#5bffde>wybierasz {0} spośród losowych Darów E.G.O rangi 3</color> wybranego słowa kluczowego
77. [Tryby lochów i Kolei Refrakcji [REVIVE_ONCE_PER_FLOOR] — opis] 전투 종료 시, 사망한 아군 {0}명 부활 (층별 1회)
   źródło: DungeonStartBuffs.json :: dataList[id=REVIVE_ONCE_PER_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Upon Encounter End: Revive {0} ally(-ies) (once per Floor)
   PL: Na koniec starcia wskrzesza {0} poległych sojuszników (1 raz na piętro)
78. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_REFRESH_EGO_GIFT_ONCE] — opis] 상점 <color=#5bffde>일반 새로고침</color> 1회 무료
   źródło: DungeonStartBuffs.json :: dataList[id=FREE_SHOP_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>
   EN: One Free <color=#5bffde>normal Refresh</color> for Shops
   PL: 1 darmowe <color=#5bffde>zwykłe odświeżenie</color> w Sklepie
79. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_COST] — opis] <color=#5bffde>시작 코스트</color> +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_START_COST].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Starting Cost</color> +{0}
   PL: <color=#5bffde>Początkowy Koszt</color> +{0}
80. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_AFTER_WIN_BATTLE] — opis] <color=#5bffde>전투 보상 코스트</color> +{0}%
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_COST_AFTER_WIN_BATTLE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Encounter Reward Cost</color> +{0}%
   PL: <color=#5bffde>Koszt z nagród za walkę</color> +{0}%
81. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE] — opis] 상점에서 <color=#5bffde>높은 등급 기프트</color> 등장 확률 상승
   źródło: DungeonStartBuffs.json :: dataList[id=ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>
   EN: Greater chance for <color=#5bffde>high Tier E.G.O Gifts</color> to appear in Shops
   PL: Większa szansa na pojawienie się <color=#5bffde>Darów E.G.O wysokiej rangi</color> w Sklepie
82. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE] — opis] 상점 <color=#5bffde>키워드 새로고침</color> 1회 무료
   źródło: DungeonStartBuffs.json :: dataList[id=FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>
   EN: One Free <color=#5bffde>Keyword Refresh</color> for Shops
   PL: 1 darmowe <color=#5bffde>odświeżenie wg słowa kluczowego</color> w Sklepie
83. [Tryby lochów i Kolei Refrakcji [ACQUIRE_2_TIER_RANDOM_EGO_GIFT_ON_ENTER_2ND_FLOOR] — opis] 2층 입장 시, 무작위 <color=#5bffde>2등급 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_2_TIER_RANDOM_EGO_GIFT_ON_ENTER_2ND_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 2, gain {0} random <color=#5bffde>Tier 2 E.G.O Gift(s)</color>
   PL: Przy wejściu na 2. piętro otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O rangi 2</color>
84. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 1층 입장 시, 무작위 <color=#5bffde>1등급 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs.json :: dataList[id=ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 1, gain {0} random <color=#5bffde>Tier 1 E.G.O Gift(s)</color>
   PL: Przy wejściu na 1. piętro otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O rangi 1</color>
85. [Tryby lochów i Kolei Refrakcji [MaxSpeedUpAdder] — opis] <color=#5bffde>속도</color> 최댓값 +{0}
   źródło: DungeonStartBuffs.json :: dataList[id=MaxSpeedUpAdder].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Max Speed</color> +{0}
   PL: Maks. <color=#5bffde>Szybkość</color> +{0}
86. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRoundStart] — opis] <color=#5bffde>{1}</color> {2} 얻음
   źródło: DungeonStartBuffs.json :: dataList[id=GiveBuffOnRoundStart].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {1}, {2}
   EN: Gain {2} <color=#5bffde>{1}</color>
   PL: Zyskujesz {2} <color=#5bffde>{1}</color>
87. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnNewFloorTheme] — opis] 기록되지 않은 테마팩 전투 ({4}층 이하)에서 <color=#5bffde>{1}</color> {2} 얻음
   źródło: DungeonStartBuffs.json :: dataList[id=GiveBuffOnRSOnNewFloorTheme].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {4}, {1}, {2}
   EN: When choosing a new Theme Pack for the first time(in Floor {4} or lower only), gain {2} <color=#5bffde>{1}</color> in its combat Encounters.
   PL: W walkach nieodkrytego Pakietu Tematycznego (piętro {4} lub niższe) zyskujesz {2} <color=#5bffde>{1}</color>
88. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnThemePackUnlockCount] — opis] 테마팩 도감의 테마팩이 {4}개 이상 해금되어 있으면 <color=#5bffde>{1}</color> {2} 얻음
   źródło: DungeonStartBuffs.json :: dataList[id=GiveBuffOnRSOnThemePackUnlockCount].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {4}, {1}, {2}
   EN: If {4}+ Theme Packs are unlocked in the Theme Pack Compendium, gain {2} <color=#5bffde>{1}</color>
   PL: Jeśli w Kompendium odblokowano min. {4} Pakietów Tematycznych, zyskujesz {2} <color=#5bffde>{1}</color>

## Tryby lochów i Kolei Refrakcji: DungeonStartBuffs_MD6
- plik gry: `DungeonStartBuffs_MD6.json`

89. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_COST] — opis] 시작 <color=#5bffde>코스트</color> +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_START_COST].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Starting <color=#5bffde>Cost</color> +{0}
   PL: Początkowy <color=#5bffde>Koszt</color> +{0}
90. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_SLOT] — opis] <color=#5bffde>테마팩</color> 목록 +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_FLOOR_THEME_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Theme Pack</color> Selection +{0}
   PL: Wybór <color=#5bffde>Pakietów Tematycznych</color> +{0}
91. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_EGO_GIFT_SLOT] — opis] <color=#5bffde>상점 기프트</color> 목록 +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_SHOP_EGO_GIFT_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Shop E.G.O Gift</color> Choice +{0}
   PL: Oferta <color=#5bffde>Darów E.G.O w Sklepie</color> +{0}
92. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_REFRESH_EGO_GIFT_ONCE] — opis] <color=#5bffde>상점 일반 새로고침</color> {0}회 무료
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=FREE_SHOP_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: {0} Free <color=#5bffde>normal Refresh(es) for Shops</color>
   PL: {0} darm. <color=#5bffde>zwykłe odświeżenie Sklepu</color>
93. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_COST_TEXT_HIGHLIGHT] — opis] 시작 <color=#5bffde>코스트</color> <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_START_COST_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: Starting <color=#5bffde>Cost</color> <color=#f8c200>+{0}</color>
   PL: Początkowy <color=#5bffde>Koszt</color> <color=#f8c200>+{0}</color>
94. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT] — opis] <color=#5bffde>상점 일반 새로고침</color> <color=#f8c200>{0}회</color> 무료
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=FREE_SHOP_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: <color=#f8c200>{0}</color> Free <color=#5bffde>normal Refresh(es) for Shops</color>
   PL: <color=#f8c200>{0}</color> darm. <color=#5bffde>zwykłe odświeżenie Sklepu</color>
95. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR] — opis] 층 이동 시, 보유 <color=#5bffde>코스트</color> {0}% 증가 (최대 {1})
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}, {1}
   EN: When moving to the next floor, increase current <color=#5bffde>Cost balance</color> by {0}% (max {1})
   PL: Przy przejściu na kolejne piętro posiadany <color=#5bffde>Koszt</color> wzrasta o {0}% (maks. {1})
96. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE] — opis] <color=#5bffde>기프트 판매 비용</color> {0}% 증가 (상점별 1회)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE].description
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT] — opis] 층 이동 시, 보유 <color=#5bffde>코스트</color> <color=#f8c200>{0}%</color> 증가 (최대 <color=#f8c200>{1}</color>)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}, {1}
   EN: When moving to the next floor, increase current <color=#5bffde>Cost balance</color> by <color=#f8c200>{0}%</color> (max <color=#f8c200>{1}</color>)
   PL: Przy przejściu na kolejne piętro posiadany <color=#5bffde>Koszt</color> wzrasta o <color=#f8c200>{0}%</color> (maks. <color=#f8c200>{1}</color>)
98. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE_TEXT_HIGHLIGHT] — opis] <color=#5bffde>기프트 판매 비용</color> <color=#f8c200>{0}%</color> 증가 (상점별 1회)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: Increase <color=#5bffde>E.G.O Gift sale price</color> by <color=#f8c200>{0}%</color> (once per Shop)
   PL: <color=#5bffde>Cena sprzedaży Darów E.G.O</color> +<color=#f8c200>{0}%</color> (1 raz na Sklep)
99. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_REFRESH] — opis] <color=#5bffde>테마팩 새로고침</color> 횟수 +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_FLOOR_THEME_REFRESH].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Theme Pack Refresh </color> Chance +{0}
   PL: Liczba <color=#5bffde>odświeżeń Pakietów Tematycznych</color> +{0}
100. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME] — opis] 기록 없는 테마팩 선택 시, 모든 <color=#5bffde>인격 레벨</color> +{0} (최대 9)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME].description
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_REFRESH_TEXT_HIGHLIGHT] — opis] <color=#5bffde>테마팩 새로고침</color> 횟수 <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_FLOOR_THEME_REFRESH_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: <color=#5bffde>Theme Pack Refresh </color> Chance <color=#f8c200>+{0}</color>
   PL: Liczba <color=#5bffde>odświeżeń Pakietów Tematycznych</color> <color=#f8c200>+{0}</color>
102. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnNewFloorTheme] — opis] <color=#f8c200>기록 없는 테마팩 전투 ({4}층 이하)에서 {1} {2} 얻음</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=GiveBuffOnRSOnNewFloorTheme].description
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {4}, {1}, {2}
   EN: <color=#f8c200>When choosing a new Theme Pack for the first time(in Floor {4} or lower only), gain {2} {1} in its combat Encounters</color>
   PL: <color=#f8c200>W walkach nieodkrytego Pakietu Tematycznego (piętro {4} lub niższe) zyskujesz {2} {1}</color>
103. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnThemePackUnlockCount] — opis] <color=#f8c200>테마팩 도감의 테마팩이 {4}개 이상 해금되어 있으면, {1} {2} 얻음</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=GiveBuffOnRSOnThemePackUnlockCount].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {4}, {1}, {2}
   EN: <color=#f8c200>If {4}+ Theme Packs are unlocked in the Theme Pack Compendium, gain {2} {1}</color>
   PL: <color=#f8c200>Jeśli w Kompendium odblokowano min. {4} Pakietów Tematycznych, zyskujesz {2} {1}</color>
104. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_EGO_GIFT_SELECT] — opis] 시작 <color=#5bffde>기프트</color> 수 +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_START_EGO_GIFT_SELECT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Starting <color=#5bffde>E.G.O Gift</color> Choice +{0}
   PL: Liczba początkowych <color=#5bffde>Darów E.G.O</color> +{0}
105. [Tryby lochów i Kolei Refrakcji [ACQUIRE_COST_AFTER_SELECT_STARLIGHT_BATTLE_REWARD] — opis] <color=#f8c200>전투 보상 카드에서 별빛 선택 시, 코스트 +{0}</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_COST_AFTER_SELECT_STARLIGHT_BATTLE_REWARD].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: <color=#f8c200>When Choosing Starlight from Encounter Reward Cards, Cost +{0}</color>
   PL: <color=#f8c200>Przy wyborze Gwiezdnego Blasku z kart nagród po walce: Koszt +{0}</color>
106. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_AFTER_WIN_BATTLE] — opis] 전투 보상 <color=#5bffde>코스트</color> +{0}%
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_COST_AFTER_WIN_BATTLE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Encounter Reward <color=#5bffde>Cost</color> +{0}%
   PL: <color=#5bffde>Koszt</color> z nagród za walkę +{0}%
107. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE] — opis] 상점에서 <color=#5bffde>높은 등급 기프트 등장 확률 상승</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>
   EN: <color=#5bffde>Greater chance for high Tier E.G.O Gifts</color> to appear in Shops
   PL: <color=#5bffde>Większa szansa na Dary E.G.O wysokiej rangi</color> w Sklepie
108. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_AFTER_WIN_BATTLE_TEXT_HIGHLIGHT] — opis] 전투 보상 <color=#5bffde>코스트</color> <color=#f8c200>+{0}%</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_COST_AFTER_WIN_BATTLE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: Encounter Reward <color=#5bffde>Cost</color> <color=#f8c200>+{0}%</color>
   PL: <color=#5bffde>Koszt</color> z nagród za walkę <color=#f8c200>+{0}%</color>
109. [Tryby lochów i Kolei Refrakcji [ACQUIRE_COST_BY_EGOGIFT_TIER_TOTAL_ON_ENTER_SHOP] — opis] <color=#f8c200>상점 입장 시, 보유한 기프트 등급 합계만큼 코스트 획득 (최대 {1})</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_COST_BY_EGOGIFT_TIER_TOTAL_ON_ENTER_SHOP].description
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {1}
   EN: <color=#f8c200>Upon entering a Shop, add up all the Tier numbers of currently owned E.G.O Gifts and gain it as Cost (max {1})</color>
   PL: <color=#f8c200>Przy wejściu do Sklepu zyskujesz Koszt równy sumie rang posiadanych Darów E.G.O (maks. {1})</color>
110. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE] — opis] <color=#5bffde>상점 키워드 새로고침</color> {0}회 무료
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: {0} Free <color=#5bffde>Keyword Refresh(es) for Shops</color>
   PL: {0} darm. <color=#5bffde>odświeżenie Sklepu wg słowa kluczowego</color>
111. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 1층 입장 시, 무작위 1등급 <color=#5bffde>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 1, gain {0} random Tier 1 <color=#5bffde>E.G.O Gift(s)</color>
   PL: Przy wejściu na 1. piętro otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O</color> rangi 1
112. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT] — opis] <color=#5bffde>상점 키워드 새로고침</color> <color=#f8c200>{0}회</color> 무료
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: <color=#f8c200>{0}</color> Free <color=#5bffde>Keyword Refresh(es) for Shops</color>
   PL: <color=#f8c200>{0}</color> darm. <color=#5bffde>odświeżenie Sklepu wg słowa kluczowego</color>
113. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT] — opis] 1층 입장 시, 무작위 1등급 <color=#5bffde>기프트</color> <color=#f8c200>{0}개</color> 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: Upon entering Floor 1, gain <color=#f8c200>{0}</color> random Tier 1 <color=#5bffde>E.G.O Gift(s)</color>
   PL: Przy wejściu na 1. piętro otrzymujesz <color=#f8c200>{0}</color> los. <color=#5bffde>Dar(y) E.G.O</color> rangi 1
114. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_ENHANCED_SHOP_APPEARANCE_PROB] — opis] <color=#f8c200>강화 상점 등장 확률 +{0}%</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_ENHANCED_SHOP_APPEARANCE_PROB].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: <color=#f8c200>+{0}% chance for Super Shop to appear</color>
   PL: <color=#f8c200>Szansa na pojawienie się Wzmocnionego Sklepu +{0}%</color>
115. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR] — opis] 1층 입장 시, <color=#5bffde>인격 레벨</color> +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 1, all Identities gain {0} <color=#5bffde>Level(s)</color>
   PL: Przy wejściu na 1. piętro <color=#5bffde>poziom Tożsamości</color> +{0}
116. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR] — opis] 층 클리어 시, <color=#5bffde>인격 레벨</color> +{0} (최대 {1})
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}, {1}
   EN: Upon Floor clear, all Identities gain {0} <color=#5bffde>Level(s)</color> (max {1})
   PL: Po ukończeniu piętra <color=#5bffde>poziom Tożsamości</color> +{0} (maks. {1})
117. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT] — opis] 층 클리어 시, <color=#5bffde>인격 레벨</color> +{0} (최대 <color=#f8c200>{1}</color>)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}, {1}
   EN: Upon Floor clear, all Identities gain {0} <color=#5bffde>Level(s)</color> (max <color=#f8c200>{1}</color>)
   PL: Po ukończeniu piętra <color=#5bffde>poziom Tożsamości</color> +{0} (maks. <color=#f8c200>{1}</color>)
118. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_6TH_FLOOR] — opis] <color=#f8c200>6층 입장 시, 인격 레벨 +{0}</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_6TH_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: <color=#f8c200>Upon entering Floor 6, all Identities gain {0} Level(s)</color>
   PL: <color=#f8c200>Przy wejściu na 6. piętro poziom Tożsamości +{0}</color>
119. [Tryby lochów i Kolei Refrakcji [MaxSpeedUpAdder] — opis] <color=#5bffde>속도 최댓값</color> +{0}
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=MaxSpeedUpAdder].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: <color=#5bffde>Max Speed</color> +{0}
   PL: <color=#5bffde>Maks. Szybkość</color> +{0}
120. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRoundStart] — opis] <color=#5bffde>{1}</color> {2} 얻음
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=GiveBuffOnRoundStart].description
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Tryby lochów i Kolei Refrakcji [MaxSpeedUpAdder_TEXT_HIGHLIGHT] — opis] <color=#5bffde>속도 최댓값</color> <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=MaxSpeedUpAdder_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: <color=#5bffde>Max Speed</color> <color=#f8c200>+{0}</color>
   PL: <color=#5bffde>Maks. Szybkość</color> <color=#f8c200>+{0}</color>
122. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRoundStart_TEXT_HIGHLIGHT] — opis] <color=#5bffde>{1}</color> <color=#f8c200>{2}</color> 얻음
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=GiveBuffOnRoundStart_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {1}, {2}
   EN: Gain <color=#f8c200>{2}</color> <color=#5bffde>{1}</color>
   PL: Zyskujesz <color=#f8c200>{2}</color> <color=#5bffde>{1}</color>
123. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP] — opis] 상점 입장 시, 3등급 이하 무작위 <color=#5bffde>합성·판매용 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP].description
   (powtórzenie elementu 72 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR] — opis] 3층 입장 시, 무작위 3등급 <color=#5bffde>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entering Floor 3, gain {0} random Tier 3 <color=#5bffde>E.G.O Gift(s)</color>
   PL: Przy wejściu na 3. piętro otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O</color> rangi 3
125. [Tryby lochów i Kolei Refrakcji [ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE] — opis] 합성 시, 합성 결과(3등급 이상)보다 두 단계 낮은 무작위 <color=#5bffde>기프트</color> 획득 (상점별 1회)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE].description
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_2] — opis] 상점 입장 시, <color=#5bffde>합성 · 판매용 기프트</color> 1개 획득\n<color=#f8c200>· 5층 이하 : 1~3등급\n· 6층 이상 : 2~3등급</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_2].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, \n
   EN: Upon entering a Shop, gain 1 <color=#5bffde>'For Fuse or Sale only E.G.O Gift'</color>\n<color=#f8c200>· Floor 5 or lower : Tier 1~3\n· Floor 6 or higher : Tier 2~3</color>
   PL: Przy wejściu do Sklepu otrzymujesz 1 <color=#5bffde>Dar E.G.O do Syntezy/Sprzedaży</color>\n<color=#f8c200>· Piętro 5 lub niższe: ranga 1~3\n· Piętro 6 lub wyższe: ranga 2~3</color>
127. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_3] — opis] 상점 입장 시, <color=#5bffde>합성 · 판매용 기프트</color> 1개 획득\n<color=#f8c200>· 5층 이하 : 2~3등급\n· 6층 이상 : 3~4등급</color>
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_3].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, \n
   EN: Upon entering a Shop, gain 1 <color=#5bffde>'For Fuse or Sale only E.G.O Gift'</color>\n<color=#f8c200>· Floor 5 or lower : Tier 2~3\n· Floor 6 or higher : Tier 3~4</color>
   PL: Przy wejściu do Sklepu otrzymujesz 1 <color=#5bffde>Dar E.G.O do Syntezy/Sprzedaży</color>\n<color=#f8c200>· Piętro 5 lub niższe: ranga 2~3\n· Piętro 6 lub wyższe: ranga 3~4</color>
128. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F] — opis] 3<color=#f8c200>/5층</color> 입장 시, <color=#f8c200>선택한 키워드</color>의 무작위 3등급 <color=#5bffde>기프트</color> 1개 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#5bffde>
   EN: Upon entering Floor 3<color=#f8c200>/Floor 5</color>, gain 1 Tier 3 <color=#5bffde>E.G.O Gift</color> from the <color=#f8c200>selected Keyword category</color>
   PL: Przy wejściu na 3.<color=#f8c200>/5. piętro</color> otrzymujesz 1 los. <color=#5bffde>Dar E.G.O</color> rangi 3 z <color=#f8c200>wybranego słowa kluczowego</color>
129. [Tryby lochów i Kolei Refrakcji [ACQUIRE_4_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F_7F] — opis] 3<color=#f8c200>/5/7층</color> 입장 시, <color=#f8c200>선택한 키워드</color>의 무작위 <color=#f8c200>4등급</color> <color=#5bffde>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_4_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F_7F].description
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#5bffde>, {0}
   EN: Upon entering Floor 3<color=#f8c200>/Floor 5/Floor 7</color>, gain {0} random <color=#f8c200>Tier 4</color> <color=#5bffde>E.G.O Gift(s)</color> from the <color=#f8c200>selected Keyword category</color>
   PL: Przy wejściu na 3.<color=#f8c200>/5./7. piętro</color> otrzymujesz {0} los. <color=#5bffde>Dar(y) E.G.O</color> <color=#f8c200>rangi 4</color> z <color=#f8c200>wybranego słowa kluczowego</color>
130. [Tryby lochów i Kolei Refrakcji [ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE_1] — opis] 합성 시, 합성 결과(3등급 이상)보다 <color=#f8c200>한 단계</color> 낮은 무작위 <color=#5bffde>기프트</color> 획득 (상점별 1회)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE_1].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#5bffde>
   EN: When Fusing, gain a <color=#5bffde>random additional E.G.O Gift</color> <color=#f8c200>1 Tier</color> below the Fusion result(must be Tier 3 or higher) (once per Shop)
   PL: Przy Syntezowaniu otrzymujesz losowy <color=#5bffde>Dar E.G.O</color> o <color=#f8c200>1 rangę</color> niższy od wyniku Syntezy (min. ranga 3; 1 raz na Sklep)
131. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, 선택한 키워드의 무작위 3등급 <color=#5bffde>기프트</color> 중 {0}개 선택하여 획득 (해당 등급 없을 시, 낮은 등급 출현)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, {0}
   EN: Upon entry, gain {0} Tier 3 <color=#5bffde>E.G.O Gift(s)</color> of your choice for the selected Keyword (if no remaining Gifts meet the conditions, a lower Tier one will appear instead)
   PL: Przy wejściu wybierasz {0} spośród losowych <color=#5bffde>Darów E.G.O</color> rangi 3 wybranego słowa kluczowego (w razie braku — niższej rangi)
132. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT] — opis] 입장 시, 선택한 키워드의 무작위 3등급 <color=#5bffde>기프트</color> 중 <color=#f8c200>{0}개 선택</color>하여 획득 (해당 등급 없을 시, 낮은 등급 출현)
   źródło: DungeonStartBuffs_MD6.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#5bffde>, </color>, <color=#f8c200>, {0}
   EN: Upon entry, gain <color=#f8c200>{0} Tier 3</color> <color=#5bffde>E.G.O Gift(s)</color> <color=#f8c200>of your choice</color> for the selected Keyword (if no remaining Gifts meet the conditions, a lower Tier one will appear instead)
   PL: Przy wejściu <color=#f8c200>wybierasz {0}</color> spośród losowych <color=#5bffde>Darów E.G.O</color> rangi 3 wybranego słowa kluczowego (w razie braku — niższej rangi)

## Tryby lochów i Kolei Refrakcji: DungeonStartBuffs_MD7
- plik gry: `DungeonStartBuffs_MD7.json`

133. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_COST] — opis] 시작 <color=#627eff>코스트</color> +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_START_COST].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Starting <color=#627eff>Cost</color> +{0}
   PL: Początkowy <color=#627eff>Koszt</color> +{0}
134. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_SLOT] — opis] <color=#627eff>테마팩</color> 목록 +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_FLOOR_THEME_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: <color=#627eff>Theme Pack</color> Selection +{0}
   PL: Wybór <color=#627eff>Pakietów Tematycznych</color> +{0}
135. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_EGO_GIFT_SLOT] — opis] <color=#627eff>상점 기프트</color> 목록 +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_SHOP_EGO_GIFT_SLOT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: <color=#627eff>Shop E.G.O Gift</color> Choice +{0}
   PL: Oferta <color=#627eff>Darów E.G.O w Sklepie</color> +{0}
136. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_REFRESH_EGO_GIFT_ONCE] — opis] <color=#627eff>상점 일반 새로고침</color> {0}회 무료
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=FREE_SHOP_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: {0} Free <color=#627eff>normal Refresh(es) for Shops</color>
   PL: {0} darm. <color=#627eff>zwykłe odświeżenie Sklepu</color>
137. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_COST_TEXT_HIGHLIGHT] — opis] 시작 <color=#627eff>코스트</color> <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_START_COST_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: Starting <color=#627eff>Cost</color> <color=#f8c200>+{0}</color>
   PL: Początkowy <color=#627eff>Koszt</color> <color=#f8c200>+{0}</color>
138. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT] — opis] <color=#627eff>상점 일반 새로고침</color> <color=#f8c200>{0}회</color> 무료
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=FREE_SHOP_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: <color=#f8c200>{0}</color> Free <color=#627eff>normal Refresh(es) for Shops</color>
   PL: <color=#f8c200>{0}</color> darm. <color=#627eff>zwykłe odświeżenie Sklepu</color>
139. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR] — opis] 층 이동 시, 보유 <color=#627eff>코스트</color> {0}% 증가 (최대 {1})
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}, {1}
   EN: When moving to the next floor, increase current <color=#627eff>Cost balance</color> by {0}% (max {1})
   PL: Przy przejściu na kolejne piętro posiadany <color=#627eff>Koszt</color> wzrasta o {0}% (maks. {1})
140. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE] — opis] <color=#627eff>기프트 판매 비용</color> {0}% 증가 (상점별 1회)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Increase <color=#627eff>E.G.O Gift sale price</color> by {0}% (once per Shop)
   PL: <color=#627eff>Cena sprzedaży Darów E.G.O</color> +{0}% (1 raz na Sklep)
141. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT] — opis] 층 이동 시, 보유 <color=#627eff>코스트</color> <color=#f8c200>{0}%</color> 증가 (최대 <color=#f8c200>{1}</color>)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_COST_RATE_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}, {1}
   EN: When moving to the next floor, increase current <color=#627eff>Cost balance</color> by <color=#f8c200>{0}%</color> (max <color=#f8c200>{1}</color>)
   PL: Przy przejściu na kolejne piętro posiadany <color=#627eff>Koszt</color> wzrasta o <color=#f8c200>{0}%</color> (maks. <color=#f8c200>{1}</color>)
142. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE_TEXT_HIGHLIGHT] — opis] <color=#627eff>기프트 판매 비용</color> <color=#f8c200>{0}%</color> 증가 (상점별 1회)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_SHOP_SELL_EGO_GIFT_COST_RATE_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: Increase <color=#627eff>E.G.O Gift sale price</color> by <color=#f8c200>{0}%</color> (once per Shop)
   PL: <color=#627eff>Cena sprzedaży Darów E.G.O</color> +<color=#f8c200>{0}%</color> (1 raz na Sklep)
143. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_REFRESH] — opis] <color=#627eff>테마팩 새로고침</color> 횟수 +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_FLOOR_THEME_REFRESH].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: <color=#627eff>Theme Pack Refresh </color> Chance +{0}
   PL: Liczba <color=#627eff>odświeżeń Pakietów Tematycznych</color> +{0}
144. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME] — opis] 기록 없는 테마팩 선택 시, 모든 <color=#627eff>인격 레벨</color> +{0} (최대 9)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_SELECT_NEW_FLOOR_THEME].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: When choosing a new Theme Pack for the first time, all Identities gain +{0} <color=#627eff>Level(s)</color> (max 9)
   PL: Przy wyborze nieodkrytego Pakietu Tematycznego <color=#627eff>poziom wszystkich Tożsamości</color> +{0} (maks. 9)
145. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_FLOOR_THEME_REFRESH_TEXT_HIGHLIGHT] — opis] <color=#627eff>테마팩 새로고침</color> 횟수 <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_FLOOR_THEME_REFRESH_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: <color=#627eff>Theme Pack Refresh </color> Chance <color=#f8c200>+{0}</color>
   PL: Liczba <color=#627eff>odświeżeń Pakietów Tematycznych</color> <color=#f8c200>+{0}</color>
146. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnNewFloorTheme] — opis] <color=#f8c200>기록 없는 테마팩 전투 ({4}층 이하)에서 {1} {2} 얻음</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=GiveBuffOnRSOnNewFloorTheme].description
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRSOnThemePackUnlockCount] — opis] <color=#f8c200>테마팩 도감의 테마팩이 {4}개 이상 해금되어 있으면, {1} {2} 얻음</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=GiveBuffOnRSOnThemePackUnlockCount].description
   (powtórzenie elementu 103 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_START_EGO_GIFT_SELECT] — opis] 시작 <color=#627eff>기프트</color> 수 +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_START_EGO_GIFT_SELECT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Starting <color=#627eff>E.G.O Gift</color> Choice +{0}
   PL: Liczba początkowych <color=#627eff>Darów E.G.O</color> +{0}
149. [Tryby lochów i Kolei Refrakcji [ACQUIRE_COST_AFTER_SELECT_STARLIGHT_BATTLE_REWARD] — opis] <color=#f8c200>전투 보상 카드에서 별빛 선택 시, 코스트 +{0}</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_COST_AFTER_SELECT_STARLIGHT_BATTLE_REWARD].description
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
150. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_AFTER_WIN_BATTLE] — opis] 전투 보상 <color=#627eff>코스트</color> +{0}%
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_COST_AFTER_WIN_BATTLE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Encounter Reward <color=#627eff>Cost</color> +{0}%
   PL: <color=#627eff>Koszt</color> z nagród za walkę +{0}%
151. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE] — opis] 상점에서 <color=#627eff>높은 등급 기프트 등장 확률 상승</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_SHOP_HIGH_TIER_EGO_GIFT_CHANCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>
   EN: <color=#627eff>Greater chance for high Tier E.G.O Gifts</color> to appear in Shops
   PL: <color=#627eff>Większa szansa na Dary E.G.O wysokiej rangi</color> w Sklepie
152. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_COST_AFTER_WIN_BATTLE_TEXT_HIGHLIGHT] — opis] 전투 보상 <color=#627eff>코스트</color> <color=#f8c200>+{0}%</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_COST_AFTER_WIN_BATTLE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: Encounter Reward <color=#627eff>Cost</color> <color=#f8c200>+{0}%</color>
   PL: <color=#627eff>Koszt</color> z nagród za walkę <color=#f8c200>+{0}%</color>
153. [Tryby lochów i Kolei Refrakcji [ACQUIRE_COST_BY_EGOGIFT_TIER_TOTAL_ON_ENTER_SHOP] — opis] <color=#f8c200>상점 입장 시, 보유한 기프트 등급 합계만큼 코스트 획득 (최대 {1})</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_COST_BY_EGOGIFT_TIER_TOTAL_ON_ENTER_SHOP].description
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE] — opis] <color=#627eff>상점 키워드 새로고침</color> {0}회 무료
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: {0} Free <color=#627eff>Keyword Refresh(es) for Shops</color>
   PL: {0} darm. <color=#627eff>odświeżenie Sklepu wg słowa kluczowego</color>
155. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 1층 입장 시, 무작위 1등급 <color=#627eff>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Upon entering Floor 1, gain {0} random Tier 1 <color=#627eff>E.G.O Gift(s)</color>
   PL: Przy wejściu na 1. piętro otrzymujesz {0} los. <color=#627eff>Dar(y) E.G.O</color> rangi 1
156. [Tryby lochów i Kolei Refrakcji [FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT] — opis] <color=#627eff>상점 키워드 새로고침</color> <color=#f8c200>{0}회</color> 무료
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=FREE_SHOP_KEYWORD_REFRESH_EGO_GIFT_ONCE_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: <color=#f8c200>{0}</color> Free <color=#627eff>Keyword Refresh(es) for Shops</color>
   PL: <color=#f8c200>{0}</color> darm. <color=#627eff>odświeżenie Sklepu wg słowa kluczowego</color>
157. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT] — opis] 1층 입장 시, 무작위 1등급 <color=#627eff>기프트</color> <color=#f8c200>{0}개</color> 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_1_TIER_RANDOM_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: Upon entering Floor 1, gain <color=#f8c200>{0}</color> random Tier 1 <color=#627eff>E.G.O Gift(s)</color>
   PL: Przy wejściu na 1. piętro otrzymujesz <color=#f8c200>{0}</color> los. <color=#627eff>Dar(y) E.G.O</color> rangi 1
158. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_ENHANCED_SHOP_APPEARANCE_PROB] — opis] <color=#f8c200>강화 상점 등장 확률 +{0}%</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_ENHANCED_SHOP_APPEARANCE_PROB].description
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR] — opis] 1층 입장 시, <color=#627eff>인격 레벨</color> +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Upon entering Floor 1, all Identities gain {0} <color=#627eff>Level(s)</color>
   PL: Przy wejściu na 1. piętro <color=#627eff>poziom Tożsamości</color> +{0}
160. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR] — opis] 층 클리어 시, <color=#627eff>인격 레벨</color> +{0} (최대 {1})
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}, {1}
   EN: Upon Floor clear, all Identities gain {0} <color=#627eff>Level(s)</color> (max {1})
   PL: Po ukończeniu piętra <color=#627eff>poziom Tożsamości</color> +{0} (maks. {1})
161. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT] — opis] 층 클리어 시, <color=#627eff>인격 레벨</color> +{0} (최대 <color=#f8c200>{1}</color>)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_CLEAR_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}, {1}
   EN: Upon Floor clear, all Identities gain {0} <color=#627eff>Level(s)</color> (max <color=#f8c200>{1}</color>)
   PL: Po ukończeniu piętra <color=#627eff>poziom Tożsamości</color> +{0} (maks. <color=#f8c200>{1}</color>)
162. [Tryby lochów i Kolei Refrakcji [ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_6TH_FLOOR] — opis] <color=#f8c200>6층 입장 시, 인격 레벨 +{0}</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ADDITIONAL_PERSONALITY_LEVEL_ON_ENTER_6TH_FLOOR].description
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [Tryby lochów i Kolei Refrakcji [MaxSpeedUpAdder] — opis] <color=#627eff>속도 최댓값</color> +{0}
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=MaxSpeedUpAdder].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: <color=#627eff>Max Speed</color> +{0}
   PL: <color=#627eff>Maks. Szybkość</color> +{0}
164. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRoundStart] — opis] <color=#627eff>{1}</color> {2} 얻음
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=GiveBuffOnRoundStart].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {1}, {2}
   EN: Gain {2} <color=#627eff>{1}</color>
   PL: Zyskujesz {2} <color=#627eff>{1}</color>
165. [Tryby lochów i Kolei Refrakcji [MaxSpeedUpAdder_TEXT_HIGHLIGHT] — opis] <color=#627eff>속도 최댓값</color> <color=#f8c200>+{0}</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=MaxSpeedUpAdder_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: <color=#627eff>Max Speed</color> <color=#f8c200>+{0}</color>
   PL: <color=#627eff>Maks. Szybkość</color> <color=#f8c200>+{0}</color>
166. [Tryby lochów i Kolei Refrakcji [GiveBuffOnRoundStart_TEXT_HIGHLIGHT] — opis] <color=#627eff>{1}</color> <color=#f8c200>{2}</color> 얻음
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=GiveBuffOnRoundStart_TEXT_HIGHLIGHT].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {1}, {2}
   EN: Gain <color=#f8c200>{2}</color> <color=#627eff>{1}</color>
   PL: Zyskujesz <color=#f8c200>{2}</color> <color=#627eff>{1}</color>
167. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP] — opis] 상점 입장 시, 3등급 이하 무작위 <color=#627eff>합성·판매용 기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Upon entering a Shop, gain {0} random Tier 3 or less <color=#627eff>For Fuse or Sale only E.G.O Gift(s)</color>
   PL: Przy wejściu do Sklepu otrzymujesz {0} los. <color=#627eff>Dar(y) E.G.O do Syntezy/Sprzedaży</color> rangi 3 lub niższej
168. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR] — opis] 3층 입장 시, 무작위 3등급 <color=#627eff>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3RD_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Upon entering Floor 3, gain {0} random Tier 3 <color=#627eff>E.G.O Gift(s)</color>
   PL: Przy wejściu na 3. piętro otrzymujesz {0} los. <color=#627eff>Dar(y) E.G.O</color> rangi 3
169. [Tryby lochów i Kolei Refrakcji [ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE] — opis] 합성 시, 합성 결과(3등급 이상)보다 두 단계 낮은 무작위 <color=#627eff>기프트</color> 획득 (상점별 1회)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>
   EN: When Fusing, gain a <color=#627eff>random additional E.G.O Gift</color> 2 Tiers below the Fusion result(must be Tier 3 or higher) (once per Shop)
   PL: Przy Syntezowaniu otrzymujesz losowy <color=#627eff>Dar E.G.O</color> o 2 rangi niższy od wyniku Syntezy (min. ranga 3; 1 raz na Sklep)
170. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_2] — opis] 상점 입장 시, <color=#627eff>합성 · 판매용 기프트</color> 1개 획득\n<color=#f8c200>· 5층 이하 : 1~3등급\n· 6층 이상 : 2~3등급</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_2].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, \n
   EN: Upon entering a Shop, gain 1 <color=#627eff>'For Fuse or Sale only E.G.O Gift'</color>\n<color=#f8c200>· Floor 5 or lower : Tier 1~3\n· Floor 6 or higher : Tier 2~3</color>
   PL: Przy wejściu do Sklepu otrzymujesz 1 <color=#627eff>Dar E.G.O do Syntezy/Sprzedaży</color>\n<color=#f8c200>· Piętro 5 lub niższe: ranga 1~3\n· Piętro 6 lub wyższe: ranga 2~3</color>
171. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_3] — opis] 상점 입장 시, <color=#627eff>합성 · 판매용 기프트</color> 1개 획득\n<color=#f8c200>· 5층 이하 : 2~3등급\n· 6층 이상 : 3~4등급</color>
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_MATERIAL_EGO_GIFT_ON_ENTER_SHOP_3].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, \n
   EN: Upon entering a Shop, gain 1 <color=#627eff>'For Fuse or Sale only E.G.O Gift'</color>\n<color=#f8c200>· Floor 5 or lower : Tier 2~3\n· Floor 6 or higher : Tier 3~4</color>
   PL: Przy wejściu do Sklepu otrzymujesz 1 <color=#627eff>Dar E.G.O do Syntezy/Sprzedaży</color>\n<color=#f8c200>· Piętro 5 lub niższe: ranga 2~3\n· Piętro 6 lub wyższe: ranga 3~4</color>
172. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F] — opis] 3<color=#f8c200>/5층</color> 입장 시, <color=#f8c200>선택한 키워드</color>의 무작위 3등급 <color=#627eff>기프트</color> 1개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#627eff>
   EN: Upon entering Floor 3<color=#f8c200>/Floor 5</color>, gain 1 Tier 3 <color=#627eff>E.G.O Gift</color> from the <color=#f8c200>selected Keyword category</color>
   PL: Przy wejściu na 3.<color=#f8c200>/5. piętro</color> otrzymujesz 1 los. <color=#627eff>Dar E.G.O</color> rangi 3 z <color=#f8c200>wybranego słowa kluczowego</color>
173. [Tryby lochów i Kolei Refrakcji [ACQUIRE_4_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F_7F] — opis] 3<color=#f8c200>/5/7층</color> 입장 시, <color=#f8c200>선택한 키워드</color>의 무작위 <color=#f8c200>4등급</color> <color=#627eff>기프트</color> {0}개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_4_TIER_RANDOM_EGO_GIFT_ON_ENTER_3F_5F_7F].description
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#627eff>, {0}
   EN: Upon entering Floor 3<color=#f8c200>/Floor 5/Floor 7</color>, gain {0} random <color=#f8c200>Tier 4</color> <color=#627eff>E.G.O Gift(s)</color> from the <color=#f8c200>selected Keyword category</color>
   PL: Przy wejściu na 3.<color=#f8c200>/5./7. piętro</color> otrzymujesz {0} los. <color=#627eff>Dar(y) E.G.O</color> <color=#f8c200>rangi 4</color> z <color=#f8c200>wybranego słowa kluczowego</color>
174. [Tryby lochów i Kolei Refrakcji [ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE_1] — opis] 합성 시, 합성 결과(3등급 이상)보다 <color=#f8c200>한 단계</color> 낮은 무작위 <color=#627eff>기프트</color> 획득 (상점별 1회)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_LOWER_TIER_RANDOM_EGO_GIFT_ON_COMBINE_1].description
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, <color=#627eff>
   EN: When Fusing, gain a <color=#627eff>random additional E.G.O Gift</color> <color=#f8c200>1 Tier</color> below the Fusion result(must be Tier 3 or higher) (once per Shop)
   PL: Przy Syntezowaniu otrzymujesz losowy <color=#627eff>Dar E.G.O</color> o <color=#f8c200>1 rangę</color> niższy od wyniku Syntezy (min. ranga 3; 1 raz na Sklep)
175. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, 선택한 키워드의 무작위 3등급 <color=#627eff>기프트</color> 중 {0}개 선택하여 획득 (해당 등급 없을 시, 낮은 등급 출현)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, {0}
   EN: Upon entry, gain {0} Tier 3 <color=#627eff>E.G.O Gift(s)</color> of your choice for the selected Keyword (if no remaining Gifts meet the conditions, a lower Tier one will appear instead)
   PL: Przy wejściu wybierasz {0} spośród losowych <color=#627eff>Darów E.G.O</color> rangi 3 wybranego słowa kluczowego (w razie braku — niższej rangi)
176. [Tryby lochów i Kolei Refrakcji [ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT] — opis] 입장 시, 선택한 키워드의 무작위 3등급 <color=#627eff>기프트</color> 중 <color=#f8c200>{0}개 선택</color>하여 획득 (해당 등급 없을 시, 낮은 등급 출현)
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_3_TIER_RANDOM_KEYWORD_EGO_GIFT_ON_ENTER_1ST_FLOOR_TEXT_HIGHLIGHT].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>, <color=#f8c200>, {0}
   EN: Upon entry, gain <color=#f8c200>{0} Tier 3</color> <color=#627eff>E.G.O Gift(s)</color> <color=#f8c200>of your choice</color> for the selected Keyword (if no remaining Gifts meet the conditions, a lower Tier one will appear instead)
   PL: Przy wejściu <color=#f8c200>wybierasz {0}</color> spośród losowych <color=#627eff>Darów E.G.O</color> rangi 3 wybranego słowa kluczowego (w razie braku — niższej rangi)
177. [Tryby lochów i Kolei Refrakcji [ACQUIRE_1_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, <color=#627eff>어두운 잔영</color> 1개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_1_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, </color>
   EN: Upon entry, gain 1 <color=#627eff>Dark Vestige</color>
   PL: Przy wejściu otrzymujesz 1 <color=#627eff>Mroczny Powidok</color>
178. [Tryby lochów i Kolei Refrakcji [ACQUIRE_12_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, <color=#627eff>어두운 잔영, <color=#f8c200>아스라한 잔영</color></color> 각각 1개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_12_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, <color=#f8c200>, </color>
   EN: Upon entry, gain 1 <color=#627eff>Dark Vestige</color> and 1 <color=#f8c200>Faint Vestige</color> each
   PL: Przy wejściu otrzymujesz po 1 szt.: <color=#627eff>Mroczny Powidok, <color=#f8c200>Nikły Powidok</color></color>
179. [Tryby lochów i Kolei Refrakcji [ACQUIRE_123_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR] — opis] 입장 시, <color=#627eff>어두운 잔영, <color=#f8c200>아스라한 잔영, 빛나는 잔영</color></color> 각각 1개 획득
   źródło: DungeonStartBuffs_MD7.json :: dataList[id=ACQUIRE_123_TIER_MATERIAL_EGO_GIFT_ON_ENTER_1ST_FLOOR].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#627eff>, <color=#f8c200>, </color>
   EN: Upon entry, gain 1 <color=#627eff>Dark Vestige</color>,1 <color=#f8c200>Faint Vestige, and 1 Twinkling Vestige</color> each
   PL: Przy wejściu otrzymujesz po 1 szt.: <color=#627eff>Mroczny Powidok, <color=#f8c200>Nikły Powidok, Lśniący Powidok</color></color>

## Tryby lochów i Kolei Refrakcji: HellsChickenDungeonNode
- plik gry: `HellsChickenDungeonNode.json`

180. [Tryby lochów i Kolei Refrakcji [910301] — tytuł] 고소한 향을 따라서
   źródło: HellsChickenDungeonNode.json :: dataList[id=910301].title
   limit: do 40 znaków
   EN: Following a Crispy Scent
   PL: Śladem Chrupiącego Aromatu
181. [Tryby lochów i Kolei Refrakcji [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: HellsChickenDungeonNode.json :: dataList[id=910301].desc
   limit: do 120 znaków
   EN: A waft of something crisp and well-roasted tickles the nose.
   PL: Skądś unosi się smakowity zapach chrupiącej pieczeni.
182. [Tryby lochów i Kolei Refrakcji [910701] — tytuł] 김삿갓의 심상
   źródło: HellsChickenDungeonNode.json :: dataList[id=910701].title
   limit: do 40 znaków
   EN: Bamboo-hatted Kim's Fathoms
   PL: Głębia Kima w Słomkowym Kapeluszu
183. [Tryby lochów i Kolei Refrakcji [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: HellsChickenDungeonNode.json :: dataList[id=910701].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In the shimmering fathoms of ego,\nA painfully pale nightly trail unfolds before us.
   PL: W falującej głębi ego\nrozpościera się przed nami przejmująco błękitny nocny trakt.
184. [Tryby lochów i Kolei Refrakcji [910901] — tytuł] 시간살인마의 심상
   źródło: HellsChickenDungeonNode.json :: dataList[id=910901].title
   limit: do 40 znaków
   EN: Time Ripper's Fathoms
   PL: Głębia Rozpruwacza Czasu
185. [Tryby lochów i Kolei Refrakcji [911401] — tytuł] 호엔하임의 심상
   źródło: HellsChickenDungeonNode.json :: dataList[id=911401].title
   limit: do 40 znaków
   EN: Hohenheim's Fathoms
   PL: Głębia Hohenheima
186. [Tryby lochów i Kolei Refrakcji [912401] — tytuł] 호엔하임의 심상
   źródło: HellsChickenDungeonNode.json :: dataList[id=912401].title
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
187. [Tryby lochów i Kolei Refrakcji [912711] — tytuł] ???의 심상
   źródło: HellsChickenDungeonNode.json :: dataList[id=912711].title
   limit: do 40 znaków
   EN: ???'s Fathoms
   PL: Głębia ???

## Tryby lochów i Kolei Refrakcji: MirrorDungeonAbName
- plik gry: `MirrorDungeonAbName.json`

188. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9001] — tekst] 지옥나비의 꿈
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9001].content
   limit: do 120 znaków
   EN: Hellterfly’s Dream
   PL: Sen Piekielnego Motyla
189. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9002] — tekst] 도착증
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9002].content
   limit: do 120 znaków
   EN: Perversion
   PL: Perwersja
190. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9003] — tekst] 재에서 재로
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9003].content
   limit: do 120 znaków
   EN: Ashes to Ashes
   PL: Z Prochu w Proch
191. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9004] — tekst] 혈액 포집팩
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9004].content
   limit: do 120 znaków
   EN: Phlebotomy Pack
   PL: Pakiet Krwiodawczy
192. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9005] — tekst] 상처붙이
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9005].content
   limit: do 120 znaków
   EN: Wound Clerid
   PL: Chrząszcz Rany
193. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9006] — tekst] 커피와 종이학
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9006].content
   limit: do 120 znaków
   EN: Coffee and Cranes
   PL: Kawa i Papierowe Żurawie
194. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9007] — tekst] 주홍 나방떼
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9007].content
   limit: do 120 znaków
   EN: Eclipse of Scarlet Moths
   PL: Rój Szkarłatnych Ćm
195. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9008] — tekst] 늘어붙은 쇠말뚝
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9008].content
   limit: do 120 znaków
   EN: Grimy Iron Stake
   PL: Oblepiony Żelazny Pal
196. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9009] — tekst] 작열우모
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9009].content
   limit: do 120 znaków
   EN: Fiery Down
   PL: Żarzące Pióro
197. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9010] — tekst] 블러디가젯
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9010].content
   limit: do 120 znaków
   EN: Bloody Gadget
   PL: Krwawy Gadżet
198. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9011] — tekst] 여우비
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9011].content
   limit: do 120 znaków
   EN: Sunshower
   PL: Lisi Deszcz
199. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9012] — tekst] 오늘의 표정
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9012].content
   limit: do 120 znaków
   EN: Today’s Expression
   PL: Dzisiejszy Wyraz Twarzy
200. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9013] — tekst] 부적 묶음
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9013].content
   limit: do 120 znaków
   EN: Talisman Bundle
   PL: Plik Talizmanów
201. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9014] — tekst] 녹슨 기념 주화
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9014].content
   limit: do 120 znaków
   EN: Rusty Commemorative Coin
   PL: Zardzewiała Moneta Pamiątkowa
202. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9015] — tekst] 고혈
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9015].content
   limit: do 120 znaków
   EN: Blood, Sweat, and Tears
   PL: Krew, Pot i Łzy
203. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9016] — tekst] 초록빛 결실
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9016].content
   limit: do 120 znaków
   EN: Green Spirit
   PL: Zielony Owoc
204. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9017] — tekst] 문자 석판
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9017].content
   limit: do 120 znaków
   EN: Lithograph
   PL: Kamienna Tablica
205. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9018] — tekst] 장미 면류관
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9018].content
   limit: do 120 znaków
   EN: Crown of Roses
   PL: Korona z Róż
206. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9019] — tekst] 끈적거리는 진액
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9019].content
   limit: do 120 znaków
   EN: Sticky Muck
   PL: Lepka Wydzielina
207. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9020] — tekst] 흰 국화
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9020].content
   limit: do 120 znaków
   EN: White Chrysanthemum
   PL: Biała Chryzantema
208. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9021] — tekst] 쪽빛 지포라이터
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9021].content
   limit: do 120 znaków
   EN: Blue Zippo Lighter
   PL: Zapalniczka Indygo
209. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9022] — tekst] 환상통
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9022].content
   limit: do 120 znaków
   EN: Phantom Pain
   PL: Ból Fantomowy
210. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9023] — tekst] 벼락 가지
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9023].content
   limit: do 120 znaków
   EN: Thunderbranch
   PL: Gałąź Pioruna
211. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9024] — tekst] 녹아내린 눈알
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9024].content
   limit: do 120 znaków
   EN: Melty Eyeball
   PL: Stopiona Gałka Oczna
212. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9025] — tekst] 잿빛 코트
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9025].content
   limit: do 120 znaków
   EN: Grey Coat
   PL: Popielaty Płaszcz
213. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9026] — tekst] 대기만성형 타투
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9026].content
   limit: do 120 znaków
   EN: Late-bloomer’s Tattoo
   PL: Tatuaż Późnego Rozkwitu
214. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9027] — tekst] 가장 낮은 별
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9027].content
   limit: do 120 znaków
   EN: Lowest Star
   PL: Najniższa Gwiazda
215. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9028] — tekst] 편견
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9028].content
   limit: do 120 znaków
   EN: Prejudice
   PL: Uprzedzenie
216. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9029] — tekst] 작고 나쁠 인형
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9029].content
   limit: do 120 znaków
   EN: Little and To-be-Naughty Plushie
   PL: Mała i Wkrótce Zła Laleczka
217. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9030] — tekst] 수집하는 해골
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9030].content
   limit: do 120 znaków
   EN: Gathering Skulls
   PL: Zbierająca Czaszka
218. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9031] — tekst] 닉시 다이버전스
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9031].content
   limit: do 120 znaków
   EN: Nixie Divergence
   PL: Dywergencja Nixie
219. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9032] — tekst] 꿈을 꾸는 전기양
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9032].content
   limit: do 120 znaków
   EN: Dreaming Electric Sheep
   PL: Śniąca Elektryczna Owca
220. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9033] — tekst] 근무용 통상 배터리
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9033].content
   limit: do 120 znaków
   EN: Standard-duty Battery
   PL: Standardowa Bateria Służbowa
221. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9034] — tekst] 일점타격논리회로
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9034].content
   limit: do 120 znaków
   EN: Pinpoint Logic Circuit
   PL: Obwód Logiczny Punktowego Uderzenia
222. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9035] — tekst] 저주 인형
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9035].content
   limit: do 120 znaków
   EN: Voodoo Doll
   PL: Laleczka Voodoo
223. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9036] — tekst] 카르밀라
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9036].content
   limit: do 120 znaków
   EN: Carmilla
   PL: Carmilla
224. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9037] — tekst] 플라스크 속의 아이
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9037].content
   limit: do 120 znaków
   EN: Child within a Flask
   PL: Dziecko w Kolbie
225. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9038] — tekst] 환상 사냥
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9038].content
   limit: do 120 znaków
   EN: Illusory Hunt
   PL: Polowanie na Złudzenia
226. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9039] — tekst] 귀로
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9039].content
   limit: do 120 znaków
   EN: Homeward
   PL: Powrót do Domu
227. [Tryby lochów i Kolei Refrakcji [mirrordungeon_egogift_temp_ab_name_9040] — tekst] 내일의 운세
   źródło: MirrorDungeonAbName.json :: dataList[id=mirrordungeon_egogift_temp_ab_name_9040].content
   limit: do 120 znaków
   EN: Tomorrow’s Fortune
   PL: Jutrzejsza Wróżba

## Tryby lochów i Kolei Refrakcji: MirrorDungeonBattleRewardCase
- plik gry: `MirrorDungeonBattleRewardCase.json`

228. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_cost_acquisition] — tekst] 코스트 {0} 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_cost_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain {0} Cost
   PL: Zyskaj {0} Kosztu
229. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_cost_and_gift_acquisition] — tekst] 코스트 {0} 획득\n{1}% 확률로 {2}등급 이하의 무작위 (입장 시 선택한 키워드) E.G.O 기프트 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_cost_and_gift_acquisition].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: Gain {0} Cost\n{1}% chance to gain a random Tier {2} or lower E.G.O Gift of the Keyword Category selected at the start of the Mirror Dungeon
   PL: Zyskaj {0} Kosztu\n{1}% szansy na losowy Dar E.G.O rangi {2} lub niższej (z kategorii słowa kluczowego wybranego na starcie)
230. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_cost_and_all_tier_gift_acquisition] — tekst] 코스트 {0} 획득\n{1}% 확률로 무작위 E.G.O 기프트 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_cost_and_all_tier_gift_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: Gain {0} Cost\n{1}% chance to gain a random E.G.O Gift
   PL: Zyskaj {0} Kosztu\n{1}% szansy na losowy Dar E.G.O
231. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_random_gift_acquisition] — tekst] {0}등급 무작위 E.G.O 기프트 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_random_gift_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain a random Tier {0} E.G.O Gift
   PL: Zyskaj losowy Dar E.G.O rangi {0}
232. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_chip_acquisition] — tekst] 최종 클리어 시, 별빛 {0} 추가 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_chip_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Gain additional {0} Starlight upon clearing the Mirror Dungeon
   PL: Po końcowym ukończeniu zyskaj dodatkowo {0} Gwiezdnego Blasku
233. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_random_ego_resource_acquisition] — tekst] 무작위 E.G.O 자원 {0}종 +{1}
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_random_ego_resource_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: E.G.O Resource +{1} for {0} different Affinities
   PL: {0} los. rodz. zasobów E.G.O +{1}
234. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_least_ego_resource_acquisition] — tekst] 제일 적은 E.G.O 자원 {0}종 +{1}
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_least_ego_resource_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: E.G.O Resource +{1} for {0} of the least-owned Affinities
   PL: {0} najrzadsze rodz. zasobów E.G.O +{1}
235. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_cost_and_gift_acquisition_from_start_keyword] — tekst] 코스트 {0} 획득\n{1}% 확률로 {2}등급 무작위 {3} E.G.O 기프트 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_cost_and_gift_acquisition_from_start_keyword].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, \n
   EN: Gain {0} Cost\n{1}% chance to gain a random Tier {2} {3} E.G.O Gift
   PL: Zyskaj {0} Kosztu\n{1}% szansy na losowy Dar E.G.O ({3}) rangi {2}
236. [Tryby lochów i Kolei Refrakcji [dungeon_battle_reward_case_format_cost_and_gift_acquisition_from_start_keyword_none_or_random] — tekst] 코스트 {0} 획득\n{1}% 확률로 {2}등급 무작위 E.G.O 기프트 획득
   źródło: MirrorDungeonBattleRewardCase.json :: dataList[id=dungeon_battle_reward_case_format_cost_and_gift_acquisition_from_start_keyword_none_or_random].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: Gain {0} Cost\n{1}% chance to gain a random Tier {2} E.G.O Gift
   PL: Zyskaj {0} Kosztu\n{1}% szansy na losowy Dar E.G.O rangi {2}

## Tryby lochów i Kolei Refrakcji: MirrorDungeonName
- plik gry: `MirrorDungeonName.json`

237. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_1] — tekst] 시작의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_1].content
   limit: do 120 znaków
   EN: Mirror of the Beginning
   PL: Lustro Początku
238. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_2] — tekst] 거울의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_2].content
   limit: do 120 znaków
   EN: Mirror of Mirrors
   PL: Lustro Luster
239. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_1_0] — tekst] 시작의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_1_0].content
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_2_0] — tekst] 거울의 거울 - 보통 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_2_0].content
   limit: do 120 znaków
   EN: Mirror of Mirrors - Normal
   PL: Lustro Luster — Normalny
241. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_2_1] — tekst] 거울의 거울 - 어려움 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_2_1].content
   limit: do 120 znaków
   EN: Mirror of Mirrors - Hard
   PL: Lustro Luster — Trudny
242. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_3] — tekst] 호수의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_3].content
   limit: do 120 znaków
   EN: Mirror of the Lake
   PL: Lustro Jeziora
243. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_3_0] — tekst] 호수의 거울 - 일반 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_3_0].content
   limit: do 120 znaków
   EN: Mirror of the Lake - Normal
   PL: Lustro Jeziora — Normalny
244. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_3_1] — tekst] 호수의 거울 - 어려움 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_3_1].content
   limit: do 120 znaków
   EN: Mirror of the Lake - Hard
   PL: Lustro Jeziora — Trudny
245. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_4] — tekst] 폭풍의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_4].content
   limit: do 120 znaków
   EN: Mirror of the Wuthering
   PL: Lustro Wichury
246. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_4_0] — tekst] 폭풍의 거울 - 시뮬레이션 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_4_0].content
   limit: do 120 znaków
   EN: Mirror of the Wuthering - Simulation
   PL: Lustro Wichury — Symulacja
247. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_4_1] — tekst] 폭풍의 거울 - 리토르넬로 난이도
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_4_1].content
   limit: do 120 znaków
   EN: Mirror of the Wuthering - Ritornello
   PL: Lustro Wichury — Ritornello
248. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_5] — tekst] 꿈결의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_5].content
   limit: do 120 znaków
   EN: Mirror of the Dreaming
   PL: Lustro Snu
249. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_5_0] — tekst] 꿈결의 거울 [NORMAL]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_5_0].content
   limit: do 120 znaków
   EN: Mirror of the Dreaming [NORMAL]
   PL: Lustro Snu [NORMAL]
250. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_5_1] — tekst] 꿈결의 거울 [HARD]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_5_1].content
   limit: do 120 znaków
   EN: Mirror of the Dreaming [HARD]
   PL: Lustro Snu [HARD]
251. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_6] — tekst] 영생의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_6].content
   limit: do 120 znaków
   EN: Mirror of Immortality
   PL: Lustro Nieśmiertelności
252. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_6_0] — tekst] 영생의 거울 [NORMAL]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_6_0].content
   limit: do 120 znaków
   EN: Mirror of Immortality [NORMAL]
   PL: Lustro Nieśmiertelności [NORMAL]
253. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_6_1] — tekst] 영생의 거울 [HARD]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_6_1].content
   limit: do 120 znaków
   EN: Mirror of Immortality [HARD]
   PL: Lustro Nieśmiertelności [HARD]
254. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_7] — tekst] 이름과 거미의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_7].content
   limit: do 120 znaków
   EN: Mirror of Names and Spiders
   PL: Lustro Imion i Pająków
255. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_7_0] — tekst] 이름과 거미의 거울 [NORMAL]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_7_0].content
   limit: do 120 znaków
   EN: Mirror of Names and Spiders [NORMAL]
   PL: Lustro Imion i Pająków [NORMAL]
256. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_7_1] — tekst] 이름과 거미의 거울 [HARD]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_7_1].content
   limit: do 120 znaków
   EN: Mirror of Names and Spiders [HARD]
   PL: Lustro Imion i Pająków [HARD]
257. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_8] — tekst] 시지프의 거울
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_8].content
   limit: do 120 znaków
   EN: Mirror of Sisyphe
   PL: Lustro Sisyphe
258. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_8_0] — tekst] 시지프의 거울 [NORMAL]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_8_0].content
   limit: do 120 znaków
   EN: Mirror of Sisyphe [NORMAL]
   PL: Lustro Sisyphe [NORMAL]
259. [Tryby lochów i Kolei Refrakcji [mirrordungeon_name_8_1] — tekst] 시지프의 거울 [HARD]
   źródło: MirrorDungeonName.json :: dataList[id=mirrordungeon_name_8_1].content
   limit: do 120 znaków
   EN: Mirror of Sisyphe [HARD]
   PL: Lustro Sisyphe [HARD]

## Tryby lochów i Kolei Refrakcji: MirrorDungeonNode1-1
- plik gry: `MirrorDungeonNode1-1.json`

260. [Tryby lochów i Kolei Refrakcji [2010000] — tytuł] 특정하기 어려운 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2010000].title
   limit: do 40 znaków
   EN: Indistinguishable Space
   PL: Nieokreślona Przestrzeń
261. [Tryby lochów i Kolei Refrakcji [2010000] — opis] 고요한 소음이 이곳에는 있다. 이 공간 안으로 걸음 하면 어디로 이어지게 될지 도무지 감이 잡히지 않는다.\n그 공간 안에서는 냄새도 난다. 달콤하다가도, 금방\n시어지고, 쿱쿱하다가, 상쾌하고 청량하기도 하다.\n\n그 체험이 문 밖에서도, 공간을 걸음 하면서도\n자꾸만 바뀌어 간다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2010000].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A quiet noise is in the air. You cannot begin to imagine what might await here once you enter.\nIt exudes a smell.\nAt one moment, it’s sweet.\nYet it soon turns sour, musky, then refreshing, clear.\n\nThe experience shifts repeatedly even as you approach the door from outside.
   PL: W powietrzu unosi się cichy szum. Nie sposób odgadnąć, dokąd zaprowadzi postawienie kroku za próg.\nWnętrze przesyca też woń — w jednej chwili słodka, zaraz potem kwaśna i zatęchła, by po chwili stać się rześka i czysta.\n\nWrażenia zmieniają się raz po raz już przed samymi drzwiami.
262. [Tryby lochów i Kolei Refrakcji [2011000] — tytuł] 적의가 느껴지는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011000].title
   limit: do 40 znaków
   EN: Radiating Malice
   PL: Przestrzeń Ziejąca Wrogością
263. [Tryby lochów i Kolei Refrakcji [2011000] — opis] 이 기이한 공간들 안에서 그나마 마음이 놓이는 것 같다.\n분명한 적의가 저 너머에서 느껴지고 있지만, 이보다 두렵고 소름돋는 공간이 존재함을 알기 때문이다.\n\n물론, 긴장을 놓아서는 안된다. 공간에서 마주하는 적들은 언제든지 수감자들을 부숴버릴 수 있을 테니까.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011000].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Seeing this gives you an odd sense of relief.\nEven though you can feel a clear hostility coming from the area, you know well that there are far more terrifying encounters in this spiral of uncanny spaces.\n\nOf course, this does not mean that you can relax.\nThe enemies you face here might crush your Sinners at any moment.
   PL: Pośród tych osobliwych przestrzeni widok ten przynosi dziwną ulgę.\nZ głębi bije wprawdzie wyraźna wrogość, lecz dobrze wiesz, że w tej spirali czają się miejsca o wiele bardziej przerażające.\n\nNie wolno jednak tracić czujności — tutejsi wrogowie w każdej chwili mogą zmiażdżyć Grzeszników.
264. [Tryby lochów i Kolei Refrakcji [2011001] — tytuł] 적의가 느껴지는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011001].title
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Tryby lochów i Kolei Refrakcji [2011001] — opis] 이 공간은 이전보다도 더 짙은 적의를 내뿜고 있다.\n수감자들은 처음과 같은 상태가 아니다.\n아래로 내려오면서, 그들은 피로한 몸을 이끌고 있다.\n긴장하지 않으면, 가장 보통의 공간에서 수감자들을 잃을 수도 있을 것이다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011001].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This zone is radiating an even deeper malice.\nThe Sinners are no longer in their top shapes.\nThey are all exhausted, barely dragging their feet onward after this long journey.\nWe shouldn't let our guards down... lest we lose the Sinners here.
   PL: Przestrzeń ta zieje jeszcze gęstszą wrogością niż poprzednie.\nGrzesznicy nie są już w pełni sił — schodząc coraz niżej, powłóczą zmęczonymi nogami.\nChwila nieuwagi sprawi, że stracimy ich nawet w najzwyklejszym pomieszczeniu.
266. [Tryby lochów i Kolei Refrakcji [2011002] — tytuł] 적의가 느껴지는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011002].title
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Tryby lochów i Kolei Refrakcji [2011002] — opis] 도달한 이 공간의 무게는 이제\n처음 느꼈던 것과는 크게 달라졌다.\n공간 하나 하나를 건널 때마다 수감자들이 크게 피로해진다.\n\n이곳에서 피로를 제어하지 못한다면, 위험한 공간에 들어서자마자 우리는 산산히 찢겨나갈 것이다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2011002].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The air in these spots has become considerably more oppressive than it was at first.\nEach step forward is a considerable undertaking for the Sinners.\n\nIf you’re unable to keep fatigue from taking over, any level of danger is sure to tear your team apart.
   PL: Ciężar tej przestrzeni nie przypomina już tego z początku drogi.\nKażde kolejne przejście coraz mocniej wyczerpuje Grzeszników.\n\nJeśli nie zapanujemy nad zmęczeniem, pierwsze groźniejsze starcie rozerwie nas na strzępy.
268. [Tryby lochów i Kolei Refrakcji [2012000] — tytuł] 기이한 감각이 새어나오는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2012000].title
   limit: do 40 znaków
   EN: Uncanny Presentiment
   PL: Przestrzeń Dziwnych Przeczuć
269. [Tryby lochów i Kolei Refrakcji [2012000] — opis] 온 몸의 털 끝이 저릿저릿 곤두선다.\n아직 아무것도 눈에 담지 않았지만, 이 앞에 분명하게 무언가 이해하기 어려운 것이 도사리고 있다는 것을 느낄 수 있다.\n\n가늠조차 할 수 없는, 이 세상의 것이\n아닌 듯한 무언가와 조우할 것만 같다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2012000].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The space ahead induces a hair-raising sensation.\nThough you’ve yet to see anything, you get the vivid feeling that something strange awaits ahead.\n\nYou know you’re about to come face to face with an unfathomable and otherworldly being.
   PL: Włosy jeżą się na całym ciele.\nChoć niczego jeszcze nie widać, czujesz wyraźnie, że tuż przed nami czai się coś niepojętego.\n\nLada chwila staniemy oko w oko z istotą nie z tego świata.
270. [Tryby lochów i Kolei Refrakcji [2012001] — tytuł] 기이한 감각이 새어나오는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2012001].title
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Tryby lochów i Kolei Refrakcji [2012001] — opis] 털 끝이 곤두서는 감각에 이 공간이 어떤 곳인지 순식간에 파악이 된다. 그것들은 이 세상의 것이 아니었다. 단순히 머리를 베고, 척추를 끊는 것으로 해결되지 않는 무언가였다. 어떤 것들이 그 자리에 도사리고 있을지는 모른다.\n\n우리가 할 수 있는 것은,\n최대한 빨리 그것을 파악하는 것 뿐이다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2012001].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The chill up your spine tells you what this space contains.\nThose things did not belong to this world. Neither a removed head nor a detached spinal cord ended their lives. You don’t know what you will face this time.\n\nThe one thing we can do…\nIs study them as quickly as possible.
   PL: Dreszcz przebiegający po karku natychmiast zdradza naturę tego miejsca.\nTe istoty nie należą do naszego świata — nie powstrzyma ich ani ścięcie głowy, ani przetrącenie kręgosłupa. Nie wiadomo, co przyjdzie nam tu spotkać.\n\nJedyne, co możemy zrobić,\nto jak najszybciej rozpoznać wroga.
272. [Tryby lochów i Kolei Refrakcji [2013000] — tytuł] 알 수 없는 괴성이 흘러나오는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2013000].title
   limit: do 40 znaków
   EN: Unknown Screams
   PL: Przestrzeń Nieznanych Wrzasków
273. [Tryby lochów i Kolei Refrakcji [2013000] — opis] 다른 공간보다 위험한 것이 기다리고 있는 것 같다.\n정체 모를 동물의 피비린내가 한층 더 짙고,\n조명이 더욱 공포스럽게 깜빡 대서 만은 아니다.\n오감에게 포착되지 않는 형언키 어려운 감각이\n전신을 핥아 내리고 있는 것이 그 이유이다.\n\n단단한 채비를 하지 않으면, 헤쳐 나가기 어려울 것 같다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2013000].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Something even more threatening seems to be ahead.\nThe scent of an unknown animal’s blood is stronger than ever.\nThe lights flicker eerily, but those are not your only clues.\nAn indescribable feeling, beyond your five senses…\nIt licks your entire body with a clear warning.\n\nYou must brace yourself to get through this area.
   PL: Przed nami czeka coś groźniejszego niż dotychczas.\nNie chodzi wyłącznie o gęsty odór zwierzęcej krwi ani złowieszczo migoczące światła.\nNieuchwytne dla pięciu zmysłów przeczucie spływa po całym ciele wyraźnym ostrzeżeniem.\n\nBez solidnego przygotowania trudno będzie przebić się dalej.
274. [Tryby lochów i Kolei Refrakcji [2013001] — tytuł] 알 수 없는 괴성이 흘러나오는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2013001].title
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Tryby lochów i Kolei Refrakcji [2013001] — opis] 위기감이 뒷목을 쓸고 내려가는 감각은 이전보다 더욱 짙어져있다.  기이한 악몽, 광기 어린 비명, 과육을 짜내듯 불쾌한 소리가 시시각각 사방에서 터져나온다.\n어느 순간인지 모를 순간 부터, 허벅지에 경련이 오는 것을 느꼈다. 걸음을 옮기지 말라는 몸의 경고임을 알 수 있다.\n\n하지만 나아가는 것 만이 답이라는 것 또한, 알고있다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2013001].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A more vivid sense of danger breathes down your neck. Strange nightmares, maddening shrills, and eerie noises in mimicry of a fruit being drained of its lifeblood all constantly assault your senses.\nAt one point, your thighs even begin to tremble. Your own body might be trying to prevent you from approaching such imminent peril.\n\nNevertheless, you know that the only path is forward.
   PL: Poczucie zagrożenia na karku zgęstniało jeszcze bardziej. Ze wszystkich stron wybuchają koszmarne wizje, obłąkańcze wrzaski i obrzydliwy odgłos wyciskanego miąższu.\nW pewnej chwili uda zaczynają drżeć w skurczu — własne ciało ostrzega, by nie stawiać kolejnego kroku.\n\nWiesz jednak dobrze, że jedyna droga prowadzi naprzód.
276. [Tryby lochów i Kolei Refrakcji [2014000] — tytuł] 비치우는 공간이 가장 강렬히 왜곡되는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014000].title
   limit: do 50 znaków
   EN: Inordinately Warped Reflection
   PL: Przestrzeń Skrajnego Załamania
277. [Tryby lochów i Kolei Refrakcji [2014000] — opis] 이곳에서 또 한 번 굴절될 것만 같다.\n이곳을 무사히 지날 수만 있다면.\n그러나 어째서인지, 더 깊은 곳으로 꺾여 들어가기 보다는 튕겨져 나갈 것만 같다는 예감도 사무친다. 어느 방향으로 비추어지든, 그 이전으로 돌아갈 수는 없을 것이다.\n\n단단한 벽으로 된 것만 같은 공포감에 압도되어 버린다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014000].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This looks to be another point of refraction.\nIf you can just make it past here…\nBut, you also get the feeling that it might repel you rather than take you deeper inside. Whichever direction it decides to lead you, there will be no going back.\n\nA solid wall of fear overwhelms you.
   PL: Wygląda na to, że tutaj znów nastąpi załamanie ścieżki — o ile zdołamy przejść cało.\nGłęboko w środku kiełkuje jednak przeczucie, że zamiast zejść głębiej, zostaniemy odbici na zewnątrz. Niezależnie od kierunku odwrotu już nie będzie.\n\nPrzytłacza cię strach twardy niczym mur.
278. [Tryby lochów i Kolei Refrakcji [2014001] — tytuł] 비치우는 공간이 가장 강렬히 왜곡되는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014001].title
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Tryby lochów i Kolei Refrakcji [2014001] — opis] 한 번은 겪었던 공간이다.\n그러나 여전히 흉악한 공포감이 단단한 성벽처럼 서 있다.\n이전과 같이, 이번에도 굴절되어 아래로 향할 수 있을까.\n아니면 파손된 거울의 갈라진 틈새에 튕겨나가 소멸될까.\n\n이제 와서 돌아갈 수는 없을 것이다.\n그저 받아들이는 수 밖에 없다.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014001].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You’ve been through this at least once before.\nEven still, foreboding terror stands tall like a castle wall.\nWill you be able to refract downwards to the area below?\nWill you be reflected between the cracks of the damaged mirror straight into nothingness?\n\nTurning back is out of the question now.\nYou have to accept whatever outcome it grants you.
   PL: Byliśmy już kiedyś w podobnym miejscu,\nlecz groza wciąż wznosi się przed nami jak warowny mur.\nCzy i tym razem załamiemy się ku głębszym warstwom?\nCzy też odbijemy się w szczelinach pękniętego lustra i przepadniemy w nicości?\n\nNa odwrót jest już za późno.\nPozostaje przyjąć to, co przyniesie los.
280. [Tryby lochów i Kolei Refrakcji [2014002] — tytuł] 비치우는 공간이 가장 강렬히 왜곡되는 공간
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014002].title
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Tryby lochów i Kolei Refrakcji [2014002] — opis] 또 다시 이 벽에 다다랐다.\n언제든지 벽이 넘어져 나와 수감자를 덮칠 것만 같다.\n그래서, 어떻게든 돌아가기 위해 왼쪽으로, 오른쪽으로 달려보지만 벽은 끝이 없다. 뒤로 돌아 이 곳을 벗어나지\n않는 이상, 방법은 벽을 부수는 것 밖에 없을 것이다.\n\n공포를 직면하는 것 만이 자신을 지키는 길이니까.
   źródło: MirrorDungeonNode1-1.json :: dataList[id=2014002].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You meet the wall once again.\nIt seems as though it might tip over and crush your Sinners at any second.\nYou try running left and right to circumvent it, but the wall is endless.\nYour only two choices are to turn around and walk away…\nOr break this wall to move forward.\n\nFacing the fear is how you secure your safety.
   PL: Znów stanęliśmy przed tym murem.\nZdaje się, że w każdej chwili może runąć i zmiażdżyć Grzeszników.\nBiegniemy w lewo i w prawo w poszukiwaniu obejścia, lecz mur nie ma końca. O ile nie zawrócimy,\njedyne wyjście to przebić go na wylot.\n\nTylko stawiając czoła lękowi, ocalimy własne życie.

## Tryby lochów i Kolei Refrakcji: MirrorDungeonRentalName
- plik gry: `MirrorDungeonRentalName.json`

282. [Tryby lochów i Kolei Refrakcji [1] — tekst] 관통, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=1].content
   limit: do 120 znaków
   EN: Pierce, Poise
   PL: Kłucie, Oddech
283. [Tryby lochów i Kolei Refrakcji [2] — tekst] 진동
   źródło: MirrorDungeonRentalName.json :: dataList[id=2].content
   limit: do 120 znaków
   EN: Tremor
   PL: Wstrząs
284. [Tryby lochów i Kolei Refrakcji [3] — tekst] 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=3].content
   limit: do 120 znaków
   EN: Rupture
   PL: Rozdarcie
285. [Tryby lochów i Kolei Refrakcji [4] — tekst] 진동, 화상, 파열, 호흡, 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=4].content
   limit: do 120 znaków
   EN: Tremor, Burn, Rupture, Poise, Charge
   PL: Wstrząs, Podpalenie, Rozdarcie, Oddech, Ładunek
286. [Tryby lochów i Kolei Refrakcji [5] — tekst] 화상, 출혈, 진동
   źródło: MirrorDungeonRentalName.json :: dataList[id=5].content
   limit: do 120 znaków
   EN: Burn, Bleed, Tremor
   PL: Podpalenie, Krwawienie, Wstrząs
287. [Tryby lochów i Kolei Refrakcji [6] — tekst] 침잠
   źródło: MirrorDungeonRentalName.json :: dataList[id=6].content
   limit: do 120 znaków
   EN: Sinking
   PL: Zatonięcie
288. [Tryby lochów i Kolei Refrakcji [7] — tekst] 출혈, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=7].content
   limit: do 120 znaków
   EN: Bleed, Poise
   PL: Krwawienie, Oddech
289. [Tryby lochów i Kolei Refrakcji [8] — tekst] 충전, 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=8].content
   limit: do 120 znaków
   EN: Charge, Rupture
   PL: Ładunek, Rozdarcie
290. [Tryby lochów i Kolei Refrakcji [9] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=9].content
   limit: do 120 znaków
   EN: Bleed
   PL: Krwawienie
291. [Tryby lochów i Kolei Refrakcji [10] — tekst] 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=10].content
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [Tryby lochów i Kolei Refrakcji [11] — tekst] 관통, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=11].content
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Tryby lochów i Kolei Refrakcji [12] — tekst] 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=12].content
   limit: do 120 znaków
   EN: Charge
   PL: Ładunek
294. [Tryby lochów i Kolei Refrakcji [13] — tekst] 침잠
   źródło: MirrorDungeonRentalName.json :: dataList[id=13].content
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
295. [Tryby lochów i Kolei Refrakcji [14] — tekst] 침잠, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=14].content
   limit: do 120 znaków
   EN: Sinking, Poise
   PL: Zatonięcie, Oddech
296. [Tryby lochów i Kolei Refrakcji [15] — tekst] 출혈, 질투
   źródło: MirrorDungeonRentalName.json :: dataList[id=15].content
   limit: do 120 znaków
   EN: Bleed, Envy
   PL: Krwawienie, Zawiść
297. [Tryby lochów i Kolei Refrakcji [16] — tekst] 침잠
   źródło: MirrorDungeonRentalName.json :: dataList[id=16].content
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Tryby lochów i Kolei Refrakcji [17] — tekst] 침잠
   źródło: MirrorDungeonRentalName.json :: dataList[id=17].content
   (powtórzenie elementu 287 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [Tryby lochów i Kolei Refrakcji [18] — tekst] 침잠, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=18].content
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Tryby lochów i Kolei Refrakcji [19] — tekst] 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=19].content
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Tryby lochów i Kolei Refrakcji [20] — tekst] 충전, 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=20].content
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Tryby lochów i Kolei Refrakcji [21] — tekst] 출혈, 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=21].content
   limit: do 120 znaków
   EN: Bleed, Charge
   PL: Krwawienie, Ładunek
303. [Tryby lochów i Kolei Refrakcji [22] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=22].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Tryby lochów i Kolei Refrakcji [23] — tekst] 질투, 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=23].content
   limit: do 120 znaków
   EN: Envy, Bleed
   PL: Zawiść, Krwawienie
305. [Tryby lochów i Kolei Refrakcji [24] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=24].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Tryby lochów i Kolei Refrakcji [25] — tekst] 질투, 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=25].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Tryby lochów i Kolei Refrakcji [26] — tekst] 출혈, 호흡
   źródło: MirrorDungeonRentalName.json :: dataList[id=26].content
   (powtórzenie elementu 288 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Tryby lochów i Kolei Refrakcji [27] — tekst] 진동, 화상
   źródło: MirrorDungeonRentalName.json :: dataList[id=27].content
   limit: do 120 znaków
   EN: Tremor, Burn
   PL: Wstrząs, Podpalenie
309. [Tryby lochów i Kolei Refrakcji [28] — tekst] 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=28].content
   (powtórzenie elementu 284 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Tryby lochów i Kolei Refrakcji [29] — tekst] 충전, 파열
   źródło: MirrorDungeonRentalName.json :: dataList[id=29].content
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Tryby lochów i Kolei Refrakcji [30] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=30].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Tryby lochów i Kolei Refrakcji [31] — tekst] 호흡, 관통
   źródło: MirrorDungeonRentalName.json :: dataList[id=31].content
   limit: do 120 znaków
   EN: Poise, Pierce
   PL: Oddech, Kłucie
313. [Tryby lochów i Kolei Refrakcji [32] — tekst] 질투, 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=32].content
   (powtórzenie elementu 304 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Tryby lochów i Kolei Refrakcji [33] — tekst] 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=33].content
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Tryby lochów i Kolei Refrakcji [34] — tekst] 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=34].content
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Tryby lochów i Kolei Refrakcji [35] — tekst] 진동, 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=35].content
   limit: do 120 znaków
   EN: Tremor, Charge
   PL: Wstrząs, Ładunek
317. [Tryby lochów i Kolei Refrakcji [36] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=36].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Tryby lochów i Kolei Refrakcji [37] — tekst] 출혈
   źródło: MirrorDungeonRentalName.json :: dataList[id=37].content
   (powtórzenie elementu 290 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Tryby lochów i Kolei Refrakcji [38] — tekst] 충전
   źródło: MirrorDungeonRentalName.json :: dataList[id=38].content
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Tryby lochów i Kolei Refrakcji [39] — tekst] 거미집
   źródło: MirrorDungeonRentalName.json :: dataList[id=39].content
   limit: do 120 znaków
   EN: The House of Spiders
   PL: Dom Pająków

## Tryby lochów i Kolei Refrakcji: MirrorDungeonRentalUI
- plik gry: `MirrorDungeonRentalUI.json`

321. [Tryby lochów i Kolei Refrakcji [mirror_rental_title] — tekst] 편성 대여
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_title].content
   limit: do 120 znaków
   EN: Team Rental
   PL: Wypożyczenie składu
322. [Tryby lochów i Kolei Refrakcji [mirror_rental_no_item] — tekst] 현재 사용 가능한 대여 편성이 없습니다.
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_no_item].content
   limit: do 120 znaków
   EN: No available Rental Teams.
   PL: Brak dostępnych składów do wypożyczenia.
323. [Tryby lochów i Kolei Refrakcji [mirror_rental_period] — tekst] 대여 기간
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_period].content
   limit: do 120 znaków
   EN: Rental Period
   PL: Okres wypożyczenia
324. [Tryby lochów i Kolei Refrakcji [mirror_rental_keyword_label] — tekst] 키워드
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_keyword_label].content
   limit: do 120 znaków
   EN: Keywords
   PL: Słowa kluczowe
325. [Tryby lochów i Kolei Refrakcji [mirror_rental_ask_to_enter] — tekst] 대여 편성을 사용하여\n{0}에 입장하시겠습니까?
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_ask_to_enter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: <font="EN/Pretendard/Pretendard-Regular SDF">Use {0} with a Rental Team?</font>
   PL: Wejść do: {0},\nkorzystając z wypożyczonego składu?
326. [Tryby lochów i Kolei Refrakcji [mirror_rental_warnings] — tekst] • 대여 기간 중 1회 한정으로 편성을 대여하여 거울 던전을 플레이할 수 있습니다.\n\n • 대여 편성 사용시 상점에서 인격 및 E.G.O 스킬 교체를 할 수 없으며, 평행 중첩 모드에 진입할 수 없습니다.\n\n • 대여 편성으로 거울 던전 클리어 시에도 거울 던전 클리어 보상과 이벤트 재화를 획득할 수 있습니다. \n\n• 주간 추가 보상 기회는 3회 중 1회만 소모할 수 있습니다.\n\n• 거울 던전 클리어 보상 수령 시 대여 횟수가 차감됩니다.
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_warnings].content
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <font="EN/Pretendard/Pretendard-Regular SDF">• Players have one Rental chance to rent the Team over the rental period to play through the Mirror Dungeon.\n\n• When using a rental Team, the Mirror Dungeon Identity & E.G.O swap function and the Parallel Superposition Mode(Infinity Mode) will not be accessible.\n\n• You can obtain Mirror Dungeon clear rewards and Event currencies by clearing the Mirror Dungeon using the Rental team.\n\n• Only one out of three Weekly Bonuses can be consumed when clearing a Mirror Dungeon with a Rental Team.\n\n• Claiming the Mirror Dungeon Clear Reward will consume your Rental chance.\n\n\n\n\n</font>
   PL: • W okresie wypożyczenia można jednorazowo wypożyczyć skład, aby rozegrać Lustrzany Loch.\n\n• Podczas gry wypożyczonym składem nie można wymieniać Tożsamości ani umiejętności E.G.O w Sklepie oraz nie można wejść w Tryb Superpozycji Równoległej.\n\n• Ukończenie Lustrzanego Lochu wypożyczonym składem również zapewnia nagrody za ukończenie oraz walutę wydarzenia.\n\n• Można przy tym zużyć maksymalnie 1 z 3 szans na Cotygodniową Premię.\n\n• Odebranie nagrody za ukończenie Lustrzanego Lochu zużywa limit wypożyczenia.
327. [Tryby lochów i Kolei Refrakcji [mirror_rental_unable_by_running_other] — tekst] 던전 진행 중
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_unable_by_running_other].content
   limit: do 120 znaków
   EN: Dungeon In Progress
   PL: Loch w toku
328. [Tryby lochów i Kolei Refrakcji [mirror_rental_already_reward_acquired] — tekst] 보상 획득 완료
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_already_reward_acquired].content
   limit: do 120 znaków
   EN: Rewards Claimed
   PL: Nagrody odebrane
329. [Tryby lochów i Kolei Refrakcji [unable_to_change_formation_by_rental_formation] — tekst] 편성 변경 불가
   źródło: MirrorDungeonRentalUI.json :: dataList[id=unable_to_change_formation_by_rental_formation].content
   limit: do 120 znaków
   EN: Fixed Team
   PL: Stały skład
330. [Tryby lochów i Kolei Refrakcji [mirror_rental_failed_to_enter] — tekst] 유효하지 않은 대여 편성 데이터입니다. UI가 최신화되었습니다.\n(error code : {0})
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_failed_to_enter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Invalid Rental Team Data. UI has been refreshed.\n(error code : {0})
   PL: Nieprawidłowe dane wypożyczonego składu. Odświeżono interfejs.\n(kod błędu: {0})
331. [Tryby lochów i Kolei Refrakcji [mirror_rental_button_label] — tekst] 대여
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_rental_button_label].content
   limit: do 120 znaków
   EN: Rental
   PL: Wypożycz
332. [Tryby lochów i Kolei Refrakcji [mirror_unable_to_infinity_by_rental] — tekst] 대여 편성 사용시 적용 불가
   źródło: MirrorDungeonRentalUI.json :: dataList[id=mirror_unable_to_infinity_by_rental].content
   limit: do 120 znaków
   EN: Cannot activate with a Rental Team
   PL: Niedostępne dla wypożyczonego składu

## Tryby lochów i Kolei Refrakcji: MirrorDungeonTheme-1
- plik gry: `MirrorDungeonTheme-1.json`

333. [Tryby lochów i Kolei Refrakcji [1001] — nazwa] 잊혀진 자들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1001].name
   limit: do 40 znaków
   EN: The Forgotten
   PL: Zapomniani
334. [Tryby lochów i Kolei Refrakcji [1002] — nazwa] 속하지 못하는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1002].name
   limit: do 40 znaków
   EN: The Outcast
   PL: Nieprzynależny
335. [Tryby lochów i Kolei Refrakcji [1003] — nazwa] 카지노 푸어
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1003].name
   limit: do 40 znaków
   EN: Flat-broke Gamblers
   PL: Spłukani Hazardziści
336. [Tryby lochów i Kolei Refrakcji [1004] — nazwa] 공장 자동화
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1004].name
   limit: do 40 znaków
   EN: Automated Factory
   PL: Automatyzacja Fabryki
337. [Tryby lochów i Kolei Refrakcji [1005] — nazwa] 사랑할 수 없는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1005].name
   limit: do 40 znaków
   EN: The Unloving
   PL: Niekochająca
338. [Tryby lochów i Kolei Refrakcji [1006] — nazwa] 못과 망치
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1006].name
   limit: do 40 znaków
   EN: Nagel und Hammer
   PL: Nagel und Hammer
339. [Tryby lochów i Kolei Refrakcji [1007] — nazwa] 신앙과 침식
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1007].name
   limit: do 40 znaków
   EN: Faith & Erosion
   PL: Wiara i Korozja
340. [Tryby lochów i Kolei Refrakcji [1008] — nazwa] 마주하지 않는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1008].name
   limit: do 40 znaków
   EN: The Unconfronting
   PL: Unikający
341. [Tryby lochów i Kolei Refrakcji [1009] — nazwa] 둥지, 공방, 기술
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1009].name
   limit: do 50 znaków
   EN: Nest, Workshop, and Technology
   PL: Gniazdo, Warsztat i Technologia
342. [Tryby lochów i Kolei Refrakcji [1010] — nazwa] 낙화
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1010].name
   limit: do 40 znaków
   EN: Falling Flowers
   PL: Opadające Kwiaty
343. [Tryby lochów i Kolei Refrakcji [1011] — nazwa] 흘리는 것들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1011].name
   limit: do 40 znaków
   EN: Tearful Things
   PL: To, Co Spływa Łzami
344. [Tryby lochów i Kolei Refrakcji [1012] — nazwa] 변하지 않는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1012].name
   limit: do 40 znaków
   EN: The Unchanging
   PL: Niezmienny
345. [Tryby lochów i Kolei Refrakcji [1013] — nazwa] 레이크 월드
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1013].name
   limit: do 40 znaków
   EN: Lake World
   PL: Świat Jeziora
346. [Tryby lochów i Kolei Refrakcji [1014] — nazwa] 기어오는 심연
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1014].name
   limit: do 40 znaków
   EN: Crawling Abyss
   PL: Pełznąca Otchłań
347. [Tryby lochów i Kolei Refrakcji [1015] — nazwa] 악으로 규정되는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1015].name
   limit: do 40 znaków
   EN: The Evil Defining
   PL: Naznaczające Zło
348. [Tryby lochów i Kolei Refrakcji [1016] — nazwa] 저택의 부산물
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1016].name
   limit: do 40 znaków
   EN: Dregs of the Manor
   PL: Pozostałości Posiadłości
349. [Tryby lochów i Kolei Refrakcji [1017] — nazwa] 어느 세계
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1017].name
   limit: do 40 znaków
   EN: A Certain World
   PL: Pewien Świat
350. [Tryby lochów i Kolei Refrakcji [1101] — nazwa] 헬스치킨
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1101].name
   limit: do 40 znaków
   EN: Hell's Chicken
   PL: Piekielny Kurczak
351. [Tryby lochów i Kolei Refrakcji [1102] — nazwa] 우.미.다
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1102].name
   limit: do 40 znaków
   EN: S.E.A.
   PL: M.O.R.Z.E.
352. [Tryby lochów i Kolei Refrakcji [1103] — nazwa] 20번구의 기적
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1103].name
   limit: do 40 znaków
   EN: Miracle in District 20
   PL: Cud w Dystrykcie 20
353. [Tryby lochów i Kolei Refrakcji [1104] — nazwa] 육참골단
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1104].name
   limit: do 50 znaków
   EN: Yield My Flesh to Claim Their Bones
   PL: Oddam Ciało, by Złamać Ich Kości
354. [Tryby lochów i Kolei Refrakcji [1201] — nazwa] 가르고 베는 이들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1201].name
   limit: do 40 znaków
   EN: Slicers & Dicers
   PL: Tnący i Siekący
355. [Tryby lochów i Kolei Refrakcji [1202] — nazwa] 베어낼 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1202].name
   limit: do 40 znaków
   EN: To be Cleaved
   PL: Do Rozcięcia
356. [Tryby lochów i Kolei Refrakcji [1203] — nazwa] 꿰고 뚫는 이들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1203].name
   limit: do 40 znaków
   EN: Piercers & Penetrators
   PL: Kłujący i Przebijający
357. [Tryby lochów i Kolei Refrakcji [1204] — nazwa] 꿰뚫을 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1204].name
   limit: do 40 znaków
   EN: To be Pierced
   PL: Do Przebicia
358. [Tryby lochów i Kolei Refrakcji [1205] — nazwa] 부수고 깨뜨릴 이들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1205].name
   limit: do 40 znaków
   EN: Crushers & Breakers
   PL: Miażdżący i Kruszący
359. [Tryby lochów i Kolei Refrakcji [1206] — nazwa] 바스라질 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1206].name
   limit: do 40 znaków
   EN: To be Crushed
   PL: Do Zmiażdżenia
360. [Tryby lochów i Kolei Refrakcji [1301] — nazwa] 억눌린 분노
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1301].name
   limit: do 40 znaków
   EN: Repressed Wrath
   PL: Stłumiony Gniew
361. [Tryby lochów i Kolei Refrakcji [1302] — nazwa] 해방된 분노
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1302].name
   limit: do 40 znaków
   EN: Unbound Wrath
   PL: Wyzwolony Gniew
362. [Tryby lochów i Kolei Refrakcji [1303] — nazwa] 감정에 짓눌리는 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1303].name
   limit: do 40 znaków
   EN: Emotional Repression
   PL: Przygniecenie Uczuciami
363. [Tryby lochów i Kolei Refrakcji [1304] — nazwa] 빠져드는 색욕
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1304].name
   limit: do 40 znaków
   EN: Addicting Lust
   PL: Uzależniająca Żądza
364. [Tryby lochów i Kolei Refrakcji [1305] — nazwa] 옭아매는 색욕
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1305].name
   limit: do 40 znaków
   EN: Tangling Lust
   PL: Spętanie Żądzą
365. [Tryby lochów i Kolei Refrakcji [1306] — nazwa] 감정에 홀리는 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1306].name
   limit: do 40 znaków
   EN: Emotional Seduction
   PL: Omamienie Uczuciami
366. [Tryby lochów i Kolei Refrakcji [1307] — nazwa] 헛도는 나태
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1307].name
   limit: do 40 znaków
   EN: Treadwheel Sloth
   PL: Jałowe Lenistwo
367. [Tryby lochów i Kolei Refrakcji [1308] — nazwa] 멎어버린 나태
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1308].name
   limit: do 40 znaków
   EN: Inert Sloth
   PL: Zastygłe Lenistwo
368. [Tryby lochów i Kolei Refrakcji [1309] — nazwa] 감정 앞에 게으른 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1309].name
   limit: do 40 znaków
   EN: Emotional Indolence
   PL: Zobojętnienie Uczuć
369. [Tryby lochów i Kolei Refrakcji [1310] — nazwa] 먹어치운 탐식
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1310].name
   limit: do 40 znaków
   EN: Devoured Gluttony
   PL: Nienasycone Obżarstwo
370. [Tryby lochów i Kolei Refrakcji [1311] — nazwa] 넘쳐흐른 탐식
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1311].name
   limit: do 40 znaków
   EN: Excessive Gluttony
   PL: Wylewające się Obżarstwo
371. [Tryby lochów i Kolei Refrakcji [1312] — nazwa] 감정에 굶주린 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1312].name
   limit: do 40 znaków
   EN: Emotional Craving
   PL: Głód Uczuć
372. [Tryby lochów i Kolei Refrakcji [1313] — nazwa] 전락하는 우울
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1313].name
   limit: do 40 znaków
   EN: Degraded Gloom
   PL: Upadła Posępność
373. [Tryby lochów i Kolei Refrakcji [1314] — nazwa] 가라앉은 우울
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1314].name
   limit: do 40 znaków
   EN: Sunk Gloom
   PL: Zatopiona Posępność
374. [Tryby lochów i Kolei Refrakcji [1315] — nazwa] 감정에 침수된 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1315].name
   limit: do 40 znaków
   EN: Emotional Flood
   PL: Zalanie Uczuciami
375. [Tryby lochów i Kolei Refrakcji [1316] — nazwa] 허세짙은 오만
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1316].name
   limit: do 40 znaków
   EN: Vain Pride
   PL: Próżna Pycha
376. [Tryby lochów i Kolei Refrakcji [1317] — nazwa] 독선적인 오만
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1317].name
   limit: do 40 znaków
   EN: Tyrannical Pride
   PL: Samowładna Pycha
377. [Tryby lochów i Kolei Refrakcji [1318] — nazwa] 감정에 복종한 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1318].name
   limit: do 40 znaków
   EN: Emotional Subservience
   PL: Uległość Uczuciom
378. [Tryby lochów i Kolei Refrakcji [1319] — nazwa] 초라한 질투
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1319].name
   limit: do 40 znaków
   EN: Insignificant Envy
   PL: Nędzna Zawiść
379. [Tryby lochów i Kolei Refrakcji [1320] — nazwa] 처량한 질투
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1320].name
   limit: do 40 znaków
   EN: Pitiful Envy
   PL: Żałosna Zawiść
380. [Tryby lochów i Kolei Refrakcji [1321] — nazwa] 감정으로 평가된 것
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1321].name
   limit: do 40 znaków
   EN: Emotional Judgment
   PL: Osąd Uczuć
381. [Tryby lochów i Kolei Refrakcji [1401] — nazwa] 타오르는 일렁임
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1401].name
   limit: do 40 znaków
   EN: Burning Haze
   PL: Płonące Drganie
382. [Tryby lochów i Kolei Refrakcji [1402] — nazwa] 화왕지절
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1402].name
   limit: do 40 znaków
   EN: Season of the Flame
   PL: Pora Władcy Ognia
383. [Tryby lochów i Kolei Refrakcji [1403] — nazwa] 새어나온 적혈
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1403].name
   limit: do 40 znaków
   EN: Trickled Sanguine Blood
   PL: Sącząca się Posoka
384. [Tryby lochów i Kolei Refrakcji [1404] — nazwa] 시산혈해
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1404].name
   limit: do 50 znaków
   EN: Mountain of Corpses, Sea of Blood
   PL: Góra Trupów, Morze Krwi
385. [Tryby lochów i Kolei Refrakcji [1405] — nazwa] 어지러운 파동
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1405].name
   limit: do 40 znaków
   EN: Dizzying Waves
   PL: Przyprawiające o Zawrót Fale
386. [Tryby lochów i Kolei Refrakcji [1406] — nazwa] 이상진역
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1406].name
   limit: do 40 znaków
   EN: Abnormal Seismic Zone
   PL: Strefa Anomalii Sejsmicznej
387. [Tryby lochów i Kolei Refrakcji [1407] — nazwa] 부서뜨리는 외력
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1407].name
   limit: do 40 znaków
   EN: Crushing External Force
   PL: Krusząca Siła Zewnętrzna
388. [Tryby lochów i Kolei Refrakcji [1408] — nazwa] 파죽지세
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1408].name
   limit: do 40 znaków
   EN: Unrelenting Might
   PL: Niepowstrzymany Rozmach
389. [Tryby lochów i Kolei Refrakcji [1409] — nazwa] 잠겨드는 아림
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1409].name
   limit: do 40 znaków
   EN: Sinking Pang
   PL: Tonące Ukłucie
390. [Tryby lochów i Kolei Refrakcji [1410] — nazwa] 침잠쇄도
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1410].name
   limit: do 40 znaków
   EN: Sinking Deluge
   PL: Nawałnica Zatonięcia
391. [Tryby lochów i Kolei Refrakcji [1411] — nazwa] 내쉬어진 한숨
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1411].name
   limit: do 40 znaków
   EN: Deep Sigh
   PL: Głębokie Westchnienie
392. [Tryby lochów i Kolei Refrakcji [1412] — nazwa] 순환호흡
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1412].name
   limit: do 40 znaków
   EN: Poised Breathing
   PL: Oddech Krążenia
393. [Tryby lochów i Kolei Refrakcji [1413] — nazwa] 차오르는 동력
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1413].name
   limit: do 40 znaków
   EN: Rising Power Supply
   PL: Wzrastająca Moc
394. [Tryby lochów i Kolei Refrakcji [1414] — nazwa] 벽력섬전
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1414].name
   limit: do 40 znaków
   EN: Thunder and Lightning
   PL: Grom i Błyskawica
395. [Tryby lochów i Kolei Refrakcji [1105] — nazwa] 시간살인시간
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1105].name
   limit: do 40 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
396. [Tryby lochów i Kolei Refrakcji [1106] — nazwa] 워프특급 살인사건
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1106].name
   limit: do 40 znaków
   EN: Murder on the WARP Express
   PL: Morderstwo w Ekspresie WARP
397. [Tryby lochów i Kolei Refrakcji [1107] — nazwa] 자색 정오의 시련
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1107].name
   limit: do 40 znaków
   EN: The Noon of Violet
   PL: Próba Fioletowego Południa
398. [Tryby lochów i Kolei Refrakcji [1018] — nazwa] 마음이 어긋나는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1018].name
   limit: do 40 znaków
   EN: The Heartbreaking
   PL: Rozdzierające Serca
399. [Tryby lochów i Kolei Refrakcji [1019] — nazwa] 다시 열린 라만차랜드
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1019].name
   limit: do 40 znaków
   EN: La Manchaland Re-opening
   PL: Ponowne Otwarcie La Manchalandu
400. [Tryby lochów i Kolei Refrakcji [1020] — nazwa] 끝나지 않는 행렬
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1020].name
   limit: do 40 znaków
   EN: The Infinite Procession
   PL: Niekończąca się Parada
401. [Tryby lochów i Kolei Refrakcji [1108] — nazwa] 1호선
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1108].name
   limit: do 40 znaków
   EN: Line 1
   PL: Linia 1
402. [Tryby lochów i Kolei Refrakcji [1109] — nazwa] 2호선
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1109].name
   limit: do 40 znaków
   EN: Line 2
   PL: Linia 2
403. [Tryby lochów i Kolei Refrakcji [1110] — nazwa] 3호선
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1110].name
   limit: do 40 znaków
   EN: Line 3
   PL: Linia 3
404. [Tryby lochów i Kolei Refrakcji [1111] — nazwa] 4호선 - 제 3 구간
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1111].name
   limit: do 40 znaków
   EN: Line 4 - Section #3
   PL: Linia 4 — Odcinek 3
405. [Tryby lochów i Kolei Refrakcji [1112] — nazwa] 4호선 - 제 4 구간
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1112].name
   limit: do 40 znaków
   EN: Line 4 - Section #4
   PL: Linia 4 — Odcinek 4
406. [Tryby lochów i Kolei Refrakcji [1113] — nazwa] 20번구의 기적 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1113].name
   limit: do 50 znaków
   EN: Miracle in District 20 BokGak
   PL: Cud w Dystrykcie 20 BokGak
407. [Tryby lochów i Kolei Refrakcji [1114] — nazwa] 탄환이 찍은 마침표
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1114].name
   limit: do 40 znaków
   EN: Full-Stopped by a Bullet
   PL: Kropka Postawiona Kulą
408. [Tryby lochów i Kolei Refrakcji [1115] — nazwa] LCB 정기검진
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1115].name
   limit: do 40 znaków
   EN: LCB Regular Check-up
   PL: Okresowe Badania LCB
409. [Tryby lochów i Kolei Refrakcji [1116] — nazwa] 육참골단 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1116].name
   limit: do 60 znaków
   EN: Yield My Flesh to Claim Their Bones BokGak
   PL: Oddam Ciało, by Złamać Ich Kości BokGak
410. [Tryby lochów i Kolei Refrakcji [1117] — nazwa] 심야청소
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1117].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping
   PL: Nocne Sprzątanie
411. [Tryby lochów i Kolei Refrakcji [1118] — nazwa] 5호선
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1118].name
   limit: do 40 znaków
   EN: Line 5
   PL: Linia 5
412. [Tryby lochów i Kolei Refrakcji [1021] — nazwa] 꿈이 끝나는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1021].name
   limit: do 40 znaków
   EN: The Dream Ending
   PL: Koniec Snu
413. [Tryby lochów i Kolei Refrakcji [1022] — nazwa] 사대 가문과 욕망
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1022].name
   limit: do 40 znaków
   EN: Four Houses and Greed
   PL: Cztery Rody i Chciwość
414. [Tryby lochów i Kolei Refrakcji [1023] — nazwa] 바라볼 수밖에 없는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1023].name
   limit: do 40 znaków
   EN: The Surrendered Witnessing
   PL: Skazany na Patrzenie
415. [Tryby lochów i Kolei Refrakcji [1119] — nazwa] 증오와 절망
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1119].name
   limit: do 40 znaków
   EN: Hatred and Despair
   PL: Nienawiść i Rozpacz
416. [Tryby lochów i Kolei Refrakcji [1119] — nazwa specjalna] <color=#ee4893>증오와</color> <color=#0060c5>절망</color>
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1119].specialName
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <color=#ee4893>, </color>, <color=#0060c5>
   EN: <color=#ee4893>Hatred</color> and <color=#0060c5>Despair</color>
   PL: <color=#ee4893>Nienawiść</color> i <color=#0060c5>Rozpacz</color>
417. [Tryby lochów i Kolei Refrakcji [1120] — nazwa] 시간살인시간 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1120].name
   limit: do 40 znaków
   EN: Timekilling Time BokGak
   PL: Czas Zabijania Czasu BokGak
418. [Tryby lochów i Kolei Refrakcji [1121] — nazwa] 절차탁춘
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1121].name
   limit: do 40 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
419. [Tryby lochów i Kolei Refrakcji [1501] — nazwa] N사 신 구인회
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1501].name
   limit: do 60 znaków
   EN: N Corp. New League of Nine Littérateurs
   PL: Nowy Krąg Dziewięciu N Corp.
420. [Tryby lochów i Kolei Refrakcji [1502] — nazwa] 개화하는 녹림
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1502].name
   limit: do 40 znaków
   EN: Efflorescing Greenery
   PL: Rozkwitający Zielony Las
421. [Tryby lochów i Kolei Refrakcji [1503] — nazwa] 3호선 - 종착역
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1503].name
   limit: do 40 znaków
   EN: Line 3 - Terminus
   PL: Linia 3 — Stacja Końcowa
422. [Tryby lochów i Kolei Refrakcji [1504] — nazwa] 영겁의 굴레
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1504].name
   limit: do 40 znaków
   EN: Bridle of Infinity
   PL: Jarzmo Wieczności
423. [Tryby lochów i Kolei Refrakcji [1505] — nazwa] 우.미.다 게.판
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1505].name
   limit: do 40 znaków
   EN: S.E.A. C.R
   PL: M.O.R.Z.E. K.R.
424. [Tryby lochów i Kolei Refrakcji [1506] — nazwa] 끝도 없이 막힌 길
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1506].name
   limit: do 40 znaków
   EN: Impenetrable Path
   PL: Droga bez Przejścia
425. [Tryby lochów i Kolei Refrakcji [1507] — nazwa] 혈귀가 되지 못한 자들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1507].name
   limit: do 40 znaków
   EN: Who Couldn't be Bloodfiends
   PL: Ci, Którzy Nie Stali się Krwiożercami
426. [Tryby lochów i Kolei Refrakcji [1122] — nazwa] 선의의 순례
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1122].name
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
427. [Tryby lochów i Kolei Refrakcji [1508] — nazwa] 아름다운 목소리
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1508].name
   limit: do 40 znaków
   EN: A Beautiful Voice
   PL: Piękny Głos
428. [Tryby lochów i Kolei Refrakcji [1509] — nazwa] 녹빛 여명의 시련
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1509].name
   limit: do 40 znaków
   EN: The Dawn of Green
   PL: Próba Zielonego Świtu
429. [Tryby lochów i Kolei Refrakcji [1510] — nazwa] 어느 도서관의 어떤 책 속으로
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1510].name
   limit: do 50 znaków
   EN: Into a Certain Library's Book
   PL: W Księgę Pewnej Biblioteki
430. [Tryby lochów i Kolei Refrakcji [1123] — nazwa] 워프특급 살인사건 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1123].name
   limit: do 50 znaków
   EN: Murder on the WARP Express BokGak
   PL: Morderstwo w Ekspresie WARP BokGak
431. [Tryby lochów i Kolei Refrakcji [1024] — nazwa] 현혹, 방황, 불신
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1024].name
   limit: do 40 znaków
   EN: Charm, Wander, Doubt
   PL: Ułuda, Błądzenie, Nieufność
432. [Tryby lochów i Kolei Refrakcji [1025] — nazwa] 교본
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1025].name
   limit: do 40 znaków
   EN: Textbook
   PL: Podręcznik
433. [Tryby lochów i Kolei Refrakcji [1026] — nazwa] 검과 작품
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1026].name
   limit: do 40 znaków
   EN: Blade and Artwork
   PL: Ostrze i Dzieło
434. [Tryby lochów i Kolei Refrakcji [1027] — nazwa] 끊어지지 않는
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1027].name
   limit: do 40 znaków
   EN: The Unsevering
   PL: Nierozerwalne
435. [Tryby lochów i Kolei Refrakcji [1124] — nazwa] 호박색 어스름의 시련
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1124].name
   limit: do 40 znaków
   EN: The Dusk of Amber
   PL: Próba Bursztynowego Zmierzchu
436. [Tryby lochów i Kolei Refrakcji [1125] — nazwa] LCB 정기검진 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1125].name
   limit: do 40 znaków
   EN: LCB Regular Check-up BokGak
   PL: Okresowe Badania LCB BokGak
437. [Tryby lochów i Kolei Refrakcji [3001] — nazwa] 뽕.황
   źródło: MirrorDungeonTheme-1.json :: dataList[id=3001].name
   limit: do 40 znaków
   EN: The B.E.
   PL: C.K.
438. [Tryby lochów i Kolei Refrakcji [1126] — nazwa] 타래 엮기
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1126].name
   limit: do 40 znaków
   EN: Twining Threads
   PL: Splatanie Pasm
439. [Tryby lochów i Kolei Refrakcji [1127] — nazwa] 심야청소 BokGak
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1127].name
   limit: do 40 znaków
   EN: Nocturnal Sweeping BokGak
   PL: Nocne Sprzątanie BokGak
440. [Tryby lochów i Kolei Refrakcji [1511] — nazwa] 코드 퍼플
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1511].name
   limit: do 40 znaków
   EN: Code Purple
   PL: Kod Fioletowy
441. [Tryby lochów i Kolei Refrakcji [1512] — nazwa] 무게를 진 자들
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1512].name
   limit: do 40 znaków
   EN: Bearers of Weight
   PL: Dźwigający Ciężar
442. [Tryby lochów i Kolei Refrakcji [1513] — nazwa] 1호선 : 광기
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1513].name
   limit: do 40 znaków
   EN: Line 1 : MADNESS
   PL: Linia 1: SZALEŃSTWO
443. [Tryby lochów i Kolei Refrakcji [1514] — nazwa] 축복의 카니발
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1514].name
   limit: do 40 znaków
   EN: Blessed Carnival
   PL: Błogosławiony Karnawał
444. [Tryby lochów i Kolei Refrakcji [1515] — nazwa] 페어리테일
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1515].name
   limit: do 40 znaków
   EN: Fairy Tale
   PL: Baśń
445. [Tryby lochów i Kolei Refrakcji [1516] — nazwa] 핏물진 비린내
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1516].name
   limit: do 40 znaków
   EN: Bloodtinged Ichthyic Odor
   PL: Krwawy Rybi Odór
446. [Tryby lochów i Kolei Refrakcji [1517] — nazwa] 즉결처형의 시간
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1517].name
   limit: do 50 znaków
   EN: Complete & Total Extermination
   PL: Czas Doraźnej Egzekucji
447. [Tryby lochów i Kolei Refrakcji [1518] — nazwa] 라만차랜드의 주인
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1518].name
   limit: do 40 znaków
   EN: The Master of La Manchaland
   PL: Władca La Manchalandu
448. [Tryby lochów i Kolei Refrakcji [1519] — nazwa] 삽시호
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1519].name
   limit: do 40 znaków
   EN: Chachihu
   PL: Chachihu
449. [Tryby lochów i Kolei Refrakcji [1520] — nazwa] 한 봄 밤의 꿈 2
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1520].name
   limit: do 40 znaków
   EN: A Midspring Night's Dream 2
   PL: Sen Nocy Wiosennej 2
450. [Tryby lochów i Kolei Refrakcji [1128] — nazwa] 경험기억
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1128].name
   limit: do 40 znaków
   EN: Mnestic Experience
   PL: Pamięć Doświadczenia
451. [Tryby lochów i Kolei Refrakcji [1028] — nazwa] 오픈런
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1028].name
   limit: do 40 znaków
   EN: Storefront Campout
   PL: Nocna Kolejka przed Otwarciem
452. [Tryby lochów i Kolei Refrakcji [1029] — nazwa] 번잡한 색채
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1029].name
   limit: do 40 znaków
   EN: An Anarchy of Colors
   PL: Zgiełk Barw
453. [Tryby lochów i Kolei Refrakcji [1030] — nazwa] 보존의 신념
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1030].name
   limit: do 40 znaków
   EN: Creed of Preservation
   PL: Wiara w Zachowanie
454. [Tryby lochów i Kolei Refrakcji [1031] — nazwa] 탐식의 재림
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1031].name
   limit: do 40 znaków
   EN: Readvent of Gluttony
   PL: Powrót Obżarstwa
455. [Tryby lochów i Kolei Refrakcji [1129] — nazwa] 새벽 뒤 꿰뚫어 오는 쐐기
   źródło: MirrorDungeonTheme-1.json :: dataList[id=1129].name
   limit: do 50 znaków
   EN: The Wedge in the Wake of Dawnbreak
   PL: Klin Przebijający za Świtem

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI
- plik gry: `MirrorDungeonUI.json`

456. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_level_up] — tekst] 성장 인격 선택
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_level_up].content
   limit: do 120 znaków
   EN: Choose Identity to Level Up
   PL: Wybierz Tożsamość do rozwinięcia
457. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_ask_level_up] — tekst] 해당 인격을 성장시키겠습니까?
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_ask_level_up].content
   limit: do 120 znaków
   EN: Will you enhance the selected Identity?
   PL: Rozwinąć wybraną Tożsamość?
458. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_warning_stop_dungeon] — tekst] ※탐사를 마칠 시, 현재까지 클리어한 층을 기준으로 보상이 지급됩니다.
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_warning_stop_dungeon].content
   limit: do 120 znaków
   EN: ※ If you quit exploration, you’ll return with rewards based on the floors you’ve cleared.
   PL: ※ Po przerwaniu wyprawy nagrody zostaną przyznane na podstawie dotychczas ukończonych pięter.
459. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_current_reward] — tekst] 현재 보상
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_current_reward].content
   limit: do 120 znaków
   EN: Current Rewards
   PL: Bieżące nagrody
460. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_acquire_new_character] — tekst] 인격 획득
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_acquire_new_character].content
   limit: do 120 znaków
   EN: Identity Acquired
   PL: Zdobyto Tożsamość
461. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_level_up_complete] — tekst] 인격 성장 완료
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_level_up_complete].content
   limit: do 120 znaków
   EN: Identity Upgraded
   PL: Rozwinięto Tożsamość
462. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_continue] — tekst] 탐사를 계속 진행하겠습니까?
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_continue].content
   limit: do 120 znaków
   EN: Will you continue exploration?
   PL: Kontynuować wyprawę?
463. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_select_character] — tekst] 수감자 선택
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_select_character].content
   limit: do 120 znaków
   EN: Select Sinner
   PL: Wybierz Grzesznika
464. [Tryby lochów i Kolei Refrakcji [mirrordungeonui_able_to_equip] — tekst] 장착 가능
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeonui_able_to_equip].content
   limit: do 120 znaków
   EN: Can Equip
   PL: Można wyposażyć
465. [Tryby lochów i Kolei Refrakcji [mirrordungeon_success_to_levelup] — tekst] 인격 단계 상승!
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_success_to_levelup].content
   limit: do 120 znaków
   EN: Identity Powered Up!
   PL: Wzrost poziomu Tożsamości!
466. [Tryby lochów i Kolei Refrakcji [mirrordungeon_additional_exp] — tekst] 금일 패스 경험치 추가 보상
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_additional_exp].content
   limit: do 120 znaków
   EN: Daily Pass EXP Bonus
   PL: Dzienna premia PD Przepustki
467. [Tryby lochów i Kolei Refrakcji [mirrordungeon_already_in_member] — tekst] 출전 중
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_already_in_member].content
   limit: do 120 znaków
   EN: On Team
   PL: W drużynie
468. [Tryby lochów i Kolei Refrakcji [mirrordungeon_select_start_character] — tekst] 거울 세계 진입
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_select_start_character].content
   limit: do 120 znaków
   EN: Enter Mirror World
   PL: Wejdź do Świata Lustrzanego
469. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_ego_gift_popup] — tekst] E.G.O 기프트를 획득하였습니다!
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_acquire_ego_gift_popup].content
   limit: do 120 znaków
   EN: E.G.O Gift GET!
   PL: Zdobyto Dar E.G.O!
470. [Tryby lochów i Kolei Refrakcji [mirrordungeon_additional_exp_weekly] — tekst] 금주 패스 경험치 추가 보상
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_additional_exp_weekly].content
   limit: do 120 znaków
   EN: Weekly Pass EXP Bonus
   PL: Tygodniowa premia PD Przepustki
471. [Tryby lochów i Kolei Refrakcji [mirrordungeon_daily_free] — tekst] 일일 1회 무료
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_daily_free].content
   limit: do 120 znaków
   EN: Daily Free Entry
   PL: 1 raz dziennie za darmo
472. [Tryby lochów i Kolei Refrakcji [mirrordungeon_entrance_quit_former_simulation] — tekst] 기존 시뮬레이션을 그만 두시겠습니까?
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_entrance_quit_former_simulation].content
   limit: do 120 znaków
   EN: Terminate the ongoing simulation?
   PL: Zakończyć bieżącą symulację?
473. [Tryby lochów i Kolei Refrakcji [mirrordungeon_progress_rate_simulation] — tekst] {0} 시뮬레이션 진행도
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_progress_rate_simulation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Simulation Progress
   PL: Postęp symulacji: {0}
474. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resume_simulation] — tekst] 시뮬레이션 재개
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_resume_simulation].content
   limit: do 120 znaków
   EN: Resume Simulation
   PL: Wznów symulację
475. [Tryby lochów i Kolei Refrakcji [mirrordungeon_stop_simulation] — tekst] 시뮬레이션 중단
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_stop_simulation].content
   limit: do 120 znaków
   EN: Halt Simulation
   PL: Przerwij symulację
476. [Tryby lochów i Kolei Refrakcji [mirrordungeon_simulation_info_1] — tekst] ◆ 소비 엔케팔린 없음
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_simulation_info_1].content
   limit: do 120 znaków
   EN: ◆ No Enkephalin Cost
   PL: ◆ Brak kosztu Enkefaliny
477. [Tryby lochów i Kolei Refrakcji [mirrordungeon_simulation_info_2] — tekst] ◆ 획득 보상 없음
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_simulation_info_2].content
   limit: do 120 znaków
   EN: ◆ No Rewards
   PL: ◆ Brak nagród
478. [Tryby lochów i Kolei Refrakcji [mirrordungeon_progress] — tekst] 탐사 재개
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_progress].content
   limit: do 120 znaków
   EN: Resume
   PL: Wznów wyprawę
479. [Tryby lochów i Kolei Refrakcji [mirrordungeon_stop] — tekst] 탐사 중단
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_stop].content
   limit: do 120 znaków
   EN: Halt Exploration
   PL: Przerwij wyprawę
480. [Tryby lochów i Kolei Refrakcji [mirrordungeon_dungeon_name_simulation] — tekst] {0} 시뮬레이션
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_dungeon_name_simulation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Simulation
   PL: Symulacja: {0}
481. [Tryby lochów i Kolei Refrakcji [mirrordungeon_warning_not_equip_ego] — tekst] E.G.O를 장착하지 않았습니다.\n이대로 진행하시겠습니까?
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_warning_not_equip_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: E.G.O not equipped.\nAre you sure you wish to proceed?
   PL: Nie wyposażono E.G.O.\nCzy mimo to kontynuować?
482. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards] — tekst] 보상 수령
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_acquire_rewards].content
   limit: do 120 znaków
   EN: Claim Rewards
   PL: Odbierz nagrody
483. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ask_select_character_level_up] — tekst] 성장 인격 선택 가능 횟수
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_ask_select_character_level_up].content
   limit: do 120 znaków
   EN: Enhancements Used
   PL: Pozostałe wybory rozwoju Tożsamości
484. [Tryby lochów i Kolei Refrakcji [mirrordungeon_simulation_info_no_use_module] — tekst] ◆ 엔케팔린 모듈 소비하지 않음
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_simulation_info_no_use_module].content
   limit: do 120 znaków
   EN: ◆ No Enkephalin Module Cost
   PL: ◆ Nie zużywa Modułów Enkefaliny
485. [Tryby lochów i Kolei Refrakcji [mirrordungeon_after_levelup] — tekst] {0} 단계 완료
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_after_levelup].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Level Up #{0}
   PL: Ukończono etap {0}
486. [Tryby lochów i Kolei Refrakcji [mirrordunge_ego_gift_history_button_label] — tekst] E.G.O 기프트 기록집
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordunge_ego_gift_history_button_label].content
   limit: do 120 znaków
   EN: E.G.O Gift Compendium
   PL: Kompendium Darów E.G.O
487. [Tryby lochów i Kolei Refrakcji [mirrordungeon_weekly_reset_description] — tekst] 주간 기록이 초기화되었습니다.\n유리창으로 이동합니다.
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_weekly_reset_description].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The weekly record has been reset.\nMoving over to the Window.
   PL: Tygodniowy zapis został zresetowany.\nPrzejście do Okna.
488. [Tryby lochów i Kolei Refrakcji [mirrordungeon_simulation_on] — tekst] ! 시뮬레이션 중
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_simulation_on].content
   limit: do 120 znaków
   EN: ! Simulating… !
   PL: ! Symulacja w toku !
489. [Tryby lochów i Kolei Refrakcji [mirrordungeon_participated] — tekst] 참여 중
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_participated].content
   limit: do 120 znaków
   EN: Participant
   PL: Bierze udział
490. [Tryby lochów i Kolei Refrakcji [select_ego_gift] — tekst] E.G.O 기프트 선택
   źródło: MirrorDungeonUI.json :: dataList[id=select_ego_gift].content
   limit: do 120 znaków
   EN: Select E.G.O Gift
   PL: Wybierz Dar E.G.O
491. [Tryby lochów i Kolei Refrakcji [explore_dungeon_finished] — tekst] 탐사 완료
   źródło: MirrorDungeonUI.json :: dataList[id=explore_dungeon_finished].content
   limit: do 120 znaków
   EN: Exploration Complete
   PL: Wyprawa ukończona
492. [Tryby lochów i Kolei Refrakcji [participated_personality] — tekst] 참여 인격
   źródło: MirrorDungeonUI.json :: dataList[id=participated_personality].content
   limit: do 120 znaków
   EN: Identities
   PL: Użyte Tożsamości
493. [Tryby lochów i Kolei Refrakcji [dungeon_final_area] — tekst] 최종 탐사 구역
   źródło: MirrorDungeonUI.json :: dataList[id=dungeon_final_area].content
   limit: do 120 znaków
   EN: Last Reached
   PL: Ostatni osiągnięty obszar
494. [Tryby lochów i Kolei Refrakcji [total_progress_rate] — tekst] 총 진행도
   źródło: MirrorDungeonUI.json :: dataList[id=total_progress_rate].content
   limit: do 120 znaków
   EN: Total Progress
   PL: Całkowity postęp
495. [Tryby lochów i Kolei Refrakcji [mirrordungeon_weekly_reset] — tekst] 이전 플레이 기록이 만료되었습니다.\n보상을 수령하십시오.
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordungeon_weekly_reset].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The previous session has expired.\nPlease claim your rewards.
   PL: Poprzedni zapis rozgrywki wygasł.\nOdbierz nagrody.
496. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_error_desc] — tekst] 서버 오류로 인하여 데이터가 손실되었습니다.
   źródło: MirrorDungeonUI.json :: dataList[id=mirror_dungeon_error_desc].content
   limit: do 120 znaków
   EN: Data was lost due to a server error.
   PL: Dane zostały utracone z powodu błędu serwera.
497. [Tryby lochów i Kolei Refrakcji [mirrordunge_achievement_history_button_label] — tekst] 거울 투영 / 업적
   źródło: MirrorDungeonUI.json :: dataList[id=mirrordunge_achievement_history_button_label].content
   limit: do 120 znaków
   EN: Mirror Projection / Achievements
   PL: Projekcja Lustra / Osiągnięcia

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_2
- plik gry: `MirrorDungeonUI_2.json`

498. [Tryby lochów i Kolei Refrakcji [mirrordungeon_product_list] — tekst] 상품 목록
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_product_list].content
   limit: do 120 znaków
   EN: Product Catalogue
   PL: Katalog towarów
499. [Tryby lochów i Kolei Refrakcji [ego_gift_list] — tekst] 보유 E.G.O 기프트
   źródło: MirrorDungeonUI_2.json :: dataList[id=ego_gift_list].content
   limit: do 120 znaków
   EN: E.G.O Gifts Owned
   PL: Posiadane Dary E.G.O
500. [Tryby lochów i Kolei Refrakcji [normal_difficulty] — tekst] 일반 난이도
   źródło: MirrorDungeonUI_2.json :: dataList[id=normal_difficulty].content
   limit: do 120 znaków
   EN: Normal
   PL: Normalny
501. [Tryby lochów i Kolei Refrakcji [hard_difficulty] — tekst] 어려움 난이도
   źródło: MirrorDungeonUI_2.json :: dataList[id=hard_difficulty].content
   limit: do 120 znaków
   EN: Hard
   PL: Trudny
502. [Tryby lochów i Kolei Refrakcji [start_buffs] — tekst] 적용 효과 목록
   źródło: MirrorDungeonUI_2.json :: dataList[id=start_buffs].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
503. [Tryby lochów i Kolei Refrakcji [enter_normal_difficulty] — tekst] 일반 난이도 입장
   źródło: MirrorDungeonUI_2.json :: dataList[id=enter_normal_difficulty].content
   limit: do 120 znaków
   EN: Enter Normal Dungeon
   PL: Wejdź (Normalny)
504. [Tryby lochów i Kolei Refrakcji [enter_hard_difficulty] — tekst] 어려움 난이도 입장
   źródło: MirrorDungeonUI_2.json :: dataList[id=enter_hard_difficulty].content
   limit: do 120 znaków
   EN: Enter Hard Dungeon
   PL: Wejdź (Trudny)
505. [Tryby lochów i Kolei Refrakcji [list_of_applied_effects] — tekst] 적용 효과 목록
   źródło: MirrorDungeonUI_2.json :: dataList[id=list_of_applied_effects].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Tryby lochów i Kolei Refrakcji [activation_complete] — tekst] 활성화 완료
   źródło: MirrorDungeonUI_2.json :: dataList[id=activation_complete].content
   limit: do 120 znaków
   EN: Activated
   PL: Aktywowano
507. [Tryby lochów i Kolei Refrakcji [lack_of_points] — tekst] 별빛이 부족합니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=lack_of_points].content
   limit: do 120 znaków
   EN: Not enough Starlight.
   PL: Za mało Gwiezdnego Blasku.
508. [Tryby lochów i Kolei Refrakcji [require_to_activate_former_buffs] — tekst] 이전 단계 버프를\n별새김해야 합니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=require_to_activate_former_buffs].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Engrave Stars on the previous\nstage's Starter Buffs first.
   PL: Najpierw wyryj gwiazdy\npoprzedniego etapu wzmocnień.
509. [Tryby lochów i Kolei Refrakcji [weekly_bonus_reward] — tekst] 주간 추가 보상
   źródło: MirrorDungeonUI_2.json :: dataList[id=weekly_bonus_reward].content
   limit: do 120 znaków
   EN: Weekly Bonuses
   PL: Cotygodniowa Premia
510. [Tryby lochów i Kolei Refrakcji [hard_dungeon_reward] — tekst] 어려움 난이도 보상
   źródło: MirrorDungeonUI_2.json :: dataList[id=hard_dungeon_reward].content
   limit: do 120 znaków
   EN: Hard Rewards
   PL: Nagrody poz. Trudnego
511. [Tryby lochów i Kolei Refrakcji [dungeon_shop_return_title] — tekst] 구매하지 않는다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_return_title].content
   limit: do 120 znaków
   EN: Don't purchase.
   PL: Nie kupuj.
512. [Tryby lochów i Kolei Refrakcji [dungeon_shop_return_desc] — tekst] 상점 화면으로 이동
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_return_desc].content
   limit: do 120 znaków
   EN: Move to Shop
   PL: Wróć do Sklepu
513. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_title_one] — tekst] 값비싼 자양강장제를 선택한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_heal_title_one].content
   limit: do 120 znaków
   EN: Choose the expensive tonic.
   PL: Wybierz drogi tonik wzmacniający.
514. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_desc_one_hp_perc_mp_int] — tekst] 선택한 수감자 체력 {0}%, 정신력 {1} 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_heal_desc_one_hp_perc_mp_int].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: The selected Sinner heals {0}% HP and {1} SP
   PL: Wybrany Grzesznik odzyskuje {0}% PŻ i {1} SP
515. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_title_all] — tekst] 에너지 드링크를 선택한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_heal_title_all].content
   limit: do 120 znaków
   EN: Choose the energy drinks.
   PL: Wybierz napoje energetyczne.
516. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_desc_all_hp_perc_mp_int] — tekst] 모든 수감자 체력 {0}%, 정신력 {1} 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_heal_desc_all_hp_perc_mp_int].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: All Sinners heal {0}% HP and {1} SP
   PL: Wszyscy Grzesznicy odzyskują {0}% PŻ i {1} SP
517. [Tryby lochów i Kolei Refrakcji [dungeon_shop_purchase_title] — tekst] 구매한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_purchase_title].content
   limit: do 120 znaków
   EN: Purchase.
   PL: Kup.
518. [Tryby lochów i Kolei Refrakcji [dungeon_shop_change_formation_title] — tekst] 부스러기 안에 보이는 거울 조각을 집어든다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_change_formation_title].content
   limit: do 120 znaków
   EN: Pick up a mirror shard amid the crumbs.
   PL: Podnieś odłamek lustra spomiędzy okruchów.
519. [Tryby lochów i Kolei Refrakcji [dungeon_shop_change_formation_desc] — tekst] 현재 편성에 새로운 인격 또는 E.G.O를 추가
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_change_formation_desc].content
   limit: do 120 znaków
   EN: Add a new Identity or E.G.O to the current team
   PL: Dodaj nową Tożsamość lub E.G.O do bieżącego składu
520. [Tryby lochów i Kolei Refrakcji [dungeon_shop_heal_character] — tekst] 수감자 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_heal_character].content
   limit: do 120 znaków
   EN: Heal Sinner
   PL: Ulecz Grzesznika
521. [Tryby lochów i Kolei Refrakcji [dungeon_shop_change_formation] — tekst] 편성
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_change_formation].content
   limit: do 120 znaków
   EN: Team
   PL: Skład
522. [Tryby lochów i Kolei Refrakcji [dungeon_shop_upgrade_personality] — tekst] {0} 스킬 교체
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_upgrade_personality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace {0}'s Skill
   PL: Wymień umiejętność: {0}
523. [Tryby lochów i Kolei Refrakcji [dungeon_shop_upgrade_personality_0_title] — tekst] 적당한 비용을 치룬다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_upgrade_personality_0_title].content
   limit: do 120 znaków
   EN: Pay a moderate price.
   PL: Zapłać umiarkowaną cenę.
524. [Tryby lochów i Kolei Refrakcji [dungeon_shop_upgrade_personality_1_title] — tekst] 큰 값을 치룬다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_upgrade_personality_1_title].content
   limit: do 120 znaków
   EN: Pay a large sum.
   PL: Zapłać wysoką cenę.
525. [Tryby lochów i Kolei Refrakcji [dungeon_shop_upgrade_personality_2_title] — tekst] 어마어마한 값을 치룬다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_upgrade_personality_2_title].content
   limit: do 120 znaków
   EN: Pay a tremendous price.
   PL: Zapłać astronomiczną cenę.
526. [Tryby lochów i Kolei Refrakcji [dungeon_shop_upgrade_personality_desc] — tekst] 해당 인격이 보유한 [스킬 {2} - {0}] 중 하나를 [스킬 {3} - {1}]으로 변경
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_upgrade_personality_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {2}, {0}, {3}, {1}
   EN: Change one of the Identity's [skills {2} - {0}] to a [skill {3} - {1}]
   PL: Zmień jedną z posiadanych przez Tożsamość [umiejętności {2} — {0}] na [umiejętność {3} — {1}]
527. [Tryby lochów i Kolei Refrakcji [dungeon_shop_out] — tekst] 나가기
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_shop_out].content
   limit: do 120 znaków
   EN: Leave
   PL: Wyjdź
528. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_hard_open_at] — tekst] 거울의 거울 보통 난이도 클리어 시 개방
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_hard_open_at].content
   limit: do 120 znaków
   EN: Clear Mirror of Mirrors on Normal to unlock
   PL: Odblokowanie po ukończeniu Lustra Luster (Normalny)
529. [Tryby lochów i Kolei Refrakcji [mirrordungeon_with_number] — tekst] 거울 던전 {0}
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_with_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mirror Dungeon {0}
   PL: Lustrzany Loch {0}
530. [Tryby lochów i Kolei Refrakcji [mirrordungeon_select_buffs_title] — tekst] 선택지 효과 선택
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_select_buffs_title].content
   limit: do 120 znaków
   EN: Select Event Effect
   PL: Wybierz efekt wydarzenia
531. [Tryby lochów i Kolei Refrakcji [acquire_additional_rewards] — tekst] 추가 보상 받기
   źródło: MirrorDungeonUI_2.json :: dataList[id=acquire_additional_rewards].content
   limit: do 120 znaków
   EN: Receive additional rewards
   PL: Odbierz dodatkowe nagrody
532. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_using_chance_desc] — tekst] 「주간 추가 보상」 기회를 소모하여 보너스 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_using_chance_desc].content
   limit: do 120 znaków
   EN: Spend your 「Weekly Bonuses」 to claim the bonus rewards?
   PL: Zużyć szansę na 「Cotygodniową Premię」, aby odebrać dodatkowe nagrody?
533. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_not_using_chance_desc] — tekst] 「주간 추가 보상」 기회가 남아있습니다. "주간 추가 보상" 기회를 사용하지 않고 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_not_using_chance_desc].content
   limit: do 170 znaków
   EN: You have Weekly Bonus Eligibility remaining. Are you sure you want to claim the current rewards without using the Eligibility?
   PL: Masz niewykorzystaną szansę na 「Cotygodniową Premię」. Czy na pewno chcesz odebrać nagrody bez jej użycia?
534. [Tryby lochów i Kolei Refrakcji [mirrordungeon_acquire_rewards_no_chance_desc] — tekst] 보상을 수령하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_acquire_rewards_no_chance_desc].content
   limit: do 120 znaków
   EN: Claim the rewards?
   PL: Odebrać nagrody?
535. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buffs_chip_name] — tekst] 별빛
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_start_buffs_chip_name].content
   limit: do 120 znaków
   EN: Starlight
   PL: Gwiezdny Blask
536. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_exit_without_acquire_rewards] — tekst] 보상을 수령하지 않고 탐사를 종료하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_exit_without_acquire_rewards].content
   limit: do 120 znaków
   EN: End expedition without claiming rewards?
   PL: Zakończyć wyprawę bez odbierania nagród?
537. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_1] — tekst] 반걸음 더
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_1].content
   limit: do 120 znaków
   EN: Half a Step More
   PL: Pół Kroku Dalej
538. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_2] — tekst] 투지
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_2].content
   limit: do 120 znaków
   EN: Fighting Spirit
   PL: Duch Walki
539. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_3] — tekst] 약점 파악
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_3].content
   limit: do 120 znaków
   EN: Spotting Vulnerabilities
   PL: Wypatrzenie Słabości
540. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_4] — tekst] 나아갈 투지
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_4].content
   limit: do 120 znaków
   EN: Spirit to Push Ahead
   PL: Wola Parcia Naprzód
541. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_5] — tekst] 약점 집중
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_5].content
   limit: do 120 znaków
   EN: Focusing Vulnerabilities
   PL: Skupienie na Słabościach
542. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_6] — tekst] 체력 단련
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_6].content
   limit: do 120 znaków
   EN: Physical Training
   PL: Trening Wytrzymałościowy
543. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_7] — tekst] 엿보이는 간절함
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_7].content
   limit: do 120 znaków
   EN: Glimpse of Earnestness
   PL: Przebłysk Żarliwości
544. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_8] — tekst] 고강도 체력 단련
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_8].content
   limit: do 120 znaków
   EN: Intense Training
   PL: Intensywny Trening Wytrzymałościowy
545. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_9] — tekst] 자생
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_9].content
   limit: do 120 znaków
   EN: Autogenic
   PL: Samoregeneracja
546. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_10] — tekst] 맞물린 가능성
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_10].content
   limit: do 120 znaków
   EN: Meshed Possibilities
   PL: Zazębione Możliwości
547. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_11] — tekst] 단 하나의 주머니
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_11].content
   limit: do 120 znaków
   EN: Just One Pocket
   PL: Tylko Jedna Kieszeń
548. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_12] — tekst] 한걸음 더
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_12].content
   limit: do 120 znaków
   EN: One Step Further
   PL: Jeden Krok Dalej
549. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_13] — tekst] 우연한 습득물
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_13].content
   limit: do 120 znaków
   EN: Fortuitous Find
   PL: Szczęśliwe Znalezisko
550. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_14] — tekst] 돋보이는 주머니
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_14].content
   limit: do 120 znaków
   EN: Distinct Pocket
   PL: Wyróżniająca się Kieszeń
551. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_15] — tekst] 견고한 수비
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_15].content
   limit: do 120 znaków
   EN: Solid Defense
   PL: Solidna Obrona
552. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_16] — tekst] 재빠른 다리
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_16].content
   limit: do 120 znaków
   EN: Quick Legs
   PL: Zwinne Nogi
553. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_17] — tekst] 준족
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_17].content
   limit: do 120 znaków
   EN: Fleet-footed
   PL: Chyżonogi
554. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_18] — tekst] 스쳐가는 공격
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_18].content
   limit: do 120 znaków
   EN: Grazing Attack
   PL: Draśnięcie
555. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_buffs_title_19] — tekst] 굳센 정신
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_buffs_title_19].content
   limit: do 120 znaków
   EN: Stalwart Spirit
   PL: Niezłomny Duch
556. [Tryby lochów i Kolei Refrakcji [mirrordungeon_unable_to_purchase_buffs_when_running_dungeon] — tekst] 던전 진행 중에는 시작 버프를 구매할 수 없습니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_unable_to_purchase_buffs_when_running_dungeon].content
   limit: do 120 znaków
   EN: You may not purchase starter buffs while an expedition is in progress.
   PL: Nie można kupować wzmocnień początkowych podczas trwającej wyprawy.
557. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_open] — tekst] 부디 편히 쉬었다 가시길!\n\n혹여 원하는 게 만남이라면, 책상 위에 그것을 올려주세요.\n\n- 자판기를 찾아 미로를 여행하는 편의점 주인 올림
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_open].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Feel free to take a rest here!\n\nIf you'd like a chance meeting, please place that on the desk.\n\n- Convenience store owner exploring the maze for a dispenser
   PL: Odpocznijcie tu wygodnie!\n\nA jeśli pragniecie spotkania, połóżcie to na biurku.\n\n— Właściciel sklepiku wędrujący przez labirynt w poszukiwaniu automatu
558. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_open] — tekst] 자판기에서 흘러나오는 진동음이 공간을 가득 메운다.\n\n그것은 우리가 무엇을 원하는지 알고 있다.\n\n우리 역시 그게 원하는 것이 무엇인지를 알고 있다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_open].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The dispenser's hum fills the air.\n\nIt knows what we want.\n\nWe also know what it wants.
   PL: Buczenie automatu wypełnia całą przestrzeń.\n\nOn wie, czego pragniemy.\n\nA my wiemy, czego on pragnie od nas.
559. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_title] — tekst] 편히 쉰다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_title].content
   limit: do 120 znaków
   EN: Take a rest.
   PL: Odpocznij.
560. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_desc] — tekst] 수감자 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_desc].content
   limit: do 120 znaków
   EN: Sinners heal HP
   PL: Uleczenie Grzeszników
561. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_desc_1] — tekst] 선택한 수감자 체력 {0}% 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_desc_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The selected Sinner heals {0}% HP
   PL: Wybrany Grzesznik odzyskuje {0}% PŻ
562. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_desc_2] — tekst] 모든 수감자 체력 {0}% 회복
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_desc_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All Sinners heal {0}% HP
   PL: Wszyscy Grzesznicy odzyskują {0}% PŻ
563. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_change_formation_title] — tekst] 부스러기를 테이블 위에 올려둔다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_change_formation_title].content
   limit: do 120 znaków
   EN: Place the crumb on the table.
   PL: Połóż okruch na stole.
564. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_change_formation_desc] — tekst] 현재 편성에 새로운 인격 또는 E.G.O를 추가
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_change_formation_desc].content
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
565. [Tryby lochów i Kolei Refrakcji [hard_difficulty_en] — tekst] 어려움 난이도
   źródło: MirrorDungeonUI_2.json :: dataList[id=hard_difficulty_en].content
   (powtórzenie elementu 501 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
566. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_normal_open_at] — tekst] 주요이야기 4-54, 시작의 거울 클리어 시 개방
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_normal_open_at].content
   limit: do 120 znaków
   EN: Clear Main Story 4-54 and Mirror of the Beginning to unlock
   PL: Odblokowanie po ukończeniu etapu 4-54 oraz Lustra Początku
567. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_shop_stageinfo_title] — tekst] 진동음이 굵게 울리는 공간
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_shop_stageinfo_title].content
   limit: do 120 znaków
   EN: Thick Rumbling Hum
   PL: Przestrzeń Głębokiego Buczenia
568. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_shop_stageinfo_desc] — tekst] 섬뜩하리만치 텅 빈 공간이 자판기에서 흘러나오는 진동음으로 메워진다.\n\n그 목소리는 말한다. 너희가 가진 그 부스러기를 바친다면 쓸모있는 것으로 바꾸어 주겠다고.\n\n정체를 알 수 없는 그것을 향해 홀린 듯이 다가간다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_shop_stageinfo_desc].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The eerily empty space is occupied by the hum coming from the dispenser.\n\nThe voice speaks: 'Yield that crumb you have, and it'll be exchanged for something useful.'\n\nYou're drawn by the mysterious object.
   PL: Upiornie pustą przestrzeń wypełnia niskie buczenie dobiegające z automatu.\n\nGłos przemawia: „Oddajcie posiadany okruch, a wymienię go na coś pożytecznego”.\n\nJak urzeczony podchodzisz do tajemniczej maszyny.
569. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_resting_stageinfo_title] — tekst] 고요함이 짙게 드리운 공간
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_resting_stageinfo_title].content
   limit: do 120 znaków
   EN: Dense Quietness
   PL: Przestrzeń Gęstej Ciszy
570. [Tryby lochów i Kolei Refrakcji [mirrordungeon_2_resting_stageinfo_desc] — tekst] 고요함에 고통을 묻어두거나,\n그 속에서 고통을 함께할 자를 꺼내어보자.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_2_resting_stageinfo_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You may bury your pain in the quiet,\nor bring out someone to share the pain with.
   PL: Pogrzeb swój ból w ciszy\nlub przywołaj kogoś, kto pomoże ci go dźwigać.
571. [Tryby lochów i Kolei Refrakcji [dungeon_resting_change_formation_title] — tekst] 부스러기 안에 보이는 거울 조각을 집어든다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_resting_change_formation_title].content
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Tryby lochów i Kolei Refrakcji [dungeon_resting_change_formation_desc] — tekst] 현재 편성에 새로운 인격 또는 E.G.O를 추가
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_resting_change_formation_desc].content
   (powtórzenie elementu 519 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Tryby lochów i Kolei Refrakcji [dungeon_resting_heal_title_one] — tekst] 제일 피곤해보이는 수감자를 의자에 눕힌다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_resting_heal_title_one].content
   limit: do 120 znaków
   EN: Place the most tired Sinner in the chair.
   PL: Połóż na krześle najbardziej wyczerpanego Grzesznika.
574. [Tryby lochów i Kolei Refrakcji [dungeon_resting_heal_title_all] — tekst] 수감자 전원이 의자에 걸터앉아 휴식을 취한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_resting_heal_title_all].content
   limit: do 120 znaków
   EN: All Sinners take a seat to rest.
   PL: Wszyscy Grzesznicy przysiadają na krzesłach, by odpocząć.
575. [Tryby lochów i Kolei Refrakcji [ego_gift_info] — tekst] E.G.O 기프트 정보
   źródło: MirrorDungeonUI_2.json :: dataList[id=ego_gift_info].content
   limit: do 120 znaków
   EN: E.G.O Gift Info
   PL: Informacje o Darze E.G.O
576. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_gift_entrance] — tekst] 기이하고 신비로운 것에 자꾸만 시선이 간다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_gift_entrance].content
   limit: do 120 znaków
   EN: The bizarre and curious things draw your attention.
   PL: Wzrok raz po raz przyciągają osobliwe i tajemnicze przedmioty.
577. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_gift_purchase] — tekst] 철컹거리며 무언가가 떨어지는 소리가 들린다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_gift_purchase].content
   limit: do 120 znaków
   EN: You hear something drop with a clang.
   PL: Słychać metaliczny szczęk wypadającego przedmiotu.
578. [Tryby lochów i Kolei Refrakcji [mirrordungeon_reenter] — tekst] 더 살 게 있을까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_reenter].content
   limit: do 120 znaków
   EN: Anything else to buy?
   PL: Kupić coś jeszcze?
579. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_one_who] — tekst] 안타깝게도 이 귀한 피로회복제는 하나 뿐이다.\n누가 마시는 게 좋을까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_heal_one_who].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unfortunately, there's only one of this precious restorative drink.\nWho should drink it?
   PL: Niestety ten cenny napój regenerujący jest tylko jeden.\nKto powinien go wypić?
580. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_one_answer] — tekst] 비싼 물건은 그 값을 하나보다.\n자양강장제를 맛본 수감자의 얼굴에는 피로는 커녕 광채가 어른거린다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_heal_one_answer].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It looks like the item was well worth the price.\nAfter drinking the tonic, the Sinner is almost glowing with vigor.
   PL: Drogi specyfik był wart swojej ceny.\nNa twarzy Grzesznika po wypiciu toniku zamiast zmęczenia maluje się blask wigoru.
581. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_all_answer] — tekst] 수감자 수만큼 에너지 드링크를 뽑았다.\n달고 시큼한 것을 맛보며, 모두의 얼굴에 이제야 피로가 좀 풀리는 모습이다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_heal_all_answer].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You bought energy drinks for every Sinner.\nTasting the sweet and sour liquid, fatigue seems to be leaving the Sinners' faces.
   PL: Wybrano z automatu napoje energetyczne dla wszystkich Grzeszników.\nSłodko-kwaśny łyk wyraźnie zdejmuje zmęczenie z ich twarzy.
582. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_one_answer] — tekst] 잠시 누워 눈을 붙이도록 했다.\n휴식 시간이 끝날 무렵에 다시 보니 다행히 기운을 차린 듯한 모습이다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_one_answer].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I had the Sinner take a light nap.\nThankfully, the Sinner seems to have recovered their strength when I looked at them by the end of the break.
   PL: Pozwoliłem Grzesznikowi położyć się na krótką drzemkę.\nNa szczęście pod koniec przerwy wyglądał już na znacznie pokrzepionego.
583. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_all_answer] — tekst] 모두 앉으려니 조금 비좁기는 했지만,\n모처럼 단비 같은 휴식이었다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_all_answer].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It was a bit cramped for everyone to sit,\nBut the rest was blissful to have nonetheless.
   PL: Trochę ciasno było usiąść wszystkim naraz,\nale chwila wytchnienia okazała się zbawienna.
584. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_one_after] — tekst] 모두 앉으려니 조금 비좁기는 했지만,\n모처럼 단비 같은 휴식이었다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_heal_one_after].content
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_heal_one_who_right] — tekst] 피곤해 보이는 수감자를 선택한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_heal_one_who_right].content
   limit: do 120 znaków
   EN: Choose the Sinner that looks tired.
   PL: Wybierz zmęczonego Grzesznika.
586. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_upgrade_start_left] — tekst] 이 자판기 안에는 무한한 가능성이라는 개념이 실재하는 것일까.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_shop_upgrade_start_left].content
   limit: do 120 znaków
   EN: Could infinite possibilities really reside within this dispenser?
   PL: Czy wewnątrz tego automatu naprawdę kryją się nieskończone możliwości?
587. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_mirror_shop] — tekst] 상점
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_encounter_guide_mirror_shop].content
   limit: do 120 znaków
   EN: Shop
   PL: Sklep
588. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_mirror_select_event] — tekst] 쉼터
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_encounter_guide_mirror_select_event].content
   limit: do 120 znaków
   EN: Rest Stop
   PL: Przystanek Odpoczynku
589. [Tryby lochów i Kolei Refrakcji [dungeon_explore_floor] — tekst] {0}층 탐사 중
   źródło: MirrorDungeonUI_2.json :: dataList[id=dungeon_explore_floor].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Exploring Floor {0}
   PL: Eksploracja {0}. piętra
590. [Tryby lochów i Kolei Refrakcji [lack_of_point_for_shop] — tekst] 코스트 부족
   źródło: MirrorDungeonUI_2.json :: dataList[id=lack_of_point_for_shop].content
   limit: do 120 znaków
   EN: Not Enough Cost
   PL: Za mało Kosztu
591. [Tryby lochów i Kolei Refrakcji [mirrordungeon_select_less_character_at_start] — tekst] 선택가능한 수감자 수보다 적게 편성되었습니다.\n이대로 진행하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_select_less_character_at_start].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You've deployed fewer Sinners than your max for the team.\nAre you sure you want to proceed?
   PL: Wybrano mniej Grzeszników niż wynosi limit składu.\nCzy mimo to kontynuować?
592. [Tryby lochów i Kolei Refrakcji [list_of_applied_effects_is_empty] — tekst] 현재 적용된 효과가 없습니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=list_of_applied_effects_is_empty].content
   limit: do 120 znaków
   EN: No effects active.
   PL: Brak aktywnych efektów.
593. [Tryby lochów i Kolei Refrakcji [give_up_rewards] — tekst] 수령 포기
   źródło: MirrorDungeonUI_2.json :: dataList[id=give_up_rewards].content
   limit: do 120 znaków
   EN: Give Up Rewards
   PL: Zrezygnuj z nagród
594. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_rewards_back_to_lobby_button] — tekst] 유리창으로 이동
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_rewards_back_to_lobby_button].content
   limit: do 120 znaków
   EN: To Window
   PL: Do Okna
595. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_rewards_back_to_lobby_desc] — tekst] 유리창으로 이동하시겠습니까?\n탐사 종료 보상 창은 이후 거울 던전에 다시 입장할 때 재등장합니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_rewards_back_to_lobby_desc].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Would you like to move to the Window?\nThe expedition rewards popup will reappear when you return to the Mirror Dungeons menu.
   PL: Przejść do Okna?\nOkno odbioru nagród za wyprawę pojawi się ponownie przy kolejnym wejściu do Lustrzanych Lochów.
596. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_rewards_back_to_lobby_button_lobby] — tekst] 목록으로 이동
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_rewards_back_to_lobby_button_lobby].content
   limit: do 120 znaków
   EN: To List
   PL: Do listy
597. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_one_who] — tekst] 자리가 그다지 넓진 않다.\n누구를 쉬게 하는 게 좋을까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_one_who].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The space isn't all that wide.\nWho should take the rest?
   PL: Miejsca nie ma tu zbyt wiele.\nKomu pozwolić odpocząć?
598. [Tryby lochów i Kolei Refrakcji [mirrordungeon_resting_heal_one_who_right] — tekst] 피곤해 보이는 수감자를 선택한다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_resting_heal_one_who_right].content
   (powtórzenie elementu 585 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_change_formation_release_character] — tekst] 선택 항목 일괄 취소
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_change_formation_release_character].content
   limit: do 120 znaków
   EN: Cancel All Selected
   PL: Odznacz wszystko
600. [Tryby lochów i Kolei Refrakcji [mirrordungeon_exit_shop] — tekst] 상점에서 나가시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_exit_shop].content
   limit: do 120 znaków
   EN: Leave the shop?
   PL: Opuścić Sklep?
601. [Tryby lochów i Kolei Refrakcji [mirrordungeon_exit_resting] — tekst] 쉼터에서 나가시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_exit_resting].content
   limit: do 120 znaków
   EN: Leave the rest stop?
   PL: Opuścić Przystanek Odpoczynku?
602. [Tryby lochów i Kolei Refrakcji [mirrordungeon_change_formation_confirm_less_participants] — tekst] 선택 횟수가 남았습니다.\n이대로 편성하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_change_formation_confirm_less_participants].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You have selections remaining.\nAre you sure you want to finish the setup?
   PL: Pozostały jeszcze niewykorzystane wybory.\nZatwierdzić taki skład?
603. [Tryby lochów i Kolei Refrakcji [mirrordungeon_change_formation_confirm_exact_participants] — tekst] 코스트를 사용하여 선택한 인격과 E.G.O를 편성하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirrordungeon_change_formation_confirm_exact_participants].content
   limit: do 120 znaków
   EN: Spend the Cost to deploy the selected Identities and E.G.O?
   PL: Wydać Koszt, aby dodać wybrane Tożsamości i E.G.O do składu?
604. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_clear_battle_reward_label] — tekst] 클리어 보상
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_clear_battle_reward_label].content
   limit: do 120 znaków
   EN: Clear Rewards
   PL: Nagrody za ukończenie
605. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_change_formation_but_button] — tekst] 구매
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_start_change_formation_but_button].content
   limit: do 120 znaków
   EN: Buy
   PL: Kup
606. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_give_up_ego_gift] — tekst] 선택하지 않음
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_give_up_ego_gift].content
   limit: do 120 znaków
   EN: Refuse Gift
   PL: Pomiń wybór
607. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_give_up_ego_gift_ask] — tekst] E.G.O 기프트를 선택하지 않고 진행하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_give_up_ego_gift_ask].content
   limit: do 120 znaków
   EN: Continue without choosing an E.G.O Gift?
   PL: Kontynuować bez wyboru Daru E.G.O?
608. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_challenge_mode_description] — tekst] 도전 모드를 활성화할 경우, 무작위 편성이 진행됩니다.\n조합된 편성은 해당 편성으로 보상을 수령하기 전까지 변경되지 않습니다.\n도전 모드 상태로 클리어 시, 보상이 증가합니다.
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_challenge_mode_description].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: While Challenge Mode is active, the team will be set up randomly.\nThe setup will not change until you have claimed rewards for an expedition with the team.\nYou can receive more rewards in Challenge Mode clears.
   PL: Po włączeniu Trybu Wyzwania skład drużyny zostanie wylosowany.\nWylosowany skład nie zmieni się aż do odebrania nim nagród za wyprawę.\nUkończenie w Trybie Wyzwania zwiększa nagrody.
609. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_challenge_mode_ask] — tekst] 도전 모드를 활성화하시겠습니까?
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_challenge_mode_ask].content
   limit: do 120 znaków
   EN: Activate Challenge Mode?
   PL: Włączyć Tryb Wyzwania?
610. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_challenge_mode] — tekst] 도전 모드
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_challenge_mode].content
   limit: do 120 znaków
   EN: Challenge Mode
   PL: Tryb Wyzwania
611. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_require_condition_title] — tekst] 권장 조건
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_hard_require_condition_title].content
   limit: do 120 znaków
   EN: Recommendations
   PL: Zalecane warunki
612. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hard_require_condition_level] — tekst] - 인격 레벨 45
   źródło: MirrorDungeonUI_2.json :: dataList[id=mirror_dungeon_hard_require_condition_level].content
   limit: do 120 znaków
   EN: - Identity Levels 45
   PL: - Poziom Tożsamości: 45
