# Paczka AI P41 (Fala 2 · 2C) — Tabela modeli postaci oraz interfejs, zadania i przedmioty RPG Canto X (część 3/4)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P41_2c_modele_i_rpg_ui_cz03.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P41_2c_modele_i_rpg_ui_cz03.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryb RPG [common] — rpg-loc-ui-common-a1c10p1
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-ui-common-a1c10p1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

1. [RPG [Setting_Sisyphus_VirtualPadWalkStart] — tekst] 걷기 시작 반경
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadWalkStart].text
   limit: do 120 znaków
   EN: V. Joystick Walk Threshold
   PL: Próg rozpoczęcia chodu
2. [RPG [Setting_Sisyphus_VirtualPadRunKeep] — tekst] 달리기 유지 반경
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadRunKeep].text
   limit: do 120 znaków
   EN: V. Joystick Maintain Sprint Radius
   PL: Promień utrzymania biegu
3. [RPG [Setting_Sisyphus_VirtualPadRunStart] — tekst] 달리기 시작 반경
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadRunStart].text
   limit: do 120 znaków
   EN: V. Joystic Sprint Threshold
   PL: Próg rozpoczęcia biegu
4. [RPG [Setting_Sisyphus_TurnAssist] — tekst] 이동 중 방향 전환 보조
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_TurnAssist].text
   limit: do 120 znaków
   EN: Directional Change Threshold Adjustment
   PL: Asysta skrętu w ruchu
5. [RPG [Setting_Sisyphus_VirtualPadMode] — tekst] 가상 패드 방식
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadMode].text
   limit: do 120 znaków
   EN: Virtual Pad
   PL: Tryb wirtualnego pada
6. [RPG [Setting_Sisyphus_VirtualPadModeFixed] — tekst] 고정형
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadModeFixed].text
   limit: do 120 znaków
   EN: Fixed
   PL: Stały
7. [RPG [Setting_Sisyphus_VirtualPadModeFloating] — tekst] 이동형
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_VirtualPadModeFloating].text
   limit: do 120 znaków
   EN: Floating
   PL: Pływający
8. [RPG [Setting_Sisyphus_RunStartDelayValue] — tekst] {0}초
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_RunStartDelayValue].text
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Seconds
   PL: {0} sek.
9. [RPG [Setting_Sisyphus_Move] — tekst] 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Move].text
   limit: do 120 znaków
   EN: Move
   PL: Ruch
10. [RPG [Setting_Sisyphus_Interaction] — tekst] 상호 작용
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Interaction].text
   limit: do 120 znaków
   EN: Interact
   PL: Interakcja
11. [RPG [Setting_Sisyphus_Quest] — tekst] 저널:퀘스트
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Quest].text
   limit: do 120 znaków
   EN: Journal: Quests
   PL: Dziennik: Zadania
12. [RPG [Setting_Sisyphus_GauntletSuicide] — tekst] 샘터로 돌아가기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_GauntletSuicide].text
   limit: do 120 znaków
   EN: Return to the Fount
   PL: Powrót do Źródła
13. [RPG [Setting_Sisyphus_Attack] — tekst] 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Attack].text
   limit: do 120 znaków
   EN: Attack
   PL: Atak
14. [RPG [Setting_Sisyphus_Guard] — tekst] 가드
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Guard].text
   limit: do 120 znaków
   EN: Block
   PL: Blok
15. [RPG [Setting_Sisyphus_Dodge] — tekst] 회피
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Dodge].text
   limit: do 120 znaków
   EN: Evade
   PL: Unik
16. [RPG [Setting_Sisyphus_Run] — tekst] 달리기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Run].text
   limit: do 120 znaków
   EN: Sprint
   PL: Bieg
17. [RPG [Setting_Sisyphus_LockedNeedItem] — tekst] ※ 미해금, 아이템 구매 필요
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_LockedNeedItem].text
   limit: do 120 znaków
   EN: ※ Unavailable. Purchase relevant item to unlock.
   PL: ※ Zablokowane. Odblokujesz, kupując odpowiedni przedmiot.
18. [RPG [Setting_Sisyphus_LanternToggle] — tekst] 랜턴 ON/OFF
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_LanternToggle].text
   limit: do 120 znaków
   EN: Lantern ON/OFF
   PL: Lampa wł./wył.
19. [RPG [Setting_Sisyphus_CloseWindowOrSetting] — tekst] 열린 창 닫기 / 설정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_CloseWindowOrSetting].text
   limit: do 120 znaków
   EN: Close open window / Settings
   PL: Zamknij okno / Ustawienia
20. [RPG [Setting_Sisyphus_Inventory] — tekst] 인벤토리
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Inventory].text
   limit: do 120 znaków
   EN: View Inventory
   PL: Ekwipunek
21. [RPG [Setting_Sisyphus_DialogueNext] — tekst] 진행·선택지 확정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_DialogueNext].text
   limit: do 120 znaków
   EN: Proceed / Finalize dialogue choice
   PL: Kontynuuj / zatwierdź wybór dialogu
22. [RPG [Setting_Sisyphus_DialogueChoice] — tekst] 대화 중 선택지 선택
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_DialogueChoice].text
   limit: do 120 znaków
   EN: Browse dialogue choices
   PL: Przeglądaj opcje dialogu
23. [RPG [Setting_Sisyphus_DialogueSkip] — tekst] 대화 스킵
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_DialogueSkip].text
   limit: do 120 znaków
   EN: Skip dialogue
   PL: Pomiń dialog
24. [RPG [Setting_Sisyphus_FullLog] — tekst] 전체 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_FullLog].text
   limit: do 120 znaków
   EN: View Log History
   PL: Pełny dziennik
25. [RPG [Setting_Sisyphus_CreditFastForward] — tekst] 크레딧 빨리 감기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_CreditFastForward].text
   limit: do 120 znaków
   EN: Speed up credit scroll
   PL: Przewiń napisy końcowe szybciej
26. [RPG [Setting_Sisyphus_CreditSkip] — tekst] 크레딧 스킵
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_CreditSkip].text
   limit: do 120 znaków
   EN: Skip credits
   PL: Pomiń napisy końcowe
27. [RPG [Setting_Sisyphus_QuestNavigation] — tekst] 퀘스트 안내 화살표
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_QuestNavigation].text
   limit: do 120 znaków
   EN: Toggle Quest Navigation Arrow
   PL: Przełącz strzałkę naprowadzania zadania
28. [RPG [Setting_Sisyphus_TabDefault] — tekst] 단축키
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_TabDefault].text
   limit: do 120 znaków
   EN: Controls (Keyboard)
   PL: Sterowanie (klawiatura)
29. [RPG [Setting_Sisyphus_TabMobile] — tekst] 버튼
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_TabMobile].text
   limit: do 120 znaków
   EN: Controls (Mobile)
   PL: Sterowanie (dotyk)
30. [RPG [WardenBigNail] — tekst] 간수의 대못
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=WardenBigNail].text
   limit: do 120 znaków
   EN: The Warden's Greatnail
   PL: Wielki Gwóźdź Strażnika
31. [RPG [FormationUI_AskToBack] — tekst] 뒤로가기를 통해 전투 이탈 시 패배합니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=FormationUI_AskToBack].text
   limit: do 120 znaków
   EN: Leaving via the "back" button will count as defeat.
   PL: Wyjście z walki przyciskiem „wstecz” oznacza porażkę.
32. [RPG [Setting_Sisyphus_Manual] — tekst] 매뉴얼
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_Manual].text
   limit: do 120 znaków
   EN: Manual
   PL: Instrukcja
33. [RPG [Setting_Sisyphus_BattleStatus] — tekst] 그림자계 현황
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_BattleStatus].text
   limit: do 120 znaków
   EN: Status in the Shadowed
   PL: Status w Zacienionym
34. [RPG [TheaterTitle] — tekst] 상영관
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=TheaterTitle].text
   limit: do 120 znaków
   EN: Cinéma
   PL: Teatr
35. [RPG [SettingTitle] — tekst] 설정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=SettingTitle].text
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
36. [RPG [Setting_Sisyphus_MobileMenu] — tekst] 메뉴
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileMenu].text
   limit: do 120 znaków
   EN: Open Menu
   PL: Menu
37. [RPG [Setting_Sisyphus_MobileAutoAttack] — tekst] 오토 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileAutoAttack].text
   limit: do 120 znaków
   EN: Auto-attack
   PL: Atak Automatyczny
38. [RPG [Setting_Sisyphus_MobileInteraction] — tekst] 상호작용
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileInteraction].text
   limit: do 120 znaków
   EN: Interact
   PL: Interakcja
39. [RPG [Setting_Sisyphus_MobileQuestNavigation] — tekst] 화살표
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileQuestNavigation].text
   limit: do 120 znaków
   EN: Quest Nav. Arrow
   PL: Strzałka naprowadzania zadania
40. [RPG [Setting_Sisyphus_MobileLantern] — tekst] 랜턴
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileLantern].text
   limit: do 120 znaków
   EN: Lantern
   PL: Lampa
41. [RPG [Setting_Sisyphus_MobileUnlockNotice] — tekst] ※ 표시된 기능은 아이템 구매로 해금할 수 있습니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Setting_Sisyphus_MobileUnlockNotice].text
   limit: do 120 znaków
   EN: Functions marked with "※" must be unlocked by purchasing a relevant item.
   PL: Funkcje oznaczone „※” można odblokować, kupując odpowiedni przedmiot.
42. [RPG [Rpg_Menu_Status_Ego_Resources_Owned] — tekst] E.G.O 자원 현황
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Rpg_Menu_Status_Ego_Resources_Owned].text
   limit: do 120 znaków
   EN: Current E.G.O Resources
   PL: Stan zasobów E.G.O
43. [RPG [Rpg_Menu_Status_Character_Mental_Status] — tekst] 수감자 정신력 현황
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Rpg_Menu_Status_Character_Mental_Status].text
   limit: do 120 znaków
   EN: Sinner SP Status
   PL: Stan SP Grzeszników
44. [RPG [Rpg_Move_Floor_Ui_Current_Floor] — tekst] 현재 층
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p1.json :: dataList[key=Rpg_Move_Floor_Ui_Current_Floor].text
   limit: do 120 znaków
   EN: Current Floor
   PL: Obecne piętro

## Tryb RPG [common] — rpg-loc-ui-common-a1c10p2
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-ui-common-a1c10p2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

45. [RPG [ItemFilterBuffetUpgrade] — tekst] 뿌이 강화
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=ItemFilterBuffetUpgrade].text
   limit: do 120 znaków
   EN: Pwie Upgrades
   PL: Ulepszenia Pwie
46. [RPG [Setting_Tab_Key] — tekst] 키 설정
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=Setting_Tab_Key].text
   limit: do 120 znaków
   EN: Key Mapping
   PL: Mapowanie klawiszy
47. [RPG [KeyDesc_PlayerMoveUp] — tekst] 위로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerMoveUp].text
   limit: do 120 znaków
   EN: Move up
   PL: Ruch w górę
48. [RPG [KeyDesc_PlayerMoveDown] — tekst] 아래로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerMoveDown].text
   limit: do 120 znaków
   EN: Move down
   PL: Ruch w dół
49. [RPG [KeyDesc_PlayerMoveLeft] — tekst] 왼쪽으로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerMoveLeft].text
   limit: do 120 znaków
   EN: Move left
   PL: Ruch w lewo
50. [RPG [KeyDesc_PlayerMoveRight] — tekst] 오른쪽으로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerMoveRight].text
   limit: do 120 znaków
   EN: Move right
   PL: Ruch w prawo
51. [RPG [KeyDesc_PlayerFieldAttack] — tekst] 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerFieldAttack].text
   (powtórzenie elementu 13 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [RPG [KeyDesc_PlayerGuard] — tekst] 가드
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerGuard].text
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
53. [RPG [KeyDesc_PlayerDodge] — tekst] 회피
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerDodge].text
   (powtórzenie elementu 15 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
54. [RPG [KeyDesc_PlayerRun] — tekst] 달리기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerRun].text
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [RPG [KeyDesc_PlayerQuestNavigationToggle] — tekst] 퀘스트 안내 화살표
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerQuestNavigationToggle].text
   limit: do 120 znaków
   EN: Toggle quest navigation arrow
   PL: Przełącz strzałkę naprowadzania zadania
56. [RPG [KeyDesc_PlayerLanternToggle] — tekst] 랜턴 ON/OFF
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerLanternToggle].text
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
57. [RPG [KeyDesc_PlayerAutoAttackToggle] — tekst] 오토 공격
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerAutoAttackToggle].text
   (powtórzenie elementu 37 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [RPG [KeyDesc_PlayerSuicide] — tekst] 샘터로 돌아가기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_PlayerSuicide].text
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [RPG [KeyDesc_UiToggleInventoryTab] — tekst] 인벤토리
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_UiToggleInventoryTab].text
   limit: do 120 znaków
   EN: View inventory
   PL: Ekwipunek
60. [RPG [KeyDesc_UiToggleQuestTab] — tekst] 저널:퀘스트
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_UiToggleQuestTab].text
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [RPG [KeyDesc_UiToggleManualTab] — tekst] 단축키 매뉴얼
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_UiToggleManualTab].text
   limit: do 120 znaków
   EN: Keyboard shortcuts guide
   PL: Przewodnik po skrótach klawiszowych
62. [RPG [KeyDesc_UiToggleSystemLog] — tekst] 전체 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyDesc_UiToggleSystemLog].text
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
63. [RPG [KeyBind_InvalidKey] — tekst] 사용할 수 없는 키입니다.
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=KeyBind_InvalidKey].text
   limit: do 120 znaków
   EN: This key is unavailable.
   PL: Ten klawisz jest niedostępny.
64. [RPG [MoveToKeyBind] — tekst] 키 설정 바로가기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p2.json :: dataList[key=MoveToKeyBind].text
   limit: do 120 znaków
   EN: To Key Mapping
   PL: Do mapowania klawiszy

