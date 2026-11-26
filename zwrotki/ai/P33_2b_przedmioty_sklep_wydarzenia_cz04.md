# Paczka AI P33 (Fala 2 · 2B) — Przedmioty, sklep, ekstrakcja, Przepustka Bitewna i UI wydarzeń (część 4/9)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P33_2b_przedmioty_sklep_wydarzenia_cz04.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P33_2b_przedmioty_sklep_wydarzenia_cz04.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Wydarzenia i Przepustka: LimtochessUI
- plik gry: `LimtochessUI.json`

1. [Wydarzenia i Przepustka [limtochess_packselect_summary_ego_replace] — tekst] {0} E.G.O 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_summary_ego_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace {0} E.G.O
   PL: Wymiana {0} E.G.O
2. [Wydarzenia i Przepustka [limtochess_packselect_full] — tekst] 고를 수 있는 카드는 {0}장까지입니다. 고른 카드를 눌러 뺄 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_full].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You can select up to {0} cards. Select a chosen card again to remove it.
   PL: Możesz wybrać maks. {0} kart. Dotknięcie wybranej karty usuwa ją.
3. [Wydarzenia i Przepustka [limtochess_packselect_full_identity] — tekst] 인격은 {0}장까지 고를 수 있습니다. 고른 카드를 눌러 뺄 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_full_identity].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You can select up to {0} Identities. Select a chosen card again to remove it.
   PL: Możesz wybrać maks. {0} Tożsamości. Dotknięcie wybranej karty usuwa ją.
4. [Wydarzenia i Przepustka [limtochess_packselect_full_ego] — tekst] E.G.O는 {0}장까지 고를 수 있습니다. 고른 카드를 눌러 뺄 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_full_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You can select up to {0} E.G.O cards. Select a chosen card again to remove it.
   PL: Możesz wybrać maks. {0} kart E.G.O. Dotknięcie wybranej karty usuwa ją.
5. [Wydarzenia i Przepustka [limtochess_packselect_count_identity] — tekst] 인격 {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_count_identity].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: ID {0}/{1}
   PL: Tożsamości {0}/{1}
6. [Wydarzenia i Przepustka [limtochess_packselect_count_ego] — tekst] E.G.O {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_count_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: E.G.O {0}/{1}
   PL: E.G.O {0}/{1}
7. [Wydarzenia i Przepustka [limtochess_packselect_need_identity] — tekst] 인격을 {0}장 더 골라야 확정할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_need_identity].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select {0} more Identity card(s) to confirm.
   PL: Aby potwierdzić, wybierz jeszcze {0} Tożsamości.
8. [Wydarzenia i Przepustka [limtochess_packselect_need_ego] — tekst] E.G.O를 {0}장 더 골라야 확정할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_need_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select {0} more E.G.O card(s) to confirm.
   PL: Aby potwierdzić, wybierz jeszcze {0} kart E.G.O.
9. [Wydarzenia i Przepustka [limtochess_packselect_need_both] — tekst] 인격 {0}장, E.G.O {1}장을 더 골라야 확정할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_need_both].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Select {0} more Identity card(s) and {1} more E.G.O card(s) to confirm.
   PL: Aby potwierdzić, wybierz jeszcze {0} Tożsamości i {1} kart E.G.O.
10. [Wydarzenia i Przepustka [limtochess_roster_count] — tekst] 편성 {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Team {0}/{1}
   PL: Skład {0}/{1}
11. [Wydarzenia i Przepustka [limtochess_roster_replace_note] — tekst] 현재 도상의 편성 최대 인원({0}명)에 도달하여 {1}명을 제외해야 합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_note].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: The team size limit for this Schema ({0}) has been reached. Remove {1} member(s).
   PL: Osiągnięto maksymalny rozmiar składu tego Schematu ({0}). Usuń {1} członka(-ów).
12. [Wydarzenia i Przepustka [limtochess_confirm_unclaimed_title] — tekst] 받지 않은 보상이 있습니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_unclaimed_title].content
   limit: do 120 znaków
   EN: You have unclaimed rewards.
   PL: Masz nieodebrane nagrody
13. [Wydarzenia i Przepustka [limtochess_confirm_unclaimed_desc] — tekst] {0}\n이대로 진행하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_unclaimed_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: {0}\nProceed anyway?
   PL: {0}\nKontynuować?
14. [Wydarzenia i Przepustka [limtochess_confirm_overwrite_title] — tekst] 새 판 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_overwrite_title].content
   limit: do 120 znaków
   EN: Fresh Start
   PL: Nowa rozgrywka
15. [Wydarzenia i Przepustka [limtochess_packselect_reroll_bonus_title] — tekst] 새로고침 기회 보너스
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_reroll_bonus_title].content
   limit: do 120 znaków
   EN: Bonus Reshuffle
   PL: Bonus odświeżeń
16. [Wydarzenia i Przepustka [limtochess_packselect_reroll_count] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_reroll_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}/{1}
   PL: {0}/{1}
17. [Wydarzenia i Przepustka [limtochess_elite_swap_title] — tekst] 인격 교체 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_swap_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Identity Replacement: {0}
   PL: Wymiana Tożsamości: {0}
18. [Wydarzenia i Przepustka [limtochess_elite_swap_head] — tekst] 바꿀 대상
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_swap_head].content
   limit: do 120 znaków
   EN: Identity to Replace
   PL: Tożsamość do wymiany
19. [Wydarzenia i Przepustka [limtochess_elite_personality_sync] — tekst] {0} 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_personality_sync].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Uptie {1}
   PL: {0} Synchronizacja {1}
20. [Wydarzenia i Przepustka [limtochess_elite_recruit_title] — tekst] 편성 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_recruit_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Recruit: {0}
   PL: Werbunek: {0}
21. [Wydarzenia i Przepustka [limtochess_elite_replace_title] — tekst] 교체 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_replace_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace: {0}
   PL: Wymiana: {0}
22. [Wydarzenia i Przepustka [limtochess_elite_keyword_head] — tekst] 동기화 {0}단계 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_keyword_head].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie {0} Identity
   PL: Tożsamość z Synchronizacją {0}
23. [Wydarzenia i Przepustka [limtochess_elite_base_ego] — tekst] 수감자 기본 E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_base_ego].content
   limit: do 120 znaków
   EN: Sinner's Base E.G.O
   PL: Podstawowe E.G.O Grzesznika
24. [Wydarzenia i Przepustka [limtochess_elite_growth_title] — tekst] 성장 : 조각 +{0}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_growth_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Upgrade: Slivers +{0}
   PL: Rozwój: Skrawki +{0}
25. [Wydarzenia i Przepustka [limtochess_elite_growth_head] — tekst] 전투 편성 내 수감자 1명에게 조각 부여
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_growth_head].content
   limit: do 120 znaków
   EN: Give Sliver(s) to 1 Sinner in the Team
   PL: Przyznaj Skrawki 1 Grzesznikowi w składzie bojowym
26. [Wydarzenia i Przepustka [limtochess_elite_growth_desc] — tekst] 인격 동기화에 사용됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_growth_desc].content
   limit: do 120 znaków
   EN: Used to Uptie Identities.
   PL: Służy do Synchronizacji Tożsamości.
27. [Wydarzenia i Przepustka [limtochess_elite_skip_title] — tekst] 받지 않기
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_skip_title].content
   limit: do 120 znaków
   EN: Decline
   PL: Odrzuć
28. [Wydarzenia i Przepustka [limtochess_elite_skip_head] — tekst] 현재 전투 편성 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_skip_head].content
   limit: do 120 znaków
   EN: Keep Current Team
   PL: Zachowaj obecny skład bojowy
29. [Wydarzenia i Przepustka [limtochess_elite_sync] — tekst] 동기화 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_sync].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie {0}
   PL: Synchronizacja {0}
30. [Wydarzenia i Przepustka [limtochess_elite_fragments_label] — tekst] 보유 {0} 조각
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fragments_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Slivers Owned
   PL: Posiadane Skrawki: {0}
31. [Wydarzenia i Przepustka [limtochess_elite_back] — tekst] 뒤로가기
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_back].content
   limit: do 120 znaków
   EN: Back
   PL: Wstecz
32. [Wydarzenia i Przepustka [limtochess_elite_confirm] — tekst] 확인
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_confirm].content
   limit: do 120 znaków
   EN: Confirm
   PL: Potwierdź
33. [Wydarzenia i Przepustka [limtochess_confirm_pack_none] — tekst] 인격 카드를 하나도 고르지 않았습니다. 최대 {0}장까지 받을 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_none].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You haven't selected any Identity cards. You can claim up to {0}.
   PL: Nie wybrano żadnych kart Tożsamości. Możesz odebrać maks. {0}.
34. [Wydarzenia i Przepustka [limtochess_confirm_pack_left] — tekst] 인격 카드를 {0}장 더 받을 수 있습니다(고른 {1}/{2}장).
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_left].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: You can claim {0} more Identity card(s) ({1}/{2} selected).
   PL: Możesz odebrać jeszcze {0} kart Tożsamości (wybrano {1}/{2}).
35. [Wydarzenia i Przepustka [limtochess_confirm_pack_none_ego] — tekst] E.G.O 카드를 하나도 고르지 않았습니다. 최대 {0}장까지 받을 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_none_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You haven't selected any E.G.O cards. You can claim up to {0}.
   PL: Nie wybrano żadnych kart E.G.O. Możesz odebrać maks. {0}.
36. [Wydarzenia i Przepustka [limtochess_confirm_pack_none_both] — tekst] 카드를 하나도 고르지 않았습니다. 인격 최대 {0}장, E.G.O 최대 {1}장까지 받을 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_none_both].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: You haven't selected any cards. You can claim up to {0} Identity card(s) and {1} E.G.O card(s).
   PL: Nie wybrano żadnych kart. Możesz odebrać maks. {0} Tożsamości i {1} E.G.O.
37. [Wydarzenia i Przepustka [limtochess_confirm_pack_left_ego] — tekst] E.G.O 카드를 {0}장 더 받을 수 있습니다(고른 {1}/{2}장).
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_left_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: You can claim {0} more E.G.O card(s) ({1}/{2} selected).
   PL: Możesz odebrać jeszcze {0} kart E.G.O (wybrano {1}/{2}).
38. [Wydarzenia i Przepustka [limtochess_confirm_pack_left_both] — tekst] 인격 카드 {0}장, E.G.O 카드 {1}장을 더 받을 수 있습니다(고른 {2}/{3}장).
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_pack_left_both].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: You can claim {0} more Identity card(s) and {1} more E.G.O card(s) ({2}/{3} selected).
   PL: Możesz odebrać jeszcze {0} kart Tożsamości i {1} kart E.G.O (wybrano {2}/{3}).
39. [Wydarzenia i Przepustka [limtochess_confirm_reward_skip] — tekst] 받을 수 있는 보상 {0}개 중 하나도 받지 않고 넘어갑니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_reward_skip].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Proceed without claiming any of the {0} available rewards.
   PL: Przejdź dalej bez odbierania żadnej z {0} dostępnych nagród.
40. [Wydarzenia i Przepustka [limtochess_confirm_reward_rest_generic] — tekst] 범용 조각 {0}개를 이 휴식에서 아직 쓸 수 있습니다(최대 {1}번).\n휴식 보상을 받으면 휴식이 끝나 이번에는 더 쓸 수 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_reward_rest_generic].content
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: You can still spend {0} Universal Sliver(s) at this Respite (up to {1} times).\nClaiming a Respite reward ends the Respite, so you won't be able to spend them here afterward.
   PL: W tym Wytchnieniu możesz jeszcze wydać {0} Okruchów Uniwersalnych (maks. {1} razy).\nOdebranie nagrody Wytchnienia kończy je — wtedy już nie wydasz.
41. [Wydarzenia i Przepustka [limtochess_confirm_ego_replace_title] — tekst] E.G.O 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_ego_replace_title].content
   limit: do 120 znaków
   EN: Replace E.G.O
   PL: Wymiana E.G.O
42. [Wydarzenia i Przepustka [limtochess_confirm_ego_replace_desc] — tekst] {0}의 {1} 칸에 이미 '{2}'({3}단계)가 있습니다.\n'{4}'({5}단계)로 덮어쓰시겠습니까?\n취소하면 새 E.G.O는 버립니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_ego_replace_desc].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}, {5}, \n
   EN: {0}'s {1} slot already contains '{2}' (Tier {3}).\nReplace it with '{4}' (Tier {5})?\nCanceling discards the new E.G.O.
   PL: W gnieździe {1} jednostki {0} jest już „{2}” ({3}).\nZastąpić „{4}” ({5})?\nAnulowanie wyrzuca nowe E.G.O.
43. [Wydarzenia i Przepustka [limtochess_elite_disabled_swap] — tekst] 바꿀 수 있는 인격이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_disabled_swap].content
   limit: do 120 znaków
   EN: No Identities can be replaced.
   PL: Brak Tożsamości do wymiany.
44. [Wydarzenia i Przepustka [limtochess_elite_disabled_keyword] — tekst] 고를 수 있는 인격이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_disabled_keyword].content
   limit: do 120 znaków
   EN: No Identities available to select.
   PL: Brak Tożsamości do wyboru.
45. [Wydarzenia i Przepustka [limtochess_elite_disabled_growth] — tekst] 조각을 받을 수감자가 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_disabled_growth].content
   limit: do 120 znaków
   EN: No Sinners available to receive Slivers.
   PL: Brak Grzeszników, którzy mogą otrzymać Skrawki.
46. [Wydarzenia i Przepustka [limtochess_elite_head_swap] — tekst] 인격 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_head_swap].content
   limit: do 120 znaków
   EN: Replace Identity
   PL: Wymiana Tożsamości
47. [Wydarzenia i Przepustka [limtochess_elite_head_recruit] — tekst] 인격 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_head_recruit].content
   limit: do 120 znaków
   EN: Recruit Identity
   PL: Wystawienie do składu
48. [Wydarzenia i Przepustka [limtochess_elite_head_growth] — tekst] 성장
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_head_growth].content
   limit: do 120 znaków
   EN: Upgrade
   PL: Rozwój
49. [Wydarzenia i Przepustka [limtochess_elite_growth_target] — tekst] 전투 편성 내 수감자 1명에게 조각 {0}개 부여
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_growth_target].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Give {0} Sliver(s) to 1 Sinner in the Team
   PL: Przyznaj {0} Skrawków 1 Grzesznikowi w składzie bojowym
50. [Wydarzenia i Przepustka [limtochess_elite_base_ego_equipped] — tekst] 수감자 기본 E.G.O 장착 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_base_ego_equipped].content
   limit: do 120 znaków
   EN: Sinner's Base E.G.O Equipped
   PL: Wyposażone podstawowe E.G.O Grzesznika
51. [Wydarzenia i Przepustka [limtochess_elite_roster_full_head] — tekst] 편성 인원 가득 참
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_roster_full_head].content
   limit: do 120 znaków
   EN: Team Full
   PL: Skład pełny
52. [Wydarzenia i Przepustka [limtochess_elite_roster_full_desc] — tekst] 선택 시 기존 인격 {0}명을 제외합니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_roster_full_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Must remove {0} ID from Team to recruit
   PL: Wybór usunie {0} dotychczasowych Tożsamości
53. [Wydarzenia i Przepustka [limtochess_elite_skip_desc] — tekst] 정예 보상을 받지 않고\n진행합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_skip_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Continue without claiming\nElite Reward.
   PL: Kontynuuj bez odbierania\nnagrody elit.
54. [Wydarzenia i Przepustka [limtochess_start_title_direct] — tekst] 시작 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_title_direct].content
   limit: do 120 znaków
   EN: Starting Team
   PL: Drużyna startowa
55. [Wydarzenia i Przepustka [limtochess_start_title_auto] — tekst] 시작 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_title_auto].content
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
56. [Wydarzenia i Przepustka [limtochess_start_toggle_direct] — tekst] 수동 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_toggle_direct].content
   limit: do 120 znaków
   EN: Manual Team
   PL: Skład ręczny
57. [Wydarzenia i Przepustka [limtochess_start_toggle_auto] — tekst] 자동 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_toggle_auto].content
   limit: do 120 znaków
   EN: Randomize Team
   PL: Skład losowy
58. [Wydarzenia i Przepustka [limtochess_start_count] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_count].content
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
59. [Wydarzenia i Przepustka [limtochess_start_remaining_cost] — tekst] 남은 코스트
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_remaining_cost].content
   limit: do 120 znaków
   EN: Remaining Cost
   PL: Pozostały Koszt
60. [Wydarzenia i Przepustka [limtochess_start_clear_all] — tekst] 일괄 편성 해제
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_clear_all].content
   limit: do 120 znaków
   EN: Deselect All
   PL: Odznacz wszystkich
61. [Wydarzenia i Przepustka [limtochess_start_empty_slot] — tekst] 편성 가능
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_empty_slot].content
   limit: do 120 znaków
   EN: Available Slot
   PL: Wolne miejsce
62. [Wydarzenia i Przepustka [limtochess_start_empty] — tekst] 편성 해제
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_empty].content
   limit: do 120 znaków
   EN: Deselect
   PL: Odznacz
63. [Wydarzenia i Przepustka [limtochess_start_locked_band] — tekst] 편성 불가
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_locked_band].content
   limit: do 120 znaków
   EN: Cannot Deploy
   PL: Niedostępny
64. [Wydarzenia i Przepustka [limtochess_start_locked_list] — tekst] ※ 자동 편성 중에는 목록을 수정할 수 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_locked_list].content
   limit: do 120 znaków
   EN: ※ You cannot edit the list on a Randomized Team.
   PL: ※ Przy Składzie Losowym nie można edytować listy.
65. [Wydarzenia i Przepustka [limtochess_start_block_budget] — tekst] 코스트 부족
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_block_budget].content
   limit: do 120 znaków
   EN: Not Enough Cost
   PL: Za mało Kosztu
66. [Wydarzenia i Przepustka [limtochess_start_block_topcost] — tekst] {0}코스트 제한
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_block_topcost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}-Cost Limit
   PL: Limit Kosztu: {0}
67. [Wydarzenia i Przepustka [limtochess_start_block_full] — tekst] 인원 초과
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_block_full].content
   limit: do 120 znaków
   EN: Team Full
   PL: Skład pełny
68. [Wydarzenia i Przepustka [limtochess_start_block_auto] — tekst] 자동 편성 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_block_auto].content
   limit: do 120 znaków
   EN: Randomized Team Active
   PL: Skład Losowy aktywny
69. [Wydarzenia i Przepustka [limtochess_start_desc_auto] — tekst] ※자동 편성 시 패스 경험치 추가 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_desc_auto].content
   limit: do 120 znaków
   EN: ※ Use Randomized Teams to gain extra Pass EXP
   PL: ※ Skład Losowy daje dodatkowe PD Przepustki
70. [Wydarzenia i Przepustka [limtochess_start_start] — tekst] 시작
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_start].content
   limit: do 120 znaków
   EN: Start
   PL: Start
71. [Wydarzenia i Przepustka [limtochess_start_saved_deck] — tekst] 자동 편성 목록
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_saved_deck].content
   limit: do 120 znaków
   EN: Randomized Teams
   PL: Składy Losowe
