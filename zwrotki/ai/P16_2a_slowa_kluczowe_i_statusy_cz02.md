# Paczka AI P16 (Fala 2 · 2A) — Słowa kluczowe walki i opisy statusów (Bufs / BattleKeywords) (część 2/15)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P16_2a_slowa_kluczowe_i_statusy_cz02.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P16_2a_slowa_kluczowe_i_statusy_cz02.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Słowa kluczowe bitwy — BattleKeywords-a1c5p3
- plik gry: `BattleKeywords-a1c5p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

1. [Słowo kluczowe [AaCePcBt] — nazwa] 원호 공격
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBt].name
   kontekst: identyfikator tagu w tekstach: `[AaCePcBt]`
   limit: do 40 znaków
   EN: Assist Attack
   PL: Atak Wsparcia
2. [Słowo kluczowe [AaCePcBt] — opis] 에이해브의 공격 스킬 종료 시 에이해브가 공격한 대상을 1회 일방 공격함.\n이 때 사용하는 스킬은 '명령을 받들어...' 스킬과 동일한 코인 값, 코인 효과, 공격 레벨을 가짐.
   źródło: BattleKeywords-a1c5p3.json :: dataList[id=AaCePcBt].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: After Ahab's attack, commence unopposed attack against the same target Ahab attacked.\nThe Skill used in this action has the same Offense Level, Coin values and effects as this unit's 'I Follow Orders...' Skill.
   PL: Po zakończeniu Umiejętności ataku Ahaba jednostka wykonuje 1 Atak Jednostronny na cel, którego Ahab zaatakował.\nUmiejętność użyta w ten sposób ma takie same wartości i efekty Monet oraz Poziom Ataku jak Umiejętność „Z rozkazu...” tej jednostki.

## Słowa kluczowe bitwy — BattleKeywords-a1c6p2
- plik gry: `BattleKeywords-a1c6p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

3. [Słowo kluczowe [AaCfPbBe] — nazwa] 사냥감 표시
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBe].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBe]`
   limit: do 40 znaków
   EN: Marked Prey
   PL: Oznaczona Zdobycz
4. [Słowo kluczowe [AaCfPbBe] — opis] - 이번 턴동안 피해 받지 않고 공격 종료시, 열등감 1 부여 이후 소멸\n- 최대 1
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBe].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - If this unit does not take damage during this turn, inflict 1 Inferiority Complex at Attack End then expires\n- Max Stack: 1
   PL: - Przez tę turę nie otrzymuje obrażeń, a po zakończeniu ataku nakłada 1 Kompleksu Niższości, po czym znika\n- Maks. 1
5. [Słowo kluczowe [AaCfPbBf] — nazwa] 열등감
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBf].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBf]`
   limit: do 40 znaków
   EN: Inferiority Complex
   PL: Kompleks Niższości
6. [Słowo kluczowe [AaCfPbBf] — opis] - 피격시마다 받는 체력 피해량의 (20% * 수치)만큼 피해를 입음.\n- 최대 5
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBf].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Every time this unit is hit, take ((20% of HP damage taken) * Value) damage\n- Max Value: 5
   PL: - Przy każdym trafieniu otrzymuje obrażenia HP równe (20% otrzymanych obrażeń HP x wartość)\n- Maks. wartości: 5
7. [Słowo kluczowe [AaCfPbBf] — podsumowanie] 받는 체력 피해량의 (20% * 수치)만큼 피해를 입음.
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBf].summary
   limit: do 120 znaków
   EN: Take ((20% of HP damage taken) * Value) damage
   PL: Otrzymuje obrażenia HP równe (20% otrzymanych obrażeń HP x wartość)
8. [Słowo kluczowe [AaCfPbBa] — nazwa] 폭발하는 우울
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBa].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBa]`
   limit: do 40 znaków
   EN: Explosive Gloom
   PL: Wybuchowa Posępność
9. [Słowo kluczowe [AaCfPbBa] — opis] - 우울 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 대상에게 정신력 피해 3, 자신은 침잠 횟수를 1 얻고, 다음 턴에 공격 레벨 증가 1 얻음 (턴 당 최대 9회 발동)
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBa].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gloom Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: inflict 3 SP damage on the attacker, gain 1 Sinking Count, and gain 1 Offense Level Up next turn (9 times per turn)
   PL: - Odporność na Posępność +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu zadaje atakującemu 3 obrażeń Poczytalności, zyskuje 1 Licznik Zatonięcia i 1 Wzrostu Poziomu Ataku na następną turę (maks. 9 razy na turę)
10. [Słowo kluczowe [AaCfPbBb] — nazwa] 폭발하는 질투
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBb].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBb]`
   limit: do 40 znaków
   EN: Explosive Envy
   PL: Wybuchowa Zawiść
11. [Słowo kluczowe [AaCfPbBb] — opis] - 질투 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 대상에게 공격 레벨 증가 1, 출혈 2, 출혈 횟수 2 부여, 다음 턴에 방어 레벨 감소 1 얻음 (턴 당 최대 9회 발동)
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBb].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Envy Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: apply 1 Offense Level Up, inflict 2 Bleed, and 2 Bleed Count on attacker, and gain 1 Defense Level Down next turn (9 times per turn)
   PL: - Odporność na Zawiść +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu nakłada na atakującego 1 Wzrost Poziomu Ataku, 2 Siły Krwawienia i 2 Liczniki Krwawienia, a w następnej turze zyskuje 1 Spadek Poziomu Obrony (maks. 9 razy na turę)
12. [Słowo kluczowe [AaCfPbBc] — nazwa] 폭발하는 분노
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBc].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBc]`
   limit: do 40 znaków
   EN: Explosive Wrath
   PL: Wybuchowy Gniew
13. [Słowo kluczowe [AaCfPbBc] — opis] - 분노 속성 내성 +0.3\n- 그 외 속성 내성 -0.5\n- 피격 시 다음 턴에 공격 레벨 증가 1, 방어 레벨 감소 1 얻음 (턴 당 최대 9회 발동)
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBc].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Wrath Affinity Resistance +0.3\n- Other Affinity Resistance -0.5\n- When hit: Gain 1 Offense Level Up and 1 Defense Level Down next turn (9 times per turn)
   PL: - Odporność na Gniew +0,3\n- Pozostałe odporności -0,5\n- Przy trafieniu w następnej turze zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony (maks. 9 razy na turę)
14. [Słowo kluczowe [AaCfPbBd] — nazwa] 깊은 상실
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBd].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPbBd]`
   limit: do 40 znaków
   EN: Deep Bereavement
   PL: Głęboka Żałoba
15. [Słowo kluczowe [AaCfPbBd] — opis] 턴 시작 시 속도 5 감소, 방어 레벨 감소 5 얻음
   źródło: BattleKeywords-a1c6p2.json :: dataList[id=AaCfPbBd].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 5 Speed and gain 5 Defense Level Down
   PL: Na początku tury traci 5 Szybkości i zyskuje 5 Spadek Poziomu Obrony

## Słowa kluczowe bitwy — BattleKeywords-a1c6p3
- plik gry: `BattleKeywords-a1c6p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

16. [Słowo kluczowe [AaCfPcBe] — nazwa] 깊은 상실
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBe].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBe]`
   (powtórzenie elementu 14 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
17. [Słowo kluczowe [AaCfPcBe] — opis] 공격 종료 시 정신력 5 피해 입힘.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBe].desc
   limit: do 120 znaków
   EN: Inflict 5 SP damage at Attack End.
   PL: Po zakończeniu ataku zadaje 5 obrażeń Poczytalności.
18. [Słowo kluczowe [AaCfPcBf] — nazwa] 해방되지 못한 서글픔
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBf].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBf]`
   limit: do 40 znaków
   EN: Fettered Woe
   PL: Skuty Żal
19. [Słowo kluczowe [AaCfPcBf] — opis] 특정 조건에서 턴 종료시 3이상이면, 다음 턴에 모든 부위가 흐트러짐 상태가 됨.\n사슬 부위에 취약을 3 얻고 소멸함.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBf].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Under a certain condition, and at 3+ Value, all Parts become Staggered next turn.\nExpires after applying 3 Fragile to the Chain Part
   PL: - Przy określonym warunku, przy wartości 3+ na koniec tury, wszystkie części przechodzą w Oszołomienie w następnej turze.\nNakłada 3 Wrażliwości na część Łańcucha i znika
20. [Słowo kluczowe [AaCfPcBg] — nazwa] 분노의 대상
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBg].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBg]`
   limit: do 40 znaków
   EN: Subject of Wrath
   PL: Cel Gniewu
21. [Słowo kluczowe [AaCfPcBg] — opis] 마음이 찢겨진 히스클리프의 공격에 우선 지정 당함.\n죽음을 맞이할 때, 다른 인격에게 부여가 됨.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBg].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Becomes a priority attack target for Heathcliff the Heartbroken.\nWhen this unit is killed, this effect moves to a different Identity.
   PL: Staje się głównym celem ataków Heathcliffa ze Złamanym Sercem.\nGdy ginie, efekt przenosi się na inną Tożsamość.
22. [Słowo kluczowe [AaCfPcBb] — nazwa] 버틀러의 표식
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBb].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBb]`
   limit: do 40 znaków
   EN: Butler's Mark
   PL: Znak Kamerdynera
23. [Słowo kluczowe [AaCfPcBb] — opis] 특정 공격 스킬의 가중치 증가에 사용됨
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBb].desc
   limit: do 120 znaków
   EN: Used to raise Atk Weight of certain Attack Skills
   PL: Służy do zwiększania Wagi Ataku określonych Umiejętności ataku
24. [Słowo kluczowe [AaCfPcBc] — nazwa] 포박술
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBc].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBc]`
   limit: do 40 znaków
   EN: Binding Technique
   PL: Technika Spętań
25. [Słowo kluczowe [AaCfPcBc] — opis] - 최대 3\n- 턴 종료시 1 증가\n- 턴 종료 시 다음 턴에 속박을 수치만큼 얻음.\n- 턴 종료 시 수치가 3이면, 이번 전투 동안 흐트러짐 상태가 됨.\n 소멸하지 않음.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBc].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max 3\n- Turn End: increases by 1\n- Turn End: gain Bind equal to the Value of this effect.\n- Turn End: if at 3 Value, become Staggered for the rest of the Encounter.\nDoes not expire.
   PL: - Maks. 3\n- Na koniec tury rośnie o 1\n- Na koniec tury zyskuje w następnej turze Spętań w liczbie wartości efektu.\n- Na koniec tury przy wartości 3 przechodzi w stan Oszołomienia na resztę walki.\n Nie znika.
26. [Słowo kluczowe [AaCfPcBc] — podsumowanie] 다음 턴에 속박을 수치만큼 얻음.\n수치가 3이면, 이번 전투 동안 흐트러짐 상태가 됨.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBc].summary
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Bind equal to the Value next turn.\nIf at 3 Value, become Staggered for the rest of the Encounter.
   PL: W następnej turze zyskuje Spętań w liczbie wartości.\nPrzy wartości 3 przechodzi w stan Oszołomienia na resztę walki.
27. [Słowo kluczowe [AaCfPcBh] — nazwa] 고통스러운 분노
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBh].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBh]`
   limit: do 40 znaków
   EN: Excruciating Rage
   PL: Rozdzierający Gniew
28. [Słowo kluczowe [AaCfPcBh] — opis] 공격자에게 폭발하는 분노가 있으면 받는 피해 +100%
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBh].desc
   limit: do 120 znaków
   EN: If the attacker has Explosive Wrath, take +100% damage
   PL: Jeżeli atakujący posiada Wybuchowy Gniew, otrzymuje +100% obrażeń
29. [Słowo kluczowe [AaCfPcBm] — nazwa] 고통의 벼락
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBm].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBm]`
   limit: do 40 znaków
   EN: Lightning of Suffering
   PL: Grom Cierpienia
30. [Słowo kluczowe [AaCfPcBm] — opis] - 합 승리 시 대상에게 찢어지는 마음을 부여하고, 대상에게 체력 피해를 7 준다.\n- 합 패배 또는 일방 공격 종료 시 찢어지는 마음을 얻고, 체력 피해를 7 받는다.\n- 스킬 종료 시 1 감소
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBm].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Win: Inflict Breaking Heart and deal 7 HP damage.\n- Clash Lose or After Unopposed Attack: Gain Breaking Heart and take 7 HP damage.\n- Reduced by 1 at Skill End
   PL: - Po wygranym Starciu nakłada na cel Rwające Serce i zadaje 7 obrażeń HP.\n- Po przegranej w Starciu lub po Ataku Jednostronnym zyskuje Rwające Serce i otrzymuje 7 obrażeń HP.\n- Na koniec Umiejętności maleje o 1
31. [Słowo kluczowe [AaCfPcBn] — nazwa] 찢어지는 마음
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBn].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBn]`
   limit: do 40 znaków
   EN: Breaking Heart
   PL: Rwające Serce
32. [Słowo kluczowe [AaCfPcBn] — opis] - (수치 X 0.2)만큼 모든 죄악 속성 내성 증가\n- 수치가 3이 되면 흐트러짐 상태가 된다.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBn].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Every Sin Affinity Resistance is increased by (Value x 0.2)\n- At 3 Value, become Staggered.
   PL: - Zwiększa odporność na wszystkie Grzechy o (wartość x 0,2)\n- Przy wartości 3 przechodzi w stan Oszołomienia.
33. [Słowo kluczowe [AaCfPcBp] — nazwa] 다가갈 용기
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBp].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBp]`
   limit: do 40 znaków
   EN: Courage to Approach
   PL: Odwaga, by się Zbliżyć
34. [Słowo kluczowe [AaCfPcBp] — opis] - 턴 종료시 정신력 10 회복\n- 매 턴마다 공격 위력 증가 3, 보호 5 얻음\n- 피격 시 정신력 5 회복. 다음 턴에 공격 레벨 증가 1 얻음.(턴 당 3회)\n- 턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.\n- 이번 전투동안 생존한 아군이 자신을 제외하여 1명 이상 있을 때, 히스클리프의 체력이 1 미만으로 감소하지 않는다.\n이번 전투동안 자신의 퇴각 관련 기능이 작동하지 않음.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBp].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Heal 10 SP\n- Gain 3 Attack Power Up and 5 Protection every turn\n- When attacked, heal 5 SP. Gain 1 Offense Level Up next turn. (3 times per turn)\n- Turn Start: If at less than 0 SP, gain 3 Attack Power Up.\n- As long as there are 1 or more other surviving ally in this Encounter, Heathcliff's HP does not drop below 1.\nThis unit's Retreat abilities do not activate for the duration of this Encounter.
   PL: - Na koniec tury odzyskuje 10 Poczytalności\n- Co turę zyskuje 3 Wzrostu Mocy Ataku i 5 Ochrony\n- Przy trafieniu odzyskuje 5 Poczytalności. W następnej turze zyskuje 1 Wzrost Poziomu Ataku. (3 razy na turę)\n- Na początku tury, jeżeli Poczytalność jest niższa od 0, zyskuje 3 Wzrostu Mocy Ataku.\n- Dopóki w tej walce żyje co najmniej 1 sojusznik poza Heathcliffem, HP Heathcliffa nie spada poniżej 1.\nW tej walce funkcje wycofania tej jednostki nie działają.
35. [Słowo kluczowe [AaCfPcBo] — nazwa] 각오
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBo].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBo]`
   limit: do 40 znaków
   EN: Determination
   PL: Postanowienie
36. [Słowo kluczowe [AaCfPcBo] — opis] - 턴 종료시 정신력 10 회복\n- 피격 시 다음 턴에 공격 레벨 증가 1 얻음. (턴 당 3회)\n- 턴 시작 시 정신력이 0 미만이면, 공격 위력 증가 3 얻음.\n- 이번 전투동안 생존한 아군이 자신을 제외하여 1명 이상 있을 때, 히스클리프의 체력이 1 미만으로 감소하지 않는다.\n이번 전투동안 퇴각 관련 기능이 작동하지 않음.
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBo].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn End: Heal 10 SP\n- When attacked, gain 1 Offense Level Up next turn. (3 times per turn)\n- Turn Start: If at less than 0 SP, gain 3 Attack Power Up.\n- As long as there are 1 or more other surviving ally in this Encounter, Heathcliff's HP does not drop below 1.\nThis unit's Retreat abilities do not activate for the duration of this Encounter.
   PL: - Na koniec tury odzyskuje 10 Poczytalności\n- Przy trafieniu w następnej turze zyskuje 1 Wzrost Poziomu Ataku. (3 razy na turę)\n- Na początku tury, jeżeli Poczytalność jest niższa od 0, zyskuje 3 Wzrostu Mocy Ataku.\n- Dopóki w tej walce żyje co najmniej 1 sojusznik poza Heathcliffem, HP Heathcliffa nie spada poniżej 1.\nW tej walce funkcje wycofania nie działają.
37. [Słowo kluczowe [AaCfPcBq] — nazwa] 찢긴 마음
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBq].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBq]`
   limit: do 40 znaków
   EN: Broken Heart
   PL: Złamane Serce
38. [Słowo kluczowe [AaCfPcBq] — opis] - 최대 속도 값 +2\n- 매 턴마다 피해량 증가, 취약 3 얻음\n- 메인 공격 대상이 히스클리프면 공격 스킬의 최종 위력 +2\n- 히스클리프에게 합 패배 시 다음 턴에 속박 3, 피해량 감소 3 얻음
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBq].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Speed +2\n- Gain 3 Damage Up and 3 Fragile every turn\n- If the main target is Heathcliff, the Attack Skill gains Final Power +2\n- Clash Lose against Heathcliff: gain 3 Bind and 3 Damage Down next turn
   PL: - Maks. Szybkość +2\n- Co turę zyskuje 3 Wzrostu Obrażeń i 3 Wrażliwości\n- Jeżeli głównym celem jest Heathcliff, Umiejętność ataku zyskuje Moc Końcowa +2\n- Po przegranej w Starciu z Heathcliffem w następnej turze zyskuje 3 Spętań i 3 Spadku Obrażeń
39. [Słowo kluczowe [AaCfPcBr] — nazwa] 고통 속에서...비참하게 깨어나기를!
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBr].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBr]`
   limit: do 40 znaków
   EN: May She... Wake in Torment!
   PL: Niech się... Przebudzi w Męce!
40. [Słowo kluczowe [AaCfPcBr] — opis] 고통의 벼락이 부여된 대상과 합 진행 시 합 위력 -6
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBr].desc
   limit: do 120 znaków
   EN: Clash Power -6 in a Clash against targets with Lightning of Suffering
   PL: Moc Starcia -6 w Starciu z celami posiadającymi Grom Cierpienia
41. [Słowo kluczowe [AaCfPcBi] — nazwa] 고열기전
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBi].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBi]`
   limit: do 40 znaków
   EN: Superthermogenesis
   PL: Nadtermogeneza
42. [Słowo kluczowe [AaCfPcBi] — opis] 턴 종료 시 수치에 비례하여 고정 피해를 받고 효과 소멸
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBi].desc
   limit: do 120 znaków
   EN: Turn End: Take fixed damage based on Stack and lose this effect
   PL: Na koniec tury otrzymuje obrażenia stałe zależne od wartości i traci efekt
43. [Słowo kluczowe [Unobservable] — nazwa] 관측 불가
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=Unobservable].name
   kontekst: identyfikator tagu w tekstach: `[Unobservable]`
   limit: do 40 znaków
   EN: Unobservable
   PL: Poza Obserwacją
44. [Słowo kluczowe [AaCfPcBs] — nazwa] 방해하지마
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBs].name
   kontekst: identyfikator tagu w tekstach: `[AaCfPcBs]`
   limit: do 40 znaków
   EN: Away With You
   PL: Nie Przeszkadzaj
45. [Słowo kluczowe [AaCfPcBs] — opis] 남은 보호막 수치
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=AaCfPcBs].desc
   limit: do 120 znaków
   EN: Remaining Shield Value
   PL: Pozostała wartość Tarczy
46. [Słowo kluczowe [RageResonance] — nazwa] 움켜쥔 분노
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=RageResonance].name
   kontekst: identyfikator tagu w tekstach: `[RageResonance]`
   limit: do 40 znaków
   EN: Seized Wrath
   PL: Uchwycony Gniew
47. [Słowo kluczowe [RageResonance] — opis] 턴 종료 시, 다음 턴에 공격 레벨 증가를 {0} 얻음 (매 턴마다 효과 강화됨)
   źródło: BattleKeywords-a1c6p3.json :: dataList[id=RageResonance].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: gain {0} Offense Level Up next turn (effect intensifies with each turn)
   PL: Na koniec tury zyskuje w następnej turze {0} Wzrostu Poziomu Ataku (efekt nasila się z każdą turą)

## Słowa kluczowe bitwy — BattleKeywords-a1c7p1
- plik gry: `BattleKeywords-a1c7p1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

48. [Słowo kluczowe [BloodScissor] — nazwa] 핏빛 가위날
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissor].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissor]`
   limit: do 40 znaków
   EN: Blood-tinged Scissorblades
   PL: Krwawe Ostrza Nożyc
49. [Słowo kluczowe [BloodScissor] — opis] - 최댓값 : 10\n- 핏빛 가위날 1단계\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Blood-tinged Scissorblades\n- Used for special skills
   PL: - Maks. wartości: 10\n- Krwawe Ostrza Nożyc 1. stopnia\n- Służy Umiejętnościom specjalnym
50. [Słowo kluczowe [BloodScissorTwo] — nazwa] 핏빛 가위날 II
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorTwo].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorTwo]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades II
   PL: Krwawe Ostrza Nożyc II
51. [Słowo kluczowe [BloodScissorTwo] — opis] - 최댓값 : 20\n- 핏빛 가위날 2단계\n- 턴 시작시 수치 5당 공격 레벨 증가 1, 방어 레벨 감소 1 얻음\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorTwo].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Blood-tinged Scissorblades\n- Turn Start: gain 1 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- Used for certain Skills
   PL: - Maks. wartości: 20\n- Krwawe Ostrza Nożyc 2. stopnia\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 wartości\n- Służy Umiejętnościom specjalnym
52. [Słowo kluczowe [BloodScissorThree] — nazwa] 핏빛 가위날 III
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorThree].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorThree]`
   limit: do 50 znaków
   EN: Blood-tinged Scissorblades III
   PL: Krwawe Ostrza Nożyc III
53. [Słowo kluczowe [BloodScissorThree] — opis] - 최댓값 : 30\n- 핏빛 가위날 3단계\n- 턴 시작시 수치 5당 공격 레벨 증가 2, 방어 레벨 감소 1 얻음\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorThree].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Blood-tinged Scissorblades\n- Turn Start: gain 2 Offense Level Up and 1 Defense Level Down for every 5 Stack\n- Used for certain Skills
   PL: - Maks. wartości: 30\n- Krwawe Ostrza Nożyc 3. stopnia\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Spadek Poziomu Obrony za każde 5 wartości\n- Służy Umiejętnościom specjalnym
54. [Słowo kluczowe [BloodDinner] — nazwa] 혈찬
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodDinner].name
   kontekst: identyfikator tagu w tekstach: `[BloodDinner]`
   limit: do 40 znaków
   EN: Bloodfeast
   PL: Krwawa Uczta
55. [Słowo kluczowe [BloodDinner] — opis] - 최댓값 : 999\n- 해당 장소에서 발생한 출혈 피해를 저장함\n- 전투 장소가 변경되면, 초기화됨\n- 이 수치는 모든 캐릭터가 공유함\n- 아군 중 같은 턴에 혈찬을 소모하는 상위 권속이 있으면, 해당 캐릭터가 혈찬을 소모할 때까지 혈찬을 소모할 수 없음
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodDinner].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 999\n- Stores all Bleed damage dealt in this zone\n- Resets when moving to a different zone\n- This value is shared by all characters\n- If there is a higher Kindred among the allies who also consumes Bloodfeast, this unit cannot consume Bloodfeast until that ally consumes it first.
   PL: - Maks. wartości: 999\n- Przechowuje obrażenia Krwawienia zadane w tym miejscu\n- Resetuje się przy zmianie miejsca walki\n- Wartość jest współdzielona przez wszystkie postacie\n- Jeżeli wśród sojuszników jest wyższy Pokrewny, który w tej samej turze zużywa Krwawą Ucztę, ta jednostka nie może jej zużyć, dopóki nie zrobi tego tamten sojusznik
56. [Słowo kluczowe [BloodDinner_Accumulation] — nazwa] 누적 소모 혈찬
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodDinner_Accumulation].name
   kontekst: identyfikator tagu w tekstach: `[BloodDinner_Accumulation]`
   limit: do 40 znaków
   EN: Bloodfeast Consumed
   PL: Skonsumowana Krwawa Uczta
57. [Słowo kluczowe [BloodDinner_Accumulation] — opis] - 최댓값 : 999\n- 이번 전투 동안 누적 소모한 혈찬이 표시됨
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodDinner_Accumulation].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 999\n- Displays the total amount of Bloodfeast consumed in this Encounter
   PL: - Maks. wartości: 999\n- Wyświetla łączną liczbę Krwawej Uczty skonsumowanej w tej walce
58. [Słowo kluczowe [FamineBlood_LowMorale] — nazwa] 굶주림
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FamineBlood_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[FamineBlood_LowMorale]`
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
59. [Słowo kluczowe [FamineBlood_LowMorale] — opis] - 사기 저하\n턴 시작 시, 속박 1, 공격 위력 증가 2 얻음.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FamineBlood_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 1 Bind and 2 Attack Power Up.
   PL: - Niskie Morale\nNa początku tury zyskuje 1 Spętanie i 2 Wzrostu Mocy Ataku.
60. [Słowo kluczowe [FamineBlood_Panic] — nazwa] 굶주림
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FamineBlood_Panic].name
   kontekst: identyfikator tagu w tekstach: `[FamineBlood_Panic]`
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
61. [Słowo kluczowe [FamineBlood_Panic] — opis] - 패닉\n턴 시작 시, 속박 2, 공격 위력 증가 4 얻음.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FamineBlood_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: Gain 2 Bind and 4 Attack Power Up.
   PL: - Panika\nNa początku tury zyskuje 2 Spętań i 4 Wzrostu Mocy Ataku.
62. [Słowo kluczowe [DuelDeclaration_Camille] — nazwa] 결투 선포 - 까미유
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=DuelDeclaration_Camille].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclaration_Camille]`
   limit: do 40 znaków
   EN: Declared Duel - Camille
   PL: Wyzwanie na Pojedynek - Camille
63. [Słowo kluczowe [DuelDeclaration_Camille] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1\n공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회)\n부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸.\n다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=DuelDeclaration_Camille].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash between the unit that inflicted Declared Duel and the unit with the status, the declarer has +1 Clash Power. On Hit, the declarer gains 1 Haste next turn. (4 times per turn)\n- Expires when the unit inflicts Declared Duel on a different target. \n- Replaced when another unit inflicts Declared Duel on the same target.
   PL: W Starciu między jednostką, która nałożyła Wyzwanie na Pojedynek, a jednostką z tym efektem wyzywająca ma Moc Starcia +1.\nPrzy trafieniu w następnej turze zyskuje 1 Pośpiechu. (maks. 4 razy na turę)\nEfekt znika, gdy wyzywająca jednostka nałoży go na inny cel.\nZastępowany, gdy inna postać nałoży Wyzwanie na Pojedynek.
64. [Słowo kluczowe [RecklessDuel] — nazwa] 무모한 결투
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RecklessDuel].name
   kontekst: identyfikator tagu w tekstach: `[RecklessDuel]`
   limit: do 40 znaków
   EN: Foolhardy Duel
   PL: Nieostrożny Pojedynek
65. [Słowo kluczowe [RecklessDuel] — opis] 턴 종료시 전투 중 전체 체력의 잃어버린 체력 10%당 다음 턴에 합 위력 증가를 얻음. (최대 5)\n턴 종료시 전투 중 전체 체력의 잃어버린 체력 10%당 다음 턴에 속박을 얻음. (최대 5)
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RecklessDuel].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: gain 1 Clash Power Up next turn for every 10% of the missing HP. (max 5)\nTurn End: gain 1 Bind next turn for every 10% of the missing HP. (max 5)
   PL: Na koniec tury zyskuje 1 Wzrost Mocy Starcia na następną turę za każde 10% brakującego HP. (maks. 5)\nNa koniec tury zyskuje 1 Spętanie na następną turę za każde 10% brakującego HP. (maks. 5)
66. [Słowo kluczowe [ConcentratedAttack] — nazwa] 집중 공격
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=ConcentratedAttack].name
   kontekst: identyfikator tagu w tekstach: `[ConcentratedAttack]`
   limit: do 40 znaków
   EN: Focused Attack
   PL: Atak Skupiony
67. [Słowo kluczowe [ConcentratedAttack] — opis] 이전 턴에 공격 성공한 슬롯에 스킬 사용시 누적된 공격 성공 턴 수에 따라 다음과 같은 효과를 얻음.\n- 공격 성공 누적 1턴: 합 위력 +1\n- 공격 성공 누적 2턴: 기본 위력 + 1\n- 공격 성공 누적 3턴: 기본 위력 + 1, 코인 위력 + 1
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=ConcentratedAttack].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n
   EN: When using a Skill against the same Slot this unit successfully hit last turn, gain the following effects based on the number of consecutive turns it successfully hit the Slot\n- 1 Consecutive hit: Clash Power +1\n- 2 Consecutive hits: Base Power +1\n- 3 Consecutive hits: Base Power +1, Coin Power +1
   PL: Gdy używa Umiejętności na slocie, w który w poprzedniej turze udało mu się trafić, zyskuje efekty zależne od liczby kolejnych tur trafień\n- 1 tura z rzędu: Moc Starcia +1\n- 2 tury z rzędu: Moc Bazowa +1\n- 3 tury z rzędu: Moc Bazowa +1, Moc Monety +1
68. [Słowo kluczowe [TrulyWeak] — nazwa] 약자
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=TrulyWeak].name
   kontekst: identyfikator tagu w tekstach: `[TrulyWeak]`
   limit: do 40 znaków
   EN: The Weak
   PL: Słabeusz
69. [Słowo kluczowe [TrulyWeak] — opis] - 가하는 피해량 -10%
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=TrulyWeak].desc
   limit: do 120 znaków
   EN: - Damage Dealt -10%
   PL: - Zadaje obrażenia -10%
70. [Słowo kluczowe [RealPaperBear] — nazwa] 진짜 곰
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RealPaperBear].name
   kontekst: identyfikator tagu w tekstach: `[RealPaperBear]`
   limit: do 40 znaków
   EN: An Actual Bear
   PL: Prawdziwy Niedźwiedź
71. [Słowo kluczowe [RealPaperBear] — opis] - 사람까지 잡아먹는 무시무시한 곰
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RealPaperBear].desc
   limit: do 120 znaków
   EN: - It eats people. How fearsome!
   PL: - Zjada ludzi. Jak przerażające!
72. [Słowo kluczowe [BloodScissorScars] — nazwa] 깊게 베인 상처
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorScars].name
   kontekst: identyfikator tagu w tekstach: `[BloodScissorScars]`
   limit: do 40 znaków
   EN: Deep Laceration
   PL: Głębokie Rozcięcie
73. [Słowo kluczowe [BloodScissorScars] — opis] - 출혈 횟수가 3 증가하고, 자신의 출혈이 발동됨. 이후  출혈 횟수 1 감소.\n- 턴 종료 시 제거
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodScissorScars].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +3 Bleed Count and trigger Bleed on self. Then, lose 1 Bleed Count.\n- Expires at Turn End
   PL: - Zyskuje +3 Licznika Krwawienia i wywołuje Krwawienie na sobie. Następnie traci 1 Licznika Krwawienia.\n- Znika na koniec tury
74. [Słowo kluczowe [LineCutting] — nazwa] 재봉 대상
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=LineCutting].name
   kontekst: identyfikator tagu w tekstach: `[LineCutting]`
   limit: do 40 znaków
   EN: Sewing Target
   PL: Cel Szycia
75. [Słowo kluczowe [LineCutting] — opis] - ???의 우선 공격 대상이 됨.\n- 턴 종료 시 제거
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=LineCutting].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Prioritized by ???.\n- Expires at Turn End
   PL: - Staje się głównym celem ataków ???.\n- Znika na koniec tury
76. [Słowo kluczowe [StarvingBarberOne] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=StarvingBarberOne].name
   kontekst: identyfikator tagu w tekstach: `[StarvingBarberOne]`
   limit: do 40 znaków
   EN: Withered
   PL: Zwiędnięcie
77. [Słowo kluczowe [StarvingBarberOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=StarvingBarberOne].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 15 Base Offense Level\n- Lose 15 Base Defense Level
   PL: - Przez długi, długi czas nie mógł wypić krwi.\n- Podstawowy Poziom Ataku -15\n- Podstawowy Poziom Obrony -15
78. [Słowo kluczowe [StarvingBarberTwo] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=StarvingBarberTwo].name
   kontekst: identyfikator tagu w tekstach: `[StarvingBarberTwo]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
79. [Słowo kluczowe [StarvingBarberTwo] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=StarvingBarberTwo].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 25 Base Offense Level\n- Lose 25 Base Defense Level
   PL: - Przez długi, długi czas nie mógł wypić krwi.\n- Podstawowy Poziom Ataku -25\n- Podstawowy Poziom Obrony -25
80. [Słowo kluczowe [BloodShooting] — nazwa] 블러드슈팅!!
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodShooting].name
   kontekst: identyfikator tagu w tekstach: `[BloodShooting]`
   limit: do 40 znaków
   EN: Blood-shooting!!
   PL: Krwawy Wystrzał!!
81. [Słowo kluczowe [BloodShooting] — opis] 사망 시\n- 혈찬 30 증가\n- 가장 수량이 적은 E.G.O 자원 2 증가\n- 다음 턴에 자신과 같은 팀의 캐릭터의 모든 물리 내성이 0.1 증가. 이 효과는 중첩됨. (최대 5)
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=BloodShooting].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Death:\n- Bloodfeast +30\n- gain 2 E.G.O resource for the least-owned E.G.O resource\n- Next turn: all allies gain 0.1 to all Phys. Resistances. This effect can stack. (max 5)
   PL: Po śmierci\n- Krwawa Uczta +30\n- Zyskuje 2 Zasoby E.G.O najmniej posiadanego Grzechu\n- W następnej turze wszystkie odporności fizyczne postaci z jego drużyny rosną o 0,1. Ten efekt się kumuluje. (maks. 5)
82. [Słowo kluczowe [RighteousFeeling] — nazwa] 정의로운 기분이라네!!
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RighteousFeeling].name
   kontekst: identyfikator tagu w tekstach: `[RighteousFeeling]`
   limit: do 40 znaków
   EN: HOW RIGHTEOUS!!
   PL: Jak to Sprawiedliwie!!