## Tryb RPG [common] — rpg-loc-ui-common-a1c10p3
- obszar/warstwa: `common` · plik gry: `RPGSystem/rpg-loc-ui-common-a1c10p3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

65. [RPG [Setting_Sisyphus_CheckpointRestart] — tekst] 체크포인트 재시작
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Setting_Sisyphus_CheckpointRestart].text
   limit: do 120 znaków
   EN: Restart from checkpoint
   PL: Restart od punktu kontrolnego
66. [RPG [Sisyphus_CheckpointRestartConfirmDesc] — tekst] 체크포인트에서 다시 시작하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Sisyphus_CheckpointRestartConfirmDesc].text
   limit: do 120 znaków
   EN: Restart from the Checkpoint?
   PL: Uruchomić ponownie od punktu kontrolnego?
67. [RPG [Sisyphus_SkipConfirmDesc] — tekst] 이 구간을 건너뛰고 다음으로 진행하시겠습니까?
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Sisyphus_SkipConfirmDesc].text
   limit: do 120 znaków
   EN: Skip this part and continue to the next part of the story?
   PL: Pominąć tę część i przejść do następnej części historii?
68. [RPG [Setting_Sisyphus_PushRock] — tekst] 드롭 바위 때리기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Setting_Sisyphus_PushRock].text
   limit: do 120 znaków
   EN: Punch the Drop-boulder
   PL: Uderz Spadający Głaz
69. [RPG [Setting_Sisyphus_CatchRock] — tekst] 드롭 바위 잡기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Setting_Sisyphus_CatchRock].text
   limit: do 120 znaków
   EN: Grab the Drop-boulder
   PL: Złap Spadający Głaz
70. [RPG [Setting_Sisyphus_Log] — tekst] 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=Setting_Sisyphus_Log].text
   limit: do 120 znaków
   EN: Log
   PL: Dziennik
71. [RPG [WardenArena_ResistFate] — tekst] 운명에 저항하라
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=WardenArena_ResistFate].text
   limit: do 120 znaków
   EN: DEFY FATE
   PL: SPRZECIW SIĘ PRZEZNACZENIU
72. [RPG [KeyDesc_SisypMoveUp] — tekst] 위로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypMoveUp].text
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
73. [RPG [KeyDesc_SisypMoveDown] — tekst] 아래로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypMoveDown].text
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [RPG [KeyDesc_SisypMoveLeft] — tekst] 왼쪽으로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypMoveLeft].text
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
75. [RPG [KeyDesc_SisypMoveRight] — tekst] 오른쪽으로 이동
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypMoveRight].text
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [RPG [KeyDesc_SisypAttack] — tekst] 드롭 바위 때리기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypAttack].text
   (powtórzenie elementu 68 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
77. [RPG [KeyDesc_SisypGrab] — tekst] 드롭 바위 잡기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypGrab].text
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [RPG [KeyDesc_SisypRunToggle] — tekst] 달리기 전환
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypRunToggle].text
   limit: do 120 znaków
   EN: Switch to Sprinting
   PL: Przełącz na bieg
79. [RPG [KeyDesc_SisypRestart] — tekst] 체크포인트에서 재시작
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypRestart].text
   limit: do 120 znaków
   EN: Restart from the Checkpoint
   PL: Restart od punktu kontrolnego
80. [RPG [KeyDesc_SyncNormalSysypKey] — tekst] 단축키 연동하기
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SyncNormalSysypKey].text
   limit: do 120 znaków
   EN: Import Key Mapping
   PL: Zaimportuj mapowanie klawiszy
81. [RPG [KeyDesc_SisypLogToggle] — tekst] 전체 로그
   źródło: RPGSystem/rpg-loc-ui-common-a1c10p3.json :: dataList[key=KeyDesc_SisypLogToggle].text
   (powtórzenie elementu 24 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-location-floor-1
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-location-floor-1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

82. [RPG [999999] — tekst] 샘터
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=999999].text
   limit: do 120 znaków
   EN: The Fount
   PL: Źródło
83. [RPG [110200] — tekst] 뷰티관 로비
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110200].text
   limit: do 120 znaków
   EN: Beauty Hall, 1F
   PL: Salon Urody, 1. piętro
84. [RPG [110300] — tekst] 뷰티관
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110300].text
   limit: do 120 znaków
   EN: Beauty Hall
   PL: Salon Urody
85. [RPG [110400] — tekst] 뷰티관 복도
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110400].text
   limit: do 120 znaków
   EN: Beauty Hall, Corridor
   PL: Salon Urody, Korytarz
86. [RPG [110500] — tekst] SPA관 서쪽
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110500].text
   limit: do 120 znaków
   EN: Casualwear Hall, West
   PL: Salon SPA, Zachód
87. [RPG [110600] — tekst] SPA관 중앙 홀
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110600].text
   limit: do 120 znaków
   EN: Casualwear Hall, Central
   PL: Salon SPA, Środek
88. [RPG [110700] — tekst] SPA관 동쪽
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110700].text
   limit: do 120 znaków
   EN: Casualwear Hall, East
   PL: Salon SPA, Wschód
89. [RPG [110800] — tekst] SPA관 복도
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110800].text
   limit: do 120 znaków
   EN: Casualwear Hall, Corridor
   PL: Salon SPA, Korytarz
90. [RPG [110900] — tekst] 르누아르의 컨템포러리관
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=110900].text
   limit: do 120 znaków
   EN: Le Noir Contemporary Hall
   PL: Salon Contempora Le Noir
91. [RPG [111000] — tekst] 컨템포러리관 복도
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=111000].text
   limit: do 120 znaków
   EN: Contemporary Hall Corridor
   PL: Korytarz Salonu Contempora
92. [RPG [111100] — tekst] 르루주의 컨템포러리관
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=111100].text
   limit: do 120 znaków
   EN: Le Rouge Contemporary Hall
   PL: Salon Contempora Le Rouge
93. [RPG [8000] — tekst] 상영관 A
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=8000].text
   limit: do 120 znaków
   EN: Theater A
   PL: Teatr A
94. [RPG [8001] — tekst] 상영관 B
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=8001].text
   limit: do 120 znaków
   EN: Theater B
   PL: Teatr B
95. [RPG [8002] — tekst] 상영관 C
   źródło: RPGSystem/rpg-loc-location-floor-1.json :: dataList[key=8002].text
   limit: do 120 znaków
   EN: Theater C
   PL: Teatr C

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-a-enemy
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

96. [RPG [N101004] — nazwa wyświetlana] 르루주 점원 미모사
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101004].displayName
   limit: do 50 znaków
   EN: Le Rouge Sales Associate Mimosa
   PL: Pracownik Le Rouge Mimosa
97. [RPG [N101006] — nazwa wyświetlana] 르누아르 점원 구스타프
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101006].displayName
   limit: do 50 znaków
   EN: Le Noir Sales Associate Gustave
   PL: Pracownik Le Noir Gustave
98. [RPG [N101009] — nazwa wyświetlana] 절박한 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101009].displayName
   limit: do 40 znaków
   EN: Desperate Kaki
   PL: Zdesperowany Le Kaki
99. [RPG [N101010] — nazwa wyświetlana] 초조한 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101010].displayName
   limit: do 40 znaków
   EN: Anxious Kaki
   PL: Zniecierpliwiony Le Kaki
100. [RPG [N101011] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101011].displayName
   limit: do 40 znaków
   EN: Leather Glove
   PL: Skórzana Rękawica
101. [RPG [N101030] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101030].displayName
   limit: do 40 znaków
   EN: Denim Wallet
   PL: Portfel z Denimu
102. [RPG [N101034] — nazwa wyświetlana] 바늘꽂이 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-a-enemy.json :: dataList[key=N101034].displayName
   limit: do 40 znaków
   EN: Pincushion Glove
   PL: Rękawica z Poduszką na Szpilki

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-b-enemy
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

103. [RPG [N101004] — nazwa wyświetlana] 르루주 점원 미모사
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101004].displayName
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
104. [RPG [N101006] — nazwa wyświetlana] 르누아르 점원 구스타프
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101006].displayName
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
105. [RPG [N101009] — nazwa wyświetlana] 절박한 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101009].displayName
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
106. [RPG [N101010] — nazwa wyświetlana] 초조한 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101010].displayName
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
107. [RPG [N101011] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101011].displayName
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [RPG [N101030] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101030].displayName
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [RPG [N101034] — nazwa wyświetlana] 바늘꽂이 장갑
   źródło: RPGSystem/rpg-loc-npc-floor-1-b-enemy.json :: dataList[key=N101034].displayName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-b
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

110. [RPG [N101002] — nazwa wyświetlana] 크로머 언니
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101002].displayName
   limit: do 40 znaków
   EN: Kromer's Sister
   PL: Siostra Kromer
111. [RPG [N101003] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101003].displayName
   limit: do 40 znaków
   EN: Meursault
   PL: Meursault
112. [RPG [N101005] — nazwa wyświetlana] 뒤부아
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101005].displayName
   limit: do 40 znaków
   EN: Dubois
   PL: Dubois
113. [RPG [N101007] — nazwa wyświetlana] 퀼리안
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101007].displayName
   limit: do 40 znaków
   EN: Quillian
   PL: Quillian
114. [RPG [N101008] — nazwa wyświetlana] 뒤부아
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101008].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [RPG [N101012] — nazwa wyświetlana] 구경 중인 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101012].displayName
   limit: do 40 znaków
   EN: Eye-shopping Customer
   PL: Klient Tylko Oglądający
116. [RPG [N101013] — nazwa wyświetlana] 시술 받고 있는 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101013].displayName
   limit: do 40 znaków
   EN: Treatment Customer
   PL: Klient w Trakcie Zabiegu
117. [RPG [N101014] — nazwa wyświetlana] 시술 받고 있는 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101014].displayName
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [RPG [N101015] — nazwa wyświetlana] 구경 중인 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101015].displayName
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [RPG [N101017] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101017].displayName
   limit: do 40 znaków
   EN: ???
   PL: ???
120. [RPG [N101021] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101021].displayName
   limit: do 40 znaków
   EN: Yi Sang
   PL: Yi Sang
121. [RPG [N101022] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101022].displayName
   limit: do 40 znaków
   EN: Faust
   PL: Faust
122. [RPG [N101023] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101023].displayName
   limit: do 40 znaków
   EN: Sinclair
   PL: Sinclair
123. [RPG [N101024] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101024].displayName
   limit: do 40 znaków
   EN: Gregor
   PL: Gregor
124. [RPG [N101025] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101025].displayName
   limit: do 40 znaków
   EN: Ryōshū
   PL: Ryōshū
125. [RPG [N101026] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101026].displayName
   limit: do 40 znaków
   EN: Heathcliff
   PL: Heathcliff
126. [RPG [N101027] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101027].displayName
   limit: do 40 znaków
   EN: Outis
   PL: Outis
127. [RPG [N101028] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101028].displayName
   limit: do 40 znaków
   EN: Hong Lu
   PL: Hong Lu
128. [RPG [N101029] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101029].displayName
   limit: do 40 znaków
   EN: Don Quixote
   PL: Don Quixote
129. [RPG [N101031] — nazwa wyświetlana] 초조한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101031].displayName
   limit: do 40 znaków
   EN: Impatient Customer
   PL: Niecierpliwy Klient
130. [RPG [N101032] — nazwa wyświetlana] 절박한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101032].displayName
   limit: do 40 znaków
   EN: Desperate Customer
   PL: Zdesperowany Klient
131. [RPG [N101033] — nazwa wyświetlana] 궁핍한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-b.json :: dataList[key=N101033].displayName
   limit: do 40 znaków
   EN: Destitute Customer
   PL: Skrajnie Biedny Klient

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-c1-enemy
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-c1-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

132. [RPG [N101010] — nazwa wyświetlana] 초조한 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1-enemy.json :: dataList[key=N101010].displayName
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-c1
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-c1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

133. [RPG [N101012] — nazwa wyświetlana] 구경 중인 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101012].displayName
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [RPG [N101013] — nazwa wyświetlana] 시술 받고 있는 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101013].displayName
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [RPG [N101017] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101017].displayName
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [RPG [N101021] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101021].displayName
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [RPG [N101022] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101022].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [RPG [N101023] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101023].displayName
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
139. [RPG [N101024] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101024].displayName
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [RPG [N101025] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101025].displayName
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
141. [RPG [N101026] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101026].displayName
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
142. [RPG [N101027] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101027].displayName
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
143. [RPG [N101028] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101028].displayName
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
144. [RPG [N101029] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101029].displayName
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
145. [RPG [N101031] — nazwa wyświetlana] 초조한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101031].displayName
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [RPG [N101032] — nazwa wyświetlana] 절박한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101032].displayName
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [RPG [N101033] — nazwa wyświetlana] 궁핍한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1-c1.json :: dataList[key=N101033].displayName
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-c2-enemy
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-c2-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

148. [RPG [N990001_C2] — nazwa wyświetlana] 쌓인 것
   źródło: RPGSystem/rpg-loc-npc-floor-1-c2-enemy.json :: dataList[key=N990001_C2].displayName
   limit: do 40 znaków
   EN: The Sedimented
   PL: Osad

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1-c2
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

149. [RPG [N10204] — nazwa wyświetlana] 르네앙
   źródło: RPGSystem/rpg-loc-npc-floor-1-c2.json :: dataList[key=N10204].displayName
   limit: do 40 znaków
   EN: Le Néant
   PL: Le Néant

## Tryb RPG [floor-1] — rpg-loc-npc-floor-1
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-npc-floor-1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

150. [RPG [N101002] — nazwa wyświetlana] 크로머 언니
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101002].displayName
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [RPG [N101003] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101003].displayName
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [RPG [N101005] — nazwa wyświetlana] 뒤부아
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101005].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
153. [RPG [N101007] — nazwa wyświetlana] 퀼리안
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101007].displayName
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
154. [RPG [N101008] — nazwa wyświetlana] 뒤부아
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101008].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [RPG [N101012] — nazwa wyświetlana] 구경 중인 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101012].displayName
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
156. [RPG [N101013] — nazwa wyświetlana] 시술 받고 있는 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101013].displayName
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
157. [RPG [N101014] — nazwa wyświetlana] 시술 받고 있는 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101014].displayName
   (powtórzenie elementu 116 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
158. [RPG [N101015] — nazwa wyświetlana] 구경 중인 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101015].displayName
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
159. [RPG [N101017] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101017].displayName
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
160. [RPG [N101021] — nazwa wyświetlana] 이상
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101021].displayName
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [RPG [N101022] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101022].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [RPG [N101023] — nazwa wyświetlana] 싱클레어
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101023].displayName
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
163. [RPG [N101024] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101024].displayName
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [RPG [N101025] — nazwa wyświetlana] 료슈
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101025].displayName
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
165. [RPG [N101026] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101026].displayName
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [RPG [N101027] — nazwa wyświetlana] 오티스
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101027].displayName
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
167. [RPG [N101028] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101028].displayName
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
168. [RPG [N101029] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101029].displayName
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [RPG [N101031] — nazwa wyświetlana] 초조한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101031].displayName
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [RPG [N101032] — nazwa wyświetlana] 절박한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101032].displayName
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [RPG [N101033] — nazwa wyświetlana] 궁핍한 고객
   źródło: RPGSystem/rpg-loc-npc-floor-1.json :: dataList[key=N101033].displayName
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-quest-floor-1-b
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-quest-floor-1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

172. [RPG [Q1001] — opis] 화장실로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1001].description
   limit: do 120 znaków
   EN: Return to the Restroom
   PL: Wróć do toalety
173. [RPG [Q1011] — tytuł] 백화점을 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1011].title
   limit: do 40 znaków
   EN: Explore the Department Store
   PL: Zbadaj Dom Handlowy
174. [RPG [Q1011] — opis] 이상하다. 우리는 다시 화장실로 돌아왔고, 다들 아무것도 기억하지 못하는 것처럼 행동하며 뫼르소는 보이지 않는다. 모든 게 꿈이었을리는 없다. 일단 백화점을 둘러보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1011].description
   limit: do 280 znaków
   EN: Something's off. We're back in the restroom, but everyone is acting like they don't remember a thing, and Meursault is nowhere to be seen. This couldn't all have been a dream. Let's look around the department store.
   PL: Coś jest nie tak. Znaleźliśmy się z powrotem w toalecie, a wszyscy zachowują się, jakby niczego nie pamiętali, i nie widać Meursaulta. To nie mogło być tylko snem. Zbadajmy dom handlowy.
175. [RPG [Q1011] — krok 1 — cel zadania 1] 백화점 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1011].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Explore the Department Store
   PL: Zbadaj Dom Handlowy
176. [RPG [Q1013] — tytuł] SPA관으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1013].title
   limit: do 40 znaków
   EN: Head to the Casualwear Hall
   PL: Udaj się do Salonu SPA
177. [RPG [Q1013] — opis] 다행히도 꿈은 아닌 것 같다. 일단 앞으로 계속 가보자. 어딘가에 있을 뫼르소를 찾는 게 먼저일 것 같다. 어쩌면 지난번에 있던 그 매장에 있을지도?
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1013].description
   limit: do 200 znaków
   EN: At least it doesn't seem like it was all a dream. For now, let's keep moving and focus on finding Meursault. He may be back at the same store as last time.
   PL: Wygląda na to, że to jednak nie był sen. Na razie idźmy dalej. Najpierw trzeba odnaleźć Meursaulta. Może wciąż jest w tym samym sklepie co ostatnio?
178. [RPG [Q1013] — krok 1 — cel zadania 1] SPA관으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1013].steps[#0].goalDescription1
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [RPG [Q1021] — tytuł] 뫼르소를 찾기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1021].title
   limit: do 40 znaków
   EN: Find Meursault
   PL: Odnajdź Meursaulta
180. [RPG [Q1021] — opis] 이 근처 어딘가에 뫼르소가 있을 것이다. 뫼르소를 찾은 후 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1021].description
   limit: do 120 znaków
   EN: Meursault should be somewhere nearby. Find him and talk to him.
   PL: Meursault powinien być gdzieś w pobliżu. Odnajdź go i zagadaj.
181. [RPG [Q1021] — krok 1 — cel zadania 1] 뫼르소에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1021].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to Meursault
   PL: Zagadaj Meursaulta
182. [RPG [Q1022] — tytuł] 마네킹의 퇴장
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1022].title
   limit: do 50 znaków
   EN: Show the Mannequins to the Exit
   PL: Wyprowadź Manekiny
183. [RPG [Q1022] — opis] 뫼르소를 데려가기 위해서는 SPA관의 미모사의 부탁을 들어줘야 한다. 빠르게 마네킹들을 처치하고 벗어나자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1022].description
   limit: do 180 znaków
   EN: If we want to take Meursault with us, we'll have to do Mimosa a favor first. Let's make quick work of the Mannequins and get out of here.
   PL: Żeby zabrać Meursaulta, musimy najpierw spełnić prośbę Mimosy z Salonu SPA. Szybko rozprawmy się z manekinami i stąd uciekajmy.
184. [RPG [Q1022] — krok 1 — cel zadania 1] 마네킹을 찾으러 가기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1022].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Go Find the Mannequins
   PL: Idź odszukać manekiny
185. [RPG [Q1023] — tytuł] 마네킹의 퇴장 2
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1023].title
   limit: do 50 znaków
   EN: Show the Mannequins to the Exit (2)
   PL: Wyprowadź Manekiny (2)
186. [RPG [Q1023] — opis] 대화를 더 이상 길게 이어갈 필요가 없다. 마네킹들을 빠르게 퇴장시키자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1023].description
   limit: do 140 znaków
   EN: There's no need to drag this conversation out any longer. Let's clear out the Mannequins and move on.
   PL: Nie ma sensu przeciągać tej rozmowy. Szybko przepędźmy manekiny.
187. [RPG [Q1023] — krok 1 — cel zadania 1] 마네킹 퇴장시키기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1023].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Help the Mannequins "to the Exit"
   PL: Pomóż manekinom „dotrzeć do wyjścia”
188. [RPG [Q1023] — krok 2 — cel zadania 1] 미모사에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1023].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Return to Mimosa
   PL: Wróć do Mimosy
189. [RPG [Q1031] — tytuł] 1층 벗어나기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1031].title
   limit: do 40 znaków
   EN: Leave 1F
   PL: Opuść 1. piętro
190. [RPG [Q1031] — opis] 다행히도 처음보다는 좋아진 상황이다. 이번에는 다른 결과를 도출해야 한다. 일단 1층을 벗어나는 게 급선무다. 빠르게 SPA관을 벗어나 다음 매장으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1031].description
   limit: do 270 znaków
   EN: Things are already going better than last time. If we're going to get a different outcome, we need to keep moving. First priority: get off 1F. We should leave the Casualwear Hall and head for the next store.
   PL: Na szczęście sytuacja wygląda lepiej niż za pierwszym razem. Tym razem musi wyjść inaczej. Priorytetem jest opuszczenie 1. piętra. Szybko opuśćmy Salon SPA i udamy się do kolejnego sklepu.
191. [RPG [Q1031] — krok 1 — cel zadania 1] SPA관 벗어나기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1031].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Leave the Casualwear Hall
   PL: Opuść Salon SPA
192. [RPG [Q1064] — tytuł] 2층으로 향하는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1064].title
   limit: do 40 znaków
   EN: Take the Escalator to 2F
   PL: Wjedź schodami ruchomymi na 2. piętro
193. [RPG [Q1064] — opis] 지난번에도 우리에게 말을 걸었던 뒤부아라는 자를 만났다. 하지만 길게 대화할 시간이 없다. 빠르게 다음 층으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1064].description
   limit: do 190 znaków
   EN: We ran into Dubois, who spoke to us last time as well. There's no time for a long conversation, though. Let's head straight to the next floor.
   PL: Spotkaliśmy Dubois, który rozmawiał z nami już ostatnio. Nie ma jednak czasu na długie rozmowy. Szybko udamy się na kolejne piętro.
194. [RPG [Q1064] — krok 1 — cel zadania 1] 2층으로 향하는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-1-b.json :: dataList[key=Q1064].steps[#0].goalDescription1
   (powtórzenie elementu 192 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-quest-floor-1-c1
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-quest-floor-1-c1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

195. [RPG [Q1011] — tytuł] 뷰티관에서 곧 벌어질 상황을 받아들이기
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1011].title
   limit: do 70 znaków
   EN: Accept the Inevitabilities of the Beauty Hall
   PL: Zaakceptuj nieuchronność Salonu Urody
196. [RPG [Q1011] — opis] 결말은 달라지지 않았다. 이제 어떡해야 할까? 무턱대고 화장실 밖으로 나왔다. 이제 곧 벌어질 상황들을 받아들이고 빠르게 뫼르소를 찾아야 한다.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1011].description
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The end refused to change. I don't know what else we can do at this moment, but I decided to leave the restroom. \nFirst things first: process the inevitable and find Meursault.
   PL: Zakończenie się nie zmieniło. Co teraz? Wyszliśmy z toalety bez zastanowienia. Najpierw pogódźmy się z nieuchronnym i szybko odnajdźmy Meursaulta.
197. [RPG [Q1014] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1014].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [RPG [Q1014] — opis] 무언가 숨겨져 있는 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1014].description
   limit: do 120 znaków
   EN: It seems something is hidden here.
   PL: Wygląda na to, że coś się tu ukrywa.
199. [RPG [Q1014] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1014].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [RPG [Q1015] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1015].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [RPG [Q1015] — opis] 무언가 숨겨져 있는 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1015].description
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
202. [RPG [Q1015] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1015].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [RPG [Q1016] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1016].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
204. [RPG [Q1016] — opis] 무언가 숨겨져 있는 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1016].description
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [RPG [Q1016] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1016].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [RPG [Q1017] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1017].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [RPG [Q1017] — opis] 무언가 숨겨져 있는 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1017].description
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [RPG [Q1017] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1017].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [RPG [Q1064] — tytuł] 2층으로
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1064].title
   limit: do 40 znaków
   EN: To 2F
   PL: Na 2. piętro
210. [RPG [Q1064] — krok 1 — cel zadania 1] 2층 도착
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1064].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Arrived at 2F
   PL: Przybycie na 2. piętro
211. [RPG [Q1018] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1-c1.json :: dataList[key=Q1018].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-quest-floor-1-c2
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-quest-floor-1-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

212. [RPG [Q1001_C2] — tytuł] 5층까지 올라가기
   źródło: RPGSystem/rpg-loc-quest-floor-1-c2.json :: dataList[key=Q1001_C2].title
   limit: do 40 znaków
   EN: Climb to 5F
   PL: Wspinaj się na 5. piętro
213. [RPG [Q1001_C2] — opis] 우리는 운명에 저항했다. 간수는 더 이상 나타나지 않을 것이다. 우리가 마지막에 도달했었던 백화점의 5층까지 올라가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1-c2.json :: dataList[key=Q1001_C2].description
   limit: do 190 znaków
   EN: We defied fate. The Warden will no longer show up and hamper us at every turn. It's now time to head to 5F, where things ended in our previous loop.
   PL: Sprzeciwiliśmy się przeznaczeniu. Strażnik już się nie pojawi. Udamy się na 5. piętro, gdzie skończyła się nasza poprzednia pętla.
214. [RPG [Q1001_C2] — krok 1 — cel zadania 1] 5층까지 올라가기
   źródło: RPGSystem/rpg-loc-quest-floor-1-c2.json :: dataList[key=Q1001_C2].steps[#0].goalDescription1
   (powtórzenie elementu 212 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-quest-floor-1
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-quest-floor-1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

215. [RPG [Q1011] — tytuł] 주위 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1011].title
   limit: do 40 znaków
   EN: Explore the Surroundings
   PL: Rozglądaj się w okolicy
216. [RPG [Q1011] — opis] 시지프 백화점이라는 곳으로 왔다. 뫼르소는 어디 있는 걸까? 일단 주위를 둘러보는 편이 좋을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1011].description
   limit: do 170 znaków
   EN: We've arrived at a place called Grand Magasin Sisyphe. Where could Meursault be...? Let's first look around and get our bearings.
   PL: Przybyliśmy do miejsca zwanego Grand Magasin Sisyphe. Gdzie może być Meursault? Najpierw dobrze się rozejrzyjmy.
217. [RPG [Q1011] — krok 1 — cel zadania 1] 주위 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1011].steps[#0].goalDescription1
   (powtórzenie elementu 215 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [RPG [Q1012] — tytuł] 화장실로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1012].title
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [RPG [Q1012] — opis] 시지프 백화점에서 크로머의 친언니를 만났다. 일단 화장실로 다시 돌아가서 재정비를 해보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1012].description
   limit: do 150 znaków
   EN: We ran into Kromer's older sister at Grand Magasin Sisyphe. We should return to the restroom and regroup first.
   PL: W Grand Magasin Sisyphe spotkaliśmy rodzoną siostrę Kromer. Najpierw wróćmy do toalety i przegrupujmy się.
220. [RPG [Q1012] — krok 1 — cel zadania 1] 화장실로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1012].steps[#0].goalDescription1
   (powtórzenie elementu 172 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [RPG [Q1013] — tytuł] 뫼르소를 찾아서
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1013].title
   limit: do 40 znaków
   EN: In Search of Meursault
   PL: W poszukiwaniu Meursaulta
222. [RPG [Q1013] — opis] 뫼르소는 백화점 어딘가에 있는 것 같다. 바닥에 카펫이 보였고 앞에는 옷들이 진열되어 있는 곳이었다. 백화점을 둘러보며 옷이 전시되어 있는 곳을 찾아가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1013].description
   limit: do 270 znaków
   EN: Meursault seems to be somewhere in the department store. We saw carpeting on the floor, with clothes displayed in the front. We should explore the department store and find the place where clothes are on display.
   PL: Meursault chyba przebywa gdzieś w domu handlowym. Widzieliśmy dywan na podłodze, a przed nim miejsce, gdzie wystawiono ubrania. Zwiedźmy dom handlowy i odszukajmy miejsce z wystawą odzieży.
223. [RPG [Q1013] — krok 1 — cel zadania 1] 백화점 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1013].steps[#0].goalDescription1
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [RPG [Q1014] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1014].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
225. [RPG [Q1014] — opis] 무언가 숨겨져 있는 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1014].description
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
226. [RPG [Q1014] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1014].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [RPG [Q1021] — tytuł] 뫼르소를 찾아서 2
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1021].title
   limit: do 40 znaków
   EN: In Search of Meursault (2)
   PL: W poszukiwaniu Meursaulta (2)
228. [RPG [Q1021] — opis] 이 근처 어딘가에 뫼르소가 있을 것 같다. 뫼르소를 찾아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1021].description
   limit: do 120 znaków
   EN: Meursault seems to be somewhere nearby. We should look for him.
   PL: Meursault chyba jest gdzieś w pobliżu. Poszukajmy go.
229. [RPG [Q1021] — krok 1 — cel zadania 1] 뫼르소를 찾아보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1021].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Locate Meursault
   PL: Zlokalizuj Meursaulta
230. [RPG [Q1022] — tytuł] 퀘스트4-1 - 뫼르소의 제안
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1022].title
   limit: do 40 znaków
   EN: Meursault's Suggestion
   PL: Zadanie 4-1 — Propozycja Meursaulta
231. [RPG [Q1022] — opis] 뫼르소의 제안을 수락할지 결정하기\n→ 수락 시 사냥 퀘스트 시작, 보류 시 SPA 직원에게 다시 문의 가능
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1022].description
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Decide whether to accept Meursault's suggestion.\n→ Accepting begins the hunting quest; if deferred, this quest can be received again from the Casualwear Hall employee.
   PL: Zdecyduj, czy przyjąć propozycję Meursaulta.\n→ Przyjęcie rozpoczyna zadanie łowieckie; przy odmowie można zapytać ponownie pracownika Salonu SPA.
232. [RPG [Q1023] — tytuł] 마네킹의 퇴장
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1023].title
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [RPG [Q1023] — opis] 뫼르소를 돌려받기 위해서는 마네킹이라 불리는 것들을 3마리 퇴장시켜야 한다고 한다. 마네킹들을 처치한 후 매장의 주인으로 보이는 미모사에게 되돌아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1023].description
   limit: do 230 znaków
   EN: To get Meursault back, we need to "help the Mannequins to the exit"—three of them, in total. Kill them and report back to Mimosa, who seems to be the proprietor of the store.
   PL: Aby odzyskać Meursaulta, mamy podobno „odprowadzić do wyjścia” trzy manekiny. Pokonajmy je i wróćmy do Mimosy, która wygląda na właścicielkę sklepu.
234. [RPG [Q1023] — krok 1 — cel zadania 1] 마네킹 퇴장시키기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1023].steps[#0].goalDescription1
   (powtórzenie elementu 187 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [RPG [Q1023] — krok 2 — cel zadania 1] 미모사에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1023].steps[#1].goalDescription1
   (powtórzenie elementu 188 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [RPG [Q1031] — tytuł] 시지프 백화점 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1031].title
   limit: do 50 znaków
   EN: Explore Grand Magasin Sisyphe
   PL: Zbadaj Grand Magasin Sisyphe
237. [RPG [Q1031] — opis] 뫼르소로부터 시지프 백화점에 대한 설명을 들었다. 전부 이해 가는 것은 아니지만 이곳엔 제대로 된 출구가 있는 것 같진 않다. 일단 이곳을 계속 둘러보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1031].description
   limit: do 230 znaków
   EN: Meursault explained what he knows about Grand Magasin Sisyphe. I didn't follow all of it, but one thing is clear: there doesn't seem to be a normal way out. Let's keep exploring.
   PL: Meursault opowiedział nam, co wie o Grand Magasin Sisyphe. Nie wszystko zrozumiałem, ale jedno jest pewne: nie wygląda na to, by było tu normalne wyjście. Rozglądajmy się dalej.
238. [RPG [Q1031] — krok 1 — cel zadania 1] 백화점 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1031].steps[#0].goalDescription1
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [RPG [Q1032] — tytuł] 시지프 백화점 둘러보기 2
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1032].title
   limit: do 50 znaków
   EN: Explore Grand Magasin Sisyphe (2)
   PL: Zbadaj Grand Magasin Sisyphe (2)
240. [RPG [Q1032] — opis] 뒤부아라고 불리는 자를 만났다. 이자도 우리처럼 시지프 백화점에 들어온 지 얼마 안 된 사람 같아 보였다. 위층에 올라갈 방법을 찾기 위해 백화점을 계속해서 둘러보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1032].description
   limit: do 180 znaków
   EN: We met a guy named Dubois. Like us, he doesn't seem to have been here long. Let's keep searching the department store for a way upstairs.
   PL: Spotkaliśmy człowieka nazwiskiem Dubois. Wygląda na to, że jak my trafił tu niedawno. Szukajmy dalej sposobu na dostanie się na wyższe piętra.
241. [RPG [Q1032] — krok 1 — cel zadania 1] 백화점 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1032].steps[#0].goalDescription1
   (powtórzenie elementu 175 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [RPG [Q1041] — tytuł] 진열되어 있는 옷 구경하기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1041].title
   limit: do 40 znaków
   EN: Browse the Clothing Display
   PL: Obejrzyj wystawę ubrań
243. [RPG [Q1041] — opis] 컨템포러리 매장이라는 곳에 왔다. 이곳의 직원은 우리에게 별다른 말을 걸지 않는다. 매장에 진열되어 있는 옷들을 구경해보는 것도 좋을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1041].description
   limit: do 180 znaków
   EN: We've reached a Contemporary Hall. The employee doesn't seem interested in talking. We may as well look through the clothes on display.
   PL: Dotarliśmy do Salonu Contempora. Jego pracownik nie kwapi się do rozmowy. Możemy się przyjrzeć ubraniom wystawionym w sklepie.
244. [RPG [Q1041] — krok 1 — cel zadania 1] 옷 구경하기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1041].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Browse the Clothes
   PL: Obejrzyj ubrania
245. [RPG [Q1042] — tytuł] 공격하는 르누아르 직원을 막아내기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1042].title
   limit: do 50 znaków
   EN: Fend off the Hostile Noir Employee
   PL: Odepchnij agresywnego pracownika Le Noir
246. [RPG [Q1051] — tytuł] 르루주의 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1051].title
   limit: do 40 znaków
   EN: Head to the Rouges' Store
   PL: Udaj się do sklepu Le Rouge
247. [RPG [Q1051] — opis] 르누아르 직원으로부터 황금송진에 대한 이야기를 들었다. 이번에는 위에 있는 르루주의 컨템포러리 매장으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1051].description
   limit: do 150 znaków
   EN: A Noir employee told us about Golden Resin. Next, let's check Le Rouge's Contemporary store on the upper side.
   PL: Pracownik Le Noir opowiedział nam o Złotej Żywicy. Teraz udajmy się do położonego wyżej Salonu Contempora Le Rouge.
248. [RPG [Q1051] — krok 1 — cel zadania 1] 르루주의 컨템포러리 매장으로 가기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1051].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Go to Le Rouge's Contemporary Store
   PL: Udaj się do Salonu Contempora Le Rouge
249. [RPG [Q1052] — tytuł] 커다란 바늘 구해오기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1052].title
   limit: do 40 znaków
   EN: Find a Huge Needle
   PL: Zdobądź wielką igłę
250. [RPG [Q1052] — opis] 르루주 컨템포러리 매장 직원인 퀼리안으로부터 커다란 바늘을 구해 와달라는 부탁을 받았다. 바늘을 가지고 있는 마네킹을 찾아본 후, 바늘을 얻고 퀼리안에게 돌아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1052].description
   limit: do 200 znaków
   EN: Quillian at Le Rouge's Contemporary Store asked us to bring back a huge needle. Find the Mannequin carrying it, take the needle, and return to Quillian.
   PL: Quillian, pracownik Salonu Contempora Le Rouge, poprosił o przyniesienie wielkiej igły. Odszukaj manekina, który ją ma, zdobądź igłę i wróć do Quilliana.
251. [RPG [Q1052] — krok 1 — cel zadania 1] 마네킹으로부터 커다란 바늘을 구한 후 퀼리안에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1052].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Retrieve the Huge Needle and Return to Quillian
   PL: Zdobądź wielką igłę od manekina i wróć do Quilliana
252. [RPG [Q1061] — tytuł] 옷 쇼핑하기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1061].title
   limit: do 40 znaków
   EN: Go Shopping for Clothes
   PL: Kup ubrania
253. [RPG [Q1061] — opis] 위층으로 가기 위해서는 먼저 구매 실적을 쌓아야 한다고 한다. 매장의 직원으로부터 옷을 구매한 후 위층으로 갈 방법을 계속 찾아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1061].description
   limit: do 190 znaków
   EN: We need to build up a purchase record before we can access the upper floor. Buy some clothes from Quillian, then keep looking for a way upstairs.
   PL: Podobno, żeby dostać się na wyższe piętro, trzeba najpierw zbudować historię zakupów. Kup coś od pracownika sklepu i szukajmy dalej sposobu wejścia na górę.
254. [RPG [Q1061] — krok 1 — cel zadania 1] 퀼리안으로부터 옷을 구매하기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1061].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Buy Clothes from Quillian
   PL: Kup ubrania od Quilliana
255. [RPG [Q1062] — tytuł] 에스컬레이터로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1062].title
   limit: do 40 znaków
   EN: To the Escalator
   PL: Udaj się do schodów ruchomych
256. [RPG [Q1062] — opis] 다음 층으로 갈 수 있는 에스컬레이터를 찾았다. 아까 만났던 뒤부아도 보인다. 말을 걸어보는 편이 좋을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1062].description
   limit: do 140 znaków
   EN: We've found an escalator leading to the next floor. Dubois is here too. Let's talk to him before heading up.
   PL: Znaleźliśmy schody ruchome na kolejne piętro. Widzę też Dubois. Porozmawiajmy z nim przed wjazdem.
257. [RPG [Q1062] — krok 1 — cel zadania 1] 뒤부아에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1062].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to Dubois
   PL: Zagadaj Dubois
258. [RPG [Q1064] — tytuł] 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1064].title
   limit: do 40 znaków
   EN: Take the Escalator
   PL: Wjedź schodami ruchomymi
259. [RPG [Q1064] — opis] 에스컬레이터가 무사히 작동되고 있다. 이제 2층으로 올라갈 수 있을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1064].description
   limit: do 120 znaków
   EN: The escalator is working. We should finally be able to reach 2F.
   PL: Schody ruchome działają bez zarzutu. Chyba możemy wreszcie dostać się na 2. piętro.
260. [RPG [Q1064] — krok 1 — cel zadania 1] 2층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1064].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Take the Escalator to 2F
   PL: Wjedź schodami ruchomymi na 2. piętro
261. [RPG [Q1018] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-1.json :: dataList[key=Q1018].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-swarm-mob-floor-1-a
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-1-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

262. [RPG [swarm_denim_baggar] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-a.json :: dataList[key=swarm_denim_baggar].displayName
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [RPG [swarm_leather_mutt] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-a.json :: dataList[key=swarm_leather_mutt].displayName
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [RPG [swarm_needle_leather_mutt] — nazwa wyświetlana] 바늘꽂이 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-a.json :: dataList[key=swarm_needle_leather_mutt].displayName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [RPG [swarm_shopper_a] — nazwa wyświetlana] 절박한 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-a.json :: dataList[key=swarm_shopper_a].displayName
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [RPG [swarm_shopper_b] — nazwa wyświetlana] 초조한 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-a.json :: dataList[key=swarm_shopper_b].displayName
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-1] — rpg-loc-swarm-mob-floor-1-b
- obszar/warstwa: `floor-1` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

267. [RPG [swarm_denim_baggar] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-b.json :: dataList[key=swarm_denim_baggar].displayName
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [RPG [swarm_leather_mutt] — nazwa wyświetlana] 가죽 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-b.json :: dataList[key=swarm_leather_mutt].displayName
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [RPG [swarm_needle_leather_mutt] — nazwa wyświetlana] 바늘꽂이 장갑
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-b.json :: dataList[key=swarm_needle_leather_mutt].displayName
   (powtórzenie elementu 102 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [RPG [swarm_shopper_a] — nazwa wyświetlana] 절박한 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-b.json :: dataList[key=swarm_shopper_a].displayName
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [RPG [swarm_shopper_b] — nazwa wyświetlana] 초조한 르카키
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-1-b.json :: dataList[key=swarm_shopper_b].displayName
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-location-floor-2
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-location-floor-2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

272. [RPG [120100] — tekst] 명품관 입구
   źródło: RPGSystem/rpg-loc-location-floor-2.json :: dataList[key=120100].text
   limit: do 120 znaków
   EN: Luxury Hall Entrance
   PL: Wejście do Salonu Prestiżu
273. [RPG [120200] — tekst] 명품관의 요람 입구
   źródło: RPGSystem/rpg-loc-location-floor-2.json :: dataList[key=120200].text
   limit: do 120 znaków
   EN: Entrance to Luxury Hall Cradle
   PL: Wejście do Kołyski Salonu Prestiżu
274. [RPG [120300] — tekst] 명품관
   źródło: RPGSystem/rpg-loc-location-floor-2.json :: dataList[key=120300].text
   limit: do 120 znaków
   EN: Luxury Hall
   PL: Salon Prestiżu
275. [RPG [120400] — tekst] 명품관의 요람
   źródło: RPGSystem/rpg-loc-location-floor-2.json :: dataList[key=120400].text
   limit: do 120 znaków
   EN: Luxury Hall Cradle
   PL: Kołyska Salonu Prestiżu

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-a-enemy
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

276. [RPG [N102002] — nazwa wyświetlana] 브랜드 디렉터
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102002].displayName
   limit: do 40 znaków
   EN: Brand Director
   PL: Dyrektor Marki
277. [RPG [N102004] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102004].displayName
   limit: do 40 znaków
   EN: Le Rouge Staff
   PL: Personel Le Rouge
278. [RPG [N102025] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102025].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [RPG [N102026] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102026].displayName
   limit: do 40 znaków
   EN: Resisting Rouge
   PL: Buntujący się Le Rouge
280. [RPG [N102027] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102027].displayName
   limit: do 40 znaków
   EN: Le Rouge Store Manager
   PL: Kierownik Sklepu Le Rouge
281. [RPG [N102042] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102042].displayName
   limit: do 40 znaków
   EN: Charging Noir
   PL: Szarżujący Le Noir
282. [RPG [N102043] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102043].displayName
   limit: do 40 znaków
   EN: Storming Noir
   PL: Szturmujący Le Noir
283. [RPG [N102044] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102044].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [RPG [N102046] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-a-enemy.json :: dataList[key=N102046].displayName
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-b-enemy
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

285. [RPG [N102002] — nazwa wyświetlana] 브랜드 디렉터
   źródło: RPGSystem/rpg-loc-npc-floor-2-b-enemy.json :: dataList[key=N102002].displayName
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [RPG [N102004] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b-enemy.json :: dataList[key=N102004].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [RPG [N102071] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b-enemy.json :: dataList[key=N102071].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-b
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

288. [RPG [N102003] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102003].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [RPG [N102008] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102008].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [RPG [N102009] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102009].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
291. [RPG [N102010] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102010].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
292. [RPG [N102011] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102011].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [RPG [N102013] — nazwa wyświetlana] 르누아르 메종 점원
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102013].displayName
   limit: do 50 znaków
   EN: Maison du Noir Sales Associate
   PL: Pracownik Maison du Noir
294. [RPG [N102014] — nazwa wyświetlana] 고치
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102014].displayName
   limit: do 40 znaków
   EN: Cocoon
   PL: Kokon
295. [RPG [N102015] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102015].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [RPG [N102016] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102016].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
297. [RPG [N102017] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102017].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [RPG [N102018] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102018].displayName
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
299. [RPG [N102019] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102019].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [RPG [N102020] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102020].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [RPG [N102021] — nazwa wyświetlana] 브랜드 디렉터
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102021].displayName
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [RPG [N102022] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102022].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [RPG [N102023] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102023].displayName
   limit: do 40 znaków
   EN: Buffet
   PL: Bufet
304. [RPG [N102024] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102024].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [RPG [N102025] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102025].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [RPG [N102026] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-2-b.json :: dataList[key=N102026].displayName
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-c1-enemy
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-c1-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

307. [RPG [N102050] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-2-c1-enemy.json :: dataList[key=N102050].displayName
   limit: do 40 znaków
   EN: (brak wersji angielskiej)
   PL: ???

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-c2-enemy
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-c2-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

308. [RPG [N990001_C2] — nazwa wyświetlana] 쌓인 것
   źródło: RPGSystem/rpg-loc-npc-floor-2-c2-enemy.json :: dataList[key=N990001_C2].displayName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2-c2
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

309. [RPG [N10200] — nazwa wyświetlana] 르네앙
   źródło: RPGSystem/rpg-loc-npc-floor-2-c2.json :: dataList[key=N10200].displayName
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-npc-floor-2
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-npc-floor-2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

310. [RPG [N102001] — nazwa wyświetlana] 크로머 언니
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102001].displayName
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [RPG [N102003] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102003].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [RPG [N102008] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102008].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
313. [RPG [N102009] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102009].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [RPG [N102010] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102010].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [RPG [N102011] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102011].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [RPG [N102012] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102012].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
317. [RPG [N102013] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102013].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [RPG [N102014] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102014].displayName
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [RPG [N102015] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102015].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [RPG [N102018] — nazwa wyświetlana] 고치
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102018].displayName
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [RPG [N102019] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102019].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [RPG [N102020] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102020].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [RPG [N102021] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102021].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [RPG [N102022] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102022].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [RPG [N102023] — nazwa wyświetlana] 브랜드 디렉터
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102023].displayName
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [RPG [N102024] — nazwa wyświetlana] 브랜드 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102024].displayName
   limit: do 40 znaków
   EN: Brand Manager
   PL: Dyrektor Marki
327. [RPG [N102028] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102028].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [RPG [N102029] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102029].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [RPG [N102030] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102030].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [RPG [N102031] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102031].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [RPG [N102032] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102032].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [RPG [N102033] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102033].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [RPG [N102034] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102034].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [RPG [N102040] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102040].displayName
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [RPG [N102041] — nazwa wyświetlana] 르누아르 대형 경비
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102041].displayName
   limit: do 40 znaków
   EN: Le Noir Highguard
   PL: Wielki Strażnik Le Noir
336. [RPG [N102035] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102035].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [RPG [N102036] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102036].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [RPG [N102037] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102037].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [RPG [N102038] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102038].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [RPG [N102039] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102039].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [RPG [N102045] — nazwa wyświetlana] 브랜드 디렉터
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102045].displayName
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
342. [RPG [N102047] — nazwa wyświetlana] 붉은 신[미생]
   źródło: RPGSystem/rpg-loc-npc-floor-2.json :: dataList[key=N102047].displayName
   limit: do 50 znaków
   EN: The Crimson God [Inchoate Life]
   PL: Karmazynowy Bóg [Zarodek Życia]

## Tryb RPG [floor-2] — rpg-loc-quest-floor-2-b
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-quest-floor-2-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

343. [RPG [Q2001] — tytuł] 2층 빠르게 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2001].title
   limit: do 40 znaków
   EN: Take a Quick Look Around 2F
   PL: Szybkie rozejrzenie się po 2. piętrze
344. [RPG [Q2001] — opis] 또다시 2층에 도착했다. 지난번에도 그랬듯이 곧바로 들어가지는 못할 것이다. 일단 빠르게 주위를 둘러보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2001].description
   limit: do 160 znaków
   EN: We're back on 2F. Just like last time, we probably won't be able to head straight in. Let's take a quick look around first.
   PL: Znowu jesteśmy na 2. piętrze. Podobnie jak ostatnio, raczej nie wejdziemy od razu do środka. Najpierw szybko się rozejrzyjmy.
345. [RPG [Q2001] — krok 1 — cel zadania 1] 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Explore 2F
   PL: Rozejrzyj się po 2. piętrze
346. [RPG [Q2003] — tytuł] 명품관 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2003].title
   limit: do 40 znaków
   EN: Enter the Luxury Hall
   PL: Wejdź do Salonu Prestiżu
347. [RPG [Q2003] — opis] 문을 지키던 자가 사라졌다. 상황이 달라진 걸까? 안으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2003].description
   limit: do 120 znaków
   EN: The one guarding the entrance is gone. Maybe things have changed. Let's head inside.
   PL: Ten, kto strzegł wejścia, zniknął. Czy coś się zmieniło? Wejdźmy do środka.
348. [RPG [Q2003] — krok 1 — cel zadania 1] 명품관 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2003].steps[#0].goalDescription1
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [RPG [Q2004] — tytuł] 명품관 안으로 들어가기 2
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2004].title
   limit: do 40 znaków
   EN: Enter the Luxury Hall (2)
   PL: Wejdź do Salonu Prestiżu (2)
350. [RPG [Q2004] — opis] 명품관에는 르누아르들의 시체로 가득하다. 더 안쪽으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2004].description
   limit: do 120 znaków
   EN: The Luxury Hall is littered with Le Noir corpses. Let's keep moving in.
   PL: Salon Prestiżu jest usiany zwłokami Le Noir. Idźmy głębiej.
351. [RPG [Q2004] — krok 1 — cel zadania 1] 명품관 안으로 계속 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2004].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head deeper into the Luxury Hall
   PL: Wchodź dalej w głąb Salonu Prestiżu
352. [RPG [Q2005] — tytuł] 명품관 안으로 들어가기 3
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2005].title
   limit: do 40 znaków
   EN: Enter the Luxury Hall (3)
   PL: Wejdź do Salonu Prestiżu (3)
353. [RPG [Q2005] — opis] 지난번과 똑같이 르루주들이 만든 입구가 보였다. 안으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2005].description
   limit: do 120 znaków
   EN: The same entrance created by the Rouges is here again. Let's go through.
   PL: Znowu widać wejście utworzone przez Le Rouge. Wejdźmy.
354. [RPG [Q2005] — krok 1 — cel zadania 1] 명품관 입구로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2005].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Enter the Luxury Hall via the entrance
   PL: Wejdź przez wejście do Salonu Prestiżu
355. [RPG [Q2008] — tytuł] 요람을 관찰해보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].title
   limit: do 40 znaków
   EN: Inspect the Cradle
   PL: Przyjrzyj się Kołysce
356. [RPG [Q2008] — opis] 르루주의 브랜드 디렉터는 요람에 자고 있는 것이 곧 깨어날 것이며, 그 곁에 우리가 있어 달라는 부탁을 했다. 일단 요람 앞으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].description
   limit: do 200 znaków
   EN: Le Rouge's Brand Director says whatever is sleeping in the Cradle will wake soon, and asked us to stay by its side. For now, let's approach the Cradle.
   PL: Dyrektor Marki Le Rouge powiedział, że to, co śpi w Kołysce, wkrótce się obudzi, i poprosił, byśmy byli przy tym obecni. Podejdźmy najpierw do Kołyski.
357. [RPG [Q2008] — krok 1 — cel zadania 1] 요람을 관찰해보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].steps[#0].goalDescription1
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [RPG [Q2008] — krok 2 — cel zadania 1] 요람에 조각을 가까이 대보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Bring the piece near the Cradle
   PL: Przyłóż Okruch blisko Kołyski
359. [RPG [Q2008] — krok 3 — cel zadania 1] 요람에 조각을 먹여보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Try feeding the piece to the Cradle
   PL: Spróbuj nakarmić Kołyskę Okruchem
360. [RPG [Q2008] — krok 4 — cel zadania 1] 요람의 아이를 구출하기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008].steps[#3].goalDescription1
   limit: do 120 znaków
   EN: Rescue the child from the Cradle
   PL: Uwolnij dziecko z Kołyski
361. [RPG [Q2008A] — tytuł] 요람에서 나온 아이에게 말 걸어보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008A].title
   limit: do 50 znaków
   EN: Talk to the child from the Cradle
   PL: Zagadaj dziecko z Kołyski
362. [RPG [Q2008A] — opis] 요람 안에서 나온 것은 작은 아이같은 형체였다. 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008A].description
   limit: do 120 znaków
   EN: What emerged from the Cradle looks like a small child. Let's try talking to them.
   PL: Z Kołyski wyłoniła się postać wyglądająca jak małe dziecko. Spróbujmy z nim porozmawiać.
363. [RPG [Q2008A] — krok 1 — cel zadania 1] 요람에서 나온 아이에게 말 걸어보기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008A].steps[#0].goalDescription1
   (powtórzenie elementu 361 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [RPG [Q2008B] — tytuł] 도망친 아이를 붙잡기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008B].title
   limit: do 40 znaków
   EN: Catch the runaway child
   PL: Złap zbiegłe dziecko
365. [RPG [Q2008B] — opis] 요람에서부터 나온 아이가 우리를 보자마자 구석으로 도망친다. 붙잡아서 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008B].description
   limit: do 140 znaków
   EN: The child from the Cradle bolted into a corner the moment they saw us. Catch up and try talking to them.
   PL: Dziecko z Kołyski rzuciło się do ucieczki, gdy tylko nas zobaczyło. Dopadnij je i spróbuj zagadać.
366. [RPG [Q2008B] — krok 1 — cel zadania 1] 요람에서 나온 것을 붙잡기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2008B].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Catch the child from the Cradle
   PL: Złap to, co wyszło z Kołyski
367. [RPG [Q2009] — tytuł] 명품관 벗어나기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2009].title
   limit: do 40 znaków
   EN: Leave the Luxury Hall
   PL: Opuść Salon Prestiżu
368. [RPG [Q2009] — opis] 요람에서 나온 아이가 우리를 따라오기 시작했다. 우리가 무서운지 거리를 두고는 있지만… 일단 명품관을 나가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2009].description
   limit: do 170 znaków
   EN: The child from the Cradle has started following us, though they still keep their distance. For now, let's leave the Luxury Hall.
   PL: Dziecko z Kołyski zaczęło iść za nami, choć wciąż trzyma dystans, jakby się nas bało… Na razie opuśćmy Salon Prestiżu.
369. [RPG [Q2009] — krok 1 — cel zadania 1] 명품관 벗어나기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2009].steps[#0].goalDescription1
   (powtórzenie elementu 367 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [RPG [Q2010] — tytuł] 4층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2010].title
   limit: do 40 znaków
   EN: Head to 4F
   PL: Udaj się na 4. piętro
371. [RPG [Q2010] — opis] 리나모비블로부터 척추 뼈를 챙겼다. 앞으로 무슨 일이 일어날지 모르니 챙겨둘 수 있는 것은 챙겨두는 편이 좋을 것 같다. 이제 이 층에서 볼일은 끝난 것 같으니 4층으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2010].description
   limit: do 250 znaków
   EN: We took the Rouge vendor's spine with us. There's no telling what will come next, so we may as well hold on to anything that could prove useful. We're done here for now. We should head to 4F.
   PL: Zabraliśmy kręgosłup L'Inamovible. Nie wiadomo, co wydarzy się dalej, więc warto zbierać wszystko, co może się przydać. Sprawy na tym piętrze wydają się skończone. Udamy się na 4. piętro.
372. [RPG [Q2010] — krok 1 — cel zadania 1] 4층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2-b.json :: dataList[key=Q2010].steps[#0].goalDescription1
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-quest-floor-2-c1
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-quest-floor-2-c1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

373. [RPG [Q2001] — tytuł] 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2-c1.json :: dataList[key=Q2001].title
   limit: do 40 znaków
   EN: Head to 2F
   PL: Udaj się na 2. piętro
374. [RPG [Q2001] — opis] 바뀌는 게 없을지라도, 우리는 계속 올라가야 했다.
   źródło: RPGSystem/rpg-loc-quest-floor-2-c1.json :: dataList[key=Q2001].description
   limit: do 120 znaków
   EN: Even if it turns out nothing's going to change, we still have to keep climbing.
   PL: Nawet jeśli nic się nie zmieni, musimy iść w górę dalej.
375. [RPG [Q2001] — krok 1 — cel zadania 1] 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2-c1.json :: dataList[key=Q2001].steps[#0].goalDescription1
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-quest-floor-2
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-quest-floor-2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

376. [RPG [Q2001] — tytuł] 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2001].title
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [RPG [Q2001] — opis] 드디어 2층에 올 수 있었다. 이곳은 붉고 어둡고 심상치 않은 분위기를 풍기는 장소다. 일단 주위를 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2001].description
   limit: do 140 znaków
   EN: We've finally reached 2F. It's dark, drenched in red, and nothing about it feels right. Let's look around.
   PL: Wreszcie dotarliśmy na 2. piętro. To miejsce jest czerwone, mroczne i przesycone grozą. Rozglądajmy się.
378. [RPG [Q2001] — krok 1 — cel zadania 1] 2층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2001].steps[#0].goalDescription1
   (powtórzenie elementu 345 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [RPG [Q2002] — tytuł] 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2002].title
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [RPG [Q2002] — opis] 플라넬과 펠트는 우리가 구해온 무기를 보고 매우 감격스러워했다. 그들은 2층 명품관에서 르루주들이 벌이고 있는 짓을 막아 달라고 부탁했다. 과연 2층에서는 공사가 끝났을까? 내려가 볼 시간이다.
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2002].description
   limit: do 270 znaków
   EN: Flannel and Felt were thrilled by the weapon we brought them. They asked us to stop whatever the Rouges are doing in the Luxury Hall on 2F. I wonder if the renovation on 2F is over yet. Time to head back down.
   PL: Flannel i Felt byli niezwykle poruszeni widząc broń, którą przynieśliśmy. Poprosili, byśmy powstrzymali Le Rouge przed tym, co robią w Salonie Prestiżu na 2. piętrze. Czy remont na 2. piętrze już się skończył? Czas zejść na dół.
381. [RPG [Q2002] — krok 1 — cel zadania 1] 2층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2002].steps[#0].goalDescription1
   (powtórzenie elementu 373 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [RPG [Q2003] — tytuł] 명품관 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2003].title
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [RPG [Q2003] — opis] 2층은 계속해서 학살이 자행되고 있었다. 명품관 입구를 막고 있는 르누아르가 우리가 가진 황금의 못을 보더니 길을 비켜주었다. 르루주가 만들고 있는 거짓 신을 없애 달라고 한다. 안에는 무엇이 있는 걸까? 명품관 안으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2003].description
   limit: do 300 znaków
   EN: The slaughter on 2F is still going on. The Noir guarding the Luxury Hall saw our Golden Nail and let us through, asking us to destroy the false god the Rouges are creating inside. We need to check what's waiting beyond the entrance.
   PL: Na 2. piętrze wciąż trwała rzeź. Le Noir strzegący wejścia do Salonu Prestiżu, zobaczywszy nasz Złoty Gwóźdź, przepuścił nas, prosząc, byśmy zniszczyli fałszywego boga, którego tworzy Le Rouge. Co czeka w środku? Wejdźmy do Salonu Prestiżu.
384. [RPG [Q2003] — krok 1 — cel zadania 1] 명품관 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2003].steps[#0].goalDescription1
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [RPG [Q2011] — tytuł] 몰려오는 르루주들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2011].title
   limit: do 40 znaków
   EN: Fend off the Rouge Onslaught
   PL: Odepchnij nawałę Le Rouge
386. [RPG [Q2011] — opis] 명품관에 있는 장막 안으로 들어가야 할 것 같다. 르누아르들을 도와 몰려오는 르루주들을 처치하고 장막을 지키고 있는 르루주 브랜드 디렉터를 없애자.
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2011].description
   limit: do 200 znaków
   EN: We need to reach the area beyond the Tabernacle. Let's help the Noirs wipe out the Rouges, then take down the Le Rouge Brand Director guarding the way.
   PL: Chyba trzeba wejść w głąb Zasłony. Pomóżmy Le Noir wytłumić nawałę Le Rouge, a potem pozbądźmy się Dyrektora Marki Le Rouge, który jej strzeże.
387. [RPG [Q2011] — krok 1 — cel zadania 1] 르루주 브랜드 디렉터 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2011].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Kill the Rouge Brand Director
   PL: Zabij Dyrektora Marki Le Rouge
388. [RPG [Q2004] — tytuł] 장막 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2004].title
   limit: do 40 znaków
   EN: Enter the Tabernacle
   PL: Wejdź za Zasłonę
389. [RPG [Q2004] — opis] 명품관을 지키고 있던 르루주들을 없앴다. 이제 뫼르소를 따라 장막 안으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2004].description
   limit: do 130 znaków
   EN: We've wiped out the Rouges guarding the Luxury Hall. Let's follow Meursault beyond the Tabernacle.
   PL: Pozbyliśmy się Le Rouge strzegących Salonu Prestiżu. Pójdźmy za Meursaultem za Zasłonę.
390. [RPG [Q2004] — krok 1 — cel zadania 1] 장막 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-2.json :: dataList[key=Q2004].steps[#0].goalDescription1
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-2] — rpg-loc-swarm-mob-floor-2-a
- obszar/warstwa: `floor-2` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-2-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

391. [RPG [swarm_lanoir_guard] — nazwa wyświetlana] 돌진하는 르누아르
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_lanoir_guard].displayName
   (powtórzenie elementu 281 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [RPG [swarm_larouge_elite] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_larouge_elite].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [RPG [swarm_larouge_sickle_sp] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_larouge_sickle_sp].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [RPG [swarm_larouge_spa_staff] — nazwa wyświetlana] 반항하는 르루주
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_larouge_spa_staff].displayName
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [RPG [swarm_renoir_contemporary] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_renoir_contemporary].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [RPG [swarm_renoir_high_domestic_2] — nazwa wyświetlana] 돌격하는 르누아르
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-2-a.json :: dataList[key=swarm_renoir_high_domestic_2].displayName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-location-floor-3
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-location-floor-3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

397. [RPG [130100] — tekst] 3층 복도
   źródło: RPGSystem/rpg-loc-location-floor-3.json :: dataList[key=130100].text
   limit: do 120 znaków
   EN: Corridor, 3F
   PL: Korytarz na 3. piętrze
398. [RPG [130200] — tekst] 르루주의 부티크
   źródło: RPGSystem/rpg-loc-location-floor-3.json :: dataList[key=130200].text
   limit: do 120 znaków
   EN: Boutique du Rouge
   PL: Boutique du Rouge
399. [RPG [130300] — tekst] 르누아르의 메종
   źródło: RPGSystem/rpg-loc-location-floor-3.json :: dataList[key=130300].text
   limit: do 120 znaków
   EN: Maison du Noir
   PL: Maison du Noir
400. [RPG [130400] — tekst] 수선실
   źródło: RPGSystem/rpg-loc-location-floor-3.json :: dataList[key=130400].text
   limit: do 120 znaków
   EN: Alteration Shop
   PL: Warsztat Poprawek
401. [RPG [130500] — tekst] 방송실
   źródło: RPGSystem/rpg-loc-location-floor-3.json :: dataList[key=130500].text
   limit: do 120 znaków
   EN: Public Address Room
   PL: Pomieszczenie Zapowiedzi

## Tryb RPG [floor-3] — rpg-loc-npc-floor-3-a-enemy
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-npc-floor-3-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

402. [RPG [N103012] — nazwa wyświetlana] 르누아르 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103012].displayName
   limit: do 50 znaków
   EN: Le Noir Sales Associate [Sunshone]
   PL: Pracownik Le Noir [Napromieniony]
403. [RPG [N103013] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103013].displayName
   limit: do 40 znaków
   EN: Mobile-Go-Spin
   PL: Wirująca Karuzela
404. [RPG [N103027] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103027].displayName
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [RPG [N103014] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103014].displayName
   limit: do 50 znaków
   EN: Le Rouge Sales Associate [Sunshone]
   PL: Pracownik Le Rouge [Napromieniony]
406. [RPG [N103015] — nazwa wyświetlana] 가죽아비
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103015].displayName
   limit: do 40 znaków
   EN: Leatherfather
   PL: Skórzany Ojciec
407. [RPG [N103016] — nazwa wyświetlana] 3층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103016].displayName
   limit: do 40 znaków
   EN: 3F Floor Manager
   PL: Kierownik 3. Piętra
408. [RPG [N103016C] — nazwa wyświetlana] 3층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-3-a-enemy.json :: dataList[key=N103016C].displayName
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-npc-floor-3-b-enemy
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-npc-floor-3-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

409. [RPG [N103019] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103019].displayName
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [RPG [N103028] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103028].displayName
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [RPG [N103014] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103014].displayName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [RPG [N103020] — nazwa wyświetlana] 가죽아비
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103020].displayName
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [RPG [N103016] — nazwa wyświetlana] 3층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103016].displayName
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [RPG [N103005] — nazwa wyświetlana] 플라넬
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103005].displayName
   limit: do 40 znaków
   EN: Flannel
   PL: Flannel
415. [RPG [N103017] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103017].displayName
   limit: do 40 znaków
   EN: Maison du Noir
   PL: Maison du Noir
416. [RPG [N103029] — nazwa wyświetlana] 펠트
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103029].displayName
   limit: do 40 znaków
   EN: Felt
   PL: Felt
417. [RPG [N103030] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103030].displayName
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [RPG [N103071] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103071].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [RPG [N103016C] — nazwa wyświetlana] 3층 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-3-b-enemy.json :: dataList[key=N103016C].displayName
   (powtórzenie elementu 407 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-npc-floor-3-b
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-npc-floor-3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

420. [RPG [N103001] — nazwa wyświetlana] 리나모비블
   źródło: RPGSystem/rpg-loc-npc-floor-3-b.json :: dataList[key=N103001].displayName
   limit: do 40 znaków
   EN: L'Inamovible
   PL: L'Inamovible
421. [RPG [N103003] — nazwa wyświetlana] 투피스
   źródło: RPGSystem/rpg-loc-npc-floor-3-b.json :: dataList[key=N103003].displayName
   limit: do 40 znaków
   EN: Two-piece
   PL: Garnitur Dzielony
422. [RPG [N103004] — nazwa wyświetlana] 수선사 아네트
   źródło: RPGSystem/rpg-loc-npc-floor-3-b.json :: dataList[key=N103004].displayName
   limit: do 40 znaków
   EN: Annette the Alterationist
   PL: Krawcowa Annette
423. [RPG [N103018] — nazwa wyświetlana] 수선사 아네트
   źródło: RPGSystem/rpg-loc-npc-floor-3-b.json :: dataList[key=N103018].displayName
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [RPG [N101008] — nazwa wyświetlana] 뒤부아
   źródło: RPGSystem/rpg-loc-npc-floor-3-b.json :: dataList[key=N101008].displayName
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-npc-floor-3-c2-enemy
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-npc-floor-3-c2-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

425. [RPG [N990001_C2] — nazwa wyświetlana] 쌓인 것
   źródło: RPGSystem/rpg-loc-npc-floor-3-c2-enemy.json :: dataList[key=N990001_C2].displayName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
426. [RPG [N990003_C2] — nazwa wyświetlana] 쌓인 것
   źródło: RPGSystem/rpg-loc-npc-floor-3-c2-enemy.json :: dataList[key=N990003_C2].displayName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-npc-floor-3
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-npc-floor-3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

427. [RPG [N103001] — nazwa wyświetlana] 리나모비블
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103001].displayName
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [RPG [N103003] — nazwa wyświetlana] 투피스
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103003].displayName
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [RPG [N103004] — nazwa wyświetlana] 수선사 아네트
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103004].displayName
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
430. [RPG [N103005] — nazwa wyświetlana] 플라넬
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103005].displayName
   (powtórzenie elementu 414 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [RPG [N103010] — nazwa wyświetlana] 이오네스코
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103010].displayName
   limit: do 40 znaków
   EN: Ionesco
   PL: Ionesco
432. [RPG [N103011] — nazwa wyświetlana] 리나모비블
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103011].displayName
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [RPG [N103017] — nazwa wyświetlana] 펠트
   źródło: RPGSystem/rpg-loc-npc-floor-3.json :: dataList[key=N103017].displayName
   (powtórzenie elementu 416 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-quest-floor-3-b
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-quest-floor-3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

434. [RPG [Q3001] — tytuł] 3층으로 올라가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3001].title
   limit: do 40 znaków
   EN: Head to 3F
   PL: Wspinaj się na 3. piętro
435. [RPG [Q3001] — opis] 역시나 2층은 이번에도 '인테리어 공사' 중이라고 한다. 빠르게 3층으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3001].description
   limit: do 120 znaków
   EN: As expected, 2F is under "renovation" again. Let's make our way to 3F.
   PL: Jak można było oczekiwać, 2. piętro znów jest w trakcie „remontu”. Szybko udamy się na 3. piętro.
436. [RPG [Q3001] — krok 1 — cel zadania 1] 3층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Get on the escalator to 3F
   PL: Wjedź schodami ruchomymi na 3. piętro
437. [RPG [Q3002] — tytuł] 가위 소리를 따라가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3002].title
   limit: do 40 znaków
   EN: Follow the Snip-snip
   PL: Pójdź za dźwiękiem nożyc
438. [RPG [Q3002] — opis] 3층으로 올라왔다. 이번에도 어김없이 가위 소리가 들린다. 수선실로 가서 아네트라는 자를 만나보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3002].description
   limit: do 150 znaków
   EN: We've reached the 3F, and sure enough, the sound of scissors is back. Head to the Alteration Shop and find Annette.
   PL: Dotarliśmy na 3. piętro. I znów słychać dźwięk nożyc. Udamy się do Warsztatu Poprawek i spotkamy się z krawcową Annette.
439. [RPG [Q3002] — krok 1 — cel zadania 1] 수선실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3002].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the Alteration Shop
   PL: Udaj się do Warsztatu Poprawek
440. [RPG [Q3004] — tytuł] 르루주의 부티크로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3004].title
   limit: do 40 znaków
   EN: Head to Boutique du Rouge
   PL: Udaj się do Boutique du Rouge
441. [RPG [Q3004] — opis] 역시나 복도를 가로막고 있는 투피스로 인해 오른쪽 매장으론 진입하기가 어렵다. 왼쪽에 있는 르루주의 부티크관으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3004].description
   limit: do 190 znaków
   EN: As expected, the Two-piece is blocking the corridor again. The store on the right is out of reach. Head to Boutique du Rouge on the left instead.
   PL: Jak zwykle Garnitur Dzielony znów zagradza drogę, przez co trudno wejść do sklepu po prawej. Udamy się na lewo, do Boutique du Rouge.
442. [RPG [Q3004] — krok 1 — cel zadania 1] 르루주의 부티크로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3004].steps[#0].goalDescription1
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [RPG [Q3005] — tytuł] 리나모비블에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3005].title
   limit: do 40 znaków
   EN: Talk to L'Inamovible
   PL: Zagadaj L'Inamovible
444. [RPG [Q3005] — opis] 이번에도 매장에는 르루주의 거인… 뫼르소 엄마의 목소리가 들려오고 있었다. 부티크의 리나모비블은 목소리가 들리지 않는 것에 무척이나 괴로워하였다. 아마 이번에도 마찬가지일 것이다. 일단 리나모비블에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3005].description
   limit: do 320 znaków
   EN: Once again, the Boutique is filled with the Voice of Le Rouge's Giant—Meursault's mother. The Boutique's vendor was deeply distressed that she couldn't hear the Voice last time, and this time will likely be no different. Let's talk to her first.
   PL: I tym razem w sklepie rozbrzmiewa głos giganta Le Rouge… matki Meursaulta. Sprzedawca Boutique bardzo cierpiał, że nie mógł usłyszeć tego głosu, i pewnie tym razem będzie podobnie. Zagadajmy najpierw L'Inamovible.
445. [RPG [Q3005] — krok 1 — cel zadania 1] 리나모비블에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3005].steps[#0].goalDescription1
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [RPG [Q3006] — tytuł] 복도로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3006].title
   limit: do 40 znaków
   EN: Head Out to the Corridor
   PL: Wyjdź na korytarz
447. [RPG [Q3006] — opis] 이전에는 괴로워만하던 리나모비블이, 우리에게 목소리가 다시 들리고 있다고 했다. 어쩌면 우리가 가지고 있던 살점 때문인지도 모른다. 그자는 우리가 수선실의 아네트를 죽이기를 원한다. 어떻게 해야 할지 아직 모르겠지만 일단 오른쪽에 있는 르누아르의 메종으로 가보자. 회의가 끝났을지도 모르니…
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3006].description
   limit: do 460 znaków
   EN: The Boutique's vendor, who could do little but suffer before, says she can hear the Voice again. It may have something to do with the piece of flesh we're carrying. This time, she wants us to kill Annette in the Alteration Shop. We're not sure what to do yet, so for now, we decided to head to Maison du Noir on the right. Maybe the "meeting" is over by now...
   PL: L'Inamovible, który wcześniej tylko cierpiał, powiedział, że znów słyszy głos. Może to za sprawą kawałka ciała, który nosimy przy sobie. On chce, byśmy zabili Annette z Warsztatu Poprawek. Nie wiemy jeszcze, co robić, ale na razie udamy się do Maison du Noir po prawej. Może „spotkanie” już się skończyło…
448. [RPG [Q3006] — krok 1 — cel zadania 1] 복도로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head out to the corridor
   PL: Wyjdź na korytarz
449. [RPG [Q3020] — tytuł] 우회해서 르누아르의 메종으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3020].title
   limit: do 50 znaków
   EN: Take a detour to Maison du Noir
   PL: Obejdź i udaj się do Maison du Noir
450. [RPG [Q3020] — opis] 이번에도 투피스가 복도를 막고 있다. 뿐만 아니라 우리가 가진 살점 조각의 존재를 눈치챈 것 같다. 투피스를 피해서 르누아르 메종으로 가보자. 르루주의 부티크 매장에 있는 방송실을 우회하면 될 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3020].description
   limit: do 270 znaków
   EN: Two-piece is blocking the corridor again, and they seem to have noticed the piece of flesh we're carrying. Find another way to Maison du Noir by going around through the Public Address Room in Boutique du Rouge.
   PL: Garnitur Dzielony znów blokuje korytarz. Poza tym chyba zwietrzył kawałek ciała, który nosimy. Obejdźmy go i udamy się do Maison du Noir drogą przez Pomieszczenie Zapowiedzi w Boutique du Rouge.
451. [RPG [Q3020] — krok 1 — cel zadania 1] 우회해서 르누아르의 메종으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3020].steps[#0].goalDescription1
   (powtórzenie elementu 449 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [RPG [Q3021] — tytuł] 르누아르 메종의 플라넬, 펠트를 처치
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3021].title
   limit: do 60 znaków
   EN: Kill Flannel and Felt at Maison du Noir
   PL: Zabij Flannela i Felta z Maison du Noir
453. [RPG [Q3022] — tytuł] 수선실로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3022].title
   limit: do 50 znaków
   EN: Return to the Alteration Shop
   PL: Wróć do Warsztatu Poprawek
454. [RPG [Q3022] — opis] 잔느의 말에 의하면 백화점의 끝은 정해져있고 다른 선택을 하는 건 아무 의미가 없다고 한다. 하지만 가만히 멈출 수는 없다. 다른 선택을 하기 위해서, 수선실로 다시 향하기로 했다.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3022].description
   limit: do 320 znaków
   EN: According to Jeanne, the Grand Magasin's ending is already set, and making other choices won't change a thing. But we can't just twiddle our thumbs and do nothing. If we're going to make a different choice, we need to head back to the Alteration Shop.
   PL: Według Jeanne koniec Grand Magasin jest już przesądzony, a inne wybory nic nie zmienią. Ale nie możemy stać w miejscu z założonymi rękami. Żeby dokonać innego wyboru, postanowiliśmy wrócić do Warsztatu Poprawek.
455. [RPG [Q3022] — krok 1 — cel zadania 1] 수선실로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3022].steps[#0].goalDescription1
   (powtórzenie elementu 453 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [RPG [Q3023] — tytuł] 수선실의 아네트를 처치
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3023].title
   limit: do 40 znaków
   EN: Kill Annette
   PL: Zabij krawcową Annette
457. [RPG [Q3024] — tytuł] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3024].title
   limit: do 40 znaków
   EN: Return to L'Inamovible
   PL: Wróć do L'Inamovible
458. [RPG [Q3024] — opis] 수선사 아네트를 처치했다. 아네트는 이젠 다시 르누아르의 편을 고를 수 없다고 경고했다. 이번엔 다른 결과를 도출할 수 있을까? 르루주 부티크의 리나모비블에게 돌아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3024].description
   limit: do 290 znaków
   EN: We defeated Annette, but not before she warned us that we had irrevocably made ourselves enemies of Le Noir. Maybe this choice will lead to a different ending this time. We should return to the vendor at Boutique du Rouge.
   PL: Pokonaliśmy Annette, ale ostrzegła, że już nigdy nie będzie mogła stanąć po stronie Le Noir. Czy tym razem wybór doprowadzi do innego zakończenia? Wróćmy do L'Inamovible z Boutique du Rouge.
459. [RPG [Q3024] — krok 1 — cel zadania 1] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3024].steps[#0].goalDescription1
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [RPG [Q3025] — tytuł] 2층으로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3025].title
   limit: do 40 znaków
   EN: Return to 2F
   PL: Wróć na 2. piętro
461. [RPG [Q3025] — opis] 리나모비블은 크게 기뻐하며 우리가 2층 명품관으로 가야 한다고 했다. 목소리라는 것이 우리를 부르고 있다 한다. 만약 고치에 있었던 그것을 강제로 끄집어 내지 않았더라면 다른 결과를 만들 수 있을까? 2층으로 다시 돌아가 보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3025].description
   limit: do 330 znaków
   EN: The Boutique's proprietress was overjoyed and told us to head for the Luxury Hall on 2F. She says the Voice is calling us there. Maybe things would have turned out differently if we hadn't forced that thing out of the cocoon last time. We should return to 2F.
   PL: L'Inamovible ucieszył się niesamowicie i kazał nam udać się do Salonu Prestiżu na 2. piętrze. Podobno głos wzywa nas tam. Może wszystko potoczyłoby się inaczej, gdybyśmy ostatnim razem nie wyciągnili tego czegoś z kokonu siłą? Wróćmy na 2. piętro.
462. [RPG [Q3025] — krok 1 — cel zadania 1] 2층으로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3025].steps[#0].goalDescription1
   (powtórzenie elementu 460 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [RPG [Q3003] — tytuł] 복도로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3003].title
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [RPG [Q3003] — opis] 지난번과는 달리 아네트는 가위를 내어주지 않았다. 이대로라면 복도를 막고 있는 마네킹을 처치하기 어려울텐데… 이번에도 투피스가 복도를 막고 있는지 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3003].description
   limit: do 280 znaków
   EN: Unlike last time, Annette refused to hand over the scissors. Without them, dealing with the Mannequin blocking the corridor may prove difficult. We need to check whether Two-piece is still guarding the way this time.
   PL: Tym razem Annette nie oddała nam nożyc. Bez nich trudno będzie poradzić sobie z manekinem zagradzającym korytarz… Sprawdźmy, czy Garnitur Dzielony znów blokuje przejście.
465. [RPG [Q3003] — krok 1 — cel zadania 1] 복도로 나가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3003].steps[#0].goalDescription1
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [RPG [Q3026] — tytuł] 3층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3026].title
   limit: do 40 znaków
   EN: Head to 3F
   PL: Udaj się na 3. piętro
467. [RPG [Q3026] — opis] 이번에는 르루주를 돕기로 결정한 만큼 그들에게 협조를 하는 쪽으로 행동하기로 했다. 목소리를 간절히 기다렸던 3층의 리나모비블에게 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3026].description
   limit: do 240 znaków
   EN: This time, we've chosen to side with Le Rouge, so we'll have to act accordingly. We should go to Boutique du Rouge's vendor on 3F, who has been waiting desperately to hear the Voice again.
   PL: Tym razem zdecydowaliśmy się stanąć po stronie Le Rouge, więc będziemy z nimi współpracować. Udamy się do L'Inamovible z 3. piętra, który gorączkowo czeka na ponowne usłyszenie głosu.
468. [RPG [Q3026] — krok 1 — cel zadania 1] 3층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3026].steps[#0].goalDescription1
   (powtórzenie elementu 466 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [RPG [Q3027] — tytuł] 리나모비블에게 아이를 보여주기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3027].title
   limit: do 50 znaków
   EN: Show the child to L'Inamovible
   PL: Pokaż dziecko L'Inamovible
470. [RPG [Q3027] — opis] 3층에 도착했다. 리나모비블에게 아이를 보여주자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3027].description
   limit: do 120 znaków
   EN: We've arrived at 3F. Let's show the child to Boutique du Rouge's vendor.
   PL: Dotarliśmy na 3. piętro. Pokażmy dziecko L'Inamovible.
471. [RPG [Q3027] — krok 1 — cel zadania 1] 리나모비블에게 아이를 보여주기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3027].steps[#0].goalDescription1
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [RPG [Q3028] — tytuł] 리나모비블의 잔해 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3028].title
   limit: do 50 znaków
   EN: Inspect L'Inamovible's remains
   PL: Przejrzyj szczątki L'Inamovible
473. [RPG [Q3028] — opis] 리나모비블은 아이에게 손수건을 건네주었고 아이가 그것을 받아들자마자 눈앞에서 터져버렸다. 잔해로부터 못으로 쓸 수 있는 것을 얻을 수 있는지 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3028].description
   limit: do 240 znaków
   EN: The proprietress of the Boutique handed the child a handkerchief, and the moment it was accepted, she burst apart before our eyes. Search the remains for something we can use as a Nail.
   PL: L'Inamovible podał dziecku chusteczkę, a gdy je przyjęło, wybuchł nam na oczach. Przejrzyjmy szczątki, czy nie da się z nich zrobić gwóździa.
474. [RPG [Q3028] — krok 1 — cel zadania 1] 리나모비블의 잔해 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-3-b.json :: dataList[key=Q3028].steps[#0].goalDescription1
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-quest-floor-3
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-quest-floor-3.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

475. [RPG [Q3001] — tytuł] 3층으로 올라가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3001].title
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [RPG [Q3001] — opis] 2층은 '공사' 중이라고 한다. 아무리 봐도 평범한 공사로는 보이지 않지만, 지금 들어갈 수는 없을 것 같다. 에스컬레이터를 타고 3층으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3001].description
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 2F is currently "undergoing renovations." Now matter how you cut it, it didn't look like your average construction project. \n\nSince we can't explore the floor anyway, perhaps we should get on the escalator and check out 3F first.
   PL: 2. piętro podobno jest „w trakcie remontu”. Cokolwiek by o tym myśleć, nie wygląda to jak zwykły remont, a teraz i tak nie można wejść do środka. Wjedźmy schodami ruchomymi na 3. piętro.
477. [RPG [Q3001] — krok 1 — cel zadania 1] 3층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3001].steps[#0].goalDescription1
   (powtórzenie elementu 436 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [RPG [Q3002] — tytuł] 가위 소리를 따라가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3002].title
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [RPG [Q3002] — opis] 3층으로 올라왔다. 어딘가에서 가위질 소리가 들려온다. 소리를 따라서 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3002].description
   limit: do 160 znaków
   EN: We're on 3F. What sounds like a distant pair of scissors are going snip-snip. Let's see where that sound's coming from.
   PL: Dotarliśmy na 3. piętro. Skądś dochodzi dźwięk cięcia nożycami. Pójdźmy za tym dźwiękiem.
480. [RPG [Q3002] — krok 1 — cel zadania 1] 가위질 소리를 따라 위쪽으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3002].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Follow the snip-snip and explore the area to the top
   PL: Pójdź za dźwiękiem nożyc w górę
481. [RPG [Q3003] — tytuł] 복도로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3003].title
   limit: do 40 znaków
   EN: Head to the Corridor
   PL: Udaj się na korytarz
482. [RPG [Q3003] — opis] 수선사 아네트를 만났다. 언젠가 원단을 만들 일이 있을 때 부탁해보면 좋을 것 같다. 이제 수선실을 나가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3003].description
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We met Annette the Alterationist. I suppose she'll come in handy if we ever need a bundle of fabric woven.\nFor now, time to leave.
   PL: Poznaliśmy krawcową Annette. Przyda się, gdy kiedyś będziemy potrzebować utkać tkaninę. A teraz czas wyjść z Warsztatu Poprawek.
483. [RPG [Q3003] — krok 1 — cel zadania 1] 수선실을 나와서 복도로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3003].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Leave the Alteration Shop and head back to the corridor
   PL: Wyjdź z Warsztatu Poprawek i udaj się na korytarz
484. [RPG [Q3004] — tytuł] 3층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3004].title
   limit: do 40 znaków
   EN: Explore 3F
   PL: Rozejrzyj się po 3. piętrze
485. [RPG [Q3004] — opis] 안타깝게도 투피스들에게는 말이 통하지 않았다. 일단 다른 곳을 먼저 둘러보도록 하자. 왼쪽에 있는 매장으로 가보는 게 좋을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3004].description
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sadly, we weren't able to get through to Two-piece. Or is it Two-pieces?\n\nAnyways, let's explore the remaining areas first. That store to the left, for example.
   PL: Niestety z Garniturem Dzielonym nie dało się dogadać. Najpierw rozejrzyjmy się gdzie indziej. Dobrym pomysłem będzie sklep po lewej.
486. [RPG [Q3004] — krok 1 — cel zadania 1] 왼쪽에 있는 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3004].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the store on the left
   PL: Udaj się do sklepu po lewej
487. [RPG [Q3005] — tytuł] 부티크의 르루주에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3005].title
   limit: do 50 znaków
   EN: Talk to the Rouge at the Boutique
   PL: Zagadaj Le Rouge z Boutique
488. [RPG [Q3005] — opis] 부티크라는 곳에 왔다. 매장 어딘가에서는 거인으로 추정되는 목소리가 계속해서 들려온다. 매장의 직원에게 말을 걸어보는 편이 좋을 것 같다.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3005].description
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We found ourselves inside a store called the "Boutique." A disembodied voice, probably belonging to a "Giant," constantly recites a mantra throughout the store.\nLet's talk to the vendor and see if there's anything more we could learn about this place.
   PL: Trafiliśmy do sklepu zwanego „Boutique”. Gdzieś w sklepie wciąż rozbrzmiewa głos, który należy do jakiegoś „Giganta”. Porozmawiajmy ze sprzedawcą i dowiedzmy się, co można o tym miejscu wiedzieć.
489. [RPG [Q3005] — krok 1 — cel zadania 1] 르루주 부티크 직원에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3005].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to the employee at Boutique du Rouge
   PL: Zagadaj pracownika Boutique du Rouge
490. [RPG [Q3006] — tytuł] 방송실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3006].title
   limit: do 40 znaków
   EN: Head to the PA Room
   PL: Udaj się do Pomieszczenia Zapowiedzi
491. [RPG [Q3006] — opis] 리나모비블이라는 르루주는 목소리가 같은 말을 반복한다는 것에 괴로워하고 있었다. 그자는 우리에게 방송실에 가서 왜 목소리가 계속 반복되는지에 대한 이유를 알아오길 원한다. 목소리의 주인은 죽은 뫼르소의 엄마였다. 하지만 우리는 그자의 부탁을 들어주기 위해 방송실로 향하기로 했다.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3006].description
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Rouge vendor looks distraught that the "Voice" would only repeat what it had said before and wants to know why.\nBut the Voice's identity is Meursault's mother, who'd already passed away... Still, we decided to head to the PA Room as asked.
   PL: Sprzedawca z Boutique du Rouge rozpacza, że głos wciąż powtarza to samo, i chce się dowiedzieć dlaczego. Ale tożsamością głosu okazała się matka Meursaulta, która już nie żyje… Mimo to postanowiliśmy, na jego prośbę, udać się do Pomieszczenia Zapowiedzi.
492. [RPG [Q3006] — krok 1 — cel zadania 1] 방송실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3006].steps[#0].goalDescription1
   (powtórzenie elementu 490 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [RPG [Q3007] — tytuł] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3007].title
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [RPG [Q3007] — opis] 3층 플로어 매니저로부터 방송실 테이프를 얻었다. 이 테이프에 거인의 목소리가 녹음되어 있었던 걸까? 르루주의 부티크로 돌아간 뒤 리나모비블에게 전해주자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3007].description
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Received a PA Room Audiotape from the 3F Floor Manager. Maybe this tape contains the Giant's voice?\n\nTime to return to Boutique du Rouge and hand this over to the vendor.
   PL: Otrzymaliśmy od Kierownika 3. Piętra taśmę z Pomieszczenia Zapowiedzi. Może na tej taśmie zapisany jest głos Giganta? Wróćmy do Boutique du Rouge i przekażmy ją L'Inamovible.
495. [RPG [Q3007] — krok 1 — cel zadania 1] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3007].steps[#0].goalDescription1
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [RPG [Q3008] — tytuł] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3008].title
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [RPG [Q3008] — opis] 3층 플로어 매니저로부터 방송실 테이프를 얻었다. 이 테이프에 거인의 목소리가 녹음되어 있었던 걸까? 르루주의 부티크로 돌아간 뒤 리나모비블에게 전해주자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3008].description
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [RPG [Q3008] — krok 1 — cel zadania 1] 리나모비블에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3008].steps[#0].goalDescription1
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [RPG [Q3009] — tytuł] 투피스에게 말을 걸어보기 2
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3009].title
   limit: do 40 znaków
   EN: Talk to Two-piece (2)
   PL: Zagadaj Garnitur Dzielony (2)
500. [RPG [Q3009] — opis] 이쯤 되면 회의가 끝나지 않았을까? 오른쪽 복도를 막고 있었던 투피스에게 돌아가서 다시 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3009].description
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Okay, their "meeting" should be over by now. I hope.\nLet's return to Two-piece blocking the corridor to the right and find out.
   PL: Najwyższy czas, by „spotkanie” się skończyło, nie? Wróćmy do Garnituru Dzielonego blokującego korytarz po prawej i się przekonajmy.
501. [RPG [Q3009] — krok 1 — cel zadania 1] 복도의 투피스에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3009].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to Two-piece in the corridor
   PL: Zagadaj Garnitur Dzielony na korytarzu
502. [RPG [Q3010] — tytuł] 수선실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3010].title
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [RPG [Q3010] — opis] 회의는 아직 끝나지 않았고 언제 끝날지 알 수 없어 보인다. 오티스와 싱클레어가 눈빛을 교환한 후 수선실로 가자고 제안한다. 뭔가 좋은 계획이 생긴 모양이다.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3010].description
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The meeting is still underway with no signs of ever adjourning.\nOutis and Sinclair exchanged a look, then suggested that we head to the Alteration Shop... Maybe they've come up with a plan?
   PL: Spotkanie wciąż trwa i nie widać, by miało się kiedyś skończyć. Outis i Sinclair wymienili spojrzenia, po czym zasugerowali wypad do Warsztatu Poprawek… Chyba mają jakiś plan?
504. [RPG [Q3010] — krok 1 — cel zadania 1] 수선실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3010].steps[#0].goalDescription1
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
505. [RPG [Q3012] — tytuł] 오른쪽으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3012].title
   limit: do 40 znaków
   EN: Head to the Right
   PL: Udaj się na prawo
506. [RPG [Q3012] — opis] 아네트의 말대로 정말 날이 잘 든 가위였다. 길을 막고 있던 투피스들은 깔끔하게 분리되었다. 이제 오른쪽으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3012].description
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Like Annette said, the scissors were well-sharpened, and managed to snip-snip the Two-piece into two-pieces.\nLet's explore what's behind them.
   PL: Annette miała rację: nożyczki były naprawdę ostre, i Garnitur Dzielony rozpadł się na dwie połowy. Zobaczmy, co jest za nimi.
507. [RPG [Q3012] — krok 1 — cel zadania 1] 오른쪽에 있는 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3012].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the store on the right
   PL: Udaj się do sklepu po prawej
508. [RPG [Q3013] — tytuł] 홀려버린 르누아르들을 없애기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3013].title
   limit: do 40 znaków
   EN: Eliminate Enthralled Noirs
   PL: Usuń Oczarowanych Le Noir
509. [RPG [Q3013] — opis] 르누아르의 메종으로 향했다. 플라넬과 펠트라는 르누아르들은 자신의 브랜드를 격상시키기 위해 다른 목소리에 홀려버린 르누아르들을 치워 달라고 부탁했다. 홀려버린 르누아르 세 명 정도를 없앤 후 다시 이들에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3013].description
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Made it to Maison du Noir.\nFlannel and Felt, two Noirs managing the store, want to "premiumize" their brand and asked us to remove a few Noirs who were enthralled by a foreign Voice.\nWe should talk to them after removing a few enthralled Noirs—about 3 should do.
   PL: Dotarliśmy do Maison du Noir. Flannel i Felt, dwóch Le Noir prowadzących sklep, chcą „podnieść prestiż” swojej marki i poprosili nas o pozbycie się kilku Le Noir, które zaczarował obcy Głos. Po usunięciu około trzech Oczarowanych Le Noir wróćmy do nich, by porozmawiać.
510. [RPG [Q3013] — krok 1 — cel zadania 1] 홀려버린 르누아르 3명 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3013].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Eliminate 3 enthralled Noirs
   PL: Usuń 3 Oczarowanych Le Noir
511. [RPG [Q3013] — krok 2 — cel zadania 1] 플라넬과 펠트에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3013].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Return to Flannel and Felt
   PL: Wróć do Flannela i Felta
512. [RPG [Q3011] — tytuł] 가위를 사서 회의를 끝내기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3011].title
   limit: do 70 znaków
   EN: Purchase a Pair of Scissors and Adjourn the Meeting
   PL: Kup nożyczki i zakończ spotkanie
513. [RPG [Q3011] — opis] 수선사 아네트로부터 가위를 살 수 있을 것 같다. '날이 잘 든 재봉 가위'를 구매한 후 투피스에게 다시 가보자. 오티스와 싱클레어가 만족스럽다는 듯이 씩 웃는다. 설마 이걸로…?
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3011].description
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Annette the Alterationist was selling a few pairs of scissors, last I recall.\nLet's purchase a pair of "Well-sharpened Sewing Scissors" and head back to Two-piece.\nOutis and Sinclair are both wearing the same strange, self-satisfied grin on their faces.\n\nWait, are they planning to—?
   PL: Chyba krawcowa Annette sprzedawała kilka par nożyc. Kupmy „Ostre Nożyczki Krawieckie” i wróćmy do Garnituru Dzielonego. Outis i Sinclair wymieniają zadowolone, dziwne uśmiechy. Czyżby to miało być to…?
514. [RPG [Q3011] — krok 1 — cel zadania 1] 수선사 아네트로부터 날이 잘 든 재봉 가위를 구매하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3011].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Purchase a pair of "Well-sharpened Sewing Scissors" from Annette the Alterationist
   PL: Kup „Ostre Nożyczki Krawieckie” od krawcowej Annette
515. [RPG [Q3011] — krok 2 — cel zadania 1] 복도의 투피스에게 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3011].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Return to Two-piece in the corridor
   PL: Wróć do Garnituru Dzielonego na korytarzu
516. [RPG [Q4014] — tytuł] 르누아르들에게 정보 전달해주기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4014].title
   limit: do 40 znaków
   EN: Bring the Noirs up to Speed
   PL: Przekaż Le Noir informacje
517. [RPG [Q4014] — opis] 행복한 옷장의 잔해로부터 '황금원단과 못'에 대해 적혀있는 레시피를 얻었다. 이게 원레그가 말했던 무기일지도 모르겠다. 정보를 전해주기 위해 4층의 르누아르 신발관 직원 원레그에게 대화를 한 후, 3층의 메종 직원 플라넬과 펠트에게 돌아가자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4014].description
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A note we found in the Happy Closet's remains said something about "Golden Fabric" and "Nail." Maybe this is the recipe to crafting that legendary weapon that One-leg mentioned?\nLet's bring this back to that One-leg in the 4F Noir Footwear Hall as promised, then return to Flannel and Felt at Maison du Noir on 3F.
   PL: Ze szczątków Szczęśliwej Szafy uzyskaliśmy przepis opisujący „Złotą Tkaninę i Gwóźdź”. Chyba to jest broń, o której mówiła Surowa Noga? Przekażmy zgodnie z obietnicą te informacje Surowej Nodze, pracownikowi Salonu Obuwia Le Noir na 4. piętrze, a potem wróćmy do Flannela i Felta z Maison du Noir na 3. piętrze.
518. [RPG [Q4014] — krok 1 — cel zadania 1] 떠나기 전, 등굽은 조명에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4014].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to the Arc Floor Lamp before leaving
   PL: Przed wyjściem zagadaj Lampę Łukową
519. [RPG [Q4014] — krok 2 — cel zadania 1] 4층의 르누아르 신발관에 있는 원레그에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4014].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Talk to the One-leg in the 4F Noir Footwear Hall
   PL: Zagadaj Surową Nogę w Salonie Obuwia Le Noir na 4. piętrze
520. [RPG [Q4014] — krok 3 — cel zadania 1] 3층의 르누아르 메종에 있는 플라넬에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4014].steps[#2].goalDescription1
   limit: do 120 znaków
   EN: Talk to Flannel in the 3F Maison du Noir
   PL: Zagadaj Flannela w Maison du Noir na 3. piętrze
521. [RPG [Q4015] — tytuł] 수선실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4015].title
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
522. [RPG [Q4015] — opis] 3층으로 다시 올라왔다. 수선실에 있는 아네트에게 황금 실타래를 갖다준다면 황금원단을 만들어줄 수 있을 것이다.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4015].description
   limit: do 170 znaków
   EN: We're back on 3F. Let's bring the Golden Skein back to Annette the Alterationist, and she'll weave a Golden Fabric out of it.
   PL: Znowu jesteśmy na 3. piętrze. Jeśli przyniesiemy krawcowej Annette Złotą Przędzę, utka z niej Złotą Tkaninę.
523. [RPG [Q4015] — krok 1 — cel zadania 1] 수선실로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4015].steps[#0].goalDescription1
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [RPG [Q4017] — tytuł] 르루주의 부티크로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4017].title
   (powtórzenie elementu 440 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [RPG [Q4017] — opis] 수선사 아네트가 황금원단을 만들어주었다. 이제 못을 얻어야 한다. 못은 부티크의 르루주인 리나모비블로부터 얻을 수 있을 것 같다. 정확히는 그자의 척추라고 했지만…
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4017].description
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Received the Golden Fabric from Annette the Alterationist... Now, to obtain the Nail.\nWe should be able to get the "Nail"—or, as the Noirs said, the "spine"—from Boutique du Rouge.
   PL: Krawcowa Annette utkała nam Złotą Tkaninę. Teraz trzeba zdobyć gwóźdź. Podobno dostaniemy go od L'Inamovible, Le Rouge z Boutique. A właściwie: to ma być jego kręgosłup…
526. [RPG [Q4017] — krok 1 — cel zadania 1] 리나모비블에게 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4017].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Return to L'Inamovible
   PL: Udaj się do L'Inamovible
527. [RPG [Q4016] — tytuł] 못을 얻고 르누아르의 메종으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4016].title
   limit: do 70 znaków
   EN: Obtain the "Nail" and Return to Maison du Noir
   PL: Zdobądź „Gwóźdź” i udaj się do Maison du Noir
528. [RPG [Q4016] — opis] 괴로워하며 뒤틀림이 심해진 리나모비블을 처치했다. 이제 그자로부터 척추… 이자 못을 뽑아내야 한다. 못에 황금원단을 두르면 어떤 옷감이든 찢을 수 있는 르누아르의 무기를 완성할 수 있을 것이다. 플라넬과 펠트가 있었던 르누아르의 메종으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4016].description
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Rouge vendor's Distortion quickly exacerbated before our eyes, so we had to cut her down.\nTime to remove her spi—"Nail."\nNow, we only need to drape the Golden Fabric around the nail to complete the legendary weapon of the Noirs, capable of ripping through any and all fabric.\n\nTime to return to Maison du Noir and deliver the news to Flannel and Felt.
   PL: Pozbiliśmy L'Inamovible, którego Wypaczenie gwałtownie postępowało. Teraz trzeba wyciągnąć z niego kręgosłup… to znaczy „Gwóźdź”. Gdy owiniemy Złotą Tkaninę wokół gwóździa, powstanie legendarna broń Le Noir, zdolna poderwać każdą tkaninę. Udamy się do Maison du Noir, gdzie czekają Flannel i Felt, i przekażmy im wiadomość.
529. [RPG [Q4016] — krok 1 — cel zadania 1] 리나모비블의 잔해로부터 못을 얻기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4016].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Obtain the "Nail" from L'Inamovible's remains
   PL: Zdobądź „Gwóźdź” ze szczątków L'Inamovible
530. [RPG [Q4016] — krok 2 — cel zadania 1] 르누아르의 메종으로 가기
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q4016].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Return to Maison du Noir
   PL: Udaj się do Maison du Noir
531. [RPG [Q3016H1] — opis] 0901
   źródło: RPGSystem/rpg-loc-quest-floor-3.json :: dataList[key=Q3016H1].description
   limit: do 120 znaków
   EN: 0901
   PL: 0901

## Tryb RPG [floor-3] — rpg-loc-swarm-mob-floor-3-a
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-3-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

532. [RPG [swarm_lanoir_fanatic_3f] — nazwa wyświetlana] 르누아르 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-a.json :: dataList[key=swarm_lanoir_fanatic_3f].displayName
   (powtórzenie elementu 402 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [RPG [swarm_larouge_spa_staff_3f] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-a.json :: dataList[key=swarm_larouge_spa_staff_3f].displayName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [RPG [swarm_leather_scarecrow] — nazwa wyświetlana] 가죽아비
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-a.json :: dataList[key=swarm_leather_scarecrow].displayName
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [RPG [swarm_star] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-a.json :: dataList[key=swarm_star].displayName
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-3] — rpg-loc-swarm-mob-floor-3-b
- obszar/warstwa: `floor-3` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-3-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

536. [RPG [swarm_larouge_spa_staff_3f] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-b.json :: dataList[key=swarm_larouge_spa_staff_3f].displayName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [RPG [swarm_leather_scarecrow] — nazwa wyświetlana] 가죽아비
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-b.json :: dataList[key=swarm_leather_scarecrow].displayName
   (powtórzenie elementu 406 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [RPG [swarm_star] — nazwa wyświetlana] 빙글 모빌
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-3-b.json :: dataList[key=swarm_star].displayName
   (powtórzenie elementu 403 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-location-floor-4-b
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-location-floor-4-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

539. [RPG [140500] — tekst] 르누아르 가방관
   źródło: RPGSystem/rpg-loc-location-floor-4-b.json :: dataList[key=140500].text
   limit: do 120 znaków
   EN: Le Noir Handbags Hall
   PL: Salon Torebek Le Noir
540. [RPG [140600] — tekst] 르루주 가방관
   źródło: RPGSystem/rpg-loc-location-floor-4-b.json :: dataList[key=140600].text
   limit: do 120 znaków
   EN: Le Rouge Handbags Hall
   PL: Salon Torebek Le Rouge
541. [RPG [140700] — tekst] 미아 보호소
   źródło: RPGSystem/rpg-loc-location-floor-4-b.json :: dataList[key=140700].text
   limit: do 120 znaków
   EN: Lost Child Center
   PL: Przytułek Zagubionych Dzieci
542. [RPG [140800] — tekst] 미아 보호소 안쪽
   źródło: RPGSystem/rpg-loc-location-floor-4-b.json :: dataList[key=140800].text
   limit: do 120 znaków
   EN: Interior, Lost Child Center
   PL: Wnętrze Przytułku Zagubionych Dzieci

## Tryb RPG [floor-4] — rpg-loc-location-floor-4-c2
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-location-floor-4-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

543. [RPG [140500] — tekst] 르누아르 가방관
   źródło: RPGSystem/rpg-loc-location-floor-4-c2.json :: dataList[key=140500].text
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [RPG [140600] — tekst] 르루주 가방관
   źródło: RPGSystem/rpg-loc-location-floor-4-c2.json :: dataList[key=140600].text
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-location-floor-4
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-location-floor-4.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

545. [RPG [140100] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-4.json :: dataList[key=140100].text
   limit: do 120 znaków
   EN: Corridor
   PL: Korytarz
546. [RPG [140200] — tekst] 신발관
   źródło: RPGSystem/rpg-loc-location-floor-4.json :: dataList[key=140200].text
   limit: do 120 znaków
   EN: Footwear Hall
   PL: Salon Obuwia
547. [RPG [140300] — tekst] 가구관
   źródło: RPGSystem/rpg-loc-location-floor-4.json :: dataList[key=140300].text
   limit: do 120 znaków
   EN: Furniture Hall
   PL: Salon Mebli
548. [RPG [140400] — tekst] 에스컬레이터
   źródło: RPGSystem/rpg-loc-location-floor-4.json :: dataList[key=140400].text
   limit: do 120 znaków
   EN: Escalator
   PL: Schody ruchome

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4-a-enemy
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

549. [RPG [N104001] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-a-enemy.json :: dataList[key=N104001].displayName
   limit: do 40 znaków
   EN: Rattling Drawer
   PL: Trzaskająca Szuflada
550. [RPG [N104007] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-a-enemy.json :: dataList[key=N104007].displayName
   limit: do 40 znaków
   EN: Creaking Drawer
   PL: Skrzypiąca Szuflada
551. [RPG [N104008] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-a-enemy.json :: dataList[key=N104008].displayName
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
552. [RPG [N104014] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-a-enemy.json :: dataList[key=N104014].displayName
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4-b-enemy
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

553. [RPG [N104001] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104001].displayName
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [RPG [N104007] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104007].displayName
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [RPG [N104008] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104008].displayName
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [RPG [N104014] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104014].displayName
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
557. [RPG [N104029] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104029].displayName
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [RPG [N104030] — nazwa wyświetlana] 르네
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104030].displayName
   limit: do 40 znaków
   EN: Renée
   PL: Renée
559. [RPG [N104034] — nazwa wyświetlana] 황금 꽁지 가방
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104034].displayName
   limit: do 40 znaków
   EN: Golden-tailed Handbag
   PL: Torebka ze Złotym Ogonkiem
560. [RPG [N104035] — nazwa wyświetlana] 황금 눈 가방
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104035].displayName
   limit: do 40 znaków
   EN: Golden-eyed Handbag
   PL: Torebka ze Złotym Okiem
561. [RPG [N104036] — nazwa wyświetlana] 황금 수염 가방
   źródło: RPGSystem/rpg-loc-npc-floor-4-b-enemy.json :: dataList[key=N104036].displayName
   limit: do 40 znaków
   EN: Golden-whiskered Handbag
   PL: Torebka ze Złotymi Wąsami

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4-b
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

562. [RPG [N104010] — nazwa wyświetlana] 르누아르 신발관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104010].displayName
   limit: do 60 znaków
   EN: Le Noir Footwear Hall Sales Associate
   PL: Pracownik Salonu Obuwia Le Noir
563. [RPG [N104012] — nazwa wyświetlana] 포레그
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104012].displayName
   limit: do 40 znaków
   EN: Four-legs
   PL: Czteronogi
564. [RPG [N104011] — nazwa wyświetlana] 원레그
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104011].displayName
   limit: do 40 znaków
   EN: One-leg
   PL: Surowa Noga
565. [RPG [N104009] — nazwa wyświetlana] 도로테아
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104009].displayName
   limit: do 40 znaków
   EN: Dorothea
   PL: Dorothea
566. [RPG [N104013] — nazwa wyświetlana] 코제트
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104013].displayName
   limit: do 40 znaków
   EN: Cosette
   PL: Cosette
567. [RPG [N104005] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104005].displayName
   limit: do 40 znaków
   EN: Skinhide Couch
   PL: Sofa ze Skóry
568. [RPG [N104003] — nazwa wyświetlana] 등굽은 조명
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104003].displayName
   limit: do 40 znaków
   EN: Arc Floor Lamp
   PL: Lampa Łukowa
569. [RPG [N104002] — nazwa wyświetlana] 뼛걸이
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104002].displayName
   limit: do 40 znaków
   EN: Bonehanger
   PL: Kościany Wieszak
570. [RPG [N104004] — nazwa wyświetlana] 박제된 가죽 커튼
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104004].displayName
   limit: do 40 znaków
   EN: Taxidermied Leather Curtain
   PL: Wypchana Skórzana Kurtyna
571. [RPG [N104006] — nazwa wyświetlana] 행복한 옷장
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104006].displayName
   limit: do 40 znaków
   EN: Happy Closet
   PL: Szczęśliwa Szafa
572. [RPG [N101028] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N101028].displayName
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [RPG [N101029] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N101029].displayName
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [RPG [N104015] — nazwa wyświetlana] 쌍둥이 램프
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104015].displayName
   limit: do 40 znaków
   EN: Lamp Twin
   PL: Lampa-Bliźniak
575. [RPG [N104016] — nazwa wyświetlana] 빨간 방석 스툴
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104016].displayName
   limit: do 40 znaków
   EN: Red-cushioned Stool
   PL: Taboret z Czerwonym Gąbkiem
576. [RPG [N104017] — nazwa wyświetlana] 느긋한 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104017].displayName
   limit: do 40 znaków
   EN: Mellow Leather Bed
   PL: Spokojne Skórzane Łóżko
577. [RPG [N104018] — nazwa wyświetlana] 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104018].displayName
   limit: do 40 znaków
   EN: Leather Bed
   PL: Skórzane Łóżko
578. [RPG [N104019] — nazwa wyświetlana] 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104019].displayName
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [RPG [N104020] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104020].displayName
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [RPG [N104021] — nazwa wyświetlana] 빨간 방석 스툴
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104021].displayName
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [RPG [N104022] — nazwa wyświetlana] 길쭉 램프
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104022].displayName
   limit: do 40 znaków
   EN: Longshank Lamp
   PL: Wydłużona Lampa
582. [RPG [N104023] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104023].displayName
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [RPG [N104024] — nazwa wyświetlana] 르누아르 가방관 디자이너
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104024].displayName
   limit: do 50 znaków
   EN: Le Noir Handbags Hall Designer
   PL: Projektant Salonu Torebek Le Noir
584. [RPG [N104025] — nazwa wyświetlana] 르네
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104025].displayName
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [RPG [N104026] — nazwa wyświetlana] 르루주 가방관 디자이너
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104026].displayName
   limit: do 50 znaków
   EN: Le Rouge Handbags Hall Designer
   PL: Projektant Salonu Torebek Le Rouge
586. [RPG [N104031] — nazwa wyświetlana] 디자이너의 걸작
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104031].displayName
   limit: do 40 znaków
   EN: The Designer's Chef D'oeuvre
   PL: Dzieło Projektanta
587. [RPG [N104032] — nazwa wyświetlana] 디자이너의 걸작
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104032].displayName
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [RPG [N104033] — nazwa wyświetlana] 디자이너의 걸작
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104033].displayName
   (powtórzenie elementu 586 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [RPG [N104037] — nazwa wyświetlana] ???의 알
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104037].displayName
   limit: do 40 znaków
   EN: ???'s Egg
   PL: Jajo ???
590. [RPG [N104038] — nazwa wyświetlana] 부서진 가구
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104038].displayName
   limit: do 40 znaków
   EN: Destroyed Furnishing
   PL: Zniszczony Mebel
591. [RPG [N104041] — nazwa wyświetlana] 부서진 뼛걸이
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104041].displayName
   limit: do 40 znaków
   EN: Destroyed Bonehanger
   PL: Zniszczony Kościany Wieszak
592. [RPG [N104042] — nazwa wyświetlana] 부서진 느긋한 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104042].displayName
   limit: do 40 znaków
   EN: Destroyed Mellow Leather Bed
   PL: Zniszczone Spokojne Skórzane Łóżko
593. [RPG [N104043] — nazwa wyświetlana] 부서진 박제된 가죽 커튼
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104043].displayName
   limit: do 60 znaków
   EN: Destroyed Taxidermied Leather Curtain
   PL: Zniszczona Wypchana Skórzana Kurtyna
594. [RPG [N104044] — nazwa wyświetlana] 부서진 빨간 방석 스툴
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104044].displayName
   limit: do 50 znaków
   EN: Destroyed Red-cushioned Stool
   PL: Zniszczony Taboret z Czerwonym Gąbkiem
595. [RPG [N104045] — nazwa wyświetlana] 부서진 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104045].displayName
   limit: do 40 znaków
   EN: Destroyed Skinhide Couch
   PL: Zniszczona Sofa ze Skóry
596. [RPG [N104046] — nazwa wyświetlana] 부서진 쌍둥이 램프
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104046].displayName
   limit: do 40 znaków
   EN: Destroyed Lamp Twin
   PL: Zniszczona Lampa-Bliźniak
597. [RPG [N104039] — nazwa wyświetlana] 도로테아
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104039].displayName
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [RPG [N104040] — nazwa wyświetlana] ???의 잔해
   źródło: RPGSystem/rpg-loc-npc-floor-4-b.json :: dataList[key=N104040].displayName
   limit: do 40 znaków
   EN: ???'s Remains
   PL: Szczątki ???

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4-c2-enemy
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4-c2-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

599. [RPG [N990001_C2] — nazwa wyświetlana] 쌓인 것
   źródło: RPGSystem/rpg-loc-npc-floor-4-c2-enemy.json :: dataList[key=N990001_C2].displayName
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4-c2
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

600. [RPG [N10201] — nazwa wyświetlana] 르네앙
   źródło: RPGSystem/rpg-loc-npc-floor-4-c2.json :: dataList[key=N10201].displayName
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [RPG [N10202] — nazwa wyświetlana] 르네
   źródło: RPGSystem/rpg-loc-npc-floor-4-c2.json :: dataList[key=N10202].displayName
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-npc-floor-4
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-npc-floor-4.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

602. [RPG [N104010] — nazwa wyświetlana] ???
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104010].displayName
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [RPG [N104012] — nazwa wyświetlana] 포레그
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104012].displayName
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [RPG [N104011] — nazwa wyświetlana] 원레그
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104011].displayName
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [RPG [N104009] — nazwa wyświetlana] 도로테아
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104009].displayName
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [RPG [N104013] — nazwa wyświetlana] 코제트
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104013].displayName
   (powtórzenie elementu 566 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [RPG [N104005] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104005].displayName
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [RPG [N104003] — nazwa wyświetlana] 등굽은 조명
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104003].displayName
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [RPG [N104002] — nazwa wyświetlana] 뼛걸이
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104002].displayName
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [RPG [N104004] — nazwa wyświetlana] 박제된 가죽 커튼
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104004].displayName
   (powtórzenie elementu 570 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [RPG [N104006] — nazwa wyświetlana] 행복한 옷장
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104006].displayName
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [RPG [N101028] — nazwa wyświetlana] 홍루
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N101028].displayName
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [RPG [N101029] — nazwa wyświetlana] 돈키호테
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N101029].displayName
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [RPG [N104015] — nazwa wyświetlana] 쌍둥이 램프
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104015].displayName
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [RPG [N104016] — nazwa wyświetlana] 빨간 방석 스툴
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104016].displayName
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [RPG [N104017] — nazwa wyświetlana] 느긋한 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104017].displayName
   (powtórzenie elementu 576 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [RPG [N104018] — nazwa wyświetlana] 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104018].displayName
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [RPG [N104019] — nazwa wyświetlana] 가죽 침대
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104019].displayName
   (powtórzenie elementu 577 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [RPG [N104020] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104020].displayName
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [RPG [N104021] — nazwa wyświetlana] 빨간 방석 스툴
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104021].displayName
   (powtórzenie elementu 575 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [RPG [N104022] — nazwa wyświetlana] 길쭉 램프
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104022].displayName
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [RPG [N104023] — nazwa wyświetlana] 살갗 소파
   źródło: RPGSystem/rpg-loc-npc-floor-4.json :: dataList[key=N104023].displayName
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-quest-floor-4-b
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-quest-floor-4-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

623. [RPG [Q4001] — tytuł] 신발관으로 이동
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4001].title
   limit: do 40 znaków
   EN: To the Footwear Hall
   PL: Do Salonu Obuwia
624. [RPG [Q4001] — opis] 4층에 올라왔다. 통로를 따라 신발관으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4001].description
   limit: do 120 znaków
   EN: We've arrived at 4F. Let's follow the Corridor to the Footwear Hall.
   PL: Dotarliśmy na 4. piętro. Udajmy się korytarzem do Salonu Obuwia.
625. [RPG [Q4001] — krok 1 — cel zadania 1] 신발관으로 이동한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Follow the corridor to the Footwear Hall
   PL: Idziemy do Salonu Obuwia
626. [RPG [Q4002] — tytuł] 신발관으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4002].title
   limit: do 40 znaków
   EN: Head to the Footwear Hall
   PL: Udaj się do Salonu Obuwia
627. [RPG [Q4002] — opis] 우리를 따라오는 그 아이에게 뿌이라는 이름을 붙여주었다. 여전히 우리를 꺼려하는 것 같기도 하지만… 일단 지난번처럼 4층에 있는 신발관으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4002].description
   limit: do 230 znaków
   EN: We gave a name to the child following us—"Pwie". They still seem a little wary of us... But for now, our priority should be to head to the Footwear Hall on 4F, just like before.
   PL: Nazwaliśmy dziecko, które podąża za nami, „Pwie”. Chyba wciąż nie czuje się przy nas pewnie… Ale najpierw, jak ostatnio, udamy się do Salonu Obuwia na 4. piętrze.
628. [RPG [Q4002] — krok 1 — cel zadania 1] 신발관으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4002].steps[#0].goalDescription1
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [RPG [Q4002A] — tytuł] 포레그를 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4002A].title
   limit: do 40 znaków
   EN: Kill Four-legs
   PL: Zabij Czteronogiego
630. [RPG [Q4003] — tytuł] 원레그를 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4003].title
   limit: do 40 znaków
   EN: Kill One-leg
   PL: Zabij Surową Nogę
631. [RPG [Q4003A] — krok 1 — cel zadania 1] 신발관의 남은 이와 대화한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4003A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to whoever's left in the Footwear Hall
   PL: Rozmawiamy z tym, kto został w Salonie Obuwia
632. [RPG [Q4003B] — tytuł] 가구관으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4003B].title
   limit: do 40 znaków
   EN: Head to the Furniture Hall
   PL: Udaj się do Salonu Mebli
633. [RPG [Q4003B] — opis] 르루주 신발관에서 만난 도로테아가 집으로 갈 방법을 찾고 싶다며 심장 조각을 구해달라는 부탁을 해왔다. 그자를 도와주면 5층에 가는 방법을 알려준다고 한다. 심장 조각을 얻기 위해 가구관으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4003B].description
   limit: do 250 znaków
   EN: Dorothea from Le Rouge's Footwear Hall asked us to find a shard of heart so she can find her way home. In return, she'll tell us how to reach 5F. Head to the Furniture Hall to find what she wants.
   PL: Dorothea z Salonu Obuwia Le Rouge poprosiła o przyniesienie odłamka serca, żeby móc znaleźć drogę do domu. W zamian zdradzi, jak dostać się na 5. piętro. Udamy się do Salonu Mebli, by go zdobyć.
634. [RPG [Q4003B] — krok 1 — cel zadania 1] 가구관의 행복한 옷장에게 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4003B].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the Happy Closet in the Furniture Hall
   PL: Udaj się do Szczęśliwej Szafy w Salonie Mebli
635. [RPG [Q4004] — tytuł] 등굽은 조명에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4004].title
   limit: do 40 znaków
   EN: Talk to the Arc Floor Lamp
   PL: Zagadaj Lampę Łukową
636. [RPG [Q4004] — opis] 가구관에 있는 행복한 옷장에게 말을 걸었지만 그자는 여전히 아무말도 없다. 우리는 그자로부터 몇 가지 물건들을 떼어냈다. 가구관에 있는 등굽은 조명에게 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4004].description
   limit: do 190 znaków
   EN: The Happy Closet in the Furniture Hall still refuses to say a word. We pried a few things loose from them. Time to head over to the Arc Floor Lamp.
   PL: Zagadaliśmy Szczęśliwą Szafę w Salonie Mebli, ale on wciąż milczy. Oderwaliśmy od niego kilka przedmiotów. Udamy się do Lampy Łukowej.
637. [RPG [Q4004] — krok 1 — cel zadania 1] 등굽은 조명에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4004].steps[#0].goalDescription1
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
638. [RPG [Q4005] — krok 1 — cel zadania 1] 등굽은 조명에게 옷을 가져다준다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4005].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Take the clothing to the Arc Floor Lamp
   PL: Przynosisz ubranie Lampie Łukowej
639. [RPG [Q4006] — tytuł] 행복한 옷장에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4006].title
   limit: do 40 znaków
   EN: Return to the Happy Closet
   PL: Wróć do Szczęśliwej Szafy
640. [RPG [Q4006] — opis] 등굽은 조명에게 행복한 옷장으로부터 가져온 옷을 건네주었다. 다른 가구들도 앞다투어 자신들을 꾸며줄 옷을 가져와달라고 한다. 행복한 옷장에게 돌아가 보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4006].description
   limit: do 220 znaków
   EN: We gave the Arc Floor Lamp the clothing we took from the Happy Closet. Now the other Furnishings are clamoring for outfits of their own. Head back to the Happy Closet.
   PL: Wręczyliśmy Lampie Łukowej ubranie zdobyte od Szczęśliwej Szafy. Teraz pozostałe Meble rzucają się, by przynieść im coś do ubrania. Wróćmy do Szczęśliwej Szafy.
641. [RPG [Q4006] — krok 1 — cel zadania 1] 행복한 옷장에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4006].steps[#0].goalDescription1
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [RPG [Q4007] — tytuł] 가구들에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].title
   limit: do 60 znaków
   EN: Deliver the Clothes to the Furnishings
   PL: Dostarcz ubrania Meblom
643. [RPG [Q4007] — opis] 이번에도 행복한 옷장은 자신이 가진 것들을 아낌없이 내주었다. 가구들에게 옷을 전달해주자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].description
   limit: do 150 znaków
   EN: Once again, the Happy Closet gave up what they had without complaint. Deliver the clothes to the Furnishings.
   PL: Szczęśliwa Szafa znów rozdała, co miała, bez wahania. Dostarczmy ubrania Meblom.
644. [RPG [Q4007] — krok 1 — cel zadania 1] 뼛걸이에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Delivery for Bonehanger
   PL: Dostawa dla Kościanego Wieszaka
645. [RPG [Q4007] — krok 1 — cel zadania 2] 느긋한 가죽 침대에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Delivery for Mellow Leather Bed
   PL: Dostawa dla Spokojnego Skórzanego Łóżka
646. [RPG [Q4007] — krok 1 — cel zadania 3] 박제된 가죽 커튼에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription3
   limit: do 120 znaków
   EN: Delivery for Taxidermied Leather Curtain
   PL: Dostawa dla Wypchanej Skórzanej Kurtyny
647. [RPG [Q4007] — krok 1 — cel zadania 4] 빨간 방석 스툴에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription4
   limit: do 120 znaków
   EN: Delivery for Red-cushioned Stool
   PL: Dostawa dla Taboretu z Czerwonym Gąbkiem
648. [RPG [Q4007] — krok 1 — cel zadania 5] 살갗 소파에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription5
   limit: do 120 znaków
   EN: Delivery for Skinhide Couch
   PL: Dostawa dla Sofy ze Skóry
649. [RPG [Q4007] — krok 1 — cel zadania 6] 쌍둥이 램프에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4007].steps[#0].goalDescription6
   limit: do 120 znaków
   EN: Delivery for Lamp Twin
   PL: Dostawa dla Lampy-Bliźniaka
650. [RPG [Q4008] — tytuł] 행복한 옷장에게 심장 조각을 받을 수 있는지 물어보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4008].title
   limit: do 80 znaków
   EN: Ask the Happy Closet whether we can get a shard of heart
   PL: Zapytaj Szczęśliwą Szafę o odłamek serca
651. [RPG [Q4008] — opis] 가구들의 부탁을 모두 들어주었다. 행복한 옷장에게 심장 조각을 받을 수 있을지 물어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4008].description
   limit: do 120 znaków
   EN: We've finished helping the Furnishings. Time to ask the Happy Closet for a shard of heart.
   PL: Pomogliśmy już wszystkim Meblom. Czas zapytać Szczęśliwą Szafę o odłamek serca.
652. [RPG [Q4008] — krok 1 — cel zadania 1] 행복한 옷장에게 심장 조각을 받을 수 있는지 물어보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4008].steps[#0].goalDescription1
   (powtórzenie elementu 650 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [RPG [Q4008A] — tytuł] 가구들의 습격
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4008A].title
   limit: do 40 znaków
   EN: The Furnishings' Ambush
   PL: Zasadzka Mebli
654. [RPG [Q4008A] — krok 1 — cel zadania 1] 가구들의 습격을 지켜본다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4008A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: The Furnishings are ripping the Happy Closet apart.
   PL: Przyglądamy się zasadzce Mebli
655. [RPG [Q4013] — tytuł] 행복한 옷장의 잔해를 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4013].title
   limit: do 50 znaków
   EN: Inspect the Happy Closet's remains
   PL: Przejrzyj szczątki Szczęśliwej Szafy
656. [RPG [Q4013] — opis] 가구들은 행복한 옷장을 마구잡이로 뜯어가다가 마침내는 자신들끼리 싸우다 부서졌다. 행복한 옷장의 잔해를 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4013].description
   limit: do 240 znaków
   EN: The Furnishings tore the Happy Closet apart in their scramble for their belongings, then turned on each other until no one was left standing. Let's search the Happy Closet's remains.
   PL: Meble rozszarpały Szczęśliwą Szafę w walce o jej rzeczy, aż w końcu pozabijały się nawzajem. Przejrzyjmy szczątki Szczęśliwej Szafy.
657. [RPG [Q4013] — krok 1 — cel zadania 1] 행복한 옷장의 잔해를 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4013].steps[#0].goalDescription1
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [RPG [Q4021] — tytuł] 르루주 신발관 매장으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4021].title
   limit: do 50 znaków
   EN: Head to the Rouge Footwear Hall
   PL: Udaj się do Salonu Obuwia Le Rouge
659. [RPG [Q4021] — opis] 르누아르 신발관에서의 볼일은 끝난 것 같다. 밑에 있는 르루주의 신발관으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4021].description
   limit: do 150 znaków
   EN: Our business with the Noir Footwear Hall is done. Time to head to the Rouge's Footwear Hall just next door below.
   PL: Nasze sprawy w Salonie Obuwia Le Noir wyglądają na skończone. Udamy się do położonego tuż obok, niżej Salonu Obuwia Le Rouge.
660. [RPG [Q4021] — krok 1 — cel zadania 1] 르루주 신발관 매장으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4021].steps[#0].goalDescription1
   (powtórzenie elementu 658 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [RPG [Q4022] — tytuł] 르루주의 신발관으로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4022].title
   limit: do 50 znaków
   EN: Return to the Rouge Footwear Hall
   PL: Wróć do Salonu Obuwia Le Rouge
662. [RPG [Q4022] — opis] 행복한 옷장으로부터 심장 조각을 얻을 수 있었다. 르루주의 신발관으로 돌아가서 도로테아에게 심장을 건네주자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4022].description
   limit: do 170 znaków
   EN: We managed to collect a shard of heart from the Happy Closet. Let's return to Le Rouge's Footwear Hall and give it to Dorothea.
   PL: Udało się zdobyć odłamek serca ze Szczęśliwej Szafy. Wróćmy do Salonu Obuwia Le Rouge i przekażmy serce Dorothei.
663. [RPG [Q4022] — krok 1 — cel zadania 1] 르루주의 신발관으로 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4022].steps[#0].goalDescription1
   (powtórzenie elementu 661 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
664. [RPG [Q4023] — tytuł] 도로테아를 따라가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023].title
   limit: do 40 znaków
   EN: Follow Dorothea
   PL: Pójdź za Dorotheą
665. [RPG [Q4023] — opis] 도로테아에게 심장 조각을 건네주었다. 그자는 우리에게 5층으로 가는 방법을 알려주겠다고 하였다. 그자가 이끄는 곳으로 따라가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023].description
   limit: do 170 znaków
   EN: We gave Dorothea the shard of heart taken from the Happy Closet, and she agreed to tell us how to get to 5F. Let's follow her.
   PL: Wręczyliśmy Dorothei odłamek serca ze Szczęśliwej Szafy, a ona zgodziła się zdradzić, jak dostać się na 5. piętro. Pójdźmy za nią.
666. [RPG [Q4023] — krok 1 — cel zadania 1] 도로테아를 따라가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023].steps[#0].goalDescription1
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [RPG [Q4023A] — tytuł] 벽에 생긴 구멍
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023A].title
   limit: do 40 znaków
   EN: The Hole in the Wall
   PL: Dziura w Ścianie
668. [RPG [Q4023A] — opis] 벽에 구멍이 생겼다. 가까이서 확인해 보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023A].description
   limit: do 120 znaków
   EN: There's hole in the wall. We should inspect it.
   PL: W ścianie powstała dziura. Przyjrzyjmy się jej z bliska.
669. [RPG [Q4023A] — krok 1 — cel zadania 1] 생겨난 구멍을 확인한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Inspect the hole
   PL: Sprawdzamy powstałą dziurę
670. [RPG [Q4023B] — tytuł] 벽에 생긴 입구를 통해 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023B].title
   limit: do 40 znaków
   EN: Head into the Hole
   PL: Wejdź do środka przez otwór w ścianie
671. [RPG [Q4023B] — opis] 도로테아가 신발을 맞부딪히자 벽에서부터 어딘가로 통하는 입구가 생겼다. 안으로 들어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023B].description
   limit: do 120 znaków
   EN: Dorothea clicked her shoes together, and an opening appeared in the wall. Let's head inside.
   PL: Dorothea stuknęła obcasami, a w ścianie otworzyło się wejście prowadzące gdzieś w głąb. Wejdźmy do środka.
672. [RPG [Q4023B] — krok 1 — cel zadania 1] 벽에 생긴 입구를 통해 안으로 들어가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023B].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head into the hole
   PL: Wejdź do środka przez otwór w ścianie
673. [RPG [Q4023C] — tytuł] 환상체를 쫓아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023C].title
   limit: do 40 znaków
   EN: Follow the Abnormality
   PL: Pogoni za Abnormalnością
674. [RPG [Q4023C] — opis] 들어간 곳은 미아보호실이라는 장소였다. 환상체가 나타나 도로테아를 데려갔다. 쫓아가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023C].description
   limit: do 180 znaków
   EN: The passage led us to a place called the Lost Child Center. An Abnormality appeared and carried Dorothea away. We should go after it.
   PL: To, do czego weszliśmy, okazało się miejscem zwanym Przytułkiem Zagubionych Dzieci. Abnormalność pojawiła się i porwała Dorotheę. Trzeba za nią podążyć.
675. [RPG [Q4023C] — krok 1 — cel zadania 1] 환상체를 쫓아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023C].steps[#0].goalDescription1
   (powtórzenie elementu 673 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [RPG [Q4023D] — tytuł] 환상체 잔해를 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023D].title
   limit: do 50 znaków
   EN: Inspect the Abnormality's Remains
   PL: Przejrzyj szczątki Abnormalności
677. [RPG [Q4023D] — opis] 환상체를 물리쳤다. 잔해를 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023D].description
   limit: do 120 znaków
   EN: We dealt with the Abnormality. Let's inspect its remains.
   PL: Pokonaliśmy Abnormalność. Przejrzyjmy jej szczątki.
678. [RPG [Q4023D] — krok 1 — cel zadania 1] 환상체 잔해를 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023D].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Inspect the Abnormality's remains
   PL: Przejrzyj szczątki Abnormalności
679. [RPG [Q4023E] — tytuł] 환상체 잔해를 살펴보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023E].title
   (powtórzenie elementu 676 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [RPG [Q4023E] — opis] 함께 끌려온 이가 쓰러져 있다. 살펴보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4023E].description
   limit: do 120 znaków
   EN: The abducted Dorothea is lying on the floor. Let's inspect her.
   PL: Porwana Dorothea leży na podłodze. Przejrzyjmy ją.
681. [RPG [Q4024] — tytuł] 다른 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024].title
   limit: do 40 znaków
   EN: Head to the Other Stores
   PL: Udaj się do innych sklepów
682. [RPG [Q4024] — opis] 뿌이는 멋진 신발을 얻었다. 4층에는 아직 들리지 않은 매장이 남아있는 것 같다. 아직 들리지 않았던 매장으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024].description
   limit: do 160 znaków
   EN: Pwie has a fine new pair of shoes. There still seems to be stores on 4F we haven't visited yet. Let's go check them out.
   PL: Pwie ma już piękne nowe buty. Chyba zostały jeszcze sklepy na 4. piętrze, których nie odwiedziliśmy. Udamy się do nich.
683. [RPG [Q4024] — krok 1 — cel zadania 1] 다른 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Head to the other stores
   PL: Udaj się do innych sklepów
684. [RPG [Q4024] — krok 1 — cel zadania 2] 가방관의 다른 직원과 이야기해보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Talk to the other employee in the Handbags Hall
   PL: Porozmawiaj z innym pracownikiem Salonu Torebek
685. [RPG [Q4024A] — tytuł] 르루주 가방관의 벽 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024A].title
   limit: do 70 znaków
   EN: Inspect the Wall in the Le Rouge Handbags Hall
   PL: Zbadaj ścianę w Salonie Torebek Le Rouge
686. [RPG [Q4024A] — opis] 벽을 직접 조사해 보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024A].description
   limit: do 120 znaków
   EN: We should check the wall out.
   PL: Sprawdźmy sami tę ścianę.
687. [RPG [Q4024A] — krok 1 — cel zadania 1] 벽을 조사한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Investigate the wall
   PL: Badamy ścianę
688. [RPG [Q4024B] — tytuł] 숨어 있던 것
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024B].title
   limit: do 50 znaków
   EN: What was Hidden Behind the Wall?
   PL: To, co się Ukrywało
689. [RPG [Q4024B] — opis] 벽 뒤에 숨어 있던 것이 정체를 드러냈다. 저것을 어떻게 할지 답해주자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024B].description
   limit: do 130 znaków
   EN: The one who was hidden behind the wall revealed herself. We should decide what to do with her.
   PL: Ta, która ukrywała się za ścianą, ujawniła swoją tożsamość. Rozstrzygnijmy, co z nią zrobić.
690. [RPG [Q4024B] — krok 1 — cel zadania 1] 르네를 어떻게 할지 결정하기.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024B].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Decide what to do with Renée
   PL: Rozstrzygnij, co zrobić z Renée.
691. [RPG [Q4024C] — tytuł] 르네를 어떻게 할지 결정하기.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024C].title
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [RPG [Q4024C] — opis] 정해진 처분이 끝나기를 지켜보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024C].description
   limit: do 120 znaków
   EN: Wait for the decision to be carried out.
   PL: Przyglądajmy się, aż wykonanie decyzji dobiegnie końca.
693. [RPG [Q4024C] — krok 1 — cel zadania 1] 르네를 어떻게 할지 결정하기.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4024C].steps[#0].goalDescription1
   (powtórzenie elementu 690 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [RPG [Q4025] — tytuł] 다른 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [RPG [Q4025] — opis] 르루주 가방관에서의 볼일은 끝났다. 다른 매장으로 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025].description
   limit: do 120 znaków
   EN: Our business in the Rouge Handbags Hall is done. Time to check out the other store.
   PL: Nasze sprawy w Salonie Torebek Le Rouge są skończone. Udamy się do innego sklepu.
696. [RPG [Q4025] — krok 1 — cel zadania 1] 다른 매장으로 가보기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025].steps[#0].goalDescription1
   (powtórzenie elementu 683 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [RPG [Q4025A] — tytuł] 황금 재료를 모아오기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025A].title
   limit: do 40 znaków
   EN: Collect the Golden material
   PL: Zbierz Złote Materiały
698. [RPG [Q4025A] — opis] 르누아르의 가방관 디자이너가 황금 재료를 모아와달라고 부탁을 하였다. 이자의 부탁을 들어주면 5층으로 가는 에스컬레이터 위치를 알려줄지도 모른다. 황금 재료는 마네킹들로부터 얻을 수 있다.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025A].description
   limit: do 270 znaków
   EN: The designer at Le Noir's Handbags Hall asked us to gather some Golden materials. Help out so we can obtain information about where to find the escalator to the 5F. The materials can be taken from Mannequins.
   PL: Projektant z Salonu Torebek Le Noir poprosił o zebranie Złotych Materiałów. Jeśli spełnimy jego prośbę, może zdradzi, gdzie są schody ruchome na 5. piętro. Materiały można zdobyć od manekinów.
699. [RPG [Q4025A] — krok 1 — cel zadania 1] 황금 단추를 구한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025A].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Collect the Golden Button
   PL: Zdobywamy Złoty Guzik
700. [RPG [Q4025A] — krok 1 — cel zadania 2] 황금 이빨을 구한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025A].steps[#0].goalDescription2
   limit: do 120 znaków
   EN: Collect the Golden Tooth
   PL: Zdobywamy Złoty Ząb
701. [RPG [Q4025A] — krok 1 — cel zadania 3] 황금 머리카락을 구한다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025A].steps[#0].goalDescription3
   limit: do 120 znaków
   EN: Collect the Golden Hair
   PL: Zdobywamy Złote Włosy
702. [RPG [Q4025B] — tytuł] 르누아르 가방관 디자이너에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].title
   limit: do 70 znaków
   EN: Return to the designer at the Noir Handbags Hall
   PL: Wróć do projektanta z Salonu Torebek Le Noir
703. [RPG [Q4025B] — opis] 황금 재료들을 다 모아왔다. 디자이너에게 돌아가서 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].description
   limit: do 120 znaków
   EN: We've collected all the Golden materials requested. Time to head back to the designer.
   PL: Zebraliśmy wszystkie Złote Materiały. Wróćmy do projektanta i z nim pogadajmy.
704. [RPG [Q4025B] — krok 1 — cel zadania 1] 르누아르 가방관 디자이너에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].steps[#0].goalDescription1
   (powtórzenie elementu 702 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [RPG [Q4025B] — krok 2 — cel zadania 1] 첫 번째 걸작에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Talk to the first masterpiece
   PL: Zagadaj pierwsze Dzieło
706. [RPG [Q4025B] — krok 2 — cel zadania 2] 두 번째 걸작에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].steps[#1].goalDescription2
   limit: do 120 znaków
   EN: Talk to the second masterpiece
   PL: Zagadaj drugie Dzieło
707. [RPG [Q4025B] — krok 2 — cel zadania 3] 세 번째 걸작에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025B].steps[#1].goalDescription3
   limit: do 120 znaków
   EN: Talk to the third masterpiece
   PL: Zagadaj trzecie Dzieło
708. [RPG [Q4025C] — tytuł] 디자이너의 선택
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025C].title
   limit: do 40 znaków
   EN: The Designer's Decision
   PL: Wybór Projektanta
709. [RPG [Q4025C] — opis] .
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025C].description
   limit: do 120 znaków
   EN: .
   PL: .
710. [RPG [Q4025C] — krok 1 — cel zadania 1] 디자이너의 선택을 지켜본다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025C].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Wait for the designer's decision
   PL: Przyglądamy się Wyborowi Projektanta
711. [RPG [Q4025C] — krok 2 — cel zadania 1] 디자이너의 선택을 끝까지 지켜본다
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4025C].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Wait until the end
   PL: Przyglądamy się Wyborowi Projektanta do końca
712. [RPG [Q4026] — tytuł] 5층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4026].title
   limit: do 40 znaków
   EN: Take the Escalator to 5F
   PL: Wjedź schodami ruchomymi na 5. piętro
713. [RPG [Q4026] — opis] 신발관에서의 볼일은 끝났다. 5층으로 가는 에스컬레이터로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4026].description
   limit: do 120 znaków
   EN: Our business in the Handbags Hall is done. We should head to the escalator leading to 5F.
   PL: Nasze sprawy w Salonie Obuwia są skończone. Udamy się do schodów ruchomych na 5. piętro.
714. [RPG [Q4026] — krok 1 — cel zadania 1] 5층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-4-b.json :: dataList[key=Q4026].steps[#0].goalDescription1
   (powtórzenie elementu 712 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-quest-floor-4
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-quest-floor-4.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

715. [RPG [Q4001] — tytuł] 4층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4001].title
   (powtórzenie elementu 370 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [RPG [Q4001] — opis] 르누아르들이 준 감정평가서를 가지고 4층으로 올라가 보자. 이걸 가지고 가면 르누아르들이 극진히 환대를 해준다고 하니 더 수월하게 백화점을 다닐 수 있을지도 모른다.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4001].description
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We now have the Authenticity Certificate, courtesy of the Noirs on 3F. They told us that other Noirs will show us the same hospitality they showed us—the lavish kind, apparently. Hopefully, it'll make getting around the department store a little easier.\n\nNow, let's head upstairs to 4F.
   PL: Z Certyfikatem Autentyczności otrzymanym od Le Noir udamy się na 4. piętro. Podobno z nim inni Le Noir ugoszczą nas z równą, przepychem bijącą hojnością. Może to ułatwić nam chodzenie po domu handlowym.
717. [RPG [Q4001] — krok 1 — cel zadania 1] 4층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Get on the escalator to 4F
   PL: Wjedź schodami ruchomymi na 4. piętro
718. [RPG [Q4002] — tytuł] 4층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4002].title
   limit: do 40 znaków
   EN: Explore 4F
   PL: Rozejrzyj się po 4. piętrze
719. [RPG [Q4002] — opis] 4층으로 왔다. 이곳엔 어떤 매장들이 있을까? 일단 오른쪽으로 향해서 4층을 둘러보도록 하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4002].description
   limit: do 170 znaków
   EN: We're on 4F. What kind of weird stores will we find here, I wonder? Let's start by checking out what's to the hallway on the right.
   PL: Dotarliśmy na 4. piętro. Jakie sklepy tu znajdziemy? Najpierw skierujmy się w prawo i rozejrzyjmy się.
720. [RPG [Q4002] — krok 1 — cel zadania 1] 4층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4002].steps[#0].goalDescription1
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [RPG [Q4003] — tytuł] 4층 둘러보기 2
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4003].title
   limit: do 40 znaków
   EN: Explore 4F (2)
   PL: Rozejrzyj się po 4. piętrze (2)
722. [RPG [Q4003] — opis] 르누아르의 신발관 직원인 원레그로부터 어떤 옷감도 찢을 수 있는 무기에 대한 이야기를 들었다. 일단은 르누아르의 신발관을 나와서 4층을 마저 둘러보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4003].description
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A One-leg, sales associate at the Noir Footwear Hall, told us about a legendary weapon capable of ripping through any fabric.\nFor now, let's leave the Noir Footwear Hall and explore the rest of 4F.
   PL: Surowa Noga, pracownik Salonu Obuwia Le Noir, opowiedział nam o legendarnej broni zdolnej poderwać każdą tkaninę. Na razie opuśćmy Salon Obuwia Le Noir i rozejrzyjmy się po reszcie 4. piętra.
723. [RPG [Q4003] — krok 1 — cel zadania 1] 원레그와 대화 마치기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4003].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Finish talking to One-leg
   PL: Dokończ rozmowę z Surową Nogą
724. [RPG [Q4003] — krok 2 — cel zadania 1] 4층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4003].steps[#1].goalDescription1
   (powtórzenie elementu 718 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
725. [RPG [Q4003] — krok 2 — cel zadania 2] 등굽은 조명과 대화한다
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4003].steps[#1].goalDescription2
   limit: do 120 znaków
   EN: Talk to the Arc Floor Lamp
   PL: Rozmawiasz z Lampą Łukową
726. [RPG [Q4004] — tytuł] 가구관의 주인을 만나기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4004].title
   limit: do 50 znaków
   EN: Meet the Owner of the Furniture Hall
   PL: Spotkaj właściciela Salonu Mebli
727. [RPG [Q4004] — opis] 가구관이라는 곳에 왔다. 등굽은 조명이 자신에게 어울릴 옷을 가져와 달라는 부탁을 해왔다. 가구관의 주인을 만나보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4004].description
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: So, this is the "Furnishing Hall," huh?\nThe Arc Floor Lamp we talked to asked that we bring him an outfit "most fashionable and suitable." Let's go meet the owner of the Furniture Hall.
   PL: Oto Salon Mebli. Lampa Łukowa poprosiła, byśmy przynieśli jej ubranie „najmodniejsze i najbardziej stosowne”. Udajmy się do właściciela Salonu Mebli.
728. [RPG [Q4004] — krok 1 — cel zadania 1] 가구관의 주인에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4004].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Talk to the owner of the Furniture Hall
   PL: Zagadaj właściciela Salonu Mebli
729. [RPG [Q4005] — tytuł] 등굽은 조명에게 새 옷을 갖다주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4005].title
   limit: do 70 znaków
   EN: Deliver the New Clothes to the Arc Floor Lamp
   PL: Przynieś Lampie Łukowej nowe ubranie
730. [RPG [Q4005] — opis] 가구관의 주인, ‘행복한 옷장’은 말 없이 자신의 몸에 매달린 물건들을 보여준다. 그자에게 적당한 옷을 하나 떼 왔다. 등굽은 조명에게 가져다주도록 하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4005].description
   limit: do 270 znaków
   EN: The owner of the Furniture Hall, "Happy Closet," opened themselves up to show us some items dangling from inside their body. We picked an outfit that seemed adequate—now, let's bring this to the Arc Floor Lamp.
   PL: Właściciel Salonu Mebli, „Szczęśliwa Szafa”, milcząc pokazuje rzeczy wiszące na jego własnym ciele. Oderwaliśmy od niego odpowiednie ubranie. Przynieśmy je Lampie Łukowej.
731. [RPG [Q4005] — krok 1 — cel zadania 1] 등굽은 조명에게 새 옷을 갖다주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4005].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Bring the new article of clothing for the Arc Floor Lamp
   PL: Przynieś Lampie Łukowej nowe ubranie
732. [RPG [Q4006] — tytuł] 행복한 옷장으로부터 옷을 꺼내가기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4006].title
   limit: do 60 znaków
   EN: Take More Clothes from the Happy Closet
   PL: Weź więcej ubrań od Szczęśliwej Szafy
733. [RPG [Q4006] — opis] 등굽은 조명에게 옷을 가져다준 것을 보고 다른 가구들이 불만을 터뜨리기 시작했다. 행복한 옷장에게 돌아가서 가구들에게 줄 옷을 꺼내오자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4006].description
   limit: do 240 znaków
   EN: The other Furnishings weren't so happy to see the Arc Floor Lamp receive an article of clothing. Let's return to the Happy Closet and pick out clothes for the rest of the Furnishings.
   PL: Gdy pozostałe Meble zobaczyły, że Lampa Łukowa dostała ubranie, wybuchnęły niezadowoleniem. Wróćmy do Szczęśliwej Szafy i wybierzmy ubrania dla reszty Mebli.
734. [RPG [Q4006] — krok 1 — cel zadania 1] 행복한 옷장으로부터 옷을 꺼내가기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Take more articles of clothing from the Happy Closet
   PL: Weź więcej ubrań od Szczęśliwej Szafy
735. [RPG [Q4007] — tytuł] 가구들에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].title
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [RPG [Q4007] — opis] 행복한 옷장으로부터 몇 가지 옷들을 꺼내 왔다. 이제 가구들에게 각각 옷을 전해주도록 하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].description
   limit: do 140 znaków
   EN: Picked out a few articles of clothing from the Happy Closet. Now, to deliver them to the Furnishings.
   PL: Wybraliśmy kilka ubrań od Szczęśliwej Szafy. Teraz dostarczmy je Meblom.
737. [RPG [Q4007] — krok 1 — cel zadania 1] 뼛걸이에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription1
   (powtórzenie elementu 644 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [RPG [Q4007] — krok 1 — cel zadania 2] 느긋한 가죽 침대에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription2
   (powtórzenie elementu 645 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [RPG [Q4007] — krok 1 — cel zadania 3] 박제된 가죽 커튼에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription3
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [RPG [Q4007] — krok 1 — cel zadania 4] 빨간 방석 스툴에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription4
   (powtórzenie elementu 647 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [RPG [Q4007] — krok 1 — cel zadania 5] 살갗 소파에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription5
   (powtórzenie elementu 648 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [RPG [Q4007] — krok 1 — cel zadania 6] 쌍둥이 램프에게 옷을 전해주기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4007].steps[#0].goalDescription6
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [RPG [Q4008] — tytuł] 행복한 옷장에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4008].title
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [RPG [Q4008] — opis] 다른 가구들에게 옷을 다 전해주었다. 이제 다시 행복한 옷장에게 돌아가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4008].description
   limit: do 160 znaków
   EN: Made sure that each of the angry Furnishings received their article of clothing. Time to head back to the Happy Closet.
   PL: Dopilnowaliśmy, by każde z niezadowolonych Mebli dostało swoje ubranie. Czas wrócić do Szczęśliwej Szafy.
745. [RPG [Q4008] — krok 1 — cel zadania 1] 행복한 옷장에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4008].steps[#0].goalDescription1
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [RPG [Q4008] — krok 2 — cel zadania 1] 가구들의 습격을 지켜본다
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4008].steps[#1].goalDescription1
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [RPG [Q4013] — tytuł] 등굽은 조명에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4013].title
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [RPG [Q4013] — opis] 심장마저 뜯긴 행복한 옷장은 더 이상 미동이 없다. 가구관을 벗어나기 전, 등굽은 조명에게 다시 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4013].description
   limit: do 210 znaków
   EN: The Happy Closet, with even their heart torn out, has gone completely still. Maybe we should talk to the Arc Floor Lamp before we get out of the Furniture Hall.
   PL: Szczęśliwa Szafa, której wyrwano nawet serce, już się nie rusza. Zanim opuścimy Salon Mebli, zagadajmy jeszcze Lampę Łukową.
749. [RPG [Q4013] — krok 1 — cel zadania 1] 등굽은 조명에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4013].steps[#0].goalDescription1
   (powtórzenie elementu 635 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
750. [RPG [Q4009] — tytuł] 지하로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4009].title
   limit: do 40 znaków
   EN: Head to the Basement Floors
   PL: Udaj się na poziomy podziemne
751. [RPG [Q4009] — opis] 우리가 얻은 레시피에 의하면, 황금고치를 통해 황금 실타래를 얻어야 한다. 황금고치는 지하 1층에서 볼 수 있다고 한다. 지하 1층에서 황금고치를 얻은 후, 지하 2층으로 가보도록 하자.
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4009].description
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: According to the recipe we acquired, we're first going to have to obtain this "Golden Cocoon," which will lead to us getting our hands on the Golden Thread.\n\nLet's head to B1F, acquire the Golden Cocoon, then head deeper down to B2F.
   PL: Według zdobytego przepisu najpierw trzeba zdobyć Złoty Kokon, z którego uzyskamy Złotą Przędzę. Podobno Złoty Kokon można znaleźć na poziomie -1. Zdobądźmy go tam, a potem zejdźmy na poziom -2.
752. [RPG [Q4009] — krok 1 — cel zadania 1] 지하 1층으로 가는 에스컬레이터 타기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4009].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Get on the escalator to B1F
   PL: Wjedź schodami ruchomymi na poziom -1
753. [RPG [Q4009] — krok 2 — cel zadania 1] 지하 1층 둘러보기
   źródło: RPGSystem/rpg-loc-quest-floor-4.json :: dataList[key=Q4009].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Explore B1F
   PL: Rozejrzyj się na poziomie -1

## Tryb RPG [floor-4] — rpg-loc-swarm-mob-floor-4-a
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-4-a.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

754. [RPG [swarm_mannequin_type_a] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-4-a.json :: dataList[key=swarm_mannequin_type_a].displayName
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [RPG [swarm_mannequin_type_b] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-4-a.json :: dataList[key=swarm_mannequin_type_b].displayName
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-4] — rpg-loc-swarm-mob-floor-4-b
- obszar/warstwa: `floor-4` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-4-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

756. [RPG [swarm_mannequin_type_a] — nazwa wyświetlana] 덜컹대는 서랍
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-4-b.json :: dataList[key=swarm_mannequin_type_a].displayName
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [RPG [swarm_mannequin_type_b] — nazwa wyświetlana] 삐걱이는 서랍
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-4-b.json :: dataList[key=swarm_mannequin_type_b].displayName
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [RPG [swarm_unbound_bagware_npc_a] — nazwa wyświetlana] 르네
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-4-b.json :: dataList[key=swarm_unbound_bagware_npc_a].displayName
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-location-floor-5
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-location-floor-5.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

759. [RPG [150100] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-5.json :: dataList[key=150100].text
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [RPG [150200] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-5.json :: dataList[key=150200].text
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [RPG [150300] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-5.json :: dataList[key=150300].text
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [RPG [150201] — tekst] 복도
   źródło: RPGSystem/rpg-loc-location-floor-5.json :: dataList[key=150201].text
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-npc-floor-5-b-enemy
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-npc-floor-5-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

763. [RPG [N105103] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105103].displayName
   limit: do 40 znaków
   EN: Le Noir Priest
   PL: Kapłan Le Noir
764. [RPG [N105104] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105104].displayName
   limit: do 40 znaków
   EN: Le Noir Sales Associate
   PL: Pracownik Le Noir
765. [RPG [N105102] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105102].displayName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [RPG [N105101] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105101].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [RPG [N105105] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105105].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [RPG [N105106] — nazwa wyświetlana] 검은 실
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105106].displayName
   limit: do 40 znaków
   EN: Blackthread
   PL: Czarna Nić
769. [RPG [N105107] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105107].displayName
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [RPG [N105108] — nazwa wyświetlana] 르누아르 메종 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105108].displayName
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [RPG [N105109] — nazwa wyświetlana] 르누아르 컨템포러리 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105109].displayName
   limit: do 60 znaków
   EN: Le Noir Contemporary Hall Sales Associate
   PL: Pracownik Salonu Contempora Le Noir
772. [RPG [N105110] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105110].displayName
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [RPG [N105111] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105111].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [RPG [N105112] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105112].displayName
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [RPG [N105113] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105113].displayName
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [RPG [N105114] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105114].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [RPG [N105115] — nazwa wyświetlana] 르루주 점원[햇살]
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105115].displayName
   (powtórzenie elementu 405 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [RPG [N105116] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105116].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [RPG [N105122] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105122].displayName
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [RPG [N105117] — nazwa wyświetlana] 르누아르 경비원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105117].displayName
   limit: do 40 znaków
   EN: Le Noir Guard
   PL: Strażnik Le Noir
781. [RPG [N105118] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105118].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [RPG [N105119] — nazwa wyświetlana] 르누아르 메종
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105119].displayName
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [RPG [N105120] — nazwa wyświetlana] 르누아르 메종 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105120].displayName
   (powtórzenie elementu 293 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [RPG [N105121] — nazwa wyświetlana] 르누아르 컨템포러리 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-b-enemy.json :: dataList[key=N105121].displayName
   (powtórzenie elementu 771 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-npc-floor-5-b
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-npc-floor-5-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

785. [RPG [N101002] — nazwa wyświetlana] 크로머 언니
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N101002].displayName
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [RPG [N105001] — nazwa wyświetlana] 르누아르 브랜드 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105001].displayName
   limit: do 40 znaków
   EN: Le Noir's Brand Manager
   PL: Dyrektor Marki Le Noir
787. [RPG [N105002] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105002].displayName
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [RPG [N105003] — nazwa wyświetlana] 고치
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105003].displayName
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [RPG [N105005] — nazwa wyświetlana] 뿌이
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105005].displayName
   limit: do 40 znaków
   EN: Pwie
   PL: Pwie
790. [RPG [N105006] — nazwa wyświetlana] 먹는 거인
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105006].displayName
   limit: do 40 znaków
   EN: Voracious Giant
   PL: Pożerający Gigant
791. [RPG [N105007] — nazwa wyświetlana] 먹는 거인
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105007].displayName
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [RPG [N105008] — nazwa wyświetlana] 먹는 거인
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105008].displayName
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [RPG [N105009] — nazwa wyświetlana] 먹는 거인
   źródło: RPGSystem/rpg-loc-npc-floor-5-b.json :: dataList[key=N105009].displayName
   (powtórzenie elementu 790 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-npc-floor-5-c2-enemy
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

794. [RPG [N105001_C2] — nazwa wyświetlana] 르루주 순찰자
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105001_C2].displayName
   limit: do 40 znaków
   EN: Le Rouge Patrol
   PL: Patrol Le Rouge
795. [RPG [N105002_C2] — nazwa wyświetlana] 르루주 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105002_C2].displayName
   limit: do 40 znaków
   EN: Le Rouge Porter
   PL: Tragarz Le Rouge
796. [RPG [N105003_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105003_C2].displayName
   limit: do 50 znaków
   EN: Boutique du Rouge Sales Associate
   PL: Pracownik Boutique du Rouge
797. [RPG [N105010_C2] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105010_C2].displayName
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [RPG [N105010S_C2] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105010S_C2].displayName
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [RPG [N105020_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105020_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [RPG [N105021_C2] — nazwa wyświetlana] 르루주 순찰자
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105021_C2].displayName
   (powtórzenie elementu 794 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
801. [RPG [N105040_C2] — nazwa wyświetlana] 르루주 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105040_C2].displayName
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
802. [RPG [N105041_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105041_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [RPG [N105042_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105042_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [RPG [N105043_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105043_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [RPG [N105044_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105044_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [RPG [N105045_C2] — nazwa wyświetlana] 르루주 부티크 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105045_C2].displayName
   (powtórzenie elementu 796 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [RPG [N105046_C2] — nazwa wyświetlana] 르루주 명품관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105046_C2].displayName
   limit: do 50 znaków
   EN: Le Rouge Luxury Hall Sales Associate
   PL: Pracownik Salonu Prestiżu Le Rouge
808. [RPG [N105047_C2] — nazwa wyświetlana] 르루주 명품관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105047_C2].displayName
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [RPG [N105048_C2] — nazwa wyświetlana] 르루주 명품관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105048_C2].displayName
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [RPG [N105049_C2] — nazwa wyświetlana] 르루주 명품관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105049_C2].displayName
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [RPG [N105050_C2] — nazwa wyświetlana] 르루주 명품관 점원
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105050_C2].displayName
   (powtórzenie elementu 807 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [RPG [N105023_C2] — nazwa wyświetlana] 순환하는 것
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105023_C2].displayName
   limit: do 40 znaków
   EN: That Which Cycles
   PL: To, Co Cykluje
813. [RPG [N105024_C2] — nazwa wyświetlana] 순환하는 것
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2-enemy.json :: dataList[key=N105024_C2].displayName
   (powtórzenie elementu 812 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-npc-floor-5-c2
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-npc-floor-5-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

814. [RPG [N105030_C2] — nazwa wyświetlana] 크로머
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2.json :: dataList[key=N105030_C2].displayName
   limit: do 40 znaków
   EN: Kromer
   PL: Kromer
815. [RPG [N105011_C2] — nazwa wyświetlana] 뷔페
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2.json :: dataList[key=N105011_C2].displayName
   (powtórzenie elementu 303 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [RPG [N105031_C2] — nazwa wyświetlana] 만찬 식탁
   źródło: RPGSystem/rpg-loc-npc-floor-5-c2.json :: dataList[key=N105031_C2].displayName
   limit: do 40 znaków
   EN: The Feast
   PL: Stół Uczty

## Tryb RPG [floor-5] — rpg-loc-quest-floor-5-b
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-quest-floor-5-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

817. [RPG [Q5001] — tytuł] 5층 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5001].title
   limit: do 40 znaków
   EN: Investigate 5F
   PL: Zbadaj 5. piętro
818. [RPG [Q5001] — opis] 드디어 뿌이와 함께 5층으로 오게 되었다. 무엇이 있을진 모르겠지만 앞으로 계속 걸어가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5001].description
   limit: do 160 znaków
   EN: We finally reached 5F with Pwie. There's no telling what we'll encounter on this floor, but we should keep exploring.
   PL: W końcu dotarliśmy z Pwie na 5. piętro. Nie wiadomo, co tu zastaniemy, ale idźmy dalej.
819. [RPG [Q5001] — krok 1 — cel zadania 1] 5층 복도에 있는 문을 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5001].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Investigate the Door on 5F Corridor
   PL: Zbadaj drzwi na korytarzu 5. piętra
820. [RPG [Q5001] — krok 2 — cel zadania 1] 크로머의 이야기를 듣기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5001].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Hear Kromer Out
   PL: Wysłuchaj, co mówi Kromer
821. [RPG [Q5011] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5011].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
822. [RPG [Q5011] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5011].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
823. [RPG [Q5002] — tytuł] 지하 1층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5002].title
   limit: do 40 znaków
   EN: Head to B1F
   PL: Udaj się na poziom -1
824. [RPG [Q5002] — opis] 5층 안으로 들어가기에는 미덕이 부족하다고 한다. 뿌이는 황금가죽으로 만든 수의를 입어야 한다고 했다. 지하에 내려가면 가죽을 가공해주는 이가 있다고 했다. 지하로 내려가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5002].description
   limit: do 270 znaków
   EN: Apparently, we're still lacking in "virtue" to enter 5F. Pwie said they need to wear a Golden Shroud, and that somewhere down on the underground floors, there's someone who can process hides. Let's head there.
   PL: Podobno brakuje nam „cnoty”, by wejść na 5. piętro. Pwie powiedział, że musi założyć Całun ze Złotej Skóry, a gdzieś na podziemnych poziomach mieszka ktoś, kto obrabia skóry. Zejdźmy na dół.
825. [RPG [Q5002] — krok 1 — cel zadania 1] 지하 1층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5002].steps[#0].goalDescription1
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [RPG [Q5002] — krok 2 — cel zadania 1] 5층의 장막을 만져보기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5002].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Touch the Curtain on 5F
   PL: Dotknij Zasłony na 5. piętrze
827. [RPG [Q5004] — tytuł] 5층 안쪽으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5004].title
   limit: do 40 znaków
   EN: Head to the Inner Part of 5F
   PL: Udaj się w głąb 5. piętra
828. [RPG [Q5004] — opis] 통제자가 완성해준 황금가죽 옷을 뿌이가 입었다. 하지만 꼬물이를 먹어치워버린 뿌이의 기분은 그다지 좋지 않아 보인다. 이제 5층으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5004].description
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Overseer completed the Golden Hide, allowing Pwie to don clothing made from it. Pwie, however, doesn't seem glad at all after devouring Wriggley.\n... It's time to head to 5F.
   PL: Nadzorca ukończył Złotą Skórę, a Pwie przywdział ubranie z niej. Ale Pwie, który pożarł Wriggleya, widać, nie ma dobrego humoru. Czas udać się na 5. piętro.
829. [RPG [Q5004] — krok 1 — cel zadania 1] 5층 안쪽으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5004].steps[#0].goalDescription1
   (powtórzenie elementu 827 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [RPG [Q5004] — krok 2 — cel zadania 2] 몰려오는 것들을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5004].steps[#1].goalDescription2
   limit: do 120 znaków
   EN: Fend off the Onslaught
   PL: Rozpraw się z nawałą
831. [RPG [Q5008] — krok 1 — cel zadania 1] 길을 막아선 르누아르와 마주치기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5008].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Face the Noir Blocking the Path
   PL: Stan twarzą w twarz z Le Noir na drodze
832. [RPG [Q5006] — krok 1 — cel zadania 1] 르누아르 점원[햇살] 9기 처치
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5006].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Defeat 9 Le Noir Sales Associates [Sunshone]
   PL: Pokonaj 9 Pracowników Le Noir [Napromienionych]
833. [RPG [Q5007] — tytuł] 5층 안쪽의 장막으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5007].title
   limit: do 50 znaków
   EN: Approach the Curtain Beyond 5F
   PL: Udaj się do Zasłony w głębi 5. piętra
834. [RPG [Q5007] — opis] 5층에서 몰려오는 적들을 처치했다. 이제 5층의 안쪽으로 진입해서 장막을 만져보자. 뿌이가 황금 수의를 입었으니 이전과는 다른 변화가 생길지도 모른다.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5007].description
   limit: do 240 znaków
   EN: We dealt with the onslaught of enemies on 5F. Now it's time to head to the inside and lay our hands on the curtain. With the Golden Shroud on Pwie, things may turn out different this time.
   PL: Rozbiliśmy nawałę wrogów na 5. piętrze. Teraz wejdźmy w głąb i dotknijmy Zasłony. Pwie nosi już Całun ze Złotej Skóry — może tym razem coś się zmieni.
835. [RPG [Q5007] — krok 1 — cel zadania 1] 5층의 장막을 만져보기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5007].steps[#0].goalDescription1
   (powtórzenie elementu 826 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [RPG [Q5003] — tytuł] 르누아르 브랜드 매니저 처치
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5003].title
   limit: do 40 znaków
   EN: Kill Le Noir's Brand Manager
   PL: Zabij Dyrektora Marki Le Noir
837. [RPG [Q5003] — opis] 길을 막아선 르누아르 브랜드 매니저를 쓰러뜨리자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5003].description
   limit: do 120 znaków
   EN: We need to defeat the Le Noir Brand Manager who's standing in the way.
   PL: Trzeba pokonać Dyrektora Marki Le Noir, który zagradza nam drogę.
838. [RPG [Q5003] — krok 1 — cel zadania 1] 르누아르 브랜드 매니저를 쓰러뜨린다
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5003].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Defeat Le Noir's Brand Manager
   PL: Pokonuj Dyrektora Marki Le Noir
839. [RPG [Q5005] — tytuł] 뷔페를 지켜보기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5005].title
   limit: do 40 znaków
   EN: Observe Buffet
   PL: Obserwuj Bufet
840. [RPG [Q5005] — opis] 고치가 갈라졌다.\n뷔페가 무엇이 되는지 지켜보자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5005].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The cocoon finally parted.\nLet's see what Buffet will transform into.
   PL: Kokon pękł.\nObserwujmy, w co przemieni się Bufet.
841. [RPG [Q5005] — krok 1 — cel zadania 1] 뷔페가 무엇이 되는지 끝까지 지켜본다
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5005].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Keep Observing Buffet until the End
   PL: Obserwujemy do końca, w co przemieni się Bufet
842. [RPG [Q5009] — tytuł] 레스토랑 안으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5009].title
   limit: do 40 znaków
   EN: Enter the Restaurant
   PL: Udaj się do restauracji
843. [RPG [Q5009] — opis] 5층을 가로막고 있었던 장막 안으로 무사히 들어왔다. 안에는 거대한 무언가들이 식사하는 광경이 보인다. 일단 적들을 피해 안쪽으로 계속 도망치자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5009].description
   limit: do 120 znaków
   EN: We were able to venture beyond the curtain that had been blocking our path on 5F.
   PL: Weszliśmy za Zasłonę blokującą 5. piętro. W środku ogromne istoty jedzą. Uciekajmy w głąb, omijając wrogów.
844. [RPG [Q5009] — krok 1 — cel zadania 1] 레스토랑 안으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5009].steps[#0].goalDescription1
   (powtórzenie elementu 842 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [RPG [Q5010] — tytuł] 몰려오는 르누아들로부터 고치를 지키기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5010].title
   limit: do 70 znaków
   EN: Protect the Cocoon from the Le Noir Onslaught
   PL: Chroń Kokon przed nawałą Le Noir
846. [RPG [Q5010] — opis] 뿌이가 졸리다고 하며 잠에 들 것 같다고 했다. 자리에서 잠에 든 뿌이는 그대로 고치의 형상이 되었다. 르누아르들이 고치를 노리고 사방에서 몰려온다. 뿌이를 지켜내자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5010].description
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pwie told us they were feeling tired moments before they fell asleep and became a cocoon. Seemingly having discovered the cocoon's location, a small army of Le Noir have arrived here to destroy it.\n\nLet's protect Pwie.
   PL: Pwie powiedział, że zasną, po czym w tym samym miejscu zapadł w sen i zamienił się w kokon. Le Noir, wykrywszy kokon, nadciągają ze wszystkich stron. Brońmy Pwie.
847. [RPG [Q5010] — krok 1 — cel zadania 1] 몰려오는 르누아들로부터 고치를 지키기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5010].steps[#0].goalDescription1
   (powtórzenie elementu 845 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [RPG [Q5012] — tytuł] 검은 실을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5012].title
   limit: do 40 znaków
   EN: Kill Blackthread
   PL: Zabij Czarną Nić
849. [RPG [Q5012] — opis] 길을 가로막는 검은 실을 쓰러뜨리자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5012].description
   limit: do 120 znaków
   EN: We should deal with the Blackthread and open the path.
   PL: Trzeba pokonać Czarną Nić zagradzającą nam drogę.
850. [RPG [Q5012] — krok 1 — cel zadania 1] 검은 실을 처치하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-b.json :: dataList[key=Q5012].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Kill the Blackthread
   PL: Zabij Czarną Nić

## Tryb RPG [floor-5] — rpg-loc-quest-floor-5-c2
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-quest-floor-5-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

851. [RPG [Q5000_C2] — tytuł] 5층 안으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5000_C2].title
   limit: do 40 znaków
   EN: Proceed Through 5F
   PL: Udaj się na 5. piętro
852. [RPG [Q5000_C2] — opis] 5층으로 올라왔다. 5층 안쪽으로 계속 가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5000_C2].description
   limit: do 120 znaków
   EN: We're on 5F. Let's keep heading inside.
   PL: Dotarliśmy na 5. piętro. Idźmy dalej w głąb.
853. [RPG [Q5000_C2] — krok 1 — cel zadania 1] 5층 안으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5000_C2].steps[#0].goalDescription1
   (powtórzenie elementu 851 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [RPG [Q5001_C2] — tytuł] 뷔페를 막아서기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5001_C2].title
   limit: do 40 znaków
   EN: Stop Buffet
   PL: Stan na drodze Bufetowi
855. [RPG [Q5001_C2] — opis] 5층에는 이전과는 달리 비대해지지 않은 뷔페가 있었다. 뷔페는 우리가 계속 머무르기를 원하지만 그럴 수는 없다. 계속 나아가기 위해서는, 뷔페를 쓰러뜨려야 한다.
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5001_C2].description
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What awaited us on the 5F was Buffet, who hadn't engorged into the massive form they'd turned into before the Liquidation.\n\nThey want us to stay, but we can't. We need to defeat Buffet to keep moving forward.
   PL: Na 5. piętrze czekał Bufet — tym razem nie rozdęty do poprzednich rozmiarów. On chce, byśmy zostali, ale nie możemy. Żeby iść dalej, musimy pokonać Bufeta.
856. [RPG [Q5001_C2] — krok 1 — cel zadania 1] 뷔페를 막아서기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5001_C2].steps[#0].goalDescription1
   (powtórzenie elementu 854 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [RPG [Q5002_C2] — tytuł] 5층 안으로 나아가기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5002_C2].title
   limit: do 40 znaków
   EN: Proceed Through 5F
   PL: Idź dalej w głąb 5. piętra
858. [RPG [Q5002_C2] — opis] 르루주의 붉은 신이었던 뷔페, 동시에 우리의 동행자였던 뿌이는 더 이상 움직이지 않는다. 5층 안쪽으로 계속 나아가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5002_C2].description
   limit: do 160 znaków
   EN: Buffet, the Crimson God of Le Rouge, who was also our companion, Pwie... has gone still. We should proceed deeper into 5F.
   PL: Bufet — czerwony bóg Le Rouge, a dawniej nasz towarzysz Pwie — już się nie rusza. Idźmy dalej w głąb 5. piętra.
859. [RPG [Q5002_C2] — krok 1 — cel zadania 1] 5층 안으로 나아가기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5002_C2].steps[#0].goalDescription1
   (powtórzenie elementu 857 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [RPG [Q5003_C2] — tytuł] 6층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5003_C2].title
   limit: do 40 znaków
   EN: Head to 6F
   PL: Udaj się na 6. piętro
861. [RPG [Q5003_C2] — opis] 식사를 마치자 6층으로 향하는 길이 열렸다. 6층으로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5003_C2].description
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The path to 6F opened after Meursault finished his meal.\n\nLet's head up to 6F.
   PL: Gdy posiłek się skończył, droga na 6. piętro stanęła otworem. Udamy się na górę.
862. [RPG [Q5003_C2] — krok 1 — cel zadania 1] 6층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-5-c2.json :: dataList[key=Q5003_C2].steps[#0].goalDescription1
   (powtórzenie elementu 860 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-swarm-mob-floor-5-b
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-5-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

863. [RPG [swarm_lanoir_fanatic] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-b.json :: dataList[key=swarm_lanoir_fanatic].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [RPG [swarm_lanoir_fanatic_3f] — nazwa wyświetlana] 르누아르 점원
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-b.json :: dataList[key=swarm_lanoir_fanatic_3f].displayName
   (powtórzenie elementu 764 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [RPG [swarm_lanoir_guard] — nazwa wyświetlana] 르누아르 사제
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-b.json :: dataList[key=swarm_lanoir_guard].displayName
   (powtórzenie elementu 763 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-5] — rpg-loc-swarm-mob-floor-5-c2
- obszar/warstwa: `floor-5` · plik gry: `RPGSystem/rpg-loc-swarm-mob-floor-5-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

