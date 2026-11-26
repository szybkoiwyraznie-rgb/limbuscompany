# Paczka AI P04 (Fala 1 · 1B) — Interfejs główny, ustawienia, okna dialogowe i formacja (część 2/2)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P04_1b_interfejs_i_ustawienia_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P04_1b_interfejs_i_ustawienia_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Interfejs i ustawienia: MainUIText
- plik gry: `MainUIText.json`

1. [Interfejs i ustawienia [mainui_default_personality_blocked] — tekst] 기본 인격 편성 불가
   źródło: MainUIText.json :: dataList[id=mainui_default_personality_blocked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot\nDeploy\nBase\nIdentity
   PL: Nie można\nwystawić\nTożsamości\nBazowej
2. [Interfejs i ustawienia [mainui_change_personality_of_character] — tekst] {0} 수감자 인격 변경 필요. 지원 인격이 추가됨.
   źródło: MainUIText.json :: dataList[id=mainui_change_personality_of_character].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cannot proceed with this {0} Identity. Support Identities added.
   PL: Wymagana zmiana Tożsamości Grzesznika ({0}). Dodano Tożsamości Wsparcia.
3. [Interfejs i ustawienia [caution] — tekst] 주의
   źródło: MainUIText.json :: dataList[id=caution].content
   limit: do 120 znaków
   EN: WARNING
   PL: UWAGA
4. [Interfejs i ustawienia [announcer_spoiler_caution] — tekst] 해당 아나운서에는 <color=#990000><{0}-{1}></color> 챕터의\n스포일러가 포함되어 있습니다.\n\n확인하시겠습니까?
   źródło: MainUIText.json :: dataList[id=announcer_spoiler_caution].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}, {1}, \n
   EN: This Announcer contains spoilers for Chapter <color=#990000><{0}-{1}></color>.\n\nView anyway?
   PL: Ten Komentator zawiera spoilery z Rozdziału <color=#990000><{0}-{1}></color>.\n\nWyświetlić mimo to?
5. [Interfejs i ustawienia [mass_announcer_spoiler_caution] — tekst] 수령 목록에 클리어 하지 않은 챕터의\n스포일러가 될 수 있는 아나운서가\n포함되어 있습니다.\n\n보상을 수령하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mass_announcer_spoiler_caution].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the rewards you are about to claim\nincludes an Announcer who may contain spoilers\nfor a Chapter you haven't cleared yet.\n\nClaim them anyway?
   PL: Wśród odbieranych nagród znajduje się Komentator,\nktóry może zawierać spoilery z nieukończonego\nprzez ciebie rozdziału.\n\nOdebrać mimo to?
6. [Interfejs i ustawienia [vending_machine_item_available_date_label] — tekst] {0}월 {1}일 {2} ({3}) 부터 자판기 교환 가능
   źródło: MainUIText.json :: dataList[id=vending_machine_item_available_date_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, \n
   EN: Dispenser Unlock:\n{0}/{1} {2} ({3})
   PL: Dostępne w Automacie od:\n{1}.{0} {2} ({3})
7. [Interfejs i ustawienia [gacha_notice_vending_available_date] — tekst] 시즌 인격은 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal Identities can be Dispensed from the Dispenser starting from {0}/{1} {2} ({3})
   PL: Sezonowe Tożsamości będzie można wymienić w Automacie od {1}.{0} {2} ({3}).
8. [Interfejs i ustawienia [gacha_notice_vending_available_date_v2] — tekst] 시즌 E.G.O는 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date_v2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal E.G.O can be Dispensed starting from {0}/{1} {2} ({3})
   PL: Sezonowe E.G.O będzie można wymienić w Automacie od {1}.{0} {2} ({3}).
9. [Interfejs i ustawienia [gacha_notice_vending_available_date_v3] — tekst] 시즌 인격·E.G.O는 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date_v3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal ID & E.G.O can be Dispensed starting from {0}/{1} {2} ({3})
   PL: Sezonowe Tożsamości i E.G.O będzie można wymienić w Automacie od {1}.{0} {2} ({3}).
10. [Interfejs i ustawienia [mini_story_warning_spoiler_checkbox_desc] — tekst] 팝업 다시 보지 않기
   źródło: MainUIText.json :: dataList[id=mini_story_warning_spoiler_checkbox_desc].content
   limit: do 120 znaków
   EN: Don't see this message again
   PL: Nie pokazuj ponownie tego okna
11. [Interfejs i ustawienia [mainui_settings_push_notification] — tekst] 알림 설정
   źródło: MainUIText.json :: dataList[id=mainui_settings_push_notification].content
   limit: do 120 znaków
   EN: Notification Settings
   PL: Ustawienia powiadomień
12. [Interfejs i ustawienia [paid_lunacy_ui] — tekst] 유료 광기
   źródło: MainUIText.json :: dataList[id=paid_lunacy_ui].content
   limit: do 120 znaków
   EN: Paid Lunacy
   PL: Płatne Szaleństwo
13. [Interfejs i ustawienia [story_unable_to_skip] — tekst] 스킵할 수 없는 스토리입니다.
   źródło: MainUIText.json :: dataList[id=story_unable_to_skip].content
   limit: do 120 znaków
   EN: This story cannot be skipped.
   PL: Tej sceny fabularnej nie można pominąć.
14. [Interfejs i ustawienia [remote_download_quit_game] — tekst] 새로운 다운로드 항목이 추가되었습니다.\n게임이 종료되며, 재시작을 통해 다운로드 받아주시기 바랍니다.
   źródło: MainUIText.json :: dataList[id=remote_download_quit_game].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new download has been added.\nThe game will be closed; please restart the game to download the update.
   PL: Dodano nowe pliki do pobrania.\nGra zostanie zamknięta — uruchom ją ponownie, aby pobrać aktualizację.
15. [Interfejs i ustawienia [mainui_settings_battle_speech] — tekst] 전투 중 대사 자막
   źródło: MainUIText.json :: dataList[id=mainui_settings_battle_speech].content
   limit: do 120 znaków
   EN: In-combat Dialogue Subtitles
   PL: Napisy dialogów w trakcie walki
16. [Interfejs i ustawienia [unable_to_upgrade_sync_level_by_main_story_1] — tekst] 주요 이야기\n1장 클리어 시\n자동 진행
   źródło: MainUIText.json :: dataList[id=unable_to_upgrade_sync_level_by_main_story_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upties upon\nclearing\nCanto I
   PL: Automatycznie\npo ukończeniu\nCanto I
17. [Interfejs i ustawienia [unable_to_upgrade_sync_level_by_main_story_2] — tekst] 주요 이야기\n2장 클리어 시\n자동 진행
   źródło: MainUIText.json :: dataList[id=unable_to_upgrade_sync_level_by_main_story_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upties upon\nclearing\nCanto II
   PL: Automatycznie\npo ukończeniu\nCanto II
18. [Interfejs i ustawienia [exp_dungeon_opened_desc] — tekst] 경험치 채광이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=exp_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: EXP Luxcavation has been unlocked.
   PL: Odblokowano Wydobycie PD.
19. [Interfejs i ustawienia [abnormality_tutorial_battle_participate_desc] — tekst] 전투에 참여할 수감자 5명을 선택해주세요.
   źródło: MainUIText.json :: dataList[id=abnormality_tutorial_battle_participate_desc].content
   limit: do 120 znaków
   EN: Select five Sinners to participate in this Encounter.
   PL: Wybierz 5 Grzeszników do udziału w walce.
20. [Interfejs i ustawienia [thread_dungeon_opened_desc] — tekst] 끈 채광이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=thread_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: Thread Luxcavation has been unlocked.
   PL: Odblokowano Wydobycie Nici.
21. [Interfejs i ustawienia [mirror_dungeon_opened_desc] — tekst] 거울 던전이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=mirror_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: Mirror Dungeon has been unlocked.
   PL: Odblokowano Lustrzany Loch.
22. [Interfejs i ustawienia [ego_gift_combine_explain_title] — tekst] 합성 조합식
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_title].content
   limit: do 120 znaków
   EN: Fusion Recipes
   PL: Receptury Syntezy
23. [Interfejs i ustawienia [ego_gift_combine_explain_label_keyword] — tekst] 키워드
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_keyword].content
   limit: do 120 znaków
   EN: Keywords
   PL: Słowa kluczowe
24. [Interfejs i ustawienia [ego_gift_combine_explain_label_attack_type] — tekst] 공격 유형
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_attack_type].content
   limit: do 120 znaków
   EN: Attack Type
   PL: Typ ataku
25. [Interfejs i ustawienia [ego_gift_combine_explain_label_etc] — tekst] 기타
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_etc].content
   limit: do 120 znaków
   EN: Other
   PL: Inne
26. [Interfejs i ustawienia [ego_gift_combine_explain_button_label] — tekst] 조합식
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_button_label].content
   limit: do 120 znaków
   EN: Recipes
   PL: Receptury
27. [Interfejs i ustawienia [ego_gift_combine_explain_no_item_list] — tekst] 관련된 E.G.O 기프트 합성 조합식이 없습니다.
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_no_item_list].content
   limit: do 120 znaków
   EN: No E.G.O Gift Fusion Recipe search result.
   PL: Brak powiązanych receptur syntezy Darów E.G.O.
28. [Interfejs i ustawienia [ego_gift_combine_explain_required_label] — tekst] {0}종 중 {1}개
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_required_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} of {0}
   PL: {1} z {0}
29. [Interfejs i ustawienia [attendance_event_s6_desc] — tekst] 이벤트 기간 동안 누적 출석일에 따라 보상을 획득할 수 있으며, 보상은 해당 팝업 등장과 함께 자동으로 수령합니다.\n\n총 14일 출석 시, 모든 보상을 획득할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=attendance_event_s6_desc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Earn rewards based on your attendance during the Event period. Rewards are automatically claimed when the pop-up window appears.\n\nCollect 14 cumulative attendance checks to receive all rewards.
   PL: W okresie wydarzenia zdobywasz nagrody za łączną liczbę dni logowania; nagrody odbierane są automatycznie po wyświetleniu tego okna.\n\nZaloguj się łącznie przez 14 dni, aby odebrać wszystkie nagrody.
30. [Interfejs i ustawienia [formation_none_selected_desc] — tekst] 편성 순서가 지정된 수감자가 없습니다.\n\n수감자의 편성 순서를 지정해주세요.
   źródło: MainUIText.json :: dataList[id=formation_none_selected_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You haven't Deployed any Sinners.\n\nSelect the Sinners to set the Deployment order.
   PL: Nie wyznaczono kolejności wystawienia żadnego Grzesznika.\n\nWybierz Grzeszników, aby ustalić kolejność wystawienia.
31. [Interfejs i ustawienia [ego_gift_category_current_theme] — tekst] 테마팩 한정 합성 기프트
   źródło: MainUIText.json :: dataList[id=ego_gift_category_current_theme].content
   limit: do 120 znaków
   EN: Theme Pack Exclusive Fusion Gift
   PL: Dar Syntezy na wyłączność Pakietu Tematycznego
32. [Interfejs i ustawienia [mainui_exp_dungeon_10_title] — tekst] 경험치 채광-8 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_10_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Slash)
   PL: Wydobycie PD #8 (Cięcie)