72. [Wydarzenia i Przepustka [limtochess_start_reroll] — tekst] 자동 편성 새로고침
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_reroll].content
   limit: do 120 znaków
   EN: Reshuffle Randomized Team
   PL: Odśwież Skład Losowy
73. [Wydarzenia i Przepustka [limtochess_start_rolls_left] — tekst] 남은 굴림 횟수
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_rolls_left].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Remaining\nRolls
   PL: Pozostałe rzuty
74. [Wydarzenia i Przepustka [limtochess_start_rolls_bonus] — tekst] · 지난 판 진행 보너스로 자동 편성 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_rolls_bonus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: · Randomized Team Reshuffles +{0} based on your progress in the previous run
   PL: · Odświeżenia Składu Losowego +{0} za postęp w poprzedniej rozgrywce
75. [Wydarzenia i Przepustka [limtochess_start_reroll_help_tier] — tekst] - 도상 보스 처치 {0} : <color=#f8c200>+{1}</color>
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_reroll_help_tier].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}
   EN: - Schema Bosses defeated {0} : <color=#f8c200>+{1}</color>
   PL: - Pokonani bossowie Schematów {0}: <color=#f8c200>+{1}</color>
76. [Wydarzenia i Przepustka [limtochess_start_reroll_help_single] — tekst] {0}회
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_reroll_help_single].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Time(s)
   PL: {0} raz(y)
77. [Wydarzenia i Przepustka [limtochess_start_reroll_help_range] — tekst] {0}~{1}회
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_reroll_help_range].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} ~ {1} Time(s)
   PL: {0}~{1} raz(y)
78. [Wydarzenia i Przepustka [limtochess_start_reroll_help_open] — tekst] {0}회 이상
   źródło: LimtochessUI.json :: dataList[id=limtochess_start_reroll_help_open].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}+ Time(s)
   PL: {0}+ raz(y)
79. [Wydarzenia i Przepustka [limtochess_packselect_deck_tag_more] — tekst] ...
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_deck_tag_more].content
   limit: do 120 znaków
   EN: ...
   PL: ...
80. [Wydarzenia i Przepustka [limtochess_confirm_underfilled_desc] — tekst] 편성 가능한 인원보다 적게 선택했습니다. ({0}/{1}명)
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_underfilled_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Not all Deployable Identities have been selected. ({0} / {1} Deployed)
   PL: Wybrano mniej niż dostępne miejsca. ({0}/{1})
81. [Wydarzenia i Przepustka [limtochess_confirm_underfilled_proceed] — tekst] 이대로 진행하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_underfilled_proceed].content
   limit: do 120 znaków
   EN: Proceed anyway?
   PL: Kontynuować?
82. [Wydarzenia i Przepustka [limtochess_map_roster_standby] — tekst] 대기
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_roster_standby].content
   limit: do 120 znaków
   EN: Backup
   PL: Rezerwa
83. [Wydarzenia i Przepustka [limtochess_map_extra_move_steps] — tekst] 추가 굴림
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_extra_move_steps].content
   limit: do 120 znaków
   EN: Bonus Rolls
   PL: Rzuty dodatkowe
84. [Wydarzenia i Przepustka [limtochess_map_extra_roll_warning] — tekst] 초과 굴림 시, 도상 왜곡
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_extra_roll_warning].content
   limit: do 120 znaków
   EN: Excess reroll triggers Schema Deformation
   PL: Nadmiarowe rzuty wywołują Wypaczenie Schematu
85. [Wydarzenia i Przepustka [limtochess_map_elite_conversion_warning] — tekst] (※ 초과 굴림 3번째부터 이번 도상의 남은 일반 전투가 모두 정예 전투로 바뀝니다.)
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_elite_conversion_warning].content
   limit: do 120 znaków
   EN: (brak wersji angielskiej)
   PL: (※ Od 3. nadmiarowego rzutu wszystkie pozostałe Zwykłe Starcia tego Schematu zamieniają się w Walki Elitarne.)
86. [Wydarzenia i Przepustka [limtochess_map_unreachable_room] — tekst] 현재 갈 수 없는 표상입니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_unreachable_room].content
   limit: do 120 znaków
   EN: Cannot travel. This Representation is too far away.
   PL: Nie można się tam udać. Ta Reprezentacja jest zbyt daleko.
87. [Wydarzenia i Przepustka [limtochess_map_legend_title] — tekst] 범례
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_title].content
   limit: do 120 znaków
   EN: Legend
   PL: Legenda
88. [Wydarzenia i Przepustka [limtochess_map_legend_normal] — tekst] 일반 전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_normal].content
   limit: do 120 znaków
   EN: Regular Encounter
   PL: Zwykłe starcie
89. [Wydarzenia i Przepustka [limtochess_map_legend_elite] — tekst] 정예 전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_elite].content
   limit: do 120 znaków
   EN: Elite Encounter
   PL: Walka Elitarna
90. [Wydarzenia i Przepustka [limtochess_map_legend_boss] — tekst] 보스 전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_boss].content
   limit: do 120 znaków
   EN: Boss Encounter
   PL: Walka z bossem
91. [Wydarzenia i Przepustka [limtochess_map_legend_rest] — tekst] 휴식
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_rest].content
   limit: do 120 znaków
   EN: Respite
   PL: Wytchnienie
92. [Wydarzenia i Przepustka [limtochess_map_legend_temptation] — tekst] 유혹
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_legend_temptation].content
   limit: do 120 znaków
   EN: Temptation
   PL: Pokusa
93. [Wydarzenia i Przepustka [limtochess_map_section] — tekst] 제 {0}도상
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_section].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Schema {0}
   PL: Schemat {0}
94. [Wydarzenia i Przepustka [limtochess_roll_penalty_title] — tekst] 도상 왜곡
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_title].content
   limit: do 120 znaków
   EN: Schema Deformation
   PL: Wypaczenie Schematu
95. [Wydarzenia i Przepustka [limtochess_roll_penalty_count] — tekst] 도상 왜곡 {0}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Schema Deformation(s)
   PL: Wypaczenia Schematu: {0}
96. [Wydarzenia i Przepustka [limtochess_roll_penalty_next] — tekst] 무작위 왜곡 1개 (후보 {0})
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_next].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 1 Random Deformation (out of {0})
   PL: 1 losowe Wypaczenie (z {0})
97. [Wydarzenia i Przepustka [limtochess_roll_penalty_next_short] — tekst] +1
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_next_short].content
   limit: do 120 znaków
   EN: +1
   PL: +1
98. [Wydarzenia i Przepustka [limtochess_roll_penalty_level] — tekst] 적 레벨 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_level].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy Level +{0}
   PL: Poziom Wroga +{0}
99. [Wydarzenia i Przepustka [limtochess_roll_penalty_clash_power] — tekst] 합 위력 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_clash_power].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Clash Power +{0}
   PL: Moc Starcia +{0}
100. [Wydarzenia i Przepustka [limtochess_roll_penalty_final_power] — tekst] 최종 위력 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_final_power].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Final Power +{0}
   PL: Moc Końcowa +{0}
101. [Wydarzenia i Przepustka [limtochess_roll_penalty_damage] — tekst] 가하는 피해량 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_damage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Deal +{0}% more damage
   PL: Zadawane obrażenia +{0}%
102. [Wydarzenia i Przepustka [limtochess_roll_penalty_max_hp] — tekst] 최대 체력 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_max_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Max HP +{0}%
   PL: Maks. HP +{0}%
103. [Wydarzenia i Przepustka [limtochess_roll_penalty_boss_max_hp] — tekst] 보스 전투 최대 체력 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_boss_max_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Boss Max HP +{0}%
   PL: Maks. HP Bossów +{0}%
104. [Wydarzenia i Przepustka [limtochess_roll_penalty_level_name] — tekst] 적 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_level_name].content
   limit: do 120 znaków
   EN: Enemy Level
   PL: Poziom Wroga
105. [Wydarzenia i Przepustka [limtochess_roll_penalty_clash_power_name] — tekst] 합 위력
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_clash_power_name].content
   limit: do 120 znaków
   EN: Clash Power
   PL: Moc Starcia
106. [Wydarzenia i Przepustka [limtochess_roll_penalty_final_power_name] — tekst] 최종 위력
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_final_power_name].content
   limit: do 120 znaków
   EN: Final Power
   PL: Moc Końcowa
107. [Wydarzenia i Przepustka [limtochess_roll_penalty_damage_name] — tekst] 가하는 피해량
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_damage_name].content
   limit: do 120 znaków
   EN: Damage Dealt
   PL: Zadawane obrażenia
108. [Wydarzenia i Przepustka [limtochess_roll_penalty_max_hp_name] — tekst] 최대 체력
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_max_hp_name].content
   limit: do 120 znaków
   EN: Max HP
   PL: Maks. HP
109. [Wydarzenia i Przepustka [limtochess_roll_penalty_boss_max_hp_name] — tekst] 보스 전투 최대 체력
   źródło: LimtochessUI.json :: dataList[id=limtochess_roll_penalty_boss_max_hp_name].content
   limit: do 120 znaków
   EN: Boss Max HP
   PL: Maks. HP Bossów
110. [Wydarzenia i Przepustka [limtochess_map_setting_title] — tekst] 설정
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_setting_title].content
   limit: do 120 znaków
   EN: Settings
   PL: Ustawienia
111. [Wydarzenia i Przepustka [limtochess_map_setting_leave] — tekst] 잠시 나가기
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_setting_leave].content
   limit: do 120 znaków
   EN: Pause and Exit
   PL: Pauza i wyjście
112. [Wydarzenia i Przepustka [limtochess_map_setting_abandon] — tekst] 도상구축 포기
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_setting_abandon].content
   limit: do 120 znaków
   EN: Forfeit Schemacraft Run
   PL: Porzucić Konstrukcję Schematów
113. [Wydarzenia i Przepustka [limtochess_map_setting_close] — tekst] 닫기
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_setting_close].content
   limit: do 120 znaków
   EN: Close
   PL: Zamknij
114. [Wydarzenia i Przepustka [limtochess_map_setting_wait] — tekst] 지금은 나갈 수 없습니다. 잠시 뒤 다시 시도해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_map_setting_wait].content
   limit: do 120 znaków
   EN: Cannot exit at the moment. Please try again in a moment.
   PL: W tej chwili nie można wyjść. Spróbuj ponownie za chwilę.
115. [Wydarzenia i Przepustka [limtochess_confirm_leave_title] — tekst] 잠시 나가기
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_leave_title].content
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
116. [Wydarzenia i Przepustka [limtochess_confirm_leave_desc] — tekst] 진행 중인 도상구축을 그대로 두고 로비로 나가시겠습니까?\n입장 화면의 '이어하기'로 돌아올 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_leave_desc].content
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Pause the in-progress Schemacraft run and return to the lobby?\nTo resume a paused run, select "Continue" at the lobby.
   PL: Zostawić trwającą Konstrukcję Schematów i wrócić do lobby?\nMożesz wrócić przez „Kontynuuj” na ekranie wejścia.
117. [Wydarzenia i Przepustka [limtochess_confirm_abandon_title] — tekst] 도상구축 포기
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_abandon_title].content
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
118. [Wydarzenia i Przepustka [limtochess_confirm_abandon_desc] — tekst] 이번 도상구축을 포기하시겠습니까?\n지금까지의 진행도에 따라 보상을 받고 종료됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_abandon_desc].content
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Forfeit the Schemacraft run in progress?\nSelecting "Confirm" will forfeit the run and yield the rewards based on your current Schemacraft progress.
   PL: Porzucić tę Konstrukcję Schematów?\nOtrzymasz nagrody stosownie do dotychczasowego postępu, a rozgrywka się zakończy.
119. [Wydarzenia i Przepustka [limtochess_report_title] — tekst] 전투 리포트
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_title].content
   limit: do 120 znaków
   EN: Battle Report
   PL: Raport z walki
120. [Wydarzenia i Przepustka [limtochess_report_tab_hp] — tekst] 진영별 체력
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_tab_hp].content
   limit: do 120 znaków
   EN: Ally / Enemy HP Graph
   PL: Wykres PŻ obu stron
121. [Wydarzenia i Przepustka [limtochess_report_ally] — tekst] 아군
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_ally].content
   limit: do 120 znaków
   EN: Allies
   PL: Sojusznicy
122. [Wydarzenia i Przepustka [limtochess_report_enemy] — tekst] 적
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_enemy].content
   limit: do 120 znaków
   EN: Enemies
   PL: Wrogowie
123. [Wydarzenia i Przepustka [limtochess_report_legend_death] — tekst] 사망
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_legend_death].content
   limit: do 120 znaków
   EN: Death
   PL: MARTWY
124. [Wydarzenia i Przepustka [limtochess_report_legend_ego] — tekst] E.G.O 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_legend_ego].content
   limit: do 120 znaków
   EN: E.G.O Use
   PL: Użycie E.G.O
125. [Wydarzenia i Przepustka [limtochess_report_detail_ally_death] — tekst] 아군 사망
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_detail_ally_death].content
   limit: do 120 znaków
   EN: Ally Death
   PL: Śmierć Sojusznika
126. [Wydarzenia i Przepustka [limtochess_report_detail_ego] — tekst] E.G.O 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_detail_ego].content
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
127. [Wydarzenia i Przepustka [limtochess_report_retry_title] — tekst] 재전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_retry_title].content
   limit: do 120 znaków
   EN: Retry Battle
   PL: Ponów walkę
128. [Wydarzenia i Przepustka [limtochess_report_retry_desc] — tekst] 같은 전투를 바로 다시 시작하시겠습니까?\n취소하면 도상으로 돌아가며, 이 전투에 다시 들어갈 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_retry_desc].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Retry this Encounter now?\nSelect "Cancel" to return to the Schema map. You may choose to enter this Encounter again.
   PL: Natychmiast powtórzyć tę walkę?\nWybór „Anuluj” wraca do Schematu — do tej walki można wejść ponownie.
129. [Wydarzenia i Przepustka [limtochess_report_retry_button] — tekst] 재도전 (남은 횟수 <color=#6F87FF>{2}</color>)
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_retry_button].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#6F87FF>, </color>, {2}
   EN: Retry (Remaining: {2})
   PL: Ponów (pozostało: <color=#6F87FF>{2}</color>)
130. [Wydarzenia i Przepustka [limtochess_report_retry_button_unlimited] — tekst] 재도전 <color=#6F87FF>{0}</color>
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_retry_button_unlimited].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#6F87FF>, </color>, {0}
   EN: Retry <color=#6F87FF>{0}</color>
   PL: Ponów <color=#6F87FF>{0}</color>
131. [Wydarzenia i Przepustka [limtochess_final_clear] — tekst] CLEAR
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_clear].content
   limit: do 120 znaków
   EN: CLEARED
   PL: CLEAR
132. [Wydarzenia i Przepustka [limtochess_final_fail] — tekst] FAIL
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_fail].content
   limit: do 120 znaków
   EN: FAILED
   PL: FAIL
133. [Wydarzenia i Przepustka [limtochess_report_defeat_title] — tekst] 구축 실패
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_defeat_title].content
   limit: do 120 znaków
   EN: SCHEMA FAILED
   PL: KONSTRUKCJA NIEUDANA
134. [Wydarzenia i Przepustka [limtochess_report_defeat_title_alt] — tekst] 구축 실패
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_defeat_title_alt].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
135. [Wydarzenia i Przepustka [limtochess_report_p0_line] — tekst] 공통 주기 {0} · 합 {1}승 {2}패 · 일방 아군 {3}/적 {4} · 정신력 {5}→{6} · 사망 {7} · 수비 발동 {8}/충족 {9}/큐 부족 {10}
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_p0_line].content
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}
   EN: Shared Turn(s) {0} · Clashes: {1} Won, {2} Lost · Unopp. Atk.: Allies {3} / Enemies {4} · SP {5} → {6} · Killed {7} · Def. Activated {8} / Cond. Met {9} / Queue Missed {10}
   PL: Tury wspólne {0} · Starcia: {1} wygrane, {2} przegrane · Ataki bez oporu: Sojusznicy {3}/Wrogowie {4} · PP {5}→{6} · Polegli {7} · Garda: aktywacje {8}/warunki {9}/brak w kolejce {10}
136. [Wydarzenia i Przepustka [limtochess_report_p0_death] — tekst] {0} ← {1}「{2}」
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_p0_death].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} ← {1}「{2}」
   PL: {0} ← {1}「{2}」
137. [Wydarzenia i Przepustka [limtochess_report_p0_death_more] — tekst] {0} 외 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_p0_death_more].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} and {1} other
   PL: {0} i {1} innych
138. [Wydarzenia i Przepustka [limtochess_report_p0_death_noskill] — tekst] {0} ← {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_p0_death_noskill].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} ← {1}
   PL: {0} ← {1}
139. [Wydarzenia i Przepustka [limtochess_final_stage] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} / {1}
   PL: {0}/{1}
140. [Wydarzenia i Przepustka [limtochess_final_time] — tekst] 총 소요 시간 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_time].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Total Elapsed Time {0}
   PL: Łączny czas: {0}
141. [Wydarzenia i Przepustka [limtochess_final_count] — tekst] {0}<color=#a16a3b>/{1}</color>
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a16a3b>, </color>, {0}, {1}
   EN: {0}<color=#a16a3b>/1</color>
   PL: {0}<color=#a16a3b>/{1}</color>
142. [Wydarzenia i Przepustka [limtochess_final_complete] — tekst] 완성
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_complete].content
   limit: do 120 znaków
   EN: Complete
   PL: Gotowe
143. [Wydarzenia i Przepustka [limtochess_final_incomplete] — tekst] 미완성
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_incomplete].content
   limit: do 120 znaków
   EN: Incomplete
   PL: Niegotowe
144. [Wydarzenia i Przepustka [limtochess_final_gift_enhance] — tekst] {0} +{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_gift_enhance].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} +{1}
   PL: {0} +{1}
145. [Wydarzenia i Przepustka [limtochess_final_empty] — tekst] -
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_empty].content
   limit: do 120 znaków
   EN: -
   PL: -
146. [Wydarzenia i Przepustka [limtochess_final_ego] — tekst] E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_ego].content
   limit: do 120 znaków
   EN: E.G.O
   PL: E.G.O
147. [Wydarzenia i Przepustka [limtochess_rest_mp_title] — tekst] 정신력 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_mp_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: SP +{0}
   PL: PP +{0}
148. [Wydarzenia i Przepustka [limtochess_rest_mp_desc] — tekst] 현재 평균 {0} → {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_mp_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Current Avg. {0} → {1}
   PL: Obecna średnia {0} → {1}
149. [Wydarzenia i Przepustka [limtochess_rest_reroll_title] — tekst] 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_reroll_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reshuffles +{0}
   PL: Odświeżenia +{0}
150. [Wydarzenia i Przepustka [limtochess_rest_reroll_desc] — tekst] 팩 · 인격 · E.G.O 교체에 쓸 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_reroll_desc].content
   limit: do 120 znaków
   EN: Used to reshuffle Packs / Identities / E.G.O.
   PL: Służy do odświeżania Pakietów, Tożsamości i E.G.O.
