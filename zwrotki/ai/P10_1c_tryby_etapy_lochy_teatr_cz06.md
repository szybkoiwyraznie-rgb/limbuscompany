# Paczka AI P10 (Fala 1 · 1C) — Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI) (część 6/6)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P10_1c_tryby_etapy_lochy_teatr_cz06.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P10_1c_tryby_etapy_lochy_teatr_cz06.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_5_InfinityFloor
- plik gry: `MirrorDungeonUI_5_InfinityFloor.json`

1. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_CLEAR] — tekst] 클리어
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_CLEAR].content
   limit: do 120 znaków
   EN: Clears
   PL: Ukończenia
2. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_DECK] — tekst] 편성
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_DECK].content
   limit: do 120 znaków
   EN: Loadout
   PL: Skład
3. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_SHOP] — tekst] 상점
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_SHOP].content
   limit: do 120 znaków
   EN: Shop
   PL: Sklep
4. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_date] — tekst] 거울 던전 6 업데이트 전까지 보상을 수령할 수 있습니다.
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_date].content
   limit: do 120 znaków
   EN: The rewards can be claimed until before the Mirror Dungeon #6 Update.
   PL: Nagrody można odebrać do aktualizacji Lustrzanego Lochu #6.
5. [Tryby lochów i Kolei Refrakcji [mirrordungeon_infinityFloor_Entrance_ThemeSelectPanel] — tekst] 평행중첩 모드 활성화
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_infinityFloor_Entrance_ThemeSelectPanel].content
   limit: do 120 znaków
   EN: Parallel Superposition Engaged
   PL: Tryb Superpozycji Równoległej aktywny
6. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_clear_condition] — tekst] ※ 보상 수령 창에서 엔케팔린 모듈을 소모한 경우에만 클리어한 것으로 간주됩니다.
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_clear_condition].content
   limit: do 170 znaków
   EN: ※ Mirror Dungeon floors are counted as 'cleared' only when the player consumed Enkephalin Modules in the Reward Claim window.
   PL: ※ Ukończenie jest zaliczane wyłącznie wtedy, gdy w oknie odbioru nagród zużyto Moduły Enkefaliny.
7. [Tryby lochów i Kolei Refrakcji [mirrordungeon_infinity_open_condition] — tekst] 6장 클리어
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_infinity_open_condition].content
   limit: do 120 znaków
   EN: Clear Canto VI
   PL: Ukończ Canto VI
8. [Tryby lochów i Kolei Refrakcji [InfinityFloor_Mode_Button_Notie] — tekst] ※ 모든 층을 하드 난이도로 클리어 시, 적용됩니다.
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=InfinityFloor_Mode_Button_Notie].content
   limit: do 120 znaków
   EN: ※ Clear every Floor of your run in Hard difficulty to enter.
   PL: ※ Aktywuje się po ukończeniu wszystkich pięter na poziomie Trudnym.
9. [Tryby lochów i Kolei Refrakcji [IsOnInfinityMod] — tekst] ON
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=IsOnInfinityMod].content
   limit: do 120 znaków
   EN: ON
   PL: ON
10. [Tryby lochów i Kolei Refrakcji [IsOFFInfinityMod] — tekst] OFF
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=IsOFFInfinityMod].content
   limit: do 120 znaków
   EN: OFF
   PL: OFF
11. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_BATTLE] — tekst] 전투
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_BATTLE].content
   limit: do 120 znaków
   EN: Combat
   PL: Walka
12. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON5_ALL] — tekst] 달성도
   źródło: MirrorDungeonUI_5_InfinityFloor.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON5_ALL].content
   limit: do 120 znaków
   EN: Completionist
   PL: Postęp ogólny

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_6
- plik gry: `MirrorDungeonUI_6.json`

13. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_button] — tekst] 테마팩 관측
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_button].content
   limit: do 120 znaków
   EN: Pack Search
   PL: Obserwacja Pakietów
14. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_list_popup_title_format] — tekst] {0}층 테마팩 관측
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_list_popup_title_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Search Theme Packs for Floor {0}
   PL: Obserwacja Pakietów Tematycznych — {0}. piętro
15. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_comfirm_modal_desc_format] — tekst] '{0}' 테마팩이 '{1}' 테마팩으로 변경됩니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_comfirm_modal_desc_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: '{0}' Pack will be replaced with '{1}' Pack.
   PL: Pakiet Tematyczny „{0}” zostanie zastąpiony pakietem „{1}”.
16. [Tryby lochów i Kolei Refrakcji [combineUI_enableStarlight] — tekst] 소원 빌기
   źródło: MirrorDungeonUI_6.json :: dataList[id=combineUI_enableStarlight].content
   limit: do 120 znaków
   EN: Wishmaking
   PL: Wypowiedz życzenie
17. [Tryby lochów i Kolei Refrakcji [combineUI_enableStarlight_confirm_desc] — tekst] 별빛을 5 소모하여 합성 확률을 증가시키시겠습니까?
   źródło: MirrorDungeonUI_6.json :: dataList[id=combineUI_enableStarlight_confirm_desc].content
   limit: do 120 znaków
   EN: Spend 5 Starlight to improve Fusion chance?
   PL: Wydać 5 Gwiezdnego Blasku, aby zwiększyć szansę Syntezy?
18. [Tryby lochów i Kolei Refrakcji [side_title_not_enough_starlight] — tekst] 별빛이 충분하지 않습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=side_title_not_enough_starlight].content
   limit: do 120 znaków
   EN: Not enough Starlight.
   PL: Za mało Gwiezdnego Blasku.
19. [Tryby lochów i Kolei Refrakcji [side_title_not_use_starlight] — tekst] 별빛을 소모할 수 없습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=side_title_not_use_starlight].content
   limit: do 120 znaków
   EN: Cannot spend Starlight.
   PL: Nie można wydać Gwiezdnego Blasku.
20. [Tryby lochów i Kolei Refrakcji [side_desc_is_fixed_combine_egogift] — tekst] 확정합성되는 E.G.O 기프트 조합식입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=side_desc_is_fixed_combine_egogift].content
   limit: do 120 znaków
   EN: This is a guaranteed E.G.O Gift Fusion Recipe.
   PL: To receptura gwarantowanej Syntezy Daru E.G.O.
21. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_side_popup_already_in_pool] — tekst] 이미 목록에 존재하는 테마팩입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_side_popup_already_in_pool].content
   limit: do 120 znaków
   EN: This Theme Pack is already available.
   PL: Ten Pakiet Tematyczny znajduje się już na liście.
22. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_1] — tekst] 개방 조건을 만족해야하는 테마팩입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_1].content
   limit: do 120 znaków
   EN: This Theme Pack's unlock conditions need to be met first.
   PL: Ten Pakiet Tematyczny wymaga spełnienia warunków odblokowania.
23. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_2_format] — tekst] 개방 조건 {0}장 클리어 시 진입 가능한 테마팩입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_2_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This Theme Pack will become available when meeting the Unlock Conditions: Clear Chapter {0}.
   PL: Pakiet dostępny po spełnieniu warunku odblokowania: ukończ Canto {0}.
24. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_side_popup_passed_pack] — tekst] 이전 층에서 선택한 테마팩입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_side_popup_passed_pack].content
   limit: do 120 znaków
   EN: This Theme Pack has already been selected in previous Floors.
   PL: Ten Pakiet Tematyczny został już wybrany na wcześniejszym piętrze.
25. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_not_enough_point] — tekst] 테마팩 관측에 필요한 별빛이 부족합니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_detect_theme_pack_not_enough_point].content
   limit: do 120 znaków
   EN: Not enough Starlight to Observe Theme Packs.
   PL: Za mało Gwiezdnego Blasku do Obserwacji Pakietów Tematycznych.
26. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_blocked_6] — tekst] 7장 클리어 시 개방됩니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_theme_hard_blocked_6].content
   limit: do 120 znaków
   EN: Clear Canto 7 to Unlock.
   PL: Odblokowanie po ukończeniu Canto VII.
27. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_difficulty_button_no_hard_data] — tekst] 하드 업데이트 예정입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_theme_difficulty_button_no_hard_data].content
   limit: do 120 znaków
   EN: Hard Difficulty will be updated at a later date.
   PL: Poziom Trudny zostanie dodany w aktualizacji.
28. [Tryby lochów i Kolei Refrakcji [on_click_mirrordungeon_theme_list_hard_button] — tekst] 추후 업데이트 예정
   źródło: MirrorDungeonUI_6.json :: dataList[id=on_click_mirrordungeon_theme_list_hard_button].content
   limit: do 120 znaków
   EN: Will be updated at a later date
   PL: W przyszłej aktualizacji
29. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_unavailable_purchase] — tekst] 보유 중인 별빛이 부족합니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_unavailable_purchase].content
   limit: do 120 znaków
   EN: Not enough Starlight.
   PL: Za mało posiadanego Gwiezdnego Blasku.
30. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_unavailable_purchase_modal_title] — tekst] 별빛 부족
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_unavailable_purchase_modal_title].content
   limit: do 120 znaków
   EN: Not Enough Starlight
   PL: Za mało Gwiezdnego Blasku
31. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_left_cost] — tekst] 잔여 별빛
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_purchase_modal_left_cost].content
   limit: do 120 znaków
   EN: Remaining Starlight
   PL: Pozostały Gwiezdny Blask
32. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_desc_md6_toggle_on] — tekst] 별의 가호를 구매하고 남은\n별빛을 코스트로 전환합니다.\n\n※ 보유 별빛은 코스트로\n전환되지 않습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_purchase_modal_desc_md6_toggle_on].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Coverts any remaining Starlight\nafter purchasing Grace of Stars to Cost.\n\n※ "Owned Starlight" will\nnot be converted into Cost.
   PL: Zamienia Gwiezdny Blask pozostały po zakupie\nBłogosławieństw Gwiazd na Koszt.\n\n※ Posiadany zapas Gwiezdnego Blasku\nnie jest zamieniany na Koszt.
33. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_desc_md6_toggle_off] — tekst] 별의 가호를 구매하고 남은\n별빛을 클리어 시 수령합니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_purchase_modal_desc_md6_toggle_off].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Any unspent Starlight will be\nadded to your Dungeon clear rewards.
   PL: Gwiezdny Blask pozostały po zakupie\nBłogosławieństw Gwiazd odbierzesz po ukończeniu lochu.
34. [Tryby lochów i Kolei Refrakcji [mirror_theme_list_pack_tag_not_selectable] — tekst] 선택 불가
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_theme_list_pack_tag_not_selectable].content
   limit: do 120 znaków
   EN: Unselectable
   PL: Niedostępny
35. [Tryby lochów i Kolei Refrakcji [mirror_theme_list_pack_tag_required_extra_point] — tekst] 추가 소모
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_theme_list_pack_tag_required_extra_point].content
   limit: do 120 znaków
   EN: Extra Charge
   PL: Dodatkowy koszt
36. [Tryby lochów i Kolei Refrakcji [side_desc_is_already_success_percent] — tekst] 합성 확률은 100%를 초과할 수 없습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=side_desc_is_already_success_percent].content
   limit: do 120 znaków
   EN: Fusion Forecast cannot exceed 100%.
   PL: Szansa Syntezy nie może przekroczyć 100%.
37. [Tryby lochów i Kolei Refrakcji [side_desc_is_all_collect_egogift] — tekst] 무작위 키워드 확률 입니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=side_desc_is_all_collect_egogift].content
   limit: do 120 znaków
   EN: Random Keyword Chance.
   PL: Szansa na losowe słowo kluczowe.
38. [Tryby lochów i Kolei Refrakcji [mirrordungeon_infinity_open_condition_no_have_infinity_data] — tekst] 공사중
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_infinity_open_condition_no_have_infinity_data].content
   limit: do 120 znaków
   EN: Under Construction
   PL: W budowie
39. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_6] — tekst] 영생의 거울 {0}층
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_progress_text_6].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mirror of Immortality - F{0}
   PL: Lustro Nieśmiertelności — {0}. piętro
40. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_available_starlight] — tekst] 사용 가능
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_available_starlight].content
   limit: do 120 znaków
   EN: Available
   PL: Dostępne
41. [Tryby lochów i Kolei Refrakcji [mirrordungeon_starlight_personality_button_label] — tekst] 별빛 보존 대상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_starlight_personality_button_label].content
   limit: do 120 znaków
   EN: Starlight Retention Units
   PL: Zachowanie Gwiezdnego Blasku
42. [Tryby lochów i Kolei Refrakcji [mirrordungeon_starlight_personality_title] — tekst] 별빛 보존 대상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_starlight_personality_title].content
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Tryby lochów i Kolei Refrakcji [mirrordungeon_starlight_personality_desc] — tekst] 별빛 보존 기간 동안 해당 인격으로 거울 던전 클리어 시 별빛 보너스가 소모되지 않습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_starlight_personality_desc].content
   limit: do 150 znaków
   EN: For the retention duration, these units' Starlight Bonuses will not be spent upon clearing a Mirror Dungeon run.
   PL: W okresie zachowania ukończenie Lustrzanego Lochu tymi Tożsamościami nie zużywa ich Premii Gwiezdnego Blasku.
44. [Tryby lochów i Kolei Refrakcji [combine_egogift_not_allow] — tekst] 선택 불가
   źródło: MirrorDungeonUI_6.json :: dataList[id=combine_egogift_not_allow].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
45. [Tryby lochów i Kolei Refrakcji [number_of_cleared_hard_floors] — tekst] 하드 팩 클리어 층 수
   źródło: MirrorDungeonUI_6.json :: dataList[id=number_of_cleared_hard_floors].content
   limit: do 120 znaków
   EN: Hard Pack Floors Cleared
   PL: Piętra ukończone z pakietem Trudnym
46. [Tryby lochów i Kolei Refrakcji [mirror_starlight_unlock_condition_lack_of_current_point] — tekst] 별빛 부족
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_unlock_condition_lack_of_current_point].content
   (powtórzenie elementu 30 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
47. [Tryby lochów i Kolei Refrakcji [mirror_starlight_unlock_condition_needs_held_buff_points] — tekst] 별빛 {0}이상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_unlock_condition_needs_held_buff_points].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: At {0}+ Starlight
   PL: Gwiezdny Blask min. {0}
48. [Tryby lochów i Kolei Refrakcji [mirror_cleared_floor_count_over_6] — tekst] 평행중첩 모드 적용 클리어 층 수
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_cleared_floor_count_over_6].content
   limit: do 120 znaków
   EN: Parallel Superposition Floors Cleared
   PL: Piętra ukończone w Superpozycji Równoległej
49. [Tryby lochów i Kolei Refrakcji [mirror_cleared_railway_theme_pack_count] — tekst] 거울굴절철도 테마팩 클리어 수
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_cleared_railway_theme_pack_count].content
   limit: do 120 znaków
   EN: Refraction Railway Packs Cleared
   PL: Ukończone pakiety Kolei Załamania
50. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_title_md6] — tekst] 영생 별의 가호
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_start_buff_Panel_title_md6].content
   limit: do 120 znaków
   EN: Grace of the Immortal Star
   PL: Błogosławieństwo Nieśmiertelnej Gwiazdy
51. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_card_enhancement] — tekst] 강화
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_start_buff_card_enhancement].content
   limit: do 120 znaków
   EN: Enhance
   PL: Ulepsz
52. [Tryby lochów i Kolei Refrakcji [mirror_user_starlight_buff] — tekst] 별의 가호
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_user_starlight_buff].content
   limit: do 120 znaków
   EN: Grace of Stars
   PL: Błogosławieństwo Gwiazd
53. [Tryby lochów i Kolei Refrakcji [mirror_unobservable_egogift_reason] — tekst] 관측 불가
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_unobservable_egogift_reason].content
   limit: do 120 znaków
   EN: Unobservable
   PL: Obserwacja niemożliwa
54. [Tryby lochów i Kolei Refrakcji [mirror_unobservable_egogift_reason_is_owned] — tekst] 보유 중
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_unobservable_egogift_reason_is_owned].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadany
55. [Tryby lochów i Kolei Refrakcji [mirror_start_buff_purchase_modal_check_box] — tekst] 별빛을 코스트로 전환
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_start_buff_purchase_modal_check_box].content
   limit: do 120 znaków
   EN: Convert Starlight to Cost
   PL: Zamień Gwiezdny Blask na Koszt
56. [Tryby lochów i Kolei Refrakcji [mirrordungeon_additional_reserved_starlight_from_startBuff] — tekst] 사용하지 않은 별빛이 클리어 보상으로 이월되었습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirrordungeon_additional_reserved_starlight_from_startBuff].content
   limit: do 120 znaków
   EN: Unused Starlight have been added to the Clear Rewards.
   PL: Niewykorzystany Gwiezdny Blask został przeniesiony do nagród za ukończenie.
57. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_base_point] — tekst] 기본
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_base_point].content
   limit: do 120 znaków
   EN: Default
   PL: Podstawa
58. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus] — tekst] 편성 보너스
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus].content
   limit: do 120 znaków
   EN: Loadout Bonus
   PL: Premia składu
59. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_battle_reward_card] — tekst] 전투 보상 카드
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_battle_reward_card].content
   limit: do 120 znaków
   EN: Encounter Reward Cards
   PL: Karty nagród za walkę
60. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_points_on_start] — tekst] 시작 별빛 소모
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_points_on_start].content
   limit: do 120 znaków
   EN: Starting Starlight Spent
   PL: Gwiezdny Blask zużyty na starcie
61. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_dungeon_play_point] — tekst] 탐사 점수
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_dungeon_play_point].content
   limit: do 120 znaków
   EN: Exploration Score
   PL: Punkty eksploracji
62. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier] — tekst] 편성 보너스 배율
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier].content
   limit: do 120 znaków
   EN: Loadout Bonus Mult.
   PL: Mnożnik premii składu
63. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_during_dungeon_play] — tekst] 진행 중 소모
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_during_dungeon_play].content
   limit: do 120 znaków
   EN: Spent in Dungeon
   PL: Zużyto w trakcie wyprawy
64. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_owned_before_enter_dungeon] — tekst] 기존 보유
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_owned_before_enter_dungeon].content
   limit: do 120 znaków
   EN: Pre-dungeon Reserve
   PL: Zapas przed wejściem
65. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_reward_point] — tekst] 보상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_reward_point].content
   limit: do 120 znaków
   EN: Reward
   PL: Nagroda
66. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_total_owned_point_after_dungeon_play] — tekst] 총 보유 수량
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_total_owned_point_after_dungeon_play].content
   limit: do 120 znaków
   EN: Net Amount
   PL: Łączny stan posiadania
67. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_tooltip_button] — tekst] 상세 내역
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_tooltip_button].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
68. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_points_on_start_tooltip_title] — tekst] 시작 별빛 소모
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_points_on_start_tooltip_title].content
   (powtórzenie elementu 60 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
69. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_points_on_start_tooltip_item_purchased] — tekst] 별의 가호 구매
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_points_on_start_tooltip_item_purchased].content
   limit: do 120 znaków
   EN: Grace of Stars Purchased
   PL: Zakup Błogosławieństw Gwiazd
70. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_points_on_start_tooltip_item_converted_to_cost] — tekst] 코스트 전환
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_points_on_start_tooltip_item_converted_to_cost].content
   limit: do 120 znaków
   EN: Converted to Cost
   PL: Zamiana na Koszt
71. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_dungeon_play_point_tooltip_title] — tekst] 탐사 점수 상세
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_dungeon_play_point_tooltip_title].content
   limit: do 120 znaków
   EN: Exploration Score Details
   PL: Szczegóły punktów eksploracji
72. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_dungeon_play_point_tooltip_item_cleared_floor] — tekst] 클리어 층
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_dungeon_play_point_tooltip_item_cleared_floor].content
   limit: do 120 znaków
   EN: Cleared Floors
   PL: Ukończone piętra
73. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_dungeon_play_point_tooltip_item_hard_difficulty] — tekst] 하드 난이도
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_dungeon_play_point_tooltip_item_hard_difficulty].content
   limit: do 120 znaków
   EN: Hard Difficulty
   PL: Poziom Trudny
74. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_dungeon_play_point_tooltip_item_railway_theme_pack] — tekst] 거울굴절철도 테마팩
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_dungeon_play_point_tooltip_item_railway_theme_pack].content
   limit: do 120 znaków
   EN: Refraction Railway Theme Pack
   PL: Pakiet Kolei Załamania
75. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier_tooltip_title] — tekst] 편성 별빛 보너스 배율
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier_tooltip_title].content
   limit: do 120 znaków
   EN: Loadout Starlight Bonus Mult.
   PL: Mnożnik Premii Gwiezdnego Blasku składu
76. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier_tooltip_item_desc] — tekst] ※ 소수점은 버림하여 처리됩니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier_tooltip_item_desc].content
   limit: do 120 znaków
   EN: ※ Rounded down.
   PL: ※ Wartości ułamkowe są zaokrąglane w dół.
77. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_consumed_during_dungeon_play_tooltip_title] — tekst] 진행 중 소모
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_consumed_during_dungeon_play_tooltip_title].content
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
78. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier_tooltip_item_detect_theme_pack] — tekst] 테마팩 관측
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier_tooltip_item_detect_theme_pack].content
   limit: do 120 znaków
   EN: Theme Pack Observation
   PL: Obserwacja Pakietów Tematycznych
79. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier_tooltip_item_combine_ego_gift] — tekst] 소원 빌기
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier_tooltip_item_combine_ego_gift].content
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
80. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_total_consumed_point] — tekst] 총 소모량
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_total_consumed_point].content
   limit: do 120 znaków
   EN: Sum Expenditure
   PL: Łączne zużycie
81. [Tryby lochów i Kolei Refrakcji [mirror_hard_recommended_level_popup_desctiption] — tekst] 편성 인격의 현재 평균 레벨이 권장 레벨보다 <color=#990000>낮습니다.</color>\n전투를 진행하시겠습니까?
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_hard_recommended_level_popup_desctiption].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: The current average level of Identities in your loadout is <color=#990000>lower</color> than the recommended level.\nProceed anyway?
   PL: Średni poziom wybranych Tożsamości jest <color=#990000>niższy</color> od zalecanego.\nRozpocząć walkę mimo to?
82. [Tryby lochów i Kolei Refrakcji [mirror_hard_recommended_level_popup_detail_desctiption] — tekst] 현재 평균 레벨: {0}\n<color=#f8c200>권장 레벨: {1}</color>
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_hard_recommended_level_popup_detail_desctiption].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, \n
   EN: Current Avg. Level: {0}\n<color=#f8c200>Recommended Level: {1}</color>
   PL: Obecny śr. poziom: {0}\n<color=#f8c200>Zalecany poziom: {1}</color>
83. [Tryby lochów i Kolei Refrakcji [mirror_observation_ego_gift_select_list] — tekst] 선택한 E.G.O 기프트
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_ego_gift_select_list].content
   limit: do 120 znaków
   EN: Selected E.G.O Gift
   PL: Wybrane Dary E.G.O
84. [Tryby lochów i Kolei Refrakcji [mirror_observation_ego_gift_title] — tekst] E.G.O 기프트 관측
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_ego_gift_title].content
   limit: do 120 znaków
   EN: E.G.O Gift Search
   PL: Obserwacja Darów E.G.O
85. [Tryby lochów i Kolei Refrakcji [mirror_observation_ego_gift_confirm] — tekst] 선택
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_ego_gift_confirm].content
   limit: do 120 znaków
   EN: Select
   PL: Wybierz
86. [Tryby lochów i Kolei Refrakcji [mirror_observation_have_starlight] — tekst] 보유
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_have_starlight].content
   limit: do 120 znaków
   EN: Owned
   PL: Posiadane
87. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_give_up_ego_gift_observation] — tekst] E.G.O 기프트 관측을 진행하지 않으시겠습니까?
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_give_up_ego_gift_observation].content
   limit: do 120 znaków
   EN: Forgo E.G.O Gift Search?
   PL: Pominąć Obserwację Darów E.G.O?
88. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_confirm_ego_gift_observation] — tekst] 별빛 {0}개를 소모하여 E.G.O 기프트 관측을 진행하시겠습니까?
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_confirm_ego_gift_observation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Consume {0} Starlight to search and obtain these E.G.O Gifts?
   PL: Wydać {0} Gwiezdnego Blasku, aby przeprowadzić Obserwację Darów E.G.O?
89. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_observation_filter_reset] — tekst] 초기화
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_observation_filter_reset].content
   limit: do 120 znaków
   EN: Reset
   PL: Resetuj
90. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_formation_bonus_multiplier_tooltip_item_detect_egogift] — tekst] E.G.O 기프트 관측
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_starlight_result_formation_bonus_multiplier_tooltip_item_detect_egogift].content
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Tryby lochów i Kolei Refrakcji [mirror_observation_ego_gift_title_toggle] — tekst] 기프트 관측\n활성화
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_ego_gift_title_toggle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Activate Gift\nSearch
   PL: Aktywuj Obserwację\nDarów
92. [Tryby lochów i Kolei Refrakcji [mirror_observation_lack_starlight_title] — tekst] 기프트 관측\n활성화 불가
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_lack_starlight_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot Search\nGifts
   PL: Obserwacja Darów\nniedostępna
93. [Tryby lochów i Kolei Refrakcji [mirror_observation_lack_starlight_desc] — tekst] 사용 가능한 별빛이 기프트 관측에서 필요한 양보다 적습니다
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_observation_lack_starlight_desc].content
   limit: do 120 znaków
   EN: You do not have enough Starlight for this Gift Search.
   PL: Masz za mało dostępnego Gwiezdnego Blasku do Obserwacji Darów.
94. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_selected_startBuff] — tekst] 선택 별의 가호
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_selected_startBuff].content
   limit: do 120 znaków
   EN: Selected Grace of Stars
   PL: Wybrane Błogosławieństwa Gwiazd
95. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_not_selected_startBuff] — tekst] 선택된 별의 가호가 없습니다
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_not_selected_startBuff].content
   limit: do 120 znaków
   EN: No Grace of Stars Selected
   PL: Nie wybrano Błogosławieństw Gwiazd
96. [Tryby lochów i Kolei Refrakcji [InfinityFloor_Extreme_CheckEnter_Modal_Title] — tekst] 평행중첩 EXTREME 모드
   źródło: MirrorDungeonUI_6.json :: dataList[id=InfinityFloor_Extreme_CheckEnter_Modal_Title].content
   limit: do 120 znaków
   EN: Parallel Superposition EXTREME
   PL: Superpozycja Równoległa EXTREME
97. [Tryby lochów i Kolei Refrakcji [InfinityFloor_Extreme_CheckEnter_Modal_Desc] — tekst] EXTREME 모드를 추가 적용할 수 있습니다.\n\nEXTREME 모드를 적용하여\n다음 층으로 이동하시겠습니까?
   źródło: MirrorDungeonUI_6.json :: dataList[id=InfinityFloor_Extreme_CheckEnter_Modal_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can enter the EXTREME Mode.\n\nEnter the EXTREME Mode and proceed to the next floor?
   PL: Możesz dodatkowo włączyć tryb EXTREME.\n\nAktywować tryb EXTREME\ni przejść na następne piętro?
98. [Tryby lochów i Kolei Refrakcji [mirror_constrain_buff] — tekst] 제약
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_constrain_buff].content
   limit: do 120 znaków
   EN: Adversity
   PL: Utrudnienia
99. [Tryby lochów i Kolei Refrakcji [mirror_constraint_button] — tekst] 도전
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_constraint_button].content
   limit: do 120 znaków
   EN: Challenge
   PL: Wyzwanie
100. [Tryby lochów i Kolei Refrakcji [mirror_select_constraint_title] — tekst] 제약 설정
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_select_constraint_title].content
   limit: do 120 znaków
   EN: Set Adversities
   PL: Ustawienia Utrudnień
101. [Tryby lochów i Kolei Refrakcji [mirror_select_constraint_slot_achievement] — tekst] 달성
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_select_constraint_slot_achievement].content
   limit: do 120 znaków
   EN: Completed
   PL: Ukończone
102. [Tryby lochów i Kolei Refrakcji [mirror_select_constraint_slot_unachieved] — tekst] 미달성
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_select_constraint_slot_unachieved].content
   limit: do 120 znaków
   EN: Incomplete
   PL: Nieukończone
103. [Tryby lochów i Kolei Refrakcji [mirror_select_constraint_slot_reward_title] — tekst] 제약 보상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_select_constraint_slot_reward_title].content
   limit: do 120 znaków
   EN: Adversity Rewards
   PL: Nagrody za Utrudnienia
104. [Tryby lochów i Kolei Refrakcji [mirror_hidden_stage_information_quit_button] — tekst] 이탈
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_hidden_stage_information_quit_button].content
   limit: do 120 znaków
   EN: Skip
   PL: Omiń
105. [Tryby lochów i Kolei Refrakcji [mirror_hidden_stage_information_enter_button] — tekst] 입장
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_hidden_stage_information_enter_button].content
   limit: do 120 znaków
   EN: Enter
   PL: Wejdź
106. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_battle_pass_exp_label_name_format] — tekst] 시즌 {0} 배틀 패스
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_battle_pass_exp_label_name_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0} Battle Pass
   PL: Przepustka Bitewna Sezonu {0}
107. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_exp_reward_label] — tekst] 보상
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_exp_reward_label].content
   (powtórzenie elementu 65 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_exp_reward_label_name_format] — tekst] 영생의 거울 투영
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_exp_reward_label_name_format].content
   limit: do 120 znaków
   EN: Mirror of Immortality Projection
   PL: Projekcja Lustra Nieśmiertelności
109. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_constraint_bonus_starlight] — tekst] 제약 보너스
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_constraint_bonus_starlight].content
   limit: do 120 znaków
   EN: Adversity Bonus
   PL: Premia za Utrudnienia
110. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_constraint_bonus_starlight_tooltip_title] — tekst] 제약 보너스 배율
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_constraint_bonus_starlight_tooltip_title].content
   limit: do 120 znaków
   EN: Adversity Bonus Mult.
   PL: Mnożnik premii za Utrudnienia
111. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_constraint_bonus_starlight_tooltip_desc] — tekst] 제약 점수
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_constraint_bonus_starlight_tooltip_desc].content
   limit: do 120 znaków
   EN: Adversity Score
   PL: Punkty Utrudnień
112. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_reward_popup_exp_limit] — tekst] 주간 획득 가능 투영도
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_reward_popup_exp_limit].content
   limit: do 120 znaków
   EN: Weekly Projection Cap
   PL: Tygodniowy limit Stopnia Projekcji
113. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_reward_popup_mirror_pass_exp] — tekst] 투영도
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_reward_popup_mirror_pass_exp].content
   limit: do 120 znaków
   EN: Projection Rate
   PL: Stopień Projekcji
114. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_default] — tekst] 기본
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_default].content
   (powtórzenie elementu 57 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
115. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_infinite] — tekst] 평행 중첩
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_infinite].content
   limit: do 120 znaków
   EN: Parallel Superposition
   PL: Superpozycja Równoległa
116. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_constraint_bonus] — tekst] 제약 보너스
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_constraint_bonus].content
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
117. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_weekly_limit] — tekst] 주간 제한 도달
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_weekly_limit].content
   limit: do 120 znaków
   EN: Weekly Cap Reached
   PL: Osiągnięto limit tygodniowy
118. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_total] — tekst] 합계
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_total].content
   limit: do 120 znaków
   EN: Sum
   PL: Suma
119. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_detail_weekly_limit_tag] — tekst] 주간 제한량
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_mirror_pass_detail_weekly_limit_tag].content
   limit: do 120 znaków
   EN: Weekly Cap
   PL: Limit tygodniowy
120. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_constraint_section_title] — tekst] 선택한 제약
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_constraint_section_title].content
   limit: do 120 znaków
   EN: Selected Adversities
   PL: Wybrane Utrudnienia
121. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_enemy_buff_section_title] — tekst] 선택한 고난
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_enemy_buff_section_title].content
   limit: do 120 znaków
   EN: Selected Trials
   PL: Wybrane Próby
122. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_select_constraint_accumulated_score] — tekst] 누적 제약 점수
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_select_constraint_accumulated_score].content
   limit: do 120 znaków
   EN: Cumulative Adversity Score
   PL: Łączne punkty Utrudnień
123. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_popup_reward_preview_button] — tekst] 진행 현황
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_progress_popup_reward_preview_button].content
   limit: do 120 znaków
   EN: Progress
   PL: Stan wyprawy
124. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_preview_version_confirm_button] — tekst] 닫기
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_preview_version_confirm_button].content
   limit: do 120 znaków
   EN: Close
   PL: Zamknij
125. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_preview_version_title] — tekst] 탐사 진행중
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_preview_version_title].content
   limit: do 120 znaków
   EN: Exploring
   PL: Wyprawa w toku
126. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_preview_version_last_sector_label] — tekst] 현재 탐사 구역
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_preview_version_last_sector_label].content
   limit: do 120 znaków
   EN: Current Area
   PL: Bieżący obszar
127. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_finished_panel_preview_version_progress_percent_label] — tekst] 현재 진행도
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_finished_panel_preview_version_progress_percent_label].content
   limit: do 120 znaków
   EN: Current Progress
   PL: Bieżący postęp
128. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_return_title] — tekst] 스테이지 입장 화면으로 이동
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_return_title].content
   limit: do 120 znaków
   EN: Return to Stage Select
   PL: Wróć do ekranu wejścia na etap
129. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_return_desc] — tekst] 스테이지 입장 화면으로 이동합니다.\n편성 순서를 다시 설정할 수 있습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_return_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Return to the Stage Select menu.\nYou can adjust your Deployment order before entering this Section again.
   PL: Powrót do ekranu wejścia na etap.\nMożesz ponownie ustawić kolejność wystawienia.
130. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_retry_title] — tekst] 스테이지 재도전
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_retry_title].content
   limit: do 120 znaków
   EN: Retry Stage
   PL: Ponów etap
131. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_retry_desc] — tekst] 스테이지를 재도전하여 첫 번째 웨이브부터 다시 시작합니다. 편성창에서 지정한 편성 순서가 유지됩니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_retry_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Retry Stage and start over from the first wave of the Stage.\nYour Deployment order will not be changed.
   PL: Ponawia etap od pierwszej fali.\nKolejność wystawienia wybrana w oknie składu zostaje zachowana.
132. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_accept_title] — tekst] 결과 반영 후 스테이지 입장 화면으로 이동
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_accept_title].content
   limit: do 120 znaków
   EN: Accept results and return to Stage select
   PL: Zapisz wynik i wróć do ekranu etapu
133. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_accept_desc] — tekst] 수감자 사망 등 현재 전투 결과를 반영하고 스테이지 입장 화면으로 이동합니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_accept_desc].content
   limit: do 130 znaków
   EN: Accept the current battle results such as Sinner deaths, and return to the Stage select menu.
   PL: Zachowuje bieżący wynik walki (w tym poległych Grzeszników) i wraca do ekranu wejścia na etap.
134. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_current_floor] — tekst] 현재 진행 층
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_current_floor].content
   limit: do 120 znaków
   EN: Floor In Progress
   PL: Bieżące piętro
135. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_desc] — tekst] 전투에 참여한 모든 수감자가 사망했습니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_desc].content
   limit: do 120 znaków
   EN: All participating Sinners have been killed.
   PL: Wszyscy Grzesznicy biorący udział w walce polegli.
136. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ask_after_defeat_remain_unit_desc] — tekst] 현재 남은 인원:
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_ask_after_defeat_remain_unit_desc].content
   limit: do 120 znaków
   EN: Remaining Units:
   PL: Pozostali uczestnicy:
137. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hidden_stage_title] — tekst] 차원 반전 구역 - 인식 오류 주의
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_hidden_stage_title].content
   limit: do 120 znaków
   EN: Dimension Reversal Zone - COGNITION ERROR WARNING
   PL: Strefa Odwrócenia Wymiaru — UWAGA: BŁĄD POZNAWCZY
138. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_hidden_stage_description] — tekst] 입장할 경우,\n해당 스테이지의 전투를 클리어할 때까지\n스테이지를 이탈 할 수 없습니다.\n\n입장하시겠습니까?\n※클리어 시, 모든 아군이 부활 및 최대 체력으로 회복됩니다.
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_hidden_stage_description].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upon entry, you will not be able to leave the Stage until its Combat Encounter is cleared.\n\nEnter anyway?\n※ Clearing this Stage will heal allies to their max HP and revive any defeated allies.
   PL: Po wejściu\nnie będzie można opuścić tego etapu\naż do ukończenia walki.\n\nWejść mimo to?\n※ Po ukończeniu wszyscy polegli sojusznicy zostaną wskrzeszeni, a cała drużyna w pełni uleczona.
139. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_revive_after_hidden_boss_alarm] — tekst] 사망한 아군이 부활하고 모든 아군이 회복되었습니다
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_revive_after_hidden_boss_alarm].content
   limit: do 120 znaków
   EN: All allies have been fully healed, and defeated allies have been revived
   PL: Wskrzeszono poległych sojuszników i uleczono całą drużynę
140. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_floor_format] — tekst] {0}층
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_finished_panel_floor_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}F
   PL: {0}. piętro
141. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_auto_participate_order_adjustment_notice] — tekst] 아군 부활을 통한 편성 순서가 재조정되었습니다
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_auto_participate_order_adjustment_notice].content
   limit: do 120 znaków
   EN: Deployment Order has been restored via ally revival.
   PL: Kolejność wystawienia została przywrócona po wskrzeszeniu sojuszników
142. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_option_participation_modification] — tekst] 거울 던전 전투 편성 순서 자동 조정
   źródło: MirrorDungeonUI_6.json :: dataList[id=mirror_dungeon_option_participation_modification].content
   limit: do 120 znaków
   EN: Auto-Restore MD Deployment Order
   PL: Automatyczne przywracanie kolejności składu w Lustrzanych Lochach

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_6_Achievement
- plik gry: `MirrorDungeonUI_6_Achievement.json`

143. [Tryby lochów i Kolei Refrakcji [mirrordungeon6_mission_date] — tekst] 거울 던전 7 업데이트 전까지 보상을 수령할 수 있습니다.
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon6_mission_date].content
   limit: do 120 znaków
   EN: The rewards can be claimed until before the Mirror Dungeon #7 Update.
   PL: Nagrody można odebrać do aktualizacji Lustrzanego Lochu #7.
144. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_COLLECTION] — tekst] 수집
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_COLLECTION].content
   limit: do 120 znaków
   EN: Collection
   PL: Kolekcja
145. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_CLEAR] — tekst] 클리어
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_CLEAR].content
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
146. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_DECK] — tekst] 편성
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_DECK].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
147. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_SHOP] — tekst] 상점
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_SHOP].content
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_BATTLE] — tekst] 전투
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_BATTLE].content
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_EXTREME] — tekst] 제약 - 익스트림
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_EXTREME].content
   limit: do 120 znaków
   EN: Adversity - EXTREME
   PL: Utrudnienia — EXTREME
150. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_ALL] — tekst] 달성도
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_ALL].content
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON6_HIDDEN] — tekst] 히든
   źródło: MirrorDungeonUI_6_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON6_HIDDEN].content
   limit: do 120 znaków
   EN: Hidden
   PL: Ukryte

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_7
- plik gry: `MirrorDungeonUI_7.json`

152. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_tooltip_item_refresh_egogift] — tekst] E.G.O 기프트 새로고침
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_starlight_result_tooltip_item_refresh_egogift].content
   limit: do 120 znaków
   EN: E.G.O Gift Refresh
   PL: Odświeżenie Darów E.G.O
153. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_7] — tekst] 이름과 거미의 거울 {0}층
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_progress_text_7].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mirror of Names and Spiders - F{0}
   PL: Lustro Imion i Pająków — {0}. piętro
154. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_notice_desc_cannot_refresh_by_lack_of_egogift_pool] — tekst] 새로고침 가능한 E.G.O 기프트가 없습니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_notice_desc_cannot_refresh_by_lack_of_egogift_pool].content
   limit: do 120 znaków
   EN: No E.G.O Gifts available for Refresh.
   PL: Brak dostępnych Darów E.G.O do odświeżenia.
155. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_notice_desc_cannot_refresh_by_lack_of_starlight] — tekst] 새로고침에 필요한 별빛이 부족합니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_notice_desc_cannot_refresh_by_lack_of_starlight].content
   limit: do 120 znaków
   EN: Not enough Starlight for Refresh.
   PL: Za mało Gwiezdnego Blasku do odświeżenia.
156. [Tryby lochów i Kolei Refrakcji [mirrordungeon_ego_gift_sort_by_acquired_order] — tekst] 획득 순
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirrordungeon_ego_gift_sort_by_acquired_order].content
   limit: do 120 znaków
   EN: Recent
   PL: Wg zdobycia
157. [Tryby lochów i Kolei Refrakcji [mirrordungeon_shop_change_skill_popup_skill_pool_desc] — tekst] 스킬 보유 현황
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirrordungeon_shop_change_skill_popup_skill_pool_desc].content
   limit: do 120 znaków
   EN: Skills Owned
   PL: Posiadane umiejętności
158. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_title_md7] — tekst] 이름과 거미 별의 가호
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_start_buff_Panel_title_md7].content
   limit: do 120 znaków
   EN: Grace of the Star of Names and Spiders
   PL: Błogosławieństwo Gwiazdy Imion i Pająków
159. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_acquire_material_ego_gift_by_start_buff_notice] — tekst] 별의 가호 <{0}>효과로 잔영 획득
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_acquire_material_ego_gift_by_start_buff_notice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Grace of Stars <{0}> Activated: Gained Vestige(s)
   PL: Błogosławieństwo Gwiazd <{0}>: zdobyto Powidok
160. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_blocked_7] — tekst] 8장 클리어 시 개방됩니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirrordungeon_theme_hard_blocked_7].content
   limit: do 120 znaków
   EN: Clear Canto VIII to Unlock.
   PL: Odblokowanie po ukończeniu Canto VIII.
161. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_cursed_to_blessing_remain_count] — tekst] (현재 {0}회)
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_cursed_to_blessing_remain_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ({0} battles won)
   PL: (obecnie: {0})
162. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_free_refresh_side_popup] — tekst] 무료 새로고침
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_shop_free_refresh_side_popup].content
   limit: do 120 znaków
   EN: Free Refresh
   PL: Darmowe odświeżenie
163. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_refresh_cost_returned_side_popup] — tekst] 새로고침 비용 반환
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_shop_refresh_cost_returned_side_popup].content
   limit: do 120 znaków
   EN: Refresh Cost Refunded
   PL: Zwrócono koszt odświeżenia
164. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_select_all] — tekst] 가호 전체 선택
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_start_buff_select_all].content
   limit: do 120 znaków
   EN: Select All Graces
   PL: Wybierz wszystkie Błogosławieństwa
165. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_select_all_level] — tekst] 전체 강화
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_start_buff_select_all_level].content
   limit: do 120 znaków
   EN: Enhance All
   PL: Ulepsz wszystkie
166. [Tryby lochów i Kolei Refrakcji [dungeon_shop_detect_personality_skill] — tekst] 인격 스킬 관측
   źródło: MirrorDungeonUI_7.json :: dataList[id=dungeon_shop_detect_personality_skill].content
   limit: do 120 znaków
   EN: ID Skill Search
   PL: Obserwacja umiejętności Tożsamości
167. [Tryby lochów i Kolei Refrakcji [ui_blocker_mirror_dungeon_detect_personality_skill] — tekst] 스킬을 교체할 수감자를 선택해주세요.
   źródło: MirrorDungeonUI_7.json :: dataList[id=ui_blocker_mirror_dungeon_detect_personality_skill].content
   limit: do 120 znaków
   EN: Select a Sinner for Skill Replacement.
   PL: Wybierz Grzesznika do wymiany umiejętności.
168. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_back_to_heal_again_button] — tekst] 추가로 회복시킨다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_shop_back_to_heal_again_button].content
   limit: do 120 znaków
   EN: Heal again.
   PL: Ulecz ponownie.
169. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_back_to_heal_again_button_desc] — tekst] 회복 유형 선택
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_shop_back_to_heal_again_button_desc].content
   limit: do 120 znaków
   EN: Return to healing type selection
   PL: Wybór rodzaju leczenia
170. [Tryby lochów i Kolei Refrakcji [purchase_personality_skill_by_starlight_desc] — tekst] 별빛 <color=#f8c200>{0}</color>을 소모하여 교체하시겠습니까?
   źródło: MirrorDungeonUI_7.json :: dataList[id=purchase_personality_skill_by_starlight_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}
   EN: Spend <color=#f8c200>{0}</color> Starlight to replace this Skill?
   PL: Wydać <color=#f8c200>{0}</color> Gwiezdnego Blasku, aby wymienić umiejętność?
171. [Tryby lochów i Kolei Refrakcji [mirror_starlight_result_tooltip_item_detect_personality_skill] — tekst] 인격 스킬 관측
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_starlight_result_tooltip_item_detect_personality_skill].content
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_shop_cannot_detect_personality_skill_desc] — tekst] 구매 불가
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_shop_cannot_detect_personality_skill_desc].content
   limit: do 120 znaków
   EN: Cannot Purchase
   PL: Zakup niemożliwy
173. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_combine_panel_combinable_egoGift_tag] — tekst] 합성 가능
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_combine_panel_combinable_egoGift_tag].content
   limit: do 120 znaków
   EN: Fusion Available
   PL: Możliwa Synteza
174. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_combine_panel_owned_egoGift_tag] — tekst] 보유 E.G.O 기프트
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_combine_panel_owned_egoGift_tag].content
   limit: do 120 znaków
   EN: E.G.O Gifts Owned
   PL: Posiadane Dary E.G.O
175. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_notice_desc_already_upgraded_ego_gift] — tekst] 현재 강화 상태로 강화할 수 없습니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_notice_desc_already_upgraded_ego_gift].content
   limit: do 120 znaków
   EN: Cannot Enhance to the same Tier.
   PL: Nie można ulepszyć do obecnego stopnia ulepszenia.
176. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_notice_desc_cannot_upgrade_ego_gift_by_low_cost] — tekst] 강화에 필요한 코스트가 부족합니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_notice_desc_cannot_upgrade_ego_gift_by_low_cost].content
   limit: do 120 znaków
   EN: You need more Cost to Enhance this E.G.O Gift.
   PL: Za mało Kosztu do ulepszenia Daru E.G.O.
177. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_notice_desc_not_exist_level] — tekst] 해당 단계로 강화할 수 없는 기프트입니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_notice_desc_not_exist_level].content
   limit: do 120 znaków
   EN: Cannot be Enhanced to the selected Tier.
   PL: Tego Daru nie można ulepszyć do wybranego stopnia.
178. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_upgrade_level] — tekst] 강화 단계
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_upgrade_level].content
   limit: do 120 znaków
   EN: Enhancement Tier
   PL: Stopień ulepszenia
179. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_cannot_combine] — tekst] 합성 불가
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_cannot_combine].content
   limit: do 120 znaków
   EN: Cannot Fuse
   PL: Synteza niemożliwa
180. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_will_be_uncombineable] — tekst] 합성 불가[얽힘]
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_will_be_uncombineable].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fusion Disabled\n[Entanglement]
   PL: Synteza niemożliwa\n[Splot]
181. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_side_popup_cannot_combine_requireds_prior_combine] — tekst] 해당 기프트를 바로 조합하기 위한 합성 칸이 부족합니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_side_popup_cannot_combine_requireds_prior_combine].content
   limit: do 120 znaków
   EN: Not enough Fusion slots to immediately Fuse this E.G.O Gift.
   PL: Za mało miejsc Syntezy, aby od razu połączyć ten Dar.
182. [Tryby lochów i Kolei Refrakcji [mirror_finished_panel_mirror_pass_exp_reward_label_name_format_base] — tekst] {0} 투영
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_finished_panel_mirror_pass_exp_reward_label_name_format_base].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Projection
   PL: Projekcja: {0}
183. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_sort_by_id] — tekst] 기본 정렬
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_sort_by_id].content
   limit: do 120 znaków
   EN: Default
   PL: Domyślnie
184. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_sort_by_tier] — tekst] 등급
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_sort_by_tier].content
   limit: do 120 znaków
   EN: Tier
   PL: Ranga
185. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_keyword_filter] — tekst] 필터 - 키워드
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_keyword_filter].content
   limit: do 120 znaków
   EN: Filter - Keyword
   PL: Filtr — słowo kluczowe
186. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_acquire_status_filter] — tekst] 필터 - 획득 현황
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_acquire_status_filter].content
   limit: do 120 znaków
   EN: Filter - Acquisition
   PL: Filtr — stan posiadania
187. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_acquire_status_filter_content_0] — tekst] 획득
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_acquire_status_filter_content_0].content
   limit: do 120 znaków
   EN: Acquired
   PL: Zdobyte
188. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_acquire_status_filter_content_1] — tekst] 미획득
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_acquire_status_filter_content_1].content
   limit: do 120 znaków
   EN: Unacquired
   PL: Niezdobyte
189. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_inventory_no_owned_ego_gift] — tekst] 보유 E.G.O 기프트 없음
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_inventory_no_owned_ego_gift].content
   limit: do 120 znaków
   EN: No E.G.O Gifts Owned
   PL: Brak posiadanych Darów E.G.O
190. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_no_owned_ego_gift] — tekst] 보유 E.G.O 기프트 없음
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_no_owned_ego_gift].content
   (powtórzenie elementu 189 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_card_theme_appear_floor] — tekst] 등장 층
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_card_theme_appear_floor].content
   limit: do 120 znaków
   EN: Featured Floors
   PL: Piętra występowania
192. [Tryby lochów i Kolei Refrakcji [EgoGiftListPopupTabType_OWNED_WITH_DETAIL_TAG] — tekst] 보유
   źródło: MirrorDungeonUI_7.json :: dataList[id=EgoGiftListPopupTabType_OWNED_WITH_DETAIL_TAG].content
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Tryby lochów i Kolei Refrakcji [EgoGiftListPopupTabType_CLEAR_THEME_REWARD] — tekst] 클리어 보상
   źródło: MirrorDungeonUI_7.json :: dataList[id=EgoGiftListPopupTabType_CLEAR_THEME_REWARD].content
   limit: do 120 znaków
   EN: Clear Rewards
   PL: Nagrody za ukończenie
194. [Tryby lochów i Kolei Refrakcji [EgoGiftListPopupTabType_THEME_LIMITED_EGO_GIFT] — tekst] 현재 팩 한정
   źródło: MirrorDungeonUI_7.json :: dataList[id=EgoGiftListPopupTabType_THEME_LIMITED_EGO_GIFT].content
   limit: do 120 znaków
   EN: Current Theme Pack-Exclusive
   PL: Wyłącznie w tym pakiecie
195. [Tryby lochów i Kolei Refrakcji [EgoGiftListPopupTabType_EGO_GIFT_POOL_IN_CURRENT_THEME] — tekst] 등장 가능
   źródło: MirrorDungeonUI_7.json :: dataList[id=EgoGiftListPopupTabType_EGO_GIFT_POOL_IN_CURRENT_THEME].content
   limit: do 120 znaków
   EN: Featured
   PL: Dostępne
196. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_owned_scroll_tag_default] — tekst] 통상
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_owned_scroll_tag_default].content
   limit: do 120 znaków
   EN: Regular
   PL: Zwykłe
197. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_owned_scroll_tag_theme_limited] — tekst] 테마 팩 한정
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_owned_scroll_tag_theme_limited].content
   limit: do 120 znaków
   EN: Theme Pack-Exclusive
   PL: Wyłącznie w pakiecie
198. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_clear_scroll_tag_theme_limited] — tekst] 테마 팩 한정
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_clear_scroll_tag_theme_limited].content
   (powtórzenie elementu 197 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
199. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_clear_scroll_tag_theme_default] — tekst] 통상
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_clear_scroll_tag_theme_default].content
   (powtórzenie elementu 196 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
200. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_theme_limited_scroll_tag_theme_limited] — tekst] 현재 테마 팩 한정
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_theme_limited_scroll_tag_theme_limited].content
   limit: do 120 znaków
   EN: Current Theme Pack-Exclusive
   PL: Wyłącznie w bieżącym pakiecie
201. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_combine_scroll_tag_theme_limited] — tekst] 테마팩 한정
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_combine_scroll_tag_theme_limited].content
   limit: do 120 znaków
   EN: Theme Pack-Exclusive
   PL: Wyłącznie w pakiecie
202. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_combine_scroll_tag_theme_limited_combine_ego_gift] — tekst] 현재 테마 팩 한정 - 합성
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_combine_scroll_tag_theme_limited_combine_ego_gift].content
   limit: do 120 znaków
   EN: Current Theme Pack-Exclusive - Fusion
   PL: Wyłącznie w bieżącym pakiecie — Synteza
203. [Tryby lochów i Kolei Refrakcji [ego_gift_list_default] — tekst] E.G.O 기프트
   źródło: MirrorDungeonUI_7.json :: dataList[id=ego_gift_list_default].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL: Dary E.G.O
204. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_theme_list_popup_no_theme_on_list] — tekst] 해금된 테마팩이 없습니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_theme_list_popup_no_theme_on_list].content
   limit: do 120 znaków
   EN: No Theme Packs unlocked.
   PL: Brak odblokowanych Pakietów Tematycznych.
205. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_theme_list_popup_no_selected_theme_on_list] — tekst] 선택된 테마팩이 없습니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_theme_list_popup_no_selected_theme_on_list].content
   limit: do 120 znaków
   EN: No Theme Packs selected.
   PL: Brak wybranych Pakietów Tematycznych.
206. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_theme_ego_gift_pool_scroll_tag_rate_up] — tekst] 등장 확률 업
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_theme_ego_gift_pool_scroll_tag_rate_up].content
   limit: do 120 znaków
   EN: Rate Up
   PL: Większa szansa
207. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ego_gift_list_popup_theme_ego_gift_pool_scroll_tag_appearable] — tekst] 등장 가능
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ego_gift_list_popup_theme_ego_gift_pool_scroll_tag_appearable].content
   (powtórzenie elementu 195 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Tryby lochów i Kolei Refrakcji [warning_select_lack_of_ego_gift_desc] — tekst] 기프트를 선택할 기회가 남아있습니다.\n선택하지 않고 넘어 가시겠습니까?
   źródło: MirrorDungeonUI_7.json :: dataList[id=warning_select_lack_of_ego_gift_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You have not selected an E.G.O Gift yet.\nContinue without choosing an E.G.O Gift?
   PL: Pozostała niewykorzystana szansa wyboru Daru.\nKontynuować bez wyboru?
209. [Tryby lochów i Kolei Refrakcji [mainui_settings_select_lack_of_ego_gift_warning] — tekst] 기프트 선택 팝업
   źródło: MirrorDungeonUI_7.json :: dataList[id=mainui_settings_select_lack_of_ego_gift_warning].content
   limit: do 120 znaków
   EN: E.G.O Gift Choice
   PL: Okno wyboru Daru
210. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_ui_purchase_exp_loss_warning] — tekst] ※ 최대 레벨 달성 시, 초과 투영도는 획득되지 않습니다.
   źródło: MirrorDungeonUI_7.json :: dataList[id=mirror_dungeon_ui_purchase_exp_loss_warning].content
   limit: do 120 znaków
   EN: ※ Excess Projection Rate cannot be obtained once you reach the maximum Pass Level.
   PL: ※ Po osiągnięciu maksymalnego poziomu nadmiarowy Stopień Projekcji przepada.

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_7_Achievement
- plik gry: `MirrorDungeonUI_7_Achievement.json`

211. [Tryby lochów i Kolei Refrakcji [mirrordungeon7_mission_date] — tekst] 거울 던전 8 업데이트 전까지 보상을 수령할 수 있습니다.
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon7_mission_date].content
   limit: do 120 znaków
   EN: The rewards can be claimed until before the Mirror Dungeon #8 Update.
   PL: Nagrody można odebrać do aktualizacji Lustrzanego Lochu #8.
212. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_COLLECTION] — tekst] 수집
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_COLLECTION].content
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
213. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_CLEAR] — tekst] 클리어
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_CLEAR].content
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_DECK] — tekst] 편성
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_DECK].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_SHOP] — tekst] 상점
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_SHOP].content
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_BATTLE] — tekst] 전투
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_BATTLE].content
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_EXTREME] — tekst] 제약 - 익스트림
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_EXTREME].content
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_ALL] — tekst] 달성도
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_ALL].content
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
219. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON7_HIDDEN] — tekst] 히든
   źródło: MirrorDungeonUI_7_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON7_HIDDEN].content
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_8
- plik gry: `MirrorDungeonUI_8.json`

220. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_progress_text_8] — tekst] 시지프의 거울 {0}층
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirror_dungeon_progress_text_8].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Mirror of Sisyphe - F{0}
   PL: Lustro Sisyphe — {0}. piętro
221. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_start_buff_Panel_title_md8] — tekst] 시지프 별의 가호
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirror_dungeon_start_buff_Panel_title_md8].content
   limit: do 120 znaków
   EN: Grace of the Sisyphean Star
   PL: Błogosławieństwo Gwiazdy Sisyphe
222. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_blocked_8] — tekst] 9장 클리어 시 개방됩니다.
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirrordungeon_theme_hard_blocked_8].content
   limit: do 120 znaków
   EN: Clear Canto IX to Unlock.
   PL: Odblokowanie po ukończeniu Canto IX.
223. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_hard_blocked_short_8] — tekst] 9장 클리어
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirrordungeon_theme_hard_blocked_short_8].content
   limit: do 120 znaków
   EN: Clear Canto IX
   PL: Ukończ Canto IX
224. [Tryby lochów i Kolei Refrakcji [mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_110] — tekst] 개방 조건 9.5-26 및 10장 클리어 시 진입 가능한 테마팩입니다.
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirror_dungeon_detect_theme_pack_side_popup_locked_by_unlockcode_110].content
   limit: do 140 znaków
   EN: This Theme Pack will become available when meeting the Unlock Conditions: Clear Chapter 9.5-26 and Canto X
   PL: Pakiet dostępny po spełnieniu warunków odblokowania: ukończ 9.5-26 oraz Canto X.
225. [Tryby lochów i Kolei Refrakcji [mirrordungeon_theme_pack_blocked_short_110] — tekst] 9.5-26 및 10장 클리어
   źródło: MirrorDungeonUI_8.json :: dataList[id=mirrordungeon_theme_pack_blocked_short_110].content
   limit: do 120 znaków
   EN: Clear 9.5-26 and Canto X
   PL: Ukończ 9.5-26 oraz Canto X

## Tryby lochów i Kolei Refrakcji: MirrorDungeonUI_8_Achievement
- plik gry: `MirrorDungeonUI_8_Achievement.json`

226. [Tryby lochów i Kolei Refrakcji [mirrordungeon8_mission_date] — tekst] 거울 던전 9 업데이트 전까지 보상을 수령할 수 있습니다.
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon8_mission_date].content
   limit: do 120 znaków
   EN: The rewards can be claimed until before the Mirror Dungeon #9 Update.
   PL: Nagrody można odebrać do aktualizacji Lustrzanego Lochu #9.
227. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_COLLECTION] — tekst] 수집
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_COLLECTION].content
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_CLEAR] — tekst] 클리어
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_CLEAR].content
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_DECK] — tekst] 편성
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_DECK].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_SHOP] — tekst] 상점
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_SHOP].content
   (powtórzenie elementu 3 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_BATTLE] — tekst] 전투
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_BATTLE].content
   (powtórzenie elementu 11 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_EXTREME] — tekst] 제약 - 익스트림
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_EXTREME].content
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_ALL] — tekst] 달성도
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_ALL].content
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Tryby lochów i Kolei Refrakcji [mirrordungeon_mission_category_title_MIRROR_DUNGEON8_HIDDEN] — tekst] 히든
   źródło: MirrorDungeonUI_8_Achievement.json :: dataList[id=mirrordungeon_mission_category_title_MIRROR_DUNGEON8_HIDDEN].content
   (powtórzenie elementu 151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeon
- plik gry: `RailwayDungeon.json`

235. [Tryby lochów i Kolei Refrakcji [1] — nazwa] 1호선
   źródło: RailwayDungeon.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Line 1
   PL: Linia 1
236. [Tryby lochów i Kolei Refrakcji [2] — nazwa] 2호선
   źródło: RailwayDungeon.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Line 2
   PL: Linia 2
237. [Tryby lochów i Kolei Refrakcji [3] — nazwa] 3호선
   źródło: RailwayDungeon.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Line 3
   PL: Linia 3
238. [Tryby lochów i Kolei Refrakcji [4] — nazwa] 4호선
   źródło: RailwayDungeon.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Line 4
   PL: Linia 4
239. [Tryby lochów i Kolei Refrakcji [4] — pełna nazwa] 4호선
   źródło: RailwayDungeon.json :: dataList[id=4].longName
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Tryby lochów i Kolei Refrakcji [5] — nazwa] 5호선
   źródło: RailwayDungeon.json :: dataList[id=5].name
   limit: do 40 znaków
   EN: Line 5
   PL: Linia 5
241. [Tryby lochów i Kolei Refrakcji [5] — pełna nazwa] 5호선
   źródło: RailwayDungeon.json :: dataList[id=5].longName
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Tryby lochów i Kolei Refrakcji [1001] — nazwa] 1호선
   źródło: RailwayDungeon.json :: dataList[id=1001].name
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Tryby lochów i Kolei Refrakcji [6] — nazwa] 6호선
   źródło: RailwayDungeon.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Line 6
   PL: Linia 6
244. [Tryby lochów i Kolei Refrakcji [1002] — nazwa] 2호선
   źródło: RailwayDungeon.json :: dataList[id=1002].name
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeonBuff
- plik gry: `RailwayDungeonBuff.json`

245. [Tryby lochów i Kolei Refrakcji [HealHpMaxForSelected] — tekst] 선택한 인격 체력 최대로 회복
   źródło: RailwayDungeonBuff.json :: dataList[id=HealHpMaxForSelected].content
   limit: do 120 znaków
   EN: Fully heal selected Identity
   PL: W pełni ulecz PŻ wybranej Tożsamości
246. [Tryby lochów i Kolei Refrakcji [HealHpPercentageForAll] — tekst] 모든 인격 체력 {0}% 회복
   źródło: RailwayDungeonBuff.json :: dataList[id=HealHpPercentageForAll].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All Identities heal {0}% HP
   PL: Odnowienie {0}% PŻ wszystkich Tożsamości
247. [Tryby lochów i Kolei Refrakcji [ResurrectForSelected] — tekst] 사망한 인격 1명 최대 체력 상태로 부활
   źródło: RailwayDungeonBuff.json :: dataList[id=ResurrectForSelected].content
   limit: do 120 znaków
   EN: Revive an Identity with fully healed HP
   PL: Wskrześ 1 poległą Tożsamość z pełnymi PŻ

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode1-1
- plik gry: `RailwayDungeonNode1-1.json`

248. [Tryby lochów i Kolei Refrakcji [1] — tytuł] 시 착 역 : 조우
   źródło: RailwayDungeonNode1-1.json :: dataList[id=1].title
   limit: do 40 znaków
   EN: First Stop: Contact
   PL: Stacja początkowa: Spotkanie
249. [Tryby lochów i Kolei Refrakcji [1] — opis] <color=#990000><b> [굴절률 : 3%] </b></color>\n\n꺾여들어간지 얼마 안 되었지만,\n벌써 정차한 듯 하다.\n\n아직 익숙한 감각은 아니지만,\n몇 번 전투를 치르면 이 또한 익숙해지겠지.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 3%] </b></color>\n\nNot long after first embarking,\nthe vehicle seems to have pulled in.\n\nAlthough this doesn’t feel familiar yet,\nthings should change after a fight or three.
   PL: <color=#990000><b> [Współczynnik załamania: 3%] </b></color>\n\nLedwie skręciliśmy w głąb torów,\na pociąg już się zatrzymał.\n\nTo wciąż obce uczucie,\nlecz po paru starciach powinniśmy przywyknąć.
250. [Tryby lochów i Kolei Refrakcji [2] — tytuł] 제 2 역 : 원복
   źródło: RailwayDungeonNode1-1.json :: dataList[id=2].title
   limit: do 40 znaków
   EN: Station #2: Restoration
   PL: Stacja 2: Przywrócenie
251. [Tryby lochów i Kolei Refrakcji [2] — opis] <color=#990000><b> [굴절률 : 8%] </b></color>\n\n언젠가 만나왔던 것들이다.\n이번에도 언젠가 만났던 것일지 모른다.\n또는 언젠가는 만날 것들일지도.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=2].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 8%] </b></color>\n\nThey are things that we’ve met at one point.\nThis may be another such encounter.\nOr, they might be beings that we will meet at some point.
   PL: <color=#990000><b> [Współczynnik załamania: 8%] </b></color>\n\nIstoty, które już kiedyś napotkaliśmy.\nMoże i tym razem znamy je z przeszłości.\nA może dopiero przyjdzie nam je spotkać.
252. [Tryby lochów i Kolei Refrakcji [3] — tytuł] 제 3 역 : 침잠
   źródło: RailwayDungeonNode1-1.json :: dataList[id=3].title
   limit: do 40 znaków
   EN: Station #3: Sinkage
   PL: Stacja 3: Zatonięcie
253. [Tryby lochów i Kolei Refrakcji [3] — opis] <color=#990000><b> [굴절률 : 13%] </b></color>\n\n슬픈 울음소리가 퍼져온다.\n가만히 그 소리를 들어주고 싶지만,\n오래 정차하고 있을 수는 없다.\n다음 역을 향해 가기 위해서는, 마주해야 한다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=3].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 13%] </b></color>\n\nA sorrowful and gloomy cry is heard.\nAs tempting as it is to stick around and hear its cry,\nwe can’t stay for too long.\nTo reach the next station, there’s no choice but to face it.
   PL: <color=#990000><b> [Współczynnik załamania: 13%] </b></color>\n\nNiesie się żałosny szloch.\nChoć chciałoby się przystanąć i wysłuchać tego płaczu,\nnie możemy zatrzymywać się na długo.\nAby ruszyć do następnej stacji, musimy stawić mu czoła.
254. [Tryby lochów i Kolei Refrakcji [4] — tytuł] 제 4 역 : 재회
   źródło: RailwayDungeonNode1-1.json :: dataList[id=4].title
   limit: do 40 znaków
   EN: Station #4: Reunion
   PL: Stacja 4: Ponowne spotkanie
255. [Tryby lochów i Kolei Refrakcji [4] — opis] <color=#990000><b> [굴절률 : 19%] </b></color>\n\n언젠가 끝도 없이 우리를 따라왔던 것들이다.\n다시금 우리 앞에 서있는 것을 보니,\n헛구역질이 올라오기도 한다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=4].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 19%] </b></color>\n\nThose are the ones that relentlessly chased us once before.\nSeeing them confront us yet again…\nWhy, it could almost make me sick.
   PL: <color=#990000><b> [Współczynnik załamania: 19%] </b></color>\n\nTo te same byty, które kiedyś bez wytchnienia nas ścigały.\nNa sam widok, że znów stoją nam na drodze,\npodchodzi mi do gardła mdłość.
256. [Tryby lochów i Kolei Refrakcji [5] — tytuł] 제 5 역 : 절연
   źródło: RailwayDungeonNode1-1.json :: dataList[id=5].title
   limit: do 40 znaków
   EN: Station #5: Insulation
   PL: Stacja 5: Izolacja
257. [Tryby lochów i Kolei Refrakcji [5] — opis] <color=#990000><b> [굴절률 : 23%] </b></color>\n\n사방이 천둥의 소리다.\n어둑한 시야를 가끔 가끔, 보랏빛 낙뢰가 밝혀온다.\n멀었던 소리는 가까워오고,\n빛의 밝기는 더욱 선명해지니.\n무엇이 우리를 기다리는지 알 것만 같다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=5].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 23%] </b></color>\n\nRoaring thunder shakes the air.\nOccasionally, the darkness is pierced by a purple bolt of lightning.\nThe sound grows closer.\nThe lights glow brighter.\nIt becomes clear what awaits us.
   PL: <color=#990000><b> [Współczynnik załamania: 23%] </b></color>\n\nZe wszystkich stron przetacza się grzmot.\nMrok raz po raz rozdziera fioletowa błyskawica.\nOdległy huk przybliża się z każdą chwilą,\na blask staje coraz wyraźniejszy.\nChyba wiemy już, co na nas czeka.
258. [Tryby lochów i Kolei Refrakcji [6] — tytuł] 제 6 역 : 선발
   źródło: RailwayDungeonNode1-1.json :: dataList[id=6].title
   limit: do 40 znaków
   EN: Station #6: Pickup
   PL: Stacja 6: Selekcja
259. [Tryby lochów i Kolei Refrakcji [6] — opis] <color=#990000><b> [굴절률 : 34%] </b></color>\n\n천둥 소리가 아직 멀어지지 않은 것 같다.\n아니, 그렇지 않다.\n그 소리와 흡사하면서도 다른 종류의 소리다.\n녹물 흐르는 냄새와 태운 고기의 향이 어렴풋이 스친다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=6].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 34%] </b></color>\n\nIt seems the thunderous hums still linger.\nNo, that’s incorrect.\nThe sound is similar but not quite the same.\nThe scent of rust stains and burnt meat brushed past us.
   PL: <color=#990000><b> [Współczynnik załamania: 34%] </b></color>\n\nZdaje się, że pomruk gromu jeszcze nie ucichł.\nNie — to coś innego.\nDźwięk łudząco podobny, a jednak odmienny.\nW powietrzu unosi się woń rdzawej wody i przypalonego mięsa.
260. [Tryby lochów i Kolei Refrakcji [7] — tytuł] 제 7 역 : 무수
   źródło: RailwayDungeonNode1-1.json :: dataList[id=7].title
   limit: do 40 znaków
   EN: Station #7: Headlessness
   PL: Stacja 7: Bezgłowość
261. [Tryby lochów i Kolei Refrakcji [7] — opis] <color=#990000><b> [굴절률 : 42%] </b></color>\n\n이리저리 튕기고 꺾인 것만 같다.\n머리를 차라리 뜯어내고 싶을 정도로 어지러웠다.\n나올리 없는 구역질을 참고 도착지에서 일어섰을 때는.\n생각만으로 멈출 수 있어서\n다행이라고 생각할 만한 것이 앞에 있었다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=7].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 42%] </b></color>\n\nMany reflections and refractions were suffered.\nVertigo induces the urge to tear my head off.\nManaging to hold in the impossible impulse to vomit,\na being came into sight that made me glad\nthat my urge stopped as a mere thought.
   PL: <color=#990000><b> [Współczynnik załamania: 42%] </b></color>\n\nOdbijało nas i załamywało na wszystkie strony.\nZawrót głowy był tak nieznośny, że miałem ochotę własnoręcznie ją sobie urwać.\nGdy zdusiłem niemożliwe mdłości i podniosłem wzrok na peronie,\nujrzałem przed sobą coś, na widok czego odetchnąłem,\nże skończyło się tylko na myśli.
262. [Tryby lochów i Kolei Refrakcji [8] — tytuł] 제 8 역 : 존재
   źródło: RailwayDungeonNode1-1.json :: dataList[id=8].title
   limit: do 40 znaków
   EN: Station #8: Existence
   PL: Stacja 8: Istnienie
263. [Tryby lochów i Kolei Refrakcji [8] — opis] <color=#990000><b> [굴절률 : 51%] </b></color>\n\n베어도 베어도 차오르는 것은 하나 뿐이 아니었다.\n떠올려보면… 싸우면서 무엇이든 앗아가고,\n자기 것으로 만들던 것이 있었다.\n자신의 존재를 타인의 것으로 덮어 올리던 것이.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=8].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 51%] </b></color>\n\nThose corporate drones weren’t the only beasts known for regeneration.\nLooking back… there was also a being that took from what it fought.\nIt would mimic them as its own.\nA being that covered its existence in what belonged to others.
   PL: <color=#990000><b> [Współczynnik załamania: 51%] </b></color>\n\nNie tylko tamci odrastali bez końca mimo kolejnych cięć.\nGdy sięgnąć pamięcią… był też byt, który w walce wydzierał wszystko\ni czynił to własnym.\nIstota przykrywająca własne istnienie cudzym.
264. [Tryby lochów i Kolei Refrakcji [9] — tytuł] 제 9 역 : 혈청
   źródło: RailwayDungeonNode1-1.json :: dataList[id=9].title
   limit: do 40 znaków
   EN: Station #9: Serum
   PL: Stacja 9: Surowica
265. [Tryby lochów i Kolei Refrakcji [9] — opis] <color=#990000><b> [굴절률 : 59%] </b></color>\n\n한 때 우리를 아찔하게 했던 그 회사의 표식이 보인다.\n\n베어도 베어도 차오르는…\n정신을 단단히 붙들어야만 할 것 같다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=9].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 59%] </b></color>\n\nThe logo of a corporation that once cornered us can be seen.\n\nThose who would heal their scrapes the instant they were inflicted…\nThis will require some determination.
   PL: <color=#990000><b> [Współczynnik załamania: 59%] </b></color>\n\nWidać emblemat korporacji, która kiedyś przyprawiła nas o zawrót głowy.\n\nIle by ich nie ciąć, rany natychmiast się zasklepiają…\nTrzeba będzie mocno trzymać nerwy na wodzy.
266. [Tryby lochów i Kolei Refrakcji [10] — tytuł] 제 10 역 : 아설
   źródło: RailwayDungeonNode1-1.json :: dataList[id=10].title
   limit: do 40 znaków
   EN: Station #10: Forked Tongue
   PL: Stacja 10: Rozwidlony język
267. [Tryby lochów i Kolei Refrakcji [10] — opis] <color=#990000><b> [굴절률 : 71%] </b></color>\n\n날름거리는 혓바닥은 두 갈래로 나누어져 있다.\n어느쪽을 향해야 할지 모른다는 듯,\n안절부절 나왔다 들어갔다를 반복한다.\n저것이든, 우리든.\n까딱 잘못 선택하면 이대로 튕겨나갈 것은 분명하다.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=10].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 71%] </b></color>\n\nThe slithering tongue is split into two.\nUnsure of which direction to point,\nit nervously extends and retracts.\nBoth we and it are in peril.\nOne wrong choice could mean being reflected off this plane.
   PL: <color=#990000><b> [Współczynnik załamania: 71%] </b></color>\n\nŚmigający język rozdziela się na dwoje.\nJakby sam nie wiedział, w którą stronę się zwrócić,\nnerwowo wysuwa się i chowa.\nZarówno on, jak i my balansujemy na krawędzi.\nJeden fałszywy ruch wyrzuci nas z tej płaszczyzny.
268. [Tryby lochów i Kolei Refrakcji [11] — tytuł] 제 11 역 : 통전
   źródło: RailwayDungeonNode1-1.json :: dataList[id=11].title
   limit: do 40 znaków
   EN: Station #11: Energization
   PL: Stacja 11: Przewodnictwo
269. [Tryby lochów i Kolei Refrakcji [11] — opis] <color=#990000><b> [굴절률 : 84%] </b></color>\n\n몇 역 전인가, 분명히 보았던 것들이다.\n그것들이 왜 한 자리에 함께 하고\n있는 지는 도무지 알 수 없다.\n지나오며 굴절될 때, 같은 공간으로 쏘아진 것일까.\n아니면, 물에 전기가 통하듯 자연스레 합세하게 된 것일까.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=11].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 84%] </b></color>\n\nThose are beings that we saw several stations ago.\nWhy they are together in one place\nis a complete mystery.\nPerhaps they were cast into the same location when they were refracted.\nOr, they might have joined together as naturally as water conducts electricity.
   PL: <color=#990000><b> [Współczynnik załamania: 84%] </b></color>\n\nTe istoty widzieliśmy już kilka stacji wcześniej.\nDlaczego znalazły się tu razem —\ntego nie sposób pojąć.\nMoże kolejne załamanie rzuciło je w tę samą przestrzeń.\nA może połączyły się tak naturalnie, jak woda przewodzi prąd.
270. [Tryby lochów i Kolei Refrakcji [12] — tytuł] 제 12 역 : 순수
   źródło: RailwayDungeonNode1-1.json :: dataList[id=12].title
   limit: do 40 znaków
   EN: Station #12: Purity
   PL: Stacja 12: Czystość
271. [Tryby lochów i Kolei Refrakcji [12] — opis] <color=#990000><b> [굴절률 : 92%] </b></color>\n\n가장 순수하다고 믿는 모습으로, 그것은 자리해 있었다.\n수감자 하나가 그럴 순 없다며 무어라 외치지만,\n이미 발언조차 튕겨나갈 정도로 심하게 왜곡된 세계에서\n그 말은 나아가거나 닿지 못하였다.\n우리가 나눌 수 있는 것은… 총칼을 앞세운 싸움의 합뿐.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=12].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 92%] </b></color>\n\nIt stood there, taking the form it believed to be purest.\nOne Sinner exclaimed that this couldn’t be possible,\nbut in a world as warped and twisted as this,\nsuch a statement wouldn’t travel far.\nThe only exchange allowed was that of blows—dealt with weapons and arms.
   PL: <color=#990000><b> [Współczynnik załamania: 92%] </b></color>\n\nTrwało tam w postaci, którą uważało za najczystszą.\nKtóryś z Grzeszników krzyknął, że to niemożliwe,\nlecz w świecie tak głęboko wypaczonym, że nawet słowa ulegają odbiciu,\ngłos ten nie zdołał nigdzie dotrzeć.\nPozostała nam już tylko wymiana ciosów żelazem i ołowiem.
272. [Tryby lochów i Kolei Refrakcji [13] — tytuł] 종 착 역 : 무아
   źródło: RailwayDungeonNode1-1.json :: dataList[id=13].title
   limit: do 40 znaków
   EN: Last Stop: Non-self
   PL: Stacja końcowa: Nie-ja
273. [Tryby lochów i Kolei Refrakcji [13] — opis] <color=#990000><b> [굴절률 : 99%] </b></color>\n\n이제 한계다. 잠시 정차하는 것 만으로도\n원래 있던 공간으로 튕겨져 나갈 지경이다.\n한 차례라도 방심하는 순간 이 모든 것은 물거품이 될 것이다.\n뚫고 지나갈 수 있다면, 종착할 수 있을 것이다.\n마치 그곳에 아무것도 없는 것처럼. 마음을 비우고 전진하자.
   źródło: RailwayDungeonNode1-1.json :: dataList[id=13].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 99%] </b></color>\n\nThis is the limit.\nEven a short rest feels like it might eject us back to whence we came.\nA single moment’s carelessness can bring all our effort to naught.\nIf we make it through this, we will be able to reach the terminus.\nLet’s empty our minds and proceed—as if nothing were ever there.
   PL: <color=#990000><b> [Współczynnik załamania: 99%] </b></color>\n\nTo już granica. Nawet krótki postój grozi tym,\nże wyrzuci nas z powrotem do pierwotnej przestrzeni.\nJedna chwila nieuwagi obróci cały dotychczasowy trud wniwecz.\nJeśli zdołamy się przebić, dotrzemy do końca trasy.\nOpróżnijmy umysły i ruszajmy naprzód — jakby nic tam nie istniało.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode1002
- plik gry: `RailwayDungeonNode1002.json`

274. [Tryby lochów i Kolei Refrakcji [100201] — tytuł] 제 1 순환 : 저주-사역-낙우
   źródło: RailwayDungeonNode1002.json :: dataList[id=100201].title
   limit: do 50 znaków
   EN: Cycle #1: Curse-Servitude-Rainfall
   PL: Cykl 1: Klątwa–Kierat–Ulewa
275. [Tryby lochów i Kolei Refrakcji [100202] — tytuł] 제 2 순환 : 저주-이취-착취-사역
   źródło: RailwayDungeonNode1002.json :: dataList[id=100202].title
   limit: do 70 znaków
   EN: Cycle #2: Curse-Odd Stench-Exploitation-Servitude
   PL: Cykl 2: Klątwa–Odór–Wyzysk–Kierat
276. [Tryby lochów i Kolei Refrakcji [100203] — tytuł] 제 3 순환 : 저주-체납-이취-낙우
   źródło: RailwayDungeonNode1002.json :: dataList[id=100203].title
   limit: do 60 znaków
   EN: Cycle #3: Curse-Arrears-Odd Stench-Rainfall
   PL: Cykl 3: Klątwa–Zwłoka–Odór–Ulewa
277. [Tryby lochów i Kolei Refrakcji [100204] — tytuł] 제 4 순환 : 저주-유인-이취-체납-순환
   źródło: RailwayDungeonNode1002.json :: dataList[id=100204].title
   limit: do 70 znaków
   EN: Cycle #4: Curse-Lure-Odd Stench-Arrears-Cycle
   PL: Cykl 4: Klątwa–Wabik–Odór–Zwłoka–Cykl
278. [Tryby lochów i Kolei Refrakcji [100205] — tytuł] 최종 순환 : 저주-사역-낙우-체납-유인-착취-이취-순환
   źródło: RailwayDungeonNode1002.json :: dataList[id=100205].title
   limit: do 110 znaków
   EN: <size=50%>Final Cycle: Curse-Servitude-Rainfall-Arrears-Lure-Exploitation-Odd Stench-Cycle</size>
   PL: Ostatni Cykl: Klątwa–Kierat–Ulewa–Zwłoka–Wabik–Wyzysk–Odór–Cykl
279. [Tryby lochów i Kolei Refrakcji [100206] — tytuł] 종착역 : 정원
   źródło: RailwayDungeonNode1002.json :: dataList[id=100206].title
   limit: do 40 znaków
   EN: Terminus: The Garden
   PL: Stacja końcowa: Ogród

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode1BokGak
- plik gry: `RailwayDungeonNode1BokGak.json`

280. [Tryby lochów i Kolei Refrakcji [101] — tytuł] 1호선 진입 전
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=101].title
   limit: do 40 znaków
   EN: Line 1 Boarding
   PL: Przed wejściem na Linię 1
281. [Tryby lochów i Kolei Refrakcji [102] — tytuł] 1호선
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=102].title
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Tryby lochów i Kolei Refrakcji [100101] — tytuł] 시착역 - 조우
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100101].title
   limit: do 40 znaków
   EN: First Stop: Contact
   PL: Stacja początkowa: Spotkanie
283. [Tryby lochów i Kolei Refrakcji [100102] — tytuł] 제 2역 - 원복
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100102].title
   limit: do 40 znaków
   EN: Station #2: Restoration
   PL: Stacja 2: Przywrócenie
284. [Tryby lochów i Kolei Refrakcji [100103] — tytuł] 제 3역 - 침잠
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100103].title
   limit: do 40 znaków
   EN: Station #3: Sinkage
   PL: Stacja 3: Zatonięcie
285. [Tryby lochów i Kolei Refrakcji [100104] — tytuł] 제 4역 - 재회
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100104].title
   limit: do 40 znaków
   EN: Station #4: Reunion
   PL: Stacja 4: Ponowne spotkanie
286. [Tryby lochów i Kolei Refrakcji [100105] — tytuł] 제 5역 - 절연
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100105].title
   limit: do 40 znaków
   EN: Station #5: Insulation
   PL: Stacja 5: Izolacja
287. [Tryby lochów i Kolei Refrakcji [100106] — tytuł] 제 6역 - 선발
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100106].title
   limit: do 40 znaków
   EN: Station #6: Pickup
   PL: Stacja 6: Selekcja
288. [Tryby lochów i Kolei Refrakcji [100107] — tytuł] 제 7역 - 무수
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100107].title
   limit: do 40 znaków
   EN: Station #7: Headlessness
   PL: Stacja 7: Bezgłowość
289. [Tryby lochów i Kolei Refrakcji [100108] — tytuł] 제 8역 - 존재
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100108].title
   limit: do 40 znaków
   EN: Station #8: Existence
   PL: Stacja 8: Istnienie
290. [Tryby lochów i Kolei Refrakcji [100109] — tytuł] 제 9역 - 혈청
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100109].title
   limit: do 40 znaków
   EN: Station #9: Serum
   PL: Stacja 9: Surowica
291. [Tryby lochów i Kolei Refrakcji [100110] — tytuł] 제 10역 - 아설
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100110].title
   limit: do 40 znaków
   EN: Station #10: Forked Tongue
   PL: Stacja 10: Rozwidlony język
292. [Tryby lochów i Kolei Refrakcji [100111] — tytuł] 제 11역 - 통전
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100111].title
   limit: do 40 znaków
   EN: Station #11: Energization
   PL: Stacja 11: Przewodnictwo
293. [Tryby lochów i Kolei Refrakcji [100112] — tytuł] 제 12역 - 순수
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100112].title
   limit: do 40 znaków
   EN: Station #12: Purity
   PL: Stacja 12: Czystość
294. [Tryby lochów i Kolei Refrakcji [100113] — tytuł] 종착역 - 무아
   źródło: RailwayDungeonNode1BokGak.json :: dataList[id=100113].title
   limit: do 40 znaków
   EN: Last Stop: Non-self
   PL: Stacja końcowa: Nie-ja

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode2
- plik gry: `RailwayDungeonNode2.json`

295. [Tryby lochów i Kolei Refrakcji [201] — tytuł] 시 착 역 : 저주
   źródło: RailwayDungeonNode2.json :: dataList[id=201].title
   limit: do 40 znaków
   EN: First Stop: Curse
   PL: Stacja początkowa: Klątwa
296. [Tryby lochów i Kolei Refrakcji [201] — opis] <color=#990000><b> [굴절률 : 0%] </b></color>\n\n또 한 번, 이곳이다.\n과거에 겪었던 고달픈 전투와 이리저리\n굴절되는 기묘한 기분이 또 다시 전신에 느껴진다.\n\n이번에도 익숙해질 수 있을까.
   źródło: RailwayDungeonNode2.json :: dataList[id=201].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 0%] </b></color>\n\nHere we go again.\nMemories of painful battles we've endured,\nthe odd feeling of refraction pierces through my body.\n\nI wonder if we can adapt once more.
   PL: <color=#990000><b> [Współczynnik załamania: 0%] </b></color>\n\nZnów tu jesteśmy.\nWspomnienie wyczerpujących walk i osobliwe uczucie\nzałamania na nowo przeszywają całe ciało.\n\nCiekawe, czy i tym razem zdołamy przywyknąć.
297. [Tryby lochów i Kolei Refrakcji [202] — tytuł] 제 2 역 : 사역
   źródło: RailwayDungeonNode2.json :: dataList[id=202].title
   limit: do 40 znaków
   EN: Station #2: Servitude
   PL: Stacja 2: Kierat
298. [Tryby lochów i Kolei Refrakcji [202] — opis] <color=#990000><b> [굴절률 : 14%] </b></color>\n\n그것은 계속해서 일하고 있었다.\n꽉 들어찬 뜨거운 증기가 쇳덩이들을\n굴리기 시작하던 시절부터 줄곧 그래왔다.\n지나가기 위해서는, 그 길었던 순환고리를\n끊어내야만 할 것이다.
   źródło: RailwayDungeonNode2.json :: dataList[id=202].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 14%] </b></color>\n\nIt was working ceaselessly.\nThe machine has never stopped working since\nits pressurized, scalding hot steam turned its first gears.\nWe must break the cycle in which it has long been\ntrapped to continue on our path.
   PL: <color=#990000><b> [Współczynnik załamania: 14%] </b></color>\n\nPracowało bez wytchnienia.\nOdkąd rozgrzana pod ciśnieniem para po raz pierwszy\nwprawiła żelastwo w ruch, nie zatrzymało się ani na chwilę.\nAby ruszyć dalej, musimy przerwać\nten ciągnący się od wieków krąg.
299. [Tryby lochów i Kolei Refrakcji [203] — tytuł] 제 3 역 : 낙우
   źródło: RailwayDungeonNode2.json :: dataList[id=203].title
   limit: do 40 znaków
   EN: Station #3: Rainfall
   PL: Stacja 3: Ulewa
300. [Tryby lochów i Kolei Refrakcji [203] — opis] <color=#990000><b> [굴절률 : 21%] </b></color>\n\n여우는 가끔씩 운다.\n그 울음이 슬픔인지, 그저 비를 불러오는 주문인지는 모른다.\n그러나 그 몸에 꽂혀있는 우산들이\n비를 막기 위한 것이 아니었다는 건 안다.\n여우가 제 스스로를 위해서 펼쳤던 적은 없었던 우산이니까.
   źródło: RailwayDungeonNode2.json :: dataList[id=203].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 21%] </b></color>\n\nThe fox cries, sometimes.\nWe know not if it cries for sorrow or rain.\nWe know, however, that the umbrellas piercing\nits body are not there for the rain.\nFor the fox has not once opened them for itself.
   PL: <color=#990000><b> [Współczynnik załamania: 21%] </b></color>\n\nLis czasem płacze.\nNie wiadomo, czy z żalu, czy tylko zaklina deszcz.\nWiemy jednak, że parasole wbite w jego ciało\nnigdy nie chroniły go przed ulewą.\nAni razu nie rozłożył ich dla samego siebie.
301. [Tryby lochów i Kolei Refrakcji [204] — tytuł] 제 4 역 : 체납
   źródło: RailwayDungeonNode2.json :: dataList[id=204].title
   limit: do 40 znaków
   EN: Station #4: Arrears
   PL: Stacja 4: Zwłoka