33. [Interfejs i ustawienia [mainui_exp_dungeon_10_open_day] — tekst] 경험치 채광 8단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_10_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Slash) opens on MON, TUE, and SUN.
   PL: Wydobycie PD #8 (Cięcie) jest otwarte w poniedziałki, wtorki i niedziele.
34. [Interfejs i ustawienia [mainui_exp_dungeon_11_title] — tekst] 경험치 채광-8 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_11_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Pierce)
   PL: Wydobycie PD #8 (Kłucie)
35. [Interfejs i ustawienia [mainui_exp_dungeon_11_open_day] — tekst] 경험치 채광 8단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_11_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Pierce) opens on WED, THU, and SUN.
   PL: Wydobycie PD #8 (Kłucie) jest otwarte w środy, czwartki i niedziele.
36. [Interfejs i ustawienia [mainui_exp_dungeon_12_title] — tekst] 경험치 채광-8 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_12_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Blunt)
   PL: Wydobycie PD #8 (Obuch)
37. [Interfejs i ustawienia [mainui_exp_dungeon_12_open_day] — tekst] 경험치 채광 8단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_12_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Blunt) opens on FRI, SAT, and SUN.
   PL: Wydobycie PD #8 (Obuch) jest otwarte w piątki, soboty i niedziele.
38. [Interfejs i ustawienia [mainui_notice_download_failed] — tekst] 공지사항을 로드하지 못했습니다. 네트워크를 확인해주세요.
   źródło: MainUIText.json :: dataList[id=mainui_notice_download_failed].content
   limit: do 120 znaków
   EN: Could not load notices. Please check your network connection.
   PL: Nie udało się wczytać ogłoszeń. Sprawdź połączenie sieciowe.
39. [Interfejs i ustawienia [mainui_settings_show_importance_level_UI] — tekst] 중요도 표기
   źródło: MainUIText.json :: dataList[id=mainui_settings_show_importance_level_UI].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Show Battle Hints\n(Gimmick Priority)
   PL: Wskazówki priorytetu\nw walce
40. [Interfejs i ustawienia [mainui_settings_battle_result_announcer] — tekst] 전투 종료 아나운서 음성 재생 완료 대기
   źródło: MainUIText.json :: dataList[id=mainui_settings_battle_result_announcer].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wait for Announcer Lines\nto end after Battle
   PL: Czekaj na koniec kwestii\nKomentatora po walce
41. [Interfejs i ustawienia [jiaxicun_level] — tekst] 가주 레벨
   źródło: MainUIText.json :: dataList[id=jiaxicun_level].content
   limit: do 120 znaków
   EN: Hierarch Level
   PL: Poziom Głowy Rodu
42. [Interfejs i ustawienia [mainui_settings_stage_continue] — tekst] 컨티뉴
   źródło: MainUIText.json :: dataList[id=mainui_settings_stage_continue].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuacja
43. [Interfejs i ustawienia [defence_skill_with_index] — tekst] 수비{0}
   źródło: MainUIText.json :: dataList[id=defence_skill_with_index].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Def. {0}
   PL: Obr. {0}
44. [Interfejs i ustawienia [servererror_invalid_battle_version] — tekst] 버전이 업데이트 되었습니다.\n리소스 다운로드 후 다시 시도해주세요.
   źródło: MainUIText.json :: dataList[id=servererror_invalid_battle_version].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Version update available.\nPlease download new resources and try again.
   PL: Wersja gry została zaktualizowana.\nPobierz nowe zasoby i spróbuj ponownie.
45. [Interfejs i ustawienia [gacha_rate_info_intro1_1_announcer_rate] — tekst] ※ 아나운서 등장 확률은 기존의 3성 인격 또는 E.G.O 등장 확률에는 영향을 주지 않으며, 대신 2성 또는 1성 인격의 등장 확률에서 차감되어 반영됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1_announcer_rate].content
   limit: do 190 znaków
   EN: ※ Announcer Extraction rate does not affect 3★ IDs or E.G.O rates. Instead, 2★ and 1★ IDs will have lowered rates to make room for the Announcer.
   PL: ※ Szansa wylosowania Komentatora nie wpływa na szanse Tożsamości 3★ ani E.G.O — jest odejmowana od puli szans Tożsamości 2★ i 1★.
46. [Interfejs i ustawienia [mainui_exp_dungeon_13_title] — tekst] 경험치 채광-9 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_13_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Slash)
   PL: Wydobycie PD #9 (Cięcie)
47. [Interfejs i ustawienia [mainui_exp_dungeon_13_open_day] — tekst] 경험치 채광 9단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_13_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Slash) opens on MON, TUE, and SUN.
   PL: Wydobycie PD #9 (Cięcie) jest otwarte w poniedziałki, wtorki i niedziele.
48. [Interfejs i ustawienia [mainui_exp_dungeon_14_title] — tekst] 경험치 채광-9 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_14_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Pierce)
   PL: Wydobycie PD #9 (Kłucie)
49. [Interfejs i ustawienia [mainui_exp_dungeon_14_open_day] — tekst] 경험치 채광 9단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_14_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Pierce) opens on WED, THU, and SUN.
   PL: Wydobycie PD #9 (Kłucie) jest otwarte w środy, czwartki i niedziele.
50. [Interfejs i ustawienia [mainui_exp_dungeon_15_title] — tekst] 경험치 채광-9 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_15_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Blunt)
   PL: Wydobycie PD #9 (Obuch)
51. [Interfejs i ustawienia [mainui_exp_dungeon_15_open_day] — tekst] 경험치 채광 9단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_15_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Blunt) opens on FRI, SAT, and SUN.
   PL: Wydobycie PD #9 (Obuch) jest otwarte w piątki, soboty i niedziele.
52. [Interfejs i ustawienia [assistant_level] — tekst] 캐릭터 레벨
   źródło: MainUIText.json :: dataList[id=assistant_level].content
   limit: do 120 znaków
   EN: Character Level
   PL: Poziom Postaci
53. [Interfejs i ustawienia [mainui_ego_gift_keyword] — tekst] 키워드
   źródło: MainUIText.json :: dataList[id=mainui_ego_gift_keyword].content
   limit: do 120 znaków
   EN: Keyword
   PL: Słowo kluczowe
54. [Interfejs i ustawienia [mainui_ego_gift_grade] — tekst] 등급
   źródło: MainUIText.json :: dataList[id=mainui_ego_gift_grade].content
   limit: do 120 znaków
   EN: Tier
   PL: Ranga
55. [Interfejs i ustawienia [mainui_use_random_piece_package] — tekst] 자아 파편 상자 사용
   źródło: MainUIText.json :: dataList[id=mainui_use_random_piece_package].content
   limit: do 120 znaków
   EN: Use Egoshard Crate
   PL: Użyj Skrzynki Odłamków E.G.O
56. [Interfejs i ustawienia [mainui_use_optional_piece_package] — tekst] 자아 파편 선택 상자 사용
   źródło: MainUIText.json :: dataList[id=mainui_use_optional_piece_package].content
   limit: do 120 znaków
   EN: Use Nominable Egoshard Crate
   PL: Użyj Imiennej Skrzynki Odłamków E.G.O
57. [Interfejs i ustawienia [mainui_battleresult_consumable] — tekst] 소모 모듈
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_consumable].content
   limit: do 120 znaków
   EN: Module Cost
   PL: Zużyte Moduły
58. [Interfejs i ustawienia [mainui_cont_mine_title] — tekst] 연속 진행
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_title].content
   limit: do 120 znaków
   EN: Consecutive Battle
   PL: Walka Seryjna
59. [Interfejs i ustawienia [mainui_cont_mine_daily_bonus_desc] — tekst] 일일 추가 보상 {0}회 적용
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_daily_bonus_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Daily Bonuses Applied
   PL: Zastosowano bonusy dzienne: {0}
60. [Interfejs i ustawienia [mainui_cont_mine_invalid_text] — tekst] 1회 클리어 이후 연속 진행 가능
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_invalid_text].content
   limit: do 120 znaków
   EN: Clear Stage once to unlock Consecutive Battle
   PL: Ukończ etap 1 raz, aby odblokować Walkę Seryjną
61. [Interfejs i ustawienia [mainui_ego_sync_level_up_select_item] — tekst] 재화 제작 재료 선택
   źródło: MainUIText.json :: dataList[id=mainui_ego_sync_level_up_select_item].content
   limit: do 120 znaków
   EN: Select Crafting Ingredients
   PL: Wybierz materiały do wytworzenia
62. [Interfejs i ustawienia [mainui_passive_skill_upgrade] — tekst] 패시브 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_passive_skill_upgrade].content
   limit: do 120 znaków
   EN: Passives Upgraded
   PL: Ulepszono pasywkę
63. [Interfejs i ustawienia [mainui_new_passive_skill_upgrade] — tekst] 패시브 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_new_passive_skill_upgrade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Passive Enhanced: [{0}]
   PL: Ulepszono pasywkę: [{0}]
64. [Interfejs i ustawienia [formation_announcer_preset_name] — tekst] 프리셋 #{0}
   źródło: MainUIText.json :: dataList[id=formation_announcer_preset_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Preset #{0}
   PL: Zestaw #{0}
65. [Interfejs i ustawienia [formation_announcer_preset_title] — tekst] 아나운서 프리셋
   źródło: MainUIText.json :: dataList[id=formation_announcer_preset_title].content
   limit: do 120 znaków
   EN: Announcers Preset
   PL: Zestawy Komentatorów
66. [Interfejs i ustawienia [formation_announcer_reset_desc] — tekst] {0}을(를) 초기화하시겠습니까?
   źródło: MainUIText.json :: dataList[id=formation_announcer_reset_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Are you sure you want to reset {0}?
   PL: Czy na pewno chcesz zresetować {0}?
67. [Interfejs i ustawienia [mainui_exp_dungeon_16_title] — tekst] 경험치 채광-10 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_16_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Slash)
   PL: Wydobycie PD #10 (Cięcie)
68. [Interfejs i ustawienia [mainui_exp_dungeon_16_open_day] — tekst] 경험치 채광 10단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_16_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Slash) opens on MON, TUE, and SUN.
   PL: Wydobycie PD #10 (Cięcie) jest otwarte w poniedziałki, wtorki i niedziele.
69. [Interfejs i ustawienia [mainui_exp_dungeon_17_title] — tekst] 경험치 채광-10 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_17_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Pierce)
   PL: Wydobycie PD #10 (Kłucie)
70. [Interfejs i ustawienia [mainui_exp_dungeon_17_open_day] — tekst] 경험치 채광 10단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_17_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Pierce) opens on WED, THU, and SUN.
   PL: Wydobycie PD #10 (Kłucie) jest otwarte w środy, czwartki i niedziele.