83. [Słowo kluczowe [RighteousFeeling] — opis] - 매 턴 종료 시, 다음 턴에 신속 1, 공격 레벨 증가 3, 방어 레벨 감소 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RighteousFeeling].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At every Turn End: gain 1 Haste, 3 Offense Level Up, and 3 Defense Level Down next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Na koniec każdej tury zyskuje w następnej turze 1 Pośpiech, 3 Wzrostu Poziomu Ataku i 3 Spadek Poziomu Obrony\n- Za każde 3 zsumowane tury zyskuje +2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 1 Wzrost Mocy Starcia (1 raz na turę)
84. [Słowo kluczowe [DuelDeclarationMeursault] — nazwa] 결투 선포 - 뫼르소
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=DuelDeclarationMeursault].name
   kontekst: identyfikator tagu w tekstach: `[DuelDeclarationMeursault]`
   limit: do 40 znaków
   EN: Declared Duel - Meursault
   PL: Wyzwanie na Pojedynek - Meursault
85. [Słowo kluczowe [DuelDeclarationMeursault] — opis] 결투 선포를 부여한 캐릭터가 부여된 캐릭터와 합 진행 시 합 위력 +1\n공격 적중 시 다음 턴에 신속 1을 얻음. (턴 당 최대 4회)\n부여한 캐릭터가 다른 대상에게 이 효과를 부여하면 소멸.\n다른 캐릭터의 결투 선포가 부여될 경우 교체됨.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=DuelDeclarationMeursault].desc
   (powtórzenie elementu 63 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Słowo kluczowe [ConcentratedAttackMeursault] — nazwa] 집중 공격 - 뫼르소
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=ConcentratedAttackMeursault].name
   kontekst: identyfikator tagu w tekstach: `[ConcentratedAttackMeursault]`
   limit: do 40 znaków
   EN: Focused Attack - Meursault
   PL: Atak Skupiony - Meursault
87. [Słowo kluczowe [ConcentratedAttackMeursault] — opis] <집중 전투 전용>\n집중 공격을 부여한 캐릭터가 대상 슬롯의 집중 공격 수치에 따라 다음 효과를 얻음\n1스택: 합 위력 +1\n2스택: 기본 위력 + 1\n3스택: 기본 위력 + 1, 코인 위력 + 1\n- 부여한 캐릭터가 한 턴 동안 집중 공격이 부여된 슬롯에 공격을 성공하지 못하면, 소멸.\n- 부여한 캐릭터가 다른 슬롯에 이 효과를 부여하면 소멸.\n- 부여된 슬롯에 다른 캐릭터의 집중 공격이 부여될 경우, 교체됨.\n- 다음 턴 시작시 제거된 슬롯에 집중 공격이 있었다면, 해당 부위의 모든 슬롯에 부여된 집중 공격을 편성 순서 순으로 재배치함.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=ConcentratedAttackMeursault].desc
   limit: do 960 znaków
   tokeny: zachowaj dokładnie: \n
   EN: <Focused Encounters Only>\nThe unit that inflicted this Focused Attack gains the following effects based on the target Slot's Focused Attack Stack.\n  · 1x Stack: Gain Clash Power +1\n  · 2x Stack: Gain Base Power +1\n  · 3x Stack: Gain Base Power +1 and Coin Power +1\n- Expires if, for a turn, the unit that inflicted it fails to hit the Slot inflicted with their Focused Attack.\n- Expires if the unit that inflicted Focused Attack inflicts it on a different Slot.\n- Replaced if a different unit inflicts Focused Attack on a Slot already inflicted with Focused Attack.\n- At the start of the next turn, if a Slot inflicted with Focused Attack is no longer present, rearrange all Focused Attacks inflicted against the Slots of that Part in the order of Deployment
   PL: <Wyłącznie walki skupione>\nJednostka, która nałożyła Atak Skupiony, zyskuje następujące efekty zależnie od liczby stosów Ataku Skupionego na celu slocie\n1 stos: Moc Starcia +1\n2 stosy: Moc Bazowa +1\n3 stosy: Moc Bazowa +1, Moc Monety +1\n- Znika, jeżeli przez turę nakładająca jednostka nie trafi slotu z nałożonym swoim Atakiem Skupionym.\n- Znika, gdy jednostka, która nałożyła Atak Skupiony, nałoży go na inny slot.\n- Zastępowany, gdy inna postać nałoży Atak Skupiony na slot, który go już ma.\n- Na początku następnej tury, jeżeli slot z Atakiem Skupionym już nie istnieje, Ataki Skupione nałożone na wszystkie sloty tej części są przearanżowane według kolejności rozmieszczenia
88. [Słowo kluczowe [Duello_LowMorale] — nazwa] 1:1 전력
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=Duello_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Duello_LowMorale]`
   limit: do 40 znaków
   EN: Duel Specialist
   PL: Specjalista od Pojedynków
89. [Słowo kluczowe [Duello_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 증가 2 얻음. 합 패배 시 방어 레벨 감소 1얻음 (턴 당 최대 3). 속도 최솟값 -1
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=Duello_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 2 Offense Level Up. On Clash Lose, gain 1 Defense Level Down(max 3 per turn). Min. Speed -1
   PL: - Niskie Morale\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku. Po przegranej w Starciu zyskuje 1 Spadek Poziomu Obrony (maks. 3 na turę). Min. Szybkość -1
90. [Słowo kluczowe [Duello_Panic] — nazwa] 1:1 전력
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=Duello_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Duello_Panic]`
   (powtórzenie elementu 88 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
91. [Słowo kluczowe [Duello_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 증가 4 얻음. 합 패배 시 방어 레벨 감소 2얻음 (턴 당 최대 6). 속도 최솟값 -1
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=Duello_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 4 Offense Level Up. On Clash Lose, gain 2 Defense Level Down(max 6 per turn). Min. Speed -1
   PL: - Panika\n- Na początku tury zyskuje 4 Wzrostu Poziomu Ataku. Po przegranej w Starciu zyskuje 2 Spadku Poziomu Obrony (maks. 6 na turę). Min. Szybkość -1
92. [Słowo kluczowe [RighteousFeelingSancho] — nazwa] 피눈물을 머금고, 내가 책임지겠다.
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RighteousFeelingSancho].name
   kontekst: identyfikator tagu w tekstach: `[RighteousFeelingSancho]`
   limit: do 70 znaków
   EN: I will take responsibility, through my bloody tears.
   PL: Zapłakawszy krwawymi łzami, wezmę to na siebie.
93. [Słowo kluczowe [RighteousFeelingSancho] — opis] - 경혈을 얻을 때마다, 경혈을 1 추가로 얻음. (턴 당 최대 5회)\n- 매 턴 종료 시, 다음 턴에 신속 2, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=RighteousFeelingSancho].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 1 additional Hardblood every time this unit gains Hardblood. (5 times per turn)\n- At every Turn End: gain 2 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Za każde zdobycie Twardej Krwi zyskuje dodatkowo 1 Twardej Krwi. (maks. 5 razy na turę)\n- Na koniec każdej tury zyskuje w następnej turze 2 Pośpiechu i 3 Wzrostu Poziomu Ataku\n- Za każde 3 zsumowane tury zyskuje dodatkowo 2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 1 Wzrost Mocy Starcia (1 raz na turę)
94. [Słowo kluczowe [UnfinishedDreamSancho] — nazwa] 물보다 진한 피에서 벗어나지 못하여,
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=UnfinishedDreamSancho].name
   kontekst: identyfikator tagu w tekstach: `[UnfinishedDreamSancho]`
   limit: do 90 znaków
   EN: In which is recounted the thralldom to blood thicker than water.
   PL: W którym mowa o niewoli krwi gęstszej niż woda,
95. [Słowo kluczowe [UnfinishedDreamSancho] — opis] - 경혈을 얻을 때마다, 경혈을 2 추가로 얻음. (턴 당 최대 5회)\n- 매 턴 종료 시, 다음 턴에 신속 2, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=UnfinishedDreamSancho].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain 2 additional Hardblood every time this unit gains Hardblood. (5 times per turn)\n- At every Turn End: gain 2 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 2 Clash Power Up next turn (once per turn)
   PL: - Za każde zdobycie Twardej Krwi zyskuje dodatkowo 2 Twardej Krwi. (maks. 5 razy na turę)\n- Na koniec każdej tury zyskuje w następnej turze 2 Pośpiechu i 3 Wzrostu Poziomu Ataku\n- Za każde 3 zsumowane tury zyskuje dodatkowo 2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 2 Wzrostu Mocy Starcia (1 raz na turę)
96. [Słowo kluczowe [FragmentOfHopeSancho] — nazwa] 고통 받은 가족들을 위해 피의 만찬을 열고,
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FragmentOfHopeSancho].name
   kontekst: identyfikator tagu w tekstach: `[FragmentOfHopeSancho]`
   limit: do 90 znaków
   EN: Which treats the banquet of blood for the Family's suffering.
   PL: W którym urządza się ucztę krwi dla cierpiącej Rodziny,
97. [Słowo kluczowe [FragmentOfHopeSancho] — opis] 수치만큼 합 위력 증가\n가하는 피해량 +10%
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FragmentOfHopeSancho].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain Clash Power Up equal to Stack\nDeal +10% damage
   PL: Zyskuje Wzrost Mocy Starcia w liczbie wartości\nZadaje obrażenia +10%
98. [Słowo kluczowe [FragmentOfHopeTwoSancho] — nazwa] 자식을 등진 어버이를 처단하여 모든 죄악감을 짊어진 어느 혈귀에 대하여
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FragmentOfHopeTwoSancho].name
   kontekst: identyfikator tagu w tekstach: `[FragmentOfHopeTwoSancho]`
   limit: do 100 znaków
   EN: Of how a certain Bloodfiend came to bear the guilt of patricide alone.
   PL: O pewnym Krwiożercy, który po zabiciu rodzica wziął całą winę na siebie,
99. [Słowo kluczowe [FragmentOfHopeTwoSancho] — opis] - 수치당 합 위력 +4\n- 전투 시작 시 자신과 아군에게 보호막 부여\n- 가하는 피해량 +20%\n- 적중시마다 고정 피해 1 입힘
   źródło: BattleKeywords-a1c7p1.json :: dataList[id=FragmentOfHopeTwoSancho].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power +4 for every value\n- Apply Shield to self and all allies at Combat Start\n- Deal +20% damage\n- On Hit, deal 1 fixed damage as well
   PL: - Moc Starcia +4 za każdą wartość\n- Na początku walki nakłada Tarczę na siebie i wszystkich sojuszników\n- Zadaje obrażenia +20%\n- Przy trafieniu zadaje dodatkowo 1 obrażeń stałych

## Słowa kluczowe bitwy — BattleKeywords-a1c7p2
- plik gry: `BattleKeywords-a1c7p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

100. [Słowo kluczowe [BloodyHand] — nazwa] 피로 물든 손
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloodyHand].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHand]`
   limit: do 40 znaków
   EN: Bloodied Hand
   PL: Krwawa Dłoń
101. [Słowo kluczowe [BloodyHand] — opis] - 최댓값: 10\n- 기본값 : 0\n- 수치가 10이면, 자신의 스킬 적중시 파열 1 추가로 부여
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloodyHand].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Base Value: 0\n- At 10 Stack: inflict +1 additional Rupture On Hit with this unit's Skill
   PL: - Maks. wartości: 10\n- Wartość bazowa: 0\n- Przy 10 stosach Umiejętności tej jednostki nakładają przy trafieniu dodatkowe 1 Rozdarcia
102. [Słowo kluczowe [BloomingThorns] — nazwa] 피어나는 가시
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThorns]`
   limit: do 40 znaków
   EN: Blooming Thorn
   PL: Kwitnący Cierń
103. [Słowo kluczowe [BloomingThorns] — opis] - 최댓값 : 10\n- 스킬로 피해를 받을 때, 공격자에게 스택의 절반만큼 출혈을 부여하고 1 감소 (올림하여 처리)
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- When taking damage from Skills, inflict Bleed equal to half of this effect's Stack against the Attacker (rounded up)
   PL: - Maks. wartości: 10\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe połowie stosów (zaokrąglone w górę)
104. [Słowo kluczowe [BloomingThorns] — podsumowanie] 공격자에게 스택 절반만큼 출혈 부여
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns].summary
   limit: do 120 znaków
   EN: Inflict Bleed equal to Stack against the Attacker
   PL: Nakłada na atakującego Krwawienie równe stosom
105. [Słowo kluczowe [BloomingThorns_2nd] — nazwa] 피를 엮은 가시
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_2nd].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThorns_2nd]`
   limit: do 40 znaków
   EN: Bloodwoven Thorn
   PL: Krwawo Utkany Cierń
106. [Słowo kluczowe [BloomingThorns_2nd] — opis] - 피어나는 가시를 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 10\n- 턴 시작 시, 수치 3당 공격 레벨 증가 1 얻음 (최대 3)\n- 스킬로 피해를 받을 때, 공격자에게 스택만큼 출혈을 부여하고 1 감소 (올림하여 처리)\n- 스킬 효과로 적중 시 출혈, 출혈 횟수의 부여량 +1\n- 아군(자신 제외)에게 스킬 코인 효과로 공격 레벨 증가 또는 방어 레벨 증가를 부여할 때, 다음 턴에 합 위력 증가 1을 추가로 부여\n- 혈찬을 소모하는 스킬의 코인 위력 +1
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_2nd].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Blooming Thorn gain this effect instead\n- Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 3 Stack (max 3)\n- When taking damage from Skills, inflict Bleed equal to this effect's Stack against the Attacker, then lose 1 Stack (rounded up)\n- On Hit, inflict +1 more Bleed and Bleed Count with this unit's Skill effects\n- When applying Offense Level Up or Defense Level Up to another ally with Skill Coin effects, apply 1 Clash Power Up next turn as well\n- All Skills that consume Bloodfeast gain Coin Power +1
   PL: - Efekty zdobywające Kwitnący Cierń zdobywają zamiast tego ten efekt\n- Maks. wartości: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 3 stosy (maks. 3)\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe stosom i traci 1 stos (zaokrąglone w górę)\n- Umiejętności tej jednostki nakładają przy trafieniu o 1 więcej Siły Krwawienia i Licznika Krwawienia\n- Gdy sojusznik (poza sobą) nakłada Monetą Umiejętności Wzrost Poziomu Ataku lub Wzrost Poziomu Obrony, nakłada dodatkowo 1 Wzrost Mocy Starcia na następną turę\n- Umiejętności zużywające Krwawą Ucztę zyskują Moc Monety +1
107. [Słowo kluczowe [BloomingThorns_2nd] — podsumowanie] 공격자에게 스택만큼 출혈 부여\n출혈, 출혈 횟수 부여량 +1\n아군일 경우 합 위력 증가 1 부여\n혈찬 소모 스킬일 경우 코인 위력 +1
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_2nd].summary
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict Bleed on the Attacker equal to Stack\nInflict +1 more Bleed Potency & Count\nApply 1 Clash Power Up to allies\nIf the Skill consumes Bloodfeast, Coin Power +1
   PL: Nakłada na atakującego Krwawienie równe stosom\nNakłada o 1 więcej Siły Krwawienia i Licznika Krwawienia\nSojusznikom nakłada 1 Wzrost Mocy Starcia\nJeżeli Umiejętność zużywa Krwawą Ucztę, Moc Monety +1
108. [Słowo kluczowe [BloomingThorns_3rd] — nazwa] 피로 빚은 가시
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_3rd].name
   kontekst: identyfikator tagu w tekstach: `[BloomingThorns_3rd]`
   limit: do 40 znaków
   EN: Bloodmolded Thorn
   PL: Ulepiony z Krwi Cierń
109. [Słowo kluczowe [BloomingThorns_3rd] — opis] - 피어나는 가시를 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 10\n- 턴 시작 시, 수치 2당 공격 레벨 증가 1 얻음 (최대 5)\n- 스킬로 피해를 받을 때, 공격자에게 스택만큼 출혈을 부여하고 1 감소 (올림하여 처리)\n- 스킬 효과로 적중 시 출혈, 출혈 횟수의 부여량 +2\n- 아군(자신 제외)에게 스킬 코인 효과로 공격 레벨 증가 또는 방어 레벨 증가를 부여할 때, 다음 턴에 합 위력 증가 2를 추가로 부여\n- 혈찬을 소모하는 스킬의 코인 위력 +2, 피해량 +50%\n- '퍼레이드는 영원히 반복될거야' 스킬 사용 시, 체력을 회복하는 대신 그 수치만큼 정신력을 회복
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_3rd].desc
   limit: do 840 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Blooming Thorn gain this effect instead\n- Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 2 Stack (max 5)\n- When taking damage from Skills, inflict Bleed equal to this effect's Stack against the Attacker, then lose 1 Stack (rounded up)\n- On Hit, inflict +2 more Bleed and Bleed Count with this unit's Skill effects\n- When applying Offense Level Up or Defense Level Up to another ally with Skill Coin effects, apply 2 Clash Power Up next turn as well\n- All Skills that consume Bloodfeast gain Coin Power +2 and deal +50% damage\n- When using 'The Parade Repeats for Eternity' Skill, instead of healing HP, heal the same value as SP
   PL: - Efekty zdobywające Kwitnący Cierń zdobywają zamiast tego ten efekt\n- Maks. wartości: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 2 stosy (maks. 5)\n- Gdy otrzymuje obrażenia od Umiejętności, nakłada na atakującego Krwawienie równe stosom i traci 1 stos (zaokrąglone w górę)\n- Umiejętności tej jednostki nakładają przy trafieniu o 2 więcej Siły Krwawienia i Licznika Krwawienia\n- Gdy sojusznik (poza sobą) nakłada Monetą Umiejętności Wzrost Poziomu Ataku lub Wzrost Poziomu Obrony, nakłada dodatkowo 2 Wzrostu Mocy Starcia na następną turę\n- Umiejętności zużywające Krwawą Ucztę zyskują Moc Monety +2 i zadają +50% obrażeń\n- Przy użyciu Umiejętności „Parada powtarza się wiecznie” zamiast leczyć HP, leczy tę samą liczbę Poczytalności
110. [Słowo kluczowe [BloomingThorns_3rd] — podsumowanie] 공격자에게 스택만큼 출혈 부여\n출혈, 출혈 횟수 부여량 +2\n아군일 경우 합 위력 증가 2 부여\n혈찬 소모 스킬일 경우 코인 위력 +2, 피해량 +50%
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=BloomingThorns_3rd].summary
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Inflict Bleed on the Attacker equal to Stack\nInflict +2 more Bleed Potency & Count\nApply 2 Clash Power Up to allies\nIf the Skill consumes Bloodfeast, Coin Power +2 and deal +50% damage
   PL: Nakłada na atakującego Krwawienie równe stosom\nNakłada o 2 więcej Siły Krwawienia i Licznika Krwawienia\nSojusznikom nakłada 2 Wzrostu Mocy Starcia\nJeżeli Umiejętność zużywa Krwawą Ucztę, Moc Monety +2 i +50% obrażeń
111. [Słowo kluczowe [FestivalFever] — nazwa] 축제의 열기
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FestivalFever].name
   kontekst: identyfikator tagu w tekstach: `[FestivalFever]`
   limit: do 40 znaków
   EN: Festive Fever
   PL: Gorączka Święta
112. [Słowo kluczowe [FestivalFever] — opis] - 최댓값 : 10\n- 턴 시작 시, 수치 3당 공격 레벨 증가 1 얻음 (최대 3)\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FestivalFever].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Turn Start: gain 1 Offense Level Up per 3 Stack (max 3)\n- Used for special skills
   PL: - Maks.: 10\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 3 stosy (maks. 3)\n- Służy Umiejętnościom specjalnym
113. [Słowo kluczowe [IncompleteParade] — nazwa] 불완전한 퍼레이드
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=IncompleteParade].name
   kontekst: identyfikator tagu w tekstach: `[IncompleteParade]`
   limit: do 40 znaków
   EN: Imperfect Parade
   PL: Niedoskonała Parada
114. [Słowo kluczowe [IncompleteParade] — opis] - 최댓값 : 50\n- 피주머니 사망 시, 2 얻음\n- 혈귀 사망 시, 3 얻음\n- 턴 시작 시, 누적 소모한 수치 5당 취약 1 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=IncompleteParade].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 50\n- Gain 2 when a Bloodbag dies\n- Gain 3 when a Bloodfiend dies\n- Turn Start: gain 1 Fragile every time this unit consumes 5 cumulative Stack
   PL: - Maks. wartości: 50\n- Zyskuje 2, gdy ginie Worek Krwi\n- Zyskuje 3, gdy ginie Krwiożerca\n- Na początku tury zyskuje 1 Wrażliwości za każde 5 skonsumowanych stosów
115. [Słowo kluczowe [FamineBloodDolci_LowMorale] — nazwa] 허무의 굴레
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[FamineBloodDolci_LowMorale]`
   limit: do 40 znaków
   EN: Bridle of Nihility
   PL: Ogłowie Nicości
116. [Słowo kluczowe [FamineBloodDolci_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 위력 증가 1, 방어 레벨 감소 3을 얻음\n- 턴 종료 시, 정신력 5 피해
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Attack Power Up and 3 Defense Level Down\n- Turn End: take 5 SP damage
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony\n- Na koniec tury otrzymuje 5 obrażeń Poczytalności
117. [Słowo kluczowe [FamineBloodDolci_LowMorale] — podsumowanie] 공격 위력 증가 1, 방어 레벨 감소 3 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_LowMorale].summary
   limit: do 120 znaków
   EN: Gain 1 Attack Power Up & 3 Defense Level Down
   PL: Zyskuje 1 Wzrost Mocy Ataku i 3 Spadek Poziomu Obrony
118. [Słowo kluczowe [FamineBloodDolci_Panic] — nazwa] 허무의 굴레
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].name
   kontekst: identyfikator tagu w tekstach: `[FamineBloodDolci_Panic]`
   (powtórzenie elementu 115 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
119. [Słowo kluczowe [FamineBloodDolci_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 위력 증가 2, 방어 레벨 감소 6을 얻음\n- 턴 종료 시, 정신력 10 회복
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: gain 2 Attack Power Up and 6 Defense Level Down\n- Turn End: heal 10 SP
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 6 Spadek Poziomu Obrony\n- Na koniec tury +10 Poczytalności
120. [Słowo kluczowe [FamineBloodDolci_Panic] — podsumowanie] 공격 위력 증가 2, 방어 레벨 감소 6 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodDolci_Panic].summary
   limit: do 120 znaków
   EN: Gain 2 Attack Power Up & 6 Defense Level Down
   PL: Zyskuje 2 Wzrostu Mocy Ataku i 6 Spadek Poziomu Obrony
121. [Słowo kluczowe [StarvingDolcineaOne] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingDolcineaOne].name
   kontekst: identyfikator tagu w tekstach: `[StarvingDolcineaOne]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
122. [Słowo kluczowe [StarvingDolcineaOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingDolcineaOne].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Starved for blood for a long, long time.\n- Lose 35 Base Offense Level\n- Lose 35 Base Defense Level
   PL: - Przez długi, długi czas nie mogła wypić krwi.\n- Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
123. [Słowo kluczowe [StarvingDolcineaServant] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingDolcineaServant].name
   kontekst: identyfikator tagu w tekstach: `[StarvingDolcineaServant]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
124. [Słowo kluczowe [StarvingDolcineaServant] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingDolcineaServant].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
125. [Słowo kluczowe [ThornyFall_LowMorale] — nazwa] 가시
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ThornyFall_LowMorale]`
   limit: do 40 znaków
   EN: Thorns
   PL: Cierń
126. [Słowo kluczowe [ThornyFall_LowMorale] — opis] 합 승리 시, 피해량 증가 1 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].desc
   limit: do 120 znaków
   EN: Clash Win: gain 1 Damage Up
   PL: Po wygranym Starciu zyskuje 1 Wzrost Obrażeń
127. [Słowo kluczowe [ThornyFall_LowMorale] — podsumowanie] 합 승리 시, 피해량 증가 1 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_LowMorale].summary
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
128. [Słowo kluczowe [ThornyFall_Panic] — nazwa] 가시
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ThornyFall_Panic]`
   (powtórzenie elementu 125 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
129. [Słowo kluczowe [ThornyFall_Panic] — opis] 합 승리 시, 피해량 증가 1 얻음\n턴 종료 시, 다음 턴에 합 위력 증가 2 얻음.
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Win: gain 1 Damage Up\nTurn End: gain 2 Clash Power Up next turn
   PL: Po wygranym Starciu zyskuje 1 Wzrost Obrażeń\nNa koniec tury zyskuje 2 Wzrostu Mocy Starcia w następnej turze.
130. [Słowo kluczowe [ThornyFall_Panic] — podsumowanie] 합 승리 시, 피해량 증가 1 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=ThornyFall_Panic].summary
   (powtórzenie elementu 126 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
131. [Słowo kluczowe [HonorableDuel_Don] — nazwa] 명예로운 결투
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=HonorableDuel_Don].name
   kontekst: identyfikator tagu w tekstach: `[HonorableDuel_Don]`
   limit: do 40 znaków
   EN: Honorable Duel
   PL: Honorowy Pojedynek
132. [Słowo kluczowe [HonorableDuel_Don] — opis] 기억 속 모험담\n능력치가 대폭 증가함
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=HonorableDuel_Don].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: A Reminisced Tale of Adventures\nBecome immensely powerful
   PL: Przygodowa opowieść z pamięci\nStatystyki rosną drastycznie
133. [Słowo kluczowe [HonorableDuel_Knight] — nazwa] 명예로운 결투
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=HonorableDuel_Knight].name
   kontekst: identyfikator tagu w tekstach: `[HonorableDuel_Knight]`
   (powtórzenie elementu 131 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
134. [Słowo kluczowe [HonorableDuel_Knight] — opis] 기억 속 모험담
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=HonorableDuel_Knight].desc
   limit: do 120 znaków
   EN: Reminisced Tales of Adventure
   PL: Przygodowe opowieści z pamięci
135. [Słowo kluczowe [StarvingPriestOne] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingPriestOne].name
   kontekst: identyfikator tagu w tekstach: `[StarvingPriestOne]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
136. [Słowo kluczowe [StarvingPriestOne] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 15 감소\n- 기본 방어 레벨 15 감소
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=StarvingPriestOne].desc
   (powtórzenie elementu 77 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
137. [Słowo kluczowe [FamineBloodPriestServant_LowMorale] — nazwa] 굶주림
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodPriestServant_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[FamineBloodPriestServant_LowMorale]`
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
138. [Słowo kluczowe [FamineBloodPriestServant_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 합 위력 증가 1, 방어 레벨 감소 3을 얻음\n- 턴 종료 시, 정신력 5 피해
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodPriestServant_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: gain 1 Clash Power Up and 3 Defense Level Down\n- Turn End: take 5 SP damage
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Starcia i 3 Spadek Poziomu Obrony\n- Na koniec tury 5 obrażeń Poczytalności
139. [Słowo kluczowe [FamineBloodPriestServant_Panic] — nazwa] 굶주림
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodPriestServant_Panic].name
   kontekst: identyfikator tagu w tekstach: `[FamineBloodPriestServant_Panic]`
   (powtórzenie elementu 58 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
140. [Słowo kluczowe [FamineBloodPriestServant_Panic] — opis] - 패닉\n- 턴 시작 시, 합 위력 증가 2, 방어 레벨 감소 6을 얻음\n- 턴 종료 시, 정신력 10 회복
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=FamineBloodPriestServant_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: gain 2 Clash Power Up and 6 Defense Level Down\n- Turn End: heal 10 SP
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Starcia i 6 Spadek Poziomu Obrony\n- Na koniec tury +10 Poczytalności
141. [Słowo kluczowe [UnstoppableFunny] — nazwa] 멈출 수 없는 환희
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=UnstoppableFunny].name
   kontekst: identyfikator tagu w tekstach: `[UnstoppableFunny]`
   limit: do 40 znaków
   EN: Unstoppable Bliss
   PL: Niepowstrzymana Rozkosz
142. [Słowo kluczowe [UnstoppableFunny] — opis] 사망 시\n- 가장 수량이 적은 E.G.O 자원 3종 각각 1씩 증가\n- 적 하나의 출혈 횟수 3 증가 (자신을 처치한 대상을 우선으로 함)\n- 축제의 열기가 5 이상인 모든 아군이 다음 턴에 신속 1 얻음\n- 축제의 열기가 없는 모든 아군이 다음 턴에 합 위력 증가 1 얻음
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=UnstoppableFunny].desc
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Death:\n- Gain 1 E.G.O resource for 3 least-owned E.G.O resources\n- Inflict +3 Bleed Count against an enemy (prioritizes the unit that killed this unit)\n- All allies at 5+ Festive Fever gain 1 Haste next turn\n- All allies without Festive Fever gain 1 Clash Power Up
   PL: Po śmierci\n- Zyskuje po 1 Zasobie E.G.O dla 3 najmniej posiadanych Zasobów E.G.O\n- Nakłada +3 Licznika Krwawienia na wroga (priorytet: jednostka, która ją zabiła)\n- Wszyscy sojusznicy z 5 lub więcej Gorączki Świętej zyskują w następnej turze 1 Pośpiech\n- Wszyscy sojusznicy bez Gorączki Świętej zyskują 1 Wzrost Mocy Starcia
143. [Słowo kluczowe [UnstoppableFunny] — podsumowanie] E.G.O 자원 3종 하나씩 획득\n출혈 횟수 3 증가
   źródło: BattleKeywords-a1c7p2.json :: dataList[id=UnstoppableFunny].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 1 of each 3 E.G.O resources\nInflict +3 Bleed Count
   PL: Zyskuje po 1 z 3 Zasobów E.G.O\nNakłada +3 Licznika Krwawienia

## Słowa kluczowe bitwy — BattleKeywords-a1c7p3
- plik gry: `BattleKeywords-a1c7p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

144. [Słowo kluczowe [BloodyHand_2nd] — nazwa] 피로 물든 손 II
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodyHand_2nd].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHand_2nd]`
   limit: do 40 znaków
   EN: Bloodied Hand II
   PL: Krwawa Dłoń II
145. [Słowo kluczowe [BloodyHand_2nd] — opis] - 피로 물든 손을 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 20\n- 기본값 : 10\n- 수치 6당 공격 레벨 1 증가
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodyHand_2nd].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Bloodied Hand gain this effect instead\n- Max Value: 20\n- Base Value: 10\n- Gain 1 Offense Level for every 6 Stack
   PL: - Efekty zdobywające Krwawą Dłoń zdobywają zamiast tego ten efekt\n- Maks. wartości: 20\n- Wartość bazowa: 10\n- Zyskuje 1 Poziomu Ataku za każde 6 stosów
146. [Słowo kluczowe [BloodyHand_3rd] — nazwa] 피로 물든 손 III
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodyHand_3rd].name
   kontekst: identyfikator tagu w tekstach: `[BloodyHand_3rd]`
   limit: do 40 znaków
   EN: Bloodied Hand III
   PL: Krwawa Dłoń III
147. [Słowo kluczowe [BloodyHand_3rd] — opis] - 피로 물든 손을 얻는 효과가 해당 버프를 얻는 효과로 변경됨\n- 최댓값 : 30\n- 기본값 : 20\n- 공격 위력 1 증가\n- 수치가 30이면, 자신의 스킬 적중시 파열 2, 파열 횟수 1 추가로 부여\n- 수치가 30이면, 자신의 스킬 적중시 자신과 공격 대상에게 서로 출혈 3 부여
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodyHand_3rd].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Any effects that gain Bloodied Hand gain this effect instead\n- Max Value: 30\n- Base Value: 20\n- Gain 1 Attack Power\n- At 30 Stack: On Hit with this unit's Skill, inflict additional 2 Rupture and +1 Rupture Count\n- At 30 Stack: On Hit with this unit's Skill, inflict 3 Bleed both on self and against the target
   PL: - Efekty zdobywające Krwawą Dłoń zdobywają zamiast tego ten efekt\n- Maks. wartości: 30\n- Wartość bazowa: 20\n- Zyskuje 1 Mocy Ataku\n- Przy 30 stosach Umiejętności tej jednostki nakładają przy trafieniu dodatkowe 2 Rozdarcia i +1 Licznika Rozdarcia\n- Przy 30 stosach Umiejętności tej jednostki nakładają przy trafieniu po 3 Siły Krwawienia na sobie i na celu
148. [Słowo kluczowe [WornHeart] — nazwa] 닳아버린 마음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WornHeart].name
   kontekst: identyfikator tagu w tekstach: `[WornHeart]`
   limit: do 40 znaków
   EN: Ailing Heart
   PL: Wytarte Serce
149. [Słowo kluczowe [WornHeart] — opis] - 최대 10 스택\n- 처음부터 3을 가지고 전투 시작.\n- 턴 시작시, 수치 1당 방어 레벨 감소 1 얻음\n- 턴 시작시, 수치 2당 공격 레벨 증가 1 얻음\n- 턴 시작시, 수치가 10이면 취약 3 얻고 정신력 5 감소\n- 수치가 10이면, 자신의 공격 적중시 피해량의 40%만큼 부위와 본체 체력 회복하고 피로 물든 손을 2 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WornHeart].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Enters Encounter with 3 Stack\n- Turn Start: gain 1 Defense Level Down for every Stack\n- Turn Start: gain 1 Offense Level Up for every 2 Stack\n- Turn Start: at 10 Stack, gain 3 Fragile and lose 5 SP\n- At 10 Stack: On Hit, heal 40% of the damage dealt to this unit's Part and Core, and gain 2 Bloodied Hand
   PL: - Maks. 10 stosów\n- Rozpoczyna walkę z 3 stosami\n- Na początku tury zyskuje 1 Spadek Poziomu Obrony za każdy stos\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku za każde 2 stosy\n- Na początku tury przy 10 stosach zyskuje 3 Wrażliwości i traci 5 Poczytalności\n- Przy 10 stosach, gdy jego atak trafia, leczy 40% zadanych obrażeń części i korpusu oraz zyskuje 2 Krwawej Dłoni
150. [Słowo kluczowe [StarvingPriestTwo] — nazwa] 노쇠
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=StarvingPriestTwo].name
   kontekst: identyfikator tagu w tekstach: `[StarvingPriestTwo]`
   (powtórzenie elementu 76 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
151. [Słowo kluczowe [StarvingPriestTwo] — opis] - 오랫동안 피를 마시지 못했다.\n- 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=StarvingPriestTwo].desc
   (powtórzenie elementu 79 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
152. [Słowo kluczowe [Guilt_LowMorale] — nazwa] 죄책감
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Guilt_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Guilt_LowMorale]`
   limit: do 40 znaków
   EN: Guilt
   PL: Poczucie Winy
153. [Słowo kluczowe [Guilt_LowMorale] — opis] 턴 종료 시 다음 턴에 취약, 정신력 회복 효율 감소 1 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Guilt_LowMorale].desc
   limit: do 120 znaków
   EN: Turn End: gain 1 Fragile and SP Heal Efficiency Down next turn
   PL: Na koniec tury w następnej turze zyskuje 1 Wrażliwości i Spadek Wydajności Leczenia Poczytalności