151. [Wydarzenia i Przepustka [limtochess_rest_syncup_title] — tekst] 인격 1명 동기화 +{0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_syncup_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie +{0} for 1 Identity
   PL: Synchronizacja +{0} dla 1 Tożsamości
152. [Wydarzenia i Przepustka [limtochess_rest_syncup_desc] — tekst] 전투 편성 내 동기화 {0}단계 이하 인격 1명을 고릅니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_syncup_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select 1 Identity from the Team to Uptie. Must be Uptie {0} or lower.
   PL: Wybierz 1 Tożsamość ze składu bojowego na Synchronizacji {0} lub niższej.
153. [Wydarzenia i Przepustka [limtochess_rest_syncup_disabled] — tekst] 동기화를 올릴 수 있는 인격이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_syncup_disabled].content
   limit: do 120 znaków
   EN: No Identities available for Uptie.
   PL: Brak Tożsamości, które można zsynchronizować.
154. [Wydarzenia i Przepustka [limtochess_rest_syncup_unowned_cap] — tekst] 계정에서 보유하지 않은 인격은 최대 동기화 단계가 {0}단계로 제한됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_syncup_unowned_cap].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Identities not in account are limited to Uptie {0}.
   PL: Tożsamości nieposiadane na koncie mają Synchronizację ograniczoną do {0}.
155. [Wydarzenia i Przepustka [limtochess_rest_freeroll_title] — tekst] 추가 굴림 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_freeroll_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Bonus Roll(s) +{0}
   PL: Rzuty dodatkowe +{0}
156. [Wydarzenia i Przepustka [limtochess_rest_freeroll_carry] — tekst] 쓰지 않은 추가 굴림은 다음 도상으로 이어집니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_freeroll_carry].content
   limit: do 120 znaków
   EN: Unused Bonus Rolls carry over to the next Schema.
   PL: Niewykorzystane Rzuty dodatkowe przechodzą na następny Schemat.
157. [Wydarzenia i Przepustka [limtochess_rest_generic_label] — tekst] 범용 조각
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_label].content
   limit: do 120 znaków
   EN: Universal Sliver
   PL: Okruch Uniwersalny
158. [Wydarzenia i Przepustka [limtochess_rest_generic_use] — tekst] 범용 조각 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_use].content
   limit: do 120 znaków
   EN: Use Universal Sliver(s)
   PL: Użycie Okruchów Uniwersalnych
159. [Wydarzenia i Przepustka [limtochess_rest_generic_desc] — tekst] 범용 조각으로 동기화 {1}단계 이하 인격을 동기화할 수 있습니다.\n※ 필요 범용 조각 (동기화 1/2/3단계) : 4/6/6개\n※ 보유한 인격 조각 1개당 필요한 범용 조각이 2개씩 줄어듭니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_desc].content
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: {1}, \n
   EN: Use Universal Slivers to Uptie Identities at Uptie {1} or lower.\n※ Needs 4/6/6 Universal Slivers for ID Uptie 1/2/3, respectively.\n※ Each Identity Sliver in your possession reduces Universal Sliver requirement by 2.
   PL: Okruchami Uniwersalnymi można synchronizować Tożsamości na Synchronizacji {1} lub niższej.\n※ Potrzebne Okruchy Uniwersalne (Synchronizacja 1/2/3): 4/6/6\n※ Za 1 posiadany Skrawek Tożsamości wymaganie spada o 2 Okruchy Uniwersalne.
160. [Wydarzenia i Przepustka [limtochess_rest_generic_none] — tekst] 범용 조각으로 동기화할 수 있는 인격이 없습니다. (동기화 {0}단계 이하 인격만 가능)
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_none].content
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No Identities available for Uptie via Universal Sliver. (available only for Identities at Uptie {0} or lower)
   PL: Brak Tożsamości do synchronizacji Okruchami Uniwersalnymi. (tylko Synchronizacja {0} lub niższa)
161. [Wydarzenia i Przepustka [limtochess_rest_generic_confirm] — tekst] 범용 조각을 사용하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_confirm].content
   limit: do 120 znaków
   EN: Use Universal Slivers?
   PL: Użyć Okruchów Uniwersalnych?
162. [Wydarzenia i Przepustka [limtochess_rest_growth_title] — tekst] 휴식 : 성장
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_growth_title].content
   limit: do 120 znaków
   EN: Respite: Upgrade
   PL: Wytchnienie: Rozwój
163. [Wydarzenia i Przepustka [limtochess_rest_generic_title] — tekst] 범용 조각 사용
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_title].content
   (powtórzenie elementu 158 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
164. [Wydarzenia i Przepustka [limtochess_rest_empty] — tekst] 비어 있음
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_empty].content
   limit: do 120 znaków
   EN: Unequipped
   PL: Nie wyposażono
165. [Wydarzenia i Przepustka [limtochess_bossreward_empty_slot] — tekst] 비어 있음
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_empty_slot].content
   (powtórzenie elementu 164 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
166. [Wydarzenia i Przepustka [limtochess_rest_sync_change] — tekst] 동기화 {0}단계 → 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_sync_change].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} → Uptie {1}
   PL: Synchronizacja {0} → Synchronizacja {1}
167. [Wydarzenia i Przepustka [limtochess_rest_sync_cap] — tekst] 동기화 {0}단계 상한
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_sync_cap].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie Limit at Tier {0}
   PL: Limit Synchronizacji {0}
168. [Wydarzenia i Przepustka [limtochess_rest_generic_need] — tekst] 범용 {0}개 필요
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_generic_need].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Universal Slivers required
   PL: Potrzeba {0} Okruchów Uniwersalnych
169. [Wydarzenia i Przepustka [limtochess_rest_not_target] — tekst] 대상 아님
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_not_target].content
   limit: do 120 znaków
   EN: Ineligible
   PL: Niekwalifikuje się
170. [Wydarzenia i Przepustka [limtochess_rest_select] — tekst] 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_rest_select].content
   limit: do 120 znaków
   EN: Select
   PL: Wybierz
171. [Wydarzenia i Przepustka [limtochess_current_deck] — tekst] 편성 확인
   źródło: LimtochessUI.json :: dataList[id=limtochess_current_deck].content
   limit: do 120 znaków
   EN: View Team
   PL: Zobacz skład
172. [Wydarzenia i Przepustka [limtochess_current_deck_sync] — tekst] 동기화 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_current_deck_sync].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Wydarzenia i Przepustka [limtochess_giftstatus_title] — tekst] E.G.O 기프트 현황
   źródło: LimtochessUI.json :: dataList[id=limtochess_giftstatus_title].content
   limit: do 120 znaków
   EN: E.G.O Gift Status
   PL: Stan Darów E.G.O
174. [Wydarzenia i Przepustka [limtochess_tempt_title_original] — tekst] 유혹
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_title_original].content
   (powtórzenie elementu 92 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Wydarzenia i Przepustka [limtochess_tempt_original_title] — tekst] 동기화 {0}단계 인격 + E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_original_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtain Uptie {0} Identity + E.G.O
   PL: Tożsamość na Synchronizacji {0} + E.G.O
176. [Wydarzenia i Przepustka [limtochess_tempt_recruit] — tekst] {0} 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_recruit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Add {0} to Team
   PL: {0} do składu
177. [Wydarzenia i Przepustka [limtochess_tempt_replace] — tekst] {0} 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace {0}
   PL: Wymiana {0}
178. [Wydarzenia i Przepustka [limtochess_tempt_replace_before] — tekst] 기존 인격 {0} 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_replace_before].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Current ID: {0} · Uptie {1}
   PL: Obecna Tożsamość: {0} · Synchronizacja {1}
179. [Wydarzenia i Przepustka [limtochess_tempt_ego_equip] — tekst] {0} {1} {2}단계 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_ego_equip].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Equip {0} {1} at Tier {2}
   PL: Wyposaż {0} {1} — Stopień {2}
180. [Wydarzenia i Przepustka [limtochess_tempt_ego_no_slot] — tekst] 장착할 수 있는 빈 E.G.O 칸이 없어 E.G.O는 받지 못합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_ego_no_slot].content
   limit: do 120 znaków
   EN: No E.G.O will be received because there are no available E.G.O slots.
   PL: Brak wolnego gniazda E.G.O — nie otrzymasz E.G.O.
181. [Wydarzenia i Przepustka [limtochess_tempt_ego_none] — tekst] 받을 수 있는 E.G.O가 없어 E.G.O는 받지 못합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_ego_none].content
   limit: do 120 znaków
   EN: There is no E.G.O available to receive.
   PL: Brak dostępnego E.G.O — nie otrzymasz E.G.O.
182. [Wydarzenia i Przepustka [limtochess_tempt_skip_title] — tekst] 받지 않기
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_skip_title].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
183. [Wydarzenia i Przepustka [limtochess_tempt_skip_desc] — tekst] 지금 전투 편성을 유지합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_skip_desc].content
   limit: do 120 znaków
   EN: Keep your current Team.
   PL: Zachowaj obecny skład bojowy.
184. [Wydarzenia i Przepustka [limtochess_tempt_roll_cost] — tekst] 주사위 굴림 {1}회 차감
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_roll_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}
   EN: Lose {1} Dice Reroll(s)
   PL: Utrata {1} rzutów kością
185. [Wydarzenia i Przepustka [limtochess_tempt_roll_free] — tekst] 주사위 굴림 차감 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_roll_free].content
   limit: do 120 znaków
   EN: No Dice Reroll loss
   PL: Bez utraty rzutów kością
186. [Wydarzenia i Przepustka [limtochess_tempt_roll_penalty] — tekst] 남은 굴림 개수가 부족하여 도상 왜곡 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_roll_penalty].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Not enough Rerolls. Schema Deformation +{0}
   PL: Za mało rzutów — Wypaczenie Schematu +{0}
187. [Wydarzenia i Przepustka [limtochess_tempt_before_label] — tekst] 기존 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_before_label].content
   limit: do 120 znaków
   EN: Current Identity
   PL: Obecna Tożsamość
188. [Wydarzenia i Przepustka [limtochess_tempt_before_sync] — tekst] 동기화
   źródło: LimtochessUI.json :: dataList[id=limtochess_tempt_before_sync].content
   limit: do 120 znaków
   EN: Uptie
   PL: Synchronizacja
189. [Wydarzenia i Przepustka [limtochess_battleprep_level_label] — tekst] 현재 인격 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_battleprep_level_label].content
   limit: do 120 znaków
   EN: Current ID Lvl.
   PL: Poziom Tożsamości
190. [Wydarzenia i Przepustka [limtochess_briefing_threat_title] — tekst] 위협 등급
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_title].content
   limit: do 120 znaków
   EN: Threat Level
   PL: Poziom Zagrożenia
191. [Wydarzenia i Przepustka [limtochess_briefing_threat_reason] — tekst] 레벨 차이 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_reason].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Level Gap {0}
   PL: Różnica poziomów {0}
192. [Wydarzenia i Przepustka [limtochess_briefing_threat_reason_script] — tekst] 레벨 차이 {0} · {2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_reason_script].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {2}
   EN: Level Gap {0} · {2}
   PL: Różnica poziomów {0} · {2}
193. [Wydarzenia i Przepustka [limtochess_briefing_threat_script_1] — tekst] 정예 +1
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_script_1].content
   limit: do 120 znaków
   EN: Elite +1
   PL: Elita +1
194. [Wydarzenia i Przepustka [limtochess_briefing_threat_script_2] — tekst] 보스 +2
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_threat_script_2].content
   limit: do 120 znaków
   EN: Boss +2
   PL: Boss +2
195. [Wydarzenia i Przepustka [limtochess_briefing_weak_label] — tekst] 약점
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_weak_label].content
   limit: do 120 znaków
   EN: Weakness
   PL: Słaba
196. [Wydarzenia i Przepustka [limtochess_briefing_weak_none] — tekst] 약점 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_weak_none].content
   limit: do 120 znaków
   EN: No Weaknesses
   PL: Brak Słabych
197. [Wydarzenia i Przepustka [limtochess_briefing_egores_title] — tekst] 획득 자원
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_egores_title].content
   limit: do 120 znaków
   EN: Resource Gain
   PL: Zysk zasobów
198. [Wydarzenia i Przepustka [limtochess_briefing_egores_demand] — tekst] 필요 자원
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_egores_demand].content
   limit: do 120 znaków
   EN: Resource Req.
   PL: Wymagane zasoby
199. [Wydarzenia i Przepustka [limtochess_briefing_appear] — tekst] 명 출현
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_appear].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Enemies\nFeatured
   PL: wrogów wystąpi
200. [Wydarzenia i Przepustka [limtochess_briefing_reinforce] — tekst] 전투 중 적 {0}명 추가 등장
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_reinforce].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} enemy reinforcements
   PL: W trakcie walki pojawi się dodatkowo {0} wrogów
201. [Wydarzenia i Przepustka [limtochess_briefing_refill_card] — tekst] 증원 {0}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_briefing_refill_card].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Backup(s)
   PL: Wzmocnienia: {0}
202. [Wydarzenia i Przepustka [limtochess_packselect_screen_title] — tekst] 전투 보상 : 팩 고르기
   źródło: LimtochessUI.json :: dataList[id=limtochess_packselect_screen_title].content
   limit: do 120 znaków
   EN: Battle Reward: Pack Choice
   PL: Nagroda za walkę: Wybór Pakietu
203. [Wydarzenia i Przepustka [limtochess_elite_screen_title] — tekst] 정예 보상 : 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_screen_title].content
   limit: do 120 znaków
   EN: Choose Elite Reward
   PL: Nagroda elit: Wybór
204. [Wydarzenia i Przepustka [limtochess_bossreward_screen_title] — tekst] 도상 클리어 보상
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_screen_title].content
   limit: do 120 znaków
   EN: Schema Clear Rewards
   PL: Nagrody za ukończenie Schematu
205. [Wydarzenia i Przepustka [limtochess_bossreward_progress] — tekst] 완성 : 동기화 4단계 {0}/{1}명 · E.G.O 조건 {2}/{1}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_progress].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Team Built: {0}/{1} Uptie 4 Units; {2}/{1} E.G.O Equipped
   PL: Gotowość: {0}/{1} Tożsamości na Synchronizacji 4; {2}/{1} z E.G.O
206. [Wydarzenia i Przepustka [limtochess_bossreward_reroll_title] — tekst] 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_reroll_title].content
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
207. [Wydarzenia i Przepustka [limtochess_bossreward_reroll_desc] — tekst] 새로고침 기회를 {0}회 얻습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_reroll_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Reshuffle(s) gained.
   PL: Zyskujesz {0} odświeżeń.
208. [Wydarzenia i Przepustka [limtochess_bossreward_sync_under_title] — tekst] 동기화 {0}단계 이하인 인격 1명의 동기화 단계 +{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_sync_under_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie +{1} for 1 Identity with {0} or lower Uptie Tier
   PL: Synchronizacja +{1} dla 1 Tożsamości na Synchronizacji {0} lub niższej
209. [Wydarzenia i Przepustka [limtochess_bossreward_sync_plus_title] — tekst] 동기화 {0}단계 이하인 인격 1명의 동기화 단계 +{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_sync_plus_title].content
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Wydarzenia i Przepustka [limtochess_bossreward_sync_desc] — tekst] 조건에 맞는 인격 {0}명 중 1명을 고릅니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_sync_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select 1 of {0} Identities that fulfil the conditions.
   PL: Wybierz 1 z {0} Tożsamości spełniających warunki.
211. [Wydarzenia i Przepustka [limtochess_bossreward_sync_disabled] — tekst] 동기화를 올릴 수 있는 인격이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_sync_disabled].content
   (powtórzenie elementu 153 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Wydarzenia i Przepustka [limtochess_bossreward_generic_title] — tekst] 범용 조각 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_generic_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Universal Sliver +{0}
   PL: Okruchy Uniwersalne +{0}
213. [Wydarzenia i Przepustka [limtochess_bossreward_generic_desc] — tekst] 범용 조각이 +{0} 추가됩니다. 휴식에서 다른 인격의 동기화를 올릴 때 씁니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_generic_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtain +{0} Universal Slivers. Used to Uptie other Identities at Respites.
   PL: Zyskujesz +{0} Okruchów Uniwersalnych — służą do synchronizacji innych Tożsamości w Wytchnieniach.
214. [Wydarzenia i Przepustka [limtochess_bossreward_gift_pick] — tekst] 도상 클리어 보상 : 기프트 강화
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_gift_pick].content
   limit: do 120 znaków
   EN: Schema Clear Rewards: Gift Upgrade
   PL: Nagrody za ukończenie Schematu: Wzmocnienie Daru
215. [Wydarzenia i Przepustka [limtochess_bossreward_gift_pick_count] — tekst] 도상 클리어 보상 : 기프트 강화 ({0}/{1})
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_gift_pick_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Schema Clear Rewards: Gift Upgrade ({0}/{1})
   PL: Nagrody za ukończenie Schematu: Wzmocnienie Daru ({0}/{1})
216. [Wydarzenia i Przepustka [limtochess_bossreward_sync_pick] — tekst] 도상 클리어 보상 : 성장
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_sync_pick].content
   limit: do 120 znaków
   EN: Schema Clear Rewards: Upgrade
   PL: Nagrody za ukończenie Schematu: Rozwój
217. [Wydarzenia i Przepustka [limtochess_bossreward_pack_random] — tekst] + 무작위 팩 1개 ({0}등급)
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_pack_random].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: + 1 Random Pack (Tier {0})
   PL: + 1 losowy Pakiet (Tier {0})
218. [Wydarzenia i Przepustka [limtochess_bossreward_pack_sinner] — tekst] + 선택한 수감자 팩 1개 ({0}등급)
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_pack_sinner].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: + Obtain 1 Pack for a selected Sinner (Tier {0})
   PL: + 1 Pakiet dla wybranego Grzesznika (Tier {0})
219. [Wydarzenia i Przepustka [limtochess_bossreward_pack_sinner_pick] — tekst] 도상 클리어 보상 : 수감자 팩
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_pack_sinner_pick].content
   limit: do 120 znaków
   EN: Schema Clear Rewards: Sinner Packs
   PL: Nagrody za ukończenie Schematu: Pakiety Grzeszników
220. [Wydarzenia i Przepustka [limtochess_bossreward_pack_sinner_change] — tekst] 수감자 팩 {0}등급
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_pack_sinner_change].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Tier {0} Sinner Pack
   PL: Pakiet Grzesznika Tier {0}
221. [Wydarzenia i Przepustka [limtochess_bossreward_pack_sinner_not_joined] — tekst] 편성 밖 — 인격 카드로 영입
   źródło: LimtochessUI.json :: dataList[id=limtochess_bossreward_pack_sinner_not_joined].content
   limit: do 120 znaków
   EN: Not in Team — Recruit via Identity Card
   PL: Poza składem — werbunek kartą Tożsamości
222. [Wydarzenia i Przepustka [limtochess_gauge_cycle] — tekst] TURN {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_gauge_cycle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: TURN {0}
   PL: TURN {0}
223. [Wydarzenia i Przepustka [limtochess_unitstatus_break] — tekst] 흐트러짐
   źródło: LimtochessUI.json :: dataList[id=limtochess_unitstatus_break].content
   limit: do 120 znaków
   EN: STAGGER
   PL: OSZOŁOMIENIE
224. [Wydarzenia i Przepustka [limtochess_unitstatus_panic] — tekst] 패닉
   źródło: LimtochessUI.json :: dataList[id=limtochess_unitstatus_panic].content
   limit: do 120 znaków
   EN: Panic
   PL: Panika
225. [Wydarzenia i Przepustka [limtochess_unitstatus_erode] — tekst] 침식
   źródło: LimtochessUI.json :: dataList[id=limtochess_unitstatus_erode].content
   limit: do 120 znaków
   EN: Corrosion
   PL: Korozja
226. [Wydarzenia i Przepustka [limtochess_skillart_awaken] — tekst] 각성
   źródło: LimtochessUI.json :: dataList[id=limtochess_skillart_awaken].content
   limit: do 120 znaków
   EN: Awakening
   PL: Przebudzenie
227. [Wydarzenia i Przepustka [limtochess_skillart_erosion] — tekst] 침식
   źródło: LimtochessUI.json :: dataList[id=limtochess_skillart_erosion].content
   (powtórzenie elementu 225 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
228. [Wydarzenia i Przepustka [limtochess_unitstatus_lowmorale] — tekst] 동요
   źródło: LimtochessUI.json :: dataList[id=limtochess_unitstatus_lowmorale].content
   limit: do 120 znaków
   EN: Uneasy
   PL: Zaniepokojenie
229. [Wydarzenia i Przepustka [limtochess_egobar_auto_target] — tekst] 자동 타겟
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_auto_target].content
   limit: do 120 znaków
   EN: Auto-targeted
   PL: Automatyczny cel
230. [Wydarzenia i Przepustka [limtochess_egobar_waiting] — tekst] 발동 대기
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_waiting].content
   limit: do 120 znaków
   EN: Activation Standby
   PL: Oczekiwanie na aktywację
231. [Wydarzenia i Przepustka [limtochess_egobar_waiting_target] — tekst] 발동 대기 → {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_waiting_target].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Acitvation Standby → {0}
   PL: Oczekiwanie na aktywację → {0}
232. [Wydarzenia i Przepustka [limtochess_egobar_lethal] — tekst] 사망 직전
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_lethal].content
   limit: do 120 znaków
   EN: Death Imminent
   PL: Tuż przed śmiercią
233. [Wydarzenia i Przepustka [limtochess_egobar_aimed] — tekst] 타겟됨 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_aimed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Targeted {0}
   PL: Wybrano jako cel {0}
234. [Wydarzenia i Przepustka [limtochess_egobar_retreat] — tekst] 퇴각 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_retreat].content
   limit: do 120 znaków
   EN: Retreating
   PL: W Odwrocie
235. [Wydarzenia i Przepustka [limtochess_egobar_block_defect] — tekst] 결함
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_block_defect].content
   limit: do 120 znaków
   EN: Defective
   PL: Uszkodzony
236. [Wydarzenia i Przepustka [limtochess_egobar_block_inactionable] — tekst] 행동 불가
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_block_inactionable].content
   limit: do 120 znaków
   EN: Immobilized
   PL: Unieruchomiony
237. [Wydarzenia i Przepustka [limtochess_egobar_block_resource] — tekst] 자원 부족
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_block_resource].content
   limit: do 120 znaków
   EN: Lack Resources
   PL: Brak zasobów
238. [Wydarzenia i Przepustka [limtochess_egobar_block_unusable] — tekst] 사용 불가
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_block_unusable].content
   limit: do 120 znaków
   EN: Cannot Use
   PL: Nie można użyć
239. [Wydarzenia i Przepustka [limtochess_egobar_onesided] — tekst] 일방 공격
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_onesided].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unopp.\nAtk
   PL: Atak bez oporu
240. [Wydarzenia i Przepustka [limtochess_egobar_resonance] — tekst] 공명
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_resonance].content
   limit: do 120 znaków
   EN: Resonance
   PL: Rezonans
241. [Wydarzenia i Przepustka [limtochess_egobar_notice_lack] — tekst] 자원 부족 — {0} 더 필요
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_notice_lack].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Missing Resources — Need {0} more
   PL: Brak zasobów — potrzeba jeszcze {0}
242. [Wydarzenia i Przepustka [limtochess_egobar_notice_no_overclock] — tekst] 오버클록 불가 — 침식 스킬 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_egobar_notice_no_overclock].content
   limit: do 120 znaków
   EN: Cannot Overclock — No Corr. Skill
   PL: Przeciążenie niemożliwe — brak Umiejętności Korozji
243. [Wydarzenia i Przepustka [limtochess_roominfo_pack_label] — tekst] {0}등급 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_pack_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Tier {0} {1}
   PL: Tier {0} {1}
244. [Wydarzenia i Przepustka [limtochess_battle_pause] — tekst] 정지
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_pause].content
   limit: do 120 znaków
   EN: Pause
   PL: Pauza
245. [Wydarzenia i Przepustka [limtochess_battle_resume] — tekst] 재개
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_resume].content
   limit: do 120 znaków
   EN: Resume
   PL: Wznów
246. [Wydarzenia i Przepustka [limtochess_battle_speed] — tekst] {0}x
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_speed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: x{0}
   PL: {0}x
247. [Wydarzenia i Przepustka [limtochess_battle_resume_hint] — tekst] [재개]를 눌러 계속
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_resume_hint].content
   limit: do 120 znaków
   EN: Press the [Play/Pause] button to continue
   PL: Wciśnij [Wznów], aby kontynuować
248. [Wydarzenia i Przepustka [limtochess_battle_resume_hint_key] — tekst] [재개]를 눌러 계속
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_resume_hint_key].content
   (powtórzenie elementu 247 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Wydarzenia i Przepustka [limtochess_battle_tail_speed] — tekst] 후반 배속 {0}x
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_tail_speed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Tail-end Fast-forward x{0}
   PL: Przyspieszenie końcówki {0}x
250. [Wydarzenia i Przepustka [limtochess_battle_toggle_damage] — tekst] 대미지 숫자
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_toggle_damage].content
   limit: do 120 znaków
   EN: Damage Numbers
   PL: Liczby obrażeń
251. [Wydarzenia i Przepustka [limtochess_battle_toggle_ally_cards] — tekst] 아군 카드
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_toggle_ally_cards].content
   limit: do 120 znaków
   EN: Ally Cards
   PL: Karty sojuszników
252. [Wydarzenia i Przepustka [limtochess_battle_toggle_enemy_cards] — tekst] 적 카드
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_toggle_enemy_cards].content
   limit: do 120 znaków
   EN: Enemy Cards
   PL: Karty wrogów
253. [Wydarzenia i Przepustka [limtochess_battle_stage] — tekst] 제 {0}도상 {1}스테이지
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_stage].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Schema {0} Stage {1}
   PL: Schemat {0} Etap {1}
254. [Wydarzenia i Przepustka [limtochess_battle_turn] — tekst] 공통 턴 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_turn].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Shared Turn {0}
   PL: Tura wspólna {0}
255. [Wydarzenia i Przepustka [limtochess_report_seconds] — tekst] {0}s
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_seconds].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}s
   PL: {0}s
256. [Wydarzenia i Przepustka [limtochess_report_time] — tekst] 소요 시간
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_time].content
   limit: do 120 znaków
   EN: Elapsed Time
   PL: Upływ czasu
257. [Wydarzenia i Przepustka [limtochess_roominfo_enemy_avg_level] — tekst] 적 평균 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_enemy_avg_level].content
   limit: do 120 znaków
   EN: Enemy Avg. Lvl
   PL: Średni poziom wrogów
258. [Wydarzenia i Przepustka [limtochess_gauge_skill_tier] — tekst] 스킬 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_gauge_skill_tier].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Skill {0}
   PL: Umiejętność {0}
259. [Wydarzenia i Przepustka [limtochess_gauge_clash] — tekst] 합 진행
   źródło: LimtochessUI.json :: dataList[id=limtochess_gauge_clash].content
   limit: do 120 znaków
   EN: Clash
   PL: Starcie
260. [Wydarzenia i Przepustka [limtochess_gauge_onesided] — tekst] 일방 공격
   źródło: LimtochessUI.json :: dataList[id=limtochess_gauge_onesided].content
   limit: do 120 znaków
   EN: Unopposed Attack
   PL: Atak bez oporu
261. [Wydarzenia i Przepustka [limtochess_battle_retry_used_up] — tekst] 마지막 재도전입니다 — 패배하면 도상구축이 종료됩니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_retry_used_up].content
   limit: do 120 znaków
   EN: This is your last Retry! Defeat will end this Schemacraft run.
   PL: To Twoje ostatnie ponowienie — porażka zakończy Konstrukcję Schematów
262. [Wydarzenia i Przepustka [limtochess_battle_retry_count] — tekst] 재도전 {0}회 사용 (남은 횟수 {2})
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_retry_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {2}
   EN: {0} Retries used (Remaining: {2})
   PL: Użyto ponowień: {0} (pozostało: {2})
263. [Wydarzenia i Przepustka [limtochess_battle_retry_count_unlimited] — tekst] 재도전 {0}회 사용(무제한)
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_retry_count_unlimited].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Retries used (Unlimited)
   PL: Użyto ponowień: {0} (bez limitu)
264. [Wydarzenia i Przepustka [limtochess_battle_retry_confirm_title] — tekst] 전투 재도전
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_retry_confirm_title].content
   limit: do 120 znaków
   EN: Retry Battle
   PL: Ponów walkę
265. [Wydarzenia i Przepustka [limtochess_battle_retry_confirm_desc] — tekst] 다시 시작하면 재도전 기회를 1회 사용합니다 (남은 횟수 {2}).\n다시 시작하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_retry_confirm_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {2}, \n
   EN: Restarting will consume 1 Retry token. (Remaining: {2})\nRestart?
   PL: Ponowny start zużyje 1 ponowienie (pozostało: {2}).\nZacząć ponownie?
266. [Wydarzenia i Przepustka [limtochess_battle_giveup_confirm_title] — tekst] 전투 포기
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_giveup_confirm_title].content
   limit: do 120 znaków
   EN: Forfeit Battle
   PL: Poddaj walkę
267. [Wydarzenia i Przepustka [limtochess_battle_giveup_confirm_desc] — tekst] 포기하면 재도전 기회를 1회 사용합니다 (남은 횟수 {2}).\n도상으로 돌아가며, 이 전투에 다시 들어갈 수 있습니다. 포기하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_giveup_confirm_desc].content
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: {2}, \n
   EN: Forfeiting will consume 1 Retry token. (Remaining: {2})\nYou will be returned to the Schema map, and can choose to enter this Encounter again. Forfeit?
   PL: Poddanie zużyje 1 ponowienie (pozostało: {2}).\nWrócisz do Schematu i będziesz mógł ponownie wejść do tej walki. Poddaj walkę?
268. [Wydarzenia i Przepustka [limtochess_battle_giveup_confirm_desc_last] — tekst] 재도전 횟수를 모두 사용했습니다.\n포기하면 이번 도상구축이 종료됩니다. 포기하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_giveup_confirm_desc_last].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Retries exhausted.\nForfeiting will end this Schemacraft run. Forfeit?
   PL: Wykorzystano wszystkie ponowienia.\nPoddanie zakończy tę Konstrukcję Schematów. Poddaj walkę?
269. [Wydarzenia i Przepustka [limtochess_room_info_elite_fx] — tekst] 정예 효과
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_info_elite_fx].content
   limit: do 120 znaków
   EN: Elite Effects
   PL: Efekty Elit
270. [Wydarzenia i Przepustka [limtochess_elite_fx_brawler] — tekst] 싸움꾼
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_brawler].content
   limit: do 120 znaków
   EN: Brawlers
   PL: Bijacze
271. [Wydarzenia i Przepustka [limtochess_elite_fx_brawler_desc] — tekst] 모든 적의 합 위력 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_brawler_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All enemies gain Clash Power +{0}
   PL: Moc Starcia wszystkich wrogów +{0}
272. [Wydarzenia i Przepustka [limtochess_elite_fx_footwork] — tekst] 발놀림
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_footwork].content
   limit: do 120 znaków
   EN: Footwork
   PL: Praca Nóg
273. [Wydarzenia i Przepustka [limtochess_elite_fx_footwork_desc] — tekst] 모든 적의 속도 최솟값·최댓값 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_footwork_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All enemies' Min & Max Speed +{0}
   PL: Min. i maks. Szybkość wszystkich wrogów +{0}
274. [Wydarzenia i Przepustka [limtochess_elite_fx_weapon] — tekst] 연장
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_weapon].content
   limit: do 120 znaków
   EN: Tools of the Trade
   PL: Narzędzia Fachu
275. [Wydarzenia i Przepustka [limtochess_elite_fx_weapon_desc] — tekst] 모든 적이 가하는 피해량 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_weapon_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All enemies deal +{0}% more damage
   PL: Wszyscy wrogowie zadają +{0}% obrażeń
276. [Wydarzenia i Przepustka [limtochess_elite_fx_firststrike] — tekst] 선제공격
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_firststrike].content
   limit: do 120 znaków
   EN: Strike First
   PL: Pierwszy Cios
277. [Wydarzenia i Przepustka [limtochess_elite_fx_firststrike_desc] — tekst] 전장에 등장한 적이 {0}턴 동안 가하는 피해량 +{1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_firststrike_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Enemies on the field deal +{1}% more damage for {0} turns
   PL: Wrogowie na polu zadają +{1}% obrażeń przez {0} tur
278. [Wydarzenia i Przepustka [limtochess_elite_fx_tough] — tekst] 맷집
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_tough].content
   limit: do 120 znaków
   EN: Hardy
   PL: Twardziel
279. [Wydarzenia i Przepustka [limtochess_elite_fx_tough_desc] — tekst] 모든 적의 최대 체력 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_tough_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All enemies' Max HP +{0}%
   PL: Maks. HP wszystkich wrogów +{0}%
280. [Wydarzenia i Przepustka [limtochess_elite_fx_struggle] — tekst] 발버둥
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_struggle].content
   limit: do 120 znaków
   EN: Tantrum
   PL: Furia
281. [Wydarzenia i Przepustka [limtochess_elite_fx_struggle_desc] — tekst] 턴 시작 시 체력 50% 이하인 적이 피해량 증가 {0}, 신속 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_struggle_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Turn Start: Enemies at 50% or lower HP gain {0} Damage Up and {1} Haste
   PL: Początek tury: wrogowie z HP 50% lub niższym zyskują {0} Wzrostu Obrażeń i {1} Pośpiechu
282. [Wydarzenia i Przepustka [limtochess_elite_fx_boss] — tekst] 두목
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_boss].content
   limit: do 120 znaków
   EN: Big Boss
   PL: Szef Szefów
283. [Wydarzenia i Przepustka [limtochess_elite_fx_boss_desc] — tekst] 스테이지 시작 시 최대 체력이 가장 높은 적 1명의 최대 체력 +{0}%, 가하는 피해량 +{1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_boss_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Encounter Start: 1 enemy with the highest HP gain Max HP +{0}% and deal +{1}% more damage
   PL: Początek spotkania: 1 wrog z najwyższym HP zyskuje Maks. HP +{0}% i zadaje +{1}% obrażeń
284. [Wydarzenia i Przepustka [limtochess_elite_fx_brawl] — tekst] 막싸움
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_brawl].content
   limit: do 120 znaków
   EN: Backstreets Fighters
   PL: Zaułkowa Bijatyka
285. [Wydarzenia i Przepustka [limtochess_elite_fx_brawl_desc] — tekst] 적이 가하는 피해량 +{0}%, 적이 받는 피해량 +{1}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_brawl_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Enemies deal +{0}% damage and take +{1}% damage
   PL: Wrogowie zadają +{0}% obrażeń i otrzymują +{1}% obrażeń
286. [Wydarzenia i Przepustka [limtochess_elite_fx_loyalty] — tekst] 의리
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_loyalty].content
   limit: do 120 znaków
   EN: Loyalty
   PL: Braterstwo
287. [Wydarzenia i Przepustka [limtochess_elite_fx_loyalty_desc] — tekst] 적 사망 시 전장의 다른 모든 적이 다음 턴에 공격 레벨 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_loyalty_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: When an enemy is defeated, all other enemies gain Offense Level {0} next turn
   PL: Gdy wrogi zostanie pokonany, wszyscy pozostali wrogowie zyskują {0} Poziomu Ataku w następnej turze
288. [Wydarzenia i Przepustka [limtochess_elite_fx_interest] — tekst] 이자
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_interest].content
   limit: do 120 znaków
   EN: With Interest
   PL: Odsetki
289. [Wydarzenia i Przepustka [limtochess_elite_fx_interest_desc] — tekst] 모든 적의 공격 레벨 +{0}, 턴이 지날 때마다 +{1}씩 (합산 최대 +{2})
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_interest_desc].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: All enemies gain Offense Level +{0}; increases by +{1} with each passing turn (max total +{2})
   PL: Poziom Ataku wszystkich wrogów +{0}, rośnie o +{1} z każdą turą (łącznie maks. +{2})
290. [Wydarzenia i Przepustka [limtochess_elite_fx_companion] — tekst] 길동무
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_companion].content
   limit: do 120 znaków
   EN: Taking You With Me
   PL: Towarzysz Drogi
291. [Wydarzenia i Przepustka [limtochess_elite_fx_companion_desc] — tekst] 적이 받는 스킬 피해 +{0}% 대신, 받은 최종 피해량의 {1}%를 공격한 수감자에게 되돌림
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_companion_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Enemies take +{0}% Skill damage; reflect {1}% of the final damage taken to the Sinner
   PL: Wrogowie otrzymują +{0}% obrażeń Umiejętności, a {1}% otrzymanych obrażeń końcowych wraca do atakującego Grzesznika
292. [Wydarzenia i Przepustka [limtochess_elite_fx_intimidate] — tekst] 위압
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_intimidate].content
   limit: do 120 znaków
   EN: Domineer
   PL: Zastraszanie
293. [Wydarzenia i Przepustka [limtochess_elite_fx_intimidate_desc] — tekst] 수감자가 합 패배 시 또는 다른 수감자 사망 시 잃는 정신력 {0}배
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_intimidate_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lose x{0} SP when a Sinner loses a Clash or when another Sinner is defeated
   PL: Utrata ×{0} PP, gdy Grzesznik przegra Starcie lub gdy inny Grzesznik zginie
294. [Wydarzenia i Przepustka [limtochess_elite_fx_backer] — tekst] 뒷배
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_backer].content
   limit: do 120 znaków
   EN: Got Your Back
   PL: Poparcie
295. [Wydarzenia i Przepustka [limtochess_elite_fx_backer_desc] — tekst] 대기 중인 적이 전장에 나올 때마다 정신력이 있는 모든 적의 정신력 +{0}, 다음 턴 신속 {1}·더하기 코인 강화 {2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_elite_fx_backer_desc].content
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Whenever a Backup enemy enters the field, all SP unit enemies heal +{0} SP, then gain {1} Haste and {2} Plus Coin Boost next turn
   PL: Gdy Wzmocnienie wchodzi na pole, wszyscy wrogowie z PP lecą się o {0} PP, a w następnej turze zyskują {1} Pośpiechu i {2} Wzmocnienia Monet Plus
296. [Wydarzenia i Przepustka [limtochess_event_deck_title] — tekst] 선택지 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_deck_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Choice {0}
   PL: Opcja {0}
297. [Wydarzenia i Przepustka [limtochess_event_deck_text] — tekst] 덱을 다듬을 기회다. 고른 칸의 대가는 판이 끝날 때까지 모든 적에게 걸린다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_deck_text].content
   limit: do 120 znaków
   EN: Time to hone the Team. All enemies gain the "Consequences" until the end of the run.
   PL: Czas doszlifować skład. Wybrana przestrzeń obdarzy wszystkich wrogów „Konsekwencjami” do końca rozgrywki.
298. [Wydarzenia i Przepustka [limtochess_event_boss_title] — tekst] 보스 선택지 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Boss Choice {0}
   PL: Opcja Bossa {0}
299. [Wydarzenia i Przepustka [limtochess_event_boss_text] — tekst] 이번 판의 최종 보스를 정한다. 대가는 없다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_text].content
   limit: do 120 znaków
   EN: Select the final boss of this run. There are no Consequences.
   PL: Wybierz finałowego bossa tej rozgrywki. Bez Konsekwencji.
300. [Wydarzenia i Przepustka [limtochess_event_effect_none] — tekst] 효과 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_none].content
   limit: do 120 znaków
   EN: No effect
   PL: Bez efektu
301. [Wydarzenia i Przepustka [limtochess_event_effect_reroll_segment] — tekst] 이번 도상 새로고침 기회 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_reroll_segment].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reshuffles for this Schema +{0}
   PL: Odświeżenia tego Schematu +{0}
302. [Wydarzenia i Przepustka [limtochess_event_effect_reroll_carry] — tekst] 새로고침 기회 +{0} (다음 도상 이월)
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_reroll_carry].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Reshuffles +{0} (carries over to the next Schema)
   PL: Odświeżenia +{0} (przechodzą na następny Schemat)
303. [Wydarzenia i Przepustka [limtochess_event_effect_sync_pick] — tekst] 고른 인격 {0}명 동기화 +1단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_sync_pick].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie +1 for {0} selected ID(s)
   PL: Synchronizacja +1 dla {0} wybranych Tożsamości
304. [Wydarzenia i Przepustka [limtochess_event_effect_sync_pick_set] — tekst] 고른 인격 {0}명 동기화 {1}단계로
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_sync_pick_set].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} selected ID(s) to Uptie {1}
   PL: Synchronizacja wybranych {0} Tożsamości na poziom {1}
305. [Wydarzenia i Przepustka [limtochess_event_effect_sync_random] — tekst] 무작위 인격 {0}명 동기화 +1단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_sync_random].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie +1 for {0} random ID(s)
   PL: Synchronizacja +1 dla {0} losowych Tożsamości
306. [Wydarzenia i Przepustka [limtochess_event_effect_recruit_pick] — tekst] 편성에 없는 수감자 1명 영입\n동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_recruit_pick].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {1}, \n
   EN: Recruit 1 Sinner not in the Team\nRecruited at Uptie {1}
   PL: Zrekrutuj 1 Grzesznika spoza składu\nSynchronizacja {1}
307. [Wydarzenia i Przepustka [limtochess_event_effect_pack_random] — tekst] 무작위 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_random].content
   limit: do 120 znaków
   EN: Obtain a random Pack
   PL: Zdobądź losowy Pakiet
308. [Wydarzenia i Przepustka [limtochess_event_effect_pack_keyword] — tekst] 고른 키워드의 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_keyword].content
   limit: do 120 znaków
   EN: Select and obtain a Keyword Pack
   PL: Zdobądź Pakiet wybranego Słowa Kluczowego
309. [Wydarzenia i Przepustka [limtochess_event_effect_pack_random_grade] — tekst] 무작위 {0}등급 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_random_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtain a Tier {0} Pack
   PL: Zdobądź losowy Pakiet Tier {0}
310. [Wydarzenia i Przepustka [limtochess_event_effect_pack_keyword_grade] — tekst] 고른 키워드의 {0}등급 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_keyword_grade].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select and obtain a Tier {0} Keyword Pack
   PL: Zdobądź Pakiet Tier {0} wybranego Słowa Kluczowego
311. [Wydarzenia i Przepustka [limtochess_event_effect_ego_pick] — tekst] 편성 수감자의 E.G.O 1개 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_ego_pick].content
   limit: do 120 znaków
   EN: Equip 1 E.G.O for a Sinner in the Team
   PL: Wyposaż 1 E.G.O dla Grzesznika w składzie
312. [Wydarzenia i Przepustka [limtochess_event_effect_ego_keyword] — tekst] 고른 키워드의 E.G.O 1개 장착
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_ego_keyword].content
   limit: do 120 znaków
   EN: Equip 1 E.G.O from the selected Keyword
   PL: Wyposaż 1 E.G.O wybranego Słowa Kluczowego
313. [Wydarzenia i Przepustka [limtochess_event_effect_reroll_to_generic] — tekst] 남은 새로고침 기회 {0}개당 범용 조각 1개로 교환
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_reroll_to_generic].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obtain 1 Universal Sliver for every {0} remaining Reshuffle
   PL: Za każde {0} pozostałych odświeżeń: 1 Okruch Uniwersalny
314. [Wydarzenia i Przepustka [limtochess_event_effect_swap_affiliation_random] — tekst] 무작위 수감자 {0}명을 같은 소속 인격으로 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_affiliation_random].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace the ID(s) of {0} random Sinners with ID(s) of the same faction
   PL: Wymień Tożsamości {0} losowych Grzeszników na Tożsamości tej samej Przynależności
315. [Wydarzenia i Przepustka [limtochess_event_effect_swap_affiliation_pick] — tekst] 수감자 1명을 같은 소속 인격으로 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_affiliation_pick].content
   limit: do 120 znaków
   EN: Replace 1 Sinner's ID with an ID of the same faction
   PL: Wymień Tożsamość 1 Grzesznika na Tożsamość tej samej Przynależności
316. [Wydarzenia i Przepustka [limtochess_event_effect_cost_up_tail] — tekst] {0}% 확률로 코스트 +1
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_cost_up_tail].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: {0}% chance for Cost +1
   PL: {0}% szans na Koszt +1
317. [Wydarzenia i Przepustka [limtochess_event_effect_swap_pick] — tekst] 편성 수감자 1명을 다른 인격으로 교체\n동기화 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_pick].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Replace 1 Sinner in the Team with a different Identity\nUptie Tier carries over
   PL: Wymień 1 Grzesznika ze składu na inną Tożsamość\nSynchronizacja bez zmian
318. [Wydarzenia i Przepustka [limtochess_event_effect_swap_all_cost_up] — tekst] 편성 전원을 무작위 인격으로 교체\n동기화 유지 · {0}% 확률로 코스트 +1
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_all_cost_up].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Replace the entire Team with different, random Identities\nUptie Tier carries over; {0} chance for Cost +1
   PL: Wymień cały skład na losowe Tożsamości\nSynchronizacja bez zmian · {0}% szans na Koszt +1
319. [Wydarzenia i Przepustka [limtochess_event_effect_swap_one_random] — tekst] 무작위 수감자 1명을 무작위 인격으로 교체\n동기화 무작위
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_one_random].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Replace 1 random Sinner in the Team with a random Identity\nUptie Tier randomized
   PL: Wymień 1 losowego Grzesznika na losową Tożsamość\nSynchronizacja losowa
320. [Wydarzenia i Przepustka [limtochess_event_effect_swap_one_cost_up] — tekst] 무작위 수감자 1명을 무작위 인격으로 교체\n동기화 유지 · {0}% 확률로 코스트 +1
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_one_cost_up].content
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Replace 1 random Sinner in the Team with a random Identity\nUptie Tier carries over; {0}% chance for Cost +1
   PL: Wymień 1 losowego Grzesznika na losową Tożsamość\nSynchronizacja bez zmian · {0}% szans na Koszt +1
321. [Wydarzenia i Przepustka [limtochess_event_effect_pack_grade_open] — tekst] 새로고침 기회 {0}회 소모 · 무작위 {1}등급 팩 획득
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_grade_open].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Spend {0} Reshuffles left · Obtain a Tier {1} Pack
   PL: Koszt: {0} odświeżeń · Zdobądź losowy Pakiet Tier {1}
322. [Wydarzenia i Przepustka [limtochess_event_effect_pack_sync_tail] — tekst] 인격 동기화 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_pack_sync_tail].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: ID Uptie Tier {0}
   PL: Synchronizacja Tożsamości: {0}
323. [Wydarzenia i Przepustka [limtochess_event_reroll_left] — tekst] 남은 새로고침 기회 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_reroll_left].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Remaining Reshuffles: {0}
   PL: Pozostałe odświeżenia: {0}
324. [Wydarzenia i Przepustka [limtochess_event_effect_swap_cost_up_pick] — tekst] 고른 수감자 1명을 코스트 +1 인격으로 교체\n동기화 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_cost_up_pick].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Select and replace 1 Sinner with an Identity of 1 higher Cost\nUptie Tier carries over
   PL: Wybierz i wymień 1 Grzesznika na Tożsamość o Koszcie +1\nSynchronizacja bez zmian
325. [Wydarzenia i Przepustka [limtochess_event_effect_swap_cost_up_pick_multi] — tekst] 고른 수감자 {0}명을 코스트 +1 인격으로 교체\n동기화 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_cost_up_pick_multi].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Select and replace {0} Sinner(s) with an Identity of 1 higher Cost\nUptie Tier carries over
   PL: Wybierz i wymień {0} Grzesznika(-ów) na Tożsamości o Koszcie +1\nSynchronizacja bez zmian
326. [Wydarzenia i Przepustka [limtochess_event_effect_swap_one_pick] — tekst] 고른 수감자 1명을 무작위 인격으로 교체\n동기화 유지 · 코스트 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_swap_one_pick].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Select and replace 1 Sinner with a random Identity\nUptie Tier carries over; Cost {0}
   PL: Wybierz i wymień 1 Grzesznika na losową Tożsamość\nSynchronizacja bez zmian · Koszt {0}
327. [Wydarzenia i Przepustka [limtochess_event_effect_final_boss] — tekst] 최종 보스 → {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_final_boss].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Final Boss → {0}
   PL: Boss Finałowy → {0}
328. [Wydarzenia i Przepustka [limtochess_event_effect_segment_boss] — tekst] 제 {0}도상 보스 → {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_segment_boss].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Schema {0} Boss → {1}
   PL: Boss Schematu {0} → {1}
329. [Wydarzenia i Przepustka [limtochess_event_effect_segment_pool] — tekst] 제 {0}도상 전투가 {1}의 적으로 바뀜
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_segment_pool].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Schema {0} Encounters will feature enemies from {1}
   PL: Walki Schematu {0} będą toczyć się z wrogami z {1}
330. [Wydarzenia i Przepustka [limtochess_event_effect_stage_unlock] — tekst] 보스 변경 없음 · 보스 선택지 {0} 등장 가능
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_stage_unlock].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No change to the boss · Boss Option {0} may appear
   PL: Boss bez zmian · może pojawić się Opcja Bossa {0}
331. [Wydarzenia i Przepustka [limtochess_event_effect_decline] — tekst] 보스 변경 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_effect_decline].content
   limit: do 120 znaków
   EN: No change to the boss
   PL: Boss bez zmian
332. [Wydarzenia i Przepustka [limtochess_event_locked] — tekst] 미해금 — {0} 격파 필요
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_locked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Locked: Defeat {0}
   PL: Zablokowane — pokonaj {0}
333. [Wydarzenia i Przepustka [limtochess_event_hardship_hp] — tekst] 모든 적의 체력 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_hardship_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All enemies gain HP +{0}%
   PL: HP wszystkich wrogów +{0}%
334. [Wydarzenia i Przepustka [limtochess_event_hardship_dmg] — tekst] 모든 적이 가하는 피해량 +{0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_hardship_dmg].content
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Wydarzenia i Przepustka [limtochess_event_hardship_none] — tekst] 고난 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_hardship_none].content
   limit: do 120 znaków
   EN: No Obstacle
   PL: Brak Prób
336. [Wydarzenia i Przepustka [limtochess_event_pick_cost_up_sinner] — tekst] 코스트 +1 인격으로 바꿀 수감자를 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_cost_up_sinner].content
   limit: do 120 znaków
   EN: Select the Sinner to be replaced with an Identity of 1 higher Cost.
   PL: Wybierz Grzesznika do wymiany na Tożsamość o Koszcie +1.
337. [Wydarzenia i Przepustka [limtochess_event_pick_swap_one_sinner] — tekst] 무작위 인격으로 바꿀 수감자를 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_swap_one_sinner].content
   limit: do 120 znaków
   EN: Select the Sinner to be replaced with a random Identity.
   PL: Wybierz Grzesznika do wymiany na losową Tożsamość.
338. [Wydarzenia i Przepustka [limtochess_event_pick_sinner] — tekst] 동기화를 올릴 인격을 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_sinner].content
   limit: do 120 znaków
   EN: Select the Identity to Uptie.
   PL: Wybierz Tożsamość do synchronizacji.
339. [Wydarzenia i Przepustka [limtochess_event_pick_personality] — tekst] 영입할 인격을 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_personality].content
   limit: do 120 znaków
   EN: Select the Identity to recruit.
   PL: Wybierz Tożsamość do werbunku.
340. [Wydarzenia i Przepustka [limtochess_event_pick_ego] — tekst] 장착할 E.G.O를 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_ego].content
   limit: do 120 znaków
   EN: Select the E.G.O to equip.
   PL: Wybierz E.G.O do wyposażenia.
341. [Wydarzenia i Przepustka [limtochess_event_pick_keyword] — tekst] 받을 팩의 키워드를 고르세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_keyword].content
   limit: do 120 znaków
   EN: Select the Pack Keyword.
   PL: Wybierz Słowo Kluczowe Pakietu.
342. [Wydarzenia i Przepustka [limtochess_event_boss_name_jun] — tekst] 흑운회 부조장 쥰
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_name_jun].content
   limit: do 120 znaków
   EN: Kurokumo Clan Captain Jun
   PL: Jun, Kapitan Klanu Kurokumo
343. [Wydarzenia i Przepustka [limtochess_event_boss_name_ricardo] — tekst] 리카르도
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_name_ricardo].content
   limit: do 120 znaków
   EN: Ricardo
   PL: Ricardo
344. [Wydarzenia i Przepustka [limtochess_event_boss_name_cleaners] — tekst] 도시의 청소부
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_name_cleaners].content
   limit: do 120 znaków
   EN: The City's Sweepers
   PL: Sprzątacze Miasta
345. [Wydarzenia i Przepustka [limtochess_event_boss_name_alley] — tekst] 골목 파수견·포레그
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_name_alley].content
   limit: do 120 znaków
   EN: Alleyway Watchdog & Four-legs
   PL: Pies Stróżujący Zaułków i Cztery Łapy
346. [Wydarzenia i Przepustka [limtochess_event_boss_name_blackcloud] — tekst] 흑운회
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_name_blackcloud].content
   limit: do 120 znaków
   EN: Kurokumo Clan
   PL: Klan Kurokumo
347. [Wydarzenia i Przepustka [limtochess_event_skip_text] — tekst] 무작위 패널티 1개 (정신력·조각·체력·공격 레벨·합 위력 감소)
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_skip_text].content
   limit: do 120 znaków
   EN: Random Penalty x1 (selected from: SP/Sliver/HP/Offense Level/Clash Power loss)
   PL: Losowa Kara ×1 (utrata PP/Skrawków/HP/Poziomu Ataku/Mocy Starcia)
348. [Wydarzenia i Przepustka [limtochess_event_skip_short] — tekst] 받지 않기
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_skip_short].content
   (powtórzenie elementu 27 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Wydarzenia i Przepustka [limtochess_event_skip_text_reserve_roll] — tekst] 무작위 패널티 1개 (정신력·조각·체력·공격 레벨·합 위력 감소)
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_skip_text_reserve_roll].content
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Wydarzenia i Przepustka [limtochess_event_skip_short_reserve_roll] — tekst] 받지 않기 · 추가 굴림 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_skip_short_reserve_roll].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decline & Bonus Roll(s) +{0}
   PL: Odrzuć · Rzuty dodatkowe +{0}
351. [Wydarzenia i Przepustka [limtochess_event_penalty_none] — tekst] 패널티 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_none].content
   limit: do 120 znaków
   EN: No Penalties
   PL: Brak Kar
352. [Wydarzenia i Przepustka [limtochess_event_penalty_mentalall] — tekst] 편성 수감자 전원 정신력 −{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_mentalall].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: All Sinners in the Team: SP -{0}
   PL: Wszyscy Grzesznicy w składzie tracą {0} PP
353. [Wydarzenia i Przepustka [limtochess_event_penalty_mentalrandom] — tekst] 무작위 수감자 {0}명 정신력 −{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_mentalrandom].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} Random Sinners: SP -{1}
   PL: {0} losowych Grzeszników traci {1} PP
354. [Wydarzenia i Przepustka [limtochess_event_penalty_fragmentsinner] — tekst] 수감자 {0}의 동기화 조각을 0으로
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_fragmentsinner].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}'s Uptie Sliver reduced to 0
   PL: Skrawki Synchronizacji Grzesznika {0} spadają do 0
355. [Wydarzenia i Przepustka [limtochess_event_penalty_fragmentgeneric] — tekst] 범용 조각 {0}개 잃음
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_fragmentgeneric].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Lost {0} Universal Slivers
   PL: Utracone Okruchy Uniwersalne: {0}
356. [Wydarzenia i Przepustka [limtochess_event_penalty_hpall] — tekst] 스테이지 시작 시 출격 아군 전원 최대 체력의 {0}% 체력 감소
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_hpall].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Encounter Start: All fielded Identities lose {0}% HP
   PL: Początek Etapu: wszyscy wystawieni Sojusznicy tracą {0}% HP
357. [Wydarzenia i Przepustka [limtochess_event_penalty_hprandom] — tekst] 스테이지 시작 시 무작위 출격 아군 {0}명 최대 체력의 {1}% 체력 감소
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_hprandom].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Encounter Start: {0} random fielded Identities lose {1}% HP
   PL: Początek Etapu: {0} losowych wystawionych Sojuszników traci {1}% HP
358. [Wydarzenia i Przepustka [limtochess_event_penalty_attackdownall] — tekst] 스테이지 시작 시 출격 아군 전원 공격 레벨 감소 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_attackdownall].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Encounter Start: All fielded Identities lose {0} Offense Level
   PL: Początek Etapu: wszyscy wystawieni Sojusznicy tracą {0} Poziomu Ataku
359. [Wydarzenia i Przepustka [limtochess_event_penalty_attackdownrandom] — tekst] 스테이지 시작 시 무작위 출격 아군 {0}명 공격 레벨 감소 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_attackdownrandom].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Encounter Start: {0} random fielded Identities lose {1} Offense Level
   PL: Początek Etapu: {0} losowych wystawionych Sojuszników traci {1} Poziomu Ataku
360. [Wydarzenia i Przepustka [limtochess_event_penalty_clashdownall] — tekst] 스테이지 시작 시 출격 아군 전원 합 위력 감소 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_clashdownall].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Encounter Start: All fielded Identities lose {0} Clash Power
   PL: Początek Etapu: wszyscy wystawieni Sojusznicy tracą {0} Mocy Starcia
361. [Wydarzenia i Przepustka [limtochess_event_penalty_clashdownrandom] — tekst] 스테이지 시작 시 무작위 출격 아군 {0}명 합 위력 감소 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_clashdownrandom].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Encounter Start: {0} random fielded Identities lose {1} Clash Power
   PL: Początek Etapu: {0} losowych wystawionych Sojuszników traci {1} Mocy Starcia
362. [Wydarzenia i Przepustka [limtochess_event_penalty_pending] — tekst] 다음 전투 패널티 {0}개
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_pending].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Penalty(ies) in the next Encounter
   PL: Kary w następnej walce: {0}
363. [Wydarzenia i Przepustka [limtochess_event_penalty_label] — tekst] 패널티
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_penalty_label].content
   limit: do 120 znaków
   EN: Penalties
   PL: Kary
364. [Wydarzenia i Przepustka [limtochess_hud_hardship] — tekst] 고난 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Obstacle: {0}
   PL: Próba: {0}
365. [Wydarzenia i Przepustka [limtochess_hud_segment_penalty] — tekst] 도상 왜곡 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_segment_penalty].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Schema Deformation: {0}
   PL: Wypaczenie Schematu: {0}
366. [Wydarzenia i Przepustka [limtochess_hud_none] — tekst] 없음
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_none].content
   limit: do 120 znaków
   EN: None
   PL: Brak
367. [Wydarzenia i Przepustka [limtochess_hud_hardship_hp] — tekst] 적 체력 {0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship_hp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy HP {0}%
   PL: HP wrogów {0}%
368. [Wydarzenia i Przepustka [limtochess_hud_hardship_dmg] — tekst] 적 피해량 {0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship_dmg].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Enemy Damage {0}%
   PL: Obrażenia wrogów {0}%
369. [Wydarzenia i Przepustka [limtochess_hud_hardship_atk] — tekst] 공격 레벨 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship_atk].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Offense Level {0}
   PL: Poziom Ataku {0}
370. [Wydarzenia i Przepustka [limtochess_hud_hardship_def] — tekst] 방어 레벨 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship_def].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Defense Level {0}
   PL: Poziom Obrony {0}
371. [Wydarzenia i Przepustka [limtochess_hud_hardship_order] — tekst] 고른 고난 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_hardship_order].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Selected Obstacle: {0}
   PL: Wybrana Próba: {0}
372. [Wydarzenia i Przepustka [limtochess_hud_penalty_order] — tekst] 적용 순서 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_penalty_order].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Order: {0}
   PL: Kolejność stosowania: {0}
373. [Wydarzenia i Przepustka [limtochess_hud_penalty_target_all] — tekst] 도상 왜곡은 이번 도상의 모든 전투에 적용됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_penalty_target_all].content
   limit: do 120 znaków
   EN: Schema Deformation affects all Encounters in this Schema.
   PL: Wypaczenie Schematu dotyczy wszystkich walk tego Schematu.
374. [Wydarzenia i Przepustka [limtochess_hud_penalty_target_boss] — tekst] 도상 왜곡은 이번 도상의 보스 전투에 적용됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_hud_penalty_target_boss].content
   limit: do 120 znaków
   EN: Schema Deformation affects the Boss Encounter in this Schema.
   PL: Wypaczenie Schematu dotyczy walki z bossem tego Schematu.
375. [Wydarzenia i Przepustka [limtochess_event_pick_swap] — tekst] 바꿔 들일 인격을 고르세요. (동기화 유지)
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_swap].content
   limit: do 120 znaków
   EN: Select the Identity to Swap in. (Uptie Tier carries over)
   PL: Wybierz Tożsamość do wprowadzenia. (Synchronizacja bez zmian)
376. [Wydarzenia i Przepustka [limtochess_synergy_line] — tekst] 시너지 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Synergy: {0}
   PL: Synergia: {0}
377. [Wydarzenia i Przepustka [limtochess_synergy_more] — tekst] +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_more].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: +{0}
   PL: +{0}
378. [Wydarzenia i Przepustka [limtochess_synergy_strength_1] — tekst] 약
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_strength_1].content
   limit: do 120 znaków
   EN: Weak
   PL: Słaba
379. [Wydarzenia i Przepustka [limtochess_synergy_strength_2] — tekst] 중
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_strength_2].content
   limit: do 120 znaków
   EN: Average
   PL: Średnia
380. [Wydarzenia i Przepustka [limtochess_synergy_strength_3] — tekst] 강
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_strength_3].content
   limit: do 120 znaków
   EN: Powerful
   PL: Silna
381. [Wydarzenia i Przepustka [limtochess_synergy_set_full_stop_office] — tekst] 마침표 사무소
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_full_stop_office].content
   limit: do 120 znaków
   EN: Full-Stop Office
   PL: Biuro Kropki
382. [Wydarzenia i Przepustka [limtochess_synergy_set_black_beast_hongyuan_lord] — tekst] 흑수 + 홍원 군주 홍루
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_black_beast_hongyuan_lord].content
   limit: do 120 znaków
   EN: The Heishou + The Lord of Hongyuan Hong Lu
   PL: Heishou + Władca Hongyuanu Hong Lu
383. [Wydarzenia i Przepustka [limtochess_synergy_set_black_beast_horse_family_ga] — tekst] 흑수 - 오 필두 이상 + 가주 후보 이스마엘
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_black_beast_horse_family_ga].content
   limit: do 120 znaków
   EN: Heishou Pack - Wu Branch Adept Yi Sang + Family Hierarch Candidate Ishmael
   PL: Wataha Heishou - Adept Gałęzi Wu Yi Sang + Kandydatka na Głowę Rodu Ishmael
384. [Wydarzenia i Przepustka [limtochess_synergy_set_blade_lineage] — tekst] 검계
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_blade_lineage].content
   limit: do 120 znaków
   EN: Blade Lineage
   PL: Ród Ostrza
385. [Wydarzenia i Przepustka [limtochess_synergy_set_blade_lineage_chakyeong_hwido] — tekst] 검계 + 착영휘도
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_blade_lineage_chakyeong_hwido].content
   limit: do 120 znaków
   EN: Blade Lineage + Shadow-vested Bladesinger
   PL: Ród Ostrza + Pieśniarz Ostrza w Szacie Cieni
386. [Wydarzenia i Przepustka [limtochess_synergy_set_black_cloud] — tekst] 흑운회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_black_cloud].content
   (powtórzenie elementu 346 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Wydarzenia i Przepustka [limtochess_synergy_set_wedge_office] — tekst] 쐐기 사무소
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_wedge_office].content
   limit: do 120 znaków
   EN: Wedge Office
   PL: Biuro Klina
388. [Wydarzenia i Przepustka [limtochess_synergy_set_wedge_dawn_office] — tekst] 쐐기 + 새벽 사무소
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_wedge_dawn_office].content
   limit: do 120 znaków
   EN: Wedge + Dawn Office
   PL: Klin + Biuro Świtu
389. [Wydarzenia i Przepustka [limtochess_synergy_set_dawn_office] — tekst] 새벽 사무소
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_dawn_office].content
   limit: do 120 znaków
   EN: Dawn Office
   PL: Biuro Świtu
390. [Wydarzenia i Przepustka [limtochess_synergy_set_spider_house] — tekst] 거미집
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_spider_house].content
   limit: do 120 znaków
   EN: The House of Spiders
   PL: Dom Pajęczyn
391. [Wydarzenia i Przepustka [limtochess_synergy_set_spider_house_thumb] — tekst] 거미집 엄지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_spider_house_thumb].content
   limit: do 120 znaków
   EN: The House of Spiders: The Thumb
   PL: Dom Pajęczyn: Kciuk
392. [Wydarzenia i Przepustka [limtochess_synergy_set_spider_house_middle] — tekst] 거미집 중지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_spider_house_middle].content
   limit: do 120 znaków
   EN: The House of Spiders: The Middle
   PL: Dom Pajęczyn: Środkowy
393. [Wydarzenia i Przepustka [limtochess_synergy_set_spider_house_ring] — tekst] 거미집 약지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_spider_house_ring].content
   limit: do 120 znaków
   EN: The House of Spiders: The Ring
   PL: Dom Pajęczyn: Serdeczny
394. [Wydarzenia i Przepustka [limtochess_synergy_set_ring_finger] — tekst] 약지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ring_finger].content
   limit: do 120 znaków
   EN: The Ring
   PL: Serdeczny
395. [Wydarzenia i Przepustka [limtochess_synergy_set_ring_finger_fauvism] — tekst] 약지 야수파
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ring_finger_fauvism].content
   limit: do 120 znaków
   EN: Fauvists of the Ring
   PL: Fowiści Serdecznego
396. [Wydarzenia i Przepustka [limtochess_synergy_set_index_finger] — tekst] 검지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_index_finger].content
   limit: do 120 znaków
   EN: The Index
   PL: Wskazujący
397. [Wydarzenia i Przepustka [limtochess_synergy_set_thumb_finger] — tekst] 엄지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_thumb_finger].content
   limit: do 120 znaków
   EN: The Thumb
   PL: Kciuk
398. [Wydarzenia i Przepustka [limtochess_synergy_set_middle_finger] — tekst] 중지
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_middle_finger].content
   limit: do 120 znaków
   EN: The Middle
   PL: Środkowy
399. [Wydarzenia i Przepustka [limtochess_synergy_set_middle_finger_spider_house] — tekst] 중지·거미집
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_middle_finger_spider_house].content
   limit: do 120 znaków
   EN: The Middle & The House of Spiders
   PL: Środkowy i Dom Pajęczyn
400. [Wydarzenia i Przepustka [limtochess_synergy_set_le_rouge] — tekst] 르루주
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_le_rouge].content
   limit: do 120 znaków
   EN: Le Rouge
   PL: Le Rouge
401. [Wydarzenia i Przepustka [limtochess_synergy_set_le_noir] — tekst] 르누아르
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_le_noir].content
   limit: do 120 znaków
   EN: Le Noir
   PL: Le Noir
402. [Wydarzenia i Przepustka [limtochess_synergy_set_la_mancha_land] — tekst] 라만차랜드
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_la_mancha_land].content
   limit: do 120 znaków
   EN: La Manchaland
   PL: La Manchaland
403. [Wydarzenia i Przepustka [limtochess_synergy_set_la_mancha_land_mircalla] — tekst] 라만차랜드 + 갈망-미르칼라
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_la_mancha_land_mircalla].content
   limit: do 120 znaków
   EN: La Manchaland + Yearning-Mircalla
   PL: La Manchaland + Tęsknota-Mircalla
404. [Wydarzenia i Przepustka [limtochess_synergy_set_n_corp_ego] — tekst] N사 E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_n_corp_ego].content
   limit: do 120 znaków
   EN: N Corp. E.G.O
   PL: E.G.O Korp. N
405. [Wydarzenia i Przepustka [limtochess_synergy_set_n_corp_fanatic] — tekst] N사 광신도
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_n_corp_fanatic].content
   limit: do 120 znaków
   EN: N Corp. Fanatic
   PL: Fanatyk Korp. N
406. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_solemn_lament] — tekst] 엄숙한 애도
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_solemn_lament].content
   limit: do 120 znaków
   EN: Solemn Lament
   PL: Uroczysty Lament
407. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_hyungtan] — tekst] 흉탄
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_hyungtan].content
   limit: do 120 znaków
   EN: Fell Bullet
   PL: Złowroga Kula
408. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_gyeongmyeol_gyeongoe] — tekst] 경멸, 경외
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_gyeongmyeol_gyeongoe].content
   limit: do 120 znaków
   EN: Contempt, Awe
   PL: Pogarda, Trwoga
409. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_hongyeomsal] — tekst] 홍염살
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_hongyeomsal].content
   limit: do 120 znaków
   EN: Ardor Blossom Star
   PL: Gwiazda Żarzącego Kwiatu
410. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_aedd] — tekst] AEDD
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_aedd].content
   limit: do 120 znaków
   EN: AEDD
   PL: AEDD
411. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_matan] — tekst] 마탄
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_matan].content
   limit: do 120 znaków
   EN: Magic Bullet
   PL: Magiczny Pocisk
412. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_love_and_hate] — tekst] 사랑과 증오의 이름으로
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_love_and_hate].content
   limit: do 120 znaków
   EN: In the Name of Love and Hate
   PL: W Imię Miłości i Nienawiści
413. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_ohyeol_eupru] — tekst] 오혈읍루
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_ohyeol_eupru].content
   limit: do 120 znaków
   EN: Tears of the Tarnished Blood
   PL: Łzy Splamionej Krwi
414. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_samcheon_daesegye] — tekst] 삼천대세계
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_samcheon_daesegye].content
   limit: do 120 znaków
   EN: Great Trichiliocosm
   PL: Wielki Trichiliokosm
415. [Wydarzenia i Przepustka [limtochess_synergy_set_wuthering_heights] — tekst] 워더링하이츠
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_wuthering_heights].content
   limit: do 120 znaków
   EN: Wuthering Heights
   PL: Wichrowe Wzgórza
416. [Wydarzenia i Przepustka [limtochess_synergy_set_t_corp] — tekst] T사
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_t_corp].content
   limit: do 120 znaków
   EN: T Corp.
   PL: T Corp.
417. [Wydarzenia i Przepustka [limtochess_synergy_set_dieci] — tekst] 디에치 협회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_dieci].content
   limit: do 120 znaków
   EN: Dieci Association
   PL: Stowarzyszenie Dieci
418. [Wydarzenia i Przepustka [limtochess_synergy_set_pequod] — tekst] 피쿼드호
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_pequod].content
   limit: do 120 znaków
   EN: The Pequod
   PL: Pequod
419. [Wydarzenia i Przepustka [limtochess_synergy_set_seven] — tekst] 세븐 협회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_seven].content
   limit: do 120 znaków
   EN: Seven Association
   PL: Stowarzyszenie Seven
420. [Wydarzenia i Przepustka [limtochess_synergy_set_cinq] — tekst] 섕크 협회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_cinq].content
   limit: do 120 znaków
   EN: Cinq Association
   PL: Stowarzyszenie Cinq
421. [Wydarzenia i Przepustka [limtochess_synergy_set_zwei] — tekst] 츠바이 협회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_zwei].content
   limit: do 120 znaków
   EN: Zwei Association
   PL: Stowarzyszenie Zwei
422. [Wydarzenia i Przepustka [limtochess_synergy_set_liu] — tekst] 리우 협회
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_liu].content
   limit: do 120 znaków
   EN: Liu Association
   PL: Stowarzyszenie Liu
423. [Wydarzenia i Przepustka [limtochess_synergy_set_w_corp] — tekst] W사
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_w_corp].content
   limit: do 120 znaków
   EN: W Corp.
   PL: W Corp.
424. [Wydarzenia i Przepustka [limtochess_synergy_set_ego_equipment] — tekst] E.G.O 장비
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_ego_equipment].content
   limit: do 120 znaków
   EN: E.G.O Gear
   PL: Sprzęt E.G.O
425. [Wydarzenia i Przepustka [limtochess_synergy_set_fixer] — tekst] 해결사
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_fixer].content
   limit: do 120 znaków
   EN: Fixers
   PL: Fikserzy
426. [Wydarzenia i Przepustka [limtochess_synergy_set_backstreet_cook] — tekst] 료.고.파
   źródło: LimtochessUI.json :: dataList[id=limtochess_synergy_set_backstreet_cook].content
   limit: do 120 znaków
   EN: R.B.
   PL: R.P.M.
427. [Wydarzenia i Przepustka [limtochess_sync_change] — tekst] 동기화 {0}단계 → 동기화 {1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_change].content
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Wydarzenia i Przepustka [limtochess_event_cost_up_sinner] — tekst] {0} · {1} · 코스트 {2} → {3}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_cost_up_sinner].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: {0} · {1} · ({2} Cost) → {3}
   PL: {0} · {1} · Koszt {2} → {3}
429. [Wydarzenia i Przepustka [limtochess_event_swap_one_sinner] — tekst] {0} · {1} · 코스트 {2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_swap_one_sinner].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} · {1} · ({2} Cost)
   PL: {0} · {1} · Koszt {2}
430. [Wydarzenia i Przepustka [limtochess_sync_target] — tekst] {0} · {1} 동기화 {2}단계 → 동기화 {3}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_target].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}
   EN: - Uptie {0} ID {1} from Uptie {2} to Uptie {3}
   PL: {0} · {1} Synchronizacja {2} → Synchronizacja {3}
431. [Wydarzenia i Przepustka [limtochess_sync_level] — tekst] 동기화 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_level].content
   (powtórzenie elementu 29 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Wydarzenia i Przepustka [limtochess_sync_of_cap] — tekst] 동기화 {0}/{1}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_of_cap].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0}/{1}
   PL: Synchronizacja {0}/{1}
433. [Wydarzenia i Przepustka [limtochess_sync_keep] — tekst] · 동기화 {0}단계 유지
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_keep].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: · Remains Uptie {0}
   PL: · Synchronizacja {0} bez zmian
434. [Wydarzenia i Przepustka [limtochess_sync_after_replace] — tekst] 교체 후 동기화 {0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_after_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie {0} after swap
   PL: Po wymianie Synchronizacja {0}
435. [Wydarzenia i Przepustka [limtochess_sync_cap_unowned] — tekst] (미보유 동기화 3단계 상한)
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_cap_unowned].content
   limit: do 120 znaków
   EN: (Not Owned. Uptie Capped at Tier 3)
   PL: (Nieposiadana: Synchronizacja maks. 3)
436. [Wydarzenia i Przepustka [limtochess_sync_cap_unowned_sub] — tekst] · 미보유 동기화 3단계 상한
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_cap_unowned_sub].content
   limit: do 120 znaków
   EN: · Not Owned. Uptie Capped at Tier 3
   PL: · Nieposiadana: Synchronizacja maks. 3
437. [Wydarzenia i Przepustka [limtochess_pack_outcome_replace] — tekst] 동기화 {0}단계 → 동기화 {1}단계 교체
   źródło: LimtochessUI.json :: dataList[id=limtochess_pack_outcome_replace].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Replace: Uptie {0} → Uptie {1}
   PL: Wymiana: Synchronizacja {0} → Synchronizacja {1}
438. [Wydarzenia i Przepustka [limtochess_cost_label] — tekst] 코스트 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_cost_label].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Cost
   PL: Koszt {0}
439. [Wydarzenia i Przepustka [limtochess_affiliation_tail] — tekst] · 소속 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_affiliation_tail].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: · {0} Faction
   PL: · Przynależność: {0}
440. [Wydarzenia i Przepustka [limtochess_reward_no_target_sync] — tekst] 대상 없음 (※ 모두 동기화 {0}단계 이상이거나 편성에 없는 경우)
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_no_target_sync].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: No eligible units (※ Either all units are at Uptie {0}+, or are not in your current Team)
   PL: Brak kwalifikujących się jednostek (※ wszystkie mają Synchronizację {0} lub wyższą albo są poza składem)
441. [Wydarzenia i Przepustka [limtochess_reward_face_sync_plus] — tekst] 동기화 +{0}단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_face_sync_plus].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie +{0}
   PL: Synchronizacja +{0}
442. [Wydarzenia i Przepustka [limtochess_reward_why_capped] — tekst] 동기화 {0}단계 · 상한
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_why_capped].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie +{0} · Capped
   PL: Synchronizacja +{0} · limit
443. [Wydarzenia i Przepustka [limtochess_reward_why_generic_cost] — tekst] 동기화 {0}단계 · 범용 {1}개 필요
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_why_generic_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} · Need {1} Universal Sliver
   PL: Synchronizacja {0} · potrzeba {1} Okruchów Uniwersalnych
444. [Wydarzenia i Przepustka [limtochess_reward_why_generic_max] — tekst] 동기화 {0}단계 · 범용은 동기화 {1}단계까지
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_why_generic_max].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie {0} · Universal Sliver can upgrade to Uptie {1}
   PL: Synchronizacja {0} · Okruchy Uniwersalne do Synchronizacji {1}
445. [Wydarzenia i Przepustka [limtochess_reward_why_not_target] — tekst] 동기화 {0}단계 · 대상 아님
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_why_not_target].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie {0} · Ineligible
   PL: Synchronizacja {0} · niekwalifikuje się
446. [Wydarzenia i Przepustka [limtochess_reward_title_sync_up_small] — tekst] 보유 인격 1명 동기화 ({0}단계까지)
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_title_sync_up_small].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Uptie 1 Identity in Team (Up to Uptie {0})
   PL: Synchronizacja 1 posiadanej Tożsamości (do Synchronizacji {0})
447. [Wydarzenia i Przepustka [limtochess_reward_face_sync_personality] — tekst] 동기화 {0}단계 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_face_sync_personality].content
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
448. [Wydarzenia i Przepustka [limtochess_reward_title_sync_under] — tekst] 동기화 {0}단계 미만 인격 1명
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_title_sync_under].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: 1 Identity under Uptie {0}
   PL: 1 Tożsamość poniżej Synchronizacji {0}
449. [Wydarzenia i Przepustka [limtochess_reward_label_sync_up_small] — tekst] 보유 인격 1명 동기화 +{0}단계 ({1}단계까지)
   źródło: LimtochessUI.json :: dataList[id=limtochess_reward_label_sync_up_small].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Uptie +{0} for 1 Identity in Team (up to Uptie {1})
   PL: Synchronizacja +{0} dla 1 posiadanej Tożsamości (do Synchronizacji {1})
450. [Wydarzenia i Przepustka [limtochess_sync_cap_unowned_short] — tekst] 미보유(동기화 {0}단계 상한)
   źródło: LimtochessUI.json :: dataList[id=limtochess_sync_cap_unowned_short].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Not Owned (Uptie Capped at Tier {0})
   PL: Nieposiadana (Synchronizacja maks. {0})
451. [Wydarzenia i Przepustka [limtochess_completion_stage2] — tekst] 2단계 : 전원 동기화 4단계 + 인격마다 4단계 E.G.O {0}개 ({1}/{2}명)
   źródło: LimtochessUI.json :: dataList[id=limtochess_completion_stage2].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Stage 2: All IDs at Uptie 4 + {0} Tier 4 E.G.O per ID ({1}/{2})
   PL: Etap 2: wszyscy na Synchronizacji 4 + {0} E.G.O Tier 4 na Tożsamość ({1}/{2})
452. [Wydarzenia i Przepustka [limtochess_completion_record] — tekst] 기록 달성 — {0} 인격 {1}명 동기화 4단계
   źródło: LimtochessUI.json :: dataList[id=limtochess_completion_record].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Record achieved: {1} {0} ID(s) at Uptie 4
   PL: Osiągnięto zapis — {1} Tożsamości {0} na Synchronizacji 4
453. [Wydarzenia i Przepustka [limtochess_roominfo_name_battle] — tekst] {0} 전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_name_battle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Encounter
   PL: Walka: {0}
454. [Wydarzenia i Przepustka [limtochess_roominfo_name_room] — tekst] {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_name_room].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}
   PL: {0}
455. [Wydarzenia i Przepustka [limtochess_roominfo_name_hidden] — tekst] 밝혀지지 않은 방
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_name_hidden].content
   limit: do 120 znaków
   EN: Room in Gloom
   PL: Pokój w Mroku
456. [Wydarzenia i Przepustka [limtochess_roominfo_name_visited] — tekst] {0} · 방문한 방
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_name_visited].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} · Already Visited
   PL: {0} · Pokój odwiedzony
457. [Wydarzenia i Przepustka [limtochess_roominfo_name_current] — tekst] {0} · 현재 위치
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_name_current].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} · Current Location
   PL: {0} · Bieżąca pozycja
458. [Wydarzenia i Przepustka [limtochess_roominfo_pack_count] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_pack_count].content
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
459. [Wydarzenia i Przepustka [limtochess_packtip_cost_low] — tekst] COST 0~1
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_cost_low].content
   limit: do 120 znaków
   EN: COST 0~1
   PL: COST 0~1
460. [Wydarzenia i Przepustka [limtochess_packtip_chance_line] — tekst] {0}  {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_chance_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0}  {1}
   PL: {0}  {1}
461. [Wydarzenia i Przepustka [limtochess_packtip_percent] — tekst] {0}%
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_percent].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}%
   PL: {0}%
462. [Wydarzenia i Przepustka [limtochess_packtip_percent_under_min] — tekst] 0.01% 미만
   źródło: LimtochessUI.json :: dataList[id=limtochess_packtip_percent_under_min].content
   limit: do 120 znaków
   EN: <0.01%
   PL: poniżej 0.01%
463. [Wydarzenia i Przepustka [limtochess_part_focus_header] — tekst] WARNING
   źródło: LimtochessUI.json :: dataList[id=limtochess_part_focus_header].content
   limit: do 120 znaków
   EN: WARNING
   PL: WARNING
464. [Wydarzenia i Przepustka [limtochess_part_focus_6011_pole] — tekst] 전봇대 우선 공격
   źródło: LimtochessUI.json :: dataList[id=limtochess_part_focus_6011_pole].content
   limit: do 120 znaków
   EN: Prioritize Telepole
   PL: Atakuj najpierw Telepole
465. [Wydarzenia i Przepustka [limtochess_entrance_pass_locked_title] — tekst] 미개방
   źródło: LimtochessUI.json :: dataList[id=limtochess_entrance_pass_locked_title].content
   limit: do 120 znaków
   EN: Locked
   PL: Zablokowane
466. [Wydarzenia i Przepustka [limtochess_final_title_cleared] — tekst] 구축 성공
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_title_cleared].content
   limit: do 120 znaków
   EN: SCHEMA SUCCESS
   PL: KONSTRUKCJA UKOŃCZONA
467. [Wydarzenia i Przepustka [limtochess_final_title_defeated] — tekst] 구축 실패
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_title_defeated].content
   (powtórzenie elementu 133 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Wydarzenia i Przepustka [limtochess_final_title_abandoned] — tekst] 구축 포기
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_title_abandoned].content
   limit: do 120 znaków
   EN: Craft Forfeited
   PL: Konstrukcja porzucona
469. [Wydarzenia i Przepustka [limtochess_final_mode_auto] — tekst] 자동 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_mode_auto].content
   limit: do 120 znaków
   EN: Randomized Team
   PL: Skład losowy
470. [Wydarzenia i Przepustka [limtochess_final_mode_manual] — tekst] 수동 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_mode_manual].content
   (powtórzenie elementu 56 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Wydarzenia i Przepustka [limtochess_final_summary_line] — tekst] {0} · 도상 진행도 {1}/{2} · 편성 인격 {3}명 · 인격 레벨 {4}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_summary_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}
   EN: {0} · Schema Progress {1}/{2} · {3} Team Identities · Identity Level {4}
   PL: {0} · Postęp Schematu {1}/{2} · Tożsamości w składzie: {3} · Poziom Tożsamości {4}
472. [Wydarzenia i Przepustka [limtochess_final_auto_bonus] — tekst] ※ 자동 편성 보너스 : 도상구축 패스 경험치 +40%
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_auto_bonus].content
   limit: do 120 znaków
   EN: ※ Randomized Team Bonus: Schemacraft Pass EXP +40%
   PL: ※ Bonus Składu Losowego: PD Przepustki Konstrukcji Schematów +40%
473. [Wydarzenia i Przepustka [limtochess_final_measure_line] — tekst] 총 소요 시간 : {0} · 주사위 굴림 횟수 : {1}회
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_measure_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Total Time Taken: {0} · Total Reroll Attempts: x{1}
   PL: Łączny czas: {0} · Liczba rzutów kością: {1}
474. [Wydarzenia i Przepustka [limtochess_duration_hours] — tekst] {0}시간 {1}분
   źródło: LimtochessUI.json :: dataList[id=limtochess_duration_hours].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} hrs, {1} mins
   PL: {0} godz. {1} min
475. [Wydarzenia i Przepustka [limtochess_duration_minutes] — tekst] {0}분 {1}초
   źródło: LimtochessUI.json :: dataList[id=limtochess_duration_minutes].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} mins, {1} seconds
   PL: {0} min {1} s
476. [Wydarzenia i Przepustka [limtochess_final_defeat_where] — tekst] 패배 스테이지 - {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_defeat_where].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Failed Stage - {0}
   PL: Nieudany Etap — {0}
477. [Wydarzenia i Przepustka [limtochess_final_completion_none] — tekst] 최종 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_completion_none].content
   limit: do 120 znaków
   EN: Final Team
   PL: Skład końcowy
478. [Wydarzenia i Przepustka [limtochess_final_not_in_roster] — tekst] 편성 제외
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_not_in_roster].content
   limit: do 120 znaków
   EN: Removed from Team
   PL: Usunięty ze składu
479. [Wydarzenia i Przepustka [limtochess_final_damage_head] — tekst] 피해 기록 [일반 전투 {0}회, 정예 전투 {1}회, 보스 전투 {2}회 합계]
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_damage_head].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Damage Record: sum of [ {0} Regular Encounter(s), {1} Elite Encounter(s), {2} Boss Encounter(s) ]
   PL: Statystyki obrażeń [suma: {0}× Zwykłe Starcie, {1}× Walka Elitarna, {2}× Walka z Bossem]
480. [Wydarzenia i Przepustka [limtochess_final_damage_row] — tekst] 가한 피해 {0}({1}%) · 받은 피해 {2} · 처치 {3} · 출전 {4}회
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_damage_row].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}
   EN: Dmg Dealt {0} ({1}%) · Dmg Taken {2} · Kills {3} · Deployed {0} times
   PL: Zadane obrażenia {0} ({1}%) · Otrzymane obrażenia {2} · Pokonani {3} · Występy {4}
481. [Wydarzenia i Przepustka [limtochess_final_damage_row_deaths] — tekst] · 사망 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_damage_row_deaths].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: · Defeated {0}
   PL: · Polegli {0}
482. [Wydarzenia i Przepustka [limtochess_final_damage_total] — tekst] 합계 — 가한 피해 {0} · 받은 피해 {1} · 처치 {2}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_damage_total].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: Sum - Dmg Dealt {0} · Dmg Taken {1} · Kills {2}
   PL: Suma — zadane obrażenia {0} · otrzymane obrażenia {1} · pokonani {2}
483. [Wydarzenia i Przepustka [limtochess_final_battle_log_head] — tekst] 전투 기록
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_battle_log_head].content
   limit: do 120 znaków
   EN: Battle Stats
   PL: Statystyki walki
484. [Wydarzenia i Przepustka [limtochess_final_battle_log_line] — tekst] {0} — {1} ({2}턴 진행) · 소요 시간 : {3} · 사망한 인격 수 : {4}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_battle_log_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}, {3}, {4}
   EN: {0} — {1} ({2} Turns elapsed) · Elapsed Time: {3} · Defeated Allies: {4}
   PL: {0} — {1} ({2} tury) · czas: {3} · liczba poległych Tożsamości: {4}
485. [Wydarzenia i Przepustka [limtochess_battle_result_win] — tekst] 승리
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_result_win].content
   limit: do 120 znaków
   EN: Victory
   PL: Zwycięstwo
486. [Wydarzenia i Przepustka [limtochess_room_title] — tekst] 제 {0}도상 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Schema {0} {1}
   PL: Schemat {0} {1}
487. [Wydarzenia i Przepustka [limtochess_room_label_final_boss] — tekst] 최종 보스 전투
   źródło: LimtochessUI.json :: dataList[id=limtochess_room_label_final_boss].content
   limit: do 120 znaków
   EN: Final Boss Encounter
   PL: Walka z Finałowym Bossem
488. [Wydarzenia i Przepustka [limtochess_report_subline] — tekst] {0} · {1}턴
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_subline].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} · {1} Turn(s)
   PL: {0} · {1} tury
489. [Wydarzenia i Przepustka [limtochess_report_round] — tekst] {0}턴
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_round].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Turn(s)
   PL: {0} tury
490. [Wydarzenia i Przepustka [limtochess_report_retry_left] — tekst] 재전투 (남은 횟수 {0})
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_retry_left].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Retry Battle (Remaining: {0})
   PL: Ponów walkę (pozostało: {0})
491. [Wydarzenia i Przepustka [limtochess_report_continue] — tekst] 계속
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_continue].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuuj
492. [Wydarzenia i Przepustka [limtochess_event_hardship_stacked] — tekst] 받은 고난 {0}개 — {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_hardship_stacked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Obstacles Received {0} — 1
   PL: Otrzymane Próby: {0} — {1}
493. [Wydarzenia i Przepustka [limtochess_event_boss_current] — tekst] 현재 최종 보스 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_boss_current].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Current Final Boss: {0}
   PL: Obecny Boss Finałowy: {0}
494. [Wydarzenia i Przepustka [limtochess_event_pick_guide] — tekst] 추가되는 고난은 이후 모든 전투의 적에게 누적되어 적용됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_pick_guide].content
   limit: do 120 znaków
   EN: Added Obstacles will stack and apply to enemies in all subsequent battles.
   PL: Dodane Próby akumulują się na wrogach we wszystkich kolejnych walkach.
495. [Wydarzenia i Przepustka [limtochess_event_card_selected] — tekst] 선택됨
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_card_selected].content
   limit: do 120 znaków
   EN: Selected
   PL: Wybrano
496. [Wydarzenia i Przepustka [limtochess_event_card_select] — tekst] 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_card_select].content
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Wydarzenia i Przepustka [limtochess_event_choice_confirm] — tekst] 확인
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_choice_confirm].content
   (powtórzenie elementu 32 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
498. [Wydarzenia i Przepustka [limtochess_event_keyword_picked] — tekst] 선택한 키워드 : {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_keyword_picked].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Selected Keyword: {0}
   PL: Wybrane Słowo Kluczowe: {0}
499. [Wydarzenia i Przepustka [limtochess_event_roster_note] — tekst] 편성 {0}/{1}명 — 영입하면 편성된 인격 1명과 교체됩니다
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_roster_note].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Team: {0}/{1} — Recruiting will replace 1 Identity in the  team
   PL: Skład {0}/{1} — werbunek zastąpi 1 Tożsamość ze składu
500. [Wydarzenia i Przepustka [limtochess_event_none] — tekst] 진행할 수 있는 이벤트가 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_none].content
   limit: do 120 znaków
   EN: No available Events.
   PL: Brak dostępnych Wydarzeń.
501. [Wydarzenia i Przepustka [limtochess_event_back_to_map] — tekst] 맵으로 돌아가기
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_back_to_map].content
   limit: do 120 znaków
   EN: Return to Schema Map
   PL: Wróć do mapy Schematu
502. [Wydarzenia i Przepustka [limtochess_event_empty_slot] — tekst] 비어 있는 편성
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_empty_slot].content
   limit: do 120 znaków
   EN: Empty Team Slot
   PL: Puste miejsce w składzie
503. [Wydarzenia i Przepustka [limtochess_event_unknown_personality] — tekst] 알 수 없는 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_unknown_personality].content
   limit: do 120 znaków
   EN: Unknown Identity
   PL: Nieznana Tożsamość
504. [Wydarzenia i Przepustka [limtochess_event_unknown_ego] — tekst] 알 수 없는 E.G.O
   źródło: LimtochessUI.json :: dataList[id=limtochess_event_unknown_ego].content
   limit: do 120 znaków
   EN: Unknown E.G.O
   PL: Nieznane E.G.O
505. [Wydarzenia i Przepustka [limtochess_notice_battle_quit] — tekst] 전투를 중단했습니다. 전투 진입 직전 상태로 되돌아갑니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_battle_quit].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Battle canceled.\nReturning to the state just before the battle.
   PL: Walka przerwana.\nPowrót do stanu sprzed wejścia do walki.
506. [Wydarzenia i Przepustka [limtochess_notice_server_wait] — tekst] 서버 정보를 불러오는 중입니다. 잠시 후 다시 시도해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_server_wait].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Loading server data.\nPlease try again in a moment.
   PL: Wczytywanie danych serwera.\nSpróbuj ponownie za chwilę.
507. [Wydarzenia i Przepustka [limtochess_notice_deck_unavailable] — tekst] 지금은 사용할 수 없는 편성입니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_deck_unavailable].content
   limit: do 120 znaków
   EN: This formation is currently unavailable.
   PL: Ten skład jest obecnie niedostępny.
508. [Wydarzenia i Przepustka [limtochess_notice_rolls_used_up] — tekst] 편성 새로고침 횟수를 전부 소모했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_rolls_used_up].content
   limit: do 120 znaków
   EN: No more Team Reshuffles.
   PL: Wykorzystano wszystkie odświeżenia składu.
509. [Wydarzenia i Przepustka [limtochess_notice_auto_rolls_used_up] — tekst] 자동 편성 새로고침 횟수를 전부 소모했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_auto_rolls_used_up].content
   limit: do 120 znaków
   EN: No more Randomized Team Reshuffles.
   PL: Wykorzystano wszystkie odświeżenia Składu Losowego.
510. [Wydarzenia i Przepustka [limtochess_notice_pick_one] — tekst] 인격을 1명 이상 선택해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_pick_one].content
   limit: do 120 znaków
   EN: Select at least 1 Identity.
   PL: Wybierz co najmniej 1 Tożsamość.
511. [Wydarzenia i Przepustka [limtochess_notice_roll_first] — tekst] 먼저 편성 새로고침을 진행해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_roll_first].content
   limit: do 120 znaków
   EN: Please Reshuffle first.
   PL: Najpierw odśwież skład.
512. [Wydarzenia i Przepustka [limtochess_notice_cost_over] — tekst] 코스트가 부족합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_cost_over].content
   limit: do 120 znaków
   EN: Insufficient Cost.
   PL: Za mało Kosztu.
513. [Wydarzenia i Przepustka [limtochess_notice_max_picks] — tekst] 최대 {0}명까지 편성할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_max_picks].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You can add up to {0} Identities to the team.
   PL: Do składu można dodać maks. {0} Tożsamości.
514. [Wydarzenia i Przepustka [limtochess_notice_run_in_progress] — tekst] 진행 중인 데이터가 확인되었습니다. 이어하기로 진행해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_run_in_progress].content
   limit: do 120 znaków
   EN: A run is already in progress. Select "Continue" to resume.
   PL: Wykryto zapis rozgrywki. Kontynuuj przez „Kontynuuj”.
515. [Wydarzenia i Przepustka [limtochess_notice_already_picked] — tekst] 이미 선택한 대상입니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_already_picked].content
   limit: do 120 znaków
   EN: Already selected.
   PL: Już wybrano.
