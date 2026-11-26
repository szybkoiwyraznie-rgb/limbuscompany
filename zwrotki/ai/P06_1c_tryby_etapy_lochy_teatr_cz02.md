# Paczka AI P06 (Fala 1 · 1C) — Tryby gry, nazwy etapów, Lustrzane Lochy, Kolej i Teatr (UI) (część 2/6)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P06_1c_tryby_etapy_lochy_teatr_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P06_1c_tryby_etapy_lochy_teatr_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Rozdziały, etapy i zdolności Dantego: Ch8VideoEffectSettings
- plik gry: `Ch8VideoEffectSettings.json`

1. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch4] — tekst] 애잔함
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch4].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Melancholy
   PL: Melancholia
2. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch4] — tekst] 따듯함
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch4].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Warmth
   PL: Ciepło
3. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch5] — tekst] 격정
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch5].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Passion
   PL: Namiętność
4. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch5] — tekst] 모험심
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch5].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Adventure
   PL: Duch przygody
5. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch5] — tekst] 치열함
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch5].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Ferocity
   PL: Zaciętość
6. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch6] — tekst] 허망함
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch6].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Futility
   PL: Próżność
7. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch6] — tekst] 결연
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch6].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Determination
   PL: Determinacja
8. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch6] — tekst] 사랑
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch6].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Love
   PL: Miłość
9. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch7] — tekst] 가슴 벅참
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch7].texts[#0].texts[#0].text
   limit: do 120 znaków
   EN: Exhilaration
   PL: Uniesienie
10. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch7] — tekst] 비극
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch7].texts[#1].texts[#0].text
   limit: do 120 znaków
   EN: Tragedy
   PL: Tragedia
11. [Rozdziały, etapy i zdolności Dantego [Ch8_Ch7] — tekst] 설렘
   źródło: Ch8VideoEffectSettings.json :: dataList[id=Ch8_Ch7].texts[#2].texts[#0].text
   limit: do 120 znaków
   EN: Excitement
   PL: Podekscytowanie

## Rozdziały, etapy i zdolności Dantego: DanteAbility-a1c9p2
- plik gry: `DanteAbility-a1c9p2.json`

12. [Rozdziały, etapy i zdolności Dantego [10102] — opis] - 현현된 수감자는 인격을 장착하고 명령을 수행하지만 자아를 가지지 않으며 기억하지 못한다.\n- 수감자에게 인격을 장착시킬 수 있는 거리의 범위가 비약적으로 늘어난다.
   źródło: DanteAbility-a1c9p2.json :: dataList[id=10102].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Manifested Sinners can equip Identities and follow commands, but they lack independent will and retain no memory of their manifestation.\n- The distance limit between the manager and the Sinners for equipping Identities increases vastly.
   PL: - Przywołani w ten sposób Grzesznicy mogą zakładać Tożsamości i wykonywać rozkazy, lecz są pozbawieni własnej woli i nie zachowują wspomnień z manifestacji.\n- Zasięg pozwalający Kierownikowi nakładać Tożsamości na Grzeszników ulega ogromnemu zwiększeniu.
13. [Rozdziały, etapy i zdolności Dantego [10102] — opis bazowy] 모든 수감자와 불안정하지만 원격으로 지휘하고 소통할 수 있습니다.
   źródło: DanteAbility-a1c9p2.json :: dataList[id=10102].rawDesc
   limit: do 130 znaków
   EN: - Though somewhat unstable, the manager can remotely command and communicate with every Sinner.
   PL: Pozwala niestabilnie, lecz zdalnie dowodzić wszystkimi Grzesznikami i komunikować się z nimi.

## Rozdziały, etapy i zdolności Dantego: DanteAbility-a1c9p3
- plik gry: `DanteAbility-a1c9p3.json`

14. [Rozdziały, etapy i zdolności Dantego [60101] — opis] - 적용 효과\n • 기본 공격 스킬과 반격 스킬의 코인이 파괴 불가 코인으로 변경되고, 스킬 피해량 증가 및 위력 증가\n • 피격 시 흐트러짐 상태가 되지 않고, 최소 체력이 10으로 고정됨\n • 기본 스킬로 가한 피해량의 일정 수치만큼 체력 회복\n- 이미 사망하였거나 조작 불가, 행동 불가인 캐릭터는 선택할 수 없습니다.
   źródło: DanteAbility-a1c9p3.json :: dataList[id=60101].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Applied Effects:\n • Base Attack Skill Coins and Counter Skill Coins deal more Skill damage, gain Power, and are converted into Unbreakable Coins\n • When hit, does not become Staggered. Minimum HP is fixed to 10\n • Heal HP by a certain percentage of damage dealt with Base Skills\n- Units that are killed, cannot be controlled, or immobilized cannot be selected.
   PL: - Nakładane efekty:\n • Monety umiejętności ataku podstawowego oraz kontrataku zmieniają się w Monety Niezniszczalne oraz zyskują premię do Mocy i obrażeń\n • Jednostka nie wpada w Oszołomienie przy trafieniu, a jej minimalne PŻ zostają ustalone na 10\n • Leczy PŻ o część obrażeń zadanych umiejętnościami podstawowymi\n- Nie można wybrać jednostek poległych, niekontrolowalnych ani niezdolnych do działania.
15. [Rozdziały, etapy i zdolności Dantego [60101] — opis bazowy] 캐릭터 1명을 선택하여 능력치를 강화합니다.
   źródło: DanteAbility-a1c9p3.json :: dataList[id=60101].rawDesc
   limit: do 120 znaków
   EN: Select a single unit to strengthen its stats.
   PL: Wybierz 1 postać, aby wzmocnić jej zdolności bojowe.

## Rozdziały, etapy i zdolności Dantego: DanteAbility
- plik gry: `DanteAbility.json`

16. [Rozdziały, etapy i zdolności Dantego [90101] — opis] - 모든 캐릭터의 타겟팅이 해제됩니다.\n- 턴 시작 페이즈 때 발동된 효과는 갱신되지 않습니다.
   źródło: DanteAbility.json :: dataList[id=90101].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Targeting for all Skills will be reset.\n- Effects activated at Turn Start will not be updated.
   PL: - Celowanie wszystkich postaci zostanie zresetowane.\n- Efekty aktywowane na Początku Tury nie zostaną odświeżone.
17. [Rozdziały, etapy i zdolności Dantego [90101] — opis bazowy] 모든 적의 속도가 절반으로 감소합니다.
   źródło: DanteAbility.json :: dataList[id=90101].rawDesc
   limit: do 120 znaków
   EN: Halve the Speed of all enemies.
   PL: Zmniejsza o połowę Szybkość wszystkich wrogów.
18. [Rozdziały, etapy i zdolności Dantego [80101] — opis] - 모든 캐릭터의 생성된 E.G.O 스킬이 초기화되고, 타겟팅이 해제됩니다.
   źródło: DanteAbility.json :: dataList[id=80101].desc
   limit: do 130 znaków
   EN: - Resets any slotted E.G.O Skills for all characters, and targeting for all Skills will be reset.
   PL: - Resetuje wygenerowane umiejętności E.G.O wszystkich postaci oraz ich celowanie.
19. [Rozdziały, etapy i zdolności Dantego [80101] — opis bazowy] E.G.O 스킬을 자원 소모 없이 1회 생성할 수 있습니다.
   źródło: DanteAbility.json :: dataList[id=80101].rawDesc
   limit: do 120 znaków
   EN: Slot in a single E.G.O Skill without consuming any E.G.O resources.
   PL: Pozwala jednorazowo wygenerować umiejętność E.G.O bez zużywania zasobów E.G.O.
20. [Rozdziały, etapy i zdolności Dantego [70101] — opis] - 모든 캐릭터의 공격 레벨과 방어 레벨이 3턴 동안 평균을 이룹니다.
   źródło: DanteAbility.json :: dataList[id=70101].desc
   limit: do 130 znaków
   EN: - For 3 turns, set all units' Offense and Defense Levels to the average of all units' values.
   PL: - Przez 3 tury uśrednia Poziom Ataku i Poziom Obrony wszystkich postaci na polu walki.
21. [Rozdziały, etapy i zdolności Dantego [70101] — opis bazowy] 모든 캐릭터의 공격 레벨과 방어 레벨이 평균을 이룹니다.
   źródło: DanteAbility.json :: dataList[id=70101].rawDesc
   limit: do 120 znaków
   EN: Set all units' Offense and Defense Levels to the average of all units' values.
   PL: Uśrednia Poziom Ataku i Poziom Obrony wszystkich postaci.
22. [Rozdziały, etapy i zdolności Dantego [50101] — opis] - 적용 효과\n • 이번 턴 동안 모든 스킬 코인이 선택한 면(앞면 또는 뒷면)으로 나올 확률 100% 고정\n • 이 효과는 캐릭터가 보유한 스킬, 패시브, 다른 효과보다 우선 적용됨\n- 모든 캐릭터의 타겟팅이 해제됩니다.\n- 이미 사망하였거나 조작 불가, 행동 불가인 캐릭터는 선택할 수 없습니다.
   źródło: DanteAbility.json :: dataList[id=50101].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Applied Effects:\n • For this turn, all Skill Coins have a 100% chance to flip Heads or Tails, depending on the side chosen\n • Prioritize this effect over the unit's Skills, Passives, and other effects\n- All characters' targeting will be reset.\n- Units that are killed, cannot be controlled, or immobilized cannot be selected.
   PL: - Nakładane efekty:\n • W tej turze wszystkie Monety umiejętności wybranej postaci mają 100% szansy na wypadnięcie wybraną stroną (Awersem lub Rewersem)\n • Efekt ten ma pierwszeństwo przed umiejętnościami, pasywkami i innymi efektami postaci\n- Celowanie wszystkich postaci zostanie zresetowane.\n- Nie można wybrać jednostek poległych, niekontrolowalnych ani niezdolnych do działania.
23. [Rozdziały, etapy i zdolności Dantego [50101] — opis bazowy] 캐릭터 1명을 선택하여 모든 스킬 코인을 앞면 또는 뒷면으로 고정합니다.
   źródło: DanteAbility.json :: dataList[id=50101].rawDesc
   limit: do 120 znaków
   EN: Select 1 target to gain a 100% chance to flip either Heads or Tails for all Skill Coins
   PL: Wybierz 1 postać, aby ustalić wynik wszystkich jej Monet umiejętności na Awers lub Rewers.

## Rozdziały, etapy i zdolności Dantego: DanteAbilityUIText
- plik gry: `DanteAbilityUIText.json`

24. [Rozdziały, etapy i zdolności Dantego [danteAbility_UIPopup_Title] — tekst] 빛의 묘목 능력 선택
   źródło: DanteAbilityUIText.json :: dataList[id=danteAbility_UIPopup_Title].content
   limit: do 120 znaków
   EN: Select Sapling of Light Ability
   PL: Wybór zdolności Sadzonki Światła
25. [Rozdziały, etapy i zdolności Dantego [danteAbility_UIPopup_Remain] — tekst] 남은 횟수
   źródło: DanteAbilityUIText.json :: dataList[id=danteAbility_UIPopup_Remain].content
   limit: do 120 znaków
   EN: Remaining Activations
   PL: Pozostałe użycia
26. [Rozdziały, etapy i zdolności Dantego [dnateAbiltiy_Unlock_GoldenBranch_Resonance] — tekst] 황금가지 공명
   źródło: DanteAbilityUIText.json :: dataList[id=dnateAbiltiy_Unlock_GoldenBranch_Resonance].content
   limit: do 120 znaków
   EN: Golden Bough Resonance
   PL: Rezonans Złotej Gałęzi
27. [Rozdziały, etapy i zdolności Dantego [tutorial_battle_danteAbility_title] — tekst] 빛의 묘목 능력
   źródło: DanteAbilityUIText.json :: dataList[id=tutorial_battle_danteAbility_title].content
   limit: do 120 znaków
   EN: Sapling of Light Ability
   PL: Zdolność Sadzonki Światła
28. [Rozdziały, etapy i zdolności Dantego [tutorial_battle_danteAbility_01_desc_01] — tekst] 우측 상단의 빛의 묘목 능력 버튼을 클릭합니다.
   źródło: DanteAbilityUIText.json :: dataList[id=tutorial_battle_danteAbility_01_desc_01].content
   limit: do 120 znaków
   EN: Select the Sapling of Light ability button on the top right.
   PL: Kliknij przycisk zdolności Sadzonki Światła w prawym górnym rogu.
29. [Rozdziały, etapy i zdolności Dantego [tutorial_battle_danteAbility_02_desc_01] — tekst] 사용할 능력을 선택합니다.
   źródło: DanteAbilityUIText.json :: dataList[id=tutorial_battle_danteAbility_02_desc_01].content
   limit: do 120 znaków
   EN: Select the ability to use.
   PL: Wybierz zdolność, której chcesz użyć.
30. [Rozdziały, etapy i zdolności Dantego [tutorial_battle_danteAbility_03_desc_01] — tekst] 확인 버튼을 누르면 빛의 묘목 능력이 발동됩니다.\n빛의 묘목은 사용 횟수만큼 사용할 수 있습니다.\n사용 횟수는 하루마다 초기화됩니다.
   źródło: DanteAbilityUIText.json :: dataList[id=tutorial_battle_danteAbility_03_desc_01].content
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Press the confirmation button to activate the Sapling of Light ability.\nSapling of Light can be used as long as there are remaining Activations.\nRemaining Activations are reset every day.
   PL: Naciśnij przycisk potwierdzenia, aby aktywować zdolność Sadzonki Światła.\nSadzonki Światła można używać do wyczerpania dostępnych użyć.\nLiczba użyć odnawia się każdego dnia.
31. [Rozdziały, etapy i zdolności Dantego [ui_activated] — tekst] 발동
   źródło: DanteAbilityUIText.json :: dataList[id=ui_activated].content
   limit: do 120 znaków
   EN: Activate
   PL: Aktywuj
32. [Rozdziały, etapy i zdolności Dantego [IsUnavailableDanteAbility_TitleText] — tekst] 사용할 수 없는 빛의 묘목 능력입니다.
   źródło: DanteAbilityUIText.json :: dataList[id=IsUnavailableDanteAbility_TitleText].content
   limit: do 120 znaków
   EN: Cannot use this Sapling of Light ability.
   PL: Nie można użyć tej zdolności Sadzonki Światła.
33. [Rozdziały, etapy i zdolności Dantego [IsUnavailableDanteAbility_DescText_IsActivatedAbility] — tekst] 오늘 이미 사용된 빛의 묘목 능력입니다.
   źródło: DanteAbilityUIText.json :: dataList[id=IsUnavailableDanteAbility_DescText_IsActivatedAbility].content
   limit: do 120 znaków
   EN: Already used this Sapling of Light ability today.
   PL: Ta zdolność Sadzonki Światła została już dzisiaj użyta.
34. [Rozdziały, etapy i zdolności Dantego [IsUnavailableDanteAbility_DescText_RemainingCountIsZero] — tekst] 오늘 더 이상 남은 횟수가 없습니다.
   źródło: DanteAbilityUIText.json :: dataList[id=IsUnavailableDanteAbility_DescText_RemainingCountIsZero].content
   limit: do 120 znaków
   EN: No remaining activations for today.
   PL: Brak pozostałych użyć na dzisiaj.
35. [Rozdziały, etapy i zdolności Dantego [danteAbility_50101_Option_0] — tekst] 앞면
   źródło: DanteAbilityUIText.json :: dataList[id=danteAbility_50101_Option_0].content
   limit: do 120 znaków
   EN: Heads
   PL: Awers
36. [Rozdziały, etapy i zdolności Dantego [danteAbility_50101_Option_1] — tekst] 뒷면
   źródło: DanteAbilityUIText.json :: dataList[id=danteAbility_50101_Option_1].content
   limit: do 120 znaków
   EN: Tails
   PL: Rewers

## Rozdziały, etapy i zdolności Dantego: DanteAbilityUIText_a1c9p3
- plik gry: `DanteAbilityUIText_a1c9p3.json`

37. [Rozdziały, etapy i zdolności Dantego [danteAbility_Personality_Selection_UIPopup_Title] — tekst] {0}: 수감자 선택
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbility_Personality_Selection_UIPopup_Title].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: {0}: Select Sinner
   PL: {0}: Wybierz Grzesznika
38. [Rozdziały, etapy i zdolności Dantego [danteAbility_Personality_Selection_UIPopup_View_Battle_Status] — tekst] 전투 현황 보기
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbility_Personality_Selection_UIPopup_View_Battle_Status].content
   limit: do 120 znaków
   EN: Observe Battlefield
   PL: Podgląd pola bitwy
39. [Rozdziały, etapy i zdolności Dantego [danteAbility_Personality_Selection_UIPopup_Confirm_Desc] — tekst] {0}을 적용하시겠습니까?\n적용 대상: <color=#f8c200>[{1}]</color>
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbility_Personality_Selection_UIPopup_Confirm_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, {0}, {1}, \n
   EN: Will you apply {0} on <color=#f8c200>[{1}]</color>?
   PL: Czy zastosować zdolność {0}?\nCel: <color=#f8c200>[{1}]</color>
40. [Rozdziały, etapy i zdolności Dantego [danteAbility_Apply] — tekst] 적용
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbility_Apply].content
   limit: do 120 znaków
   EN: Apply
   PL: Zastosuj
41. [Rozdziały, etapy i zdolności Dantego [danteAbilityButton_resume] — tekst] 돌아가기
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbilityButton_resume].content
   limit: do 120 znaków
   EN: Return
   PL: Wróć
42. [Rozdziały, etapy i zdolności Dantego [danteAbility_view_battle_status] — tekst] 현재 전투 현황
   źródło: DanteAbilityUIText_a1c9p3.json :: dataList[id=danteAbility_view_battle_status].content
   limit: do 120 znaków
   EN: Battlefield Status
   PL: Stan pola bitwy

## Rozdziały, etapy i zdolności Dantego: DungeonArea-a1c5p3
- plik gry: `DungeonArea-a1c5p3.json`

43. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0101] — tekst] 고래 위장
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0101].content
   limit: do 120 znaków
   EN: Whale Guts
   PL: Żołądek Wieloryba
44. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0102] — tekst] 피쿼드타운
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0102].content
   limit: do 120 znaków
   EN: Pequod Town
   PL: Miasteczko Pequod
45. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0103] — tekst] 에이해브 사무실
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0103].content
   limit: do 120 znaków
   EN: Ahab's Office
   PL: Gabinet Ahab
46. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0104] — tekst] 심장으로 떠나는 길
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0104].content
   limit: do 120 znaków
   EN: Journey to the Heart
   PL: Droga ku Sercu
47. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0201] — tekst] 피쿼드타운 출구
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0201].content
   limit: do 120 znaków
   EN: Pequod Town Entrance
   PL: Wyjście z Miasteczka Pequod
48. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0202] — tekst] 우심방
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0202].content
   limit: do 120 znaków
   EN: Right Heart Atrium
   PL: Prawy Przedsionek
49. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0203] — tekst] 우심실
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0203].content
   limit: do 120 znaków
   EN: Right Heart Ventricle
   PL: Prawa Komora
50. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0204] — tekst] 힘줄 다리
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0204].content
   limit: do 120 znaków
   EN: Sinew Bridge
   PL: Most ze Ścięgien
51. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0205] — tekst] 심장 소리가 들려오는 곳
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0205].content
   limit: do 120 znaków
   EN: Thumping of the Heart
   PL: Echo Bicia Serca
52. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0301] — tekst] 심장 앞 집결지
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0301].content
   limit: do 120 znaków
   EN: Rendezvous Area Before the Heart
   PL: Miejsce Zbiórki przed Sercem
53. [Rozdziały, etapy i zdolności Dantego [dungeon_1_5_0302] — tekst] 고래 심장
   źródło: DungeonArea-a1c5p3.json :: dataList[id=dungeon_1_5_0302].content
   limit: do 120 znaków
   EN: Heart of the Whale
   PL: Serce Wieloryba

## Rozdziały, etapy i zdolności Dantego: DungeonArea-a1c8p2
- plik gry: `DungeonArea-a1c8p2.json`

54. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0101] — tekst] 지상 실험실 제 n 입구
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0101].content
   limit: do 120 znaków
   EN: Ground Level Laboratory - Entrance n
   PL: Laboratorium Naziemne — Wejście n
55. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0102] — tekst] 준비실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0102].content
   limit: do 120 znaków
   EN: Preparation Room
   PL: Sala Przygotowawcza
56. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0103] — tekst] 검역실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0103].content
   limit: do 120 znaków
   EN: Quarantine Office
   PL: Izba Kwarantanny
57. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0104] — tekst] 지상 실험실 제 n 입구
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0104].content
   (powtórzenie elementu 54 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
58. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0105] — tekst] 폐기물 처리장
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0105].content
   limit: do 120 znaków
   EN: Waste Disposal
   PL: Składowisko Odpadów
59. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0106] — tekst] 제 4 실험실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0106].content
   limit: do 120 znaków
   EN: Laboratory 4
   PL: Laboratorium nr 4
60. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0107] — tekst] 연구동
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0107].content
   limit: do 120 znaków
   EN: Research Wing
   PL: Skrzydło Badawcze
61. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0108] — tekst] 처치실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0108].content
   limit: do 120 znaków
   EN: Execution Room
   PL: Sala Likwidacji
62. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0109] — tekst] 실험 구역
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0109].content
   limit: do 120 znaków
   EN: Experimentation Zone
   PL: Strefa Eksperymentalna
63. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0110] — tekst] 제 1 실험실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0110].content
   limit: do 120 znaków
   EN: Laboratory 1
   PL: Laboratorium nr 1
64. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0111] — tekst] 폐쇄된 실험실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0111].content
   limit: do 120 znaków
   EN: Closed Laboratory
   PL: Zamknięte Laboratorium
65. [Rozdziały, etapy i zdolności Dantego [dungeon_1_8_0112] — tekst] 제 2 실험실
   źródło: DungeonArea-a1c8p2.json :: dataList[id=dungeon_1_8_0112].content
   limit: do 120 znaków
   EN: Laboratory 2
   PL: Laboratorium nr 2

## Rozdziały, etapy i zdolności Dantego: DungeonArea1-1
- plik gry: `DungeonArea1-1.json`

66. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0101] — tekst] 지휘팀 담당 격리 지역
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0101].content
   limit: do 120 znaków
   EN: Control Team Containment
   PL: Strefa Izolacji Zespołu Dowodzenia
67. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0102] — tekst] 지휘팀 로비
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0102].content
   limit: do 120 znaków
   EN: Control Team Lobby
   PL: Lobby Zespołu Dowodzenia
68. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0103] — tekst] 제 1 격리 복도
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0103].content
   limit: do 120 znaków
   EN: Containment Hall 1
   PL: Korytarz Izolacyjny nr 1
69. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0104] — tekst] 제 2 격리 복도
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0104].content
   limit: do 120 znaków
   EN: Containment Hall 2
   PL: Korytarz Izolacyjny nr 2
70. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0105] — tekst] 제 3 격리 복도
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0105].content
   limit: do 120 znaków
   EN: Containment Hall 3
   PL: Korytarz Izolacyjny nr 3
71. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0106] — tekst] 직원 휴게실
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0106].content
   limit: do 120 znaków
   EN: Employee Lounge
   PL: Pokój Socjalny Pracowników
72. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0107] — tekst] 정보팀\n연결통로
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0107].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Info. Team Passage
   PL: Łącznik\nZesp. Informacji
73. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0201] — tekst] 정보팀\n로비
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0201].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Info. Team Lobby
   PL: Lobby\nZesp. Informacji
74. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0202] — tekst] 직원 대기실
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0202].content
   limit: do 120 znaków
   EN: Employee Waiting Room
   PL: Poczekalnia Pracowników
75. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0203] — tekst] 제 4 격리복도
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0203].content
   limit: do 120 znaków
   EN: Containment Hall 4
   PL: Korytarz Izolacyjny nr 4
76. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0204] — tekst] 제 5 격리복도
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0204].content
   limit: do 120 znaków
   EN: Containment Hall 5
   PL: Korytarz Izolacyjny nr 5
77. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0205] — tekst] 탕비실
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0205].content
   limit: do 120 znaków
   EN: Canteen
   PL: Kuchnia Pracownicza
78. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0206] — tekst] 간이통로
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0206].content
   limit: do 120 znaków
   EN: Reserve Passageway
   PL: Przejście Zapasowe
79. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0207] — tekst] 중요\n환상체 관리소
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0207].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Critical Abnormality Block
   PL: Blok Groźnych\nAnomalii
80. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0301] — tekst] 연기전쟁 중부 전선
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0301].content
   limit: do 120 znaków
   EN: Smoke War Central Front
   PL: Front Środkowy Wojny Dymnej
81. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0302] — tekst] 제 23-7 방어선 11:00
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0302].content
   limit: do 120 znaków
   EN: Defense Line 23-7 - 1100 Hours
   PL: Linia Obrony 23-7 — 11:00
82. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0303] — tekst] 주요 거점
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0303].content
   limit: do 120 znaków
   EN: Key Foothold
   PL: Kluczowy Przyczółek
83. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0304] — tekst] 제 23-7 방어선 13:00
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0304].content
   limit: do 120 znaków
   EN: Defense Line 23-7 - 1300 Hours
   PL: Linia Obrony 23-7 — 13:00
84. [Rozdziały, etapy i zdolności Dantego [dungeon_1_1_0305] — tekst] 제 23-7 방어선 15:36
   źródło: DungeonArea1-1.json :: dataList[id=dungeon_1_1_0305].content
   limit: do 120 znaków
   EN: Defense Line 23-7 - 1536 Hours
   PL: Linia Obrony 23-7 — 15:36

## Rozdziały, etapy i zdolności Dantego: DungeonArea1-2
- plik gry: `DungeonArea1-2.json`

85. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0101] — tekst] 금고 보관실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0101].content
   limit: do 120 znaków
   EN: Vault Storage
   PL: Skarbiec
86. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0102] — tekst] 채굴장 출입구
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0102].content
   limit: do 120 znaków
   EN: Quarry Entrance
   PL: Wejście do Wyrobiska
87. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0103] — tekst] 제 1 채굴장
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0103].content
   limit: do 120 znaków
   EN: Quarry 1
   PL: Wyrobisko nr 1
88. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0104] — tekst] 제 2 채굴장
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0104].content
   limit: do 120 znaków
   EN: Quarry 2
   PL: Wyrobisko nr 2
89. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0105] — tekst] 제 3 채굴장
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0105].content
   limit: do 120 znaków
   EN: Quarry 3
   PL: Wyrobisko nr 3
90. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0106] — tekst] 제 4 채굴장
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0106].content
   limit: do 120 znaków
   EN: Quarry 4
   PL: Wyrobisko nr 4
91. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0107] — tekst] 폭약 적재소
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0107].content
   limit: do 120 znaków
   EN: Explosives Bay
   PL: Skład Materiałów Wybuchowych
92. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0108] — tekst] 죄종 수용소
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0108].content
   limit: do 120 znaków
   EN: Peccatula Enclosure
   PL: Klatki Peccatulów
93. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0109] — tekst] 대피소
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0109].content
   limit: do 120 znaków
   EN: Shelter
   PL: Schron
94. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0110] — tekst] 지하 공장 출입구
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0110].content
   limit: do 120 znaków
   EN: Underground Factory Gate
   PL: Brama Podziemnej Fabryki
95. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0201] — tekst] 공장 입구
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0201].content
   limit: do 120 znaków
   EN: Factory Entrance
   PL: Wejście do Fabryki
96. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0202] — tekst] 1번 라인
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0202].content
   limit: do 120 znaków
   EN: Production Line 1
   PL: Linia Produkcyjna nr 1
97. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0203] — tekst] 2번 라인
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0203].content
   limit: do 120 znaków
   EN: Production Line 2
   PL: Linia Produkcyjna nr 2
98. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0204] — tekst] 3번 라인
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0204].content
   limit: do 120 znaków
   EN: Production Line 3
   PL: Linia Produkcyjna nr 3
99. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0205] — tekst] 사출\n성형실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0205].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Molding Chamber
   PL: Hala\nOdlewnicza
100. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0206] — tekst] 사출\n성형실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0206].content
   (powtórzenie elementu 99 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
101. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0207] — tekst] 부품\n조립실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0207].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Assembly Line
   PL: Hala\nMontażu
102. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0208] — tekst] 도장실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0208].content
   limit: do 120 znaków
   EN: Paint Shop
   PL: Lakiernia
103. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0209] — tekst] 설비\n정비소
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0209].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Maintenance Point
   PL: Warsztat\nKonserwacji
104. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0210] — tekst] 비상\n발전소
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0210].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Backup Generators
   PL: Zasilanie\nAwaryjne
105. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0211] — tekst] 안전 검사 시설
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0211].content
   limit: do 120 znaków
   EN: Safety Testing
   PL: Stacja Kontroli Bezpieczeństwa
106. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0212] — tekst] 전진 기지
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0212].content
   limit: do 120 znaków
   EN: Forward Base
   PL: Baza Wysunięta
107. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0213] — tekst] 최종 가공실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0213].content
   limit: do 120 znaków
   EN: Final Processing
   PL: Obróbka Końcowa
108. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0214] — tekst] 폐기물 처리장
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0214].content
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
109. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0215] — tekst] 검증실
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0215].content
   limit: do 120 znaków
   EN: Quality Control
   PL: Kontrola Jakości
110. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0301] — tekst] 설원 갈림길
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0301].content
   limit: do 120 znaków
   EN: Snowy Crossroads
   PL: Śnieżne Rozdroże
111. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0302] — tekst] 얼어붙은 폐허
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0302].content
   limit: do 120 znaków
   EN: Frozen Ruins
   PL: Zamarznięte Ruiny
112. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0303] — tekst] 파괴된 마을
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0303].content
   limit: do 120 znaków
   EN: Ruined Village
   PL: Zniszczona Wioska
113. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0304] — tekst] 눈보라 지대
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0304].content
   limit: do 120 znaków
   EN: Snowstorm Fields
   PL: Pole Śnieżycy
114. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0305] — tekst] 파묻힌 은신처
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0305].content
   limit: do 120 znaków
   EN: Buried Hideout
   PL: Zasypana Kryjówka
115. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0306] — tekst] 도개교
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0306].content
   limit: do 120 znaków
   EN: Drawbridge
   PL: Most Zwodzony
116. [Rozdziały, etapy i zdolności Dantego [dungeon_1_2_0307] — tekst] 잠든\n이웃들의 성
   źródło: DungeonArea1-2.json :: dataList[id=dungeon_1_2_0307].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ice Castle Where Neighbors Lie
   PL: Zamek Śpiących\nSąsiadów

## Rozdziały, etapy i zdolności Dantego: DungeonArea1-3
- plik gry: `DungeonArea1-3.json`

117. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0101] — tekst] 관문 초입
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0101].content
   limit: do 120 znaków
   EN: Gate Entrance
   PL: Przedpole Bramy
118. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0102] — tekst] 지하실 입구
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0102].content
   limit: do 120 znaków
   EN: Basement Entrance
   PL: Wejście do Podziemi
119. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0103] — tekst] 기계 장치방
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0103].content
   limit: do 120 znaków
   EN: Machinery Room
   PL: Maszynownia
120. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0104] — tekst] 제 1 관문
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0104].content
   limit: do 120 znaków
   EN: Gate #1
   PL: Brama nr 1
121. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0105] — tekst] 폐쇄된 문
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0105].content
   limit: do 120 znaków
   EN: Sealed Door
   PL: Zapieczętowane Drzwi
122. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0106] — tekst] 잊혀진 통로
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0106].content
   limit: do 120 znaków
   EN: Forgotten Passage
   PL: Zapomniany Korytarz
123. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0107] — tekst] 격리 구역
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0107].content
   limit: do 120 znaków
   EN: Containment Area
   PL: Strefa Izolacji
124. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0108] — tekst] 침식 개체 격리소
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0108].content
   limit: do 120 znaków
   EN: Corroded Entity Block
   PL: Blok Skorodowanych Bytów
125. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0109] — tekst] 정예병 훈련소
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0109].content
   limit: do 120 znaków
   EN: Elite Training Quarters
   PL: Koszary Elitarne
126. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0110] — tekst] 감옥 구역
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0110].content
   limit: do 120 znaków
   EN: Prison Area
   PL: Lochy Więzienne
127. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0111] — tekst] 옛 창고
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0111].content
   limit: do 120 znaków
   EN: Old Warehouse
   PL: Stary Magazyn
128. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0112] — tekst] 봉쇄 구역
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0112].content
   limit: do 120 znaków
   EN: Blockade Zone
   PL: Strefa Blokady
129. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0113] — tekst] 예배실
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0113].content
   limit: do 120 znaków
   EN: Chapel
   PL: Kaplica
130. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0114] — tekst] 고문실
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0114].content
   limit: do 120 znaków
   EN: Torture Chamber
   PL: Sala Tortur
131. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0201] — tekst] 지하 예배당 복도
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0201].content
   limit: do 120 znaków
   EN: Church Corridor
   PL: Korytarz Podziemnej Kaplicy
132. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0202] — tekst] 페쇄된 기도실
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0202].content
   limit: do 120 znaków
   EN: Closed Prayer Room
   PL: Zamknięta Rozmównica Modlitewna
133. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0203] — tekst] 비명이\n들리는 방
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0203].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Room of Echoing Screams
   PL: Komnata\nKrzyków
134. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0204] — tekst] 제 2 관문
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0204].content
   limit: do 120 znaków
   EN: Gate #2
   PL: Brama nr 2
135. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0205] — tekst] 짓무름의 다리
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0205].content
   limit: do 120 znaków
   EN: Bridge of Suppuration
   PL: Most Jątrzenia
136. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0206] — tekst] 지하 예배당
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0206].content
   limit: do 120 znaków
   EN: Underground Church
   PL: Podziemna Kaplica
137. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0207] — tekst] 묵상의 교단
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0207].content
   limit: do 120 znaków
   EN: Meditator’s Pulpit
   PL: Ambona Kontemplacji
138. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0208] — tekst] 예배당 입구
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0208].content
   limit: do 120 znaków
   EN: Church Door
   PL: Wrota Kaplicy
139. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0209] — tekst] 눈물의 제단
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0209].content
   limit: do 120 znaków
   EN: Altar of Tears
   PL: Ołtarz Łez
140. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0210] — tekst] 제단 입구
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0210].content
   limit: do 120 znaków
   EN: Altar Entrance
   PL: Wejście do Ołtarza
141. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0211] — tekst] 성물함
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0211].content
   limit: do 120 znaków
   EN: Sacristy
   PL: Relikwiarz
142. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0212] — tekst] 중앙 구역
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0212].content
   limit: do 120 znaków
   EN: Central Area
   PL: Strefa Centralna
143. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0213] — tekst] 속죄의 제단
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0213].content
   limit: do 120 znaków
   EN: Altar of Penance
   PL: Ołtarz Pokuty
144. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0214] — tekst] 정화소
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0214].content
   limit: do 120 znaków
   EN: Purificatory
   PL: Oczyszczalnia
145. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0215] — tekst] 제 3 관문
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0215].content
   limit: do 120 znaków
   EN: Gate #3
   PL: Brama nr 3
146. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0216] — tekst] 자격 판별대
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0216].content
   limit: do 120 znaków
   EN: The Judging Block
   PL: Trybunał Osądu
147. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0217] — tekst] 성소로 가는 길
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0217].content
   limit: do 120 znaków
   EN: Path to Hallowed Ground
   PL: Droga do Sanktuarium
148. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0301] — tekst] 의식의 광장
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0301].content
   limit: do 120 znaków
   EN: Ritual Square
   PL: Plac Rytualny
149. [Rozdziały, etapy i zdolności Dantego [dungeon_1_3_0302] — tekst] 시체들의 언덕
   źródło: DungeonArea1-3.json :: dataList[id=dungeon_1_3_0302].content
   limit: do 120 znaków
   EN: Hill of Corpses
   PL: Wzgórze Trupów

## Rozdziały, etapy i zdolności Dantego: DungeonArea1-4
- plik gry: `DungeonArea1-4.json`

150. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0101] — tekst] 봄의 구인회 연구실
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0101].content
   limit: do 120 znaków
   EN: League of Nine Littérateurs Lab - Spring
   PL: Pracownia Kręgu Dziewięciu — Wiosna
151. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0102] — tekst] 재배치 된 K사 연구소
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0102].content
   limit: do 120 znaków
   EN: Rearranged K Corp. Laboratory
   PL: Przebudowane Laboratorium K Corp.
152. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0201] — tekst] 가을의 구인회 연구실
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0201].content
   limit: do 120 znaków
   EN: League of Nine Littérateurs Lab - Autumn
   PL: Pracownia Kręgu Dziewięciu — Jesień
153. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0202] — tekst] 여름의 구인회 연구실
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0202].content
   limit: do 120 znaków
   EN: League of Nine Littérateurs Lab - Summer
   PL: Pracownia Kręgu Dziewięciu — Lato
154. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0301] — tekst] 겨울의 구인회 연구실
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0301].content
   limit: do 120 znaków
   EN: League of Nine Littérateurs Lab - Winter
   PL: Pracownia Kręgu Dziewięciu — Zima
155. [Rozdziały, etapy i zdolności Dantego [dungeon_1_4_0302] — tekst] N사의 하얀 방
   źródło: DungeonArea1-4.json :: dataList[id=dungeon_1_4_0302].content
   limit: do 120 znaków
   EN: N Corp's White Room
   PL: Biały Pokój N Corp.

## Rozdziały, etapy i zdolności Dantego: DungeonName_Event
- plik gry: `DungeonName_Event.json`

156. [Rozdziały, etapy i zdolności Dantego [910301] — nazwa] 3.5장 헬스치킨 던전
   źródło: DungeonName_Event.json :: dataList[id=910301].name
   limit: do 50 znaków
   EN: Ch. 3.5 Hell's Chicken Dungeon
   PL: Rozdz. 3.5 — Loch Piekielnego Kurczaka
157. [Rozdziały, etapy i zdolności Dantego [910302] — nazwa] 3.5장 헬스치킨 던전(어려움 난이도)
   źródło: DungeonName_Event.json :: dataList[id=910302].name
   limit: do 70 znaków
   EN: Ch. 3.5 Hell's Chicken Dungeon (Hard Difficulty)
   PL: Rozdz. 3.5 — Loch Piekielnego Kurczaka (Trudny)
158. [Rozdziały, etapy i zdolności Dantego [910701] — nazwa] 5.5장 육참골단 던전
   źródło: DungeonName_Event.json :: dataList[id=910701].name
   limit: do 70 znaków
   EN: Ch. 5.5 Yield My Flesh to Claim Their Bones Dungeon
   PL: Rozdz. 5.5 — Loch „Oddam Ciało, by Złamać Ich Kości”
159. [Rozdziały, etapy i zdolności Dantego [910901] — nazwa] 6.5장 시간살인시간 던전
   źródło: DungeonName_Event.json :: dataList[id=910901].name
   limit: do 50 znaków
   EN: Ch. 6.5 Timekilling Time Dungeon
   PL: Rozdz. 6.5 — Loch Czasu Zabijania Czasu
160. [Rozdziały, etapy i zdolności Dantego [911401] — nazwa] 7.5장 LCB 정기검진 던전
   źródło: DungeonName_Event.json :: dataList[id=911401].name
   limit: do 50 znaków
   EN: Ch. 7.5 LCB Regular Check-up Dungeon
   PL: Rozdz. 7.5 — Loch Okresowych Badań LCB
161. [Rozdziały, etapy i zdolności Dantego [911501] — nazwa] 5.5장 육참골단 던전(어려움 난이도)
   źródło: DungeonName_Event.json :: dataList[id=911501].name
   limit: do 100 znaków
   EN: Ch. 5.5 Yield My Flesh to Claim Their Bones Dungeon (Hard Difficulty)
   PL: Rozdz. 5.5 — Loch „Oddam Ciało, by Złamać Ich Kości” (Trudny)
162. [Rozdziały, etapy i zdolności Dantego [911801] — nazwa] 6.5장 시간살인시간 던전(어려움 난이도)
   źródło: DungeonName_Event.json :: dataList[id=911801].name
   limit: do 70 znaków
   EN: Ch. 6.5 Timekilling Time Dungeon (Hard Difficulty)
   PL: Rozdz. 6.5 — Loch Czasu Zabijania Czasu (Trudny)
163. [Rozdziały, etapy i zdolności Dantego [912014] — nazwa] 선의의 순례 던전
   źródło: DungeonName_Event.json :: dataList[id=912014].name
   limit: do 50 znaków
   EN: Pilgrimage of Compassion Dungeon
   PL: Loch Pielgrzymki Współczucia
164. [Rozdziały, etapy i zdolności Dantego [912114] — nazwa] 선의의 순례 던전(어려움 난이도)
   źródło: DungeonName_Event.json :: dataList[id=912114].name
   limit: do 70 znaków
   EN: Pilgrimage of Compassion Dungeon (Hard Difficulty)
   PL: Loch Pielgrzymki Współczucia (Trudny)
165. [Rozdziały, etapy i zdolności Dantego [912401] — nazwa] 7.5장 LCB 정기검진 던전 (어려움 난이도)
   źródło: DungeonName_Event.json :: dataList[id=912401].name
   limit: do 80 znaków
   EN: Ch. 7.5 LCB Regular Check-up Dungeon (Hard Difficulty)
   PL: Rozdz. 7.5 — Loch Okresowych Badań LCB (Trudny)
166. [Rozdziały, etapy i zdolności Dantego [912711] — nazwa] 9.5장 경험기억 던전
   źródło: DungeonName_Event.json :: dataList[id=912711].name
   limit: do 50 znaków
   EN: Ch. 9.5 Mnestic Experience Dungeon
   PL: Rozdz. 9.5 — Loch Pamięci Doświadczenia

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-1
- plik gry: `DungeonNode1-1.json`

167. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 지휘팀 담당 격리구역
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=12].title
   limit: do 40 znaków
   EN: Control Team Containment
   PL: Strefa Izolacji Zespołu Dowodzenia
168. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 처음 맞닥뜨리는 로보토미 코퍼레이션 지부는 입구부터 처참하기 그지 없는 광경을 띠고 있었다. 우리는 할말을 잃은 채 벌레 신체를 가진 시체들을 가만히 쳐다보았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=12].desc
   limit: do 210 znaków
   EN: First impressions of the Lobotomy Corporation facility were downright gruesome. Rendered speechless, we stared into the corpses of people with insectile features.
   PL: Pierwszy napotkany oddział Lobotomy Corporation już od progu witał makabrycznym widokiem. Odebrało nam mowę na widok zwłok o owadzich kończynach.
169. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 지휘팀 담당 격리구역
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=11].title
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
170. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 처음 맞닥뜨리는 로보토미 코퍼레이션 지부는 입구부터 처참하기 그지 없는 광경을 띠고 있었다. 우리는 할말을 잃은 채 벌레 신체를 가진 시체들을 가만히 쳐다보았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=11].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
171. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 지휘팀 로비
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=10].title
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 처음 맞닥뜨리는 로보토미 코퍼레이션 지부는 입구부터 처참하기 그지 없는 광경을 띠고 있었다. 우리는 할말을 잃은 채 벌레 신체를 가진 시체들을 가만히 쳐다보았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=10].desc
   (powtórzenie elementu 168 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 직원 대기실
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=110].title
   (powtórzenie elementu 74 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 어둠이 가득 찬 복도 속, 끄트머리에서 누군가의 인영이 보인다. 그것 역시 가만히 다가오는 우리를 가만히 쳐다보고 있다. 확실하진 않아도 하나만은 분명했다. 서로가 서로에게 달가운 존재는 분명히 아닐 것이라고.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=110].desc
   limit: do 200 znaków
   EN: A shadow appears in the dusky corridor. It carefully watches us approach. It was clear that we were not going to be a welcome presence to each other.
   PL: W głębi spowitego mrokiem korytarza zamajaczyła czyjaś sylwetka, bacznie obserwująca nasze kroki. Jedno było pewne: żadna ze stron nie ucieszy się z tego spotkania.
175. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 11:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=210].title
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
176. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 다음 층으로 올라가자마자 눈에 보이는 건 수많은 구더기였다. 곧이어 번쩍이는 황금빛과 함께 희뿌연 하늘과 포격, 함성 소리가 우리를 환영처럼 맞이한다. 그레고르의 잇새 사이로 헝클어진 목소리가 이곳이 전장 한복판이라는 사실을 알 수 있었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=210].desc
   limit: do 300 znaków
   EN: A swarm of maggots was the first thing we saw on the next floor. Then, with a golden flash, we were greeted by a blurry sky, ringing with the sounds of cannons and shouts. Gregor’s shaky voice let me know that this was a battlefield.
   PL: Gdy tylko weszliśmy na kolejne piętro, powitało nas mrowie czerwi. Chwilę później wśród złotego błysku wyłoniło się zamglone niebo, huk dział i bitewne okrzyki. Drżący głos Gregora uświadomił mi, że znaleźliśmy się w samym środku pola bitwy.
177. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 11:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=211].title
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 다음 층으로 올라가자마자 눈에 보이는 건 수많은 구더기였다. 곧이어 번쩍이는 황금빛과 함께 희뿌연 하늘과 포격, 함성 소리가 우리를 환영처럼 맞이한다. 그레고르의 잇새 사이로 헝클어진 목소리가 이곳이 전장 한복판이라는 사실을 알 수 있었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=211].desc
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
179. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 11:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=212].title
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
180. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 다음 층으로 올라가자마자 눈에 보이는 건 수많은 구더기였다. 곧이어 번쩍이는 황금빛과 함께 희뿌연 하늘과 포격, 함성 소리가 우리를 환영처럼 맞이한다. 그레고르의 잇새 사이로 헝클어진 목소리가 이곳이 전장 한복판이라는 사실을 알 수 있었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=212].desc
   (powtórzenie elementu 176 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=250].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=250].desc
   limit: do 210 znaków
   EN: Tomah the young soldier greets us as though this were his first time seeing us, and our surroundings make less and less sense. Is this how Gregor viewed his past?
   PL: Młody żołnierz imieniem Tomah wita się z nami, jakby widział nas po raz pierwszy, a otoczenie z każdą chwilą traci spójność. Czy tak potwornie wyglądała przeszłość w pamięci Gregora?
183. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 1 격리복도
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=20].title
   limit: do 40 znaków
   EN: Containment Hall 1
   PL: Korytarz Izolacyjny nr 1
184. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 환상체처럼 보이지만 환상체와는 확연히 다른 것을 상대하게 되며 우리는 혼란에 휩싸였다. 표정을 보아하니 유리조차도 모르는 얼굴이었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=20].desc
   limit: do 190 znaków
   EN: We were perplexed by the encounter with creatures that, at first glance, resembled Abnormalities. Yuri seemed just as confused as the rest of us.
   PL: Starcie z istotami przypominającymi z pozoru Anomalie, lecz wyraźnie od nich odmiennymi, wprawiło nas w zakłopotanie. Sądząc po minie Yuri, ona również nie wiedziała, czym są.
185. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 2 격리복도
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=30].title
   limit: do 40 znaków
   EN: Containment Hall 2
   PL: Korytarz Izolacyjny nr 2
186. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 연달아 전투를 거치면서 수감자들이 크고 작은 부상을 입고 지쳐갔다. 이제는 시계를 돌려야 할 때였다. 파우스트가 적당한 장소를 찾으려는 듯 주위를 둘러본다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=30].desc
   limit: do 200 znaków
   EN: Continued battles have wounded and fatigued the Sinners. It was about time I winded my clock. Faust looks around for the right spot to let me do my thing.
   PL: Kolejne potyczki wyczerpały i poraniły Grzeszników. Nadeszła pora, by cofnąć wskazówki zegara. Faust rozgląda się za odpowiednim ku temu miejscem.
187. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 2 격리복도
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=31].title
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 연달아 전투를 거치면서 수감자들이 크고 작은 부상을 입고 지쳐갔다. 이제는 시계를 돌려야 할 때였다. 파우스트가 적당한 장소를 찾으려는 듯 주위를 둘러본다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=31].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 직원 휴게실
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=40].title
   (powtórzenie elementu 71 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 연달아 전투를 거치면서 수감자들이 크고 작은 부상을 입고 지쳐갔다. 이제는 시계를 돌려야 할 때였다. 파우스트가 적당한 장소를 찾으려는 듯 주위를 둘러본다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=40].desc
   (powtórzenie elementu 186 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
191. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=240].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
192. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=240].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 4 격리복도
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=121].title
   (powtórzenie elementu 75 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 어둠이 가득 찬 복도 속, 끄트머리에서 누군가의 인영이 보인다. 그것 역시 가만히 다가오는 우리를 가만히 쳐다보고 있다. 확실하진 않아도 하나만은 분명했다. 서로가 서로에게 달가운 존재는 분명히 아닐 것이라고.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=121].desc
   (powtórzenie elementu 174 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
195. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 5 격리복도
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=120].title
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
196. [Rozdziały, etapy i zdolności Dantego [10101] — opis] '더 이상 전진 하지 말아라' 그레고르의 옛 상사가 남긴 경고를 뒤로 하고 앞으로 향했다. 그 어리석음을 질책이라도 하는 듯 어디선가 메케한 냄새가 퍼져가기 시작했다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=120].desc
   limit: do 180 znaków
   EN: Leaving aside the warning from Gregor’s old boss, we moved on. An acrid smell began to fill the air as if to punish our foolhardiness.
   PL: Mijając ostrzeżenie dawnego przełożonego Gregora — „Nie idźcie dalej” — ruszyliśmy naprzód. W powietrzu rozszedł się gryzący swąd, jakby chciał skarcić naszą zuchwałość.
197. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 탕비실
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=130].title
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 아마 이곳에 수많은 재앙을 몰고 왔을 환상체를 만났다. 유리 말로는 한때 환상체들은 관리법이라는 규율 아래 철저히 감독되어 왔다고 한다. 그렇다면 지부가 폐쇄된 이후부터는 어떻게 되었을지 상상에게라도 맡기고 싶지 않았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=130].desc
   limit: do 360 znaków
   EN: We faced the Abnormality that most likely caused many disasters in the facility. According to Yuri, these Abnormalities used to be under strict supervision, kept in check by detailed managerial procedures. I don’t want to imagine what happened now that the facility’s faced closure.
   PL: Stanęliśmy oko w oko z Anomalią, która musiała sprowadzić na to miejsce niezliczone nieszczęścia. Według Yuri Anomalie trzymano niegdyś w ryzach ścisłych procedur zarządczych. Strach było nawet myśleć, co działo się tu po zamknięciu filii.
199. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 직원 식당
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=140].title
   limit: do 40 znaków
   EN: Cafeteria
   PL: Stołówka Pracownicza
200. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 아마 이곳에 수많은 재앙을 몰고 왔을 환상체를 만났다. 유리 말로는 한때 환상체들은 관리법이라는 규율 아래 철저히 감독되어 왔다고 한다. 그렇다면 지부가 폐쇄된 이후부터는 어떻게 되었을지 상상에게라도 맡기고 싶지 않았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=140].desc
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 정보팀 연결통로
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=50].title
   limit: do 40 znaków
   EN: Info. Team Passage
   PL: Łącznik Zespołu Informacji
202. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 시계를 돌리며 수감자 전원이 무사히 회복이 됐지만 지부는  불길한 징조로 변해간다. 복도를 감싸는 가시들이 금방이라도 신체를 꿰뚫기라도 한 것처럼 곤두세워지고 있는 건 내 착각이길 바라며, 발걸음을 계속했다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=50].desc
   limit: do 260 znaków
   EN: The clock restored every Sinner to health, but the facility continues to grow more foreboding. Hoping that I was only imagining that the spiky things along the aisles bristled up, we proceeded farther.
   PL: Cofnięcie zegara uzdrowiło wszystkich Grzeszników, lecz sama placówka staje się coraz bardziej złowieszcza. Mając nadzieję, że kolce jeżące się wzdłuż ścian korytarza to tylko złudzenie, ruszyliśmy dalej.
203. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 중요 환상체 격리소
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=150].title
   limit: do 40 znaków
   EN: Critical Abnormality Block
   PL: Blok Groźnych Anomalii
204. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 아마 이곳에 수많은 재앙을 몰고 왔을 환상체를 만났다. 유리 말로는 한때 환상체들은 관리법이라는 규율 아래 철저히 감독되어 왔다고 한다. 그렇다면 지부가 폐쇄된 이후부터는 어떻게 되었을지 상상에게라도 맡기고 싶지 않았다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=150].desc
   (powtórzenie elementu 198 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
205. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 15:36
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=270].title
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
206. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 그레고르의 기억 속 거대한 손바닥은 우리를 다시 격리실로 이끌었다. 전장에서 벗어났다고 전쟁이 끝난 게 아니듯, 황금가지를 찾기 위해선 아직 가야 할 길이 남아 있다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=270].desc
   limit: do 260 znaków
   EN: The massive hand from Gregor’s memories took us back to the containment unit. Getting off the battleground doesn’t mean the end of the war, however; the Golden Bough is still waiting to be claimed.
   PL: Olbrzymia dłoń ze wspomnień Gregora przeniosła nas z powrotem do celi izolacyjnej. Zejście z pola bitwy nie oznacza jednak końca wojny — wciąż musimy odnaleźć Złotą Gałąź.
207. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=241].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
208. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=241].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
209. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=242].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
210. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=242].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 11:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=100117].title
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
212. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 시계를 돌리며 수감자 전원이 무사히 회복이 됐지만 지부는 불길한 징조로 변해간다. 복도를 감싸는 가시들이 금방이라도 신체를 꿰뚫기라도 한 것처럼 곤두세워지고 있는 건 내 착각이길 바라며, 발걸음을 계속했다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=100117].desc
   limit: do 260 znaków
   EN: The clock restored every Sinner to health, but the facility continues to grow more foreboding. Hoping that I was only imagining that the spiky things along the aisles bristled up, we proceeded farther.
   PL: Cofnięcie zegara uzdrowiło wszystkich Grzeszników, lecz sama placówka staje się coraz bardziej złowieszcza. Mając nadzieję, że kolce jeżące się wzdłuż ścian korytarza to tylko złudzenie, ruszyliśmy dalej.
213. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 15:36
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=251].title
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
214. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=251].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
215. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 15:36
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=260].title
   (powtórzenie elementu 84 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 앳된 얼굴의 병사였던 토마 라는 자는 우리를 기억하지 못한다는 듯 인사를 건네오고 공간은 점점 지리멸렬하게 변해간다. 그레고르 속 기억은 이토록 끔찍한 광경이었던 걸까.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=260].desc
   (powtórzenie elementu 182 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
217. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=221].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
218. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 전장 속에서 우리는 그레고르과 같은 벌레 신체를 가진 자들과 전투를 벌인다. 이곳이 어디인지, 저 자들은 누구인지 알 수는 없었지만 어쩌면 이것이 황금가지로 인한 영향일지도 모른다는 예감이 들었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=221].desc
   limit: do 270 znaków
   EN: On the battlefield, we fight soldiers with insectile body parts just like Gregor. I couldn’t tell where this was or who they were, but I got the feeling that this was a product of the Golden Bough’s influence.
   PL: Pośród bitewnego zgiełku walczymy z ludźmi o owadzich ciałach podobnych do Gregora. Nie wiedziałem, gdzie jesteśmy ani kim są, lecz przeczuwałem, że to sprawka Złotej Gałęzi.
219. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=220].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
220. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 전장 속에서 우리는 그레고르과 같은 벌레 신체를 가진 자들과 전투를 벌인다. 이곳이 어디인지, 저 자들은 누구인지 알 수는 없었지만 어쩌면 이것이 황금가지로 인한 영향일지도 모른다는 예감이 들었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=220].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 13:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=230].title
   (powtórzenie elementu 83 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
222. [Rozdziały, etapy i zdolności Dantego [10101] — opis] 전장 속에서 우리는 그레고르과 같은 벌레 신체를 가진 자들과 전투를 벌인다. 이곳이 어디인지, 저 자들은 누구인지 알 수는 없었지만 어쩌면 이것이 황금가지로 인한 영향일지도 모른다는 예감이 들었다.
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=230].desc
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
223. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 지휘팀 로비
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=0].title
   (powtórzenie elementu 67 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
224. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 정보팀 로비
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=100].title
   limit: do 40 znaków
   EN: Info. Team Lobby
   PL: Lobby Zespołu Informacji
225. [Rozdziały, etapy i zdolności Dantego [10101] — tytuł] 제 23-7 방어선 11:00
   źródło: DungeonNode1-1.json :: dataList[id=10101].stageList[id=200].title
   (powtórzenie elementu 81 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-2
- plik gry: `DungeonNode1-2.json`

226. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 채굴장 출입구
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=10].title
   (powtórzenie elementu 86 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
227. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=10].desc
   limit: do 300 znaków
   EN: Even though we won the right to enter the basement, the Lobotomy Corp. Branch seemed to be long overtaken by the casino. Slaves dig away at walls, security guards watch them, and Peccatula chew at iron bars… A lot stood in our way.
   PL: Jako zwycięzcy gry zdołaliśmy zjechać pod ziemię, lecz filia Lobotomy Corp. od dawna należała już do kasyna. Niewolnicy kujący skałę, pilnujący ich strażnicy i Peccatula gryzące kraty… Musieliśmy przebić się przez to wszystko.
228. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 제 1 채굴장
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=20].title
   (powtórzenie elementu 87 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
229. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=20].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
230. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 제 2 채굴장
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=21].title
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
231. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=21].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
232. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 제 3 채굴장
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=22].title
   (powtórzenie elementu 89 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=22].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
234. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 제 4 채굴장
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=30].title
   (powtórzenie elementu 90 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=30].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
236. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 폭약 적재소
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=31].title
   (powtórzenie elementu 91 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=31].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 대피소
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=40].title
   (powtórzenie elementu 93 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 게임의 승자가 되어 지하로 내려오는 데에는 성공했지만 로보토미 지부는 이미 카지노에서 점령한 듯 보였다. 끊임없이 곡괭이 질을 하는 노예들, 이를 감시하는 경호원들, 철장을 씹어대는 죄종들. 이 모든 걸 뚫고 내려가야 한다는 뜻일까.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=40].desc
   (powtórzenie elementu 227 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 지하 공장 출입구
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=50].title
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 그레고르의 기가 막힌 선동 연기로 인해 경호원들이 푼 죄종까지 상대해야 했다. 하지만 이 죄종들… 이제 보니 누군가의 명령에 따라서 싸우는 것이 아니라 그저 눈 앞에 놓인 상대는 가리지 않고 공격하는 모양이다. 그렇다면…
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=50].desc
   limit: do 320 znaków
   EN: Gregor’s breathtaking attempt at insurrection caused security to release the Peccatula. Taking a better look at these creatures, though… They don’t seem to be following any orders, instead opting to attack any human in sight. If that’s the case…
   PL: Porywająca przemowa wywrotowa Gregora sprawiła, że strażnicy wypuścili na nas także Peccatula. Przyjrzawszy się im bliżej, dostrzegłem jednak, że nie słuchają niczyich rozkazów i rzucają się na każdego bez wyjątku. A skoro tak…
242. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 1번 라인
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=110].title
   (powtórzenie elementu 96 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 우여곡절 끝에 다음 층으로 내려가는 데 성공했다. 눈에 보이는 건 형형 색색의 컨테이너 박스들. 아무도 지키지 않는 이곳에 쉽사리 발을 들여놓기 불길해지는 건 나만의 기분 탓일까?
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=110].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We managed to reach the next floor. Colorful containers awaited us in an unguarded space.\nThere’s no one here, so what’s with this ominous feeling we’re getting while entering?
   PL: Po wielu perypetiach dotarliśmy na niższe piętro, pełne różnobarwnych kontenerów.\nChoć nikt nie pilnuje tego miejsca, przed postawieniem kroku ogarnia mnie złe przeczucie.
244. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 2번 라인
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=111].title
   (powtórzenie elementu 97 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 우여곡절 끝에 다음 층으로 내려가는 데 성공했다. 눈에 보이는 건 형형색색의 컨테이너 박스들. 아무도 지키지 않는 이곳에 쉽사리 발을 들여놓기 불길해지는 건 나만의 기분 탓일까?
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=111].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We managed to reach the next floor. Colorful containers awaited us in an unguarded space.\nThere’s no one here, so what’s with this ominous feeling we’re getting while entering?
   PL: Po wielu perypetiach dotarliśmy na niższe piętro, pełne różnobarwnych kontenerów.\nChoć nikt nie pilnuje tego miejsca, przed postawieniem kroku ogarnia mnie złe przeczucie.
246. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 3번 라인
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=112].title
   (powtórzenie elementu 98 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 우여곡절 끝에 다음 층으로 내려가는 데 성공했다. 눈에 보이는 건 형형색색의 컨테이너 박스들. 아무도 지키지 않는 이곳에 쉽사리 발을 들여놓기 불길해지는 건 나만의 기분 탓일까?
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=112].desc
   (powtórzenie elementu 245 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
248. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 사출 성형실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=120].title
   limit: do 40 znaków
   EN: Molding Chamber
   PL: Hala Odlewnicza
249. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간을 물리치며 이곳을 헤쳐 나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=120].desc
   limit: do 120 znaków
   EN: We must defeat the ruthless cyborgs singing with jolly voices to make it through here.
   PL: Aby przebić się dalej, musimy pokonać bezwzględnych cyborgów nacierających z wesołą piosenką na ustach.
250. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 알록달록 자판기 방
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=121].title
   limit: do 40 znaków
   EN: Colorful Dispenser Stand
   PL: Pokój Kolorowych Automatów
251. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간을 물리치며 이곳을 헤쳐 나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=121].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
252. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 부품 조립실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=130].title
   limit: do 40 znaków
   EN: Assembly Line
   PL: Hala Montażu
253. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간을 물리치며 이곳을 헤쳐 나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=130].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
254. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 설비 정비소
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=140].title
   limit: do 40 znaków
   EN: Maintenance Point
   PL: Warsztat Konserwacji
255. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간을 물리치며 이곳을 헤쳐 나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=140].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
256. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 비상 발전소
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=151].title
   limit: do 40 znaków
   EN: Backup Generators
   PL: Zasilanie Awaryjne
257. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간을 물리치며 이곳을 헤쳐 나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=151].desc
   (powtórzenie elementu 249 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
258. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 신나는 룰렛 방
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=150].title
   limit: do 40 znaków
   EN: Riveting Roulette
   PL: Pokój Wesołej Ruletki
259. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=150].desc
   limit: do 120 znaków
   EN: We must defeat the ruthless cyborgs singing with jolly voices to make it through here.
   PL: Aby przebić się dalej, musimy pokonać bezwzględnych cyborgów nacierających z wesołą piosenką na ustach.
260. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 비상 발전소
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=10214].title
   (powtórzenie elementu 256 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
261. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=10214].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
262. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 안전 검사 시설
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=160].title
   (powtórzenie elementu 105 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
263. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=160].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
264. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 최종 가공실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=170].title
   (powtórzenie elementu 107 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=170].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
266. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 검증실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=161].title
   (powtórzenie elementu 109 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
267. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=161].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
268. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 폐기물 처리장
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=171].title
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
269. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=171].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
270. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 감시실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=180].title
   limit: do 40 znaków
   EN: Security Room
   PL: Dyżurka Straży
271. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=180].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
272. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 전진 기지
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=190].title
   (powtórzenie elementu 106 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 노래는 흥겹게, 그러나 살벌하게 덤비는 각종 강화 인간들을 물리치며 이곳을 헤쳐나가야 한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=190].desc
   (powtórzenie elementu 259 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 설원 갈림길
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=200].title
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=200].desc
   limit: do 140 znaków
   EN: Moving past the containers, we’re met with a chill air. The chunks of ice hint that we’re almost to the end.
   PL: Gdy minęliśmy piętro kontenerów, owiało nas lodowate powietrze. Wyrastające wokół bryły lodu zwiastują, że cel jest już blisko.
276. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 눈보라 지대
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=210].title
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
277. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=210].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 눈보라 지대
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=211].title
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=211].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 얼어붙은 폐허
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=220].title
   (powtórzenie elementu 111 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
281. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=220].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
282. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 파묻힌 은신처
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=221].title
   (powtórzenie elementu 114 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=221].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
284. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 눈보라 지대
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=230].title
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
285. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=230].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
286. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 눈보라 지대
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=231].title
   (powtórzenie elementu 113 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
287. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=231].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
288. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 파괴된 마을
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=240].title
   (powtórzenie elementu 112 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
289. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 컨테이너들이 있는 층을 지나 내려오니, 서늘한 공기가 우리를 맞이한다. 곳곳에 보이는 얼음들은 끝이 머지않았음을 암시한다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=240].desc
   (powtórzenie elementu 275 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
290. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 잠든 이웃들의 성
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=250].title
   limit: do 50 znaków
   EN: Ice Castle Where Neighbors Lie
   PL: Zamek Śpiących Sąsiadów
291. [Rozdziały, etapy i zdolności Dantego [10201] — opis] 얼음으로 둘러싸인 지대들을 지나 광산의 끝에 도달했다. 저 멀리 보이는 건 거대한 얼음성과… 예상치 못한 손님이 우리를 맞이해주고 있었다.
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=250].desc
   limit: do 190 znaków
   EN: We made it across the frozen landscape and reached the end of the mines. In the distance, I saw a massive castle of ice… and an unexpected guest.
   PL: Przemierzywszy skute lodem pustkowie, dotarliśmy na sam kraniec kopalni. W oddali majaczył olbrzymi lodowy zamek… oraz niespodziewany gość.
292. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 금고 보관실
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=0].title
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
293. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 공장 입구
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=100].title
   (powtórzenie elementu 95 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
294. [Rozdziały, etapy i zdolności Dantego [10201] — tytuł] 설원 갈림길
   źródło: DungeonNode1-2.json :: dataList[id=10201].stageList[id=200#2].title
   (powtórzenie elementu 110 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-3
- plik gry: `DungeonNode1-3.json`

295. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하실 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=10].title
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
296. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 이단 심문관들이 점령하고 있던 로보토미 지부는 이미 끔찍한 학살이 이뤄지고 있는 고문실이 되어 버렸다. 칼프 마을 주민들은 의체 시술을 받았다는 이유만으로, 무력하게 이 고통을 받아들이고 있을 뿐이었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=10].desc
   limit: do 240 znaków
   EN: The Inquisitors have transformed this branch facility into a torture chamber for prosthesis users, committing bloodcurdling murders. The townsfolk were powerless against such torment.
   PL: Zajęta przez Inkwizytorów filia Lobotomy Corp. zmieniła się w krwawą katownię. Mieszkańcy miasteczka Calw bezsilnie znosili katusze wyłącznie za to, że poddali się wszczepieniu protez.
297. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하실 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=11].title
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
298. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 지하실 입구에서 죽어가고 있는 소드를 만났다. 에피의 생사를 확인하는 절박한 질문에 누구도 사실을 이야기할 수 없었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=11].desc
   limit: do 160 znaków
   EN: We met a dying Saude next to the entrance. No one could truthfully answer her desperate question about Effie’s status.
   PL: Przy wejściu do podziemi natknęliśmy się na konającą Saude. Nikt nie miał serca odpowiedzieć zgodnie z prawdą na jej rozpaczliwe pytanie o los Effiego.
299. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하실 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=12].title
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
300. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 이단 심문관들이 점령하고 있던 로보토미 지부는 이미 끔찍한 학살이 이뤄지고 있는 고문실이 되어 버렸다. 칼프 마을 주민들은 의체 시술을 받았다는 이유만으로, 무력하게 이 고통을 받아들이고 있을 뿐이었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=12].desc
   (powtórzenie elementu 296 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
301. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 기계 장치 방
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=20].title
   limit: do 40 znaków
   EN: Machinery Room
   PL: Maszynownia
302. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 지하실 입구에서 죽어가고 있는 소드를 만났다. 에피의 생사를 확인하는 절박한 질문에 누구도 사실을 이야기할 수 없었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=20].desc
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
303. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 기계 장치 방
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=21].title
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
304. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 지하실 입구에서 죽어가고 있는 소드를 만났다. 에피의 생사를 확인하는 절박한 질문에 누구도 사실을 이야기할 수 없었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=21].desc
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
305. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 기계 장치 방
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=22].title
   (powtórzenie elementu 301 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
306. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 지하실 입구에서 죽어가고 있는 소드를 만났다. 에피의 생사를 확인하는 절박한 질문에 누구도 사실을 이야기할 수 없었다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=22].desc
   (powtórzenie elementu 298 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 격리 구역
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=30].title
   (powtórzenie elementu 123 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
308. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 수차례의 전투를 치렀음에도 귀도라는 자의 끔찍한 집념은 꺾여지지 않았다. 마침내 그가 더 이상 움직이지 않게 되자 소드를 남겨둔 채 우린 다음 지역으로 나아갔다. 모든 게 끔찍했고 엉망이었다. 누구도 말을 하지 않았다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=30].desc
   limit: do 300 znaków
   EN: Even after several battles, Guido still pursued us with a terrifying persistence. We stopped him at last, and leaving Saude behind, we proceeded to the next area. Everything was a terrible mess, and nobody had the energy for words.
   PL: Nawet po kilku starciach przerażająca zawziętość Guida nie słabła. Gdy wreszcie znieruchomiał, zostawiliśmy Saude i ruszyliśmy dalej. Wszystko wokół tonęło w koszmarze i nikt nie potrafił wydusić słowa.
309. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 제 1 관문
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=31].title
   (powtórzenie elementu 120 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
310. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 수차례의 전투를 치렀음에도 귀도라는 자의 끔찍한 집념은 꺾여지지 않았다. 마침내 그가 더 이상 움직이지 않게 되자 소드를 남겨둔 채 우린 다음 지역으로 나아갔다. 모든 게 끔찍했고 엉망이었다. 누구도 말을 하지 않았다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=31].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
311. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 폐쇄된 문
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=32].title
   (powtórzenie elementu 121 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
312. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=32].desc
   limit: do 170 znaków
   EN: I can hear the sound of something scuttling along the floor. I wonder what it might be, but part of me doesn’t want to find out.
   PL: Wciąż słychać, jak coś pełznie po posadzce. Część mnie chce poznać źródło tego dźwięku, a druga wolałaby nigdy się nie dowiedzieć.
313. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 잊혀진 통로
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=33].title
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
314. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 수차례의 전투를 치렀음에도 귀도라는 자의 끔찍한 집념은 꺾여지지 않았다. 마침내 그가 더 이상 움직이지 않게 되자 소드를 남겨둔 채 우린 다음 지역으로 나아갔다. 모든 게 끔찍했고 엉망이었다. 누구도 말을 하지 않았다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=33].desc
   (powtórzenie elementu 308 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
315. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 감옥 구역
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=40].title
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
316. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 침식된 심문관들과 전투를 치르며 우리는 황금가지가 있는 곳을 향해 계속해서 나아갔다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=40].desc
   limit: do 120 znaków
   EN: Fighting off corroded Inquisitors, we made our way for the Golden Bough.
   PL: Odpychając skorodowanych Inkwizytorów, parliśmy naprzód w stronę Złotej Gałęzi.
317. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 침식 개체 격리소
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=50].title
   (powtórzenie elementu 124 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
318. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=50].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
319. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 정예병 훈련소
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=51].title
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
320. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=51].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 감옥 구역
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=52].title
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
322. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 침식된 심문관들과 전투를 치르며 우리는 황금가지가 있는 곳을 향해 계속해서 나아갔다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=52].desc
   (powtórzenie elementu 316 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 옛 창고
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=53].title
   (powtórzenie elementu 127 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=53].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
325. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 고문실
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=60].title
   (powtórzenie elementu 130 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=60].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 예배실
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=61].title
   (powtórzenie elementu 129 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=61].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 봉쇄 구역
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=62].title
   (powtórzenie elementu 128 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 자꾸만 무언가 바닥을 기어 다니는 소리가 들려온다. 정체를 알고 싶은 마음과 한편으로는 알지 않아도 좋을 것 같은 기분이다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=62].desc
   (powtórzenie elementu 312 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하 예배당 복도
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=101].title
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
332. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=101].desc
   limit: do 230 znaków
   EN: We reached the next floor. All around us were torture devices, bits of flesh, gore, and dying townsfolk succumbing to pain. The least bearable of all is the periodic whistling.
   PL: Dotarliśmy na kolejne piętro. Wszędzie wokół poniewierały się narzędzia tortur, strzępy ciał i konający z bólu mieszkańcy Calw. Najtrudniej było jednak znieść rozbrzmiewające co jakiś czas gwizdanie.
333. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하 예배당 복도
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=102].title
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
334. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=102].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
335. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 폐쇄된 기도실
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=110].title
   limit: do 40 znaków
   EN: Closed Prayer Room
   PL: Zamknięta Rozmównica Modlitewna
336. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=110].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하 예배당 복도
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=111].title
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=111].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 폐쇄된 기도실
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=120].title
   (powtórzenie elementu 335 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=120].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 비명이 들리는 방
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=121].title
   limit: do 40 znaków
   EN: Room of Echoing Screams
   PL: Komnata Krzyków
342. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=121].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
343. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 제 2 관문
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=130].title
   (powtórzenie elementu 134 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
344. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=130].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 짓무름의 방
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=140].title
   limit: do 40 znaków
   EN: Chamber of Suppuration
   PL: Komnata Jątrzenia
346. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=140].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 예배당 내부
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=150].title
   limit: do 40 znaków
   EN: Church Interior
   PL: Wnętrze Kaplicy
348. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=150].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
349. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 예배당 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=151].title
   (powtórzenie elementu 138 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
350. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=151].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
351. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 묵상의 다리
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=152].title
   limit: do 40 znaków
   EN: Meditator’s Bridge
   PL: Most Kontemplacji
352. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=152].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
353. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 눈물의 제단
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=152#2].title
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
354. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=152#2].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
355. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 눈물의 제단
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=160].title
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
356. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=160].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
357. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 성물함
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=161].title
   (powtórzenie elementu 141 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
358. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=161].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
359. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 중앙 구역
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=162].title
   (powtórzenie elementu 142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=162].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 제단 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=163].title
   (powtórzenie elementu 140 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=163].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
363. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 속죄의 제단
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=164].title
   (powtórzenie elementu 143 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
364. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=164].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
365. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 정화소
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=170].title
   (powtórzenie elementu 144 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
366. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=170].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
367. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 예배당 내부
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=180].title
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
368. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=180].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
369. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 제 3 관문
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=181].title
   (powtórzenie elementu 145 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
370. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=181].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
371. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 예배당 내부
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=182].title
   (powtórzenie elementu 347 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
372. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=182].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 자격 판별대
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=190].title
   (powtórzenie elementu 146 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
374. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=190].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 성소로 가는 길
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=1100].title
   (powtórzenie elementu 147 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 우리는 다음 층에 도달했다. 곳곳에 심문관들이 만들어 놓은 고문 기구와 살점들, 고통에 못 이겨 목숨이 꺼져가는 칼프 마을 주민들이 보였다. 제일 견디기 힘들었던 건 중간 중간에 들리는 누군가의 휘파람 소리다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=1100].desc
   (powtórzenie elementu 332 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
377. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=210].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
378. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 이미 황금가지로 인해 영향을 받은 이 공간은 끝없는 시체들의 언덕이 되었다. 누군가를 향해 경배를 올리는 심문관들이 보인다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=210].desc
   limit: do 200 znaków
   EN: The area has transformed into endless hills of corpses thanks to the Golden Bough’s influence. Inquisitors in the midst of prayer to somebody can be seen.
   PL: Pod wpływem Złotej Gałęzi przestrzeń ta zmieniła się w bezkresne wzgórze trupów. Widać Inkwizytorów pogrążonych w modłach ku czyjejś czci.
379. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=220].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
380. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=220].desc
   limit: do 210 znaków
   EN: Hearing bells that may be familiar to some and new to others, we peek into Sinclair’s past. He sits in the middle of a lively classroom full of chatty students.
   PL: Wśród bicia dzwonów — dla jednych znajomego, dla innych obcego — zaglądamy w przeszłość Sinclaira. Chłopak siedzi pośrodku gwarnej klasy pełnej rozgadanych uczniów.
381. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=230].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
382. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=230].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
383. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=240].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=240].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=250].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=250].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=260].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
388. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=260].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
389. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=270].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
390. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 누군가에게는 한없이 익숙하고 누군가에겐 낯선 종소리를 들으면서 우리는 싱클레어의 과거를 본다. 떠들썩한 교실, 재잘거리는 학생들, 그 가운데에 싱클레어가 앉아 있다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=270].desc
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
391. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=280].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
392. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 마치 재해처럼 망가져 버린 싱클레어의 끔찍한 시절은 종결을 맞이한다. 오직 크로머 만이 이 모든 것이 만족스러워서 견딜 수 없다는 듯 웃는다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=280].desc
   limit: do 220 znaków
   EN: Flashbacks to a ruin that ravaged Sinclair’s life in a storm come to an end. Kromer is the only one with feelings to show, and hers is an uncontainable satisfaction.
   PL: Wspomnienia burzy, która obróciła życie Sinclaira w ruinę, dobiegają końca. Tylko Kromer otwarcie okazuje uczucia — niepohamowaną satysfakcję.
393. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=290].title
   (powtórzenie elementu 148 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 마치 재해처럼 망가져 버린 싱클레어의 끔찍한 시절은 종결을 맞이한다. 오직 크로머 만이 이 모든 것이 만족스러워서 견딜 수 없다는 듯 웃는다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=290].desc
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 시체들의 언덕
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=2100].title
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
396. [Rozdziały, etapy i zdolności Dantego [10301] — opis] 마치 재해처럼 망가져 버린 싱클레어의 끔찍한 시절은 종결을 맞이한다. 오직 크로머 만이 이 모든 것이 만족스러워서 견딜 수 없다는 듯 웃는다.
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=2100].desc
   (powtórzenie elementu 392 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하실 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=0].title
   (powtórzenie elementu 118 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
398. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 지하 예배당 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=100].title
   limit: do 40 znaków
   EN: Underground Church Entrance
   PL: Wejście do Podziemnej Kaplicy
399. [Rozdziały, etapy i zdolności Dantego [10301] — tytuł] 의식의 광장 입구
   źródło: DungeonNode1-3.json :: dataList[id=10301].stageList[id=200].title
   limit: do 40 znaków
   EN: Ritual Square Entrance
   PL: Wejście na Plac Rytualny

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-4
- plik gry: `DungeonNode1-4.json`

400. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10401].title
   limit: do 60 znaków
   EN: Blossoming League of Nine Littérateurs
   PL: Rozkwitający Krąg Dziewięciu
401. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10401].desc
   limit: do 440 znaków
   EN: We've entered the space of scattering yellow petals where the Golden Bough is resonating. It was the only place where Yi Sang may breathe as he put it. The Sinners are tasked with acting their parts of the script they're given, based on the place they're in. We're then greeted by Dongbaek from the past, accompanying a stunning fireworks display.
   PL: Wkroczyliśmy w przestrzeń wirujących żółtych płatków, gdzie rozbrzmiewa rezonans Złotej Gałęzi — jedyne miejsce, w którym Yi Sang, jak sam mawiał, mógł swobodnie oddychać. Grzesznicy muszą odgrywać role według rozdanych scenariuszy. Wśród pokazu fajerwerków powitała nas Dongbaek z przeszłości.
402. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10402].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10402].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
404. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10403].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
405. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10403].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
406. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10404].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
407. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10404].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10405].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
409. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10405].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
410. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10406].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10406].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
412. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10407].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
413. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 황금가지가 공명하는 곳, 흩날리고 있는 노란색 꽃잎들의 공간으로 들어갔다. 그곳은 이상의 '유일하게 숨을 쉴 수 있는 곳'이었다. 수감자들은 각자 놓여있는 극본을 낭독하며 공간에 맞는 연기를 해내야 한다. 그리고 과거 속 동백이 나타났다. 화려한 불꽃놀이와 함께.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10407].desc
   (powtórzenie elementu 401 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
414. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10408].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 수감자들은 각자 주어진 역할을 어색하지만 최선을 다해 수행 중이다. 꽃이 피고 새가 지저귀는 소리가 들렸던 구인회는, 비록 빛깔은 잃었어도 웃음과 다정함이 넘쳐있었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10408].desc
   limit: do 270 znaków
   EN: The Sinners are doing their best to play their roles, as awkward as it may be. Visited by sights of flowers and chirps of birds, the League of Nine was filled with joy and warmth even if it had become colorless.
   PL: Choć nieporadnie, Grzesznicy ze wszystkich sił odgrywają powierzone im role. Wypełniony kwiatami i świergotem ptaków Krąg Dziewięciu — choć pozbawiony barw — tętnił śmiechem i ciepłem.
416. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10409].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
417. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 수감자들은 각자 주어진 역할을 어색하지만 최선을 다해 수행 중이다. 꽃이 피고 새가 지저귀는 소리가 들렸던 구인회는, 비록 빛깔은 잃었어도 웃음과 다정함이 넘쳐있었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10409].desc
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10410].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
419. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 수감자들은 각자 주어진 역할을 어색하지만 최선을 다해 수행 중이다. 꽃이 피고 새가 지저귀는 소리가 들렸던 구인회는, 비록 빛깔은 잃었어도 웃음과 다정함이 넘쳐있었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10410].desc
   (powtórzenie elementu 415 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10411].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 영지는 구인회 일원들에게 자신이 만든 기술, 유리창을 보여주었다. 누군가는 감탄했고 누군가는 염려를 표했다. 화기애애했던 구인회에 조금씩 변화의 그림자가 다가오고 있었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10411].desc
   limit: do 250 znaków
   EN: Young-ji demonstrated the glass window, his new invention, to his fellow members. Some were astonished, while some showed concern. Shades of change were slowly beginning to cast over the League.
   PL: Young-ji zademonstrował towarzyszom swój nowy wynalazek — szklane okno. Jedni patrzyli z podziwem, inni z niepokojem. Nad serdecznym dotąd Kręgiem powoli kładł się cień zmian.
422. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10412].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 영지는 구인회 일원들에게 자신이 만든 기술, 유리창을 보여주었다. 누군가는 감탄했고 누군가는 염려를 표했다. 화기애애했던 구인회에 조금씩 변화의 그림자가 다가오고 있었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10412].desc
   (powtórzenie elementu 421 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10413].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
425. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구인회 시절의 이상은 영지의 유리창을 자신만의 방식으로 재구성한 기술을 발명했다. 그 기술 속에서 이상은 자신의 왼손잡이를 만나게 된다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10413].desc
   limit: do 190 znaków
   EN: During his time in the League, Yi Sang invented his reconstruction of Young-ji's glass window. In the invention, he meets his left-handed self.
   PL: W czasach Kręgu Dziewięciu Yi Sang przebudował szklane okno Young-jiego na własną modłę. W swoim wynalazku spotyka leworęcznego samego siebie.
426. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10414].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구인회 시절의 이상은 영지의 유리창을 자신만의 방식으로 재구성한 기술을 발명했다. 그 기술 속에서 이상은 자신의 왼손잡이를 만나게 된다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10414].desc
   (powtórzenie elementu 425 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10415].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
429. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 이번에는 구인회 속 이야기가 아닌 아주 머나먼 어딘가의 이야기가 등장한다. 고요하기 그지없는 외곽 어딘가에서 이름 모를 소년의 이야기가 밤하늘 속 별빛을 수놓듯이 펼쳐진다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10415].desc
   limit: do 220 znaków
   EN: This time, we see a story that takes place somewhere far away. In a quiet corner of the Outskirts, stories of an unknown boy unfolds like stars lighting the night sky.
   PL: Tym razem ukazuje nam się opowieść z bardzo dalekich stron. W cichym zakątku Peryferii historia bezimiennego chłopca rozwija się niczym gwiazdy rozświetlające nocne niebo.
430. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10416].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
431. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 이번에는 구인회 속 이야기가 아닌 아주 머나먼 어딘가의 이야기가 등장한다. 고요하기 그지없는 외곽 어딘가에서 이름 모를 소년의 이야기가 밤하늘 속 별빛을 수놓듯이 펼쳐진다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10416].desc
   (powtórzenie elementu 429 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
432. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10417].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
433. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 공간이 바뀌고, 수감자들은 T사 거리를 내려다보고 있다. 거리 속에는 구부정한 걸음걸이의 색을 잃은 사람들이 걸어 다닌다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10417].desc
   limit: do 180 znaków
   EN: The place changes once more, and the Sinners are looking out at streets of T Corp's district. People deviod of color stoop on the roads.
   PL: Sceneria zmienia się ponownie i Grzesznicy spoglądają z góry na ulice Dystryktu T Corp., którymi przemykają przygarbieni, pozbawieni barw ludzie.
434. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10418].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
435. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 공간이 바뀌고, 수감자들은 T사 거리를 내려다보고 있다. 거리 속에는 구부정한 걸음걸이의 색을 잃은 사람들이 걸어 다닌다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10418].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
436. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 꽃이 피던 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10419].title
   (powtórzenie elementu 400 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
437. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 공간이 바뀌고, 수감자들은 T사 거리를 내려다보고 있다. 거리 속에는 구부정한 걸음걸이의 색을 잃은 사람들이 걸어 다닌다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10419].desc
   (powtórzenie elementu 433 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
438. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10421].title
   limit: do 50 znaków
   EN: Rowdy League of Nine Littérateurs
   PL: Gwarny Krąg Dziewięciu
439. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 어느덧 꽃은 지고 구인회는 소란스러워져 간다. 그저 소음에 불과할지 혹은 변화의 한 걸음일지 그 당시엔 아무도 몰랐다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10421].desc
   limit: do 190 znaków
   EN: Flowers fall as time passes, and the League of Nine grows noisy. At the time, no one knew whether this was simple noise or a step toward change.
   PL: Kwiaty opadają wraz z upływem czasu, a w Kręgu Dziewięciu robi się głośno. Nikt wówczas nie wiedział, czy to zwykły zgiełk, czy pierwszy krok ku nieuchronnej zmianie.
440. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10422].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 어느덧 꽃은 지고 구인회는 소란스러워져 간다. 그저 소음에 불과할지 혹은 변화의 한 걸음일지 그 당시엔 아무도 몰랐다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10422].desc
   (powtórzenie elementu 439 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
442. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10423].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
443. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 기술에도 가치가 매겨지기 시작하고 구인회에도 아주 미세한 균열의 소리가 들려온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10423].desc
   limit: do 140 znaków
   EN: As technology starts to be appraised for their worth, tiny cracks are heard being made amidst the League.
   PL: Gdy wynalazki zaczęto wyceniać w pieniądzu, wewnątrz Kręgu rozległ się cichy trzask pierwszych pęknięć.
444. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10424].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
445. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 기술에도 가치가 매겨지기 시작하고 구인회에도 아주 미세한 균열의 소리가 들려온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10424].desc
   (powtórzenie elementu 443 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10425].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 모든 이야기가 다 행복하기만 하다면 더할 나위 없이 좋았을 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10425].desc
   limit: do 120 znaków
   EN: How nice it would have been if all stories told happy tales.
   PL: Jakże byłoby pięknie, gdyby wszystkie opowieści miały szczęśliwe zakończenie.
448. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10426].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
449. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 모든 이야기가 다 행복하기만 하다면 더할 나위 없이 좋았을 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10426].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
450. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10427].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
451. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 모든 이야기가 다 행복하기만 하다면 더할 나위 없이 좋았을 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10427].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10428].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
453. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 모든 이야기가 다 행복하기만 하다면 더할 나위 없이 좋았을 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10428].desc
   (powtórzenie elementu 447 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
454. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10429].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구인회 사무실 한복판에 이질적인 물건이 놓여있다. 구인회가 만들어진 목적에 대해 회고하며 각자의 마음이 어긋나기 시작한다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10429].desc
   limit: do 200 znaków
   EN: An outlandish item is placed at the center of the League's office. Looking back on the group's original purpose, the members' thoughts begin to clash.
   PL: Na środku siedziby Kręgu spoczywa obcy temu miejscu przedmiot. Wspominając pierwotny cel zgromadzenia, jego członkowie zaczynają oddalać się od siebie.
456. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10430].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
457. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 낯선 소리들이 구인회를 채우기 시작한다. 아홉은 더 이상 아홉이 아니게 되며 죄가 아니라고 여겼던 것들이 죄가 되어 돌아온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10430].desc
   limit: do 170 znaków
   EN: Unfamiliar sounds occupy the League. The nine ceased to be nine, and things that weren't thought to be crimes turn into accusations.
   PL: Krąg wypełniają obce dźwięki. Dziewięcioro przestaje być dziewięciorgiem, a to, co dotąd nie uchodziło za przewinę, powraca jako oskarżenie.
458. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10431].title
   limit: do 60 znaków
   EN: Withering League of Nine Littérateurs
   PL: Więdnący Krąg Dziewięciu
459. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 낯선 소리들이 구인회를 채우기 시작한다. 아홉은 더 이상 아홉이 아니게 되며 죄가 아니라고 여겼던 것들이 죄가 되어 돌아온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10431].desc
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
460. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10432].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 낯선 소리들이 구인회를 채우기 시작한다. 아홉은 더 이상 아홉이 아니게 되며 죄가 아니라고 여겼던 것들이 죄가 되어 돌아온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10432].desc
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10433].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
463. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 낯선 소리들이 구인회를 채우기 시작한다. 아홉은 더 이상 아홉이 아니게 되며 죄가 아니라고 여겼던 것들이 죄가 되어 돌아온다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10433].desc
   (powtórzenie elementu 457 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
464. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10434].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
465. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 저마다 지키고 싶었던 것이 무엇인지 알지 못한 채, 구인회는 갑작스러운 방문을 받게 된다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10434].desc
   limit: do 130 znaków
   EN: While the members are unsure of what they wanted to protect, the League sees an unexpected visitor.
   PL: Zanim członkowie Kręgu zdołali pojąć, co tak naprawdę chcieli ocalić, składają im wizytę niespodziewani goście.
466. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10435].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
467. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 저마다 지키고 싶었던 것이 무엇인지 알지 못한 채, 구인회는 갑작스러운 방문을 받게 된다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10435].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
468. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10436].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
469. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 어떠한 색도 없이 불타오르는 구인회와 함께 모든 것이 사라졌다. 산산조각 속에서 이상이 택한 것은 정지, 즉 무관심이었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10436].desc
   limit: do 190 znaków
   EN: The League of Nine Littérateurs was consumed in a colorless fire. In the shattering, Yi Sang chose to stop; in other words, he chose indifference.
   PL: Krąg Dziewięciu spłonął w bezbarwnym ogniu, a wraz z nim przepadło wszystko. Pośród zgliszcz Yi Sang wybrał bezruch — inaczej mówiąc, obojętność.
470. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10437].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 어떠한 색도 없이 불타오르는 구인회와 함께 모든 것이 사라졌다. 산산조각 속에서 이상이 택한 것은 정지, 즉 무관심이었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10437].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
472. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10438].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
473. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 세월이 지나 스테파네트는 노쇠해갔고, K사는 새로운 변화를 맞게 된다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10438].desc
   limit: do 120 znaków
   EN: As time passed, Stephanette grew old, and K Corp. faces a new change.
   PL: Z biegiem lat Stephanette zestarzała się, a K Corp. stanęła u progu nowej przemiany.
474. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10440].title
   limit: do 40 znaków
   EN: N Corp. Cubic Room
   PL: Kwadratowy Pokój N Corp.
475. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구보의 손에 이끌려 이상이 온 곳은 사방이 하얀색으로 칠해진 방이었다. 그곳에서 이상은 긴 침묵으로 거울과 함께 세월을 덮었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10440].desc
   limit: do 180 znaków
   EN: Taken by Gubo, Yi Sang was brought to a room entirely painted in white. He covered the time with a long silence, accompanied by the mirror.
   PL: Prowadzony za rękę przez Gubo, Yi Sang trafił do pokoju pomalowanego ze wszystkich stron na biało. Tam, w towarzystwie lustra, przykrył upływające lata długim milczeniem.
476. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10441].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구보의 손에 이끌려 이상이 온 곳은 사방이 하얀색으로 칠해진 방이었다. 그곳에서 이상은 긴 침묵으로 거울과 함께 세월을 덮었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10441].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10442].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 구보의 손에 이끌려 이상이 온 곳은 사방이 하얀색으로 칠해진 방이었다. 그곳에서 이상은 긴 침묵으로 거울과 함께 세월을 덮었다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10442].desc
   (powtórzenie elementu 475 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10443].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 그곳에서 유일한 방문자는 헤르만과 구보뿐이었다. 구보는 계속해서 새로운 구인회의 가입을 독려한다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10443].desc
   limit: do 150 znaków
   EN: The only visitors to the room were Hermann and Gubo. Gubo keeps recommending him to join the new League of Nine.
   PL: Jedynymi gośćmi w tym pokoju byli Hermann oraz Gubo, który nieustannie namawiał go do wstąpienia do nowego Kręgu Dziewięciu.
482. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10444].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
483. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 그곳에서 유일한 방문자는 헤르만과 구보뿐이었다. 구보는 계속해서 새로운 구인회의 가입을 독려한다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10444].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
484. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10445].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
485. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 그곳에서 유일한 방문자는 헤르만과 구보뿐이었다. 구보는 계속해서 새로운 구인회의 가입을 독려한다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10445].desc
   (powtórzenie elementu 481 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
486. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10446].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
487. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 상이는 어느 순간부터 이해되지 않는 말을 하기 시작하며 이상에게 두 가지 선택지에 관해 이야기 해준다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10446].desc
   limit: do 130 znaków
   EN: At some point, Sang Yi started saying strange things, and talks to Yi Sang about two options.
   PL: W pewnym momencie Sang Yi zaczął wypowiadać niezrozumiałe słowa i przedstawił Yi Sangowi dwie drogi wyboru.
488. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10447].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
489. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 상이는 어느 순간부터 이해되지 않는 말을 하기 시작하며 이상에게 두 가지 선택지에 관해 이야기 해준다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10447].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
490. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10448].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 상이는 어느 순간부터 이해되지 않는 말을 하기 시작하며 이상에게 두 가지 선택지에 관해 이야기 해준다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10448].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
492. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10449].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 상이는 어느 순간부터 이해되지 않는 말을 하기 시작하며 이상에게 두 가지 선택지에 관해 이야기 해준다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10449].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
494. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10450].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
495. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 상이는 어느 순간부터 이해되지 않는 말을 하기 시작하며 이상에게 두 가지 선택지에 관해 이야기 해준다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10450].desc
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] N사 사각형의 방
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10451].title
   (powtórzenie elementu 474 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
497. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 사각형을 나선 이상은 비틀거리며 어딘가로 향해간다. 그리고 이제 동랑의 차례가 왔다. 과거의 그는 K사로 넘어가 자신의 기술을 건넬 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10451].desc
   limit: do 250 znaków
   EN: Leaving the room of squares, Yi Sang takes staggering steps to somewhere. And now, Dongrang's turn has come. At this point in the past, he'd leave for K Corp. and give the Wing his technology.
   PL: Opuściwszy kwadratowy pokój, Yi Sang rusza chwiejnym krokiem przed siebie. Teraz nadeszła kolej na Dongranga — w tym punkcie przeszłości odejdzie do K Corp., by oddać Skrzydłu swoją technologię.
498. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] K사 어딘가의 실험실
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10452].title
   limit: do 40 znaków
   EN: K Corp. Laboratory
   PL: Laboratorium K Corp.
499. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 사각형을 나선 이상은 비틀거리며 어딘가로 향해간다. 그리고 이제 동랑의 차례가 왔다. 과거의 그는 K사로 넘어가 자신의 기술을 건넬 것이다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10452].desc
   (powtórzenie elementu 497 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
500. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] K사 어딘가의 실험실
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10453].title
   (powtórzenie elementu 498 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
501. [Rozdziały, etapy i zdolności Dantego [10401] — opis] 뒤틀린 동랑은 치명상을 입은 채 죽어가고 있다. 이대로 정말 끝일까. 동랑의 눈이 평화로웠던 어딘가의 들판을 향하듯 고요해진다.
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10453].desc
   limit: do 210 znaków
   EN: Fatally wounded, Dongrang is nearing his death in this distorted form. Could this be it? His eyes grow calm, as if looking at a once peaceful field in his memories.
   PL: Śmiertelnie ranny, wypaczony Dongrang zbliża się ku końcowi. Czy to już naprawdę kres? Jego oczy cichną, jakby spoglądały na spokojną niegdyś łąkę ze wspomnień.
502. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 소란스러워지는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10420].title
   (powtórzenie elementu 438 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
503. [Rozdziały, etapy i zdolności Dantego [10401] — tytuł] 시들어가는 구인회
   źródło: DungeonNode1-4.json :: dataList[id=10401].stageList[id=10439].title
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-5
- plik gry: `DungeonNode1-5.json`

504. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 기다란 강
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10502].title
   limit: do 40 znaków
   EN: A Long River
   PL: Długa Rzeka
505. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 눈을 뜨자마자 제일 거슬린 건 이곳의 감촉이었다. 이전에 이스마엘이 우리에게 제시했던 계획을 찬찬히 되돌아본다. 이곳은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10502].desc
   limit: do 190 znaków
   EN: The first thing I noticed upon waking up was the unpleasant sensation of this place. I tried to recall what Ishmael's plan was. This place is...
   PL: Gdy tylko otworzyłem oczy, uderzyła mnie obrzydliwa faktura tego miejsca. Próbowałem odtworzyć w pamięci plan Ishmael. Jesteśmy…
506. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 기다란 강 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10503].title
   limit: do 40 znaków
   EN: A Long River 2
   PL: Długa Rzeka 2
507. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 우리는 창백한 고래가 삼킨 황금가지를 찾기 위해 그것의 뱃속으로 들어왔다. 다행히 열두 수감자 모두 작전대로 잘 내려온 것 같았지만… 보트가 보이지 않는다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10503].desc
   limit: do 220 znaków
   EN: We voluntarily entered the Pallid Whale's maws in search of the Golden Bough. Luckily, all twelve Sinners made it down here without getting lost... But where's our boat?
   PL: W poszukiwaniu połkniętej Złotej Gałęzi z własnej woli wpłynęliśmy do paszczy Bladego Wieloryba. Cała dwunastka Grzeszników dotarła na dół zgodnie z planem… tylko gdzie podziała się nasza łódź?
508. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 기다란 강 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10504].title
   limit: do 40 znaków
   EN: A Long River 3
   PL: Długa Rzeka 3
509. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 우리는 창백한 고래가 삼킨 황금가지를 찾기 위해 그것의 뱃속으로 들어왔다. 다행히 열두 수감자 모두 작전대로 잘 내려온 것 같았지만… 보트가 보이지 않는다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10504].desc
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 고래 위장
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10505].title
   (powtórzenie elementu 43 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 쏟아지는 위산을 피해 있는 힘을 다해 도망쳤다. 그리고 어디선가 우리에게 말을 거는 이들이 있었다. 인어일까?
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10505].desc
   limit: do 210 znaków
   EN: The Whale's stomach acid began to rain—we had no choice but to run away to the best of our abilities. That's when we suddenly heard voices talking to us. Mermaids?
   PL: Uciekając ile sił w nogach przed ulewą kwasu żołądkowego, usłyszeliśmy nagle czyjeś głosy. Syreny?
512. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 고래 위장 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10506].title
   limit: do 40 znaków
   EN: Whale Guts 2
   PL: Żołądek Wieloryba 2
513. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 쏟아지는 위산을 피해 있는 힘을 다해 도망쳤다. 그리고 어디선가 우리에게 말을 거는 이들이 있었다. 인어일까?
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10506].desc
   (powtórzenie elementu 511 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
514. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 피쿼드타운
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10507].title
   (powtórzenie elementu 44 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 그들은 몸의 일부가 하얗게 덮여 있었지만 인어가 아니었다. 여전히 정체를 알 수 없는 채로 우리는 그들이 안내하는 길을 따라갔다. 유일하게 이스마엘이 걸음을 멈추며 의미심장하게 이들 중 하나를 바라본다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10507].desc
   limit: do 230 znaków
   EN: Their bodies were partially Pallidified, but they weren't Mermaids. These mysterious strangers began leading us somewhere. Only Ishmael stopped to look at one of them curiously.
   PL: Choć części ich ciał pokrywała biel, nie byli Syrenami. Nieznajomi poprowadzili nas przed siebie; jedynie Ishmael przystanęła, wpatrując się wymownie w jedną z postaci.
516. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 피쿼드타운 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10508].title
   limit: do 40 znaków
   EN: Pequod Town 2
   PL: Miasteczko Pequod 2
517. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 그들이 우리를 데려간 곳은 피쿼드타운 이라는 이름의 마을이었다. 그곳에서 이스마엘은 그토록 살아있길 바라고 원했던 얼굴을 보게 된다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10508].desc
   limit: do 160 znaków
   EN: The strangers led us to a village called 'Pequod Town'. There, Ishmael meets someone that she so dearly wished to see again.
   PL: Nieznajomi zaprowadzili nas do osady zwanej Miasteczkiem Pequod. Tam Ishmael ujrzała twarz kogoś, kogo tak żarliwie pragnęła znów zobaczyć żywym.
518. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 피쿼드타운 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10509].title
   limit: do 40 znaków
   EN: Pequod Town 3
   PL: Miasteczko Pequod 3
519. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 그들이 우리를 데려간 곳은 피쿼드타운 이라는 이름의 마을이었다. 그곳에서 이스마엘은 그토록 살아있길 바라고 원했던 얼굴을 보게 된다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10509].desc
   (powtórzenie elementu 517 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
520. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 선장실
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10510].title
   limit: do 40 znaków
   EN: Captain's Quarters
   PL: Kajuta Kapitańska
521. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘과 함께 항해를 했던 피쿼드호의 옛 선원들과 에이해브 선장을 만났다. 에이해브는 우리와 대화를 나누고 싶다고 했다. 여유롭고 자신만만한 미소와 함께.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10510].desc
   limit: do 160 znaków
   EN: We met the Pequod's Crew—Ishmael's old crew—and Captain Ahab. With a confident smile, Ahab invited us to her office to talk.
   PL: Spotkaliśmy dawnych załogantów Pequoda oraz kapitan Ahab. Z pewnym siebie uśmiechem Ahab zaprosiła nas na rozmowę.
522. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 선장실 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10511].title
   limit: do 40 znaków
   EN: Captain's Quarters 2
   PL: Kajuta Kapitańska 2
523. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브 선장은 지나칠 정도로 우리를 꿰뚫고 있었다. 수감자들 사이에서도 의견이 갈리며 조금씩 동요하고 있었다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10511].desc
   limit: do 160 znaków
   EN: Captain Ahab seemed to see right through us. Discord grew among the Sinners as agreement drew even further out of reach.
   PL: Kapitan Ahab zdawała się przejrzeć nas na wylot. Wśród Grzeszników narastał rozdźwięk i niepokój.
524. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 선장실 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10512].title
   limit: do 40 znaków
   EN: Captain's Quarters 3
   PL: Kajuta Kapitańska 3
525. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 이스마엘에게 받아들일 수밖에 없는 치명적인 제안을 내건다. 아마 나는 이스마엘이 그 제안을 승낙하지 않기를 바랐는지도 모른다. 그 외에 다른 적절한 해결책을 제시할 수도 없었으면서.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10512].desc
   limit: do 220 znaków
   EN: Ahab makes an offer to Ishmael that she could not refuse. Maybe... I was hoping that Ishmael wouldn't accept that offer. When I didn't even have a better alternative.
   PL: Ahab składa Ishmael zabójczą propozycję nie do odrzucenia. W głębi ducha pragnąłem chyba, by Ishmael jej nie przyjęła — choć sam nie potrafiłem wskazać innego wyjścia.
526. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 선장실 4
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10513].title
   limit: do 40 znaków
   EN: Captain's Quarters 4
   PL: Kajuta Kapitańska 4
527. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 이스마엘에게 받아들일 수밖에 없는 치명적인 제안을 내건다. 아마 나는 이스마엘이 그 제안을 승낙하지 않기를 바랐는지도 모른다. 그 외에 다른 적절한 해결책을 제시할 수도 없었으면서.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10513].desc
   (powtórzenie elementu 525 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
528. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 퀴케그
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10515].title
   limit: do 40 znaków
   EN: Queequeg
   PL: Queequeg
529. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 자신의 선원들과 함께 췌장을, 우리는 심장의 우심방을 지나 집결지에서 만나기로 했다. 퀴케그라는 자가 우리 항해의 운전수로 합류하였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10515].desc
   limit: do 320 znaków
   EN: Ahab would pass through the Whale's pancreas with her crew, while we would pass through its right heart atrium. Once we have completed our missions, we would rendezvous before the heart and proceed from there. Queequeg joined us as our helmswoman.
   PL: Ustaliliśmy, że Ahab ze swoją załogą przebije się przez trzustkę, a my przejdziemy przez prawy przedsionek, by spotkać się przed sercem. Jako sterniczka dołączyła do nas Queequeg.
530. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 퀴케그 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10516].title
   limit: do 40 znaków
   EN: Queequeg 2
   PL: Queequeg 2
531. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 자신의 선원들과 함께 췌장을, 우리는 심장의 우심방을 지나 집결지에서 만나기로 했다. 퀴케그라는 자가 우리 항해의 운전수로 합류하였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10516].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 퀴케그 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10517].title
   limit: do 40 znaków
   EN: Queequeg 3
   PL: Queequeg 3
533. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 자신의 선원들과 함께 췌장을, 우리는 심장의 우심방을 지나 집결지에서 만나기로 했다. 퀴케그라는 자가 우리 항해의 운전수로 합류하였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10517].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
534. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 퀴케그 4
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10518].title
   limit: do 40 znaków
   EN: Queequeg 4
   PL: Queequeg 4
535. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 자신의 선원들과 함께 췌장을, 우리는 심장의 우심방을 지나 집결지에서 만나기로 했다. 퀴케그라는 자가 우리 항해의 운전수로 합류하였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10518].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
536. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 퀴케그 5
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10519].title
   limit: do 40 znaków
   EN: Queequeg 5
   PL: Queequeg 5
537. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 자신의 선원들과 함께 췌장을, 우리는 심장의 우심방을 지나 집결지에서 만나기로 했다. 퀴케그라는 자가 우리 항해의 운전수로 합류하였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10519].desc
   (powtórzenie elementu 529 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
538. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심방
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10520].title
   (powtórzenie elementu 48 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘은 퀴케그라는 선원과 꽤 각별한 사이였는 듯 보였다. 그리고 내게는 또다시 이스마엘의 장면이 보인다. 그 장면 속에서 나는 누군가의 끔찍한 울음소리를 들었다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10520].desc
   limit: do 200 znaków
   EN: Looks like Ishmael shared a pretty close relationship with Queequeg. I'm seeing another vision of Ishmael... and from that vision, I hear a terrifying cry.
   PL: Wygląda na to, że Ishmael łączyła z Queequeg szczególna więź. Znów nawiedza mnie wizja z przeszłości Ishmael… a z jej głębi dobiega przeraźliwy płacz.
540. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심방 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10521].title
   limit: do 40 znaków
   EN: Right Heart Atrium 2
   PL: Prawy Przedsionek 2
541. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘은 퀴케그라는 선원과 꽤 각별한 사이였는 듯 보였다. 그리고 내게는 또다시 이스마엘의 장면이 보인다. 그 장면 속에서 나는 누군가의 끔찍한 울음소리를 들었다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10521].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
542. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심방 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10522].title
   limit: do 40 znaków
   EN: Right Heart Atrium 3
   PL: Prawy Przedsionek 3
543. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘은 퀴케그라는 선원과 꽤 각별한 사이였는 듯 보였다. 그리고 내게는 또다시 이스마엘의 장면이 보인다. 그 장면 속에서 나는 누군가의 끔찍한 울음소리를 들었다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10522].desc
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
544. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심실
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10523].title
   (powtórzenie elementu 49 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
545. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘이 마침내 원하는 걸 이룬다면, 그 후에 '앞으로'가 남아있을까? 나는 그저… 다같이 아이스크림을 먹으러 가고 싶었던 것 같다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10523].desc
   limit: do 180 znaków
   EN: ... What 'next' is there for Ishmael if she finally gets what she wants? I... I think I just wanted everyone to go get ice cream together.
   PL: Gdy Ishmael dopnie swego, czy zostanie jej jeszcze jakiekolwiek „potem”? Ja… chciałem chyba tylko pójść ze wszystkimi na lody.
546. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심실 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10524].title
   limit: do 40 znaków
   EN: Right Heart Ventricle 2
   PL: Prawa Komora 2
547. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘이 마침내 원하는 걸 이룬다면, 그 후에 '앞으로'가 남아있을까? 나는 그저… 다같이 아이스크림을 먹으러 가고 싶었던 것 같다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10524].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
548. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 우심실 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10525].title
   limit: do 40 znaków
   EN: Right Heart Ventricle 3
   PL: Prawa Komora 3
549. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 이스마엘이 마침내 원하는 걸 이룬다면, 그 후에 '앞으로'가 남아있을까? 나는 그저… 다같이 아이스크림을 먹으러 가고 싶었던 것 같다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10525].desc
   (powtórzenie elementu 545 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
550. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 힘줄 다리
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10526].title
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10526].desc
   limit: do 170 znaków
   EN: Ahab's crew and Ishmael shouted from the top of their lungs. Kill the Pallid Whale, and all shall be over. And now, Ishmael...
   PL: Załoga i Ishmael krzyczeli z całych płuc, że śmierć Bladego Wieloryba zakończy wszystko. A teraz Ishmael…
552. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 힘줄 다리 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10527].title
   limit: do 40 znaków
   EN: Sinew Bridge 2
   PL: Most ze Ścięgien 2
553. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10527].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 소리가 들려오는 곳
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10528].title
   (powtórzenie elementu 51 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
555. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10528].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
556. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 소리가 들려오는 곳 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10529].title
   limit: do 40 znaków
   EN: Thumping of the Heart 2
   PL: Echo Bicia Serca 2
557. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10529].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 소리가 들려오는 곳 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10530].title
   limit: do 40 znaków
   EN: Thumping of the Heart 3
   PL: Echo Bicia Serca 3
559. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10530].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 소리가 들려오는 곳 4
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10531].title
   limit: do 40 znaków
   EN: Thumping of the Heart 4
   PL: Echo Bicia Serca 4
561. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 선원들과 이스마엘은 목청껏 부르짖었다. 창백한 고래만 죽이면 모든 게 끝난다고. 그리고 지금 이스마엘은…
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10531].desc
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
562. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 앞 집결지
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10533].title
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 창백한 고래의 심장 소리가 들려온다. 이제 남은 건 눈앞에 움찔거리고 있는 환상체일 뿐.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10533].desc
   limit: do 150 znaków
   EN: I hear the Pallid Whale's beating heart. All that remains is taking out that twitching Abnormality before us.
   PL: Słychać łomot serca Bladego Wieloryba. Na drodze stoi nam już tylko drgająca przed nami Anomalia.
564. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 앞 집결지 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10534].title
   limit: do 50 znaków
   EN: Rendezvous Area Before the Heart 2
   PL: Miejsce Zbiórki przed Sercem 2
565. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 집결지에서 에이해브를 만났다. 하지만 뒤에 남은 선원들의 숫자는 현저히 적어 보인다. 그리고 에이해브가 지나왔던 길들과 죽어가는 선원들의 모습이 보였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10534].desc
   limit: do 290 znaków
   EN: We met Ahab at the rendezvous area. But the crew that accompanied her at the start of this journey had shrunk significantly in number. I see a vision of the path Ahab walked... and the corpses of her crew she left in her wake.
   PL: Na miejscu zbiórki spotkaliśmy Ahab, lecz garstka ocalałych za jej plecami wyraźnie stopniała. Ujrzałem wizję ścieżki, którą przeszła Ahab — usłanej ciałami jej własnych ludzi.
566. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 앞 집결지 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10535].title
   limit: do 50 znaków
   EN: Rendezvous Area Before the Heart 3
   PL: Miejsce Zbiórki przed Sercem 3
567. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 집결지에서 에이해브를 만났다. 하지만 뒤에 남은 선원들의 숫자는 현저히 적어 보인다. 그리고 에이해브가 지나왔던 길들과 죽어가는 선원들의 모습이 보였다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10535].desc
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 고래 심장
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10536].title
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
569. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 에이해브는 내 머리통에 있는 황금가지를 달라고 한다. 나는 죽으려 하지 않을 것이다. 그리고 드디어… 심장으로 가는 문이 열렸다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10536].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Ahab is asking for the Golden Bough in my clock. But I won't seek death willingly.\n... The gate to the heart opens.
   PL: Ahab żąda Złotej Gałęzi tkwiącej w mojej głowie. Nie zamierzam jednak dobrowolnie oddać życia.\n…Wrota prowadzące do serca stają otworem.
570. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 고래 심장 2
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10537].title
   limit: do 40 znaków
   EN: Heart of the Whale 2
   PL: Serce Wieloryba 2
571. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 창백한 고래의 심장이 고동치는 것이 보인다. 이스마엘과 에이해브의 세계가 서로 맞붙어 간다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10537].desc
   limit: do 120 znaków
   EN: I can see the beating heart of the Pallid Whale. Ishmael and Ahab's worlds collide.
   PL: Przed nami pulsuje serce Bladego Wieloryba. Światy Ishmael i Ahab zderzają się ze sobą.
572. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 고래 심장 3
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10538].title
   limit: do 40 znaków
   EN: Heart of the Whale 3
   PL: Serce Wieloryba 3
573. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 창백한 고래의 심장이 고동치는 것이 보인다. 이스마엘과 에이해브의 세계가 서로 맞붙어 간다.
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10538].desc
   (powtórzenie elementu 571 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
574. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 기다란 강
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10501].title
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 피쿼드타운 출구
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10514].title
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 심장 앞 집결지
   źródło: DungeonNode1-5.json :: dataList[id=10501].stageList[id=10532].title
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-7
- plik gry: `DungeonNode1-7.json`

577. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 빌려 쓴 이름
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10702].title
   limit: do 40 znaków
   EN: A Borrowed Name
   PL: Pożyczone Imię
578. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 비참한 실패
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10703].title
   limit: do 40 znaków
   EN: Abject Failure
   PL: Żałosna Klęska
579. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 비참한 실패
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10704].title
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 비참한 실패
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10705].title
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 비참한 실패
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10706].title
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 비참한 실패
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10707].title
   (powtórzenie elementu 578 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 깨어진 꿈속
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10708].title
   limit: do 40 znaków
   EN: Within Broken Dreams
   PL: Pośród Strzaskanych Marzeń
584. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 위대한 모험
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10709].title
   limit: do 40 znaków
   EN: The Great Adventure
   PL: Wielka Przygoda
585. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 위대한 모험
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10710].title
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 위대한 모험
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10711].title
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 위대한 모험
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10712].title
   (powtórzenie elementu 584 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
588. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 막간
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10713].title
   limit: do 40 znaków
   EN: Interlude
   PL: Antrakt
589. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 욕망을 버리지 못한 자들의 수용소
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10714].title
   limit: do 80 znaków
   EN: An Internment For Those Who Could Not Abandon Their Desire
   PL: Izolatorium Tych, Którzy Nie Porzucili Pragnienia
590. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 욕망을 버리지 못한 자들의 수용소
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10715].title
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 욕망을 버리지 못한 자들의 수용소
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10716].title
   (powtórzenie elementu 589 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 막간
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10717].title
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
593. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 사라진 후의 200년
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10718].title
   limit: do 50 znaków
   EN: 200 Years After the Departure
   PL: 200 Lat po Zniknięciu
594. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 사라진 후의 200년
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10719].title
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 사라진 후의 200년
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10720].title
   (powtórzenie elementu 593 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 막간
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10721].title
   (powtórzenie elementu 588 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 병자의 운명
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10722].title
   limit: do 40 znaków
   EN: The Fate of the Afflicted
   PL: Los Dotkniętych Chorobą
598. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 꿈이 끝나는
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10723].title
   limit: do 40 znaków
   EN: The Dream Ending
   PL: Koniec Snu
599. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 회전목마
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10724].title
   limit: do 40 znaków
   EN: The Carousel
   PL: Karuzela
600. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 끝나지 않는 꿈
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10725].title
   limit: do 40 znaków
   EN: The Dream Unending
   PL: Niekończący się Sen
601. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 꿈꾸는 라만차랜드
   źródło: DungeonNode1-7.json :: dataList[id=10701].stageList[id=10726].title
   limit: do 40 znaków
   EN: La Manchaland, the Dreamer
   PL: Śniący La Manchaland

## Rozdziały, etapy i zdolności Dantego: DungeonNode1-8
- plik gry: `DungeonNode1-8.json`

602. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 동전 세닢
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10802].title
   limit: do 40 znaków
   EN: Three Coins
   PL: Trzy Monety
603. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 임시동맹
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10803].title
   limit: do 40 znaków
   EN: Temporary Alliance
   PL: Tymczasowy Sojusz
604. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 준비실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10804].title
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
605. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 준비실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10805].title
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 준비실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10806].title
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 준비실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10807].title
   (powtórzenie elementu 55 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 어떤 소문
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10808].title
   limit: do 40 znaków
   EN: A Certain Rumor
   PL: Pewna Pogłoska
609. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 좁아지는 공간
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10809].title
   limit: do 40 znaków
   EN: Walls, Closing In
   PL: Ściany Coraz Bliżej
610. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 두번째 임시동맹
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10810].title
   limit: do 40 znaków
   EN: Second Temporary Alliance
   PL: Drugi Tymczasowy Sojusz
611. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 처치실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10811].title
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄인의 방
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10812].title
   limit: do 40 znaków
   EN: Chamber of the Condemned
   PL: Komnata Skazańca
613. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄인의 방
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10813].title
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
614. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10814].title
   limit: do 40 znaków
   EN: Ruined Laboratory
   PL: Zrujnowane Laboratorium
615. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10815].title
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
616. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10816].title
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
617. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10817].title
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10818].title
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 폐허가 된 실험실
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10819].title
   (powtórzenie elementu 614 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄인의 방
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10820].title
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄인의 방
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10821].title
   (powtórzenie elementu 612 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 쉼터
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10822].title
   limit: do 40 znaków
   EN: Rest Stop
   PL: Miejsce Odpoczynku
623. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 아무것도 남지 않은
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10823].title
   limit: do 40 znaków
   EN: Nothing Left
   PL: Nic Już Nie Zostało
624. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 아무것도 남지 않은
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10824].title
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
625. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 아무것도 남지 않은
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10825].title
   (powtórzenie elementu 623 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
626. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10826].title
   limit: do 40 znaków
   EN: Into the Earth of Sin
   PL: Pod Ziemię Grzechu
627. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10827].title
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10828].title
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
629. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10829].title
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10830].title
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 죄를 묻은 흙 밑으로
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10831].title
   (powtórzenie elementu 626 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 깎여 나간 마음의 산
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10832].title
   limit: do 40 znaków
   EN: Eroded Mountain of the Heart
   PL: Zeszlifowana Góra Serca
633. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 깎여 나간 마음의 산
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10833].title
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 깎여 나간 마음의 산
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10834].title
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 깎여 나간 마음의 산
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10835].title
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 깎여 나간 마음의 산
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10836].title
   (powtórzenie elementu 632 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 가라앉은 소망에서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10837].title
   limit: do 40 znaków
   EN: From the Sunken Hope
   PL: Z Zatopionej Nadziei
638. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 가라앉은 소망에서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10838].title
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
639. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 가라앉은 소망에서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10839].title
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
640. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 가라앉은 소망에서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10840].title
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 가라앉은 소망에서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10841].title
   (powtórzenie elementu 637 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
642. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 손끝에 머문 바람
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10842].title
   limit: do 50 znaków
   EN: Lingering Breeze at the Fingertips
   PL: Wiatr na Czubkach Palców
643. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 손끝에 머문 바람
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10843].title
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
644. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 손끝에 머문 바람
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10844].title
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
645. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 손끝에 머문 바람
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10845].title
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
646. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 우레와 같은 비명을
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10846].title
   limit: do 40 znaków
   EN: Thunderous Cry
   PL: Gromowy Krzyk
647. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 우레와 같은 비명을
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10847].title
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
648. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 우레와 같은 비명을
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10848].title
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
649. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 우레와 같은 비명을
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10849].title
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
650. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 우레와 같은 비명을
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10850].title
   (powtórzenie elementu 646 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 타오르는 욕망
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10851].title
   limit: do 40 znaków
   EN: Burning Desire
   PL: Płonące Pragnienie
652. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 타오르는 욕망
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10852].title
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
653. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 타오르는 욕망
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10853].title
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
654. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 타오르는 욕망
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10854].title
   (powtórzenie elementu 651 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
655. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 고인 채 썩어버린
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10855].title
   limit: do 40 znaków
   EN: Stagnant and Festering
   PL: Zastałe i Zgniłe
656. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 고인 채 썩어버린
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10856].title
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
657. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 고인 채 썩어버린
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10857].title
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 고인 채 썩어버린
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10858].title
   (powtórzenie elementu 655 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
659. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 하늘에 오를 자
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10859].title
   limit: do 60 znaków
   EN: One Destined for Heavenward Ascension
   PL: Ten, Który Wstąpi ku Niebiosom
660. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 하늘에 오를 자
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10860].title
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
661. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 하늘에 오를 자
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10861].title
   (powtórzenie elementu 659 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
662. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 빛을 따라서
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10862].title
   limit: do 40 znaków
   EN: Follow the Light
   PL: Za Światłem
663. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 그늘 아래 쉬어가는
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10863].title
   limit: do 40 znaków
   EN: Respite Under the Shades
   PL: Wytchnienie w Cieniu
664. [Rozdziały, etapy i zdolności Dantego [10801] — tytuł] 홍원에 가장 필요한 것
   źródło: DungeonNode1-8.json :: dataList[id=10801].stageList[id=10864].title
   limit: do 40 znaków
   EN: What Hongyuan Needs
   PL: Czego Najbardziej Potrzebuje Hongyuan

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-14
- plik gry: `DungeonNode91-14.json`

665. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911401].title
   limit: do 40 znaków
   EN: Hohenheim's Fathoms
   PL: Głębia Hohenheima
666. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911402].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
667. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911403].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911404].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
669. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911405].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
670. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911406].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911407].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
672. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911408].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
673. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911409].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911410].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911411].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
676. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911412].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
677. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911413].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
678. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911414].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
679. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911415].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
680. [Rozdziały, etapy i zdolności Dantego [911401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-14.json :: dataList[id=911401].stageList[id=911416].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-15
- plik gry: `DungeonNode91-15.json`

681. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911501].title
   limit: do 40 znaków
   EN: Bamboo-hatted Kim's Fathoms
   PL: Głębia Kima w Słomkowym Kapeluszu
682. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In the shimmering fathoms of ego,\nA painfully pale nightly trail unfolds before us.
   PL: W falującej głębi ego\nrozpościera się przed nami przejmująco błękitny nocny trakt.
683. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911502].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
684. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911502].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911503].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
686. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911503].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
687. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911504].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
688. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911504].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
689. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911505].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911505].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
691. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911506].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911506].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911507].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
694. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911507].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
695. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911508].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
696. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911508].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911509].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911509].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911510].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911510].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911511].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911511].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
703. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911512].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911512].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911513].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911513].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
707. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911514].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
708. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911514].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
709. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911515].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911515].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
711. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911516].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
712. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911516].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
713. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911517].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
714. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911517].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
715. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911518].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911518].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911519].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
718. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911519].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
719. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911520].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
720. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911520].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
721. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911521].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911521].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
723. [Rozdziały, etapy i zdolności Dantego [911501] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911522].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
724. [Rozdziały, etapy i zdolności Dantego [911501] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-15.json :: dataList[id=911501].stageList[id=911522].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-18
- plik gry: `DungeonNode91-18.json`

725. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911801].title
   limit: do 40 znaków
   EN: Time Ripper's Fathoms
   PL: Głębia Rozpruwacza Czasu
726. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911802].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
727. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911803].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
728. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911804].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
729. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911805].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
730. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911806].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
731. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911807].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
732. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911808].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
733. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911809].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
734. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911810].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
735. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911811].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
736. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911812].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
737. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911813].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
738. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911814].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
739. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911815].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
740. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911816].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
741. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911817].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
742. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911818].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
743. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911819].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
744. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911820].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
745. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911821].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
746. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911822].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
747. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911823].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
748. [Rozdziały, etapy i zdolności Dantego [911801] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-18.json :: dataList[id=911801].stageList[id=911824].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-20
- plik gry: `DungeonNode91-20.json`

749. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912001].title
   limit: do 40 znaków
   EN: Mayors's Fathoms
   PL: Głębia Mayors
750. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912002].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
751. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912003].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
752. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912004].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
753. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912005].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
754. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912006].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
755. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912007].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
756. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912008].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
757. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912009].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
758. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912010].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
759. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912011].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
760. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912012].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
761. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912013].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
762. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912014].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
763. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912015].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
764. [Rozdziały, etapy i zdolności Dantego [912014] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-20.json :: dataList[id=912014].stageList[id=912016].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-21
- plik gry: `DungeonNode91-21.json`

765. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912101].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
766. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912102].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
767. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912103].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
768. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912104].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
769. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912105].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
770. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912106].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
771. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912107].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
772. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912108].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
773. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912109].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
774. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912110].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
775. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912111].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
776. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912112].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
777. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912113].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
778. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912114].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
779. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912115].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
780. [Rozdziały, etapy i zdolności Dantego [912114] — tytuł] 메이어스의 심상
   źródło: DungeonNode91-21.json :: dataList[id=912114].stageList[id=912116].title
   (powtórzenie elementu 749 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-24
- plik gry: `DungeonNode91-24.json`

781. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912401].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
782. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912402].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
783. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912403].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
784. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912404].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
785. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912405].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
786. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912406].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
787. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912407].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
788. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912408].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
789. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912409].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
790. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912410].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
791. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912411].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
792. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912412].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
793. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912413].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
794. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912414].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
795. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912415].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
796. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912416].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
797. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912417].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
798. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912418].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
799. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912419].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
800. [Rozdziały, etapy i zdolności Dantego [912401] — tytuł] 호엔하임의 심상
   źródło: DungeonNode91-24.json :: dataList[id=912401].stageList[id=912420].title
   (powtórzenie elementu 665 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-27
- plik gry: `DungeonNode91-27.json`

801. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912701].title
   limit: do 40 znaków
   EN: ???'s Fathoms
   PL: Głębia ???
802. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912702].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
803. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912703].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
804. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912704].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
805. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912705].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
806. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912706].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
807. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912707].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
808. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912708].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
809. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912709].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
810. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912710].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
811. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912711].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
812. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912712].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
813. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912713].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
814. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912714].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
815. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912715].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
816. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912716].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
817. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912717].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
818. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912718].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
819. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912719].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
820. [Rozdziały, etapy i zdolności Dantego [912711] — tytuł] ???의 심상
   źródło: DungeonNode91-27.json :: dataList[id=912711].stageList[id=912720].title
   (powtórzenie elementu 801 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-3
- plik gry: `DungeonNode91-3.json`

821. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910301].title
   limit: do 40 znaków
   EN: Following a Crispy Scent
   PL: Śladem Chrupiącego Aromatu
822. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910301].desc
   limit: do 120 znaków
   EN: A waft of something crisp and well-roasted tickles the nose.
   PL: Skądś unosi się smakowity zapach chrupiącej pieczeni.
823. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910302].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
824. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910302].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
825. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910303].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
826. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910303].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
827. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910304].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
828. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910304].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
829. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910305].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
830. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910305].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
831. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910306].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
832. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910306].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
833. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910307].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
834. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910307].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
835. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910308].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
836. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910308].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
837. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910309].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
838. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910309].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
839. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910310].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
840. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910310].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
841. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910311].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
842. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910311].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
843. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910312].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
844. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910312].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
845. [Rozdziały, etapy i zdolności Dantego [910301] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910313].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
846. [Rozdziały, etapy i zdolności Dantego [910301] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910301].stageList[id=910313].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
847. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910301].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
848. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910301].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
849. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910302].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
850. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910302].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
851. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910303].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
852. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910303].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
853. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910304].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
854. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910304].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
855. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910305].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
856. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910305].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
857. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910306].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
858. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910306].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
859. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910307].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
860. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910307].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
861. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910308].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
862. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910308].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
863. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910309].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
864. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910309].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
865. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910310].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
866. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910310].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
867. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910311].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
868. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910311].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
869. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910312].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
870. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910312].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
871. [Rozdziały, etapy i zdolności Dantego [910302] — tytuł] 고소한 향을 따라서
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910313].title
   (powtórzenie elementu 821 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
872. [Rozdziały, etapy i zdolności Dantego [910302] — opis] 어디선가 바삭하고 고소한 향이 솔솔 올라온다.
   źródło: DungeonNode91-3.json :: dataList[id=910302].stageList[id=910313].desc
   (powtórzenie elementu 822 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-7
- plik gry: `DungeonNode91-7.json`

873. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910701].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
874. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910701].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
875. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910702].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
876. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910702].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
877. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910703].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
878. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910703].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
879. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910704].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
880. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910704].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
881. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910705].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
882. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910705].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
883. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910706].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
884. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910706].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
885. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910707].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
886. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910707].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
887. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910708].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
888. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910708].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
889. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910709].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
890. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910709].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
891. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910710].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
892. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910710].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
893. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910711].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
894. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910711].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
895. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910712].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
896. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910712].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
897. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910713].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
898. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910713].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
899. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910714].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
900. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910714].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
901. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910715].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
902. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910715].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
903. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910716].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
904. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910716].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
905. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910717].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
906. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910717].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
907. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910718].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
908. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910718].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
909. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910719].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
910. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910719].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
911. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910720].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
912. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910720].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
913. [Rozdziały, etapy i zdolności Dantego [910701] — tytuł] 김삿갓의 심상
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910721].title
   (powtórzenie elementu 681 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
914. [Rozdziały, etapy i zdolności Dantego [910701] — opis] 일렁이는 심상 속으로,\n시릴 정도로 푸른 밤의 거리가 보인다.
   źródło: DungeonNode91-7.json :: dataList[id=910701].stageList[id=910721].desc
   (powtórzenie elementu 682 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: DungeonNode91-9
- plik gry: `DungeonNode91-9.json`

915. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910901].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
916. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910902].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
917. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910903].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
918. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910904].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
919. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910905].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
920. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910906].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
921. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910907].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
922. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910908].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
923. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910909].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
924. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910910].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
925. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910911].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
926. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910912].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
927. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910913].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
928. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910914].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
929. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910915].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
930. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910916].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
931. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910917].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
932. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910918].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
933. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910919].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
934. [Rozdziały, etapy i zdolności Dantego [910901] — tytuł] 시간살인마의 심상
   źródło: DungeonNode91-9.json :: dataList[id=910901].stageList[id=910920].title
   (powtórzenie elementu 725 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageChapterText-a1c7p1
- plik gry: `StageChapterText-a1c7p1.json`

935. [Rozdziały, etapy i zdolności Dantego [chapter_p_107] — korporacja] P사
   źródło: StageChapterText-a1c7p1.json :: dataList[id=chapter_p_107].company
   limit: do 40 znaków
   EN: P Corp.
   PL: P Corp.
936. [Rozdziały, etapy i zdolności Dantego [chapter_p_107] — dzielnica / obszar] 16구
   źródło: StageChapterText-a1c7p1.json :: dataList[id=chapter_p_107].area
   limit: do 40 znaków
   EN: District 16
   PL: Dystrykt 16
937. [Rozdziały, etapy i zdolności Dantego [chapter_p_107] — numer rozdziału] 7장
   źródło: StageChapterText-a1c7p1.json :: dataList[id=chapter_p_107].chapter
   limit: do 40 znaków
   EN: Canto VII
   PL: Canto VII
938. [Rozdziały, etapy i zdolności Dantego [chapter_p_107] — tytuł rozdziału] 꿈이 끝나는
   źródło: StageChapterText-a1c7p1.json :: dataList[id=chapter_p_107].chaptertitle
   (powtórzenie elementu 598 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageChapterText
- plik gry: `StageChapterText.json`

939. [Rozdziały, etapy i zdolności Dantego [chapter_d_100] — korporacja] D사
   źródło: StageChapterText.json :: dataList[id=chapter_d_100].company
   limit: do 40 znaków
   EN: D Corp.
   PL: D Corp.
940. [Rozdziały, etapy i zdolności Dantego [chapter_d_100] — dzielnica / obszar] 4구
   źródło: StageChapterText.json :: dataList[id=chapter_d_100].area
   limit: do 40 znaków
   EN: District 4
   PL: Dystrykt 4
941. [Rozdziały, etapy i zdolności Dantego [chapter_d_100] — numer rozdziału] 0장
   źródło: StageChapterText.json :: dataList[id=chapter_d_100].chapter
   limit: do 40 znaków
   EN: Prologue
   PL: Prolog
942. [Rozdziały, etapy i zdolności Dantego [chapter_d_100] — tytuł rozdziału] 어두운 숲
   źródło: StageChapterText.json :: dataList[id=chapter_d_100].chaptertitle
   limit: do 40 znaków
   EN: Selva Oscura
   PL: Selva Oscura
943. [Rozdziały, etapy i zdolności Dantego [chapter_d_101] — korporacja] D사
   źródło: StageChapterText.json :: dataList[id=chapter_d_101].company
   (powtórzenie elementu 939 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
944. [Rozdziały, etapy i zdolności Dantego [chapter_d_101] — dzielnica / obszar] 4구
   źródło: StageChapterText.json :: dataList[id=chapter_d_101].area
   (powtórzenie elementu 940 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
945. [Rozdziały, etapy i zdolności Dantego [chapter_d_101] — numer rozdziału] 1장
   źródło: StageChapterText.json :: dataList[id=chapter_d_101].chapter
   limit: do 40 znaków
   EN: Canto I
   PL: Canto I
946. [Rozdziały, etapy i zdolności Dantego [chapter_d_101] — tytuł rozdziału] 속하지 못하는
   źródło: StageChapterText.json :: dataList[id=chapter_d_101].chaptertitle
   limit: do 40 znaków
   EN: The Outcast
   PL: Nieprzynależny
947. [Rozdziały, etapy i zdolności Dantego [chapter_j_102] — korporacja] J사
   źródło: StageChapterText.json :: dataList[id=chapter_j_102].company
   limit: do 40 znaków
   EN: J Corp.
   PL: J Corp.
948. [Rozdziały, etapy i zdolności Dantego [chapter_j_102] — dzielnica / obszar] 10구
   źródło: StageChapterText.json :: dataList[id=chapter_j_102].area
   limit: do 40 znaków
   EN: District 10
   PL: Dystrykt 10
949. [Rozdziały, etapy i zdolności Dantego [chapter_j_102] — numer rozdziału] 2장
   źródło: StageChapterText.json :: dataList[id=chapter_j_102].chapter
   limit: do 40 znaków
   EN: Canto II
   PL: Canto II
950. [Rozdziały, etapy i zdolności Dantego [chapter_j_102] — tytuł rozdziału] 사랑할 수 없는
   źródło: StageChapterText.json :: dataList[id=chapter_j_102].chaptertitle
   limit: do 40 znaków
   EN: The Unloving
   PL: Niekochająca
951. [Rozdziały, etapy i zdolności Dantego [chapter_k_103] — korporacja] K사
   źródło: StageChapterText.json :: dataList[id=chapter_k_103].company
   limit: do 40 znaków
   EN: K Corp.
   PL: K Corp.
952. [Rozdziały, etapy i zdolności Dantego [chapter_k_103] — dzielnica / obszar] 11구
   źródło: StageChapterText.json :: dataList[id=chapter_k_103].area
   limit: do 40 znaków
   EN: District 11
   PL: Dystrykt 11
953. [Rozdziały, etapy i zdolności Dantego [chapter_k_103] — numer rozdziału] 3장
   źródło: StageChapterText.json :: dataList[id=chapter_k_103].chapter
   limit: do 40 znaków
   EN: Canto III
   PL: Canto III
954. [Rozdziały, etapy i zdolności Dantego [chapter_k_103] — tytuł rozdziału] 마주하지 않는
   źródło: StageChapterText.json :: dataList[id=chapter_k_103].chaptertitle
   limit: do 40 znaków
   EN: The Unconfronting
   PL: Unikający
955. [Rozdziały, etapy i zdolności Dantego [chapter_k_9103] — korporacja] K사
   źródło: StageChapterText.json :: dataList[id=chapter_k_9103].company
   (powtórzenie elementu 951 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
956. [Rozdziały, etapy i zdolności Dantego [chapter_k_9103] — dzielnica / obszar] 11구
   źródło: StageChapterText.json :: dataList[id=chapter_k_9103].area
   (powtórzenie elementu 952 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
957. [Rozdziały, etapy i zdolności Dantego [chapter_k_9103] — numer rozdziału] 3.5장
   źródło: StageChapterText.json :: dataList[id=chapter_k_9103].chapter
   limit: do 40 znaków
   EN: Intervallo I
   PL: Intervallo I
958. [Rozdziały, etapy i zdolności Dantego [chapter_k_9103] — tytuł rozdziału] 헬스 치킨
   źródło: StageChapterText.json :: dataList[id=chapter_k_9103].chaptertitle
   limit: do 40 znaków
   EN: Hell’s Chicken
   PL: Piekielny Kurczak
959. [Rozdziały, etapy i zdolności Dantego [chapter_k_104] — korporacja] K사
   źródło: StageChapterText.json :: dataList[id=chapter_k_104].company
   (powtórzenie elementu 951 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
960. [Rozdziały, etapy i zdolności Dantego [chapter_k_104] — dzielnica / obszar] 11구
   źródło: StageChapterText.json :: dataList[id=chapter_k_104].area
   (powtórzenie elementu 952 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
961. [Rozdziały, etapy i zdolności Dantego [chapter_k_104] — numer rozdziału] 4장
   źródło: StageChapterText.json :: dataList[id=chapter_k_104].chapter
   limit: do 40 znaków
   EN: Canto IV
   PL: Canto IV
962. [Rozdziały, etapy i zdolności Dantego [chapter_k_104] — tytuł rozdziału] 변하지 않는
   źródło: StageChapterText.json :: dataList[id=chapter_k_104].chaptertitle
   limit: do 40 znaków
   EN: The Unchanging
   PL: Niezmienny
963. [Rozdziały, etapy i zdolności Dantego [chapter_u_9104] — korporacja] U사
   źródło: StageChapterText.json :: dataList[id=chapter_u_9104].company
   limit: do 40 znaków
   EN: U Corp.
   PL: U Corp.
964. [Rozdziały, etapy i zdolności Dantego [chapter_u_9104] — dzielnica / obszar] 21구
   źródło: StageChapterText.json :: dataList[id=chapter_u_9104].area
   limit: do 40 znaków
   EN: District 21
   PL: Dystrykt 21
965. [Rozdziały, etapy i zdolności Dantego [chapter_u_9104] — numer rozdziału] 4.5장
   źródło: StageChapterText.json :: dataList[id=chapter_u_9104].chapter
   limit: do 40 znaków
   EN: Intervallo II
   PL: Intervallo II
966. [Rozdziały, etapy i zdolności Dantego [chapter_u_9104] — tytuł rozdziału] 우.미.다
   źródło: StageChapterText.json :: dataList[id=chapter_u_9104].chaptertitle
   limit: do 40 znaków
   EN: S.E.A.
   PL: M.O.R.Z.E.
967. [Rozdziały, etapy i zdolności Dantego [chapter_u_105] — korporacja] U사
   źródło: StageChapterText.json :: dataList[id=chapter_u_105].company
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
968. [Rozdziały, etapy i zdolności Dantego [chapter_u_105] — dzielnica / obszar] 21구
   źródło: StageChapterText.json :: dataList[id=chapter_u_105].area
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
969. [Rozdziały, etapy i zdolności Dantego [chapter_u_105] — numer rozdziału] 5장
   źródło: StageChapterText.json :: dataList[id=chapter_u_105].chapter
   limit: do 40 znaków
   EN: Canto V
   PL: Canto V
970. [Rozdziały, etapy i zdolności Dantego [chapter_u_105] — tytuł rozdziału] 악으로 규정되는
   źródło: StageChapterText.json :: dataList[id=chapter_u_105].chaptertitle
   limit: do 40 znaków
   EN: The Evil Defining
   PL: Naznaczające Zło
971. [Rozdziały, etapy i zdolności Dantego [chapter_u_9105] — korporacja] U사
   źródło: StageChapterText.json :: dataList[id=chapter_u_9105].company
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
972. [Rozdziały, etapy i zdolności Dantego [chapter_u_9105] — dzielnica / obszar] 21구
   źródło: StageChapterText.json :: dataList[id=chapter_u_9105].area
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
973. [Rozdziały, etapy i zdolności Dantego [chapter_u_9105] — numer rozdziału] 5.5장
   źródło: StageChapterText.json :: dataList[id=chapter_u_9105].chapter
   limit: do 40 znaków
   EN: Intervallo III
   PL: Intervallo III
974. [Rozdziały, etapy i zdolności Dantego [chapter_u_9105] — tytuł rozdziału] 20번구의 기적
   źródło: StageChapterText.json :: dataList[id=chapter_u_9105].chaptertitle
   limit: do 40 znaków
   EN: Miracle in District 20
   PL: Cud w Dystrykcie 20
975. [Rozdziały, etapy i zdolności Dantego [chapter_u_9106] — korporacja] U사
   źródło: StageChapterText.json :: dataList[id=chapter_u_9106].company
   (powtórzenie elementu 963 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
976. [Rozdziały, etapy i zdolności Dantego [chapter_u_9106] — dzielnica / obszar] 21구
   źródło: StageChapterText.json :: dataList[id=chapter_u_9106].area
   (powtórzenie elementu 964 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
977. [Rozdziały, etapy i zdolności Dantego [chapter_u_9106] — tytuł rozdziału] 제 2 회 발푸르기스의 밤
   źródło: StageChapterText.json :: dataList[id=chapter_u_9106].chaptertitle
   limit: do 40 znaków
   EN: The 2nd Walpurgis Night
   PL: 2. Noc Walpurgii
978. [Rozdziały, etapy i zdolności Dantego [chapter_t_9107] — korporacja] T사
   źródło: StageChapterText.json :: dataList[id=chapter_t_9107].company
   limit: do 40 znaków
   EN: T Corp.
   PL: T Corp.
979. [Rozdziały, etapy i zdolności Dantego [chapter_t_9107] — dzielnica / obszar] 20구
   źródło: StageChapterText.json :: dataList[id=chapter_t_9107].area
   limit: do 40 znaków
   EN: District 20
   PL: Dystrykt 20
980. [Rozdziały, etapy i zdolności Dantego [chapter_t_9107] — numer rozdziału] 5.5장
   źródło: StageChapterText.json :: dataList[id=chapter_t_9107].chapter
   (powtórzenie elementu 973 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
981. [Rozdziały, etapy i zdolności Dantego [chapter_t_9107] — tytuł rozdziału] 육참골단
   źródło: StageChapterText.json :: dataList[id=chapter_t_9107].chaptertitle
   limit: do 50 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Yield My Flesh\nto Claim Their Bones
   PL: Oddam Ciało,\nby Złamać Ich Kości
982. [Rozdziały, etapy i zdolności Dantego [chapter_t_106] — korporacja] T사
   źródło: StageChapterText.json :: dataList[id=chapter_t_106].company
   (powtórzenie elementu 978 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
983. [Rozdziały, etapy i zdolności Dantego [chapter_t_106] — dzielnica / obszar] 20구
   źródło: StageChapterText.json :: dataList[id=chapter_t_106].area
   (powtórzenie elementu 979 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
984. [Rozdziały, etapy i zdolności Dantego [chapter_t_106] — numer rozdziału] 6장
   źródło: StageChapterText.json :: dataList[id=chapter_t_106].chapter
   limit: do 40 znaków
   EN: Canto VI
   PL: Canto VI
985. [Rozdziały, etapy i zdolności Dantego [chapter_t_106] — tytuł rozdziału] 마음이 어긋나는
   źródło: StageChapterText.json :: dataList[id=chapter_t_106].chaptertitle
   limit: do 40 znaków
   EN: The Heartbreaking
   PL: Rozdzierające Serca
986. [Rozdziały, etapy i zdolności Dantego [chapter_t_9108] — korporacja] T사
   źródło: StageChapterText.json :: dataList[id=chapter_t_9108].company
   (powtórzenie elementu 978 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
987. [Rozdziały, etapy i zdolności Dantego [chapter_t_9108] — dzielnica / obszar] 20구
   źródło: StageChapterText.json :: dataList[id=chapter_t_9108].area
   (powtórzenie elementu 979 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
988. [Rozdziały, etapy i zdolności Dantego [chapter_t_9108] — tytuł rozdziału] 제 3 회 발푸르기스의 밤
   źródło: StageChapterText.json :: dataList[id=chapter_t_9108].chaptertitle
   limit: do 40 znaków
   EN: The 3rd Walpurgis Night
   PL: 3. Noc Walpurgii
989. [Rozdziały, etapy i zdolności Dantego [chapter_t_9109] — korporacja] T사
   źródło: StageChapterText.json :: dataList[id=chapter_t_9109].company
   (powtórzenie elementu 978 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
990. [Rozdziały, etapy i zdolności Dantego [chapter_t_9109] — dzielnica / obszar] 20구
   źródło: StageChapterText.json :: dataList[id=chapter_t_9109].area
   (powtórzenie elementu 979 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
991. [Rozdziały, etapy i zdolności Dantego [chapter_t_9109] — numer rozdziału] 6.5장
   źródło: StageChapterText.json :: dataList[id=chapter_t_9109].chapter
   limit: do 40 znaków
   EN: Intervallo IV
   PL: Intervallo IV
992. [Rozdziały, etapy i zdolności Dantego [chapter_t_9109] — tytuł rozdziału] 시간살인시간
   źródło: StageChapterText.json :: dataList[id=chapter_t_9109].chaptertitle
   limit: do 40 znaków
   EN: Timekilling Time
   PL: Czas Zabijania Czasu
993. [Rozdziały, etapy i zdolności Dantego [chapter_t_9110] — korporacja] T사
   źródło: StageChapterText.json :: dataList[id=chapter_t_9110].company
   (powtórzenie elementu 978 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
994. [Rozdziały, etapy i zdolności Dantego [chapter_t_9110] — dzielnica / obszar] 20구
   źródło: StageChapterText.json :: dataList[id=chapter_t_9110].area
   (powtórzenie elementu 979 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
995. [Rozdziały, etapy i zdolności Dantego [chapter_t_9110] — numer rozdziału] 6.5장
   źródło: StageChapterText.json :: dataList[id=chapter_t_9110].chapter
   (powtórzenie elementu 991 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
996. [Rozdziały, etapy i zdolności Dantego [chapter_t_9110] — tytuł rozdziału] 워프특급 살인사건
   źródło: StageChapterText.json :: dataList[id=chapter_t_9110].chaptertitle
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Murder on the\nWARP Express
   PL: Morderstwo\nw Ekspresie WARP
997. [Rozdziały, etapy i zdolności Dantego [chapter_p_9111] — korporacja] P사
   źródło: StageChapterText.json :: dataList[id=chapter_p_9111].company
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
998. [Rozdziały, etapy i zdolności Dantego [chapter_p_9111] — dzielnica / obszar] 16구
   źródło: StageChapterText.json :: dataList[id=chapter_p_9111].area
   (powtórzenie elementu 936 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
999. [Rozdziały, etapy i zdolności Dantego [chapter_p_9111] — tytuł rozdziału] 제 4 회 발푸르기스의 밤
   źródło: StageChapterText.json :: dataList[id=chapter_p_9111].chaptertitle
   limit: do 40 znaków
   EN: The 4th Walpurgis Night
   PL: 4. Noc Walpurgii
1000. [Rozdziały, etapy i zdolności Dantego [chapter_p_9019] — korporacja] P사
   źródło: StageChapterText.json :: dataList[id=chapter_p_9019].company
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1001. [Rozdziały, etapy i zdolności Dantego [chapter_p_9019] — dzielnica / obszar] 16구
   źródło: StageChapterText.json :: dataList[id=chapter_p_9019].area
   (powtórzenie elementu 936 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1002. [Rozdziały, etapy i zdolności Dantego [chapter_p_9019] — tytuł rozdziału] 제 5 회 발푸르기스의 밤
   źródło: StageChapterText.json :: dataList[id=chapter_p_9019].chaptertitle
   limit: do 40 znaków
   EN: The 5th Walpurgis Night
   PL: 5. Noc Walpurgii
1003. [Rozdziały, etapy i zdolności Dantego [chapter_p_9114] — korporacja] P사
   źródło: StageChapterText.json :: dataList[id=chapter_p_9114].company
   (powtórzenie elementu 935 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1004. [Rozdziały, etapy i zdolności Dantego [chapter_p_9114] — dzielnica / obszar] 16구
   źródło: StageChapterText.json :: dataList[id=chapter_p_9114].area
   (powtórzenie elementu 936 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1005. [Rozdziały, etapy i zdolności Dantego [chapter_p_9114] — numer rozdziału] 7.5장
   źródło: StageChapterText.json :: dataList[id=chapter_p_9114].chapter
   limit: do 40 znaków
   EN: Intervallo V
   PL: Intervallo V
1006. [Rozdziały, etapy i zdolności Dantego [chapter_p_9114] — tytuł rozdziału] LCB 정기검진
   źródło: StageChapterText.json :: dataList[id=chapter_p_9114].chaptertitle
   limit: do 40 znaków
   EN: LCB Regular Check-up
   PL: Okresowe Badania LCB
1007. [Rozdziały, etapy i zdolności Dantego [chapter_h_9116] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_h_9116].company
   limit: do 40 znaków
   EN: H Corp.
   PL: H Corp.
1008. [Rozdziały, etapy i zdolności Dantego [chapter_h_9116] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_h_9116].area
   limit: do 40 znaków
   EN: District 8
   PL: Dystrykt 8
1009. [Rozdziały, etapy i zdolności Dantego [chapter_h_9116] — numer rozdziału] 7.5장
   źródło: StageChapterText.json :: dataList[id=chapter_h_9116].chapter
   (powtórzenie elementu 1005 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1010. [Rozdziały, etapy i zdolności Dantego [chapter_h_9116] — tytuł rozdziału] 심야청소
   źródło: StageChapterText.json :: dataList[id=chapter_h_9116].chaptertitle
   limit: do 40 znaków
   EN: Nocturnal Sweeping
   PL: Nocne Sprzątanie
1011. [Rozdziały, etapy i zdolności Dantego [chapter_h_108] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_h_108].company
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1012. [Rozdziały, etapy i zdolności Dantego [chapter_h_108] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_h_108].area
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1013. [Rozdziały, etapy i zdolności Dantego [chapter_h_108] — numer rozdziału] 8장
   źródło: StageChapterText.json :: dataList[id=chapter_h_108].chapter
   limit: do 40 znaków
   EN: Canto VIII
   PL: Canto VIII
1014. [Rozdziały, etapy i zdolności Dantego [chapter_h_108] — tytuł rozdziału] 바라볼 수밖에 없는
   źródło: StageChapterText.json :: dataList[id=chapter_h_108].chaptertitle
   limit: do 40 znaków
   EN: The Surrendered Witnessing
   PL: Skazany na Patrzenie
1015. [Rozdziały, etapy i zdolności Dantego [chapter_p_9020] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_p_9020].company
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1016. [Rozdziały, etapy i zdolności Dantego [chapter_p_9020] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_p_9020].area
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1017. [Rozdziały, etapy i zdolności Dantego [chapter_p_9020] — tytuł rozdziału] 제 6 회 발푸르기스의 밤
   źródło: StageChapterText.json :: dataList[id=chapter_p_9020].chaptertitle
   limit: do 40 znaków
   EN: The 6th Walpurgis Night
   PL: 6. Noc Walpurgii
1018. [Rozdziały, etapy i zdolności Dantego [chapter_h_9119] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_h_9119].company
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1019. [Rozdziały, etapy i zdolności Dantego [chapter_h_9119] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_h_9119].area
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1020. [Rozdziały, etapy i zdolności Dantego [chapter_h_9119] — numer rozdziału] 8.5장
   źródło: StageChapterText.json :: dataList[id=chapter_h_9119].chapter
   limit: do 40 znaków
   EN: Intervallo VI
   PL: Intervallo VI
1021. [Rozdziały, etapy i zdolności Dantego [chapter_h_9119] — tytuł rozdziału] 절차탁춘
   źródło: StageChapterText.json :: dataList[id=chapter_h_9119].chaptertitle
   limit: do 40 znaków
   EN: Spring Cultivation
   PL: Wiosenny Szlif
1022. [Rozdziały, etapy i zdolności Dantego [chapter_h_9120] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_h_9120].company
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1023. [Rozdziały, etapy i zdolności Dantego [chapter_h_9120] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_h_9120].area
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1024. [Rozdziały, etapy i zdolności Dantego [chapter_h_9120] — numer rozdziału] 8.5-EX
   źródło: StageChapterText.json :: dataList[id=chapter_h_9120].chapter
   limit: do 40 znaków
   EN: 8.5-EX
   PL: 8.5-EX
1025. [Rozdziały, etapy i zdolności Dantego [chapter_h_9120] — tytuł rozdziału] 선의의 순례
   źródło: StageChapterText.json :: dataList[id=chapter_h_9120].chaptertitle
   limit: do 40 znaków
   EN: Pilgrimage of Compassion
   PL: Pielgrzymka Współczucia
1026. [Rozdziały, etapy i zdolności Dantego [chapter_h_109] — korporacja] H사
   źródło: StageChapterText.json :: dataList[id=chapter_h_109].company
   (powtórzenie elementu 1007 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1027. [Rozdziały, etapy i zdolności Dantego [chapter_h_109] — dzielnica / obszar] 8구
   źródło: StageChapterText.json :: dataList[id=chapter_h_109].area
   (powtórzenie elementu 1008 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1028. [Rozdziały, etapy i zdolności Dantego [chapter_h_109] — numer rozdziału] 9장
   źródło: StageChapterText.json :: dataList[id=chapter_h_109].chapter
   limit: do 40 znaków
   EN: Canto IX
   PL: Canto IX
1029. [Rozdziały, etapy i zdolności Dantego [chapter_h_109] — tytuł rozdziału] 끊어지지 않는
   źródło: StageChapterText.json :: dataList[id=chapter_h_109].chaptertitle
   limit: do 40 znaków
   EN: The Unsevering
   PL: Nierozerwalne
1030. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_109] — korporacja] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_109].company
   limit: do 40 znaków
   EN: ??
   PL: ??
1031. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_109] — dzielnica / obszar] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_109].area
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1032. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_109] — numer rozdziału] 9장
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_109].chapter
   (powtórzenie elementu 1028 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1033. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_109] — tytuł rozdziału] 끊어지지 않는
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_109].chaptertitle
   (powtórzenie elementu 1029 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1034. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9123] — korporacja] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9123].company
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1035. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9123] — dzielnica / obszar] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9123].area
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1036. [Rozdziały, etapy i zdolności Dantego [chapter_h_9125] — korporacja] ??
   źródło: StageChapterText.json :: dataList[id=chapter_h_9125].company
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1037. [Rozdziały, etapy i zdolności Dantego [chapter_h_9125] — dzielnica / obszar] ??
   źródło: StageChapterText.json :: dataList[id=chapter_h_9125].area
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1038. [Rozdziały, etapy i zdolności Dantego [chapter_h_9125] — numer rozdziału] 9.5장
   źródło: StageChapterText.json :: dataList[id=chapter_h_9125].chapter
   limit: do 40 znaków
   EN: Intervallo VII
   PL: Intervallo VII
1039. [Rozdziały, etapy i zdolności Dantego [chapter_h_9125] — tytuł rozdziału] 타래 엮기
   źródło: StageChapterText.json :: dataList[id=chapter_h_9125].chaptertitle
   limit: do 40 znaków
   EN: Twining Threads
   PL: Splatanie Pasm
1040. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9125] — korporacja] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9125].company
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1041. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9125] — dzielnica / obszar] ??
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9125].area
   (powtórzenie elementu 1030 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1042. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9125] — numer rozdziału] 9.5장
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9125].chapter
   (powtórzenie elementu 1038 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1043. [Rozdziały, etapy i zdolności Dantego [chapter_unknown_9125] — tytuł rozdziału] 타래 엮기
   źródło: StageChapterText.json :: dataList[id=chapter_unknown_9125].chaptertitle
   (powtórzenie elementu 1039 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1044. [Rozdziały, etapy i zdolności Dantego [chapter_n_9127] — korporacja] N사
   źródło: StageChapterText.json :: dataList[id=chapter_n_9127].company
   limit: do 40 znaków
   EN: N Corp.
   PL: N Corp.
1045. [Rozdziały, etapy i zdolności Dantego [chapter_n_9127] — dzielnica / obszar] 14구
   źródło: StageChapterText.json :: dataList[id=chapter_n_9127].area
   limit: do 40 znaków
   EN: District 14
   PL: Dystrykt 14
1046. [Rozdziały, etapy i zdolności Dantego [chapter_n_9127] — numer rozdziału] 9.5장
   źródło: StageChapterText.json :: dataList[id=chapter_n_9127].chapter
   (powtórzenie elementu 1038 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1047. [Rozdziały, etapy i zdolności Dantego [chapter_n_9127] — tytuł rozdziału] 경험기억
   źródło: StageChapterText.json :: dataList[id=chapter_n_9127].chaptertitle
   limit: do 40 znaków
   EN: Mnestic Experience
   PL: Pamięć Doświadczenia
1048. [Rozdziały, etapy i zdolności Dantego [chapter_n_110] — korporacja] N사
   źródło: StageChapterText.json :: dataList[id=chapter_n_110].company
   (powtórzenie elementu 1044 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1049. [Rozdziały, etapy i zdolności Dantego [chapter_n_110] — dzielnica / obszar] 14구
   źródło: StageChapterText.json :: dataList[id=chapter_n_110].area
   (powtórzenie elementu 1045 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1050. [Rozdziały, etapy i zdolności Dantego [chapter_n_110] — numer rozdziału] 10장
   źródło: StageChapterText.json :: dataList[id=chapter_n_110].chapter
   limit: do 40 znaków
   EN: Canto X
   PL: Canto X
1051. [Rozdziały, etapy i zdolności Dantego [chapter_n_110] — tytuł rozdziału] 바라보아지는
   źródło: StageChapterText.json :: dataList[id=chapter_n_110].chaptertitle
   limit: do 40 znaków
   EN: The Gaze Bearing
   PL: Pod Spojrzeniem
1052. [Rozdziały, etapy i zdolności Dantego [chapter_n_9128] — korporacja] N사
   źródło: StageChapterText.json :: dataList[id=chapter_n_9128].company
   (powtórzenie elementu 1044 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1053. [Rozdziały, etapy i zdolności Dantego [chapter_n_9128] — dzielnica / obszar] 14구
   źródło: StageChapterText.json :: dataList[id=chapter_n_9128].area
   (powtórzenie elementu 1045 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1054. [Rozdziały, etapy i zdolności Dantego [chapter_n_9128] — numer rozdziału] 10장
   źródło: StageChapterText.json :: dataList[id=chapter_n_9128].chapter
   (powtórzenie elementu 1050 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1055. [Rozdziały, etapy i zdolności Dantego [chapter_n_9128] — tytuł rozdziału] 바라보아지는
   źródło: StageChapterText.json :: dataList[id=chapter_n_9128].chaptertitle
   (powtórzenie elementu 1051 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageContinueText
- plik gry: `StageContinueText.json`

1056. [Rozdziały, etapy i zdolności Dantego [StageInfoUI_ContinueText] — tekst] 컨티뉴 가능
   źródło: StageContinueText.json :: dataList[id=StageInfoUI_ContinueText].content
   limit: do 120 znaków
   EN: Continuable
   PL: Możliwa Kontynuacja
1057. [Rozdziały, etapy i zdolności Dantego [ContinueMainTitle] — tekst] 컨티뉴
   źródło: StageContinueText.json :: dataList[id=ContinueMainTitle].content
   limit: do 120 znaków
   EN: Continue
   PL: Kontynuacja
1058. [Rozdziały, etapy i zdolności Dantego [ContinueMainDesc_HellChainInsufficient] — tekst] 전투에서 패배했습니다.\n<color=#e94d37>광기 40</color>을 사용하여 계속 플레이 하시겠습니까?\n\n<color=#ebcaa2><컨티뉴 시 적용되는 효과></color>\n<color=#F8C200>- 인격, E.G.O가 보유한 효과의 전투당 횟수 제한 초기화\n- 모든 속성 E.G.O 자원 +10\n- 모든 아군 체력 · 정신력 최대로 회복\n(빼기 코인 인격은 정신력 -30으로 적용)</color>
   źródło: StageContinueText.json :: dataList[id=ContinueMainDesc_HellChainInsufficient].content
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: <color=#e94d37>, </color>, <color=#ebcaa2>, <color=#F8C200>, \n
   EN: You have been defeated.\nUse <color=#e94d37>40 Lunacy</color> and continue the battle?\n\n<color=#ebcaa2><Effects Applied Upon Continuing></color>\n<color=#F8C200>- Reset Identities & E.G.O Per-Encounter Effect Activation Limits\n- Gain 10 E.G.O Resources for all Affinities\n- Fully restore HP and SP of all allies\n(SP of Minus Coin Identities set to -30)</color>
   PL: Poniosłeś porażkę w walce.\nCzy chcesz użyć <color=#e94d37>40 Szaleństwa</color>, aby kontynuować?\n\n<color=#ebcaa2>[Efekty po Kontynuacji]</color>\n<color=#F8C200>- Reset limitów aktywacji efektów na walkę dla Tożsamości i E.G.O\n- +10 zasobów E.G.O każdego Grzechu\n- Pełne odnowienie PŻ i SP wszystkich sojuszników\n(dla Tożsamości z Monetami Ujemnymi SP ustawiane na -30)</color>
1059. [Rozdziały, etapy i zdolności Dantego [ContinueMainRemainContinueCount] — tekst] 남은 횟수
   źródło: StageContinueText.json :: dataList[id=ContinueMainRemainContinueCount].content
   limit: do 120 znaków
   EN: Remaining Continues
   PL: Pozostałe użycia
1060. [Rozdziały, etapy i zdolności Dantego [ContinueMainHaveLunacy] — tekst] 보유 광기
   źródło: StageContinueText.json :: dataList[id=ContinueMainHaveLunacy].content
   limit: do 120 znaków
   EN: Remaining Lunacy
   PL: Posiadane Szaleństwo
1061. [Rozdziały, etapy i zdolności Dantego [ContinueMainFreeLunacy] — tekst] 무료
   źródło: StageContinueText.json :: dataList[id=ContinueMainFreeLunacy].content
   limit: do 120 znaków
   EN: Free
   PL: Darmowe
1062. [Rozdziały, etapy i zdolności Dantego [ContinueMainPaidLunacy] — tekst] 유료
   źródło: StageContinueText.json :: dataList[id=ContinueMainPaidLunacy].content
   limit: do 120 znaków
   EN: Paid
   PL: Płatne
1063. [Rozdziały, etapy i zdolności Dantego [ContinueMainCancel] — tekst] 스테이지 포기
   źródło: StageContinueText.json :: dataList[id=ContinueMainCancel].content
   limit: do 120 znaków
   EN: Forfeit Battle
   PL: Poddaj etap
1064. [Rozdziały, etapy i zdolności Dantego [ContinueMainUseContinue] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainUseContinue].content
   limit: do 120 znaków
   EN: Continue Battle
   PL: Kontynuuj walkę
1065. [Rozdziały, etapy i zdolności Dantego [ContinueMainBuyHellChain] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainBuyHellChain].content
   (powtórzenie elementu 1064 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1066. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Title_HellChain] — tekst] 안내
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Title_HellChain].content
   limit: do 120 znaków
   EN: Notice
   PL: Informacja
1067. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Desc] — tekst] 스테이지 컨티뉴 기능을 사용해 스테이지를 클리어한 경우,\nEX 클리어로 기록되지 않습니다.\n또한 컨티뉴에 사용된 재화가 반환되지 않으며,\n사용된 광기는 청약철회가 불가능합니다.\n\n단, 스테이지를 포기하거나 비상적으로 게임이 종료된 경우,\n이번 전투에서 컨티뉴에 사용된 재화가 모두 반환됩니다.
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Desc].content
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing this Stage by using a Stage Continue function will prevent its Extra Conditions from being fulfilled.\nAlso, upon clearing the Stage, resources spent to continue this battle will not be restored, and spent Lunacy cannot be refunded.\n\nHowever, if, after using the Continue function, the player forfeits this Stage or if the game closes due to unusual circumstances, any Lunacy spent to continue this battle will be restored.
   PL: Ukończenie etapu z użyciem funkcji Kontynuacji nie zostanie zaliczone jako ukończenie EX.\nPonadto po ukończeniu etapu zasoby zużyte na Kontynuację nie podlegają zwrotowi, a wydane Szaleństwo nie podlega anulowaniu zakupu.\n\nJeśli jednak poddasz etap lub gra zamknie się w wyniku błędu, całe Szaleństwo użyte na Kontynuację w tej walce zostanie zwrócone.
1068. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Skip] — tekst] 다음 접속까지 안내 팝업 띄우지 않기
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Skip].content
   limit: do 120 znaków
   EN: Don't show this message again until next login
   PL: Nie pokazuj ponownie do następnego logowania
1069. [Rozdziały, etapy i zdolności Dantego [ContinuePurchase_LunacyTitle] — tekst] 광기
   źródło: StageContinueText.json :: dataList[id=ContinuePurchase_LunacyTitle].content
   limit: do 120 znaków
   EN: Lunacy
   PL: Szaleństwo
1070. [Rozdziały, etapy i zdolności Dantego [ContinuePurchase_Notice] — tekst] ※ 무료 광기부터 사용됩니다.
   źródło: StageContinueText.json :: dataList[id=ContinuePurchase_Notice].content
   limit: do 120 znaków
   EN: ※ Free Lunacy is used first.
   PL: ※ W pierwszej kolejności zużywane jest Darmowe Szaleństwo.
1071. [Rozdziały, etapy i zdolności Dantego [ContinueConfirmCancel] — tekst] 취소
   źródło: StageContinueText.json :: dataList[id=ContinueConfirmCancel].content
   limit: do 120 znaków
   EN: Cancel
   PL: Anuluj
1072. [Rozdziały, etapy i zdolności Dantego [ContinueMainConfirm] — tekst] 컨티뉴 진행
   źródło: StageContinueText.json :: dataList[id=ContinueMainConfirm].content
   (powtórzenie elementu 1064 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1073. [Rozdziały, etapy i zdolności Dantego [ContinueConfirm_Title_Lunacy] — tekst] 안내
   źródło: StageContinueText.json :: dataList[id=ContinueConfirm_Title_Lunacy].content
   (powtórzenie elementu 1066 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1074. [Rozdziały, etapy i zdolności Dantego [ContinueResult_Win_Desc] — tekst] 스테이지를 클리어하여\n컨티뉴에 사용한 재화가 소모되었습니다.
   źródło: StageContinueText.json :: dataList[id=ContinueResult_Win_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clearing the Stage has consumed all resources\nspent to Continue the battle.
   PL: Ukończono etap — zużyto zasoby\nprzeznaczone na Kontynuację walki.
1075. [Rozdziały, etapy i zdolności Dantego [ContinueResult_Defeat_Desc] — tekst] 스테이지를 포기하여\n컨티뉴에 사용한 재화가 반환되었습니다.
   źródło: StageContinueText.json :: dataList[id=ContinueResult_Defeat_Desc].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Forfeiting the Stage has returned all resources\nspent to Continue the battle.
   PL: Poddano etap — zwrócono zasoby\nprzeznaczone na Kontynuację walki.

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c10p1
- plik gry: `StageNode-a1c10p1.json`

1076. [Rozdziały, etapy i zdolności Dantego [11001] — tytuł] 재판
   źródło: StageNode-a1c10p1.json :: dataList[id=11001].title
   limit: do 40 znaków
   EN: The Trial
   PL: Proces
1077. [Rozdziały, etapy i zdolności Dantego [11002] — tytuł] 법정
   źródło: StageNode-a1c10p1.json :: dataList[id=11002].title
   limit: do 40 znaków
   EN: The Courthouse
   PL: Sala Sądowa
1078. [Rozdziały, etapy i zdolności Dantego [11003] — tytuł] 계획
   źródło: StageNode-a1c10p1.json :: dataList[id=11003].title
   limit: do 40 znaków
   EN: The Plan
   PL: Plan
1079. [Rozdziały, etapy i zdolności Dantego [11004] — tytuł] 시지프 백화점
   źródło: StageNode-a1c10p1.json :: dataList[id=11004].title
   limit: do 40 znaków
   EN: Grand Magasin Sisyphe
   PL: Dom Towarowy Sisyphe

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c10p3
- plik gry: `StageNode-a1c10p3.json`

1080. [Rozdziały, etapy i zdolności Dantego [11007] — tytuł] 연기
   źródło: StageNode-a1c10p3.json :: dataList[id=11007].title
   limit: do 40 znaków
   EN: The Smoke
   PL: Dym

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p1
- plik gry: `StageNode-a1c5p1.json`

1081. [Rozdziały, etapy i zdolności Dantego [10501] — tytuł] 항해
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].title
   limit: do 40 znaków
   EN: Setting Sail
   PL: Rejs
1082. [Rozdziały, etapy i zdolności Dantego [10501] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].place
   limit: do 40 znaków
   EN: Mephistopheles the Busboat
   PL: Autobus-Łódź Mefistofeles
1083. [Rozdziały, etapy i zdolności Dantego [10501] — opis] 한바탕 초록색 불빛의 소동이 일단락된 뒤, 버스배는 계속 항해 중이다. 파우스트가 무언갈 발견한 듯이 키가 있는 곳을 향해 걸어간다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10501].desc
   limit: do 160 znaków
   EN: We sail on, the incident with the green lights finally behind us. Faust approaches the helm as though she noticed something.
   PL: Gdy zamieszanie z zielonym światłem dobiegło końca, nasz autobus-łódź płynie dalej. Faust rusza w stronę steru, jakby coś dostrzegła.
1084. [Rozdziały, etapy i zdolności Dantego [10502] — tytuł] 규칙
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].title
   limit: do 40 znaków
   EN: The Laws
   PL: Prawa Jeziora
1085. [Rozdziały, etapy i zdolności Dantego [10502] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1086. [Rozdziały, etapy i zdolności Dantego [10502] — opis] 항해에 대한 오티스의 강의가 무르익을 무렵, 엔진이 멈춰버렸다. 앞으로 갈 길은 한참 남았는데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10502].desc
   limit: do 160 znaków
   EN: The engine came to a sputtering halt as Outis's seafaring lecture reached its climax. But we still have so much to go...
   PL: Gdy wykład Outis o żegludze sięgał zenitu, silnik zgasł z kaszlem. A przed nami wciąż szmat drogi…
1087. [Rozdziały, etapy i zdolności Dantego [10503] — tytuł] 공명 굽쇠
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].title
   limit: do 40 znaków
   EN: Resonance Tuning Fork
   PL: Kamerton Rezonansowy
1088. [Rozdziały, etapy i zdolności Dantego [10503] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1089. [Rozdziały, etapy i zdolności Dantego [10503] — opis] 오티스의 구령에 맞춰 일심동체…는 아니지만 수감자들의 단합으로 엔진이 멈춘 버스배는 움직이고 있었다. 그러던 중 이 호수에 살아남기 위해서 반드시 알아야만 하는 사실이 있었다. 가령 규칙을 어기면 과자 부스러기 꼴이 된다거나… 그리고 우리의 버스배는 항해 노선과는 무관하게 끌려가고 있었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10503].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Our busboat with a dead engine was still sailing, with every Sinner's hearts and bodies... well, not exactly every Sinner, but most Sinner's hearts and bodies working as one. Oh, and we learned a very valuable lesson about surviving in the Great Lake: that breaking its laws can have catastrophic results.\n... And that's when we noticed that our busboat was getting dragged by something off course.
   PL: W rytm komend Outis nasz autobus-łódź z martwym silnikiem wciąż posuwał się naprzód dzięki jedności serc i rąk… no, może nie wszystkich, ale większości Grzeszników. Przy okazji poznaliśmy bezcenną lekcję przetrwania na Wielkim Jeziorze: złamanie jego praw grozi marnym końcem.\n…I właśnie wtedy zauważyliśmy, że coś ściąga nas z kursu.
1090. [Rozdziały, etapy i zdolności Dantego [10504] — tytuł] 납치범
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].title
   limit: do 40 znaków
   EN: Kidnappers
   PL: Porywacze
1091. [Rozdziały, etapy i zdolności Dantego [10504] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].place
   limit: do 40 znaków
   EN: U Corp.'s Marlin Portship
   PL: Portowiec Marlin U Corp.
1092. [Rozdziały, etapy i zdolności Dantego [10504] — opis] 몇 번의 위험과 호수를 건너 목적지에 도착했다. 이번 목적지는 U사의 청새치 항구선 이라는 곳인듯하다. 그곳은 수없이 많은 컨테이너로 이루어진 거대한 배였다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10504].desc
   limit: do 280 znaków
   EN: After numerous trials and tribulations, we finally arrived at our destination. Looks like this place is called Marlin Portship of U Corp., a giant seafaring vessel made by merging together countless shipping containers.
   PL: Po wielu niebezpieczeństwach dotarliśmy do celu — olbrzymiego statku-portu Marlin należącego do U Corp., złożonego z niezliczonych kontenerów.
1093. [Rozdziały, etapy i zdolności Dantego [10505] — tytuł] 명령 불복종
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].title
   limit: do 40 znaków
   EN: Insubordination
   PL: Niesubordynacja
1094. [Rozdziały, etapy i zdolności Dantego [10505] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1095. [Rozdziały, etapy i zdolności Dantego [10505] — opis] 접선하기로 했었던 LCCB 대원 대신 악질적인 납치범이 우릴 반겨주었다. 몸값을 요구하는 그들에게 어떻게 대응해야 할지 논의하고 있었던 와중… 이스마엘은 아랑곳없이 돌발 행동을 한다. 이스마엘의 눈은 여러 감정으로 가득 차 갈피를 못 잡고 있는 것만 같았다. 우리는 납치된 LCCB 대원의 생사도 확인 못 한 채로 납치범들을 물리쳐야 한다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10505].desc
   limit: do 490 znaków
   EN: In place of the LCCB Agent we were supposed to meet was a posse of kidnappers who demanded ransom from us. As we were discussing our plan of action, Ishmael suddenly decided to act. I could see from her eyes... that there was a mix of numerous, complex feelings. Now, we have no choice but to take these kidnappers out, even if we are yet to learn if the LCCB Agent is alive or not.
   PL: Zamiast łącznika LCCB powitała nas zgraja porywaczy żądających okupu. Gdy naradzaliśmy się, co począć, Ishmael bez ostrzeżenia ruszyła do ataku; w jej oczach kłębił się istny zamęt uczuć. Nie wiedząc nawet, czy porwany agent LCCB żyje, musimy rozprawić się z porywaczami.
1096. [Rozdziały, etapy i zdolności Dantego [10506] — tytuł] 클럽
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].title
   limit: do 40 znaków
   EN: The Club
   PL: Klub
1097. [Rozdziały, etapy i zdolności Dantego [10506] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1098. [Rozdziały, etapy i zdolności Dantego [10506] — opis] 모두가 함께 결속된 상태로 작전을 수행하는 건 아닌 것 같다.  우리는 이스마엘의 협박으로 인해 겨우 얻어낸 보스의 위치를 향해 이동했다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10506].desc
   limit: do 210 znaków
   EN: Maybe not everyone felt a sense of unity, a sense of belonging from this group. We headed to the boss's location that Ishmael threatened out of the kidnappers.
   PL: Wygląda na to, że nie wszyscy czuli się częścią jednej drużyny. Ruszyliśmy pod adres szefa wydobyty groźbami przez Ishmael.
1099. [Rozdziały, etapy i zdolności Dantego [10507] — tytuł] 클럽 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].title
   limit: do 40 znaków
   EN: The Club 2
   PL: Klub 2