154. [Słowo kluczowe [Guilt_Panic] — nazwa] 죄책감
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Guilt_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Guilt_Panic]`
   (powtórzenie elementu 152 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
155. [Słowo kluczowe [Guilt_Panic] — opis] 턴 종료 시 다음 턴에 취약, 정신력 회복 효율 감소 2 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Guilt_Panic].desc
   limit: do 120 znaków
   EN: Turn End: gain 2 Fragile and SP Heal Efficiency Down next turn
   PL: Na koniec tury w następnej turze zyskuje 2 Wrażliwości i Spadek Wydajności Leczenia Poczytalności
156. [Słowo kluczowe [MentalIncreaseDown] — nazwa] 정신력 회복 효율 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=MentalIncreaseDown].name
   kontekst: identyfikator tagu w tekstach: `[MentalIncreaseDown]`
   limit: do 40 znaków
   EN: SP Heal Efficiency Down
   PL: Słabsze Leczenie Poczytalności
157. [Słowo kluczowe [MentalIncreaseDown] — opis] 정신력 회복 효율이 스택만큼 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=MentalIncreaseDown].desc
   limit: do 120 znaków
   EN: SP Heal Efficiency decreases by the effect's Stack
   PL: Efektywność leczenia Poczytalności maleje o liczbę stosów
158. [Słowo kluczowe [AffectionTeddy] — nazwa] 애착
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=AffectionTeddy].name
   kontekst: identyfikator tagu w tekstach: `[AffectionTeddy]`
   limit: do 40 znaków
   EN: Attachment
   PL: Przywiązanie
159. [Słowo kluczowe [AffectionTeddy] — opis] - 최댓값 : 9\n- 공격자가 이 효과를 보유한 대상을 공격할 때, 수치만큼 합 위력 증가\n- 턴 종료 시, 1 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=AffectionTeddy].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 9\n- When the Attacker attacks the target with this effect, the Attacker gains Clash Power equal to the Stack\n- Turn End: reduce by 1
   PL: - Maks. wartości: 9\n- Gdy atakujący atakuje cel z tym efektem, zyskuje Moc Starcia równą liczbie stosów\n- Na koniec tury maleje o 1
160. [Słowo kluczowe [FaintMemory] — nazwa] 아련한 기억
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FaintMemory].name
   kontekst: identyfikator tagu w tekstach: `[FaintMemory]`
   limit: do 40 znaków
   EN: Faint Memories
   PL: Zamglone Wspomnienia
161. [Słowo kluczowe [FaintMemory] — opis] - 기본값 : 10\n- 턴 시작 시, 수치만큼 방어 레벨 증가를 얻음\n- 합 패배 시, 1 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FaintMemory].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Value: 10\n- Turn Start: gain Defense Level Up equal to the Stack\n- Clash Lose: reduce by 1
   PL: - Wartość bazowa: 10\n- Na początku tury zyskuje Wzrost Poziomu Obrony równy liczbie stosów\n- Po przegranej w Starciu maleje o 1
162. [Słowo kluczowe [CursePackage] — nazwa] 저주 꾸러미
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=CursePackage].name
   kontekst: identyfikator tagu w tekstach: `[CursePackage]`
   limit: do 40 znaków
   EN: Box of Curses
   PL: Pakunek Klątw
163. [Słowo kluczowe [CursePackage] — opis] - 최댓값 : 1\n- 턴 종료시, 공격 위력 감소 1, 수비 위력 감소 1, 공격 레벨 감소 2, 방어 레벨 감소 2를 얻고 수치 1 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=CursePackage].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 1\n- Turn End: gain 1 Attack Power Down, 1 Defense Power Down, 2 Offense Level Down, 2 Defense Level Down, and reduce the Stack of this effect by 1
   PL: - Maks. wartości: 1\n- Na koniec tury zyskuje 1 Spadek Mocy Ataku, 1 Spadek Mocy Obrony, 2 Spadku Poziomu Ataku i 2 Spadek Poziomu Obrony, a wartość maleje o 1
164. [Słowo kluczowe [TinyCarmilla] — nazwa] 작은 카르밀라
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=TinyCarmilla].name
   kontekst: identyfikator tagu w tekstach: `[TinyCarmilla]`
   limit: do 40 znaków
   EN: Little Carmilla
   PL: Mała Carmilla
165. [Słowo kluczowe [TinyCarmilla] — opis] - 최댓값 3\n- 작은 카르밀라를 얻을 때마다 출혈을 2 얻음\n- 턴 종료시, 출혈 횟수 2 증가\n- 턴 종료시, 3이면 대상의 최대 체력 15%만큼 고정 피해를 입히고 모든 적들의 최대 체력의 5% 회복 이후 제거됨
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=TinyCarmilla].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Gain 2 Bleed every time this unit gains Little Carmilla\n- Turn End: gain +2 Bleed Count\n- Turn End: at 3 Stack, take fixed damage equal to 15% of this unit's max HP, heal HP equal to 5% of each enemy's max HP, then this effect expires
   PL: - Maks. 3 stosów\n- Za każde zdobycie Małej Carmilli zyskuje 2 Krwawienia\n- Na koniec tury zyskuje +2 Licznika Krwawienia\n- Na koniec tury przy 3 stosach otrzymuje obrażenia stałe równe 15% Maks. HP i leczy HP równe 5% Maks. HP wszystkich wrogów, po czym efekt znika
166. [Słowo kluczowe [OneDropNutrition] — nazwa] 한 방울의 양분
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=OneDropNutrition].name
   kontekst: identyfikator tagu w tekstach: `[OneDropNutrition]`
   limit: do 40 znaków
   EN: A Drop of Nourishment
   PL: Kropla Pożywienia
167. [Słowo kluczowe [OneDropNutrition] — opis] - 최댓값: 10\n- 자신의 공격으로 체력 회복할 때, 회복한 최대 체력의 비율 10%당, 1 증가\n- 회복한 체력 비율이 표시됨
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=OneDropNutrition].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Gain 1 Stack every time this unit heals 10% of its max HP with its HP-healing Attacks\n- Shows the % of HP healed
   PL: - Maks. 10 stosów\n- Za każde wyleczenie 10% Maks. HP atakami leczącymi HP zyskuje 1 stos\n- Wyświetla procent wyleczonego HP
168. [Słowo kluczowe [ThornNoose] — nazwa] 가시 올가미
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ThornNoose].name
   kontekst: identyfikator tagu w tekstach: `[ThornNoose]`
   limit: do 40 znaków
   EN: Barbed Lasso
   PL: Kolczaste Lasso
169. [Słowo kluczowe [ThornNoose] — opis] - 최댓값: 3\n- 턴 종료 시 파열 2, 파열 횟수 2 증가\n- 턴 종료 시 수치가 1 이상이면, 다음 턴에 속도가 1로 고정됨.\n- 턴 종료 시 수치가 2가 되면, 20의 탐식 피해를 입음.\n- 턴 종료 시 수치가 3이 되면, 다음 턴에 강제 흐트러짐 상태가 됨.  버프 제거 및 연결된 가시 올가미 제거됨.\n- 턴 시작 시 1 증가
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ThornNoose].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn End: gain 2 Rupture and +2 Rupture Count\n- Turn End: at 1+ Stack, fix this unit's Speed to 1.\n- Turn End: at 2 Stack, take 20 Gluttony damage.\n- Turn End: at 3 Stack, become forcibly Staggered next turn. This effect and the connected Barbed Lasso both expire.\n- Gain 1 at Turn Start
   PL: - Maks. 3 stosów\n- Na koniec tury zyskuje 2 Siły Rozdarcia i 2 Licznika Rozdarcia\n- Na koniec tury przy 1+ stosach Szybkość w następnej turze wynosi 1.\n- Na koniec tury przy 2 stosach otrzymuje 20 obrażeń Obżarstwa.\n- Na koniec tury przy 3 stosach przechodzi w wymuszone Oszołomienie w następnej turze; efekt i połączone Kolczaste Lasso znikają.\n- Na początku tury rośnie o 1
170. [Słowo kluczowe [SwirlingBlood] — nazwa] 일렁임【혈귀】
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SwirlingBlood].name
   kontekst: identyfikator tagu w tekstach: `[SwirlingBlood]`
   limit: do 40 znaków
   EN: Shimmering【Bloodfiend】
   PL: Drgnięcie【Krwiożerca】
171. [Słowo kluczowe [SwirlingBlood] — opis] - 이 버프가 있을 때, 피해를 입으면 대상의 공격 종료 시 출혈 5를 부여함.\n- 이 버프가 있는 동안 보호막 체력은 턴 종료 시 사라지지 않음\n- 조건 만족 시, 소멸 및 패턴 변경전까지 취약을 3 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SwirlingBlood].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - While this effect is active: when this unit takes damage, the Attacker gains 5 Bleed at Attack End.\n- While this effect is active: the Shield HP does not expire at Turn End\n- When conditions are met, gain 3 Fragile until this effect expires and this unit gains a new pattern
   PL: - Dopóki ten efekt jest aktywny: gdy otrzymuje obrażenia, atakujący zyskuje 5 Krwawienia po zakończeniu ataku.\n- Dopóki ten efekt jest aktywny: HP Tarczy nie znika na koniec tury\n- Po spełnieniu warunków zyskuje 3 Wrażliwości aż do zniknięcia efektu i zmiany wzorca
172. [Słowo kluczowe [BloodArmor] — nazwa] 경혈
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmor]`
   limit: do 40 znaków
   EN: Hardblood
   PL: Twarda Krew
173. [Słowo kluczowe [BloodArmor] — opis] - 최댓값: 10\n- 경혈 1단계\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Hardblood\n- Used for special Skills
   PL: - Maks. wartości: 10\n- Twarda Krew 1. stopnia\n- Służy specjalnym Umiejętnościom
174. [Słowo kluczowe [BloodArmor_2nd] — nazwa] 경혈 II
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor_2nd].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmor_2nd]`
   limit: do 40 znaków
   EN: Hardblood II
   PL: Twarda Krew II
175. [Słowo kluczowe [BloodArmor_2nd] — opis] - 최댓값: 20\n- 경혈 2단계\n- 턴 시작시 수치 6당 공격 레벨 1, 방어 레벨 1 증가\n- 속도 최솟값, 최댓값 1 증가\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor_2nd].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Hardblood\n- Turn Start: gain 1 Offense Level and Defense Level for every 6 Stack\n- Raise Min & Max Speed values by 1\n- Used for special Skills
   PL: - Maks. wartości: 20\n- Twarda Krew 2. stopnia\n- Na początku tury zyskuje 1 Poziomu Ataku i 1 Poziomu Obrony za każde 6 wartości\n- Podnosi Min. i Maks. Szybkość o 1\n- Służy specjalnym Umiejętnościom
176. [Słowo kluczowe [BloodArmor_3rd] — nazwa] 경혈 III
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor_3rd].name
   kontekst: identyfikator tagu w tekstach: `[BloodArmor_3rd]`
   limit: do 40 znaków
   EN: Hardblood III
   PL: Twarda Krew III
177. [Słowo kluczowe [BloodArmor_3rd] — opis] - 최댓값: 30\n- 경혈 3단계\n- 턴 시작시 수치 6당 공격 레벨 2, 방어 레벨 2 증가\n- 속도 최솟값, 최댓값 2 증가\n- 특수 스킬에 사용됨
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodArmor_3rd].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Hardblood\n- Turn Start: gain 2 Offense Level and Defense Level for every 6 Stack\n- Raise Min & Max Speed values by 2\n- Used for special Skills
   PL: - Maks. wartości: 30\n- Twarda Krew 3. stopnia\n- Na początku tury zyskuje 2 Poziomu Ataku i 2 Poziomu Obrony za każde 6 wartości\n- Podnosi Min. i Maks. Szybkość o 2\n- Służy specjalnym Umiejętnościom
178. [Słowo kluczowe [Dreamy] — nazwa] 꿈결속 망설임
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Dreamy].name
   kontekst: identyfikator tagu w tekstach: `[Dreamy]`
   limit: do 40 znaków
   EN: Dreamy Hesitation
   PL: Senne Wahanie
179. [Słowo kluczowe [Dreamy] — opis] - 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Dreamy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 35 Base Offense Level\n- Lose 35 Base Defense Level
   PL: - Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
180. [Słowo kluczowe [BloodDinner_Common_Accumulation] — nazwa] 공용 누적 소모 혈찬
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodDinner_Common_Accumulation].name
   kontekst: identyfikator tagu w tekstach: `[BloodDinner_Common_Accumulation]`
   limit: do 40 znaków
   EN: Bloodfeast Consumed (shared)
   PL: Krwawa Uczta (wspólna)
181. [Słowo kluczowe [BloodDinner_Common_Accumulation] — opis] 이번 전투 동안 누적 소모한 혈찬
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=BloodDinner_Common_Accumulation].desc
   limit: do 120 znaków
   EN: Total Bloodfeast consumed in this Encounter
   PL: Łączna liczba Krwawej Uczty skonsumowanej w tej walce
182. [Słowo kluczowe [ThirstyRose] — nazwa] 목마른 장미
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ThirstyRose].name
   kontekst: identyfikator tagu w tekstach: `[ThirstyRose]`
   limit: do 40 znaków
   EN: Polydipsic Rose
   PL: Spragniona Róża
183. [Słowo kluczowe [ThirstyRose] — opis] - 최댓값: 5\n- 턴 종료 시 자신의 출혈 위력이 10이상일 때, 자신의 최대 체력 1%만큼 색욕 피해를 입음. (최대 30)\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ThirstyRose].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 5\n- Turn End: at 10+ Bleed Potency, take Lust damage equal to 1% of this unit's max HP. (max 30)\n- Turn End: reduced by 1
   PL: - Maks. wartości: 5\n- Na koniec tury, jeżeli Siła Krwawienia wynosi 10 lub więcej, otrzymuje obrażenia Żądzy równe 1% Maks. HP. (maks. 30)\n- Na koniec tury maleje o 1
184. [Słowo kluczowe [RoseWedge] — nazwa] 장미 쐐기
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RoseWedge].name
   kontekst: identyfikator tagu w tekstach: `[RoseWedge]`
   limit: do 40 znaków
   EN: Rose Wedge
   PL: Klin Róży
185. [Słowo kluczowe [RoseWedge] — opis] - 위력 최댓값 : 10\n- 횟수 최댓값 : 4\n- 출혈 피해를 10 받을 때마다, 위력 1 증가.\n- 피격시 자신에게 스킬 효과로 출혈, 특수 출혈이 부여될 때마다 출혈 2를 얻고, 공격자에게 출혈 1을 부여함. (턴 당 최대 5회)\n· 이 효과의 위력이 10이면, 위 효과 발동 시 추가로 출혈 횟수가 1 증가함.\n- 턴 종료 시 횟수 1 감소\n- 전투 종료 시 위력 10 또는 횟수 1이면, 버프가 소멸하고 (위력 x 10)만큼 색욕 피해를 받음.\n- 부여 대상이 사망하거나 버프 소멸 시 (위력 x 10)만큼 혈찬 증가, 부여 대상의 모든 아군 유닛에게 (위력 x 2)만큼 색욕 피해를 입힘 (최소 1)
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RoseWedge].desc
   limit: do 780 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Potency: 10\n- Max Count: 4\n- Gain 1 Potency every time this unit takes 10 Bleed damage\n- When gaining Bleed or 'Unique Bleed' from getting hit, gain 2 Bleed and inflict 1 Bleed against the Attacker. (5 times per turn)\n· At 10 Potency, gain +1 Bleed Count as well when triggering the above effect.\n- Turn End: lose 1 Count\n- Combat End: at 10 Potency or 1 Count, this effect expires, and this unit takes (Potency x 10) Lust damage.\n- If the unit inflicted with this effect dies, or when this effect expires: increase Bloodfeast by (Potency x 10), and deal (Potency x 2) Lust damage against all of its allies (min 1)
   PL: - Maks. Siły: 10\n- Maks. Licznika: 4\n- Zyskuje 1 Siły za każde otrzymanie 10 obrażeń Krwawienia\n- Przy otrzymaniu od trafienia Krwawienia lub Specjalnego Krwawienia z efektu Umiejętności zyskuje 2 Krwawienia i nakłada 1 Krwawienie na atakującego. (maks. 5 razy na turę)\n· Przy 10 Siły, podczas wywołania powyższego efektu, zyskuje dodatkowo +1 Licznika Krwawienia.\n- Na koniec tury traci 1 Licznika\n- Po zakończeniu walki, przy 10 Siły lub 1 Liczniku, efekt znika, a jednostka otrzymuje (Siła x 10) obrażeń Żądzy.\n- Przy śmierci jednostki z tym efektem lub zniknięciu efektu: Krwawa Uczta rośnie o (Siła x 10), a wszyscy sojusznicy jednostki otrzymują (Siła x 2) obrażeń Żądzy (min. 1)
186. [Słowo kluczowe [FerrisWheel] — nazwa] 돌고도는 관람차
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FerrisWheel].name
   kontekst: identyfikator tagu w tekstach: `[FerrisWheel]`
   limit: do 40 znaków
   EN: The Endless Wheel
   PL: Wieczny Diabelski Młyn
187. [Słowo kluczowe [FerrisWheel] — opis] 곤돌라가 처치될 때마다 1 감소.\n이 수치가 0이고, 다음 턴에 생성될 유닛이 없으면 다음 페이즈로 넘어감.
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FerrisWheel].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduced by 1 every time a Gondola is defeated.\nIf this value is at 0, and if there are no units to be spawned next turn, move on to the next phase.
   PL: Maleje o 1 za każdą pokonaną Gondolę.\nJeżeli wartość wynosi 0, a w następnej turze nie pojawi się żadna jednostka, następuje przejście do następnej fazy.
188. [Słowo kluczowe [StarvingDonqui] — nazwa] 굶주림과 노쇠
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=StarvingDonqui].name
   kontekst: identyfikator tagu w tekstach: `[StarvingDonqui]`
   limit: do 40 znaków
   EN: Starved and Withered
   PL: Wygłodniały i Zwiędnięty
189. [Słowo kluczowe [StarvingDonqui] — opis] - 기본 공격 레벨 10 감소\n- 기본 방어 레벨 10 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=StarvingDonqui].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 10 Base Offense Level\n- Lose 10 Base Defense Level
   PL: - Podstawowy Poziom Ataku -10\n- Podstawowy Poziom Obrony -10
190. [Słowo kluczowe [RegainedStrength] — nazwa] 다시 도는 피의 충동
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength].name
   kontekst: identyfikator tagu w tekstach: `[RegainedStrength]`
   limit: do 40 znaków
   EN: Returning Bloodlust
   PL: Powracający Popęd Krwi
191. [Słowo kluczowe [RegainedStrength] — opis] - 최댓값: 10\n- 다시 도는 피의 충동 1단계
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 10\n- Stage 1 Returning Bloodlust
   PL: - Maks. wartości: 10\n- Powracający Popęd Krwi 1. stopnia
192. [Słowo kluczowe [RegainedStrength_2nd] — nazwa] 다시 도는 피의 충동 II
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength_2nd].name
   kontekst: identyfikator tagu w tekstach: `[RegainedStrength_2nd]`
   limit: do 40 znaków
   EN: Returning Bloodlust II
   PL: Powracający Popęd Krwi II
193. [Słowo kluczowe [RegainedStrength_2nd] — opis] - 최대 20\n- 다시 도는 피의 충동 2단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 1, 방어 레벨 증가 1 얻음\n- 다시 도는 피의 충동을 소모하는 스킬의 합 위력 +1, 해당 스킬에서 부여하는 출혈, 파열의 위력과 횟수 +1
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength_2nd].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 20\n- Stage 2 Returning Bloodlust\n- Turn Start: gain 1 Offense Level up and 1 Defense Level Up for every 5 Value\n- Clash Power +1 to Skills that consume Returning Bloodlust; inflict +1 more of Potency and Count for Bleed and Rupture inflicted by the said Skill
   PL: - Maks. 20\n- Powracający Popęd Krwi 2. stopnia\n- Na początku tury zyskuje 1 Wzrost Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 5 wartości\n- Umiejętności zużywające Powracający Popęd Krwi zyskują Moc Starcia +1 i nakładają o 1 więcej Siły i Licznika Krwawienia oraz Rozdarcia
194. [Słowo kluczowe [RegainedStrength_3rd] — nazwa] 다시 도는 피의 충동 III
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength_3rd].name
   kontekst: identyfikator tagu w tekstach: `[RegainedStrength_3rd]`
   limit: do 40 znaków
   EN: Returning Bloodlust III
   PL: Powracający Popęd Krwi III
195. [Słowo kluczowe [RegainedStrength_3rd] — opis] - 최대 30\n- 다시 도는 피의 충동 3단계\n- 턴 시작시 수치 5 당, 공격 레벨 증가 2, 방어 레벨 증가 1 얻음\n- 다시 도는 피의 충동을 소모하는 스킬의 코인 위력 +1, 해당 스킬에서 부여하는 출혈, 파열의 위력과 횟수 +1
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=RegainedStrength_3rd].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Value: 30\n- Stage 3 Returning Bloodlust\n- Turn Start: gain 2 Offense Level up and 1 Defense Level Up for every 5 Value\n- Coin Power +1 to Skills that consume Returning Bloodlust; inflict +1 more of Potency and Count for Bleed and Rupture inflicted by the said Skill
   PL: - Maks. 30\n- Powracający Popęd Krwi 3. stopnia\n- Na początku tury zyskuje 2 Wzrostu Poziomu Ataku i 1 Wzrost Poziomu Obrony za każde 5 wartości\n- Umiejętności zużywające Powracający Popęd Krwi zyskują Moc Monety +1 i nakładają o 1 więcej Siły i Licznika Krwawienia oraz Rozdarcia
196. [Słowo kluczowe [WeightOfResponsibility_LowMorale] — nazwa] 내 꿈을 버리고 이제는...
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WeightOfResponsibility_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WeightOfResponsibility_LowMorale]`
   limit: do 40 znaków
   EN: Time to abandon my dream...
   PL: Pora porzucić mój sen...
197. [Słowo kluczowe [WeightOfResponsibility_LowMorale] — opis] - 사기 저하\n- 공격 위력 증가 2, 취약  1 얻음, 속도 최댓값 2 증가\n- 체력 회복량 30% 증가\n- 턴 종료 시 턴 시작 시보다 다시 도는 피의 충동의 수치가 낮으면 다음 턴에 공격 레벨 증가 2, 방어 레벨 감소 2 얻음.
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WeightOfResponsibility_LowMorale].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Fragile; raise max Speed value by 2\n- Heal +30% more HP when healing\n- Turn End: if the current Returning Bloodlust is lower than its value at Turn Start, gain 2 Offense Level Up and 2 Defense Level Down
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Wrażliwości; Maks. Szybkość +2\n- Leczenie HP +30%\n- Na koniec tury, jeżeli wartość Powracającego Popędu Krwi jest niższa niż na początku tury, w następnej turze zyskuje 2 Wzrostu Poziomu Ataku i 2 Spadek Poziomu Obrony.
198. [Słowo kluczowe [WeightOfResponsibility_Panic] — nazwa] 어버이로써 가족을 위해....
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WeightOfResponsibility_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WeightOfResponsibility_Panic]`
   limit: do 60 znaków
   EN: ... For my Family, as their Father...
   PL: ... Dla mojej Rodziny, jako jej Ojciec...
199. [Słowo kluczowe [WeightOfResponsibility_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 신속 2, 취약 2 얻음\n- 체력 회복량 50% 증가\n- 턴 종료 시 턴 시작 시보다 다시 도는 피의 충동의 수치가 낮으면 다음 턴에 공격 레벨 증가 3, 방어 레벨 감소 5 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=WeightOfResponsibility_Panic].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up, 2 Haste, and 2 Fragile\n- Heal +50% more HP when healing\n- Turn End: if the current Returning Bloodlust is lower than its value at Turn Start, gain 3 Offense Level Up and 5 Defense Level Down
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku, 2 Pośpiechu i 2 Wrażliwości\n- Leczenie HP +50%\n- Na koniec tury, jeżeli wartość Powracającego Popędu Krwi jest niższa niż na początku tury, w następnej turze zyskuje 3 Wzrostu Poziomu Ataku i 5 Spadek Poziomu Obrony.
200. [Słowo kluczowe [Precarious] — nazwa] 무책임한 꿈
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Precarious].name
   kontekst: identyfikator tagu w tekstach: `[Precarious]`
   limit: do 40 znaków
   EN: Irresponsible Dream
   PL: Nieodpowiedzialny Sen
201. [Słowo kluczowe [Precarious] — opis] 돈키호테에게 피격 시 처치됨.
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Precarious].desc
   limit: do 120 znaków
   EN: Killed when hit by Don Quixote.
   PL: Ginie przy trafieniu przez Don Quixote.
202. [Słowo kluczowe [Penetration] — nazwa] 굳어가는 피
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Penetration].name
   kontekst: identyfikator tagu w tekstach: `[Penetration]`
   limit: do 40 znaków
   EN: Congealing Blood
   PL: Zastygająca Krew
203. [Słowo kluczowe [Penetration] — opis] 2턴동안 행동이 불가능하며, 아군을 꿰뚫은 창 유닛이 생성됨.
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=Penetration].desc
   limit: do 120 znaków
   EN: Cannot act for 2 turns; spawns an Impaling Spear unit over the ally.
   PL: Przez 2 tury nie może działać; nad sojusznikiem pojawia się jednostka Przebijającej Włóczni.
204. [Słowo kluczowe [DecreamentalDefense] — nazwa] 심각한 부상
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=DecreamentalDefense].name
   kontekst: identyfikator tagu w tekstach: `[DecreamentalDefense]`
   limit: do 40 znaków
   EN: Crippling Injury
   PL: Wyniszczająca Rana
205. [Słowo kluczowe [DecreamentalDefense] — opis] - 이전 전투의 부상이 아직 회복되지 않았다.\n- 최대 체력 대폭 감소\n- 턴 시작시, 누적된 턴 1 당 방어 레벨 감소 1 추가로 얻음 (최대 15)
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=DecreamentalDefense].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Yet to recover from the wounds gained in the previous battle.\n- Massively reduce max HP\n- Turn Start: gain 1 Defense Level Down for every cumulative turn (max 15)
   PL: - Rany z poprzedniej walki jeszcze się nie zagoiły.\n- Maks. HP drastycznie maleje\n- Na początku tury zyskuje dodatkowo 1 Spadek Poziomu Obrony za każdą zsumowaną turę (maks. 15)
206. [Słowo kluczowe [UnfinishedDream] — nazwa] 물보다 진한 피에서 벗어나,
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=UnfinishedDream].name
   kontekst: identyfikator tagu w tekstach: `[UnfinishedDream]`
   limit: do 90 znaków
   EN: IN WHICH IS RECOUNTED THE LIBERATION FROM BLOOD THICKER THAN WATER
   PL: W KTÓRYM NASTĘPUJE WYZWOLENIE SPOD KRWI GĘSTSZEJ NIŻ WODA
207. [Słowo kluczowe [UnfinishedDream] — opis] - 매 턴 종료 시, 다음 턴에 신속 1, 공격 레벨 증가 3 얻음\n- 누적된 턴 3 당, 공격 레벨 증가 2 추가로 얻음 (최대 6)\n- 합 승리 시 정신력 3 회복\n- 적 처치 시 다음 턴에 합 위력 증가 1 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=UnfinishedDream].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - At every Turn End: gain 1 Haste and 3 Offense Level Up next turn\n- Gain 2 additional Offense Level Up after every 3 cumulative turns (max 6)\n- On Clash Win, heal 3 SP\n- On Kill, gain 1 Clash Power Up next turn (once per turn)
   PL: - Na koniec każdej tury zyskuje w następnej turze 1 Pośpiech i 3 Wzrostu Poziomu Ataku\n- Za każde 3 zsumowane tury zyskuje +2 Wzrostu Poziomu Ataku (maks. 6)\n- Po wygranym Starciu odzyskuje 3 Poczytalności\n- Przy zabiciu wroga w następnej turze zyskuje 1 Wzrost Mocy Starcia (1 raz na turę)
208. [Słowo kluczowe [SanchoMind_LowMorale] — nazwa] 깨어나는 살육의 고양감
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SanchoMind_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[SanchoMind_LowMorale]`
   limit: do 40 znaków
   EN: Reawakening Joy Of Carnage
   PL: Przebudzająca się Radość Rzezi
209. [Słowo kluczowe [SanchoMind_LowMorale] — opis] - 사기 저하\n매 턴 시작 시, 공격 레벨 증가 2 얻음. 정신력 효율 +2
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SanchoMind_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nGain 2 Attack Power Up at every Turn Start; +2 SP Efficiency
   PL: - Niskie Morale\nZyskuje 2 Wzrostu Poziomu Ataku na początku każdej tury; +2 Efektywności Poczytalności
210. [Słowo kluczowe [SanchoMind_Panic] — nazwa] 깨어나는 살육의 고양감
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SanchoMind_Panic].name
   kontekst: identyfikator tagu w tekstach: `[SanchoMind_Panic]`
   (powtórzenie elementu 208 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
211. [Słowo kluczowe [SanchoMind_Panic] — opis] - 패닉\n턴 시작 시, 방어 레벨 증가 6 얻음. 다음 턴에 공격 레벨 증가 3 얻음
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=SanchoMind_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 6 Defense Level Up. Gain 3 Offense Level Up next turn
   PL: - Panika\nNa początku tury zyskuje 6 Wzrostu Poziomu Obrony. W następnej turze zyskuje 3 Wzrostu Poziomu Ataku
212. [Słowo kluczowe [FragmentOfHope] — nazwa] 버스에서 동료들과 함께 여러 모험을 겪었으며,
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FragmentOfHope].name
   kontekst: identyfikator tagu w tekstach: `[FragmentOfHope]`
   limit: do 80 znaków
   EN: WHICH TREATS THE BUS, THE COMPANIONS, AND THE ADVENTURES
   PL: W którym mowa o autobusie, towarzyszach i przygodach,
213. [Słowo kluczowe [FragmentOfHope] — opis] 수치만큼 합 위력 증가
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FragmentOfHope].desc
   limit: do 120 znaków
   EN: Gain Clash Power equal to the value
   PL: Zyskuje Moc Starcia równą wartości
214. [Słowo kluczowe [FragmentOfHopeTwo] — nazwa] 꿈을 끝내지 않을 산초이자 우리의 돈키호테에 대하여
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FragmentOfHopeTwo].name
   kontekst: identyfikator tagu w tekstach: `[FragmentOfHopeTwo]`
   limit: do 80 znaków
   EN: OF HOW SANCHO, OUR DON QUIXOTE, REFUSED TO END THE DREAM
   PL: O tym, jak Sancho, nasza Don Quixote, odmówiła zakończenia snu
215. [Słowo kluczowe [FragmentOfHopeTwo] — opis] 수치당 합 위력 +4\n전투 시작 시 자신과 아군에게 보호막 부여
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=FragmentOfHopeTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Clash Power +4 for every value\nApply Shield to self and all allies at Combat Start
   PL: Moc Starcia +4 za każdą wartość\nNa początku walki nakłada Tarczę na siebie i wszystkich sojuszników
216. [Słowo kluczowe [ConfinementOfGoldenBranch] — nazwa] 황금가지의 강제 조율
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ConfinementOfGoldenBranch].name
   kontekst: identyfikator tagu w tekstach: `[ConfinementOfGoldenBranch]`
   limit: do 60 znaków
   EN: The Golden Bough's Forced Arbitration
   PL: Przymusowy Arbitraż Złotej Gałęzi
217. [Słowo kluczowe [ConfinementOfGoldenBranch] — opis] - 기본 공격 레벨 30 감소\n- 기본 방어 레벨 30 감소
   źródło: BattleKeywords-a1c7p3.json :: dataList[id=ConfinementOfGoldenBranch].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Lose 30 Base Offense Level\n- Lose 30 Base Defense Level
   PL: - Podstawowy Poziom Ataku -30\n- Podstawowy Poziom Obrony -30

## Słowa kluczowe bitwy — BattleKeywords-a1c8p1
- plik gry: `BattleKeywords-a1c8p1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

218. [Słowo kluczowe [TheDrifter_LowMorale] — nazwa] 박도
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=TheDrifter_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[TheDrifter_LowMorale]`
   limit: do 40 znaków
   EN: Podao
   PL: Podao
219. [Słowo kluczowe [TheDrifter_LowMorale] — opis] - 사기저하\n- 일방 공격에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=TheDrifter_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Take +10% damage from Unopposed Attacks; deal +30% damage with Counterattacks
   PL: - Niskie Morale\n- Otrzymuje +10% obrażeń od Ataków Jednostronnych; zadaje +30% obrażeń Kontrą
220. [Słowo kluczowe [TheDrifter_Panic] — nazwa] 박도
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=TheDrifter_Panic].name
   kontekst: identyfikator tagu w tekstach: `[TheDrifter_Panic]`
   (powtórzenie elementu 218 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
221. [Słowo kluczowe [TheDrifter_Panic] — opis] - 패닉\n- 일방 공격에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=TheDrifter_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Take +20% damage from Unopposed Attacks; deal +50% damage with Counterattacks
   PL: - Panika\n- Otrzymuje +20% obrażeń od Ataków Jednostronnych; zadaje +50% obrażeń Kontrą
222. [Słowo kluczowe [SipOfAlcohol] — nazwa] 한 모금
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=SipOfAlcohol].name
   kontekst: identyfikator tagu w tekstach: `[SipOfAlcohol]`
   limit: do 40 znaków
   EN: Swig
   PL: Łyczek
223. [Słowo kluczowe [SipOfAlcohol] — opis] - 최대값: 5\n- 턴 종료 시 수치가 3 이상이면, 전체 체력의 3%만큼 회복 (본체, 부위)\n- 턴 종료 시 수치가 5라면, 다음 턴에 공격 위력 증가 3, 취약 2 얻음
   źródło: BattleKeywords-a1c8p1.json :: dataList[id=SipOfAlcohol].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack :5\n- Turn End: at 3 Stack, heal 3% HP (Core, Part)\n- Turn End: at 5 Stack, gain 3 Attack Power Up and 2 Fragile next turn
   PL: - Maks. stosów: 5\n- Na koniec tury przy 3+ stosach leczy 3% HP (korpus, części)\n- Na koniec tury przy 5 stosach zyskuje w następnej turze 3 Wzrostu Mocy Ataku i 2 Wrażliwości