302. [Tryby lochów i Kolei Refrakcji [204] — opis] <color=#990000><b> [굴절률 : 37%] </b></color>\n\n시간은 금이라는 이야기를 들었던 것 같기도 하다.\n지하 깊숙한 금고에 금을 차곡차곡 모으는 자린고비의 이야기도 들었던 것 같다.\n그러니 시간을 돈처럼 모으고 뺏는 일도 당연한 것일지도 모르겠다.\n\n…그들의 시계를 보고 괜시리 머리가 아파지는 이유는 모르겠다.
   źródło: RailwayDungeonNode2.json :: dataList[id=204].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 37%] </b></color>\n\nYou know what they say: time is money.\nI've once heard the tale of a miser who amasses a hoard of gold deep within his basement.\nAmassing time as one does gold is not so different, perhaps.\n\n... Their clocks are giving me a headache for some reason.
   PL: <color=#990000><b> [Współczynnik załamania: 37%] </b></color>\n\nMówią, że czas to pieniądz.\nSłyszałem też kiedyś opowieść o skąpcu gromadzącym złoto w głębokim podziemnym skarbcu.\nMoże więc gromadzenie i odbieranie czasu jak pieniędzy też nie powinno dziwić.\n\n…Nie rozumiem tylko, dlaczego od patrzenia na ich zegary pęka mi głowa.
303. [Tryby lochów i Kolei Refrakcji [205] — tytuł] 제 5 역 : 유인
   źródło: RailwayDungeonNode2.json :: dataList[id=205].title
   limit: do 40 znaków
   EN: Station #5: The Lure
   PL: Stacja 5: Wabik
304. [Tryby lochów i Kolei Refrakcji [205] — opis] <color=#990000><b> [굴절률 : 49%] </b></color>\n\n다른 열차보다 굴절률이 가파르게 올라간다.\n그런 만큼 하나 하나의 역이 버겁다.\n저 굵다란 나무기둥과 푸른 빛의 숲들은 잠시 쉬어가기에 딱 좋아 보인다…\n나뭇가지 위에 앉은 청록빛 불빛이 마치 이리로 오라는 듯, 흔들거리는 것만 같다…
   źródło: RailwayDungeonNode2.json :: dataList[id=205].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 49%] </b></color>\n\nThe refraction rate rises steeply in this train.\nEvery single Station feels like a mountain to climb.\nI think we can take a short rest by the stocky tree stump and the forest with the blue lights...\nThe teal-colored light atop the branch dances from side to side, beckoning us...
   PL: <color=#990000><b> [Współczynnik załamania: 49%] </b></color>\n\nW tym pociągu współczynnik załamania rośnie wyjątkowo stromo.\nKażda kolejna stacja ciąży coraz bardziej.\nTen gruby pień i las skąpany w błękitnym blasku wyglądają jak wymarzone miejsce na chwilę wytchnienia…\nTurkusowe światełko na gałęzi kołysze się, jakby przyzywało nas do siebie…
305. [Tryby lochów i Kolei Refrakcji [206] — tytuł] 제 6 역 : 착취
   źródło: RailwayDungeonNode2.json :: dataList[id=206].title
   limit: do 40 znaków
   EN: Station #6: Exploitation
   PL: Stacja 6: Wyzysk
306. [Tryby lochów i Kolei Refrakcji [206] — opis] <color=#990000><b> [굴절률 : 63%] </b></color>\n\n때로 우리는, 살아가기 위해 배타적이고 이기적인 것이 된다.\n자신이 고통스러워 하고 싶지 않기 위해,\n다른 것을 고통스럽게 만들기도 한다.\n문득, 역 앞에 있는 두 개의 버튼 앞에서 머뭇대게 된다.\n이게 맞을까…?
   źródło: RailwayDungeonNode2.json :: dataList[id=206].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 63%] </b></color>\n\nWe must sometimes become selfish things,\nfull of animosity if it means our survival.\nSometimes, we make others suffer so that we may not.\nFor a moment, I hesitate before the two buttons in front of the Station.\nAm I doing the right thing...?
   PL: <color=#990000><b> [Współczynnik załamania: 63%] </b></color>\n\nCzasem, by przetrwać, stajemy się bezwzględni i samolubni.\nŻeby samemu uniknąć cierpienia,\nskazujemy na nie innych.\nPrzed dwoma przyciskami na stacji ogarnia mnie chwila wahania.\nCzy na pewno postępuję słusznie…?
307. [Tryby lochów i Kolei Refrakcji [207] — tytuł] 제 7 역 : 이취
   źródło: RailwayDungeonNode2.json :: dataList[id=207].title
   limit: do 40 znaków
   EN: Station #7: Odd Stench
   PL: Stacja 7: Odór
308. [Tryby lochów i Kolei Refrakcji [207] — opis] <color=#990000><b> [굴절률 : 86%] </b></color>\n\n‘한 잔 들어요!’\n열차의 문을 열지도 않았는데, 벌써부터 불쾌한 술냄새가 넘실거리며 들어온다.\n’얼른~ 크하! 요정주만한게 없다니까?’\n…도무지 마실만한 것으로 보이지 않는다.\n우리 수감자들 중 한 명이 경기를 일으킬 정도인 걸 봐서는, 혼자만의 생각은 아닌 듯 하다.
   źródło: RailwayDungeonNode2.json :: dataList[id=207].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 86%] </b></color>\n\n'Come here, come all! Take a swig!'\nI can smell the unpleasant stench of alcohol even before the Train door opens.\n'Hurry along, all! A big swill, and you'll feel swell!'\n... It doesn't even look remotely look potable. One of the Sinners begins to retch violently. Guess I'm not alone in thinking that.
   PL: <color=#990000><b> [Współczynnik załamania: 86%] </b></color>\n\n„Wypijcie po jednym!”\nDrzwi wagonu jeszcze się nie otworzyły, a do środka już wlewa się mdlący odór alkoholu.\n„Śmiało~ Cha! Nie ma to jak wróżkowy trunek, co nie?”\n…To nie wygląda na coś, co w ogóle nadaje się do picia.\nSądząc po tym, że jednego z naszych Grzeszników aż skręca, nie tylko ja mam takie wrażenie.
309. [Tryby lochów i Kolei Refrakcji [208] — tytuł] 제 8 역 : 순환
   źródło: RailwayDungeonNode2.json :: dataList[id=208].title
   limit: do 40 znaków
   EN: Station #8: Cycle
   PL: Stacja 8: Cykl
310. [Tryby lochów i Kolei Refrakcji [208] — opis] <color=#990000><b> [굴절률 : 96%] </b></color>\n\n열차는 선택의 순간을 기다리고 있었다.\n이미 한계에 다다른 굴절률을 뚫고 나갈 것인가, 아니면…\n튕겨져 나가 다시 한 번 이 길들을 순환할 것인가.\n어느 쪽이든, 현명하게 선택해야할 것이다.\n역 밖에 서 있는 저것처럼… 길을 잃을 수는 없으니까.
   źródło: RailwayDungeonNode2.json :: dataList[id=208].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 96%] </b></color>\n\nThe train awaits our choice.\nThe refraction rate is at its limits. Breach past it, or...\nRicochet off and start a new Cycle?\nWhichever it is, we must choose carefully.\nWe want to avoid falling off into a wayward path like that... thing outside the Station.
   PL: <color=#990000><b> [Współczynnik załamania: 96%] </b></color>\n\nPociąg czeka na naszą decyzję.\nPrzebić się przez sięgający granicy współczynnik załamania, czy…\nodbić się i jeszcze raz zatoczyć krąg po tych torach?\nTak czy inaczej, musimy wybrać rozważnie.\nNie możemy przecież zabłądzić… jak to coś stojące przed stacją.
311. [Tryby lochów i Kolei Refrakcji [209] — tytuł] 제 4 역 : 체납
   źródło: RailwayDungeonNode2.json :: dataList[id=209].title
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Tryby lochów i Kolei Refrakcji [209] — opis] <color=#990000><b> [굴절률 : 37%] </b></color>\n\n시간은 금이라는 이야기를 들었던 것 같기도 하다.\n지하 깊숙한 금고에 금을 차곡차곡 모으는 자린고비의 이야기도 들었던 것 같다.\n그러니 시간을 돈처럼 모으고 뺏는 일도 당연한 것일지도 모르겠다.\n\n…그들의 시계를 보고 괜시리 머리가 아파지는 이유는 모르겠다.
   źródło: RailwayDungeonNode2.json :: dataList[id=209].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 37%] </b></color>\n\nYou know what they say: time is money.\nI've once heard the tale of a miser who amasses a hoard of gold deep within his basement.\nAmassing time as one does gold is not so different, perhaps.\n... Their clocks are giving me a headache for some reason.
   PL: <color=#990000><b> [Współczynnik załamania: 37%] </b></color>\n\nMówią, że czas to pieniądz.\nSłyszałem też kiedyś opowieść o skąpcu gromadzącym złoto w głębokim podziemnym skarbcu.\nMoże więc gromadzenie i odbieranie czasu jak pieniędzy też nie powinno dziwić.\n\n…Nie rozumiem tylko, dlaczego od patrzenia na ich zegary pęka mi głowa.
313. [Tryby lochów i Kolei Refrakcji [210] — tytuł] 제 7 역 : 이취
   źródło: RailwayDungeonNode2.json :: dataList[id=210].title
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Tryby lochów i Kolei Refrakcji [210] — opis] <color=#990000><b> [굴절률 : 86%] </b></color>\n\n‘한 잔 들어요!’\n열차의 문을 열지도 않았는데, 벌써부터 불쾌한 술냄새가 넘실거리며 들어온다.\n‘얼른~ 크하! 요정주만한게 없다니까?’\n…도무지 마실만한 것으로 보이지 않는다.\n우리 수감자들 중 한 명이 경기를 일으킬 정도인 걸 봐서는, 혼자만의 생각은 아닌 듯 하다.
   źródło: RailwayDungeonNode2.json :: dataList[id=210].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b> [REFRACTION RATE: 86%] </b></color>\n\n'Come here, come all! Take a swig!'\nI can smell the unpleasant stench of alcohol even before the Train door opens.\n'Hurry along, all! A big swill, and you'll feel swell!'\n... It doesn't even look remotely potable. One of the Sinners begins to retch. Guess I'm not alone there.
   PL: <color=#990000><b> [Współczynnik załamania: 86%] </b></color>\n\n„Wypijcie po jednym!”\nDrzwi wagonu jeszcze się nie otworzyły, a do środka już wlewa się mdlący odór alkoholu.\n„Śmiało~ Cha! Nie ma to jak wróżkowy trunek, co nie?”\n…To nie wygląda na coś, co w ogóle nadaje się do picia.\nSądząc po tym, że jednego z naszych Grzeszników aż skręca, nie tylko ja mam takie wrażenie.
315. [Tryby lochów i Kolei Refrakcji [211] — tytuł] 종 착 역 : 정원
   źródło: RailwayDungeonNode2.json :: dataList[id=211].title
   limit: do 40 znaków
   EN: Terminus: The Garden
   PL: Stacja końcowa: Ogród
316. [Tryby lochów i Kolei Refrakcji [211] — opis] <color=#990000><b> [굴절률 : ∞%] </b></color>\n\n이곳이 진정한 종착역이다.\n\n미아가 되지 않고, 이 열차에서 올바르게 하차할 수 있는 합당한 장소.\n이미 굴절률은 측정할 수 없다.\n처음으로, 이 열차를 타고 오면서 처음으로…\n표지판이라는 것을 보았다.\n그건, 이곳이 끝이라고 말하고 있는 걸까.\n아니면… 여기서 우리는 끝이라는 뜻일까.
   źródło: RailwayDungeonNode2.json :: dataList[id=211].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000> [REFRACTION RATE: ∞%] <b></b></color>\n\nThe true Terminus.\n\nThis is an adequate place to get off this train without getting lost.\nThe refraction rate is already off the charts.\nFor the first time since we embarked on this journey...\nI see a signpost.\nMaybe, this is where this railway line ends.\nOr maybe… this is where we meet our ends.
   PL: <color=#990000><b> [Współczynnik załamania: ∞%] </b></color>\n\nOto prawdziwa stacja końcowa.\n\nWłaściwe miejsce, by wysiąść z tego pociągu i nie stać się zbłąkaną duszą.\nWspółczynnika załamania nie sposób już zmierzyć.\nPo raz pierwszy odkąd wsiedliśmy do tego składu…\nzobaczyłem drogowskaz.\nCzy mówi nam, że to koniec trasy?\nCzy może… że tutaj kończymy się my.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode3
- plik gry: `RailwayDungeonNode3.json`

317. [Tryby lochów i Kolei Refrakcji [301] — tytuł] 시 착 역 : 치륜
   źródło: RailwayDungeonNode3.json :: dataList[id=301].title
   limit: do 40 znaków
   EN: First Stop: Cogwheel
   PL: Stacja początkowa: Tryby
318. [Tryby lochów i Kolei Refrakcji [301] — opis] <color=#990000><b> [굴절률 : 0%] </b></color>\n\n톱니가 까득거리며 맞물리는 소리가 들린다.\n둔중하고 무거운 무언가가, 그 소리에 맞추어 한 걸음씩 어딘가를 향하고 있는 것만 같다.
   źródło: RailwayDungeonNode3.json :: dataList[id=301].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 0%]</b></color>\n\nI can hear the metal cogwheels turning and creaking.\nSomething heavy and massive seems to be taking a step with every teeth that click into each other.
   PL: <color=#990000><b> [Współczynnik załamania: 0%] </b></color>\n\nSłychać zgrzyt zazębiających się kół zębatych.\nCoś ciężkiego i masywnego zdaje się stawiać kolejne kroki w rytm tego szczęku.
319. [Tryby lochów i Kolei Refrakcji [302] — tytuł] 제 2 역 : 파랑
   źródło: RailwayDungeonNode3.json :: dataList[id=302].title
   limit: do 40 znaków
   EN: Station #2: Waves
   PL: Stacja 2: Fale
320. [Tryby lochów i Kolei Refrakcji [302] — opis] <color=#990000><b> [굴절률 : 14%] </b></color>\n\n맑지만은 않은 일렁거림이 우리들을 덮쳐온다.\n등뼈에 빼곡하게 박혀있는 감정도, 그 일렁거림을 닮았는지.\n조용하고 무겁게, 우리를 덮쳐온다.
   źródło: RailwayDungeonNode3.json :: dataList[id=302].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 14%]</b></color>\n\nAn opaque, shimmering wave crashes unto us.\nPerhaps its countless emotions, all of it lodged into its back, is reminiscent of that shimmering.\nSilently yet ponderously, it crashes unto us.
   PL: <color=#990000><b> [Współczynnik załamania: 14%] </b></color>\n\nMętne, falujące drżenie napiera w naszą stronę.\nUczucia gęsto wbite w jego kręgosłup zdają się przypominać tę samą toń.\nCicho i ciężko uderza prosto w nas.
321. [Tryby lochów i Kolei Refrakcji [303] — tytuł] 제 3 역 : 향수
   źródło: RailwayDungeonNode3.json :: dataList[id=303].title
   limit: do 40 znaków
   EN: Station #3: Nostalgia
   PL: Stacja 3: Nostalgia
322. [Tryby lochów i Kolei Refrakcji [303] — opis] <color=#990000><b> [굴절률 : 28%] </b></color>\n\n그리운 풍경이 펼쳐진다.\n마치 손짓이라도 하는 듯이 흔들거리는 풍경이 아련한 감정을 불러일으키는 것 같기도 하다.\n수감자들 중 몇몇의 표정이 그다지 좋지는 않은 것 같다…\n이번에 다가갈 때는, 무기를 들고 나서는 게 좋을 것 같다.
   źródło: RailwayDungeonNode3.json :: dataList[id=303].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 28%]</b></color>\n\nA nostalgic sight appears before us.\nThe scene seems to beckon us—perhaps it brings out in us a faint remembrance of the past.\nSome Sinners appear rather distraught…\nThis time, we’ll have to approach it with our weapons drawn.
   PL: <color=#990000><b> [Współczynnik załamania: 28%] </b></color>\n\nRozpościera się znajomy, tęskny krajobraz.\nFalujący widok zdaje się nas przywoływać, budząc mgliste wspomnienia.\nMiny kilku Grzeszników nie wróżą nic dobrego…\nTym razem lepiej podejść z dobytymi broniami.
323. [Tryby lochów i Kolei Refrakcji [304] — tytuł] 제 4 역 : 정시
   źródło: RailwayDungeonNode3.json :: dataList[id=304].title
   limit: do 40 znaków
   EN: Station #4: Interlude
   PL: Stacja 4: Postój
324. [Tryby lochów i Kolei Refrakcji [304] — opis] <color=#990000><b> [굴절률 : ??%] </b></color>\n\n묵직한 소리가 한차례 낮게 울려 퍼진다.\n톱니는 째깍, 째깍 돌아가다가 까드득하는 소리를 내면서 멈추어 버렸다.\n이 공간을 벗어나면, 다시 톱니는 움직이기 시작할 것이다.\n다음 역으로 떠나기 전에, 채비를 해두자.
   źródło: RailwayDungeonNode3.json :: dataList[id=304].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: ??%]</b></color>\n\nA heavy noise echoes once.\nThe teeth on the cogwheel click into one another—tick, tock, then it comes to a stop with a heavy grating noise.\nThe cogs will begin to turn again as soon as we exit this place.\nLet’s prepare ourselves before moving to the next stop.
   PL: <color=#990000><b> [Współczynnik załamania: ??%] </b></color>\n\nNiski, głuchy dźwięk niesie się echem po przestrzeni.\nKoła zębate tykały miarowo, aż wreszcie z chrzęstem znieruchomiały.\nGdy tylko opuścimy to miejsce, tryby znów ruszą.\nPrzygotujmy się przed odjazdem do następnej stacji.
325. [Tryby lochów i Kolei Refrakcji [305] — tytuł] 제 5 역 : 고행
   źródło: RailwayDungeonNode3.json :: dataList[id=305].title
   limit: do 40 znaków
   EN: Station #5: Drudgery
   PL: Stacja 5: Umartwienie
326. [Tryby lochów i Kolei Refrakcji [305] — opis] <color=#990000><b> [굴절률 : 39%] </b></color>\n\n언젠가 겪었던 소금기 있는 냄새가 풍겨온다.\n그 냄새 속에는, 각종 오물과 염분, 그리고 그것과 비슷한 것들을 아프게 품고 있는 자가 우리를 기다리고 있다.
   źródło: RailwayDungeonNode3.json :: dataList[id=305].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 39%]</b></color>\n\nWe’ve gone through this salty scent of the sea before.\nThe one who painfully bears the multitude of filth, salt, and other similar things within it awaits us there.
   PL: <color=#990000><b> [Współczynnik załamania: 39%] </b></color>\n\nDolatuje nas znajoma, słonawa woń.\nW tym oparze czeka na nas istota boleśnie dźwigająca w sobie wszelkie nieczystości, sól i rzeczy im podobne.
327. [Tryby lochów i Kolei Refrakcji [306] — tytuł] 제 6 역 : 진리
   źródło: RailwayDungeonNode3.json :: dataList[id=306].title
   limit: do 40 znaków
   EN: Station #6: Truth
   PL: Stacja 6: Prawda
328. [Tryby lochów i Kolei Refrakcji [306] — opis] <color=#990000><b> [굴절률 : 51%] </b></color>\n\n묘한 양초 타는 향이 공간 안에 만연하다.\n그 안에는 진리를 추구하는 자가 있다. 단 한 글자도 놓치지 않고 모든 지식을 쓸어 담으려는 듯 커다란 눈알을 굴리고 있다.\n진리의 불꽃이 타오르기 전에, 지식의 흡입을 막아내는 게 좋을 것이다.
   źródło: RailwayDungeonNode3.json :: dataList[id=306].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 51%]</b></color>\n\nAn odd, miasmatic scent of a burning candle fills this place.\nIn it is the one who seeks the truth. Its massive eyes roll about to capture every little detail and knowledge.\nIt would be best that we stop it from consuming more knowledge before the flames of truth begin burning.
   PL: <color=#990000><b> [Współczynnik załamania: 51%] </b></color>\n\nPrzestrzeń wypełnia osobliwy zapach palonej świecy.\nW środku czeka poszukiwacz prawdy, toczący ogromnymi gałkami ocznymi, jakby chciał pochłonąć każdą literę wiedzy.\nLepiej powstrzymać go przed dalszym chłonięciem wiedzy, zanim zapłonie ogień prawdy.
329. [Tryby lochów i Kolei Refrakcji [307] — tytuł] 제 7 역 : 우화
   źródło: RailwayDungeonNode3.json :: dataList[id=307].title
   limit: do 40 znaków
   EN: Station #7: Eclosion
   PL: Stacja 7: Przeobrażenie
330. [Tryby lochów i Kolei Refrakcji [307] — opis] <color=#990000><b> [굴절률 : 66%] </b></color>\n\n노을빛으로 감싸여진 열기가 벌써 이 곳까지 치닫고 있다.\n잠시 닿기만 해도 불타 없어질 것만 같이 뜨겁지만, 어쩌면 그 불길 안에 안겼을 때 다시 없을 따스함을 느낄지도 모른다는 생각이 들었다.\n불꽃 속에서 우화한 가능성이, 우리를 천천히 유혹하는 것만 같다.
   źródło: RailwayDungeonNode3.json :: dataList[id=307].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 66%]</b></color>\n\nThe heat from the flaming sunset can be felt all the way from here.\nA mere brush against its flames will burn everything to ashes, but its fiery embrace may be a warmth that cannot be found anywhere else.\nThe potential, born again from the flames, gently beckons us.
   PL: <color=#990000><b> [Współczynnik załamania: 66%] </b></color>\n\nŻar skąpany w barwach zachodu słońca dociera aż tutaj.\nChoć jedno muśnięcie spopieliłoby wszystko na proch, przemyka myśl, że w objęciach tych płomieni kryje się niespotykane nigdzie indziej ciepło.\nMożliwość przeobrażona w ogniu zdaje się powoli nas kusić.
331. [Tryby lochów i Kolei Refrakcji [308] — tytuł] 제 8 역 : 정시
   źródło: RailwayDungeonNode3.json :: dataList[id=308].title
   limit: do 40 znaków
   EN: Station #8: Interlude
   PL: Stacja 8: Postój
332. [Tryby lochów i Kolei Refrakcji [308] — opis] <color=#990000><b> [굴절률 : ??%] </b></color>\n\n묵직한 소리가 한차례 낮게 울려 퍼진다.\n톱니는 째깍, 째깍 돌아가다가 까드득하는 소리를 내면서 멈추어 버렸다.\n이 공간을 벗어나면, 다시 톱니는 움직이기 시작할 것이다.\n다음 역으로 떠나기 전에, 채비를 해두자.
   źródło: RailwayDungeonNode3.json :: dataList[id=308].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
333. [Tryby lochów i Kolei Refrakcji [309] — tytuł] 제 9 역 : 백화
   źródło: RailwayDungeonNode3.json :: dataList[id=309].title
   limit: do 40 znaków
   EN: Station #9: Pallidification
   PL: Stacja 9: Zblednięcie
334. [Tryby lochów i Kolei Refrakcji [309] — opis] <color=#990000><b> [굴절률 : 75%] </b></color>\n\n누군가에게 마음을 덮인 자들이 기어 내려온다.\n흰색 보다도 더욱 하얀, 창백한 빛깔을 가진 자들이.\n텅 빈 도화지가 되어버린 그들은 무슨 색으로 되어있었던 걸까.
   źródło: RailwayDungeonNode3.json :: dataList[id=309].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 14%]</b></color>\n\nThey crawl down and appear before us, those whose hearts were painted over.\nThey are pallid, whiter than white.\nWhat were their colors before something painted over them and turned them into empty canvases?
   PL: <color=#990000><b> [Współczynnik załamania: 75%] </b></color>\n\nWypełzają ku nam ci, których serca zostały zamalowane.\nIstoty bielsze od samej bieli, o trupio bladej barwie.\nJakie kolory nosiły, zanim stały się pustym płótnem?
335. [Tryby lochów i Kolei Refrakcji [310] — tytuł] 제 10 역 : 세뇌
   źródło: RailwayDungeonNode3.json :: dataList[id=310].title
   limit: do 40 znaków
   EN: Station #10: Brainwash
   PL: Stacja 10: Pranie mózgu
336. [Tryby lochów i Kolei Refrakcji [310] — opis] <color=#990000><b> [굴절률 : 83%] </b></color>\n\n마음을 덮인 자가 있다면, 마음을 덮은 자도 있을 것이다.\n열차가 멈춰서자 무리를 이끄는 자의 의기양양한 모습이 멀찍이 보인다.\n마치 마중이라도 나온 듯이, 우리의 마음조차 덮으려는 듯이.\n우리도 무기를 들고 맞이해 주도록 하자.
   źródło: RailwayDungeonNode3.json :: dataList[id=310].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 83%]</b></color>\n\nIf there are those whose hearts are painted, then there is one who paints hearts.\nWhen the train comes to a stop, I can see from a distance a confident figure. She is flanked by her followers.\nShe stands as though to greet us, to paint over our hearts as well.\nThen we will meet her with our weapons drawn.
   PL: <color=#990000><b> [Współczynnik załamania: 83%] </b></color>\n\nSkoro istnieją ci o zamalowanych sercach, musi istnieć też ten, kto je zamalował.\nGdy pociąg staje, w oddali rysuje się triumfalna sylwetka przewodząca gromadzie.\nJakby wyszła nam na powitanie, gotowa zamalować również nasze serca.\nPowitajmy ją z dobytymi broniami.
337. [Tryby lochów i Kolei Refrakcji [311] — tytuł] 제 11 역 : 화등
   źródło: RailwayDungeonNode3.json :: dataList[id=311].title
   limit: do 40 znaków
   EN: Station #11: Gaslight
   PL: Stacja 11: Lampa gazowa
338. [Tryby lochów i Kolei Refrakcji [311] — opis] <color=#990000><b> [굴절률 : 89%] </b></color>\n\n이전 역에서 분명히 쓰러트렸다고 생각했지만.\n마음을 덮는 자는 더욱 흉측한 몰골로 우리 앞에 다시 모습을 드러낸다.\n이제 추종자는 눈에 띄지 않지만... 어쩐지, 그 모든 추종자가 그자의 안에 있는 것만 같기도 하다.\n팔뚝에 붙은, 여리게 흔들리는 불꽃에 시선을 팔아서는 안된다.\n저 자에게 집중하자.
   źródło: RailwayDungeonNode3.json :: dataList[id=311].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 89%]</b></color>\n\nI thought we had defeated her in the previous Station, but…\nThe one who paints hearts had only grown even more hideous.\nShe is no longer flanked by her followers, yet… it feels as though they are now within her.\nWe mustn’t let ourselves be distracted by the flickering, dancing flames on her weapon arm.\nFocus on her instead.
   PL: <color=#990000><b> [Współczynnik załamania: 89%] </b></color>\n\nZdawało się, że na poprzedniej stacji już ją powaliliśmy.\nTa, która zamalowuje serca, staje jednak przed nami w jeszcze bardziej potwornej postaci.\nNie widać już jej popleczników… a jednak ma się wrażenie, jakby wszyscy tkwili teraz w jej wnętrzu.\nNie wolno dać się zahipnotyzować drżącemu płomykowi na jej ramieniu.\nSkupmy wzrok na niej samej.
339. [Tryby lochów i Kolei Refrakcji [312] — tytuł] 제 12 역 : 정시
   źródło: RailwayDungeonNode3.json :: dataList[id=312].title
   limit: do 40 znaków
   EN: Station #12: Interlude
   PL: Stacja 12: Postój
340. [Tryby lochów i Kolei Refrakcji [312] — opis] <color=#990000><b> [굴절률 : ??%] </b></color>\n\n묵직한 소리가 한차례 낮게 울려 퍼진다.\n톱니는 째깍, 째깍 돌아가다가 까드득하는 소리를 내면서 멈추어 버렸다.\n이 공간을 벗어나면, 다시 톱니는 움직이기 시작할 것이다.\n다음 역으로 떠나기 전에, 채비를 해두자.
   źródło: RailwayDungeonNode3.json :: dataList[id=312].desc
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Tryby lochów i Kolei Refrakcji [313] — tytuł] 종 착 역 : 나선
   źródło: RailwayDungeonNode3.json :: dataList[id=313].title
   limit: do 40 znaków
   EN: Terminus: Spiral
   PL: Stacja końcowa: Spirala
342. [Tryby lochów i Kolei Refrakcji [313] — opis] <color=#990000><b> [굴절률 : 99%] </b></color>\n\n지하의 긴 터널을 빠져나와, 마침내 종착에 다다르자, 그곳에 황금향이 있었다.\n이미 멀리에서부터, 기이한 쇳소리가 들려온다.\n듣기 거북하진 않지만... 너무나 깊은 곳까지 그 소리가 침투하는 기분이 든다.\n배배 꼬인 무형의 감각이 뇌를 전부 헤집어 놓기 전에, 끝장을 내야 한다.
   źródło: RailwayDungeonNode3.json :: dataList[id=313].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, <b>, </b>, </color>, \n
   EN: <color=#990000><b>[Refraction Rate: 99%]</b></color>\n\nWe emerge from the long tunnel and arrive at the Terminus; there lies the land of gold.\nI can hear an odd, metallic noise echoing from the distance.\nIt’s not the kind of metallic noise that makes one shudder, but the sound digs deep under our skin.\nWe have to finish this fight before this twisted and formless sensation scrambles our brains.
   PL: <color=#990000><b> [Współczynnik załamania: 99%] </b></color>\n\nPo wyjeździe z długiego podziemnego tunelu docieramy wreszcie na stację końcową — do złotej krainy.\nJuż z oddali niesie się osobliwy, metaliczny dźwięk.\nNie drażni uszu… lecz zdaje się przenikać zbyt głęboko pod skórę.\nMusimy zakończyć to starcie, zanim to poskręcane, bezkształtne wrażenie doszczętnie zmąci nam zmysły.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode4
- plik gry: `RailwayDungeonNode4.json`