516. [Wydarzenia i Przepustka [limtochess_notice_no_target] — tekst] 선택할 수 있는 대상이 없습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_no_target].content
   limit: do 120 znaków
   EN: No eligible targets.
   PL: Brak dostępnych celów.
517. [Wydarzenia i Przepustka [limtochess_confirm_ego_swap_desc] — tekst] {0}의 E.G.O를 교체하시겠습니까?
   źródło: LimtochessUI.json :: dataList[id=limtochess_confirm_ego_swap_desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Replace {0}'s E.G.O?
   PL: Wymienić E.G.O jednostki {0}?
518. [Wydarzenia i Przepustka [limtochess_notice_reroll_charged] — tekst] 새로고침 기회가 {0}회 충전되었습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_reroll_charged].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Reshuffle(s) charged.
   PL: Naładowano {0} odświeżeń.
519. [Wydarzenia i Przepustka [limtochess_notice_reroll_short] — tekst] 새로고침 기회가 부족합니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_reroll_short].content
   limit: do 120 znaków
   EN: Out of Reshuffles.
   PL: Za mało odświeżeń.
520. [Wydarzenia i Przepustka [limtochess_notice_identity_joined] — tekst] 인격을 편성했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_identity_joined].content
   limit: do 120 znaków
   EN: Identity recruited.
   PL: Tożsamość zrekrutowana.
521. [Wydarzenia i Przepustka [limtochess_notice_identity_replaced] — tekst] 인격을 교체했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_identity_replaced].content
   limit: do 120 znaków
   EN: Identity replaced.
   PL: Tożsamość wymieniona.
522. [Wydarzenia i Przepustka [limtochess_notice_sync_up] — tekst] {0} 인격의 동기화 단계가 {1}단계에서 {2}단계로 상승했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_sync_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: {0} Identity Uptied: Uptie {1} → {2}
   PL: Tożsamość {0}: Synchronizacja {1} → {2}
523. [Wydarzenia i Przepustka [limtochess_notice_level_catch_up] — tekst] 인격 레벨이 {0} → {1} 상승했습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_level_catch_up].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Identity Lvl. Gained: {0} → {1}
   PL: Poziom Tożsamości: {0} → {1}
524. [Wydarzenia i Przepustka [limtochess_formation_cost] — tekst] {0} Cost
   źródło: LimtochessUI.json :: dataList[id=limtochess_formation_cost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} Cost
   PL: {0} Cost
525. [Wydarzenia i Przepustka [limtochess_notice_server_error] — tekst] 서버 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_server_error].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A server error has occurred.\nPlease try again in a moment.
   PL: Błąd serwera.\nSpróbuj ponownie za chwilę.
526. [Wydarzenia i Przepustka [limtochess_notice_battle_enter_failed] — tekst] 전투에 진입하지 못했습니다. 잠시 후 다시 시도해 주세요.
   źródło: LimtochessUI.json :: dataList[id=limtochess_notice_battle_enter_failed].content
   limit: do 120 znaków
   EN: Unable to enter battle. Please try again in a moment.
   PL: Nie udało się wejść do walki. Spróbuj ponownie za chwilę.
527. [Wydarzenia i Przepustka [limtochess_roster_replace_title] — tekst] 편성 인원 초과 - 제외할 인격 {0}명을 선택하세요
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Team limit exceeded - Select {0} Identities to remove
   PL: Limit składu przekroczony — wybierz {0} Tożsamości do usunięcia
528. [Wydarzenia i Przepustka [limtochess_roster_replace_desc] — tekst] 이번 도상의 편성 상한은 {0}명이며, 영입하면 편성 인격이 총 {1}명이 됩니다.\n제외된 인격은 장착한 E.G.O를 잃고, 동기화 단계에 따라 그 인격의 조각 일부가 보관됩니다. 다시 영입하면 보관된 조각이 적용됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_desc].content
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, \n
   EN: This Schema allows up to {0} Identities on your team. Recruiting will bring your team to {1} Identities.\nRemoved Identities lose their equipped E.G.O. Some of their Slivers are saved based on their Uptie Tier. The saved Slivers will be applied if you recruit them again.
   PL: Limit tego Schematu to {0} Tożsamości; werbunek da {1} Tożsamości w składzie.\nUsunięte Tożsamości tracą wyposażone E.G.O, a część ich Skrawków — zależnie od Stopnia Synchronizacji — zostaje zapisana. Przy ponownym werbunku zapisane Skrawki wracają.
529. [Wydarzenia i Przepustka [limtochess_roster_replace_confirm] — tekst] 제외하고 받기
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_confirm].content
   limit: do 120 znaków
   EN: Remove and Claim
   PL: Usuń i odbierz
530. [Wydarzenia i Przepustka [limtochess_roster_replace_count] — tekst] 선택 {0}/{1}명
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Selected {0}/{1}
   PL: Wybrano {0}/{1}
531. [Wydarzenia i Przepustka [limtochess_roster_replace_head] — tekst] 편성 인원 초과
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_head].content
   limit: do 120 znaków
   EN: Team Limit Exceeded
   PL: Limit składu przekroczony
532. [Wydarzenia i Przepustka [limtochess_roster_replace_sub] — tekst] 제외할 인격을 {0}명 선택하세요
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_sub].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Select {0} Identity(ies) to remove
   PL: Wybierz {0} Tożsamości do usunięcia
533. [Wydarzenia i Przepustka [limtochess_roster_replace_card_power] — tekst] 구축력 {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_card_power].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Craftpower {0}
   PL: Siła Konstrukcji {0}
534. [Wydarzenia i Przepustka [limtochess_roster_replace_card_refund] — tekst] 제외할 경우, 조각 {0}개 보관
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_card_refund].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Slivers saved if removed: {0}
   PL: Po usunięciu zapisane Skrawki: {0}
535. [Wydarzenia i Przepustka [limtochess_roster_replace_exclude] — tekst] 제외하기
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_exclude].content
   limit: do 120 znaków
   EN: Remove
   PL: Usuń
536. [Wydarzenia i Przepustka [limtochess_roster_replace_cancel] — tekst] 취소
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_cancel].content
   limit: do 120 znaków
   EN: Cancel
   PL: Anuluj
537. [Wydarzenia i Przepustka [limtochess_roster_replace_limit] — tekst] 대체는 {0}명까지 — 고른 수감자를 눌러 빼고 고르세요
   źródło: LimtochessUI.json :: dataList[id=limtochess_roster_replace_limit].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: You can replace up to {0} Identities. Tap a selected Sinner to deselect them before choosing another
   PL: Wymiana maks. {0} — dotknij wybranego Grzesznika, aby go zdjąć, i wybierz innego
538. [Wydarzenia i Przepustka [limtochess_formation_all_join] — tekst] 모든 인격이 전투에 참전해야 진행할 수 있습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_formation_all_join].content
   limit: do 120 znaków
   EN: All Identities must participate.
   PL: Wszystkie Tożsamości muszą wziąć udział w walce.
539. [Wydarzenia i Przepustka [limtochess_weekly_reset_end_title] — tekst] 구축 종료
   źródło: LimtochessUI.json :: dataList[id=limtochess_weekly_reset_end_title].content
   limit: do 120 znaków
   EN: Run Ended
   PL: Konstrukcja zakończona
540. [Wydarzenia i Przepustka [limtochess_weekly_reset_end_desc] — tekst] 주간 초기화로 진행 중이던 구축이 종료되었습니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_weekly_reset_end_desc].content
   limit: do 120 znaków
   EN: The weekly reset has ended your current Schemacraft run.
   PL: Reset tygodniowy zakończył trwającą Konstrukcję.
541. [Wydarzenia i Przepustka [limtochess_final_claim_reward] — tekst] 보상받기
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_claim_reward].content
   limit: do 120 znaków
   EN: Claim Rewards
   PL: Odbierz nagrody
542. [Wydarzenia i Przepustka [limtochess_final_exit] — tekst] 나가기
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_exit].content
   limit: do 120 znaków
   EN: Exit
   PL: Wyjdź
543. [Wydarzenia i Przepustka [limtochess_report_duel_win] — tekst] 아군 합 승리 수
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_duel_win].content
   limit: do 120 znaków
   EN: Ally Clash Wins
   PL: Liczba wygranych starć sojuszników
544. [Wydarzenia i Przepustka [limtochess_report_mp_avg] — tekst] 아군 정신력 평균
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_mp_avg].content
   limit: do 120 znaków
   EN: SP Average (allies)
   PL: Średnie PP (sojuszników)
545. [Wydarzenia i Przepustka [limtochess_report_table_title] — tekst] 전투 기록
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_table_title].content
   (powtórzenie elementu 483 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Wydarzenia i Przepustka [limtochess_report_dealt] — tekst] 가한 피해
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_dealt].content
   limit: do 120 znaków
   EN: Dmg Dealt
   PL: Zadane obrażenia
547. [Wydarzenia i Przepustka [limtochess_report_taken] — tekst] 받은 피해
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_taken].content
   limit: do 120 znaków
   EN: Dmg Taken
   PL: Otrzymane obrażenia
548. [Wydarzenia i Przepustka [limtochess_report_ego_damage] — tekst] E.G.O 피해
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_ego_damage].content
   limit: do 120 znaków
   EN: E.G.O Dmg dealt
   PL: Obrażenia E.G.O
549. [Wydarzenia i Przepustka [limtochess_report_kill] — tekst] 처치
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_kill].content
   limit: do 120 znaków
   EN: Kills
   PL: Pokonani
550. [Wydarzenia i Przepustka [limtochess_report_duel] — tekst] 합 승리
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_duel].content
   limit: do 120 znaków
   EN: Clashes Won
   PL: Wygrane starcia
551. [Wydarzenia i Przepustka [limtochess_report_dealt_count] — tekst] 가한 피해(횟수)
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_dealt_count].content
   limit: do 120 znaków
   EN: Dmg Dealt (Hits)
   PL: Zadane obrażenia (ciosy)
552. [Wydarzenia i Przepustka [limtochess_report_taken_count] — tekst] 받은 피해(횟수)
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_taken_count].content
   limit: do 120 znaków
   EN: Dmg Taken (Hits)
   PL: Otrzymane obrażenia (ciosy)
553. [Wydarzenia i Przepustka [limtochess_report_damage_count] — tekst] {0} ({1})
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_damage_count].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} ({1})
   PL: {0} ({1})
554. [Wydarzenia i Przepustka [limtochess_report_duel_rate] — tekst] 합 승률
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_duel_rate].content
   limit: do 120 znaków
   EN: Clashes Won (%)
   PL: Wygrane starcia (%)
555. [Wydarzenia i Przepustka [limtochess_report_one_sided] — tekst] 일방 공격 비율
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_one_sided].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unopp.\nAtk. Rate
   PL: Odsetek ataków bez oporu
556. [Wydarzenia i Przepustka [limtochess_report_weak_resist] — tekst] <color=#FF6B5E>약점</color>·<color=#6FB2FF>내성</color> 적중
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_weak_resist].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#FF6B5E>, </color>, <color=#6FB2FF>, \n
   EN: <color=#FF6B5E>Weak</color>/<color=#6FB2FF>Resist.</color>\nExploited
   PL: Trafione <color=#FF6B5E>Słabe</color>·<color=#6FB2FF>Odporności</color>
557. [Wydarzenia i Przepustka [limtochess_report_dot] — tekst] 지속 피해
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_dot].content
   limit: do 120 znaków
   EN: Damage over time
   PL: Obrażenia w czasie
558. [Wydarzenia i Przepustka [limtochess_report_tab_attack] — tekst] 공격
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_tab_attack].content
   limit: do 120 znaków
   EN: Inflicted
   PL: Zadane
559. [Wydarzenia i Przepustka [limtochess_report_tab_hit] — tekst] 피격
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_tab_hit].content
   limit: do 120 znaków
   EN: Taken
   PL: Otrzymane
560. [Wydarzenia i Przepustka [limtochess_report_total_ally] — tekst] 아군 전체
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_total_ally].content
   limit: do 120 znaków
   EN: Ally Total
   PL: Sojusznicy łącznie
561. [Wydarzenia i Przepustka [limtochess_report_total_enemy] — tekst] 적 전체
   źródło: LimtochessUI.json :: dataList[id=limtochess_report_total_enemy].content
   limit: do 120 znaków
   EN: Enemy Total
   PL: Wrogowie łącznie
562. [Wydarzenia i Przepustka [limtochess_sweeper_banner_start_time] — tekst] 새벽 3시 13분
   źródło: LimtochessUI.json :: dataList[id=limtochess_sweeper_banner_start_time].content
   limit: do 120 znaków
   EN: 3:13 AM
   PL: 3:13 w nocy
563. [Wydarzenia i Przepustka [limtochess_sweeper_banner_elapsed] — tekst] {0}분 경과
   źródło: LimtochessUI.json :: dataList[id=limtochess_sweeper_banner_elapsed].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0} min elapsed
   PL: Minęło {0} min
564. [Wydarzenia i Przepustka [limtochess_sweeper_banner_night_start] — tekst] 뒷골목의 밤이 시작됩니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_sweeper_banner_night_start].content
   limit: do 120 znaków
   EN: The Night in the Backstreets begins.
   PL: Noc w Zaułkach się zaczyna.
565. [Wydarzenia i Przepustka [limtochess_sweeper_banner_rush] — tekst] 더 많은 청소부가 몰려옵니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_sweeper_banner_rush].content
   limit: do 120 znaków
   EN: More Sweepers are approaching.
   PL: Nadciągają kolejni Sprzątacze.
566. [Wydarzenia i Przepustka [limtochess_sweeper_banner_night_end] — tekst] 뒷골목의 밤이 끝나갑니다.
   źródło: LimtochessUI.json :: dataList[id=limtochess_sweeper_banner_night_end].content
   limit: do 120 znaków
   EN: The Night in the Backstreets is coming to an end.
   PL: Noc w Zaułkach dobiega końca.
567. [Wydarzenia i Przepustka [limtochess_battle_hardship_label] — tekst] 고난
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_hardship_label].content
   limit: do 120 znaków
   EN: Obstacle
   PL: Próba
568. [Wydarzenia i Przepustka [limtochess_final_result_title] — tekst] 최종 전투 결과
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_result_title].content
   limit: do 120 znaków
   EN: Final Battle Results
   PL: Podsumowanie wyprawy
569. [Wydarzenia i Przepustka [limtochess_final_pass_exp] — tekst] 도상구축 패스 경험치 +{0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_pass_exp].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Schemacraft Pass EXP +{0}
   PL: PD Przepustki Konstrukcji Schematów +{0}
570. [Wydarzenia i Przepustka [limtochess_final_segment_progress] — tekst] 도상 진행도
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_segment_progress].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Schema\nProgress
   PL: Postęp Schematu
571. [Wydarzenia i Przepustka [limtochess_final_battle_progress] — tekst] 전투 진행 횟수
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_battle_progress].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Encounters\nFought
   PL: Liczba stoczonych walk
572. [Wydarzenia i Przepustka [limtochess_final_participants] — tekst] 참여 인격
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_participants].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Participating\nIdentities
   PL: Użyte Tożsamości
573. [Wydarzenia i Przepustka [limtochess_final_identity_level] — tekst] 인격 레벨
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_identity_level].content
   limit: do 120 znaków
   EN: Identity Lvl.
   PL: Poziom Tożsamości
574. [Wydarzenia i Przepustka [limtochess_final_level_value] — tekst] LV {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_level_value].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: LV {0}
   PL: LV {0}
575. [Wydarzenia i Przepustka [limtochess_final_damage_title] — tekst] 피해 기록
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_damage_title].content
   limit: do 120 znaków
   EN: Damage Record
   PL: Statystyki obrażeń
576. [Wydarzenia i Przepustka [limtochess_final_battle_detail_bracket] — tekst] [ 일반 전투 {0}회, 정예 전투 {1}회, 보스 전투 {2}회 ]
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_battle_detail_bracket].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}, {2}
   EN: [ {0} Regular Encounter(s), {1} Elite Encounter(s), {2} Boss Encounter(s) ]
   PL: [ {0}× Zwykłe Starcie, {1}× Walka Elitarna, {2}× Walka z Bossem ]
577. [Wydarzenia i Przepustka [limtochess_final_clash_value] — tekst] {0}/{1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_clash_value].content
   (powtórzenie elementu 16 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Wydarzenia i Przepustka [limtochess_final_reward_title] — tekst] 보상 기록
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_reward_title].content
   limit: do 120 znaków
   EN: Reward Record
   PL: Zdobyte nagrody
579. [Wydarzenia i Przepustka [limtochess_final_pack_picked] — tekst] 선택
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_pack_picked].content
   limit: do 120 znaków
   EN: Picked
   PL: Wybierz
580. [Wydarzenia i Przepustka [limtochess_final_reroll_used] — tekst] 새로고침 기회 사용 횟수
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_reroll_used].content
   limit: do 120 znaków
   EN: Reshuffles Used
   PL: Liczba użytych odświeżeń
581. [Wydarzenia i Przepustka [limtochess_final_generic_shards] — tekst] 범용 조각 개수
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_generic_shards].content
   limit: do 120 znaków
   EN: Universal Shards
   PL: Liczba Okruchów Uniwersalnych
582. [Wydarzenia i Przepustka [limtochess_final_acquired_identity] — tekst] 획득한 인격 개수
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_acquired_identity].content
   limit: do 120 znaków
   EN: Identities Recruited
   PL: Zrekrutowane Tożsamości
583. [Wydarzenia i Przepustka [limtochess_final_acquired_ego] — tekst] 획득한 E.G.O 개수
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_acquired_ego].content
   limit: do 120 znaków
   EN: E.G.O Acquired
   PL: Zdobyte E.G.O
584. [Wydarzenia i Przepustka [limtochess_final_history_title] — tekst] 히스토리
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_history_title].content
   limit: do 120 znaków
   EN: History
   PL: Historia
585. [Wydarzenia i Przepustka [limtochess_final_history_change] — tekst] {0} → {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_history_change].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} → {1}
   PL: {0} → {1}
586. [Wydarzenia i Przepustka [limtochess_final_history_ego] — tekst] [{0}] {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_final_history_ego].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: [{0}] {1}
   PL: [{0}] {1}
587. [Wydarzenia i Przepustka [limtochess_battle_buildpower_label] — tekst] 구축력
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_buildpower_label].content
   limit: do 120 znaków
   EN: Craftpower
   PL: Siła Konstrukcji
588. [Wydarzenia i Przepustka [limtochess_battle_distortion_row] — tekst] 도상 왜곡
   źródło: LimtochessUI.json :: dataList[id=limtochess_battle_distortion_row].content
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Wydarzenia i Przepustka [limtochess_roominfo_line] — tekst] • {0}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_line].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: • {0}
   PL: • {0}
590. [Wydarzenia i Przepustka [limtochess_roominfo_effect_hardship] — tekst] {0} 또는 {1}
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_effect_hardship].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: {0} OR {1}
   PL: {0} lub {1}
591. [Wydarzenia i Przepustka [limtochess_roominfo_section_packs] — tekst] 등장 팩 목록
   źródło: LimtochessUI.json :: dataList[id=limtochess_roominfo_section_packs].content
   limit: do 120 znaków
   EN: Available Packs
   PL: Dostępne Pakiety