866. [RPG [swarm_5f_c2_larouge_spa] — nazwa wyświetlana] 르루주 점원
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-c2.json :: dataList[key=swarm_5f_c2_larouge_spa].displayName
   limit: do 40 znaków
   EN: Le Rouge Sales Associate
   PL: Pracownik Le Rouge
867. [RPG [swarm_5f_c2_larouge_elite] — nazwa wyświetlana] 르루주 스토어 매니저
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-c2.json :: dataList[key=swarm_5f_c2_larouge_elite].displayName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [RPG [swarm_5f_c2_larouge_sickle] — nazwa wyświetlana] 르루주 스태프
   źródło: RPGSystem/rpg-loc-swarm-mob-floor-5-c2.json :: dataList[key=swarm_5f_c2_larouge_sickle].displayName
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-6] — rpg-loc-npc-floor-6-c2
- obszar/warstwa: `floor-6` · plik gry: `RPGSystem/rpg-loc-npc-floor-6-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

869. [RPG [N106001_C2] — nazwa wyświetlana — tylko EN w danych gry] Sisyphus
   źródło: RPGSystem/rpg-loc-npc-floor-6-c2.json :: dataList[key=N106001_C2].displayName
   limit: do 40 znaków
   EN: Sisyphus
   PL: Sisyphus

## Tryb RPG [floor-7] — rpg-loc-location-floor-7-c2
- obszar/warstwa: `floor-7` · plik gry: `RPGSystem/rpg-loc-location-floor-7-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

