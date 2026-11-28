# Paczka AI P03 (Fala 1 · 1B) — Interfejs główny, ustawienia, okna dialogowe i formacja (część 1/2)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P03_1b_interfejs_i_ustawienia_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P03_1b_interfejs_i_ustawienia_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Interfejs i ustawienia: Filter
- plik gry: `Filter.json`

1. [Interfejs i ustawienia [filter_title_ego_type] — tekst] 희귀도
   źródło: Filter.json :: dataList[id=filter_title_ego_type].content
   limit: do 120 znaków
   EN: Rarity
   PL: Rzadkość
2. [Interfejs i ustawienia [filter_title_ego_level] — tekst] 강화 단계
   źródło: Filter.json :: dataList[id=filter_title_ego_level].content
   limit: do 120 znaków
   EN: Level
   PL: Poziom
3. [Interfejs i ustawienia [number_of_targets] — tekst] 대상 수
   źródło: Filter.json :: dataList[id=number_of_targets].content
   limit: do 120 znaków
   EN: Targets
   PL: Liczba celów
4. [Interfejs i ustawienia [SINGLE_TARGET] — tekst] 단일
   źródło: Filter.json :: dataList[id=SINGLE_TARGET].content
   limit: do 120 znaków
   EN: Single
   PL: Pojedynczy
5. [Interfejs i ustawienia [MULTIPLE_TARGET] — tekst] 광역
   źródło: Filter.json :: dataList[id=MULTIPLE_TARGET].content
   limit: do 120 znaków
   EN: Area
   PL: Obszarowy
6. [Interfejs i ustawienia [filter_title_attribute] — tekst] 속성
   źródło: Filter.json :: dataList[id=filter_title_attribute].content
   limit: do 120 znaków
   EN: Affinity
   PL: Grzech
7. [Interfejs i ustawienia [filter_awaken_state] — tekst] 동기화 단계
   źródło: Filter.json :: dataList[id=filter_awaken_state].content
   limit: do 120 znaków
   EN: Uptie Tier
   PL: Synchronizacja
8. [Interfejs i ustawienia [filter_normal] — tekst] 1,2단계
   źródło: Filter.json :: dataList[id=filter_normal].content
   limit: do 120 znaków
   EN: Tier 1/2
   PL: Poz. 1/2
9. [Interfejs i ustawienia [filter_awaken] — tekst] 3단계
   źródło: Filter.json :: dataList[id=filter_awaken].content
   limit: do 120 znaków
   EN: Tier 3
   PL: Poz. 3
10. [Interfejs i ustawienia [filter_skill_keyword] — tekst] 스킬 키워드
   źródło: Filter.json :: dataList[id=filter_skill_keyword].content
   limit: do 120 znaków
   EN: Keyword
   PL: Słowo kluczowe
11. [Interfejs i ustawienia [sorting_acqisition] — tekst] 획득 순
   źródło: Filter.json :: dataList[id=sorting_acqisition].content
   limit: do 120 znaków
   EN: Recent
   PL: Najnowsze
12. [Interfejs i ustawienia [filter_title_ego_gacksung] — tekst] 환상 해석 단계
   źródło: Filter.json :: dataList[id=filter_title_ego_gacksung].content
   limit: do 120 znaków
   EN: Threadspun Tier
   PL: Splot Nici

## Interfejs i ustawienia: LoginUIText
- plik gry: `LoginUIText.json`

13. [Interfejs i ustawienia [loginui_sign_in_with_google] — tekst] Google 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_google].content
   limit: do 120 znaków
   EN: Sign in with Google
   PL: Zaloguj przez Google
14. [Interfejs i ustawienia [loginui_sign_in_with_apple] — tekst] Apple 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_apple].content
   limit: do 120 znaków
   EN: Sign in with Apple
   PL: Zaloguj przez Apple
15. [Interfejs i ustawienia [loginui_sign_in_with_steam] — tekst] Steam 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_steam].content
   limit: do 120 znaków
   EN: Sign in with Steam
   PL: Zaloguj przez Steam
16. [Interfejs i ustawienia [loginui_sign_in_with_guest] — tekst] 게스트 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_guest].content
   limit: do 120 znaków
   EN: Sign in as a guest
   PL: Zaloguj jako gość
17. [Interfejs i ustawienia [loginui_sign_out_current_account] — tekst] 현재 계정 로그아웃
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_current_account].content
   limit: do 120 znaków
   EN: Sign Out
   PL: Wyloguj obecne konto
18. [Interfejs i ustawienia [loginui_sign_out_current_account_desc] — tekst] 현재 계정을 로그아웃 하시겠습니까?\n게스트 계정일 경우에는 데이터가 유실될 수 있습니다
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_current_account_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sign out from the current account?\nIf you’re playing as a guest, your data may be lost.
   PL: Czy chcesz wylogować obecne konto?\nW przypadku konta gościa dane mogą zostać utracone.
19. [Interfejs i ustawienia [loginui_sign_out_switch_account_desc] — tekst] 현재 계정을 로그아웃하고\n선택한 계정으로 변경하시겠습니까?\n게스트 계정일 경우에는 데이터가 유실될 수 있습니다
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_switch_account_desc].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sign out from the current account\nand switch to the selected one?\nIf you’re playing as a guest, your data may be lost.
   PL: Czy chcesz wylogować obecne konto\ni przełączyć na wybrane?\nW przypadku konta gościa dane mogą zostać utracone.
20. [Interfejs i ustawienia [switch_account] — tekst] 계정 변경
   źródło: LoginUIText.json :: dataList[id=switch_account].content
   limit: do 120 znaków
   EN: Change Account
   PL: Zmień konto
21. [Interfejs i ustawienia [user_agreements] — tekst] 이용 약관
   źródło: LoginUIText.json :: dataList[id=user_agreements].content
   limit: do 120 znaków
   EN: Terms of Service
   PL: Warunki korzystania
22. [Interfejs i ustawienia [title_game_data_download] — tekst] 게임 데이터 다운로드
   źródło: LoginUIText.json :: dataList[id=title_game_data_download].content
   limit: do 120 znaków
   EN: Download Game Data
   PL: Pobieranie danych gry
23. [Interfejs i ustawienia [content_game_data_download] — tekst] {0} 의 데이터를 다운로드합니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Downloading {0} of data.
   PL: Pobieranie {0} danych.
24. [Interfejs i ustawienia [content_game_data_download_description] — tekst] 저장 공간이 부족한 경우에는 타이틀 화면으로 돌아갑니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download_description].content
   limit: do 120 znaków
   EN: You will be returned to the title screen if your device has insufficient storage space.
   PL: W przypadku braku miejsca na urządzeniu nastąpi powrót do ekranu tytułowego.
25. [Interfejs i ustawienia [content_game_data_download_recommend] — tekst] Wi-Fi 환경에서 다운로드하는 걸 권장합니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download_recommend].content
   limit: do 120 znaków
   EN: A direct Internet connection (Wi-Fi) is recommended.
   PL: Zalecane jest pobieranie przez sieć Wi-Fi.
26. [Interfejs i ustawienia [switch_allcacheclear] — tekst] 모든 캐시 삭제
   źródło: LoginUIText.json :: dataList[id=switch_allcacheclear].content
   limit: do 120 znaków
   EN: Clear all caches
   PL: Wyczyść całą pamięć podręczną
27. [Interfejs i ustawienia [switch_oldcacheclear] — tekst] 이전 캐시 삭제
   źródło: LoginUIText.json :: dataList[id=switch_oldcacheclear].content
   limit: do 120 znaków
   EN: Clear old caches
   PL: Wyczyść starą pamięć podręczną
28. [Interfejs i ustawienia [networkingerror_content] — tekst] 네트워크가 불안정합니다.\n 네트워크 상태를 확인해 주세요
   źródło: LoginUIText.json :: dataList[id=networkingerror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The network is unstable.\nPlease check your Internet connection.
   PL: Połączenie sieciowe jest niestabilne.\nSprawdź połączenie z internetem.
29. [Interfejs i ustawienia [networkingerror_close] — tekst] 닫기
   źródło: LoginUIText.json :: dataList[id=networkingerror_close].content
   limit: do 120 znaków
   EN: Close
   PL: Zamknij
30. [Interfejs i ustawienia [networkingerror_retry] — tekst] 재시도
   źródło: LoginUIText.json :: dataList[id=networkingerror_retry].content
   limit: do 120 znaków
   EN: Retry
   PL: Ponów
31. [Interfejs i ustawienia [loginui_ok] — tekst] 확인
   źródło: LoginUIText.json :: dataList[id=loginui_ok].content
   limit: do 120 znaków
   EN: Confirm
   PL: Potwierdź
32. [Interfejs i ustawienia [login_cancel] — tekst] 취소
   źródło: LoginUIText.json :: dataList[id=login_cancel].content
   limit: do 120 znaków
   EN: Cancel
   PL: Anuluj
33. [Interfejs i ustawienia [loginui_loading_battlehint] — tekst] 전투 팁
   źródło: LoginUIText.json :: dataList[id=loginui_loading_battlehint].content
   limit: do 120 znaków
   EN: Combat Tips
   PL: Wskazówki Bojowe
34. [Interfejs i ustawienia [servererror_content] — tekst] 서버 에러가 발생하였습니다.\n잠시 후에 다시 시도해 주세요.
   źródło: LoginUIText.json :: dataList[id=servererror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A server error has occurred.\nPlease try again in a moment.
   PL: Wystąpił błąd serwera.\nSpróbuj ponownie za chwilę.
35. [Interfejs i ustawienia [serverstate_server_busy] — tekst] 서버가 혼잡합니다.\n잠시 후에 다시 시도해 주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_server_busy].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The server is currently busy.\nPlease try again in a moment.
   PL: Serwer jest obecnie przeciążony.\nSpróbuj ponownie za chwilę.
36. [Interfejs i ustawienia [forcequit_content] — tekst] 게임을 진행할 수 없습니다.\n게임이 종료됩니다.
   źródło: LoginUIText.json :: dataList[id=forcequit_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot operate the game.\nShutting down now.
   PL: Nie można kontynuować działania gry.\nGra zostanie zamknięta.
37. [Interfejs i ustawienia [serverstate_openpreparation] — tekst] 오픈 준비 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_openpreparation].content
   limit: do 120 znaków
   EN: Things are still being prepared!
   PL: Trwają przygotowania do otwarcia!
38. [Interfejs i ustawienia [serverstate_regularcheck] — tekst] 서버 정기 점검이 진행 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_regularcheck].content
   limit: do 120 znaków
   EN: The server is currently under routine maintenance.
   PL: Trwa planowa przerwa techniczna serwera.
39. [Interfejs i ustawienia [serverstate_temporary_check] — tekst] 서버 임시 점검이 진행 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_temporary_check].content
   limit: do 120 znaków
   EN: The server is currently under temporary maintenance.
   PL: Trwa tymczasowa przerwa techniczna serwera.
40. [Interfejs i ustawienia [serverstate_verify_invaliduser] — tekst] 존재하지 않거나 탈퇴 처리가 완료된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invaliduser].content
   limit: do 120 znaków
   EN: The account does not exist or has been closed.
   PL: Konto nie istnieje lub zostało usunięte.
41. [Interfejs i ustawienia [serverstate_verify_ban] — tekst] 게임 이용이 제한된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban].content
   limit: do 120 znaków
   EN: The account is restricted from playing.
   PL: Dostęp tego konta do gry został ograniczony.
42. [Interfejs i ustawienia [serverstate_verify_invalidauth] — tekst] 오류가 발생하였습니다.\n다시 로그인을 진행해주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invalidauth].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An error has occurred.\nPlease sign in again.
   PL: Wystąpił błąd.\nZaloguj się ponownie.
43. [Interfejs i ustawienia [guestlogin_failed_try_newguest] — tekst] 게스트 계정이 존재하지 않거나,\n이미 연동된 계정이기 때문에 게스트 로그인에 실패하였습니다.\n\n새로운 게스트 계정을 만드시겠습니까?
   źródło: LoginUIText.json :: dataList[id=guestlogin_failed_try_newguest].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed Guest Login.\nThe account is either already linked, or the Guest account doesn't exist.\n\nWould you like to make a new Guest account?
   PL: Logowanie gościa nie powiodło się.\nKonto gościa nie istnieje lub jest już powiązane.\n\nCzy chcesz utworzyć nowe konto gościa?
44. [Interfejs i ustawienia [secession_remain_days] — tekst] 해당 계정은 탈퇴 처리 중 입니다.\n남은 시간 : {0}일 {1}시간 {2}분\n\n로그인 시, 계정이 복구됩니다.\n계정 복구를 진행하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=secession_remain_days].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: The account is currently under a closure period.\nTime Remaining: {0}D {1}H {2}M\n\nYou can recover the account if you sign in now.\nRecover the account?
   PL: To konto jest w trakcie usuwania.\nPozostały czas: {0} dni {1} godz. {2} min\n\nZalogowanie się teraz przywróci konto.\nCzy chcesz przywrócić konto?
45. [Interfejs i ustawienia [secession_canceled] — tekst] 계정 복구가 정상적으로 완료되었습니다.
   źródło: LoginUIText.json :: dataList[id=secession_canceled].content
   limit: do 120 znaków
   EN: Account recovered successfully.
   PL: Pomyślnie przywrócono konto.
46. [Interfejs i ustawienia [serverstate_verify_invalidclientversion] — tekst] 게임 클라이언트가 최신 버전이 아닙니다.\n업데이트를 진행해주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invalidclientversion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Game client is not up to date.\nPlease update to the latest version.
   PL: Klient gry jest nieaktualny.\nZaktualizuj grę do najnowszej wersji.
47. [Interfejs i ustawienia [create_guest] — tekst] 게스트 생성
   źródło: LoginUIText.json :: dataList[id=create_guest].content
   limit: do 120 znaków
   EN: Create Guest Account
   PL: Utwórz konto gościa
48. [Interfejs i ustawienia [ask_to_remove_all_cache] — tekst] 모든 캐시를 삭제하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=ask_to_remove_all_cache].content
   limit: do 120 znaków
   EN: Clear all caches?
   PL: Wyczyścić całą pamięć podręczną?
49. [Interfejs i ustawienia [networkingerror_update] — tekst] 스토어로 이동
   źródło: LoginUIText.json :: dataList[id=networkingerror_update].content
   limit: do 120 znaków
   EN: Go to Store
   PL: Przejdź do sklepu
50. [Interfejs i ustawienia [speed_hack_warning] — tekst] 비인가 프로그램 사용이 확인되었습니다.
   źródło: LoginUIText.json :: dataList[id=speed_hack_warning].content
   limit: do 120 znaków
   EN: Usage of unauthorized third party program has been detected.
   PL: Wykryto użycie nieautoryzowanego oprogramowania.
51. [Interfejs i ustawienia [serverstate_verify_ban_startdate] — tekst] 일자
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_startdate].content
   limit: do 120 znaków
   EN: Date
   PL: Data
52. [Interfejs i ustawienia [serverstate_verify_ban_reason] — tekst] 내용
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason].content
   limit: do 120 znaków
   EN: Description
   PL: Opis
53. [Interfejs i ustawienia [serverstate_verify_ban_reason_refund] — tekst] 오픈 마켓 환불 시스템 어뷰징
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason_refund].content
   limit: do 120 znaków
   EN: Abuse of Open Market refund system
   PL: Nadużycie systemu zwrotów sklepu
54. [Interfejs i ustawienia [serverstate_verify_ban_reason_cheat] — tekst] 비정상적인 게임 이용 기록
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason_cheat].content
   limit: do 120 znaków
   EN: Abnormal game activity records
   PL: Nieprawidłowa aktywność w grze
55. [Interfejs i ustawienia [serverstate_blocking_endpoint] — tekst] 현재 점검 중인 기능입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_blocking_endpoint].content
   limit: do 120 znaków
   EN: This function is currently under maintenance.
   PL: Ta funkcja jest obecnie objęta przerwą techniczną.
56. [Interfejs i ustawienia [serverstate_verify_invaliduuid] — tekst] 이미 처리된 요청입니다.\n동기화를 위해 게임을 다시 실행해 주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invaliduuid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This request has already been processed.\nPlease restart the game to synchronize.
   PL: To żądanie zostało już przetworzone.\nUruchom grę ponownie w celu synchronizacji.
57. [Interfejs i ustawienia [login_scene_mini_story_warning_spoiler_format] — tekst] 주요 이야기 {0}장 이후의 내용을 담고 있습니다. 스토리를 감상하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_warning_spoiler_format].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This story takes place after the Main Story Chapter {0}. Would you like to view the story anyway?
   PL: Ta historia rozgrywa się po Rozdziale {0} Głównej Opowieści. Czy mimo to chcesz ją obejrzeć?
58. [Interfejs i ustawienia [login_scene_mini_story_unlock_code_105] — tekst] 5
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_unlock_code_105].content
   limit: do 120 znaków
   EN: 5
   PL: 5
59. [Interfejs i ustawienia [login_scene_mini_story_unlock_code_9105] — tekst] 5.5
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_unlock_code_9105].content
   limit: do 120 znaków
   EN: 5.5
   PL: 5.5
60. [Interfejs i ustawienia [switch_clearcatalog] — tekst] 카탈로그 삭제
   źródło: LoginUIText.json :: dataList[id=switch_clearcatalog].content
   limit: do 120 znaków
   EN: Delete Catalogue
   PL: Usuń katalog
61. [Interfejs i ustawienia [panel_clearcatalog] — tekst] 카탈로그를 삭제하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=panel_clearcatalog].content
   limit: do 120 znaków
   EN: Delete catalogue?
   PL: Czy usunąć katalog?
62. [Interfejs i ustawienia [serverstate_error_thirdparty_api] — tekst] 외부 서버와의 통신에 문제가 발생하였습니다. 잠시 후에 다시 시도해 주십시오.
   źródło: LoginUIText.json :: dataList[id=serverstate_error_thirdparty_api].content
   limit: do 120 znaków
   EN: External server connection error. Please try again at a later time.
   PL: Błąd połączenia z serwerem zewnętrznym. Spróbuj ponownie później.
63. [Interfejs i ustawienia [servererror_invalid_purchasing_package] — tekst] 상품거래에 실패하였습니다.
   źródło: LoginUIText.json :: dataList[id=servererror_invalid_purchasing_package].content
   limit: do 120 znaków
   EN: Transaction failed.
   PL: Transakcja nie powiodła się.
64. [Interfejs i ustawienia [forcequit_cache_initialize_fail] — tekst] 게임 클라이언트가 정상적으로 기동하지 못하였습니다.\n네트워크 연결 상태를 확인하시고 다시 시도해 주세요.\n문의: limbussupport+bug@projmoon.com
   źródło: LoginUIText.json :: dataList[id=forcequit_cache_initialize_fail].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Game Client failed to launch properly.\nPlease confirm your network status and try again.\nInquiries: limbussupport+bug@projmoon.com
   PL: Nie udało się poprawnie uruchomić klienta gry.\nSprawdź stan połączenia sieciowego i spróbuj ponownie.\nKontakt: limbussupport+bug@projmoon.com
65. [Interfejs i ustawienia [push_notification_message_full_stamina_default_title] — tekst] 림버스 컴퍼니
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_default_title].content
   limit: do 120 znaków
   EN: Limbus Company
   PL: Limbus Company
66. [Interfejs i ustawienia [push_notification_message_full_stamina_default_text] — tekst] 엔케팔린 충전이 완료되었습니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_default_text].content
   limit: do 120 znaków
   EN: Enkephalin has been fully recharged.
   PL: Enkefalina została w pełni naładowana.
67. [Interfejs i ustawienia [push_notification_message_full_stamina_1_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_1_title].content
   limit: do 120 znaków
   EN: Enkephalin Charged
   PL: Enkefalina Naładowana
68. [Interfejs i ustawienia [push_notification_message_full_stamina_1_text] — tekst] 이상하다 여길 것은 없소. 그저 엔케팔린이 가득 찼다 말하러 온 것이기에… 용건은 이상이오.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_1_text].content
   limit: do 200 znaków
   EN: Take notice, yet naught is odd here. Ideally, my only purpose here would be to inform you that Enkephalin is replenished fully. Such is all I have to say.
   PL: Nie ma w tym nic osobliwego. Przybyłem jedynie powiadomić, iż Enkefalina wypełniła się po brzegi… To wszystko z mej strony.