71. [Interfejs i ustawienia [mainui_exp_dungeon_18_title] — tekst] 경험치 채광-10 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_18_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Blunt)
   PL: Wydobycie PD #10 (Obuch)
72. [Interfejs i ustawienia [mainui_exp_dungeon_18_open_day] — tekst] 경험치 채광 10단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_18_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Blunt) opens on FRI, SAT, and SUN.
   PL: Wydobycie PD #10 (Obuch) jest otwarte w piątki, soboty i niedziele.
73. [Interfejs i ustawienia [unitinfo_tab_synergy] — tekst] 시너지
   źródło: MainUIText.json :: dataList[id=unitinfo_tab_synergy].content
   limit: do 120 znaków
   EN: Synergy
   PL: Synergia
74. [Interfejs i ustawienia [unitinfo_synergy_unsatisfied] — tekst] 조건 {0}개 불충족
   źródło: MainUIText.json :: dataList[id=unitinfo_synergy_unsatisfied].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} condition(s) unmet
   PL: Niespełnione warunki: {0}
75. [Interfejs i ustawienia [limtochess_entrance_coming_soon] — tekst] 준비 중입니다.
   źródło: MainUIText.json :: dataList[id=limtochess_entrance_coming_soon].content
   limit: do 120 znaków
   EN: Under construction
   PL: W przygotowaniu.

## Interfejs i ustawienia: MainUIText_UPDATE_ON_0720
- plik gry: `MainUIText_UPDATE_ON_0720.json`

76. [Interfejs i ustawienia [move_to_inventory] — tekst] 인벤토리 이동
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=move_to_inventory].content
   limit: do 120 znaków
   EN: Go to Inventory
   PL: Przejdź do Ekwipunku
77. [Interfejs i ustawienia [progress_personality_gacksung] — tekst] 동기화 진행
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=progress_personality_gacksung].content
   limit: do 120 znaków
   EN: Uptie
   PL: Synchronizuj
78. [Interfejs i ustawienia [mainui_reinforce_support_passive] — tekst] 서포트 패시브 [{0}] 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_reinforce_support_passive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Support Passive [{0}] Enhanced
   PL: Ulepszono pasywkę wsparcia: [{0}]
79. [Interfejs i ustawienia [mainui_reinforce_battle_passive] — tekst] 전투 패시브 [{0}] 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_reinforce_battle_passive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Combat Passive [{0}] Enhanced
   PL: Ulepszono pasywkę bojową: [{0}]
80. [Interfejs i ustawienia [mainui_battle_passsive_reinforce] — tekst] 전투 패시브 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_battle_passsive_reinforce].content
   limit: do 120 znaków
   EN: Combat Passive Enhanced
   PL: Ulepszono pasywkę bojową
81. [Interfejs i ustawienia [mainui_support_passsive_reinforce] — tekst] 서포트 패시브 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_support_passsive_reinforce].content
   limit: do 120 znaków
   EN: Support Passive Enhanced
   PL: Ulepszono pasywkę wsparcia
82. [Interfejs i ustawienia [mainui_target_num_label] — tekst] 공격 가중치
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_target_num_label].content
   limit: do 120 znaków
   EN: Atk Weight
   PL: Waga Ataku
83. [Interfejs i ustawienia [mainui_awaken_requirement_label] — tekst] 필요 재화 수량
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_awaken_requirement_label].content
   limit: do 120 znaków
   EN: Currency Req.
   PL: Wymagane zasoby

## Interfejs i ustawienia: UpgradeCharacterUI
- plik gry: `UpgradeCharacterUI.json`

84. [Interfejs i ustawienia [upgrade_character_exp_up] — tekst] 경험치가\n상승했습니다.
   źródło: UpgradeCharacterUI.json :: dataList[id=upgrade_character_exp_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Experience\ngained.
   PL: Zdobyto\ndoświadczenie.
85. [Interfejs i ustawienia [upgrade_character_level_up] — tekst] 레벨 상승
   źródło: UpgradeCharacterUI.json :: dataList[id=upgrade_character_level_up].content
   limit: do 120 znaków
   EN: Level Up
   PL: Awans Poziomu
86. [Interfejs i ustawienia [upgrade_character_level_max] — tekst] <color=#f8c200>최대 레벨</color>에\n도달했습니다.
   źródło: UpgradeCharacterUI.json :: dataList[id=upgrade_character_level_max].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: <color=#f8c200>MAX LEVEL</color>\nhas been reached.
   PL: Osiągnięto\n<color=#f8c200>MAKSYMALNY POZIOM</color>.

## Interfejs i ustawienia: kr_settings-ui-donttranslate
- plik gry: `kr_settings-ui-donttranslate.json`

87. [Interfejs i ustawienia [mainui_settings_game] — tekst] 기본 설정
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_game].content
   limit: do 120 znaków
   EN: General
   PL: Ogólne
88. [Interfejs i ustawienia [mainui_settings_ego_fast_forward_speed] — tekst] E.G.O 빠른 재생 배속
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_ego_fast_forward_speed].content
   limit: do 120 znaków
   EN: E.G.O Fast-forward Speed
   PL: Szybkość przyspieszenia E.G.O
89. [Interfejs i ustawienia [mainui_settings_graphic] — tekst] 그래픽
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_graphic].content
   limit: do 120 znaków
   EN: Graphics
   PL: Grafika
90. [Interfejs i ustawienia [mainui_settings_sound] — tekst] 음성
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_sound].content
   limit: do 120 znaków
   EN: Audio
   PL: Dźwięk
91. [Interfejs i ustawienia [mainui_settings_notice] — tekst] 알림
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_notice].content
   limit: do 120 znaków
   EN: Notifs
   PL: Powiadomienia
92. [Interfejs i ustawienia [mainui_settings_etc] — tekst] 기타
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_etc].content
   limit: do 120 znaków
   EN: Misc.
   PL: Inne
93. [Interfejs i ustawienia [mainui_settings_download] — tekst] 다운로드
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_download].content
   limit: do 120 znaków
   EN: Download
   PL: Pobieranie
94. [Interfejs i ustawienia [mainui_settings_download_complete] — tekst] 다운로드 완료
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_download_complete].content
   limit: do 120 znaków
   EN: Download Complete
   PL: Pobieranie zakończone
95. [Interfejs i ustawienia [mainui_settings_video_resource] — tekst] 영상 리소스
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_video_resource].content
   limit: do 120 znaków
   EN: Video Resources
   PL: Zasoby wideo
96. [Interfejs i ustawienia [mainui_settings_audio_resource] — tekst] 음성 리소스
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_audio_resource].content
   limit: do 120 znaków
   EN: Audio Resources
   PL: Zasoby głosowe
97. [Interfejs i ustawienia [mainui_settings_animation_resource] — tekst] 애니메이션 리소스
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_animation_resource].content
   limit: do 120 znaków
   EN: Animation Resources
   PL: Zasoby animacji
98. [Interfejs i ustawienia [mainui_settings_ego_presentation] — tekst] E.G.O 연출
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_ego_presentation].content
   limit: do 120 znaków
   EN: E.G.O Animation
   PL: Animacje E.G.O
99. [Interfejs i ustawienia [mainui_settings_on] — tekst] 켜기
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_on].content
   limit: do 120 znaków
   EN: On
   PL: Wł.
100. [Interfejs i ustawienia [mainui_settings_off] — tekst] 끄기
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_off].content
   limit: do 120 znaków
   EN: Off
   PL: Wył.
101. [Interfejs i ustawienia [mainui_settings_play_once_per_day] — tekst] 하루에 한 번만 재생
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_play_once_per_day].content
   limit: do 120 znaków
   EN: Once per Day
   PL: Raz dziennie
102. [Interfejs i ustawienia [mainui_settings_resolution] — tekst] 해상도
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_resolution].content
   limit: do 120 znaków
   EN: Resolution
   PL: Rozdzielczość
103. [Interfejs i ustawienia [mainui_settings_resolution_windowded] — tekst] 창모드
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_resolution_windowded].content
   limit: do 120 znaków
   EN: Windowed
   PL: W oknie
104. [Interfejs i ustawienia [mainui_settings_resolution_fullscreen] — tekst] 전체화면
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_resolution_fullscreen].content
   limit: do 120 znaków
   EN: Fullscreen
   PL: Pełny ekran
105. [Interfejs i ustawienia [mainui_settings_texquality] — tekst] 텍스쳐 품질
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_texquality].content
   limit: do 120 znaków
   EN: Texture Quality
   PL: Jakość tekstur
106. [Interfejs i ustawienia [mainui_settings_resolution_warning] — tekst] 화질이 높을수록 전력 소모 증가 및 발열 현상이 유발될 수 있습니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_resolution_warning].content
   limit: do 120 znaków
   EN: Higher resolutions may cause the device to heat and consume additional power.
   PL: Wyższa rozdzielczość może zwiększać zużycie energii i nagrzewanie urządzenia.
107. [Interfejs i ustawienia [mainui_settings_fps_warning] — tekst] 프레임이 높을수록 전력 소모 및 발열 현상이 유발될 수 있습니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_fps_warning].content
   limit: do 120 znaków
   EN: Higher framerates may cause the device to heat and consume additional power.
   PL: Wyższa liczba klatek może zwiększać zużycie energii i nagrzewanie urządzenia.
108. [Interfejs i ustawienia [mainui_settings_low] — tekst] 저
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_low].content
   limit: do 120 znaków
   EN: Low
   PL: Niska
109. [Interfejs i ustawienia [mainui_settings_middle] — tekst] 중
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_middle].content
   limit: do 120 znaków
   EN: Medium
   PL: Średnia
110. [Interfejs i ustawienia [mainui_settings_high] — tekst] 고
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_high].content
   limit: do 120 znaków
   EN: High
   PL: Wysoka
111. [Interfejs i ustawienia [mainui_settings_postprocessing] — tekst] 포스트프로세싱
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_postprocessing].content
   limit: do 120 znaków
   EN: Post-processing
   PL: Post-processing
112. [Interfejs i ustawienia [mainui_settings_ppon] — tekst] 켜기
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_ppon].content
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
113. [Interfejs i ustawienia [mainui_settings_ppoff] — tekst] 끄기
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_ppoff].content
   (powtórzenie elementu 100 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
114. [Interfejs i ustawienia [mainui_settings_ppdesc] — tekst] 전투에서 사용하는 카메라 효과를 제어합니다. 성능에 영향을 줍니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_ppdesc].content
   limit: do 120 znaków
   EN: Controls camera effects in battle. Affects game performance.
   PL: Steruje efektami kamery w walce. Wpływa na wydajność gry.
115. [Interfejs i ustawienia [mainui_settings_antialiasing] — tekst] 안티앨리어싱
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_antialiasing].content
   limit: do 120 znaków
   EN: Anti-aliasing
   PL: Wygładzanie krawędzi
116. [Interfejs i ustawienia [mainui_settings_clear] — tekst] 설정 초기화
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_clear].content
   limit: do 120 znaków
   EN: Reset
   PL: Resetuj ustawienia
117. [Interfejs i ustawienia [mainui_settings_clear_ask] — tekst] 모든 설정을 초기화하시겠습니까?
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_clear_ask].content
   limit: do 120 znaków
   EN: Reset everything to default?
   PL: Przywrócić wszystkie ustawienia do wartości domyślnych?
118. [Interfejs i ustawienia [mainui_settings_render_acceleration] — tekst] 렌더링 가속
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_render_acceleration].content
   limit: do 120 znaków
   EN: Accelerated Rendering
   PL: Akceleracja renderowania
119. [Interfejs i ustawienia [mainui_settings_sound_master] — tekst] 마스터
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_sound_master].content
   limit: do 120 znaków
   EN: Master
   PL: Ogólna
120. [Interfejs i ustawienia [mainui_settings_sound_sfx] — tekst] 효과음
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_sound_sfx].content
   limit: do 120 znaków
   EN: SFX
   PL: Efekty dźwiękowe
121. [Interfejs i ustawienia [mainui_settings_sound_voice] — tekst] 보이스
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_sound_voice].content
   limit: do 120 znaków
   EN: Voice
   PL: Dialogi
122. [Interfejs i ustawienia [mainui_settings_sound_battle_announcer] — tekst] 아나운서
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_sound_battle_announcer].content
   limit: do 120 znaków
   EN: Announcer
   PL: Komentator
123. [Interfejs i ustawienia [mainui_settings_notice_enkephalin_full] — tekst] 엔케팔린 충전 완료 알림
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_notice_enkephalin_full].content
   limit: do 120 znaków
   EN: Enkephalin Recovery
   PL: Pełne naładowanie Enkefaliny
124. [Interfejs i ustawienia [mainui_settings_notice_ads] — tekst] 홍보성 알림
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_notice_ads].content
   limit: do 120 znaków
   EN: Promotional Notices
   PL: Powiadomienia promocyjne
125. [Interfejs i ustawienia [mainui_settings_notice_ads_night] — tekst] 홍보성 알림 (야간)
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_notice_ads_night].content
   limit: do 120 znaków
   EN: Promotional Notices (Night)
   PL: Powiadomienia promocyjne (nocne)
126. [Interfejs i ustawienia [mainui_settings_change_launguage] — tekst] 언어 변경
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_change_launguage].content
   limit: do 120 znaków
   EN: Language
   PL: Zmiana języka
127. [Interfejs i ustawienia [mainui_settings_change_launguage_ask] — tekst] 언어 변경은 게임 재시작 시 정상 적용됩니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_change_launguage_ask].content
   limit: do 120 znaków
   EN: Language changes apply after restarting the game.
   PL: Zmiana języka zostanie zastosowana po ponownym uruchomieniu gry.
128. [Interfejs i ustawienia [mainui_settings_faq_btn] — tekst] 고객 센터
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_faq_btn].content
   limit: do 120 znaków
   EN: Customer Service
   PL: Obsługa klienta
129. [Interfejs i ustawienia [connect_to_google_account] — tekst] Google 연동
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=connect_to_google_account].content
   limit: do 120 znaków
   EN: Link with Google
   PL: Powiąż z Google
130. [Interfejs i ustawienia [connect_to_apple_account] — tekst] Apple 연동
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=connect_to_apple_account].content
   limit: do 120 znaków
   EN: Link with Apple
   PL: Powiąż z Apple
131. [Interfejs i ustawienia [explain_sucession] — tekst] 이용하시는 계정 탈퇴 시 모든 계정 및 구매 정보가 삭제됩니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=explain_sucession].content
   limit: do 120 znaków
   EN: If you close the account, all gameplay and purchase data will be deleted.
   PL: Usunięcie konta spowoduje bezpowrotne skasowanie wszystkich danych gry oraz historii zakupów.
132. [Interfejs i ustawienia [explain_sucession_remain_days] — tekst] 계정 탈퇴 기간은 7일이며 기간 내 접속 시 탈퇴 취소가 가능합니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=explain_sucession_remain_days].content
   limit: do 150 znaków
   EN: You will be given a 7-day grace period. You can restore the account if you sign in before the end of the period.
   PL: Okres karencji przed usunięciem konta wynosi 7 dni — zalogowanie się w tym czasie pozwala anulować usunięcie.
133. [Interfejs i ustawienia [explain_writing_code_for_sucession] — tekst] ※ 위 내용에 동의하실 경우,\n텍스트 박스 내 문자를 입력해주세요.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=explain_writing_code_for_sucession].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ If you agree to the terms above,\nplease enter the letters you see in the box.
   PL: ※ Jeśli zgadzasz się z powyższymi warunkami,\nwpisz tekst widoczny w polu poniżej.
134. [Interfejs i ustawienia [explain_secession_status] — tekst] 해당 계정은 탈퇴 처리 중입니다.\n남은시간 : {0} 일 {1} 시간 {2} 분\n지금 로그인 하시면 복구할 수 있습니다.\n계정 복구 하시겠습니까?
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=explain_secession_status].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: The account is currently under a closure period.\nTime Remaining: {0}D {1}H {2}M\nYou can recover the account if you sign in now.\nRecover the account?
   PL: To konto jest w trakcie usuwania.\nPozostały czas: {0} dni {1} godz. {2} min\nZalogowanie się teraz pozwoli je przywrócić.\nPrzywrócić konto?
135. [Interfejs i ustawienia [recover] — tekst] 복구
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=recover].content
   limit: do 120 znaków
   EN: Recover
   PL: Przywróć
136. [Interfejs i ustawienia [request_sucession] — tekst] 탈퇴 신청
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=request_sucession].content
   limit: do 120 znaków
   EN: Request Closure
   PL: Złóż wniosek o usunięcie
137. [Interfejs i ustawienia [request_sucession_success] — tekst] 탈퇴 신청을 성공하셨습니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=request_sucession_success].content
   limit: do 120 znaków
   EN: Closure successfully requested.
   PL: Pomyślnie złożono wniosek o usunięcie konta.
138. [Interfejs i ustawienia [mainui_settings_account] — tekst] 계정
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_account].content
   limit: do 120 znaków
   EN: Account
   PL: Konto
139. [Interfejs i ustawienia [account_secede] — tekst] 계정 탈퇴
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=account_secede].content
   limit: do 120 znaków
   EN: Close Account
   PL: Usuń konto
140. [Interfejs i ustawienia [connected_accounts] — tekst] 연동된 계정
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=connected_accounts].content
   limit: do 120 znaków
   EN: Linked Accounts
   PL: Powiązane konta
141. [Interfejs i ustawienia [mainui_settings_bloom] — tekst] 블룸
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_bloom].content
   limit: do 120 znaków
   EN: Bloom
   PL: Poświata (Bloom)
142. [Interfejs i ustawienia [mainui_settings_blur] — tekst] 블러
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_blur].content
   limit: do 120 znaków
   EN: Blur
   PL: Rozmycie (Blur)
143. [Interfejs i ustawienia [mainui_settings_bloomdesc] — tekst] 빛 번짐 효과를 제어합니다. 성능에 영향을 줍니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_bloomdesc].content
   limit: do 120 znaków
   EN: Controls spread of light effects. Affects game performance.
   PL: Steruje efektem rozproszenia światła. Wpływa na wydajność gry.
144. [Interfejs i ustawienia [mainui_settings_blurdesc] — tekst] 흐려짐 효과를 제어합니다. 성능에 영향을 줍니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_blurdesc].content
   limit: do 120 znaków
   EN: Controls blur effects. Affects game performance.
   PL: Steruje efektem rozmycia obrazu. Wpływa na wydajność gry.
145. [Interfejs i ustawienia [mainui_settings_fps_common] — tekst] 일반 FPS
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_fps_common].content
   limit: do 120 znaków
   EN: Normal FPS
   PL: FPS poza walką
146. [Interfejs i ustawienia [mainui_settings_fps_battle] — tekst] 전투 FPS
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_fps_battle].content
   limit: do 120 znaków
   EN: Combat FPS
   PL: FPS w walce
147. [Interfejs i ustawienia [mainui_settings_renderingscale] — tekst] 렌더링 스케일
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_renderingscale].content
   limit: do 120 znaków
   EN: Render Scaling
   PL: Skala renderowania
148. [Interfejs i ustawienia [mainui_settings_renderingscale_warning] — tekst] PC 환경에서는 「고」, 모바일 환경에서는 「중」 이하의 값을 권장합니다.\n렌더링 스케일 값이 높을수록 전력 소모 증가 및 발열 현상이 유발될 수 있습니다.
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_renderingscale_warning].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We recommend that you set it to 「High」 on PC. On mobile, 「Medium」 or lower is recommended.\nHigher rendering scale value may lead to increased power drainage and heat.
   PL: Na PC zalecamy ustawienie 「Wysoka」, a na urządzeniach mobilnych 「Średnia」 lub niższe.\nWyższa skala renderowania może zwiększać zużycie energii i nagrzewanie urządzenia.
149. [Interfejs i ustawienia [mainui_settings_story_voice_download_title] — tekst] 스토리 보이스
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_story_voice_download_title].content
   limit: do 120 znaków
   EN: Story Voices Management
   PL: Głosy fabularne
150. [Interfejs i ustawienia [mainui_settings_story_voice_download_desc] — tekst] 스토리 보이스 다운로드 및 삭제를 관리합니다
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_story_voice_download_desc].content
   limit: do 120 znaków
   EN: Download or delete story voice files here
   PL: Zarządzaj pobieraniem i usuwaniem nagrań głosowych fabuły
151. [Interfejs i ustawienia [mainui_settings_story_voice_download_button] — tekst] 관리
   źródło: kr_settings-ui-donttranslate.json :: dataList[id=mainui_settings_story_voice_download_button].content
   limit: do 120 znaków
   EN: Manage
   PL: Zarządzaj

## Przedmioty, sklep i profil gracza: UnlockCode-1
- plik gry: `UnlockCode-1.json`

152. [Przedmioty, sklep i profil gracza [101] — warunek odblokowania] 주요 이야기 1장 클리어
   źródło: UnlockCode-1.json :: dataList[id=101].openCondition
   limit: do 120 znaków
   EN: Clear Canto 1
   PL: Ukończ Canto I
153. [Przedmioty, sklep i profil gracza [101] — powiązany rozdział] Canto I
   źródło: UnlockCode-1.json :: dataList[id=101].relatedChapterText
   limit: do 120 znaków
   EN: Canto I
   PL: Canto I
154. [Przedmioty, sklep i profil gracza [102] — warunek odblokowania] 주요 이야기 2장 클리어
   źródło: UnlockCode-1.json :: dataList[id=102].openCondition
   limit: do 120 znaków
   EN: Clear Canto 2
   PL: Ukończ Canto II
155. [Przedmioty, sklep i profil gracza [102] — powiązany rozdział] Canto II
   źródło: UnlockCode-1.json :: dataList[id=102].relatedChapterText
   limit: do 120 znaków
   EN: Canto II
   PL: Canto II
156. [Przedmioty, sklep i profil gracza [103] — warunek odblokowania] 주요 이야기 3장 클리어
   źródło: UnlockCode-1.json :: dataList[id=103].openCondition
   limit: do 120 znaków
   EN: Clear Canto 3
   PL: Ukończ Canto III