870. [RPG [170100] — tekst] 밝은 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170100].text
   limit: do 120 znaków
   EN: A Bright Room
   PL: Jasny Pokój
871. [RPG [170200] — tekst] 빈 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170200].text
   limit: do 120 znaków
   EN: An Empty Room
   PL: Pusty Pokój
872. [RPG [170300] — tekst] 어두운 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170300].text
   limit: do 120 znaków
   EN: A Dark Room
   PL: Ciemny Pokój
873. [RPG [170400] — tekst] 어두운 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170400].text
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [RPG [170500] — tekst] 어두운 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170500].text
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [RPG [170600] — tekst] 어두운 방
   źródło: RPGSystem/rpg-loc-location-floor-7-c2.json :: dataList[key=170600].text
   (powtórzenie elementu 872 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-7] — rpg-loc-npc-floor-7-c2
- obszar/warstwa: `floor-7` · plik gry: `RPGSystem/rpg-loc-npc-floor-7-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

876. [RPG [N107001_C2] — nazwa wyświetlana] 잔느
   źródło: RPGSystem/rpg-loc-npc-floor-7-c2.json :: dataList[key=N107001_C2].displayName
   limit: do 40 znaków
   EN: Jeanne
   PL: Jeanne

## Tryb RPG [floor-7] — rpg-loc-player-floor-7-c2
- obszar/warstwa: `floor-7` · plik gry: `RPGSystem/rpg-loc-player-floor-7-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