69. [Interfejs i ustawienia [push_notification_message_full_stamina_2_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_2_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
70. [Interfejs i ustawienia [push_notification_message_full_stamina_2_text] — tekst] 엔케팔린이 가득 찼네요. 관리자님. 효율적인 사용을 위해서 모듈로의 변환을 추천드립니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_2_text].content
   limit: do 160 znaków
   EN: Enkephalin recharge is complete. Dear manager, Enkephalin module conversion is recommended for the sake of efficiency.
   PL: Ładowanie Enkefaliny zakończone, Kierowniku. W trosce o wydajność zalecam przetworzenie jej w moduły.
71. [Interfejs i ustawienia [push_notification_message_full_stamina_3_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_3_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Interfejs i ustawienia [push_notification_message_full_stamina_3_text] — tekst] 연료통이 빵빵해졌소, 관리자 나리이이!!! 모험을 떠나야 하는데 어디로 간 겐가!!!
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_3_text].content
   limit: do 130 znaków
   EN: MANAGER ESQUIRE!!! THE FUEL TANK HATH BEEN REFILLED!!! COME HITHER, FOR OUR ADVENTURES MUST GO ON!!!
   PL: KIEROWNIKU SZLACHETNY!!! ZBIORNIK PALIWA JEST PEŁEN PO BRZEGI!!! PRZYBYWAJ, ALBOWIEM PRZYGODA WZYWA!!!
73. [Interfejs i ustawienia [push_notification_message_full_stamina_4_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_4_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
74. [Interfejs i ustawienia [push_notification_message_full_stamina_4_text] — tekst] 엔.팔.충.완.(엔케팔린 충전 완료.)
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_4_text].content
   limit: do 120 znaków
   EN: E.C.(Enkephalin Charged.)
   PL: E.N. (Enkefalina Naładowana.)
75. [Interfejs i ustawienia [push_notification_message_full_stamina_5_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_5_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
76. [Interfejs i ustawienia [push_notification_message_full_stamina_5_text] — tekst] 엔케팔린 충전이 완료되었습니다, 관리자님.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_5_text].content
   limit: do 120 znaków
   EN: Enkephalin has been fully recharged, manager.
   PL: Ładowanie Enkefaliny zostało zakończone, Kierowniku.
77. [Interfejs i ustawienia [push_notification_message_full_stamina_6_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_6_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Interfejs i ustawienia [push_notification_message_full_stamina_6_text] — tekst] 와아~ 벌써 엔케팔린이 다 충전됐나 봐요~ 확인해 보러 가지 않으실래요?
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_6_text].content
   limit: do 120 znaków
   EN: Woow~ Enkephalin's already fully charged~ Would you like to go check?
   PL: Ojej~ Wygląda na to, że Enkefalina już się naładowała~ Zajrzymy tam razem?
79. [Interfejs i ustawienia [push_notification_message_full_stamina_7_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_7_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Interfejs i ustawienia [push_notification_message_full_stamina_7_text] — tekst] 그 뭐냐. 엔케…? 아무튼 초록색 연료 그거 충전 다 됐다더라. 가서 좀 봐.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_7_text].content
   limit: do 120 znaków
   EN: The, uh. Enkeph—? ... The green stuff's full. Go take a gander, yeah?
   PL: Ej, to całe… Enkefa-coś tam? No, to zielone paliwo jest już pełne. Idź rzuć okiem.
81. [Interfejs i ustawienia [push_notification_message_full_stamina_8_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_8_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Interfejs i ustawienia [push_notification_message_full_stamina_8_text] — tekst] 엔케팔린 충전 완료... 음. 다시 버스가 출발할 수 있겠네요. 어서 가보죠.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_8_text].content
   limit: do 120 znaków
   EN: Enkephalin's been recharged... Hm. Yeah, the bus is ready for another voyage. Let's go.
   PL: Enkefalina naładowana… Hm. Autobus może znów ruszać w drogę. Chodźmy.
83. [Interfejs i ustawienia [push_notification_message_full_stamina_9_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_9_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Interfejs i ustawienia [push_notification_message_full_stamina_9_text] — tekst] 단테~ 엔케팔린 충전 끝났어. 모듈로 안 바꾸면 더 안 쌓일 거라구~
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_9_text].content
   limit: do 120 znaków
   EN: Dante~ Enkephalin's charged! Don'tcha forget to convert 'em to modules!
   PL: Dante~ Enkefalina już pełna! Jak nie przerobisz jej na moduły, więcej się nie zmieści~
85. [Interfejs i ustawienia [push_notification_message_full_stamina_11_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_11_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Interfejs i ustawienia [push_notification_message_full_stamina_11_text] — tekst] 관리자님... 바쁘신가요? 벼, 별건 아니고… 엔케팔린이 넘치고 있어서…
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_11_text].content
   limit: do 130 znaków
   EN: Hi, manager... are you... busy? I-it's nothing too serious, but... Enkephalin's about to overflow...
   PL: Kierowniku… jesteś zajęty? N-nic wielkiego, tylko… Enkefalina zaraz zacznie się przelewać…
87. [Interfejs i ustawienia [push_notification_message_full_stamina_12_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_12_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
88. [Interfejs i ustawienia [push_notification_message_full_stamina_12_text] — tekst] 보고드립니다, 관리자님. 엔케팔린이 완충되었습니다. 소모나 축적을 권장드립니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_12_text].content
   limit: do 160 znaków
   EN: Reporting to the Executive Manager. Enkephalin has been fully replenished. May I suggest that you use or convert them?
   PL: Melduję, Kierowniku Wykonawczy. Enkefalina osiągnęła pełny stan. Zalecam jej zużycie bądź konwersję.
89. [Interfejs i ustawienia [push_notification_message_full_stamina_13_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_13_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Interfejs i ustawienia [push_notification_message_full_stamina_13_text] — tekst] 어어, 관리자 양반! 그, 버스 연료가 가득 찼는데... 한 번 확인하지 그래?
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_13_text].content
   limit: do 120 znaków
   EN: Uhh, manager bud? You there? The, uh, the bus fuel tank is full... Might wanna come check?
   PL: Eee, Kierowniku! Słuchaj no, bak w autobusie pełny… Może byś tak zerknął?
91. [Interfejs i ustawienia [push_notification_message_full_stamina_14_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_14_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Interfejs i ustawienia [push_notification_message_full_stamina_14_text] — tekst] 휴식 시간은 끝났습니다. 관리자 단테. 버스를 너무 오래 세워두지 마시지요.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_14_text].content
   limit: do 120 znaków
   EN: Your break is over, Manager Dante. Don't keep the bus sitting for too long.
   PL: Koniec przerwy, Kierowniku Dante. Nie trzymaj autobusu na postoju zbyt długo.
93. [Interfejs i ustawienia [push_notification_message_full_stamina_15_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_15_title].content
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Interfejs i ustawienia [push_notification_message_full_stamina_15_text] — tekst] 메피가 배부르대, 카론. 부릉부릉할 시간이야.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_15_text].content
   limit: do 120 znaków
   EN: Mephi's stuffed. Charon, time to vroom-vroom.
   PL: Mefi ma pełny brzuszek. Charon mówi, że pora na brum-brum.
95. [Interfejs i ustawienia [custom_localize_button] — tekst] 커스텀 언어 선택
   źródło: LoginUIText.json :: dataList[id=custom_localize_button].content
   limit: do 120 znaków
   EN: Select Custom Language
   PL: Wybierz własny język
96. [Interfejs i ustawienia [custom_localize_title] — tekst] 커스텀 언어 선택
   źródło: LoginUIText.json :: dataList[id=custom_localize_title].content
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Interfejs i ustawienia [custom_localize_desc] — tekst] ※ 언어 변경은 게임 재시작 시 정상 적용됩니다.
   źródło: LoginUIText.json :: dataList[id=custom_localize_desc].content
   limit: do 120 znaków
   EN: ※ Restart the game to apply the language change.
   PL: ※ Zmiana języka zostanie zastosowana po ponownym uruchomieniu gry.
98. [Interfejs i ustawienia [steam_overlay_cannot_activate_title] — tekst] 스팀 거래 오류
   źródło: LoginUIText.json :: dataList[id=steam_overlay_cannot_activate_title].content
   limit: do 120 znaków
   EN: Steam Transaction Error
   PL: Błąd transakcji Steam
99. [Interfejs i ustawienia [steam_overlay_cannot_activate_text] — tekst] Steam 라이브러리에서\n[게임 내 Steam 오버레이 사용]을 활성화 후\n재접속해주세요.
   źródło: LoginUIText.json :: dataList[id=steam_overlay_cannot_activate_text].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please turn on the [Enable the Steam Overlay while in-game] option\nfrom Steam's game properties - General,\nthen restart the game.
   PL: Włącz opcję [Włącz nakładkę Steam podczas gry]\nw ustawieniach gry w Bibliotece Steam,\na następnie uruchom grę ponownie.
100. [Interfejs i ustawienia [servererror_remain_restore_purchasing] — tekst] 아직 진행중이던 거래가 존재합니다.\n[구매 복구] 버튼을 눌러 재시도해주세요.
   źródło: LoginUIText.json :: dataList[id=servererror_remain_restore_purchasing].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A transaction is still in progress.\nPlease use the [Restore Purchase] button and try again.
   PL: Poprzednia transakcja wciąż trwa.\nUżyj przycisku [Przywróć zakupy] i spróbuj ponownie.
101. [Interfejs i ustawienia [invalid_login_no_guest_uid] — tekst] 게스트 계정이 존재하지 않거나,\n탈퇴된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=invalid_login_no_guest_uid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Guest account does not exist,\nor has been deleted.
   PL: Konto gościa nie istnieje\nlub zostało usunięte.
102. [Interfejs i ustawienia [invalid_login_is_not_guest] — tekst] 이 게스트 계정은 이미 플랫폼과 연동되어 있습니다.\n[계정 변경]을 눌러 연동된 플랫폼으로 로그인해 주세요.
   źródło: LoginUIText.json :: dataList[id=invalid_login_is_not_guest].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Guest account is already linked to a platform.\nPlease use the [Change Account] button to log into your linked platform.
   PL: To konto gościa jest już powiązane z platformą.\nKliknij [Zmień konto], aby zalogować się przez powiązaną platformę.
103. [Interfejs i ustawienia [try_new_guest] — tekst] 새로운 게스트 계정을 만드시겠습니까?
   źródło: LoginUIText.json :: dataList[id=try_new_guest].content
   limit: do 120 znaków
   EN: Make a new Guest account?
   PL: Utworzyć nowe konto gościa?
104. [Interfejs i ustawienia [need_verify_integrity_steam] — tekst] 일부 리소스의 누락이 감지되었습니다.\n스팀 무결성 검사를 진행해 주세요
   źródło: LoginUIText.json :: dataList[id=need_verify_integrity_steam].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Missing resources detected.\nPlease use Steam's "Verify integrity of game files" function.
   PL: Wykryto brakujące zasoby.\nUżyj funkcji „Sprawdź spójność plików gry” na Steam.

## Interfejs i ustawienia: MainUIText-a1c10p1
- plik gry: `MainUIText-a1c10p1.json`

105. [Interfejs i ustawienia [main_ui_rpg_battle_defeated_title] — tekst] 전투 패배
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_battle_defeated_title].content
   limit: do 120 znaków
   EN: Battle Lost
   PL: Porażka w Walce
106. [Interfejs i ustawienia [main_ui_rpg_battle_defeated_desc] — tekst] <color=#990000>모든 수감자가 사망했습니다.</color>\n이후 진행을 선택해주세요.
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_battle_defeated_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: <color=#990000>All Sinners have been defeated.</color>\nChoose what you would like to do next.
   PL: <color=#990000>Wszyscy Grzesznicy polegli.</color>\nWybierz dalsze działanie.
107. [Interfejs i ustawienia [main_ui_rpg_retry] — tekst] 재도전
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_retry].content
   limit: do 120 znaków
   EN: Try Again
   PL: Ponów próbę
108. [Interfejs i ustawienia [main_ui_rpg_retry_desc] — tekst] 해당 전투를 처음부터 다시 시작
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_retry_desc].content
   limit: do 120 znaków
   EN: Restart this battle from the beginning
   PL: Rozpocznij tę walkę od początku
109. [Interfejs i ustawienia [main_ui_rpg_accept_defeat] — tekst] 포기
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_accept_defeat].content
   limit: do 120 znaków
   EN: Forfeit
   PL: Poddaj się
110. [Interfejs i ustawienia [main_ui_rpg_accept_defeat_desc] — tekst] 마지막 저장 상태의 샘터로 복귀
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_accept_defeat_desc].content
   limit: do 120 znaków
   EN: Return to the Fount of the last save state
   PL: Wróć do Źródełka z ostatniego zapisu
111. [Interfejs i ustawienia [ContinueConfirm_Desc_Rpg_Stage] — tekst] 10-4 스테이지는 전투 중 컨티뉴 기능을 사용하여도 \n최종 클리어 시 EX 클리어로 기록됩니다.\n\n단, 컨티뉴 사용 이후 <color=#990000>재도전, 패배, 포기 없이 전투에서 승리하고 진행도가 저장</color>된 경우,\n<color=#990000>10-4 스테이지를 중도 포기하여도 컨티뉴에 사용된 재화가 반환되지 않습니다.</color>\n또한 사용된 광기는 청약철회가 불가능합니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=ContinueConfirm_Desc_Rpg_Stage].content
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: Regardless of whether the player used the Continue function or not,\nclearing Stage 10-4 will mark it as "Extra Conditions Fulfilled".\n\nHowever, <color=#990000>forfeiting Stage 10-4 will not refund any resources consumed to use the Continue function if a save state is created in Stage 10-4 <i>after</i> the user makes use of the Continue function to win the Encounter in question without retrying, losing, or forfeiting.</color>\n\nPlease note that consumed Lunacy cannot be refunded.
   PL: Na etapie 10-4 użycie funkcji Kontynuacji w trakcie walki nadal pozwala uzyskać ukończenie EX.\n\nJednakże jeśli po użyciu Kontynuacji <color=#990000>wygrasz walkę bez ponawiania, porażki ani poddania i postęp zostanie zapisany</color>,\n<color=#990000>późniejsze porzucenie etapu 10-4 nie zwróci waluty zużytej na Kontynuację.</color>\nZużyte Szaleństwo nie podlega zwrotowi.
112. [Interfejs i ustawienia [formation_ego_resource_popup_current_owned_desc] — tekst] 현재 보유한 E.G.O 자원의 수량입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ego_resource_popup_current_owned_desc].content
   limit: do 120 znaków
   EN: Currently owned E.G.O Resources can be viewed here.
   PL: Liczba posiadanych obecnie zasobów E.G.O.
113. [Interfejs i ustawienia [formation_ego_resource_popup_current_owned] — tekst] 보유 E.G.O 자원
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ego_resource_popup_current_owned].content
   limit: do 120 znaków
   EN: E.G.O Resource Stock
   PL: Zasoby E.G.O
114. [Interfejs i ustawienia [9128_chapter_notice_button_title] — tekst] 챕터 유의사항
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_button_title].content
   limit: do 120 znaków
   EN: Warning
   PL: Uwagi o rozdziale
115. [Interfejs i ustawienia [9128_chapter_notice_popup_title] — tekst] 현재 플레이하고 있는 챕터는 <color=#3246AB>[{0}장 {1}]</color>입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_popup_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#3246AB>, </color>, {0}, {1}
   EN: You are currently playing through Chapter <color=#3246AB>[{0} - {1}]</color>.
   PL: Obecnie rozgrywany rozdział to <color=#3246AB>[Rozdział {0}: {1}]</color>.
116. [Interfejs i ustawienia [9128_chapter_notice_enter_title] — tekst] <color=#3246AB>[{0}장 {1}]</color>에 진입하시겠습니까?
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_enter_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#3246AB>, </color>, {0}, {1}
   EN: Enter <color=#3246AB>[Chapter {0} - {1}]</color>?
   PL: Czy chcesz wejść do <color=#3246AB>[Rozdziału {0}: {1}]</color>?
117. [Interfejs i ustawienia [9128_chapter_notice_popup_desc] — tekst] ◆ 이전 챕터를 클리어하지 않았더라도 <color=#ff6000><mark color=#ff000040><b><u>주요 이야기 10장의 플레이가 가능</color></mark></b></u>합니다.\n◆ <color=#ff6000><mark color=#ff000040><b><u>9.5장까지의 스포일러</color></mark></b></u>를 담고 있습니다.\n◆ 10장을 클리어했을 때 이전 챕터를 클리어하지 않은 경우, 거울 던전, 거울굴절철도, 채광, 사영전투 등 <color=#ff6000><mark color=#ff000040><b><u>이전 챕터를 클리어해야 개방되는 콘텐츠를 이용할 수 없습니다.</color></mark></b></u> 모든 콘텐츠를 이용하기 위해 개방 조건을 충족해주시기 바랍니다.\n◆ 10장 클리어를 조건으로 하는 콘텐츠(향후 업데이트 예정)는 <color=#ff6000><mark color=#ff000040><b><u>10장 및 9.5-26 스테이지를 클리어</color></mark></b></u>해주시기 바랍니다.\n◆ 10장 플레이 시, <color=#ff6000><mark color=#ff000040><b><u>뫼르소의 일부 인격이 지원</color></mark></b></u>됩니다. (지원 인격 및 E.G.O에는 동기화/환상 해석 4단계가 적용됩니다.)\n◆ 10장 플레이 시, <color=#ff6000><mark color=#ff000040><b><u>모든 아군의 인격 동기화 3단계가 지원</color></mark></b></u>됩니다. E.G.O는 별도로 환상 해석이 보정되지 않습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_popup_desc].content
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: ◆ <color=#ff6000><mark color=#ff000040><b><u>Main Story Canto 10 can be played</color></mark></b></u> without clearing previous story chapters.\n◆ <color=#ff6000><mark color=#ff000040><b><u>Canto 10 contains spoilers up to Intervallo VII-2.</color></mark></b></u>\n◆ If you have not cleared the previous chapter by the time you have cleared Canto 10, <color=#ff6000><mark color=#ff000040><b><u>various content that requires Main Story progression (Mirror Dungeon, Refraction Railway, Luxcavation, Reflectrial, etc.) will not be unlocked until each respective prerequisite is cleared.</color></mark></b></u>\n◆ For any future content that requires clearing Canto 10 as the prerequisite, <color=#ff6000><mark color=#ff000040><b><u>please clear both Canto 10 and Stage 9.5-26 to unlock.</color></mark></b></u>\n◆ During Canto 10, <color=#ff6000><mark color=#ff000040><b><u>Meursault will have access to certain Support Identities</color></mark></b></u> and E.G.O (at Uptie/Threadspinning Tier 4).\n◆ During Canto 10, <color=#ff6000><mark color=#ff000040><b><u>all allied Identities, including Meursault, will be guaranteed at least Uptie 3</color></mark></b></u> (E.G.O Threadspinning Tier will not be affected).
   PL: ◆ <color=#ff6000><mark color=#ff000040><b><u>Rozdział 10 Głównej Opowieści można rozegrać</u></b></mark></color> nawet bez ukończenia poprzednich rozdziałów.\n◆ Zawiera <color=#ff6000><mark color=#ff000040><b><u>spoilery aż do Rozdziału 9.5</u></b></mark></color>.\n◆ Jeśli ukończysz Rozdział 10 bez przejścia wcześniejszych rozdziałów, <color=#ff6000><mark color=#ff000040><b><u>zawartość wymagająca postępów fabularnych (Lustrzane Lochy, Kolej Załamania, Wydobycie, Walki Projekcyjne itd.) pozostanie zablokowana</u></b></mark></color> do czasu spełnienia odpowiednich warunków.\n◆ Aby odblokować przyszłą zawartość wymagającą Rozdziału 10, <color=#ff6000><mark color=#ff000040><b><u>ukończ zarówno Rozdział 10, jak i etap 9.5-26</u></b></mark></color>.\n◆ W Rozdziale 10 <color=#ff6000><mark color=#ff000040><b><u>udostępniane są wybrane Tożsamości Wsparcia dla Meursaulta</u></b></mark></color> (Synchronizacja / Splot Nici na poziomie 4).\n◆ W Rozdziale 10 <color=#ff6000><mark color=#ff000040><b><u>wszystkie sojusznicze Tożsamości mają gwarantowany co najmniej 3. poziom Synchronizacji</u></b></mark></color> (poziom Splotu Nici E.G.O nie ulega zmianie).
118. [Interfejs i ustawienia [settings_battle_effect_gate] — tekst] 중요 전투 진행 시 인격/E.G.O 연출용 오브젝트 숨김
   źródło: MainUIText-a1c10p1.json :: dataList[id=settings_battle_effect_gate].content
   limit: do 120 znaków
   EN: Hide Identity/E.G.O props in plot-critical battles
   PL: Ukryj rekwizyty Tożsamości/E.G.O w kluczowych walkach fabularnych
119. [Interfejs i ustawienia [exp_dungeon_10_open_condition] — tekst] 9.5-26 및 10-4 클리어
   źródło: MainUIText-a1c10p1.json :: dataList[id=exp_dungeon_10_open_condition].content
   limit: do 120 znaków
   EN: Clear 9.5-26 and 10-4
   PL: Ukończ 9.5-26 oraz 10-4
120. [Interfejs i ustawienia [formation_deck_code_condition_reset] — tekst] 편성 조건에 맞지 않는 인격은 기본 인격으로 적용되었습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_deck_code_condition_reset].content
   limit: do 140 znaków
   EN: Base Identities have been applied in place of Identities that do not meet the Team Loadout requirement.
   PL: Tożsamości niespełniające warunków składu zastąpiono Tożsamościami Bazowymi.
121. [Interfejs i ustawienia [character_list_friend_support_companion_impossible] — tekst] 함께 지정되는 {0}의 지원 인격을 지정할 수 없는 스테이지입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=character_list_friend_support_companion_impossible].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} will be selected in tandem. This Stage does not allow you to use their Support Identity.
   PL: Na tym etapie nie można użyć Tożsamości Wsparcia dla powiązanego Grzesznika ({0}).
122. [Interfejs i ustawienia [gacha_additional_explain_button_label] — tekst] 동시 획득 인격 안내
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_additional_explain_button_label].content
   limit: do 120 znaków
   EN: Pair Identity Details
   PL: Tożsamości Parzyste
123. [Interfejs i ustawienia [gacha_307_additional_explain_title] — tekst] 동시 획득 인격 안내
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_307_additional_explain_title].content
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Interfejs i ustawienia [gacha_307_additional_explain_desc] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며,\n등장 시 두 인격을 항상 함께 획득합니다.\n\n· 쐐기 사무소 해결사 돈키호테 & 쐐기 사무소 해결사 싱클레어의 등장 확률은 아래와 같습니다.\n- 두 인격이 대표 3성 인격(픽업)인 특정 추출: 대표 3성 인격 1명의 등장 확률과 동일\n- 그 외 두 인격이 등장하는 추출: 대표가 아닌 3성 인격 1명의 등장 확률과 동일\n(자세한 확률은 각 추출의 [확률 상세보기]에서 확인할 수 있습니다.)\n \n· 별빛도 3성 인격 1명분으로 계산되어, 추출에서 첫 획득 시 두 인격을 합쳐 별빛 300개를 얻습니다.\n\n· 두 인격이 대표 3성 인격인 특정 추출에서는 이상[理想] 200개로 두 인격을 함께 교환할 수 있습니다.\n\n· 두 인격을 이미 보유한 상태에서 다시 획득하면,\n등급에 따른 자아 파편 대신 현재 시즌의 돈키호테 자아 파편 25개와 싱클레어 자아 파편 25개를 획득합니다.\n\n· 자판기에 추가된 후에는 돈키호테 자아 파편과 싱클레어 자아 파편을 합쳐 400개로 두 인격을 함께 구입할 수 있습니다. 두 자아 파편을 각각 1개 이상 사용해야 하며, 비율은 자유롭게 정할 수 있습니다.\n\n· 인격 레벨 상승, 동기화, 외형 투영 시 두 인격을 각각 따로 진행해야하며, 인격마다 일반 3성 인격과 같은 재료가 필요합니다. 이때 자아 파편은 해당 수감자의 자아 파편을 사용합니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_307_additional_explain_desc].content
   limit: do 2090 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wedge Office Fixer Don Quixote and Wedge Office Fixer Sinclair are treated as a single 3★ Identity in the Extraction. Obtaining either Identity will always yield the other in the pair.\n\n· The Extraction rates for Wedge Office Fixer Don Quixote & Wedge Office Fixer Sinclair are as follows:\n  - In Target Extractions where the pair is featured as the 3★ pickup: The same appearance rate as 1 featured 3★ Identity\n  - In all other Extractions where the pair can appear: The same appearance rate as 1 non-featured 3★ Identity\n(for detailed rates, please refer to [Probabilities] for each Extraction)\n\n· Starlight is also calculated as if the pair were a single 3★ Identity. When first obtained through Extraction, the two Identities grant a combined total of 300 Starlight.\n\n· In Target Extractions where both Identities are featured as the 3★ pickup, both can be exchanged together for 200 Yisang [Ideality].\n\n· If the pair is obtained again after both Identities have already been acquired, you will receive 25 Don Quixote Egoshards and 25 Sinclair Egoshards from the current Season instead of the usual Egoshards awarded for duplicate Identities of their rarity.\n\n· Once the pair is added to the Dispenser, both Identities can be obtained together for a combined total of 400 Don Quixote and Sinclair Egoshards. You must use at least 1 Egoshard from each Sinner, but you can adjust the ratio between the two freely.\n\n· Identity level-ups, Upties, and Façade Projection must be performed separately for each Identity. Each Identity requires the same materials as a standard 3★ Identity. Any Egoshards required for these upgrades must belong to the respective Sinner.
   PL: Fikserka Biura Klina Don Quixote oraz Fikser Biura Klina Sinclair są traktowani w Ekstrakcji jako pojedyncza Tożsamość 3★ — wylosowanie jednej z nich zawsze przyznaje obie naraz.\n\n· Szanse pojawienia się pary Fikserka Biura Klina Don Quixote i Fikser Biura Klina Sinclair:\n  - W Ekstrakcji Celowanej, w której para jest wyróżnioną Tożsamością 3★: taka sama szansa jak dla 1 wyróżnionej Tożsamości 3★\n  - W pozostałych Ekstrakcjach, w których para występuje: taka sama szansa jak dla 1 niewyróżnionej Tożsamości 3★\n(szczegółowe wartości znajdziesz w oknie [Szczegóły szans] danej Ekstrakcji).\n\n· Gwiezdny Blask również naliczany jest jak za jedną Tożsamość 3★ — przy pierwszym zdobyciu pary otrzymasz łącznie 300 szt. Gwiezdnego Blasku.\n\n· W Ekstrakcji Celowanej z tą parą obie Tożsamości można wymienić łącznie za 200 pkt Yisang [Ideału].\n\n· Ponowne wylosowanie posiadanej już pary przyznaje 25 Odłamków E.G.O Don Quixote oraz 25 Odłamków E.G.O Sinclaira z bieżącego sezonu zamiast standardowej liczby Odłamków.\n\n· Po dodaniu pary do Automatu obie Tożsamości można kupić razem za łącznie 400 Odłamków E.G.O Don Quixote i Sinclaira. Należy użyć co najmniej po 1 Odłamku każdego z dwojga Grzeszników, a pozostałą proporcję można dobrać dowolnie.\n\n· Podnoszenie poziomu, Synchronizację oraz Projekcję Wyglądu wykonuje się osobno dla każdej z dwóch Tożsamości, zużywając standardową ilość materiałów dla Tożsamości 3★ danego Grzesznika.