1100. [Rozdziały, etapy i zdolności Dantego [10507] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1101. [Rozdziały, etapy i zdolności Dantego [10507] — opis] 납치범들의 보스가 있는 곳은 시끄러운 음악들이 새어 나오고 있는 클럽이었다. 조용히 들어가고자 했지만… 우리는 클럽 입구에서부터 싸움에 휩싸이게 되었고 겨우 문지기들을 물러나게 만들었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10507].desc
   limit: do 360 znaków
   EN: Following the kidnapper's directions, we found ourselves at the entrance of a club blaring with music. I wanted to do this quietly... But we broke into a fight pretty much immediately as we tried to talk to the bouncers. We had to find different ways to convince them to let us in.
   PL: Siedzibą szefa porywaczy okazał się tętniący głośną muzyką klub. Chciałem załatwić sprawę po cichu… lecz już od progu wywiązała się bójka z bramkarzami, których ledwie zmusiliśmy do ustąpienia.
1102. [Rozdziały, etapy i zdolności Dantego [10508] — tytuł] 클럽 3
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].title
   limit: do 40 znaków
   EN: The Club 3
   PL: Klub 3
1103. [Rozdziały, etapy i zdolności Dantego [10508] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1104. [Rozdziały, etapy i zdolności Dantego [10508] — opis] 납치범들의 보스가 있는 곳은 시끄러운 음악들이 새어 나오고 있는 클럽이었다. 조용히 들어가고자 했지만… 우리는 클럽 입구에서부터 싸움에 휩싸이게 되었고 겨우 문지기들을 물러나게 만들었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10508].desc
   (powtórzenie elementu 1101 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1105. [Rozdziały, etapy i zdolności Dantego [10509] — tytuł] 부선장
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].title
   limit: do 40 znaków
   EN: The First Mate
   PL: Pierwsza Oficer
1106. [Rozdziały, etapy i zdolności Dantego [10509] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1107. [Rozdziały, etapy i zdolności Dantego [10509] — opis] 클럽을 돌아다니며 납치범들이 소속되어 있는 조직원들을 물리쳤다. 이제 슬슬 그들의 보스가 있는 방도 알아내야 할 텐데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10509].desc
   limit: do 190 znaków
   EN: We trashed the club and defeated members of the Syndicate that the kidnappers were part of. Hopefully we can learn their boss's location soon...
   PL: Przeczesując klub, rozbiliśmy członków syndykatu stojącego za porwaniem. Pora dowiedzieć się, w którym pokoju kryje się ich przywódca…
1108. [Rozdziały, etapy i zdolności Dantego [10510] — tytuł] 부선장 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].title
   limit: do 40 znaków
   EN: The First Mate 2
   PL: Pierwsza Oficer 2
1109. [Rozdziały, etapy i zdolności Dantego [10510] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1110. [Rozdziały, etapy i zdolności Dantego [10510] — opis] 싱클레어의 활약으로 그들의 보스가 있는 방을 알아냈다. 자신을 쌍갈고리 해적단의 부선장이라고 소개하는데…
   źródło: StageNode-a1c5p1.json :: dataList[id=10510].desc
   limit: do 170 znaków
   EN: We learned where the boss's room was, all thanks to Sinclair. She introduced herself as the first mate of the Twinhook Pirates...
   PL: Dzięki Sinclairowi odnaleźliśmy właściwe drzwi. Czekająca w środku kobieta przedstawiła się jako pierwsza oficer Piratów Podwójnego Haka…
1111. [Rozdziały, etapy i zdolności Dantego [10511] — tytuł] 컨테이너
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].title
   limit: do 40 znaków
   EN: Shipping Containers
   PL: Kontenery
1112. [Rozdziały, etapy i zdolności Dantego [10511] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1113. [Rozdziały, etapy i zdolności Dantego [10511] — opis] 쌍갈고리 해적단의 부선장, 스미로부터 납치된 LCCB 부서의 팀장이라는 자가 잡혀있는 위치를 전달받았다. 이스마엘은 확실한 몰살을 원하는 것 같았지만… 나는 몸을 던지면서까지 막았다. 논리적으로 설명할 수도, 납득시킬 수도 없었지만, 후회는 없다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10511].desc
   limit: do 420 znaków
   EN: Smee, first mate of the Twinhook Pirates, told us where they were keeping the captured LCCB Team Leader. Ishmael wanted to leave no loose threads behind... But I stopped her, even if it meant putting myself in danger. I have no logical explanation for what I did, nor could I convince Ishmael... But I don't regret what I did.
   PL: Smee, pierwsza oficer Piratów Podwójnego Haka, zdradziła nam miejsce przetrzymywania kierownika zespołu LCCB. Ishmael chciała wybić piratów co do nogi, lecz własnym ciałem zastąpiłem jej drogę. Nie potrafiłem jej tego logicznie wytłumaczyć, ale nie żałuję swojej decyzji.
1114. [Rozdziały, etapy i zdolności Dantego [10512] — tytuł] 컨테이너 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].title
   limit: do 40 znaków
   EN: Shipping Containers 2
   PL: Kontenery 2
1115. [Rozdziały, etapy i zdolności Dantego [10512] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1116. [Rozdziały, etapy i zdolności Dantego [10512] — opis] 부선장, 스미로부터 납치된 LCCB 부서의 팀장이라는 자가 잡혀있는 위치를 전달받았다. 그곳엔 산처럼 쌓여있는 컨테이너들이 보인다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10512].desc
   limit: do 230 znaków
   EN: Smee, first mate of the Twinhook Pirates, told us where they were keeping the captured LCCB Team Leader. When we got there, we found a whole mountain of shipping containers.
   PL: Dotarliśmy we wskazane przez Smee miejsce, w którym przetrzymywano kierownika zespołu LCCB. Naszym oczom ukazała się cała góra spiętrzonych kontenerów.
1117. [Rozdziały, etapy i zdolności Dantego [10513] — tytuł] 파일럿
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].title
   limit: do 40 znaków
   EN: Mr. Pilot
   PL: Pilot
1118. [Rozdziały, etapy i zdolności Dantego [10513] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1119. [Rozdziały, etapy i zdolności Dantego [10513] — opis] 스미라는 자가 말한 컨테이너를 열자 얼굴엔 눈물범벅이 되어있는 앳된 LCCB 대원이 보인다. 크게 다친 것 같진 않아 보여 다행이다만, 이 자가 팀장이라고…?
   źródło: StageNode-a1c5p1.json :: dataList[id=10513].desc
   limit: do 260 znaków
   EN: When we opened the shipping container Smee singled out, an unexpectedly tearful and youthful face of an LCCB Agent greeted us. I'm glad that he looks mostly unharmed, but... Is he really the Team Leader?
   PL: Gdy otworzyliśmy wskazany przez Smee kontener, ujrzeliśmy zalaną łzami, młodzieńczą twarz agenta LCCB. Na szczęście nie wyglądał na ciężko rannego, ale… to naprawdę ma być kierownik zespołu?
1120. [Rozdziały, etapy i zdolności Dantego [10514] — tytuł] 파일럿 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].title
   limit: do 40 znaków
   EN: Mr. Pilot 2
   PL: Pilot 2
1121. [Rozdziały, etapy i zdolności Dantego [10514] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1122. [Rozdziały, etapy i zdolności Dantego [10514] — opis] 파일럿이라는 LCCB 생존자 대원을 만났다. 또한 소드가 살아있다는 반가운 사실도 전해주었다. 이제 파일럿이 겪은 이야기를 들어봐야 할 때이다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10514].desc
   limit: do 200 znaków
   EN: We met an LCCB survivor who called himself Pilot. He shared a very good news with us—that Saude was alive! It's time to listen to what he's got to say.
   PL: Spotkaliśmy ocalałego agenta LCCB o pseudonimie Pilot, który przekazał nam radosną wieść: Saude żyje! Pora wysłuchać jego relacji.
1123. [Rozdziały, etapy i zdolności Dantego [10515] — tytuł] 아이스크림
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].title
   limit: do 40 znaków
   EN: Ice Cream
   PL: Lody
1124. [Rozdziały, etapy i zdolności Dantego [10515] — miejsce] U사 청새치 항구선
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].place
   (powtórzenie elementu 1091 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1125. [Rozdziały, etapy i zdolności Dantego [10515] — opis] 파일럿으로부터 황금가지가 마지막으로 목격되었다고 하는 로보토미 지부의 변동 좌표를 전달받았다. 아무렇지 않게 말을 이어가던 파일럿은 결국 눈물을 보인다. 부디 앞으로 향할 로보토미 지부에 생존자가 남아있기를 간절히 믿고 싶었다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10515].desc
   limit: do 350 znaków
   EN: Pilot handed us the variable coordinates to the Lobotomy Corp. Branch where the Golden Bough was last seen. Pilot, who so far has been trying to appear nonchalant, broke into tears. I really wanted to believe that there are survivors at the upcoming Lobotomy Corp. Branch.
   PL: Pilot przekazał nam zmienne współrzędne filii Lobotomy Corp., w której po raz ostatni widziano Złotą Gałąź. Choć próbował nadrabiać miną, w końcu zalał się łzami. Z całego serca chciałem wierzyć, że na miejscu zastaniemy jeszcze żywych ocalałych.
1126. [Rozdziały, etapy i zdolności Dantego [10516] — tytuł] 해적들
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].title
   limit: do 40 znaków
   EN: Pirates
   PL: Piraci
1127. [Rozdziały, etapy i zdolności Dantego [10516] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1128. [Rozdziały, etapy i zdolności Dantego [10516] — opis] 파일럿이 전달해 준 변동 좌표를 토대로 호수 어딘가에 있을 로보토미 지부를 향해 가야 한다.  이스마엘은 초조한 표정으로 계속 망원경을 연신 확인하고 있다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10516].desc
   limit: do 220 znaków
   EN: We have to make our way to the Lobotomy Corp. Branch based on the variable coordinates that Pilot gave us. Meanwhile, Ishmael keeps nervously checking the telescope.
   PL: Kierując się zmiennymi współrzędnymi od Pilota, płyniemy ku filii Lobotomy Corp. gdzieś na wodach Jeziora. Ishmael z napięciem na twarzy co chwilę spogląda przez lunetę.
1129. [Rozdziały, etapy i zdolności Dantego [10517] — tytuł] 해적들 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].title
   limit: do 40 znaków
   EN: Pirates 2
   PL: Piraci 2
1130. [Rozdziały, etapy i zdolności Dantego [10517] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1131. [Rozdziały, etapy i zdolności Dantego [10517] — opis] 쌍갈고리 해적단들이 우리를 뒤쫓고 있었다. 이스마엘의 제안에 따라 우리가 먼저 그들의 배로 넘어가기로 했다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10517].desc
   limit: do 160 znaków
   EN: The Twinhook Pirates were tailing us. I decided to follow Ishmael's advice and board their ship first before they did ours.
   PL: Na ogonie siedzieli nam Piraci Podwójnego Haka. Za radą Ishmael postanowiliśmy pierwsi wedrzeć się na ich pokład.
1132. [Rozdziały, etapy i zdolności Dantego [10518] — tytuł] 파도
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].title
   limit: do 40 znaków
   EN: The Waves
   PL: Fale
1133. [Rozdziały, etapy i zdolności Dantego [10518] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1134. [Rozdziały, etapy i zdolności Dantego [10518] — opis] 해적들을 물리쳤지만 찝찝함이 가시지 않는다. 호수의 규칙을 유념하며 계속 항해를 하는 수밖에…
   źródło: StageNode-a1c5p1.json :: dataList[id=10518].desc
   limit: do 200 znaków
   EN: We defeated the Pirates, but... I can't shake this uneasy feeling. Well, no choice but to continue our voyage while minding the laws of the Great Lake.
   PL: Odparliśmy piratów, lecz niepokój nie ustępuje. Pozostaje nam płynąć dalej, bacznie przestrzegając praw Wielkiego Jeziora…
1135. [Rozdziały, etapy i zdolności Dantego [10519] — tytuł] 파도 2
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].title
   limit: do 40 znaków
   EN: The Waves 2
   PL: Fale 2
1136. [Rozdziały, etapy i zdolności Dantego [10519] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1137. [Rozdziały, etapy i zdolności Dantego [10519] — opis] 오티스는 시간을 단축하기 위해 규칙을 어기고 파도를 이겨내자고 했다. 곧바로 날씨는 험악해지고 무엇일지 모르는 파도가 밀려온다.
   źródło: StageNode-a1c5p1.json :: dataList[id=10519].desc
   limit: do 220 znaków
   EN: Outis suggested that we break the laws of the Great Lake and sail headfirst into the Waves. The sky immediately darkens, and the unknown Waves begin crashing into us.
   PL: Aby zyskać na czasie, Outis zaproponowała złamanie praw Jeziora i przebicie się prosto przez Fale. Niebo natychmiast pociemniało, a naprzeciw ruszył ku nam nieznany żywioł.

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p2
- plik gry: `StageNode-a1c5p2.json`

1138. [Rozdziały, etapy i zdolności Dantego [10520] — tytuł] 크루즈 파티
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].title
   limit: do 40 znaków
   EN: Cruise Party
   PL: Przyjęcie na Wycieczkowcu
1139. [Rozdziały, etapy i zdolności Dantego [10520] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1140. [Rozdziały, etapy i zdolności Dantego [10520] — opis] 파도를 헤치고 나와, 조금은 잔잔한 항해를 시작했다.\n이제 좌표를 향해 순항할 수 있을까, 그런 생각도 잠시.\n호수 가운데 덩그러니 놓여져 있는 크루즈 선박이 눈에 띈다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10520].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We finally made it out of the Waves and into calmer seas.\nI briefly wondered if we can finally start smooth-sailing toward the coordinates...\n... and that's when I noticed a stationary cruise ship floating in the middle of a Lake.
   PL: Przedarliśmy się przez Fale na spokojniejsze wody.\nPrzez chwilę łudziłem się, że dalej pożeglujemy już bez przeszkód…\n…gdy na środku Jeziora dostrzegłem dryfujący nieruchomo wycieczkowiec.
1141. [Rozdziały, etapy i zdolności Dantego [10521] — tytuł] 크루즈 파티 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].title
   limit: do 40 znaków
   EN: Cruise Party 2
   PL: Przyjęcie na Wycieczkowcu 2
1142. [Rozdziały, etapy i zdolności Dantego [10521] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].place
   limit: do 40 znaków
   EN: Cruise Ship
   PL: Statek Wycieczkowy
1143. [Rozdziały, etapy i zdolności Dantego [10521] — opis] 정보를 얻기 위해 크루즈 위로 올랐다. 화려한 음식과 치장과는 다르게 사람 한 명 보이지 않는 것이, 어쩐지 서늘한 기운을 느끼게한다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10521].desc
   limit: do 230 znaków
   EN: We boarded the cruise ship to gather some intel. Though it's littered with gaudy decorations, I don't see anyone on board... Something about this whole affair is creeping me out.
   PL: Weszliśmy na pokład wycieczkowca w poszukiwaniu informacji. Wśród wystawnych potraw i dekoracji nie widać żywej duszy, od czego po plecach przebiega chłodny dreszcz.
1144. [Rozdziały, etapy i zdolności Dantego [10522] — tytuł] 크루즈 파티 3
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].title
   limit: do 40 znaków
   EN: Cruise Party 3
   PL: Przyjęcie na Wycieczkowcu 3
1145. [Rozdziały, etapy i zdolności Dantego [10522] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].place
   (powtórzenie elementu 1142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1146. [Rozdziały, etapy i zdolności Dantego [10522] — opis] 무서운 이야기를 피해 도망간 싱클레어를 찾아 선실 내부로 들어갔다. 싱클레어는 어렵지 않게 발견할 수 있었다.\n그런데…
   źródło: StageNode-a1c5p2.json :: dataList[id=10522].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I ran into the cabins of the ship in search of Sinclair, who fled from Hong Lu's scary tales. Thankfully, I was able to find him without much trouble.\nBut...
   PL: Wszedłem pod pokład w poszukiwaniu Sinclaira, który uciekł przed strasznymi opowieściami Hong Lu. Odnalezienie go nie sprawiło trudności.\nJednakże…
1147. [Rozdziały, etapy i zdolności Dantego [10523] — tytuł] 크루즈 파티 4
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].title
   limit: do 40 znaków
   EN: Cruise Party 4
   PL: Przyjęcie na Wycieczkowcu 4
1148. [Rozdziały, etapy i zdolności Dantego [10523] — miejsce] 크루즈 선박
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].place
   (powtórzenie elementu 1142 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1149. [Rozdziały, etapy i zdolności Dantego [10523] — opis] 크루즈는 희생의 결과물이었다. 호수 위에서 규칙을 소홀히 한 죄는 이토록 무거웠다.\n…다음 번에는 좀 더 현명한 판단을 해야할 것 같다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10523].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Cruise was an aftermath of a devastation. The consequences of breaking the laws of the Great Lake were severe.\n... I'll have to be more careful from now on.
   PL: Wycieczkowiec okazał się pomnikiem rzezi. Cena zlekceważenia praw Wielkiego Jeziora była przerażająca.\n…Następnym razem muszę podejmować rozważniejsze decyzje.
1150. [Rozdziały, etapy i zdolności Dantego [10524] — tytuł] 재앙
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].title
   limit: do 40 znaków
   EN: The Calamity
   PL: Kataklizm
1151. [Rozdziały, etapy i zdolności Dantego [10524] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].place
   limit: do 60 znaków
   EN: Abandoned Lobotomy Corp. Drilling Ship
   PL: Opuszczony Statek Wiertniczy Lobotomy Corp.
1152. [Rozdziały, etapy i zdolności Dantego [10524] — opis] 안개 너머로 보이는 것은 그토록 찾던 U사의 로보토미 지부였다. 정말 저것이 지부인지 되물을 정도로 기괴한 흰 점막이 지부의 전체를 뒤덮고 있다는 것 만 빼면… 우린 나쁘지 않은 과정 속에 있는 것만 같았다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10524].desc
   limit: do 280 znaków
   EN: The elusive Lobotomy Corp. Branch of U Corp. finally appeared from beyond the veil of mist. But... it was completely covered under a layer of bizarre, white membrane. I think we're on the correct path, at least...
   PL: Zza zasłony mgły wyłoniła się wreszcie poszukiwana filia Lobotomy Corp. w U Corp. Gdyby nie dziwaczna biała błona pokrywająca całą konstrukcję, mógłbym uznać, że wszystko idzie zgodnie z planem…
1153. [Rozdziały, etapy i zdolności Dantego [10525] — tytuł] 고래잡이
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].title
   limit: do 40 znaków
   EN: The Whaler
   PL: Wielorybnik
1154. [Rozdziały, etapy i zdolności Dantego [10525] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].place
   (powtórzenie elementu 1151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1155. [Rozdziały, etapy i zdolności Dantego [10525] — opis] 기괴함을 간직한 것은 단순히 외부 만의 일이 아니었다. 희고도 창백한 점막은 그 내부를 모조리 뒤덮고 있었다.\n그리고… 그런 점막을 뒤집어 쓴 채 걸어다니는 이도 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10525].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The bizarreness continued deep into the Lobotomy Corp. Branch. That white, pallid membrane was covering every inch of its interiors.\nAnd... we found those that were shambling around, wrapped under that very same membrane.
   PL: Makabryczny widok nie kończył się na poszyciu. Biała, blada błona wyścielała każdy zakamarek wnętrza.\nCo gorsza… natknęliśmy się na postacie snujące się pod warstwą tej samej tkanki.
1156. [Rozdziały, etapy i zdolności Dantego [10526] — tytuł] 호수와 나비
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly
   PL: Jezioro i Motyl
1157. [Rozdziały, etapy i zdolności Dantego [10526] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].place
   (powtórzenie elementu 1151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1158. [Rozdziały, etapy i zdolności Dantego [10526] — opis] 신비로운 분위기를 자아내는 나비를 따라, 우리는 지부의 안으로 더욱 걸어들어갔다. 그 안에는, 찰랑거리는 머리를 가진 자가 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10526].desc
   limit: do 170 znaków
   EN: We followed the mysterious butterfly deeper into the Lobotomy Corp. Branch. A man with a flowing head was waiting for us in there.
   PL: Podążając za tajemniczym motylem, zapuściliśmy się w głąb filii. W środku czekał na nas człowiek o falującej jak woda głowie.
1159. [Rozdziały, etapy i zdolności Dantego [10527] — tytuł] 호수와 나비 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly 2
   PL: Jezioro i Motyl 2
1160. [Rozdziały, etapy i zdolności Dantego [10527] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].place
   (powtórzenie elementu 1151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1161. [Rozdziały, etapy i zdolności Dantego [10527] — opis] 마치 나비가 수면 위에 잠시 앉았다 날아가듯, 림이라는 자는 꿈결같이 사라졌다. 그리고 우리는, 언젠가 보았던 익숙한 붉은 문양을 떠올린다. …다시 인어들이 몰려든다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10527].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rim disappeared from our sights like a butterfly leaving its brief respite upon the water surface. It was as though we had all awakened from a dream. From him we saw that familiar red mark. \n... The Mermaids are coming back.
   PL: Człowiek imieniem Rim zniknął jak ze snu — niczym motyl wzbijający się znad tafli wody. Pozostawił nam w pamięci znajomy czerwony znak.\n…Syreny znów nadciągają.
1162. [Rozdziały, etapy i zdolności Dantego [10529] — tytuł] 호수와 나비 3
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].title
   limit: do 40 znaków
   EN: The Lake and the Butterfly 3
   PL: Jezioro i Motyl 3
1163. [Rozdziały, etapy i zdolności Dantego [10529] — miejsce] 로보토미 지부 시추선 어딘가
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].place
   (powtórzenie elementu 1151 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1164. [Rozdziały, etapy i zdolności Dantego [10529] — opis] 림이라는 자의 말대로, 지부 안에서는 황금가지의 흔적을 찾을 수 없었다.\n…그의 말대로 고래라는 걸 찾아야만 하겠지.
   źródło: StageNode-a1c5p2.json :: dataList[id=10529].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Rim was right. We could not find even a hint of the Golden Bough from within the Lobotomy Corp. Branch.\n... We'll have to search for the Whale like he said, then.
   PL: Zgodnie ze słowami Rima wewnątrz filii nie zostało ani śladu po Złotej Gałęzi.\n…Pozostaje nam odszukać Wieloryba, o którym mówił.
1165. [Rozdziały, etapy i zdolności Dantego [10530] — tytuł] 작살
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].title
   limit: do 40 znaków
   EN: Harpoons
   PL: Harpuny
1166. [Rozdziały, etapy i zdolności Dantego [10530] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].place
   limit: do 60 znaków
   EN: Lobotomy Corp. Drilling Ship Entrance
   PL: Wejście na Statek Wiertniczy Lobotomy Corp.
1167. [Rozdziały, etapy i zdolności Dantego [10530] — opis] 베르길리우스와 합류를 대기하려는데, 갑작스러운 충격이 지부를 덮쳤다. 황급히 외부로 나가 안개 속을 쳐다보았더니… 그 안개로부터 험상궂은 선박이 고개를 내밀기 시작했다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10530].desc
   limit: do 230 znaków
   EN: We were waiting by the entrance when a sudden shock shook the Lobotomy Corp. Branch. We hurried out and gazed into the mists... and saw several intimidating-looking vessels emerge.
   PL: Czekaliśmy na dołączenie Wergiliusza, gdy całą placówką wstrząsnęło uderzenie. Wybiegliśmy na zewnątrz i ujrzeliśmy groźnie wyglądające jednostki wyłaniające się z mgły.
1168. [Rozdziały, etapy i zdolności Dantego [10532] — tytuł] 작은 형님
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].title
   limit: do 40 znaków
   EN: The Big Brother
   PL: Starszy Brat
1169. [Rozdziały, etapy i zdolności Dantego [10532] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].place
   (powtórzenie elementu 1166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1170. [Rozdziały, etapy i zdolności Dantego [10532] — opis] 습격한 해적들을 처리하고 있었지만, 이들은 그저 전초전에 불과하다는 생각이 불현듯 스쳤다. 그러고보면, 아직 저들의 선박 중 가장 화려하고 커다란 것은 우리에게 갈고리를 걸지 않았었는데…
   źródło: StageNode-a1c5p2.json :: dataList[id=10532].desc
   limit: do 290 znaków
   EN: We were making relatively short work of the ambushing pirates, but I had a feeling that they were just gauging our capabilities... Now that I mention it, the largest and gaudiest vessel from their fleet has yet to hook us.
   PL: Sprawnie odpierałem nacierających piratów, lecz przemknęło mi przez myśl, że to zaledwie zwiad. Największy i najbardziej okazały okręt ich floty wciąż nie zarzucił na nas haków…
1171. [Rozdziały, etapy i zdolności Dantego [10533] — tytuł] 작은 형님 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].title
   limit: do 40 znaków
   EN: The Big Brother 2
   PL: Starszy Brat 2
1172. [Rozdziały, etapy i zdolności Dantego [10533] — miejsce] 로보토미 지부 시추선 입구
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].place
   (powtórzenie elementu 1166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1173. [Rozdziały, etapy i zdolności Dantego [10533] — opis] 이건 일종의 유린이나 기만에 가깝다. 이스마엘은 계속해서 죽고, 나는 그 죽음의 고통을 공유하며 끊임없이 되살린다.\n…승리는 요원하다. 정말 파우스트가 말한 대로… 여기서 끝이 나는 걸까.
   źródło: StageNode-a1c5p2.json :: dataList[id=10533].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is nothing short of a massacre. A humiliation. He kills Ishmael again and again. I keep bringing her back, feeling that very same pain that killed her.\n... This battle is lost. Maybe Faust is right... Maybe this is where our journey ends.
   PL: To nie walka, lecz rzeź i upokorzenie. Ishmael ginie raz po raz, a ja dzielę ból każdej jej śmierci, przywracając ją do życia.\n…Nie mamy szans na zwycięstwo. Czy tak, jak mówiła Faust, tutaj kończy się nasza podróż?
1174. [Rozdziały, etapy i zdolności Dantego [10534] — tytuł] 쪽빛노인
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].title
   limit: do 40 znaków
   EN: The Indigo Elder
   PL: Starzec Indygo
1175. [Rozdziały, etapy i zdolności Dantego [10534] — miejsce] 메피스토펠레스 버스배
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].place
   (powtórzenie elementu 1082 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1176. [Rozdziały, etapy i zdolności Dantego [10534] — opis] 푸른 불꽃이 올라오는 담배를 물고 있는 노인은, 설명을 들을 필요도 없이 강력했다. 파우스트는 이미 이 자가 누구인지 아는 듯이, 가벼운 인사와 함께 그를 베르길리우스에게로 데려갔다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10534].desc
   limit: do 320 znaków
   EN: Blue embers flickered from the old man's cigar. We didn't need anyone to tell us that he was overwhelmingly powerful; we knew instinctively. Faust, who seemed to recognize the old man, led him to Vergilius after a quick exchange of pleasantries.
   PL: Starzec z cygarem tlącym się błękitnym płomieniem emanował potęgą niewymagającą żadnych słów. Faust, wyraźnie wiedząc, kim jest nieznajomy, po krótkim powitaniu zaprowadziła go do Wergiliusza.
1177. [Rozdziały, etapy i zdolności Dantego [10535] — tytuł] 암초
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].title
   limit: do 40 znaków
   EN: Rocks
   PL: Rafy
1178. [Rozdziały, etapy i zdolności Dantego [10535] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].place
   limit: do 40 znaków
   EN: Mephistopheles' Skiff
   PL: Szalupa Mefistofelesa
1179. [Rozdziały, etapy i zdolności Dantego [10535] — opis] 쪽빛노인과 의논한 대로, 우리는 회색빛 호수를 향해 노를 저어갔다. 탁하고 흐린 호수의 물결 위로, 희끄무레한 암초 같은 것들이 멀찍하게 보인다. 저것들을 피하면서 지나가야 하는 건가.
   źródło: StageNode-a1c5p2.json :: dataList[id=10535].desc
   limit: do 270 znaków
   EN: We rowed toward the gray Lake as we previously discussed with the Indigo Elder. We can see some rocks poking out of the pale, opaque waters of the Lake. Looks like we'll have to maneuver our way between them.
   PL: Zgodnie z ustaleniami ze Starcem Indygo wiosłowaliśmy w stronę szarego Jeziora. Ponad mętną taflą majaczyły białawe kształty przypominające rafy, między którymi musieliśmy ostrożnie lawirować.
1180. [Rozdziały, etapy i zdolności Dantego [10537] — tytuł] 창백한 고래
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].title
   limit: do 40 znaków
   EN: The Pallid Whale
   PL: Blady Wieloryb
1181. [Rozdziały, etapy i zdolności Dantego [10537] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].place
   (powtórzenie elementu 1178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1182. [Rozdziały, etapy i zdolności Dantego [10537] — opis] 암초라고 생각했던 구멍 고래 위로 흘러나오는 인어들을 해치워냈다. 하지만… 우리가 찾는 고래는 이게 아닐텐데, 이스마엘이 이렇게 한 이유가 뭘까?\n히스클리프의 안색을 보아하니… 나만 궁금한 건 아닌 것 같다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10537].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: What we thought to be a rock was a Porous Whale. When its Mermaids crawled out of the holes, we defeated them. But... This isn't the Whale we're looking for, is it? What is Ishmael thinking?\nI could tell from the look on Heathcliff's face that I wasn't the only one wondering about this.
   PL: Domniemana rafa okazała się Dziurawym Wielorybem, z którego otworów wypełzły Syreny. Rozprawiliśmy się z nimi, lecz… to przecież nie tego Wieloryba szukamy. Co chodzi po głowie Ishmael?\nSądząc po minie Heathcliffa, nie tylko ja zachodziłem w głowę.
1183. [Rozdziały, etapy i zdolności Dantego [10538] — tytuł] 창백한 고래 2
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].title
   limit: do 40 znaków
   EN: The Pallid Whale 2
   PL: Blady Wieloryb 2