877. [RPG [999999] — nazwa wyświetlana] 뫼르소
   źródło: RPGSystem/rpg-loc-player-floor-7-c2.json :: dataList[key=999999].displayName
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-7] — rpg-loc-quest-floor-7-c2
- obszar/warstwa: `floor-7` · plik gry: `RPGSystem/rpg-loc-quest-floor-7-c2.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

878. [RPG [Q7001_C2] — tytuł] 밝은 방
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7001_C2].title
   (powtórzenie elementu 870 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [RPG [Q7001_C2] — opis] 뫼르소는 돌을 굴려 꼭대기에 닿았고, 돌은 또 다시 굴러 떨어진다. 그리고 우리가 마침내 닿은 곳은... 백화점의 꼭대기다.
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7001_C2].description
   limit: do 240 znaków
   EN: Meursault rolled the boulder all the way to the summit, only for it to come tumbling down once more. And now, the place we've finally reached is... the very top of the department store.
   PL: Meursault stoczył głaz aż na szczyt, a głaz znów stoczył się na dół. A miejsce, do którego w końcu dotarliśmy, to… sam szczyt domu handlowego.
880. [RPG [Q7001_C2] — krok 1 — cel zadania 1] 향한다.
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7001_C2].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Keep moving forward.
   PL: Idziemy przed siebie.
881. [RPG [Q7001_C2] — krok 2 — cel zadania 1] 그리고 앉는다.
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7001_C2].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: And take a seat.
   PL: A potem siadamy.
882. [RPG [Q7002_C2] — tytuł] ???
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7002_C2].title
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [RPG [Q7002_C2] — krok 1 — cel zadania 1] ???
   źródło: RPGSystem/rpg-loc-quest-floor-7-c2.json :: dataList[key=Q7002_C2].steps[#0].goalDescription1
   (powtórzenie elementu 119 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-9990] — rpg-loc-quest-floor-9990-c1
- obszar/warstwa: `floor-9990` · plik gry: `RPGSystem/rpg-loc-quest-floor-9990-c1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