343. [Tryby lochów i Kolei Refrakcji [401] — tytuł] 제 1 구간 : 연회-정저-왜곡
   źródło: RailwayDungeonNode4.json :: dataList[id=401].title
   limit: do 60 znaków
   EN: Section #1 : Banquet/Well Basin/Twisted
   PL: Odcinek 1: Bankiet–Dno Studni–Wypaczenie
344. [Tryby lochów i Kolei Refrakcji [402] — tytuł] 제 4 역 : 휴연
   źródło: RailwayDungeonNode4.json :: dataList[id=402].title
   limit: do 40 znaków
   EN: Station #4 : Interlude
   PL: Stacja 4: Antrakt
345. [Tryby lochów i Kolei Refrakcji [403] — tytuł] 제 2 구간 : 타정-운무-골육
   źródło: RailwayDungeonNode4.json :: dataList[id=403].title
   limit: do 60 znaków
   EN: Section #2 : Chiseling/Cloudbrume/Boneflesh
   PL: Odcinek 2: Dłutowanie–Mgławica–Ciało i Kość
346. [Tryby lochów i Kolei Refrakcji [404] — tytuł] 제 8 역 : 휴연
   źródło: RailwayDungeonNode4.json :: dataList[id=404].title
   limit: do 40 znaków
   EN: Station #8 : Interlude
   PL: Stacja 8: Antrakt
347. [Tryby lochów i Kolei Refrakcji [405] — tytuł] 제 3 구간 : 위작-몽상
   źródło: RailwayDungeonNode4.json :: dataList[id=405].title
   limit: do 50 znaków
   EN: Section #3 : Forgery/Dreaming
   PL: Odcinek 3: Falsyfikat–Marzenie
348. [Tryby lochów i Kolei Refrakcji [406] — tytuł] 제 11 역 : 휴연
   źródło: RailwayDungeonNode4.json :: dataList[id=406].title
   limit: do 40 znaków
   EN: Station #11 : Interlude
   PL: Stacja 11: Antrakt
349. [Tryby lochów i Kolei Refrakcji [407] — tytuł] 제 4 구간 : 난관-향연
   źródło: RailwayDungeonNode4.json :: dataList[id=407].title
   limit: do 50 znaków
   EN: Section #4 : Adamantine Wall/Feast
   PL: Odcinek 4: Zapora–Uczta

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode5
- plik gry: `RailwayDungeonNode5.json`

350. [Tryby lochów i Kolei Refrakcji [501] — tytuł] 제 1 구간 : 연착-수렵-원류-분무
   źródło: RailwayDungeonNode5.json :: dataList[id=501].title
   limit: do 70 znaków
   EN: Section #1 : Attachment/Hunt/Fountainhead/Misting
   PL: Odcinek 1: Przywiązanie–Łowy–Źródło–Rozpylenie
351. [Tryby lochów i Kolei Refrakcji [502] — tytuł] 제 2 구간 : 격철-광분-망각
   źródło: RailwayDungeonNode5.json :: dataList[id=502].title
   limit: do 60 znaków
   EN: Section #2 : Ironstrike/Rampage/Oblivion
   PL: Odcinek 2: Kurek–Szał–Zapomnienie
352. [Tryby lochów i Kolei Refrakcji [503] — tytuł] 제 3 구간 : 모성-반역-혈죄-갈망
   źródło: RailwayDungeonNode5.json :: dataList[id=503].title
   limit: do 70 znaków
   EN: Section #3 : Motherhood/Treason/Blood Sin/Yearning
   PL: Odcinek 3: Macierzyństwo–Zdrada–Grzech Krwi–Pragnienie

## Tryby lochów i Kolei Refrakcji: RailwayDungeonNode6
- plik gry: `RailwayDungeonNode6.json`

353. [Tryby lochów i Kolei Refrakcji [601] — tytuł] 제 1 구간 : 현의
   źródło: RailwayDungeonNode6.json :: dataList[id=601].title
   limit: do 50 znaków
   EN: Section #1 : Weighing of Robes
   PL: Odcinek 1: Ważenie Szat
354. [Tryby lochów i Kolei Refrakcji [602] — tytuł] 제 2 구간 : 염오
   źródło: RailwayDungeonNode6.json :: dataList[id=602].title
   limit: do 40 znaków
   EN: Section #2 : Tarnishing
   PL: Odcinek 2: Skalanie
355. [Tryby lochów i Kolei Refrakcji [603] — tytuł] 제 3 구간 : 동심-현상
   źródło: RailwayDungeonNode6.json :: dataList[id=603].title
   limit: do 70 znaków
   EN: Section #3 : Heart of Innocence - Face of Things
   PL: Odcinek 3: Niewinne Serce–Oblicze Rzeczy
356. [Tryby lochów i Kolei Refrakcji [604] — tytuł] 제 4 구간 : 반착-탐닉-몽매
   źródło: RailwayDungeonNode6.json :: dataList[id=604].title
   limit: do 80 znaków
   EN: Section #4 : Tangled Knots - Drowning Desire - Blind Folly
   PL: Odcinek 4: Splot–Zatracenie–Zaślepienie
357. [Tryby lochów i Kolei Refrakcji [605] — tytuł] 제 5 구간 : 도래
   źródło: RailwayDungeonNode6.json :: dataList[id=605].title
   limit: do 40 znaków
   EN: Section #5 : Advent
   PL: Odcinek 5: Nadejście

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName1-1
- plik gry: `RailwayDungeonStationName1-1.json`

358. [Tryby lochów i Kolei Refrakcji [1] — tekst] 1호선 진입 전
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=0].content
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Tryby lochów i Kolei Refrakcji [1] — tekst] 시착역 - 조우
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=1].content
   limit: do 120 znaków
   EN: First Stop - Contact
   PL: Stacja początkowa — Spotkanie
360. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제2역 - 원복
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=2].content
   limit: do 120 znaków
   EN: Station #2 - Restoration
   PL: Stacja 2 — Przywrócenie
361. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제3역 - 침잠
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=3].content
   limit: do 120 znaków
   EN: Station #3 - Sinkage
   PL: Stacja 3 — Zatonięcie
362. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제4역 - 재회
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=4].content
   limit: do 120 znaków
   EN: Station #4 - Reunion
   PL: Stacja 4 — Ponowne spotkanie
363. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제5역 - 절연
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=5].content
   limit: do 120 znaków
   EN: Station #5 - Insulation
   PL: Stacja 5 — Izolacja
364. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제6역 - 선발
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=6].content
   limit: do 120 znaków
   EN: Station #6 - Pickup
   PL: Stacja 6 — Selekcja
365. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제7역 - 무수
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=7].content
   limit: do 120 znaków
   EN: Station #7 - Headlessness
   PL: Stacja 7 — Bezgłowość
366. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제8역 - 존재
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=8].content
   limit: do 120 znaków
   EN: Station #8 - Existence
   PL: Stacja 8 — Istnienie
367. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제9역 - 혈청
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=9].content
   limit: do 120 znaków
   EN: Station #9 - Serum
   PL: Stacja 9 — Surowica
368. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제10역 - 아설
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=10].content
   limit: do 120 znaków
   EN: Station #10 - Forked Tongue
   PL: Stacja 10 — Rozwidlony język
369. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제11역 - 통전
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=11].content
   limit: do 120 znaków
   EN: Station #11 - Energization
   PL: Stacja 11 — Przewodnictwo
370. [Tryby lochów i Kolei Refrakcji [1] — tekst] 제12역 - 순수
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=12].content
   limit: do 120 znaków
   EN: Station #12 - Purity
   PL: Stacja 12 — Czystość
371. [Tryby lochów i Kolei Refrakcji [1] — tekst] 종착역 - 무아
   źródło: RailwayDungeonStationName1-1.json :: dataList[id=1].nameList[id=13].content
   limit: do 120 znaków
   EN: Last Stop - Non-self
   PL: Stacja końcowa — Nie-ja

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName1001
- plik gry: `RailwayDungeonStationName1001.json`

372. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 1호선 진입 전
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=0].content
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 1호선 진입 전
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=0].shortName
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 시착역 - 조우
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=1].content
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 시착역 - 조우
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=1].shortName
   (powtórzenie elementu 282 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제2역 - 원복
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=2].content
   limit: do 120 znaków
   EN: Station #2: Restoration
   PL: Stacja 2 — Przywrócenie
377. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제2역 - 원복
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=2].shortName
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제3역 - 침잠
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=3].content
   limit: do 120 znaków
   EN: Station #3: Sinkage
   PL: Stacja 3 — Zatonięcie
379. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제3역 - 침잠
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=3].shortName
   (powtórzenie elementu 378 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제4역 - 재회
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=4].content
   limit: do 120 znaków
   EN: Station #4: Reunion
   PL: Stacja 4 — Ponowne spotkanie
381. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제4역 - 재회
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=4].shortName
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제5역 - 절연
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=5].content
   limit: do 120 znaków
   EN: Station #5: Insulation
   PL: Stacja 5 — Izolacja
383. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제5역 - 절연
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=5].shortName
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제6역 - 선발
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=6].content
   limit: do 120 znaków
   EN: Station #6: Pickup
   PL: Stacja 6 — Selekcja
385. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제6역 - 선발
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=6].shortName
   (powtórzenie elementu 384 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제7역 - 무수
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=7].content
   limit: do 120 znaków
   EN: Station #7: Headlessness
   PL: Stacja 7 — Bezgłowość
387. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제7역 - 무수
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=7].shortName
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제8역 - 존재
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=8].content
   limit: do 120 znaków
   EN: Station #8: Existence
   PL: Stacja 8 — Istnienie
389. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제8역 - 존재
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=8].shortName
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제9역 - 혈청
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=9].content
   limit: do 120 znaków
   EN: Station #9: Serum
   PL: Stacja 9 — Surowica
391. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제9역 - 혈청
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=9].shortName
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제10역 - 아설
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=10].content
   limit: do 120 znaków
   EN: Station #10: Forked Tongue
   PL: Stacja 10 — Rozwidlony język
393. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제10역 - 아설
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=10].shortName
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제11역 - 통전
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=11].content
   limit: do 120 znaków
   EN: Station #11: Energization
   PL: Stacja 11 — Przewodnictwo
395. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제11역 - 통전
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=11].shortName
   (powtórzenie elementu 394 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 제12역 - 순수
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=12].content
   limit: do 120 znaków
   EN: Station #12: Purity
   PL: Stacja 12 — Czystość
397. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 제12역 - 순수
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=12].shortName
   (powtórzenie elementu 396 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Tryby lochów i Kolei Refrakcji [1001] — tekst] 종착역 - 무아
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=13].content
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
399. [Tryby lochów i Kolei Refrakcji [1001] — nazwa skrócona] 종착역 - 무아
   źródło: RailwayDungeonStationName1001.json :: dataList[id=1001].nameList[id=13].shortName
   (powtórzenie elementu 294 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName1002
- plik gry: `RailwayDungeonStationName1002.json`

400. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 2호선 진입 전
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=0].content
   limit: do 120 znaków
   EN: Line 2 Boarding
   PL: Przed wejściem na Linię 2
401. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 2호선 진입 전
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=0].shortName
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
402. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 제 1 순환 : 저주-사역-낙우
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=1].content
   (powtórzenie elementu 274 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 제 1 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=1].shortName
   limit: do 40 znaków
   EN: The First Cycle
   PL: Cykl 1
404. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 제 2 순환 : 저주-이취-착취-사역
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=2].content
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 제 2 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=2].shortName
   limit: do 40 znaków
   EN: The Second Cycle
   PL: Cykl 2
406. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 제 3 순환 : 저주-체납-이취-낙우
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=3].content
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 제 3 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=3].shortName
   limit: do 40 znaków
   EN: The Third Cycle
   PL: Cykl 3
408. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 제 4 순환 : 저주-유인-이취-체납-순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=4].content
   (powtórzenie elementu 277 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 제 4 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=4].shortName
   limit: do 40 znaków
   EN: The Fourth Cycle
   PL: Cykl 4
410. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 최종 순환 : 저주-사역-낙우-체납-유인-착취-이취-순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=5].content
   limit: do 120 znaków
   EN: <size=75%>Final Cycle: Curse-Servitude-Rainfall-Arrears-Lure-Exploitation-Odd Stench-Cycle</size>
   PL: Ostatni Cykl: Klątwa–Kierat–Ulewa–Zwłoka–Wabik–Wyzysk–Odór–Cykl
411. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 최종 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=5].shortName
   limit: do 40 znaków
   EN: The Final Cycle
   PL: Ostatni Cykl
412. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 최종 순환 : 저주-사역-낙우-체납-유인-착취-이취-순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=6].content
   (powtórzenie elementu 410 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 최종 순환
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=6].shortName
   (powtórzenie elementu 411 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Tryby lochów i Kolei Refrakcji [1002] — tekst] 종착역 : 정원
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=7].content
   (powtórzenie elementu 279 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Tryby lochów i Kolei Refrakcji [1002] — nazwa skrócona] 종착역
   źródło: RailwayDungeonStationName1002.json :: dataList[id=1002].nameList[id=7].shortName
   limit: do 40 znaków
   EN: Terminus
   PL: Stacja końcowa

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName2
- plik gry: `RailwayDungeonStationName2.json`

416. [Tryby lochów i Kolei Refrakcji [2] — tekst] 2호선 진입 전
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=0].content
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Tryby lochów i Kolei Refrakcji [2] — tekst] 시착역 - 저주
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=1].content
   limit: do 120 znaków
   EN: First Stop: Curse
   PL: Stacja początkowa — Klątwa
418. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 시착역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=1].shortName
   limit: do 40 znaków
   EN: First Stop
   PL: Stacja pocz.
419. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 2역 - 사역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=2].content
   limit: do 120 znaków
   EN: Station #2: Servitude
   PL: Stacja 2 — Kierat
420. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 2역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=2].shortName
   limit: do 40 znaków
   EN: Station #2
   PL: Stacja 2
421. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 3역 - 낙우
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=3].content
   limit: do 120 znaków
   EN: Station #3: Rainfall
   PL: Stacja 3 — Ulewa
422. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 3역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=3].shortName
   limit: do 40 znaków
   EN: Station #3
   PL: Stacja 3
423. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 4역 - 체납
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=4].content
   limit: do 120 znaków
   EN: Station #4: Arrears
   PL: Stacja 4 — Zwłoka
424. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 4역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=4].shortName
   limit: do 40 znaków
   EN: Station #4
   PL: Stacja 4
425. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 5역 - 유인
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=5].content
   limit: do 120 znaków
   EN: Station #5: The Lure
   PL: Stacja 5 — Wabik
426. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 5역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=5].shortName
   limit: do 40 znaków
   EN: Station #5
   PL: Stacja 5
427. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 6역 - 착취
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=6].content
   limit: do 120 znaków
   EN: Station #6: Exploitation
   PL: Stacja 6 — Wyzysk
428. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 6역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=6].shortName
   limit: do 40 znaków
   EN: Station #6
   PL: Stacja 6
429. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 7역 - 이취
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=7].content
   limit: do 120 znaków
   EN: Station #7: Odd Stench
   PL: Stacja 7 — Odór
430. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 7역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=7].shortName
   limit: do 40 znaków
   EN: Station #7
   PL: Stacja 7
431. [Tryby lochów i Kolei Refrakcji [2] — tekst] 제 8역 - 순환
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=8].content
   limit: do 120 znaków
   EN: Station #8: Cycle
   PL: Stacja 8 — Cykl
432. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 제 8역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=8].shortName
   limit: do 40 znaków
   EN: Station #8
   PL: Stacja 8
433. [Tryby lochów i Kolei Refrakcji [2] — tekst] 종착역 - 정원
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=9].content
   limit: do 120 znaków
   EN: Terminus: The Garden
   PL: Stacja końcowa — Ogród
434. [Tryby lochów i Kolei Refrakcji [2] — nazwa skrócona] 종착역
   źródło: RailwayDungeonStationName2.json :: dataList[id=2].nameList[id=9].shortName
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName3
- plik gry: `RailwayDungeonStationName3.json`

435. [Tryby lochów i Kolei Refrakcji [3] — tekst] 3호선 진입 전
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=0].content
   limit: do 120 znaków
   EN: Line 3 Boarding
   PL: Przed wejściem na Linię 3
436. [Tryby lochów i Kolei Refrakcji [3] — tekst] 시착역 - 치륜
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=1].content
   limit: do 120 znaków
   EN: First Stop: Cogwheel
   PL: Stacja początkowa — Tryby
437. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 시착역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=1].shortName
   (powtórzenie elementu 418 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 2역 - 파랑
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=2].content
   limit: do 120 znaków
   EN: Station #2: Waves
   PL: Stacja 2 — Fale
439. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 2역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=2].shortName
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
440. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 3역 - 향수
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=3].content
   limit: do 120 znaków
   EN: Station #3: Nostalgia
   PL: Stacja 3 — Nostalgia
441. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 3역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=3].shortName
   (powtórzenie elementu 422 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 4역 - 정시
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=4].content
   limit: do 120 znaków
   EN: Station #4: Interlude
   PL: Stacja 4 — Postój
443. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 4역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=4].shortName
   (powtórzenie elementu 424 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
444. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 5역 - 고행
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=5].content
   limit: do 120 znaków
   EN: Station #5: Drudgery
   PL: Stacja 5 — Umartwienie
445. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 5역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=5].shortName
   (powtórzenie elementu 426 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 6역 - 진리
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=6].content
   limit: do 120 znaków
   EN: Station #6: Truth
   PL: Stacja 6 — Prawda
447. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 6역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=6].shortName
   (powtórzenie elementu 428 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 7역 - 우화
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=7].content
   limit: do 120 znaków
   EN: Station #7: Eclosion
   PL: Stacja 7 — Przeobrażenie
449. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 7역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=7].shortName
   (powtórzenie elementu 430 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 8역 - 정시
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=8].content
   limit: do 120 znaków
   EN: Station #8: Interlude
   PL: Stacja 8 — Postój
451. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 8역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=8].shortName
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 9역 - 백화
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=9].content
   limit: do 120 znaków
   EN: Station #9: Pallidification
   PL: Stacja 9 — Zblednięcie
453. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 9역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=9].shortName
   limit: do 40 znaków
   EN: Station #9
   PL: Stacja 9
454. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 10역 - 세뇌
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=10].content
   limit: do 120 znaków
   EN: Station #10: Brainwash
   PL: Stacja 10 — Pranie mózgu
455. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 10역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=10].shortName
   limit: do 40 znaków
   EN: Station #10
   PL: Stacja 10
456. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 11역 - 화등
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=11].content
   limit: do 120 znaków
   EN: Station #11: Gaslight
   PL: Stacja 11 — Lampa gazowa
457. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 11역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=11].shortName
   limit: do 40 znaków
   EN: Station #11
   PL: Stacja 11
458. [Tryby lochów i Kolei Refrakcji [3] — tekst] 제 12역 - 정시
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=12].content
   limit: do 120 znaków
   EN: Station #12: Interlude
   PL: Stacja 12 — Postój
459. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 제 12역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=12].shortName
   limit: do 40 znaków
   EN: Station #12
   PL: Stacja 12
460. [Tryby lochów i Kolei Refrakcji [3] — tekst] 종착역 - 나선
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=13].content
   limit: do 120 znaków
   EN: Terminus: The Helix
   PL: Stacja końcowa — Spirala
461. [Tryby lochów i Kolei Refrakcji [3] — nazwa skrócona] 종착역
   źródło: RailwayDungeonStationName3.json :: dataList[id=3].nameList[id=13].shortName
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName4
- plik gry: `RailwayDungeonStationName4.json`

462. [Tryby lochów i Kolei Refrakcji [4] — tekst] 4호선 진입 전
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=0].content
   limit: do 120 znaków
   EN: Line 4 Boarding
   PL: Przed wejściem na Linię 4
463. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 1 구간 : 연회-정저-왜곡
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=1].content
   limit: do 120 znaków
   EN: Section #1
   PL: Odcinek 1: Bankiet–Dno Studni–Wypaczenie
464. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 1 구간
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=1].shortName
   limit: do 40 znaków
   EN: Section #1
   PL: Odcinek 1
465. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 4 역 : 휴연
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=2].content
   (powtórzenie elementu 344 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
466. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 4 역
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=2].shortName
   limit: do 40 znaków
   EN: Station #4
   PL: Stacja 4
467. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 2 구간 : 타정-운무-골육
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=3].content
   limit: do 120 znaków
   EN: Section #2
   PL: Odcinek 2: Dłutowanie–Mgławica–Ciało i Kość
468. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 2 구간
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=3].shortName
   limit: do 40 znaków
   EN: Section #2
   PL: Odcinek 2
469. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 8 역 : 휴연
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=4].content
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
470. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 8 역
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=4].shortName
   limit: do 40 znaków
   EN: Station #8
   PL: Stacja 8
471. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 3 구간 : 위작-몽상
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=5].content
   limit: do 120 znaków
   EN: Section #3
   PL: Odcinek 3: Falsyfikat–Marzenie
472. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 3 구간
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=5].shortName
   limit: do 40 znaków
   EN: Section #3
   PL: Odcinek 3
473. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 11 역 : 휴연
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=6].content
   (powtórzenie elementu 348 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 11 역
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=6].shortName
   limit: do 40 znaków
   EN: Station #11
   PL: Stacja 11
475. [Tryby lochów i Kolei Refrakcji [4] — tekst] 제 4 구간 : 난관-향연
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=7].content
   limit: do 120 znaków
   EN: Section #4
   PL: Odcinek 4: Zapora–Uczta
476. [Tryby lochów i Kolei Refrakcji [4] — nazwa skrócona] 제 4 구간
   źródło: RailwayDungeonStationName4.json :: dataList[id=4].nameList[id=7].shortName
   limit: do 40 znaków
   EN: Section #4
   PL: Odcinek 4

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName5
- plik gry: `RailwayDungeonStationName5.json`

477. [Tryby lochów i Kolei Refrakcji [5] — tekst] 5호선 진행 중
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=0].content
   limit: do 120 znaków
   EN: Line 5 in Progress
   PL: Linia 5 w toku
478. [Tryby lochów i Kolei Refrakcji [5] — tekst] 제 1 구간 : 연착-수렵-원류-분무
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=1].content
   (powtórzenie elementu 350 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Tryby lochów i Kolei Refrakcji [5] — nazwa skrócona] 제 1 구간
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=1].shortName
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Tryby lochów i Kolei Refrakcji [5] — tekst] 제 2 구간 : 격철-광분-망각
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=2].content
   (powtórzenie elementu 351 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Tryby lochów i Kolei Refrakcji [5] — nazwa skrócona] 제 2 구간
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=2].shortName
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
482. [Tryby lochów i Kolei Refrakcji [5] — tekst] 제 3 구간 : 모성-반역-혈죄-갈망
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=3].content
   (powtórzenie elementu 352 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Tryby lochów i Kolei Refrakcji [5] — nazwa skrócona] 제 3 구간
   źródło: RailwayDungeonStationName5.json :: dataList[id=5].nameList[id=3].shortName
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Tryby lochów i Kolei Refrakcji: RailwayDungeonStationName6
- plik gry: `RailwayDungeonStationName6.json`

484. [Tryby lochów i Kolei Refrakcji [6] — tekst] 6호선 진행 중
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=0].content
   limit: do 120 znaków
   EN: Line 6 in Progress
   PL: Linia 6 w toku
485. [Tryby lochów i Kolei Refrakcji [6] — tekst] 제 1 구간 : 현의
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=1].content
   (powtórzenie elementu 353 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Tryby lochów i Kolei Refrakcji [6] — nazwa skrócona] 제 1 구간
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=1].shortName
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Tryby lochów i Kolei Refrakcji [6] — tekst] 제 2 구간 : 염오
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=2].content
   (powtórzenie elementu 354 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Tryby lochów i Kolei Refrakcji [6] — nazwa skrócona] 제 2 구간
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=2].shortName
   (powtórzenie elementu 468 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Tryby lochów i Kolei Refrakcji [6] — tekst] 제 3 구간 : 동심-현상
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=3].content
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Tryby lochów i Kolei Refrakcji [6] — nazwa skrócona] 제 3 구간
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=3].shortName
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Tryby lochów i Kolei Refrakcji [6] — tekst] 제 4 구간 : 반착-탐닉-몽매
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=4].content
   (powtórzenie elementu 356 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Tryby lochów i Kolei Refrakcji [6] — nazwa skrócona] 제 4 구간
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=4].shortName
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Tryby lochów i Kolei Refrakcji [6] — tekst] 제 5 구간 : 도래
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=5].content
   (powtórzenie elementu 357 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Tryby lochów i Kolei Refrakcji [6] — nazwa skrócona] 제 5 구간
   źródło: RailwayDungeonStationName6.json :: dataList[id=6].nameList[id=5].shortName
   limit: do 40 znaków
   EN: Section #5
   PL: Odcinek 5

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI
- plik gry: `RailwayDungeonUI.json`

495. [Tryby lochów i Kolei Refrakcji [clear_turn] — tekst] 클리어 턴
   źródło: RailwayDungeonUI.json :: dataList[id=clear_turn].content
   limit: do 120 znaków
   EN: Clear Turns
   PL: Tury ukończenia
496. [Tryby lochów i Kolei Refrakcji [accumulated_turn] — tekst] 누적 턴
   źródło: RailwayDungeonUI.json :: dataList[id=accumulated_turn].content
   limit: do 120 znaków
   EN: Total Turns
   PL: Łączne tury
497. [Tryby lochów i Kolei Refrakcji [final_accumulated_turn] — tekst] 최종 누적 턴
   źródło: RailwayDungeonUI.json :: dataList[id=final_accumulated_turn].content
   limit: do 120 znaków
   EN: Final Turn Count
   PL: Końcowa liczba tur
498. [Tryby lochów i Kolei Refrakcji [reward_after_clear] — tekst] 클리어 시 보상
   źródło: RailwayDungeonUI.json :: dataList[id=reward_after_clear].content
   limit: do 120 znaków
   EN: Clear Rewards
   PL: Nagrody za ukończenie
499. [Tryby lochów i Kolei Refrakcji [lost_and_found] — tekst] 분실물 보관소
   źródło: RailwayDungeonUI.json :: dataList[id=lost_and_found].content
   limit: do 120 znaków
   EN: Lost & Found
   PL: Biuro Rzeczy Znalezionych
500. [Tryby lochów i Kolei Refrakcji [railway_line] — tekst] {0}호선
   źródło: RailwayDungeonUI.json :: dataList[id=railway_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Line {0}
   PL: Linia {0}
501. [Tryby lochów i Kolei Refrakcji [progressing_railway_line] — tekst] 진행 노선: {0}
   źródło: RailwayDungeonUI.json :: dataList[id=progressing_railway_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Traveling: {0}
   PL: Aktualna trasa: {0}
502. [Tryby lochów i Kolei Refrakcji [select_railway_line] — tekst] 노선도를 선택하세요
   źródło: RailwayDungeonUI.json :: dataList[id=select_railway_line].content
   limit: do 120 znaków
   EN: What Line will you travel?
   PL: Wybierz linię
503. [Tryby lochów i Kolei Refrakcji [stage_info] — tekst] 스테이지 정보
   źródło: RailwayDungeonUI.json :: dataList[id=stage_info].content
   limit: do 120 znaków
   EN: Station Data
   PL: Informacje o stacji
504. [Tryby lochów i Kolei Refrakcji [stage_number] — tekst] 스테이지 {0}
   źródło: RailwayDungeonUI.json :: dataList[id=stage_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Station {0}
   PL: Stacja {0}
505. [Tryby lochów i Kolei Refrakcji [mirror_refraction_railway] — tekst] 거울굴절철도
   źródło: RailwayDungeonUI.json :: dataList[id=mirror_refraction_railway].content
   limit: do 120 znaków
   EN: Refraction Railway
   PL: Kolej Załamania
506. [Tryby lochów i Kolei Refrakcji [mirror_refraction_railway_with_dungeon_name] — tekst] 거울굴절철도 {0}
   źródło: RailwayDungeonUI.json :: dataList[id=mirror_refraction_railway_with_dungeon_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Refraction Railway {0}
   PL: Kolej Załamania — {0}
507. [Tryby lochów i Kolei Refrakcji [accumulated_records] — tekst] 누적 기록
   źródło: RailwayDungeonUI.json :: dataList[id=accumulated_records].content
   limit: do 120 znaków
   EN: Travel Collection
   PL: Archiwum przejazdów
508. [Tryby lochów i Kolei Refrakcji [rank_with_number] — tekst] {0}위
   źródło: RailwayDungeonUI.json :: dataList[id=rank_with_number].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Rank #{0}
   PL: Miejsce #{0}
509. [Tryby lochów i Kolei Refrakcji [open_railway_dungeon_records] — tekst] 기록 열람
   źródło: RailwayDungeonUI.json :: dataList[id=open_railway_dungeon_records].content
   limit: do 120 znaków
   EN: Logs
   PL: Pokaż zapis
510. [Tryby lochów i Kolei Refrakcji [no_more_rewards_remains_desc] — tekst] 수령할 수 있는 보상이 없습니다.
   źródło: RailwayDungeonUI.json :: dataList[id=no_more_rewards_remains_desc].content
   limit: do 120 znaków
   EN: No rewards to claim.
   PL: Brak nagród do odebrania.
511. [Tryby lochów i Kolei Refrakcji [use_enkephalin_module_to_acquire_rewards] — tekst] <color=#990000>엔케팔린 모듈 {0}개</color>를 소모하여\n보상을 수령하시겠습니까?
   źródło: RailwayDungeonUI.json :: dataList[id=use_enkephalin_module_to_acquire_rewards].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}, \n
   EN: Spend <color=#990000>{0} Enkephalin Modules</color>\nto unlock the rewards?
   PL: Wydać <color=#990000>{0} Modułów Enkefaliny</color>,\naby odebrać nagrody?
512. [Tryby lochów i Kolei Refrakcji [able_to_acquire_rewards_without_using_enkephalin_module] — tekst] ※이벤트 기간 동안 추가로 획득한 보상은 엔케팔린 모듈 추가 소모 없이 언제든지 획득할 수 있습니다.
   źródło: RailwayDungeonUI.json :: dataList[id=able_to_acquire_rewards_without_using_enkephalin_module].content
   limit: do 140 znaków
   EN: ※ Once unlocked, you can freely claim the rewards you’ve earned during the event at no additional cost.
   PL: ※ Dodatkowe nagrody zdobyte w trakcie wydarzenia można później odbierać w dowolnej chwili bez ponownego zużywania Modułów Enkefaliny.
513. [Tryby lochów i Kolei Refrakcji [railway_dungeon_ask_for_re_enter] — tekst] <color=#990000>{0}-{1}</color>를 도전 중입니다.\n계속 진행하시겠습니까?
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_ask_for_re_enter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}, {1}, \n
   EN: Currently on <color=#990000>{0} to Station {1}</color>.\nResume your travels?
   PL: Trwa przejazd na etapie <color=#990000>{0}-{1}</color>.\nKontynuować?
514. [Tryby lochów i Kolei Refrakcji [railway_dungeon_current_running] — tekst] {0}-{1} 진행 중
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_current_running].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}-{1} In Progress
   PL: {0}-{1} w toku