1184. [Rozdziały, etapy i zdolności Dantego [10538] — miejsce] 메피스토펠레스 보트
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].place
   (powtórzenie elementu 1178 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1185. [Rozdziały, etapy i zdolności Dantego [10538] — opis] 걷혀진 해무를 비집고, 우리는 새카만 호수의 안으로 들어왔다.\n이스마엘이 말하는, 전설 속의 호수. 그리고 그 안에는…\n시릴 정도로 창백한 고래가 있었다.
   źródło: StageNode-a1c5p2.json :: dataList[id=10538].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: We waded past the ocean mist and entered the obsidian Lake.\nThe Lake of legends, as told by Ishmael. Within it...\n... Was the Pallid Whale, pale as the midnight moon.
   PL: Przebiwszy się przez morską mgłę, wpłynęliśmy na kruczoczarne Jezioro.\nJezioro z legend opowiadanych przez Ishmael. A pośród jego wód…\n…czekał przejmująco Blady Wieloryb.

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c5p3
- plik gry: `StageNode-a1c5p3.json`

1186. [Rozdziały, etapy i zdolności Dantego [10539] — tytuł] 칠흑 속으로
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].title
   limit: do 40 znaków
   EN: Into the Dark
   PL: W Kruczą Czerń
1187. [Rozdziały, etapy i zdolności Dantego [10539] — miejsce] 창백한 고래
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].place
   (powtórzenie elementu 1180 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
1188. [Rozdziały, etapy i zdolności Dantego [10539] — opis] 걷혀진 해무를 비집고, 우리는 새카만 호수의 안으로 들어왔다.\n이스마엘이 말하는, 전설 속의 호수. 그리고 그 안에는…\n시릴 정도로 창백한 고래가 있었다.
   źródło: StageNode-a1c5p3.json :: dataList[id=10539].desc
   (powtórzenie elementu 1185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p1
- plik gry: `StageNode-a1c6p1.json`

1189. [Rozdziały, etapy i zdolności Dantego [10601] — tytuł] 워더링하이츠
   źródło: StageNode-a1c6p1.json :: dataList[id=10601].title
   limit: do 40 znaków
   EN: Wuthering Heights
   PL: Wichrowe Wzgórza
1190. [Rozdziały, etapy i zdolności Dantego [10602] — tytuł] 시간이 없어
   źródło: StageNode-a1c6p1.json :: dataList[id=10602].title
   limit: do 40 znaków
   EN: There's no TIME
   PL: Nie ma CZASU
1191. [Rozdziały, etapy i zdolności Dantego [10603] — tytuł] 시간이 없어 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10603].title
   limit: do 40 znaków
   EN: There's no TIME 2
   PL: Nie ma CZASU 2
1192. [Rozdziały, etapy i zdolności Dantego [10604] — tytuł] 편지
   źródło: StageNode-a1c6p1.json :: dataList[id=10604].title
   limit: do 40 znaków
   EN: The Letter
   PL: List
1193. [Rozdziały, etapy i zdolności Dantego [10605] — tytuł] 색깔
   źródło: StageNode-a1c6p1.json :: dataList[id=10605].title
   limit: do 40 znaków
   EN: Colours
   PL: Barwy
1194. [Rozdziały, etapy i zdolności Dantego [10606] — tytuł] 단장
   źródło: StageNode-a1c6p1.json :: dataList[id=10606].title
   limit: do 40 znaków
   EN: The Makeover
   PL: Przemiana
1195. [Rozdziały, etapy i zdolności Dantego [10607] — tytuł] 대문
   źródło: StageNode-a1c6p1.json :: dataList[id=10607].title
   limit: do 40 znaków
   EN: The Front Gate
   PL: Brama Główna
1196. [Rozdziały, etapy i zdolności Dantego [10608] — tytuł] 넬리
   źródło: StageNode-a1c6p1.json :: dataList[id=10608].title
   limit: do 40 znaków
   EN: Nelly
   PL: Nelly
1197. [Rozdziały, etapy i zdolności Dantego [10609] — tytuł] 환영 인사
   źródło: StageNode-a1c6p1.json :: dataList[id=10609].title
   limit: do 40 znaków
   EN: A Warm Reception
   PL: Gorące Powitanie
1198. [Rozdziały, etapy i zdolności Dantego [10610] — tytuł] 캐서린
   źródło: StageNode-a1c6p1.json :: dataList[id=10610].title
   limit: do 40 znaków
   EN: Catherine
   PL: Catherine
1199. [Rozdziały, etapy i zdolności Dantego [10611] — tytuł] 버틀러
   źródło: StageNode-a1c6p1.json :: dataList[id=10611].title
   limit: do 40 znaków
   EN: Butlers
   PL: Kamerdynerzy
1200. [Rozdziały, etapy i zdolności Dantego [10612] — tytuł] 유령
   źródło: StageNode-a1c6p1.json :: dataList[id=10612].title
   limit: do 40 znaków
   EN: The Ghost
   PL: Zjawa
1201. [Rozdziały, etapy i zdolności Dantego [10613] — tytuł] 수수께끼
   źródło: StageNode-a1c6p1.json :: dataList[id=10613].title
   limit: do 40 znaków
   EN: Riddles
   PL: Zagadki
1202. [Rozdziały, etapy i zdolności Dantego [10614] — tytuł] 복도
   źródło: StageNode-a1c6p1.json :: dataList[id=10614].title
   limit: do 40 znaków
   EN: The Corridor
   PL: Korytarz
1203. [Rozdziały, etapy i zdolności Dantego [10615] — tytuł] 복도 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10615].title
   limit: do 40 znaków
   EN: The Corridor 2
   PL: Korytarz 2
1204. [Rozdziały, etapy i zdolności Dantego [10616] — tytuł] 복도 3
   źródło: StageNode-a1c6p1.json :: dataList[id=10616].title
   limit: do 40 znaków
   EN: The Corridor 3
   PL: Korytarz 3
1205. [Rozdziały, etapy i zdolności Dantego [10617] — tytuł] 데드레빗츠
   źródło: StageNode-a1c6p1.json :: dataList[id=10617].title
   limit: do 40 znaków
   EN: The Dead Rabbits
   PL: Martwe Króliki
1206. [Rozdziały, etapy i zdolności Dantego [10618] — tytuł] 데드레빗츠 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10618].title
   limit: do 40 znaków
   EN: The Dead Rabbits 2
   PL: Martwe Króliki 2
1207. [Rozdziały, etapy i zdolności Dantego [10619] — tytuł] 일기장
   źródło: StageNode-a1c6p1.json :: dataList[id=10619].title
   limit: do 40 znaków
   EN: The Diary
   PL: Pamiętnik
1208. [Rozdziały, etapy i zdolności Dantego [10620] — tytuł] 일기장 2
   źródło: StageNode-a1c6p1.json :: dataList[id=10620].title
   limit: do 40 znaków
   EN: The Diary 2
   PL: Pamiętnik 2
1209. [Rozdziały, etapy i zdolności Dantego [10621] — tytuł] 벽난로
   źródło: StageNode-a1c6p1.json :: dataList[id=10621].title
   limit: do 40 znaków
   EN: The Fireplace
   PL: Kominek

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p2
- plik gry: `StageNode-a1c6p2.json`

1210. [Rozdziały, etapy i zdolności Dantego [10622] — tytuł] 깊고 깊은 지하실
   źródło: StageNode-a1c6p2.json :: dataList[id=10622].title
   limit: do 40 znaków
   EN: Abyssal Basement
   PL: Bezgłębna Piwnica
1211. [Rozdziały, etapy i zdolności Dantego [10623] — tytuł] 깊고 깊은 지하실 2
   źródło: StageNode-a1c6p2.json :: dataList[id=10623].title
   limit: do 40 znaków
   EN: Abyssal Basement 2
   PL: Bezgłębna Piwnica 2
1212. [Rozdziały, etapy i zdolności Dantego [10624] — tytuł] 유리관
   źródło: StageNode-a1c6p2.json :: dataList[id=10624].title
   limit: do 40 znaków
   EN: Glass Pods
   PL: Szklane Kapsuły
1213. [Rozdziały, etapy i zdolności Dantego [10625] — tytuł] 모조품
   źródło: StageNode-a1c6p2.json :: dataList[id=10625].title
   limit: do 40 znaków
   EN: Imitations
   PL: Imitacje
1214. [Rozdziały, etapy i zdolności Dantego [10626] — tytuł] 모조품 2
   źródło: StageNode-a1c6p2.json :: dataList[id=10626].title
   limit: do 40 znaków
   EN: Imitations 2
   PL: Imitacje 2
1215. [Rozdziały, etapy i zdolności Dantego [10627] — tytuł] 모조품 3
   źródło: StageNode-a1c6p2.json :: dataList[id=10627].title
   limit: do 40 znaków
   EN: Imitations 3
   PL: Imitacje 3
1216. [Rozdziały, etapy i zdolności Dantego [10628] — tytuł] 그리웠던 얼굴
   źródło: StageNode-a1c6p2.json :: dataList[id=10628].title
   limit: do 40 znaków
   EN: Nostalgic Face
   PL: Stęskniona Twarz
1217. [Rozdziały, etapy i zdolności Dantego [10629] — tytuł] 모조품 4
   źródło: StageNode-a1c6p2.json :: dataList[id=10629].title
   limit: do 40 znaków
   EN: Imitations 4
   PL: Imitacje 4
1218. [Rozdziały, etapy i zdolności Dantego [10630] — tytuł] 잘못 끼워진 단추
   źródło: StageNode-a1c6p2.json :: dataList[id=10630].title
   limit: do 40 znaków
   EN: Where It All Went Wrong
   PL: Źle Zapięty Guzik
1219. [Rozdziały, etapy i zdolności Dantego [10631] — tytuł] 검은색의 풀
   źródło: StageNode-a1c6p2.json :: dataList[id=10631].title
   limit: do 40 znaków
   EN: Obsidian Grass
   PL: Czarna Trawa
1220. [Rozdziały, etapy i zdolności Dantego [10632] — tytuł] 바이올린
   źródło: StageNode-a1c6p2.json :: dataList[id=10632].title
   limit: do 40 znaków
   EN: Violin
   PL: Skrzypce
1221. [Rozdziały, etapy i zdolności Dantego [10633] — tytuł] 매트
   źródło: StageNode-a1c6p2.json :: dataList[id=10633].title
   limit: do 40 znaków
   EN: Matt
   PL: Matt
1222. [Rozdziały, etapy i zdolności Dantego [10634] — tytuł] 짐승
   źródło: StageNode-a1c6p2.json :: dataList[id=10634].title
   limit: do 40 znaków
   EN: The Beast
   PL: Bestia

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c6p3
- plik gry: `StageNode-a1c6p3.json`

1223. [Rozdziały, etapy i zdolności Dantego [10635] — tytuł] 시계 소리
   źródło: StageNode-a1c6p3.json :: dataList[id=10635].title
   limit: do 40 znaków
   EN: Ticking Sounds
   PL: Tykanie Zegara
1224. [Rozdziały, etapy i zdolności Dantego [10636] — tytuł] 이사벨라
   źródło: StageNode-a1c6p3.json :: dataList[id=10636].title
   limit: do 40 znaków
   EN: Isabella
   PL: Isabella
1225. [Rozdziały, etapy i zdolności Dantego [10637] — tytuł] 피뢰침
   źródło: StageNode-a1c6p3.json :: dataList[id=10637].title
   limit: do 40 znaków
   EN: Lightning Rod
   PL: Piorunochron
1226. [Rozdziały, etapy i zdolności Dantego [10638] — tytuł] 와일드헌트
   źródło: StageNode-a1c6p3.json :: dataList[id=10638].title
   limit: do 40 znaków
   EN: The Wild Hunt
   PL: Dziki Gon
1227. [Rozdziały, etapy i zdolności Dantego [10639] — tytuł] 와일드헌트 2
   źródło: StageNode-a1c6p3.json :: dataList[id=10639].title
   limit: do 40 znaków
   EN: The Wild Hunt 2
   PL: Dziki Gon 2
1228. [Rozdziały, etapy i zdolności Dantego [10640] — tytuł] 와일드헌트 3
   źródło: StageNode-a1c6p3.json :: dataList[id=10640].title
   limit: do 40 znaków
   EN: The Wild Hunt 3
   PL: Dziki Gon 3
1229. [Rozdziały, etapy i zdolności Dantego [10641] — tytuł] 끝도 없이 막힌 길
   źródło: StageNode-a1c6p3.json :: dataList[id=10641].title
   limit: do 40 znaków
   EN: Impenetrable Path
   PL: Droga bez Przejścia
1230. [Rozdziały, etapy i zdolności Dantego [10642] — tytuł] 옥상으로
   źródło: StageNode-a1c6p3.json :: dataList[id=10642].title
   limit: do 40 znaków
   EN: To The Rooftop
   PL: Na Dach
1231. [Rozdziały, etapy i zdolności Dantego [10643] — tytuł] 황금가지
   źródło: StageNode-a1c6p3.json :: dataList[id=10643].title
   limit: do 40 znaków
   EN: The Golden Bough
   PL: Złota Gałąź
1232. [Rozdziały, etapy i zdolności Dantego [10644] — tytuł] 마왕
   źródło: StageNode-a1c6p3.json :: dataList[id=10644].title
   limit: do 40 znaków
   EN: Erlking
   PL: Król Olch
1233. [Rozdziały, etapy i zdolności Dantego [10645] — tytuł] 도둑맞은 삶
   źródło: StageNode-a1c6p3.json :: dataList[id=10645].title
   limit: do 40 znaków
   EN: Life, Stolen
   PL: Skradzione Życie
1234. [Rozdziały, etapy i zdolności Dantego [10646] — tytuł] 사랑한다는 말
   źródło: StageNode-a1c6p3.json :: dataList[id=10646].title
   limit: do 40 znaków
   EN: Expression of Love
   PL: Wyznanie Miłości
1235. [Rozdziały, etapy i zdolności Dantego [10647] — tytuł] 같은 마음
   źródło: StageNode-a1c6p3.json :: dataList[id=10647].title
   limit: do 40 znaków
   EN: Hearts Unbroken
   PL: Jedno Serce
1236. [Rozdziały, etapy i zdolności Dantego [10648] — tytuł] 모든 세계
   źródło: StageNode-a1c6p3.json :: dataList[id=10648].title
   limit: do 40 znaków
   EN: Every World
   PL: Każdy ze Światów

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c7p1
- plik gry: `StageNode-a1c7p1.json`

1237. [Rozdziały, etapy i zdolności Dantego [10701] — tytuł] 유명하진 않지만 용감한 돈키호테의 일상과 의뢰에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10701].title
   limit: do 110 znaków
   EN: WHICH TREATS THE LIFE AND THE CONTRACTS OF THE NOT-SO-FAMOUS-BUT-VALIANT DON QUIXOTE
   PL: O CODZIENNOŚCI I ZLECENIACH NIEZBYT SŁAWNEJ, LECZ DZIELNEJ DON QUIXOTE
1238. [Rozdziały, etapy i zdolności Dantego [10702] — tytuł] 림버스컴퍼니가 처음은 아니지만 날개와 협력하는 것에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10702].title
   limit: do 100 znaków
   EN: IN WHICH IS EXPLORED LIMBUS COMPANY'S NOT-EXACTLY-FIRST ALLIANCE WITH A WING
   PL: O TYM, JAK LIMBUS COMPANY PO RAZ NIEZUPEŁNIE PIERWSZY ZE SKRZYDŁEM WSPÓŁPRACUJE
1239. [Rozdziały, etapy i zdolności Dantego [10703] — tytuł] 수감자들이 도시의 방법으로 해결사에게 인정받는 것에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10703].title
   limit: do 100 znaków
   EN: WHEREIN THE SINNERS ARE ACCEPTED AND RESPECTED BY FIXERS IN WAYS OF THE CITY
   PL: O TYM, JAK GRZESZNICY OBYCZAJEM MIASTA UZNANIE WŚRÓD FIKSERÓW ZDOBYWAJĄ
1240. [Rozdziały, etapy i zdolności Dantego [10704] — tytuł] 붉은시선 품에서 벗어난 우리에게 일어난 일들에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10704].title
   limit: do 100 znaków
   EN: OF WHAT BEFELL OUR COMPANY UPON OUR DEPARTURE FROM THE RED GAZE'S HANDS
   PL: O TYM, CO NAS SPOTKAŁO PO OPUSZCZENIU PIECZY CZERWONEGO SPOJRZENIA
1241. [Rozdziały, etapy i zdolności Dantego [10705] — tytuł] 여기에서는 우리의 도련님이 겪어온 이야기가 밝혀진다
   źródło: StageNode-a1c7p1.json :: dataList[id=10705].title
   limit: do 70 znaków
   EN: IN WHICH THE TALE OF OUR YOUNG MASTER IS REVEALED
   PL: W KTÓRYM WYJAWIONA ZOSTAJE PRZESZŁOŚĆ NASZEGO PANICZA
1242. [Rozdziały, etapy i zdolności Dantego [10706] — tytuł] 섕크가 우리의 해결사에게 행한 어마어마한 결투에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10706].title
   limit: do 100 znaków
   EN: OF THE IMMENSELY DEVASTATING DUEL IN WHICH OUR FIXER AND THE CINQ BATTLED
   PL: O STRASZLIWYM POJEDYNKU, KTÓRY CINQ Z NASZĄ FIKSERKĄ STOCZYŁO
1243. [Rozdziały, etapy i zdolności Dantego [10707] — tytuł] 우리의 훌륭한 정보원 LCD 부서의 두번째 연락에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10707].title
   limit: do 170 znaków
   EN: OF THE EXCELLENT DIALOGUE IN WHICH OUR EXCEPTIONAL INFORMANT LCD DEPARTMENT HAS PASSED INTEL TO US IN OUR SECOND COMMUNICATION
   PL: O DRUGIEJ ROZMOWIE Z NASZYM ZNAKOMITYM INFORMATOREM Z DZIAŁU LCD
1244. [Rozdziały, etapy i zdolności Dantego [10708] — tytuł] 버스 기사의 놀이공원과 관리자의 유쾌한 약속에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10708].title
   limit: do 130 znaków
   EN: IN WHICH IS DISCUSSED THE MERRY OATH OF THE BUS DRIVER AND THE MANAGER CONCERNING AMUSEMENT PARKS
   PL: O WESOŁEJ OBIETNICY MIĘDZY KIEROWCĄ AUTOBUSU A KIEROWNIKIEM W SPRAWIE WESOŁEGO MIASTECZKA
1245. [Rozdziały, etapy i zdolności Dantego [10709] — tytuł] 여기에서는 용감무쌍한 해결사들의 토벌에 결말이 난다
   źródło: StageNode-a1c7p1.json :: dataList[id=10709].title
   limit: do 150 znaków
   EN: WHEREIN IS CONCLUDED THE METHOD BY WHICH ERADICATION QUEST OF FIXERS, THE BRAVE AND THE BOLD, ARE TO BE CONDUCTED
   PL: W KTÓRYM ROZSTRZYGA SIĘ SPOSÓB PRZEPROWADZENIA WYPRAWY DZIELNYCH FIKSERÓW
1246. [Rozdziały, etapy i zdolności Dantego [10710] — tytuł] 라만차랜드의 사건과 혈귀와의 만남에서 생긴 위험에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10710].title
   limit: do 120 znaków
   EN: OF WHAT PERIL BEFELL US IN THE CASE OF LA MANCHALAND AND OUR ENCOUNTER WITH THE BLOODFIENDS
   PL: O NIEBEZPIECZEŃSTWACH W LA MANCHALANDZIE I SPOTKANIU Z KRWIOŻERCAMI
1247. [Rozdziały, etapy i zdolności Dantego [10711] — tytuł] 림버스컴퍼니와 돈키호테에게 일어난 전투에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10711].title
   limit: do 100 znaków
   EN: WHEREIN IS DISCUSSED THE BATTLE THAT FOUND LIMBUS COMPANY AND DON QUIXOTE
   PL: O BITWIE, KTÓRA STAŁA SIĘ UDZIAŁEM LIMBUS COMPANY I DON QUIXOTE
1248. [Rozdziały, etapy i zdolności Dantego [10712] — tytuł] 쓰러진 혈귀들이 들려주려다 실패한 이야기에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10712].title
   limit: do 120 znaków
   EN: OF THE TALE WHICH THE FALLEN BLOODFIENDS HAVE FAILED TO TELL, DESPITE THEIR BEST ENDEAVORS
   PL: O OPOWIEŚCI, KTÓREJ POLEGLI KRWIOŻERCY MIMO STARAŃ DOKOŃCZYĆ NIE ZDOŁALI
1249. [Rozdziały, etapy i zdolności Dantego [10713] — tytuł] 여기에서는 어트랙션의 내레이션과 퀴즈가 이어진다
   źródło: StageNode-a1c7p1.json :: dataList[id=10713].title
   limit: do 80 znaków
   EN: IN WHICH THE ATTRACTION'S NARRATION AND ITS RIDDLES CONTINUE
   PL: W KTÓRYM TRWAJĄ DALEJ NARRACJA ATRAKCJI ORAZ ZAGADKI
1250. [Rozdziały, etapy i zdolności Dantego [10714] — tytuł] 여기에서는 혈귀와 관련된 뜻밖의 사실들을 이야기한다
   źródło: StageNode-a1c7p1.json :: dataList[id=10714].title
   limit: do 90 znaków
   EN: WHEREIN IS LEARNED THE UNEXPECTED TRUTHS REGARDING BLOODFIENDS
   PL: W KTÓRYM MOWA O NIESPODZIEWANYCH FAKTACH DOTYCZĄCYCH KRWIOŻERCÓW
1251. [Rozdziały, etapy i zdolności Dantego [10715] — tytuł] 여기에서는 라만차랜드에 대한 수감자의 감상을 이야기한다
   źródło: StageNode-a1c7p1.json :: dataList[id=10715].title
   limit: do 90 znaków
   EN: WHEREIN THE SINNERS EACH SHARE THEIR IMPRESSIONS OF LA MANCHALAND
   PL: W KTÓRYM GRZESZNICY DZIELĄ SIĘ WRAŻENIAMI Z LA MANCHALANDU
1252. [Rozdziały, etapy i zdolności Dantego [10716] — tytuł] 해결사 돈키호테가 동료라고 믿은 사람이 벌인 일에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10716].title
   limit: do 120 znaków
   EN: IN WHICH ARE DISCUSSED THE DEEDS OF THE FIXER WHOM DON QUIXOTE HAD BELIEVED TO BE A FRIEND
   PL: O CZYNACH TEJ, KTÓRĄ FIKSERKA DON QUIXOTE ZA TOWARZYSZKĘ UWAŻAŁA
1253. [Rozdziały, etapy i zdolności Dantego [10717] — tytuł] 여기에서는 돈키호테가 과거에 겪은 수많은 모험담이 계속된다
   źródło: StageNode-a1c7p1.json :: dataList[id=10717].title
   limit: do 90 znaków
   EN: WHEREIN THE NUMEROUS TALES OF DON QUIXOTE'S ADVENTURES ARE RECOUNTED
   PL: W KTÓRYM CIĄGNĄ SIĘ LICZNE DAWNE PRZYGODY DON QUIXOTE
1254. [Rozdziały, etapy i zdolności Dantego [10718] — tytuł] 맘브리노 투구를 탈취한 모험과 주어진 배역들에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10718].title
   limit: do 110 znaków
   EN: OF THE ADVENTURE TO LAY CLAIM UPON THE HELM OF MAMBRINO AND THE ROLES THAT ARE GIVEN
   PL: O WYPRAWIE PO HEŁM MAMBRINA ORAZ ROZDANYCH ROLACH
1255. [Rozdziały, etapy i zdolności Dantego [10719] — tytuł] 관리자와 나눈 분별 있는 이야기와 마술사에 대하여
   źródło: StageNode-a1c7p1.json :: dataList[id=10719].title
   limit: do 110 znaków
   EN: OF THE VERY NICE DISCUSSION THAT WAS HAD BETWEEN THE MANAGER AND THE MAGICIAN
   PL: O ROZWAŻNEJ ROZMOWIE KIEROWNIKA Z ILUZJONISTĄ

## Rozdziały, etapy i zdolności Dantego: StageNode-a1c7p2
- plik gry: `StageNode-a1c7p2.json`

1256. [Rozdziały, etapy i zdolności Dantego [10720] — tytuł] 여기에서는 유령의 집에 대한 수감자들의 감상이 이어진다
   źródło: StageNode-a1c7p2.json :: dataList[id=10720].title
   limit: do 100 znaków
   EN: WHEREIN THE SINNERS EACH SHARE THEIR IMPRESSIONS OF THE HAUNTED MANSION
   PL: W KTÓRYM GRZESZNICY DZIELĄ SIĘ WRAŻENIAMI Z NAWIEDZONEGO DOMU
1257. [Rozdziały, etapy i zdolności Dantego [10721] — tytuł] '헌티드 블러디 메리' 유령의 집인지 혈귀의 집인지와 맞닥뜨린 수감자들의 모험에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10721].title
   limit: do 230 znaków
   EN: IN WHICH IS RECOUNTED THE SINNERS' ADVENTURE IN THE ENCOUNTER WITH 'HAUNTED: BLOODY MARY', THE NATURE OF WHICH IS UNCLEAR WHETHER IT IS A HAUNTED MANSION OR A BLOODFIENDS' DEN
   PL: O PRZYGODZIE GRZESZNIKÓW W PRZYBYTKU „NAWIEDZONA KRWAWA MARY”, CO DO KTÓREGO NIE WIADOMO, CZY JEST DOMEM DUCHÓW, CZY SIEDLISKIEM KRWIOŻERCÓW
1258. [Rozdziały, etapy i zdolności Dantego [10722] — tytuł] 숨어있던 혈귀들과 앞서 지나간 해결사들에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10722].title
   limit: do 110 znaków
   EN: WHEREIN IS DISCUSSED THE BLOODFIENDS IN HIDING AND THE FIXERS WHO ARRIVED FIRST
   PL: O UKRYTYCH KRWIOŻERCACH ORAZ FIKSERACH, KTÓRZY PRZESZLI TĘDY PIERWSI
1259. [Rozdziały, etapy i zdolności Dantego [10723] — tytuł] 여기에서는 <쓸쓸했던 왕과 행복했던 가족>을 들려준다
   źródło: StageNode-a1c7p2.json :: dataList[id=10723].title
   limit: do 120 znaków
   EN: HERE IT IS RECOUNTED THE TALE OF <THE FORLORN KING AND THE FAMILY THAT WAS ONCE HAPPY>
   PL: W KTÓRYM OPOWIEDZIANA ZOSTAJE HISTORIA „SAMOTNY KRÓL I NIEGDYŚ SZCZĘŚLIWA RODZINA”
1260. [Rozdziały, etapy i zdolności Dantego [10724] — tytuł] 회개하는 혈귀들과 기이한 설문조사에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10724].title
   limit: do 70 znaków
   EN: OF THE PENITENT BLOODFIENDS AND THE BIZARRE SURVEY
   PL: O KAJĄCYCH SIĘ KRWIOŻERCACH I OSOBLIWEJ ANKIECIE
1261. [Rozdziały, etapy i zdolności Dantego [10725] — tytuł] 만일 주의 깊게 본다면 알게 될 사실을 산손이 미리 말하는 일에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10725].title
   limit: do 140 znaków
   EN: IN WHICH A TRUTH THAT MAY BE REVEALED BY CLOSE INSPECTION IS SPOILED BY NONE OTHER THAN SANSÓN HIMSELF
   PL: O TYM, JAK SANSÓN ZDRADZA Z GÓRY FAKT DOSTRZEGALNY DLA UWAŻNEGO OKA
1262. [Rozdziały, etapy i zdolności Dantego [10726] — tytuł] 하얀 달의 기사와 용감한 돈키호테의 치열한 전투에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10726].title
   limit: do 140 znaków
   EN: WHICH RECOUNTS THE CLOSE AND DRAMATIC DUEL BETWEEN THE KNIGHT OF THE WHITE MOON AND THE VALIANT DON QUIXOTE
   PL: O ZAŻARTYM BOJU MIĘDZY RYCERZEM BIAŁEGO KSIĘŻYCA A DZIELNĄ DON QUIXOTE
1263. [Rozdziały, etapy i zdolności Dantego [10727] — tytuł] 산손의 연극에 다가온 뻔한 결말에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10727].title
   limit: do 70 znaków
   EN: OF THE PREDICTABLE ENDING TO SANSÓN'S STAGEPLAY
   PL: O PRZEWIDYWALNYM ZAKOŃCZENIU SZTUKI SANSONA
1264. [Rozdziały, etapy i zdolności Dantego [10728] — tytuł] 가시춘의 의문과 질문에 대한 수감자들의 그냥저냥한 대답에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10728].title
   limit: do 80 znaków
   EN: OF JIA XICHUN'S QUERY AND THE SINNER'S LUKEWARM ANSWERS
   PL: O PYTANIU JIA XICHUN ORAZ LETNICH ODPOWIEDZIACH GRZESZNIKÓW
1265. [Rozdziały, etapy i zdolności Dantego [10729] — tytuł] 에밀 싱클레어의 걱정과 돈키호테의 착각에 대하여
   źródło: StageNode-a1c7p2.json :: dataList[id=10729].title
   limit: do 100 znaków
   EN: IN WHICH IS DISCUSSED EMIL SINCLAIR'S CONCERNS AND DON QUIXOTE'S DELUSIONS
   PL: O OBAWACH EMILA SINCLAIRA I ZŁUDZENIACH DON QUIXOTE