157. [Przedmioty, sklep i profil gracza [103] — powiązany rozdział] Canto III
   źródło: UnlockCode-1.json :: dataList[id=103].relatedChapterText
   limit: do 120 znaków
   EN: Canto III
   PL: Canto III
158. [Przedmioty, sklep i profil gracza [104] — warunek odblokowania] 주요 이야기 4장 클리어
   źródło: UnlockCode-1.json :: dataList[id=104].openCondition
   limit: do 120 znaków
   EN: Clear Canto 4
   PL: Ukończ Canto IV
159. [Przedmioty, sklep i profil gracza [104] — powiązany rozdział] Canto IV
   źródło: UnlockCode-1.json :: dataList[id=104].relatedChapterText
   limit: do 120 znaków
   EN: Canto IV
   PL: Canto IV
160. [Przedmioty, sklep i profil gracza [105] — warunek odblokowania] 주요 이야기 5장 클리어
   źródło: UnlockCode-1.json :: dataList[id=105].openCondition
   limit: do 120 znaków
   EN: Clear Canto 5
   PL: Ukończ Canto V
161. [Przedmioty, sklep i profil gracza [105] — komunikat limitu poziomu] 인격의 레벨 상한은 스토리 진행도에 따라 개방되며,\n이 티켓으로 달성할 수 있는 최대 레벨(Lv. {0})은\n주요 이야기 5장을 클리어할 경우 개방됩니다.
   źródło: UnlockCode-1.json :: dataList[id=105].askLevelUp
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Identity level caps are unlocked by progressing through the main story,\nand the highest level achievable with this ticket(Lv. {0})\nwill be unlocked upon clearing Main Story Canto V.
   PL: Limit poziomu Tożsamości rośnie wraz z postępem fabularnym,\na maksymalny poziom osiągalny tym biletem (Poz. {0})\nzostaje odblokowany po ukończeniu Canto V Głównej Opowieści.
162. [Przedmioty, sklep i profil gracza [105] — powiązany rozdział] Canto V
   źródło: UnlockCode-1.json :: dataList[id=105].relatedChapterText
   limit: do 120 znaków
   EN: Canto V
   PL: Canto V
163. [Przedmioty, sklep i profil gracza [106] — warunek odblokowania] 주요 이야기 6장 클리어
   źródło: UnlockCode-1.json :: dataList[id=106].openCondition
   limit: do 120 znaków
   EN: Clear Canto 6
   PL: Ukończ Canto VI
164. [Przedmioty, sklep i profil gracza [106] — komunikat limitu poziomu] 인격의 레벨 상한은 스토리 진행도에 따라 개방되며,\n이 티켓으로 달성할 수 있는 최대 레벨(Lv. {0})은\n주요 이야기 6장을 클리어할 경우 개방됩니다.
   źródło: UnlockCode-1.json :: dataList[id=106].askLevelUp
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Identity level caps are unlocked by progressing through the main story,\nand the highest level achievable with this ticket(Lv. {0})\nwill be unlocked upon clearing Main Story Canto VI.
   PL: Limit poziomu Tożsamości rośnie wraz z postępem fabularnym,\na maksymalny poziom osiągalny tym biletem (Poz. {0})\nzostaje odblokowany po ukończeniu Canto VI Głównej Opowieści.
165. [Przedmioty, sklep i profil gracza [106] — powiązany rozdział] Canto VI
   źródło: UnlockCode-1.json :: dataList[id=106].relatedChapterText
   limit: do 120 znaków
   EN: Canto VI
   PL: Canto VI
166. [Przedmioty, sklep i profil gracza [108] — warunek odblokowania] 주요 이야기 8장 클리어
   źródło: UnlockCode-1.json :: dataList[id=108].openCondition
   limit: do 120 znaków
   EN: Clear Canto 8
   PL: Ukończ Canto VIII
167. [Przedmioty, sklep i profil gracza [108] — komunikat limitu poziomu] 인격의 레벨 상한은 스토리 진행도에 따라 개방되며,\n이 티켓으로 달성할 수 있는 최대 레벨(Lv. {0})은\n주요 이야기 8장을 클리어할 경우 개방됩니다.
   źródło: UnlockCode-1.json :: dataList[id=108].askLevelUp
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Identity level caps are unlocked by progressing through the main story,\nand the highest level achievable with this ticket(Lv. {0})\nwill be unlocked upon clearing Main Story Canto VIII.
   PL: Limit poziomu Tożsamości rośnie wraz z postępem fabularnym,\na maksymalny poziom osiągalny tym biletem (Poz. {0})\nzostaje odblokowany po ukończeniu Canto VIII Głównej Opowieści.
168. [Przedmioty, sklep i profil gracza [108] — wymagany etap] 8-33 클리어
   źródło: UnlockCode-1.json :: dataList[id=108].openConditionNumber
   limit: do 120 znaków
   EN: Clear 8-33
   PL: Ukończ 8-33
169. [Przedmioty, sklep i profil gracza [108] — powiązany rozdział] Canto VIII
   źródło: UnlockCode-1.json :: dataList[id=108].relatedChapterText
   limit: do 120 znaków
   EN: Canto VIII
   PL: Canto VIII
170. [Przedmioty, sklep i profil gracza [9103] — warunek odblokowania] 헬스치킨 클리어
   źródło: UnlockCode-1.json :: dataList[id=9103].openCondition
   limit: do 120 znaków
   EN: Clear Hell's Chicken
   PL: Ukończ Piekielny Kurczak
171. [Przedmioty, sklep i profil gracza [9103] — powiązany rozdział] 헬스치킨
   źródło: UnlockCode-1.json :: dataList[id=9103].relatedChapterText
   limit: do 120 znaków
   EN: Hell's Chicken
   PL: Piekielny Kurczak
172. [Przedmioty, sklep i profil gracza [9104] — warunek odblokowania] 우.미.다 클리어
   źródło: UnlockCode-1.json :: dataList[id=9104].openCondition
   limit: do 120 znaków
   EN: Clear S.E.A.
   PL: Ukończ M.O.R.Z.E.
173. [Przedmioty, sklep i profil gracza [9104] — powiązany rozdział] 우.미.다
   źródło: UnlockCode-1.json :: dataList[id=9104].relatedChapterText
   limit: do 120 znaków
   EN: S.E.A.
   PL: M.O.R.Z.E.
174. [Przedmioty, sklep i profil gracza [9105] — warunek odblokowania] 20번구의 기적 클리어
   źródło: UnlockCode-1.json :: dataList[id=9105].openCondition
   limit: do 120 znaków
   EN: Clear Miracle in District 20
   PL: Ukończ Cud w Dystrykcie 20
175. [Przedmioty, sklep i profil gracza [9105] — powiązany rozdział] 20번구의 기적
   źródło: UnlockCode-1.json :: dataList[id=9105].relatedChapterText
   limit: do 120 znaków
   EN: Miracle in District 20
   PL: Cud w Dystrykcie 20
176. [Przedmioty, sklep i profil gracza [9106] — warunek odblokowania] 제2회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9106].openCondition
   limit: do 120 znaków
   EN: Clear The 2nd Walpurgis Night
   PL: Ukończ 2. Noc Walpurgii
177. [Przedmioty, sklep i profil gracza [9106] — powiązany rozdział] 제2회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9106].relatedChapterText
   limit: do 120 znaków
   EN: The 2nd Walpurgis Night
   PL: 2. Noc Walpurgii
178. [Przedmioty, sklep i profil gracza [9107] — warunek odblokowania] 육참골단 클리어
   źródło: UnlockCode-1.json :: dataList[id=9107].openCondition
   limit: do 120 znaków
   EN: Clear Yield My Flesh to Claim Their Bones
   PL: Ukończ Oddam Ciało, by Złamać Ich Kości
179. [Przedmioty, sklep i profil gracza [9107] — powiązany rozdział] 육참골단
   źródło: UnlockCode-1.json :: dataList[id=9107].relatedChapterText
   limit: do 120 znaków
   EN: Yield My Flesh to Claim Their Bones
   PL: Oddam Ciało, by Złamać Ich Kości
180. [Przedmioty, sklep i profil gracza [9108] — warunek odblokowania] 제3회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9108].openCondition
   limit: do 120 znaków
   EN: Clear The 3rd Walpurgis Night
   PL: Ukończ 3. Noc Walpurgii
181. [Przedmioty, sklep i profil gracza [9108] — powiązany rozdział] 제3회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9108].relatedChapterText
   limit: do 120 znaków
   EN: The 3rd Walpurgis Night
   PL: 3. Noc Walpurgii
182. [Przedmioty, sklep i profil gracza [9109] — warunek odblokowania] 시간살인시간 클리어
   źródło: UnlockCode-1.json :: dataList[id=9109].openCondition
   limit: do 120 znaków
   EN: Clear Timekilling Time
   PL: Ukończ Czas Zabijania Czasu
183. [Przedmioty, sklep i profil gracza [9109] — powiązany rozdział] 시간살인시간
   źródło: UnlockCode-1.json :: dataList[id=9109].relatedChapterText
   limit: do 120 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
184. [Przedmioty, sklep i profil gracza [107] — warunek odblokowania] 주요 이야기 7장 클리어
   źródło: UnlockCode-1.json :: dataList[id=107].openCondition
   limit: do 120 znaków
   EN: Clear Canto 7
   PL: Ukończ Canto VII
185. [Przedmioty, sklep i profil gracza [107] — powiązany rozdział] Canto VII
   źródło: UnlockCode-1.json :: dataList[id=107].relatedChapterText
   limit: do 120 znaków
   EN: Canto VII
   PL: Canto VII
186. [Przedmioty, sklep i profil gracza [9110] — warunek odblokowania] 워프특급 살인사건 클리어
   źródło: UnlockCode-1.json :: dataList[id=9110].openCondition
   limit: do 120 znaków
   EN: Clear Murder on the WARP Express
   PL: Ukończ Morderstwo w Ekspresie WARP
187. [Przedmioty, sklep i profil gracza [9110] — powiązany rozdział] 워프특급 살인사건
   źródło: UnlockCode-1.json :: dataList[id=9110].relatedChapterText
   limit: do 120 znaków
   EN: Murder on the WARP Express
   PL: Morderstwo w Ekspresie WARP
188. [Przedmioty, sklep i profil gracza [9111] — warunek odblokowania] 제4회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9111].openCondition
   limit: do 120 znaków
   EN: Clear The 4th Walpurgis Night
   PL: Ukończ 4. Noc Walpurgii
189. [Przedmioty, sklep i profil gracza [9111] — powiązany rozdział] 제4회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9111].relatedChapterText
   limit: do 120 znaków
   EN: The 4th Walpurgis Night
   PL: 4. Noc Walpurgii
190. [Przedmioty, sklep i profil gracza [9113] — warunek odblokowania] 제5회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9113].openCondition
   limit: do 120 znaków
   EN: Clear The 5th Walpurgis Night
   PL: Ukończ 5. Noc Walpurgii