125. [Interfejs i ustawienia [formation_ui_panel_start_battle_lor] — tekst] 접대 시작
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ui_panel_start_battle_lor].content
   limit: do 120 znaków
   EN: Commence Reception
   PL: Rozpocznij Przyjęcie
126. [Interfejs i ustawienia [battle_walpu10_ego_page_history_ashes] — tekst] 밝은 모든 것들을 남김없이 태워버리기 위해…
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_ashes].content
   limit: do 120 znaków
   EN: To burn all things that are bright to ashes...
   PL: Aby spalić na popiół wszystko, co jasne…
127. [Interfejs i ustawienia [battle_walpu10_ego_page_history_nostalgic_embrace] — tekst] 나를 꼬옥 안아주지 않을래? 마음이 편해질 거야.
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_nostalgic_embrace].content
   limit: do 120 znaków
   EN: Give me a tight hug, will you? It'll soothe your mind.
   PL: Przytulisz mnie mocno? Od razu zrobi ci się lżej na duszy.
128. [Interfejs i ustawienia [battle_walpu10_ego_page_history_gluttony] — tekst] 우리가 네 곁을 지키는 이유?\n당연히 보호하기 위해서지!
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_gluttony].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The reason we're staying by your side?\nOf course it's to protect you!
   PL: Dlaczego trwamy u twego boku?\nOczywiście po to, by cię chronić!
129. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not_already_have_companion] — tekst] 선택한 인격을 모두 이미 보유 중입니다. 이상[理想] 200개를 소모하여 각 수감자의 파편을 25개씩 교환하시겠습니까?
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_pity_point_progress_or_not_already_have_companion].content
   limit: do 140 znaków
   EN: You already own the selected Identity pair. Exchange 200 Yisang [Ideality] for each Sinner's 25 Egoshards?
   PL: Posiadasz już obie wybrane Tożsamości. Czy chcesz wymienić 200 pkt Yisang [Ideału] na po 25 Odłamków E.G.O każdego z tych Grzeszników?
130. [Interfejs i ustawienia [notice_of_vending_machine_companion_1] — tekst] 돈키호테 자아 파편과 싱클레어 자아 파편을 합쳐 400개로 두 인격을 함께 구입할 수 있습니다. 두 자아 파편을 각각 1개 이상 사용해야 하며, 비율은 자유롭게 정할 수 있습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_vending_machine_companion_1].content
   limit: do 270 znaków
   EN: Both Identities can be obtained together for a combined total of 400 Don Quixote and Sinclair Egoshards. You must use at least 1 Egoshard from each Sinner, but you can adjust the ratio between the two freely.
   PL: Obie Tożsamości można kupić razem za łącznie 400 Odłamków E.G.O Don Quixote i Sinclaira. Należy użyć co najmniej po 1 Odłamku każdego z dwojga Grzeszników, a pozostałą proporcję można dobrać dowolnie.
131. [Interfejs i ustawienia [notice_of_story_same_content] — tekst] {0}와 동일한 내용으로, 보상만 수령되었습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_story_same_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Contents the same as {0}. Only the reward is obtained.
   PL: Zawartość identyczna z {0} — odebrano wyłącznie nagrodę.
132. [Interfejs i ustawienia [10th_anniversary_event_desc] — tekst] 기간 내 접속 시 3성 인격 출현 추출 티켓 및 광기 증정
   źródło: MainUIText-a1c10p1.json :: dataList[id=10th_anniversary_event_desc].content
   limit: do 120 znaków
   EN: Log in during the event and pick up a [3★ Guarantee Decaextraction Ticket and Lunacy]
   PL: Zaloguj się w trakcie wydarzenia, aby odebrać [Bilet Dekstrakcji Gwarantowanej 3★ oraz Szaleństwo]

## Interfejs i ustawienia: MainUIText-a1c7p1
- plik gry: `MainUIText-a1c7p1.json`

133. [Interfejs i ustawienia [stage_recommend_level_popup_battle_participant_desc] — tekst] 전투에 참가할 인격의 현재 평균 레벨이 스테이지 권장 레벨보다 <color=#990000>낮습니다.</color>\n전투를 진행하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_battle_participant_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: The current average level of your deployed Identities is <color=#990000>lower</color> than the recommended level for this Stage.\nStart the Encounter anyway?
   PL: Średni poziom wybranych do walki Tożsamości jest <color=#990000>niższy</color> od zalecanego poziomu etapu.\nRozpocząć walkę mimo to?
134. [Interfejs i ustawienia [stage_recommend_level_popup_formation_desc] — tekst] 현재 편성의 육성 수준이 권장 사양보다 <color=#990000>낮습니다. 진입 시 어려운 전투가 진행될 수 있습니다.</color>\n전투를 진행하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_formation_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: Your current loadout's average upgrade progress is <color=#990000>below the recommended specs, and you may face a difficult battle.</color>\nEnter the battle anyway?
   PL: Poziom rozwinięcia obecnego składu jest <color=#990000>niższy od zalecanego — walka może okazać się bardzo trudna.</color>\nRozpocząć walkę mimo to?
135. [Interfejs i ustawienia [stage_recommend_level_popup_dungeon_entrance_desc] — tekst] 편성 인격의 현재 평균 레벨이 스테이지 권장 레벨보다 <color=#990000>낮습니다.</color>\n던전에 입장하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_dungeon_entrance_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: The current average level of Identities in your loadout is <color=#990000>lower</color> than the recommended level for this Stage.\nEnter the Dungeon anyway?
   PL: Średni poziom Tożsamości w składzie jest <color=#990000>niższy</color> od zalecanego poziomu etapu.\nWejść do lochu mimo to?
136. [Interfejs i ustawienia [current_average_level_and_recommend_level_format] — tekst] 현재 평균 레벨: {0}\n<color=#f8c200>스테이지 권장 레벨: {1}</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=current_average_level_and_recommend_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, \n
   EN: Current Avg. Level: {0}\n<color=#f8c200>Recommended Level: {1}</color>
   PL: Obecny śr. poziom: {0}\n<color=#f8c200>Zalecany poziom etapu: {1}</color>
137. [Interfejs i ustawienia [current_average_level_with_additional_val_and_recommend_level_format] — tekst] 현재 평균 레벨: {0} ({1})\n<color=#f8c200>스테이지 권장 레벨: {2}</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=current_average_level_with_additional_val_and_recommend_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, {2}, \n
   EN: Current Avg. Level: {0} ({1})\n<color=#f8c200>Recommended Level: {2}</color>
   PL: Obecny śr. poziom: {0} ({1})\n<color=#f8c200>Zalecany poziom etapu: {2}</color>
138. [Interfejs i ustawienia [stage_recommend_uptie_popup_dungeon_entrance_desc] — tekst] <color=#f8c200>인격 동기화, E.G.O 환상 해석 <color=#990000>{0}단계</color> 권장</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_uptie_popup_dungeon_entrance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#990000>, </color>, {0}
   EN: <color=#f8c200>Recommended Identity & E.G.O Uptie/Threadspin <color=#990000>Tiers: {0}</color> </color>
   PL: <color=#f8c200>Zalecana Synchronizacja Tożsamości i Splot Nici E.G.O: <color=#990000>Poziom {0}</color></color>

## Interfejs i ustawienia: MainUIText
- plik gry: `MainUIText.json`

139. [Interfejs i ustawienia [mainui_main_button0] — tekst] 유리창
   źródło: MainUIText.json :: dataList[id=mainui_main_button0].content
   limit: do 120 znaków
   EN: Window
   PL: Okno
140. [Interfejs i ustawienia [mainui_main_button1] — tekst] 수감자
   źródło: MainUIText.json :: dataList[id=mainui_main_button1].content
   limit: do 120 znaków
   EN: Sinners
   PL: Grzesznicy
141. [Interfejs i ustawienia [mainui_main_button2] — tekst] 상영관
   źródło: MainUIText.json :: dataList[id=mainui_main_button2].content
   limit: do 120 znaków
   EN: Theater
   PL: Teatr
142. [Interfejs i ustawienia [mainui_main_button3] — tekst] 운전석
   źródło: MainUIText.json :: dataList[id=mainui_main_button3].content
   limit: do 120 znaków
   EN: Drive
   PL: Jazda
143. [Interfejs i ustawienia [mainui_main_button4] — tekst] 추출
   źródło: MainUIText.json :: dataList[id=mainui_main_button4].content
   limit: do 120 znaków
   EN: Extract
   PL: Ekstrakcja
144. [Interfejs i ustawienia [mainui_main_button5] — tekst] 자판기
   źródło: MainUIText.json :: dataList[id=mainui_main_button5].content
   limit: do 120 znaków
   EN: Dispense
   PL: Automat
145. [Interfejs i ustawienia [mainui_main_exp] — tekst] EXP
   źródło: MainUIText.json :: dataList[id=mainui_main_exp].content
   limit: do 120 znaków
   EN: EXP
   PL: PD
146. [Interfejs i ustawienia [mainui_main_stamina] — tekst] 스태미너
   źródło: MainUIText.json :: dataList[id=mainui_main_stamina].content
   limit: do 120 znaków
   EN: Stamina
   PL: Kondycja
147. [Interfejs i ustawienia [mainui_main_enkephalin] — tekst] 엔케팔린
   źródło: MainUIText.json :: dataList[id=mainui_main_enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin
   PL: Enkefalina
148. [Interfejs i ustawienia [mainui_main_madness] — tekst] 광기
   źródło: MainUIText.json :: dataList[id=mainui_main_madness].content
   limit: do 120 znaków
   EN: Lunacy
   PL: Szaleństwo
149. [Interfejs i ustawienia [mainui_battleselection_everydungeon] — tekst] 거울 던전
   źródło: MainUIText.json :: dataList[id=mainui_battleselection_everydungeon].content
   limit: do 120 znaków
   EN: Mirror Dungeons
   PL: Lustrzane Lochy
150. [Interfejs i ustawienia [mainui_stageinfo_recommendlevel] — tekst] 추천 레벨
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_recommendlevel].content
   limit: do 120 znaków
   EN: Difficulty
   PL: Zalec. Poz.
151. [Interfejs i ustawienia [mainui_stageinfo_enemyinfo] — tekst] 적 정보
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_enemyinfo].content
   limit: do 120 znaków
   EN: Enemy Info
   PL: Dane Wrogów
152. [Interfejs i ustawienia [mainui_stageinfo_exclearcondition] — tekst] EX 클리어 조건
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_exclearcondition].content
   limit: do 120 znaków
   EN: EX Objectives
   PL: Warunki EX
153. [Interfejs i ustawienia [mainui_stageinfo_statinfo] — tekst] 스테이터스
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_statinfo].content
   limit: do 120 znaków
   EN: Status
   PL: Status
154. [Interfejs i ustawienia [mainui_stageinfo_resistinfo] — tekst] 내성 정보
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_resistinfo].content
   limit: do 120 znaków
   EN: Resistances
   PL: Odporności
155. [Interfejs i ustawienia [mainui_stageinfo_enterbutton] — tekst] 입장
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_enterbutton].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
156. [Interfejs i ustawienia [mainui_stageinfo_dungeonclear] — tekst] 던전 클리어 조건
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_dungeonclear].content
   limit: do 120 znaków
   EN: Main Objectives
   PL: Cel Lochu
157. [Interfejs i ustawienia [mainui_sinners_battleannouncer] — tekst] 아나운서
   źródło: MainUIText.json :: dataList[id=mainui_sinners_battleannouncer].content
   limit: do 120 znaków
   EN: Announcer
   PL: Komentator
158. [Interfejs i ustawienia [mainui_sinners_dante] — tekst] 단테
   źródło: MainUIText.json :: dataList[id=mainui_sinners_dante].content
   limit: do 120 znaków
   EN: Dante
   PL: Dante
159. [Interfejs i ustawienia [mainui_sinners_decklist] — tekst] 덱 목록
   źródło: MainUIText.json :: dataList[id=mainui_sinners_decklist].content
   limit: do 120 znaków
   EN: DECK LIST
   PL: LISTA TALII
160. [Interfejs i ustawienia [mainui_sinners_deck] — tekst] 덱
   źródło: MainUIText.json :: dataList[id=mainui_sinners_deck].content
   limit: do 120 znaków
   EN: Deck
   PL: Talia
161. [Interfejs i ustawienia [mainui_sinners_passive] — tekst] 지속 효과
   źródło: MainUIText.json :: dataList[id=mainui_sinners_passive].content
   limit: do 120 znaków
   EN: PASSIVES
   PL: PASYWKI
162. [Interfejs i ustawienia [mainui_sinners_egoresource] — tekst] E.G.O 자원
   źródło: MainUIText.json :: dataList[id=mainui_sinners_egoresource].content
   limit: do 120 znaków
   EN: AFFINITIES
   PL: ZASOBY E.G.O
163. [Interfejs i ustawienia [mainui_sinners_participant] — tekst] 참여 인원 선택
   źródło: MainUIText.json :: dataList[id=mainui_sinners_participant].content
   limit: do 120 znaków
   EN: Select Participants
   PL: Wybór Uczestników
164. [Interfejs i ustawienia [mainui_sinners_startbattle] — tekst] 전투 시작
   źródło: MainUIText.json :: dataList[id=mainui_sinners_startbattle].content
   limit: do 120 znaków
   EN: To Battle!
   PL: Do Boju!
165. [Interfejs i ustawienia [mainui_common_personality] — tekst] 인격
   źródło: MainUIText.json :: dataList[id=mainui_common_personality].content
   limit: do 120 znaków
   EN: Identities
   PL: Tożsamości
166. [Interfejs i ustawienia [mainui_common_filter] — tekst] 필터
   źródło: MainUIText.json :: dataList[id=mainui_common_filter].content
   limit: do 120 znaków
   EN: Filter
   PL: Filtr
167. [Interfejs i ustawienia [mainui_common_state] — tekst] 현황
   źródło: MainUIText.json :: dataList[id=mainui_common_state].content
   limit: do 120 znaków
   EN: Current
   PL: Stan
168. [Interfejs i ustawienia [mainui_common_sort] — tekst] 정렬
   źródło: MainUIText.json :: dataList[id=mainui_common_sort].content
   limit: do 120 znaków
   EN: Sort
   PL: Sortuj
169. [Interfejs i ustawienia [mainui_sinners_unequipego] — tekst] 미장착
   źródło: MainUIText.json :: dataList[id=mainui_sinners_unequipego].content
   limit: do 120 znaków
   EN: Unequipped
   PL: Brak
170. [Interfejs i ustawienia [mainui_skip_desc] — tekst] 스킵 하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_skip_desc].content
   limit: do 120 znaków
   EN: Are you sure you want to skip?
   PL: Czy na pewno chcesz pominąć?
171. [Interfejs i ustawienia [mainui_story_continue_next_desc] — tekst] 다음 화를 이어보시겠습니까?\n(초회 보상이 있다면 수령후 이어봄)
   źródło: MainUIText.json :: dataList[id=mainui_story_continue_next_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Continue to the next episode?\n(will proceed after receiving any available first-time viewing rewards)
   PL: Przejść do następnego odcinka?\n(ewentualna nagroda za pierwsze obejrzenie zostanie odebrana automatycznie)
172. [Interfejs i ustawienia [mainui_battleresult_reward] — tekst] 보상
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_reward].content
   limit: do 120 znaków
   EN: Rewards
   PL: Nagrody
173. [Interfejs i ustawienia [mainui_battleresult_exclearreward] — tekst] EX 클리어 보상
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_exclearreward].content
   limit: do 120 znaków
   EN: EX Rewards
   PL: Nagrody EX
174. [Interfejs i ustawienia [mainui_battleresult_statistics] — tekst] 통계
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_statistics].content
   limit: do 120 znaków
   EN: Stats
   PL: Statystyki
175. [Interfejs i ustawienia [mainui_ok] — tekst] 확인
   źródło: MainUIText.json :: dataList[id=mainui_ok].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Interfejs i ustawienia [mainui_battleresult_victory] — tekst] 전투 승리
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_victory].content
   limit: do 120 znaków
   EN: Victory
   PL: Zwycięstwo
177. [Interfejs i ustawienia [mainui_battleresult_defeat] — tekst] 전투 패배
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_defeat].content
   limit: do 120 znaków
   EN: Defeat
   PL: Porażka
178. [Interfejs i ustawienia [mainui_battleresult_return] — tekst] 반환
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_return].content
   limit: do 120 znaków
   EN: Return
   PL: Zwrot
179. [Interfejs i ustawienia [mainui_battleresult_hint] — tekst] 힌트
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_hint].content
   limit: do 120 znaków
   EN: Hint
   PL: Wskazówka
180. [Interfejs i ustawienia [mainui_page] — tekst] {0}장
   źródło: MainUIText.json :: dataList[id=mainui_page].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pg. {0}
   PL: Str. {0}
181. [Interfejs i ustawienia [mainui_cancel] — tekst] 취소
   źródło: MainUIText.json :: dataList[id=mainui_cancel].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Interfejs i ustawienia [mainui_select] — tekst] 선택
   źródło: MainUIText.json :: dataList[id=mainui_select].content
   limit: do 120 znaków
   EN: Select
   PL: Wybierz
183. [Interfejs i ustawienia [mainui_select_finished] — tekst] 선택 완료
   źródło: MainUIText.json :: dataList[id=mainui_select_finished].content
   limit: do 120 znaków
   EN: Finalize
   PL: Zatwierdź
184. [Interfejs i ustawienia [mainui_grade] — tekst] {0} 단계
   źródło: MainUIText.json :: dataList[id=mainui_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Stage {0}
   PL: Etap {0}
185. [Interfejs i ustawienia [mainui_floor] — tekst] {0}층
   źródło: MainUIText.json :: dataList[id=mainui_floor].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Floor {0}
   PL: Piętro {0}
186. [Interfejs i ustawienia [mainui_main_enkephalin_Box] — tekst] 엔케팔린 박스
   źródło: MainUIText.json :: dataList[id=mainui_main_enkephalin_Box].content
   limit: do 120 znaków
   EN: Enkephalin Box
   PL: Skrzynka Enkefaliny
187. [Interfejs i ustawienia [mainui_main_own_count] — tekst] 소지 수
   źródło: MainUIText.json :: dataList[id=mainui_main_own_count].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
188. [Interfejs i ustawienia [mainui_mirror_entrance_entry] — tekst] {0}에 입장하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_entry].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Will you enter {0}?
   PL: Czy chcesz wejść do: {0}?
189. [Interfejs i ustawienia [mainui_mirror_entrance_progressing] — tekst] {0}을 진행 중입니다.
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_progressing].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is in progress.
   PL: Trwa wyprawa: {0}.
190. [Interfejs i ustawienia [mainui_mirror_entrance_re_entry] — tekst] 다시 입장하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_re_entry].content
   limit: do 120 znaków
   EN: Will you reenter the dungeon?
   PL: Czy chcesz wejść ponownie?
191. [Interfejs i ustawienia [mainui_mirror_entrance_quit] — tekst] 던전 탐사를 그만두시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_quit].content
   limit: do 120 znaków
   EN: Quit exploring the dungeon?
   PL: Przerwać eksplorację lochu?
192. [Interfejs i ustawienia [mainui_mirror_entrance_quit_former] — tekst] 기존 던전 탐사를 그만두시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_quit_former].content
   limit: do 120 znaków
   EN: Forfeit previous exploration progress?
   PL: Porzucić dotychczasową eksplorację lochu?
193. [Interfejs i ustawienia [mainui_mirror_entrance_warning] — tekst] ※소비한 엔케팔린 모듈은 반환되지 않습니다.
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_warning].content
   limit: do 120 znaków
   EN: ※ Spent Enkephalin Modules will not be refunded.
   PL: ※ Zużyte Moduły Enkefaliny nie podlegają zwrotowi.
194. [Interfejs i ustawienia [mainui_proress] — tekst] 진행
   źródło: MainUIText.json :: dataList[id=mainui_proress].content
   limit: do 120 znaków
   EN: Proceed
   PL: Kontynuuj
195. [Interfejs i ustawienia [mainui_stop] — tekst] 중단
   źródło: MainUIText.json :: dataList[id=mainui_stop].content
   limit: do 120 znaków
   EN: Halt
   PL: Wstrzymaj
