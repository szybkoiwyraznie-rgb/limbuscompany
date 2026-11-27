# Paczka AI P65 (Fala 3 · 3C) — Przeciwnicy, części Anomalii, bossowie i jednostki wsparcia (statystyki/skille) (część 1/23)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P65_3c_przeciwnicy_i_anomalie_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P65_3c_przeciwnicy_i_anomalie_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Mechanika wydarzeń wyboru: ChoiceEventEffect-a1c7p3
- plik gry: `ChoiceEventEffect-a1c7p3.json`

1. [Mechanika wydarzeń wyboru [LoseRatioHpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#e30000>{amount}%만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=LoseRatioHpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>{conditions}{targets}</color> takes <color=#e30000>{amount}% HP</color> <color=#ebcaa2>Damage!</color>
   PL:
2. [Mechanika wydarzeń wyboru [Choice_901070401] — tekst] <color=#f8c200>분노 속성 E.G.O 자원을 2개</color> 획득\n<color=#f8c200>오만 속성 E.G.O 자원을 2개</color> 획득
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=Choice_901070401].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: Gain <color=#f8c200>2 Wrath E.G.O resources</color>\nGain <color=#f8c200>2 Pride E.G.O resources</color>
   PL:
3. [Mechanika wydarzeń wyboru [Choice_901070402] — tekst] <color=#f8c200>색욕 속성 E.G.O 자원을 2개</color> 획득\n<color=#f8c200>탐식 속성 E.G.O 자원을 2개</color> 획득
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=Choice_901070402].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: Gain <color=#f8c200>2 Lust E.G.O resources</color>\nGain <color=#f8c200>2 Gluttony E.G.O resources</color>
   PL:
4. [Mechanika wydarzeń wyboru [Choice_901070403] — tekst] <color=#f8c200>우울 속성 E.G.O 자원을 2개</color> 획득\n<color=#f8c200>질투 속성 E.G.O 자원을 2개</color> 획득
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=Choice_901070403].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>, \n
   EN: Gain <color=#f8c200>2 Gloom E.G.O resources</color>\nGain <color=#f8c200>2 Envy E.G.O resources</color>
   PL:
5. [Mechanika wydarzeń wyboru [Choice_901070404] — tekst] 모든 수감자가 다음 전투 시작 시 <color=#e30000>파열 횟수 4</color> 얻음
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=Choice_901070404].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#e30000>, </color>
   EN: All sinners gain <color=#e30000>+4 Rupture Count</color> at the next Combat Start
   PL:
6. [Mechanika wydarzeń wyboru [Choice_901070405] — tekst] 모든 수감자가 다음 전투 시작 시 <color=#e30000>파열 4, 파열 횟수 4</color> 얻음
   źródło: ChoiceEventEffect-a1c7p3.json :: dataList[id=Choice_901070405].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#e30000>, </color>
   EN: All sinners gain <color=#e30000>4 Rupture and +4 Rupture Count</color> at the next Combat Start
   PL:

## Mechanika wydarzeń wyboru: ChoiceEventEffect-a1c8p2
- plik gry: `ChoiceEventEffect-a1c8p2.json`

7. [Mechanika wydarzeń wyboru [GetConfirmedObject] — tekst] <color=#ebcaa2>기물 {reward} 획득!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=GetConfirmedObject].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>{reward} Artifact obtained!</color>
   PL:
8. [Mechanika wydarzeń wyboru [GetConfirmedCoin] — tekst] <color=#ebcaa2>기물 {reward} {stack}개 획득!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=GetConfirmedCoin].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>{stack} {reward} Artifact(s) obtained!</color>
   PL:
9. [Mechanika wydarzeń wyboru [LoseConfirmedCoin] — tekst] <color=#ebcaa2>기물 {reward} {stack}개 잃음!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=LoseConfirmedCoin].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>{stack} {reward} Artifact(s) lost!</color>
   PL:
10. [Mechanika wydarzeń wyboru [DestroyObject] — tekst] <color=#ebcaa2>기물 {reward}</color> <color=#e30000>소멸!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=DestroyObject].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>{reward} Artifact</color> <color=#e30000>lost!</color>
   PL:
11. [Mechanika wydarzeń wyboru [GetConfirmedObjectOnWinBattle] — tekst] <color=#ebcaa2>다음 전투 승리 시 기물 {reward} 획득!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=GetConfirmedObjectOnWinBattle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Win the next battle to gain {reward} Artifact!</color>
   PL:
12. [Mechanika wydarzeń wyboru [HiddenGiftUnlockHiddenRoute] — tekst] <color=#ebcaa2>새로운 길이 지도에 추가됨!</color>
   źródło: ChoiceEventEffect-a1c8p2.json :: dataList[id=HiddenGiftUnlockHiddenRoute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>A new path opened up on the map!</color>
   PL:

## Mechanika wydarzeń wyboru: ChoiceEventEffect
- plik gry: `ChoiceEventEffect.json`

13. [Mechanika wydarzeń wyboru [Nothing] — tekst] <color=#ebcaa2>아무 일도 일어나지 않았다.</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Nothing].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Nothing happened.</color>
   PL:
14. [Mechanika wydarzeń wyboru [LevelupPersonality] — tekst] <color=#ebcaa2>수감자 강화 이벤트 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LevelupPersonality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Event: Sinner Power-up!</color>
   PL:
15. [Mechanika wydarzeń wyboru [GetEgogift] — tekst] <color=#ebcaa2>랜덤 에고기프트 획득 이벤트 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetEgogift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Event: Random E.G.O Gift!</color>
   PL:
16. [Mechanika wydarzeń wyboru [GetCharacter] — tekst] <color=#ebcaa2>수감자 추가 이벤트 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetCharacter].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Event: Sinner Recruitment!</color>
   PL:
17. [Mechanika wydarzeń wyboru [LevelupPersonalityOnWinBattle] — tekst] <color=#ebcaa2>다음 전투 승리 시 수감자 추가 이벤트 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LevelupPersonalityOnWinBattle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Win the next battle to recruit a Sinner!</color>
   PL:
18. [Mechanika wydarzeń wyboru [GetConfirmedEgogiftOnWinBattle] — tekst] <color=#ebcaa2>다음 전투 승리 시 E.G.O 기프트 {reward} 획득!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetConfirmedEgogiftOnWinBattle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Win the next battle to gain E.G.O Gift {reward}!</color>
   PL:
19. [Mechanika wydarzeń wyboru [StartBattle] — tekst] <color=#ff0000>전투 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=StartBattle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>Combat Encounter!</color>
   PL:
20. [Mechanika wydarzeń wyboru [StartBattle_Normal] — tekst] <color=#ff0000>일반 전투 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=StartBattle_Normal].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>Regular Encounter!</color>
   PL:
21. [Mechanika wydarzeń wyboru [StartBattle_Danger] — tekst] <color=#ff0000>위험 전투 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=StartBattle_Danger].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>Risky Encounter!</color>
   PL:
22. [Mechanika wydarzeń wyboru [StartBattle_Abnormality] — tekst] <color=#ff0000>집중 전투 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=StartBattle_Abnormality].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>Focused Encounter!</color>
   PL:
23. [Mechanika wydarzeń wyboru [StartBattle_FloorBoss] — tekst] <color=#ff0000>층 보스 전투 발생!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=StartBattle_FloorBoss].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>Floor Boss Encounter!</color>
   PL:
24. [Mechanika wydarzeń wyboru [RecoverHpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#00ff9c>{amount}만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverHpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed for</color> <color=#00ff9c>{amount} HP.</color>
   PL:
25. [Mechanika wydarzeń wyboru [RecoverMpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#80c9ff>{amount}만큼 정신력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverMpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#80c9ff>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed for</color> <color=#80c9ff>{amount} SP.</color>
   PL:
26. [Mechanika wydarzeń wyboru [RecoverHpOnlyUntilMax] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#00ff9c>체력 최대로</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverHpOnlyUntilMax].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed back to</color> <color=#00ff9c>Full HP.</color>
   PL:
27. [Mechanika wydarzeń wyboru [RecoverMpOnlyUntilMax] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#80c9ff>정신력 최대로</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverMpOnlyUntilMax].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#80c9ff>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed back to</color> <color=#80c9ff>Full SP.</color>
   PL:
28. [Mechanika wydarzeń wyboru [LoseHpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#e30000>{amount}만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseHpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>took</color> <color=#e30000>{amount} HP Damage!</color>
   PL:
29. [Mechanika wydarzeń wyboru [LoseMpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#fe4b48>{amount}만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseMpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>lost</color> <color=#fe4b48>{amount} SP!</color>
   PL:
30. [Mechanika wydarzeń wyboru [RecoverHpMpSameAmount] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#00ff9c>{amount}만큼 체력</color>, <color=#80c9ff>정신력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverHpMpSameAmount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>, <color=#80c9ff>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed for</color> <color=#00ff9c>{amount} HP</color> and <color=#80c9ff>SP.</color>
   PL:
31. [Mechanika wydarzeń wyboru [RecoverHpMpDifferentAmount] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#00ff9c>{hpAmount}만큼 체력</color> <color=#ebcaa2>회복</color>, <color=#80c9ff>{mpAmount}만큼 정신력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverHpMpDifferentAmount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>, <color=#80c9ff>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed for</color> <color=#00ff9c>{hpAmount} HP</color> and <color=#80c9ff>{mpAmount} SP.</color>
   PL:
32. [Mechanika wydarzeń wyboru [LoseHpMpSameAmount] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#e30000>{amount}만큼 체력</color>, <color=#fe4b48>정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseHpMpSameAmount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>, <color=#fe4b48>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>took</color> <color=#e30000>{amount} HP</color> and <color=#fe4b48>SP damage!</color>
   PL:
33. [Mechanika wydarzeń wyboru [LoseHpMpDifferentAmount] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#e30000>{hpAmount}만큼 체력</color> <color=#ebcaa2>피해</color>, <color=#fe4b48>{mpAmount}만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseHpMpDifferentAmount].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>, <color=#fe4b48>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>took</color> <color=#e30000>{hpAmount} HP</color> and <color=#fe4b48>{mpAmount} SP damage!</color>
   PL:
34. [Mechanika wydarzeń wyboru [GetConfirmedEgogift] — tekst] <color=#ebcaa2>E.G.O 기프트 {reward} 획득!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetConfirmedEgogift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>E.G.O Gift {reward} obtained!</color>
   PL:
35. [Mechanika wydarzeń wyboru [GetConfirmedStackableEgogift] — tekst] <color=#ebcaa2>E.G.O 기프트 {reward} {stack}개 획득!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetConfirmedStackableEgogift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>E.G.O Gift {stack} {reward} obtained!</color>
   PL:
36. [Mechanika wydarzeń wyboru [LoseConfirmedStackableEgogift] — tekst] <color=#ebcaa2>E.G.O 기프트 {reward} {stack}개 잃음!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseConfirmedStackableEgogift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>E.G.O Gift {stack} {reward} lost!</color>
   PL:
37. [Mechanika wydarzeń wyboru [GetBuff_OnStageStart] — tekst] <color=#ebcaa2>다음 전투에서 스테이지 진입 시 {conditional}{target} {buffName} {stack} 획득</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetBuff_OnStageStart].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>{target} {conditional} will enter the next combat encounter with {stack} {buffName}.</color>
   PL:
38. [Mechanika wydarzeń wyboru [UnlockHiddenRoute] — tekst] <color=#ebcaa2>새로운 길이 지도에 추가됨!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=UnlockHiddenRoute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>There’s a new path on the map!</color>
   PL:
39. [Mechanika wydarzeń wyboru [ReduceEnemyWave] — tekst] <color=#ebcaa2>다음 전투에서 적 웨이브 {waveNum} 감소</color>
   źródło: ChoiceEventEffect.json :: dataList[id=ReduceEnemyWave].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Enemy waves reduced by {waveNum} for the next battle</color>
   PL:
40. [Mechanika wydarzeń wyboru [DestroyEgogift] — tekst] <color=#ebcaa2>E.G.O 기프트 {reward}</color> <color=#e30000>소멸!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=DestroyEgogift].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>E.G.O Gift {reward}</color> <color=#e30000>destroyed!</color>
   PL:
41. [Mechanika wydarzeń wyboru [Choice_90103301] — tekst] <color=#ebcaa2>이번 전투 동안</color> <color=#f8c200>속도 +1</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90103301].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#f8c200>
   EN: <color=#f8c200>Speed +1</color> <color=#ebcaa2>for this battle</color>
   PL:
42. [Mechanika wydarzeń wyboru [Choice_901001] — tekst] <color=#ebcaa2>전투 시작 시</color> <color=#a0392b>분노 속성 공격 스킬</color>을 보유하지 않은 인격이 <color=#e30000>분노 피해 5</color> <color=#ebcaa2>입음</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901001].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#a0392b>, <color=#e30000>
   EN: <color=#ebcaa2>At the start of the combat phase,</color> allies without <color=#a0392b>Wrath Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#e30000>5 Wrath damage</color>
   PL:
43. [Mechanika wydarzeń wyboru [Choice_901007] — tekst] <color=#ebcaa2>턴 시작 시</color> <color=#00ff9c>10만큼 체력</color>, <color=#80c9ff>정신력</color> </color=#ebcaa2>회복</color> (최대 3턴)
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901007].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>, <color=#80c9ff>, </color=#ebcaa2>
   EN: <color=#ebcaa2>At the start of the turn,</color> </color=#ebcaa2>heal</color> <color=#00ff9c>10 HP</color> and <color=#80c9ff>10 SP</color> (Up to 3 turns)
   PL:
44. [Mechanika wydarzeń wyboru [Choice_901009] — tekst] <color=#ebcaa2>전투 시작 시</color> <color=#e30000>스킬 최종 위력 -1</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901009].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#e30000>Skill Final Power -1</color> <color=#ebcaa2>at the start of the combat phase.</color>
   PL:
45. [Mechanika wydarzeń wyboru [Choice_901010] — tekst] <color=#ebcaa2>전투 시작 시</color> <color=#bb521f>색욕 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격이 흐트러짐 상태로 시작함</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901010].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#bb521f>
   EN: <color=#ebcaa2>At the start of the next battle,</color> <color=#ebcaa2>Ally Units without</color> <color=#bb521f>Lust Affinity Attack Skill</color> <color=#ebcaa2>are Staggered</color>
   PL:
46. [Mechanika wydarzeń wyboru [Choice_901019] — tekst] <color=#ebcaa2>전투 시작 시</color> <color=#e30000>속도 -2</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901019].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#e30000>Speed -2</color> <color=#ebcaa2>at the start of the combat phase.</color>
   PL:
47. [Mechanika wydarzeń wyboru [Choice_90103402] — tekst] <color=#ebcaa2>이번 전투 동안</color> <color=#f8c200>속도 +2</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90103402].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#f8c200>
   EN: <color=#f8c200>Speed +2</color> <color=#ebcaa2>for this battle</color>
   PL:
48. [Mechanika wydarzeń wyboru [Choice_1030301] — tekst] <color=#ebcaa2>다음 전투 시작 시 모든 아군이</color> <color=#f8c200>공격 위력 증가 3</color><color=#ebcaa2>을 얻음</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_1030301].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#f8c200>
   EN: <color=#ebcaa2>At the start of the next battle, All Ally Units</color> <color=#ebcaa2>gain</color> <color=#f8c200>3 Attack Power Up.</color>
   PL:
49. [Mechanika wydarzeń wyboru [Choice_1030501] — tekst] <color=#ff0000>전투 발생!</color>\n<color=#ebcaa2>모든 적에게</color> <color=#e30000>공격 위력 감소 5</color> <color=#ebcaa2>부여됨!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_1030501].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, <color=#ebcaa2>, <color=#e30000>, \n
   EN: <color=#ff0000>Combat Encounter!</color>\n<color=#ebcaa2>All enemies</color> <color=#ebcaa2>are inflicted with</color> <color=#e30000>5 Attack Power Down!</color>
   PL:
50. [Mechanika wydarzeń wyboru [Choice_1031001] — tekst] <color=#ebcaa2>선택한 인격이 다음 전투 2회동안</color> <color=#e30000>피해량 감소 3</color><color=#ebcaa2>을 얻음</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_1031001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>The chosen Sinner</color> <color=#ebcaa2>gains</color> <color=#e30000>3 Damage Down</color> <color=#ebcaa2>for the next 2 battles.</color>
   PL:
51. [Mechanika wydarzeń wyboru [Choice_90100201] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#e30000>12만큼 체력</color> <color=#ebcaa2>피해</color>, <color=#fe4b48>8만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90100201].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#e30000>12 HP</color> <color=#ebcaa2>damage and</color> <color=#fe4b48>8 SP</color> <color=#ebcaa2>damage!</color>
   PL:
52. [Mechanika wydarzeń wyboru [Choice_90100502] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#e30000>15만큼 체력</color> <color=#ebcaa2>피해</color>, <color=#fe4b48>12만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90100502].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#e30000>15 HP</color> <color=#ebcaa2>damage and</color> <color=#fe4b48>12 SP</color> <color=#ebcaa2>damage!</color>
   PL:
53. [Mechanika wydarzeń wyboru [Choice_90101001] — tekst] <color=#bb521f>색욕 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>10만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#bb521f>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#bb521f>Lust Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>10 SP</color> <color=#ebcaa2>damage!</color>
   PL:
54. [Mechanika wydarzeń wyboru [Choice_90101101] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#fe4b48>15만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#fe4b48>15 SP</color> <color=#ebcaa2>damage!</color>
   PL:
55. [Mechanika wydarzeń wyboru [Choice_90101701] — tekst] <color=#ebcaa2>판정에 성공한 수감자</color> <color=#fe4b48>5만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101701].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who passed the check takes</color> <color=#fe4b48>5 SP</color> <color=#ebcaa2>damage!</color>
   PL:
56. [Mechanika wydarzeń wyboru [Choice_90101702] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#fe4b48>25만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101702].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#fe4b48>25 SP</color> <color=#ebcaa2>damage!</color>
   PL:
57. [Mechanika wydarzeń wyboru [Choice_90101801] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#fe4b48>12만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101801].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#fe4b48>12 SP</color> <color=#ebcaa2>damage!</color>
   PL:
58. [Mechanika wydarzeń wyboru [Choice_90101901] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#fe4b48>10만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101901].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>The Sinner who failed the check takes</color> <color=#fe4b48>10 SP</color> <color=#ebcaa2>damage!</color>
   PL:
59. [Mechanika wydarzeń wyboru [Choice_90102001] — tekst] <color=#61822b>탐식 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>5만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#61822b>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#61822b>Gluttony Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>5 HP</color> <color=#ebcaa2>damage!</color>
   PL:
60. [Mechanika wydarzeń wyboru [Choice_90102002] — tekst] <color=#61822b>탐식 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>10만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102002].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#61822b>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#61822b>Gluttony Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>10 HP</color> <color=#ebcaa2>damage!</color>
   PL:
61. [Mechanika wydarzeń wyboru [Choice_90102201] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>13만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102201].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>13 HP</color> <color=#ebcaa2>damage!</color>
   PL:
62. [Mechanika wydarzeń wyboru [Choice_90103302] — tekst] <color=#7d4e94>질투 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#e30000>15만큼 체력</color>, <color=#fe4b48>정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90103302].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#7d4e94>, </color>, <color=#ebcaa2>, <color=#e30000>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#7d4e94>Envy Affinity Attack Skill</color> <color=#fe4b48>take</color> <color=#e30000>15 HP</color> <color=#ebcaa2>damage and</color> <color=#fe4b48>15 SP</color> <color=#ebcaa2>damage!</color>
   PL:
63. [Mechanika wydarzeń wyboru [Choice_90100101] — tekst] <color=#a0392b>분노 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>16만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90100101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a0392b>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#a0392b>Wrath Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>16 HP</color> <color=#ebcaa2>damage!</color>
   PL:
64. [Mechanika wydarzeń wyboru [Choice_901004] — tekst] <color=#a0392b>분노 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>15만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901004].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a0392b>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#a0392b>Wrath Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>15 HP.</color>
   PL:
65. [Mechanika wydarzeń wyboru [Choice_90100701] — tekst] <color=#bb521f>색욕 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#80c9ff>정신력</color> </color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90100701].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#bb521f>, </color>, <color=#ebcaa2>, <color=#80c9ff>, </color=#ebcaa2>
   EN: <color=#ebcaa2>Identities with</color> <color=#bb521f>Lust Affinity Attack Skill</color> </color=#ebcaa2>heal</color> <color=#80c9ff>SP.</color>
   PL:
66. [Mechanika wydarzeń wyboru [Choice_901008] — tekst] <color=#bb521f>색욕 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>10만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901008].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#bb521f>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#bb521f>Lust Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>10 HP.</color>
   PL:
67. [Mechanika wydarzeń wyboru [Choice_90100901] — tekst] <color=#bb521f>색욕 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>20만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90100901].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#bb521f>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#bb521f>Lust Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>20 SP</color> <color=#ebcaa2>damage!</color>
   PL:
68. [Mechanika wydarzeń wyboru [Choice_901014] — tekst] <color=#e48801>나태 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>20만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901014].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#e48801>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#e48801>Sloth Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>20 HP</color> <color=#ebcaa2>damage!</color>
   PL:
69. [Mechanika wydarzeń wyboru [Choice_90101401] — tekst] <color=#e48801>나태 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>12만큼 체력</color>과 <color=#fe4b48>정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101401].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#e48801>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#e48801>Sloth Affinity Attack Skill</color> <color=#fe4b48>take</color> <color=#fe4b48>12 HP</color> <color=#ebcaa2>damage and</color> <color=#fe4b48>12 SP</color> <color=#ebcaa2>damage!</color>
   PL:
70. [Mechanika wydarzeń wyboru [Choice_90101601] — tekst] <color=#61822b>탐식 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#80c9ff>정신력</color> </color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90101601].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#61822b>, </color>, <color=#ebcaa2>, <color=#80c9ff>, </color=#ebcaa2>
   EN: <color=#ebcaa2>Identities with</color> <color=#61822b>Gluttony Affinity Attack Skill</color> </color=#ebcaa2>heal</color> <color=#80c9ff>SP.</color>
   PL:
71. [Mechanika wydarzeń wyboru [Choice_901018] — tekst] <color=#a0392b>분노 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 무작위 인격 1명</color> <color=#fe4b48>10만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901018].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#a0392b>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>One random Identity without</color> <color=#a0392b>Wrath Affinity Attack Skill</color> <color=#ebcaa2>takes</color> <color=#fe4b48>10 HP</color> <color=#ebcaa2>damage!</color>
   PL:
72. [Mechanika wydarzeń wyboru [Choice_901021] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>10만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901021].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>10 HP</color> <color=#ebcaa2>damage!</color>
   PL:
73. [Mechanika wydarzeń wyboru [Choice_901023] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>9만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901023].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>9 SP</color> <color=#ebcaa2>damage!</color>
   PL:
74. [Mechanika wydarzeń wyboru [Choice_90102301] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 무작위 인격 1명</color> <color=#fe4b48>10만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102301].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>One random Identity without</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>takes</color> <color=#fe4b48>10 SP</color> <color=#ebcaa2>damage!</color>
   PL:
75. [Mechanika wydarzeń wyboru [Choice_901024] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 정신력이 가장 낮은 인격</color> <color=#f8c200>체력 최대로</color> </color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901024].content
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#f8c200>, </color=#ebcaa2>
   EN: <color=#ebcaa2>The Identity with the lowest Sanity who possesses</color> <color=#306471>Gloom Affinity Attack Skill</color> </color=#ebcaa2>fully heals their</color> <color=#f8c200>HP.</color>
   PL:
76. [Mechanika wydarzeń wyboru [Choice_901025] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>20만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901025].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>20 HP</color> <color=#ebcaa2>damage!</color>
   PL:
77. [Mechanika wydarzeń wyboru [Choice_90102501] — tekst] <color=#306471>우울 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>20만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102501].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#306471>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#306471>Gloom Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>20 HP.</color>
   PL:
78. [Mechanika wydarzeń wyboru [Choice_901026] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>10만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901026].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#185188>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#185188>Pride Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>10 HP</color> <color=#ebcaa2>damage!</color>
   PL:
79. [Mechanika wydarzeń wyboru [Choice_90102601] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>10만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102601].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#185188>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#185188>Pride Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>10 HP.</color>
   PL:
80. [Mechanika wydarzeń wyboru [Choice_901027] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>25만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901027].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#185188>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#185188>Pride Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>25 HP</color> <color=#ebcaa2>damage!</color>
   PL:
81. [Mechanika wydarzeń wyboru [Choice_90102701] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>25만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102701].content
   (powtórzenie elementu 80 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
82. [Mechanika wydarzeń wyboru [Choice_901028] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>5만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901028].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#185188>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#185188>Pride Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>5 HP</color> <color=#ebcaa2>damage!</color>
   PL:
83. [Mechanika wydarzeń wyboru [Choice_90102801] — tekst] <color=#185188>오만 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>15만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90102801].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#185188>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#185188>Pride Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>15 HP.</color>
   PL:
84. [Mechanika wydarzeń wyboru [Choice_901032] — tekst] <color=#7d4e94>질투 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>20만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901032].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#7d4e94>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#7d4e94>Envy Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>20 SP</color> <color=#ebcaa2>damage!</color>
   PL:
85. [Mechanika wydarzeń wyboru [Choice_901034] — tekst] <color=#7d4e94>질투 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#e30000>15만큼 체력</color>, <color=#fe4b48>정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901034].content
   (powtórzenie elementu 62 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
86. [Mechanika wydarzeń wyboru [Choice_901035] — tekst] <color=#7d4e94>질투 속성 공격 스킬</color><color=#ebcaa2>을 보유하지 않은 인격</color> <color=#fe4b48>12만큼 체력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_901035].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#7d4e94>, </color>, <color=#ebcaa2>, <color=#fe4b48>
   EN: <color=#ebcaa2>Identities without</color> <color=#7d4e94>Envy Affinity Attack Skill</color> <color=#ebcaa2>take</color> <color=#fe4b48>12 HP</color> <color=#ebcaa2>damage!</color>
   PL:
87. [Mechanika wydarzeń wyboru [Choice_90103501] — tekst] <color=#7d4e94>질투 속성 공격 스킬</color><color=#ebcaa2>을 보유하고 있는 인격</color> <color=#f8c200>15만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90103501].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#7d4e94>, </color>, <color=#ebcaa2>, <color=#f8c200>
   EN: <color=#ebcaa2>Identities with</color> <color=#7d4e94>Envy Affinity Attack Skill</color> <color=#ebcaa2>heal</color> <color=#f8c200>15 HP.</color>
   PL:
88. [Mechanika wydarzeń wyboru [Choice_1040301] — tekst] <color=#ebcaa2>선택한 인격 다음 전투에서 1턴 동안</color> <color=#e30000>파열 10</color><color=#ebcaa2>을 얻음</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_1040301].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#e30000>
   EN: <color=#ebcaa2>The chosen Sinner</color> <color=#ebcaa2>has</color> <color=#e30000>10 Rupture</color> <color=#ebcaa2>for 1 turn in the next battle.</color>
   PL:
89. [Mechanika wydarzeń wyboru [MirrorDungeonAcquireCost] — tekst] <color=#ebcaa2>코스트 {amount} 획득 </color>
   źródło: ChoiceEventEffect.json :: dataList[id=MirrorDungeonAcquireCost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Cost {amount} gained</color>
   PL:
90. [Mechanika wydarzeń wyboru [MirrorDungeonLossCost] — tekst] <color=#ebcaa2>코스트 {amount} 소멸 </color>
   źródło: ChoiceEventEffect.json :: dataList[id=MirrorDungeonLossCost].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>
   EN: <color=#ebcaa2>Cost {amount} lost</color>
   PL:
91. [Mechanika wydarzeń wyboru [Choice_90104001] — tekst] <color=#ebcaa2>다음 전투에서 모든 속성의 <color=#f8c200>E.G.O 자원을 2</color> <color=#ebcaa2>얻고 시작함</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90104001].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, <color=#f8c200>, </color>
   EN: <color=#ebcaa2>Start the next battle with</color> <color=#f8c200>+2 E.G.O resources</color> <color=#ebcaa2>of all affinities</color>
   PL:
92. [Mechanika wydarzeń wyboru [Choice_9010400101] — tekst] <color=#ebcaa2>다음 전투에서 모든 인격이 <color=#f8c200>최종 스킬 위력 2</color> <color=#ebcaa2>증가</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_9010400101].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, <color=#f8c200>, </color>
   EN: <color=#ebcaa2>All allies have</color> <color=#f8c200>+2 Skill Final Power</color> <color=#ebcaa2>for the next battle</color>
   PL:
93. [Mechanika wydarzeń wyboru [Choice_90104002] — tekst] <color=#ebcaa2>다음 전투에서 모든 인격이 <color=#f8c200>스킬 위력 1</color> <color=#ebcaa2>증가</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90104002].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, <color=#f8c200>, </color>
   EN: <color=#ebcaa2>All allies have</color> <color=#f8c200>+1 Skill Power</color> <color=#ebcaa2>for the next battle</color>
   PL:
94. [Mechanika wydarzeń wyboru [Choice_90105801] — tekst] 편성한 모든 인격 레벨 2 증가
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90105801].content
   limit: do 120 znaków
   EN: All Deployed Identities gain 2 Levels
   PL:
95. [Mechanika wydarzeń wyboru [Choice_90106802] — tekst] 편성한 모든 인격 레벨 3 증가
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90106802].content
   limit: do 120 znaków
   EN: All Deployed Identities gain 3 Levels
   PL:
96. [Mechanika wydarzeń wyboru [Choice_90107402] — tekst] 편성한 모든 인격 레벨 2 증가
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90107402].content
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
97. [Mechanika wydarzeń wyboru [Choice_90109101] — tekst] 편성한 모든 인격 레벨 2 증가
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90109101].content
   (powtórzenie elementu 94 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
98. [Mechanika wydarzeń wyboru [Choice_90200502] — tekst] <color=#ebcaa2>판정에 실패한 수감자</color> <color=#e30000>15만큼 체력</color> <color=#ebcaa2>피해</color>, <color=#fe4b48>12만큼 정신력</color> <color=#ebcaa2>피해!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_90200502].content
   (powtórzenie elementu 52 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
99. [Mechanika wydarzeń wyboru [Choice_LoseBattle] — tekst] <color=#ff0000>전투 패배 시, 보상 없음</color>
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_LoseBattle].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>
   EN: <color=#ff0000>No rewards upon Defeat</color>
   PL:
100. [Mechanika wydarzeń wyboru [Choice_EGO901001] — tekst] 전투 승리 시, E.G.O 기프트 "지옥나비의 꿈", "불빛꽃" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901001].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Hellterfly's Dream" & "Ardent Flower"
   PL:
101. [Mechanika wydarzeń wyboru [Choice_EGO901002] — tekst] 전투 승리 시, E.G.O 기프트 "도착증", "경외심" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901002].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Perversion" & "Awe"
   PL:
102. [Mechanika wydarzeń wyboru [Choice_EGO901009] — tekst] 전투 승리 시, E.G.O 기프트 "작열우모", "융해된 파라핀" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901009].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Fiery Down" & "Melted Paraffin"
   PL:
103. [Mechanika wydarzeń wyboru [Choice_EGO901010] — tekst] 전투 승리 시, E.G.O 기프트 "블러디 가젯", "장엄" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901010].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Bloody Gadget" & "Grandeur"
   PL:
104. [Mechanika wydarzeń wyboru [Choice_EGO901011] — tekst] 전투 승리 시, E.G.O 기프트 "여우비", "해진 우산" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901011].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Sunshower" & "Ragged Umbrella"
   PL:
105. [Mechanika wydarzeń wyboru [Choice_EGO901013] — tekst] 전투 승리 시, E.G.O 기프트 "부적 묶음", "낡은 목각 인형" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901013].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Talisman Bundle" & "Old Wooden Doll"
   PL:
106. [Mechanika wydarzeń wyboru [Choice_EGO901014] — tekst] 전투 승리 시, E.G.O 기프트 "녹슨 기념 주화", "울화통" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901014].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Rusty Commemorative Coin" & "Pain of Stifled Rage"
   PL:
107. [Mechanika wydarzeń wyboru [Choice_EGO901016] — tekst] 전투 승리 시, E.G.O 기프트 "초록빛 결실", "시큼한 주향" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901016].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Green Spirit" & "Sour Liquor Aroma"
   PL:
108. [Mechanika wydarzeń wyboru [Choice_EGO901018] — tekst] 전투 승리 시, E.G.O 기프트 "장미 면류관", "안식처" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901018].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Crown of Roses" & "Respite"
   PL:
109. [Mechanika wydarzeń wyboru [Choice_EGO901019] — tekst] 전투 승리 시, E.G.O 기프트 "끈적거리는 진액", "생체 맹독 바이알" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901019].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Sticky Muck" & "Bio-venom Vial"
   PL:
110. [Mechanika wydarzeń wyboru [Choice_EGO901020] — tekst] 전투 승리 시, E.G.O 기프트 "흰 목화", "옭아맨 타래" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901020].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "White Gossypium" & "Tangled Bundle"
   PL:
111. [Mechanika wydarzeń wyboru [Choice_EGO901021] — tekst] 전투 승리 시, E.G.O 기프트 "쪽빛 지포라이터", "순찰용 손전등" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901021].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Blue Zippo Lighter" & "Patrolling Flashlight"
   PL:
112. [Mechanika wydarzeń wyboru [Choice_EGO901024] — tekst] 전투 승리 시, E.G.O 기프트 "녹아내린 눈알", "극독성 외피" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901024].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Melted Eyeball" & "Venomous Skin"
   PL:
113. [Mechanika wydarzeń wyboru [Choice_EGO901031] — tekst] 전투 승리 시, E.G.O 기프트 "닉시 다이버전스", "톱니바퀴 태엽" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901031].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Nixie Divergence" & "Clockwork Spring"
   PL:
114. [Mechanika wydarzeń wyboru [Choice_EGO901033] — tekst] 전투 승리 시, E.G.O 기프트 "근무용 통상 배터리", "제한 풀린 제세동기" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901033].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Standard-duty Battery" & "Uncapped Defibrilator"
   PL:
115. [Mechanika wydarzeń wyboru [Choice_EGO901034] — tekst] 전투 승리 시, E.G.O 기프트 "일점타격논리회로", "무정전 전원장치" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901034].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Pinpoint Logic Circuit" & "UPS System"
   PL:
116. [Mechanika wydarzeń wyboru [Choice_EGO901056] — tekst] 전투 승리 시, E.G.O 기프트 "네잎클로버", "녹빛 겉날개" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901056].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Four-leaf Clover" & "Emerald Elytra"
   PL:
117. [Mechanika wydarzeń wyboru [Choice_EGO901059] — tekst] 전투 승리 시, E.G.O 기프트 "한겨울 밤의 악몽", "고목 함정" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901059].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Midwinter Nightmare" & "Eldtree Snare"
   PL:
118. [Mechanika wydarzeń wyboru [Choice_EGO901073] — tekst] 전투 승리 시, E.G.O 기프트 "엔도르핀 키트", "형광색 램프" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901073].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Endorphin Kit" & "Fluorescent Lamp"
   PL:
119. [Mechanika wydarzeń wyboru [Choice_EGO971029] — tekst] 전투 승리 시, E.G.O 기프트 "E식 차원 단검", "휴대용 역장 배터리" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO971029].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "E-Type Dimensional Dagger" & "Portable Barrier Battery"
   PL:
120. [Mechanika wydarzeń wyboru [GetImmediateConfirmedEgogifts] — tekst] <color=#ebcaa2>E.G.O 기프트 {reward} 획득!</color>
   źródło: ChoiceEventEffect.json :: dataList[id=GetImmediateConfirmedEgogifts].content
   (powtórzenie elementu 34 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
121. [Mechanika wydarzeń wyboru [Choice_EGO901101] — tekst] 전투 승리 시, E.G.O 기프트 "미니어처 전봇대" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901101].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gifts "Miniature Telepole"
   PL:
122. [Mechanika wydarzeń wyboru [Choice_EGO901104] — tekst] 전투 승리 시, E.G.O 기프트 "찢어진 피주머니" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO901104].content
   limit: do 120 znaków
   EN: Win the battle to earn the E.G.O Gift "Ruptured Blood Sac"
   PL:
123. [Mechanika wydarzeń wyboru [Choice_EGO971054] — tekst] 전투 승리 시, E.G.O 기프트 "찰랑이는 연료통" 획득
   źródło: ChoiceEventEffect.json :: dataList[id=Choice_EGO971054].content
   limit: do 120 znaków
   EN: Win the battle to gain E.G.O Gift "Swishing Fuel Tank"
   PL:
124. [Mechanika wydarzeń wyboru [LoseMpOnlyUntilMin] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#fe4b48>정신력 최소치로</color> <color=#ebcaa2>감소</color>
   źródło: ChoiceEventEffect.json :: dataList[id=LoseMpOnlyUntilMin].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#fe4b48>
   EN: <color=#ebcaa2>Reduce</color> <color=#fe4b48>SP to minimum value for</color> <color=#ebcaa2>{conditions}{targets}</color>
   PL:
125. [Mechanika wydarzeń wyboru [ReviveOutOfBattleAndRecoverHpAll] — tekst] 사망한 수감자 부활 및 모든 수감자 <color=#00ff9c>체력 최대로</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=ReviveOutOfBattleAndRecoverHpAll].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#00ff9c>, </color>, <color=#ebcaa2>
   EN: Revive all dead Sinners and <color=#ebcaa2>heal</color> any surviving Sinners <color=#00ff9c>to max HP</color>
   PL:
126. [Mechanika wydarzeń wyboru [RecoverRatioHpOnly] — tekst] <color=#ebcaa2>{conditions}{targets}</color> <color=#00ff9c>최대 체력의 {amount}%만큼 체력</color> <color=#ebcaa2>회복</color>
   źródło: ChoiceEventEffect.json :: dataList[id=RecoverRatioHpOnly].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ebcaa2>, </color>, <color=#00ff9c>
   EN: <color=#ebcaa2>{targets} {conditions}</color> <color=#ebcaa2>healed for</color> <color=#00ff9c>{amount}% of max HP.</color>
   PL:

## Mechanika wydarzeń wyboru: ChoiceEventKeyword
- plik gry: `ChoiceEventKeyword.json`

127. [Mechanika wydarzeń wyboru [EGO_GIFT] — tekst] E.G.O 기프트
   źródło: ChoiceEventKeyword.json :: dataList[id=EGO_GIFT].content
   limit: do 120 znaków
   EN: E.G.O Gift
   PL:
128. [Mechanika wydarzeń wyboru [OnStageStart] — tekst] 스테이지 진입 시
   źródło: ChoiceEventKeyword.json :: dataList[id=OnStageStart].content
   limit: do 120 znaków
   EN: Upon Stage Entry
   PL:
129. [Mechanika wydarzeń wyboru [IncludeSkillAttribute] — tekst] [ATTRIBUTES] 속성 공격 스킬을 보유한
   źródło: ChoiceEventKeyword.json :: dataList[id=IncludeSkillAttribute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ATTRIBUTES]
   EN: with the [ATTRIBUTES] Sin Affinity Attack Skill
   PL:
130. [Mechanika wydarzeń wyboru [NotIncludeSkillAttribute] — tekst] [ATTRIBUTES] 속성 공격 스킬을 보유하지 않은
   źródło: ChoiceEventKeyword.json :: dataList[id=NotIncludeSkillAttribute].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ATTRIBUTES]
   EN: without the [ATTRIBUTES] Sin Affinity Attack Skill
   PL:
131. [Mechanika wydarzeń wyboru [NextBattle] — tekst] 다음 전투에 참여하는
   źródło: ChoiceEventKeyword.json :: dataList[id=NextBattle].content
   limit: do 120 znaków
   EN: participating in the next battle
   PL:
132. [Mechanika wydarzeń wyboru [LowestMp] — tekst] 가장 정신력이 낮은
   źródło: ChoiceEventKeyword.json :: dataList[id=LowestMp].content
   limit: do 120 znaków
   EN: with the lowest SP
   PL:
133. [Mechanika wydarzeń wyboru [FAILURE] — tekst] 판정에 실패한
   źródło: ChoiceEventKeyword.json :: dataList[id=FAILURE].content
   limit: do 120 znaków
   EN: that failed the Check
   PL:
134. [Mechanika wydarzeń wyboru [SUCCESS] — tekst] 판정에 성공한
   źródło: ChoiceEventKeyword.json :: dataList[id=SUCCESS].content
   limit: do 120 znaków
   EN: that passed the Check
   PL:
135. [Mechanika wydarzeń wyboru [ADD] — tekst] 더하기
   źródło: ChoiceEventKeyword.json :: dataList[id=ADD].content
   limit: do 120 znaków
   EN: Add
   PL:
136. [Mechanika wydarzeń wyboru [SUB] — tekst] 빼기
   źródło: ChoiceEventKeyword.json :: dataList[id=SUB].content
   limit: do 120 znaków
   EN: Subtract
   PL:
137. [Mechanika wydarzeń wyboru [85560101CRIMSON] — tekst] 붉은
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101CRIMSON].content
   limit: do 120 znaków
   EN: Crimson
   PL:
138. [Mechanika wydarzeń wyboru [85560101SCARLET] — tekst] 주홍
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101SCARLET].content
   limit: do 120 znaków
   EN: Scarlet
   PL:
139. [Mechanika wydarzeń wyboru [85560101AMBER] — tekst] 노란
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101AMBER].content
   limit: do 120 znaków
   EN: Amber
   PL:
140. [Mechanika wydarzeń wyboru [85560101SHAMROCK] — tekst] 푸른
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101SHAMROCK].content
   limit: do 120 znaków
   EN: Shamrock
   PL:
141. [Mechanika wydarzeń wyboru [85560101AZURE] — tekst] 새파란
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101AZURE].content
   limit: do 120 znaków
   EN: Azure
   PL:
142. [Mechanika wydarzeń wyboru [85560101INDIGO] — tekst] 쪽빛
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101INDIGO].content
   limit: do 120 znaków
   EN: Indigo?
   PL:
143. [Mechanika wydarzeń wyboru [85560101VIOLET] — tekst] 보랏빛
   źródło: ChoiceEventKeyword.json :: dataList[id=85560101VIOLET].content
   limit: do 120 znaków
   EN: Violet
   PL:

## Mechanika wydarzeń wyboru: ChoiceEventTarget
- plik gry: `ChoiceEventTarget.json`

144. [Mechanika wydarzeń wyboru [Ally] — tekst] 아군
   źródło: ChoiceEventTarget.json :: dataList[id=Ally].content
   limit: do 120 znaków
   EN: Friendly Units
   PL:
145. [Mechanika wydarzeń wyboru [RandomAlly] — tekst] 무작위 아군
   źródło: ChoiceEventTarget.json :: dataList[id=RandomAlly].content
   limit: do 120 znaków
   EN: Random Friendly Units
   PL:
146. [Mechanika wydarzeń wyboru [EveryAlly] — tekst] 모든 아군
   źródło: ChoiceEventTarget.json :: dataList[id=EveryAlly].content
   limit: do 120 znaków
   EN: All Allies
   PL:
147. [Mechanika wydarzeń wyboru [EveryEnemy] — tekst] 모든 적군
   źródło: ChoiceEventTarget.json :: dataList[id=EveryEnemy].content
   limit: do 120 znaków
   EN: All Enemies
   PL:
148. [Mechanika wydarzeń wyboru [ChosenPersonality] — tekst] 선택한 인격
   źródło: ChoiceEventTarget.json :: dataList[id=ChosenPersonality].content
   limit: do 120 znaków
   EN: The Selected Identity
   PL:
149. [Mechanika wydarzeń wyboru [HighestHpAlly] — tekst] 체력이 높은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=HighestHpAlly].content
   limit: do 120 znaków
   EN: Friendly Units with the most HP
   PL:
150. [Mechanika wydarzeń wyboru [LowestHpAlly] — tekst] 체력이 낮은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=LowestHpAlly].content
   limit: do 120 znaków
   EN: Friendly Units with the least HP
   PL:
151. [Mechanika wydarzeń wyboru [HighestMpAlly] — tekst] 정신력이 높은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=HighestMpAlly].content
   limit: do 120 znaków
   EN: Friendly Units with the highest SP
   PL:
152. [Mechanika wydarzeń wyboru [LowestMpAlly] — tekst] 정신력이 낮은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=LowestMpAlly].content
   limit: do 120 znaków
   EN: Friendly Units with the lowest SP
   PL:
153. [Mechanika wydarzeń wyboru [NotFullHpAlly] — tekst] 최대 체력이 아닌 아군
   źródło: ChoiceEventTarget.json :: dataList[id=NotFullHpAlly].content
   limit: do 120 znaków
   EN: Friendly Units whose HP is not full
   PL:
154. [Mechanika wydarzeń wyboru [NotAffectedAlly] — tekst] 이전 효과들의 영향을 받지 않은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=NotAffectedAlly].content
   limit: do 120 znaków
   EN: Allies unaffected by previous effects
   PL:
155. [Mechanika wydarzeń wyboru [LowestHpRatioAlly] — tekst] 현재 체력 비율이 가장 낮은 아군
   źródło: ChoiceEventTarget.json :: dataList[id=LowestHpRatioAlly].content
   limit: do 120 znaków
   EN: Ally with the lowest HP percentage
   PL:
156. [Mechanika wydarzeń wyboru [Every] — tekst] 모든
   źródło: ChoiceEventTarget.json :: dataList[id=Every].content
   limit: do 120 znaków
   EN: All
   PL:

## Mechanika wydarzeń wyboru: ChoiceEventUI
- plik gry: `ChoiceEventUI.json`

157. [Mechanika wydarzeń wyboru [event_judgement_above] — tekst] <color=#f8c200>유리</color> 판정
   źródło: ChoiceEventUI.json :: dataList[id=event_judgement_above].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#f8c200>, </color>
   EN: <color=#f8c200>Advantage</color>
   PL:
158. [Mechanika wydarzeń wyboru [event_judgement_below] — tekst] <color=#e30000>불리</color> 판정
   źródło: ChoiceEventUI.json :: dataList[id=event_judgement_below].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#e30000>, </color>
   EN: <color=#e30000>Disadvantage</color>
   PL:
159. [Mechanika wydarzeń wyboru [event_select_personality_to_proceed_judgement] — tekst] 판정을 진행할 인격을 선택하세요.
   źródło: ChoiceEventUI.json :: dataList[id=event_select_personality_to_proceed_judgement].content
   limit: do 120 znaków
   EN: Choose an Identity to perform the check with:
   PL:
160. [Mechanika wydarzeń wyboru [event_expected_success_rate_format] — tekst] 예상 확률 : {0}
   źródło: ChoiceEventUI.json :: dataList[id=event_expected_success_rate_format].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Predicted Odds: {0}
   PL:
161. [Mechanika wydarzeń wyboru [all_attribute] — tekst] 모든 속성
   źródło: ChoiceEventUI.json :: dataList[id=all_attribute].content
   limit: do 120 znaków
   EN: All Affinities
   PL:

## Jednostka wsparcia: Assist-a1c10p2
- plik gry: `Assist-a1c10p2.json`

162. [Jednostka wsparcia [400041] — nazwa] 뿌이
   źródło: Assist-a1c10p2.json :: dataList[id=400041].name
   limit: do 40 znaków
   EN: Pwie
   PL:
163. [Jednostka wsparcia [400042] — nazwa] 뿌이
   źródło: Assist-a1c10p2.json :: dataList[id=400042].name
   (powtórzenie elementu 162 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Jednostka wsparcia: Assist-a1c7p2
- plik gry: `Assist-a1c7p2.json`

164. [Jednostka wsparcia [400001] — nazwa] 가시춘
   źródło: Assist-a1c7p2.json :: dataList[id=400001].name
   limit: do 40 znaków
   EN: Jia Xichun
   PL:

## Jednostka wsparcia: Assist-a1c8p2
- plik gry: `Assist-a1c8p2.json`

165. [Jednostka wsparcia [400002] — nazwa] 임대옥
   źródło: Assist-a1c8p2.json :: dataList[id=400002].name
   limit: do 40 znaków
   EN: Lin Daiyu
   PL:
166. [Jednostka wsparcia [400002] — opis] 어시스트 이름
   źródło: Assist-a1c8p2.json :: dataList[id=400002].desc
   limit: do 120 znaków
   EN: Assist Unit Name
   PL:

## Jednostka wsparcia: Assist-a1c9p2
- plik gry: `Assist-a1c9p2.json`

167. [Jednostka wsparcia [400006] — nazwa] 베스파
   źródło: Assist-a1c9p2.json :: dataList[id=400006].name
   limit: do 40 znaków
   EN: Vespa
   PL:
168. [Jednostka wsparcia [400006] — opis] 어시스트 이름
   źródło: Assist-a1c9p2.json :: dataList[id=400006].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
169. [Jednostka wsparcia [40000601] — nazwa] 몸통
   źródło: Assist-a1c9p2.json :: dataList[id=40000601].name
   limit: do 40 znaków
   EN: Body
   PL:
170. [Jednostka wsparcia [40000601] — opis] 베스파 부위
   źródło: Assist-a1c9p2.json :: dataList[id=40000601].desc
   limit: do 120 znaków
   EN: Vespa Part
   PL:

## Jednostka wsparcia: Assist-a1c9p3
- plik gry: `Assist-a1c9p3.json`

171. [Jednostka wsparcia [400009] — nazwa] 베스파
   źródło: Assist-a1c9p3.json :: dataList[id=400009].name
   (powtórzenie elementu 167 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
172. [Jednostka wsparcia [400009] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400009].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
173. [Jednostka wsparcia [40000901] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40000901].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
174. [Jednostka wsparcia [40000901] — opis] 베스파 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40000901].desc
   (powtórzenie elementu 170 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
175. [Jednostka wsparcia [400010] — nazwa] 모제스
   źródło: Assist-a1c9p3.json :: dataList[id=400010].name
   limit: do 40 znaków
   EN: Moses
   PL:
176. [Jednostka wsparcia [400010] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400010].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
177. [Jednostka wsparcia [40001001] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40001001].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
178. [Jednostka wsparcia [40001001] — opis] 모제스 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40001001].desc
   limit: do 120 znaków
   EN: Moses Part
   PL:
179. [Jednostka wsparcia [400011] — nazwa] 에즈라
   źródło: Assist-a1c9p3.json :: dataList[id=400011].name
   limit: do 40 znaków
   EN: Ezra
   PL:
180. [Jednostka wsparcia [400011] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400011].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
181. [Jednostka wsparcia [40001101] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40001101].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
182. [Jednostka wsparcia [40001101] — opis] 에즈라 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40001101].desc
   limit: do 120 znaków
   EN: Ezra Part
   PL:
183. [Jednostka wsparcia [400007] — nazwa] LCE E.G.O::홍염살 알리사
   źródło: Assist-a1c9p3.json :: dataList[id=400007].name
   limit: do 50 znaków
   EN: LCE E.G.O::Ardor Blossom Star Alyssa
   PL:
184. [Jednostka wsparcia [400007] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400007].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
185. [Jednostka wsparcia [40000701] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40000701].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
186. [Jednostka wsparcia [40000701] — opis] 알리사 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40000701].desc
   limit: do 120 znaków
   EN: Alyssa Part
   PL:
187. [Jednostka wsparcia [400008] — nazwa] 로보토미 E.G.O::램프 호엔하임
   źródło: Assist-a1c9p3.json :: dataList[id=400008].name
   limit: do 50 znaków
   EN: Lobotomy E.G.O::Lamp Hohenheim
   PL:
188. [Jednostka wsparcia [400008] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400008].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
189. [Jednostka wsparcia [40000801] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40000801].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
190. [Jednostka wsparcia [40000801] — opis] 호엔하임 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40000801].desc
   limit: do 120 znaków
   EN: Hohenheim Part
   PL:
191. [Jednostka wsparcia [400013] — nazwa] 어느 싱클레어
   źródło: Assist-a1c9p3.json :: dataList[id=400013].name
   limit: do 40 znaków
   EN: A Certain Sinclair
   PL:
192. [Jednostka wsparcia [400013] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400013].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
193. [Jednostka wsparcia [40001301] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40001301].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
194. [Jednostka wsparcia [40001301] — opis] 각성 싱클레어 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40001301].desc
   limit: do 120 znaków
   EN: A Certain Sinclair Part
   PL:
195. [Jednostka wsparcia [400015] — nazwa] 무아 료슈
   źródło: Assist-a1c9p3.json :: dataList[id=400015].name
   limit: do 40 znaków
   EN: Muga Ryōshū
   PL:
196. [Jednostka wsparcia [400015] — opis] 어시스트 이름
   źródło: Assist-a1c9p3.json :: dataList[id=400015].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
197. [Jednostka wsparcia [40001501] — nazwa] 몸통
   źródło: Assist-a1c9p3.json :: dataList[id=40001501].name
   (powtórzenie elementu 169 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
198. [Jednostka wsparcia [40001501] — opis] 료슈 부위
   źródło: Assist-a1c9p3.json :: dataList[id=40001501].desc
   limit: do 120 znaków
   EN: Ryōshū Part
   PL:

## Jednostka wsparcia: Assist-exme
- plik gry: `Assist-exme.json`

199. [Jednostka wsparcia [400038] — nazwa] 앵두
   źródło: Assist-exme.json :: dataList[id=400038].name
   limit: do 40 znaków
   EN: Aeng-du
   PL:
200. [Jednostka wsparcia [400038] — opis] 어시스트 이름
   źródło: Assist-exme.json :: dataList[id=400038].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
201. [Jednostka wsparcia [400040] — nazwa] 김삿갓
   źródło: Assist-exme.json :: dataList[id=400040].name
   limit: do 40 znaków
   EN: Bamboo-hatted Kim
   PL:
202. [Jednostka wsparcia [400040] — opis] 어시스트 이름
   źródło: Assist-exme.json :: dataList[id=400040].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
203. [Jednostka wsparcia [1460] — nazwa] 섬광 현상 - 영사기
   źródło: Assist-exme.json :: dataList[id=1460].name
   limit: do 40 znaków
   EN: Flash Phenomenon - Projector
   PL:
204. [Jednostka wsparcia [1460] — opis] 적 어시스트 이름
   źródło: Assist-exme.json :: dataList[id=1460].desc
   limit: do 120 znaków
   EN: Enemy Assist Unit Name
   PL:

## Jednostka wsparcia: Assist-twth
- plik gry: `Assist-twth.json`

205. [Jednostka wsparcia [400037] — nazwa] 키라
   źródło: Assist-twth.json :: dataList[id=400037].name
   limit: do 40 znaków
   EN: Kira
   PL:

## Jednostka wsparcia: Assist-walpu6
- plik gry: `Assist-walpu6.json`

206. [Jednostka wsparcia [400003] — nazwa] 마법소녀
   źródło: Assist-walpu6.json :: dataList[id=400003].name
   limit: do 40 znaków
   EN: Magical Girl
   PL:
207. [Jednostka wsparcia [400003] — opis] 어시스트 이름
   źródło: Assist-walpu6.json :: dataList[id=400003].desc
   (powtórzenie elementu 166 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Jednostka wsparcia: Passives_Assist-Cultivation
- plik gry: `Passives_Assist-Cultivation.json`

208. [Jednostka wsparcia [940000501] — nazwa] 내면의 자신
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000501].name
   limit: do 40 znaków
   EN: The Inner Self
   PL:
209. [Jednostka wsparcia [940000501] — opis] 3턴부터 매 턴 시작시 마다 [AttackUp] 2 얻음
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000501].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Starting from Turn 3: gain 2 [AttackUp] at every Turn Start
   PL:
210. [Jednostka wsparcia [940000502] — nazwa] 알아가는 지식
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000502].name
   limit: do 40 znaków
   EN: Widening Knowledge
   PL:
211. [Jednostka wsparcia [940000502] — opis] 자신의 공격 시작 전 해당 적의 타격 내성 +1.0 (스킬 종료 시 초기화)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000502].desc
   limit: do 120 znaków
   EN: Before Attack: the targeted enemy gains +1 Blunt Resist. (resets after Skill ends)
   PL:
212. [Jednostka wsparcia [940000503] — nazwa] 해결사 정신
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000503].name
   limit: do 40 znaków
   EN: Spirit of Fixers
   PL:
213. [Jednostka wsparcia [940000503] — opis] 자신의 흐트러짐 구간 중 첫번째 흐트러짐 구간 삭제\n피격 시 [Protection] 1, [AttackUp] 1 얻음, 정신력 3 회복 (턴 당 1회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000503].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Protection], [AttackUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Remove the first Stagger Threshold from this unit\nWhen hit, gain 1 [Protection], 1 [AttackUp], and heal 3 SP (once per turn)
   PL:
214. [Jednostka wsparcia [940000504] — nazwa] 천애검
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000504].name
   limit: do 40 znaków
   EN: The Tianya Sword
   PL:
215. [Jednostka wsparcia [940000504] — opis] 턴 종료 시 자신의 [Breath] 위력이 15 이상이면, [Breath] 위력이 절반으로 감소하고 아래 효과 발동\n자신을 포함한 모든 아군의 체력을 10 회복\n자신을 포함한 모든 아군의 정신력 3 회복\n- 자신을 포함한 모든 아군의 해제 가능한 부정적인 효과를 절반으로 감소
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000504].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn End: at 15+ [Breath] Potency, halve [Breath] Potency and gain the following effects:\n- All allies, including this unit, heal 10 HP\n- All allies, including this unit, heal 3 SP\n- Halve all removable negative effects from all allies, including this unit
   PL:
216. [Jednostka wsparcia [940000505] — nazwa] 전쟁을 대비하는 법
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000505].name
   limit: do 40 znaków
   EN: How to Prepare for War
   PL:
217. [Jednostka wsparcia [940000505] — opis] 스테이지 시작 시 자신의 정신력 10 회복, [AttackUp] 2, [DefenseUp] 2 얻음
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000505].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Encounter Start: heals 10 SP, gain 2 [AttackUp], and 2 [DefenseUp]
   PL:
218. [Jednostka wsparcia [940000506] — nazwa] 살아남는 법
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000506].name
   limit: do 40 znaków
   EN: How to Survive
   PL:
219. [Jednostka wsparcia [940000506] — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨. (전투 당 1회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000506].desc
   limit: do 230 znaków
   EN: In this Encounter, when this unit takes damage that brings their HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn. (once per Encounter)
   PL:
220. [Jednostka wsparcia [940000507] — nazwa] 무감정대응
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000507].name
   limit: do 40 znaków
   EN: Apathetic Response
   PL:
221. [Jednostka wsparcia [940000507] — opis] 자신을 제외한 아군 피격 시 [AttackUp] 1 얻고, 다음 턴에 [Agility] 2 얻음 (턴 당 1회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000507].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [Agility]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Agility] = 신속 / Haste
   EN: When other allies are hit, gain 1 [AttackUp]; then, gain 2 [Agility] next turn (once per turn)
   PL:
222. [Jednostka wsparcia [940000508] — nazwa] 포로 고문 기술
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000508].name
   limit: do 40 znaków
   EN: POW Torture Technique
   PL:
223. [Jednostka wsparcia [940000508] — opis] 공격 적중 시 대상에게 [Binding] 또는 [Laceration] 이 있으면, 다음 턴에 합 위력 증가 1 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000508].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [Binding], [Laceration]
   znaczenie tagów: [Binding] = 속박 / Bind; [Laceration] = 출혈 / Bleed
   EN: On Hit: if target has [Binding] or [Laceration], gain 1 Clash Power Up next turn (2 times per turn)
   PL:
224. [Jednostka wsparcia [940000509] — nazwa] 상대를 달래주는 마음
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000509].name
   limit: do 40 znaków
   EN: The Reassuring Heart
   PL:
225. [Jednostka wsparcia [940000509] — opis] 턴 시작 시 자신을 포함한 모든 아군의 정신력을 5 회복\n 전투 시작 시 메인 타겟의 정신력이 자신보다 같거나 높다면 [Protection] 1 얻음 (턴 당 1회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000509].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Turn Start: all allies, including this unit, heals 5 SP\nCombat Start: if the main target's SP is equal to or higher than this unit's, gain 1 [Protection] (once per turn)
   PL:
226. [Jednostka wsparcia [940000510] — nazwa] 도신
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000510].name
   limit: do 40 znaków
   EN: God of Gamblers
   PL:
227. [Jednostka wsparcia [940000510] — opis] 모든 코인이 파괴되지 않고 합 승리 후 공격 시 적중에 관계 없이 해당 스킬의 마지막 코인까지 모든 코인이 앞면이었으면, 마지막 코인의 피해량 +30%
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000510].desc
   limit: do 240 znaków
   EN: On Clash Win without losing any Coins: regardless of whether they hit or not, if every Coin flipped by that Skill, down to the final Coin, flipped heads, the final Coin deals +30% damage
   PL:
228. [Jednostka wsparcia [940000511] — nazwa] 짝꿍이자 라이벌
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000511].name
   limit: do 40 znaków
   EN: My Bestie and a Rival
   PL:
229. [Jednostka wsparcia [940000511] — opis] 턴 시작 시 싱클레어 수감자가 전투에 참여 중이면, 자신과 싱클레어가 [AttackUp] 2 , [DefenseUp] 2 얻음 (대기 인원 제외)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000511].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: if Sinner Sinclair is participating in this battle, this unit and Sinclair both gain 2 [AttackUp] and 2 [DefenseUp] (does not count if he is a Backup Unit)
   PL:
230. [Jednostka wsparcia [940000512] — nazwa] 홍원의 가주
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000512].name
   limit: do 40 znaków
   EN: The Hierarch of Hongyuan
   PL:
231. [Jednostka wsparcia [940000512] — opis] 턴 시작 시 자신을 포함한 모든 아군에게 [DefenseUp] 1 부여
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000512].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: apply 1 [DefenseUp] to all allies, including this unit
   PL:
232. [Jednostka wsparcia [940000513] — nazwa] 홍원의 가주
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000513].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
233. [Jednostka wsparcia [940000513] — opis] 턴 시작 시 자신을 포함한 모든 아군에게 [AttackUp] 1, [DefenseUp] 1 부여
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000513].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: apply 1 [AttackUp] and 1 [DefenseUp] to all allies, including this unit
   PL:
234. [Jednostka wsparcia [940000514] — nazwa] 홍원의 가주
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000514].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
235. [Jednostka wsparcia [940000514] — opis] 턴 시작 시 자신을 포함한 모든 아군에게 [AttackUp] 2, [DefenseUp] 2 부여
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000514].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: apply 2 [AttackUp] and 2 [DefenseUp] to all allies, including this unit
   PL:
236. [Jednostka wsparcia [940000515] — nazwa] 홍원의 가주
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000515].name
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
237. [Jednostka wsparcia [940000515] — opis] 턴 시작 시 자신을 포함한 모든 아군에게 [AttackUp] 3, [DefenseUp] 3 부여
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000515].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: apply 3 [AttackUp] and 3 [DefenseUp] to all allies, including this unit
   PL:
238. [Jednostka wsparcia [940000516] — nazwa] 금강환단
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000516].name
   limit: do 40 znaków
   EN: Jin Gang Bolus
   PL:
239. [Jednostka wsparcia [940000516] — opis] 합 패배 시, [Protection] 1, [DefenseUp] 3 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000516].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: On Clash Lose, gain 1 [Protection] and 3 [DefenseUp] (2 times per turn)
   PL:
240. [Jednostka wsparcia [940000517] — nazwa] 금강환단
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000517].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
241. [Jednostka wsparcia [940000517] — opis] 합 패배 시, [Protection] 1 , [AttackUp] 1, [DefenseUp] 3 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000517].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection], [AttackUp], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: On Clash Lose, gain 1 [Protection], 1 [AttackUp], and 3 [DefenseUp] (2 times per turn)
   PL:
242. [Jednostka wsparcia [940000518] — nazwa] 금강환단
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000518].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
243. [Jednostka wsparcia [940000518] — opis] 합 패배 시, [Protection] 2, [AttackUp] 1 , [DefenseUp] 3 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000518].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection], [AttackUp], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: On Clash Lose, gain 2 [Protection], 1 [AttackUp], and 3 [DefenseUp] (2 times per turn)
   PL:
244. [Jednostka wsparcia [940000519] — nazwa] 금강환단
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000519].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
245. [Jednostka wsparcia [940000519] — opis] 합 패배 시, [Protection] 2, [AttackUp] 1 , [DefenseUp] 4 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000519].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection], [AttackUp], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: On Clash Lose, gain 2 [Protection], 1 [AttackUp], and 4 [DefenseUp] (2 times per turn)
   PL:
246. [Jednostka wsparcia [940000520] — nazwa] 금강환단
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000520].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
247. [Jednostka wsparcia [940000520] — opis] 합 패배 시, [Protection] 3, [AttackUp] 1 , [DefenseUp] 4 얻음 (턴 당 2회)
   źródło: Passives_Assist-Cultivation.json :: dataList[id=940000520].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection], [AttackUp], [DefenseUp]
   znaczenie tagów: [Protection] = 보호 / Protection; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: On Clash Lose, gain 3 [Protection], 1 [AttackUp], and 4 [DefenseUp] (2 times per turn)
   PL:

## Jednostka wsparcia: Passives_Assist-a1c10p2
- plik gry: `Passives_Assist-a1c10p2.json`

248. [Jednostka wsparcia [40004101] — nazwa] 어린 붉은 신
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004101].name
   limit: do 40 znaków
   EN: The Nascent Crimson God
   PL:
249. [Jednostka wsparcia [40004101] — opis] [Charge] 효과를 얻을 때, 대신 [ChargeRouge] 얻음\n\n스테이지 시작 시 [ChargeRouge] 위력 1 얻음\n\n턴 시작 시 자신의 [ChargeRouge] 위력이 2 이상이면, (자신의 [ChargeRouge] 위력 x 2)만큼 자신의 [ChargeRouge] 횟수 증가
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004101].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [Charge], [ChargeRouge]
   znaczenie tagów: [Charge] = 충전 / Charge; [ChargeRouge] = 맥동 / Pulsation
   EN: When this unit gains [Charge], gains [ChargeRouge] instead\n\nEncounter Start: Gain 1 [ChargeRouge] Potency\n\nTurn Start: At 2+ [ChargeRouge] Potency, gain +([ChargeRouge] Potency x 2) [ChargeRouge] Count
   PL:
250. [Jednostka wsparcia [40004101] — podsumowanie] [ChargeRouge] 얻음
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004101].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Gain [ChargeRouge]
   PL:
251. [Jednostka wsparcia [40004101] — tekst klimatyczny] 어리지만 분명 신격을 가졌다.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004101].flavor
   limit: do 120 znaków
   EN: A young god, but a god nonetheless.
   PL:
252. [Jednostka wsparcia [40004102] — nazwa] 맥동하는 본성
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004102].name
   limit: do 40 znaków
   EN: Pulsating Nature
   PL:
253. [Jednostka wsparcia [40004102] — opis] 전투에서 [Laceration] 효과가 발동할 때마다 자신의 [ChargeRouge] 횟수 1 증가
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004102].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [ChargeRouge]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation
   EN: Gain +1 [ChargeRouge] Count every time [Laceration] effect is activated in an Encounter
   PL:
254. [Jednostka wsparcia [40004102] — podsumowanie] [ChargeRouge] 횟수 증가
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004102].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Gain [ChargeRouge] Count
   PL:
255. [Jednostka wsparcia [40004102] — tekst klimatyczny] 왜 피를 볼때마다 내 심장이 자꾸 뛰는거야…?
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004102].flavor
   limit: do 120 znaków
   EN: Why... does blood make my heart rush so excitedly?
   PL:
256. [Jednostka wsparcia [40004103] — nazwa] 여정
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004103].name
   limit: do 40 znaków
   EN: The Adventure
   PL:
257. [Jednostka wsparcia [40004103] — opis] 자신의 [ChargeRouge] 위력에 따라 다음 효과를 전부 얻음\n- 1 : 자신의 [ChargeRouge] 횟수 1당, 가하는 피해량 +2% (최대 20%), 대상의 체력 회복량 +10% (최대 100%, 소수점 버림)\n- 2 : 자신의 [ChargeRouge] 위력 2당, 기본 위력 +1\n- 3 : 턴 시작 시 자신에게 [GourmandiseAlly] 효과가 없고 자신의 [ChargeRouge] 횟수가 15 이상이면, [ChargeRouge] 횟수를 모두 소모하고 [GourmandiseAlly] 3 얻음\n- 4 : 스킬 슬롯 수 +1\n- 5 : 스테이지 시작 시 [GourmandiseAlly] 3을 얻고 모든 적에게 [BloodyMucusAlly] 3 부여
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004103].desc
   limit: do 680 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [GourmandiseAlly], [BloodyMucusAlly]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [GourmandiseAlly] = 폭주 / Uncontrollable Rampage; [BloodyMucusAlly] = 세례[적] / Baptism [Crimson]
   EN: Gain the following effects based on [ChargeRouge] Potency on self\n- 1+: For every [ChargeRouge] Count, deal +2% damage and heal +10% HP on target (max 20%, 100% respectively; rounded down)\n- 2+: Base Power +1 for every 2 [ChargeRouge] Potency on self\n- 3+: Turn Start: If this unit does not have [GourmandiseAlly], and if this unit has 15+ [ChargeRouge] Count, consume all [ChargeRouge] Count and gain 3 [GourmandiseAlly]\n- 4+: Skill Slot +1\n- 5+: Encounter Start: Gain 3 [GourmandiseAlly] and inflict 3 [BloodyMucusAlly] on all enemies
   PL:
258. [Jednostka wsparcia [40004103] — podsumowanie] 자신의 [ChargeRouge] 위력에 따라 강화됨
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004103].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ChargeRouge]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation
   EN: Effect enhanced based on [ChargeRouge] Potency on self
   PL:
259. [Jednostka wsparcia [40004103] — tekst klimatyczny] 그들의 등 뒤를 보며 한 걸음 한 걸음 세상을, 백화점을 알아간다. 그리고 자신에 대한 것도. 자신의 육체 중 눈만이 가장 또렷하고 자연스러웠기에.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004103].flavor
   limit: do 290 znaków
   EN: With every step they take, toddling from behind their first guardians, the child learns about the world, about the department store... and themself, for their eyes were the clearest and the most natural part of their body.
   PL:
260. [Jednostka wsparcia [40004104] — nazwa] 도움의 손길
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004104].name
   limit: do 40 znaków
   EN: A Helping Hand
   PL:
261. [Jednostka wsparcia [40004104] — opis] 전투 중 아군이 흐트러짐 상태가 되면, 그 아군에게 '내 손 잡아' 사용 (턴당 2회)
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004104].desc
   limit: do 140 znaków
   EN: When an ally is Staggered during an Encounter, use "Grab My Hand" on the said ally (2 times per turn)
   PL:
262. [Jednostka wsparcia [40004105] — nazwa] 주체되지 않는 몸
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004105].name
   limit: do 40 znaków
   EN: Body Out of Control
   PL:
263. [Jednostka wsparcia [40004105] — opis] 자신에게 [GourmandiseAlly] 효과가 있으면 다음 효과를 얻음\n- 가하는 피해량의 20% 만큼 체력 회복\n- 스킬 사용 시 자신의 [Laceration] 횟수 3 증가\n- 스킬 적중 시 [Laceration] 1 얻음
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004105].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [GourmandiseAlly], [Laceration]
   znaczenie tagów: [GourmandiseAlly] = 폭주 / Uncontrollable Rampage; [Laceration] = 출혈 / Bleed
   EN: If this unit has [GourmandiseAlly], gain the following effects:\n- Heal HP equal to 20% of damage dealt\n- On Skill Use, gain +3 [Laceration] Count\n- On Hit using a Skill, gain 1 [Laceration]
   PL:
264. [Jednostka wsparcia [40004105] — podsumowanie] [Laceration] 1 얻음
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004105].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Gain 1 [Laceration]
   PL:
265. [Jednostka wsparcia [40004105] — tekst klimatyczny] 팔과 다리 모든게 낯설지만 안에서부터 시작된 미약한 고동은 점차 미칠듯 맥동하려고만 한다.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004105].flavor
   limit: do 200 znaków
   EN: Though the arms, legs, and everything else about their body feels alien to the child, the faint beating from their core will soon begin its mad pulsation.
   PL:
266. [Jednostka wsparcia [40004107] — nazwa] 가죽 봉제 못
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004107].name
   limit: do 40 znaków
   EN: Leather-sewing Nail
   PL:
267. [Jednostka wsparcia [40004107] — opis] 공격 스킬로 적을 처치하지 못했을 때, 해당 적에게 '내가 끝내줄게…' 사용 (턴당 1회)
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004107].desc
   limit: do 170 znaków
   EN: When this unit fails to defeat an enemy using its Attack Skills, use "I'll End It for You..." on the said enemy (once per turn)
   PL:
268. [Jednostka wsparcia [40004107] — tekst klimatyczny] 가죽을 꿰메기 위해서는 뾰족하기만하지 않은 굵고 튼튼한 못이 필요하댔어. 그렇게해도 뚫리지 않는다면 한번 더..!
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004107].flavor
   limit: do 170 znaków
   EN: They said I needed a thick, sturdy nail to punch through leather for sewing. If that didn't work, I just need to try again...!
   PL:
269. [Jednostka wsparcia [40004108] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004108].name
   limit: do 40 znaków
   EN: Fate Lost
   PL:
270. [Jednostka wsparcia [40004108] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004108].desc
   limit: do 120 znaków
   EN: Lose this Encounter if this unit is killed
   PL:
271. [Jednostka wsparcia [40004108] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004108].flavor
   limit: do 160 znaków
   EN: One may get lost and wander onto the wrong path, but willful defiance or deviation from the flow are forbidden by "it."
   PL:
272. [Jednostka wsparcia [40004202] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004202].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
273. [Jednostka wsparcia [40004202] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004202].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
274. [Jednostka wsparcia [40004202] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004202].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
275. [Jednostka wsparcia [40004203] — nazwa] 르 비스쾨아브젝트(le Visqueux-Abject)
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004203].name
   limit: do 50 znaków
   EN: Le Visqueux-Abject
   PL:
276. [Jednostka wsparcia [40004203] — opis] 이 유닛은 자신을 메인 타겟으로 지정한 스킬의 피해만 적용되며, 그 외의 피해를 받지 않음\n\n전투에 처음 등장할 때, 전장에 [BuffetField] 생성\n\n턴 시작 시 [BuffetField] 범위 안의 대상에게 다음 효과가 적용됨\n- 아군 (자신 포함)\n· 최대 체력의 5%만큼 체력 회복\n· [Charge] 횟수 4 증가\n· [Protection] 1 부여\n· 대상 아군이 르루주 소속이면, [Enhancement] 2 부여\n· E.G.O 스킬 피해량 +50%\n\n- 적\n· [AttackDown] 3 부여\n· [DefenseDown] 3 부여\n· [BloodyMucusAlly] 2 부여
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004203].desc
   limit: do 690 znaków
   tokeny: zachowaj dokładnie: \n, [BuffetField], [Charge], [Protection], [Enhancement], [AttackDown], [DefenseDown], [BloodyMucusAlly]
   znaczenie tagów: [BuffetField] = 르 보미스망 (Le Vomissement) / Le Vomissement; [Charge] = 충전 / Charge; [Protection] = 보호 / Protection; [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [BloodyMucusAlly] = 세례[적] / Baptism [Crimson]
   EN: This unit takes damage only from Skills mainly targeting this unit, and it takes no other damage\n\nUpon entering the Encounter for the first time, generate [BuffetField] on the field\n\nTurn Start: Targets within the [BuffetField] gain the following effects:\n- Allies (including this unit)\n  · Heal 5% HP\n  · Gain +4 [Charge] Count\n  · Gain 1 [Protection]\n  · If the affected ally is a "Le Rouge" unit, gain 2 [Enhancement]\n  · E.G.O Skills deal +50% damage\n\n- Enemies\n  · Gain 3 [AttackDown]\n  · Gain 3 [DefenseDown]\n  · Gain 2 [BloodyMucusAlly]
   PL:
277. [Jednostka wsparcia [40004203] — tekst klimatyczny] 붉은신은 눈앞의 것을 섭취하고 섭취한다. 그 결과 점막질의 지대가 펼쳐진다. 그것은 섭취의 결과물. 나에게서 나왔지만 내것인지 아닌지의 경계가 흐려지는 비체이자 끈적임. 이 위에서 나의 것은 맥동하고, 아닌것은 녹아내린다. 경계 밖의 것은 공포스럽기에.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004203].flavor
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: In an endless feast, the Crimson God consumes and consumes; what is devoured is then digested and excreted as a field of mucus around them.\nThis is the outcome of consumption, where the distinction between self and other blurs. Is this phlegmatic discharge a part of me, or is it of another? Within this boundary, all that is mine pulsates, while all that is not disintegrates.\n\nFor I am afraid of what lies outside the periphery.
   PL:
278. [Jednostka wsparcia [40004204] — nazwa] 라 팽 드 랑팡스(La Fin de l'enfance)
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004204].name
   limit: do 50 znaków
   EN: La Fin de l'Enfance
   PL:
279. [Jednostka wsparcia [40004204] — opis] 스테이지 시작시, [ChargeRouge] 위력 5 얻음\n\n턴 종료시 자신의 [ChargeRouge] 횟수가 15 이상이면, '라 노제 (la nausée)' 스킬 장착\n매 턴 시작시 [Aggro] 20 얻음
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004204].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeRouge], [Aggro]
   znaczenie tagów: [ChargeRouge] = 맥동 / Pulsation; [Aggro] = 도발치 / Aggro
   EN: Encounter Start: Gain 5 [ChargeRouge] Potency\n\nTurn End: At 15+ [ChargeRouge] Count, equip "La Nausée" Skill\nEvery Turn Start: Gain +20 [Aggro]
   PL:
280. [Jednostka wsparcia [40004204] — tekst klimatyczny] 유년기가 언제 끝나는지를 누가 정해주는가? 붉은 아이는 여정을 통해 성장했다. 여정의 경험을 통해 무언가가 되려하였고, 그렇게 되어가고 있다 생각했지만 그 과정은 갑작스럽게 끝났다. 유년기는 스스로 끝을 맺을수있는게 아니었다. 갑작스럽게 밖에서부터 현실이 들이밀어지며 강제적이면서도 성마르게 통보된다. 이제 끝이라고.
   źródło: Passives_Assist-a1c10p2.json :: dataList[id=40004204].flavor
   limit: do 620 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Who determines the childhood's end?\n\nThe crimson child matured throughout the adventure, shaped by their experiences and sketching their own future at the end of the journey—or so they thought. Their childhood came to a sudden halt, and so too did the adventure; it was never something they could've ended on their own terms.\n\nChildhood's end is a sudden, violent intrusion of reality from the world outside, more a forceful notice than a promised ritual: "You're not a child anymore."
   PL:

## Jednostka wsparcia: Passives_Assist-a1c8p2
- plik gry: `Passives_Assist-a1c8p2.json`

281. [Jednostka wsparcia [40000201] — nazwa] 가척
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000201].name
   limit: do 40 znaków
   EN: Paired Assault
   PL:
282. [Jednostka wsparcia [40000201] — opis] 아군이 적을 공격하여 피해를 입히면, 해당 공격 종료시 '빈틈찌르기'로 일방 공격함 (턴 당 2회)
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000201].desc
   limit: do 200 znaków
   EN: When an ally deals damage by striking an enemy, use the Skill 'Weakness Thrust' as an Unopposed Attack after the ally's attack ends (2 times per turn)
   PL:
283. [Jednostka wsparcia [40000202] — nazwa] 부자
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000202].name
   limit: do 40 znaków
   EN: Aiding Stab
   PL:
284. [Jednostka wsparcia [40000202] — opis] 적이 자신을 제외한 아군을 공격 종료 후 공격당한 아군의 체력이 25% 미만이면, 공격자를 '가척아원'으로 일방 공격함 (전투 당 1회)
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000202].desc
   limit: do 250 znaków
   EN: When an enemy attacks another ally, and if the allied unit has less than 25% HP after the attack, use the Skill 'Aiding Strike' as an Unopposed Attack against the attacker (once per Encounter)
   PL:
285. [Jednostka wsparcia [40000203] — nazwa] 흡조
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000203].name
   limit: do 40 znaków
   EN: Siphoning Fulfillment
   PL:
286. [Jednostka wsparcia [40000203] — opis] 턴 종료시 자신의 호흡 3 당, 다음 턴에 방어 레벨 증가 1 얻음 (최대 6)
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000203].desc
   limit: do 120 znaków
   EN: Turn End: gain 1 Defense Level Up next turn for every 3 Poise on self (max 6)
   PL:
287. [Jednostka wsparcia [40000204] — nazwa] 고양
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000204].name
   limit: do 40 znaków
   EN: Morale Boost
   PL:
288. [Jednostka wsparcia [40000204] — opis] 적 처치시, 정신력이 가장 낮은 수감자 2명의 정신력 10 회복
   źródło: Passives_Assist-a1c8p2.json :: dataList[id=40000204].desc
   limit: do 120 znaków
   EN: On Kill, heal 10 SP for 2 Sinners with the least SP
   PL:

## Jednostka wsparcia: Passives_Assist-a1c9p2
- plik gry: `Passives_Assist-a1c9p2.json`

289. [Jednostka wsparcia [40000601] — nazwa] 노란작살 (작명: 에즈라)
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000601].name
   limit: do 50 znaków
   EN: The Yellow Harpoon (named by: Ezra)
   PL:
290. [Jednostka wsparcia [40000601] — opis] 턴 시작시 [YellowHarpoon]을 얻음 (전투당 1회)\n\n정신력이 35인 상태로 전투를 시작함\n\n턴 종료시 적의 체력이 50% 미만일 때, [YellowHarpoonSin] 얻음
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000601].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [YellowHarpoon], [YellowHarpoonSin]
   znaczenie tagów: [YellowHarpoon] = 노란작살 / The Yellow Harpoon; [YellowHarpoonSin] = 신(心) - 노란작살 / Shin(心) - The Yellow Harpoon
   EN: Turn Start: Gain [YellowHarpoon] (once per Encounter)\n\nBegins Encounter at 35 SP\n\nTurn End: If the enemy has less than 50% HP, gain [YellowHarpoonSin]
   PL:
291. [Jednostka wsparcia [40000601] — tekst klimatyczny] <color=#fde55d>“아니이 들어봐바! 막내 넌 그 작살을 진짜 잘 쓰고!\n그 작살은 완전 특별한거고! 넌 노란색을 노리고 있었고!\n그러니까 노란작살이 딱이지!!!”</color>
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000601].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>, \n
   EN: <color=#fde55d>"Okay, hear me out. Hear me out, Baby bee!\nYou're good with harpoons, right?\nYou use a super snazzy special harpoon, right?\nAnd you're shootin' for the Yellow Color, right?\nBam! There ya have it!\n\n<b>The Yellow Harpoon</b>!!!"</color>
   PL:
292. [Jednostka wsparcia [40000602] — nazwa] 궁니르
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000602].name
   limit: do 40 znaków
   EN: Gungnir
   PL:
293. [Jednostka wsparcia [40000602] — opis] [BeeSting]이 있는 대상에게 합 승리시 대상의 [Vibration]을\n[VibrationBleeding]로 [Switch_Vibration]\n\n[ArtifactBeeSting]이 있는 대상에게 합 승리시 대상의 [Vibration]을 [VibrationEcho]으로 [FusionVibration]\n\n[BeeSting], [ArtifactBeeSting]이 있는 대상에게 마지막 코인 적중시 [VibrationExplosion]
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000602].desc
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n, [BeeSting], [Vibration], [VibrationBleeding], [Switch_Vibration], [ArtifactBeeSting], [VibrationEcho], [FusionVibration], [VibrationExplosion]
   znaczenie tagów: [BeeSting] = 박힌 작살 [벌침] / Nested Harpoon [Beesting]; [Vibration] = 진동 / Tremor; [VibrationBleeding] = 진동 - 과다출혈 / Tremor - Hemorrhage; [Switch_Vibration] = 진폭 변환 / Amplitude Conversion; [ArtifactBeeSting] = 박힌 작살 [말벌침] / Nested Harpoon [Waspsting]; [VibrationEcho] = 진동 - 반향 / Tremor - Reverb; [FusionVibration] = 진폭 얽힘 / Amplitude Entanglement; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: On Clash Win against targets with [BeeSting], trigger [Switch_Vibration] on their [Vibration] into [VibrationBleeding]\n\nOn Clash Win against targets with [ArtifactBeeSting], trigger [FusionVibration] on their [Vibration] into [VibrationEcho]\n\nOn Hit with the final Coin against targets with both [BeeSting] and [ArtifactBeeSting], trigger [VibrationExplosion]
   PL:
294. [Jednostka wsparcia [40000602] — tekst klimatyczny] <color=#fde55d>유적 심층에서 발견되는 가장 귀한 등급의 유물.\n과거, 피범벅이 된 소년은 이 창날을 우연히 주웠고, 사용에 적합한 적성을 우연히 가지고 있었다. 우연은 무엇인가.</color>
   źródło: Passives_Assist-a1c9p2.json :: dataList[id=40000602].flavor
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>, \n
   EN: <color=#fde55d>A precious Relic of the highest rarity, found in the depths of the Ruins.\nIt was by mere coincidence that the young boy, blood-soaked, came to be in possession of this speartip; coincidentally, he also possessed the aptitude to wield it. \n\nWhat is coincidence, indeed?</color>
   PL:

## Jednostka wsparcia: Passives_Assist-a1c9p3
- plik gry: `Passives_Assist-a1c9p3.json`

295. [Jednostka wsparcia [40000701] — nazwa] 최후의 수단
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000701].name
   limit: do 40 znaków
   EN: The Last Resort
   PL:
296. [Jednostka wsparcia [40000701] — opis] 턴 종료 시 자신을 제외한 모든 아군이 외부 효과로 행동 불가능 상태가 되면, 다음 턴에 '홍염살 최대 감응 【열화침식】' 장착
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000701].desc
   limit: do 190 znaków
   EN: Turn End: If all allies except for this unit are immobilized due to external effects, equip 'A.B.S Max Attunement 【Degraded Corrosion】' next turn
   PL:
297. [Jednostka wsparcia [40000701] — tekst klimatyczny] ‘전부… 역시…’
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000701].flavor
   limit: do 120 znaków
   EN: 'I knew it... Everyone...'
   PL:
298. [Jednostka wsparcia [40000702] — nazwa] 내화
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000702].name
   limit: do 40 znaków
   EN: Fireproof
   PL:
299. [Jednostka wsparcia [40000702] — opis] [Combustion] 피해로 흐트러지거나 체력이 1 미만으로 감소하지 않고, 외부 효과로 행동 불가능 상태가 되지 않음\n\n[Combustion]으로 받는 피해량 -50%
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000702].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: Damage from [Combustion] cannot Stagger this unit and does not reduce this unit's HP below 1; this unit cannot be immobilized due to external effects\n\nTake -50% damage from [Combustion]
   PL:
300. [Jednostka wsparcia [40000703] — nazwa] E.G.O 감응도 증가
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000703].name
   limit: do 40 znaków
   EN: E.G.O Attunement Boost
   PL:
301. [Jednostka wsparcia [40000703] — opis] 스테이지 시작 시 [LvUpFireFly] 얻음\n\n자신의 체력이 70% 미만이면, 공격 적중 시 대상과 자신에게 [Combustion] 1 부여
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000703].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [LvUpFireFly], [Combustion]
   znaczenie tagów: [LvUpFireFly] = E.G.O 감응도 증가 / E.G.O Attunement Boost; [Combustion] = 화상 / Burn
   EN: Encounter Start: Gain [LvUpFireFly]\n\nOn Hit: At less than 70% HP, apply 1 [Combustion] to target and self
   PL:
302. [Jednostka wsparcia [40000704] — nazwa] E.G.O 공명도 증가
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000704].name
   limit: do 40 znaków
   EN: E.G.O Resonance Boost
   PL:
303. [Jednostka wsparcia [40000704] — opis] 턴 시작 시 E.G.O 장비를 착용한 아군 1명당 [AttackUp] 1 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000704].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: Gain 1 [AttackUp] for every ally wearing E.G.O gear
   PL:
304. [Jednostka wsparcia [40000705] — nazwa] 불에 뛰어드는 나방과 같이
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000705].name
   limit: do 40 znaków
   EN: Like a Moth to a Flame
   PL:
305. [Jednostka wsparcia [40000705] — opis] 이 캐릭터는 최대 체력이 가장 낮은 적을 우선 공격함\n\n[Combustion]을 부여하는 공격 스킬 또는 [Combustion] 피해로 적 처치 시 정신력 10 회복 (턴당 1회)
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000705].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion]
   znaczenie tagów: [Combustion] = 화상 / Burn
   EN: This unit prioritizes attacking enemies with the lowest max HP\n\nHeal 10 SP when killing enemies with [Combustion] damage or Attack Skills that apply [Combustion] (max once per turn)
   PL:
306. [Jednostka wsparcia [40000706] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000706].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
307. [Jednostka wsparcia [40000706] — opis] 호엔하임이 사망한 상태에서 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000706].desc
   limit: do 120 znaków
   EN: Lose this Encounter if this unit is killed after Hohenheim is killed
   PL:
308. [Jednostka wsparcia [40000706] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000706].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
309. [Jednostka wsparcia [40000801] — nazwa] 역시 본사 E.G.O의 감응도에 따른 침식도는 만만치 않네
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000801].name
   limit: do 90 znaków
   EN: Can't Underestimate the HQ's E.G.O Attunement and its Corrosion
   PL:
310. [Jednostka wsparcia [40000801] — opis] 스테이지 시작 시 [LvUpHohenheimBigBird] 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000801].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LvUpHohenheimBigBird]
   znaczenie tagów: [LvUpHohenheimBigBird] = E.G.O 감응도 증가 / E.G.O Attunement Boost
   EN: Encounter Start: Gain [LvUpHohenheimBigBird]
   PL:
311. [Jednostka wsparcia [40000802] — nazwa] E.G.O 장비 숙련 매뉴얼
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000802].name
   limit: do 50 znaków
   EN: E.G.O Gear Proficiency Manual
   PL:
312. [Jednostka wsparcia [40000802] — opis] 턴 시작 시 E.G.O 장비를 착용한 아군 1명당 [DefenseUp] 1 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000802].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: Gain 1 [DefenseUp] for every ally wearing E.G.O gear
   PL:
313. [Jednostka wsparcia [40000802] — tekst klimatyczny] 저자 호엔하임.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000802].flavor
   limit: do 120 znaków
   EN: Written by Hohenheim.
   PL:
314. [Jednostka wsparcia [40000803] — nazwa] 검은 숲에서 길을 잃었을 때 함부로 빛을 따라가지는 말아야 한다는 건가
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000803].name
   limit: do 80 znaków
   EN: Don't Blindly Follow the Light when Lost in the Black Forest
   PL:
315. [Jednostka wsparcia [40000803] — opis] 턴 시작 시 [LanternHohenheimBigBird]가 없으면, [LanternHohenheimBigBird] 1 얻음\n\n<color=#ff6000><mark=#ff000040><b><u>턴 종료 시 [LanternHohenheimBigBird]가 20이면, 다음 턴에 강력한 공격을 사용하는 적에게 [DelusionHohenheimBigBird] 부여</u></b></mark></color>
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000803].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [LanternHohenheimBigBird], [DelusionHohenheimBigBird]
   znaczenie tagów: [LanternHohenheimBigBird] = 램프 / Lamp; [DelusionHohenheimBigBird] = 현혹 / Dazzle
   EN: Turn Start: If this unit does not have [LanternHohenheimBigBird], gain 1 [LanternHohenheimBigBird]\n\n<color=#ff6000><mark=#ff000040><b><u>Turn End: At 20 [LanternHohenheimBigBird], inflict [DelusionHohenheimBigBird] to the enemy that uses its powerful attack next turn</u></b></mark></color>
   PL:
316. [Jednostka wsparcia [40000804] — nazwa] 현혹의 램프
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000804].name
   limit: do 40 znaków
   EN: Dazzling Lamp
   PL:
317. [Jednostka wsparcia [40000804] — opis] 이 캐릭터는 속도 최댓값이 가장 높은 적을 우선 공격함\n\n스킬 지정 시 속도에 관계 없이 공격 대상을 자신으로 변경할 수 있음 (집중 전투 전용)
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000804].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This unit prioritizes attacking the enemy with the fastest Max Speed\n\nWhen chaining Skills, this unit can draw enemies' attack toward self regardless of Speed (Focused Encounters only)
   PL:
318. [Jednostka wsparcia [40000805] — nazwa] 이 눈으로 검은 숲 전체를 지켜봐 왔다는군
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000805].name
   limit: do 70 znaków
   EN: Its Eyes Have Watched Over the Entire Black Forest
   PL:
319. [Jednostka wsparcia [40000805] — opis] 턴 시작 시 자신을 제외한 속도가 가장 낮은 아군 1명에게 다음 턴에 [Agility] (자신의 [Binding] / 2) 부여 (최대 2. 소수점 버림[TabExplain])\n\n모든 아군 중에서 자신이 속도가 가장 낮으면, 기본 공격 스킬로 가하는 피해량 +10%\n- 자신의 속도가 1이면, 대신 피해량 +20%
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000805].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [Agility], [Binding], [TabExplain]
   znaczenie tagów: [Agility] = 신속 / Haste; [Binding] = 속박 / Bind
   EN: Turn Start: Apply ([Binding] on self /2) [Agility] to the ally (excluding this unit) with the slowest Speed next turn (max 2, rounded down)\n\nIf this unit has the slowest Speed, deal +10% damage with Base Attack Skills\n- If this unit's Speed is 1, deal +20% damage instead
   PL:
320. [Jednostka wsparcia [40000806] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000806].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
321. [Jednostka wsparcia [40000806] — opis] 알리사가 사망한 상태에서 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000806].desc
   limit: do 120 znaków
   EN: Lose this Encounter if this unit is killed after Alyssa is killed
   PL:
322. [Jednostka wsparcia [40000806] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000806].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
323. [Jednostka wsparcia [40000901] — nazwa] 노란작살 (작명: 에즈라)
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000901].name
   (powtórzenie elementu 289 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
324. [Jednostka wsparcia [40000901] — opis] 스테이지 시작시, [YellowHarpoon]을 얻음\n\n턴 시작시 중지 아비의 [ReinforcedTattooSpider]이 2이고 자신의 정신력이 0 이상이면, [YellowHarpoonSin]을 얻음\n\n자신의 정신력이 0 미만이면, [YellowHarpoonSin] 제거
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000901].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [YellowHarpoon], [ReinforcedTattooSpider], [YellowHarpoonSin]
   znaczenie tagów: [YellowHarpoon] = 노란작살 / The Yellow Harpoon; [ReinforcedTattooSpider] = 중지 - 원한 문신 [큰 형님] / The Middle - Vengeance Tattoo [Great Brother]; [YellowHarpoonSin] = 신(心) - 노란작살 / Shin(心) - The Yellow Harpoon
   EN: Encounter Start: Gain [YellowHarpoon]\n\nTurn Start: If this unit has 0+ SP and The Middle Nursefather has 2 [ReinforcedTattooSpider], gain [YellowHarpoonSin]\n\nAt less than 0 SP, lose [YellowHarpoonSin]
   PL:
325. [Jednostka wsparcia [40000901] — tekst klimatyczny] <color=#fde55d>“아니이 들어봐바! 막내 넌 그 작살을 진짜 잘 쓰고!\n그 작살은 완전 특별한거고! 넌 노란색을 노리고 있었고!\n그러니까 노란작살이 딱이지!!!”</color>
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000901].flavor
   (powtórzenie elementu 291 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
326. [Jednostka wsparcia [40000902] — nazwa] 뒤틀림 탐정 사무소의 말벌
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000902].name
   limit: do 60 znaków
   EN: The Wasp of the Distortion Detective Office
   PL:
327. [Jednostka wsparcia [40000902] — opis] 모제스가 ‘붉은 숨을 깊게 들이마신다.’를 장착한 턴에 [YellowHarpoonSin]을 얻고 이후 제거하지 않음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000902].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [YellowHarpoonSin]
   znaczenie tagów: [YellowHarpoonSin] = 신(心) - 노란작살 / Shin(心) - The Yellow Harpoon
   EN: In the turn Moses equips 'Inhale Deep the Red Breath', this unit gains [YellowHarpoonSin] permanently
   PL:
328. [Jednostka wsparcia [40000904] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000904].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
329. [Jednostka wsparcia [40000904] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000904].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
330. [Jednostka wsparcia [40000904] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40000904].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
331. [Jednostka wsparcia [40001001] — nazwa] 깊은 사색
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001001].name
   limit: do 40 znaków
   EN: Deep Contemplation
   PL:
332. [Jednostka wsparcia [40001001] — opis] 스테이지 시작시, [MosesWarPTSD]을 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [MosesWarPTSD]
   znaczenie tagów: [MosesWarPTSD] = 그 날의 기억 / Memories of that Day
   EN: Encounter Start: Gain [MosesWarPTSD]
   PL:
333. [Jednostka wsparcia [40001002] — nazwa] 붉은 점
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001002].name
   limit: do 40 znaków
   EN: Crimson Point
   PL:
334. [Jednostka wsparcia [40001002] — opis] 중지 아비가 레바테인 보유 시 [MosesSin]를 얻고,\n‘붉은 숨을 깊게 들이마신다.’를 매 턴 사용함\n\n[MosesRedBreathCharge]을 보유 중이면, 패닉 상태가 되지 않음\n\n<color=#ff6000><mark color=#ff000040><b><u>턴 종료시 자신의 [MosesRedBreathCharge]이 3이면, 강력한 스킬을 사용함</color></mark></b></u>
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001002].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [MosesSin], [MosesRedBreathCharge]
   znaczenie tagów: [MosesSin] = 신(心) - 모제스 / Shin (心) - Moses; [MosesRedBreathCharge] = 깊은 숨 - 붉은색 / Deep Breath - Red
   EN: If the Middle Nursefather has Lævateinn, this unit gains [MosesSin] and uses 'Inhale Deep the Red Breath' every turn\n\nIf this unit has [MosesRedBreathCharge], becomes immune to Panic\n\n<color=#ff6000><mark color=#ff000040><b><u>Turn End: At 3 [MosesRedBreathCharge], use a powerful Skill</color></mark></b></u>
   PL:
335. [Jednostka wsparcia [40001002] — tekst klimatyczny] 물리력을 이루는 모든 것을 한 점에 모으고 쌓아 만들어 낸, 적층된 원기둥을 다른 한 점으로 밀어낸다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001002].flavor
   limit: do 210 znaków
   EN: Concentrate into a single point all that constitutes the physical force and stack the layers into a cylindrical pillar—then expel it toward another single point.
   PL:
336. [Jednostka wsparcia [40001003] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001003].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
337. [Jednostka wsparcia [40001003] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001003].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
338. [Jednostka wsparcia [40001003] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001003].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
339. [Jednostka wsparcia [40001101] — nazwa] 차원가방 [에즈라]
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001101].name
   limit: do 40 znaków
   EN: Dimensional Bag [Ezra]
   PL:
340. [Jednostka wsparcia [40001101] — opis] 스테이지 시작시 [DimensionalBagEzraA]을 1 얻음\n\n현재 사용하는 공방 무기 스킬을 1회 이상 사용했으면, 다음 턴에 공방 무기를 교체함\n\n사용 공방 무기\n- 알라스 공방 장갑\n- 네스터 공방 망치\n- 스크류 아틀리에제 드릴 망치\n- 나미르 공방 건틀릿
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001101].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [DimensionalBagEzraA]
   znaczenie tagów: [DimensionalBagEzraA] = 차원가방 - 알라스 공방 / Dimensional Bag - Allas Workshop
   EN: Encounter Start: Gain 1 [DimensionalBagEzraA]\n\nIf this unit used the current Workshop weapon more than once, switch weapons the next turn\n\nList of weapons:\n- Allas Workshop Gloves\n- Nester Workshop Hammer\n- Screw Atelier Drill Hammer\n- Namir Workshop Gauntlets
   PL:
341. [Jednostka wsparcia [40001102] — nazwa] 탐정..! 아니.. 팀장님 저희만 믿으세요!
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001102].name
   limit: do 70 znaków
   EN: Detecti—I mean, Team Leader! We've Got Your Back!
   PL:
342. [Jednostka wsparcia [40001102] — opis] 모제스가 ‘붉은 숨을 깊게 들이마신다.’를 장착한 턴부터\n유리아 공방 - 특제 수제작 골든 리트리버 전용 도끼만 사용함\n\n모제스가 ‘붉은 숨을 깊게 들이마신다.’를 장착한 턴부터 [MiddleFingerEzraSin]를 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001102].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [MiddleFingerEzraSin]
   znaczenie tagów: [MiddleFingerEzraSin] = 신(心) - 에즈라 / Shin (心) - Ezra
   EN: This unit's weapon rotation is fixed to 'YuRia Atelier Special Handmade Golden Retriever-Exclusive Axe' starting from the turn Moses equips 'Inhale Deep the Red Breath'\n\nThis unit gains [MiddleFingerEzraSin] starting from the turn Moses equips 'Inhale Deep the Red Breath'
   PL:
343. [Jednostka wsparcia [40001102] — tekst klimatyczny] “그때 그 혈귀가 있던 호텔에서의 일, 갑자기 생각나지 않아요? 대박이었는데.”
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001102].flavor
   limit: do 120 znaków
   EN: "Remember that case in that hotel with the Bloodfiend? Man, that was sick."
   PL:
344. [Jednostka wsparcia [40001104] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001104].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Jednostka wsparcia [40001104] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001104].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Jednostka wsparcia [40001104] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001104].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
347. [Jednostka wsparcia [40001201] — nazwa] 붉은시선
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001201].name
   limit: do 40 znaków
   EN: The Red Gaze
   PL:
348. [Jednostka wsparcia [40001201] — opis] 턴 종료 시 체력이 최대 체력의 50% 이상인 적에게 다음 턴에 [Binding] 3 부여\n<color=#ff6000><mark=#ff000040><b><u>자신에게 공격 스킬을 사용하려는 적이 [Reduction] 1 얻음</u></b></mark></color>
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001201].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [Binding], [Reduction]
   znaczenie tagów: [Binding] = 속박 / Bind; [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: Turn End: Inflict 3 [Binding] next turn against enemies with 50% or more HP\n<color=#ff6000><mark=#ff000040><b><u>Enemies that are about to use Attack Skills against this unit gain 1 [Reduction]</u></b></mark></color>
   PL:
349. [Jednostka wsparcia [40001202] — nazwa] 초고열 글라디우스
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001202].name
   limit: do 40 znaków
   EN: White-hot Gladius
   PL:
350. [Jednostka wsparcia [40001202] — opis] 글라디우스 스킬 적중시 [AaCfPcBiv2] 1 부여
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001202].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AaCfPcBiv2]
   znaczenie tagów: [AaCfPcBiv2] = 고열기전 / Superthermogenesis
   EN: Inflict 1 [AaCfPcBiv2] On Hit with a Gladius Skill
   PL:
351. [Jednostka wsparcia [40001203] — nazwa] 피눈물
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001203].name
   limit: do 40 znaków
   EN: Bloody Tears
   PL:
352. [Jednostka wsparcia [40001203] — opis] 스킬 사용시 최대 체력의 3%만큼 고정 피해를 받음(해당 효과로 사망하지 않음)\n스킬 적중시, 입힌 체력 피해량의 10% 만큼 체력 회복
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001203].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n
   EN: On Skill Use: Take 3% of max HP as fixed damage (this damage cannot kill this unit).\nOn Hit with a Skill: Heal 10% of HP damage dealt
   PL:
353. [Jednostka wsparcia [40001204] — nazwa] 피의 장막
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001204].name
   limit: do 40 znaków
   EN: Blood Barrier
   PL:
354. [Jednostka wsparcia [40001204] — opis] 매 턴마다 자신을 포함한 모든 아군이 보호막을 얻음.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001204].desc
   limit: do 120 znaków
   EN: Every turn, all allies, including this unit, gains Shield HP
   PL:
355. [Jednostka wsparcia [40001205] — nazwa] 신(心) - 붉은시선
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001205].name
   limit: do 40 znaków
   EN: Shin (心) - The Red Gaze
   PL:
356. [Jednostka wsparcia [40001205] — opis] ‘엄지 아비 - 발렌치나’가 [ObsessionAndGreed]를 보유하면, 다음 턴에 [VergiliusSin]을 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001205].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [ObsessionAndGreed], [VergiliusSin]
   znaczenie tagów: [ObsessionAndGreed] = 신(心) - 발렌치나 / Shin (心) - Valencina; [VergiliusSin] = 신(心) - 붉은시선 / Shin (心) - The Red Gaze
   EN: When 'The Thumb Nursefather - Valencina' has [ObsessionAndGreed], this unit gains [VergiliusSin] next turn
   PL:
357. [Jednostka wsparcia [40001206] — nazwa] 개화 E.G.O::라바크롬 상귀니스
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001206].name
   limit: do 60 znaków
   EN: Effloresced E.G.O::Lavacrum Sanguinis
   PL:
358. [Jednostka wsparcia [40001206] — opis] 개화[TabExplain] E.G.O::라바크롬 상귀니스 상태가 되며, 다음 효과 적용\n- 매턴마다 신속 3 얻음\n- [Laceration] 피해를 받지 않음\n- E.G.O 발현 스킬들을 사용할 수 있음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001206].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain], [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: Enter Effloresced[TabExplain] E.G.O::Lavacrum Sanguinis state, and gain the following effects:\n- Gain 3 Haste every turn\n- Become immune to [Laceration] damage\n- Unlocks E.G.O Manifestation Skills
   PL:
359. [Jednostka wsparcia [40001208] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001208].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
360. [Jednostka wsparcia [40001208] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001208].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
361. [Jednostka wsparcia [40001208] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001208].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
362. [Jednostka wsparcia [40001209] — nazwa] 길잡이
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001209].name
   limit: do 40 znaków
   EN: The Guide
   PL:
363. [Jednostka wsparcia [40001209] — opis] 단테의 지휘에 호응하여, 자신의 스킬 타겟을 변경
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001209].desc
   limit: do 120 znaków
   EN: Observes Dante's command and adjusts his Skills' targets accordingly
   PL:
364. [Jednostka wsparcia [40001209] — tekst klimatyczny] ‘흐름을 따라…’
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001209].flavor
   limit: do 120 znaków
   EN: 'Following the flow...'
   PL:
365. [Jednostka wsparcia [40001302] — nazwa] 의체 해체
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001302].name
   limit: do 40 znaków
   EN: Dismantle Prosthesis
   PL:
366. [Jednostka wsparcia [40001302] — opis] <기계 융화 생명체>와 <뒤틀림>에게 가하는 피해량 +40%\n\n적 처치 시 자신을 제외한 모든 아군의 정신력 20 회복 (턴당 1회)
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001302].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Deal +40% damage to <Mechanical Amalgam> and <Distortion>\n\nOn Kill, all other allies heal 20 SP (once per turn)
   PL:
367. [Jednostka wsparcia [40001302] — tekst klimatyczny] 2차 연기전쟁은 인간과 인간으로 보이지 않는 인간들의 싸움이었다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001302].flavor
   limit: do 120 znaków
   EN: The Second Smoke War was a conflict between humans and humans who no longer looked the part.
   PL:
368. [Jednostka wsparcia [40001306] — nazwa] 신(心) - 어느 싱클레어
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001306].name
   limit: do 50 znaków
   EN: Shin (心) - A Certain Sinclair
   PL:
369. [Jednostka wsparcia [40001306] — opis] 턴 시작 시 [WillAwakenSinclair] 얻음 (전투당 1회)
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001306].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WillAwakenSinclair]
   znaczenie tagów: [WillAwakenSinclair] = 신(心) - 어느 싱클레어 / Shin (心) - A Certain Sinclair
   EN: Turn Start: Gain [WillAwakenSinclair] (once per Encounter)
   PL:
370. [Jednostka wsparcia [40001309] — nazwa] 연기 버티기
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001309].name
   limit: do 40 znaków
   EN: Withstand the Smoke
   PL:
371. [Jednostka wsparcia [40001309] — opis] 외부 효과로 정신력 피해를 받지 않고, 행동 불가능 상태가 되지 않음\n\n턴 종료 전 아군이 외부 효과로 행동 불가능 상태가 되면, ‘연기[TabExplain] 거두기’ 사용
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001309].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [TabExplain]
   EN: This unit does not take SP damage due to external effects and cannot become immobilized\n\nIf an ally becomes immobilized due to external effects before Turn End, use 'Abate the Smoke[TabExplain]'
   PL:
372. [Jednostka wsparcia [40001309] — tekst klimatyczny] 제2차 전쟁의 연기는 1차 전쟁 당시의 연기와 본질적으로 다르지 않았다.\n연기는 정신에 침투해, 이성을 흐릿하게 만든다.\n이를 숨쉬듯 자연스럽게 일상으로 받아들일 수 있어야만, 연기전쟁에서 살아남을 수 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001309].flavor
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The Smoke of the Second War was no different in nature from that of the First—it invaded the mind and clouded the judgement of the victim.\nSurvival was reserved only for those who learned to accept the Smoke as part of their daily lives.
   PL:
373. [Jednostka wsparcia [40001308] — nazwa] 내면에 귀를 기울이고 그 소리의 표상을 붙잡는다면…
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001308].name
   limit: do 100 znaków
   EN: Lend My Ear to the Inner Self, Hold onto the Representation of its Voice...
   PL:
374. [Jednostka wsparcia [40001308] — opis] 최대 체력이 1000 이상인 적 사망 시 [SignAwakenSinclair], [LimitedAwakenSinclair] 얻음 (전투당 1회)\n- 이후 오만, 분노, 질투 속성 스킬 사용 시 [SuperCoin]으로 변경됨
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001308].desc
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [SignAwakenSinclair], [LimitedAwakenSinclair], [SuperCoin]
   znaczenie tagów: [SignAwakenSinclair] = 표지 - 미래현현 / Sign - Manifestation of the Future; [LimitedAwakenSinclair] = 움브라 금제 해제 / Umbra Unsealed; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: Gain [SignAwakenSinclair] and [LimitedAwakenSinclair] when an enemy with 1,000+ max HP is killed (once per Encounter)\n- Afterward, convert all Coins into [SuperCoin]s when this unit uses Pride, Wrath, Envy Skills
   PL:
375. [Jednostka wsparcia [40001301] — nazwa] 공수특전단 - 아브락사스의 전차
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001301].name
   limit: do 70 znaków
   EN: Special Airborne Operations Force - Abraxas Chariot
   PL:
376. [Jednostka wsparcia [40001301] — opis] [Burst] 위력, 횟수를 부여하는 스킬 사용 시 대상의 [Burst]이 20 미만이면, 공격 적중 시 대상의 [Burst] 횟수를 소모하지 않음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001301].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Targets with less than 20 [Burst] do not lose [Burst] Count when this unit hits them with Skills that inflict [Burst] Potency or Count
   PL:
377. [Jednostka wsparcia [40001301] — tekst klimatyczny] 제2차 연기전쟁에서는 게릴라 부대의 성과가 중요했다.\n그중에서도 작전 지역에 강하하여 전장의 판도를 바꾸는 공수부대들은 전쟁 내내 두려움의 대상이었다.\n그들은 날개의 기술 등을 이용해 저마다의 방식으로 예고 없이 나타나 전투를 수행했고, 목표를 달성하는 즉시 홀연히 자취를 감추었다.\n그러한 공수부대들 가운데서도 ‘아브락사스의 전차’는 악명 높은 ‘101문의 낙하자들’, ‘차원 유랑단’과 나란히 경외와 공포를 불러일으키는 존재 중 하나였다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001301].flavor
   limit: do 860 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Guerrilla warfare played an important role during the Second Smoke War.\nThe most feared among the undertakers of these ambushes were none other than the airborne forces that descended directly upon the combat zone and turned the tide of the battle unexpectedly.\nThese airborne soldiers would appear out of nowhere by utilizing technologies such as Singularities of the Wings—they would carry out their mission immediately, and once their objectives were accomplished, they would disappear without a trace.\n"The Abraxas Chariot" was one of the groups that inspired the most dread in the War alongside those airborne forces such as "Descenders of 101 Doors" and "The Dimension Roamers."
   PL:
378. [Jednostka wsparcia [40001304] — nazwa] 할버드와 바스타드 소드
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001304].name
   limit: do 40 znaków
   EN: Halberd and Bastard Sword
   PL:
379. [Jednostka wsparcia [40001304] — opis] 공격 종료 시 대상의 긍정적인 효과를 1개 해제하고 [Burst] 4 부여 (턴당 1회)\n\n턴 종료 시 자신의 부정적인 효과를 1개 해제하고 [Breath] 5 얻고 [Breath] 횟수 2 증가
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001304].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: Attack End: Remove 1 beneficial effect from target and inflict 4 [Burst] (once per turn)\n\nTurn End: Remove 1 negative effect from self and gain 5 [Breath] and +2 [Breath] Count
   PL:
380. [Jednostka wsparcia [40001304] — tekst klimatyczny] 이름 모를 할버드와 바스타드 소드를 든 청년은 칙칙한 녹색 코트를 걸친 채 적진을 누비다 사라졌다. \n그렇기에 누군가에겐 초록공포, 누군가에겐 초록구원이라 불리었다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001304].flavor
   limit: do 340 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Wielding a nameless halberd and a bastard sword, the young man, clad in a dull green coat, would ravage through the enemy lines before vanishing without a trace once he was done.\nSome called him the Green Damnation, while others called him the Green Deliverance.
   PL:
381. [Jednostka wsparcia [40001307] — nazwa] 표지 - 미래현현
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001307].name
   limit: do 50 znaków
   EN: Sign - Manifestation of the Future
   PL:
382. [Jednostka wsparcia [40001307] — opis] 자신을 포함한 아군이 스킬 사용 시 획득하는 E.G.O 자원 수 +1\n\n턴 종료 시 자신을 제외한 수감자 1명당, 자신의 정신력을 6 회복함
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001307].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n
   EN: All allies, including this unit, gain 1 more E.G.O resource when using Skills\n\nTurn End: Heal 6 SP for every other Sinner present in the Encounter
   PL:
383. [Jednostka wsparcia [40001310] — nazwa] 운명 이탈
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001310].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
384. [Jednostka wsparcia [40001310] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001310].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
385. [Jednostka wsparcia [40001310] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001310].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
386. [Jednostka wsparcia [40001401] — nazwa] 신(心) - 붉은시선
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001401].name
   (powtórzenie elementu 355 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
387. [Jednostka wsparcia [40001401] — opis] 스테이지 시작 시 [VergiliusSin]을 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001401].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [VergiliusSin]
   znaczenie tagów: [VergiliusSin] = 신(心) - 붉은시선 / Shin (心) - The Red Gaze
   EN: Encounter Start: Gain [VergiliusSin]
   PL:
388. [Jednostka wsparcia [40001501] — nazwa] 무아몽중 [無我夢中]
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001501].name
   limit: do 80 znaków
   EN: Wading Through a Dream, the Self Nowhere to be Found [無我夢中]
   PL:
389. [Jednostka wsparcia [40001501] — opis] 턴 시작 시, 현재 턴 수만큼 [CutbondRyoshu] 얻음\n자신의 코인이 사용될 때마다 [CutbondRyoshu] 1 얻음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001501].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CutbondRyoshu]
   znaczenie tagów: [CutbondRyoshu] = 무아 [無我] / Muga [無我]
   EN: Turn Start: Gain [CutbondRyoshu] equal to current turn count\nGain 1 [CutbondRyoshu] for every use of this unit's Coin
   PL:
390. [Jednostka wsparcia [40001501] — tekst klimatyczny] ‘내가 아라야를 이미 거미집 밖으로 피신시킨 것처럼 보여야만 한다.’\n\n‘아라야를 찾으러 따라오는 아비들을 처리하기 위해, 칼부림을 벌인 것처럼 보이게 한다.’
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001501].flavor
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'I must make it look as though Araya is already safely out of the House of Spiders.'\n\n'I'll stage it by raising this blade against the Nursefathers—that should sell the story that I am trying to stop them from going after Araya.'
   PL:
391. [Jednostka wsparcia [40001502] — nazwa] 아비규환 [阿鼻叫喚]
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001502].name
   limit: do 60 znaków
   EN: Like the Naraka of Avīci and Raurava [阿鼻叫喚]
   PL:
392. [Jednostka wsparcia [40001502] — opis] 스테이지 시작 시, [HeavenlyKillerStar]을 얻고 정신력이 -44로 고정됨\n\n침잠 효과를 포함하여 정신력 피해를 받을 때, 대신 그 수치의 3배만큼 체력 피해를 입음
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001502].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [HeavenlyKillerStar]
   znaczenie tagów: [HeavenlyKillerStar] = 천살성도 - 아라야시키 [天殺星刀阿賴耶識] / Tiansha Star's Blade - Arayashiki [天殺星刀阿賴耶識]
   EN: Encounter Start: Gain [HeavenlyKillerStar] and fix SP at -44\n\nWhen taking SP damage including effects caused by Sinking, take (SP damage x 3) HP damage instead
   PL:
393. [Jednostka wsparcia [40001502] — tekst klimatyczny] ‘아비들의 힘과 지독함은 내가 가장 잘 안다.’\n\n‘그자들을 속이기 위해선 필사적으로 연기해야 한다.’\n\n‘아비들 하나하나에 맞춰, 어떤 식으로 상대할지, 어떻게 칼을 맞댈지.’\n\n‘정신을 놓는 와중에도 머릿속에서 수없이 그려낸다.’
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001502].flavor
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'I know better than anyone how strong and tenacious the Nursefathers are.'\n\n'If I am to deceive them, I'll need to stage a desperate act with everything at my disposal.'\n\n'Plan how I'll take on each of them—how their swords will clash with mine.'\n\n'I may lose control over my own mind, but I <i>will</i> make sure to run the picture through my head over and over.'
   PL:
394. [Jednostka wsparcia [40001503] — nazwa] 지리멸렬 [支離滅裂]
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001503].name
   limit: do 80 znaków
   EN: Severed and Torn until Even the Form is Undone [支離滅裂]
   PL:
395. [Jednostka wsparcia [40001503] — opis] 공격 적중 시, [CutoffRyoshu] 1 부여\n- 턴 시작 시 자신의 [CutbondRyoshu] 10당 [CutoffRyoshu] 부여값 +1 (최대 4)\n\n피격 시, 피해량이 (대상의 [CutoffRyoshu] + 자신의 [CutbondRyoshu])%만큼 감소 (최대 90%)\n\n모든 스킬 공격이 종료되었을 때 [CutoffRyoshu] 100을 보유한 적이 있으면, 대상에게 강력한 스킬을 사용
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001503].desc
   limit: do 440 znaków
   tokeny: zachowaj dokładnie: \n, [CutoffRyoshu], [CutbondRyoshu]
   znaczenie tagów: [CutoffRyoshu] = 절사 [切絲] / Sever the Thread [切絲]; [CutbondRyoshu] = 무아 [無我] / Muga [無我]
   EN: On Hit, inflict 1 [CutoffRyoshu]\n- Turn Start: Inflict 1 more [CutoffRyoshu] for every 10 [CutbondRyoshu] on self (max 4)\n\nWhen hit, take -([CutbondRyoshu] on self + [CutoffRyoshu] on target)% damage (max 90%)\n\nIf there is an enemy that has 100 [CutoffRyoshu] after this unit finishes all attacks with its Skills, use a powerful Skill on target
   PL:
396. [Jednostka wsparcia [40001503] — tekst klimatyczny] ‘아비들을 죽일 수는 없겠지만, 발을 묶어두고 잠시 무력화시킬 수는 있겠지.’\n\n‘그러고 나서.’\n\n‘나가서’\n\n‘강해져서 돌아가야 한다.’\n\n‘나보다 강한 누군가를 내 편으로 만들든, 수를 늘리든, 아비들을 확실히 없앨 수 있을 수단을 준비해야 한다.’
   źródło: Passives_Assist-a1c9p3.json :: dataList[id=40001503].flavor
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n
   EN: 'I'm not strong enough to kill the Nursefathers—this I know. But I can still incapacitate and hold them back, if only for a little while.'\n\n'And then...'\n\n'And then, I'll leave...'\n\n'I'll leave and come back stronger.'\n\n'Secure the help of someone stronger than me, or gain more allies... Either way, I must come back with a guaranteed means of dealing with them once and for all.'
   PL:

## Jednostka wsparcia: Passives_Assist-exme
- plik gry: `Passives_Assist-exme.json`

397. [Jednostka wsparcia [40003801] — nazwa] 림버스 컴퍼니 제작 특수 의체 시제품 mk5 - 도깨비팔
   źródło: Passives_Assist-exme.json :: dataList[id=40003801].name
   limit: do 100 znaków
   EN: Limbus Company Specialized Custom Prosthetic Prototype mk5 - Dokkaebi Arms
   PL:
398. [Jednostka wsparcia [40003801] — opis] 스테이지 시작 시 [AengduNewArm] 얻음\n\n자신을 제외한 현재 체력이 최대 체력의 50% 미만인 아군이 있다면, [SupportProtect] 1 얻음 (턴당 1회)
   źródło: Passives_Assist-exme.json :: dataList[id=40003801].desc
   limit: do 200 znaków
   tokeny: zachowaj dokładnie: \n, [AengduNewArm], [SupportProtect]
   znaczenie tagów: [AengduNewArm] = 도깨비팔 / Dokkaebi Arms; [SupportProtect] = 원호 방어 / Assist Defense
   EN: Encounter Start: Gain [AengduNewArm]\n\nIf there is an ally at less than 50% HP on the field excluding this unit, gain 1 [SupportProtect] (once per turn)
   PL:
399. [Jednostka wsparcia [40003801] — podsumowanie] [SupportProtect] 얻음
   źródło: Passives_Assist-exme.json :: dataList[id=40003801].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SupportProtect]
   znaczenie tagów: [SupportProtect] = 원호 방어 / Assist Defense
   EN: Gain [SupportProtect]
   PL:
400. [Jednostka wsparcia [40003801] — tekst klimatyczny] “겉으로는 다른 둥지나 뒷골목에서 볼 수 있는 의체와 다를 바 없어 보이지만… 림버스 컴퍼니만의 기술이 들어갔다고 하네요. 림버스 컴퍼니만의 기술이라, 그게 뭘까요?”\n“이 시제품은 LCD 부서를 주축으로 만들어졌으니 당연히 뒤틀림의 힘과 연관되었을 것 같은데... 아. 저는 운반 업무를 맡았을 뿐이라, 잘 알진 못합니다. 어디까지나 추측이죠. 아무튼 평범한 신체 강화용 의체는 아닐 겁니다.”
   źródło: Passives_Assist-exme.json :: dataList[id=40003801].flavor
   limit: do 800 znaków
   tokeny: zachowaj dokładnie: \n
   EN: "On the outside, it looks no different from prostheses you might find in other Nests or Backstreets... But apparently, this particular prosthetic limb has been created using technology unique to Limbus Company. I wonder what that could be..."\n\n"Since the development of this prototype was led by the LCD Department, I would assume it has something to do with the power of Distortions... Oh, that's not to say that I have any certainty regarding the matter—I was only in charge of transporting it, you see. It's just a simple speculation, really. In any case, I doubt this is your average prosthetic limb meant for body enhancement."
   PL:
401. [Jednostka wsparcia [40003802] — nazwa] 귀화요격
   źródło: Passives_Assist-exme.json :: dataList[id=40003802].name
   limit: do 40 znaków
   EN: Demonfire Spinecleaver
   PL:
402. [Jednostka wsparcia [40003802] — opis] 스킬 종료 시 [Breath] 3당, [WindBlade] 1 얻음 (최대 5, 턴당 2회)\n\n기본 공격 스킬 종료 시 [WindBlade]이 15 이상이면, 적에게 ‘상전 청린화’ 발동 (턴당 1회)\n\n수비 스킬 합 패배 시 [Agility]이 3 이상이면, 수비 스킬 종료 시까지 피해로 인해 흐트러짐 상태가 되지 않으며, 피격후 적에게 ‘골단’ 발동 (턴당 2회, 강제 흐트러짐 제외)
   źródło: Passives_Assist-exme.json :: dataList[id=40003802].desc
   limit: do 580 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [WindBlade], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [WindBlade] = 묵 공방 - 예[銳] 2식 발도 / 추력:도깨비불 / Mook Workshop - Ye [銳] Type II Bladedraw / Thrust Force: Dokkaebi Fire; [Agility] = 신속 / Haste
   EN: Skill End: Gain 1 [WindBlade] for every 3 [Breath] (max 5, 2 times per turn)\n\nOn Base Attack Skill End: At 15+ [WindBlade], activate "Even the Balance - Lucent Rippling Flame" on the enemy (once per turn)\n\nOn Defense Skill Clash Lose, if this unit has 3+ [Agility], this unit cannot be Staggered from taking damage until Defense Skill End, and activate "To Claim Their Bones" against the enemy after being hit (2 times per turn, excluding forced Staggers)
   PL:
403. [Jednostka wsparcia [40003802] — podsumowanie] 조건 만족 시 추가 스킬 발동
   źródło: Passives_Assist-exme.json :: dataList[id=40003802].summary
   limit: do 120 znaków
   EN: Activate additional Skill when conditions are met
   PL:
404. [Jednostka wsparcia [40003803] — nazwa] 쾌검
   źródło: Passives_Assist-exme.json :: dataList[id=40003803].name
   limit: do 40 znaków
   EN: Swiftblade
   PL:
405. [Jednostka wsparcia [40003803] — opis] 크리티컬 적중 시 다음 턴에 [Agility] 1 얻음 (스킬당 3회, 턴당 2회)
   źródło: Passives_Assist-exme.json :: dataList[id=40003803].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: On Crit, gain 1 [Agility] next turn (3 times per Skill, 2 times per turn)
   PL:
406. [Jednostka wsparcia [40003803] — podsumowanie] [Agility] 얻음
   źródło: Passives_Assist-exme.json :: dataList[id=40003803].summary
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Gain [Agility]
   PL:
407. [Jednostka wsparcia [40003804] — nazwa] 돌아가야 할 곳
   źródło: Passives_Assist-exme.json :: dataList[id=40003804].name
   limit: do 40 znaków
   EN: To Where I Must Return
   PL:
408. [Jednostka wsparcia [40003804] — opis] 자신을 제외한 아군 검계 소속 인원이 3명 이상 사망한 경우\n- 자신의 스킬, 코인 효과로 [Breath] 위력, 횟수를 얻을 때, [Breath] 위력, 횟수 1 추가 증가\n- 아군 검계 소속 인원이 5명 이상 사망한 경우, 대신 2 증가\n- 전투 시작 시 자신에게 [SwordPlayOfTheHomeland] 부여
   źródło: Passives_Assist-exme.json :: dataList[id=40003804].desc
   limit: do 390 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [SwordPlayOfTheHomeland]
   znaczenie tagów: [Breath] = 호흡 / Poise; [SwordPlayOfTheHomeland] = 본국검술 / Swordplay of the Homeland
   EN: When 3 or more other Blade Lineage allies are defeated:\n- When gaining [Breath] Potency/Count using this unit's own Skills and Coin effects: Gain 1 more of each\n- When 5 or more other Blade Lineage allies are defeated, gain 2 more of each instead\n- Combat Start: Apply [SwordPlayOfTheHomeland] on self
   PL:
409. [Jednostka wsparcia [40004001] — nazwa] 도망자
   źródło: Passives_Assist-exme.json :: dataList[id=40004001].name
   limit: do 40 znaków
   EN: Fugitive
   PL:
410. [Jednostka wsparcia [40004001] — opis] 스테이지 첫 등장 시 [BrandedKimSatgat] 얻음
   źródło: Passives_Assist-exme.json :: dataList[id=40004001].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [BrandedKimSatgat]
   znaczenie tagów: [BrandedKimSatgat] = 낙인[奴] / Brand - No [奴]
   EN: Upon entering the Encounter for the first time, gain [BrandedKimSatgat]
   PL:
411. [Jednostka wsparcia [40004002] — nazwa] 살수본위
   źródło: Passives_Assist-exme.json :: dataList[id=40004002].name
   limit: do 40 znaków
   EN: Bearing of a Salsu
   PL:
412. [Jednostka wsparcia [40004002] — opis] 자신의 [Breath] 횟수가 1이면, [Breath] 횟수가 감소하지 않는 대신 자신의 체력 10 감소 (이 효과로 흐트러지지 않고, 체력이 1 미만이 되지 않음)\n\n기본 스킬의 크리티컬 피해량이 (자신의 잃은 체력 비율 / 2)만큼 증가함 (최대 50%)
   źródło: Passives_Assist-exme.json :: dataList[id=40004002].desc
   limit: do 310 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: At 1 [Breath] Count, lose 10 HP instead of losing [Breath] Count (this effect cannot Stagger this unit and does not drop this unit's HP below 1)\n\nDeal +(missing HP percentage on self / 2) damage on Critical Hit using Base Skills (max 50%)
   PL:
413. [Jednostka wsparcia [40004003] — nazwa] 본국검술
   źródło: Passives_Assist-exme.json :: dataList[id=40004003].name
   limit: do 40 znaków
   EN: Swordplay of the Homeland
   PL:
414. [Jednostka wsparcia [40004003] — opis] 전투 시작 시 오만 공명이 발동했으면,\n- [Breath] (오만 공명 수 x 2) 얻음 (최대 8)\n- 자신을 제외한 모든 수감자 및 조력자에게 [SlashResultUp] 1, [CriticalDamageUp] 1 부여 (대상이 검계 소속이면, 2배로 부여함)\n\n턴 종료 시 다음 턴에 (자신의 [Breath] / 4)만큼 [Agility] 얻음 (최대 6, 소수점 버림)
   źródło: Passives_Assist-exme.json :: dataList[id=40004003].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [Breath], [SlashResultUp], [CriticalDamageUp], [Agility]
   znaczenie tagów: [Breath] = 호흡 / Poise; [SlashResultUp] = 참격 위력 증가 / Slash Power Up; [CriticalDamageUp] = 크리티컬 피해량 증가 / Crit DMG Up; [Agility] = 신속 / Haste
   EN: Combat Start: If Pride Reson. was activated,\n- Gain (Pride Reson. x 2) [Breath] (max 8)\n- Apply 1 [SlashResultUp] and 1 [CriticalDamageUp] on all Sinners and Assist Units excluding this unit (for Blade Lineage targets, double this effect)\n\nTurn End: Gain ([Breath] on self / 4) [Agility] next turn (max 6, rounded down)
   PL:
415. [Jednostka wsparcia [40004004] — nazwa] 검계 우두머리
   źródło: Passives_Assist-exme.json :: dataList[id=40004004].name
   limit: do 40 znaków
   EN: Blade Lineage Mentor
   PL:
416. [Jednostka wsparcia [40004004] — opis] 자신의 스킬 및 코인 효과로 [Breath] 위력, 횟수를 얻을 때, 자신을 제외한 [Breath]이 없거나 [Breath] 위력이 가장 낮은 수감자 및 조력자 2명에게 [Breath] 위력 1, [Breath] 횟수 1 증가\n- 아군이 검계 소속이면, 대신 [Breath] 위력 3, [Breath] 횟수 2 증가\n\n검계 소속 수감자 및 조력자 사망시 자신의 정신력 10 감소
   źródło: Passives_Assist-exme.json :: dataList[id=40004004].desc
   limit: do 520 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: When gaining [Breath] Potency/Count using this unit's own Skills and Coin effects: Apply 1 [Breath] Potency and 1 [Breath] Count on the Sinner and 2 Assist Units that do not have [Breath] or have the lowest [Breath] Potency (excluding this unit)\n- For Blade Lineage allies, apply 3 [Breath] Potency and +2 [Breath] Count instead\n\nWhen a Blade Lineage Sinner or Assist Unit is defeated, this unit loses 10 SP
   PL:
417. [Jednostka wsparcia [40004005] — nazwa] 육참골단
   źródło: Passives_Assist-exme.json :: dataList[id=40004005].name
   limit: do 50 znaków
   EN: Yield My Flesh to Claim Their Bones
   PL:
418. [Jednostka wsparcia [40004005] — opis] 이번 전투에서 체력이 0이 되는 피해를 받았을 때, 해당 피해를 받지 않고, 해당 턴 동안 체력이 1로 유지됨 (전투당 1회)\n\n턴 종료 시 [Breath] 위력이 30 이상이면, 다음 턴에 속도 20으로 고정하고 맨 왼쪽 슬롯에 ‘육참’ 장착\n- 스킬 효과로 '육참'을 사용할 수 없으면, 이 효과는 발동하지 않음
   źródło: Passives_Assist-exme.json :: dataList[id=40004005].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: In this Encounter, when this unit takes damage that brings its HP down to 0, nullify that damage; then, this unit's HP cannot drop below 1 for the turn (once per Encounter)\n\nTurn End: At 30+ [Breath] Potency, fix this unit's Speed to 20 next turn and equip "Yield My Flesh" on the leftmost Skill Slot\n- If "Yield My Flesh" becomes inaccessible due to Skill effect, this effect does not activate
   PL:
419. [Jednostka wsparcia [40004006] — nazwa] 운명 이탈
   źródło: Passives_Assist-exme.json :: dataList[id=40004006].name
   (powtórzenie elementu 269 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
420. [Jednostka wsparcia [40004006] — opis] 이 유닛 사망 시 전투 패배
   źródło: Passives_Assist-exme.json :: dataList[id=40004006].desc
   (powtórzenie elementu 270 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
421. [Jednostka wsparcia [40004006] — tekst klimatyczny] 길을 잘못 들 수는 있어도, 흐름을 거스르거나 이탈하는 것은 ‘그것’에 따라 금지되어 있다.
   źródło: Passives_Assist-exme.json :: dataList[id=40004006].flavor
   (powtórzenie elementu 271 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
422. [Jednostka wsparcia [40003901] — nazwa] 차원가방 [에즈라]
   źródło: Passives_Assist-exme.json :: dataList[id=40003901].name
   (powtórzenie elementu 339 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
423. [Jednostka wsparcia [40003901] — opis] 스테이지 시작시 [DimensionalBagEzraA]을 1 얻음\n\n현재 사용하는 공방 무기 스킬을 1회 이상 사용했으면, 다음 턴에 공방 무기를 교체함\n\n사용 공방 무기\n- 알라스 공방 장갑\n- 네스터 공방 망치\n- 스크류 아틀리에제 드릴 망치\n- 나미르 공방 건틀릿\n- 유리아 공방 도끼
   źródło: Passives_Assist-exme.json :: dataList[id=40003901].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [DimensionalBagEzraA]
   znaczenie tagów: [DimensionalBagEzraA] = 차원가방 - 알라스 공방 / Dimensional Bag - Allas Workshop
   EN: Encounter Start: Gain 1 [DimensionalBagEzraA]\n\nIf this unit used the current Workshop weapon more than once, switch weapons the next turn\n\nList of weapons:\n- Allas Workshop Gloves\n- Nester Workshop Hammer\n- Screw Atelier Drill Hammer\n- Namir Workshop Gauntlets\n- YuRia Atelier Axe
   PL:

## Jednostka wsparcia: Passives_Assist-twth
- plik gry: `Passives_Assist-twth.json`

424. [Jednostka wsparcia [40003701] — nazwa] 열선 무기
   źródło: Passives_Assist-twth.json :: dataList[id=40003701].name
   limit: do 40 znaków
   EN: Thermal Weapon
   PL:
425. [Jednostka wsparcia [40003701] — opis] 스테이지 시작시 [HeatingWireOffSpider]를 가지고 시작함\n\n턴 시작 시 자신이 보유한 [ReinforcedTattooSpiderDaughterTwo]이 2 이상이면 [HeatingWireOnSpiderTwo]으로 바뀌고, [Laceration]을 부여하는 스킬로 [Combustion]을 추가로 부여함
   źródło: Passives_Assist-twth.json :: dataList[id=40003701].desc
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n, [HeatingWireOffSpider], [ReinforcedTattooSpiderDaughterTwo], [HeatingWireOnSpiderTwo], [Laceration], [Combustion]
   znaczenie tagów: [HeatingWireOffSpider] = 열선 OFF / Thermal Blades OFF; [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos; [HeatingWireOnSpiderTwo] = 열선 ON / Thermal Blades ON; [Laceration] = 출혈 / Bleed; [Combustion] = 화상 / Burn
   EN: Begins Encounter with [HeatingWireOffSpider]\n\nTurn Start: At 2+ [ReinforcedTattooSpiderDaughterTwo], gain [HeatingWireOnSpiderTwo] and also inflict [Combustion] with Skills that inflict [Laceration]
   PL:
426. [Jednostka wsparcia [40003702] — nazwa] <s>중지</s>
   źródło: Passives_Assist-twth.json :: dataList[id=40003702].name
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle</s>
   PL:
427. [Jednostka wsparcia [40003702] — opis] 스킬 2개가 적중했으면, [ReinforcedTattooSpiderDaughterTwo] 1 얻음 (적중 횟수는 누적됨)
   źródło: Passives_Assist-twth.json :: dataList[id=40003702].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [ReinforcedTattooSpiderDaughterTwo]
   znaczenie tagów: [ReinforcedTattooSpiderDaughterTwo] = 중지식 강화문신 / The Middle Styled Augmentation Tattoos
   EN: If this unit hit with more than 2 Skills, gain 1 [ReinforcedTattooSpiderDaughterTwo] for every excess Skill that hit
   PL:
428. [Jednostka wsparcia [40003703] — nazwa] 원한
   źródło: Passives_Assist-twth.json :: dataList[id=40003703].name
   limit: do 40 znaków
   EN: Resentment
   PL:
429. [Jednostka wsparcia [40003703] — opis] 스킬 피격 시 [ResentmentSpiderDaughterTwo] 2 얻음 (스킬당 1회)\n\n아군이 피격 시 [ResentmentSpiderDaughterTwo] 1 얻음 (스킬당 1회)\n\n[ResentmentSpiderDaughterTwo]이 최댓값이면 강력한 공격을 사용함\n\n턴 종료시 체력이 80%, 60%, 40% 미만이면, [ResentmentSpiderDaughterTwo] 최댓값으로 획득함
   źródło: Passives_Assist-twth.json :: dataList[id=40003703].desc
   limit: do 410 znaków
   tokeny: zachowaj dokładnie: \n, [ResentmentSpiderDaughterTwo]
   znaczenie tagów: [ResentmentSpiderDaughterTwo] = 중지 - 원한 / The Middle - Grudge
   EN: When hit by a Skill, gain 2 [ResentmentSpiderDaughterTwo] (once per Skill)\n\nWhen an ally is hit, gain 1 [ResentmentSpiderDaughterTwo] (once per Skill)\n\nAt max [ResentmentSpiderDaughterTwo] Stack, use a powerful attack\n\nTurn End: At less than 80% / 60% / 40% HP, max out this unit's [ResentmentSpiderDaughterTwo] Stack
   PL:

## Jednostka wsparcia: Passives_Assist-walpu6
- plik gry: `Passives_Assist-walpu6.json`

430. [Jednostka wsparcia [40000301] — nazwa] 사랑과 정의의 이름으로~ 지금 이 곳에 등장!
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000301].name
   limit: do 80 znaków
   EN: In the name of Love and Justice~ Here comes Magical Girl!
   PL:
431. [Jednostka wsparcia [40000301] — opis] 등장 시 모든 수감자에게 [ResultEnhancement] 1 부여\n흐트러짐 상태가 되지 않음
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000301].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [ResultEnhancement]
   znaczenie tagów: [ResultEnhancement] = 위력 증가 / Power Up
   EN: Upon entry, apply 1 [ResultEnhancement] to all Sinners\nCannot be Staggered
   PL:
432. [Jednostka wsparcia [40000302] — nazwa] 모두들, 너무 고마워!
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000302].name
   limit: do 40 znaków
   EN: Thanks so much, everyone!
   PL:
433. [Jednostka wsparcia [40000302] — opis] 아르카나[TabExplain] 슬레이브가 적중한 대상에게 [WornOutKnight]가 있을 경우 턴 종료 시 제압에 성공함
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000302].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [WornOutKnight]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight
   EN: If the target that ARCANA[TabExplain] SLAVE hit has [WornOutKnight], wins Suppression at Turn End
   PL:
434. [Jednostka wsparcia [40000303] — nazwa] 나도… 결국 다른 사람들이랑 똑같았던거야?
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000303].name
   limit: do 60 znaków
   EN: In the end, I'm... just like the others?
   PL:
435. [Jednostka wsparcia [40000303] — opis] 아르카나[TabExplain] 슬레이브가 적중한 대상에게 [WornOutKnight]가 없을 경우 모든 아군에게 [FailedToAssistQueen]를 부여함
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000303].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [WornOutKnight], [FailedToAssistQueen]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight; [FailedToAssistQueen] = 내가… 무슨 쓸모…야? / What use... am I...?
   EN: If the target that ARCANA[TabExplain] SLAVE hit does not have [WornOutKnight], apply [FailedToAssistQueen] to all allies
   PL:
436. [Jednostka wsparcia [40000304] — nazwa] 사랑과 정의의 힘
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000304].name
   limit: do 40 znaków
   EN: Power of Love and Justice
   PL:
437. [Jednostka wsparcia [40000304] — opis] 자신의 [PowerOfLoveAndJustice]의 횟수가 10 이상이면, 다음 턴에 횟수를 10 감소하고 [PowerOfLoveAndJustice]의 위력을 1 얻음\n\n자신의 [PowerOfLoveAndJustice]의 위력이 3이면, [Burst] 위력 부여 시 대상의 [Burst] 횟수도 1 추가로 증가 시킴 (턴 당 2회)
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000304].desc
   limit: do 300 znaków
   tokeny: zachowaj dokładnie: \n, [PowerOfLoveAndJustice], [Burst]
   znaczenie tagów: [PowerOfLoveAndJustice] = 사랑/정의 / Love/Justice; [Burst] = 파열 / Rupture
   EN: At 10+ [PowerOfLoveAndJustice] Count: lose 10 of its Count and gain 1 [PowerOfLoveAndJustice] Potency next turn\n\nAt 3 [PowerOfLoveAndJustice] Potency: when inflicting [Burst] Potency, inflict 1 [Burst] Count as well (2 times per turn)
   PL:
438. [Jednostka wsparcia [40000305] — nazwa] 나도… 결국 다른 사람들이랑 똑같았던거야?
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000305].name
   (powtórzenie elementu 434 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
439. [Jednostka wsparcia [40000305] — opis] 아르카나[TabExplain] 슬레이브가 적중한 대상에게 [WornOutKnight]가 없고 대상의 체력이 600 이하가 아닐 경우 모든 아군에게 [FailedToAssistQueen]를 부여함
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000305].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [WornOutKnight], [FailedToAssistQueen]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight; [FailedToAssistQueen] = 내가… 무슨 쓸모…야? / What use... am I...?
   EN: If the target that ARCANA[TabExplain] SLAVE hit does not have [WornOutKnight] and isn't at 600- HP, apply [FailedToAssistQueen] to all allies
   PL:
440. [Jednostka wsparcia [40000306] — nazwa] 모두들, 너무 고마워!
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000306].name
   (powtórzenie elementu 432 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
441. [Jednostka wsparcia [40000306] — opis] 아르카나[TabExplain] 슬레이브가 적중한 대상에게 [WornOutKnight]가 있고 대상의 체력이 600 이하일 경우 턴 종료 시 제압에 성공함
   źródło: Passives_Assist-walpu6.json :: dataList[id=40000306].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [TabExplain], [WornOutKnight]
   znaczenie tagów: [WornOutKnight] = 닳디 닳은 기사 / Weathered Knight
   EN: If the target that ARCANA[TabExplain] SLAVE hit has [WornOutKnight] and 600- HP, wins Suppression at Turn End
   PL:

## Jednostka wsparcia: Passives_Assist
- plik gry: `Passives_Assist.json`

442. [Jednostka wsparcia [40000101] — nazwa] 파상흡환
   źródło: Passives_Assist.json :: dataList[id=40000101].name
   limit: do 50 znaków
   EN: Bursting Strike, Breathing Siphon
   PL:
443. [Jednostka wsparcia [40000101] — opis] 자신의 공격 스킬로 대상 처치 시 대상이 가지고 있던, [Burst]만큼 [Breath]을 얻음 (최대 5)
   źródło: Passives_Assist.json :: dataList[id=40000101].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Burst], [Breath]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Breath] = 호흡 / Poise
   EN: On Kill with this unit's Attack Skill, gain [Breath] equal to [Burst] on the target (max 5)
   PL:
444. [Jednostka wsparcia [40000102] — nazwa] 파초환단
   źródło: Passives_Assist.json :: dataList[id=40000102].name
   limit: do 40 znaków
   EN: Ba Jiao Banana Bolus
   PL:
445. [Jednostka wsparcia [40000102] — opis] 부여하는 [Burst] 위력 혹은 [Burst] 횟수 +1 (턴 당 2 회)\n공격 대상보다 공격 레벨이 높을 경우, 합 위력 +1
   źródło: Passives_Assist.json :: dataList[id=40000102].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Burst]
   znaczenie tagów: [Burst] = 파열 / Rupture
   EN: Inflict +1 more [Burst] Potency or [Burst] Count (2 times per turn)\nIf this unit's Offense Level is higher than the target's, Clash Power +1
   PL:
446. [Jednostka wsparcia [40000103] — nazwa] 금강환단
   źródło: Passives_Assist.json :: dataList[id=40000103].name
   (powtórzenie elementu 238 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
447. [Jednostka wsparcia [40000103] — opis] 합 패배 시, [DefenseUp] 3 얻음 (턴 당 2회)
   źródło: Passives_Assist.json :: dataList[id=40000103].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Clash Lose: gain 3 [DefenseUp] (2 times per turn)
   PL:

## Umiejętności jednostek wsparcia — Skills_Assist-Cultivation
- plik gry: `Skills_Assist-Cultivation.json`

448. [Umiejętność sojusznika [40000501] (ulepszenie 1) — nazwa] 적참
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].name
   limit: do 40 znaków
   EN: Crimson Cleave
   PL:
449. [Umiejętność sojusznika [40000501] (ulepszenie 1) — opis] [WhenUse] 대상의 [Burst] 3당 기본 위력 +1 (최대 2)
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Burst] = 파열 / Rupture
   EN: [WhenUse] Base Power +1 for every 3 [Burst] on the target (max 2)
   PL:
450. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 3 [Laceration]
   PL:
451. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [DefenseDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: [OnSucceedAttack] Inflict 3 [DefenseDown]
   PL:
452. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Breath]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Breath] = 호흡 / Poise
   EN: [CriticalOnSucceedAttack] Gain +2 [Breath] Count
   PL:
453. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttackHead] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttackHead], [Laceration]
   znaczenie tagów: [OnSucceedAttackHead] = [앞면 적중시] / [Heads Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttackHead] Inflict +2 [Laceration] Count
   PL:
454. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [DefenseDown] 3 부여
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 451 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
455. [Umiejętność sojusznika [40000501] (ulepszenie 1) — moneta 2, efekt 3 — opis] [CriticalOnSucceedAttack] [Breath] 횟수 2 증가
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000501].levelList[level=1].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 452 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
456. [Umiejętność sojusznika [40000502] (ulepszenie 1) — nazwa] 취수낭랑
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000502].levelList[level=1].name
   limit: do 60 znaków
   EN: Plastered Sleep, Unrestrained Ripples
   PL:
457. [Umiejętność sojusznika [40000502] (ulepszenie 1) — opis] 속도에 상관없이 공격 대상을 자신으로 변경할 수 있음\n[WhenUse] [Breath] 3당, 기본 위력 +1 (최대 3)\n[WhenUse] 대상의 부정적인 효과 1개당, 기본 위력 +3 (최대 9)\n[WhenUse] 다음 턴에 [Agility] 5 얻음 (턴 당 1회)\n[WhenUse] [Breath] 10 얻음,[Breath] 횟수 2 증가
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000502].levelList[level=1].desc
   limit: do 360 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [Agility] = 신속 / Haste
   EN: Can draw any attack to this unit regardless of Speed\n[WhenUse] Base Power +1 for every 3 [Breath] (max 3)\n[WhenUse] Base Power +3 for every type of negative effect on target (max 9)\n[WhenUse] Gain 5 [Agility] next turn (once per turn)\n[WhenUse] Gain 10 [Breath] and +2 [Breath] Count
   PL:
458. [Umiejętność sojusznika [40000502] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 7 부여, [Laceration] 횟수 2 증가
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000502].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 7 [Laceration] and +2 [Laceration] Count
   PL:
459. [Umiejętność sojusznika [40000502] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Paralysis] 3 부여
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000502].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Paralysis]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Paralysis] = 마비 / Paralyze
   EN: [OnSucceedAttack] Inflict 3 [Paralysis] next turn
   PL:
460. [Umiejętność sojusznika [40000502] (ulepszenie 1) — moneta 1, efekt 3 — opis] [CriticalOnSucceedAttack] 피해량 +300%
   źródło: Skills_Assist-Cultivation.json :: dataList[id=40000502].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]
   EN: [CriticalOnSucceedAttack] Deal +300% damage
   PL:

## Umiejętności jednostek wsparcia — Skills_Assist-a1c10p2
- plik gry: `Skills_Assist-a1c10p2.json`

461. [Umiejętność sojusznika [40004101] (ulepszenia 1–3) — nazwa] 붉은 못
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=1].name ; dataList[id=40004101].levelList[level=2].name ; dataList[id=40004101].levelList[level=3].name
   limit: do 40 znaków
   EN: Crimson Nail
   PL:
462. [Umiejętność sojusznika [40004101] (ulepszenia 1–2) — opis] [WhenUse] 대상의 [Laceration] 4당, 기본 위력 +1 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=1].desc ; dataList[id=40004101].levelList[level=2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Base Power +1 for every 4 [Laceration] on target (max 2)
   PL:
463. [Umiejętność sojusznika [40004101] (ulepszenia 1–3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004101].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=40004101].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict 2 [Laceration]
   PL:
464. [Umiejętność sojusznika [40004101] (ulepszenia 1–3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40004101].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=40004101].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BloodyMucusAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BloodyMucusAlly] = 세례[적] / Baptism [Crimson]
   EN: [OnSucceedAttack] Inflict 1 [BloodyMucusAlly]
   PL:
465. [Umiejętność sojusznika [40004101] (ulepszenia 2–3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 위력 2당, [BloodyMucusAlly] 1 부여 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=40004101].levelList[level=3].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ChargeRouge], [BloodyMucusAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ChargeRouge] = 맥동 / Pulsation; [BloodyMucusAlly] = 세례[적] / Baptism [Crimson]
   EN: [OnSucceedAttack] Inflict 1 [BloodyMucusAlly] for every 2 [ChargeRouge] Potency (max 2)
   PL:
466. [Umiejętność sojusznika [40004101] (ulepszenia 2–3) — moneta 2, efekt 1 — opis] 정신력이 없는 대상이면, 피해량 +50%
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=40004101].levelList[level=3].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   EN: Against non-SP units, deal +50% damage
   PL:
467. [Umiejętność sojusznika [40004101] (ulepszenia 2–3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 정신력 10 감소
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=40004101].levelList[level=3].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target loses 10 SP
   PL:
468. [Umiejętność sojusznika [40004101] (ulepszenie 3) — opis] [WhenUse] 대상의 [Laceration] 4당, 기본 위력 +1 (최대 2)\n[WhenUse] 대상보다 정신력이 높거나 대상에게 정신력이 없으면, 코인 위력 +1
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=3].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Base Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] If this unit has higher SP than the target, or if target is a non-SP unit, Coin Power +1
   PL:
469. [Umiejętność sojusznika [40004101] (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004101].levelList[level=3].coinlist[#1].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BuffetGold]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BuffetGold] = 황금계시 / Golden Revelation
   EN: [OnSucceedAttack] Inflict 1 [BuffetGold]
   PL:
470. [Umiejętność sojusznika [40004102] (ulepszenia 1–3) — nazwa] 저리가
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].name ; dataList[id=40004102].levelList[level=2].name ; dataList[id=40004102].levelList[level=3].name
   limit: do 40 znaków
   EN: Go Away
   PL:
471. [Umiejętność sojusznika [40004102] (ulepszenie 1) — opis] [WhenUse] 대상의 [Laceration] 4당, 코인 위력 +1 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)
   PL:
472. [Umiejętność sojusznika [40004102] (ulepszenia 1–3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004102].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=40004102].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +2 [Laceration] Count
   PL:
473. [Umiejętność sojusznika [40004102] (ulepszenia 1–3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40004102].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=40004102].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
474. [Umiejętność sojusznika [40004102] (ulepszenia 1–3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=40004102].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=40004102].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
475. [Umiejętność sojusznika [40004102] (ulepszenia 1–3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=40004102].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=40004102].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
476. [Umiejętność sojusznika [40004102] (ulepszenia 2–3) — opis] [WhenUse] 대상의 [Laceration] 4당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRouge] 위력 2당, 가중치 +1 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=2].desc ; dataList[id=40004102].levelList[level=3].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] Coin Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] Gain +1 Atk Weight for every 2 [ChargeRouge] Potency on self (max 2)
   PL:
477. [Umiejętność sojusznika [40004102] (ulepszenia 2–3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 위력 2당, [BloodyMucusAlly] 1 부여 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=2].coinlist[#0].coindescs[#2].desc ; dataList[id=40004102].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
478. [Umiejętność sojusznika [40004102] (ulepszenia 2–3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] 자신의 [ChargeRouge] 위력 2당, [BloodyMucusAlly] 1 부여 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=2].coinlist[#1].coindescs[#2].desc ; dataList[id=40004102].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 465 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
479. [Umiejętność sojusznika [40004102] (ulepszenie 3) — moneta 1, efekt 4 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=3].coinlist[#0].coindescs[#3].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
480. [Umiejętność sojusznika [40004102] (ulepszenie 3) — moneta 2, efekt 4 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004102].levelList[level=3].coinlist[#1].coindescs[#3].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
481. [Umiejętność sojusznika [40004103] (ulepszenia 1–4) — nazwa] 힘내
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=1].name ; dataList[id=40004103].levelList[level=2].name ; dataList[id=40004103].levelList[level=3].name ; dataList[id=40004103].levelList[level=4].name
   limit: do 40 znaków
   EN: Perk Up
   PL:
482. [Umiejętność sojusznika [40004103] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   PL:
483. [Umiejętność sojusznika [40004103] (ulepszenia 1–3) — moneta 1, efekt 1 — opis] [EndCoin] [ParryingResultUp] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004103].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=40004103].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [ParryingResultUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: [EndCoin] Apply 1 [ParryingResultUp]
   PL:
484. [Umiejętność sojusznika [40004103] (ulepszenia 1–3) — moneta 1, efekt 2 — opis] [EndCoin] 자신의 [ChargeRouge] 위력 1당, [AttackUp] 1 부여 (최대 5)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40004103].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=40004103].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [ChargeRouge], [AttackUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ChargeRouge] = 맥동 / Pulsation; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [EndCoin] Apply 1 [AttackUp] for every [ChargeRouge] Potency on self (max 5)
   PL:
485. [Umiejętność sojusznika [40004103] (ulepszenie 2) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] 자신의 [ChargeRouge] 위력 2당, 가중치 +1 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=2].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [ChargeRouge]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] Gain +1 Atk Weight for every 2 [ChargeRouge] Potency on self (max 2)
   PL:
486. [Umiejętność sojusznika [40004103] (ulepszenia 3–4) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] 자신의 [ChargeRouge] 위력 2당, 가중치 +1 (최대 2)\n[EndSkill] 자신에게 [GourmandiseAlly] 효과가 있고 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 최대 10 소모하고 적중한 모든 대상에게 [SkillPowerUp] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=3].desc ; dataList[id=40004103].levelList[level=4].desc
   limit: do 370 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [ChargeRouge], [EndSkill], [GourmandiseAlly], [SkillPowerUp]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [EndSkill] = [공격 종료시] / [Attack End]; [GourmandiseAlly] = 폭주 / Uncontrollable Rampage; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] Gain +1 Atk Weight for every 2 [ChargeRouge] Potency on self (max 2)\n[EndSkill] If this unit has [GourmandiseAlly], and at 10+ [ChargeRouge] Count, consume up to 10 [ChargeRouge] and apply 1 [SkillPowerUp] to all targets that were hit
   PL:
487. [Umiejętność sojusznika [40004103] (ulepszenie 4) — moneta 1, efekt 1 — opis] [EndCoin] [SkillPowerUp] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=4].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [SkillPowerUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [SkillPowerUp] = 기본 위력 증가 / Base Power Up
   EN: [EndCoin] Apply 1 [SkillPowerUp]
   PL:
488. [Umiejętność sojusznika [40004103] (ulepszenie 4) — moneta 1, efekt 2 — opis] [EndCoin] 자신의 [ChargeRouge] 위력 1당, 이번 턴과 다음 턴에 [AttackUp] 1 부여 (최대 5)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004103].levelList[level=4].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [EndCoin], [ChargeRouge], [AttackUp]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ChargeRouge] = 맥동 / Pulsation; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [EndCoin] Apply 1 [AttackUp] this turn and next turn for every [ChargeRouge] Potency on self (max 5)
   PL:
489. [Umiejętność sojusznika [40004104] (ulepszenia 1–3) — nazwa] 아프지마
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=1].name ; dataList[id=40004104].levelList[level=2].name ; dataList[id=40004104].levelList[level=3].name
   limit: do 40 znaków
   EN: Don't Get Hurty
   PL:
490. [Umiejętność sojusznika [40004104] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=1].desc
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
491. [Umiejętność sojusznika [40004104] (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [EndCoin] (이 스킬 최종 위력 x 2)만큼 대상의 체력 회복\n- 르루주 소속이면, 대신 체력을 감소시키고, 그 수치만큼 자신의 체력 회복 (해당 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004104].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Heal (Skill Final Power x 2) HP on target\n- If target is a "Le Rouge" unit, consume their HP instead and heal self by the same amount (damage dealt by this effect does not Stagger or reduce the target's HP below 1)
   PL:
492. [Umiejętność sojusznika [40004104] (ulepszenie 2) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] 자신의 [ChargeRouge] 위력이 3 이상이면, 가중치 +2
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=2].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [ChargeRouge]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] At 3+ [ChargeRouge] Potency, gain +2 Atk Weight
   PL:
493. [Umiejętność sojusznika [40004104] (ulepszenie 2) — moneta 1, efekt 2 — opis] [EndCoin] 이 스킬 최종 위력만큼 대상의 정신력 회복\n- 정신력이 최댓값이면, 해제 가능한 부정적인 효과 중 무작위 1개 제거
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Heal (Skill Final Power) SP on target\n- If target is at max SP, remove 1 removable negative effect applied on target
   PL:
494. [Umiejętność sojusznika [40004104] (ulepszenie 3) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] 자신의 [ChargeRouge] 위력이 3 이상이면, 가중치 +4
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=3].desc
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [ChargeRouge]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] At 3+ [ChargeRouge] Potency, gain +4 Atk Weight
   PL:
495. [Umiejętność sojusznika [40004104] (ulepszenie 3) — moneta 1, efekt 1 — opis] [EndCoin] (이 스킬 최종 위력 x 2)만큼 대상의 체력 회복\n- 대상의 최대 체력의 (자신의 [ChargeRouge] 위력 x 2)%만큼 추가로 체력 회복\n- 르루주 소속이면, 대신 체력을 감소시키고, 그 수치만큼 자신의 체력 회복 (해당 효과로 흐트러지거나 체력이 1 미만으로 감소하지 않음)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=3].coinlist[#0].coindescs[#0].desc
   limit: do 380 znaków
   tokeny: zachowaj dokładnie: \n, [EndCoin], [ChargeRouge]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ChargeRouge] = 맥동 / Pulsation
   EN: [EndCoin] Heal (Skill Final Power x 2) HP on target\n- Additionally heal ([ChargeRouge] Potency on self x 2)% HP on target\n- If target is a "Le Rouge" unit, consume their HP instead and heal self by the same amount (damage dealt by this effect does not Stagger or reduce the target's HP below 1)
   PL:
496. [Umiejętność sojusznika [40004104] (ulepszenie 3) — moneta 1, efekt 2 — opis] [EndCoin] 이 스킬 최종 위력만큼 대상의 정신력 회복\n- (자신의 [ChargeRouge] 위력 x 3)만큼 추가로 정신력 회복\n- 정신력이 최댓값이면, 해제 가능한 부정적인 효과 중 무작위 1개 제거
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004104].levelList[level=3].coinlist[#0].coindescs[#1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [EndCoin], [ChargeRouge]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]; [ChargeRouge] = 맥동 / Pulsation
   EN: [EndCoin] Heal (Skill Final Power) SP on target\n- Additionally heal ([ChargeRouge] Potency on self x 3) SP on target\n- If target is at max SP, remove 1 removable negative effect applied on target
   PL:
497. [Umiejętność sojusznika [40004105] (ulepszenia 1–2) — nazwa] 내 손 잡아
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=1].name ; dataList[id=40004105].levelList[level=2].name
   limit: do 40 znaków
   EN: Grab My Hand
   PL:
498. [Umiejętność sojusznika [40004105] (ulepszenie 1) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] 다음 턴에 [Binding] 5 얻음
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [CantChangeTarget], [SupportAlly], [WhenUse], [Binding]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [SupportAlly] = 양극성 / Duality; [WhenUse] = [사용시] / [On Use]; [Binding] = 속박 / Bind
   EN: [CantDuel]\n[CantChangeTarget]\n[SupportAlly]\n\n[WhenUse] Gain 5 [Binding] next turn
   PL:
499. [Umiejętność sojusznika [40004105] (ulepszenia 1–2) — moneta 1, efekt 1 — opis] [EndCoin] 대상의 흐트러짐 상태 해제
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004105].levelList[level=2].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Recover target from Stagger
   PL:
500. [Umiejętność sojusznika [40004105] (ulepszenia 1–2) — moneta 1, efekt 2 — opis] [EndCoin] 이 스킬 최종 위력만큼 대상의 체력 회복
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40004105].levelList[level=2].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Heal HP on target equal to this Skill's Final Power
   PL:
501. [Umiejętność sojusznika [40004105] (ulepszenie 2) — opis] [CantDuel]\n[CantChangeTarget]\n[SupportAlly]
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=2].desc
   (powtórzenie elementu 482 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
502. [Umiejętność sojusznika [40004105] (ulepszenie 2) — moneta 1, efekt 3 — opis] [EndCoin] 다음 턴에 대상의 최대 체력의 50%만큼 보호막 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004105].levelList[level=2].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [EndCoin]
   znaczenie tagów: [EndCoin] = [이 코인 공격 종료 시] / [Current Coin Attack End]
   EN: [EndCoin] Apply Shield next turn equal to 50% of target's max HP
   PL:
503. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — nazwa] 붉은못 세례
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].name ; dataList[id=40004106].levelList[level=2].name ; dataList[id=40004106].levelList[level=3].name
   limit: do 40 znaków
   EN: Baptism of Crimson Nails
   PL:
504. [Umiejętność sojusznika [40004106] (ulepszenie 1) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 최대 10 소모하고 가중치 +2, 코인 위력 +2
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].desc
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: [WhenUse], [ChargeRouge]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation
   EN: [WhenUse] At 10+ [ChargeRouge] Count, consume up to 10 [ChargeRouge] Count to gain +2 Atk Weight and Coin Power +2
   PL:
505. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#0].coindescs[#0].desc ; dataList[id=40004106].levelList[level=2].coinlist[#0].coindescs[#0].desc ; dataList[id=40004106].levelList[level=3].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
506. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#0].coindescs[#1].desc ; dataList[id=40004106].levelList[level=2].coinlist[#0].coindescs[#1].desc ; dataList[id=40004106].levelList[level=3].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
507. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#1].coindescs[#0].desc ; dataList[id=40004106].levelList[level=2].coinlist[#1].coindescs[#0].desc ; dataList[id=40004106].levelList[level=3].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
508. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 2 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#1].coindescs[#1].desc ; dataList[id=40004106].levelList[level=2].coinlist[#1].coindescs[#1].desc ; dataList[id=40004106].levelList[level=3].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 463 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Umiejętność sojusznika [40004106] (ulepszenia 1–3) — moneta 3, efekt 1 — opis] [OnSucceedAttack] [BloodyMucusAlly] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#2].coindescs[#0].desc ; dataList[id=40004106].levelList[level=2].coinlist[#2].coindescs[#0].desc ; dataList[id=40004106].levelList[level=3].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 464 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
510. [Umiejętność sojusznika [40004106] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
511. [Umiejętność sojusznika [40004106] (ulepszenie 2) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 최대 10 소모하고 가중치 +2, 코인 위력 +2\n[WhenUse] 대상의 [Laceration] 4당, 기본 위력 +1 (최대 2)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=2].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 10+ [ChargeRouge] Count, consume up to 10 [ChargeRouge] Count to gain +2 Atk Weight and Coin Power +2\n[WhenUse] Base Power +1 for every 4 [Laceration] on target (max 2)
   PL:
512. [Umiejętność sojusznika [40004106] (ulepszenia 2–3) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=2].coinlist[#2].coindescs[#1].desc ; dataList[id=40004106].levelList[level=3].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Inflict +3 [Laceration] Count
   PL:
513. [Umiejętność sojusznika [40004106] (ulepszenie 3) — opis] [WhenUse] 자신의 [ChargeRouge] 횟수가 10 이상이면, [ChargeRouge] 횟수를 최대 10 소모하고 가중치 +2, 코인 위력 +2\n[WhenUse] 대상의 [Laceration] 4당, 기본 위력 +1 (최대 2)\n[WhenUse] 자신의 [ChargeRouge] 위력이 5 이상이면, 다음 효과가 적용됨\n- 가중치 +2\n- 코인 위력 +(자신의 [ChargeRouge] 위력 - 3)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=3].desc
   limit: do 420 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [ChargeRouge], [Laceration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [ChargeRouge] = 맥동 / Pulsation; [Laceration] = 출혈 / Bleed
   EN: [WhenUse] At 10+ [ChargeRouge] Count, consume up to 10 [ChargeRouge] Count to gain +2 Atk Weight and Coin Power +2\n[WhenUse] Base Power +1 for every 4 [Laceration] on target (max 2)\n[WhenUse] At 5+ [ChargeRouge] Potency, apply the following effects:\n- Gain +2 Atk Weight\n- Gain Coin Power +([ChargeRouge] Potency on self - 3)
   PL:
514. [Umiejętność sojusznika [40004106] (ulepszenie 3) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=3].coinlist[#0].coindescs[#2].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
515. [Umiejętność sojusznika [40004106] (ulepszenie 3) — moneta 2, efekt 3 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=3].coinlist[#1].coindescs[#2].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
516. [Umiejętność sojusznika [40004106] (ulepszenie 3) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [BuffetGold] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004106].levelList[level=3].coinlist[#2].coindescs[#2].desc
   (powtórzenie elementu 469 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
517. [Umiejętność sojusznika [40004107] (ulepszenie 1) — nazwa] 내가 끝내줄게…
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004107].levelList[level=1].name
   limit: do 40 znaków
   EN: I'll End It for You...
   PL:
518. [Umiejętność sojusznika [40004107] (ulepszenie 1) — opis] [CantDuel]\n대상의 잃은 체력 1%당, 피해량 +0.5% (최대 30%)\n[WhenUse] 자신에게 [GourmandiseAlly] 효과가 있으면, 가중치 +1
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004107].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [GourmandiseAlly]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [GourmandiseAlly] = 폭주 / Uncontrollable Rampage
   EN: [CantDuel]\nDeal +0.5% damage for every 1% missing HP on target (max 30%)\n[WhenUse] If this unit has [GourmandiseAlly], gain +1 Atk Weight
   PL:
519. [Umiejętność sojusznika [40004107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 1 부여
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 1 [Binding] next turn
   PL:
520. [Umiejętność sojusznika [40004107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신에게 [GourmandiseAlly] 효과가 있으면, 이 코인 재사용 (최대 1회)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [GourmandiseAlly]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [GourmandiseAlly] = 폭주 / Uncontrollable Rampage
   EN: [OnSucceedAttack] If this unit has [GourmandiseAlly], Reuse this Coin (1 time max)
   PL:
521. [Umiejętność sojusznika [40004201] (ulepszenie 1) — nazwa] 라 노제(la nausée)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004201].levelList[level=1].name
   limit: do 40 znaków
   EN: La Nausée
   PL:
522. [Umiejętność sojusznika [40004201] (ulepszenie 1) — opis] [StartBattle] 자신의 [ChargeRouge] 횟수를 모두 소모하여, 자신을 포함한 모든 아군의 체력을 최대 체력의 ([ChargeRouge] 횟수 소모값)%만큼 회복
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004201].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ChargeRouge]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeRouge] = 맥동 / Pulsation
   EN: [StartBattle] Consume all [ChargeRouge] Count on self and heal ([ChargeRouge] Count consumed)% HP on all allies, including this unit
   PL:
523. [Umiejętność sojusznika [40004201] (ulepszenie 1) — tekst klimatyczny] 신으로 성장하는 과정에서 필연적으로 겪는 감각. 누군가는 현기증으로, 누군가는 구역질로, 누군가는 발작으로, 누군가는 기만으로 그리고 누군가는 거부로. 세상 모든것이 어지럽고 두렵고 혼란스럽다. 이것을 견뎌내기 위해, 이것은 아직 경계적으로 흐려지지 않은 자신의 것들을 지켜내기 위해 무엇이라도 토해내며 지키려한다.
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004201].levelList[level=1].flavor
   limit: do 460 znaków
   tokeny: zachowaj dokładnie: \n
   EN: The inevitable growing pains for those who are maturing into gods.\n\nThis sensation takes many forms: vertigo, nausea, seizure, self-deception... and to some, refusal. To them, the world is full of terror and alienating chaos. To endure the nausea, to protect those that are yet their own and those that are yet to become superfluous, the nascent god vomits.
   PL:
524. [Umiejętność sojusznika [40004202] (ulepszenie 1) — nazwa] 르 트루 루주(le Trou rouge)
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004202].levelList[level=1].name
   limit: do 40 znaków
   EN: Le Trou Rouge
   PL:
525. [Umiejętność sojusznika [40004202] (ulepszenie 1) — opis] [StartBattle] [ChargeRouge] 횟수 4 얻음
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004202].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [StartBattle], [ChargeRouge]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [ChargeRouge] = 맥동 / Pulsation
   EN: [StartBattle] Gain +4 [ChargeRouge] Count
   PL:
526. [Umiejętność sojusznika [40004202] (ulepszenie 1) — tekst klimatyczny] 이것은 붉은 구멍이다. 닫혀있지만 이것은 구멍과 같이 끝없는 허기로 구멍이 채워지길 원한다. 그렇게 기대받은대로, 그렇게 태어나져버린대로.
   źródło: Skills_Assist-a1c10p2.json :: dataList[id=40004202].levelList[level=1].flavor
   limit: do 280 znaków
   tokeny: zachowaj dokładnie: \n
   EN: This is a crimson hollow.\nThough it is closed, the endless hunger lingers, desiring the impossible satiation.\n\nFor that is what the others expect this being to be. For that is the purpose for which this being was born.
   PL:

## Umiejętności jednostek wsparcia — Skills_Assist-a1c8p2
- plik gry: `Skills_Assist-a1c8p2.json`

527. [Umiejętność sojusznika [40000201] (ulepszenie 1) — nazwa] 빈틈찌르기
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000201].levelList[level=1].name
   limit: do 40 znaków
   EN: Weakness Thrust
   PL:
528. [Umiejętność sojusznika [40000201] (ulepszenie 1) — opis] [WhenUse] 대상이 보유한 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 1 증가\n[OnDirectAttack] [Burst] 횟수 1 증가
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000201].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath], [OnDirectAttack], [Burst]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise; [OnDirectAttack] = [일방 공격 시] / [On Unopposed Attack]; [Burst] = 파열 / Rupture
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Gain +1 [Breath] Count\n[OnDirectAttack] Inflict +1 [Burst] Count
   PL:
529. [Umiejętność sojusznika [40000201] (ulepszenie 1) — moneta 1, efekt 1 — opis] 크리티컬 피해량 +30%
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000201].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   EN: +30% Damage on Critical Hit
   PL:
530. [Umiejętność sojusznika [40000201] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000201].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 2 [Burst]
   PL:
531. [Umiejętność sojusznika [40000202] (ulepszenie 1) — nazwa] 복검중충
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].name
   limit: do 50 znaków
   EN: Dualblade Substitution Thrust
   PL:
532. [Umiejętność sojusznika [40000202] (ulepszenie 1) — opis] [StartBattle] [Protection] 1 얻음\n[WhenUse] 대상이 보유한 부정적인 효과가 3개 이상이면, 코인 위력 +1\n[WhenUse] [Breath] 위력 3 얻음
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [StartBattle], [Protection], [WhenUse], [Breath]
   znaczenie tagów: [StartBattle] = [전투 시작시] / [Combat Start]; [Protection] = 보호 / Protection; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [StartBattle] Gain 1 [Protection]\n[WhenUse] If target has 3+ types of negative effects, Coin Power +1\n[WhenUse] Gain 3 [Breath] Potency
   PL:
533. [Umiejętność sojusznika [40000202] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict +2 [Burst] Count
   PL:
534. [Umiejętność sojusznika [40000202] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 1 얻음
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Breath]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Breath] = 호흡 / Poise
   EN: [OnSucceedAttack] Gain +1 [Breath] Count
   PL:
535. [Umiejętność sojusznika [40000202] (ulepszenie 1) — moneta 3, efekt 1 — opis] 크리티컬 피해량 +50%
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   EN: +50% Damage on Critical Hit
   PL:
536. [Umiejętność sojusznika [40000202] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Burst] 3 부여
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000202].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Burst]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Burst] = 파열 / Rupture
   EN: [OnSucceedAttack] Inflict 3 [Burst]
   PL:
537. [Umiejętność sojusznika [40000203] (ulepszenie 1) — nazwa] 가척아원
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].name
   limit: do 40 znaków
   EN: Aiding Strike
   PL:
538. [Umiejętność sojusznika [40000203] (ulepszenie 1) — opis] [WhenUse] 대상이 보유한 부정적인 효과가 3개 이상이면, 코인 위력 +1\n[WhenUse] 자신의 [Breath] 횟수 3 증가\n[WhenUse] [Breath] 위력 6 얻음
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [WhenUse] If target has 3+ types of negative effects, Coin Power +1\n[WhenUse] Gain +3 [Breath] Count\n[WhenUse] Gain 6 [Breath] Potency
   PL:
539. [Umiejętność sojusznika [40000203] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Burst] 횟수 2 증가
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 533 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
540. [Umiejętność sojusznika [40000203] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Breath] 횟수 1 얻음
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 534 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
541. [Umiejętność sojusznika [40000203] (ulepszenie 1) — moneta 3, efekt 1 — opis] [CriticalOnSucceedAttack] [Burst] 2 부여
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].coinlist[#2].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Inflict 2 [Burst]
   PL:
542. [Umiejętność sojusznika [40000203] (ulepszenie 1) — moneta 4, efekt 1 — opis] 크리티컬 피해량 +100%
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].coinlist[#3].coindescs[#0].desc
   limit: do 120 znaków
   EN: +100% Damage on Critical Hit
   PL:
543. [Umiejętność sojusznika [40000203] (ulepszenie 1) — moneta 4, efekt 2 — opis] [CriticalOnSucceedAttack] [Burst] 5 부여
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000203].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [CriticalOnSucceedAttack], [Burst]
   znaczenie tagów: [CriticalOnSucceedAttack] = [크리티컬 적중 시] / [On Crit]; [Burst] = 파열 / Rupture
   EN: [CriticalOnSucceedAttack] Inflict 5 [Burst]
   PL:
544. [Umiejętność sojusznika [40000204] (ulepszenie 1) — nazwa] 방호
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000204].levelList[level=1].name
   limit: do 40 znaków
   EN: Defend
   PL:
545. [Umiejętność sojusznika [40000204] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] 자신에게 부여된 해제 가능한 부정적인 효과 중 무작위 1개 제거\n[StartBattle] 정신력 10 회복\n[WhenUse] [ProtectStance] 2 얻음
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000204].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [StartBattle], [WhenUse], [ProtectStance]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [WhenUse] = [사용시] / [On Use]; [ProtectStance] = 보호 태세 / Protective Stance
   EN: [CanDuelGuard]\n[StartBattle] Remove 1 random removable negative effect applied to self\n[StartBattle] Heal 10 SP\n[WhenUse] Gain 2 [ProtectStance]
   PL:
546. [Umiejętność sojusznika [40000204] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c8p2.json :: dataList[id=40000204].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SuperCoin]
   znaczenie tagów: [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: [SuperCoin]
   PL:

## Umiejętności jednostek wsparcia — Skills_Assist-a1c9p2
- plik gry: `Skills_Assist-a1c9p2.json`

547. [Umiejętność sojusznika [40000601] (ulepszenie 1) — nazwa] 견제
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000601].levelList[level=1].name
   limit: do 40 znaków
   EN: Obstruction
   PL:
548. [Umiejętność sojusznika [40000601] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 2당 기본 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000601].levelList[level=1].desc
   limit: do 240 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [Vibration], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Breath] = 호흡 / Poise
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] Base Power +1 for every 2 ([Laceration] + [Vibration]) on target (max 5)\n[WhenUse] Gain +3 [Breath] Count
   PL:
549. [Umiejętność sojusznika [40000601] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000601].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 5 [Vibration]
   PL:
550. [Umiejętność sojusznika [40000601] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000601].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
551. [Umiejętność sojusznika [40000602] (ulepszenie 1) — nazwa] 이연삭
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000602].levelList[level=1].name
   limit: do 40 znaków
   EN: Double Chaincleave
   PL:
552. [Umiejętność sojusznika [40000602] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 2당 기본 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000602].levelList[level=1].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
553. [Umiejętność sojusznika [40000602] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000602].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
554. [Umiejętność sojusznika [40000602] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000602].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +3 [Vibration] Count
   PL:
555. [Umiejętność sojusznika [40000603] (ulepszenie 1) — nazwa] 작살 투척
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000603].levelList[level=1].name
   limit: do 40 znaków
   EN: Harpoon Throw
   PL:
556. [Umiejętność sojusznika [40000603] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 200%)\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 2 얻음
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000603].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CriticalDmgUpVespa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CriticalDmgUpVespa] = 섬봉광검술 - 환도 / Apic Flashburst Blade Art - Hwando
   EN: Deal +50% damage for every type of negative effect on target (max 200%)\n[WhenUse] Gain 2 [CriticalDmgUpVespa] next turn
   PL:
557. [Umiejętność sojusznika [40000603] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000603].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
558. [Umiejętność sojusznika [40000603] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BeeSting] 부여
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000603].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BeeSting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BeeSting] = 박힌 작살 [벌침] / Nested Harpoon [Beesting]
   EN: [OnSucceedAttack] Inflict [BeeSting]
   PL:
559. [Umiejętność sojusznika [40000603] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 80%만큼 흐트러짐 손상을 입힘
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000603].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 80% of damage dealt
   PL:
560. [Umiejętność sojusznika [40000604] (ulepszenie 1) — nazwa] 작살 심기 - 거기입니까.
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000604].levelList[level=1].name
   limit: do 50 znaków
   EN: Harpoon Impalement - There It Is.
   PL:
561. [Umiejętność sojusznika [40000604] (ulepszenie 1) — opis] [CantChangeTarget]\n대상의 부정적인 효과 종류 당 피해량 +50% (최대 300%)\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 5 얻음
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000604].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CantChangeTarget], [WhenUse], [CriticalDmgUpVespa]
   znaczenie tagów: [CantChangeTarget] = [대상 변경 불가] / [Target Fixed]; [WhenUse] = [사용시] / [On Use]; [CriticalDmgUpVespa] = 섬봉광검술 - 환도 / Apic Flashburst Blade Art - Hwando
   EN: [CantChangeTarget]\nDeal +50% damage for every type of negative effect on target (max 300%)\n[WhenUse] Gain 5 [CriticalDmgUpVespa] next turn
   PL:
562. [Umiejętność sojusznika [40000604] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000604].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
563. [Umiejętność sojusznika [40000604] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [ArtifactBeeSting] 부여
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000604].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ArtifactBeeSting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ArtifactBeeSting] = 박힌 작살 [말벌침] / Nested Harpoon [Waspsting]
   EN: [OnSucceedAttack] Inflict [ArtifactBeeSting]
   PL:
564. [Umiejętność sojusznika [40000604] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 대상을 흐트러짐 상태로 만듦
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000604].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Stagger target
   PL:
565. [Umiejętność sojusznika [40000605] (ulepszenie 1) — nazwa] 작살 회수
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000605].levelList[level=1].name
   limit: do 40 znaków
   EN: Harpoon Recall
   PL:
566. [Umiejętność sojusznika [40000605] (ulepszenie 1) — opis] [CantDuel]\n대상의 부정적인 효과 종류 당 피해량 +50% (최대 200%)
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000605].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nDeal +50% damage for every type of negative effect on target (max 200%)
   PL:
567. [Umiejętność sojusznika [40000605] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 박힌 작살 제거
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000605].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Remove the Nested Harpoon on target
   PL:
568. [Umiejętność sojusznika [40000606] (ulepszenie 1) — nazwa] 되받아치죠.
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000606].levelList[level=1].name
   limit: do 40 znaków
   EN: Counterattack.
   PL:
569. [Umiejętność sojusznika [40000606] (ulepszenie 1) — opis] [DuelCounter]\n대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[StartBattle] <color=#ff6000><mark color=#ff000040><b><u>[SupportProtect] 1 얻음</color></mark></b></u>\n[WhenUse] 다음 턴에 [ResultEnhancement] 2, [AttackDmgUp] 2 얻음
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000606].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [DuelCounter], [StartBattle], [SupportProtect], [WhenUse], [ResultEnhancement], [AttackDmgUp]
   znaczenie tagów: [DuelCounter] = [합 가능 반격] / [Clashable Counter]; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WhenUse] = [사용시] / [On Use]; [ResultEnhancement] = 위력 증가 / Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: [DuelCounter]\nDeal +50% damage for every type of negative effect on target (max 100%)\n[StartBattle] <color=#ff6000><mark color=#ff000040><b><u>Gain 1 [SupportProtect]</color></mark></b></u>\n[WhenUse] Gain 2 [ResultEnhancement] and 2 [AttackDmgUp] next turn
   PL:
570. [Umiejętność sojusznika [40000606] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000606].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
571. [Umiejętność sojusznika [40000606] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000606].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
572. [Umiejętność sojusznika [40000607] (ulepszenie 1) — nazwa] 원호하겠습니다.
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000607].levelList[level=1].name
   limit: do 40 znaków
   EN: Defensive Assist.
   PL:
573. [Umiejętność sojusznika [40000607] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000607].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill
   PL:
574. [Umiejętność sojusznika [40000607] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p2.json :: dataList[id=40000607].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Umiejętności jednostek wsparcia — Skills_Assist-a1c9p3
- plik gry: `Skills_Assist-a1c9p3.json`

575. [Umiejętność sojusznika [40000901] (ulepszenie 1) — nazwa] 견제
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000901].levelList[level=1].name
   (powtórzenie elementu 547 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
576. [Umiejętność sojusznika [40000901] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 2당 기본 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000901].levelList[level=1].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
577. [Umiejętność sojusznika [40000901] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000901].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
578. [Umiejętność sojusznika [40000901] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000901].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
579. [Umiejętność sojusznika [40000902] (ulepszenie 1) — nazwa] 이연삭
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000902].levelList[level=1].name
   (powtórzenie elementu 551 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
580. [Umiejętność sojusznika [40000902] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Laceration]과 [Vibration]의 합 2당 기본 위력 +1 (최대 5)\n[WhenUse] 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000902].levelList[level=1].desc
   (powtórzenie elementu 548 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
581. [Umiejętność sojusznika [40000902] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Laceration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000902].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 512 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
582. [Umiejętność sojusznika [40000902] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000902].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
583. [Umiejętność sojusznika [40000903] (ulepszenie 1) — nazwa] 작살 투척
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000903].levelList[level=1].name
   (powtórzenie elementu 555 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
584. [Umiejętność sojusznika [40000903] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 200%)\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 2 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000903].levelList[level=1].desc
   (powtórzenie elementu 556 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
585. [Umiejętność sojusznika [40000903] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000903].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
586. [Umiejętność sojusznika [40000903] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [BeeSting] 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000903].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 558 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
587. [Umiejętność sojusznika [40000903] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 40%만큼 흐트러짐 손상을 입힘
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000903].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 40% of damage dealt
   PL:
588. [Umiejętność sojusznika [40000904] (ulepszenie 1) — nazwa] 작살 심기 - 거기입니까.
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000904].levelList[level=1].name
   (powtórzenie elementu 560 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
589. [Umiejętność sojusznika [40000904] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 300%)\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 5 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000904].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CriticalDmgUpVespa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CriticalDmgUpVespa] = 섬봉광검술 - 환도 / Apic Flashburst Blade Art - Hwando
   EN: Deal +50% damage for every type of negative effect on target (max 300%)\n[WhenUse] Gain 5 [CriticalDmgUpVespa] next turn
   PL:
590. [Umiejętność sojusznika [40000904] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000904].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
591. [Umiejętność sojusznika [40000904] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [ArtifactBeeSting] 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000904].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 563 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
592. [Umiejętność sojusznika [40000904] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] 피해량의 60%만큼 흐트러짐 손상을 입힘
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000904].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Raise Stagger Threshold by 60% of damage dealt
   PL:
593. [Umiejętność sojusznika [40000905] (ulepszenie 1) — nazwa] 작살 회수
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000905].levelList[level=1].name
   (powtórzenie elementu 565 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
594. [Umiejętność sojusznika [40000905] (ulepszenie 1) — opis] [CantDuel]\n박힌 작살을 보유한 캐릭터를 타겟팅함 (대상이 없으면 스킬 취소)\n대상의 부정적인 효과 종류 당 피해량 +50% (최대 200%)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000905].levelList[level=1].desc
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]
   EN: [CantDuel]\nTargets the unit that has Nested Harpoon (cancel this Skill when there are no available target)\nDeal +50% damage for every type of negative effect on target (max 200%)
   PL:
595. [Umiejętność sojusznika [40000905] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 대상의 박힌 작살 제거
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000905].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 567 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
596. [Umiejętność sojusznika [40000906] (ulepszenie 1) — nazwa] 되받아치죠.
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000906].levelList[level=1].name
   (powtórzenie elementu 568 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
597. [Umiejętność sojusznika [40000906] (ulepszenie 1) — opis] [DuelCounter]\n대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[StartBattle] <color=#ff6000><mark color=#ff000040><b><u>[SupportProtect] 1 얻음</color></mark></b></u>\n[WhenUse] 다음 턴에 [ResultEnhancement] 2, [AttackDmgUp] 2 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000906].levelList[level=1].desc
   (powtórzenie elementu 569 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
598. [Umiejętność sojusznika [40000906] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000906].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 549 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
599. [Umiejętność sojusznika [40000906] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000906].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 554 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
600. [Umiejętność sojusznika [40000907] (ulepszenie 1) — nazwa] 원호하겠습니다.
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000907].levelList[level=1].name
   (powtórzenie elementu 572 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
601. [Umiejętność sojusznika [40000907] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WinDuel] 아군 정신력 4 상승 (본인 포함)\n- LCD 소속이면, 대신 정신력 8 상승
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000907].levelList[level=1].desc
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [CanDuelGuard], [SupportProtect], [WinDuel]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [SupportProtect] = 원호 방어 / Assist Defense; [WinDuel] = [합 승리시] / [Clash Win]
   EN: [CanDuelGuard]\n[SupportProtect] exclusive Skill\n[WinDuel] Heal 4 SP for all allies (including this unit)\n- Heal 8 SP instead for LCD Faction
   PL:
602. [Umiejętność sojusznika [40000907] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000907].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
603. [Umiejętność sojusznika [40000908] (ulepszenie 1) — nazwa] 황봉침[黄蜂針]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].name
   limit: do 40 znaków
   EN: Yellow Apic Stinger [黄蜂針]
   PL:
604. [Umiejętność sojusznika [40000908] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 3 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [CriticalDmgUpVespa]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [CriticalDmgUpVespa] = 섬봉광검술 - 환도 / Apic Flashburst Blade Art - Hwando
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] Gain 3 [CriticalDmgUpVespa] next turn
   PL:
605. [Umiejętność sojusznika [40000908] (ulepszenie 1) — tekst klimatyczny] <color=#fde55d>“저항할 생각조차 마시죠”</color>
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>
   EN: <color=#fde55d>"Do not even think about resisting."</color>
   PL:
606. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
607. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
608. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
609. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
610. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
611. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상에게 [BeeSting] 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BeeSting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BeeSting] = 박힌 작살 [벌침] / Nested Harpoon [Beesting]
   EN: [OnSucceedAttack] Inflict [BeeSting] on target
   PL:
612. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
613. [Umiejętność sojusznika [40000908] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [BeeSting] 제거
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000908].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [BeeSting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [BeeSting] = 박힌 작살 [벌침] / Nested Harpoon [Beesting]
   EN: [OnSucceedAttack] Remove [BeeSting] on the target
   PL:
614. [Umiejętność sojusznika [40000909] (ulepszenie 1) — nazwa] 궁그닐
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].name
   limit: do 40 znaków
   EN: Gungnir
   PL:
615. [Umiejętność sojusznika [40000909] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Vibration] 위력 10당 피해량 +20%\n[BeforeAttack] 대상의 체력이 50% 미만이면, 이 스킬에서 [VibrationExplosion] 적중시 진동 횟수가 감소하지 않음\n[WhenUse] 정신력이 0 이상이면, 망(望) 하나를 생성함\n- 코인 위력 +1, 피해량 +50%\n[WhenUse] 다음 턴에 [CriticalDmgUpVespa] 3 얻음\n[EndSkill] 망(望)을 생성했으면, 정신력 2만큼 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].desc
   limit: do 560 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [BeforeAttack], [VibrationExplosion], [CriticalDmgUpVespa], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [CriticalDmgUpVespa] = 섬봉광검술 - 환도 / Apic Flashburst Blade Art - Hwando; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] Deal +20% damage for every 10 [Vibration] Potency on target\n[BeforeAttack] If target is at less than 50% HP, [VibrationExplosion] triggered by this Skill does not consume Tremor Count\n[WhenUse] At 0+ SP, generate 1 Mang (望)\n- Coin Power +1, deal +50% damage\n[WhenUse] Gain 3 [CriticalDmgUpVespa] next turn\n[EndSkill] If this Skill generated Mang (望), lose 2 SP
   PL:
616. [Umiejętność sojusznika [40000909] (ulepszenie 1) — tekst klimatyczny] <color=#fde55d>“반드시 맞추고, 반드시 뚫겠습니다.”</color>
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].flavor
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#fde55d>, </color>
   EN: <color=#fde55d>"This throw will strike and pierce through without fail."</color>
   PL:
617. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
618. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
619. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
620. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
621. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
622. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion]; then, reduce target's [Vibration] Count by 1
   PL:
623. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
624. [Umiejętność sojusznika [40000909] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상에게 [ArtifactBeeSting] 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000909].levelList[level=1].coinlist[#3].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [ArtifactBeeSting]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [ArtifactBeeSting] = 박힌 작살 [말벌침] / Nested Harpoon [Waspsting]
   EN: [OnSucceedAttack] Inflict [ArtifactBeeSting] on target
   PL:
625. [Umiejętność sojusznika [40000910] (ulepszenie 1) — nazwa] 공간참 - 섬봉광검[空間斬 - 閃蜂光劍]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].name
   limit: do 70 znaków
   EN: Rend Space - Apic Flashburst Blade [空間斬 - 閃蜂光劍]
   PL:
626. [Umiejętność sojusznika [40000910] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류 당 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Laceration] 위력 10당 피해량 +20%\n[WhenUse] 정신력이 0 이상이면, 망(望) 두개를 생성함\n- 코인 위력 +2, 피해량 +100%\n[BeforeAttack] 대상의 체력이 50% 미만이면, 이 스킬에서 [Laceration]을 발동할 때 출혈 횟수가 감소하지 않음\n[EndSkill] 망(望)을 생성했으면, 정신력 3만큼 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].desc
   limit: do 490 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Laceration], [BeforeAttack], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Laceration] = 출혈 / Bleed; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] Deal +20% damage for every 10 [Laceration] Potency on target\n[WhenUse] At 0+ SP, generate 2 Mang (望)\n- Coin Power +2, deal +100% damage\n[BeforeAttack] If target is at less than 50% HP, [Laceration] triggered by this Skill does not consume Bleed Count\n[EndSkill] If this Skill generated Mang (望), lose 3 SP
   PL:
627. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
628. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Laceration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Laceration] = 출혈 / Bleed
   EN: [OnSucceedAttack] Activate [Laceration] on target once. Target loses 1 [Laceration] Count
   PL:
629. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
630. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
631. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
632. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
633. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
634. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
635. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 5, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#4].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
636. [Umiejętność sojusznika [40000910] (ulepszenie 1) — moneta 5, efekt 2 — opis] [OnSucceedAttack] 대상을 흐트러짐 상태로 만듦
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000910].levelList[level=1].coinlist[#4].coindescs[#1].desc
   (powtórzenie elementu 564 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
637. [Umiejętność sojusznika [40001001] (ulepszenie 1) — nazwa] 붉은 숨: 절삭
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001001].levelList[level=1].name
   limit: do 40 znaków
   EN: Red Breath: Incision
   PL:
638. [Umiejętność sojusznika [40001001] (ulepszenie 1) — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%\n[WhenUse] 자신의 정신력 3 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001001].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]
   EN: If target has a negative effect, deal +50% damage\n[WhenUse] Lose 3 SP
   PL:
639. [Umiejętność sojusznika [40001001] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 피해 +5
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001001].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 5 bonus damage
   PL:
640. [Umiejętność sojusznika [40001001] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 피해 +5
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001001].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 639 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
641. [Umiejętność sojusznika [40001002] (ulepszenie 1) — nazwa] 하얀 숨: 안개. 새벽. 숨겨짐 - 정신 보호
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001002].levelList[level=1].name
   limit: do 80 znaków
   EN: White Breath: Fog. Dawn. Concealment - Safeguard the Mind
   PL:
642. [Umiejętność sojusznika [40001002] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아군을 타겟팅 하고 수비 스킬을 발동시키지 않고 피해를 주지 않음\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001002].levelList[level=1].desc
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CantDuel]\nThis Skill targets allies, does not trigger Defense Skills, and does not deal damage\n[WhenUse] Gain 5 [Breath] and +3 [Breath] Count
   PL:
643. [Umiejętność sojusznika [40001002] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 공격 대상의 정신력 15 회복
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001002].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Target heals 15 SP
   PL:
644. [Umiejętność sojusznika [40001002] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신과 공격 대상에게 [MosesWhiteBreathMental] 2 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001002].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MosesWhiteBreathMental]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MosesWhiteBreathMental] = 하얀 숨 - 정신 보호 / White Breath - Safeguard the Mind
   EN: [OnSucceedAttack] Apply 2 [MosesWhiteBreathMental] on self and target
   PL:
645. [Umiejętność sojusznika [40001003] (ulepszenie 1) — nazwa] 붉은 숨: 육체. 피. 가속. 경화 - 신체 강화
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001003].levelList[level=1].name
   limit: do 100 znaków
   EN: Red Breath: Body. Blood. Acceleration. Hardening - Strengthen the Body
   PL:
646. [Umiejętność sojusznika [40001003] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아군을 타겟팅 하고 수비 스킬을 발동시키지 않고 피해를 주지 않음\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001003].levelList[level=1].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
647. [Umiejętność sojusznika [40001003] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신과 공격 대상에게 [MosesRedBreathBody] 2, [AttackUp] 1, [DefenseUp] 1 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001003].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MosesRedBreathBody], [AttackUp], [DefenseUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MosesRedBreathBody] = 붉은 숨 - 육체 강화 / Red Breath - Strengthen the Body; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: [OnSucceedAttack] Apply 2 [MosesRedBreathBody], 1 [AttackUp], 1 [DefenseUp] on self and target
   PL:
648. [Umiejętność sojusznika [40001004] (ulepszenie 1) — nazwa] 보라색 숨: 성마른. 지끈거림. 조여오는 것 - 억압
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].name
   limit: do 80 znaków
   EN: Purple Breath: Impatience. Aching. Tightening - Oppress
   PL:
649. [Umiejętność sojusznika [40001004] (ulepszenie 1) — opis] 이 스킬은 대상의 수비 스킬을 발동시키지 않음\n대상에게 부정적인 효과가 있으면, 피해량 +50%\n[WhenUse] 자신의 정신력 8 감소\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].desc
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Breath]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: This Skill does not trigger the target's Defense Skill\nIf target has a negative effect, deal +50% damage\n[WhenUse] Lose 8 SP\n[WhenUse] Gain 5 [Breath] and +3 [Breath] Count
   PL:
650. [Umiejętność sojusznika [40001004] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
651. [Umiejętność sojusznika [40001004] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 정신력 피해 8
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 8 SP damage
   PL:
652. [Umiejętność sojusznika [40001004] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [MosesPurpleBreathBind] 4, [Vulnerable] 2, [PlusCoinValueDown] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MosesPurpleBreathBind], [Vulnerable], [PlusCoinValueDown]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MosesPurpleBreathBind] = 보라색 숨 - 히스테릭 / Purple Breath - Hysteria; [Vulnerable] = 취약 / Fragile; [PlusCoinValueDown] = 더하기 코인 약화 / Plus Coin Drop
   EN: [OnSucceedAttack] Inflict 4 [MosesPurpleBreathBind], 2 [Vulnerable], 3 [PlusCoinValueDown]
   PL:
653. [Umiejętność sojusznika [40001004] (ulepszenie 1) — moneta 1, efekt 4 — opis] [OnSucceedAttack] 다음 턴에 [Binding] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001004].levelList[level=1].coinlist[#0].coindescs[#3].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Binding]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Binding] = 속박 / Bind
   EN: [OnSucceedAttack] Inflict 5 [Binding] next turn
   PL:
654. [Umiejętność sojusznika [40001005] (ulepszenie 1) — nazwa] 숨 고르기
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001005].levelList[level=1].name
   limit: do 40 znaków
   EN: Steady the Breath
   PL:
655. [Umiejętność sojusznika [40001005] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 적에게 적중하지 않고 수비 스킬을 발동시키지 않음\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001005].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [WhenUse], [Breath]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [WhenUse] = [사용시] / [On Use]; [Breath] = 호흡 / Poise
   EN: [CantDuel]\nThis Skill does not hit enemies and does not trigger Defense Skills\n[WhenUse] Gain 5 [Breath] and +3 [Breath] Count
   PL:
656. [Umiejętność sojusznika [40001006] (ulepszenie 1) — nazwa] 붉은 숨: 피. 근육. 수축 - 보호
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001006].levelList[level=1].name
   limit: do 70 znaków
   EN: Red Breath: Blood. Muscle. Contraction - Protect
   PL:
657. [Umiejętność sojusznika [40001006] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아군을 타겟팅 하고 수비 스킬을 발동시키지 않고 피해를 주지 않음\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001006].levelList[level=1].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
658. [Umiejętność sojusznika [40001006] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 자신과 공격 대상에게 [MosesRedBreathShield] 1, [Protection] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001006].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MosesRedBreathShield], [Protection]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MosesRedBreathShield] = 붉은 숨 - 보호 / Red Breath - Protect; [Protection] = 보호 / Protection
   EN: [OnSucceedAttack] Apply 1 [MosesRedBreathShield] and 5 [Protection] on self and target
   PL:
659. [Umiejętność sojusznika [40001007] (ulepszenie 1) — nazwa] ‘붉은 숨을 깊게 들이마신다.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001007].levelList[level=1].name
   limit: do 50 znaków
   EN: 'Inhale Deep the Red Breath.'
   PL:
660. [Umiejętność sojusznika [40001007] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 적에게 적중하지 않고, 수비 스킬을 발동시키지 않음\n[StartBattle] 보호막을 100 얻음 (전투당 1회)\n[StartBattle] <color=#ff6000><mark=#ff000040><b><u>[MosesRedBreathCharge] 1 얻음</u></b></mark></color>\n[EndBattle] 정신력 15 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001007].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [CantDuel], [StartBattle], [MosesRedBreathCharge], [EndBattle]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [StartBattle] = [전투 시작시] / [Combat Start]; [MosesRedBreathCharge] = 깊은 숨 - 붉은색 / Deep Breath - Red; [EndBattle] = [턴 종료 시] / [Turn End]
   EN: [CantDuel]\nThis Skill does not hit enemies and does not trigger Defense Skills\n[StartBattle] Gain 100 Shield (once per Encounter)\n[StartBattle]<color=#ff6000><mark=#ff000040><b><u>Gain 1 [MosesRedBreathCharge]</u></b></mark></color>\n[EndBattle] Lose 15 SP
   PL:
661. [Umiejętność sojusznika [40001008] (ulepszenie 1) — nazwa] 붉은 숨: 박동. 피. 경화. 분노. 충동 - 내달리는 몸
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001008].levelList[level=1].name
   limit: do 100 znaków
   EN: Red Breath: Pulse. Blood. Hardening. Anger. Urge - Push the Body's Limit
   PL:
662. [Umiejętność sojusznika [40001008] (ulepszenie 1) — opis] [CantDuel]\n이 스킬은 아군을 타겟팅 하고 수비 스킬을 발동시키지 않고 피해를 주지 않음\n[WhenUse] [Breath] 5 얻음, 자신의 [Breath] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001008].levelList[level=1].desc
   (powtórzenie elementu 642 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
663. [Umiejętność sojusznika [40001008] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [MosesRedBreathAttack] 1, [AttackUp] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001008].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [MosesRedBreathAttack], [AttackUp]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [MosesRedBreathAttack] = 붉은 숨 - 내달리는 몸 / Red Breath - Push the Body's Limit; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: [OnSucceedAttack] Apply 1 [MosesRedBreathAttack] and 5 [AttackUp]
   PL:
664. [Umiejętność sojusznika [40001101] (ulepszenie 1) — nazwa] 알라스 공방 - 가속 펀치!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001101].levelList[level=1].name
   limit: do 50 znaków
   EN: Allas Workshop - Acceleration Punch!
   PL:
665. [Umiejętność sojusznika [40001101] (ulepszenie 1) — opis] 자신의 속도가 6 이상이면 피해량 +50%\n[WhenUse] 다음 턴에 [Agility] 3 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001101].levelList[level=1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Agility]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Agility] = 신속 / Haste
   EN: At 6+ Speed, deal +50% damage\n[WhenUse] Gain 3 [Agility] next turn
   PL:
666. [Umiejętność sojusznika [40001101] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001101].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]
   EN: [OnSucceedAttack] Deal 3 Blunt bonus damage
   PL:
667. [Umiejętność sojusznika [40001101] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 추가 타격 피해 3
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001101].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 666 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
668. [Umiejętność sojusznika [40001102] (ulepszenie 1) — nazwa] 네스터 공방 - 하나! 둘! 확산!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].name
   limit: do 50 znaków
   EN: Nester Workshop - One! Two! Diffuse!
   PL:
669. [Umiejętność sojusznika [40001102] (ulepszenie 1) — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%\n[WhenUse] 대상의 [Vibration]이 5 이상이면, 코인 적중시 대상의 [Vibration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor
   EN: If target has a negative effect, deal +50% damage\n[WhenUse] If target has 5+ [Vibration], inflict +1 [Vibration] Count on Coin Hit
   PL:
670. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
671. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Vibration] 6 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 6 [Vibration]
   PL:
672. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 1, efekt 3 — opis] - 자신의 속도가 6 이상이면, [Vibration] 위력 2 추가 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: - At 6+ Speed, inflict 2 additional [Vibration] Potency
   PL:
673. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
674. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
675. [Umiejętność sojusznika [40001102] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] 다음 턴에 [Agility] 2 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001102].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Agility]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Agility] = 신속 / Haste
   EN: [OnSucceedAttack] Gain 2 [Agility] next turn
   PL:
676. [Umiejętność sojusznika [40001103] (ulepszenie 1) — nazwa] 스크류 아틀리에 - 스크류! 드릴!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].name
   limit: do 50 znaków
   EN: Screw Atelier - Screw! Drill!
   PL:
677. [Umiejętność sojusznika [40001103] (ulepszenie 1) — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%\n[WhenUse] [Charge] 횟수 5 증가\n[WhenUse] 자신의 [Charge] 횟수가 10 이상이면, 이 스킬의 모든 코인이 [SuperCoin]이 됨
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].desc
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [SuperCoin]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [SuperCoin] = 파괴 불가 코인 / Unbreakable Coin
   EN: If target has a negative effect, deal +50% damage\n[WhenUse] Gain +5 [Charge] Count\n[WhenUse] At 10+ [Charge] Count, convert all Coins of this Skill to [SuperCoin]s
   PL:
678. [Umiejętność sojusznika [40001103] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +2 [Vibration] Count
   PL:
679. [Umiejętność sojusznika [40001103] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수가 6 이상이면, [Vibration] 3 추가 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] At 6+ [Charge] Count, inflict 3 additional [Vibration]
   PL:
680. [Umiejętność sojusznika [40001103] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Charge]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Charge] = 충전 / Charge
   EN: [OnSucceedAttack] Gain +3 [Charge] Count
   PL:
681. [Umiejętność sojusznika [40001103] (ulepszenie 1) — moneta 3, efekt 1 — opis] [OnSucceedAttack] 자신의 [Charge] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001103].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 680 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
682. [Umiejętność sojusznika [40001104] (ulepszenie 1) — nazwa] 나미르 공방 - 중량 다섯배!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001104].levelList[level=1].name
   limit: do 60 znaków
   EN: Namir Workshop - Five Times the Weight!
   PL:
683. [Umiejętność sojusznika [40001104] (ulepszenie 1) — opis] 대상에게 부정적인 효과가 있으면, 피해량 +50%\n[WhenUse] 자신에게 [Charge] 횟수가 없으면, 스킬 적중시 대상의 [Vibration] 횟수 1 추가 증가\n[WhenUse] 자신의 [Charge] 횟수가 15 이상이면, 전부 소모하고 아래 효과 적용\n- [VibrationExplosion] 1회 추가\n- 이 스킬에서 사용하는 [VibrationExplosion]이 [Vibration] 횟수를 감소하지 않음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001104].levelList[level=1].desc
   limit: do 500 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Charge], [Vibration], [VibrationExplosion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Charge] = 충전 / Charge; [Vibration] = 진동 / Tremor; [VibrationExplosion] = 진동 폭발 / Tremor Burst
   EN: If target has a negative effect, deal +50% damage\n[WhenUse] If this unit does not have [Charge] Count, inflict +1 additional [Vibration] Count on target on Skill Hit\n[WhenUse] At 15+ [Charge] Count, consume all [Charge] Count and apply the following effects:\n- Trigger an additional [VibrationExplosion]\n- [VibrationExplosion] triggered by this Skill does not consume target's [Vibration] Count
   PL:
684. [Umiejętność sojusznika [40001104] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001104].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
685. [Umiejętność sojusznika [40001104] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [VibrationExplosion] 2회. 대상의 [Vibration] 횟수 2 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001104].levelList[level=1].coinlist[#0].coindescs[#1].desc
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [VibrationExplosion], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [VibrationExplosion] = 진동 폭발 / Tremor Burst; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Trigger [VibrationExplosion] twice; then, reduce target's [Vibration] Count by 2
   PL:
686. [Umiejętność sojusznika [40001104] (ulepszenie 1) — moneta 1, efekt 3 — opis] [OnSucceedAttack] [Vibration] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001104].levelList[level=1].coinlist[#0].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict +1 [Vibration] Count
   PL:
687. [Umiejętność sojusznika [40001105] (ulepszenie 1) — nazwa] 막고 지켜낼게요
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001105].levelList[level=1].name
   limit: do 50 znaków
   EN: I'll Block Them and Keep You Safe!
   PL:
688. [Umiejętność sojusznika [40001105] (ulepszenie 1) — opis] [CanDuelGuard]\n[StartBattle] <color=#ff6000><mark color=#ff000040><b><u>[SupportProtect] 1 얻음</color></mark></b></u>\n[WinDuel] 대상에게 [Vibration] 2 부여, [Vibration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001105].levelList[level=1].desc
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, \n, [CanDuelGuard], [StartBattle], [SupportProtect], [WinDuel], [Vibration]
   znaczenie tagów: [CanDuelGuard] = 합 가능 가드 / Clashable Guard; [StartBattle] = [전투 시작시] / [Combat Start]; [SupportProtect] = 원호 방어 / Assist Defense; [WinDuel] = [합 승리시] / [Clash Win]; [Vibration] = 진동 / Tremor
   EN: [CanDuelGuard]\n[StartBattle] <color=#ff6000><mark color=#ff000040><b><u>Gain 1 [SupportProtect]</color></mark></b></u>\n[WinDuel] Inflict 2 [Vibration] and +2 [Vibration] Count on target
   PL:
689. [Umiejętność sojusznika [40001105] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001105].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
690. [Umiejętność sojusznika [40001106] (ulepszenie 1) — nazwa] 멋있는 걸 막내가 다 하게 둘 순 없지!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001106].levelList[level=1].name
   limit: do 80 znaków
   EN: No Way I'm Letting Our Junior Steal all the Spotlight!
   PL:
691. [Umiejętność sojusznika [40001106] (ulepszenie 1) — opis] [CanDuelGuard]\n[SupportProtect] 전용 스킬\n[WinDuel] 아군 정신력 4 상승 (본인 포함)\n- LCD 소속이면, 대신 정신력 8 상승
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001106].levelList[level=1].desc
   (powtórzenie elementu 601 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
692. [Umiejętność sojusznika [40001106] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001106].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
693. [Umiejętność sojusznika [40001107] (ulepszenie 1) — nazwa] 유리아 공방 - 총공 모드, 마크 17!
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].name
   limit: do 60 znaków
   EN: YuRia Atelier - All-out Attack Mode, Mk. 17!
   PL:
694. [Umiejętność sojusznika [40001107] (ulepszenie 1) — opis] 대상의 부정적인 효과 종류당, 피해량 +50% (최대 100%)\n[WhenUse] 대상의 [Vibration]이 6 이상이면, 기본 위력 +3\n[WhenUse] 정신력이 0 이상이면, 망(望) 하나를 생성함\n- 기본 위력 +2, 피해량 +20%\n[EndSkill] 망(望)을 생성했으면, 정신력 10만큼 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].desc
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Vibration], [EndSkill]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Vibration] = 진동 / Tremor; [EndSkill] = [공격 종료시] / [Attack End]
   EN: Deal +50% damage for every type of negative effect on target (max 100%)\n[WhenUse] If target has 6+ [Vibration], Base Power +3\n[WhenUse] At 0+ SP, generate 1 Mang (望)\n- Base Power +2, deal +20% damage\n[EndSkill] If this Skill generated Mang (望), lose 10 SP
   PL:
695. [Umiejętność sojusznika [40001107] (ulepszenie 1) — tekst klimatyczny] 특별 수제작, 골든 리트리버 전용 도끼.
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].flavor
   limit: do 120 znaków
   EN: Special Handmade Golden Retriever-Exclusive Axe.
   PL:
696. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 1, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#0].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
697. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 1, efekt 2 — opis] [OnSucceedAttack] [Laceration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#0].coindescs[#1].desc
   (powtórzenie elementu 472 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
698. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
699. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Vibration] 횟수 2 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#1].coindescs[#1].desc
   (powtórzenie elementu 678 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
700. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
701. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Laceration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 450 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
702. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 3, efekt 3 — opis] [OnSucceedAttack] [Vibration] 3 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#2].coindescs[#2].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Vibration]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Vibration] = 진동 / Tremor
   EN: [OnSucceedAttack] Inflict 3 [Vibration]
   PL:
703. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 4, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#3].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
704. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 4, efekt 2 — opis] [OnSucceedAttack] 대상의 [Laceration] 1회 발동. 대상의 [Laceration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#3].coindescs[#1].desc
   (powtórzenie elementu 628 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
705. [Umiejętność sojusznika [40001107] (ulepszenie 1) — moneta 4, efekt 3 — opis] [OnSucceedAttack] [VibrationExplosion]. 대상의 [Vibration] 횟수 1 감소
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40001107].levelList[level=1].coinlist[#3].coindescs[#2].desc
   (powtórzenie elementu 622 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
706. [Umiejętność sojusznika [40000701] (ulepszenie 1) — nazwa] 착화
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000701].levelList[level=1].name
   limit: do 40 znaków
   EN: Ignition
   PL:
707. [Umiejętność sojusznika [40000701] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] (자신의 [Combustion] + 대상의 [Combustion]) 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000701].levelList[level=1].desc
   limit: do 250 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Coin Power +1 for every 6 ([Combustion] on self + [Combustion] on target) (max 2)\n[WhenUse] Gain +1 [Combustion] Count
   PL:
708. [Umiejętność sojusznika [40000701] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 4 부여. [Combustion] 횟수 1 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000701].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion] and +1 [Combustion] Count
   PL:
709. [Umiejętność sojusznika [40000701] (ulepszenie 1) — moneta 2, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000701].levelList[level=1].coinlist[#1].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
710. [Umiejętność sojusznika [40000701] (ulepszenie 1) — moneta 2, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000701].levelList[level=1].coinlist[#1].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 1 [Combustion]
   PL:
711. [Umiejętność sojusznika [40000702] (ulepszenie 1) — nazwa] E.G.O 홍염살 전개
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].name
   limit: do 40 znaków
   EN: E.G.O - A.B.S Activation
   PL:
712. [Umiejętność sojusznika [40000702] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] (자신의 [Combustion] + 메인 타겟의 [Combustion]) 6당, 코인 위력 +1 (최대 2)\n[WhenUse] 자신의 [Combustion] 횟수 3 증가\n[BeforeAttack] 자신의 [Combustion]이 5 이상이면, 공격 가중치 +1
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].desc
   limit: do 320 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Coin Power +1 for every 6 ([Combustion] on self + [Combustion] on main target) (max 2)\n[WhenUse] Gain +3 [Combustion] Count\n[BeforeAttack] At 5+ [Combustion], Atk Weight +1
   PL:
713. [Umiejętność sojusznika [40000702] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 3 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +3 [Combustion] Count
   PL:
714. [Umiejętność sojusznika [40000702] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 4 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 4 [Combustion]
   PL:
715. [Umiejętność sojusznika [40000702] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
716. [Umiejętność sojusznika [40000702] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 1 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000702].levelList[level=1].coinlist[#2].coindescs[#1].desc
   (powtórzenie elementu 710 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
717. [Umiejętność sojusznika [40000703] (ulepszenie 1) — nazwa] 불에 끌리는 마음으로
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].name
   limit: do 40 znaków
   EN: Drawn by Flame
   PL:
718. [Umiejętność sojusznika [40000703] (ulepszenie 1) — opis] [WhenUse] 대상의 부정적인 효과가 3개 이상이면, 기본 위력 +1\n[WhenUse] (자신의 [Combustion] + 메인 타겟의 [Combustion]) 6당, 코인 위력 +1 (최대 2)\n[WhenUse] (자신의 [Combustion] + 메인 타겟의 [Combustion]) 1당 피해량 +1% (최대 50%)\n[WhenUse] 자신의 [Combustion] 횟수 2 증가\n[BeforeAttack] 자신의 [Combustion] 5당, 공격 가중치 +1 (최대 3)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].desc
   limit: do 470 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [BeforeAttack]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [BeforeAttack] = [공격 시작 전] / [Before Attack]
   EN: [WhenUse] If target has 3+ types of negative effects, Base Power +1\n[WhenUse] Coin Power +1 for every 6 ([Combustion] on self + [Combustion] on main target) (max 2)\n[WhenUse] Deal +1% damage for every 1 ([Combustion] on self + [Combustion] on main target) (max 50%)\n[WhenUse] Gain +2 [Combustion] Count\n[BeforeAttack] Atk Weight +1 for every 5 [Combustion] on self (max 3)
   PL:
719. [Umiejętność sojusznika [40000703] (ulepszenie 1) — moneta 1, efekt 1 — opis] [OnSucceedAttack] [Combustion] 횟수 4 증가
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].coinlist[#0].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict +4 [Combustion] Count
   PL:
720. [Umiejętność sojusznika [40000703] (ulepszenie 1) — moneta 2, efekt 1 — opis] [OnSucceedAttack] [Combustion] 5 부여
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].coinlist[#1].coindescs[#0].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Inflict 5 [Combustion]
   PL:
721. [Umiejętność sojusznika [40000703] (ulepszenie 1) — moneta 3, efekt 1 — opis] [SuperCoin]
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].coinlist[#2].coindescs[#0].desc
   (powtórzenie elementu 546 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
722. [Umiejętność sojusznika [40000703] (ulepszenie 1) — moneta 3, efekt 2 — opis] [OnSucceedAttack] [Combustion] 2 얻음
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000703].levelList[level=1].coinlist[#2].coindescs[#1].desc
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [OnSucceedAttack], [Combustion]
   znaczenie tagów: [OnSucceedAttack] = [적중시] / [On Hit]; [Combustion] = 화상 / Burn
   EN: [OnSucceedAttack] Gain 2 [Combustion]
   PL:
723. [Umiejętność sojusznika [40000704] (ulepszenie 1) — nazwa] 홍염살의 감응도를 올릴게요
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000704].levelList[level=1].name
   limit: do 60 znaków
   EN: I'm Going to Raise A.B.S's Attunement Level.
   PL:
724. [Umiejętność sojusznika [40000704] (ulepszenie 1) — opis] [WhenUse] 자신의 [Combustion]이 10 이상이면, 코인 위력 +3\n[WhenUse] 자신의 [Combustion] 10 감소\n[OnSucceedEvade] 자신의 [Combustion] 5 감소 (턴당 1회)
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000704].levelList[level=1].desc
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [WhenUse], [Combustion], [OnSucceedEvade]
   znaczenie tagów: [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [OnSucceedEvade] = [회피 성공시] / [On Evade]
   EN: [WhenUse] At 10+ [Combustion], Coin Power +3\n[WhenUse] Lose 10 [Combustion]\n[OnSucceedEvade] Lose 5 [Combustion] (once per turn)
   PL:
725. [Umiejętność sojusznika [40000704] (ulepszenie 1) — tekst klimatyczny] ‘걱정 마세요. 저도 요령껏 살아남을 구멍 정도는 만들어뒀으니까.’
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000704].levelList[level=1].flavor
   limit: do 120 znaków
   EN: 'Don't worry. I've thought of a way that might get me out of this alive.'
   PL:
726. [Umiejętność sojusznika [40000705] (ulepszenie 1) — nazwa] 홍염살 최대 감응 【열화침식】
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000705].levelList[level=1].name
   limit: do 60 znaków
   EN: A.B.S Max Attunement 【Degraded Corrosion】
   PL:
727. [Umiejętność sojusznika [40000705] (ulepszenie 1) — opis] [CantDuel]\n이 스킬을 사용하는 동안 사망하지 않음\n[BeforeAttack] 적들의 슬롯 수 합만큼 공격 가중치 증가\n[WhenUse] (자신의 [Combustion] + 모든 대상의 [Combustion]) 1당, 피해량 +1% (최대 100%)\n[EndSkillAll] 전투 불능 상태가 됨
   źródło: Skills_Assist-a1c9p3.json :: dataList[id=40000705].levelList[level=1].desc
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n, [CantDuel], [BeforeAttack], [WhenUse], [Combustion], [EndSkillAll]
   znaczenie tagów: [CantDuel] = [합 불가능] / [Unclashable]; [BeforeAttack] = [공격 시작 전] / [Before Attack]; [WhenUse] = [사용시] / [On Use]; [Combustion] = 화상 / Burn; [EndSkillAll] = [스킬 종료시] / [Skill End]
   EN: [CantDuel]\nThis unit cannot be defeated while using this Skill\n[BeforeAttack] Gain +(total number of all enemies' Slots) Atk Weight\n[WhenUse] Deal +1% damage for every 1 ([Combustion] on self + [Combustion] on all targets) (max 100%)\n[EndSkillAll] This unit is defeated
   PL:
