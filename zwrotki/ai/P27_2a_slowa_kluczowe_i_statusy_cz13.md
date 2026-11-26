# Paczka AI P27 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 13/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P27_2a_slowa_kluczowe_i_statusy_cz13.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P27_2a_slowa_kluczowe_i_statusy_cz13.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Statusy i efekty bojowe — Bufs
- plik gry: `Bufs.json`

1. [Status [VioletResultDown] — opis] 이번 턴 동안 질투 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=VioletResultDown].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy Skill Final Power -{0} for this turn.
   PL: W tej turze Moc Końcowa Umiejętności Zazdrości -{0}
2. [Status [VioletResultDown] — podsumowanie] 질투 속성 스킬의 최종 위력 -{0}
   źródło: Bufs.json :: dataList[id=VioletResultDown].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Envy Skill Final Power -{0}
   PL: Moc Końcowa Umiejętności Zazdrości -{0}
3. [Status [VibrationCollapse] — nazwa] 진동 - 붕괴
   źródło: Bufs.json :: dataList[id=VibrationCollapse].name
   kontekst: identyfikator statusu w tekstach: `[VibrationCollapse]`
   limit: do 40 znaków
   EN: Tremor - Decay
   PL: Wstrząs - Rozpad
4. [Status [VibrationCollapse] — opis] 대상의 진동 위력 4 당 방어 레벨 1 감소\n{1}턴 동안 진동 폭발 스킬로 피격 시 {0}만큼 흐트러짐 손상\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationCollapse].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Lose 1 Defense Level for every 4 Tremor Potency on self\nFor {1} turns: when Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by {0}\n(Interacts the same way as normal Tremor does to effects that raises or reduces Tremor Potency/Count)
   PL: Poziom Obrony maleje o 1 za każde 4 Mocy Wstrząsu celu\nPrzez {1} tur przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Wstrząsu)
5. [Status [VibrationCollapse] — podsumowanie] 대상의 진동 위력 4 당 방어 레벨 1 감소\n{0}만큼 흐트러짐 손상
   źródło: Bufs.json :: dataList[id=VibrationCollapse].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Lose 1 Defense Level for every 4 Tremor Potency on self\nRaise Stagger Threshold by {0}
   PL: Poziom Obrony maleje o 1 za każde 4 Mocy Wstrząsu celu\nPróg Oszołomienia rośnie o {0}
6. [Status [EchoOfMansion] — nazwa] 저택의 메아리
   źródło: Bufs.json :: dataList[id=EchoOfMansion].name
   kontekst: identyfikator statusu w tekstach: `[EchoOfMansion]`
   limit: do 40 znaków
   EN: Echoes of the Manor
   PL: Echa Rezydencji
7. [Status [EchoOfMansion] — opis] - 스킬, 코인의 효과로 침잠 위력이나 횟수가 부여될 때, 50% 확률로 침잠 횟수 1 증가\n- 정신력이 있는 대상인 경우, 패닉 유형이 '저택의 메아리'로 변경되고, 패닉이 되면 다음 턴에 자신을 제외한 같은 팀의 무작위 캐릭터 2명에게 저택의 메아리 2 부여\n- 정신력이 없는 대상인 경우, 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=EchoOfMansion].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - 50% chance to gain +1 Sinking Count when gaining Sinking Potency or Count from Skill or Coin effects\n- SP Units: Change Panic Type to Echoes of the Manor. When this unit Panics, inflict 2 Echoes of the Manor to 2 random other allies of this unit next turn\n- Non-SP Units: -10% chance to flip Heads\n- Reduce by 1 at Turn End
   PL: - Przy nadawaniu Mocy lub Licznika Zatonięcia przez efekt Umiejętności lub Monety, 50% szans na +1 Licznika Zatonięcia\n- Jednostki z Poczytalnością: zmienia typ Paniki na „Echa Posiadłości”; przy Panice w następnej turze nadaje 2 Echa Posiadłości 2 losowym innym sojusznikom\n- Jednostki bez Poczytalności: szansa na Awersy -10%\n- Na koniec tury maleje o 1
8. [Status [EchoOfMansion_Main] — nazwa] 저택의 메아리
   źródło: Bufs.json :: dataList[id=EchoOfMansion_Main].name
   kontekst: identyfikator statusu w tekstach: `[EchoOfMansion_Main]`
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
9. [Status [EchoOfMansion_Main] — opis] - 스킬, 코인의 효과로 침잠 위력이나 횟수가 부여될 때, 50% 확률로 침잠 횟수 1 증가\n- 패닉 유형이 '저택의 메아리'로 변경됨.\n- 패닉이 되면 다음 턴에 자신을 제외한 같은 팀의 무작위 캐릭터 2명에게 저택의 메아리 2 부여\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=EchoOfMansion_Main].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - 50% chance to gain +1 Sinking Count when gaining Sinking Potency or Count from Skill or Coin effects\n- Change this unit's Panic Type to Echoes of the Manor.\n- When this unit Panics, inflict 2 Echoes of the Manor to 2 random other allies of this unit\n- Reduced by 1 at Turn End
   PL: - Przy nadawaniu Mocy lub Licznika Zatonięcia przez efekt Umiejętności lub Monety, 50% szans na +1 Licznika Zatonięcia\n- Zmienia typ Paniki na „Echa Posiadłości”.\n- Przy Panice w następnej turze nadaje 2 Echa Posiadłości 2 losowym innym sojusznikom\n- Na koniec tury maleje o 1
10. [Status [EchoOfMansion_Sub] — nazwa] 저택의 메아리
   źródło: Bufs.json :: dataList[id=EchoOfMansion_Sub].name
   kontekst: identyfikator statusu w tekstach: `[EchoOfMansion_Sub]`
   (powtórzenie elementu 6 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
11. [Status [EchoOfMansion_Sub] — opis] - 스킬, 코인의 효과로 침잠 위력이나 횟수가 부여될 때, 50% 확률로 침잠 횟수 1 증가\n- 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=EchoOfMansion_Sub].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - 50% chance to gain +1 Sinking Count when gaining Sinking Potency or Count from Skill or Coin effects\n- -10% chance to flip Heads\n- Reduce by 1 at Turn End
   PL: - Przy nadawaniu Mocy lub Licznika Zatonięcia przez efekt Umiejętności lub Monety, 50% szans na +1 Licznika Zatonięcia\n- Szansa na Awersy -10%\n- Maleje o 1 na koniec tury
12. [Status [VibrationCrack] — nazwa] 진동 - 균열
   źródło: Bufs.json :: dataList[id=VibrationCrack].name
   kontekst: identyfikator statusu w tekstach: `[VibrationCrack]`
   limit: do 40 znaków
   EN: Tremor - Fracture
   PL: Wstrząs - Pęknięcie
13. [Status [VibrationCrack] — opis] - 흐트러짐 상태가 되었을 때, 자신의 진동 위력과 횟수의 합이 20 이상이면, 흐트러짐 단계 1 증가\n- 해당 효과로 최대 흐트러짐 단계를 초과할 수 없음\n{1}턴 동안 진동 폭발 스킬로 피격 시 {0}만큼 흐트러짐 손상\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationCrack].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: - When Staggered, and when the sum of Tremor Potency and Count adds up to 20 or higher, raise Stagger Level by 1\n- Cannot exceed maximum Stagger Level with this effect\nWhen hit by attacks that trigger Tremor Burst, raise the Stagger Threshold by {0}. Lasts {1} turns\n(Interacts the same way as normal Tremor does to effects that raises or reduces Tremor Potency/Count)
   PL: - W stanie Oszołomienia, przy sumie Mocy i Licznika Wstrząsu wynoszącej 20 lub więcej, Poziom Oszołomienia rośnie o 1\n- Ten efekt nie może przekroczyć maksymalnego Poziomu Oszołomienia\nPrzez {1} tur przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Wstrząsu)
14. [Status [VibrationCrack] — podsumowanie] 흐트러짐 상태가 되었을 때, 진동 위력과 횟수의 합이 20 이상이면, 흐트러짐 단계 1 증가\n{0}만큼 흐트러짐 손상
   źródło: Bufs.json :: dataList[id=VibrationCrack].summary
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: When Staggered, and when the sum of Tremor Potency and Count adds up to 20 or higher, raise Stagger Level by 1\nRaise Stagger Threshold by {0}
   PL: W stanie Oszołomienia, przy sumie Mocy i Licznika Wstrząsu wynoszącej 20 lub więcej, Poziom Oszołomienia rośnie o 1\nPróg Oszołomienia rośnie o {0}
15. [Status [ForwardToTheKing] — nazwa] 왕의 앞으로
   źródło: Bufs.json :: dataList[id=ForwardToTheKing].name
   kontekst: identyfikator statusu w tekstach: `[ForwardToTheKing]`
   limit: do 40 znaków
   EN: Before the King
   PL: Przed Królem
16. [Status [ForwardToTheKing] — opis] 자신의 공격 적중 시 코인 결과 값의 50%만큼 동일한 대상이 아닌 공격 가능한 적 중 체력이 가장 낮은 적 2명에게 공격한 스킬의 속성과 같은 속성의 피해를 준다.
   źródło: Bufs.json :: dataList[id=ForwardToTheKing].desc
   limit: do 230 znaków
   EN: On Hit, inflict 50% of the resulting Coin value On Hit as (Affinity/Attack Type of the Attack Skill used to hit) damage against 2 other attackable enemies with the least HP.
   PL: Przy trafieniu własnym atakiem zadaje 50% wartości wyniku Monety jako obrażenia atrybutu atakowanej Umiejętności 2 innym możliwym do zaatakowania wrogom (nie temu samemu celowi) o najniższym HP.
17. [Status [ForwardToTheBoundKing] — nazwa] 묶인 왕의 앞으로
   źródło: Bufs.json :: dataList[id=ForwardToTheBoundKing].name
   kontekst: identyfikator statusu w tekstach: `[ForwardToTheBoundKing]`
   limit: do 40 znaków
   EN: Before the King in Binds
   PL: Przed Królem w Spętaniu
18. [Status [ForwardToTheBoundKing] — opis] 자신의 공격 적중 시 코인 결과 값의 100%만큼 동일한 대상이 아닌 공격 가능한 적 중 체력이 가장 낮은 적 2명에게 공격한 스킬의 속성과 같은 속성의 피해를 준다.
   źródło: Bufs.json :: dataList[id=ForwardToTheBoundKing].desc
   limit: do 230 znaków
   EN: On Hit, inflict 100% of the resulting Coin value On Hit as (Affinity/Attack Type of the Attack Skill used to hit) damage against 2 other attackable enemies with the least HP.
   PL: Przy trafieniu własnym atakiem zadaje 100% wartości wyniku Monety jako obrażenia atrybutu atakowanej Umiejętności 2 innym możliwym do zaatakowania wrogom (nie temu samemu celowi) o najniższym HP.
19. [Status [Switch_Vibration] — nazwa] 진폭 변환
   źródło: Bufs.json :: dataList[id=Switch_Vibration].name
   kontekst: identyfikator statusu w tekstach: `[Switch_Vibration]`
   limit: do 40 znaków
   EN: Amplitude Conversion
   PL: Konwersja Amplitudy
20. [Status [Switch_Vibration] — opis] 대상의 진동과 변경된 진동을 다른 유형의 진동으로 변경함.\n변경 시 기존 진동의 위력, 횟수가 유지됨.
   źródło: Bufs.json :: dataList[id=Switch_Vibration].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Converts Tremor or already converted Tremor on target to a different type of Tremor.\nPotency and Count values do not change over the conversion.
   PL: Zamienia Wstrząs lub już przekształcony Wstrząs celu w inny rodzaj Wstrząsu.\nMoc i Licznik pozostają bez zmian.
21. [Status [MarkOfButler] — nazwa] 버.표
   źródło: Bufs.json :: dataList[id=MarkOfButler].name
   kontekst: identyfikator statusu w tekstach: `[MarkOfButler]`
   limit: do 40 znaków
   EN: B.M.
   PL: Oznaczenie Kamerdynera
22. [Status [MarkOfButler] — opis] 이 효과가 있는 대상에게 에드가 가문 치프 버틀러 료슈의 스킬이 강화됨.\n턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=MarkOfButler].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Enhances Edgar Family Chief Butler Ryōshū Skills against targets with this effect.\nReduced by 1 at Turn End
   PL: Wzmacnia Umiejętności Ryośu, Głównej Kamerdynerki Rodziny Edgara, przeciwko celom z tym efektem.\nNa koniec tury maleje o 1
23. [Status [LibrarianOfHistoryNormal] — nazwa] 역사의 층 보조 사서
   źródło: Bufs.json :: dataList[id=LibrarianOfHistoryNormal].name
   kontekst: identyfikator statusu w tekstach: `[LibrarianOfHistoryNormal]`
   limit: do 50 znaków
   EN: Assistant Librarian of History
   PL: Asystent Bibliotekarza Piętra Historii
24. [Status [LibrarianOfHistoryNormal] — opis] - 해당 캐릭터의 슬롯 +1\n-턴 시작 시 정신력 15 회복\n- 자신이 스킬로 부여하는 화상, 출혈, 파열, 침잠, 진동의 위력, 횟수가 2배로 부여됨. (특수 상태이상에도 적용)
   źródło: Bufs.json :: dataList[id=LibrarianOfHistoryNormal].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Heal 15 SP at Turn Start\n- Inflicts double the amount of Potency & Count for Burn, Bleed, Rupture, Sinking, and Tremor. (applies to 'Unique' Status effects as well)
   PL: - Liczba slotów Umiejętności +1\n- Na początek tury odzyskuje 15 Poczytalności\n- Podwaja nadawaną przez Umiejętności Moc i Licznik Podpalenia, Krwawienia, Rozdarcia, Zatonięcia i Wstrząsu (dotyczy również stanów „Specjalnych”)
25. [Status [PreparedMeat] — nazwa] 준비된 고기
   źródło: Bufs.json :: dataList[id=PreparedMeat].name
   kontekst: identyfikator statusu w tekstach: `[PreparedMeat]`
   limit: do 40 znaków
   EN: Prepared Meat
   PL: Przygotowane Mięso
26. [Status [PreparedMeat] — opis] 조건이 만족되면 턴 종료 시 여왕 요정이 이 캐릭터를 처치함
   źródło: Bufs.json :: dataList[id=PreparedMeat].desc
   limit: do 120 znaków
   EN: If conditions are met, Fairy Queen kills this unit at Turn End
   PL: Jeśli warunki zostaną spełnione, Królowa Wróżek zabija tę jednostkę na koniec tury
27. [Status [Hunger] — nazwa] 굶주림
   źródło: Bufs.json :: dataList[id=Hunger].name
   kontekst: identyfikator statusu w tekstach: `[Hunger]`
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
28. [Status [Hunger] — opis] 턴 종료 시 준비된 고기가 부여된 아군을 처치하지 못했으면 1 증가\n체력이 75% 미만이면, 2 증가, 체력이 50% 미만이면, 3 증가.\n턴 시작 시 준비된 고기가 부여된 아군을 처치했으면 1 감소.\n이후 수치가 0이면, 공격 위력 감소, 수비 위력 감소를 (이번 턴에 처치한 아군 수 x 3)만큼 얻음.
   źródło: Bufs.json :: dataList[id=Hunger].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: gain 1 if this unit failed to defeat an ally with Prepared Meat.\nAt 75%- HP, gain 2. At 50%- HP, gain 3.\nTurn Start: lose 1 if this unit defeated an ally with Prepared Meat.\nAt 0 value, gain (# of allies defeated x 3)Attack Power Down and Defense Power Down.
   PL: Na koniec tury zyskuje 1, jeśli nie pokonał sojusznika z Przygotowanym Mięsem.\nPrzy HP poniżej 75% zyskuje 2; przy HP poniżej 50% zyskuje 3.\nNa początku tury traci 1, jeśli pokonał sojusznika z Przygotowanym Mięsem.\nPrzy wartości 0 zyskuje (liczba pokonanych sojuszników x 3) Spadków Mocy Ataku i Spadków Mocy Obrony
29. [Status [UnstableFeeling] — nazwa] 불안정한 격정
   źródło: Bufs.json :: dataList[id=UnstableFeeling].name
   kontekst: identyfikator statusu w tekstach: `[UnstableFeeling]`
   limit: do 40 znaków
   EN: Volatile Passion
   PL: Niestabilne Namiętności
30. [Status [UnstableFeeling] — opis] - 공격 적중 시 화상 1 부여\n- 메인 타겟에게 화상이 있으면 최종 위력 +1\n- 수비 스킬을 연결하고 전투를 시작하면, 해당 턴동안 피격 시 공격자에게 화상 1 부여\n- 턴 종료 시 정신력이 {0} x 5만큼 감소.(최대 정신력 감소량 : 40)
   źródło: Bufs.json :: dataList[id=UnstableFeeling].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - On Hit, inflict 1 Burn\n- If the main target has Burn, Final Power +1\n- If this unit has a Defense Skill chained at Combat Start, inflict 1 Burn per hit against the attacker for the turn\n- Turn End: lose ({0} x 5) SP. (Max SP loss : 40)
   PL: - Przy trafieniu nadaje Podpalenie 1\n- Jeśli główny cel posiada Podpalenie, Moc Końcowa +1\n- Jeśli rozpoczyna walkę z połączoną Umiejętnością obrony, przez tę turę nadaje atakującemu Podpalenie 1 przy każdym trafieniu\n- Na koniec tury traci {0} x 5 Poczytalności (maks. utraty: 40)
31. [Status [LibrarianOfHistoryHard] — nazwa] 역사의 층 사서
   źródło: Bufs.json :: dataList[id=LibrarianOfHistoryHard].name
   kontekst: identyfikator statusu w tekstach: `[LibrarianOfHistoryHard]`
   limit: do 40 znaków
   EN: Librarian of History
   PL: Bibliotekarz Piętra Historii
32. [Status [LibrarianOfHistoryHard] — opis] - 해당 캐릭터의 슬롯 +1\n- 턴 시작 시 정신력 15 회복\n- 자신이 스킬로 부여하는 화상, 출혈, 파열, 침잠, 진동의 위력, 횟수가 2배로 부여됨. (특수 상태이상에도 적용)\n- 적이 사망하면, 자신을 포함하여 정신력이 가장 낮은 아군 2명 정신력 25 회복.\n- 적 처치시 적을 처치한 속성의 EGO 자원 +2, 모든 속성의 EGO 자원 +1
   źródło: Bufs.json :: dataList[id=LibrarianOfHistoryHard].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Heal 15 SP at Turn Start\n- Inflicts double the amount of Potency & Count for Burn, Bleed, Rupture, Sinking, and Tremor. (applies to 'Unique' Status effects as well)\n- When an enemy is defeated, 2 allies(including this unit) with the least SP heal 25 SP.\n- On Kill, gain +2 E.G.O resource for the Affinity that defeated the enemy; +1 to all E.G.O resources
   PL: - Liczba slotów Umiejętności +1\n- Na początek tury odzyskuje 15 Poczytalności\n- Podwaja nadawaną przez Umiejętności Moc i Licznik Podpalenia, Krwawienia, Rozdarcia, Zatonięcia i Wstrząsu (dotyczy również stanów „Specjalnych”)\n- Gdy wróg ginie, 2 sojusznicy (wliczając tę jednostkę) z najniższą Poczytalnością odzyskują 25 Poczytalności.\n- Przy zabiciu: +2 zasobów E.G.O atrybutu, który zabił wroga; +1 wszystkich zasobów E.G.O
33. [Status [PriceOfCare] — nazwa] 채워지지 않는 허기
   źródło: Bufs.json :: dataList[id=PriceOfCare].name
   kontekst: identyfikator statusu w tekstach: `[PriceOfCare]`
   limit: do 40 znaków
   EN: Bottomless Hunger
   PL: Nienasycony Głód
34. [Status [PriceOfCare] — opis] 잡아먹은 요정 덩이의 수 : {0}
   źródło: Bufs.json :: dataList[id=PriceOfCare].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Fairy Mass Devoured: {0}
   PL: Liczba pożartych Zgraj Wróżek: {0}
35. [Status [VibrationEcho] — nazwa] 진동 - 반향
   źródło: Bufs.json :: dataList[id=VibrationEcho].name
   kontekst: identyfikator statusu w tekstach: `[VibrationEcho]`
   limit: do 40 znaków
   EN: Tremor - Reverb
   PL: Wstrząs - Rezonans
36. [Status [VibrationEcho] — opis] - {1} 턴 동안 진동 폭발 시 {0}만큼 나태 피해를 입음.\n- {1} 턴 동안 진동 폭발 스킬로 피격 시, {0}만큼 흐트러짐 손상.\n- 턴 종료 시 횟수 1 감소.\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationEcho].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: - For {1} Turns: On Tremor Burst, take {0} Sloth damage.\n- For {1} Turns: When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by {0}.\n- Turn End: reduce the Count by 1.\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przez {1} tur przy Wyładowaniu Wstrząsu otrzymuje {0} obrażeń Lenistwa.\n- Przez {1} tur przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu Próg Oszołomienia rośnie o {0}.\n- Na koniec tury Licznik maleje o 1.\n(Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Wstrząsu)
37. [Status [ShieldManagerCryingToad] — nazwa] 울음 방울
   źródło: Bufs.json :: dataList[id=ShieldManagerCryingToad].name
   kontekst: identyfikator statusu w tekstach: `[ShieldManagerCryingToad]`
   limit: do 40 znaków
   EN: Blubberbubble
   PL: Pękająca Bańka
38. [Status [ShieldManagerCryingToad] — opis] - 이 효과는 보호막 관리 효과로 취급됨.\n- 턴 종료 시, 1 감소\n- 울음 방울 효과가 적용되는 동안 턴 종료 시 보호막이 사라지지 않음 (피해나 효과에 의해 사라지는 경우는 제외).\n- 울음 방울 효과가 적용된 보호막이 피격을 받아 파괴될 경우, 공격한 대상에게 침잠 위력과 침잠 횟수를 합하여 4만큼 무작위로 부여.\n- 보호막 수치는 중첩 가능하며, 울음 방울 효과가 적용 중인 경우에는 보호막의 수치가 보호막 적용 대상의 최대 체력 60%를 넘을 수 없음.
   źródło: Bufs.json :: dataList[id=ShieldManagerCryingToad].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This effect counts as a 'Shield Management' effect.\n- Turn End: Reduce Count by 1\n- This unit does not lose Shield at Turn End as long as it has the Blubberbubble effect (unless depleted by damage or effect)\n- If the Shield affected by Blubberbubble breaks due to taking damage, inflict 4 Sinking Potency/Count against the attacker. (How much of that '4' value is Potency or Count is randomly determined)\n- This unit can stack their Shield value by using this effect. However, as long as Blubberbubble is in effect, the Shield value cannot exceed 60% of this unit's Max HP.
   PL: - Efekt zarządzania Tarczą\n- Na koniec tury maleje o 1\n- Podczas działania tego efektu Tarcza nie znika na koniec tury (poza przypadkami utraty od obrażeń lub efektów)\n- Gdy Tarcza objęta tym efektem pęknie od otrzymanych obrażeń, nadaje atakującemu łącznie 4 jednostek Mocy/Licznika Zatonięcia w losowym podziale\n- Wartość Tarczy można kumulować tym efektem; podczas jego działania Tarcza nie może przekroczyć 60% Maks. HP celu
39. [Status [VibrationContinue] — nazwa] 진동 - 영속
   źródło: Bufs.json :: dataList[id=VibrationContinue].name
   kontekst: identyfikator statusu w tekstach: `[VibrationContinue]`
   limit: do 40 znaków
   EN: Tremor - Everlasting
   PL: Wstrząs - Wieczność
40. [Status [VibrationContinue] — opis] - 스킬, 코인 효과로 진동 폭발 시 자신의 (진동 위력)% 확률로 진동 폭발 1회 추가 발동. (최대 50%)\n- 스킬, 코인 효과로 진동 폭발 시 자신의 (진동 횟수)% 확률로 진동 폭발 1회 추가 발동. (최대 50%)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소.\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationContinue].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When hit by Skills or Coin effects that trigger Tremor Burst, (Tremor Potency on self)% chance to trigger an additional Tremor Burst. (max 50%)\n- When hit by Skills or Coin effects that trigger Tremor Burst, (Tremor Count on self)% chance to trigger an additional Tremor Burst. (max 50%)\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy trafieniu Umiejętnościami lub monetami wyzwalającymi Wybuch Wstrząsu: szansa równa (Moc Wstrząsu)% na dodatkowy Wybuch Wstrząsu. (maks. 50%)\n- Przy trafieniu Umiejętnościami lub monetami wyzwalającymi Wybuch Wstrząsu: szansa równa (Licznik Wstrząsu)% na dodatkowy Wybuch Wstrząsu. (maks. 50%)\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
41. [Status [TimeSuspend] — nazwa] 시간 유예
   źródło: Bufs.json :: dataList[id=TimeSuspend].name
   kontekst: identyfikator statusu w tekstach: `[TimeSuspend]`
   limit: do 40 znaków
   EN: Time Moratorium
   PL: Zawieszenie Czasu
42. [Status [TimeSuspend] — opis] - 이 효과가 있는 동안 모든 피해를 받지 않고 저장함\n- 전투 종료 시 횟수가 1이면, {3}만큼 나태 피해를 입히고 진동 폭발 {0}회 발동.\n- 턴 종료 시 위력 1 증가, 횟수 1 감소\n- 시간 유예가 적용된 대상에게 시간 유예를 추가로 부여 시, 시간 유예의 나태 피해와 진동 폭발 효과가 즉시 발동하고 버프 해제\n- 저장된 피해량: {2}
   źródło: Bufs.json :: dataList[id=TimeSuspend].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: {3}, {0}, {2}, \n
   EN: - Does not take any damage as long as this effect is active; store all damage received instead\n- Combat End: If there is only 1 Count left of this effect, the effect triggers {0} Tremor Burst(s) after dealing {3} Sloth damage.\n- Turn End: Gain 1 Stack and lose 1 Count\n- The Time Moratorium will immediately expire after triggering the Tremor Burst and the Sloth damage effect if another instance of Time Moratorium is inflicted on a unit that has Time Moratorium.\n- Stored damage: {2}
   PL: - Dopóki efekt jest aktywny, nie otrzymuje obrażeń, lecz je magazynuje\n- Po zakończeniu walki, przy Liczniku równym 1, zadaje {3} obrażeń Lenistwem i wywołuje Wybuch Wstrząsu {0} razy.\n- Na koniec tury wartość rośnie o 1, a Licznik maleje o 1\n- Nadanie kolejnego Zawieszenia Czasu jednostce, która je posiada, natychmiast uruchamia efekt obrażeń Lenistwem i Wybuch Wstrząsu, po czym wzmocnienie znika\n- Magazynowane obrażenia: {2}
43. [Status [TimeRentalTwoPersonality] — nazwa] 시간 대여
   źródło: Bufs.json :: dataList[id=TimeRentalTwoPersonality].name
   kontekst: identyfikator statusu w tekstach: `[TimeRentalTwoPersonality]`
   limit: do 40 znaków
   EN: Borrowed Time
   PL: Pożyczony Czas
44. [Status [TimeRentalTwoPersonality] — opis] 턴 종료 시 횟수가 2 이상이면,\n- 다음 턴에 신속, 합 위력 증가, 취약 {1}만큼 얻음\n- 다음 턴에 얻을 신속보다 속박이 많을 경우, 다음 턴 시작 시 시간 대여 해제, 흐트러짐 상태가 됨\n턴 종료 시 횟수가 1이면, 다음 턴에 속박 {0} 얻음\n턴 종료 시 위력 1 증가, 횟수 1 감소
   źródło: Bufs.json :: dataList[id=TimeRentalTwoPersonality].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: {1}, {0}, \n
   EN: Turn End at 2+ Count:\n- Gain {1} Haste, Clash Power Up, and Fragile next turn\n- If this unit is set to gain more Bind than Haste next turn, the Borrowed Time effect expires at the next Turn Start, and this unit gets Staggered\n\nTurn End: At 1 Count, gain {0} Bind next turn\nTurn End: Gain 1 Stack, lose 1 Count
   PL: Na koniec tury, przy Liczniku 2+:\n- W następnej turze zyskuje {1} Pośpiechu, Wzrostów Mocy Starcia i Wrażliwości\n- Jeśli w następnej turze ma otrzymać więcej Spętań niż Pośpiechu, efekt Pożyczonego Czasu znika na początku następnej tury, a jednostka zostaje oszołomiona\nNa koniec tury, przy Liczniku 1, w następnej turze zyskuje {0} Spętań\nNa koniec tury wartość rośnie o 1, a Licznik maleje o 1
45. [Status [VibrationChainPersonality] — nazwa] 진동 - 사슬
   źródło: Bufs.json :: dataList[id=VibrationChainPersonality].name
   kontekst: identyfikator statusu w tekstach: `[VibrationChainPersonality]`
   limit: do 40 znaków
   EN: Tremor - Chain
   PL: Wstrząs - Łańcuch
46. [Status [VibrationChainPersonality] — opis] - 진동 위력 10 당 합 위력 1 감소 (최대 3)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationChainPersonality].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 1 Clash Power for every 10 Tremor Potency on self (max 3)\n- When Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu (maks. 3)\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n- (Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
47. [Status [GazePersonality] — nazwa] 경멸의 시선
   źródło: Bufs.json :: dataList[id=GazePersonality].name
   kontekst: identyfikator statusu w tekstach: `[GazePersonality]`
   limit: do 40 znaków
   EN: Gaze of Contempt
   PL: Pogardliwe Spojrzenie
48. [Status [GazePersonality] — opis] - 최댓값 : 7\n- 경멸의 시선 1당 가하는 피해량 +7%\n- 턴 종료 시 효과 소멸됨\n- 턴 종료 시 경멸의 시선이 7이면, 효과가 소멸되는 대신 다음 턴에 시선의 경멸로 변환됨
   źródło: Bufs.json :: dataList[id=GazePersonality].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 7\n- Deal +7% damage for every Gaze of Contempt\n- Turn End: this effect expires\n- Turn End: At 7 Gaze of Contempt value, convert it to Contempt of the Gaze next turn instead of expiring
   PL: - Maks. wartości: 7\n- Zadaje +7% obrażeń za każde Pogardliwe Spojrzenie\n- Znika na koniec tury\n- Na koniec tury przy wartości 7 zamiast zniknięcia zamienia się w następnej turze w Pogardę Spojrzenia
49. [Status [ContemptPersonality] — nazwa] 시선의 경멸
   źródło: Bufs.json :: dataList[id=ContemptPersonality].name
   kontekst: identyfikator statusu w tekstach: `[ContemptPersonality]`
   limit: do 40 znaków
   EN: Contempt of the Gaze
   PL: Pogarda Spojrzenia
50. [Status [ContemptPersonality] — opis] - 보호 7 얻음\n- 피해량 감소 7 얻음\n- 보유 중인 스킬 슬롯 중 하나의 도발치 20 증가\n- 시선의 경멸이 유지되는 동안 경멸의 시선을 얻을 수 없음\n- 턴 종료 시 효과 소멸됨
   źródło: Bufs.json :: dataList[id=ContemptPersonality].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 7 Protection\n- Gain 7 Damage Down\n- One of this unit's Skill Slots gains +20 Aggro\n- Cannot gain Gaze of Contempt as long as Contempt of the Gaze is active\n- Turn End: this effect expires
   PL: - Zyskuje 7 Ochrony\n- Zyskuje 7 Spadków Obrażeń\n- Jeden z slotów zyskuje +20 Wartości Prowokacji\n- Dopóki aktywna jest Pogarda Spojrzenia, nie może zyskać Pogardliwego Spojrzenia\n- Na koniec tury efekt znika
51. [Status [KnowledgeTraining] — nazwa] 지식 단련
   źródło: Bufs.json :: dataList[id=KnowledgeTraining].name
   kontekst: identyfikator statusu w tekstach: `[KnowledgeTraining]`
   limit: do 40 znaków
   EN: Erudition
   PL: Biegłość Wiedzy
52. [Status [KnowledgeTraining] — opis] - 최댓값 : 6\n- 스킬을 버릴 때 자신의 최대 체력의 (지식 단련 x 1.5)%만큼의 보호막을 얻음 (턴 당 1회)\n- 탐구한 지식이 2 이상인 상태에서 스킬을 버릴 때, 합 위력 증가 1 얻음 (턴 당 1회)\n- 적에게 공격 스킬로 피격받아 체력 피해를 입을 때마다 1 감소\n- 흐트러질 시 효과 소멸됨
   źródło: Bufs.json :: dataList[id=KnowledgeTraining].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 6\n- When Discarding a Skill, gain (Erudition x 1.5)% of this unit's max HP as Shield (once per turn)\n- If this unit Discards a Skill at 2+ Insight, gain 1 Clash Power (once per turn)\n- Reduced by 1 when taking HP damage after getting hit by an enemy's Attack Skill\n- Expires when Staggered
   PL: - Maks.: 6\n- Odrzucając Umiejętność, zyskuje Tarczę równą (Biegłość x 1,5)% Maks. HP (raz na turę)\n- Odrzucając Umiejętność przy 2 lub więcej Zgłębionej Wiedzy, zyskuje 1 Wzrost Mocy Starcia (raz na turę)\n- Maleje o 1 przy każdej utracie HP od trafienia Umiejętnością ataku wroga\n- Znika po oszołomieniu
53. [Status [BoseProjektil] — nazwa] 찢어진 추억
   źródło: Bufs.json :: dataList[id=BoseProjektil].name
   kontekst: identyfikator statusu w tekstach: `[BoseProjektil]`
   limit: do 40 znaków
   EN: Torn Memory
   PL: Naderwane Wspomnienie
54. [Status [BoseProjektil] — opis] - 최댓값 : 7\n- 특정 스킬에 사용됨
   źródło: Bufs.json :: dataList[id=BoseProjektil].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value : 7\n- Used for certain Skills
   PL: - Maks.: 7\n- Zużywane przez określone Umiejętności
55. [Status [ChargeLoad] — nazwa] 부하
   źródło: Bufs.json :: dataList[id=ChargeLoad].name
   kontekst: identyfikator statusu w tekstach: `[ChargeLoad]`
   limit: do 40 znaków
   EN: Load
   PL: Obciążenie
56. [Status [ChargeLoad] — opis] - 최댓값 : 6\n- 충전 횟수를 소모한 공격 스킬의 피해량 +({0} x 2.5)% (최대 15%)\n- 효과가 부여된 대상이 W사 직원이면, 피해량 +({0} x 5)%로 적용됨. (최대 30%)\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=ChargeLoad].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Value: 6\n- Attack Skills that consumed Charge Count: deal +({0} x 2.5)% damage (max 15%)\n- If the affected unit is a W Corp. employee, deal +({0} x 5)% damage instead. (max 30%)\n- Turn End: this effect expires
   PL: - Maks. wartości: 6\n- Umiejętności ataku zużywające Licznik Ładowania zadają +({0} x 2.5)% obrażeń (maks. 15%)\n- Jeśli celem efektu jest pracownik W Corp., zamiast tego zadają +({0} x 5)% obrażeń (maks. 30%)\n- Znika na koniec tury
57. [Status [PhotoElectricity] — nazwa] 광전
   źródło: Bufs.json :: dataList[id=PhotoElectricity].name
   kontekst: identyfikator statusu w tekstach: `[PhotoElectricity]`
   limit: do 40 znaków
   EN: Photoelectricity
   PL: Fotopobudzenie
58. [Status [PhotoElectricity] — opis] 최댓값 : 3\n피격 시 공격자의 충전 횟수가 수치만큼 증가 (스킬당 1회)\n- 공격자의 충전 횟수가 5 이하면, 충전 횟수 3 추가로 얻음\n턴 종료 시 효과 소멸됨
   źródło: Bufs.json :: dataList[id=PhotoElectricity].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Value: 3\nWhen this unit is hit, the Attacker gains Charge Count equal to the value (once per Skill)\n- If the Attacker has 5- Charge Count, they gain +3 additional Charge Count\nTurn End: this effect expires
   PL: Maks.: 3\nPrzy trafieniu atakujący zyskuje Licznik Ładowania równy wartości (raz na Umiejętność)\n- Przy 5 lub mniej Liczników Ładowania atakujący dodatkowo zyskuje 3\n- Na koniec tury efekt znika
59. [Status [AaCfPaBa_Alt1] — nazwa] 끝없는 상실
   źródło: Bufs.json :: dataList[id=AaCfPaBa_Alt1].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPaBa_Alt1]`
   limit: do 40 znaków
   EN: Unending Bereavement
   PL: Niekończąca się Żałoba
60. [Status [AaCfPaBa_Alt1] — opis] 매 턴 시작 시, 정신력 5 회복\n피격 시 정신력 3 감소, 다음 턴에 공격 레벨 증가 2 얻음 (턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음
   źródło: Bufs.json :: dataList[id=AaCfPaBa_Alt1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every Turn Start: heal 5 SP\nWhen hit, lose 3 SP and gain 2 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 0 SP, gain 3 Attack Power Up
   PL: Co turę odzyskuje 5 Poczytalności\nPrzy trafieniu: -3 Poczytalności, 2 Wzrosty Poziomu Ataku w następnej turze (3 razy na turę)\nNa początek tury przy Poczytalności ujemnej: 3 Wzrosty Mocy Ataku
61. [Status [AaCfPaBa_Alt2] — nazwa] 히스클리프들의 목을 벤다
   źródło: Bufs.json :: dataList[id=AaCfPaBa_Alt2].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPaBa_Alt2]`
   limit: do 40 znaków
   EN: Behead Heathcliffs
   PL: Ścina Głowy Heathcliffów
62. [Status [AaCfPaBa_Alt2] — opis] 매 턴 시작 시, 정신력 10 회복\n피격 시 다음 턴에 공격 레벨 증가 2 얻음 (턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음
   źródło: Bufs.json :: dataList[id=AaCfPaBa_Alt2].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Every Turn Start: heal 10 SP\nWhen hit, gain 2 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 0 SP, gain 3 Attack Power Up
   PL: Co turę odzyskuje 10 Poczytalności\nPrzy trafieniu: 2 Wzrosty Poziomu Ataku w następnej turze (3 razy na turę)\nNa początek tury przy Poczytalności ujemnej: 3 Wzrosty Mocy Ataku
63. [Status [AaCfPcBa_Alt1] — nazwa] 쏟아내는 분노
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt1].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa_Alt1]`
   limit: do 40 znaków
   EN: Pouring Wrath
   PL: Wylewający Gniew
64. [Status [AaCfPcBa_Alt1] — opis] 턴 종료 시 정신력 회복 10\n피격 시 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 3회)\n턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음\n턴 시작 시 듀라한이 있다면, 피해량 증가 1, 방어 레벨 감소 3 얻음
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt1].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 10 SP\nWhen hit, gain 1 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 0 SP, gain 3 Attack Power Up\nTurn Start: if this unit has Dullahan, gain 1 Damage Up and 3 Defense Level Down
   PL: Na koniec tury odzyskuje 10 Poczytalności\nPrzy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury przy Poczytalności ujemnej: 3 Wzrosty Mocy Ataku\nPrzy aktywnym Dullahanie: 1 Wzrost Obrażeń i 3 Spadki Poziomu Obrony
65. [Status [AaCfPcBa_Alt2] — nazwa] 히스클리프들의 목을 벤다
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt2].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa_Alt2]`
   (powtórzenie elementu 61 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
66. [Status [AaCfPcBa_Alt2] — opis] 턴 종료 시 정신력 회복 10\n피격 시 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 3회)\n턴 시작 시 정신력이 10 미만이면, 공격 위력 증가 3 얻음\n턴 시작 시 듀라한이 있다면, 피해량 증가 3, 방어 레벨 감소 3 얻음
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt2].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 10 SP\nWhen hit, gain 1 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 10 SP, gain 3 Attack Power Up\nTurn Start: if this unit has Dullahan, gain 3 Damage Up and 3 Defense Level Down
   PL: Na koniec tury odzyskuje 10 Poczytalności\nPrzy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury przy Poczytalności poniżej 10: 3 Wzrosty Mocy Ataku\nPrzy aktywnym Dullahanie: 3 Wzrosty Obrażeń i 3 Spadki Poziomu Obrony
67. [Status [AaCfPcBa_Alt3] — nazwa] 애정과 증오
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt3].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa_Alt3]`
   limit: do 40 znaków
   EN: Affection and Hatred
   PL: Czułość i Nienawiść
68. [Status [AaCfPcBa_Alt3] — opis] 턴 종료 시 정신력 회복 15\n공격 적중 시 다음 턴에 신속 1, 공격 레벨 증가 1 얻음 (턴 당 3회)\n턴 시작 시 정신력이 10 미만이면, 공격 위력 증가 3 얻음\n턴 시작 시 듀라한이 있다면, 피해량 증가 3 얻음
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt3].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 15 SP\nOn Hit, gain 1 Haste and 1 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 10 SP, gain 3 Attack Power Up\nTurn Start: if this unit has Dullahan, gain 3 Damage Up
   PL: Na koniec tury odzyskuje 15 Poczytalności\nPrzy trafieniu zyskuje w następnej turze 1 Pośpiechu i 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury przy Poczytalności poniżej 10: 3 Wzrosty Mocy Ataku\nPrzy aktywnym Dullahanie: 3 Wzrosty Obrażeń
69. [Status [AaCfPcBa_Alt4] — nazwa] 색바랜 약속
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt4].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa_Alt4]`
   limit: do 40 znaków
   EN: Faded Promise
   PL: Wyblakła Obietnica
70. [Status [AaCfPcBa_Alt4] — opis] 턴 종료 시 정신력 회복 15\n공격 적중 시 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 3회)\n턴 시작 시 정신력이 20 미만이면, 공격 위력 증가 3 얻음\n턴 시작 시 듀라한이 있다면, 피해량 증가 3, 공격 레벨 증가 3 얻음\n체력이 1이 되었다면, 전체 체력 40%회복, 정신력 25 회복 (전투당 1회)
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt4].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 15 SP\nOn Hit, gain 1 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 20 SP, gain 3 Attack Power Up\nTurn Start: if this unit has Dullahan, gain 3 Damage Up and 3 Offense Level Up\nAt 1 HP, heal 40% HP and 25 SP (once per Encounter)
   PL: Na koniec tury odzyskuje 15 Poczytalności\nPrzy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury przy Poczytalności poniżej 20: 3 Wzrosty Mocy Ataku\nPrzy aktywnym Dullahanie: 3 Wzrosty Obrażeń i 3 Wzrosty Poziomu Ataku\nGdy HP osiągnie 1, odzyskuje 40% Maks. HP i 25 Poczytalności (raz na walkę)
71. [Status [AaCfPcBa_Alt5] — nazwa] 색바랜 약속
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt5].name
   kontekst: identyfikator statusu w tekstach: `[AaCfPcBa_Alt5]`
   (powtórzenie elementu 69 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
72. [Status [AaCfPcBa_Alt5] — opis] 턴 종료 시 정신력 회복 15\n공격 적중 시 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 3회)\n턴 시작 시 정신력이 20 미만이면, 공격 위력 증가 3 얻음\n턴 시작 시 듀라한이 있다면, 피해량 증가 3, 공격 레벨 증가 3 얻음\n이번 전투동안 생존한 아군이 자신을 제외하여 1명 이상 있을 때, 히스클리프의 체력이 1 미만으로 감소하지 않는다\n체력이 1이 되었다면, 전체 체력 40%회복, 정신력 25 회복 (전투당 1회)
   źródło: Bufs.json :: dataList[id=AaCfPcBa_Alt5].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: heal 15 SP\nOn Hit, gain 1 Offense Level Up next turn (3 times per turn)\nTurn Start: at less than 20 SP, gain 3 Attack Power Up\nTurn Start: if this unit has Dullahan, gain 3 Damage Up and 3 Offense Level Up\nAs long as there is at least 1 other surviving ally, Heathcliff's HP does not drop below 1\nAt 1 HP, heal 40% HP and 25 SP (once per Encounter)
   PL: Na koniec tury odzyskuje 15 Poczytalności\nPrzy trafieniu zyskuje w następnej turze 1 Wzrost Poziomu Ataku (3 razy na turę)\nNa początek tury przy Poczytalności poniżej 20: 3 Wzrosty Mocy Ataku\nPrzy aktywnym Dullahanie: 3 Wzrosty Obrażeń i 3 Wzrosty Poziomu Ataku\nDopóki w tej walce przeżywa co najmniej 1 sojusznik poza nim samym, HP Heathcliffa nie spada poniżej 1\nGdy HP osiągnie 1, odzyskuje 40% Maks. HP i 25 Poczytalności (raz na walkę)
73. [Status [Coffin] — nazwa] 관
   źródło: Bufs.json :: dataList[id=Coffin].name
   kontekst: identyfikator statusu w tekstach: `[Coffin]`
   limit: do 40 znaków
   EN: Coffin
   PL: Trumna
74. [Status [Coffin] — opis] - 최대 10\n- 턴 종료 시 다음 턴에\n3당 피해량 증가 2 얻음 (최대 6)\n4당 속도 최솟값 1 증가 (최대 2)\n5당 합 위력 증가 1 얻음 (최대 2)
   źródło: Bufs.json :: dataList[id=Coffin].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- At Turn End:\n  - Gain 2 Damage Up next turn for every 3 Value (max 6)\n  - Raise minimum Speed by 1 next turn for every 4 Value (max 2)\n  - Gain 1 Clash Power Up next turn for every 5 Value (max 2)
   PL: - Maks.: 10\n- Na koniec tury, w następnej turze:\nza każde 3 — 2 Wzrosty Obrażeń (maks. 6)\nza każde 4 — minimalna Szybkość +1 (maks. 2)\nza każde 5 — 1 Wzrost Mocy Starcia (maks. 2)
75. [Status [WildHunt] — nazwa] 와일드헌트
   źródło: Bufs.json :: dataList[id=WildHunt].name
   kontekst: identyfikator statusu w tekstach: `[WildHunt]`
   limit: do 40 znaków
   EN: Wild Hunt
   PL: Dziki Gon
76. [Status [WildHunt] — opis] - 처음 부여받은 턴동안 체력이 1 남고 턴 종료 시 전체 체력의 50%만큼 체력 회복, 정신력이 0으로 초기화됨.\n- 사망시, 가장 적은 E.G.O 자원을 1 얻음\n- 공격에 의해 사망시, 마지막으로 자신을 공격한 대상에게 침잠 3 부여\n- 부활한 턴 종료시 사망
   źródło: Bufs.json :: dataList[id=WildHunt].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In the same turn this unit gained Wild Hunt for the first time, always have 1 remaining HP; "revive"(heal 50% HP and reset SP to 0) this unit at Turn End.\n- On death, gain 1 E.G.O resource for the least-owned E.G.O resource\n- If this unit is killed by an attack, inflict 3 Sinking against the last attacker\n- Dies at the end of the same turn this unit was revived in
   PL: - W turze pierwszego nadania HP spada do 1; na koniec tury regeneruje 50% ogólnego HP i zeruje Poczytalność\n- Po śmierci zyskuje 1 zasobu E.G.O najrzadszego atrybutu\n- Śmierć od ataku nadaje 3 Zatonięcia ostatniemu atakującemu\n- Umiera na koniec tury, w której został wskrzeszony
77. [Status [NightPathfinding] — nazwa] 듀라한
   źródło: Bufs.json :: dataList[id=NightPathfinding].name
   kontekst: identyfikator statusu w tekstach: `[NightPathfinding]`
   limit: do 40 znaków
   EN: Dullahan
   PL: Dullahan
78. [Status [NightPathfinding] — opis] - 최대 3\n- 공격 레벨 3 증가\n- 방어 레벨 3 감소\n- 속도 최솟값, 최댓값 1 증가\n- 턴 종료 시, 다음 턴에 1 얻음 (단, 자신의 정신력이 -25 이하면 제거)\n- 턴 종료 시 듀라한이 있으면, 자신의 정신력이 (15 - (관 수치/2))만큼 감소 (최소 10)
   źródło: Bufs.json :: dataList[id=NightPathfinding].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 3\n- Gain 3 Offense Level\n- Lose 3 Defense Level\n- Raise Min & Max Speed values by 1\n- Turn End: Gain 1 Dullahan next turn (At -25 SP or less, however, completely lose Dullahan)\n- Turn End: If this unit has Dullahan, lose (15 - (Coffin/2)) SP. (min 10)
   PL: - Maks.: 3\n- Poziom Ataku +3\n- Poziom Obrony -3\n- Minimalna i maksymalna Szybkość +1\n- Na koniec tury zyskuje 1 w następnej turze (przy Poczytalności -25 lub niższej efekt znika całkowicie)\n- Na koniec tury, przy aktywnym Dullahanie, traci (15 - (Trumna/2)) Poczytalności (min. 10)
79. [Status [WanderingFootsteps] — nazwa] 다가오는 파탄
   źródło: Bufs.json :: dataList[id=WanderingFootsteps].name
   kontekst: identyfikator statusu w tekstach: `[WanderingFootsteps]`
   limit: do 40 znaków
   EN: Impending Ruin
   PL: Nadchodząca Ruina
80. [Status [WanderingFootsteps] — opis] - 정신력이 있는 대상인 경우, 패닉 유형이 '파탄'으로 변경됨.\n(파탄: 사기저하가 되면, 매 턴 종료 시 침잠 3 얻음. 자신의 합 위력 -1\n패닉이 되면 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가. 자신의 합 위력 -2)\n- 정신력이 없는 대상인 경우, 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨.\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨.
   źródło: Bufs.json :: dataList[id=WanderingFootsteps].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: change their Panic Type to "Ruin".\n(Ruin: When this unit enters Low Morale state, gain 3 Sinking at every Turn End and lose 1 Clash Power. When this unit Panics, gain 5 Sinking and 3 Sinking Count at every Turn End and lose 2 Clash Power)\n- Non-SP Units: -10% chance to flip Heads\n- Reduced by 1 at Turn End\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value.\n※ Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types.
   PL: - Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Ruina”\n(Ruina: w stanie Spadku Moralu na koniec każdej tury zyskuje 3 Zatonięcia i traci 1 Mocy Starcia; w stanie Paniki na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia oraz traci 2 Mocy Starcia)\n- Jednostki bez Poczytalności: -10% szansy na awers\n- Na koniec tury maleje o 1\nTen efekt nie kumuluje się — nadanie zastępuje bieżącą wartość.\n※ Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności.
81. [Status [WanderingFootsteps_Main] — nazwa] 다가오는 파탄
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Main].name
   kontekst: identyfikator statusu w tekstach: `[WanderingFootsteps_Main]`
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Status [WanderingFootsteps_Main] — opis] - 정신력이 있는 대상인 경우, 패닉 유형이 '파탄'으로 변경됨\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Main].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Change their Panic Type to 'Ruin'\n- Reduced by 1 at Turn End
   PL: - Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Ruina”\n- Na koniec tury maleje o 1
83. [Status [WanderingFootsteps_Sub] — nazwa] 다가오는 파탄
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Sub].name
   kontekst: identyfikator statusu w tekstach: `[WanderingFootsteps_Sub]`
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
84. [Status [WanderingFootsteps_Sub] — opis] - 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Sub].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - -10% chance to flip Heads\n- Reduced by 1 at Turn End
   PL: - -10% szansy na awers\n- Na koniec tury maleje o 1
85. [Status [WanderingFootsteps_LowMorale] — nazwa] 파탄
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[WanderingFootsteps_LowMorale]`
   limit: do 40 znaków
   EN: Ruin
   PL: Ruina
86. [Status [WanderingFootsteps_LowMorale] — opis] - 사기 저하\n- 자신의 합 위력 -1. 매 턴 종료시 침잠 3 얻음
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1 on self. Gain 3 Sinking at every Turn End
   PL: - Spadek Moralu\n- Moc Starcia -1; na koniec każdej tury zyskuje 3 Zatonięcia
87. [Status [WanderingFootsteps_LowMorale] — podsumowanie] 자신의 합 위력 -1. 매 턴 종료시 침잠 3 얻음
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_LowMorale].summary
   limit: do 120 znaków
   EN: Clash Power -1 on self. Gain 3 Sinking at every Turn End
   PL: Moc Starcia -1; na koniec każdej tury zyskuje 3 Zatonięcia
88. [Status [WanderingFootsteps_Panic] — nazwa] 파탄
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Panic].name
   kontekst: identyfikator statusu w tekstach: `[WanderingFootsteps_Panic]`
   (powtórzenie elementu 85 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Status [WanderingFootsteps_Panic] — opis] - 패닉\n- 자신의 합 위력 -2. 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2 on self. Gain 5 Sinking and +3 Sinking Count at every Turn End
   PL: - Panika\n- Moc Starcia -2; na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia
90. [Status [WanderingFootsteps_Panic] — podsumowanie] 자신의 합 위력 -2. 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가
   źródło: Bufs.json :: dataList[id=WanderingFootsteps_Panic].summary
   limit: do 120 znaków
   EN: Clash Power -2 on self. Gain 5 Sinking and +3 Sinking Count at every Turn End
   PL: Moc Starcia -2; na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia
91. [Status [UninvitedGuestPersonality] — nazwa] 초청받지 않은 자
   źródło: Bufs.json :: dataList[id=UninvitedGuestPersonality].name
   kontekst: identyfikator statusu w tekstach: `[UninvitedGuestPersonality]`
   limit: do 40 znaków
   EN: The Uninvited
   PL: Nieproszony Gość
92. [Status [UninvitedGuestPersonality] — opis] - 최대 2\n- 사망 시 마지막 공격자의 정신력 3 회복, 이 효과가 효과를 보유하지 않은 무작위 아군에게 2로 옮겨감.\n- 자신의 침잠 1당 받는 피해량 +0.5% (최대 10%, 집중 전투일 경우 부위마다 별도로 판정)\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=UninvitedGuestPersonality].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 2\n- Upon death, the last attacker heals 3 SP; then, a random ally without this effect gains 2 Stacks of this effect.\n- Take +0.5% damage for every Sinking on self (max 10%; for Focused Encounters, count Sinking on each Part separately)\n- Turn End: reduced by 1
   PL: - Maks.: 2\n- Po śmierci ostatni atakujący regeneruje 3 Poczytalności, po czym losowy sojusznik bez tego efektu zyskuje 2 stosy\n- Otrzymuje +0,5% obrażeń za każde Zatonięcie (maks. 10%; w walkach skupionych liczone osobno dla każdej części)\n- Na koniec tury maleje o 1
93. [Status [DevyatDimensionalSack] — nazwa] 딜리버리 캐리어 - 로쟈
   źródło: Bufs.json :: dataList[id=DevyatDimensionalSack].name
   kontekst: identyfikator statusu w tekstach: `[DevyatDimensionalSack]`
   limit: do 40 znaków
   EN: Courier Trunk - Rodion
   PL: Kufer Kuriera - Rodion
94. [Status [DevyatDimensionalSack] — opis] - 기본값 : 0\n- 턴 시작 시, 3 얻음\n- 스택은 퇴각 시 사라지지 않고 저장됨\n- 10 이상이면, 속도 최솟값, 최댓값 1 증가\n- 20 이상이면, 합 위력 증가 1, 참격 피해량 증가 1 얻음\n- 30 이상이면,\n· 스킬 사용 시 최대 체력의 (스택/3)%만큼 체력 피해와 (스택/3)만큼의 정신력 피해를 받음\n· 턴 종료 시 최대 체력의 (스택/2)%만큼 체력 피해와 (스택/2)만큼 정신력 피해를 받음 (퇴각 전에 적용됨)
   źródło: Bufs.json :: dataList[id=DevyatDimensionalSack].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 0\n- Turn Start: gain 3 Stack\n- Stack does not expire upon Retreat; it is stored instead\n- At 10+ Stack: raise Min & Max Speed values by 1\n- At 20+ Stack: Gain 1 Clash Power Up and 1 Slash Damage Up\n- At 30+ Stack:\n· On Skill Use, take (Stack/3)% HP damage and (Stack/3) SP damage\n· On Turn End, take (Stack/2)% HP damage and (Stack/2) SP damage (applies before Retreat)
   PL: - Wartość bazowa: 0\n- Na początku tury zyskuje 3 stosy\n- Stosy nie znikają przy Odwrócie — zostają zapisane\n- Przy 10 lub więcej: minimalna i maksymalna Szybkość +1\n- Przy 20 lub więcej: 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń Cięcia\n- Przy 30 lub więcej:\n· Przy użyciu Umiejętności otrzymuje (stosy/3)% obrażeń HP i tyle samo obrażeń Poczytalności\n· Na koniec tury otrzymuje (stosy/2)% obrażeń HP i tyle samo obrażeń Poczytalności (przed Odwrótem)
95. [Status [Retreat] — nazwa] 전략적 휴식 복지 모드
   źródło: Bufs.json :: dataList[id=Retreat].name
   kontekst: identyfikator statusu w tekstach: `[Retreat]`
   limit: do 40 znaków
   EN: Strategic R&R Mode
   PL: Tryb Strategicznego Odpoczynku
96. [Status [Retreat] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n· 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n· 전투 복귀 시 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: Bufs.json :: dataList[id=Retreat].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death)\n· In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n· When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Na koniec tury dochodzi do siebie z Oszołomienia i wycofuje się z walki (nie dotyczy wymuszonego Oszołomienia; nie traktowane jako śmierć)\n· W walkach łańcuchowych oddaje swoje sloty jednostce zastępczej i przesuwa się na koniec kolejności rozmieszczenia jednostek rezerwowych (opuszcza walkę całkowicie, jeśli w następnej turze nie ma innych jednostek rezerwowych do zamiany. Przy powrocie do walki wraca w kolejności wycofań)\n· Przy powrocie do walki wraca z HP i Poczytalnością z momentu wycofania i traci wszystkie efekty poza wybranymi kilkoma (przy Poczytalności poniżej 0 resetuje ją do 0)
97. [Status [DefensiveStance] — nazwa] 방어 태세
   źródło: Bufs.json :: dataList[id=DefensiveStance].name
   kontekst: identyfikator statusu w tekstach: `[DefensiveStance]`
   limit: do 40 znaków
   EN: Defensive Stance
   PL: Postawa Obronna
98. [Status [DefensiveStance] — opis] - 최댓값: 2\n- 이 효과는 합산되지 않고, 갱신됨\n- 턴 종료 시 1 감소\n- 이 효과를 얻으면 다음 턴에 아래 효과 적용\n· 속도가 최솟값으로 고정됨\n· 방어 레벨 증가 5 얻음\n· (10 / 자신의 슬롯 수)만큼 자신의 각 슬롯 도발치 증가\n· 스킬 지정 시 속도에 관계 없이 공격 대상을 자신으로 변경할 수 있음 (집중 전투 전용)\n· 합 승리시 진동 폭발\n· 피해로 인해 흐트러짐 상태가 되지 않음
   źródło: Bufs.json :: dataList[id=DefensiveStance].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 2\n- This effect does not compound in potency; stacking it only extends its duration.\n- Reduced by 1 at Turn End\n- When a unit gains this effect, gain the following effects next turn:\n  · Fix this unit's Speed to its minimum value\n  · Gain 5 Defense Level Up\n  · Each of this unit's Slots gain +(10 / this unit's # of Slots) Aggro\n  · When chaining Skills, this unit can draw enemies' attack toward this unit regardless of Speed (Focused Encounters only)\n  · Upon Clash Win, trigger Tremor Burst\n  · Cannot be Staggered by damage
   PL: - Maks.: 2\n- Nie kumuluje się — nadanie przedłuża czas działania\n- Na koniec tury maleje o 1\n- Po nadaniu, w następnej turze:\n· Szybkość zostaje zablokowana na wartości minimalnej\n· 5 Wzrostów Poziomu Obrony\n· Każdy slot zyskuje +(10/liczba slotów) Wartości Prowokacji\n· Może przyciągać ataki wrogów niezależnie od Szybkości przy wskazywaniu Umiejętności (tylko walki skupione)\n· Po wygranej w Starciu wywołuje Wybuch Wstrząsu\n· Nie zostaje oszołomiony przez obrażenia
99. [Status [CanDuelGuard] — nazwa] 합 가능 가드
   źródło: Bufs.json :: dataList[id=CanDuelGuard].name
   kontekst: identyfikator statusu w tekstach: `[CanDuelGuard]`
   limit: do 40 znaków
   EN: Clashable Guard
   PL: Blok Zdatny do Starcia
100. [Status [CanDuelGuard] — opis] - 합 승리 시 대상에게 마지막 합 위력만큼 흐트러짐 손상을 입힘.\n- 합 패배 후 피격 시 최종 위력만큼 공격자의 스킬 최종 위력을 감소시킴.\n- 합 패배 시 공격 스킬과의 레벨 차이, 공명으로 인해 최종 위력이 증가하지 않음.
   źródło: Bufs.json :: dataList[id=CanDuelGuard].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Win: raise the target's Stagger Threshold by this unit's final Clash Power.\n- On Clash Lose: when hit, reduce the attacker's final Skill Power by this unit's Final Power.\n- On Clash Lose: does not gain Final Power from the following sources: Resonance and the Level disparity against the Attack Skill
   PL: - Po wygranej w Starciu podnosi Próg Oszołomienia celu o własną końcową Moc Starcia\n- Po przegranej w Starciu, przy trafieniu, obniża końcową Moc Umiejętności atakującego o własną Moc Końcową\n- Po przegranej w Starciu nie zyskuje Mocy Końcowej z Rezonansu ani różnicy poziomów względem Umiejętności ataku
101. [Status [SuperCoin] — nazwa] 파괴 불가 코인
   źródło: Bufs.json :: dataList[id=SuperCoin].name
   kontekst: identyfikator statusu w tekstach: `[SuperCoin]`
   limit: do 40 znaków
   EN: Unbreakable Coin
   PL: Moneta Niezniszczalna
102. [Status [SuperCoin] — opis] - 합 패배 시 코인이 파괴되지 않음.\n- 공격 스킬에 해당 코인이 있으면, 피격 후 해당 코인으로 공격함.\n- 합 패배 시 파괴되지 않은 코인은 코인 위력이 1이 됨.
   źródło: Bufs.json :: dataList[id=SuperCoin].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This coin does not break upon Clash Lose.\n- If an Attack Skill has this Coin, attack with this Coin after getting hit.\n- Upon Clash Lose, fix the Coin Power of the unbroken Coin to 1
   PL: - Moneta nie ulega zniszczeniu po przegranej w Starciu\n- Jeśli Umiejętność ataku zawiera tę monetę, atakuje nią po otrzymaniu trafienia\n- Po przegranej w Starciu moc niezniszczonej monety zostaje ustalona na 1
103. [Status [BloodScissorPersonalityFirst] — nazwa] 핏빛 가위날
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalityFirst].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorPersonalityFirst]`
   limit: do 40 znaków
   EN: Blood-tinged Scissorblades
   PL: Zakrwawione Ostrza Nożyc
104. [Status [BloodScissorPersonalityFirst] — opis] - 최댓값: 10\n- 핏빛 가위날 1단계\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalityFirst].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blood-tinged Scissorblades\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 10\n- Zakrwawione Ostrza Nożyc, etap 1\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
105. [Status [BloodScissorPersonalitySecond] — nazwa] 핏빛 가위날 II
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalitySecond].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorPersonalitySecond]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades II
   PL: Zakrwawione Ostrza Nożyc II
106. [Status [BloodScissorPersonalitySecond] — opis] - 최댓값: 20\n- 핏빛 가위날 2단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalitySecond].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 20\n- Zakrwawione Ostrza Nożyc, etap 2\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
107. [Status [BloodScissorPersonalityThird] — nazwa] 핏빛 가위날 III
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalityThird].name
   kontekst: identyfikator statusu w tekstach: `[BloodScissorPersonalityThird]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades III
   PL: Zakrwawione Ostrza Nożyc III
108. [Status [BloodScissorPersonalityThird] — opis] - 최댓값: 30\n- 핏빛 가위날 3단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1 얻음\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodScissorPersonalityThird].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up for every 5 Stack\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 30\n- Zakrwawione Ostrza Nożyc, etap 3\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
109. [Status [LineCuttingPersonality] — nazwa] 재봉 대상
   źródło: Bufs.json :: dataList[id=LineCuttingPersonality].name
   kontekst: identyfikator statusu w tekstach: `[LineCuttingPersonality]`
   limit: do 40 znaków
   EN: Sewing Target
   PL: Cel Szycia
110. [Status [LineCuttingPersonality] — opis] - 최댓값: 1\n- 출혈당 받는 피해량 +0.5% (최대 10%)\n- 턴 종료 시, 1 감소
   źródło: Bufs.json :: dataList[id=LineCuttingPersonality].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Take +0.5% damage for every Bleed (max 10%)\n- Turn End: reduced by 1
   PL: - Maks.: 1\n- Otrzymuje +0,5% obrażeń za każde Krwawienie (maks. 10%)\n- Na koniec tury maleje o 1
111. [Status [Snare] — nazwa] 올가미
   źródło: Bufs.json :: dataList[id=Snare].name
   kontekst: identyfikator statusu w tekstach: `[Snare]`
   limit: do 40 znaków
   EN: Lasso
   PL: Lasso
112. [Status [Snare] — opis] - 최댓값 : 3\n- 턴 종료시 자신의 현재 속도만큼 파열 위력 얻음 (최대 5), 다음 턴에 속박 1 얻음\n- 턴 종료시 수치 1 감소
   źródło: Bufs.json :: dataList[id=Snare].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 3\n- Turn End: gain Rupture Potency equal to this unit's current Speed value (max 5), and gain 1 Bind next turn\n- Turn End: reduced by 1
   PL: - Maks.: 3\n- Na koniec tury zyskuje Moc Rozdarcia równą aktualnej Szybkości (maks. 5), a w następnej turze 1 Spętania\n- Na koniec tury maleje o 1
113. [Status [BloodyHandGregFirst] — nazwa] 피로 물든 손
   źródło: Bufs.json :: dataList[id=BloodyHandGregFirst].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHandGregFirst]`
   limit: do 40 znaków
   EN: Bloodied Hand
   PL: Zakrwawiona Dłoń
114. [Status [BloodyHandGregFirst] — opis] - 최댓값 : 10\n- 피로 물든 손 1단계\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: Bufs.json :: dataList[id=BloodyHandGregFirst].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Bloodied Hand\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 10\n- Zakrwawiona Dłoń, etap 1\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
115. [Status [BloodyHandGregSecond] — nazwa] 피로 물든 손 II
   źródło: Bufs.json :: dataList[id=BloodyHandGregSecond].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHandGregSecond]`
   limit: do 40 znaków
   EN: Bloodied Hand II
   PL: Zakrwawiona Dłoń II
116. [Status [BloodyHandGregSecond] — opis] - 최댓값 : 20\n- 피로 물든 손 2단계\n- 턴 시작시, 수치 10당 공격 레벨 증가 1 얻음\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: Bufs.json :: dataList[id=BloodyHandGregSecond].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Bloodied Hand\n- Turn Start: gain 1 Offense Level Up for every 10 Stack\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 20\n- Zakrwawiona Dłoń, etap 2\n- Na początku tury za każde 10 stosów: 1 Wzrost Poziomu Ataku\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
117. [Status [BloodyHandGregThird] — nazwa] 피로 물든 손 III
   źródło: Bufs.json :: dataList[id=BloodyHandGregThird].name
   kontekst: identyfikator statusu w tekstach: `[BloodyHandGregThird]`
   limit: do 40 znaków
   EN: Bloodied Hand III
   PL: Zakrwawiona Dłoń III
118. [Status [BloodyHandGregThird] — opis] - 최댓값 : 30\n- 피로 물든 손 3단계\n- 턴 시작시, 수치 10당 공격 레벨 증가 1 얻음\n- 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: Bufs.json :: dataList[id=BloodyHandGregThird].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Bloodied Hand\n- Turn Start: gain 1 Offense Level Up for every 10 Stack\n- On Hit with Base Skills: additionally inflict 1 Rupture and 1 Bleed\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 30\n- Zakrwawiona Dłoń, etap 3\n- Na początku tury za każde 10 stosów: 1 Wzrost Poziomu Ataku\n- Każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
119. [Status [WornHeartGreg] — nazwa] 닳아버린 마음
   źródło: Bufs.json :: dataList[id=WornHeartGreg].name
   kontekst: identyfikator statusu w tekstach: `[WornHeartGreg]`
   limit: do 40 znaków
   EN: Ailing Heart
   PL: Zmęczone Serce
120. [Status [WornHeartGreg] — opis] - 최댓값 : 10\n- 턴 종료시, 수치 1 증가\n- 턴 시작시 수치 3당 방어 레벨 증가 1 얻음\n- 자신의 체력이 50% 미만이면 수치 3당 방어 레벨이 1 증가함\n- 자신의 현재 체력이 최대 체력의 40% 미만이면, 기본 스킬 적중시 피해량의 (수치 x 5)% 만큼 체력 회복 (최소 1. 소수점 버림. 스킬 당 최대 30 회복)
   źródło: Bufs.json :: dataList[id=WornHeartGreg].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Turn End: gain 1 Stack\n- Turn Start: gain 1 Defense Level Up for every 3 Stack\n- At 50%- HP, gain 1 Defense Level for every 3 Stack\n- At 40%- HP, On Hit with Base Skills, heal (Stack x 5)% of damage dealt On Hit as HP (min 1; rounded down; heal up to 30 HP per Skill)
   PL: - Maks.: 10\n- Na koniec tury wartość rośnie o 1\n- Na początku tury za każde 3 wartości: 1 Wzrost Poziomu Obrony\n- Przy HP poniżej 50% za każde 3 wartości: dodatkowo 1 Poziomu Obrony\n- Przy HP poniżej 40% każde trafienie Umiejętnością bazową leczy 10% zadanych obrażeń (min. 1; zaokrąglone w dół; do 30 HP na Umiejętność)
121. [Status [BloomingThornsRodionFirst] — nazwa] 피어나는 가시
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionFirst].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThornsRodionFirst]`
   limit: do 40 znaków
   EN: Blooming Thorn
   PL: Kwitnące Ciernie
122. [Status [BloomingThornsRodionFirst] — opis] - 최댓값 : 10\n- 피어나는 가시 1단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionFirst].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 10\n- Kwitnące Ciernie, etap 1\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Mocy Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
123. [Status [BloomingThornsRodionSecond] — nazwa] 피어나는 가시 II
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionSecond].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThornsRodionSecond]`
   limit: do 40 znaków
   EN: Blooming Thorn II
   PL: Kwitnące Ciernie II
124. [Status [BloomingThornsRodionSecond] — opis] - 최댓값 : 20\n- 피어나는 가시 2단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionSecond].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 20\n- Kwitnące Ciernie, etap 2\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
125. [Status [BloomingThornsRodionThird] — nazwa] 피어나는 가시 III
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionThird].name
   kontekst: identyfikator statusu w tekstach: `[BloomingThornsRodionThird]`
   limit: do 40 znaków
   EN: Blooming Thorn III
   PL: Kwitnące Ciernie III
126. [Status [BloomingThornsRodionThird] — opis] - 최댓값 : 30\n- 피어나는 가시 3단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: Bufs.json :: dataList[id=BloomingThornsRodionThird].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 30\n- Kwitnące Ciernie, etap 3\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
127. [Status [FestivalFeverRodion] — nazwa] 축제의 열기
   źródło: Bufs.json :: dataList[id=FestivalFeverRodion].name
   kontekst: identyfikator statusu w tekstach: `[FestivalFeverRodion]`
   limit: do 40 znaków
   EN: Festive Fever
   PL: Gorączka Święta
128. [Status [FestivalFeverRodion] — opis] - 최댓값 : 10\n- 턴 종료시 소멸\n- 출혈이 부여된 대상에게 가하는 피해량 +({0} x 1.5)%\n- 혈찬을 소모하거나 얻는 스킬이면, 대신 가하는 피해량 +({0} x 3)%
   źródło: Bufs.json :: dataList[id=FestivalFeverRodion].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Max Value: 10\n- Expires at Turn End\n- Deal +({0} x 1.5)% damage against targets with Bleed\n- Skills that consume or gain Bloodfeast : deal +({0} x 3)% damage instead
   PL: - Maks. wartości: 10\n- Znika na koniec tury\n- Zadaje +({0} x 1.5)% obrażeń celom z Krwawieniem\n- Umiejętności zużywające lub zyskujące Krwawą Ucztę zadają zamiast tego +({0} x 3)% obrażeń
129. [Status [VibrationSpring] — nazwa] 진동 - 태엽감기
   źródło: Bufs.json :: dataList[id=VibrationSpring].name
   kontekst: identyfikator statusu w tekstach: `[VibrationSpring]`
   limit: do 40 znaków
   EN: Tremor - Clockwinding
   PL: Wstrząs - Nakręcanie
130. [Status [VibrationSpring] — opis] - 속도 최댓값 +2\n- 자신이 스킬, 코인 효과로 진동 위력이나 진동 횟수를 부여할 때, 자신의 진동 횟수를 1 소모하여 부여량 +1\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationSpring].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed + 2\n- Consume Tremor Count on self to inflict 1 more of Tremor Potency or Count when inflicting them with this unit's Skill or Coin effects\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Maksymalna Szybkość +2\n- Nadając Moc lub Licznik Wstrząsu efektami własnych Umiejętności lub monet, zużywa 1 Licznika Wstrząsu, by nadać o 1 więcej\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n- (Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
131. [Status [VibrationSpring] — podsumowanie] 속도 최댓값 +2\n자신의 진동 횟수를 소모하여 진동 위력, 횟수 부여량 +1
   źródło: Bufs.json :: dataList[id=VibrationSpring].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Speed +2\nConsume Tremor Count on self to inflict +1 more Tremor Potency and Count
   PL: Maks. Szybkość +2\nZużywa własny Licznik Wstrząsu, nadając o 1 więcej Mocy i Licznika Wstrząsu
132. [Status [DevyatDimensionalSackSinclair] — nazwa] 딜리버리 캐리어 - 싱클레어
   źródło: Bufs.json :: dataList[id=DevyatDimensionalSackSinclair].name
   kontekst: identyfikator statusu w tekstach: `[DevyatDimensionalSackSinclair]`
   limit: do 40 znaków
   EN: Courier Trunk - Sinclair
   PL: Kufer Kuriera - Sinclair
133. [Status [DevyatDimensionalSackSinclair] — opis] - 기본값 : 0\n- 턴 시작 시, 3 얻음\n- 스택은 퇴각 시 사라지지 않고 저장됨\n- 10 이상이면, 속도 최솟값, 최댓값 1 증가\n- 20 이상이면, 합 위력 증가 1, 타격 피해량 증가 1 얻음\n- 30 이상이면,\n· 스킬 사용 시 최대 체력의 (스택/3)%만큼 체력 피해와 (스택/3)만큼의 정신력 피해를 받음\n· 턴 종료 시 최대 체력의 (스택/2)%만큼 체력 피해와 (스택/2)만큼 정신력 피해를 받음 (퇴각 전에 적용됨)
   źródło: Bufs.json :: dataList[id=DevyatDimensionalSackSinclair].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 0\n- Turn Start: gain 3 Stack\n- Stack does not expire upon Retreat; it is stored instead\n- At 10+ Stack: raise Min & Max Speed values by 1\n- At 20+ Stack: Gain 1 Clash Power Up and 1 Blunt Damage Up\n- At 30+ Stack:\n· On Skill Use, take (Stack/3)% HP damage and (Stack/3) SP damage\n· On Turn End, take (Stack/2)% HP damage and (Stack/2) SP damage (applies before Retreat)
   PL: - Wartość bazowa: 0\n- Na początku tury zyskuje 3 stosy\n- Stosy nie znikają przy Odwrócie — zostają zapisane\n- Przy 10 lub więcej: minimalna i maksymalna Szybkość +1\n- Przy 20 lub więcej: 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń Uderzenia\n- Przy 30 lub więcej:\n· Przy użyciu Umiejętności otrzymuje (stosy/3)% obrażeń HP i tyle samo obrażeń Poczytalności\n· Na koniec tury otrzymuje (stosy/2)% obrażeń HP i tyle samo obrażeń Poczytalności (przed Odwrótem)
134. [Status [Zazen] — nazwa] 참선
   źródło: Bufs.json :: dataList[id=Zazen].name
   kontekst: identyfikator statusu w tekstach: `[Zazen]`
   limit: do 40 znaków
   EN: Dhyāna
   PL: Dhyāna
135. [Status [Zazen] — opis] - 최댓값 : 108\n- 수치당 가하는 피해량 +1%
   źródło: Bufs.json :: dataList[id=Zazen].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 108\n- Deal +1% damage for every Stack
   PL: - Maks.: 108\n- Zadaje +1% obrażeń za każdą wartość
136. [Status [Zazen] — podsumowanie] 가하는 피해량 증가
   źródło: Bufs.json :: dataList[id=Zazen].summary
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
137. [Status [SwirlingBloodPersonality] — nazwa] 일렁임【혈귀】
   źródło: Bufs.json :: dataList[id=SwirlingBloodPersonality].name
   kontekst: identyfikator statusu w tekstach: `[SwirlingBloodPersonality]`
   limit: do 40 znaków
   EN: Shimmering【Bloodfiend】
   PL: Drgający【Krwiopijca】
138. [Status [SwirlingBloodPersonality] — opis] - 최댓값: 50\n- 이 버프가 있는 동안 보호막 체력이 받는 출혈 피해는 혈찬이 됨.\n- 부여될 때 수치만큼 보호막 체력을 얻음.\n- 턴 종료시 제거됨.
   źródło: Bufs.json :: dataList[id=SwirlingBloodPersonality].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- As long as this effect exists, all Bleed damage taken by the Shield HP is converted to Bloodfeast.\n- Gain Shield HP equal to the Stack at the moment of its application\n- Expires at Turn End
   PL: - Maks.: 50\n- Dopóki to wzmocnienie działa, obrażenia Krwawieniem otrzymywane przez HP Tarczy stają się Ucztą Krwi\n- Przy nadaniu zyskuje HP Tarczy równe wartości\n- Znika na koniec tury
139. [Status [BloodArmorPersonalityFirst] — nazwa] 경혈
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalityFirst].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmorPersonalityFirst]`
   limit: do 40 znaków
   EN: Hardblood
   PL: Skondensowana Krew
140. [Status [BloodArmorPersonalityFirst] — opis] - 최댓값: 10\n- 경혈 1단계\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 10 당, 속도 최솟값, 최댓값 1 증가\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalityFirst].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Stage 1 Hardblood\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- Raise Min & Max Speed values by 1 for every 10 Hardblood\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 10\n- Skondensowana Krew, etap 1\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Za każde 10 Skondensowanej Krwi: minimalna i maksymalna Szybkość +1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
141. [Status [BloodArmorPersonalitySecond] — nazwa] 경혈 II
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalitySecond].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmorPersonalitySecond]`
   limit: do 40 znaków
   EN: Hardblood II
   PL: Skondensowana Krew II
142. [Status [BloodArmorPersonalitySecond] — opis] - 최댓값: 20\n- 경혈 2단계\n- 턴 시작시 수치 5 당 공격 레벨 증가 1 얻음\n- 속도 최솟값, 최댓값 1 증가\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalitySecond].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Stage 2 Hardblood\n- Turn Start: gain 1 Offense Level Up for every 5 Stack\n- Raise Min & Max Speed values by 1\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 20\n- Skondensowana Krew, etap 2\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku\n- Minimalna i maksymalna Szybkość +1\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
143. [Status [BloodArmorPersonalityThird] — nazwa] 경혈 III
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalityThird].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmorPersonalityThird]`
   limit: do 40 znaków
   EN: Hardblood III
   PL: Skondensowana Krew III
144. [Status [BloodArmorPersonalityThird] — opis] - 최댓값: 30\n- 경혈 3단계\n- 턴 시작시 수치 5 당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 속도 최솟값, 최댓값 2 증가\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=BloodArmorPersonalityThird].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Stage 3 Hardblood\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Up for every 5 Stack\n- Raise Min & Max Speed values by 2\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 30\n- Skondensowana Krew, etap 3\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony\n- Minimalna i maksymalna Szybkość +2\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
145. [Status [SadLamanchaland] — nazwa] 책임감
   źródło: Bufs.json :: dataList[id=SadLamanchaland].name
   kontekst: identyfikator statusu w tekstach: `[SadLamanchaland]`
   limit: do 40 znaków
   EN: Responsibility
   PL: Poczucie Obowiązku
146. [Status [SadLamanchaland] — opis] - 최댓값: 1\n- 합 위력 +1\n- 가하는 피해량 +20%\n- 받는 피해량 +20%
   źródło: Bufs.json :: dataList[id=SadLamanchaland].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Clash Power +1\n- Deal +20% damage\n- Take +20% damage
   PL: - Maks.: 1\n- Moc Starcia +1\n- Zadawane obrażenia +20%\n- Otrzymywane obrażenia +20%
147. [Status [FreishutzOutisEgoBullet_1st] — nazwa] 첫번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_1st].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_1st]`
   limit: do 40 znaków
   EN: The First Magic Bullet
   PL: Pierwsza Magiczna Amunicja
148. [Status [FreishutzOutisEgoBullet_1st] — opis] - 가하는 피해량 +20%\n- 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 30)
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_1st].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +20% damage\n- Raise the target's Stagger Threshold by damage dealt (max 30)
   PL: - Zadawane obrażenia +20%\n- Podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 30)
149. [Status [FreishutzOutisEgoBullet_2nd] — nazwa] 두번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_2nd].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_2nd]`
   limit: do 40 znaków
   EN: The Second Magic Bullet
   PL: Druga Magiczna Amunicja
150. [Status [FreishutzOutisEgoBullet_2nd] — opis] - 가하는 피해량 +10%\n- 메인 대상을 제외한 대상에게 피해를 입힘 (대상 수: 최대 4명), 메인 대상이 받는 피해는 0이 됨\n- 적중시 마비 3 부여
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_2nd].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage\n- Deal damage to targets other than the main target (max targets: 4); the main target takes 0 damage\n- On Hit, inflict 3 Paralyze
   PL: - Zadawane obrażenia +10%\n- Zadaje obrażenia celom poza głównym celem (maks. 4 cele); główny cel otrzymuje 0 obrażeń\n- Przy trafieniu nadaje 3 Paraliżu
151. [Status [FreishutzOutisEgoBullet_3rd] — nazwa] 세번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_3rd].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_3rd]`
   limit: do 40 znaków
   EN: The Third Magic Bullet
   PL: Trzecia Magiczna Amunicja
152. [Status [FreishutzOutisEgoBullet_3rd] — opis] - 가하는 피해량 +20%\n- 공격 시작 전 가중치 2 증가\n- 적중시 대상에게 공격 위력 감소 2, 화상 10 부여
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_3rd].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage\n- Before Attack: gain +2 Atk Weight\n- On Hit, inflict 2 Attack Power Down and 10 Burn
   PL: - Zadawane obrażenia +20%\n- Przed atakiem: wagi +2\n- Przy trafieniu nadaje 2 Spadki Mocy Ataku i 10 Podpalenia
153. [Status [FreishutzOutisEgoBullet_4th] — nazwa] 네번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_4th].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_4th]`
   limit: do 40 znaków
   EN: The Fourth Magic Bullet
   PL: Czwarta Magiczna Amunicja
154. [Status [FreishutzOutisEgoBullet_4th] — opis] - 가하는 피해량 +30%\n- 공격 시작 전 가중치 3 증가\n- 적중시 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 20), 다음 턴에 취약 3 부여
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_4th].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +30% damage\n- Before Attack: gain +3 Atk Weight\n- On Hit, raise the target's Stagger Threshold by damage dealt (max 20); then, inflict 3 Fragility next turn
   PL: - Zadawane obrażenia +30%\n- Przed atakiem: wagi +3\n- Przy trafieniu podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 20), a w następnej turze nadaje 3 Wrażliwości
155. [Status [FreishutzOutisEgoBullet_5th] — nazwa] 다섯번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_5th].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_5th]`
   limit: do 40 znaków
   EN: The Fifth Magic Bullet
   PL: Piąta Magiczna Amunicja
156. [Status [FreishutzOutisEgoBullet_5th] — opis] - 가하는 피해량 +30%\n- 공격 시작 전 가중치 4 증가\n- 적중시 대상에게 화상 10 부여. 다음 턴에 공격 레벨 감소 4, 방어 레벨 감소 4 부여
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_5th].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +30% damage\n- Before Attack: gain +4 Atk Weight\n- On Hit, inflict 10 Burn; then, inflict 4 Offense Level down and 4 Defense Level Down next turn
   PL: - Zadawane obrażenia +30%\n- Przed atakiem: wagi +4\n- Przy trafieniu nadaje 10 Podpalenia, a w następnej turze 4 Spadki Poziomu Ataku i 4 Spadki Poziomu Obrony
157. [Status [FreishutzOutisEgoBullet_6th] — nazwa] 여섯번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_6th].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_6th]`
   limit: do 40 znaków
   EN: The Sixth Magic Bullet
   PL: Szósta Magiczna Amunicja
158. [Status [FreishutzOutisEgoBullet_6th] — opis] - 공격 시작 전 가중치 6 증가\n- 적중시 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 30)\n- 메인 타겟의 화상 7당 코인을 재사용함 (최대 2회 재사용)\n- 더하기 코인 스킬 기본 위력 16 감소\n- 빼기 코인 스킬 기본 위력 22 감소\n - 더하기 코인 위력 8 감소\n - 빼기 코인 위력 12 감소
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_6th].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Before Attack: gain +6 Atk Weight\n- On Hit, raise the target's Stagger Threshold by damage dealt (max 30)\n- Reuse the Coin for every 7 Burn on the main target (2 times max)\n- Plus Coin Skill Base Power -16\n- Minus Coin Skill Base Power -22\n - Plus Coin Power -8\n - Minus Coin Power -12
   PL: - Przed atakiem: wagi +6\n- Przy trafieniu podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 30)\n- Używa monety ponownie za każde 7 Podpalenia na głównym celu (maks. 2 razy)\n- Moc Bazowa Umiejętności z monetą plus -16\n- Moc Bazowa Umiejętności z monetą minus -22\n- Moc monety plus -8\n- Moc monety minus -12
159. [Status [FreishutzOutisEgoBullet_7th] — nazwa] 일곱번째 마탄
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_7th].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBullet_7th]`
   limit: do 40 znaków
   EN: The Seventh Magic Bullet
   PL: Siódma Magiczna Amunicja
160. [Status [FreishutzOutisEgoBullet_7th] — opis] - 가하는 피해량 +200%\n- 대상의 잃은 체력 1%당 피해량 +2.5% (최대 200%)\n- 공격 시작 전 대상이나 자신의 관통 속성 내성이 2.0 미만이면, 이 공격에 한해 취약(x2.0)으로 변경함\n- 공격 종료 시, 사망함
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBullet_7th].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +200% damage\n- Deal +2.5% damage for every 1% missing HP on target (max 200%)\n- Before Attack: for this attack, if the Pierce Damage Res. on target or on self are less than 2.0, change them to Fatal(x2.0)\n- Attack End: kills this unit
   PL: - Zadawane obrażenia +200%\n- Zadaje +2,5% obrażeń za każdy 1% brakującego HP celu (maks. 200%)\n- Przed atakiem: jeśli Odporność na Przebicie celu lub własna jest niższa niż 2,0, dla tego ataku zmienia ją na Wrażliwość Maksymalną (x2,0)\n- Po zakończeniu ataku umiera
161. [Status [FreishutzOutisEgoBulletCnt] — nazwa] 사수의 탄환
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBulletCnt].name
   kontekst: identyfikator statusu w tekstach: `[FreishutzOutisEgoBulletCnt]`
   limit: do 40 znaków
   EN: Marksman's Bullet
   PL: Pocisk Strzelca Wyborowego
162. [Status [FreishutzOutisEgoBulletCnt] — opis] 사수의 탄환에 따라 사용하는 탄환이 달라짐
   źródło: Bufs.json :: dataList[id=FreishutzOutisEgoBulletCnt].desc
   limit: do 120 znaków
   EN: Uses a different Ammo depending on Marksman's Bullet
   PL: Używana amunicja zależy od Pocisku Strzelca Wyborowego
163. [Status [CoveringFire] — nazwa] 타겟 포착
   źródło: Bufs.json :: dataList[id=CoveringFire].name
   kontekst: identyfikator statusu w tekstach: `[CoveringFire]`
   limit: do 40 znaków
   EN: Target Spotted
   PL: Namierzenie Celu
164. [Status [CoveringFire] — opis] 이 효과를 부여한 대상의 공격 스킬 종료시, 부여 대상이 공격한 적을 스킬 2로 일방 공격함\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: Bufs.json :: dataList[id=CoveringFire].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 2 against the same enemy Unit A attacked with its Skill. Activates at Unit A's Attack End.\n- The Skill used due to this effect does not affect Unit B's upcoming Skills list.
   PL: Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 2 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A.\n- Umiejętność użyta dzięki temu efektowi nie wpływa na nadchodzącą listę Umiejętności B.
165. [Status [FullReload] — nazwa] 재장전
   źródło: Bufs.json :: dataList[id=FullReload].name
   kontekst: identyfikator statusu w tekstach: `[FullReload]`
   limit: do 40 znaków
   EN: Reload
   PL: Przeładowanie
166. [Status [FullReload] — opis] 보유한 탄환을 모두 버리고, 최대치만큼 다시 얻음
   źródło: Bufs.json :: dataList[id=FullReload].desc
   limit: do 120 znaków
   EN: Lose all currently owned Ammo, and reload it back to full
   PL: Zużywa całą posiadaną amunicję i uzupełnia ją do maksimum
167. [Status [Bullet_LogicAtelier] — nazwa] 탄환 - 로직 아틀리에
   źródło: Bufs.json :: dataList[id=Bullet_LogicAtelier].name
   kontekst: identyfikator statusu w tekstach: `[Bullet_LogicAtelier]`
   limit: do 40 znaków
   EN: Ammo - Atelier Logic
   PL: Amunicja - Atelier Logic
168. [Status [Bullet_LogicAtelier] — opis] 특수 탄환\n로직 아틀리에 공방제 특수탄\n- 이 탄환은 외부 효과로 얻거나 값이 증가할 수 없음
   źródło: Bufs.json :: dataList[id=Bullet_LogicAtelier].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unique Ammo\nAtelier Logic Workshop Special Ammo\n- This Ammo's count cannot be gained or lost due to external effects
   PL: Szczególna amunicja\nSpecjalny pocisk warsztatu Atelier Logic\n- Liczby tej amunicji nie można zyskać ani zmienić efektami zewnętrznymi
169. [Status [Retreat_FullStop] — nazwa] 후방 지원 배치
   źródło: Bufs.json :: dataList[id=Retreat_FullStop].name
   kontekst: identyfikator statusu w tekstach: `[Retreat_FullStop]`
   limit: do 40 znaków
   EN: Overwatch Assignment
   PL: Przydział Odwachu
170. [Status [Retreat_FullStop] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n· 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n· 전투 복귀 시 자신의 슬롯 수가 1로 초기화, 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: Bufs.json :: dataList[id=Retreat_FullStop].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death)\n· In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n· When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)\n· W walkach łańcuchowych przekazuje swoje sloty jednostce zastępczej i trafia na koniec kolejki rezerwowych (jeśli w następnej turze nie ma kogo zastąpić, opuszcza walkę całkowicie; przy powrocie wraca w kolejności odwrotu)\n· Wracając do walki zachowuje HP i Poczytalność z chwili odwrotu i traci wszystkie efekty poza nielicznymi wyjątkami (przy Poczytalności poniżej 0 zostaje ona wyzerowana)
171. [Status [LogicAtelierAM] — nazwa] 집중【저격】
   źródło: Bufs.json :: dataList[id=LogicAtelierAM].name
   kontekst: identyfikator statusu w tekstach: `[LogicAtelierAM]`
   limit: do 40 znaków
   EN: Concentration【Sniper】
   PL: Skupienie【Snajper】
172. [Status [LogicAtelierAM] — opis] - 최댓값 : 4\n- 턴 종료시 수치 1 증가
   źródło: Bufs.json :: dataList[id=LogicAtelierAM].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: gain 1 Stack
   PL: - Maks.: 4\n- Na koniec tury wartość rośnie o 1
173. [Status [MeleeCover] — nazwa] 근접 지원
   źródło: Bufs.json :: dataList[id=MeleeCover].name
   kontekst: identyfikator statusu w tekstach: `[MeleeCover]`
   limit: do 40 znaków
   EN: Melee Support
   PL: Wsparcie z Bliska
174. [Status [MeleeCover] — opis] - 이 효과를 부여한 대상의 스킬 종료시, 해당 아군을 공격한 적을 ‘근접 지원’ 스킬로 일방 공격함.\n- 근접 지원 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음
   źródło: Bufs.json :: dataList[id=MeleeCover].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with the 'Melee Support' Skill against the same enemy that attacked Unit A. Activates at Unit A's Skill End.\n- The Skill used due to the 'Melee Support' effect does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością „Wsparcie z Bliska” przeciwko temu samemu wrogowi, który zaatakował A. Aktywuje się po zakończeniu Umiejętności A.\n- Umiejętność użyta dzięki efektowi „Wsparcie z Bliska” nie wpływa na nadchodzącą listę Umiejętności B
175. [Status [RequestedTarget] — nazwa] 의뢰 대상
   źródło: Bufs.json :: dataList[id=RequestedTarget].name
   kontekst: identyfikator statusu w tekstach: `[RequestedTarget]`
   limit: do 40 znaków
   EN: Requested Target
   PL: Cel Zlecenia
176. [Status [RequestedTarget] — opis] 참격, 관통, 타격 중 1.5 이하인 내성 +0.2. 이 버프가 부여된 대상을 처치하면, 모든 E.G.O 자원을 1 얻고 처치한 대상의 정신력을 10 회복시킴
   źródło: Bufs.json :: dataList[id=RequestedTarget].desc
   limit: do 250 znaków
   EN: +0.2 Resistance to Attack Types with 1.5 or less Resistance. If the target with this effect is defeated, gain 1 E.G.O resource for all Affinities, and the unit that defeated the target heals 10 SP
   PL: Jeśli cel z tym wzmocnieniem zostanie pokonany, pokonujący zyskuje po 1 zasobu E.G.O każdego atrybutu i regeneruje 10 Poczytalności
177. [Status [GlowingLantern] — nazwa] 미끼 요정
   źródło: Bufs.json :: dataList[id=GlowingLantern].name
   kontekst: identyfikator statusu w tekstach: `[GlowingLantern]`
   limit: do 40 znaków
   EN: Fairy Lure
   PL: Wabik Wróżek
178. [Status [GlowingLantern] — opis] - 최댓값 5\n- 턴 시작 시 조작 패널에서 가장 왼쪽 슬롯이 도발치 10 얻음\n- 자신의 받는 피해량 + 50%\n- 피격 시 대상에게 파열 1 부여 (대상의 스킬당 최대 3회)\n· 자신의 체력이 최대 체력의 50% 미만이면, 파열 1 추가 부여\n· 대상의 파열 위력이 15 이상이면, 이 효과로 파열을 부여하지 않음\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=GlowingLantern].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: leftmost Slot on the Dashboard gains +10 Aggro\n- Take +50% damage\n- When hit, inflict 1 Rupture against the Attacker (3 times per target's Skill)\n· At less than 50% HP, inflict 1 additional Rupture\n· If the target has 15+ Rupture, this effect does not inflict Rupture\n- Reduced by 1 at Turn End
   PL: - Maks.: 5\n- Na początku tury skrajnie lewy slot na panelu zyskuje +10 Wartości Prowokacji\n- Otrzymywane obrażenia +50%\n- Przy trafieniu nadaje atakującemu 1 Rozdarcia (do 3 razy na Umiejętność atakującego)\n· Przy HP poniżej 50% dodatkowo nadaje 1 Rozdarcia\n· Przy 15 lub więcej Mocy Rozdarcia atakującego ten efekt nie nadaje Rozdarcia\n- Na koniec tury maleje o 1
179. [Status [HoldingBreath] — nazwa] 깊은 들숨
   źródło: Bufs.json :: dataList[id=HoldingBreath].name
   kontekst: identyfikator statusu w tekstach: `[HoldingBreath]`
   limit: do 40 znaków
   EN: Deep Inhale
   PL: Głęboki Wdech
180. [Status [HoldingBreath] — opis] - 최댓값 : 20\n- 크리티컬 발동 시 호흡 위력이 15, 호흡 횟수가 5 이상이면, 호흡 위력을 (보유한 호흡 위력/5)만큼 소모하여 크리티컬 피해량이 (소모한 값 x 4)%만큼 증가하고 수치 1 소모
   źródło: Bufs.json :: dataList[id=HoldingBreath].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- On Crit, at 15+ Poise Potency and 5+ Poise Count, consume (Poise Potency on self / 5) Poise Potency to deal +(Poise Potency consumed x 4)% damage on Critical Hit and lose 1 Stack
   PL: - Maks.: 20\n- Przy trafieniu krytycznym, przy 15 lub więcej Mocy Oddechu i 5 lub więcej Liczników Oddechu, zużywa (Moc Oddechu/5) Mocy Oddechu, by zadać +(zużyta wartość x 4)% obrażeń krytycznych, a wartość maleje o 1
181. [Status [HoldingBreath] — podsumowanie] 크리티컬 피해량 증가
   źródło: Bufs.json :: dataList[id=HoldingBreath].summary
   limit: do 120 znaków
   EN: Deal more Damage on Critical Hit
   PL: Zadaje więcej obrażeń krytycznych
182. [Status [NebulizerInhale] — nazwa] 네뷸라이저 β
   źródło: Bufs.json :: dataList[id=NebulizerInhale].name
   kontekst: identyfikator statusu w tekstach: `[NebulizerInhale]`
   limit: do 40 znaków
   EN: Nebulizer β
   PL: Nebulizer β
183. [Status [NebulizerInhale] — opis] - 최댓값 : 5\n- 이 효과는 이번 전투 동안 유지됨\n- 오만 완전 공명을 발동하였다면 전투 시작 시, 자신과 무작위 아군 (스택)명이 호흡 3 얻고 호흡 횟수 3 증가 (호흡 또는 호흡 횟수를 스스로 사용하거나 획득하는 스킬을 보유한 아군 중 호흡 위력이 낮은 대상에게 우선 적용)
   źródło: Bufs.json :: dataList[id=NebulizerInhale].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- This effect persists throughout the Encounter\n- When activating Pride A-Reson.: on Combat Start, apply 3 Poise and +3 Poise Count on self and (Stack) allies (prioritizes allies that gain or use Poise or Poise Count; among them, prioritize allies with the least Poise Potency)
   PL: - Maks.: 5\n- Efekt utrzymuje się przez całą walkę\n- Po aktywacji Pełnego Rezonansu Pychy: na początku walki nadaje 3 Oddechu i 3 Liczniki Oddechu sobie oraz (stosy) losowym sojusznikom (priorytet dla sojuszników z Umiejętnościami używającymi lub zyskującymi Oddech; wśród nich dla tych z najniższą Mocą Oddechu)
184. [Status [NebulizerInhale] — podsumowanie] 호흡 위력 얻음, 호흡 횟수 증가
   źródło: Bufs.json :: dataList[id=NebulizerInhale].summary
   limit: do 120 znaków
   EN: Gain Poise and Poise Count
   PL: Zyskuje Moc Oddechu, Licznik Oddechu rośnie
185. [Status [Hohenheim_LowMorale] — nazwa] 고뇌
   źródło: Bufs.json :: dataList[id=Hohenheim_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[Hohenheim_LowMorale]`
   limit: do 40 znaków
   EN: Anguish
   PL: Udręka
186. [Status [Hohenheim_LowMorale] — opis] 턴 시작 시, 취약 1, 정신력 회복 효율 감소 2 얻음
   źródło: Bufs.json :: dataList[id=Hohenheim_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: gain 1 Fragile and 2 SP Heal Efficiency Down
   PL: Na początku tury zyskuje 1 Wrażliwości i 2 Spadki Wydajności Leczenia Poczytalności
187. [Status [Hohenheim_Panic] — nazwa] 고뇌
   źródło: Bufs.json :: dataList[id=Hohenheim_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Hohenheim_Panic]`
   (powtórzenie elementu 185 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
188. [Status [Hohenheim_Panic] — opis] 턴 시작 시, 취약 2 정신력 회복 효율 감소 3 얻음
   źródło: Bufs.json :: dataList[id=Hohenheim_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: gain 2 Fragile and 3 SP Heal Efficiency Down
   PL: Na początku tury zyskuje 2 Wrażliwości i 3 Spadki Wydajności Leczenia Poczytalności
189. [Status [BlackCloud] — nazwa] 검은 구름
   źródło: Bufs.json :: dataList[id=BlackCloud].name
   kontekst: identyfikator statusu w tekstach: `[BlackCloud]`
   limit: do 40 znaków
   EN: Dark Cloud
   PL: Czarna Chmura
190. [Status [BlackCloud] — opis] 최댓값 : 1\n이번 턴에 자신이 사용하는 기본 공격 스킬의 코인이 파괴 불가 코인으로 변경되며, 해당 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않고, 코인에서 적에게 부여하는 출혈 효과의 값 +1\n합 패배시 최종 위력 3 증가\n턴 종료시 버프 소멸
   źródło: Bufs.json :: dataList[id=BlackCloud].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nConverts all of this unit's Base Attack Skill Coins used this turn to Unbreakable Coins, prevents damage from Staggering this unit until Skill End, and inflict +1 more of Bleed effects\nOn Clash Lose: gain Final Power +3\nTurn End: this effect expires
   PL: Maks.: 1\nZamienia wszystkie monety bazowych Umiejętności ataku użytych w tej turze w Monety Niezniszczalne, do końca Umiejętności chroni przed oszołomieniem od obrażeń i zwiększa o 1 wartość Krwawienia nadawanego monetami\nPo przegranej w Starciu: Moc Końcowa +3\nNa koniec tury wzmocnienie znika
191. [Status [BlackCloud] — podsumowanie] 공격 스킬이 [파괴 불가 코인]으로 변경되고 효과가 강화됨.
   źródło: Bufs.json :: dataList[id=BlackCloud].summary
   limit: do 120 znaków
   EN: Converts Attack Skill to Unbreakable Coin and gains a new effect
   PL: Zamienia Umiejętność ataku w Monetę Niezniszczalną i zyskuje nowy efekt.
192. [Status [BlackCloudBlade] — nazwa] 흑운도
   źródło: Bufs.json :: dataList[id=BlackCloudBlade].name
   kontekst: identyfikator statusu w tekstach: `[BlackCloudBlade]`
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL: Ostrze Czarnej Chmury
193. [Status [BlackCloudBlade] — opis] 최댓값 : 1\n참격 위력 1 증가\n참격 스킬로 공격 적중시 출혈 1 부여
   źródło: Bufs.json :: dataList[id=BlackCloudBlade].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nGain 1 Slash Power\nInflict 1 Bleed On Hit with Slash Skills
   PL: - Maks. stosów: 1\n- Moc Cięcia +1\n- Przy trafieniu Umiejętnościami Cięcia nadaje Krwawienie 1
194. [Status [BlackCloudBlade] — podsumowanie] 참격 스킬 강화
   źródło: Bufs.json :: dataList[id=BlackCloudBlade].summary
   limit: do 120 znaków
   EN: Enhance Slash Skills
   PL: Wzmacnia Umiejętności Cięcia
195. [Status [EngageToBattle] — nazwa] 임전
   źródło: Bufs.json :: dataList[id=EngageToBattle].name
   kontekst: identyfikator statusu w tekstach: `[EngageToBattle]`
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
196. [Status [EngageToBattle] — opis] 최댓값 : 1\n자신의 스킬, 코인 효과로 출혈 위력, 횟수를 부여할 때 부여하는 값 +1\n이번 전투 동안 참격 위력 증가 1, 참격 피해량 증가 3 얻음
   źródło: Bufs.json :: dataList[id=EngageToBattle].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Value: 1\nBleed Potency and Count inflicted using this unit's Skill or Coin effects: +1\nGain 1 Slash Power Up and 3 Slash DMG Up for the duration of this Encounter
   PL: Maks.: 1\nMoc i Licznik Krwawienia nadawane efektami własnych Umiejętności lub monet: +1\nW tej walce zyskuje 1 Wzrost Mocy Cięcia i 3 Wzrosty Obrażeń Cięcia
197. [Status [EngageToBattle] — podsumowanie] 참격 스킬 강화, 출혈 부여량 증가.
   źródło: Bufs.json :: dataList[id=EngageToBattle].summary
   limit: do 120 znaków
   EN: Enhance Slash Skills and inflict more Bleed
   PL: Wzmacnia Umiejętności Cięcia i nadaje więcej Krwawienia.
198. [Status [CloudWall] — nazwa] 구름 장벽
   źródło: Bufs.json :: dataList[id=CloudWall].name
   kontekst: identyfikator statusu w tekstach: `[CloudWall]`
   limit: do 40 znaków
   EN: Cumulus Wall
   PL: Mur z Chmur
199. [Status [CloudWall] — opis] 최댓값 : 1\n수비 스킬 최종 위력 +1\n‘뒷골목의 규칙’으로 공격 종료시 또는 턴 종료시 버프 소멸
   źródło: Bufs.json :: dataList[id=CloudWall].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nDefense Skill Final Power +1\nThis effect expires at Turn End or after the following attack ends: 'Rules of the Backstreets'
   PL: Maks.: 1\nMoc Końcowa Umiejętności obrony +1\nWzmocnienie znika po zakończeniu ataku lub na koniec tury po użyciu „Zasad Podwórza”
200. [Status [CloudWall] — podsumowanie] 수비 스킬 강화
   źródło: Bufs.json :: dataList[id=CloudWall].summary
   limit: do 120 znaków
   EN: Enhance Defense Skill
   PL: Wzmacnia Umiejętności obrony
201. [Status [NebulizerExhale] — nazwa] 네뷸라이저 α
   źródło: Bufs.json :: dataList[id=NebulizerExhale].name
   kontekst: identyfikator statusu w tekstach: `[NebulizerExhale]`
   limit: do 40 znaków
   EN: Nebulizer α
   PL: Nebulizer α
202. [Status [NebulizerExhale] — opis] - 최댓값 : 5\n- 이 효과는 이번 전투 동안 유지됨\n- 전투 시작시 자신을 포함한 모든 아군이 호흡 위력 1 얻고, 호흡 횟수 1 증가
   źródło: Bufs.json :: dataList[id=NebulizerExhale].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- This effect persists throughout the Encounter\n- Combat Start: on all allies, including this unit, apply 1 Poise Potency and +1 Poise Count
   PL: - Maks.: 5\n- Efekt utrzymuje się przez całą walkę\n- Na początku walki wszyscy sojusznicy, łącznie z tą jednostką, zyskują 1 Mocy Oddechu i 1 Licznika Oddechu
203. [Status [ReleaseBreath] — nazwa] 가쁜 날숨
   źródło: Bufs.json :: dataList[id=ReleaseBreath].name
   kontekst: identyfikator statusu w tekstach: `[ReleaseBreath]`
   limit: do 40 znaków
   EN: Shallow Exhale
   PL: Przyspieszony Wydech
204. [Status [ReleaseBreath] — opis] - 최댓값 : 1\n- 자신의 호흡 위력이 20 이상이면, 자신의 스킬, 코인 효과로 호흡 위력을 얻을 때, 횟수 1 증가.\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=ReleaseBreath].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- At 20+ Poise Potency, gain +1 Count as well whenever this unit gains Poise Potency with Skill and Coin effects\n- Expires at Turn End
   PL: - Maks.: 1\n- Przy 20 lub więcej Mocy Oddechu zyskuje dodatkowo 1 Licznika Oddechu za każdym razem, gdy zyskuje Moc Oddechu efektami Umiejętności lub monet\n- Znika na koniec tury
205. [Status [FirePunchFuel] — nazwa] 12구산 연료
   źródło: Bufs.json :: dataList[id=FirePunchFuel].name
   kontekst: identyfikator statusu w tekstach: `[FirePunchFuel]`
   limit: do 40 znaków
   EN: District 12 Fuel
   PL: Paliwo Dystryktu 12
206. [Status [FirePunchFuel] — opis] 최댓값: 100\n특정 스킬 사용 시 연료가 소모됨.\n수치가 50 이하가 되면, 과열 연료가 됨\n소모한 연료 : {0}
   źródło: Bufs.json :: dataList[id=FirePunchFuel].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Max Stack: 100\nConsumed by certain Skills.\nAt 50- Stack, become Overheated Fuel\nFuel consumed: {0}
   PL: - Maks. stosów: 100\n- Zużywane przez określone Umiejętności\n- Przy wartości 50 lub mniej: Przegrzane Paliwo\n- Zużyte paliwo: {0}
207. [Status [FirePunchFuelOverheated] — nazwa] 과열 연료
   źródło: Bufs.json :: dataList[id=FirePunchFuelOverheated].name
   kontekst: identyfikator statusu w tekstach: `[FirePunchFuelOverheated]`
   limit: do 40 znaków
   EN: Overheated Fuel
   PL: Przegrzane Paliwo
208. [Status [FirePunchFuelOverheated] — opis] 최댓값: 100\n과열 연료 상태에서 12구산 연료를 소모 시, 대신 과열 연료가 소모됨\n이 연료를 소모 시, 12구산 연료가 소모된 것으로 판정됨\n수치가 50 초과시, 12구산 연료가 됨\n소모한 연료 : {0}
   źródło: Bufs.json :: dataList[id=FirePunchFuelOverheated].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Max Stack: 100\nConsuming District 12 Fuel in Overheated Fuel State consumes Overheated Fuel instead\nConsuming Overheated Fuel counts as consuming District 12 Fuel\nAt over 50 Stack, become District 12 Fuel\nFuel consumed: {0}
   PL: - Maks. stosów: 100\n- Zużycie Paliwa z Dystryktu 12 w stanie Przegrzanego Paliwa zużywa zamiast tego Przegrzane Paliwo\n- Zużycie Przegrzanego Paliwa liczone jest jako zużycie Paliwa z Dystryktu 12\n- Przy wartości powyżej 50 staje się Paliwem z Dystryktu 12\n- Zużyte paliwo: {0}
209. [Status [DianxueDonQuixote] — nazwa] 점혈 - 돈키호테
   źródło: Bufs.json :: dataList[id=DianxueDonQuixote].name
   kontekst: identyfikator statusu w tekstach: `[DianxueDonQuixote]`
   limit: do 40 znaków
   EN: Nerve Strike - Don Quixote
   PL: Punkt Witalny - Don Kichot
210. [Status [DianxueDonQuixote] — opis] - 최댓값 : 3\n- 점혈을 부여한 캐릭터가 대상(또는 부위)의 점혈 수치에 따라 다음 효과를 얻음\n· 1스택 : 합 위력 +1\n· 2스택 : 기본 위력 +1\n· 3스택 : 합 위력 +1, 기본 위력 +1\n- 부여한 캐릭터가 다른 대상(또는 부위)에게 이 효과를 부여하면 소멸\n- 다른 캐릭터의 점혈이 부여될 경우, 교체됨 (수치 유지)
   źródło: Bufs.json :: dataList[id=DianxueDonQuixote].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- The unit that inflicted this Nerve Strike gains the following effects based on target's (or targeted Part's) Nerve Strike Stack\n· 1x Stack: Gain Clash Power +1\n· 2x Stack: Gain Base Power +1\n· 3x Stack: Gain Clash Power +1 and Base Power +1\n- Expires if the unit that inflicted it inflicts this effect against a different target (or a different Part)\n- Replaced when another unit inflicts Nerve Strike (Stacks are preserved)
   PL: - Maks.: 3\n- Jednostka, która nadała Punkt Witalny, zyskuje następujące efekty zależnie od wartości Punktu Witalnego celu (lub części):\n· 1 stos: Moc Starcia +1\n· 2 stosy: Moc Bazowa +1\n· 3 stosy: Moc Starcia +1 i Moc Bazowa +1\n- Znika, gdy nadający nada ten efekt innemu celowi (lub innej części)\n- Zastępowany, gdy inna jednostka nada Punkt Witalny (wartość zachowana)
211. [Status [VengeanceBookSinclair] — nazwa] 앙갚음 장부 [싱클레어]
   źródło: Bufs.json :: dataList[id=VengeanceBookSinclair].name
   kontekst: identyfikator statusu w tekstach: `[VengeanceBookSinclair]`
   limit: do 40 znaków
   EN: Book of Vengeance [Sinclair]
   PL: Rejestr Odwetu [Sinclair]
212. [Status [VengeanceBookSinclair] — opis] - 최댓값 : 30\n- 피해량이 (수치)%만큼 증가 (최대 30%)\n- 수치에 따라 다음 턴에 효과 얻음\n· 10 ~ : 타격 피해량 증가 1 얻음\n· 20 ~ : 속도 최댓값 1 증가, 위력 증가 1 얻음\n· 30 : 타격 피해량 증가 2 얻음
   źródło: Bufs.json :: dataList[id=VengeanceBookSinclair].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Deal more damage equal to (Stack)% (max 30%)\n- Gain the following effects next turn based on Stack:\n· At 10+ Stack: gain 1 Blunt DMG Up\n· At 20+ Stack: Max Speed +1, gain 1 Power Up\n· At 30 Stack: gain 2 Blunt DMG Up
   PL: - Maks.: 30\n- Zadawane obrażenia rosną o wartość% (maks. 30%)\n- W następnej turze zyskuje efekty zależnie od wartości:\n· 10 lub więcej: 1 Wzrost Obrażeń Uderzenia\n· 20 lub więcej: maksymalna Szybkość +1 i 1 Wzrost Mocy\n· 30: 2 Wzrosty Obrażeń Uderzenia
213. [Status [VendettaMark] — nazwa] 복수 대상
   źródło: Bufs.json :: dataList[id=VendettaMark].name
   kontekst: identyfikator statusu w tekstach: `[VendettaMark]`
   limit: do 40 znaków
   EN: Vendetta Mark
   PL: Cel Zemsty
214. [Status [VendettaMark] — opis] - 최댓값 : 10 \n- 특정 스킬 또는 패시브에 의해 소모됨\n- 수치 1당 중지 소속 적에게 받는 피해 +2% (최대 20%)\n- 턴 종료 시 이 수치가 가장 높으면, 다음 턴에 형제자매의 앙갚음 대상 1 얻음\n(앙갚음 대상 보유 여부와 별개로 적용되며, 수치가 동일한 경우에는 남은 체력 비율이 더 높은 쪽을 대상으로 함)
   źródło: Bufs.json :: dataList[id=VendettaMark].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Consumed by certain Skills or Passives\n- Take +2% damage from The Middle enemies for every Stack (max 20%)\n- Turn End: The unit that has the highest Stack of this effect gains 1 Sibling Vengeance Mark next turn\n(Counted separately from Vengeance Mark; if more than a single unit has the highest Stack of this effect, this effect targets the one that has a higher HP percentage)
   PL: - Maks.: 10\n- Zużywane przez określone Umiejętności lub pasywy\n- Otrzymuje +2% obrażeń od wrogów Korporacji Środkowego za każdą wartość (maks. 20%)\n- Na koniec tury jednostka z najwyższą wartością zyskuje 1 Celu Odwetu Rodzeństwa w następnej turze\n(liczone osobno od Celu Odwetu; przy remisie efekt dotyczy jednostki z wyższym procentem HP)
215. [Status [RetaliationBookFamily] — nazwa] 형제자매의 앙갚음 대상
   źródło: Bufs.json :: dataList[id=RetaliationBookFamily].name
   kontekst: identyfikator statusu w tekstach: `[RetaliationBookFamily]`
   limit: do 40 znaków
   EN: Sibling Vengeance Mark
   PL: Cel Odwetu Rodzeństwa
216. [Status [RetaliationBookFamily] — opis] - 최댓값 : 1\n- 턴 종료 시, 사라짐\n- 모든 인격의 앙갚음 대상으로 취급됨
   źródło: Bufs.json :: dataList[id=RetaliationBookFamily].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Expires at Turn End\n- Every Identity treats this unit as having their Vengeance Mark
   PL: - Maks.: 1\n- Znika na koniec tury\n- Wszyscy traktują tę jednostkę jak nosiciela swojego Celu Odwetu
217. [Status [BirdCage] — nazwa] 달궈진 새장
   źródło: Bufs.json :: dataList[id=BirdCage].name
   kontekst: identyfikator statusu w tekstach: `[BirdCage]`
   limit: do 40 znaków
   EN: Searing Birdcage
   PL: Rozgrzana Klatka
218. [Status [BirdCage] — opis] - 최댓값: 5\n- 대상에게 화상이 있으면, 수치당 분노 내성 +0.1 (이 효과로 분노 내성은 2.0 초과가 될 수 없음)\n- 턴 종료 시, 다음 턴에 속박을 수치만큼 얻음\n- 턴 종료 시 수치 반으로 감소 (소수점 버림)\n※ 이 효과는 갱신되지 않음
   źródło: Bufs.json :: dataList[id=BirdCage].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\nIf this unit has Burn, Wrath Resistance +0.1 for every Stack (cannot exceed 2.0 Wrath Resistance with this effect)\nTurn End: gain Bind equal to Stack next turn\nTurn End: halve Stack (rounded down)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: Maks.: 5\nJeśli jednostka ma Podpalenie, +0,1 Odporności na Gniew za każdą wartość (tym efektem Odporność nie przekroczy 2,0)\nNa koniec tury zyskuje w następnej turze Spętania równe wartości\nNa koniec tury wartość maleje o połowę (zaokrąglona w dół)\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny
219. [Status [BirdCage] — podsumowanie] 수치당 분노 내성 +0.1
   źródło: Bufs.json :: dataList[id=BirdCage].summary
   limit: do 120 znaków
   EN: Wrath Resistance +0.1 for every Stack
   PL: +0,1 Odporności na Gniew za każdą wartość
220. [Status [WideAreaRampage] — nazwa] 광역 난사
   źródło: Bufs.json :: dataList[id=WideAreaRampage].name
   kontekst: identyfikator statusu w tekstach: `[WideAreaRampage]`
   limit: do 40 znaków
   EN: Unfocused Volley
   PL: Ostrzał Bez Celowania
221. [Status [WideAreaRampage] — opis] - 이 스킬의 코인을 굴릴 때, 공격 대상 중에 하나를 무작위로 선택해 공격\n· 첫 코인은 반드시 메인 공격 대상에게 적중함\n· 모든 적중시 효과, 해당 코인의 피해는 위 효과에서 선택된 공격 대상에게만 적용됨
   źródło: Bufs.json :: dataList[id=WideAreaRampage].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When this Skill flips Coins, each Coin flips against a random enemy among its targets\n· The first Coin always targets the main target\n· All 'On Hit' effects and all damage dealt by each Coin are inflicted only against the random target the Coin selected
   PL: - Przy rzucie monetami tej Umiejętności każda moneta trafia losowo wybranego wroga spośród celów ataku\n· Pierwsza moneta zawsze trafia główny cel\n· Wszystkie efekty przy trafieniu i obrażenia danej monety dotyczą wyłącznie losowego celu wybranego przez tę monetę
222. [Status [WideAreaRampage] — podsumowanie] 공격 대상 중 하나를 무작위로 선택해 공격
   źródło: Bufs.json :: dataList[id=WideAreaRampage].summary
   limit: do 120 znaków
   EN: Attack indiscriminately among targets
   PL: Atakuje losowo wybrany cel spośród wybranych celów
223. [Status [ActivatedEgoPassive] — nazwa] E.G.O 패시브
   źródło: Bufs.json :: dataList[id=ActivatedEgoPassive].name
   kontekst: identyfikator statusu w tekstach: `[ActivatedEgoPassive]`
   limit: do 40 znaków
   EN: E.G.O Passives
   PL: Pasywy E.G.O
224. [Status [ActivatedEgoPassive] — opis] 현재 적용 중인 E.G.O 패시브
   źródło: Bufs.json :: dataList[id=ActivatedEgoPassive].desc
   limit: do 120 znaków
   EN: Active E.G.O Passives
   PL: Aktywne pasywy E.G.O
225. [Status [BurstPoison] — nazwa] 주살【독】
   źródło: Bufs.json :: dataList[id=BurstPoison].name
   kontekst: identyfikator statusu w tekstach: `[BurstPoison]`
   limit: do 40 znaków
   EN: Deathrite【Venom】
   PL: Obrzęd Śmierci【Jad】
226. [Status [BurstPoison] — opis] - 기본값 : 5\n- 대상에게 크리티컬 피해를 받아 파열이 발동될 때, 1 감소\n- 버프 효과에 의해 감소할 때, 공격 레벨 감소 1 또는 방어 레벨 감소 1 얻음 (턴 당 최대 3회)\n버프 효과에 의해 감소할 때, 수치가 0이면, (파열 위력)만큼 탐식 피해를 받음\n※ 이 효과는 갱신되지 않음.
   źródło: Bufs.json :: dataList[id=BurstPoison].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 5\n- When getting Rupture triggered by a Critical Hit from the target, lose 1 Stack\n- When losing Stacks due to this effect, gain 1 Offense Level Down or 1 Defense Level Down (3 times per turn)\n- When losing Stacks due to this effect, if the Stack drops to 0, take Gluttony damage equal to Rupture Potency on self\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Wartość bazowa: 5\n- Gdy Rozdarcie zostanie wywołane przez trafienie krytyczne celu, maleje o 1\n- Tracąc stosy z tego efektu zyskuje 1 Spadek Poziomu Ataku lub 1 Spadek Poziomu Obrony (3 razy na turę)\n- Tracąc stosy z tego efektu, przy wartości 0 otrzymuje obrażenia Obżarstwa równe Mocy Rozdarcia\n※ Ten efekt nie odświeża się.
227. [Status [SnakeStance] — nazwa] 사완
   źródło: Bufs.json :: dataList[id=SnakeStance].name
   kontekst: identyfikator statusu w tekstach: `[SnakeStance]`
   limit: do 40 znaków
   EN: Serpent Arm
   PL: Wężowe Ramię
228. [Status [SnakeStance] — opis] 최댓값: 3\n턴 종료 시, 다음 턴에 호흡 3 얻음, 호흡 횟수 2 증가\n기본 공격 스킬 사용시 대상에게 파열이 있으면, 호흡 5 얻음\n턴 종료 시, 1 감소
   źródło: Bufs.json :: dataList[id=SnakeStance].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nTurn End: gain 3 Poise and +2 Poise Count next turn\nOn Base Attack Skill use, if target has Rupture, gain 5 Poise\nTurn End: lose 1 Stack
   PL: Maks.: 3\nNa koniec tury zyskuje w następnej turze 3 Oddechu i 2 Liczniki Oddechu\nPrzy użyciu bazowej Umiejętności ataku, jeśli cel ma Rozdarcie, zyskuje 5 Oddechu\nNa koniec tury maleje o 1
229. [Status [BurstZilu] — nazwa] 주살【파】
   źródło: Bufs.json :: dataList[id=BurstZilu].name
   kontekst: identyfikator statusu w tekstach: `[BurstZilu]`
   limit: do 40 znaków
   EN: Deathrite 【Fissure】
   PL: Obrzęd Śmierci 【Szczelina】
230. [Status [BurstZilu] — opis] - 기본값 : 3\n- 자신에게 주살이 있는 상태에서 파열이 발동될 때, 수치가 1 감소하고, 다음 턴에 속박 1 부여\n· 해당 효과가 발동할 때 자신에게 다음 턴에 부여되는 속박이 3 이상이면, 속박 부여 대신 수치 2 감소\n- 수치가 0이 될 때, (파열 위력)만큼 탐식 피해를 받음\n※ 이 효과는 갱신되지 않음.
   źródło: Bufs.json :: dataList[id=BurstZilu].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- When getting Rupture triggered while this unit has Deathrite, lose 1 Stack, and gain 1 Bind next turn\n· When this effect activates, if this unit is to gain 3 or more Bind next turn, lose 2 Stacks instead of gaining Bind\n- At 0 Stack, take Gluttony damage equal to Rupture Potency on self\n※ Cannot gain additional Stacks of this effect while it is already active.
   PL: - Wartość bazowa: 3\n- Gdy Rozdarcie zostanie wyzwolone, podczas gdy jednostka ma Obrzęd Śmierci, wartość maleje o 1, a w następnej turze zyskuje 1 Spętania\n· Jeśli przy aktywacji tego efektu jednostka ma otrzymać 3 lub więcej Spętań w następnej turze, zamiast Spętań wartość maleje o 2\n- Gdy wartość spadnie do 0, otrzymuje obrażenia Obżarstwem równe własnej Mocy Rozdarcia\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny.
231. [Status [SupportProtect] — nazwa] 원호 방어
   źródło: Bufs.json :: dataList[id=SupportProtect].name
   kontekst: identyfikator statusu w tekstach: `[SupportProtect]`
   limit: do 40 znaków
   EN: Assist Defense
   PL: Obrona Wsparcia
232. [Status [SupportProtect] — opis] - 최댓값 : 3\n- 아군이 적에게 일방공격 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고, 원호 방어 전용 스킬 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 발동\n- 수비 스킬을 장착한 아군에게는 발동하지 않음\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=SupportProtect].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When an ally is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then, use the unique Skill that activates for Assist Defense\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- Does not activate for allies who equipped Defense Skills\n- Expires at Turn End
   PL: - Maks.: 3\n- Gdy sojusznik ma zostać zaatakowany atakiem niekwestionowanym wroga, zużywa 1 wartości, by przekierować cel ataku wroga na siebie, i używa specjalnej Umiejętności Obrony Wsparcia\n- Gdy Obrona Wsparcia jest u wielu sojuszników, pierwszeństwo ma ten z najwyższą wartością\n- Nie aktywuje się dla sojuszników z wyposażoną Umiejętnością obronną\n- Znika na koniec tury
233. [Status [EnhanceZilu] — nazwa] 천구성도
   źródło: Bufs.json :: dataList[id=EnhanceZilu].name
   kontekst: identyfikator statusu w tekstach: `[EnhanceZilu]`
   limit: do 40 znaków
   EN: Tianjiu Star's Blade
   PL: Ostrze Gwiazdy Tianjiu
234. [Status [EnhanceZilu] — opis] - 최대값 : 20\n- 수치가 10 이상이면, 턴 종료 시 다음 턴에 신속 1 얻음\n- 특정 스킬에 사용됨
   źródło: Bufs.json :: dataList[id=EnhanceZilu].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- At 10+ Stack: at Turn End, gain 1 Haste next turn\n- Used for certain Skills
   PL: - Maks.: 20\n- Przy 10+ stosach: na koniec tury zyskuje 1 Pośpiechu w następnej turze\n- Zużywane przez określone Umiejętności
235. [Status [BurstVulnerableZilu] — nazwa] 붕괴 표식
   źródło: Bufs.json :: dataList[id=BurstVulnerableZilu].name
   kontekst: identyfikator statusu w tekstach: `[BurstVulnerableZilu]`
   limit: do 40 znaków
   EN: Mark of Decay
   PL: Znak Rozkładu
236. [Status [BurstVulnerableZilu] — opis] - 최대값 : 1\n- 탐식 속성 스킬로 받는 피해량 +10%\n- 주살로 받는 피해량 +10%\n- 턴 종료 시 제거
   źródło: Bufs.json :: dataList[id=BurstVulnerableZilu].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +10% damage from Gluttony Skills\n- Take +10% damage from Deathrite\n- Removed at Turn End
   PL: - Maks.: 1\n- Otrzymuje +10% obrażeń od Umiejętności Obżarstwa\n- Otrzymuje +10% obrażeń od Obrzędu Śmierci\n- Usuwany na koniec tury
237. [Status [SupportProtectTypo] — nazwa] 원호 방어
   źródło: Bufs.json :: dataList[id=SupportProtectTypo].name
   kontekst: identyfikator statusu w tekstach: `[SupportProtectTypo]`
   (powtórzenie elementu 231 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
238. [Status [EntangledCurseTalisman] — nazwa] 얽혀버린 저주 부적
   źródło: Bufs.json :: dataList[id=EntangledCurseTalisman].name
   kontekst: identyfikator statusu w tekstach: `[EntangledCurseTalisman]`
   limit: do 40 znaków
   EN: Twisted Curse Talisman
   PL: Spleciony Talizman Klątwy
239. [Status [EntangledCurseTalisman] — opis] - 최댓값 : 10\n- 턴 종료 시 제거\n- 수치가 10 이상이면, 스킬 피해로 30 이상의 피해를 받았을 때 파열 횟수 1 증가, 파열 위력만큼 탐식 피해받음 (턴 당 1회)\n- 이 효과가 제거될 때 다음 턴에 (수치/4)만큼 공격 위력 감소 부여 (최대 2)\n※ 이 효과는 갱신되지 않음
   źródło: Bufs.json :: dataList[id=EntangledCurseTalisman].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Expires at Turn End\n- At 10+ Stack, when taking 30+ damage from a Skill: gain +1 Rupture Count; take Gluttony damage equal to Rupture Potency on self (once per turn)\n- When this effect expires, gain (Stack / 4) Attack Power Down next turn (max 2)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Maks.: 10\n- Usuwany na koniec tury\n- Przy 10 lub więcej stosach, przy otrzymaniu 30 lub więcej obrażeń od Umiejętności: 1 Licznik Rozdarcia i obrażenia Obżarstwem równe własnej Mocy Rozdarcia (raz na turę)\n- Przy usunięciu zyskuje w następnej turze (wartość/4) Spadków Mocy Ataku (maks. 2)\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny
240. [Status [CentipedePoison] — nazwa] 지네 독
   źródło: Bufs.json :: dataList[id=CentipedePoison].name
   kontekst: identyfikator statusu w tekstach: `[CentipedePoison]`
   limit: do 40 znaków
   EN: Centipede Venom
   PL: Trucizna Skolopendry
241. [Status [CentipedePoison] — opis] - 최댓값: 20\n- 턴 종료 시 (수치/4)만큼 다음 턴에 방어 레벨 감소 얻음 (소수점 버림)\n- 턴 종료 시 수치만큼 탐식 피해를 받고, 수치가 반으로 감소 (소수점 버림)\n사망시, 이 유닛 아군 중 지네 독이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 위력만큼 옮겨감
   źródło: Bufs.json :: dataList[id=CentipedePoison].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Turn End: Gain (Stack / 4) Defense Level Down next turn (rounded down)\n- Turn End: Take Gluttony damage equal to Stack, and halve the Stack (rounded down)\nUpon death, transfers to this unit's ally (for Focused Encounters, a different Part) that has none or the least Centipede Venom Stacks.
   PL: - Maks.: 20\n- Na koniec tury zyskuje w następnej turze (stosy/4) Spadków Poziomu Obrony (zaokrąglone w dół)\n- Na koniec tury otrzymuje obrażenia Obżarstwem równe wartości, a wartość maleje o połowę (zaokrąglona w dół)\nPo śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Trucizny Skolopendry lub z jej najmniejszą liczbą
242. [Status [DragonLance] — nazwa] 매화첨[埋花櫼]
   źródło: Bufs.json :: dataList[id=DragonLance].name
   kontekst: identyfikator statusu w tekstach: `[DragonLance]`
   limit: do 40 znaków
   EN: Flower-burying Wedge [埋花櫼]
   PL: Klin Pogrzebania Kwiatów [埋花櫼]
243. [Status [DragonLance] — opis] 기본값: 0\n최댓값: 3\n- 자신의 조작 패널에서 가장 왼쪽의 기본 공격 스킬이 파괴 불가 코인이 됨\n- 턴 시작 시 수치당 공격 레벨 증가 2, 방어 레벨 감소 2 얻음\n- 턴 시작 시 수치가 3 이상이면, 오혈 1 얻음 (전투당 1회)\n- 턴 종료 시 1 증가\n※ 위 효과만으로 증가할 수 있음\n- 사망, 퇴각 시 제거됨\n\n- 이번 턴에 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않고, 피해로 인한 흐트러짐 상태를 해제함.\n이후 해당 턴 동안 피해로 인해 흐트러지거나 사망하지 않고, 해당 턴의 마지막 순서에 '오혈읍루 - 종'스킬을 사용함. 해당 스킬 종료 시 매화첨 제거.\n턴 종료시 체력이 1이 되는 피해를 받은 경우, 다음 턴에 속도에 따라 '오혈읍루 - 종'스킬 사용.
   źródło: Bufs.json :: dataList[id=DragonLance].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 0\nMax Stack: 3\n- All Coins on this unit's leftmost Base Attack Skill on the Dashboard become Unbreakable Coins\n- Turn Start: gain 2 Offense Level Up and 2 Defense Level Down for every Stack\n- Turn Start: at 3+ Stack, gain 1 Tarnished Blood (once per Encounter)\n- Turn End: gain 1 Stack\n※ Cannot raise the effect's Stack by any other means than the ones above\n- Expires upon death or Retreat\n\n- When this unit takes damage that brings their HP down to 0: instead of letting this unit's HP drop below 1, or becoming Staggered or Defeated, use the 'Tears of the Tarnished Blood - The End' Skill at the very end of that turn. Remove the Flower-burying Wedge when the Skill ends.\nWhen this unit takes damage that brings their HP down to 1 at Turn End, use 'Tears of the Tarnished Blood - The End' Skill based on this unit's Speed next turn
   PL: Wartość bazowa: 0\nMaks.: 3\n- Wszystkie monety skrajnie lewej bazowej Umiejętności ataku na panelu stają się Monetami Niezniszczalnymi\n- Na początku tury za każdą wartość: 2 Wzrosty Poziomu Ataku i 2 Spadki Poziomu Obrony\n- Na początku tury, przy wartości 3 lub wyższej, zyskuje 1 Splamionej Krwi (raz na walkę)\n- Na koniec tury wartość rośnie o 1\n※ Efekt rośnie wyłącznie dzięki powyższym regułom\n- Znika po śmierci lub Odwrócie\n\n- Gdy jednostka otrzyma obrażenia redukujące HP do 0: zamiast utraty HP poniżej 1, oszołomienia lub śmierci, używa na samym końcu tej tury Umiejętności „Łzy Splamionej Krwi - Kres”. Po zakończeniu Umiejętności Klin Pogrzebania Kwiatów znika.\nGdy na koniec tury jednostka otrzyma obrażenia redukujące HP do 1, w następnej turze użyje Umiejętności „Łzy Splamionej Krwi - Kres” według własnej Szybkości
244. [Status [CondensedBlood] — nazwa] 오혈
   źródło: Bufs.json :: dataList[id=CondensedBlood].name
   kontekst: identyfikator statusu w tekstach: `[CondensedBlood]`
   limit: do 40 znaków
   EN: Tarnished Blood
   PL: Splamiona Krew
245. [Status [CondensedBlood] — opis] 최댓값: 5\n- 턴 종료 시 수치당 최대 체력의 20%만큼 체력 피해를 받음 (해당 피해로 인해 흐트러지지 않음)\n- 턴 종료 시 1 증가\n- 사망, 퇴각 시 제거됨
   źródło: Bufs.json :: dataList[id=CondensedBlood].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\n- Turn End: take 20% HP damage per Stack (cannot be Staggered by this effect)\n- Gain 1 Stack at Turn End\n- Expires upon death or Retreat
   PL: Maks.: 5\n- Na koniec tury otrzymuje za każdą wartość 20% HP jako obrażenia (nie powodują oszołomienia)\n- Na koniec tury wartość rośnie o 1\n- Znika po śmierci lub Odwrócie
246. [Status [YesdragonSelf] — nazwa] 매화침[埋花針]
   źródło: Bufs.json :: dataList[id=YesdragonSelf].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonSelf]`
   limit: do 40 znaków
   EN: Flower-burying Pin [埋花針]
   PL: Igła Pogrzebania Kwiatów [埋花針]
247. [Status [YesdragonSelf] — opis] 최댓값 : 20\n- 턴 종료시 또는 피격 시 수치 1 증가\n- 수치 5당 공격 레벨 1 증가\n- 이 버프를 보유한 캐릭터가 사망 시, 모든 적에게 수치만큼 탐식 피해를 입히고 파열 5 부여\n- 사망 시 또는 퇴각 시 버프 소멸
   źródło: Bufs.json :: dataList[id=YesdragonSelf].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 20\n- Gain 1 Stack at Turn End or when hit\n- Gain 1 Offense Level per 5 Stack\n- If the unit that has this effect dies, inflict Gluttony damage equal to Stack and inflict 5 Rupture\n- Expires upon death or Retreat
   PL: Maks.: 20\n- Na koniec tury lub przy trafieniu wartość rośnie o 1\n- Za każde 5 wartości: Poziom Ataku +1\n- Po śmierci nosiciela tego wzmocnienia zadaje wszystkim wrogom obrażenia Obżarstwem równe wartości i nadaje 5 Rozdarcia\n- Znika po śmierci, Odwrócie lub na koniec tury
248. [Status [YesdragonNodie] — nazwa] 불허[不許]
   źródło: Bufs.json :: dataList[id=YesdragonNodie].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonNodie]`
   limit: do 40 znaków
   EN: Denial [不許]
   PL: Zakaz [不許]
249. [Status [YesdragonNodie] — opis] 이번 턴에 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않고, 피해로 인한 흐트러짐 상태를 해제함.\n위 효과가 발동한 경우, 턴 종료 시 사망함.\n사망 시, 퇴각 시 또는 턴 종료시 버프 소멸
   źródło: Bufs.json :: dataList[id=YesdragonNodie].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit takes damage that brings their HP down to 0: this unit's HP does not drop below 1; recover from Stagger due to damage.\nIf the above effect activated, dies at Turn End.\nExpires upon death, Retreat, or Turn End
   PL: Gdy jednostka otrzyma obrażenia redukujące HP do 0: jej HP nie spada poniżej 1, a oszołomienie od obrażeń zostaje wyleczone.\nJeśli powyższy efekt się aktywował, jednostka umiera na koniec tury.\nZnika po śmierci, Odwrócie lub na koniec tury
250. [Status [YesdragonBurst] — nazwa] 칼날 가시
   źródło: Bufs.json :: dataList[id=YesdragonBurst].name
   kontekst: identyfikator statusu w tekstach: `[YesdragonBurst]`
   limit: do 40 znaków
   EN: Razor Thorn
   PL: Ostre Ciernie
251. [Status [WaitingXichun] — nazwa] 대[待]
   źródło: Bufs.json :: dataList[id=WaitingXichun].name
   kontekst: identyfikator statusu w tekstach: `[WaitingXichun]`
   limit: do 40 znaków
   EN: Ready [待]
   PL: Oczekiwanie [待]
252. [Status [WaitingXichun] — opis] - 최댓값: 3\n- 대기 해제 또는 복귀할 때까지 자신이 대기, 퇴각 상태였던 턴 수
   źródło: Bufs.json :: dataList[id=WaitingXichun].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Number of turns this unit spent in Retreat or as a Backup unit
   PL: - Maks.: 3\n- Liczba tur spędzonych na Odwrócie lub w rezerwie
253. [Status [StartXichun] — nazwa] 시[始]
   źródło: Bufs.json :: dataList[id=StartXichun].name
   kontekst: identyfikator statusu w tekstach: `[StartXichun]`
   limit: do 40 znaków
   EN: Launcher [始]
   PL: Inicjator [始]
254. [Status [StartXichun] — opis] - 최댓값: 6\n- 자신이 전투에 참여한 턴 수\n- 퇴각 시 제거됨\n- 턴 종료 시 1 증가
   źródło: Bufs.json :: dataList[id=StartXichun].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 6\n- Number of turns this unit spent active in the Encounter\n- Expires upon Retreat\n- Gain 1 Stack at Turn End
   PL: - Maks.: 6\n- Liczba tur aktywnego udziału w walce\n- Znika przy Odwrócie\n- Na koniec tury wartość rośnie o 1
255. [Status [CheerUpXichun] — nazwa] 원[援]
   źródło: Bufs.json :: dataList[id=CheerUpXichun].name
   kontekst: identyfikator statusu w tekstach: `[CheerUpXichun]`
   limit: do 40 znaków
   EN: Assist [援]
   PL: Wsparcie [援]
256. [Status [CheerUpXichun] — opis] - 최댓값: 1\n- 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1, 피해량 +10%
   źródło: Bufs.json :: dataList[id=CheerUpXichun].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- If target has 5+ types of negative effects, Clash Power +1, deal +10% damage
   PL: - Maks.: 1\n- Jeśli cel ma 5 lub więcej rodzajów negatywnych efektów: Moc Starcia +1 i zadawane obrażenia +10%
257. [Status [RetreatForCommon] — nazwa] 전장 퇴각
   źródło: Bufs.json :: dataList[id=RetreatForCommon].name
   kontekst: identyfikator statusu w tekstach: `[RetreatForCommon]`
   limit: do 40 znaków
   EN: Battlefield Retreat
   PL: Odwrót z Pola Bitwy
258. [Status [RetreatForCommon] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n- 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n- 전투 복귀 시 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: Bufs.json :: dataList[id=RetreatForCommon].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death)\n· In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n· When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self save for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)\n- W walkach łańcuchowych przekazuje swoje sloty jednostce zastępczej i trafia na koniec kolejki rezerwowych (jeśli w następnej turze nie ma kogo zastąpić, opuszcza walkę całkowicie; przy powrocie wraca w kolejności odwrotu)\n- Wracając do walki zachowuje HP i Poczytalność z chwili odwrotu i traci wszystkie efekty poza nielicznymi wyjątkami (przy Poczytalności poniżej 0 zostaje ona wyzerowana)
259. [Status [FireBulletPropellant] — nazwa] 작열 추진탄
   źródło: Bufs.json :: dataList[id=FireBulletPropellant].name
   kontekst: identyfikator statusu w tekstach: `[FireBulletPropellant]`
   limit: do 40 znaków
   EN: Scorch Propellant Ammo
   PL: Żarzący się Pocisk Napędowy
260. [Status [FireBulletPropellant] — opis] - 특수 탄환\n- 최댓값 : 15\n- 특정 스킬 사용 시 소모
   źródło: Bufs.json :: dataList[id=FireBulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Stack : 15\n- Consumed when using certain Skills
   PL: - Szczególna amunicja\n- Maks.: 15\n- Zużywana przy użyciu określonych Umiejętności
261. [Status [BulletPropellantAlly] — nazwa] 호표탄
   źródło: Bufs.json :: dataList[id=BulletPropellantAlly].name
   kontekst: identyfikator statusu w tekstach: `[BulletPropellantAlly]`
   limit: do 40 znaków
   EN: Tigermark Round
   PL: Pocisk Tygrysiego Znaku
262. [Status [BulletPropellantAlly] — opis] - 특수 탄환\n- 호표탄, 맹호표탄의 누적 소모 합이 8 이상이면, 패시브로 얻는 천퇴성[天退星]이 신(心) - 천퇴성[天退星]으로 변경\n· 누적 소모 합 : {0}\n- 최댓값 : 12
   źródło: Bufs.json :: dataList[id=BulletPropellantAlly].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Unique Ammo\n- At 8+ (cumulative sum of Tigermark Rounds and Savage Tigermark Rounds spent), gain Shin (心) - Tiantui Star [天退星] instead of Tiantui Star [天退星] from this unit's Passive\n- Cumulative Rounds spent: {0}\n- Max Capacity: 12
   PL: - Szczególna amunicja\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku pasyw zamiast Gwiazdy Tianhui [天退星] przyznaje Serce (心) - Gwiazdę Tianhui [天退星]\n· Łączne zużycie Pocisków: {0}\n- Maks.: 12
263. [Status [BulletPropellantSpecialAlly] — nazwa] 맹호표탄
   źródło: Bufs.json :: dataList[id=BulletPropellantSpecialAlly].name
   kontekst: identyfikator statusu w tekstach: `[BulletPropellantSpecialAlly]`
   limit: do 40 znaków
   EN: Savage Tigermark Round
   PL: Dziki Pocisk Tygrysiego Znaku
264. [Status [BulletPropellantSpecialAlly] — opis] - 특수 탄환\n- 호표탄, 맹호표탄의 누적 소모 합이 8 이상이면, 패시브로 얻는 천퇴성[天退星]이 신(心) - 천퇴성[天退星]으로 변경\n· 누적 소모 합 : {0}\n- 호표탄의 효과가 적용됨\n- 최댓값 : 8
   źródło: Bufs.json :: dataList[id=BulletPropellantSpecialAlly].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Unique Ammo\n- At 8+ (cumulative sum of Tigermark Rounds and Savage Tigermark Rounds spent), gain Shin (心) - Tiantui Star [天退星] instead of Tiantui Star [天退星] from this unit's Passive\n- Cumulative Rounds spent: {0}\n- Actives the same way as Tigermark Round does\n- Max Capacity: 8
   PL: - Szczególna amunicja\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku pasyw zamiast Gwiazdy Tianhui [天退星] przyznaje Serce (心) - Gwiazdę Tianhui [天退星]\n· Łączne zużycie Pocisków: {0}\n- Działa tak samo jak Pocisk Tygrysiego Znaku\n- Maks.: 8
265. [Status [IrritationAlly] — nazwa] 천퇴성[天退星]
   źródło: Bufs.json :: dataList[id=IrritationAlly].name
   kontekst: identyfikator statusu w tekstach: `[IrritationAlly]`
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL: Gwiazda Tianhui [天退星]
266. [Status [IrritationAlly] — opis] - 속도 최솟값, 최댓값 1 증가\n- 자신의 속도가 대상보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 2.5)% (최대 20%)\n- 적에게 스킬로 부여하는 진동 위력과 진동 횟수 부여값 +1\n- 소모한 호표탄, 맹호표탄 합이 8 이상이면, 턴 종료 시 다음 턴에 이 버프가 신(心) - 천퇴성[天退星]으로 변경\n- 최댓값 : 1
   źródło: Bufs.json :: dataList[id=IrritationAlly].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 2.5)% damage (max 20%)\n- Inflict +1 more Tremor Potency and Tremor Count with this unit's Skills\n- If this unit has spent 8+ (sum of Tigermark Round and Savage Tigermark Round): at Turn End, convert this buff to Shin (心) - Tiantui Star [天退星] next turn\n- Max Stack: 1
   PL: - Minimalna i maksymalna Szybkość +1\n- Jeśli Szybkość przewyższa cel o 3 lub więcej, zadaje +(różnica Szybkości x 2,5)% obrażeń (maks. 20%)\n- Umiejętności nadają wrogom o 1 więcej Mocy i Licznika Wstrząsu\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku: na koniec tury wzmocnienie zamienia się w Serce (心) - Gwiazdę Tianhui [天退星]\n- Maks.: 1
267. [Status [HugeIrritationAlly] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: Bufs.json :: dataList[id=HugeIrritationAlly].name
   kontekst: identyfikator statusu w tekstach: `[HugeIrritationAlly]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
268. [Status [HugeIrritationAlly] — opis] - 속도 최솟값, 최댓값 3 증가\n- 자신의 속도가 대상보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 40%)\n- 적에게 스킬로 부여하는 진동 위력과 진동 횟수 부여값 +2\n- 최댓값 : 1
   źródło: Bufs.json :: dataList[id=HugeIrritationAlly].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 40%)\n- Inflict +2 more Tremor Potency and Tremor Count with this unit's Skills\n- Max Stack: 1
   PL: - Minimalna i maksymalna Szybkość +3\n- Jeśli Szybkość przewyższa cel o 3 lub więcej, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 40%)\n- Umiejętności nadają wrogom o 2 więcej Mocy i Licznika Wstrząsu\n- Maks.: 1
269. [Status [BeastEyesAlly] — nazwa] 오버히트
   źródło: Bufs.json :: dataList[id=BeastEyesAlly].name
   kontekst: identyfikator statusu w tekstach: `[BeastEyesAlly]`
   limit: do 40 znaków
   EN: Overheat
   PL: Przegrzanie
270. [Status [BeastEyesAlly] — opis] - 맹호표탄을 얻으면, 이 효과가 사라짐\n- 속도 최솟값, 최댓값 2 증가\n- 기본 공격 스킬의 합 위력이 (호표탄, 맹호표탄의 누적 소모 합/2)만큼 감소(최대 10)하는 대신 다음 효과 얻음 (전부 획득)\n· 누적 소모 합 : {0}\n· 8 ~ : 턴 시작 시 잃은 체력 10%당 보호 1 얻음 (최대 5)\n· 14 ~ : 합 패배 시, 기본 공격 스킬의 파괴 불가 코인 피해량 +(75 + 잃은 체력 비율)% (최대 150%)\n· 20 ~ : 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이)%만큼 증가 (최대 50%, E.G.O 스킬 제외)
   źródło: Bufs.json :: dataList[id=BeastEyesAlly].desc
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: - Loses this effect when this unit gains Savage Tigermark Round\n- Min & Max Speed +2\n- Base Attack Skills Lose (cumulative number of Tigermark & Savage Tigermark Rounds spent / 2) Clash Power (max 10); however, gain the following effects(cumulative):\n· Cumulative Rounds spent: {0}\n· 8+ Rounds spent: Gain 1 Protection for every 10% missing HP on self at Turn Start (max 5)\n· 14+ Rounds spent: On Clash Lose, Unbreakable Coins of this unit's Base Attack Skills deal +(75 + missing HP percentage on self)% damage (max 150%)\n· 20+ Rounds Spent: Deal +(HP percentage difference)% damage against targets with higher remaining HP percentage than this unit (max 50%; except E.G.O Skills)
   PL: - Traci ten efekt przy zyskaniu Dzikiego Pocisku Tygrysiego Znaku\n- Minimalna i maksymalna Szybkość +2\n- Moc Starcia bazowych Umiejętności ataku maleje o (łączna liczba zużytych Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku / 2) (maks. 10); w zamian zyskuje następujące efekty (skumulowane):\n· Łączne zużycie Pocisków: {0}\n· 8+: na początek tury zyskuje 1 Ochrony za każde 10% brakującego HP (maks. 5)\n· 14+: po przegranej w Starciu Niezniszczalne Monety bazowych Umiejętności ataku zadają +(75 + procent brakującego HP)% obrażeń (maks. 150%)\n· 20+: zadaje +(różnica procentów HP)% obrażeń celom o wyższym procentie pozostałego HP (maks. 50%, z wyłączeniem Umiejętności E.G.O)
271. [Status [RoseThorn] — nazwa] 탐식극(貪食棘)
   źródło: Bufs.json :: dataList[id=RoseThorn].name
   kontekst: identyfikator statusu w tekstach: `[RoseThorn]`
   limit: do 40 znaków
   EN: Gluttonous Thorn (貪食棘)
   PL: Kolec Obżarstwa (貪食棘)
272. [Status [RoseThorn] — opis] 최댓값: 9\n\n턴 종료 시, 색욕 공명 수만큼 출혈 횟수를 증가 시키고, 탐식극(貪食棘) 1 감소. (최대 출혈 횟수 증가 값 5)\n\n이 효과를 지닌 채로 출혈 위력을 99 이상으로 부여 되었을 때 초과된 출혈 위력 수치만큼 혈찬을 획득하고, 다음 턴에 획득한 혈찬 수치만큼 방어 레벨 감소를 얻음 (최대 방어 레벨 감소 획득 값 5)
   źródło: Bufs.json :: dataList[id=RoseThorn].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 9\n\nTurn End: gain Bleed Count equal to Lust Reson., then lose 1 Gluttonous Thorn (貪食棘). (max Bleed Count gain: 5)\n\nWhile this unit has this effect, if it gains Bleed Potency beyond 99, increase Bloodfeast equal to the excess Bleed Potency; then, gain Defense Level Down next turn equal to Bloodfeast increased (max Defense Level Down gain: 5)
   PL: Maks.: 9\n\nNa koniec tury zwiększa Licznik Krwawienia o liczbę Rezonansów Żądzy i traci 1 Kolca Obżarstwa (maks. 5 zwiększonych Liczników)\n\nGdy przy tym efekcie Moc Krwawienia zostanie nadana ponad 99, zyskuje Ucztę Krwi równą nadwyżce, a w następnej turze tyle Spadków Poziomu Obrony (maks. 5)
273. [Status [FellBulletPersonality] — nazwa] 흉탄
   źródło: Bufs.json :: dataList[id=FellBulletPersonality].name
   kontekst: identyfikator statusu w tekstach: `[FellBulletPersonality]`
   limit: do 40 znaków
   EN: Fell Bullet
   PL: Mroczny Pocisk
274. [Status [FellBulletPersonality] — opis] 최댓값: 1\n찢어진 추억당 크리티컬 피해량 +3% (최대 18%)\n적중 시 출혈 1 부여 (턴 당 최대 3)\n대상 처치 시 호흡 3 얻음, 자신의 호흡 횟수 2 증가 (턴 당 최대 2회)\n턴 종료 시 제거됨
   źródło: Bufs.json :: dataList[id=FellBulletPersonality].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\n+3% damage on Critical Hit for every Torn Memory (max 18%)\nOn Hit, inflict 1 Bleed (3 per turn)\nOn Kill, gain 3 Poise and +2 Poise Count (2 times per turn)\nExpires at Turn End
   PL: Maks.: 1\n+3% obrażeń krytycznych za każde Naderwane Wspomnienie (maks. 18%)\nPrzy trafieniu nadaje 1 Krwawienia (do 3 razy na turę)\nPo pokonaniu wroga zyskuje 3 Oddechu i 2 Liczniki Oddechu (do 2 razy na turę)\nUsuwany na koniec tury
275. [Status [FellBulletPersonality] — podsumowanie] 크리티컬 피해량 증가, 추가 출혈 부여
   źródło: Bufs.json :: dataList[id=FellBulletPersonality].summary
   limit: do 120 znaków
   EN: Deal more Crit damage, inflict more Bleed
   PL: Zadaje więcej obrażeń krytycznych, nadaje więcej Krwawienia
276. [Status [ChoSuperCharge] — nazwa] 초아광축전
   źródło: Bufs.json :: dataList[id=ChoSuperCharge].name
   kontekst: identyfikator statusu w tekstach: `[ChoSuperCharge]`
   limit: do 40 znaków
   EN: Near-light Superbattery
   PL: Superbateria Pobliskiego Światła
277. [Status [ChoSuperCharge] — opis] - 최대값 : 100\n- 자신이 충전 횟수를 소모할 때, 소모값만큼 이 버프 수치 증가\n- 충전 횟수 최대치 +10\n- 아군이 충전 위력이나 횟수를 얻을 때, 자신의 충전 횟수 1 증가\n- 자신의 스킬로 충전 횟수를 소모할 때, 소모량만큼 추가 1회 소모 (횟수가 부족하면, 부족한 만큼 최대로 소모)\n- 수치 10 당 자신의 스킬 피해량 +10%\n- 수치 20 당, 자신의 공격에 한해 적의 모든 내성 +0.1 . (최대 +0.5. 흐트러짐 상태 제외)\n- 이 버프를 보유한 인격 사망 시, 현재 출전 인원 중 편성 순서가 다음으로 빠른 아군에게 이 버프가 계승되며, 버프 수치가 유지됨\n- 이 버프의 효과는 특수 충전에도 적용됨
   źródło: Bufs.json :: dataList[id=ChoSuperCharge].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- When consuming Charge Count, add the amount consumed to this buff's Stack\n- Max Charge Count Cap +10\n- Gain 1 Charge Count when allies gain Charge Potency or Count\n- When this unit consumes Charge Count with its Skills, consume the same amount of Charge Count 1 more time (when there isn't enough Charge Count, consume as much as available)\n- Deal +10% damage for every 10 Stack\n- Enemies gain +0.1 Resistance against this unit's attacks for every 20 Stack (max +0.5 Resist; does not activate against Staggered enemies)\n- When the Identity with this effect dies, the buff transfers to the ally who is second earliest to this unit in the Deployment order. The Stack carries over as well.\n- This effect works on 'Unique Charge' as well.
   PL: - Maks.: 100\n- Zużywając Licznik Ładowania, dodaje zużytą ilość do stosów wzmocnienia\n- Limit Liczników Ładowania +10\n- Zyskuje 1 Licznika Ładowania, gdy sojusznicy zyskują Moc lub Licznik Ładowania\n- Zużywając Licznik Ładowania Umiejętnościami, zużywa tę samą ilość jeszcze raz (przy niedoborze zużywa maksymalnie tyle, ile jest dostępne)\n- Zadaje +10% obrażeń za każde 10 stosów\n- Wrogowie zyskują +0,1 Odporności na ataki tej jednostki za każde 20 stosów (maks. +0,5; nie działa na oszołomionych)\n- Po śmierci osobowości z tym wzmocnieniem przechodzi na sojusznika następnego w kolejce składu, zachowując stosy\n- Działa także na Szczególne Ładowanie
278. [Status [ShareCharge] — nazwa] 자가 공진 회로
   źródło: Bufs.json :: dataList[id=ShareCharge].name
   kontekst: identyfikator statusu w tekstach: `[ShareCharge]`
   limit: do 40 znaków
   EN: Self Resonance Circuitry
   PL: Obwód Samorezonansu
279. [Status [ShareCharge] — opis] 현재 모든 아군이 보유한 충전 횟수의 총합\n\n아군 충전 횟수 누적 소모량: {0}\n\n스킬 적중 시 피해량 +(현재 아군 충전 횟수 총합 / 3)%\n아군 충전 횟수 누적 소모량 100 당, 모든 아군이 공격 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=ShareCharge].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Total sum of Charge Count currently owned by all allies\n\nCumulative Charge Count consumed by allies: {0}\n\nOn Hit with a Skill: deal +(sum of charge count on all allies / 3)% damage\nAll allies gain 1 Offense Level Up for every 100 cumulative Charge Count consumed by allies
   PL: Łączna suma Liczników Ładowania posiadanych obecnie przez wszystkich sojuszników\n\nSkumulowane zużycie Liczników Ładowania sojuszników: {0}\n\nPrzy trafieniu Umiejętnością: zadaje +(suma Liczników Ładowania sojuszników / 3)% obrażeń\nZa każde 100 skumulowanego zużycia Liczników Ładowania sojuszników wszyscy sojusznicy zyskują 1 Wzrost Poziomu Ataku
280. [Status [WaveSinking] — nazwa] 역류
   źródło: Bufs.json :: dataList[id=WaveSinking].name
   kontekst: identyfikator statusu w tekstach: `[WaveSinking]`
   limit: do 40 znaków
   EN: Reflux
   PL: Refluks
281. [Status [WaveSinking] — opis] - 최대값 : 3\n피격 시, 수치만큼 침잠 위력 얻음\n\n턴 종료시 자신의 정신력이 -30 이하면 아래 효과 적용 (정신력이 없는 적은 침잠 위력 60 이상 보유시 발동)\n- 자신의 (침잠 위력 x 수치)만큼 우울 피해를 받음\n- 자신을 제외한 정신력이 가장 낮은 대상 둘 (환상체의 경우, 부위)에게 역류 1 부여하고, 각 대상의 (침잠 위력 x 수치) 만큼 우울 피해\n- 역류를 보유한 상태로 사망 시, 역류 수치가 가장 높은 아군에게 자신의 역류 수치만큼 역류 부여
   źródło: Bufs.json :: dataList[id=WaveSinking].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\nWhen hit, gain Sinking Potency equal to Stack\n\nTurn End: if this unit has -30 or less SP, activate the following effects (for Non-SP Units, activates at 60+ Sinking Potency)\n- Take (Sinking Potency on self x Stack) Gloom damage\n- Inflict 1 Reflux against 2 other targets with the least SP (for Abnormalities, Parts); then, deal (Sinking Potency x Stack) Gloom damage to both targets, respectively\nIf the unit with Reflux dies, transfer its Reflux Stack to its ally with the highest Reflux stack
   PL: - Maks.: 3\nPrzy trafieniu zyskuje Moc Zatonięcia równą wartości\n\nNa koniec tury, przy Poczytalności -30 lub niższej, aktywuje poniższe efekty (jednostki bez Poczytalności: przy 60 lub więcej Mocy Zatonięcia)\n- Otrzymuje (Moc Zatonięcia x wartość) obrażeń Posępnością\n- Nadaje 1 Refluksu 2 jednostkom (w walkach skupionych: częściom) z najniższą Poczytalnością poza sobą, zadając każdemu (Moc Zatonięcia x wartość) obrażeń Posępnością\n- Jednostka, która umrze z Refluksem, przenosi swoje stosy na sojusznika z najwyższą ich liczbą
282. [Status [HeishouDeathCount] — nazwa] 사중구활[死中求活]
   źródło: Bufs.json :: dataList[id=HeishouDeathCount].name
   kontekst: identyfikator statusu w tekstach: `[HeishouDeathCount]`
   limit: do 40 znaków
   EN: Life from Death [死中求活]
   PL: Życie ze Śmierci [死中求活]
283. [Status [HeishouDeathCount] — opis] - 최댓값 : 5\n- 턴 시작시 아래 효과 적용\n· 수치 1 당 공격 레벨 증가 1 얻음 (최대 5)\n· 수치 2 당 피해량 증가 1 얻음 (최대 2)\n· 수치 3 이상이면 공격 위력 증가 1 얻음
   źródło: Bufs.json :: dataList[id=HeishouDeathCount].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: activate the following\n· Gain 1 Offense Level Up for every 1 Stack (max 5)\n· Gain 1 Damage Up for every 2 Stack (max 2)\n· Gain 1 Attack Power Up at 3+ Stack
   PL: - Maks.: 5\n- Na początku tury aktywuje poniższe efekty\n· Za każdą wartość: 1 Wzrost Poziomu Ataku (maks. 5)\n· Za każde 2 wartości: 1 Wzrost Obrażeń (maks. 2)\n· Przy 3 lub więcej wartościach: 1 Wzrost Mocy Ataku
284. [Status [HeishouCombo] — nazwa] 존명
   źródło: Bufs.json :: dataList[id=HeishouCombo].name
   kontekst: identyfikator statusu w tekstach: `[HeishouCombo]`
   limit: do 40 znaków
   EN: Exalted Command
   PL: Czcigodny Rozkaz
285. [Status [HeishouCombo] — opis] - 이 효과를 부여한 대상의 스킬 종료시, 부여 대상이 공격한 적을 기본 스킬 3으로 일방 공격함 (강화 스킬로 발동되지 않음)\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음\n- 3스킬을 사용할 수 있는 아군이 없으면, 발동되지 않음
   źródło: Bufs.json :: dataList[id=HeishouCombo].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Base Skill 3 against the same enemy unit A attacked with its Skill. Activates at unit A's Attack End. (Does not activate as Empowered Skills)\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.\n- Does not activate if affected ally's Skill 3 is not unlocked.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany bazową Umiejętnością 3 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A. (Nie aktywuje się jako Umiejętność Wzmocniona)\n- Umiejętność użyta jako atak niekwestionowany nie wpływa na nadchodzącą listę Umiejętności B.\n- Nie aktywuje się, gdy Umiejętność 3 sojusznika nie jest odblokowana
286. [Status [HeishouComboCount] — nazwa] 몰아침
   źródło: Bufs.json :: dataList[id=HeishouComboCount].name
   kontekst: identyfikator statusu w tekstach: `[HeishouComboCount]`
   limit: do 40 znaków
   EN: Unrelenting Storm
   PL: Nawałnica
287. [Status [HeishouComboCount] — opis] - 홍원 군주 홍루 인격과 연계를 진행한 횟수\n- 최댓값 : 2\n- 턴 시작시 수치 1 당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음
   źródło: Bufs.json :: dataList[id=HeishouComboCount].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Number of times this unit activated combo with The Lord of Hongyuan Hong Lu Identity\n- Max Stack: 2\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Up for every Stack
   PL: - Liczba wykonanych połączeń z osobowością Władcy Hongyuan Hong Lu\n- Maks.: 2\n- Na początku tury za każdą wartość: 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
288. [Status [HeishouAttack] — nazwa] 뜻에 따라, 베겠습니다.
   źródło: Bufs.json :: dataList[id=HeishouAttack].name
   kontekst: identyfikator statusu w tekstach: `[HeishouAttack]`
   limit: do 40 znaków
   EN: Your Will Guides My Blade.
   PL: Twoja Wola Prowadzi Moje Ostrze.
289. [Status [HeishouAttack] — opis] - 이 효과를 부여한 대상의 공격 스킬 종료 시, 부여 대상이 공격한 적을 스킬 1로 일방 공격 함.\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: Bufs.json :: dataList[id=HeishouAttack].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 1 against the same enemy unit A attacked with its Skill. Activates at unit A's Skill Attack End.\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 1 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku Umiejętności A.\n- Umiejętność użyta jako atak niekwestionowany nie wpływa na nadchodzącą listę Umiejętności B.
290. [Status [HeishouSupportProtect] — nazwa] 호위
   źródło: Bufs.json :: dataList[id=HeishouSupportProtect].name
   kontekst: identyfikator statusu w tekstach: `[HeishouSupportProtect]`
   limit: do 40 znaków
   EN: Lordsguard
   PL: Straż Władcy
291. [Status [HeishouSupportProtect] — opis] - 특수 원호 방어\n- 최댓값 : 1\n- 홍원 군주 홍루가 적에게 일방공격 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고, 홍원 군주 홍루 인격의 '호위' 스킬을 복사하여 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 사용\n- 이 효과는 원호 방어로 간주되며, 원호 방어 수치를 계산할 때 합산됨\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=HeishouSupportProtect].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Assist Defense\n- Max Stack: 1\n- When The Lord of Hongyuan Hong Lu is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then, copy and use The Lord of Hongyuan Hong Lu's 'Lordsguard' Skill\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- This effect counts as Assist Defense, and is counted toward calculating Assist Defense Stacks\n- Expires at Turn End
   PL: - Specjalna Obrona Wsparcia\n- Maks.: 1\n- Gdy Władca Hongyuan Hong Lu ma zostać zaatakowany atakiem niekwestionowanym wroga, zużywa 1 wartości, by przekierować cel ataku na siebie, i kopiuje Umiejętność „Straż Władcy” tej osobowości\n- Gdy Obrona Wsparcia jest u wielu sojuszników, pierwszeństwo ma ten z najwyższą wartością\n- Liczy się jako Obrona Wsparcia i jest wliczana do jej wartości\n- Znika na koniec tury
292. [Status [HeishouSynergy] — nazwa] 모든 흑수의 주인
   źródło: Bufs.json :: dataList[id=HeishouSynergy].name
   kontekst: identyfikator statusu w tekstach: `[HeishouSynergy]`
   limit: do 40 znaków
   EN: Leash-holder of All Heishou
   PL: Trzymający Smycz Wszystkich Heishou
293. [Status [HeishouSynergy] — opis] - 최댓값 : 11\n- 수치 당, 매 턴 시작시 아래 효과 얻음\n· 1 당 속도 최댓값 1 증가 (최대 5), 자신의 스킬 피해량 +1%\n· 2 당 속도 최솟값 1 증가 (최대 2), 방어 레벨 증가 1 얻음 (최대 5)\n· 3 당 공격 레벨 증가 1 얻음 (최대 3)\n· 5 이상이면, 피해량 증가 1 얻고, 모든 흑수 인격에게 공격 레벨 증가 1 부여
   źródło: Bufs.json :: dataList[id=HeishouSynergy].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 11\n- Gain the following effects based on Stack:\n· For every 1 Stack, gain 1 Max Speed (max 5) and deal +1% damage with Skills\n· For every 2 Stack, gain 1 Min Speed (max 2) and 1 Defense Level Up (max 5)\n· For every 3 Stack, gain 1 Offense Level Up (max 3)\n· At 5+ Stack, gain 1 Damage Up and apply 1 Offense Level Up to all Heishou Pack Identities
   PL: - Maks.: 11\n- Na początku każdej tury zyskuje efekty zależnie od wartości:\n· Za każdą wartość: maksymalna Szybkość +1 (maks. 5) i zadawane obrażenia Umiejętnościami +1%\n· Za każde 2 wartości: minimalna Szybkość +1 (maks. 2) i 1 Wzrost Poziomu Obrony (maks. 5)\n· Za każde 3 wartości: 1 Wzrost Poziomu Ataku (maks. 3)\n· Przy 5 lub więcej: 1 Wzrost Obrażeń i 1 Wzrost Poziomu Ataku dla wszystkich osobowości Heishou
294. [Status [HeishouComboCountHonglu] — nazwa] 흑수환염[黑獣丸染]
   źródło: Bufs.json :: dataList[id=HeishouComboCountHonglu].name
   kontekst: identyfikator statusu w tekstach: `[HeishouComboCountHonglu]`
   limit: do 50 znaków
   EN: Heishou Bolus Contamination [黑獣丸染]
   PL: Heishou - Zakażenie [黑獣丸染]
295. [Status [HeishouComboCountHonglu] — opis] - 최댓값 : 11\n- 연계를 진행한 흑수에 따라 홍원 군주 홍루가 강화됨\n- 강화 효과는 중첩됨\n\n· 흑수 - 묘 필두 파우스트 : 받는 스킬 피해 -5%\n· 흑수 - 묘 료슈 : 자신의 속도가 대상보다 빠르면, 피해량 +5%\n· 흑수 - 묘 오티스 : 일방 공격 적중 시, 파열 횟수 1 증가 (턴 당 1회)\n· 흑수 - 사 로쟈 : 크리티컬 적중 시, 파열 1 부여 (턴 당 3회)\n· 흑수 - 사 그레고르 : 파열 피해를 가하면, 호흡 횟수 1 얻음 (턴 당 1회)
   źródło: Bufs.json :: dataList[id=HeishouComboCountHonglu].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 11\n- Empowers The Lord of Hongyuan Hong Lu based on which Heishou he activated combo with\n- The Heishou Bolus Contamination effects can stack with each other\n\n· Heishou - Mao Adept Faust: take -5% damage from Skills\n· Heishou - Mao Ryōshū: if this unit's Speed is faster than the target's, deal +5% damage\n· Heishou - Mao Outis: inflict +1 Rupture Count On Hit with Unopposed Attacks (once per turn)\n· Heishou - Si Rodion: Inflict 1 Rupture On Critical Hit (3 times per turn)\n· Heishou - Si Gregor: Gain +1 Poise Count when dealing Rupture damage (once per turn)
   PL: - Maks.: 11\n- Władca Hongyuan Hong Lu zyskuje wzmocnienia zależnie od Heishou, z którym wykonał połączenie\n- Efekty się kumulują\n\n· Heishou - Mao Adept Faust: otrzymywane obrażenia od Umiejętności -5%\n· Heishou - Mao Ryośu: jeśli Szybkość przewyższa cel, zadawane obrażenia +5%\n· Heishou - Mao Outis: trafienie atakiem niekwestionowanym zwiększa Licznik Rozdarcia o 1 (raz na turę)\n· Heishou - Si Rodion: trafienie krytyczne nadaje 1 Rozdarcia (do 3 razy na turę)\n· Heishou - Si Gregor: zadanie obrażeń Rozdarciem zyskuje 1 Licznik Oddechu (raz na turę)
296. [Status [DarkHongluQiuAndHonglu] — nazwa] 패도를 걷는 자
   źródło: Bufs.json :: dataList[id=DarkHongluQiuAndHonglu].name
   kontekst: identyfikator statusu w tekstach: `[DarkHongluQiuAndHonglu]`
   limit: do 50 znaków
   EN: One Who Walks The Way of the Hegemon
   PL: Kroczący Drogą Hegemona
297. [Status [DarkHongluQiuAndHonglu] — opis] - 홍루의 모든 스킬의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 다음 턴에 자신이 공격 위력 증가 2, 남은 아군이 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: Bufs.json :: dataList[id=DarkHongluQiuAndHonglu].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Skills gain +1 Final Power\n- On Clash Win, 1 ally(including this unit) with the least SP heals 5 SP\n- When an ally dies, next turn, this unit gains 2 Attack Power Up and remaining allies gain 1 Attack Power Up (once per turn)
   PL: - Moc Końcowa wszystkich Umiejętności Hong Lua +1\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- Po śmierci sojusznika ta jednostka zyskuje 2 Wzrosty Mocy Ataku, a pozostali 1 Wzrost Mocy Ataku w następnej turze (raz na turę)
298. [Status [DarkHongluTeaching] — nazwa] 관철
   źródło: Bufs.json :: dataList[id=DarkHongluTeaching].name
   kontekst: identyfikator statusu w tekstach: `[DarkHongluTeaching]`
   limit: do 40 znaków
   EN: Uncompromising Imposition
   PL: Nieustępliwe Narzucanie
299. [Status [DarkHongluTeaching] — opis] 최댓값: 3\n-  턴 종료시, 정신력 5 회복\n- 전투 중 체력이 0이 될 때 체력을 최대 체력만큼 회복함 (수치만큼 발동)\n- 이 버프로 체력을 회복했을 시, 다음 턴에 위력 증가 1 얻음\n- 발동 횟수: {0}
   źródło: Bufs.json :: dataList[id=DarkHongluTeaching].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Max Stack: 3\n- Turn End: heal 5 SP\n- When HP drops to 0 during the Encounter, heal up to max HP (activates as many times as this unit has Stacks)\n- When healed by this effect, gain 1 Power Up next turn\n- Activated: {0} times
   PL: Maks.: 3\n- Na koniec tury odzyskuje 5 Poczytalności\n- Gdy w trakcie walki HP spadnie do 0, odzyskuje HP do Maks. HP (wywoływane tyle razy, ile wynosi wartość)\n- Gdy HP zostanie odzyskane dzięki temu Wzmocnieniu, zyskuje w następnej turze 1 Wzrost Mocy\n- Liczba wywołań: {0}
300. [Status [DarkHongluParryGahwan] — nazwa] 가증스럽군요, 형님.
   źródło: Bufs.json :: dataList[id=DarkHongluParryGahwan].name
   kontekst: identyfikator statusu w tekstach: `[DarkHongluParryGahwan]`
   limit: do 50 znaków
   EN: You're Ridiculous, Big Brother.
   PL: Jesteś Żenujący, Bracie.
301. [Status [DarkHongluParryGahwan] — opis] 가환과 합을 진행할 때, 합 위력 +2
   źródło: Bufs.json :: dataList[id=DarkHongluParryGahwan].desc
   limit: do 120 znaków
   EN: In Clashes against Jia Huan, Clash Power +2
   PL: W Starciach przeciwko Jia Huan: Moc Starcia +2
302. [Status [DarkHonglu_EGOResourceup] — nazwa] 수없이 많은 자들의 피를 흘리게 될지라도…
   źródło: Bufs.json :: dataList[id=DarkHonglu_EGOResourceup].name
   kontekst: identyfikator statusu w tekstach: `[DarkHonglu_EGOResourceup]`
   limit: do 50 znaków
   EN: No Matter How Many Must Bleed...
   PL: Nawet Gdy Musi Krwawić Bez Liku…
303. [Status [DarkHonglu_EGOResourceup] — opis] [홍루 특수 효과]\n- 이번 전투에서 자신의 스킬 공격 종료 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 1회)\n- 피해를 받았을 때, 다음 턴에 참격 피해량 증가 2를 얻음(턴당 1회)
   źródło: Bufs.json :: dataList[id=DarkHonglu_EGOResourceup].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Hong Lu Exclusive Effect]\n- For this Encounter: after using a Skill Attack, gain 2 additional E.G.O resources of the Skill's Affinity (once per turn)\n- When this unit takes damage, it gains 2 Slash DMG Up next turn (once per turn)
   PL: [Specjalny efekt Hong Lua]\n- W tej walce po zakończeniu ataku Umiejętnością zyskuje 2 dodatkowych zasobów E.G.O jej atrybutu (raz na turę)\n- Po otrzymaniu obrażeń zyskuje w następnej turze 2 Wzrosty Obrażeń Cięcia (raz na turę)
304. [Status [DarkHonglu_Xi] — nazwa] 기쁨
   źródło: Bufs.json :: dataList[id=DarkHonglu_Xi].name
   kontekst: identyfikator statusu w tekstach: `[DarkHonglu_Xi]`
   limit: do 40 znaków
   EN: Happiness
   PL: Radość
305. [Status [DarkHonglu_Xi] — opis] - 홍루의 합 위력 +1\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 페이즈에서 1회 보옥 상태가 되지 않음. 보옥 상태로 만드는 스킬과 합 진행 시 합 위력 +5, 해당 스킬과 합에서 승리한 경우, 보옥 상태가 되지 않고 자신의 흐트러짐 해제, 가모의 정신력 10 감소, 가모에게 취약 2 부여\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs.json :: dataList[id=DarkHonglu_Xi].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Clash Power +1\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Nullfies the effect that turns this unit into a Precious Jade once. When clashing against Skills that turns this unit into a Precious Jade, Clash Power +5; if this unit wins that Clash, this unit does not become a Precious Jade, recovers from Stagger, reduces Jia Mu's SP by 10, and inflicts 2 Fragile against Jia Mu\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Starcia Hong Lua +1\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Jednorazowo unieważnia przemianę w Jadeit; w Starciu z Umiejętnością przemieniającą w Jadeit Moc Starcia +5; po wygranej nie następuje przemiana, oszołomienie zostaje wyleczone, Poczytalność Jia Mu maleje o 10, a Jia Mu otrzymuje 2 Wrażliwości\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
306. [Status [DarkHonglu_Le] — nazwa] 기쁨, 즐거움
   źródło: Bufs.json :: dataList[id=DarkHonglu_Le].name
   kontekst: identyfikator statusu w tekstach: `[DarkHonglu_Le]`
   limit: do 40 znaków
   EN: Happiness, Joy
   PL: Radość, Rozkosz
307. [Status [DarkHonglu_Le] — opis] - 홍루의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs.json :: dataList[id=DarkHonglu_Le].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +1\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +1\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
308. [Status [DarkHonglu_Ai] — nazwa] 기쁨, 즐거움, 슬픔
   źródło: Bufs.json :: dataList[id=DarkHonglu_Ai].name
   kontekst: identyfikator statusu w tekstach: `[DarkHonglu_Ai]`
   limit: do 40 znaków
   EN: Happiness, Joy, Sorrow
   PL: Radość, Rozkosz, Smutek
309. [Status [DarkHonglu_Ai] — opis] - 홍루의 최종 위력 +3\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs.json :: dataList[id=DarkHonglu_Ai].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +3\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +3\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
310. [Status [DarkHonglu_Nu] — nazwa] 기쁨, 즐거움, 슬픔, 분노
   źródło: Bufs.json :: dataList[id=DarkHonglu_Nu].name
   kontekst: identyfikator statusu w tekstach: `[DarkHonglu_Nu]`
   limit: do 50 znaków
   EN: Happiness, Joy, Sorrow, Wrath
   PL: Radość, Rozkosz, Smutek, Gniew
311. [Status [DarkHonglu_Nu] — opis] - 홍루의 최종 위력 +5\n- 매 턴 시작 시 모든 아군의 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 전투에서 누적으로 잃은 체력 비율의 30%만큼 피해량 증가 (최대 100%)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: Bufs.json :: dataList[id=DarkHonglu_Nu].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +5\n- Allies heal 5 SP at every Turn Start (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Increases damage dealt by 30% of the total HP percentage this unit has cumulatively lost during this Encounter (max 100%)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +5\n- Na początku każdej tury wszyscy sojusznicy regenerują 5 Poczytalności (łącznie z tą jednostką)\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Zadawane obrażenia rosną o 30% łącznie utraconego procentu HP w tej walce (maks. 100%)\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
312. [Status [ChickenStance] — nazwa] 혈염 [血炎]
   źródło: Bufs.json :: dataList[id=ChickenStance].name
   kontekst: identyfikator statusu w tekstach: `[ChickenStance]`
   limit: do 40 znaków
   EN: Bloodflame [血炎]
   PL: Krwawy Płomień [血炎]
313. [Status [ChickenStance] — opis] - 최댓값: 3\n- 자신의 기본 스킬로 적에게 부여하는 화상, 파열 위력 +1\n- 이 버프를 보유한 상태로 적을 흐트러뜨리거나 처치하면, 정신력 3 회복 (턴 당 3회)\n· 위 효과가 발동했을 때 자신의 정신력이 최대치면, 다음 턴에 공격 레벨 증가 1, 신속 1 얻음\n- 턴 종료시 수치 1 감소
   źródło: Bufs.json :: dataList[id=ChickenStance].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- This unit inflicts +1 more Burn and Rupture Potency with its Base Skills\n- While this unit has this effect, heal 3 SP upon Staggering or killing an enemy (3 times per turn)\n· If this unit's SP is at max when the above effect activates, gain 1 Offense Level Up and 1 Haste next turn\n- Lose 1 Stack at Turn End
   PL: - Maks.: 3\n- Bazowe Umiejętności nadają wrogom o 1 więcej Mocy Podpalenia i Rozdarcia\n- Oszołomienie lub pokonanie wroga regeneruje 3 Poczytalności (do 3 razy na turę)\n· Przy pełnej Poczytalności zyskuje w następnej turze 1 Wzrost Poziomu Ataku i 1 Pośpiechu\n- Na koniec tury wartość maleje o 1
314. [Status [ChickenStance] — podsumowanie] 부여하는 화상, 파열 +1
   źródło: Bufs.json :: dataList[id=ChickenStance].summary
   limit: do 120 znaków
   EN: Inflict +1 more Burn or Rupture
   PL: Nadaje o 1 więcej Podpalenia lub Rozdarcia
315. [Status [LegStrengthHorseYisang] — nazwa] 각력【오】
   źródło: Bufs.json :: dataList[id=LegStrengthHorseYisang].name
   kontekst: identyfikator statusu w tekstach: `[LegStrengthHorseYisang]`
   limit: do 40 znaków
   EN: Strider【Wu】
   PL: Kroczący【Wu】
316. [Status [LegStrengthHorseYisang] — opis] - 최댓값: 3\n- 턴 종료 시 다음 턴에 신속 2, 도발치를 (수치 x 2)만큼 얻음\n- 공격 시작 전 진동 위력을 수치만큼 메인 타겟에게 부여 (턴 당 최대 6)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=LegStrengthHorseYisang].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Haste and (Stack x 2) Aggro next turn\n- Before Attack: inflict (Stack) Tremor Potency against the main target (max 6 per turn)\n- Lose 1 Stack at Turn End
   PL: - Maks.: 3\n- Na koniec tury zyskuje w następnej turze 2 Pośpiechu i (wartość x 2) Wartości Prowokacji\n- Przed atakiem nadaje głównemu celowi Moc Wstrząsu równą wartości (do 6 na turę)\n- Na koniec tury maleje o 1
317. [Status [ConcussionYisang] — nazwa] 뇌진탕
   źródło: Bufs.json :: dataList[id=ConcussionYisang].name
   kontekst: identyfikator statusu w tekstach: `[ConcussionYisang]`
   limit: do 40 znaków
   EN: Concussion
   PL: Wstrząs Mózgu
318. [Status [ConcussionYisang] — opis] - 최댓값: 2\n- 이 효과가 있는 동안 파열 피해와 진동 폭발로 인한 흐트러짐 손상을 1.2배로 받음. (소수점 버림)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=ConcussionYisang].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Multiply the amount of Stagger Threshold raised by Tremor Burst and Rupture damage dealt against this unit by 1.2 (rounded down)\n- Lose 1 Stack at Turn End
   PL: - Maks.: 2\n- Podczas działania tego efektu otrzymywane obrażenia Rozdarciem i podnoszenie Progu Oszołomienia przez Wybuch Wstrząsu mnożą się x 1,2 (zaokrąglone w dół)\n- Na koniec tury maleje o 1
319. [Status [BreakthroughHorse] — nazwa] 적진 주파
   źródło: Bufs.json :: dataList[id=BreakthroughHorse].name
   kontekst: identyfikator statusu w tekstach: `[BreakthroughHorse]`
   limit: do 40 znaków
   EN: Linebreaker
   PL: Przełamanie Linii
320. [Status [BreakthroughHorse] — opis] - 최댓값: 5\n- 턴 시작 시 해당 턴 동안 보호막 (수치 x 10)을 얻음\n- 최댓값일 시, 자신의 최종 위력이 2 증가함\n- 피격 시 한 스킬로 100 이상의 피해를 입었다면 해당 스킬 종료 시 보호 1 획득 (턴 당 2회, 보호막 피해 포함, 키워드로 인한 피해는 판정하지 않음)
   źródło: Bufs.json :: dataList[id=BreakthroughHorse].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain (Stack x 10) Shield for the turn\n- At max Stack, gain 2 Final Power\n- When hit: if this unit took 100+ damage from a single Skill, gain 1 Protection after that Skill ends (2 times per turn; includes damage against Shield HP; does not count damage from Keywords)
   PL: - Maks.: 5\n- Na początku tury zyskuje (wartość x 10) Tarczy na tę turę\n- Przy maksymalnej wartości Moc Końcowa +2\n- Przy otrzymaniu 100 lub więcej obrażeń z jednej Umiejętności zyskuje po jej zakończeniu 1 Ochrony (do 2 razy na turę; wlicza obrażenia Tarczy; nie liczy obrażeń od Słów Kluczowych)
321. [Status [BattlefieldHorse] — nazwa] 호령
   źródło: Bufs.json :: dataList[id=BattlefieldHorse].name
   kontekst: identyfikator statusu w tekstach: `[BattlefieldHorse]`
   limit: do 40 znaków
   EN: Commanding Cry
   PL: Rozkaz Dowódcy
322. [Status [BattlefieldHorse] — opis] - 합 위력 1 증가, 방어 레벨 2 증가\n- 턴 종료 시 제거
   źródło: Bufs.json :: dataList[id=BattlefieldHorse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Clash Power and 2 Defense Level\n- Expires at Turn End
   PL: - Moc Starcia +1 i Poziom Obrony +2\n- Usuwany na koniec tury
323. [Status [VibrationBleeding] — nazwa] 진동 - 과다출혈
   źródło: Bufs.json :: dataList[id=VibrationBleeding].name
   kontekst: identyfikator statusu w tekstach: `[VibrationBleeding]`
   limit: do 40 znaków
   EN: Tremor - Hemorrhage
   PL: Wstrząs - Krwotok
324. [Status [VibrationBleeding] — opis] - 진동 폭발 시 (진동 위력과 출혈 위력의 합/2)만큼 색욕 속성 피해를 입고 출혈 횟수 1 감소\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: Bufs.json :: dataList[id=VibrationBleeding].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Lust Damage equal to (sum of Tremor Potency and Bleed Potency / 2), and lose 1 Bleed Count\n- When hit by Skills that trigger Tremor Burst, raise this unit's Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wybuchu Wstrząsu otrzymuje obrażenia Żądzą równe (suma Mocy Wstrząsu i Mocy Krwawienia / 2) i traci 1 Licznik Krwawienia\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
325. [Status [GazeRyoshu] — nazwa] 시선
   źródło: Bufs.json :: dataList[id=GazeRyoshu].name
   kontekst: identyfikator statusu w tekstach: `[GazeRyoshu]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
326. [Status [GazeRyoshu] — opis] - 최댓값 : 7\n- 시선 1당 료슈에게 받는 피해량과 료슈에게 가하는 피해량 +10%\n- 사망시, 이 유닛 아군 중 시선 또는 경멸이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 옮겨감 ('경멸 밑으로 쏟아지는 경외의 시선' 공격 도중 사망한 경우 해당 효과가 발동하지 않음)\n- 턴 종료시 수치가 7이면, 다음 턴에 경멸로 변환됨
   źródło: Bufs.json :: dataList[id=GazeRyoshu].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- Take and deal +10% damage from and against Ryōshū for every 1 Stack of Gaze\n- On death, transfers to this unit's ally (for Focused Encounters, a different Part) that has no Contempt or Gaze, or has the least Contempt or Gaze (this effect does not activate if this unit was killed during the Skill attack 'Cascading Gaze of Awe Underneath Contempt')\n- Turn End: At 7 Stacks, convert this effect into Contempt next turn
   PL: - Maks.: 7\n- Otrzymuje i zadaje +10% obrażeń od i przeciwko Ryośu za każdą wartość Spojrzenia\n- Po śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Pogardy lub Spojrzenia albo z ich najmniejszą liczbą (nie aktywuje się, gdy śmierć nastąpiła podczas ataku „Kaskadowe Spojrzenie Grozy pod Pogardą”)\n- Na koniec tury, przy wartości 7, w następnej turze zamienia się w Pogardę
327. [Status [ContemptRyoshu] — nazwa] 경멸
   źródło: Bufs.json :: dataList[id=ContemptRyoshu].name
   kontekst: identyfikator statusu w tekstach: `[ContemptRyoshu]`
   limit: do 40 znaków
   EN: Contempt
   PL: Pogarda
328. [Status [ContemptRyoshu] — opis] - 최댓값 : 1\n- 료슈에게 받는 피해량과 료슈에게 가하는 피해량 -50%\n- 경멸이 있는 대상은 시선을 얻을 수 없음\n- 사망시, 이 유닛 아군 중 시선 또는 경멸이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 옮겨감 ('경멸 밑으로 쏟아지는 경외의 시선' 공격 도중 사망한 경우 해당 효과가 발동하지 않음)\n- 턴 종료 시, 소멸하면서 다음 턴에 시선 7 얻음
   źródło: Bufs.json :: dataList[id=ContemptRyoshu].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take and deal -50% damage from and against Ryōshū\n- Targets that have Contempt cannot gain Gaze\n- On death, transfers to this unit's ally (for Focused Encounters, a different Part) that has no Contempt or Gaze, or has the least Contempt or Gaze (this effect does not activate if this unit was killed during the Skill attack 'Cascading Gaze of Awe Underneath Contempt')\n- Turn End: Expires; then, this unit gains 7 Gaze next turn
   PL: - Maks.: 1\n- Otrzymuje i zadaje -50% obrażeń od i przeciwko Ryośu\n- Cele z Pogardą nie mogą zyskać Spojrzenia\n- Po śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Pogardy lub Spojrzenia albo z ich najmniejszą liczbą (nie aktywuje się, gdy śmierć nastąpiła podczas ataku „Kaskadowe Spojrzenie Grozy pod Pogardą”)\n- Na koniec tury znika, a w następnej turze jednostka zyskuje 7 Spojrzeń
329. [Status [CommonExit] — nazwa] 전장 이탈
   źródło: Bufs.json :: dataList[id=CommonExit].name
   kontekst: identyfikator statusu w tekstach: `[CommonExit]`
   limit: do 40 znaków
   EN: Escape Battlefield
   PL: Ucieczka z Pola Bitwy
330. [Status [CommonExit] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)
   źródło: Bufs.json :: dataList[id=CommonExit].desc
   limit: do 150 znaków
   EN: - Turn End: recover from Stagger and escape from the Encounter (excluding forced Staggers; does not count as death)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)
331. [Status [CuredFilm] — nazwa] 경화막
   źródło: Bufs.json :: dataList[id=CuredFilm].name
   kontekst: identyfikator statusu w tekstach: `[CuredFilm]`
   limit: do 40 znaków
   EN: Hardened Shell-Barrier
   PL: Utwardzona Błona
332. [Status [CuredFilm] — opis] - 턴 시작 시, (수치/3)만큼 방어 레벨 증가 얻음 (최대 3, 소수점 버림)\n- 적에게 피격 직전, 경화막을 절반만큼 소모하여 소모한 수치만큼 보호 얻음 (턴당 1회, 소수점 올림)\n- 턴 종료 시, 3 감소\n- 최대 10
   źródło: Bufs.json :: dataList[id=CuredFilm].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain (Stack / 3) Defense Level Up (max 3; rounded down)\n- Immediately before getting hit by an enemy, consume half of Hardened Shell-Barrier and gain Protection equal to the Stack consumed (once per turn, rounded up)\n- Turn End: lose 3 Stack\n- Max Stack: 10
   PL: - Na początku tury zyskuje (stosy/3) Wzrostów Poziomu Obrony (maks. 3; zaokrąglone w dół)\n- Tuż przed trafieniem atakiem wroga zużywa połowę Utwardzonej Błony i zyskuje Ochrony równą zużytej wartości (raz na turę; zaokrąglone w górę)\n- Na koniec tury maleje o 3\n- Maks.: 10
333. [Status [CuredFilm] — podsumowanie] 방어 레벨 증가 얻음\n스킬로 체력 피해 받기 전, 수치를 소모하여 보호 얻음
   źródło: Bufs.json :: dataList[id=CuredFilm].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Defense Level Up\nImmediately before taking damage from Skills, consume Stack to gain Protection
   PL: Zyskuje Wzrost Poziomu Obrony\nTuż przed utratą HP od Umiejętności zużywa stosy, by zyskać Ochronę
334. [Status [Cianjing] — nazwa] 시엔징
   źródło: Bufs.json :: dataList[id=Cianjing].name
   kontekst: identyfikator statusu w tekstach: `[Cianjing]`
   limit: do 40 znaków
   EN: Thunderer
   PL: Thunderer
335. [Status [Cianjing] — opis] - 턴 시작 시, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 턴 종료 시, 1 감소\n- 최대 5
   źródło: Bufs.json :: dataList[id=Cianjing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Offense Level Up and 1 Defense Level Up\n- Turn End: lose 1 Stack\n- Max Stack: 5
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony\n- Na koniec tury maleje o 1\n- Maks.: 5
336. [Status [Cianjing] — podsumowanie] 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: Bufs.json :: dataList[id=Cianjing].summary
   limit: do 120 znaków
   EN: Gain Offense Level Up & Defense Level Up
   PL: Zyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony
337. [Status [SeniorCianjing] — nazwa] 상급 시엔징
   źródło: Bufs.json :: dataList[id=SeniorCianjing].name
   kontekst: identyfikator statusu w tekstach: `[SeniorCianjing]`
   limit: do 40 znaków
   EN: Higher Thunderer
   PL: Wyższy Thunderer
338. [Status [SeniorCianjing] — opis] - 턴 시작 시, 공격 레벨 증가 2, 방어 레벨 증가 2 얻음\n- 턴 종료 시, 1 감소\n- 최대 5
   źródło: Bufs.json :: dataList[id=SeniorCianjing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 2 Offense Level Up and 2 Defense Level Up\n- Turn End: lose 1 Stack\n- Max Stack: 5
   PL: - Na początku tury zyskuje 2 Wzrosty Poziomu Ataku i 2 Wzrosty Poziomu Obrony\n- Na koniec tury maleje o 1\n- Maks.: 5
339. [Status [SeniorCianjing] — podsumowanie] 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: Bufs.json :: dataList[id=SeniorCianjing].summary
   (powtórzenie elementu 336 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
340. [Status [MlynarWaiting] — nazwa] 칼집 속 사람
   źródło: Bufs.json :: dataList[id=MlynarWaiting].name
   kontekst: identyfikator statusu w tekstach: `[MlynarWaiting]`
   limit: do 40 znaków
   EN: Man in Scabbard
   PL: Człowiek w Pochwie
341. [Status [MlynarWaiting] — opis] - 최댓값: 40\n- (수치 / 8) 당 도발치 1 얻음 (최대 5, 소수점 버림, 조작 패널에서 가장 왼쪽의 스킬 슬롯에 적용)\n- (수치 / 20) 당 보호 1 얻음 (최대 2, 소수점 버림)\n- 턴 종료 시 10 증가\n※ 턴당 최대 20 획득 가능
   źródło: Bufs.json :: dataList[id=MlynarWaiting].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 40\n- For every (Stack / 8), gain 1 Aggro (max 5; rounded down; affects the leftmost Skill Slot on the Dashboard)\n- For every (Stack / 20), gain 1 Protection (max 2; rounded down)\n- Gain 10 Stacks at Turn End\n※ Can gain up to 20 per turn
   PL: - Maks.: 40\n- Za każde (wartość/8): 1 Wartości Prowokacji (maks. 5; zaokrąglone w dół; dotyczy skrajnie lewego slotu na panelu)\n- Za każde (wartość/20): 1 Ochrony (maks. 2; zaokrąglone w dół)\n- Na koniec tury wartość rośnie o 10\n※ Maksymalnie 20 na turę
342. [Status [ArrowShiFau] — nazwa] 화살 - 시
   źródło: Bufs.json :: dataList[id=ArrowShiFau].name
   kontekst: identyfikator statusu w tekstach: `[ArrowShiFau]`
   limit: do 40 znaków
   EN: Arrow - Shi
   PL: Strzała - Shi
343. [Status [ArrowShiFau] — opis] - 최솟값: 0\n- 최댓값: 4\n- 특정 스킬 사용 시 화살이 소모됨
   źródło: Bufs.json :: dataList[id=ArrowShiFau].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min Capacity: 0\n- Max Capacity: 4\n- Arrows spent by certain Skills
   PL: - Min.: 0\n- Maks.: 4\n- Zużywana przy użyciu określonych Umiejętności
344. [Status [ArrowInTheEyeFau] — nazwa] 박힌 화살
   źródło: Bufs.json :: dataList[id=ArrowInTheEyeFau].name
   kontekst: identyfikator statusu w tekstach: `[ArrowInTheEyeFau]`
   limit: do 40 znaków
   EN: Lodged Arrow
   PL: Wbita Strzała
345. [Status [ArrowInTheEyeFau] — opis] - 최댓값: 4\n- 턴 시작 시 출혈 위력을 수치만큼 획득\n- 방어 레벨이 수치만큼 감소\n- 턴 종료 시 수치가 2 이상이면 다음 턴에 취약 1 얻음 (턴당 1회)\n- 사망, 퇴각, 효과 해제 및 소멸 시 이 효과가 소멸하고, 동부 시 협회 3과 파우스트에 화살 - 시를 수치만큼 부여
   źródło: Bufs.json :: dataList[id=ArrowInTheEyeFau].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn Start: gain Bleed Potency by Stack\n- Lose Defense Level by Stack\n- Turn End: at 2+ Stack, gain 1 Fragile next turn (once per turn)\n- Expires on: Death, Retreat, buff removal/expiration. When it expires, apply Arrow - Shi to Shi East Section 3 Faust by Stack
   PL: - Maks.: 4\n- Na początku tury zyskuje Moc Krwawienia równą wartości\n- Poziom Obrony maleje o wartość\n- Na koniec tury, przy wartości 2 lub wyższej, zyskuje 1 Wrażliwości w następnej turze (raz na turę)\n- Po śmierci, Odwrócie lub usunięciu efektu nadaje tyle Strzał - Shi, ile wynosiła wartość, osobowości Shi Wschodnia Sekcja 3 Faust
346. [Status [AimForTheGoal] — nazwa] 목표 조준
   źródło: Bufs.json :: dataList[id=AimForTheGoal].name
   kontekst: identyfikator statusu w tekstach: `[AimForTheGoal]`
   limit: do 40 znaków
   EN: Target Aim
   PL: Namierzenie Celu
347. [Status [AimForTheGoal] — opis] - 최댓값: 4\n- 저격 자세가 없다면 소멸
   źródło: Bufs.json :: dataList[id=AimForTheGoal].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Expires if this unit does not have "Ready to Loose"
   PL: - Maks.: 4\n- Znika, gdy jednostka nie ma „Postawy Snajperskiej”
348. [Status [SnipingArrowMode] — nazwa] 저격 자세
   źródło: Bufs.json :: dataList[id=SnipingArrowMode].name
   kontekst: identyfikator statusu w tekstach: `[SnipingArrowMode]`
   limit: do 40 znaków
   EN: Ready to Loose
   PL: Postawa Snajperska
349. [Status [SnipingArrowMode] — opis] - 이 효과 보유 시 아래 효과 적용\n· 가장 왼쪽에 장착한 기본 공격 스킬을 '섬궁'으로 변경하여 전투 시작 시 사용함.\n· 피해, 흐트러짐 손상 효과로 받는 흐트러짐 피해로 인해 흐트러짐 상태가 되지 않음\n· 원호 공격을 사용하지 않음\n- E.G.O 스킬 장착하여 전투를 시작한 경우, 해제됨
   źródło: Bufs.json :: dataList[id=SnipingArrowMode].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When this unit has this effect, activate the following:\n· Converts the leftmost Base Attack Skill on the Dashboard to "Bow's Glimmer", then uses it at Combat Start\n· This unit cannot be Staggered from taking damage, Tremor Burst, or raised Stagger Threshold\n· Does not trigger <noparse>Assist Attack</noparse>\n· Removed if an E.G.O Skill was equipped at Combat Start
   PL: - Posiadając ten efekt, jednostka:\n· Zamienia skrajnie lewą bazową Umiejętność ataku na „Błysk Łuku” i używa jej na początku walki\n· Nie zostaje oszołomiona przez obrażenia, Wybuch Wstrząsu ani podniesienie Progu Oszołomienia\n· Nie wykonuje Ataków Wsparcia\n- Efekt znika, jeśli na początku walki wyposażono Umiejętność E.G.O
350. [Status [AStrokeOfDeath] — nazwa] 절명
   źródło: Bufs.json :: dataList[id=AStrokeOfDeath].name
   kontekst: identyfikator statusu w tekstach: `[AStrokeOfDeath]`
   limit: do 40 znaków
   EN: Liferender
   PL: Kres Życia
351. [Status [AStrokeOfDeath] — opis] - 공격 레벨 2 증가\n- 최종 위력 1 증가\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=AStrokeOfDeath].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2\n- Final Power +1\n- Expires at Turn End
   PL: - Poziom Ataku +2\n- Moc Końcowa +1\n- Usuwany na koniec tury
352. [Status [WOverCharge] — nazwa] 과충전
   źródło: Bufs.json :: dataList[id=WOverCharge].name
   kontekst: identyfikator statusu w tekstach: `[WOverCharge]`
   limit: do 40 znaków
   EN: Overcharge
   PL: Nadładowanie
353. [Status [WOverCharge] — opis] - 최댓값 : 1\n- 행동 불가 상태가 됨 \n- 받는 피해량 10 + (자신의 충전 위력x5)% 만큼 감소 (최대 25%)\n- 턴 시작 시 자신의 충전 위력만큼 충전 역장을 얻음 (최대 5)\n- 턴 종료 시 다음 턴에 충전 횟수 10, 공격 위력 증가 2 얻고 이 버프 소멸\n- 자신의 충전 위력만큼 자신의 가장 왼쪽 슬롯이 도발치를 얻음 (최대 5)\n- 피격 시 다음 턴에 충전 횟수 1, 부하 1 얻음 (턴 당 최대 5)\n- 자신이 흐트러졌거나, 턴 시작 시 패닉 또는 E.G.O 침식 상태면, 이 버프 소멸
   źródło: Bufs.json :: dataList[id=WOverCharge].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value : 1\n- Become Immobilized\n- Take 10 + (Charge Potency on self x 5)% less damage (max 25%)\n- Turn Start: Gain Charge Barrier based on Charge Potency on self (max 5)\n- Turn End: Gain +10 Charge Count and 2 Attack Power Up next turn, and lose this effect\n- Gain Aggro to this unit's leftmost Slot based on Charge Potency on self (max 5)\n- When hit, gain +1 Charge Count and 1 Load next turn (max 5 per turn)\n- If this unit is in Panic or in E.G.O Corrosion at Turn Start, or if this unit is Staggered, lose this effect
   PL: - Maks.: 1\n- Nie może podejmować działań\n- Otrzymywane obrażenia maleją o 10 + (Moc Ładowania x 5)% (maks. 25%)\n- Na początku tury zyskuje Bariery Ładunku równe Mocy Ładowania (maks. 5)\n- Na koniec tury zyskuje w następnej turze 10 Liczników Ładowania i 2 Wzrosty Mocy Ataku, po czym efekt znika\n- Skrajnie lewy slot zyskuje Wartości Prowokacji równe Mocy Ładowania (maks. 5)\n- Przy trafieniu zyskuje w następnej turze 1 Licznik Ładowania i 1 Obciążenia (do 5 razy na turę)\n- W stanie Paniki lub Korozji E.G.O na początku tury albo po oszołomieniu efekt znika
354. [Status [WOverCharge] — podsumowanie] 행동 불가. 받는 피해량 감소. 도발치, 충전 역장 얻음. 다음 턴에 충전 횟수 얻음. 피격 시 부하, 충전 횟수 얻음
   źródło: Bufs.json :: dataList[id=WOverCharge].summary
   limit: do 170 znaków
   EN: Immobilized. Take less damage. Gain Aggro and Charge Barrier. Gain Charge Count next turn. When hit, gain Load and Charge Count
   PL: Nie może działać. Mniej otrzymywanych obrażeń. Prowokacja i Bariera Ładunku. Liczniki Ładowania w następnej turze. Przy trafieniu: Obciążenie i Liczniki Ładowania
355. [Status [BloodArmorMeursault] — nazwa] 경혈 갑주
   źródło: Bufs.json :: dataList[id=BloodArmorMeursault].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmorMeursault]`
   limit: do 40 znaków
   EN: Hardblood Armor
   PL: Pancerz Skondensowanej Krwi
356. [Status [BloodArmorMeursault] — opis] - 최댓값: 5\n- 자신의 체력이 감소한 상태라면, 공격 스킬 종료 시 가한 체력 피해량의 10%만큼 체력을 회복 (턴당 1회, 최대 40회복)\n- 공격 종료 시 체력 피해를 입혔으면 1 감소 (턴당 1회)\n• 색욕 공명 했으면 회복량이 절반으로 감소하는 대신 경혈 갑주 수치가 감소하지 않음
   źródło: Bufs.json :: dataList[id=BloodArmorMeursault].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- If this unit isn't at max HP: after its Skill attack, heal 10% of HP damage dealt (once per turn; max 40 healing)\n- Attack End: If this unit dealt HP damage, lose 1 Stack (once per turn)\n• If Lust Reson. was activated, halve the amount of HP healed, but do not lose any Hardblood Armor Stack
   PL: - Maks.: 5\n- Jeśli HP nie jest pełne: po ataku Umiejętnością leczy 10% zadanych obrażeń HP (raz na turę; maks. 40 leczenia)\n- Po zakończeniu ataku, jeśli zadano obrażenia HP, wartość maleje o 1 (raz na turę)\n• Po Rezonansie Żądzy kwota leczenia maleje o połowę, ale stosy Pancerza Skondensowanej Krwi nie maleją
357. [Status [FocusOnActing] — nazwa] 연기 집중
   źródło: Bufs.json :: dataList[id=FocusOnActing].name
   kontekst: identyfikator statusu w tekstach: `[FocusOnActing]`
   limit: do 40 znaków
   EN: Focused Performance
   PL: Skupienie na Odgrywaniu
358. [Status [FocusOnActing] — opis] - 최댓값: 3\n- <라만차랜드> 소속 인격 전용, 강화 스킬 포함\n- 스킬 1, 스킬 2 최종 위력 +1, 수치당 피해량 +5% (최대 15%)\n- 스킬 3 최종 위력 +2, 수치당 피해량 +10% (최대 30%)\n- 스킬 3 공격 종료 시 또는 턴 시작 시 경혈 갑주가 없으면 1 감소
   źródło: Bufs.json :: dataList[id=FocusOnActing].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- <La Manchaland> Identities only; includes Empowered Skills\n- Skill 1 and Skill 2 gain Final Power +1; deal +5% damage for every Stack (max 15%)\n- Skill 3 gains Final Power +2; deals +10% damage for every Stack (max 30%)\n- Lose 1 Stack when:\n  1) Skill 3 Attack End\n  2) If this unit does not have Hardblood Armor at Turn Start
   PL: - Maks.: 3\n- Tylko dla osobowości <La Manchaland>, łącznie z Umiejętnościami Wzmocnionymi\n- Umiejętności 1 i 2: Moc Końcowa +1 oraz +5% obrażeń za stos (maks. 15%)\n- Umiejętność 3: Moc Końcowa +2 oraz +10% obrażeń za stos (maks. 30%)\n- Maleje o 1 po zakończeniu ataku Umiejętnością 3 albo na początku tury bez Pancerza Skondensowanej Krwi
359. [Status [FocusOnActing] — podsumowanie] 적중시 피해량 증가
   źródło: Bufs.json :: dataList[id=FocusOnActing].summary
   limit: do 120 znaków
   EN: On Hit, deal more damage
   PL: Przy trafieniu zadaje więcej obrażeń
360. [Status [ParadeConcentration] — nazwa] 라만차 퍼레이드
   źródło: Bufs.json :: dataList[id=ParadeConcentration].name
   kontekst: identyfikator statusu w tekstach: `[ParadeConcentration]`
   limit: do 40 znaków
   EN: La Mancha Parade
   PL: Parada La Mancha
361. [Status [ParadeConcentration] — opis] - 최댓값: 4\n- 색욕 속성 스킬로 받는 피해량 +10%\n• 공격 대상이 <라만차랜드> 소속 인격이면 스킬 속성에 상관없이 받는 피해량 +20%\n• 수치가 최댓값이면 <라만차랜드> 소속 인격에게 가하는 피해량 -20%\n- 적중 혹은 피격한 스킬 종료 후 1 감소
   źródło: Bufs.json :: dataList[id=ParadeConcentration].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Take +10% damage from Lust Skills\n• If the target is a <La Manchaland> Identity, take +20% damage regardless of the Skill's Affinity\n• At max Stack, deal -20% damage against <La Manchaland> Identities\n- Lose 1 Stack either after this unit's Skill hits and ends or after the Skill that attacked this unit hits and ends
   PL: - Maks.: 4\n- Otrzymuje +10% obrażeń od Umiejętności Żądzy\n• Jeśli atakującym jest osobowość <La Manchaland>, otrzymuje +20% obrażeń niezależnie od atrybutu Umiejętności\n• Przy maksymalnej wartości zadaje -20% obrażeń osobowościom <La Manchaland>\n- Maleje o 1 po trafieniu i zakończeniu własnej Umiejętności lub Umiejętności, która zaatakowała jednostkę
362. [Status [ParadeConcentration] — podsumowanie] <라만차랜드>소속이면, 피해량 감소
   źródło: Bufs.json :: dataList[id=ParadeConcentration].summary
   limit: do 120 znaków
   EN: <La Manchaland> Identities take less damage
   PL: Osobowości <La Manchaland> otrzymują mniej obrażeń
363. [Status [EmergencyChargeForceField] — nazwa] 비상용 역장 배터리
   źródło: Bufs.json :: dataList[id=EmergencyChargeForceField].name
   kontekst: identyfikator statusu w tekstach: `[EmergencyChargeForceField]`
   limit: do 40 znaków
   EN: Emergency Barrier Battery
   PL: Awaryjna Bateria Bariery
364. [Status [EmergencyChargeForceField] — opis] - 최댓값: 7\n- 흐트러짐 상태가 되면, 비상용 역장 배터리를 전부 소모하고, 소모된 수치만큼 충전 역장 얻음
   źródło: Bufs.json :: dataList[id=EmergencyChargeForceField].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- When Staggered, consume all Emergency Barrier Battery Stack and gain Charge Barrier by the Stack consumed
   PL: - Maks.: 7\n- Po oszołomieniu zużywa wszystkie stosy i zyskuje Bariery Ładunku równe zużytej liczbie
365. [Status [BloodArmorCasting] — nazwa] 주조된 경혈
   źródło: Bufs.json :: dataList[id=BloodArmorCasting].name
   kontekst: identyfikator statusu w tekstach: `[BloodArmorCasting]`
   limit: do 40 znaków
   EN: Hardblood Cast
   PL: Odlew Skondensowanej Krwi
366. [Status [BloodArmorCasting] — opis] - 최댓값: 3\n- 출혈 또는 특수 출혈을 보유한 적과 합을 진행할 때, 합 위력 +1\n- 공격 스킬에서 혈찬을 소모 시 혈찬이 부족하면, 대신 부족한 혈찬 1당 체력 1 소모하여 혈찬을 생성한 후 혈찬 소모 (이 효과로 인해 받는 피해로 흐트러짐이 되지 않고, 체력이 1 미만으로 감소하지 않음)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BloodArmorCasting].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When clashing against enemies with Bleed or Unique Bleed, Clash Power +1\n- When consuming Bloodfeast with an Attack Skill, if there isn't enough Bloodfeast, consume 1 HP for every 1 missing Bloodfeast to generate it before consuming it (the damage from this effect does not Stagger or reduce this unit's HP below 1)\n- Reduced by 1 at Turn End
   PL: - Maks.: 3\n- W Starciach z wrogami z Krwawieniem lub Szczególnym Krwawieniem: Moc Starcia +1\n- Zużywając Ucztę Krwi Umiejętnością ataku, przy niedoborze zużywa 1 HP za każdy brakujący 1 Uczty Krwi, by go wygenerować (obrażenia od tego efektu nie powodują oszołomienia i nie redukują HP poniżej 1)\n- Na koniec tury maleje o 1
367. [Status [HanafudaOne] — nazwa] 짝패 - 송학
   źródło: Bufs.json :: dataList[id=HanafudaOne].name
   kontekst: identyfikator statusu w tekstach: `[HanafudaOne]`
   limit: do 40 znaków
   EN: Hand - Pine Crane Suit
   PL: Ręka - Sosna i Żuraw
368. [Status [HanafudaOne] — opis] - 스킬 1 기본 위력 +2\n- 자신의 가장 왼쪽 슬롯에 <color=#ff0000>분노</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: Bufs.json :: dataList[id=HanafudaOne].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - Skill 1 Base Power +2\n- When this unit equips and uses a <color=#ff0000>Wrath</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 1 +2\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#ff0000>Gniewu</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
369. [Status [HanafudaOne] — podsumowanie] 기본 위력 증가
   źródło: Bufs.json :: dataList[id=HanafudaOne].summary
   limit: do 120 znaków
   EN: Gain Base Power
   PL: Zyskuje Moc Bazową
370. [Status [HanafudaTwo] — nazwa] 짝패 - 억새
   źródło: Bufs.json :: dataList[id=HanafudaTwo].name
   kontekst: identyfikator statusu w tekstach: `[HanafudaTwo]`
   limit: do 40 znaków
   EN: Hand - Susuki Grass Suit
   PL: Ręka - Trawa Susuki
371. [Status [HanafudaTwo] — opis] - 스킬 2 기본 위력 +1\n- 자신의 가장 왼쪽 슬롯에 <color=#fbc82b>나태</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: Bufs.json :: dataList[id=HanafudaTwo].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#fbc82b>, </color>, \n
   EN: - Skill 2 Base Power +1\n- When this unit equips and uses a <color=#fbc82b>Sloth</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 2 +1\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#fbc82b>Lenistwa</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
372. [Status [HanafudaTwo] — podsumowanie] 기본 위력 증가
   źródło: Bufs.json :: dataList[id=HanafudaTwo].summary
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Status [HanafudaThree] — nazwa] 짝패 - 청벚꽃
   źródło: Bufs.json :: dataList[id=HanafudaThree].name
   kontekst: identyfikator statusu w tekstach: `[HanafudaThree]`
   limit: do 40 znaków
   EN: Hand - Blue Sakura Suit
   PL: Ręka - Błękitna Sakura
374. [Status [HanafudaThree] — opis] - 스킬 3 기본 위력 +1\n- 자신의 가장 왼쪽 슬롯에 <color=#15c3ee>우울</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: Bufs.json :: dataList[id=HanafudaThree].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#15c3ee>, </color>, \n
   EN: - Skill 3 Base Power +1\n- When this unit equips and uses a <color=#15c3ee>Gloom</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 3 +1\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#15c3ee>Posępności</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
375. [Status [HanafudaThree] — podsumowanie] 기본 위력 증가
   źródło: Bufs.json :: dataList[id=HanafudaThree].summary
   (powtórzenie elementu 369 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
376. [Status [HanafudaCombo] — nazwa] 광【光】
   źródło: Bufs.json :: dataList[id=HanafudaCombo].name
   kontekst: identyfikator statusu w tekstach: `[HanafudaCombo]`
   limit: do 40 znaków
   EN: Bright【光】
   PL: Jasne【光】
377. [Status [HanafudaCombo] — opis] - 위력 : 기본값 0, 최댓값 5\n- 횟수 : 기본값 3, 최댓값 3\n\n- 턴 시작 시 위력당 공격 레벨 증가 1 얻음\n- 턴 시작 시 횟수 1 감소
   źródło: Bufs.json :: dataList[id=HanafudaCombo].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Potency : Base 0, Max 5\n- Count : Base 3, Max 3\n\n- Turn Start: gain 1 Offense Level Up for every Potency\n- Turn Start: lose 1 Stack
   PL: - Moc: baza 0, maks. 5\n- Licznik: baza 3, maks. 3\n\n- Na początku tury za każdą Moc: 1 Wzrost Poziomu Ataku\n- Na początku tury Licznik maleje o 1
378. [Status [HurtNightStiletto] — nazwa] 상처
   źródło: Bufs.json :: dataList[id=HurtNightStiletto].name
   kontekst: identyfikator statusu w tekstach: `[HurtNightStiletto]`
   limit: do 40 znaków
   EN: Open Wound
   PL: Otwarta Rana
379. [Status [HurtNightStiletto] — opis] - 최댓값: 2\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 수치가 2면 다음 턴에 깊은 상처로 변환됨
   źródło: Bufs.json :: dataList[id=HurtNightStiletto].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Gain 1 Bind next turn\n- Turn End: At 2 Stack, replace this effect with Deep Wound next turn
   PL: - Maks.: 2\n- Na koniec tury zyskuje w następnej turze 1 Spętania\n- Na koniec tury, przy wartości 2, w następnej turze zamienia się w Głęboką Ranę
380. [Status [HurtNightStiletto] — podsumowanie] 다음 턴에 속박 얻음
   źródło: Bufs.json :: dataList[id=HurtNightStiletto].summary
   limit: do 120 znaków
   EN: Gain Bind next turn
   PL: Zyskuje Spętanie w następnej turze
381. [Status [CriHurtNightStiletto] — nazwa] 깊은 상처
   źródło: Bufs.json :: dataList[id=CriHurtNightStiletto].name
   kontekst: identyfikator statusu w tekstach: `[CriHurtNightStiletto]`
   limit: do 40 znaków
   EN: Deep Wound
   PL: Głęboka Rana
382. [Status [CriHurtNightStiletto] — opis] - 기본값: 3\n- 진동 폭발 시 출혈 횟수 1 증가 (턴당 2회)\n- 상처를 얻을 수 없음 (집중 전투일 경우, 부위로 판정)\n- 턴 종료 시 다음 턴에 (수치 - 1)만큼 속박 얻음\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=CriHurtNightStiletto].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- On Tremor Burst, gain +1 Bleed Count (2 times per turn)\n- Cannot gain Open Wound (in Focused Encounters, the Part)\n- Turn End: Gain (Stack - 1) Bind next turn\n- Turn End: Reduce Stack by 1
   PL: - Wartość bazowa: 3\n- Przy Wybuchu Wstrząsu zyskuje 1 Licznik Krwawienia (do 2 razy na turę)\n- Nie może zyskać Otwartej Rany (w walkach skupionych: dotyczy części)\n- Na koniec tury zyskuje w następnej turze (wartość - 1) Spętań\n- Na koniec tury wartość maleje o 1
383. [Status [CriHurtNightStiletto] — podsumowanie] 출혈 횟수 증가\n다음 턴에 속박 얻음
   źródło: Bufs.json :: dataList[id=CriHurtNightStiletto].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Bleed Count\nGain Bind next turn
   PL: Zyskuje Licznik Krwawienia\nZyskuje Spętanie w następnej turze
384. [Status [HorrHurtNightStiletto] — nazwa] 치명적인 상처
   źródło: Bufs.json :: dataList[id=HorrHurtNightStiletto].name
   kontekst: identyfikator statusu w tekstach: `[HorrHurtNightStiletto]`
   limit: do 40 znaków
   EN: Fatal Wound
   PL: Rana Śmiertelna
385. [Status [HorrHurtNightStiletto] — opis] - 기본값: 3\n- 진동 폭발 시 출혈 횟수 3 증가 (턴당 2회)\n- 상처를 얻을 수 없음 (집중 전투일 경우, 부위로 판정)\n- 턴 종료 시 다음 턴에 수치만큼 속박 얻음\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=HorrHurtNightStiletto].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- On Tremor Burst, gain +3 Bleed Count (2 times per turn)\n- Cannot gain Open Wound (in Focused Encounters, the Part)\n- Turn End: Gain Bind equal to Stack next turn\n- Turn End: Reduce Stack by 1
   PL: - Wartość bazowa: 3\n- Przy Wybuchu Wstrząsu zyskuje 3 Liczniki Krwawienia (do 2 razy na turę)\n- Nie może zyskać Otwartej Rany (w walkach skupionych: dotyczy części)\n- Na koniec tury zyskuje w następnej turze Spętania równe wartości\n- Na koniec tury wartość maleje o 1
386. [Status [HorrHurtNightStiletto] — podsumowanie] 출혈 횟수 증가\n다음 턴에 속박 얻음
   źródło: Bufs.json :: dataList[id=HorrHurtNightStiletto].summary
   (powtórzenie elementu 383 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Status [GrownHorns] — nazwa] 발각[發角]
   źródło: Bufs.json :: dataList[id=GrownHorns].name
   kontekst: identyfikator statusu w tekstach: `[GrownHorns]`
   limit: do 40 znaków
   EN: Burgeoning of Horns [發角]
   PL: Wyrastanie Rogów [發角]
388. [Status [GrownHorns] — opis] - 최댓값 : 3\n- 자신의 기본 스킬로 적에게 부여하는 파열, 침잠 위력 +1\n- 턴 종료 시, 1 감소
   źródło: Bufs.json :: dataList[id=GrownHorns].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max value: 3\n- This unit's Base Skills inflict +1 more of Rupture and Sinking Potency\n- Turn End: Lose 1 Stack
   PL: - Maks. wartości: 3\n- Bazowe Umiejętności tej jednostki nadają +1 Mocy Rozdarcia i Zatonięcia\n- Na koniec tury maleje o 1
389. [Status [GrownHorns] — podsumowanie] 부여하는 파열, 침잠 위력 +1
   źródło: Bufs.json :: dataList[id=GrownHorns].summary
   limit: do 120 znaków
   EN: Inflict +1 more of Rupture and Sinking Potency
   PL: Nadaje o 1 więcej Mocy Rozdarcia i Zatonięcia
390. [Status [CrushMarks] — nazwa] 파쇄흔
   źródło: Bufs.json :: dataList[id=CrushMarks].name
   kontekst: identyfikator statusu w tekstach: `[CrushMarks]`
   limit: do 40 znaków
   EN: Shattermark
   PL: Znamiona Roztrzaskania
391. [Status [CrushMarks] — opis] - 탐식 속성, 우울 속성 스킬로 피격 시 받는 피해량 +10%\n- 정신력이 있는 대상이면, 패닉 유형이 '파쇄흔'으로 변경됨\n- 정신력이 없는 대상이면, 합 위력 -1\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 파쇄흔 패닉 효과\n- 사기 저하 : 자신의 합 위력 -1, 방어 레벨 -2\n- 패닉 : 자신의 합 위력 -2, 방어 레벨 -3
   źródło: Bufs.json :: dataList[id=CrushMarks].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gluttony and Gloom Skills\n- SP Units: change their Panic Type to "Shattermark"\n- Non-SP Units: Clash Power -1\n- Turn End: Reduce 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Shattermark Panic-type Effects\n- Low Morale: Clash Power -1, Defense Level -2 on self\n- Panic: Clash Power -2, Defense Level -3 on self
   PL: - Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Znamiona Roztrzaskania”\n- Jednostki bez Poczytalności: Moc Starcia -1\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Znamion Roztrzaskania”\n- Spadek Moralu: Moc Starcia -1 i Poziom Obrony -2\n- Panika: Moc Starcia -2 i Poziom Obrony -3
392. [Status [CrushMarks] — podsumowanie] 탐식 속성, 우울 속성 스킬 피격 시 받는 피해량 +10%\n- 정신력이 있으면, 패닉 유형이 '파쇄흔'으로 변경\n- 정신력이 없으면, 더하기 코인 앞면 확률 -10%
   źródło: Bufs.json :: dataList[id=CrushMarks].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +10% damage from Gluttony and Gloom Skills\n- SP Units: change their Panic Type to "Shattermark"\n- Non-SP Units: -10% chance to flip Heads for Plus Coins
   PL: Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Jednostki z Poczytalnością zmieniają typ Paniki na „Ślad Roztrzaskania”\n- Jednostki bez Poczytalności: szansa na Awersy monet Plus -10%
393. [Status [CrushMarks_Main] — nazwa] 파쇄흔
   źródło: Bufs.json :: dataList[id=CrushMarks_Main].name
   kontekst: identyfikator statusu w tekstach: `[CrushMarks_Main]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Status [CrushMarks_Main] — opis] - 탐식 속성, 우울 속성 스킬로 피격 시 받는 피해량 +10%\n- 정신력이 있는 대상이면, 패닉 유형이 '파쇄흔'으로 변경됨\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=CrushMarks_Main].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +10% damage from Gluttony and Gloom Skills\n- SP Units: change their Panic Type to "Shattermark"\n- Turn End: Reduce 1 Stack
   PL: - Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Jednostki z Poczytalnością zmieniają typ Paniki na „Ślad Roztrzaskania”\n- Na koniec tury maleje o 1
395. [Status [CrushMarks_Main] — podsumowanie] 탐식 속성, 우울 속성 스킬 피격 시 받는 피해량 +10%\n- 패닉 유형이 '파쇄흔'으로 변경
   źródło: Bufs.json :: dataList[id=CrushMarks_Main].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +10% damage from Gluttony and Gloom Skills\n- Change Panic Type to "Shattermark"
   PL: Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Zmienia typ Paniki na „Ślad Roztrzaskania”
396. [Status [CrushMarks_Sub] — nazwa] 파쇄흔
   źródło: Bufs.json :: dataList[id=CrushMarks_Sub].name
   kontekst: identyfikator statusu w tekstach: `[CrushMarks_Sub]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Status [CrushMarks_Sub] — opis] - 탐식 속성, 우울 속성 스킬로 피격 시 받는 피해량 +10%\n- 정신력이 없는 대상이면, 합 위력 -1\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=CrushMarks_Sub].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gluttony and Gloom Skills\n- Non-SP Units: Clash Power -1\n- Turn End: Reduce 1 Stack
   PL: - Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Jednostki bez Poczytalności: Moc Starcia -1\n- Na koniec tury maleje o 1
398. [Status [CrushMarks_Sub] — podsumowanie] 탐식 속성, 우울 속성 스킬 피격 시 받는 피해량 +10%\n- 합 위력 -1
   źródło: Bufs.json :: dataList[id=CrushMarks_Sub].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +10% damage from Gluttony and Gloom Skills\n- Clash Power -1
   PL: Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Moc Starcia -1
399. [Status [CrushMarks_LowMorale] — nazwa] 파쇄흔
   źródło: Bufs.json :: dataList[id=CrushMarks_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[CrushMarks_LowMorale]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
400. [Status [CrushMarks_LowMorale] — opis] - 사기 저하\n- 자신의 합 위력 -1, 방어 레벨 -2
   źródło: Bufs.json :: dataList[id=CrushMarks_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1, Defense Level -2
   PL: - Niskie Morale\n- Moc Starcia -1, Poziom Obrony -2
401. [Status [CrushMarks_LowMorale] — podsumowanie] 자신의 합 위력 -1, 방어 레벨 -2
   źródło: Bufs.json :: dataList[id=CrushMarks_LowMorale].summary
   limit: do 120 znaków
   EN: Clash Power -1, Defense Level -2
   PL: Moc Starcia -1, Poziom Obrony -2
402. [Status [CrushMarks_Panic] — nazwa] 파쇄흔
   źródło: Bufs.json :: dataList[id=CrushMarks_Panic].name
   kontekst: identyfikator statusu w tekstach: `[CrushMarks_Panic]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
403. [Status [CrushMarks_Panic] — opis] - 패닉\n- 자신의 합 위력 -2, 방어 레벨 -3
   źródło: Bufs.json :: dataList[id=CrushMarks_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -2, Defense Level -3
   PL: - Panika\n- Moc Starcia -2, Poziom Obrony -3
404. [Status [CrushMarks_Panic] — podsumowanie] 자신의 합 위력 -2, 방어 레벨 -3
   źródło: Bufs.json :: dataList[id=CrushMarks_Panic].summary
   limit: do 120 znaków
   EN: Clash Power -2, Defense Level -3
   PL: Moc Starcia -2, Poziom Obrony -3
405. [Status [ChickenFightlust] — nazwa] 혈투본능
   źródło: Bufs.json :: dataList[id=ChickenFightlust].name
   kontekst: identyfikator statusu w tekstach: `[ChickenFightlust]`
   limit: do 40 znaków
   EN: Battleblood Instinct
   PL: Instynkt Krwawej Walki
406. [Status [ChickenFightlust] — opis] - 최댓값: 20\n- 수치 1당 가하는 피해량 +0.75%\n- 수치 10당 턴 종료 시 다음 턴에 신속 1 얻음
   źródło: Bufs.json :: dataList[id=ChickenFightlust].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- For every Stack, deal +0.75% damage\n- For every 10 Stack, gain 1 Haste next turn
   PL: - Maks.: 20\n- Zadaje +0,75% obrażeń za każdą wartość\n- Za każde 10 wartości zyskuje 1 Pośpiechu w następnej turze
407. [Status [ProtectStanceRyoshu] — nazwa] 호위태세
   źródło: Bufs.json :: dataList[id=ProtectStanceRyoshu].name
   kontekst: identyfikator statusu w tekstach: `[ProtectStanceRyoshu]`
   limit: do 40 znaków
   EN: Protector's Stance
   PL: Postawa Strażnicza
408. [Status [ProtectStanceRyoshu] — opis] - 최댓값 : 2\n- 받는 피해 (수치 x 10)% 감소\n- 턴 시작 시, 자신의 호흡만큼 보호막 얻음 (최대 20)\n- 턴 종료 시, 호흡 위력 3, 호흡 횟수 1 얻고 다음 턴에 자신의 가장 왼쪽 슬롯 도발치 5 증가\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=ProtectStanceRyoshu].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take (Stack x 10)% less damage\n- Turn Start: Gain Shield by Poise on self (max 20)\n- Turn End: Gain 3 Poise Potency and +1 Poise Count; this unit's leftmost Skill Slot gains +5 Aggro next turn\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Otrzymywane obrażenia maleją o (wartość x 10)%\n- Na początku tury zyskuje Tarczę równą własnemu Oddechowi (maks. 20)\n- Na koniec tury zyskuje 3 Mocy Oddechu i 1 Licznik Oddechu, a skrajnie lewy slot zyskuje +5 Wartości Prowokacji w następnej turze\n- Na koniec tury maleje o 1
409. [Status [ProtectStanceRyoshu] — podsumowanie] 받는 피해 감소
   źródło: Bufs.json :: dataList[id=ProtectStanceRyoshu].summary
   limit: do 120 znaków
   EN: Take less damage
   PL: Otrzymuje mniej obrażeń
410. [Status [TheUdjatOutis] — nazwa] 우제트의 눈 [선봉]
   źródło: Bufs.json :: dataList[id=TheUdjatOutis].name
   kontekst: identyfikator statusu w tekstach: `[TheUdjatOutis]`
   limit: do 40 znaków
   EN: The Udjat [Vanguard]
   PL: Oko Udżat [Awangarda]
411. [Status [TheUdjatOutis] — opis] - 최댓값: 2\n- 속도 최솟값, 최댓값 +3\n- 전투 시작 시 보호 1 얻음\n- 전투 중 아래의 효과 적용 (스킬당 1회, 턴당 3회)\n· 자신이 메인 타겟인 일방 공격 스킬의 첫번째 코인이 앞면으로 나올 확률 절반 감소\n· 합 시작 시 첫 합에서 대상의 모든 코인이 앞면으로 나올 확률 절반 감소\n· 위 효과에서 대상 코인이 마이너스 코인인 경우, 뒷면이 나올 확률로 적용됨\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=TheUdjatOutis].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Min & Max Speed +3\n- Combat Start: gain 1 Protection\n- Gain the following effects during the Combat Phase (once per Skill, 3 times per turn)\n· When this unit is the main target of an Unopposed Attack Skill, halve the chance for the Skill's first Coin to flip Heads\n· Clash Start: In the first Clash, halve the target's chance to flip Heads for all of its Coins\n· For both of the above effects, if the target uses Minus Coins, halve their chance to flip Tails instead\n- Turn End: Reduce 1 Stack
   PL: - Maks.: 2\n- Minimalna i maksymalna Szybkość +3\n- Na początku walki zyskuje 1 Ochrony\n- Podczas fazy walki (raz na Umiejętność, 3 razy na turę):\n· Będąc głównym celem ataku niekwestionowanego, zmniejsza o połowę szansę awersu pierwszej monety Umiejętności\n· Na początku Starcia zmniejsza w pierwszym Starciu o połowę szansę awersu wszystkich monet celu\n· Jeśli cel używa monet minus, zamiast tego zmniejsza o połowę szansę rewersu\n- Na koniec tury maleje o 1
412. [Status [BlueSand] — nazwa] 푸른 모래
   źródło: Bufs.json :: dataList[id=BlueSand].name
   kontekst: identyfikator statusu w tekstach: `[BlueSand]`
   limit: do 40 znaków
   EN: Blue Sand
   PL: Błękitny Piasek
413. [Status [BlueSand] — opis] - 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 있는 대상이면, 패닉 유형이 '푸른 모래'로 변경됨\n- 정신력이 없는 대상이면, 속도 최솟값, 최댓값 -1\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 푸른 모래 패닉 효과\n- 사기 저하 : 자신의 합 위력 -1, 속도 최솟값, 최댓값 -1\n- 패닉 : 자신의 합 위력 -2, 속도 최솟값, 최댓값 -1
   źródło: Bufs.json :: dataList[id=BlueSand].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- SP Units: change their Panic Type to "Blue Sand"\n- Non-SP Units: Min & Max Speed -1\n- Turn End: Reduce 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Blue Sand Panic Effects\n- Low Morale: Clash Power -1, Min & Max Speed -1\n- Panic: Clash Power -2, Min & Max Speed -1
   PL: - Po przegranej w Starciu zyskuje 1 Licznik Zatonięcia (do 3 razy na turę)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Błękitny Piasek”\n- Jednostki bez Poczytalności: minimalna i maksymalna Szybkość -1\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Błękitnego Piasku”\n- Spadek Moralu: Moc Starcia -1, minimalna i maksymalna Szybkość -1\n- Panika: Moc Starcia -2, minimalna i maksymalna Szybkość -1
414. [Status [BlueSand_Main] — nazwa] 푸른 모래
   źródło: Bufs.json :: dataList[id=BlueSand_Main].name
   kontekst: identyfikator statusu w tekstach: `[BlueSand_Main]`
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
415. [Status [BlueSand_Main] — opis] - 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 있는 대상이면, 패닉 유형이 '푸른 모래'로 변경됨\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BlueSand_Main].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- SP Units: change their Panic Type to "Blue Sand"\n- Turn End: Reduce 1 Stack
   PL: - Po przegranej w Starciu Licznik Zatonięcia rośnie o 1 (3 razy na turę)\n- Jednostki z Poczytalnością zmieniają typ Paniki na „Błękitny Piasek”\n- Na koniec tury maleje o 1
416. [Status [BlueSand_Main] — podsumowanie] 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 있는 대상이면, 패닉 유형이 '푸른 모래'로 변경됨
   źródło: Bufs.json :: dataList[id=BlueSand_Main].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- SP Units: change their Panic Type to "Blue Sand"
   PL: Po przegranej w Starciu Licznik Zatonięcia rośnie o 1 (3 na turę)\nJednostki z Poczytalnością zmieniają typ Paniki na „Błękitny Piasek”
417. [Status [BlueSand_Sub] — nazwa] 푸른 모래
   źródło: Bufs.json :: dataList[id=BlueSand_Sub].name
   kontekst: identyfikator statusu w tekstach: `[BlueSand_Sub]`
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
418. [Status [BlueSand_Sub] — opis] - 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 없는 대상이면, 속도 최솟값, 최댓값 -1\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BlueSand_Sub].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- Non-SP Units: Min & Max Speed -1\n- Turn End: Reduce 1 Stack
   PL: Po przegranej w Starciu Licznik Zatonięcia rośnie o 1 (3 na turę)\n- Jednostki bez Poczytalności: min. i maks. Szybkość -1\n- Na koniec tury maleje o 1
419. [Status [BlueSand_Sub] — podsumowanie] 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 없는 대상이면, 속도 최솟값, 최댓값 -1
   źródło: Bufs.json :: dataList[id=BlueSand_Sub].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- Non-SP Units: Min & Max Speed -1
   PL: Po przegranej w Starciu Licznik Zatonięcia rośnie o 1 (3 na turę)\nJednostki bez Poczytalności: min. i maks. Szybkość -1
420. [Status [BlueSand_LowMorale] — nazwa] 푸른 모래
   źródło: Bufs.json :: dataList[id=BlueSand_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[BlueSand_LowMorale]`
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Status [BlueSand_LowMorale] — opis] - 사기 저하\n- 자신의 합 위력 -1\n- 속도 최솟값, 최댓값 -1
   źródło: Bufs.json :: dataList[id=BlueSand_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1\n- Min & Max Speed -1
   PL: - Niskie Morale\n- Moc Starcia -1\n- Minimalna i maksymalna Szybkość -1
422. [Status [BlueSand_LowMorale] — podsumowanie] 자신의 합 위력 -1
   źródło: Bufs.json :: dataList[id=BlueSand_LowMorale].summary
   limit: do 120 znaków
   EN: Clash Power -1 on self
   PL: Moc Starcia -1
423. [Status [BlueSand_Panic] — nazwa] 푸른 모래
   źródło: Bufs.json :: dataList[id=BlueSand_Panic].name
   kontekst: identyfikator statusu w tekstach: `[BlueSand_Panic]`
   (powtórzenie elementu 412 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
424. [Status [BlueSand_Panic] — opis] - 패닉\n- 자신의 합 위력 -2\n속도 최솟값, 최댓값 -1
   źródło: Bufs.json :: dataList[id=BlueSand_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2\n- Min & Max Speed -1
   PL: - Panika\n- Moc Starcia -2\nMinimalna i maksymalna Szybkość -1
425. [Status [BlueSand_Panic] — podsumowanie] 자신의 합 위력 -2
   źródło: Bufs.json :: dataList[id=BlueSand_Panic].summary
   limit: do 120 znaków
   EN: Clash Power -2 on self
   PL: Moc Starcia -2
426. [Status [SheutFracture] — nazwa] 셰우트의 균열
   źródło: Bufs.json :: dataList[id=SheutFracture].name
   kontekst: identyfikator statusu w tekstach: `[SheutFracture]`
   limit: do 40 znaków
   EN: Sheut Fracture
   PL: Pęknięcie Sheut
427. [Status [SheutFracture] — opis] - 특수 침잠\n- 최댓값: 10\n- 수치 1당, 나태 속성, 우울 속성 스킬로 피격 시 받는 피해량 +1%\n- 수치가 최댓값에 도달하면 우울 취약 1 얻음(턴당 1회). 자신의 침잠 위력만큼 우울 피해를 받은 후 소멸 (침잠 횟수 1 감소)\n- 효과를 가진 채 사망하면 정신력이 가장 높은 아군 1명에게 수치의 절반만큼 부여 (소수점 버림)\n- 턴 시작 시 출전 인원 중 LCA 소속 인격이 없으면 소멸
   źródło: Bufs.json :: dataList[id=SheutFracture].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Sinking\n- Max Stack: 10\n- For every Stack, take +1% more damage from Sloth and Gloom Skills\n- At max Stack, gain 1 Gloom Fragility (once per turn), take Gloom damage equal to Sinking Potency on self (lose 1 Sinking Count), then expires\n- If the unit that has this effect dies, transfer half of its Stack to its ally that has the highest SP (rounded down)\n- Turn Start: If there are no LCA Identities on the field, expires
   PL: - Szczególne Zatonięcie\n- Maks.: 10\n- Za każdą wartość: +1% otrzymywanych obrażeń od Umiejętności Lenistwa i Posępności\n- Przy maksymalnej wartości zyskuje 1 Wrażliwości na Posępność (raz na turę), otrzymuje obrażenia Posępnością równe własnej Mocy Zatonięcia (traci 1 Licznik Zatonięcia), po czym znika\n- Po śmierci nosiciela przenosi połowę stosów (zaokrąglona w dół) na sojusznika z najwyższą Poczytalnością\n- Na początku tury znika, jeśli w składzie nie ma osobowości LCA
428. [Status [LCA_Bullet] — nazwa] LCA 균열탄
   źródło: Bufs.json :: dataList[id=LCA_Bullet].name
   kontekst: identyfikator statusu w tekstach: `[LCA_Bullet]`
   limit: do 40 znaków
   EN: LCA Fracture Round
   PL: Pocisk Rozłamowy LCA
429. [Status [LCA_Bullet] — opis] - 특수 탄환\n- 최댓값 : 16\n- 특정 스킬 사용 시 소모\n- 탄환이 없을 때 공격이 취소됨
   źródło: Bufs.json :: dataList[id=LCA_Bullet].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Capacity: 16\n- Spent by certain Skills\n- Some attacks cancel if lacking Ammo
   PL: - Szczególna amunicja\n- Maks.: 16\n- Zużywana przy użyciu określonych Umiejętności\n- Przy braku amunicji atak zostaje anulowany
430. [Status [NiddleEGO] — nazwa] 바늘
   źródło: Bufs.json :: dataList[id=NiddleEGO].name
   kontekst: identyfikator statusu w tekstach: `[NiddleEGO]`
   limit: do 40 znaków
   EN: Needle
   PL: Igła
431. [Status [NiddleEGO] — opis] - 특수 출혈\n- 질투 피해를 받으면, 출혈 횟수 1 증가하고 이 효과 수치 1 감소\n- 턴 종료 시 출혈 1 얻고 수치 1 감소
   źródło: Bufs.json :: dataList[id=NiddleEGO].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- When taking Envy damage, gain +1 Bleed Count and reduce this effect's Stack by 1\n- Turn End: Gain 1 Bleed and reduce this effect's Stack by 1
   PL: - Szczególne Krwawienie\n- Przy otrzymaniu obrażeń Zazdrością zyskuje 1 Licznik Krwawienia, a wartość maleje o 1\n- Na koniec tury zyskuje 1 Krwawienia, a wartość maleje o 1
432. [Status [NiddleEGO] — podsumowanie] 출혈 횟수 증가
   źródło: Bufs.json :: dataList[id=NiddleEGO].summary
   limit: do 120 znaków
   EN: Gain Bleed Count
   PL: Zyskuje Licznik Krwawienia
433. [Status [IDMicroChip] — nazwa] 주민등록 마이크로칩
   źródło: Bufs.json :: dataList[id=IDMicroChip].name
   kontekst: identyfikator statusu w tekstach: `[IDMicroChip]`
   limit: do 40 znaków
   EN: Resident Reg. Microchip
   PL: Mikrochip Rejestracji Mieszkańców
434. [Status [IDMicroChip] — opis] - 최댓값: 2\n- 분노 속성, 질투 속성으로 피격 시 받는 피해량 +10%\n- 합 패배 시 화상 1 얻음 (턴당 최대 3회)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=IDMicroChip].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take +10% damage from Wrath and Envy Skills\n- On Clash Lose, gain 1 Burn (3 times per turn)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Otrzymuje +10% obrażeń od Umiejętności Gniewu i Zazdrości\n- Po przegranej w Starciu zyskuje 1 Podpalenia (do 3 razy na turę)\n- Na koniec tury maleje o 1
435. [Status [ExtractCoin] — nazwa] 적출 코인
   źródło: Bufs.json :: dataList[id=ExtractCoin].name
   kontekst: identyfikator statusu w tekstach: `[ExtractCoin]`
   limit: do 40 znaków
   EN: Excision Coin
   PL: Moneta Wycięcia
436. [Status [ExtractCoin] — opis] - 합 진행 시 파괴 불가 코인도 파괴 가능.\n- 합 패배 시 코인이 파괴되지 않음.\n- 공격 스킬에 해당 코인이 있으면, 피격 후 해당 코인으로 공격함.\n- 합 패배 시 파괴되지 않은 코인은 코인 위력이 1이 됨.
   źródło: Bufs.json :: dataList[id=ExtractCoin].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin can destroy Unbreakable Coins in a Clash.\n- This coin does not break upon Clash Lose.\n- If an Attack Skill has this Coin, attack with this Coin after getting hit.\n- Upon Clash Lose, fix the Coin Power of the unbroken Coin to 1
   PL: - W Starciu może zniszczyć nawet Monetę Niezniszczalną\n- Moneta nie ulega zniszczeniu po przegranej w Starciu\n- Jeśli Umiejętność ataku zawiera tę monetę, atakuje nią po otrzymaniu trafienia\n- Po przegranej w Starciu moc niezniszczonej monety zostaje ustalona na 1
437. [Status [ReinforcedTattooIshmael] — nazwa] 중지식 강화 문신
   źródło: Bufs.json :: dataList[id=ReinforcedTattooIshmael].name
   kontekst: identyfikator statusu w tekstach: `[ReinforcedTattooIshmael]`
   limit: do 60 znaków
   EN: The Middle Styled Augmentation Tattoos
   PL: Wzmocnione Tatuaże Stylu Środkowego
438. [Status [ReinforcedTattooIshmael] — opis] - 최댓값: 10\n- 수치 5당 기본 스킬의 최종 위력 +1 (최대 2)\n- 수치 1당 질투 속성 스킬이나 타격 속성 스킬 피해량 +5% (최대 50%)
   źródło: Bufs.json :: dataList[id=ReinforcedTattooIshmael].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Final Power +1 for Base Skills for every 5 Stack (max 2)\n- Envy Skills and Blunt Skills deal +5% damage for every Stack (max 50%)
   PL: - Maks.: 10\n- Moc Końcowa Umiejętności bazowych +1 za każde 5 stosów (maks. 2)\n- Umiejętności Zazdrości i Uderzenia zadają +5% obrażeń za każdą wartość (maks. 50%)
439. [Status [ResentmentIshmael] — nazwa] 중지 - 원한
   źródło: Bufs.json :: dataList[id=ResentmentIshmael].name
   kontekst: identyfikator statusu w tekstach: `[ResentmentIshmael]`
   limit: do 40 znaków
   EN: The Middle - Grudge
   PL: Środkowy - Uraza
440. [Status [ResentmentIshmael] — opis] - 최댓값: 15\n- 앙갚음 대상에게 주는 피해량 +20%
   źródło: Bufs.json :: dataList[id=ResentmentIshmael].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- If target has Vengeance Mark, deal +20% damage
   PL: - Maks.: 15\n- Zadaje +20% obrażeń celom z Celem Odwetu
441. [Status [HeatingWireIshmael] — nazwa] 열선
   źródło: Bufs.json :: dataList[id=HeatingWireIshmael].name
   kontekst: identyfikator statusu w tekstach: `[HeatingWireIshmael]`
   limit: do 40 znaków
   EN: Thermal Blades
   PL: Ostrza Termiczne
442. [Status [HeatingWireIshmael] — opis] - 최댓값: 2\n- 기본 스킬을 적중한 대상이 화상을 보유 중이면, 자신의 정신력 3 회복 (턴당 2회)\n- 특정 스킬 코인으로 출혈 부여 시 화상 부여\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=HeatingWireIshmael].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- If target hit by Base Skills has Burn, heal 3 SP (2 times per turn)\n- Inflict Burn when inflicting Bleed with certain Skill Coins\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Jeśli cel trafiony Umiejętnością bazową ma Podpalenie, regeneruje 3 Poczytalności (do 2 razy na turę)\n- Nadając Krwawienie monetami określonych Umiejętności, nadaje Podpalenie\n- Na koniec tury maleje o 1
443. [Status [LanternGregBigBird] — nazwa] 램프
   źródło: Bufs.json :: dataList[id=LanternGregBigBird].name
   kontekst: identyfikator statusu w tekstach: `[LanternGregBigBird]`
   limit: do 40 znaków
   EN: Lamp
   PL: Lampa
444. [Status [LanternGregBigBird] — opis] - 최댓값: 8\n- 턴 종료 시 다음 턴에 수치 2당 속박 1 얻음 (최대 4)\n- 턴 종료 시 수치가 최대고 적이 있으면, 수치를 전부 소모하고 다음 턴에 아래 효과 발동\n• 가장 왼쪽 슬롯이 도발치를 10만큼 얻음\n• 현재 체력이 가장 높은 적(본체)에게 현혹 3 부여
   źródło: Bufs.json :: dataList[id=LanternGregBigBird].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 8\n- Turn End: Gain 1 Bind next turn for every 2 Stack (max 4)\n- Turn End: At max Stack, if there are enemies on the field, consume all Stack to activate the following effects next turn:\n• Gain +10 Aggro to the leftmost Slot\n• Inflict 3 Dazzle to the enemy(Core) with the most current HP
   PL: - Maks.: 8\n- Na koniec tury zyskuje w następnej turze 1 Spętania za każde 2 wartości (maks. 4)\n- Na koniec tury, przy maksymalnej wartości i obecności wrogów, zużywa wszystkie stosy, by w następnej turze:\n• Skrajnie lewy slot zyskuje +10 Wartości Prowokacji\n• Wrogowi (Korpusowi) z najwyższym HP nadaje 3 Omamów
445. [Status [LanternGregBigBird] — podsumowanie] 다음 턴에 속박 얻음
   źródło: Bufs.json :: dataList[id=LanternGregBigBird].summary
   (powtórzenie elementu 380 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
446. [Status [ObedienceGregBigBird] — nazwa] 숲의 파수꾼
   źródło: Bufs.json :: dataList[id=ObedienceGregBigBird].name
   kontekst: identyfikator statusu w tekstach: `[ObedienceGregBigBird]`
   limit: do 40 znaków
   EN: Guardians of the Forest
   PL: Strażnik Lasu
447. [Status [ObedienceGregBigBird] — opis] 공격 시작 전 아래 효과 발동\n- 더하기 코인을 사용하는 스킬이면, 정신력 4 회복 (이 효과로 정신력 회복 시 자신의 정신력이 최대면 다음 턴에 공격 레벨 증가 2 얻음)\n- 빼기 코인을 사용하는 스킬이면, 정신력 8 감소 (이 효과로 정신력이 -40 미만이 되지 않음)\n- 이 효과 소멸
   źródło: Bufs.json :: dataList[id=ObedienceGregBigBird].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Before Attack, activate the following effects:\n- Plus Coin Skills heal 4 SP (if already at max SP, gain 2 Offense Level Up next turn)\n- Minus Coin Skills lose 8 SP (this effect cannot reduce the unit's SP below -40)\n- Lose this effect
   PL: Przed atakiem aktywuje poniższe efekty:\n- Umiejętności z monetą plus regenerują 4 Poczytalności (przy pełnej Poczytalności zyskuje w następnej turze 2 Wzrosty Poziomu Ataku)\n- Umiejętności z monetą minus tracą 8 Poczytalności (nie poniżej -40)\n- Efekt znika
448. [Status [DelusionGregBigBird] — nazwa] 현혹
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird].name
   kontekst: identyfikator statusu w tekstach: `[DelusionGregBigBird]`
   limit: do 40 znaków
   EN: Dazzle
   PL: Omam
449. [Status [DelusionGregBigBird] — opis] - 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n- 정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n- 정신력이 없는 대상이면, 방어 레벨 -2\n- 턴 종료시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 현혹 패닉 효과\n- 사기 저하 : 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 2 얻음\n- 패닉 : 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 4 얻음
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\n- SP Units: Change their Panic Type to "Dazzle"\n- Non-SP Units: Defense Level -2\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Dazzle Panic-type Effects\n- Low Morale: Turn End: Gain 1 Bind and 2 Offense Level Down next turn\n- Panic: Turn End: Gain 1 Bind and 4 Offense Level Down next turn
   PL: - Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Omam”\n- Jednostki bez Poczytalności: Poziom Obrony -2\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Omamu”\n- Spadek Moralu: na koniec tury zyskuje w następnej turze 1 Spętania i 2 Spadki Poziomu Ataku\n- Panika: na koniec tury zyskuje w następnej turze 1 Spętania i 4 Spadki Poziomu Ataku
450. [Status [DelusionGregBigBird] — podsumowanie] 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n정신력이 없는 대상이면, 방어 레벨 -2
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\nSP Units: Change their Panic Type to "Dazzle"\nNon-SP Units: Defense Level -2
   PL: Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\nZ Poczytalnością: zmienia Panikę na „Omam”\nBez Poczytalności: Poziom Obrony -2
451. [Status [DelusionGregBigBird_Main] — nazwa] 현혹
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Main].name
   kontekst: identyfikator statusu w tekstach: `[DelusionGregBigBird_Main]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
452. [Status [DelusionGregBigBird_Main] — opis] - 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n- 정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Main].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\n- SP Units: Change their Panic Type to "Dazzle"\n- Turn End: Lose 1 Stack
   PL: - Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Omam”\n- Na koniec tury maleje o 1
453. [Status [DelusionGregBigBird_Main] — podsumowanie] 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n패닉 유형이 현혹으로 변경됨
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Main].summary
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\nChange Panic Type to "Dazzle"
   PL: Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\nZmienia rodzaj Paniki na „Omam”
454. [Status [DelusionGregBigBird_Sub] — nazwa] 현혹
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Sub].name
   kontekst: identyfikator statusu w tekstach: `[DelusionGregBigBird_Sub]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Status [DelusionGregBigBird_Sub] — opis] - 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n- 정신력이 없는 대상이면, 방어 레벨 -2\n- 턴 종료시 1 감소
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Sub].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\n- Non-SP Units: Defense Level -2\n- Turn End: Lose 1 Stack
   PL: - Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\n- Jednostki bez Poczytalności: Poziom Obrony -2\n- Na koniec tury maleje o 1
456. [Status [DelusionGregBigBird_Sub] — podsumowanie] 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n방어 레벨 -2
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Sub].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\nDefense Level -2
   PL: Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\nPoziom Obrony -2
457. [Status [DelusionGregBigBird_LowMorale] — nazwa] 현혹
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_LowMorale].name
   kontekst: identyfikator statusu w tekstach: `[DelusionGregBigBird_LowMorale]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
458. [Status [DelusionGregBigBird_LowMorale] — opis] - 사기 저하\n- 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 2 얻음
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn End: Gain 1 Bind and 2 Offense Level Down next turn
   PL: - Spadek Moralu\n- Na koniec tury zyskuje w następnej turze 1 Spętania i 2 Spadki Poziomu Ataku
459. [Status [DelusionGregBigBird_LowMorale] — podsumowanie] 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 2 얻음
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_LowMorale].summary
   limit: do 120 znaków
   EN: Turn End: Gain 1 Bind and 2 Offense Level Down next turn
   PL: Na koniec tury zyskuje w następnej turze 1 Spętania i 2 Spadki Poziomu Ataku
460. [Status [DelusionGregBigBird_Panic] — nazwa] 현혹
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Panic].name
   kontekst: identyfikator statusu w tekstach: `[DelusionGregBigBird_Panic]`
   (powtórzenie elementu 448 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
461. [Status [DelusionGregBigBird_Panic] — opis] - 패닉\n- 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 4 얻음
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn End: Gain 1 Bind and 4 Offense Level Down next turn
   PL: - Panika\n- Na koniec tury zyskuje w następnej turze 1 Spętania i 4 Spadki Poziomu Ataku
462. [Status [DelusionGregBigBird_Panic] — podsumowanie] 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 4 얻음
   źródło: Bufs.json :: dataList[id=DelusionGregBigBird_Panic].summary
   limit: do 120 znaków
   EN: Turn End: Gain 1 Bind and 4 Offense Level Down next turn
   PL: Na koniec tury zyskuje w następnej turze 1 Spętania i 4 Spadki Poziomu Ataku
463. [Status [LittleFingerID] — nazwa] 월하청도
   źródło: Bufs.json :: dataList[id=LittleFingerID].name
   kontekst: identyfikator statusu w tekstach: `[LittleFingerID]`
   limit: do 40 znaków
   EN: Moonlit Azure Blade
   PL: Błękitne Ostrze w Blasku Księżyca
464. [Status [LittleFingerID] — opis] - 최댓값 : 20\n- 턴 시작시 수치 1당 보호막 2 얻음\n- 수치 1당 크리티컬 피해량 +1%
   źródło: Bufs.json :: dataList[id=LittleFingerID].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Turn Start: Gain 2 Shield for every Stack\n- Deal +1% damage on Critical Hit for every Stack
   PL: - Maks.: 20\n- Na początku tury zyskuje 2 Tarczy za każdą wartość\n- Zadaje +1% obrażeń krytycznych za każdą wartość
465. [Status [IndexPrescriptYi_0] — nazwa] 지령[단말기] I
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_0].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptYi_0]`
   limit: do 40 znaków
   EN: Prescript: [Device] I
   PL: Nakaz [Urządzenie] I
466. [Status [IndexPrescriptYi_0] — opis] 지령 표식이 새겨진 스킬을 사용하거나 적중한다.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a Skill marked with Mark of the Prescript or hit a target with a marked Skill.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Używa Umiejętności oznaczonej Znakiem Nakazu lub trafia nią cel.\n\n- Na początku tury zyskuje efekt, gdy nie ma Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
467. [Status [IndexPrescriptYi_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_0].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy przekazywane są na rozmaite sposoby. Forma, w jakiej dotrą do adresata, zostaje wybrana jednokierunkowo, niczym wyrocznia — bez jego wpływu.
468. [Status [IndexPrescriptYi_1] — nazwa] 지령[단말기] II
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_1].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptYi_1]`
   limit: do 40 znaków
   EN: Prescript: [Device] II
   PL: Nakaz [Urządzenie] II
469. [Status [IndexPrescriptYi_1] — opis] 지령 표식이 새겨진 스킬이 적중한다.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with a Skill marked with Mark of the Prescript.\n\n- Turn Start: Gain this effect if this unit has Unlock - I\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Trafia cel Umiejętnością oznaczoną Znakiem Nakazu.\n\n- Na początku tury zyskuje efekt przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
470. [Status [IndexPrescriptYi_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_1].flavor
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
471. [Status [IndexPrescriptYi_2] — nazwa] 지령[단말기] III
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_2].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptYi_2]`
   limit: do 40 znaków
   EN: Prescript: [Device] III
   PL: Nakaz [Urządzenie] III
472. [Status [IndexPrescriptYi_2] — opis] 대행 [헤르메스]를 얻는다. 대행 [헤르메스]가 9가 될 때까지 이 지령을 반복한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Procuration [Hermes]. Repeat this Prescript until Procuration [Hermes] reaches 9 Stacks.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Zyskuje Procuration [Hermes]. Powtarza ten Nakaz, aż Procuration [Hermes] osiągnie 9 stosów.\n\n- Na początku tury zyskuje efekt przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
473. [Status [IndexPrescriptYi_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_2].flavor
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Status [IndexPrescriptYi_3] — nazwa] 지령[단말기] IV
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_3].name
   kontekst: identyfikator statusu w tekstach: `[IndexPrescriptYi_3]`
   limit: do 40 znaków
   EN: Prescript: [Device] IV
   PL: Nakaz [Urządzenie] IV
475. [Status [IndexPrescriptYi_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Zabija wszystkich wrogów przed nadejściem kolejnego Nakazu.\n\n- Na początku tury zyskuje efekt przy Odblokowaniu - III
476. [Status [IndexPrescriptYi_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: Bufs.json :: dataList[id=IndexPrescriptYi_3].flavor
   (powtórzenie elementu 467 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
477. [Status [StackYisangSpecialSkill] — nazwa] 대행 [헤르메스]
   źródło: Bufs.json :: dataList[id=StackYisangSpecialSkill].name
   kontekst: identyfikator statusu w tekstach: `[StackYisangSpecialSkill]`
   limit: do 40 znaków
   EN: Procuration [Hermes]
   PL: Procuration [Hermes]
478. [Status [StackYisangSpecialSkill] — opis] - 턴 시작 시 수치가 9면 강력한 스킬을 사용 가능\n- 한 턴에 (해금 단계+2)만큼 획득 가능\n- 최댓값 : 9\n· 해금 - II 미만이면 최대 8까지만 획득 가능
   źródło: Bufs.json :: dataList[id=StackYisangSpecialSkill].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: At 9 Stack, a powerful Skill becomes available\n- Can be gained up to (Unlock stage + 2) Stack per turn\n- Max Stack: 9\n· At below Unlock - II, this effect's maximum Stack is limited to 8
   PL: - Na początku tury, przy 9 stosach, dostępna staje się potężna Umiejętność\n- Można zyskać do (etap Odblokowania + 2) stosów na turę\n- Maks.: 9\n· Poniżej Odblokowania - II maksimum to 8
479. [Status [Shin_IndexFingerYisang] — nazwa] 신(心) - 운명
   źródło: Bufs.json :: dataList[id=Shin_IndexFingerYisang].name
   kontekst: identyfikator statusu w tekstach: `[Shin_IndexFingerYisang]`
   limit: do 40 znaków
   EN: Shin (心) - Fate
   PL: Serce (心) - Przeznaczenie
480. [Status [Shin_IndexFingerYisang] — opis] - 속도 최솟값, 최댓값 1 증가\n- 기본 스킬로 획득하는 호흡 위력과 횟수 +1\n- 자신의 정신력이 대상보다 높으면, 정신력 차이 3당 피해량 +1%\n(최대 15%, 정신력이 없으면 정신력 0으로 계산)
   źródło: Bufs.json :: dataList[id=Shin_IndexFingerYisang].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Gain +1 more Poise Potency and Count from Base Skills\n- If this unit's SP is higher than the target's, deal +1% damage for every 3 SP difference (max 15%; Non-SP Units are considered to be at 0 SP)
   PL: - Minimalna i maksymalna Szybkość +1\n- Umiejętności bazowe zyskują o 1 więcej Mocy i Licznika Oddechu\n- Jeśli Poczytalność przewyższa cel, zadaje +1% obrażeń za każde 3 różnicy (maks. 15%; jednostki bez Poczytalności liczone jako 0)
481. [Status [BurningWoundYisangMask] — nazwa] 상처를 가린 가면
   źródło: Bufs.json :: dataList[id=BurningWoundYisangMask].name
   kontekst: identyfikator statusu w tekstach: `[BurningWoundYisangMask]`
   limit: do 40 znaków
   EN: Wound-casing Mask
   PL: Maska Kryjąca Ranę
482. [Status [BurningWoundYisangMask] — opis] - 공격 레벨 +2, 방어 레벨 -2\n- 일방 공격으로 받는 피해량 -10%
   źródło: Bufs.json :: dataList[id=BurningWoundYisangMask].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2, Defense Level -2\n- Take -10% damage from Unopposed Attacks
   PL: - Poziom Ataku +2, Poziom Obrony -2\n- Otrzymuje -10% obrażeń od ataków niekwestionowanych
483. [Status [BurningWoundYisang] — nazwa] 이글거리는 상처
   źródło: Bufs.json :: dataList[id=BurningWoundYisang].name
   kontekst: identyfikator statusu w tekstach: `[BurningWoundYisang]`
   limit: do 40 znaków
   EN: Sizzling Wound
   PL: Kipiąca Rana
484. [Status [BurningWoundYisang] — opis] - 공격 레벨 +3, 방어 레벨 -3\n- 일방 공격으로 받는 피해량 -25%\n- 턴 시작 시 화상 1, 출혈 1 얻음\n- 기본 공격 스킬의 파괴 불가 코인 피해량 +15%
   źródło: Bufs.json :: dataList[id=BurningWoundYisang].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3, Defense Level -3\n- Take -25% damage from Unopposed Attacks\n- Turn Start: Gain 1 Burn and 1 Bleed\n- Deal +15% damage with Base Attack Skill's Unbreakable Coins
   PL: - Poziom Ataku +3, Poziom Obrony -3\n- Otrzymuje -25% obrażeń od ataków niekwestionowanych\n- Na początku tury zyskuje 1 Podpalenia i 1 Krwawienia\n- Niezniszczalne Monety bazowych Umiejętności ataku zadają +15% obrażeń
485. [Status [BlackNightmareYisang] — nazwa] 지령 탐닉
   źródło: Bufs.json :: dataList[id=BlackNightmareYisang].name
   kontekst: identyfikator statusu w tekstach: `[BlackNightmareYisang]`
   limit: do 40 znaków
   EN: Indulgence in Prescripts
   PL: Indulgencja w Nakazach
486. [Status [BlackNightmareYisang] — opis] - 속도 최솟값, 최댓값 5 증가\n- ‘Furioso-Replica’에 다음 효과 적용\n· 적중 시 부여하는 침잠 위력 +1, 획득하는 호흡 위력 +1\n· 적중 시 침잠 횟수 3 증가 (대상별 1회)\n· 피해량 +30%\n- 턴 종료 시 소멸
   źródło: Bufs.json :: dataList[id=BlackNightmareYisang].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +5\n- Apply the following effects to 'Furioso-Replica':\n· On Hit, inflict +1 more Sinking Potency and gain +1 more Poise Potency\n· On Hit, inflict +3 Sinking Count (once per target)\n· Deal +30% damage\n- Expires at Turn End
   PL: - Minimalna i maksymalna Szybkość +5\n- Nadaje następujące efekty Umiejętności „Furioso-Replica”:\n· Przy trafieniu nadaje o 1 więcej Mocy Zatonięcia i zyskuje o 1 więcej Mocy Oddechu\n· Przy trafieniu nadaje 3 Liczniki Zatonięcia (raz na cel)\n· Zadaje +30% obrażeń\n- Znika na koniec tury
487. [Status [YisangWeapon01Hatchet] — nazwa] 손도끼로 갈비뼈를 찍어 내릴 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon01Hatchet].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon01Hatchet]`
   limit: do 70 znaków
   EN: When hacking through the ribs with a hatchet...
   PL: Kiedy ocierasz żebra toporkiem…
488. [Status [YisangWeapon01Hatchet] — opis] - 이 코인의 피해는 타격 속성 피해로 적용됨\n- 파괴되지 않고 적중 시 호흡 2 얻음
   źródło: Bufs.json :: dataList[id=YisangWeapon01Hatchet].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Blunt damage\n- On Hit without Cracking, gain 2 Poise
   PL: - Ta moneta zadaje obrażenia Uderzeniem\n- Przy trafieniu bez Roztrzaskania zyskuje 2 Oddechu
489. [Status [YisangWeapon02Stiletto] — nazwa] 스틸레토로 허파를 꿰뚫을 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon02Stiletto].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon02Stiletto]`
   limit: do 70 znaków
   EN: When penetrating the lungs with a stiletto...
   PL: Kiedy przebijasz płuca sztyletą…
490. [Status [YisangWeapon02Stiletto] — opis] - 이 코인의 피해는 관통 속성 피해로 적용됨\n- 파괴되지 않고 적중 시 침잠 2 부여
   źródło: Bufs.json :: dataList[id=YisangWeapon02Stiletto].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Pierce damage\n- On Hit without Cracking, inflict 2 Sinking
   PL: - Ta moneta zadaje obrażenia Przebiciem\n- Przy trafieniu bez Roztrzaskania nadaje 2 Zatonięcia
491. [Status [YisangWeapon03Greatsword] — nazwa] 바스타드 소드로 어깨와 머리를 짓이길 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon03Greatsword].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon03Greatsword]`
   limit: do 100 znaków
   EN: When cleaving through the shoulder and the skull with a bastard sword...
   PL: Kiedy miażdzysz bark i czaszkę mieczem bastardowym…
492. [Status [YisangWeapon03Greatsword] — opis] - 이 코인의 피해는 참격 속성 피해로 적용됨\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시 다음 턴에 공격 레벨 증가 1 얻음 (턴당 2회)
   źródło: Bufs.json :: dataList[id=YisangWeapon03Greatsword].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Slash damage\n- This Coin deals +5% damage\n- On Hit without Cracking, gain 1 Offense Level Up next turn (2 times per turn)
   PL: - Ta moneta zadaje obrażenia Cięciem\n- Ta moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania zyskuje w następnej turze 1 Wzrost Poziomu Ataku (do 2 razy na turę)
493. [Status [YisangWeapon04Rapier] — nazwa] 레이피어로 몸에 10개 이상의 구멍을 내야할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon04Rapier].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon04Rapier]`
   limit: do 80 znaków
   EN: When punching 10 or more holes in the torso with a rapier...
   PL: Kiedy musisz zrobić rapierem 10 lub więcej dziur w korpusie…
494. [Status [YisangWeapon04Rapier] — opis] - 이 코인의 피해는 관통 속성 피해로 적용됨\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시 다음 턴에 방어 레벨 감소 1 부여 (턴당 2회)
   źródło: Bufs.json :: dataList[id=YisangWeapon04Rapier].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Pierce damage\n- This Coin deals +5% damage\n- On Hit without Cracking, inflict 1 Defense Level Down next turn (2 times per turn)
   PL: - Ta moneta zadaje obrażenia Przebiciem\n- Ta moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania nadaje w następnej turze 1 Spadek Poziomu Obrony (do 2 razy na turę)
495. [Status [YisangWeapon05Sledgehammer] — nazwa] 망치로 뒤통수를 으깨야 할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon05Sledgehammer].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon05Sledgehammer]`
   limit: do 80 znaków
   EN: When caving in the back of the skull with a hammer...
   PL: Kiedy musisz roztrzaskać młotem potylicę…
496. [Status [YisangWeapon05Sledgehammer] — opis] - 이 코인의 피해는 타격 속성 피해로 적용됨\n- 해당 코인의 피해량 +5%\n- 파괴되지 않고 적중 시 3만큼 흐트러짐 손상
   źródło: Bufs.json :: dataList[id=YisangWeapon05Sledgehammer].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Blunt damage\n- This Coin deals +5% damage\n- On Hit without Cracking, raise target's Stagger Threshold by 3
   PL: - Ta moneta zadaje obrażenia Uderzeniem\n- Ta moneta zadaje +5% obrażeń\n- Przy trafieniu bez Roztrzaskania podnosi Próg Oszołomienia celu o 3
497. [Status [YisangWeapon06Ultragreatsword] — nazwa] 커다란 검으로 몸통을 갈라야 할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon06Ultragreatsword].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon06Ultragreatsword]`
   limit: do 60 znaków
   EN: When rending the body with a great sword...
   PL: Kiedy musisz rozciąć wielkim mieczem korpus…
498. [Status [YisangWeapon06Ultragreatsword] — opis] - 이 코인의 피해는 참격 속성 피해로 적용됨\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시 다음 턴까지 참격 취약 1 부여 (턴당 2회)
   źródło: Bufs.json :: dataList[id=YisangWeapon06Ultragreatsword].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Slash damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Slash Fragility until next turn (2 times per turn)
   PL: - Ta moneta zadaje obrażenia Cięciem\n- Ta moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nadaje do następnej tury 1 Wrażliwości na Cięcie (do 2 razy na turę)
499. [Status [YisangWeapon07Lance] — nazwa] 랜스로 20인치의 구멍을 내야 할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon07Lance].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon07Lance]`
   limit: do 60 znaków
   EN: When boring a 20-inch hole with a lance...
   PL: Kiedy musisz zrobić lancem 20-calową dziurę…
500. [Status [YisangWeapon07Lance] — opis] - 이 코인의 피해는 관통 속성 피해로 적용됨\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시 다음 턴까지 관통 취약 1 부여 (턴당 2회)
   źródło: Bufs.json :: dataList[id=YisangWeapon07Lance].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Pierce damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Pierce Fragility until next turn (2 times per turn)
   PL: - Ta moneta zadaje obrażenia Przebiciem\n- Ta moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nadaje do następnej tury 1 Wrażliwości na Przebicie (do 2 razy na turę)
501. [Status [YisangWeapon08Chain] — nazwa] 채찍으로 살점을 만 갈래 떼어내야 할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon08Chain].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon08Chain]`
   limit: do 80 znaków
   EN: When ripping the flesh to ten thousand strips with a whip...
   PL: Kiedy musisz strzępić ciało biczem na 10 000 kawałków…
502. [Status [YisangWeapon08Chain] — opis] - 이 코인의 피해는 타격 속성 피해로 적용됨\n- 해당 코인의 피해량 +15%\n- 파괴되지 않고 적중 시 다음 턴까지 타격 취약 1 부여 (턴당 2회)
   źródło: Bufs.json :: dataList[id=YisangWeapon08Chain].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Blunt damage\n- This Coin deals +15% damage\n- On Hit without Cracking, inflict 1 Blunt Fragility until next turn (2 times per turn)
   PL: - Ta moneta zadaje obrażenia Uderzeniem\n- Ta moneta zadaje +15% obrażeń\n- Przy trafieniu bez Roztrzaskania nadaje do następnej tury 1 Wrażliwości na Uderzenie (do 2 razy na turę)
503. [Status [YisangWeapon09Scythe] — nazwa] 낫으로… 누군가처럼 공간을 따라 베어내야 할 때는…
   źródło: Bufs.json :: dataList[id=YisangWeapon09Scythe].name
   kontekst: identyfikator statusu w tekstach: `[YisangWeapon09Scythe]`
   limit: do 110 znaków
   EN: When lacerating through space itself with a scythe, like a certain someone...
   PL: Kiedy musisz ciąć kosą… przestrzeń, jak ktoś…
504. [Status [YisangWeapon09Scythe] — opis] - 이 코인의 피해는 참격 속성 피해로 적용됨\n- 해당 코인의 피해량 +30%\n- 파괴되지 않고 적중 시 반드시 크리티컬로 적중
   źródło: Bufs.json :: dataList[id=YisangWeapon09Scythe].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin deals Slash damage\n- This Coin deals +30% damage\n- On Hit without Cracking, it hits a guaranteed Crit
   PL: - Ta moneta zadaje obrażenia Cięciem\n- Ta moneta zadaje +30% obrażeń\n- Przy trafieniu bez Roztrzaskania zawsze trafia krytycznie
505. [Status [SatisfyingEsteemNeeds] — nazwa] 인정 욕구 충족
   źródło: Bufs.json :: dataList[id=SatisfyingEsteemNeeds].name
   kontekst: identyfikator statusu w tekstach: `[SatisfyingEsteemNeeds]`
   limit: do 50 znaków
   EN: Desire for Acknowledgement Sated
   PL: Zaspokojony Głód Uznania
506. [Status [SatisfyingEsteemNeeds] — opis] - 지령 표식 스킬의 피해량 +7.5%\n- 지령 대상에게 가하는 피해량 +7.5%
   źródło: Bufs.json :: dataList[id=SatisfyingEsteemNeeds].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +7.5% damage with Skills marked with Mark of the Prescript\n- Deal +7.5% damage against The Prescript's Targets
   PL: - Umiejętności oznaczone Znakiem Nakazu zadają +7,5% obrażeń\n- Zadaje +7,5% obrażeń celom Nakazu
507. [Status [ThatIsRhythm] — nazwa] 리듬
   źródło: Bufs.json :: dataList[id=ThatIsRhythm].name
   kontekst: identyfikator statusu w tekstach: `[ThatIsRhythm]`
   limit: do 40 znaków
   EN: Rhythm
   PL: Rytm
508. [Status [ThatIsRhythm] — opis] - 최댓값: 5\n- 수치 1당, 가하는 피해량 +2% (최대 10%)\n- 수치 1당, 공격 레벨 +1 (최대 5)\n- 수치 1당, 방어 레벨 -1 (최대 -5)\n- 턴 종료 시 효과 소멸
   źródło: Bufs.json :: dataList[id=ThatIsRhythm].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Deal +2% damage for every Stack (max 10%)\n- Offense Level +1 for every Stack (max 5)\n- Defense Level -1 for every Stack (max -5)\n- Turn End: This effect expires
   PL: - Maks.: 5\n- Zadaje +2% obrażeń za każdą wartość (maks. 10%)\n- Poziom Ataku +1 za każdą wartość (maks. 5)\n- Poziom Obrony -1 za każdą wartość (maks. -5)\n- Na koniec tury efekt znika
509. [Status [MeursaultBeeSpore] — nazwa] 포자
   źródło: Bufs.json :: dataList[id=MeursaultBeeSpore].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBeeSpore]`
   limit: do 40 znaków
   EN: Spore
   PL: Zarodnik
510. [Status [MeursaultBeeSpore] — opis] - 최댓값: 15\n- 턴 종료 시 수치 5당 화상 횟수 1 증가\n- 다음 턴에 속박 1 얻음
   źródło: Bufs.json :: dataList[id=MeursaultBeeSpore].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- Turn End: Gain +1 Burn Count for every 5 Stack\n- Gain 1 Bind next turn
   PL: - Maks.: 15\n- Na koniec tury za każde 5 wartości zyskuje 1 Licznik Podpalenia\n- Zyskuje 1 Spętania w następnej turze
511. [Status [MeursaultWorkerBee] — nazwa] 충성 페로몬
   źródło: Bufs.json :: dataList[id=MeursaultWorkerBee].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultWorkerBee]`
   limit: do 40 znaków
   EN: Loyalty Pheromone
   PL: Feromon Lojalności
512. [Status [MeursaultWorkerBee] — opis] - 최댓값: 3\n- 수치에 따라 턴 종료시 다음 턴에 아래 효과를 얻음\n1 ~ : 보호 1\n2 ~ : 신속 1\n3: 합 위력 증가 1
   źródło: Bufs.json :: dataList[id=MeursaultWorkerBee].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain the following effects next turn based on Stack at Turn End:\n1+ Stack: 1 Protection\n2+ Stack: 1 Haste\n3 Stack: 1 Clash Power Up
   PL: - Maks.: 3\n- Na koniec tury zyskuje w następnej turze efekty zależnie od wartości:\n1 lub więcej: 1 Ochrony\n2 lub więcej: 1 Pośpiechu\n3: 1 Wzrost Mocy Starcia
513. [Status [MeursaultSporeBulletLong] — nazwa] 포자탄[기본]
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletLong].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultSporeBulletLong]`
   limit: do 40 znaków
   EN: Spore Round [Base]
   PL: Pocisk Zarodnikowy [Podstawowy]
514. [Status [MeursaultSporeBulletLong] — opis] - 특수 탄환\n- 최댓값: 10\n- 특정 스킬 사용 시 소모\n- 소모 시 수치가 부족한 경우, 공격이 취소됨\n- 소모하여 적중시 대상에게 포자 2 부여
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletLong].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Stack: 10\n- Spent when using certain Skills\n- Some attacks cancel if lacking Ammo\n- When spent, inflict 2 Spore on target On Hit
   PL: - Szczególna amunicja\n- Maks.: 10\n- Zużywana przy użyciu określonych Umiejętności\n- Przy niedoborze wartości atak zostaje anulowany\n- Zużywając przy trafieniu nadaje celowi 2 Zarodników
515. [Status [MeursaultSporeBulletShort] — nazwa] 포자탄[산탄]
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletShort].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultSporeBulletShort]`
   limit: do 40 znaków
   EN: Spore Round [Buckshot]
   PL: Pocisk Zarodnikowy [Śrut]
516. [Status [MeursaultSporeBulletShort] — opis] - 특수 탄환\n- 최댓값: 6\n- 특정 스킬 사용 시 소모\n- 소모 시 수치가 부족한 경우, 공격이 취소됨\n- 소모하여 적중시 대상에게 포자 3 부여
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletShort].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Stack: 6\n- Spent when using certain Skills\n- Some attacks cancel if lacking Ammo\n- When spent, inflict 3 Spore on target On Hit
   PL: - Szczególna amunicja\n- Maks.: 6\n- Zużywana przy użyciu określonych Umiejętności\n- Przy niedoborze wartości atak zostaje anulowany\n- Zużywając przy trafieniu nadaje celowi 3 Zarodniki
517. [Status [MeursaultSporeBulletReloading] — nazwa] 재장전[포자보충]
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletReloading].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultSporeBulletReloading]`
   limit: do 40 znaków
   EN: Reload [Germination]
   PL: Przeładowanie [Uzupełnienie Zarodników]
518. [Status [MeursaultSporeBulletReloading] — opis] - 포자탄(특수 탄환)에 적용되는 효과\n- 정신력을 ((16 - 보유한 포자탄의 합) / 2)만큼 소모하여, 보유한 포자탄[기본], 포자탄[산탄]을 각각 0으로 만들고, 최댓값만큼 얻음 (소수점 버림)
   źródło: Bufs.json :: dataList[id=MeursaultSporeBulletReloading].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Effect applied to Spore Round (Unique Ammo)\n- Consume ((16 - sum of Spore Round) / 2) SP(rounded down), reset both Spore Round [Base] and Spore Round [Buckshot] to 0 Stacks, and gain them up to max Stacks
   PL: - Efekt stosowany do Pocisków Zarodnikowych (szczególnej amunicji)\n- Zużywa ((16 - suma posiadanych Pocisków Zarodnikowych) / 2) Poczytalności (zaokrąglona w dół), wyzerowuje Pocisk Zarodnikowy [Podstawowy] i Pocisk Zarodnikowy [Śrut], po czym uzupełnia je do maksimum
519. [Status [MeursaultBeeGunLong] — nazwa] 호넷[라이플]
   źródło: Bufs.json :: dataList[id=MeursaultBeeGunLong].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBeeGunLong]`
   limit: do 40 znaków
   EN: Hornet [Rifle]
   PL: Hornet [Karabin]
520. [Status [MeursaultBeeGunLong] — opis] 현재 모드: 호넷[라이플]
   źródło: Bufs.json :: dataList[id=MeursaultBeeGunLong].desc
   limit: do 120 znaków
   EN: Current Mode: Hornet [Rifle]
   PL: Obecny tryb: Hornet [Karabin]
521. [Status [MeursaultBeeGunShort] — nazwa] 호넷[샷건]
   źródło: Bufs.json :: dataList[id=MeursaultBeeGunShort].name
   kontekst: identyfikator statusu w tekstach: `[MeursaultBeeGunShort]`
   limit: do 40 znaków
   EN: Hornet [Shotgun]
   PL: Hornet [Strzelba]
522. [Status [MeursaultBeeGunShort] — opis] 현재 모드: 호넷[샷건]
   źródło: Bufs.json :: dataList[id=MeursaultBeeGunShort].desc
   limit: do 120 znaków
   EN: Current Mode: Hornet [Shotgun]
   PL: Obecny tryb: Hornet [Strzelba]
523. [Status [MeursaultBeeGunShort] — tekst klimatyczny] 라이플이라는 형태에 얽매이지 않고, 호넷이 가지는 본질 그 자체를 들여다본다. \nepoché
   źródło: Bufs.json :: dataList[id=MeursaultBeeGunShort].flavor
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Instead of deferring the definition to its rifle-form, gaze into the core essence of "Hornet."\nepoché
   PL: Nie ograniczając się do formy karabinu, wgląd w samą istotę, jaką posiada Hornet.\nepoché
524. [Status [BulletGodok] — nazwa] 탄환 - 고독
   źródło: Bufs.json :: dataList[id=BulletGodok].name
   kontekst: identyfikator statusu w tekstach: `[BulletGodok]`
   limit: do 40 znaków
   EN: Bullet - Solitude
   PL: Pocisk - Samotność
525. [Status [BulletGodok] — opis] - 특수 탄환\n- 최댓값 : 6\n특정 스킬 사용시 탄환이 소모됨\n\n- 이 탄환은 외부 효과로 얻거나 값이 증가할 수 없음
   źródło: Bufs.json :: dataList[id=BulletGodok].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Capacity: 6\nSpent when using certain Skills\n\n- This Ammo's count cannot be gained or lost due to external effects
   PL: - Szczególna amunicja\n- Maks.: 6\nZużywana przy użyciu określonych Umiejętności\n\n- Nie można zyskać tego Pocisku ani zwiększyć jego wartości efektami zewnętrznymi
526. [Status [AlriuneEGOThey] — nazwa] 잔향
   źródło: Bufs.json :: dataList[id=AlriuneEGOThey].name
   kontekst: identyfikator statusu w tekstach: `[AlriuneEGOThey]`
   limit: do 40 znaków
   EN: Faint Aroma
   PL: Pogłos
527. [Status [AlriuneEGOThey] — opis] - 최댓값 : 30\n- 침잠 피해를 받으면, 수치 1 증가\n- 진동 폭발시, 자신을 제외한 무작위 아군 3명에게 잔향 1 ~ 2 부여  (환상체의 경우, 부위로 판정)\n- 수치가 최대면 진동을 2 얻고 진동 폭발, 자신의 침잠만큼 우울 피해를 받고 잔향 소멸. 이번 턴 동안 잔향을 얻을 수 없음\n- 사망 시, 아군에게 자신의 잔향을 수치의 절반만큼 무작위로 나눠서 부여 (소수점 버림)
   źródło: Bufs.json :: dataList[id=AlriuneEGOThey].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Gain 1 Stack if this unit takes Sinking damage\n- Upon Tremor Burst, apply 1~2 Faint Aroma on 3 other random allies (for Abnormalities, the Part)\n- At max Stack, gain 2 Tremor and trigger Tremor Burst on self; then, take Gloom damage equal to Sinking on self and lose all Faint Aroma. Cannot gain Faint Aroma for the rest of the turn.\n- If this unit is killed, inflict (remaining Faint Aroma on this unit / 2) Faint Aroma randomly between this unit's allies (rounded down)
   PL: - Maks.: 30\n- Przy otrzymaniu obrażeń Zatonięciem wartość rośnie o 1\n- Przy Wybuchu Wstrząsu nadaje 1-2 Pogłosów 3 losowym sojusznikom poza sobą (w przypadku Anomalii: częściom)\n- Przy maksymalnej wartości zyskuje 2 Wstrząsu i wywołuje Wybuch Wstrząsu, otrzymuje obrażenia Posępnością równe własnemu Zatonięciu, po czym Pogłos znika. Do końca tury nie może zyskać Pogłosu\n- Po śmierci losowo rozdziela połowę swojego Pogłosu między sojuszników (zaokrąglona w dół)
528. [Status [AlriuneEGOWe] — nazwa] 꽃잎
   źródło: Bufs.json :: dataList[id=AlriuneEGOWe].name
   kontekst: identyfikator statusu w tekstach: `[AlriuneEGOWe]`
   limit: do 40 znaków
   EN: Petals
   PL: Płatki
529. [Status [AlriuneEGOWe] — opis] - 최댓값 : 30\n- 수치 10당 공격 레벨 +1\n- 턴당 최대 15까지 얻을 수 있음
   źródło: Bufs.json :: dataList[id=AlriuneEGOWe].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Offense Level +1 for every 10 Stack\n- Can be gained up to 15 Stacks per turn
   PL: - Maks.: 30\n- Poziom Ataku +1 za każde 10 stosów\n- Można zyskać do 15 stosów na turę
530. [Status [GodokPanicType] — nazwa] 고독
   źródło: Bufs.json :: dataList[id=GodokPanicType].name
   kontekst: identyfikator statusu w tekstach: `[GodokPanicType]`
   limit: do 40 znaków
   EN: Solitude
   PL: Samotność
531. [Status [GodokPanicType] — opis] - 우울 속성 스킬로 받는 피해 +10%\n- 정신력이 있는 대상이면, 패닉 유형이 ‘고독’으로 변경됨\n- 정신력이 없는 대상이면, 턴 종료시 침잠 횟수 2 증가\n\n- 턴 종료시 1 감소\n- 이 효과는 합산되지 않고 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n※ 고독 패닉 효과\n- 사기 저하 : 턴 종료시 침잠 횟수 2 증가\n- 패닉 : 턴 종료시 침잠 횟수 3 증가
   źródło: Bufs.json :: dataList[id=GodokPanicType].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gloom Skills\n- SP Units: Change their Panic Type to 'Solitude'\n- Non-SP Units: Gain +2 Sinking Count at Turn End\n\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but cannot change their Panic Types\n\n※ Solitude Panic Effect:\n- Low Morale: Gain +2 Sinking Count at Turn End\n- Panic: Gain +3 Sinking Count at Turn End
   PL: - Otrzymuje +10% obrażeń od Umiejętności Posępności\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Samotność”\n- Jednostki bez Poczytalności: na koniec tury zyskuje 2 Liczniki Zatonięcia\n\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n※ Efekty Paniki „Samotności”\n- Spadek Moralu: na koniec tury zyskuje 2 Liczniki Zatonięcia\n- Panika: na koniec tury zyskuje 3 Liczniki Zatonięcia
532. [Status [Godok_Lowmorale] — nazwa] 고독
   źródło: Bufs.json :: dataList[id=Godok_Lowmorale].name
   kontekst: identyfikator statusu w tekstach: `[Godok_Lowmorale]`
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Status [Godok_Lowmorale] — opis] - 사기저하\n- 턴 종료시 침잠 횟수 2 증가
   źródło: Bufs.json :: dataList[id=Godok_Lowmorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn End: Gain +2 Sinking Count
   PL: - Spadek Moralu\n- Na koniec tury zyskuje 2 Liczniki Zatonięcia
534. [Status [Godok_Panic] — nazwa] 고독
   źródło: Bufs.json :: dataList[id=Godok_Panic].name
   kontekst: identyfikator statusu w tekstach: `[Godok_Panic]`
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Status [Godok_Panic] — opis] - 패닉\n- 턴 종료시 침잠 횟수 3 증가
   źródło: Bufs.json :: dataList[id=Godok_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn End: Gain +3 Sinking Count
   PL: - Panika\n- Na koniec tury zyskuje 3 Liczniki Zatonięcia
536. [Status [GodokPanicType_Sub] — nazwa] 고독
   źródło: Bufs.json :: dataList[id=GodokPanicType_Sub].name
   kontekst: identyfikator statusu w tekstach: `[GodokPanicType_Sub]`
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
537. [Status [GodokPanicType_Sub] — opis] - 우울 속성 스킬로 받는 피해 +10%\n- 턴 종료시 침잠 횟수 2 증가\n\n- 턴 종료시 1 감소\n- 이 효과는 합산되지 않고 갱신됨
   źródło: Bufs.json :: dataList[id=GodokPanicType_Sub].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gloom Skills\n- Turn End: Gain +2 Sinking Count\n\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value
   PL: - Otrzymuje +10% obrażeń od Umiejętności Posępności\n- Na koniec tury zyskuje 2 Liczniki Zatonięcia\n\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość
538. [Status [GodokPanicType_Main] — nazwa] 고독
   źródło: Bufs.json :: dataList[id=GodokPanicType_Main].name
   kontekst: identyfikator statusu w tekstach: `[GodokPanicType_Main]`
   (powtórzenie elementu 530 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
539. [Status [GodokPanicType_Main] — opis] - 우울 속성 스킬로 받는 피해 +10%\n- 패닉 유형이 ‘고독’으로 변경됨\n\n- 턴 종료시 1 감소\n- 이 효과는 합산되지 않고 갱신됨
   źródło: Bufs.json :: dataList[id=GodokPanicType_Main].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gloom Skills\n- Change Panic Type to 'Solitude'\n\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value
   PL: - Otrzymuje +10% obrażeń od Umiejętności Posępności\n- Zmienia rodzaj Paniki na „Samotność”\n\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość
540. [Status [SelfChargeAlly] — nazwa] 자가 충전
   źródło: Bufs.json :: dataList[id=SelfChargeAlly].name
   kontekst: identyfikator statusu w tekstach: `[SelfChargeAlly]`
   limit: do 40 znaków
   EN: Self-charge
   PL: Samoładowanie
541. [Status [SelfChargeAlly] — opis] - 최종 위력 +2\n- 수치가 감소할 때마다 그 수치만큼 자신의 충전 횟수 증가\n- 다음 조건 만족 시, 감소\n· 자신이 피격당한 스킬의 공격 종료 시, 1 감소\n· 공격 종료 시, 3 감소\n· 턴 종료 시, 5 감소\n- 최댓값 : 20\n- 이 효과가 소멸되기 전까지 체력이 1 미만으로 내려가지 않음
   źródło: Bufs.json :: dataList[id=SelfChargeAlly].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Final Power +2\n- Gain Charge Count equal to Stack lost\n- Lose Stack at:\n· Attack End of Skills that hit this unit (lose 1 Stack)\n· Attack End (lose 3 Stack)\n· Turn End (lose 5 Stack)\n- Max Stack: 20\n- This unit's HP cannot drop below 1 before this effect expires
   PL: - Moc Końcowa +2\n- Przy każdej utracie wartości zyskuje Licznik Ładowania równy utraconej ilości\n- Traci wartość przy:\n· zakończeniu ataku Umiejętności, która trafiła tę jednostkę (traci 1)\n· zakończeniu ataku (traci 3)\n· końcu tury (traci 5)\n- Maks.: 20\n- Dopóki efekt nie zniknie, HP nie spada poniżej 1
542. [Status [HighVoltageExoshell] — nazwa] 고전압 외피
   źródło: Bufs.json :: dataList[id=HighVoltageExoshell].name
   kontekst: identyfikator statusu w tekstach: `[HighVoltageExoshell]`
   limit: do 40 znaków
   EN: High-voltage Exoskeleton
   PL: Pancerz Wysokiego Napięcia
543. [Status [HighVoltageExoshell] — opis] - (수치 x 5)만큼 보호막을 얻음\n- (수치 x 5)만큼 보호막을 잃으면, 고전압 외피 1 감소\n- 턴 종료 시 충전 횟수를 고전압 외피 수치만큼 얻고, 고전압 외피와 고전압 외피 효과로 얻는 보호막 소멸\n- 최댓값 : 20
   źródło: Bufs.json :: dataList[id=HighVoltageExoshell].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain (Stack x 5) Shield\n- If this unit loses (Stack x 5) Shield, lose 1 Stack\n- Turn End: Gain Charge Count equal to Stack; both High-voltage Exoskeleton and Shield gained from its effect expire\n- Max Stack: 20
   PL: - Zyskuje (wartość x 5) Tarczy\n- Po utracie (wartość x 5) Tarczy traci 1 Pancerza Wysokiego Napięcia\n- Na koniec tury zyskuje Licznik Ładowania równy wartości, po czym Pancerz Wysokiego Napięcia i Tarcza z niego znikają\n- Maks.: 20
544. [Status [ChargedSting] — nazwa] 전하침
   źródło: Bufs.json :: dataList[id=ChargedSting].name
   kontekst: identyfikator statusu w tekstach: `[ChargedSting]`
   limit: do 40 znaków
   EN: Charged Sting
   PL: Naładowane Żądło
545. [Status [ChargedSting] — opis] - 충전 횟수(특수 충전 포함)를 획득하거나 소모하는 스킬로 받는 피해량이 수치당 4% 증가 (최대 20%)\n· 해당 스킬이 질투 속성이면, 효과가 강화되어 수치당 8% 증가 (최대 40%)\n- 최댓값 : 5\n- 효과 발동 조건에 맞는 스킬로 피격 후 해당 스킬 공격 종료 시 또는 턴 종료 시, 1 감소\n(단, 전하침을 부여하는 기본 공격 스킬로 피격받은 경우에는 수치가 감소하지 않음)
   źródło: Bufs.json :: dataList[id=ChargedSting].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every Stack, take +4% damage from Skills that gain or consume Charge Count (including 'Unique Charge') (max 20%)\n· For Envy Skills, strengthen this effect and take +8% damage for every Stack instead (max 40%)\n- Max Stack: 5\n- Lose 1 Stack at Attack End or Turn End after being hit by Skills that fulfill the effect-triggering conditions above (excluding Base Attack Skills that inflict Charged Sting)
   PL: - Otrzymuje +4% obrażeń za każdą wartość od Umiejętności zyskujących lub zużywających Licznik Ładowania (łącznie ze Szczególnym Ładowaniem) (maks. 20%)\n· Jeśli Umiejętność jest atrybutu Zazdrości, efekt się wzmacnia: +8% za wartość (maks. 40%)\n- Maks.: 5\n- Po trafieniu Umiejętnością spełniającą warunek traci 1 wartości na zakończeniu ataku tej Umiejętności lub na koniec tury\n(ale nie przy trafieniu bazową Umiejętnością ataku nadającą Naładowane Żądło)
546. [Status [FaustFlameMothEmber] — nazwa] 잔불
   źródło: Bufs.json :: dataList[id=FaustFlameMothEmber].name
   kontekst: identyfikator statusu w tekstach: `[FaustFlameMothEmber]`
   limit: do 40 znaków
   EN: Embers
   PL: Żar
547. [Status [FaustFlameMothEmber] — opis] - 최대 위력: 3\n- 최대 횟수: 6\n- 자신이 화상을 보유 중이면, 적으로부터 화상 위력, 화상 횟수 또는 특수 화상을 부여하는 스킬로 피격 시 횟수 1 감소 (E.G.O 스킬 포함)\n\n- 자신에게 화상이 없는 상태로 피격 시 횟수 6으로 초기화\n\n- 횟수가 0이면, 아래 효과 적용\n· 자신의 화상 1회 발동. 화상 횟수 1 감소\n· 잔불 위력 1 감소\n· 남은 잔불 위력이 1 이상이면, 횟수 6으로 초기화
   źródło: Bufs.json :: dataList[id=FaustFlameMothEmber].desc
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 3\n- Max Count: 6\n- If this unit has Burn, lose 1 Embers Count when hit by a Skill that inflicts Burn Potency, Count, or 'Unique Burn' (including E.G.O Skills)\n\n- If this unit does not have Burn, reset Embers Count to 6 when hit (independent of Skills that inflict Burn)\n\n- At 0 Embers Count, activate the following effects:\n· Activate Burn on self once and lose 1 Burn Count\n· Lose 1 Embers Potency\n· If this unit has 1+ remaining Embers Potency, reset Embers Count to 6
   PL: - Maks. Mocy: 3\n- Maks. Licznika: 6\n- Jeśli jednostka ma Podpalenie, traci 1 Licznika Żaru przy trafieniu Umiejętnością nadającą Moc, Licznik lub Szczególne Podpalenie (łącznie z Umiejętnościami E.G.O)\n\n- Przy trafieniu bez Podpalenia Licznik Żaru wraca do 6\n\n- Przy 0 Liczników Żaru:\n· Aktywuje własne Podpalenie raz i traci 1 Licznik Podpalenia\n· Traci 1 Mocy Żaru\n· Przy 1 lub więcej pozostałej Mocy Żaru Licznik wraca do 6
548. [Status [ChargeBodyArt] — nazwa] 생체 재료
   źródło: Bufs.json :: dataList[id=ChargeBodyArt].name
   kontekst: identyfikator statusu w tekstach: `[ChargeBodyArt]`
   limit: do 40 znaków
   EN: Corpus Ingredient
   PL: Materiał Biologiczny
549. [Status [ChargeBodyArt] — opis] - 횟수 최댓값: 20\n- 특수 충전\n- 충전 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용 받음\n- 턴 종료 시 횟수 1 감소\n\n<color=#1aece7>횟수 누적 소모량: {2}</color>
   źródło: Bufs.json :: dataList[id=ChargeBodyArt].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#1aece7>, </color>, {2}, \n
   EN: - Max Count: 20\n- Unique Charge\n- Interacts the same way as normal Charge does to effects that raise or reduce Charge Potency and Count\n- Turn End: Lose 1 Count\n\n<color=#1aece7>Cumulative Count consumed: {2}</color>
   PL: - Maks. Licznika: 20\n- Szczególne Ładowanie\n- Podlega w ten sam sposób efektom zwiększającym lub zmniejszającym Moc i Licznik Ładowania\n- Na koniec tury Licznik maleje o 1\n\n<color=#1aece7>Skumulowane zużycie Licznika: {2}</color>
550. [Status [ChargeBodyArt] — podsumowanie] 특정 스킬 사용 시 증가 또는 소모
   źródło: Bufs.json :: dataList[id=ChargeBodyArt].summary
   limit: do 120 znaków
   EN: Consumed or gained when using certain Skills
   PL: Zyskiwany lub zużywany przy użyciu określonych Umiejętności
551. [Status [TibiaPersonality] — nazwa] 작품명: 티비아
   źródło: Bufs.json :: dataList[id=TibiaPersonality].name
   kontekst: identyfikator statusu w tekstach: `[TibiaPersonality]`
   limit: do 40 znaków
   EN: Artwork: Tibia
   PL: Dzieło: Tibia
552. [Status [TibiaPersonality] — opis] 생체 재료 위력에 따라 기본 공격 스킬과 합 가능 반격 스킬이 아래 효과 얻음\n- 1 ~ : 기본 위력 +1\n- 2 ~ : 적에게 출혈 또는 특수 출혈이 있으면, 피해량 +10%\n- 3 ~ : 출혈 위력, 횟수 부여 값 +1\n- 4 ~ : 기본 위력 +1\n- 5 ~ : 기본 위력 +1
   źródło: Bufs.json :: dataList[id=TibiaPersonality].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effects to this unit's Base Attack Skills and Clashable Counter Skill based on Corpus Ingredient Potency:\n- 1+ : Base Power +1\n- 2+ : If the enemy has Bleed or 'Unique Bleed', deal +10% damage\n- 3+ : Inflict +1 more Bleed Potency and Count\n- 4+ : Base Power +1\n- 5+ : Base Power +1
   PL: Na podstawie Mocy Materiału Biologicznego bazowe Umiejętności ataku i Umiejętności kontr zdatne do Starcia zyskują:\n- 1 lub więcej: Moc Bazowa +1\n- 2 lub więcej: +10% obrażeń, jeśli wróg ma Krwawienie lub Szczególne Krwawienie\n- 3 lub więcej: nadaje o 1 więcej Mocy i Licznika Krwawienia\n- 4 lub więcej: Moc Bazowa +1\n- 5 lub więcej: Moc Bazowa +1
553. [Status [TibiaPersonality] — podsumowanie] 생체 재료 위력에 따라 다양한 효과를 얻음
   źródło: Bufs.json :: dataList[id=TibiaPersonality].summary
   limit: do 120 znaków
   EN: Gain various effects based on Corpus Ingredient Potency
   PL: Zyskuje różne efekty w zależności od Mocy Materiału Biologicznego
554. [Status [MelodyBodyArt] — nazwa] 신체가 울리는 선율
   źródło: Bufs.json :: dataList[id=MelodyBodyArt].name
   kontekst: identyfikator statusu w tekstach: `[MelodyBodyArt]`
   limit: do 50 znaków
   EN: Somatic Frisson-inspiring Melody
   PL: Melodia Drgającego Ciała
555. [Status [MelodyBodyArt] — opis] - 속도 최솟값, 최댓값 +1\n- 기본 공격 스킬의 합 위력 +1, 피해량 +10%
   źródło: Bufs.json :: dataList[id=MelodyBodyArt].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Base Attack Skills gain Clash Power +1 and deal +10% damage
   PL: - Minimalna i maksymalna Szybkość +1\n- Bazowe Umiejętności ataku zyskują Moc Starcia +1 i zadają +10% obrażeń
556. [Status [MelodyBodyArt] — podsumowanie] 속도 최솟값, 최댓값 증가\n기본 공격 스킬의 합 위력, 피해량 증가함
   źródło: Bufs.json :: dataList[id=MelodyBodyArt].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain Min & Max Speed\n- Base Attack Skills gain Clash Power and deal more damage
   PL: Minimalna i maksymalna Szybkość rosną\nBazowe Umiejętności ataku zyskują Moc Starcia i zadają więcej obrażeń
557. [Status [MelodyBodyArtChebello] — nazwa] 신체가 울리는 선율[강화됨]
   źródło: Bufs.json :: dataList[id=MelodyBodyArtChebello].name
   kontekst: identyfikator statusu w tekstach: `[MelodyBodyArtChebello]`
   limit: do 60 znaków
   EN: Somatic Frisson-inspiring Melody [Empowered]
   PL: Melodia Drgającego Ciała [Wzmocniona]
558. [Status [MelodyBodyArtChebello] — opis] - 속도 최솟값, 최댓값 +2\n- 기본 공격 스킬의 합 위력 +2, 피해량 +20%
   źródło: Bufs.json :: dataList[id=MelodyBodyArtChebello].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- Base Attack Skills gain Clash Power +2 and deal +20% damage
   PL: - Minimalna i maksymalna Szybkość +2\n- Bazowe Umiejętności ataku zyskują Moc Starcia +2 i zadają +20% obrażeń
559. [Status [MelodyBodyArtChebello] — podsumowanie] 속도 최솟값, 최댓값 증가\n기본 공격 스킬의 합 위력, 피해량 증가함
   źródło: Bufs.json :: dataList[id=MelodyBodyArtChebello].summary
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
560. [Status [LivingSpecimenPersonality] — nazwa] 신체관극
   źródło: Bufs.json :: dataList[id=LivingSpecimenPersonality].name
   kontekst: identyfikator statusu w tekstach: `[LivingSpecimenPersonality]`
   limit: do 40 znaków
   EN: Corpus Theater
   PL: Teatr Ciała
561. [Status [LivingSpecimenPersonality] — opis] - 기본값: 3\n- 적의 공격 스킬로 자신에게 출혈이 부여되면, 다음 턴에 아래의 무작위 효과 1개를 얻고, 이 효과 수치 1 감소 (스킬당 1회)\n· 출혈 위력 3\n· 속박 1\n· 수비 위력 감소 1
   źródło: Bufs.json :: dataList[id=LivingSpecimenPersonality].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- When this unit gains Bleed from enemy Attack Skills, randomly gain 1 of the following effects next turn and lose 1 Stack of this effect (once per Skill)\n  · 3 Bleed Potency\n  · 1 Bind\n  · 1 Defense Power Down
   PL: - Wartość bazowa: 3\n- Gdy wrogska Umiejętność ataku nadaje tej jednostce Krwawienie, zyskuje w następnej turze 1 losowy efekt poniżej i traci 1 wartości (raz na Umiejętność)\n· 3 Mocy Krwawienia\n· 1 Spętania\n· 1 Spadek Mocy Obrony
562. [Status [LivingSpecimenPersonality] — podsumowanie] 출혈 위력, 속박, 수비 위력 감소 중 무작위 1개의 효과를 얻음
   źródło: Bufs.json :: dataList[id=LivingSpecimenPersonality].summary
   limit: do 120 znaków
   EN: Randomly gain 1 of the following: Bleed Potency, Bind, or Defense Power Down
   PL: Losowo zyskuje 1 z następujących: Moc Krwawienia, Spętanie lub Spadek Mocy Obrony
563. [Status [GoldenOpportunity] — nazwa] 조망
   źródło: Bufs.json :: dataList[id=GoldenOpportunity].name
   kontekst: identyfikator statusu w tekstach: `[GoldenOpportunity]`
   limit: do 40 znaków
   EN: Viewing the Tableau
   PL: Podziwianie Tableau
564. [Status [GoldenOpportunity] — opis] - 전장에 거미집 약지 제자 파우스트가 있으면, 턴 시작 시 보호 2 얻음\n- 턴 종료 시 수치 2 감소
   źródło: Bufs.json :: dataList[id=GoldenOpportunity].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If The House of Spiders: The Ring Apprentice Faust is on the field, gain 2 Protection at Turn Start\n- Turn End: Lose 2 Stack
   PL: - Jeśli na polu jest Dom Pajęczyn: Uczeń Serdecznego Faust, na początku tury zyskuje 2 Ochrony\n- Na koniec tury wartość maleje o 2
565. [Status [GoldenOpportunity] — podsumowanie] 조건 만족 시 보호 얻음
   źródło: Bufs.json :: dataList[id=GoldenOpportunity].summary
   limit: do 120 znaków
   EN: Gain Protection when conditions are met
   PL: Zyskuje Ochronę po spełnieniu warunków
566. [Status [IronMaidenPersonality] — nazwa] 아이언 메이든
   źródło: Bufs.json :: dataList[id=IronMaidenPersonality].name
   kontekst: identyfikator statusu w tekstach: `[IronMaidenPersonality]`
   limit: do 40 znaków
   EN: Iron Maiden
   PL: Iron Maiden
567. [Status [IronMaidenPersonality] — opis] - 가장 왼쪽 슬롯의 도발치 +4\n- 턴 시작 시 보호 1, 방어 레벨 증가 5 얻고 보호막을 현재 체력의 5%만큼 얻음\n- 공격자의 마지막 코인으로 피격 시 공격자에게 해당 코인으로 받은 피해량의 20%만큼 관통 피해를 입히고 출혈 횟수 2 증가 (스킬당 1회, 턴당 최대 3회, 턴당 최대 피해 60)
   źródło: Bufs.json :: dataList[id=IronMaidenPersonality].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +4 Aggro to the leftmost Slot\n- Turn Start: Gain 1 Protection, 5 Defense Level Up, and Shield HP equal to 5% of this unit's current HP\n- When hit by the last Coin of an attacker, deal Pierce damage equal to 20% of the said Coin's damage and inflict +2 Bleed Count (max once per Skill, 3 times per turn. Max damage per turn: 60)
   PL: - Wartość Prowokacji skrajnie lewego slotu +4\n- Na początku tury zyskuje 1 Ochrony, 5 Wzrostów Poziomu Obrony i Tarczę równą 5% aktualnego HP\n- Przy trafieniu ostatnią monetą atakującego zadaje mu obrażenia Przebiciem równe 20% obrażeń od tej monety i nadaje atakującemu 2 Liczniki Krwawienia (raz na Umiejętność, do 3 razy na turę, maks. 60 obrażeń na turę)
568. [Status [IronMaidenPersonality] — podsumowanie] 가장 왼쪽 슬롯의 도발치 증가\n보호, 방어 레벨 증가, 보호막 얻음\n조건 만족 시 공격자에게 관통 피해 입히고 출혈 횟수 증가
   źródło: Bufs.json :: dataList[id=IronMaidenPersonality].summary
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain Aggro to the leftmost Slot\n- Gain Protection, Defense Level Up, and Shield\n- When conditions are met, deal Pierce damage and inflict Bleed count on the attacker
   PL: Zwiększa Wartość Prowokacji skrajnie lewego slotu\nZyskuje Ochronę, Wzrost Poziomu Obrony i Tarczę\nPo spełnieniu warunków zadaje atakującemu obrażenia Przebiciem i nadaje mu Liczniki Krwawienia
569. [Status [SilverOpportunity] — nazwa] 구속 해제 - 창작 몰입
   źródło: Bufs.json :: dataList[id=SilverOpportunity].name
   kontekst: identyfikator statusu w tekstach: `[SilverOpportunity]`
   limit: do 50 znaków
   EN: The Self Unbound - Flow State
   PL: Uwolnienie Jaźni - Stan Przepływu
570. [Status [SilverOpportunity] — opis] - 속도 최솟값, 최댓값 +2\n- 기본 스킬이 교체됨\n- 자신보다 속도가 낮은 적에게 기본 공격 스킬로 가하는 피해량 +10%
   źródło: Bufs.json :: dataList[id=SilverOpportunity].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- Gain a new set of Base Skills\n- Deal +20% damage with Base Attack Skills to enemies whose Speed is slower than this unit
   PL: - Minimalna i maksymalna Szybkość +2\n- Zyskuje nowy zestaw Umiejętności bazowych\n- Bazowe Umiejętności ataku zadają +10% obrażeń wrogom o niższej Szybkości
571. [Status [SilverOpportunity] — podsumowanie] 속도 최솟값, 최댓값 증가\n기본 스킬 교체됨\n조건 만족 시 피해량 증가
   źródło: Bufs.json :: dataList[id=SilverOpportunity].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Min & Max Speed\nGain a new set of Base Skills\nWhen conditions are met, deal more damage
   PL: Min. i maks. Szybkość rosną\nUmiejętności bazowe zostają zastąpione\nPo spełnieniu warunków zadaje więcej obrażeń
572. [Status [FasciaPersonality] — nazwa] 작품명: 파시아
   źródło: Bufs.json :: dataList[id=FasciaPersonality].name
   kontekst: identyfikator statusu w tekstach: `[FasciaPersonality]`
   limit: do 40 znaków
   EN: Artwork: Fascia
   PL: Dzieło: Fascia
573. [Status [FasciaPersonality] — opis] 생체 재료 위력에 따라 기본 공격 스킬과 합 가능 반격 스킬이 아래 효과 얻음\n- 1 ~ : 기본 위력 +1\n- 2 ~ : 적에게 출혈 또는 특수 출혈이 있으면, 피해량 +10%\n- 3 ~ : 출혈 위력, 횟수 부여 값 +1\n- 4 ~ : 기본 위력 +1
   źródło: Bufs.json :: dataList[id=FasciaPersonality].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Apply the following effects to this unit's Base Attack Skills and Clashable Counter Skill based on Corpus Ingredient Potency:\n- 1+ : Base Power +1\n- 2+ : If the enemy has Bleed or 'Unique Bleed', deal +10% damage\n- 3+ : Inflict +1 more Bleed Potency and Count\n- 4+ : Base Power +1
   PL: Na podstawie Mocy Materiału Biologicznego bazowe Umiejętności ataku i Umiejętności kontr zdatne do Starcia zyskują:\n- 1 lub więcej: Moc Bazowa +1\n- 2 lub więcej: +10% obrażeń, jeśli wróg ma Krwawienie lub Szczególne Krwawienie\n- 3 lub więcej: nadaje o 1 więcej Mocy i Licznika Krwawienia\n- 4 lub więcej: Moc Bazowa +1
574. [Status [FasciaPersonality] — podsumowanie] 생체 재료 위력에 따라 다양한 효과를 얻음
   źródło: Bufs.json :: dataList[id=FasciaPersonality].summary
   (powtórzenie elementu 553 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
575. [Status [FaubismMaskMeursault] — nazwa] 야수파 - 마스크 드 시앵
   źródło: Bufs.json :: dataList[id=FaubismMaskMeursault].name
   kontekst: identyfikator statusu w tekstach: `[FaubismMaskMeursault]`
   limit: do 50 znaków
   EN: Le Fauvisme - Masque de Chien
   PL: Le Fauvisme - Masque de Chien
576. [Status [FaubismMaskMeursault] — opis] - 대상의 찢긴 색채 3당, 가하는 피해량 +5% (최대 15%)\n- 기본 스킬로 부여하는 출혈, 침잠 위력 부여량 +1\n- 기본 스킬 적중 전 대상에게 출혈이 없으면, 대상의 출혈 횟수 2 증가 (턴당 1회)
   źródło: Bufs.json :: dataList[id=FaubismMaskMeursault].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +5% damage for every 3 Mauled Color on target (max 15%)\n- Inflict +1 more Bleed and Sinking Potency with Base Skills\n- Before hitting with a Base Skill, if target does not have Bleed, inflict +2 Bleed Count on target (once per turn)
   PL: - Zadaje +5% obrażeń za każde 3 Rwanego Barwy [Rouge] na celu (maks. 15%)\n- Umiejętności bazowe nadają o 1 więcej Mocy Krwawienia i Zatonięcia\n- Przed trafieniem Umiejętnością bazową, jeśli cel nie ma Krwawienia, nadaje mu 2 Liczniki Krwawienia (raz na turę)
577. [Status [TestWaitingMeursault] — nazwa] 결점 보완
   źródło: Bufs.json :: dataList[id=TestWaitingMeursault].name
   kontekst: identyfikator statusu w tekstach: `[TestWaitingMeursault]`
   limit: do 40 znaków
   EN: Imperfections Addressed
   PL: Kompensacja Wad
578. [Status [TestWaitingMeursault] — opis] - 가하는 피해량 +10%\n- 약지 야수파 도슨트 로쟈의 ‘크리틱’ 스킬 코인 재사용 시 정신력 3 회복 (턴당 1회)\n- 턴 시작 시 약지 야수파 도슨트 로쟈에게 레플렉시옹이 없으면 소멸
   źródło: Bufs.json :: dataList[id=TestWaitingMeursault].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage\n- On Reuse of a Coin in The Ring Fauvist Docent Rodion's "Critique" Skill, heal 3 SP (once per turn)\n- Turn Start: If The Ring Fauvist Docent Rodion does not have Réflexion, this effect expires
   PL: - Zadawane obrażenia +10%\n- Przy ponownym użyciu monety Umiejętności „Krytyka” Docentki Fowizmu Serdecznego Rodion regeneruje 3 Poczytalności (raz na turę)\n- Na początku tury znika, jeśli Docentka Fowizmu Serdecznego Rodion nie ma Réflexion
579. [Status [FaubismWolfMaskRodion] — nazwa] 야수파 - 마스크 드 루
   źródło: Bufs.json :: dataList[id=FaubismWolfMaskRodion].name
   kontekst: identyfikator statusu w tekstach: `[FaubismWolfMaskRodion]`
   limit: do 40 znaków
   EN: Le Fauvisme - Masque de Loup
   PL: Le Fauvisme - Masque de Loup
580. [Status [FaubismWolfMaskRodion] — opis] - 속도 최솟값, 최댓값 +1\n- 기본 스킬로 부여하는 출혈, 침잠 위력 부여량 +1\n- 공격 적중시 대상의 찢긴 색채 [블뢰]가 3 이상이면 침잠 횟수 1 증가 (턴당 1회)\n- 공격 적중시 대상의 찢긴 색채 [루주]가 3 이상이면 출혈 횟수 1 증가 (턴당 1회)
   źródło: Bufs.json :: dataList[id=FaubismWolfMaskRodion].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Inflict +1 more Bleed and Sinking Potency with Base Skills\n- On Hit, if target has 3+ Mauled Color [Bleu], inflict +1 Sinking Count (once per turn)\n- On Hit, if target has 3+ Mauled Color [Rouge], inflict +1 Bleed Count (once per turn)
   PL: - Minimalna i maksymalna Szybkość +1\n- Umiejętności bazowe nadają o 1 więcej Mocy Krwawienia i Zatonięcia\n- Przy trafieniu, jeśli cel ma 3 lub więcej Rwanej Barwy [Bleu], zyskuje 1 Licznik Zatonięcia (raz na turę)\n- Przy trafieniu, jeśli cel ma 3 lub więcej Rwanej Barwy [Rouge], zyskuje 1 Licznik Krwawienia (raz na turę)
581. [Status [BoldBrushstrokesRodion] — nazwa] 과감한 터치
   źródło: Bufs.json :: dataList[id=BoldBrushstrokesRodion].name
   kontekst: identyfikator statusu w tekstach: `[BoldBrushstrokesRodion]`
   limit: do 40 znaków
   EN: Touche Hardie
   PL: Touche Hardie
582. [Status [BoldBrushstrokesRodion] — opis] - 최댓값 : 2\n- 수치 1당 출혈 효과와 침잠 효과로 받는 체력, 정신력 피해량 +10% (최대 20%, 소수점 버림)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BoldBrushstrokesRodion].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take +10% HP and SP damage from Bleed and Sinking effects for every Stack (max 20%, rounded down)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Otrzymuje +10% obrażeń HP i Poczytalności od efektów Krwawienia i Zatonięcia za każdą wartość (maks. 20%, zaokrąglona w dół)\n- Na koniec tury maleje o 1
583. [Status [IntenseColorsRodion] — nazwa] 강렬한 색채
   źródło: Bufs.json :: dataList[id=IntenseColorsRodion].name
   kontekst: identyfikator statusu w tekstach: `[IntenseColorsRodion]`
   limit: do 40 znaków
   EN: Palette Vibrante
   PL: Palette Vibrante
584. [Status [IntenseColorsRodion] — opis] - 최댓값 : 4\n- 약지 소속 인격에게 받는 피해량 +(수치 x 2.5)% \n· 공격자가 약지 소속이면서 야수파 소속이면, 대신 받는 피해량 +(수치×5)%\n- 전투 시작 시 수치만큼 출혈, 침잠, 출혈 횟수, 침잠 횟수 중 무작위로 1씩 얻음\n- 전투 종료 시 이 효과가 소멸되고 찢긴 색채 [루주], 찢긴 색채 [블뢰] 수치가 절반으로 감소 (소수점 버림)
   źródło: Bufs.json :: dataList[id=IntenseColorsRodion].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Take +(Stack x 2.5)% damage from The Ring-faction Identities\n· If the attacker is in both The Ring faction and School of Fauvism faction, take +(Stack x 5)% damage instead\n- Combat Start: Randomly gain 1 Bleed, 1 Sinking, 1 Bleed Count, or 1 Sinking Count (Stack) times\n- Combat End: This effect expires. Halve Mauled Color [Rouge] and Mauled Color [Bleu] Stacks on this unit (rounded down)
   PL: - Maks.: 4\n- Otrzymuje +(wartość x 2,5)% obrażeń od osobowości Stronnictwa Serdecznego\n· Jeśli atakujący należy zarówno do Stronnictwa Serdecznego, jak i do Szkoły Fowizmu, otrzymuje zamiast tego +(wartość x 5)% obrażeń\n- Na początku walki losowo zyskuje po 1 Krwawienia, Zatonięcia, Licznika Krwawienia lub Licznika Zatonięcia (tyle razy, ile wynosi wartość)\n- Po zakończeniu walki efekt znika, a stosy Rwanej Barwy [Rouge] i Rwanej Barwy [Bleu] maleją o połowę (zaokrąglona w dół)
585. [Status [ThankyouDocentRodion] — nazwa] 경의
   źródło: Bufs.json :: dataList[id=ThankyouDocentRodion].name
   kontekst: identyfikator statusu w tekstach: `[ThankyouDocentRodion]`
   limit: do 40 znaków
   EN: L'Hommage
   PL: L'Hommage
586. [Status [ThankyouDocentRodion] — opis] - 최댓값: 3\n- 턴 시작 시 수치당 공격 레벨 증가나 방어 레벨 증가 중 무작위로 1 얻음 (최대 3회)\n- 턴 종료시 소멸
   źródło: Bufs.json :: dataList[id=ThankyouDocentRodion].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Randomly gain 1 Offense Level Up or 1 Defense Level Up for every Stack (max 3 times)\n- Turn End: This effect expires
   PL: - Maks.: 3\n- Na początku tury losowo zyskuje za każdą wartość 1 Wzrost Poziomu Ataku lub 1 Wzrost Poziomu Obrony (do 3 razy)\n- Znika na koniec tury
587. [Status [TestWaitDocentRodion] — nazwa] 레플렉시옹
   źródło: Bufs.json :: dataList[id=TestWaitDocentRodion].name
   kontekst: identyfikator statusu w tekstach: `[TestWaitDocentRodion]`
   limit: do 40 znaków
   EN: Réflexion
   PL: Réflexion
588. [Status [TestWaitDocentRodion] — opis] - 최댓값: 2\n- 이 효과가 있는 턴 동안 ‘크리틱’을 사용할 수 없음\n- 턴 시작시 정신력 5 회복\n- 턴 종료시 1 감소\n- 이 버프 소멸 시 (전장에 있는 스튜던트 인격 수)만큼 다음 턴에 경의를 얻음
   źródło: Bufs.json :: dataList[id=TestWaitDocentRodion].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Cannot use "Critique" during the turn this unit has this effect\n- Turn Start: Heal 5 SP\n- Turn End: Lose 1 Stack\n- When this effect expires, gain L'Hommage next turn equal to the number of The Ring Student Identities on the field
   PL: - Maks.: 2\n- W turze posiadania tego efektu nie można użyć „Krytyki”\n- Na początku tury regeneruje 5 Poczytalności\n- Na koniec tury maleje o 1\n- Po zniknięciu wzmocnienia zyskuje w następnej turze tyle L'Hommage, ile osobowości Studentów Serdecznego jest na polu
589. [Status [BearClawWoundAlly] — nazwa] 찢긴 색채 [루주]
   źródło: Bufs.json :: dataList[id=BearClawWoundAlly].name
   kontekst: identyfikator statusu w tekstach: `[BearClawWoundAlly]`
   limit: do 40 znaków
   EN: Mauled Color [Rouge]
   PL: Rwana Barwa [Rouge]
590. [Status [BearClawWoundAlly] — opis] - 최댓값 : 9\n- 피격 시 수치 3당 출혈 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 다음 턴에 수치 4당 방어 레벨 감소 1 얻음 (최대 2)\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=BearClawWoundAlly].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Bleed Potency for every 3 Stack (once per turn)\n- Turn End: Gain 1 Defense Level Down next turn for every 4 Stack (max 2)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 9\n- Przy trafieniu zyskuje 1 Mocy Krwawienia za każde 3 wartości (raz na turę)\n- Na koniec tury zyskuje w następnej turze 1 Spadek Poziomu Obrony za każde 4 wartości (maks. 2)\n- Na koniec tury maleje o 1
591. [Status [EagleClawWoundAlly] — nazwa] 찢긴 색채 [블뢰]
   źródło: Bufs.json :: dataList[id=EagleClawWoundAlly].name
   kontekst: identyfikator statusu w tekstach: `[EagleClawWoundAlly]`
   limit: do 40 znaków
   EN: Mauled Color [Bleu]
   PL: Rwana Barwa [Bleu]
592. [Status [EagleClawWoundAlly] — opis] - 최댓값 : 9\n- 피격 시 수치 3당 침잠 위력 1 얻음 (턴당 1회)\n- 턴 종료 시 수치가 5 이상이면, 정신력 5 감소\n- 턴 종료 시 1 감소
   źródło: Bufs.json :: dataList[id=EagleClawWoundAlly].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 9\n- When hit, gain 1 Sinking Potency for every 3 Stack (once per turn)\n- Turn End: At 5+ Stack, lose 5 SP\n- Turn End: Lose 1 Stack
   PL: - Maks.: 9\n- Przy trafieniu zyskuje 1 Mocy Zatonięcia za każde 3 wartości (raz na turę)\n- Na koniec tury, przy 5 lub więcej wartości, traci 5 Poczytalności\n- Na koniec tury maleje o 1
593. [Status [VengeanceBookHeathcliff] — nazwa] 앙갚음 장부 [히스클리프]
   źródło: Bufs.json :: dataList[id=VengeanceBookHeathcliff].name
   kontekst: identyfikator statusu w tekstach: `[VengeanceBookHeathcliff]`
   limit: do 50 znaków
   EN: Book of Vengeance [Heathcliff]
   PL: Rejestr Odwetu [Heathcliff]
594. [Status [VengeanceBookHeathcliff] — opis] - 최댓값 : 30\n- 수치 5당 공격 레벨 +1, 방어 레벨 +1
   źródło: Bufs.json :: dataList[id=VengeanceBookHeathcliff].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Offense Level +1, Defense Level +1 for every 5 Stack
   PL: - Maks.: 30\n- Poziom Ataku +1, Poziom Obrony +1 za każde 5 wartości
595. [Status [MiddleFingerTattooID] — nazwa] 원한 문신
   źródło: Bufs.json :: dataList[id=MiddleFingerTattooID].name
   kontekst: identyfikator statusu w tekstach: `[MiddleFingerTattooID]`
   limit: do 40 znaków
   EN: Vengeance Tattoo
   PL: Tatuaż Zemsty