196. [Interfejs i ustawienia [mainui_next] — tekst] 다음
   źródło: MainUIText.json :: dataList[id=mainui_next].content
   limit: do 120 znaków
   EN: Next
   PL: Dalej
197. [Interfejs i ustawienia [mainui_ego_list] — tekst] E.G.O 목록
   źródło: MainUIText.json :: dataList[id=mainui_ego_list].content
   limit: do 120 znaków
   EN: E.G.O List
   PL: Lista E.G.O
198. [Interfejs i ustawienia [mainui_personality_list] — tekst] 인격 목록
   źródło: MainUIText.json :: dataList[id=mainui_personality_list].content
   limit: do 120 znaków
   EN: Identity List
   PL: Lista Tożsamości
199. [Interfejs i ustawienia [mainui_acquired_reward] — tekst] 획득 보상
   źródło: MainUIText.json :: dataList[id=mainui_acquired_reward].content
   limit: do 120 znaków
   EN: Rewards Acquired
   PL: Zdobyte Nagrody
200. [Interfejs i ustawienia [mainui_dungeon_finished] — tekst] 탐사 종료
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_finished].content
   limit: do 120 znaków
   EN: Pause Exploration
   PL: Wstrzymaj Wyprawę
201. [Interfejs i ustawienia [mainui_category] — tekst] 범례
   źródło: MainUIText.json :: dataList[id=mainui_category].content
   limit: do 120 znaków
   EN: Legend
   PL: Legenda
202. [Interfejs i ustawienia [mainui_stats_hp] — tekst] 체력
   źródło: MainUIText.json :: dataList[id=mainui_stats_hp].content
   limit: do 120 znaków
   EN: HP
   PL: PŻ
203. [Interfejs i ustawienia [mainui_stats_speed] — tekst] 속도
   źródło: MainUIText.json :: dataList[id=mainui_stats_speed].content
   limit: do 120 znaków
   EN: SPD
   PL: SZYB.
204. [Interfejs i ustawienia [mainui_stats_defense] — tekst] 방어 레벨
   źródło: MainUIText.json :: dataList[id=mainui_stats_defense].content
   limit: do 120 znaków
   EN: Defense Level
   PL: Poziom Obrony
205. [Interfejs i ustawienia [mainui_upgrade] — tekst] 강화
   źródło: MainUIText.json :: dataList[id=mainui_upgrade].content
   limit: do 120 znaków
   EN: Power-up
   PL: Ulepsz
206. [Interfejs i ustawienia [mainui_mirror_select_ego] — tekst] E.G.O 선택으로 이동
   źródło: MainUIText.json :: dataList[id=mainui_mirror_select_ego].content
   limit: do 120 znaków
   EN: To E.G.O
   PL: Do E.G.O
207. [Interfejs i ustawienia [mainui_mirror_opening] — tekst] 개방 중
   źródło: MainUIText.json :: dataList[id=mainui_mirror_opening].content
   limit: do 120 znaków
   EN: Now Open
   PL: Otwarte
208. [Interfejs i ustawienia [mainui_simulation] — tekst] 시뮬레이션
   źródło: MainUIText.json :: dataList[id=mainui_simulation].content
   limit: do 120 znaków
   EN: Simulation
   PL: Symulacja
209. [Interfejs i ustawienia [mainui_untill] — tekst] 까지
   źródło: MainUIText.json :: dataList[id=mainui_untill].content
   limit: do 120 znaków
   EN: Expiry
   PL: Ważne do
210. [Interfejs i ustawienia [mainui_free] — tekst] 무료
   źródło: MainUIText.json :: dataList[id=mainui_free].content
   limit: do 120 znaków
   EN: Free
   PL: Darmowe
211. [Interfejs i ustawienia [mainui_paid] — tekst] 유료
   źródło: MainUIText.json :: dataList[id=mainui_paid].content
   limit: do 120 znaków
   EN: Paid
   PL: Płatne
212. [Interfejs i ustawienia [mainui_support] — tekst] 지원
   źródło: MainUIText.json :: dataList[id=mainui_support].content
   limit: do 120 znaków
   EN: Support
   PL: Wsparcie
213. [Interfejs i ustawienia [mainui_gacha_rateinfo] — tekst] 확률 상세보기
   źródło: MainUIText.json :: dataList[id=mainui_gacha_rateinfo].content
   limit: do 120 znaków
   EN: Probabilities
   PL: Szczegóły szans
214. [Interfejs i ustawienia [mainui_gacha_history] — tekst] 추출 이력
   źródło: MainUIText.json :: dataList[id=mainui_gacha_history].content
   limit: do 120 znaków
   EN: Extraction History
   PL: Historia Ekstrakcji
215. [Interfejs i ustawienia [mainui_gacha_daliynotice] — tekst] 매일 {0}시에 초기화
   źródło: MainUIText.json :: dataList[id=mainui_gacha_daliynotice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Resets each day at {0}:00
   PL: Reset codziennie o {0}:00
216. [Interfejs i ustawienia [mainui_gacha_alreadyusedgacha] — tekst] 금일 이용 가능 횟수 이용 완료
   źródło: MainUIText.json :: dataList[id=mainui_gacha_alreadyusedgacha].content
   limit: do 120 znaków
   EN: Daily Quota Exhausted
   PL: Wykorzystano dzienny limit
217. [Interfejs i ustawienia [mainui_gacha_extract1] — tekst] 1회 추출
   źródło: MainUIText.json :: dataList[id=mainui_gacha_extract1].content
   limit: do 120 znaków
   EN: Extract 1
   PL: Ekstrakcja ×1
218. [Interfejs i ustawienia [mainui_gacha_extract10] — tekst] 10회 추출
   źródło: MainUIText.json :: dataList[id=mainui_gacha_extract10].content
   limit: do 120 znaków
   EN: Extract 10
   PL: Ekstrakcja ×10
219. [Interfejs i ustawienia [mainui_open_battlepass] — tekst] 배틀 패스가 열렸습니다!
   źródło: MainUIText.json :: dataList[id=mainui_open_battlepass].content
   limit: do 120 znaków
   EN: The Battle Pass is unlocked!
   PL: Przepustka Bojowa odblokowana!
220. [Interfejs i ustawienia [mainui_grade_without_space] — tekst] {0}단계
   źródło: MainUIText.json :: dataList[id=mainui_grade_without_space].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Step {0}
   PL: Poz. {0}
221. [Interfejs i ustawienia [mainui_type] — tekst] 유형
   źródło: MainUIText.json :: dataList[id=mainui_type].content
   limit: do 120 znaków
   EN: Type
   PL: Typ
222. [Interfejs i ustawienia [mainui_level_unit] — tekst] {0}성
   źródło: MainUIText.json :: dataList[id=mainui_level_unit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}★
   PL: {0}★
223. [Interfejs i ustawienia [mainui_Change_lobby_illust] — tekst] 로비 일러스트 변경
   źródło: MainUIText.json :: dataList[id=mainui_Change_lobby_illust].content
   limit: do 120 znaków
   EN: Change Lobby Art
   PL: Zmień ilustrację lobby
224. [Interfejs i ustawienia [mainui_lobby_illust_acquisition_method] — tekst] 획득 조건
   źródło: MainUIText.json :: dataList[id=mainui_lobby_illust_acquisition_method].content
   limit: do 120 znaków
   EN: To Unlock:
   PL: Warunek odblokowania:
225. [Interfejs i ustawienia [mainui_networkingerror_content] — tekst] 네트워크가 불안정 합니다.\n 네트워크 상태를 확인해주세요
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The network is unstable.\nPlease check your Internet connection.
   PL: Połączenie sieciowe jest niestabilne.\nSprawdź połączenie z internetem.
226. [Interfejs i ustawienia [mainui_networkingerror_close] — tekst] 닫기
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_close].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Interfejs i ustawienia [mainui_networkingerror_retry] — tekst] 재시도
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_retry].content
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Interfejs i ustawienia [mainui_event_notice] — tekst] 이벤트 공지
   źródło: MainUIText.json :: dataList[id=mainui_event_notice].content
   limit: do 120 znaków
   EN: Event Notifs
   PL: Ogłoszenia Wydarzeń
229. [Interfejs i ustawienia [mainui_system_notice] — tekst] 시스템 공지
   źródło: MainUIText.json :: dataList[id=mainui_system_notice].content
   limit: do 120 znaków
   EN: System Notifs
   PL: Ogłoszenia Systemowe
230. [Interfejs i ustawienia [mainui_team] — tekst] 팀
   źródło: MainUIText.json :: dataList[id=mainui_team].content
   limit: do 120 znaków
   EN: Team
   PL: Drużyna
231. [Interfejs i ustawienia [mainui_cost] — tekst] 코스트
   źródło: MainUIText.json :: dataList[id=mainui_cost].content
   limit: do 120 znaków
   EN: Cost
   PL: Koszt
232. [Interfejs i ustawienia [mainui_dungeon_progress_rate] — tekst] 던전 진행도
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_progress_rate].content
   limit: do 120 znaków
   EN: Dungeon Progress
   PL: Postęp w Lochu
233. [Interfejs i ustawienia [mainui_guaranteed_reward] — tekst] 확정 보상
   źródło: MainUIText.json :: dataList[id=mainui_guaranteed_reward].content
   limit: do 120 znaków
   EN: Rewards
   PL: Nagrody Gwarantowane
234. [Interfejs i ustawienia [mainui_select_reward] — tekst] 선택 보상
   źródło: MainUIText.json :: dataList[id=mainui_select_reward].content
   limit: do 120 znaków
   EN: Optional Rewards
   PL: Nagrody do Wyboru
235. [Interfejs i ustawienia [mainui_battle_pass_exp] — tekst] 배틀 패스 경험치
   źródło: MainUIText.json :: dataList[id=mainui_battle_pass_exp].content
   limit: do 120 znaków
   EN: Battle Pass XP
   PL: PD Przepustki Bojowej
236. [Interfejs i ustawienia [mainui_enforce_ticket] — tekst] 강화 티켓
   źródło: MainUIText.json :: dataList[id=mainui_enforce_ticket].content
   limit: do 120 znaków
   EN: Upgrade Tickets
   PL: Bilety Treningowe
237. [Interfejs i ustawienia [mainui_reward_random_box] — tekst] 랜덤 자아 파편 상자
   źródło: MainUIText.json :: dataList[id=mainui_reward_random_box].content
   limit: do 120 znaków
   EN: Egoshard Crates
   PL: Losowe Skrzynki Odłamków E.G.O
238. [Interfejs i ustawienia [mainui_reward_select_box] — tekst] 선택 자아 파편 상자
   źródło: MainUIText.json :: dataList[id=mainui_reward_select_box].content
   limit: do 120 znaków
   EN: Nominable Egoshard Crates
   PL: Imienne Skrzynki Odłamków E.G.O
239. [Interfejs i ustawienia [mainui_manaUsage] — tekst] 정신 소모량
   źródło: MainUIText.json :: dataList[id=mainui_manaUsage].content
   limit: do 120 znaków
   EN: Sanity Cost
   PL: Koszt SP
240. [Interfejs i ustawienia [mainui_abnormality_analysis_level] — tekst] 환상 해석 단계
   źródło: MainUIText.json :: dataList[id=mainui_abnormality_analysis_level].content
   limit: do 120 znaków
   EN: Current Tier
   PL: Poziom Splotu Nici
241. [Interfejs i ustawienia [mainui_analysis] — tekst] 해석
   źródło: MainUIText.json :: dataList[id=mainui_analysis].content
   limit: do 120 znaków
   EN: Threadspin
   PL: Splot Nici
242. [Interfejs i ustawienia [mainui_abnormality_analysis] — tekst] 환상 해석
   źródło: MainUIText.json :: dataList[id=mainui_abnormality_analysis].content
   limit: do 120 znaków
   EN: Threadspinning
   PL: Splot Nici
243. [Interfejs i ustawienia [mainui_receive] — tekst] 수령
   źródło: MainUIText.json :: dataList[id=mainui_receive].content
   limit: do 120 znaków
   EN: Claim
   PL: Odbierz
244. [Interfejs i ustawienia [mainui_dungeon_finished_reward] — tekst] 탐사 종료 보상
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_finished_reward].content
   limit: do 120 znaków
   EN: Exploration Reward
   PL: Nagroda za Wyprawę
245. [Interfejs i ustawienia [mainui_passive] — tekst] 패시브
   źródło: MainUIText.json :: dataList[id=mainui_passive].content
   limit: do 120 znaków
   EN: Passives
   PL: Pasywki
246. [Interfejs i ustawienia [mainui_support_passive] — tekst] 서포트 패시브
   źródło: MainUIText.json :: dataList[id=mainui_support_passive].content
   limit: do 120 znaków
   EN: Support
   PL: Pasywka Wsparcia
247. [Interfejs i ustawienia [mainui_synchronization] — tekst] 동기화
   źródło: MainUIText.json :: dataList[id=mainui_synchronization].content
   limit: do 120 znaków
   EN: Uptie
   PL: Synchronizacja
248. [Interfejs i ustawienia [mainui_personality_synchronization_level] — tekst] 인격 동기화 레벨
   źródło: MainUIText.json :: dataList[id=mainui_personality_synchronization_level].content
   limit: do 120 znaków
   EN: Uptie Tier
   PL: Poziom Synchronizacji
249. [Interfejs i ustawienia [mainui_owned] — tekst] 보유
   źródło: MainUIText.json :: dataList[id=mainui_owned].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
250. [Interfejs i ustawienia [mainui_growth_level_limited] — tekst] Lv. {0} 이상 사용 불가
   źródło: MainUIText.json :: dataList[id=mainui_growth_level_limited].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cannot use at Lv. {0}+
   PL: Niedostępne od Poz. {0}+
251. [Interfejs i ustawienia [mainui_stats_attack] — tekst] 공격력
   źródło: MainUIText.json :: dataList[id=mainui_stats_attack].content
   limit: do 120 znaków
   EN: ATK
   PL: ATK
252. [Interfejs i ustawienia [mainui_mailbox_receive_all] — tekst] 일괄 수령
   źródło: MainUIText.json :: dataList[id=mainui_mailbox_receive_all].content
   limit: do 120 znaków
   EN: Claim All
   PL: Odbierz wszystko
253. [Interfejs i ustawienia [mainui_mailbox_receive_history] — tekst] 수령 이력
   źródło: MainUIText.json :: dataList[id=mainui_mailbox_receive_history].content
   limit: do 120 znaków
   EN: History
   PL: Historia odbioru
254. [Interfejs i ustawienia [mainui_remain_days] — tekst] {0}일 남음
   źródło: MainUIText.json :: dataList[id=mainui_remain_days].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} days left
   PL: Pozostało dni: {0}
255. [Interfejs i ustawienia [mainui_mail_remains_count] — tekst] 보관중인 우편
   źródło: MainUIText.json :: dataList[id=mainui_mail_remains_count].content
   limit: do 120 znaków
   EN: Inbox
   PL: Przechowywane listy
256. [Interfejs i ustawienia [mainui_mail_warning] — tekst] ※ 최대 100개 까지 보관이 가능하며, 기한이 지난 선물은 <color=#990000>삭제</color>됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_mail_warning].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>
   EN: ※ Maximum capacity is 100; expired mail will be <color=#990000>deleted</color>.
   PL: ※ Maksymalna pojemność to 100 listów; przeterminowane przesyłki zostają <color=#990000>usunięte</color>.
257. [Interfejs i ustawienia [mainui_mail_warning2] — tekst] ※ 우편함에서 수령한 아이템은 청약 철회가 제한될 수 있습니다.
   źródło: MainUIText.json :: dataList[id=mainui_mail_warning2].content
   limit: do 120 znaków
   EN: ※ Items claimed at the mailbox may be subject to cancellation restrictions.
   PL: ※ Przedmioty odebrane ze skrzynki pocztowej mogą nie podlegać zwrotowi.
258. [Interfejs i ustawienia [main_information] — tekst] 정보
   źródło: MainUIText.json :: dataList[id=main_information].content
   limit: do 120 znaków
   EN: Info
   PL: Informacje
259. [Interfejs i ustawienia [main_until] — tekst] 까지
   źródło: MainUIText.json :: dataList[id=main_until].content
   (powtórzenie elementu 209 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
260. [Interfejs i ustawienia [mainui_synchronization_grade] — tekst] 동기화 단계
   źródło: MainUIText.json :: dataList[id=mainui_synchronization_grade].content
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Interfejs i ustawienia [mainui_organization] — tekst] 편성
   źródło: MainUIText.json :: dataList[id=mainui_organization].content
   limit: do 120 znaków
   EN: TEAMS
   PL: SKŁADY
262. [Interfejs i ustawienia [story_ui_log_popup] — tekst] 로그
   źródło: MainUIText.json :: dataList[id=story_ui_log_popup].content
   limit: do 120 znaków
   EN: Log
   PL: Dziennik
263. [Interfejs i ustawienia [mail_box_attachments] — tekst] 우편 내용물
   źródło: MainUIText.json :: dataList[id=mail_box_attachments].content
   limit: do 120 znaków
   EN: Content
   PL: Zawartość listu
264. [Interfejs i ustawienia [mail_box_unseal_result] — tekst] 우편 보상
   źródło: MainUIText.json :: dataList[id=mail_box_unseal_result].content
   limit: do 120 znaków
   EN: Parcel Received
   PL: Odebrano przesyłkę
265. [Interfejs i ustawienia [item_use_result] — tekst] 아이템 사용 결과
   źródło: MainUIText.json :: dataList[id=item_use_result].content
   limit: do 120 znaków
   EN: Item Used
   PL: Wynik użycia przedmiotu
266. [Interfejs i ustawienia [giving_up_story_dungeon_title] — tekst] 스토리 던전 포기
   źródło: MainUIText.json :: dataList[id=giving_up_story_dungeon_title].content
   limit: do 120 znaków
   EN: Forfeit Story Dungeon
   PL: Porzuć Loch Fabularny
267. [Interfejs i ustawienia [giving_up_story_dungeon_content] — tekst] 현재 {0}장 스토리 던전을 진행 중입니다.\n진행을 포기하고 새로운 던전에 도전하시겠습니까?
   źródło: MainUIText.json :: dataList[id=giving_up_story_dungeon_content].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: You’re currently exploring Episode {0}’s Story Dungeon.\nForfeit your progress and enter a new dungeon?
   PL: Trwa eksploracja Lochu Fabularnego Rozdziału {0}.\nPorzucić dotychczasowy postęp i rozpocząć nowy loch?
268. [Interfejs i ustawienia [mainui_all] — tekst] 전체
   źródło: MainUIText.json :: dataList[id=mainui_all].content
   limit: do 120 znaków
   EN: All
   PL: Wszystko
269. [Interfejs i ustawienia [mainui_opened] — tekst] 개방
   źródło: MainUIText.json :: dataList[id=mainui_opened].content
   limit: do 120 znaków
   EN: Open
   PL: Odblokowane
270. [Interfejs i ustawienia [mainui_not_opened] — tekst] 미개방
   źródło: MainUIText.json :: dataList[id=mainui_not_opened].content
   limit: do 120 znaków
   EN: Locked
   PL: Zablokowane
271. [Interfejs i ustawienia [mainui_buy] — tekst] 구매
   źródło: MainUIText.json :: dataList[id=mainui_buy].content
   limit: do 120 znaków
   EN: Confirm
   PL: Kup
272. [Interfejs i ustawienia [mainui_use] — tekst] 사용
   źródło: MainUIText.json :: dataList[id=mainui_use].content
   limit: do 120 znaków
   EN: Use
   PL: Użyj
273. [Interfejs i ustawienia [mainui_consume] — tekst] 소모
   źródło: MainUIText.json :: dataList[id=mainui_consume].content
   limit: do 120 znaków
   EN: Consumable
   PL: Zużywalne
274. [Interfejs i ustawienia [mainui_currencies] — tekst] 재화
   źródło: MainUIText.json :: dataList[id=mainui_currencies].content
   limit: do 120 znaków
   EN: Currency
   PL: Waluty
275. [Interfejs i ustawienia [mainui_inventory] — tekst] 인벤토리
   źródło: MainUIText.json :: dataList[id=mainui_inventory].content
   limit: do 120 znaków
   EN: Inventory
   PL: Ekwipunek
276. [Interfejs i ustawienia [mainui_awaken_requirement_amount] — tekst] 필요 재화 수량
   źródło: MainUIText.json :: dataList[id=mainui_awaken_requirement_amount].content
   limit: do 120 znaków
   EN: Currency Req.
   PL: Wymagane zasoby
277. [Interfejs i ustawienia [mainui_passive_skill_addition] — tekst] 패시브 스킬 추가
   źródło: MainUIText.json :: dataList[id=mainui_passive_skill_addition].content
   limit: do 120 znaków
   EN: Passives Unlocked
   PL: Odblokowano pasywkę
278. [Interfejs i ustawienia [mainui_synergy_addition] — tekst] 시너지 획득
   źródło: MainUIText.json :: dataList[id=mainui_synergy_addition].content
   limit: do 120 znaków
   EN: Synergy Unlocked
   PL: Odblokowano synergię
279. [Interfejs i ustawienia [mainui_ego_awaken_skill_reinforcement] — tekst] E.G.O 각성 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_skill_reinforcement].content
   limit: do 120 znaków
   EN: E.G.O Awakening Upgraded
   PL: Ulepszono Przebudzenie E.G.O
280. [Interfejs i ustawienia [mainui_ego_erosion_skill_reinforcement] — tekst] E.G.O 침식 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_erosion_skill_reinforcement].content
   limit: do 120 znaków
   EN: E.G.O Corrosion Upgraded
   PL: Ulepszono Korozję E.G.O
281. [Interfejs i ustawienia [mainui_lack_of_material_amount] — tekst] 끈이 부족합니다.
   źródło: MainUIText.json :: dataList[id=mainui_lack_of_material_amount].content
   limit: do 120 znaków
   EN: Not enough Thread.
   PL: Za mało Nici.
282. [Interfejs i ustawienia [mainui_move] — tekst] 이동
   źródło: MainUIText.json :: dataList[id=mainui_move].content
   limit: do 120 znaków
   EN: Go
   PL: Przejdź
283. [Interfejs i ustawienia [mainui_move_to_twine_store] — tekst] 파편::끈 교환기 이동
   źródło: MainUIText.json :: dataList[id=mainui_move_to_twine_store].content
   limit: do 120 znaków
   EN: Shard::Thread Exchange
   PL: Wymiana Odłamki::Nić
284. [Interfejs i ustawienia [mainui_move_to_twine_store_question] — tekst] 끈이 부족합니다.\n파편::끈 교환기로 이동하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_move_to_twine_store_question].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Insufficient Thread.\nGo to the Shard::Thread Exchange?
   PL: Za mało Nici.\nPrzejść do Wymiany Odłamki::Nić?