## Słowa kluczowe bitwy — BattleKeywords-a1c8p2
- plik gry: `BattleKeywords-a1c8p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

224. [Słowo kluczowe [ExaminationOfQiu] — nazwa] 일말의 기대
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ExaminationOfQiu].name
   kontekst: identyfikator tagu w tekstach: `[ExaminationOfQiu]`
   limit: do 40 znaków
   EN: A Sliver of Anticipation
   PL: Iskra Oczekiwania
225. [Słowo kluczowe [ExaminationOfQiu] — opis] 전력으로 싸우고 있지 않다.\n- 기본 공격 레벨 35 감소, 기본 방어 레벨 35 감소\n- 대상에게 일방 공격 시 피해량 +30%
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ExaminationOfQiu].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: He's not giving it his all.\n- Lose 35 Base Offense Level, Lose 35 Base Defense Level\n- Deal +30% damage with Unopposed Attacks
   PL: Nie walczy z pełną siłą.\n- Podstawowy Poziom Ataku -35, Podstawowy Poziom Obrony -35\n- Zadaje +30% obrażeń Atakami Jednostronnymi
226. [Słowo kluczowe [BurstStop] — nazwa] 주살【물동】
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstStop].name
   kontekst: identyfikator tagu w tekstach: `[BurstStop]`
   limit: do 40 znaków
   EN: Deathrite 【Halt】
   PL: Obrzęd Śmierci 【Halt】
227. [Słowo kluczowe [BurstStop] — opis] 기본값: 4\n- 주살\n- 속박이 3 이상 있는 상태에서 파열이 발동될 때, 1 감소.\n- 수치 감소 시 10만큼 흐트러짐 손상\n- 수치가 0이 될 때, 파열 위력만큼 흐트러짐 손상. 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstStop].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 4\n- Deathrite\n- When getting Rupture triggered while this unit has 3+ Bind, lose 1 Stack\n- When losing Stacks, raise this unit's Stagger Threshold by 10\n- At 0 Stack, raise this unit's Stagger Threshold by Rupture Potency on self, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 4\n- Obrzęd Śmierci\n- Gdy wywołane zostaje Rozdarcie, a jednostka ma 3 lub więcej Spętań, maleje o 1.\n- Przy utracie wartości podnosi Próg Oszołomienia o 10\n- Przy wartości 0 podnosi Próg Oszołomienia o Siłę Rozdarcia, po czym znika\n- ※ Ten efekt nie odnawia się.
228. [Słowo kluczowe [BurstSuppress] — nazwa] 주살【철주】
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstSuppress].name
   kontekst: identyfikator tagu w tekstach: `[BurstSuppress]`
   limit: do 40 znaków
   EN: Deathrite 【Impede】
   PL: Obrzęd Śmierci 【Impede】
229. [Słowo kluczowe [BurstSuppress] — opis] 기본값: 10\n- 주살\n- 다른 주살이 조건에 의해 감소할 때, 수치 1 감소. (턴 당 최대 4)\n- 수치가 0이 될 때, 다음 턴동안 공격 레벨 감소 6 얻음. 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstSuppress].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 10\n- Deathrite\n- When this unit loses other Deathrites' Stacks due to their conditions, lose 1 Stack (max 4 per turn)\n- At 0 Stack, gain 6 Offense Level Down for the next turn, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 10\n- Obrzęd Śmierci\n- Gdy inne Obrzędy Śmierci tracą stosy przez swoje warunki, ten maleje o 1. (maks. 4 na turę)\n- Przy wartości 0 zyskuje 6 Spadku Poziomu Ataku na następną turę, po czym znika\n- ※ Ten efekt nie odnawia się.
230. [Słowo kluczowe [BurstWave] — nazwa] 주살【즉감】
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstWave].name
   kontekst: identyfikator tagu w tekstach: `[BurstWave]`
   limit: do 40 znaków
   EN: Deathrite 【Wane】
   PL: Obrzęd Śmierci 【Wane】
231. [Słowo kluczowe [BurstWave] — opis] 기본값: 10\n- 주살\n부여자에 의해 파열이 발동될 때, 1 감소.\n- 해당 효과를 제외한 자신이 가지고 있는 주살 중 무작위 1개의 수치가 1 감소함.\n- 수치가 0이 될 때, 소멸함\n- ※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstWave].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 10\n- Deathrite\nWhen the unit that inflicted this effect triggers Rupture, lose 1 Stack\n- Also lose 1 Stack of a random Deathrite on self, except for this Deathrite\n- At 0 Stack, expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 10\n- Obrzęd Śmierci\nGdy jednostka, która nałożyła ten efekt, wywołuje Rozdarcie, maleje o 1.\n- Dodatkowo o 1 maleje wartość losowego Obrzędu Śmierci na tej jednostce (poza tym Obrzędem)\n- Przy wartości 0 znika\n- ※ Ten efekt nie odnawia się.
232. [Słowo kluczowe [Teaching] — nazwa] 문답
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Teaching].name
   kontekst: identyfikator tagu w tekstach: `[Teaching]`
   limit: do 40 znaków
   EN: Dialogues
   PL: Dialogi
233. [Słowo kluczowe [Teaching] — opis] 최댓값: 3\n- 턴 종료시, 정신력 5 회복\n- 전투 중 체력이 0이 될 때 체력을 최대 체력만큼 회복함 (수치만큼 발동)
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Teaching].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\n- Turn End: heal 5 SP\n- When HP drops to 0 during the Encounter, heal up to max HP (activates as many times as this unit has Stacks)
   PL: Maks. stosów: 3\n- Na koniec tury odzyskuje 5 Poczytalności\n- Gdy HP spada do 0 podczas walki, leczy HP do Maks. HP (wywołuje się tyle razy, ile wynosi liczba stosów)
234. [Słowo kluczowe [BurstWeakness] — nazwa] 주살【약화】
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstWeakness].name
   kontekst: identyfikator tagu w tekstach: `[BurstWeakness]`
   limit: do 40 znaków
   EN: Deathrite 【Enfeeble】
   PL: Obrzęd Śmierci 【Enfeeble】
235. [Słowo kluczowe [BurstWeakness] — opis] 기본값: 5\n- 주살\n- 대상의 속도가 빠르고, 속도 차이가 5 이상일 때, 피격 시 파열이 발동될 때, 1 감소.\n- 수치 감소 시 다음 턴에 방어 레벨 감소 1 을 얻음 (턴 당 최대 1)\n- 수치가 0이 될 때, 다음 턴 방어 레벨 감소 3, 속박 1을 얻고 소멸\n- ※ 이 효과는 갱신되지 않음.
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=BurstWeakness].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 5\n- Deathrite\n- If the target's Speed is faster than this unit's, and if the Speed difference 5 or greater: when getting Rupture triggered, lose 1 Stack\n- When losing Stacks, gain 1 Defense Level Down next turn (once per turn)\n- At 0 Stack, gain 3 Defense Level Down and 1 Bind next turn, then expires\n- ※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 5\n- Obrzęd Śmierci\n- Jeżeli Szybkość celu jest większa, a różnica Szybkości wynosi 5 lub więcej: gdy przy trafieniu wywołane zostaje Rozdarcie, maleje o 1.\n- Przy utracie wartości zyskuje 1 Spadek Poziomu Obrony na następną turę (1 raz na turę)\n- Przy wartości 0 zyskuje 3 Spadek Poziomu Obrony i 1 Spętanie na następną turę, po czym znika\n- ※ Ten efekt nie odnawia się.
236. [Słowo kluczowe [Qiu_LowMorale] — nazwa] 가치우
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Qiu_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Qiu_LowMorale]`
   limit: do 40 znaków
   EN: Jia Qiu
   PL: Jia Qiu
237. [Słowo kluczowe [Qiu_LowMorale] — opis] - 사기저하\n- 홍루를 제외한 대상에게 가하는 피해량 +10%
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Qiu_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +10% damage against targets that aren't Hong Lu
   PL: - Niskie Morale\n- Zadaje +10% obrażeń celom innym niż Hong Lu
238. [Słowo kluczowe [Qiu_Panic] — nazwa] 가치우
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Qiu_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Qiu_Panic]`
   (powtórzenie elementu 236 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
239. [Słowo kluczowe [Qiu_Panic] — opis] - 패닉\n- 홍루를 제외한 대상에게 가하는 피해량 +20%
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=Qiu_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +20% damage against targets that aren't Hong Lu
   PL: - Panika\n- Zadaje +20% obrażeń celom innym niż Hong Lu
240. [Słowo kluczowe [QiuAndHonglu] — nazwa] 나의 진짜 마음…
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=QiuAndHonglu].name
   kontekst: identyfikator tagu w tekstach: `[QiuAndHonglu]`
   limit: do 40 znaków
   EN: My True Heart...
   PL: Moje prawdziwe serce…
241. [Słowo kluczowe [QiuAndHonglu] — opis] - 홍루의 모든 스킬의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=QiuAndHonglu].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Skills gain +1 Final Power\n- On Clash Win, 1 ally(including this unit) with the least SP heals 5 SP\n- When an ally dies, remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)
   PL: - Wszystkie Umiejętności Hong Lu zyskują Moc Końcowa +1\n- Po wygranym Starciu 1 sojusznik (w tym ta jednostka) o najniższej Poczytalności odzyskuje +5 Poczytalności\n- Gdy ginie sojusznik, pozostali na koniec tury zyskują 1 Wzrost Mocy Ataku na następną turę (raz/turę)
242. [Słowo kluczowe [ProtectStance] — nazwa] 보호 태세
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ProtectStance].name
   kontekst: identyfikator tagu w tekstach: `[ProtectStance]`
   limit: do 40 znaków
   EN: Protective Stance
   PL: Postawa Ochronna
243. [Słowo kluczowe [ProtectStance] — opis] 최댓값 : 2\n이 효과는 합산되지 않고, 갱신됨\n턴 종료 시 1 감소\n이 효과를 얻으면 다음 턴에 아래 효과 적용\n- 보호 2 얻음\n- 자신의 각 슬롯 도발치 5 증가
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ProtectStance].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 2\nThis effect does not compound in potency; stacking it only extends its duration\nReduced by 1 at Turn End\nWhen a unit gains this effect, gain the following effects next turn:\n- Gain 2 Protection\n- Gain 5 Aggro to each of this unit's Slots
   PL: Maks. stosów: 2\nTen efekt się nie sumuje — odnawia się\nNa koniec tury maleje o 1\nPo zdobyciu tego efektu w następnej turze:\n- Zyskuje 2 Ochrony\n- Prowokacja każdego slotu tej jednostki rośnie o 5
244. [Słowo kluczowe [ZiluDebuff] — nazwa] 살기 억제
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ZiluDebuff].name
   kontekst: identyfikator tagu w tekstach: `[ZiluDebuff]`
   limit: do 40 znaków
   EN: Bloodthirst Suppressed
   PL: Ukrócona Krwiożerczość
245. [Słowo kluczowe [ZiluDebuff] — opis] - 기본 공격 레벨 20 감소, 기본 방어 레벨 20 감소
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=ZiluDebuff].desc
   limit: do 120 znaków
   EN: - Lose 20 Base Offense Level, Lose 20 Base Defense Level
   PL: - Podstawowy Poziom Ataku -20, Podstawowy Poziom Obrony -20
246. [Słowo kluczowe [WitheredWood_LowMorale] — nazwa] 고목화
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=WitheredWood_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[WitheredWood_LowMorale]`
   limit: do 40 znaków
   EN: Eldtree Mutation
   PL: Mutacja Prastarego Drzewa
247. [Słowo kluczowe [WitheredWood_LowMorale] — opis] - 사기 저하\n- 피해량 증가 1, 취약 1, 파열 취약 1 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=WitheredWood_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Damage Up, 1 Fragile, and 1 Rupture Fragility
   PL: - Niskie Morale\n- Zyskuje 1 Wzrost Obrażeń, 1 Wrażliwości i 1 Wrażliwość na Rozdarcie
248. [Słowo kluczowe [WitheredWood_Panic] — nazwa] 고목화
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=WitheredWood_Panic].name
   kontekst: identyfikator tagu w tekstach: `[WitheredWood_Panic]`
   (powtórzenie elementu 246 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
249. [Słowo kluczowe [WitheredWood_Panic] — opis] - 패닉\n- 피해량 증가 2, 취약 2, 파열 취약 2 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=WitheredWood_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Damage Up, 2 Fragile, and 2 Rupture Fragility
   PL: - Panika\n- Zyskuje 2 Wzrostu Obrażeń, 2 Wrażliwości i 2 Wrażliwość na Rozdarcie
250. [Słowo kluczowe [EvilHeart_LowMorale] — nazwa] 사심
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=EvilHeart_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[EvilHeart_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Evil
   PL: Serce Zła
251. [Słowo kluczowe [EvilHeart_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 2, 취약 1 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=EvilHeart_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +2\nTurn Start: gain 2 Damage Up and 1 Fragile
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +2\nNa początku tury zyskuje 2 Wzrostu Obrażeń i 1 Wrażliwości
252. [Słowo kluczowe [EvilHeart_Panic] — nazwa] 사심
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=EvilHeart_Panic].name
   kontekst: identyfikator tagu w tekstach: `[EvilHeart_Panic]`
   (powtórzenie elementu 250 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Słowo kluczowe [EvilHeart_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 3, 취약 2 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=EvilHeart_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +3\nTurn Start: gain 3 Damage Up and 2 Fragile
   PL: - Panika\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +3\nNa początku tury zyskuje 3 Wzrostu Obrażeń i 2 Wrażliwości
254. [Słowo kluczowe [DeepEvilHeart_LowMorale] — nazwa] 짙은 사심
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepEvilHeart_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DeepEvilHeart_LowMorale]`
   limit: do 40 znaków
   EN: Heart of Oppressive Evil
   PL: Głębokie Serce Zła
255. [Słowo kluczowe [DeepEvilHeart_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 3, 취약 1 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepEvilHeart_LowMorale].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +2\nTurn Start: gain 3 Damage Up and 1 Fragile
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +2\nNa początku tury zyskuje 3 Wzrostu Obrażeń i 1 Wrażliwości
256. [Słowo kluczowe [DeepEvilHeart_Panic] — nazwa] 짙은 사심
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepEvilHeart_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DeepEvilHeart_Panic]`
   (powtórzenie elementu 254 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
257. [Słowo kluczowe [DeepEvilHeart_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 4, 취약 2 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepEvilHeart_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Omen Talisman, Clash Power +3\nTurn Start: gain 4 Damage Up and 2 Fragile
   PL: - Panika\nW Starciu z celami posiadającymi Złowieszczy Talizman Moc Starcia +3\nNa początku tury zyskuje 4 Wzrostu Obrażeń i 2 Wrażliwości
258. [Słowo kluczowe [OminousTalisman] — nazwa] 불길한 부적
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=OminousTalisman].name
   kontekst: identyfikator tagu w tekstach: `[OminousTalisman]`
   limit: do 40 znaków
   EN: Omen Talisman
   PL: Złowieszczy Talizman
259. [Słowo kluczowe [OminousTalisman] — opis] - 기본값 : 10\n- 수치가 0이 될 때, 파열 위력만큼 탐식 속성 피해와 정신력 피해를 받고 소멸 (정신력 피해 최대 20)\n- 불길한 부적이 감소할 때 감소한 수치만큼 파열 위력을 얻고 그 수치의 절반만큼 파열 횟수가 증가 (소수점 버림)\n※ 이 효과는 갱신되지 않음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=OminousTalisman].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- When dropping to 0 Stack: take Gluttony damage and SP damage equal to Rupture Potency on self, then expires (max SP damage: 20)\n- When losing Omen Talismans, gain Rupture Potency equal to the number of Omen Talismans lost; then, gain half of Rupture Potency lost as Rupture Count (rounded down)\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: - Wartość bazowa: 10\n- Przy spadku do 0 stosów otrzymuje obrażenia Obżarstwa i obrażenia Poczytalności równe Sile Rozdarcia, po czym znika (maks. obrażeń Poczytalności: 20)\n- Gdy Złowieszczy Talizman maleje, zyskuje Siłę Rozdarcia równą utraconej liczbie, a Licznik Rozdarcia rośnie o połowę tej liczby (zaokrąglone w dół)\n※ Ten efekt nie odnawia się
260. [Słowo kluczowe [RepressedMurderousIntendTwo] — nazwa] 눌린 살기
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=RepressedMurderousIntendTwo].name
   kontekst: identyfikator tagu w tekstach: `[RepressedMurderousIntendTwo]`
   limit: do 40 znaków
   EN: Concealed Bloodthirst
   PL: Skryta Krwiożerczość
261. [Słowo kluczowe [RepressedMurderousIntendTwo] — opis] 기본 공격 레벨 5 감소\n기본 방어 레벨 5 감소
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=RepressedMurderousIntendTwo].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Lose 5 Base Offense Level\nLose 5 Base Defense Level
   PL: Podstawowy Poziom Ataku -5\nPodstawowy Poziom Obrony -5
262. [Słowo kluczowe [UncontrolledChargeAxe_LowMorale] — nazwa] 충전 회로 역류
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[UncontrolledChargeAxe_LowMorale]`
   limit: do 50 znaków
   EN: Charge Circuitry Countercurrent
   PL: Wsteczny Prąd Obwodu Ładowania
263. [Słowo kluczowe [UncontrolledChargeAxe_LowMorale] — opis] - 사기 저하\n파열을 보유한 대상과 합 진행 시, 충전 횟수 3, 취약 1 얻음 (턴 당 2회)
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_LowMorale].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nWhen Clashing against targets with Rupture, gain +3 Charge Count and 1 Fragile (2 times per turn)
   PL: - Niskie Morale\nW Starciu z celami posiadającymi Rozdarcie zyskuje +3 Liczby Ładunków i 1 Wrażliwości (2 razy na turę)
264. [Słowo kluczowe [UncontrolledChargeAxe_Panic] — nazwa] 충전 회로 역류
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_Panic].name
   kontekst: identyfikator tagu w tekstach: `[UncontrolledChargeAxe_Panic]`
   (powtórzenie elementu 262 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
265. [Słowo kluczowe [UncontrolledChargeAxe_Panic] — opis] - 패닉\n파열을 보유한 대상과 합 진행 시, 충전 횟수 5, 피해량 증가 1, 취약 2 얻음 (턴 당 2회)
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=UncontrolledChargeAxe_Panic].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nWhen Clashing against targets with Rupture, gain +5 Charge Count, 1 Damage Up, and 2 Fragile (2 times per turn)
   PL: - Panika\nW Starciu z celami posiadającymi Rozdarcie zyskuje +5 Liczby Ładunków, 1 Wzrost Obrażeń i 2 Wrażliwości (2 razy na turę)
266. [Słowo kluczowe [MadFeather] — nazwa] 눈알 깃
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather].name
   kontekst: identyfikator tagu w tekstach: `[MadFeather]`
   limit: do 40 znaków
   EN: Eyeball Pinion
   PL: Pióro z Gałką Oczową
267. [Słowo kluczowe [MadFeather] — opis] - 최대값 : 10\n- 턴 종료시, (수치/2)만큼 파열 횟수, 출혈 횟수 얻음 (소수점 버림)\n- 턴 종료시, 수치 1 감소
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- Turn End: gain (Stack / 2) Rupture Count and Bleed Count (rounded down)\n- Turn End: lose 1 Stack
   PL: - Maks. stosów: 10\n- Na koniec tury zyskuje (stosy/2) Licznika Rozdarcia i Licznika Krwawienia (zaokrąglone w dół)\n- Na koniec tury traci 1 stos
268. [Słowo kluczowe [MadFeather_LowMorale] — nazwa] 양날깃
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[MadFeather_LowMorale]`
   limit: do 40 znaków
   EN: Double-edged Feather
   PL: Dwukrawędziowe Pióro
269. [Słowo kluczowe [MadFeather_LowMorale] — opis] - 사기 저하\n턴 시작시 취약 1, 체력 회복 증가 1 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather_LowMorale].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 1 Fragile and 1 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: - Niskie Morale\nNa początku tury zyskuje 1 Wrażliwości i 1 Wzrost Leczenia HP. Przy trafieniu nakłada 1 Rozdarcie i 1 Krwawienie
270. [Słowo kluczowe [MadFeather_Panic] — nazwa] 양날깃
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather_Panic].name
   kontekst: identyfikator tagu w tekstach: `[MadFeather_Panic]`
   (powtórzenie elementu 268 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
271. [Słowo kluczowe [MadFeather_Panic] — opis] - 패닉\n턴 시작시 취약 2, 체력 회복 증가 2 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=MadFeather_Panic].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: -Panic\nTurn Start: gain 2 Fragile and 2 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: - Panika\nNa początku tury zyskuje 2 Wrażliwości i 2 Wzrost Leczenia HP. Przy trafieniu nakłada 1 Rozdarcie i 1 Krwawienie
272. [Słowo kluczowe [JarMaster_LowMorale] — nazwa] 돌격 지시
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=JarMaster_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[JarMaster_LowMorale]`
   limit: do 40 znaków
   EN: Charge Order
   PL: Rozkaz Szturmu
273. [Słowo kluczowe [JarMaster_LowMorale] — opis] - 사기 저하\n턴 시작시 취약 1을 얻고, 모든 아군에게 피해량 증가 1 부여
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=JarMaster_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 1 Fragile and apply 1 Damage Up to all allies
   PL: - Niskie Morale\nNa początku tury zyskuje 1 Wrażliwości i nakłada 1 Wzrost Obrażeń na wszystkich sojuszników
274. [Słowo kluczowe [JarMaster_Panic] — nazwa] 돌격 지시
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=JarMaster_Panic].name
   kontekst: identyfikator tagu w tekstach: `[JarMaster_Panic]`
   (powtórzenie elementu 272 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Słowo kluczowe [JarMaster_Panic] — opis] - 패닉\n턴 시작시 취약 2를 얻고, 모든 아군에게 피해량 증가 2 부여
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=JarMaster_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 2 Fragile and apply 2 Damage Up to all allies
   PL: - Panika\nNa początku tury zyskuje 2 Wrażliwości i nakłada 2 Wzrostu Obrażeń na wszystkich sojuszników
276. [Słowo kluczowe [DeepAngry_LowMorale] — nazwa] 울분
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepAngry_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DeepAngry_LowMorale]`
   limit: do 40 znaków
   EN: Angst
   PL: Udręka
277. [Słowo kluczowe [DeepAngry_LowMorale] — opis] - 사기 저하\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 피해량 증가 2, 취약 1 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepAngry_LowMorale].desc
   (powtórzenie elementu 251 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
278. [Słowo kluczowe [DeepAngry_Panic] — nazwa] 울분
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepAngry_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DeepAngry_Panic]`
   (powtórzenie elementu 276 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
279. [Słowo kluczowe [DeepAngry_Panic] — opis] - 패닉\n불길한 부적을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 피해량 증가 3, 취약 2 얻음
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=DeepAngry_Panic].desc
   (powtórzenie elementu 253 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
280. [Słowo kluczowe [TakeBreath_LowMorale] — nazwa] 숨 돌리기
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=TakeBreath_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[TakeBreath_LowMorale]`
   limit: do 40 znaków
   EN: Catching Breath
   PL: Wyrównanie Oddechu
281. [Słowo kluczowe [TakeBreath_LowMorale] — opis] - 사기 저하\n턴 시작시 방어 레벨 증가 2를 얻고 호흡 위력 2 감소
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=TakeBreath_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: gain 2 Defense Level Up and lose 2 Poise Potency
   PL: - Niskie Morale\nNa początku tury zyskuje 2 Wzrostu Poziomu Obrony i traci 2 Siły Oddechu
282. [Słowo kluczowe [TakeBreath_Panic] — nazwa] 숨 돌리기
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=TakeBreath_Panic].name
   kontekst: identyfikator tagu w tekstach: `[TakeBreath_Panic]`
   (powtórzenie elementu 280 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
283. [Słowo kluczowe [TakeBreath_Panic] — opis] - 패닉\n턴 시작시 방어 레벨 증가 5를 얻고 호흡 위력 5 감소
   źródło: BattleKeywords-a1c8p2.json :: dataList[id=TakeBreath_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\nTurn Start: gain 5 Defense Level Up and lose 5 Poise Potency
   PL: - Panika\nNa początku tury zyskuje 5 Wzrostu Poziomu Obrony i traci 5 Siły Oddechu

## Słowa kluczowe bitwy — BattleKeywords-a1c8p3
- plik gry: `BattleKeywords-a1c8p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

284. [Słowo kluczowe [Bothersome] — nazwa] 절참 [切斬]
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Bothersome].name
   kontekst: identyfikator tagu w tekstach: `[Bothersome]`
   limit: do 40 znaków
   EN: Severing Slash [切斬]
   PL: Rozcinające Cięcie [切斬]
285. [Słowo kluczowe [Bothersome] — opis] - 대상의 참격 내성을 약점(1.5)으로 취급함 (대상의 참격 내성이 1.5 이상인 경우에는 적용되지 않음)\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Bothersome].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - The target's Slash Resistance counts as 'Weak'(1.5). (does not activate against targets with 1.5 or higher Slash Resistance)\n- Expires at Turn End
   PL: - Odporność na Cięcie celu liczy się jako Słaba (1,5). (nie działa na cele z odpornością na Cięcie 1,5 lub wyższą)\n- Na koniec tury znika
286. [Słowo kluczowe [VibrationIgnition] — nazwa] 진동 - 작열
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=VibrationIgnition].name
   kontekst: identyfikator tagu w tekstach: `[VibrationIgnition]`
   limit: do 40 znaków
   EN: Tremor - Scorch
   PL: Wstrząs - Żar
287. [Słowo kluczowe [VibrationIgnition] — opis] - 진동 폭발 시 (진동 위력과 화상 위력의 합/2)만큼 분노 피해를 입고 화상 횟수 1 감소\n- 진동 폭발 스킬로 피격 시, 효과 위력만큼 흐트러짐 손상\n- 턴 종료 후 횟수 1 감소\n(진동 위력 및 횟수를 증가, 감소시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=VibrationIgnition].desc
   limit: do 450 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Tremor Burst, take Wrath Damage equal to (sum of Tremor Potency and Burn Potency / 2), and lose 1 Burn Count\n- When hit by Skills that trigger Tremor Burst, raise this unit's Stagger Threshold by the effect's Potency\n- Turn End: reduce the Count by 1\n(Interacts the same way as normal Tremor does to effects that raise or reduce Tremor Potency/Count)
   PL: - Przy Wyładowaniu Wstrząsu otrzymuje obrażenia Gniewu równe (suma Siły Wstrząsu i Siły Podpalenia / 2) i traci 1 Licznika Podpalenia\n- Przy trafieniu Umiejętnościami wywołującymi Wyładowanie Wstrząsu podnosi Próg Oszołomienia o Siłę tego efektu\n- Po zakończeniu tury traci 1 Licznika\n(Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających lub zmniejszających Siłę i Licznik Wstrząsu)
288. [Słowo kluczowe [BulletPropellant] — nazwa] 호표탄
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BulletPropellant].name
   kontekst: identyfikator tagu w tekstach: `[BulletPropellant]`
   limit: do 40 znaków
   EN: Tigermark Round
   PL: Pocisk Znaku Tygrysa
289. [Słowo kluczowe [BulletPropellant] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모\n- 최댓값 : 6
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills\n- Max Stack: 6
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności\n- Maks. stosów: 6
290. [Słowo kluczowe [BulletPropellantSpecial] — nazwa] 맹호표탄
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BulletPropellantSpecial].name
   kontekst: identyfikator tagu w tekstach: `[BulletPropellantSpecial]`
   limit: do 40 znaków
   EN: Savage Tigermark Round
   PL: Pocisk Dzikiego Tygrysa
291. [Słowo kluczowe [BulletPropellantSpecial] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모 (호표탄의 효과가 적용됨)\n- 장착한 탄환과 남은 탄환이 이 효과의 위력과 횟수로 표기됨\n· 위력 최댓값 (장착한 탄환) : 6\n- 이 탄환을 소모한 코인의 피해량이 30%만큼 증가하고, 부여하는 화상 위력, 화상 횟수의 부여값이 2배로 증가\n- 장착한 탄환과 남은 탄환을 전부 소모하면 호표탄으로 변경
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BulletPropellantSpecial].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills (actives the same way as Tigermark Round does)\n- The Potency and the Count of this effect are "Loaded Ammo" and "Remaining Ammo", respectively\n· Max Potency (Loaded Ammo): 6\n- Coins that spent this Ammo deal +30% damage, and inflict double the normal amount of Burn Potency and Count\n- When all Loaded Ammo and Remaining Ammo are spent, converts back to Tigermark Round
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności (działa jak Pocisk Znaku Tygrysa)\n- Siła i Licznik tego efektu oznaczają „Załadowaną Amunicję” i „Pozostałą Amunicję”\n· Maks. Siły (Załadowana Amunicja): 6\n- Monety, które zużyły tę amunicję, zadają +30% obrażeń i nakładają dwukrotnie więcej Siły i Licznika Podpalenia\n- Po zużyciu całej Załadowanej i Pozostałej Amunicji zmienia się z powrotem w Pocisk Znaku Tygrysa
292. [Słowo kluczowe [Prey] — nazwa] 사냥감
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Prey].name
   kontekst: identyfikator tagu w tekstach: `[Prey]`
   limit: do 40 znaków
   EN: Prey
   PL: Zdobycz
293. [Słowo kluczowe [Prey] — opis] - 적과 합 진행 시, 합 위력 - 5\n- 전투 시작 시,\n· 공격 스킬을 장착하였다면 공격 스킬로 뇌횡에게 가하는 피해량이 50%만큼 감소\n· 수비 스킬을 장착하였다면 뇌횡에게 받는 피해량이 75%만큼 감소\n- 이 효과를 보유한 상태에서 뇌횡과 합하여 승리 시, 제일 적게 보유한 E.G.O 자원 3개 획득\n- 턴 종료 시 사라지고, 자신의 정신력 10 회복
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Prey].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - In a Clash with an enemy, Clash Power -5\n- Combat Start:\n· If this unit equipped an Attack Skill, deal -50% damage against Lei Heng using Attack Skills\n· If this unit equipped a Defense Skill, take -75% damage from Lei Heng\n- If this unit wins a Clash against Lei Heng while under this effect, gain 3 of the least-owned E.G.O Resources\n- Expires at Turn End; this unit heals 10 SP
   PL: - W Starciu z wrogiem Moc Starcia -5\n- Na początku walki,\n· Jeżeli wyposażono Umiejętność ataku, zadaje o 50% mniej obrażeń Lei Hengowi Umiejętnościami ataku\n· Jeżeli wyposażono Umiejętność obrony, otrzymuje o 75% mniej obrażeń od Lei Henga\n- Jeżeli wygrywa Starcie z Lei Hengiem, mając ten efekt, zyskuje 3 najmniej posiadanych Zasobów E.G.O\n- Znika na koniec tury, a jednostka odzyskuje 10 Poczytalności
294. [Słowo kluczowe [Complacency] — nazwa] 오버히트
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Complacency].name
   kontekst: identyfikator tagu w tekstach: `[Complacency]`
   limit: do 40 znaków
   EN: Overheat
   PL: Przegrzanie
295. [Słowo kluczowe [Complacency] — opis] - 최댓값 : 5\n- 턴 시작 시, 수치만큼 합 위력 감소, 취약 얻음\n- 턴 종료 시, 사라짐
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Complacency].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 5\n- Turn Start: gain Clash Power Down and Fragile equal to the Stack\n- Expires at Turn End
   PL: - Maks. stosów: 5\n- Na początku tury zyskuje Spadek Mocy Starcia i Wrażliwości równy liczbie stosów\n- Na koniec tury znika
296. [Słowo kluczowe [BattleSense] — nazwa] 저력 [底力]
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BattleSense].name
   kontekst: identyfikator tagu w tekstach: `[BattleSense]`
   limit: do 40 znaków
   EN: Inner Strength [底力]
   PL: Siła Skryta [底力]
297. [Słowo kluczowe [BattleSense] — opis] - 최댓값 : 25\n- 특정 스킬 사용 시 소모하며, 해당 턴 종료 시 소모한 수치만큼 정신력을 회복\n- 합을 진행할 때마다 1 증가 (스킬당 최대 5). 합 패배 시, 해당 합에서 얻은 스택을 잃음\n- 일방 공격으로 적중 시 2 증가 (스킬당 최대 10)\n- 누적 소모한 수치에 비례하여 턴 종료 시 다음 턴에 신속 얻음 (수치 25당 신속 1, 최대 2)\n- 특정 패턴 시, 버프가 변경됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BattleSense].desc
   limit: do 590 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 25\n- Consumed by certain Skills; at Turn End, heal SP equal to the Stack consumed by the end of the turn\n- Gain 1 Stack with every Clash (max 5 per Skill). On Clash Lose, lose the Stacks gained from the said Clash\n- Gain 2 Stack when hitting with an Unopposed Attack (max 10 per Skill)\n- Turn End: next turn, gain Haste based on the total Stack consumed this turn (1 Haste per 25 Stack; max 2)\n- Gains a different buff when using a specific pattern
   PL: - Maks. stosów: 25\n- Zużywana przez określone Umiejętności; na koniec tury odzyskuje Poczytalność równą liczbie zużytych stosów\n- Zyskuje 1 stos za każde Starcie (maks. 5 na Umiejętność). Po przegranej w Starciu traci stosy zdobyte w tym Starciu\n- Zyskuje 2 stosy przy trafieniu Atakiem Jednostronnym (maks. 10 na Umiejętność)\n- Na koniec tury, w następnej turze, zyskuje Pośpiech zależny od łącznej liczby zużytych w tej turze stosów (1 Pośpiech za 25 stosów; maks. 2)\n- Przy określonym wzorcu zmienia się w inny buff
298. [Słowo kluczowe [RestoredBattleSense] — nazwa] 극력 [極力]
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=RestoredBattleSense].name
   kontekst: identyfikator tagu w tekstach: `[RestoredBattleSense]`
   limit: do 40 znaków
   EN: Extreme Strength [極力]
   PL: Siła Skrajna [極力]
299. [Słowo kluczowe [RestoredBattleSense] — opis] - 최댓값 : 50\n- 저력으로 취급함. 특정 스킬 사용 시 소모하며, 해당 턴 종료 시 소모한 수치만큼 정신력을 회복\n- 합을 진행할 때마다 2 증가 (스킬당 최대 10). 합 패배 시, 해당 합에서 얻은 스택을 잃음\n- 일방 공격으로 적중 시 3 증가 (스킬당 최대 15)\n- 누적 소모한 수치에 비례하여 턴 종료 시 다음 턴에 신속 얻음 (수치 25당 신속 1, 최대 5)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=RestoredBattleSense].desc
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Counts as "Inner Strength". Consumed by certain Skills; at Turn End, heal SP equal to the Stack consumed by the end of the turn.\n- Gain 2 Stack with every Clash (max 10 per Skill). On Clash Lose, lose the Stacks gained from the said Clash\n- Gain 3 Stack when hitting with an Unopposed Attack (max 15 per Skill)\n- Turn End: next turn, gain Haste based on the total Stack consumed this turn (1 Haste per 25 Stack, max 5)
   PL: - Maks. stosów: 50\n- Liczy się jako „Siła Skryta”. Zużywana przez określone Umiejętności; na koniec tury odzyskuje Poczytalność równą liczbie zużytych stosów.\n- Zyskuje 2 stosy za każde Starcie (maks. 10 na Umiejętność). Po przegranej w Starciu traci stosy zdobyte w tym Starciu\n- Zyskuje 3 stosy przy trafieniu Atakiem Jednostronnym (maks. 15 na Umiejętność)\n- Na koniec tury, w następnej turze, zyskuje Pośpiech zależny od łącznej liczby zużytych w tej turze stosów (1 Pośpiech za 25 stosów, maks. 5)
300. [Słowo kluczowe [Irritation] — nazwa] 천퇴성[天退星]
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Irritation].name
   kontekst: identyfikator tagu w tekstach: `[Irritation]`
   limit: do 40 znaków
   EN: Tiantui Star [天退星]
   PL: Gwiazda Tiantui [天退星]
301. [Słowo kluczowe [Irritation] — opis] - 턴 시작 시, 잃은 체력 20%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 3)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +2\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 20%)\n- '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경\n- 특정 패턴 시, 이 버프가 신(心) - 천퇴성[天退星]으로 변경
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Irritation].desc
   limit: do 530 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Damage Up and 1 Power Up for every 20% missing HP on self (max 3 each)\n- Inflict +2 more Tremor Potency with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 20%)\n- Convert the final Coin of 'Triple Slash - Blast' to an Unbreakable Coin\n- This buff changes into Shin (心) - Tiantui Star [天退星] when using a specific pattern
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy za każde 20% brakującego HP (każdy maks. 3)\n- Umiejętności nakładają na wrogów o 2 więcej Siły Wstrząsu\n- Jeżeli Szybkość tej jednostki jest o 3 lub więcej większa od Szybkości celu, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 20%)\n- Ostatnia Moneta „Potrójnego Cięcia - Wybuch” staje się Niezniszczalną Monetą\n- Przy określonym wzorcu ten buff zmienia się w Shin (心) - Gwiazdę Tiantui [天退星]
302. [Słowo kluczowe [HugeIrritation] — nazwa] 신(心) - 천퇴성[天退星]
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=HugeIrritation].name
   kontekst: identyfikator tagu w tekstach: `[HugeIrritation]`
   limit: do 50 znaków
   EN: Shin (心) - Tiantui Star [天退星]
   PL: Shin (心) - Gwiazda Tiantui [天退星]
303. [Słowo kluczowe [HugeIrritation] — opis] - 턴 시작 시, 잃은 체력 15%당 피해량 증가 1, 위력 증가 1 얻음 (각각 최대 5)\n- 적에게 스킬로 부여하는 진동 위력 부여량 +3, 진동 횟수 증가량 +1\n- 자신의 속도가 대상의 속도보다 3 이상 높으면, 피해량 +(대상과의 속도 차이 x 5)% (최대 20%)\n- '이연참-폭', '삼연격-폭'의 마지막 코인이 파괴 불가 코인으로 변경
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=HugeIrritation].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: gain 1 Damage Up and 1 Power Up for every 15% missing HP on self (max 5 each)\n- Inflict +3 more Tremor Potency and +1 more Tremor Count with this unit's Skills\n- If this unit's Speed is faster than the target's by 3 or more, deal +(Speed difference x 5)% damage (max 20%)\n- Convert the final Coins of 'Double Slash - Blast' and 'Triple Slash - Blast' to Unbreakable Coins
   PL: - Na początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy za każde 15% brakującego HP (każdy maks. 5)\n- Umiejętności nakładają na wrogów o 3 więcej Siły Wstrząsu i +1 Licznika Wstrząsu\n- Jeżeli Szybkość tej jednostki jest o 3 lub więcej większa od Szybkości celu, zadaje +(różnica Szybkości x 5)% obrażeń (maks. 20%)\n- Ostatnie Monety „Podwójnego Cięcia - Wybuch” i „Potrójnego Cięcia - Wybuch” stają się Niezniszczalnymi Monetami
304. [Słowo kluczowe [ReloadKeepAmmo] — nazwa] 재장전 - 잔탄 유지
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ReloadKeepAmmo].name
   kontekst: identyfikator tagu w tekstach: `[ReloadKeepAmmo]`
   limit: do 40 znaków
   EN: Reload - Tactical
   PL: Przeładowanie - Taktyczne
305. [Słowo kluczowe [ReloadKeepAmmo] — opis] - 탄환을 획득 가능한 최대 수치만큼 다시 얻음 (단, 보유한 탄환을 버리지 않음)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ReloadKeepAmmo].desc
   limit: do 120 znaków
   EN: - Restore this unit's Ammo to its maximum capacity (does not discard any remaining Ammo)
   PL: - Odzyskuje amunicję do Maks. wartości (bez wyrzucania posiadanej amunicji)
306. [Słowo kluczowe [BeastEyes_LowMorale] — nazwa] 맹수의 본능 - 사기저하
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BeastEyes_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BeastEyes_LowMorale]`
   limit: do 50 znaków
   EN: Beastly Instinct - Low Morale
   PL: Instynkt Bestii - Niskie Morale
307. [Słowo kluczowe [BeastEyes_LowMorale] — opis] - 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이/2)%만큼 증가 (최대 10%)\n- 턴 시작 시, 최종 위력 증가 1, 피해량 증가 1, 취약 1 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BeastEyes_LowMorale].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +(HP percentage difference / 2)% damage to targets with higher HP percentages that this unit's (max 10%)\n- Turn Start: gain 1 Final Power Up, 1 Damage Up, and 1 Fragile
   PL: - Zadaje +(różnica procentowa HP / 2)% obrażeń celom o wyższym procentowym HP niż własne (maks. 10%)\n- Na początku tury zyskuje 1 Wzrost Mocy Końcowej, 1 Wzrost Obrażeń i 1 Wrażliwości
308. [Słowo kluczowe [BeastEyes_Panic] — nazwa] 맹수의 본능 - 패닉
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BeastEyes_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BeastEyes_Panic]`
   limit: do 40 znaków
   EN: Beastly Instinct - Panic
   PL: Instynkt Bestii - Panika
309. [Słowo kluczowe [BeastEyes_Panic] — opis] - 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이)%만큼 증가 (최대 25%)\n- 턴 시작 시, 코인 위력 증가 1, 피해량 증가 2, 취약 2 얻음\n- 다음 턴 시작 시, 자신의 잃은 체력 비율 수치만큼 정신력 회복 (최대 25)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BeastEyes_Panic].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deals +(HP percentage difference)% damage to targets with higher HP percentages that this unit's (max 25%)\n- Turn Start: gain 1 Coin Power Up, 2 Damage Up, and 2 Fragile\n- Next Turn Start: heal SP equal to this unit's missing HP percentage (max 25)
   PL: - Zadaje +(różnica procentowa HP)% obrażeń celom o wyższym procentowym HP niż własne (maks. 25%)\n- Na początku tury zyskuje 1 Wzrost Mocy Monety, 2 Wzrostu Obrażeń i 2 Wrażliwości\n- Na początku następnej tury odzyskuje Poczytalność równą procentowi brakującego HP (maks. 25)
310. [Słowo kluczowe [DisengageCombat] — nazwa] 전투 이탈
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=DisengageCombat].name
   kontekst: identyfikator tagu w tekstach: `[DisengageCombat]`
   limit: do 40 znaków
   EN: Escape Battle
   PL: Wycofanie z Walki
311. [Słowo kluczowe [DisengageCombat] — opis] - 턴 종료 시 흐트러짐 상태를 해제하고 전투에서 이탈함 (강제 흐트러짐 제외, 사망으로 처리되지 않음)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=DisengageCombat].desc
   limit: do 150 znaków
   EN: - Turn End: recover from Stagger and escape from the Encounter (excluding forced Staggers; does not count as death)
   PL: - Na koniec tury wychodzi z Oszołomienia i opuszcza walkę (poza wymuszonym Oszołomieniem; nie liczy się jako śmierć)
312. [Słowo kluczowe [Chesed_Mercy] — nazwa] 헤세드의 자비
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Chesed_Mercy].name
   kontekst: identyfikator tagu w tekstach: `[Chesed_Mercy]`
   limit: do 40 znaków
   EN: Chesed's Mercy
   PL: Miłosierdzie Cheseda
313. [Słowo kluczowe [Chesed_Mercy] — opis] - 모든 캐릭터의 공격 레벨, 방어 레벨이 평균으로 조정됨\n- 아군 인격은 헤세드 효과가 적용된 후 공격 레벨 3, 방어 레벨 6을 추가로 얻음\n- [최초 개방 효과] 헤세드의 자비가 이번 전투 동안 지속됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Chesed_Mercy].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Averages the Offense Level and Defense Level of all units\n- After the Chesed effect activates, allied Identities gain 3 Offense Levels and 6 Defense Levels\n- First-time Unleashing Effect: "Chesed's Mercy" lasts for the duration of this Encounter
   PL: - Poziom Ataku i Poziom Obrony wszystkich postaci są wyrównane do średniej\n- Po aktywacji efektu Cheseda sojusznicze Tożsamości zyskują dodatkowo 3 Poziomy Ataku i 6 Poziomów Obrony\n- [Efekt Pierwszego Uwolnienia] „Miłosierdzie Cheseda” trwa przez resztę walki
314. [Słowo kluczowe [Ryoshu_Attackup] — nazwa] 난도질당한 기억
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Ryoshu_Attackup].name
   kontekst: identyfikator tagu w tekstach: `[Ryoshu_Attackup]`
   limit: do 40 znaków
   EN: Mutilated Memory
   PL: Pocięta Pamięć
315. [Słowo kluczowe [Ryoshu_Attackup] — opis] [료슈 특수 효과]\n- 이번 전투에서 뇌횡에게 입히는 피해량 +(현재 턴 수 x 2.5)% (최대 30%)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Ryoshu_Attackup].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Ryōshū Exclusive Effect]\n- Deal +(Current Turn Count x 2.5)% damage against Lei Heng in this Encounter (max 30%)
   PL: [Efekt specjalny Ryōshū]\n- W tej walce zadaje Lei Hengowi +(liczba tur x 2,5)% obrażeń (maks. 30%)
316. [Słowo kluczowe [Honglu_EGOResourceup] — nazwa] 나의 마음과 생각...
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_EGOResourceup].name
   kontekst: identyfikator tagu w tekstach: `[Honglu_EGOResourceup]`
   limit: do 40 znaków
   EN: My Heart, My Own Thoughts...
   PL: Moje serce i myśli...
317. [Słowo kluczowe [Honglu_EGOResourceup] — opis] [홍루 특수 효과]\n- 이번 전투에서 자신의 스킬 공격 종료 시 해당 속성의 E.G.O 자원 2개를 추가로 얻음 (턴당 1회)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_EGOResourceup].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: [Hong Lu Exclusive Effect]\n- For this Encounter: after using a Skill Attack, gain 2 additional E.G.O resources of the Skill's Affinity (once per turn)
   PL: [Efekt specjalny Hong Lu]\n- W tej walce po zakończeniu ataku Umiejętnością zyskuje dodatkowo 2 Zasoby E.G.O Grzechu tej Umiejętności (1 raz na turę)
318. [Słowo kluczowe [BudgetBulletPropellant] — nazwa] 추진탄
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BudgetBulletPropellant].name
   kontekst: identyfikator tagu w tekstach: `[BudgetBulletPropellant]`
   limit: do 40 znaków
   EN: Propellant Ammo
   PL: Amunicja Napędowa
319. [Słowo kluczowe [BudgetBulletPropellant] — opis] - 특수 탄환\n- 특정 스킬 사용 시 소모\n- 최댓값 : 4
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BudgetBulletPropellant].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Unique Ammo\n- Spent by certain Skills\n- Max Stack: 4
   PL: - Specjalna amunicja\n- Zużywana przy użyciu określonych Umiejętności\n- Maks. stosów: 4
320. [Słowo kluczowe [NEgoFleshSpatula_LowMorale] — nazwa] 살점 주걱
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=NEgoFleshSpatula_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[NEgoFleshSpatula_LowMorale]`
   limit: do 40 znaków
   EN: Flesh Scoop
   PL: Łopatka do Mięsa
321. [Słowo kluczowe [NEgoFleshSpatula_LowMorale] — opis] - 사기 저하\n- 턴 시작시 출혈 5 획득, 공격 위력 증가 1 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=NEgoFleshSpatula_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 5 Bleed and 1 Attack Power Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 5 Krwawienia i 1 Wzrost Mocy Ataku
322. [Słowo kluczowe [NEgoFleshSpatula_Panic] — nazwa] 살점 주걱
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=NEgoFleshSpatula_Panic].name
   kontekst: identyfikator tagu w tekstach: `[NEgoFleshSpatula_Panic]`
   (powtórzenie elementu 320 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Słowo kluczowe [NEgoFleshSpatula_Panic] — opis] - 패닉\n- 턴 시작시 출혈 10 획득, 공격 위력 증가 2 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=NEgoFleshSpatula_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\nTurn Start: Gain 10 Bleed and 2 Attack Power Up
   PL: - Panika\n- Na początku tury zyskuje 10 Krwawienia i 2 Wzrostu Mocy Ataku
324. [Słowo kluczowe [LeRegole_LowMorale] — nazwa] 규율
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LeRegole_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LeRegole_LowMorale]`
   limit: do 40 znaków
   EN: Le Regole
   PL: Le Regole
325. [Słowo kluczowe [LeRegole_LowMorale] — opis] - 사기 저하\n- 전 턴에 진동을 2 이상 부여 했다면, 나태 피해량 증가 1 획득,\n- 전 턴에 화상을 2 이상 부여 했다면, 분노 피해량 증가 1 획득,\n- 아무것도 부여하지 못했으면, 방어 레벨 감소 2 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LeRegole_LowMorale].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit inflicted 2+ Tremor last turn, gain 1 Sloth DMG Up\n- If this unit inflicted 2+ Burn last turn, gain 1 Wrath DMG Up\n- If this unit failed to inflict anything, gain 2 Defense Level Down
   PL: - Niskie Morale\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Wstrząsu, zyskuje 1 Wzrost Obrażeń Lenistwa,\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Podpalenia, zyskuje 1 Wzrost Obrażeń Gniewu,\n- Jeżeli nie nałożyła niczego, zyskuje 2 Spadek Poziomu Obrony
326. [Słowo kluczowe [LeRegole_Panic] — nazwa] 규율
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LeRegole_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LeRegole_Panic]`
   (powtórzenie elementu 324 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
327. [Słowo kluczowe [LeRegole_Panic] — opis] - 패닉\n- 전 턴에 진동을 2 이상 부여 했다면, 나태 피해량 증가 2 획득,\n- 전 턴에 화상을 2 이상 부여 했다면, 분노 피해량 증가 2 획득,\n- 아무것도 부여하지 못했으면, 방어 레벨 감소 3 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LeRegole_Panic].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit inflicted 2+ Tremor last turn, gain 2 Sloth DMG Up\n- If this unit inflicted 2+ Burn last turn, gain 2 Wrath DMG Up\n- If this unit failed to inflict anything, gain 3 Defense Level Down
   PL: - Panika\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Wstrząsu, zyskuje 2 Wzrostu Obrażeń Lenistwa,\n- Jeżeli w poprzedniej turze nałożyła 2 lub więcej Podpalenia, zyskuje 2 Wzrostu Obrażeń Gniewu,\n- Jeżeli nie nałożyła niczego, zyskuje 3 Spadek Poziomu Obrony
328. [Słowo kluczowe [GazeReplica] — nazwa] 시선
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GazeReplica].name
   kontekst: identyfikator tagu w tekstach: `[GazeReplica]`
   limit: do 40 znaków
   EN: Gaze
   PL: Spojrzenie
329. [Słowo kluczowe [GazeReplica] — opis] - 최대치 : 7\n- 수치 1당 가환에게 받는 피해량과 가하는 피해량 모두 +10%\n- 수치가 7이 되면 경멸로 변경됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GazeReplica].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 7\n- Take and deal +10% damage from and against Jia Huan\n- At 7 Stack, converts to Contempt
   PL: - Maks. stosów: 7\n- Za każdy stos otrzymuje i zadaje +10% obrażeń od i wobec Jia Huana\n- Przy 7 stosach zamienia się w Pogardę
330. [Słowo kluczowe [ContemptReplica] — nazwa] 경멸
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ContemptReplica].name
   kontekst: identyfikator tagu w tekstach: `[ContemptReplica]`
   limit: do 40 znaków
   EN: Contempt
   PL: Pogarda
331. [Słowo kluczowe [ContemptReplica] — opis] - 최대치 : 1\n- 가환에게 받는 피해량과 가하는 피해량 -50%\n- 경멸이 있는 대상은 시선을 얻을 수 없음\n- 턴 종료시 소멸
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ContemptReplica].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 1\n- Take and deal -50% damage from and against Jia Huan\n- Targets with Contempt cannot gain Gaze\n- Expires at Turn End
   PL: - Maks. stosów: 1\n- Otrzymuje i zadaje -50% obrażeń od i wobec Jia Huana\n- Cele z Pogardą nie mogą zdobyć Spojrzenia\n- Znika na koniec tury
332. [Słowo kluczowe [GraspReplica] — nazwa] 손아귀
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GraspReplica].name
   kontekst: identyfikator tagu w tekstach: `[GraspReplica]`
   limit: do 40 znaków
   EN: Grasp
   PL: Uchwyt
333. [Słowo kluczowe [GraspReplica] — opis] - 최대치 : 4\n- 턴 종료시 다음 턴에 속박 10 얻음\n- 턴 종료시 수치 1 감소
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GraspReplica].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: gain 10 Bind next turn\n- Turn End: lose 1 Stack
   PL: - Maks. stosów: 4\n- Na koniec tury zyskuje 10 Spętań w następnej turze\n- Na koniec tury traci 1 stos
334. [Słowo kluczowe [EgoErodeReplica] — nazwa] E.G.O 침식 - N사
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeReplica].name
   kontekst: identyfikator tagu w tekstach: `[EgoErodeReplica]`
   limit: do 40 znaków
   EN: E.G.O Corrosion - N Corp.
   PL: Korozja E.G.O - Korporacja N
335. [Słowo kluczowe [EgoErodeReplica] — opis] - 최대치 : 10\n- 턴 시작시마다 아래 효과 적용\n· 수치만큼 정신력 감소\n· 수치 3당 공격 위력 증가 1 얻음\n- 수치가 최대치면 턴 종료시 최대 체력의 5%만큼 피해
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeReplica].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 10\n- The following effects activate at every Turn Start:\n· Lose SP by the effect's Stack\n· Gain 1 Attack Power Up for every 3 Stack\n- At Max Stack, take 5% HP damage at Turn End
   PL: - Maks. stosów: 10\n- Na początku każdej tury:\n· Traci Poczytalność równą liczbie stosów\n· Zyskuje 1 Wzrost Mocy Ataku za każde 3 stosy\n- Przy Maks. stosach otrzymuje na koniec tury 5% Maks. HP obrażeń
336. [Słowo kluczowe [BoseProjektilReplica] — nazwa] 찢어진 추억
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BoseProjektilReplica].name
   kontekst: identyfikator tagu w tekstach: `[BoseProjektilReplica]`
   limit: do 40 znaków
   EN: Torn Memory
   PL: Poszarpane Wspomnienie
337. [Słowo kluczowe [BoseProjektilReplica] — opis] 최대치: 7
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=BoseProjektilReplica].desc
   limit: do 120 znaków
   EN: Max Stack: 7
   PL: Maks. stosów: 7
338. [Słowo kluczowe [EgoErodeContempt_LowMorale] — nazwa] 여린 금으로 주조한 마음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeContempt_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[EgoErodeContempt_LowMorale]`
   limit: do 40 znaków
   EN: Soft Goldcasted Heart
   PL: Serce z Miękkiego Złota
339. [Słowo kluczowe [EgoErodeContempt_LowMorale] — opis] - 사기 저하\n- 턴 시작시 공격 위력 증가 1, 취약 1 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeContempt_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Attack Power Up and 1 Fragile
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Wzrost Mocy Ataku i 1 Wrażliwości
340. [Słowo kluczowe [EgoErodeContempt_Panic] — nazwa] 여린 금으로 주조한 마음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeContempt_Panic].name
   kontekst: identyfikator tagu w tekstach: `[EgoErodeContempt_Panic]`
   (powtórzenie elementu 338 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
341. [Słowo kluczowe [EgoErodeContempt_Panic] — opis] - 패닉\n- 턴 시작시 공격 위력 증가 2, 취약 2 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeContempt_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Attack Power Up and 2 Fragile
   PL: - Panika\n- Na początku tury zyskuje 2 Wzrostu Mocy Ataku i 2 Wrażliwości
342. [Słowo kluczowe [EgoErodeMemory_LowMorale] — nazwa] 새 시대로 향하는 마음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeMemory_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[EgoErodeMemory_LowMorale]`
   limit: do 40 znaków
   EN: Heart Toward the New Era
   PL: Serce Ku Nowej Erze
343. [Słowo kluczowe [EgoErodeMemory_LowMorale] — opis] - 사기 저하\n- 공격 적중시 자신의 정신력 3 소모, 침잠 2 부여
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeMemory_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Hit, consume 3 SP on self to inflict 2 Sinking
   PL: - Niskie Morale\n- Przy trafieniu traci 3 Poczytalności i nakłada 2 Zatonięcia
344. [Słowo kluczowe [EgoErodeMemory_Panic] — nazwa] 새 시대로 향하는 마음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeMemory_Panic].name
   kontekst: identyfikator tagu w tekstach: `[EgoErodeMemory_Panic]`
   (powtórzenie elementu 342 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Słowo kluczowe [EgoErodeMemory_Panic] — opis] - 패닉\n- 공격 적중시 침잠 3 부여, 침잠 1 얻음
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=EgoErodeMemory_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- On Hit, inflict 3 Sinking and gain 1 Sinking
   PL: - Panika\n- Przy trafieniu nakłada 3 Zatonięcia i zyskuje 1 Zatonięcie
346. [Słowo kluczowe [PileObedient] — nazwa] 쌓이는 순종
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=PileObedient].name
   kontekst: identyfikator tagu w tekstach: `[PileObedient]`
   limit: do 40 znaków
   EN: Heaping Obedience
   PL: Narastające Uposłuszeństwo
347. [Słowo kluczowe [PileObedient] — opis] - 턴 종료 시 수치가 3이면, 다음 턴에 이 효과가 공허한 순종으로 변경됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=PileObedient].desc
   limit: do 120 znaków
   EN: - Turn End: at 3 Stack, convert this effect to Hollow Obedience next turn
   PL: - Na koniec tury przy 3 stosach efekt zamienia się w następną turę w Puste Uposłuszeństwo
348. [Słowo kluczowe [Obedient] — nazwa] 공허한 순종
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Obedient].name
   kontekst: identyfikator tagu w tekstach: `[Obedient]`
   limit: do 40 znaków
   EN: Hollow Obedience
   PL: Puste Uposłuszeństwo
349. [Słowo kluczowe [Obedient] — opis] - 가모와 합 진행 시 합 위력 -2\n- 이 캐릭터의 정신력이 45가 되거나 수치가 0이 되면 해제됨\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Obedient].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Clash Power -2 in Clashes against Jia Mu\n- Expires when this unit's SP reaches 45, or when the Stack drops to 0\n- Turn End: lose 1 Stack
   PL: - W Starciu z Jia Mu Moc Starcia -2\n- Znika, gdy Poczytalność tej postaci osiągnie 45 lub wartość spadnie do 0\n- Na koniec tury maleje o 1
350. [Słowo kluczowe [ExpensiveJade] — nazwa] 보옥요람
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ExpensiveJade].name
   kontekst: identyfikator tagu w tekstach: `[ExpensiveJade]`
   limit: do 40 znaków
   EN: Precious Jade's Cradle
   PL: Kołyska Jadeitu
351. [Słowo kluczowe [ExpensiveJade] — opis] - 버프, 체력, 정신력이 갱신되지 않는 행동 불가능 상태가 되고, 이 캐릭터와 연결된 보옥이 생성됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ExpensiveJade].desc
   limit: do 170 znaków
   EN: - Enter an 'Immobilized' state where this unit's buffs, HP, and SP cannot be changed. Forms a Precious Jade connected to this unit
   PL: - Przechodzi w stan „Unieruchomienia”, w którym buffy, HP i Poczytalność nie mogą się zmieniać. Tworzy Jadeit połączony z tą postacią
352. [Słowo kluczowe [FamilyTreasure] — nazwa] 폭발유희
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=FamilyTreasure].name
   kontekst: identyfikator tagu w tekstach: `[FamilyTreasure]`
   limit: do 40 znaków
   EN: Explosive Amusement
   PL: Wybuchowa Zabawa
353. [Słowo kluczowe [FamilyTreasure] — opis] - 턴 종료 시\n· 기본 값 : 1\n· 이 유닛과 연결된 캐릭터의 체력이 최대 체력의 25%만큼 회복, 정신력 20 감소\n· 수치 1 증가\n· 수치가 3이면, 자폭 스킬을 사용함. 이 캐릭터가 자폭으로 사망한 경우, 갇혀있던 캐릭터에게 다음 턴에 공허한 순종 3을 부여함
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=FamilyTreasure].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - On Turn End:\n· Base Stack: 1\n· The unit connected to this unit heals 25% HP and loses 20 SP\n· Gain 1 Stack\n· At 3 Stack, use a self-detonation Skill. If this unit is killed by self-detonation, inflict the caged character with 3 Hollow Obedience next turn
   PL: - Na koniec tury\n· Wartość bazowa: 1\n· Postać połączona z tą jednostką leczy 25% HP i traci 20 Poczytalności\n· Wartość rośnie o 1\n· Przy wartości 3 używa Umiejętności samozniszczenia. Jeżeli ta jednostka ginie od samozniszczenia, nakłada na uwięzioną postać 3 Pustego Uposłuszeństwa w następnej turze
354. [Słowo kluczowe [OutpouringAnger] — nazwa] 발악
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=OutpouringAnger].name
   kontekst: identyfikator tagu w tekstach: `[OutpouringAnger]`
   limit: do 40 znaków
   EN: Rampage
   PL: Ostatnie Zrywy
355. [Słowo kluczowe [OutpouringAnger] — opis] - ‘너희는 그 눈의 힘과 특별함을 아직도 한참을 모르고 있구나’ 스킬의 메인 공격 대상이 홍루면, 해당 스킬의 모든 코인이 스킬 효과를 무시하고 파괴 불가 코인이 됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=OutpouringAnger].desc
   limit: do 250 znaków
   EN: - If the 'You do not know the fathoms of the eye's powers, its special nature' Skill's main target is Hong Lu, ignore all Skill effects and convert all Coins on that Skill to Unbreakable Coins
   PL: - Jeżeli głównym celem Umiejętności „Jeszcze nie pojmujesz, jak głęboka jest moc tego oka i jego szczególna natura” jest Hong Lu, wszystkie Monety tej Umiejętności ignorują efekty Umiejętności i stają się Niezniszczalnymi Monetami
356. [Słowo kluczowe [Honglu_Xi] — nazwa] 기쁨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Xi].name
   kontekst: identyfikator tagu w tekstach: `[Honglu_Xi]`
   limit: do 40 znaków
   EN: Happiness
   PL: Radość
357. [Słowo kluczowe [Honglu_Xi] — opis] - 홍루의 합 위력 +1\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 페이즈에서 1회 보옥 상태가 되지 않음. 보옥 상태로 만드는 스킬과 합 진행 시 합 위력 +5, 해당 스킬과 합에서 승리한 경우, 보옥 상태가 되지 않고 자신의 흐트러짐 해제, 가모의 정신력 10 감소, 가모에게 취약 2 부여\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Xi].desc
   limit: do 770 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Clash Power +1\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Nullfies the effect that turns this unit into a Precious Jade once. When clashing against Skills that turns this unit into a Precious Jade, Clash Power +5; if this unit wins that Clash, this unit does not become a Precious Jade, recovers from Stagger, reduces Jia Mu's SP by 10, and inflicts 2 Fragile against Jia Mu\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Starcia Hong Lu +1\n- Jeżeli w tej walce żyje co najmniej 1 inny sojusznik, gdy Hong Lu otrzyma obrażenia obniżające HP do 1, nie ginie i leczy 50% Maks. HP\n- Raz na fazę nie przechodzi w stan Jadeitu. W Starciu z Umiejętnościami zamieniającymi w Jadeit Moc Starcia +5; jeżeli wygra to Starcie, nie przechodzi w stan Jadeitu, wychodzi z Oszołomienia, obniża Poczytalność Jia Mu o 10 i nakłada na Jia Mu 2 Wrażliwości\nPo wygranym Starciu z Jia Mu zyskuje 1 losowy Zasób E.G.O z każdego z 3 Grzechów o najmniejszej liczbie zasobów
358. [Słowo kluczowe [Honglu_Le] — nazwa] 기쁨, 즐거움
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Le].name
   kontekst: identyfikator tagu w tekstach: `[Honglu_Le]`
   limit: do 40 znaków
   EN: Happiness, Joy
   PL: Radość, Rozkosz
359. [Słowo kluczowe [Honglu_Le] — opis] - 홍루의 최종 위력 +1\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Le].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +1\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lu +1\n- Po wygranym Starciu 1 sojusznik (w tym ta jednostka) o najniższej Poczytalności odzyskuje 5 Poczytalności\n- Jeżeli w tej walce żyje co najmniej 1 inny sojusznik, gdy Hong Lu otrzyma obrażenia obniżające HP do 1, nie ginie i leczy 50% Maks. HP\nPo wygranym Starciu z Jia Mu zyskuje 1 losowy Zasób E.G.O z każdego z 3 Grzechów o najmniejszej liczbie zasobów
360. [Słowo kluczowe [Honglu_Ai] — nazwa] 기쁨, 즐거움, 슬픔
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Ai].name
   kontekst: identyfikator tagu w tekstach: `[Honglu_Ai]`
   limit: do 40 znaków
   EN: Happiness, Joy, Sorrow
   PL: Radość, Rozkosz, Smutek
361. [Słowo kluczowe [Honglu_Ai] — opis] - 홍루의 최종 위력 +3\n- 합 승리 시, 정신력이 가장 낮은 아군 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Ai].desc
   limit: do 600 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +3\n- On Clash Win, heal 5 SP for 1 ally with the least SP (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lu +3\n- Po wygranym Starciu 1 sojusznik (w tym ta jednostka) o najniższej Poczytalności odzyskuje 5 Poczytalności\n- Gdy ginie sojusznik, pozostali sojusznicy na koniec tury zyskują 1 Wzrost Mocy Ataku na następną turę (1 raz na turę)\n- Jeżeli w tej walce żyje co najmniej 1 inny sojusznik, gdy Hong Lu otrzyma obrażenia obniżające HP do 1, nie ginie i leczy 50% Maks. HP\nPo wygranym Starciu z Jia Mu zyskuje 1 losowy Zasób E.G.O z każdego z 3 Grzechów o najmniejszej liczbie zasobów
362. [Słowo kluczowe [Honglu_Nu] — nazwa] 기쁨, 즐거움, 슬픔, 분노
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Nu].name
   kontekst: identyfikator tagu w tekstach: `[Honglu_Nu]`
   limit: do 50 znaków
   EN: Happiness, Joy, Sorrow, Wrath
   PL: Radość, Rozkosz, Smutek, Gniew
363. [Słowo kluczowe [Honglu_Nu] — opis] - 홍루의 최종 위력 +5\n- 매 턴 시작 시 모든 아군의 정신력 5 회복 (자신 포함)\n- 아군이 사망한 경우, 턴 종료 시 남은 아군이 다음 턴에 공격 위력 증가 1을 얻음 (턴 당 1회)\n- 이번 전투에서 다른 아군이 1명 이상 살아있는 경우, 홍루의 체력이 1이 되는 피해를 받았을 때, 사망하지 않고 최대 체력의 50%만큼 체력을 회복함\n- 이번 전투에서 누적으로 잃은 체력 비율의 30%만큼 피해량 증가 (최대 100%)\n가모와 합 승리 시 수량이 가장 부족한 E.G.O 자원 중 무작위 속성의 자원을 1개씩, 총 3개 획득
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=Honglu_Nu].desc
   limit: do 740 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Hong Lu's Final Power +5\n- Allies heal 5 SP at every Turn Start (including this unit)\n- When an ally is killed, the remaining allies at Turn End gain 1 Attack Power Up next turn (once per turn)\n- When there are 1 or more surviving allies in this Encounter: upon taking fatal damage, Hong Lu does not die and heals 50% HP instead\n- Increases damage dealt by 30% of the total HP percentage this unit has cumulatively lost during this Encounter (max 100%)\nOn Clash Win against Jia Mu, gain 1 random E.G.O Resource each from 3 of the E.G.O Affinities with the least amount of resources
   PL: - Moc Końcowa Hong Lu +5\n- Na początku każdej tury wszyscy sojusznicy odzyskują 5 Poczytalności (w tym ta jednostka)\n- Gdy ginie sojusznik, pozostali sojusznicy na koniec tury zyskują 1 Wzrost Mocy Ataku na następną turę (1 raz na turę)\n- Jeżeli w tej walce żyje co najmniej 1 inny sojusznik, gdy Hong Lu otrzyma obrażenia obniżające HP do 1, nie ginie i leczy 50% Maks. HP\n- Zwiększa zadawane obrażenia o 30% łącznego procenta HP utraconego w tej walce (maks. 100%)\nPo wygranym Starciu z Jia Mu zyskuje 1 losowy Zasób E.G.O z każdego z 3 Grzechów o najmniejszej liczbie zasobów
364. [Słowo kluczowe [SupremeEternalLife] — nazwa] 지고한 불사
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=SupremeEternalLife].name
   kontekst: identyfikator tagu w tekstach: `[SupremeEternalLife]`
   limit: do 40 znaków
   EN: Sublime Immortality
   PL: Wzniosła Nieśmiertelność
365. [Słowo kluczowe [SupremeEternalLife] — opis] - 턴 시작 시 가모의 본체와 모든 부위에 각 최대 체력의 5%만큼 보호막 부여
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=SupremeEternalLife].desc
   limit: do 120 znaków
   EN: - Turn Start: Jia Mu's Core and every Part gain 5% of each of their max HP as Shield
   PL: - Na początku tury nakłada korpusowi i wszystkim częściom Jia Mu Tarczę równą 5% Maks. HP każdego z nich
366. [Słowo kluczowe [ImperfectEternalLife] — nazwa] 불완전한 불사
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ImperfectEternalLife].name
   kontekst: identyfikator tagu w tekstach: `[ImperfectEternalLife]`
   limit: do 40 znaków
   EN: Imperfect Immortality
   PL: Niedoskonała Nieśmiertelność
367. [Słowo kluczowe [ImperfectEternalLife] — opis] - 가모의 특정 스킬에 피격 시 흡수 당함\n- 이 효과가 가모에게 부여된 경우, 수치당 취약 1 얻고, 수치가 5면, 흐트러짐 상태가 됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=ImperfectEternalLife].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Absorbed when struck by certain Skills of Jia Mu\n- If this effect was inflicted against Jia Mu, gain 1 Fragile per Stack; at 5 Stack, become Staggered
   PL: - Jest absorbowany przy trafieniu określonymi Umiejętnościami Jia Mu\n- Jeżeli ten efekt nałożono na Jia Mu, zyskuje 1 Wrażliwości za każdy stos; przy 5 stosach przechodzi w stan Oszołomienia
368. [Słowo kluczowe [GoldenBoughSync] — nazwa] 부감응
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GoldenBoughSync].name
   kontekst: identyfikator tagu w tekstach: `[GoldenBoughSync]`
   limit: do 40 znaków
   EN: Malattunement
   PL: Zdegradowane Dostrojenie
369. [Słowo kluczowe [GoldenBoughSync] — opis] - 기본 공격 레벨 +2, 기본 방어 레벨 +2
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GoldenBoughSync].desc
   limit: do 120 znaków
   EN: - Base Offense Level +2, Base Defense Level +2
   PL: - Podstawowy Poziom Ataku +2, Podstawowy Poziom Obrony +2
370. [Słowo kluczowe [GoldenBoughSyncDistorted] — nazwa] 괴력난신
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GoldenBoughSyncDistorted].name
   kontekst: identyfikator tagu w tekstach: `[GoldenBoughSyncDistorted]`
   limit: do 60 znaków
   EN: Supernatural, Strength, Chaos, and Spirits
   PL: Demoniczna Siła i Chaotyczne Duchy
371. [Słowo kluczowe [GoldenBoughSyncDistorted] — opis] - 기본 공격 레벨 +4, 기본 방어 레벨 +4
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GoldenBoughSyncDistorted].desc
   limit: do 120 znaków
   EN: - Base Offense Level +4, Base Defense Level +4
   PL: - Podstawowy Poziom Ataku +4, Podstawowy Poziom Obrony +4
372. [Słowo kluczowe [LastingHongwonWill_LowMorale] — nazwa] 계승된 홍원의 뜻
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LastingHongwonWill_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LastingHongwonWill_LowMorale]`
   limit: do 40 znaków
   EN: Inherited Will of Hongyuan
   PL: Odziedziczona Wola Hongyuan
373. [Słowo kluczowe [LastingHongwonWill_LowMorale] — opis] - 사기저하\n- 공격 위력 증가 2, 속박 1 얻음\n- 홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 피해량 증가 1, 취약 1 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LastingHongwonWill_LowMorale].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Bind\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 1 Damage Up and 1 Fragile next turn (once per turn)
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Spętanie\n- Gdy część Tułowia przegra Starcie z Hong Lu, część Tułowia zyskuje 1 Wzrost Obrażeń i 1 Wrażliwości w następnej turze (1 raz na turę)
374. [Słowo kluczowe [LastingHongwonWill_Panic] — nazwa] 계승된 홍원의 뜻
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LastingHongwonWill_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LastingHongwonWill_Panic]`
   (powtórzenie elementu 372 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
375. [Słowo kluczowe [LastingHongwonWill_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 속박 2 얻음\n- 홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 피해량 증가 2, 취약 2 얻음 (턴 당 1회)
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LastingHongwonWill_Panic].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up and 2 Bind\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 2 Damage Up and 2 Fragile next turn (once per turn)
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku i 2 Spętań\n- Gdy część Tułowia przegra Starcie z Hong Lu, część Tułowia zyskuje 2 Wzrostu Obrażeń i 2 Wrażliwości w następnej turze (1 raz na turę)
376. [Słowo kluczowe [LongLastingHongwonWill_LowMorale] — nazwa] 유구히 계승될 홍원의 뜻
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LongLastingHongwonWill_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[LongLastingHongwonWill_LowMorale]`
   limit: do 60 znaków
   EN: Infinitely Bequeathing Will of Hongyuan
   PL: Wiecznie Przekazywana Wola Hongyuan
377. [Słowo kluczowe [LongLastingHongwonWill_LowMorale] — opis] - 사기저하\n- 공격 위력 증가 2, 취약 1 얻음\n- 자신이 생성한 유닛이 방어 레벨 감소 3 얻음\n- 가하는 피해량 20% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 10% 감소
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LongLastingHongwonWill_LowMorale].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 2 Attack Power Up and 1 Fragile\n- Units generated by this unit gain 3 Defense Level Down\n- Deal +20% damage. If the Palanquin Part's HP drops to 0, deal -10% damage instead
   PL: - Niskie Morale\n- Zyskuje 2 Wzrostu Mocy Ataku i 1 Wrażliwości\n- Jednostki wytworzone przez tę jednostkę zyskują 3 Spadek Poziomu Obrony\n- Zadaje +20% obrażeń. Jeżeli HP części Lektyki spadnie do 0, zamiast tego zadaje -10% obrażeń
378. [Słowo kluczowe [LongLastingHongwonWill_Panic] — nazwa] 유구히 계승될 홍원의 뜻
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LongLastingHongwonWill_Panic].name
   kontekst: identyfikator tagu w tekstach: `[LongLastingHongwonWill_Panic]`
   (powtórzenie elementu 376 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
379. [Słowo kluczowe [LongLastingHongwonWill_Panic] — opis] - 패닉\n- 공격 위력 증가 2, 취약 2 얻음\n- 자신이 생성한 유닛이 방어 레벨 감소 6 얻음\n- 가하는 피해량 30% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 15% 감소
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=LongLastingHongwonWill_Panic].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Attack Power Up and 2 Fragile\n- Units generated by this unit gain 6 Defense Level Down\n- Deal +30% damage. If the Palanquin Part's HP drops to 0, deal -15% damage instead
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Ataku i 2 Wrażliwości\n- Jednostki wytworzone przez tę jednostkę zyskują 6 Spadek Poziomu Obrony\n- Zadaje +30% obrażeń. Jeżeli HP części Lektyki spadnie do 0, zamiast tego zadaje -15% obrażeń
380. [Słowo kluczowe [YisangParryGubo] — nazwa] 책임감
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=YisangParryGubo].name
   kontekst: identyfikator tagu w tekstach: `[YisangParryGubo]`
   limit: do 40 znaków
   EN: Responsibility
   PL: Poczucie Obowiązku
381. [Słowo kluczowe [YisangParryGubo] — opis] 구보와 합을 진행할 때, 합 위력 +2
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=YisangParryGubo].desc
   limit: do 120 znaków
   EN: In Clashes against Gubo, Clash Power +2
   PL: W Starciach z Gubo Moc Starcia +2
382. [Słowo kluczowe [HongluParryGahwan] — nazwa] 마주하려는 의지
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=HongluParryGahwan].name
   kontekst: identyfikator tagu w tekstach: `[HongluParryGahwan]`
   limit: do 40 znaków
   EN: The Will to Confront
   PL: Wola Konfrontacji
383. [Słowo kluczowe [HongluParryGahwan] — opis] 가환과 합을 진행할 때, 합 위력 +2
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=HongluParryGahwan].desc
   limit: do 120 znaków
   EN: In Clashes against Jia Huan, Clash Power +2
   PL: W Starciach z Jia Huanem Moc Starcia +2
384. [Słowo kluczowe [GahwanEgoContempt] — nazwa] 불안정 E.G.O 감응 - 경멸
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GahwanEgoContempt].name
   kontekst: identyfikator tagu w tekstach: `[GahwanEgoContempt]`
   limit: do 50 znaków
   EN: Volatile E.G.O Attunement - Contempt
   PL: Niestabilne Dostrojenie E.G.O - Pogarda
385. [Słowo kluczowe [GahwanEgoContempt] — opis] - N사에서 추출한 E.G.O 장비. 적성에는 맞으나 경험은 적어 아직 사용에 익숙하지 않다.\n- 최대값 : 5\n- 공격 레벨, 방어 레벨 -7\n- 합 승리 시 수치 1 증가\n- 수치 1 당 공격 레벨 1 감소, 방어 레벨 1 증가\n- 수치가 최대치면, 다음 턴에 보호 2를 얻고 수치 0으로 초기화
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GahwanEgoContempt].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - E.G.O Gear extracted by N Corp. While the user meets the aptitude requirements, the lack of experience may cause issues.\n- Max Stack: 5\n- Offense Level, Defense Level -7\n- On Clash Win, gain 1 Stack\n- Lose 1 Offense Level and gain 1 Defense Level for every Stack\n- At Max Stack: next turn, gain 2 Protection and reset the Stack to 0
   PL: - E.G.O wyekstrahowane przez Korporację N. Użytkownik spełnia wymogi predyspozycji, ale brak doświadczenia może sprawiać trudności.\n- Maks. stosów: 5\n- Poziom Ataku i Poziom Obrony -7\n- Po wygranym Starciu zyskuje 1 stos\n- Traci 1 Poziom Ataku i zyskuje 1 Poziom Obrony za każdy stos\n- Przy Maks. stosach zyskuje w następnej turze 2 Ochrony i resetuje liczbę stosów do 0
386. [Słowo kluczowe [GuboEgoShooter] — nazwa] 불안정 E.G.O 감응 - 흉탄
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GuboEgoShooter].name
   kontekst: identyfikator tagu w tekstach: `[GuboEgoShooter]`
   limit: do 60 znaków
   EN: Volatile E.G.O Attunement - Fell Bullet
   PL: Niestabilne Dostrojenie E.G.O - Zabójczy Pocisk
387. [Słowo kluczowe [GuboEgoShooter] — opis] - N사에서 추출한 E.G.O 장비. 적성에는 맞으나 경험은 적어 아직 사용에 익숙하지 않다.\n- 최대값 : 5\n- 공격 레벨, 방어 레벨  -2\n- 합 패배 시 수치 1 증가\n- 수치 1 당 공격 레벨 1 증가, 방어 레벨 1 감소\n- 수치가 최대치면, 다음 턴에 피해량 증가 2를 얻고 수치 0으로 초기화
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=GuboEgoShooter].desc
   limit: do 430 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - E.G.O Gear extracted by N Corp. While the user meets the aptitude requirements, the lack of experience may cause issues.\n- Max Stack: 5\n- Offense Level, Defense Level -2\n- On Clash Lose, gain 1 Stack\n- Gain 1 Offense Level and lose 1 Defense Level for every Stack\n- At Max Stack: next turn, gain 2 Damage Up and reset the Stack to 0
   PL: - E.G.O wyekstrahowane przez Korporację N. Użytkownik spełnia wymogi predyspozycji, ale brak doświadczenia może sprawiać trudności.\n- Maks. stosów: 5\n- Poziom Ataku i Poziom Obrony -2\n- Po przegranej w Starciu zyskuje 1 stos\n- Zyskuje 1 Poziom Ataku i traci 1 Poziom Obrony za każdy stos\n- Przy Maks. stosach zyskuje w następnej turze 2 Wzrost Obrażeń i resetuje liczbę stosów do 0
388. [Słowo kluczowe [FellBulletMarkReplica] — nazwa] 징표
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=FellBulletMarkReplica].name
   kontekst: identyfikator tagu w tekstach: `[FellBulletMarkReplica]`
   limit: do 40 znaków
   EN: Stigmatized
   PL: Naznaczony
389. [Słowo kluczowe [FellBulletMarkReplica] — opis] - 구보의 표적이 됨\n- 턴 종료시 제거됨
   źródło: BattleKeywords-a1c8p3.json :: dataList[id=FellBulletMarkReplica].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Tageted by Gubo\n- Expires at Turn End
   PL: - Staje się celem Gubo\n- Znika na koniec tury

## Słowa kluczowe bitwy — BattleKeywords-a1c9114
- plik gry: `BattleKeywords-a1c9114.json` (opisy wyświetlane w dymkach pomocy podczas walki)

390. [Słowo kluczowe [A1c971a] — nazwa] 끓어오르는 분노
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971a].name
   kontekst: identyfikator tagu w tekstach: `[A1c971a]`
   limit: do 40 znaków
   EN: Boiling Wrath
   PL: Wrzący Gniew
391. [Słowo kluczowe [A1c971a] — opis] 매 턴 시작 시, 턴 수만큼 화상을 얻음.
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971a].desc
   limit: do 120 znaków
   EN: Every Turn Start: gain Burn equal to Turn Count
   PL: Na początku każdej tury zyskuje Podpalenie równe liczbie tur.
392. [Słowo kluczowe [A1c971b] — nazwa] 퍼져나가는 우울
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971b].name
   kontekst: identyfikator tagu w tekstach: `[A1c971b]`
   limit: do 40 znaków
   EN: Propagating Gloom
   PL: Rozprzestrzeniająca się Posępność
393. [Słowo kluczowe [A1c971b] — opis] 턴 종료 시, 수치가 1이라면 체력이 가장 적은 적에게 자신의 현재 체력만큼 피해를 입히고 사망함\n턴 종료 시, 1 감소
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971b].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: at 1 Stack, inflict damage equal to this unit's current HP against the enemy with the least HP, then die\nReduced by 1 at Turn End
   PL: Na koniec tury, jeżeli wartość wynosi 1, zadaje wrogowi z najmniejszym HP obrażenia równe swojemu obecnemu HP i ginie\nNa koniec tury maleje o 1
394. [Słowo kluczowe [A1c971c] — nazwa] 계속되는 탐식
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971c].name
   kontekst: identyfikator tagu w tekstach: `[A1c971c]`
   limit: do 40 znaków
   EN: Perpetuating Gluttony
   PL: Nieustanne Obżarstwo
395. [Słowo kluczowe [A1c971c] — opis] 턴 시작 시, 진행된 턴 수 2당 체력 회복량 증가 1 얻음 (최대 5)\n턴 시작 시, 회복한 체력량 10당 피해량 증가 1, 합 위력 증가 1 얻음 (최대 5)\n\n회복한 체력량: {0}
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971c].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: {0}, \n
   EN: Turn Start: gain 1 HP heal boost every 2 turns (max 5)\nTurn Start: gain 1 Damage Up and 1 Clash Power Up for every 10 HP healed (max 5)\n\nHP Healed: {0}
   PL: Na początku tury zyskuje 1 Wzrost Leczenia HP za każde 2 tury (maks. 5)\nNa początku tury zyskuje 1 Wzrost Obrażeń i 1 Wzrost Mocy Starcia za każde 10 wyleczonych HP (maks. 5)\n\nWyleczone HP: {0}
396. [Słowo kluczowe [A1c971d] — nazwa] 뱉어내는 호흡
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971d].name
   kontekst: identyfikator tagu w tekstach: `[A1c971d]`
   limit: do 40 znaków
   EN: Gasping Breath
   PL: Dyszący Oddech
397. [Słowo kluczowe [A1c971d] — opis] 호흡을 얻을 때, 호흡 추가 3 얻음 혹은 호흡 횟수 추가 2 증가
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971d].desc
   limit: do 120 znaków
   EN: When gaining Poise, gain 3 additional Poise or +2 additional Poise Count
   PL: Przy zdobyciu Oddechu zyskuje dodatkowo 3 Oddechu lub +2 Licznika Oddechu
398. [Słowo kluczowe [A1c971e] — nazwa] 상처속의 상처
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971e].name
   kontekst: identyfikator tagu w tekstach: `[A1c971e]`
   limit: do 40 znaków
   EN: Wounded Wound
   PL: Rana w Ranę
399. [Słowo kluczowe [A1c971e] — opis] 적중시, 출혈 추가 2 부여 혹은 출혈 횟수 추가 1 증가
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971e].desc
   limit: do 120 znaków
   EN: On Hit, inflict 2 additional Bleed or +1 additional Bleed Count
   PL: Przy trafieniu nakłada 2 dodatkowe Krwawienia lub zwiększa Licznik Krwawienia o +1
400. [Słowo kluczowe [A1c971f] — nazwa] 게으른 나태
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971f].name
   kontekst: identyfikator tagu w tekstach: `[A1c971f]`
   limit: do 40 znaków
   EN: Lazy Sloth
   PL: Leniwe Lenistwo
401. [Słowo kluczowe [A1c971f] — opis] 턴 종료 시 1 감소.\n0이 되면, EX클리어 실패.
   źródło: BattleKeywords-a1c9114.json :: dataList[id=A1c971f].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Reduced by 1 at Turn End.\nFails Extra Condition at 0
   PL: Na koniec tury maleje o 1.\nPrzy 0 — niepowodzenie Warunku Dodatkowego.

## Słowa kluczowe bitwy — BattleKeywords-a1c9116
- plik gry: `BattleKeywords-a1c9116.json` (opisy wyświetlane w dymkach pomocy podczas walki)

402. [Słowo kluczowe [BurstAgility] — nazwa] 주살【신속】
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BurstAgility].name
   kontekst: identyfikator tagu w tekstach: `[BurstAgility]`
   limit: do 40 znaków
   EN: Deathrite【Haste】
   PL: Obrzęd Śmierci 【Haste】
403. [Słowo kluczowe [BurstAgility] — opis] 기본값: 3\n속도가 10 이상인 대상에게 공격 스킬로 피격되어 파열이 발동될 때 1 감소, 자신의 파열 횟수 1 증가\n수치가 0이 될 때, (파열 위력)만큼 탐식 속성 피해를 받고 소멸\n※ 이 효과는 갱신되지 않음
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BurstAgility].desc
   limit: do 400 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Stack: 3\nWhen getting Rupture triggered by getting hit by an Attack Skill from a target with 10+ Speed, lose 1 Stack and gain +1 Rupture Count\nAt 0 Stack, take Gluttony damage equal to Rupture Potency on self; then, this effect expires\n※ Cannot gain additional Stacks of this effect while it is already active
   PL: Wartość bazowa: 3\nGdy wywołane zostaje Rozdarcie po trafieniu Umiejętnością ataku celu o Szybkości 10 lub większej, maleje o 1, a Licznik Rozdarcia rośnie o 1\nPrzy wartości 0 otrzymuje obrażenia Obżarstwa równe Sile Rozdarcia, po czym znika\n※ Ten efekt nie odnawia się
404. [Słowo kluczowe [BurstAgility] — podsumowanie] 조건 만족시, 탐식 추가 피해 입힘
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BurstAgility].summary
   limit: do 120 znaków
   EN: If conditions are met: inflict Gluttony bonus damage
   PL: Po spełnieniu warunków otrzymuje dodatkowe obrażenia Obżarstwa
405. [Słowo kluczowe [LegStrength] — nazwa] 각력【묘】
   źródło: BattleKeywords-a1c9116.json :: dataList[id=LegStrength].name
   kontekst: identyfikator tagu w tekstach: `[LegStrength]`
   limit: do 40 znaków
   EN: Strider【Mao】
   PL: Biegacz【Mao】
406. [Słowo kluczowe [LegStrength] — opis] 최댓값: 3\n턴 종료 시 다음 턴에 신속을 5 얻음\n턴 종료 시 1 감소
   źródło: BattleKeywords-a1c9116.json :: dataList[id=LegStrength].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 3\nTurn End: gain 5 Haste next turn\nReduced by 1 at Turn End
   PL: Maks. stosów: 3\nNa koniec tury zyskuje 5 Pośpiechu w następnej turze\nNa koniec tury maleje o 1
407. [Słowo kluczowe [LegStrength] — podsumowanie] 조건 만족시, 탐식 추가 피해 입힘
   źródło: BattleKeywords-a1c9116.json :: dataList[id=LegStrength].summary
   (powtórzenie elementu 404 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
408. [Słowo kluczowe [DarkBeast_LowMorale] — nazwa] 암수
   źródło: BattleKeywords-a1c9116.json :: dataList[id=DarkBeast_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[DarkBeast_LowMorale]`
   limit: do 40 znaków
   EN: Deception
   PL: Podstęp
409. [Słowo kluczowe [DarkBeast_LowMorale] — opis] - 사기 저하\n- 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +10%
   źródło: BattleKeywords-a1c9116.json :: dataList[id=DarkBeast_LowMorale].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +10% damage against the target
   PL: - Niskie Morale\n- Jeżeli Szybkość tej jednostki jest większa niż celu lub przy Ataku Jednostronnym, zadaje +10% obrażeń celowi
410. [Słowo kluczowe [DarkBeast_Panic] — nazwa] 암수
   źródło: BattleKeywords-a1c9116.json :: dataList[id=DarkBeast_Panic].name
   kontekst: identyfikator tagu w tekstach: `[DarkBeast_Panic]`
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
411. [Słowo kluczowe [DarkBeast_Panic] — opis] - 패닉\n- 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +20%, 자신의 속도가 대상보다 빠르면, 받는 피해량 -20%
   źródło: BattleKeywords-a1c9116.json :: dataList[id=DarkBeast_Panic].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +20% damage against the target; if this unit's Speed is faster than the target's, take -20% damage
   PL: - Panika\n- Jeżeli Szybkość tej jednostki jest większa niż celu lub przy Ataku Jednostronnym, zadaje +20% obrażeń celowi; jeżeli Szybkość jest większa, otrzymuje -20% obrażeń
412. [Słowo kluczowe [RepressedMurderousIntend] — nazwa] 억눌린 살기
   źródło: BattleKeywords-a1c9116.json :: dataList[id=RepressedMurderousIntend].name
   kontekst: identyfikator tagu w tekstach: `[RepressedMurderousIntend]`
   limit: do 40 znaków
   EN: Repressed Bloodthirst
   PL: Stłumiona Krwiożerczość
413. [Słowo kluczowe [RepressedMurderousIntend] — opis] 기본 공격 레벨 -10, 기본 방어 레벨 -10
   źródło: BattleKeywords-a1c9116.json :: dataList[id=RepressedMurderousIntend].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -10\nBase Defense Level -10
   PL: Podstawowy Poziom Ataku -10, Podstawowy Poziom Obrony -10
414. [Słowo kluczowe [WeighedMurderousIntend] — nazwa] 짓눌린 살기
   źródło: BattleKeywords-a1c9116.json :: dataList[id=WeighedMurderousIntend].name
   kontekst: identyfikator tagu w tekstach: `[WeighedMurderousIntend]`
   limit: do 40 znaków
   EN: Crushed Bloodthirst
   PL: Rozgnieciona Krwiożerczość
415. [Słowo kluczowe [WeighedMurderousIntend] — opis] 기본 공격 레벨 -25, 기본 방어 레벨 -25
   źródło: BattleKeywords-a1c9116.json :: dataList[id=WeighedMurderousIntend].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Base Offense Level -25\nBase Defense Level -25
   PL: Podstawowy Poziom Ataku -25, Podstawowy Poziom Obrony -25
416. [Słowo kluczowe [MiddleFingerBook] — nazwa] 중지의 복수 대상
   źródło: BattleKeywords-a1c9116.json :: dataList[id=MiddleFingerBook].name
   kontekst: identyfikator tagu w tekstach: `[MiddleFingerBook]`
   limit: do 40 znaków
   EN: The Middle's Vendetta Mark
   PL: Cel Zemsty Środkowego
417. [Słowo kluczowe [MiddleFingerBook] — opis] 최댓값 : 10\n중지 소속에게 공격당할 때, 받는 피해량 +3% (최대 30%)
   źródło: BattleKeywords-a1c9116.json :: dataList[id=MiddleFingerBook].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 10\nWhen attacked by The Middle, take +3% damage per Stack (max 30%)
   PL: Maks. stosów: 10\nPrzy ataku przez Środkowy otrzymuje +3% obrażeń za każdy stos (maks. 30%)
418. [Słowo kluczowe [Persistent] — nazwa] 끈질김
   źródło: BattleKeywords-a1c9116.json :: dataList[id=Persistent].name
   kontekst: identyfikator tagu w tekstach: `[Persistent]`
   limit: do 40 znaków
   EN: Persistence
   PL: Wytrwałość
419. [Słowo kluczowe [Persistent] — opis] 최댓값 : 4\n체력이 0이 되는 피해를 받으면, 80% 확률로 해당 피해를 받지 않고, 체력을 60 회복, 흐트러짐 해제하고 이 버프 소멸\n\n아래 상황에서는 사망 방지 및 회복 효과가 발동하지 않음\n- 피격 시 코인 피해량이 자신의 최대 체력을 초과\n- 체력 회복 감소 효과를 보유\n턴 종료시 수치 1 감소
   źródło: BattleKeywords-a1c9116.json :: dataList[id=Persistent].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Max Stack: 4\nWhen taking lethal damage, 80% chance to not take that damage, heal 60 HP, recover from Stagger, and lose this effect\n\nThe above effects do not activate under the following conditions:\n- When the Coin damage taken exceeds this unit's max HP\n- When this unit has the HP Healing Down effect\nReduced by 1 at Turn End
   PL: Maks. stosów: 4\nGdy otrzymuje obrażenia redukujące HP do 0, z 80% szansą nie otrzymuje ich, leczy 60 HP, wychodzi z Oszołomienia i traci ten buff\n\nPoniższe efekty nie działają w następujących sytuacjach:\n- Gdy obrażenia Monety przy trafieniu przekraczają Maks. HP\n- Gdy posiada efekt obniżenia Leczenia HP\nNa koniec tury traci 1 stos
420. [Słowo kluczowe [BackstreetsNight_LowMorale] — nazwa] 뒷골목의 밤
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BackstreetsNight_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BackstreetsNight_LowMorale]`
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
421. [Słowo kluczowe [BackstreetsNight_LowMorale] — opis] 턴 시작시 공격 위력 증가 1, 체력 회복 증가 1, 취약 1을 얻음
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BackstreetsNight_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: gain 1 Attack Power Up, 1 HP Healing Boost, and 1 Fragile
   PL: Na początku tury zyskuje 1 Wzrost Mocy Ataku, 1 Wzrost Leczenia HP i 1 Wrażliwości
422. [Słowo kluczowe [BackstreetsNight_Panic] — nazwa] 뒷골목의 밤
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BackstreetsNight_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BackstreetsNight_Panic]`
   (powtórzenie elementu 420 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Słowo kluczowe [BackstreetsNight_Panic] — opis] 턴 시작시 공격 위력 증가 2, 체력 회복 증가 2, 취약 1을 얻음
   źródło: BattleKeywords-a1c9116.json :: dataList[id=BackstreetsNight_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: gain 2 Attack Power Up, 2 HP Healing Boost, and 1 Fragile
   PL: Na początku tury zyskuje 2 Wzrostu Mocy Ataku, 2 Wzrost Leczenia HP i 1 Wrażliwości
424. [Słowo kluczowe [SweeperA] — nazwa] 제 1파
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperA].name
   kontekst: identyfikator tagu w tekstach: `[SweeperA]`
   limit: do 40 znaków
   EN: The First Wave
   PL: Pierwsza Fala
425. [Słowo kluczowe [SweeperA] — opis] {0}턴 후 제 1파 종료
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperA].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The first wave ends after {0} turn(s)
   PL: Pierwsza fala kończy się po {0} turach
426. [Słowo kluczowe [SweeperB] — nazwa] 제 2파
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperB].name
   kontekst: identyfikator tagu w tekstach: `[SweeperB]`
   limit: do 40 znaków
   EN: The Second Wave
   PL: Druga Fala
427. [Słowo kluczowe [SweeperB] — opis] {0}턴 후 제 2파 종료
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperB].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The second wave ends after {0} turn(s)
   PL: Druga fala kończy się po {0} turach
428. [Słowo kluczowe [SweeperC] — nazwa] 제 3파
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperC].name
   kontekst: identyfikator tagu w tekstach: `[SweeperC]`
   limit: do 40 znaków
   EN: The Third Wave
   PL: Trzecia Fala
429. [Słowo kluczowe [SweeperC] — opis] {0}턴 후 제 3파 종료
   źródło: BattleKeywords-a1c9116.json :: dataList[id=SweeperC].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: The third wave ends after {0} turn(s)
   PL: Trzecia fala kończy się po {0} turach

## Słowa kluczowe bitwy — BattleKeywords-a1c951
- plik gry: `BattleKeywords-a1c951.json` (opisy wyświetlane w dymkach pomocy podczas walki)

430. [Słowo kluczowe [AaCeSeBa] — nazwa] 호!호!호!
   źródło: BattleKeywords-a1c951.json :: dataList[id=AaCeSeBa].name
   kontekst: identyfikator tagu w tekstach: `[AaCeSeBa]`
   limit: do 40 znaków
   EN: HO! HO! HO!
   PL: HO! HO! HO!
431. [Słowo kluczowe [AaCeSeBa] — opis] 턴 종료 시 (가지고 있는 호흡 / 5)만큼 다음 턴에 호흡 횟수를 얻음.\n충전이 0이되면, 제거됨.
   źródło: BattleKeywords-a1c951.json :: dataList[id=AaCeSeBa].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Turn End: Gain (Poise on self/5) Poise Count next turn.\nExpires at 0 Charge.
   PL: Na koniec tury zyskuje Licznika Oddechu równy (posiadany Oddech / 5) w następnej turze.\nZnika przy 0 Ładunku.
432. [Słowo kluczowe [AaCeSeBb] — nazwa] 선물로 만들어주마
   źródło: BattleKeywords-a1c951.json :: dataList[id=AaCeSeBb].name
   kontekst: identyfikator tagu w tekstach: `[AaCeSeBb]`
   limit: do 40 znaków
   EN: I'll Gift-wrap You
   PL: Zapakuję Cię na Prezent
433. [Słowo kluczowe [AaCeSeBb] — opis] 매 턴마다 호흡 3을 얻음.\n턴 종료시 피해를 입힌 공격 스킬당 정신력 3 회복
   źródło: BattleKeywords-a1c951.json :: dataList[id=AaCeSeBb].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Gain 3 Poise every turn.\nTurn End: Heal 3 SP for every Attack Skill that dealt damage
   PL: Zyskuje 3 Oddechu co turę.\nNa koniec tury odzyskuje 3 Poczytalności za każdą Umiejętność ataku, która zadała obrażenia

## Słowa kluczowe bitwy — BattleKeywords-a1c971
- plik gry: `BattleKeywords-a1c971.json` (opisy wyświetlane w dymkach pomocy podczas walki)

434. [Słowo kluczowe [Bloodthirst] — nazwa] 피갈망
   źródło: BattleKeywords-a1c971.json :: dataList[id=Bloodthirst].name
   kontekst: identyfikator tagu w tekstach: `[Bloodthirst]`
   limit: do 40 znaków
   EN: Yearning for Blood
   PL: Tęsknota za Krwią
435. [Słowo kluczowe [Bloodthirst] — opis] - 기본 공격 레벨 35 감소\n- 기본 방어 레벨 35 감소
   źródło: BattleKeywords-a1c971.json :: dataList[id=Bloodthirst].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -35\n- Base Defense Level -35
   PL: - Podstawowy Poziom Ataku -35\n- Podstawowy Poziom Obrony -35
436. [Słowo kluczowe [ObservedPerson] — nazwa] 피관찰자
   źródło: BattleKeywords-a1c971.json :: dataList[id=ObservedPerson].name
   kontekst: identyfikator tagu w tekstach: `[ObservedPerson]`
   limit: do 40 znaków
   EN: Subject of Observation
   PL: Obiekt Obserwacji
437. [Słowo kluczowe [ObservedPerson] — opis] - 최대 30\n- 턴 시작 시, 3 증가 (획득한 다음 턴부터 적용)\n- 뒤틀린 호엔하임에게 공격 스킬 효과로 피해를 받거나 입힐 때마다 1 증가\n- (수치 x 4)%만큼 적에게 받는 피해량 증가\n- (수치 x 2)%만큼 가하는 피해량이 증가하는 대신 적중 시 입힌 피해량의 (수치 / 2)%만큼 체력 피해를 입음 (이 효과로 흐트러지지 않음)
   źródło: BattleKeywords-a1c971.json :: dataList[id=ObservedPerson].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 30\n- Turn Start: gain 3 Stack (starting from the turn after this unit gained this effect)\n- Gain 1 Stack every time this unit takes or deals damage with an Attack Skill effect against Distorted Hohenheim\n- Take +(Stack x 4)% damage from enemies\n- Deal +(Stack x 2)% damage, but On Hit, take (Stack / 2)% of the damage dealt as HP damage (cannot be Staggered from this effect)
   PL: - Maks. 30\n- Na początku tury rośnie o 3 (od tury po zdobyciu)\n- Rośnie o 1 za każde otrzymanie lub zadanie obrażeń efektem Umiejętności ataku wobec Wykrzywionego Hohenheima\n- Otrzymuje +(stosy x 4)% obrażeń od wrogów\n- Zadaje +(stosy x 2)% obrażeń, ale przy trafieniu otrzymuje (stosy / 2)% zadanych obrażeń jako obrażenia HP (nie powoduje Oszołomienia)
438. [Słowo kluczowe [BloodthirstHard] — nazwa] 피갈망
   źródło: BattleKeywords-a1c971.json :: dataList[id=BloodthirstHard].name
   kontekst: identyfikator tagu w tekstach: `[BloodthirstHard]`
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Słowo kluczowe [BloodthirstHard] — opis] - 기본 공격 레벨 25 감소\n- 기본 방어 레벨 25 감소
   źródło: BattleKeywords-a1c971.json :: dataList[id=BloodthirstHard].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level -25\n- Base Defense Level -25
   PL: - Podstawowy Poziom Ataku -25\n- Podstawowy Poziom Obrony -25

## Słowa kluczowe bitwy — BattleKeywords-a1c9p1
- plik gry: `BattleKeywords-a1c9p1.json` (opisy wyświetlane w dymkach pomocy podczas walki)

440. [Słowo kluczowe [MuscleContraction] — nazwa] 근섬유의 기계적 수축과 이완
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=MuscleContraction].name
   kontekst: identyfikator tagu w tekstach: `[MuscleContraction]`
   limit: do 40 znaków
   EN: Automated Myofiber Activity
   PL: Automatyczna Praca Włókien Mięśniowych
441. [Słowo kluczowe [MuscleContraction] — opis] 최댓값: 2\n수치 당 피해량 +15%\n수치가 2일경우, 전투 시작 시 자신이 사용하는 공격 스킬의 모든 코인이 파괴 불가 코인으로 변경됨.\n공격 종료 시 버프 소멸
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=MuscleContraction].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Deal +15% damage per Stack\n- Combat Start: At 2 Stacks, convert all Coins of this unit's Attack Skills into Unbreakable Coins.\n- Attack End: Lose this effect
   PL: - Maks. 2 stosów\n- Zadaje +15% obrażeń za każdy stos\n- Na początku walki przy 2 stosach wszystkie Monety Umiejętności ataku tej jednostki stają się Niezniszczalnymi Monetami.\n- Po zakończeniu ataku traci efekt
442. [Słowo kluczowe [DuelEdge] — nazwa] 결투 고조
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=DuelEdge].name
   kontekst: identyfikator tagu w tekstach: `[DuelEdge]`
   limit: do 40 znaków
   EN: The Duel Escalates
   PL: Eskalacja Pojedynku
443. [Słowo kluczowe [DuelEdge] — opis] - 최댓값: 20\n- '엄지 제자 - 루치오'와 합을 진행할 시 '엄지 제자 - 루치오'의 스킬 위력과 피해량 증가\n- 매 턴마다 '엄지 제자 - 루치오'와 합을 하지 않으면 턴 종료 시 소멸
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=DuelEdge].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 20\n- 'The Thumb Apprentice - Lucio' gains Skill Power and deals more damage with every Clash with this unit\n- Expires at Turn End if this unit did not Clash with 'The Thumb Apprentice - Lucio' this turn
   PL: - Maks. wartości: 20\n- W Starciu z „Uczniem Kciuka - Lucio” Umiejętności tego wroga zyskują Siłę i zadają więcej obrażeń\n- Znika na koniec tury, jeżeli w tej turze nie odbyło się Starcie z „Uczniem Kciuka - Lucio"
444. [Słowo kluczowe [HostageCharon] — nazwa] 인질극
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HostageCharon].name
   kontekst: identyfikator tagu w tekstach: `[HostageCharon]`
   limit: do 40 znaków
   EN: Hostage Situation
   PL: Wzięcie Zakładnika
445. [Słowo kluczowe [HostageCharon] — opis] - '엄지 제자 - 루치오'와 합을 진행할 시 합 위력 -1\n- '엄지 제자 - 루치오'에게 가하는 피해량 -20%
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HostageCharon].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When Clashing with 'The Thumb Apprentice - Lucio', Clash Power -1\n- Deal -20% damage to 'The Thumb Apprentice - Lucio'
   PL: - W Starciu z „Uczniem Kciuka - Lucio” Moc Starcia -1\n- Zadaje -20% obrażeń „Uczniowi Kciuka - Lucio"
446. [Słowo kluczowe [SeveredTendon] — nazwa] 힘줄 절단
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=SeveredTendon].name
   kontekst: identyfikator tagu w tekstach: `[SeveredTendon]`
   limit: do 40 znaków
   EN: Severed Tendon
   PL: Przecięte Ścięgno