515. [Tryby lochów i Kolei Refrakcji [final_clear_accumulated_turn] — tekst] 최종 클리어 누적 턴
   źródło: RailwayDungeonUI.json :: dataList[id=final_clear_accumulated_turn].content
   limit: do 120 znaków
   EN: Final Turn Count
   PL: Końcowa łączna liczba tur
516. [Tryby lochów i Kolei Refrakcji [railway_dungeon_detailed_info] — tekst] 상세 정보
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_detailed_info].content
   limit: do 120 znaków
   EN: Details
   PL: Szczegóły
517. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1_banner_reward_condition_1] — tekst] 거울굴절철도 - {0}단계 클리어
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_1_banner_reward_condition_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Refraction Railway - Clear Station {0}
   PL: Kolej Załamania — ukończ stację {0}
518. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1_banner_reward_condition_2] — tekst] 거울굴절철도 - {0}단계 클리어, 누적 턴 {1} 이하
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_1_banner_reward_condition_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Refraction Railway - Clear Station {0} under {1} total turns
   PL: Kolej Załamania — ukończ stację {0} w maks. {1} łącznych turach
519. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1_banner_reward_condition_3] — tekst] ({0} 까지 위 획득 조건 달성)
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_1_banner_reward_condition_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Complete before {0})
   PL: (Spełnij powyższy warunek przed {0})
520. [Tryby lochów i Kolei Refrakcji [railway_dungeon_banner_reward_condition_title] — tekst] 배너 획득 조건
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_banner_reward_condition_title].content
   limit: do 120 znaków
   EN: Banner Requisites
   PL: Warunki zdobycia sztandaru
521. [Tryby lochów i Kolei Refrakcji [railway_dungeon_banner_reward_unable_over] — tekst] (단, 누적 턴 {0} 초과 시 획득 불가)
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_banner_reward_unable_over].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Unobtainable past {0} total turns)
   PL: (Niedostępne po przekroczeniu {0} łącznych tur)
522. [Tryby lochów i Kolei Refrakcji [no_records_description] — tekst] 기록이 존재하지 않습니다.
   źródło: RailwayDungeonUI.json :: dataList[id=no_records_description].content
   limit: do 120 znaków
   EN: The travelogue is currently empty.
   PL: Brak zapisanych przejazdów.
523. [Tryby lochów i Kolei Refrakcji [recover_after_resting_battle] — tekst] 이번 전투\n휴식 시\n상태 초기화 및\n체력 전체회복
   źródło: RailwayDungeonUI.json :: dataList[id=recover_after_resting_battle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fully recovers\nafter resting\nfor this battle
   PL: Odpoczynek w tej walce\nresetuje stan\ni w pełni leczy PŻ
524. [Tryby lochów i Kolei Refrakcji [railway_dungeon_try_last_node] — tekst] 종착역에 입장하면 이전 역으로 되돌아갈 수 없습니다.\n\n종착역에 입장하시겠습니까?
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_try_last_node].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You cannot go back once you enter the Terminus.\n\nEnter the Terminus?
   PL: Po wejściu na Stację końcową nie można wrócić do poprzednich stacji.\n\nWejść na Stację końcową?
525. [Tryby lochów i Kolei Refrakcji [railway_dungeon_ask_stop_desc] — tekst] 거울굴절철도 탐사를 그만두시겠습니까?
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_ask_stop_desc].content
   limit: do 120 znaków
   EN: Would you like to disembark from the Refraction Railway?
   PL: Przerwać wyprawę Koleją Załamania?
526. [Tryby lochów i Kolei Refrakcji [railway_dungeon_finished_description] — tekst] ※ 동일한 턴 수의 기록이 추가될 경우 사망 상태가 더 많은 기록을 덮어쓰며,\n이 역시 동일할 경우 가장 오래된 기록을 덮어씁니다.
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_finished_description].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ If two records have the same Total Turns, the one with the higher death count will be overwritten.\nIf the death counts are also identical, then the older one will be overwritten.
   PL: ※ W przypadku równej liczby tur nadpisany zostanie zapis z większą liczbą zgonów,\na jeśli ta również jest identyczna — najstarszy zapis.
527. [Tryby lochów i Kolei Refrakcji [railway_dungeon_open_duration] — tekst] 운행기간
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_open_duration].content
   limit: do 120 znaków
   EN: Operation Period
   PL: Okres kursowania
528. [Tryby lochów i Kolei Refrakcji [railway_dungeon_current_station] — tekst] {0}
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_current_station].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}
   PL: {0}
529. [Tryby lochów i Kolei Refrakcji [railway_dungeon_route_map] — tekst] 노선 운행도
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_route_map].content
   limit: do 120 znaków
   EN: Line Diagram
   PL: Schemat trasy
530. [Tryby lochów i Kolei Refrakcji [railway_dungeon_resume_operation] — tekst] 운영 재개
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_resume_operation].content
   limit: do 120 znaków
   EN: Continue Travels
   PL: Wznów przejazd
531. [Tryby lochów i Kolei Refrakcji [railway_dungeon_stop_operation] — tekst] 운영 중단
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_stop_operation].content
   limit: do 120 znaków
   EN: Disembark
   PL: Zakończ przejazd
532. [Tryby lochów i Kolei Refrakcji [railway_dungeon_station_info] — tekst] 노선 정보
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_station_info].content
   limit: do 120 znaków
   EN: Line Info
   PL: Informacje o linii
533. [Tryby lochów i Kolei Refrakcji [railway_dungeon_operation_closed] — tekst] 운행 종료
   źródło: RailwayDungeonUI.json :: dataList[id=railway_dungeon_operation_closed].content
   limit: do 120 znaków
   EN: Line Closure
   PL: Kursowanie zakończone
534. [Tryby lochów i Kolei Refrakcji [final_clear_accumulated_round] — tekst] 최종 클리어 누적 라운드
   źródło: RailwayDungeonUI.json :: dataList[id=final_clear_accumulated_round].content
   limit: do 120 znaków
   EN: Final Cycle Count
   PL: Końcowa liczba cykli
535. [Tryby lochów i Kolei Refrakcji [railway_clear_date] — tekst] 기록 일자
   źródło: RailwayDungeonUI.json :: dataList[id=railway_clear_date].content
   limit: do 120 znaków
   EN: Record Date
   PL: Data zapisu
536. [Tryby lochów i Kolei Refrakcji [railway_clear_turn_count] — tekst] 누적 클리어 턴 수
   źródło: RailwayDungeonUI.json :: dataList[id=railway_clear_turn_count].content
   limit: do 120 znaków
   EN: Total Clear Turn Count
   PL: Łączna liczba tur ukończenia
537. [Tryby lochów i Kolei Refrakcji [railway_clear_turn_count_by_stage] — tekst] 구간별 클리어 턴 수
   źródło: RailwayDungeonUI.json :: dataList[id=railway_clear_turn_count_by_stage].content
   limit: do 120 znaków
   EN: Clear Turn Count by Section
   PL: Tury ukończenia wg odcinków

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_1001
- plik gry: `RailwayDungeonUI_1001.json`

538. [Tryby lochów i Kolei Refrakcji [railwayBannerTitle] — tekst] 거울굴절철도 개방
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railwayBannerTitle].content
   limit: do 120 znaków
   EN: Refraction Railway Opening
   PL: Otwarcie Kolei Załamania
539. [Tryby lochów i Kolei Refrakcji [railwayDungeonEntranceItemTitle_1001] — tekst] 1호선
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railwayDungeonEntranceItemTitle_1001].content
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Tryby lochów i Kolei Refrakcji [railwayDungeonEntranceItemTitle_5] — tekst] 5호선
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railwayDungeonEntranceItemTitle_5].content
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1001_entrance_recommended_level] — tekst] - 인격 : 동기화 4단계, 레벨 55 (최대 레벨 제한 : 55)
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_1001_entrance_recommended_level].content
   limit: do 120 znaków
   EN: - Identities : Uptie Tier 4, Level 55 (Level Cap: 55)
   PL: - Tożsamości: Synchronizacja poz. 4, poziom 55 (limit poziomu: 55)
542. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1001_entrance_recommended_gacksung] — tekst] - E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_1001_entrance_recommended_gacksung].content
   limit: do 120 znaków
   EN: - E.G.O : Threadspin Tier 4
   PL: - E.G.O: Splot Nici poz. 4
543. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_openCondition_title] — tekst] 개방 조건
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_advice_openCondition_title].content
   limit: do 120 znaków
   EN: Unlock Requirements
   PL: Warunki odblokowania
544. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_level_title] — tekst] 입장 권장 사양
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_advice_level_title].content
   limit: do 120 znaków
   EN: Recommended Level & Tier
   PL: Zalecane parametry
545. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_1001_openCondition_desc] — tekst] 8장 클리어
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_advice_1001_openCondition_desc].content
   limit: do 120 znaków
   EN: Clear Canto VIII
   PL: Ukończ Canto VIII
546. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_1001_level_desc] — tekst] - 인격 : 동기화 4단계, 레벨 55\n- E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_advice_1001_level_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Identities : Uptie Tier 4, Level 55\n- E.G.O : Threadspinning Tier 4
   PL: - Tożsamości: Synchronizacja poz. 4, poziom 55\n- E.G.O: Splot Nici poz. 4
547. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1001_banner_reward_condition_1] — tekst] 누적 턴 수 <color=#005823>{0}</color>턴 이하로 1호선 BokGak 클리어 시 획득할 수 있습니다.
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_1001_banner_reward_condition_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#005823>, </color>, {0}
   EN: Obtain by clearing Line 1 BokGak under <color=#005823>{0}</color> total turns.
   PL: Zdobywane za ukończenie Linii 1 BokGak w maks. <color=#005823>{0}</color> łącznych turach.
548. [Tryby lochów i Kolei Refrakcji [railway_1001_must_participate_all] — tekst] 편성되지 않은 인격이 존재합니다.
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_1001_must_participate_all].content
   limit: do 120 znaków
   EN: Please Deploy all Sinners.
   PL: Nie wszyscy Grzesznicy zostali wystawieni.
549. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1001_reward_condition_special_ticket] — tekst] 누적 턴 수 120턴 이하로 1호선 BokGak 클리어 시 획득할 수 있습니다.
   źródło: RailwayDungeonUI_1001.json :: dataList[id=railway_dungeon_1001_reward_condition_special_ticket].content
   limit: do 120 znaków
   EN: Obtain by clearing Line 1 BokGak under 120 total turns.
   PL: Zdobywane za ukończenie Linii 1 BokGak w maks. 120 łącznych turach.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_1002
- plik gry: `RailwayDungeonUI_1002.json`

550. [Tryby lochów i Kolei Refrakcji [ui_railway_dungeon_rotation_count] — tekst] 순환 횟수
   źródło: RailwayDungeonUI_1002.json :: dataList[id=ui_railway_dungeon_rotation_count].content
   limit: do 120 znaków
   EN: Cycle Count
   PL: Liczba cykli
551. [Tryby lochów i Kolei Refrakcji [ui_railway_dungeon_upper_status_ui_rotation_count] — tekst] 순환 완료 횟수
   źródło: RailwayDungeonUI_1002.json :: dataList[id=ui_railway_dungeon_upper_status_ui_rotation_count].content
   limit: do 120 znaków
   EN: Completed Cycle Count
   PL: Ukończone cykle
552. [Tryby lochów i Kolei Refrakcji [ui_railway_dungeon_reward_condition_clear_boss_after_cycle] — tekst] 종착역 클리어 시
   źródło: RailwayDungeonUI_1002.json :: dataList[id=ui_railway_dungeon_reward_condition_clear_boss_after_cycle].content
   limit: do 120 znaków
   EN: Clear the Terminus
   PL: Po ukończeniu Stacji końcowej
553. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1002_banner_reward_condition_1] — tekst] 순환 {1} 이상, 누적 턴 수 <color=#005823>{0}</color>턴 이하로 2호선 BokGak 클리어 시 획득할 수 있습니다.
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_dungeon_1002_banner_reward_condition_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#005823>, </color>, {1}, {0}
   EN: Obtain by clearing Line 2 BokGak at {1} or more Cycle Counts and under <color=#005823>{0}</color> total turns.
   PL: Zdobywane za ukończenie Linii 2 BokGak przy min. {1} cyklach i w maks. <color=#005823>{0}</color> łącznych turach.
554. [Tryby lochów i Kolei Refrakcji [railway_1002_must_participate_all] — tekst] 편성되지 않은 인격이 존재합니다.
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_1002_must_participate_all].content
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Tryby lochów i Kolei Refrakcji [railway_dungeon_1002_change_rotation_alarm] — tekst] {0}번째 순환 진행 완료
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_dungeon_1002_change_rotation_alarm].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cycle {0} Completed
   PL: Ukończono {0}. cykl
556. [Tryby lochów i Kolei Refrakcji [railway_1002_bgm_reward_desc] — tekst] 거울굴절철도 2호선 BokGak 클리어
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_1002_bgm_reward_desc].content
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 2 BokGak
   PL: Ukończ Kolej Załamania — Linię 2 BokGak
557. [Tryby lochów i Kolei Refrakcji [railway_1001_bgm_reward_desc] — tekst] 거울굴절철도 1호선 BokGak 클리어
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_1001_bgm_reward_desc].content
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 1 BokGak
   PL: Ukończ Kolej Załamania — Linię 1 BokGak
558. [Tryby lochów i Kolei Refrakcji [railway_6_bgm_reward_desc] — tekst] 거울굴절철도 6호선 클리어
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_6_bgm_reward_desc].content
   limit: do 120 znaków
   EN: Clear Refraction Railway Line 6
   PL: Ukończ Kolej Załamania — Linię 6
559. [Tryby lochów i Kolei Refrakcji [railway_clear_reward_popup_title] — tekst] 클리어 보상
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_clear_reward_popup_title].content
   (powtórzenie elementu 193 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Tryby lochów i Kolei Refrakcji [railway_clear_reward_popup_item_column_desc] — tekst] 보상
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_clear_reward_popup_item_column_desc].content
   limit: do 120 znaków
   EN: Rewards
   PL: Nagrody
561. [Tryby lochów i Kolei Refrakcji [railway_node_clear_info_ui_buff_list] — tekst] 버프 선택 목록
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_node_clear_info_ui_buff_list].content
   limit: do 120 znaków
   EN: Selected Buffs
   PL: Wybrane wzmocnienia
562. [Tryby lochów i Kolei Refrakcji [railway_1002_no_buff_in_list] — tekst] 현재 선택된 버프가 없습니다.
   źródło: RailwayDungeonUI_1002.json :: dataList[id=railway_1002_no_buff_in_list].content
   limit: do 120 znaków
   EN: No selected Buffs.
   PL: Brak wybranych wzmocnień.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_2
- plik gry: `RailwayDungeonUI_2.json`

563. [Tryby lochów i Kolei Refrakcji [railway_dungeon_alarm_buff_no_one_select_for_heal] — tekst] 회복 가능 인격 없음
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_alarm_buff_no_one_select_for_heal].content
   limit: do 120 znaków
   EN: No Recoverable ID
   PL: Brak Tożsamości do uleczenia
564. [Tryby lochów i Kolei Refrakcji [railway_dungeon_alarm_buff_no_one_select_for_resurrect] — tekst] 부활 가능 인격 없음
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_alarm_buff_no_one_select_for_resurrect].content
   limit: do 120 znaków
   EN: No Revivable ID
   PL: Brak Tożsamości do wskrzeszenia
565. [Tryby lochów i Kolei Refrakcji [railway_dungeon_healable] — tekst] 회복 가능
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_healable].content
   limit: do 120 znaków
   EN: Recoverable
   PL: Można uleczyć
566. [Tryby lochów i Kolei Refrakcji [railway_dungeon_resurrectable] — tekst] 부활 가능
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_resurrectable].content
   limit: do 120 znaków
   EN: Revivable
   PL: Można wskrzesić
567. [Tryby lochów i Kolei Refrakcji [railway_dungeon_ask_to_select_buff_and_rotate] — tekst] 노선을 타고 <color=#0f7137>시착역</color>으로 이동하시겠습니까?\n\n<size=90%>이동 시 순환 횟수가 증가하며, \n적용할 <color=#0f7137>아군 버프</color> · <color=#990000>적 버프</color>를 각각 선택합니다.</size>
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_ask_to_select_buff_and_rotate].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#0f7137>, </color>, <size=90%>, <color=#990000>, </size>, \n
   EN: Return to the <color=#0f7137>First Stop</color>?\n<size=90%>Doing so increases your Cycle Count, \nand you can select 1 <color=#0f7137>Ally Buff</color> & 1 <color=#990000>Enemy Buff</color>.</size>
   PL: Przejść trasą na <color=#0f7137>Stację początkową</color>?\n\n<size=90%>Zwiększy to liczbę cykli i pozwoli wybrać\npo jednym <color=#0f7137>wzmocnieniu sojuszników</color> oraz <color=#990000>wzmocnieniu wrogów</color>.</size>
568. [Tryby lochów i Kolei Refrakcji [railway_dungeon_current_rotation_count_title] — tekst] 현재 순환 횟수 :
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_current_rotation_count_title].content
   limit: do 120 znaków
   EN: Cycle Count :
   PL: Bieżąca liczba cykli:
569. [Tryby lochów i Kolei Refrakcji [railway_dungeon_rotation_count] — tekst] 순환 횟수
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_rotation_count].content
   (powtórzenie elementu 550 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Tryby lochów i Kolei Refrakcji [railway_dungeon_cumulative_turn_count] — tekst] 누적 턴 수
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_cumulative_turn_count].content
   limit: do 120 znaków
   EN: Total Turns
   PL: Łączna liczba tur
571. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_1] — tekst] 순환 횟수 {1} 이상으로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}
   EN: Obtained by clearing Line 2 with {1} or more Cycle Counts
   PL: Zdobywane za ukończenie Linii 2 przy min. {1} cyklach
572. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_2] — tekst] 순환 횟수 {1} 이상으로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_2].content
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_3] — tekst] 순환 횟수 {1} 이상, 누적 턴 수 {0}턴 이하로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}
   EN: Obtained by clearing Line 2 with {1} or more Cycle Counts and under {0} Total Turns
   PL: Zdobywane za ukończenie Linii 2 przy min. {1} cyklach i w maks. {0} łącznych turach
574. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_4] — tekst] <color=#d6e7f2>시즌 2 레미니센스</color> 기간 내에 순환 횟수 {1} 이상으로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d6e7f2>, </color>, {1}
   EN: Obtained by clearing Line 2 with {1} or more Cycle Counts before <color=#d6e7f2>Season 2: Reminiscence</color> ends
   PL: Zdobywane za ukończenie Linii 2 przy min. {1} cyklach przed końcem <color=#d6e7f2>Sezonu 2: Reminiscencja</color>
575. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_5] — tekst] <color=#d6e7f2>시즌 2 레미니센스</color> 기간 내에 순환 횟수 {1} 이상으로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_5].content
   (powtórzenie elementu 574 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_6] — tekst] <color=#d6e7f2>시즌 2 레미니센스</color> 기간 내에 순환 횟수 {1} 이상, 누적 턴 수 {0}턴 이하로 2호선 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_6].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#d6e7f2>, </color>, {1}, {0}
   EN: Obtained by clearing Line 2 with {1} or more Cycle Counts and {0} or less Total Turns before <color=#d6e7f2>Season 2: Reminiscence</color> ends
   PL: Zdobywane za ukończenie Linii 2 przy min. {1} cyklach i w maks. {0} łącznych turach przed końcem <color=#d6e7f2>Sezonu 2: Reminiscencja</color>
577. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_list] — tekst] 버프 목록
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_list].content
   limit: do 120 znaków
   EN: Buffs List
   PL: Lista wzmocnień
578. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_dummy_buff_name_1] — tekst] 버프 이름 1 (더미)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_dummy_buff_name_1].content
   limit: do 120 znaków
   EN: Buff Name 1 (Dummy)
   PL: Nazwa wzmocnienia 1 (atrapa)
579. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_dummy_buff_name_2] — tekst] 버프 이름 2 (더미)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_dummy_buff_name_2].content
   limit: do 120 znaków
   EN: Buff Name 2 (Dummy)
   PL: Nazwa wzmocnienia 2 (atrapa)
580. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_dummy_buff_name_3] — tekst] 버프 이름 3 (더미)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_dummy_buff_name_3].content
   limit: do 120 znaków
   EN: Buff Name 3 (Dummy)
   PL: Nazwa wzmocnienia 3 (atrapa)
581. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_dummy_buff_name_4] — tekst] 버프 이름 4 (더미)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_dummy_buff_name_4].content
   limit: do 120 znaków
   EN: Buff Name 4 (Dummy)
   PL: Nazwa wzmocnienia 4 (atrapa)
582. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_dummy_buff_name_5] — tekst] 버프 이름 5 (더미)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_dummy_buff_name_5].content
   limit: do 120 znaków
   EN: Buff Name 5 (Dummy)
   PL: Nazwa wzmocnienia 5 (atrapa)
583. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_no_owned_buff_desc] — tekst] 보유 중인 버프가 없습니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_no_owned_buff_desc].content
   limit: do 120 znaków
   EN: No active Buffs.
   PL: Brak aktywnych wzmocnień.
584. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_effect_title] — tekst] 버프 선택 목록
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_effect_title].content
   limit: do 120 znaków
   EN: Selected Buffs List
   PL: Lista wybranych wzmocnień
585. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_current_buff] — tekst] 버프 현황
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_current_buff].content
   limit: do 120 znaków
   EN: Buff Status
   PL: Stan wzmocnień
586. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_acquire_ally_buff] — tekst] <style="railwayDungeonAlly">아군 버프</style> 1종을 선택합니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_acquire_ally_buff].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="railwayDungeonAlly">, </style>
   EN: Select 1 <style="railwayDungeonAlly">Ally Buff</style>.
   PL: Wybierz 1 <style="railwayDungeonAlly">wzmocnienie sojuszników</style>.
587. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_acquire_enemy_buff] — tekst] <style="railwayDungeonEnemy">적 버프</style> 1종을 선택합니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_acquire_enemy_buff].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="railwayDungeonEnemy">, </style>
   EN: Select 1 <style="railwayDungeonEnemy">Enemy Buff</style>.
   PL: Wybierz 1 <style="railwayDungeonEnemy">wzmocnienie wrogów</style>.
588. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_not_selectable] — tekst] 이번 순환에서 선택 불가
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_not_selectable].content
   limit: do 120 znaków
   EN: Cannot be selected this Cycle.
   PL: Niedostępne w tym cyklu
589. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_buff_fixed_selection] — tekst] 고정 선택
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_buff_fixed_selection].content
   limit: do 120 znaków
   EN: Fixed Choice
   PL: Stały wybór
590. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_select_buff_popup_title] — tekst] 버프 선택
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_select_buff_popup_title].content
   limit: do 120 znaków
   EN: Select Buffs
   PL: Wybór wzmocnień
591. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_select_ally_buff] — tekst] 아군 버프 선택
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_select_ally_buff].content
   limit: do 120 znaków
   EN: Select Ally Buff
   PL: Wybierz wzmocnienie sojuszników
592. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_select_enemy_buff] — tekst] 적 버프 선택
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_select_enemy_buff].content
   limit: do 120 znaków
   EN: Select Enemy Buff
   PL: Wybierz wzmocnienie wrogów
593. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ally_buff] — tekst] 아군 버프
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ally_buff].content
   limit: do 120 znaków
   EN: Ally Buffs
   PL: Wzmocnienia sojuszników
594. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_enemy_buff] — tekst] 적 버프
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_enemy_buff].content
   limit: do 120 znaków
   EN: Enemy Buffs
   PL: Wzmocnienia wrogów
595. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_select_resurrect] — tekst] 부활 인격 선택
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_select_resurrect].content
   limit: do 120 znaków
   EN: Select Identity to Revive
   PL: Wybierz Tożsamość do wskrzeszenia
596. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_empty_selected_buffs] — tekst] 선택한 버프가 없습니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_empty_selected_buffs].content
   limit: do 120 znaków
   EN: No selected Buffs.
   PL: Brak wybranych wzmocnień.
597. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_all_died] — tekst] 모든 수감자가 사망하여 진행할 수 없습니다.\n현재 스테이지의 입장 직전으로 돌아가시겠습니까?
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_all_died].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All of your Sinners are dead. You can no longer continue the encounter.\nReturn to the state immediately before entering this stage?
   PL: Wszyscy Grzesznicy polegli — nie można kontynuować.\nWrócić do stanu bezpośrednio sprzed wejścia na bieżący etap?
598. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_defeat] — tekst] 현재 스테이지의 입장 직전으로 돌아가시겠습니까?
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_defeat].content
   limit: do 120 znaków
   EN: Return to state immediately before entering this stage?
   PL: Wrócić do stanu bezpośrednio sprzed wejścia na bieżący etap?
599. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_defeat_info] — tekst] ※ 그렇지 않은 경우에는 적의 HP와 버프 효과가 유지된 상태로 남은 인격들을 사용하여 전투를 진행합니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_defeat_info].content
   limit: do 180 znaków
   EN: ※ Should you choose to continue, you may use the remaining Sinners to continue the battle. Enemy HP and Buff effects will carry over.
   PL: ※ W przeciwnym razie będziesz kontynuować walkę pozostałymi Tożsamościami przy zachowaniu PŻ wrogów i efektów wzmocnień.
600. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_retry_stage] — tekst] 스테이지 재도전
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_retry_stage].content
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_retry_popup_exit] — tekst] 종료하기
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_retry_popup_exit].content
   limit: do 120 znaków
   EN: End Stage
   PL: Zakończ
602. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_retry_popup_continue] — tekst] 컨티뉴
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_retry_popup_continue].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuuj
603. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_retry_popup_retry] — tekst] 다시 도전
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_retry_popup_retry].content
   limit: do 120 znaków
   EN: Try Again
   PL: Ponów próbę
604. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_rotation_count] — tekst] (순환 횟수 {0})
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_rotation_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ({0} Cycle Count)
   PL: (liczba cykli: {0})
605. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_rotation_count_short] — tekst] 순환 : {0}
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_rotation_count_short].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cycle : {0}
   PL: Cykle: {0}
606. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_turn_count_short] — tekst] 턴 : {0}
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_turn_count_short].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turns : {0}
   PL: Tury: {0}
607. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_rotation_node] — tekst] 순환
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_rotation_node].content
   limit: do 120 znaków
   EN: Cycle
   PL: Cykl
608. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_reward_condition_special_ticket] — tekst] ※ <color=#32434f>시즌 2 레미니센스</color> 기간 내에 순환 횟수 <color=#005823>{1}</color> 이상, 누적 턴 수 <color=#005823>{0}</color>턴 이하로 종착역 클리어 시 획득
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_reward_condition_special_ticket].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#32434f>, </color>, <color=#005823>, {1}, {0}, \n
   EN: ※ Obtained by clearing Line 2 with <color=#005823>{1}</color> or more Cycle Counts and<color=#005823>{0}</color> or less Total Turns before \n<color=#32434f>Season 2: Reminiscence</color> ends
   PL: ※ Zdobywane za ukończenie Stacji końcowej przy min. <color=#005823>{1}</color> cyklach i w maks. <color=#005823>{0}</color> łącznych turach\nprzed końcem <color=#32434f>Sezonu 2: Reminiscencja</color>
609. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_special_reward_title] — tekst] 특별 보상
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_special_reward_title].content
   limit: do 120 znaków
   EN: Special Rewards
   PL: Nagrody specjalne
610. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_fixed_enemy_buff] — tekst] 고정 적 버프
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_fixed_enemy_buff].content
   limit: do 120 znaków
   EN: Fixed Enemy Buffs
   PL: Stałe wzmocnienia wrogów
611. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_pass_station] — tekst] 무정차
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_pass_station].content
   limit: do 120 znaków
   EN: Pass Station
   PL: Bez postoju
612. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_next_station] — tekst] 다음 역
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_next_station].content
   limit: do 120 znaków
   EN: Next Station
   PL: Następna stacja
613. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_final_station] — tekst] 종착역
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_final_station].content
   limit: do 120 znaków
   EN: The Terminus
   PL: Stacja końcowa
614. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_banner_reward_condition_7] — tekst] <color=#d6e7f2>시즌 2 레미니센스</color> 기간 내에 순환 횟수 {1} 이상, 누적 턴 수 {0}턴 이하로 2호선 클리어 시 획득\n(단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_banner_reward_condition_7].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#d6e7f2>, </color>, {1}, {0}, \n
   EN: Obtained by clearing Line 2 with {1} or more Cycle Counts and {0} or less Total Turns before\n<color=#d6e7f2>Season 2: Reminiscence</color> ends (Must be a record from a run started after 2023.09.15 20:15(KST))
   PL: Zdobywane za ukończenie Linii 2 przy min. {1} cyklach i w maks. {0} łącznych turach przed końcem <color=#d6e7f2>Sezonu 2: Reminiscencja</color>\n(dotyczy przejazdów rozpoczętych po 15.09.2023 20:15 KST)
615. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_reward_condition_special_ticket_14] — tekst] ※ <color=#32434f>시즌 2 레미니센스</color> 기간 내에 순환 횟수 <color=#005823>{1}</color> 이상, 누적 턴 수 <color=#005823>{0}</color>턴 이하로 종착역 클리어 시 획득\n(단, 23/09/15 20:15 (KST) 이후에 새롭게 시작한 기록을 기준으로 함)
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_reward_condition_special_ticket_14].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#32434f>, </color>, <color=#005823>, {1}, {0}, \n
   EN: Obtained by clearing Line 2 with <color=#005823>{1}</color> or more Cycle Counts and <color=#005823>{0}</color> or less Total Turns\nbefore <color=#32434f>Season 2: Reminiscence</color> ends\n(Must be a record from a run started after 2023.09.15 20:15(KST))
   PL: ※ Zdobywane za ukończenie Stacji końcowej przy min. <color=#005823>{1}</color> cyklach i w maks. <color=#005823>{0}</color> łącznych turach przed końcem <color=#32434f>Sezonu 2: Reminiscencja</color>\n(dotyczy przejazdów rozpoczętych po 15.09.2023 20:15 KST)
616. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_current_battle_turn_count] — tekst] 현재 스테이지 턴 수 : <style="number_highlight"><size="60%">{0}</size></style>
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_current_battle_turn_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <style="number_highlight">, <size="60%">, </size>, </style>, {0}
   EN: Turns taken this Station : <style="number_highlight"><size="60%">{0}</size></style>
   PL: Tury na bieżącym etapie: <style="number_highlight"><size="60%">{0}</size></style>
617. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_defeat_info_turn_count] — tekst] ※ 스테이지 클리어 시, <style="yellow">현재 스테이지 턴 수</style>가 <style="yellow">누적 턴 수</style>에 포함됩니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_defeat_info_turn_count].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <style="yellow">, </style>
   EN: ※ Upon completing the Station, <style="yellow">Turns taken in the current Station</style> will be added to the <style="yellow">Total Turns</style>.
   PL: ※ Po ukończeniu etapu <style="yellow">tury z bieżącego etapu</style> zostaną doliczone do <style="yellow">łącznej liczby tur</style>.
618. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_defeat_info_save_battle] — tekst] 이어하는 경우에는 적의 HP와 버프 효과가 유지된 상태로 남은 인격들을 사용하여 전투를 진행합니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_defeat_info_save_battle].content
   limit: do 170 znaków
   EN: Should you choose to continue, you may use the remaining Sinners to continue the battle. Enemy HP and Buff effects will carry over.
   PL: W przypadku kontynuacji dalszą walkę stoczysz pozostałymi Tożsamościami przy zachowaniu PŻ wrogów i efektów wzmocnień.
619. [Tryby lochów i Kolei Refrakcji [railway_dungeon_2_ask_retry_when_all_died_turn_count] — tekst] ※ 스테이지를 클리어한 경우에만 <style="yellow">현재 스테이지 턴 수</style>가 <style="yellow">누적 턴 수</style>에 포함됩니다.
   źródło: RailwayDungeonUI_2.json :: dataList[id=railway_dungeon_2_ask_retry_when_all_died_turn_count].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <style="yellow">, </style>
   EN: ※ <style="yellow">Turns taken in the current Station</style> will be added to the <style="yellow">Total Turns</style> only after completing the Station.
   PL: ※ <style="yellow">Tury z bieżącego etapu</style> są doliczane do <style="yellow">łącznej liczby tur</style> wyłącznie po ukończeniu etapu.

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_3
- plik gry: `RailwayDungeonUI_3.json`

620. [Tryby lochów i Kolei Refrakcji [railway_dungeon_save_formation] — tekst] 편성 저장
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_save_formation].content
   limit: do 120 znaków
   EN: Save Team
   PL: Zapisz skład
621. [Tryby lochów i Kolei Refrakcji [railway_dungeon_init_saved_stage_data] — tekst] 초기화
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_init_saved_stage_data].content
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Tryby lochów i Kolei Refrakcji [railway_dungeon_init_saved_stage_data_desc] — tekst] 전투 중인 역의 진행 상황을 초기화하고\n입장 직전으로 되돌아가시겠습니까?
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_init_saved_stage_data_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reset the current Station progress\nand return to the state immediately before entry?
   PL: Zresetować postęp na bieżącej stacji\ni wrócić do stanu sprzed wejścia?
623. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_reward_condition_special_ticket] — tekst] ※ <color=#003c3e>시즌 3 본 보야지</color> 기간 내에 누적 턴 수 <color=#cd5e00>{0}</color>턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_reward_condition_special_ticket].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#003c3e>, </color>, <color=#cd5e00>, {0}, \n
   EN: ※ Obtained by clearing the Terminus of Line 3 with <color=#cd5e00>{0}</color> Turns or less Total Turns before\n<color=#003c3e>Season 3: Bon Voyage</color> ends
   PL: ※ Zdobywane za ukończenie Stacji końcowej Kolei Załamania — Linii 3 w maks. <color=#cd5e00>{0}</color> łącznych turach\nprzed końcem <color=#003c3e>Sezonu 3: Bon Voyage</color>
624. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_banner_reward_condition_1] — tekst] 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_banner_reward_condition_1].content
   limit: do 120 znaków
   EN: Obtained by clearing the Terminus of Refraction Railway Line 3
   PL: Zdobywane za ukończenie Stacji końcowej Kolei Załamania — Linii 3
625. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_banner_reward_condition_2] — tekst] 시즌 3 본 보야지 기간 내에 누적 턴 수 {0}턴 이하로 거울굴절철도 3호선 종착역 클리어 시 획득
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_banner_reward_condition_2].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtained by clearing the Terminus of Line 3 with {0} Turns or less Total Turns before Season 3: Bon Voyage ends
   PL: Zdobywane za ukończenie Stacji końcowej Kolei Załamania — Linii 3 w maks. {0} łącznych turach przed końcem Sezonu 3: Bon Voyage
626. [Tryby lochów i Kolei Refrakcji [railway_dungeon_before_enter_past_node_change_formation] — tekst] 편성 저장 시, 선택한 휴게역 이후의\n진행 기록이 완전히 초기화됩니다.\n\n편성을 저장하시겠습니까?
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_before_enter_past_node_change_formation].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Saving your Team Loadout will completely reset any progress\nmade after your selected Rest Station.\n\nSave your Team Loadout anyway?
   PL: Zapisanie składu całkowicie zresetuje cały postęp\npo wybranej stacji postojowej.\n\nZapisać skład mimo to?
627. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_retry_popup_init] — tekst] 돌아가기
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_retry_popup_init].content
   limit: do 120 znaków
   EN: Return
   PL: Wróć
628. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_boss_accumulated_turn] — tekst] 최종 누적 턴
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_boss_accumulated_turn].content
   limit: do 120 znaków
   EN: Total Turns
   PL: Końcowa liczba tur
629. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_unit_recovered] — tekst] 체력, 정신력이 회복되었습니다.
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_unit_recovered].content
   limit: do 120 znaków
   EN: HP and SP have been restored.
   PL: Odnowiono PŻ i SP.
630. [Tryby lochów i Kolei Refrakcji [railway_dungeon_3_formation_saved] — tekst] 편성이 저장되었습니다.
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_3_formation_saved].content
   limit: do 120 znaków
   EN: Your Team Loadout has been saved.
   PL: Skład został zapisany.
631. [Tryby lochów i Kolei Refrakcji [railway_dungeon_before_enter_past_node_battle] — tekst] 클리어한 역을 다시 도전할 경우,\n선택한 역 이후의 진행\n기록이 완전히 초기화됩니다.\n\n선택한 역을 다시 도전하시겠습니까?
   źródło: RailwayDungeonUI_3.json :: dataList[id=railway_dungeon_before_enter_past_node_battle].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Retrying an already-cleared Station\nwill completely reset any progress\nyou have made since that Station.\n\nRetry the Station anyway?
   PL: Ponowne wyzwanie ukończonej stacji\ncałkowicie zresetuje cały postęp\nod tej stacji wzwyż.\n\nPonowić wybraną stację?

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_4
- plik gry: `RailwayDungeonUI_4.json`

632. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_reward_condition_special_ticket] — tekst] ※ <color=#4e3076>시즌 4 클리어 올 캐시</color> 기간 내에 누적 턴 수 <color=#066386>{0}</color>턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_reward_condition_special_ticket].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#4e3076>, </color>, <color=#066386>, {0}, \n
   EN: ※ Obtained by clearing Section 4 of Line 4 with <color=#066386>{0}</color> Turns or less Total Turns before\n<color=#4e3076>Season 4: Clear All Cathy</color> ends
   PL: ※ Zdobywane za ukończenie Odcinka 4 Kolei Załamania — Linii 4 w maks. <color=#066386>{0}</color> łącznych turach\nprzed końcem <color=#4e3076>Sezonu 4: Clear All Cathy</color>
633. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_banner_reward_condition_1] — tekst] 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_banner_reward_condition_1].content
   limit: do 120 znaków
   EN: Obtained by clearing Section #4 of Refraction Railway Line 4
   PL: Zdobywane za ukończenie Odcinka 4 Kolei Załamania — Linii 4
634. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_banner_reward_condition_2] — tekst] 시즌 4 클리어 올 캐시 기간 내에 누적 턴 수 {0}턴 이하로 거울굴절철도 4호선 제 4 구간 클리어 시 획득
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_banner_reward_condition_2].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Obtained by clearing Section 4 of Line 4 with {0} Turns or less Total Turns before\nSeason 4: Clear All Cathy ends
   PL: Zdobywane za ukończenie Odcinka 4 Kolei Załamania — Linii 4 w maks. {0} łącznych turach\nprzed końcem Sezonu 4: Clear All Cathy
635. [Tryby lochów i Kolei Refrakcji [formation_waiting_character] — tekst] 대기 인원
   źródło: RailwayDungeonUI_4.json :: dataList[id=formation_waiting_character].content
   limit: do 120 znaków
   EN: Backup
   PL: Rezerwa
636. [Tryby lochów i Kolei Refrakcji [railway_dungeon_entrance_warning] — tekst] <입장 시 권장 사양>\n\n- 인격 : 동기화 4단계, 레벨 45\n- E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_entrance_warning].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <Recommended Level & Tier>\n- Identities : Uptie Tier 4, Level 45\n- E.G.O : Threadspinning Tier 4
   PL: [Zalecane parametry wejścia]\n\n- Tożsamości: Synchronizacja poz. 4, poziom 45\n- E.G.O: Splot Nici poz. 4
637. [Tryby lochów i Kolei Refrakcji [railway_dungeon_formation_must_select_all_alive] — tekst] 편성 순서를 지정하지 않은 수감자가 있습니다.\n\n모든 수감자의 편성 순서를 지정해주세요.
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_formation_must_select_all_alive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There are unselected Sinners.\n\nPlease select and Deploy all 12 Sinners to enter.
   PL: Nie przypisano kolejności wystawienia wszystkim Grzesznikom.\n\nWyznacz kolejność dla wszystkich Grzeszników.
638. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_exit_title] — tekst] 스테이지 입장 화면으로 이동
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_exit_title].content
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_exit_content] — tekst] 스테이지 입장 화면으로 이동합니다.\n편성 순서를 다시 설정할 수 있습니다.
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_exit_content].content
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_retry_title] — tekst] 스테이지 재도전
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_retry_title].content
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_retry_content] — tekst] 스테이지를 재도전하여 첫 번째 웨이브부터 다시 시작합니다.\n편성 창에서 지정한 편성 순서가 유지됩니다.
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_retry_content].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Retry Stage and start over from the first wave of the Stage.\nYour Deployment order will not be changed.
   PL: Ponawia etap od pierwszej fali.\nKolejność wystawienia wybrana w oknie składu zostaje zachowana.
642. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_give_up_title] — tekst] 포기하기 (사용하지 않음 제거 필요)
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_give_up_title].content
   limit: do 120 znaków
   EN: GIVE UP (there's no giving up, delete this option)
   PL: Poddaj się (nieużywane — do usunięcia)
643. [Tryby lochów i Kolei Refrakcji [formation_participate_battle_label] — tekst] 총 전투 인원
   źródło: RailwayDungeonUI_4.json :: dataList[id=formation_participate_battle_label].content
   limit: do 120 znaków
   EN: Total Participants
   PL: Łącznie w walce
644. [Tryby lochów i Kolei Refrakcji [formation_setting_waiting_character] — tekst] 대기 인원 편성
   źródło: RailwayDungeonUI_4.json :: dataList[id=formation_setting_waiting_character].content
   limit: do 120 znaków
   EN: Backup Deployed
   PL: Wystawiono w rezerwie
645. [Tryby lochów i Kolei Refrakcji [heal_character_who_does_not_participate_battle] — tekst] 전투에 참여하지 않은 인격의 체력이 회복되었습니다.
   źródło: RailwayDungeonUI_4.json :: dataList[id=heal_character_who_does_not_participate_battle].content
   limit: do 120 znaków
   EN: Sinners who are not directly participating in battle have been healed.
   PL: Odnowiono PŻ Tożsamości niebiorących udziału w walce.
646. [Tryby lochów i Kolei Refrakcji [railway_dungeon_ask_to_go_past_node] — tekst] 전투 진입 시 해당 역을 포함하여 이후의 진행 기록이 완전히 초기화됩니다.\n\n전투에 입장하시겠습니까?
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_ask_to_go_past_node].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Entering this Stage will completely reset the progress made in this Stage and any subsequent Stages.\n\nEnter the Stage anyway?
   PL: Wejście do walki całkowicie zresetuje postęp na tej stacji oraz wszystkich kolejnych.\n\nRozpocząć walkę?
647. [Tryby lochów i Kolei Refrakcji [formation_baton_continue] — tekst] 연속
   źródło: RailwayDungeonUI_4.json :: dataList[id=formation_baton_continue].content
   limit: do 120 znaków
   EN: Chain
   PL: Seria
648. [Tryby lochów i Kolei Refrakcji [railway_dungeon_lose_battle_all_identity_dead] — tekst] 모든 수감자가 사망했습니다. 이후 진행을 선택해주세요.
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_lose_battle_all_identity_dead].content
   limit: do 120 znaków
   EN: All Sinners have been defeated. Choose what you would like to do next.
   PL: Wszyscy Grzesznicy polegli. Wybierz dalsze działanie.
649. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_unit_inited] — tekst] 체력, 정신력이 초기화되었습니다.
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_unit_inited].content
   limit: do 120 znaków
   EN: HP and SP have been reset.
   PL: Zresetowano PŻ i SP.
650. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_entrance_recommended] — tekst] 입장 권장 사양
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_entrance_recommended].content
   limit: do 120 znaków
   EN: Recommended Levels
   PL: Zalecane parametry
651. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_entrance_recommended_level] — tekst] - 인격 : 동기화 4단계, 레벨 45
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_entrance_recommended_level].content
   limit: do 120 znaków
   EN: - Identities : Uptie Tier 4, Level 45
   PL: - Tożsamości: Synchronizacja poz. 4, poziom 45
652. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_entrance_recommended_gacksung] — tekst] - E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_entrance_recommended_gacksung].content
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_1] — tekst] <font="BebasKai SDF">SECTION 01</font>
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="BebasKai SDF">, </font>
   EN: <font="BebasKai SDF">SECTION 01</font>
   PL: <font="BebasKai SDF">SECTION 01</font>
654. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_2] — tekst] <font="BebasKai SDF">SECTION 02</font>
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="BebasKai SDF">, </font>
   EN: <font="BebasKai SDF">SECTION 02</font>
   PL: <font="BebasKai SDF">SECTION 02</font>
655. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_3] — tekst] <font="BebasKai SDF">SECTION 03</font>
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="BebasKai SDF">, </font>
   EN: <font="BebasKai SDF">SECTION 03</font>
   PL: <font="BebasKai SDF">SECTION 03</font>
656. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_4] — tekst] <font="BebasKai SDF">SECTION 04</font>
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_4].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="BebasKai SDF">, </font>
   EN: <font="BebasKai SDF">SECTION 04</font>
   PL: <font="BebasKai SDF">SECTION 04</font>
657. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_1_lost_and_found] — tekst] 제 1 구간
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_1_lost_and_found].content
   limit: do 120 znaków
   EN: Section 1
   PL: Odcinek 1
658. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_2_lost_and_found] — tekst] 제 2 구간
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_2_lost_and_found].content
   limit: do 120 znaków
   EN: Section 2
   PL: Odcinek 2
659. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_3_lost_and_found] — tekst] 제 3 구간
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_3_lost_and_found].content
   limit: do 120 znaków
   EN: Section 3
   PL: Odcinek 3
660. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_section_4_lost_and_found] — tekst] 제 4 구간
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_section_4_lost_and_found].content
   limit: do 120 znaków
   EN: Section 4
   PL: Odcinek 4
661. [Tryby lochów i Kolei Refrakcji [railway_dungeon_4_formation_reset] — tekst] 선택 초기화
   źródło: RailwayDungeonUI_4.json :: dataList[id=railway_dungeon_4_formation_reset].content
   limit: do 120 znaków
   EN: Clear Selection
   PL: Wyczyść wybór

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_5
- plik gry: `RailwayDungeonUI_5.json`

662. [Tryby lochów i Kolei Refrakcji [railway_5_must_participate_all] — tekst] 편성되지 않은 인격이 존재합니다.\n\n※ 거울굴절철도 5호선에서는 모든 수감자가 편성에 포함되어야 입장할 수 있습니다.
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_must_participate_all].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please Deploy all Sinners.\n\n※ In Refraction Railway Line 5, every Sinner has to be Deployed in order to enter.
   PL: Nie wszyscy Grzesznicy zostali wystawieni.\n\n※ Aby wejść na Linię 5 Kolei Załamania, w składzie muszą znaleźć się wszyscy Grzesznicy.
663. [Tryby lochów i Kolei Refrakcji [mainui_personality_blocked] — tekst] 편성 불가
   źródło: RailwayDungeonUI_5.json :: dataList[id=mainui_personality_blocked].content
   limit: do 120 znaków
   EN: Cannot Deploy
   PL: Niedostępny
664. [Tryby lochów i Kolei Refrakcji [railway5_clear_info] — tekst] 클리어 정보
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway5_clear_info].content
   limit: do 120 znaków
   EN: Clear Info
   PL: Podsumowanie ukończenia
665. [Tryby lochów i Kolei Refrakcji [railway5_clear_info_node_ui] — tekst] 클리어 정보
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway5_clear_info_node_ui].content
   (powtórzenie elementu 664 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
666. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_entrance_recommended_level] — tekst] - 인격 : 동기화 4단계, 레벨 50
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_entrance_recommended_level].content
   limit: do 120 znaków
   EN: - Identities : Uptie Tier 4, Level 50
   PL: - Tożsamości: Synchronizacja poz. 4, poziom 50
667. [Tryby lochów i Kolei Refrakcji [railway5_clear_info_clear_turn_count] — tekst] 클리어 턴 수
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway5_clear_info_clear_turn_count].content
   limit: do 120 znaków
   EN: Clear Turns
   PL: Tury ukończenia
668. [Tryby lochów i Kolei Refrakcji [railway5_clear_info_ego_stock] — tekst] 남은 자원
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway5_clear_info_ego_stock].content
   limit: do 120 znaków
   EN: Remaining Resources
   PL: Pozostałe zasoby
669. [Tryby lochów i Kolei Refrakcji [railway5_clear_info_selected_buffs] — tekst] 선택 버프
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway5_clear_info_selected_buffs].content
   limit: do 120 znaków
   EN: Selected Buff
   PL: Wybrane wzmocnienia
670. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_reward_condition_special_ticket] — tekst] 시즌 5 오블리비언 기간 내에 누적 턴 수 100턴 이하로 5호선 클리어 시 획득할 수 있습니다.
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_reward_condition_special_ticket].content
   limit: do 120 znaków
   EN: Obtained by clearing Line 5 with 100 or fewer Total Turns before Season 5: Oblivion ends.
   PL: Zdobywane za ukończenie Linii 5 w maks. 100 łącznych turach przed końcem Sezonu 5: Oblivion.
671. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_statistics_button] — tekst] 상세 정보
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_statistics_button].content
   (powtórzenie elementu 516 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_required_condition_to_enter_format] — tekst] ※ 안내 사항\n\n{0}에 입장하기 위해서는 수감자 별로 최소 2개의 인격이 필요합니다.
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_required_condition_to_enter_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: ※ Information\n\nEach Sinner needs to have at least 2 Identities in order to enter {0}.
   PL: ※ Informacja\n\nAby wejść na etap {0}, każdy Grzesznik musi posiadać co najmniej 2 Tożsamości.
673. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_reward_condition_special_ticket_warning] — tekst] <color=#990000>※ 시즌 5 오블리비언 기간이 종료된 이후에는 획득할 수 없습니다.</color>
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_reward_condition_special_ticket_warning].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>
   EN: <color=#990000>※ This cannot be obtained after Season 5: Oblivion ends.</color>
   PL: <color=#990000>※ Niemożliwe do zdobycia po zakończeniu Sezonu 5: Oblivion.</color>
674. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_reward_condition_warning] — tekst] ※ 시즌 5 오블리비언 기간이 종료된 이후에 보상 수령 시, 시즌 이월이 적용되어 시즌 관련 재화인 <color=#990000>자아 파편 상자, 자아 파편 선택 상자의 획득 수량이 반감</color>되오니 참고해주시기 바랍니다.\n(이월되지 않은 자아 파편 상자, 자아 파편 선택 상자는 끈 상자로 전환됩니다.)
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_reward_condition_warning].content
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: ※ Please note that any rewards claimed after Season 5: Oblivion ends will be affected by the Seasonal carryover process. Any Seasonal currencies, such as <color=#990000>Egoshard Crates and Nominable Egoshard Crates</color> will be halved.\n(Egoshard Crates—both Random and Nominable—that have not been carried over are converted into Thread Crates.)
   PL: ※ W przypadku odbioru nagród po zakończeniu Sezonu 5: Oblivion zadziała przeniesienie sezonowe — liczba walut sezonowych (<color=#990000>Skrzyń Odłamków E.G.O oraz Imiennych Skrzyń Odłamków E.G.O</color>) zostanie zmniejszona o połowę.\n(Nieprzeniesione Skrzynie Odłamków E.G.O zostaną zamienione na Skrzynie Nici.)
675. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_banner_reward_condition_1] — tekst] 거울굴절철도 5호선 클리어 시 획득
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_banner_reward_condition_1].content
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 5
   PL: Zdobywane za ukończenie Kolei Załamania — Linii 5
676. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_banner_reward_condition_2] — tekst] <color=#9a0634>시즌 5 오블리비언</color> 기간 내에 누적 턴 수 {0}턴 이하로 거울굴절철도 5호선 클리어 시 획득
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_banner_reward_condition_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#9a0634>, </color>, {0}
   EN: Obtained by clearing Line 5 with {0} or fewer Total Turns before <color=#9a0634>Season 5: Oblivion</color> ends.
   PL: Zdobywane za ukończenie Kolei Załamania — Linii 5 w maks. {0} łącznych turach przed końcem <color=#9a0634>Sezonu 5: Oblivion</color>
677. [Tryby lochów i Kolei Refrakcji [railway_5_banned_personality_exist] — tekst] 사용할 수 없는 인격이 편성되어있습니다.\n\n※ 거울굴절철도 6호선 제 3, 4 구간에서는 직전 구간에서 선택한 인격을 사용할 수 없습니다.
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_banned_personality_exist].content
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A locked Identity is among the Deployed Identities.\n\n※ Please note that, in Refraction Railway Line 6, Sections #3 and #4 do not allow the participation of Identities used in the immediately preceding Sections.
   PL: W składzie znajduje się niedostępna Tożsamość.\n\n※ Na Odcinkach 3 i 4 Linii 6 Kolei Załamania nie można używać Tożsamości wybranych na bezpośrednio poprzedzającym odcinku.
678. [Tryby lochów i Kolei Refrakcji [railway_5_ally_buff] — tekst] 버프
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_ally_buff].content
   limit: do 120 znaków
   EN: Buffs
   PL: Wzmocnienia
679. [Tryby lochów i Kolei Refrakcji [railway_5_enemy_buff] — tekst] 고난
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_enemy_buff].content
   limit: do 120 znaków
   EN: Trials
   PL: Próby
680. [Tryby lochów i Kolei Refrakcji [railway_5_section] — tekst] 제 {0} 구간
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_section].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Section #{0}
   PL: Odcinek {0}
681. [Tryby lochów i Kolei Refrakcji [railway_5_warning_enter_node_1] — tekst] 제 1 구간 전투에 참여한 인격은 제 2 구간 전투에 참여할 수 없습니다.\n\n해당 편성으로 제 1 구간 전투를 진행하시겠습니까?
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_warning_enter_node_1].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please note that Identities participating in Section #1 cannot participate in Section #2.\n\nAre you sure you want to use this loadout for Section #1?
   PL: Tożsamości biorące udział w walce na Odcinku 1 nie będą mogły wystąpić na Odcinku 2.\n\nRozpocząć Odcinek 1 w tym składzie?
682. [Tryby lochów i Kolei Refrakcji [railway_5_select_buff_title] — tekst] 버프 선택
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_select_buff_title].content
   (powtórzenie elementu 590 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
683. [Tryby lochów i Kolei Refrakcji [railway_5_stage_level_warning] — tekst] ※ 현재 인격 평균 레벨 : <color=#990000>{0}</color> (권장 레벨: <color=#990000>{1}</color>)
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_5_stage_level_warning].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}, {1}
   EN: ※ Current Avg. ID Level: <color=#990000>{0}</color> (Recommended Level: <color=#990000>{1}</color>)
   PL: ※ Obecny śr. poziom Tożsamości: <color=#990000>{0}</color> (zalecany: <color=#990000>{1}</color>)
684. [Tryby lochów i Kolei Refrakcji [railway_dungeon_5_entrance_recommended_gacksung] — tekst] - E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_5_entrance_recommended_gacksung].content
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_5_openCondition_desc] — tekst] 7장 클리어
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_advice_5_openCondition_desc].content
   limit: do 120 znaków
   EN: Clear Canto VII
   PL: Ukończ Canto VII
686. [Tryby lochów i Kolei Refrakcji [railway_dungeon_advice_5_level_desc] — tekst] - 인격 : 동기화 4단계, 레벨 50\n- E.G.O : 환상 해석 4단계
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_advice_5_level_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Identities : Uptie Tier 4, Level 50\n- E.G.O : Threadspinning Tier 4
   PL: - Tożsamości: Synchronizacja poz. 4, poziom 50\n- E.G.O: Splot Nici poz. 4
687. [Tryby lochów i Kolei Refrakcji [railway_dungeon_end_date_until] — tekst] ~ <font="ExcelsiorSans SDF">{0}</font>
   źródło: RailwayDungeonUI_5.json :: dataList[id=railway_dungeon_end_date_until].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <font="ExcelsiorSans SDF">, </font>, {0}
   EN: ~ <font="ExcelsiorSans SDF">{0}</font>
   PL: ~ <font="ExcelsiorSans SDF">{0}</font>

## Tryby lochów i Kolei Refrakcji: RailwayDungeonUI_6
- plik gry: `RailwayDungeonUI_6.json`

688. [Tryby lochów i Kolei Refrakcji [railway_dungeon_enter_recommend_growth] — tekst] - 인격 : 동기화 {1}단계, 레벨 {0}\n- E.G.O : 환상 해석 {2}단계
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_enter_recommend_growth].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, {2}, \n
   EN: - Identities : Uptie Tier {1}, Level {0}\n- E.G.O : Threadspinning Tier {2}
   PL: - Tożsamości: Synchronizacja poz. {1}, poziom {0}\n- E.G.O: Splot Nici poz. {2}
689. [Tryby lochów i Kolei Refrakcji [railway_dungeon_enter_recommend_growth_level_max] — tekst] - 인격 : 동기화 {1}단계, 레벨 {0} (최대 레벨 제한 : {3})\n- E.G.O : 환상 해석 {2}단계
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_enter_recommend_growth_level_max].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, {3}, {2}, \n
   EN: - Identities : Uptie Tier {1}, Level {0} (maximum Level cap : {3})\n- E.G.O : Threadspinning Tier {2}
   PL: - Tożsamości: Synchronizacja poz. {1}, poziom {0} (limit poziomu: {3})\n- E.G.O: Splot Nici poz. {2}
690. [Tryby lochów i Kolei Refrakcji [railway_dungeon_6_reward_condition_warning] — tekst] ※ 시즌 7 쿠모노 이토 · 아카노 이토 기간이 종료된 이후에 보상 수령 시, 시즌 이월이 적용되어 시즌 관련 재화인 <color=#990000>자아 파편 상자, 자아 파편 선택 상자의 획득 수량이 반감</color>되오니 참고해주시기 바랍니다.\n(이월되지 않은 자아 파편 상자, 자아 파편 선택 상자는 끈 상자로 전환됩니다.)
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_6_reward_condition_warning].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: ※ Please note that any rewards claimed after Season 7: Kumo no Ito · otI on akA ends will be affected by the Seasonal carryover process. Any Seasonal currencies, such as <color=#990000>Egoshard Crates and Nominable Egoshard Crates</color> will be halved.\n(Egoshard Crates—both Random and Nominable—that have not been carried over are converted into Thread Crates.)
   PL: ※ W przypadku odbioru nagród po zakończeniu Sezonu 7: Kumo no Ito · otI on akA zadziała przeniesienie sezonowe — liczba walut sezonowych (<color=#990000>Skrzyń Odłamków E.G.O oraz Imiennych Skrzyń Odłamków E.G.O</color>) zostanie zmniejszona o połowę.\n(Nieprzeniesione Skrzynie Odłamków E.G.O zostaną zamienione na Skrzynie Nici.)
691. [Tryby lochów i Kolei Refrakcji [railway_dungeon_6_reward_condition_special_ticket] — tekst] 시즌 7 쿠모노 이토 · 아카노 이토 기간 내에 누적 턴 수 111턴 이하로 6호선 클리어 시 획득할 수 있습니다.
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_6_reward_condition_special_ticket].content
   limit: do 140 znaków
   EN: Obtained by clearing Line 6 with 111 or fewer Total Turns before Season 7: Kumo no Ito · otI on akA ends.
   PL: Zdobywane za ukończenie Linii 6 w maks. 111 łącznych turach przed końcem Sezonu 7: Kumo no Ito · otI on akA.