285. [Interfejs i ustawienia [mainui_confirm_of_purchased_twine] — tekst] 끈 {0}개를 구입하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_confirm_of_purchased_twine].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Convert to {0} Thread?
   PL: Wymienić na {0} Nici?
286. [Interfejs i ustawienia [mainui_result_of_purchased_twine] — tekst] 끈 {0}개를 구입하였습니다.
   źródło: MainUIText.json :: dataList[id=mainui_result_of_purchased_twine].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Acquired {0} Thread.
   PL: Zdobyto {0} Nici.
287. [Interfejs i ustawienia [mainui_personality_awaken_completion] — tekst] 인격 동기화 완료
   źródło: MainUIText.json :: dataList[id=mainui_personality_awaken_completion].content
   limit: do 120 znaków
   EN: Identity Uptied
   PL: Synchronizacja Ukończona
288. [Interfejs i ustawienia [mainui_ego_awaken_completion] — tekst] 환상 해석 완료
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_completion].content
   limit: do 120 znaków
   EN: E.G.O Threadspun
   PL: Splot Nici Ukończony
289. [Interfejs i ustawienia [mainui_new_skill_acquisition] — tekst] 신규 스킬 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_skill_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Skill: [{0}]
   PL: Nowa umiejętność: [{0}]
290. [Interfejs i ustawienia [mainui_new_passive_skill_acquisition] — tekst] 신규 패시브 스킬 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_passive_skill_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Passive: [{0}]
   PL: Nowa pasywka: [{0}]
291. [Interfejs i ustawienia [mainui_new_synergy_acquisition] — tekst] 시너지 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_synergy_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Synergy: [{0}]
   PL: Nowa synergia: [{0}]
292. [Interfejs i ustawienia [mainui_new_battle_passive_acquisition] — tekst] 신규 전투 패시브 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_battle_passive_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Combat Passive: [{0}]
   PL: Nowa pasywka bojowa: [{0}]
293. [Interfejs i ustawienia [mainui_new_support_passive_acquisition] — tekst] 신규 서포트 패시브 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_support_passive_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Support Passive: [{0}]
   PL: Nowa pasywka wsparcia: [{0}]
294. [Interfejs i ustawienia [mainui_skill_reinforcement] — tekst] 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_skill_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Enhanced: [{0}]
   PL: Ulepszono umiejętność: [{0}]
295. [Interfejs i ustawienia [mainui_unlock_personality_story] — tekst] [{0}]의 이야기 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_personality_story].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Story of [{0}] Unlocked
   PL: Odblokowano historię: [{0}]
296. [Interfejs i ustawienia [mainui_ego_awaken_skill_name_reinforcement] — tekst] E.G.O 각성 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_skill_name_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Awakening [{0}] Upgraded
   PL: Ulepszono Przebudzenie E.G.O: [{0}]
297. [Interfejs i ustawienia [mainui_ego_erosion_skill_name_reinforcement] — tekst] E.G.O 침식 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_erosion_skill_name_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Corrosion [{0}] Upgraded
   PL: Ulepszono Korozję E.G.O: [{0}]
298. [Interfejs i ustawienia [mainui_specific_level_achievement] — tekst] LV{0} 달성
   źródło: MainUIText.json :: dataList[id=mainui_specific_level_achievement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reach Lv. {0}
   PL: Osiągnij Poz. {0}
299. [Interfejs i ustawienia [mainui_personality_awaken_level_up_condition] — tekst] 동기화 {0}단계 조건
   źródło: MainUIText.json :: dataList[id=mainui_personality_awaken_level_up_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie Tier {0} Requirements
   PL: Wymagania Synchronizacji Poz. {0}
300. [Interfejs i ustawienia [mainui_battle_passsive_addition] — tekst] 전투 패시브 추가
   źródło: MainUIText.json :: dataList[id=mainui_battle_passsive_addition].content
   limit: do 120 znaków
   EN: Combat Passives Unlocked
   PL: Odblokowano pasywkę bojową
301. [Interfejs i ustawienia [mainui_support_passsive_addition] — tekst] 서포트 패시브 추가
   źródło: MainUIText.json :: dataList[id=mainui_support_passsive_addition].content
   limit: do 120 znaków
   EN: Support Passives Unlocked
   PL: Odblokowano pasywkę wsparcia
302. [Interfejs i ustawienia [mainui_check_purchase] — tekst] 구매 확인
   źródło: MainUIText.json :: dataList[id=mainui_check_purchase].content
   limit: do 120 znaków
   EN: Confirm Purchase
   PL: Potwierdzenie zakupu
303. [Interfejs i ustawienia [mainui_acquire_banner] — tekst] 배너 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquire_banner].content
   limit: do 120 znaków
   EN: Banner Acquired
   PL: Zdobyto Baner
304. [Interfejs i ustawienia [mainui_purchase_complete] — tekst] 구매 완료
   źródło: MainUIText.json :: dataList[id=mainui_purchase_complete].content
   limit: do 120 znaków
   EN: Purchased
   PL: Zakupiono
305. [Interfejs i ustawienia [mainui_activation] — tekst] 활성화
   źródło: MainUIText.json :: dataList[id=mainui_activation].content
   limit: do 120 znaków
   EN: ACTIVATED
   PL: AKTYWNE
306. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin] — tekst] 엔케팔린이 부족합니다.\n엔케팔린 충전 창으로 이동하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Insufficient Enkephalin.\nWould you like to recharge your Enkephalin?
   PL: Za mało Enkefaliny.\nPrzejść do okna ładowania Enkefaliny?
307. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin_box] — tekst] 엔케팔린 박스가 부족합니다.\n엔케팔린 박스를 구매하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin_box].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You don’t have enough Enkephalin Boxes.\nWould you like to go purchase some?
   PL: Za mało Skrzynek Enkefaliny.\nCzy chcesz przejść do ich zakupu?
308. [Interfejs i ustawienia [mainui_rewatching-stage-story] — tekst] 스토리 다시보기
   źródło: MainUIText.json :: dataList[id=mainui_rewatching-stage-story].content
   limit: do 120 znaków
   EN: Rewatch Story
   PL: Obejrzyj ponownie
309. [Interfejs i ustawienia [mainui_before_battle] — tekst] 전투 전
   źródło: MainUIText.json :: dataList[id=mainui_before_battle].content
   limit: do 120 znaków
   EN: Pre-battle
   PL: Przed walką
310. [Interfejs i ustawienia [mainui_after_battle] — tekst] 전투 후
   źródło: MainUIText.json :: dataList[id=mainui_after_battle].content
   limit: do 120 znaków
   EN: Post-battle
   PL: Po walce
311. [Interfejs i ustawienia [mainui_story] — tekst] 스토리
   źródło: MainUIText.json :: dataList[id=mainui_story].content
   limit: do 120 znaków
   EN: Story
   PL: Fabuła
312. [Interfejs i ustawienia [Get_Reward] — tekst] 보상 획득
   źródło: MainUIText.json :: dataList[id=Get_Reward].content
   limit: do 120 znaków
   EN: Rewards Earned
   PL: Zdobyte Nagrody
313. [Interfejs i ustawienia [mainui_user_exp] — tekst] 관리자 경험치
   źródło: MainUIText.json :: dataList[id=mainui_user_exp].content
   limit: do 120 znaków
   EN: Manager EXP
   PL: PD Kierownika
314. [Interfejs i ustawienia [mainui_chapter_progress] — tekst] 챕터 진행도
   źródło: MainUIText.json :: dataList[id=mainui_chapter_progress].content
   limit: do 120 znaków
   EN: Progress
   PL: Postęp rozdziału
315. [Interfejs i ustawienia [mainui_ex_clear_progress] — tekst] EX-클리어
   źródło: MainUIText.json :: dataList[id=mainui_ex_clear_progress].content
   limit: do 120 znaków
   EN: EX Cleared
   PL: Ukończono EX
316. [Interfejs i ustawienia [mainui_notice_spend_free_lunacy_first] — tekst] ※무료 광기부터 먼저 사용됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_notice_spend_free_lunacy_first].content
   limit: do 120 znaków
   EN: ※ Free Lunacy is used first.
   PL: ※ W pierwszej kolejności zużywane jest Darmowe Szaleństwo.
317. [Interfejs i ustawienia [mainui_notice_require_lunacy] — tekst] ※광기가 부족합니다.
   źródło: MainUIText.json :: dataList[id=mainui_notice_require_lunacy].content
   limit: do 120 znaków
   EN: ※ Not enough Lunacy.
   PL: ※ Za mało Szaleństwa.
318. [Interfejs i ustawienia [mainui_progress_of_spend] — tekst] {0}을(를) 소비하여 {1}을(를) 진행합니다.
   źródło: MainUIText.json :: dataList[id=mainui_progress_of_spend].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Spend {0} to proceed with {1}?
   PL: Zużyć {0}, aby wykonać: {1}?
319. [Interfejs i ustawienia [game_setting] — tekst] 게임 설정
   źródło: MainUIText.json :: dataList[id=game_setting].content
   limit: do 120 znaków
   EN: Config
   PL: Ustawienia gry
320. [Interfejs i ustawienia [level] — tekst] 레벨
   źródło: MainUIText.json :: dataList[id=level].content
   limit: do 120 znaków
   EN: Level
   PL: Poziom
321. [Interfejs i ustawienia [name] — tekst] 이름
   źródło: MainUIText.json :: dataList[id=name].content
   limit: do 120 znaków
   EN: Name
   PL: Nazwa
322. [Interfejs i ustawienia [order_of_acquisition] — tekst] 획득 순
   źródło: MainUIText.json :: dataList[id=order_of_acquisition].content
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Interfejs i ustawienia [tolerance] — tekst] 내성
   źródło: MainUIText.json :: dataList[id=tolerance].content
   limit: do 120 znaków
   EN: Resist
   PL: Odporn.
324. [Interfejs i ustawienia [outstanding_staff] — tekst] 우수 사원
   źródło: MainUIText.json :: dataList[id=outstanding_staff].content
   limit: do 120 znaków
   EN: Most Valued Employee
   PL: Wzorowy Pracownik
325. [Interfejs i ustawienia [total_damage_contribution] — tekst] 총 대미지 기여량
   źródło: MainUIText.json :: dataList[id=total_damage_contribution].content
   limit: do 120 znaków
   EN: Damage Contributed
   PL: Udział w obrażeniach
326. [Interfejs i ustawienia [deal_damage] — tekst] 가한 피해량
   źródło: MainUIText.json :: dataList[id=deal_damage].content
   limit: do 120 znaków
   EN: Dealt
   PL: Zadane
327. [Interfejs i ustawienia [taken_damage] — tekst] 받은 피해량
   źródło: MainUIText.json :: dataList[id=taken_damage].content
   limit: do 120 znaków
   EN: Taken
   PL: Otrzymane
328. [Interfejs i ustawienia [user_level_up_notice] — tekst] 관리자 레벨이 상승했습니다.
   źródło: MainUIText.json :: dataList[id=user_level_up_notice].content
   limit: do 120 znaków
   EN: Manager Level Increased!
   PL: Poziom Kierownika wzrósł!
329. [Interfejs i ustawienia [increase_maxium_enkephalin] — tekst] 엔케팔린 최대치 상승
   źródło: MainUIText.json :: dataList[id=increase_maxium_enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin Capacity Up!
   PL: Zwiększono limit Enkefaliny!
330. [Interfejs i ustawienia [recharge_enkephalin_notice] — tekst] 엔케팔린이 충전되었습니다.
   źródło: MainUIText.json :: dataList[id=recharge_enkephalin_notice].content
   limit: do 120 znaków
   EN: Enkephalin has been refilled.
   PL: Enkefalina została uzupełniona.
331. [Interfejs i ustawienia [gacha_extract_multiple] — tekst] {0}회 추출
   źródło: MainUIText.json :: dataList[id=gacha_extract_multiple].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Extract {0}
   PL: Ekstrakcja ×{0}
332. [Interfejs i ustawienia [number_of_times] — tekst] 회
   źródło: MainUIText.json :: dataList[id=number_of_times].content
   limit: do 120 znaków
   EN: Time(s)
   PL: raz(y)
333. [Interfejs i ustawienia [number_of_remain_extract_times] — tekst] 남은 추출 횟수
   źródło: MainUIText.json :: dataList[id=number_of_remain_extract_times].content
   limit: do 120 znaków
   EN: Extractions Remaining
   PL: Pozostałe Ekstrakcje
334. [Interfejs i ustawienia [notice_of_remain_extract_chance] — tekst] {0}회 이내 3성 인격 또는 E.G.O 확정 등장
   źródło: MainUIText.json :: dataList[id=notice_of_remain_extract_chance].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 3★ Identity or E.G.O assured in {0} Extractions
   PL: Gwarantowana Tożsamość 3★ lub E.G.O w ciągu {0} Ekstrakcji
335. [Interfejs i ustawienia [mainui_settings] — tekst] 설정
   źródło: MainUIText.json :: dataList[id=mainui_settings].content
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
336. [Interfejs i ustawienia [mainui_environment_settings] — tekst] 환경 설정
   źródło: MainUIText.json :: dataList[id=mainui_environment_settings].content
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
337. [Interfejs i ustawienia [mainui_back] — tekst] 돌아가기
   źródło: MainUIText.json :: dataList[id=mainui_back].content
   limit: do 120 znaków
   EN: Return
   PL: Wróć
338. [Interfejs i ustawienia [mainui_quit_game] — tekst] 게임 종료
   źródło: MainUIText.json :: dataList[id=mainui_quit_game].content
   limit: do 120 znaków
   EN: Quit Game
   PL: Wyjdź z gry
339. [Interfejs i ustawienia [mainui_acquisition] — tekst] 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquisition].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
340. [Interfejs i ustawienia [mainui_not_acquisition] — tekst] 미획득
   źródło: MainUIText.json :: dataList[id=mainui_not_acquisition].content
   limit: do 120 znaków
   EN: Unowned
   PL: Nieposiadane
341. [Interfejs i ustawienia [mainui_no_record] — tekst] 획득 기록 없음
   źródło: MainUIText.json :: dataList[id=mainui_no_record].content
   limit: do 120 znaków
   EN: No Acquisition Records
   PL: Brak historii zdobycia
342. [Interfejs i ustawienia [resume] — tekst] 재개
   źródło: MainUIText.json :: dataList[id=resume].content
   limit: do 120 znaków
   EN: Resume
   PL: Wznów
343. [Interfejs i ustawienia [mainui_entering] — tekst] 입장하기
   źródło: MainUIText.json :: dataList[id=mainui_entering].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
344. [Interfejs i ustawienia [mainui_open_after_clear] — tekst] {0}장 클리어 후 개방
   źródło: MainUIText.json :: dataList[id=mainui_open_after_clear].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Ch. {0} to Unlock
   PL: Odblokowanie po Rozdz. {0}
345. [Interfejs i ustawienia [mainui_organization_sharp] — tekst] 편성 #{0}
   źródło: MainUIText.json :: dataList[id=mainui_organization_sharp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Team #{0}
   PL: Skład #{0}
346. [Interfejs i ustawienia [mainui_participant_count] — tekst] 편성 편집
   źródło: MainUIText.json :: dataList[id=mainui_participant_count].content
   limit: do 120 znaków
   EN: Edit Team
   PL: Edytuj skład
347. [Interfejs i ustawienia [mainui_edit] — tekst] 편집
   źródło: MainUIText.json :: dataList[id=mainui_edit].content
   limit: do 120 znaków
   EN: Edit
   PL: Edytuj
348. [Interfejs i ustawienia [mainui_unlock_condition_by_personality_awaken_level] — tekst] 동기화 {0}단계 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_condition_by_personality_awaken_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Unlocked at Tier {0}
   PL: Odblokowanie na {0}. poz. Synchronizacji
349. [Interfejs i ustawienia [skill_growth_value] — tekst] 성장계수
   źródło: MainUIText.json :: dataList[id=skill_growth_value].content
   limit: do 120 znaków
   EN: Growth
   PL: Przyrost
350. [Interfejs i ustawienia [gacha_history_notice] — tekst] ※지난 {0}일간 이력이 최대 {1}건 표기됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_history_notice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: ※ Up to {1} cases over the last {0} days are displayed.
   PL: ※ Wyświetlane jest maks. {1} wpisów z ostatnich {0} dni.
351. [Interfejs i ustawienia [gacha_history_empty] — tekst] 추출 이력이 없습니다.
   źródło: MainUIText.json :: dataList[id=gacha_history_empty].content
   limit: do 120 znaków
   EN: No extraction record to display.
   PL: Brak historii Ekstrakcji do wyświetlenia.
352. [Interfejs i ustawienia [own] — tekst] 소지
   źródło: MainUIText.json :: dataList[id=own].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
353. [Interfejs i ustawienia [gacha_category] — tekst] 추출 종류
   źródło: MainUIText.json :: dataList[id=gacha_category].content
   limit: do 120 znaków
   EN: Category
   PL: Rodzaj Ekstrakcji
354. [Interfejs i ustawienia [gacha_time] — tekst] 추출 일시
   źródło: MainUIText.json :: dataList[id=gacha_time].content
   limit: do 120 znaków
   EN: Date
   PL: Data
355. [Interfejs i ustawienia [used_currencies] — tekst] 사용 재화
   źródło: MainUIText.json :: dataList[id=used_currencies].content
   limit: do 120 znaków
   EN: Currency Used
   PL: Użyta waluta
356. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin_module] — tekst] 엔케팔린 모듈이 부족합니다.\n엔케팔린 모듈을 제작하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin_module].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You don’t have enough Enkephalin Modules.\nWould you like to go assemble some?
   PL: Za mało Modułów Enkefaliny.\nCzy chcesz przejść do ich wytworzenia?
357. [Interfejs i ustawienia [list] — tekst] 목록
   źródło: MainUIText.json :: dataList[id=list].content
   limit: do 120 znaków
   EN: List
   PL: Lista
358. [Interfejs i ustawienia [rank] — tekst] 등급
   źródło: MainUIText.json :: dataList[id=rank].content
   limit: do 120 znaków
   EN: Rarity
   PL: Rzadkość
359. [Interfejs i ustawienia [probability] — tekst] 확률
   źródło: MainUIText.json :: dataList[id=probability].content
   limit: do 120 znaków
   EN: Odds
   PL: Szansa
360. [Interfejs i ustawienia [gacha_rate_label] — tekst] 추출 확률 안내
   źródło: MainUIText.json :: dataList[id=gacha_rate_label].content
   limit: do 120 znaków
   EN: Extraction Probabilities
   PL: Szanse w Ekstrakcji
361. [Interfejs i ustawienia [gacha_rate_title_ten1] — tekst] [10회 추출 (1~9번째 추출)]: [1회 추출]과 동일
   źródło: MainUIText.json :: dataList[id=gacha_rate_title_ten1].content
   limit: do 120 znaków
   EN: [10 Extractions (1st-9th)]: Same rates as [1 Extraction]
   PL: [Ekstrakcja ×10 ( próby 1–9 )]: takie same szanse jak [Ekstrakcja ×1]
362. [Interfejs i ustawienia [gacha_rate_title_ten2] — tekst] [10회 추출 (10번째 추출)]
   źródło: MainUIText.json :: dataList[id=gacha_rate_title_ten2].content
   limit: do 120 znaków
   EN: [10 Extractions (10th)]
   PL: [Ekstrakcja ×10 ( 10. próba )]
363. [Interfejs i ustawienia [gacha_rate_info_intro1] — tekst] 「한국게임산업협회의 자율 규제」에 따라 확률형 아이템의 상세 확률을 안내드립니다.\n\n개별 등장 확률은 소수점 5번째 자리에서 반올림한 수치이며, 실제 합산 확률은 100%에 맞추어 적용됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In compliance with the 「Voluntary Restraint Guidelines of Korea Association of Game Industry」, detailed rates for chance-based items are disclosed here.\n\nIndividual rates are rounded up from the fifth digit after the decimal point. The actual sum is applied as 100%.
   PL: Zgodnie z zasadami przejrzystości publikujemy szczegółowe prawdopodobieństwa przedmiotów losowych.\n\nPoszczególne wartości zaokrąglono na piątym miejscu po przecinku, a rzeczywista suma prawdopodobieństw wynosi 100%.
364. [Interfejs i ustawienia [gacha_rate_info_intro2] — tekst] 10회 추출을 진행할 경우에는 2성 이상의 인격 1명을 확정으로 획득합니다.\n\n이에 따라 10번째 추출의 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro2].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In [10 Extractions], at least 1 Identity with a rarity of 2★ or higher will be extracted.\n\nThe table for the 10th Extraction is as follows:
   PL: W [Ekstrakcji ×10] gwarantowane jest zdobycie co najmniej 1 Tożsamości o rzadkości 2★ lub wyższej.\n\nSzanse dla 10. próby przedstawiają się następująco:
365. [Interfejs i ustawienia [gacha_rate_info_ego1] — tekst] 상단에 있는 추출 확률에 따라 하단에 명시된 목록에 있는 인격과 E.G.O를 획득할 수 있습니다.\n\n획득할 수 있는 인격과 E.G.O는 특정 시즌에 따라 변경될 수 있으며, 이러한 경우에는 변경 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_ego1].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Below is the list of Identities and E.G.O you can obtain following the aforementioned rates.\n\nThe list may change in certain seasons; upcoming changes to the reward tables will be announced in advance.
   PL: Zgodnie z powyższymi szansami można zdobyć Tożsamości oraz E.G.O z listy poniżej.\n\nDostępna pula może ulec zmianie wraz z sezonem, o czym poinformujemy z wyprzedzeniem w ogłoszeniach.
366. [Interfejs i ustawienia [gacha_rate_info_ego2] — tekst] <b>추출 진행 시 E.G.O는 비복원 추출로 진행되며, 추출이나 자판기 또는 보상을 수령하여 획득한 E.G.O는 추출을 통해 획득할 수 있는 목록에서 제외됩니다.</b>\n\n획득할 수 있는 목록에 E.G.O가 존재한다면 추출을 통해 E.G.O를 획득할 확률은 변동되지 않습니다. 이에 따라 E.G.O를 획득할수록 E.G.O의 개별 획득 확률은 증가합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_ego2].content
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <b>, </b>, \n
   EN: <b>E.G.O is extracted non-repetitively; E.G.O acquired through any means, including Extraction, Dispenser, and redemption from the mailbox, will be excluded from the Extraction table.</b>\n\nAs long as there is E.G.O remaining in the table of possible results, the chance of extracting E.G.O in Extraction does not change. Therefore, the chance of acquiring specific E.G.O will increase as more extractions are performed.
   PL: <b>E.G.O losowane są bez powtórzeń — każde E.G.O zdobyte w Ekstrakcji, Automacie lub ze skrzynki pocztowej zostaje wykluczone z puli Ekstrakcji.</b>\n\nDopóki w puli pozostaje co najmniej jedno nieposiadane E.G.O, łączna szansa wylosowania kategorii E.G.O nie zmienia się, dzięki czemu rośnie szansa zdobycia pozostałych E.G.O.
