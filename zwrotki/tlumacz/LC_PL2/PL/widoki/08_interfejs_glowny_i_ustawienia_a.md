# Interfejs główny, bitwa, formacja, ustawienia, komunikaty i skróty (część a) — Limbus Company

Przyciski, okna dialogowe, menu ustawień, filtry formacji, komunikaty błędów, regulaminy i FAQ.

Polski tekst wpisujesz w **jednej linii** po `PL:`. Znacznik `\n` oznacza łamanie linii w oknie gry — zachowaj go tam, gdzie napis ma mieć kilka wierszy. Nie zmieniaj linii `źródło:`, `limit:`, `tokeny:` ani `EN:`.

## Interfejs i ustawienia: AssociationName
- plik gry: `AssociationName.json`

1. [Interfejs i ustawienia [associationName_BLADE_LINEAGE] — tekst] 검계
   źródło: AssociationName.json :: dataList[id=associationName_BLADE_LINEAGE].content
   limit: do 120 znaków
   EN: Blade Lineage
   PL:
2. [Interfejs i ustawienia [associationName_BLACK_CLOUD] — tekst] 흑운회
   źródło: AssociationName.json :: dataList[id=associationName_BLACK_CLOUD].content
   limit: do 120 znaków
   EN: Kurokumo Clan
   PL:
3. [Interfejs i ustawienia [associationName_YURODIVY] — tekst] 유로지비
   źródło: AssociationName.json :: dataList[id=associationName_YURODIVY].content
   limit: do 120 znaków
   EN: Yurodiviye
   PL:

## Interfejs i ustawienia: BattleUIText
- plik gry: `BattleUIText.json`

4. [Interfejs i ustawienia [battle_battleunit_guard] — tekst] 방어
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_guard].content
   limit: do 120 znaków
   EN: Guard
   PL:
5. [Interfejs i ustawienia [popup_message_ego_seat_lack] — tekst] 에고를 사용할 수 없는 상태입니다. 자리를 확인해주세요.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_seat_lack].content
   limit: do 120 znaków
   EN: Cannot use this E.G.O. Please check available space.
   PL:
6. [Interfejs i ustawienia [popup_message_ego_resources_lack] — tekst] 에고를 사용할 수 없는 상태입니다. 문양을 확인해주세요.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_resources_lack].content
   limit: do 120 znaków
   EN: Cannot use this E.G.O. Please check your resources.
   PL:
7. [Interfejs i ustawienia [option_title] — tekst] 설정
   źródło: BattleUIText.json :: dataList[id=option_title].content
   limit: do 120 znaków
   EN: Settings
   PL:
8. [Interfejs i ustawienia [option_btn_exit] — tekst] 스테이지 나가기
   źródło: BattleUIText.json :: dataList[id=option_btn_exit].content
   limit: do 120 znaków
   EN: Exit Stage
   PL:
9. [Interfejs i ustawienia [option_btn_statistical] — tekst] 전투 통계
   źródło: BattleUIText.json :: dataList[id=option_btn_statistical].content
   limit: do 120 znaków
   EN: Battle Data
   PL:
10. [Interfejs i ustawienia [creature_destroy_notice] — tekst] 부위파괴
   źródło: BattleUIText.json :: dataList[id=creature_destroy_notice].content
   limit: do 120 znaków
   EN: Part Broken
   PL:
11. [Interfejs i ustawienia [oneside_attack] — tekst] 일방공격
   źródło: BattleUIText.json :: dataList[id=oneside_attack].content
   limit: do 120 znaków
   EN: Unopposed
   PL:
12. [Interfejs i ustawienia [guard] — tekst] 방어
   źródło: BattleUIText.json :: dataList[id=guard].content
   (powtórzenie elementu 4 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
13. [Interfejs i ustawienia [power] — tekst] 위력
   źródło: BattleUIText.json :: dataList[id=power].content
   limit: do 120 znaków
   EN: Potency
   PL:
14. [Interfejs i ustawienia [require] — tekst] 필요
   źródło: BattleUIText.json :: dataList[id=require].content
   limit: do 120 znaków
   EN: Req.
   PL:
15. [Interfejs i ustawienia [battle_log_atk_hp] — tekst] {0}가(이) {1}에게 {2}의 피해!
   źródło: BattleUIText.json :: dataList[id=battle_log_atk_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} deals {2} damage to {1}!
   PL:
16. [Interfejs i ustawienia [battle_log_atk_mp] — tekst] {0}가(이) {1}에게 {2}의 정신력 피해!
   źródło: BattleUIText.json :: dataList[id=battle_log_atk_mp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} deals {2} damage to {1}’s sanity!
   PL:
17. [Interfejs i ustawienia [battle_log_recover_hp] — tekst] {0}가(이) {1}을 사용하여 체력{2} 회복
   źródło: BattleUIText.json :: dataList[id=battle_log_recover_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} healed {2} HP using {1}.
   PL:
18. [Interfejs i ustawienia [battle_log_guard] — tekst] {0} 방어 사용
   źródło: BattleUIText.json :: dataList[id=battle_log_guard].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} raised their guard.
   PL:
19. [Interfejs i ustawienia [battle_log_buf_to_other] — tekst] {0}가(이) {1}에게 {2}를(을) {3} 부여
   źródło: BattleUIText.json :: dataList[id=battle_log_buf_to_other].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: {0} applied {3} {2} to {1}.
   PL:
20. [Interfejs i ustawienia [battle_log_buf_to_self] — tekst] {0}가(이) 자신에게 {1}를(을) {2} 부여
   źródło: BattleUIText.json :: dataList[id=battle_log_buf_to_self].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} applied {2} {1} to themself.
   PL:
21. [Interfejs i ustawienia [battle_log_use_ego] — tekst] {0}의 E.G.O:{1} 각성!!
   źródło: BattleUIText.json :: dataList[id=battle_log_use_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} awakens {1}!!
   PL:
22. [Interfejs i ustawienia [battle_log_use_ego_corrosion] — tekst] {0}의 E.G.O:{1} 침식!!
   źródło: BattleUIText.json :: dataList[id=battle_log_use_ego_corrosion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} corrodes {0}!!
   PL:
23. [Interfejs i ustawienia [battle_log_personality_corrosion] — tekst] {0}의 정신붕괴!!
   źródło: BattleUIText.json :: dataList[id=battle_log_personality_corrosion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} has a breakdown!!
   PL:
24. [Interfejs i ustawienia [battle_log_low_morale] — tekst] {0}의 사기 저하!
   źródło: BattleUIText.json :: dataList[id=battle_log_low_morale].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}’s morale is low!
   PL:
25. [Interfejs i ustawienia [battle_log_panic] — tekst] {0}의 패닉!!
   źródło: BattleUIText.json :: dataList[id=battle_log_panic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is panicking!!
   PL:
26. [Interfejs i ustawienia [choice_result_success] — tekst] 판정 성공
   źródło: BattleUIText.json :: dataList[id=choice_result_success].content
   limit: do 120 znaków
   EN: Check Passed
   PL:
27. [Interfejs i ustawienia [choice_result_fail] — tekst] 판정 실패
   źródło: BattleUIText.json :: dataList[id=choice_result_fail].content
   limit: do 120 znaków
   EN: Check Failed
   PL:
28. [Interfejs i ustawienia [choice_result_skip] — tekst] 판정 넘김
   źródło: BattleUIText.json :: dataList[id=choice_result_skip].content
   limit: do 120 znaków
   EN: Check Skipped
   PL:
29. [Interfejs i ustawienia [info_button_detailinfo] — tekst] 상세 정보
   źródło: BattleUIText.json :: dataList[id=info_button_detailinfo].content
   limit: do 120 znaków
   EN: Details
   PL:
30. [Interfejs i ustawienia [info_button_skill] — tekst] 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_skill].content
   limit: do 120 znaków
   EN: Skill
   PL:
31. [Interfejs i ustawienia [info_button_awakenskill] — tekst] 각성 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_awakenskill].content
   limit: do 120 znaków
   EN: Awakening
   PL:
32. [Interfejs i ustawienia [info_button_erosionskill] — tekst] 침식 스킬
   źródło: BattleUIText.json :: dataList[id=info_button_erosionskill].content
   limit: do 120 znaków
   EN: Corrosion
   PL:
33. [Interfejs i ustawienia [resonance] — tekst] 공명
   źródło: BattleUIText.json :: dataList[id=resonance].content
   limit: do 120 znaków
   EN: Res
   PL:
34. [Interfejs i ustawienia [perfect_resonance] — tekst] 완전공명
   źródło: BattleUIText.json :: dataList[id=perfect_resonance].content
   limit: do 120 znaków
   EN: A-Res
   PL:
35. [Interfejs i ustawienia [break] — tekst] 흐트러짐
   źródło: BattleUIText.json :: dataList[id=break].content
   limit: do 120 znaków
   EN: STAGGER
   PL:
36. [Interfejs i ustawienia [mental_break] — tekst] 정신붕괴
   źródło: BattleUIText.json :: dataList[id=mental_break].content
   limit: do 120 znaków
   EN: BREAKDOWN
   PL:
37. [Interfejs i ustawienia [low_morale] — tekst] 사기저하
   źródło: BattleUIText.json :: dataList[id=low_morale].content
   limit: do 120 znaków
   EN: Low Morale
   PL:
38. [Interfejs i ustawienia [panic] — tekst] 패닉
   źródło: BattleUIText.json :: dataList[id=panic].content
   limit: do 120 znaków
   EN: Panic
   PL:
39. [Interfejs i ustawienia [status] — tekst] 스테이터스
   źródło: BattleUIText.json :: dataList[id=status].content
   limit: do 120 znaków
   EN: Status
   PL:
40. [Interfejs i ustawienia [status_abnormal] — tekst] 상태이상
   źródło: BattleUIText.json :: dataList[id=status_abnormal].content
   limit: do 120 znaków
   EN: Effects
   PL:
41. [Interfejs i ustawienia [immunity_information] — tekst] 내성 정보
   źródło: BattleUIText.json :: dataList[id=immunity_information].content
   limit: do 120 znaków
   EN: Resistances
   PL:
42. [Interfejs i ustawienia [awaken_ego_skill] — tekst] 각성 스킬
   źródło: BattleUIText.json :: dataList[id=awaken_ego_skill].content
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
43. [Interfejs i ustawienia [erosion_ego_skill] — tekst] 침식 스킬
   źródło: BattleUIText.json :: dataList[id=erosion_ego_skill].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
44. [Interfejs i ustawienia [turnplace_test_name] — tekst] 남겨진 로보토미 지부 어딘가
   źródło: BattleUIText.json :: dataList[id=turnplace_test_name].content
   limit: do 120 znaków
   EN: An Abandoned LC Branch
   PL:
45. [Interfejs i ustawienia [death] — tekst] 사망
   źródło: BattleUIText.json :: dataList[id=death].content
   limit: do 120 znaków
   EN: DEAD
   PL:
46. [Interfejs i ustawienia [slash] — tekst] 참격
   źródło: BattleUIText.json :: dataList[id=slash].content
   limit: do 120 znaków
   EN: Slash
   PL:
47. [Interfejs i ustawienia [penetrate] — tekst] 관통
   źródło: BattleUIText.json :: dataList[id=penetrate].content
   limit: do 120 znaków
   EN: Pierce
   PL:
48. [Interfejs i ustawienia [hit] — tekst] 타격
   źródło: BattleUIText.json :: dataList[id=hit].content
   limit: do 120 znaków
   EN: Blunt
   PL:
49. [Interfejs i ustawienia [action_disable] — tekst] 행동불가
   źródło: BattleUIText.json :: dataList[id=action_disable].content
   limit: do 120 znaków
   EN: Immobile
   PL:
50. [Interfejs i ustawienia [ab_event_select_character] — tekst] 수감자 선택
   źródło: BattleUIText.json :: dataList[id=ab_event_select_character].content
   limit: do 120 znaków
   EN: Select Sinner
   PL:
51. [Interfejs i ustawienia [ab_event_select_desc] — tekst] 선택 내용
   źródło: BattleUIText.json :: dataList[id=ab_event_select_desc].content
   limit: do 120 znaków
   EN: Info
   PL:
52. [Interfejs i ustawienia [ab_event_rate] — tekst] 성공 확률
   źródło: BattleUIText.json :: dataList[id=ab_event_rate].content
   limit: do 120 znaków
   EN: Success Rate
   PL:
53. [Interfejs i ustawienia [formet_event_rate] — tekst] 성공 확률 : {0}
   źródło: BattleUIText.json :: dataList[id=formet_event_rate].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Success Rate: {0}
   PL:
54. [Interfejs i ustawienia [ab_event_decision] — tekst] 판정 시작
   źródło: BattleUIText.json :: dataList[id=ab_event_decision].content
   limit: do 120 znaków
   EN: Commence
   PL:
55. [Interfejs i ustawienia [ab_event_need] — tekst] 필요
   źródło: BattleUIText.json :: dataList[id=ab_event_need].content
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Interfejs i ustawienia [ab_battle_resume] — tekst] 전투 재개
   źródło: BattleUIText.json :: dataList[id=ab_battle_resume].content
   limit: do 120 znaków
   EN: Resume Battle
   PL:
57. [Interfejs i ustawienia [info_button_choice_log] — tekst] 선택지 로그
   źródło: BattleUIText.json :: dataList[id=info_button_choice_log].content
   limit: do 120 znaków
   EN: Decision Log
   PL:
58. [Interfejs i ustawienia [info_button_story] — tekst] 스토리
   źródło: BattleUIText.json :: dataList[id=info_button_story].content
   limit: do 120 znaków
   EN: Story
   PL:
59. [Interfejs i ustawienia [info_button_ego] — tekst] E.G.O
   źródło: BattleUIText.json :: dataList[id=info_button_ego].content
   limit: do 120 znaków
   EN: E.G.O
   PL:
60. [Interfejs i ustawienia [dungeon_encounter_start] — tekst] 시작점
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_start].content
   limit: do 120 znaków
   EN: Start
   PL:
61. [Interfejs i ustawienia [dungeon_encounter_battle] — tekst] 일반 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_battle].content
   limit: do 120 znaków
   EN: Regular Encounter
   PL:
62. [Interfejs i ustawienia [dungeon_encounter_ab_battle] — tekst] 집중 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_ab_battle].content
   limit: do 120 znaków
   EN: Focused Encounter
   PL:
63. [Interfejs i ustawienia [dungeon_encounter_hard_battle] — tekst] 위험 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_hard_battle].content
   limit: do 120 znaków
   EN: Risky Encounter
   PL:
64. [Interfejs i ustawienia [dungeon_encounter_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_event].content
   limit: do 120 znaków
   EN: Event
   PL:
65. [Interfejs i ustawienia [dungeon_encounter_save] — tekst] 세이브 포인트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_save].content
   limit: do 120 znaków
   EN: Checkpoint
   PL:
66. [Interfejs i ustawienia [dungeon_encounter_boss] — tekst] 층 보스
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_boss].content
   limit: do 120 znaków
   EN: Floor Boss
   PL:
67. [Interfejs i ustawienia [bottom_winrate] — tekst] 승률
   źródło: BattleUIText.json :: dataList[id=bottom_winrate].content
   limit: do 120 znaków
   EN: Win Rate
   PL:
68. [Interfejs i ustawienia [bottom_dmg] — tekst] 피해량
   źródło: BattleUIText.json :: dataList[id=bottom_dmg].content
   limit: do 120 znaków
   EN: Damage
   PL:
69. [Interfejs i ustawienia [ab_event_next] — tekst] 다음으로
   źródło: BattleUIText.json :: dataList[id=ab_event_next].content
   limit: do 120 znaków
   EN: Proceed
   PL:
70. [Interfejs i ustawienia [explanatory] — tekst] 범례
   źródło: BattleUIText.json :: dataList[id=explanatory].content
   limit: do 120 znaków
   EN: Legend
   PL:
71. [Interfejs i ustawienia [get_ego_gift] — tekst] E.G.O 기프트 획득
   źródło: BattleUIText.json :: dataList[id=get_ego_gift].content
   limit: do 120 znaków
   EN: E.G.O Gift GET
   PL:
72. [Interfejs i ustawienia [get_ego_gift_desc] — tekst] E.G.O 기프트를 획득했습니다.
   źródło: BattleUIText.json :: dataList[id=get_ego_gift_desc].content
   limit: do 120 znaków
   EN: E.G.O Gift GET!
   PL:
73. [Interfejs i ustawienia [selection] — tekst] 선택지
   źródło: BattleUIText.json :: dataList[id=selection].content
   limit: do 120 znaków
   EN: Choices
   PL:
74. [Interfejs i ustawienia [result] — tekst] 결과
   źródło: BattleUIText.json :: dataList[id=result].content
   limit: do 120 znaków
   EN: Result
   PL:
75. [Interfejs i ustawienia [choice_total_rate] — tekst] 총 성공 확률
   źródło: BattleUIText.json :: dataList[id=choice_total_rate].content
   limit: do 120 znaków
   EN: Total Success Rate
   PL:
76. [Interfejs i ustawienia [enter] — tekst] 입장
   źródło: BattleUIText.json :: dataList[id=enter].content
   limit: do 120 znaków
   EN: Enter
   PL:
77. [Interfejs i ustawienia [recommend_level] — tekst] 추천 레벨
   źródło: BattleUIText.json :: dataList[id=recommend_level].content
   limit: do 120 znaków
   EN: Ideal LVL
   PL:
78. [Interfejs i ustawienia [enemy_info] — tekst] 적 정보
   źródło: BattleUIText.json :: dataList[id=enemy_info].content
   limit: do 120 znaków
   EN: Enemy Info
   PL:
79. [Interfejs i ustawienia [enter_clear_requirement] — tekst] EX 클리어 조건
   źródło: BattleUIText.json :: dataList[id=enter_clear_requirement].content
   limit: do 120 znaków
   EN: Extra Objective
   PL:
80. [Interfejs i ustawienia [choice_event_resume] — tekst] 돌아가기
   źródło: BattleUIText.json :: dataList[id=choice_event_resume].content
   limit: do 120 znaków
   EN: Continue
   PL:
81. [Interfejs i ustawienia [crime_state_judgment] — tekst] {0} 판정
   źródło: BattleUIText.json :: dataList[id=crime_state_judgment].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Check
   PL:
82. [Interfejs i ustawienia [choice_personality] — tekst] 판정을 진행할 인격을 선택하세요
   źródło: BattleUIText.json :: dataList[id=choice_personality].content
   limit: do 120 znaków
   EN: Choose a character to perform the check with:
   PL:
83. [Interfejs i ustawienia [success_result] — tekst] 성공 값
   źródło: BattleUIText.json :: dataList[id=success_result].content
   limit: do 120 znaków
   EN: Threshold
   PL:
84. [Interfejs i ustawienia [expectation_result] — tekst] 예상 값
   źródło: BattleUIText.json :: dataList[id=expectation_result].content
   limit: do 120 znaków
   EN: Predicted
   PL:
85. [Interfejs i ustawienia [outcome_result] — tekst] 결과 값
   źródło: BattleUIText.json :: dataList[id=outcome_result].content
   limit: do 120 znaków
   EN: Outcome
   PL:
86. [Interfejs i ustawienia [choice_event_percent] — tekst] 예상 확률
   źródło: BattleUIText.json :: dataList[id=choice_event_percent].content
   limit: do 120 znaków
   EN: Odds
   PL:
87. [Interfejs i ustawienia [skill_expectition_value] — tekst] 스킬 예상 값 {0}-{1}
   źródło: BattleUIText.json :: dataList[id=skill_expectition_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Predicted Range: {0}-{1}
   PL:
88. [Interfejs i ustawienia [skill_expectition_or_value] — tekst] 스킬 예상 값 {0}or{1}
   źródło: BattleUIText.json :: dataList[id=skill_expectition_or_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Predicted Value: {0} / {1}
   PL:
89. [Interfejs i ustawienia [skill_correction_value] — tekst] {0} 보정 값 {1}
   źródło: BattleUIText.json :: dataList[id=skill_correction_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Modifier: {1}
   PL:
90. [Interfejs i ustawienia [correction_based_on_association] — tekst] {0} 소속 보정 값 {1}(, )
   źródło: BattleUIText.json :: dataList[id=correction_based_on_association].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Faction Modifier: {1}(, )
   PL:
91. [Interfejs i ustawienia [action_choice_event_result_example_battle] — tekst] 전투 발생
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_battle].content
   limit: do 120 znaków
   EN: Combat Encounter
   PL:
92. [Interfejs i ustawienia [action_choice_event_result_example_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_event].content
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
93. [Interfejs i ustawienia [action_choice_event_result_example_resume] — tekst] 돌아가기
   źródło: BattleUIText.json :: dataList[id=action_choice_event_result_example_resume].content
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
94. [Interfejs i ustawienia [areaatk_attack] — tekst] 광역 스킬
   źródło: BattleUIText.json :: dataList[id=areaatk_attack].content
   limit: do 120 znaków
   EN: AoE Skills
   PL:
95. [Interfejs i ustawienia [enter_battle] — tekst] 전투 시작
   źródło: BattleUIText.json :: dataList[id=enter_battle].content
   limit: do 120 znaków
   EN: Commence Battle
   PL:
96. [Interfejs i ustawienia [choice_event_five_percent] — tekst] 5% 확률로 성공
   źródło: BattleUIText.json :: dataList[id=choice_event_five_percent].content
   limit: do 120 znaków
   EN: 5% Chance
   PL:
97. [Interfejs i ustawienia [choice_event_five_percent_success] — tekst] 5% 확률로 판정 성공
   źródło: BattleUIText.json :: dataList[id=choice_event_five_percent_success].content
   limit: do 120 znaków
   EN: 5% Chance of Success
   PL:
98. [Interfejs i ustawienia [skillinfo_passivetitle] — tekst] 지속 효과
   źródło: BattleUIText.json :: dataList[id=skillinfo_passivetitle].content
   limit: do 120 znaków
   EN: Passives
   PL:
99. [Interfejs i ustawienia [skillinfo_coinabilitytitle] — tekst] 스킬 효과
   źródło: BattleUIText.json :: dataList[id=skillinfo_coinabilitytitle].content
   limit: do 120 znaków
   EN: Skill Effects
   PL:
100. [Interfejs i ustawienia [dungeon_save_desc] — tekst] 세이브 포인트 도달.\n던전 진행 상황이 저장되었습니다.\n모든 수감자가 회복됩니다.
   źródło: BattleUIText.json :: dataList[id=dungeon_save_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Checkpoint reached.\nDungeon progress has been saved.\nAll Sinners have been healed.
   PL:
101. [Interfejs i ustawienia [battle_battleunit_evade] — tekst] 회피
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_evade].content
   limit: do 120 znaków
   EN: Evade
   PL:
102. [Interfejs i ustawienia [battle_battleunit_counter] — tekst] 반격
   źródło: BattleUIText.json :: dataList[id=battle_battleunit_counter].content
   limit: do 120 znaków
   EN: Counter
   PL:
103. [Interfejs i ustawienia [battle_operation_defence] — tekst] 수비
   źródło: BattleUIText.json :: dataList[id=battle_operation_defence].content
   limit: do 120 znaków
   EN: Defense
   PL:
104. [Interfejs i ustawienia [battle_increase_mp] — tekst] 정신력 증가
   źródło: BattleUIText.json :: dataList[id=battle_increase_mp].content
   limit: do 120 znaków
   EN: Sanity Up
   PL:
105. [Interfejs i ustawienia [battle_decrease_mp] — tekst] 정신력 감소
   źródło: BattleUIText.json :: dataList[id=battle_decrease_mp].content
   limit: do 120 znaków
   EN: Sanity Down
   PL:
106. [Interfejs i ustawienia [dungeon_encounter_type_start] — tekst] 시작
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_start].content
   limit: do 120 znaków
   EN: Start
   PL:
107. [Interfejs i ustawienia [dungeon_encounter_type_battle] — tekst] 일반 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_battle].content
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
108. [Interfejs i ustawienia [dungeon_encounter_type_ab_battle] — tekst] 집중 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_ab_battle].content
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Interfejs i ustawienia [dungeon_encounter_type_hard_battle] — tekst] 위험 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_hard_battle].content
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
110. [Interfejs i ustawienia [dungeon_encounter_type_event] — tekst] 이벤트
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_event].content
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
111. [Interfejs i ustawienia [dungeon_encounter_type_save] — tekst] 세이브룸
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_save].content
   limit: do 120 znaków
   EN: Saferoom
   PL:
112. [Interfejs i ustawienia [dungeon_encounter_type_boss] — tekst] 보스 전투
   źródło: BattleUIText.json :: dataList[id=dungeon_encounter_type_boss].content
   limit: do 120 znaków
   EN: Boss Encounter
   PL:
113. [Interfejs i ustawienia [battle_mp] — tekst] 정신력
   źródło: BattleUIText.json :: dataList[id=battle_mp].content
   limit: do 120 znaków
   EN: Sanity
   PL:
114. [Interfejs i ustawienia [abnormality_part_hp] — tekst] 부위 체력
   źródło: BattleUIText.json :: dataList[id=abnormality_part_hp].content
   limit: do 120 znaków
   EN: Part HP
   PL:
115. [Interfejs i ustawienia [abnormality_research_level] — tekst] 관찰 단계
   źródło: BattleUIText.json :: dataList[id=abnormality_research_level].content
   limit: do 120 znaków
   EN: Obs. Level
   PL:
116. [Interfejs i ustawienia [abnormality_no_research_level] — tekst] 관찰 단계 없음
   źródło: BattleUIText.json :: dataList[id=abnormality_no_research_level].content
   limit: do 120 znaków
   EN: Lacking Data
   PL:
117. [Interfejs i ustawienia [Insufficient_conditions] — tekst] 조건 불충족
   źródło: BattleUIText.json :: dataList[id=Insufficient_conditions].content
   limit: do 120 znaków
   EN: Conditions Unmet
   PL:
118. [Interfejs i ustawienia [skillinfo_keyword] — tekst] 키워드
   źródło: BattleUIText.json :: dataList[id=skillinfo_keyword].content
   limit: do 120 znaków
   EN: Keywords
   PL:
119. [Interfejs i ustawienia [ability_turn] — tekst] 횟수
   źródło: BattleUIText.json :: dataList[id=ability_turn].content
   limit: do 120 znaków
   EN: Count
   PL:
120. [Interfejs i ustawienia [ego_erosion] — tekst] E.G.O 침식
   źródło: BattleUIText.json :: dataList[id=ego_erosion].content
   limit: do 120 znaków
   EN: E.G.O Corrosion
   PL:
121. [Interfejs i ustawienia [continuous_turn] — tekst] 지속 턴
   źródło: BattleUIText.json :: dataList[id=continuous_turn].content
   limit: do 120 znaków
   EN: Turns
   PL:
122. [Interfejs i ustawienia [status_buff_list] — tekst] 효과 목록
   źródło: BattleUIText.json :: dataList[id=status_buff_list].content
   limit: do 120 znaków
   EN: Effects
   PL:
123. [Interfejs i ustawienia [stack] — tekst] 스택
   źródło: BattleUIText.json :: dataList[id=stack].content
   limit: do 120 znaków
   EN: Stack
   PL:
124. [Interfejs i ustawienia [slash_resistance] — tekst] 참격 내성
   źródło: BattleUIText.json :: dataList[id=slash_resistance].content
   limit: do 120 znaków
   EN: Slash Res.
   PL:
125. [Interfejs i ustawienia [penetrate_resistance] — tekst] 관통 내성
   źródło: BattleUIText.json :: dataList[id=penetrate_resistance].content
   limit: do 120 znaków
   EN: Pierce Res.
   PL:
126. [Interfejs i ustawienia [hit_resistance] — tekst] 타격 내성
   źródło: BattleUIText.json :: dataList[id=hit_resistance].content
   limit: do 120 znaków
   EN: Blunt Res.
   PL:
127. [Interfejs i ustawienia [Lack_Buff] — tekst] !{0} 부족!
   źródło: BattleUIText.json :: dataList[id=Lack_Buff].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No {0}!
   PL:
128. [Interfejs i ustawienia [received_the_golden_bough] — tekst] 황금가지 수복
   źródło: BattleUIText.json :: dataList[id=received_the_golden_bough].content
   limit: do 120 znaków
   EN: Golden Bough Recovered
   PL:
129. [Interfejs i ustawienia [destroyable] — tekst] 파괴 가능
   źródło: BattleUIText.json :: dataList[id=destroyable].content
   limit: do 120 znaków
   EN: Destructible
   PL:
130. [Interfejs i ustawienia [resumption] — tekst] 게임 재개
   źródło: BattleUIText.json :: dataList[id=resumption].content
   limit: do 120 znaków
   EN: Resume
   PL:
131. [Interfejs i ustawienia [stage_GiveUp] — tekst] 스테이지 포기
   źródło: BattleUIText.json :: dataList[id=stage_GiveUp].content
   limit: do 120 znaków
   EN: Give Up
   PL:
132. [Interfejs i ustawienia [show_skillTool] — tekst] 스킬 툴 표시
   źródło: BattleUIText.json :: dataList[id=show_skillTool].content
   limit: do 120 znaków
   EN: Show Skill Tools
   PL:
133. [Interfejs i ustawienia [auto_coinToss] — tekst] 코인 토스 자동
   źródło: BattleUIText.json :: dataList[id=auto_coinToss].content
   limit: do 120 znaków
   EN: Auto Cointoss
   PL:
134. [Interfejs i ustawienia [babayaga_alert] — tekst] {0}번의 기회가 남았어.
   źródło: BattleUIText.json :: dataList[id=babayaga_alert].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You have {0} chances left.
   PL:
135. [Interfejs i ustawienia [battle_operation_offset] — tekst] 상쇄
   źródło: BattleUIText.json :: dataList[id=battle_operation_offset].content
   limit: do 120 znaków
   EN: Offset
   PL:
136. [Interfejs i ustawienia [oneside_defense] — tekst] 일방방어
   źródło: BattleUIText.json :: dataList[id=oneside_defense].content
   limit: do 120 znaków
   EN: One-sided Guard
   PL:
137. [Interfejs i ustawienia [cantIdentify] — tekst] <color=#ff0000>[피아식별불가]</color>
   źródło: BattleUIText.json :: dataList[id=cantIdentify].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>[Indiscriminate]</color>
   PL:
138. [Interfejs i ustawienia [popup_message_ego_irrevocable] — tekst] 이전 턴에 생성한 E.G.O 스킬은 취소할 수 없습니다.
   źródło: BattleUIText.json :: dataList[id=popup_message_ego_irrevocable].content
   limit: do 120 znaków
   EN: E.G.O Skills generated on previous turns cannot be canceled.
   PL:
139. [Interfejs i ustawienia [stock] — tekst] 보유
   źródło: BattleUIText.json :: dataList[id=stock].content
   limit: do 120 znaków
   EN: Owned
   PL:
140. [Interfejs i ustawienia [stable] — tekst] 안정
   źródło: BattleUIText.json :: dataList[id=stable].content
   limit: do 120 znaków
   EN: Stable
   PL:
141. [Interfejs i ustawienia [un_stable] — tekst] 불안정
   źródło: BattleUIText.json :: dataList[id=un_stable].content
   limit: do 120 znaków
   EN: Unstable
   PL:
142. [Interfejs i ustawienia [vibration_explosion] — tekst] 진동 폭발!
   źródło: BattleUIText.json :: dataList[id=vibration_explosion].content
   limit: do 120 znaków
   EN: Tremor Burst!
   PL:
143. [Interfejs i ustawienia [sinking_surge] — tekst] 침잠쇄도!
   źródło: BattleUIText.json :: dataList[id=sinking_surge].content
   limit: do 120 znaków
   EN: Sinking Deluge!
   PL:
144. [Interfejs i ustawienia [targetSlotWeight] — tekst] 공격 가중치
   źródło: BattleUIText.json :: dataList[id=targetSlotWeight].content
   limit: do 120 znaków
   EN: Atk Weight
   PL:
145. [Interfejs i ustawienia [EGO_ErodeProbability] — tekst] 침식확률
   źródło: BattleUIText.json :: dataList[id=EGO_ErodeProbability].content
   limit: do 120 znaków
   EN: To Corrode
   PL:
146. [Interfejs i ustawienia [EGOSelectUI_resources_lack] — tekst] 자원이 부족합니다.\n문양을 확인해 주세요.
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_resources_lack].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You lack sufficient resources.\nPlease check the symbols.
   PL:
147. [Interfejs i ustawienia [EGOSelectUI_DetailInfo] — tekst] 상세 정보
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_DetailInfo].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
148. [Interfejs i ustawienia [ab_part_destroyable] — tekst] 파괴 가능
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyable].content
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
149. [Interfejs i ustawienia [ab_part_destroyable_and_can_vanish] — tekst] 파괴 및 적출 가능
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyable_and_can_vanish].content
   limit: do 120 znaków
   EN: Destr. & Severable
   PL:
150. [Interfejs i ustawienia [ab_guidebook_view] — tekst] 도감 보기
   źródło: BattleUIText.json :: dataList[id=ab_guidebook_view].content
   limit: do 120 znaków
   EN: View Logs
   PL:
151. [Interfejs i ustawienia [show_BattleAblityUI] — tekst] 전투 중 상세 정보 UI 표시
   źródło: BattleUIText.json :: dataList[id=show_BattleAblityUI].content
   limit: do 120 znaków
   EN: Display detailed info UI in Combat Phase
   PL:
152. [Interfejs i ustawienia [Ahab_NotTarget_Onece] — tekst] 내가 진짜 노려야하는건…
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Onece].content
   limit: do 120 znaków
   EN: Where my Harpoon must strike...
   PL:
153. [Interfejs i ustawienia [Ahab_NotTarget_Twice] — tekst] 늘 앞만 뚫어지게 바라봐야만하는게 아니야...
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Twice].content
   limit: do 120 znaków
   EN: ... Sometimes, the answer isn't right before me.
   PL:
154. [Interfejs i ustawienia [Ahab_NotTarget_Thrice] — tekst] 나아가려면 내 옆에 있던 것들\n바라봐야할 때도 있는거야…
   źródło: BattleUIText.json :: dataList[id=Ahab_NotTarget_Thrice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sometimes, to move forward...\n... I have to turn and look beside me.
   PL:
155. [Interfejs i ustawienia [show_BattleUnitAblityUI] — tekst] 전투 중 효과 UI 표시
   źródło: BattleUIText.json :: dataList[id=show_BattleUnitAblityUI].content
   limit: do 120 znaków
   EN: Show active effects UI in Combat Phase
   PL:
156. [Interfejs i ustawienia [LobotomyStartTypo_Title_1] — tekst] 녹빛 여명의 시련
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Title_1].content
   limit: do 120 znaków
   EN: The Dawn of Green
   PL:
157. [Interfejs i ustawienia [LobotomyStartTypo_Name_1] — tekst] 의문
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Name_1].content
   limit: do 120 znaków
   EN: Doubt
   PL:
158. [Interfejs i ustawienia [LobotomyStartTypo_Desc_1] — tekst] 어느날 의문이 생겼다. 우리는 어디서 왔는가. 누군가에게 생명을 받고 무책임하게 놓여졌다.
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_Desc_1].content
   limit: do 180 znaków
   EN: One day, a question crossed through my mind. Where do we come from? We were given life and left in this world against our own volition.
   PL:
159. [Interfejs i ustawienia [LobotomyStartTypo_KillCountTitle_1] — tekst] 제압 현황
   źródło: BattleUIText.json :: dataList[id=LobotomyStartTypo_KillCountTitle_1].content
   limit: do 120 znaków
   EN: Suppression Status
   PL:
160. [Interfejs i ustawienia [LobotomyClearTypo_Title_1] — tekst] 녹빛 여명의 시련
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Title_1].content
   (powtórzenie elementu 156 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
161. [Interfejs i ustawienia [LobotomyClearTypo_Name_1] — tekst] 의문
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Name_1].content
   (powtórzenie elementu 157 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
162. [Interfejs i ustawienia [LobotomyClearTypo_Desc_1] — tekst] 살아간다는 것은 고통이었다.
   źródło: BattleUIText.json :: dataList[id=LobotomyClearTypo_Desc_1].content
   limit: do 120 znaków
   EN: To live was a process full of pain.
   PL:
163. [Interfejs i ustawienia [LobotomyEndTypo_Title] — tekst] 제압 시간 만료
   źródło: BattleUIText.json :: dataList[id=LobotomyEndTypo_Title].content
   limit: do 120 znaków
   EN: Time Limit Reached
   PL:
164. [Interfejs i ustawienia [LobotomyEndTypo_Desc] — tekst] 남은 시련 개체: {0}
   źródło: BattleUIText.json :: dataList[id=LobotomyEndTypo_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Remaining Ordeal Entities: {0}
   PL:
165. [Interfejs i ustawienia [abnormality_all_part] — tekst] 전체 부위
   źródło: BattleUIText.json :: dataList[id=abnormality_all_part].content
   limit: do 120 znaków
   EN: All Parts
   PL:
166. [Interfejs i ustawienia [applying_buff_format] — tekst] {0} 적용중
   źródło: BattleUIText.json :: dataList[id=applying_buff_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Activated
   PL:
167. [Interfejs i ustawienia [level_number_UNDEF] — tekst] 미정
   źródło: BattleUIText.json :: dataList[id=level_number_UNDEF].content
   limit: do 120 znaków
   EN: Undef.
   PL:
168. [Interfejs i ustawienia [level_number_HYPHEN] — tekst] -
   źródło: BattleUIText.json :: dataList[id=level_number_HYPHEN].content
   limit: do 120 znaków
   EN: -
   PL:
169. [Interfejs i ustawienia [received_the_golden_bough_undecided] — tekst] ?
   źródło: BattleUIText.json :: dataList[id=received_the_golden_bough_undecided].content
   limit: do 120 znaków
   EN: ?
   PL:
170. [Interfejs i ustawienia [vibration_fusion] — tekst] 진폭 얽힘!
   źródło: BattleUIText.json :: dataList[id=vibration_fusion].content
   limit: do 120 znaków
   EN: Amplitude Entanglement!
   PL:
171. [Interfejs i ustawienia [BatonPassUIText] — tekst] 대기해제
   źródło: BattleUIText.json :: dataList[id=BatonPassUIText].content
   limit: do 120 znaków
   EN: Substitute
   PL:
172. [Interfejs i ustawienia [perfect] — tekst] 완전
   źródło: BattleUIText.json :: dataList[id=perfect].content
   limit: do 120 znaków
   EN: A-Res
   PL:
173. [Interfejs i ustawienia [ab_part_destroyed] — tekst] 파괴 완료
   źródło: BattleUIText.json :: dataList[id=ab_part_destroyed].content
   limit: do 120 znaków
   EN: Destroyed
   PL:
174. [Interfejs i ustawienia [ab_part_vanished] — tekst] 파괴 및 적출 완료
   źródło: BattleUIText.json :: dataList[id=ab_part_vanished].content
   limit: do 120 znaków
   EN: Destr. & Severed
   PL:
175. [Interfejs i ustawienia [ab_part_cannot_destroy_and_vanish] — tekst] 파괴 및 적출 불가
   źródło: BattleUIText.json :: dataList[id=ab_part_cannot_destroy_and_vanish].content
   limit: do 120 znaków
   EN: Indestr. & Unsever.
   PL:
176. [Interfejs i ustawienia [current_hp] — tekst] 현재 체력
   źródło: BattleUIText.json :: dataList[id=current_hp].content
   limit: do 120 znaków
   EN: Current HP
   PL:
177. [Interfejs i ustawienia [break_section_format] — tekst] 흐트러짐 [{0}]
   źródło: BattleUIText.json :: dataList[id=break_section_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Stagger [{0}]
   PL:
178. [Interfejs i ustawienia [no_break_section] — tekst] 흐트러짐 없음
   źródło: BattleUIText.json :: dataList[id=no_break_section].content
   limit: do 120 znaków
   EN: No Stagger Threshold
   PL:
179. [Interfejs i ustawienia [correction_based_on_unit_keyword] — tekst] {0} 인격 보정 값 {1}(, )
   źródło: BattleUIText.json :: dataList[id=correction_based_on_unit_keyword].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Identity Modifier: {1}(, )
   PL:
180. [Interfejs i ustawienia [battle_operation_counter] — tekst] 강화 반격
   źródło: BattleUIText.json :: dataList[id=battle_operation_counter].content
   limit: do 120 znaków
   EN: Power Counter
   PL:
181. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_0] — tekst] 여명
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_0].content
   limit: do 120 znaków
   EN: Dawn
   PL:
182. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_1] — tekst] 정오
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_1].content
   limit: do 120 znaków
   EN: Noon
   PL:
183. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_2] — tekst] 어스름
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_2].content
   limit: do 120 znaków
   EN: Dusk
   PL:
184. [Interfejs i ustawienia [LOBOTOMY_ORDEAL_TIME_TYPE_3] — tekst] 자정
   źródło: BattleUIText.json :: dataList[id=LOBOTOMY_ORDEAL_TIME_TYPE_3].content
   limit: do 120 znaków
   EN: Midnight
   PL:
185. [Interfejs i ustawienia [LobotomyOrdealTypo_QliphothLevel] — tekst] 클리포트 폭주 - {0}단계
   źródło: BattleUIText.json :: dataList[id=LobotomyOrdealTypo_QliphothLevel].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Qliphoth Meltdown - Level {0}
   PL:
186. [Interfejs i ustawienia [SinkingWhite_stack] — tekst] 산나비
   źródło: BattleUIText.json :: dataList[id=SinkingWhite_stack].content
   limit: do 120 znaków
   EN: The Living
   PL:
187. [Interfejs i ustawienia [SinkingWhite_turn] — tekst] 죽은나비
   źródło: BattleUIText.json :: dataList[id=SinkingWhite_turn].content
   limit: do 120 znaków
   EN: The Departed
   PL:
188. [Interfejs i ustawienia [BulletLament_stack] — tekst] 산나비(탄환)
   źródło: BattleUIText.json :: dataList[id=BulletLament_stack].content
   limit: do 120 znaków
   EN: The Living(Ammo)
   PL:
189. [Interfejs i ustawienia [BulletLament_turn] — tekst] 죽은나비(탄환)
   źródło: BattleUIText.json :: dataList[id=BulletLament_turn].content
   limit: do 120 znaków
   EN: The Departed(Ammo)
   PL:
190. [Interfejs i ustawienia [Retreat_TextAlarm] — tekst] !퇴각!
   źródło: BattleUIText.json :: dataList[id=Retreat_TextAlarm].content
   limit: do 120 znaków
   EN: !Retreat!
   PL:
191. [Interfejs i ustawienia [Retreat_TextPassive] — tekst] 퇴각 중
   źródło: BattleUIText.json :: dataList[id=Retreat_TextPassive].content
   limit: do 120 znaków
   EN: Retreating
   PL:
192. [Interfejs i ustawienia [battle_operation_defense] — tekst] 강화 방어
   źródło: BattleUIText.json :: dataList[id=battle_operation_defense].content
   limit: do 120 znaków
   EN: Power Guard
   PL:
193. [Interfejs i ustawienia [battle_operation_defense_TextTypo] — tekst] 위력 경감!
   źródło: BattleUIText.json :: dataList[id=battle_operation_defense_TextTypo].content
   limit: do 120 znaków
   EN: Depowered!
   PL:
194. [Interfejs i ustawienia [battle_StageBuffUI_Stackdesc] — tekst] (현재 수치: {0})
   źródło: BattleUIText.json :: dataList[id=battle_StageBuffUI_Stackdesc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Current Value: {0})
   PL:
195. [Interfejs i ustawienia [EGOSelectUI_not_allow] — tekst] 현재 장착이 불가능한 에고입니다.
   źródło: BattleUIText.json :: dataList[id=EGOSelectUI_not_allow].content
   limit: do 120 znaków
   EN: This E.G.O cannot be equipped at the moment.
   PL:
196. [Interfejs i ustawienia [laceration_surge] — tekst] 출혈쇄도!
   źródło: BattleUIText.json :: dataList[id=laceration_surge].content
   limit: do 120 znaków
   EN: Bleed Deluge!
   PL:
197. [Interfejs i ustawienia [QTE_Notice] — tekst] 같이 달려나가는 거야!
   źródło: BattleUIText.json :: dataList[id=QTE_Notice].content
   limit: do 120 znaków
   EN: GALLOP ON, TOGETHER!
   PL:
198. [Interfejs i ustawienia [septempeccata_classification] — tekst] {0}형
   źródło: BattleUIText.json :: dataList[id=septempeccata_classification].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Class {0}
   PL:
199. [Interfejs i ustawienia [run_forBattlePortraitStateText] — tekst] 후퇴
   źródło: BattleUIText.json :: dataList[id=run_forBattlePortraitStateText].content
   limit: do 120 znaków
   EN: FLED
   PL:
200. [Interfejs i ustawienia [ReturnPassUIText] — tekst] 복귀
   źródło: BattleUIText.json :: dataList[id=ReturnPassUIText].content
   limit: do 120 znaków
   EN: Return
   PL:
201. [Interfejs i ustawienia [NoHavePassive] — tekst] 동기화 단계 낮음\n서포트 패시브 비활성화 상태
   źródło: BattleUIText.json :: dataList[id=NoHavePassive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Support Passive Locked\nUptie to Unlock
   PL:
202. [Interfejs i ustawienia [LocalSetButtonTitle_ImportanceLevel] — tekst] 중요도
   źródło: BattleUIText.json :: dataList[id=LocalSetButtonTitle_ImportanceLevel].content
   limit: do 120 znaków
   EN: Hints
   PL:
203. [Interfejs i ustawienia [Retreat_Command_TextAlarm] — tekst] !퇴각 명령!
   źródło: BattleUIText.json :: dataList[id=Retreat_Command_TextAlarm].content
   limit: do 120 znaków
   EN: !Retreat Order!
   PL:
204. [Interfejs i ustawienia [Retreat_Quit_TextAlarm] — tekst] !전장 이탈!
   źródło: BattleUIText.json :: dataList[id=Retreat_Quit_TextAlarm].content
   limit: do 120 znaków
   EN: !Escape Battlefield!
   PL:
205. [Interfejs i ustawienia [ab_part_gadget_activated] — tekst] 활성화
   źródło: BattleUIText.json :: dataList[id=ab_part_gadget_activated].content
   limit: do 120 znaków
   EN: On
   PL:
206. [Interfejs i ustawienia [ab_part_gadget_deactivated] — tekst] 비활성화
   źródło: BattleUIText.json :: dataList[id=ab_part_gadget_deactivated].content
   limit: do 120 znaków
   EN: Off
   PL:
207. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_1_Desc] — tekst] !대응 중요도: 중간!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_1_Desc].content
   limit: do 120 znaków
   EN: !Priority:Med.!
   PL:
208. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_2_Desc] — tekst] !대응 중요도: 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_2_Desc].content
   limit: do 120 znaków
   EN: !Priority:High!
   PL:
209. [Interfejs i ustawienia [UpperSkillInfo_Player_ImportanceLevel_3_Desc] — tekst] !대응 중요도: 매우 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Player_ImportanceLevel_3_Desc].content
   limit: do 120 znaków
   EN: !Priority:V.High!
   PL:
210. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_1_Desc] — tekst] !대응 중요도: 중간!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_1_Desc].content
   limit: do 120 znaków
   EN: !Priority: Med.!
   PL:
211. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_2_Desc] — tekst] !대응 중요도: 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_2_Desc].content
   limit: do 120 znaków
   EN: !Priority: High!
   PL:
212. [Interfejs i ustawienia [UpperSkillInfo_Enemy_ImportanceLevel_3_Desc] — tekst] !대응 중요도: 매우 높음!
   źródło: BattleUIText.json :: dataList[id=UpperSkillInfo_Enemy_ImportanceLevel_3_Desc].content
   limit: do 120 znaków
   EN: !Priority: Very High!
   PL:
213. [Interfejs i ustawienia [EgoGiftListPopupTabType_CANDIDATE] — tekst] 조건부 발동
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_CANDIDATE].content
   limit: do 120 znaków
   EN: Conditional
   PL:
214. [Interfejs i ustawienia [EgoGiftListPopupTabType_EXCLUDE_CANDIDATE] — tekst] 상시 발동
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_EXCLUDE_CANDIDATE].content
   limit: do 120 znaków
   EN: Always Active
   PL:
215. [Interfejs i ustawienia [EgoGiftListPopupTabType_active] — tekst] 발동 중
   źródło: BattleUIText.json :: dataList[id=EgoGiftListPopupTabType_active].content
   limit: do 120 znaków
   EN: Activated
   PL:
216. [Interfejs i ustawienia [UnitInformation_emptySkillList] — tekst] 스킬이 없습니다.
   źródło: BattleUIText.json :: dataList[id=UnitInformation_emptySkillList].content
   limit: do 120 znaków
   EN: No Skills in this category.
   PL:
217. [Interfejs i ustawienia [retire_forBattlePortraitStateText] — tekst] 전투 불능
   źródło: BattleUIText.json :: dataList[id=retire_forBattlePortraitStateText].content
   limit: do 120 znaków
   EN: Incapacitated
   PL:
218. [Interfejs i ustawienia [KAA1C9ActivateEffect] — tekst] 사용된 K사 앰플
   źródło: BattleUIText.json :: dataList[id=KAA1C9ActivateEffect].content
   limit: do 120 znaków
   EN: Used K Corp. Ampule
   PL:
219. [Interfejs i ustawienia [contMineInfo_Title] — tekst] 현재 진행 중인 회차
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Title].content
   limit: do 120 znaków
   EN: Progress:
   PL:
220. [Interfejs i ustawienia [contMineInfo_Desc_Valid_Reward] — tekst] ※ 스테이지 포기 시 모듈 {0}개 소모 및 보상 획득
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Desc_Valid_Reward].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ Forfeiting the Stage now will cost {0} Enkephalin Modules and yield rewards based on Modules used
   PL:
221. [Interfejs i ustawienia [contMineInfo_Desc_Invalid_Reward] — tekst] ※ 스테이지 포기 시 모듈 소모·보상 획득 없음
   źródło: BattleUIText.json :: dataList[id=contMineInfo_Desc_Invalid_Reward].content
   limit: do 120 znaków
   EN: ※ Forfeiting the Stage now will not cost Enkephalin Modules and will not yield rewards
   PL:
222. [Interfejs i ustawienia [battle_operation_player_support] — tekst] 서포트
   źródło: BattleUIText.json :: dataList[id=battle_operation_player_support].content
   limit: do 120 znaków
   EN: Support
   PL:
223. [Interfejs i ustawienia [PassiveSynergyConditionCount] — tekst] {0}
   źródło: BattleUIText.json :: dataList[id=PassiveSynergyConditionCount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}
   PL:

## Interfejs i ustawienia: ErrorCodeMsg
- plik gry: `ErrorCodeMsg.json`

224. [Interfejs i ustawienia [servererror_content] — tekst] 서버 에러가 발생하였습니다.\n잠시 후에 다시 시도해 주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A server error has occurred.\nPlease try again in a moment.
   PL:
225. [Interfejs i ustawienia [serverstate_blocking_endpoint] — tekst] 현재 점검 중인 기능입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_blocking_endpoint].content
   limit: do 120 znaków
   EN: This function is currently under maintenance.
   PL:
226. [Interfejs i ustawienia [networkingerror_content] — tekst] 네트워크가 불안정합니다.\n 네트워크 상태를 확인해 주세요
   źródło: ErrorCodeMsg.json :: dataList[id=networkingerror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The network is unstable.\nPlease check your Internet connection.
   PL:
227. [Interfejs i ustawienia [serverstate_temporary_check] — tekst] 서버 임시 점검이 진행 중입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_temporary_check].content
   limit: do 120 znaków
   EN: The server is currently under temporary maintenance.
   PL:
228. [Interfejs i ustawienia [serverstate_regularcheck] — tekst] 서버 정기 점검이 진행 중입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_regularcheck].content
   limit: do 120 znaków
   EN: The server is currently under routine maintenance.
   PL:
229. [Interfejs i ustawienia [serverstate_openpreparation] — tekst] 오픈 준비 중입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_openpreparation].content
   limit: do 120 znaków
   EN: Things are still being prepared!
   PL:
230. [Interfejs i ustawienia [serverstate_verify_invaliduser] — tekst] 존재하지 않거나 탈퇴 처리가 완료된 계정입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_verify_invaliduser].content
   limit: do 120 znaków
   EN: The account does not exist or has been closed.
   PL:
231. [Interfejs i ustawienia [serverstate_verify_ban] — tekst] 게임 이용이 제한된 계정입니다.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_verify_ban].content
   limit: do 120 znaków
   EN: The account is restricted from playing.
   PL:
232. [Interfejs i ustawienia [serverstate_verify_invalidauth] — tekst] 오류가 발생하였습니다.\n다시 로그인을 진행해주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_verify_invalidauth].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An error has occurred.\nPlease sign in again.
   PL:
233. [Interfejs i ustawienia [serverstate_verify_invalidclientversion] — tekst] 게임 클라이언트가 최신 버전이 아닙니다.\n업데이트를 진행해주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_verify_invalidclientversion].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Game client is not up to date.\nPlease update to the latest version.
   PL:
234. [Interfejs i ustawienia [serverstate_verify_invaliduuid] — tekst] 이미 처리된 요청입니다.\n동기화를 위해 게임을 다시 실행해 주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_verify_invaliduuid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This request has already been processed.\nPlease restart the game to synchronize.
   PL:
235. [Interfejs i ustawienia [serverstate_error_thirdparty_api] — tekst] 외부 서버와의 통신에 문제가 발생하였습니다. 잠시 후에 다시 시도해 주십시오.
   źródło: ErrorCodeMsg.json :: dataList[id=serverstate_error_thirdparty_api].content
   limit: do 120 znaków
   EN: External server connection error. Please try again at a later time.
   PL:
236. [Interfejs i ustawienia [servererror_invalid_purchasing_package] — tekst] 상품거래에 실패하였습니다.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_invalid_purchasing_package].content
   limit: do 120 znaków
   EN: Transaction failed.
   PL:
237. [Interfejs i ustawienia [servererror_remain_restore_purchasing] — tekst] 아직 진행중이던 거래가 존재합니다.\n[구매 복구] 버튼을 눌러 재시도해주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_remain_restore_purchasing].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A transaction is still in progress.\nPlease use the [Restore Purchase] button and try again.
   PL:
238. [Interfejs i ustawienia [servererror_invalid_battle_version] — tekst] 버전이 업데이트 되었습니다.\n리소스 다운로드 후 다시 시도해주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_invalid_battle_version].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Version update available.\nPlease download new resources and try again.
   PL:
239. [Interfejs i ustawienia [servererror_steam_auth_error] — tekst] 스팀 로그인에 실패했습니다.\n스팀 로그인 상태를 확인해주시고, 잠시 후에 재시도 해주시길 바랍니다.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_steam_auth_error].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed to login via Steam.\nPlease check your Steam login status and try again at a later time.
   PL:
240. [Interfejs i ustawienia [servererror_invalid_date] — tekst] 기기의 시간 설정이 다릅니다.\n기기의 시간을 인터넷 시간과 동기화 후 재시도 해주시길 바랍니다.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_invalid_date].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The device time does not match.\nPlease try again after ensuring your device's system clock is synced with the internet time.
   PL:
241. [Interfejs i ustawienia [servererror_lack_of_stamina] — tekst] 보유한 엔케팔린 동기화에 실패하였습니다.\n기기의 시간 설정이 "자동"인지 확인해 주시길 바랍니다.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_lack_of_stamina].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed to sync currently owned Enkephalin.\nPlease check your device settings to verify if your time has been set automatically.
   PL:
242. [Interfejs i ustawienia [servererror_egogift_not_exist] — tekst] 보유한 E.G.O 기프트 동기화에 실패하여\n작업을 완료할 수 없습니다.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_egogift_not_exist].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed to sync currently owned E.G.O Gift list.\nTask could not be completed.
   PL:
243. [Interfejs i ustawienia [servererror_already_entered_stage] — tekst] 이미 진행 중인 스테이지가 있습니다.\n진행 상황 동기화를 위해 재접속해 주세요.
   źródło: ErrorCodeMsg.json :: dataList[id=servererror_already_entered_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: There is a stage already in progress.\nPlease log in again to synchronize your progress.
   PL:

## Interfejs i ustawienia: FAQ
- plik gry: `FAQ.json`

244. [Interfejs i ustawienia [faq_description] — tekst] 자주 묻는 질문을\n이곳에서 확인할 수 있습니다.
   źródło: FAQ.json :: dataList[id=faq_description].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You can check\nFrequently Asked Questions here.
   PL:
245. [Interfejs i ustawienia [faq_payment] — tekst] 결제
   źródło: FAQ.json :: dataList[id=faq_payment].content
   limit: do 120 znaków
   EN: Payment
   PL:
246. [Interfejs i ustawienia [faq_payment_title_1] — tekst] 월간 광기 패키지 / 월간 광기 하프 패키지는 어떻게 사용되나요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_1].content
   limit: do 120 znaków
   EN: How does the Monthly Lunacy Supply work?
   PL:
247. [Interfejs i ustawienia [faq_payment_desc_1] — tekst] <b>월간 광기 패키지</b>를 구매하신 경우, 구매 보상인 광기가 650만큼 지급되며, 구매일로부터 30일 동안 아래와 같은 일일 보상을 수령할 수 있습니다.<b>월간 광기 하프 패키지</b>를 구매하신 경우, 구매 보상인 광기가 130만큼 지급되며, 구매일로부터 30일 동안 아래와 같은 일일 보상을 수령할 수 있습니다.\n\n■ 월간 광기 패키지 일일 보상:\n무료 광기 65\n\n■ 월간 광기 하프 패키지 일일 보상:\n무료 광기 39\n\n\n※ 주의사항\n1) 모든 보상은 게임 내 우편으로 지급됩니다.\n2) 위 두 패키지는 별개로 적용됩니다.\n3) 두 패키지는 최대 2번 추가 구매 가능합니다. (최대 67일까지 추가 가능)\n4) 게임 미접속 시 해당 날짜의 보상은 지급되지 않습니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_1].content
   limit: do 1000 znaków
   tokeny: zachowaj dokładnie: <b>, </b>, \n
   EN: When you purchase the <b>Monthly Lunacy Supply</b>, you will be given 650 Lunacy upfront, and you become eligible to receive the daily rewards listed below for the following 30 days.\nWhen you purchase the <b>Monthly Lunacy Batch</b>, you will be given 130 Lunacy upfront, and you become eligible to receive the daily rewards listed below for the following 30 days.\n\n■ Daily Rewards from Monthly Lunacy Supply:\n65 Free Lunacy\n\n■ Daily Rewards from Monthly Lunacy Batch:\n39 Free Lunacy\n\n※ NOTES\n1) All rewards are provided through in-game mail.\n2) The two monthly packs function separately.\n3) The two monthly packs can be purchased again up to two times within their duration. (This duration can be extended up to 67 days.)\n4) The daily rewards will not be provided for days when you do not log into the game.
   PL:
248. [Interfejs i ustawienia [faq_payment_title_2] — tekst] 결제된 상품을 환불하고 싶어요. 방법이 어떻게 되나요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_2].content
   limit: do 120 znaków
   EN: I want to refund an item I purchased. How do I?
   PL:
249. [Interfejs i ustawienia [faq_payment_desc_2] — tekst] 결제 상품 환불의 경우, 결제 후 7일 이내 문의 접수 및 지급된 아이템을 사용하지 않으셨을 경우에만 결제 취소가 가능합니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_2].content
   limit: do 130 znaków
   EN: You may request a refund within 7 days of purchase as long as you did not use the purchased item.
   PL:
250. [Interfejs i ustawienia [faq_payment_title_3] — tekst] 환불이 가능한 결제 상품은 어떤 것들이 있나요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_3].content
   limit: do 120 znaków
   EN: What are purchases I am able to refund?
   PL:
251. [Interfejs i ustawienia [faq_payment_desc_3] — tekst] 각종 패키지, 기간제 상품, 보너스 포함 상품 등의 경우 수령 즉시 효과가 적용된 것으로 간주되어 부득이하게 환불 진행에 도움을 드리기 어려운 점 양해 부탁드립니다.\n그 외에는 구매일로부터 14일이 지나지 않았으며, 수령 이후 사용하지 않은 상품에 한해 결제 상품 환불을 진행하실 수 있습니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_3].content
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please understand that certain packs, period-based products, items that include bonuses, and other products that come immediately into effect upon purchase may be difficult to refund.\nOtherwise, you may request a refund for items within 14 days of purchase as long as you did not use them.
   PL:
252. [Interfejs i ustawienia [faq_payment_title_4] — tekst] 결제한 내역이나 영수증은 어디서 확인할 수 있나요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_4].content
   limit: do 120 znaków
   EN: Where can I see my purchase history or receipts?
   PL:
253. [Interfejs i ustawienia [faq_payment_desc_4] — tekst] <b>구글 결제를 통한 확인 방법</b>\n1. 구글 결제센터(<color=#F8C200><u><link="https://payments.google.com/">https://payments.google.com/</link></u></color>)에 접속\n2. 결제한 구글 계정으로 로그인\n3. 구매 내역 보기 선택\n4. 확인하고 싶은 내역 선택\n5. 거래 ID 확인 (GPA. 0000-0000-0000-00000의 형태)\n\n<b>앱스토어를 통한 확인 방법</b>\n1. 아이튠즈 페이지(<color=#F8C200><u><link="https://www.apple.com/kr/itunes/">https://www.apple.com/kr/itunes/</link></u></color>) 접속\n2. 로그인 후 [계정] 항목 선택\n3. 구매 내역에서 [모두 보기] 선택\n\n<b>스팀을 통한 확인 방법</b>\n1. 고객센터 페이지(<color=#F8C200><u><link="https://help.steampowered.com/">https://help.steampowered.com/</link></u></color>)접속\n2. 구매 항목 선택\n3. 전체 구매 기록 보기 선택\n4. 확인하고 싶은 내역 선택
   źródło: FAQ.json :: dataList[id=faq_payment_desc_4].content
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: <b>, </b>, <color=#F8C200>, <u>, <link="https://payments.google.com/">, </link>, </u>, </color>, <link="https://www.apple.com/kr/itunes/">, <link="https://help.steampowered.com/">, \n
   EN: <b>Using Google Pay</b>\n1. Enter Google Payment center (<color=#F8C200><u><link="https://payments.google.com/">https://payments.google.com/</link></u></color>)\n2. Log in with the Google account used to make the purchase\n3. Go to [Activity]\n4. Select the transaction to examine\n5. Check transaction ID (GPA. 0000-0000-0000-00000)\n\n<b>Using App Store</b>\n1. Enter iTunes page (<color=#F8C200><u><link="https://www.apple.com/kr/itunes/">https://www.apple.com/kr/itunes/</link></u></color>)\n2. Log in and go to [Account]\n3. Select [View All] in purchase history\n\n<b>Using Steam</b>\n1. Enter customer support page (<color=#F8C200><u><link="https://help.steampowered.com/">https://help.steampowered.com/</link></u></color>)\n2. Go to [Purchases]\n3. Go to [View complete purchasing history]\n4. Check the transaction
   PL:
254. [Interfejs i ustawienia [faq_payment_title_5] — tekst] 동일한 상품이 중복 결제되었어요.
   źródło: FAQ.json :: dataList[id=faq_payment_title_5].content
   limit: do 120 znaków
   EN: Multiple payments were made for one item.
   PL:
255. [Interfejs i ustawienia [faq_payment_desc_5] — tekst] 상품이 중복으로 결제되었다면, 결제 영수증과 결제 내역을 포함하여 게임 내 고객센터로 문의를 보내주시기 바랍니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_5].content
   limit: do 230 znaków
   EN: If you encounter an error where multiple payments are made for a single product, please send an inquiry to customer service with the purchase history and the receipt included.
   PL:
256. [Interfejs i ustawienia [faq_payment_title_6] — tekst] 결제했는데 아직 상품이 없어요. 어떻게 해야하나요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_6].content
   limit: do 120 znaków
   EN: I made a purchase, but the item hasn’t arrived. What should I do?
   PL:
257. [Interfejs i ustawienia [faq_payment_desc_6] — tekst] 게임 아이템을 구매하셨으나, 오류로 지급받지 못한 경우 게임 내 고객센터로 결제 영수증을 포함하여 문의 보내주시기 바랍니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_6].content
   limit: do 210 znaków
   EN: If you have encountered an error where you failed to receive in-game items from your purchase, please send an inquiry to customer service with the receipt included.
   PL:
258. [Interfejs i ustawienia [faq_payment_title_7] — tekst] 결제가 계속 실패하는데 이유가 뭘까요?
   źródło: FAQ.json :: dataList[id=faq_payment_title_7].content
   limit: do 120 znaków
   EN: My payment keeps failing to process, why is that?
   PL:
259. [Interfejs i ustawienia [faq_payment_desc_7] — tekst] 현재 게임 내에서 구매할 수 있는 결제 상품은 플레이 스토어(구글)와 앱스토어를 통해 판매되고 있으며, 결제 수단도 다양하기에 원인이 다양하게 있을 수 있습니다.\n\n■ 결제 실패 해결 방법\n1) 원활한 네트워크 환경에서 게임 종료 후 재실행\n2) 계정 설정 문제 발생 (구글 결제 고객센터 혹은 애플 고객 지원에 문의 필요) \n\n구글 고객지원 홈페이지\n링크 : <color=#F8C200><u><link="https://payments.google.com/payments/u/2/home#oneTimePurchase">https://payments.google.com/payments/u/2/home#oneTimePurchase</link></u></color>\n\n애플 고객지원 홈페이지\n링크 : <color=#F8C200><u><link="https://expresslane.apple.com/GetproductgroupList.action">https://expresslane.apple.com/GetproductgroupList.action</link></u></color>\n\nSTEAM 고객지원 홈페이지\n링크 : <color=#F8C200><u><link="https://help.steampowered.com/">https://help.steampowered.com/</link></u></color>\n\n3) 통신사 결제 문제 발생 (통신사로 문의)\n- 소액 결제 결제 한도 등 결제 수단의 문제가 있다면, 이용하는 카드사 또는 통신사 고객센터를 통해 확인하실 수 있어요.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_7].content
   limit: do 920 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, <u>, <link="https://payments.google.com/payments/u/2/home#oneTimePurchase">, </link>, </u>, </color>, <link="https://expresslane.apple.com/GetproductgroupList.action">, <link="https://help.steampowered.com/">, \n
   EN: The in-game items are currently sold through the Google Play Store and App Store, taking a variety of payment methods; there may be various causes for the issue.\n\n■ Possible Solutions for Failed Transactions\n1) Restart the game under a stable network connection\n2) For problems with the account setting: \n\nGoogle Customer Support\nLink: <color=#F8C200><u><link="https://payments.google.com/payments/u/2/home#oneTimePurchase">https://payments.google.com/payments/u/2/home#oneTimePurchase</link></u></color>\n\nApple Customer Support\nLink: <color=#F8C200><u><link="https://expresslane.apple.com/GetproductgroupList.action">https://expresslane.apple.com/GetproductgroupList.action</link></u></color>\n\nSteam Customer Support\nLink: <color=#F8C200><u><link="https://help.steampowered.com/">https://help.steampowered.com/</link></u></color>\n\n3) For problems with processing the payment:\n- For issues with the payment method such as budget limits, you may consult customer support for the card company or the network provider.
   PL:
260. [Interfejs i ustawienia [faq_payment_title_8] — tekst] 상품의 금액과 청구된 결제금액이 달라요.
   źródło: FAQ.json :: dataList[id=faq_payment_title_8].content
   limit: do 120 znaków
   EN: An item’s listed price doesn’t match how much it actually costs.
   PL:
261. [Interfejs i ustawienia [faq_payment_desc_8] — tekst] Limbus Company에서 구매할 수 있는 유료 상품은 각 스토어(구글 플레이스토어, 앱스토어, STEAM)의 정책에 따라 판매되고 있습니다. 유료 상품 구입 시, 상품에 표기된 가격을 기준으로 결제됩니다.\n\n다만, 결제수단에 따라 외화 결제가 진행될 경우, 환율 및 일부 수수료가 추가되어 상품에 기재된 금액과 다소 차이가 있을 수 있는 점 참고 부탁드립니다.
   źródło: FAQ.json :: dataList[id=faq_payment_desc_8].content
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Paid products in Limbus Company follow the policies of the respective store (Google Play Store, App Store, Steam) on which the game is hosted. The price of the items is as displayed.\n\nHowever, please note that there may be minor differences in the sum of payment due to external factors such as exchange rates and fees depending on the means of payment.
   PL:
262. [Interfejs i ustawienia [faq_payment_common_template] — tekst] ■ ANDROID 문의 양식\n1) UID(유저 번호):\n2) 요청 사항 : 결제 취소\n3) 구글 결제 계정 : (이메일 형식)\n4) 결제 일시 :\n5) 결제 상품명/금액 :\n6) 주문번호 : (또는 주문번호가 포함된 구글 영수증 스크린샷 첨부)\n\n■ IOS 문의 양식\n1) UID(유저 번호) :\n2) 요청 사항 : 결제 취소 / 상품 재지급\n3) 주문번호가 확인되는 아이튠즈 결제 내역 스크린샷 첨부 (필수)4) 결제 일시 : \n5) 결제 상품명/금액 : \n\n■ STEAM 문의 양식\n1) UID(유저 번호) :\n2) 요청 사항 : 결제 취소 \n3) 주문번호가 확인되는 STEAM 결제 내역 스크린샷 첨부 (필수)\n4) 결제 일시 : \n5) 결제 상품명/금액 :
   źródło: FAQ.json :: dataList[id=faq_payment_common_template].content
   limit: do 980 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ■ Inquiry Template for Android\n1) UID (User Identification):\n2) Request: Payment cancellation\n3) Google Payment Account: (Enter email here)\n4) Date of Purchase:\n5) Purchased Item and Price Paid:\n6) Transaction ID: (Or a screenshot of the Google receipt with the transaction ID visible)\n\n■ Inquiry Template for iOS\n1) UID (User Identification):\n2) Request: Payment cancellation / Reissuance of item\n3) Screenshot of Purchase Record on iTunes with Identifiable Transaction ID (Mandatory)\n4) Date of Purchase: \n5) Purchased Item and Price Paid: \n\n■ Inquiry Template for STEAM\n1) UID (User Identification):\n2) Request: Payment cancellation\n3) Screenshot of Purchase Record on Steam with Identifiable Transaction ID (Mandatory)\n4) Date of Purchase: \n5) Purchased Item and Price Paid:
   PL:
263. [Interfejs i ustawienia [faq_account] — tekst] 계정
   źródło: FAQ.json :: dataList[id=faq_account].content
   limit: do 120 znaków
   EN: Account
   PL:
264. [Interfejs i ustawienia [faq_account_title_1] — tekst] 계정 ID는 어디서 확인할 수 있나요?
   źródło: FAQ.json :: dataList[id=faq_account_title_1].content
   limit: do 120 znaków
   EN: Where can I check my account ID?
   PL:
265. [Interfejs i ustawienia [faq_account_desc_1] — tekst] 계정 ID는 게임 내 하단 UI의 레벨 위에서 확인하실 수 있습니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_1].content
   limit: do 120 znaków
   EN: The account ID is displayed above the level in the lower side of the screen.
   PL:
266. [Interfejs i ustawienia [faq_account_title_2] — tekst] 계정 연동하는 방법이 궁금해요.
   źródło: FAQ.json :: dataList[id=faq_account_title_2].content
   limit: do 120 znaków
   EN: I want to know how to link my account.
   PL:
267. [Interfejs i ustawienia [faq_account_desc_2] — tekst] 환경 설정 → 기타 탭 → 계정란에서 연동이 가능합니다.\n\n게스트 계정으로 생성하였더라도 연동 완료 시 해당 계정으로 변경되는 점 참고 부탁드리며, 연동하지 않은 계정의 경우 데이터가 소실될 수 있는 점 유의해 주시기 바랍니다.\n\n※ 주의사항\n계정 유실을 방지하기 위해, 1회 이상 연동이 진행되었던 경우 최소 1개 이상의 연동 계정이 유지되도록 설정되어 있습니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_2].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: To link your account, go to Settings → Other → Account.\n\nIf you use a guest account, it will be converted to a registered account after linking. Please note that unlinked accounts are susceptible to data loss when immediate access is lost.\n\n※ NOTE\nTo prevent loss of account data, accounts linked at least once must maintain linkage with at least 1 external service at a time.
   PL:
268. [Interfejs i ustawienia [faq_account_title_3] — tekst] 계정을 잊어버렸어요. / 비밀번호를 잊어버렸어요.
   źródło: FAQ.json :: dataList[id=faq_account_title_3].content
   limit: do 120 znaków
   EN: I forgot my account ID and/or the password.
   PL:
269. [Interfejs i ustawienia [faq_account_desc_3] — tekst] 연동한 계정의 아이디나 비밀번호를 잊어버리셨을 경우, 선생님께서 연동한 계정의 고객센터에 문의하시어 확인 부탁 드리겠습니다.\n\n구글 고객센터: <color=#F8C200><u><link="https://support.google.com/accounts/#topic=3382296">https://support.google.com/accounts/#topic=3382296</link></u></color>\n애플 고객센터: <color=#F8C200><u><link="https://support.apple.com/ko-kr">https://support.apple.com/ko-kr</link></u></color>\n스팀 고객센터: <color=#F8C200><u><link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In</link></u></color>\n\n※주의사항\n게스트 계정의 경우 기기 변경, 애플리케이션 삭제등이 진행되었을 시 모든 계정 관련 데이터가 소실될 수 있는 점 유의해 주시기 바랍니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_3].content
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, <u>, <link="https://support.google.com/accounts/#topic=3382296">, </link>, </u>, </color>, <link="https://support.apple.com/ko-kr">, <link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">, \n
   EN: If you cannot remember the ID or the password of the account you linked your game account to, please contact the customer support of the respective service.\n\nGoogle Customer Support: <color=#F8C200><u><link="https://support.google.com/accounts/#topic=3382296">https://support.google.com/accounts/#topic=3382296</link></u></color>\nApple Customer Support: <color=#F8C200><u><link="https://support.apple.com/ko-kr">https://support.apple.com/ko-kr</link></u></color>\nSteam Customer Support: <color=#F8C200><u><link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In</link></u></color>\n\n※ NOTE\nPlease be aware that unlinked guest accounts may be permanently lost upon migrating devices or deleting the application.
   PL:
270. [Interfejs i ustawienia [faq_account_title_4] — tekst] 기기 변경 및 재설치 이후에도 계정을 사용할 수 있나요?
   źródło: FAQ.json :: dataList[id=faq_account_title_4].content
   limit: do 120 znaków
   EN: Can I keep using my account after changing to a different device or reinstalling the game?
   PL:
271. [Interfejs i ustawienia [faq_account_desc_4] — tekst] 기기를 변경하였거나, 애플리케이션을 삭제 후 재설치하였더라도 기존의 계정으로 로그인하면 계속해서 게임을 진행하실 수 있습니다.\n\n다만, 게스트 계정 생성 이후 별도의 연동을 진행하지 않았다면 기기 변경 및 재설치 시 데이터가 소실될 수 있는 점 유의 부탁드립니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_4].content
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Even if you migrate to a different device or delete and then reinstall the application, you can log in with an existing account to continue playing.\n\nHowever, please note that guest accounts that did not undergo any integration may be lost when access to the application is lost.
   PL:
272. [Interfejs i ustawienia [faq_account_title_5] — tekst] 계정을 삭제(탈퇴)하라면 어떻게 해야하나요
   źródło: FAQ.json :: dataList[id=faq_account_title_5].content
   limit: do 120 znaków
   EN: How do I delete (close) my account?
   PL:
273. [Interfejs i ustawienia [faq_account_desc_5] — tekst] 계정 삭제(탈퇴)의 경우 계정 연동이 되어 있는 상태에서만 가능합니다.\n게스트 계정은 계정 연동하신 후 게임 탈퇴를 진행하실 수 있습니다.\n게임 내에서 설정 → ‘기타’ → ‘계정 탈퇴’를 선택하여 계정 삭제(탈퇴)를 진행할 수 있습니다.\n\n※ 계정 삭제 시 유예기간은 14일로 적용되며, 유예기간이 종료되면 계정 삭제가 완료됩니다.\n※ 계정 삭제를 하시면 게임 정보가 모두 사라지니, 유의하여 진행해주시기 바랍니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_5].content
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You may only delete (close) an account that is linked with another service.\nGuest accounts also need to be linked before closure.\nTo delete (close) an account, enter Settings → ‘Other’ → ‘Close Account’.\n\n※ When you choose to close the account, you will be given a 14-day grace period, after which the closure is fully complete.\n※ All game data will be lost when the account is deleted, so proceed with caution.
   PL:
274. [Interfejs i ustawienia [faq_account_title_6] — tekst] 혹시나 탈퇴한 계정은 복구가 가능한가요?
   źródło: FAQ.json :: dataList[id=faq_account_title_6].content
   limit: do 120 znaków
   EN: Can a closed account be recovered?
   PL:
275. [Interfejs i ustawienia [faq_account_desc_6] — tekst] 게임 탈퇴 후 유예기간(14일)이 지나기 전, 기존에 이용하시던 계정으로 다시 로그인 하시면 탈퇴 복구를 하실 수 있습니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_6].content
   limit: do 130 znaków
   EN: If you log into the account before the 14-day grace period ends, you can restore the account.
   PL:
276. [Interfejs i ustawienia [faq_account_title_7] — tekst] 계정이 차단되었어요. 왜 그런가요?
   źródło: FAQ.json :: dataList[id=faq_account_title_7].content
   limit: do 120 znaków
   EN: My account was suspended. Why is that?
   PL:
277. [Interfejs i ustawienia [faq_account_desc_7] — tekst] 쾌적한 게임 환경을 제공하기 위해 운영정책에 따라 서비스를 제공하고 있습니다.\n운영정책에 위배되는 활동으로 다른 관리자분들 및 게임 서비스에 피해를 줄 경우 게임 이용이 제한 될 수 있습니다.\n\n<color=#F8C200><u><link="https://limbuscompany.kr/policy/">[게임 운영정책 바로 가기]</link></u></color>\n\n운영정책에 따라 게임 이용이 제한되었다면 별도의 조치로 도움을 드릴 수 없는 점 양해 부탁드립니다.
   źródło: FAQ.json :: dataList[id=faq_account_desc_7].content
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, <u>, <link="https://limbuscompany.kr/policy/">, </link>, </u>, </color>, \n
   EN: To provide an enjoyable experience, we operate under Terms of Service.\nMisconduct and violations of the terms that negatively affect the service and its management may result in restrictions from playing the game.\n\n<color=#F8C200><u><link="https://limbuscompany.kr/policy/">[Read full text]</link></u></color>\n\nPlease understand that we are unable to help you with restrictions carried out according to the Terms of Service.
   PL:
278. [Interfejs i ustawienia [faq_account_title_8] — tekst] 계정 연동 실패 해결 방법
   źródło: FAQ.json :: dataList[id=faq_account_title_8].content
   limit: do 120 znaków
   EN: Regarding failure to link accounts
   PL:
279. [Interfejs i ustawienia [faq_account_desc_8] — tekst] 연동한 계정에 문제가 발생하였을 경우 계정 도용 여부를 확인할 수 없어 도움을 드릴 수 없으며, 연동한 계정에 문제가 발생했다면 아래 고객센터에 문의해 주시기 바랍니다.\n\n구글 고객센터: <color=#F8C200><u><link="https://support.google.com/accounts/#topic=3382296">https://support.google.com/accounts/#topic=3382296</link></u></color>\n애플 고객센터: <color=#F8C200><u><link="https://support.apple.com/ko-kr">https://support.apple.com/ko-kr</link></u></color>\n스팀 고객센터: <color=#F8C200><u><link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In</link></u></color>
   źródło: FAQ.json :: dataList[id=faq_account_desc_8].content
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, <u>, <link="https://support.google.com/accounts/#topic=3382296">, </link>, </u>, </color>, <link="https://support.apple.com/ko-kr">, <link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">, \n
   EN: Please understand that we are unable to provide help regarding issues with external accounts linked to the user’s game account as we are unable to ensure that the access is not fraudulent. In such cases, please contact the customer support of the respective service.\n\nGoogle Customer Support: <color=#F8C200><u><link="https://support.google.com/accounts/#topic=3382296">https://support.google.com/accounts/#topic=3382296</link></u></color>\nApple Customer Support: <color=#F8C200><u><link="https://support.apple.com/ko-kr">https://support.apple.com/ko-kr</link></u></color>\nSteam Customer Support: <color=#F8C200><u><link="https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In">https://help.steampowered.com/ko/wizard/HelpWithPurchase.Vender+cromos+raacutepidamente+con+Steam+In</link></u></color>
   PL:
280. [Interfejs i ustawienia [faq_normal] — tekst] 일반
   źródło: FAQ.json :: dataList[id=faq_normal].content
   limit: do 120 znaków
   EN: General
   PL:
281. [Interfejs i ustawienia [faq_normal_title_1] — tekst] 이곳에 없는 문의가 있습니다. 어디로 해야하나요?
   źródło: FAQ.json :: dataList[id=faq_normal_title_1].content
   limit: do 120 znaków
   EN: I couldn’t find an article that answers my question. Where should I make my inquiry?
   PL:
282. [Interfejs i ustawienia [faq_normal_desc_1] — tekst] FAQ(자주묻는 질문)에 없는 문의는 고객센터 이메일로 문의 접수부탁드립니다.\n\n계정문의\n<color=#F8C200><u><link="mailto:limbussupport+account@projmoon.com">limbussupport+account@projmoon.com</link></u></color>\n\n결제문의\n<color=#F8C200><u><link="mailto:limbussupport+payment@projmoon.com">limbussupport+payment@projmoon.com</link></u></color>\n\n버그제보\n<color=#F8C200><u><link="mailto:limbussupport+bug@projmoon.com">limbussupport+bug@projmoon.com</link></u></color>\n\n앱 이용 문제\n<color=#F8C200><u><link="mailto:limbussupport+applicationissue@projmoon.com">limbussupport+applicationissue@projmoon.com</link></u></color>\n\n기타 문의 사항\n<color=#F8C200><u><link="mailto:limbussupport+others@projmoon.com">limbussupport+others@projmoon.com</link></u></color>
   źródło: FAQ.json :: dataList[id=faq_normal_desc_1].content
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, <u>, <link="mailto:limbussupport+account@projmoon.com">, </link>, </u>, </color>, <link="mailto:limbussupport+payment@projmoon.com">, <link="mailto:limbussupport+bug@projmoon.com">, <link="mailto:limbussupport+applicationissue@projmoon.com">, <link="mailto:limbussupport+others@projmoon.com">, \n
   EN: For inquiries not covered in the FAQ, please contact our Customer Service emails listed below.\n\nAccount Inquiry\n<color=#F8C200><u><link="mailto:limbussupport+account@projmoon.com">limbussupport+account@projmoon.com</link></u></color>\n\nPayment Inquiry\n<color=#F8C200><u><link="mailto:limbussupport+payment@projmoon.com">limbussupport+payment@projmoon.com</link></u></color>\n\nBug Report\n<color=#F8C200><u><link="mailto:limbussupport+bug@projmoon.com">limbussupport+bug@projmoon.com</link></u></color>\n\nIssues with application usage\n<color=#F8C200><u><link="mailto:limbussupport+applicationissue@projmoon.com">limbussupport+applicationissue@projmoon.com</link></u></color>\n\nOther Inquiries\n<color=#F8C200><u><link="mailto:limbussupport+others@projmoon.com">limbussupport+others@projmoon.com</link></u></color>
   PL:

## Interfejs i ustawienia: FileDownloadDesc
- plik gry: `FileDownloadDesc.json`

283. [Interfejs i ustawienia [FileDownload_Desc_01] — tytuł] 도시, 그리고 둥지
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_01].title
   limit: do 40 znaków
   EN: The City and the Nests
   PL: Miasto i Gniazda
284. [Interfejs i ustawienia [FileDownload_Desc_01] — opis] 관리자 님이 처해 있는 특수한 상황을 저희는 이해하고 있습니다. 대부분 당연할 사실이지만, 이곳에 기술하도록 하려고 합니다.\n잊으셨을 지 모르지만, 우리는 26개의 구로 나뉘어진 거대한 도시 속에서 살아가고 있습니다. 모든 구역은 둥지라고 불리 우는 핵심 구역이 존재합니다. 새가 둥지 속 알을 품듯, 해당 둥지를 관장하는 거대 기업은 둥지 속 거주민을 보호합니다.\n물론, 모든 빛에 그림자가 있듯이 둥지의 바깥… 뒷골목의 거주민까지 보호하지는 않습니다.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_01].desc
   limit: do 720 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We understand the unique situation you find yourself in, Executive Manager. Allow us to lay down a number of key facts about our world here.\nIn case you’ve become unfamiliar with your surroundings, we live in a massive City, divided into 26 Districts. Each District has a central area called the ‘Nest’, whose inhabitants are under the protection of a corporate entity overseeing the District, much like a bird brooding its eggs.\nAlas, the corporation’s protection doesn’t extend beyond the Nest’s boundaries… The dwellers of the Backstreets have to fend for themselves.
   PL: Rozumiemy, Kierowniku, szczególne położenie, w jakim się pan znalazł. Większość z tego to oczywistości, ale pozwolimy sobie je tu spisać.\nMógł pan zapomnieć, ale żyjemy w ogromnym Mieście podzielonym na 26 Dystryktów. W każdym z nich jest kluczowy obszar zwany Gniazdem. Tak jak ptak wysiaduje jaja w gnieździe, tak wielka korporacja zarządzająca Gniazdem chroni jego mieszkańców.\nRzecz jasna, jak każde światło rzuca cień, tak i ta ochrona nie sięga poza Gniazdo… do mieszkańców Zaułków.
285. [Interfejs i ustawienia [FileDownload_Desc_02] — tytuł] 날개
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_02].title
   limit: do 40 znaków
   EN: The Wings
   PL: Skrzydła
286. [Interfejs i ustawienia [FileDownload_Desc_02] — opis] 새의 날개를 말하는 것이 아닙니다.\n하지만 둥지를 품는 어미 새와도 같으니, 관련성까지 부정할 수는 없겠습니다.\n날개는 도시의 각 둥지를 관장하는 26개의 초 거대 기업을 말합니다. 각 날개는 특이점이라고 불리는 놀라운 기술을 토대로 도시 곳곳의 삶의 질을 높이고, 둥지의 안녕을 도모하고 있다고 알려져 있습니다.\n그러나 날개가 꺾이기라도 하는 날에는 이야기가 달라집니다. 대대로, 도시의 날개가 꺾이는 날에는 어마어마한 사건들이 동반되어 왔죠.\n날개가 꺾인 자리에는 언젠가 새 날개가 돋아나기 마련입니다. 하지만, 그 동안 비어 버린 둥지의 안전은… 누구도 보장하지 못할 것입니다.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_02].desc
   limit: do 940 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This term does not refer to a bird’s bodily structure.\nHowever, one can’t deny that a Wing’s role resembles that of a bird caring for its nest.\nThe ‘Wings’ are a collective term we use to refer to the 26 biggest conglomerates in the City. These Wings contribute to the quality of life in the City via astounding technological feats known as ‘Singularities’. Under the jurisdiction of a Wing, the citizens of each Nest enjoy comfortable and safe lives. However, that changes the moment a Wing is snapped or plucked of its feathers; historically, the fall of a Wing has accompanied events of considerable magnitudes.\nIn time, a new Wing will rise to fill that vacant spot. In the meantime, though… no one can guarantee your safety in its fallen Nest.
   PL: Nie chodzi o ptasie skrzydła.\nSkoro jednak Skrzydła przypominają ptaka, który otacza opieką gniazdo, trudno zaprzeczyć pewnemu podobieństwu.\nSkrzydła to 26 megakorporacji, które zarządzają Gniazdami Miasta. Powszechnie uważa się, że każde Skrzydło dzięki zdumiewającej technologii zwanej Osobliwością podnosi jakość życia w całym Mieście i dba o pomyślność swojego Gniazda.\nSprawa wygląda jednak inaczej, gdy Skrzydło zostanie złamane. Od pokoleń dniom, w których łamało się któreś ze Skrzydeł Miasta, towarzyszyły wydarzenia o ogromnej skali.\nW miejscu złamanego Skrzydła prędzej czy później wyrasta nowe. Ale za bezpieczeństwo opustoszałego w tym czasie Gniazda… nikt nie ręczy.
287. [Interfejs i ustawienia [FileDownload_Desc_03] — tytuł] 로보토미 코퍼레이션
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_03].title
   limit: do 40 znaków
   EN: Lobotomy Corporation
   PL: Lobotomy Corporation
288. [Interfejs i ustawienia [FileDownload_Desc_03] — opis] 한 때 날개 중 하나 였던 L 둥지의 회사입니다.\nL사라고도 불렸던 그들은, 대량의 에너지를 생산해 도시의 전력을 담당하는 역할을 하고 있었습니다.\n그러나 백야, 흑주 사건이라고 불리우는 충격적인 사건을 계기로 회사는 몰락해 버렸으며, 지금도 L 둥지의 날개는 여전히 공석인 채 입니다.\n구 L사의 전력망은 도시를 아울렀기 때문에, 이곳저곳에 그들의 지부가 많이 세워져 있습니다. 몰락과 함께 그들도 전부 폐허로 변해버렸지만, 그 안에는 쓸 만한 것들이 남아있을 것입니다.\n어쩌면… 가장 위험한 것들과 함께.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_03].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A former Wing that was located in Nest L.\nLobotomy Corporation, or L Corp. (LC) for short, was an energy company that produced an ample supply of power for the City. The corporation has fallen since the ‘White Nights and Dark Days’ incident, and the spot of Nest L’s Wing remains unclaimed to this day.\nBecause the former L Corp’s electric grids had encompassed the City, its branches were built in various places. Though these branch facilities have all fallen to ruin with the collapse of the Wing, you should still be able to find valuable goods.\nAlong with… possibly the most dangerous beings you’ll face.
   PL: Firma z Gniazda L, niegdyś jedno ze Skrzydeł.\nZnana też jako L Corp., wytwarzała ogromne ilości energii i zaopatrywała Miasto w prąd.\nJednak po wstrząsających wydarzeniach zwanych Białymi Nocami i Ciemnymi Dniami firma upadła, a miejsce Skrzydła Gniazda L wciąż pozostaje puste.\nPonieważ sieć energetyczna dawnego L Corp. obejmowała całe Miasto, jego filie powstały w wielu miejscach. Wraz z upadkiem wszystkie obróciły się w ruiny, ale w środku powinno zostać sporo przydatnych rzeczy.\nByć może… razem z tym, co najgroźniejsze.
289. [Interfejs i ustawienia [FileDownload_Desc_04] — tytuł] 황금가지
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_04].title
   limit: do 40 znaków
   EN: The Golden Boughs
   PL: Złote Gałęzie
290. [Interfejs i ustawienia [FileDownload_Desc_04] — opis] 몰락한 로보토미 코퍼레이션 지부의 지하에는 한 때 그들 기술의 정수였던 황금가지가 있습니다. 황금빛으로 빛나는, 나무의 가지죠.\n관리자께서, 수감자들과 함께 회수해야 할 가장 핵심적인 목표라고 할 수 있습니다.\n황금가지가 갖고 있는 무수한 가능성은 도시의 사람이라면 누구나 탐을 내기 때문에, 편의점에서 물건을 꺼내 오는 것처럼 쉬운 일이 되지는 않을 것입니다.\n현명한 판단을 통해 모든 가지를 회수해 오시기를 요청 드리는 바입니다.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_04].desc
   limit: do 750 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Within the depths of these facilities lie the Golden Boughs, the essence of Lobotomy Corporation’s energy production technology… or what’s left of it. Its appearance is exactly as the name suggests: a tree branch radiating a golden glow.\nYour objective as an Executive Manager is to obtain the Golden Boughs.\nOf course, any denizen of the City would be attracted by the promise of the infinite possibilities these items possess; the task of retrieval will not be as easy as grabbing goods from a convenience store.\nWe implore you to collect all the Golden Boughs with prudent decision-making.
   PL: W podziemiach upadłych filii Lobotomy Corporation spoczywają Złote Gałęzie, niegdyś kwintesencja jej technologii. To gałęzie drzewa lśniące złotym blaskiem.\nMożna powiedzieć, że to najważniejszy cel, który Kierownik ma odzyskać razem z Grzesznikami.\nNieskończone możliwości Złotych Gałęzi kuszą każdego mieszkańca Miasta, więc nie pójdzie to tak łatwo jak zdjęcie czegoś z półki w sklepie.\nUprzejmie prosimy o odzyskanie wszystkich Gałęzi dzięki rozważnym decyzjom.
291. [Interfejs i ustawienia [FileDownload_Desc_05] — tytuł] 환상체
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_05].title
   limit: do 40 znaków
   EN: Abnormalities
   PL: Anomalie
292. [Interfejs i ustawienia [FileDownload_Desc_05] — opis] 로보토미 코퍼레이션은 환상체라고 하는 것들을 이용하여 에너지를 생산했습니다.\n이름 그대로, 그것들은 실존한다고는 믿기지 않는 괴기하고 공포스러운 존재부터, 겉은 멀쩡하지만 잘못 ‘관리’ 했을 때 끔찍한 결말을 초래하는 존재까지 다양한 종류가 그 회사에 있었습니다.\n몰락한 이후, 대부분의 지부는 규정에 따라 (아마 직원은 제대로 알고 있지도 않았을, 극히 세부적인 조항이었겠지요.) 매몰되어 환상체와 직원들이 함께 갇히게 되었습니다.\n시간이 꽤 지났기에, 내부의 직원은 이미 명을 달리 했겠지만, 그것들은 아닙니다. 아직도 그것들은 폐허가 된 지부 내부를 배회하고 있겠지요.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_05].desc
   limit: do 850 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy Corporation used to produce energy using creatures they dubbed ‘Abnormalities’.\nAs the term suggests, these peculiar entities ranged from unfathomably bizarre and terrifying creatures to outwardly unremarkable beings capable of causing potentially catastrophic events as a result of incorrect “management” procedures.\nAfter the Wing’s unexpected and swift collapse, most of the branches were subject to a burial protocol, trapping those creatures underground alongside the likely-oblivious employees.\nBy now, the employees have most likely passed away—but Abnormalities don’t succumb as easily. You can expect them to still prowl the ruins of these sealed facilities.
   PL: Lobotomy Corporation wytwarzała energię, wykorzystując istoty zwane Anomaliami.\nZgodnie z nazwą firma miała ich najróżniejsze rodzaje: od istot tak dziwacznych i przerażających, że trudno uwierzyć w ich istnienie, po takie, które z pozoru wyglądały zwyczajnie, lecz przy niewłaściwym “postępowaniu” z nimi prowadziły do strasznych skutków.\nPo upadku większość filii zgodnie z przepisami (zapewne niezwykle szczegółowymi, o których pracownicy nawet dobrze nie wiedzieli) zasypano, zamykając w nich Anomalie razem z pracownikami.\nMinęło sporo czasu, więc pracownicy w środku zapewne już nie żyją. Ale Anomalie - nie. Wciąż pewnie krążą po zrujnowanych filiach.
293. [Interfejs i ustawienia [FileDownload_Desc_06] — tytuł] E.G.O
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_06].title
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Interfejs i ustawienia [FileDownload_Desc_06] — opis] 로보토미 코퍼레이션은 환상체를 통해 무기와 방어구를 추출하는 기술이 있었다고 전해집니다. 그것들의 내면을 물질화하는 기술로 추정되지만, 아쉽게도 현재는 소실되어 직접적인 방법을 알아낼 수는 없었습니다.\n유관 부서에서는, 수감자들의 활동 방향에 따라 그들 스스로가 E.G.O를 발현할 수 있을 것이라 예측하고 있습니다. 또한, 환상체의 E.G.O 역시 감정적 유착을 매개로 사용하는 것도 가능하리라 여기고 있습니다.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_06].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lobotomy Corporation was said to also have possessed technology allowing them to extract weapons and armor from the Abnormalities. It is speculated to be created using a technology that manifests their inner sides in material form, but unfortunately, we were unable to recover any means to replicate it.\nRelevant departments predict that your Sinners will be able to manifest E.G.O of their own depending on their course of action. In addition, they expect E.G.O from Abnormalities to be available via emotional attachment.
   PL: Podobno Lobotomy Corporation dysponowała technologią pozyskiwania z Anomalii broni i pancerzy. Przypuszcza się, że polegała ona na materializowaniu ich wnętrza, lecz niestety dziś jest utracona i nie zdołaliśmy ustalić, jak dokładnie działała.\nWłaściwe działy przewidują, że zależnie od obranej drogi Grzesznicy będą mogli sami przejawiać E.G.O. Uważają również, że możliwe będzie używanie E.G.O Anomalii za pośrednictwem więzi emocjonalnej.
295. [Interfejs i ustawienia [FileDownload_Desc_07] — tytuł] 엔케팔린
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_07].title
   limit: do 40 znaków
   EN: Enkephalin
   PL: Enkefalina
296. [Interfejs i ustawienia [FileDownload_Desc_07] — opis] 로보토미 코퍼레이션에서 생산하던 에너지를 일컫습니다.\n전력으로서 사용된다고 일반적으로 알려져 있지만, 꼭 그런 형태로만 사용되진 않습니다.\n보통 액체의 상태로 존재하는 이 초록색 물질은, 흡입시 깊은 위안감을 불러일으킨다고 알려져 있습니다. 구 L사에서는 적절한 처방을 통해 과도한 스트레스를 받은 직원에게 투여하여 업무 효율의 상승을 꾀하기도 했다고 합니다.\n하지만, 과용하거나 정제되지 않은 것에 노출될 경우에는…\n좋은 결과가 있지는 않았던 것 같군요.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_07].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This refers to the form of energy Lobotomy Corporation produced.\nWhile commonly known as a source of electricity, this is not the only use for it.\nThis green substance which normally exists in liquid form is known to induce a considerable sense of relaxation. The former L Corp. administered appropriate doses of Enkephalin to its employees suffering under great amounts of stress for increased work efficiency.\nHowever, overdose or exposure to unrefined forms of the substance…\nWell, let’s just say it didn’t seem to end well.
   PL: Tak nazywa się energię wytwarzaną przez Lobotomy Corporation.\nPowszechnie wiadomo, że służy jako źródło prądu, ale nie tylko w tej postaci się jej używa.\nTa zielona substancja, zwykle w stanie ciekłym, podobno przy wdychaniu wywołuje głębokie ukojenie. Dawne L Corp. ponoć podawało ją w odpowiednich dawkach pracownikom pod silnym stresem, by podnieść wydajność ich pracy.\nJednak w razie przedawkowania albo kontaktu z substancją nieoczyszczoną…\nChyba nie kończyło się to dobrze.
297. [Interfejs i ustawienia [FileDownload_Desc_08] — tytuł] 해결사
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_08].title
   limit: do 40 znaków
   EN: Fixers
   PL: Fikserzy
298. [Interfejs i ustawienia [FileDownload_Desc_08] — opis] 도시에서 일어나는 수많은 사건들, 그리고 그 수만큼의 의뢰를 해결하는 것을 업으로 삼는 자들을 해결사라고 부릅니다.\n물론, 자칭하는 것 만으로 해결사가 될 수는 없으며 협회에 인가된 사무소나, 협회에 직접 방문하여 해결사 면허를 취득해야만 합니다.\n면허를 얻는 것으로 끝나는 것이 아닙니다. 그들은 말단부터 높은 등급의 해결사가 되기 위해 실적을 쌓아야만 합니다. (물론, 그런 것에 관심이 없는 자도 있습니다.)\n도시의 문제를 해결하기 위해 존재하고 있지만, 가끔은 그들 스스로가 문제가 되기도 한다는 것은 공공연한 사실이기도 합니다.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_08].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Fixers are the all-around handymen of the City, handling their clients’ various cases and incidents.\nOne doesn’t simply become a Fixer by declaring to be one; in order to acquire a Fixer license officially, one must rap on the door of an Office authorized by the Associations or visit one of the Associations in person.\nFurthermore, the license is only the beginning. To rise through the ranks and earn higher Grades, they must prove themselves through trackable performance. (Of course, some are uninterested in career advancement altogether.)\nWhile Fixers exist to solve the City’s problems, it’s no secret that these Fixers can be sources of problems themselves.
   PL: Fikserami nazywa się tych, którzy zawodowo rozwiązują niezliczone sprawy dziejące się w Mieście i równie liczne zlecenia.\nRzecz jasna, nie zostaje się Fikserem, samemu się tak nazywając: licencję Fiksera trzeba uzyskać w biurze uprawnionym przez Stowarzyszenie albo bezpośrednio w Stowarzyszeniu.\nNa zdobyciu licencji się nie kończy. Aby z najniższego szczebla awansować na wyższy stopień, trzeba gromadzić osiągnięcia. (Oczywiście są i tacy, których to nie interesuje).\nFikserzy istnieją po to, by rozwiązywać problemy Miasta, ale nie jest tajemnicą, że czasem sami stają się problemem.
299. [Interfejs i ustawienia [FileDownload_Desc_09] — tytuł] 협회와 사무소
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_09].title
   limit: do 40 znaków
   EN: The Associations and Offices
   PL: Stowarzyszenia i biura
300. [Interfejs i ustawienia [FileDownload_Desc_09] — opis] 도시에는 모든 해결사를 총괄하는 하나 협회를 주축으로, 해결사를 관리하는 커다란 단체를 협회라고 합니다. 보통 도시에서 일어나는 사건들을 각 협회의 특성에 맞게 배분하고, 협회가 또 다시 해결사에게 일을 분배하는 형태를 가지게 되죠.\n사무소는 해결사들의 모임이라는 점에서 협회와 흡사한 형태인 것 같지만, 그 규모가 작습니다. 어떠한 사무소는 협회에 직속되어 일을 하청 받기도 하고, 또 다른 사무소는 스스로 일을 찾아다니기도 하죠.\n누군가가 ‘사무소는 해결사의 수만큼 존재한다.’고 말한 것처럼, 도시에는 셀 수 없이 많은 사무소가 존재합니다. 금방 생겨났다가, 또 금방 사라지기도 하고요.
   źródło: FileDownloadDesc.json :: dataList[id=FileDownload_Desc_09].desc
   limit: do 1010 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Associations are major organizations that supervise and manage Fixers, and the Hana Association is at the center of all Fixer-related affairs. Cases occurring in the City are handed over to the Associations according to their specialties, and they then distribute those cases to the Fixers that are deemed to be best suited for the job.\nAn Office is similar to an Association in that it’s an organized group of Fixers, but it’s usually far smaller in scale. Some Offices are directly affiliated with an Association that issues tasks to them, while others seek clients and requests on their own. As some aptly put it: “There are as many Offices as there are Fixers.” A great number of Offices exist in the City, seeing constant waves of new entries as well as those sucked up by metaphorical riptides.
   PL: Stowarzyszenia to wielkie organizacje zarządzające Fikserami; ich osią jest Stowarzyszenie Hana, które nadzoruje wszystkich Fikserów. Zwykle sprawy dziejące się w Mieście przydziela się Stowarzyszeniom zgodnie z ich specjalnością, a te z kolei rozdzielają zadania między Fikserów.\nBiuro przypomina Stowarzyszenie o tyle, że też skupia Fikserów, ale działa na mniejszą skalę. Niektóre biura podlegają bezpośrednio Stowarzyszeniu i dostają od niego podzlecenia, inne same szukają pracy.\nJak ktoś kiedyś powiedział: “Biur jest tyle, ilu Fikserów”. W Mieście istnieje niezliczona ilość biur. Szybko powstają i równie szybko znikają.

## Interfejs i ustawienia: Filter
- plik gry: `Filter.json`

301. [Interfejs i ustawienia [filter_title_ego_type] — tekst] 희귀도
   źródło: Filter.json :: dataList[id=filter_title_ego_type].content
   limit: do 120 znaków
   EN: Rarity
   PL:
302. [Interfejs i ustawienia [filter_title_ego_level] — tekst] 강화 단계
   źródło: Filter.json :: dataList[id=filter_title_ego_level].content
   limit: do 120 znaków
   EN: Level
   PL:
303. [Interfejs i ustawienia [number_of_targets] — tekst] 대상 수
   źródło: Filter.json :: dataList[id=number_of_targets].content
   limit: do 120 znaków
   EN: Targets
   PL:
304. [Interfejs i ustawienia [SINGLE_TARGET] — tekst] 단일
   źródło: Filter.json :: dataList[id=SINGLE_TARGET].content
   limit: do 120 znaków
   EN: Single
   PL:
305. [Interfejs i ustawienia [MULTIPLE_TARGET] — tekst] 광역
   źródło: Filter.json :: dataList[id=MULTIPLE_TARGET].content
   limit: do 120 znaków
   EN: Area
   PL:
306. [Interfejs i ustawienia [filter_title_attribute] — tekst] 속성
   źródło: Filter.json :: dataList[id=filter_title_attribute].content
   limit: do 120 znaków
   EN: Affinity
   PL:
307. [Interfejs i ustawienia [filter_awaken_state] — tekst] 동기화 단계
   źródło: Filter.json :: dataList[id=filter_awaken_state].content
   limit: do 120 znaków
   EN: Uptie Tier
   PL:
308. [Interfejs i ustawienia [filter_normal] — tekst] 1,2단계
   źródło: Filter.json :: dataList[id=filter_normal].content
   limit: do 120 znaków
   EN: Tier 1/2
   PL:
309. [Interfejs i ustawienia [filter_awaken] — tekst] 3단계
   źródło: Filter.json :: dataList[id=filter_awaken].content
   limit: do 120 znaków
   EN: Tier 3
   PL:
310. [Interfejs i ustawienia [filter_skill_keyword] — tekst] 스킬 키워드
   źródło: Filter.json :: dataList[id=filter_skill_keyword].content
   limit: do 120 znaków
   EN: Keyword
   PL:
311. [Interfejs i ustawienia [sorting_acqisition] — tekst] 획득 순
   źródło: Filter.json :: dataList[id=sorting_acqisition].content
   limit: do 120 znaków
   EN: Recent
   PL:
312. [Interfejs i ustawienia [filter_title_ego_gacksung] — tekst] 환상 해석 단계
   źródło: Filter.json :: dataList[id=filter_title_ego_gacksung].content
   limit: do 120 znaków
   EN: Threadspun Tier
   PL:

## Interfejs i ustawienia: FormationNameEtcFilter
- plik gry: `FormationNameEtcFilter.json`

313. [Interfejs i ustawienia [formation_name_filter_Etc_title] — tekst] 기타
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_title].content
   limit: do 120 znaków
   EN: Other
   PL:
314. [Interfejs i ustawienia [formation_name_filter_Etc_LIMBUS_COMPANY] — tekst] 림버스 컴퍼니
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LIMBUS_COMPANY].content
   limit: do 120 znaków
   EN: Limbus Company
   PL:
315. [Interfejs i ustawienia [formation_name_filter_Etc_L_CORP] — tekst] 로보토미 본사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_L_CORP].content
   limit: do 120 znaków
   EN: Lobotomy Corp. HQ
   PL:
316. [Interfejs i ustawienia [formation_name_filter_Etc_H_CORP] — tekst] H사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_H_CORP].content
   limit: do 120 znaków
   EN: H Corp.
   PL:
317. [Interfejs i ustawienia [formation_name_filter_Etc_N_CORP] — tekst] N사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_N_CORP].content
   limit: do 120 znaków
   EN: N Corp.
   PL:
318. [Interfejs i ustawienia [formation_name_filter_Etc_R_CORP] — tekst] R사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_R_CORP].content
   limit: do 120 znaków
   EN: R Corp.
   PL:
319. [Interfejs i ustawienia [formation_name_filter_Etc_T_CORP] — tekst] T사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_T_CORP].content
   limit: do 120 znaków
   EN: T Corp.
   PL:
320. [Interfejs i ustawienia [formation_name_filter_Etc_W_CORP] — tekst] W사
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_W_CORP].content
   limit: do 120 znaków
   EN: W Corp.
   PL:
321. [Interfejs i ustawienia [formation_name_filter_Etc_ZWEI] — tekst] 츠바이
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_ZWEI].content
   limit: do 120 znaków
   EN: Zwei
   PL:
322. [Interfejs i ustawienia [formation_name_filter_Etc_SHI] — tekst] 시
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_SHI].content
   limit: do 120 znaków
   EN: Shi
   PL:
323. [Interfejs i ustawienia [formation_name_filter_Etc_CINQ] — tekst] 섕크
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_CINQ].content
   limit: do 120 znaków
   EN: Cinq
   PL:
324. [Interfejs i ustawienia [formation_name_filter_Etc_LIU] — tekst] 리우
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LIU].content
   limit: do 120 znaków
   EN: Liu
   PL:
325. [Interfejs i ustawienia [formation_name_filter_Etc_SEVEN] — tekst] 세븐
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_SEVEN].content
   limit: do 120 znaków
   EN: Seven
   PL:
326. [Interfejs i ustawienia [formation_name_filter_Etc_DEVYAT] — tekst] 제뱌찌
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_DEVYAT].content
   limit: do 120 znaków
   EN: Devyat'
   PL:
327. [Interfejs i ustawienia [formation_name_filter_Etc_DIECI] — tekst] 디에치
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_DIECI].content
   limit: do 120 znaków
   EN: Dieci
   PL:
328. [Interfejs i ustawienia [formation_name_filter_Etc_OUFI] — tekst] 외우피
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_OUFI].content
   limit: do 120 znaków
   EN: Öufi
   PL:
329. [Interfejs i ustawienia [formation_name_filter_Etc_BLADE_LINEAGE] — tekst] 검계
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_BLADE_LINEAGE].content
   (powtórzenie elementu 1 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Interfejs i ustawienia [formation_name_filter_Etc_BLACK_CLOUD] — tekst] 흑운회
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_BLACK_CLOUD].content
   (powtórzenie elementu 2 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Interfejs i ustawienia [formation_name_filter_Etc_ATL] — tekst] 기술 해방 연합
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_ATL].content
   limit: do 120 znaków
   EN: Technology Liberation Alliance
   PL:
332. [Interfejs i ustawienia [formation_name_filter_Etc_WUTHERING_HEIGHTS] — tekst] 워더링 하이츠
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_WUTHERING_HEIGHTS].content
   limit: do 120 znaków
   EN: Wuthering Heights
   PL:
333. [Interfejs i ustawienia [formation_name_filter_Etc_PEQUOD_CREW] — tekst] 피쿼드호
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_PEQUOD_CREW].content
   limit: do 120 znaków
   EN: The Pequod
   PL:
334. [Interfejs i ustawienia [formation_name_filter_Etc_BLOODFIEND] — tekst] 혈귀
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_BLOODFIEND].content
   limit: do 120 znaków
   EN: Bloodfiend
   PL:
335. [Interfejs i ustawienia [formation_name_filter_Etc_BLACK_BEAST] — tekst] 흑수
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_BLACK_BEAST].content
   limit: do 120 znaków
   EN: Heishou
   PL:
336. [Interfejs i ustawienia [formation_name_filter_Etc_FINGER] — tekst] 손가락
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_FINGER].content
   limit: do 120 znaków
   EN: The Fingers
   PL:
337. [Interfejs i ustawienia [formation_name_filter_Etc_THUMB_FINGER] — tekst] 엄지
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_THUMB_FINGER].content
   limit: do 120 znaków
   EN: The Thumb
   PL:
338. [Interfejs i ustawienia [formation_name_filter_Etc_INDEX_FINGER] — tekst] 검지
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_INDEX_FINGER].content
   limit: do 120 znaków
   EN: The Index
   PL:
339. [Interfejs i ustawienia [formation_name_filter_Etc_MIDDLE_FINGER] — tekst] 중지
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_MIDDLE_FINGER].content
   limit: do 120 znaków
   EN: The Middle
   PL:
340. [Interfejs i ustawienia [formation_name_filter_Etc_RING_FINGER] — tekst] 약지
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_RING_FINGER].content
   limit: do 120 znaków
   EN: The Ring
   PL:
341. [Interfejs i ustawienia [formation_name_filter_Etc_LITTLE_FINGER] — tekst] 소지
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LITTLE_FINGER].content
   limit: do 120 znaków
   EN: The Pinky
   PL:
342. [Interfejs i ustawienia [formation_name_filter_Etc_SPIDER_HOUSE] — tekst] 거미집
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_SPIDER_HOUSE].content
   limit: do 120 znaków
   EN: The House of Spiders
   PL:
343. [Interfejs i ustawienia [formation_name_filter_Etc_LIMBUS_COMPANY_LCE] — tekst] LCE
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LIMBUS_COMPANY_LCE].content
   limit: do 120 znaków
   EN: LCE
   PL:
344. [Interfejs i ustawienia [formation_name_filter_Etc_EGO_EQUIPMENT] — tekst] E.G.O 장비
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_EGO_EQUIPMENT].content
   limit: do 120 znaków
   EN: E.G.O Gear
   PL:
345. [Interfejs i ustawienia [formation_name_filter_Etc_BULLET] — tekst] 탄환
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_BULLET].content
   limit: do 120 znaków
   EN: Ammo
   PL:
346. [Interfejs i ustawienia [formation_name_filter_Etc_DISCARD_SKILL] — tekst] 버림
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_DISCARD_SKILL].content
   limit: do 120 znaków
   EN: Discard
   PL:
347. [Interfejs i ustawienia [formation_name_filter_Etc_SISYPHE] — tekst] 시지프
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_SISYPHE].content
   limit: do 120 znaków
   EN: Sisyphe
   PL:
348. [Interfejs i ustawienia [formation_name_filter_Etc_LE_ROUGE] — tekst] 르루주
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LE_ROUGE].content
   limit: do 120 znaków
   EN: Le Rouge
   PL:
349. [Interfejs i ustawienia [formation_name_filter_Etc_LE_NOIR] — tekst] 르누아르
   źródło: FormationNameEtcFilter.json :: dataList[id=formation_name_filter_Etc_LE_NOIR].content
   limit: do 120 znaków
   EN: Le Noir
   PL:

## Interfejs i ustawienia: FormationNameFilterUI
- plik gry: `FormationNameFilterUI.json`

350. [Interfejs i ustawienia [change_formation_name_title] — tekst] 편성명 수정
   źródło: FormationNameFilterUI.json :: dataList[id=change_formation_name_title].content
   limit: do 120 znaków
   EN: Edit Team Name
   PL:
351. [Interfejs i ustawienia [formation_name_filter_contents_title] — tekst] 콘텐츠
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_title].content
   limit: do 120 znaków
   EN: Contents
   PL:
352. [Interfejs i ustawienia [formation_name_filter_contents_story] — tekst] 스토리
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_story].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Interfejs i ustawienia [formation_name_filter_contents_mirrordungeon] — tekst] 거울 던전
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_mirrordungeon].content
   limit: do 120 znaków
   EN: Mirror Dun.
   PL:
354. [Interfejs i ustawienia [formation_name_filter_contents_railwaydungeon] — tekst] 거울 굴절 철도
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_railwaydungeon].content
   limit: do 120 znaków
   EN: Railway
   PL:
355. [Interfejs i ustawienia [formation_name_filter_contents_exp_mining] — tekst] 경험치 채광
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_exp_mining].content
   limit: do 120 znaków
   EN: EXP Lux.
   PL:
356. [Interfejs i ustawienia [formation_name_filter_contents_thread_mining] — tekst] 끈 채광
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_thread_mining].content
   limit: do 120 znaków
   EN: Thread Lux.
   PL:
357. [Interfejs i ustawienia [formation_name_filter_contents_practice] — tekst] 연습
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_practice].content
   limit: do 120 znaków
   EN: Testing
   PL:
358. [Interfejs i ustawienia [formation_name_total_tag_count_limitation] — tekst] ※ 최대 10개의 태그를 선택 가능합니다.
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_total_tag_count_limitation].content
   limit: do 120 znaków
   EN: ※ Up to 10 tags can be selected.
   PL:
359. [Interfejs i ustawienia [formation_name_filter_contents_raid] — tekst] 사영전투
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_raid].content
   limit: do 120 znaków
   EN: Reflectrial
   PL:
360. [Interfejs i ustawienia [formation_name_filter_contents_walpurgisnacht] — tekst] 발푸르기스의 밤
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_walpurgisnacht].content
   limit: do 120 znaków
   EN: Walp. Night
   PL:
361. [Interfejs i ustawienia [formation_name_filter_contents_event] — tekst] 이벤트
   źródło: FormationNameFilterUI.json :: dataList[id=formation_name_filter_contents_event].content
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Interfejs i ustawienia: FormationUI_S6
- plik gry: `FormationUI_S6.json`

362. [Interfejs i ustawienia [formation_ego_resource_detail] — tekst] 상세
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_detail].content
   limit: do 120 znaków
   EN: Details
   PL:
363. [Interfejs i ustawienia [formation_deck_code_auto_filled] — tekst] 보유하지 않은 인격과 E.G.O는 기본 인격, E.G.O로 적용되었습니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_deck_code_auto_filled].content
   limit: do 130 znaków
   EN: Base Identities & E.G.O have been slotted in for Identities or E.G.O that you have not obtained yet.
   PL:
364. [Interfejs i ustawienia [formation_deck_filled_complete] — tekst] 편성 코드 불러오기 완료
   źródło: FormationUI_S6.json :: dataList[id=formation_deck_filled_complete].content
   limit: do 120 znaków
   EN: Team Code Loading Complete
   PL:
365. [Interfejs i ustawienia [formation_set_to_default] — tekst] 편성을 초기화하시겠습니까?\n\n<size=80%>초기화 시 기본 인격, 기본 E.G.O 장착 상태로 돌아갑니다.</size>
   źródło: FormationUI_S6.json :: dataList[id=formation_set_to_default].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <size=80%>, </size>, \n
   EN: Reset this Team loadout?\n\n<size=80%>Resetting this Team loadout will unequip everything save for Base Identities and Base E.G.O.</size>
   PL:
366. [Interfejs i ustawienia [formation_unable_to_set_default] — tekst] 기본 편성은 초기화 할 수 없습니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_unable_to_set_default].content
   limit: do 120 znaków
   EN: You cannot reset the Base loadout.
   PL:
367. [Interfejs i ustawienia [formation_ego_resource_popup_title] — tekst] E.G.O 자원 상세
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_title].content
   limit: do 120 znaków
   EN: Team E.G.O Resource Overview
   PL:
368. [Interfejs i ustawienia [formation_ego_resource_popup_total_used] — tekst] 총 E.G.O 소모 자원 개수
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_total_used].content
   limit: do 120 znaków
   EN: E.G.O Resource Expenditure Overview:
   PL:
369. [Interfejs i ustawienia [formation_ego_resource_popup_total_acquirable] — tekst] 총 E.G.O 자원 개수
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_total_acquirable].content
   limit: do 120 znaków
   EN: Obtainable E.G.O Resources Overview:
   PL:
370. [Interfejs i ustawienia [formation_ego_resource_popup_personality] — tekst] 인격 자원 정보
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_personality].content
   limit: do 120 znaków
   EN: Identity Resources
   PL:
371. [Interfejs i ustawienia [formation_ego_resource_popup_ego] — tekst] E.G.O 소모 자원
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_ego].content
   limit: do 120 znaków
   EN: E.G.O Resource Expenditure
   PL:
372. [Interfejs i ustawienia [formation_code_popup_title] — tekst] 편성 코드
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_title].content
   limit: do 120 znaków
   EN: Team Code
   PL:
373. [Interfejs i ustawienia [formation_code_popup_desc] — tekst] 편성 코드를 복사하여\n공유하거나 불러올 수 있습니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: With Team Codes, you can:\n- Copy and share your Team loadouts\n- Paste and load Team loadouts
   PL:
374. [Interfejs i ustawienia [formation_code_popup_copy] — tekst] 편성 코드 복사
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_copy].content
   limit: do 120 znaków
   EN: Copy Team Code
   PL:
375. [Interfejs i ustawienia [formation_code_popup_paste] — tekst] 편성 코드 불러오기
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_paste].content
   limit: do 120 znaków
   EN: Load Team Code
   PL:
376. [Interfejs i ustawienia [formation_code_popup_paste_desc] — tekst] 복사한 편성 코드를 입력하여\n새로운 편성을 생성합니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_paste_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Paste the copied Team Code here to equip the Team loadout.
   PL:
377. [Interfejs i ustawienia [formation_code_popup_paste_input] — tekst] 코드 입력
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_paste_input].content
   limit: do 120 znaków
   EN: Enter Code
   PL:
378. [Interfejs i ustawienia [formation_code_popup_copy_success] — tekst] 편성 코드 복사 완료
   źródło: FormationUI_S6.json :: dataList[id=formation_code_popup_copy_success].content
   limit: do 120 znaków
   EN: Team Code Copied
   PL:
379. [Interfejs i ustawienia [formation_side_button_all_personality] — tekst] 모든 인격
   źródło: FormationUI_S6.json :: dataList[id=formation_side_button_all_personality].content
   limit: do 120 znaków
   EN: All Identities
   PL:
380. [Interfejs i ustawienia [formation_side_button_all_ego] — tekst] 모든 E.G.O
   źródło: FormationUI_S6.json :: dataList[id=formation_side_button_all_ego].content
   limit: do 120 znaków
   EN: All E.G.O
   PL:
381. [Interfejs i ustawienia [formation_side_button_friend_support] — tekst] 지원
   źródło: FormationUI_S6.json :: dataList[id=formation_side_button_friend_support].content
   limit: do 120 znaków
   EN: Support
   PL:
382. [Interfejs i ustawienia [character_list_title_all_personality] — tekst] 인격
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_personality].content
   limit: do 120 znaków
   EN: Identities
   PL:
383. [Interfejs i ustawienia [character_list_title_all_personality_with_character_name] — tekst] 인격 : {0}
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_personality_with_character_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Identities: {0}
   PL:
384. [Interfejs i ustawienia [character_list_title_all_ego] — tekst] E.G.O
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_ego].content
   (powtórzenie elementu 59 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Interfejs i ustawienia [character_list_title_all_ego_with_character_name] — tekst] E.G.O : {0}
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_ego_with_character_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O: {0}
   PL:
386. [Interfejs i ustawienia [character_list_title_friend_support] — tekst] 지원 인격 : {0}
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_friend_support].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Support Identities: {0}
   PL:
387. [Interfejs i ustawienia [character_list_collect_rate] — tekst] 수집률
   źródło: FormationUI_S6.json :: dataList[id=character_list_collect_rate].content
   limit: do 120 znaków
   EN: Collection Rate
   PL:
388. [Interfejs i ustawienia [character_list_owned_toggle_label] — tekst] 보유
   źródło: FormationUI_S6.json :: dataList[id=character_list_owned_toggle_label].content
   limit: do 120 znaków
   EN: Obtained
   PL:
389. [Interfejs i ustawienia [character_list_sort_label] — tekst] 정렬
   źródło: FormationUI_S6.json :: dataList[id=character_list_sort_label].content
   limit: do 120 znaków
   EN: Sort By
   PL:
390. [Interfejs i ustawienia [character_list_friend_support_not_existed] — tekst] 해당 수감자에 대한 지원 인격이 없습니다.
   źródło: FormationUI_S6.json :: dataList[id=character_list_friend_support_not_existed].content
   limit: do 120 znaków
   EN: No Support Identities for this Sinner.
   PL:
391. [Interfejs i ustawienia [character_list_friend_support_impossible] — tekst] 해당 수감자의 지원 인격을 지정할 수 없습니다.
   źródło: FormationUI_S6.json :: dataList[id=character_list_friend_support_impossible].content
   limit: do 120 znaków
   EN: Cannot equip Support Identities for this Sinner.
   PL:
392. [Interfejs i ustawienia [view_personality_status_button_label] — tekst] 인격
   źródło: FormationUI_S6.json :: dataList[id=view_personality_status_button_label].content
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Interfejs i ustawienia [formation_ui_announcer] — tekst] 아나운서
   źródło: FormationUI_S6.json :: dataList[id=formation_ui_announcer].content
   limit: do 120 znaków
   EN: Announcers
   PL:
394. [Interfejs i ustawienia [formation_ui_announcer_detail] — tekst] 아나운서 상세
   źródło: FormationUI_S6.json :: dataList[id=formation_ui_announcer_detail].content
   limit: do 120 znaków
   EN: Announcer Details
   PL:
395. [Interfejs i ustawienia [formation_deck_code_invalid_code] — tekst] 유효하지 않은 편성 코드 입니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_deck_code_invalid_code].content
   limit: do 120 znaków
   EN: This Team Code is invalid.
   PL:
396. [Interfejs i ustawienia [formation_ego_resource_popup_personality_desc] — tekst] 현재 편성된 인격들로 모을 수 있는 총 E.G.O 자원 개수와 편성된 각 인격들이 모을 수 있는 E.G.O 자원의 수량입니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_personality_desc].content
   limit: do 130 znaków
   EN: Overview of E.G.O Resources obtainable by Identities in your Team loadout & per-Identity overview.
   PL:
397. [Interfejs i ustawienia [formation_ego_resource_popup_ego_desc] — tekst] 현재 장착된 E.G.O가 소모하는 자원의 수량입니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_ego_resource_popup_ego_desc].content
   limit: do 120 znaków
   EN: E.G.O Resources expenditure for each equipped E.G.O.
   PL:
398. [Interfejs i ustawienia [formation_current_personality] — tekst] 현재 선택 인격
   źródło: FormationUI_S6.json :: dataList[id=formation_current_personality].content
   limit: do 120 znaków
   EN: Selected Identity
   PL:
399. [Interfejs i ustawienia [ego_sort_label_rarity] — tekst] 희귀도
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_rarity].content
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Interfejs i ustawienia [ego_filter_label_attack_type] — tekst] E.G.O 유형
   źródło: FormationUI_S6.json :: dataList[id=ego_filter_label_attack_type].content
   limit: do 120 znaków
   EN: E.G.O Attack Type
   PL:
401. [Interfejs i ustawienia [ego_filter_label_attribute_type] — tekst] E.G.O 속성
   źródło: FormationUI_S6.json :: dataList[id=ego_filter_label_attribute_type].content
   limit: do 120 znaków
   EN: E.G.O Affinity
   PL:
402. [Interfejs i ustawienia [personality_filter_label_attack_type] — tekst] 스킬 유형
   źródło: FormationUI_S6.json :: dataList[id=personality_filter_label_attack_type].content
   limit: do 120 znaków
   EN: Skill Attack Type
   PL:
403. [Interfejs i ustawienia [personality_filter_label_attribute_type] — tekst] 스킬 속성
   źródło: FormationUI_S6.json :: dataList[id=personality_filter_label_attribute_type].content
   limit: do 120 znaków
   EN: Skill Affinity
   PL:
404. [Interfejs i ustawienia [character_list_personality_not_existed] — tekst] 해당하는 인격이 없습니다.
   źródło: FormationUI_S6.json :: dataList[id=character_list_personality_not_existed].content
   limit: do 120 znaków
   EN: No identities matched your filter settings.
   PL:
405. [Interfejs i ustawienia [character_list_ego_not_existed] — tekst] 해당하는 E.G.O가 없습니다
   źródło: FormationUI_S6.json :: dataList[id=character_list_ego_not_existed].content
   limit: do 120 znaków
   EN: No E.G.O matched your filter settings.
   PL:
406. [Interfejs i ustawienia [filter_condition_speed] — tekst] 속도
   źródło: FormationUI_S6.json :: dataList[id=filter_condition_speed].content
   limit: do 120 znaków
   EN: Speed
   PL:
407. [Interfejs i ustawienia [filter_condition_defense] — tekst] 방어 레벨
   źródło: FormationUI_S6.json :: dataList[id=filter_condition_defense].content
   limit: do 120 znaków
   EN: Def. Lv.
   PL:
408. [Interfejs i ustawienia [filter_condition_grade] — tekst] {0}단계
   źródło: FormationUI_S6.json :: dataList[id=filter_condition_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Tier {0}
   PL:
409. [Interfejs i ustawienia [ego_sort_label_syncLevel] — tekst] 환상 해석
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_syncLevel].content
   limit: do 120 znaków
   EN: T.Spinning
   PL:
410. [Interfejs i ustawienia [ego_sort_label_crimson_resist] — tekst] 분노 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_crimson_resist].content
   limit: do 120 znaków
   EN: Wrath Res.
   PL:
411. [Interfejs i ustawienia [ego_sort_label_scarlet_resist] — tekst] 색욕 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_scarlet_resist].content
   limit: do 120 znaków
   EN: Lust Res.
   PL:
412. [Interfejs i ustawienia [ego_sort_label_amber_resist] — tekst] 나태 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_amber_resist].content
   limit: do 120 znaków
   EN: Sloth Res.
   PL:
413. [Interfejs i ustawienia [ego_sort_label_shamrock_resist] — tekst] 탐식 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_shamrock_resist].content
   limit: do 120 znaków
   EN: Glut. Res.
   PL:
414. [Interfejs i ustawienia [ego_sort_label_azure_resist] — tekst] 우울 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_azure_resist].content
   limit: do 120 znaków
   EN: Gloom Res.
   PL:
415. [Interfejs i ustawienia [ego_sort_label_indigo_resist] — tekst] 오만 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_indigo_resist].content
   limit: do 120 znaków
   EN: Pride Res.
   PL:
416. [Interfejs i ustawienia [ego_sort_label_violet_resist] — tekst] 질투 내성
   źródło: FormationUI_S6.json :: dataList[id=ego_sort_label_violet_resist].content
   limit: do 120 znaków
   EN: Envy Res.
   PL:
417. [Interfejs i ustawienia [personality_info_list_not_owned] — tekst] 미획득
   źródło: FormationUI_S6.json :: dataList[id=personality_info_list_not_owned].content
   limit: do 120 znaków
   EN: Not Owned
   PL:
418. [Interfejs i ustawienia [formation_must_participate_specific_character_with_baton] — tekst] {0} 수감자가 대기 인원에 포함되지 않은 채로 전투에 참여해야 합니다.
   źródło: FormationUI_S6.json :: dataList[id=formation_must_participate_specific_character_with_baton].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} cannot enter as a Backup unit. {0} must be an active participant in the battle.
   PL:
419. [Interfejs i ustawienia [character_list_skin_not_existed] — tekst] 해당하는 외형이 없습니다
   źródło: FormationUI_S6.json :: dataList[id=character_list_skin_not_existed].content
   limit: do 120 znaków
   EN: No Façade matched your filter settings
   PL:
420. [Interfejs i ustawienia [character_list_title_all_skin] — tekst] 외형 투영
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_skin].content
   limit: do 120 znaków
   EN: Façades
   PL:
421. [Interfejs i ustawienia [character_list_title_all_skin_with_character_name] — tekst] 외형 투영 : {0}
   źródło: FormationUI_S6.json :: dataList[id=character_list_title_all_skin_with_character_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Façade Projection : {0}
   PL:
422. [Interfejs i ustawienia [mainui_common_skin] — tekst] 외형 투영
   źródło: FormationUI_S6.json :: dataList[id=mainui_common_skin].content
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Interfejs i ustawienia [formation_side_button_skin] — tekst] 외형 투영
   źródło: FormationUI_S6.json :: dataList[id=formation_side_button_skin].content
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Interfejs i ustawienia: IntegrateAccountUI
- plik gry: `IntegrateAccountUI.json`

424. [Interfejs i ustawienia [receive_integrate_account_code] — tekst] 연동 코드 발급
   źródło: IntegrateAccountUI.json :: dataList[id=receive_integrate_account_code].content
   limit: do 120 znaków
   EN: Send Merge Code
   PL:
425. [Interfejs i ustawienia [receive_integrate_account_code_description] — tekst] 발급된 계정 연동 코드를 시간 내에 연동해주시기 바랍니다.
   źródło: IntegrateAccountUI.json :: dataList[id=receive_integrate_account_code_description].content
   limit: do 120 znaków
   EN: After receiving your code, please make sure to complete the process before it expires.
   PL:
426. [Interfejs i ustawienia [request_integrate_account_code] — tekst] 발급 신청
   źródło: IntegrateAccountUI.json :: dataList[id=request_integrate_account_code].content
   limit: do 120 znaków
   EN: Request Code
   PL:
427. [Interfejs i ustawienia [input_integrate_account_code] — tekst] 연동 코드 입력
   źródło: IntegrateAccountUI.json :: dataList[id=input_integrate_account_code].content
   limit: do 120 znaków
   EN: Merge Code Input
   PL:
428. [Interfejs i ustawienia [input_code] — tekst] 코드 입력
   źródło: IntegrateAccountUI.json :: dataList[id=input_code].content
   (powtórzenie elementu 377 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Interfejs i ustawienia [integrate_account_code] — tekst] 계정 연동 코드
   źródło: IntegrateAccountUI.json :: dataList[id=integrate_account_code].content
   limit: do 120 znaków
   EN: Account Merger Code
   PL:
430. [Interfejs i ustawienia [input_integrate_account_code_description] — tekst] UID와 발급된 코드를 입력하세요
   źródło: IntegrateAccountUI.json :: dataList[id=input_integrate_account_code_description].content
   limit: do 120 znaków
   EN: Please enter your UID and the provided code.
   PL:
431. [Interfejs i ustawienia [unable_to_integrate_account] — tekst] 연동을 진행할 수 없습니다.
   źródło: IntegrateAccountUI.json :: dataList[id=unable_to_integrate_account].content
   limit: do 120 znaków
   EN: Could not merge account.
   PL:
432. [Interfejs i ustawienia [not_exist_integrate_code] — tekst] 연동 코드가 존재하지 않습니다.
   źródło: IntegrateAccountUI.json :: dataList[id=not_exist_integrate_code].content
   limit: do 120 znaków
   EN: The merge code does not exist.
   PL:
433. [Interfejs i ustawienia [select_account_for_integrate] — tekst] 연동할 계정을 선택하세요.
   źródło: IntegrateAccountUI.json :: dataList[id=select_account_for_integrate].content
   limit: do 120 znaków
   EN: Please select an account to merge.
   PL:
434. [Interfejs i ustawienia [current_account] — tekst] 현재 계정
   źródło: IntegrateAccountUI.json :: dataList[id=current_account].content
   limit: do 120 znaków
   EN: Current Account
   PL:
435. [Interfejs i ustawienia [new_account] — tekst] 새로운 계정
   źródło: IntegrateAccountUI.json :: dataList[id=new_account].content
   limit: do 120 znaków
   EN: New Account
   PL:
436. [Interfejs i ustawienia [warning_none_integrate_account_removed] — tekst] ※ 선택되지 않은 계정은 삭제됩니다.
   źródło: IntegrateAccountUI.json :: dataList[id=warning_none_integrate_account_removed].content
   limit: do 120 znaków
   EN: ※ The unselected account will be deleted.
   PL:
437. [Interfejs i ustawienia [ask_to_integrate_account] — tekst] 선택한 계정으로 연동을 진행하시겠습니까?
   źródło: IntegrateAccountUI.json :: dataList[id=ask_to_integrate_account].content
   limit: do 120 znaków
   EN: Merge data to the selected account?
   PL:
438. [Interfejs i ustawienia [ask_to_integrate_account_warning] — tekst] 선택한 계정으로 연동을 진행하시겠습니까?
   źródło: IntegrateAccountUI.json :: dataList[id=ask_to_integrate_account_warning].content
   (powtórzenie elementu 437 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Interfejs i ustawienia [receiving_integrate_account_code] — tekst] 발급 중
   źródło: IntegrateAccountUI.json :: dataList[id=receiving_integrate_account_code].content
   limit: do 120 znaków
   EN: Sending code…
   PL:
440. [Interfejs i ustawienia [success_integrate_account_message] — tekst] 계정 연동이 정상적으로 처리되었습니다.
   źródło: IntegrateAccountUI.json :: dataList[id=success_integrate_account_message].content
   limit: do 120 znaków
   EN: Account data merged successfully.
   PL:
441. [Interfejs i ustawienia [warning_before_integrate] — tekst] <color=red>선택되지 않은 계정은 삭제됩니다.</color>
   źródło: IntegrateAccountUI.json :: dataList[id=warning_before_integrate].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=red>, </color>
   EN: <color=red>The unselected account will be deleted.</color>
   PL:
442. [Interfejs i ustawienia [link_error_link_failed] — tekst] 연동 불가
   źródło: IntegrateAccountUI.json :: dataList[id=link_error_link_failed].content
   limit: do 120 znaków
   EN: Cannot Merge
   PL:
443. [Interfejs i ustawienia [link_error_expired] — tekst] 연동 코드가 만료되었습니다.
   źródło: IntegrateAccountUI.json :: dataList[id=link_error_expired].content
   limit: do 120 znaków
   EN: The merge code has expired.
   PL:
444. [Interfejs i ustawienia [link_error] — tekst] 연동에 실패하였습니다.\n게스트 계정이거나 동일한 플랫폼의 계정에 연동을 시도할 경우, 연동이 불가능합니다.
   źródło: IntegrateAccountUI.json :: dataList[id=link_error].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed to integrate account data.\nYou cannot merge data with an account of the same platform or a guest account.
   PL:
445. [Interfejs i ustawienia [input_unlink_account] — tekst] 연동 해제
   źródło: IntegrateAccountUI.json :: dataList[id=input_unlink_account].content
   limit: do 120 znaków
   EN: Unlink Accounts
   PL:
446. [Interfejs i ustawienia [alarm_unlink_account] — tekst] 연동 해제 완료
   źródło: IntegrateAccountUI.json :: dataList[id=alarm_unlink_account].content
   limit: do 120 znaków
   EN: Account Unlinked
   PL:
447. [Interfejs i ustawienia [unlink_account_ask_title] — tekst] 연동 해제
   źródło: IntegrateAccountUI.json :: dataList[id=unlink_account_ask_title].content
   (powtórzenie elementu 445 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Interfejs i ustawienia [unlink_account_ask_content] — tekst] 해당 계정들의 연동을 해제합니다.\n연동 해제 시, {0}일간 해제가 불가능합니다.
   źródło: IntegrateAccountUI.json :: dataList[id=unlink_account_ask_content].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Unlink the following Accounts.\nOnce you unlink, you will not be able to unlink again for {0} days.
   PL:

## Interfejs i ustawienia: Limbus3rdAnniversary
- plik gry: `Limbus3rdAnniversary.json`

449. [Interfejs i ustawienia [anniversary_3rd_day_1_date] — tekst] 1일차
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_day_1_date].content
   limit: do 120 znaków
   EN: Day 1
   PL:
450. [Interfejs i ustawienia [anniversary_3rd_day_1_reward] — tekst] <size=70%>림버스 컴퍼니 3주년 기념 배너</size>\n시즌 1 인격 선택권
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_day_1_reward].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <size=70%>, </size>, \n
   EN: <size=60%>Limbus Company 3rd Anniv. Banner</size>\n<size=90%>Nominable S1 Identity Ticket</size>
   PL:
451. [Interfejs i ustawienia [anniversary_3rd_day_7_date] — tekst] 7일차
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_day_7_date].content
   limit: do 120 znaków
   EN: Day 7
   PL:
452. [Interfejs i ustawienia [anniversary_3rd_day_7_reward] — tekst] 3rd Anniversary
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_day_7_reward].content
   limit: do 120 znaków
   EN: 3rd Anniversary
   PL:
453. [Interfejs i ustawienia [anniversary_3rd_last_day_reward] — tekst] 3주년 기념 인격 선택권\n앤젤라 (도서관 관장-초기) 아나운서\n림버스 컴퍼니 3주년 기념 특별 배너\n3rd Anniversary (Special)
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_last_day_reward].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 3rd Anniversary Nominable Identity Ticket\nAngela (Library Director - Early Days) Announcer\nLimbus Company 3rd Anniversary Special Banner\n3rd Anniversary (Special)
   PL:
454. [Interfejs i ustawienia [anniversary_3rd_last_day_reward_desc] — tekst] 이미 보유한 아나운서를 중복하여 획득하는 경우에는 끈 상자 50개로 전환되어 획득하게 됩니다.
   źródło: Limbus3rdAnniversary.json :: dataList[id=anniversary_3rd_last_day_reward_desc].content
   limit: do 120 znaków
   EN: Obtaining a duplicate of an Announcer you already have will yield 50 Thread Crates instead.
   PL:
455. [Interfejs i ustawienia [select_identity_popup_title_season_2] — tekst] 시즌 2 인격 선택
   źródło: Limbus3rdAnniversary.json :: dataList[id=select_identity_popup_title_season_2].content
   limit: do 120 znaków
   EN: Select Season 2 Identity
   PL:
456. [Interfejs i ustawienia [select_identity_popup_title_season_3] — tekst] 시즌 3 인격 선택
   źródło: Limbus3rdAnniversary.json :: dataList[id=select_identity_popup_title_season_3].content
   limit: do 120 znaków
   EN: Select Season 3 Identity
   PL:
457. [Interfejs i ustawienia [select_identity_popup_permanent_personality_label] — tekst] 상시
   źródło: Limbus3rdAnniversary.json :: dataList[id=select_identity_popup_permanent_personality_label].content
   limit: do 120 znaków
   EN: Always Available
   PL:

## Interfejs i ustawienia: LoginUIText
- plik gry: `LoginUIText.json`

458. [Interfejs i ustawienia [loginui_sign_in_with_google] — tekst] Google 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_google].content
   limit: do 120 znaków
   EN: Sign in with Google
   PL:
459. [Interfejs i ustawienia [loginui_sign_in_with_apple] — tekst] Apple 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_apple].content
   limit: do 120 znaków
   EN: Sign in with Apple
   PL:
460. [Interfejs i ustawienia [loginui_sign_in_with_steam] — tekst] Steam 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_steam].content
   limit: do 120 znaków
   EN: Sign in with Steam
   PL:
461. [Interfejs i ustawienia [loginui_sign_in_with_guest] — tekst] 게스트 계정으로 로그인하기
   źródło: LoginUIText.json :: dataList[id=loginui_sign_in_with_guest].content
   limit: do 120 znaków
   EN: Sign in as a guest
   PL:
462. [Interfejs i ustawienia [loginui_sign_out_current_account] — tekst] 현재 계정 로그아웃
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_current_account].content
   limit: do 120 znaków
   EN: Sign Out
   PL:
463. [Interfejs i ustawienia [loginui_sign_out_current_account_desc] — tekst] 현재 계정을 로그아웃 하시겠습니까?\n게스트 계정일 경우에는 데이터가 유실될 수 있습니다
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_current_account_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sign out from the current account?\nIf you’re playing as a guest, your data may be lost.
   PL:
464. [Interfejs i ustawienia [loginui_sign_out_switch_account_desc] — tekst] 현재 계정을 로그아웃하고\n선택한 계정으로 변경하시겠습니까?\n게스트 계정일 경우에는 데이터가 유실될 수 있습니다
   źródło: LoginUIText.json :: dataList[id=loginui_sign_out_switch_account_desc].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Sign out from the current account\nand switch to the selected one?\nIf you’re playing as a guest, your data may be lost.
   PL:
465. [Interfejs i ustawienia [switch_account] — tekst] 계정 변경
   źródło: LoginUIText.json :: dataList[id=switch_account].content
   limit: do 120 znaków
   EN: Change Account
   PL:
466. [Interfejs i ustawienia [user_agreements] — tekst] 이용 약관
   źródło: LoginUIText.json :: dataList[id=user_agreements].content
   limit: do 120 znaków
   EN: Terms of Service
   PL:
467. [Interfejs i ustawienia [title_game_data_download] — tekst] 게임 데이터 다운로드
   źródło: LoginUIText.json :: dataList[id=title_game_data_download].content
   limit: do 120 znaków
   EN: Download Game Data
   PL:
468. [Interfejs i ustawienia [content_game_data_download] — tekst] {0} 의 데이터를 다운로드합니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Downloading {0} of data.
   PL:
469. [Interfejs i ustawienia [content_game_data_download_description] — tekst] 저장 공간이 부족한 경우에는 타이틀 화면으로 돌아갑니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download_description].content
   limit: do 120 znaków
   EN: You will be returned to the title screen if your device has insufficient storage space.
   PL:
470. [Interfejs i ustawienia [content_game_data_download_recommend] — tekst] Wi-Fi 환경에서 다운로드하는 걸 권장합니다
   źródło: LoginUIText.json :: dataList[id=content_game_data_download_recommend].content
   limit: do 120 znaków
   EN: A direct Internet connection (Wi-Fi) is recommended.
   PL:
471. [Interfejs i ustawienia [switch_allcacheclear] — tekst] 모든 캐시 삭제
   źródło: LoginUIText.json :: dataList[id=switch_allcacheclear].content
   limit: do 120 znaków
   EN: Clear all caches
   PL:
472. [Interfejs i ustawienia [switch_oldcacheclear] — tekst] 이전 캐시 삭제
   źródło: LoginUIText.json :: dataList[id=switch_oldcacheclear].content
   limit: do 120 znaków
   EN: Clear old caches
   PL:
473. [Interfejs i ustawienia [networkingerror_content] — tekst] 네트워크가 불안정합니다.\n 네트워크 상태를 확인해 주세요
   źródło: LoginUIText.json :: dataList[id=networkingerror_content].content
   (powtórzenie elementu 226 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Interfejs i ustawienia [networkingerror_close] — tekst] 닫기
   źródło: LoginUIText.json :: dataList[id=networkingerror_close].content
   limit: do 120 znaków
   EN: Close
   PL:
475. [Interfejs i ustawienia [networkingerror_retry] — tekst] 재시도
   źródło: LoginUIText.json :: dataList[id=networkingerror_retry].content
   limit: do 120 znaków
   EN: Retry
   PL:
476. [Interfejs i ustawienia [loginui_ok] — tekst] 확인
   źródło: LoginUIText.json :: dataList[id=loginui_ok].content
   limit: do 120 znaków
   EN: Confirm
   PL:
477. [Interfejs i ustawienia [login_cancel] — tekst] 취소
   źródło: LoginUIText.json :: dataList[id=login_cancel].content
   limit: do 120 znaków
   EN: Cancel
   PL:
478. [Interfejs i ustawienia [loginui_loading_battlehint] — tekst] 전투 팁
   źródło: LoginUIText.json :: dataList[id=loginui_loading_battlehint].content
   limit: do 120 znaków
   EN: Combat Tips
   PL:
479. [Interfejs i ustawienia [servererror_content] — tekst] 서버 에러가 발생하였습니다.\n잠시 후에 다시 시도해 주세요.
   źródło: LoginUIText.json :: dataList[id=servererror_content].content
   (powtórzenie elementu 224 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Interfejs i ustawienia [serverstate_server_busy] — tekst] 서버가 혼잡합니다.\n잠시 후에 다시 시도해 주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_server_busy].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The server is currently busy.\nPlease try again in a moment.
   PL:
481. [Interfejs i ustawienia [forcequit_content] — tekst] 게임을 진행할 수 없습니다.\n게임이 종료됩니다.
   źródło: LoginUIText.json :: dataList[id=forcequit_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot operate the game.\nShutting down now.
   PL:
482. [Interfejs i ustawienia [serverstate_openpreparation] — tekst] 오픈 준비 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_openpreparation].content
   (powtórzenie elementu 229 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Interfejs i ustawienia [serverstate_regularcheck] — tekst] 서버 정기 점검이 진행 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_regularcheck].content
   (powtórzenie elementu 228 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Interfejs i ustawienia [serverstate_temporary_check] — tekst] 서버 임시 점검이 진행 중입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_temporary_check].content
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Interfejs i ustawienia [serverstate_verify_invaliduser] — tekst] 존재하지 않거나 탈퇴 처리가 완료된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invaliduser].content
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Interfejs i ustawienia [serverstate_verify_ban] — tekst] 게임 이용이 제한된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban].content
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Interfejs i ustawienia [serverstate_verify_invalidauth] — tekst] 오류가 발생하였습니다.\n다시 로그인을 진행해주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invalidauth].content
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
488. [Interfejs i ustawienia [guestlogin_failed_try_newguest] — tekst] 게스트 계정이 존재하지 않거나,\n이미 연동된 계정이기 때문에 게스트 로그인에 실패하였습니다.\n\n새로운 게스트 계정을 만드시겠습니까?
   źródło: LoginUIText.json :: dataList[id=guestlogin_failed_try_newguest].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Failed Guest Login.\nThe account is either already linked, or the Guest account doesn't exist.\n\nWould you like to make a new Guest account?
   PL:
489. [Interfejs i ustawienia [secession_remain_days] — tekst] 해당 계정은 탈퇴 처리 중 입니다.\n남은 시간 : {0}일 {1}시간 {2}분\n\n로그인 시, 계정이 복구됩니다.\n계정 복구를 진행하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=secession_remain_days].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, \n
   EN: The account is currently under a closure period.\nTime Remaining: {0}D {1}H {2}M\n\nYou can recover the account if you sign in now.\nRecover the account?
   PL:
490. [Interfejs i ustawienia [secession_canceled] — tekst] 계정 복구가 정상적으로 완료되었습니다.
   źródło: LoginUIText.json :: dataList[id=secession_canceled].content
   limit: do 120 znaków
   EN: Account recovered successfully.
   PL:
491. [Interfejs i ustawienia [serverstate_verify_invalidclientversion] — tekst] 게임 클라이언트가 최신 버전이 아닙니다.\n업데이트를 진행해주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invalidclientversion].content
   (powtórzenie elementu 233 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Interfejs i ustawienia [create_guest] — tekst] 게스트 생성
   źródło: LoginUIText.json :: dataList[id=create_guest].content
   limit: do 120 znaków
   EN: Create Guest Account
   PL:
493. [Interfejs i ustawienia [ask_to_remove_all_cache] — tekst] 모든 캐시를 삭제하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=ask_to_remove_all_cache].content
   limit: do 120 znaków
   EN: Clear all caches?
   PL:
494. [Interfejs i ustawienia [networkingerror_update] — tekst] 스토어로 이동
   źródło: LoginUIText.json :: dataList[id=networkingerror_update].content
   limit: do 120 znaków
   EN: Go to Store
   PL:
495. [Interfejs i ustawienia [speed_hack_warning] — tekst] 비인가 프로그램 사용이 확인되었습니다.
   źródło: LoginUIText.json :: dataList[id=speed_hack_warning].content
   limit: do 120 znaków
   EN: Usage of unauthorized third party program has been detected.
   PL:
496. [Interfejs i ustawienia [serverstate_verify_ban_startdate] — tekst] 일자
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_startdate].content
   limit: do 120 znaków
   EN: Date
   PL:
497. [Interfejs i ustawienia [serverstate_verify_ban_reason] — tekst] 내용
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason].content
   limit: do 120 znaków
   EN: Description
   PL:
498. [Interfejs i ustawienia [serverstate_verify_ban_reason_refund] — tekst] 오픈 마켓 환불 시스템 어뷰징
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason_refund].content
   limit: do 120 znaków
   EN: Abuse of Open Market refund system
   PL:
499. [Interfejs i ustawienia [serverstate_verify_ban_reason_cheat] — tekst] 비정상적인 게임 이용 기록
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_ban_reason_cheat].content
   limit: do 120 znaków
   EN: Abnormal game activity records
   PL:
500. [Interfejs i ustawienia [serverstate_blocking_endpoint] — tekst] 현재 점검 중인 기능입니다.
   źródło: LoginUIText.json :: dataList[id=serverstate_blocking_endpoint].content
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Interfejs i ustawienia [serverstate_verify_invaliduuid] — tekst] 이미 처리된 요청입니다.\n동기화를 위해 게임을 다시 실행해 주세요.
   źródło: LoginUIText.json :: dataList[id=serverstate_verify_invaliduuid].content
   (powtórzenie elementu 234 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Interfejs i ustawienia [login_scene_mini_story_warning_spoiler_format] — tekst] 주요 이야기 {0}장 이후의 내용을 담고 있습니다. 스토리를 감상하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_warning_spoiler_format].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: This story takes place after the Main Story Chapter {0}. Would you like to view the story anyway?
   PL:
503. [Interfejs i ustawienia [login_scene_mini_story_unlock_code_105] — tekst] 5
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_unlock_code_105].content
   limit: do 120 znaków
   EN: 5
   PL:
504. [Interfejs i ustawienia [login_scene_mini_story_unlock_code_9105] — tekst] 5.5
   źródło: LoginUIText.json :: dataList[id=login_scene_mini_story_unlock_code_9105].content
   limit: do 120 znaków
   EN: 5.5
   PL:
505. [Interfejs i ustawienia [switch_clearcatalog] — tekst] 카탈로그 삭제
   źródło: LoginUIText.json :: dataList[id=switch_clearcatalog].content
   limit: do 120 znaków
   EN: Delete Catalogue
   PL:
506. [Interfejs i ustawienia [panel_clearcatalog] — tekst] 카탈로그를 삭제하시겠습니까?
   źródło: LoginUIText.json :: dataList[id=panel_clearcatalog].content
   limit: do 120 znaków
   EN: Delete catalogue?
   PL:
507. [Interfejs i ustawienia [serverstate_error_thirdparty_api] — tekst] 외부 서버와의 통신에 문제가 발생하였습니다. 잠시 후에 다시 시도해 주십시오.
   źródło: LoginUIText.json :: dataList[id=serverstate_error_thirdparty_api].content
   (powtórzenie elementu 235 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Interfejs i ustawienia [servererror_invalid_purchasing_package] — tekst] 상품거래에 실패하였습니다.
   źródło: LoginUIText.json :: dataList[id=servererror_invalid_purchasing_package].content
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Interfejs i ustawienia [forcequit_cache_initialize_fail] — tekst] 게임 클라이언트가 정상적으로 기동하지 못하였습니다.\n네트워크 연결 상태를 확인하시고 다시 시도해 주세요.\n문의: limbussupport+bug@projmoon.com
   źródło: LoginUIText.json :: dataList[id=forcequit_cache_initialize_fail].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Game Client failed to launch properly.\nPlease confirm your network status and try again.\nInquiries: limbussupport+bug@projmoon.com
   PL:
510. [Interfejs i ustawienia [push_notification_message_full_stamina_default_title] — tekst] 림버스 컴퍼니
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_default_title].content
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Interfejs i ustawienia [push_notification_message_full_stamina_default_text] — tekst] 엔케팔린 충전이 완료되었습니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_default_text].content
   limit: do 120 znaków
   EN: Enkephalin has been fully recharged.
   PL:
512. [Interfejs i ustawienia [push_notification_message_full_stamina_1_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_1_title].content
   limit: do 120 znaków
   EN: Enkephalin Charged
   PL:
513. [Interfejs i ustawienia [push_notification_message_full_stamina_1_text] — tekst] 이상하다 여길 것은 없소. 그저 엔케팔린이 가득 찼다 말하러 온 것이기에… 용건은 이상이오.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_1_text].content
   limit: do 200 znaków
   EN: Take notice, yet naught is odd here. Ideally, my only purpose here would be to inform you that Enkephalin is replenished fully. Such is all I have to say.
   PL:
514. [Interfejs i ustawienia [push_notification_message_full_stamina_2_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_2_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Interfejs i ustawienia [push_notification_message_full_stamina_2_text] — tekst] 엔케팔린이 가득 찼네요. 관리자님. 효율적인 사용을 위해서 모듈로의 변환을 추천드립니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_2_text].content
   limit: do 160 znaków
   EN: Enkephalin recharge is complete. Dear manager, Enkephalin module conversion is recommended for the sake of efficiency.
   PL:
516. [Interfejs i ustawienia [push_notification_message_full_stamina_3_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_3_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Interfejs i ustawienia [push_notification_message_full_stamina_3_text] — tekst] 연료통이 빵빵해졌소, 관리자 나리이이!!! 모험을 떠나야 하는데 어디로 간 겐가!!!
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_3_text].content
   limit: do 130 znaków
   EN: MANAGER ESQUIRE!!! THE FUEL TANK HATH BEEN REFILLED!!! COME HITHER, FOR OUR ADVENTURES MUST GO ON!!!
   PL:
518. [Interfejs i ustawienia [push_notification_message_full_stamina_4_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_4_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
519. [Interfejs i ustawienia [push_notification_message_full_stamina_4_text] — tekst] 엔.팔.충.완.(엔케팔린 충전 완료.)
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_4_text].content
   limit: do 120 znaków
   EN: E.C.(Enkephalin Charged.)
   PL:
520. [Interfejs i ustawienia [push_notification_message_full_stamina_5_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_5_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Interfejs i ustawienia [push_notification_message_full_stamina_5_text] — tekst] 엔케팔린 충전이 완료되었습니다, 관리자님.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_5_text].content
   limit: do 120 znaków
   EN: Enkephalin has been fully recharged, manager.
   PL:
522. [Interfejs i ustawienia [push_notification_message_full_stamina_6_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_6_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
523. [Interfejs i ustawienia [push_notification_message_full_stamina_6_text] — tekst] 와아~ 벌써 엔케팔린이 다 충전됐나 봐요~ 확인해 보러 가지 않으실래요?
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_6_text].content
   limit: do 120 znaków
   EN: Woow~ Enkephalin's already fully charged~ Would you like to go check?
   PL:
524. [Interfejs i ustawienia [push_notification_message_full_stamina_7_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_7_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
525. [Interfejs i ustawienia [push_notification_message_full_stamina_7_text] — tekst] 그 뭐냐. 엔케…? 아무튼 초록색 연료 그거 충전 다 됐다더라. 가서 좀 봐.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_7_text].content
   limit: do 120 znaków
   EN: The, uh. Enkeph—? ... The green stuff's full. Go take a gander, yeah?
   PL:
526. [Interfejs i ustawienia [push_notification_message_full_stamina_8_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_8_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
527. [Interfejs i ustawienia [push_notification_message_full_stamina_8_text] — tekst] 엔케팔린 충전 완료... 음. 다시 버스가 출발할 수 있겠네요. 어서 가보죠.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_8_text].content
   limit: do 120 znaków
   EN: Enkephalin's been recharged... Hm. Yeah, the bus is ready for another voyage. Let's go.
   PL:
528. [Interfejs i ustawienia [push_notification_message_full_stamina_9_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_9_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
529. [Interfejs i ustawienia [push_notification_message_full_stamina_9_text] — tekst] 단테~ 엔케팔린 충전 끝났어. 모듈로 안 바꾸면 더 안 쌓일 거라구~
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_9_text].content
   limit: do 120 znaków
   EN: Dante~ Enkephalin's charged! Don'tcha forget to convert 'em to modules!
   PL:
530. [Interfejs i ustawienia [push_notification_message_full_stamina_11_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_11_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Interfejs i ustawienia [push_notification_message_full_stamina_11_text] — tekst] 관리자님... 바쁘신가요? 벼, 별건 아니고… 엔케팔린이 넘치고 있어서…
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_11_text].content
   limit: do 130 znaków
   EN: Hi, manager... are you... busy? I-it's nothing too serious, but... Enkephalin's about to overflow...
   PL:
532. [Interfejs i ustawienia [push_notification_message_full_stamina_12_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_12_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Interfejs i ustawienia [push_notification_message_full_stamina_12_text] — tekst] 보고드립니다, 관리자님. 엔케팔린이 완충되었습니다. 소모나 축적을 권장드립니다.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_12_text].content
   limit: do 160 znaków
   EN: Reporting to the Executive Manager. Enkephalin has been fully replenished. May I suggest that you use or convert them?
   PL:
534. [Interfejs i ustawienia [push_notification_message_full_stamina_13_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_13_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Interfejs i ustawienia [push_notification_message_full_stamina_13_text] — tekst] 어어, 관리자 양반! 그, 버스 연료가 가득 찼는데... 한 번 확인하지 그래?
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_13_text].content
   limit: do 120 znaków
   EN: Uhh, manager bud? You there? The, uh, the bus fuel tank is full... Might wanna come check?
   PL:
536. [Interfejs i ustawienia [push_notification_message_full_stamina_14_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_14_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Interfejs i ustawienia [push_notification_message_full_stamina_14_text] — tekst] 휴식 시간은 끝났습니다. 관리자 단테. 버스를 너무 오래 세워두지 마시지요.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_14_text].content
   limit: do 120 znaków
   EN: Your break is over, Manager Dante. Don't keep the bus sitting for too long.
   PL:
538. [Interfejs i ustawienia [push_notification_message_full_stamina_15_title] — tekst] 엔케팔린 충전 완료
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_15_title].content
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Interfejs i ustawienia [push_notification_message_full_stamina_15_text] — tekst] 메피가 배부르대, 카론. 부릉부릉할 시간이야.
   źródło: LoginUIText.json :: dataList[id=push_notification_message_full_stamina_15_text].content
   limit: do 120 znaków
   EN: Mephi's stuffed. Charon, time to vroom-vroom.
   PL:
540. [Interfejs i ustawienia [custom_localize_button] — tekst] 커스텀 언어 선택
   źródło: LoginUIText.json :: dataList[id=custom_localize_button].content
   limit: do 120 znaków
   EN: Select Custom Language
   PL:
541. [Interfejs i ustawienia [custom_localize_title] — tekst] 커스텀 언어 선택
   źródło: LoginUIText.json :: dataList[id=custom_localize_title].content
   (powtórzenie elementu 540 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Interfejs i ustawienia [custom_localize_desc] — tekst] ※ 언어 변경은 게임 재시작 시 정상 적용됩니다.
   źródło: LoginUIText.json :: dataList[id=custom_localize_desc].content
   limit: do 120 znaków
   EN: ※ Restart the game to apply the language change.
   PL:
543. [Interfejs i ustawienia [steam_overlay_cannot_activate_title] — tekst] 스팀 거래 오류
   źródło: LoginUIText.json :: dataList[id=steam_overlay_cannot_activate_title].content
   limit: do 120 znaków
   EN: Steam Transaction Error
   PL:
544. [Interfejs i ustawienia [steam_overlay_cannot_activate_text] — tekst] Steam 라이브러리에서\n[게임 내 Steam 오버레이 사용]을 활성화 후\n재접속해주세요.
   źródło: LoginUIText.json :: dataList[id=steam_overlay_cannot_activate_text].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Please turn on the [Enable the Steam Overlay while in-game] option\nfrom Steam's game properties - General,\nthen restart the game.
   PL:
545. [Interfejs i ustawienia [servererror_remain_restore_purchasing] — tekst] 아직 진행중이던 거래가 존재합니다.\n[구매 복구] 버튼을 눌러 재시도해주세요.
   źródło: LoginUIText.json :: dataList[id=servererror_remain_restore_purchasing].content
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Interfejs i ustawienia [invalid_login_no_guest_uid] — tekst] 게스트 계정이 존재하지 않거나,\n탈퇴된 계정입니다.
   źródło: LoginUIText.json :: dataList[id=invalid_login_no_guest_uid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Guest account does not exist,\nor has been deleted.
   PL:
547. [Interfejs i ustawienia [invalid_login_is_not_guest] — tekst] 이 게스트 계정은 이미 플랫폼과 연동되어 있습니다.\n[계정 변경]을 눌러 연동된 플랫폼으로 로그인해 주세요.
   źródło: LoginUIText.json :: dataList[id=invalid_login_is_not_guest].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This Guest account is already linked to a platform.\nPlease use the [Change Account] button to log into your linked platform.
   PL:
548. [Interfejs i ustawienia [try_new_guest] — tekst] 새로운 게스트 계정을 만드시겠습니까?
   źródło: LoginUIText.json :: dataList[id=try_new_guest].content
   limit: do 120 znaków
   EN: Make a new Guest account?
   PL:
549. [Interfejs i ustawienia [need_verify_integrity_steam] — tekst] 일부 리소스의 누락이 감지되었습니다.\n스팀 무결성 검사를 진행해 주세요
   źródło: LoginUIText.json :: dataList[id=need_verify_integrity_steam].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Missing resources detected.\nPlease use Steam's "Verify integrity of game files" function.
   PL:

## Interfejs i ustawienia: MainUIText-a1c10p1
- plik gry: `MainUIText-a1c10p1.json`

550. [Interfejs i ustawienia [main_ui_rpg_battle_defeated_title] — tekst] 전투 패배
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_battle_defeated_title].content
   limit: do 120 znaków
   EN: Battle Lost
   PL:
551. [Interfejs i ustawienia [main_ui_rpg_battle_defeated_desc] — tekst] <color=#990000>모든 수감자가 사망했습니다.</color>\n이후 진행을 선택해주세요.
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_battle_defeated_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: <color=#990000>All Sinners have been defeated.</color>\nChoose what you would like to do next.
   PL:
552. [Interfejs i ustawienia [main_ui_rpg_retry] — tekst] 재도전
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_retry].content
   limit: do 120 znaków
   EN: Try Again
   PL:
553. [Interfejs i ustawienia [main_ui_rpg_retry_desc] — tekst] 해당 전투를 처음부터 다시 시작
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_retry_desc].content
   limit: do 120 znaków
   EN: Restart this battle from the beginning
   PL:
554. [Interfejs i ustawienia [main_ui_rpg_accept_defeat] — tekst] 포기
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_accept_defeat].content
   limit: do 120 znaków
   EN: Forfeit
   PL:
555. [Interfejs i ustawienia [main_ui_rpg_accept_defeat_desc] — tekst] 마지막 저장 상태의 샘터로 복귀
   źródło: MainUIText-a1c10p1.json :: dataList[id=main_ui_rpg_accept_defeat_desc].content
   limit: do 120 znaków
   EN: Return to the Fount of the last save state
   PL:
556. [Interfejs i ustawienia [ContinueConfirm_Desc_Rpg_Stage] — tekst] 10-4 스테이지는 전투 중 컨티뉴 기능을 사용하여도 \n최종 클리어 시 EX 클리어로 기록됩니다.\n\n단, 컨티뉴 사용 이후 <color=#990000>재도전, 패배, 포기 없이 전투에서 승리하고 진행도가 저장</color>된 경우,\n<color=#990000>10-4 스테이지를 중도 포기하여도 컨티뉴에 사용된 재화가 반환되지 않습니다.</color>\n또한 사용된 광기는 청약철회가 불가능합니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=ContinueConfirm_Desc_Rpg_Stage].content
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: Regardless of whether the player used the Continue function or not,\nclearing Stage 10-4 will mark it as "Extra Conditions Fulfilled".\n\nHowever, <color=#990000>forfeiting Stage 10-4 will not refund any resources consumed to use the Continue function if a save state is created in Stage 10-4 <i>after</i> the user makes use of the Continue function to win the Encounter in question without retrying, losing, or forfeiting.</color>\n\nPlease note that consumed Lunacy cannot be refunded.
   PL:
557. [Interfejs i ustawienia [formation_ego_resource_popup_current_owned_desc] — tekst] 현재 보유한 E.G.O 자원의 수량입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ego_resource_popup_current_owned_desc].content
   limit: do 120 znaków
   EN: Currently owned E.G.O Resources can be viewed here.
   PL:
558. [Interfejs i ustawienia [formation_ego_resource_popup_current_owned] — tekst] 보유 E.G.O 자원
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ego_resource_popup_current_owned].content
   limit: do 120 znaków
   EN: E.G.O Resource Stock
   PL:
559. [Interfejs i ustawienia [9128_chapter_notice_button_title] — tekst] 챕터 유의사항
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_button_title].content
   limit: do 120 znaków
   EN: Warning
   PL:
560. [Interfejs i ustawienia [9128_chapter_notice_popup_title] — tekst] 현재 플레이하고 있는 챕터는 <color=#3246AB>[{0}장 {1}]</color>입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_popup_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#3246AB>, </color>, {0}, {1}
   EN: You are currently playing through Chapter <color=#3246AB>[{0} - {1}]</color>.
   PL:
561. [Interfejs i ustawienia [9128_chapter_notice_enter_title] — tekst] <color=#3246AB>[{0}장 {1}]</color>에 진입하시겠습니까?
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_enter_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#3246AB>, </color>, {0}, {1}
   EN: Enter <color=#3246AB>[Chapter {0} - {1}]</color>?
   PL:
562. [Interfejs i ustawienia [9128_chapter_notice_popup_desc] — tekst] ◆ 이전 챕터를 클리어하지 않았더라도 <color=#ff6000><mark color=#ff000040><b><u>주요 이야기 10장의 플레이가 가능</color></mark></b></u>합니다.\n◆ <color=#ff6000><mark color=#ff000040><b><u>9.5장까지의 스포일러</color></mark></b></u>를 담고 있습니다.\n◆ 10장을 클리어했을 때 이전 챕터를 클리어하지 않은 경우, 거울 던전, 거울굴절철도, 채광, 사영전투 등 <color=#ff6000><mark color=#ff000040><b><u>이전 챕터를 클리어해야 개방되는 콘텐츠를 이용할 수 없습니다.</color></mark></b></u> 모든 콘텐츠를 이용하기 위해 개방 조건을 충족해주시기 바랍니다.\n◆ 10장 클리어를 조건으로 하는 콘텐츠(향후 업데이트 예정)는 <color=#ff6000><mark color=#ff000040><b><u>10장 및 9.5-26 스테이지를 클리어</color></mark></b></u>해주시기 바랍니다.\n◆ 10장 플레이 시, <color=#ff6000><mark color=#ff000040><b><u>뫼르소의 일부 인격이 지원</color></mark></b></u>됩니다. (지원 인격 및 E.G.O에는 동기화/환상 해석 4단계가 적용됩니다.)\n◆ 10장 플레이 시, <color=#ff6000><mark color=#ff000040><b><u>모든 아군의 인격 동기화 3단계가 지원</color></mark></b></u>됩니다. E.G.O는 별도로 환상 해석이 보정되지 않습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=9128_chapter_notice_popup_desc].content
   limit: do 1020 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n
   EN: ◆ <color=#ff6000><mark color=#ff000040><b><u>Main Story Canto 10 can be played</color></mark></b></u> without clearing previous story chapters.\n◆ <color=#ff6000><mark color=#ff000040><b><u>Canto 10 contains spoilers up to Intervallo VII-2.</color></mark></b></u>\n◆ If you have not cleared the previous chapter by the time you have cleared Canto 10, <color=#ff6000><mark color=#ff000040><b><u>various content that requires Main Story progression (Mirror Dungeon, Refraction Railway, Luxcavation, Reflectrial, etc.) will not be unlocked until each respective prerequisite is cleared.</color></mark></b></u>\n◆ For any future content that requires clearing Canto 10 as the prerequisite, <color=#ff6000><mark color=#ff000040><b><u>please clear both Canto 10 and Stage 9.5-26 to unlock.</color></mark></b></u>\n◆ During Canto 10, <color=#ff6000><mark color=#ff000040><b><u>Meursault will have access to certain Support Identities</color></mark></b></u> and E.G.O (at Uptie/Threadspinning Tier 4).\n◆ During Canto 10, <color=#ff6000><mark color=#ff000040><b><u>all allied Identities, including Meursault, will be guaranteed at least Uptie 3</color></mark></b></u> (E.G.O Threadspinning Tier will not be affected).
   PL:
563. [Interfejs i ustawienia [settings_battle_effect_gate] — tekst] 중요 전투 진행 시 인격/E.G.O 연출용 오브젝트 숨김
   źródło: MainUIText-a1c10p1.json :: dataList[id=settings_battle_effect_gate].content
   limit: do 120 znaków
   EN: Hide Identity/E.G.O props in plot-critical battles
   PL:
564. [Interfejs i ustawienia [exp_dungeon_10_open_condition] — tekst] 9.5-26 및 10-4 클리어
   źródło: MainUIText-a1c10p1.json :: dataList[id=exp_dungeon_10_open_condition].content
   limit: do 120 znaków
   EN: Clear 9.5-26 and 10-4
   PL:
565. [Interfejs i ustawienia [formation_deck_code_condition_reset] — tekst] 편성 조건에 맞지 않는 인격은 기본 인격으로 적용되었습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_deck_code_condition_reset].content
   limit: do 140 znaków
   EN: Base Identities have been applied in place of Identities that do not meet the Team Loadout requirement.
   PL:
566. [Interfejs i ustawienia [character_list_friend_support_companion_impossible] — tekst] 함께 지정되는 {0}의 지원 인격을 지정할 수 없는 스테이지입니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=character_list_friend_support_companion_impossible].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} will be selected in tandem. This Stage does not allow you to use their Support Identity.
   PL:
567. [Interfejs i ustawienia [gacha_additional_explain_button_label] — tekst] 동시 획득 인격 안내
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_additional_explain_button_label].content
   limit: do 120 znaków
   EN: Pair Identity Details
   PL:
568. [Interfejs i ustawienia [gacha_307_additional_explain_title] — tekst] 동시 획득 인격 안내
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_307_additional_explain_title].content
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Interfejs i ustawienia [gacha_307_additional_explain_desc] — tekst] 쐐기 사무소 해결사 돈키호테와 쐐기 사무소 해결사 싱클레어는 추출에서 하나의 3성 인격으로 취급되며,\n등장 시 두 인격을 항상 함께 획득합니다.\n\n· 쐐기 사무소 해결사 돈키호테 & 쐐기 사무소 해결사 싱클레어의 등장 확률은 아래와 같습니다.\n- 두 인격이 대표 3성 인격(픽업)인 특정 추출: 대표 3성 인격 1명의 등장 확률과 동일\n- 그 외 두 인격이 등장하는 추출: 대표가 아닌 3성 인격 1명의 등장 확률과 동일\n(자세한 확률은 각 추출의 [확률 상세보기]에서 확인할 수 있습니다.)\n \n· 별빛도 3성 인격 1명분으로 계산되어, 추출에서 첫 획득 시 두 인격을 합쳐 별빛 300개를 얻습니다.\n\n· 두 인격이 대표 3성 인격인 특정 추출에서는 이상[理想] 200개로 두 인격을 함께 교환할 수 있습니다.\n\n· 두 인격을 이미 보유한 상태에서 다시 획득하면,\n등급에 따른 자아 파편 대신 현재 시즌의 돈키호테 자아 파편 25개와 싱클레어 자아 파편 25개를 획득합니다.\n\n· 자판기에 추가된 후에는 돈키호테 자아 파편과 싱클레어 자아 파편을 합쳐 400개로 두 인격을 함께 구입할 수 있습니다. 두 자아 파편을 각각 1개 이상 사용해야 하며, 비율은 자유롭게 정할 수 있습니다.\n\n· 인격 레벨 상승, 동기화, 외형 투영 시 두 인격을 각각 따로 진행해야하며, 인격마다 일반 3성 인격과 같은 재료가 필요합니다. 이때 자아 파편은 해당 수감자의 자아 파편을 사용합니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=gacha_307_additional_explain_desc].content
   limit: do 2090 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wedge Office Fixer Don Quixote and Wedge Office Fixer Sinclair are treated as a single 3★ Identity in the Extraction. Obtaining either Identity will always yield the other in the pair.\n\n· The Extraction rates for Wedge Office Fixer Don Quixote & Wedge Office Fixer Sinclair are as follows:\n  - In Target Extractions where the pair is featured as the 3★ pickup: The same appearance rate as 1 featured 3★ Identity\n  - In all other Extractions where the pair can appear: The same appearance rate as 1 non-featured 3★ Identity\n(for detailed rates, please refer to [Probabilities] for each Extraction)\n\n· Starlight is also calculated as if the pair were a single 3★ Identity. When first obtained through Extraction, the two Identities grant a combined total of 300 Starlight.\n\n· In Target Extractions where both Identities are featured as the 3★ pickup, both can be exchanged together for 200 Yisang [Ideality].\n\n· If the pair is obtained again after both Identities have already been acquired, you will receive 25 Don Quixote Egoshards and 25 Sinclair Egoshards from the current Season instead of the usual Egoshards awarded for duplicate Identities of their rarity.\n\n· Once the pair is added to the Dispenser, both Identities can be obtained together for a combined total of 400 Don Quixote and Sinclair Egoshards. You must use at least 1 Egoshard from each Sinner, but you can adjust the ratio between the two freely.\n\n· Identity level-ups, Upties, and Façade Projection must be performed separately for each Identity. Each Identity requires the same materials as a standard 3★ Identity. Any Egoshards required for these upgrades must belong to the respective Sinner.
   PL:
570. [Interfejs i ustawienia [formation_ui_panel_start_battle_lor] — tekst] 접대 시작
   źródło: MainUIText-a1c10p1.json :: dataList[id=formation_ui_panel_start_battle_lor].content
   limit: do 120 znaków
   EN: Commence Reception
   PL:
571. [Interfejs i ustawienia [battle_walpu10_ego_page_history_ashes] — tekst] 밝은 모든 것들을 남김없이 태워버리기 위해…
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_ashes].content
   limit: do 120 znaków
   EN: To burn all things that are bright to ashes...
   PL:
572. [Interfejs i ustawienia [battle_walpu10_ego_page_history_nostalgic_embrace] — tekst] 나를 꼬옥 안아주지 않을래? 마음이 편해질 거야.
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_nostalgic_embrace].content
   limit: do 120 znaków
   EN: Give me a tight hug, will you? It'll soothe your mind.
   PL:
573. [Interfejs i ustawienia [battle_walpu10_ego_page_history_gluttony] — tekst] 우리가 네 곁을 지키는 이유?\n당연히 보호하기 위해서지!
   źródło: MainUIText-a1c10p1.json :: dataList[id=battle_walpu10_ego_page_history_gluttony].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The reason we're staying by your side?\nOf course it's to protect you!
   PL:
574. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not_already_have_companion] — tekst] 선택한 인격을 모두 이미 보유 중입니다. 이상[理想] 200개를 소모하여 각 수감자의 파편을 25개씩 교환하시겠습니까?
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_pity_point_progress_or_not_already_have_companion].content
   limit: do 140 znaków
   EN: You already own the selected Identity pair. Exchange 200 Yisang [Ideality] for each Sinner's 25 Egoshards?
   PL:
575. [Interfejs i ustawienia [notice_of_vending_machine_companion_1] — tekst] 돈키호테 자아 파편과 싱클레어 자아 파편을 합쳐 400개로 두 인격을 함께 구입할 수 있습니다. 두 자아 파편을 각각 1개 이상 사용해야 하며, 비율은 자유롭게 정할 수 있습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_vending_machine_companion_1].content
   limit: do 270 znaków
   EN: Both Identities can be obtained together for a combined total of 400 Don Quixote and Sinclair Egoshards. You must use at least 1 Egoshard from each Sinner, but you can adjust the ratio between the two freely.
   PL:
576. [Interfejs i ustawienia [notice_of_story_same_content] — tekst] {0}와 동일한 내용으로, 보상만 수령되었습니다.
   źródło: MainUIText-a1c10p1.json :: dataList[id=notice_of_story_same_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Contents the same as {0}. Only the reward is obtained.
   PL:
577. [Interfejs i ustawienia [10th_anniversary_event_desc] — tekst] 기간 내 접속 시 3성 인격 출현 추출 티켓 및 광기 증정
   źródło: MainUIText-a1c10p1.json :: dataList[id=10th_anniversary_event_desc].content
   limit: do 120 znaków
   EN: Log in during the event and pick up a [3★ Guarantee Decaextraction Ticket and Lunacy]
   PL:

## Interfejs i ustawienia: MainUIText-a1c7p1
- plik gry: `MainUIText-a1c7p1.json`

578. [Interfejs i ustawienia [stage_recommend_level_popup_battle_participant_desc] — tekst] 전투에 참가할 인격의 현재 평균 레벨이 스테이지 권장 레벨보다 <color=#990000>낮습니다.</color>\n전투를 진행하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_battle_participant_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: The current average level of your deployed Identities is <color=#990000>lower</color> than the recommended level for this Stage.\nStart the Encounter anyway?
   PL:
579. [Interfejs i ustawienia [stage_recommend_level_popup_formation_desc] — tekst] 현재 편성의 육성 수준이 권장 사양보다 <color=#990000>낮습니다. 진입 시 어려운 전투가 진행될 수 있습니다.</color>\n전투를 진행하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_formation_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: Your current loadout's average upgrade progress is <color=#990000>below the recommended specs, and you may face a difficult battle.</color>\nEnter the battle anyway?
   PL:
580. [Interfejs i ustawienia [stage_recommend_level_popup_dungeon_entrance_desc] — tekst] 편성 인격의 현재 평균 레벨이 스테이지 권장 레벨보다 <color=#990000>낮습니다.</color>\n던전에 입장하시겠습니까?
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_level_popup_dungeon_entrance_desc].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, \n
   EN: The current average level of Identities in your loadout is <color=#990000>lower</color> than the recommended level for this Stage.\nEnter the Dungeon anyway?
   PL:
581. [Interfejs i ustawienia [current_average_level_and_recommend_level_format] — tekst] 현재 평균 레벨: {0}\n<color=#f8c200>스테이지 권장 레벨: {1}</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=current_average_level_and_recommend_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, \n
   EN: Current Avg. Level: {0}\n<color=#f8c200>Recommended Level: {1}</color>
   PL:
582. [Interfejs i ustawienia [current_average_level_with_additional_val_and_recommend_level_format] — tekst] 현재 평균 레벨: {0} ({1})\n<color=#f8c200>스테이지 권장 레벨: {2}</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=current_average_level_with_additional_val_and_recommend_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, {2}, \n
   EN: Current Avg. Level: {0} ({1})\n<color=#f8c200>Recommended Level: {2}</color>
   PL:
583. [Interfejs i ustawienia [stage_recommend_uptie_popup_dungeon_entrance_desc] — tekst] <color=#f8c200>인격 동기화, E.G.O 환상 해석 <color=#990000>{0}단계</color> 권장</color>
   źródło: MainUIText-a1c7p1.json :: dataList[id=stage_recommend_uptie_popup_dungeon_entrance_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, <color=#990000>, </color>, {0}
   EN: <color=#f8c200>Recommended Identity & E.G.O Uptie/Threadspin <color=#990000>Tiers: {0}</color> </color>
   PL:

## Interfejs i ustawienia: MainUIText
- plik gry: `MainUIText.json`

584. [Interfejs i ustawienia [mainui_main_button0] — tekst] 유리창
   źródło: MainUIText.json :: dataList[id=mainui_main_button0].content
   limit: do 120 znaków
   EN: Window
   PL:
585. [Interfejs i ustawienia [mainui_main_button1] — tekst] 수감자
   źródło: MainUIText.json :: dataList[id=mainui_main_button1].content
   limit: do 120 znaków
   EN: Sinners
   PL:
586. [Interfejs i ustawienia [mainui_main_button2] — tekst] 상영관
   źródło: MainUIText.json :: dataList[id=mainui_main_button2].content
   limit: do 120 znaków
   EN: Theater
   PL:
587. [Interfejs i ustawienia [mainui_main_button3] — tekst] 운전석
   źródło: MainUIText.json :: dataList[id=mainui_main_button3].content
   limit: do 120 znaków
   EN: Drive
   PL:
588. [Interfejs i ustawienia [mainui_main_button4] — tekst] 추출
   źródło: MainUIText.json :: dataList[id=mainui_main_button4].content
   limit: do 120 znaków
   EN: Extract
   PL:
589. [Interfejs i ustawienia [mainui_main_button5] — tekst] 자판기
   źródło: MainUIText.json :: dataList[id=mainui_main_button5].content
   limit: do 120 znaków
   EN: Dispense
   PL:
590. [Interfejs i ustawienia [mainui_main_exp] — tekst] EXP
   źródło: MainUIText.json :: dataList[id=mainui_main_exp].content
   limit: do 120 znaków
   EN: EXP
   PL:
591. [Interfejs i ustawienia [mainui_main_stamina] — tekst] 스태미너
   źródło: MainUIText.json :: dataList[id=mainui_main_stamina].content
   limit: do 120 znaków
   EN: Stamina
   PL:
592. [Interfejs i ustawienia [mainui_main_enkephalin] — tekst] 엔케팔린
   źródło: MainUIText.json :: dataList[id=mainui_main_enkephalin].content
   (powtórzenie elementu 295 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Interfejs i ustawienia [mainui_main_madness] — tekst] 광기
   źródło: MainUIText.json :: dataList[id=mainui_main_madness].content
   limit: do 120 znaków
   EN: Lunacy
   PL:
594. [Interfejs i ustawienia [mainui_battleselection_everydungeon] — tekst] 거울 던전
   źródło: MainUIText.json :: dataList[id=mainui_battleselection_everydungeon].content
   limit: do 120 znaków
   EN: Mirror Dungeons
   PL:
595. [Interfejs i ustawienia [mainui_stageinfo_recommendlevel] — tekst] 추천 레벨
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_recommendlevel].content
   limit: do 120 znaków
   EN: Difficulty
   PL:
596. [Interfejs i ustawienia [mainui_stageinfo_enemyinfo] — tekst] 적 정보
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_enemyinfo].content
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Interfejs i ustawienia [mainui_stageinfo_exclearcondition] — tekst] EX 클리어 조건
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_exclearcondition].content
   limit: do 120 znaków
   EN: EX Objectives
   PL:
598. [Interfejs i ustawienia [mainui_stageinfo_statinfo] — tekst] 스테이터스
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_statinfo].content
   (powtórzenie elementu 39 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Interfejs i ustawienia [mainui_stageinfo_resistinfo] — tekst] 내성 정보
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_resistinfo].content
   (powtórzenie elementu 41 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Interfejs i ustawienia [mainui_stageinfo_enterbutton] — tekst] 입장
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_enterbutton].content
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Interfejs i ustawienia [mainui_stageinfo_dungeonclear] — tekst] 던전 클리어 조건
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_dungeonclear].content
   limit: do 120 znaków
   EN: Main Objectives
   PL:
602. [Interfejs i ustawienia [mainui_sinners_battleannouncer] — tekst] 아나운서
   źródło: MainUIText.json :: dataList[id=mainui_sinners_battleannouncer].content
   limit: do 120 znaków
   EN: Announcer
   PL:
603. [Interfejs i ustawienia [mainui_sinners_dante] — tekst] 단테
   źródło: MainUIText.json :: dataList[id=mainui_sinners_dante].content
   limit: do 120 znaków
   EN: Dante
   PL:
604. [Interfejs i ustawienia [mainui_sinners_decklist] — tekst] 덱 목록
   źródło: MainUIText.json :: dataList[id=mainui_sinners_decklist].content
   limit: do 120 znaków
   EN: DECK LIST
   PL:
605. [Interfejs i ustawienia [mainui_sinners_deck] — tekst] 덱
   źródło: MainUIText.json :: dataList[id=mainui_sinners_deck].content
   limit: do 120 znaków
   EN: Deck
   PL:
606. [Interfejs i ustawienia [mainui_sinners_passive] — tekst] 지속 효과
   źródło: MainUIText.json :: dataList[id=mainui_sinners_passive].content
   limit: do 120 znaków
   EN: PASSIVES
   PL:
607. [Interfejs i ustawienia [mainui_sinners_egoresource] — tekst] E.G.O 자원
   źródło: MainUIText.json :: dataList[id=mainui_sinners_egoresource].content
   limit: do 120 znaków
   EN: AFFINITIES
   PL:
608. [Interfejs i ustawienia [mainui_sinners_participant] — tekst] 참여 인원 선택
   źródło: MainUIText.json :: dataList[id=mainui_sinners_participant].content
   limit: do 120 znaków
   EN: Select Participants
   PL:
609. [Interfejs i ustawienia [mainui_sinners_startbattle] — tekst] 전투 시작
   źródło: MainUIText.json :: dataList[id=mainui_sinners_startbattle].content
   limit: do 120 znaków
   EN: To Battle!
   PL:
610. [Interfejs i ustawienia [mainui_common_personality] — tekst] 인격
   źródło: MainUIText.json :: dataList[id=mainui_common_personality].content
   (powtórzenie elementu 382 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Interfejs i ustawienia [mainui_common_filter] — tekst] 필터
   źródło: MainUIText.json :: dataList[id=mainui_common_filter].content
   limit: do 120 znaków
   EN: Filter
   PL:
612. [Interfejs i ustawienia [mainui_common_state] — tekst] 현황
   źródło: MainUIText.json :: dataList[id=mainui_common_state].content
   limit: do 120 znaków
   EN: Current
   PL:
613. [Interfejs i ustawienia [mainui_common_sort] — tekst] 정렬
   źródło: MainUIText.json :: dataList[id=mainui_common_sort].content
   limit: do 120 znaków
   EN: Sort
   PL:
614. [Interfejs i ustawienia [mainui_sinners_unequipego] — tekst] 미장착
   źródło: MainUIText.json :: dataList[id=mainui_sinners_unequipego].content
   limit: do 120 znaków
   EN: Unequipped
   PL:
615. [Interfejs i ustawienia [mainui_skip_desc] — tekst] 스킵 하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_skip_desc].content
   limit: do 120 znaków
   EN: Are you sure you want to skip?
   PL:
616. [Interfejs i ustawienia [mainui_story_continue_next_desc] — tekst] 다음 화를 이어보시겠습니까?\n(초회 보상이 있다면 수령후 이어봄)
   źródło: MainUIText.json :: dataList[id=mainui_story_continue_next_desc].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Continue to the next episode?\n(will proceed after receiving any available first-time viewing rewards)
   PL:
617. [Interfejs i ustawienia [mainui_battleresult_reward] — tekst] 보상
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_reward].content
   limit: do 120 znaków
   EN: Rewards
   PL:
618. [Interfejs i ustawienia [mainui_battleresult_exclearreward] — tekst] EX 클리어 보상
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_exclearreward].content
   limit: do 120 znaków
   EN: EX Rewards
   PL:
619. [Interfejs i ustawienia [mainui_battleresult_statistics] — tekst] 통계
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_statistics].content
   limit: do 120 znaków
   EN: Stats
   PL:
620. [Interfejs i ustawienia [mainui_ok] — tekst] 확인
   źródło: MainUIText.json :: dataList[id=mainui_ok].content
   (powtórzenie elementu 476 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Interfejs i ustawienia [mainui_battleresult_victory] — tekst] 전투 승리
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_victory].content
   limit: do 120 znaków
   EN: Victory
   PL:
622. [Interfejs i ustawienia [mainui_battleresult_defeat] — tekst] 전투 패배
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_defeat].content
   limit: do 120 znaków
   EN: Defeat
   PL:
623. [Interfejs i ustawienia [mainui_battleresult_return] — tekst] 반환
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_return].content
   limit: do 120 znaków
   EN: Return
   PL:
624. [Interfejs i ustawienia [mainui_battleresult_hint] — tekst] 힌트
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_hint].content
   limit: do 120 znaków
   EN: Hint
   PL:
625. [Interfejs i ustawienia [mainui_page] — tekst] {0}장
   źródło: MainUIText.json :: dataList[id=mainui_page].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Pg. {0}
   PL:
626. [Interfejs i ustawienia [mainui_cancel] — tekst] 취소
   źródło: MainUIText.json :: dataList[id=mainui_cancel].content
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
627. [Interfejs i ustawienia [mainui_select] — tekst] 선택
   źródło: MainUIText.json :: dataList[id=mainui_select].content
   limit: do 120 znaków
   EN: Select
   PL:
628. [Interfejs i ustawienia [mainui_select_finished] — tekst] 선택 완료
   źródło: MainUIText.json :: dataList[id=mainui_select_finished].content
   limit: do 120 znaków
   EN: Finalize
   PL:
629. [Interfejs i ustawienia [mainui_grade] — tekst] {0} 단계
   źródło: MainUIText.json :: dataList[id=mainui_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Stage {0}
   PL:
630. [Interfejs i ustawienia [mainui_floor] — tekst] {0}층
   źródło: MainUIText.json :: dataList[id=mainui_floor].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Floor {0}
   PL:
631. [Interfejs i ustawienia [mainui_main_enkephalin_Box] — tekst] 엔케팔린 박스
   źródło: MainUIText.json :: dataList[id=mainui_main_enkephalin_Box].content
   limit: do 120 znaków
   EN: Enkephalin Box
   PL:
632. [Interfejs i ustawienia [mainui_main_own_count] — tekst] 소지 수
   źródło: MainUIText.json :: dataList[id=mainui_main_own_count].content
   limit: do 120 znaków
   EN: Owned
   PL:
633. [Interfejs i ustawienia [mainui_mirror_entrance_entry] — tekst] {0}에 입장하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_entry].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Will you enter {0}?
   PL:
634. [Interfejs i ustawienia [mainui_mirror_entrance_progressing] — tekst] {0}을 진행 중입니다.
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_progressing].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} is in progress.
   PL:
635. [Interfejs i ustawienia [mainui_mirror_entrance_re_entry] — tekst] 다시 입장하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_re_entry].content
   limit: do 120 znaków
   EN: Will you reenter the dungeon?
   PL:
636. [Interfejs i ustawienia [mainui_mirror_entrance_quit] — tekst] 던전 탐사를 그만두시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_quit].content
   limit: do 120 znaków
   EN: Quit exploring the dungeon?
   PL:
637. [Interfejs i ustawienia [mainui_mirror_entrance_quit_former] — tekst] 기존 던전 탐사를 그만두시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_quit_former].content
   limit: do 120 znaków
   EN: Forfeit previous exploration progress?
   PL:
638. [Interfejs i ustawienia [mainui_mirror_entrance_warning] — tekst] ※소비한 엔케팔린 모듈은 반환되지 않습니다.
   źródło: MainUIText.json :: dataList[id=mainui_mirror_entrance_warning].content
   limit: do 120 znaków
   EN: ※ Spent Enkephalin Modules will not be refunded.
   PL:
639. [Interfejs i ustawienia [mainui_proress] — tekst] 진행
   źródło: MainUIText.json :: dataList[id=mainui_proress].content
   limit: do 120 znaków
   EN: Proceed
   PL:
640. [Interfejs i ustawienia [mainui_stop] — tekst] 중단
   źródło: MainUIText.json :: dataList[id=mainui_stop].content
   limit: do 120 znaków
   EN: Halt
   PL:
641. [Interfejs i ustawienia [mainui_next] — tekst] 다음
   źródło: MainUIText.json :: dataList[id=mainui_next].content
   limit: do 120 znaków
   EN: Next
   PL:
642. [Interfejs i ustawienia [mainui_ego_list] — tekst] E.G.O 목록
   źródło: MainUIText.json :: dataList[id=mainui_ego_list].content
   limit: do 120 znaków
   EN: E.G.O List
   PL:
643. [Interfejs i ustawienia [mainui_personality_list] — tekst] 인격 목록
   źródło: MainUIText.json :: dataList[id=mainui_personality_list].content
   limit: do 120 znaków
   EN: Identity List
   PL:
644. [Interfejs i ustawienia [mainui_acquired_reward] — tekst] 획득 보상
   źródło: MainUIText.json :: dataList[id=mainui_acquired_reward].content
   limit: do 120 znaków
   EN: Rewards Acquired
   PL:
645. [Interfejs i ustawienia [mainui_dungeon_finished] — tekst] 탐사 종료
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_finished].content
   limit: do 120 znaków
   EN: Pause Exploration
   PL:
646. [Interfejs i ustawienia [mainui_category] — tekst] 범례
   źródło: MainUIText.json :: dataList[id=mainui_category].content
   (powtórzenie elementu 70 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Interfejs i ustawienia [mainui_stats_hp] — tekst] 체력
   źródło: MainUIText.json :: dataList[id=mainui_stats_hp].content
   limit: do 120 znaków
   EN: HP
   PL:
648. [Interfejs i ustawienia [mainui_stats_speed] — tekst] 속도
   źródło: MainUIText.json :: dataList[id=mainui_stats_speed].content
   limit: do 120 znaków
   EN: SPD
   PL:
649. [Interfejs i ustawienia [mainui_stats_defense] — tekst] 방어 레벨
   źródło: MainUIText.json :: dataList[id=mainui_stats_defense].content
   limit: do 120 znaków
   EN: Defense Level
   PL:
650. [Interfejs i ustawienia [mainui_upgrade] — tekst] 강화
   źródło: MainUIText.json :: dataList[id=mainui_upgrade].content
   limit: do 120 znaków
   EN: Power-up
   PL:
651. [Interfejs i ustawienia [mainui_mirror_select_ego] — tekst] E.G.O 선택으로 이동
   źródło: MainUIText.json :: dataList[id=mainui_mirror_select_ego].content
   limit: do 120 znaków
   EN: To E.G.O
   PL:
652. [Interfejs i ustawienia [mainui_mirror_opening] — tekst] 개방 중
   źródło: MainUIText.json :: dataList[id=mainui_mirror_opening].content
   limit: do 120 znaków
   EN: Now Open
   PL:
653. [Interfejs i ustawienia [mainui_simulation] — tekst] 시뮬레이션
   źródło: MainUIText.json :: dataList[id=mainui_simulation].content
   limit: do 120 znaków
   EN: Simulation
   PL:
654. [Interfejs i ustawienia [mainui_untill] — tekst] 까지
   źródło: MainUIText.json :: dataList[id=mainui_untill].content
   limit: do 120 znaków
   EN: Expiry
   PL:
655. [Interfejs i ustawienia [mainui_free] — tekst] 무료
   źródło: MainUIText.json :: dataList[id=mainui_free].content
   limit: do 120 znaków
   EN: Free
   PL:
656. [Interfejs i ustawienia [mainui_paid] — tekst] 유료
   źródło: MainUIText.json :: dataList[id=mainui_paid].content
   limit: do 120 znaków
   EN: Paid
   PL:
657. [Interfejs i ustawienia [mainui_support] — tekst] 지원
   źródło: MainUIText.json :: dataList[id=mainui_support].content
   (powtórzenie elementu 381 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Interfejs i ustawienia [mainui_gacha_rateinfo] — tekst] 확률 상세보기
   źródło: MainUIText.json :: dataList[id=mainui_gacha_rateinfo].content
   limit: do 120 znaków
   EN: Probabilities
   PL:
659. [Interfejs i ustawienia [mainui_gacha_history] — tekst] 추출 이력
   źródło: MainUIText.json :: dataList[id=mainui_gacha_history].content
   limit: do 120 znaków
   EN: Extraction History
   PL:
660. [Interfejs i ustawienia [mainui_gacha_daliynotice] — tekst] 매일 {0}시에 초기화
   źródło: MainUIText.json :: dataList[id=mainui_gacha_daliynotice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Resets each day at {0}:00
   PL:
661. [Interfejs i ustawienia [mainui_gacha_alreadyusedgacha] — tekst] 금일 이용 가능 횟수 이용 완료
   źródło: MainUIText.json :: dataList[id=mainui_gacha_alreadyusedgacha].content
   limit: do 120 znaków
   EN: Daily Quota Exhausted
   PL:
662. [Interfejs i ustawienia [mainui_gacha_extract1] — tekst] 1회 추출
   źródło: MainUIText.json :: dataList[id=mainui_gacha_extract1].content
   limit: do 120 znaków
   EN: Extract 1
   PL:
663. [Interfejs i ustawienia [mainui_gacha_extract10] — tekst] 10회 추출
   źródło: MainUIText.json :: dataList[id=mainui_gacha_extract10].content
   limit: do 120 znaków
   EN: Extract 10
   PL:
664. [Interfejs i ustawienia [mainui_open_battlepass] — tekst] 배틀 패스가 열렸습니다!
   źródło: MainUIText.json :: dataList[id=mainui_open_battlepass].content
   limit: do 120 znaków
   EN: The Battle Pass is unlocked!
   PL:
665. [Interfejs i ustawienia [mainui_grade_without_space] — tekst] {0}단계
   źródło: MainUIText.json :: dataList[id=mainui_grade_without_space].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Step {0}
   PL:
666. [Interfejs i ustawienia [mainui_type] — tekst] 유형
   źródło: MainUIText.json :: dataList[id=mainui_type].content
   limit: do 120 znaków
   EN: Type
   PL:
667. [Interfejs i ustawienia [mainui_level_unit] — tekst] {0}성
   źródło: MainUIText.json :: dataList[id=mainui_level_unit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}★
   PL:
668. [Interfejs i ustawienia [mainui_Change_lobby_illust] — tekst] 로비 일러스트 변경
   źródło: MainUIText.json :: dataList[id=mainui_Change_lobby_illust].content
   limit: do 120 znaków
   EN: Change Lobby Art
   PL:
669. [Interfejs i ustawienia [mainui_lobby_illust_acquisition_method] — tekst] 획득 조건
   źródło: MainUIText.json :: dataList[id=mainui_lobby_illust_acquisition_method].content
   limit: do 120 znaków
   EN: To Unlock:
   PL:
670. [Interfejs i ustawienia [mainui_networkingerror_content] — tekst] 네트워크가 불안정 합니다.\n 네트워크 상태를 확인해주세요
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_content].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The network is unstable.\nPlease check your Internet connection.
   PL:
671. [Interfejs i ustawienia [mainui_networkingerror_close] — tekst] 닫기
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_close].content
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Interfejs i ustawienia [mainui_networkingerror_retry] — tekst] 재시도
   źródło: MainUIText.json :: dataList[id=mainui_networkingerror_retry].content
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Interfejs i ustawienia [mainui_event_notice] — tekst] 이벤트 공지
   źródło: MainUIText.json :: dataList[id=mainui_event_notice].content
   limit: do 120 znaków
   EN: Event Notifs
   PL:
674. [Interfejs i ustawienia [mainui_system_notice] — tekst] 시스템 공지
   źródło: MainUIText.json :: dataList[id=mainui_system_notice].content
   limit: do 120 znaków
   EN: System Notifs
   PL:
675. [Interfejs i ustawienia [mainui_team] — tekst] 팀
   źródło: MainUIText.json :: dataList[id=mainui_team].content
   limit: do 120 znaków
   EN: Team
   PL:
676. [Interfejs i ustawienia [mainui_cost] — tekst] 코스트
   źródło: MainUIText.json :: dataList[id=mainui_cost].content
   limit: do 120 znaków
   EN: Cost
   PL:
677. [Interfejs i ustawienia [mainui_dungeon_progress_rate] — tekst] 던전 진행도
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_progress_rate].content
   limit: do 120 znaków
   EN: Dungeon Progress
   PL:
678. [Interfejs i ustawienia [mainui_guaranteed_reward] — tekst] 확정 보상
   źródło: MainUIText.json :: dataList[id=mainui_guaranteed_reward].content
   limit: do 120 znaków
   EN: Rewards
   PL:
679. [Interfejs i ustawienia [mainui_select_reward] — tekst] 선택 보상
   źródło: MainUIText.json :: dataList[id=mainui_select_reward].content
   limit: do 120 znaków
   EN: Optional Rewards
   PL:
680. [Interfejs i ustawienia [mainui_battle_pass_exp] — tekst] 배틀 패스 경험치
   źródło: MainUIText.json :: dataList[id=mainui_battle_pass_exp].content
   limit: do 120 znaków
   EN: Battle Pass XP
   PL:
681. [Interfejs i ustawienia [mainui_enforce_ticket] — tekst] 강화 티켓
   źródło: MainUIText.json :: dataList[id=mainui_enforce_ticket].content
   limit: do 120 znaków
   EN: Upgrade Tickets
   PL:
682. [Interfejs i ustawienia [mainui_reward_random_box] — tekst] 랜덤 자아 파편 상자
   źródło: MainUIText.json :: dataList[id=mainui_reward_random_box].content
   limit: do 120 znaków
   EN: Egoshard Crates
   PL:
683. [Interfejs i ustawienia [mainui_reward_select_box] — tekst] 선택 자아 파편 상자
   źródło: MainUIText.json :: dataList[id=mainui_reward_select_box].content
   limit: do 120 znaków
   EN: Nominable Egoshard Crates
   PL:
684. [Interfejs i ustawienia [mainui_manaUsage] — tekst] 정신 소모량
   źródło: MainUIText.json :: dataList[id=mainui_manaUsage].content
   limit: do 120 znaków
   EN: Sanity Cost
   PL:
685. [Interfejs i ustawienia [mainui_abnormality_analysis_level] — tekst] 환상 해석 단계
   źródło: MainUIText.json :: dataList[id=mainui_abnormality_analysis_level].content
   limit: do 120 znaków
   EN: Current Tier
   PL:
686. [Interfejs i ustawienia [mainui_analysis] — tekst] 해석
   źródło: MainUIText.json :: dataList[id=mainui_analysis].content
   limit: do 120 znaków
   EN: Threadspin
   PL:
687. [Interfejs i ustawienia [mainui_abnormality_analysis] — tekst] 환상 해석
   źródło: MainUIText.json :: dataList[id=mainui_abnormality_analysis].content
   limit: do 120 znaków
   EN: Threadspinning
   PL:
688. [Interfejs i ustawienia [mainui_receive] — tekst] 수령
   źródło: MainUIText.json :: dataList[id=mainui_receive].content
   limit: do 120 znaków
   EN: Claim
   PL:
689. [Interfejs i ustawienia [mainui_dungeon_finished_reward] — tekst] 탐사 종료 보상
   źródło: MainUIText.json :: dataList[id=mainui_dungeon_finished_reward].content
   limit: do 120 znaków
   EN: Exploration Reward
   PL:
690. [Interfejs i ustawienia [mainui_passive] — tekst] 패시브
   źródło: MainUIText.json :: dataList[id=mainui_passive].content
   limit: do 120 znaków
   EN: Passives
   PL:
691. [Interfejs i ustawienia [mainui_support_passive] — tekst] 서포트 패시브
   źródło: MainUIText.json :: dataList[id=mainui_support_passive].content
   limit: do 120 znaków
   EN: Support
   PL:
692. [Interfejs i ustawienia [mainui_synchronization] — tekst] 동기화
   źródło: MainUIText.json :: dataList[id=mainui_synchronization].content
   limit: do 120 znaków
   EN: Uptie
   PL:
693. [Interfejs i ustawienia [mainui_personality_synchronization_level] — tekst] 인격 동기화 레벨
   źródło: MainUIText.json :: dataList[id=mainui_personality_synchronization_level].content
   limit: do 120 znaków
   EN: Uptie Tier
   PL:
694. [Interfejs i ustawienia [mainui_owned] — tekst] 보유
   źródło: MainUIText.json :: dataList[id=mainui_owned].content
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Interfejs i ustawienia [mainui_growth_level_limited] — tekst] Lv. {0} 이상 사용 불가
   źródło: MainUIText.json :: dataList[id=mainui_growth_level_limited].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cannot use at Lv. {0}+
   PL:
696. [Interfejs i ustawienia [mainui_stats_attack] — tekst] 공격력
   źródło: MainUIText.json :: dataList[id=mainui_stats_attack].content
   limit: do 120 znaków
   EN: ATK
   PL:
697. [Interfejs i ustawienia [mainui_mailbox_receive_all] — tekst] 일괄 수령
   źródło: MainUIText.json :: dataList[id=mainui_mailbox_receive_all].content
   limit: do 120 znaków
   EN: Claim All
   PL:
698. [Interfejs i ustawienia [mainui_mailbox_receive_history] — tekst] 수령 이력
   źródło: MainUIText.json :: dataList[id=mainui_mailbox_receive_history].content
   limit: do 120 znaków
   EN: History
   PL:
699. [Interfejs i ustawienia [mainui_remain_days] — tekst] {0}일 남음
   źródło: MainUIText.json :: dataList[id=mainui_remain_days].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} days left
   PL:
700. [Interfejs i ustawienia [mainui_mail_remains_count] — tekst] 보관중인 우편
   źródło: MainUIText.json :: dataList[id=mainui_mail_remains_count].content
   limit: do 120 znaków
   EN: Inbox
   PL:
701. [Interfejs i ustawienia [mainui_mail_warning] — tekst] ※ 최대 100개 까지 보관이 가능하며, 기한이 지난 선물은 <color=#990000>삭제</color>됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_mail_warning].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>
   EN: ※ Maximum capacity is 100; expired mail will be <color=#990000>deleted</color>.
   PL:
702. [Interfejs i ustawienia [mainui_mail_warning2] — tekst] ※ 우편함에서 수령한 아이템은 청약 철회가 제한될 수 있습니다.
   źródło: MainUIText.json :: dataList[id=mainui_mail_warning2].content
   limit: do 120 znaków
   EN: ※ Items claimed at the mailbox may be subject to cancellation restrictions.
   PL:
703. [Interfejs i ustawienia [main_information] — tekst] 정보
   źródło: MainUIText.json :: dataList[id=main_information].content
   limit: do 120 znaków
   EN: Info
   PL:
704. [Interfejs i ustawienia [main_until] — tekst] 까지
   źródło: MainUIText.json :: dataList[id=main_until].content
   (powtórzenie elementu 654 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Interfejs i ustawienia [mainui_synchronization_grade] — tekst] 동기화 단계
   źródło: MainUIText.json :: dataList[id=mainui_synchronization_grade].content
   (powtórzenie elementu 307 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Interfejs i ustawienia [mainui_organization] — tekst] 편성
   źródło: MainUIText.json :: dataList[id=mainui_organization].content
   limit: do 120 znaków
   EN: TEAMS
   PL:
707. [Interfejs i ustawienia [story_ui_log_popup] — tekst] 로그
   źródło: MainUIText.json :: dataList[id=story_ui_log_popup].content
   limit: do 120 znaków
   EN: Log
   PL:
708. [Interfejs i ustawienia [mail_box_attachments] — tekst] 우편 내용물
   źródło: MainUIText.json :: dataList[id=mail_box_attachments].content
   limit: do 120 znaków
   EN: Content
   PL:
709. [Interfejs i ustawienia [mail_box_unseal_result] — tekst] 우편 보상
   źródło: MainUIText.json :: dataList[id=mail_box_unseal_result].content
   limit: do 120 znaków
   EN: Parcel Received
   PL:
710. [Interfejs i ustawienia [item_use_result] — tekst] 아이템 사용 결과
   źródło: MainUIText.json :: dataList[id=item_use_result].content
   limit: do 120 znaków
   EN: Item Used
   PL:
711. [Interfejs i ustawienia [giving_up_story_dungeon_title] — tekst] 스토리 던전 포기
   źródło: MainUIText.json :: dataList[id=giving_up_story_dungeon_title].content
   limit: do 120 znaków
   EN: Forfeit Story Dungeon
   PL:
712. [Interfejs i ustawienia [giving_up_story_dungeon_content] — tekst] 현재 {0}장 스토리 던전을 진행 중입니다.\n진행을 포기하고 새로운 던전에 도전하시겠습니까?
   źródło: MainUIText.json :: dataList[id=giving_up_story_dungeon_content].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: You’re currently exploring Episode {0}’s Story Dungeon.\nForfeit your progress and enter a new dungeon?
   PL:
713. [Interfejs i ustawienia [mainui_all] — tekst] 전체
   źródło: MainUIText.json :: dataList[id=mainui_all].content
   limit: do 120 znaków
   EN: All
   PL:
714. [Interfejs i ustawienia [mainui_opened] — tekst] 개방
   źródło: MainUIText.json :: dataList[id=mainui_opened].content
   limit: do 120 znaków
   EN: Open
   PL:
715. [Interfejs i ustawienia [mainui_not_opened] — tekst] 미개방
   źródło: MainUIText.json :: dataList[id=mainui_not_opened].content
   limit: do 120 znaków
   EN: Locked
   PL:
716. [Interfejs i ustawienia [mainui_buy] — tekst] 구매
   źródło: MainUIText.json :: dataList[id=mainui_buy].content
   limit: do 120 znaków
   EN: Confirm
   PL:
717. [Interfejs i ustawienia [mainui_use] — tekst] 사용
   źródło: MainUIText.json :: dataList[id=mainui_use].content
   limit: do 120 znaków
   EN: Use
   PL:
718. [Interfejs i ustawienia [mainui_consume] — tekst] 소모
   źródło: MainUIText.json :: dataList[id=mainui_consume].content
   limit: do 120 znaków
   EN: Consumable
   PL:
719. [Interfejs i ustawienia [mainui_currencies] — tekst] 재화
   źródło: MainUIText.json :: dataList[id=mainui_currencies].content
   limit: do 120 znaków
   EN: Currency
   PL:
720. [Interfejs i ustawienia [mainui_inventory] — tekst] 인벤토리
   źródło: MainUIText.json :: dataList[id=mainui_inventory].content
   limit: do 120 znaków
   EN: Inventory
   PL:
721. [Interfejs i ustawienia [mainui_awaken_requirement_amount] — tekst] 필요 재화 수량
   źródło: MainUIText.json :: dataList[id=mainui_awaken_requirement_amount].content
   limit: do 120 znaków
   EN: Currency Req.
   PL:
722. [Interfejs i ustawienia [mainui_passive_skill_addition] — tekst] 패시브 스킬 추가
   źródło: MainUIText.json :: dataList[id=mainui_passive_skill_addition].content
   limit: do 120 znaków
   EN: Passives Unlocked
   PL:
723. [Interfejs i ustawienia [mainui_synergy_addition] — tekst] 시너지 획득
   źródło: MainUIText.json :: dataList[id=mainui_synergy_addition].content
   limit: do 120 znaków
   EN: Synergy Unlocked
   PL:
724. [Interfejs i ustawienia [mainui_ego_awaken_skill_reinforcement] — tekst] E.G.O 각성 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_skill_reinforcement].content
   limit: do 120 znaków
   EN: E.G.O Awakening Upgraded
   PL:
725. [Interfejs i ustawienia [mainui_ego_erosion_skill_reinforcement] — tekst] E.G.O 침식 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_erosion_skill_reinforcement].content
   limit: do 120 znaków
   EN: E.G.O Corrosion Upgraded
   PL:
726. [Interfejs i ustawienia [mainui_lack_of_material_amount] — tekst] 끈이 부족합니다.
   źródło: MainUIText.json :: dataList[id=mainui_lack_of_material_amount].content
   limit: do 120 znaków
   EN: Not enough Thread.
   PL:
727. [Interfejs i ustawienia [mainui_move] — tekst] 이동
   źródło: MainUIText.json :: dataList[id=mainui_move].content
   limit: do 120 znaków
   EN: Go
   PL:
728. [Interfejs i ustawienia [mainui_move_to_twine_store] — tekst] 파편::끈 교환기 이동
   źródło: MainUIText.json :: dataList[id=mainui_move_to_twine_store].content
   limit: do 120 znaków
   EN: Shard::Thread Exchange
   PL:
729. [Interfejs i ustawienia [mainui_move_to_twine_store_question] — tekst] 끈이 부족합니다.\n파편::끈 교환기로 이동하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_move_to_twine_store_question].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Insufficient Thread.\nGo to the Shard::Thread Exchange?
   PL:
730. [Interfejs i ustawienia [mainui_confirm_of_purchased_twine] — tekst] 끈 {0}개를 구입하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_confirm_of_purchased_twine].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Convert to {0} Thread?
   PL:
731. [Interfejs i ustawienia [mainui_result_of_purchased_twine] — tekst] 끈 {0}개를 구입하였습니다.
   źródło: MainUIText.json :: dataList[id=mainui_result_of_purchased_twine].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Acquired {0} Thread.
   PL:
732. [Interfejs i ustawienia [mainui_personality_awaken_completion] — tekst] 인격 동기화 완료
   źródło: MainUIText.json :: dataList[id=mainui_personality_awaken_completion].content
   limit: do 120 znaków
   EN: Identity Uptied
   PL:
733. [Interfejs i ustawienia [mainui_ego_awaken_completion] — tekst] 환상 해석 완료
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_completion].content
   limit: do 120 znaków
   EN: E.G.O Threadspun
   PL:
734. [Interfejs i ustawienia [mainui_new_skill_acquisition] — tekst] 신규 스킬 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_skill_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Skill: [{0}]
   PL:
735. [Interfejs i ustawienia [mainui_new_passive_skill_acquisition] — tekst] 신규 패시브 스킬 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_passive_skill_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Passive: [{0}]
   PL:
736. [Interfejs i ustawienia [mainui_new_synergy_acquisition] — tekst] 시너지 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_synergy_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Synergy: [{0}]
   PL:
737. [Interfejs i ustawienia [mainui_new_battle_passive_acquisition] — tekst] 신규 전투 패시브 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_battle_passive_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Combat Passive: [{0}]
   PL:
738. [Interfejs i ustawienia [mainui_new_support_passive_acquisition] — tekst] 신규 서포트 패시브 [{0}] 획득
   źródło: MainUIText.json :: dataList[id=mainui_new_support_passive_acquisition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: New Support Passive: [{0}]
   PL:
739. [Interfejs i ustawienia [mainui_skill_reinforcement] — tekst] 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_skill_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill Enhanced: [{0}]
   PL:
740. [Interfejs i ustawienia [mainui_unlock_personality_story] — tekst] [{0}]의 이야기 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_personality_story].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Story of [{0}] Unlocked
   PL:
741. [Interfejs i ustawienia [mainui_ego_awaken_skill_name_reinforcement] — tekst] E.G.O 각성 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_awaken_skill_name_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Awakening [{0}] Upgraded
   PL:
742. [Interfejs i ustawienia [mainui_ego_erosion_skill_name_reinforcement] — tekst] E.G.O 침식 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_ego_erosion_skill_name_reinforcement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Corrosion [{0}] Upgraded
   PL:
743. [Interfejs i ustawienia [mainui_specific_level_achievement] — tekst] LV{0} 달성
   źródło: MainUIText.json :: dataList[id=mainui_specific_level_achievement].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reach Lv. {0}
   PL:
744. [Interfejs i ustawienia [mainui_personality_awaken_level_up_condition] — tekst] 동기화 {0}단계 조건
   źródło: MainUIText.json :: dataList[id=mainui_personality_awaken_level_up_condition].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie Tier {0} Requirements
   PL:
745. [Interfejs i ustawienia [mainui_battle_passsive_addition] — tekst] 전투 패시브 추가
   źródło: MainUIText.json :: dataList[id=mainui_battle_passsive_addition].content
   limit: do 120 znaków
   EN: Combat Passives Unlocked
   PL:
746. [Interfejs i ustawienia [mainui_support_passsive_addition] — tekst] 서포트 패시브 추가
   źródło: MainUIText.json :: dataList[id=mainui_support_passsive_addition].content
   limit: do 120 znaków
   EN: Support Passives Unlocked
   PL:
747. [Interfejs i ustawienia [mainui_check_purchase] — tekst] 구매 확인
   źródło: MainUIText.json :: dataList[id=mainui_check_purchase].content
   limit: do 120 znaków
   EN: Confirm Purchase
   PL:
748. [Interfejs i ustawienia [mainui_acquire_banner] — tekst] 배너 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquire_banner].content
   limit: do 120 znaków
   EN: Banner Acquired
   PL:
749. [Interfejs i ustawienia [mainui_purchase_complete] — tekst] 구매 완료
   źródło: MainUIText.json :: dataList[id=mainui_purchase_complete].content
   limit: do 120 znaków
   EN: Purchased
   PL:
750. [Interfejs i ustawienia [mainui_activation] — tekst] 활성화
   źródło: MainUIText.json :: dataList[id=mainui_activation].content
   limit: do 120 znaków
   EN: ACTIVATED
   PL:
751. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin] — tekst] 엔케팔린이 부족합니다.\n엔케팔린 충전 창으로 이동하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Insufficient Enkephalin.\nWould you like to recharge your Enkephalin?
   PL:
752. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin_box] — tekst] 엔케팔린 박스가 부족합니다.\n엔케팔린 박스를 구매하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin_box].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You don’t have enough Enkephalin Boxes.\nWould you like to go purchase some?
   PL:
753. [Interfejs i ustawienia [mainui_rewatching-stage-story] — tekst] 스토리 다시보기
   źródło: MainUIText.json :: dataList[id=mainui_rewatching-stage-story].content
   limit: do 120 znaków
   EN: Rewatch Story
   PL:
754. [Interfejs i ustawienia [mainui_before_battle] — tekst] 전투 전
   źródło: MainUIText.json :: dataList[id=mainui_before_battle].content
   limit: do 120 znaków
   EN: Pre-battle
   PL:
755. [Interfejs i ustawienia [mainui_after_battle] — tekst] 전투 후
   źródło: MainUIText.json :: dataList[id=mainui_after_battle].content
   limit: do 120 znaków
   EN: Post-battle
   PL:
756. [Interfejs i ustawienia [mainui_story] — tekst] 스토리
   źródło: MainUIText.json :: dataList[id=mainui_story].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Interfejs i ustawienia [Get_Reward] — tekst] 보상 획득
   źródło: MainUIText.json :: dataList[id=Get_Reward].content
   limit: do 120 znaków
   EN: Rewards Earned
   PL:
758. [Interfejs i ustawienia [mainui_user_exp] — tekst] 관리자 경험치
   źródło: MainUIText.json :: dataList[id=mainui_user_exp].content
   limit: do 120 znaków
   EN: Manager EXP
   PL:
759. [Interfejs i ustawienia [mainui_chapter_progress] — tekst] 챕터 진행도
   źródło: MainUIText.json :: dataList[id=mainui_chapter_progress].content
   limit: do 120 znaków
   EN: Progress
   PL:
760. [Interfejs i ustawienia [mainui_ex_clear_progress] — tekst] EX-클리어
   źródło: MainUIText.json :: dataList[id=mainui_ex_clear_progress].content
   limit: do 120 znaków
   EN: EX Cleared
   PL:
761. [Interfejs i ustawienia [mainui_notice_spend_free_lunacy_first] — tekst] ※무료 광기부터 먼저 사용됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_notice_spend_free_lunacy_first].content
   limit: do 120 znaków
   EN: ※ Free Lunacy is used first.
   PL:
762. [Interfejs i ustawienia [mainui_notice_require_lunacy] — tekst] ※광기가 부족합니다.
   źródło: MainUIText.json :: dataList[id=mainui_notice_require_lunacy].content
   limit: do 120 znaków
   EN: ※ Not enough Lunacy.
   PL:
763. [Interfejs i ustawienia [mainui_progress_of_spend] — tekst] {0}을(를) 소비하여 {1}을(를) 진행합니다.
   źródło: MainUIText.json :: dataList[id=mainui_progress_of_spend].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Spend {0} to proceed with {1}?
   PL:
764. [Interfejs i ustawienia [game_setting] — tekst] 게임 설정
   źródło: MainUIText.json :: dataList[id=game_setting].content
   limit: do 120 znaków
   EN: Config
   PL:
765. [Interfejs i ustawienia [level] — tekst] 레벨
   źródło: MainUIText.json :: dataList[id=level].content
   limit: do 120 znaków
   EN: Level
   PL:
766. [Interfejs i ustawienia [name] — tekst] 이름
   źródło: MainUIText.json :: dataList[id=name].content
   limit: do 120 znaków
   EN: Name
   PL:
767. [Interfejs i ustawienia [order_of_acquisition] — tekst] 획득 순
   źródło: MainUIText.json :: dataList[id=order_of_acquisition].content
   (powtórzenie elementu 311 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Interfejs i ustawienia [tolerance] — tekst] 내성
   źródło: MainUIText.json :: dataList[id=tolerance].content
   limit: do 120 znaków
   EN: Resist
   PL:
769. [Interfejs i ustawienia [outstanding_staff] — tekst] 우수 사원
   źródło: MainUIText.json :: dataList[id=outstanding_staff].content
   limit: do 120 znaków
   EN: Most Valued Employee
   PL:
770. [Interfejs i ustawienia [total_damage_contribution] — tekst] 총 대미지 기여량
   źródło: MainUIText.json :: dataList[id=total_damage_contribution].content
   limit: do 120 znaków
   EN: Damage Contributed
   PL:
771. [Interfejs i ustawienia [deal_damage] — tekst] 가한 피해량
   źródło: MainUIText.json :: dataList[id=deal_damage].content
   limit: do 120 znaków
   EN: Dealt
   PL:
772. [Interfejs i ustawienia [taken_damage] — tekst] 받은 피해량
   źródło: MainUIText.json :: dataList[id=taken_damage].content
   limit: do 120 znaków
   EN: Taken
   PL:
773. [Interfejs i ustawienia [user_level_up_notice] — tekst] 관리자 레벨이 상승했습니다.
   źródło: MainUIText.json :: dataList[id=user_level_up_notice].content
   limit: do 120 znaków
   EN: Manager Level Increased!
   PL:
774. [Interfejs i ustawienia [increase_maxium_enkephalin] — tekst] 엔케팔린 최대치 상승
   źródło: MainUIText.json :: dataList[id=increase_maxium_enkephalin].content
   limit: do 120 znaków
   EN: Enkephalin Capacity Up!
   PL:
775. [Interfejs i ustawienia [recharge_enkephalin_notice] — tekst] 엔케팔린이 충전되었습니다.
   źródło: MainUIText.json :: dataList[id=recharge_enkephalin_notice].content
   limit: do 120 znaków
   EN: Enkephalin has been refilled.
   PL:
776. [Interfejs i ustawienia [gacha_extract_multiple] — tekst] {0}회 추출
   źródło: MainUIText.json :: dataList[id=gacha_extract_multiple].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Extract {0}
   PL:
777. [Interfejs i ustawienia [number_of_times] — tekst] 회
   źródło: MainUIText.json :: dataList[id=number_of_times].content
   limit: do 120 znaków
   EN: Time(s)
   PL:
778. [Interfejs i ustawienia [number_of_remain_extract_times] — tekst] 남은 추출 횟수
   źródło: MainUIText.json :: dataList[id=number_of_remain_extract_times].content
   limit: do 120 znaków
   EN: Extractions Remaining
   PL:
779. [Interfejs i ustawienia [notice_of_remain_extract_chance] — tekst] {0}회 이내 3성 인격 또는 E.G.O 확정 등장
   źródło: MainUIText.json :: dataList[id=notice_of_remain_extract_chance].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 3★ Identity or E.G.O assured in {0} Extractions
   PL:
780. [Interfejs i ustawienia [mainui_settings] — tekst] 설정
   źródło: MainUIText.json :: dataList[id=mainui_settings].content
   (powtórzenie elementu 7 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
781. [Interfejs i ustawienia [mainui_environment_settings] — tekst] 환경 설정
   źródło: MainUIText.json :: dataList[id=mainui_environment_settings].content
   limit: do 120 znaków
   EN: Settings
   PL:
782. [Interfejs i ustawienia [mainui_back] — tekst] 돌아가기
   źródło: MainUIText.json :: dataList[id=mainui_back].content
   limit: do 120 znaków
   EN: Return
   PL:
783. [Interfejs i ustawienia [mainui_quit_game] — tekst] 게임 종료
   źródło: MainUIText.json :: dataList[id=mainui_quit_game].content
   limit: do 120 znaków
   EN: Quit Game
   PL:
784. [Interfejs i ustawienia [mainui_acquisition] — tekst] 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquisition].content
   limit: do 120 znaków
   EN: Owned
   PL:
785. [Interfejs i ustawienia [mainui_not_acquisition] — tekst] 미획득
   źródło: MainUIText.json :: dataList[id=mainui_not_acquisition].content
   limit: do 120 znaków
   EN: Unowned
   PL:
786. [Interfejs i ustawienia [mainui_no_record] — tekst] 획득 기록 없음
   źródło: MainUIText.json :: dataList[id=mainui_no_record].content
   limit: do 120 znaków
   EN: No Acquisition Records
   PL:
787. [Interfejs i ustawienia [resume] — tekst] 재개
   źródło: MainUIText.json :: dataList[id=resume].content
   limit: do 120 znaków
   EN: Resume
   PL:
788. [Interfejs i ustawienia [mainui_entering] — tekst] 입장하기
   źródło: MainUIText.json :: dataList[id=mainui_entering].content
   limit: do 120 znaków
   EN: Enter
   PL:
789. [Interfejs i ustawienia [mainui_open_after_clear] — tekst] {0}장 클리어 후 개방
   źródło: MainUIText.json :: dataList[id=mainui_open_after_clear].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Ch. {0} to Unlock
   PL:
790. [Interfejs i ustawienia [mainui_organization_sharp] — tekst] 편성 #{0}
   źródło: MainUIText.json :: dataList[id=mainui_organization_sharp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Team #{0}
   PL:
791. [Interfejs i ustawienia [mainui_participant_count] — tekst] 편성 편집
   źródło: MainUIText.json :: dataList[id=mainui_participant_count].content
   limit: do 120 znaków
   EN: Edit Team
   PL:
792. [Interfejs i ustawienia [mainui_edit] — tekst] 편집
   źródło: MainUIText.json :: dataList[id=mainui_edit].content
   limit: do 120 znaków
   EN: Edit
   PL:
793. [Interfejs i ustawienia [mainui_unlock_condition_by_personality_awaken_level] — tekst] 동기화 {0}단계 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_condition_by_personality_awaken_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Unlocked at Tier {0}
   PL:
794. [Interfejs i ustawienia [skill_growth_value] — tekst] 성장계수
   źródło: MainUIText.json :: dataList[id=skill_growth_value].content
   limit: do 120 znaków
   EN: Growth
   PL:
795. [Interfejs i ustawienia [gacha_history_notice] — tekst] ※지난 {0}일간 이력이 최대 {1}건 표기됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_history_notice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: ※ Up to {1} cases over the last {0} days are displayed.
   PL:
796. [Interfejs i ustawienia [gacha_history_empty] — tekst] 추출 이력이 없습니다.
   źródło: MainUIText.json :: dataList[id=gacha_history_empty].content
   limit: do 120 znaków
   EN: No extraction record to display.
   PL:
797. [Interfejs i ustawienia [own] — tekst] 소지
   źródło: MainUIText.json :: dataList[id=own].content
   limit: do 120 znaków
   EN: Owned
   PL:
798. [Interfejs i ustawienia [gacha_category] — tekst] 추출 종류
   źródło: MainUIText.json :: dataList[id=gacha_category].content
   limit: do 120 znaków
   EN: Category
   PL:
799. [Interfejs i ustawienia [gacha_time] — tekst] 추출 일시
   źródło: MainUIText.json :: dataList[id=gacha_time].content
   limit: do 120 znaków
   EN: Date
   PL:
800. [Interfejs i ustawienia [used_currencies] — tekst] 사용 재화
   źródło: MainUIText.json :: dataList[id=used_currencies].content
   limit: do 120 znaków
   EN: Currency Used
   PL:
801. [Interfejs i ustawienia [mainui_ask_purchase_enkephalin_module] — tekst] 엔케팔린 모듈이 부족합니다.\n엔케팔린 모듈을 제작하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_purchase_enkephalin_module].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You don’t have enough Enkephalin Modules.\nWould you like to go assemble some?
   PL:
802. [Interfejs i ustawienia [list] — tekst] 목록
   źródło: MainUIText.json :: dataList[id=list].content
   limit: do 120 znaków
   EN: List
   PL:
803. [Interfejs i ustawienia [rank] — tekst] 등급
   źródło: MainUIText.json :: dataList[id=rank].content
   limit: do 120 znaków
   EN: Rarity
   PL:
804. [Interfejs i ustawienia [probability] — tekst] 확률
   źródło: MainUIText.json :: dataList[id=probability].content
   limit: do 120 znaków
   EN: Odds
   PL:
805. [Interfejs i ustawienia [gacha_rate_label] — tekst] 추출 확률 안내
   źródło: MainUIText.json :: dataList[id=gacha_rate_label].content
   limit: do 120 znaków
   EN: Extraction Probabilities
   PL:
806. [Interfejs i ustawienia [gacha_rate_title_ten1] — tekst] [10회 추출 (1~9번째 추출)]: [1회 추출]과 동일
   źródło: MainUIText.json :: dataList[id=gacha_rate_title_ten1].content
   limit: do 120 znaków
   EN: [10 Extractions (1st-9th)]: Same rates as [1 Extraction]
   PL:
807. [Interfejs i ustawienia [gacha_rate_title_ten2] — tekst] [10회 추출 (10번째 추출)]
   źródło: MainUIText.json :: dataList[id=gacha_rate_title_ten2].content
   limit: do 120 znaków
   EN: [10 Extractions (10th)]
   PL:
808. [Interfejs i ustawienia [gacha_rate_info_intro1] — tekst] 「한국게임산업협회의 자율 규제」에 따라 확률형 아이템의 상세 확률을 안내드립니다.\n\n개별 등장 확률은 소수점 5번째 자리에서 반올림한 수치이며, 실제 합산 확률은 100%에 맞추어 적용됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1].content
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In compliance with the 「Voluntary Restraint Guidelines of Korea Association of Game Industry」, detailed rates for chance-based items are disclosed here.\n\nIndividual rates are rounded up from the fifth digit after the decimal point. The actual sum is applied as 100%.
   PL:
809. [Interfejs i ustawienia [gacha_rate_info_intro2] — tekst] 10회 추출을 진행할 경우에는 2성 이상의 인격 1명을 확정으로 획득합니다.\n\n이에 따라 10번째 추출의 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro2].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In [10 Extractions], at least 1 Identity with a rarity of 2★ or higher will be extracted.\n\nThe table for the 10th Extraction is as follows:
   PL:
810. [Interfejs i ustawienia [gacha_rate_info_ego1] — tekst] 상단에 있는 추출 확률에 따라 하단에 명시된 목록에 있는 인격과 E.G.O를 획득할 수 있습니다.\n\n획득할 수 있는 인격과 E.G.O는 특정 시즌에 따라 변경될 수 있으며, 이러한 경우에는 변경 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_ego1].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Below is the list of Identities and E.G.O you can obtain following the aforementioned rates.\n\nThe list may change in certain seasons; upcoming changes to the reward tables will be announced in advance.
   PL:
811. [Interfejs i ustawienia [gacha_rate_info_ego2] — tekst] <b>추출 진행 시 E.G.O는 비복원 추출로 진행되며, 추출이나 자판기 또는 보상을 수령하여 획득한 E.G.O는 추출을 통해 획득할 수 있는 목록에서 제외됩니다.</b>\n\n획득할 수 있는 목록에 E.G.O가 존재한다면 추출을 통해 E.G.O를 획득할 확률은 변동되지 않습니다. 이에 따라 E.G.O를 획득할수록 E.G.O의 개별 획득 확률은 증가합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_ego2].content
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: <b>, </b>, \n
   EN: <b>E.G.O is extracted non-repetitively; E.G.O acquired through any means, including Extraction, Dispenser, and redemption from the mailbox, will be excluded from the Extraction table.</b>\n\nAs long as there is E.G.O remaining in the table of possible results, the chance of extracting E.G.O in Extraction does not change. Therefore, the chance of acquiring specific E.G.O will increase as more extractions are performed.
   PL:
812. [Interfejs i ustawienia [gacha_rate_info_complete1] — tekst] 목록 내에 있는 모든 E.G.O를 획득하여 더 이상 목록에 E.G.O가 존재하지 않게 된다면 1회 추출 시와 10회 추출 시의 등장 확률은 다음과 같이 변경됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete1].content
   limit: do 230 znaków
   EN: If there is no E.G.O remaining in the table due to the user acquiring all of them, the rates for [1 Extraction] and [10 Extraction] will change accordingly to the following:
   PL:
813. [Interfejs i ustawienia [gacha_rate_info_complete2] — tekst] 특정 추출 인격 또는 E.G.O가 등장할 경우에는 특정 추출 확률이 적용되어 추출 확률이 증가합니다.\n\n특정 추출 확률 인격이 등장할 경우, 해당 특정 추출 인격과 동일한 등급 인격이 등장할 확률의 50%를 동일한 단계의 특정 추출 인격 수만큼 균등하게 분배합니다.\n\n특정 추출 대상이 아닌 인격도 마찬가지로 등장할 확률의 50%을 특정 추출 대상이 아닌 인격 수만큼 균등하게 분배합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete2].content
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In Target Extractions, certain Identities and E.G.O have higher extraction rates.\n\nTarget Identities account for 50% of the probabilities for their respective rarities; the rates are evenly shared among them.\n\nThe other 50% of probabilities are evenly distributed between the non-targeted Identities in the table.
   PL:
814. [Interfejs i ustawienia [gacha_rate_info_complete3] — tekst] 위 내용은 특정 추출 E.G.O의 경우에도 동일하게 동작합니다.\n\n특정 추출 확률이 적용되어도 각 추출의 경우에 대한 등장 확률은 변동되지 않습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_complete3].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The same applies to Target E.G.O.\n\nChanges in probabilities for Target Extractions do not affect the chances of items of certain types and rarities appearing.
   PL:
815. [Interfejs i ustawienia [gacha_rate_info_piece1] — tekst] ★ 자아 파편\n이미 보유한 인격 또는 E.G.O를 중복하여 획득할 경우에는 분류와 단계에 따라 각 캐릭터의 자아 파편으로 전환되어 획득하게 됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece1].content
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: ★ Egoshards\nWhen you extract an Identity or E.G.O you already own, you will get Egoshards of the character, its quantity depending on the item’s type and rarity.
   PL:
816. [Interfejs i ustawienia [gacha_rate_info_piece2] — tekst] 획득한 자아 파편은 미리 공지한 기간 동안 사용할 수 있으며, 보유한 자아 파편의 50%만큼 다음 시즌으로 이월됩니다.\n\n이월되지 않은 자아 파편은 끈으로 전환됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece2].content
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Egoshards can only be used for a set period. When the expiration date arrives, 50% of the Egoshards in possession are carried over to the next season.\n\nThe remaining Egoshards are converted to Thread.
   PL:
817. [Interfejs i ustawienia [gacha_rate_info_piece3] — tekst] 위 내용은 자아 파편 상자의 경우에도 동일하게 동작합니다.\n\n이러한 경우에는 다음 시즌이 시작되어 자아 파편과 자아 파편 상자가 이월되기 전에 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_piece3].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The same applies to Egoshard Crates.\n\nPlayers will be notified of the upcoming season change and expiration of Egoshards and Egoshard Crates sometime before the expiration date.
   PL:
818. [Interfejs i ustawienia [personality_preview_notice] — tekst] 본 화면에는 인격의 최대 레벨, 동기화 단계가 표시됩니다.
   źródło: MainUIText.json :: dataList[id=personality_preview_notice].content
   limit: do 120 znaków
   EN: The Identity’s stats at max level and Uptie tier are displayed here.
   PL:
819. [Interfejs i ustawienia [ego_preview_notice] — tekst] 본 화면에는 E.G.O의 최대 환상 해석 단계가 표시됩니다.
   źródło: MainUIText.json :: dataList[id=ego_preview_notice].content
   limit: do 120 znaków
   EN: The E.G.O is displayed at its max tier here.
   PL:
820. [Interfejs i ustawienia [season_1] — tekst] 시즌 1
   źródło: MainUIText.json :: dataList[id=season_1].content
   limit: do 120 znaków
   EN: Season 1
   PL:
821. [Interfejs i ustawienia [commonly] — tekst] 통상
   źródło: MainUIText.json :: dataList[id=commonly].content
   limit: do 120 znaków
   EN: Regular
   PL:
822. [Interfejs i ustawienia [notice_external_website] — tekst] 외부 웹사이트로 이동합니다.
   źródło: MainUIText.json :: dataList[id=notice_external_website].content
   limit: do 120 znaków
   EN: Move to an external website.
   PL:
823. [Interfejs i ustawienia [pass_level] — tekst] 패스 레벨
   źródło: MainUIText.json :: dataList[id=pass_level].content
   limit: do 120 znaków
   EN: Pass Level
   PL:
824. [Interfejs i ustawienia [normal_reward] — tekst] 일반 보상
   źródło: MainUIText.json :: dataList[id=normal_reward].content
   limit: do 120 znaków
   EN: Regular Reward
   PL:
825. [Interfejs i ustawienia [limbus_pass_reward] — tekst] 림버스 패스 보상
   źródło: MainUIText.json :: dataList[id=limbus_pass_reward].content
   limit: do 120 znaków
   EN: Limbus Pass Reward
   PL:
826. [Interfejs i ustawienia [loading_battlehint] — tekst] 전투 팁
   źródło: MainUIText.json :: dataList[id=loading_battlehint].content
   (powtórzenie elementu 478 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Interfejs i ustawienia [status_up] — tekst] 스테이터스 증가
   źródło: MainUIText.json :: dataList[id=status_up].content
   limit: do 120 znaków
   EN: Stats Increased
   PL:
828. [Interfejs i ustawienia [active_skill_acquired] — tekst] 액티브 스킬 추가
   źródło: MainUIText.json :: dataList[id=active_skill_acquired].content
   limit: do 120 znaków
   EN: Skills Gained
   PL:
829. [Interfejs i ustawienia [active_skill_reinforcement] — tekst] 액티브 스킬 강화
   źródło: MainUIText.json :: dataList[id=active_skill_reinforcement].content
   limit: do 120 znaków
   EN: Skills Upgraded
   PL:
830. [Interfejs i ustawienia [progress_ego_gacksung] — tekst] 해석 진행
   źródło: MainUIText.json :: dataList[id=progress_ego_gacksung].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Progress\nThreadspin
   PL:
831. [Interfejs i ustawienia [skill_with_index] — tekst] 스킬{0}
   źródło: MainUIText.json :: dataList[id=skill_with_index].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill {0}
   PL:
832. [Interfejs i ustawienia [mail_date] — tekst] 수령 일시
   źródło: MainUIText.json :: dataList[id=mail_date].content
   limit: do 120 znaków
   EN: Date
   PL:
833. [Interfejs i ustawienia [mail_sender] — tekst] 보낸 이
   źródło: MainUIText.json :: dataList[id=mail_sender].content
   limit: do 120 znaków
   EN: Sender
   PL:
834. [Interfejs i ustawienia [mail_history_notice] — tekst] ※최대 {0}개의 수령 이력이 표시됩니다.
   źródło: MainUIText.json :: dataList[id=mail_history_notice].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ Up to {0} claimed items will be displayed in the history.
   PL:
835. [Interfejs i ustawienia [cant_receive_mail_all_tilte] — tekst] 수령 불가
   źródło: MainUIText.json :: dataList[id=cant_receive_mail_all_tilte].content
   limit: do 120 znaków
   EN: Cannot Claim
   PL:
836. [Interfejs i ustawienia [cant_receive_mail_all_main] — tekst] 일괄 수령 가능한 우편물 없음
   źródło: MainUIText.json :: dataList[id=cant_receive_mail_all_main].content
   limit: do 120 znaków
   EN: No mail available to claim with “Claim All”
   PL:
837. [Interfejs i ustawienia [attached_item] — tekst] 첨부 아이템
   źródło: MainUIText.json :: dataList[id=attached_item].content
   limit: do 120 znaków
   EN: Attached
   PL:
838. [Interfejs i ustawienia [inventory_category_all] — tekst] 전체
   źródło: MainUIText.json :: dataList[id=inventory_category_all].content
   (powtórzenie elementu 713 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Interfejs i ustawienia [inventory_category_normal] — tekst] 기본
   źródło: MainUIText.json :: dataList[id=inventory_category_normal].content
   limit: do 120 znaków
   EN: Basic
   PL:
840. [Interfejs i ustawienia [inventory_category_consumable] — tekst] 소모품
   źródło: MainUIText.json :: dataList[id=inventory_category_consumable].content
   limit: do 120 znaków
   EN: Consumables
   PL:
841. [Interfejs i ustawienia [inventory_category_pieces] — tekst] 파편
   źródło: MainUIText.json :: dataList[id=inventory_category_pieces].content
   limit: do 120 znaków
   EN: Egoshards
   PL:
842. [Interfejs i ustawienia [enkephalin_injection_complete] — tekst] 엔케팔린 주입 완료
   źródło: MainUIText.json :: dataList[id=enkephalin_injection_complete].content
   limit: do 120 znaków
   EN: Enkephalin Charged
   PL:
843. [Interfejs i ustawienia [purchase_impossible] — tekst] 구매 불가
   źródło: MainUIText.json :: dataList[id=purchase_impossible].content
   limit: do 120 znaków
   EN: Cannot Purchase
   PL:
844. [Interfejs i ustawienia [notice_not_enough_pieces] — tekst] ※파편이 부족합니다.
   źródło: MainUIText.json :: dataList[id=notice_not_enough_pieces].content
   limit: do 120 znaków
   EN: ※ Not enough Egoshards.
   PL:
845. [Interfejs i ustawienia [buy_personaliy] — tekst] 인격 구매
   źródło: MainUIText.json :: dataList[id=buy_personaliy].content
   limit: do 120 znaków
   EN: Purchase Identity
   PL:
846. [Interfejs i ustawienia [buy_ego] — tekst] E.G.O 구매
   źródło: MainUIText.json :: dataList[id=buy_ego].content
   limit: do 120 znaków
   EN: Purchase E.G.O
   PL:
847. [Interfejs i ustawienia [not_enough_pieces] — tekst] 파편 수량 부족
   źródło: MainUIText.json :: dataList[id=not_enough_pieces].content
   limit: do 120 znaków
   EN: Not enough Egoshards
   PL:
848. [Interfejs i ustawienia [basis] — tekst] 기초
   źródło: MainUIText.json :: dataList[id=basis].content
   limit: do 120 znaków
   EN: Basic
   PL:
849. [Interfejs i ustawienia [skip_tutorial] — tekst] 튜토리얼 스킵
   źródło: MainUIText.json :: dataList[id=skip_tutorial].content
   limit: do 120 znaków
   EN: Skip Tutorial
   PL:
850. [Interfejs i ustawienia [skip_tutorial_description] — tekst] 튜토리얼을 스킵하시겠습니까?
   źródło: MainUIText.json :: dataList[id=skip_tutorial_description].content
   limit: do 120 znaków
   EN: Are you sure you want to skip the tutorial?
   PL:
851. [Interfejs i ustawienia [min_speed_upgrade] — tekst] 최소 속도 상승
   źródło: MainUIText.json :: dataList[id=min_speed_upgrade].content
   limit: do 120 znaków
   EN: Min. SPD Up
   PL:
852. [Interfejs i ustawienia [max_speed_upgrade] — tekst] 최대 속도 상승
   źródło: MainUIText.json :: dataList[id=max_speed_upgrade].content
   limit: do 120 znaków
   EN: Max. SPD Up
   PL:
853. [Interfejs i ustawienia [min_max_speed_upgrade] — tekst] 최소, 최대 속도 상승
   źródło: MainUIText.json :: dataList[id=min_max_speed_upgrade].content
   limit: do 120 znaków
   EN: Min. and Max. SPD Up
   PL:
854. [Interfejs i ustawienia [mailbox] — tekst] 우편함
   źródło: MainUIText.json :: dataList[id=mailbox].content
   limit: do 120 znaków
   EN: Mailbox
   PL:
855. [Interfejs i ustawienia [remain_days_label] — tekst] 수령 기한
   źródło: MainUIText.json :: dataList[id=remain_days_label].content
   limit: do 120 znaków
   EN: Due Date
   PL:
856. [Interfejs i ustawienia [extract_again] — tekst] 재추출
   źródło: MainUIText.json :: dataList[id=extract_again].content
   limit: do 120 znaków
   EN: Extract Again
   PL:
857. [Interfejs i ustawienia [ego_gift] — tekst] E.G.O 기프트
   źródło: MainUIText.json :: dataList[id=ego_gift].content
   limit: do 120 znaków
   EN: E.G.O Gifts
   PL:
858. [Interfejs i ustawienia [classification] — tekst] 분류
   źródło: MainUIText.json :: dataList[id=classification].content
   limit: do 120 znaków
   EN: Category
   PL:
859. [Interfejs i ustawienia [quantity] — tekst] 수량
   źródło: MainUIText.json :: dataList[id=quantity].content
   limit: do 120 znaków
   EN: Quantity
   PL:
860. [Interfejs i ustawienia [appearance_probability] — tekst] 등장 확률
   źródło: MainUIText.json :: dataList[id=appearance_probability].content
   limit: do 120 znaków
   EN: Rate
   PL:
861. [Interfejs i ustawienia [Individual_appearance_probability] — tekst] 개별 등장 확률
   źródło: MainUIText.json :: dataList[id=Individual_appearance_probability].content
   limit: do 120 znaków
   EN: Individual Rate
   PL:
862. [Interfejs i ustawienia [notice_sold_out] — tekst] 입고 준비 중...
   źródło: MainUIText.json :: dataList[id=notice_sold_out].content
   limit: do 120 znaków
   EN: Out of Stock
   PL:
863. [Interfejs i ustawienia [select_piece] — tekst] 교환 파편 선택
   źródło: MainUIText.json :: dataList[id=select_piece].content
   limit: do 120 znaków
   EN: Choose Egoshard
   PL:
864. [Interfejs i ustawienia [mail_item_warning] — tekst] ※수령 시 청약 철회 제한
   źródło: MainUIText.json :: dataList[id=mail_item_warning].content
   limit: do 120 znaków
   EN: ※ Refund may be restricted after redeeming the item.
   PL:
865. [Interfejs i ustawienia [mainui_unlock_condition_by_ego_awaken_level] — tekst] 환상 해석 {0}단계 개방
   źródło: MainUIText.json :: dataList[id=mainui_unlock_condition_by_ego_awaken_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Unlocked at Tier {0}
   PL:
866. [Interfejs i ustawienia [empty_mailbox_notice] — tekst] 보관 중인 우편이 없습니다.
   źródło: MainUIText.json :: dataList[id=empty_mailbox_notice].content
   limit: do 120 znaków
   EN: No mail in storage.
   PL:
867. [Interfejs i ustawienia [gacha_rate_detail] — tekst] 추출 확률 상세
   źródło: MainUIText.json :: dataList[id=gacha_rate_detail].content
   limit: do 120 znaków
   EN: Detailed Rates
   PL:
868. [Interfejs i ustawienia [gacha_alarm_title] — tekst] 추출 진행
   źródło: MainUIText.json :: dataList[id=gacha_alarm_title].content
   limit: do 120 znaków
   EN: Proceeding with Extraction
   PL:
869. [Interfejs i ustawienia [clear_specific_stage] — tekst] {0} 클리어
   źródło: MainUIText.json :: dataList[id=clear_specific_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear {0}
   PL:
870. [Interfejs i ustawienia [clear_main_chapter_stage] — tekst] {0}장 클리어
   źródło: MainUIText.json :: dataList[id=clear_main_chapter_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clear Ch. {0}
   PL:
871. [Interfejs i ustawienia [ingredients] — tekst] 재료
   źródło: MainUIText.json :: dataList[id=ingredients].content
   limit: do 120 znaków
   EN: Items
   PL:
872. [Interfejs i ustawienia [remote_download_return_title] — tekst] 새로운 다운로드 항목이 추가되었습니다.\n타이틀로 돌아갑니다.
   źródło: MainUIText.json :: dataList[id=remote_download_return_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new download has been added.\nReturning to the title screen.
   PL:
873. [Interfejs i ustawienia [battle_skip] — tekst] 전투 스킵
   źródło: MainUIText.json :: dataList[id=battle_skip].content
   limit: do 120 znaków
   EN: Skip Battle
   PL:
874. [Interfejs i ustawienia [ask_battle_skip] — tekst] 전투 스킵을 진행하시겠습니까?
   źródło: MainUIText.json :: dataList[id=ask_battle_skip].content
   limit: do 120 znaków
   EN: Would you like to skip the battle?
   PL:
875. [Interfejs i ustawienia [notice_consumption_multiples] — tekst] {0} 소모 {1} 배 증가
   źródło: MainUIText.json :: dataList[id=notice_consumption_multiples].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} cost x {1}
   PL:
876. [Interfejs i ustawienia [notice_additional_rewards] — tekst] 추가 보상 {0} 획득
   źródło: MainUIText.json :: dataList[id=notice_additional_rewards].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Additional rewards {0} earned
   PL:
877. [Interfejs i ustawienia [gacha_notice_exclude_ego] — tekst] 본 추출에는 E.G.O 가 등장하지 않습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_exclude_ego].content
   limit: do 120 znaków
   EN: This extraction banner does not include E.G.O.
   PL:
878. [Interfejs i ustawienia [gacha_notice_single_season] — tekst] 본 추출에서 등장하는 2성과 3성 인격은 시즌 {0} 에 해당합니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_single_season].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The 2★ and 3★ Identities in this extraction banner belong to Season {0}.
   PL:
879. [Interfejs i ustawienia [error_and_return_to_main] — tekst] 오류가 발생하였습니다.\n메인 화면으로 돌아가겠습니다.
   źródło: MainUIText.json :: dataList[id=error_and_return_to_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: An error has occurred.\nReturning to the title screen.
   PL:
880. [Interfejs i ustawienia [to_window] — tekst] 유리창 이동
   źródło: MainUIText.json :: dataList[id=to_window].content
   limit: do 120 znaków
   EN: To Window
   PL:
881. [Interfejs i ustawienia [completion] — tekst] 완료
   źródło: MainUIText.json :: dataList[id=completion].content
   limit: do 120 znaków
   EN: Complete
   PL:
882. [Interfejs i ustawienia [event_in_progress] — tekst] 이벤트 중
   źródło: MainUIText.json :: dataList[id=event_in_progress].content
   limit: do 120 znaków
   EN: Event Open
   PL:
883. [Interfejs i ustawienia [end_of_event] — tekst] 이벤트 종료
   źródło: MainUIText.json :: dataList[id=end_of_event].content
   limit: do 120 znaków
   EN: Event Closed
   PL:
884. [Interfejs i ustawienia [gacha_rate_info_intro1_1a] — tekst] 1회 추출 시 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1a].content
   limit: do 120 znaków
   EN: The rates for a single Extraction are as follows.
   PL:
885. [Interfejs i ustawienia [gacha_rate_info_intro1_1b] — tekst] {0} 1회 사용 시, 등장 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1b].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The table for one use of {0} is as follows.
   PL:
886. [Interfejs i ustawienia [gacha_rate_info_intro1_1c] — tekst] {0} 사용 시, 다음 재화 중 하나를 선택할 수 있습니다
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1c].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When you use {0}, you can choose one currency from the following.
   PL:
887. [Interfejs i ustawienia [package_info_detail1] — tekst] 등장하는 재화를 설정하였을 때, {0} 1개를 사용하여 설정한 재화를 획득할 수량의 확률은 다음과 같습니다.
   źródło: MainUIText.json :: dataList[id=package_info_detail1].content
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When you have selected the currency, the table for acquiring different quantities of the set currency by using one {0} is as follows.
   PL:
888. [Interfejs i ustawienia [package_info_detail2] — tekst] ※ 하단 표의 “{0}”은(는) 상단 표의 등장하는 재화 중 하나를 선택하였을 때의 예시입니다.
   źródło: MainUIText.json :: dataList[id=package_info_detail2].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: ※ “{0}” in the lower table is an example for selecting one of the currencies from the table above.
   PL:
889. [Interfejs i ustawienia [acquired_quantity] — tekst] 획득 수량
   źródło: MainUIText.json :: dataList[id=acquired_quantity].content
   limit: do 120 znaków
   EN: Amount
   PL:
890. [Interfejs i ustawienia [name_of_currencies] — tekst] 재화명
   źródło: MainUIText.json :: dataList[id=name_of_currencies].content
   limit: do 120 znaków
   EN: Currency
   PL:
891. [Interfejs i ustawienia [package_info_title] — tekst] 재화 등장 확률 상세
   źródło: MainUIText.json :: dataList[id=package_info_title].content
   limit: do 120 znaków
   EN: Detailed Currency Appearance Rates
   PL:
892. [Interfejs i ustawienia [used_once] — tekst] 1회 사용
   źródło: MainUIText.json :: dataList[id=used_once].content
   limit: do 120 znaków
   EN: One Use
   PL:
893. [Interfejs i ustawienia [probability_details] — tekst] 확률 상세
   źródło: MainUIText.json :: dataList[id=probability_details].content
   limit: do 120 znaków
   EN: Probabilities
   PL:
894. [Interfejs i ustawienia [be_in_use] — tekst] 사용 중
   źródło: MainUIText.json :: dataList[id=be_in_use].content
   limit: do 120 znaków
   EN: In Use
   PL:
895. [Interfejs i ustawienia [season_information] — tekst] 시즌 안내
   źródło: MainUIText.json :: dataList[id=season_information].content
   limit: do 120 znaków
   EN: Seasons Guide
   PL:
896. [Interfejs i ustawienia [announcer_selection_description] — tekst] ※ 2개 이상의 아나운서를 선택할 경우, 선택된 아나운서의 대사들이 무작위로 재생됩니다. (최대 100개)
   źródło: MainUIText.json :: dataList[id=announcer_selection_description].content
   limit: do 140 znaków
   EN: ※ If you select 2 or more Announcers at once, the dialogue to play will be randomly chosen (up to 100).
   PL:
897. [Interfejs i ustawienia [panic_type] — tekst] 패닉 유형
   źródło: MainUIText.json :: dataList[id=panic_type].content
   limit: do 120 znaków
   EN: Panic Types
   PL:
898. [Interfejs i ustawienia [mental_strength] — tekst] 정신력
   źródło: MainUIText.json :: dataList[id=mental_strength].content
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Interfejs i ustawienia [mental_increase_condition] — tekst] 기본 정신력 증가 조건
   źródło: MainUIText.json :: dataList[id=mental_increase_condition].content
   limit: do 120 znaków
   EN: Base factors increasing Sanity
   PL:
900. [Interfejs i ustawienia [mental_decrease_condition] — tekst] 기본 정신력 감소 조건
   źródło: MainUIText.json :: dataList[id=mental_decrease_condition].content
   limit: do 120 znaków
   EN: Base factors decreasing Sanity
   PL:
901. [Interfejs i ustawienia [mental_low_morale_effect] — tekst] 사기 저하 효과
   źródło: MainUIText.json :: dataList[id=mental_low_morale_effect].content
   limit: do 120 znaków
   EN: Low Morale Effects
   PL:
902. [Interfejs i ustawienia [mental_panic_effect] — tekst] 패닉 효과
   źródło: MainUIText.json :: dataList[id=mental_panic_effect].content
   limit: do 120 znaków
   EN: Panic Effects
   PL:
903. [Interfejs i ustawienia [open_scheduled_date_month_day] — tekst] {0}월 {1}일 개방 예정
   źródło: MainUIText.json :: dataList[id=open_scheduled_date_month_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Opening {0}M {1}D (Month/Day)
   PL:
904. [Interfejs i ustawienia [mainui_acquire_user_ticker_deco] — tekst] 아이템 획득
   źródło: MainUIText.json :: dataList[id=mainui_acquire_user_ticker_deco].content
   limit: do 120 znaków
   EN: Item gained
   PL:
905. [Interfejs i ustawienia [last_battlepass_season_level] — tekst] 패스 달성 레벨
   źródło: MainUIText.json :: dataList[id=last_battlepass_season_level].content
   limit: do 120 znaków
   EN: Pass Level
   PL:
906. [Interfejs i ustawienia [season_end_notification] — tekst] 시즌 종료 안내
   źródło: MainUIText.json :: dataList[id=season_end_notification].content
   limit: do 120 znaków
   EN: Season End Notice
   PL:
907. [Interfejs i ustawienia [season_start_notification] — tekst] 시즌 시작 안내
   źródło: MainUIText.json :: dataList[id=season_start_notification].content
   limit: do 120 znaków
   EN: Season Start Notice
   PL:
908. [Interfejs i ustawienia [new_story_appeared_by_new_season] — tekst] 신규 주요 이야기 등장
   źródło: MainUIText.json :: dataList[id=new_story_appeared_by_new_season].content
   limit: do 120 znaków
   EN: New Main Story Content
   PL:
909. [Interfejs i ustawienia [collection_rate] — tekst] 수집률
   źródło: MainUIText.json :: dataList[id=collection_rate].content
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Interfejs i ustawienia [season_n_personality] — tekst] 시즌 {0} 인격
   źródło: MainUIText.json :: dataList[id=season_n_personality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0} Identity
   PL:
911. [Interfejs i ustawienia [season_n_ego] — tekst] 시즌 {0} E.G.O
   źródło: MainUIText.json :: dataList[id=season_n_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0} E.G.O
   PL:
912. [Interfejs i ustawienia [season_n] — tekst] 시즌 {0}
   źródło: MainUIText.json :: dataList[id=season_n].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Season {0}
   PL:
913. [Interfejs i ustawienia [new_season_former_piece_to_current_piece_desc] — tekst] 기존에 보유하였던 자아 파편의 일정량이 현재 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_piece_to_current_piece_desc].content
   limit: do 120 znaków
   EN: A portion of the Egoshards you own will be carried over to the current season.
   PL:
914. [Interfejs i ustawienia [new_season_former_piece_to_thread_desc] — tekst] 이월되지 않은 자아 파편은 끈으로 변경됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_piece_to_thread_desc].content
   limit: do 120 znaków
   EN: The Egoshards that have not been carried over are converted into Thread.
   PL:
915. [Interfejs i ustawienia [new_season_former_box_to_current_box_desc] — tekst] 기존에 보유하였던 자아 파편 상자, 자아 파편 선택 상자의 일정량이 현재 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_box_to_current_box_desc].content
   limit: do 150 znaków
   EN: A portion of the Egoshard Crates (both random & nominable) you own will be carried over to the current season.
   PL:
916. [Interfejs i ustawienia [new_season_former_box_to_thread_box] — tekst] 이월되지 않은 자아 파편 상자, 자아 파편 선택 상자는 끈 상자로 변경됩니다.
   źródło: MainUIText.json :: dataList[id=new_season_former_box_to_thread_box].content
   limit: do 120 znaków
   EN: The Egoshard Crates that have not been carried over are converted into Thread Crates.
   PL:
917. [Interfejs i ustawienia [new_pass_appeared] — tekst] 신규 패스 출현
   źródło: MainUIText.json :: dataList[id=new_pass_appeared].content
   limit: do 120 znaków
   EN: New Pass Available
   PL:
918. [Interfejs i ustawienia [get_not_acquired_rewards] — tekst] 미수령 보상 지급
   źródło: MainUIText.json :: dataList[id=get_not_acquired_rewards].content
   limit: do 120 znaków
   EN: Unclaimed Rewards Delivered
   PL:
919. [Interfejs i ustawienia [items_changed_by_season_changed_desc] — tekst] 이전 시즌의 재화가 현재 시즌에 맞추어 이월 적용됩니다.
   źródło: MainUIText.json :: dataList[id=items_changed_by_season_changed_desc].content
   limit: do 120 znaków
   EN: Currencies from the previous season will be converted into the current season.
   PL:
920. [Interfejs i ustawienia [exchange] — tekst] 교환
   źródło: MainUIText.json :: dataList[id=exchange].content
   limit: do 120 znaków
   EN: Exchange
   PL:
921. [Interfejs i ustawienia [notice_of_pity_system] — tekst] 추출 기간 동안 추출을 진행한 횟수에 따라 이상[理想]을 획득합니다.\n일정 수량의 이상[理想]을 모을 경우, 특정 추출에 등장하는\n대표 3성 인격 혹은 E.G.O와 교환할 수 있습니다.\n\n※ 각각의 특정 추출에서 획득할 수 있는 이상[理想]은 공유되지 않고 서로 별개의 재화로 계산됩니다. \n※ 특정 추출의 기간이 종료되면 교환되지 않은 이상[理想]은 끈으로 전환됩니다.
   źródło: MainUIText.json :: dataList[id=notice_of_pity_system].content
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: During a banner, you can gain ‘Yisang’ [Ideality] based on the number of extractions you’ve done.\nAfter collecting a certain amount, you can exchange it for a 3★ Identity or E.G.O represented on the banner.\n\n※ Ideality is not shared between banners; Ideality in each is considered its own currency.\n※ After the banner is over, the remaining Ideality is converted into Thread.
   PL:
922. [Interfejs i ustawienia [twine_store] — tekst] 파편::끈 교환기
   źródło: MainUIText.json :: dataList[id=twine_store].content
   limit: do 120 znaków
   EN: Shard::Thread Exchange
   PL:
923. [Interfejs i ustawienia [pass] — tekst] 패스
   źródło: MainUIText.json :: dataList[id=pass].content
   limit: do 120 znaków
   EN: Pass
   PL:
924. [Interfejs i ustawienia [event] — tekst] 이벤트
   źródło: MainUIText.json :: dataList[id=event].content
   (powtórzenie elementu 64 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Interfejs i ustawienia [notice_of_pity_point_expiration] — tekst] {0} 에서 누적된 이상[理想] {1}개가 끈으로 변환되었습니다.
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_expiration].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} Yisang [Ideality] from {0} has been converted to Thread.
   PL:
926. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not] — tekst] 이상[理想] 200개를 소모하여 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_progress_or_not].content
   limit: do 120 znaków
   EN: Spend 200 Yisang [Ideality] and make this exchange?
   PL:
927. [Interfejs i ustawienia [notice_of_pity_point_progress_or_not_already_have] — tekst] 선택한 인격을 이미 보유 중입니다. 이상[理想] 200개를 소모하여 선택한 수감자의 파편 50개로 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_progress_or_not_already_have].content
   limit: do 140 znaków
   EN: You already own the selected Identity. Exchange 200 Yisang [Ideality] for this Sinner's 50 Identity Shards?
   PL:
928. [Interfejs i ustawienia [open_date_description_month_day_time_zone] — tekst] {0}월 {1}일 ({2}) 업데이트 이후 개방
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Unlocked after {0}/{1} ({2}) update
   PL:
929. [Interfejs i ustawienia [open_date_description_month_day_time_zone_date] — tekst] {0}월 {1}일 ({2})
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0}/{1} ({2})
   PL:
930. [Interfejs i ustawienia [open_date_description_month_day_time_zone_desc] — tekst] 업데이트 이후 개방
   źródło: MainUIText.json :: dataList[id=open_date_description_month_day_time_zone_desc].content
   limit: do 120 znaków
   EN: Unlocked after Update
   PL:
931. [Interfejs i ustawienia [enkephalin_desc] — tekst] 스테이지를 입장할 때 사용한다.
   źródło: MainUIText.json :: dataList[id=enkephalin_desc].content
   limit: do 120 znaków
   EN: Used for entering stages.
   PL:
932. [Interfejs i ustawienia [not_exchangeable] — tekst] 교환 불가
   źródło: MainUIText.json :: dataList[id=not_exchangeable].content
   limit: do 120 znaków
   EN: Cannot Exchange
   PL:
933. [Interfejs i ustawienia [ego_already_have] — tekst] 이미 보유 중인 EGO
   źródło: MainUIText.json :: dataList[id=ego_already_have].content
   limit: do 120 znaków
   EN: E.G.O Already Owned
   PL:
934. [Interfejs i ustawienia [shortage_number_of_extractions] — tekst] 추출 횟수 부족
   źródło: MainUIText.json :: dataList[id=shortage_number_of_extractions].content
   limit: do 120 znaków
   EN: Not Enough Extractions Done
   PL:
935. [Interfejs i ustawienia [lack_of_formation_participation] — tekst] 이번 전투에서는 <color=#990000>최대 {0}명</color>의 수감자가 전투에 참여할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=lack_of_formation_participation].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}
   EN: In this battle, <color=#990000>up to {0}</color> Sinners can participate in combat.
   PL:
936. [Interfejs i ustawienia [tutorial_formation_participation_add_title] — tekst] 편성 인원 증가
   źródło: MainUIText.json :: dataList[id=tutorial_formation_participation_add_title].content
   limit: do 120 znaków
   EN: More Participants
   PL:
937. [Interfejs i ustawienia [tutorial_formation_participation_add_desc] — tekst] 특정 스테이지에서는 참여할 수 있는 최대 인원 수가 직전에 입장한 스테이지 인원 수와 비교하였을 때 증가할 수 있습니다. 이러한 경우에는 편성 편집 영역이 깜빡거립니다.
   źródło: MainUIText.json :: dataList[id=tutorial_formation_participation_add_desc].content
   limit: do 200 znaków
   EN: Certain stages may allow more Sinners to participate in battle compared to the previous stage played. In this case, the 'Edit Team' area will flicker.
   PL:
938. [Interfejs i ustawienia [could_not_select_friend_support_in_this_dungeon] — tekst] 이번 던전에서는 {0}의 지원 인격을 선택할 수 없습니다.
   źródło: MainUIText.json :: dataList[id=could_not_select_friend_support_in_this_dungeon].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You may not bring {0}'s Support Identity for this dungeon.
   PL:
939. [Interfejs i ustawienia [formation_force_participation_on] — tekst] 고정 편성
   źródło: MainUIText.json :: dataList[id=formation_force_participation_on].content
   limit: do 120 znaków
   EN: Fixed
   PL:
940. [Interfejs i ustawienia [formation_force_participation_off] — tekst] 고정 편성 필요
   źródło: MainUIText.json :: dataList[id=formation_force_participation_off].content
   limit: do 120 znaków
   EN: Fixed Member Needed
   PL:
941. [Interfejs i ustawienia [formation_must_participate_specific_character] — tekst] {0} 수감자가 참여해야 합니다.
   źródło: MainUIText.json :: dataList[id=formation_must_participate_specific_character].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} must participate.
   PL:
942. [Interfejs i ustawienia [cannot_exit_node_after_enter_by_force_alice_character] — tekst] 진입 시 던전의 다른 곳으로 이동할 수 없게 되며, {0} 수감자의 체력이 최대로 회복되고 정신력이 초기화됩니다.\n그래도 진입하시겠습니까?
   źródło: MainUIText.json :: dataList[id=cannot_exit_node_after_enter_by_force_alice_character].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Upon entry, you will no longer be able to travel to other nodes of the dungeon; {0} will fully heal HP and have their SP reset to 0.\nAre you sure you want to proceed?
   PL:
943. [Interfejs i ustawienia [story_dungeon_4_first_open_popup_desc] — tekst] 이번 던전에서는 이상 수감자의 지원 인격을 선택할 수 없으며, 해당 수감자가 전투에 항상 참여해야합니다.
   źródło: MainUIText.json :: dataList[id=story_dungeon_4_first_open_popup_desc].content
   limit: do 150 znaków
   EN: For this dungeon, you may not select a Support Identity for Yi Sang. Yi Sang must always participate in battles.
   PL:
944. [Interfejs i ustawienia [attack_level] — tekst] 공격 레벨
   źródło: MainUIText.json :: dataList[id=attack_level].content
   limit: do 120 znaków
   EN: Offense Level
   PL:
945. [Interfejs i ustawienia [defense_level] — tekst] 방어 레벨
   źródło: MainUIText.json :: dataList[id=defense_level].content
   (powtórzenie elementu 649 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
946. [Interfejs i ustawienia [personality_level] — tekst] 인격 레벨
   źródło: MainUIText.json :: dataList[id=personality_level].content
   limit: do 120 znaków
   EN: Identity Level
   PL:
947. [Interfejs i ustawienia [enemy_level] — tekst] 적 레벨
   źródło: MainUIText.json :: dataList[id=enemy_level].content
   limit: do 120 znaków
   EN: Enemy Level
   PL:
948. [Interfejs i ustawienia [cannot_enter] — tekst] 입장 불가
   źródło: MainUIText.json :: dataList[id=cannot_enter].content
   limit: do 120 znaków
   EN: Cannot Enter
   PL:
949. [Interfejs i ustawienia [lack_of_item_amount] — tekst] {0} 보유량 부족
   źródło: MainUIText.json :: dataList[id=lack_of_item_amount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Not enough {0}
   PL:
950. [Interfejs i ustawienia [required_count] — tekst] 필요 개수
   źródło: MainUIText.json :: dataList[id=required_count].content
   limit: do 120 znaków
   EN: Required
   PL:
951. [Interfejs i ustawienia [on_event_reward_grace_period] — tekst] 보상 수령 기간
   źródło: MainUIText.json :: dataList[id=on_event_reward_grace_period].content
   limit: do 120 znaków
   EN: Reward Reception Period
   PL:
952. [Interfejs i ustawienia [user_level_maximum_notice] — tekst] 관리자 최대 레벨에 도달했습니다.
   źródło: MainUIText.json :: dataList[id=user_level_maximum_notice].content
   limit: do 120 znaków
   EN: Reached Max Level.
   PL:
953. [Interfejs i ustawienia [user_level_limit_increase_notice] — tekst] ※ 추후 관리자 레벨 상한이 증가할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=user_level_limit_increase_notice].content
   limit: do 120 znaków
   EN: ※ The Max Manager Level may be raised with future updates.
   PL:
954. [Interfejs i ustawienia [level_up] — tekst] 레벨업
   źródło: MainUIText.json :: dataList[id=level_up].content
   limit: do 120 znaków
   EN: Level Up
   PL:
955. [Interfejs i ustawienia [summary] — tekst] 요약
   źródło: MainUIText.json :: dataList[id=summary].content
   limit: do 120 znaków
   EN: Summary
   PL:
956. [Interfejs i ustawienia [abnormality_part_skill] — tekst] 부위 스킬
   źródło: MainUIText.json :: dataList[id=abnormality_part_skill].content
   limit: do 120 znaków
   EN: Part Skills
   PL:
957. [Interfejs i ustawienia [awaken] — tekst] 각성
   źródło: MainUIText.json :: dataList[id=awaken].content
   limit: do 120 znaków
   EN: Awakening
   PL:
958. [Interfejs i ustawienia [erosion] — tekst] 침식
   źródło: MainUIText.json :: dataList[id=erosion].content
   limit: do 120 znaków
   EN: Corrosion
   PL:
959. [Interfejs i ustawienia [formation_panel_detail] — tekst] 상세
   źródło: MainUIText.json :: dataList[id=formation_panel_detail].content
   (powtórzenie elementu 362 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Interfejs i ustawienia [ego_cost] — tekst] E.G.O 자원
   źródło: MainUIText.json :: dataList[id=ego_cost].content
   limit: do 120 znaków
   EN: E.G.O Resources
   PL:
961. [Interfejs i ustawienia [enable_count_for_battle] — tekst] 전투 참가 가능 수
   źródło: MainUIText.json :: dataList[id=enable_count_for_battle].content
   limit: do 120 znaków
   EN: Participant Limit
   PL:
962. [Interfejs i ustawienia [select_for_formation] — tekst] 전투 참가 인격 선택
   źródło: MainUIText.json :: dataList[id=select_for_formation].content
   limit: do 120 znaków
   EN: Deploy Identity
   PL:
963. [Interfejs i ustawienia [edit_for_formation] — tekst] 편성 편집
   źródło: MainUIText.json :: dataList[id=edit_for_formation].content
   (powtórzenie elementu 791 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
964. [Interfejs i ustawienia [full_participated] — tekst] 참가 인원 최대
   źródło: MainUIText.json :: dataList[id=full_participated].content
   limit: do 120 znaków
   EN: Max Participants
   PL:
965. [Interfejs i ustawienia [select_for_delete_participation] — tekst] 전투 참가 해제
   źródło: MainUIText.json :: dataList[id=select_for_delete_participation].content
   limit: do 120 znaków
   EN: Dismiss Identity
   PL:
966. [Interfejs i ustawienia [clear_reward] — tekst] 클리어 보상
   źródło: MainUIText.json :: dataList[id=clear_reward].content
   limit: do 120 znaków
   EN: Clear Rewards
   PL:
967. [Interfejs i ustawienia [event_information] — tekst] 이벤트 안내
   źródło: MainUIText.json :: dataList[id=event_information].content
   limit: do 120 znaków
   EN: Event Info.
   PL:
968. [Interfejs i ustawienia [notice_not_on_sales_period] — tekst] ※구매할 수 있는 기간이 아닙니다.
   źródło: MainUIText.json :: dataList[id=notice_not_on_sales_period].content
   limit: do 120 znaków
   EN: ※ Cannot be purchased during this period.
   PL:
969. [Interfejs i ustawienia [pc_shortcut] — tekst] PC 단축키
   źródło: MainUIText.json :: dataList[id=pc_shortcut].content
   limit: do 120 znaków
   EN: PC Keyboard Shortcuts
   PL:
970. [Interfejs i ustawienia [shortcut_manual_popup_title] — tekst] 단축키 매뉴얼
   źródło: MainUIText.json :: dataList[id=shortcut_manual_popup_title].content
   limit: do 120 znaków
   EN: Keyboard Shortcuts Guide
   PL:
971. [Interfejs i ustawienia [new_dungeon_update_alarm] — tekst] 뒷문 변화 감지
   źródło: MainUIText.json :: dataList[id=new_dungeon_update_alarm].content
   limit: do 120 znaków
   EN: BACKDOOR VOLATILITY DETECTED
   PL:
972. [Interfejs i ustawienia [buy_announcer] — tekst] 아나운서 구매
   źródło: MainUIText.json :: dataList[id=buy_announcer].content
   limit: do 120 znaków
   EN: Purchase Announcer
   PL:
973. [Interfejs i ustawienia [label_require_paid_lunacy] — tekst] ※유료 광기가 부족합니다.
   źródło: MainUIText.json :: dataList[id=label_require_paid_lunacy].content
   limit: do 120 znaków
   EN: ※You don’t have enough paid Lunacy.
   PL:
974. [Interfejs i ustawienia [notice_require_paid_lunacy] — tekst] 유료 광기 수량 부족
   źródło: MainUIText.json :: dataList[id=notice_require_paid_lunacy].content
   limit: do 120 znaków
   EN: Insufficient Paid Lunacy
   PL:
975. [Interfejs i ustawienia [mainui_original] — tekst] 기존
   źródło: MainUIText.json :: dataList[id=mainui_original].content
   limit: do 120 znaków
   EN: Before
   PL:
976. [Interfejs i ustawienia [open_after_clear_node] — tekst] {0}-{1} 클리어 후 개방
   źródło: MainUIText.json :: dataList[id=open_after_clear_node].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Clear {0}-{1} to Unlock
   PL:
977. [Interfejs i ustawienia [effect_list_to_applied_level] — tekst] 레벨 적용 효과 목록
   źródło: MainUIText.json :: dataList[id=effect_list_to_applied_level].content
   limit: do 120 znaków
   EN: Active Level Effects
   PL:
978. [Interfejs i ustawienia [choice_event_effect] — tekst] 선택지 효과
   źródło: MainUIText.json :: dataList[id=choice_event_effect].content
   limit: do 120 znaków
   EN: Choice Effect
   PL:
979. [Interfejs i ustawienia [ego_gift_effect_format] — tekst] E.G.O 기프트 「{0}」 효과
   źródło: MainUIText.json :: dataList[id=ego_gift_effect_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: E.G.O Gift 「{0}」 Effect
   PL:
980. [Interfejs i ustawienia [mainui_previous] — tekst] 이전
   źródło: MainUIText.json :: dataList[id=mainui_previous].content
   limit: do 120 znaków
   EN: Previous
   PL:
981. [Interfejs i ustawienia [formation_force_abstain] — tekst] 인격 편성 불가
   źródło: MainUIText.json :: dataList[id=formation_force_abstain].content
   limit: do 120 znaków
   EN: Cannot Deploy
   PL:
982. [Interfejs i ustawienia [formation_view_detail] — tekst] 상세 보기
   źródło: MainUIText.json :: dataList[id=formation_view_detail].content
   limit: do 120 znaków
   EN: Details
   PL:
983. [Interfejs i ustawienia [only_hyphen] — tekst] -
   źródło: MainUIText.json :: dataList[id=only_hyphen].content
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Interfejs i ustawienia [first_time] — tekst] 초회
   źródło: MainUIText.json :: dataList[id=first_time].content
   limit: do 120 znaków
   EN: First-time
   PL:
985. [Interfejs i ustawienia [formation_Announcer_fixed] — tekst] 고정 편성
   źródło: MainUIText.json :: dataList[id=formation_Announcer_fixed].content
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
986. [Interfejs i ustawienia [gacha_rate_info_wa1] — tekst] ★ 끈 상자
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_wa1].content
   limit: do 120 znaków
   EN: ★ Thread Crate
   PL:
987. [Interfejs i ustawienia [gacha_rate_info_wa2] — tekst] 이미 보유한 아나운서를 중복하여 획득할 경우에는 끈 상자로 전환되어 획득하게 됩니다.\n\n획득한 끈 상자는 보유한 수량 그대로 다음 시즌으로 이월됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_wa2].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Obtaining a duplicate of an already-owned Announcer will convert it to Thread Crates.\n\nThese Thread Crates will be carried over as-is to the next Season.
   PL:
988. [Interfejs i ustawienia [login_scene_mini_story_warning_spoiler_format] — tekst] 주요 이야기 {0}장 이후의 내용을 담고 있습니다. 스토리를 감상하시겠습니까?
   źródło: MainUIText.json :: dataList[id=login_scene_mini_story_warning_spoiler_format].content
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
989. [Interfejs i ustawienia [notice_of_pity_point_already_have_announcer] — tekst] 선택한 아나운서를 이미 보유 중입니다. 이상[理想] 200개를 소모하여 끈 상자 50개로 교환하시겠습니까?
   źródło: MainUIText.json :: dataList[id=notice_of_pity_point_already_have_announcer].content
   limit: do 120 znaków
   EN: You already own the selected Announcer. Exchange 200 Yisang [Ideality] for 50 Thread Crates?
   PL:
990. [Interfejs i ustawienia [gacha_rate_info_announcer1] — tekst] 상단에 있는 추출 확률에 따라 하단에 명시된 목록에 있는 인격과 E.G.O 또는 아나운서를 획득할 수 있습니다.\n\n획득할 수 있는 인격과 E.G.O, 아나운서는 특정 시즌에 따라 변경될 수 있으며, 이러한 경우에는 변경 전에 공지사항을 통해 미리 안내합니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_announcer1].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Below is the list of Identities, E.G.O, and Announcers you can obtain following the aforementioned rates.\n\nThe list may change in certain seasons; upcoming changes to the reward tables will be announced in advance.
   PL:
991. [Interfejs i ustawienia [mainui_battleresult_ordeal_victory] — tekst] 제압 종료
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_ordeal_victory].content
   limit: do 120 znaków
   EN: Suppression Complete
   PL:
992. [Interfejs i ustawienia [mainui_battleresult_ordeal_defeat] — tekst] 제압 실패
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_ordeal_defeat].content
   limit: do 120 znaków
   EN: Suppression Failed
   PL:
993. [Interfejs i ustawienia [remain_exchange_count] — tekst] 잔여 교환 횟수
   źródło: MainUIText.json :: dataList[id=remain_exchange_count].content
   limit: do 120 znaków
   EN: Remaining Stock
   PL:
994. [Interfejs i ustawienia [remains] — tekst] 잔여
   źródło: MainUIText.json :: dataList[id=remains].content
   limit: do 120 znaków
   EN: Remaining
   PL:
995. [Interfejs i ustawienia [everyday] — tekst] 매일
   źródło: MainUIText.json :: dataList[id=everyday].content
   limit: do 120 znaków
   EN: Daily
   PL:
996. [Interfejs i ustawienia [for_n_days] — tekst] {0}일째
   źródło: MainUIText.json :: dataList[id=for_n_days].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Days
   PL:
997. [Interfejs i ustawienia [all_personalities] — tekst] 전체 인격
   źródło: MainUIText.json :: dataList[id=all_personalities].content
   limit: do 120 znaków
   EN: All Identities
   PL:
998. [Interfejs i ustawienia [leap_up_ticket_title] — tekst] 상승 도약 인격 선택
   źródło: MainUIText.json :: dataList[id=leap_up_ticket_title].content
   limit: do 120 znaków
   EN: Select Identity to Takeoff
   PL:
999. [Interfejs i ustawienia [leap_up_able_uptie_tier_and_level] — tekst] 동기화 단계, 레벨 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_uptie_tier_and_level].content
   limit: do 120 znaków
   EN: Can raise Uptie Tier & Identity Level
   PL:
1000. [Interfejs i ustawienia [leap_up_able_uptie_tier] — tekst] 동기화 단계 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_uptie_tier].content
   limit: do 120 znaków
   EN: Can raise Uptie Tier
   PL:
1001. [Interfejs i ustawienia [leap_up_able_level] — tekst] 레벨 상승 가능
   źródło: MainUIText.json :: dataList[id=leap_up_able_level].content
   limit: do 120 znaków
   EN: Can raise Identity Level
   PL:
1002. [Interfejs i ustawienia [leap_up_confim_title] — tekst] 인격 선택
   źródło: MainUIText.json :: dataList[id=leap_up_confim_title].content
   limit: do 120 znaków
   EN: Select Identity
   PL:
1003. [Interfejs i ustawienia [leap_up_confim_main] — tekst] [{0}] 인격의 성장 단계가 다음과 같이 변경됩니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_main].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: [{0}] Identity's Uptie Tier & Level will be changed as follows.
   PL:
1004. [Interfejs i ustawienia [leap_up_confim_caution_uptie] — tekst] 선택한 인격의 동기화 단계가 더 이상 증가하지 않습니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_caution_uptie].content
   limit: do 120 znaków
   EN: The selected Identity's Uptie Tier cannot be raised further.
   PL:
1005. [Interfejs i ustawienia [leap_up_confim_caution_level] — tekst] 선택한 인격의 레벨이 더 이상 증가하지 않습니다.
   źródło: MainUIText.json :: dataList[id=leap_up_confim_caution_level].content
   limit: do 120 znaków
   EN: The selected Identity's Level cannot be raised further.
   PL:
1006. [Interfejs i ustawienia [leap_up_confim_last_question] — tekst] <color=#F8C200>{0}</color> 을(를) 사용하시겠습니까?
   źródło: MainUIText.json :: dataList[id=leap_up_confim_last_question].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#F8C200>, </color>, {0}
   EN: Use <color=#F8C200>{0}</color>?
   PL:
1007. [Interfejs i ustawienia [expiration_date] — tekst] 유효 기간
   źródło: MainUIText.json :: dataList[id=expiration_date].content
   limit: do 120 znaków
   EN: Available Period
   PL:
1008. [Interfejs i ustawienia [unlink_account_title] — tekst] 연동 해제 계정 선택
   źródło: MainUIText.json :: dataList[id=unlink_account_title].content
   limit: do 120 znaków
   EN: Select Account to Unlink
   PL:
1009. [Interfejs i ustawienia [unlink_account_current_account] — tekst] 현재 계정
   źródło: MainUIText.json :: dataList[id=unlink_account_current_account].content
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [Interfejs i ustawienia [unlink_account_linked_account] — tekst] 연동된 계정
   źródło: MainUIText.json :: dataList[id=unlink_account_linked_account].content
   limit: do 120 znaków
   EN: Linked Accounts
   PL:
1011. [Interfejs i ustawienia [unlink_account_desc] — tekst] 연동 해제 시, {0}일간 해제가 불가능합니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Once you unlink, you will not be able to unlink again for {0} days.
   PL:
1012. [Interfejs i ustawienia [unlink_account_desc_unable_by_day] — tekst] {0} 이후부터 연동 해제가 가능합니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_desc_unable_by_day].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Can be unlinked after {0}.
   PL:
1013. [Interfejs i ustawienia [unlink_account_complete_title] — tekst] 연동 해제 완료
   źródło: MainUIText.json :: dataList[id=unlink_account_complete_title].content
   (powtórzenie elementu 446 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1014. [Interfejs i ustawienia [unlink_account_complete_desc] — tekst] 연동 해제가 완료되었습니다.\n타이틀 화면으로 돌아갑니다.
   źródło: MainUIText.json :: dataList[id=unlink_account_complete_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Account unlinking complete.\nReturning to the title screen.
   PL:
1015. [Interfejs i ustawienia [mainui_stageinfo_effectiveAttribute] — tekst] 유효 속성
   źródło: MainUIText.json :: dataList[id=mainui_stageinfo_effectiveAttribute].content
   limit: do 120 znaków
   EN: Effective Affinities
   PL:
1016. [Interfejs i ustawienia [personality_level_limit_release_title] — tekst] 인격 최대 레벨 확장
   źródło: MainUIText.json :: dataList[id=personality_level_limit_release_title].content
   limit: do 120 znaków
   EN: Identity Max Lv. Expanded
   PL:
1017. [Interfejs i ustawienia [personality_level_limit_release_desc] — tekst] 인격의 최대 레벨이 상승하였습니다.
   źródło: MainUIText.json :: dataList[id=personality_level_limit_release_desc].content
   limit: do 120 znaków
   EN: The level cap for your Identities have been raised.
   PL:
1018. [Interfejs i ustawienia [mainui_sinners_startSuppress] — tekst] 제압 시작
   źródło: MainUIText.json :: dataList[id=mainui_sinners_startSuppress].content
   limit: do 120 znaków
   EN: Suppress
   PL:
1019. [Interfejs i ustawienia [mainui_battleresult_AbnormalitySuppress_victory] — tekst] 환상체 제압 성공
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_AbnormalitySuppress_victory].content
   limit: do 120 znaków
   EN: Abnormality Suppression Successful
   PL:
1020. [Interfejs i ustawienia [mainui_battleresult_AbnormalitySuppress_defeat] — tekst] 환상체 제압 실패
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_AbnormalitySuppress_defeat].content
   limit: do 120 znaków
   EN: Abnormality Suppression Failed
   PL:
1021. [Interfejs i ustawienia [ui_text_unknown] — tekst] 알 수 없음
   źródło: MainUIText.json :: dataList[id=ui_text_unknown].content
   limit: do 120 znaków
   EN: Unknown
   PL:
1022. [Interfejs i ustawienia [buff_effect_for_level_format] — tekst] 버프「{0}」
   źródło: MainUIText.json :: dataList[id=buff_effect_for_level_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 「{0}」
   PL:
1023. [Interfejs i ustawienia [unit_keyword] — tekst] 특성 키워드
   źródło: MainUIText.json :: dataList[id=unit_keyword].content
   limit: do 120 znaków
   EN: Trait Keywords
   PL:
1024. [Interfejs i ustawienia [formation_ask_clear_selection] — tekst] 편성 순서를 초기화하시겠습니까?
   źródło: MainUIText.json :: dataList[id=formation_ask_clear_selection].content
   limit: do 120 znaków
   EN: Reset Deployment Order?
   PL:
1025. [Interfejs i ustawienia [item_owned_count] — tekst] (보유량 : {0})
   źródło: MainUIText.json :: dataList[id=item_owned_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: (Owned : {0})
   PL:
1026. [Interfejs i ustawienia [lunacy_owned_count_paid] — tekst] (유료 보유량 : {0}, 무료 보유량 : {1})
   źródło: MainUIText.json :: dataList[id=lunacy_owned_count_paid].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: (Paid : {0}, Free : {1})
   PL:
1027. [Interfejs i ustawienia [lunacy_owned_count_free] — tekst] (유료 보유량 : {0}, 무료 보유량 : {1})
   źródło: MainUIText.json :: dataList[id=lunacy_owned_count_free].content
   (powtórzenie elementu 1026 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Interfejs i ustawienia [mainui_ask_use_personality_level_ticket_disadvantage] — tekst] 관리자님이 현재 진행도에서 해당 티켓을 사용할 경우,\n선택한 인격의 레벨이 {0}이 아닌 {1}으로 적용되어\n대량의 경험치 손실을 입을 수 있습니다.\n\n그럼에도 불구하고 해당 티켓을 사용하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mainui_ask_use_personality_level_ticket_disadvantage].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: Using this ticket at your current story progress will raise your selected Identity's level to {1} instead of {0}, and any unused EXP in that process will be lost.\n\nWill you use this ticket anyway?
   PL:
1029. [Interfejs i ustawienia [mainui_exp_dungeon_7_title] — tekst] 경험치 채광-7 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_7_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Slash)
   PL:
1030. [Interfejs i ustawienia [mainui_exp_dungeon_7_open_day] — tekst] 경험치 채광 7단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_7_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Slash) opens on MON, TUE, and SUN.
   PL:
1031. [Interfejs i ustawienia [mainui_exp_dungeon_8_title] — tekst] 경험치 채광-7 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_8_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Pierce)
   PL:
1032. [Interfejs i ustawienia [mainui_exp_dungeon_8_open_day] — tekst] 경험치 채광 7단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_8_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Pierce) opens on WED, THU, and SUN.
   PL:
1033. [Interfejs i ustawienia [mainui_exp_dungeon_9_title] — tekst] 경험치 채광-7 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_9_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Blunt)
   PL:
1034. [Interfejs i ustawienia [mainui_exp_dungeon_9_open_day] — tekst] 경험치 채광 7단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_9_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #7 (Blunt) opens on FRI, SAT, and SUN.
   PL:
1035. [Interfejs i ustawienia [mainui_default_personality_blocked] — tekst] 기본 인격 편성 불가
   źródło: MainUIText.json :: dataList[id=mainui_default_personality_blocked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot\nDeploy\nBase\nIdentity
   PL:
1036. [Interfejs i ustawienia [mainui_change_personality_of_character] — tekst] {0} 수감자 인격 변경 필요. 지원 인격이 추가됨.
   źródło: MainUIText.json :: dataList[id=mainui_change_personality_of_character].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Cannot proceed with this {0} Identity. Support Identities added.
   PL:
1037. [Interfejs i ustawienia [caution] — tekst] 주의
   źródło: MainUIText.json :: dataList[id=caution].content
   limit: do 120 znaków
   EN: WARNING
   PL:
1038. [Interfejs i ustawienia [announcer_spoiler_caution] — tekst] 해당 아나운서에는 <color=#990000><{0}-{1}></color> 챕터의\n스포일러가 포함되어 있습니다.\n\n확인하시겠습니까?
   źródło: MainUIText.json :: dataList[id=announcer_spoiler_caution].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#990000>, </color>, {0}, {1}, \n
   EN: This Announcer contains spoilers for Chapter <color=#990000><{0}-{1}></color>.\n\nView anyway?
   PL:
1039. [Interfejs i ustawienia [mass_announcer_spoiler_caution] — tekst] 수령 목록에 클리어 하지 않은 챕터의\n스포일러가 될 수 있는 아나운서가\n포함되어 있습니다.\n\n보상을 수령하시겠습니까?
   źródło: MainUIText.json :: dataList[id=mass_announcer_spoiler_caution].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: One of the rewards you are about to claim\nincludes an Announcer who may contain spoilers\nfor a Chapter you haven't cleared yet.\n\nClaim them anyway?
   PL:
1040. [Interfejs i ustawienia [vending_machine_item_available_date_label] — tekst] {0}월 {1}일 {2} ({3}) 부터 자판기 교환 가능
   źródło: MainUIText.json :: dataList[id=vending_machine_item_available_date_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, \n
   EN: Dispenser Unlock:\n{0}/{1} {2} ({3})
   PL:
1041. [Interfejs i ustawienia [gacha_notice_vending_available_date] — tekst] 시즌 인격은 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal Identities can be Dispensed from the Dispenser starting from {0}/{1} {2} ({3})
   PL:
1042. [Interfejs i ustawienia [gacha_notice_vending_available_date_v2] — tekst] 시즌 E.G.O는 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date_v2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal E.G.O can be Dispensed starting from {0}/{1} {2} ({3})
   PL:
1043. [Interfejs i ustawienia [gacha_notice_vending_available_date_v3] — tekst] 시즌 인격·E.G.O는 {0}월 {1}일 {2} ({3}) 부터 자판기에서 교환할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=gacha_notice_vending_available_date_v3].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: Seasonal ID & E.G.O can be Dispensed starting from {0}/{1} {2} ({3})
   PL:
1044. [Interfejs i ustawienia [mini_story_warning_spoiler_checkbox_desc] — tekst] 팝업 다시 보지 않기
   źródło: MainUIText.json :: dataList[id=mini_story_warning_spoiler_checkbox_desc].content
   limit: do 120 znaków
   EN: Don't see this message again
   PL:
1045. [Interfejs i ustawienia [mainui_settings_push_notification] — tekst] 알림 설정
   źródło: MainUIText.json :: dataList[id=mainui_settings_push_notification].content
   limit: do 120 znaków
   EN: Notification Settings
   PL:
1046. [Interfejs i ustawienia [paid_lunacy_ui] — tekst] 유료 광기
   źródło: MainUIText.json :: dataList[id=paid_lunacy_ui].content
   limit: do 120 znaków
   EN: Paid Lunacy
   PL:
1047. [Interfejs i ustawienia [story_unable_to_skip] — tekst] 스킵할 수 없는 스토리입니다.
   źródło: MainUIText.json :: dataList[id=story_unable_to_skip].content
   limit: do 120 znaków
   EN: This story cannot be skipped.
   PL:
1048. [Interfejs i ustawienia [remote_download_quit_game] — tekst] 새로운 다운로드 항목이 추가되었습니다.\n게임이 종료되며, 재시작을 통해 다운로드 받아주시기 바랍니다.
   źródło: MainUIText.json :: dataList[id=remote_download_quit_game].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A new download has been added.\nThe game will be closed; please restart the game to download the update.
   PL:
1049. [Interfejs i ustawienia [mainui_settings_battle_speech] — tekst] 전투 중 대사 자막
   źródło: MainUIText.json :: dataList[id=mainui_settings_battle_speech].content
   limit: do 120 znaków
   EN: In-combat Dialogue Subtitles
   PL:
1050. [Interfejs i ustawienia [unable_to_upgrade_sync_level_by_main_story_1] — tekst] 주요 이야기\n1장 클리어 시\n자동 진행
   źródło: MainUIText.json :: dataList[id=unable_to_upgrade_sync_level_by_main_story_1].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upties upon\nclearing\nCanto I
   PL:
1051. [Interfejs i ustawienia [unable_to_upgrade_sync_level_by_main_story_2] — tekst] 주요 이야기\n2장 클리어 시\n자동 진행
   źródło: MainUIText.json :: dataList[id=unable_to_upgrade_sync_level_by_main_story_2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Upties upon\nclearing\nCanto II
   PL:
1052. [Interfejs i ustawienia [exp_dungeon_opened_desc] — tekst] 경험치 채광이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=exp_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: EXP Luxcavation has been unlocked.
   PL:
1053. [Interfejs i ustawienia [abnormality_tutorial_battle_participate_desc] — tekst] 전투에 참여할 수감자 5명을 선택해주세요.
   źródło: MainUIText.json :: dataList[id=abnormality_tutorial_battle_participate_desc].content
   limit: do 120 znaków
   EN: Select five Sinners to participate in this Encounter.
   PL:
1054. [Interfejs i ustawienia [thread_dungeon_opened_desc] — tekst] 끈 채광이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=thread_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: Thread Luxcavation has been unlocked.
   PL:
1055. [Interfejs i ustawienia [mirror_dungeon_opened_desc] — tekst] 거울 던전이 개방되었습니다.
   źródło: MainUIText.json :: dataList[id=mirror_dungeon_opened_desc].content
   limit: do 120 znaków
   EN: Mirror Dungeon has been unlocked.
   PL:
1056. [Interfejs i ustawienia [ego_gift_combine_explain_title] — tekst] 합성 조합식
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_title].content
   limit: do 120 znaków
   EN: Fusion Recipes
   PL:
1057. [Interfejs i ustawienia [ego_gift_combine_explain_label_keyword] — tekst] 키워드
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_keyword].content
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1058. [Interfejs i ustawienia [ego_gift_combine_explain_label_attack_type] — tekst] 공격 유형
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_attack_type].content
   limit: do 120 znaków
   EN: Attack Type
   PL:
1059. [Interfejs i ustawienia [ego_gift_combine_explain_label_etc] — tekst] 기타
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_label_etc].content
   (powtórzenie elementu 313 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1060. [Interfejs i ustawienia [ego_gift_combine_explain_button_label] — tekst] 조합식
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_button_label].content
   limit: do 120 znaków
   EN: Recipes
   PL:
1061. [Interfejs i ustawienia [ego_gift_combine_explain_no_item_list] — tekst] 관련된 E.G.O 기프트 합성 조합식이 없습니다.
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_no_item_list].content
   limit: do 120 znaków
   EN: No E.G.O Gift Fusion Recipe search result.
   PL:
1062. [Interfejs i ustawienia [ego_gift_combine_explain_required_label] — tekst] {0}종 중 {1}개
   źródło: MainUIText.json :: dataList[id=ego_gift_combine_explain_required_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {1} of {0}
   PL:
1063. [Interfejs i ustawienia [attendance_event_s6_desc] — tekst] 이벤트 기간 동안 누적 출석일에 따라 보상을 획득할 수 있으며, 보상은 해당 팝업 등장과 함께 자동으로 수령합니다.\n\n총 14일 출석 시, 모든 보상을 획득할 수 있습니다.
   źródło: MainUIText.json :: dataList[id=attendance_event_s6_desc].content
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Earn rewards based on your attendance during the Event period. Rewards are automatically claimed when the pop-up window appears.\n\nCollect 14 cumulative attendance checks to receive all rewards.
   PL:
1064. [Interfejs i ustawienia [formation_none_selected_desc] — tekst] 편성 순서가 지정된 수감자가 없습니다.\n\n수감자의 편성 순서를 지정해주세요.
   źródło: MainUIText.json :: dataList[id=formation_none_selected_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: You haven't Deployed any Sinners.\n\nSelect the Sinners to set the Deployment order.
   PL:
1065. [Interfejs i ustawienia [ego_gift_category_current_theme] — tekst] 테마팩 한정 합성 기프트
   źródło: MainUIText.json :: dataList[id=ego_gift_category_current_theme].content
   limit: do 120 znaków
   EN: Theme Pack Exclusive Fusion Gift
   PL:
1066. [Interfejs i ustawienia [mainui_exp_dungeon_10_title] — tekst] 경험치 채광-8 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_10_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Slash)
   PL:
1067. [Interfejs i ustawienia [mainui_exp_dungeon_10_open_day] — tekst] 경험치 채광 8단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_10_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Slash) opens on MON, TUE, and SUN.
   PL:
1068. [Interfejs i ustawienia [mainui_exp_dungeon_11_title] — tekst] 경험치 채광-8 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_11_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Pierce)
   PL:
1069. [Interfejs i ustawienia [mainui_exp_dungeon_11_open_day] — tekst] 경험치 채광 8단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_11_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Pierce) opens on WED, THU, and SUN.
   PL:
1070. [Interfejs i ustawienia [mainui_exp_dungeon_12_title] — tekst] 경험치 채광-8 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_12_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Blunt)
   PL:
1071. [Interfejs i ustawienia [mainui_exp_dungeon_12_open_day] — tekst] 경험치 채광 8단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_12_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #8 (Blunt) opens on FRI, SAT, and SUN.
   PL:
1072. [Interfejs i ustawienia [mainui_notice_download_failed] — tekst] 공지사항을 로드하지 못했습니다. 네트워크를 확인해주세요.
   źródło: MainUIText.json :: dataList[id=mainui_notice_download_failed].content
   limit: do 120 znaków
   EN: Could not load notices. Please check your network connection.
   PL:
1073. [Interfejs i ustawienia [mainui_settings_show_importance_level_UI] — tekst] 중요도 표기
   źródło: MainUIText.json :: dataList[id=mainui_settings_show_importance_level_UI].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Show Battle Hints\n(Gimmick Priority)
   PL:
1074. [Interfejs i ustawienia [mainui_settings_battle_result_announcer] — tekst] 전투 종료 아나운서 음성 재생 완료 대기
   źródło: MainUIText.json :: dataList[id=mainui_settings_battle_result_announcer].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wait for Announcer Lines\nto end after Battle
   PL:
1075. [Interfejs i ustawienia [jiaxicun_level] — tekst] 가주 레벨
   źródło: MainUIText.json :: dataList[id=jiaxicun_level].content
   limit: do 120 znaków
   EN: Hierarch Level
   PL:
1076. [Interfejs i ustawienia [mainui_settings_stage_continue] — tekst] 컨티뉴
   źródło: MainUIText.json :: dataList[id=mainui_settings_stage_continue].content
   limit: do 120 znaków
   EN: Continue
   PL:
1077. [Interfejs i ustawienia [defence_skill_with_index] — tekst] 수비{0}
   źródło: MainUIText.json :: dataList[id=defence_skill_with_index].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Def. {0}
   PL:
1078. [Interfejs i ustawienia [servererror_invalid_battle_version] — tekst] 버전이 업데이트 되었습니다.\n리소스 다운로드 후 다시 시도해주세요.
   źródło: MainUIText.json :: dataList[id=servererror_invalid_battle_version].content
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1079. [Interfejs i ustawienia [gacha_rate_info_intro1_1_announcer_rate] — tekst] ※ 아나운서 등장 확률은 기존의 3성 인격 또는 E.G.O 등장 확률에는 영향을 주지 않으며, 대신 2성 또는 1성 인격의 등장 확률에서 차감되어 반영됩니다.
   źródło: MainUIText.json :: dataList[id=gacha_rate_info_intro1_1_announcer_rate].content
   limit: do 190 znaków
   EN: ※ Announcer Extraction rate does not affect 3★ IDs or E.G.O rates. Instead, 2★ and 1★ IDs will have lowered rates to make room for the Announcer.
   PL:
1080. [Interfejs i ustawienia [mainui_exp_dungeon_13_title] — tekst] 경험치 채광-9 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_13_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Slash)
   PL:
1081. [Interfejs i ustawienia [mainui_exp_dungeon_13_open_day] — tekst] 경험치 채광 9단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_13_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Slash) opens on MON, TUE, and SUN.
   PL:
1082. [Interfejs i ustawienia [mainui_exp_dungeon_14_title] — tekst] 경험치 채광-9 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_14_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Pierce)
   PL:
1083. [Interfejs i ustawienia [mainui_exp_dungeon_14_open_day] — tekst] 경험치 채광 9단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_14_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Pierce) opens on WED, THU, and SUN.
   PL:
1084. [Interfejs i ustawienia [mainui_exp_dungeon_15_title] — tekst] 경험치 채광-9 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_15_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Blunt)
   PL:
1085. [Interfejs i ustawienia [mainui_exp_dungeon_15_open_day] — tekst] 경험치 채광 9단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_15_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #9 (Blunt) opens on FRI, SAT, and SUN.
   PL:
1086. [Interfejs i ustawienia [assistant_level] — tekst] 캐릭터 레벨
   źródło: MainUIText.json :: dataList[id=assistant_level].content
   limit: do 120 znaków
   EN: Character Level
   PL:
1087. [Interfejs i ustawienia [mainui_ego_gift_keyword] — tekst] 키워드
   źródło: MainUIText.json :: dataList[id=mainui_ego_gift_keyword].content
   limit: do 120 znaków
   EN: Keyword
   PL:
1088. [Interfejs i ustawienia [mainui_ego_gift_grade] — tekst] 등급
   źródło: MainUIText.json :: dataList[id=mainui_ego_gift_grade].content
   limit: do 120 znaków
   EN: Tier
   PL:
1089. [Interfejs i ustawienia [mainui_use_random_piece_package] — tekst] 자아 파편 상자 사용
   źródło: MainUIText.json :: dataList[id=mainui_use_random_piece_package].content
   limit: do 120 znaków
   EN: Use Egoshard Crate
   PL:
1090. [Interfejs i ustawienia [mainui_use_optional_piece_package] — tekst] 자아 파편 선택 상자 사용
   źródło: MainUIText.json :: dataList[id=mainui_use_optional_piece_package].content
   limit: do 120 znaków
   EN: Use Nominable Egoshard Crate
   PL:
1091. [Interfejs i ustawienia [mainui_battleresult_consumable] — tekst] 소모 모듈
   źródło: MainUIText.json :: dataList[id=mainui_battleresult_consumable].content
   limit: do 120 znaków
   EN: Module Cost
   PL:
1092. [Interfejs i ustawienia [mainui_cont_mine_title] — tekst] 연속 진행
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_title].content
   limit: do 120 znaków
   EN: Consecutive Battle
   PL:
1093. [Interfejs i ustawienia [mainui_cont_mine_daily_bonus_desc] — tekst] 일일 추가 보상 {0}회 적용
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_daily_bonus_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Daily Bonuses Applied
   PL:
1094. [Interfejs i ustawienia [mainui_cont_mine_invalid_text] — tekst] 1회 클리어 이후 연속 진행 가능
   źródło: MainUIText.json :: dataList[id=mainui_cont_mine_invalid_text].content
   limit: do 120 znaków
   EN: Clear Stage once to unlock Consecutive Battle
   PL:
1095. [Interfejs i ustawienia [mainui_ego_sync_level_up_select_item] — tekst] 재화 제작 재료 선택
   źródło: MainUIText.json :: dataList[id=mainui_ego_sync_level_up_select_item].content
   limit: do 120 znaków
   EN: Select Crafting Ingredients
   PL:
1096. [Interfejs i ustawienia [mainui_passive_skill_upgrade] — tekst] 패시브 스킬 강화
   źródło: MainUIText.json :: dataList[id=mainui_passive_skill_upgrade].content
   limit: do 120 znaków
   EN: Passives Upgraded
   PL:
1097. [Interfejs i ustawienia [mainui_new_passive_skill_upgrade] — tekst] 패시브 스킬 [{0}] 강화
   źródło: MainUIText.json :: dataList[id=mainui_new_passive_skill_upgrade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Passive Enhanced: [{0}]
   PL:
1098. [Interfejs i ustawienia [formation_announcer_preset_name] — tekst] 프리셋 #{0}
   źródło: MainUIText.json :: dataList[id=formation_announcer_preset_name].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Preset #{0}
   PL:
1099. [Interfejs i ustawienia [formation_announcer_preset_title] — tekst] 아나운서 프리셋
   źródło: MainUIText.json :: dataList[id=formation_announcer_preset_title].content
   limit: do 120 znaków
   EN: Announcers Preset
   PL:
1100. [Interfejs i ustawienia [formation_announcer_reset_desc] — tekst] {0}을(를) 초기화하시겠습니까?
   źródło: MainUIText.json :: dataList[id=formation_announcer_reset_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Are you sure you want to reset {0}?
   PL:
1101. [Interfejs i ustawienia [mainui_exp_dungeon_16_title] — tekst] 경험치 채광-10 (참격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_16_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Slash)
   PL:
1102. [Interfejs i ustawienia [mainui_exp_dungeon_16_open_day] — tekst] 경험치 채광 10단계 (참격) 스테이지는 월요일, 화요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_16_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Slash) opens on MON, TUE, and SUN.
   PL:
1103. [Interfejs i ustawienia [mainui_exp_dungeon_17_title] — tekst] 경험치 채광-10 (관통)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_17_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Pierce)
   PL:
1104. [Interfejs i ustawienia [mainui_exp_dungeon_17_open_day] — tekst] 경험치 채광 10단계 (관통) 스테이지는 수요일, 목요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_17_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Pierce) opens on WED, THU, and SUN.
   PL:
1105. [Interfejs i ustawienia [mainui_exp_dungeon_18_title] — tekst] 경험치 채광-10 (타격)
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_18_title].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Blunt)
   PL:
1106. [Interfejs i ustawienia [mainui_exp_dungeon_18_open_day] — tekst] 경험치 채광 10단계 (타격) 스테이지는 금요일, 토요일, 일요일에 개방됩니다.
   źródło: MainUIText.json :: dataList[id=mainui_exp_dungeon_18_open_day].content
   limit: do 120 znaków
   EN: EXP Luxcavation #10 (Blunt) opens on FRI, SAT, and SUN.
   PL:
1107. [Interfejs i ustawienia [unitinfo_tab_synergy] — tekst] 시너지
   źródło: MainUIText.json :: dataList[id=unitinfo_tab_synergy].content
   limit: do 120 znaków
   EN: Synergy
   PL:
1108. [Interfejs i ustawienia [unitinfo_synergy_unsatisfied] — tekst] 조건 {0}개 불충족
   źródło: MainUIText.json :: dataList[id=unitinfo_synergy_unsatisfied].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} condition(s) unmet
   PL:
1109. [Interfejs i ustawienia [limtochess_entrance_coming_soon] — tekst] 준비 중입니다.
   źródło: MainUIText.json :: dataList[id=limtochess_entrance_coming_soon].content
   limit: do 120 znaków
   EN: Under construction
   PL:

## Interfejs i ustawienia: MainUIText_UPDATE_ON_0720
- plik gry: `MainUIText_UPDATE_ON_0720.json`

1110. [Interfejs i ustawienia [move_to_inventory] — tekst] 인벤토리 이동
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=move_to_inventory].content
   limit: do 120 znaków
   EN: Go to Inventory
   PL:
1111. [Interfejs i ustawienia [progress_personality_gacksung] — tekst] 동기화 진행
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=progress_personality_gacksung].content
   limit: do 120 znaków
   EN: Uptie
   PL:
1112. [Interfejs i ustawienia [mainui_reinforce_support_passive] — tekst] 서포트 패시브 [{0}] 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_reinforce_support_passive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Support Passive [{0}] Enhanced
   PL:
1113. [Interfejs i ustawienia [mainui_reinforce_battle_passive] — tekst] 전투 패시브 [{0}] 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_reinforce_battle_passive].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Combat Passive [{0}] Enhanced
   PL:
1114. [Interfejs i ustawienia [mainui_battle_passsive_reinforce] — tekst] 전투 패시브 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_battle_passsive_reinforce].content
   limit: do 120 znaków
   EN: Combat Passive Enhanced
   PL:
1115. [Interfejs i ustawienia [mainui_support_passsive_reinforce] — tekst] 서포트 패시브 강화
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_support_passsive_reinforce].content
   limit: do 120 znaków
   EN: Support Passive Enhanced
   PL:
1116. [Interfejs i ustawienia [mainui_target_num_label] — tekst] 공격 가중치
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_target_num_label].content
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1117. [Interfejs i ustawienia [mainui_awaken_requirement_label] — tekst] 필요 재화 수량
   źródło: MainUIText_UPDATE_ON_0720.json :: dataList[id=mainui_awaken_requirement_label].content
   (powtórzenie elementu 721 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