447. [Słowo kluczowe [SeveredTendon] — opis] - 최댓값 3\n- 수치 1당 기본 공격 스킬의 기본 위력 -1\n- 턴 종료 시 1 감소
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=SeveredTendon].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Base Attack Skill Base Power -1 for every Stack\n- Turn End: Lose 1 Stack
   PL: - Maks. 3 stosów\n- Podstawowa Siła podstawowej Umiejętności ataku -1 za każdy stos\n- Na koniec tury traci 1 stos
448. [Słowo kluczowe [HowDareYouApple] — nazwa] 감히…!
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HowDareYouApple].name
   kontekst: identyfikator tagu w tekstach: `[HowDareYouApple]`
   limit: do 40 znaków
   EN: The Audacity...!
   PL: Zuchwałość...!
449. [Słowo kluczowe [HowDareYouApple] — opis] - 최댓값: 4\n- 수치당 피해량 +20%\n- 특정 스킬 사용시 소모됨
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HowDareYouApple].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Deal +20% damage for every Stack\n- Consumed when using certain Skills
   PL: - Maks. stosów: 4\n- Zadaje +20% obrażeń za każdy stos\n- Zużywane przy użyciu określonych Umiejętności
450. [Słowo kluczowe [RapidGrowthApple] — nazwa] 급한 성장
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RapidGrowthApple].name
   kontekst: identyfikator tagu w tekstach: `[RapidGrowthApple]`
   limit: do 40 znaków
   EN: Rapid Growth
   PL: Przyspieszony Wzrost
451. [Słowo kluczowe [RapidGrowthApple] — opis] - 최댓값: 3\n- 수치당 부위의 방어 레벨 1 감소 (최소 방어 레벨 1)\n- 팔 부위 전부 파괴 시 소멸
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RapidGrowthApple].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Lose 1 Defense Level for every Stack; minimum Defense Level due to this effect: 1\n- Lose this effect when all Arms are broken
   PL: - Maks. stosów: 3\n- Poziom Obrony części maleje o 1 za każdy stos (min. Poziom Obrony 1)\n- Znika po zniszczeniu wszystkich części Ramion
452. [Słowo kluczowe [HumanFleshTheRings] — nazwa] 생체 재료
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HumanFleshTheRings].name
   kontekst: identyfikator tagu w tekstach: `[HumanFleshTheRings]`
   limit: do 40 znaków
   EN: Corpus Ingredient
   PL: Materiał Biologiczny
453. [Słowo kluczowe [HumanFleshTheRings] — opis] - 최댓값: 2\n- 특수 충전 (위력 고정)
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=HumanFleshTheRings].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 2\n- Unique Charge (fixed Potency)
   PL: - Maks. stosów: 2\n- Specjalny Ładunek (Siła zablokowana)
454. [Słowo kluczowe [BoneBladeTheRings] — nazwa] 작품명: 파시아
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BoneBladeTheRings].name
   kontekst: identyfikator tagu w tekstach: `[BoneBladeTheRings]`
   limit: do 40 znaków
   EN: Artwork: Fascia
   PL: Tytuł dzieła: Fascia
455. [Słowo kluczowe [BoneBladeTheRings] — opis] - 턴 시작 시, 기본 위력 증가 4 얻음\n- 공격 스킬로 출혈 부여 시, 출혈 위력 2 추가 부여
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BoneBladeTheRings].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Base Power Up\n- When inflicting Bleed with Attack Skills, inflict additional 2 Bleed Potency
   PL: - Na początku tury zyskuje 4 Wzrostu Mocy Bazowej\n- Nakładając Krwawienie Umiejętnościami ataku, nakłada dodatkowo 2 Siły Krwawienia
456. [Słowo kluczowe [UnsteadyTheRings] — nazwa] 심하게 울리는 갑주
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=UnsteadyTheRings].name
   kontekst: identyfikator tagu w tekstach: `[UnsteadyTheRings]`
   limit: do 40 znaków
   EN: Impact-rattled Armor
   PL: Rozkołysana Zbroja
457. [Słowo kluczowe [UnsteadyTheRings] — opis] - 최댓값: 3\n- ‘억압당한 육체’ 사용 시 수치 1당, 최종 위력 10 감소\n- ‘억압당한 육체’ 공격 종료 후 수치가 3이면, 효과 소멸하고 다음 턴까지 흐트러짐 상태가 됨
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=UnsteadyTheRings].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- When using 'Repressed Flesh', lose 10 Final Power for every Stack\n- At 3 Stacks after using 'Repressed Flesh', lose this effect and become Staggered until next turn
   PL: - Maks. stosów: 3\n- Przy użyciu „Uciskanego Ciała” traci 10 Mocy Końcowej za każdy stos\n- Jeżeli po zakończeniu ataku „Uciskanego Ciała” wartość wynosi 3, efekt znika, a jednostka pozostaje w stanie Oszołomienia do następnej tury
458. [Słowo kluczowe [IronMaiden_LowMorale] — nazwa] 아이언 메이든
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[IronMaiden_LowMorale]`
   limit: do 40 znaków
   EN: Iron Maiden
   PL: Iron Maiden
459. [Słowo kluczowe [IronMaiden_LowMorale] — opis] - 사기 저하\n- 턴 시작 시, 공격 레벨 감소 1, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Turn Start: Gain 1 Offense Level Down and 1 Defense Level Up
   PL: - Niskie Morale\n- Na początku tury zyskuje 1 Spadek Poziomu Ataku i 1 Wzrost Poziomu Obrony
460. [Słowo kluczowe [IronMaiden_LowMorale] — podsumowanie] 턴 시작 시, 공격 레벨 감소 1, 방어 레벨 증가 1 얻음
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_LowMorale].summary
   limit: do 120 znaków
   EN: Turn Start: Gain 1 Offense Level Down and 1 Defense Level Up
   PL: Na początku tury zyskuje 1 Spadek Poziomu Ataku i 1 Wzrost Poziomu Obrony
461. [Słowo kluczowe [IronMaiden_Panic] — nazwa] 아이언 메이든
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_Panic].name
   kontekst: identyfikator tagu w tekstach: `[IronMaiden_Panic]`
   (powtórzenie elementu 458 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
462. [Słowo kluczowe [IronMaiden_Panic] — opis] - 패닉\n- 턴 시작 시, 공격 레벨 감소 2, 방어 레벨 증가 2 얻음
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Turn Start: Gain 2 Offense Level Down and 2 Defense Level Up
   PL: - Panika\n- Na początku tury zyskuje 2 Spadku Poziomu Ataku i 2 Wzrost Poziomu Obrony
463. [Słowo kluczowe [IronMaiden_Panic] — podsumowanie] 턴 시작 시, 공격 레벨 감소 2, 방어 레벨 증가 2 얻음
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IronMaiden_Panic].summary
   limit: do 120 znaków
   EN: Turn Start: Gain 2 Offense Level Down and 2 Defense Level Up
   PL: Na początku tury zyskuje 2 Spadku Poziomu Ataku i 2 Wzrost Poziomu Obrony
464. [Słowo kluczowe [DicipleLittleFinger] — nazwa] 월하청도
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=DicipleLittleFinger].name
   kontekst: identyfikator tagu w tekstach: `[DicipleLittleFinger]`
   limit: do 40 znaków
   EN: Moonlit Azure Blade
   PL: Błękitne Ostrze w Blasku Księżyca
465. [Słowo kluczowe [DicipleLittleFinger] — opis] - 최댓값 : 50\n- 턴 시작시 수치 1당 보호막 5 얻음\n- 수치 1당 자신의 크리티컬 피해량 +1%\n- 피격 시 수치 1 감소
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=DicipleLittleFinger].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 50\n- Turn Start: Gain 5 Shield for every Stack\n- +1% Damage on Critical Hit for every Stack\n- Lose 1 Stack when hit
   PL: - Maks. stosów: 50\n- Na początku tury zyskuje 5 Tarczy za każdy stos\n- +1% obrażeń Krytycznych za każdy stos\n- Przy trafieniu traci 1 stos
466. [Słowo kluczowe [RyoshuSlotPlusA1C9] — nazwa] 과거의 악취
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuSlotPlusA1C9]`
   limit: do 40 znaków
   EN: Stench of Times Past
   PL: Smród Przeszłości
467. [Słowo kluczowe [RyoshuSlotPlusA1C9] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)\n- Wycofanie niemożliwe
468. [Słowo kluczowe [RyoshuSlotPlusA1C9] — podsumowanie] 거미집 소속 적에게 가하는 피해량 증가
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RyoshuSlotPlusA1C9].summary
   limit: do 120 znaków
   EN: Deal more damage to The House of Spiders enemies
   PL: Zadaje więcej obrażeń wrogom z Domu Pajęczyn
469. [Słowo kluczowe [ObservationMoses] — nazwa] 관찰력
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=ObservationMoses].name
   kontekst: identyfikator tagu w tekstach: `[ObservationMoses]`
   limit: do 40 znaków
   EN: Keen Observation
   PL: Spostrzegawczość
470. [Słowo kluczowe [ObservationMoses] — opis] - 매혹 대상이 되지 않음\n- 요정 부위에 가하는 피해량 +25%
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=ObservationMoses].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Cannot be targeted for Charmed\n- Deal +25% damage to Fairy
   PL: - Nie może być celem Zauroczenia\n- Zadaje +25% obrażeń Wróżce
471. [Słowo kluczowe [CalmAnalysisMoses] — nazwa] 차분한 분석
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=CalmAnalysisMoses].name
   kontekst: identyfikator tagu w tekstach: `[CalmAnalysisMoses]`
   limit: do 40 znaków
   EN: Untroubled Analysis
   PL: Spokojna Analiza
472. [Słowo kluczowe [CalmAnalysisMoses] — opis] - 요정 초롱에게 가하는 피해량 +25%
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=CalmAnalysisMoses].desc
   limit: do 120 znaków
   EN: - Deal +25% damage to Faelantern
   PL: - Zadaje +25% obrażeń Faelantern
473. [Słowo kluczowe [TeachersCommand] — nazwa] 엄지 아비의 명령
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=TeachersCommand].name
   kontekst: identyfikator tagu w tekstach: `[TeachersCommand]`
   limit: do 50 znaków
   EN: The Thumb Nursefather's Command
   PL: Rozkaz Ojca Kciuka
474. [Słowo kluczowe [TeachersCommand] — opis] - 공격 레벨 5 감소
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=TeachersCommand].desc
   limit: do 120 znaków
   EN: - Lose 5 Offense Levels
   PL: - Traci 5 Poziomów Ataku
475. [Słowo kluczowe [RyoshuStartA1C9] — nazwa] 되살아나는 희열
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RyoshuStartA1C9].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuStartA1C9]`
   limit: do 40 znaków
   EN: Rekindled Exhilaration
   PL: Odrodzona Euforia
476. [Słowo kluczowe [RyoshuStartA1C9] — opis] - 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=RyoshuStartA1C9].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)
   PL: - Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)
477. [Słowo kluczowe [BreathLoss_LowMorale] — nazwa] 흐트러진 숨
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BreathLoss_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BreathLoss_LowMorale]`
   limit: do 40 znaków
   EN: Ragged Breath
   PL: Urywany Oddech
478. [Słowo kluczowe [BreathLoss_LowMorale] — opis] 턴 시작시 자신의 호흡 위력 3 감소
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BreathLoss_LowMorale].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 3 Poise Potency
   PL: Na początku tury traci 3 Siły Oddechu
479. [Słowo kluczowe [BreathLoss_Panic] — nazwa] 흐트러진 숨
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BreathLoss_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BreathLoss_Panic]`
   (powtórzenie elementu 477 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Słowo kluczowe [BreathLoss_Panic] — opis] 턴 시작시 자신의 호흡 위력 5 감소
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BreathLoss_Panic].desc
   limit: do 120 znaków
   EN: Turn Start: Lose 5 Poise Potency
   PL: Na początku tury traci 5 Siły Oddechu
481. [Słowo kluczowe [IndexPrescriptTargetMarkToEnemy] — nazwa] 지령 표식
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptTargetMarkToEnemy].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptTargetMarkToEnemy]`
   limit: do 40 znaków
   EN: Mark of the Prescript
   PL: Znak Nakazu
482. [Słowo kluczowe [IndexPrescriptTargetMarkToEnemy] — opis] - 조작 슬롯에 배치된 기본 공격 스킬 중 하나에 지령 표식이 새겨짐
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptTargetMarkToEnemy].desc
   limit: do 120 znaków
   EN: - Apply Mark of the Prescript to a Base Attack Skill on this unit's Dashboard
   PL: - Nakłada Znak Nakazu na jedną podstawową Umiejętność ataku na Panelu dowodzenia tej jednostki
483. [Słowo kluczowe [IndexPrescriptTargetToEnemy] — nazwa] 지령 대상
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptTargetToEnemy].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptTargetToEnemy]`
   limit: do 40 znaków
   EN: The Prescript's Target
   PL: Cel Nakazu
484. [Słowo kluczowe [IndexPrescriptTargetToEnemy] — opis] - 검지 소속에게 받는 피해 +10%\n- 검지 소속 인격 수와 상관없이 매 턴마다 하나의 대상에게만 적용됨
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptTargetToEnemy].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Take +10% damage from The Index units\n- This effect is applied to a single target every turn regardless of the number of The Index units deployed
   PL: - Otrzymuje +10% obrażeń od jednostek Wskazującego\n- Niezależnie od liczby Tożsamości Wskazującego efekt nakładany jest co turę tylko na jeden cel
485. [Słowo kluczowe [BlessingOfIndexPrescriptAlly] — nazwa] 지령의 가호
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BlessingOfIndexPrescriptAlly].name
   kontekst: identyfikator tagu w tekstach: `[BlessingOfIndexPrescriptAlly]`
   limit: do 40 znaków
   EN: Grace of the Prescript
   PL: Łaska Nakazu
486. [Słowo kluczowe [BlessingOfIndexPrescriptAlly] — opis] - 수치 3당 공격 레벨 +1\n- 최대 9
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=BlessingOfIndexPrescriptAlly].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1 for every 3 Stacks\n- Max Stack: 9
   PL: - Poziom Ataku +1 za każde 3 stosy\n- Maks. 9
487. [Słowo kluczowe [IndexPrescript_Base] — nazwa] 지령
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescript_Base].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescript_Base]`
   limit: do 40 znaków
   EN: Prescript
   PL: Nakaz
488. [Słowo kluczowe [IndexPrescript_Base] — opis] - 특정 조건에 따라 지령[쪽지]가 주어짐
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescript_Base].desc
   limit: do 120 znaków
   EN: - Receive 'Prescript: [Paper Slip]' under specific conditions
   PL: - Zgodnie z określonymi warunkami otrzymuje Nakaz [Kartka]
489. [Słowo kluczowe [IndexPrescript_Base] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescript_Base].flavor
   limit: do 220 znaków
   EN: The Prescripts are delivered by many means, their medium determined with finality akin to divine prophecy. Those who receive them hold no power over how they arrive.
   PL: Nakazy przekazywane są na wiele sposobów — ich forma jest wybierana jednostronnie, niczym wyrocznia.
490. [Słowo kluczowe [IndexPrescriptFaust_0] — nazwa] 지령[쪽지] I
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptFaust_0]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] I
   PL: Nakaz [Kartka] I
491. [Słowo kluczowe [IndexPrescriptFaust_0] — opis] 지령 표식이 새겨진 스킬을 사용하거나 적중한다.\n\n- 턴 시작 시 지령의 가호가 0~2일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a Skill marked with Mark of the Prescript or hit a target with a marked Skill.\n\n- Turn Start: At 0~2 Grace of the Prescript, gain this effect \n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Używa Umiejętności oznaczonej Znakiem Nakazu lub trafia nią cel.\n\n- Na początku tury zdobywany przy Łasce Nakazu 0–2\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
492. [Słowo kluczowe [IndexPrescriptFaust_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_0].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
493. [Słowo kluczowe [IndexPrescriptFaust_1] — nazwa] 지령[쪽지] II
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptFaust_1]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] II
   PL: Nakaz [Kartka] II
494. [Słowo kluczowe [IndexPrescriptFaust_1] — opis] 지령 표식이 새겨진 스킬이 적중한다.\n\n- 턴 시작 시 지령의 가호가 3~5일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with a Skill marked with Mark of the Prescript.\n\n- Turn Start: At 3~5 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Umiejętność oznaczona Znakiem Nakazu trafia cel.\n\n- Na początku tury zdobywany przy Łasce Nakazu 3–5\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
495. [Słowo kluczowe [IndexPrescriptFaust_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_1].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
496. [Słowo kluczowe [IndexPrescriptFaust_2] — nazwa] 지령[쪽지] III
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptFaust_2]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] III
   PL: Nakaz [Kartka] III
497. [Słowo kluczowe [IndexPrescriptFaust_2] — opis] E.G.O 각성 스킬 또는 지령 표식이 새겨진 ‘스킬 3’이 적중한다.\n\n- 턴 시작 시 지령의 가호가 6~8일 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with E.G.O Awakening Skill or 'Skill 3' marked with Mark of the Prescript.\n\n- Turn Start: At 6~8 Grace of the Prescript, gain this effect\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Trafia cel Umiejętność Przebudzenia E.G.O lub „Umiejętność 3” oznaczona Znakiem Nakazu.\n\n- Na początku tury zdobywany przy Łasce Nakazu 6–8\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
498. [Słowo kluczowe [IndexPrescriptFaust_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_2].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
499. [Słowo kluczowe [IndexPrescriptFaust_3] — nazwa] 지령[쪽지] IV
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptFaust_3]`
   limit: do 40 znaków
   EN: Prescript: [Paper Slip] IV
   PL: Nakaz [Kartka] IV
500. [Słowo kluczowe [IndexPrescriptFaust_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 지령의 가호가 9일 때 얻음
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: At 9 Grace of the Prescript, gain this effect
   PL: Wyeliminuj wszystkich wrogów, zanim przyjdzie kolejny Nakaz.\n\n- Na początku tury zdobywany przy Łasce Nakazu 9
501. [Słowo kluczowe [IndexPrescriptFaust_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=IndexPrescriptFaust_3].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Słowo kluczowe [KarmaOfIndexAlly] — nazwa] 카르마
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].name
   kontekst: identyfikator tagu w tekstach: `[KarmaOfIndexAlly]`
   limit: do 40 znaków
   EN: Karmic Consequence
   PL: Karma
503. [Słowo kluczowe [KarmaOfIndexAlly] — opis] - 턴 시작 시,\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury,\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Maks. 100 stosów
504. [Słowo kluczowe [KarmaOfIndexAlly] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: BattleKeywords-a1c9p1.json :: dataList[id=KarmaOfIndexAlly].flavor
   limit: do 200 znaków
   EN: Receive the Prescript and undertake it. Its execution is etched as karma, drawn into a ceaseless cycle that circles back to the hand of its executor.
   PL: Otrzymaj Nakaz i wykonaj go. To staje się karmą, która krąży i nieuchronnie się kumuluje.

## Słowa kluczowe bitwy — BattleKeywords-a1c9p2
- plik gry: `BattleKeywords-a1c9p2.json` (opisy wyświetlane w dymkach pomocy podczas walki)

505. [Słowo kluczowe [IndexPrescriptTargetToPersonality] — nazwa] 검지의 지령 대상
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptTargetToPersonality].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptTargetToPersonality]`
   limit: do 50 znaków
   EN: The Prescript's Target - The Index
   PL: Cel Nakazu - Wskazujący
506. [Słowo kluczowe [IndexPrescriptTargetToPersonality] — opis] 검지 소속 적에게 사용하는 스킬 위력 -2, 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptTargetToPersonality].desc
   limit: do 120 znaków
   EN: Skill Power -2 against and take +20% damage from The Index enemies
   PL: Siła Umiejętności -2 i otrzymuje +20% obrażeń od wrogów Wskazującego
507. [Słowo kluczowe [BlessingOfIndexPrescriptEnemy] — nazwa] 지령의 가호
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlessingOfIndexPrescriptEnemy].name
   kontekst: identyfikator tagu w tekstach: `[BlessingOfIndexPrescriptEnemy]`
   (powtórzenie elementu 485 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Słowo kluczowe [BlessingOfIndexPrescriptEnemy] — opis] - 수치 3당 공격 레벨 +1\n- 최대 9
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlessingOfIndexPrescriptEnemy].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1 for every 3 Stack\n- Max Stack: 9
   PL: - Poziom Ataku +1 za każde 3 stosy\n- Maks. 9
509. [Słowo kluczowe [IndexPrescript_Base_2nd] — nazwa] 지령
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescript_Base_2nd]`
   (powtórzenie elementu 487 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Słowo kluczowe [IndexPrescript_Base_2nd] — opis] 특정 조건에 따라 지령[단말기]가 주어짐
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].desc
   limit: do 120 znaków
   EN: Receive Prescript: [Device] under specific conditions
   PL: Zgodnie z określonymi warunkami otrzymuje Nakaz [Urządzenie]
511. [Słowo kluczowe [IndexPrescript_Base_2nd] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescript_Base_2nd].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
512. [Słowo kluczowe [IndexPrescriptStudent_0] — nazwa] 지령[단말기] I
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptStudent_0]`
   limit: do 40 znaków
   EN: Prescript: [Device] I
   PL: Nakaz [Urządzenie] I
513. [Słowo kluczowe [IndexPrescriptStudent_0] — opis] 지령 대상을 공격하여 적중한다.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Attack and hit a Prescript's Target.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Atakuje Cel Nakazu i trafia.\n\n- Na początku tury zdobywany przy braku Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
514. [Słowo kluczowe [IndexPrescriptStudent_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_0].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Słowo kluczowe [IndexPrescriptStudent_1] — nazwa] 지령[단말기] II
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptStudent_1]`
   limit: do 40 znaków
   EN: Prescript: [Device] II
   PL: Nakaz [Urządzenie] II
516. [Słowo kluczowe [IndexPrescriptStudent_1] — opis] 지령 대상에게 첫 번째 슬롯에 장착된 스킬이 적중한다. 또는 무작위 상대를 처치한다.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a Prescript's Target with the Skill equipped in the first Slot, or eliminate a random target.\n\n- Turn Start: Gain this effect if this unit has Unlock - I\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Cel Nakazu trafiają Umiejętność z pierwszego slotu lub losowy cel zostaje zabity.\n\n- Na początku tury zdobywany przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
517. [Słowo kluczowe [IndexPrescriptStudent_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_1].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
518. [Słowo kluczowe [IndexPrescriptStudent_2] — nazwa] 지령[단말기] III
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptStudent_2]`
   limit: do 40 znaków
   EN: Prescript: [Device] III
   PL: Nakaz [Urządzenie] III
519. [Słowo kluczowe [IndexPrescriptStudent_2] — opis] 무작위 상대를 흐트러뜨리거나 처치한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stagger or eliminate a random target.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Oszłamia lub zabija losowy cel.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
520. [Słowo kluczowe [IndexPrescriptStudent_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_2].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
521. [Słowo kluczowe [IndexPrescriptStudent_3] — nazwa] 지령[단말기] IV
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptStudent_3]`
   limit: do 40 znaków
   EN: Prescript: [Device] IV
   PL: Nakaz [Urządzenie] IV
522. [Słowo kluczowe [IndexPrescriptStudent_3] — opis] 모든 방해물을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all obstacles before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Wyeliminuj wszystkie przeszkody, zanim przyjdzie kolejny Nakaz.\n\n- Na początku tury zdobywany przy Odblokowaniu - III
523. [Słowo kluczowe [IndexPrescriptStudent_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptStudent_3].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
524. [Słowo kluczowe [UnlockBuff_1] — nazwa] 해금 - I
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_1].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_1]`
   limit: do 40 znaków
   EN: Unlock - I
   PL: Odblokowanie - I
525. [Słowo kluczowe [UnlockBuff_1] — opis] - 공격 레벨 +1, 방어 레벨 +1\n- 전투 종료 시, 정신력 15 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +1, Defense Level +1\n- Combat End: Heal 15 SP
   PL: - Poziom Ataku +1, Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 15 Poczytalności
526. [Słowo kluczowe [UnlockBuff_2] — nazwa] 해금 - II
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_2].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_2]`
   limit: do 40 znaków
   EN: Unlock - II
   PL: Odblokowanie - II
527. [Słowo kluczowe [UnlockBuff_2] — opis] - 공격 레벨 +2, 방어 레벨 +2\n- 전투 종료 시, 정신력 30 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +2, Defense Level +2\n- Combat End: Heal 30 SP
   PL: - Poziom Ataku +2, Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 30 Poczytalności
528. [Słowo kluczowe [UnlockBuff_3] — nazwa] 해금 - III
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_3].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_3]`
   limit: do 40 znaków
   EN: Unlock - III
   PL: Odblokowanie - III
529. [Słowo kluczowe [UnlockBuff_3] — opis] - 공격 레벨 +3, 방어 레벨 +3\n- 전투 종료 시, 정신력 45 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Offense Level +3, Defense Level +3\n- Combat End: Heal 45 SP
   PL: - Poziom Ataku +3, Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 45 Poczytalności
530. [Słowo kluczowe [KarmaOfIndexStudent] — nazwa] 카르마
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].name
   kontekst: identyfikator tagu w tekstach: `[KarmaOfIndexStudent]`
   (powtórzenie elementu 502 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
531. [Słowo kluczowe [KarmaOfIndexStudent] — opis] - 턴 시작 시\n· 수치 10당 방어 레벨 감소 1 얻음\n· 수치 20당 취약 1 얻음\n- 최대 100
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start:\n· Gain 1 Defense Level Down for every 10 Stacks\n· Gain 1 Fragile for every 20 Stacks\n- Max Stack: 100
   PL: - Na początku tury\n· Zyskuje 1 Spadek Poziomu Obrony za każde 10 stosów\n· Zyskuje 1 Wrażliwości za każde 20 stosów\n- Maks. 100 stosów
532. [Słowo kluczowe [KarmaOfIndexStudent] — tekst klimatyczny] 지령을 받고, 수행한다. 그것은 하나의 업이 되어, 돌고 돌아 축적되기 마련.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=KarmaOfIndexStudent].flavor
   (powtórzenie elementu 504 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
533. [Słowo kluczowe [Blandishment_Enemy] — nazwa] 당연한 믿음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Enemy].name
   kontekst: identyfikator tagu w tekstach: `[Blandishment_Enemy]`
   limit: do 40 znaków
   EN: Faith Beyond Question
   PL: Wiara Ponad Wątpliwość
534. [Słowo kluczowe [Blandishment_Enemy] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +3, 방어 레벨 +3\n- 스킬로 획득하는 호흡 위력 +1
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Enemy].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +3, Defense Level +3\n- Gain +1 more Poise Potency from Skills
   PL: - Min. i Maks. Szybkość +1\n- Poziom Ataku +3, Poziom Obrony +3\n- Umiejętności zyskują +1 więcej Siły Oddechu
535. [Słowo kluczowe [Blandishment_Enemy] — tekst klimatyczny] “다, 당연한 것 아닌가요? 삐삐가 전해주는 말들은 당연히… 다, 당연한 거잖아요?”
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Enemy].flavor
   limit: do 140 znaków
   EN: "Isn't... Isn't it self-evident? Each word that the beeper grants is unquestionably... b-beyond question."
   PL: „Cz-czy to nie oczywiste? Każde słowo, które przynosi beeper, jest bezdyskusyjnie... b-bez dyskusji.”
536. [Słowo kluczowe [Blandishment_Shin_Enemy] — nazwa] 신(心) - 소라
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Shin_Enemy].name
   kontekst: identyfikator tagu w tekstach: `[Blandishment_Shin_Enemy]`
   limit: do 40 znaków
   EN: Shin (心) - Sora
   PL: Shin (心) - Sora
537. [Słowo kluczowe [Blandishment_Shin_Enemy] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +2, 방어 레벨 +2\n- 스킬로 획득하는 호흡 위력과 횟수 +1\n- 가하는 피해량 +(25+잃은 체력 비율)% (최대 100%)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Shin_Enemy].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +2, Defense Level +2\n- Gain +1 more Poise Potency and Poise Count from Skills\n- Deal +(missing HP percentage + 25)% damage (max 100%)
   PL: - Min. i Maks. Szybkość +1\n- Poziom Ataku +2, Poziom Obrony +2\n- Umiejętności zyskują +1 więcej Siły Oddechu i Licznika Oddechu\n- Zadaje +(25 + procent brakującego HP)% obrażeń (maks. 100%)
538. [Słowo kluczowe [PressureOfPrescript] — nazwa] 압박감
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PressureOfPrescript].name
   kontekst: identyfikator tagu w tekstach: `[PressureOfPrescript]`
   limit: do 40 znaków
   EN: Onus
   PL: Nacisk
539. [Słowo kluczowe [PressureOfPrescript] — opis] - 수치 1당 가하는 피해량 +25% (최대 50%)\n- 개화 E.G.O::대행 상태면,\n· 수치가 1일 때, 최종 위력 +1\n· 수치가 2일 때, 대신 최종 위력 +3\n- 최대 2
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PressureOfPrescript].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +25% damage for every Stack (max 50%)\n- Under Effloresced E.G.O::Procuration state:\n· At 1 Stack, Final Power +1\n· At 2 Stack, Final Power +3 instead\n- Max Stack: 2
   PL: - Zadaje +25% obrażeń za każdy stos (maks. 50%)\n- W stanie Rozkwitu E.G.O::Procuration,\n· Przy 1 stosie Moc Końcowa +1\n· Przy 2 stosach zamiast tego Moc Końcowa +3\n- Maks. 2
540. [Słowo kluczowe [PressureOfPrescript] — tekst klimatyczny] ‘어,어떡하지. 당연한 건 당연히 수행되어야만 하는데….’
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PressureOfPrescript].flavor
   limit: do 120 znaków
   EN: 'W-what should I do? What is unquestionable must be carried out unquestionably...'
   PL: „C-co robić? To, co oczywiste, musi być wykonane bezdyskusyjnie…”
541. [Słowo kluczowe [PressureOfPrescript_2nd] — nazwa] 극심한 압박감
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PressureOfPrescript_2nd].name
   kontekst: identyfikator tagu w tekstach: `[PressureOfPrescript_2nd]`
   limit: do 40 znaków
   EN: Extreme Onus
   PL: Ekstremalny Nacisk
542. [Słowo kluczowe [PressureOfPrescript_2nd] — opis] - 수치 1당 가하는 피해량 +50% (최대 100%)\n- 개화 E.G.O::대행 상태면,\n· 수치가 1일 때, 최종 위력 +2\n· 수치가 2일 때, 대신 더하기 코인 위력 +1, 최종 위력 +3\n- 최대 2\n- 특정 스킬 사용 시, 압박감과 동일하게 취급되어 소모됨
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PressureOfPrescript_2nd].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Deal +50% damage for every Stack (max 100%)\n- Under Effloresced E.G.O::Procuration state:\n· At 1 Stack, Final Power +2\n· At 2 Stack, Plus Coin Power +1 and Final Power +3 instead\n- Max Stack: 2\n- When using certain Skills, counts as Onus and is consumed
   PL: - Zadaje +50% obrażeń za każdy stos (maks. 100%)\n- W stanie Rozkwitu E.G.O::Procuration,\n· Przy 1 stosie Moc Końcowa +2\n· Przy 2 stosach zamiast tego Moc Monety Plus +1 i Moc Końcowa +3\n- Maks. 2\n- Przy użyciu określonych Umiejętności traktowana jak Nacisk i zużywana