367. [Interfejs i ustawienia [gacha_rate_info_complete1] — tekst] 목록 내에 있는 모든 E.G.O를 획득하여 더 이상 목록에 E.G.O가 존재하지 않게 된다면 1회 추출 시와 10회 추출 시의 등장 확률은 다음과 같이 변경됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete1].content
   limit: do 230 znaków
   EN: If there is no E.G.O remaining in the table due to the user acquiring all of them, the rates for [1 Extraction] and [10 Extraction] will change accordingly to the following:
   PL: Gdy gracz zdobędzie wszystkie E.G.O dostępne w danej puli, szanse dla [Ekstrakcji ×1] oraz [Ekstrakcji ×10] zmieniają się następująco:
368. [Interfejs i ustawienia [gacha_rate_info_complete2] — tekst] 특정 추출 인격 또는 E.G.O가 등장할 경우에는 특정 추출 확률이 적용되어 추출 확률이 증가합니다.\n\n특정 추출 확률 인격이 등장할 경우, 해당 특정 추출 인격과 동일한 등급 인격이 등장할 확률의 50%를 동일한 단계의 특정 추출 인격 수만큼 균등하게 분배합니다.\n\n특정 추출 대상이 아닌 인격도 마찬가지로 등장할 확률의 50%을 특정 추출 대상이 아닌 인격 수만큼 균등하게 분배합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete2].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Target Extractions, certain Identities and E.G.O have higher extraction rates.\n\nTarget Identities account for 50% of the probabilities for their respective rarities; the rates are evenly shared among them.\n\nThe other 50% of probabilities are evenly distributed between the non-targeted Identities in the table.
   PL: W Ekstrakcjach Celowanych wybrane Tożsamości oraz E.G.O mają zwiększoną szansę pojawienia się.\n\nWyróżnione Tożsamości odpowiadają łącznie za 50% szansy danej rzadkości (dzielonej równo między nie).\n\nPozostałe 50% szansy danej rzadkości dzielone jest równo między wszystkie niewyróżnione Tożsamości w puli.
369. [Interfejs i ustawienia [gacha_rate_info_complete3] — tekst] 위 내용은 특정 추출 E.G.O의 경우에도 동일하게 동작합니다.\n\n특정 추출 확률이 적용되어도 각 추출의 경우에 대한 등장 확률은 변동되지 않습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete3].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The same applies to Target E.G.O.\n\nChanges in probabilities for Target Extractions do not affect the chances of items of certain types and rarities appearing.
   PL: Ta sama zasada dotyczy wyróżnionych E.G.O.\n\nZastosowanie szans Ekstrakcji Celowanej nie zmienia ogólnego prawdopodobieństwa poszczególnych kategorii i rzadkości.
370. [Interfejs i ustawienia [gacha_rate_info_piece1] — tekst] ★ 자아 파편\n이미 보유한 인격 또는 E.G.O를 중복하여 획득할 경우에는 분류와 단계에 따라 각 캐릭터의 자아 파편으로 전환되어 획득하게 됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ★ Egoshards\nWhen you extract an Identity or E.G.O you already own, you will get Egoshards of the character, its quantity depending on the item’s type and rarity.
   PL: ★ Odłamki E.G.O\nWylosowanie duplikatu posiadanej już Tożsamości zostaje zamienione na Odłamki E.G.O danego Grzesznika w liczbie zależnej od rzadkości.
371. [Interfejs i ustawienia [gacha_rate_info_piece2] — tekst] 획득한 자아 파편은 미리 공지한 기간 동안 사용할 수 있으며, 보유한 자아 파편의 50%만큼 다음 시즌으로 이월됩니다.\n\n이월되지 않은 자아 파편은 끈으로 전환됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece2].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Egoshards can only be used for a set period. When the expiration date arrives, 50% of the Egoshards in possession are carried over to the next season.\n\nThe remaining Egoshards are converted to Thread.
   PL: Zdobyte Odłamki E.G.O ważne są przez ogłoszony okres sezonu; wraz z końcem sezonu 50% posiadanych Odłamków przechodzi na kolejny sezon.\n\nNieprzeniesiona połowa zostaje zamieniona na Nić.
372. [Interfejs i ustawienia [gacha_rate_info_piece3] — tekst] 위 내용은 자아 파편 상자의 경우에도 동일하게 동작합니다.\n\n이러한 경우에는 다음 시즌이 시작되어 자아 파편과 자아 파편 상자가 이월되기 전에 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece3].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The same applies to Egoshard Crates.\n\nPlayers will be notified of the upcoming season change and expiration of Egoshards and Egoshard Crates sometime before the expiration date.
   PL: Ta sama zasada dotyczy Skrzynek Odłamków E.G.O.\n\nO nadchodzącej zmianie sezonu i przeniesieniu Odłamków oraz Skrzynek poinformujemy z wyprzedzeniem w ogłoszeniach.
373. [Interfejs i ustawienia [personality_preview_notice] — tekst] 본 화면에는 인격의 최대 레벨, 동기화 단계가 표시됩니다.
   źródło: MainUIText.json :: dataList[id=personality_preview_notice].content
   limit: do 120 znaków
   EN: The Identity’s stats at max level and Uptie tier are displayed here.
   PL: Na tym ekranie wyświetlane są maksymalny poziom oraz Synchronizacja Tożsamości.
374. [Interfejs i ustawienia [ego_preview_notice] — tekst] 본 화면에는 E.G.O의 최대 환상 해석 단계가 표시됩니다.
   źródło: MainUIText.json :: dataList[id=ego_preview_notice].content
   limit: do 120 znaków
   EN: The E.G.O is displayed at its max tier here.
   PL: Na tym ekranie wyświetlany jest maksymalny poziom Splotu Nici E.G.O.
375. [Interfejs i ustawienia [season_1] — tekst] 시즌 1
   źródło: MainUIText.json :: dataList[id=season_1].content
   limit: do 120 znaków
   EN: Season 1
   PL: Sezon 1
376. [Interfejs i ustawienia [commonly] — tekst] 통상
   źródło: MainUIText.json :: dataList[id=commonly].content
   limit: do 120 znaków
   EN: Regular
   PL: Standardowe
377. [Interfejs i ustawienia [notice_external_website] — tekst] 외부 웹사이트로 이동합니다.
   źródło: MainUIText.json :: dataList[id=notice_external_website].content
   limit: do 120 znaków
   EN: Move to an external website.
   PL: Przejście na zewnętrzną stronę internetową.
378. [Interfejs i ustawienia [pass_level] — tekst] 패스 레벨
   źródło: MainUIText.json :: dataList[id=pass_level].content
   limit: do 120 znaków
   EN: Pass Level
   PL: Poziom Przepustki
379. [Interfejs i ustawienia [normal_reward] — tekst] 일반 보상
   źródło: MainUIText.json :: dataList[id=normal_reward].content
   limit: do 120 znaków
   EN: Regular Reward
   PL: Nagroda Zwykła
380. [Interfejs i ustawienia [limbus_pass_reward] — tekst] 림버스 패스 보상
   źródło: MainUIText.json :: dataList[id=limbus_pass_reward].content
   limit: do 120 znaków
   EN: Limbus Pass Reward
   PL: Nagroda Limbus Pass
381. [Interfejs i ustawienia [loading_battlehint] — tekst] 전투 팁
   źródło: MainUIText.json :: dataList[id=loading_battlehint].content
   (powtórzenie elementu 33 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Interfejs i ustawienia [status_up] — tekst] 스테이터스 증가
   źródło: MainUIText.json :: dataList[id=status_up].content
   limit: do 120 znaków
   EN: Stats Increased
   PL: Wzrost Statystyk
383. [Interfejs i ustawienia [active_skill_acquired] — tekst] 액티브 스킬 추가
   źródło: MainUIText.json :: dataList[id=active_skill_acquired].content
   limit: do 120 znaków
   EN: Skills Gained
   PL: Dodano Umiejętności
384. [Interfejs i ustawienia [active_skill_reinforcement] — tekst] 액티브 스킬 강화
   źródło: MainUIText.json :: dataList[id=active_skill_reinforcement].content
   limit: do 120 znaków
   EN: Skills Upgraded
   PL: Ulepszono Umiejętności
385. [Interfejs i ustawienia [progress_ego_gacksung] — tekst] 해석 진행
   źródło: MainUIText.json :: dataList[id=progress_ego_gacksung].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Progress\nThreadspin
   PL: Wykonaj\nSplot Nici
386. [Interfejs i ustawienia [skill_with_index] — tekst] 스킬{0}
   źródło: MainUIText.json :: dataList[id=skill_with_index].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill {0}
   PL: Umiejętność {0}
387. [Interfejs i ustawienia [mail_date] — tekst] 수령 일시
   źródło: MainUIText.json :: dataList[id=mail_date].content
   limit: do 120 znaków
   EN: Date
   PL: Data odbioru
388. [Interfejs i ustawienia [mail_sender] — tekst] 보낸 이
   źródło: MainUIText.json :: dataList[id=mail_sender].content
   limit: do 120 znaków
   EN: Sender
   PL: Nadawca
389. [Interfejs i ustawienia [mail_history_notice] — tekst] ※최대 {0}개의 수령 이력이 표시됩니다.
   źródło: MainUIText.json :: dataList[id=mail_history_notice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ Up to {0} claimed items will be displayed in the history.
   PL: ※ W historii wyświetlane jest maks. {0} odebranych przesyłek.
390. [Interfejs i ustawienia [cant_receive_mail_all_tilte] — tekst] 수령 불가
   źródło: MainUIText.json :: dataList[id=cant_receive_mail_all_tilte].content
   limit: do 120 znaków
   EN: Cannot Claim
   PL: Nie można odebrać
391. [Interfejs i ustawienia [cant_receive_mail_all_main] — tekst] 일괄 수령 가능한 우편물 없음
   źródło: MainUIText.json :: dataList[id=cant_receive_mail_all_main].content
   limit: do 120 znaków
   EN: No mail available to claim with “Claim All”
   PL: Brak przesyłek możliwych do zbiorczego odbioru
392. [Interfejs i ustawienia [attached_item] — tekst] 첨부 아이템
   źródło: MainUIText.json :: dataList[id=attached_item].content
   limit: do 120 znaków
   EN: Attached
   PL: Załączniki
393. [Interfejs i ustawienia [inventory_category_all] — tekst] 전체
   źródło: MainUIText.json :: dataList[id=inventory_category_all].content
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Interfejs i ustawienia [inventory_category_normal] — tekst] 기본
   źródło: MainUIText.json :: dataList[id=inventory_category_normal].content
   limit: do 120 znaków
   EN: Basic
   PL: Podstawowe
395. [Interfejs i ustawienia [inventory_category_consumable] — tekst] 소모품
   źródło: MainUIText.json :: dataList[id=inventory_category_consumable].content
   limit: do 120 znaków
   EN: Consumables
   PL: Zużywalne
396. [Interfejs i ustawienia [inventory_category_pieces] — tekst] 파편
   źródło: MainUIText.json :: dataList[id=inventory_category_pieces].content
   limit: do 120 znaków
   EN: Egoshards
   PL: Odłamki
397. [Interfejs i ustawienia [enkephalin_injection_complete] — tekst] 엔케팔린 주입 완료
   źródło: MainUIText.json :: dataList[id=enkephalin_injection_complete].content
   limit: do 120 znaków
   EN: Enkephalin Charged
   PL: Enkefalina uzupełniona
398. [Interfejs i ustawienia [purchase_impossible] — tekst] 구매 불가
   źródło: MainUIText.json :: dataList[id=purchase_impossible].content
   limit: do 120 znaków
   EN: Cannot Purchase
   PL: Zakup niemożliwy
399. [Interfejs i ustawienia [notice_not_enough_pieces] — tekst] ※파편이 부족합니다.
   źródło: MainUIText.json :: dataList[id=notice_not_enough_pieces].content
   limit: do 120 znaków
   EN: ※ Not enough Egoshards.
   PL: ※ Za mało Odłamków E.G.O.
400. [Interfejs i ustawienia [buy_personaliy] — tekst] 인격 구매
   źródło: MainUIText.json :: dataList[id=buy_personaliy].content
   limit: do 120 znaków
   EN: Purchase Identity
   PL: Kup Tożsamość
401. [Interfejs i ustawienia [buy_ego] — tekst] E.G.O 구매
   źródło: MainUIText.json :: dataList[id=buy_ego].content
   limit: do 120 znaków
   EN: Purchase E.G.O
   PL: Kup E.G.O
402. [Interfejs i ustawienia [not_enough_pieces] — tekst] 파편 수량 부족
   źródło: MainUIText.json :: dataList[id=not_enough_pieces].content
   limit: do 120 znaków
   EN: Not enough Egoshards
   PL: Niewystarczająca liczba Odłamków
403. [Interfejs i ustawienia [basis] — tekst] 기초
   źródło: MainUIText.json :: dataList[id=basis].content
   limit: do 120 znaków
   EN: Basic
   PL: Bazowe
404. [Interfejs i ustawienia [skip_tutorial] — tekst] 튜토리얼 스킵
   źródło: MainUIText.json :: dataList[id=skip_tutorial].content
   limit: do 120 znaków
   EN: Skip Tutorial
   PL: Pomiń samouczek
405. [Interfejs i ustawienia [skip_tutorial_description] — tekst] 튜토리얼을 스킵하시겠습니까?
   źródło: MainUIText.json :: dataList[id=skip_tutorial_description].content
   limit: do 120 znaków
   EN: Are you sure you want to skip the tutorial?
   PL: Czy na pewno chcesz pominąć samouczek?
406. [Interfejs i ustawienia [min_speed_upgrade] — tekst] 최소 속도 상승
   źródło: MainUIText.json :: dataList[id=min_speed_upgrade].content
   limit: do 120 znaków
   EN: Min. SPD Up
   PL: Wzrost Min. SZYB.
407. [Interfejs i ustawienia [max_speed_upgrade] — tekst] 최대 속도 상승
   źródło: MainUIText.json :: dataList[id=max_speed_upgrade].content
   limit: do 120 znaków
   EN: Max. SPD Up
   PL: Wzrost Maks. SZYB.
408. [Interfejs i ustawienia [min_max_speed_upgrade] — tekst] 최소, 최대 속도 상승
   źródło: MainUIText.json :: dataList[id=min_max_speed_upgrade].content
   limit: do 120 znaków
   EN: Min. and Max. SPD Up
   PL: Wzrost Min. i Maks. SZYB.
409. [Interfejs i ustawienia [mailbox] — tekst] 우편함
   źródło: MainUIText.json :: dataList[id=mailbox].content
   limit: do 120 znaków
   EN: Mailbox
   PL: Poczta
410. [Interfejs i ustawienia [remain_days_label] — tekst] 수령 기한
   źródło: MainUIText.json :: dataList[id=remain_days_label].content
   limit: do 120 znaków
   EN: Due Date
   PL: Termin odbioru
411. [Interfejs i ustawienia [extract_again] — tekst] 재추출
   źródło: MainUIText.json :: dataList[id=extract_again].content
   limit: do 120 znaków
   EN: Extract Again
   PL: Ponów Ekstrakcję
412. [Interfejs i ustawienia [ego_gift] — tekst] E.G.O 기프트
   źródło: MainUIText.json :: dataList[id=ego_gift].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
413. [Interfejs i ustawienia [classification] — tekst] 분류
   źródło: MainUIText.json :: dataList[id=classification].content
   limit: do 120 znaków
   EN: Category
   PL: Kategoria
414. [Interfejs i ustawienia [quantity] — tekst] 수량
   źródło: MainUIText.json :: dataList[id=quantity].content
   limit: do 120 znaków
   EN: Quantity
   PL: Ilość
415. [Interfejs i ustawienia [appearance_probability] — tekst] 등장 확률
   źródło: MainUIText.json :: dataList[id=appearance_probability].content
   limit: do 120 znaków
   EN: Rate
   PL: Szansa
416. [Interfejs i ustawienia [Individual_appearance_probability] — tekst] 개별 등장 확률
   źródło: MainUIText.json :: dataList[id=Individual_appearance_probability].content
   limit: do 120 znaków
   EN: Individual Rate
   PL: Szansa jednostkowa
417. [Interfejs i ustawienia [notice_sold_out] — tekst] 입고 준비 중...
   źródło: MainUIText.json :: dataList[id=notice_sold_out].content
   limit: do 120 znaków
   EN: Out of Stock
   PL: Wyprzedane
418. [Interfejs i ustawienia [select_piece] — tekst] 교환 파편 선택
   źródło: MainUIText.json :: dataList[id=select_piece].content
   limit: do 120 znaków
   EN: Choose Egoshard
   PL: Wybierz Odłamki
419. [Interfejs i ustawienia [mail_item_warning] — tekst] ※수령 시 청약 철회 제한
   źródło: MainUIText.json :: dataList[id=mail_item_warning].content
   limit: do 120 znaków
   EN: ※ Refund may be restricted after redeeming the item.
   PL: ※ Po odebraniu zwrot zakupu może być ograniczony.
420. [Interfejs i ustawienia [mainui_unlock_condition_by_ego_awaken_level] — tekst] 환상 해석 {0}단계 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_condition_by_ego_awaken_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Unlocked at Tier {0}
   PL: Odblokowanie na {0}. poz. Splotu Nici
421. [Interfejs i ustawienia [empty_mailbox_notice] — tekst] 보관 중인 우편이 없습니다.
   źródło: MainUIText.json :: dataList[id=empty_mailbox_notice].content
   limit: do 120 znaków
   EN: No mail in storage.
   PL: Brak listów w skrzynce.
422. [Interfejs i ustawienia [gacha_rate_detail] — tekst] 추출 확률 상세
   źródło: MainUIText.json :: dataList[id=gacha_rate_detail].content
   limit: do 120 znaków
   EN: Detailed Rates
   PL: Szczegóły szans
423. [Interfejs i ustawienia [gacha_alarm_title] — tekst] 추출 진행
   źródło: MainUIText.json :: dataList[id=gacha_alarm_title].content
   limit: do 120 znaków
   EN: Proceeding with Extraction
   PL: Potwierdzenie Ekstrakcji
424. [Interfejs i ustawienia [clear_specific_stage] — tekst] {0} 클리어
   źródło: MainUIText.json :: dataList[id=clear_specific_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear {0}
   PL: Ukończ {0}
425. [Interfejs i ustawienia [clear_main_chapter_stage] — tekst] {0}장 클리어
   źródło: MainUIText.json :: dataList[id=clear_main_chapter_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Ch. {0}
   PL: Ukończ Rozdz. {0}
426. [Interfejs i ustawienia [ingredients] — tekst] 재료
   źródło: MainUIText.json :: dataList[id=ingredients].content
   limit: do 120 znaków
   EN: Items
   PL: Materiały
427. [Interfejs i ustawienia [remote_download_return_title] — tekst] 새로운 다운로드 항목이 추가되었습니다.\n타이틀로 돌아갑니다.
   źródło: MainUIText.json :: dataList[id=remote_download_return_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new download has been added.\nReturning to the title screen.
   PL: Dodano nowe pliki do pobrania.\nPowrót do ekranu tytułowego.
428. [Interfejs i ustawienia [battle_skip] — tekst] 전투 스킵
   źródło: MainUIText.json :: dataList[id=battle_skip].content
   limit: do 120 znaków
   EN: Skip Battle
   PL: Pomiń walkę
429. [Interfejs i ustawienia [ask_battle_skip] — tekst] 전투 스킵을 진행하시겠습니까?
   źródło: MainUIText.json :: dataList[id=ask_battle_skip].content
   limit: do 120 znaków
   EN: Would you like to skip the battle?
   PL: Czy chcesz pominąć walkę?
430. [Interfejs i ustawienia [notice_consumption_multiples] — tekst] {0} 소모 {1} 배 증가
   źródło: MainUIText.json :: dataList[id=notice_consumption_multiples].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} cost x {1}
   PL: Zużycie ({0}) ×{1}
431. [Interfejs i ustawienia [notice_additional_rewards] — tekst] 추가 보상 {0} 획득
   źródło: MainUIText.json :: dataList[id=notice_additional_rewards].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Additional rewards {0} earned
   PL: Dodatkowe nagrody: {0}
432. [Interfejs i ustawienia [gacha_notice_exclude_ego] — tekst] 본 추출에는 E.G.O 가 등장하지 않습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_exclude_ego].content
   limit: do 120 znaków
   EN: This extraction banner does not include E.G.O.
   PL: W tej Ekstrakcji nie występują E.G.O.
433. [Interfejs i ustawienia [gacha_notice_single_season] — tekst] 본 추출에서 등장하는 2성과 3성 인격은 시즌 {0} 에 해당합니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_single_season].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The 2★ and 3★ Identities in this extraction banner belong to Season {0}.
   PL: Tożsamości 2★ i 3★ w tej Ekstrakcji należą do Sezonu {0}.
434. [Interfejs i ustawienia [error_and_return_to_main] — tekst] 오류가 발생하였습니다.\n메인 화면으로 돌아가겠습니다.
   źródło: MainUIText.json :: dataList[id=error_and_return_to_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An error has occurred.\nReturning to the title screen.
   PL: Wystąpił błąd.\nPowrót do ekranu głównego.
435. [Interfejs i ustawienia [to_window] — tekst] 유리창 이동
   źródło: MainUIText.json :: dataList[id=to_window].content
   limit: do 120 znaków
   EN: To Window
   PL: Do Okna
436. [Interfejs i ustawienia [completion] — tekst] 완료
   źródło: MainUIText.json :: dataList[id=completion].content
   limit: do 120 znaków
   EN: Complete
   PL: Ukończono
437. [Interfejs i ustawienia [event_in_progress] — tekst] 이벤트 중
   źródło: MainUIText.json :: dataList[id=event_in_progress].content
   limit: do 120 znaków
   EN: Event Open
   PL: Wydarzenie trwa
438. [Interfejs i ustawienia [end_of_event] — tekst] 이벤트 종료
   źródło: MainUIText.json :: dataList[id=end_of_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL: Wydarzenie zakończone
439. [Interfejs i ustawienia [gacha_rate_info_intro1_1a] — tekst] 1회 추출 시 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1a].content
   limit: do 120 znaków
   EN: The rates for a single Extraction are as follows.
   PL: Szanse w pojedynczej Ekstrakcji przedstawiają się następująco:
440. [Interfejs i ustawienia [gacha_rate_info_intro1_1b] — tekst] {0} 1회 사용 시, 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1b].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The table for one use of {0} is as follows.
   PL: Szanse przy jednorazowym użyciu przedmiotu {0} przedstawiają się następująco:
441. [Interfejs i ustawienia [gacha_rate_info_intro1_1c] — tekst] {0} 사용 시, 다음 재화 중 하나를 선택할 수 있습니다
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1c].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When you use {0}, you can choose one currency from the following.
   PL: Używając {0}, możesz wybrać jedną z poniższych walut:
442. [Interfejs i ustawienia [package_info_detail1] — tekst] 등장하는 재화를 설정하였을 때, {0} 1개를 사용하여 설정한 재화를 획득할 수량의 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=package_info_detail1].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When you have selected the currency, the table for acquiring different quantities of the set currency by using one {0} is as follows.
   PL: Po wybraniu waluty szanse otrzymania poszczególnych jej ilości przy użyciu 1 szt. {0} przedstawiają się następująco:
443. [Interfejs i ustawienia [package_info_detail2] — tekst] ※ 하단 표의 “{0}”은(는) 상단 표의 등장하는 재화 중 하나를 선택하였을 때의 예시입니다.
   źródło: MainUIText.json :: dataList[id=package_info_detail2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ “{0}” in the lower table is an example for selecting one of the currencies from the table above.
   PL: ※ „{0}” w dolnej tabeli stanowi przykład po wybraniu jednej z walut z górnej tabeli.
444. [Interfejs i ustawienia [acquired_quantity] — tekst] 획득 수량
   źródło: MainUIText.json :: dataList[id=acquired_quantity].content
   limit: do 120 znaków
   EN: Amount
   PL: Ilość
445. [Interfejs i ustawienia [name_of_currencies] — tekst] 재화명
   źródło: MainUIText.json :: dataList[id=name_of_currencies].content
   limit: do 120 znaków
   EN: Currency
   PL: Nazwa waluty
446. [Interfejs i ustawienia [package_info_title] — tekst] 재화 등장 확률 상세
   źródło: MainUIText.json :: dataList[id=package_info_title].content
   limit: do 120 znaków
   EN: Detailed Currency Appearance Rates
   PL: Szczegóły szans na waluty
447. [Interfejs i ustawienia [used_once] — tekst] 1회 사용
   źródło: MainUIText.json :: dataList[id=used_once].content
   limit: do 120 znaków
   EN: One Use
   PL: 1 użycie
448. [Interfejs i ustawienia [probability_details] — tekst] 확률 상세
   źródło: MainUIText.json :: dataList[id=probability_details].content
   limit: do 120 znaków
   EN: Probabilities
   PL: Szczegóły szans
449. [Interfejs i ustawienia [be_in_use] — tekst] 사용 중
   źródło: MainUIText.json :: dataList[id=be_in_use].content
   limit: do 120 znaków
   EN: In Use
   PL: W użyciu
450. [Interfejs i ustawienia [season_information] — tekst] 시즌 안내
   źródło: MainUIText.json :: dataList[id=season_information].content
   limit: do 120 znaków
   EN: Seasons Guide
   PL: Przewodnik po Sezonach
451. [Interfejs i ustawienia [announcer_selection_description] — tekst] ※ 2개 이상의 아나운서를 선택할 경우, 선택된 아나운서의 대사들이 무작위로 재생됩니다. (최대 100개)
   źródło: MainUIText.json :: dataList[id=announcer_selection_description].content
   limit: do 140 znaków
   EN: ※ If you select 2 or more Announcers at once, the dialogue to play will be randomly chosen (up to 100).
   PL: ※ Wybranie co najmniej 2 Komentatorów naraz sprawi, że ich kwestie będą odtwarzane losowo (maks. 100).
452. [Interfejs i ustawienia [panic_type] — tekst] 패닉 유형
   źródło: MainUIText.json :: dataList[id=panic_type].content
   limit: do 120 znaków
   EN: Panic Types
   PL: Typ Paniki
453. [Interfejs i ustawienia [mental_strength] — tekst] 정신력
   źródło: MainUIText.json :: dataList[id=mental_strength].content
   limit: do 120 znaków
   EN: Sanity
   PL: Poczytalność
454. [Interfejs i ustawienia [mental_increase_condition] — tekst] 기본 정신력 증가 조건
   źródło: MainUIText.json :: dataList[id=mental_increase_condition].content
   limit: do 120 znaków
   EN: Base factors increasing Sanity
   PL: Podstawowe warunki wzrostu SP
455. [Interfejs i ustawienia [mental_decrease_condition] — tekst] 기본 정신력 감소 조건
   źródło: MainUIText.json :: dataList[id=mental_decrease_condition].content
   limit: do 120 znaków
   EN: Base factors decreasing Sanity
   PL: Podstawowe warunki spadku SP
456. [Interfejs i ustawienia [mental_low_morale_effect] — tekst] 사기 저하 효과
   źródło: MainUIText.json :: dataList[id=mental_low_morale_effect].content
   limit: do 120 znaków
   EN: Low Morale Effects
   PL: Efekt Niskiego Morale
457. [Interfejs i ustawienia [mental_panic_effect] — tekst] 패닉 효과
   źródło: MainUIText.json :: dataList[id=mental_panic_effect].content
   limit: do 120 znaków
   EN: Panic Effects
   PL: Efekt Paniki
458. [Interfejs i ustawienia [open_scheduled_date_month_day] — tekst] {0}월 {1}일 개방 예정
   źródło: MainUIText.json :: dataList[id=open_scheduled_date_month_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Opening {0}M {1}D (Month/Day)
   PL: Otwarcie: {1}.{0} (dzień.miesiąc)
459. [Interfejs i ustawienia [mainui_acquire_user_ticker_deco] — tekst] 아이템 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquire_user_ticker_deco].content
   limit: do 120 znaków
   EN: Item gained
   PL: Zdobyto przedmiot
460. [Interfejs i ustawienia [last_battlepass_season_level] — tekst] 패스 달성 레벨
   źródło: MainUIText.json :: dataList[id=last_battlepass_season_level].content
   limit: do 120 znaków
   EN: Pass Level
   PL: Osiągnięty Poziom Przepustki
461. [Interfejs i ustawienia [season_end_notification] — tekst] 시즌 종료 안내
   źródło: MainUIText.json :: dataList[id=season_end_notification].content
   limit: do 120 znaków
   EN: Season End Notice
   PL: Koniec Sezonu
462. [Interfejs i ustawienia [season_start_notification] — tekst] 시즌 시작 안내
   źródło: MainUIText.json :: dataList[id=season_start_notification].content
   limit: do 120 znaków
   EN: Season Start Notice
   PL: Początek Sezonu
463. [Interfejs i ustawienia [new_story_appeared_by_new_season] — tekst] 신규 주요 이야기 등장
   źródło: MainUIText.json :: dataList[id=new_story_appeared_by_new_season].content
   limit: do 120 znaków
   EN: New Main Story Content
   PL: Nowy rozdział Głównej Opowieści
464. [Interfejs i ustawienia [collection_rate] — tekst] 수집률
   źródło: MainUIText.json :: dataList[id=collection_rate].content
   limit: do 120 znaków
   EN: Collection Rate
   PL: Stopień kolekcji
465. [Interfejs i ustawienia [season_n_personality] — tekst] 시즌 {0} 인격
   źródło: MainUIText.json :: dataList[id=season_n_personality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0} Identity
   PL: Tożsamość Sezonu {0}
466. [Interfejs i ustawienia [season_n_ego] — tekst] 시즌 {0} E.G.O
   źródło: MainUIText.json :: dataList[id=season_n_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0} E.G.O
   PL: E.G.O Sezonu {0}
467. [Interfejs i ustawienia [season_n] — tekst] 시즌 {0}
   źródło: MainUIText.json :: dataList[id=season_n].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0}
   PL: Sezon {0}
468. [Interfejs i ustawienia [new_season_former_piece_to_current_piece_desc] — tekst] 기존에 보유하였던 자아 파편의 일정량이 현재 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_piece_to_current_piece_desc].content
   limit: do 120 znaków
   EN: A portion of the Egoshards you own will be carried over to the current season.
   PL: Część posiadanych Odłamków E.G.O zostaje przeniesiona na bieżący sezon.
469. [Interfejs i ustawienia [new_season_former_piece_to_thread_desc] — tekst] 이월되지 않은 자아 파편은 끈으로 변경됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_piece_to_thread_desc].content
   limit: do 120 znaków
   EN: The Egoshards that have not been carried over are converted into Thread.
   PL: Nieprzeniesione Odłamki E.G.O zostają zamienione na Nić.
470. [Interfejs i ustawienia [new_season_former_box_to_current_box_desc] — tekst] 기존에 보유하였던 자아 파편 상자, 자아 파편 선택 상자의 일정량이 현재 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_box_to_current_box_desc].content
   limit: do 150 znaków
   EN: A portion of the Egoshard Crates (both random & nominable) you own will be carried over to the current season.
   PL: Część posiadanych losowych oraz imiennych Skrzynek Odłamków E.G.O zostaje przeniesiona na bieżący sezon.
471. [Interfejs i ustawienia [new_season_former_box_to_thread_box] — tekst] 이월되지 않은 자아 파편 상자, 자아 파편 선택 상자는 끈 상자로 변경됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_box_to_thread_box].content
   limit: do 120 znaków
   EN: The Egoshard Crates that have not been carried over are converted into Thread Crates.
   PL: Nieprzeniesione losowe oraz imienne Skrzynki Odłamków E.G.O zostają zamienione na Skrzynki Nici.
472. [Interfejs i ustawienia [new_pass_appeared] — tekst] 신규 패스 출현
   źródło: MainUIText.json :: dataList[id=new_pass_appeared].content
   limit: do 120 znaków
   EN: New Pass Available
   PL: Nowa Przepustka Bojowa
473. [Interfejs i ustawienia [get_not_acquired_rewards] — tekst] 미수령 보상 지급
   źródło: MainUIText.json :: dataList[id=get_not_acquired_rewards].content
   limit: do 120 znaków
   EN: Unclaimed Rewards Delivered
   PL: Przekazano nieodebrane nagrody
474. [Interfejs i ustawienia [items_changed_by_season_changed_desc] — tekst] 이전 시즌의 재화가 현재 시즌에 맞추어 이월 적용됩니다.
   źródło: MainUIText.json :: dataList[id=items_changed_by_season_changed_desc].content
   limit: do 120 znaków
   EN: Currencies from the previous season will be converted into the current season.
   PL: Waluty z poprzedniego sezonu zostały przeliczone na bieżący sezon.
475. [Interfejs i ustawienia [exchange] — tekst] 교환
   źródło: MainUIText.json :: dataList[id=exchange].content
   limit: do 120 znaków
   EN: Exchange
   PL: Wymień
476. [Interfejs i ustawienia [notice_of_pity_system] — tekst] 추출 기간 동안 추출을 진행한 횟수에 따라 이상[理想]을 획득합니다.\n일정 수량의 이상[理想]을 모을 경우, 특정 추출에 등장하는\n대표 3성 인격 혹은 E.G.O와 교환할 수 있습니다.\n\n※ 각각의 특정 추출에서 획득할 수 있는 이상[理想]은 공유되지 않고 서로 별개의 재화로 계산됩니다. \n※ 특정 추출의 기간이 종료되면 교환되지 않은 이상[理想]은 끈으로 전환됩니다.
   źródło: MainUIText.json :: dataList[id=notice_of_pity_system].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During a banner, you can gain ‘Yisang’ [Ideality] based on the number of extractions you’ve done.\nAfter collecting a certain amount, you can exchange it for a 3★ Identity or E.G.O represented on the banner.\n\n※ Ideality is not shared between banners; Ideality in each is considered its own currency.\n※ After the banner is over, the remaining Ideality is converted into Thread.
   PL: W okresie trwania danej Ekstrakcji za każdą wykonaną próbę otrzymujesz punkty Yisang [Ideału].\nPo zebraniu określonej liczby punktów możesz wymienić je na wyróżnioną w tym banerze Tożsamość 3★ lub E.G.O.\n\n※ Punkty Yisang [Ideału] nie są współdzielone między banerami — każdy baner nalicza je osobno.\n※ Po zakończeniu baneru niewykorzystane punkty Yisang [Ideału] zostają zamienione na Nić.
477. [Interfejs i ustawienia [twine_store] — tekst] 파편::끈 교환기
   źródło: MainUIText.json :: dataList[id=twine_store].content
   limit: do 120 znaków
   EN: Shard::Thread Exchange
   PL: Wymiana Odłamki::Nić
478. [Interfejs i ustawienia [pass] — tekst] 패스
   źródło: MainUIText.json :: dataList[id=pass].content
   limit: do 120 znaków
   EN: Pass
   PL: Przepustka
479. [Interfejs i ustawienia [event] — tekst] 이벤트
   źródło: MainUIText.json :: dataList[id=event].content
   limit: do 120 znaków
   EN: Event
   PL: Wydarzenie
480. [Interfejs i ustawienia [notice_of_pity_point_expiration] — tekst] {0} 에서 누적된 이상[理想] {1}개가 끈으로 변환되었습니다.
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_expiration].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} Yisang [Ideality] from {0} has been converted to Thread.
   PL: {1} pkt Yisang [Ideału] z baneru „{0}” zamieniono na Nić.
481. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not] — tekst] 이상[理想] 200개를 소모하여 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_progress_or_not].content
   limit: do 120 znaków
   EN: Spend 200 Yisang [Ideality] and make this exchange?
   PL: Zużyć 200 pkt Yisang [Ideału], aby dokonać wymiany?
482. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not_already_have] — tekst] 선택한 인격을 이미 보유 중입니다. 이상[理想] 200개를 소모하여 선택한 수감자의 파편 50개로 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_progress_or_not_already_have].content
   limit: do 140 znaków
   EN: You already own the selected Identity. Exchange 200 Yisang [Ideality] for this Sinner's 50 Identity Shards?
   PL: Posiadasz już wybraną Tożsamość. Wymienić 200 pkt Yisang [Ideału] na 50 Odłamków E.G.O tego Grzesznika?
483. [Interfejs i ustawienia [open_date_description_month_day_time_zone] — tekst] {0}월 {1}일 ({2}) 업데이트 이후 개방
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Unlocked after {0}/{1} ({2}) update
   PL: Odblokowanie po aktualizacji {1}.{0} ({2})
484. [Interfejs i ustawienia [open_date_description_month_day_time_zone_date] — tekst] {0}월 {1}일 ({2})
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0}/{1} ({2})
   PL: {1}.{0} ({2})
485. [Interfejs i ustawienia [open_date_description_month_day_time_zone_desc] — tekst] 업데이트 이후 개방
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone_desc].content
   limit: do 120 znaków
   EN: Unlocked after Update
   PL: Odblokowanie po aktualizacji
486. [Interfejs i ustawienia [enkephalin_desc] — tekst] 스테이지를 입장할 때 사용한다.
   źródło: MainUIText.json :: dataList[id=enkephalin_desc].content
   limit: do 120 znaków
   EN: Used for entering stages.
   PL: Służy do wchodzenia na etapy.
487. [Interfejs i ustawienia [not_exchangeable] — tekst] 교환 불가
   źródło: MainUIText.json :: dataList[id=not_exchangeable].content
   limit: do 120 znaków
   EN: Cannot Exchange
   PL: Wymiana niemożliwa
488. [Interfejs i ustawienia [ego_already_have] — tekst] 이미 보유 중인 EGO
   źródło: MainUIText.json :: dataList[id=ego_already_have].content
   limit: do 120 znaków
   EN: E.G.O Already Owned
   PL: Posiadane już E.G.O
489. [Interfejs i ustawienia [shortage_number_of_extractions] — tekst] 추출 횟수 부족
   źródło: MainUIText.json :: dataList[id=shortage_number_of_extractions].content
   limit: do 120 znaków
   EN: Not Enough Extractions Done
   PL: Za mało wykonanych Ekstrakcji
490. [Interfejs i ustawienia [lack_of_formation_participation] — tekst] 이번 전투에서는 <color=#990000>최대 {0}명</color>의 수감자가 전투에 참여할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=lack_of_formation_participation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}
   EN: In this battle, <color=#990000>up to {0}</color> Sinners can participate in combat.
   PL: W tej walce może wziąć udział <color=#990000>maks. {0}</color> Grzeszników.
491. [Interfejs i ustawienia [tutorial_formation_participation_add_title] — tekst] 편성 인원 증가
   źródło: MainUIText.json :: dataList[id=tutorial_formation_participation_add_title].content
   limit: do 120 znaków
   EN: More Participants
   PL: Większy limit uczestników
492. [Interfejs i ustawienia [tutorial_formation_participation_add_desc] — tekst] 특정 스테이지에서는 참여할 수 있는 최대 인원 수가 직전에 입장한 스테이지 인원 수와 비교하였을 때 증가할 수 있습니다. 이러한 경우에는 편성 편집 영역이 깜빡거립니다.
   źródło: MainUIText.json :: dataList[id=tutorial_formation_participation_add_desc].content
   limit: do 200 znaków
   EN: Certain stages may allow more Sinners to participate in battle compared to the previous stage played. In this case, the 'Edit Team' area will flicker.
   PL: Na niektórych etapach maksymalna liczba uczestników walki jest wyższa niż na poprzednio rozgrywanym etapie. W takim przypadku przycisk „Edytuj skład” pulsuje.
493. [Interfejs i ustawienia [could_not_select_friend_support_in_this_dungeon] — tekst] 이번 던전에서는 {0}의 지원 인격을 선택할 수 없습니다.
   źródło: MainUIText.json :: dataList[id=could_not_select_friend_support_in_this_dungeon].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You may not bring {0}'s Support Identity for this dungeon.
   PL: W tym lochu nie można wybrać Tożsamości Wsparcia dla Grzesznika: {0}.
494. [Interfejs i ustawienia [formation_force_participation_on] — tekst] 고정 편성
   źródło: MainUIText.json :: dataList[id=formation_force_participation_on].content
   limit: do 120 znaków
   EN: Fixed
   PL: Stały skład
495. [Interfejs i ustawienia [formation_force_participation_off] — tekst] 고정 편성 필요
   źródło: MainUIText.json :: dataList[id=formation_force_participation_off].content
   limit: do 120 znaków
   EN: Fixed Member Needed
   PL: Wymagany uczestnik
496. [Interfejs i ustawienia [formation_must_participate_specific_character] — tekst] {0} 수감자가 참여해야 합니다.
   źródło: MainUIText.json :: dataList[id=formation_must_participate_specific_character].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} must participate.
   PL: W walce musi uczestniczyć: {0}.
497. [Interfejs i ustawienia [cannot_exit_node_after_enter_by_force_alice_character] — tekst] 진입 시 던전의 다른 곳으로 이동할 수 없게 되며, {0} 수감자의 체력이 최대로 회복되고 정신력이 초기화됩니다.\n그래도 진입하시겠습니까?
   źródło: MainUIText.json :: dataList[id=cannot_exit_node_after_enter_by_force_alice_character].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Upon entry, you will no longer be able to travel to other nodes of the dungeon; {0} will fully heal HP and have their SP reset to 0.\nAre you sure you want to proceed?
   PL: Po wejściu nie będzie można przemieszczać się do innych węzłów lochu; PŻ Grzesznika ({0}) zostaną w pełni uleczone, a jego SP zresetowane do 0.\nCzy na pewno chcesz wejść?
498. [Interfejs i ustawienia [story_dungeon_4_first_open_popup_desc] — tekst] 이번 던전에서는 이상 수감자의 지원 인격을 선택할 수 없으며, 해당 수감자가 전투에 항상 참여해야합니다.
   źródło: MainUIText.json :: dataList[id=story_dungeon_4_first_open_popup_desc].content
   limit: do 150 znaków
   EN: For this dungeon, you may not select a Support Identity for Yi Sang. Yi Sang must always participate in battles.
   PL: W tym lochu nie można wybrać Tożsamości Wsparcia dla Yi Sanga, a sam Yi Sang musi zawsze uczestniczyć w walce.
499. [Interfejs i ustawienia [attack_level] — tekst] 공격 레벨
   źródło: MainUIText.json :: dataList[id=attack_level].content
   limit: do 120 znaków
   EN: Offense Level
   PL: Poziom Ataku
500. [Interfejs i ustawienia [defense_level] — tekst] 방어 레벨
   źródło: MainUIText.json :: dataList[id=defense_level].content
   (powtórzenie elementu 204 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Interfejs i ustawienia [personality_level] — tekst] 인격 레벨
   źródło: MainUIText.json :: dataList[id=personality_level].content
   limit: do 120 znaków
   EN: Identity Level
   PL: Poziom Tożsamości
502. [Interfejs i ustawienia [enemy_level] — tekst] 적 레벨
   źródło: MainUIText.json :: dataList[id=enemy_level].content
   limit: do 120 znaków
   EN: Enemy Level
   PL: Poziom Wroga
503. [Interfejs i ustawienia [cannot_enter] — tekst] 입장 불가
   źródło: MainUIText.json :: dataList[id=cannot_enter].content
   limit: do 120 znaków
   EN: Cannot Enter
   PL: Wejście niemożliwe
504. [Interfejs i ustawienia [lack_of_item_amount] — tekst] {0} 보유량 부족
   źródło: MainUIText.json :: dataList[id=lack_of_item_amount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Not enough {0}
   PL: Za mało: {0}
505. [Interfejs i ustawienia [required_count] — tekst] 필요 개수
   źródło: MainUIText.json :: dataList[id=required_count].content
   limit: do 120 znaków
   EN: Required
   PL: Wymagana ilość
506. [Interfejs i ustawienia [on_event_reward_grace_period] — tekst] 보상 수령 기간
   źródło: MainUIText.json :: dataList[id=on_event_reward_grace_period].content
   limit: do 120 znaków
   EN: Reward Reception Period
   PL: Okres odbioru nagród
507. [Interfejs i ustawienia [user_level_maximum_notice] — tekst] 관리자 최대 레벨에 도달했습니다.
   źródło: MainUIText.json :: dataList[id=user_level_maximum_notice].content
   limit: do 120 znaków
   EN: Reached Max Level.
   PL: Osiągnięto maksymalny Poziom Kierownika.
508. [Interfejs i ustawienia [user_level_limit_increase_notice] — tekst] ※ 추후 관리자 레벨 상한이 증가할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=user_level_limit_increase_notice].content
   limit: do 120 znaków
   EN: ※ The Max Manager Level may be raised with future updates.
   PL: ※ Maksymalny Poziom Kierownika może zostać podniesiony w przyszłych aktualizacjach.
509. [Interfejs i ustawienia [level_up] — tekst] 레벨업
   źródło: MainUIText.json :: dataList[id=level_up].content
   limit: do 120 znaków
   EN: Level Up
   PL: Awans Poziomu