884. [RPG [Q9990_C1] — tytuł] 운명에 저항하기
   źródło: RPGSystem/rpg-loc-quest-floor-9990-c1.json :: dataList[key=Q9990_C1].title
   limit: do 40 znaków
   EN: Defy Fate
   PL: Sprzeciw się przeznaczeniu
885. [RPG [Q9990_C1] — opis] 이제는 정해진 길에서 벗어나야 한다.
   źródło: RPGSystem/rpg-loc-quest-floor-9990-c1.json :: dataList[key=Q9990_C1].description
   limit: do 120 znaków
   EN: It's time we stepped off the predetermined path.
   PL: Czas zejść z wyznaczonej ścieżki.
886. [RPG [Q9990_C1] — krok 1 — cel zadania 1] 간수를 쓰러뜨리고 운명에 저항하기
   źródło: RPGSystem/rpg-loc-quest-floor-9990-c1.json :: dataList[key=Q9990_C1].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Defeat the Warden and defy fate
   PL: Pokonaj Strażnika i sprzeciw się przeznaczeniu

## Tryb RPG [floor-b1] — rpg-loc-location-floor-b1-b
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-location-floor-b1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

887. [RPG [210300] — tekst] 수산시장
   źródło: RPGSystem/rpg-loc-location-floor-b1-b.json :: dataList[key=210300].text
   limit: do 120 znaków
   EN: Fish Market
   PL: Targ Rybny
888. [RPG [210400] — tekst] 해변
   źródło: RPGSystem/rpg-loc-location-floor-b1-b.json :: dataList[key=210400].text
   limit: do 120 znaków
   EN: The Shore
   PL: Brzeg

## Tryb RPG [floor-b1] — rpg-loc-location-floor-b1
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-location-floor-b1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

889. [RPG [210100] — tekst] 푸드코트
   źródło: RPGSystem/rpg-loc-location-floor-b1.json :: dataList[key=210100].text
   limit: do 120 znaków
   EN: Food Court
   PL: Strefa Gastronomiczna
890. [RPG [210200] — tekst] 신선정육코너
   źródło: RPGSystem/rpg-loc-location-floor-b1.json :: dataList[key=210200].text
   limit: do 120 znaków
   EN: Fresh Meat Section
   PL: Stoisko ze Świeżym Mięsem
891. [RPG [210500] — tekst] 에스컬레이터 홀
   źródło: RPGSystem/rpg-loc-location-floor-b1.json :: dataList[key=210500].text
   limit: do 120 znaków
   EN: Escalator Hall
   PL: Hala Schodów Ruchomych
892. [RPG [210600] — tekst] 우측 복도
   źródło: RPGSystem/rpg-loc-location-floor-b1.json :: dataList[key=210600].text
   limit: do 120 znaków
   EN: Corridor, Right
   PL: Korytarz Prawy