692. [Tryby lochów i Kolei Refrakcji [railway_dungeon_6_reward_condition_special_ticket_warning] — tekst] <color=#990000>※ 시즌 7 쿠모노 이토 · 아카노 이토 기간이 종료된 이후에는 획득할 수 없습니다.</color>
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_6_reward_condition_special_ticket_warning].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>
   EN: <color=#990000>※ This cannot be obtained after Season 7: Kumo no Ito · otI on akA ends.</color>
   PL: <color=#990000>※ Niemożliwe do zdobycia po zakończeniu Sezonu 7: Kumo no Ito · otI on akA.</color>
693. [Tryby lochów i Kolei Refrakcji [railway_dungeon_6_banner_reward_condition_1] — tekst] 거울굴절철도 6호선 클리어 시 획득
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_6_banner_reward_condition_1].content
   limit: do 120 znaków
   EN: Obtained by clearing Refraction Railway Line 6
   PL: Zdobywane za ukończenie Kolei Załamania — Linii 6
694. [Tryby lochów i Kolei Refrakcji [railway_dungeon_6_banner_reward_condition_2] — tekst] <color=#990000>시즌 7 쿠모노 이토 · 아카노 이토</color> 기간 내에 누적 턴 수 {0}턴 이하로 거울굴절철도 6호선 클리어 시 획득
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_dungeon_6_banner_reward_condition_2].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}
   EN: Obtained by clearing Line 6 with {0} or fewer Total Turns before <color=#990000>Season 7: Kumo no Ito · otI on akA</color> ends.
   PL: Zdobywane za ukończenie Kolei Załamania — Linii 6 w maks. {0} łącznych turach przed końcem <color=#990000>Sezonu 7: Kumo no Ito · otI on akA</color>
695. [Tryby lochów i Kolei Refrakcji [railway_6_warning_enter_node_1] — tekst] 5구간 진입 시 1구간 클리어 시점의 체력 비율과 정신력이 유지됩니다.\n\n선택한 편성으로 전투에 입장하시겠습니까?
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_warning_enter_node_1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Team's HP percentage and SP at the point of clearing Section 1 will be carried over to Section 5.\n\nWill you enter the battle with the selected Team Loadout?
   PL: Przy wejściu na Odcinek 5 zachowany zostanie procent PŻ oraz SP z chwili ukończenia Odcinka 1.\n\nRozpocząć walkę w wybranym składzie?
696. [Tryby lochów i Kolei Refrakcji [railway_6_must_participate_all] — tekst] 편성되지 않은 인격이 존재합니다.\n\n※ 거울굴절철도 6호선에서는 모든 수감자가 편성에 포함되어야 입장할 수 있습니다.
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_must_participate_all].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please Deploy all Sinners.\n\n※ In Refraction Railway Line 6, every Sinner has to be Deployed in order to enter.
   PL: Nie wszyscy Grzesznicy zostali wystawieni.\n\n※ Aby wejść na Linię 6 Kolei Załamania, w składzie muszą znaleźć się wszyscy Grzesznicy.
697. [Tryby lochów i Kolei Refrakcji [railway_6_past] — tekst] 과거
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_past].content
   limit: do 120 znaków
   EN: The Past
   PL: Przeszłość
698. [Tryby lochów i Kolei Refrakcji [railway_6_present] — tekst] 현재
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_present].content
   limit: do 120 znaków
   EN: The Present
   PL: Teraźniejszość
699. [Tryby lochów i Kolei Refrakcji [railway_6_future] — tekst] 미래
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_future].content
   limit: do 120 znaków
   EN: The Future
   PL: Przyszłość
700. [Tryby lochów i Kolei Refrakcji [railway_6_check_first_stage_unit_hp_mp] — tekst] 수감자 상태 현황
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_check_first_stage_unit_hp_mp].content
   limit: do 120 znaków
   EN: Sinner Status
   PL: Stan Grzeszników
701. [Tryby lochów i Kolei Refrakcji [railway_6_ui_battle_effect] — tekst] 적용 효과
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_battle_effect].content
   limit: do 120 znaków
   EN: Active Effects
   PL: Aktywne efekty
702. [Tryby lochów i Kolei Refrakcji [railway_6_ui_empty_battle_effect_desc] — tekst] 적용된 효과가 없습니다.
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_empty_battle_effect_desc].content
   limit: do 120 znaków
   EN: No effects active.
   PL: Brak aktywnych efektów.
703. [Tryby lochów i Kolei Refrakcji [railway_6_ui_passive_effect_title] — tekst] 나생접::나비 패시브
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_passive_effect_title].content
   limit: do 120 znaków
   EN: Butterfly of Entangled Lives::Imago Passive
   PL: Pasywka Motyla Splecionych Żywotów::Imago
704. [Tryby lochów i Kolei Refrakcji [railway_6_ui_empty_passive_effect_desc] — tekst] 제 2 구간 클리어 시, 표시됩니다.
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_empty_passive_effect_desc].content
   limit: do 120 znaków
   EN: Will be displayed upon clearing Section 2.
   PL: Wyświetli się po ukończeniu Odcinka 2.
705. [Tryby lochów i Kolei Refrakcji [railway_6_ui_empty_statistics_desc] — tekst] 해당 구간 전투 클리어 시, 표시됩니다.
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_empty_statistics_desc].content
   limit: do 120 znaków
   EN: Will be displayed upon clearing the relevant Encounter of the Section.
   PL: Wyświetli się po ukończeniu walki na danym odcinku.
706. [Tryby lochów i Kolei Refrakcji [railway_6_ui_attack_resistance_buff_for_ui] — tekst] {0} 내성 + 0.25, {1} 내성 + 0.25
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_attack_resistance_buff_for_ui].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Resistance + 0.25, {1} Resistance + 0.25
   PL: Odporność na {0} +0,25, Odporność na {1} +0,25
707. [Tryby lochów i Kolei Refrakcji [railway_6_ui_attack_resistance_buff_for_ui_only_one] — tekst] {0} 내성 + 0.25
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui_attack_resistance_buff_for_ui_only_one].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Resistance + 0.25
   PL: Odporność na {0} +0,25
708. [Tryby lochów i Kolei Refrakcji [railway_6_ui__attack_resistance_buff_for_ui_empty] — tekst] 적용 효과 없음
   źródło: RailwayDungeonUI_6.json :: dataList[id=railway_6_ui__attack_resistance_buff_for_ui_empty].content
   limit: do 120 znaków
   EN: No effect applied
   PL: Brak aktywnego efektu

## Tryby lochów i Kolei Refrakcji: RewardDungeonUI
- plik gry: `RewardDungeonUI.json`

709. [Tryby lochów i Kolei Refrakcji [enter_exp_dungeon] — tekst] 경험치 채광
   źródło: RewardDungeonUI.json :: dataList[id=enter_exp_dungeon].content
   limit: do 120 znaków
   EN: EXP Luxcavation
   PL: Lochy Wydobywcze PD
710. [Tryby lochów i Kolei Refrakcji [enter_mirror_dungeon] — tekst] 거울 던전
   źródło: RewardDungeonUI.json :: dataList[id=enter_mirror_dungeon].content
   limit: do 120 znaków
   EN: Mirror Dungeons
   PL: Lustrzane Lochy
711. [Tryby lochów i Kolei Refrakcji [enter_thread_dungeon] — tekst] 끈 채광
   źródło: RewardDungeonUI.json :: dataList[id=enter_thread_dungeon].content
   limit: do 120 znaków
   EN: Thread Luxcavation
   PL: Lochy Wydobywcze Nici
712. [Tryby lochów i Kolei Refrakcji [enter_count] — tekst] 입장 횟수
   źródło: RewardDungeonUI.json :: dataList[id=enter_count].content
   limit: do 120 znaków
   EN: Entries
   PL: Wejścia
713. [Tryby lochów i Kolei Refrakcji [remain_time] — tekst] 남은 시간
   źródło: RewardDungeonUI.json :: dataList[id=remain_time].content
   limit: do 120 znaków
   EN: Time Left
   PL: Pozostały czas
714. [Tryby lochów i Kolei Refrakcji [open_at_day_of_the_week] — tekst] {0} 오픈
   źródło: RewardDungeonUI.json :: dataList[id=open_at_day_of_the_week].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Opens {0}
   PL: Otwarte w: {0}
715. [Tryby lochów i Kolei Refrakcji [recommended_level] — tekst] 권장 레벨
   źródło: RewardDungeonUI.json :: dataList[id=recommended_level].content
   limit: do 120 znaków
   EN: Difficulty
   PL: Zalecany poz.
716. [Tryby lochów i Kolei Refrakcji [equal_or_more] — tekst] 이상
   źródło: RewardDungeonUI.json :: dataList[id=equal_or_more].content
   limit: do 120 znaków
   EN: or above
   PL: lub wyższy
717. [Tryby lochów i Kolei Refrakcji [valid_attack_type] — tekst] 유효 속성
   źródło: RewardDungeonUI.json :: dataList[id=valid_attack_type].content
   limit: do 120 znaków
   EN: Useful Types
   PL: Skuteczne typy
718. [Tryby lochów i Kolei Refrakcji [exp_dungeon_index] — tekst] 경험치 채광-{0}
   źródło: RewardDungeonUI.json :: dataList[id=exp_dungeon_index].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: EXP Luxcavation #{0}
   PL: Wydobycie PD #{0}
719. [Tryby lochów i Kolei Refrakcji [Monday] — tekst] 월요일
   źródło: RewardDungeonUI.json :: dataList[id=Monday].content
   limit: do 120 znaków
   EN: MON
   PL: Poniedziałek
720. [Tryby lochów i Kolei Refrakcji [Tuesday] — tekst] 화요일
   źródło: RewardDungeonUI.json :: dataList[id=Tuesday].content
   limit: do 120 znaków
   EN: TUE
   PL: Wtorek
721. [Tryby lochów i Kolei Refrakcji [Wednesday] — tekst] 수요일
   źródło: RewardDungeonUI.json :: dataList[id=Wednesday].content
   limit: do 120 znaków
   EN: WED
   PL: Środa
722. [Tryby lochów i Kolei Refrakcji [Thursday] — tekst] 목요일
   źródło: RewardDungeonUI.json :: dataList[id=Thursday].content
   limit: do 120 znaków
   EN: THU
   PL: Czwartek
723. [Tryby lochów i Kolei Refrakcji [Friday] — tekst] 금요일
   źródło: RewardDungeonUI.json :: dataList[id=Friday].content
   limit: do 120 znaków
   EN: FRI
   PL: Piątek
724. [Tryby lochów i Kolei Refrakcji [Saturday] — tekst] 토요일
   źródło: RewardDungeonUI.json :: dataList[id=Saturday].content
   limit: do 120 znaków
   EN: SAT
   PL: Sobota
725. [Tryby lochów i Kolei Refrakcji [Sunday] — tekst] 일요일
   źródło: RewardDungeonUI.json :: dataList[id=Sunday].content
   limit: do 120 znaków
   EN: SUN
   PL: Niedziela
726. [Tryby lochów i Kolei Refrakcji [select_level] — tekst] 레벨 선택
   źródło: RewardDungeonUI.json :: dataList[id=select_level].content
   limit: do 120 znaków
   EN: Level Select
   PL: Wybór poziomu
727. [Tryby lochów i Kolei Refrakcji [require_clear_story_stage] — tekst] 주요 이야기 {0}-{1} 클리어
   źródło: RewardDungeonUI.json :: dataList[id=require_clear_story_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Clear Main Story {0}-{1}
   PL: Ukończ główną fabułę {0}-{1}
728. [Tryby lochów i Kolei Refrakcji [daily_bonus_count] — tekst] 일일 추가 보상
   źródło: RewardDungeonUI.json :: dataList[id=daily_bonus_count].content
   limit: do 120 znaków
   EN: Daily Bonuses
   PL: Premia dzienna
729. [Tryby lochów i Kolei Refrakcji [reward_dungeon_exp] — tekst] 경험치
   źródło: RewardDungeonUI.json :: dataList[id=reward_dungeon_exp].content
   limit: do 120 znaków
   EN: EXP
   PL: PD
730. [Tryby lochów i Kolei Refrakcji [reward_dungeon_thread] — tekst] 끈
   źródło: RewardDungeonUI.json :: dataList[id=reward_dungeon_thread].content
   limit: do 120 znaków
   EN: Thread
   PL: Nić
731. [Tryby lochów i Kolei Refrakcji [reward_dungeon_mining] — tekst] 채광
   źródło: RewardDungeonUI.json :: dataList[id=reward_dungeon_mining].content
   limit: do 120 znaków
   EN: Luxcavation
   PL: Wydobycie
732. [Tryby lochów i Kolei Refrakcji [thread_dungeon_stage_name_with_attribute] — tekst] 끈 채광({0})
   źródło: RewardDungeonUI.json :: dataList[id=thread_dungeon_stage_name_with_attribute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Thread Luxcavation ({0})
   PL: Wydobycie Nici ({0})

## Tryby lochów i Kolei Refrakcji: StoryDungeonUI-a1c8p2
- plik gry: `StoryDungeonUI-a1c8p2.json`

733. [Tryby lochów i Kolei Refrakcji [storyDungeon_108_coinCount] — tekst] 동전
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=storyDungeon_108_coinCount].content
   limit: do 120 znaków
   EN: Coins
   PL: Monety
734. [Tryby lochów i Kolei Refrakcji [gabook] — tekst] 가보옥
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=gabook].content
   limit: do 120 znaków
   EN: Jia Baoyu
   PL: Jia Baoyu
735. [Tryby lochów i Kolei Refrakcji [gachiu] — tekst] 가치우
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=gachiu].content
   limit: do 120 znaków
   EN: Jia Qiu
   PL: Jia Qiu
736. [Tryby lochów i Kolei Refrakcji [gahwan] — tekst] 가환
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=gahwan].content
   limit: do 120 znaków
   EN: Jia Huan
   PL: Jia Huan
737. [Tryby lochów i Kolei Refrakcji [ego_gift_list_8] — tekst] 보유 기물
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=ego_gift_list_8].content
   limit: do 120 znaków
   EN: Artifacts Found
   PL: Posiadane Artefakty
738. [Tryby lochów i Kolei Refrakcji [get_ego_gift_desc_8] — tekst] 기물을 획득했습니다.
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=get_ego_gift_desc_8].content
   limit: do 120 znaków
   EN: Artifact Obtained
   PL: Zdobyto Artefakt.
739. [Tryby lochów i Kolei Refrakcji [subtractor_ego_gift_title] — tekst] E.G.O 기프트 상실
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=subtractor_ego_gift_title].content
   limit: do 120 znaków
   EN: E.G.O Gift Lost
   PL: Utrata Daru E.G.O
740. [Tryby lochów i Kolei Refrakcji [subtractor_ego_gift_title_8] — tekst] 기물 상실
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=subtractor_ego_gift_title_8].content
   limit: do 120 znaków
   EN: Artifact Lost
   PL: Utrata Artefaktu
741. [Tryby lochów i Kolei Refrakcji [subtractor_ego_gift_desc] — tekst] {0}를 {1}개 잃었습니다.
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=subtractor_ego_gift_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Lost {1} {0}(s).
   PL: Utracono {0} ×{1}.
742. [Tryby lochów i Kolei Refrakcji [story_dungeon_cannot_move_to_target_node_side_popup_content] — tekst] 해당 칸으로 이동할 수 없습니다
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=story_dungeon_cannot_move_to_target_node_side_popup_content].content
   limit: do 120 znaków
   EN: Cannot move to this node.
   PL: Nie można przejść na ten węzeł.
743. [Tryby lochów i Kolei Refrakcji [rankUITitle] — tekst] 순위
   źródło: StoryDungeonUI-a1c8p2.json :: dataList[id=rankUITitle].content
   limit: do 120 znaków
   EN: Ranking
   PL: Ranking

## Tryby lochów i Kolei Refrakcji: StoryDungeonUI
- plik gry: `StoryDungeonUI.json`

744. [Tryby lochów i Kolei Refrakcji [story_dungeon_return_to_savepoint_title] — tekst] 아군 전멸
   źródło: StoryDungeonUI.json :: dataList[id=story_dungeon_return_to_savepoint_title].content
   limit: do 120 znaków
   EN: Team Annihilated
   PL: Drużyna unicestwiona
745. [Tryby lochów i Kolei Refrakcji [story_dungeon_return_to_savepoint_content] — tekst] 수감자가 모두 <color=#990000>사망</color>하였습니다.\n세이브 포인트로 돌아갑니다.
   źródło: StoryDungeonUI.json :: dataList[id=story_dungeon_return_to_savepoint_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: All Sinners have <color=#990000>perished</color>.\nReturning to the last checkpoint.
   PL: Wszyscy Grzesznicy <color=#990000>polegli</color>.\nPowrót do punktu zapisu.
746. [Tryby lochów i Kolei Refrakcji [story_dungeon_give_up] — tekst] 포기
   źródło: StoryDungeonUI.json :: dataList[id=story_dungeon_give_up].content
   limit: do 120 znaków
   EN: Forfeit
   PL: Porzuć
747. [Tryby lochów i Kolei Refrakcji [story_dungeon_to_main] — tekst] 메인으로
   źródło: StoryDungeonUI.json :: dataList[id=story_dungeon_to_main].content
   limit: do 120 znaków
   EN: Main Menu
   PL: Menu główne
748. [Tryby lochów i Kolei Refrakcji [story_dungeon_continue] — tekst] 계속
   źródło: StoryDungeonUI.json :: dataList[id=story_dungeon_continue].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuuj
749. [Tryby lochów i Kolei Refrakcji [story_ask_move_to_main] — tekst] 탐색 진도를 저장하고\n메인 화면으로 돌아가시겠습니까?
   źródło: StoryDungeonUI.json :: dataList[id=story_ask_move_to_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Save your progress and\nreturn to the Main Menu?
   PL: Zapisać postęp eksploracji\ni wrócić do ekranu głównego?
750. [Tryby lochów i Kolei Refrakcji [story_ask_give_up_dungeon] — tekst] 던전 탐사를 그만두시겠습니까?
   źródło: StoryDungeonUI.json :: dataList[id=story_ask_give_up_dungeon].content
   limit: do 120 znaków
   EN: Quit exploring the dungeon?
   PL: Przerwać eksplorację lochu?
751. [Tryby lochów i Kolei Refrakcji [story_to_be_return_enkephalin_box_warning] — tekst] ※입장할 때 사용한 엔케팔린 모듈은 반환됩니다
   źródło: StoryDungeonUI.json :: dataList[id=story_to_be_return_enkephalin_box_warning].content
   limit: do 120 znaków
   EN: ※ The Enkephalin Module spent for entry will be returned.
   PL: ※ Zużyte przy wejściu Moduły Enkefaliny zostaną zwrócone.
752. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_start] — tekst] 시작점
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_start].content
   limit: do 120 znaków
   EN: Start
   PL: Punkt startowy
753. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_battle] — tekst] 일반 전투
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_battle].content
   limit: do 120 znaków
   EN: Regular Encounter
   PL: Zwykłe starcie
754. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_ab_battle] — tekst] 집중 전투
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_ab_battle].content
   limit: do 120 znaków
   EN: Focused Encounter
   PL: Starcie skupione
755. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_hard_battle] — tekst] 위험 전투
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_hard_battle].content
   limit: do 120 znaków
   EN: Risky Encounter
   PL: Starcie ryzykowne
756. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_event] — tekst] 이벤트
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_event].content
   limit: do 120 znaków
   EN: Event
   PL: Wydarzenie
757. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_save] — tekst] 저장
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_save].content
   limit: do 120 znaków
   EN: Checkpoint
   PL: Punkt zapisu
758. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_boss] — tekst] 보스 전투
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_boss].content
   limit: do 120 znaków
   EN: Boss Encounter
   PL: Walka z bossem
759. [Tryby lochów i Kolei Refrakcji [dungeon_enter_save_point] — tekst] 세이브 포인트 도달
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_enter_save_point].content
   limit: do 120 znaków
   EN: Checkpoint Reached
   PL: Dotarto do punktu zapisu
760. [Tryby lochów i Kolei Refrakcji [dungeon_recover_hp_mp] — tekst] 체력, 정신력이 회복되었습니다.
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_recover_hp_mp].content
   (powtórzenie elementu 629 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Tryby lochów i Kolei Refrakcji [dungeon_save_completion] — tekst] 저장 완료
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_save_completion].content
   limit: do 120 znaków
   EN: Progress Saved
   PL: Zapisano
762. [Tryby lochów i Kolei Refrakcji [dungeon_save_completion_content] — tekst] 진행 사항이 저장되었습니다.
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_save_completion_content].content
   limit: do 120 znaków
   EN: Your progress has been saved.
   PL: Postęp został zapisany.
763. [Tryby lochów i Kolei Refrakcji [dungeon_return_to_save_point] — tekst] 세이브\n포인트로
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_return_to_save_point].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To Checkpoint
   PL: Do punktu\nzapisu
764. [Tryby lochów i Kolei Refrakcji [dungeon_unlocked_node_notice] — tekst] 새로운 장소가 추가되었습니다.
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_unlocked_node_notice].content
   limit: do 120 znaków
   EN: A new location has been discovered.
   PL: Odkryto nowe miejsce.
765. [Tryby lochów i Kolei Refrakcji [dungeon_unlocked_line_notice] — tekst] 새로운 길이 열렸습니다.
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_unlocked_line_notice].content
   limit: do 120 znaków
   EN: A new path has opened.
   PL: Otworzyła się nowa ścieżka.
766. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_stairs] — tekst] 다음 구역 이동
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_stairs].content
   limit: do 120 znaków
   EN: Move to Next Zone
   PL: Przejdź do kolejnej strefy
767. [Tryby lochów i Kolei Refrakcji [dungeon_encounter_guide_story] — tekst] 이야기
   źródło: StoryDungeonUI.json :: dataList[id=dungeon_encounter_guide_story].content
   limit: do 120 znaków
   EN: Story
   PL: Fabuła
768. [Tryby lochów i Kolei Refrakcji [formation_ui_ask_to_use_saved_formation] — tekst] 해당 편성으로 교체할 경우, 사용 중인 편성이 해당 편성으로 교체됩니다.\n편성을 교체하시겠습니까?\n\n<size=80%>※ 교체가 진행된 이후에는 사용 중인 편성으로 다시 되돌릴 수 없습니다.\n※ 스토리 던전 진행 중 변경된 편성은 수감자 창의 편성에 영향을 주지 않습니다.</size>
   źródło: StoryDungeonUI.json :: dataList[id=formation_ui_ask_to_use_saved_formation].content
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: <size=80%>, </size>, \n
   EN: Your current Team Loadout will be replaced with this new Loadout.\nWill you replace your current Team Loadout with this Loadout?\n\n<size=80%>※ Once your Team Loadout has been replaced, you cannot revert back to your previous Loadout.\n※ Loadout changes made in the middle of Story Dungeons have no effect in the Loadouts in the Sinners Window.</size>
   PL: Obecnie używany skład zostanie zastąpiony wybranym składem.\nZamienić skład?\n\n<size=80%>※ Po zamianie nie można przywrócić poprzedniego składu.\n※ Zmiany składu w trakcie Lochu Fabularnego nie wpływają na składy w oknie Grzeszników.</size>
769. [Tryby lochów i Kolei Refrakcji [story_to_be_return_stage_continue_used_warning] — tekst] ※컨티뉴 기능으로 사용된 재화는 탐사 종료 시 반환되지 않습니다.
   źródło: StoryDungeonUI.json :: dataList[id=story_to_be_return_stage_continue_used_warning].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ※ Resources spent via the continue function will not be refunded upon the end of exploration.
   PL: ※ Zasoby wydane na funkcję kontynuacji nie podlegają zwrotowi po zakończeniu eksploracji.

## Tryby lochów i Kolei Refrakcji: ThreadDungeon
- plik gry: `ThreadDungeon.json`

770. [Tryby lochów i Kolei Refrakcji [1] — nazwa] 흑단여왕의 사과
   źródło: ThreadDungeon.json :: dataList[id=1].name
   limit: do 40 znaków
   EN: Ebony Queen's Apple
   PL: Jabłko Hebanowej Królowej
771. [Tryby lochów i Kolei Refrakcji [2] — nazwa] 단수어
   źródło: ThreadDungeon.json :: dataList[id=2].name
   limit: do 40 znaków
   EN: Headless Ichthys
   PL: Bezgłowy Ichtis
772. [Tryby lochów i Kolei Refrakcji [3] — nazwa] 황금빛의 사과
   źródło: ThreadDungeon.json :: dataList[id=3].name
   limit: do 40 znaków
   EN: Golden Apple
   PL: Złociste Jabłko
773. [Tryby lochów i Kolei Refrakcji [4] — nazwa] 골목파수견
   źródło: ThreadDungeon.json :: dataList[id=4].name
   limit: do 40 znaków
   EN: Alleyway Watchdog
   PL: Pies Stróżujący Zaułków
774. [Tryby lochów i Kolei Refrakcji [5] — nazwa] 너 맞아볼래? 매우?
   źródło: ThreadDungeon.json :: dataList[id=5].name
   limit: do 50 znaków
   EN: You Want To Get Beat? Hurtily?
   PL: Chcesz oberwać? Mocno?
775. [Tryby lochów i Kolei Refrakcji [6] — nazwa] 매혹하는 분홍신
   źródło: ThreadDungeon.json :: dataList[id=6].name
   limit: do 40 znaków
   EN: Enchanting Pink Shoes
   PL: Urzekające Różowe Buciki
776. [Tryby lochów i Kolei Refrakcji [7] — nazwa] 종말 달력
   źródło: ThreadDungeon.json :: dataList[id=7].name
   limit: do 40 znaków
   EN: Doomsday Calendar
   PL: Kalendarz Zagłady
777. [Tryby lochów i Kolei Refrakcji [8] — nazwa] 누구도 울지 않도록
   źródło: ThreadDungeon.json :: dataList[id=8].name
   limit: do 40 znaków
   EN: So That No One Will Cry
   PL: By Nikt Nie Płakał
778. [Tryby lochów i Kolei Refrakcji [9] — nazwa] 떠돌이 여우
   źródło: ThreadDungeon.json :: dataList[id=9].name
   limit: do 40 znaków
   EN: Drifting Fox
   PL: Błędny Lis
779. [Tryby lochów i Kolei Refrakcji [10] — nazwa] 신사 요정
   źródło: ThreadDungeon.json :: dataList[id=10].name
   limit: do 40 znaków
   EN: Fairy Gentleman
   PL: Wróżkowy Dżentelmen
780. [Tryby lochów i Kolei Refrakcji [11] — nazwa] 키다리 요정
   źródło: ThreadDungeon.json :: dataList[id=11].name
   limit: do 40 znaków
   EN: Fairy-Long-Legs
   PL: Długonoga Wróżka
781. [Tryby lochów i Kolei Refrakcji [12] — nazwa] 놋쇠 황소 - 눈물 흘리는
   źródło: ThreadDungeon.json :: dataList[id=12].name
   limit: do 40 znaków
   EN: Brazen Bull - Tearful
   PL: Spiżowy Byk — Łzawiący
782. [Tryby lochów i Kolei Refrakcji [13] — nazwa] kqe-1j-23
   źródło: ThreadDungeon.json :: dataList[id=13].name
   limit: do 40 znaków
   EN: kqe-1j-23
   PL: kqe-1j-23
783. [Tryby lochów i Kolei Refrakcji [14] — nazwa] 울음 두꺼비
   źródło: ThreadDungeon.json :: dataList[id=14].name
   limit: do 40 znaków
   EN: Blubbering Toad
   PL: Szlochająca Ropucha
784. [Tryby lochów i Kolei Refrakcji [15] — nazwa] 장미 사냥꾼
   źródło: ThreadDungeon.json :: dataList[id=15].name
   limit: do 40 znaków
   EN: Rose Hunter
   PL: Łowca Róż
785. [Tryby lochów i Kolei Refrakcji [16] — nazwa] 요정초롱
   źródło: ThreadDungeon.json :: dataList[id=16].name
   limit: do 40 znaków
   EN: Faelantern
   PL: Wróżkowa Latarnia
786. [Tryby lochów i Kolei Refrakcji [17] — nazwa] 충격 지네
   źródło: ThreadDungeon.json :: dataList[id=17].name
   limit: do 40 znaków
   EN: Shock Centipede
   PL: Wstrząsowa Stonoga
787. [Tryby lochów i Kolei Refrakcji [18] — nazwa] 길 잃은 승객
   źródło: ThreadDungeon.json :: dataList[id=18].name
   limit: do 40 znaków
   EN: Wayward Passenger
   PL: Zbłąkany Pasażer
788. [Tryby lochów i Kolei Refrakcji [19] — nazwa] 홍염나방
   źródło: ThreadDungeon.json :: dataList[id=19].name
   limit: do 40 znaków
   EN: Ardor Blossom Moth
   PL: Ćma Szkarłatnego Płomienia
789. [Tryby lochów i Kolei Refrakcji [20] — nazwa] 흑단여왕의 사과
   źródło: ThreadDungeon.json :: dataList[id=20].name
   (powtórzenie elementu 770 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Tryby lochów i Kolei Refrakcji [21] — nazwa] 아파하는 테디
   źródło: ThreadDungeon.json :: dataList[id=21].name
   limit: do 40 znaków
   EN: Hurting Teddy Bear
   PL: Cierpiący Miś