510. [Interfejs i ustawienia [summary] — tekst] 요약
   źródło: MainUIText.json :: dataList[id=summary].content
   limit: do 120 znaków
   EN: Summary
   PL: Podsumowanie
511. [Interfejs i ustawienia [abnormality_part_skill] — tekst] 부위 스킬
   źródło: MainUIText.json :: dataList[id=abnormality_part_skill].content
   limit: do 120 znaków
   EN: Part Skills
   PL: Umiej. Części
512. [Interfejs i ustawienia [awaken] — tekst] 각성
   źródło: MainUIText.json :: dataList[id=awaken].content
   limit: do 120 znaków
   EN: Awakening
   PL: Przebudzenie
513. [Interfejs i ustawienia [erosion] — tekst] 침식
   źródło: MainUIText.json :: dataList[id=erosion].content
   limit: do 120 znaków
   EN: Corrosion
   PL: Korozja
514. [Interfejs i ustawienia [formation_panel_detail] — tekst] 상세
   źródło: MainUIText.json :: dataList[id=formation_panel_detail].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
515. [Interfejs i ustawienia [ego_cost] — tekst] E.G.O 자원
   źródło: MainUIText.json :: dataList[id=ego_cost].content
   limit: do 120 znaków
   EN: E.G.O Resources
   PL: Zasoby E.G.O
516. [Interfejs i ustawienia [enable_count_for_battle] — tekst] 전투 참가 가능 수
   źródło: MainUIText.json :: dataList[id=enable_count_for_battle].content
   limit: do 120 znaków
   EN: Participant Limit
   PL: Limit uczestników
517. [Interfejs i ustawienia [select_for_formation] — tekst] 전투 참가 인격 선택
   źródło: MainUIText.json :: dataList[id=select_for_formation].content
   limit: do 120 znaków
   EN: Deploy Identity
   PL: Wystaw Tożsamość
518. [Interfejs i ustawienia [edit_for_formation] — tekst] 편성 편집
   źródło: MainUIText.json :: dataList[id=edit_for_formation].content
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Interfejs i ustawienia [full_participated] — tekst] 참가 인원 최대
   źródło: MainUIText.json :: dataList[id=full_participated].content
   limit: do 120 znaków
   EN: Max Participants
   PL: Pełny skład
520. [Interfejs i ustawienia [select_for_delete_participation] — tekst] 전투 참가 해제
   źródło: MainUIText.json :: dataList[id=select_for_delete_participation].content
   limit: do 120 znaków
   EN: Dismiss Identity
   PL: Wycofaj z walki
521. [Interfejs i ustawienia [clear_reward] — tekst] 클리어 보상
   źródło: MainUIText.json :: dataList[id=clear_reward].content
   limit: do 120 znaków
   EN: Clear Rewards
   PL: Nagrody za ukończenie
522. [Interfejs i ustawienia [event_information] — tekst] 이벤트 안내
   źródło: MainUIText.json :: dataList[id=event_information].content
   limit: do 120 znaków
   EN: Event Info.
   PL: O wydarzeniu
523. [Interfejs i ustawienia [notice_not_on_sales_period] — tekst] ※구매할 수 있는 기간이 아닙니다.
   źródło: MainUIText.json :: dataList[id=notice_not_on_sales_period].content
   limit: do 120 znaków
   EN: ※ Cannot be purchased during this period.
   PL: ※ Przedmiot niedostępny w obecnym okresie sprzedaży.
524. [Interfejs i ustawienia [pc_shortcut] — tekst] PC 단축키
   źródło: MainUIText.json :: dataList[id=pc_shortcut].content
   limit: do 120 znaków
   EN: PC Keyboard Shortcuts
   PL: Skróty klawiszowe PC
525. [Interfejs i ustawienia [shortcut_manual_popup_title] — tekst] 단축키 매뉴얼
   źródło: MainUIText.json :: dataList[id=shortcut_manual_popup_title].content
   limit: do 120 znaków
   EN: Keyboard Shortcuts Guide
   PL: Przewodnik po skrótach klawiszowych
526. [Interfejs i ustawienia [new_dungeon_update_alarm] — tekst] 뒷문 변화 감지
   źródło: MainUIText.json :: dataList[id=new_dungeon_update_alarm].content
   limit: do 120 znaków
   EN: BACKDOOR VOLATILITY DETECTED
   PL: WYKRYTO ZMIANY ZA TYLNYMI DRZWIAMI
527. [Interfejs i ustawienia [buy_announcer] — tekst] 아나운서 구매
   źródło: MainUIText.json :: dataList[id=buy_announcer].content
   limit: do 120 znaków
   EN: Purchase Announcer
   PL: Kup Komentatora
528. [Interfejs i ustawienia [label_require_paid_lunacy] — tekst] ※유료 광기가 부족합니다.
   źródło: MainUIText.json :: dataList[id=label_require_paid_lunacy].content
   limit: do 120 znaków
   EN: ※You don’t have enough paid Lunacy.
   PL: ※ Za mało Płatnego Szaleństwa.
529. [Interfejs i ustawienia [notice_require_paid_lunacy] — tekst] 유료 광기 수량 부족
   źródło: MainUIText.json :: dataList[id=notice_require_paid_lunacy].content
   limit: do 120 znaków
   EN: Insufficient Paid Lunacy
   PL: Niewystarczające Płatne Szaleństwo
530. [Interfejs i ustawienia [mainui_original] — tekst] 기존
   źródło: MainUIText.json :: dataList[id=mainui_original].content
   limit: do 120 znaków
   EN: Before
   PL: Poprzednio
531. [Interfejs i ustawienia [open_after_clear_node] — tekst] {0}-{1} 클리어 후 개방
   źródło: MainUIText.json :: dataList[id=open_after_clear_node].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Clear {0}-{1} to Unlock
   PL: Odblokowanie po ukończeniu {0}-{1}
532. [Interfejs i ustawienia [effect_list_to_applied_level] — tekst] 레벨 적용 효과 목록
   źródło: MainUIText.json :: dataList[id=effect_list_to_applied_level].content
   limit: do 120 znaków
   EN: Active Level Effects
   PL: Aktywne efekty poziomu
533. [Interfejs i ustawienia [choice_event_effect] — tekst] 선택지 효과
   źródło: MainUIText.json :: dataList[id=choice_event_effect].content
   limit: do 120 znaków
   EN: Choice Effect
   PL: Efekt wyboru
534. [Interfejs i ustawienia [ego_gift_effect_format] — tekst] E.G.O 기프트 「{0}」 효과
   źródło: MainUIText.json :: dataList[id=ego_gift_effect_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Gift 「{0}」 Effect
   PL: Efekt Daru E.G.O 「{0}」
535. [Interfejs i ustawienia [mainui_previous] — tekst] 이전
   źródło: MainUIText.json :: dataList[id=mainui_previous].content
   limit: do 120 znaków
   EN: Previous
   PL: Wstecz
536. [Interfejs i ustawienia [formation_force_abstain] — tekst] 인격 편성 불가
   źródło: MainUIText.json :: dataList[id=formation_force_abstain].content
   limit: do 120 znaków
   EN: Cannot Deploy
   PL: Nie można wystawić
537. [Interfejs i ustawienia [formation_view_detail] — tekst] 상세 보기
   źródło: MainUIText.json :: dataList[id=formation_view_detail].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
538. [Interfejs i ustawienia [only_hyphen] — tekst] -
   źródło: MainUIText.json :: dataList[id=only_hyphen].content
   limit: do 120 znaków
   EN: -
   PL: -
539. [Interfejs i ustawienia [first_time] — tekst] 초회
   źródło: MainUIText.json :: dataList[id=first_time].content
   limit: do 120 znaków
   EN: First-time
   PL: 1. raz
540. [Interfejs i ustawienia [formation_Announcer_fixed] — tekst] 고정 편성
   źródło: MainUIText.json :: dataList[id=formation_Announcer_fixed].content
   (powtórzenie elementu 494 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Interfejs i ustawienia [gacha_rate_info_wa1] — tekst] ★ 끈 상자
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_wa1].content
   limit: do 120 znaków
   EN: ★ Thread Crate
   PL: ★ Skrzynka Nici
542. [Interfejs i ustawienia [gacha_rate_info_wa2] — tekst] 이미 보유한 아나운서를 중복하여 획득할 경우에는 끈 상자로 전환되어 획득하게 됩니다.\n\n획득한 끈 상자는 보유한 수량 그대로 다음 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_wa2].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtaining a duplicate of an already-owned Announcer will convert it to Thread Crates.\n\nThese Thread Crates will be carried over as-is to the next Season.
   PL: Wylosowanie duplikatu posiadanego już Komentatora zostaje zamienione na Skrzynki Nici.\n\nZdobyte Skrzynki Nici przechodzą w całości na kolejny sezon.
543. [Interfejs i ustawienia [login_scene_mini_story_warning_spoiler_format] — tekst] 주요 이야기 {0}장 이후의 내용을 담고 있습니다. 스토리를 감상하시겠습니까?
   źródło: MainUIText.json :: dataList[id=login_scene_mini_story_warning_spoiler_format].content
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Interfejs i ustawienia [notice_of_pity_point_already_have_announcer] — tekst] 선택한 아나운서를 이미 보유 중입니다. 이상[理想] 200개를 소모하여 끈 상자 50개로 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_already_have_announcer].content
   limit: do 120 znaków
   EN: You already own the selected Announcer. Exchange 200 Yisang [Ideality] for 50 Thread Crates?
   PL: Posiadasz już wybranego Komentatora. Wymienić 200 pkt Yisang [Ideału] na 50 Skrzynek Nici?
545. [Interfejs i ustawienia [gacha_rate_info_announcer1] — tekst] 상단에 있는 추출 확률에 따라 하단에 명시된 목록에 있는 인격과 E.G.O 또는 아나운서를 획득할 수 있습니다.\n\n획득할 수 있는 인격과 E.G.O, 아나운서는 특정 시즌에 따라 변경될 수 있으며, 이러한 경우에는 변경 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_announcer1].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Below is the list of Identities, E.G.O, and Announcers you can obtain following the aforementioned rates.\n\nThe list may change in certain seasons; upcoming changes to the reward tables will be announced in advance.
   PL: Zgodnie z powyższymi szansami można zdobyć Tożsamości, E.G.O oraz Komentatorów z listy poniżej.\n\nDostępna pula może ulec zmianie wraz z sezonem, o czym poinformujemy z wyprzedzeniem w ogłoszeniach.
546. [Interfejs i ustawienia [mainui_battleresult_ordeal_victory] — tekst] 제압 종료
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_ordeal_victory].content
   limit: do 120 znaków
   EN: Suppression Complete
   PL: Tłumienie Zakończone
547. [Interfejs i ustawienia [mainui_battleresult_ordeal_defeat] — tekst] 제압 실패
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_ordeal_defeat].content
   limit: do 120 znaków
   EN: Suppression Failed
   PL: Tłumienie Nieudane
548. [Interfejs i ustawienia [remain_exchange_count] — tekst] 잔여 교환 횟수
   źródło: MainUIText.json :: dataList[id=remain_exchange_count].content
   limit: do 120 znaków
   EN: Remaining Stock
   PL: Pozostała liczba wymian
549. [Interfejs i ustawienia [remains] — tekst] 잔여
   źródło: MainUIText.json :: dataList[id=remains].content
   limit: do 120 znaków
   EN: Remaining
   PL: Pozostało
550. [Interfejs i ustawienia [everyday] — tekst] 매일
   źródło: MainUIText.json :: dataList[id=everyday].content
   limit: do 120 znaków
   EN: Daily
   PL: Codziennie
551. [Interfejs i ustawienia [for_n_days] — tekst] {0}일째
   źródło: MainUIText.json :: dataList[id=for_n_days].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Days
   PL: Dzień {0}
552. [Interfejs i ustawienia [all_personalities] — tekst] 전체 인격
   źródło: MainUIText.json :: dataList[id=all_personalities].content
   limit: do 120 znaków
   EN: All Identities
   PL: Wszystkie Tożsamości
553. [Interfejs i ustawienia [leap_up_ticket_title] — tekst] 상승 도약 인격 선택
   źródło: MainUIText.json :: dataList[id=leap_up_ticket_title].content
   limit: do 120 znaków
   EN: Select Identity to Takeoff
   PL: Wybierz Tożsamość do Skoku Rozwoju
554. [Interfejs i ustawienia [leap_up_able_uptie_tier_and_level] — tekst] 동기화 단계, 레벨 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_uptie_tier_and_level].content
   limit: do 120 znaków
   EN: Can raise Uptie Tier & Identity Level
   PL: Możliwy wzrost Synchronizacji i Poziomu
555. [Interfejs i ustawienia [leap_up_able_uptie_tier] — tekst] 동기화 단계 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_uptie_tier].content
   limit: do 120 znaków
   EN: Can raise Uptie Tier
   PL: Możliwy wzrost Synchronizacji
556. [Interfejs i ustawienia [leap_up_able_level] — tekst] 레벨 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_level].content
   limit: do 120 znaków
   EN: Can raise Identity Level
   PL: Możliwy wzrost Poziomu
557. [Interfejs i ustawienia [leap_up_confim_title] — tekst] 인격 선택
   źródło: MainUIText.json :: dataList[id=leap_up_confim_title].content
   limit: do 120 znaków
   EN: Select Identity
   PL: Wybór Tożsamości
558. [Interfejs i ustawienia [leap_up_confim_main] — tekst] [{0}] 인격의 성장 단계가 다음과 같이 변경됩니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0}] Identity's Uptie Tier & Level will be changed as follows.
   PL: Stopień rozwoju Tożsamości [{0}] zmieni się następująco:
559. [Interfejs i ustawienia [leap_up_confim_caution_uptie] — tekst] 선택한 인격의 동기화 단계가 더 이상 증가하지 않습니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_caution_uptie].content
   limit: do 120 znaków
   EN: The selected Identity's Uptie Tier cannot be raised further.
   PL: Poziom Synchronizacji wybranej Tożsamości nie może już wzrosnąć.
560. [Interfejs i ustawienia [leap_up_confim_caution_level] — tekst] 선택한 인격의 레벨이 더 이상 증가하지 않습니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_caution_level].content
   limit: do 120 znaków
   EN: The selected Identity's Level cannot be raised further.
   PL: Poziom wybranej Tożsamości nie może już wzrosnąć.
561. [Interfejs i ustawienia [leap_up_confim_last_question] — tekst] <color=#F8C200>{0}</color> 을(를) 사용하시겠습니까?
   źródło: MainUIText.json :: dataList[id=leap_up_confim_last_question].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, {0}
   EN: Use <color=#F8C200>{0}</color>?
   PL: Czy chcesz użyć: <color=#F8C200>{0}</color>?
562. [Interfejs i ustawienia [expiration_date] — tekst] 유효 기간
   źródło: MainUIText.json :: dataList[id=expiration_date].content
   limit: do 120 znaków
   EN: Available Period
   PL: Okres ważności
563. [Interfejs i ustawienia [unlink_account_title] — tekst] 연동 해제 계정 선택
   źródło: MainUIText.json :: dataList[id=unlink_account_title].content
   limit: do 120 znaków
   EN: Select Account to Unlink
   PL: Wybierz konto do odłączenia
564. [Interfejs i ustawienia [unlink_account_current_account] — tekst] 현재 계정
   źródło: MainUIText.json :: dataList[id=unlink_account_current_account].content
   limit: do 120 znaków
   EN: Current Account
   PL: Obecne konto
565. [Interfejs i ustawienia [unlink_account_linked_account] — tekst] 연동된 계정
   źródło: MainUIText.json :: dataList[id=unlink_account_linked_account].content
   limit: do 120 znaków
   EN: Linked Accounts
   PL: Powiązane konta
566. [Interfejs i ustawienia [unlink_account_desc] — tekst] 연동 해제 시, {0}일간 해제가 불가능합니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Once you unlink, you will not be able to unlink again for {0} days.
   PL: Po odłączeniu konta ponowne odłączenie będzie niemożliwe przez {0} dni.
567. [Interfejs i ustawienia [unlink_account_desc_unable_by_day] — tekst] {0} 이후부터 연동 해제가 가능합니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_desc_unable_by_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Can be unlinked after {0}.
   PL: Odłączenie konta będzie możliwe po: {0}.
568. [Interfejs i ustawienia [unlink_account_complete_title] — tekst] 연동 해제 완료
   źródło: MainUIText.json :: dataList[id=unlink_account_complete_title].content
   limit: do 120 znaków
   EN: Account Unlinked
   PL: Odłączono konto
569. [Interfejs i ustawienia [unlink_account_complete_desc] — tekst] 연동 해제가 완료되었습니다.\n타이틀 화면으로 돌아갑니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_complete_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Account unlinking complete.\nReturning to the title screen.
   PL: Odłączanie konta zakończone.\nPowrót do ekranu tytułowego.
570. [Interfejs i ustawienia [mainui_stageinfo_effectiveAttribute] — tekst] 유효 속성
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_effectiveAttribute].content
   limit: do 120 znaków
   EN: Effective Affinities
   PL: Skuteczne Grzechy
571. [Interfejs i ustawienia [personality_level_limit_release_title] — tekst] 인격 최대 레벨 확장
   źródło: MainUIText.json :: dataList[id=personality_level_limit_release_title].content
   limit: do 120 znaków
   EN: Identity Max Lv. Expanded
   PL: Zwiększono Maks. Poziom Tożsamości
572. [Interfejs i ustawienia [personality_level_limit_release_desc] — tekst] 인격의 최대 레벨이 상승하였습니다.
   źródło: MainUIText.json :: dataList[id=personality_level_limit_release_desc].content
   limit: do 120 znaków
   EN: The level cap for your Identities have been raised.
   PL: Maksymalny poziom Tożsamości został podniesiony.
573. [Interfejs i ustawienia [mainui_sinners_startSuppress] — tekst] 제압 시작
   źródło: MainUIText.json :: dataList[id=mainui_sinners_startSuppress].content
   limit: do 120 znaków
   EN: Suppress
   PL: Rozpocznij Tłumienie
574. [Interfejs i ustawienia [mainui_battleresult_AbnormalitySuppress_victory] — tekst] 환상체 제압 성공
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_AbnormalitySuppress_victory].content
   limit: do 120 znaków
   EN: Abnormality Suppression Successful
   PL: Tłumienie Anomalii Zakończone Sukcesem
575. [Interfejs i ustawienia [mainui_battleresult_AbnormalitySuppress_defeat] — tekst] 환상체 제압 실패
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_AbnormalitySuppress_defeat].content
   limit: do 120 znaków
   EN: Abnormality Suppression Failed
   PL: Tłumienie Anomalii Nieudane
576. [Interfejs i ustawienia [ui_text_unknown] — tekst] 알 수 없음
   źródło: MainUIText.json :: dataList[id=ui_text_unknown].content
   limit: do 120 znaków
   EN: Unknown
   PL: Nieznane
577. [Interfejs i ustawienia [buff_effect_for_level_format] — tekst] 버프「{0}」
   źródło: MainUIText.json :: dataList[id=buff_effect_for_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 「{0}」
   PL: 「{0}」
578. [Interfejs i ustawienia [unit_keyword] — tekst] 특성 키워드
   źródło: MainUIText.json :: dataList[id=unit_keyword].content
   limit: do 120 znaków
   EN: Trait Keywords
   PL: Cechy Jednostki
579. [Interfejs i ustawienia [formation_ask_clear_selection] — tekst] 편성 순서를 초기화하시겠습니까?
   źródło: MainUIText.json :: dataList[id=formation_ask_clear_selection].content
   limit: do 120 znaków
   EN: Reset Deployment Order?
   PL: Zresetować kolejność wystawienia?
580. [Interfejs i ustawienia [item_owned_count] — tekst] (보유량 : {0})
   źródło: MainUIText.json :: dataList[id=item_owned_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Owned : {0})
   PL: (Posiadane: {0})
581. [Interfejs i ustawienia [lunacy_owned_count_paid] — tekst] (유료 보유량 : {0}, 무료 보유량 : {1})
   źródło: MainUIText.json :: dataList[id=lunacy_owned_count_paid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: (Paid : {0}, Free : {1})
   PL: (Płatne: {0}, Darmowe: {1})
582. [Interfejs i ustawienia [lunacy_owned_count_free] — tekst] (유료 보유량 : {0}, 무료 보유량 : {1})
   źródło: MainUIText.json :: dataList[id=lunacy_owned_count_free].content
   (powtórzenie elementu 581 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Interfejs i ustawienia [mainui_ask_use_personality_level_ticket_disadvantage] — tekst] 관리자님이 현재 진행도에서 해당 티켓을 사용할 경우,\n선택한 인격의 레벨이 {0}이 아닌 {1}으로 적용되어\n대량의 경험치 손실을 입을 수 있습니다.\n\n그럼에도 불구하고 해당 티켓을 사용하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_use_personality_level_ticket_disadvantage].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: Using this ticket at your current story progress will raise your selected Identity's level to {1} instead of {0}, and any unused EXP in that process will be lost.\n\nWill you use this ticket anyway?
   PL: Użycie tego biletu przy obecnym postępie fabularnym podniesie poziom wybranej Tożsamości do {1} zamiast {0}, co spowoduje utratę nadmiarowych PD.\n\nCzy mimo to chcesz użyć tego biletu?
584. [Interfejs i ustawienia [mainui_exp_dungeon_7_title] — tekst] 경험치 채광-7 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_7_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Slash)
   PL: Wydobycie PD #7 (Cięcie)
585. [Interfejs i ustawienia [mainui_exp_dungeon_7_open_day] — tekst] 경험치 채광 7단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_7_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Slash) opens on MON, TUE, and SUN.
   PL: Wydobycie PD #7 (Cięcie) jest otwarte w poniedziałki, wtorki i niedziele.
586. [Interfejs i ustawienia [mainui_exp_dungeon_8_title] — tekst] 경험치 채광-7 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_8_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Pierce)
   PL: Wydobycie PD #7 (Kłucie)
587. [Interfejs i ustawienia [mainui_exp_dungeon_8_open_day] — tekst] 경험치 채광 7단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_8_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Pierce) opens on WED, THU, and SUN.
   PL: Wydobycie PD #7 (Kłucie) jest otwarte w środy, czwartki i niedziele.
588. [Interfejs i ustawienia [mainui_exp_dungeon_9_title] — tekst] 경험치 채광-7 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_9_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Blunt)
   PL: Wydobycie PD #7 (Obuch)
589. [Interfejs i ustawienia [mainui_exp_dungeon_9_open_day] — tekst] 경험치 채광 7단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_9_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Blunt) opens on FRI, SAT, and SUN.
   PL: Wydobycie PD #7 (Obuch) jest otwarte w piątki, soboty i niedziele.
