# Paczka AI P19 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 5/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P19_2a_slowa_kluczowe_i_statusy_cz05.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P19_2a_slowa_kluczowe_i_statusy_cz05.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords
- plik gry: `BattleKeywords.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [ATL_Agility] — nazwa] 더 빠르게!
   źródło: BattleKeywords.json :: dataList[id=ATL_Agility].name
   kontekst: identyfikator tagu w tekstach: `[ATL_Agility]`
   limit: do 40 znaków
   EN: Faster!
   PL: Szybciej!
2. [Słowo kluczowe [ATL_Agility] — opis] 신속 2 얻음
   źródło: BattleKeywords.json :: dataList[id=ATL_Agility].desc
   limit: do 120 znaków
   EN: Gain 2 Haste
   PL: Zyskuje 2 Pośpiechu
3. [Słowo kluczowe [ATL_Breath] — nazwa] 더 정확하게!
   źródło: BattleKeywords.json :: dataList[id=ATL_Breath].name
   kontekst: identyfikator tagu w tekstach: `[ATL_Breath]`
   limit: do 40 znaków
   EN: Aim True!
   PL: Celniej!
4. [Słowo kluczowe [ATL_Breath] — opis] 호흡 3 얻음
   źródło: BattleKeywords.json :: dataList[id=ATL_Breath].desc
   limit: do 120 znaków
   EN: Gain 3 Poise
   PL: Zyskuje 3 Oddechu
5. [Słowo kluczowe [ATL_Target] — nazwa] 저 놈 잡아!
   źródło: BattleKeywords.json :: dataList[id=ATL_Target].name
   kontekst: identyfikator tagu w tekstach: `[ATL_Target]`
   limit: do 40 znaków
   EN: Get 'Em!
   PL: Złapcie Go!
6. [Słowo kluczowe [ATL_Target] — opis] 한 명의 적을 동시 공격합니다.
   źródło: BattleKeywords.json :: dataList[id=ATL_Target].desc
   limit: do 120 znaków
   EN: Simultaneously attacks one unit.
   PL: Atakuje jednocześnie jedną jednostkę.
7. [Słowo kluczowe [Bull_FadedHeat] — nazwa] 잠시 사그라든 열기
   źródło: BattleKeywords.json :: dataList[id=Bull_FadedHeat].name
   kontekst: identyfikator tagu w tekstach: `[Bull_FadedHeat]`
   limit: do 40 znaków
   EN: Momentary Cool
   PL: Chwilowe Ostudzenie
8. [Słowo kluczowe [Bull_FadedHeat] — opis] 본체와 몸통 부위의 최대 체력 -50%
   źródło: BattleKeywords.json :: dataList[id=Bull_FadedHeat].desc
   limit: do 120 znaków
   EN: Core and body lose 50% Max HP
   PL: Korpus i część Tułowia tracą 50% Maks. HP
9. [Słowo kluczowe [Bull_Fever] — nazwa] 흥분
   źródło: BattleKeywords.json :: dataList[id=Bull_Fever].name
   kontekst: identyfikator tagu w tekstach: `[Bull_Fever]`
   limit: do 40 znaków
   EN: Fever
   PL: Podniecenie
10. [Słowo kluczowe [Bull_Fever] — opis] 가하는 피해량 수치x10%만큼 증가.\n턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=Bull_Fever].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +10% damage per Count\nReduced by 1 at turn end
   PL: Zadawane obrażenia rosną o wartość x 10%\nNa koniec tury maleje o 1
11. [Słowo kluczowe [Bull_ReinforcedSadness] — nazwa] 팽창하는 슬픔
   źródło: BattleKeywords.json :: dataList[id=Bull_ReinforcedSadness].name
   kontekst: identyfikator tagu w tekstach: `[Bull_ReinforcedSadness]`
   limit: do 40 znaków
   EN: Expanding Sorrow
   PL: Rozszerzający Smutek
12. [Słowo kluczowe [Bull_ReinforcedSadness] — opis] 스킬 패턴이 변경됨.
   źródło: BattleKeywords.json :: dataList[id=Bull_ReinforcedSadness].desc
   limit: do 120 znaków
   EN: Changes behavior.
   PL: Zmienia wzorzec Umiejętności.
13. [Słowo kluczowe [Bull_ReinforcedSadness] — podsumowanie] 스킬 패턴이 변경됨.
   źródło: BattleKeywords.json :: dataList[id=Bull_ReinforcedSadness].summary
   (powtórzenie elementu 12 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
14. [Słowo kluczowe [Crazy_LowMorale] — nazwa] 광인
   źródło: BattleKeywords.json :: dataList[id=Crazy_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Crazy_LowMorale]`
   limit: do 40 znaków
   EN: Maddened
   PL: Szaleniec
15. [Słowo kluczowe [Crazy_LowMorale] — opis] - 사기 저하\n- 첫 사기저하일 때, 피아식별 불가상태
   źródło: BattleKeywords.json :: dataList[id=Crazy_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When at low morale for the first time, targets units indiscriminately
   PL: - Spadek Moralu\n- Przy pierwszym Spadku Moralu atakuje sojuszników i wrogów bez rozeznania
16. [Słowo kluczowe [Crazy_Panic] — nazwa] 광인
   źródło: BattleKeywords.json :: dataList[id=Crazy_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Crazy_Panic]`
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Słowo kluczowe [Crazy_Panic] — opis] - 패닉\n- 피아식별 불가상태, 합 위력 +1, 피해량 증가 2 얻음
   źródło: BattleKeywords.json :: dataList[id=Crazy_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Targets indiscriminately; Clash Power +1, and gain 2 Damage Up
   PL: - Panika\n- Atakuje bez rozeznania; Moc Starcia +1, zyskuje 2 Wzrosty Obrażeń
18. [Słowo kluczowe [Suicide_LowMorale] — nazwa] 자살
   źródło: BattleKeywords.json :: dataList[id=Suicide_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Suicide_LowMorale]`
   limit: do 40 znaków
   EN: Suicidal
   PL: Samobójstwo
19. [Słowo kluczowe [Suicide_LowMorale] — opis] - 사기 저하\n- 첫 사기저하 상태였을 때, 행동 불가 상태.
   źródło: BattleKeywords.json :: dataList[id=Suicide_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- When at low morale for the first time, become unable to act
   PL: - Spadek Moralu\n- Przy pierwszym Spadku Moralu nie może podejmować działań
20. [Słowo kluczowe [Suicide_Panic] — nazwa] 자살
   źródło: BattleKeywords.json :: dataList[id=Suicide_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Suicide_Panic]`
   (powtórzenie elementu 18 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
21. [Słowo kluczowe [Suicide_Panic] — opis] - 패닉\n- 3턴 간 행동불가 상태. 턴 시작 시 죽음. 모든 아군 고정 정신력 -10
   źródło: BattleKeywords.json :: dataList[id=Suicide_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Cannot act for 3 turns. Unit dies at turn start; all its allies lose 10 SP
   PL: - Panika\n- Nie może działać przez 3 tury. Umiera na początku tury; wszyscy sojusznicy tracą 10 Poczytalności
22. [Słowo kluczowe [Prowl_LowMorale] — nazwa] 배회
   źródło: BattleKeywords.json :: dataList[id=Prowl_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Prowl_LowMorale]`
   limit: do 40 znaków
   EN: Wandering
   PL: Błąkanie
23. [Słowo kluczowe [Prowl_LowMorale] — opis] - 사기 저하\n- 턴 종료 시 아군에게 정신력 2 피해
   źródło: BattleKeywords.json :: dataList[id=Prowl_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn End: Deal 2 SP damage to allies
   PL: - Spadek Moralu\n- Na koniec tury zadaje sojusznikom 2 obrażeń Poczytalności
24. [Słowo kluczowe [Prowl_Panic] — nazwa] 배회
   źródło: BattleKeywords.json :: dataList[id=Prowl_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Prowl_Panic]`
   (powtórzenie elementu 22 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
25. [Słowo kluczowe [Prowl_Panic] — opis] - 패닉\n- 3턴 간 턴 종료 시 아군에게 정신력 5 피해. 3턴 종료 시 도주
   źródło: BattleKeywords.json :: dataList[id=Prowl_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn End: Deal 5 SP damage to allies. Flees from battle after 3 turns have passed
   PL: - Panika\n- Przez 3 tury na koniec tury zadaje sojusznikom 5 obrażeń Poczytalności. Po 3 turach ucieka z walki
26. [Słowo kluczowe [Blue_LowMorale] — nazwa] 우울
   źródło: BattleKeywords.json :: dataList[id=Blue_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Blue_LowMorale]`
   limit: do 40 znaków
   EN: Dejection
   PL: Przygnębienie
27. [Słowo kluczowe [Blue_LowMorale] — opis] - 사기 저하\n- 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 대상의 합 위력 -1
   źródło: BattleKeywords.json :: dataList[id=Blue_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- In a clash, if any Coin lands tails, Clash Power -1 for the clash
   PL: - Spadek Moralu\n- Jeśli w Starciu któraś moneta wypadła rewersem, Moc Starcia celu maleje w tym Starciu o 1
28. [Słowo kluczowe [Blue_Panic] — nazwa] 우울
   źródło: BattleKeywords.json :: dataList[id=Blue_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Blue_Panic]`
   (powtórzenie elementu 26 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
29. [Słowo kluczowe [Blue_Panic] — opis] - 패닉\n- 합 중 코인이 한 번이라도 뒷면이라면, 해당 합 동안 대상의 합 위력 -3
   źródło: BattleKeywords.json :: dataList[id=Blue_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- In a clash, if any Coin lands tails, Clash Power -3 for the clash
   PL: - Panika\n- Jeśli w Starciu któraś moneta wypadła rewersem, Moc Starcia celu maleje w tym Starciu o 3
30. [Słowo kluczowe [DongbaekGrow] — nazwa] 성장
   źródło: BattleKeywords.json :: dataList[id=DongbaekGrow].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekGrow]`
   limit: do 40 znaków
   EN: Growing
   PL: Wzrost
31. [Słowo kluczowe [DongbaekGrow] — opis] 턴 종료 시 수치가 1 증가하고, 수치에 비례하여 최대 체력이 증가한다. (최대 3)
   źródło: BattleKeywords.json :: dataList[id=DongbaekGrow].desc
   limit: do 120 znaków
   EN: At the end of the turn, add +1 Count, and gain Max HP proportional to the Count. (Max 3)
   PL: Na koniec tury wartość rośnie o 1, a Maks. HP rośnie proporcjonalnie do wartości. (maks. 3)
32. [Słowo kluczowe [DongbaekGrow] — podsumowanie] 턴 종료 시 수치가 1 증가하고, 수치에 비례하여 최대 체력이 증가한다. (최대 3)
   źródło: BattleKeywords.json :: dataList[id=DongbaekGrow].summary
   (powtórzenie elementu 31 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
33. [Słowo kluczowe [DongbaekFlorescence] — nazwa] 개화
   źródło: BattleKeywords.json :: dataList[id=DongbaekFlorescence].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekFlorescence]`
   limit: do 40 znaków
   EN: Blooming
   PL: Zakwitanie
34. [Słowo kluczowe [DongbaekFlorescence] — opis] 턴 종료 시 수치가 5 이상이면, 최대 체력의 (수치)%만큼 나태 속성 피해를 받고 만개 상태가 됨\n수치가 5 미만이면, (수치x5)만큼 정신력 피해를 받고, 수치가 1 감소함
   źródło: BattleKeywords.json :: dataList[id=DongbaekFlorescence].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: At 5+ Count, take Sloth damage by (Count)% of Max HP, and become Fully Bloomed\nAt less than 5 Count, lose (Count * 5) SP, then reduce Count by 1
   PL: Na koniec tury, przy wartości 5+, otrzymuje obrażenia Lenistwem równe (wartość)% Maks. HP i przechodzi w stan Pełnego Rozkwitu\nPoniżej 5 traci (wartość x 5) Poczytalności, a wartość maleje o 1
35. [Słowo kluczowe [DongbaekFullBloom] — nazwa] 만개
   źródło: BattleKeywords.json :: dataList[id=DongbaekFullBloom].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekFullBloom]`
   limit: do 40 znaków
   EN: Fully Bloomed
   PL: Pełen Rozkwit
36. [Słowo kluczowe [DongbaekFullBloom] — opis] 행동 불가\n턴 종료 시 정신력 -20. 정신력이 -45가 된 경우 정신력을 최대로 회복하고, 다음 턴에 아찔한 정신 상태가 됨\n2턴 동안 해제되지 않으면, 턴 종료 시 상태 해제
   źródło: BattleKeywords.json :: dataList[id=DongbaekFullBloom].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Cannot act\nAt the end of the turn, lose 20 SP; if SP reaches -45, fully heal SP, then gain 'Dazzled Mind' next turn.\nIf this effect isn't removed for 2 turns, remove it at the end of the turn.
   PL: Nie może działać\nNa koniec tury traci 20 Poczytalności; przy Poczytalności -45 regeneruje ją w pełni, a w następnej turze wpada w stan Oszalałego Umysłu\nJeśli efekt nie zostanie zdjęty przez 2 tury, znika na koniec tury
37. [Słowo kluczowe [DongbaekFascination] — nazwa] 아찔한 정신
   źródło: BattleKeywords.json :: dataList[id=DongbaekFascination].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekFascination]`
   limit: do 40 znaków
   EN: Dazzled Mind
   PL: Oszalały Umysł
38. [Słowo kluczowe [DongbaekFascination] — opis] 이번 턴 동안 아군을 공격함\n흐트러짐 상태가 되면 다음 턴 시작 시 상태 해제\n2턴 동안 해제되지 않으면, 턴 종료 시 정신력이 30 감소하고, 상태 해제
   źródło: BattleKeywords.json :: dataList[id=DongbaekFascination].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Targets allies for attacks\nWhen staggered, remove this effect next turn.\nIf this effect isn't removed for 2 turns, lose 30 SP and remove it at the end of the turn.
   PL: W tej turze atakuje sojuszników\nPo oszołomieniu efekt znika na początku następnej tury\nJeśli nie zostanie zdjęty przez 2 tury, na koniec tury traci 30 Poczytalności i znika
39. [Słowo kluczowe [DongbaekShowdown] — nazwa] 대결
   źródło: BattleKeywords.json :: dataList[id=DongbaekShowdown].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekShowdown]`
   limit: do 40 znaków
   EN: Dueling
   PL: Konfrontacja
40. [Słowo kluczowe [DongbaekShowdown] — opis] 턴 시작 시 이 효과를 보유하지 않은 대상이 만개 상태가 됨.\n보유한 캐릭터가 이상이면, 동백이 공격 위력 증가 1을 얻음
   źródło: BattleKeywords.json :: dataList[id=DongbaekShowdown].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: Units without this status go into a 'Fully Bloomed' status\nIf Yi Sang has this effect, Dongbaek gains 1 Attack Power Up
   PL: Na początku tury cele bez tego efektu przechodzą w stan Pełnego Rozkwitu.\nJeśli ma go Yi Sang, Dongbaek zyskuje 1 Wzrost Mocy Ataku
41. [Słowo kluczowe [DongbaekScatterPetal] — nazwa] 흩어지는 꽃잎
   źródło: BattleKeywords.json :: dataList[id=DongbaekScatterPetal].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekScatterPetal]`
   limit: do 40 znaków
   EN: Scattering Petals
   PL: Rozsypujące się Płatki
42. [Słowo kluczowe [DongbaekScatterPetal] — opis] 턴 종료 시 수치가 6 이상이면 흐트러짐 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=DongbaekScatterPetal].desc
   limit: do 120 znaków
   EN: Turn End: At 6+ Count, become staggered
   PL: Na koniec tury, przy wartości 6 lub wyższej, zostaje oszołomiony
43. [Słowo kluczowe [Thorn] — nazwa] 가시
   źródło: BattleKeywords.json :: dataList[id=Thorn].name
   kontekst: identyfikator tagu w tekstach: `[Thorn]`
   limit: do 40 znaków
   EN: Thorns
   PL: Ciernie
44. [Słowo kluczowe [Thorn] — opis] 피격 시 자신이 받은 피해량의 50%를 공격자에게 돌려줌
   źródło: BattleKeywords.json :: dataList[id=Thorn].desc
   limit: do 120 znaków
   EN: When hit, return 50% of the damage taken to the attacker
   PL: Przy trafieniu oddaje atakującemu 50% otrzymanych obrażeń
45. [Słowo kluczowe [Thorn] — podsumowanie] 받은 피해의 50%를 공격자에게 입힘
   źródło: BattleKeywords.json :: dataList[id=Thorn].summary
   limit: do 120 znaków
   EN: Deal 50% of damage taken to attacker
   PL: Zadaje atakującemu 50% otrzymanych obrażeń
46. [Słowo kluczowe [Fragile_Mind_LowMorale] — nazwa] 위태로운 마음
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Fragile_Mind_LowMorale]`
   limit: do 40 znaków
   EN: Perilous Heart
   PL: Chwiejne Serce
47. [Słowo kluczowe [Fragile_Mind_LowMorale] — opis] 턴 시작 시 공격 위력 증가 2 , 속박 3 얻음
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Attack Power Up and 3 Bind
   PL: Na początku tury zyskuje 2 Wzrosty Mocy Ataku i 3 Spętań
48. [Słowo kluczowe [Fragile_Mind_LowMorale] — podsumowanie] 턴 시작 시 공격 위력 증가 2 , 속박 3 얻음
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_LowMorale].summary
   (powtórzenie elementu 47 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
49. [Słowo kluczowe [Fragile_Mind_Panic] — nazwa] 흐트러진 마음
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Fragile_Mind_Panic]`
   limit: do 40 znaków
   EN: Faltering Heart
   PL: Roztrzęsione Serce
50. [Słowo kluczowe [Fragile_Mind_Panic] — opis] 패닉 상태면 흐트러짐 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_Panic].desc
   limit: do 120 znaków
   EN: In panic, become staggered.
   PL: W stanie Paniki zostaje oszołomiony
51. [Słowo kluczowe [Fragile_Mind_Panic] — podsumowanie] 패닉 상태면 흐트러짐 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=Fragile_Mind_Panic].summary
   (powtórzenie elementu 50 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
52. [Słowo kluczowe [ErodingMind] — nazwa] 침식되는 마음
   źródło: BattleKeywords.json :: dataList[id=ErodingMind].name
   kontekst: identyfikator tagu w tekstach: `[ErodingMind]`
   limit: do 40 znaków
   EN: Corroding Heart
   PL: Korodujące Serce
53. [Słowo kluczowe [ErodingMind] — opis] 턴 시작 시 공격 위력 감소 2, 취약 2, 속박 5를 얻음
   źródło: BattleKeywords.json :: dataList[id=ErodingMind].desc
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Attack Power Down, 2 Fragile, and 5 Bind
   PL: Na początku tury zyskuje 2 Spadki Mocy Ataku, 2 Wrażliwości i 5 Spętań
54. [Słowo kluczowe [ErodingMind] — podsumowanie] 턴 시작 시 공격 위력 감소 2, 취약 2, 속박 5를 얻음
   źródło: BattleKeywords.json :: dataList[id=ErodingMind].summary
   (powtórzenie elementu 53 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
55. [Słowo kluczowe [CrimsonResultUp] — nazwa] 분노 위력 증가
   źródło: BattleKeywords.json :: dataList[id=CrimsonResultUp].name
   kontekst: identyfikator tagu w tekstach: `[CrimsonResultUp]`
   limit: do 40 znaków
   EN: Wrath Power Up
   PL: Wzrost Mocy Gniewu
56. [Słowo kluczowe [CrimsonResultUp] — opis] 한 턴 동안 분노 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=CrimsonResultUp].desc
   limit: do 120 znaków
   EN: Wrath skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Gniewu rośnie o wartość efektu
57. [Słowo kluczowe [EmittedCurrent] — nazwa] 방출 전류
   źródło: BattleKeywords.json :: dataList[id=EmittedCurrent].name
   kontekst: identyfikator tagu w tekstach: `[EmittedCurrent]`
   limit: do 40 znaków
   EN: Spark Discharge
   PL: Wyładowanie Prądu
58. [Słowo kluczowe [EmittedCurrent] — opis] 피격 시 공격자의 충전 횟수 1 증가. 우울 속성으로 피격 시 자신의 파열 횟수 1 증가. 이후 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=EmittedCurrent].desc
   limit: do 160 znaków
   EN: When hit, the attacker gains +1 Charge Count; when hit with a Gloom attack, gain +1 Rupture Count, then reduce Count by 1
   PL: Przy trafieniu atakujący zyskuje +1 Licznika Ładowania; przy trafieniu atakiem Posępności zyskuje +1 Licznika Rozdarcia, po czym wartość maleje o 1
59. [Słowo kluczowe [DistortedDongrangRadiantVanity] — nazwa] 빛나는 허영
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangRadiantVanity].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangRadiantVanity]`
   limit: do 40 znaków
   EN: Radiant Vanity
   PL: Jaśniejąca Próżność
60. [Słowo kluczowe [DistortedDongrangRadiantVanity] — opis] 턴 시작 시 동랑에게 보호 1, 공격 위력 증가 1 부여
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangRadiantVanity].desc
   limit: do 120 znaków
   EN: At the start of the turn, Dongrang gains 1 Protection and 1 Attack Power Up.
   PL: Na początku tury Dongrang zyskuje 1 Ochrony i 1 Wzrost Mocy Ataku
61. [Słowo kluczowe [DistortedDongrangEmptyMark] — nazwa] 텅 빈 징표
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptyMark].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangEmptyMark]`
   limit: do 40 znaków
   EN: Empty Mark
   PL: Pusty Ślad
62. [Słowo kluczowe [DistortedDongrangEmptyMark] — opis] 동랑의 타겟이 됨. 매 턴 시작 시 속박 2를 얻고, 동랑에게 받는 피해량 +50%
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptyMark].desc
   limit: do 120 znaków
   EN: Targeted by Dongrang. Gain 2 Bind every turn, and take +50% damage from Dongrang.
   PL: Staje się celem Dongranga. Na początku każdej tury zyskuje 2 Spętań i otrzymuje +50% obrażeń od Dongranga
63. [Słowo kluczowe [DistortedDongrangEarnestAchievement] — nazwa] 간절한 성과
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEarnestAchievement].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangEarnestAchievement]`
   limit: do 40 znaków
   EN: Earnest Accomplishment
   PL: Gorliwy Dorobek
64. [Słowo kluczowe [DistortedDongrangEarnestAchievement] — opis] 이 유닛의 체력을 1로 만들거나, 처치하면 공격자가 강화 효과를 얻음
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEarnestAchievement].desc
   limit: do 120 znaków
   EN: If this unit is defeated or its HP is brought to 1, the attacker gains buffs.
   PL: Gdy ta jednostka zostaje pokonana lub jej HP spada do 1, atakujący zyskuje wzmocnienie
65. [Słowo kluczowe [DistortedDongrangEmptyHonor] — nazwa] 공허한 영예
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptyHonor].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangEmptyHonor]`
   limit: do 40 znaków
   EN: Empty Honor
   PL: Pusta Chwała
66. [Słowo kluczowe [DistortedDongrangEmptyHonor] — opis] 동랑이 이 유닛을 처치하면, 체력을 잃은 뒤 공허함 1을 얻고 다음 턴에 약화됨
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptyHonor].desc
   limit: do 120 znaków
   EN: If Dongrang defeats this unit, he loses HP, gains 1 Emptiness, and is weakened next turn.
   PL: Gdy Dongrang pokona tę jednostkę, traci HP, zyskuje 1 Pustki i w następnej turze zostaje osłabiony
67. [Słowo kluczowe [DistortedDongrangMomentaryGlory] — nazwa] 찰나의 영광
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangMomentaryGlory].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangMomentaryGlory]`
   limit: do 40 znaków
   EN: Momentary Glory
   PL: Chwalebna Chwila
68. [Słowo kluczowe [DistortedDongrangMomentaryGlory] — opis] 수치가 3 이상이면 동랑이 강화 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangMomentaryGlory].desc
   limit: do 120 znaków
   EN: At 3+ Count, Dongrang becomes more powerful.
   PL: Przy wartości 3 lub wyższej Dongrang zostaje wzmocniony
69. [Słowo kluczowe [DistortedDongrangEmptiness] — nazwa] 공허함
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptiness].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangEmptiness]`
   limit: do 40 znaków
   EN: Emptiness
   PL: Pustka
70. [Słowo kluczowe [DistortedDongrangEmptiness] — opis] 수치가 4 이상이면 동랑이 흐트러짐 상태가 됨
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangEmptiness].desc
   limit: do 120 znaków
   EN: At 4+ Count, Dongrang becomes staggered.
   PL: Przy wartości 4 lub wyższej Dongrang zostaje oszołomiony
71. [Słowo kluczowe [DistortedDongrangFruition] — nazwa] 맺힌 결실
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangFruition].name
   kontekst: identyfikator tagu w tekstach: `[DistortedDongrangFruition]`
   limit: do 40 znaków
   EN: Borne Fruition
   PL: Dojrzały Owoc
72. [Słowo kluczowe [DistortedDongrangFruition] — opis] 이 유닛을 처치한 대상은 체력을 회복하고, 다음 턴에 신속 1, 공격 위력 증가 1을 얻음
   źródło: BattleKeywords.json :: dataList[id=DistortedDongrangFruition].desc
   limit: do 120 znaków
   EN: The unit that defeated this unit heals HP, and gains 1 Haste and 1 Attack Power Up next turn
   PL: Jednostka, która pokonała tę jednostkę, leczy HP, a w następnej turze zyskuje 1 Pośpiechu i 1 Wzrost Mocy Ataku
73. [Słowo kluczowe [EgoAwakenDongrangRadiantDesire] — nazwa] 빛나는 욕망
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangRadiantDesire].name
   kontekst: identyfikator tagu w tekstach: `[EgoAwakenDongrangRadiantDesire]`
   limit: do 40 znaków
   EN: Radiant Desire
   PL: Jaśniejące Pożądanie
74. [Słowo kluczowe [EgoAwakenDongrangRadiantDesire] — opis] 동랑이 턴 시작 시 피해량 증가, 보호 1을 얻음
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangRadiantDesire].desc
   limit: do 120 znaków
   EN: Turn Start: Dongrang gains 1 Damage Up and 1 Protection.
   PL: Na początku tury Dongrang zyskuje 1 Wzrost Obrażeń i 1 Ochrony
75. [Słowo kluczowe [EgoAwakenDongrangSeed] — nazwa] 씨앗
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangSeed].name
   kontekst: identyfikator tagu w tekstach: `[EgoAwakenDongrangSeed]`
   limit: do 40 znaków
   EN: Seeds
   PL: Nasiona
76. [Słowo kluczowe [EgoAwakenDongrangSeed] — opis] 턴 종료 시 수치가 5 이상이면, 2턴 동안 양분 흡수 상태가 됨. 수치가 5 미만이면 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangSeed].desc
   limit: do 130 znaków
   EN: Turn End: At 5+ Count, gain Nutrient Drain for 2 turns; at less than 5 Count, reduce Count by 1
   PL: Na koniec tury, przy wartości 5+, przechodzi w stan Poboru Substancji na 2 tury; poniżej 5 wartość maleje o 1
77. [Słowo kluczowe [EgoAwakenDongrangTree] — nazwa] 양분 흡수
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangTree].name
   kontekst: identyfikator tagu w tekstach: `[EgoAwakenDongrangTree]`
   limit: do 40 znaków
   EN: Nutrient Drain
   PL: Pobór Substancji
78. [Słowo kluczowe [EgoAwakenDongrangTree] — opis] 매 턴 종료 시 동랑의 체력 10 회복
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangTree].desc
   limit: do 120 znaków
   EN: Turn End: Dongrang heals 10 HP
   PL: Na koniec każdej tury Dongrang leczy 10 HP
79. [Słowo kluczowe [EgoAwakenDongrangOverHeal] — nazwa] 과잉 회복
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangOverHeal].name
   kontekst: identyfikator tagu w tekstach: `[EgoAwakenDongrangOverHeal]`
   limit: do 40 znaków
   EN: Overheal
   PL: Nadmierna Regeneracja
80. [Słowo kluczowe [EgoAwakenDongrangOverHeal] — opis] 동랑이 회복시킨 체력만큼 수치 증가. 수치가 50 이상이 되면 수치만큼 탐식 피해를 주고, 다음 턴에 취약 5 부여 후 효과가 소멸됨.
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangOverHeal].desc
   limit: do 200 znaków
   EN: Count rises by the amount of HP Dongrang caused to heal; at 50+ Count, take Gluttony damage by the effect's Count, gain 5 Fragile, and remove the effect.
   PL: Wartość rośnie o HP wyleczone przez Dongranga; przy wartości 50+ otrzymuje tyle obrażeń Obżarstwem, ile wynosi wartość, a w następnej turze 5 Wrażliwości, po czym efekt znika.
81. [Słowo kluczowe [SinkingSurge] — nazwa] 침잠쇄도
   źródło: BattleKeywords.json :: dataList[id=SinkingSurge].name
   kontekst: identyfikator tagu w tekstach: `[SinkingSurge]`
   limit: do 40 znaków
   EN: Sinking Deluge
   PL: Powódź Zatonięcia
82. [Słowo kluczowe [SinkingSurge] — opis] (침잠 횟수 x 침잠 위력)만큼 정신 피해를 주고, 침잠 제거\n대상의 정신력이 -45 이하면 초과된 정신 피해를 우울 속성 피해로 가함.\n(정신력이 없는 대상에게는 전부 우울 속성 피해로 적용됨)
   źródło: BattleKeywords.json :: dataList[id=SinkingSurge].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal SP damage by (Sinking Count * Sinking Potency), then remove Sinking\nIf target's SP is -45 or lower, the excess SP damage is dealt as Gloom-affinity HP damage\n(Non-SP Units take all of it as Gloom HP damage)
   PL: Zadaje (Licznik Zatonięcia x Moc Zatonięcia) obrażeń Poczytalności i usuwa Zatonięcie\nJeśli Poczytalność celu wynosi -45 lub mniej, nadwyżka obrażeń Poczytalności trafia jako obrażenia Posępnością\n(Jednostki bez Poczytalności otrzymują całość jako obrażenia Posępnością)
83. [Słowo kluczowe [AmberResultUp] — nazwa] 나태 위력 증가
   źródło: BattleKeywords.json :: dataList[id=AmberResultUp].name
   kontekst: identyfikator tagu w tekstach: `[AmberResultUp]`
   limit: do 40 znaków
   EN: Sloth Power Up
   PL: Wzrost Mocy Lenistwa
84. [Słowo kluczowe [AmberResultUp] — opis] 한 턴 동안 나태 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=AmberResultUp].desc
   limit: do 120 znaków
   EN: Sloth skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Lenistwa rośnie o wartość efektu
85. [Słowo kluczowe [AmberResultUp] — podsumowanie] 나태 속성 스킬의 최종 위력 +{0}
   źródło: BattleKeywords.json :: dataList[id=AmberResultUp].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Sloth Skill Final Power +{0}
   PL: Moc Końcowa Umiejętności Lenistwa +{0}
86. [Słowo kluczowe [Blue] — nazwa] 눈물
   źródło: BattleKeywords.json :: dataList[id=Blue].name
   kontekst: identyfikator tagu w tekstach: `[Blue]`
   limit: do 40 znaków
   EN: Tears
   PL: Łzy
87. [Słowo kluczowe [Blue] — opis] 턴 종료 시, 자신의 정신력 5 감소.\n뒷면 적중 시 침잠 2 부여
   źródło: BattleKeywords.json :: dataList[id=Blue].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Lose 5 SP\nTails Coins inflict 2 Sinking
   PL: Na koniec tury traci 5 Poczytalności.\nMonety rewersu nadają 2 Zatonięcia
88. [Słowo kluczowe [EgoAwakenDongrangTreeDisplay] — nazwa] 양분 흡수
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangTreeDisplay].name
   kontekst: identyfikator tagu w tekstach: `[EgoAwakenDongrangTreeDisplay]`
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
89. [Słowo kluczowe [EgoAwakenDongrangTreeDisplay] — opis] 매 턴 종료 시 동랑의 체력 10 회복
   źródło: BattleKeywords.json :: dataList[id=EgoAwakenDongrangTreeDisplay].desc
   (powtórzenie elementu 78 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
90. [Słowo kluczowe [DongbaekFullBloomDisplay] — nazwa] 만개
   źródło: BattleKeywords.json :: dataList[id=DongbaekFullBloomDisplay].name
   kontekst: identyfikator tagu w tekstach: `[DongbaekFullBloomDisplay]`
   (powtórzenie elementu 35 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Słowo kluczowe [DongbaekFullBloomDisplay] — opis] 행동 불가\n턴 종료 시 정신력 -20. 정신력이 -45가 된 경우 정신력을 최대로 회복하고, 다음 턴에 아찔한 정신 상태가 됨\n2턴 동안 해제되지 않으면, 턴 종료 시 상태 해제
   źródło: BattleKeywords.json :: dataList[id=DongbaekFullBloomDisplay].desc
   (powtórzenie elementu 36 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
92. [Słowo kluczowe [TakeHpHealIncrease] — nazwa] 체력 회복 증가
   źródło: BattleKeywords.json :: dataList[id=TakeHpHealIncrease].name
   kontekst: identyfikator tagu w tekstach: `[TakeHpHealIncrease]`
   limit: do 40 znaków
   EN: HP Healing Boost
   PL: Wzrost Leczenia HP
93. [Słowo kluczowe [TakeHpHealIncrease] — opis] 패시브, 스킬, 코인의 효과로 회복하는 체력이 수치에 비례하여 증가 (최대 5)
   źródło: BattleKeywords.json :: dataList[id=TakeHpHealIncrease].desc
   limit: do 150 znaków
   EN: HP healed by Passives, Skill effects, or Coin effects increases proportionally to the value of this effect. (Max 5)
   PL: HP leczone pasywami, Umiejętnościami lub monetami rośnie proporcjonalnie do wartości efektu (maks. 5)
94. [Słowo kluczowe [SkillPowerUp] — nazwa] 기본 위력 증가
   źródło: BattleKeywords.json :: dataList[id=SkillPowerUp].name
   kontekst: identyfikator tagu w tekstach: `[SkillPowerUp]`
   limit: do 40 znaków
   EN: Base Power Up
   PL: Wzrost Mocy Bazowej
95. [Słowo kluczowe [SkillPowerUp] — opis] 스킬 기본 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=SkillPowerUp].desc
   limit: do 120 znaków
   EN: Raise the Base Power of Skills by the effect's Count.
   PL: Moc Bazowa Umiejętności rośnie o wartość efektu
96. [Słowo kluczowe [MaxHpMultiplier] — nazwa] 최대 체력 증가
   źródło: BattleKeywords.json :: dataList[id=MaxHpMultiplier].name
   kontekst: identyfikator tagu w tekstach: `[MaxHpMultiplier]`
   limit: do 40 znaków
   EN: Max HP Up
   PL: Wzrost Maks. HP
97. [Słowo kluczowe [MaxHpMultiplier] — opis] 최대 체력이 수치당 10% 증가
   źródło: BattleKeywords.json :: dataList[id=MaxHpMultiplier].desc
   limit: do 120 znaków
   EN: Raise the Max HP by 10% per Count.
   PL: Maks. HP rośnie o 10% za każdą wartość
98. [Słowo kluczowe [KCorpSerum] — nazwa] K사 앰플
   źródło: BattleKeywords.json :: dataList[id=KCorpSerum].name
   kontekst: identyfikator tagu w tekstach: `[KCorpSerum]`
   limit: do 40 znaków
   EN: K Corp Ampule
   PL: Ampułka Korporacji K
99. [Słowo kluczowe [KCorpSerum] — opis] 턴 시작 시 4 미만이면, 최대 체력의 (수치 X 5) %만큼 체력 회복.\n수치가 4 이상이면, 사망
   źródło: BattleKeywords.json :: dataList[id=KCorpSerum].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn Start: At less than 4 Count, heal by (Count * 5)% of Max HP\nAt 4+ Count, the unit dies
   PL: Na początku tury, przy wartości poniżej 4, leczy (wartość x 5)% Maks. HP.\nPrzy wartości 4 lub wyższej umiera
100. [Słowo kluczowe [Talisman] — nazwa] 부적
   źródło: BattleKeywords.json :: dataList[id=Talisman].name
   kontekst: identyfikator tagu w tekstach: `[Talisman]`
   limit: do 40 znaków
   EN: Talisman
   PL: Talizman
101. [Słowo kluczowe [Talisman] — opis] 최댓값 : 6\n- 공격 적중 시 대상의 파열 횟수를 1 소모하여 (수치/2)만큼 파열 부여 (파열 횟수를 소모한 경우 최소 1 부여. 소수점 버림)\n- 피격 시 (수치/2)만큼 파열을 얻고 수치 1 감소 (최소 1 얻음, 소수점 버림)\n- 턴 종료 시 수치가 6 이상이면, 부적을 전부 소모하고 수치만큼 고정 피해를 받음
   źródło: BattleKeywords.json :: dataList[id=Talisman].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 6\nOn Hit, consume 1 Rupture Count on target to inflict (Stack / 2) Rupture (inflicts at least 1 Rupture if Rupture Count was consumed; rounded down)\nWhen hit, gain (Stack / 2) Rupture and lose 1 Stack (gain at least 1 Rupture; rounded down)\nTurn End: at 6+ Stack, remove all Talisman on self and take fixed damage by Stack
   PL: Maks.: 6\n- Przy trafieniu atakiem zużywa 1 Licznika Rozdarcia celu, by nadać (wartość/2) Rozdarcia (przy zużytym Liczniku nadaje co najmniej 1; zaokrąglone w dół)\n- Przy trafieniu zyskuje (wartość/2) Rozdarcia, a wartość maleje o 1 (co najmniej 1; zaokrąglone w dół)\n- Na koniec tury, przy wartości 6 lub wyższej, zużywa wszystkie Talizmany i otrzymuje obrażenia stałe równe wartości
102. [Słowo kluczowe [Talisman] — podsumowanie] 공격 적중 시 파열 횟수를 소모하여 파열 부여, 피격 시 파열 얻고 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=Talisman].summary
   limit: do 130 znaków
   EN: On Hit, consume Rupture Count on target to inflict Rupture; when hit, gain Rupture and lose 1 Stack
   PL: Przy trafieniu zużywa Licznik Rozdarcia celu, by nadać Rozdarcie; przy trafieniu zyskuje Rozdarcie, a wartość maleje o 1
103. [Słowo kluczowe [Choice_90104001] — nazwa] 이해
   źródło: BattleKeywords.json :: dataList[id=Choice_90104001].name
   kontekst: identyfikator tagu w tekstach: `[Choice_90104001]`
   limit: do 40 znaków
   EN: Understanding
   PL: Zrozumienie
104. [Słowo kluczowe [Choice_90104001] — opis] 이번 전투 시작 시 모든 속성의 E.G.O 자원+2
   źródło: BattleKeywords.json :: dataList[id=Choice_90104001].desc
   limit: do 120 znaków
   EN: At the start of the battle, gain 2 E.G.O resources for every Affinity.
   PL: Na początku tej walki +2 zasobów E.G.O każdego atrybutu
105. [Słowo kluczowe [Choice_90104001] — podsumowanie] 모든 속성 E.G.O 자원 +2
   źródło: BattleKeywords.json :: dataList[id=Choice_90104001].summary
   limit: do 120 znaków
   EN: Gain +2 E.G.O resource for all Affinities
   PL: Zasoby E.G.O wszystkich atrybutów +2
106. [Słowo kluczowe [Choice_9010400101] — nazwa] 각오
   źródło: BattleKeywords.json :: dataList[id=Choice_9010400101].name
   kontekst: identyfikator tagu w tekstach: `[Choice_9010400101]`
   limit: do 40 znaków
   EN: Determined
   PL: Postanowienie
107. [Słowo kluczowe [Choice_9010400101] — opis] 이번 전투 동안 모든 인격이 최종 스킬 위력 +2
   źródło: BattleKeywords.json :: dataList[id=Choice_9010400101].desc
   limit: do 120 znaków
   EN: All Ally Units gain +2 Skill Final Power for this battle
   PL: W tej walce wszystkie osobowości zyskują Moc Końcową Umiejętności +2
108. [Słowo kluczowe [Choice_9010400101] — podsumowanie] 최종 스킬 위력 +2
   źródło: BattleKeywords.json :: dataList[id=Choice_9010400101].summary
   limit: do 120 znaków
   EN: Skill Final Power +2
   PL: Moc Końcowa Umiejętności +2
109. [Słowo kluczowe [Choice_90104002] — nazwa] 회모
   źródło: BattleKeywords.json :: dataList[id=Choice_90104002].name
   kontekst: identyfikator tagu w tekstach: `[Choice_90104002]`
   limit: do 40 znaków
   EN: Longing
   PL: Tęsknota
110. [Słowo kluczowe [Choice_90104002] — opis] 이번 전투 동안 모든 인격이 스킬 위력 +1
   źródło: BattleKeywords.json :: dataList[id=Choice_90104002].desc
   limit: do 120 znaków
   EN: All Ally Units gain +1 Skill Power for this battle
   PL: W tej walce wszystkie osobowości zyskują Moc Umiejętności +1
111. [Słowo kluczowe [Choice_90104002] — podsumowanie] 스킬 위력 +1
   źródło: BattleKeywords.json :: dataList[id=Choice_90104002].summary
   limit: do 120 znaków
   EN: Skill Power +1
   PL: Moc Umiejętności +1
112. [Słowo kluczowe [MentalSystemResultIncrease_Typo] — nazwa] 정신력 회복 효율
   źródło: BattleKeywords.json :: dataList[id=MentalSystemResultIncrease_Typo].name
   kontekst: identyfikator tagu w tekstach: `[MentalSystemResultIncrease_Typo]`
   limit: do 40 znaków
   EN: SP Heal Efficiency
   PL: Wydajność Leczenia Poczytalności
113. [Słowo kluczowe [MentalSystemResultIncrease_Typo] — opis] 인격의 기본 정신력 증가 조건에 의한 정신력 회복량
   źródło: BattleKeywords.json :: dataList[id=MentalSystemResultIncrease_Typo].desc
   limit: do 120 znaków
   EN: Amount of SP healed due to the Identity's 'Base factors increasing Sanity(SP)'
   PL: Ilość regenerowanej Poczytalności z warunków bazowych zwiększających Poczytalność osobowości
114. [Słowo kluczowe [MentalSystemResultDecrease_Typo] — nazwa] 정신력 감소 효율
   źródło: BattleKeywords.json :: dataList[id=MentalSystemResultDecrease_Typo].name
   kontekst: identyfikator tagu w tekstach: `[MentalSystemResultDecrease_Typo]`
   limit: do 40 znaków
   EN: SP Loss Efficiency
   PL: Wydajność Spadku Poczytalności
115. [Słowo kluczowe [MentalSystemResultDecrease_Typo] — opis] 인격의 기본 정신력 감소 조건에 의한 정신력 감소량
   źródło: BattleKeywords.json :: dataList[id=MentalSystemResultDecrease_Typo].desc
   limit: do 120 znaków
   EN: Amount of SP lost due to the Identity's 'Base factors decreasing Sanity(SP)'
   PL: Ilość traconej Poczytalności z warunków bazowych zmniejszających Poczytalność osobowości
116. [Słowo kluczowe [DuelDeclaration] — nazwa] 결투 선포
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclaration]`
   limit: do 40 znaków
   EN: Declared Duel
   PL: Wyzwanie na Pojedynek
117. [Słowo kluczowe [DuelDeclaration] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. Replaced when another unit inflicts Declared Duel on the same target.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
118. [Słowo kluczowe [Aggro] — nazwa] 도발치
   źródło: BattleKeywords.json :: dataList[id=Aggro].name
   kontekst: identyfikator tagu w tekstach: `[Aggro]`
   limit: do 40 znaków
   EN: Aggro
   PL: Wartość Prowokacji
119. [Słowo kluczowe [Aggro] — opis] 집중 전투에서 도발치가 높은 슬롯일수록 적에게 공격 받을 확률이 증가함
   źródło: BattleKeywords.json :: dataList[id=Aggro].desc
   limit: do 130 znaków
   EN: In focused encounters, slots with higher Aggro values are more likely to be targeted by enemies.
   PL: W walkach skupionych sloty o wyższej Wartości Prowokacji są częściej atakowane przez wrogów.
120. [Słowo kluczowe [BurstVulnerable] — nazwa] 파열 취약
   źródło: BattleKeywords.json :: dataList[id=BurstVulnerable].name
   kontekst: identyfikator tagu w tekstach: `[BurstVulnerable]`
   limit: do 40 znaków
   EN: Rupture Fragility
   PL: Wrażliwość na Rozdarcie
121. [Słowo kluczowe [BurstVulnerable] — opis] 한 턴 동안 파열 효과로 받는 피해 수치당 1 증가
   źródło: BattleKeywords.json :: dataList[id=BurstVulnerable].desc
   limit: do 120 znaków
   EN: Take +1 damage per Count from Rupture effects for one turn.
   PL: W tej turze otrzymuje +1 obrażeń stałych za każdą wartość od efektów Rozdarcia
122. [Słowo kluczowe [EmergencyFeed] — nazwa] 긴급 영양 보급
   źródło: BattleKeywords.json :: dataList[id=EmergencyFeed].name
   kontekst: identyfikator tagu w tekstach: `[EmergencyFeed]`
   limit: do 40 znaków
   EN: Emergency Nutrient Supply
   PL: Awaryjna Dostawa Substancji
123. [Słowo kluczowe [EmergencyFeed] — opis] 턴 종료 시 총 회복한 양이 자신의 체력 15% 이상이면, 다음 턴에 몸통 부위 회복.
   źródło: BattleKeywords.json :: dataList[id=EmergencyFeed].desc
   limit: do 140 znaków
   EN: At the end of the turn, if this unit has healed 15% of Max HP or more, the body is restored next turn.
   PL: Na koniec tury, jeśli ogół wyleczonych ilości wynosi 15% HP lub więcej, część Tułowia zostaje odtworzona w następnej turze.
124. [Słowo kluczowe [Bullet_Crab] — nazwa] 오래된 게딱지 탄
   źródło: BattleKeywords.json :: dataList[id=Bullet_Crab].name
   kontekst: identyfikator tagu w tekstach: `[Bullet_Crab]`
   limit: do 40 znaków
   EN: Molted Shell Shot
   PL: Pocisk ze Starego Pancerza Kraba
125. [Słowo kluczowe [Bullet_Crab] — opis] 특정 스킬 사용 시 오래된 게딱지 탄이 소모됨
   źródło: BattleKeywords.json :: dataList[id=Bullet_Crab].desc
   limit: do 120 znaków
   EN: Resource used by certain skills for additional effects.
   PL: Zużywany przez określone Umiejętności
126. [Słowo kluczowe [SinkingVulnerable] — nazwa] 침잠 취약
   źródło: BattleKeywords.json :: dataList[id=SinkingVulnerable].name
   kontekst: identyfikator tagu w tekstach: `[SinkingVulnerable]`
   limit: do 40 znaków
   EN: Sinking Fragility
   PL: Wrażliwość na Zatonięcie
127. [Słowo kluczowe [SinkingVulnerable] — opis] 한 턴 동안 침잠 효과로 받는 피해 수치당 1 증가
   źródło: BattleKeywords.json :: dataList[id=SinkingVulnerable].desc
   limit: do 120 znaków
   EN: Take +1 damage per Count from Sinking effects for one turn.
   PL: W tej turze otrzymuje +1 obrażeń stałych za każdą wartość od efektów Zatonięcia
128. [Słowo kluczowe [BurstProtection] — nazwa] 파열 보호
   źródło: BattleKeywords.json :: dataList[id=BurstProtection].name
   kontekst: identyfikator tagu w tekstach: `[BurstProtection]`
   limit: do 40 znaków
   EN: Rupture Protection
   PL: Ochrona przed Rozdarciem
129. [Słowo kluczowe [BurstProtection] — opis] 한 턴 동안 파열 효과로 받는 피해 수치당 1 감소
   źródło: BattleKeywords.json :: dataList[id=BurstProtection].desc
   limit: do 120 znaków
   EN: Take -1 damage per Count from Rupture effects for one turn.
   PL: W tej turze otrzymuje -1 obrażeń stałych za każdą wartość od efektów Rozdarcia
130. [Słowo kluczowe [PseudoLastBoss_KingCrap] — nazwa] 분.게
   źródło: BattleKeywords.json :: dataList[id=PseudoLastBoss_KingCrap].name
   kontekst: identyfikator tagu w tekstach: `[PseudoLastBoss_KingCrap]`
   limit: do 40 znaków
   EN: Crab Rage
   PL: Wściek. Krab
131. [Słowo kluczowe [PseudoLastBoss_KingCrap] — opis] 매 턴 시작 시 자신을 제외한 모든 아군 게에게 공격 위력 증가 1 부여하고, 소라가 파괴되지 않았으면, 보호 2를 얻음.\n스킬 사용시 대상의 정신력 5 감소.\n체력이 50% 미만이 되면 모든 부위가 공격 위력 증가 2, 취약 2를 얻음
   źródło: BattleKeywords.json :: dataList[id=PseudoLastBoss_KingCrap].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: At the start of the turn, apply Attack Power Up to all other allied crabs, and gain 2 Protection if its Shell isn't broken.\n-5 SP to target when using a skill.\nAt 50%- HP, every part gains 2 Attack Power Up and 2 Fragile.
   PL: Na początku każdej tury nadaje 1 Wzrost Mocy Ataku wszystkim sojuszniczym krabom poza sobą, a jeśli Pancerz nie jest rozbity, zyskuje 2 Ochrony.\nPrzy użyciu Umiejętności traci 5 Poczytalności celu.\nPoniżej 50% HP wszystkie części zyskują 2 Wzrosty Mocy Ataku i 2 Wrażliwości
132. [Słowo kluczowe [ChargeForceField] — nazwa] 충전 역장
   źródło: BattleKeywords.json :: dataList[id=ChargeForceField].name
   kontekst: identyfikator tagu w tekstach: `[ChargeForceField]`
   limit: do 40 znaków
   EN: Charge Barrier
   PL: Bariera Ładunku
133. [Słowo kluczowe [ChargeForceField] — opis] - (충전 역장 수치 x 3)만큼 보호막을 얻음\n- (충전 역장 수치 x 3)만큼 보호막을 잃으면, 충전 역장 1 감소\n- (효과가 부여된 대상이 W사 직원이면, 보호막 계수가 3 대신 5로 적용됨)\n- 턴 종료 시 충전 횟수를 충전 역장 수치만큼 얻고, 충전 역장과 충전 역장 효과로 얻는 보호막 소멸.
   źródło: BattleKeywords.json :: dataList[id=ChargeForceField].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain (Charge Barrier # x 3) Shield.\n- Lose 1 Charge Barrier after losing (Charge Barrier # x 3) Shield.\n- (If the unit is a W Corp. employee, ALL Charge Barrier effects activate at (Charge Barrier # x 5) instead of at (Charge Barrier # x 3))\n- Turn End: Gain a Charge Count for each Charge Barrier #, and Charge Barrier and Shield gained from Charge Barrier expire completely next turn
   PL: - Zyskuje Tarczę równą (wartość Bariery Ładunku x 3)\n- Traci 1 Bariery Ładunku po utracie Tarczy równej (wartość Bariery Ładunku x 3)\n- (Jeśli celem jest pracownik Korporacji W, wszystkie efekty Bariery Ładunku działają z mnożnikiem 5 zamiast 3)\n- Na koniec tury zyskuje Licznik Ładowania równy wartości Bariery Ładunku, a Bariera Ładunku i Tarcza z niej znikają w następnej turze
134. [Słowo kluczowe [SlashResultUp] — nazwa] 참격 위력 증가
   źródło: BattleKeywords.json :: dataList[id=SlashResultUp].name
   kontekst: identyfikator tagu w tekstach: `[SlashResultUp]`
   limit: do 40 znaków
   EN: Slash Power Up
   PL: Wzrost Mocy Cięcia
135. [Słowo kluczowe [SlashResultUp] — opis] 한 턴 동안 참격 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=SlashResultUp].desc
   limit: do 120 znaków
   EN: Slash skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Cięcia rośnie o wartość efektu
136. [Słowo kluczowe [Discard] — nazwa] 버림
   źródło: BattleKeywords.json :: dataList[id=Discard].name
   kontekst: identyfikator tagu w tekstach: `[Discard]`
   limit: do 40 znaków
   EN: Discard
   PL: Odrzut
137. [Słowo kluczowe [Discard] — opis] - 명령 페이즈 때 선택 가능한 스킬 중 조건에 맞는 스킬을 패널에서 제거함. (수비, E.G.O 스킬 제외. 버린 스킬은 다음 스킬 목록에서 사라지지 않음)\n- 버려지는 스킬은 버림 관련 효과 외의 스킬, 코인 효과가 발동하지 않으며, 해당 스킬의 E.G.O 자원을 얻지 않음.
   źródło: BattleKeywords.json :: dataList[id=Discard].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Delete Skills that fit the condition and are selectable during the Chaining Phase from the Dashboard. (Defensive & E.G.O Skills do not count. Does not delete the Skill from the upcoming Skills list)\n- Discarded Skills will not activate Skill effects or Coin effects other than effects from Discard, and will not give E.G.O resources.
   PL: - Usuwa z panelu poleceń Umiejętności spełniające warunek, które da się wybrać w fazie łączenia (poza Umiejętnościami obronnymi i E.G.O; odrzucona Umiejętność nie znika z nadchodzącej listy Umiejętności)\n- Odrzucone Umiejętności nie aktywują efektów Umiejętności ani monet poza efektami Odrzutu i nie dają zasobów E.G.O
138. [Słowo kluczowe [KnowledgeExplored] — nazwa] 탐구한 지식
   źródło: BattleKeywords.json :: dataList[id=KnowledgeExplored].name
   kontekst: identyfikator tagu w tekstach: `[KnowledgeExplored]`
   limit: do 40 znaków
   EN: Insight
   PL: Zgłębiona Wiedza
139. [Słowo kluczowe [KnowledgeExplored] — opis] 이 효과를 보유한 캐릭터가 마지막으로 버린 스킬의 등급 (기본값: 1)
   źródło: BattleKeywords.json :: dataList[id=KnowledgeExplored].desc
   limit: do 120 znaków
   EN: The rank of the last Skill Discarded by the unit with this effect (Base Value: 1)
   PL: Ranga ostatniej Umiejętności odrzuconej przez jednostkę z tym efektem (wartość bazowa: 1)
140. [Słowo kluczowe [Unjust_Enrichment] — nazwa] 부당 수익
   źródło: BattleKeywords.json :: dataList[id=Unjust_Enrichment].name
   kontekst: identyfikator tagu w tekstach: `[Unjust_Enrichment]`
   limit: do 40 znaków
   EN: Unjust Enrichment
   PL: Nieprawne Wzbogacenie
141. [Słowo kluczowe [Unjust_Enrichment] — opis] - 출혈이 부여된 대상에게 앞면 적중시 획득 (최대 4)\n- 총알은 비싸다고 패시브의 효과 발동 시 이 버프를 전부 소모하여 추가 피해를 줌
   źródło: BattleKeywords.json :: dataList[id=Unjust_Enrichment].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gained on Heads Hit against targets that have Bleed (Max 4)\n- When 'Bullets are Pricey' Passive activates, consume all Unjust Enrichment stack to deal bonus damage
   PL: - Zyskiwane przy trafieniu atakiem w cel z nadanym Krwawieniem (maks. 4)\n- Po aktywacji pasywu „Amunicja Jest Droga” zużywa wszystkie stosy tego wzmocnienia, by zadać dodatkowe obrażenia
142. [Słowo kluczowe [Resentment] — nazwa] 원한
   źródło: BattleKeywords.json :: dataList[id=Resentment].name
   kontekst: identyfikator tagu w tekstach: `[Resentment]`
   limit: do 40 znaków
   EN: Resentment
   PL: Uraza
143. [Słowo kluczowe [Resentment] — opis] <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">앙갚음 장부</color></link></u>가 부여된 대상에게 공격이 적중한 경우, 공격 종료 시 소멸\n턴 종료 시 남아있으면 소멸
   źródło: BattleKeywords.json :: dataList[id=Resentment].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <sprite name="RetaliationBook">, <color=#e30000>, <u>, <link="RetaliationBook">, </color>, </link>, </u>, \n
   EN: If the enemy with the <sprite name="RetaliationBook"><color=#e30000><link="RetaliationBook">Vengeance Mark</color></link></u> is hit by an attack, this effect expires at Attack End.\nExpires at the end of the turn
   PL: Gdy atak trafi w cel z nadanym <sprite name="RetaliationBook"><color=#e30000><u><link="RetaliationBook">Rejestrem Odwetu</link></u></color>, efekt znika po zakończeniu ataku\nZnika na koniec tury
144. [Słowo kluczowe [RetaliationBook] — nazwa] 앙갚음 대상
   źródło: BattleKeywords.json :: dataList[id=RetaliationBook].name
   kontekst: identyfikator tagu w tekstach: `[RetaliationBook]`
   limit: do 40 znaków
   EN: Vengeance Mark
   PL: Cel Odwetu
145. [Słowo kluczowe [RetaliationBook] — opis] 이전 턴에 아군에게 스킬로 가장 많이 피해를 준 대상에게 부여됨. (최대 1회 부여 가능)
   źródło: BattleKeywords.json :: dataList[id=RetaliationBook].desc
   limit: do 120 znaków
   EN: Applied to the unit that dealt the most damage to an ally (Max 1)
   PL: Nadawany jednostce, która zadała sojusznikowi najwięcej obrażeń w poprzedniej turze (do nadania raz na turę)
146. [Słowo kluczowe [PenetrateResultUp] — nazwa] 관통 위력 증가
   źródło: BattleKeywords.json :: dataList[id=PenetrateResultUp].name
   kontekst: identyfikator tagu w tekstach: `[PenetrateResultUp]`
   limit: do 40 znaków
   EN: Pierce Power Up
   PL: Wzrost Mocy Przebicia
147. [Słowo kluczowe [PenetrateResultUp] — opis] 한 턴 동안 관통 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=PenetrateResultUp].desc
   limit: do 120 znaków
   EN: Pierce skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Przebicia rośnie o wartość efektu
148. [Słowo kluczowe [DuelDeclaration_DonQuixote] — nazwa] 결투 선포 - 돈키호테
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_DonQuixote].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclaration_DonQuixote]`
   limit: do 40 znaków
   EN: Declared Duel - Don Quixote
   PL: Wyzwanie na Pojedynek - Don Kichot
149. [Słowo kluczowe [DuelDeclaration_DonQuixote] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_DonQuixote].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. Replaced when other unit inflicts Declared Duel on the same target.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
150. [Słowo kluczowe [DuelDeclaration_Outis] — nazwa] 결투 선포 - 오티스
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_Outis].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclaration_Outis]`
   limit: do 40 znaków
   EN: Declared Duel - Outis
   PL: Wyzwanie na Pojedynek - Outis
151. [Słowo kluczowe [DuelDeclaration_Outis] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_Outis].desc
   (powtórzenie elementu 149 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Słowo kluczowe [DuelDeclaration_Sinclair] — nazwa] 결투 선포 - 싱클레어
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_Sinclair].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclaration_Sinclair]`
   limit: do 40 znaków
   EN: Declared Duel - Sinclair
   PL: Wyzwanie na Pojedynek - Sinclair
153. [Słowo kluczowe [DuelDeclaration_Sinclair] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1, 공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회) 부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸. 다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords.json :: dataList[id=DuelDeclaration_Sinclair].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit that has the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. Replaced when another unit inflicts Declared Duel on the same target.
   PL: Gdy wystawca Wyzwania na Pojedynek stoczy Starcie z celem, ma +1 Mocy Starcia; przy trafieniu atakiem zyskuje 1 Pośpiechu w następnej turze (do 4 razy na turę). Efekt znika, gdy wystawca wystawi Wyzwanie innemu celowi. Zostaje zastąpione, gdy inna postać wystawi Wyzwanie temu samemu celowi.
154. [Słowo kluczowe [VibrationExplosion] — nazwa] 진동 폭발
   źródło: BattleKeywords.json :: dataList[id=VibrationExplosion].name
   kontekst: identyfikator tagu w tekstach: `[VibrationExplosion]`
   limit: do 40 znaków
   EN: Tremor Burst
   PL: Wybuch Wstrząsu
155. [Słowo kluczowe [VibrationExplosion] — opis] 대상의 진동 위력만큼 흐트러짐 손상을 입힘
   źródło: BattleKeywords.json :: dataList[id=VibrationExplosion].desc
   limit: do 120 znaków
   EN: Raise target's Stagger Threshold by Tremor Potency on target
   PL: Podnosi Próg Oszołomienia celu o Moc Wstrząsu celu
156. [Słowo kluczowe [OneOnOneDuel] — nazwa] 1대1 대결
   źródło: BattleKeywords.json :: dataList[id=OneOnOneDuel].name
   kontekst: identyfikator tagu w tekstach: `[OneOnOneDuel]`
   limit: do 40 znaków
   EN: Single Combat
   PL: Pojedynek Jeden na Jednego
157. [Słowo kluczowe [OneOnOneDuel] — opis] 피격을 당하는 슬롯이 한 유닛에게만 타겟됨. 동시에 피격을 당하는 슬롯의 스킬과 합을 하는 공격 스킬과만 1대1 대결이 성립됨. (단, 스킬 재사용의 경우에는 적용되지 않음)
   źródło: BattleKeywords.json :: dataList[id=OneOnOneDuel].desc
   limit: do 280 znaków
   EN: Established when the attacked Slot is targeted by a single unit, and only by that single unit. This condition is established only between the attacking unit and the attacked Slot. (Does not apply to reused Skills)
   PL: Tworzy się, gdy atakowany slot jest celowany wyłącznie przez jedną jednostkę, i tylko przez tę jednostkę. Stan tworzy się wyłącznie między atakującą jednostką a atakowanym slocie. (Nie dotyczy ponownie używanych Umiejętności)
158. [Słowo kluczowe [FreischutzShotCount] — nazwa] 마탄
   źródło: BattleKeywords.json :: dataList[id=FreischutzShotCount].name
   kontekst: identyfikator tagu w tekstach: `[FreischutzShotCount]`
   limit: do 40 znaków
   EN: Magic Bullet
   PL: Magiczna Amunicja
159. [Słowo kluczowe [FreischutzShotCount] — opis] - 최댓값: 7\n- 특정 스킬 효과에 따라 수치가 변경됨.\n- [로보토미 E.G.O::마탄 오티스 인격 전용 효과]\n· 수치가 증가할수록 스킬 3의 기본 위력, 코인 위력 증가
   źródło: BattleKeywords.json :: dataList[id=FreischutzShotCount].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max: 7\n- Value changes depending on certain Skill effects.\n- [Lobotomy E.G.O::Magic Bullet Outis Only]\n· The higher the value, the higher the Base Power and Coin Power of Skill 3
   PL: - Maks.: 7\n- Wartość zmienia się pod wpływem określonych efektów Umiejętności.\n- [Lobotomy E.G.O::Magiczna Amunicja — tylko dla osobowości Outis]\n· Im wyższa wartość, tym wyższe Moc Bazowa i moc monet Umiejętności 3
160. [Słowo kluczowe [DarkFlame] — nazwa] 흑염
   źródło: BattleKeywords.json :: dataList[id=DarkFlame].name
   kontekst: identyfikator tagu w tekstach: `[DarkFlame]`
   limit: do 40 znaków
   EN: Dark Flame
   PL: Czarny Płomień
161. [Słowo kluczowe [DarkFlame] — opis] - 특수 화상\n- 최댓값: 7\n- 수치만큼 대상의 방어 레벨 감소\n- 턴 종료 시 (수치 x 대상의 화상)만큼 오만 속성 피해를 주고, 효과 소멸
   źródło: BattleKeywords.json :: dataList[id=DarkFlame].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Burn\n- Max Value: 7\n- Target loses Defense Level equal to the value of this effect\n- Turn End: Deal (Value x Burn on target) Pride Affinity damage, then expires
   PL: - Szczególne Podpalenie\n- Maks.: 7\n- Obniża Poziom Obrony celu o wartość efektu\n- Na koniec tury zadaje (wartość x Podpalenie celu) obrażeń Pychą, po czym efekt znika
162. [Słowo kluczowe [CtrlTeamCaptain] — nazwa] 지휘팀 팀장
   źródło: BattleKeywords.json :: dataList[id=CtrlTeamCaptain].name
   kontekst: identyfikator tagu w tekstach: `[CtrlTeamCaptain]`
   limit: do 40 znaków
   EN: Control Team Captain
   PL: Kapitan Zespołu Dowodzenia
163. [Słowo kluczowe [CtrlTeamCaptain] — opis] - 스킬 슬롯 수 +1\n- 스킬 3 수량 +1, 대신 스킬 1 수량 -1\n- 스킬로 적 처치 시 자신을 포함하여 정신력이 가장 낮은 아군 2명 정신력 25 회복, 적을 처치한 스킬 속성의 EGO 자원 +2, 나머지 속성의 EGO 자원 +1
   źródło: BattleKeywords.json :: dataList[id=CtrlTeamCaptain].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Modify Skill pool: Gain 1 use of Skill 3, but lose 1 use of Skill 1\n- When this unit defeats an enemy with a Skill, 2 allies(including this unit) with the least SP heal 25 SP. Gain +2 E.G.O resource to the Affinity of the Skill that defeated the enemy; gain +1 E.G.O resource to rest of the Affinities
   PL: - Liczba slotów Umiejętności +1\n- Modyfikuje pulę Umiejętności: +1 użycie Umiejętności 3, w zamian -1 użycie Umiejętności 1\n- Gdy ta jednostka pokona wroga Umiejętnością, 2 sojusznicy (łącznie z nią) z najniższą Poczytalnością odzyskują 25 Poczytalności; +2 zasobów E.G.O atrybutu Umiejętności, która pokonała wroga, +1 zasobów pozostałych atrybutów
164. [Słowo kluczowe [HeatedGasHarpoon] — nazwa] 가열된 가스 작살
   źródło: BattleKeywords.json :: dataList[id=HeatedGasHarpoon].name
   kontekst: identyfikator tagu w tekstach: `[HeatedGasHarpoon]`
   limit: do 40 znaków
   EN: Heated Gas Harpoon
   PL: Nagrzany Harpun Gazowy
165. [Słowo kluczowe [HeatedGasHarpoon] — opis] 한 턴 동안 공격 앞면 적중 시 화상 1 부여
   źródło: BattleKeywords.json :: dataList[id=HeatedGasHarpoon].desc
   limit: do 120 znaków
   EN: For 1 turn, inflict 1 Burn with Heads Hit
   PL: Przez 1 turę nadaje 1 Podpalenia przy trafieniu awersem
166. [Słowo kluczowe [OverHeatedGasHarpoon] — nazwa] 과열된 가스 작살
   źródło: BattleKeywords.json :: dataList[id=OverHeatedGasHarpoon].name
   kontekst: identyfikator tagu w tekstach: `[OverHeatedGasHarpoon]`
   limit: do 40 znaków
   EN: Overheated Gas Harpoon
   PL: Przegrzany Harpun Gazowy
167. [Słowo kluczowe [OverHeatedGasHarpoon] — opis] 한 턴 동안 공격 적중 시 화상 1 부여
   źródło: BattleKeywords.json :: dataList[id=OverHeatedGasHarpoon].desc
   limit: do 120 znaków
   EN: For 1 turn, inflict 1 Burn On Hit
   PL: Przez 1 turę nadaje 1 Podpalenia przy trafieniu
168. [Słowo kluczowe [CoverAttack] — nazwa] 원호 공격
   źródło: BattleKeywords.json :: dataList[id=CoverAttack].name
   kontekst: identyfikator tagu w tekstach: `[CoverAttack]`
   limit: do 40 znaków
   EN: Assist Attack
   PL: Atak Wsparcia
169. [Słowo kluczowe [CoverAttack] — opis] - 이 효과를 부여한 대상의 공격 스킬 종료 시, 부여 대상이 공격한 적을 스킬 1로 일방 공격 함.\n- 원호 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: BattleKeywords.json :: dataList[id=CoverAttack].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 1 against the same enemy Unit A attacked with its Skill. Activates at Unit A's Attack End.\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 1 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A.\n- Umiejętność użyta jako Atak Wsparcia nie wpływa na nadchodzącą listę Umiejętności B.
170. [Słowo kluczowe [ReCompulsion] — nazwa] 반전 강박
   źródło: BattleKeywords.json :: dataList[id=ReCompulsion].name
   kontekst: identyfikator tagu w tekstach: `[ReCompulsion]`
   limit: do 40 znaków
   EN: Reverse Compulsion
   PL: Odwrócona Kompulsja
171. [Słowo kluczowe [ReCompulsion] — opis] 매 턴 시작 시 정신력 15 회복
   źródło: BattleKeywords.json :: dataList[id=ReCompulsion].desc
   limit: do 120 znaków
   EN: Heal 15 SP at every Turn Start
   PL: Regeneruje 15 Poczytalności na początku każdej tury
172. [Słowo kluczowe [IndigoResultUp] — nazwa] 오만 위력 증가
   źródło: BattleKeywords.json :: dataList[id=IndigoResultUp].name
   kontekst: identyfikator tagu w tekstach: `[IndigoResultUp]`
   limit: do 40 znaków
   EN: Pride Power Up
   PL: Wzrost Mocy Pychy
173. [Słowo kluczowe [IndigoResultUp] — opis] 한 턴 동안 오만 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=IndigoResultUp].desc
   limit: do 120 znaków
   EN: Pride Skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Pychy rośnie o wartość efektu
174. [Słowo kluczowe [BladeResultUpTier1] — nazwa] 본국검 - 세법 전수
   źródło: BattleKeywords.json :: dataList[id=BladeResultUpTier1].name
   kontekst: identyfikator tagu w tekstach: `[BladeResultUpTier1]`
   limit: do 50 znaków
   EN: Sword of the Homeland - Rending
   PL: Szermierka Ojczyzny - Cięcie
175. [Słowo kluczowe [BladeResultUpTier1] — opis] 이번 턴 동안 스킬 1의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=BladeResultUpTier1].desc
   limit: do 120 znaków
   EN: Skill 1 gains Final Power by the effect’s Count for this turn.
   PL: W tej turze Moc Końcowa Umiejętności 1 rośnie o wartość efektu
176. [Słowo kluczowe [BladeResultUpTier2] — nazwa] 본국검 - 자법 전수
   źródło: BattleKeywords.json :: dataList[id=BladeResultUpTier2].name
   kontekst: identyfikator tagu w tekstach: `[BladeResultUpTier2]`
   limit: do 50 znaków
   EN: Sword of the Homeland - Penetrating
   PL: Szermierka Ojczyzny - Przebicie
177. [Słowo kluczowe [BladeResultUpTier2] — opis] 이번 턴 동안 스킬 2의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=BladeResultUpTier2].desc
   limit: do 120 znaków
   EN: Skill 2 gains Final Power by the effect’s Count for this turn.
   PL: W tej turze Moc Końcowa Umiejętności 2 rośnie o wartość efektu
178. [Słowo kluczowe [SwordPlayOfTheHomeland] — nazwa] 본국검술
   źródło: BattleKeywords.json :: dataList[id=SwordPlayOfTheHomeland].name
   kontekst: identyfikator tagu w tekstach: `[SwordPlayOfTheHomeland]`
   limit: do 40 znaków
   EN: Swordplay of the Homeland
   PL: Szermierka Ojczyzny
179. [Słowo kluczowe [SwordPlayOfTheHomeland] — opis] - 스킬 사용 시 호흡이 5 이상이면, 스킬 1, 2의 코인 위력 +(3/코인 수, 최소 1), 크리티컬 피해량 +(30/코인수)%\n- 스킬 사용 시 호흡이 7 이상이면, 스킬 3의 피해량 +(30/코인 수)%, 크리티컬 피해량 +(50/코인수)%
   źródło: BattleKeywords.json :: dataList[id=SwordPlayOfTheHomeland].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When at 5+ Poise, upon Skill use, Skill 1 and Skill 2 gain Coin Power +(3/# of Coins, minimum 1) and deal +(30/# of Coins)% damage on Critical Hit\n- When at 7+ Poise, upon Skill use, Skill 3 deals +(30/# of Coins)% damage and deals +(50/# of Coins)% damage on Critical Hit
   PL: - Przy użyciu Umiejętności, przy 5 lub więcej Oddechu, Umiejętności 1 i 2 zyskują moc monet +(3/liczba monet, min. 1) i zadają +(30/liczba monet)% obrażeń przy trafieniu krytycznym\n- Przy użyciu Umiejętności, przy 7 lub więcej Oddechu, Umiejętność 3 zadaje +(30/liczba monet)% obrażeń i +(50/liczba monet)% obrażeń przy trafieniu krytycznym
180. [Słowo kluczowe [SwordPlayOfTheMemorial] — nazwa] 추모
   źródło: BattleKeywords.json :: dataList[id=SwordPlayOfTheMemorial].name
   kontekst: identyfikator tagu w tekstach: `[SwordPlayOfTheMemorial]`
   limit: do 40 znaków
   EN: Remembrance
   PL: Pamięć
181. [Słowo kluczowe [SwordPlayOfTheMemorial] — opis] - 스킬 사용 시 호흡이 5 이상이면, 스킬 1, 2의 코인 위력 +(3/코인 수, 최소 1), 크리티컬 피해량 +(30/코인수)%\n- 스킬 사용 시 호흡이 7 이상이면, 스킬 3의 피해량 +(30/코인 수)%, 크리티컬 피해량 +(50/코인수)%
   źródło: BattleKeywords.json :: dataList[id=SwordPlayOfTheMemorial].desc
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Słowo kluczowe [RedApricotBlossom] — nazwa] 홍매화
   źródło: BattleKeywords.json :: dataList[id=RedApricotBlossom].name
   kontekst: identyfikator tagu w tekstach: `[RedApricotBlossom]`
   limit: do 40 znaków
   EN: Red Plum Blossom
   PL: Czerwony Kwiat Śliwy
183. [Słowo kluczowe [RedApricotBlossom] — opis] - 특수 출혈\n- 최댓값: 10\n- 메인 타겟이면 피격 시 크리티컬 발동 확률 +10%\n- 크리티컬로 피격 시 수치의 절반만큼 출혈을 얻고, 받는 크리티컬 피해량이 (수치x3)% 증가\n- 피격 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=RedApricotBlossom].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- Max value: 10\n- +10% chance for this unit to be Critically Hit if this unit is the main target\n- When struck by a Critical Hit, gain Bleed equal to the half of the value and take +(value x 3)% damage on Critical Hit\n- Reduce value by 1 when hit
   PL: - Szczególne Krwawienie\n- Maks.: 10\n- Jako główny cel: +10% szansy na trafienie krytyczne\n- Przy trafieniu krytycznym zyskuje tyle Krwawienia, ile wynosi połowa wartości, i otrzymuje +(wartość x 3)% obrażeń krytycznych\n- Przy trafieniu maleje o 1
184. [Słowo kluczowe [RedApricotBlossom] — podsumowanie] 피격 시 크리티컬 발동 확률, 받는 크리티컬 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=RedApricotBlossom].summary
   limit: do 120 znaków
   EN: Higher chance to be Critically Hit; take more damage upon Critical Hit
   PL: Wyższa szansa na trafienie krytyczne; otrzymuje więcej obrażeń krytycznych
185. [Słowo kluczowe [VibrationCollapse] — nazwa] 진동 - 붕괴
   źródło: BattleKeywords.json :: dataList[id=VibrationCollapse].name
   kontekst: identyfikator tagu w tekstach: `[VibrationCollapse]`
   limit: do 40 znaków
   EN: Tremor - Decay
   PL: Wstrząs - Rozpad
186. [Słowo kluczowe [VibrationCollapse] — opis] 대상의 진동 위력 4 당 방어 레벨 1 감소\n진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationCollapse].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 1 Defense Level for every 4 Tremor Potency on self\nWhen Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\nTurn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raises or reduces Tremor Potency/Count)
   PL: Poziom Obrony maleje o 1 za każde 4 Mocy Wstrząsu\nPrzy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\nNa koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
187. [Słowo kluczowe [EchoOfMansion] — nazwa] 저택의 메아리
   źródło: BattleKeywords.json :: dataList[id=EchoOfMansion].name
   kontekst: identyfikator tagu w tekstach: `[EchoOfMansion]`
   limit: do 40 znaków
   EN: Echoes of the Manor
   PL: Echa Rezydencji
188. [Słowo kluczowe [EchoOfMansion] — opis] - 스킬, 코인의 효과로 침잠 위력이나 횟수가 부여될 때, 50% 확률로 침잠 횟수 1 증가\n- 정신력이 있는 대상인 경우, 패닉 유형이 '저택의 메아리'로 변경되고, 패닉이 되면 다음 턴에 자신을 제외한 같은 팀의 무작위 캐릭터 2명에게 저택의 메아리 2 부여\n- 정신력이 없는 대상인 경우, 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨.\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨.
   źródło: BattleKeywords.json :: dataList[id=EchoOfMansion].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - 50% chance to gain +1 Sinking Count when gaining Sinking Potency or Count from Skill or Coin effects\n- SP Units: Change Panic Type to Echoes of the Manor. When this unit Panics, inflict 2 Echoes of the Manor to 2 random other allies of this unit next turn\n- Non-SP Units: -10% chance to flip Heads\n- Reduced by 1 at Turn End\nThis effect is not cumulative; inflicting it will replace the current value with the inflicted value.\n※ Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types.
   PL: - 50% szans na +1 Licznika Zatonięcia przy nadawaniu Mocy lub Licznika Zatonięcia efektami Umiejętności lub monet\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Echa Rezydencji”; w stanie Paniki nadaje 2 Echa Rezydencji 2 losowym pozostałym sojusznikom w następnej turze\n- Jednostki bez Poczytalności: -10% szansy na awers\n- Na koniec tury maleje o 1\nTen efekt nie kumuluje się — nadanie zastępuje bieżącą wartość.\n※ Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności.
189. [Słowo kluczowe [Switch_Vibration] — nazwa] 진폭 변환
   źródło: BattleKeywords.json :: dataList[id=Switch_Vibration].name
   kontekst: identyfikator tagu w tekstach: `[Switch_Vibration]`
   limit: do 40 znaków
   EN: Amplitude Conversion
   PL: Konwersja Amplitudy
190. [Słowo kluczowe [Switch_Vibration] — opis] 대상의 진동과 변경된 진동을 다른 유형의 진동으로 변경함.\n변경 시 기존 진동의 위력, 횟수가 유지됨.
   źródło: BattleKeywords.json :: dataList[id=Switch_Vibration].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Converts Tremor or already converted Tremor on target to a different type of Tremor.\nPotency and Count values do not change over the conversion.
   PL: Zamienia Wstrząs lub już przekształcony Wstrząs celu w inny rodzaj Wstrząsu.\nMoc i Licznik pozostają bez zmian.
191. [Słowo kluczowe [AzureResultUp] — nazwa] 우울 위력 증가
   źródło: BattleKeywords.json :: dataList[id=AzureResultUp].name
   kontekst: identyfikator tagu w tekstach: `[AzureResultUp]`
   limit: do 40 znaków
   EN: Gloom Power Up
   PL: Wzrost Mocy Posępności
192. [Słowo kluczowe [AzureResultUp] — opis] 이번 턴 동안 우울 속성 스킬의 최종 위력 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=AzureResultUp].desc
   limit: do 120 znaków
   EN: Gloom Skills gain final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Posępności rośnie o wartość efektu
193. [Słowo kluczowe [VibrationCrack] — nazwa] 진동 - 균열
   źródło: BattleKeywords.json :: dataList[id=VibrationCrack].name
   kontekst: identyfikator tagu w tekstach: `[VibrationCrack]`
   limit: do 40 znaków
   EN: Tremor - Fracture
   PL: Wstrząs - Pęknięcie
194. [Słowo kluczowe [VibrationCrack] — opis] - 흐트러짐 상태가 되었을 때, 자신의 진동 위력과 횟수의 합이 20 이상이면, 흐트러짐 단계 1 증가\n- 해당 효과로 최대 흐트러짐 단계를 초과할 수 없음\n\n진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationCrack].desc
   limit: do 510 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Staggered, and when the sum of Tremor Potency and Count adds up to 20 or higher, raise Stagger Level by 1\n- Cannot exceed maximum Stagger Level with this effect\n\nWhen hit by attacks that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\nTurn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raises or reduces Tremor Potency/Count)
   PL: - W stanie oszołomienia, przy sumie Mocy i Licznika Wstrząsu wynoszącej 20 lub więcej, Podnosi Poziom Oszołomienia o 1\n- Nie może przekroczyć maksymalnego Poziomu Oszołomienia tym efektem\n\nPrzy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\nNa koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
195. [Słowo kluczowe [ForwardToTheKing] — nazwa] 왕의 앞으로
   źródło: BattleKeywords.json :: dataList[id=ForwardToTheKing].name
   kontekst: identyfikator tagu w tekstach: `[ForwardToTheKing]`
   limit: do 40 znaków
   EN: Before the King
   PL: Przed Królem
196. [Słowo kluczowe [ForwardToTheKing] — opis] 공격 가중치가 1인 자신의 공격 적중 시 코인 결과 값의 50%만큼 동일한 대상이 아닌 공격 가능한 적 중 체력이 가장 낮은 적 2명에게 공격한 스킬의 속성과 같은 속성의 피해를 준다.
   źródło: BattleKeywords.json :: dataList[id=ForwardToTheKing].desc
   limit: do 280 znaków
   EN: When this unit's attack with 1 Atk Weight hits, inflict 50% of the resulting Coin value On Hit as (Affinity/Attack Type of the Attack Skill used to hit) damage against 2 other attackable enemies with the least HP.
   PL: Przy trafieniu atakiem o wagach 1 zadaje 50% wartości wyniku monet jako obrażenia atrybutu Umiejętności 2 innym atakowalnym wrogom z najniższym HP
197. [Słowo kluczowe [ForwardToTheBoundKing] — nazwa] 묶인 왕의 앞으로
   źródło: BattleKeywords.json :: dataList[id=ForwardToTheBoundKing].name
   kontekst: identyfikator tagu w tekstach: `[ForwardToTheBoundKing]`
   limit: do 40 znaków
   EN: Before the King in Binds
   PL: Przed Królem w Spętaniu
198. [Słowo kluczowe [ForwardToTheBoundKing] — opis] 공격 가중치가 1인 자신의 공격 적중 시 코인 결과 값의 100%만큼 동일한 대상이 아닌 공격 가능한 적 중 체력이 가장 낮은 적 2명에게 공격한 스킬의 속성과 같은 속성의 피해를 준다.
   źródło: BattleKeywords.json :: dataList[id=ForwardToTheBoundKing].desc
   limit: do 280 znaków
   EN: When this unit's attack with 1 Atk Weight hits, inflict 100% of the resulting Coin value On Hit as (Affinity/Attack Type of the Attack Skill used to hit) damage against 2 other attackable enemies with the least HP
   PL: Przy trafieniu atakiem o wagach 1 zadaje 100% wartości wyniku monet jako obrażenia atrybutu Umiejętności 2 innym atakowalnym wrogom z najniższym HP
199. [Słowo kluczowe [MarkOfButler] — nazwa] 버.표
   źródło: BattleKeywords.json :: dataList[id=MarkOfButler].name
   kontekst: identyfikator tagu w tekstach: `[MarkOfButler]`
   limit: do 40 znaków
   EN: B.M.
   PL: Oznaczenie Kamerdynera
200. [Słowo kluczowe [MarkOfButler] — opis] 이 효과가 있는 대상에게 에드가 가문 치프 버틀러 료슈의 스킬이 강화됨.\n턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=MarkOfButler].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Enhances Edgar Family Chief Butler Ryōshū Skills against targets with this effect.\nTurn End: reduce the Count by 1
   PL: Wzmacnia Umiejętności Ryośu, Głównej Kamerdynerki Rodziny Edgara, przeciwko celom z tym efektem.\nNa koniec tury maleje o 1
201. [Słowo kluczowe [PreparedMeat] — nazwa] 준비된 고기
   źródło: BattleKeywords.json :: dataList[id=PreparedMeat].name
   kontekst: identyfikator tagu w tekstach: `[PreparedMeat]`
   limit: do 40 znaków
   EN: Prepared Meat
   PL: Przygotowane Mięso
202. [Słowo kluczowe [PreparedMeat] — opis] 조건이 만족되면 턴 종료 시 여왕 요정이 이 캐릭터를 처치함
   źródło: BattleKeywords.json :: dataList[id=PreparedMeat].desc
   limit: do 120 znaków
   EN: If conditions are met, Fairy Queen kills this unit at Turn End
   PL: Jeśli warunki zostaną spełnione, Królowa Wróżek zabija tę jednostkę na koniec tury
203. [Słowo kluczowe [Hunger] — nazwa] 굶주림
   źródło: BattleKeywords.json :: dataList[id=Hunger].name
   kontekst: identyfikator tagu w tekstach: `[Hunger]`
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
204. [Słowo kluczowe [Hunger] — opis] 턴 종료 시 준비된 고기가 부여된 아군을 처치하지 못했으면 1 증가\n체력이 75% 미만이면, 2 증가, 체력이 50% 미만이면, 3 증가.\n턴 시작 시 준비된 고기가 부여된 아군을 처치했으면 1 감소.\n이후 수치가 0이면, 공격 위력 감소, 수비 위력 감소를 (이번 턴에 처치한 아군 수 x 3)만큼 얻음.
   źródło: BattleKeywords.json :: dataList[id=Hunger].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: gain 1 if this unit failed to defeat an ally with Prepared Meat.\nAt 75%- HP, gain 2. At 50%- HP, gain 3.\nTurn Start: lose 1 if this unit defeated an ally with Prepared Meat.\nAt 0 value, gain (# of allies defeated x 3)Attack Power Down and Defense Power Down.
   PL: Na koniec tury zyskuje 1, jeśli nie pokonał sojusznika z Przygotowanym Mięsem.\nPrzy HP poniżej 75% zyskuje 2; przy HP poniżej 50% zyskuje 3.\nNa początku tury traci 1, jeśli pokonał sojusznika z Przygotowanym Mięsem.\nPrzy wartości 0 zyskuje (liczba pokonanych sojuszników x 3) Spadków Mocy Ataku i Spadków Mocy Obrony
205. [Słowo kluczowe [UnstableFeeling] — nazwa] 불안정한 격정
   źródło: BattleKeywords.json :: dataList[id=UnstableFeeling].name
   kontekst: identyfikator tagu w tekstach: `[UnstableFeeling]`
   limit: do 40 znaków
   EN: Volatile Passion
   PL: Niestabilne Namiętności
206. [Słowo kluczowe [UnstableFeeling] — opis] - 공격 적중 시 화상 1 부여\n- 메인 타겟에게 화상이 있으면 최종 위력 +1\n- 수비 스킬을 연결하고 전투를 시작하면, 해당 턴동안 피격 시 공격자에게 화상 1 부여\n- 턴 종료 시 정신력이 (변신 유지 턴 수 x 5)만큼 감소.(최대 정신력 감소량 : 40)
   źródło: BattleKeywords.json :: dataList[id=UnstableFeeling].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Hit, inflict 1 Burn\n- If the main target has Burn, Final Power +1\n- When hit, if this unit had a Defense Skill chained at Combat Start, inflict Burn against the attacker for the turn\n- Turn End: lose (# of turns spent in Volatile E.G.O state x 5) SP. (Max SP loss : 40)
   PL: - Przy trafieniu atakiem nadaje 1 Podpalenia\n- Jeśli główny cel ma Podpalenie, Moc Końcowa +1\n- Jeśli na początku walki miała łańcuch Umiejętności obronnej, przy trafieniu nadaje atakującemu Podpalenie na czas tej tury\n- Na koniec tury traci (liczba turów utrzymania przemiany x 5) Poczytalności. (maks. 40)
207. [Słowo kluczowe [VibrationEcho] — nazwa] 진동 - 반향
   źródło: BattleKeywords.json :: dataList[id=VibrationEcho].name
   kontekst: identyfikator tagu w tekstach: `[VibrationEcho]`
   limit: do 40 znaków
   EN: Tremor - Reverb
   PL: Wstrząs - Rezonans
208. [Słowo kluczowe [VibrationEcho] — opis] - 진동 폭발 시 진동 위력만큼 나태 피해를 입음.\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상.\n- 턴 종료 후 횟수 1 감소.\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationEcho].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Sloth damage equal to Tremor Potency on self.\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency.\n- Turn End: reduce the Count by 1.\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wybuchu Wstrząsu otrzymuje obrażenia Lenistwem równe Mocy Wstrząsu.\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu.\n- Na koniec tury Licznik maleje o 1.\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
209. [Słowo kluczowe [ShieldManagerCryingToad] — nazwa] 울음 방울
   źródło: BattleKeywords.json :: dataList[id=ShieldManagerCryingToad].name
   kontekst: identyfikator tagu w tekstach: `[ShieldManagerCryingToad]`
   limit: do 40 znaków
   EN: Blubberbubble
   PL: Pękająca Bańka
210. [Słowo kluczowe [ShieldManagerCryingToad] — opis] - 이 효과는 보호막 관리 효과로 취급됨.\n- 턴 종료 시, 1 감소\n- 울음 방울 효과가 적용되는 동안 턴 종료 시 보호막이 사라지지 않음 (피해나 효과에 의해 사라지는 경우는 제외).\n- 울음 방울 효과가 적용된 보호막이 피격을 받아 파괴될 경우, 공격한 대상에게 침잠 위력과 침잠 횟수를 합하여 4만큼 무작위로 부여.\n- 보호막 수치는 중첩 가능하며, 울음 방울 효과가 적용 중인 경우에는 보호막의 수치가 보호막 적용 대상의 최대 체력 60%를 넘을 수 없음.
   źródło: BattleKeywords.json :: dataList[id=ShieldManagerCryingToad].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This effect counts as a 'Shield Management' effect.\n- Turn End: Reduce Count by 1\n- This unit does not lose Shield at Turn End as long as it has the Blubberbubble effect (unless depleted by damage or effect)\n- If the Shield affected by Blubberbubble breaks due to taking damage, inflict 4 Sinking Potency/Count against the attacker. (How much of that '4' value is Potency or Count is randomly determined)\n- This unit can stack their Shield value by using this effect. However, as long as Blubberbubble is in effect, the Shield value cannot exceed 60% of this unit's Max HP.
   PL: - Efekt zarządzania Tarczą\n- Na koniec tury maleje o 1\n- Podczas działania tego efektu Tarcza nie znika na koniec tury (poza przypadkami utraty od obrażeń lub efektów)\n- Gdy Tarcza objęta tym efektem pęknie od otrzymanych obrażeń, nadaje atakującemu łącznie 4 jednostek Mocy/Licznika Zatonięcia w losowym podziale\n- Wartość Tarczy można kumulować tym efektem; podczas jego działania Tarcza nie może przekroczyć 60% Maks. HP celu
211. [Słowo kluczowe [VibrationContinue] — nazwa] 진동 - 영속
   źródło: BattleKeywords.json :: dataList[id=VibrationContinue].name
   kontekst: identyfikator tagu w tekstach: `[VibrationContinue]`
   limit: do 40 znaków
   EN: Tremor - Everlasting
   PL: Wstrząs - Wieczność
212. [Słowo kluczowe [VibrationContinue] — opis] - 스킬, 코인 효과로 진동 폭발 시 자신의 (진동 위력)% 확률로 진동 폭발 1회 추가 발동. (최대 50%)\n- 스킬, 코인 효과로 진동 폭발 시 자신의 (진동 횟수)% 확률로 진동 폭발 1회 추가 발동. (최대 50%)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소.\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationContinue].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When hit by Skills or Coin effects that trigger Tremor Burst, (Tremor Potency on self)% chance to trigger an additional Tremor Burst. (max 50%)\n- When hit by Skills or Coin effects that trigger Tremor Burst, (Tremor Count on self)% chance to trigger an additional Tremor Burst. (max 50%)\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy trafieniu Umiejętnościami lub monetami wyzwalającymi Wybuch Wstrząsu: szansa równa (Moc Wstrząsu)% na dodatkowy Wybuch Wstrząsu. (maks. 50%)\n- Przy trafieniu Umiejętnościami lub monetami wyzwalającymi Wybuch Wstrząsu: szansa równa (Licznik Wstrząsu)% na dodatkowy Wybuch Wstrząsu. (maks. 50%)\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
213. [Słowo kluczowe [TimeSuspend] — nazwa] 시간 유예
   źródło: BattleKeywords.json :: dataList[id=TimeSuspend].name
   kontekst: identyfikator tagu w tekstach: `[TimeSuspend]`
   limit: do 40 znaków
   EN: Time Moratorium
   PL: Zawieszenie Czasu
214. [Słowo kluczowe [TimeSuspend] — opis] - 이 효과가 있는 동안 모든 피해를 받지 않고 저장함\n- 전투 종료 시 횟수가 1이면, 저장된 피해량의 (100 + 위력 x 15)%만큼 나태 피해를 입히고 위력만큼 진동 폭발\n- 턴 종료 시 위력 1 증가, 횟수 1 감소\n- 시간 유예가 적용된 대상에게 시간 유예를 추가로 부여 시, 시간 유예의 나태 피해와 진동 폭발 효과가 즉시 발동하고 버프 해제
   źródło: BattleKeywords.json :: dataList[id=TimeSuspend].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Does not take any damage as long as this effect is active; store all damage received instead\n- Combat End: If there is only 1 Count left of this effect, the effect triggers Tremor Burst (Stack) times after dealing (100 + (Stack x 15))% of stored damage as Sloth damage\n- Turn End: Gain 1 Stack and lose 1 Count\n- The Time Moratorium will immediately expire after triggering the Tremor Burst and the Sloth damage effect if another instance of Time Moratorium is inflicted on a unit that has Time Moratorium.
   PL: - Dopóki efekt jest aktywny, nie otrzymuje obrażeń, lecz je magazynuje\n- Po zakończeniu walki, przy Liczniku równym 1, zadaje (100 + wartość x 15)% zmagazynowanych obrażeń Lenistwem i wywołuje Wybuch Wstrząsu tyle razy, ile wynosi wartość\n- Na koniec tury wartość rośnie o 1, a Licznik maleje o 1\n- Nadanie kolejnego Zawieszenia Czasu jednostce, która je posiada, natychmiast uruchamia efekt obrażeń Lenistwem i Wybuch Wstrząsu, po czym wzmocnienie znika
215. [Słowo kluczowe [TimeRentalTwoPersonality] — nazwa] 시간 대여
   źródło: BattleKeywords.json :: dataList[id=TimeRentalTwoPersonality].name
   kontekst: identyfikator tagu w tekstach: `[TimeRentalTwoPersonality]`
   limit: do 40 znaków
   EN: Borrowed Time
   PL: Wypożyczony Czas
216. [Słowo kluczowe [TimeRentalTwoPersonality] — opis] 턴 종료 시 횟수가 2 이상이면,\n- 다음 턴에 신속, 합 위력 증가, 취약을 (시간 대여 횟수 - 1)만큼 얻음.\n- 다음 턴에 얻을 신속보다 속박이 많을 경우, 다음 턴 시작 시 시간 대여 해제, 흐트러짐 상태가 됨\n턴 종료 시 횟수가 1이면, 다음 턴에 속박을 (시간 대여 위력 - 1) X 2만큼 얻음\n턴 종료 시 위력 1 증가, 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=TimeRentalTwoPersonality].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End at 2+ Count:\n- Gain (Borrowed Time Count - 1) Haste, Clash Power Up, and Fragile next turn\n- If this unit is set to gain more Bind than Haste next turn, the Borrowed Time effect expires at the next Turn Start, and this unit gets Staggered\n\nTurn End: At 1 Count, gain 2(Borrowed Time Stack - 1) Bind next turn\nTurn End: Gain 1 Stack, lose 1 Count
   PL: Na koniec tury, przy Liczniku 2+:\n- W następnej turze zyskuje (Licznik Wypożyczonego Czasu - 1) Pośpiechu, Wzrostów Mocy Starcia i Wrażliwości\n- Jeśli w następnej turze ma otrzymać więcej Spętań niż Pośpiechu, efekt znika na początku następnej tury, a jednostka zostaje oszołomiona\nNa koniec tury, przy Liczniku 1, w następnej turze zyskuje (wartość Wypożyczonego Czasu - 1) x 2 Spętań\nNa koniec tury wartość rośnie o 1, a Licznik maleje o 1
217. [Słowo kluczowe [VibrationChainPersonality] — nazwa] 진동 - 사슬
   źródło: BattleKeywords.json :: dataList[id=VibrationChainPersonality].name
   kontekst: identyfikator tagu w tekstach: `[VibrationChainPersonality]`
   limit: do 40 znaków
   EN: Tremor - Chain
   PL: Wstrząs - Łańcuch
218. [Słowo kluczowe [VibrationChainPersonality] — opis] - 진동 위력 10 당 합 위력 1 감소 (최대 3)\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationChainPersonality].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 1 Clash Power for every 10 Tremor Potency on self (max 3)\n- When Hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Moc Starcia maleje o 1 za każde 10 Mocy Wstrząsu (maks. 3)\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n- (Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
219. [Słowo kluczowe [GazePersonality] — nazwa] 경멸의 시선
   źródło: BattleKeywords.json :: dataList[id=GazePersonality].name
   kontekst: identyfikator tagu w tekstach: `[GazePersonality]`
   limit: do 40 znaków
   EN: Gaze of Contempt
   PL: Pogardliwe Spojrzenie
220. [Słowo kluczowe [GazePersonality] — opis] - 최댓값 : 7\n- 경멸의 시선 1당 가하는 피해량 +7%\n- 턴 종료 시 효과 소멸됨\n- 턴 종료 시 경멸의 시선이 7이면, 효과가 소멸되는 대신 다음 턴에 시선의 경멸로 변환됨\n\n[시선의 경멸]\n- 보호 7 얻음\n- 피해량 감소 7 얻음\n- 보유 중인 스킬 슬롯 중 하나의 도발치 20 증가\n- 시선의 경멸이 유지되는 동안 경멸의 시선을 얻을 수 없음\n- 턴 종료 시 효과 소멸됨
   źródło: BattleKeywords.json :: dataList[id=GazePersonality].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 7\n- Deal +7% damage for every Gaze of Contempt\n- Turn End: this effect expires\n- Turn End: At 7 Gaze of Contempt value, convert it to Contempt of the Gaze next turn instead of expiring\n\n[Contempt of the Gaze]\n- Gain 7 Protection\n- Gain 7 Damage Down\n- One of this unit's Slots gains +20 Aggro\n- Cannot gain Gaze of Contempt as long as Contempt of the Gaze is active\n- Turn End: this effect expires
   PL: - Maks.: 7\n- Zadaje +7% obrażeń za każde Pogardliwe Spojrzenie\n- Na koniec tury efekt znika\n- Na koniec tury, przy wartości 7, zamiast zniknąć, w następnej turze zamienia się w Pogardę Spojrzenia\n\n[Pogarda Spojrzenia]\n- Zyskuje 7 Ochrony\n- Zyskuje 7 Spadków Obrażeń\n- Jeden z slotów zyskuje +20 Wartości Prowokacji\n- Dopóki aktywna jest Pogarda Spojrzenia, nie może zyskać Pogardliwego Spojrzenia\n- Na koniec tury efekt znika
221. [Słowo kluczowe [ContemptPersonality] — nazwa] 시선의 경멸
   źródło: BattleKeywords.json :: dataList[id=ContemptPersonality].name
   kontekst: identyfikator tagu w tekstach: `[ContemptPersonality]`
   limit: do 40 znaków
   EN: Contempt of the Gaze
   PL: Pogarda Spojrzenia
222. [Słowo kluczowe [ContemptPersonality] — opis] - 보호 7 얻음\n- 피해량 감소 7 얻음\n- 보유 중인 스킬 슬롯 중 하나의 도발치 20 증가\n- 시선의 경멸이 유지되는 동안 경멸의 시선을 얻을 수 없음\n- 턴 종료 시 효과 소멸됨
   źródło: BattleKeywords.json :: dataList[id=ContemptPersonality].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 7 Protection\n- Gain 7 Damage Down\n- One of this unit's Skill Slots gains +20 Aggro\n- Cannot gain Gaze of Contempt as long as Contempt of the Gaze is active\n- Turn End: this effect expires
   PL: - Zyskuje 7 Ochrony\n- Zyskuje 7 Spadków Obrażeń\n- Jeden z slotów zyskuje +20 Wartości Prowokacji\n- Dopóki aktywna jest Pogarda Spojrzenia, nie może zyskać Pogardliwego Spojrzenia\n- Na koniec tury efekt znika
223. [Słowo kluczowe [KnowledgeTraining] — nazwa] 지식 단련
   źródło: BattleKeywords.json :: dataList[id=KnowledgeTraining].name
   kontekst: identyfikator tagu w tekstach: `[KnowledgeTraining]`
   limit: do 40 znaków
   EN: Erudition
   PL: Biegłość Wiedzy
224. [Słowo kluczowe [KnowledgeTraining] — opis] - 최댓값 : 6\n- 스킬을 버릴 때 자신의 최대 체력의 (지식 단련 x 1.5)%만큼의 보호막을 얻음 (턴 당 1회)\n- 탐구한 지식이 2 이상인 상태에서 스킬을 버릴 때, 합 위력 증가 1 얻음 (턴 당 1회)\n- 적에게 공격 스킬로 피격받아 체력 피해를 입을 때마다 1 감소\n- 흐트러질 시 효과 소멸됨
   źródło: BattleKeywords.json :: dataList[id=KnowledgeTraining].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 6\n- When Discarding a Skill, gain (Erudition x 1.5)% of this unit's max HP as Shield (once per turn)\n- If this unit Discards a Skill at 2+ Insight, gain 1 Clash Power (once per turn)\n- Reduced by 1 when taking HP damage after getting hit by an enemy's Attack Skill\n- Expires when Staggered
   PL: - Maks.: 6\n- Odrzucając Umiejętność, zyskuje Tarczę równą (Biegłość x 1,5)% Maks. HP (raz na turę)\n- Odrzucając Umiejętność przy 2 lub więcej Zgłębionej Wiedzy, zyskuje 1 Wzrost Mocy Starcia (raz na turę)\n- Maleje o 1 przy każdej utracie HP od trafienia Umiejętnością ataku wroga\n- Znika po oszołomieniu
225. [Słowo kluczowe [BoseProjektil] — nazwa] 찢어진 추억
   źródło: BattleKeywords.json :: dataList[id=BoseProjektil].name
   kontekst: identyfikator tagu w tekstach: `[BoseProjektil]`
   limit: do 40 znaków
   EN: Torn Memory
   PL: Naderwane Wspomnienie
226. [Słowo kluczowe [BoseProjektil] — opis] - 최댓값 : 7\n- 특정 스킬에 사용됨
   źródło: BattleKeywords.json :: dataList[id=BoseProjektil].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value : 7\n- Used for certain Skills
   PL: - Maks.: 7\n- Zużywane przez określone Umiejętności
227. [Słowo kluczowe [ChargeLoad] — nazwa] 부하
   źródło: BattleKeywords.json :: dataList[id=ChargeLoad].name
   kontekst: identyfikator tagu w tekstach: `[ChargeLoad]`
   limit: do 40 znaków
   EN: Load
   PL: Obciążenie
228. [Słowo kluczowe [ChargeLoad] — opis] - 최댓값 : 6\n- 충전 횟수를 소모한 공격 스킬의 피해량이 수치당 2.5% 증가. (최대 15%)\n- 효과가 부여된 대상이 W사 직원이면, 수치당 5% 증가로 적용됨. (최대 30%)\n- 턴 종료시 소멸
   źródło: BattleKeywords.json :: dataList[id=ChargeLoad].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value : 6\n- Attack Skills that consumed Charge Count deal +2.5% damage for every value on self (max 15%)\n- If the affected unit is a W Corp. employee., deal +5% damage for every value instead (max 30%)\n- Turn End: this effect expires
   PL: - Maks.: 6\n- Umiejętności ataku, które zużyły Licznik Ładowania, zadają +2,5% obrażeń za każdą wartość (maks. 15%)\n- Jeśli celem jest pracownik Korporacji W, zadają +5% za każdą wartość (maks. 30%)\n- Na koniec tury efekt znika
229. [Słowo kluczowe [PhotoElectricity] — nazwa] 광전
   źródło: BattleKeywords.json :: dataList[id=PhotoElectricity].name
   kontekst: identyfikator tagu w tekstach: `[PhotoElectricity]`
   limit: do 40 znaków
   EN: Photoelectricity
   PL: Fotopobudzenie
230. [Słowo kluczowe [PhotoElectricity] — opis] 최댓값 : 3\n피격 시 공격자의 충전 횟수가 수치만큼 증가 (스킬당 1회)\n- 공격자의 충전 횟수가 5 이하면, 충전 횟수 3 추가로 얻음\n턴 종료 시 효과 소멸됨
   źródło: BattleKeywords.json :: dataList[id=PhotoElectricity].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Value: 3\nWhen this unit is hit, the Attacker gains Charge Count equal to the value (once per Skill)\n- If the Attacker has 5- Charge Count, they gain +3 additional Charge Count\nTurn End: this effect expires
   PL: Maks.: 3\nPrzy trafieniu atakujący zyskuje Licznik Ładowania równy wartości (raz na Umiejętność)\n- Przy 5 lub mniej Liczników Ładowania atakujący dodatkowo zyskuje 3\n- Na koniec tury efekt znika
231. [Słowo kluczowe [Coffin] — nazwa] 관
   źródło: BattleKeywords.json :: dataList[id=Coffin].name
   kontekst: identyfikator tagu w tekstach: `[Coffin]`
   limit: do 40 znaków
   EN: Coffin
   PL: Trumna
232. [Słowo kluczowe [Coffin] — opis] - 최대 10\n- 턴 종료 시 다음 턴에\n3당 피해량 증가 2 얻음 (최대 6)\n4당 속도 최솟값 1 증가 (최대 2)\n5당 합 위력 증가 1 얻음 (최대 2)
   źródło: BattleKeywords.json :: dataList[id=Coffin].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- At Turn End:\n  - Gain 2 Damage Up next turn for every 3 Value (max 6)\n  - Raise minimum Speed by 1 next turn for every 4 Value (max 2)\n  - Gain 1 Clash Power Up next turn for every 5 Value (max 2)
   PL: - Maks.: 10\n- Na koniec tury, w następnej turze:\nza każde 3 — 2 Wzrosty Obrażeń (maks. 6)\nza każde 4 — minimalna Szybkość +1 (maks. 2)\nza każde 5 — 1 Wzrost Mocy Starcia (maks. 2)
233. [Słowo kluczowe [WildHunt] — nazwa] 와일드헌트
   źródło: BattleKeywords.json :: dataList[id=WildHunt].name
   kontekst: identyfikator tagu w tekstach: `[WildHunt]`
   limit: do 40 znaków
   EN: Wild Hunt
   PL: Dziki Gon
234. [Słowo kluczowe [WildHunt] — opis] - 처음 부여받은 턴동안 체력이 1 남고 턴 종료 시 전체 체력의 50%만큼 체력 회복, 정신력이 0으로 초기화됨.\n- 사망시, 가장 적은 E.G.O 자원을 1 얻음\n- 공격에 의해 사망시, 마지막으로 자신을 공격한 대상에게 침잠 3 부여\n- 부활한 턴 종료시 사망
   źródło: BattleKeywords.json :: dataList[id=WildHunt].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In the same turn this unit gained Wild Hunt for the first time, always have 1 remaining HP; "revive"(heal 50% HP and reset SP to 0) this unit at Turn End.\n- On death, gain 1 E.G.O resource for the least-owned E.G.O resource\n- If this unit is killed by an attack, inflict 3 Sinking against the last attacker\n- Dies at the end of the same turn this unit was revived in
   PL: - W turze pierwszego nadania HP spada do 1; na koniec tury regeneruje 50% ogólnego HP i zeruje Poczytalność\n- Po śmierci zyskuje 1 zasobu E.G.O najrzadszego atrybutu\n- Śmierć od ataku nadaje 3 Zatonięcia ostatniemu atakującemu\n- Umiera na koniec tury, w której został wskrzeszony
235. [Słowo kluczowe [NightPathfinding] — nazwa] 듀라한
   źródło: BattleKeywords.json :: dataList[id=NightPathfinding].name
   kontekst: identyfikator tagu w tekstach: `[NightPathfinding]`
   limit: do 40 znaków
   EN: Dullahan
   PL: Dullahan
236. [Słowo kluczowe [NightPathfinding] — opis] - 최대 3\n- 공격 레벨 3 증가\n- 방어 레벨 3 감소\n- 속도 최솟값, 최댓값 1 증가\n- 턴 종료 시, 다음 턴에 1 얻음 (단, 자신의 정신력이 -25 이하면 제거)\n- 턴 종료 시 듀라한이 있으면, 자신의 정신력이 (15 - (관 수치/2))만큼 감소 (최소 10)
   źródło: BattleKeywords.json :: dataList[id=NightPathfinding].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 3\n- Gain 3 Offense Level\n- Lose 3 Defense Level\n- Raise Min & Max Speed values by 1\n- Turn End: Gain 1 Dullahan next turn (At -25 SP or less, however, completely lose Dullahan)\n- Turn End: If this unit has Dullahan, lose (15 - (Coffin/2)) SP. (min 10)
   PL: - Maks.: 3\n- Poziom Ataku +3\n- Poziom Obrony -3\n- Minimalna i maksymalna Szybkość +1\n- Na koniec tury zyskuje 1 w następnej turze (przy Poczytalności -25 lub niższej efekt znika całkowicie)\n- Na koniec tury, przy aktywnym Dullahanie, traci (15 - (Trumna/2)) Poczytalności (min. 10)
237. [Słowo kluczowe [WanderingFootsteps] — nazwa] 다가오는 파탄
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps].name
   kontekst: identyfikator tagu w tekstach: `[WanderingFootsteps]`
   limit: do 40 znaków
   EN: Impending Ruin
   PL: Nadchodząca Ruina
238. [Słowo kluczowe [WanderingFootsteps] — opis] - 정신력이 있는 대상인 경우, 패닉 유형이 '파탄'으로 변경됨.\n(파탄: 사기저하가 되면, 매 턴 종료 시 침잠 3 얻음. 자신의 합 위력 -1\n패닉이 되면 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가. 자신의 합 위력 -2)\n- 정신력이 없는 대상인 경우, 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨.\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨.
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: change their Panic Type to "Ruin".\n(Ruin: When this unit enters Low Morale state, gain 3 Sinking at every Turn End and lose 1 Clash Power. When this unit Panics, gain 5 Sinking and 3 Sinking Count at every Turn End and lose 2 Clash Power)\n- Non-SP Units: -10% chance to flip Heads\n- Reduced by 1 at Turn End\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value.\n※ Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types.
   PL: - Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Ruina”\n(Ruina: w stanie Spadku Moralu na koniec każdej tury zyskuje 3 Zatonięcia i traci 1 Mocy Starcia; w stanie Paniki na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia oraz traci 2 Mocy Starcia)\n- Jednostki bez Poczytalności: -10% szansy na awers\n- Na koniec tury maleje o 1\nTen efekt nie kumuluje się — nadanie zastępuje bieżącą wartość.\n※ Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności.
239. [Słowo kluczowe [WanderingFootsteps_Main] — nazwa] 다가오는 파탄
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Main].name
   kontekst: identyfikator tagu w tekstach: `[WanderingFootsteps_Main]`
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
240. [Słowo kluczowe [WanderingFootsteps_Main] — opis] - 정신력이 있는 대상인 경우, 패닉 유형이 '파탄'으로 변경됨\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Main].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - SP Units: Change their Panic Type to 'Ruin'\n- Reduced by 1 at Turn End
   PL: - Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Ruina”\n- Na koniec tury maleje o 1
241. [Słowo kluczowe [WanderingFootsteps_Sub] — nazwa] 다가오는 파탄
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Sub].name
   kontekst: identyfikator tagu w tekstach: `[WanderingFootsteps_Sub]`
   (powtórzenie elementu 237 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
242. [Słowo kluczowe [WanderingFootsteps_Sub] — opis] - 앞면이 나올 확률 -10%\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Sub].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - -10% chance to flip Heads\n- Reduced by 1 at Turn End
   PL: - -10% szansy na awers\n- Na koniec tury maleje o 1
243. [Słowo kluczowe [WanderingFootsteps_LowMorale] — nazwa] 파탄
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WanderingFootsteps_LowMorale]`
   limit: do 40 znaków
   EN: Ruin
   PL: Ruina
244. [Słowo kluczowe [WanderingFootsteps_LowMorale] — opis] - 사기 저하\n- 자신의 합 위력 -1. 매 턴 종료시 침잠 3 얻음
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Clash Power -1 on self. Gain 3 Sinking at every Turn End
   PL: - Spadek Moralu\n- Moc Starcia -1; na koniec każdej tury zyskuje 3 Zatonięcia
245. [Słowo kluczowe [WanderingFootsteps_LowMorale] — podsumowanie] 자신의 합 위력 -1. 매 턴 종료시 침잠 3 얻음
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_LowMorale].summary
   limit: do 120 znaków
   EN: Clash Power -1 on self. Gain 3 Sinking at every Turn End
   PL: Moc Starcia -1; na koniec każdej tury zyskuje 3 Zatonięcia
246. [Słowo kluczowe [WanderingFootsteps_Panic] — nazwa] 파탄
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WanderingFootsteps_Panic]`
   (powtórzenie elementu 243 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Słowo kluczowe [WanderingFootsteps_Panic] — opis] - 패닉\n- 자신의 합 위력 -2. 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Clash Power -2 on self. Gain 5 Sinking and +3 Sinking Count at every Turn End
   PL: - Panika\n- Moc Starcia -2; na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia
248. [Słowo kluczowe [WanderingFootsteps_Panic] — podsumowanie] 자신의 합 위력 -2. 매 턴 종료시 침잠 5 얻음, 침잠 횟수 3 증가
   źródło: BattleKeywords.json :: dataList[id=WanderingFootsteps_Panic].summary
   limit: do 120 znaków
   EN: Clash Power -2 on self. Gain 5 Sinking and +3 Sinking Count at every Turn End
   PL: Moc Starcia -2; na koniec każdej tury zyskuje 5 Zatonięć i 3 Liczniki Zatonięcia
249. [Słowo kluczowe [UninvitedGuestPersonality] — nazwa] 초청받지 않은 자
   źródło: BattleKeywords.json :: dataList[id=UninvitedGuestPersonality].name
   kontekst: identyfikator tagu w tekstach: `[UninvitedGuestPersonality]`
   limit: do 40 znaków
   EN: The Uninvited
   PL: Nieproszony Gość
250. [Słowo kluczowe [UninvitedGuestPersonality] — opis] - 최대 2\n- 사망 시 마지막 공격자의 정신력 3 회복, 이 효과가 효과를 보유하지 않은 무작위 아군에게 2로 옮겨감.\n- 자신의 침잠 1당 받는 피해량 +0.5% (최대 10%, 집중 전투일 경우 부위마다 별도로 판정)\n- 턴 종료시 1 감소
   źródło: BattleKeywords.json :: dataList[id=UninvitedGuestPersonality].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 2\n- Upon death, the last attacker heals 3 SP; then, a random ally without this effect gains 2 Stacks of this effect.\n- Take +0.5% damage for every Sinking on self (max 10%; for Focused Encounters, count Sinking on each Part separately)\n- Turn End: reduced by 1
   PL: - Maks.: 2\n- Po śmierci ostatni atakujący regeneruje 3 Poczytalności, po czym losowy sojusznik bez tego efektu zyskuje 2 stosy\n- Otrzymuje +0,5% obrażeń za każde Zatonięcie (maks. 10%; w walkach skupionych liczone osobno dla każdej części)\n- Na koniec tury maleje o 1
251. [Słowo kluczowe [DevyatDimensionalSack] — nazwa] 딜리버리 캐리어 - 로쟈
   źródło: BattleKeywords.json :: dataList[id=DevyatDimensionalSack].name
   kontekst: identyfikator tagu w tekstach: `[DevyatDimensionalSack]`
   limit: do 40 znaków
   EN: Courier Trunk - Rodion
   PL: Kufer Kuriera - Rodion
252. [Słowo kluczowe [DevyatDimensionalSack] — opis] - 기본값 : 0\n- 턴 시작 시, 3 얻음\n- 스택은 퇴각 시 사라지지 않고 저장됨\n- 10 이상이면, 속도 최솟값, 최댓값 1 증가\n- 20 이상이면, 합 위력 증가 1, 참격 피해량 증가 1 얻음\n- 30 이상이면,\n· 스킬 사용 시 최대 체력의 (스택/3)%만큼 체력 피해와 (스택/3)만큼의 정신력 피해를 받음\n· 턴 종료 시 최대 체력의 (스택/2)%만큼 체력 피해와 (스택/2)만큼 정신력 피해를 받음 (퇴각 전에 적용됨)
   źródło: BattleKeywords.json :: dataList[id=DevyatDimensionalSack].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 0\n- Turn Start: gain 3 Stack\n- Stack does not expire upon Retreat; it is stored instead\n- At 10+ Stack: raise Min & Max Speed values by 1\n- At 20+ Stack: Gain 1 Clash Power Up and 1 Slash Damage Up\n- At 30+ Stack:\n· On Skill Use, take (Stack/3)% HP damage and (Stack/3) SP damage\n· On Turn End, take (Stack/2)% HP damage and (Stack/2) SP damage (applies before Retreat)
   PL: - Wartość bazowa: 0\n- Na początku tury zyskuje 3 stosy\n- Stosy nie znikają przy Odwrócie — zostają zapisane\n- Przy 10 lub więcej: minimalna i maksymalna Szybkość +1\n- Przy 20 lub więcej: 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń Cięcia\n- Przy 30 lub więcej:\n· Przy użyciu Umiejętności otrzymuje (stosy/3)% obrażeń HP i tyle samo obrażeń Poczytalności\n· Na koniec tury otrzymuje (stosy/2)% obrażeń HP i tyle samo obrażeń Poczytalności (przed Odwrótem)
253. [Słowo kluczowe [Retreat] — nazwa] 전략적 휴식 복지 모드
   źródło: BattleKeywords.json :: dataList[id=Retreat].name
   kontekst: identyfikator tagu w tekstach: `[Retreat]`
   limit: do 40 znaków
   EN: Strategic R&R Mode
   PL: Tryb Strategicznego Odpoczynku
254. [Słowo kluczowe [Retreat] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n· 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n· 전투 복귀 시 자신의 슬롯 수가 1로 초기화, 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: BattleKeywords.json :: dataList[id=Retreat].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death)\n· In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n· When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self save for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)\n· W walkach łańcuchowych przekazuje swoje sloty jednostce zastępczej i trafia na koniec kolejki rezerwowych (jeśli w następnej turze nie ma kogo zastąpić, opuszcza walkę całkowicie; przy powrocie wraca w kolejności odwrotu)\n· Wracając do walki zachowuje HP i Poczytalność z chwili odwrotu i traci wszystkie efekty poza nielicznymi wyjątkami (przy Poczytalności poniżej 0 zostaje ona wyzerowana)
255. [Słowo kluczowe [DefensiveStance] — nazwa] 방어 태세
   źródło: BattleKeywords.json :: dataList[id=DefensiveStance].name
   kontekst: identyfikator tagu w tekstach: `[DefensiveStance]`
   limit: do 40 znaków
   EN: Defensive Stance
   PL: Postawa Obronna
256. [Słowo kluczowe [DefensiveStance] — opis] - 최댓값: 2\n- 이 효과는 합산되지 않고, 갱신됨\n- 턴 종료 시 1 감소\n- 이 효과를 얻으면 다음 턴에 아래 효과 적용\n· 속도가 최솟값으로 고정됨\n· 방어 레벨 증가 5 얻음\n· (10 / 자신의 슬롯 수)만큼 자신의 각 슬롯 도발치 증가\n· 스킬 지정 시 속도에 관계 없이 공격 대상을 자신으로 변경할 수 있음 (집중 전투 전용)\n· 합 승리시 진동 폭발\n· 피해로 인해 흐트러짐 상태가 되지 않음
   źródło: BattleKeywords.json :: dataList[id=DefensiveStance].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 2\n- This effect does not compound in potency; stacking it only extends its duration.\n- Reduced by 1 at Turn End\n- When a unit gains this effect, gain the following effects next turn:\n  · Fix this unit's Speed to its minimum value\n  · Gain 5 Defense Level Up\n  · Each of this unit's Slots gain +(10 / this unit's # of Slots) Aggro\n  · When chaining Skills, this unit can draw enemies' attack toward this unit regardless of Speed (Focused Encounters only)\n  · Upon Clash Win, trigger Tremor Burst\n  · Cannot be Staggered by damage
   PL: - Maks.: 2\n- Nie kumuluje się — nadanie przedłuża czas działania\n- Na koniec tury maleje o 1\n- Po nadaniu, w następnej turze:\n· Szybkość zostaje zablokowana na wartości minimalnej\n· 5 Wzrostów Poziomu Obrony\n· Każdy slot zyskuje +(10/liczba slotów) Wartości Prowokacji\n· Może przyciągać ataki wrogów niezależnie od Szybkości przy wskazywaniu Umiejętności (tylko walki skupione)\n· Po wygranej w Starciu wywołuje Wybuch Wstrząsu\n· Nie zostaje oszołomiony przez obrażenia
257. [Słowo kluczowe [CanDuelGuard] — nazwa] 합 가능 가드
   źródło: BattleKeywords.json :: dataList[id=CanDuelGuard].name
   kontekst: identyfikator tagu w tekstach: `[CanDuelGuard]`
   limit: do 40 znaków
   EN: Clashable Guard
   PL: Blok Zdatny do Starcia
258. [Słowo kluczowe [CanDuelGuard] — opis] - 합 승리 시 대상에게 마지막 합 위력만큼 흐트러짐 손상을 입힘.\n- 합 패배 후 피격 시 최종 위력만큼 공격자의 스킬 최종 위력을 감소시킴.\n- 합 패배 시 공격 스킬과의 레벨 차이, 공명으로 인해 최종 위력이 증가하지 않음.
   źródło: BattleKeywords.json :: dataList[id=CanDuelGuard].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Win: raise the target's Stagger Threshold by this unit's final Clash Power.\n- On Clash Lose: when hit, reduce the attacker's final Skill Power by this unit's Final Power.\n- On Clash Lose: does not gain Final Power from the following sources: Resonance and the Level disparity against the Attack Skill
   PL: - Po wygranej w Starciu podnosi Próg Oszołomienia celu o własną końcową Moc Starcia\n- Po przegranej w Starciu, przy trafieniu, obniża końcową Moc Umiejętności atakującego o własną Moc Końcową\n- Po przegranej w Starciu nie zyskuje Mocy Końcowej z Rezonansu ani różnicy poziomów względem Umiejętności ataku
259. [Słowo kluczowe [SuperCoin] — nazwa] 파괴 불가 코인
   źródło: BattleKeywords.json :: dataList[id=SuperCoin].name
   kontekst: identyfikator tagu w tekstach: `[SuperCoin]`
   limit: do 40 znaków
   EN: Unbreakable Coin
   PL: Moneta Niezniszczalna
260. [Słowo kluczowe [SuperCoin] — opis] - 합 패배 시 코인이 파괴되지 않음.\n- 공격 스킬에 해당 코인이 있으면, 피격 후 해당 코인으로 공격함.\n- 합 패배 시 파괴되지 않은 코인은 코인 위력이 1이 됨.
   źródło: BattleKeywords.json :: dataList[id=SuperCoin].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This coin does not break upon Clash Lose.\n- If an Attack Skill has this Coin, attack with this Coin after getting hit.\n- Upon Clash Lose, fix the Coin Power of the unbroken Coin to 1
   PL: - Moneta nie ulega zniszczeniu po przegranej w Starciu\n- Jeśli Umiejętność ataku zawiera tę monetę, atakuje nią po otrzymaniu trafienia\n- Po przegranej w Starciu moc niezniszczonej monety zostaje ustalona na 1
261. [Słowo kluczowe [BloodScissorPersonalityFirst] — nazwa] 핏빛 가위날
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalityFirst].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorPersonalityFirst]`
   limit: do 40 znaków
   EN: Blood-tinged Scissorblades
   PL: Zakrwawione Ostrza Nożyc
262. [Słowo kluczowe [BloodScissorPersonalityFirst] — opis] - 최댓값: 10\n- 핏빛 가위날 1단계\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalityFirst].desc
   limit: do 660 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blood-tinged Scissorblades\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 10\n- Zakrwawione Ostrza Nożyc, etap 1\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
263. [Słowo kluczowe [BloodScissorPersonalitySecond] — nazwa] 핏빛 가위날 II
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalitySecond].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorPersonalitySecond]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades II
   PL: Zakrwawione Ostrza Nożyc II
264. [Słowo kluczowe [BloodScissorPersonalitySecond] — opis] - 최댓값: 20\n- 핏빛 가위날 2단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalitySecond].desc
   limit: do 760 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 20\n- Zakrwawione Ostrza Nożyc, etap 2\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
265. [Słowo kluczowe [BloodScissorPersonalityThird] — nazwa] 핏빛 가위날 III
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalityThird].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorPersonalityThird]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades III
   PL: Zakrwawione Ostrza Nożyc III
266. [Słowo kluczowe [BloodScissorPersonalityThird] — opis] - 최댓값: 30\n- 핏빛 가위날 3단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1 얻음\n- 핏빛 가위날이 10 이상이면, 핏빛 가위날 II로 전환됨.\n- 핏빛 가위날이 20 이상이면, 핏빛 가위날 III으로 전환됨.\n- 핏빛 가위날이 소모되어, 부족해지면 이전 단계가 됨.\n- 핏빛 가위날은 1 미만으로 감소하지 않음.\n- 핏빛 가위날 II면, 수치에 비례하여 공격 레벨 증가 1, 방어 레벨 감소 1을 얻음\n- 핏빛 가위날 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodScissorPersonalityThird].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up for every 5 Stack\n- At 10+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades II.\n- At 20+ Blood-tinged Scissorblades, converts to Blood-tinged Scissorblades III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- Blood-tinged Scissorblades does not drop below 1.\n- At Blood-tinged Scissorblades II, gain 1 Offense Level Up and 1 Defense Level Down based on the Stack\n- At Blood-tinged Scissorblades III, gain 1 Offense Level Up based on the Stack
   PL: - Maks.: 30\n- Zakrwawione Ostrza Nożyc, etap 3\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku\n- Przy 10 lub więcej zamienia się w Zakrwawione Ostrza Nożyc II\n- Przy 20 lub więcej zamienia się w Zakrwawione Ostrza Nożyc III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku
267. [Słowo kluczowe [LineCuttingPersonality] — nazwa] 재봉 대상
   źródło: BattleKeywords.json :: dataList[id=LineCuttingPersonality].name
   kontekst: identyfikator tagu w tekstach: `[LineCuttingPersonality]`
   limit: do 40 znaków
   EN: Sewing Target
   PL: Cel Szycia
268. [Słowo kluczowe [LineCuttingPersonality] — opis] - 최댓값: 1\n- 출혈당 받는 피해량 +0.5% (최대 10%)\n- 턴 종료 시, 1 감소
   źródło: BattleKeywords.json :: dataList[id=LineCuttingPersonality].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Take +0.5% damage for every Bleed on self (max 10%)\n- Turn End: reduced by 1
   PL: - Maks.: 1\n- Otrzymuje +0,5% obrażeń za każde Krwawienie (maks. 10%)\n- Na koniec tury maleje o 1
269. [Słowo kluczowe [Snare] — nazwa] 올가미
   źródło: BattleKeywords.json :: dataList[id=Snare].name
   kontekst: identyfikator tagu w tekstach: `[Snare]`
   limit: do 40 znaków
   EN: Lasso
   PL: Lasso
270. [Słowo kluczowe [Snare] — opis] - 최댓값 : 3\n- 턴 종료시 자신의 현재 속도만큼 파열 위력 얻음 (최대 5), 다음 턴에 속박 1 얻음\n- 턴 종료시 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=Snare].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 3\n- Turn End: gain Rupture Potency equal to this unit's current Speed value (max 5), and gain 1 Bind next turn\n- Turn End: reduced by 1
   PL: - Maks.: 3\n- Na koniec tury zyskuje Moc Rozdarcia równą aktualnej Szybkości (maks. 5), a w następnej turze 1 Spętania\n- Na koniec tury maleje o 1
271. [Słowo kluczowe [BloodyHandGregFirst] — nazwa] 피로 물든 손
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregFirst].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHandGregFirst]`
   limit: do 40 znaków
   EN: Bloodied Hand
   PL: Zakrwawiona Dłoń
272. [Słowo kluczowe [BloodyHandGregFirst] — opis] - 최댓값 : 10\n- 피로 물든 손 1단계\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregFirst].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Bloodied Hand\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 10\n- Zakrwawiona Dłoń, etap 1\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
273. [Słowo kluczowe [BloodyHandGregSecond] — nazwa] 피로 물든 손 II
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregSecond].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHandGregSecond]`
   limit: do 40 znaków
   EN: Bloodied Hand II
   PL: Zakrwawiona Dłoń II
274. [Słowo kluczowe [BloodyHandGregSecond] — opis] - 최댓값 : 20\n- 피로 물든 손 2단계\n- 턴 시작시, 수치 10당 공격 레벨 증가 1 얻음\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregSecond].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Bloodied Hand\n- Turn Start: gain 1 Offense Level Up for every 10 Stack\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 20\n- Zakrwawiona Dłoń, etap 2\n- Na początku tury za każde 10 stosów: 1 Wzrost Poziomu Ataku\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
275. [Słowo kluczowe [BloodyHandGregThird] — nazwa] 피로 물든 손 III
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregThird].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHandGregThird]`
   limit: do 40 znaków
   EN: Bloodied Hand III
   PL: Zakrwawiona Dłoń III
276. [Słowo kluczowe [BloodyHandGregThird] — opis] - 최댓값 : 30\n- 피로 물든 손 3단계\n- 턴 시작시, 수치 10당 공격 레벨 증가 1 얻음\n- 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여\n- 피로 물든 손이 10 이상이면, 피로 물든 손 II 로 전환됨.\n- 피로 물든 손이 20 이상이면, 피로 물든 손 III 으로 전환됨.\n- 피로 물든 손이 소모되어, 부족해지면 이전 단계가 됨.\n- 피로 물든 손 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 피로 물든 손 III이면, 수치에 비례하여 공격 레벨 증가 1을 얻고, 기본 스킬 적중시마다 파열 1, 출혈 1 추가로 부여
   źródło: BattleKeywords.json :: dataList[id=BloodyHandGregThird].desc
   limit: do 700 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Bloodied Hand\n- Turn Start: gain 1 Offense Level Up for every 10 Stack\n- On Hit with Base Skills: additionally inflict 1 Rupture and 1 Bleed\n- At 10+ Bloodied Hand, converts to Bloodied Hand II.\n- At 20+ Bloodied Hand, converts to Bloodied Hand III.\n- Reverts to previous Stage when the Stack drops below the requirements.\n- At Bloodied Hand II, gain 1 Offense Level Up based on the Stack\n- At Bloodied Hand III, gain 1 Offense Level Up based on the Stack, and additionally inflict 1 Rupture and 1 Bleed On Hit with Base Skills
   PL: - Maks.: 30\n- Zakrwawiona Dłoń, etap 3\n- Na początku tury za każde 10 stosów: 1 Wzrost Poziomu Ataku\n- Każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia\n- Przy 10 lub więcej zamienia się w Zakrwawioną Dłoń II\n- Przy 20 lub więcej zamienia się w Zakrwawioną Dłoń III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku, a każde trafienie Umiejętnością bazową dodatkowo nadaje 1 Rozdarcia i 1 Krwawienia
277. [Słowo kluczowe [WornHeartGreg] — nazwa] 닳아버린 마음
   źródło: BattleKeywords.json :: dataList[id=WornHeartGreg].name
   kontekst: identyfikator tagu w tekstach: `[WornHeartGreg]`
   limit: do 40 znaków
   EN: Ailing Heart
   PL: Zmęczone Serce
278. [Słowo kluczowe [WornHeartGreg] — opis] - 최댓값 : 10\n- 턴 종료시, 수치 1 증가\n- 턴 시작시 수치 3당 방어 레벨 증가 1 얻음\n- 자신의 체력이 50% 미만이면 수치 3당 방어 레벨이 1 증가함\n- 자신의 현재 체력이 최대 체력의 40% 미만이면, 기본 스킬 적중시 피해량의 (수치 x 5)% 만큼 체력 회복 (최소 1. 소수점 버림. 스킬 당 최대 30 회복)
   źródło: BattleKeywords.json :: dataList[id=WornHeartGreg].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Turn End: gain 1 Stack\n- Turn Start: gain 1 Defense Level Up for every 3 Stack\n- At 50%- HP, gain 1 Defense Level for every 3 Stack\n- At 40%- HP, On Hit with Base Skills, heal (Stack x 5)% of damage dealt On Hit as HP (min 1; rounded down; heal up to 30 HP per Skill)
   PL: - Maks.: 10\n- Na koniec tury wartość rośnie o 1\n- Na początku tury za każde 3 wartości: 1 Wzrost Poziomu Obrony\n- Przy HP poniżej 50% za każde 3 wartości: dodatkowo 1 Poziomu Obrony\n- Przy HP poniżej 40% każde trafienie Umiejętnością bazową leczy 10% zadanych obrażeń (min. 1; zaokrąglone w dół; do 30 HP na Umiejętność)
279. [Słowo kluczowe [BloomingThornsRodionFirst] — nazwa] 피어나는 가시
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionFirst].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThornsRodionFirst]`
   limit: do 40 znaków
   EN: Blooming Thorn
   PL: Kwitnące Ciernie
280. [Słowo kluczowe [BloomingThornsRodionFirst] — opis] - 최댓값 : 10\n- 피어나는 가시 1단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionFirst].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture Potency using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 10\n- Kwitnące Ciernie, etap 1\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Mocy Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
281. [Słowo kluczowe [BloomingThornsRodionSecond] — nazwa] 피어나는 가시 II
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionSecond].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThornsRodionSecond]`
   limit: do 40 znaków
   EN: Blooming Thorn II
   PL: Kwitnące Ciernie II
282. [Słowo kluczowe [BloomingThornsRodionSecond] — opis] - 최댓값 : 20\n- 피어나는 가시 2단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionSecond].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 20\n- Kwitnące Ciernie, etap 2\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
283. [Słowo kluczowe [BloomingThornsRodionThird] — nazwa] 피어나는 가시 III
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionThird].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThornsRodionThird]`
   limit: do 40 znaków
   EN: Blooming Thorn III
   PL: Kwitnące Ciernie III
284. [Słowo kluczowe [BloomingThornsRodionThird] — opis] - 최댓값 : 30\n- 피어나는 가시 3단계\n- 수치 2당 방어 레벨 1 증가 (최대 5)\n- 피격 시 공격자에게 출혈 1 부여 후 수치 1 감소\n- [라만차랜드 공주 로쟈 인격 전용 효과]\n· 수치가 최대치면 다음 단계로 전환.\n· 기본 스킬 코인 효과의 출혈, 파열 위력 부여량이 (현재 단계 - 1)만큼 증가.\n·  피어나는 가시가 소모되어 부족해지면 이전 단계가 됨.
   źródło: BattleKeywords.json :: dataList[id=BloomingThornsRodionThird].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blooming Thorn\n- Gain 1 Defense Level for every 2 Stack (max 5)\n- When hit, inflict 1 Bleed against the attacker and lose 1 Stack\n- [The Princess of La Manchaland Rodion Only]\n· At max Stack, convert to the next Stage of this effect.\n· Inflict +(Stage - 1) more Bleed and Rupture using this unit's Base Attack Skill Coin effects.\n· Reverts to previous Stage when the Stack drops below the requirements.
   PL: - Maks.: 30\n- Kwitnące Ciernie, etap 3\n- Za każde 2 wartości: Poziom Obrony +1 (maks. 5)\n- Przy trafieniu nadaje atakującemu 1 Krwawienia, po czym wartość maleje o 1\n- [Tylko dla osobowości Księżniczki La Manchalandy Rodion]\n· Przy maksymalnej wartości zamienia się w następny etap\n· Efekty monet Umiejętności bazowych nadają o (obecny etap - 1) więcej Krwawienia i Rozdarcia\n· Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu
285. [Słowo kluczowe [FestivalFeverRodion] — nazwa] 축제의 열기
   źródło: BattleKeywords.json :: dataList[id=FestivalFeverRodion].name
   kontekst: identyfikator tagu w tekstach: `[FestivalFeverRodion]`
   limit: do 40 znaków
   EN: Festive Fever
   PL: Gorączka Święta
286. [Słowo kluczowe [FestivalFeverRodion] — opis] - 최댓값 : 10\n- 턴 종료시 소멸\n- 수치당 출혈이 부여된 대상에게 가하는 피해량 +1.5%\n- 혈찬을 소모하거나 얻는 스킬이면, 대신 수치당 가하는 피해량 +3%
   źródło: BattleKeywords.json :: dataList[id=FestivalFeverRodion].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Expires at Turn End\n- Against targets that have Bleed: deal +1.5% damage for every Stack\n- Skills that consume or gain Bloodfeast deal +3% damage for every Stack instead
   PL: - Maks.: 10\n- Znika na koniec tury\n- Zadaje +1,5% obrażeń za stos celom z Krwawieniem\n- Umiejętności zużywające lub zyskujące Uczta Krwi zadają zamiast tego +3% obrażeń za stos
287. [Słowo kluczowe [VibrationSpring] — nazwa] 진동 - 태엽감기
   źródło: BattleKeywords.json :: dataList[id=VibrationSpring].name
   kontekst: identyfikator tagu w tekstach: `[VibrationSpring]`
   limit: do 40 znaków
   EN: Tremor - Clockwinding
   PL: Wstrząs - Nakręcanie
288. [Słowo kluczowe [VibrationSpring] — opis] - 속도 최댓값 +2\n- 자신이 스킬, 코인 효과로 진동 위력이나 진동 횟수를 부여할 때, 자신의 진동 횟수를 1 소모하여 부여량 +1\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 시 횟수 1 감소\n- (진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationSpring].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed + 2\n- Consume Tremor Count on self to inflict 1 more of Tremor Potency or Count when inflicting them with this unit's Skill or Coin effects\n- When hit by Skills that trigger Tremor Burst, raise the Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n- (Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Maksymalna Szybkość +2\n- Nadając Moc lub Licznik Wstrząsu efektami własnych Umiejętności lub monet, zużywa 1 Licznika Wstrząsu, by nadać o 1 więcej\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n- (Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
289. [Słowo kluczowe [DevyatDimensionalSackSinclair] — nazwa] 딜리버리 캐리어 - 싱클레어
   źródło: BattleKeywords.json :: dataList[id=DevyatDimensionalSackSinclair].name
   kontekst: identyfikator tagu w tekstach: `[DevyatDimensionalSackSinclair]`
   limit: do 40 znaków
   EN: Courier Trunk - Sinclair
   PL: Kufer Kuriera - Sinclair
290. [Słowo kluczowe [DevyatDimensionalSackSinclair] — opis] - 기본값 : 0\n- 턴 시작 시, 3 얻음\n- 스택은 퇴각 시 사라지지 않고 저장됨\n- 10 이상이면, 속도 최솟값, 최댓값 1 증가\n- 20 이상이면, 합 위력 증가 1, 타격 피해량 증가 1 얻음\n- 30 이상이면,\n· 스킬 사용 시 최대 체력의 (스택/3)%만큼 체력 피해와 (스택/3)만큼의 정신력 피해를 받음\n· 턴 종료 시 최대 체력의 (스택/2)%만큼 체력 피해와 (스택/2)만큼 정신력 피해를 받음 (퇴각 전에 적용됨)
   źródło: BattleKeywords.json :: dataList[id=DevyatDimensionalSackSinclair].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 0\n- Turn Start: gain 3 Stack\n- Stack does not expire upon Retreat; it is stored instead\n- At 10+ Stack: raise Min & Max Speed values by 1\n- At 20+ Stack: Gain 1 Clash Power Up and 1 Blunt Damage Up\n- At 30+ Stack:\n· On Skill Use, take (Stack/3)% HP damage and (Stack/3) SP damage\n· On Turn End, take (Stack/2)% HP damage and (Stack/2) SP damage (applies before Retreat)
   PL: - Wartość bazowa: 0\n- Na początku tury zyskuje 3 stosy\n- Stosy nie znikają przy Odwrócie — zostają zapisane\n- Przy 10 lub więcej: minimalna i maksymalna Szybkość +1\n- Przy 20 lub więcej: 1 Wzrost Mocy Starcia i 1 Wzrost Obrażeń Uderzenia\n- Przy 30 lub więcej:\n· Przy użyciu Umiejętności otrzymuje (stosy/3)% obrażeń HP i tyle samo obrażeń Poczytalności\n· Na koniec tury otrzymuje (stosy/2)% obrażeń HP i tyle samo obrażeń Poczytalności (przed Odwrótem)
291. [Słowo kluczowe [Zazen] — nazwa] 참선
   źródło: BattleKeywords.json :: dataList[id=Zazen].name
   kontekst: identyfikator tagu w tekstach: `[Zazen]`
   limit: do 40 znaków
   EN: Dhyāna
   PL: Dhyāna
292. [Słowo kluczowe [Zazen] — opis] - 최댓값 : 108\n- 수치당 가하는 피해량 +1%
   źródło: BattleKeywords.json :: dataList[id=Zazen].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 108\n- Deal +1% damage for every Stack
   PL: - Maks.: 108\n- Zadaje +1% obrażeń za każdą wartość
293. [Słowo kluczowe [Zazen] — podsumowanie] 가하는 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=Zazen].summary
   limit: do 120 znaków
   EN: Deal more damage
   PL: Zadaje więcej obrażeń
294. [Słowo kluczowe [SwirlingBloodPersonality] — nazwa] 일렁임【혈귀】
   źródło: BattleKeywords.json :: dataList[id=SwirlingBloodPersonality].name
   kontekst: identyfikator tagu w tekstach: `[SwirlingBloodPersonality]`
   limit: do 40 znaków
   EN: Shimmering【Bloodfiend】
   PL: Drgający【Krwiopijca】
295. [Słowo kluczowe [SwirlingBloodPersonality] — opis] - 최댓값: 50\n- 이 버프가 있는 동안 보호막 체력이 받는 출혈 피해는 혈찬이 됨.\n- 부여될 때 수치만큼 보호막 체력을 얻음.\n- 턴 종료시 제거됨.
   źródło: BattleKeywords.json :: dataList[id=SwirlingBloodPersonality].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- As long as this effect exists, all Bleed damage taken by the Shield HP is converted to Bloodfeast.\n- Gain Shield HP equal to the Stack at the moment of its application\n- Expires at Turn End
   PL: - Maks.: 50\n- Dopóki to wzmocnienie działa, obrażenia Krwawieniem otrzymywane przez HP Tarczy stają się Ucztą Krwi\n- Przy nadaniu zyskuje HP Tarczy równe wartości\n- Znika na koniec tury
296. [Słowo kluczowe [BloodArmorPersonalityFirst] — nazwa] 경혈
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalityFirst].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmorPersonalityFirst]`
   limit: do 40 znaków
   EN: Hardblood
   PL: Skondensowana Krew
297. [Słowo kluczowe [BloodArmorPersonalityFirst] — opis] - 최댓값: 10\n- 경혈 1단계\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 10 당, 속도 최솟값, 최댓값 1 증가\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalityFirst].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Stage 1 Hardblood\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- Raise Min & Max Speed values by 1 for every 10 Hardblood\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 10\n- Skondensowana Krew, etap 1\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Za każde 10 Skondensowanej Krwi: minimalna i maksymalna Szybkość +1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
298. [Słowo kluczowe [BloodArmorPersonalitySecond] — nazwa] 경혈 II
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalitySecond].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmorPersonalitySecond]`
   limit: do 40 znaków
   EN: Hardblood II
   PL: Skondensowana Krew II
299. [Słowo kluczowe [BloodArmorPersonalitySecond] — opis] - 최댓값: 20\n- 경혈 2단계\n- 턴 시작시 수치 5 당 공격 레벨 증가 1 얻음\n- 속도 최솟값, 최댓값 1 증가\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalitySecond].desc
   limit: do 610 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Stage 2 Hardblood\n- Turn Start: gain 1 Offense Level Up for every 5 Stack\n- Raise Min & Max Speed values by 1\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 20\n- Skondensowana Krew, etap 2\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku\n- Minimalna i maksymalna Szybkość +1\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
300. [Słowo kluczowe [BloodArmorPersonalityThird] — nazwa] 경혈 III
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalityThird].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmorPersonalityThird]`
   limit: do 40 znaków
   EN: Hardblood III
   PL: Skondensowana Krew III
301. [Słowo kluczowe [BloodArmorPersonalityThird] — opis] - 최댓값: 30\n- 경혈 3단계\n- 턴 시작시 수치 5 당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 속도 최솟값, 최댓값 2 증가\n- 경혈이 10 이상이면, 경혈 II로 전환됨.\n- 경혈이 20 이상이면, 경혈 III으로 전환됨.\n- 경혈이 소모되어, 부족해지면 이전 단계가 됨.\n- 경혈은 1 미만으로 감소하지 않음.\n- 경혈 II면, 수치에 비례하여 공격 레벨 증가 1 얻음\n- 경혈 III이면, 수치에 비례하여 공격 레벨 증가 1 얻음, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=BloodArmorPersonalityThird].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Stage 3 Hardblood\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Up for every 5 Stack\n- Raise Min & Max Speed values by 2\n- At 10+ Hardblood, converts to Hardblood II.\n- At 20+ Hardblood, converts to Hardblood III.\n- Reverts to the previous Stage when the Stack drops below the requirements.\n- Hardblood does not drop below 1.\n- At Hardblood II, gain 1 Offense Level Up based on the Stack\n- At Hardblood III, gain 1 Offense Level Up and 1 Defense Level Up based on the Stack
   PL: - Maks.: 30\n- Skondensowana Krew, etap 3\n- Na początku tury za każde 5 stosów: 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony\n- Minimalna i maksymalna Szybkość +2\n- Przy 10 lub więcej zamienia się w Skondensowaną Krew II\n- Przy 20 lub więcej zamienia się w Skondensowaną Krew III\n- Po zużyciu stosów, gdy ich brakuje, wraca do poprzedniego etapu\n- Nie spada poniżej 1\n- Na etapie II zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku\n- Na etapie III zyskuje proporcjonalnie do stosów 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
302. [Słowo kluczowe [SadLamanchaland] — nazwa] 책임감
   źródło: BattleKeywords.json :: dataList[id=SadLamanchaland].name
   kontekst: identyfikator tagu w tekstach: `[SadLamanchaland]`
   limit: do 40 znaków
   EN: Responsibility
   PL: Poczucie Obowiązku
303. [Słowo kluczowe [SadLamanchaland] — opis] - 최댓값: 1\n- 합 위력 +1\n- 가하는 피해량 +20%\n- 받는 피해량 +20%
   źródło: BattleKeywords.json :: dataList[id=SadLamanchaland].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Clash Power +1\n- Deal +20% damage\n- Take +20% damage
   PL: - Maks.: 1\n- Moc Starcia +1\n- Zadawane obrażenia +20%\n- Otrzymywane obrażenia +20%
304. [Słowo kluczowe [FreishutzOutisEgoBullet_1st] — nazwa] 첫번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_1st].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_1st]`
   limit: do 40 znaków
   EN: The First Magic Bullet
   PL: Pierwsza Magiczna Amunicja
305. [Słowo kluczowe [FreishutzOutisEgoBullet_1st] — opis] - 가하는 피해량 +20%\n- 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 30)
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_1st].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +20% damage\n- Raise the target's Stagger Threshold by damage dealt (max 30)
   PL: - Zadawane obrażenia +20%\n- Podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 30)
306. [Słowo kluczowe [FreishutzOutisEgoBullet_2nd] — nazwa] 두번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_2nd].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_2nd]`
   limit: do 40 znaków
   EN: The Second Magic Bullet
   PL: Druga Magiczna Amunicja
307. [Słowo kluczowe [FreishutzOutisEgoBullet_2nd] — opis] - 가하는 피해량 +10%\n- 메인 대상을 제외한 대상에게 피해를 입힘 (대상 수: 최대 4명), 메인 대상이 받는 피해는 0이 됨\n- 적중시 마비 3 부여
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_2nd].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage\n- Deal damage to targets other than the main target (max targets: 4); the main target takes 0 damage\n- On Hit, inflict 3 Paralyze
   PL: - Zadawane obrażenia +10%\n- Zadaje obrażenia celom poza głównym celem (maks. 4 cele); główny cel otrzymuje 0 obrażeń\n- Przy trafieniu nadaje 3 Paraliżu
308. [Słowo kluczowe [FreishutzOutisEgoBullet_3rd] — nazwa] 세번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_3rd].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_3rd]`
   limit: do 40 znaków
   EN: The Third Magic Bullet
   PL: Trzecia Magiczna Amunicja
309. [Słowo kluczowe [FreishutzOutisEgoBullet_3rd] — opis] - 가하는 피해량 +20%\n- 공격 시작 전 가중치 2 증가\n- 적중시 대상에게 공격 위력 감소 2, 화상 10 부여
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_3rd].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +20% damage\n- Before Attack: gain +2 Atk Weight\n- On Hit, inflict 2 Attack Power Down and 10 Burn
   PL: - Zadawane obrażenia +20%\n- Przed atakiem: wagi +2\n- Przy trafieniu nadaje 2 Spadki Mocy Ataku i 10 Podpalenia
310. [Słowo kluczowe [FreishutzOutisEgoBullet_4th] — nazwa] 네번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_4th].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_4th]`
   limit: do 40 znaków
   EN: The Fourth Magic Bullet
   PL: Czwarta Magiczna Amunicja
311. [Słowo kluczowe [FreishutzOutisEgoBullet_4th] — opis] - 가하는 피해량 +30%\n- 공격 시작 전 가중치 3 증가\n- 적중시 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 20), 다음 턴에 취약 3 부여
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_4th].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +30% damage\n- Before Attack: gain +3 Atk Weight\n- On Hit, raise the target's Stagger Threshold by damage dealt (max 20); then, inflict 3 Fragility next turn
   PL: - Zadawane obrażenia +30%\n- Przed atakiem: wagi +3\n- Przy trafieniu podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 20), a w następnej turze nadaje 3 Wrażliwości
312. [Słowo kluczowe [FreishutzOutisEgoBullet_5th] — nazwa] 다섯번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_5th].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_5th]`
   limit: do 40 znaków
   EN: The Fifth Magic Bullet
   PL: Piąta Magiczna Amunicja
313. [Słowo kluczowe [FreishutzOutisEgoBullet_5th] — opis] - 가하는 피해량 +30%\n- 공격 시작 전 가중치 4 증가\n- 적중시 대상에게 화상 10 부여. 다음 턴에 공격 레벨 감소 4, 방어 레벨 감소 4 부여
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_5th].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +30% damage\n- Before Attack: gain +4 Atk Weight\n- On Hit, inflict 10 Burn; then, inflict 4 Offense Level down and 4 Defense Level Down next turn
   PL: - Zadawane obrażenia +30%\n- Przed atakiem: wagi +4\n- Przy trafieniu nadaje 10 Podpalenia, a w następnej turze 4 Spadki Poziomu Ataku i 4 Spadki Poziomu Obrony
314. [Słowo kluczowe [FreishutzOutisEgoBullet_6th] — nazwa] 여섯번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_6th].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_6th]`
   limit: do 40 znaków
   EN: The Sixth Magic Bullet
   PL: Szósta Magiczna Amunicja
315. [Słowo kluczowe [FreishutzOutisEgoBullet_6th] — opis] - 공격 시작 전 가중치 6 증가\n- 적중시 대상에게 피해량만큼 흐트러짐 손상을 입힘 (최대 30)\n- 메인 타겟의 화상 7당 코인을 재사용함 (최대 2회 재사용)\n- 더하기 코인 스킬 기본 위력 16 감소\n- 빼기 코인 스킬 기본 위력 22 감소\n - 더하기 코인 위력 8 감소\n - 빼기 코인 위력 12 감소
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_6th].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Before Attack: gain +6 Atk Weight\n- On Hit, raise the target's Stagger Threshold by damage dealt (max 30)\n- Reuse the Coin for every 7 Burn on the main target (2 times max)\n- Plus Coin Skill Base Power -16\n- Minus Coin Skill Base Power -22\n - Plus Coin Power -8\n - Minus Coin Power -12
   PL: - Przed atakiem: wagi +6\n- Przy trafieniu podnosi Próg Oszołomienia celu o zadane obrażenia (maks. 30)\n- Używa monety ponownie za każde 7 Podpalenia na głównym celu (maks. 2 razy)\n- Moc Bazowa Umiejętności z monetą plus -16\n- Moc Bazowa Umiejętności z monetą minus -22\n- Moc monety plus -8\n- Moc monety minus -12
316. [Słowo kluczowe [FreishutzOutisEgoBullet_7th] — nazwa] 일곱번째 마탄
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_7th].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBullet_7th]`
   limit: do 40 znaków
   EN: The Seventh Magic Bullet
   PL: Siódma Magiczna Amunicja
317. [Słowo kluczowe [FreishutzOutisEgoBullet_7th] — opis] - 가하는 피해량 +200%\n- 대상의 잃은 체력 1%당 피해량 +2.5% (최대 200%)\n- 공격 시작 전 대상이나 자신의 관통 속성 내성이 2.0 미만이면, 이 공격에 한해 취약(x2.0)으로 변경함\n- 공격 종료 시, 사망함
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBullet_7th].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +200% damage\n- Deal +2.5% damage for every 1% missing HP on target (max 200%)\n- Before Attack: for this attack, if the Pierce Damage Res. on target or on self are less than 2.0, change them to Fatal(x2.0)\n- Attack End: kills this unit
   PL: - Zadawane obrażenia +200%\n- Zadaje +2,5% obrażeń za każdy 1% brakującego HP celu (maks. 200%)\n- Przed atakiem: jeśli Odporność na Przebicie celu lub własna jest niższa niż 2,0, dla tego ataku zmienia ją na Wrażliwość Maksymalną (x2,0)\n- Po zakończeniu ataku umiera
318. [Słowo kluczowe [FreishutzOutisEgoBulletCnt] — nazwa] 사수의 탄환
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBulletCnt].name
   kontekst: identyfikator tagu w tekstach: `[FreishutzOutisEgoBulletCnt]`
   limit: do 40 znaków
   EN: Marksman's Bullet
   PL: Pocisk Strzelca Wyborowego
319. [Słowo kluczowe [FreishutzOutisEgoBulletCnt] — opis] 사수의 탄환에 따라 사용하는 탄환이 달라짐
   źródło: BattleKeywords.json :: dataList[id=FreishutzOutisEgoBulletCnt].desc
   limit: do 120 znaków
   EN: Uses a different Ammo depending on Marksman's Bullet
   PL: Używana amunicja zależy od Pocisku Strzelca Wyborowego
320. [Słowo kluczowe [CoveringFire] — nazwa] 타겟 포착
   źródło: BattleKeywords.json :: dataList[id=CoveringFire].name
   kontekst: identyfikator tagu w tekstach: `[CoveringFire]`
   limit: do 40 znaków
   EN: Target Spotted
   PL: Namierzenie Celu
321. [Słowo kluczowe [CoveringFire] — opis] 이 효과를 부여한 대상의 공격 스킬 종료시, 부여 대상이 공격한 적을 스킬 2로 일방 공격함\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: BattleKeywords.json :: dataList[id=CoveringFire].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 2 against the same enemy Unit A attacked with its Skill. Activates at Unit A's Attack End.\n- The Skill used due to this effect does not affect Unit B's upcoming Skills list.
   PL: Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 2 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A.\n- Umiejętność użyta dzięki temu efektowi nie wpływa na nadchodzącą listę Umiejętności B.
322. [Słowo kluczowe [FullReload] — nazwa] 재장전
   źródło: BattleKeywords.json :: dataList[id=FullReload].name
   kontekst: identyfikator tagu w tekstach: `[FullReload]`
   limit: do 40 znaków
   EN: Reload
   PL: Przeładowanie
323. [Słowo kluczowe [FullReload] — opis] 보유한 탄환을 모두 버리고, 최대치만큼 다시 얻음
   źródło: BattleKeywords.json :: dataList[id=FullReload].desc
   limit: do 120 znaków
   EN: Lose all currently owned Ammo, and reload it back to full
   PL: Zużywa całą posiadaną amunicję i uzupełnia ją do maksimum
324. [Słowo kluczowe [Bullet_LogicAtelier] — nazwa] 탄환 - 로직 아틀리에
   źródło: BattleKeywords.json :: dataList[id=Bullet_LogicAtelier].name
   kontekst: identyfikator tagu w tekstach: `[Bullet_LogicAtelier]`
   limit: do 40 znaków
   EN: Ammo - Atelier Logic
   PL: Amunicja - Atelier Logic
325. [Słowo kluczowe [Bullet_LogicAtelier] — opis] 특수 탄환\n로직 아틀리에 공방제 특수탄\n- 이 탄환은 외부 효과로 얻거나 값이 증가할 수 없음
   źródło: BattleKeywords.json :: dataList[id=Bullet_LogicAtelier].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Unique Ammo\nAtelier Logic Workshop Special Ammo\n- This Ammo's count cannot be gained or lost due to external effects
   PL: Szczególna amunicja\nSpecjalny pocisk warsztatu Atelier Logic\n- Liczby tej amunicji nie można zyskać ani zmienić efektami zewnętrznymi
326. [Słowo kluczowe [Retreat_FullStop] — nazwa] 후방 지원 배치
   źródło: BattleKeywords.json :: dataList[id=Retreat_FullStop].name
   kontekst: identyfikator tagu w tekstach: `[Retreat_FullStop]`
   limit: do 40 znaków
   EN: Overwatch Assignment
   PL: Przydział Odwachu
327. [Słowo kluczowe [Retreat_FullStop] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n· 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n· 전투 복귀 시 자신의 슬롯 수가 1로 초기화, 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: BattleKeywords.json :: dataList[id=Retreat_FullStop].desc
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
328. [Słowo kluczowe [LogicAtelierAM] — nazwa] 집중【저격】
   źródło: BattleKeywords.json :: dataList[id=LogicAtelierAM].name
   kontekst: identyfikator tagu w tekstach: `[LogicAtelierAM]`
   limit: do 40 znaków
   EN: Concentration【Sniper】
   PL: Skupienie【Snajper】
329. [Słowo kluczowe [LogicAtelierAM] — opis] - 최댓값 : 4\n- 턴 종료시 수치 1 증가
   źródło: BattleKeywords.json :: dataList[id=LogicAtelierAM].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: gain 1 Stack
   PL: - Maks.: 4\n- Na koniec tury wartość rośnie o 1
330. [Słowo kluczowe [MeleeCover] — nazwa] 근접 지원
   źródło: BattleKeywords.json :: dataList[id=MeleeCover].name
   kontekst: identyfikator tagu w tekstach: `[MeleeCover]`
   limit: do 40 znaków
   EN: Melee Support
   PL: Wsparcie z Bliska
331. [Słowo kluczowe [MeleeCover] — opis] - 이 효과를 부여한 대상의 스킬 종료시, 해당 아군을 공격한 적을 ‘근접 지원’ 스킬로 일방 공격함.\n- 근접 지원 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음
   źródło: BattleKeywords.json :: dataList[id=MeleeCover].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with the 'Melee Support' Skill against the same enemy that attacked Unit A. Activates at Unit A's Skill End.\n- The Skill used due to the 'Melee Support' effect does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością „Wsparcie z Bliska” przeciwko temu samemu wrogowi, który zaatakował A. Aktywuje się po zakończeniu Umiejętności A.\n- Umiejętność użyta dzięki efektowi „Wsparcie z Bliska” nie wpływa na nadchodzącą listę Umiejętności B
332. [Słowo kluczowe [RequestedTarget] — nazwa] 의뢰 대상
   źródło: BattleKeywords.json :: dataList[id=RequestedTarget].name
   kontekst: identyfikator tagu w tekstach: `[RequestedTarget]`
   limit: do 40 znaków
   EN: Requested Target
   PL: Cel Zlecenia
333. [Słowo kluczowe [RequestedTarget] — opis] 참격, 관통, 타격 중 1.5 이하인 내성 +0.2. 이 버프가 부여된 대상을 처치하면, 모든 E.G.O 자원을 1 얻고 처치한 대상의 정신력을 10 회복시킴
   źródło: BattleKeywords.json :: dataList[id=RequestedTarget].desc
   limit: do 250 znaków
   EN: +0.2 Resistance to Attack Types with 1.5 or less Resistance. If the target with this effect is defeated, gain 1 E.G.O resource for all Affinities, and the unit that defeated the target heals 10 SP
   PL: Jeśli cel z tym wzmocnieniem zostanie pokonany, pokonujący zyskuje po 1 zasobu E.G.O każdego atrybutu i regeneruje 10 Poczytalności
334. [Słowo kluczowe [GlowingLantern] — nazwa] 미끼 요정
   źródło: BattleKeywords.json :: dataList[id=GlowingLantern].name
   kontekst: identyfikator tagu w tekstach: `[GlowingLantern]`
   limit: do 40 znaków
   EN: Fairy Lure
   PL: Wabik Wróżek
335. [Słowo kluczowe [GlowingLantern] — opis] - 최댓값 5\n- 턴 시작 시 조작 패널에서 가장 왼쪽 슬롯이 도발치 10 얻음\n- 자신의 받는 피해량 + 50%\n- 피격 시 대상에게 파열 1 부여 (대상의 스킬당 최대 3회)\n· 자신의 체력이 최대 체력의 50% 미만이면, 파열 1 추가 부여\n· 대상의 파열 위력이 15 이상이면, 이 효과로 파열을 부여하지 않음\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=GlowingLantern].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: leftmost Slot on the Dashboard gains +10 Aggro\n- Take +50% damage\n- When hit, inflict 1 Rupture against the Attacker (3 times per target's Skill)\n· At less than 50% HP, inflict 1 additional Rupture\n· If the target has 15+ Rupture, this effect does not inflict Rupture\n- Reduced by 1 at Turn End
   PL: - Maks.: 5\n- Na początku tury skrajnie lewy slot na panelu zyskuje +10 Wartości Prowokacji\n- Otrzymywane obrażenia +50%\n- Przy trafieniu nadaje atakującemu 1 Rozdarcia (do 3 razy na Umiejętność atakującego)\n· Przy HP poniżej 50% dodatkowo nadaje 1 Rozdarcia\n· Przy 15 lub więcej Mocy Rozdarcia atakującego ten efekt nie nadaje Rozdarcia\n- Na koniec tury maleje o 1
336. [Słowo kluczowe [HoldingBreath] — nazwa] 깊은 들숨
   źródło: BattleKeywords.json :: dataList[id=HoldingBreath].name
   kontekst: identyfikator tagu w tekstach: `[HoldingBreath]`
   limit: do 40 znaków
   EN: Deep Inhale
   PL: Głęboki Wdech
337. [Słowo kluczowe [HoldingBreath] — opis] - 최댓값 : 20\n- 크리티컬 발동 시 호흡 위력이 15, 호흡 횟수가 5 이상이면, 호흡 위력을 (보유한 호흡 위력/5)만큼 소모하여 크리티컬 피해량이 (소모한 값 x 4)%만큼 증가하고 수치 1 소모
   źródło: BattleKeywords.json :: dataList[id=HoldingBreath].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- On Crit, at 15+ Poise Potency and 5+ Poise Count, consume (Poise Potency on self / 5) Poise Potency to deal +(Poise Potency consumed x 4)% damage on Critical Hit and lose 1 Stack
   PL: - Maks.: 20\n- Przy trafieniu krytycznym, przy 15 lub więcej Mocy Oddechu i 5 lub więcej Liczników Oddechu, zużywa (Moc Oddechu/5) Mocy Oddechu, by zadać +(zużyta wartość x 4)% obrażeń krytycznych, a wartość maleje o 1
338. [Słowo kluczowe [HoldingBreath] — podsumowanie] 크리티컬 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=HoldingBreath].summary
   limit: do 120 znaków
   EN: Deal more Damage on Critical Hit
   PL: Zadaje więcej obrażeń krytycznych
339. [Słowo kluczowe [NebulizerInhale] — nazwa] 네뷸라이저 β
   źródło: BattleKeywords.json :: dataList[id=NebulizerInhale].name
   kontekst: identyfikator tagu w tekstach: `[NebulizerInhale]`
   limit: do 40 znaków
   EN: Nebulizer β
   PL: Nebulizer β
340. [Słowo kluczowe [NebulizerInhale] — opis] - 최댓값 : 5\n- 이 효과는 이번 전투 동안 유지됨\n- 오만 완전 공명을 발동하였다면 전투 시작 시, 자신과 무작위 아군 (스택)명이 호흡 3 얻고 호흡 횟수 3 증가 (호흡 또는 호흡 횟수를 스스로 사용하거나 획득하는 스킬을 보유한 아군 중 호흡 위력이 낮은 대상에게 우선 적용)
   źródło: BattleKeywords.json :: dataList[id=NebulizerInhale].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- This effect persists throughout the Encounter\n- When activating Pride A-Reson.: on Combat Start, apply 3 Poise and +3 Poise Count on self and (Stack) allies (prioritizes allies that gain or use Poise or Poise Count; among them, prioritize allies with the least Poise Potency)
   PL: - Maks.: 5\n- Efekt utrzymuje się przez całą walkę\n- Po aktywacji Pełnego Rezonansu Pychy: na początku walki nadaje 3 Oddechu i 3 Liczniki Oddechu sobie oraz (stosy) losowym sojusznikom (priorytet dla sojuszników z Umiejętnościami używającymi lub zyskującymi Oddech; wśród nich dla tych z najniższą Mocą Oddechu)
341. [Słowo kluczowe [NebulizerInhale] — podsumowanie] 호흡 위력 얻음, 호흡 횟수 증가
   źródło: BattleKeywords.json :: dataList[id=NebulizerInhale].summary
   limit: do 120 znaków
   EN: Gain Poise and Poise Count
   PL: Zyskuje Moc Oddechu, Licznik Oddechu rośnie
342. [Słowo kluczowe [Hohenheim_LowMorale] — nazwa] 고뇌
   źródło: BattleKeywords.json :: dataList[id=Hohenheim_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Hohenheim_LowMorale]`
   limit: do 40 znaków
   EN: Anguish
   PL: Udręka
343. [Słowo kluczowe [Hohenheim_LowMorale] — opis] 턴 시작 시, 취약 1, 정신력 회복 효율 감소 2 얻음
   źródło: BattleKeywords.json :: dataList[id=Hohenheim_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: gain 1 Fragile and 2 SP Heal Efficiency Down
   PL: Na początku tury zyskuje 1 Wrażliwości i 2 Spadki Wydajności Leczenia Poczytalności
344. [Słowo kluczowe [Hohenheim_Panic] — nazwa] 고뇌
   źródło: BattleKeywords.json :: dataList[id=Hohenheim_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Hohenheim_Panic]`
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Słowo kluczowe [Hohenheim_Panic] — opis] 턴 시작 시, 취약 2 정신력 회복 효율 감소 3 얻음
   źródło: BattleKeywords.json :: dataList[id=Hohenheim_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: gain 2 Fragile and 3 SP Heal Efficiency Down
   PL: Na początku tury zyskuje 2 Wrażliwości i 3 Spadki Wydajności Leczenia Poczytalności
346. [Słowo kluczowe [BlackCloud] — nazwa] 검은 구름
   źródło: BattleKeywords.json :: dataList[id=BlackCloud].name
   kontekst: identyfikator tagu w tekstach: `[BlackCloud]`
   limit: do 40 znaków
   EN: Dark Cloud
   PL: Czarna Chmura
347. [Słowo kluczowe [BlackCloud] — opis] 최댓값 : 1\n이번 턴에 자신이 사용하는 기본 공격 스킬의 코인이 파괴 불가 코인으로 변경되며, 해당 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않고, 코인에서 적에게 부여하는 출혈 효과의 값 +1\n합 패배시 최종 위력 3 증가\n턴 종료시 버프 소멸
   źródło: BattleKeywords.json :: dataList[id=BlackCloud].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nConverts all of this unit's Base Attack Skill Coins used this turn to Unbreakable Coins, prevents damage from Staggering this unit until Skill End, and inflict +1 more of Bleed effects\nOn Clash Lose: gain Final Power +3\nTurn End: this effect expires
   PL: Maks.: 1\nZamienia wszystkie monety bazowych Umiejętności ataku użytych w tej turze w Monety Niezniszczalne, do końca Umiejętności chroni przed oszołomieniem od obrażeń i zwiększa o 1 wartość Krwawienia nadawanego monetami\nPo przegranej w Starciu: Moc Końcowa +3\nNa koniec tury wzmocnienie znika
348. [Słowo kluczowe [BlackCloud] — podsumowanie] 공격 스킬이 [파괴 불가 코인]으로 변경되고 효과가 강화됨.
   źródło: BattleKeywords.json :: dataList[id=BlackCloud].summary
   limit: do 120 znaków
   EN: Converts Attack Skill to Unbreakable Coin and gains a new effect
   PL: Zamienia Umiejętność ataku w Monetę Niezniszczalną i zyskuje nowy efekt.
349. [Słowo kluczowe [BlackCloudBlade] — nazwa] 흑운도
   źródło: BattleKeywords.json :: dataList[id=BlackCloudBlade].name
   kontekst: identyfikator tagu w tekstach: `[BlackCloudBlade]`
   limit: do 40 znaków
   EN: Dark Cloud Blade
   PL: Ostrze Czarnej Chmury
350. [Słowo kluczowe [BlackCloudBlade] — opis] 최댓값 : 1\n참격 위력 1 증가 \n참격 스킬로 공격 적중시 출혈 1 부여
   źródło: BattleKeywords.json :: dataList[id=BlackCloudBlade].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nGain 1 Slash Power\nInflict 1 Bleed On Hit with Slash Skills
   PL: Maks.: 1\nWzrost Mocy Cięcia +1\nPrzy trafieniu Umiejętnością Cięcia nadaje 1 Krwawienia
351. [Słowo kluczowe [BlackCloudBlade] — podsumowanie] 참격 스킬 강화
   źródło: BattleKeywords.json :: dataList[id=BlackCloudBlade].summary
   limit: do 120 znaków
   EN: Enhance Slash Skills
   PL: Wzmacnia Umiejętności Cięcia
352. [Słowo kluczowe [EngageToBattle] — nazwa] 임전
   źródło: BattleKeywords.json :: dataList[id=EngageToBattle].name
   kontekst: identyfikator tagu w tekstach: `[EngageToBattle]`
   limit: do 40 znaków
   EN: Battle Ready
   PL: Gotowość Bojowa
353. [Słowo kluczowe [EngageToBattle] — opis] 최댓값 : 1\n자신의 스킬, 코인 효과로 출혈 위력, 횟수를 부여할 때 부여하는 값 +1\n이번 전투 동안 참격 위력 증가 1, 참격 피해량 증가 3 얻음
   źródło: BattleKeywords.json :: dataList[id=EngageToBattle].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Value: 1\nBleed Potency and Count inflicted using this unit's Skill or Coin effects: +1\nGain 1 Slash Power Up and 3 Slash DMG Up for the duration of this Encounter
   PL: Maks.: 1\nMoc i Licznik Krwawienia nadawane efektami własnych Umiejętności lub monet: +1\nW tej walce zyskuje 1 Wzrost Mocy Cięcia i 3 Wzrosty Obrażeń Cięcia
354. [Słowo kluczowe [EngageToBattle] — podsumowanie] 참격 스킬 강화, 출혈 부여량 증가.
   źródło: BattleKeywords.json :: dataList[id=EngageToBattle].summary
   limit: do 120 znaków
   EN: Enhance Slash Skills and inflict more Bleed
   PL: Wzmacnia Umiejętności Cięcia i nadaje więcej Krwawienia.
355. [Słowo kluczowe [CloudWall] — nazwa] 구름 장벽
   źródło: BattleKeywords.json :: dataList[id=CloudWall].name
   kontekst: identyfikator tagu w tekstach: `[CloudWall]`
   limit: do 40 znaków
   EN: Cumulus Wall
   PL: Mur z Chmur
356. [Słowo kluczowe [CloudWall] — opis] 최댓값 : 1\n수비 스킬 최종 위력 +1\n‘뒷골목의 규칙’으로 공격 종료시 또는 턴 종료시 버프 소멸
   źródło: BattleKeywords.json :: dataList[id=CloudWall].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\nDefense Skill Final Power +1\nThis effect expires at Turn End or Attack End of the following: 'Rules of the Backstreets'
   PL: Maks.: 1\nMoc Końcowa Umiejętności obrony +1\nWzmocnienie znika po zakończeniu ataku lub na koniec tury po użyciu „Zasad Podwórza”
357. [Słowo kluczowe [CloudWall] — podsumowanie] 수비 스킬 강화
   źródło: BattleKeywords.json :: dataList[id=CloudWall].summary
   limit: do 120 znaków
   EN: Enhance Defense Skill
   PL: Wzmacnia Umiejętności obrony
358. [Słowo kluczowe [ScarletResultUp] — nazwa] 색욕 위력 증가
   źródło: BattleKeywords.json :: dataList[id=ScarletResultUp].name
   kontekst: identyfikator tagu w tekstach: `[ScarletResultUp]`
   limit: do 40 znaków
   EN: Lust Power Up
   PL: Wzrost Mocy Żądzy
359. [Słowo kluczowe [ScarletResultUp] — opis] 이번 턴 동안 색욕 속성 스킬의 최종 위력이 수치만큼 증가
   źródło: BattleKeywords.json :: dataList[id=ScarletResultUp].desc
   limit: do 120 znaków
   EN: Lust Skills gain Final Power by the effect’s Count for one turn.
   PL: W tej turze Moc Końcowa Umiejętności Żądzy rośnie o wartość efektu
360. [Słowo kluczowe [NebulizerExhale] — nazwa] 네뷸라이저 α
   źródło: BattleKeywords.json :: dataList[id=NebulizerExhale].name
   kontekst: identyfikator tagu w tekstach: `[NebulizerExhale]`
   limit: do 40 znaków
   EN: Nebulizer α
   PL: Nebulizer α
361. [Słowo kluczowe [NebulizerExhale] — opis] - 최댓값 : 5\n- 이 효과는 이번 전투 동안 유지됨\n- 전투 시작시 자신을 포함한 모든 아군이 호흡 위력 1 얻고, 호흡 횟수 1 증가
   źródło: BattleKeywords.json :: dataList[id=NebulizerExhale].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- This effect persists throughout the Encounter\n- Combat Start: on all allies, including this unit, apply 1 Poise Potency and +1 Poise Count
   PL: - Maks.: 5\n- Efekt utrzymuje się przez całą walkę\n- Na początku walki wszyscy sojusznicy, łącznie z tą jednostką, zyskują 1 Mocy Oddechu i 1 Licznika Oddechu
362. [Słowo kluczowe [ReleaseBreath] — nazwa] 가쁜 날숨
   źródło: BattleKeywords.json :: dataList[id=ReleaseBreath].name
   kontekst: identyfikator tagu w tekstach: `[ReleaseBreath]`
   limit: do 40 znaków
   EN: Shallow Exhale
   PL: Przyspieszony Wydech
363. [Słowo kluczowe [ReleaseBreath] — opis] - 최댓값 : 1\n- 자신의 호흡 위력이 20 이상이면, 자신의 스킬, 코인 효과로 호흡 위력을 얻을 때, 횟수 1 증가.\n- 턴 종료 시 소멸
   źródło: BattleKeywords.json :: dataList[id=ReleaseBreath].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- At 20+ Poise Potency, gain +1 Count as well whenever this unit gains Poise Potency with Skill and Coin effects\n- Expires at Turn End
   PL: - Maks.: 1\n- Przy 20 lub więcej Mocy Oddechu zyskuje dodatkowo 1 Licznika Oddechu za każdym razem, gdy zyskuje Moc Oddechu efektami Umiejętności lub monet\n- Znika na koniec tury
364. [Słowo kluczowe [FirePunchFuel] — nazwa] 12구산 연료
   źródło: BattleKeywords.json :: dataList[id=FirePunchFuel].name
   kontekst: identyfikator tagu w tekstach: `[FirePunchFuel]`
   limit: do 40 znaków
   EN: District 12 Fuel
   PL: Paliwo Dystryktu 12
365. [Słowo kluczowe [FirePunchFuel] — opis] 최댓값: 100\n특정 스킬 사용 시 연료가 소모됨.\n수치가 50 이하가 되면, 과열 연료가 됨
   źródło: BattleKeywords.json :: dataList[id=FirePunchFuel].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 100\nConsumed by certain Skills.\nAt 50- Stack, become Overheated Fuel
   PL: Maks.: 100\nZużywane przez określone Umiejętności.\nPrzy 50 lub mniej stosach staje się Przegrzanym Paliwem
366. [Słowo kluczowe [FirePunchFuelOverheated] — nazwa] 과열 연료
   źródło: BattleKeywords.json :: dataList[id=FirePunchFuelOverheated].name
   kontekst: identyfikator tagu w tekstach: `[FirePunchFuelOverheated]`
   limit: do 40 znaków
   EN: Overheated Fuel
   PL: Przegrzane Paliwo
367. [Słowo kluczowe [FirePunchFuelOverheated] — opis] 최댓값: 100\n과열 연료 상태에서 12구산 연료를 소모 시, 대신 과열 연료가 소모됨\n이 연료를 소모 시, 12구산 연료가 소모된 것으로 판정됨\n수치가 50 초과시, 12구산 연료가 됨
   źródło: BattleKeywords.json :: dataList[id=FirePunchFuelOverheated].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 100\nConsuming District 12 Fuel in Overheated Fuel State consumes Overheated Fuel instead\nConsuming Overheated Fuel counts as consuming District 12 Fuel\nAt over 50 Stack, become District 12 Fuel
   PL: Maks.: 100\nZużycie Paliwa z Dystryktu 12 w stanie Przegrzanego Paliwa zużywa zamiast tego Przegrzane Paliwo\nZużycie Przegrzanego Paliwa liczy się jak zużycie Paliwa z Dystryktu 12\nPowyżej 50 stosów staje się Paliwem z Dystryktu 12
368. [Słowo kluczowe [DianxueDonQuixote] — nazwa] 점혈 - 돈키호테
   źródło: BattleKeywords.json :: dataList[id=DianxueDonQuixote].name
   kontekst: identyfikator tagu w tekstach: `[DianxueDonQuixote]`
   limit: do 40 znaków
   EN: Nerve Strike - Don Quixote
   PL: Punkt Witalny - Don Kichot
369. [Słowo kluczowe [DianxueDonQuixote] — opis] - 최댓값 : 3\n- 점혈을 부여한 캐릭터가 대상(또는 부위)의 점혈 수치에 따라 다음 효과를 얻음\n· 1스택 : 합 위력 +1\n· 2스택 : 기본 위력 +1\n· 3스택 : 합 위력 +1, 기본 위력 +1\n- 부여한 캐릭터가 다른 대상(또는 부위)에게 이 효과를 부여하면 소멸\n- 다른 캐릭터의 점혈이 부여될 경우, 교체됨 (수치 유지)
   źródło: BattleKeywords.json :: dataList[id=DianxueDonQuixote].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- The unit that inflicted this Nerve Strike gains the following effects based on target's (or targeted Part's) Nerve Strike Stack\n· 1x Stack: Gain Clash Power +1\n· 2x Stack: Gain Base Power +1\n· 3x Stack: Gain Clash Power +1 and Base Power +1\n- Expires if the unit that inflicted it inflicts this effect against a different target (or a different Part)\n- Replaced when another unit inflicts Nerve Strike (Stacks are preserved)
   PL: - Maks.: 3\n- Wystawca Punktu Witalnego zyskuje efekty zależne od stosów celu (lub jego części):\n· 1 stos: Moc Starcia +1\n· 2 stosy: Moc Bazowa +1\n· 3 stosy: Moc Starcia +1 i Moc Bazowa +1\n- Znika, gdy wystawca nada efekt innemu celowi (lub części)\n- Zostaje zastąpiony, gdy inna postać nada Punkt Witalny (stosy zostają zachowane)
370. [Słowo kluczowe [VengeanceBookSinclair] — nazwa] 앙갚음 장부 [싱클레어]
   źródło: BattleKeywords.json :: dataList[id=VengeanceBookSinclair].name
   kontekst: identyfikator tagu w tekstach: `[VengeanceBookSinclair]`
   limit: do 40 znaków
   EN: Book of Vengeance [Sinclair]
   PL: Rejestr Odwetu [Sinclair]
371. [Słowo kluczowe [VengeanceBookSinclair] — opis] - 최댓값 : 30\n- 피해량이 (수치)%만큼 증가 (최대 30%)\n- 수치에 따라 다음 턴에 효과 얻음\n· 10 ~ : 타격 피해량 증가 1 얻음\n· 20 ~ : 속도 최댓값 1 증가, 위력 증가 1 얻음\n· 30 : 타격 피해량 증가 2 얻음
   źródło: BattleKeywords.json :: dataList[id=VengeanceBookSinclair].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Deal more damage equal to (Stack)% (max 30%)\n- Gain the following effects next turn based on Stack:\n· At 10+ Stack: gain 1 Blunt DMG Up\n· At 20+ Stack: Max Speed +1, gain 1 Power Up\n· At 30 Stack: gain 2 Blunt DMG Up
   PL: - Maks.: 30\n- Zadawane obrażenia rosną o wartość% (maks. 30%)\n- W następnej turze zyskuje efekty zależnie od wartości:\n· 10 lub więcej: 1 Wzrost Obrażeń Uderzenia\n· 20 lub więcej: maksymalna Szybkość +1 i 1 Wzrost Mocy\n· 30: 2 Wzrosty Obrażeń Uderzenia
372. [Słowo kluczowe [VendettaMark] — nazwa] 복수 대상
   źródło: BattleKeywords.json :: dataList[id=VendettaMark].name
   kontekst: identyfikator tagu w tekstach: `[VendettaMark]`
   limit: do 40 znaków
   EN: Vendetta Mark
   PL: Cel Zemsty
373. [Słowo kluczowe [VendettaMark] — opis] - 최댓값 : 10 \n- 특정 스킬 또는 패시브에 의해 소모됨\n- 수치 1당 중지 소속 적에게 받는 피해 +2% (최대 20%)\n- 턴 종료 시 이 수치가 가장 높으면, 다음 턴에 형제자매의 앙갚음 대상 1 얻음\n(앙갚음 대상 보유 여부와 별개로 적용되며, 수치가 동일한 경우에는 남은 체력 비율이 더 높은 쪽을 대상으로 함)
   źródło: BattleKeywords.json :: dataList[id=VendettaMark].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Consumed by certain Skills or Passives\n- Take +2% damage from The Middle enemies for every Stack (max 20%)\n- Turn End: The unit that has the highest Stack of this effect gains 1 Sibling Vengeance Mark next turn\n(Counted separately from Vengeance Mark; if more than a single unit has the highest Stack of this effect, this effect targets the one that has a higher HP percentage)
   PL: - Maks.: 10\n- Zużywane przez określone Umiejętności lub pasywy\n- Otrzymuje +2% obrażeń od wrogów Korporacji Środkowego za każdą wartość (maks. 20%)\n- Na koniec tury jednostka z najwyższą wartością zyskuje 1 Celu Odwetu Rodzeństwa w następnej turze\n(liczone osobno od Celu Odwetu; przy remisie efekt dotyczy jednostki z wyższym procentem HP)
374. [Słowo kluczowe [RetaliationBookFamily] — nazwa] 형제자매의 앙갚음 대상
   źródło: BattleKeywords.json :: dataList[id=RetaliationBookFamily].name
   kontekst: identyfikator tagu w tekstach: `[RetaliationBookFamily]`
   limit: do 40 znaków
   EN: Sibling Vengeance Mark
   PL: Cel Odwetu Rodzeństwa
375. [Słowo kluczowe [RetaliationBookFamily] — opis] - 최댓값 : 1\n- 턴 종료 시, 사라짐\n- 모든 인격의 앙갚음 대상으로 취급됨
   źródło: BattleKeywords.json :: dataList[id=RetaliationBookFamily].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Expires at Turn End\n- Every Identity treats this unit as having their Vengeance Mark
   PL: - Maks.: 1\n- Znika na koniec tury\n- Wszyscy traktują tę jednostkę jak nosiciela swojego Celu Odwetu
376. [Słowo kluczowe [BirdCage] — nazwa] 달궈진 새장
   źródło: BattleKeywords.json :: dataList[id=BirdCage].name
   kontekst: identyfikator tagu w tekstach: `[BirdCage]`
   limit: do 40 znaków
   EN: Searing Birdcage
   PL: Rozgrzana Klatka
377. [Słowo kluczowe [BirdCage] — opis] - 최댓값: 5\n- 대상에게 화상이 있으면, 수치당 분노 내성 +0.1 (이 효과로 분노 내성은 2.0 초과가 될 수 없음)\n- 턴 종료 시, 다음 턴에 속박을 수치만큼 얻음\n- 턴 종료 시 수치 반으로 감소 (소수점 버림)\n※ 이 효과는 갱신되지 않음
   źródło: BattleKeywords.json :: dataList[id=BirdCage].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\nIf this unit has Burn, Wrath Resistance +0.1 for every Stack (cannot exceed 2.0 Wrath Resistance with this effect)\nTurn End: gain Bind equal to Stack next turn\nTurn End: halve Stack (rounded down)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: Maks.: 5\nJeśli jednostka ma Podpalenie, +0,1 Odporności na Gniew za każdą wartość (tym efektem Odporność nie przekroczy 2,0)\nNa koniec tury zyskuje w następnej turze Spętania równe wartości\nNa koniec tury wartość maleje o połowę (zaokrąglona w dół)\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny
378. [Słowo kluczowe [BirdCage] — podsumowanie] 수치당 분노 내성 +0.1
   źródło: BattleKeywords.json :: dataList[id=BirdCage].summary
   limit: do 120 znaków
   EN: Wrath Resistance +0.1 for every Stack
   PL: +0,1 Odporności na Gniew za każdą wartość
379. [Słowo kluczowe [WideAreaRampage] — nazwa] 광역 난사
   źródło: BattleKeywords.json :: dataList[id=WideAreaRampage].name
   kontekst: identyfikator tagu w tekstach: `[WideAreaRampage]`
   limit: do 40 znaków
   EN: Unfocused Volley
   PL: Ostrzał Bez Celowania
380. [Słowo kluczowe [WideAreaRampage] — opis] - 이 스킬의 코인을 굴릴 때, 공격 대상 중에 하나를 무작위로 선택해 공격\n· 첫 코인은 반드시 메인 공격 대상에게 적중함\n· 모든 적중시 효과, 해당 코인의 피해는 위 효과에서 선택된 공격 대상에게만 적용됨
   źródło: BattleKeywords.json :: dataList[id=WideAreaRampage].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When this Skill flips Coins, each Coin flips against a random enemy among its targets\n· The first Coin always targets the main target\n· All 'On Hit' effects and all damage dealt by each Coin are inflicted only against the random target the Coin selected
   PL: - Przy rzucie monetami tej Umiejętności każda moneta trafia losowo wybranego wroga spośród celów ataku\n· Pierwsza moneta zawsze trafia główny cel\n· Wszystkie efekty przy trafieniu i obrażenia danej monety dotyczą wyłącznie losowego celu wybranego przez tę monetę
381. [Słowo kluczowe [WideAreaRampage] — podsumowanie] 공격 대상 중 하나를 무작위로 선택해 공격
   źródło: BattleKeywords.json :: dataList[id=WideAreaRampage].summary
   limit: do 120 znaków
   EN: Attack indiscriminately among selected targets
   PL: Atakuje losowo wybrany cel spośród wybranych celów
382. [Słowo kluczowe [ActivatedEgoPassive] — nazwa] E.G.O 패시브
   źródło: BattleKeywords.json :: dataList[id=ActivatedEgoPassive].name
   kontekst: identyfikator tagu w tekstach: `[ActivatedEgoPassive]`
   limit: do 40 znaków
   EN: E.G.O Passives
   PL: Pasywy E.G.O
383. [Słowo kluczowe [ActivatedEgoPassive] — opis] 현재 적용 중인 E.G.O 패시브
   źródło: BattleKeywords.json :: dataList[id=ActivatedEgoPassive].desc
   limit: do 120 znaków
   EN: Active E.G.O Passives
   PL: Aktywne pasywy E.G.O
384. [Słowo kluczowe [BurstPoison] — nazwa] 주살【독】
   źródło: BattleKeywords.json :: dataList[id=BurstPoison].name
   kontekst: identyfikator tagu w tekstach: `[BurstPoison]`
   limit: do 40 znaków
   EN: Deathrite【Venom】
   PL: Obrzęd Śmierci【Jad】
385. [Słowo kluczowe [BurstPoison] — opis] 기본값: 5\n- 주살\n- 대상에게 크리티컬 피해를 받아 파열이 발동될 때, 1 감소\n- 버프 효과에 의해 감소할 때, 공격 레벨 감소 1 또는 방어 레벨 감소 1 얻음 (턴 당 3회 발동)\n버프 효과에 의해 감소할 때, 수치가 0이면, (파열 위력)만큼 탐식 피해를 받음\n- ※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords.json :: dataList[id=BurstPoison].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 5\n- Deathrite\n- When getting Rupture triggered by a Critical Hit from the target, lose 1 Stack\n- When losing Stacks due to this effect, gain 1 Offense Level Down or 1 Defense Level Down (3 times per turn)\n- When losing Stacks due to this effect, if the Stack drops to 0, take Gluttony damage equal to Rupture Potency on self\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 5\n- Obrzęd Śmierci\n- Gdy cel wyzwoli Rozdarcie trafieniem krytycznym, wartość maleje o 1\n- Przy utracie stosów od tego efektu zyskuje 1 Spadek Poziomu Ataku lub 1 Spadek Poziomu Obrony (do 3 razy na turę)\nPrzy utracie stosów od tego efektu, gdy wartość spadnie do 0, otrzymuje obrażenia Obżarstwem równe własnej Mocy Rozdarcia\n- ※ Efekt nie ulega odnowieniu, dopóki jest aktywny.
386. [Słowo kluczowe [SnakeStance] — nazwa] 사완
   źródło: BattleKeywords.json :: dataList[id=SnakeStance].name
   kontekst: identyfikator tagu w tekstach: `[SnakeStance]`
   limit: do 40 znaków
   EN: Serpent Arm
   PL: Wężowe Ramię
387. [Słowo kluczowe [SnakeStance] — opis] 최댓값: 3\n턴 종료 시, 다음 턴에 호흡 3 얻음, 호흡 횟수 2 증가\n기본 공격 스킬 사용시 대상에게 파열이 있으면, 호흡 5 얻음\n턴 종료 시, 1 감소
   źródło: BattleKeywords.json :: dataList[id=SnakeStance].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nTurn End: gain 3 Poise and +2 Poise Count next turn\nOn Base Attack Skill use, if target has Rupture, gain 5 Poise\nTurn End: lose 1 Stack
   PL: Maks.: 3\nNa koniec tury zyskuje w następnej turze 3 Oddechu i 2 Liczniki Oddechu\nPrzy użyciu bazowej Umiejętności ataku, jeśli cel ma Rozdarcie, zyskuje 5 Oddechu\nNa koniec tury maleje o 1
388. [Słowo kluczowe [BurstZilu] — nazwa] 주살【파】
   źródło: BattleKeywords.json :: dataList[id=BurstZilu].name
   kontekst: identyfikator tagu w tekstach: `[BurstZilu]`
   limit: do 40 znaków
   EN: Deathrite 【Fissure】
   PL: Obrzęd Śmierci 【Szczelina】
389. [Słowo kluczowe [BurstZilu] — opis] - 기본값 : 3\n- 자신에게 주살이 있는 상태에서 파열이 발동될 때, 수치가 1 감소하고, 다음 턴에 속박 1 부여\n· 해당 효과가 발동할 때 자신에게 다음 턴에 부여되는 속박이 3 이상이면, 속박 부여 대신 수치 2 감소\n- 수치가 0이 될 때, (파열 위력)만큼 탐식 피해를 받음\n※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords.json :: dataList[id=BurstZilu].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- When getting Rupture triggered while this unit has Deathrite, lose 1 Stack, and gain 1 Bind next turn\n· When this effect activates, if this unit is to gain 3 or more Bind next turn, lose 2 Stacks instead of gaining Bind\n- At 0 Stack, take Gluttony damage equal to Rupture Potency on self\n※ Cannot gain additional Stacks of this effect while it is already active.
   PL: - Wartość bazowa: 3\n- Gdy Rozdarcie zostanie wyzwolone, podczas gdy jednostka ma Obrzęd Śmierci, wartość maleje o 1, a w następnej turze zyskuje 1 Spętania\n· Jeśli przy aktywacji tego efektu jednostka ma otrzymać 3 lub więcej Spętań w następnej turze, zamiast Spętań wartość maleje o 2\n- Gdy wartość spadnie do 0, otrzymuje obrażenia Obżarstwem równe własnej Mocy Rozdarcia\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny.
390. [Słowo kluczowe [SupportProtect] — nazwa] 원호 방어
   źródło: BattleKeywords.json :: dataList[id=SupportProtect].name
   kontekst: identyfikator tagu w tekstach: `[SupportProtect]`
   limit: do 40 znaków
   EN: Assist Defense
   PL: Obrona Wsparcia
391. [Słowo kluczowe [SupportProtect] — opis] - 최댓값 : 3\n- 아군이 적에게 일방공격 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고, 원호 방어 전용 스킬 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 발동\n- 수비 스킬을 장착한 아군에게는 발동하지 않음\n- 턴 종료시 소멸
   źródło: BattleKeywords.json :: dataList[id=SupportProtect].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When an ally is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then, use the unique Skill that activates for Assist Defense\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- Does not activate for allies who equipped Defense Skills\n- Expires at Turn End
   PL: - Maks.: 3\n- Gdy sojusznik ma zostać zaatakowany atakiem niekwestionowanym wroga, zużywa 1 wartości, by przekierować cel ataku wroga na siebie, i używa specjalnej Umiejętności Obrony Wsparcia\n- Gdy Obrona Wsparcia jest u wielu sojuszników, pierwszeństwo ma ten z najwyższą wartością\n- Nie aktywuje się dla sojuszników z wyposażoną Umiejętnością obronną\n- Znika na koniec tury
392. [Słowo kluczowe [EnhanceZilu] — nazwa] 천구성도
   źródło: BattleKeywords.json :: dataList[id=EnhanceZilu].name
   kontekst: identyfikator tagu w tekstach: `[EnhanceZilu]`
   limit: do 40 znaków
   EN: Tianjiu Star's Blade
   PL: Ostrze Gwiazdy Tianjiu
393. [Słowo kluczowe [EnhanceZilu] — opis] - 최대값 : 20\n- 수치가 10 이상이면, 턴 종료 시 다음 턴에 신속 1 얻음\n- 특정 스킬에 사용됨
   źródło: BattleKeywords.json :: dataList[id=EnhanceZilu].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- At 10+ Stack: at Turn End, gain 1 Haste next turn\n- Used for certain Skills
   PL: - Maks.: 20\n- Przy 10+ stosach: na koniec tury zyskuje 1 Pośpiechu w następnej turze\n- Zużywane przez określone Umiejętności
394. [Słowo kluczowe [BurstVulnerableZilu] — nazwa] 붕괴 표식
   źródło: BattleKeywords.json :: dataList[id=BurstVulnerableZilu].name
   kontekst: identyfikator tagu w tekstach: `[BurstVulnerableZilu]`
   limit: do 40 znaków
   EN: Mark of Decay
   PL: Znak Rozkładu
395. [Słowo kluczowe [BurstVulnerableZilu] — opis] - 최대값 : 1\n- 탐식 속성 스킬로 받는 피해량 +10%\n- 주살로 받는 피해량 +10%\n- 턴 종료 시 제거
   źródło: BattleKeywords.json :: dataList[id=BurstVulnerableZilu].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take +10% damage from Gluttony Skills\n- Take +10% damage from Deathrite\n- Removed at Turn End
   PL: - Maks.: 1\n- Otrzymuje +10% obrażeń od Umiejętności Obżarstwa\n- Otrzymuje +10% obrażeń od Obrzędu Śmierci\n- Usuwany na koniec tury
396. [Słowo kluczowe [SupportProtectTypo] — nazwa] 원호 방어
   źródło: BattleKeywords.json :: dataList[id=SupportProtectTypo].name
   kontekst: identyfikator tagu w tekstach: `[SupportProtectTypo]`
   (powtórzenie elementu 390 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
397. [Słowo kluczowe [EntangledCurseTalisman] — nazwa] 얽혀버린 저주 부적
   źródło: BattleKeywords.json :: dataList[id=EntangledCurseTalisman].name
   kontekst: identyfikator tagu w tekstach: `[EntangledCurseTalisman]`
   limit: do 40 znaków
   EN: Twisted Curse Talisman
   PL: Spleciony Talizman Klątwy
398. [Słowo kluczowe [EntangledCurseTalisman] — opis] - 최댓값 : 10\n- 턴 종료 시 제거\n- 수치가 10 이상이면, 스킬 피해로 30 이상의 피해를 받았을 때 파열 횟수 1 증가, 파열 위력만큼 탐식 피해받음 (턴 당 1회)\n- 이 효과가 제거될 때 다음 턴에 (수치/4)만큼 공격 위력 감소 부여 (최대 2)\n※ 이 효과는 갱신되지 않음
   źródło: BattleKeywords.json :: dataList[id=EntangledCurseTalisman].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Expires at Turn End\n- At 10+ Stack, when taking 30+ damage from a Skill: gain +1 Rupture Count; take Gluttony damage equal to Rupture Potency on self (once per turn)\n- When this effect expires, gain (Stack / 4) Attack Power Down next turn (max 2)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Maks.: 10\n- Usuwany na koniec tury\n- Przy 10 lub więcej stosach, przy otrzymaniu 30 lub więcej obrażeń od Umiejętności: 1 Licznik Rozdarcia i obrażenia Obżarstwem równe własnej Mocy Rozdarcia (raz na turę)\n- Przy usunięciu zyskuje w następnej turze (wartość/4) Spadków Mocy Ataku (maks. 2)\n※ Efekt nie ulega odnowieniu, dopóki jest aktywny
399. [Słowo kluczowe [CentipedePoison] — nazwa] 지네 독
   źródło: BattleKeywords.json :: dataList[id=CentipedePoison].name
   kontekst: identyfikator tagu w tekstach: `[CentipedePoison]`
   limit: do 40 znaków
   EN: Centipede Venom
   PL: Trucizna Skolopendry
400. [Słowo kluczowe [CentipedePoison] — opis] - 최댓값: 20\n- 턴 종료 시 (수치/4)만큼 다음 턴에 방어 레벨 감소 얻음 (소수점 버림)\n- 턴 종료 시 수치만큼 탐식 피해를 받고, 수치가 반으로 감소 (소수점 버림)\n사망시, 이 유닛 아군 중 지네 독이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 위력만큼 옮겨감
   źródło: BattleKeywords.json :: dataList[id=CentipedePoison].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- Turn End: Gain (Stack / 4) Defense Level Down next turn (rounded down)\n- Turn End: Take Gluttony damage equal to Stack, and halve the Stack (rounded down)\nUpon death, transfers to this unit's ally (for Focused Encounters, a different Part) that has none or the least Centipede Venom Stacks.
   PL: - Maks.: 20\n- Na koniec tury zyskuje w następnej turze (stosy/4) Spadków Poziomu Obrony (zaokrąglone w dół)\n- Na koniec tury otrzymuje obrażenia Obżarstwem równe wartości, a wartość maleje o połowę (zaokrąglona w dół)\nPo śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Trucizny Skolopendry lub z jej najmniejszą liczbą
401. [Słowo kluczowe [DragonLance] — nazwa] 매화첨[埋花櫼]
   źródło: BattleKeywords.json :: dataList[id=DragonLance].name
   kontekst: identyfikator tagu w tekstach: `[DragonLance]`
   limit: do 40 znaków
   EN: Flower-burying Wedge [埋花櫼]
   PL: Klin Pogrzebania Kwiatów [埋花櫼]
402. [Słowo kluczowe [DragonLance] — opis] 기본값: 0\n최댓값: 3\n- 자신의 조작 패널에서 가장 왼쪽의 기본 공격 스킬이 파괴 불가 코인이 됨\n- 턴 시작 시 수치당 공격 레벨 증가 2, 방어 레벨 감소 2 얻음\n- 턴 시작 시 수치가 3 이상이면, 오혈 1 얻음 (전투당 1회)\n- 턴 종료 시 1 증가\n※ 위 효과만으로 증가할 수 있음\n- 사망, 퇴각 시 제거됨\n\n- 이번 턴에 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않고, 피해로 인한 흐트러짐 상태를 해제함.\n이후 해당 턴 동안 피해로 인해 흐트러지거나 사망하지 않고, 해당 턴의 마지막 순서에 '오혈읍루 - 종'스킬을 사용함. 해당 스킬 종료 시 매화첨 제거.\n턴 종료시 체력이 1이 되는 피해를 받은 경우, 다음 턴에 속도에 따라 '오혈읍루 - 종'스킬 사용.
   źródło: BattleKeywords.json :: dataList[id=DragonLance].desc
   limit: do 1070 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 0\nMax Stack: 3\n- All Coins on this unit's leftmost Base Attack Skill on the Dashboard become Unbreakable Coins\n- Turn Start: gain 2 Offense Level Up and 2 Defense Level Down for every Stack\n- Turn Start: at 3+ Stack, gain 1 Tarnished Blood (once per Encounter)\n- Turn End: gain 1 Stack\n※ Cannot raise the effect's Stack by any other means than the ones above\n- Expires upon death or Retreat\n\n- When this unit takes damage that brings their HP down to 0: instead of letting this unit's HP drop below 1, or becoming Staggered or Defeated, use the 'Tears of the Tarnished Blood - The End' Skill at the very end of that turn. Remove the Flower-burying Wedge when the Skill ends.\nWhen this unit takes damage that brings their HP down to 1 at Turn End, use 'Tears of the Tarnished Blood - The End' Skill based on this unit's Speed next turn
   PL: Wartość bazowa: 0\nMaks.: 3\n- Wszystkie monety skrajnie lewej bazowej Umiejętności ataku na panelu stają się Monetami Niezniszczalnymi\n- Na początku tury za każdą wartość: 2 Wzrosty Poziomu Ataku i 2 Spadki Poziomu Obrony\n- Na początku tury, przy wartości 3 lub wyższej, zyskuje 1 Splamionej Krwi (raz na walkę)\n- Na koniec tury wartość rośnie o 1\n※ Efekt rośnie wyłącznie dzięki powyższym regułom\n- Znika po śmierci lub Odwrócie\n\n- Gdy jednostka otrzyma obrażenia redukujące HP do 0: zamiast utraty HP poniżej 1, oszołomienia lub śmierci, używa na samym końcu tej tury Umiejętności „Łzy Splamionej Krwi - Kres”. Po zakończeniu Umiejętności Klin Pogrzebania Kwiatów znika.\nGdy na koniec tury jednostka otrzyma obrażenia redukujące HP do 1, w następnej turze użyje Umiejętności „Łzy Splamionej Krwi - Kres” według własnej Szybkości
403. [Słowo kluczowe [CondensedBlood] — nazwa] 오혈
   źródło: BattleKeywords.json :: dataList[id=CondensedBlood].name
   kontekst: identyfikator tagu w tekstach: `[CondensedBlood]`
   limit: do 40 znaków
   EN: Tarnished Blood
   PL: Splamiona Krew
404. [Słowo kluczowe [CondensedBlood] — opis] 최댓값: 5\n- 턴 종료 시 수치당 최대 체력의 20%만큼 체력 피해를 받음 (해당 피해로 인해 흐트러지지 않음)\n- 턴 종료 시 1 증가\n- 사망, 퇴각 시 제거됨
   źródło: BattleKeywords.json :: dataList[id=CondensedBlood].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 5\n- Turn End: take 20% HP damage per Stack (cannot be Staggered by this effect)\n- Gain 1 Stack at Turn End\n- Expires upon death or Retreat
   PL: Maks.: 5\n- Na koniec tury otrzymuje za każdą wartość 20% HP jako obrażenia (nie powodują oszołomienia)\n- Na koniec tury wartość rośnie o 1\n- Znika po śmierci lub Odwrócie
405. [Słowo kluczowe [YesdragonSelf] — nazwa] 매화침[埋花針]
   źródło: BattleKeywords.json :: dataList[id=YesdragonSelf].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonSelf]`
   limit: do 40 znaków
   EN: Flower-burying Pin [埋花針]
   PL: Igła Pogrzebania Kwiatów [埋花針]
406. [Słowo kluczowe [YesdragonSelf] — opis] 최댓값 : 20\n- 턴 종료시 또는 피격 시 수치 1 증가\n- 수치 5당 공격 레벨 1 증가\n- 이 버프를 보유한 캐릭터가 사망 시, 모든 적에게 수치만큼 탐식 피해를 입히고 파열 5 부여\n- 사망 시 또는 퇴각 시 버프 소멸
   źródło: BattleKeywords.json :: dataList[id=YesdragonSelf].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 20\n- Gain 1 Stack at Turn End or when hit\n- Gain 1 Offense Level per 5 Stack\n- If the unit that has this effect dies, inflict Gluttony damage equal to Stack and inflict 5 Rupture\n- Expires upon death or Retreat
   PL: Maks.: 20\n- Na koniec tury lub przy trafieniu wartość rośnie o 1\n- Za każde 5 wartości: Poziom Ataku +1\n- Po śmierci nosiciela tego wzmocnienia zadaje wszystkim wrogom obrażenia Obżarstwem równe wartości i nadaje 5 Rozdarcia\n- Znika po śmierci, Odwrócie lub na koniec tury
407. [Słowo kluczowe [YesdragonNodie] — nazwa] 불허[不許]
   źródło: BattleKeywords.json :: dataList[id=YesdragonNodie].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonNodie]`
   limit: do 40 znaków
   EN: Denial [不許]
   PL: Zakaz [不許]
408. [Słowo kluczowe [YesdragonNodie] — opis] 이번 턴에 체력이 0이 되는 피해를 받으면, 해당 턴 동안 체력이 1 미만으로 감소하지 않고, 피해로 인한 흐트러짐 상태를 해제함.\n위 효과가 발동한 경우, 턴 종료 시 사망함.\n사망 시, 퇴각 시 또는 턴 종료시 버프 소멸
   źródło: BattleKeywords.json :: dataList[id=YesdragonNodie].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When this unit takes damage that brings their HP down to 0: this unit's HP does not drop below 1; recover from Stagger due to damage.\nIf the above effect activated, dies at Turn End.\nExpires upon death, Retreat, or Turn End
   PL: Gdy jednostka otrzyma obrażenia redukujące HP do 0: jej HP nie spada poniżej 1, a oszołomienie od obrażeń zostaje wyleczone.\nJeśli powyższy efekt się aktywował, jednostka umiera na koniec tury.\nZnika po śmierci, Odwrócie lub na koniec tury
409. [Słowo kluczowe [YesdragonBurst] — nazwa] 칼날 가시
   źródło: BattleKeywords.json :: dataList[id=YesdragonBurst].name
   kontekst: identyfikator tagu w tekstach: `[YesdragonBurst]`
   limit: do 40 znaków
   EN: Razor Thorn
   PL: Ostre Ciernie
410. [Słowo kluczowe [WaitingXichun] — nazwa] 대[待]
   źródło: BattleKeywords.json :: dataList[id=WaitingXichun].name
   kontekst: identyfikator tagu w tekstach: `[WaitingXichun]`
   limit: do 40 znaków
   EN: Ready [待]
   PL: Oczekiwanie [待]
411. [Słowo kluczowe [WaitingXichun] — opis] - 최댓값: 3\n- 대기 해제 또는 복귀할 때까지 자신이 대기, 퇴각 상태였던 턴 수
   źródło: BattleKeywords.json :: dataList[id=WaitingXichun].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Number of turns this unit spent in Retreat or as a Backup unit
   PL: - Maks.: 3\n- Liczba tur spędzonych na Odwrócie lub w rezerwie
412. [Słowo kluczowe [StartXichun] — nazwa] 시[始]
   źródło: BattleKeywords.json :: dataList[id=StartXichun].name
   kontekst: identyfikator tagu w tekstach: `[StartXichun]`
   limit: do 40 znaków
   EN: Launcher [始]
   PL: Inicjator [始]
413. [Słowo kluczowe [StartXichun] — opis] - 최댓값: 6\n- 자신이 전투에 참여한 턴 수\n- 퇴각 시 제거됨\n- 턴 종료 시 1 증가
   źródło: BattleKeywords.json :: dataList[id=StartXichun].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 6\n- Number of turns this unit spent active in the Encounter\n- Expires upon Retreat\n- Gain 1 Stack at Turn End
   PL: - Maks.: 6\n- Liczba tur aktywnego udziału w walce\n- Znika przy Odwrócie\n- Na koniec tury wartość rośnie o 1
414. [Słowo kluczowe [CheerUpXichun] — nazwa] 원[援]
   źródło: BattleKeywords.json :: dataList[id=CheerUpXichun].name
   kontekst: identyfikator tagu w tekstach: `[CheerUpXichun]`
   limit: do 40 znaków
   EN: Assist [援]
   PL: Wsparcie [援]
415. [Słowo kluczowe [CheerUpXichun] — opis] - 최댓값: 1\n- 대상의 부정적인 효과가 5개 이상이면, 합 위력 +1, 피해량 +10%
   źródło: BattleKeywords.json :: dataList[id=CheerUpXichun].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- If target has 5+ types of negative effects, Clash Power +1, deal +10% damage
   PL: - Maks.: 1\n- Jeśli cel ma 5 lub więcej rodzajów negatywnych efektów: Moc Starcia +1 i zadawane obrażenia +10%
416. [Słowo kluczowe [RetreatForCommon] — nazwa] 전장 퇴각
   źródło: BattleKeywords.json :: dataList[id=RetreatForCommon].name
   kontekst: identyfikator tagu w tekstach: `[RetreatForCommon]`
   limit: do 40 znaków
   EN: Battlefield Retreat
   PL: Odwrót z Pola Bitwy
417. [Słowo kluczowe [RetreatForCommon] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)\n- 연속 전투인 경우, 퇴각 시 대기 인원에게 자신의 슬롯 수를 이전한 뒤 교체되고, 대기 인원 목록의 마지막 순서로 이동 (다음 턴에 교체 가능한 대기 인원이 없으면 이탈함. 복귀 시 퇴각 순서대로 복귀)\n- 전투 복귀 시 자신에게 부여된 일부 효과를 제외한 모든 효과 제거, 퇴각 시의 체력과 정신력이 유지됨 (정신력이 0 미만이면, 0으로 초기화)
   źródło: BattleKeywords.json :: dataList[id=RetreatForCommon].desc
   limit: do 830 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Recover from Stagger and Retreat from the Encounter (excluding forced Staggers; does not count as death)\n· In Chain Battles, give this unit's Slots to a Substituted unit and move to the rearmost place in the Backup units' Deployment order (escape from the Encounter entirely if there are no other Backup Units remaining to swap places with next turn. When returning to battle, return in the order they retreated in)\n· When returning to battle, return with the same amount of HP and SP this unit had when it retreated, and eliminate all effects on self save for a select few (if this unit had less than 0 SP when retreating, reset SP to 0 instead)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)\n- W walkach łańcuchowych przekazuje swoje sloty jednostce zastępczej i trafia na koniec kolejki rezerwowych (jeśli w następnej turze nie ma kogo zastąpić, opuszcza walkę całkowicie; przy powrocie wraca w kolejności odwrotu)\n- Wracając do walki zachowuje HP i Poczytalność z chwili odwrotu i traci wszystkie efekty poza nielicznymi wyjątkami (przy Poczytalności poniżej 0 zostaje ona wyzerowana)
418. [Słowo kluczowe [FireBulletPropellant] — nazwa] 작열 추진탄
   źródło: BattleKeywords.json :: dataList[id=FireBulletPropellant].name
   kontekst: identyfikator tagu w tekstach: `[FireBulletPropellant]`
   limit: do 40 znaków
   EN: Scorch Propellant Ammo
   PL: Żarzący się Pocisk Napędowy
419. [Słowo kluczowe [FireBulletPropellant] — opis] - 특수 탄환\n- 최댓값 : 15\n- 특정 스킬 사용 시 소모
   źródło: BattleKeywords.json :: dataList[id=FireBulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Stack : 15\n- Consumed when using certain Skills
   PL: - Szczególna amunicja\n- Maks.: 15\n- Zużywana przy użyciu określonych Umiejętności
420. [Słowo kluczowe [BulletPropellantAlly] — nazwa] 호표탄
   źródło: BattleKeywords.json :: dataList[id=BulletPropellantAlly].name
   kontekst: identyfikator tagu w tekstach: `[BulletPropellantAlly]`
   limit: do 40 znaków
   EN: Tigermark Round
   PL: Pocisk Tygrysiego Znaku
421. [Słowo kluczowe [BulletPropellantAlly] — opis] - 특수 탄환\n- 호표탄, 맹호표탄의 누적 소모 합이 8 이상이면, 패시브로 얻는 천퇴성[天退星]이 신(心) - 천퇴성[天退星]으로 변경\n- 최댓값 : 12
   źródło: BattleKeywords.json :: dataList[id=BulletPropellantAlly].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- At 8+ (cumulative sum of Tigermark Rounds and Savage Tigermark Rounds spent), gain Shin (心) - Tiantui Star [天退星] instead of Tiantui Star [天退星] from this unit's Passive\n- Max Capacity: 12
   PL: - Szczególna amunicja\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku pasyw zamiast Gwiazdy Tianhui [天退星] przyznaje Serce (心) - Gwiazdę Tianhui [天退星]\n- Maks.: 12
422. [Słowo kluczowe [BulletPropellantSpecialAlly] — nazwa] 맹호표탄
   źródło: BattleKeywords.json :: dataList[id=BulletPropellantSpecialAlly].name
   kontekst: identyfikator tagu w tekstach: `[BulletPropellantSpecialAlly]`
   limit: do 40 znaków
   EN: Savage Tigermark Round
   PL: Dziki Pocisk Tygrysiego Znaku
423. [Słowo kluczowe [BulletPropellantSpecialAlly] — opis] - 특수 탄환\n- 호표탄, 맹호표탄의 누적 소모 합이 8 이상이면, 패시브로 얻는 천퇴성[天退星]이 신(心) - 천퇴성[天退星]으로 변경\n- 호표탄의 효과가 적용됨\n- 최댓값 : 8
   źródło: BattleKeywords.json :: dataList[id=BulletPropellantSpecialAlly].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- At 8+ (cumulative sum of Tigermark Rounds and Savage Tigermark Rounds spent), gain Shin (心) - Tiantui Star [天退星] instead of Tiantui Star [天退星] from this unit's Passive\n- Activates the same way as Tigermark Round does\n- Max Capacity: 8
   PL: - Szczególna amunicja\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku pasyw zamiast Gwiazdy Tianhui [天退星] przyznaje Serce (心) - Gwiazdę Tianhui [天退星]\n- Działa tak samo jak Pocisk Tygrysiego Znaku\n- Maks.: 8
424. [Słowo kluczowe [IrritationAlly] — nazwa] 천퇴성[天退星]
   źródło: BattleKeywords.json :: dataList[id=IrritationAlly].name
   kontekst: identyfikator tagu w tekstach: `[IrritationAlly]`
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL: Gwiazda Tianhui [天退星]
425. [Słowo kluczowe [IrritationAlly] — opis] - 속도 최솟값, 최댓값 1 증가\n- 자신의 속도가 대상보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 2.5)% (최대 20%)\n- 적에게 스킬로 부여하는 진동 위력과 진동 횟수 부여값 +1\n- 소모한 호표탄, 맹호표탄 합이 8 이상이면, 턴 종료 시 다음 턴에 이 버프가 신(心) - 천퇴성[天退星]으로 변경\n- 최댓값 : 1
   źródło: BattleKeywords.json :: dataList[id=IrritationAlly].desc
   limit: do 480 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 2.5)% damage (max 20%)\n- Inflict +1 more Tremor Potency and Tremor Count with this unit's Skills\n- If this unit has spent 8+ (sum of Tigermark Round and Savage Tigermark Round): at Turn End, convert this buff to Shin (心) - Tiantui Star [天退星] next turn\n- Max Stack: 1
   PL: - Minimalna i maksymalna Szybkość +1\n- Jeśli Szybkość przewyższa cel o 3 lub więcej, zadaje +(różnica Szybkości x 2,5)% obrażeń (maks. 20%)\n- Umiejętności nadają wrogom o 1 więcej Mocy i Licznika Wstrząsu\n- Przy łącznym zużyciu 8 lub więcej Pocisków Tygrysiego Znaku i Dzikich Pocisków Tygrysiego Znaku: na koniec tury wzmocnienie zamienia się w Serce (心) - Gwiazdę Tianhui [天退星]\n- Maks.: 1
426. [Słowo kluczowe [HugeIrritationAlly] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: BattleKeywords.json :: dataList[id=HugeIrritationAlly].name
   kontekst: identyfikator tagu w tekstach: `[HugeIrritationAlly]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Serce (心) - Gwiazda Tianhui [天退星]
427. [Słowo kluczowe [HugeIrritationAlly] — opis] - 속도 최솟값, 최댓값 3 증가\n- 자신의 속도가 대상보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 40%)\n- 적에게 스킬로 부여하는 진동 위력과 진동 횟수 부여값 +2\n- 최댓값 : 1
   źródło: BattleKeywords.json :: dataList[id=HugeIrritationAlly].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +3\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 40%)\n- Inflict +2 more Tremor Potency and Tremor Count with this unit's Skills\n- Max Stack: 1
   PL: - Minimalna i maksymalna Szybkość +3\n- Jeśli Szybkość przewyższa cel o 3 lub więcej, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 40%)\n- Umiejętności nadają wrogom o 2 więcej Mocy i Licznika Wstrząsu\n- Maks.: 1
428. [Słowo kluczowe [BeastEyesAlly] — nazwa] 오버히트
   źródło: BattleKeywords.json :: dataList[id=BeastEyesAlly].name
   kontekst: identyfikator tagu w tekstach: `[BeastEyesAlly]`
   limit: do 40 znaków
   EN: Overheat
   PL: Przegrzanie
429. [Słowo kluczowe [BeastEyesAlly] — opis] - 맹호표탄을 얻으면, 이 효과가 사라짐\n- 속도 최솟값, 최댓값 2 증가\n- 기본 공격 스킬의 합 위력이 (호표탄, 맹호표탄의 누적 소모 합/2)만큼 감소(최대 10)하는 대신 다음 효과 얻음 (전부 획득)\n· 8 ~ : 턴 시작 시 잃은 체력 10%당 보호 1 얻음 (최대 5)\n· 14 ~ : 합 패배 시, 기본 공격 스킬의 파괴 불가 코인 피해량 +(75 + 잃은 체력 비율)% (최대 150%)\n· 20 ~ : 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이)%만큼 증가 (최대 50%, E.G.O 스킬 제외)
   źródło: BattleKeywords.json :: dataList[id=BeastEyesAlly].desc
   limit: do 820 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Loses this effect when this unit gains Savage Tigermark Round\n- Min & Max Speed +2\n- Base Attack Skills Lose (cumulative number of Tigermark & Savage Tigermark Rounds spent / 2) Clash Power (max 10); however, gain the following effects(cumulative):\n· 8+ Rounds spent: Gain 1 Protection for every 10% missing HP on self at Turn Start (max 5)\n· 14+ Rounds spent: On Clash Lose, Unbreakable Coins of this unit's Base Attack Skills deal +(75 + missing HP percentage on self)% damage (max 150%)\n· 20+ Rounds Spent: Deal +(HP percentage difference)% damage against targets with higher remaining HP percentage than this unit (max 50%; except E.G.O Skills)
   PL: - Traci efekt po zyskaniu Dzikiego Pocisku Tygrysiego Znaku\n- Minimalna i maksymalna Szybkość +2\n- Bazowe Umiejętności ataku tracą (łączny limit zużytych Pocisków Tygrysiego Znaku i Dzikich Pocisków / 2) Mocy Starcia (maks. 10), w zamian zyskując następujące efekty (kumulatywnie):\n· 8 lub więcej zużytych pocisków: na początku tury 1 Ochrony za każde 10% brakującego HP (maks. 5)\n· 14 lub więcej: po przegranej w Starciu Niezniszczalne Monety bazowych Umiejętności ataku zadają +(75 + procent brakującego HP)% obrażeń (maks. 150%)\n· 20 lub więcej: zadaje +(różnica procentów HP)% obrażeń celom o wyższym procentu HP (maks. 50%; poza Umiejętnościami E.G.O)
430. [Słowo kluczowe [RoseThorn] — nazwa] 탐식극(貪食棘)
   źródło: BattleKeywords.json :: dataList[id=RoseThorn].name
   kontekst: identyfikator tagu w tekstach: `[RoseThorn]`
   limit: do 40 znaków
   EN: Gluttonous Thorn (貪食棘)
   PL: Kolec Obżarstwa (貪食棘)
431. [Słowo kluczowe [RoseThorn] — opis] 최댓값: 9\n\n턴 종료 시, 색욕 공명 수만큼 출혈 횟수를 증가 시키고, 탐식극(貪食棘) 1 감소. (최대 출혈 횟수 증가 값 5)\n\n이 효과를 지닌 채로 출혈 위력을 99 이상으로 부여 되었을 때 초과된 출혈 위력 수치만큼 혈찬을 획득하고, 다음 턴에 획득한 혈찬 수치만큼 방어 레벨 감소를 얻음 (최대 방어 레벨 감소 획득 값 5)
   źródło: BattleKeywords.json :: dataList[id=RoseThorn].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 9\n\nTurn End: gain Bleed Count equal to Lust Reson., then lose 1 Gluttonous Thorn (貪食棘). (max Bleed Count gain: 5)\n\nWhile this unit has this effect, if it gains Bleed Potency beyond 99, increase Bloodfeast equal to the excess Bleed Potency; then, gain Defense Level Down next turn equal to Bloodfeast increased (max Defense Level Down gain: 5)
   PL: Maks.: 9\n\nNa koniec tury zwiększa Licznik Krwawienia o liczbę Rezonansów Żądzy i traci 1 Kolca Obżarstwa (maks. 5 zwiększonych Liczników)\n\nGdy przy tym efekcie Moc Krwawienia zostanie nadana ponad 99, zyskuje Ucztę Krwi równą nadwyżce, a w następnej turze tyle Spadków Poziomu Obrony (maks. 5)
432. [Słowo kluczowe [ChoSuperCharge] — nazwa] 초아광축전
   źródło: BattleKeywords.json :: dataList[id=ChoSuperCharge].name
   kontekst: identyfikator tagu w tekstach: `[ChoSuperCharge]`
   limit: do 40 znaków
   EN: Near-light Superbattery
   PL: Superbateria Pobliskiego Światła
433. [Słowo kluczowe [ChoSuperCharge] — opis] - 최대값 : 100\n- 자신이 충전 횟수를 소모할 때, 소모값만큼 이 버프 수치 증가\n- 충전 횟수 최대치 +10\n- 아군이 충전 위력이나 횟수를 얻을 때, 자신의 충전 횟수 1 증가\n- 자신의 스킬로 충전 횟수를 소모할 때, 소모량만큼 추가 1회 소모 (횟수가 부족하면, 부족한 만큼 최대로 소모)\n- 수치 10 당 자신의 스킬 피해량 +10%\n- 수치 20 당, 자신의 공격에 한해 적의 모든 내성 +0.1 . (최대 +0.5. 흐트러짐 상태 제외)\n- 이 버프를 보유한 인격 사망 시, 현재 출전 인원 중 편성 순서가 다음으로 빠른 아군에게 이 버프가 계승되며, 버프 수치가 유지됨\n- 이 버프의 효과는 특수 충전에도 적용됨
   źródło: BattleKeywords.json :: dataList[id=ChoSuperCharge].desc
   limit: do 950 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 100\n- When consuming Charge Count, add the amount consumed to this buff's Stack\n- Max Charge Count Cap +10\n- Gain 1 Charge Count when allies gain Charge Potency or Count\n- When this unit consumes Charge Count with its Skills, consume the same amount of Charge Count 1 more time (when there isn't enough Charge Count, consume as much as available)\n- Deal +10% damage for every 10 Stack\n- Enemies gain +0.1 Resistance against this unit's attacks for every 20 Stack (max +0.5 Resist; does not activate against Staggered enemies)\n- When the Identity with this effect dies, the buff transfers to the ally who is second earliest to this unit in the Deployment order. The Stack carries over as well.\n- This effect works on 'Unique Charge' as well.
   PL: - Maks.: 100\n- Zużywając Licznik Ładowania, dodaje zużytą ilość do stosów wzmocnienia\n- Limit Liczników Ładowania +10\n- Zyskuje 1 Licznika Ładowania, gdy sojusznicy zyskują Moc lub Licznik Ładowania\n- Zużywając Licznik Ładowania Umiejętnościami, zużywa tę samą ilość jeszcze raz (przy niedoborze zużywa maksymalnie tyle, ile jest dostępne)\n- Zadaje +10% obrażeń za każde 10 stosów\n- Wrogowie zyskują +0,1 Odporności na ataki tej jednostki za każde 20 stosów (maks. +0,5; nie działa na oszołomionych)\n- Po śmierci osobowości z tym wzmocnieniem przechodzi na sojusznika następnego w kolejce składu, zachowując stosy\n- Działa także na Szczególne Ładowanie
434. [Słowo kluczowe [ShareCharge] — nazwa] 자가 공진 회로
   źródło: BattleKeywords.json :: dataList[id=ShareCharge].name
   kontekst: identyfikator tagu w tekstach: `[ShareCharge]`
   limit: do 40 znaków
   EN: Self Resonance Circuitry
   PL: Obwód Samorezonansu
435. [Słowo kluczowe [ShareCharge] — opis] 현재 모든 아군이 보유한 충전 횟수의 총합\n\n스킬 적중 시 피해량 +(현재 아군 충전 횟수 총합 / 3)%\n아군 충전 횟수 누적 소모량 100 당, 모든 아군이 공격 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=ShareCharge].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Total sum of Charge Count currently owned by all allies\n\nOn Hit with a Skill: deal +(sum of charge count on all allies / 3)% damage\nAll allies gain 1 Offense Level Up for every 100 cumulative Charge Count consumed by allies
   PL: Łączna suma Liczników Ładowania posiadanych obecnie przez wszystkich sojuszników\n\nPrzy trafieniu Umiejętnością: zadaje +(suma Liczników Ładowania sojuszników / 3)% obrażeń\nWszyscy sojusznicy zyskują 1 Wzrost Poziomu Ataku za każde 100 łącznie zużytych Liczników Ładowania
436. [Słowo kluczowe [WaveSinking] — nazwa] 역류
   źródło: BattleKeywords.json :: dataList[id=WaveSinking].name
   kontekst: identyfikator tagu w tekstach: `[WaveSinking]`
   limit: do 40 znaków
   EN: Reflux
   PL: Refluks
437. [Słowo kluczowe [WaveSinking] — opis] - 최대값 : 3\n피격 시, 수치만큼 침잠 위력 얻음\n\n턴 종료시 자신의 정신력이 -30 이하면 아래 효과 적용 (정신력이 없는 적은 침잠 위력 60 이상 보유시 발동)\n- 자신의 (침잠 위력 x 수치)만큼 우울 피해를 받음\n- 자신을 제외한 정신력이 가장 낮은 대상 둘 (환상체의 경우, 부위)에게 역류 1 부여하고, 각 대상의 (침잠 위력 x 수치) 만큼 우울 피해\n- 역류를 보유한 상태로 사망 시, 역류 수치가 가장 높은 아군에게 자신의 역류 수치만큼 역류 부여
   źródło: BattleKeywords.json :: dataList[id=WaveSinking].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\nWhen hit, gain Sinking Potency equal to Stack\n\nTurn End: if this unit has -30 or less SP, activate the following effects (for Non-SP Units, activates at 60+ Sinking Potency)\n- Take (Sinking Potency on self x Stack) Gloom damage\n- Inflict 1 Reflux against 2 other targets with the least SP (for Abnormalities, Parts); then, deal (Sinking Potency x Stack) Gloom damage to both targets, respectively\nIf the unit with Reflux dies, transfer its Reflux Stack to its ally with the highest Reflux Stack
   PL: - Maks.: 3\nPrzy trafieniu zyskuje Moc Zatonięcia równą wartości\n\nNa koniec tury, przy Poczytalności -30 lub niższej, aktywuje poniższe efekty (jednostki bez Poczytalności: przy 60 lub więcej Mocy Zatonięcia)\n- Otrzymuje (Moc Zatonięcia x wartość) obrażeń Posępnością\n- Nadaje 1 Refluksu 2 jednostkom (w walkach skupionych: częściom) z najniższą Poczytalnością poza sobą, zadając każdemu (Moc Zatonięcia x wartość) obrażeń Posępnością\n- Jednostka, która umrze z Refluksem, przenosi swoje stosy na sojusznika z najwyższą ich liczbą
438. [Słowo kluczowe [FellBulletPersonality] — nazwa] 흉탄
   źródło: BattleKeywords.json :: dataList[id=FellBulletPersonality].name
   kontekst: identyfikator tagu w tekstach: `[FellBulletPersonality]`
   limit: do 40 znaków
   EN: Fell Bullet
   PL: Mroczny Pocisk
439. [Słowo kluczowe [FellBulletPersonality] — opis] 최댓값: 1\n찢어진 추억당 크리티컬 피해량 +3% (최대 18%)\n적중 시 출혈 1 부여 (턴 당 최대 3)\n대상 처치 시 호흡 3 얻음, 자신의 호흡 횟수 2 증가 (턴 당 최대 2회)\n턴 종료 시 제거됨
   źródło: BattleKeywords.json :: dataList[id=FellBulletPersonality].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 1\n+3% damage on Critical Hit for every Torn Memory (max 18%)\nOn Hit, inflict 1 Bleed (3 per turn)\nOn Kill, gain 3 Poise and +2 Poise Count (2 times per turn)\nExpires at Turn End
   PL: Maks.: 1\n+3% obrażeń krytycznych za każde Naderwane Wspomnienie (maks. 18%)\nPrzy trafieniu nadaje 1 Krwawienia (do 3 razy na turę)\nPo pokonaniu wroga zyskuje 3 Oddechu i 2 Liczniki Oddechu (do 2 razy na turę)\nUsuwany na koniec tury
440. [Słowo kluczowe [FellBulletPersonality] — podsumowanie] 크리티컬 피해량 증가, 추가 출혈 부여
   źródło: BattleKeywords.json :: dataList[id=FellBulletPersonality].summary
   limit: do 120 znaków
   EN: Deal more Crit damage, inflict more Bleed
   PL: Zadaje więcej obrażeń krytycznych, nadaje więcej Krwawienia
441. [Słowo kluczowe [HeishouDeathCount] — nazwa] 사중구활[死中求活]
   źródło: BattleKeywords.json :: dataList[id=HeishouDeathCount].name
   kontekst: identyfikator tagu w tekstach: `[HeishouDeathCount]`
   limit: do 40 znaków
   EN: Life from Death [死中求活]
   PL: Życie ze Śmierci [死中求活]
442. [Słowo kluczowe [HeishouDeathCount] — opis] - 최댓값 : 5\n- 턴 시작시 아래 효과 적용\n· 수치 1 당 공격 레벨 증가 1 얻음 (최대 5)\n· 수치 2 당 피해량 증가 1 얻음 (최대 2)\n· 수치 3 이상이면 공격 위력 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=HeishouDeathCount].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: activate the following\n· Gain 1 Offense Level Up for every 1 Stack (max 5)\n· Gain 1 Damage Up for every 2 Stack (max 2)\n· Gain 1 Attack Power Up at 3+ Stack
   PL: - Maks.: 5\n- Na początku tury aktywuje poniższe efekty\n· Za każdą wartość: 1 Wzrost Poziomu Ataku (maks. 5)\n· Za każde 2 wartości: 1 Wzrost Obrażeń (maks. 2)\n· Przy 3 lub więcej wartościach: 1 Wzrost Mocy Ataku
443. [Słowo kluczowe [HeishouCombo] — nazwa] 존명
   źródło: BattleKeywords.json :: dataList[id=HeishouCombo].name
   kontekst: identyfikator tagu w tekstach: `[HeishouCombo]`
   limit: do 40 znaków
   EN: Exalted Command
   PL: Czcigodny Rozkaz
444. [Słowo kluczowe [HeishouCombo] — opis] - 이 효과를 부여한 대상의 스킬 종료시, 부여 대상이 공격한 적을 기본 스킬 3으로 일방 공격함 (강화 스킬로 발동되지 않음)\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음\n- 3스킬을 사용할 수 있는 아군이 없으면, 발동되지 않음
   źródło: BattleKeywords.json :: dataList[id=HeishouCombo].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Base Skill 3 against the same enemy unit A attacked with its Skill. Activates at unit A's Attack End. (Does not activate as Empowered Skills)\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.\n- Does not activate if affected ally's Skill 3 is not unlocked.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany bazową Umiejętnością 3 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku A. (Nie aktywuje się jako Umiejętność Wzmocniona)\n- Umiejętność użyta jako atak niekwestionowany nie wpływa na nadchodzącą listę Umiejętności B.\n- Nie aktywuje się, gdy Umiejętność 3 sojusznika nie jest odblokowana
445. [Słowo kluczowe [HeishouComboCount] — nazwa] 몰아침
   źródło: BattleKeywords.json :: dataList[id=HeishouComboCount].name
   kontekst: identyfikator tagu w tekstach: `[HeishouComboCount]`
   limit: do 40 znaków
   EN: Unrelenting Storm
   PL: Nawałnica
446. [Słowo kluczowe [HeishouComboCount] — opis] - 홍원 군주 홍루 인격과 연계를 진행한 횟수\n- 최댓값 : 2\n- 턴 시작시 수치 1 당 공격 레벨 증가 1, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=HeishouComboCount].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Number of times this unit activated combo with The Lord of Hongyuan Hong Lu Identity\n- Max Stack: 2\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Up for every Stack
   PL: - Liczba wykonanych połączeń z osobowością Władcy Hongyuan Hong Lu\n- Maks.: 2\n- Na początku tury za każdą wartość: 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony
447. [Słowo kluczowe [HeishouAttack] — nazwa] 뜻에 따라, 베겠습니다.
   źródło: BattleKeywords.json :: dataList[id=HeishouAttack].name
   kontekst: identyfikator tagu w tekstach: `[HeishouAttack]`
   limit: do 40 znaków
   EN: Your Will Guides My Blade.
   PL: Twoja Wola Prowadzi Moje Ostrze.
448. [Słowo kluczowe [HeishouAttack] — opis] - 이 효과를 부여한 대상의 공격 스킬 종료 시, 부여 대상이 공격한 적을 스킬 1로 일방 공격 함.\n- 부여 대상이 이 효과로 공격 시 해당 캐릭터의 사용할 스킬 목록에 영향을 주지 않음.
   źródło: BattleKeywords.json :: dataList[id=HeishouAttack].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If unit A applies this effect to unit B: Unit B follows up with an Unopposed Attack with its Skill 1 against the same enemy unit A attacked with its Skill. Activates at unit A's Skill Attack End.\n- The Skill used as an Assist Attack does not affect Unit B's upcoming Skills list.
   PL: - Gdy jednostka A nadaje ten efekt jednostce B: B wykonuje atak niekwestionowany Umiejętnością 1 przeciwko temu samemu wrogowi, którego zaatakowała A. Aktywuje się po zakończeniu ataku Umiejętności A.\n- Umiejętność użyta jako atak niekwestionowany nie wpływa na nadchodzącą listę Umiejętności B.
449. [Słowo kluczowe [HeishouSupportProtect] — nazwa] 호위
   źródło: BattleKeywords.json :: dataList[id=HeishouSupportProtect].name
   kontekst: identyfikator tagu w tekstach: `[HeishouSupportProtect]`
   limit: do 40 znaków
   EN: Lordsguard
   PL: Straż Władcy
450. [Słowo kluczowe [HeishouSupportProtect] — opis] - 특수 원호 방어\n- 최댓값 : 1\n- 홍원 군주 홍루가 적에게 일방공격 당할 때, 수치를 1 소모하여 적의 공격 대상을 자신으로 변경하고, 홍원 군주 홍루 인격의 '호위' 스킬을 복사하여 사용\n- 원호 방어를 보유한 아군이 여러 명이면, 가장 높은 수치를 가진 아군이 우선 사용\n- 이 효과는 원호 방어로 간주되며, 원호 방어 수치를 계산할 때 합산됨\n- 턴 종료시 소멸
   źródło: BattleKeywords.json :: dataList[id=HeishouSupportProtect].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Assist Defense\n- Max Stack: 1\n- When The Lord of Hongyuan Hong Lu is about to take an Unopposed Attack from an enemy, consume 1 Stack to redirect the enemy's targeting to self; then, copy and use The Lord of Hongyuan Hong Lu's 'Lordsguard' Skill\n- When there are multiple allies that have Assist Defense Stacks, the ally that has the highest Stack has the highest activation priority\n- This effect counts as Assist Defense, and is counted toward calculating Assist Defense Stacks\n- Expires at Turn End
   PL: - Specjalna Obrona Wsparcia\n- Maks.: 1\n- Gdy Władca Hongyuan Hong Lu ma zostać zaatakowany atakiem niekwestionowanym wroga, zużywa 1 wartości, by przekierować cel ataku na siebie, i kopiuje Umiejętność „Straż Władcy” tej osobowości\n- Gdy Obrona Wsparcia jest u wielu sojuszników, pierwszeństwo ma ten z najwyższą wartością\n- Liczy się jako Obrona Wsparcia i jest wliczana do jej wartości\n- Znika na koniec tury
451. [Słowo kluczowe [HeishouSynergy] — nazwa] 모든 흑수의 주인
   źródło: BattleKeywords.json :: dataList[id=HeishouSynergy].name
   kontekst: identyfikator tagu w tekstach: `[HeishouSynergy]`
   limit: do 40 znaków
   EN: Leash-holder of All Heishou
   PL: Trzymający Smycz Wszystkich Heishou
452. [Słowo kluczowe [HeishouSynergy] — opis] - 최댓값 : 11\n- 수치 당, 매 턴 시작시 아래 효과 얻음\n· 1 당 속도 최댓값 1 증가 (최대 5), 자신의 스킬 피해량 +1%\n· 2 당 속도 최솟값 1 증가 (최대 2), 방어 레벨 증가 1 얻음 (최대 5)\n· 3 당 공격 레벨 증가 1 얻음 (최대 3)\n· 5 이상이면, 피해량 증가 1 얻고, 모든 흑수 인격에게 공격 레벨 증가 1 부여
   źródło: BattleKeywords.json :: dataList[id=HeishouSynergy].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 11\n- Gain the following effects based on Stack:\n· For every 1 Stack, gain 1 Max Speed (max 5) and deal +1% damage with Skills\n· For every 2 Stack, gain 1 Min Speed (max 2) and 1 Defense Level Up (max 5)\n· For every 3 Stack, gain 1 Offense Level Up (max 3)\n· At 5+ Stack, gain 1 Damage Up and apply 1 Offense Level Up to all Heishou Pack Identities
   PL: - Maks.: 11\n- Na początku każdej tury zyskuje efekty zależnie od wartości:\n· Za każdą wartość: maksymalna Szybkość +1 (maks. 5) i zadawane obrażenia Umiejętnościami +1%\n· Za każde 2 wartości: minimalna Szybkość +1 (maks. 2) i 1 Wzrost Poziomu Obrony (maks. 5)\n· Za każde 3 wartości: 1 Wzrost Poziomu Ataku (maks. 3)\n· Przy 5 lub więcej: 1 Wzrost Obrażeń i 1 Wzrost Poziomu Ataku dla wszystkich osobowości Heishou
453. [Słowo kluczowe [HeishouComboCountHonglu] — nazwa] 흑수환염[黑獣丸染]
   źródło: BattleKeywords.json :: dataList[id=HeishouComboCountHonglu].name
   kontekst: identyfikator tagu w tekstach: `[HeishouComboCountHonglu]`
   limit: do 50 znaków
   EN: Heishou Bolus Contamination [黑獣丸染]
   PL: Heishou - Zakażenie [黑獣丸染]
454. [Słowo kluczowe [HeishouComboCountHonglu] — opis] - 최댓값 : 11\n- 연계를 진행한 흑수에 따라 홍원 군주 홍루가 강화됨\n- 강화 효과는 중첩됨\n\n· 흑수 - 묘 필두 파우스트 : 받는 스킬 피해 -5%\n· 흑수 - 묘 료슈 : 자신의 속도가 대상보다 빠르면, 피해량 +5%\n· 흑수 - 묘 오티스 : 일방 공격 적중 시, 파열 횟수 1 증가 (턴 당 1회)\n· 흑수 - 사 로쟈 : 크리티컬 적중 시, 파열 1 부여 (턴 당 3회)\n· 흑수 - 사 그레고르 : 파열 피해를 가하면, 호흡 횟수 1 얻음 (턴 당 1회)
   źródło: BattleKeywords.json :: dataList[id=HeishouComboCountHonglu].desc
   limit: do 730 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 11\n- Empowers The Lord of Hongyuan Hong Lu based on which Heishou he activated combo with\n- The Heishou Bolus Contamination effects can stack with each other\n\n· Heishou - Mao Adept Faust: take -5% damage from Skills\n· Heishou - Mao Ryōshū: if this unit's Speed is faster than the target's, deal +5% damage\n· Heishou - Mao Outis: inflict +1 Rupture Count On Hit with Unopposed Attacks (once per turn)\n· Heishou - Si Rodion: Inflict 1 Rupture On Critical Hit (3 times per turn)\n· Heishou - Si Gregor: Gain +1 Poise Count when dealing Rupture damage (once per turn)
   PL: - Maks.: 11\n- Władca Hongyuan Hong Lu zyskuje wzmocnienia zależnie od Heishou, z którym wykonał połączenie\n- Efekty się kumulują\n\n· Heishou - Mao Adept Faust: otrzymywane obrażenia od Umiejętności -5%\n· Heishou - Mao Ryośu: jeśli Szybkość przewyższa cel, zadawane obrażenia +5%\n· Heishou - Mao Outis: trafienie atakiem niekwestionowanym zwiększa Licznik Rozdarcia o 1 (raz na turę)\n· Heishou - Si Rodion: trafienie krytyczne nadaje 1 Rozdarcia (do 3 razy na turę)\n· Heishou - Si Gregor: zadanie obrażeń Rozdarciem zyskuje 1 Licznik Oddechu (raz na turę)
455. [Słowo kluczowe [DarkHongluQiuAndHonglu] — nazwa] 패도를 걷는 자
   źródło: BattleKeywords.json :: dataList[id=DarkHongluQiuAndHonglu].name
   kontekst: identyfikator tagu w tekstach: `[DarkHongluQiuAndHonglu]`
   limit: do 50 znaków
   EN: One Who Walks The Way of the Hegemon
   PL: Kroczący Drogą Hegemona
456. [Słowo kluczowe [DarkHongluQiuAndHonglu] — opis] - 홍루의 모든 스킬의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 다음 턴에 자신이 공격 위력 증가 2, 남은 아군이 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: BattleKeywords.json :: dataList[id=DarkHongluQiuAndHonglu].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Skills gain +1 Final Power\n- On Clash Win, 1 ally(including this unit) with the least SP heals 5 SP\n- When an ally dies, next turn, this unit gains 2 Attack Power Up and remaining allies gain 1 Attack Power Up (once per turn)
   PL: - Moc Końcowa wszystkich Umiejętności Hong Lua +1\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- Po śmierci sojusznika ta jednostka zyskuje 2 Wzrosty Mocy Ataku, a pozostali 1 Wzrost Mocy Ataku w następnej turze (raz na turę)
457. [Słowo kluczowe [DarkHongluTeaching] — nazwa] 관철
   źródło: BattleKeywords.json :: dataList[id=DarkHongluTeaching].name
   kontekst: identyfikator tagu w tekstach: `[DarkHongluTeaching]`
   limit: do 40 znaków
   EN: Uncompromising Imposition
   PL: Nieustępliwe Narzucanie
458. [Słowo kluczowe [DarkHongluTeaching] — opis] 최댓값: 3\n-  턴 종료시, 정신력 5 회복\n- 전투 중 체력이 0이 될 때 체력을 최대 체력만큼 회복함 (수치만큼 발동)\n- 이 버프로 체력을 회복했을 시, 다음 턴에 위력 증가 1 얻음
   źródło: BattleKeywords.json :: dataList[id=DarkHongluTeaching].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\n- Turn End: heal 5 SP\n- When HP drops to 0 during the Encounter, heal up to max HP (activates as many times as this unit has Stacks)\n- When healed by this effect, gain 1 Power Up next turn
   PL: Maks.: 3\n- Na koniec tury regeneruje 5 Poczytalności\n- Gdy HP spadnie do 0 w trakcie walki, regeneruje je do maksimum (tyle razy, ile wynosi wartość)\n- Po wyleczeniu tym efektem zyskuje w następnej turze 1 Wzrost Mocy
459. [Słowo kluczowe [DarkHongluParryGahwan] — nazwa] 가증스럽군요, 형님.
   źródło: BattleKeywords.json :: dataList[id=DarkHongluParryGahwan].name
   kontekst: identyfikator tagu w tekstach: `[DarkHongluParryGahwan]`
   limit: do 50 znaków
   EN: You're Ridiculous, Big Brother.
   PL: Jesteś Żenujący, Bracie.
460. [Słowo kluczowe [DarkHongluParryGahwan] — opis] 가환과 합을 진행할 때, 합 위력 +2
   źródło: BattleKeywords.json :: dataList[id=DarkHongluParryGahwan].desc
   limit: do 120 znaków
   EN: In Clashes against Jia Huan, Clash Power +2
   PL: W Starciach przeciwko Jia Huan: Moc Starcia +2
461. [Słowo kluczowe [DarkHonglu_EGOResourceup] — nazwa] 수없이 많은 자들의 피를 흘리게 될지라도…
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_EGOResourceup].name
   kontekst: identyfikator tagu w tekstach: `[DarkHonglu_EGOResourceup]`
   limit: do 50 znaków
   EN: No Matter How Many Must Bleed...
   PL: Nawet Gdy Musi Krwawić Bez Liku…
462. [Słowo kluczowe [DarkHonglu_EGOResourceup] — opis] [홍루 특수 효과]\n- 이번 전투에서 자신의 스킬 공격 종료 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 1회)\n- 피해를 받았을 때, 다음 턴에 참격 피해량 증가 2를 얻음(턴당 1회)
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_EGOResourceup].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Hong Lu Exclusive Effect]\n- For this Encounter: after using a Skill Attack, gain 2 additional E.G.O resources of the Skill's Affinity (once per turn)\n- When this unit takes damage, it gains 2 Slash DMG Up next turn (once per turn)
   PL: [Specjalny efekt Hong Lua]\n- W tej walce po zakończeniu ataku Umiejętnością zyskuje 2 dodatkowych zasobów E.G.O jej atrybutu (raz na turę)\n- Po otrzymaniu obrażeń zyskuje w następnej turze 2 Wzrosty Obrażeń Cięcia (raz na turę)
463. [Słowo kluczowe [DarkHonglu_Xi] — nazwa] 기쁨
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Xi].name
   kontekst: identyfikator tagu w tekstach: `[DarkHonglu_Xi]`
   limit: do 40 znaków
   EN: Happiness
   PL: Radość
464. [Słowo kluczowe [DarkHonglu_Xi] — opis] - 홍루의 합 위력 +1\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 페이즈에서 1회 보옥 상태가 되지 않음. 보옥 상태로 만드는 스킬과 합 진행 시 합 위력 +5, 해당 스킬과 합에서 승리한 경우, 보옥 상태가 되지 않고 자신의 흐트러짐 해제, 가모의 정신력 10 감소, 가모에게 취약 2 부여\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Xi].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Clash Power +1\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Nullfies the effect that turns this unit into a Precious Jade once. When clashing against Skills that turns this unit into a Precious Jade, Clash Power +5; if this unit wins that Clash, this unit does not become a Precious Jade, recovers from Stagger, reduces Jia Mu's SP by 10, and inflicts 2 Fragile against Jia Mu\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Starcia Hong Lua +1\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Jednorazowo unieważnia przemianę w Jadeit; w Starciu z Umiejętnością przemieniającą w Jadeit Moc Starcia +5; po wygranej nie następuje przemiana, oszołomienie zostaje wyleczone, Poczytalność Jia Mu maleje o 10, a Jia Mu otrzymuje 2 Wrażliwości\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
465. [Słowo kluczowe [DarkHonglu_Le] — nazwa] 기쁨, 즐거움
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Le].name
   kontekst: identyfikator tagu w tekstach: `[DarkHonglu_Le]`
   limit: do 40 znaków
   EN: Happiness, Joy
   PL: Radość, Rozkosz
466. [Słowo kluczowe [DarkHonglu_Le] — opis] - 홍루의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Le].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +1\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +1\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
467. [Słowo kluczowe [DarkHonglu_Ai] — nazwa] 기쁨, 즐거움, 슬픔
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Ai].name
   kontekst: identyfikator tagu w tekstach: `[DarkHonglu_Ai]`
   limit: do 40 znaków
   EN: Happiness, Joy, Sorrow
   PL: Radość, Rozkosz, Smutek
468. [Słowo kluczowe [DarkHonglu_Ai] — opis] - 홍루의 최종 위력 +3\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Ai].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +3\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +3\n- Po wygranej w Starciu sojusznik (łącznie z tą jednostką) z najniższą Poczytalnością regeneruje 5 Poczytalności\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
469. [Słowo kluczowe [DarkHonglu_Nu] — nazwa] 기쁨, 즐거움, 슬픔, 분노
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Nu].name
   kontekst: identyfikator tagu w tekstach: `[DarkHonglu_Nu]`
   limit: do 50 znaków
   EN: Happiness, Joy, Sorrow, Wrath
   PL: Radość, Rozkosz, Smutek, Gniew
470. [Słowo kluczowe [DarkHonglu_Nu] — opis] - 홍루의 최종 위력 +5\n- 매 턴 시작 시 모든 아군의 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 전투에서 누적으로 잃은 체력 비율의 30%만큼 피해량 증가 (최대 100%)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords.json :: dataList[id=DarkHonglu_Nu].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +5\n- Allies heal 5 SP at every Turn Start (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Increases damage dealt by 30% of the total HP percentage this unit has cumulatively lost during this Encounter (max 100%)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lua +5\n- Na początku każdej tury wszyscy sojusznicy regenerują 5 Poczytalności (łącznie z tą jednostką)\n- Po śmierci sojusznika pozostali sojusznicy zyskują na koniec tury 1 Wzrost Mocy Ataku w następnej turze (raz na turę)\n- W tej walce, gdy żyje co najmniej 1 inny sojusznik: otrzymanie obrażeń redukujących HP Hong Lua do 1 nie zabija go — regeneruje 50% HP\n- Zadawane obrażenia rosną o 30% łącznie utraconego procentu HP w tej walce (maks. 100%)\nPo wygranej w Starciu z Jia Mu zyskuje po 1 zasobu losowych atrybutów E.G.O z 3 najbardziej deficytowych
471. [Słowo kluczowe [ChickenStance] — nazwa] 혈염 [血炎]
   źródło: BattleKeywords.json :: dataList[id=ChickenStance].name
   kontekst: identyfikator tagu w tekstach: `[ChickenStance]`
   limit: do 40 znaków
   EN: Bloodflame [血炎]
   PL: Krwawy Płomień [血炎]
472. [Słowo kluczowe [ChickenStance] — opis] - 최댓값: 3\n- 자신의 기본 스킬로 적에게 부여하는 화상, 파열 위력 +1\n- 이 버프를 보유한 상태로 적을 흐트러뜨리거나 처치하면, 정신력 3 회복 (턴 당 3회)\n· 위 효과가 발동했을 때 자신의 정신력이 최대치면, 다음 턴에 공격 레벨 증가 1, 신속 1 얻음\n- 턴 종료시 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=ChickenStance].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- This unit inflicts +1 more Burn and Rupture Potency with its Base Skills\n- While this unit has this effect, heal 3 SP upon Staggering or killing an enemy (3 times per turn)\n· If this unit's SP is at max when the above effect activates, gain 1 Offense Level Up and 1 Haste next turn\n- Lose 1 Stack at Turn End
   PL: - Maks.: 3\n- Bazowe Umiejętności nadają wrogom o 1 więcej Mocy Podpalenia i Rozdarcia\n- Oszołomienie lub pokonanie wroga regeneruje 3 Poczytalności (do 3 razy na turę)\n· Przy pełnej Poczytalności zyskuje w następnej turze 1 Wzrost Poziomu Ataku i 1 Pośpiechu\n- Na koniec tury wartość maleje o 1
473. [Słowo kluczowe [ChickenStance] — podsumowanie] 부여하는 화상, 파열 +1
   źródło: BattleKeywords.json :: dataList[id=ChickenStance].summary
   limit: do 120 znaków
   EN: Inflict +1 more Burn or Rupture
   PL: Nadaje o 1 więcej Podpalenia lub Rozdarcia
474. [Słowo kluczowe [LegStrengthHorseYisang] — nazwa] 각력【오】
   źródło: BattleKeywords.json :: dataList[id=LegStrengthHorseYisang].name
   kontekst: identyfikator tagu w tekstach: `[LegStrengthHorseYisang]`
   limit: do 40 znaków
   EN: Strider【Wu】
   PL: Kroczący【Wu】
475. [Słowo kluczowe [LegStrengthHorseYisang] — opis] - 최댓값: 3\n- 턴 종료 시 다음 턴에 신속 2, 도발치를 (수치 x 2)만큼 얻음\n- 공격 시작 전 진동 위력을 수치만큼 메인 타겟에게 부여 (턴 당 최대 6)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=LegStrengthHorseYisang].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Haste and (Stack x 2) Aggro next turn\n- Before Attack: inflict (Stack) Tremor Potency against the main target (max 6 per turn)\n- Lose 1 Stack at Turn End
   PL: - Maks.: 3\n- Na koniec tury zyskuje w następnej turze 2 Pośpiechu i (wartość x 2) Wartości Prowokacji\n- Przed atakiem nadaje głównemu celowi Moc Wstrząsu równą wartości (do 6 na turę)\n- Na koniec tury maleje o 1
476. [Słowo kluczowe [ConcussionYisang] — nazwa] 뇌진탕
   źródło: BattleKeywords.json :: dataList[id=ConcussionYisang].name
   kontekst: identyfikator tagu w tekstach: `[ConcussionYisang]`
   limit: do 40 znaków
   EN: Concussion
   PL: Wstrząs Mózgu
477. [Słowo kluczowe [ConcussionYisang] — opis] - 최댓값: 2\n- 이 효과가 있는 동안 파열 피해와 진동 폭발로 인한 흐트러짐 손상을 1.2배로 받음. (소수점 버림)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=ConcussionYisang].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Multiply the amount of Stagger Threshold raised by Tremor Burst and Rupture damage dealt against this unit by 1.2 (rounded down)\n- Lose 1 Stack at Turn End
   PL: - Maks.: 2\n- Podczas działania tego efektu otrzymywane obrażenia Rozdarciem i podnoszenie Progu Oszołomienia przez Wybuch Wstrząsu mnożą się x 1,2 (zaokrąglone w dół)\n- Na koniec tury maleje o 1
478. [Słowo kluczowe [BreakthroughHorse] — nazwa] 적진 주파
   źródło: BattleKeywords.json :: dataList[id=BreakthroughHorse].name
   kontekst: identyfikator tagu w tekstach: `[BreakthroughHorse]`
   limit: do 40 znaków
   EN: Linebreaker
   PL: Przełamanie Linii
479. [Słowo kluczowe [BreakthroughHorse] — opis] - 최댓값: 5\n- 턴 시작 시 해당 턴 동안 보호막 (수치 x 10)을 얻음\n- 최댓값일 시, 자신의 최종 위력이 2 증가함\n- 피격 시 한 스킬로 100 이상의 피해를 입었다면 해당 스킬 종료 시 보호 1 획득 (턴 당 2회, 보호막 피해 포함, 키워드로 인한 피해는 판정하지 않음)
   źródło: BattleKeywords.json :: dataList[id=BreakthroughHorse].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain (Stack x 10) Shield for the turn\n- At max Stack, gain 2 Final Power\n- When hit: if this unit took 100+ damage from a single Skill, gain 1 Protection after that Skill ends (2 times per turn; includes damage against Shield HP; does not count damage from Keywords)
   PL: - Maks.: 5\n- Na początku tury zyskuje (wartość x 10) Tarczy na tę turę\n- Przy maksymalnej wartości Moc Końcowa +2\n- Przy otrzymaniu 100 lub więcej obrażeń z jednej Umiejętności zyskuje po jej zakończeniu 1 Ochrony (do 2 razy na turę; wlicza obrażenia Tarczy; nie liczy obrażeń od Słów Kluczowych)
480. [Słowo kluczowe [BattlefieldHorse] — nazwa] 호령
   źródło: BattleKeywords.json :: dataList[id=BattlefieldHorse].name
   kontekst: identyfikator tagu w tekstach: `[BattlefieldHorse]`
   limit: do 40 znaków
   EN: Commanding Cry
   PL: Rozkaz Dowódcy
481. [Słowo kluczowe [BattlefieldHorse] — opis] - 합 위력 1 증가, 방어 레벨 2 증가\n- 턴 종료 시 제거
   źródło: BattleKeywords.json :: dataList[id=BattlefieldHorse].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 Clash Power and 2 Defense Level\n- Expires at Turn End
   PL: - Moc Starcia +1 i Poziom Obrony +2\n- Usuwany na koniec tury
482. [Słowo kluczowe [VibrationBleeding] — nazwa] 진동 - 과다출혈
   źródło: BattleKeywords.json :: dataList[id=VibrationBleeding].name
   kontekst: identyfikator tagu w tekstach: `[VibrationBleeding]`
   limit: do 40 znaków
   EN: Tremor - Hemorrhage
   PL: Wstrząs - Krwotok
483. [Słowo kluczowe [VibrationBleeding] — opis] - 진동 폭발 시 (진동 위력과 출혈 위력의 합/2)만큼 색욕 속성 피해를 입고 출혈 횟수 1 감소\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords.json :: dataList[id=VibrationBleeding].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Lust Damage equal to (sum of Tremor Potency and Bleed Potency / 2), and lose 1 Bleed Count\n- When hit by Skills that trigger Tremor Burst, raise this unit's Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wybuchu Wstrząsu otrzymuje obrażenia Żądzą równe (suma Mocy Wstrząsu i Mocy Krwawienia / 2) i traci 1 Licznik Krwawienia\n- Przy trafieniu Umiejętnością wyzwalającą Wybuch Wstrząsu podnosi Próg Oszołomienia o moc efektu\n- Na koniec tury Licznik maleje o 1\n(Reaguje tak samo jak zwykły Wstrząs na efekty zmieniające Moc/Licznik Wstrząsu)
484. [Słowo kluczowe [GazeRyoshu] — nazwa] 시선
   źródło: BattleKeywords.json :: dataList[id=GazeRyoshu].name
   kontekst: identyfikator tagu w tekstach: `[GazeRyoshu]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
485. [Słowo kluczowe [GazeRyoshu] — opis] - 최댓값 : 7\n- 시선 1당 료슈에게 받는 피해량과 료슈에게 가하는 피해량 +10%\n- 사망시, 이 유닛 아군 중 시선 또는 경멸이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 옮겨감 ('경멸 밑으로 쏟아지는 경외의 시선' 공격 도중 사망한 경우 해당 효과가 발동하지 않음)\n- 턴 종료시 수치가 7이면, 다음 턴에 경멸로 변환됨
   źródło: BattleKeywords.json :: dataList[id=GazeRyoshu].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- Take and deal +10% damage from and against Ryōshū for every 1 Stack of Gaze\n- On death, transfers to this unit's ally (for Focused Encounters, a different Part) that has no Contempt or Gaze, or has the least Contempt or Gaze (this effect does not activate if this unit was killed during the Skill attack 'Cascading Gaze of Awe Underneath Contempt')\n- Turn End: At 7 Stacks, convert this effect into Contempt next turn
   PL: - Maks.: 7\n- Otrzymuje i zadaje +10% obrażeń od i przeciwko Ryośu za każdą wartość Spojrzenia\n- Po śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Pogardy lub Spojrzenia albo z ich najmniejszą liczbą (nie aktywuje się, gdy śmierć nastąpiła podczas ataku „Kaskadowe Spojrzenie Grozy pod Pogardą”)\n- Na koniec tury, przy wartości 7, w następnej turze zamienia się w Pogardę
486. [Słowo kluczowe [ContemptRyoshu] — nazwa] 경멸
   źródło: BattleKeywords.json :: dataList[id=ContemptRyoshu].name
   kontekst: identyfikator tagu w tekstach: `[ContemptRyoshu]`
   limit: do 40 znaków
   EN: Contempt
   PL: Pogarda
487. [Słowo kluczowe [ContemptRyoshu] — opis] - 최댓값 : 1\n- 료슈에게 받는 피해량과 료슈에게 가하는 피해량 -50%\n- 경멸이 있는 대상은 시선을 얻을 수 없음\n- 사망시, 이 유닛 아군 중 시선 또는 경멸이 없거나 가장 적은 대상(집중 전투일 경우, 부위로 판정)에게 옮겨감 ('경멸 밑으로 쏟아지는 경외의 시선' 공격 도중 사망한 경우 해당 효과가 발동하지 않음)\n- 턴 종료 시, 소멸하면서 다음 턴에 시선 7 얻음
   źródło: BattleKeywords.json :: dataList[id=ContemptRyoshu].desc
   limit: do 570 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take and deal -50% damage from and against Ryōshū\n- Targets that have Contempt cannot gain Gaze\n- On death, transfers to this unit's ally (for Focused Encounters, a different Part) that has no Contempt or Gaze, or has the least Contempt or Gaze (this effect does not activate if this unit was killed during the Skill attack 'Cascading Gaze of Awe Underneath Contempt')\n- Turn End: Expires; then, this unit gains 7 Gaze next turn
   PL: - Maks.: 1\n- Otrzymuje i zadaje -50% obrażeń od i przeciwko Ryośu\n- Cele z Pogardą nie mogą zyskać Spojrzenia\n- Po śmierci przenosi się na sojusznika (w walkach skupionych: na inną część) bez Pogardy lub Spojrzenia albo z ich najmniejszą liczbą (nie aktywuje się, gdy śmierć nastąpiła podczas ataku „Kaskadowe Spojrzenie Grozy pod Pogardą”)\n- Na koniec tury znika, a w następnej turze jednostka zyskuje 7 Spojrzeń
488. [Słowo kluczowe [CommonExit] — nazwa] 전장 이탈
   źródło: BattleKeywords.json :: dataList[id=CommonExit].name
   kontekst: identyfikator tagu w tekstach: `[CommonExit]`
   limit: do 40 znaków
   EN: Escape Battlefield
   PL: Ucieczka z Pola Bitwy
489. [Słowo kluczowe [CommonExit] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)
   źródło: BattleKeywords.json :: dataList[id=CommonExit].desc
   limit: do 150 znaków
   EN: - Turn End: recover from Stagger and escape from the Encounter (excluding forced Staggers; does not count as death)
   PL: - Na koniec tury dochodzi do siebie po oszołomieniu i opuszcza walkę (poza wymuszonym oszołomieniem; nie liczy się jako śmierć)
490. [Słowo kluczowe [CuredFilm] — nazwa] 경화막
   źródło: BattleKeywords.json :: dataList[id=CuredFilm].name
   kontekst: identyfikator tagu w tekstach: `[CuredFilm]`
   limit: do 40 znaków
   EN: Hardened Shell-Barrier
   PL: Utwardzona Błona
491. [Słowo kluczowe [CuredFilm] — opis] - 턴 시작 시, (수치/3)만큼 방어 레벨 증가 얻음 (최대 3, 소수점 버림)\n- 적에게 피격 직전, 경화막을 절반만큼 소모하여 소모한 수치만큼 보호 얻음 (턴당 1회, 소수점 올림)\n- 턴 종료 시, 3 감소\n- 최대 10
   źródło: BattleKeywords.json :: dataList[id=CuredFilm].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain (Stack / 3) Defense Level Up (max 3; rounded down)\n- Immediately before getting hit by an enemy, consume half of Hardened Shell-Barrier and gain Protection equal to the Stack consumed (once per turn, rounded up)\n- Turn End: lose 3 Stack\n- Max Stack: 10
   PL: - Na początku tury zyskuje (stosy/3) Wzrostów Poziomu Obrony (maks. 3; zaokrąglone w dół)\n- Tuż przed trafieniem atakiem wroga zużywa połowę Utwardzonej Błony i zyskuje Ochrony równą zużytej wartości (raz na turę; zaokrąglone w górę)\n- Na koniec tury maleje o 3\n- Maks.: 10
492. [Słowo kluczowe [CuredFilm] — podsumowanie] 방어 레벨 증가 얻음\n스킬로 체력 피해 받기 전, 수치를 소모하여 보호 얻음
   źródło: BattleKeywords.json :: dataList[id=CuredFilm].summary
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Defense Level Up\nImmediately before taking damage from Skills, consume Stack to gain Protection
   PL: Zyskuje Wzrost Poziomu Obrony\nTuż przed utratą HP od Umiejętności zużywa stosy, by zyskać Ochronę
493. [Słowo kluczowe [Cianjing] — nazwa] 시엔징
   źródło: BattleKeywords.json :: dataList[id=Cianjing].name
   kontekst: identyfikator tagu w tekstach: `[Cianjing]`
   limit: do 40 znaków
   EN: Thunderer
   PL: Thunderer
494. [Słowo kluczowe [Cianjing] — opis] - 턴 시작 시, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 턴 종료 시, 1 감소\n- 최대 5
   źródło: BattleKeywords.json :: dataList[id=Cianjing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Offense Level Up and 1 Defense Level Up\n- Turn End: lose 1 Stack\n- Max Stack: 5
   PL: - Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony\n- Na koniec tury maleje o 1\n- Maks.: 5
495. [Słowo kluczowe [Cianjing] — podsumowanie] 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: BattleKeywords.json :: dataList[id=Cianjing].summary
   limit: do 120 znaków
   EN: Gain Offense Level Up & Defense Level Up
   PL: Zyskuje Wzrost Poziomu Ataku i Wzrost Poziomu Obrony
496. [Słowo kluczowe [SeniorCianjing] — nazwa] 상급 시엔징
   źródło: BattleKeywords.json :: dataList[id=SeniorCianjing].name
   kontekst: identyfikator tagu w tekstach: `[SeniorCianjing]`
   limit: do 40 znaków
   EN: Higher Thunderer
   PL: Wyższy Thunderer
497. [Słowo kluczowe [SeniorCianjing] — opis] - 턴 시작 시, 공격 레벨 증가 2, 방어 레벨 증가 2 얻음\n- 턴 종료 시, 1 감소\n- 최대 5
   źródło: BattleKeywords.json :: dataList[id=SeniorCianjing].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 2 Offense Level Up and 2 Defense Level Up\n- Turn End: lose 1 Stack\n- Max Stack: 5
   PL: - Na początku tury zyskuje 2 Wzrosty Poziomu Ataku i 2 Wzrosty Poziomu Obrony\n- Na koniec tury maleje o 1\n- Maks.: 5
498. [Słowo kluczowe [SeniorCianjing] — podsumowanie] 공격 레벨 증가, 방어 레벨 증가 얻음
   źródło: BattleKeywords.json :: dataList[id=SeniorCianjing].summary
   (powtórzenie elementu 495 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Słowo kluczowe [MlynarWaiting] — nazwa] 칼집 속 사람
   źródło: BattleKeywords.json :: dataList[id=MlynarWaiting].name
   kontekst: identyfikator tagu w tekstach: `[MlynarWaiting]`
   limit: do 40 znaków
   EN: Man in Scabbard
   PL: Człowiek w Pochwie
500. [Słowo kluczowe [MlynarWaiting] — opis] - 최댓값: 40\n- (수치 / 8) 당 도발치 1 얻음 (최대 5, 소수점 버림, 조작 패널에서 가장 왼쪽의 스킬 슬롯에 적용)\n- (수치 / 20) 당 보호 1 얻음 (최대 2, 소수점 버림)\n- 턴 종료 시 10 증가\n※ 턴당 최대 20 획득 가능
   źródło: BattleKeywords.json :: dataList[id=MlynarWaiting].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 40\n- For every (Stack / 8), gain 1 Aggro (max 5; rounded down; affects the leftmost Skill Slot on the Dashboard)\n- For every (Stack / 20), gain 1 Protection (max 2; rounded down)\n- Gain 10 Stacks at Turn End\n※ Can gain up to 20 per turn
   PL: - Maks.: 40\n- Za każde (wartość/8): 1 Wartości Prowokacji (maks. 5; zaokrąglone w dół; dotyczy skrajnie lewego slotu na panelu)\n- Za każde (wartość/20): 1 Ochrony (maks. 2; zaokrąglone w dół)\n- Na koniec tury wartość rośnie o 10\n※ Maksymalnie 20 na turę
501. [Słowo kluczowe [ArrowShiFau] — nazwa] 화살 - 시
   źródło: BattleKeywords.json :: dataList[id=ArrowShiFau].name
   kontekst: identyfikator tagu w tekstach: `[ArrowShiFau]`
   limit: do 40 znaków
   EN: Arrow - Shi
   PL: Strzała - Shi
502. [Słowo kluczowe [ArrowShiFau] — opis] - 최솟값: 0\n- 최댓값: 4\n- 특정 스킬 사용 시 화살이 소모됨
   źródło: BattleKeywords.json :: dataList[id=ArrowShiFau].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min Capacity: 0\n- Max Capacity: 4\n- Arrows spent by certain Skills
   PL: - Min.: 0\n- Maks.: 4\n- Zużywana przy użyciu określonych Umiejętności
503. [Słowo kluczowe [ArrowInTheEyeFau] — nazwa] 박힌 화살
   źródło: BattleKeywords.json :: dataList[id=ArrowInTheEyeFau].name
   kontekst: identyfikator tagu w tekstach: `[ArrowInTheEyeFau]`
   limit: do 40 znaków
   EN: Lodged Arrow
   PL: Wbita Strzała
504. [Słowo kluczowe [ArrowInTheEyeFau] — opis] - 최댓값: 4\n- 턴 시작 시 출혈 위력을 수치만큼 획득\n- 방어 레벨이 수치만큼 감소\n- 턴 종료 시 수치가 2 이상이면 다음 턴에 취약 1 얻음 (턴당 1회)\n- 사망, 퇴각, 효과 해제 및 소멸 시 이 효과가 소멸하고, 동부 시 협회 3과 파우스트에 화살 - 시를 수치만큼 부여
   źródło: BattleKeywords.json :: dataList[id=ArrowInTheEyeFau].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn Start: gain Bleed Potency by Stack\n- Lose Defense Level by Stack\n- Turn End: at 2+ Stack, gain 1 Fragile next turn (once per turn)\n- Expires on: Death, Retreat, buff removal/expiration. When it expires, apply Arrow - Shi to Shi East Section 3 Faust by Stack
   PL: - Maks.: 4\n- Na początku tury zyskuje Moc Krwawienia równą wartości\n- Poziom Obrony maleje o wartość\n- Na koniec tury, przy wartości 2 lub wyższej, zyskuje 1 Wrażliwości w następnej turze (raz na turę)\n- Po śmierci, Odwrócie lub usunięciu efektu nadaje tyle Strzał - Shi, ile wynosiła wartość, osobowości Shi Wschodnia Sekcja 3 Faust
505. [Słowo kluczowe [AimForTheGoal] — nazwa] 목표 조준
   źródło: BattleKeywords.json :: dataList[id=AimForTheGoal].name
   kontekst: identyfikator tagu w tekstach: `[AimForTheGoal]`
   limit: do 40 znaków
   EN: Target Aim
   PL: Namierzenie Celu
506. [Słowo kluczowe [AimForTheGoal] — opis] - 최댓값: 4\n- 저격 자세가 없다면 소멸
   źródło: BattleKeywords.json :: dataList[id=AimForTheGoal].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Expires if this unit does not have "Ready to Loose"
   PL: - Maks.: 4\n- Znika, gdy jednostka nie ma „Postawy Snajperskiej”
507. [Słowo kluczowe [SnipingArrowMode] — nazwa] 저격 자세
   źródło: BattleKeywords.json :: dataList[id=SnipingArrowMode].name
   kontekst: identyfikator tagu w tekstach: `[SnipingArrowMode]`
   limit: do 40 znaków
   EN: Ready to Loose
   PL: Postawa Snajperska
508. [Słowo kluczowe [SnipingArrowMode] — opis] - 이 효과 보유 시 아래 효과 적용\n· 가장 왼쪽에 장착한 기본 공격 스킬을 '섬궁'으로 변경하여 전투 시작 시 사용함.\n· 피해, 흐트러짐 손상 효과로 받는 흐트러짐 피해로 인해 흐트러짐 상태가 되지 않음\n· 원호 공격을 사용하지 않음\n- E.G.O 스킬 장착하여 전투를 시작한 경우, 해제됨
   źródło: BattleKeywords.json :: dataList[id=SnipingArrowMode].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When this unit has this effect, activate the following:\n· Converts the leftmost Base Attack Skill on the Dashboard to "Bow's Glimmer", then uses it at Combat Start\n· This unit cannot be Staggered from taking damage, Tremor Burst, or raised Stagger Threshold\n· Does not trigger <noparse>Assist Attack</noparse>\n· Removed if an E.G.O Skill was equipped at Combat Start
   PL: - Posiadając ten efekt, jednostka:\n· Zamienia skrajnie lewą bazową Umiejętność ataku na „Błysk Łuku” i używa jej na początku walki\n· Nie zostaje oszołomiona przez obrażenia, Wybuch Wstrząsu ani podniesienie Progu Oszołomienia\n· Nie wykonuje Ataków Wsparcia\n- Efekt znika, jeśli na początku walki wyposażono Umiejętność E.G.O
509. [Słowo kluczowe [AStrokeOfDeath] — nazwa] 절명
   źródło: BattleKeywords.json :: dataList[id=AStrokeOfDeath].name
   kontekst: identyfikator tagu w tekstach: `[AStrokeOfDeath]`
   limit: do 40 znaków
   EN: Liferender
   PL: Kres Życia
510. [Słowo kluczowe [AStrokeOfDeath] — opis] - 공격 레벨 2 증가\n- 최종 위력 1 증가\n- 턴 종료 시 소멸
   źródło: BattleKeywords.json :: dataList[id=AStrokeOfDeath].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2\n- Final Power +1\n- Expires at Turn End
   PL: - Poziom Ataku +2\n- Moc Końcowa +1\n- Usuwany na koniec tury
511. [Słowo kluczowe [WOverCharge] — nazwa] 과충전
   źródło: BattleKeywords.json :: dataList[id=WOverCharge].name
   kontekst: identyfikator tagu w tekstach: `[WOverCharge]`
   limit: do 40 znaków
   EN: Overcharge
   PL: Nadładowanie
512. [Słowo kluczowe [WOverCharge] — opis] - 최댓값 : 1\n- 행동 불가 상태가 됨 \n- 받는 피해량 10 + (자신의 충전 위력x5)% 만큼 감소 (최대 25%)\n- 턴 시작 시 자신의 충전 위력만큼 충전 역장을 얻음 (최대 5)\n- 턴 종료 시 다음 턴에 충전 횟수 10, 공격 위력 증가 2 얻고 이 버프 소멸\n- 자신의 충전 위력만큼 자신의 가장 왼쪽 슬롯이 도발치를 얻음 (최대 5)\n- 피격 시 다음 턴에 충전 횟수 1, 부하 1 얻음 (턴 당 최대 5)\n- 자신이 흐트러졌거나, 턴 시작 시 패닉 또는 E.G.O 침식 상태면, 이 버프 소멸
   źródło: BattleKeywords.json :: dataList[id=WOverCharge].desc
   limit: do 670 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value : 1\n- Become Immobilized\n- Take 10 + (Charge Potency on self x 5)% less damage (max 25%)\n- Turn Start: Gain Charge Barrier based on Charge Potency on self (max 5)\n- Turn End: Gain +10 Charge Count and 2 Attack Power Up next turn, and lose this effect\n- Gain Aggro to this unit's leftmost Slot based on Charge Potency on self (max 5)\n- When hit, gain +1 Charge Count and 1 Load next turn (max 5 per turn)\n- If this unit is in Panic or in E.G.O Corrosion at Turn Start, or if this unit is Staggered, lose this effect
   PL: - Maks.: 1\n- Nie może podejmować działań\n- Otrzymywane obrażenia maleją o 10 + (Moc Ładowania x 5)% (maks. 25%)\n- Na początku tury zyskuje Bariery Ładunku równe Mocy Ładowania (maks. 5)\n- Na koniec tury zyskuje w następnej turze 10 Liczników Ładowania i 2 Wzrosty Mocy Ataku, po czym efekt znika\n- Skrajnie lewy slot zyskuje Wartości Prowokacji równe Mocy Ładowania (maks. 5)\n- Przy trafieniu zyskuje w następnej turze 1 Licznik Ładowania i 1 Obciążenia (do 5 razy na turę)\n- W stanie Paniki lub Korozji E.G.O na początku tury albo po oszołomieniu efekt znika
513. [Słowo kluczowe [WOverCharge] — podsumowanie] 행동 불가. 받는 피해량 감소. 도발치, 충전 역장 얻음. 다음 턴에 충전 횟수 얻음. 피격 시 부하, 충전 횟수 얻음
   źródło: BattleKeywords.json :: dataList[id=WOverCharge].summary
   limit: do 170 znaków
   EN: Immobilized. Take less damage. Gain Aggro and Charge Barrier. Gain Charge Count next turn. When hit, gain Load and Charge Count
   PL: Nie może działać. Mniej otrzymywanych obrażeń. Prowokacja i Bariera Ładunku. Liczniki Ładowania w następnej turze. Przy trafieniu: Obciążenie i Liczniki Ładowania
514. [Słowo kluczowe [BloodArmorMeursault] — nazwa] 경혈 갑주
   źródło: BattleKeywords.json :: dataList[id=BloodArmorMeursault].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmorMeursault]`
   limit: do 40 znaków
   EN: Hardblood Armor
   PL: Pancerz Skondensowanej Krwi
515. [Słowo kluczowe [BloodArmorMeursault] — opis] - 최댓값: 5\n- 자신의 체력이 감소한 상태라면, 공격 스킬 종료 시 가한 체력 피해량의 10%만큼 체력을 회복 (턴당 1회, 최대 40회복)\n- 공격 종료 시 체력 피해를 입혔으면 1 감소 (턴당 1회)\n• 색욕 공명 했으면 회복량이 절반으로 감소하는 대신 경혈 갑주 수치가 감소하지 않음
   źródło: BattleKeywords.json :: dataList[id=BloodArmorMeursault].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- If this unit isn't at max HP: after its Skill attack, heal 10% of HP damage dealt (once per turn; max 40 healing)\n- Attack End: If this unit dealt HP damage, lose 1 Stack (once per turn)\n• If Lust Reson. was activated, halve the amount of HP healed, but do not lose any Hardblood Armor Stack
   PL: - Maks.: 5\n- Jeśli HP nie jest pełne: po ataku Umiejętnością leczy 10% zadanych obrażeń HP (raz na turę; maks. 40 leczenia)\n- Po zakończeniu ataku, jeśli zadano obrażenia HP, wartość maleje o 1 (raz na turę)\n• Po Rezonansie Żądzy kwota leczenia maleje o połowę, ale stosy Pancerza Skondensowanej Krwi nie maleją
516. [Słowo kluczowe [FocusOnActing] — nazwa] 연기 집중
   źródło: BattleKeywords.json :: dataList[id=FocusOnActing].name
   kontekst: identyfikator tagu w tekstach: `[FocusOnActing]`
   limit: do 40 znaków
   EN: Focused Performance
   PL: Skupienie na Odgrywaniu
517. [Słowo kluczowe [FocusOnActing] — opis] - 최댓값: 3\n- <라만차랜드> 소속 인격 전용, 강화 스킬 포함\n- 스킬 1, 스킬 2 최종 위력 +1, 수치당 피해량 +5% (최대 15%)\n- 스킬 3 최종 위력 +2, 수치당 피해량 +10% (최대 30%)\n- 스킬 3 공격 종료 시 또는 턴 시작 시 경혈 갑주가 없으면 1 감소
   źródło: BattleKeywords.json :: dataList[id=FocusOnActing].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- <La Manchaland> Identities only; includes Empowered Skills\n- Skill 1 and Skill 2 gain Final Power +1; deal +5% damage for every Stack (max 15%)\n- Skill 3 gains Final Power +2; deals +10% damage for every Stack (max 30%)\n- Lose 1 Stack when:\n  1) Skill 3 Attack End\n  2) If this unit does not have Hardblood Armor at Turn Start
   PL: - Maks.: 3\n- Tylko dla osobowości <La Manchaland>, łącznie z Umiejętnościami Wzmocnionymi\n- Umiejętności 1 i 2: Moc Końcowa +1 oraz +5% obrażeń za stos (maks. 15%)\n- Umiejętność 3: Moc Końcowa +2 oraz +10% obrażeń za stos (maks. 30%)\n- Maleje o 1 po zakończeniu ataku Umiejętnością 3 albo na początku tury bez Pancerza Skondensowanej Krwi
518. [Słowo kluczowe [FocusOnActing] — podsumowanie] 적중시 피해량 증가
   źródło: BattleKeywords.json :: dataList[id=FocusOnActing].summary
   limit: do 120 znaków
   EN: On Hit, deal more damage
   PL: Przy trafieniu zadaje więcej obrażeń
519. [Słowo kluczowe [ParadeConcentration] — nazwa] 라만차 퍼레이드
   źródło: BattleKeywords.json :: dataList[id=ParadeConcentration].name
   kontekst: identyfikator tagu w tekstach: `[ParadeConcentration]`
   limit: do 40 znaków
   EN: La Mancha Parade
   PL: Parada La Mancha
520. [Słowo kluczowe [ParadeConcentration] — opis] - 최댓값: 4\n- 색욕 속성 스킬로 받는 피해량 +10%\n• 공격 대상이 <라만차랜드> 소속 인격이면 스킬 속성에 상관없이 받는 피해량 +20%\n• 수치가 최댓값이면 <라만차랜드> 소속 인격에게 가하는 피해량 -20%\n- 적중 혹은 피격한 스킬 종료 후 1 감소
   źródło: BattleKeywords.json :: dataList[id=ParadeConcentration].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Take +10% damage from Lust Skills\n• If the target is a <La Manchaland> Identity, take +20% damage regardless of the Skill's Affinity\n• At max Stack, deal -20% damage against <La Manchaland> Identities\n- Lose 1 Stack either after this unit's Skill hits and ends or after the Skill that attacked this unit hits and ends
   PL: - Maks.: 4\n- Otrzymuje +10% obrażeń od Umiejętności Żądzy\n• Jeśli atakującym jest osobowość <La Manchaland>, otrzymuje +20% obrażeń niezależnie od atrybutu Umiejętności\n• Przy maksymalnej wartości zadaje -20% obrażeń osobowościom <La Manchaland>\n- Maleje o 1 po trafieniu i zakończeniu własnej Umiejętności lub Umiejętności, która zaatakowała jednostkę
521. [Słowo kluczowe [ParadeConcentration] — podsumowanie] <라만차랜드>소속이면, 피해량 감소
   źródło: BattleKeywords.json :: dataList[id=ParadeConcentration].summary
   limit: do 120 znaków
   EN: <La Manchaland> Identities take less damage
   PL: Osobowości <La Manchaland> otrzymują mniej obrażeń
522. [Słowo kluczowe [EmergencyChargeForceField] — nazwa] 비상용 역장 배터리
   źródło: BattleKeywords.json :: dataList[id=EmergencyChargeForceField].name
   kontekst: identyfikator tagu w tekstach: `[EmergencyChargeForceField]`
   limit: do 40 znaków
   EN: Emergency Barrier Battery
   PL: Awaryjna Bateria Bariery
523. [Słowo kluczowe [EmergencyChargeForceField] — opis] - 최댓값: 7\n- 흐트러짐 상태가 되면, 비상용 역장 배터리를 전부 소모하고, 소모된 수치만큼 충전 역장 얻음
   źródło: BattleKeywords.json :: dataList[id=EmergencyChargeForceField].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- When Staggered, consume all Emergency Barrier Battery Stack and gain Charge Barrier by the Stack consumed
   PL: - Maks.: 7\n- Po oszołomieniu zużywa wszystkie stosy i zyskuje Bariery Ładunku równe zużytej liczbie
524. [Słowo kluczowe [BloodArmorCasting] — nazwa] 주조된 경혈
   źródło: BattleKeywords.json :: dataList[id=BloodArmorCasting].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmorCasting]`
   limit: do 40 znaków
   EN: Hardblood Cast
   PL: Odlew Skondensowanej Krwi
525. [Słowo kluczowe [BloodArmorCasting] — opis] - 최댓값: 3\n- 출혈 또는 특수 출혈을 보유한 적과 합을 진행할 때, 합 위력 +1\n- 공격 스킬에서 혈찬을 소모 시 혈찬이 부족하면, 대신 부족한 혈찬 1당 체력 1 소모하여 혈찬을 생성한 후 혈찬 소모 (이 효과로 인해 받는 피해로 흐트러짐이 되지 않고, 체력이 1 미만으로 감소하지 않음)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=BloodArmorCasting].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When clashing against enemies with Bleed or Unique Bleed, Clash Power +1\n- When consuming Bloodfeast with an Attack Skill, if there isn't enough Bloodfeast, consume 1 HP for every 1 missing Bloodfeast to generate it before consuming it (the damage from this effect does not Stagger or reduce this unit's HP below 1)\n- Reduced by 1 at Turn End
   PL: - Maks.: 3\n- W Starciach z wrogami z Krwawieniem lub Szczególnym Krwawieniem: Moc Starcia +1\n- Zużywając Ucztę Krwi Umiejętnością ataku, przy niedoborze zużywa 1 HP za każdy brakujący 1 Uczty Krwi, by go wygenerować (obrażenia od tego efektu nie powodują oszołomienia i nie redukują HP poniżej 1)\n- Na koniec tury maleje o 1
526. [Słowo kluczowe [HanafudaOne] — nazwa] 짝패 - 송학
   źródło: BattleKeywords.json :: dataList[id=HanafudaOne].name
   kontekst: identyfikator tagu w tekstach: `[HanafudaOne]`
   limit: do 40 znaków
   EN: Hand - Pine Crane Suit
   PL: Ręka - Sosna i Żuraw
527. [Słowo kluczowe [HanafudaOne] — opis] - 스킬 1 기본 위력 +2\n- 자신의 가장 왼쪽 슬롯에 <color=#ff0000>분노</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: BattleKeywords.json :: dataList[id=HanafudaOne].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n
   EN: - Skill 1 Base Power +2\n- When this unit equips and uses a <color=#ff0000>Wrath</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 1 +2\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#ff0000>Gniewu</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
528. [Słowo kluczowe [HanafudaOne] — podsumowanie] 기본 위력 증가
   źródło: BattleKeywords.json :: dataList[id=HanafudaOne].summary
   limit: do 120 znaków
   EN: Gain Base Power
   PL: Zyskuje Moc Bazową
529. [Słowo kluczowe [HanafudaTwo] — nazwa] 짝패 - 억새
   źródło: BattleKeywords.json :: dataList[id=HanafudaTwo].name
   kontekst: identyfikator tagu w tekstach: `[HanafudaTwo]`
   limit: do 40 znaków
   EN: Hand - Susuki Grass Suit
   PL: Ręka - Trawa Susuki
530. [Słowo kluczowe [HanafudaTwo] — opis] - 스킬 2 기본 위력 +1\n- 자신의 가장 왼쪽 슬롯에 <color=#fbc82b>나태</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: BattleKeywords.json :: dataList[id=HanafudaTwo].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#fbc82b>, </color>, \n
   EN: - Skill 2 Base Power +1\n- When this unit equips and uses a <color=#fbc82b>Sloth</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 2 +1\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#fbc82b>Lenistwa</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
531. [Słowo kluczowe [HanafudaTwo] — podsumowanie] 기본 위력 증가
   źródło: BattleKeywords.json :: dataList[id=HanafudaTwo].summary
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
532. [Słowo kluczowe [HanafudaThree] — nazwa] 짝패 - 청벚꽃
   źródło: BattleKeywords.json :: dataList[id=HanafudaThree].name
   kontekst: identyfikator tagu w tekstach: `[HanafudaThree]`
   limit: do 40 znaków
   EN: Hand - Blue Sakura Suit
   PL: Ręka - Błękitna Sakura
533. [Słowo kluczowe [HanafudaThree] — opis] - 스킬 3 기본 위력 +1\n- 자신의 가장 왼쪽 슬롯에 <color=#15c3ee>우울</color> 속성인 기본 공격 스킬 또는 E.G.O 스킬을 장착하고 사용 시 ‘코이코이’의 ‘짝패’ 관련 효과 발동
   źródło: BattleKeywords.json :: dataList[id=HanafudaThree].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: <color=#15c3ee>, </color>, \n
   EN: - Skill 3 Base Power +1\n- When this unit equips and uses a <color=#15c3ee>Gloom</color> Base Attack Skill or E.G.O Skill on its leftmost Skill Slot, activate the "forming a Hand" effects on the "Koi-Koi" Passive
   PL: - Moc Bazowa Umiejętności 3 +1\n- Wyposażając i używając na skrajnie lewym slocie bazowej Umiejętności ataku lub Umiejętności E.G.O atrybutu <color=#15c3ee>Posępności</color>, aktywuje efekt „Ręka” pasywu „Koi-Koi”
534. [Słowo kluczowe [HanafudaThree] — podsumowanie] 기본 위력 증가
   źródło: BattleKeywords.json :: dataList[id=HanafudaThree].summary
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
535. [Słowo kluczowe [HanafudaCombo] — nazwa] 광【光】
   źródło: BattleKeywords.json :: dataList[id=HanafudaCombo].name
   kontekst: identyfikator tagu w tekstach: `[HanafudaCombo]`
   limit: do 40 znaków
   EN: Bright【光】
   PL: Jasne【光】
536. [Słowo kluczowe [HanafudaCombo] — opis] - 위력 : 기본값 0, 최댓값 5\n- 횟수 : 기본값 3, 최댓값 3\n\n- 턴 시작 시 위력당 공격 레벨 증가 1 얻음\n- 턴 시작 시 횟수 1 감소
   źródło: BattleKeywords.json :: dataList[id=HanafudaCombo].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Potency : Base 0, Max 5\n- Count : Base 3, Max 3\n\n- Turn Start: gain 1 Offense Level Up for every Potency\n- Turn Start: lose 1 Stack
   PL: - Moc: baza 0, maks. 5\n- Licznik: baza 3, maks. 3\n\n- Na początku tury za każdą Moc: 1 Wzrost Poziomu Ataku\n- Na początku tury Licznik maleje o 1
537. [Słowo kluczowe [HurtNightStiletto] — nazwa] 상처
   źródło: BattleKeywords.json :: dataList[id=HurtNightStiletto].name
   kontekst: identyfikator tagu w tekstach: `[HurtNightStiletto]`
   limit: do 40 znaków
   EN: Open Wound
   PL: Otwarta Rana
538. [Słowo kluczowe [HurtNightStiletto] — opis] - 최댓값: 2\n- 턴 종료 시 다음 턴에 속박 1 얻음\n- 턴 종료 시 수치가 2면 다음 턴에 깊은 상처로 변환됨
   źródło: BattleKeywords.json :: dataList[id=HurtNightStiletto].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Turn End: Gain 1 Bind next turn\n- Turn End: At 2 Stack, replace this effect with Deep Wound next turn
   PL: - Maks.: 2\n- Na koniec tury zyskuje w następnej turze 1 Spętania\n- Na koniec tury, przy wartości 2, w następnej turze zamienia się w Głęboką Ranę
539. [Słowo kluczowe [HurtNightStiletto] — podsumowanie] 다음 턴에 속박 얻음
   źródło: BattleKeywords.json :: dataList[id=HurtNightStiletto].summary
   limit: do 120 znaków
   EN: Gain Bind next turn
   PL: Zyskuje Spętanie w następnej turze
540. [Słowo kluczowe [CriHurtNightStiletto] — nazwa] 깊은 상처
   źródło: BattleKeywords.json :: dataList[id=CriHurtNightStiletto].name
   kontekst: identyfikator tagu w tekstach: `[CriHurtNightStiletto]`
   limit: do 40 znaków
   EN: Deep Wound
   PL: Głęboka Rana
541. [Słowo kluczowe [CriHurtNightStiletto] — opis] - 기본값: 3\n- 진동 폭발 시 출혈 횟수 1 증가 (턴당 2회)\n- 상처를 얻을 수 없음 (집중 전투일 경우, 부위로 판정)\n- 턴 종료 시 다음 턴에 (수치 - 1)만큼 속박 얻음\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=CriHurtNightStiletto].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- On Tremor Burst, gain +1 Bleed Count (2 times per turn)\n- Cannot gain Open Wound (in Focused Encounters, the Part)\n- Turn End: Gain (Stack - 1) Bind next turn\n- Turn End: Reduce Stack by 1
   PL: - Wartość bazowa: 3\n- Przy Wybuchu Wstrząsu zyskuje 1 Licznik Krwawienia (do 2 razy na turę)\n- Nie może zyskać Otwartej Rany (w walkach skupionych: dotyczy części)\n- Na koniec tury zyskuje w następnej turze (wartość - 1) Spętań\n- Na koniec tury wartość maleje o 1
542. [Słowo kluczowe [CriHurtNightStiletto] — podsumowanie] 출혈 횟수 증가\n다음 턴에 속박 얻음
   źródło: BattleKeywords.json :: dataList[id=CriHurtNightStiletto].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Bleed Count\nGain Bind next turn
   PL: Zyskuje Licznik Krwawienia\nZyskuje Spętanie w następnej turze
543. [Słowo kluczowe [HorrHurtNightStiletto] — nazwa] 치명적인 상처
   źródło: BattleKeywords.json :: dataList[id=HorrHurtNightStiletto].name
   kontekst: identyfikator tagu w tekstach: `[HorrHurtNightStiletto]`
   limit: do 40 znaków
   EN: Fatal Wound
   PL: Rana Śmiertelna
544. [Słowo kluczowe [HorrHurtNightStiletto] — opis] - 기본값: 3\n- 진동 폭발 시 출혈 횟수 3 증가 (턴당 2회)\n- 상처를 얻을 수 없음 (집중 전투일 경우, 부위로 판정)\n- 턴 종료 시 다음 턴에 수치만큼 속박 얻음\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=HorrHurtNightStiletto].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Stack: 3\n- On Tremor Burst, gain +3 Bleed Count (2 times per turn)\n- Cannot gain Open Wound (in Focused Encounters, the Part)\n- Turn End: Gain Bind equal to Stack next turn\n- Turn End: Reduce Stack by 1
   PL: - Wartość bazowa: 3\n- Przy Wybuchu Wstrząsu zyskuje 3 Liczniki Krwawienia (do 2 razy na turę)\n- Nie może zyskać Otwartej Rany (w walkach skupionych: dotyczy części)\n- Na koniec tury zyskuje w następnej turze Spętania równe wartości\n- Na koniec tury wartość maleje o 1
545. [Słowo kluczowe [HorrHurtNightStiletto] — podsumowanie] 출혈 횟수 증가\n다음 턴에 속박 얻음
   źródło: BattleKeywords.json :: dataList[id=HorrHurtNightStiletto].summary
   (powtórzenie elementu 542 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Słowo kluczowe [GrownHorns] — nazwa] 발각[發角]
   źródło: BattleKeywords.json :: dataList[id=GrownHorns].name
   kontekst: identyfikator tagu w tekstach: `[GrownHorns]`
   limit: do 40 znaków
   EN: Burgeoning of Horns [發角]
   PL: Wyrastanie Rogów [發角]
547. [Słowo kluczowe [GrownHorns] — opis] - 최댓값 : 3\n- 자신의 기본 스킬로 적에게 부여하는 파열, 침잠 위력 +1 \n- 턴 종료 시, 1 감소
   źródło: BattleKeywords.json :: dataList[id=GrownHorns].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max value: 3\n- This unit's Base Skills inflict +1 more of Rupture and Sinking Potency\n- Turn End: Lose 1 Stack
   PL: - Maks.: 3\n- Bazowe Umiejętności nadają wrogom o 1 więcej Mocy Rozdarcia i Zatonięcia\n- Na koniec tury wartość maleje o 1
548. [Słowo kluczowe [GrownHorns] — podsumowanie] 부여하는 파열, 침잠 위력 +1
   źródło: BattleKeywords.json :: dataList[id=GrownHorns].summary
   limit: do 120 znaków
   EN: Inflict +1 more of Rupture and Sinking Potency
   PL: Nadaje o 1 więcej Mocy Rozdarcia i Zatonięcia
549. [Słowo kluczowe [CrushMarks] — nazwa] 파쇄흔
   źródło: BattleKeywords.json :: dataList[id=CrushMarks].name
   kontekst: identyfikator tagu w tekstach: `[CrushMarks]`
   limit: do 40 znaków
   EN: Shattermark
   PL: Znamiona Roztrzaskania
550. [Słowo kluczowe [CrushMarks] — opis] - 탐식 속성, 우울 속성 스킬로 피격 시 받는 피해량 +10%\n- 정신력이 있는 대상이면, 패닉 유형이 '파쇄흔'으로 변경됨\n- 정신력이 없는 대상이면, 합 위력 -1\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 파쇄흔 패닉 효과\n- 사기 저하 : 자신의 합 위력 -1, 방어 레벨 -2\n- 패닉 : 자신의 합 위력 -2, 방어 레벨 -3
   źródło: BattleKeywords.json :: dataList[id=CrushMarks].desc
   limit: do 640 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from Gluttony and Gloom Skills\n- SP Units: change their Panic Type to "Shattermark"\n- Non-SP Units: Clash Power -1\n- Turn End: Reduce 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Shattermark Panic-type Effects\n- Low Morale: Clash Power -1, Defense Level -2 on self\n- Panic: Clash Power -2, Defense Level -3 on self
   PL: - Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Znamiona Roztrzaskania”\n- Jednostki bez Poczytalności: Moc Starcia -1\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Znamion Roztrzaskania”\n- Spadek Moralu: Moc Starcia -1 i Poziom Obrony -2\n- Panika: Moc Starcia -2 i Poziom Obrony -3
551. [Słowo kluczowe [CrushMarks] — podsumowanie] 탐식 속성, 우울 속성 스킬 피격 시 받는 피해량 +10%\n- 정신력이 있으면, 패닉 유형이 '파쇄흔'으로 변경\n- 정신력이 없으면, 합 위력 -1
   źródło: BattleKeywords.json :: dataList[id=CrushMarks].summary
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Take +10% damage from Gluttony and Gloom Skills\n- SP Units: change their Panic Type to "Shattermark"\n- Non-SP Units: Clash Power -1
   PL: Otrzymuje +10% obrażeń od Umiejętności Obżarstwa i Posępności\n- Z Poczytalnością: zmienia Panikę na „Znamiona Roztrzaskania”\n- Bez Poczytalności: Moc Starcia -1
552. [Słowo kluczowe [ChickenFightlust] — nazwa] 혈투본능
   źródło: BattleKeywords.json :: dataList[id=ChickenFightlust].name
   kontekst: identyfikator tagu w tekstach: `[ChickenFightlust]`
   limit: do 40 znaków
   EN: Battleblood Instinct
   PL: Instynkt Krwawej Walki
553. [Słowo kluczowe [ChickenFightlust] — opis] - 최댓값: 20\n- 수치 1당 가하는 피해량 +0.75%\n- 수치 10당 턴 종료 시 다음 턴에 신속 1 얻음
   źródło: BattleKeywords.json :: dataList[id=ChickenFightlust].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- For every Stack, deal +0.75% damage\n- For every 10 Stack, gain 1 Haste next turn
   PL: - Maks.: 20\n- Zadaje +0,75% obrażeń za każdą wartość\n- Za każde 10 wartości zyskuje 1 Pośpiechu w następnej turze
554. [Słowo kluczowe [ProtectStanceRyoshu] — nazwa] 호위태세
   źródło: BattleKeywords.json :: dataList[id=ProtectStanceRyoshu].name
   kontekst: identyfikator tagu w tekstach: `[ProtectStanceRyoshu]`
   limit: do 40 znaków
   EN: Protector's Stance
   PL: Postawa Strażnicza
555. [Słowo kluczowe [ProtectStanceRyoshu] — opis] - 최댓값 : 2\n- 받는 피해 (수치 x 10)% 감소\n- 턴 시작 시, 자신의 호흡만큼 보호막 얻음 (최대 20)\n- 턴 종료 시, 호흡 위력 3, 호흡 횟수 1 얻고 다음 턴에 자신의 가장 왼쪽 슬롯 도발치 5 증가\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=ProtectStanceRyoshu].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take (Stack x 10)% less damage\n- Turn Start: Gain Shield by Poise on self (max 20)\n- Turn End: Gain 3 Poise Potency and +1 Poise Count; this unit's leftmost Skill Slot gains +5 Aggro next turn\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Otrzymywane obrażenia maleją o (wartość x 10)%\n- Na początku tury zyskuje Tarczę równą własnemu Oddechowi (maks. 20)\n- Na koniec tury zyskuje 3 Mocy Oddechu i 1 Licznik Oddechu, a skrajnie lewy slot zyskuje +5 Wartości Prowokacji w następnej turze\n- Na koniec tury maleje o 1
556. [Słowo kluczowe [ProtectStanceRyoshu] — podsumowanie] 받는 피해 감소
   źródło: BattleKeywords.json :: dataList[id=ProtectStanceRyoshu].summary
   limit: do 120 znaków
   EN: Take less damage
   PL: Otrzymuje mniej obrażeń
557. [Słowo kluczowe [TheUdjatOutis] — nazwa] 우제트의 눈 [선봉]
   źródło: BattleKeywords.json :: dataList[id=TheUdjatOutis].name
   kontekst: identyfikator tagu w tekstach: `[TheUdjatOutis]`
   limit: do 40 znaków
   EN: The Udjat [Vanguard]
   PL: Oko Udżat [Awangarda]
558. [Słowo kluczowe [TheUdjatOutis] — opis] - 최댓값: 2\n- 속도 최솟값, 최댓값 +3\n- 전투 시작 시 보호 1 얻음\n- 전투 중 아래의 효과 적용 (스킬당 1회, 턴당 3회)\n· 자신이 메인 타겟인 일방 공격 스킬의 첫번째 코인이 앞면으로 나올 확률 절반 감소\n· 합 시작 시 첫 합에서 대상의 모든 코인이 앞면으로 나올 확률 절반 감소\n· 위 효과에서 대상 코인이 마이너스 코인인 경우, 뒷면이 나올 확률로 적용됨\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=TheUdjatOutis].desc
   limit: do 650 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Min & Max Speed +3\n- Combat Start: gain 1 Protection\n- Gain the following effects during the Combat Phase (once per Skill, 3 times per turn)\n· When this unit is the main target of an Unopposed Attack Skill, halve the chance for the Skill's first Coin to flip Heads\n· Clash Start: In the first Clash, halve the target's chance to flip Heads for all of its Coins\n· For both of the above effects, if the target uses Minus Coins, halve their chance to flip Tails instead\n- Turn End: Reduce 1 Stack
   PL: - Maks.: 2\n- Minimalna i maksymalna Szybkość +3\n- Na początku walki zyskuje 1 Ochrony\n- Podczas fazy walki (raz na Umiejętność, 3 razy na turę):\n· Będąc głównym celem ataku niekwestionowanego, zmniejsza o połowę szansę awersu pierwszej monety Umiejętności\n· Na początku Starcia zmniejsza w pierwszym Starciu o połowę szansę awersu wszystkich monet celu\n· Jeśli cel używa monet minus, zamiast tego zmniejsza o połowę szansę rewersu\n- Na koniec tury maleje o 1
559. [Słowo kluczowe [BlueSand] — nazwa] 푸른 모래
   źródło: BattleKeywords.json :: dataList[id=BlueSand].name
   kontekst: identyfikator tagu w tekstach: `[BlueSand]`
   limit: do 40 znaków
   EN: Blue Sand
   PL: Błękitny Piasek
560. [Słowo kluczowe [BlueSand] — opis] - 합 패배 시, 자신의 침잠 횟수 1 증가 (턴당 3회)\n- 정신력이 있는 대상이면, 패닉 유형이 '푸른 모래'로 변경됨\n- 정신력이 없는 대상이면, 속도 최솟값, 최댓값 -1\n- 턴 종료 시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 푸른 모래 패닉 효과\n- 사기 저하 : 자신의 합 위력 -1, 속도 최솟값, 최댓값 -1\n- 패닉 : 자신의 합 위력 -2, 속도 최솟값, 최댓값 -1
   źródło: BattleKeywords.json :: dataList[id=BlueSand].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Clash Lose, gain +1 Sinking Count (3 times per turn)\n- SP Units: change their Panic Type to "Blue Sand"\n- Non-SP Units: Min & Max Speed -1\n- Turn End: Reduce 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Blue Sand Panic Effects\n- Low Morale: Clash Power -1, Min & Max Speed -1\n- Panic: Clash Power -2, Min & Max Speed -1
   PL: - Po przegranej w Starciu zyskuje 1 Licznik Zatonięcia (do 3 razy na turę)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Błękitny Piasek”\n- Jednostki bez Poczytalności: minimalna i maksymalna Szybkość -1\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Błękitnego Piasku”\n- Spadek Moralu: Moc Starcia -1, minimalna i maksymalna Szybkość -1\n- Panika: Moc Starcia -2, minimalna i maksymalna Szybkość -1
561. [Słowo kluczowe [SheutFracture] — nazwa] 셰우트의 균열
   źródło: BattleKeywords.json :: dataList[id=SheutFracture].name
   kontekst: identyfikator tagu w tekstach: `[SheutFracture]`
   limit: do 40 znaków
   EN: Sheut Fracture
   PL: Pęknięcie Sheut
562. [Słowo kluczowe [SheutFracture] — opis] - 특수 침잠\n- 최댓값: 10\n- 수치 1당, 나태 속성, 우울 속성 스킬로 피격 시 받는 피해량 +1%\n- 수치가 최댓값에 도달하면 우울 취약 1 얻음(턴당 1회). 자신의 침잠 위력만큼 우울 피해를 받은 후 소멸 (침잠 횟수 1 감소)\n- 효과를 가진 채 사망하면 정신력이 가장 높은 아군 1명에게 수치의 절반만큼 부여 (소수점 버림)\n- 턴 시작 시 출전 인원 중 LCA 소속 인격이 없으면 소멸
   źródło: BattleKeywords.json :: dataList[id=SheutFracture].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Sinking\n- Max Stack: 10\n- For every Stack, take +1% more damage from Sloth and Gloom Skills\n- At max Stack, gain 1 Gloom Fragility (once per turn), take Gloom damage equal to Sinking Potency on self (lose 1 Sinking Count), then expires\n- If the unit that has this effect dies, transfer half of its Stack to its ally that has the highest SP (rounded down)\n- Turn Start: If there are no LCA Identities on the field, expires
   PL: - Szczególne Zatonięcie\n- Maks.: 10\n- Za każdą wartość: +1% otrzymywanych obrażeń od Umiejętności Lenistwa i Posępności\n- Przy maksymalnej wartości zyskuje 1 Wrażliwości na Posępność (raz na turę), otrzymuje obrażenia Posępnością równe własnej Mocy Zatonięcia (traci 1 Licznik Zatonięcia), po czym znika\n- Po śmierci nosiciela przenosi połowę stosów (zaokrąglona w dół) na sojusznika z najwyższą Poczytalnością\n- Na początku tury znika, jeśli w składzie nie ma osobowości LCA
563. [Słowo kluczowe [LCA_Bullet] — nazwa] LCA 균열탄
   źródło: BattleKeywords.json :: dataList[id=LCA_Bullet].name
   kontekst: identyfikator tagu w tekstach: `[LCA_Bullet]`
   limit: do 40 znaków
   EN: LCA Fracture Round
   PL: Pocisk Rozłamowy LCA
564. [Słowo kluczowe [LCA_Bullet] — opis] - 특수 탄환\n- 최댓값 : 16\n- 특정 스킬 사용 시 소모\n- 탄환이 없을 때 공격이 취소됨
   źródło: BattleKeywords.json :: dataList[id=LCA_Bullet].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Max Capacity: 16\n- Spent by certain Skills\n- Some attacks cancel if lacking Ammo
   PL: - Szczególna amunicja\n- Maks.: 16\n- Zużywana przy użyciu określonych Umiejętności\n- Przy braku amunicji atak zostaje anulowany
565. [Słowo kluczowe [NiddleEGO] — nazwa] 바늘
   źródło: BattleKeywords.json :: dataList[id=NiddleEGO].name
   kontekst: identyfikator tagu w tekstach: `[NiddleEGO]`
   limit: do 40 znaków
   EN: Needle
   PL: Igła
566. [Słowo kluczowe [NiddleEGO] — opis] - 특수 출혈\n- 질투 피해를 받으면, 출혈 횟수 1 증가하고 이 효과 수치 1 감소\n- 턴 종료 시 출혈 1 얻고 수치 1 감소
   źródło: BattleKeywords.json :: dataList[id=NiddleEGO].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Bleed\n- When taking Envy damage, gain +1 Bleed Count and reduce this effect's Stack by 1\n- Turn End: Gain 1 Bleed and reduce this effect's Stack by 1
   PL: - Szczególne Krwawienie\n- Przy otrzymaniu obrażeń Zazdrością zyskuje 1 Licznik Krwawienia, a wartość maleje o 1\n- Na koniec tury zyskuje 1 Krwawienia, a wartość maleje o 1
567. [Słowo kluczowe [NiddleEGO] — podsumowanie] 출혈 횟수 증가
   źródło: BattleKeywords.json :: dataList[id=NiddleEGO].summary
   limit: do 120 znaków
   EN: Gain Bleed Count
   PL: Zyskuje Licznik Krwawienia
568. [Słowo kluczowe [IDMicroChip] — nazwa] 주민등록 마이크로칩
   źródło: BattleKeywords.json :: dataList[id=IDMicroChip].name
   kontekst: identyfikator tagu w tekstach: `[IDMicroChip]`
   limit: do 40 znaków
   EN: Resident Reg. Microchip
   PL: Mikrochip Rejestracji Mieszkańców
569. [Słowo kluczowe [IDMicroChip] — opis] - 최댓값: 2\n- 분노 속성, 질투 속성으로 피격 시 받는 피해량 +10%\n- 합 패배 시 화상 1 얻음 (턴당 최대 3회)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords.json :: dataList[id=IDMicroChip].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Take +10% damage from Wrath and Envy Skills\n- On Clash Lose, gain 1 Burn (3 times per turn)\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Otrzymuje +10% obrażeń od Umiejętności Gniewu i Zazdrości\n- Po przegranej w Starciu zyskuje 1 Podpalenia (do 3 razy na turę)\n- Na koniec tury maleje o 1
570. [Słowo kluczowe [ExtractCoin] — nazwa] 적출 코인
   źródło: BattleKeywords.json :: dataList[id=ExtractCoin].name
   kontekst: identyfikator tagu w tekstach: `[ExtractCoin]`
   limit: do 40 znaków
   EN: Excision Coin
   PL: Moneta Wycięcia
571. [Słowo kluczowe [ExtractCoin] — opis] - 합 진행 시 파괴 불가 코인도 파괴 가능.\n- 합 패배 시 코인이 파괴되지 않음.\n- 공격 스킬에 해당 코인이 있으면, 피격 후 해당 코인으로 공격함.\n- 합 패배 시 파괴되지 않은 코인은 코인 위력이 1이 됨.
   źródło: BattleKeywords.json :: dataList[id=ExtractCoin].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - This Coin can destroy Unbreakable Coins in a Clash.\n- This coin does not break upon Clash Lose.\n- If an Attack Skill has this Coin, attack with this Coin after getting hit.\n- Upon Clash Lose, fix the Coin Power of the unbroken Coin to 1
   PL: - W Starciu może zniszczyć nawet Monetę Niezniszczalną\n- Moneta nie ulega zniszczeniu po przegranej w Starciu\n- Jeśli Umiejętność ataku zawiera tę monetę, atakuje nią po otrzymaniu trafienia\n- Po przegranej w Starciu moc niezniszczonej monety zostaje ustalona na 1
572. [Słowo kluczowe [ReinforcedTattooIshmael] — nazwa] 중지식 강화 문신
   źródło: BattleKeywords.json :: dataList[id=ReinforcedTattooIshmael].name
   kontekst: identyfikator tagu w tekstach: `[ReinforcedTattooIshmael]`
   limit: do 60 znaków
   EN: The Middle Styled Augmentation Tattoos
   PL: Wzmocnione Tatuaże Stylu Środkowego
573. [Słowo kluczowe [ReinforcedTattooIshmael] — opis] - 최댓값: 10\n- 수치 5당 기본 스킬의 최종 위력 +1 (최대 2)\n- 수치 1당 질투 속성 스킬이나 타격 속성 스킬 피해량 +5% (최대 50%)
   źródło: BattleKeywords.json :: dataList[id=ReinforcedTattooIshmael].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Final Power +1 for Base Skills for every 5 Stack (max 2)\n- Envy Skills and Blunt Skills deal +5% damage for every Stack (max 50%)
   PL: - Maks.: 10\n- Moc Końcowa Umiejętności bazowych +1 za każde 5 stosów (maks. 2)\n- Umiejętności Zazdrości i Uderzenia zadają +5% obrażeń za każdą wartość (maks. 50%)
574. [Słowo kluczowe [ResentmentIshmael] — nazwa] 중지 - 원한
   źródło: BattleKeywords.json :: dataList[id=ResentmentIshmael].name
   kontekst: identyfikator tagu w tekstach: `[ResentmentIshmael]`
   limit: do 40 znaków
   EN: The Middle - Grudge
   PL: Środkowy - Uraza
575. [Słowo kluczowe [ResentmentIshmael] — opis] - 최댓값: 15\n- 앙갚음 대상에게 주는 피해량 +20%
   źródło: BattleKeywords.json :: dataList[id=ResentmentIshmael].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 15\n- If target has Vengeance Mark, deal +20% damage
   PL: - Maks.: 15\n- Zadaje +20% obrażeń celom z Celem Odwetu
576. [Słowo kluczowe [HeatingWireIshmael] — nazwa] 열선
   źródło: BattleKeywords.json :: dataList[id=HeatingWireIshmael].name
   kontekst: identyfikator tagu w tekstach: `[HeatingWireIshmael]`
   limit: do 40 znaków
   EN: Thermal Blades
   PL: Ostrza Termiczne
577. [Słowo kluczowe [HeatingWireIshmael] — opis] - 최댓값: 2\n- 기본 스킬을 적중한 대상이 화상을 보유 중이면, 자신의 정신력 3 회복 (턴당 2회)\n- 특정 스킬 코인으로 출혈 부여 시 화상 부여\n- 턴 종료시 1 감소
   źródło: BattleKeywords.json :: dataList[id=HeatingWireIshmael].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- If target hit by Base Skills has Burn, heal 3 SP (2 times per turn)\n- Inflict Burn when inflicting Bleed with certain Skill Coins\n- Turn End: Lose 1 Stack
   PL: - Maks.: 2\n- Jeśli cel trafiony Umiejętnością bazową ma Podpalenie, regeneruje 3 Poczytalności (do 2 razy na turę)\n- Nadając Krwawienie monetami określonych Umiejętności, nadaje Podpalenie\n- Na koniec tury maleje o 1
578. [Słowo kluczowe [LanternGregBigBird] — nazwa] 램프
   źródło: BattleKeywords.json :: dataList[id=LanternGregBigBird].name
   kontekst: identyfikator tagu w tekstach: `[LanternGregBigBird]`
   limit: do 40 znaków
   EN: Lamp
   PL: Lampa
579. [Słowo kluczowe [LanternGregBigBird] — opis] - 최댓값: 8\n- 턴 종료 시 다음 턴에 수치 2당 속박 1 얻음 (최대 4)\n- 턴 종료 시 수치가 최대고 적이 있으면, 수치를 전부 소모하고 다음 턴에 아래 효과 발동\n• 가장 왼쪽 슬롯이 도발치를 10만큼 얻음\n• 현재 체력이 가장 높은 적(본체)에게 현혹 3 부여
   źródło: BattleKeywords.json :: dataList[id=LanternGregBigBird].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 8\n- Turn End: Gain 1 Bind next turn for every 2 Stack (max 4)\n- Turn End: At max Stack, if there are enemies on the field, consume all Stack to activate the following effects next turn:\n• Gain +10 Aggro to the leftmost Slot\n• Inflict 3 Dazzle to the enemy(Core) with the most current HP
   PL: - Maks.: 8\n- Na koniec tury zyskuje w następnej turze 1 Spętania za każde 2 wartości (maks. 4)\n- Na koniec tury, przy maksymalnej wartości i obecności wrogów, zużywa wszystkie stosy, by w następnej turze:\n• Skrajnie lewy slot zyskuje +10 Wartości Prowokacji\n• Wrogowi (Korpusowi) z najwyższym HP nadaje 3 Omamów
580. [Słowo kluczowe [LanternGregBigBird] — podsumowanie] 다음 턴에 속박 얻음
   źródło: BattleKeywords.json :: dataList[id=LanternGregBigBird].summary
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Słowo kluczowe [ObedienceGregBigBird] — nazwa] 숲의 파수꾼
   źródło: BattleKeywords.json :: dataList[id=ObedienceGregBigBird].name
   kontekst: identyfikator tagu w tekstach: `[ObedienceGregBigBird]`
   limit: do 40 znaków
   EN: Guardians of the Forest
   PL: Strażnik Lasu
582. [Słowo kluczowe [ObedienceGregBigBird] — opis] 공격 시작 전 아래 효과 발동\n- 더하기 코인을 사용하는 스킬이면, 정신력 4 회복 (이 효과로 정신력 회복 시 자신의 정신력이 최대면 다음 턴에 공격 레벨 증가 2 얻음)\n- 빼기 코인을 사용하는 스킬이면, 정신력 8 감소 (이 효과로 정신력이 -40 미만이 되지 않음)\n- 이 효과 소멸
   źródło: BattleKeywords.json :: dataList[id=ObedienceGregBigBird].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Before Attack, activate the following effects:\n- Plus Coin Skills heal 4 SP (if already at max SP, gain 2 Offense Level Up next turn)\n- Minus Coin Skills lose 8 SP (this effect cannot reduce the unit's SP below -40)\n- Lose this effect
   PL: Przed atakiem aktywuje poniższe efekty:\n- Umiejętności z monetą plus regenerują 4 Poczytalności (przy pełnej Poczytalności zyskuje w następnej turze 2 Wzrosty Poziomu Ataku)\n- Umiejętności z monetą minus tracą 8 Poczytalności (nie poniżej -40)\n- Efekt znika
583. [Słowo kluczowe [DelusionGregBigBird] — nazwa] 현혹
   źródło: BattleKeywords.json :: dataList[id=DelusionGregBigBird].name
   kontekst: identyfikator tagu w tekstach: `[DelusionGregBigBird]`
   limit: do 40 znaków
   EN: Dazzle
   PL: Omam
584. [Słowo kluczowe [DelusionGregBigBird] — opis] - 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n- 정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n- 정신력이 없는 대상이면, 방어 레벨 -2\n- 턴 종료시 1 감소\n- 이 효과는 합산되지 않고, 갱신됨\n- 패닉 유형을 변경할 수 없는 일부 정신력이 있는 적에게는 정신력이 없는 대상의 효과가 적용됨\n\n※ 현혹 패닉 효과\n- 사기 저하 : 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 2 얻음\n- 패닉 : 턴 종료 시 다음 턴에 속박 1, 공격 레벨 감소 4 얻음
   źródło: BattleKeywords.json :: dataList[id=DelusionGregBigBird].desc
   limit: do 710 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\n- SP Units: Change their Panic Type to "Dazzle"\n- Non-SP Units: Defense Level -2\n- Turn End: Lose 1 Stack\n- This effect is not cumulative; inflicting it will replace the current value with the inflicted value\n- Apply the "Non-SP Units" conditional to certain enemies that have SP but can't change their Panic Types\n\n※ Dazzle Panic-type Effects\n- Low Morale: Turn End: Gain 1 Bind and 2 Offense Level Down next turn\n- Panic: Turn End: Gain 1 Bind and 4 Offense Level Down next turn
   PL: - Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Omam”\n- Jednostki bez Poczytalności: Poziom Obrony -2\n- Na koniec tury maleje o 1\n- Nie kumuluje się — nadanie zastępuje bieżącą wartość\n- Jednostki z Poczytalnością, które nie mogą zmieniać rodzaju Paniki, podlegają regułom jednostek bez Poczytalności\n\n※ Efekty Paniki „Omamu”\n- Spadek Moralu: na koniec tury zyskuje w następnej turze 1 Spętania i 2 Spadki Poziomu Ataku\n- Panika: na koniec tury zyskuje w następnej turze 1 Spętania i 4 Spadki Poziomu Ataku
585. [Słowo kluczowe [DelusionGregBigBird] — podsumowanie] 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n정신력이 없는 대상이면, 방어 레벨 -2
   źródło: BattleKeywords.json :: dataList[id=DelusionGregBigBird].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\nSP Units: Change their Panic Type to "Dazzle"\nNon-SP Units: Defense Level -2
   PL: Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\nZ Poczytalnością: zmienia Panikę na „Omam”\nBez Poczytalności: Poziom Obrony -2
586. [Słowo kluczowe [DelusionGregBigBird_Main] — nazwa] 현혹
   źródło: BattleKeywords.json :: dataList[id=DelusionGregBigBird_Main].name
   kontekst: identyfikator tagu w tekstach: `[DelusionGregBigBird_Main]`
   (powtórzenie elementu 583 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Słowo kluczowe [DelusionGregBigBird_Main] — opis] - 침잠과 화상의 합 1당 기본 공격 스킬로 받는 피해량 +0.5% (최대 10%)\n- 정신력이 있는 대상이면, 패닉 유형이 현혹으로 변경됨\n- 턴 종료시 1 감소
   źródło: BattleKeywords.json :: dataList[id=DelusionGregBigBird_Main].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - For every 1 (Sinking + Burn), take +0.5% damage from Base Attack Skills (max 10%)\n- SP Units: Change their Panic Type to "Dazzle"\n- Turn End: Lose 1 Stack
   PL: - Otrzymuje +0,5% obrażeń od bazowych Umiejętności ataku za każde 1 (suma Zatonięcia i Podpalenia) (maks. 10%)\n- Jednostki z Poczytalnością: zmienia rodzaj Paniki na „Omam”\n- Na koniec tury maleje o 1