191. [Przedmioty, sklep i profil gracza [9113] — powiązany rozdział] 제5회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9113].relatedChapterText
   limit: do 120 znaków
   EN: The 5th Walpurgis Night
   PL: 5. Noc Walpurgii
192. [Przedmioty, sklep i profil gracza [9114] — warunek odblokowania] LCB 정기검진 클리어
   źródło: UnlockCode-1.json :: dataList[id=9114].openCondition
   limit: do 120 znaków
   EN: Clear LCB Regular Check-up
   PL: Ukończ Okresowe Badania LCB
193. [Przedmioty, sklep i profil gracza [9114] — powiązany rozdział] LCB 정기검진
   źródło: UnlockCode-1.json :: dataList[id=9114].relatedChapterText
   limit: do 120 znaków
   EN: LCB Regular Check-up
   PL: Okresowe Badania LCB
194. [Przedmioty, sklep i profil gracza [9116] — warunek odblokowania] 심야청소 클리어
   źródło: UnlockCode-1.json :: dataList[id=9116].openCondition
   limit: do 120 znaków
   EN: Clear Nocturnal Sweeping
   PL: Ukończ Nocne Sprzątanie
195. [Przedmioty, sklep i profil gracza [9116] — powiązany rozdział] 심야청소
   źródło: UnlockCode-1.json :: dataList[id=9116].relatedChapterText
   limit: do 120 znaków
   EN: Nocturnal Sweeping
   PL: Nocne Sprzątanie
196. [Przedmioty, sklep i profil gracza [9117] — warunek odblokowania] 제6회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9117].openCondition
   limit: do 120 znaków
   EN: Clear The 6th Walpurgis Night
   PL: Ukończ 6. Noc Walpurgii
197. [Przedmioty, sklep i profil gracza [9117] — powiązany rozdział] 제6회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9117].relatedChapterText
   limit: do 120 znaków
   EN: The 6th Walpurgis Night
   PL: 6. Noc Walpurgii
198. [Przedmioty, sklep i profil gracza [9119] — warunek odblokowania] 절차탁춘 클리어
   źródło: UnlockCode-1.json :: dataList[id=9119].openCondition
   limit: do 120 znaków
   EN: Clear Spring Cultivation
   PL: Ukończ Wiosenny Szlif
199. [Przedmioty, sklep i profil gracza [9119] — powiązany rozdział] 절차탁춘
   źródło: UnlockCode-1.json :: dataList[id=9119].relatedChapterText
   limit: do 120 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
200. [Przedmioty, sklep i profil gracza [109] — warunek odblokowania] 주요 이야기 9장 클리어
   źródło: UnlockCode-1.json :: dataList[id=109].openCondition
   limit: do 120 znaków
   EN: Clear Canto 9
   PL: Ukończ Canto IX
201. [Przedmioty, sklep i profil gracza [109] — powiązany rozdział] Canto IX
   źródło: UnlockCode-1.json :: dataList[id=109].relatedChapterText
   limit: do 120 znaków
   EN: Canto IX
   PL: Canto IX
202. [Przedmioty, sklep i profil gracza [9123] — warunek odblokowania] 제8회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9123].openCondition
   limit: do 120 znaków
   EN: Clear The 8th Walpurgis Night
   PL: Ukończ 8. Noc Walpurgii
203. [Przedmioty, sklep i profil gracza [9123] — powiązany rozdział] 제8회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9123].relatedChapterText
   limit: do 120 znaków
   EN: The 8th Walpurgis Night
   PL: 8. Noc Walpurgii
204. [Przedmioty, sklep i profil gracza [9125] — warunek odblokowania] 타래 엮기 클리어
   źródło: UnlockCode-1.json :: dataList[id=9125].openCondition
   limit: do 120 znaków
   EN: Clear Twining Threads
   PL: Ukończ Splatanie Pasm
205. [Przedmioty, sklep i profil gracza [9125] — wymagany etap] 9.5-14 클리어
   źródło: UnlockCode-1.json :: dataList[id=9125].openConditionNumber
   limit: do 120 znaków
   EN: Clear 9.5-14
   PL: Ukończ 9.5-14
206. [Przedmioty, sklep i profil gracza [9125] — powiązany rozdział] 타래 엮기
   źródło: UnlockCode-1.json :: dataList[id=9125].relatedChapterText
   limit: do 120 znaków
   EN: Twining Threads
   PL: Splatanie Pasm
207. [Przedmioty, sklep i profil gracza [912520] — warunek odblokowania] 사영전투][투전영사 - 타래 엮기 Normal 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912520].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Twining Threads on Normal Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Splatanie Pasm (Normalny)
208. [Przedmioty, sklep i profil gracza [912521] — warunek odblokowania] 사영전투][투전영사 - 타래 엮기 Hard 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912521].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Twining Threads on Hard Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Splatanie Pasm (Trudny)
209. [Przedmioty, sklep i profil gracza [9126] — warunek odblokowania] 심야청소 BokGak 클리어
   źródło: UnlockCode-1.json :: dataList[id=9126].openCondition
   limit: do 120 znaków
   EN: Clear Nocturnal Sweeping BokGak
   PL: Ukończ Nocne Sprzątanie BokGak
210. [Przedmioty, sklep i profil gracza [9126] — wymagany etap] 7.5-26 Hard 클리어
   źródło: UnlockCode-1.json :: dataList[id=9126].openConditionNumber
   limit: do 120 znaków
   EN: Clear 7.5-26 on Hard Difficulty
   PL: Ukończ 7.5-26 (Trudny)
211. [Przedmioty, sklep i profil gracza [9126] — powiązany rozdział] 심야청소 BokGak
   źródło: UnlockCode-1.json :: dataList[id=9126].relatedChapterText
   limit: do 120 znaków
   EN: Nocturnal Sweeping BokGak
   PL: Nocne Sprzątanie BokGak
212. [Przedmioty, sklep i profil gracza [912620] — warunek odblokowania] 사영전투][투전영사 - 심야청소 BokGak Normal 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912620].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Nocturnal Sweeping BokGak on Normal Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Nocne Sprzątanie BokGak (Normalny)
213. [Przedmioty, sklep i profil gracza [912621] — warunek odblokowania] 사영전투][투전영사 - 심야청소 BokGak Hard 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912621].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Nocturnal Sweeping BokGak on Hard Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Nocne Sprzątanie BokGak (Trudny)
214. [Przedmioty, sklep i profil gracza [9127] — warunek odblokowania] 경험기억 클리어
   źródło: UnlockCode-1.json :: dataList[id=9127].openCondition
   limit: do 120 znaków
   EN: Clear Mnestic Experience
   PL: Ukończ Pamięć Doświadczenia
215. [Przedmioty, sklep i profil gracza [9127] — wymagany etap] 9.5-26 클리어
   źródło: UnlockCode-1.json :: dataList[id=9127].openConditionNumber
   limit: do 120 znaków
   EN: Clear 9.5-26
   PL: Ukończ 9.5-26
216. [Przedmioty, sklep i profil gracza [9127] — powiązany rozdział] 경험기억
   źródło: UnlockCode-1.json :: dataList[id=9127].relatedChapterText
   limit: do 120 znaków
   EN: Mnestic Experience
   PL: Pamięć Doświadczenia
217. [Przedmioty, sklep i profil gracza [912720] — warunek odblokowania] 사영전투][투전영사 - 경험기억 Normal 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912720].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Mnestic Experience on Normal Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Pamięć Doświadczenia (Normalny)
218. [Przedmioty, sklep i profil gracza [912721] — warunek odblokowania] 사영전투][투전영사 - 경험기억 Hard 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912721].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Mnestic Experience on Hard Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Pamięć Doświadczenia (Trudny)
219. [Przedmioty, sklep i profil gracza [100001] — warunek odblokowania] 거울굴절철도 1호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100001].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 1
   PL: Ukończ Kolej Załamania — Linia 1
220. [Przedmioty, sklep i profil gracza [100001] — powiązany rozdział] 거울굴절철도 1호선
   źródło: UnlockCode-1.json :: dataList[id=100001].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 1
   PL: Kolej Załamania — Linia 1
221. [Przedmioty, sklep i profil gracza [100002] — warunek odblokowania] 거울굴절철도 2호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100002].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 2
   PL: Ukończ Kolej Załamania — Linia 2
222. [Przedmioty, sklep i profil gracza [100002] — powiązany rozdział] 거울굴절철도 2호선
   źródło: UnlockCode-1.json :: dataList[id=100002].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 2
   PL: Kolej Załamania — Linia 2
223. [Przedmioty, sklep i profil gracza [100003] — warunek odblokowania] 거울굴절철도 3호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100003].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 3
   PL: Ukończ Kolej Załamania — Linia 3
224. [Przedmioty, sklep i profil gracza [100003] — powiązany rozdział] 거울굴절철도 3호선
   źródło: UnlockCode-1.json :: dataList[id=100003].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 3
   PL: Kolej Załamania — Linia 3
225. [Przedmioty, sklep i profil gracza [100004] — warunek odblokowania] 거울굴절철도 4호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100004].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 4
   PL: Ukończ Kolej Załamania — Linia 4
226. [Przedmioty, sklep i profil gracza [100004] — powiązany rozdział] 거울굴절철도 4호선
   źródło: UnlockCode-1.json :: dataList[id=100004].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 4
   PL: Kolej Załamania — Linia 4
227. [Przedmioty, sklep i profil gracza [100005] — warunek odblokowania] 거울굴절철도 5호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100005].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 5
   PL: Ukończ Kolej Załamania — Linia 5
228. [Przedmioty, sklep i profil gracza [100005] — powiązany rozdział] 거울굴절철도 5호선
   źródło: UnlockCode-1.json :: dataList[id=100005].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 5
   PL: Kolej Załamania — Linia 5
229. [Przedmioty, sklep i profil gracza [100006] — warunek odblokowania] 거울굴절철도 6호선 클리어
   źródło: UnlockCode-1.json :: dataList[id=100006].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 6
   PL: Ukończ Kolej Załamania — Linia 6
230. [Przedmioty, sklep i profil gracza [100006] — powiązany rozdział] 거울굴절철도 6호선
   źródło: UnlockCode-1.json :: dataList[id=100006].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 6
   PL: Kolej Załamania — Linia 6
231. [Przedmioty, sklep i profil gracza [101001] — warunek odblokowania] 거울굴절철도 1호선 BokGak 클리어
   źródło: UnlockCode-1.json :: dataList[id=101001].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 1 BokGak
   PL: Ukończ Kolej Załamania — Linia 1 BokGak
232. [Przedmioty, sklep i profil gracza [101001] — powiązany rozdział] 거울굴절철도 1호선 BokGak
   źródło: UnlockCode-1.json :: dataList[id=101001].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 1 BokGak
   PL: Kolej Załamania — Linia 1 BokGak