543. [Słowo kluczowe [BlindFaith_LowMorale] — nazwa] 지령 붕괴 위기
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlindFaith_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[BlindFaith_LowMorale]`
   limit: do 40 znaków
   EN: Prescript Incompliance Risk
   PL: Ryzyko Odrzucenia Nakazu
544. [Słowo kluczowe [BlindFaith_LowMorale] — opis] - 사기저하\n- 지령 대상에게 가하는 피해량 +20%\n지령 대상이 아닌 대상에게 받는 피해량 +10%
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlindFaith_LowMorale].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Deal +20% damage to targets that have The Prescript's Target\n- Take +10% damage from targets that do not have The Prescript's Target
   PL: - Niskie Morale\n- Zadaje +20% obrażeń celom z Celem Nakazu\nOtrzymuje +10% obrażeń od celów bez Celu Nakazu
545. [Słowo kluczowe [BlindFaith_Panic] — nazwa] 지령 붕괴 위기
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlindFaith_Panic].name
   kontekst: identyfikator tagu w tekstach: `[BlindFaith_Panic]`
   (powtórzenie elementu 543 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
546. [Słowo kluczowe [BlindFaith_Panic] — opis] - 패닉\n- 지령 대상에게 가하는 피해량 +30%\n지령 대상이 아닌 대상에게 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BlindFaith_Panic].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Deal +30% damage to targets that have The Prescript's Target\n- Take +20% damage from targets that do not have The Prescript's Target
   PL: - Panika\n- Zadaje +30% obrażeń celom z Celem Nakazu\nOtrzymuje +20% obrażeń od celów bez Celu Nakazu
547. [Słowo kluczowe [YellowHarpoon] — nazwa] 노란작살
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=YellowHarpoon].name
   kontekst: identyfikator tagu w tekstach: `[YellowHarpoon]`
   limit: do 40 znaków
   EN: The Yellow Harpoon
   PL: Żółty Harpun
548. [Słowo kluczowe [YellowHarpoon] — opis] - 턴 시작시, 신속 4, 호흡 8 얻음\n- 턴 종료시 박힌 작살을 보유한 적이 있으면, 호흡 횟수 3 증가
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=YellowHarpoon].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: Gain 4 Haste and 8 Poise\n- Turn End: Gain +3 Poise Count if an enemy has Nested Harpoon
   PL: - Na początku tury zyskuje 4 Pośpiechu i 8 Oddechu\n- Na koniec tury, jeżeli jakiś wroga ma Wbity Harpun, zyskuje +3 Licznika Oddechu
549. [Słowo kluczowe [YellowHarpoonSin] — nazwa] 신(心) - 노란작살
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=YellowHarpoonSin].name
   kontekst: identyfikator tagu w tekstach: `[YellowHarpoonSin]`
   limit: do 40 znaków
   EN: Shin(心) - The Yellow Harpoon
   PL: Shin (心) - Żółty Harpun
550. [Słowo kluczowe [YellowHarpoonSin] — opis] - 기본 공격 레벨 +3, 기본 방어 레벨 +3\n- 전 턴에 자신을 공격한 대상 공격 시 정신력 3 회복\n- 자신의 정신력이 0 이상이면, (정신력 / 10)만큼 최종 위력 증가 (소수점 버림)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=YellowHarpoonSin].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Base Offense Level +3, Base Defense Level +3\n- Heal 3 SP when attacking target that attacked this unit last turn\n- At 0+ SP, gain Final Power by (SP / 10) (rounded down)
   PL: - Podstawowy Poziom Ataku +3, Podstawowy Poziom Obrony +3\n- Atakując cel, który w poprzedniej turze ją zaatakował, odzyskuje 3 Poczytalności\n- Przy Poczytalności 0+: Moc Końcowa +(Poczytalność / 10) (zaokr. w dół)
551. [Słowo kluczowe [BeeSting] — nazwa] 박힌 작살 [벌침]
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BeeSting].name
   kontekst: identyfikator tagu w tekstach: `[BeeSting]`
   limit: do 40 znaków
   EN: Nested Harpoon [Beesting]
   PL: Wbity Harpun [Żądło]
552. [Słowo kluczowe [BeeSting] — opis] - 참격 내성 +0.2, 나태 내성 +0.2\n- 턴 종료 시 다음 턴에 속박 2 얻음\n- 공격 적중시 출혈 위력 1 얻음\n- 베스파에게 피격 시 궁니르 공명 2 얻음\n- 효과 제거 시 자신의 출혈 1회 발동
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=BeeSting].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Slash Resist. +0.2, Sloth Resist. +0.2\n- Turn End: Gain 2 Bind next turn\n- On Hit: Gain 1 Bleed Potency\n- When attacked by Vespa, gain 2 Gungnir's Droning\n- Activate Bleed on this unit once when this effect is removed
   PL: - Odporność na Cięcie +0,2, Odporność na Żądzę +0,2\n- Na koniec tury zyskuje 2 Spętań w następnej turze\n- Przy trafieniu zyskuje 1 Siły Krwawienia\n- Przy trafieniu przez Vespę zyskuje 2 Dudnienia Gungnira\n- Po usunięciu efektu wywołuje Krwawienie na tej jednostce 1 raz
553. [Słowo kluczowe [ArtifactBeeSting] — nazwa] 박힌 작살 [말벌침]
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ArtifactBeeSting].name
   kontekst: identyfikator tagu w tekstach: `[ArtifactBeeSting]`
   limit: do 40 znaków
   EN: Nested Harpoon [Waspsting]
   PL: Wbity Harpun [Żądło Osy]
554. [Słowo kluczowe [ArtifactBeeSting] — opis] - 참격 내성 +1, 나태 내성 +1\n- 턴 종료 시 다음 턴에 속박 4 얻음\n- 공격 적중시 출혈 위력 3 얻음\n- 베스파에게 피격 시 궁니르 공명 3 얻음\n- 효과 제거 시 자신의 출혈 2회 발동
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ArtifactBeeSting].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Slash Resist. +1, Sloth Resist. +1\n- Turn End: Gain 4 Bind next turn\n- On Hit: Gain 3 Bleed Potency\n- When attacked by Vespa, gain 3 Gungnir's Droning\n- Activate Bleed on this unit 2 times when this effect is removed
   PL: - Odporność na Cięcie +1, Odporność na Żądzę +1\n- Na koniec tury zyskuje 4 Spętań w następnej turze\n- Przy trafieniu zyskuje 3 Siły Krwawienia\n- Przy trafieniu przez Vespę zyskuje 3 Dudnienia Gungnira\n- Po usunięciu efektu wywołuje Krwawienie na tej jednostce 2 razy
555. [Słowo kluczowe [HornetPoison] — nazwa] 궁니르 공명
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=HornetPoison].name
   kontekst: identyfikator tagu w tekstach: `[HornetPoison]`
   limit: do 40 znaków
   EN: Gungnir's Droning
   PL: Dudnienie Gungnira
556. [Słowo kluczowe [HornetPoison] — opis] - 베스파에게 피격 시 효과 위력만큼 고정 피해를 입음\n- 턴 종료 후 횟수 1 감소 (진동 횟수를 증가시키는 효과를 동일하게 적용받음)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=HornetPoison].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - When attacked by Vespa, take fixed damage equal to this effect's Potency\n- Reduce Count by 1 after Turn End (Interacts the same way as normal Tremor does to effects that raise Tremor Count)
   PL: - Przy trafieniu przez Vespę otrzymuje obrażenia stałe równe Siłe tego efektu\n- Po zakończeniu tury traci 1 Licznika (Działa tak samo jak zwykły Wstrząs wobec efektów zwiększających Licznik Wstrząsu)
557. [Słowo kluczowe [HornetPoison] — tekst klimatyczny] <color=#fde55d>이 작살에 박힌 상대는 공격받을수록 강해지는 떨림으로 인해 붕괴된다.</color>
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=HornetPoison].flavor
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>
   EN: <color=#fde55d>Those impaled by the harpoon are pulverized as successive strikes amplify its vibrating force.</color>
   PL: <color=#fde55d>Wbięty przez ten harpun rozpada się, gdy kolejne uderzenia wzmacniają jego siłę drgań.</color>
558. [Słowo kluczowe [CriticalDmgUpVespa] — nazwa] 섬봉광검술 - 환도
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].name
   kontekst: identyfikator tagu w tekstach: `[CriticalDmgUpVespa]`
   limit: do 50 znaków
   EN: Apic Flashburst Blade Art - Hwando
   PL: Sztuka Ostrza Apic Flashburst - Hwando
559. [Słowo kluczowe [CriticalDmgUpVespa] — opis] 이번 턴 동안 치명타로 가하는 피해량이 수치당 추가로 10%씩 증가함
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].desc
   limit: do 120 znaków
   EN: Deal +10% more damage on Critical Hit for every Stack this turn
   PL: W tej turze obrażenia krytyczne rosną o 10% za każdą wartość
560. [Słowo kluczowe [CriticalDmgUpVespa] — tekst klimatyczny] <color=#fde55d>공간이동에 가까운 순간적이고 폭발적인 도약법을 다루는 자에게 알맞은 검술.\n동부에서 전해져 내려온다.\n소년은 생과 사를 오가는 시술을 필사의 마음으로 받아들였고, 끝내 이겨내어 자격을 증명했다.</color>
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=CriticalDmgUpVespa].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>, \n
   EN: <color=#fde55d>A swordfighting style originating from the East, suited to those who employ instantaneous bursts of leaping movement that verge on teleportation.\n\nThe boy braved the life-threatening augmentation with a desperate resolve, and his survival proved his worth.</color>
   PL: <color=#fde55d>Szermierka ze Wschodu, odpowiednia dla tych, którzy poruszają się skokami na granicy teleportacji.\nChłopak przyjął tę śmiertelnie niebezpieczną modyfikację z rozpaczliwą determinacją i ostatecznie ją przetrwał, dowodząc swojej wartości.</color>
561. [Słowo kluczowe [Vespa_LowMorale] — nazwa] 언짢음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Vespa_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[Vespa_LowMorale]`
   limit: do 40 znaków
   EN: Vexation
   PL: Zirytowanie
562. [Słowo kluczowe [Vespa_LowMorale] — opis] - 사기 저하\n- 관통 위력 증가 1, 정신력 회복 효율 감소 1 얻음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Vespa_LowMorale].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Low Morale\n- Gain 1 Pierce Power Up and 1 SP Heal Efficiency Down
   PL: - Niskie Morale\n- Zyskuje 1 Wzrost Mocy Kłucia i 1 Spadek Wydajności Leczenia Poczytalności
563. [Słowo kluczowe [Vespa_Panic] — nazwa] 언짢음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Vespa_Panic].name
   kontekst: identyfikator tagu w tekstach: `[Vespa_Panic]`
   (powtórzenie elementu 561 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
564. [Słowo kluczowe [Vespa_Panic] — opis] - 패닉\n- 관통 위력 증가 2, 관통 피해량 증가 1, 정신력 회복 효율 감소 2 얻음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Vespa_Panic].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Panic\n- Gain 2 Pierce Power Up, 1 Pierce DMG Up, and 2 SP Heal Efficiency Down
   PL: - Panika\n- Zyskuje 2 Wzrostu Mocy Kłucia, 1 Wzrost Obrażeń Kłucia i 2 Spadek Wydajności Leczenia Poczytalności
565. [Słowo kluczowe [ScarBygoneDays_LowMorale] — nazwa] 애증
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ScarBygoneDays_LowMorale].name
   kontekst: identyfikator tagu w tekstach: `[ScarBygoneDays_LowMorale]`
   limit: do 40 znaków
   EN: Affection and Resentment
   PL: Miłość i Uraza
566. [Słowo kluczowe [ScarBygoneDays_LowMorale] — opis] 료슈에게 가하는 피해량과 받는 피해량 +10%
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ScarBygoneDays_LowMorale].desc
   limit: do 120 znaków
   EN: Deal +10% damage to and take +10% damage from Ryōshū
   PL: Zadaje i otrzymuje +10% obrażeń od i wobec Ryōshū
567. [Słowo kluczowe [ScarBygoneDays_Panic] — nazwa] 애증
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ScarBygoneDays_Panic].name
   kontekst: identyfikator tagu w tekstach: `[ScarBygoneDays_Panic]`
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
568. [Słowo kluczowe [ScarBygoneDays_Panic] — opis] 료슈에게 가하는 피해량과 받는 피해량 +20%
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=ScarBygoneDays_Panic].desc
   limit: do 120 znaków
   EN: Deal +20% damage to and take +20% damage from Ryōshū
   PL: Zadaje i otrzymuje +20% obrażeń od i wobec Ryōshū
569. [Słowo kluczowe [PhantomIncision] — nazwa] 검흔[잔상]
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PhantomIncision].name
   kontekst: identyfikator tagu w tekstach: `[PhantomIncision]`
   limit: do 40 znaków
   EN: Bladetrail [Afterimage]
   PL: Ślad Ostrza [Powidło]
570. [Słowo kluczowe [PhantomIncision] — opis] - 최댓값 : 99\n- 턴 시작시 수치 10당 취약 1 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PhantomIncision].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 99\n- Turn Start: Gain 1 Fragile for every 10 Stack (max 5)
   PL: - Maks. stosów: 99\n- Na początku tury zyskuje 1 Wrażliwości za każde 10 stosów (maks. 5)
571. [Słowo kluczowe [PhantomIncisionTotal] — nazwa] 지혜성도
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PhantomIncisionTotal].name
   kontekst: identyfikator tagu w tekstach: `[PhantomIncisionTotal]`
   limit: do 40 znaków
   EN: Dihui Star's Blade
   PL: Ostrze Gwiazdy Dihui
572. [Słowo kluczowe [PhantomIncisionTotal] — opis] - 현재 스테이지의 검흔[잔상] 수치 총합
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=PhantomIncisionTotal].desc
   limit: do 120 znaków
   EN: - Total sum of Bladetrail [Afterimage] Stack in this Encounter
   PL: - Łączna suma stosów Śladu Ostrza [Powidło] w tej walce
573. [Słowo kluczowe [LvDownLittleFingerBoss] — nazwa] 관망
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=LvDownLittleFingerBoss].name
   kontekst: identyfikator tagu w tekstach: `[LvDownLittleFingerBoss]`
   limit: do 40 znaków
   EN: Silent Regard
   PL: Wyczekiwanie
574. [Słowo kluczowe [LvDownLittleFingerBoss] — opis] 미사용 버프
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=LvDownLittleFingerBoss].desc
   limit: do 120 znaków
   EN: UNUSED BUFF
   PL: NIEWYKORZYSTANY BUFF
575. [Słowo kluczowe [TimeGapAb] — nazwa] 괴리
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeGapAb].name
   kontekst: identyfikator tagu w tekstach: `[TimeGapAb]`
   limit: do 40 znaków
   EN: Disjunction
   PL: Dysocjacja
576. [Słowo kluczowe [TimeGapAb] — opis] - 턴 시작 시 수치만큼 부위가 보호막 얻음\n- 보호막이 감소하면 수치도 감소함
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeGapAb].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Turn Start: The Part gains Shield equal to Stack\n- Reduction in the Shield reduces the Stack as well
   PL: - Na początku tury część zyskuje Tarczę równą wartości\n- Zmniejszenie Tarczy zmniejsza również wartość
577. [Słowo kluczowe [TimeEntangleFour] — nazwa] 4중 잔상 얽힘
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleFour].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleFour]`
   limit: do 50 znaków
   EN: Fourfold Afterimage Entanglement
   PL: Splot Powideł IV
578. [Słowo kluczowe [TimeEntangleFour] — opis] 잔상 얽힘 4단계\n- 자신의 속도 최댓값, 최솟값 -2\n- 자신의 공격 적중시 아래 효과 적용\n  · 독 1 부여\n  · 출혈 2 부여\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleFour].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 4 Afterimage Entanglement\n- Min & Max Speed -2 for this unit\n- On Hit, activate the following effects:\n  · Inflict 1 Poison\n  · Inflict 2 Bleed\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 4. stopnia\n- Min. i Maks. Szybkość tej jednostki -2\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 1 Zatrucia\n  · Nakłada 2 Krwawienia\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
579. [Słowo kluczowe [TimeEntangleFour] — podsumowanie] 잔상 얽힘 4단계
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleFour].summary
   limit: do 120 znaków
   EN: Stage 4 Afterimage Entanglement
   PL: Splot Powideł 4. stopnia
580. [Słowo kluczowe [TimeEntangleThree] — nazwa] 3중 잔상 얽힘
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleThree].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleThree]`
   limit: do 50 znaków
   EN: Threefold Afterimage Entanglement
   PL: Splot Powideł III
581. [Słowo kluczowe [TimeEntangleThree] — opis] 잔상 얽힘 3단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 출혈 2 부여\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleThree].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 3 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 2 Bleed\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 3. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 2 Krwawienia\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
582. [Słowo kluczowe [TimeEntangleThree] — podsumowanie] 잔상 얽힘 3단계
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleThree].summary
   limit: do 120 znaków
   EN: Stage 3 Afterimage Entanglement
   PL: Splot Powideł 3. stopnia
583. [Słowo kluczowe [TimeEntangleTwo] — nazwa] 2중 잔상 얽힘
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleTwo].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleTwo]`
   limit: do 50 znaków
   EN: Twofold Afterimage Entanglement
   PL: Splot Powideł II
584. [Słowo kluczowe [TimeEntangleTwo] — opis] 잔상 얽힘 2단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 다음 턴에 속박 1 부여\n  · 화상 2 부여
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleTwo].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 2 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 1 Bind next turn\n  · Inflict 2 Burn
   PL: Splot Powideł 2. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 1 Spętanie w następnej turze\n  · Nakłada 2 Podpalenia
585. [Słowo kluczowe [TimeEntangleTwo] — podsumowanie] 잔상 얽힘 2단계
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleTwo].summary
   limit: do 120 znaków
   EN: Stage 2 Afterimage Entanglement
   PL: Splot Powideł 2. stopnia
586. [Słowo kluczowe [TimeEntangleOne] — nazwa] 1중 잔상 얽힘
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleOne].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleOne]`
   limit: do 50 znaków
   EN: Onefold Afterimage Entanglement
   PL: Splot Powideł I
587. [Słowo kluczowe [TimeEntangleOne] — opis] 잔상 얽힘 1단계\n- 자신의 공격 적중시 아래 효과 적용\n  · 화상 2 부여
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleOne].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Stage 1 Afterimage Entanglement\n- On Hit, activate the following effects:\n  · Inflict 2 Burn
   PL: Splot Powideł 1. stopnia\n- Przy trafieniu działają następujące efekty:\n  · Nakłada 2 Podpalenia
588. [Słowo kluczowe [TimeEntangleOne] — podsumowanie] 잔상 얽힘 1단계
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleOne].summary
   limit: do 120 znaków
   EN: Stage 1 Afterimage Entanglement
   PL: Splot Powideł 1. stopnia
589. [Słowo kluczowe [LittleFingerBoss_Shin] — nazwa] 신(心) - 지혜성
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=LittleFingerBoss_Shin].name
   kontekst: identyfikator tagu w tekstach: `[LittleFingerBoss_Shin]`
   limit: do 40 znaków
   EN: Shin (心) - Dihui Star
   PL: Shin (心) - Gwiazda Dihui
590. [Słowo kluczowe [LittleFingerBoss_Shin] — opis] - 최댓값 : 3\n- 턴 시작 시 아래 효과 적용\n· 수치 1당 호흡 위력 5, 호흡 횟수 1 얻음\n· 자신의 잃은 체력 15% 당 참격 피해량 증가 1 얻음 (최대 5)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=LittleFingerBoss_Shin].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 3\n- Turn Start: Apply the following effects\n· Gain 5 Poise Potency and +1 Poise Count for every Stack\n· Gain 1 Slash DMG Up for every 15% missing HP on self (max 5)
   PL: - Maks. stosów: 3\n- Na początku tury działają następujące efekty\n· Zyskuje 5 Siły Oddechu i +1 Licznika Oddechu za każdy stos\n· Zyskuje 1 Wzrost Obrażeń Cięcia za każde 15% brakującego HP (maks. 5)
591. [Słowo kluczowe [RyoshuParrySoji] — nazwa] 뒤엉키고 틀어진 기억과 추억
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=RyoshuParrySoji].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuParrySoji]`
   limit: do 70 znaków
   EN: Twisted and Disjointed Memory and Recollection
   PL: Skręcone i Rozdarte Wspomnienia
592. [Słowo kluczowe [RyoshuParrySoji] — opis] - 스킬 슬롯 수 +1\n- 소지 아비에게 가하는 피해량, 받는 피해량 +20%, 합 승리 시, 소지 아비 정신력 -5\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (턴당 1회)\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=RyoshuParrySoji].desc
   limit: do 630 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +20% damage to and take +20% damage from The Pinky Nursefather; On Clash Win, deal 5 SP damage to The Pinky Nursefather\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn (once per turn)\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje i otrzymuje +20% obrażeń od i wobec Ojca Małego Palca; po wygranym Starciu zadaje Ojcu Małego Palca 5 obrażeń Poczytalności\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (1 raz na turę)\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
593. [Słowo kluczowe [RyoshuParrySoji] — podsumowanie] 생존한 아군이 있으면, 체력이 1 미만으로 감소하지 않음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=RyoshuParrySoji].summary
   limit: do 120 znaków
   EN: If there is a surviving ally, HP does not drop below 1
   PL: Jeżeli żyją sojusznicy, HP nie spada poniżej 1
594. [Słowo kluczowe [RyoshuStartA1C9P2] — nazwa] 난도질당한 기억
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=RyoshuStartA1C9P2].name
   kontekst: identyfikator tagu w tekstach: `[RyoshuStartA1C9P2]`
   (powtórzenie elementu 314 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
595. [Słowo kluczowe [RyoshuStartA1C9P2] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되면, 다음 턴 시작 시 흐트러짐 해제하고, 공격 위력 증가 1 얻음 (전투당 1회)
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=RyoshuStartA1C9P2].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When Staggered, immediately recover from Stagger at the start of the next turn and gain 1 Attack Power Up (once per Encounter)
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Po Oszołomieniu wychodzi z Oszołomienia na początku następnej tury i zyskuje 1 Wzrost Mocy Ataku (1 raz na walkę)
596. [Słowo kluczowe [Ryoshu_IndexFightBuff] — nazwa] 난도질당한 기억과 추억
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].name
   kontekst: identyfikator tagu w tekstach: `[Ryoshu_IndexFightBuff]`
   limit: do 50 znaków
   EN: Mutilated Memory and Recollection
   PL: Pocięta Pamięć i Wspomnienia
597. [Słowo kluczowe [Ryoshu_IndexFightBuff] — opis] - 스킬 슬롯 수 +1\n- 거미집 소속 적에게 입히는 피해량 +10%\n- 흐트러짐 상태가 되는 피해를 받을 때, 흐트러짐 상태가 되지 않고, 해당 흐트러짐 구간을 제거함. 이후 다음 턴에 공격 위력 증가 1 얻음 (턴당 1회)\n- 이번 전투에서 자신의 스킬 사용 시, 해당 속성의 E.G.O 자원 +1, 가장 수량이 적은 무작위 E.G.O 자원 +1 (턴당 2회)\n- 퇴각 불가능
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].desc
   limit: do 540 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Skill Slot +1\n- Deal +10% damage to The House of Spiders enemies\n- When taking damage that would Stagger this unit, does not get Staggered and remove the corresponding Stagger Threshold; then, gain 1 Attack Power Up next turn (once per turn)\n- For this Encounter: After using a Skill, gain 1 E.G.O resource of the Skill's Affinity and 1 E.G.O resource for the least-owned E.G.O resource (2 times per turn)\n- Cannot Retreat
   PL: - Liczba Slotów Umiejętności +1\n- Zadaje +10% obrażeń wrogom z Domu Pajęczyn\n- Przy otrzymaniu obrażeń, które oszołomiłyby ją, nie zostaje oszołomiona i usuwa dany Próg Oszołomienia; w następnej turze zyskuje 1 Wzrost Mocy Ataku (1 raz na turę)\n- W tej walce po użyciu Umiejętności zyskuje +1 Zasób E.G.O Grzechu tej Umiejętności i +1 losowy Zasób E.G.O najmniej posiadanego Grzechu (2 razy na turę)\n- Wycofanie niemożliwe
598. [Słowo kluczowe [Ryoshu_IndexFightBuff] — podsumowanie] 료슈 특수 효과
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Ryoshu_IndexFightBuff].summary
   limit: do 120 znaków
   EN: Ryōshū Exclusive Effect
   PL: Efekt specjalny Ryōshū
599. [Słowo kluczowe [Malkuth_Imperfect] — nazwa] 말쿠트의 통치 - 불완전 현현
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Malkuth_Imperfect].name
   kontekst: identyfikator tagu w tekstach: `[Malkuth_Imperfect]`
   limit: do 60 znaków
   EN: Malkuth's Reign - Imperfect Manifestation
   PL: Panowanie Malkuth - Niedoskonała Manifestacja
600. [Słowo kluczowe [Malkuth_Imperfect] — opis] <i><color=#d3a562>완전하지는 않지만 왕국을 다스릴 힘의 편린</color></i>
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Malkuth_Imperfect].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <i>, <color=#d3a562>, </color>, </i>
   EN: <i><color=#d3a562>An imperfect glimpse of the power that shall reign over the Kingdom</color></i>
   PL: <i><color=#d3a562>Niedoskonały fragment mocy, która zapanuje nad Królestwem</color></i>
601. [Słowo kluczowe [TimeEntangleDesc] — nazwa] 잔상 얽힘
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleDesc].name
   kontekst: identyfikator tagu w tekstach: `[TimeEntangleDesc]`
   limit: do 40 znaków
   EN: Afterimage Entanglement
   PL: Splot Powideł
602. [Słowo kluczowe [TimeEntangleDesc] — opis] 잔상이 얽혀있는 상태\n패턴이 진행됨에 따라 단계가 변화함
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=TimeEntangleDesc].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Afterimages are Entangled\nEffect Stage changes with the progress of combat pattern
   PL: Stan splecionych powideł\nStopień efektu zmienia się wraz z postępem wzorca walki
603. [Słowo kluczowe [IndexPrescriptDon_0] — nazwa] 지령[단말기] I
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptDon_0]`
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
604. [Słowo kluczowe [IndexPrescriptDon_0] — opis] 지령 표식이 새겨진 스킬을 사용하거나 적중한다.\n\n- 턴 시작 시 해금이 없을 때 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 3
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Use a Skill marked with Mark of the Prescript or hit a target with a marked Skill.\n\n- Turn Start: Gain this effect when this unit has no Unlock\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 3
   PL: Używa Umiejętności oznaczonej Znakiem Nakazu lub trafia nią cel.\n\n- Na początku tury zdobywany przy braku Odblokowania\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 3
605. [Słowo kluczowe [IndexPrescriptDon_0] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_0].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
606. [Słowo kluczowe [IndexPrescriptDon_1] — nazwa] 지령[단말기] II
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptDon_1]`
   (powtórzenie elementu 515 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Słowo kluczowe [IndexPrescriptDon_1] — opis] 지령 표식이 새겨진 스킬이 적중한다.\n\n- 턴 시작 시 해금 - I일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 6
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with a Skill marked with Mark of the Prescript.\n\n- Turn Start: Gain this effect if this unit has Unlock - I\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 6
   PL: Umiejętność oznaczona Znakiem Nakazu trafia cel.\n\n- Na początku tury zdobywany przy Odblokowaniu - I\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 6
608. [Słowo kluczowe [IndexPrescriptDon_1] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_1].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Słowo kluczowe [IndexPrescriptDon_2] — nazwa] 지령[단말기] III
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptDon_2]`
   (powtórzenie elementu 518 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Słowo kluczowe [IndexPrescriptDon_2] — opis] E.G.O 각성 스킬 또는 개화 E.G.O::대행 상태에서 지령 표식이 새겨진 ‘스킬 3’이 적중한다.\n\n- 턴 시작 시 해금 - II일 경우 얻음\n- 이 지령으로 달성할 수 있는 지령의 가호 최댓값: 9
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Hit a target with E.G.O Awakening Skill, or, in Effloresced E.G.O::Procuration state, 'Skill 3' marked with Mark of the Prescript.\n\n- Turn Start: Gain this effect if this unit has Unlock - II\n- Maximum stackable Grace of the Prescript with this Prescript is limited to 9
   PL: Trafia cel Umiejętność Przebudzenia E.G.O, lub w stanie Rozkwitu E.G.O::Procuration, „Umiejętność 3” oznaczona Znakiem Nakazu.\n\n- Na początku tury zdobywany przy Odblokowaniu - II\n- Maksymalna Łaska Nakazu osiągalna tym Nakazem: 9
611. [Słowo kluczowe [IndexPrescriptDon_2] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_2].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
612. [Słowo kluczowe [IndexPrescriptDon_3] — nazwa] 지령[단말기] IV
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].name
   kontekst: identyfikator tagu w tekstach: `[IndexPrescriptDon_3]`
   (powtórzenie elementu 521 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Słowo kluczowe [IndexPrescriptDon_3] — opis] 모든 적을 처치한다. 기한은 다음 지령이 오기 전까지.\n\n- 턴 시작 시 해금 - III일 경우 얻음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Eliminate all enemies before the next Prescript arrives.\n\n- Turn Start: Gain this effect if this unit has Unlock - III
   PL: Wyeliminuj wszystkich wrogów, zanim przyjdzie kolejny Nakaz.\n\n- Na początku tury zdobywany przy Odblokowaniu - III
614. [Słowo kluczowe [IndexPrescriptDon_3] — tekst klimatyczny] 지령은 다양한 형태로 전달된다. 지령을 어떤 형태로 전달받게 될지는, 마치 신탁처럼 일방향적으로 선택당해 결정되는 것.
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=IndexPrescriptDon_3].flavor
   (powtórzenie elementu 489 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
615. [Słowo kluczowe [UnlockBuff_Base] — nazwa] 해금
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_Base].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuff_Base]`
   limit: do 40 znaków
   EN: Unlock
   PL: Odblokowanie
616. [Słowo kluczowe [UnlockBuff_Base] — opis] - 지령의 가호가 일정 수치 이상이면 획득\n- 지령의 가호 수치에 따라 단계 증가\n- 최대 3단계까지 달성 가능
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuff_Base].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain this effect when over certain Grace of the Prescript Stack\n- Effect stage increases based on Grace of the Prescript Stack\n- Max: Stage 3
   PL: - Zdobywane przy Łasce Nakazu powyżej określonej wartości\n- Stopień rośnie zależnie od liczby stosów Łaski Nakazu\n- Maksymalnie 3. stopień
617. [Słowo kluczowe [UnlockBuffAlly_1] — nazwa] 해금 - I
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_1].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuffAlly_1]`
   (powtórzenie elementu 524 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Słowo kluczowe [UnlockBuffAlly_1] — opis] - 방어 레벨 +1\n- 전투 종료 시, 정신력 5 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +1\n- Combat End: Heal 5 SP
   PL: - Poziom Obrony +1\n- Po zakończeniu walki odzyskuje 5 Poczytalności
619. [Słowo kluczowe [UnlockBuffAlly_2] — nazwa] 해금 - II
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_2].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuffAlly_2]`
   (powtórzenie elementu 526 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Słowo kluczowe [UnlockBuffAlly_2] — opis] - 방어 레벨 +2\n- 전투 종료 시, 정신력 10 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +2\n- Combat End: Heal 10 SP
   PL: - Poziom Obrony +2\n- Po zakończeniu walki odzyskuje 10 Poczytalności
621. [Słowo kluczowe [UnlockBuffAlly_3] — nazwa] 해금 - III
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_3].name
   kontekst: identyfikator tagu w tekstach: `[UnlockBuffAlly_3]`
   (powtórzenie elementu 528 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Słowo kluczowe [UnlockBuffAlly_3] — opis] - 방어 레벨 +3\n- 전투 종료 시, 정신력 15 회복
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=UnlockBuffAlly_3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Defense Level +3\n- Combat End: Heal 15 SP
   PL: - Poziom Obrony +3\n- Po zakończeniu walki odzyskuje 15 Poczytalności
623. [Słowo kluczowe [Blandishment] — nazwa] 당연한 믿음
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment].name
   kontekst: identyfikator tagu w tekstach: `[Blandishment]`
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Słowo kluczowe [Blandishment] — opis] - 속도 최솟값, 최댓값 1 증가\n- 공격 레벨 +2, 방어 레벨 +2\n- 기본 스킬로 획득하는 호흡 위력 +1\n- 기본 공격 스킬의 정신력 감소 효과로 정신력이 -15 미만으로 내려가지 않음\n- 최댓값 : 1
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment].desc
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +1\n- Offense Level +2, Defense Level +2\n- Gain 1 more Poise Potency from Base Skills\n- This unit's SP does not drop below -15 from SP loss effects on this unit's Base Attack Skills\n- Max Stack: 1
   PL: - Min. i Maks. Szybkość +1\n- Poziom Ataku +2, Poziom Obrony +2\n- Podstawowe Umiejętności zyskują +1 więcej Siły Oddechu\n- Poczytalność tej jednostki nie spada poniżej -15 z powodu efektów utraty Poczytalności jej podstawowych Umiejętności ataku\n- Maks. stosów: 1
625. [Słowo kluczowe [Blandishment_Shin] — nazwa] 신(心) - 대행
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Shin].name
   kontekst: identyfikator tagu w tekstach: `[Blandishment_Shin]`
   limit: do 40 znaków
   EN: Shin (心) - Procuration
   PL: Shin (心) - Procuration
626. [Słowo kluczowe [Blandishment_Shin] — opis] - 속도 최솟값, 최댓값 2 증가\n- 공격 레벨 +1, 방어 레벨 +1\n- 기본 스킬로 획득하는 호흡 위력과 횟수 +1\n- 기본 스킬의 피해량 +(잃은 체력 비율/2)% (최대 40%)\n- 최댓값 : 1
   źródło: BattleKeywords-a1c9p2.json :: dataList[id=Blandishment_Shin].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed +2\n- Offense Level +1, Defense Level +1\n- Gain 1 more Poise Potency and Poise Count from Base Skills\n- Deal +(missing HP percentage / 2)% damage with Base Skills (max 40%)\n- Max Stack: 1
   PL: - Min. i Maks. Szybkość +2\n- Poziom Ataku +1, Poziom Obrony +1\n- Podstawowe Umiejętności zyskują +1 więcej Siły Oddechu i Licznika Oddechu\n- Podstawowe Umiejętności zadają +(procent brakującego HP / 2)% obrażeń (maks. 40%)\n- Maks. stosów: 1

## Słowa kluczowe bitwy — BattleKeywords-a1c9p3
- plik gry: `BattleKeywords-a1c9p3.json` (opisy wyświetlane w dymkach pomocy podczas walki)

627. [Słowo kluczowe [MosesWhiteBreathMental] — nazwa] 하얀 숨 - 정신 보호
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesWhiteBreathMental].name
   kontekst: identyfikator tagu w tekstach: `[MosesWhiteBreathMental]`
   limit: do 50 znaków
   EN: White Breath - Safeguard the Mind
   PL: Biały Oddech - Osłona Umysłu
628. [Słowo kluczowe [MosesWhiteBreathMental] — opis] - 캐릭터의 기본 정신력 증가 조건에 의한 정신력 회복량 5 증가\n- 캐릭터의 기본 정신력 감소 조건에 의한 정신력 감소량 5 감소\n- 턴 종료시 1 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesWhiteBreathMental].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Amount of SP healed due to the unit's 'Base factors increasing Sanity(SP)' increases by 5\n- Amount of SP lost due to the unit's 'Base factors decreasing Sanity(SP)' decreases by 5\n- Turn End: Lose 1 Stack
   PL: - Odzyskiwana Poczytalność z podstawowych warunków wzrostu Poczytalności rośnie o 5\n- Tracona Poczytalność z podstawowych warunków spadku Poczytalności maleje o 5\n- Na koniec tury traci 1 stos
629. [Słowo kluczowe [MosesRedBreathBody] — nazwa] 붉은 숨 - 육체 강화
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathBody].name
   kontekst: identyfikator tagu w tekstach: `[MosesRedBreathBody]`
   limit: do 50 znaków
   EN: Red Breath - Strengthen the Body
   PL: Czerwony Oddech - Wzmocnienie Ciała
630. [Słowo kluczowe [MosesRedBreathBody] — opis] - (자신의 정신력 / 10)만큼 공격 레벨, 방어 레벨이 증가함 (소수점 버림)\n- 턴 종료시 1 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathBody].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Gain +(SP/10) Offense Level and Defense Level (rounded down)\n- Turn End: Lose 1 Stack
   PL: - Poziom Ataku i Poziom Obrony rosną o (Poczytalność / 10) (zaokrąglone w dół)\n- Na koniec tury traci 1 stos
631. [Słowo kluczowe [MosesRedBreathShield] — nazwa] 붉은 숨 - 보호
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathShield].name
   kontekst: identyfikator tagu w tekstach: `[MosesRedBreathShield]`
   limit: do 40 znaków
   EN: Red Breath - Protect
   PL: Czerwony Oddech - Ochrona
632. [Słowo kluczowe [MosesRedBreathShield] — opis] - 턴 시작시 이번 턴 동안 보호막 30 얻음
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesRedBreathShield].desc
   limit: do 120 znaków
   EN: - Turn Start: Gain 30 Shield for this turn
   PL: - Na początku tury zyskuje 30 Tarczy na tę turę
633. [Słowo kluczowe [MosesPurpleBreathBind] — nazwa] 보라색 숨 - 히스테릭
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesPurpleBreathBind].name
   kontekst: identyfikator tagu w tekstach: `[MosesPurpleBreathBind]`
   limit: do 40 znaków
   EN: Purple Breath - Hysteria
   PL: Fioletowy Oddech - Histeria
634. [Słowo kluczowe [MosesPurpleBreathBind] — opis] - 최댓값: 4\n- 턴 종료시 체력, 정신력 수치만큼 감소\n- 턴 종료시 모제스의 체력, 정신력 수치만큼 감소\n- 다음 턴에 취약 2, 속박 3, 더하기 코인 약화 3 얻음\n- 효과 발동시 1 감소
   źródło: BattleKeywords-a1c9p3.json :: dataList[id=MosesPurpleBreathBind].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Max Stack: 4\n- Turn End: Lose HP and SP equal to Stack\n- Turn End: Moses loses HP and SP equal to Stack\n- Gain 2 Fragile, 3 Bind, and 3 Plus Coin Drop next turn\n- Lose 1 Stack when this effect is triggered
   PL: - Maks. stosów: 4\n- Na koniec tury traci HP i Poczytalność równą wartości\n- Na koniec tury Moses traci HP i Poczytalność równą wartości\n- W następnej turze zyskuje 2 Wrażliwości, 3 Spętań i 3 Osłabienia Monet Plus\n- Przy wywołaniu efektu traci 1 stos
