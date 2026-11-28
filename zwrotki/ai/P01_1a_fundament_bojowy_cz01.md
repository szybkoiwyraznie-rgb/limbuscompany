# Paczka AI P01 (Fala 1 · 1A) — Fundament bojowy — grzechy, odporności, tagi, Panika i interfejs walki (część 1/2)

Tymczasowy przekład interfejsu, opisów technicznych i kart meta/statystyk (`origin: ai`, zgodnie z `D-11`).
Obowiązuje słownik terminów w `paczki_ai/SLOWNIK_TERMINOW.md` oraz zasady formatowania z `docs/PAKIET_TLUMACZA.md`.
Po wypełnieniu zapisz plik jako `zwrotki/ai/P01_1a_fundament_bojowy_cz01.md` i zaimportuj poleceniem:
`python3 tools/import_zwrotki.py --ai zwrotki/ai/P01_1a_fundament_bojowy_cz01.md`.

- Zasady techniczne: nie zmieniaj linii `źródło:`, `słownik:`, `EN:` ani `(powtórzenie elementu …)`; zachowaj wszystkie tokeny `{0}`, `<color=…>`, `[OnHit]`, `<sprite name=…>`.
- Wpisy już przetłumaczone przez człowieka są chronione (nawet przy ponownym imporcie `--ai` nie zostaną nadpisane).

## Tagi warunków umiejętności (SkillTag)
- Te etykiety (np. `[On Use]`, `[Heads Hit]`) gra wstawia automatycznie w miejsce tagów `[WhenUse]`, `[OnSucceedAttackHead]` w opisach umiejętności.

1. [Tag umiejętności [OnSucceedAttack] — nazwa] [적중시]
   źródło: SkillTag.json :: dataList[id=OnSucceedAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[OnSucceedAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Hit]
   PL: [Przy Trafieniu]
2. [Tag umiejętności [WhenUse] — nazwa] [사용시]
   źródło: SkillTag.json :: dataList[id=WhenUse].name
   kontekst: w opisach umiejętności zapisywany jako `[WhenUse]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Use]
   PL: [Przy Użyciu]
3. [Tag umiejętności [WinDuel] — nazwa] [합 승리시]
   źródło: SkillTag.json :: dataList[id=WinDuel].name
   kontekst: w opisach umiejętności zapisywany jako `[WinDuel]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Clash Win]
   PL: [Wygrane Starcie]
4. [Tag umiejętności [BeforeAttack] — nazwa] [공격 시작 전]
   źródło: SkillTag.json :: dataList[id=BeforeAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[BeforeAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Before Attack]
   PL: [Przed Atakiem]
5. [Tag umiejętności [Wide] — nazwa] [광역]
   źródło: SkillTag.json :: dataList[id=Wide].name
   kontekst: w opisach umiejętności zapisywany jako `[Wide]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [AoE]
   PL: [Obszarowy]
6. [Tag umiejętności [nxPostLine] — nazwa] [전열 {n}명]
   źródło: SkillTag.json :: dataList[id=nxPostLine].name
   kontekst: w opisach umiejętności zapisywany jako `[nxPostLine]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [{n} in Front]
   PL: [{n} z Przodu]
7. [Tag umiejętności [nxCenterLine] — nazwa] [중열 {n}명]
   źródło: SkillTag.json :: dataList[id=nxCenterLine].name
   kontekst: w opisach umiejętności zapisywany jako `[nxCenterLine]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [{n} in Middle]
   PL: [{n} w Środku]
8. [Tag umiejętności [nxBackLine] — nazwa] [후열 {n}명]
   źródło: SkillTag.json :: dataList[id=nxBackLine].name
   kontekst: w opisach umiejętności zapisywany jako `[nxBackLine]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [{n} in Back]
   PL: [{n} z Tyłu]
9. [Tag umiejętności [CantIdentify] — nazwa] [피아식별불가]
   źródło: SkillTag.json :: dataList[id=CantIdentify].name
   kontekst: w opisach umiejętności zapisywany jako `[CantIdentify]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Indiscriminate]
   PL: [Bez Rozróżnienia]
10. [Tag umiejętności [CRIMSON] — nazwa] 빨간색
   źródło: SkillTag.json :: dataList[id=CRIMSON].name
   kontekst: w opisach umiejętności zapisywany jako `[CRIMSON]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Crimson
   PL: Karmazyn
11. [Tag umiejętności [SCARLET] — nazwa] 주황색
   źródło: SkillTag.json :: dataList[id=SCARLET].name
   kontekst: w opisach umiejętności zapisywany jako `[SCARLET]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Scarlet
   PL: Szkarłat
12. [Tag umiejętności [AMBER] — nazwa] 노란색
   źródło: SkillTag.json :: dataList[id=AMBER].name
   kontekst: w opisach umiejętności zapisywany jako `[AMBER]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Amber
   PL: Bursztyn
13. [Tag umiejętności [SHAMROCK] — nazwa] 초록색
   źródło: SkillTag.json :: dataList[id=SHAMROCK].name
   kontekst: w opisach umiejętności zapisywany jako `[SHAMROCK]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Shamrock
   PL: Zieleń
14. [Tag umiejętności [AZURE] — nazwa] 파란색
   źródło: SkillTag.json :: dataList[id=AZURE].name
   kontekst: w opisach umiejętności zapisywany jako `[AZURE]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Azure
   PL: Lazur
15. [Tag umiejętności [INDIGO] — nazwa] 남색
   źródło: SkillTag.json :: dataList[id=INDIGO].name
   kontekst: w opisach umiejętności zapisywany jako `[INDIGO]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Indigo
   PL: Indygo
16. [Tag umiejętności [VIOLET] — nazwa] 보라색
   źródło: SkillTag.json :: dataList[id=VIOLET].name
   kontekst: w opisach umiejętności zapisywany jako `[VIOLET]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Violet
   PL: Fiolet
17. [Tag umiejętności [WHITE] — nazwa] 흰색
   źródło: SkillTag.json :: dataList[id=WHITE].name
   kontekst: w opisach umiejętności zapisywany jako `[WHITE]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: White
   PL: Biel
18. [Tag umiejętności [BLACK] — nazwa] 검정색
   źródło: SkillTag.json :: dataList[id=BLACK].name
   kontekst: w opisach umiejętności zapisywany jako `[BLACK]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: Black
   PL: Czerń
19. [Tag umiejętności [EndSkill] — nazwa] [공격 종료시]
   źródło: SkillTag.json :: dataList[id=EndSkill].name
   kontekst: w opisach umiejętności zapisywany jako `[EndSkill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Attack End]
   PL: [Koniec Ataku]
20. [Tag umiejętności [StartBattle] — nazwa] [전투 시작시]
   źródło: SkillTag.json :: dataList[id=StartBattle].name
   kontekst: w opisach umiejętności zapisywany jako `[StartBattle]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Combat Start]
   PL: [Początek Walki]
21. [Tag umiejętności [DefeatDuel] — nazwa] [합 패배]
   źródło: SkillTag.json :: dataList[id=DefeatDuel].name
   kontekst: w opisach umiejętności zapisywany jako `[DefeatDuel]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Clash Lose]
   PL: [Przegrane Starcie]
22. [Tag umiejętności [OnSucceedAttackHead] — nazwa] [앞면 적중시]
   źródło: SkillTag.json :: dataList[id=OnSucceedAttackHead].name
   kontekst: w opisach umiejętności zapisywany jako `[OnSucceedAttackHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Heads Hit]
   PL: [Trafienie Awersem]
23. [Tag umiejętności [OnSucceedAttackTail] — nazwa] [뒷면 적중시]
   źródło: SkillTag.json :: dataList[id=OnSucceedAttackTail].name
   kontekst: w opisach umiejętności zapisywany jako `[OnSucceedAttackTail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Tails Hit]
   PL: [Trafienie Rewersem]
24. [Tag umiejętności [OnSucceedEvade] — nazwa] [회피 성공시]
   źródło: SkillTag.json :: dataList[id=OnSucceedEvade].name
   kontekst: w opisach umiejętności zapisywany jako `[OnSucceedEvade]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Evade]
   PL: [Udany Unik]
25. [Tag umiejętności [AlwaysUse] — nazwa] [상시]
   źródło: SkillTag.json :: dataList[id=AlwaysUse].name
   kontekst: w opisach umiejętności zapisywany jako `[AlwaysUse]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Constant]
   PL: [Stały]
26. [Tag umiejętności [CantDuel] — nazwa] [합 불가능]
   źródło: SkillTag.json :: dataList[id=CantDuel].name
   kontekst: w opisach umiejętności zapisywany jako `[CantDuel]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Unclashable]
   PL: [Niestarciowy]
27. [Tag umiejętności [EnemyKill] — nazwa] [적 처치 시]
   źródło: SkillTag.json :: dataList[id=EnemyKill].name
   kontekst: w opisach umiejętności zapisywany jako `[EnemyKill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Kill]
   PL: [Przy Zabiciu]
28. [Tag umiejętności [EnemyKillFail] — nazwa] [적 처치 실패 시]
   źródło: SkillTag.json :: dataList[id=EnemyKillFail].name
   kontekst: w opisach umiejętności zapisywany jako `[EnemyKillFail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Failed Kill]
   PL: [Nieudane Zabicie]
29. [Tag umiejętności [ReUse] — nazwa] [재사용 시]
   źródło: SkillTag.json :: dataList[id=ReUse].name
   kontekst: w opisach umiejętności zapisywany jako `[ReUse]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Reuse]
   PL: [Przy Ponownym Użyciu]
30. [Tag umiejętności [ReUseOnSucceedAttackHead] — nazwa] [재사용 앞면 적중 시]
   źródło: SkillTag.json :: dataList[id=ReUseOnSucceedAttackHead].name
   kontekst: w opisach umiejętności zapisywany jako `[ReUseOnSucceedAttackHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Reuse - Heads Hit]
   PL: [Ponowne Użycie - Trafienie Awersem]
31. [Tag umiejętności [CriticalOnSucceedAttack] — nazwa] [크리티컬 적중 시]
   źródło: SkillTag.json :: dataList[id=CriticalOnSucceedAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalOnSucceedAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Crit]
   PL: [Trafienie Krytyczne]
32. [Tag umiejętności [StartDuel] — nazwa] [합 시작 시]
   źródło: SkillTag.json :: dataList[id=StartDuel].name
   kontekst: w opisach umiejętności zapisywany jako `[StartDuel]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Clash Start]
   PL: [Początek Starcia]
33. [Tag umiejętności [EndBattle] — nazwa] [턴 종료 시]
   źródło: SkillTag.json :: dataList[id=EndBattle].name
   kontekst: w opisach umiejętności zapisywany jako `[EndBattle]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Turn End]
   PL: [Koniec Tury]
34. [Tag umiejętności [OnDefeatEvade] — nazwa] [회피 실패시]
   źródło: SkillTag.json :: dataList[id=OnDefeatEvade].name
   kontekst: w opisach umiejętności zapisywany jako `[OnDefeatEvade]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Failed Evade]
   PL: [Nieudany Unik]
35. [Tag umiejętności [EndSkillHead] — nazwa] [앞면 공격 종료 시]
   źródło: SkillTag.json :: dataList[id=EndSkillHead].name
   kontekst: w opisach umiejętności zapisywany jako `[EndSkillHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Heads Attack End]
   PL: [Koniec Ataku Awersem]
36. [Tag umiejętności [EndSkillTail] — nazwa] [뒷면 공격 종료 시]
   źródło: SkillTag.json :: dataList[id=EndSkillTail].name
   kontekst: w opisach umiejętności zapisywany jako `[EndSkillTail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Tails Attack End]
   PL: [Koniec Ataku Rewersem]
37. [Tag umiejętności [WinDuelAttackHead] — nazwa] [합 승리 후 앞면 적중시]
   źródło: SkillTag.json :: dataList[id=WinDuelAttackHead].name
   kontekst: w opisach umiejętności zapisywany jako `[WinDuelAttackHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Heads Hit after Clash Win]
   PL: [Trafienie Awersem po Wygranym Starciu]
38. [Tag umiejętności [WinDuelAttack] — nazwa] [합 승리 후 적중시]
   źródło: SkillTag.json :: dataList[id=WinDuelAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[WinDuelAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Hit after Clash Win]
   PL: [Trafienie po Wygranym Starciu]
39. [Tag umiejętności [CriticalActivated] — nazwa] [크리티컬 발동 시]
   źródło: SkillTag.json :: dataList[id=CriticalActivated].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalActivated]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Crit]
   PL: [Przy Krytyku]
40. [Tag umiejętności [CriticalEndSkill] — nazwa] [크리티컬 공격 종료 시]
   źródło: SkillTag.json :: dataList[id=CriticalEndSkill].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalEndSkill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Crit Attack End]
   PL: [Koniec Ataku Krytycznego]
41. [Tag umiejętności [CantChangeTarget] — nazwa] [대상 변경 불가]
   źródło: SkillTag.json :: dataList[id=CantChangeTarget].name
   kontekst: w opisach umiejętności zapisywany jako `[CantChangeTarget]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Target Fixed]
   PL: [Stały Cel]
42. [Tag umiejętności [TurnStartBattle] — nazwa] [턴 시작 시]
   źródło: SkillTag.json :: dataList[id=TurnStartBattle].name
   kontekst: w opisach umiejętności zapisywany jako `[TurnStartBattle]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Turn Start]
   PL: [Początek Tury]
43. [Tag umiejętności [EndSkillAll] — nazwa] [스킬 종료시]
   źródło: SkillTag.json :: dataList[id=EndSkillAll].name
   kontekst: w opisach umiejętności zapisywany jako `[EndSkillAll]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Skill End]
   PL: [Koniec Umiejętności]
44. [Tag umiejętności [WhenUse_Force] — nazwa] <color=#26cfff>[사용시]</color>
   źródło: SkillTag.json :: dataList[id=WhenUse_Force].name
   kontekst: w opisach umiejętności zapisywany jako `[WhenUse_Force]` — gra podstawia tu ten napis
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <color=#26cfff>, </color>
   EN: <color=#26cfff>[On Use]</color>
   PL: <color=#26cfff>[Przy Użyciu]</color>
45. [Tag umiejętności [StartBattle_Force] — nazwa] <color=#93f13e>[전투 시작시]</color>
   źródło: SkillTag.json :: dataList[id=StartBattle_Force].name
   kontekst: w opisach umiejętności zapisywany jako `[StartBattle_Force]` — gra podstawia tu ten napis
   limit: do 40 znaków
   tokeny: zachowaj dokładnie: <color=#93f13e>, </color>
   EN: <color=#93f13e>[Combat Start]</color>
   PL: <color=#93f13e>[Początek Walki]</color>
46. [Tag umiejętności [TargetKill] — nazwa] [대상 처치 시]
   źródło: SkillTag.json :: dataList[id=TargetKill].name
   kontekst: w opisach umiejętności zapisywany jako `[TargetKill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Target Kill]
   PL: [Przy Zabiciu Celu]
47. [Tag umiejętności [CriticalTargetKill] — nazwa] [크리티컬 처치 시]
   źródło: SkillTag.json :: dataList[id=CriticalTargetKill].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalTargetKill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Crit Kill]
   PL: [Zabójstwo Krytyczne]
48. [Tag umiejętności [BeforeUse] — nazwa] [사용전]
   źródło: SkillTag.json :: dataList[id=BeforeUse].name
   kontekst: w opisach umiejętności zapisywany jako `[BeforeUse]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Before Use]
   PL: [Przed Użyciem]
49. [Tag umiejętności [DuelCounter] — nazwa] [합 가능 반격]
   źródło: SkillTag.json :: dataList[id=DuelCounter].name
   kontekst: w opisach umiejętności zapisywany jako `[DuelCounter]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Clashable Counter]
   PL: [Kontra Starciowa]
50. [Tag umiejętności [DuelGuard] — nazwa] [합 가능 가드]
   źródło: SkillTag.json :: dataList[id=DuelGuard].name
   kontekst: w opisach umiejętności zapisywany jako `[DuelGuard]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Clashable Guard]
   PL: [Garda Starciowa]
51. [Tag umiejętności [WhenUseEvade] — nazwa] [회피 사용시]
   źródło: SkillTag.json :: dataList[id=WhenUseEvade].name
   kontekst: w opisach umiejętności zapisywany jako `[WhenUseEvade]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Evade Use]
   PL: [Przy Użyciu Uniku]
52. [Tag umiejętności [EndCoin] — nazwa] [이 코인 공격 종료 시]
   źródło: SkillTag.json :: dataList[id=EndCoin].name
   kontekst: w opisach umiejętności zapisywany jako `[EndCoin]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Current Coin Attack End]
   PL: [Koniec Ataku Tej Monety]
53. [Tag umiejętności [CriticalEnemyTargetKillFail] — nazwa] [크리티컬 적 처치 실패 시]
   źródło: SkillTag.json :: dataList[id=CriticalEnemyTargetKillFail].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalEnemyTargetKillFail]` — gra podstawia tu ten napis
   limit: do 50 znaków
   EN: [On Crit Kill Fail Against Enemy]
   PL: [Nieudane Zabójstwo Krytyczne Wroga]
54. [Tag umiejętności [CriticalEnemyTargetKill] — nazwa] [크리티컬 적 처치 시]
   źródło: SkillTag.json :: dataList[id=CriticalEnemyTargetKill].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalEnemyTargetKill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Crit Kill Against Enemy]
   PL: [Zabójstwo Krytyczne Wroga]
55. [Tag umiejętności [DefeatDuelAttack] — nazwa] [합 패배 후 적중]
   źródło: SkillTag.json :: dataList[id=DefeatDuelAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[DefeatDuelAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Hit after Clash Lose]
   PL: [Trafienie po Przegranym Starciu]
56. [Tag umiejętności [TargetKillFail] — nazwa] [대상 처치 실패시]
   źródło: SkillTag.json :: dataList[id=TargetKillFail].name
   kontekst: w opisach umiejętności zapisywany jako `[TargetKillFail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Target Kill Fail]
   PL: [Nieudane Zabicie Celu]
57. [Tag umiejętności [AllyKill] — nazwa] [아군 처치 시]
   źródło: SkillTag.json :: dataList[id=AllyKill].name
   kontekst: w opisach umiejętności zapisywany jako `[AllyKill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Ally Kill]
   PL: [Przy Zabiciu Sojusznika]
58. [Tag umiejętności [AllyKillFail] — nazwa] [아군 처치 실패시]
   źródło: SkillTag.json :: dataList[id=AllyKillFail].name
   kontekst: w opisach umiejętności zapisywany jako `[AllyKillFail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Ally Kill Fail]
   PL: [Nieudane Zabicie Sojusznika]
59. [Tag umiejętności [UnBrokenCoinOnSucceedAttack] — nazwa] [파괴되지 않고 적중시]
   źródło: SkillTag.json :: dataList[id=UnBrokenCoinOnSucceedAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[UnBrokenCoinOnSucceedAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Hit without Cracking]
   PL: [Trafienie bez Pęknięcia]
60. [Tag umiejętności [BeforeHit] — nazwa] [피격 직전]
   źródło: SkillTag.json :: dataList[id=BeforeHit].name
   kontekst: w opisach umiejętności zapisywany jako `[BeforeHit]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Before Getting Hit]
   PL: [Tuż Przed Otrzymaniem Ciosu]
61. [Tag umiejętności [OnDirectAttack] — nazwa] [일방 공격 시]
   źródło: SkillTag.json :: dataList[id=OnDirectAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[OnDirectAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Unopposed Attack]
   PL: [Atak Jednostronny]
62. [Tag umiejętności [ReUseOnSucceedAttack] — nazwa] [재사용 적중시]
   źródło: SkillTag.json :: dataList[id=ReUseOnSucceedAttack].name
   kontekst: w opisach umiejętności zapisywany jako `[ReUseOnSucceedAttack]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Reuse - On Hit]
   PL: [Ponowne Użycie - Przy Trafieniu]
63. [Tag umiejętności [CriticalOnSucceedAttackHead] — nazwa] [크리티컬 앞면 적중 시]
   źródło: SkillTag.json :: dataList[id=CriticalOnSucceedAttackHead].name
   kontekst: w opisach umiejętności zapisywany jako `[CriticalOnSucceedAttackHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [On Crit - Heads Hit]
   PL: [Krytyk - Trafienie Awersem]
64. [Tag umiejętności [OnStartCoin] — nazwa] [코인 시작 시]
   źródło: SkillTag.json :: dataList[id=OnStartCoin].name
   kontekst: w opisach umiejętności zapisywany jako `[OnStartCoin]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Coin Start]
   PL: [Początek Monety]
65. [Tag umiejętności [BeforeBehavior] — nazwa] [행동 시작 전]
   źródło: SkillTag.json :: dataList[id=BeforeBehavior].name
   kontekst: w opisach umiejętności zapisywany jako `[BeforeBehavior]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Before Action]
   PL: [Przed Działaniem]
66. [Tag umiejętności [AlwaysUseEGOPassive2050911] — nazwa] [검계 우두머리 뫼르소 전용 상시 효과]
   źródło: SkillTag.json :: dataList[id=AlwaysUseEGOPassive2050911].name
   kontekst: w opisach umiejętności zapisywany jako `[AlwaysUseEGOPassive2050911]` — gra podstawia tu ten napis
   limit: do 90 znaków
   EN: [Always Active - Blade Lineage Mentor Meursault Exclusive Effect]
   PL: [Efekt Stały - Wyłącznie dla Mentora Rodu Ostrza Meursaulta]
67. [Tag umiejętności [WhenUseEGOPassive] — nazwa] [사용 효과]
   źródło: SkillTag.json :: dataList[id=WhenUseEGOPassive].name
   kontekst: w opisach umiejętności zapisywany jako `[WhenUseEGOPassive]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Effect on Use]
   PL: [Efekt Użycia]
68. [Tag umiejętności [WinDuelEndSkill] — nazwa] [합 승리 후 공격 종료 시]
   źródło: SkillTag.json :: dataList[id=WinDuelEndSkill].name
   kontekst: w opisach umiejętności zapisywany jako `[WinDuelEndSkill]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Attack End After Clash Win]
   PL: [Koniec Ataku po Wygranym Starciu]
69. [Tag umiejętności [WhenUseEGOPassive2010911] — nazwa] [로보토미 E.G.O::엄숙한 애도 이상 전용 사용 효과]
   źródło: SkillTag.json :: dataList[id=WhenUseEGOPassive2010911].name
   kontekst: w opisach umiejętności zapisywany jako `[WhenUseEGOPassive2010911]` — gra podstawia tu ten napis
   limit: do 100 znaków
   EN: [Effect on Use - Lobotomy E.G.O::Solemn Lament Yi Sang Exclusive Effect]
   PL: [Efekt Użycia - Wyłącznie dla Lobotomy E.G.O::Uroczysty Lament Yi Sanga]
70. [Tag umiejętności [AlwaysUseEGOPassive2010911] — nazwa] [로보토미 E.G.O::엄숙한 애도 이상 전용 상시 효과]
   źródło: SkillTag.json :: dataList[id=AlwaysUseEGOPassive2010911].name
   kontekst: w opisach umiejętności zapisywany jako `[AlwaysUseEGOPassive2010911]` — gra podstawia tu ten napis
   limit: do 100 znaków
   EN: [Always Active - Lobotomy E.G.O::Solemn Lament Yi Sang Exclusive Effect]
   PL: [Efekt Stały - Wyłącznie dla Lobotomy E.G.O::Uroczysty Lament Yi Sanga]
71. [Tag umiejętności [AlwaysUseEGOPassive] — nazwa] [상시 효과]
   źródło: SkillTag.json :: dataList[id=AlwaysUseEGOPassive].name
   kontekst: w opisach umiejętności zapisywany jako `[AlwaysUseEGOPassive]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Always Active]
   PL: [Efekt Stały]
72. [Tag umiejętności [CoinHead] — nazwa] [앞면]
   źródło: SkillTag.json :: dataList[id=CoinHead].name
   kontekst: w opisach umiejętności zapisywany jako `[CoinHead]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Heads]
   PL: [Awers]
73. [Tag umiejętności [CoinTail] — nazwa] [뒷면]
   źródło: SkillTag.json :: dataList[id=CoinTail].name
   kontekst: w opisach umiejętności zapisywany jako `[CoinTail]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Tails]
   PL: [Rewers]
74. [Tag umiejętności [OnBattleEnd] — nazwa] [전투 종료 시]
   źródło: SkillTag.json :: dataList[id=OnBattleEnd].name
   kontekst: w opisach umiejętności zapisywany jako `[OnBattleEnd]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Combat End]
   PL: [Koniec Walki]
75. [Tag umiejętności [SynergyActivationConditions] — nazwa] [발동 조건]
   źródło: SkillTag.json :: dataList[id=SynergyActivationConditions].name
   kontekst: w opisach umiejętności zapisywany jako `[SynergyActivationConditions]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Activation Conditions]
   PL: [Warunki Aktywacji]
76. [Tag umiejętności [SynergyActivationEffect] — nazwa] [발동 효과]
   źródło: SkillTag.json :: dataList[id=SynergyActivationEffect].name
   kontekst: w opisach umiejętności zapisywany jako `[SynergyActivationEffect]` — gra podstawia tu ten napis
   limit: do 40 znaków
   EN: [Activation Effects]
   PL: [Efekty Aktywacji]

## Pojęcia bazowe i cechy jednostek: AttributeText
- plik gry: `AttributeText.json`

77. [Pojęcia bazowe i cechy jednostek [CRIMSON] — nazwa] 분노
   źródło: AttributeText.json :: dataList[id=CRIMSON].name
   limit: do 40 znaków
   EN: Wrath
   PL: Gniew
78. [Pojęcia bazowe i cechy jednostek [SCARLET] — nazwa] 색욕
   źródło: AttributeText.json :: dataList[id=SCARLET].name
   limit: do 40 znaków
   EN: Lust
   PL: Żądza
79. [Pojęcia bazowe i cechy jednostek [AMBER] — nazwa] 나태
   źródło: AttributeText.json :: dataList[id=AMBER].name
   limit: do 40 znaków
   EN: Sloth
   PL: Lenistwo
80. [Pojęcia bazowe i cechy jednostek [SHAMROCK] — nazwa] 탐식
   źródło: AttributeText.json :: dataList[id=SHAMROCK].name
   limit: do 40 znaków
   EN: Glut.
   PL: Obżar.
81. [Pojęcia bazowe i cechy jednostek [AZURE] — nazwa] 우울
   źródło: AttributeText.json :: dataList[id=AZURE].name
   limit: do 40 znaków
   EN: Gloom
   PL: Posępność
82. [Pojęcia bazowe i cechy jednostek [INDIGO] — nazwa] 오만
   źródło: AttributeText.json :: dataList[id=INDIGO].name
   limit: do 40 znaków
   EN: Pride
   PL: Pycha
83. [Pojęcia bazowe i cechy jednostek [VIOLET] — nazwa] 질투
   źródło: AttributeText.json :: dataList[id=VIOLET].name
   limit: do 40 znaków
   EN: Envy
   PL: Zawiść
84. [Pojęcia bazowe i cechy jednostek [WHITE] — nazwa] 광기
   źródło: AttributeText.json :: dataList[id=WHITE].name
   limit: do 40 znaków
   EN: Mad.
   PL: Szaleń.
85. [Pojęcia bazowe i cechy jednostek [BLACK] — nazwa] 비탄
   źródło: AttributeText.json :: dataList[id=BLACK].name
   limit: do 40 znaków
   EN: Angst
   PL: Trwoga

## Pojęcia bazowe i cechy jednostek: ResistText
- plik gry: `ResistText.json`

86. [Pojęcia bazowe i cechy jednostek [resist_weak] — tekst] 취약
   źródło: ResistText.json :: dataList[id=resist_weak].content
   limit: do 120 znaków
   EN: Fatal
   PL: Zabójcza
87. [Pojęcia bazowe i cechy jednostek [resist_vulnerable] — tekst] 약점
   źródło: ResistText.json :: dataList[id=resist_vulnerable].content
   limit: do 120 znaków
   EN: Weak
   PL: Słaba
88. [Pojęcia bazowe i cechy jednostek [resist_normal] — tekst] 보통
   źródło: ResistText.json :: dataList[id=resist_normal].content
   limit: do 120 znaków
   EN: Normal
   PL: Zwykła
89. [Pojęcia bazowe i cechy jednostek [resist_endure] — tekst] 견딤
   źródło: ResistText.json :: dataList[id=resist_endure].content
   limit: do 120 znaków
   EN: Endure
   PL: Odporna
90. [Pojęcia bazowe i cechy jednostek [resist_resist] — tekst] 내성
   źródło: ResistText.json :: dataList[id=resist_resist].content
   limit: do 120 znaków
   EN: Ineff.
   PL: Nieskut.
91. [Pojęcia bazowe i cechy jednostek [resist_immune] — tekst] 면역
   źródło: ResistText.json :: dataList[id=resist_immune].content
   limit: do 120 znaków
   EN: Immune
   PL: Niewrażl.

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c10p1
- plik gry: `UnitKeyword-a1c10p1.json`

92. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SISYPHE] — tekst] 시지프
   źródło: UnitKeyword-a1c10p1.json :: dataList[id=UnitKeyword_SISYPHE].content
   limit: do 120 znaków
   EN: Sisyphe
   PL: Sisyphe
93. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LE_NOIR] — tekst] 르누아르
   źródło: UnitKeyword-a1c10p1.json :: dataList[id=UnitKeyword_LE_NOIR].content
   limit: do 120 znaków
   EN: Le Noir
   PL: Le Noir
94. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LE_ROUGE] — tekst] 르루주
   źródło: UnitKeyword-a1c10p1.json :: dataList[id=UnitKeyword_LE_ROUGE].content
   limit: do 120 znaków
   EN: Le Rouge
   PL: Le Rouge

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c10p3
- plik gry: `UnitKeyword-a1c10p3.json`

95. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FOUR_SQUARE] — tekst] □□□□
   źródło: UnitKeyword-a1c10p3.json :: dataList[id=UnitKeyword_FOUR_SQUARE].content
   limit: do 120 znaków
   EN: □□ □□□□
   PL: □□ □□□□

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c7p1
- plik gry: `UnitKeyword-a1c7p1.json`

96. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLOODBAG] — tekst] 피주머니
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_BLOODBAG].content
   limit: do 120 znaków
   EN: Bloodbag
   PL: Worek Krwi
97. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLOODFIEND] — tekst] 혈귀
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_BLOODFIEND].content
   limit: do 120 znaków
   EN: Bloodfiend
   PL: Krwiożerca
98. [Pojęcia bazowe i cechy jednostek [UnitKeyword_THIRD_DEPENDENT] — tekst] 제3권속
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_THIRD_DEPENDENT].content
   limit: do 120 znaków
   EN: Third Kindred
   PL: Trzeci Pokrewny
99. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DEPENDENT] — tekst] 권속
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_DEPENDENT].content
   limit: do 120 znaków
   EN: Kindred
   PL: Pokrewny
100. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FANG_HUNT] — tekst] 송곳니 사냥 사무소
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_FANG_HUNT].content
   limit: do 120 znaków
   EN: Fanghunt Office
   PL: Biuro Łowców Kłów
101. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FULL_STOP] — tekst] 마침표 사무소
   źródło: UnitKeyword-a1c7p1.json :: dataList[id=UnitKeyword_FULL_STOP].content
   limit: do 120 znaków
   EN: Full-Stop Office
   PL: Biuro Kropki

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c7p2
- plik gry: `UnitKeyword-a1c7p2.json`

102. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SECOND_DEPENDENT] — tekst] 제2권속
   źródło: UnitKeyword-a1c7p2.json :: dataList[id=UnitKeyword_SECOND_DEPENDENT].content
   limit: do 120 znaków
   EN: Second Kindred
   PL: Drugi Pokrewny
103. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_GA] — tekst] 가씨 가문
   źródło: UnitKeyword-a1c7p2.json :: dataList[id=UnitKeyword_FAMILY_GA].content
   limit: do 120 znaków
   EN: Jia Family
   PL: Ród Jia
104. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_GA_CANDIDATE] — tekst] 가주 후보
   źródło: UnitKeyword-a1c7p2.json :: dataList[id=UnitKeyword_FAMILY_GA_CANDIDATE].content
   limit: do 120 znaków
   EN: Family Hierarch Candidate
   PL: Kandydat na Głowę Rodu

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c7p3
- plik gry: `UnitKeyword-a1c7p3.json`

105. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FIRST_DEPENDENT] — tekst] 제1권속
   źródło: UnitKeyword-a1c7p3.json :: dataList[id=UnitKeyword_FIRST_DEPENDENT].content
   limit: do 120 znaków
   EN: First Kindred
   PL: Pierwszy Pokrewny
106. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ABNORMALITY_EROSION] — tekst] 환상 침식
   źródło: UnitKeyword-a1c7p3.json :: dataList[id=UnitKeyword_ABNORMALITY_EROSION].content
   limit: do 120 znaków
   EN: Abnormality Corrosion
   PL: Korozja Anomalii

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c8p2
- plik gry: `UnitKeyword-a1c8p2.json`

107. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_SA] — tekst] 사씨 가문
   źródło: UnitKeyword-a1c8p2.json :: dataList[id=UnitKeyword_FAMILY_SA].content
   limit: do 120 znaków
   EN: Shi Family
   PL: Ród Shi
108. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_WANG] — tekst] 왕씨 가문
   źródło: UnitKeyword-a1c8p2.json :: dataList[id=UnitKeyword_FAMILY_WANG].content
   limit: do 120 znaków
   EN: Wang Family
   PL: Ród Wang
109. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_SEOL] — tekst] 설씨 가문
   źródło: UnitKeyword-a1c8p2.json :: dataList[id=UnitKeyword_FAMILY_SEOL].content
   limit: do 120 znaków
   EN: Xue Family
   PL: Ród Xue

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c8p3
- plik gry: `UnitKeyword-a1c8p3.json`

110. [Pojęcia bazowe i cechy jednostek [UnitKeyword_THUMB_FINGER] — tekst] 엄지
   źródło: UnitKeyword-a1c8p3.json :: dataList[id=UnitKeyword_THUMB_FINGER].content
   limit: do 120 znaków
   EN: The Thumb
   PL: Kciuk

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c9p1
- plik gry: `UnitKeyword-a1c9p1.json`

111. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SPIDER_HOUSE] — tekst] 거미집
   źródło: UnitKeyword-a1c9p1.json :: dataList[id=UnitKeyword_SPIDER_HOUSE].content
   limit: do 120 znaków
   EN: The House of Spiders
   PL: Dom Pająków
112. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LITTLE_FINGER] — tekst] 소지
   źródło: UnitKeyword-a1c9p1.json :: dataList[id=UnitKeyword_LITTLE_FINGER].content
   limit: do 120 znaków
   EN: The Pinky
   PL: Mały Palec
113. [Pojęcia bazowe i cechy jednostek [UnitKeyword_INDEX_FINGER] — tekst] 검지
   źródło: UnitKeyword-a1c9p1.json :: dataList[id=UnitKeyword_INDEX_FINGER].content
   limit: do 120 znaków
   EN: The Index
   PL: Wskazujący
114. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FINGER] — tekst] 손가락
   źródło: UnitKeyword-a1c9p1.json :: dataList[id=UnitKeyword_FINGER].content
   limit: do 120 znaków
   EN: The Fingers
   PL: Palce

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c9p2
- plik gry: `UnitKeyword-a1c9p2.json`

115. [Pojęcia bazowe i cechy jednostek [UnitKeyword_UNIQUE_COLOR] — tekst] 특색
   źródło: UnitKeyword-a1c9p2.json :: dataList[id=UnitKeyword_UNIQUE_COLOR].content
   limit: do 120 znaków
   EN: Color Fixer
   PL: Kolorowy Fikser
116. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCD] — tekst] LCD
   źródło: UnitKeyword-a1c9p2.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCD].content
   limit: do 120 znaków
   EN: LCD
   PL: LCD

## Pojęcia bazowe i cechy jednostek: UnitKeyword-a1c9p3
- plik gry: `UnitKeyword-a1c9p3.json`

117. [Pojęcia bazowe i cechy jednostek [UnitKeyword_G_CORP_FORMER] — tekst] 구 G사
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_G_CORP_FORMER].content
   limit: do 120 znaków
   EN: Old G Corp.
   PL: Stara Korp. G
118. [Pojęcia bazowe i cechy jednostek [UnitKeyword_KING_OF_ALL_COCKROACHES] — tekst] 모든 바퀴벌레의 왕
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_KING_OF_ALL_COCKROACHES].content
   limit: do 120 znaków
   EN: Lord of all Roaches
   PL: Władca Wszystkich Karaluchów
119. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WINGS_ULTIMATEWEAPON] — tekst] 날개 결전병기
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_WINGS_ULTIMATEWEAPON].content
   limit: do 120 znaków
   EN: A Wing's Decisive Weapon
   PL: Broń Ostateczna Skrzydła
120. [Pojęcia bazowe i cechy jednostek [UnitKeyword_EMPEROR_OF_PESTS] — tekst] 해충들의 황제
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_EMPEROR_OF_PESTS].content
   limit: do 120 znaków
   EN: Emperor of Pests
   PL: Cesarz Szkodników
121. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ROYAL] — tekst] 왕족
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_ROYAL].content
   limit: do 120 znaków
   EN: Royalty
   PL: Ród Królewski
122. [Pojęcia bazowe i cechy jednostek [UnitKeyword_HIDDEN_KEYWORD] — tekst] ???
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_HIDDEN_KEYWORD].content
   limit: do 120 znaków
   EN: ???
   PL: ???
123. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SIGN_FUTURE] — tekst] 표지 [미래]
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_SIGN_FUTURE].content
   limit: do 120 znaków
   EN: The Sign [Future]
   PL: Znak [Przyszłość]
124. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SMOKE_WAR_2ND] — tekst] 제 2차 연기전쟁
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_SMOKE_WAR_2ND].content
   limit: do 120 znaków
   EN: The Second Smoke War
   PL: Druga Wojna Dymna
125. [Pojęcia bazowe i cechy jednostek [UnitKeyword_HIDDEN_KEYWORD_2ND] — tekst] ???
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_HIDDEN_KEYWORD_2ND].content
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
126. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ABRAXAS_CHARIOT] — tekst] 아브락사스 전차
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_ABRAXAS_CHARIOT].content
   limit: do 120 znaków
   EN: Abraxas Chariot
   PL: Rydwan Abraxasa
127. [Pojęcia bazowe i cechy jednostek [UnitKeyword_HEAVENLY_KILLING_STAR] — tekst] 천살성
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_HEAVENLY_KILLING_STAR].content
   limit: do 120 znaków
   EN: Tiansha Star
   PL: Gwiazda Tiansha
128. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BIG_BROTHER_PAST] — tekst] <color=#d40000><s>큰 형님</s></color>
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_BIG_BROTHER_PAST].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Great Brother</s></color>
   PL: <color=#d40000><s>Wielki Brat</s></color>
129. [Pojęcia bazowe i cechy jednostek [UnitKeyword_UNDERBOSS_FIRED] — tekst] <color=#d40000><s>언더보스</s></color>
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_UNDERBOSS_FIRED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Sottocapo</s></color>
   PL: <color=#d40000><s>Sottocapo</s></color>
130. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SMOKE_WAR] — tekst] 연기전쟁
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_SMOKE_WAR].content
   limit: do 120 znaków
   EN: Smoke War
   PL: Wojna Dymna
131. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WAR_HERO] — tekst] 전쟁영웅
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_WAR_HERO].content
   limit: do 120 znaków
   EN: War Hero
   PL: Bohater Wojenny
132. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SEVENFAMILIES_CANCELED] — tekst] <color=#d40000><s>7대 패밀리<s></color>
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_SEVENFAMILIES_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </color>
   EN: <color=#d40000><s>Le Sette Famiglie<s></color>
   PL: <color=#d40000><s>Siedem Rodzin<s></color>
133. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MAESTRO_FORMER] — tekst] <color=#d40000><s>마에스트로<s></color>
   źródło: UnitKeyword-a1c9p3.json :: dataList[id=UnitKeyword_MAESTRO_FORMER].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </color>
   EN: <color=#d40000><s>Maestro<s></color>
   PL: <color=#d40000><s>Maestro<s></color>

## Pojęcia bazowe i cechy jednostek: UnitKeyword-exem
- plik gry: `UnitKeyword-exem.json`

134. [Pojęcia bazowe i cechy jednostek [UnitKeyword_N_CORP_LENSMAN] — tekst] 못
   źródło: UnitKeyword-exem.json :: dataList[id=UnitKeyword_N_CORP_LENSMAN].content
   limit: do 120 znaków
   EN: Les Clous
   PL: Les Clous
135. [Pojęcia bazowe i cechy jednostek [UnitKeyword_S_CORP] — tekst] S사
   źródło: UnitKeyword-exem.json :: dataList[id=UnitKeyword_S_CORP].content
   limit: do 120 znaków
   EN: S Corp.
   PL: Korp. S
136. [Pojęcia bazowe i cechy jednostek [UnitKeyword_S_CORP_SAL] — tekst] 살 당파
   źródło: UnitKeyword-exem.json :: dataList[id=UnitKeyword_S_CORP_SAL].content
   limit: do 120 znaków
   EN: Court Circle - Sal
   PL: Stronnictwo Dworskie - Sal

## Pojęcia bazowe i cechy jednostek: UnitKeyword-pilgrimage
- plik gry: `UnitKeyword-pilgrimage.json`

137. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SEA_TERROR] — tekst] 시테러
   źródło: UnitKeyword-pilgrimage.json :: dataList[id=UnitKeyword_SEA_TERROR].content
   limit: do 120 znaków
   EN: Sea Terror
   PL: Morski Koszmar
138. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SEA_BORN] — tekst] 시본
   źródło: UnitKeyword-pilgrimage.json :: dataList[id=UnitKeyword_SEA_BORN].content
   limit: do 120 znaków
   EN: Seaborn
   PL: Zrodzony z Morza
139. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LAST_KNIGHT] — tekst] 신탁 대행자
   źródło: UnitKeyword-pilgrimage.json :: dataList[id=UnitKeyword_LAST_KNIGHT].content
   limit: do 120 znaków
   EN: The Oracle's Proxy
   PL: Pełnomocnik Wyroczni

## Pojęcia bazowe i cechy jednostek: UnitKeyword-x1p1c1
- plik gry: `UnitKeyword-x1p1c1.json`

140. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_ASSO_1] — tekst] 림버스 유치원
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_ASSO_1].content
   limit: do 120 znaków
   EN: Limbus Kindergarten
   PL: Przedszkole Limbus
141. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_ASSO_2] — tekst] 펭귄반
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_ASSO_2].content
   limit: do 120 znaków
   EN: Perky Penguins
   PL: Grupa Pingwinków
142. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_ASSO_3] — tekst] 병아리반
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_ASSO_3].content
   limit: do 120 znaków
   EN: Cheery Chickies
   PL: Grupa Kurczaczków
143. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_ASSO_4] — tekst] 코끼리반
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_ASSO_4].content
   limit: do 120 znaków
   EN: Early Elephants
   PL: Grupa Słoników
144. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_KEYWORD_1] — tekst] 바삭한 튀김용
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_KEYWORD_1].content
   limit: do 120 znaków
   EN: For Crunchy Frying
   PL: Do Chrupiącego Smażenia
145. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_KEYWORD_2] — tekst] 달콤한 스튜용
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_KEYWORD_2].content
   limit: do 120 znaków
   EN: For Sweet Stewing
   PL: Do Słodkiego Gulaszu
146. [Pojęcia bazowe i cechy jednostek [UnitKeyword_X1P1C1_KEYWORD_3] — tekst] 새콤한 조림용
   źródło: UnitKeyword-x1p1c1.json :: dataList[id=UnitKeyword_X1P1C1_KEYWORD_3].content
   limit: do 120 znaków
   EN: For Tangy Braising
   PL: Do Kwaśnego Duszenia

## Pojęcia bazowe i cechy jednostek: UnitKeyword
- plik gry: `UnitKeyword.json`

147. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLADE_LINEAGE] — tekst] 검계
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLADE_LINEAGE].content
   limit: do 120 znaków
   EN: Blade Lineage
   PL: Ród Ostrza
148. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_CLOUD] — tekst] 흑운회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_CLOUD].content
   limit: do 120 znaków
   EN: Kurokumo Clan
   PL: Klan Kurokumo
149. [Pojęcia bazowe i cechy jednostek [UnitKeyword_YURODIVY] — tekst] 유로지비
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_YURODIVY].content
   limit: do 120 znaków
   EN: Yurodiviye
   PL: Jurodiwi
150. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MACHINE_BOUND_ORGANISM] — tekst] 기계 융화 생명체
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MACHINE_BOUND_ORGANISM].content
   limit: do 120 znaków
   EN: Mechanical Amalgam
   PL: Mechaniczny Amalgamat
151. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ON_THE_LAKE] — tekst] 호수의 존재
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_ON_THE_LAKE].content
   limit: do 120 znaków
   EN: Lake Entity
   PL: Istota z Jeziora
152. [Pojęcia bazowe i cechy jednostek [UnitKeyword_N_CORP] — tekst] N사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_N_CORP].content
   limit: do 120 znaków
   EN: N Corp.
   PL: Korp. N
153. [Pojęcia bazowe i cechy jednostek [UnitKeyword_K_CORP] — tekst] K사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_K_CORP].content
   limit: do 120 znaków
   EN: K Corp.
   PL: Korp. K
154. [Pojęcia bazowe i cechy jednostek [UnitKeyword_G_CORP] — tekst] G사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_G_CORP].content
   limit: do 120 znaków
   EN: G Corp.
   PL: Korp. G
155. [Pojęcia bazowe i cechy jednostek [UnitKeyword_W_CORP] — tekst] W사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_W_CORP].content
   limit: do 120 znaków
   EN: W Corp.
   PL: Korp. W
156. [Pojęcia bazowe i cechy jednostek [UnitKeyword_R_CORP] — tekst] R사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_R_CORP].content
   limit: do 120 znaków
   EN: R Corp.
   PL: Korp. R
157. [Pojęcia bazowe i cechy jednostek [UnitKeyword_T_CORP] — tekst] T사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_T_CORP].content
   limit: do 120 znaków
   EN: T Corp.
   PL: Korp. T
158. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SEVEN] — tekst] 세븐 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_SEVEN].content
   limit: do 120 znaków
   EN: Seven Association
   PL: Stowarzyszenie Seven
159. [Pojęcia bazowe i cechy jednostek [UnitKeyword_CINQ] — tekst] 섕크 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_CINQ].content
   limit: do 120 znaków
   EN: Cinq Association
   PL: Stowarzyszenie Cinq
160. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ZWEI] — tekst] 츠바이 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_ZWEI].content
   limit: do 120 znaków
   EN: Zwei Association
   PL: Stowarzyszenie Zwei
161. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIU] — tekst] 리우 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIU].content
   limit: do 120 znaków
   EN: Liu Association
   PL: Stowarzyszenie Liu
162. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SHI] — tekst] 시 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_SHI].content
   limit: do 120 znaków
   EN: Shi Association
   PL: Stowarzyszenie Shi
163. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DIECI] — tekst] 디에치 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DIECI].content
   limit: do 120 znaków
   EN: Dieci Association
   PL: Stowarzyszenie Dieci
164. [Pojęcia bazowe i cechy jednostek [UnitKeyword_OUFI] — tekst] 외우피 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_OUFI].content
   limit: do 120 znaków
   EN: Öufi Association
   PL: Stowarzyszenie Öufi
165. [Pojęcia bazowe i cechy jednostek [UnitKeyword_TROUBLE_SHOOTER] — tekst] 장미스패너 공방
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_TROUBLE_SHOOTER].content
   limit: do 120 znaków
   EN: Rosespanner Workshop
   PL: Warsztat Różanego Klucza
166. [Pojęcia bazowe i cechy jednostek [UnitKeyword_ATL] — tekst] 기술해방연합
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_ATL].content
   limit: do 120 znaków
   EN: Technology Liberation Alliance
   PL: Sojusz Wyzwolenia Technologii
167. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MOLAR] — tekst] 어금니 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MOLAR].content
   limit: do 120 znaków
   EN: Molar Office
   PL: Biuro Trzonowca
168. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MIDDLE_FINGER] — tekst] 중지
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MIDDLE_FINGER].content
   limit: do 120 znaków
   EN: The Middle
   PL: Środkowy
169. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER] — tekst] 약지
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER].content
   limit: do 120 znaków
   EN: The Ring
   PL: Serdeczny
170. [Pojęcia bazowe i cechy jednostek [UnitKeyword_PEQUOD_CREW] — tekst] 피쿼드호
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_PEQUOD_CREW].content
   limit: do 120 znaków
   EN: The Pequod
   PL: Załoga Pequoda
171. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WUTHERING_HEIGHTS] — tekst] 워더링하이츠
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_WUTHERING_HEIGHTS].content
   limit: do 120 znaków
   EN: Wuthering Heights
   PL: Wichrowe Wzgórza
172. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DEAD_RABBITS] — tekst] 데드레빗츠
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DEAD_RABBITS].content
   limit: do 120 znaków
   EN: The Dead Rabbits
   PL: Martwe Króliki
173. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WILD_HUNT] — tekst] 와일드헌트
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_WILD_HUNT].content
   limit: do 120 znaków
   EN: The Wild Hunt
   PL: Dziki Gon
174. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY] — tekst] 림버스 컴퍼니
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY].content
   limit: do 120 znaków
   EN: Limbus Company
   PL: Limbus Company
175. [Pojęcia bazowe i cechy jednostek [UnitKeyword_KONG_KONG] — tekst] 콩콩이파
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_KONG_KONG].content
   limit: do 120 znaków
   EN: Tingtang Gang
   PL: Gang Tingtang
176. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MARIACHI] — tekst] 마리아치
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MARIACHI].content
   limit: do 120 znaków
   EN: Los Mariachis
   PL: Los Mariachis
177. [Pojęcia bazowe i cechy jednostek [UnitKeyword_HOOK_OFFICE] — tekst] 갈고리 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_HOOK_OFFICE].content
   limit: do 120 znaków
   EN: Hook Office
   PL: Biuro Haka
178. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DUAL_HOOK_PIRATE] — tekst] 쌍갈고리 해적단
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DUAL_HOOK_PIRATE].content
   limit: do 120 znaków
   EN: Twinhook Pirates
   PL: Piraci Podwójnego Haka
179. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DAWN] — tekst] 새벽 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DAWN].content
   limit: do 120 znaków
   EN: Dawn Office
   PL: Biuro Świtu
180. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MULTI_CRACK] — tekst] 멀티크랙 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MULTI_CRACK].content
   limit: do 120 znaków
   EN: MultiCrack Office
   PL: Biuro MultiCrack
181. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BACKSTREET_COOK] — tekst] 료.고.파
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BACKSTREET_COOK].content
   limit: do 120 znaków
   EN: R.B.
   PL: R.P.M.
182. [Pojęcia bazowe i cechy jednostek [UnitKeyword_TIEQIU] — tekst] 철공회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_TIEQIU].content
   limit: do 120 znaków
   EN: Tieqiu Crew
   PL: Szajka Tieqiu
183. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LINTON] — tekst] 에드가 가문
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LINTON].content
   limit: do 120 znaków
   EN: Edgar Family
   PL: Ród Edgarów
184. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LOBOTOMY_HEAD] — tekst] 로보토미 본사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LOBOTOMY_HEAD].content
   limit: do 120 znaków
   EN: Lobotomy Corp. Headquarters
   PL: Centrala Lobotomy Corp.
185. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LOBOTOMY_BRANCH] — tekst] 로보토미 지부
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LOBOTOMY_BRANCH].content
   limit: do 120 znaków
   EN: Lobotomy Corp. Branch
   PL: Oddział Lobotomy Corp.
186. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FIXER] — tekst] 해결사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_FIXER].content
   limit: do 120 znaków
   EN: Fixer
   PL: Fikser
187. [Pojęcia bazowe i cechy jednostek [UnitKeyword_CLAN] — tekst] 조직
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_CLAN].content
   limit: do 120 znaków
   EN: Syndicate
   PL: Syndykat
188. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WHITE_PARASITE] — tekst] 백화
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_WHITE_PARASITE].content
   limit: do 120 znaków
   EN: Pallidified
   PL: Zbielały
189. [Pojęcia bazowe i cechy jednostek [UnitKeyword_N_CORP_FNATIC] — tekst] N사 광신도
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_N_CORP_FNATIC].content
   limit: do 120 znaków
   EN: N Corp. Fanatic
   PL: Fanatyk Korp. N
190. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BACK_STREET] — tekst] 뒷골목
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BACK_STREET].content
   limit: do 120 znaków
   EN: The Backstreets
   PL: Zaułki
191. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DEVYAT] — tekst] 제뱌찌 협회
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DEVYAT].content
   limit: do 120 znaków
   EN: Devyat' Association
   PL: Stowarzyszenie Diewiat'
192. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LA_MANCHA_LAND] — tekst] 라만차랜드
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LA_MANCHA_LAND].content
   limit: do 120 znaków
   EN: La Manchaland
   PL: La Manchaland
193. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCE] — tekst] LCE
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCE].content
   limit: do 120 znaków
   EN: LCE
   PL: LCE
194. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCC] — tekst] LCC
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCC].content
   limit: do 120 znaków
   EN: LCC
   PL: LCC
195. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCB] — tekst] LCB
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCB].content
   limit: do 120 znaków
   EN: LCB
   PL: LCB
196. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_RABBIT] — tekst] 흑수 - 묘
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_RABBIT].content
   limit: do 120 znaków
   EN: Heishou Pack - Mao Branch
   PL: Wataha Heishou - Gałąź Mao
197. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST] — tekst] 흑수
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST].content
   limit: do 120 znaków
   EN: Heishou Pack
   PL: Wataha Heishou
198. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_SNAKE] — tekst] 흑수 - 사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_SNAKE].content
   limit: do 120 znaków
   EN: Heishou Pack - Si Branch
   PL: Wataha Heishou - Gałąź Si
199. [Pojęcia bazowe i cechy jednostek [UnitKeyword_THUMB_LEVEL_CAPO_FOUR] — tekst] 카포 IIII
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_THUMB_LEVEL_CAPO_FOUR].content
   limit: do 120 znaków
   EN: Capo IIII
   PL: Capo IIII
200. [Pojęcia bazowe i cechy jednostek [UnitKeyword_THUMB_LEVEL_SOLDATO_TWO] — tekst] 솔다토 II
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_THUMB_LEVEL_SOLDATO_TWO].content
   limit: do 120 znaków
   EN: Soldato II
   PL: Soldato II
201. [Pojęcia bazowe i cechy jednostek [UnitKeyword_THUMB_LEVEL_SOLDATO_THREE] — tekst] 솔다토 III
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_THUMB_LEVEL_SOLDATO_THREE].content
   limit: do 120 znaków
   EN: Soldato III
   PL: Soldato III
202. [Pojęcia bazowe i cechy jednostek [UnitKeyword_EGO_EQUIPMENT] — tekst] E.G.O 장비
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_EGO_EQUIPMENT].content
   limit: do 120 znaków
   EN: E.G.O Gear
   PL: Rynsztunek E.G.O
203. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_CHIEF] — tekst] 흑수 필두
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_CHIEF].content
   limit: do 120 znaków
   EN: Heishou Pack Adept
   PL: Adept Watahy Heishou
204. [Pojęcia bazowe i cechy jednostek [UnitKeyword_H_CORP] — tekst] H사
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_H_CORP].content
   limit: do 120 znaków
   EN: H Corp.
   PL: Korp. H
205. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_GA_CANCELED] — tekst] <color=#d40000><s>가씨 가문</s></color>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_FAMILY_GA_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Jia Family</s></color>
   PL: <color=#d40000><s>Ród Jia</s></color>
206. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_HORSE] — tekst] 흑수 - 오
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_HORSE].content
   limit: do 120 znaków
   EN: Heishou Pack - Wu Branch
   PL: Wataha Heishou - Gałąź Wu
207. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_CHICKEN] — tekst] 흑수 - 유
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_CHICKEN].content
   limit: do 120 znaków
   EN: Heishou Pack - You Branch
   PL: Wataha Heishou - Gałąź You
208. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FAMILY_GA_HIERARCH] — tekst] 가주
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_FAMILY_GA_HIERARCH].content
   limit: do 120 znaków
   EN: Family Hierarch
   PL: Głowa Rodu
209. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_CHIEF_FORMER] — tekst] <color=#d40000><s>흑수 필두</s></color>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_CHIEF_FORMER].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Heishou Pack Adept</s></color>
   PL: <color=#d40000><s>Adept Watahy Heishou</s></color>
210. [Pojęcia bazowe i cechy jednostek [UnitKeyword_NIGHTSTILETTO] — tekst] 밤의 송곳
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_NIGHTSTILETTO].content
   limit: do 120 znaków
   EN: Night Awls
   PL: Nocne Szydła
211. [Pojęcia bazowe i cechy jednostek [UnitKeyword_JEONG_OFFICE] — tekst] 정사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_JEONG_OFFICE].content
   limit: do 120 znaków
   EN: Jeong's Office
   PL: Biuro Jeonga
212. [Pojęcia bazowe i cechy jednostek [UnitKeyword_OUFI_COOP] — tekst] 협력 사무소 - 외우피
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_OUFI_COOP].content
   limit: do 120 znaków
   EN: Associate Office - Öufi
   PL: Biuro Współpracujące - Öufi
213. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BLACK_BEAST_SHEEP] — tekst] 흑수 - 미
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BLACK_BEAST_SHEEP].content
   limit: do 120 znaków
   EN: Heishou Pack - Wei Branch
   PL: Wataha Heishou - Gałąź Wei
214. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCA] — tekst] LCA
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCA].content
   limit: do 120 znaków
   EN: LCA
   PL: LCA
215. [Pojęcia bazowe i cechy jednostek [UnitKeyword_TRUST_AGENT] — tekst] 신탁 대행자
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_TRUST_AGENT].content
   (powtórzenie elementu 139 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
216. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_MAESTRO] — tekst] 마에스트로
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_MAESTRO].content
   limit: do 120 znaków
   EN: Maestro
   PL: Maestro
217. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_DOCENT] — tekst] 도슨트
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_DOCENT].content
   limit: do 120 znaków
   EN: Docent
   PL: Docent
218. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_STUDENT] — tekst] 스튜던트
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_STUDENT].content
   limit: do 120 znaków
   EN: Student
   PL: Student
219. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_FAUVISM] — tekst] 야수파
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_FAUVISM].content
   limit: do 120 znaków
   EN: School of Fauvism
   PL: Szkoła Fowizmu
220. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_POINTILLISM] — tekst] 점묘파
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_POINTILLISM].content
   limit: do 120 znaków
   EN: School of Pointillism
   PL: Szkoła Pointylizmu
221. [Pojęcia bazowe i cechy jednostek [UnitKeyword_RING_FINGER_PHYSICAL] — tekst] 신체파
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_RING_FINGER_PHYSICAL].content
   limit: do 120 znaków
   EN: School of Corporism
   PL: Szkoła Korporyzmu
222. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FINGER_CANCELED] — tekst] <s>손가락</s>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_FINGER_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Fingers</s>
   PL: <s>Palce</s>
223. [Pojęcia bazowe i cechy jednostek [UnitKeyword_MIDDLE_FINGER_CANCELED] — tekst] <s>중지</s>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_MIDDLE_FINGER_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The Middle</s>
   PL: <s>Środkowy</s>
224. [Pojęcia bazowe i cechy jednostek [UnitKeyword_SPIDER_HOUSE_CANCELED] — tekst] <s>거미집</s>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_SPIDER_HOUSE_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <s>, </s>
   EN: <s>The House of Spiders</s>
   PL: <s>Dom Pająków</s>
225. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LIMBUS_COMPANY_LCE_UNSETTLED] — tekst] LCE?
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LIMBUS_COMPANY_LCE_UNSETTLED].content
   limit: do 120 znaków
   EN: LCE?
   PL: LCE?
226. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DIHUI_STAR] — tekst] 지혜성
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DIHUI_STAR].content
   limit: do 120 znaków
   EN: Dihui Star
   PL: Gwiazda Dihui
227. [Pojęcia bazowe i cechy jednostek [UnitKeyword_DIHUI_STAR_CANCELED] — tekst] <color=#d40000><s>지혜성</s></color>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_DIHUI_STAR_CANCELED].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Dihui Star</s></color>
   PL: <color=#d40000><s>Gwiazda Dihui</s></color>
228. [Pojęcia bazowe i cechy jednostek [UnitKeyword_BIG_SISTER_PAST] — tekst] <color=#d40000><s>큰 누님</s></color>
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_BIG_SISTER_PAST].content
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#d40000>, <s>, </s>, </color>
   EN: <color=#d40000><s>Great Sister</s></color>
   PL: <color=#d40000><s>Wielka Siostra</s></color>
229. [Pojęcia bazowe i cechy jednostek [UnitKeyword_LE_KHAKI] — tekst] 르카키
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_LE_KHAKI].content
   limit: do 120 znaków
   EN: Le Kaki
   PL: Le Kaki
230. [Pojęcia bazowe i cechy jednostek [UnitKeyword_WEDGE] — tekst] 쐐기 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_WEDGE].content
   limit: do 120 znaków
   EN: Wedge Office
   PL: Biuro Klina
231. [Pojęcia bazowe i cechy jednostek [UnitKeyword_FIREPUNCH_OFFICE] — tekst] 불주먹 사무소
   źródło: UnitKeyword.json :: dataList[id=UnitKeyword_FIREPUNCH_OFFICE].content
   limit: do 120 znaków
   EN: Firefist Office
   PL: Biuro Ognistej Pięści

## Poczytalność i Panika: MentalCondition-a1c6p3
- plik gry: `MentalCondition-a1c6p3.json`

232. [Poczytalność i Panika [MentalConditionUnknown] — warunek wzrostu poczytalności] 확인 불가
   źródło: MentalCondition-a1c6p3.json :: dataList[id=MentalConditionUnknown].add
   limit: do 120 znaków
   EN: Unobservable
   PL: Niemożliwe do zaobserwowania
233. [Poczytalność i Panika [MentalConditionUnknown] — warunek spadku poczytalności] 확인 불가
   źródło: MentalCondition-a1c6p3.json :: dataList[id=MentalConditionUnknown].min
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Poczytalność i Panika: MentalCondition
- plik gry: `MentalCondition.json`

234. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercent] — warunek wzrostu poczytalności] 합 승리 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercent].add
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Increases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Rośnie po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
235. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercent] — warunek spadku poczytalności] 합 승리 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercent].min
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Decreases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Spada po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
236. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentWithMax] — warunek wzrostu poczytalności] 합 승리 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가, 최대 {2}%)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentWithMax].add
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, {2}, \n
   EN: Increases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1; max {2}%)</size>
   PL: Rośnie po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.; maks. {2}%)</size>
237. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentWithMax] — warunek spadku poczytalności] 합 승리 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가, 최대 {2}%)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentWithMax].min
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, {2}, \n
   EN: Decreases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1; max {2}%)</size>
   PL: Spada po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.; maks. {2}%)</size>
238. [Poczytalność i Panika [OnKillEnemyAsLevelRatioMultiply] — warunek wzrostu poczytalności] 적 처치 시 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyAsLevelRatioMultiply].add
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase by {0} after this unit defeats an enemy whose level was higher than or equal to this unit’s
   PL: Rośnie o {0} po pokonaniu wroga o poziomie równym lub wyższym od tej jednostki
239. [Poczytalność i Panika [OnKillEnemyAsLevelRatioMultiply] — warunek spadku poczytalności] 적 처치 시 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyAsLevelRatioMultiply].min
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after this unit defeats an enemy whose level was higher than or equal to this unit’s
   PL: Spada o {0} po pokonaniu wroga o poziomie równym lub wyższym od tej jednostki
240. [Poczytalność i Panika [OnKillEnemyByOtherAllyAsLevelRatioMultiply] — warunek wzrostu poczytalności] 아군이 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAllyAsLevelRatioMultiply].add
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase by {0} after an ally defeats an enemy whose level was higher than or equal to the unit’s
   PL: Rośnie o {0} gdy sojusznik pokona wroga o poziomie równym lub wyższym od tej jednostki
241. [Poczytalność i Panika [OnKillEnemyByOtherAllyAsLevelRatioMultiply] — warunek spadku poczytalności] 아군이 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAllyAsLevelRatioMultiply].min
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after an ally defeats an enemy whose level was higher than or equal to the unit’s
   PL: Spada o {0} gdy sojusznik pokona wroga o poziomie równym lub wyższym od tej jednostki
242. [Poczytalność i Panika [OnLoseDuelAsParryingCountMultiplyAndPlusPercent] — warunek wzrostu poczytalności] 합 패배 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAsParryingCountMultiplyAndPlusPercent].add
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Increases after losing a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Rośnie po przegranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
243. [Poczytalność i Panika [OnLoseDuelAsParryingCountMultiplyAndPlusPercent] — warunek spadku poczytalności] 합 패배 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAsParryingCountMultiplyAndPlusPercent].min
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Decreases after losing a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Spada po przegranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
244. [Poczytalność i Panika [OnDieAllyAsLevelRatio] — warunek wzrostu poczytalności] 아군 사망 시 사망한 아군의 레벨이 자신의 레벨 이상인 경우,\n 레벨 차에 따라 증가\n<size=95%>(증가량: 기본 값 {0}, 레벨 차이당 {0}씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnDieAllyAsLevelRatio].add
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, \n
   EN: If the level of the defeated ally was higher than or equal to the unit’s,\nincrease based on the level difference\n<size=95%>(Base Value is {0}, raised by {0} per level)</size>
   PL: Gdy polegnie sojusznik o poziomie równym lub wyższym od tej jednostki,\nrośnie zależnie od różnicy poziomów\n<size=95%>(Bazowo {0}, +{0} za każdy poziom różnicy)</size>
245. [Poczytalność i Panika [OnDieAllyAsLevelRatio] — warunek spadku poczytalności] 아군 사망 시 사망한 아군의 레벨이 자신의 레벨 이상인 경우,\n 레벨 차에 따라 감소\n<size=95%>(감소량: 기본 값 {0}, 레벨 차이당 {0}씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnDieAllyAsLevelRatio].min
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, \n
   EN: If the level of the defeated ally was higher than or equal to the unit’s,\ndecrease based on the level difference\n<size=95%>(Base Value is {0}, raised by {0} per level)</size>
   PL: Gdy polegnie sojusznik o poziomie równym lub wyższym od tej jednostki,\nspada zależnie od różnicy poziomów\n<size=95%>(Bazowo {0}, +{0} za każdy poziom różnicy)</size>
246. [Poczytalność i Panika [OnRoundStartAfterEvent] — warunek wzrostu poczytalności] 턴 시작 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnRoundStartAfterEvent].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increased by {0} at the start of the turn
   PL: Rośnie o {0} na początku tury
247. [Poczytalność i Panika [OnRoundStartAfterEvent] — warunek spadku poczytalności] 턴 시작 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnRoundStartAfterEvent].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreased by {0} at the start of the turn
   PL: Spada o {0} na początku tury
248. [Poczytalność i Panika [OnKillEnemyMp] — warunek wzrostu poczytalności] 적 처치 시 처치한 적의 레벨에 관계 없이 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyMp].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase by {0} after this unit defeats an enemy regardless of their level
   PL: Rośnie o {0} po pokonaniu wroga niezależnie od jego poziomu
249. [Poczytalność i Panika [OnKillEnemyMp] — warunek spadku poczytalności] 적 처치 시 처치한 적의 레벨에 관계 없이 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyMp].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after this unit defeats an enemy regardless of their level
   PL: Spada o {0} po pokonaniu wroga niezależnie od jego poziomu
250. [Poczytalność i Panika [OnDieAllyMp] — warunek wzrostu poczytalności] 아군 사망 시 사망한 아군의 레벨에 관계 없이 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnDieAllyMp].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If an ally is defeated, increase by {0} regardless of the ally's level
   PL: Gdy polegnie sojusznik, rośnie o {0} niezależnie od jego poziomu
251. [Poczytalność i Panika [OnDieAllyMp] — warunek spadku poczytalności] 아군 사망 시 사망한 아군의 레벨에 관계 없이 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnDieAllyMp].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If an ally is defeated, decrease by {0} regardless of the ally's level
   PL: Gdy polegnie sojusznik, spada o {0} niezależnie od jego poziomu
252. [Poczytalność i Panika [OnKillEnemyByOtherAllyExceptSupportiveAction] — warunek wzrostu poczytalności] 아군이 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAllyExceptSupportiveAction].add
   (powtórzenie elementu 240 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
253. [Poczytalność i Panika [OnKillEnemyByOtherAllyExceptSupportiveAction] — warunek spadku poczytalności] 아군이 처치한 적의 레벨이 자신의 레벨 이상인 경우 {0} 감소. 원호 공격이 부여된 아군이 처치한 경우에는 감소하지 않음.
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAllyExceptSupportiveAction].min
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after an ally defeats an enemy whose level was higher than or equal to this unit’s. Does not decrease when the enemy was defeated by an Assist Attack.
   PL: Spada o {0} gdy sojusznik pokona wroga o poziomie równym lub wyższym od tej jednostki. Nie spada, jeśli wroga pokonano Atakiem Wsparcia.
254. [Poczytalność i Panika [OnDieBladeLineageAlly] — warunek wzrostu poczytalności] 검계 조직원 사망시 사망한 아군의 레벨에 관계 없이 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnDieBladeLineageAlly].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If a Blade Lineage ally is defeated, gain {0} regardless of the ally's level
   PL: Gdy polegnie sojusznik z Rodu Ostrza, zyskaj {0} niezależnie od jego poziomu
255. [Poczytalność i Panika [OnDieBladeLineageAlly] — warunek spadku poczytalności] 검계 조직원 사망시 사망한 아군의 레벨에 관계 없이 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnDieBladeLineageAlly].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: If a Blade Lineage ally is defeated, lose {0} regardless of the ally's level
   PL: Gdy polegnie sojusznik z Rodu Ostrza, trać {0} niezależnie od jego poziomu
256. [Poczytalność i Panika [OnWinDuelLessMpTarget] — warunek wzrostu poczytalności] 정신력이 자신보다 낮은 대상과의 합에서 승리 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnWinDuelLessMpTarget].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increases by {0} after winning a Clash against an enemy with SP lower than this unit's
   PL: Rośnie o {0} po wygranym Starciu z wrogiem o niższej Poczytalności (SP)
257. [Poczytalność i Panika [OnWinDuelLessMpTarget] — warunek spadku poczytalności] 정신력이 자신보다 낮은 대상과의 합에서 승리 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnWinDuelLessMpTarget].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreases by {0} after winning a Clash against an enemy with SP lower than this unit's
   PL: Spada o {0} po wygranym Starciu z wrogiem o niższej Poczytalności (SP)
258. [Poczytalność i Panika [OnLoseDuelLessMpTarget] — warunek wzrostu poczytalności] 정신력이 자신보다 낮은 대상과의 합에서 패배 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelLessMpTarget].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increases by {0} after losing a Clash against an enemy with SP lower than this unit's
   PL: Rośnie o {0} po przegranym Starciu z wrogiem o niższej Poczytalności (SP)
259. [Poczytalność i Panika [OnLoseDuelLessMpTarget] — warunek spadku poczytalności] 정신력이 자신보다 낮은 대상과의 합에서 패배 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelLessMpTarget].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreases by {0} after losing a Clash against an enemy with SP lower than this unit's
   PL: Spada o {0} po przegranym Starciu z wrogiem o niższej Poczytalności (SP)
260. [Poczytalność i Panika [OnKillEnemyByOtherAlly] — warunek wzrostu poczytalności] 아군이 처치한 적의 레벨에 관계 없이 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAlly].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase by {0} after an ally defeats an enemy regardless of their level
   PL: Rośnie o {0} gdy sojusznik pokona wroga niezależnie od jego poziomu
261. [Poczytalność i Panika [OnKillEnemyByOtherAlly] — warunek spadku poczytalności] 아군이 처치한 적의 레벨에 관계 없이 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnKillEnemyByOtherAlly].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after an ally defeats an enemy regardless of their level
   PL: Spada o {0} gdy sojusznik pokona wroga niezależnie od jego poziomu
262. [Poczytalność i Panika [OnWinDuelAnyTarget] — warunek wzrostu poczytalności] 합 승리 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAnyTarget].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increased by {0} on Clash Win
   PL: Rośnie o {0} po wygranym Starciu
263. [Poczytalność i Panika [OnWinDuelAnyTarget] — warunek spadku poczytalności] 합 승리 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAnyTarget].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreased by {0} on Clash Lose
   PL: Spada o {0} po wygranym Starciu
264. [Poczytalność i Panika [OnLoseDuelAnyTarget] — warunek wzrostu poczytalności] 합 패배 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAnyTarget].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increased by {0} on Clash Lose
   PL: Rośnie o {0} po przegranym Starciu
265. [Poczytalność i Panika [OnLoseDuelAnyTarget] — warunek spadku poczytalności] 합 패배 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAnyTarget].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreased by {0} on Clash Lose
   PL: Spada o {0} po przegranym Starciu
266. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis] — warunek wzrostu poczytalności] 합 승리 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis].add
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, <color=red>, </color>, </size>, {0}, {1}, \n
   EN: Increases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: Rośnie po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
267. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis] — warunek spadku poczytalności] 합 승리 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis].min
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, <color=red>, </color>, </size>, {0}, {1}, \n
   EN: Decreases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: Spada po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
268. [Poczytalność i Panika [OnLoseDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis] — warunek wzrostu poczytalności] 합 패배 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis].add
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, <color=red>, </color>, </size>, {0}, {1}, \n
   EN: Increases after losing a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: Rośnie po przegranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
269. [Poczytalność i Panika [OnLoseDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis] — warunek spadku poczytalności] 합 패배 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelAsParryingCountMultiplyAndPlusPercentWithEmphasis].min
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <size=95%>, <color=red>, </color>, </size>, {0}, {1}, \n
   EN: Decreases after losing a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: Spada po przegranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
270. [Poczytalność i Panika [OnTakeAttackDamagePerWithMax] — warunek wzrostu poczytalności] <color=red>적에게 피격 시 증가\n<size=95%>(증가량: 기본 값 {0}, 턴 당 최대 {1} 증가)</size></color>
   źródło: MentalCondition.json :: dataList[id=OnTakeAttackDamagePerWithMax].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=red>, <size=95%>, </size>, </color>, {0}, {1}, \n
   EN: <color=red>Increases when hit by an enemy\n<size=95%>(Base Value is {0}, raised by up to {1} per Turn)</size></color>
   PL: <color=red>Rośnie po trafieniu przez wroga\n<size=95%>(Bazowo {0}, maks. +{1} na turę)</size></color>
271. [Poczytalność i Panika [OnTakeAttackDamagePerWithMax] — warunek spadku poczytalności] <color=red>적에게 피격 시 감소\n<size=95%>(감소량: 기본 값 {0}, 턴 당 최대 {1} 감소)</size></color>
   źródło: MentalCondition.json :: dataList[id=OnTakeAttackDamagePerWithMax].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=red>, <size=95%>, </size>, </color>, {0}, {1}, \n
   EN: <color=red>Decreases when hit by an enemy\n<size=95%>(Base Value is {0}, raised by up to {1} per Turn)</size></color>
   PL: <color=red>Spada po trafieniu przez wroga\n<size=95%>(Bazowo {0}, maks. -{1} na turę)</size></color>
272. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThan] — warunek wzrostu poczytalności] 정신력이 {2} 이상이면, 합 승리 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThan].add
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {2}, {0}, {1}, \n
   EN: At {2} or higher SP, increases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Przy {2} lub więcej SP: rośnie po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
273. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThan] — warunek spadku poczytalności] 정신력이 {2} 이상이면, 합 승리 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThan].min
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {2}, {0}, {1}, \n
   EN: At {2} or higher SP, decreases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Przy {2} lub więcej SP: spada po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
274. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThanWithEmphasis] — warunek wzrostu poczytalności] <color=red>정신력이 {2} 이상이면,</color> 합 승리 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThanWithEmphasis].add
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=red>, </color>, <size=95%>, </size>, {2}, {0}, {1}, \n
   EN: <color=red>At {2} or higher SP,</color> increases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: <color=red>Przy {2} lub więcej SP:</color> rośnie po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
275. [Poczytalność i Panika [OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThanWithEmphasis] — warunek spadku poczytalności] <color=red>정신력이 {2} 이상이면,</color> 합 승리 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 <color=red>{1}%</color>씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnWinDuelAsParryingCountMultiplyAndPlusPercentIfMpNotLessThanWithEmphasis].min
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <color=red>, </color>, <size=95%>, </size>, {2}, {0}, {1}, \n
   EN: <color=red>At {2} or higher SP,</color> decreases after winning a Clash based on the Clash count\n<size=95%>(Base Value is {0}, raised by <color=red>{1}%</color> per Clash count after 1)</size>
   PL: <color=red>Przy {2} lub więcej SP:</color> spada po wygranym Starciu zależnie od liczby starć\n<size=95%>(Bazowo {0}, +<color=red>{1}%</color> za każde starcie powyżej 1.)</size>
276. [Poczytalność i Panika [OnOneSideAttackEnd] — warunek wzrostu poczytalności] 일방 공격 종료 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnOneSideAttackEnd].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increase by {0} after Unopposed Attack
   PL: Rośnie o {0} po Ataku Jednostronnym
277. [Poczytalność i Panika [OnOneSideAttackEnd] — warunek spadku poczytalności] 일방 공격 종료 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnOneSideAttackEnd].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decrease by {0} after Unopposed Attack
   PL: Spada o {0} po Ataku Jednostronnym
278. [Poczytalność i Panika [OnSucceedAttackAsTargetHasIndexPrescriptTargetToPersonality] — warunek wzrostu poczytalności] 검지의 지령 대상에게 공격이 적중하였다면, 턴 종료 시 정신력 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnSucceedAttackAsTargetHasIndexPrescriptTargetToPersonality].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Gain {0} SP if The Prescript's Target was hit by an attack
   PL: Koniec Tury: Zyskaj {0} SP, jeśli Cel Nakazu został trafiony atakiem
279. [Poczytalność i Panika [OnSucceedAttackAsTargetHasIndexPrescriptTargetToPersonality] — warunek spadku poczytalności] 검지의 지령 대상에게 공격이 적중하였다면, 턴 종료 시 정신력 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnSucceedAttackAsTargetHasIndexPrescriptTargetToPersonality].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Turn End: Lose {0} SP if The Prescript's Target was hit by an attack
   PL: Koniec Tury: Trać {0} SP, jeśli Cel Nakazu został trafiony atakiem
280. [Poczytalność i Panika [OnUseSkillMp] — warunek wzrostu poczytalności] 스킬 사용 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnUseSkillMp].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increases by {0} on Skill Use
   PL: Rośnie o {0} przy użyciu umiejętności
281. [Poczytalność i Panika [OnUseSkillMp] — warunek spadku poczytalności] 스킬 사용 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnUseSkillMp].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreases by {0} on Skill Use
   PL: Spada o {0} przy użyciu umiejętności
282. [Poczytalność i Panika [OnEndAttackMp] — warunek wzrostu poczytalności] 공격 종료 시 {0} 증가
   źródło: MentalCondition.json :: dataList[id=OnEndAttackMp].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Increases by {0} at Attack End
   PL: Rośnie o {0} na koniec ataku
283. [Poczytalność i Panika [OnEndAttackMp] — warunek spadku poczytalności] 공격 종료 시 {0} 감소
   źródło: MentalCondition.json :: dataList[id=OnEndAttackMp].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}
   EN: Decreases by {0} at Attack End
   PL: Spada o {0} na koniec ataku
284. [Poczytalność i Panika [OnGiveNegativeBuffStackToEnemy] — warunek wzrostu poczytalności] 적에게 부정적인 효과 위력을 {0} 부여 할 때 마다 정신력 {1} 증가
   źródło: MentalCondition.json :: dataList[id=OnGiveNegativeBuffStackToEnemy].add
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Increases by {1} after this unit inflicts {0} Potency of a negative effect on an enemy
   PL: Rośnie o {1} za każde nałożenie wrogowi {0} Siły efektu negatywnego
285. [Poczytalność i Panika [OnGiveNegativeBuffStackToEnemy] — warunek spadku poczytalności] 적에게 부정적인 효과 위력을 {0} 부여 할 때 마다 정신력 {1} 감소
   źródło: MentalCondition.json :: dataList[id=OnGiveNegativeBuffStackToEnemy].min
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: {0}, {1}
   EN: Decreases by {1} after this unit inflicts {0} Potency of a negative effect on an enemy
   PL: Spada o {1} za każde nałożenie wrogowi {0} Siły efektu negatywnego
286. [Poczytalność i Panika [OnLoseDuelToSlowerEnemyAsParryingCountMultiplyAndPlusPercent] — warunek wzrostu poczytalności] 자신보다 느린 적에게 합 패배 시 합 횟수에 비례하여 증가\n<size=95%>(증가량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelToSlowerEnemyAsParryingCountMultiplyAndPlusPercent].add
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Increases after losing a Clash, against a slower enemy, based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Rośnie po przegranym Starciu z wolniejszym wrogiem zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>
287. [Poczytalność i Panika [OnLoseDuelToSlowerEnemyAsParryingCountMultiplyAndPlusPercent] — warunek spadku poczytalności] 자신보다 느린 적에게 합 패배 시 합 횟수에 비례하여 감소\n<size=95%>(감소량: 기본 값 {0}, 2합부터 1합당 {1}%씩 증가)</size>
   źródło: MentalCondition.json :: dataList[id=OnLoseDuelToSlowerEnemyAsParryingCountMultiplyAndPlusPercent].min
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: <size=95%>, </size>, {0}, {1}, \n
   EN: Decreases after losing a Clash, against a slower enemy, based on the Clash count\n<size=95%>(Base Value is {0}, raised by {1}% per Clash count after 1)</size>
   PL: Spada po przegranym Starciu z wolniejszym wrogiem zależnie od liczby starć\n<size=95%>(Bazowo {0}, +{1}% za każde starcie powyżej 1.)</size>

## Poczytalność i Panika: PanicInfo-a1c10p1
- plik gry: `PanicInfo-a1c10p1.json`

288. [Poczytalność i Panika [1098] — nazwa Paniki] 가죽 밖으로!
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1098].panicName
   limit: do 40 znaków
   EN: Leave the Leather Behind!
   PL: Porzucić Skórę!
289. [Poczytalność i Panika [1098] — efekt niskiego morale] 방어 레벨 -3, 공격 레벨 +1
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1098].lowMoraleDescription
   limit: do 120 znaków
   EN: Defense Level -3, Offense Level +1
   PL: Poziom Obrony -3, Poziom Ataku +1
290. [Poczytalność i Panika [1098] — efekt Paniki] 방어 레벨 -5, 공격 레벨 +2
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1098].panicDescription
   limit: do 120 znaków
   EN: Defense Level -5, Offense Level +2
   PL: Poziom Obrony -5, Poziom Ataku +2
291. [Poczytalność i Panika [1099] — nazwa Paniki] 껍질 속으로…
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1099].panicName
   limit: do 40 znaków
   EN: Back into My Shell...
   PL: Z Powrotem do Skorupy…
292. [Poczytalność i Panika [1099] — efekt niskiego morale] 속도 최댓값 -1, 방어 레벨 +1
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1099].lowMoraleDescription
   limit: do 120 znaków
   EN: Max Speed -1, Defense Level +1
   PL: Maks. Szybkość -1, Poziom Obrony +1
293. [Poczytalność i Panika [1099] — efekt Paniki] 속도 최댓값 -5, 방어 레벨 +3
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1099].panicDescription
   limit: do 120 znaków
   EN: Max Speed -5, Defense Level +3
   PL: Maks. Szybkość -5, Poziom Obrony +3
294. [Poczytalność i Panika [1099] — tekst klimatyczny] 이대로 단단하게 속으로, 안으로 움츠러든다.
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1099].flavor
   limit: do 120 znaków
   EN: Curl inward. Deeper. Tighter. Let the shell harden around what remains.
   PL: Skul się w sobie. Głębiej. Ciaśniej. Niech skorupa stwardnieje wokół tego, co zostało.
295. [Poczytalność i Panika [1102] — nazwa Paniki] 요리갈망
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1102].panicName
   limit: do 40 znaków
   EN: Culinary Yearning
   PL: Tęsknota Kulinarna
296. [Poczytalność i Panika [1102] — efekt niskiego morale] 자신의 [SapsareeHungry] 1당, 공격 레벨 1 증가, 받는 피해량 +3%
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1102].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SapsareeHungry]
   znaczenie tagów: [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: Offense Level +1 and take +3% damage for every [SapsareeHungry] Stack on self
   PL: Poziom Ataku +1 oraz otrzymywane obrażenia +3% za każdy ładunek [SapsareeHungry] na sobie
297. [Poczytalność i Panika [1102] — efekt Paniki] 자신의 [SapsareeHungry] 1당, 공격 레벨 2 증가, 받는 피해량 +5%
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1102].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [SapsareeHungry]
   znaczenie tagów: [SapsareeHungry] = 배고픈 거예요 / Got an appetite, you hear?
   EN: Offense Level +2 and take +5% damage for every [SapsareeHungry] Stack on self
   PL: Poziom Ataku +2 oraz otrzymywane obrażenia +5% za każdy ładunek [SapsareeHungry] na sobie
298. [Poczytalność i Panika [1102] — tekst klimatyczny] 넌 요리를 하고 싶은 게 아니다. 요리를 하는 느낌과 식사를 하는 흉내를 내고 싶은 것이지.
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1102].flavor
   limit: do 170 znaków
   EN: Don't delude yourself; you're not yearning for "culinary arts." You just want to feel like you're cooking and pretend to dine.
   PL: Nie łudź się — nie pragniesz „sztuki kulinarnej”. Chcesz tylko poczuć, jakbyś gotował, i udawać ucztowanie.
299. [Poczytalność i Panika [1104] — nazwa Paniki] FOMO
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1104].panicName
   limit: do 40 znaków
   EN: FOMO
   PL: FOMO
300. [Poczytalność i Panika [1104] — efekt niskiego morale] 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n[Vulnerable] 1 얻음
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1104].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Offense Level +1 for every 20% missing HP on self (max 2)\nGain 1 [Vulnerable]
   PL: Poziom Ataku +1 za każde 20% brakujących PŻ (maks. 2)\nZyskaj 1 [Vulnerable]
301. [Poczytalność i Panika [1104] — efekt Paniki] 자신의 잃은 체력 20%당, 공격 레벨 1 증가 (최대 2)\n[Vulnerable] 1 얻음
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1104].panicDescription
   (powtórzenie elementu 300 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
302. [Poczytalność i Panika [1104] — tekst klimatyczny] 이번 유행은 놓치면 안 되는데…!
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1104].flavor
   limit: do 120 znaków
   EN: Not again—I'm not gonna miss out on this season's trend!
   PL: Tylko nie znowu — nie mogę przegapić trendu tego sezonu…!
303. [Poczytalność i Panika [1105] — nazwa Paniki] 헝클어진 재봉
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1105].panicName
   limit: do 40 znaków
   EN: Messy Sewing
   PL: Splątane Szycie
304. [Poczytalność i Panika [1105] — efekt niskiego morale] 턴 시작 시 [Reduction] 1 얻음
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1105].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: Turn Start: Gain 1 [Reduction]
   PL: Początek Tury: Zyskaj 1 [Reduction]
305. [Poczytalność i Panika [1105] — efekt Paniki] 턴 시작 시 [Reduction] 1, [AttackDmgDown] 1 얻음
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1105].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction], [AttackDmgDown]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: Turn Start: Gain 1 [Reduction] and 1 [AttackDmgDown]
   PL: Początek Tury: Zyskaj 1 [Reduction] oraz 1 [AttackDmgDown]
306. [Poczytalność i Panika [1121] — nazwa Paniki] 분열
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1121].panicName
   limit: do 40 znaków
   EN: Inner Schism
   PL: Rozłam Wewnętrzny
307. [Poczytalność i Panika [1121] — efekt niskiego morale] 방어 레벨 -3, 공격 레벨 +3\n[BloodyMucus]을 5 보유한 대상과 합 진행 시, 합 위력 +2
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1121].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [BloodyMucus]
   znaczenie tagów: [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: Defense Level -3, Offense Level +3\nIn a Clash against targets that have 5 [BloodyMucus], Clash Power +2
   PL: Poziom Obrony -3, Poziom Ataku +3\nW Starciu z celem mającym 5 [BloodyMucus]: Moc Starcia +2
308. [Poczytalność i Panika [1121] — efekt Paniki] 방어 레벨 -5, 공격 레벨 +3\n가하는 피해량 +10%\n[BloodyMucus]을 3 이상 보유한 대상과 합 진행 시, 합 위력 +3
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1121].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [BloodyMucus]
   znaczenie tagów: [BloodyMucus] = 세례[적] / Baptism [Crimson]
   EN: Defense Level -5, Offense Level +3\nDeal +10% damage\nIn a Clash against targets that have 3 [BloodyMucus], Clash Power +3
   PL: Poziom Obrony -5, Poziom Ataku +3\nZadawane obrażenia +10%\nW Starciu z celem mającym co najmniej 3 [BloodyMucus]: Moc Starcia +3
309. [Poczytalność i Panika [1121] — tekst klimatyczny] 대체…왜? 나는 어떻게 생겼어? 나는… 뭐야?
   źródło: PanicInfo-a1c10p1.json :: dataList[id=1121].flavor
   limit: do 120 znaków
   EN: Why... ? How did I... come to exist? What... am I?
   PL: Dlaczego…? Jak… powstałem? Czym… jestem?

## Poczytalność i Panika: PanicInfo-a1c10p2
- plik gry: `PanicInfo-a1c10p2.json`

310. [Poczytalność i Panika [1109] — nazwa Paniki] 잊혀지지 않은 아픔
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1109].panicName
   limit: do 40 znaków
   EN: Unforgotten Pain
   PL: Niezapomniany Ból
311. [Poczytalność i Panika [1109] — efekt niskiego morale] [Protection] 3 얻음
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1109].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Gain 3 [Protection]
   PL: Zyskaj 3 [Protection]
312. [Poczytalność i Panika [1109] — efekt Paniki] [Protection] 5 얻음
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1109].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Protection]
   znaczenie tagów: [Protection] = 보호 / Protection
   EN: Gain 5 [Protection]
   PL: Zyskaj 5 [Protection]
313. [Poczytalność i Panika [1109] — tekst klimatyczny] …아팠어. 날 찢었었어. 그치만 지금은 지켜줘. 이상해. 지금이 좋아. 그래도 다시 아플까봐 무서워…
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1109].flavor
   limit: do 180 znaków
   EN: ... It hurt. They tore me apart. But now they protect me. It's weird. I like it now. I'm still scared they'll hurt me again, though...
   PL: …Bolało. Rozszarpali mnie. Ale teraz mnie chronią. Dziwne. Teraz mi dobrze. Choć wciąż boję się, że znów sprawią mi ból…
314. [Poczytalność i Panika [1113] — nazwa Paniki] 자식 잃은 것
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1113].panicName
   limit: do 40 znaków
   EN: Bereaved of Child
   PL: Utrata Dziecka
315. [Poczytalność i Panika [1113] — efekt niskiego morale] 스킬 사용 시 <color=#ff6000><mark=#ff000040><b><u>메인 타겟이 뿌이면, 합 위력 +3, 기본 위력 +2</u></b></mark></color>\n피격 시 [TangleBlackYarn] 1 부여 (스킬당 3회)
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1113].lowMoraleDescription
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TangleBlackYarn]
   znaczenie tagów: [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: - Low Morale\n- On Skill Use, <color=#ff6000><mark=#ff000040><b><u>if Pwie is the main target, Clash Power +3, Base Power +2</u></b></mark></color>\n- When hit, inflict 1 [TangleBlackYarn] (3 times per Skill)
   PL: - Niskie Morale\n- Przy Użyciu Umiejętności: <color=#ff6000><mark=#ff000040><b><u>jeśli głównym celem jest Pwie, Moc Starcia +3, Moc Bazowa +2</u></b></mark></color>\n- Przy otrzymaniu trafienia: nałóż 1 [TangleBlackYarn] (3 razy na umiejętność)
316. [Poczytalność i Panika [1113] — efekt Paniki] <color=#ff6000><mark=#ff000040><b><u>모든 공격의 대상을 뿌이로 지정</u></b></mark></color>\n전투 시작 시 스킬의 모든 코인이 <color=#ff6000><mark=#ff000040><b><u>파괴 불가 코인</u></b></mark></color>으로 변경됨\n스킬 사용 시 <color=#ff6000><mark=#ff000040><b><u>메인 타겟이 뿌이면, 합 위력 +6, 기본 위력 +4</u></b></mark></color>\n피격 시 [TangleBlackYarn] 1 부여 (스킬당 6회)
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1113].panicDescription
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark=#ff000040>, <b>, <u>, </u>, </b>, </mark>, </color>, \n, [TangleBlackYarn]
   znaczenie tagów: [TangleBlackYarn] = 뒤엉킴 / Tangling
   EN: - <color=#ff6000><mark=#ff000040><b><u>All Attacks target Pwie</u></b></mark></color>\n- Combat Start: Convert all Skill Coins into <color=#ff6000><mark=#ff000040><b><u>Unbreakable Coins</u></b></mark></color>\n- On Skill Use, <color=#ff6000><mark=#ff000040><b><u>if Pwie is the main target, Clash Power +6, Base Power +4</u></b></mark></color>\n- When hit, inflict 1 [TangleBlackYarn] (6 times per Skill)
   PL: - <color=#ff6000><mark=#ff000040><b><u>Wszystkie ataki celują w Pwie</u></b></mark></color>\n- Początek Walki: zamień wszystkie Monety umiejętności na <color=#ff6000><mark=#ff000040><b><u>Monety Niezniszczalne</u></b></mark></color>\n- Przy Użyciu Umiejętności: <color=#ff6000><mark=#ff000040><b><u>jeśli głównym celem jest Pwie, Moc Starcia +6, Moc Bazowa +4</u></b></mark></color>\n- Przy otrzymaniu trafienia: nałóż 1 [TangleBlackYarn] (6 razy na umiejętność)
317. [Poczytalność i Panika [1113] — tekst klimatyczny] 분노하고 슬퍼하며 울부짖지만 이 감정은 업보일것이다. 탄생은 죽음과 붙어있고 큰 상실을 각오해야했음을 모른채 알을 품고 품은 것의 업보. 이것에 선도 악도 없다. 어리석음만 있다.
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1113].flavor
   limit: do 330 znaków
   tokeny: zachowaj dokładnie: \n
   EN: It rages, grieves, and howls, but these emotions are its karma. Birth is bound to death, and it cradled the egg without knowing that to bring something forth is to accept the weight of a greater loss.\nThere is neither good nor evil in this, but only folly.
   PL: Szaleje z gniewu, rozpacza i wyje, lecz te uczucia to jego karma. Narodziny są splecione ze śmiercią, a ono tuliło jajo, nie wiedząc, że powołanie czegoś na świat oznacza zgodę na ciężar jeszcze większej straty.\nNie ma w tym dobra ani zła — jedynie głupota.
318. [Poczytalność i Panika [1110] — nazwa Paniki] 손떨림
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1110].panicName
   limit: do 40 znaków
   EN: Trembling Hands
   PL: Drżące Dłonie
319. [Poczytalność i Panika [1110] — efekt niskiego morale] 받는 피해량 +7.5%\n피격받을 때마다 자신의 [Vibration] 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1110].lowMoraleDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: - Take +7.5% damage\n- Every time this unit is hit, gain +1 [Vibration] Count (once per Skill, max 5 per turn)
   PL: - Otrzymywane obrażenia +7,5%\n- Przy każdym otrzymanym trafieniu zyskaj +1 Licznika [Vibration] (raz na umiejętność, maks. 5 na turę)
320. [Poczytalność i Panika [1110] — efekt Paniki] 받는 피해량 +15%\n피격받을 때마다 자신의 [Vibration] 위력 1, [Vibration] 횟수 1 증가 (스킬당 1회, 턴당 최대 5)
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1110].panicDescription
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: - Take +15% damage\n- Every time this unit is hit, gain 1 [Vibration] Potency and +1 [Vibration] Count (once per Skill, max 5 per turn)
   PL: - Otrzymywane obrażenia +15%\n- Przy każdym otrzymanym trafieniu zyskaj 1 Siły [Vibration] oraz +1 Licznika [Vibration] (raz na umiejętność, maks. 5 na turę)
321. [Poczytalność i Panika [1110] — tekst klimatyczny] 손이 떨리면, 가위질도 흔들려… 이대로는 재단할 수 없어…
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1110].flavor
   limit: do 160 znaków
   EN: My hands are starting to shake, and even the scissors won't stay steady... I won't be able to cut the pattern anymore...
   PL: Dłonie zaczynają mi drżeć, nawet nożyce nie tną równo… Tak nie zdołam już wykroić formy…
322. [Poczytalność i Panika [1115] — nazwa Paniki] 머신 잼
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1115].panicName
   limit: do 40 znaków
   EN: Jammed Machine
   PL: Zacięcie Maszyny
323. [Poczytalność i Panika [1115] — efekt niskiego morale] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -5%
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1115].lowMoraleDescription
   limit: do 120 znaków
   EN: Skills deal -5% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają -5% obrażeń celom o niższej Szybkości od tej jednostki
324. [Poczytalność i Panika [1115] — efekt Paniki] 자신보다 속도가 낮은 대상에게 가하는 스킬 피해량 -10%
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1115].panicDescription
   limit: do 120 znaków
   EN: Skills deal -10% damage against targets with slower Speed than this unit's
   PL: Umiejętności zadają -10% obrażeń celom o niższej Szybkości od tej jednostki
325. [Poczytalność i Panika [1115] — tekst klimatyczny] 자신보다 빠른 것을 고정시킬 수 있는가?
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1115].flavor
   limit: do 120 znaków
   EN: Can that which moves faster than oneself truly be fixed in place?
   PL: Czy można unieruchomić coś, co porusza się szybciej od nas samych?
326. [Poczytalność i Panika [1112] — nazwa Paniki] 통제 불능
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1112].panicName
   limit: do 40 znaków
   EN: Disabled Overseeing
   PL: Utrata Nadzoru
327. [Poczytalność i Panika [1112] — efekt niskiego morale] 스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 [Reduction] 1 부여
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1112].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Reduction]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down
   EN: - Skill Final Power +1\n- Turn Start: Apply 1 [Reduction] to all other allies
   PL: - Moc Końcowa umiejętności +1\n- Początek Tury: nałóż 1 [Reduction] na wszystkich pozostałych sojuszników
328. [Poczytalność i Panika [1112] — efekt Paniki] 스킬 최종 위력 +1\n턴 시작시 자신을 제외한 모든 아군에게 [Reduction] 1, [AttackDmgDown] 1 부여
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1112].panicDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [Reduction], [AttackDmgDown]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: - Skill Final Power +1\n- Turn Start: Apply 1 [Reduction] and 1 [AttackDmgDown] to all other allies
   PL: - Moc Końcowa umiejętności +1\n- Początek Tury: nałóż 1 [Reduction] oraz 1 [AttackDmgDown] na wszystkich pozostałych sojuszników
329. [Poczytalność i Panika [1111] — nazwa Paniki] 첫 껍질속으로…
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1111].panicName
   limit: do 40 znaków
   EN: Into the First Shell...
   PL: Do Pierwszej Skorupy…
330. [Poczytalność i Panika [1111] — efekt niskiego morale] 공격 레벨 -2, 방어 레벨 +2
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1111].lowMoraleDescription
   limit: do 120 znaków
   EN: Offense Level -2, Defense Level +2
   PL: Poziom Ataku -2, Poziom Obrony +2
331. [Poczytalność i Panika [1111] — efekt Paniki] 공격 레벨 -3, 방어 레벨 +4
   źródło: PanicInfo-a1c10p2.json :: dataList[id=1111].panicDescription
   limit: do 120 znaków
   EN: Offense Level -3, Defense Level +4
   PL: Poziom Ataku -3, Poziom Obrony +4

## Poczytalność i Panika: PanicInfo-a1c10p3
- plik gry: `PanicInfo-a1c10p3.json`

332. [Poczytalność i Panika [1114] — nazwa Paniki] 르 데지르(le désir)
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1114].panicName
   limit: do 40 znaków
   EN: Le Désir
   PL: Le Désir
333. [Poczytalność i Panika [1114] — efekt niskiego morale] 공격 레벨 +3, 방어 레벨 +3
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1114].lowMoraleDescription
   limit: do 120 znaków
   EN: Offense Level +3, Defense Level +3
   PL: Poziom Ataku +3, Poziom Obrony +3
334. [Poczytalność i Panika [1114] — efekt Paniki] 공격 레벨 +5, 방어 레벨 +5
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1114].panicDescription
   limit: do 120 znaków
   EN: Offense Level +5, Defense Level +5
   PL: Poziom Ataku +5, Poziom Obrony +5
335. [Poczytalność i Panika [1114] — tekst klimatyczny] 전부 모르는 말들뿐이야. 그냥 어디선가 와버렸어.\n멋대로 떠오르고, 멋대로 새겨진… 밖에서 온 그럴싸한 말들뿐이야. 난 이 말들을 전혀 몰라.\n\n…그런데도, 알겠어.
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1114].flavor
   limit: do 350 znaków
   tokeny: zachowaj dokładnie: \n
   EN: I don't know any of these words. They just... came from somewhere.\nThey pop into my head on their own. They get stuck in there on their own. They're all just fancy-sounding words that came from outside. I don't really know what any of them mean.\n\n... But somehow, I get it...
   PL: Nie znam żadnego z tych słów. Po prostu… skądś przyszły.\nSame wypływają w głowie, same się w niej ryją… To tylko zgrabnie brzmiące słowa z zewnątrz. Zupełnie ich nie znam.\n\n…A mimo to rozumiem.
336. [Poczytalność i Panika [1116] — nazwa Paniki] 싱크 오류
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1116].panicName
   limit: do 40 znaków
   EN: Sync Error
   PL: Błąd Synchronizacji
337. [Poczytalność i Panika [1116] — efekt niskiego morale] 받는 피해량 +12.5%\n속도 최솟값, 최댓값 -1\n[ChargeNoir]을 소모하는 스킬의 피해량 -15%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1116].lowMoraleDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: - Take +12.5% damage\n- Min & Max Speed -1\n- Deal -15% damage using Skills that consume [ChargeNoir]
   PL: - Otrzymywane obrażenia +12,5%\n- Min. i Maks. Szybkość -1\n- Obrażenia umiejętności zużywających [ChargeNoir] -15%
338. [Poczytalność i Panika [1116] — efekt Paniki] 받는 피해량 +20%\n속도 최솟값, 최댓값 -2\n[ChargeNoir]을 소모하는 스킬의 피해량 -25%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1116].panicDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: \n, [ChargeNoir]
   znaczenie tagów: [ChargeNoir] = 보존 / Preservation
   EN: - Take +20% damage\n- Min & Max Speed -2\n- Deal -25% damage using Skills that consume [ChargeNoir]
   PL: - Otrzymywane obrażenia +20%\n- Min. i Maks. Szybkość -2\n- Obrażenia umiejętności zużywających [ChargeNoir] -25%
339. [Poczytalność i Panika [1117] — nazwa Paniki] 죄악감
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1117].panicName
   limit: do 40 znaków
   EN: Compunction
   PL: Poczucie Winy
340. [Poczytalność i Panika [1117] — efekt niskiego morale] 속도 최솟값, 최댓값 -1\n자신보다 속도가 높은 대상에게 받는 피해량 +10%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1117].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed -1\n- Take +10% damage from targets with faster Speed than self
   PL: - Min. i Maks. Szybkość -1\n- Otrzymywane obrażenia od szybszych celów +10%
341. [Poczytalność i Panika [1117] — efekt Paniki] 속도 최솟값, 최댓값 -2\n자신보다 속도가 높은 대상에게 받는 피해량 +15%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1117].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n
   EN: - Min & Max Speed -2\n- Take +15% damage from targets with faster Speed than self
   PL: - Min. i Maks. Szybkość -2\n- Otrzymywane obrażenia od szybszych celów +15%
342. [Poczytalność i Panika [1117] — tekst klimatyczny] ‘당신은 죄악이 등을 타고 오르는 것을 느꼈다.’
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1117].flavor
   limit: do 120 znaków
   EN: "You feel your sins crawling on your back."
   PL: „Czujesz, jak twoje grzechy pełzną ci po plecach”.
343. [Poczytalność i Panika [1118] — nazwa Paniki] 검은신-르누아르의 거인-신부-망치파
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1118].panicName
   limit: do 100 znaków
   EN: The Obsidian God - The Giant of Le Noir - The Chaplain - Les Marteaux
   PL: Czarny Bóg - Olbrzym Le Noir - Kapelan - Les Marteaux
344. [Poczytalność i Panika [1118] — efekt niskiego morale] 확인 불가
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1118].lowMoraleDescription
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
345. [Poczytalność i Panika [1118] — efekt Paniki] 확인 불가
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1118].panicDescription
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
346. [Poczytalność i Panika [1118] — tekst klimatyczny] 시지프 시스템 내부의 시간은 물질적인 저항 없이 굉장히 빠르게 흐르지만, 거인들은 저마다의 관점을 통해 시스템 내부 시간과 동기화하여 고객들과 소통의 시간을 가질 수 있다.\n\n그중에서도 망치파를 대표하는 거인은 시스템 내부의 기억과 시간을 통제하고, 부분적이지만 독단적으로 재고를 리셋할 수 있다.
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1118].flavor
   limit: do 550 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Time passes at a tremendous pace within the Sisyphe System, unhindered by material resistance. Yet through their respective viewpoints, the Giants can synchronize themselves with the System's internal flow of time and communicate with its customers.\n\nAmong them, the Giant who represents the Hammers holds authority over the System's internal memories and time, with the power to reset portions of its inventory at his own discretion.
   PL: Wewnątrz Systemu Sisyphe czas płynie w zawrotnym tempie, wolny od oporu materii, lecz Olbrzymy dzięki własnym punktom widzenia potrafią zsynchronizować się z wewnętrznym biegiem czasu Systemu i rozmawiać z klientami.\n\nSpośród nich Olbrzym reprezentujący Młoty sprawuje władzę nad pamięcią i czasem wewnątrz Systemu, mogąc wedle uznania częściowo resetować jego zasoby.
347. [Poczytalność i Panika [1120] — nazwa Paniki] 좀 더 가죽 밖으로!
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1120].panicName
   limit: do 40 znaków
   EN: Farther Past the Hide!
   PL: Jeszcze Dalej Poza Skórę!
348. [Poczytalność i Panika [1120] — efekt niskiego morale] 방어 레벨 -2, 공격 레벨 +2
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1120].lowMoraleDescription
   limit: do 120 znaków
   EN: Defense Level -2, Offense Level +2
   PL: Poziom Obrony -2, Poziom Ataku +2
349. [Poczytalność i Panika [1120] — efekt Paniki] 방어 레벨 -5, 공격 레벨 +3
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1120].panicDescription
   limit: do 120 znaków
   EN: Defense Level -5, Offense Level +3
   PL: Poziom Obrony -5, Poziom Ataku +3
350. [Poczytalność i Panika [1122] — nazwa Paniki] 라 노제(la nausée)
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1122].panicName
   limit: do 40 znaków
   EN: La Nausée
   PL: La Nausée
351. [Poczytalność i Panika [1122] — efekt niskiego morale] 가하는 피해량 -10%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1122].lowMoraleDescription
   limit: do 120 znaków
   EN: Deal -10% damage
   PL: Zadawane obrażenia -10%
352. [Poczytalność i Panika [1122] — efekt Paniki] 기본 위력 -1, 가하는 피해량 -10%
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1122].panicDescription
   limit: do 120 znaków
   EN: Base Power -1, deal -10% damage
   PL: Moc Bazowa -1, zadawane obrażenia -10%
353. [Poczytalność i Panika [1122] — tekst klimatyczny] 세계에 대한 구역질과 메스꺼움. 이 세계는 그저 있다. 모든 것에 의미라는 것은 없고, 그저 우연의 산물로 눈앞에 놓여있을 뿐이다.\n\n단지 우연이다. 모든 것이.
   źródło: PanicInfo-a1c10p3.json :: dataList[id=1122].flavor
   limit: do 260 znaków
   tokeny: zachowaj dokładnie: \n
   EN: Revulsion. Nausea before the world. The world simply exists. Nothing in it bears any inherent meaning; everything before our eyes is merely the product of chance.\n\nEverything is a contingency. Everything.
   PL: Wstręt i mdłości wobec świata. Ten świat po prostu jest. Nic nie ma w nim żadnego sensu — wszystko przed naszymi oczami to jedynie dzieło przypadku.\n\nWszystko jest przypadkiem. Wszystko.

## Poczytalność i Panika: PanicInfo-a1c6p1
- plik gry: `PanicInfo-a1c6p1.json`

354. [Poczytalność i Panika [1017] — nazwa Paniki] 정리 강박
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1017].panicName
   limit: do 40 znaków
   EN: Organization Compulsion
   PL: Przymus Porządkowania
355. [Poczytalność i Panika [1017] — efekt niskiego morale] 합 패배 시 정신력 5 감소. 피격 시 다음 턴에 [Agility] 1 얻음 (최대 2)
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1017].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Agility]
   znaczenie tagów: [Agility] = 신속 / Haste
   EN: Lose 5 SP on Clash Lose. Gain 1 [Agility] next turn when hit (max 2)
   PL: Trać 5 SP po przegranym Starciu. Przy trafieniu zyskaj 1 [Agility] w następnej turze (maks. 2)
356. [Poczytalność i Panika [1017] — efekt Paniki] [Vulnerable] 2 얻음. 피격 시 다음 턴에 [Agility] 1 얻음 (최대 3)
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1017].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Agility]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Agility] = 신속 / Haste
   EN: Gain 2 [Vulnerable]. Gain 1 [Agility] next turn when hit (max 3)
   PL: Zyskaj 2 [Vulnerable]. Przy trafieniu zyskaj 1 [Agility] w następnej turze (maks. 3)
357. [Poczytalność i Panika [1018] — nazwa Paniki] 저택의 메아리
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1018].panicName
   limit: do 40 znaków
   EN: Echoes of the Manor
   PL: Echa Posiadłości
358. [Poczytalność i Panika [1018] — efekt niskiego morale] 자신의 합 위력 -1. 앞면 적중 시 피해량 +10%
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1018].lowMoraleDescription
   limit: do 120 znaków
   EN: Clash Power -1 on self. Deal +10% damage on Heads Hit
   PL: Moc Starcia -1. Zadawane obrażenia +10% przy Trafieniu Awersem
359. [Poczytalność i Panika [1018] — efekt Paniki] 자신의 합 위력 -2. [AttackDmgUp] 1 얻음
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1018].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Clash Power -2 on self. Gain 1 [AttackDmgUp]
   PL: Moc Starcia -2. Zyskaj 1 [AttackDmgUp]
360. [Poczytalność i Panika [1020] — nazwa Paniki] 분열
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1020].panicName
   limit: do 40 znaków
   EN: Splitting
   PL: Rozszczepienie
361. [Poczytalność i Panika [1020] — efekt niskiego morale] 합 진행 시 매 합마다 자신의 체력 2 피해, 턴 시작 시 [AttackUp] 1 얻음.
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1020].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Lose 2 HP on self with every Clash. Gain 1 [AttackUp] at Turn Start.
   PL: Trać 2 PŻ przy każdym Starciu. Początek Tury: zyskaj 1 [AttackUp].
362. [Poczytalność i Panika [1020] — efekt Paniki] 합 진행 시 매 합마다 자신의 체력 3 피해, 턴 시작 시 [AttackUp] 2 얻음.
   źródło: PanicInfo-a1c6p1.json :: dataList[id=1020].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Lose 3 HP on self with every Clash. Gain 2 [AttackUp] at Turn Start.
   PL: Trać 3 PŻ przy każdym Starciu. Początek Tury: zyskaj 2 [AttackUp].

## Poczytalność i Panika: PanicInfo-a1c6p2
- plik gry: `PanicInfo-a1c6p2.json`

363. [Poczytalność i Panika [1019] — nazwa Paniki] 흐트러진 그림
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1019].panicName
   limit: do 40 znaków
   EN: Misshapen Painting
   PL: Zniekształcony Obraz
364. [Poczytalność i Panika [1019] — efekt niskiego morale] [Enhancement] 1, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1019].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: Gain 1 [Enhancement] and 1 [Vulnerable]
   PL: Zyskaj 1 [Enhancement] oraz 1 [Vulnerable]
365. [Poczytalność i Panika [1019] — efekt Paniki] [PlusCoinValueUp] 1, [Vulnerable] 3 얻음.
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1019].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PlusCoinValueUp], [Vulnerable]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [Vulnerable] = 취약 / Fragile
   EN: Gain 1 [PlusCoinValueUp] and 3 [Vulnerable].
   PL: Zyskaj 1 [PlusCoinValueUp] oraz 3 [Vulnerable].
366. [Poczytalność i Panika [1021] — nazwa Paniki] 복수
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1021].panicName
   limit: do 40 znaków
   EN: Revenge
   PL: Zemsta
367. [Poczytalność i Panika [1021] — efekt niskiego morale] [DefenseDown] 3, [AttackDmgUp] 3 얻음
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1021].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Gain 3 [DefenseDown] and 3 [AttackDmgUp]
   PL: Zyskaj 3 [DefenseDown] oraz 3 [AttackDmgUp]
368. [Poczytalność i Panika [1021] — efekt Paniki] [DefenseDown] 6, [AttackDmgUp] 5 얻음
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1021].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Gain 6 [DefenseDown] and 5 [AttackDmgUp]
   PL: Zyskaj 6 [DefenseDown] oraz 5 [AttackDmgUp]
369. [Poczytalność i Panika [1022] — nazwa Paniki] 증오
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1022].panicName
   limit: do 40 znaków
   EN: Hatred
   PL: Nienawiść
370. [Poczytalność i Panika [1022] — efekt niskiego morale] 합 승리 시 다음 턴에 [AttackUp]를 1 얻음. (턴 당 최대 3)\n합 패배 시 [DefenseUp]를 1 얻음. (턴 당 최대 3)
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1022].lowMoraleDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Clash Win: Gain 1 [AttackUp] next turn. (3 times per turn)\nClash Lose: Gain 1 [DefenseUp]. (3 times per turn)
   PL: Wygrane Starcie: zyskaj 1 [AttackUp] w następnej turze (maks. 3 na turę)\nPrzegrane Starcie: zyskaj 1 [DefenseUp] (maks. 3 na turę)
371. [Poczytalność i Panika [1022] — efekt Paniki] 합 승리 시 이번 턴과 다음 턴에 [AttackUp]를 1 얻음. (턴 당 최대 3)\n합 패배 시 [DefenseUp]를 1 얻음. (턴 당 최대 3)\n턴 종료 시 다음 턴에 [Agility]을 2 얻음
   źródło: PanicInfo-a1c6p2.json :: dataList[id=1022].panicDescription
   limit: do 210 znaków
   tokeny: zachowaj dokładnie: \n, [AttackUp], [DefenseUp], [Agility]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Agility] = 신속 / Haste
   EN: Clash Win: Gain 1 [AttackUp] this turn and next turn (3 times per turn)\nClash Lose: Gain 1 [DefenseUp] (3 times per turn)\nTurn End: Gain 2 [Agility] next turn
   PL: Wygrane Starcie: zyskaj 1 [AttackUp] w tej i następnej turze (maks. 3 na turę)\nPrzegrane Starcie: zyskaj 1 [DefenseUp] (maks. 3 na turę)\nKoniec Tury: zyskaj 2 [Agility] w następnej turze

## Poczytalność i Panika: PanicInfo-a1c6p3
- plik gry: `PanicInfo-a1c6p3.json`

372. [Poczytalność i Panika [9997] — nazwa Paniki] ???
   źródło: PanicInfo-a1c6p3.json :: dataList[id=9997].panicName
   (powtórzenie elementu 122 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
373. [Poczytalność i Panika [9997] — efekt Paniki] 확인 불가
   źródło: PanicInfo-a1c6p3.json :: dataList[id=9997].panicDescription
   (powtórzenie elementu 232 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)

## Poczytalność i Panika: PanicInfo-a1c7p1
- plik gry: `PanicInfo-a1c7p1.json`

374. [Poczytalność i Panika [1027] — nazwa Paniki] 굶주림
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1027].panicName
   limit: do 40 znaków
   EN: Hunger
   PL: Głód
375. [Poczytalność i Panika [1027] — efekt niskiego morale] 턴 시작 시, [Binding] 1, [Enhancement] 2 얻음. 턴 종료 시, 정신력 5 피해
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1027].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding], [Enhancement]
   znaczenie tagów: [Binding] = 속박 / Bind; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: Gain 1 [Binding] and 2 [Enhancement]. Take 5 SP damage at Turn End
   PL: Początek Tury: zyskaj 1 [Binding] i 2 [Enhancement]. Koniec Tury: otrzymaj 5 obrażeń SP
376. [Poczytalność i Panika [1027] — efekt Paniki] 턴 시작 시, [Binding] 2, [Enhancement] 4 얻음.
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1027].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Binding], [Enhancement]
   znaczenie tagów: [Binding] = 속박 / Bind; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: gain 2 [Binding] and 4 [Enhancement].
   PL: Początek Tury: zyskaj 2 [Binding] i 4 [Enhancement].
377. [Poczytalność i Panika [1028] — nazwa Paniki] 1:1 전력
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1028].panicName
   limit: do 40 znaków
   EN: Duel Specialist
   PL: Specjalista Pojedynków
378. [Poczytalność i Panika [1028] — efekt niskiego morale] 턴 시작 시, [AttackUp] 2 얻음. 합 패배 시 [DefenseDown] 1얻음 (턴 당 최대 3). 속도 최솟값 -1
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1028].lowMoraleDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: Gain 2 [AttackUp]. On Clash Lose, gain 1 [DefenseDown] (max 3 per turn). Min. Speed -1
   PL: Początek Tury: zyskaj 2 [AttackUp]. Przegrane Starcie: zyskaj 1 [DefenseDown] (maks. 3 na turę). Min. Szybkość -1
379. [Poczytalność i Panika [1028] — efekt Paniki] 턴 시작 시, [AttackUp] 4 얻음. 합 패배 시 [DefenseDown] 2얻음 (턴 당 최대 6). 속도 최솟값 -1
   źródło: PanicInfo-a1c7p1.json :: dataList[id=1028].panicDescription
   limit: do 130 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: Gain 4 [AttackUp]. On Clash Lose, gain 2 [DefenseDown] (max 6 per turn). Min. Speed -1
   PL: Początek Tury: zyskaj 4 [AttackUp]. Przegrane Starcie: zyskaj 2 [DefenseDown] (maks. 6 na turę). Min. Szybkość -1

## Poczytalność i Panika: PanicInfo-a1c7p2
- plik gry: `PanicInfo-a1c7p2.json`

380. [Poczytalność i Panika [1030] — nazwa Paniki] 허무의 굴레
   źródło: PanicInfo-a1c7p2.json :: dataList[id=1030].panicName
   limit: do 40 znaków
   EN: Bridle of Nihility
   PL: Jarzmienie Nicości
381. [Poczytalność i Panika [1030] — efekt niskiego morale] 턴 시작 시, [Enhancement] 1, [DefenseDown] 3 얻음. 턴 종료 시, 정신력 5 피해.
   źródło: PanicInfo-a1c7p2.json :: dataList[id=1030].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: gain 1 [Enhancement] and 3 [DefenseDown]. Take 5 SP at Turn End.
   PL: Początek Tury: zyskaj 1 [Enhancement] i 3 [DefenseDown]. Koniec Tury: trać 5 SP.
382. [Poczytalność i Panika [1030] — efekt Paniki] 턴 시작 시, [Enhancement] 2, [DefenseDown] 6 얻음. 턴 종료 시, 정신력 10 회복.
   źródło: PanicInfo-a1c7p2.json :: dataList[id=1030].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: gain 2 [Enhancement] and 6 [DefenseDown]. Heal 10 SP at Turn End.
   PL: Początek Tury: zyskaj 2 [Enhancement] i 6 [DefenseDown]. Koniec Tury: odzyskaj 10 SP.
383. [Poczytalność i Panika [9996] — nazwa Paniki] 가시
   źródło: PanicInfo-a1c7p2.json :: dataList[id=9996].panicName
   limit: do 40 znaków
   EN: Thorns
   PL: Ciernie
384. [Poczytalność i Panika [9996] — efekt niskiego morale] 합 승리 시, [AttackDmgUp] 1 얻음
   źródło: PanicInfo-a1c7p2.json :: dataList[id=9996].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: On Clash Win, gain 1 [AttackDmgUp]
   PL: Wygrane Starcie: zyskaj 1 [AttackDmgUp]
385. [Poczytalność i Panika [9996] — efekt Paniki] 합 승리 시, [AttackDmgUp] 1 얻음. 턴 종료 시, 다음 턴에 [ParryingResultUp] 2 얻음.
   źródło: PanicInfo-a1c7p2.json :: dataList[id=9996].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [ParryingResultUp]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: On Clash Win, gain 1 [AttackDmgUp]. At Turn End, gain 2 [ParryingResultUp] next turn.
   PL: Wygrane Starcie: zyskaj 1 [AttackDmgUp]. Koniec Tury: zyskaj 2 [ParryingResultUp] w następnej turze.

## Poczytalność i Panika: PanicInfo-a1c7p3
- plik gry: `PanicInfo-a1c7p3.json`

386. [Poczytalność i Panika [1029] — nazwa Paniki] 죄책감
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1029].panicName
   limit: do 40 znaków
   EN: Guilt
   PL: Wyrzuty Sumienia
387. [Poczytalność i Panika [1029] — efekt niskiego morale] 턴 종료 시 다음 턴에 [Vulnerable], [MentalIncreaseDown] 1 얻음
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1029].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [MentalIncreaseDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Turn End: gain 1 [Vulnerable] and [MentalIncreaseDown] next turn
   PL: Koniec Tury: zyskaj 1 [Vulnerable] i 1 [MentalIncreaseDown] w następnej turze
388. [Poczytalność i Panika [1029] — efekt Paniki] 턴 종료 시 다음 턴에 [Vulnerable], [MentalIncreaseDown] 2 얻음.
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1029].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [MentalIncreaseDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Turn End: gain 2 [Vulnerable] and [MentalIncreaseDown] next turn.
   PL: Koniec Tury: zyskaj 2 [Vulnerable] i 2 [MentalIncreaseDown] w następnej turze.
389. [Poczytalność i Panika [1031] — nazwa Paniki] 피올림
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1031].panicName
   limit: do 40 znaków
   EN: Resanguination
   PL: Wzburzenie Krwi
390. [Poczytalność i Panika [1031] — efekt niskiego morale] [Laceration]이 없는 대상이면, 합 위력 -1, 적중시 대상의 [Laceration] 위력만큼 체력 회복
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1031].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If the target does not have [Laceration], Clash Power -1; On Hit, heal HP equal to [Laceration] Potency on the target
   PL: Przeciw celom bez [Laceration]: Moc Starcia -1; Przy Trafieniu: ulecz PŻ równe Sile [Laceration] na celu
391. [Poczytalność i Panika [1031] — efekt Paniki] [Laceration]이 있는 대상이면, 합 위력 +2, [Laceration]이 없는 대상이면, 합 위력 -2, 적중시 대상의 [Laceration] 위력만큼 체력 회복
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1031].panicDescription
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: [Laceration]
   znaczenie tagów: [Laceration] = 출혈 / Bleed
   EN: If the target has [Laceration], Clash Power +2; if the target does not have [Laceration], Clash Power -2; On Hit, heal HP equal to [Laceration] Potency on the target
   PL: Przeciw celom z [Laceration]: Moc Starcia +2; przeciw celom bez [Laceration]: Moc Starcia -2; Przy Trafieniu: ulecz PŻ równe Sile [Laceration] na celu
392. [Poczytalność i Panika [1032] — nazwa Paniki] 죄책감
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1032].panicName
   (powtórzenie elementu 386 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
393. [Poczytalność i Panika [1032] — efekt niskiego morale] 턴 종료 시 다음 턴에 [Vulnerable], [MentalIncreaseDown] 1 얻음
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1032].lowMoraleDescription
   (powtórzenie elementu 387 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
394. [Poczytalność i Panika [1032] — efekt Paniki] 턴 종료 시 다음 턴에 [Vulnerable], [MentalIncreaseDown] 2 얻음.
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1032].panicDescription
   (powtórzenie elementu 388 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
395. [Poczytalność i Panika [1034] — nazwa Paniki] 책임의 무게
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1034].panicName
   limit: do 40 znaków
   EN: Burden of Responsibility
   PL: Brzemię Odpowiedzialności
396. [Poczytalność i Panika [1034] — efekt niskiego morale] - [Enhancement] 2, [Vulnerable] 1 얻음, 속도 최댓값 2 증가\n- 체력 회복량 30% 증가\n- 턴 종료 시 턴 시작 시보다 [RegainedStrength]의 수치가 낮으면 다음 턴에 [AttackUp] 2, [DefenseDown] 2 얻음
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1034].lowMoraleDescription
   limit: do 290 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Vulnerable], [RegainedStrength], [AttackUp], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: - Gain 2 [Enhancement] and 1 [Vulnerable]; raise Max Speed value by 2\n- Heal +30% more HP when healing\n- Turn End: if the [RegainedStrength] is lower than its value at Turn Start, gain 2 [AttackUp] and [DefenseDown] next turn
   PL: - Zyskaj 2 [Enhancement] i 1 [Vulnerable]; Maks. Szybkość +2\n- Skuteczność leczenia PŻ +30%\n- Koniec Tury: jeśli wartość [RegainedStrength] jest niższa niż na Początku Tury, zyskaj 2 [AttackUp] i 2 [DefenseDown] w następnej turze
397. [Poczytalność i Panika [1034] — efekt Paniki] - [Enhancement] 2, 속도 최댓값 2 증가\n- 체력 회복량 50% 증가\n- 턴 종료 시 턴 시작 시보다 [RegainedStrength]의 수치가 낮으면 다음 턴에 [AttackUp] 3, [DefenseDown] 5 얻음
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1034].panicDescription
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [RegainedStrength], [AttackUp], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [RegainedStrength] = 다시 도는 피의 충동 / Returning Bloodlust; [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: - Gain 2 [Enhancement] and raise Max Speed value by 2\n- Heal +50% more HP when healing\n- Turn End: if the [RegainedStrength] is lower than its value at Turn Start, gain 3 [AttackUp] and 5 [DefenseDown] next turn
   PL: - Zyskaj 2 [Enhancement]; Maks. Szybkość +2\n- Skuteczność leczenia PŻ +50%\n- Koniec Tury: jeśli wartość [RegainedStrength] jest niższa niż na Początku Tury, zyskaj 3 [AttackUp] i 5 [DefenseDown] w następnej turze
398. [Poczytalność i Panika [1033] — nazwa Paniki] 깨어나는 살육의 고양감
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1033].panicName
   limit: do 40 znaków
   EN: Reawakening Joy Of Carnage
   PL: Przebudzona Euforia Rzezi
399. [Poczytalność i Panika [1033] — efekt niskiego morale] 매 턴 시작 시, [AttackUp] 2 얻음. 정신력 효율 +2
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1033].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Every Turn Start: gain 2 [AttackUp]; +2 SP Efficiency
   PL: Co Początek Tury: zyskaj 2 [AttackUp]; skuteczność SP +2
400. [Poczytalność i Panika [1033] — efekt Paniki] 턴 시작 시, [DefenseUp] 6 얻음. 다음 턴에 [AttackUp] 3 얻음
   źródło: PanicInfo-a1c7p3.json :: dataList[id=1033].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp], [AttackUp]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: gain 6 [DefenseUp], and gain 3 [AttackUp] next turn
   PL: Początek Tury: zyskaj 6 [DefenseUp] oraz 3 [AttackUp] w następnej turze

## Poczytalność i Panika: PanicInfo-a1c8p1
- plik gry: `PanicInfo-a1c8p1.json`

401. [Poczytalność i Panika [1040] — nazwa Paniki] 박도
   źródło: PanicInfo-a1c8p1.json :: dataList[id=1040].panicName
   limit: do 40 znaków
   EN: Podao
   PL: Podao
402. [Poczytalność i Panika [1040] — efekt niskiego morale] 일방 공격에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: PanicInfo-a1c8p1.json :: dataList[id=1040].lowMoraleDescription
   limit: do 120 znaków
   EN: Take +10% damage from Unopposed Attacks; deal +30% damage with Counterattacks
   PL: Otrzymywane obrażenia od Ataków Jednostronnych +10%; obrażenia Kontrataków +30%
403. [Poczytalność i Panika [1040] — efekt Paniki] 일방 공격에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: PanicInfo-a1c8p1.json :: dataList[id=1040].panicDescription
   limit: do 120 znaków
   EN: Take +20% damage from Unopposed Attacks; deal +50% damage with Counterattacks
   PL: Otrzymywane obrażenia od Ataków Jednostronnych +20%; obrażenia Kontrataków +50%

## Poczytalność i Panika: PanicInfo-a1c8p2
- plik gry: `PanicInfo-a1c8p2.json`

404. [Poczytalność i Panika [1043] — nazwa Paniki] 고목화
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1043].panicName
   limit: do 40 znaków
   EN: Eldtree Mutation
   PL: Przemiana w Stare Drzewo
405. [Poczytalność i Panika [1043] — efekt niskiego morale] [AttackDmgUp] 1, [Vulnerable] 1, [BurstVulnerable] 1 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1043].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable], [BurstVulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile; [BurstVulnerable] = 파열 취약 / Rupture Fragility
   EN: Gain 1 [AttackDmgUp], 1 [Vulnerable], and 1 [BurstVulnerable]
   PL: Zyskaj 1 [AttackDmgUp], 1 [Vulnerable] oraz 1 [BurstVulnerable]
406. [Poczytalność i Panika [1043] — efekt Paniki] [AttackDmgUp] 2, [Vulnerable] 2, [BurstVulnerable] 2 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1043].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable], [BurstVulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile; [BurstVulnerable] = 파열 취약 / Rupture Fragility
   EN: Gain 2 [AttackDmgUp], 2 [Vulnerable], and 2 [BurstVulnerable]
   PL: Zyskaj 2 [AttackDmgUp], 2 [Vulnerable] oraz 2 [BurstVulnerable]
407. [Poczytalność i Panika [1044] — nazwa Paniki] 사심
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1044].panicName
   limit: do 40 znaków
   EN: Heart of Evil
   PL: Złe Zamiary
408. [Poczytalność i Panika [1044] — efekt niskiego morale] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 [AttackDmgUp] 2, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1044].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +2 against targets with [OminousTalisman]\nTurn Start: gain 2 [AttackDmgUp] and 1 [Vulnerable]
   PL: Moc Starcia +2 przeciw celom z [OminousTalisman]\nPoczątek Tury: zyskaj 2 [AttackDmgUp] i 1 [Vulnerable]
409. [Poczytalność i Panika [1044] — efekt Paniki] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 [AttackDmgUp] 3, [Vulnerable] 2 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1044].panicDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +3 against targets with [OminousTalisman]\nTurn Start: gain 3 [AttackDmgUp] and 2 [Vulnerable]
   PL: Moc Starcia +3 przeciw celom z [OminousTalisman]\nPoczątek Tury: zyskaj 3 [AttackDmgUp] i 2 [Vulnerable]
410. [Poczytalność i Panika [1045] — nazwa Paniki] 짙은 사심
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1045].panicName
   limit: do 40 znaków
   EN: Heart of Oppressive Evil
   PL: Mroczne Zamiary
411. [Poczytalność i Panika [1045] — efekt niskiego morale] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 [AttackDmgUp] 3, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1045].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +2 against targets with [OminousTalisman]\nTurn Start: gain 3 [AttackDmgUp] and 1 [Vulnerable]
   PL: Moc Starcia +2 przeciw celom z [OminousTalisman]\nPoczątek Tury: zyskaj 3 [AttackDmgUp] i 1 [Vulnerable]
412. [Poczytalność i Panika [1045] — efekt Paniki] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 [AttackDmgUp] 4, [Vulnerable] 2 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1045].panicDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [OminousTalisman], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [OminousTalisman] = 불길한 부적 / Omen Talisman; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +3 against targets with [OminousTalisman]\nTurn Start: gain 4 [AttackDmgUp] and 2 [Vulnerable]
   PL: Moc Starcia +3 przeciw celom z [OminousTalisman]\nPoczątek Tury: zyskaj 4 [AttackDmgUp] i 2 [Vulnerable]
413. [Poczytalność i Panika [1047] — nazwa Paniki] 가치우
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1047].panicName
   limit: do 40 znaków
   EN: Jia Qiu
   PL: Jia Qiu
414. [Poczytalność i Panika [1047] — efekt niskiego morale] 홍루를 제외한 대상에게 가하는 피해량 +10%
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1047].lowMoraleDescription
   limit: do 120 znaków
   EN: Deal +10% damage against targets that aren't Hong Lu
   PL: Zadawane obrażenia +10% celom innym niż Hong Lu
415. [Poczytalność i Panika [1047] — efekt Paniki] 홍루를 제외한 대상에게 가하는 피해량 +20%
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1047].panicDescription
   limit: do 120 znaków
   EN: Deal +20% damage against targets that aren't Hong Lu
   PL: Zadawane obrażenia +20% celom innym niż Hong Lu
416. [Poczytalność i Panika [1042] — nazwa Paniki] 충전 회로 역류
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1042].panicName
   limit: do 50 znaków
   EN: Charge Circuitry Countercurrent
   PL: Prąd Wsteczny Obwodu Ładunku
417. [Poczytalność i Panika [1042] — efekt niskiego morale] [Burst]을 보유한 대상과 합 진행 시, [Charge] 횟수 3, [Vulnerable] 1 얻음 (턴 당 2회)
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1042].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Burst], [Charge], [Vulnerable]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge; [Vulnerable] = 취약 / Fragile
   EN: When Clashing against targets with [Burst], gain +3 [Charge] Count and 1 [Vulnerable] (2 times per turn)
   PL: W Starciu z celami mającymi [Burst]: zyskaj +3 Licznika [Charge] i 1 [Vulnerable] (2 razy na turę)
418. [Poczytalność i Panika [1042] — efekt Paniki] [Burst]을 보유한 대상과 합 진행 시, [Charge] 횟수 5, [AttackDmgUp] 1, [Vulnerable] 2 얻음 (턴 당 2회)
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1042].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Burst], [Charge], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [Burst] = 파열 / Rupture; [Charge] = 충전 / Charge; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: When Clashing against targets with [Burst], gain +5 [Charge] Count, 1 [AttackDmgUp], and 2 [Vulnerable] (2 times per turn)
   PL: W Starciu z celami mającymi [Burst]: zyskaj +5 Licznika [Charge], 1 [AttackDmgUp] i 2 [Vulnerable] (2 razy na turę)
419. [Poczytalność i Panika [9995] — nazwa Paniki] 숨 돌리기
   źródło: PanicInfo-a1c8p2.json :: dataList[id=9995].panicName
   limit: do 40 znaków
   EN: Catching Breath
   PL: Złapanie Oddechu
420. [Poczytalność i Panika [9995] — efekt niskiego morale] 턴 시작시 [DefenseUp] 2를 얻고 [Breath] 위력 2 감소
   źródło: PanicInfo-a1c8p2.json :: dataList[id=9995].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp], [Breath]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Breath] = 호흡 / Poise
   EN: Turn Start: gain 2 [DefenseUp] and lose 2 [Breath] Potency
   PL: Początek Tury: zyskaj 2 [DefenseUp] i trać 2 Siły [Breath]
421. [Poczytalność i Panika [9995] — efekt Paniki] 턴 시작시 [DefenseUp] 5를 얻고 [Breath] 위력 5 감소
   źródło: PanicInfo-a1c8p2.json :: dataList[id=9995].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [DefenseUp], [Breath]
   znaczenie tagów: [DefenseUp] = 방어 레벨 증가 / Defense Level Up; [Breath] = 호흡 / Poise
   EN: Turn Start: gain 5 [DefenseUp] and lose 5 [Breath] Potency
   PL: Początek Tury: zyskaj 5 [DefenseUp] i trać 5 Siły [Breath]
422. [Poczytalność i Panika [1055] — nazwa Paniki] 양날깃
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1055].panicName
   limit: do 40 znaków
   EN: Double-edged Feather
   PL: Obosieczne Pióro
423. [Poczytalność i Panika [1055] — efekt niskiego morale] 턴 시작시 취약 1, 체력 회복 증가 1 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1055].lowMoraleDescription
   limit: do 120 znaków
   EN: Turn Start: gain 1 Fragile and 1 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: Początek Tury: zyskaj 1 Wrażliwości i 1 Wzmocnienia Leczenia PŻ. Przy Trafieniu: nałóż 1 Rozdarcia i 1 Krwawienia
424. [Poczytalność i Panika [1055] — efekt Paniki] 턴 시작시 취약 2, 체력 회복 증가 2 얻음. 자신의 공격 적중시 파열 1, 출혈 1 부여
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1055].panicDescription
   limit: do 120 znaków
   EN: Turn Start: gain 2 Fragile and 2 HP Healing Boost. On Hit, inflict 1 Rupture and 1 Bleed
   PL: Początek Tury: zyskaj 2 Wrażliwości i 2 Wzmocnienia Leczenia PŻ. Przy Trafieniu: nałóż 1 Rozdarcia i 1 Krwawienia
425. [Poczytalność i Panika [1056] — nazwa Paniki] 울분
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1056].panicName
   limit: do 40 znaków
   EN: Angst
   PL: Rozgoryczenie
426. [Poczytalność i Panika [1056] — efekt niskiego morale] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +2\n턴 시작 시 [AttackDmgUp] 2, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1056].lowMoraleDescription
   (powtórzenie elementu 408 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
427. [Poczytalność i Panika [1056] — efekt Paniki] [OminousTalisman]을 보유한 대상과 합 진행 시, 합 위력 +3\n턴 시작 시 [AttackDmgUp] 3, [Vulnerable] 2 얻음
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1056].panicDescription
   (powtórzenie elementu 409 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
428. [Poczytalność i Panika [1058] — nazwa Paniki] 돌격 지시
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1058].panicName
   limit: do 40 znaków
   EN: Charge Order
   PL: Rozkaz Szturmu
429. [Poczytalność i Panika [1058] — efekt niskiego morale] 턴 시작시 [Vulnerable] 1을 얻고, 모든 아군에게 [AttackDmgUp] 1 부여
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1058].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 1 [Vulnerable] and apply 1 [AttackDmgUp] to all allies
   PL: Początek Tury: zyskaj 1 [Vulnerable] i nałóż 1 [AttackDmgUp] na wszystkich sojuszników
430. [Poczytalność i Panika [1058] — efekt Paniki] 턴 시작시 [Vulnerable] 2를 얻고, 모든 아군에게 [AttackDmgUp] 2 부여
   źródło: PanicInfo-a1c8p2.json :: dataList[id=1058].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 2 [Vulnerable] and apply 2 [AttackDmgUp] to all allies
   PL: Początek Tury: zyskaj 2 [Vulnerable] i nałóż 2 [AttackDmgUp] na wszystkich sojuszników

## Poczytalność i Panika: PanicInfo-a1c8p3
- plik gry: `PanicInfo-a1c8p3.json`

431. [Poczytalność i Panika [1049] — nazwa Paniki] 맹수의 본능
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1049].panicName
   limit: do 40 znaków
   EN: Beastly Instinct
   PL: Instynkt Bestii
432. [Poczytalność i Panika [1049] — efekt niskiego morale] 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이/2)%만큼 증가 (최대 10%)\n턴 시작 시, [Enhancement] 1, [AttackDmgUp] 1, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1049].lowMoraleDescription
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Deals +(HP percentage difference / 2)% damage to targets with higher HP percentages that this unit's (max 10%)\nTurn Start: gain 1 [Enhancement], 1 [AttackDmgUp], and 1 [Vulnerable]
   PL: Zadaje +(różnica % PŻ / 2)% obrażeń celom o wyższym % PŻ niż ta jednostka (maks. 10%)\nPoczątek Tury: zyskaj 1 [Enhancement], 1 [AttackDmgUp] i 1 [Vulnerable]
433. [Poczytalność i Panika [1049] — efekt Paniki] 자신보다 남은 체력 비율이 더 높은 대상에게 입히는 피해량이 (체력 비율 차이)%만큼 증가 (최대 25%)\n턴 시작 시, [PlusCoinValueUp] 1, [AttackDmgUp] 2, [Vulnerable] 2 얻음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1049].panicDescription
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [PlusCoinValueUp], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [PlusCoinValueUp] = 더하기 코인 강화 / Plus Coin Boost; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Deals +(HP percentage difference)% damage to targets with higher HP percentages that this unit's (max 25%)\nTurn Start: gain 1 [PlusCoinValueUp], 2 [AttackDmgUp], and 2 [Vulnerable]
   PL: Zadaje +(różnica % PŻ)% obrażeń celom o wyższym % PŻ niż ta jednostka (maks. 25%)\nPoczątek Tury: zyskaj 1 [PlusCoinValueUp], 2 [AttackDmgUp] i 2 [Vulnerable]
434. [Poczytalność i Panika [1046] — nazwa Paniki] 살점 주걱
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1046].panicName
   limit: do 40 znaków
   EN: Flesh Scoop
   PL: Czerpak Mięsa
435. [Poczytalność i Panika [1046] — efekt niskiego morale] 턴 시작시 [Laceration] 5 획득, [Enhancement] 1 얻음.
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1046].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Enhancement]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: gain 5 [Laceration] and 1 [Enhancement].
   PL: Początek Tury: zyskaj 5 [Laceration] i 1 [Enhancement].
436. [Poczytalność i Panika [1046] — efekt Paniki] 턴 시작시 [Laceration] 10 획득, [Enhancement] 2 얻음.
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1046].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Laceration], [Enhancement]
   znaczenie tagów: [Laceration] = 출혈 / Bleed; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn Start: gain 10 [Laceration] and 2 [Enhancement].
   PL: Początek Tury: zyskaj 10 [Laceration] i 2 [Enhancement].
437. [Poczytalność i Panika [1050] — nazwa Paniki] 규율
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1050].panicName
   limit: do 40 znaków
   EN: Le Regole
   PL: Le Regole
438. [Poczytalność i Panika [1050] — efekt niskiego morale] 전 턴에 [Vibration]을 2 이상 부여 했다면, [AmberDamageUp] 1 획득,\n전 턴에 [Combustion]을 2 이상 부여 했다면, [CrimsonDamageUp] 1 획득,\n아무것도 부여하지 못했으면, [DefenseDown] 2 얻음.
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1050].lowMoraleDescription
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [AmberDamageUp], [Combustion], [CrimsonDamageUp], [DefenseDown]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [AmberDamageUp] = 나태 피해량 증가 / Sloth DMG Up; [Combustion] = 화상 / Burn; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: If this unit inflicted 2+ [Vibration] last turn, gain 1 [AmberDamageUp]\nIf this unit inflicted 2+ [Combustion] last turn, gain 1 [CrimsonDamageUp]\nIf this unit failed to inflict anything, gain 2 [DefenseDown]
   PL: Jeśli w poprzedniej turze nałożono 2+ [Vibration]: zyskaj 1 [AmberDamageUp]\nJeśli w poprzedniej turze nałożono 2+ [Combustion]: zyskaj 1 [CrimsonDamageUp]\nJeśli nie nałożono żadnego z nich: zyskaj 2 [DefenseDown]
439. [Poczytalność i Panika [1050] — efekt Paniki] 전 턴에 [Vibration]을 2 이상 부여 했다면, [AmberDamageUp] 2 획득,\n전 턴에 [Combustion]을 2 이상 부여 했다면, [CrimsonDamageUp] 2 획득,\n아무것도 부여하지 못했으면, [DefenseDown] 3 얻음.
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1050].panicDescription
   limit: do 270 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration], [AmberDamageUp], [Combustion], [CrimsonDamageUp], [DefenseDown]
   znaczenie tagów: [Vibration] = 진동 / Tremor; [AmberDamageUp] = 나태 피해량 증가 / Sloth DMG Up; [Combustion] = 화상 / Burn; [CrimsonDamageUp] = 분노 피해량 증가 / Wrath DMG Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: If this unit inflicted 2+ [Vibration] last turn, gain 2 [AmberDamageUp]\nIf this unit inflicted 2+ [Combustion] last turn, gain 2 [CrimsonDamageUp]\nIf this unit failed to inflict anything, gain 3 [DefenseDown]
   PL: Jeśli w poprzedniej turze nałożono 2+ [Vibration]: zyskaj 2 [AmberDamageUp]\nJeśli w poprzedniej turze nałożono 2+ [Combustion]: zyskaj 2 [CrimsonDamageUp]\nJeśli nie nałożono żadnego z nich: zyskaj 3 [DefenseDown]
440. [Poczytalność i Panika [1051] — nazwa Paniki] 여린 금으로 주조한 마음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1051].panicName
   limit: do 40 znaków
   EN: Soft Goldcasted Heart
   PL: Serce Odlane z Miękkiego Złota
441. [Poczytalność i Panika [1051] — efekt niskiego morale] 턴 시작시 [Enhancement] 1, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1051].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 1 [Enhancement] and 1 [Vulnerable]
   PL: Początek Tury: zyskaj 1 [Enhancement] i 1 [Vulnerable]
442. [Poczytalność i Panika [1051] — efekt Paniki] 턴 시작시 [Enhancement] 2, [Vulnerable] 2 얻음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1051].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 2 [Enhancement] and 2 [Vulnerable]
   PL: Początek Tury: zyskaj 2 [Enhancement] i 2 [Vulnerable]
443. [Poczytalność i Panika [1052] — nazwa Paniki] 새 시대로 향하는 마음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1052].panicName
   limit: do 40 znaków
   EN: Heart Toward the New Era
   PL: Serce ku Nowej Erze
444. [Poczytalność i Panika [1052] — efekt niskiego morale] 공격 적중시 자신의 정신력 3 소모, [Sinking] 2 부여
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1052].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: On Hit, consume 3 SP on self to inflict 2 [Sinking]
   PL: Przy Trafieniu: zużyj 3 własne SP i nałóż 2 [Sinking]
445. [Poczytalność i Panika [1052] — efekt Paniki] 공격 적중시 [Sinking] 3 부여, [Sinking] 1 얻음
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1052].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Sinking]
   znaczenie tagów: [Sinking] = 침잠 / Sinking
   EN: On Hit, inflict 3 [Sinking] and gain 1 [Sinking]
   PL: Przy Trafieniu: nałóż 3 [Sinking] i zyskaj 1 [Sinking]
446. [Poczytalność i Panika [1053] — nazwa Paniki] 계승된 홍원의 뜻
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1053].panicName
   limit: do 40 znaków
   EN: Inherited Will of Hongyuan
   PL: Odziedziczona Wola Hongyuanu
447. [Poczytalność i Panika [1053] — efekt niskiego morale] 모든 부위가 [Enhancement] 2, [Binding] 1 얻음\n홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 [AttackDmgUp] 1, [Vulnerable] 1 얻음 (턴 당 1회)
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1053].lowMoraleDescription
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Binding], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Binding] = 속박 / Bind; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: All Parts gain 2 [Enhancement] and 1 [Binding]\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 1 [AttackDmgUp] and 1 [Vulnerable] next turn (once per turn)
   PL: Wszystkie Części zyskują 2 [Enhancement] i 1 [Binding]\n- Gdy Korpus przegra Starcie z Hong Lu: w następnej turze Korpus zyskuje 1 [AttackDmgUp] i 1 [Vulnerable] (raz na turę)
448. [Poczytalność i Panika [1053] — efekt Paniki] 모든 부위가 [Enhancement] 2, [Binding] 2 얻음\n홍루에게 몸통 부위가 합 패배 시 다음 턴에 몸통 부위가 [AttackDmgUp] 2, [Vulnerable] 2 얻음 (턴 당 1회)
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1053].panicDescription
   limit: do 230 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Binding], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Binding] = 속박 / Bind; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: All Parts gain 2 [Enhancement] and 2 [Binding]\n- When the Body Part loses a Clash against Hong Lu: the Body Part gains 2 [AttackDmgUp] and 2 [Vulnerable] next turn (once per turn)
   PL: Wszystkie Części zyskują 2 [Enhancement] i 2 [Binding]\n- Gdy Korpus przegra Starcie z Hong Lu: w następnej turze Korpus zyskuje 2 [AttackDmgUp] i 2 [Vulnerable] (raz na turę)
449. [Poczytalność i Panika [1054] — nazwa Paniki] 유구히 계승될 홍원의 뜻
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1054].panicName
   limit: do 60 znaków
   EN: Infinitely Bequeathing Will of Hongyuan
   PL: Odwiecznie Przekazywana Wola Hongyuanu
450. [Poczytalność i Panika [1054] — efekt niskiego morale] [Enhancement] 2, [Vulnerable] 1 얻음\n자신이 생성한 유닛이 [DefenseDown] 3 얻음\n가하는 피해량 20% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 10% 감소
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1054].lowMoraleDescription
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Vulnerable], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Gain 2 [Enhancement] and 1 [Vulnerable]\nUnits generated by this unit gain 3 [DefenseDown]\nDeal +20% damage. If the Palanquin Part's HP drops to 0, deal -10% damage instead
   PL: Zyskaj 2 [Enhancement] i 1 [Vulnerable]\nJednostki stworzone przez tę jednostkę zyskują 3 [DefenseDown]\nZadawane obrażenia +20%. Jeśli PŻ Lektyki spadną do 0, zamiast tego zadawane obrażenia -10%
451. [Poczytalność i Panika [1054] — efekt Paniki] [Enhancement] 2, [Vulnerable] 2 얻음\n자신이 생성한 유닛이 [DefenseDown] 6 얻음\n가하는 피해량 30% 증가. 가마 부위의 체력이 0이면, 대신 가하는 피해량 15% 감소
   źródło: PanicInfo-a1c8p3.json :: dataList[id=1054].panicDescription
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Vulnerable], [DefenseDown]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Gain 2 [Enhancement] and 2 [Vulnerable]\nUnits generated by this unit gain 6 [DefenseDown]\nDeal +30% damage. If the Palanquin Part's HP drops to 0, deal -15% damage instead
   PL: Zyskaj 2 [Enhancement] i 2 [Vulnerable]\nJednostki stworzone przez tę jednostkę zyskują 6 [DefenseDown]\nZadawane obrażenia +30%. Jeśli PŻ Lektyki spadną do 0, zamiast tego zadawane obrażenia -15%

## Poczytalność i Panika: PanicInfo-a1c9116
- plik gry: `PanicInfo-a1c9116.json`

452. [Poczytalność i Panika [1038] — nazwa Paniki] 뒷골목의 밤
   źródło: PanicInfo-a1c9116.json :: dataList[id=1038].panicName
   limit: do 40 znaków
   EN: Night in the Backstreets
   PL: Noc w Zaułkach
453. [Poczytalność i Panika [1038] — efekt niskiego morale] 턴 시작시 [Enhancement] 1, [TakeHpHealIncrease] 1, [Vulnerable] 1을 얻음
   źródło: PanicInfo-a1c9116.json :: dataList[id=1038].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [TakeHpHealIncrease], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 1 [Enhancement], 1 [TakeHpHealIncrease], and 1 [Vulnerable]
   PL: Początek Tury: zyskaj 1 [Enhancement], 1 [TakeHpHealIncrease] i 1 [Vulnerable]
454. [Poczytalność i Panika [1038] — efekt Paniki] 턴 시작시 [Enhancement] 2, [TakeHpHealIncrease] 2, [Vulnerable] 1을 얻음
   źródło: PanicInfo-a1c9116.json :: dataList[id=1038].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [TakeHpHealIncrease], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [TakeHpHealIncrease] = 체력 회복 증가 / HP Healing Boost; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 2 [Enhancement], 2 [TakeHpHealIncrease], and 1 [Vulnerable]
   PL: Początek Tury: zyskaj 2 [Enhancement], 2 [TakeHpHealIncrease] i 1 [Vulnerable]
455. [Poczytalność i Panika [1039] — nazwa Paniki] 암수
   źródło: PanicInfo-a1c9116.json :: dataList[id=1039].panicName
   limit: do 40 znaków
   EN: Deception
   PL: Podstęp
456. [Poczytalność i Panika [1039] — efekt niskiego morale] 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +10%
   źródło: PanicInfo-a1c9116.json :: dataList[id=1039].lowMoraleDescription
   limit: do 160 znaków
   EN: If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +10% damage against the target
   PL: Jeśli Szybkość tej jednostki jest wyższa od celu lub przy Ataku Jednostronnym: obrażenia przeciw celowi +10%
457. [Poczytalność i Panika [1039] — efekt Paniki] 자신의 속도가 대상보다 빠르거나 일방 공격을 할 경우, 대상에게 피해량 +20%, 자신의 속도가 대상보다 빠르면, 받는 피해량 -20%
   źródło: PanicInfo-a1c9116.json :: dataList[id=1039].panicDescription
   limit: do 240 znaków
   EN: If this unit's Speed is faster than the target's or when using an Unopposed Attack, deal +20% damage against the target; if this unit's Speed is faster than the target's, take -20% damage
   PL: Jeśli Szybkość tej jednostki jest wyższa od celu lub przy Ataku Jednostronnym: obrażenia przeciw celowi +20%; jeśli Szybkość jest wyższa od celu: otrzymywane obrażenia -20%

## Poczytalność i Panika: PanicInfo-a1c971
- plik gry: `PanicInfo-a1c971.json`

458. [Poczytalność i Panika [1036] — nazwa Paniki] 고뇌
   źródło: PanicInfo-a1c971.json :: dataList[id=1036].panicName
   limit: do 40 znaków
   EN: Anguish
   PL: Udręka
459. [Poczytalność i Panika [1036] — efekt niskiego morale] 턴 시작 시, [Vulnerable] 1, [MentalIncreaseDown] 2 얻음
   źródło: PanicInfo-a1c971.json :: dataList[id=1036].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [MentalIncreaseDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Turn Start: gain 1 [Vulnerable] and 2 [MentalIncreaseDown]
   PL: Początek Tury: zyskaj 1 [Vulnerable] i 2 [MentalIncreaseDown]
460. [Poczytalność i Panika [1036] — efekt Paniki] 턴 시작 시, [Vulnerable] 2, [MentalIncreaseDown] 3 얻음.
   źródło: PanicInfo-a1c971.json :: dataList[id=1036].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [MentalIncreaseDown]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Turn Start: gain 2 [Vulnerable] and 3 [MentalIncreaseDown]
   PL: Początek Tury: zyskaj 2 [Vulnerable] i 3 [MentalIncreaseDown].

## Poczytalność i Panika: PanicInfo-a1c9p1
- plik gry: `PanicInfo-a1c9p1.json`

461. [Poczytalność i Panika [1067] — nazwa Paniki] 흐트러진 숨
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1067].panicName
   limit: do 40 znaków
   EN: Ragged Breath
   PL: Rwany Oddech
462. [Poczytalność i Panika [1067] — efekt niskiego morale] 턴 시작시 자신의 [Breath] 위력 3 감소
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1067].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn Start: Lose 3 [Breath] Potency
   PL: Początek Tury: trać 3 Siły [Breath]
463. [Poczytalność i Panika [1067] — efekt Paniki] 턴 시작시 자신의 [Breath] 위력 5 감소
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1067].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Breath]
   znaczenie tagów: [Breath] = 호흡 / Poise
   EN: Turn Start: Lose 5 [Breath] Potency
   PL: Początek Tury: trać 5 Siły [Breath]
464. [Poczytalność i Panika [1068] — nazwa Paniki] 교본
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1068].panicName
   limit: do 40 znaków
   EN: Textbook
   PL: Podręcznik
465. [Poczytalność i Panika [1068] — efekt niskiego morale] [DuelEdge]를 보유한 적과 합 진행 시 합 위력 +1\n합 패배 시 다음 턴 [Vulnerable] 1 얻음 (턴당 1회)
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1068].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge], [Vulnerable]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +1 when Clashing against targets with [DuelEdge]\nClash Lose: Gain 1 [Vulnerable] next turn (once per turn)
   PL: Moc Starcia +1 przeciw celom z [DuelEdge]\nPrzegrane Starcie: zyskaj 1 [Vulnerable] w następnej turze (raz na turę)
466. [Poczytalność i Panika [1068] — efekt Paniki] [DuelEdge]를 보유한 적과 합 진행 시 합 위력 +2\n합 패배 시 다음 턴 [Vulnerable] 2 얻음 (턴당 1회)
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1068].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [DuelEdge], [Vulnerable]
   znaczenie tagów: [DuelEdge] = 결투 고조 / The Duel Escalates; [Vulnerable] = 취약 / Fragile
   EN: Clash Power +2 when Clashing against targets with [DuelEdge]\nClash Lose: Gain 2 [Vulnerable] next turn (once per turn)
   PL: Moc Starcia +2 przeciw celom z [DuelEdge]\nPrzegrane Starcie: zyskaj 2 [Vulnerable] w następnej turze (raz na turę)
467. [Poczytalność i Panika [1069] — nazwa Paniki] 아이언 메이든
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1069].panicName
   limit: do 40 znaków
   EN: Iron Maiden
   PL: Żelazna Dziewica
468. [Poczytalność i Panika [1069] — efekt niskiego morale] 턴 시작 시, [AttackDown] 1, [DefenseUp] 1 얻음
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1069].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown], [DefenseUp]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: gain 1 [AttackDown] and 1 [DefenseUp]
   PL: Początek Tury: zyskaj 1 [AttackDown] i 1 [DefenseUp]
469. [Poczytalność i Panika [1069] — efekt Paniki] 턴 시작 시, [AttackDown] 2, [DefenseUp] 2 얻음
   źródło: PanicInfo-a1c9p1.json :: dataList[id=1069].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDown], [DefenseUp]
   znaczenie tagów: [AttackDown] = 공격 레벨 감소 / Offense Level Down; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Turn Start: gain 2 [AttackDown] and 2 [DefenseUp]
   PL: Początek Tury: zyskaj 2 [AttackDown] i 2 [DefenseUp]

## Poczytalność i Panika: PanicInfo-a1c9p2
- plik gry: `PanicInfo-a1c9p2.json`

470. [Poczytalność i Panika [1070] — nazwa Paniki] 애증
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1070].panicName
   limit: do 40 znaków
   EN: Affection and Resentment
   PL: Miłość i Urąganie
471. [Poczytalność i Panika [1070] — efekt niskiego morale] 료슈에게 가하는 피해량과 받는 피해량 +10%
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1070].lowMoraleDescription
   limit: do 120 znaków
   EN: Deal +10% damage to and take +10% damage from Ryōshū
   PL: Zadawane obrażenia przeciw Ryōshū oraz otrzymywane od niej obrażenia +10%
472. [Poczytalność i Panika [1070] — efekt Paniki] 료슈에게 가하는 피해량과 받는 피해량 +20%
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1070].panicDescription
   limit: do 120 znaków
   EN: Deal +20% damage to and take +20% damage from Ryōshū
   PL: Zadawane obrażenia przeciw Ryōshū oraz otrzymywane od niej obrażenia +20%
473. [Poczytalność i Panika [1074] — nazwa Paniki] 언짢음
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1074].panicName
   limit: do 40 znaków
   EN: Vexation
   PL: Irytacja
474. [Poczytalność i Panika [1074] — efekt niskiego morale] [PenetrateResultUp] 1, [MentalIncreaseDown] 1 얻음
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1074].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateResultUp], [MentalIncreaseDown]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Gain 1 [PenetrateResultUp] and 1 [MentalIncreaseDown]
   PL: Zyskaj 1 [PenetrateResultUp] i 1 [MentalIncreaseDown]
475. [Poczytalność i Panika [1074] — efekt Paniki] [PenetrateResultUp] 2, [PenetrateDamageUp] 1, [MentalIncreaseDown] 2 얻음
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1074].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [PenetrateResultUp], [PenetrateDamageUp], [MentalIncreaseDown]
   znaczenie tagów: [PenetrateResultUp] = 관통 위력 증가 / Pierce Power Up; [PenetrateDamageUp] = 관통 피해량 증가 / Pierce DMG Up; [MentalIncreaseDown] = 정신력 회복 효율 감소 / SP Heal Efficiency Down
   EN: Gain 2 [PenetrateResultUp], 1 [PenetrateDamageUp], and 2 [MentalIncreaseDown]
   PL: Zyskaj 2 [PenetrateResultUp], 1 [PenetrateDamageUp] i 2 [MentalIncreaseDown]
476. [Poczytalność i Panika [1072] — nazwa Paniki] 지령 붕괴 위기
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1072].panicName
   limit: do 40 znaków
   EN: Prescript Incompliance Risk
   PL: Ryzyko Złamania Nakazu
477. [Poczytalność i Panika [1072] — efekt niskiego morale] [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +20%\n[IndexPrescriptTargetToPersonality]이 아닌 대상에게 받는 피해량 +10%
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1072].lowMoraleDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index
   EN: Deal +20% damage to [IndexPrescriptTargetToPersonality]\nTake +10% damage from those who are not [IndexPrescriptTargetToPersonality]
   PL: Zadawane obrażenia celowi [IndexPrescriptTargetToPersonality] +20%\nOtrzymywane obrażenia od celów niebędących [IndexPrescriptTargetToPersonality] +10%
478. [Poczytalność i Panika [1072] — efekt Paniki] [IndexPrescriptTargetToPersonality]에게 가하는 피해량 +30%\n[IndexPrescriptTargetToPersonality]이 아닌 대상에게 받는 피해량 +20%
   źródło: PanicInfo-a1c9p2.json :: dataList[id=1072].panicDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: \n, [IndexPrescriptTargetToPersonality]
   znaczenie tagów: [IndexPrescriptTargetToPersonality] = 검지의 지령 대상 / The Prescript's Target - The Index
   EN: Deal +30% damage to [IndexPrescriptTargetToPersonality]\nTake +20% damage from those who are not [IndexPrescriptTargetToPersonality]
   PL: Zadawane obrażenia celowi [IndexPrescriptTargetToPersonality] +30%\nOtrzymywane obrażenia od celów niebędących [IndexPrescriptTargetToPersonality] +20%

## Poczytalność i Panika: PanicInfo-a1c9p3
- plik gry: `PanicInfo-a1c9p3.json`

479. [Poczytalność i Panika [1071] — nazwa Paniki] 열화침식
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1071].panicName
   limit: do 40 znaków
   EN: Degraded Corrosion
   PL: Zdegradowana Korozja
480. [Poczytalność i Panika [1071] — efekt niskiego morale] 턴 시작 시 [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1071].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [Vulnerable]
   PL: Początek Tury: zyskaj 1 [Vulnerable]
481. [Poczytalność i Panika [1071] — efekt Paniki] 턴 시작 시 [Vulnerable] 1, [Combustion] 5 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1071].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Combustion]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Combustion] = 화상 / Burn
   EN: Turn Start: Gain 1 [Vulnerable] and 5 [Combustion]
   PL: Początek Tury: zyskaj 1 [Vulnerable] i 5 [Combustion]
482. [Poczytalność i Panika [1073] — nazwa Paniki] 쏟아지는 잠
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1073].panicName
   limit: do 40 znaków
   EN: Wave of Somnolence
   PL: Fala Senności
483. [Poczytalność i Panika [1073] — efekt niskiego morale] 스킬로 얻는 [LanternHohenheimBigBird] 획득량 1 감소
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1073].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [LanternHohenheimBigBird]
   znaczenie tagów: [LanternHohenheimBigBird] = 램프 / Lamp
   EN: Gain 1 fewer [LanternHohenheimBigBird] from Skills
   PL: Zyskujesz o 1 mniej [LanternHohenheimBigBird] z umiejętności
484. [Poczytalność i Panika [1073] — efekt Paniki] 한 턴 동안 행동하지 않음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1073].panicDescription
   limit: do 120 znaków
   EN: Does not act for this turn
   PL: Nie wykonuje działań w tej turze
485. [Poczytalność i Panika [1078] — nazwa Paniki] 가문의 수치
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1078].panicName
   limit: do 40 znaków
   EN: Shame of the Family
   PL: Hańba Rodu
486. [Poczytalność i Panika [1078] — efekt niskiego morale] 턴 시작 시 [SlashDamageUp] 1, [ParryingResultUp] 1, [Vulnerable] 1 얻음\n스킬 사용 시 망을 얻을 수 없음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1078].lowMoraleDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp], [ParryingResultUp], [Vulnerable]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [SlashDamageUp], 1 [ParryingResultUp], and 1 [Vulnerable]\nCannot gain Mang when using Skills
   PL: Początek Tury: zyskaj 1 [SlashDamageUp], 1 [ParryingResultUp] i 1 [Vulnerable]\nNie może zyskać Mang przy użyciu umiejętności
487. [Poczytalność i Panika [1078] — efekt Paniki] 턴 시작 시 [SlashDamageUp] 2, [ParryingResultUp] 2, [Vulnerable] 2 얻음\n스킬 사용 시 망을 얻을 수 없음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1078].panicDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [SlashDamageUp], [ParryingResultUp], [Vulnerable]
   znaczenie tagów: [SlashDamageUp] = 참격 피해량 증가 / Slash DMG Up; [ParryingResultUp] = 합 위력 증가 / Clash Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [SlashDamageUp], 2 [ParryingResultUp], and 2 [Vulnerable]\nCannot gain Mang when using Skills
   PL: Początek Tury: zyskaj 2 [SlashDamageUp], 2 [ParryingResultUp] i 2 [Vulnerable]\nNie może zyskać Mang przy użyciu umiejętności
488. [Poczytalność i Panika [1079] — nazwa Paniki] ‘나, 날… 죽여줘..’
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1079].panicName
   limit: do 40 znaków
   EN: "K-kill... kill me..."
   PL: „Z-zabij… zabij mnie…”
489. [Poczytalność i Panika [1079] — efekt niskiego morale] 턴 시작 시 [ParryingResultDown] 8, [ResultReduction] 5 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1079].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ParryingResultDown], [ResultReduction]
   znaczenie tagów: [ParryingResultDown] = 합 위력 감소 / Clash Power Down; [ResultReduction] = 위력 감소 / Power Down
   EN: Turn Start: Gain 8 [ParryingResultDown] and 5 [ResultReduction]
   PL: Początek Tury: zyskaj 8 [ParryingResultDown] i 5 [ResultReduction]
490. [Poczytalność i Panika [1079] — efekt Paniki] 턴 시작 시 [ParryingResultDown] 10, [ResultReduction] 5 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1079].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [ParryingResultDown], [ResultReduction]
   znaczenie tagów: [ParryingResultDown] = 합 위력 감소 / Clash Power Down; [ResultReduction] = 위력 감소 / Power Down
   EN: Turn Start: Gain 10 [ParryingResultDown] and 5 [ResultReduction]
   PL: Początek Tury: zyskaj 10 [ParryingResultDown] i 5 [ResultReduction]
491. [Poczytalność i Panika [1077] — nazwa Paniki] 한물간 예술
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1077].panicName
   limit: do 40 znaków
   EN: Outmoded Art
   PL: Przestarzała Sztuka
492. [Poczytalność i Panika [1077] — efekt niskiego morale] 턴 시작 시, [AttackUp] 1 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1077].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: Gain 1 [AttackUp]
   PL: Początek Tury: zyskaj 1 [AttackUp]
493. [Poczytalność i Panika [1077] — efekt Paniki] 턴 시작 시, [AttackUp] 2 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1077].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up
   EN: Turn Start: Gain 2 [AttackUp]
   PL: Początek Tury: zyskaj 2 [AttackUp]
494. [Poczytalność i Panika [1075] — nazwa Paniki] 광분
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1075].panicName
   limit: do 40 znaków
   EN: Mad Rampage
   PL: Szaleńcza Furia
495. [Poczytalność i Panika [1075] — efekt niskiego morale] 턴 시작 시 [Enhancement] 2, [DefenseDown] 4를 얻고, 이전 턴에 받은 체력 피해량 30당 [AttackDmgUp] 1을 얻음 (최대 5)
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1075].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: Gain 2 [Enhancement] and 4 [DefenseDown]; gain 1 [AttackDmgUp] for every 30 HP damage taken last turn (max 5)
   PL: Początek Tury: zyskaj 2 [Enhancement] i 4 [DefenseDown]; zyskaj 1 [AttackDmgUp] za każde 30 obrażeń PŻ otrzymanych w poprzedniej turze (maks. 5)
496. [Poczytalność i Panika [1075] — efekt Paniki] 턴 시작 시 [Enhancement] 3, [DefenseDown] 5를 얻고, 이전 턴에 받은 체력 피해량 25당 [AttackDmgUp] 1을 얻음 (최대 5)
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1075].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: Gain 3 [Enhancement] and 5 [DefenseDown]; gain 1 [AttackDmgUp] for every 25 HP damage taken last turn (max 5)
   PL: Początek Tury: zyskaj 3 [Enhancement] i 5 [DefenseDown]; zyskaj 1 [AttackDmgUp] za każde 25 obrażeń PŻ otrzymanych w poprzedniej turze (maks. 5)
497. [Poczytalność i Panika [1076] — nazwa Paniki] 흥분
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1076].panicName
   limit: do 40 znaków
   EN: Fervor
   PL: Uniesienie
498. [Poczytalność i Panika [1076] — efekt niskiego morale] 턴 시작 시 [DefenseDown] 2을 얻고, 이전 턴에 받은 체력 피해량 30당 [AttackDmgUp] 1을 얻음 (최대 5)
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1076].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: Gain 2 [DefenseDown]; gain 1 [AttackDmgUp] for every 30 HP damage taken last turn (max 5)
   PL: Początek Tury: zyskaj 2 [DefenseDown]; zyskaj 1 [AttackDmgUp] za każde 30 obrażeń PŻ otrzymanych w poprzedniej turze (maks. 5)
499. [Poczytalność i Panika [1076] — efekt Paniki] 턴 시작 시 [Enhancement] 1, [DefenseDown] 3를 얻고, 이전 턴에 받은 체력 피해량 25당 [AttackDmgUp] 1을 얻음 (최대 5)
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1076].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [DefenseDown], [AttackDmgUp]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: Gain 1 [Enhancement] and 3 [DefenseDown]; gain 1 [AttackDmgUp] for every 25 HP damage taken last turn (max 5)
   PL: Początek Tury: zyskaj 1 [Enhancement] i 3 [DefenseDown]; zyskaj 1 [AttackDmgUp] za każde 25 obrażeń PŻ otrzymanych w poprzedniej turze (maks. 5)
500. [Poczytalność i Panika [1081] — nazwa Paniki] 돌이킬 수 없이 망가진 몸
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1081].panicName
   limit: do 40 znaków
   EN: Body Broken Beyond Repair
   PL: Nieodwracalnie Strzaskane Ciało
501. [Poczytalność i Panika [1081] — efekt niskiego morale] 턴 시작시 에즈라, 베스파에게 [Endurance] 2 부여, [Vulnerable] 1 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1081].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Endurance], [Vulnerable]
   znaczenie tagów: [Endurance] = 수비 위력 증가 / Defense Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [Vulnerable] and apply 2 [Endurance] to Ezra and Vespa
   PL: Początek Tury: zyskaj 1 [Vulnerable] oraz nałóż 2 [Endurance] na Ezrę i Vespę
502. [Poczytalność i Panika [1081] — efekt Paniki] [Vulnerable]을 1 얻고, ‘숨 고르기’를 사용함
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1081].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Gain 1 [Vulnerable] and use 'Steady the Breath'
   PL: Zyskaj 1 [Vulnerable] i użyj „Wyrównania Oddechu”
503. [Poczytalność i Panika [1082] — nazwa Paniki] 자기 방어 - 가면
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1082].panicName
   limit: do 40 znaków
   EN: Insecurity: Mask
   PL: Samoobrona - Maska
504. [Poczytalność i Panika [1082] — efekt niskiego morale] [Reduction] 1 얻음, [DefenseUp] 2 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1082].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction], [DefenseUp]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [Reduction] and 2 [DefenseUp]
   PL: Zyskaj 1 [Reduction] i 2 [DefenseUp]
505. [Poczytalność i Panika [1082] — efekt Paniki] [Reduction] 1 얻음, [DefenseUp] 3 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1082].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Reduction], [DefenseUp]
   znaczenie tagów: [Reduction] = 공격 위력 감소 / Attack Power Down; [DefenseUp] = 방어 레벨 증가 / Defense Level Up
   EN: Gain 1 [Reduction] and 3 [DefenseUp]
   PL: Zyskaj 1 [Reduction] i 3 [DefenseUp]
506. [Poczytalność i Panika [1083] — nazwa Paniki] 아뢰야
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1083].panicName
   limit: do 40 znaków
   EN: Alaya
   PL: Alaya
507. [Poczytalność i Panika [1083] — efekt niskiego morale] -
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1083].lowMoraleDescription
   limit: do 120 znaków
   EN: -
   PL: -
508. [Poczytalność i Panika [1083] — efekt Paniki] -
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1083].panicDescription
   (powtórzenie elementu 507 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
509. [Poczytalność i Panika [1080] — nazwa Paniki] 제 2차 연기전쟁의
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1080].panicName
   limit: do 40 znaków
   EN: Of the Second Smoke War
   PL: Z Drugiej Wojny Dymnej
510. [Poczytalność i Panika [1080] — efekt niskiego morale] 턴 시작 시, [Vulnerable] 1 얻음\n정신력 회복 효율 +2
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1080].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [Vulnerable]\nSP Heal Efficiency +2
   PL: Początek Tury: zyskaj 1 [Vulnerable]\nSkuteczność odzyskiwania SP +2
511. [Poczytalność i Panika [1080] — efekt Paniki] 턴 시작 시, [Vulnerable] 2, [ParryingResultUp] 2 얻음
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1080].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [ParryingResultUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [ParryingResultUp] = 합 위력 증가 / Clash Power Up
   EN: Turn Start: Gain 2 [Vulnerable] and 2 [ParryingResultUp]
   PL: Początek Tury: zyskaj 2 [Vulnerable] i 2 [ParryingResultUp]
512. [Poczytalność i Panika [1084] — nazwa Paniki] 모조된 아비
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1084].panicName
   limit: do 40 znaków
   EN: Imitation of a Father
   PL: Imitacja Ojca
513. [Poczytalność i Panika [1084] — efekt niskiego morale] - 턴 시작 시, [Combustion] 5, [Laceration] 5 얻음\n- 수감자 료슈에게 받는 피해량 +10%
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1084].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: - Turn Start: Gain 5 [Combustion] and 5 [Laceration]\n- Take +10% damage from Sinner Ryōshū
   PL: - Początek Tury: zyskaj 5 [Combustion] i 5 [Laceration]\n- Otrzymywane obrażenia od Grzeszniczki Ryōshū +10%
514. [Poczytalność i Panika [1084] — efekt Paniki] - 턴 시작 시, [Combustion] 5, [Combustion] 횟수 3, [Laceration] 5, [Laceration] 횟수 3 얻음\n- 수감자 료슈에게 받는 피해량 +20%
   źródło: PanicInfo-a1c9p3.json :: dataList[id=1084].panicDescription
   limit: do 180 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed
   EN: - Turn Start: Gain 5 [Combustion], +3 [Combustion] Count, 5 [Laceration], and +3 [Laceration] Count\n- Take +20% damage from Sinner Ryōshū
   PL: - Początek Tury: zyskaj 5 [Combustion], +3 Licznika [Combustion], 5 [Laceration] i +3 Licznika [Laceration]\n- Otrzymywane obrażenia od Grzeszniczki Ryōshū +20%

## Poczytalność i Panika: PanicInfo-cultivation
- plik gry: `PanicInfo-cultivation.json`

515. [Poczytalność i Panika [1059] — nazwa Paniki] 고삐 풀린 말
   źródło: PanicInfo-cultivation.json :: dataList[id=1059].panicName
   limit: do 40 znaków
   EN: Unbridled Steed
   PL: Rumak bez Uzdy
516. [Poczytalność i Panika [1059] — efekt niskiego morale] 턴 시작 시, [AttackUp] 2, [Vulnerable] 1을 얻음
   źródło: PanicInfo-cultivation.json :: dataList[id=1059].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [Vulnerable]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 2 [AttackUp] and 1 [Vulnerable]
   PL: Początek Tury: zyskaj 2 [AttackUp] i 1 [Vulnerable]
517. [Poczytalność i Panika [1059] — efekt Paniki] 턴 시작 시, 최대 속도 1 증가, [AttackUp] 2, [Vulnerable] 2를 얻음
   źródło: PanicInfo-cultivation.json :: dataList[id=1059].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [Vulnerable]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: gain 1 max Speed, gain 2 [AttackUp], and 2 [Vulnerable]
   PL: Początek Tury: Maks. Szybkość +1, zyskaj 2 [AttackUp] i 2 [Vulnerable]
518. [Poczytalność i Panika [1060] — nazwa Paniki] 취수야객
   źródło: PanicInfo-cultivation.json :: dataList[id=1060].panicName
   limit: do 50 znaków
   EN: Night Drifter of the Drunken Palm
   PL: Nocny Wędrowiec Pijanej Dłoni
519. [Poczytalność i Panika [1060] — efekt niskiego morale] 가시춘에 의한 받는 피해량 +10%, 반격으로 주는 피해량 +30%
   źródło: PanicInfo-cultivation.json :: dataList[id=1060].lowMoraleDescription
   limit: do 120 znaków
   EN: Take +10% damage from Jia Xichun; deal +30% damage with Counterattacks
   PL: Otrzymywane obrażenia od Jia Xichun +10%; obrażenia Kontrataków +30%
520. [Poczytalność i Panika [1060] — efekt Paniki] 최종 위력 1 증가, 가시춘에 의한 받는 피해량 +20%, 반격으로 주는 피해량 +50%
   źródło: PanicInfo-cultivation.json :: dataList[id=1060].panicDescription
   limit: do 120 znaków
   EN: Final Power +1; take +20% damage from Jia Xichun; deal +50% damage with Counterattacks
   PL: Moc Końcowa +1; otrzymywane obrażenia od Jia Xichun +20%; obrażenia Kontrataków +50%
521. [Poczytalność i Panika [1041] — nazwa Paniki] 암완
   źródło: PanicInfo-cultivation.json :: dataList[id=1041].panicName
   limit: do 40 znaków
   EN: Shadow Arm
   PL: Ramię Cienia
522. [Poczytalność i Panika [1041] — efekt niskiego morale] 합 위력 -1, 받는 피해량 -10%
   źródło: PanicInfo-cultivation.json :: dataList[id=1041].lowMoraleDescription
   limit: do 120 znaków
   EN: Clash Power -1; take -10% damage
   PL: Moc Starcia -1; otrzymywane obrażenia -10%
523. [Poczytalność i Panika [1041] — efekt Paniki] 합 위력 -2, 받는 피해량 -20%
   źródło: PanicInfo-cultivation.json :: dataList[id=1041].panicDescription
   limit: do 120 znaków
   EN: Clash Power -2; take -20% damage
   PL: Moc Starcia -2; otrzymywane obrażenia -20%

## Poczytalność i Panika: PanicInfo-exme
- plik gry: `PanicInfo-exme.json`

524. [Poczytalność i Panika [1092] — nazwa Paniki] 뒤섞인 기억
   źródło: PanicInfo-exme.json :: dataList[id=1092].panicName
   limit: do 40 znaków
   EN: Jumbled Memories
   PL: Pomieszane Wspomnienia
525. [Poczytalność i Panika [1092] — efekt niskiego morale] 턴 시작 시 [AttackUp] 1~3, [DefenseDown] 1~3 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1092].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: Gain 1~3 [AttackUp] and 1~3 [DefenseDown]
   PL: Początek Tury: zyskaj 1~3 [AttackUp] i 1~3 [DefenseDown]
526. [Poczytalność i Panika [1092] — efekt Paniki] 턴 시작 시 [AttackUp] 1~5, [DefenseDown] 1~5 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1092].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackUp], [DefenseDown]
   znaczenie tagów: [AttackUp] = 공격 레벨 증가 / Offense Level Up; [DefenseDown] = 방어 레벨 감소 / Defense Level Down
   EN: Turn Start: Gain 1~5 [AttackUp] and 1~5 [DefenseDown]
   PL: Początek Tury: zyskaj 1~5 [AttackUp] i 1~5 [DefenseDown]
527. [Poczytalność i Panika [1093] — nazwa Paniki] 원망
   źródło: PanicInfo-exme.json :: dataList[id=1093].panicName
   limit: do 40 znaków
   EN: Resentment
   PL: Żal i Uraza
528. [Poczytalność i Panika [1093] — efekt niskiego morale] - 턴 시작 시 [Enhancement] 1, [Disarming] 1 얻음\n- 턴 종료 시 다음 턴에 [Agility] 2 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1093].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Disarming], [Agility]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Disarming] = 수비 위력 감소 / Defense Power Down; [Agility] = 신속 / Haste
   EN: - Turn Start: Gain 1 [Enhancement] and 1 [Disarming]\n- Turn End: Gain 2 [Agility] next turn
   PL: - Początek Tury: zyskaj 1 [Enhancement] i 1 [Disarming]\n- Koniec Tury: zyskaj 2 [Agility] w następnej turze
529. [Poczytalność i Panika [1093] — efekt Paniki] - 턴 시작 시 [Enhancement] 2, [Disarming] 2 얻음\n- 턴 종료 시 다음 턴에 [Agility] 2 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1093].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Enhancement], [Disarming], [Agility]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Disarming] = 수비 위력 감소 / Defense Power Down; [Agility] = 신속 / Haste
   EN: - Turn Start: Gain 2 [Enhancement] and 2 [Disarming]\n- Turn End: Gain 2 [Agility] next turn
   PL: - Początek Tury: zyskaj 2 [Enhancement] i 2 [Disarming]\n- Koniec Tury: zyskaj 2 [Agility] w następnej turze
530. [Poczytalność i Panika [1094] — nazwa Paniki] 정보 집착
   źródło: PanicInfo-exme.json :: dataList[id=1094].panicName
   limit: do 40 znaków
   EN: Intelligence Obsession
   PL: Obsesja Wywiadowcza
531. [Poczytalność i Panika [1094] — efekt niskiego morale] - [TakePicture]을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +10%\n- 턴 시작 시 [Vulnerable] 1 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1094].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [TakePicture], [Vulnerable]
   znaczenie tagów: [TakePicture] = 정보 취득 / Intelligence Gathering; [Vulnerable] = 취약 / Fragile
   EN: - In a Clash against targets that have [TakePicture], Base Power +1 and deal +10% damage\n- Turn Start: Gain 1 [Vulnerable]
   PL: - W Starciu z celami mającymi [TakePicture]: Moc Bazowa +1 i zadawane obrażenia +10%\n- Początek Tury: zyskaj 1 [Vulnerable]
532. [Poczytalność i Panika [1094] — efekt Paniki] - [TakePicture]을 보유한 대상과 합 진행 시 기본 위력 +1, 가하는 피해량 +20%\n- 턴 시작 시 [Vulnerable] 2 얻음
   źródło: PanicInfo-exme.json :: dataList[id=1094].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [TakePicture], [Vulnerable]
   znaczenie tagów: [TakePicture] = 정보 취득 / Intelligence Gathering; [Vulnerable] = 취약 / Fragile
   EN: - In a Clash against targets that have [TakePicture], Base Power +1 and deal +20% damage\n- Turn Start: Gain 2 [Vulnerable]
   PL: - W Starciu z celami mającymi [TakePicture]: Moc Bazowa +1 i zadawane obrażenia +20%\n- Początek Tury: zyskaj 2 [Vulnerable]
533. [Poczytalność i Panika [1095] — nazwa Paniki] 가라앉은 회한
   źródło: PanicInfo-exme.json :: dataList[id=1095].panicName
   limit: do 40 znaków
   EN: Deep-rooted Regret
   PL: Głęboko Zakorzeniony Żal
534. [Poczytalność i Panika [1095] — efekt niskiego morale] - 턴 시작 시 [AttackDmgDown] 2 얻고 자신의 체력 40 회복
   źródło: PanicInfo-exme.json :: dataList[id=1095].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgDown]
   znaczenie tagów: [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: - Turn Start: Gain 2 [AttackDmgDown] and heal 40 HP
   PL: - Początek Tury: zyskaj 2 [AttackDmgDown] i ulecz 40 PŻ
535. [Poczytalność i Panika [1095] — efekt Paniki] - 턴 시작 시 [AttackDmgDown] 3 얻고 자신의 체력 60 회복
   źródło: PanicInfo-exme.json :: dataList[id=1095].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgDown]
   znaczenie tagów: [AttackDmgDown] = 피해량 감소 / Damage Down
   EN: - Turn Start: Gain 3 [AttackDmgDown] and heal 60 HP
   PL: - Początek Tury: zyskaj 3 [AttackDmgDown] i ulecz 60 PŻ
536. [Poczytalność i Panika [1096] — nazwa Paniki] 현상된 기억
   źródło: PanicInfo-exme.json :: dataList[id=1096].panicName
   limit: do 40 znaków
   EN: Developed Memories
   PL: Wywołane Wspomnienia
537. [Poczytalność i Panika [1096] — efekt niskiego morale] [Vulnerable] 1 얻음, 피해량 +10%, 크리티컬 피해량 +15%
   źródło: PanicInfo-exme.json :: dataList[id=1096].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Gain 1 [Vulnerable], deal +10% damage, and deal +15% damage on Critical Hit
   PL: Zyskaj 1 [Vulnerable], zadawane obrażenia +10%, obrażenia krytyczne +15%
538. [Poczytalność i Panika [1096] — efekt Paniki] [Vulnerable] 2 얻음, 피해량 +10%, 크리티컬 피해량 +30%, <color=#ff6000><mark color=#ff000040><b><u>본국궁[살] - 살 날리기의 코인으로 부여하는 효과 2배로 부여</color></mark></b></u>
   źródło: PanicInfo-exme.json :: dataList[id=1096].panicDescription
   limit: do 220 znaków
   tokeny: zachowaj dokładnie: <color=#ff6000>, <mark color=#ff000040>, <b>, <u>, </color>, </mark>, </b>, </u>, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: Gain 2 [Vulnerable], deal +10% damage, deal +30% damage on Critical Hit, and <color=#ff6000><mark color=#ff000040><b><u>double the effects inflicted by the Coins of the "Bow of the Homeland [Sal] - Arrowloose" Skill</color></mark></b></u>
   PL: Zyskaj 2 [Vulnerable], zadawane obrażenia +10%, obrażenia krytyczne +30% oraz <color=#ff6000><mark color=#ff000040><b><u>podwój efekty nakładane przez Monety umiejętności „Łuk Ojczyzny [Sal] - Spuszczenie Strzały”</u></b></mark></color>

## Poczytalność i Panika: PanicInfo-fools
- plik gry: `PanicInfo-fools.json`

539. [Poczytalność i Panika [1037] — nazwa Paniki] 사탕
   źródło: PanicInfo-fools.json :: dataList[id=1037].panicName
   limit: do 40 znaków
   EN: Candy
   PL: Cukierek
540. [Poczytalność i Panika [1037] — efekt niskiego morale] [CandyForCharon]을 가지고 있는 인격과 합 진행 시, 합 위력 +3, 그 외의 인격과 합 진행시, 합 위력 -1
   źródło: PanicInfo-fools.json :: dataList[id=1037].lowMoraleDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [CandyForCharon]
   znaczenie tagów: [CandyForCharon] = 사탕? / Candy?
   EN: When Clashing against Identities with [CandyForCharon], Clash Power +3; when clashing against other Identities, Clash Power -1
   PL: W Starciu z Tożsamościami mającymi [CandyForCharon]: Moc Starcia +3; w Starciu z pozostałymi Tożsamościami: Moc Starcia -1
541. [Poczytalność i Panika [1037] — efekt Paniki] [CandyForCharon]을 가지고 있는 인격과 합 진행 시, 합 위력 +5, 그 외의 인격과 합 진행시, 합 위력 -2
   źródło: PanicInfo-fools.json :: dataList[id=1037].panicDescription
   limit: do 170 znaków
   tokeny: zachowaj dokładnie: [CandyForCharon]
   znaczenie tagów: [CandyForCharon] = 사탕? / Candy?
   EN: When Clashing against Identities with [CandyForCharon], Clash Power +5; when clashing against other Identities, Clash Power -2
   PL: W Starciu z Tożsamościami mającymi [CandyForCharon]: Moc Starcia +5; w Starciu z pozostałymi Tożsamościami: Moc Starcia -2

## Poczytalność i Panika: PanicInfo-hidden
- plik gry: `PanicInfo-hidden.json`

542. [Poczytalność i Panika [1063] — nazwa Paniki] 사탕
   źródło: PanicInfo-hidden.json :: dataList[id=1063].panicName
   (powtórzenie elementu 539 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
543. [Poczytalność i Panika [1063] — efekt niskiego morale] [GiveMeCandy]을 가지고 있는 인격과 합 진행 시, 합 위력 +3, 그 외의 인격과 합 진행시, 합 위력 -1
   źródło: PanicInfo-hidden.json :: dataList[id=1063].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [GiveMeCandy]
   znaczenie tagów: [GiveMeCandy] = 사탕 / Candy
   EN: When Clashing against Identities with [GiveMeCandy], Clash Power +3; when clashing against other Identities, Clash Power -1
   PL: W Starciu z Tożsamościami mającymi [GiveMeCandy]: Moc Starcia +3; w Starciu z pozostałymi Tożsamościami: Moc Starcia -1
544. [Poczytalność i Panika [1063] — efekt Paniki] [GiveMeCandy]을 가지고 있는 인격과 합 진행 시, 합 위력 +5, 그 외의 인격과 합 진행시, 합 위력 -2
   źródło: PanicInfo-hidden.json :: dataList[id=1063].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: [GiveMeCandy]
   znaczenie tagów: [GiveMeCandy] = 사탕 / Candy
   EN: When Clashing against Identities with [GiveMeCandy], Clash Power +5; when clashing against other Identities, Clash Power -2
   PL: W Starciu z Tożsamościami mającymi [GiveMeCandy]: Moc Starcia +5; w Starciu z pozostałymi Tożsamościami: Moc Starcia -2

## Poczytalność i Panika: PanicInfo-mowe
- plik gry: `PanicInfo-mowe.json`

545. [Poczytalność i Panika [1025] — nazwa Paniki] 흡혈 갈망
   źródło: PanicInfo-mowe.json :: dataList[id=1025].panicName
   limit: do 40 znaków
   EN: Bloodthirst
   PL: Żądza Krwi
546. [Poczytalność i Panika [1025] — efekt niskiego morale] 턴 시작 시 [Vulnerable], [AttackDmgUp] 1 얻음
   źródło: PanicInfo-mowe.json :: dataList[id=1025].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 1 [Vulnerable] and [AttackDmgUp]
   PL: Początek Tury: zyskaj po 1 [Vulnerable] i [AttackDmgUp]
547. [Poczytalność i Panika [1025] — efekt Paniki] 턴 시작 시 [Vulnerable], [AttackDmgUp] 2 얻음.
   źródło: PanicInfo-mowe.json :: dataList[id=1025].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [AttackDmgUp]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [AttackDmgUp] = 피해량 증가 / Damage Up
   EN: Turn Start: gain 2 [Vulnerable] and [AttackDmgUp]
   PL: Początek Tury: zyskaj po 2 [Vulnerable] i [AttackDmgUp].

## Poczytalność i Panika: PanicInfo-pilgrimage
- plik gry: `PanicInfo-pilgrimage.json`

548. [Poczytalność i Panika [1061] — nazwa Paniki] 선의의 마음
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1061].panicName
   limit: do 40 znaków
   EN: Heart of Compassion
   PL: Serce Współczucia
549. [Poczytalność i Panika [1061] — efekt niskiego morale] - 가하는 피해량이 (대상이 보유한 [NervousImpairment]/2)%만큼 증가 (최대 15%)\n턴 시작 시, [AttackDmgUp] 1, [Vulnerable] 2 얻음
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1061].lowMoraleDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [NervousImpairment], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: - Deal +([NervousImpairment] on target / 2)% damage (max 15%)\n- Turn Start: gain 1 [AttackDmgUp] and 2 [Vulnerable]
   PL: - Zadawane obrażenia +([NervousImpairment] na celu / 2)% (maks. 15%)\n- Początek Tury: zyskaj 1 [AttackDmgUp] i 2 [Vulnerable]
550. [Poczytalność i Panika [1061] — efekt Paniki] - 가하는 피해량이 (대상이 보유한 [NervousImpairment])%만큼 증가 (최대 30%)\n- 턴 시작 시, [AttackDmgUp] 2, [Vulnerable] 3 얻음
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1061].panicDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: \n, [NervousImpairment], [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [NervousImpairment] = 신경 손상 / Nervous Impairment; [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: - Deal +([NervousImpairment] on target)% damage (max 30%)\n- Turn Start: gain 2 [AttackDmgUp] and 3 [Vulnerable]
   PL: - Zadawane obrażenia +([NervousImpairment] na celu)% (maks. 30%)\n- Początek Tury: zyskaj 2 [AttackDmgUp] i 3 [Vulnerable]
551. [Poczytalność i Panika [1062] — nazwa Paniki] 동족의 부름
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1062].panicName
   limit: do 40 znaków
   EN: Call of the Bloodkin
   PL: Zew Krewniaków
552. [Poczytalność i Panika [1062] — efekt niskiego morale] 턴 종료시 자신의 체력을 3% 소모하여 모든 아군에게 [Enhancement] 1, [Vulnerable] 1 부여
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1062].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Enhancement], [Vulnerable]
   znaczenie tagów: [Enhancement] = 공격 위력 증가 / Attack Power Up; [Vulnerable] = 취약 / Fragile
   EN: Turn End: consume 3% HP to apply 1 [Enhancement] and 1 [Vulnerable] to all allies
   PL: Koniec Tury: zużyj 3% PŻ, aby nałożyć po 1 [Enhancement] i [Vulnerable] na wszystkich sojuszników
553. [Poczytalność i Panika [1062] — efekt Paniki] 턴 종료시 자신의 체력을 5% 소모하여 [Vulnerable] 1을 얻고 모든 아군에게 [Enhancement] 1, [Vulnerable] 1 부여
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1062].panicDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Enhancement]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Enhancement] = 공격 위력 증가 / Attack Power Up
   EN: Turn End: consume 5% HP and gain 1 [Vulnerable] to apply 1 [Enhancement] and 1 [Vulnerable] to all allies
   PL: Koniec Tury: zużyj 5% PŻ i zyskaj 1 [Vulnerable], aby nałożyć po 1 [Enhancement] i [Vulnerable] na wszystkich sojuszników
554. [Poczytalność i Panika [1064] — nazwa Paniki] 군체 의식
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1064].panicName
   limit: do 40 znaków
   EN: Hive Mind
   PL: Świadomość Roju
555. [Poczytalność i Panika [1064] — efekt niskiego morale] 모든 내성이 보통 상태가 됨
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1064].lowMoraleDescription
   limit: do 120 znaków
   EN: All Resistances change to 'Normal'
   PL: Wszystkie odporności zmieniają się na „Zwykła”
556. [Poczytalność i Panika [1064] — efekt Paniki] 모든 내성이 보통 상태가 됨\n스킬로 받는 [Combustion], [Laceration], [Vibration], [Burst] 위력을 2배로 받음
   źródło: PanicInfo-pilgrimage.json :: dataList[id=1064].panicDescription
   limit: do 190 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Laceration], [Vibration], [Burst]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Laceration] = 출혈 / Bleed; [Vibration] = 진동 / Tremor; [Burst] = 파열 / Rupture
   EN: All Resistances change to 'Normal'\nDouble the amount of [Combustion], [Laceration], [Vibration], and [Burst] Potency gained due to Skill effects
   PL: Wszystkie odporności zmieniają się na „Zwykła”\nPodwaja ilość Siły [Combustion], [Laceration], [Vibration] oraz [Burst] zyskiwanej z efektów umiejętności

## Poczytalność i Panika: PanicInfo-schema
- plik gry: `PanicInfo-schema.json`

557. [Poczytalność i Panika [1126] — nazwa Paniki] 안하무인
   źródło: PanicInfo-schema.json :: dataList[id=1126].panicName
   limit: do 40 znaków
   EN: Overbearing Hubris
   PL: Zuchwała Buta
558. [Poczytalność i Panika [1126] — efekt niskiego morale] 턴 시작 시 [AttackDmgUp] 1, [Vulnerable] 1을 얻음
   źródło: PanicInfo-schema.json :: dataList[id=1126].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 1 [AttackDmgUp] and 1 [Vulnerable]
   PL: Początek Tury: zyskaj 1 [AttackDmgUp] i 1 [Vulnerable]
559. [Poczytalność i Panika [1126] — efekt Paniki] 턴 시작 시 [AttackDmgUp] 2, [Vulnerable] 2를 얻음
   źródło: PanicInfo-schema.json :: dataList[id=1126].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [AttackDmgUp], [Vulnerable]
   znaczenie tagów: [AttackDmgUp] = 피해량 증가 / Damage Up; [Vulnerable] = 취약 / Fragile
   EN: Turn Start: Gain 2 [AttackDmgUp] and 2 [Vulnerable]
   PL: Początek Tury: zyskaj 2 [AttackDmgUp] i 2 [Vulnerable]

## Poczytalność i Panika: PanicInfo-tkt
- plik gry: `PanicInfo-tkt.json`

560. [Poczytalność i Panika [1024] — nazwa Paniki] 어긋난 단결
   źródło: PanicInfo-tkt.json :: dataList[id=1024].panicName
   limit: do 40 znaków
   EN: Broken Unity
   PL: Złamana Jedność
561. [Poczytalność i Panika [1024] — efekt niskiego morale] [Vulnerable] 1 얻음. 피격시, 자신의 [Vibration] 횟수 1 증가. (최대 3회)
   źródło: PanicInfo-tkt.json :: dataList[id=1024].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Vibration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Vibration] = 진동 / Tremor
   EN: Gain 1 [Vulnerable]. Gain +1 [Vibration] Count when hit. (3 times max)
   PL: Zyskaj 1 [Vulnerable]. Przy otrzymaniu trafienia zyskaj +1 Licznika [Vibration] (maks. 3 razy)
562. [Poczytalność i Panika [1024] — efekt Paniki] [Vulnerable] 2 얻음. 피격 시, 자신의 [Vibration] 횟수 2 증가. (최대 3회)
   źródło: PanicInfo-tkt.json :: dataList[id=1024].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: [Vulnerable], [Vibration]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Vibration] = 진동 / Tremor
   EN: Gain 2 [Vulnerable]. Gain +2 [Vibration] Count when hit. (3 times max)
   PL: Zyskaj 2 [Vulnerable]. Przy otrzymaniu trafienia zyskaj +2 Licznika [Vibration] (maks. 3 razy)

## Poczytalność i Panika: PanicInfo-twth
- plik gry: `PanicInfo-twth.json`

563. [Poczytalność i Panika [1088] — nazwa Paniki] 떨어지는 영감
   źródło: PanicInfo-twth.json :: dataList[id=1088].panicName
   limit: do 40 znaków
   EN: Faltering Inspiration
   PL: Gasnące Natchnienie
564. [Poczytalność i Panika [1088] — efekt niskiego morale] - 자신이 공격하는 대상에게 <color=#ff0000>찢긴 색채</color>가 있으면, 피해량 10% 증가\n- [Vulnerable] 1 얻음
   źródło: PanicInfo-twth.json :: dataList[id=1088].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: - If target this unit attacks has <color=#ff0000>Mauled Color</color>, deal +10% damage \n- Gain 1 [Vulnerable]
   PL: - Jeśli atakowany cel ma <color=#ff0000>Rozszarpaną Barwę</color>, zadawane obrażenia +10%\n- Zyskaj 1 [Vulnerable]
565. [Poczytalność i Panika [1088] — efekt Paniki] - 자신이 공격하는 대상에게 <color=#ff0000>찢긴 색채</color>가 있으면, 피해량 20% 증가\n- [Vulnerable] 2 얻음
   źródło: PanicInfo-twth.json :: dataList[id=1088].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: - If target this unit attacks has <color=#ff0000>Mauled Color</color>, deal +20% damage \n- Gain 2 [Vulnerable]
   PL: - Jeśli atakowany cel ma <color=#ff0000>Rozszarpaną Barwę</color>, zadawane obrażenia +20%\n- Zyskaj 2 [Vulnerable]
566. [Poczytalność i Panika [1090] — nazwa Paniki] 충동적인 채색
   źródło: PanicInfo-twth.json :: dataList[id=1090].panicName
   limit: do 40 znaków
   EN: Coloriage Impulsif
   PL: Coloriage Impulsif
567. [Poczytalność i Panika [1090] — efekt niskiego morale] - 자신이 공격하는 대상이 보유한 <color=#ff0000>부정적인 효과</color> 1개당, 피해량 +2.5% (최대 15%)\n- [Vulnerable] 1 얻음
   źródło: PanicInfo-twth.json :: dataList[id=1090].lowMoraleDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: - Deal +2.5% damage for every <color=#ff0000>type of negative effect</color> on target this unit attacks (max 15%)\n- Gain 1 [Vulnerable]
   PL: - Zadawane obrażenia +2,5% za każdy <color=#ff0000>rodzaj efektu negatywnego</color> na atakowanym celu (maks. 15%)\n- Zyskaj 1 [Vulnerable]
568. [Poczytalność i Panika [1090] — efekt Paniki] - 자신이 공격하는 대상이 보유한 <color=#ff0000>부정적인 효과</color> 1개당, 피해량 +5% (최대 30%)\n- [Vulnerable] 2 얻음
   źródło: PanicInfo-twth.json :: dataList[id=1090].panicDescription
   limit: do 150 znaków
   tokeny: zachowaj dokładnie: <color=#ff0000>, </color>, \n, [Vulnerable]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile
   EN: - Deal +5% damage for every <color=#ff0000>type of negative effect</color> on target this unit attacks (max 30%)\n- Gain 2 [Vulnerable]
   PL: - Zadawane obrażenia +5% za każdy <color=#ff0000>rodzaj efektu negatywnego</color> na atakowanym celu (maks. 30%)\n- Zyskaj 2 [Vulnerable]

## Poczytalność i Panika: PanicInfo-walpu10
- plik gry: `PanicInfo-walpu10.json`

569. [Poczytalność i Panika [1123] — nazwa Paniki] 새벽 사무소
   źródło: PanicInfo-walpu10.json :: dataList[id=1123].panicName
   (powtórzenie elementu 179 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
570. [Poczytalność i Panika [1123] — efekt niskiego morale] [Combustion]이 있는 적에게 가하는 피해량 -5%\n[Vibration]이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: PanicInfo-walpu10.json :: dataList[id=1123].lowMoraleDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Deal -5% damage to enemies that have [Combustion]\n+5% to Stagger Threshold raised against enemies that have [Vibration]
   PL: Zadawane obrażenia wrogom z [Combustion] -5%\nObrażenia Oszołomienia przeciw wrogom z [Vibration] +5%
571. [Poczytalność i Panika [1123] — efekt Paniki] [Combustion]이 있는 적에게 가하는 피해량 -10%\n[Vibration]이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: PanicInfo-walpu10.json :: dataList[id=1123].panicDescription
   limit: do 160 znaków
   tokeny: zachowaj dokładnie: \n, [Combustion], [Vibration]
   znaczenie tagów: [Combustion] = 화상 / Burn; [Vibration] = 진동 / Tremor
   EN: Deal -10% damage to enemies that have [Combustion]\n+10% to Stagger Threshold raised against enemies that have [Vibration]
   PL: Zadawane obrażenia wrogom z [Combustion] -10%\nObrażenia Oszołomienia przeciw wrogom z [Vibration] +10%
572. [Poczytalność i Panika [1124] — nazwa Paniki] 쐐기 사무소
   źródło: PanicInfo-walpu10.json :: dataList[id=1124].panicName
   (powtórzenie elementu 230 — nie wpisuj tu nic, tłumaczenie dziedziczy się samo)
573. [Poczytalność i Panika [1124] — efekt niskiego morale] 크리티컬 피해량 -5%\n[Vibration]이 있는 적에게 가하는 흐트러짐 피해량 +5%
   źródło: PanicInfo-walpu10.json :: dataList[id=1124].lowMoraleDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal -5% damage on Critical Hit\n+5% to Stagger Threshold raised against enemies that have [Vibration]
   PL: Obrażenia krytyczne -5%\nObrażenia Oszołomienia przeciw wrogom z [Vibration] +5%
574. [Poczytalność i Panika [1124] — efekt Paniki] 크리티컬 피해량 -10%\n[Vibration]이 있는 적에게 가하는 흐트러짐 피해량 +10%
   źródło: PanicInfo-walpu10.json :: dataList[id=1124].panicDescription
   limit: do 140 znaków
   tokeny: zachowaj dokładnie: \n, [Vibration]
   znaczenie tagów: [Vibration] = 진동 / Tremor
   EN: Deal -10% damage on Critical Hit\n+10% to Stagger Threshold raised against enemies that have [Vibration]
   PL: Obrażenia krytyczne -10%\nObrażenia Oszołomienia przeciw wrogom z [Vibration] +10%
575. [Poczytalność i Panika [1125] — nazwa Paniki] 밀랍날개
   źródło: PanicInfo-walpu10.json :: dataList[id=1125].panicName
   limit: do 40 znaków
   EN: Waxen Pinion
   PL: Woskowe Skrzydło
576. [Poczytalność i Panika [1125] — efekt niskiego morale] [Vulnerable] 1 얻음\n[Combustion]이 있는 적에게 가하는 피해량 +10%
   źródło: PanicInfo-walpu10.json :: dataList[id=1125].lowMoraleDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [Combustion]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Combustion] = 화상 / Burn
   EN: Gain 1 [Vulnerable]\nDeal +10% damage to enemies that have [Combustion]
   PL: Zyskaj 1 [Vulnerable]\nZadawane obrażenia wrogom z [Combustion] +10%
577. [Poczytalność i Panika [1125] — efekt Paniki] [Vulnerable] 1 얻음\n[Combustion]이 있는 적에게 가하는 피해량 +25%
   źródło: PanicInfo-walpu10.json :: dataList[id=1125].panicDescription
   limit: do 120 znaków
   tokeny: zachowaj dokładnie: \n, [Vulnerable], [Combustion]
   znaczenie tagów: [Vulnerable] = 취약 / Fragile; [Combustion] = 화상 / Burn
   EN: Gain 1 [Vulnerable]\nDeal +25% damage to enemies that have [Combustion]
   PL: Zyskaj 1 [Vulnerable]\nZadawane obrażenia wrogom z [Combustion] +25%

## Poczytalność i Panika: PanicInfo-walpu5
- plik gry: `PanicInfo-walpu5.json`

578. [Poczytalność i Panika [1035] — nazwa Paniki] 교단
   źródło: PanicInfo-walpu5.json :: dataList[id=1035].panicName
   limit: do 40 znaków
   EN: The Church
   PL: Kościół