233. [Przedmioty, sklep i profil gracza [101002] — warunek odblokowania] 거울굴절철도 2호선 BokGak 클리어
   źródło: UnlockCode-1.json :: dataList[id=101002].openCondition
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 2 BokGak
   PL: Ukończ Kolej Załamania — Linia 2 BokGak
234. [Przedmioty, sklep i profil gracza [101002] — powiązany rozdział] 거울굴절철도 2호선 BokGak
   źródło: UnlockCode-1.json :: dataList[id=101002].relatedChapterText
   limit: do 120 znaków
   EN: Refraction Railway Line 2 BokGak
   PL: Kolej Załamania — Linia 2 BokGak
235. [Przedmioty, sklep i profil gracza [912722] — warunek odblokowania] 사영전투][투전영사 - 삽시호 Normal 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912722].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Chachihu on Normal Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Chachihu (Normalny)
236. [Przedmioty, sklep i profil gracza [912723] — warunek odblokowania] 사영전투][투전영사 - 삽시호 Hard 난이도 클리어
   źródło: UnlockCode-1.json :: dataList[id=912723].openCondition
   limit: do 120 znaków
   EN: Clear Reflectrial][lairtcelfeR - Chachihu on Hard Difficulty
   PL: Ukończ Walkę Projekcyjną][ąnjyckejorP ęklaW — Chachihu (Trudny)
237. [Przedmioty, sklep i profil gracza [110] — warunek odblokowania] 주요 이야기 10장 클리어
   źródło: UnlockCode-1.json :: dataList[id=110].openCondition
   limit: do 120 znaków
   EN: Clear Canto 10
   PL: Ukończ Canto X
238. [Przedmioty, sklep i profil gracza [110] — wymagany etap] 10-7 클리어
   źródło: UnlockCode-1.json :: dataList[id=110].openConditionNumber
   limit: do 120 znaków
   EN: Clear 10-7
   PL: Ukończ 10-7
239. [Przedmioty, sklep i profil gracza [110] — powiązany rozdział] Canto X
   źródło: UnlockCode-1.json :: dataList[id=110].relatedChapterText
   limit: do 120 znaków
   EN: Canto X
   PL: Canto X
240. [Przedmioty, sklep i profil gracza [9128] — warunek odblokowania] 주요 이야기 10장 클리어
   źródło: UnlockCode-1.json :: dataList[id=9128].openCondition
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Przedmioty, sklep i profil gracza [9128] — wymagany etap] 10-7 클리어
   źródło: UnlockCode-1.json :: dataList[id=9128].openConditionNumber
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Przedmioty, sklep i profil gracza [9128] — powiązany rozdział] Canto X
   źródło: UnlockCode-1.json :: dataList[id=9128].relatedChapterText
   (powtórzenie elementu 239 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Przedmioty, sklep i profil gracza [9129] — warunek odblokowania] 제10회 발푸르기스의 밤 클리어
   źródło: UnlockCode-1.json :: dataList[id=9129].openCondition
   limit: do 120 znaków
   EN: Clear The 10th Walpurgis Night
   PL: Ukończ 10. Noc Walpurgii
244. [Przedmioty, sklep i profil gracza [9129] — powiązany rozdział] 제10회 발푸르기스의 밤
   źródło: UnlockCode-1.json :: dataList[id=9129].relatedChapterText
   limit: do 120 znaków
   EN: The 10th Walpurgis Night
   PL: 10. Noc Walpurgii

## Przedmioty, sklep i profil gracza: UserInfo_Friends
- plik gry: `UserInfo_Friends.json`

245. [Przedmioty, sklep i profil gracza [GetConditionTitle] — tekst] 획득조건
   źródło: UserInfo_Friends.json :: dataList[id=GetConditionTitle].content
   limit: do 120 znaków
   EN: Requirements
   PL: Warunki zdobycia
246. [Przedmioty, sklep i profil gracza [BannerSelect] — tekst] 장식 배너
   źródło: UserInfo_Friends.json :: dataList[id=BannerSelect].content
   limit: do 120 znaków
   EN: Banner
   PL: Baner ozdobny
247. [Przedmioty, sklep i profil gracza [Personality] — tekst] 인격
   źródło: UserInfo_Friends.json :: dataList[id=Personality].content
   limit: do 120 znaków
   EN: Identities
   PL: Tożsamości
248. [Przedmioty, sklep i profil gracza [CharacterNumber] — tekst] 번호
   źródło: UserInfo_Friends.json :: dataList[id=CharacterNumber].content
   limit: do 120 znaków
   EN: ID
   PL: Nr
249. [Przedmioty, sklep i profil gracza [Rarity] — tekst] 희귀도
   źródło: UserInfo_Friends.json :: dataList[id=Rarity].content
   limit: do 120 znaków
   EN: Rarity
   PL: Rzadkość
250. [Przedmioty, sklep i profil gracza [Season] — tekst] 시즌
   źródło: UserInfo_Friends.json :: dataList[id=Season].content
   limit: do 120 znaków
   EN: Season
   PL: Sezon
251. [Przedmioty, sklep i profil gracza [Group] — tekst] 소속
   źródło: UserInfo_Friends.json :: dataList[id=Group].content
   limit: do 120 znaków
   EN: Faction
   PL: Przynależność
252. [Przedmioty, sklep i profil gracza [Name] — tekst] 이름
   źródło: UserInfo_Friends.json :: dataList[id=Name].content
   limit: do 120 znaków
   EN: Name
   PL: Nazwa
253. [Przedmioty, sklep i profil gracza [LastLoginDay] — tekst] 최근 접속일
   źródło: UserInfo_Friends.json :: dataList[id=LastLoginDay].content
   limit: do 120 znaków
   EN: Last Online:
   PL: Ostatnio online:
254. [Przedmioty, sklep i profil gracza [Manager] — tekst] 관리자
   źródło: UserInfo_Friends.json :: dataList[id=Manager].content
   limit: do 120 znaków
   EN: Manager
   PL: Kierownik
255. [Przedmioty, sklep i profil gracza [Company] — tekst] 회사
   źródło: UserInfo_Friends.json :: dataList[id=Company].content
   limit: do 120 znaków
   EN: Company
   PL: Firma
256. [Przedmioty, sklep i profil gracza [Friends] — tekst] 친구
   źródło: UserInfo_Friends.json :: dataList[id=Friends].content
   limit: do 120 znaków
   EN: Friends
   PL: Znajomi
257. [Przedmioty, sklep i profil gracza [Add_Friends] — tekst] 친구 추가
   źródło: UserInfo_Friends.json :: dataList[id=Add_Friends].content
   limit: do 120 znaków
   EN: Add a Friend
   PL: Dodaj znajomego
258. [Przedmioty, sklep i profil gracza [Delete_Friends] — tekst] 친구 삭제
   źródło: UserInfo_Friends.json :: dataList[id=Delete_Friends].content
   limit: do 120 znaków
   EN: Remove Friend
   PL: Usuń znajomego
259. [Przedmioty, sklep i profil gracza [Waiting_Friends] — tekst] 요청 중
   źródło: UserInfo_Friends.json :: dataList[id=Waiting_Friends].content
   limit: do 120 znaków
   EN: Sent Requests
   PL: Wysłane
260. [Przedmioty, sklep i profil gracza [Accept_Friends] — tekst] 수락 대기
   źródło: UserInfo_Friends.json :: dataList[id=Accept_Friends].content
   limit: do 120 znaków
   EN: Inbox
   PL: Oczekujące
261. [Przedmioty, sklep i profil gracza [Last_Reload] — tekst] {0}초 전
   źródło: UserInfo_Friends.json :: dataList[id=Last_Reload].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}s ago!
   PL: {0} sek. temu
262. [Przedmioty, sklep i profil gracza [WaitCancle] — tekst] 요청 취소
   źródło: UserInfo_Friends.json :: dataList[id=WaitCancle].content
   limit: do 120 znaków
   EN: Cancel
   PL: Anuluj
263. [Przedmioty, sklep i profil gracza [Refuse] — tekst] 거절
   źródło: UserInfo_Friends.json :: dataList[id=Refuse].content
   limit: do 120 znaków
   EN: Decline
   PL: Odrzuć
264. [Przedmioty, sklep i profil gracza [Accept] — tekst] 수락
   źródło: UserInfo_Friends.json :: dataList[id=Accept].content
   limit: do 120 znaków
   EN: Accept
   PL: Akceptuj
265. [Przedmioty, sklep i profil gracza [Send_Add_Friends] — tekst] 친구 추가하시겠습니까?
   źródło: UserInfo_Friends.json :: dataList[id=Send_Add_Friends].content
   limit: do 120 znaków
   EN: Send them a friend request?
   PL: Wysłać zaproszenie do znajomych?
266. [Przedmioty, sklep i profil gracza [Delete_Friends_Apply] — tekst] 친구 목록에서 삭제하시겠습니까?
   źródło: UserInfo_Friends.json :: dataList[id=Delete_Friends_Apply].content
   limit: do 120 znaków
   EN: Are you sure you want to remove this user from your friend list?
   PL: Czy na pewno chcesz usunąć tego gracza z listy znajomych?
267. [Przedmioty, sklep i profil gracza [SendSendFriend_1] — tekst] 요청가능 상한이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_1].content
   limit: do 120 znaków
   EN: You have too many requests.
   PL: Osiągnięto limit wysłanych zaproszeń.
268. [Przedmioty, sklep i profil gracza [SendSendFriend_2] — tekst] 친구 상한이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_2].content
   limit: do 120 znaków
   EN: Your friend list is full.
   PL: Twoja lista znajomych jest pełna.
269. [Przedmioty, sklep i profil gracza [SendSendFriend_3] — tekst] 상대방의 수락대기열이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_3].content
   limit: do 120 znaków
   EN: This user currently has too many requests.
   PL: Lista oczekujących zaproszeń tego gracza jest pełna.
270. [Przedmioty, sklep i profil gracza [SendSendFriend_4] — tekst] 상대방의 친구 상한이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_4].content
   limit: do 120 znaków
   EN: This user’s friend list is full.
   PL: Lista znajomych tego gracza jest pełna.
271. [Przedmioty, sklep i profil gracza [SendSendFriend_5] — tekst] 유효하지 않은 유저입니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_5].content
   limit: do 120 znaków
   EN: Invalid user.
   PL: Nieprawidłowy użytkownik.
272. [Przedmioty, sklep i profil gracza [SendSendFriend_6] — tekst] 이미 요청목록에 있는 유저입니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_6].content
   limit: do 120 znaków
   EN: The user is already on the request list.
   PL: Ten gracz znajduje się już na liście zaproszeń.
273. [Przedmioty, sklep i profil gracza [SendSendFriend_7] — tekst] 예기치 못한 오류가 발생했습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendSendFriend_7].content
   limit: do 120 znaków
   EN: An unexpected error has occurred.
   PL: Wystąpił nieoczekiwany błąd.
274. [Przedmioty, sklep i profil gracza [SendAcceptReceivedFriend_1] — tekst] 친구 상한이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendAcceptReceivedFriend_1].content
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Przedmioty, sklep i profil gracza [SendAcceptReceivedFriend_2] — tekst] 상대방의 친구 상한이 가득찼습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendAcceptReceivedFriend_2].content
   limit: do 120 znaków
   EN: This user’s friend list became full.
   PL: Lista znajomych tego gracza zdążyła się zapełnić.