893. [RPG [210700] — tekst] 좌측 복도
   źródło: RPGSystem/rpg-loc-location-floor-b1.json :: dataList[key=210700].text
   limit: do 120 znaków
   EN: Corridor, Left
   PL: Korytarz Lewy

## Tryb RPG [floor-b1] — rpg-loc-npc-floor-b1-a-enemy
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

894. [RPG [N201101] — nazwa wyświetlana] 눈 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201101].displayName
   limit: do 40 znaków
   EN: Eye Taste Tester
   PL: Degustator Ok
895. [RPG [N201102] — nazwa wyświetlana] 코 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201102].displayName
   limit: do 40 znaków
   EN: Nose Taste Tester
   PL: Degustator Nosu
896. [RPG [N201103] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201103].displayName
   limit: do 40 znaków
   EN: Thirsty Kaki
   PL: Spragniony Le Kaki
897. [RPG [N201104] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201104].displayName
   limit: do 40 znaków
   EN: Leather Wallet
   PL: Skórzany Portfel
898. [RPG [N201105] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201105].displayName
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [RPG [N201106] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201106].displayName
   limit: do 40 znaków
   EN: Hungry Kaki
   PL: Głodny Le Kaki
900. [RPG [N201107] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201107].displayName
   limit: do 40 znaków
   EN: Mouth Taste Tester
   PL: Degustator Ust
901. [RPG [N201108] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201108].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [RPG [N201109] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201109].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [RPG [N201110] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-a-enemy.json :: dataList[key=N201110].displayName
   (powtórzenie elementu 897 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b1] — rpg-loc-npc-floor-b1-b-enemy
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

904. [RPG [N201101] — nazwa wyświetlana] 눈 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201101].displayName
   (powtórzenie elementu 894 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [RPG [N201102] — nazwa wyświetlana] 코 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201102].displayName
   (powtórzenie elementu 895 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [RPG [N201103] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201103].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [RPG [N201104] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201104].displayName
   (powtórzenie elementu 897 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [RPG [N201105] — nazwa wyświetlana] 데님 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201105].displayName
   (powtórzenie elementu 101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [RPG [N201106] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201106].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [RPG [N201107] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201107].displayName
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [RPG [N201108] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201108].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [RPG [N201109] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201109].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [RPG [N201110] — nazwa wyświetlana] 가죽 지갑
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201110].displayName
   (powtórzenie elementu 897 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [RPG [N201111] — nazwa wyświetlana] 기어다니는 가죽
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201111].displayName
   limit: do 40 znaków
   EN: Crawling Leather
   PL: Pełzająca Skóra
915. [RPG [N201112] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201112].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [RPG [N201113] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201113].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [RPG [N201114] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201114].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [RPG [N201115] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201115].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [RPG [N201116] — nazwa wyświetlana] 사나워진 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201116].displayName
   limit: do 40 znaków
   EN: Ferocious Thirsty Kaki
   PL: Rozwścieczony Spragniony Le Kaki
920. [RPG [N201117] — nazwa wyświetlana] 사나워진 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201117].displayName
   limit: do 40 znaków
   EN: Ferocious Hungry Kaki
   PL: Rozwścieczony Głodny Le Kaki
921. [RPG [N201118] — nazwa wyświetlana] 사나워진 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201118].displayName
   (powtórzenie elementu 919 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [RPG [N201119] — nazwa wyświetlana] 사나워진 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201119].displayName
   (powtórzenie elementu 920 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [RPG [N201120] — nazwa wyświetlana] 사나워진 눈 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201120].displayName
   limit: do 40 znaków
   EN: Ferocious Eye Taste Tester
   PL: Rozwścieczony Degustator Ok
924. [RPG [N201121] — nazwa wyświetlana] 사나워진 코 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201121].displayName
   limit: do 40 znaków
   EN: Ferocious Nose Taste Tester
   PL: Rozwścieczony Degustator Nosu
925. [RPG [N201122] — nazwa wyświetlana] 사나워진 입 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b-enemy.json :: dataList[key=N201122].displayName
   limit: do 40 znaków
   EN: Ferocious Mouth Taste Tester
   PL: Rozwścieczony Degustator Ust

## Tryb RPG [floor-b1] — rpg-loc-npc-floor-b1-b
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-npc-floor-b1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

926. [RPG [N201002] — nazwa wyświetlana] 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201002].displayName
   limit: do 40 znaków
   EN: Floor Manager
   PL: Kierownik Piętra
927. [RPG [N201003] — nazwa wyświetlana] 수셰프
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201003].displayName
   limit: do 40 znaków
   EN: Sous Chef
   PL: Sous Chef
928. [RPG [N201003A] — nazwa wyświetlana] 수셰프
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201003A].displayName
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [RPG [N201003B] — nazwa wyświetlana] 수셰프
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201003B].displayName
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [RPG [N201003C] — nazwa wyświetlana] 수셰프
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201003C].displayName
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [RPG [N101022] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N101022].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [RPG [N101026] — nazwa wyświetlana] 히스클리프
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N101026].displayName
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [RPG [N201005] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201005].displayName
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [RPG [N201007] — nazwa wyświetlana] 낚시꾼
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201007].displayName
   limit: do 40 znaków
   EN: Fisherman
   PL: Wędkarz
935. [RPG [N201017] — nazwa wyświetlana] 르누아르 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201017].displayName
   limit: do 40 znaków
   EN: Le Noir Porter
   PL: Tragarz Le Noir
936. [RPG [N201018] — nazwa wyświetlana] 르루주 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201018].displayName
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
937. [RPG [N201008] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201008].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
938. [RPG [N201009] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201009].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
939. [RPG [N201034] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201034].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
940. [RPG [N201035] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201035].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
941. [RPG [N201010] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201010].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
942. [RPG [N201019] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201019].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
943. [RPG [N201020] — nazwa wyświetlana] 게걸스러운 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201020].displayName
   limit: do 40 znaków
   EN: Voracious Kaki
   PL: Łakomy Le Kaki
944. [RPG [N201021] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201021].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [RPG [N201022] — nazwa wyświetlana] 허기진 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201022].displayName
   limit: do 40 znaków
   EN: Starving Kaki
   PL: Wygłodniały Le Kaki
946. [RPG [N201023] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201023].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
947. [RPG [N201024] — nazwa wyświetlana] 게걸스러운 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201024].displayName
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
948. [RPG [N201025] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201025].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
949. [RPG [N201026] — nazwa wyświetlana] 무언가의 사체
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201026].displayName
   limit: do 40 znaków
   EN: Unidentifiable Carcass
   PL: Zwłoki Czegoś
950. [RPG [N201027] — nazwa wyświetlana] 어둠의 문
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201027].displayName
   limit: do 40 znaków
   EN: Door into Darkness
   PL: Drzwi do Ciemności
951. [RPG [N201028] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201028].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
952. [RPG [N201029] — nazwa wyświetlana] 허기진 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201029].displayName
   (powtórzenie elementu 945 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
953. [RPG [N201030] — nazwa wyświetlana] 고치
   źródło: RPGSystem/rpg-loc-npc-floor-b1-b.json :: dataList[key=N201030].displayName
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryb RPG [floor-b1] — rpg-loc-npc-floor-b1
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-npc-floor-b1.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

954. [RPG [N201002] — nazwa wyświetlana] 플로어 매니저
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201002].displayName
   (powtórzenie elementu 926 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
955. [RPG [N201003] — nazwa wyświetlana] 수셰프
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201003].displayName
   (powtórzenie elementu 927 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [RPG [N101022] — nazwa wyświetlana] 파우스트
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N101022].displayName
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [RPG [N101024] — nazwa wyświetlana] 그레고르
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N101024].displayName
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
958. [RPG [N201005] — nazwa wyświetlana] 입 시식담당자
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201005].displayName
   (powtórzenie elementu 900 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
959. [RPG [N201017] — nazwa wyświetlana] 르누아르 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201017].displayName
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [RPG [N201018] — nazwa wyświetlana] 르루주 운반자
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201018].displayName
   (powtórzenie elementu 795 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [RPG [N201008] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201008].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
962. [RPG [N201009] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201009].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
963. [RPG [N201010] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201010].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [RPG [N201019] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201019].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
965. [RPG [N201020] — nazwa wyświetlana] 게걸스러운 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201020].displayName
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
966. [RPG [N201021] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201021].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
967. [RPG [N201022] — nazwa wyświetlana] 허기진 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201022].displayName
   (powtórzenie elementu 945 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [RPG [N201023] — nazwa wyświetlana] 배고픈 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201023].displayName
   (powtórzenie elementu 899 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [RPG [N201024] — nazwa wyświetlana] 게걸스러운 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201024].displayName
   (powtórzenie elementu 943 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
970. [RPG [N201025] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201025].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
971. [RPG [N201026] — nazwa wyświetlana] 무언가의 사체
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201026].displayName
   (powtórzenie elementu 949 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [RPG [N201027] — nazwa wyświetlana] 어둠의 문
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201027].displayName
   (powtórzenie elementu 950 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [RPG [N201028] — nazwa wyświetlana] 목마른 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201028].displayName
   (powtórzenie elementu 896 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
974. [RPG [N201029] — nazwa wyświetlana] 허기진 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201029].displayName
   (powtórzenie elementu 945 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
975. [RPG [N201032] — nazwa wyświetlana] 조심스러운 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201032].displayName
   limit: do 40 znaków
   EN: Careful Kaki
   PL: Ostrożny Le Kaki
976. [RPG [N201033] — nazwa wyświetlana] 의심하는 르카키
   źródło: RPGSystem/rpg-loc-npc-floor-b1.json :: dataList[key=N201033].displayName
   limit: do 40 znaków
   EN: Suspicious Kaki
   PL: Podejrzliwy Le Kaki

## Tryb RPG [floor-b1] — rpg-loc-quest-floor-b1-b
- obszar/warstwa: `floor-b1` · plik gry: `RPGSystem/rpg-loc-quest-floor-b1-b.json` (imiona mówców tłumaczone raz w `mowcy-rpg-i-anomalii.md`)

977. [RPG [Q-1000] — tytuł] 지하 1층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1000].title
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
978. [RPG [Q-1000] — opis] 5층 안으로 들어가기에는 미덕이 부족하다고 한다. 뿌이는 황금가죽으로 만든 수의를 입어야 한다고 했다. 지하에 내려가면 가죽을 가공해주는 이가 있다고 했다. 지하로 내려가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1000].description
   (powtórzenie elementu 824 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
979. [RPG [Q-1000] — krok 1 — cel zadania 1] 지하 1층으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1000].steps[#0].goalDescription1
   (powtórzenie elementu 823 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
980. [RPG [Q-1001] — tytuł] 피식자의 사유 찾기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1001].title
   limit: do 50 znaków
   EN: Find the Ruminations of the Prey
   PL: Znajdź Rozmyślania Ofiary
981. [RPG [Q-1001] — opis] 황금고치를 얻기 위해서는 지하 1층의 플로어 매니저인 부셰에게 피식자의 사유를 찾아 건네주어야 했다. 빠르게 이 근처에 있을 피식자의 사유를 찾아보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1001].description
   limit: do 210 znaków
   EN: To obtain the Golden Cocoon, we need to bring the Ruminations of the Prey to Boucher, B1F's Floor Manager. It should be somewhere nearby. Let's find it quickly.
   PL: Żeby zdobyć Złoty Kokon, trzeba dostarczyć Boucherowi, Kierownikowi Piętra poziomu -1, Rozmyślania Ofiary. Powinny być gdzieś w pobliżu. Szybko ich poszukajmy.
982. [RPG [Q-1001] — krok 1 — cel zadania 1] 피식자의 사유 찾기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1001].steps[#0].goalDescription1
   (powtórzenie elementu 980 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [RPG [Q-1002] — tytuł] 수셰프 제압하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1002].title
   limit: do 40 znaków
   EN: Subdue Sous Chef
   PL: Opanuj Sous Chef
984. [RPG [Q-1002] — opis] 피식자의 사유를 챙겨 푸드코트에 도착했다. 뿌이의 냄새를 맡던 수셰프가 갑자기 우리에게 덤벼들었다. 우선 수셰프를 제압하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1002].description
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We returned to the Food Court with the Ruminations of the Prey. After sniffing Pwie a few times, Sous Chef suddenly began attacking us...\n\nFirst, let's subdue Sous Chef.
   PL: Wróciliśmy z Rozmyślaniami Ofiary do Strefy Gastronomicznej. Sous Chef, po powąchaniu Pwie, nagle rzuciła się na nas. Najpierw opanujmy Sous Chef.
985. [RPG [Q-1002] — krok 1 — cel zadania 1] 수셰프 제압하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1002].steps[#0].goalDescription1
   limit: do 120 znaków
   EN: Defeat Sous Chef
   PL: Opanuj Sous Chef
986. [RPG [Q-1003] — tytuł] 지하 1층 플로어 매니저에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1003].title
   limit: do 40 znaków
   EN: Talk to B1F's Floor Manager
   PL: Zagadaj Kierownika Piętra poziomu -1
987. [RPG [Q-1003] — opis] 뿌이의 냄새를 맡던 수셰프가 갑자기 우리에게 덤벼들었다. 피식자의 사유가 있다는 말에 진정하고 우리를 지하 1층 플로어 매니저인 부셰에게 안내해주었다. 부셰에게 말을 걸어보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1003].description
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sous Chef suddenly attacked us after sniffing Pwie a few times, but calmed down once she heard that we'd brought Ruminations of the Prey with us, and agreed to introduce us to Boucher, the Floor Manager at B1F.\n\nLet's talk to Boucher.
   PL: Sous Chef nagle rzuciła się na nas, powąchając Pwie, ale uspokoiła się, gdy usłyszała, że mamy przy sobie Rozmyślania Ofiary, i zgodziła się zaprowadzić nas do Bouchera, Kierownika Piętra poziomu -1. Zagadajmy Bouchera.
988. [RPG [Q-1003] — krok 1 — cel zadania 1] 지하 1층 플로어 매니저에게 말 걸기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1003].steps[#0].goalDescription1
   (powtórzenie elementu 986 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [RPG [Q-1003] — krok 2 — cel zadania 1] 지하 1층 플로어 매니저에게 피식자의 사유를 건네주기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1003].steps[#1].goalDescription1
   limit: do 120 znaków
   EN: Give the Ruminations of the Prey to B1F's Floor Manager
   PL: Przekaż Rozmyślania Ofiary Kierownikowi Piętra poziomu -1
990. [RPG [Q-1004] — tytuł] 해변으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1004].title
   limit: do 40 znaków
   EN: Head to the Shore
   PL: Udaj się na Brzeg
991. [RPG [Q-1004] — opis] 사색이 된 수셰프가 말하길, 창고에 있던 유체가 도망갔다고 한다. 유체는 수산시장을 거치면 곧장 나오는 해변에 있을 거라고 한다. 어쩔 수 없이 우리는 살아있는 유체를 찾기 위해 해변으로 향하기로 했다.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1004].description
   limit: do 280 znaków
   EN: The Sous Chef, panicking, told us that the larva kept in the storage had escaped. It should be on the Shore just beyond the Fish Market. With no other options, we decided to head there and look for a living larva.
   PL: Dopadnięta panika Sous Chef powiedziała nam, że larwa trzymana w magazynie zbiegła. Podobno jest na Brzegu, tuż za Targiem Rybnym. Nie mieliśmy wyboru i postanowiliśmy udać się na Brzeg, by odnaleźć żywą larwę.
992. [RPG [Q-1004] — krok 1 — cel zadania 1] 해변으로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1004].steps[#0].goalDescription1
   (powtórzenie elementu 990 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
993. [RPG [Q-1005] — tytuł] 움직이고 있는 유체 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1005].title
   limit: do 50 znaków
   EN: Investigate the Squirming Larva
   PL: Zbadaj poruszającą się Larwę
994. [RPG [Q-1005] — opis] 해변에 도착했다. 이곳은 바다에 잠기려는 유체들로 가득하다. 하지만 그중에서 움직이고 있는 유체가 하나 보인다. 가까이 다가가보자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1005].description
   limit: do 170 znaków
   EN: We've reached the Shore, where countless larvae are drifting toward the sea. One of them is still moving. We should approach it.
   PL: Dotarliśmy na Brzeg. Pełno tu larw dryfujących ku morzu. Ale jedna z nich wciąż się rusza. Podejdźmy bliżej.
995. [RPG [Q-1005] — krok 1 — cel zadania 1] 움직이고 있는 유체 조사하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1005].steps[#0].goalDescription1
   (powtórzenie elementu 993 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [RPG [Q-1008] — tytuł] 수셰프에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1008].title
   limit: do 40 znaków
   EN: Return to Sous Chef
   PL: Wróć do Sous Chef
997. [RPG [Q-1008] — opis] 겨우 살아 숨 쉬고 있는 유체를 발견했다. 이제 다시 푸드코트로 돌아가 수셰프에게 유체를 건네주자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1008].description
   limit: do 140 znaków
   EN: We found one that's still breathing. Take it back to the Food Court and hand it over to the Sous Chef.
   PL: Znaleźliśmy larwę, która jeszcze oddycha. Wróćmy do Strefy Gastronomicznej i przekażmy ją Sous Chef.
998. [RPG [Q-1008] — krok 1 — cel zadania 1] 수셰프에게 돌아가기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1008].steps[#0].goalDescription1
   (powtórzenie elementu 996 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [RPG [Q-1009] — tytuł] 에스컬레이터 홀로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1009].title
   limit: do 40 znaków
   EN: To the Escalator Hall
   PL: Udaj się do Hali Schodów Ruchomych
1000. [RPG [Q-1009] — opis] 지난번처럼 황금고치… 아니 꼬물이가 만들어졌다. 이제 에스컬레이터들로 가득차 있었던 에스컬레이터 홀로 향하자.
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1009].description
   limit: do 180 znaków
   EN: Just like last time, we've got ourselves a Golden Cocoon... or rather, "Wriggley". Next stop: the Escalator Hall packed with escalators.
   PL: Jak ostatnio stworzono Złoty Kokon… a właściwie „Wriggley”. Następny przystanek: Hala Schodów Ruchomych, wypełniona schodami ruchomymi.
1001. [RPG [Q-1009] — krok 1 — cel zadania 1] 에스컬레이터 홀로 향하기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1009].steps[#0].goalDescription1
   (powtórzenie elementu 999 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [RPG [Q-1010] — tytuł] 에스컬레이터 고르기
   źródło: RPGSystem/rpg-loc-quest-floor-b1-b.json :: dataList[key=Q-1010].title
   limit: do 40 znaków
   EN: Choose an Escalator
   PL: Wybierz schody ruchome