276. [Przedmioty, sklep i profil gracza [SendAcceptReceivedFriend_3] — tekst] 상대방이 친구요청을 취소했습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendAcceptReceivedFriend_3].content
   limit: do 120 znaków
   EN: The user canceled their request.
   PL: Gracz anulował zaproszenie do znajomych.
277. [Przedmioty, sklep i profil gracza [SendAcceptReceivedFriend_4] — tekst] 예기치 못한 오류가 발생했습니다.
   źródło: UserInfo_Friends.json :: dataList[id=SendAcceptReceivedFriend_4].content
   (powtórzenie elementu 273 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Przedmioty, sklep i profil gracza [Today] — tekst] 오늘
   źródło: UserInfo_Friends.json :: dataList[id=Today].content
   limit: do 120 znaków
   EN: Today!
   PL: Dzisiaj
279. [Przedmioty, sklep i profil gracza [Ago] — tekst] {0}일 전
   źródło: UserInfo_Friends.json :: dataList[id=Ago].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}d ago
   PL: {0} dni temu
280. [Przedmioty, sklep i profil gracza [Day_Ago] — tekst] MM월 dd일
   źródło: UserInfo_Friends.json :: dataList[id=Day_Ago].content
   limit: do 120 znaków
   EN: MM/dd
   PL: dd.MM
281. [Przedmioty, sklep i profil gracza [Change_Introduce] — tekst] 인사말 변경
   źródło: UserInfo_Friends.json :: dataList[id=Change_Introduce].content
   limit: do 120 znaków
   EN: Edit Intro Tagline
   PL: Zmień wizytówkę
282. [Przedmioty, sklep i profil gracza [Sorting_Level] — tekst] 계정 레벨
   źródło: UserInfo_Friends.json :: dataList[id=Sorting_Level].content
   limit: do 120 znaków
   EN: Level
   PL: Poziom konta
283. [Przedmioty, sklep i profil gracza [Sorting_LastLogin] — tekst] 최근 접속일
   źródło: UserInfo_Friends.json :: dataList[id=Sorting_LastLogin].content
   limit: do 120 znaków
   EN: Last Online
   PL: Ostatnio online
284. [Przedmioty, sklep i profil gracza [Season_0] — tekst] 통상
   źródło: UserInfo_Friends.json :: dataList[id=Season_0].content
   limit: do 120 znaków
   EN: Regular
   PL: Standardowe
285. [Przedmioty, sklep i profil gracza [Season_1] — tekst] 시즌 1
   źródło: UserInfo_Friends.json :: dataList[id=Season_1].content
   limit: do 120 znaków
   EN: Season 1
   PL: Sezon 1
286. [Przedmioty, sklep i profil gracza [Season_2] — tekst] 시즌 2
   źródło: UserInfo_Friends.json :: dataList[id=Season_2].content
   limit: do 120 znaków
   EN: Season 2
   PL: Sezon 2
287. [Przedmioty, sklep i profil gracza [Change] — tekst] 변경
   źródło: UserInfo_Friends.json :: dataList[id=Change].content
   limit: do 120 znaków
   EN: Change
   PL: Zmień
288. [Przedmioty, sklep i profil gracza [Uninstall] — tekst] 해제
   źródło: UserInfo_Friends.json :: dataList[id=Uninstall].content
   limit: do 120 znaków
   EN: Unequip
   PL: Zdejmij
289. [Przedmioty, sklep i profil gracza [All] — tekst] 전체
   źródło: UserInfo_Friends.json :: dataList[id=All].content
   limit: do 120 znaków
   EN: All
   PL: Wszystko
290. [Przedmioty, sklep i profil gracza [Reset_Company_Title] — tekst] 설정 초기화
   źródło: UserInfo_Friends.json :: dataList[id=Reset_Company_Title].content
   limit: do 120 znaków
   EN: Reset Settings
   PL: Resetuj ustawienia
291. [Przedmioty, sklep i profil gracza [Reset_Company_desc] — tekst] 회사 설정을 초기화하시겠습니까?
   źródło: UserInfo_Friends.json :: dataList[id=Reset_Company_desc].content
   limit: do 120 znaków
   EN: Are you sure you want to reset your company settings?
   PL: Czy na pewno chcesz zresetować ustawienia profilu firmy?
292. [Przedmioty, sklep i profil gracza [NO_Friends] — tekst] 아직 이곳에는 아무도 없습니다.
   źródło: UserInfo_Friends.json :: dataList[id=NO_Friends].content
   limit: do 120 znaków
   EN: Nothing to display here yet.
   PL: Nikogo tu jeszcze nie ma.
293. [Przedmioty, sklep i profil gracza [NO_SendFriends] — tekst] 요청한 내용이 없습니다.
   źródło: UserInfo_Friends.json :: dataList[id=NO_SendFriends].content
   limit: do 120 znaków
   EN: No requests made.
   PL: Brak wysłanych zaproszeń.
294. [Przedmioty, sklep i profil gracza [NO_AcceptFriends] — tekst] 요청 받은 내용이 없습니다.
   źródło: UserInfo_Friends.json :: dataList[id=NO_AcceptFriends].content
   limit: do 120 znaków
   EN: No requests received.
   PL: Brak otrzymanych zaproszeń.
295. [Przedmioty, sklep i profil gracza [SupportPersonality_Reset] — tekst] 초기화
   źródło: UserInfo_Friends.json :: dataList[id=SupportPersonality_Reset].content
   limit: do 120 znaków
   EN: Reset
   PL: Resetuj
296. [Przedmioty, sklep i profil gracza [SearchFriends] — tekst] 친구 찾기
   źródło: UserInfo_Friends.json :: dataList[id=SearchFriends].content
   limit: do 120 znaków
   EN: Discover w/ ID
   PL: Szukaj po ID
297. [Przedmioty, sklep i profil gracza [ReLoad] — tekst] 새로고침
   źródło: UserInfo_Friends.json :: dataList[id=ReLoad].content
   limit: do 120 znaków
   EN: Refresh
   PL: Odśwież
298. [Przedmioty, sklep i profil gracza [Btn_Search] — tekst] 찾기
   źródło: UserInfo_Friends.json :: dataList[id=Btn_Search].content
   limit: do 120 znaków
   EN: Search
   PL: Szukaj
299. [Przedmioty, sklep i profil gracza [Sentence] — tekst] 문장
   źródło: UserInfo_Friends.json :: dataList[id=Sentence].content
   limit: do 120 znaków
   EN: Phrase
   PL: Fraza
300. [Przedmioty, sklep i profil gracza [Word] — tekst] 단어
   źródło: UserInfo_Friends.json :: dataList[id=Word].content
   limit: do 120 znaków
   EN: Word
   PL: Słowo
301. [Przedmioty, sklep i profil gracza [Uid_Copy] — tekst] 복사
   źródło: UserInfo_Friends.json :: dataList[id=Uid_Copy].content
   limit: do 120 znaków
   EN: Copy
   PL: Kopiuj
302. [Przedmioty, sklep i profil gracza [Uid_Copy_ModalTitle] — tekst] 복사 완료
   źródło: UserInfo_Friends.json :: dataList[id=Uid_Copy_ModalTitle].content
   limit: do 120 znaków
   EN: Copy Success
   PL: Skopiowano
303. [Przedmioty, sklep i profil gracza [Uid_Copy_ModalDesc] — tekst] 아이디가 복사되었습니다.
   źródło: UserInfo_Friends.json :: dataList[id=Uid_Copy_ModalDesc].content
   limit: do 120 znaków
   EN: The ID has been copied.
   PL: Identyfikator został skopiowany.
304. [Przedmioty, sklep i profil gracza [TicketCustom_Button] — tekst] 티켓 꾸미기
   źródło: UserInfo_Friends.json :: dataList[id=TicketCustom_Button].content
   limit: do 120 znaków
   EN: Customize
   PL: Personalizuj
305. [Przedmioty, sklep i profil gracza [TicketCustom_Popup_L] — tekst] 테두리 1
   źródło: UserInfo_Friends.json :: dataList[id=TicketCustom_Popup_L].content
   limit: do 120 znaków
   EN: Border 1
   PL: Ramka 1
306. [Przedmioty, sklep i profil gracza [TicketCustom_Popup_R] — tekst] 테두리 2
   źródło: UserInfo_Friends.json :: dataList[id=TicketCustom_Popup_R].content
   limit: do 120 znaków
   EN: Border 2
   PL: Ramka 2
307. [Przedmioty, sklep i profil gracza [TicketCustom_Popup_EGOBG] — tekst] 배경
   źródło: UserInfo_Friends.json :: dataList[id=TicketCustom_Popup_EGOBG].content
   limit: do 120 znaków
   EN: Bg
   PL: Tło
308. [Przedmioty, sklep i profil gracza [Using] — tekst] 사용중
   źródło: UserInfo_Friends.json :: dataList[id=Using].content
   limit: do 120 znaków
   EN: In Use
   PL: W użyciu
309. [Przedmioty, sklep i profil gracza [IntroduceSort_Default] — tekst] 기본
   źródło: UserInfo_Friends.json :: dataList[id=IntroduceSort_Default].content
   limit: do 120 znaków
   EN: Default
   PL: Domyślnie
310. [Przedmioty, sklep i profil gracza [IntroduceSort_ABC] — tekst] 가나다 순
   źródło: UserInfo_Friends.json :: dataList[id=IntroduceSort_ABC].content
   limit: do 120 znaków
   EN: Alphabetical
   PL: Alfabetycznie
311. [Przedmioty, sklep i profil gracza [IntroduceSort_Acquisition] — tekst] 획득 순
   źródło: UserInfo_Friends.json :: dataList[id=IntroduceSort_Acquisition].content
   limit: do 120 znaków
   EN: Claim Date
   PL: Wg zdobycia
312. [Przedmioty, sklep i profil gracza [SimilarBanner] — tekst] 배너 목록
   źródło: UserInfo_Friends.json :: dataList[id=SimilarBanner].content
   limit: do 120 znaków
   EN: Banner List
   PL: Lista banerów
313. [Przedmioty, sklep i profil gracza [SimilarTicket] — tekst] 티켓 목록
   źródło: UserInfo_Friends.json :: dataList[id=SimilarTicket].content
   limit: do 120 znaków
   EN: Ticket List
   PL: Lista biletów
314. [Przedmioty, sklep i profil gracza [Choosing] — tekst] 선택 중
   źródło: UserInfo_Friends.json :: dataList[id=Choosing].content
   limit: do 120 znaków
   EN: Selecting
   PL: Wybieranie
315. [Przedmioty, sklep i profil gracza [IntroduceSort_Release] — tekst] 출시 순
   źródło: UserInfo_Friends.json :: dataList[id=IntroduceSort_Release].content
   limit: do 120 znaków
   EN: Release Date
   PL: Wg premiery
